# SV — Commercial-legal — AML compliance: D.L. 426 sujetos obligados, compliance program, due diligence, reporting and sanctions (C10)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador anti-money-laundering compliance layer
under the CURRENT regime — **Ley Contra el Lavado de Dinero y de Activos,
D.L. N° 426 (2025)** — as rebased by the W12 evidence (EVID-241..249): the
*sujeto obligado* (obligated subject) classification of Art. 7 with its TEN
named categories — financial institutions, D.L. 339 credit associations,
systematic lenders, casinos and games of chance, real-estate intermediaries,
precious-metals/-stones traders, activity-listed professionals (lawyers,
notaries, accountants, auditors), transporters of money or values,
digital-asset and bitcoin service providers, and political parties — an
activity-triggered model under which an ORDINARY TRADING OR MANUFACTURING
COMPANY IS NOT a per-se subject, with dynamic inclusion/exclusion via
UIF→CIPLAFT (Art. 8) and the supervisor-routing table of Arts. 12-13; the
compliance-program chassis of Art. 9 and the kept UIF instructivo
(Acuerdo 380) Arts. 3-8 — registration before supervisor AND UIF with data
currency, annual work plans, risk-based approach, annual training, the
internal-unusual-report analysis pipeline; the due-diligence ladder of
Arts. 15-19 (simplified/standard/enhanced) with the kept instructivo's
methodology (Arts. 10-21) — *beneficiario final* (ultimate beneficial
owner) to the natural person at the law's ≥25% participation, PEP national
and foreign catalogs with the 5-year post-cesation tail, nominative-only
records, KYC-refusal abstention, and the US$1,000 low-value-account
carve-out; the officer architecture — *Oficialía de Cumplimiento*
(compliance office) vs APNFD *Encargado de Cumplimiento* (compliance
custodian), the *Comité de Prevención* (prevention committee, ≥3 members)
of Art. 23, and the 15-*días hábiles* (business days) designation/change
notice; the reporting layer — the ROS clocks of Art. 24 (15 días hábiles
analysis + ONE same-length extension + 24-hour transmit clock,
amount-irrelevant, intelligence-only), the regulated-operations report of
Art. 25 (thresholds DELEGATED to the future reglamento; operative values
US$10,000-cash/US$25,000-other-media, single + monthly-cumulative +
mixed-payment decomposition, 5 días hábiles clocks, from the kept
instructivo Art. 51 as DATED CONFIG under the authority chain), the
financial-institutions' monthly aggregates (US$1,000 wires / US$200
remesas, Art. 52), the APNFD GAFI triggers (US$3,000 casino /
US$10,000 metals-cash / US$10,000 lawyer-office, Art. 77), the kept
reglamento's red-flag catalogs (Arts. 12-18) as configurable detection
whose output is CASE CREATION, never auto-report, and the goAML/UIF
formats as an external-interface assumption; the uniform ≥15-year
retention of Art. 26 FEEDING the SOQ-28 canonical retention matrix of
`02_accounting-books.md` BY ID (SV-CML-FR-028 rows d1/d2 — never
restated); the US$15,000 border-declaration content note (Aduanas/DGA
interface kin, informational); the SMM-*sector-comercio*-indexed sanctions
of Arts. 29-39 (50-500 / 501-1000 SMM two-tier multas, officer-level
multas, suspension/cancellation, 5y/10y inhabilitación, 10-year
prescription with concealment anchor, law-level no-tip-off of Art. 28);
and the transitory adaptation windows of Arts. 55/56/58/60 as dated rows
with the pending-reglamento watch.

It does **not** cover: the retention matrix itself
(`02_accounting-books.md` SV-CML-FR-028/029 — this file only feeds the
AML-row applicability flag by id); the días-hábiles arithmetic (OWNED by
the fiscal-reporting wave's shared engine, SV-FREP-FR-203, consumed by
id); the dated SMM values (OWNED by the payroll wave's sidecar,
SV-PAY-FR-011/SV-PAY-FR-022, consumed by id); the dead 1998 law's content
(`15_` — historical-LB only, never current authority, §2); the criminal
title of D.L. 426 (Arts. 40+ — state-side); the state-side border
workflow itself (Art. 27 retained-declaration mechanics — informational
note, §3.8); the UIF's own platform mechanics (goAML channel —
external-interface assumption, §3.6/§5); or the e-invoicing DTE archive
tiers (e-invoicing wave, cited by id in `02`'s matrix). Dead-law citation
mapping and the pending new reglamento/instructivo are tracked as OQs
(§7).

## 2. Legal Basis

Authority order (binding, per master evidence index S5 and the W12 rebase,
**R28 chain**): the CURRENT AML law = **71_** — *Ley Contra el Lavado de
Dinero y de Activos*, D.L. N° 426 (7-oct-2025, D.O. N° 190 T.449
9-oct-2025; vigencia 8 days after publication ⇒ **effective 2025-10-17**,
Art. 62) — a WHOLESALE REPLACEMENT of the 1998 law (D.L. 498 = our 15_)
per Art. 61, NOT a reform. **15_ drops to historical-LB**: its Art. 9
law-text thresholds ($10,000/$25,000) and its whole article structure are
DEAD and are never cited as current authority anywhere in this file; they
survive only as the pre-2025-10-17 regime's historical rows (version
config, FR-193). Transition instrument (Art. 61 inciso 2): the OLD
reglamento = **17_** (D.E. N° 2, 21-ene-2000) and the OLD UIF instructivo
= **72_** (Acuerdo N° 380, 22-oct-2021, D.O. 205 T.433 27-oct-2021, as
reformed by Acuerdos 266-2023 and 476-2023 — the Sept-2023 consolidation)
REMAIN IN FORCE "mientras no se emitan el reglamento y el instructivo
correspondientes" — so for every NEW-law gap the operative authority
chain reads: **71_ law > 72_ kept instructivo > 17_ kept reglamento**
(normative-rank order for kept instruments; the specialty clause of Art.
59 makes the law prevail over any contrary provision). The kept
instruments cite the DEAD law's article numbers ("Art. 9 de la LCLDA",
"Art. 2 inc. 3°"); every such citation is re-anchored onto 71_'s structure
at synthesis (OQ-003), and where a kept instrument's value conflicts with
a direct 71_ rule the LAW governs (later-in-time + Art. 59) — the two
material divergences are recorded as working rulings: (i) ROS transmit
clock = 71_ Art. 24's 24 hours (displacing 72_ Art. 43's 5 días hábiles);
(ii) *beneficiario final* participation = 71_ Art. 15's ≥25% (displacing
72_ Arts. 12/20's 10% — LB-010).

**Threshold authority chain (R28/OQ-2 working ruling, binding on every
threshold and clock FR in §3.6):** 71_ Art. 25 DELEGATES the
regulated-operations report content and thresholds to the FUTURE
reglamento (GAFI-aligned); until it issues, the kept instructivo's values
(72_ Art. 51: US$10,000 cash / US$25,000 other-media, single +
monthly-cumulative; 72_ Art. 52: US$1,000 wire / US$200 remesa
aggregates) are the OPERATIVE values under the Art. 61 transitory. Every
such value is encoded as a DATED CONFIG row carrying its provenance chain
(instrument = 72_ article; delegation = 71_ Art. 25; supersession watch =
OQ-001) — NEVER hardcoded. The UIF's marco-legal page still hosted the
2023 instructivo and the 2000 reglamento at acquisition (2026-08-18),
10+ months past Art. 56's own instructivo deadline — no new reglamento
had issued (OQ-001 watch).

Verbatim text below is copied from the W12 evidence file
(EVID-241..249) and, where the evidence abbreviates, from the extraction
txts `sv/.extractions/71_Ley_LavadoActivos_DL426_2025.pdf.txt`,
`sv/.extractions/72_Instructivo_UIF_Acuerdo380_reform2023.pdf.txt` and
`sv/.extractions/17_Reglamento_Lavado_Activos.pdf.txt` (citable per
standing ruling; page pointers = txt PAGE markers). Provenance notes:
inter-word split artifacts of the text layer ("d e supervisar",
"perso nas") are silently rejoined — no other deviation; truncation
markers inside LB quotations label every omission explicitly. The SMM
feed: the sanctions units are "salarios mínimos mensuales del sector
comercio" (Arts. 34-35) where the payroll wave's 16_ decree prints the
sector as "Comercio y servicios" (monthly SMM US$408.80 from 2025-06-01)
— naming kin of SOQ-18 (recorded as a config note in FR-222, no new OQ).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 7: "Para efectos de la presente ley son sujetos obligados los siguientes: 1. Las instituciones financieras siguientes: a) Los bancos comerciales o estatales constituidos en El Salvador, sus oficinas en el extranjero y sus subsidiarias; b) Bancos de inversión; c) Las sociedades que, de conformidad con la ley, integran los conglomerados financieros; d) Las instituciones administradoras de fondos de ahorro previsional; e) Las sociedades de seguros, sus sucursales en el extranjero y las sucursales de sociedades de seguros extranjeras establecidas en el país; f) Las bolsas de valores, las casas de corredores de bolsa, las sociedades especializadas en el depósito y custodia de valores, las instituciones que presten servicios de carácter auxiliar al mercado bursátil, y los agentes especializados en valuación de valores; g) Los bancos y sociedades de ahorro y crédito, reguladas en el Decreto Legislativo número 849, de fecha 16 de febrero de 2000, publicado en el Diario Oficial número 65, Tomo 346, del 31 de marzo de 2000, y sus reformas; h) Las sociedades que ofrecen servicios complementarios a los servicios financieros de los integrantes del sistema financiero; i) Las sociedades administradoras u operadoras de sistemas de pagos y de liquidación de valores; j) El Fondo Social para la Vivienda y el Fondo Nacional de Vivienda Popular; k) Las casas de cambio de moneda extranjera; l) Las personas jurídicas que realizan operaciones de envío o recepción de dinero de manera sistemática, por cualquier medio, a nivel nacional e internacional; m) Las Sociedades Proveedores de Dinero Electrónico; n) Las titularizadoras; y, o) Las Gestoras de Fondos de Inversión. 2. Todas las asociaciones, sociedades, cajas de crédito, federaciones y confederaciones, reguladas en el decreto legislativo número 339, de fecha 6 de mayo de 1986, publicado en el Diario Oficial n.° 86, Tomo 291, del 14 de mayo de 1986, y sus reformas, y aquellas sociedades de ahorro y crédito reguladas en el Código de Comercio. 3. Personas jurídicas que operen dentro del territorio nacional, que exclusivamente se dediquen al otorgamiento sistemático de préstamos a personas naturales o jurídicas dentro o fuera del territorio nacional. 4. Casinos o empresas dedicadas a la explotación de juegos de suerte o azar. 5. Personas naturales y jurídicas que se dedican a la intermediación inmobiliaria o de bienes raíces, cuando éstos se involucran en transacciones para sus clientes para la compra y venta de bienes raíces. 6. Comerciantes de metales y piedras preciosas. 7. Abogados, notarios, contadores y auditores que, por la naturaleza de sus servicios profesionales, directa o indirectamente, realicen para sus clientes las actividades que se detallan a continuación: a) Compra y venta de bienes inmobiliarios; b) Administración del dinero, valores u otros activos del cliente; c) Administración de las cuentas bancarias, de ahorros o valores; d) Organización de contribuciones para la creación, operación o administración de empresas; o e) Creación, operación o administración de personas jurídicas u otras estructuras jurídicas, y compra y venta de entidades comerciales. 8. Personas jurídicas o naturales dedicadas al transporte de dinero o valores; 9. Proveedores de servicios de activos digitales y proveedores de servicios de bitcoin. 10. Partidos Políticos." Tail incisos: "En virtud de los estándares internacionales aplicables a los bancos centrales… el Banco Central de Reserva de El Salvador realizará su gestión de riesgo… de acuerdo con los lineamientos que dicte su Consejo Directivo…" and "Se considerarán sujetos de aplicación de medidas de debida diligencia, reportes de operaciones sospechosas, tentativa de operaciones sospechosas, de actividades sospechosas aquellas Organizaciones sin Fines de Lucro que se encuentren en un mayor nivel de exposición al riesgo…, de conformidad a las evaluaciones de riesgo que al efecto se realicen." | For the purposes of this law the obligated subjects are: 1. the financial institutions listed a)-o) (commercial/state banks and their foreign offices and subsidiaries; investment banks; financial-conglomerate companies; pension-saving fund administrators; insurance companies; stock exchanges, brokerage houses, securities deposit/custody societies, auxiliary market services, valuation agents; savings-and-loan banks and societies under D.L. 849-2000; complementary financial services societies; payment and securities-settlement system operators; FSV/FNVP; currency-exchange houses; legal persons systematically sending or receiving money; Electronic Money Provider Societies; securitization companies; Investment Fund Managers); 2. all associations, societies, credit unions, federations and confederations under D.L. 339-1986 and the savings-and-loan societies regulated in the Commercial Code; 3. legal persons operating exclusively in the systematic granting of loans; 4. casinos or gambling businesses; 5. real-estate intermediaries WHEN they engage in transactions for their clients for the purchase and sale of real estate; 6. traders in precious metals and stones; 7. lawyers, notaries, accountants and auditors who, by the nature of their professional services, directly or indirectly perform for clients: a) real-estate purchase/sale; b) management of the client's money, securities or other assets; c) management of bank, savings or securities accounts; d) organization of contributions for the creation, operation or administration of enterprises; or e) creation, operation or administration of legal persons or other legal structures, and purchase and sale of commercial entities; 8. natural or legal persons dedicated to the transport of money or values; 9. digital-asset service providers and bitcoin service providers; 10. political parties. The BCR manages its own risk per its Board's guidelines; OSFLs at higher risk exposure per risk evaluations are subjects of DD/ROS measures | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 7 pp.7-8 (EVID-242; txt PAGE 7-8) |
| LB-002 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 8: "La UIF propondrá al CIPLAFT la inclusión o exclusión de otros sujetos obligados cuando: a) Determine que existen o no riesgos en un sector o actividad específica posterior a la evaluación nacional o sectorial de riesgo o evaluación mutua desarrollada de acuerdo con los estándares internacionales. b) El ente de supervisión advierta que existen elementos suficientes y condiciones motivadas que expongan o no, al sector supervisado al riesgo de lavado de activos, sus delitos precedentes, financiamiento del terrorismo y financiamiento de la proliferación de armas de destrucción masiva. El CIPLAFT tendrá la facultad de recomendar a la autoridad competente, cuando así lo estime conveniente, las reformas de ley pertinentes." | The UIF will PROPOSE to the CIPLAFT the inclusion or exclusion of other obligated subjects when: a) it determines that risks exist or not in a specific sector or activity after a national or sectoral risk evaluation or mutual evaluation under international standards; b) the supervisor notes sufficient elements and motivated conditions exposing (or not) the supervised sector to ML/TF/PF risk. CIPLAFT may recommend the pertinent legal reforms to the competent authority | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 8 pp.8-9 (EVID-242; txt PAGE 8-9) |
| LB-003 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 12 (routing incisos): "La Superintendencia del Sistema Financiero será la encargada de supervisar a los sujetos obligados que señala el artículo 7 numeral 1 de la presente ley, sobre el cumplimiento de las obligaciones y medidas establecidas en ésta y otras leyes." "La Superintendencia del Sistema Financiero también supervisará a los sujetos comprendidos en el numeral 9 del artículo referido, siempre y cuando estos realicen operaciones con Bitcoin. Dichas entidades deberán cumplir con las Normas Técnicas que para tales efectos emita el Banco Central por medio de su Comité de Normas." "La autoridad competente según las leyes especiales vigentes… supervisará a las asociaciones, federaciones y confederaciones de ahorro y crédito específicas que señala el artículo 7 numeral 2 de la presente ley…" "La Superintendencia de Obligaciones Mercantiles supervisará a los sujetos obligados que señala el artículo 7 numeral 2, en cuanto a las sociedades de ahorro y crédito específicas ahí señaladas y las cajas de crédito; asimismo, supervisará a los sujetos obligados señalados en los numerales 3, 4, 5, 6, y 8 del mismo artículo; en los casos de casinos o empresas dedicadas a la explotación de juegos de suerte o azar en línea, supervisará la Lotería Nacional de Beneficencia." "El Consejo de Vigilancia de la Profesión de Contaduría Pública y Auditoría, supervisará a los sujetos obligados que señala el artículo 7 numeral 7 de la presente ley, en lo relacionado a los contadores y auditores." "La Corte Suprema de Justicia supervisará a los sujetos obligados que señala el artículo 7 numeral 7 de la presente ley, en lo relacionado a los abogados y notarios." "La Comisión Nacional de Activos Digitales supervisará a los sujetos obligados que señala el artículo 7 numeral 9, en lo que respecta a proveedores de servicios de activos digitales." "El Ministerio de Gobernación supervisará a las Organizaciones Financieras Sin Fines de Lucro, en cuanto al cumplimiento de las obligaciones indicadas en el inciso final del artículo 7." "El Tribunal Supremo Electoral supervisará a los sujetos obligados que señala el artículo 7 numeral 10 de la presente ley." "Para los efectos de la presente ley, se denominará como ente o entes de supervisión a las instituciones relacionadas en el presente artículo." Art. 13 (first inciso): "Todos los entes de supervisión deben aplicar el enfoque basado en riesgo para el ejercicio de la supervisión en la materia objeto de esta ley, por lo que deberán aplicar los estándares existentes en sus ámbitos de actuación, así como desarrollar su propia metodología." | Art. 12: the SSF supervises the Art. 7.1 financial subjects, and also the Art. 7.9 subjects when they operate with Bitcoin (under BCR Comité de Normas technical norms); the competent authority under special laws supervises the D.L. 339 associations/federations/confederations of Art. 7.2; the Superintendencia de Obligaciones Mercantiles supervises the Art. 7.2 savings-and-loan societies and credit unions plus the Art. 7 numerals 3, 4, 5, 6 and 8 subjects — with ONLINE casinos supervised by the Lotería Nacional de Beneficencia; the Consejo de Vigilancia de la Contaduría profession supervises the accountants/auditors of Art. 7.7; the Corte Suprema de Justicia supervises the lawyers/notaries of Art. 7.7; the Comisión Nacional de Activos Digitales supervises the digital-asset providers of Art. 7.9; the Ministerio de Gobernación supervises the financial OSFLs of Art. 7's final inciso; the Tribunal Supremo Electoral supervises the political parties of Art. 7.10 — these institutions are "los entes de supervisión". Art. 13: all supervisors apply the risk-based approach with their own methodology; supervision plans calibrate frequency and intensity to each subject's ML/TF/PF risk profile | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 12 pp.12-13 + Art. 13 p.13 (EVID-242/246; txt PAGE 12-13) |
| LB-004 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 9 (lead + numerals 1-3, 6-8; numerals 4-5 and 9-14 omitted — risk-management budget/application, UIF/supervisor information requests, internal/external audit, new-product risk assessment, transaction-profile monitoring, intensified PEP monitoring): "Los sujetos obligados establecidos en el artículo 7 de la presente ley, deberán cumplir las disposiciones aplicables contenidas en ésta y demás normativa que se emita para el desarrollo de la presente ley, a fin de implementar eficazmente un sistema integral de prevención… 1. Registrarse ante el ente de regulación o supervisión, según corresponda, y ante la UIF, de conformidad a las instrucciones establecidas y mantener actualizados los datos requeridos por éstos. 2. Desarrollar, adoptar y ejecutar planes de trabajo anuales, programas, políticas, procedimientos y controles internos, previstos en el marco regulatorio de la materia. 3. Aplicar un enfoque basado en riesgo individualizado, tomando como elementos fundamentales la identificación, evaluación y toma de acción eficaz para su mitigación, sin que ello implique una limitación indebida al acceso a productos o servicios. [4.-5. omisso] 6. Establecer y desarrollar planes anuales de capacitación especializados en materia de la presente ley, para los empleados con algún grado de responsabilidad… 7. Analizar los reportes internos de operaciones inusuales e informar a la UIF, cuando del análisis correspondiente se determine la existencia de alguna operación sospechosa… Los reportes de las operaciones sospechosas serán presentados por el Oficial de Cumplimiento. 8. Comunicar a la UIF y a los entes de supervisión respectivos, en un plazo máximo de quince días hábiles la designación o cambio del oficial de cumplimiento y su suplente, así como de los que forman parte del área u oficialía de cumplimiento. En caso de despido, traslado, renuncia o de la imposición de cualquier sanción impuesta por el sujeto obligado relacionada con el desempeño de sus funciones como oficial de cumplimiento, dicha comunicación deberá realizarla en el plazo de los cinco días hábiles siguientes. [9.-14. omisso]" | The Art. 7 obligated subjects must implement an integral prevention system, applying: 1. register before the regulation/supervision body AND the UIF per their instructions, keeping the required data current; 2. develop, adopt and execute ANNUAL work plans, programs, policies, procedures and internal controls; 3. apply an individualized risk-based approach (identify, evaluate, act) without unduly limiting access to products/services; [4-5 omitted]; 6. establish and develop ANNUAL specialized training plans for employees with responsibility in the risk system; 7. analyze the INTERNAL reports of unusual operations and inform the UIF when the analysis determines a suspicious operation — the ROS is presented by the Oficial de Cumplimiento; 8. notify the UIF and supervisors within a MAXIMUM OF FIFTEEN DÍAS HÁBILES of the designation or change of the compliance officer and alternate (and of the compliance-office members), and within FIVE DÍAS HÁBILES in case of dismissal, transfer, resignation or sanction related to the officer's functions; [9-14 omitted] | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 9 pp.9-11 (EVID-243; txt PAGE 9-11) |
| LB-005 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 3: "Todos los sujetos obligados sin excepción deben registrarse ante la UIF en la plataforma diseñada para tales efectos, y están obligados a mantener la información actualizada en todo momento. En el caso que hubiere cambios en la información requerida, deben actualizar su registro en la plataforma en un plazo de 15 días hábiles. Dicha información será compartida a los órganos de supervisión en la plataforma que señala la UIF." "En cumplimiento de las Recomendaciones del GAFI los sujetos obligados deberán suministrar en el referido formulario información sobre los beneficiarios finales." Art. 4 (third inciso): "El principio general de un enfoque basado en riesgos es que, cuando existan riesgos mayores, los sujetos obligados deben ejecutar medidas intensificadas para administrar y mitigar esos riesgos; y que, por su parte, cuando los riesgos sean menores, pueden aplicar medidas simplificadas, todo lo cual debe quedar justificado y documentado… No deberán aplicarse medidas simplificadas cuando exista una sospecha de LDA/FT/FPADM." | ALL obligated subjects without exception must register with the UIF on its designated platform and keep the information current at all times; on changes, update within 15 días hábiles; the information is shared with the supervision bodies. Per GAFI recommendations the registration form includes ultimate-beneficial-owner information. EBR general principle: greater risks demand intensified measures, lesser risks permit simplified measures — justified and documented; NO simplified measures where suspicion of ML/TF/PF exists | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Arts. 3-4 p.4 / pp.4-5 (EVID-247/249; txt PAGE 4-5) |
| LB-006 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 5 (lead + policy-requisite literals a)/b)/e)/f); literals c)/d)/g)-j) omitted; closing paragraphs in full): "Los sujetos obligados deben adoptar políticas que orienten la actuación de sus directivos, empleados, subcontratados y demás colaboradores… para que, con su aplicación, se fortalezca la cultura de prevención del LDA/FT/FPADM que permita el control, detección de operaciones inusuales y reporte de operaciones sospechosas, a través de la aplicación del enfoque basado en riesgos…" "…deberán cumplir como mínimo con los siguientes requisitos: a) Impulsar a nivel institucional la cultura de gestión de riesgos…; b) Aprobar los lineamientos que adoptará el sujeto obligado para la prevención, control y detección de operaciones inusuales, con un enfoque basado en riesgos. [c)-d) omisso] e) Aprobar las políticas de aceptación de clientes y contrapartes, así como procesos de administración, actualización de información, y consecuencias para los clientes o contrapartes de no proporcionarla. f) Elaborar procedimientos para la detección de operaciones inusuales y reporte de operaciones sospechosas y garantizar la reserva de la información reportada. [g)-j) omisso]" "Las políticas adoptadas por los sujetos obligados para la prevención, control y detección de operaciones inusuales con respecto a sus clientes y usuarios deben cubrir y desarrollar los siguientes aspectos: 1. Realizar la debida diligencia de sus clientes y usuarios. 2. Control de operaciones de los clientes y usuarios. 3. Gestión de riesgos asociados a los delitos de LDA/FT/FPADM." | Subjects must adopt policies orienting the conduct of directors, employees, subcontractors and collaborators to strengthen the prevention culture for unusual-operation control/detection and ROS reporting under the EBR; the top governance body approves and drives them, at minimum: instilling the risk culture; approving the risk-based guidelines; [c-d omitted: responsibility assignment; stricter client-knowledge parameters]; approving client/counterparty ACCEPTANCE policies and information-update processes and the consequences of not providing information; drafting unusual-operation detection and ROS procedures and guaranteeing the reserve of reported information; [g-j omitted]. The client-facing policies must cover and develop: 1. due diligence of clients and users; 2. control of their operations; 3. risk management for ML/TF/PF | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 5 pp.6-7 (EVID-243 zone; txt PAGE 6-7) |
| LB-007 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 7 (literals a), c), d), f), g), m); the rest omitted — responsibility assignment, EDD policies, resources, report knowledge, audit instruction, support, freezing mechanisms, detection procedures, non-compliance consequences, ethics precedence, archive procedures): "…será responsabilidad del órgano de gobierno de mayor jerarquía o quien haga sus veces… además de aprobar las políticas a las que se hace referencia en el Art. 5 de este instructivo, lo siguiente: a) Para el caso de los sujetos obligados supervisados por una institución oficial, crear la Oficialía de Cumplimiento… c) Nombrar al Oficial o Encargado de Cumplimiento y su suplente. d) Aprobar un sistema de gestión de riesgos para la prevención del LDA/FT/FPADM… que incluya, entre otros, los siguientes elementos: Manual de políticas y procedimientos, procedimientos de debida diligencia, código de ética, sistema de monitoreo y plan de auditoria interna para la prevención del LDA/FT/FPADM. f) Aprobar el plan de trabajo anual de la Oficialía de Cumplimiento o Encargado de Cumplimiento… g) Aprobar el plan de capacitación anual en materia de prevención del LDA/FT/FPADM, incluyendo programas de inducción al personal de nuevo ingreso… m) Comunicar a la UIF y a los organismos de fiscalización, supervisión o vigilancia respectivos, el nombramiento del Oficial o Encargado de Cumplimiento, titular y suplente, en un plazo máximo de quince días hábiles, contados a partir del inicio o entrada en vigencia de su nombramiento y en los casos de despido, sanción, remoción o renuncia del oficial o encargado de cumplimiento o su suplente, tendrán un plazo de hasta cinco días hábiles, para dicha comunicación, contados a partir de la fecha en que el despido, sanción, remoción o renuncia sea efectiva. La resolución de despido deberá ser debidamente fundamentada e informada a la UIF…" | It is the responsibility of the top governance body (or equivalent), besides approving the Art. 5 policies: a) for subjects supervised by an official institution, CREATE the Oficialía de Cumplimiento; c) appoint the Oficial or Encargado de Cumplimiento and alternate; d) approve a risk-management system including at least: policies-and-procedures manual, DD procedures, code of ethics, monitoring system and internal audit plan; f) approve the ANNUAL WORK PLAN of the Oficialía/Encargado; g) approve the ANNUAL TRAINING plan including induction for new staff; m) notify the UIF and supervision bodies of the officer/alternate appointment within a maximum of FIFTEEN DÍAS HÁBILES from the appointment's start, and within up to FIVE DÍAS HÁBILES from the effective date of dismissal, sanction, removal or resignation — dismissal resolutions must be duly founded and informed with the acta certification, resignation or dismissal copy attached | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 7 pp.8-10 (EVID-243 zone; txt PAGE 8-10) |
| LB-008 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 8 (first inciso + the 2023-reformed evaluation incisos, stamp (2) = Acuerdo 476): "Los sujetos obligados deben establecer órganos e instancias responsables de efectuar una evaluación del cumplimiento de los controles aplicables para la prevención del LDA/FT/FPADM… y para la detección de operaciones inusuales y el reporte de operaciones sospechosas, a fin de que se puedan determinar sus fallas o debilidades e informarlas a las instancias pertinentes." "CON BASE A RIESGOS, LA AUDITORÍA INTERNA DEBERÁ EVALUAR POR LO MENOS UNA VEZ AL AÑO EL CUMPLIMIENTO Y EFECTIVIDAD DE LAS NORMAS APLICABLES, POLÍTICAS Y PROCEDIMIENTOS PARA LA PREVENCIÓN DEL LAVADO DE DINERO… Y PARA EL CONTROL, DETECCIÓN DE OPERACIONES INUSUALES Y REPORTE DE OPERACIONES SOSPECHOSAS, VALIDACIÓN DEL ENVÍO DE REPORTES REGULADOS, DEBIENDO EMITIR INFORME DE LOS RESULTADOS DE LA EVALUACIÓN AL ÓRGANO DE GOBIERNO DE MAYOR JERARQUÍA, O QUIEN HAGA SUS VECES. (2)" "EN CASO DE NO CONTAR CON AUDITOR INTERNO, LA EVALUACIÓN DEBERÁ SER REALIZADA POR EL AUDITOR EXTERNO NOMBRADO POR EL SUJETO OBLIGADO DE CONFORMIDAD A LAS DISPOSICIONES DEL CÓDIGO DE COMERCIO… (2)" "La auditoría interna debe contar con un plan anual para la verificación del cumplimiento de las políticas y procedimientos para la prevención del LDA/FT/FPADM." | Subjects must establish organs and instances responsible for evaluating control compliance for ML/TF/PF prevention, unusual-operation detection and ROS reporting, determining and reporting their failures/weaknesses. RISK-BASED, INTERNAL AUDIT MUST AT LEAST ONCE A YEAR evaluate the compliance and effectiveness of the applicable norms, policies and procedures — including VALIDATION OF THE SENDING OF REGULATED REPORTS — reporting the results to the top governance body; where there is no internal auditor, the evaluation is performed by the external auditor appointed per the Commercial Code; internal audit keeps an annual verification plan | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 8 pp.10-11 (EVID-249 zone; txt PAGE 10-11) |
| LB-009 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 15 (DD-ladder incisos; the insurance-beneficiary and risk-determination incisos condensed): "Los sujetos obligados, para lograr identificar a sus clientes y usuarios, incluyendo el controlador, destinatario o beneficiario final…, deben tomar medidas razonables para llevar a cabo procedimientos de debida diligencia." "Las medidas de debida diligencia solo se deberán aplicar a los clientes o usuarios con los que el sujeto obligado tenga una relación contractual o de negocios, estableciéndose medidas de debida diligencia simplificada, estándar o intensificada, en congruencia con el enfoque basado en riesgo que defina el sujeto obligado." "…la debida diligencia simplificada se podrá aplicar a clientes con el nivel de riesgo bajo o en productos y servicios de bajo riesgo, siempre se deberá verificar la identidad del cliente o de la persona que actúe en su nombre o representación, cuando corresponda." "La debida diligencia estándar será aplicada inicialmente a todos los clientes a excepción de los clientes de riesgo alto, e incluye la identificación del cliente, beneficiario final y las personas que actúan en representación de los beneficiarios finales, la naturaleza y el propósito de la relación comercial a entablar, juntamente con la determinación del origen de los fondos." "La debida diligencia intensificada será la que se aplique a clientes que de acuerdo con su evaluación se considere que el nivel de riesgo es alto, este tipo de medidas requieren la recopilación y verificación de información relacionada con la fuente de riqueza o la fuente de fondos del cliente." "En caso de personas jurídicas se deberá identificar a los beneficiarios finales con una participación mayor o igual al veinti cinco por ciento, siendo el beneficiario final la persona natural que posea o controle directa o indirectamente el porcentaje antes manifestado del capital o de los derechos de voto de una persona jurídica, o que por otros medios ejerzan el control directo o indirecto, de la gestión de una persona jurídica." "No será necesario identificar a los beneficiarios finales o reales, cuando el cliente o el propietario posea una participación igual o superior al veinticinco por ciento del capital en una sociedad comercial que cotiza en bolsa de valores y está sujeta a requisitos de revelación de información en el mercado de valores." "Los sujetos obligados deben aplicar la debida diligencia del cliente, cuando: a) Establezcan relaciones comerciales; b) Realicen transacciones ocasionales por encima del umbral aplicable para el reporte de operaciones en efectivo…; c) Exista una sospecha de lavado de activos…; o d) El sujeto obligado tiene dudas razonables sobre la veracidad o idoneidad de los datos de identificación…" "Los sujetos obligados únicamente deben mantener registros nominativos de sus clientes o usuarios…, éstos no mantendrán cuentas o relaciones comerciales anónimas o cifradas." "Los clientes o usuarios deberán proporcionar la información o documentación requerida por los sujetos obligados para el inicio de relaciones comerciales; en caso de no proporcionarla, los sujetos obligados podrán abstenerse de iniciarlas; lo anterior, sin perjuicio de que, a partir del análisis correspondiente, se considere hacer un reporte de tentativa de transacción sospechosa sobre el cliente." | Subjects must take reasonable DD measures to identify clients and users, including the controller, recipient or ultimate beneficiary, applying the ladder — SIMPLIFIED (low-risk clients/products, identity always verified), STANDARD (applied initially to all clients except high-risk: identification of client, beneficiario final and their representatives, nature and purpose of the relation, origin of funds) or ENHANCED/INTENSIFIED (high-risk: collection and verification of source-of-wealth/source-of-funds information) — congruent with the subject's EBR. For legal persons, beneficiarios finales are identified at participation ≥ TWENTY-FIVE PERCENT — the natural person directly or indirectly holding or controlling that share of capital or voting rights, or otherwise exercising direct or indirect control of the legal person's management; listed companies subject to market disclosure are carved out. DD applies when: a) establishing commercial relations; b) occasional transactions above the applicable cash-report threshold (for casinos and metals traders, per the GAFI-standard amounts the Reglamento sets); c) suspicion of ML/TF/PF; d) reasonable doubts about identification data. Records are NOMINATIVE ONLY — no anonymous or coded accounts/relations. Clients must provide the required information/documentation to start relations; failing that, subjects MAY ABSTAIN from starting them — without prejudice to considering a tentativa (attempted-transaction) suspicious report | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 15 pp.14-15 (EVID-243; txt PAGE 14-15) |
| LB-010 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 20: "Los sujetos obligados identificarán al beneficiario final y adoptarán medidas adecuadas, a fin de comprobar su identidad con carácter previo al establecimiento de relaciones de negocio o a la ejecución de cualquier operación. Por lo que se considerará beneficiario final: a) La persona natural por cuya cuenta se pretenda establecer una relación contractual o intervenir en cualquier operación. b) La persona natural que en último término posea o controle directa o indirectamente un porcentaje igual o superior al 10% del capital o de los derechos de voto de una persona jurídica, o que por otros medios ejerzan el control directo o indirecto, de la gestión de una persona jurídica. Cuando el cliente, contraparte o el propietario de una participación igual o superior al 10% del capital de un cliente sea una sociedad comercial que cotiza en bolsa de valores…, no será necesario identificar a los beneficiarios finales o reales de dichas sociedades." | Subjects identify the beneficiario final and verify identity BEFORE establishing business relations or executing any operation. Beneficiario final: a) the natural person on whose account a contractual relation is sought or who intervenes in any operation; b) the natural person ultimately holding or controlling, directly or indirectly, ≥ TEN PERCENT of a legal person's capital or voting rights, or otherwise exercising direct/indirect control of its management (listed companies carved out) — KEPT-INSTRUCTIVO VALUE: the 10% participation is DISPLACED by the later law's ≥25% (71_ Art. 15, LB-009) under the §2 authority order; recorded as dated config with provenance, never hardcoded (OQ-003) | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 20 pp.19-20 (EVID-249; txt PAGE 19-20) |
| LB-011 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 19: "Los sujetos obligados deben mantener registros nominativos de sus clientes o contrapartes, estos no mantendrán cuentas o relaciones comerciales anónimas o cuentas en las cuales haya nombres incorrectos o ficticios." | Subjects must keep NOMINATIVE records of clients/counterparties; they shall not keep anonymous commercial accounts or relations, or accounts with incorrect or fictitious names | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 19 p.20 (EVID-249; txt PAGE 20) |
| LB-012 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 19 (lead + closing incisos; the national-positions catalog a)-n) and foreign catalog a)-h) listed by lead items): "Se entenderán por Personas Expuestas Políticamente (PEP), todas aquellas personas naturales que ejerzan función pública o a quienes se les haya confiado ésta." "Para tales efectos se entenderán como PEP nacionales, las personas que ostenten los cargos siguientes: a) El presidente, vicepresidente de la República y los designados a la presidencia; b) Los diputados de la Asamblea Legislativa; c) Los ministros, viceministros de Estado, secretarios, y los gobernadores departamentales; d) El presidente y magistrados de la Corte Suprema de Justicia…; e) Alcaldes y demás miembros de los Concejos Municipales; f) El presidente y magistrados de la Corte de Cuentas de la República; g) El Fiscal General de la República, el procurador General de la República, el procurador para la defensa de los Derechos Humanos; h) El presidente y magistrados del Tribunal Supremo Electoral; i) Los representantes diplomáticos; j) Titulares de las instituciones autónomas…; k) Directores y representantes legales de sociedades constituidas con activos del Estado…; l) Miembros del máximo organismo de dirección de partidos políticos, incluyendo el tesorero; m) Director y subdirector General de la Policía Nacional Civil; n) Generales de las Fuerzas Armadas…" "Asimismo, se entenderán por Personas Expuestas Políticamente extranjeras, las siguientes: a) Los jefes de Estado o de gobierno; b) Políticos de alto nivel; c) Funcionarios públicos extranjeros gubernamentales, judiciales o de organismos internacionales de alto nivel; d) Militares de alto rango; e) Ejecutivos de alto nivel de corporaciones estatales; f) Funcionarios de alto nivel de partidos políticos; g) Embajadores y cónsules de otros países acreditados en El Salvador; y h) Las personas que cumplen o a quienes se les han confiado funciones prominentes por una organización internacional." "La UIF será el ente encargado de la emisión y actualización del listado de los cargos de las personas expuestas políticamente…" "…se continuarán considerando PEP aquellas personas que hubiesen sido catalogadas con tal carácter, durante los cinco años siguientes a la fecha en la que cese el último nombramiento." "Se aplicarán medidas de diligencias intensificadas a los miembros de la familia hasta sus parientes en segundo grado de consanguinidad o afinidad, cónyuge y compañeros de vida o asociados cercanos de los PEP." | Politically Exposed Persons (PEP) = all natural persons exercising or entrusted with public function. National catalog: president/vice-president and presidential designees; Assembly deputies; ministers, viceministers, secretaries, departmental governors; CSJ president and magistrates (and second-instance and first-instance judges and justices of the peace); mayors and municipal council members; Corte de Cuentas president and magistrates; the FGR, PGR and PDDH heads; TSE president and magistrates; diplomatic representatives; heads of autonomous institutions; directors and legal representatives of State-asset societies; political-party top-governance members including the treasurer; PNC director and subdirector; FFAA generals. Foreign catalog: heads of state/government; senior politicians; senior governmental/judicial/international-organization officials; high-rank military; state-corporation executives; senior party officials; ambassadors and consuls accredited in El Salvador; persons entrusted prominent functions by international organizations. The UIF issues and updates the position list. PEP status CONTINUES for FIVE YEARS after the last appointment ceases. Enhanced DD applies to family members up to second degree of consanguinity/affinity, spouses, life partners or close associates | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 19 pp.17-18 (EVID-243; txt PAGE 17-18) |
| LB-013 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 18: "Cuando el sujeto obligado, después de realizar un análisis de riesgo del cliente, con base a criterios objetivos y comprobables determine elementos suficientes que demuestren la existencia de un riesgo…, que luego de ser gestionado conforme a sus políticas no puede ser mitigado, decidan dar por terminada la relación contractual o de negocios, deberán informar a la UIF esta decisión, junto con el análisis de riesgo respectivo. La notificación de cierre de cuentas únicamente procederá cuando los fondos de la cuenta sean mayores a mil dólares de los Estados Unidos de América." "La UIF contará con el plazo de diez días hábiles para comunicar al sujeto obligado reportante la imposición o no de medidas cautelares adoptadas por la Fiscalía General de la República. El sujeto obligado sólo podrá dar por terminada la relación comercial, una vez haya vencido el plazo sin que haya recibido respuesta de la UIF." | When, after an objective-and-verifiable risk analysis, the subject determines an unmanageable ML/TF/PF risk and decides to terminate the contractual or business relation, it must inform the UIF of the decision together with the risk analysis. The account-CLOSURE notification proceeds ONLY when the account funds exceed ONE THOUSAND US DOLLARS (US$1,000 — the low-value-account carve-out, dated config). The UIF then has TEN DÍAS HÁBILES to communicate whether the FGR has adopted precautionary measures; the subject may only terminate the relation once that window has lapsed without a UIF response | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 18 p.16 (EVID-243; txt PAGE 16) |
| LB-014 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 20 (first and third incisos; hierarchy/requirements incisos condensed) + Art. 22: Art. 20: "Los sujetos obligados supervisados por la Superintendencia del Sistema Financiero, la Comisión Nacional de Activos Digitales, y los contemplados en el artículo 7 numeral 2 de la presente ley, deben establecer una oficialía de cumplimiento, a cargo de un oficial de cumplimiento titular y suplente, nombrados por la junta directiva u órgano equivalente…" "Los sujetos obligados supervisados por las entidades señaladas en el artículo 11 literales b), c), d), f), g) y h)…, salvo lo dispuesto en el inciso anterior, podrán prescindir de contar con una oficialía de cumplimiento y deberán designar un oficial de cumplimiento y un suplente…" "El oficial de cumplimiento gozará de autonomía en la ejecución de las funciones y obligaciones establecidas en la presente ley…, y tendrá una relación directa funcional con la máxima autoridad de la entidad… El oficial de cumplimiento y su suplente deben reunir los requisitos que se establezcan en el instructivo emitido por la UIF para tales efectos." Art. 22: "Las personas naturales que sean catalogadas como sujetos obligados de conformidad al artículo 7 numerales 5, 6, 7, 8, y 9 de la presente ley, podrán no designar un oficial de cumplimiento; en este caso, serán los responsables de aplicar todos los controles para la prevención… establecidos en la presente ley y el ordenamiento jurídico aplicable." | Subjects supervised by the SSF, the Comisión Nacional de Activos Digitales and the Art. 7.2 subjects MUST establish an Oficialía de Cumplimiento headed by a titular compliance officer and alternate appointed by the board or equivalent organ (hierarchically dependent on it; administratively on the chief executive). Subjects supervised by the other listed entities may dispense with the Oficialía but must designate an officer and alternate. The officer enjoys autonomy and a direct functional relation with the entity's top authority; officer and alternate must meet the UIF instructivo's requirements. Art. 22: NATURAL PERSONS categorized as subjects under Art. 7 numerals 5-9 need NOT designate an officer — they are themselves responsible for applying all prevention controls | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Arts. 20/22 pp.18-19 (EVID-243; txt PAGE 18-19) |
| LB-015 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 23: "Los sujetos obligados que deban nombrar a una oficialía de cumplimiento de conformidad con lo dispuesto en la presente ley, deberán constituir un Comité de Prevención de Lavado de Activos y Financiamiento del Terrorismo y Financiamiento de la Proliferación de Armas de Destrucción Masiva, en adelante el Comité, el cual tendrá como su principal función la de servir de apoyo a la oficialía de cumplimiento, en materia de prevención dispuesta en esta ley." "En el caso de grupos empresariales o conglomerados financieros que nombren un solo oficial de cumplimiento…, podrán constituir un solo Comité y no uno por cada entidad…, debiendo llevar un solo libro de actas para dejar constancia de los acuerdos tomados, siempre que exista representación de cada una de las entidades dentro de dicho Comité." "La estructura y funcionamiento del Comité… se regulará conforme a la normativa interna de los sujetos obligados, debiendo estar integrado por al menos tres miembros, de los cuales uno deberá pertenecer al máximo organismo de dirección y otro el oficial de cumplimiento." | Subjects that must appoint an Oficialía de Cumplimiento must constitute a Prevention Committee (Comité de Prevención) whose principal function is supporting the Oficialía in the law's prevention matters. Business groups or financial conglomerates appointing a single officer may constitute a SINGLE Comité (not one per entity) keeping a SINGLE acta book, provided each entity is represented in it. The Comité's structure and functioning are governed by the subject's internal rules, with AT LEAST THREE MEMBERS, of whom ONE must belong to the top governance organ and another must be the compliance officer | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 23 p.19 (EVID-243; txt PAGE 19) |
| LB-016 | Reglamento de la Ley Contra el Lavado de Dinero y de Activos (D.E. 2-2000, kept in force), Art. 3 (second inciso — the kept window mechanics; its colones amounts and 3-day clock are DEAD superseded values, never loaded) + Art. 4 literals g) and j): Art. 3: "Para los efectos de aplicación del inciso 1º del Art. 9 de la Ley, el plazo de un mes que en el mismo se señala, habrá de computarse como los anteriores treinta días continuos, es decir, contados a partir del momento en que se realizó la última transacción, entendiéndose que si en dos o más operaciones el monto de éstas exceden a los quinientos mil colones o su equivalente en moneda extranjera, no obstante no haya transcurrido el plazo, las Instituciones estarán en la obligación de informar a la Unidad de Investigación Financiera…, al existir suficientes elementos de juicio para considerar que tales operaciones o transacciones son irregulares o sospechosas; o bien, cuando lo requiera la UIF." Art. 4 g): "Comunicar a la UIF y a los organismos de fiscalización o supervisión, en un plazo de quince días hábiles, la designación o cambio de los funcionarios, respecto a: 1) encargados de ejecutar programas, procedimientos internos y las comunicaciones referentes a transacciones irregulares o sospechosas; y 2) responsables de la supervisión del trabajo de los encargados de tal ejecución, quienes servirán de enlace con la UIF;" Art. 4 j): "Guardar confidencialidad de toda información transmitida o requerida de conformidad con la Ley y este Reglamento, de manera que no podrán divulgarla a ninguna persona, incluso a los usuarios o clientes investigados, salvo por orden de un juez competente o del Fiscal General de la República." | Art. 3: the one-month accumulation period computes as the THIRTY CONTINUOUS DAYS BEFORE the last transaction — cumulative multiple operations exceeding the (now-superseded colones) threshold inside that window trigger the UIF-informing duty even before the window closes (the window MECHANICS survive; the ¢500,000 amount and 3-días-hábiles clock are dead). Art. 4 g): notify the UIF and supervision bodies within FIFTEEN DÍAS HÁBILES of designating or changing the program-executor officials and their supervisors, who act as UIF liaison. Art. 4 j): keep confidential all information transmitted or required under the law and reglamento, never disclosing it to any person — including the investigated users or clients — save by order of a competent judge or the Fiscal General (kept liaison-mechanics and no-tip-off, co-existing with the law-level rules of 71_ Arts. 9.8 and 28) | `sv/sources/17_Reglamento_Lavado_Activos.pdf` | Arts. 3-4 pp.1-3 (EVID-232/233; txt PAGE 1-3) |
| LB-017 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 71 + Art. 72 (residence/registration/anti-retaliation incisos; requirement tiers condensed) + Art. 80 (APNFD Encargado): Art. 71: "Los sujetos obligados, acorde con las actividades, naturaleza, tamaño, operaciones y nivel de riesgo…, deben designar un Encargado de Cumplimiento nombrado por el órgano de gobierno de mayor jerarquía u órgano de dirección equivalente y dependerá jerárquicamente de éste y en lo administrativo del director presidente, presidente ejecutivo, gerente general o su equivalente." "También deberán nombrar a la persona que se desempeñará como Encargado de Cumplimiento suplente, quien deberá cumplir con los requisitos aplicables al Encargado de Cumplimiento titular." Art. 72: "…La función del Encargado de Cumplimiento y su suplente deberá ser ejercida por persona residente en el país." "El Encargado de Cumplimiento deberá registrarse ante la UIF, y no podrá ser despedido, sancionado o removido por cumplir con las atribuciones inherentes a sus funciones." Art. 80: "El Encargado de Cumplimiento de los sujetos obligados que realizan actividades y profesiones no financieras designadas (APNFD) gozarán de independencia y autonomía… La función del Encargado de Cumplimiento y su suplente deberá ser ejercido por persona residente en el país." "EL ENCARGADO DE CUMPLIMIENTO DEBERÁ REUNIR LOS REQUISITOS SEÑALADOS EN EL ART. 72 INCISO SEGUNDO DE ESTE INSTRUCTIVO. (2)" "El Encargado de Cumplimiento de las personas jurídicas que realizan actividades y profesiones no financieras designadas (APNFD) deberá registrarse ante la UIF, y no podrá ser despedido, sancionado o removido por cumplir con las atribuciones inherentes a sus funciones." | Per the EBR, subjects (the non-Oficialía population, incl. the APNFD) must designate an Encargado de Cumplimiento appointed by the top governance organ, hierarchically dependent on it and administratively on the chief executive, plus an alternate meeting the same requirements. The function must be exercised by a person RESIDENT IN THE COUNTRY; requirements in tiers (full set: training, regulatory knowledge, university degree, business knowledge; lighter set for the listed rubros: training, regulatory knowledge, activity experience — Art. 72 second inciso). The Encargado must REGISTER with the UIF and CANNOT be dismissed, sanctioned or removed for performing the functions inherent to the role (ANTI-RETALIATION protection) — the APNFD legal-person Encargados follow the same requirement, registration and protection regime (Art. 80). Annual written reports to the governance organ on management results, UIF-report compliance and detection effectiveness (Art. 73, gloss) | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Arts. 71-72 pp.45-46 + Art. 80 p.51 (EVID-249; txt PAGE 45-46, 51) |
| LB-018 | Reglamento de la Ley Contra el Lavado de Dinero y de Activos (D.E. 2-2000, kept in force), Art. 12: "Se consideran transacciones irregulares o sospechosas todas las operaciones poco usuales, las que se encuentran fuera de los patrones de transacción habituales y las que no sean significativas pero sí periódicas, sin fundamento económico o legal evidentes, y todas aquellas operaciones inconsistentes o que no guardan relación con el tipo de actividad económica del cliente." [Arts. 13-18 = the red-flag detail catalogs: Art. 13 special attention — day-to-day/inhábile-hour multiple transfers, early or oversized loan repayments without explained origin, international monetary instruments disproportionate to activity; Art. 14 markedly unusual operations — CD-collateralized loans, safe-box visits followed by just-under-threshold cash deposits, cashier's/traveller's-cheque purchases in big cash or "justo bajo el monto requerido para generar un informe", cash-heavy fideicomisos, casa-de-cambio structured deposits, constant ATM deposits, marked instruments; Art. 15 evasive conduct — refusing form information, pressing staff not to keep transaction reports; Art. 16 transfer patterns — sub-threshold deposits consolidated then sent abroad, round-trip transfers, no-currency-change international transfers, received transfers immediately converted into instruments for third-party payments; Art. 17 insufficient/suspicious KYC info — incomplete purpose/directors, refusing background, account without references/address/ID, suspect or false documents, no employment history, refusing financial statements, statements notably different from similar businesses, false/inexact information; Art. 18 pattern changes — correspondent cash patterns, cash growth without reported-transaction growth, high-denomination movement disproportionate to location, small-denomination surges, unjustified deposit frequency/volume increases] | Irregular or suspicious transactions are: all unusual operations, those outside habitual transaction patterns, insignificant-but-periodic ones without evident economic or legal foundation, and all operations inconsistent with or unrelated to the client's type of economic activity. Arts. 13-18 develop the indicator catalogs (structuring just under the reportable amount, velocity/aggregation, activity-consistency, KYC-refusal/evasion, pattern-shift) — the kept red-flag taxonomy a configurable detection engine seeds itself with | `sv/sources/17_Reglamento_Lavado_Activos.pdf` | Arts. 12-18 pp.3-5 (EVID-234; txt PAGE 3-5) |
| LB-019 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 42 + Art. 43: Art. 42: "El empleado o colaborador del sujeto obligado que detecte operaciones inusuales informará a la Oficialía de Cumplimiento o al Encargado de Cumplimiento, conforme a los procedimientos definidos por el sujeto obligado a efectos que se proceda al análisis de la operación inusual." "Inmediatamente detectada la operación inusual, la Oficialía de Cumplimiento o el Encargado de Cumplimiento, tienen el plazo de quince días hábiles para realizar el análisis de esta, prorrogables una sola vez, por igual período, previa solicitud a la UIF. La prórroga deberá solicitarse vía CEP." Art. 43: "El análisis de las operaciones inusuales de los clientes o contrapartes debe determinar si existen suficientes elementos de juicio para considerarlas operaciones sospechosas, conforme a hechos objetivos observados y establecidos por el sujeto obligado en dicho análisis, y deberán reportarse a la UIF." "Si del análisis realizado, se determina por parte del Oficial o Encargado de Cumplimiento que la operación inusual es sospechosa, deberá reportarse la misma dentro de los cinco días hábiles, contados a partir del momento en el que se determinó que la operación es sospechosa." | The employee or collaborator detecting unusual operations informs the Oficialía or Encargado per the subject's procedures. IMMEDIATELY upon detection, the Oficialía/Encargado has FIFTEEN DÍAS HÁBILES to analyze, extendable ONCE for the same period upon prior request to the UIF (via CEP). The analysis must determine whether sufficient elements of judgment — grounded on objective facts — make the operations suspicious. The 72_ transmit clock ("within five días hábiles from the determination") is DISPLACED by the law's 24-hour clock (71_ Art. 24, LB-020) under the §2 authority order — recorded as a working ruling (OQ-003) | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Arts. 42-43 pp.29-30 (EVID-249; txt PAGE 29-30) |
| LB-020 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 24: "Los sujetos obligados deberán reportar a la UIF las operaciones sospechosas en los formatos autorizados con prontitud y en un plazo máximo de veinticuatro horas después de finalizado el análisis que se realice, siempre y cuando existan suficientes elementos de juicio para considerarlas sospechosas. Los sujetos obligados, a partir de la detección de una operación inusual, tendrán un plazo de hasta 15 días hábiles para realizar el análisis y determinar la procedencia o no de un reporte de operación sospechosa. Dicho plazo podrá ser prorrogado por una sola vez por el mismo período, previa solicitud del oficial de cumplimiento a la UIF." "El reporte de operaciones sospechosas debe contar con las características de ser oportuno, completo y concreto." "Además, deben brindar a la UIF, en los formatos, canales y dentro de los plazos que ésta disponga, toda aquella información que les sea requerida como complemento al reporte remitido. La UIF determinará los canales por los cuales deban remitir los reportes y la información relacionada en el presente artículo." "El reporte de operación sospechosa es confidencial, no tendrá valor probatorio, será utilizado únicamente con fines de inteligencia y no deberá ser incorporado a los expedientes administrativos o judiciales." "La UIF emitirá la normativa correspondiente que deban adoptar los sujetos obligados para la detección de operaciones inusuales y remisión del reporte de operaciones sospechosas, incluyendo la tentativa de éstas, así como del reporte de actividades sospechosas. El monto de las operaciones o transacciones es irrelevante para los efectos del presente artículo." | Subjects must report suspicious operations to the UIF in the authorized formats PROMPTLY and within a MAXIMUM OF TWENTY-FOUR HOURS AFTER THE ANALYSIS IS COMPLETED, provided sufficient elements of judgment exist. From the DETECTION of an unusual operation, the subject has up to FIFTEEN DÍAS HÁBILES to analyze and determine whether a ROS proceeds — extendable ONCE for the same period upon the officer's prior request to the UIF. The ROS must be timely, complete and concrete; complementary information goes to the UIF in the formats, channels and deadlines it provides (the UIF determines the transmission channels). The ROS is CONFIDENTIAL, has NO PROBATIVE VALUE, is used solely for intelligence purposes and must not be incorporated into administrative or judicial files. The UIF will issue the norms for unusual-operation detection and ROS/attempted-ROS/suspicious-activity reporting. THE AMOUNT OF THE OPERATIONS OR TRANSACTIONS IS IRRELEVANT for this article | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 24 p.20 (EVID-244; txt PAGE 20) |
| LB-021 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 25: "Las transacciones en efectivo o por cualquier otro medio, las transferencias electrónicas locales o internacionales y las transacciones en activos digitales, realizadas por un cliente o usuario, en un solo evento o acumuladas durante un mes y que parezcan estar vinculadas entre sí, deberán ser reportadas por los sujetos obligados a la UIF, dentro del plazo de cinco días hábiles siguientes de realizada la operación. El contenido de los reportes que serán remitidos a la UIF y los umbrales de dichas transacciones, serán desarrollados en el reglamento de la presente ley de conformidad con los estándares emitidos por el Grupo de Acción Financiera Internacional…" | Cash or other-media transactions, local or international electronic transfers and DIGITAL-ASSET transactions, performed by a client or user, IN A SINGLE EVENT OR ACCUMULATED OVER A MONTH and apparently linked to one another, must be reported by the subjects to the UIF within FIVE DÍAS HÁBILES following the operation. The report CONTENT and the transaction THRESHOLDS are DELEGATED to the law's future Reglamento per GAFI standards — the delegation head of the threshold authority chain (operative values = 72_ Art. 51, LB-022, under the Art. 61 transitory; supersession watch OQ-001) | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 25 p.20 (EVID-244; txt PAGE 20) |
| LB-022 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 51: "Los sujetos obligados deberán enviar la información requerida en los formularios diseñados por la UIF de transacciones en efectivo u otro medio, en el plazo de cinco días hábiles contados a partir del siguiente día de realizada la operación o finalizado el mes calendario, dependiendo el caso, y a través de la plataforma electrónica desarrollada por la UIF. 1. Operación individual en efectivo. Se entenderá por transacción en efectivo que realiza un cliente en un solo evento, cuyo valor sea superior a US$10,000.00, o su equivalente en moneda extranjera. También debe considerarse como una operación individual en efectivo toda transacción que esté conformada por efectivo y otros medios, siempre y cuando la cantidad en efectivo sobrepase los US$10,000.00… 2. Operaciones múltiples en efectivo. Son transacciones en efectivo iguales o inferiores a US$ 10,000.00…, las cuales al acumularse en el término de un mes calendario, superen los US$10,000.00… El reporte solo debe incluir el monto total de las transacciones y el valor en efectivo acumulado…, en el plazo de cinco días hábiles contados a partir del día siguiente de finalizado el mes calendario. 3. Operación individual – otro medio. Son transacciones en otro medio que realiza un cliente en un solo evento, cuyo valor sea superior a US$25,000.00… También se considera como una operación individual en otro medio, toda transacción que esté conformada por otro medio y efectivo, siempre y cuando la cantidad que en otro medio sobrepase los US$25,000.00… 4. Operaciones múltiples - transacciones en otro medio. Se consideran como operaciones múltiples las transacciones en otro medio iguales o inferiores a US$25,000.00…, las cuales al acumularse en el término de un mes calendario, superen los US$25,000.00… Estas transacciones deberán reportarse a la UIF en un plazo de 5 días hábiles con posterioridad al mes calendario." "Se entenderá por 'otro medio' cualquier título valor que no sea papel moneda o metálica, tales como cheques o pagos con tarjetas de crédito." | Subjects send, in the UIF-designed forms and through the UIF's electronic platform, within FIVE DÍAS HÁBILES counted from the day after the operation or after the calendar month closes (as the case may be): 1. SINGLE CASH operation — value exceeding US$10,000.00; a mixed cash+other-media transaction counts when the CASH component alone exceeds US$10,000.00; 2. MULTIPLE CASH operations — transactions ≤ US$10,000.00 that ACCUMULATED OVER A CALENDAR MONTH exceed US$10,000.00 (the report includes only the total amount and the accumulated cash value), due 5 días hábiles from the day after month end; 3. SINGLE OTHER-MEDIA operation — value exceeding US$25,000.00 (mixed counts when the other-media component alone exceeds US$25,000.00); 4. MULTIPLE other-media operations — ≤ US$25,000.00 accumulating over the calendar month beyond US$25,000.00, due 5 días hábiles after the month. "Otro medio" = any título valor other than paper money or coin, such as cheques or credit-card payments — THE OPERATIVE THRESHOLD REGIME surviving the law replacement via the kept instructivo (provenance chain: 72_ Art. 51 under 71_ Arts. 25+61; future reglamento supersedes — OQ-001) | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 51 pp.32-34 (EVID-248; txt PAGE 32-34) |
| LB-023 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 52 (first inciso + literals; the Banca-regional detail and the GAFI R.16 originator/beneficiary data block condensed): "Las instituciones financieras deberán reportar a la UIF de forma mensual y en los primeros cinco días hábiles con posterioridad a cada mes objeto de reporte, en los formularios diseñados por la UIF, la siguiente información: a) Transferencias electrónicas internacionales de fondos iguales o mayores a US$1,000.00 o su equivalente en moneda extranjera. b) Transferencias electrónicas locales generadas a través de dispositivos o aplicaciones electrónicas, iguales o mayores a US$1,000.00 o su equivalente en moneda extranjera. c) Remesas familiares iguales o mayores a US$200.00 o su equivalente en moneda extranjera." [Banca-regional detail inciso + the originator/beneficiary information block: nombre del cliente originador; número de cuenta del originador; número y tipo de documento de identidad; nombre del beneficiario; número de cuenta del beneficiario; nombre del banco administrador de la cuenta del beneficiario; número de identificación de la transacción — required for the literal a)/b) transfers, INCLUDING those below the thresholds; batch-file transfers carry complete originator and beneficiary data] | FINANCIAL INSTITUTIONS report monthly, within the FIRST FIVE DÍAS HÁBILES after each reported month, in the UIF forms: a) international electronic funds transfers ≥ US$1,000.00; b) local electronic transfers generated through devices or electronic applications ≥ US$1,000.00; c) family remittances ≥ US$200.00 — plus Banca Regional transaction detail, and the GAFI R.16 originator/beneficiary data (name, account, ID document type/number, beneficiary name/account/bank, transaction ID) on ALL the literal a)/b) transfers, even below threshold | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 52 pp.34-35 (EVID-248; txt PAGE 34-35) |
| LB-024 | Instructivo de la UIF (Acuerdo 380, kept in force), Art. 77 (lead + the GAFI-threshold incisos; the sociedad-services activity list condensed): "Para los efectos del presente instructivo y de conformidad con la Recomendación 22 del GAFI, tienen la calidad de actividades y profesiones no financieras designadas (APNFD), las siguientes, quienes deberán aplicar las normas establecidas en el presente instructivo, para el cumplimiento de las Recomendaciones 10, 11, 12, 15 y 17 del GAFI: i. Casinos y demás juegos de suerte o azar, cuando los clientes se involucran en transacciones financieras por un monto igual o mayor a tres mil dólares de los Estados Unidos de América. ii. Agentes inmobiliarios – cuando éstos se involucran en transacciones para sus clientes concerniente a la compra y venta de bienes inmobiliarios. iii. Comerciantes de metales preciosos y comerciantes de piedras preciosas – cuando éstos se involucran en alguna transacción en efectivo con un cliente por un monto igual o mayor a diez mil dólares de los Estados Unidos de América. iv. Abogados, notarios, contadores y auditor externo – cuando se disponen a realizar transacciones o realizan transacciones para sus clientes sobre las siguientes actividades: a. compra y venta de bienes inmobiliarios; b. administración del dinero, valores u otros activos del cliente; c. administración de las cuentas bancarias, de ahorros o valores; d. organización de contribuciones para la creación, operación o administración de empresas; e. creación, operación o administración de personas jurídicas, otras estructuras jurídicas y compra y venta de estas. Así mismo los abogados, notarios, contadores y auditores externos tendrán la obligación de reportar a la UIF las transacciones que hagan o se realicen ante sus oficios, mayores de diez mil dólares… v. Proveedores de servicios societarios cuando se disponen a realizar transacciones o realizan transacciones para un cliente sobre las siguientes actividades: a. actuación como agente de creación de personas jurídicas; b. actuación… como director o apoderado de una sociedad mercantil…; c. provisión de un domicilio registrado…; d. actuación… como fiduciario de un fideicomiso expreso…; e. actuación… como un accionista nominal para otra persona." | Per GAFI Recommendation 22, the APNFD are (applying the instructivo's norms for GAFI Recommendations 10, 11, 12, 15 and 17): i. casinos and games of chance, when clients engage in financial transactions of ≥ US$3,000; ii. real-estate agents transacting for clients; iii. precious-metals and precious-stones traders, when involved in a CASH transaction with a client of ≥ US$10,000; iv. lawyers, notaries, accountants and external auditors when transacting for clients on the five listed activities — AND they must REPORT to the UIF the transactions made or occurring before their offices that exceed US$10,000 (registering with the UIF for this purpose); v. sociedad-services providers (company-formation agent, nominal director/proxy, registered address provider, express-trust fiduciary, nominal shareholder) | `sv/sources/72_Instructivo_UIF_Acuerdo380_reform2023.pdf` | Art. 77 pp.49-51 (EVID-249; txt PAGE 49-51) |
| LB-025 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 28: "Es confidencial toda información requerida por la Fiscalía General de la República y/o por la UIF, así como las respuestas remitidas a éstas, relacionadas a requerimientos de información y a reportes de operaciones sospechosas, operaciones tentadas y actividades sospechosas, en cumplimiento a lo dispuesto en la presente ley y otras aplicables. Por tanto, los sujetos obligados no podrán dar a conocer la información antes referida a clientes, usuarios o terceros, auditores, ni a sus supervisores." "La información remitida a la Fiscalía General de la República o a la UIF, así como el envío de los reportes…, no constituirá violación de las restricciones sobre divulgación de información impuestas por vía contractual o por cualquier disposición legal, reglamentaria o administrativa. Asimismo, el secreto bancario, bursátil, así como la reserva de información en materia tributaria, no es aplicable a la información requerida por la Fiscalía General de la República y la UIF." | All information required by the FGR and/or the UIF, and the answers sent to them, relating to information requests and to suspicious-operation, attempted-operation and suspicious-activity reports, is CONFIDENTIAL: subjects may NOT disclose it to clients, users or third parties, auditors, or their supervisors (law-level NO-TIP-OFF). Sending the information/reports to the FGR or UIF is NOT a violation of contractual or legal/regulatory/administrative disclosure restrictions; bank, securities and tax secrecy do not apply to FGR/UIF-required information | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 28 p.22 (EVID-245; txt PAGE 22) |
| LB-026 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 26 (same article as `02_accounting-books.md` LB-013 — quoted IN FULL there; repeated here in abbreviated form for the by-id feed): "Los sujetos obligados deben mantener por un período no menor de quince años los registros necesarios sobre transacciones realizadas…, tales registros servirán para reconstruir cada transacción…" "Los sujetos obligados deben archivar y conservar la documentación de las operaciones… por el plazo mencionado en el inciso anterior, el cual se empezará a contar a partir de la fecha de la finalización de cada transacción. Los datos de identificación del cliente y archivos de cuentas también deberán conservarse por el mismo plazo, contado a partir de la terminación de la relación comercial o cierre de cuentas." | Obligated subjects must maintain for NOT LESS THAN FIFTEEN YEARS the records necessary on transactions performed (national and international, as originator or beneficiary) enabling each transaction's reconstruction; operation documentation for the same period counted from EACH TRANSACTION'S FINALIZATION; and client-identification data and account files for the same period counted from TERMINATION OF THE COMMERCIAL RELATION OR ACCOUNT CLOSURE — the uniform ≥15-year rule FEEDING `02_accounting-books.md` SV-CML-FR-028 rows d1/d2 BY ID (full verbatim = that file's LB-013; never restated here) | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 26 pp.20-21 (EVID-244; txt PAGE 20-21; via 02 LB-013) |
| LB-027 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 27 (first inciso + the DGA/retention incisos; BCR carve-out and seizure incisos condensed): "Toda persona que al ingresar o salir del territorio de la República por cualquier vía, independientemente de su nacionalidad, deberá declarar si transporta consigo billetes o instrumentos negociables al portador, en cualquier moneda o valores en la cuantía igual o superior a quince mil dólares de los Estados Unidos de América, o el equivalente en moneda extranjera, ya sea realizado por viajeros, por medio de correo o de transporte de carga. Asimismo, las personas jurídicas deberán declarar el ingreso o salida de billetes o instrumentos negociables al portador… en la cuantía igual o superior a quince mil dólares… por medio de correo o transporte de carga." "La Dirección General de Aduanas será competente para comprobar la veracidad de las declaraciones…" "La omisión, falsedad o inexactitud de la declaración provocará solamente la retención de los activos por parte de la Dirección General de Aduanas por un plazo de hasta noventa días, durante los cuales, la persona deberá justificar el origen lícito de los fondos retenidos y dicha entidad deberá notificar a la Fiscalía General de la República…" "En los casos de archivo, sobreseimiento o absolución, se devolverá lo retenido imponiéndole una multa del veinte por ciento de los activos retenidos, si se demostrare que existió negligencia en su declaración." | Every person entering or leaving the Republic by any means, regardless of nationality, must DECLARE bearer banknotes or negotiable instruments, in any currency, in an amount ≥ FIFTEEN THOUSAND US DOLLARS (US$15,000) or its foreign-currency equivalent — carried by travelers, mail or cargo; legal persons declare the same ≥US$15,000 for mail/cargo (BCR importations carved out). The Dirección General de Aduanas (DGA) verifies; omission, falsity or inexactitude triggers RETENTION of the assets for up to NINETY DAYS (licit-origin justification; FGR notified); on archive/dismissal/acquittal the retained assets are returned with a TWENTY-PERCENT MULTA of the retained assets if negligence is shown | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 27 p.21 (EVID-245; txt PAGE 21) |
| LB-028 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 34: "Por la comisión de infracciones graves cuando se trate de persona jurídica se impondrá a los sujetos obligados la sanción de multa de cincuenta (50) a quinientos (500) salarios mínimos mensuales del sector comercio del patrimonio del sujeto obligado. En el caso de personas naturales la sanción será de hasta doscientos (200) salarios mínimos mensuales para el sector comercio vigentes." "…se impondrá, además, la sanción de suspensión de la operación u operaciones vinculadas a la infracción cometida…, por el plazo de hasta doce meses…" "…se impondrá a los directores, administradores, gerentes, u otros funcionarios o empleados, auditores internos o externos…, se les impondrá la sanción de multa de hasta cien (100) salarios mínimos mensuales para el sector comercio vigentes." "…se impondrá, además, la sanción de separación del cargo, con inhabilitación para ejercer cargos de administración o dirección en la misma entidad o cualquier otra hasta por un plazo máximo de cinco años." Art. 35: "Por la comisión de infracciones muy graves cuando se trate de personas jurídicas, se impondrá la sanción de multa de quinientos uno (501) a mil (1000) salarios mínimos mensuales del sector comercio de su patrimonio. En el caso de personas naturales la sanción será desde doscientos uno (201) hasta cuatrocientos (400) salarios mínimos mensuales para el sector comercio vigentes." "…se impondrá, además, la sanción de cancelación de la operación del sujeto obligado que realice las prácticas ilegales, procediendo a pedir al Fiscal General de la República que solicite judicialmente la disolución y liquidación forzosa de la entidad." "…se impondrá… la sanción de multa desde ciento uno (101) hasta doscientos (200) salarios mínimos mensuales para el sector comercio vigentes." "…se impondrá, además, la sanción de separación del cargo, con inhabilitación… hasta por un plazo máximo de diez años." | GRAVE infractions: legal persons — multa of FIFTY (50) to FIVE HUNDRED (500) sector-commerce MONTHLY MINIMUM WAGES (SMM); natural persons — up to 200 SMM; responsible directors/administrators/managers/employees/internal or external auditors — multa up to 100 SMM; aggravated cases add suspension of the linked operation(s) for up to 12 months, and officer separation with INHABILITACIÓN for administration/direction offices up to FIVE YEARS. VERY GRAVE infractions: legal persons — 501 to 1000 SMM; natural persons — 201 to 400 SMM; officers — 101 to 200 SMM; aggravated cases add CANCELLATION of the operation with a request to the FGR for judicial forced dissolution and liquidation, and separation with inhabilitación up to TEN YEARS. All in SMM units of the SECTOR COMERCIO — dated values fed from the payroll wave's SMM rows by id (FR-222) | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Arts. 34-35 pp.24-25 (EVID-245; txt PAGE 24-25) |
| LB-029 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 39 (+ Arts. 30-33, 36-38 gloss): "Las infracciones graves y muy graves prescribirán a los diez años, contados desde la fecha en que la infracción hubiera sido cometida. En las infracciones derivadas de una actividad continuada, la fecha inicial del cómputo será la de la finalización de la actividad o la del último acto con el que la infracción se consume. En los casos en los que se demuestre que el sujeto obligado incurrió en maniobras para ocultar el incumplimiento, el plazo de la prescripción iniciará a partir del momento en el que el supervisor advierta la existencia de la falta. La prescripción se interrumpirá por cualquier acción del supervisor correspondiente destinada a realizar inspecciones o requerir documentos, reportes o informaciones, relacionada con la comisión de una infracción específica, y se hagan con conocimiento formal de los sujetos obligados. Las auditorías generales no interrumpirán ningún tipo de prescripción. Igualmente, se interrumpirá la prescripción por el inicio de un procedimiento sancionador o de un proceso penal por los mismos hechos." | Grave and very-grave infractions PRESCRIBE after TEN YEARS from the infraction date; for continuing-activity infractions, from the activity's end or the last consummating act; where the subject used CONCEALMENT maneuvers, the clock starts only when the supervisor discovers the lack. Prescription is INTERRUPTED by any supervisor action aimed at inspections or document/report/information requirements related to a SPECIFIC infraction with formal knowledge of the subjects — GENERAL AUDITS interrupt nothing — and by the start of a sanctioning procedure or criminal process on the same facts. Context (gloss): Art. 30 two-tier classification (grave/muy grave); Arts. 31/32 the infraction catalogs (grave: duty breaches, no-DD, no-report, no-corrective adoption, no-Oficialía, no-officer, no-Comité…; muy grave: revealing confidential information, obstructing supervisors, non-freezing, non-application of risk systems, making frozen funds available, non-conservation, no Art.-18 termination analysis, terminating before the Art.-18 window); Art. 33 administrator/director liability surviving cessation and ex-partners' solidarity up to liquidation quotas; Art. 36 graduation criteria; Art. 37 public sanctions registry (publication within 10 días hábiles of firmeza); Art. 38 payment within 30 days at Tesorería with mandamiento de pago, tax-moratory interest on delay | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 39 pp.26-27 + Arts. 30-38 pp.22-26 (EVID-245; txt PAGE 22-27) |
| LB-030 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Arts. 56/58/60/61/62 (transitory block): Art. 56: "La UIF tendrá un plazo de seis meses contados a partir de la publicación de la presente ley, para emitir los instructivos que considere pertinentes para su cumplimiento. Las demás autoridades competentes… tendrán un plazo de nueve meses contados a partir de su publicación, para emitir la normativa técnica correspondiente." Art. 58: "Los entes de supervisión contarán con un plazo de seis meses después de la entrada en vigencia de la presente ley, para llevar a cabo un diagnóstico de las entidades que se incorporan bajo su supervisión…; los sujetos obligados contarán con un plazo de doce meses para adecuarse a los requerimientos de los supervisores." Art. 60: "El presidente de la República dentro del plazo de 90 días, a partir de la vigencia de esta ley, deberá emitir el reglamento de la presente ley." Art. 61 (incisos): "La presente ley deroga la Ley Contra el Lavado de Dinero y de Activos contenida en el Decreto Legislativo n.° 498, de fecha 2 de diciembre de 1998, publicado en el Diario Oficial N° 240, Tomo n.° 341, de fecha 23 de diciembre de 1998; así como cualquier otra normativa que la contraríe." "Permanecerán vigentes el Decreto Ejecutivo n.° 2 de fecha 21 de enero de 2000…, que contiene el Reglamento de la Ley Contra el Lavado de Dinero y de Activos, así como el Instructivo para la Prevención, Detección y Control del Lavado de Activos…, mientras no se emitan el reglamento y el instructivo correspondientes a la presente ley." Art. 62: "La presente ley entrará en vigencia ocho días después de su publicación en el Diario Oficial." | Adaptation clocks: the UIF has SIX MONTHS FROM PUBLICATION (9-oct-2025 ⇒ by ≈2026-04-09) to issue its instructivos; the other competent authorities NINE MONTHS from publication (⇒ ≈2026-07-09) for the technical norms; supervisors have SIX MONTHS FROM VIGENCIA (17-oct-2025 ⇒ ≈2026-04-17) for the onboarding diagnostics; obligated subjects TWELVE MONTHS FROM VIGENCIA (⇒ ≈2026-10-17) to adapt to supervisor requirements; the President NINETY DAYS FROM VIGENCIA (⇒ ≈2026-01-15) to issue the Reglamento. Art. 61 repeals the 1998 law wholesale while the old reglamento (D.E. 2-2000) and old instructivo remain in force until the new reglamento and instructivo issue; the law entered into force EIGHT DAYS AFTER PUBLICATION ⇒ 2025-10-17 (Art. 62) — the regime-cutover date | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Arts. 55-62 pp.31-33 (EVID-241/246; txt PAGE 31-33) |
| LB-031 | Resolución CVPCPA N° 111 (27-feb-2026; Acta 10/2026; no D.O. print data on face — publication ordered per LREC Art. 36, issue unpinned, EVID-420 OQ-1 non-blocking; the Council acting as D.L. 426 supervisor of the Art.-7-numeral-7 subjects, per the Art. 12 fifth-inciso recital: "…El Consejo de Vigilancia de la Profesión de Contaduría Pública y Auditoría, supervisará a los sujetos obligados que señala el artículo 7 numeral 7 de la presente ley, en lo relacionado a los contadores y auditores"): "El Consejo de Vigilancia de la Profesión de Contaduría Pública y Auditoría, como organismo de supervisión, fiscalización y vigilancia de los sujetos obligados requiere a sus regulados y supervisados, completar información, que permitirá realizar el diagnóstico requerido por el artículo 58 de la Ley Especial para la Prevención, Control y Sanción del Lavado de Activos, Financiamiento del Terrorismo y Financiamiento de la Proliferación de Armas de Destrucción Masiva, a fin de que este Consejo establezca la matriz conforme a la Ley Especial… según Decreto Legislativo No. 426, de fecha 7 de octubre de 2025, publicado en el Diario Oficial N[° 190,] Tomo No. 449, de fecha 9 de octubre de 2025…" "Aclárase a los profesionales regulados por este Consejo que, a la fecha, no se han emitido lineamientos de la metodología para el desarrollo de la práctica profesional respecto a la nueva ley, ya que de conformidad al artículo 58 de la Ley [E]special…, los [profesio]nales tendrán un plazo de doce meses a partir de la vigencia de la mencionada ley, p[ara ad]cuarse a los requerimientos que el Consejo u otros entes facultados, emitan posteriormente." "Déjese sin efecto la Resolución 237 de fecha 13 de septiembre de 2[…]" (year OCR line-cut; cross-pinned by the cvpcpa post resolucion-237-2023, dated 2023-09-13) | AWARENESS/CONFIG-OFF (W28 acquisition, cited on arrival; no FR rides this row): the CVPCPA's Feb-2026 supervisor move = the **Art.-58 diagnostic information requirement** on its contador/auditor regulados (addressee = the professionals, not product behavior) + the EXPRESS statement that **NO methodology lineamientos for the new law existed as of 27-feb-2026** — the strongest supervisor-side OQ-001 watch datum (the law's Art. 56/60 deadlines were already past: instructivos ≈2026-04-09, technical norms ≈2026-07-09, reglamento ≈2026-01-15, all still absent) — with sujetos holding the **twelve-months-from-vigencia adaptation window** (⇒ ≈2026-10-17, corroborating LB-030's derivation; recital cross-pins 71_'s D.O. 190 T.449 print). Derogates Res. 237-2023 (the AML instructivo-chain exhortation). Product consequence: NONE until lineamientos/reglamento issue — the FR-194 adaptation-window rows and the OQ-001 watch stand unchanged | `sv/sources/128_Resolucion_CVPCPA_111_2026.pdf` | Resolutivo + Aclárase + derogation, 2-pp scan OCR (EVID-419/420; txt PAGE 1-2; garbled spans bracket-marked per the EV quote discipline) |

## 3. Functional Requirements

### 3.1 Regime version configuration and authority chain (Arts. 61-62)

- **SV-CML-FR-193:** The system shall implement the AML regime as a DATED
  VERSION CONFIG with the 2025-10-17 cutover: regime rows identify the
  governing law as D.L. 426 (effective 2025-10-17, wholesale replacement
  of D.L. 498-1998 per Art. 61) for facts from that date, and the DEAD
  1998 regime (15_) as the historical row for pre-cutover facts; every
  computation, threshold, clock and duty reads the regime row of its
  operative date, and the 1998 law's law-text thresholds (its Art. 9
  US$10,000/US$25,000 values) are DEAD — never resolvable as current
  authority. Each regime row carries the authority chain of §2
  (71_ law > 72_ kept instructivo > 17_ kept reglamento for gaps; kept
  instruments operative qua the Art. 61 transitory), and direct 71_ rules
  displace conflicting kept-instrument values (working rulings: 24h ROS
  transmit clock vs 72_ Art. 43; ≥25% beneficiario final vs 72_ Arts.
  12/20 — OQ-003). (LB-030; EVID-241)
- **SV-CML-FR-194:** The system shall expose the transitory ADAPTATION
  WINDOWS as dated configuration rows, derived from the publication date
  (2025-10-09) and vigencia (2025-10-17) and never recomputed —
  UIF instructivos due ≈2026-04-09 (publication + 6 months, Art. 56);
  other authorities' technical norms ≈2026-07-09 (+ 9 months, Art. 56);
  supervisor onboarding diagnostics ≈2026-04-17 (vigencia + 6 months,
  Art. 58); subjects' adaptation to supervisor requirements ≈2026-10-17
  (vigencia + 12 months, Art. 58); presidential Reglamento ≈2026-01-15
  (vigencia + 90 days, Art. 60) — each row surfacing an overdue state
  while the pending instrument has not issued, feeding the
  pending-reglamento watch (OQ-001: no new reglamento/instructivo visible
  on uif.gob.sv as of 2026-08-18, 10+ months past the Art. 56 deadline —
  the kept instruments remain the operative layer; supervisor-side
  corroboration: the CVPCPA's own Res. 111-2026 states NO lineamientos
  issued as of 27-feb-2026 while it launches the Art.-58 diagnostic
  requirement — LB-031).
  (LB-030; LB-031; EVID-246/419/420)

### 3.2 Sujeto obligado classification (Arts. 7-8, 12-13)

- **SV-CML-FR-195:** The system shall maintain, per company record, an
  AML *sujeto obligado* profile with exactly one classification from the
  Art. 7 catalog — the ten categories: 1 financial institutions
  (sub-catalog a-o per LB-001); 2 D.L. 339 associations/societies/credit
  unions/federations/confederations + Código de Comercio savings-and-loan
  societies; 3 exclusive systematic lenders; 4 casinos and games of
  chance; 5 real-estate intermediaries (for-client transactions); 6
  precious-metals and -stones traders; 7 activity-listed lawyers,
  notaries, accountants and auditors; 8 transporters of money or values;
  9 digital-asset and bitcoin service providers; 10 political parties —
  plus the OSFL high-exposure flag (Art. 7 tail); an ordinary company
  matching NO category carries an INACTIVE AML profile: none of
  §3.3-3.9's duties activate, and the retention-matrix AML rows of
  SV-CML-FR-028 d1/d2 do not apply (applicability fed by id).
  (LB-001; EVID-242)
- **SV-CML-FR-196:** The system shall model the non-financial categories
  as ACTIVITY-TRIGGERED rather than entity-type-triggered configuration:
  category 5 attaches only when the subject engages in for-client
  real-estate purchase/sale transactions; category 7 attaches only when
  the professional performs, directly or indirectly, the five listed
  activities for clients (real-estate purchase/sale; management of
  client money/securities/assets; management of bank/savings/securities
  accounts; organization of contributions for enterprise
  creation/operation/administration; creation/operation/administration of
  legal persons or structures and purchase/sale of commercial entities);
  category 3 only for exclusive systematic lending; categories 4/6/8 by
  the named activity — the trigger set stored as a dated activity catalog
  the profile evaluates (manual assertion with reviewed evidence; the
  system never auto-infers merchant activity as subject status).
  (LB-001; EVID-242/249)
- **SV-CML-FR-197:** The system shall expose the Art. 8 dynamic-scope
  mechanism as a WATCH-FEED of dated inclusion/exclusion resolutions:
  UIF proposals to CIPLAFT grounded on (a) national/sectoral risk or
  mutual-evaluation findings or (b) supervisor-noted risk conditions,
  recorded as dated rows (resolution id, scope sector/activity, in/out,
  effective date) that re-evaluate affected profiles' category
  applicability on their effective dates — no resolution rows ship in the
  box (none evidenced in corpus, OQ-004); the feed defaults empty.
  (LB-002; EVID-242)
- **SV-CML-FR-198:** The system shall derive, from the profile's
  category, the SUPERVISOR ROUTING of Art. 12 as configuration: category
  1 → SSF; category 9 → Comisión Nacional de Activos Digitales (with SSF
  supervision for bitcoin operations under BCR Comité de Normas norms);
  category 2 → the special-law competent authority for the
  D.L.-339-specific associations/federations/confederations and the
  Superintendencia de Obligaciones Mercantiles for the savings-and-loan
  societies and credit unions; categories 3/4/5/6/8 → Superintendencia
  de Obligaciones Mercantiles, with ONLINE casinos routed to the Lotería
  Nacional de Beneficencia; category 7 → Consejo de Vigilancia de la
  Profesión de Contaduría (accountants/auditors) and Corte Suprema de
  Justicia (lawyers/notaries); category 10 → Tribunal Supremo Electoral;
  the high-exposure OSFL flag → Ministerio de Gobernación — recorded as
  the *ente de supervisión* field consumed by the registration and notice
  FRs (risk-based supervision intensity per Art. 13 is the supervisor's
  own methodology, informational only).
  (LB-003; EVID-242/246)

### 3.3 Compliance program (Art. 9; 72_ Arts. 3-8)

- **SV-CML-FR-199:** The system shall track, on the active AML profile,
  the DOUBLE REGISTRATION duty and its data currency: registration before
  the routed *ente de supervisión* AND before the UIF (universal, "sin
  excepción", on the UIF's platform) with the registration form's
  beneficiario-final information; a data-change event opens a
  15-*días hábiles* update clock (72_ Art. 3) computed on the shared
  días-hábiles engine (SV-FREP-FR-203, consumed by id), surfacing an
  overdue state. (LB-004; LB-005; EVID-243/247)
- **SV-CML-FR-200:** The system shall model the compliance-program
  chassis as YEARLY records approved by the top governance organ: the
  annual work plan (71_ Art. 9.2; 72_ Art. 7 f)) and the annual training
  plan (71_ Art. 9.6; 72_ Art. 7 g)), each carrying year, approval
  evidence and completion state; plus the risk-management-system
  component checklist (policies-and-procedures manual, DD procedures,
  código de ética, monitoring system, internal audit plan — 72_ Art. 7
  d)) and the individualized risk-based-approach record (71_ Art. 9.3)
  with its documented justification; the client-facing policy coverage
  set (DD, operation control, associated-risk management — 72_ Art. 5
  closing) is surfaced as a completeness check, with client-acceptance
  policies and information-withholding consequences flagged (72_ Art. 5
  e)). (LB-004; LB-006; LB-007; EVID-243)
- **SV-CML-FR-201:** The system shall track the program's verification
  loop: an ANNUAL risk-based internal-audit evaluation of the AML
  policies/procedures — including validation of the sending of regulated
  reports — reported to the governance organ (with the external-auditor
  fallback for subjects without internal audit), recorded as a yearly
  evaluation row; and the INTERNAL-UNUSUAL-REPORT pipeline duty of
  Art. 9.7 (the analysis machinery itself is owned by §3.6 FR-212):
  employees' detection reports feed the officer analysis whose suspicious
  outcome is informed to the UIF, with confidentiality of the internal
  reports and of the reporting employees' identity enforced (§3.6
  FR-219). (LB-004; LB-008; EVID-243/249)

### 3.4 Customer due diligence (Arts. 15-19; 72_ Arts. 10-21)

- **SV-CML-FR-202:** The system shall implement the DD LADDER on every
  client/counterparty of an active subject, applied when relations are
  established, on occasional transactions above the applicable
  cash-report threshold, on suspicion, or on doubts about identification
  data (71_ Art. 15 trigger inciso; 72_ Art. 14-A kin): SIMPLIFIED —
  low-risk clients/products only, identity verification never waived,
  never applicable under suspicion (72_ Art. 4); STANDARD — the initial
  level for all non-high-risk clients: identification of client,
  *beneficiario final* and representatives, nature and purpose of the
  relation, origin of funds; ENHANCED — high-risk clients: collection
  and verification of source-of-wealth/source-of-funds information, plus
  the kept instructivo's intensified measures (senior-management approval
  to establish or continue the relation, interviews/visits with written
  report, intensified continuous monitoring — 72_ Art. 13, gloss). The
  ladder assignment is recorded per client with its risk rating and
  documented justification.
  (LB-009; LB-005; EVID-243/249)
- **SV-CML-FR-203:** The system shall capture, per client legal person,
  the BENEFICIARIO FINAL chain resolved to NATURAL PERSONS at the law's
  participation threshold — ≥25% of capital or voting rights, direct or
  indirect, or control of management by other means (71_ Art. 15) —
  stored as a dated config value with its provenance chain (law = 71_
  Art. 15; kept instructivo 72_ Arts. 12/20 print 10% — DISPLACED by the
  later law under §2; supersession watch OQ-003/OQ-001), with the
  listed-company carve-out (exchange-listed owners subject to disclosure
  requirements), with own-account/third-account declaration capture, and
  with the DD-side requirement that identity be verified BEFORE
  establishing the relation or executing any operation (72_ Art. 20).
  (LB-009; LB-010; EVID-243/249)
- **SV-CML-FR-204:** The system shall enforce NOMINATIVE-ONLY client
  records — no anonymous or coded accounts or relations, no incorrect or
  fictitious names — and the KYC-REFUSAL route: a client failing to
  provide the required identification information/documentation blocks
  the start of the commercial relation (subjects "podrán abstenerse de
  iniciarlas"), with the refusal event queued for the officer's
  tentativa analysis (a possible attempted-suspicious-transaction
  report, §3.6 FR-212) rather than silently dropped.
  (LB-009; LB-011; EVID-243/249)
- **SV-CML-FR-205:** The system shall implement the PEP tier: a PEP
  flag on natural-person clients/partners resolved against the Art. 19
  national (a-n) and foreign (a-h) position catalogs (the UIF owns and
  updates the authoritative list — catalogs stored as configuration, not
  as an embedded freeze); PEP status persists FIVE YEARS past the cession
  of the last appointment (computed expiry on the cese date); family
  members to the second degree of consanguinity/affinity, spouses, life
  partners and close associates receive the enhanced-DD measures without
  themselves being classified PEP; and PEP relations carry the law's
  intensified permanent monitoring (71_ Art. 9.14, gloss).
  (LB-012; EVID-243)
- **SV-CML-FR-206:** The system shall implement the US$1,000
  LOW-VALUE-ACCOUNT carve-out and the termination-notice mechanics of
  Art. 18 as DATED CONFIG: when an unmanageable risk leads the subject
  to decide termination of the contractual/business relation, a UIF
  notification (with the risk analysis attached) is generated only when
  the account funds exceed US$1,000 (the closure-notification threshold
  — value as dated config with provenance 71_ Art. 18, never
  hardcoded); upon notification the system opens the UIF's
  10-*días hábiles* response window (engine-computed, SV-FREP-FR-203 by
  id) during which the relation may NOT be terminated — termination is
  permitted only once the window lapses without UIF response or upon the
  UIF's no-measures answer; termination executed inside the window is a
  muy-grave infraction exposure (Art. 32.8, gloss — FR-223).
  (LB-013; EVID-243/245)

### 3.5 Officer architecture (Arts. 20-23; 72_ Arts. 71-80)

- **SV-CML-FR-207:** The system shall derive the OFFICER ARCHITECTURE
  from the profile: subjects supervised by the SSF, the Comisión
  Nacional de Activos Digitales and category 2 MUST establish an
  *Oficialía de Cumplimiento* (titular officer + suplente, appointed by
  the junta directiva or equivalent, autonomous, direct functional
  relation with the top authority); other supervised subjects may
  dispense with the Oficialía but must designate an officer and
  suplente; NATURAL-PERSON subjects of categories 5-9 need not
  designate an officer at all — the person itself applies every control
  (self-responsible profile); the non-Oficialía juridical population
  designates an *Encargado de Cumplimiento* per FR-210. The ROS
  presentation duty belongs to the officer (71_ Art. 9.7).
  (LB-014; EVID-243/249)
- **SV-CML-FR-208:** The system shall enforce the COMITÉ DE PREVENCIÓN
  composition invariant for every subject that must appoint an Oficialía
  (FR-207 first population): a Comité record of AT LEAST THREE members,
  of which at least one belongs to the *máximo organismo de dirección*
  (top governance organ) and one is the compliance officer —
  non-conforming compositions surface as violations; groups/conglomerados
  appointing a single officer may keep a SINGLE Comité with a SINGLE
  acta book provided every group entity is represented in it
  (representation flag per member entity). (LB-015; EVID-243)
- **SV-CML-FR-209:** The system shall implement the OFFICER NOTICE
  clocks: every designation or change of the officer, suplente or
  compliance-office member opens a 15-*días hábiles* notice duty to the
  UIF and the routed supervisors (both the 15-day notice and the
  5-day acceleration below are law level, 71_ Art. 9.8; 72_ Art. 7 m)
  adds the documentation set: acta certification, resignation or
  dismissal copy; 17_ Art. 4 g) kin for the liaison roles; a dismissal,
  transfer, resignation or function-related sanction of the officer
  ACCELERATES the notice to 5 días hábiles from the effective date
  (engine-computed, SV-FREP-FR-203 by id), with the dismissal-resolution
  foundation recorded. (LB-004; LB-007; LB-016; EVID-243/233)
- **SV-CML-FR-210:** The system shall implement the APNFD/other-subject
  ENCARGADO DE CUMPLIMIENTO regime (72_ Arts. 71-80, kept): Encargado +
  suplente appointed by the top governance organ, RESIDENT in the
  country, UIF-REGISTERED (registration tracked as metadata), meeting
  the requirement tiers (full set — training, regulatory knowledge,
  university degree, business knowledge; or the lighter set for the
  listed rubros — training, regulatory knowledge, activity experience;
  natural-person subjects may serve themselves or contract an
  Encargado); the ANTI-RETALIATION guard is recorded as an invariant —
  no dismissal, sanction or removal for performing the role's functions
  (both the general and the APNFD Encargado texts); the Encargado's
  annual report to the governance organ (management results, UIF-report
  compliance, detection effectiveness) is tracked as a yearly record;
  and the Encargado (or officer) owns the exclusive ROS-decision
  competence with documented evidence of every analysis.
  (LB-017; EVID-249)

### 3.6 Detection and reporting (Arts. 24-25, 28; 72_ Arts. 42-52, 77; 17_ Arts. 3-4, 12-18)

- **SV-CML-FR-211:** The system shall provide a CONFIGURABLE RED-FLAG
  DETECTION RULE ENGINE seeded with the kept reglamento's catalogs
  (17_ Arts. 12-18): the Art. 12 generic definition (unusual operations,
  off-pattern, periodic-without-purpose, inconsistent with the client's
  activity) plus the detail families — structuring (just under the
  reportable amount), velocity/aggregation (day-to-day and
  inhábile-hour transfers, sub-threshold deposits consolidated then sent
  abroad), activity-consistency (instruments disproportionate to
  activity), KYC-refusal/evasion, pattern-shift (cash growth without
  reported growth, denomination anomalies) — each rule's parameters
  (incl. any structuring reference value) resolved from the CURRENT
  dated threshold config of FR-214, never hardcoded; the engine's
  output is CASE CREATION in the FR-212 pipeline — it NEVER
  auto-transmits any report to the UIF (reporting judgment is the
  officer's/Encargado's exclusive competence, 72_ Arts. 43/73 h)).
  (LB-018; EVID-234)
- **SV-CML-FR-212:** The system shall implement the INTERNAL CASE
  PIPELINE with states and evidence: DETECTED (employee report, red-flag
  engine case, tentativa event — incl. KYC refusal and presumptively
  false documents, which route as attempted-suspicious) → ANALYSIS
  (owned by the Oficialía/Encargado) → DETERMINATION — suspicious
  (→ ROS transmit state, FR-213) or DISMISSED (documented rationale
  mandatory; false-positive minimization duty, 72_ Art. 46); every state
  transition is stamped and evidenced, the analysis deadline discipline
  is FR-213's clock, and press-mention alone is no ROS trigger without a
  founded analysis (72_ Art. 50). (LB-019; EVID-249)
- **SV-CML-FR-213:** The system shall implement the ROS CLOCKS of
  Art. 24 on every suspicious determination: from DETECTION of the
  unusual operation, an analysis window of 15 días hábiles, extendable
  ONCE by the same period upon the officer's PRIOR request to the UIF
  (extension request recorded; a second extension request is refused —
  the window hardens); once the analysis closes with a suspicious
  determination, a TRANSMIT clock of 24 HOURS runs (date/time
  arithmetic; the kept 72_ Art. 43 5-días-hábiles transmit value is
  displaced by the law under the §2 authority order — working ruling,
  OQ-003); the ROS object is marked intelligence-only — confidential,
  no probative value, never incorporable into administrative/judicial
  files — and the AMOUNT of the operation is IRRELEVANT to ROS
  applicability (no threshold gates the pipeline).
  (LB-020; LB-019; EVID-244/249)
- **SV-CML-FR-214:** The system shall implement the REGULATED-OPERATIONS
  MONITOR with the full threshold AUTHORITY CHAIN as dated
  configuration: the law delegates content and thresholds to the future
  Reglamento (71_ Art. 25, GAFI-aligned — delegation recorded on every
  row); the OPERATIVE values load from the kept instructivo (72_ Art. 51)
  under the Art. 61 transitory — single-event CASH > US$10,000;
  monthly-cumulative cash (each ≤ US$10,000) > US$10,000; single-event
  OTHER-MEDIA > US$25,000; monthly-cumulative other-media
  (each ≤ US$25,000) > US$25,000; "otro medio" = any *título valor*
  other than paper money/coin (cheques, card payments) — with
  MIXED-PAYMENT DECOMPOSITION (a mixed transaction counts as cash when
  the cash component alone exceeds US$10,000, as other-media when the
  other-media component alone exceeds US$25,000; the report carries the
  TOTAL plus the instrument-component value), the LINKED-TRANSACTIONS
  flag ("que parezcan estar vinculadas entre sí" — same client/user,
  apparent linkage), and DIGITAL-ASSET transactions inside the report
  scope (71_ Art. 25); the clocks — 5 días hábiles counted from the day
  AFTER the operation (singles) or after month end (multiples) — run on
  the shared días-hábiles engine (SV-FREP-FR-203, consumed by id);
  issuance of the new Reglamento re-anchors the values (supersession
  watch OQ-001; never hardcoded). (LB-021; LB-022; EVID-244/248)
- **SV-CML-FR-215:** The system shall implement the ACCUMULATION WINDOW
  mechanics for the monthly-cumulative monitors of FR-214: the operative
  window is the CALENDAR MONTH of 72_ Art. 51 (accumulation per
  *mes calendario*, report due 5 días hábiles after month end); the kept
  reglamento's alternative window definition — 30 CONTINUOUS DAYS
  counted BACK from the latest transaction, with the cumulative total
  crossing the threshold inside the window (17_ Art. 3, kept mechanics
  co-cite) — is recorded on the config as the rolling-window detection
  variant for case-creation purposes (a same-month crossing under the
  calendar-month rule satisfies both), its colones amounts and 3-day
  clock being DEAD superseded values never loaded.
  (LB-022; LB-016; EVID-248/232)
- **SV-CML-FR-216:** The system shall implement, as INSTITUTION-TIER
  configuration (applicable to the financial-institution categories of
  the profile only), the monthly aggregate reports of 72_ Art. 52
  (operative values, dated config, same authority chain as FR-214):
  international electronic funds transfers ≥ US$1,000; local electronic
  transfers through devices/applications ≥ US$1,000; family remittances
  ≥ US$200 — due within the FIRST 5 días hábiles after each reported
  month (engine-computed by id), carrying the GAFI R.16
  originator/beneficiary data set (originator name/account/ID type and
  number; beneficiary name/account/bank; transaction id) on ALL the
  covered transfers INCLUDING those below threshold, plus the
  Banca-Regional detail rows. (LB-023; EVID-248)
- **SV-CML-FR-217:** The system shall implement the APNFD GAFI
  activity-report triggers of 72_ Art. 77 as DATED CONFIG on the
  activity-triggered profiles: casinos — client financial transactions
  ≥ US$3,000; precious-metals/-stones traders — CASH transactions with
  a client ≥ US$10,000; lawyers/notaries/accountants/external auditors
  — the five listed for-client activities as DD-apply triggers PLUS the
  report duty on transactions made or occurring before their offices
  exceeding US$10,000 (with UIF registration for that purpose);
  sociedad-services providers (company-formation agent, nominal
  director/proxy, registered-address provider, express-trust fiduciary,
  nominal shareholder) as an activity catalog; the trigger values ride
  the same provenance chain and supersession watch as FR-214
  (kept-instructivo values; 71_ Art. 15 b) confirms the casinos/metals
  GAFI amounts pass to the Reglamento). (LB-024; LB-009; EVID-249/243)
- **SV-CML-FR-218:** The system shall treat the UIF REPORT FORMATS AND
  CHANNELS as an EXTERNAL-INTERFACE ASSUMPTION: the UIF owns the
  authorized formats and transmission channels (71_ Arts. 3-4 i-zone
  and 24; 72_ Arts. 48/51 — "plataforma electrónica desarrollada por la
  UIF"; the goAML platform is the operative channel observed on
  uif.gob.sv) — the system produces the case/export data payloads and
  deadlines for the ROS, regulated-ops and aggregate reports, and
  records acknowledgment evidence, but performs NO built-in
  transmission; format specs are not in the corpus (17_ OQ-2 kin) and
  any connector is configuration, not shipped logic.
  (LB-020; EVID-246/244)
- **SV-CML-FR-219:** The system shall enforce the NO-TIP-OFF and
  confidentiality guard at LAW level (Art. 28; 17_ Art. 4 j) kept kin):
  AML case records, analyses, ROS objects, UIF requests and responses
  are confidential — never disclosed to clients, users, third parties,
  auditors or the supervisors themselves (save the FGR/UIF channel),
  with access controls keeping case content invisible to client-facing
  users and portal surfaces; reporting to the FGR/UIF is recorded as
  NOT a breach of contractual or legal/regulatory disclosure
  restrictions, and bank/securities/tax secrecy does not bar FGR/UIF
  information — a deliberate disclosure is a muy-grave infraction
  exposure (Art. 32.1, FR-223). (LB-025; LB-016; EVID-245/233)

### 3.7 Retention feed (Art. 26)

- **SV-CML-FR-220:** The system shall FEED the AML retention rows of
  the SOQ-28 canonical matrix BY ID — `02_accounting-books.md`
  SV-CML-FR-028 rows d1 (transaction records, ≥15 years from each
  transaction's finalization) and d2 (client-identification data and
  account files, ≥15 years from relation end/account closure) — by
  publishing the profile's *sujeto obligado* applicability flag to that
  matrix's consumer field (SV-CML-FR-028 rule ii), including the
  pre-cutover conservative note (records predating 2025-10-17 kept 15y
  too, longest-per-object discipline, owned by 02); the retention
  periods, anchors and purge machinery are OWNED by SV-CML-FR-028/029
  and are never restated in this file. (LB-026; EVID-244)

### 3.8 Border declaration content note (Art. 27)

- **SV-CML-FR-221:** The system shall expose the US$15,000
  border-cash declaration regime as INFORMATIONAL CONTENT only (dated
  config value): every person entering/leaving by any means declares
  bearer banknotes/negotiable instruments ≥ US$15,000 (natural persons
  as travelers/mail/cargo; legal persons for mail/cargo); the DGA
  verifies; omission/falsity/inexactitude → retention up to 90 days
  with FGR notice, return on archive/dismissal/acquittal with a 20%
  negligence multa on the retained assets — a state-side administrative
  workflow (Aduanas/DGA interface kin) with NO Odoo-side computation,
  tracked as awareness content for EXW/FOB logistics operations and
  cross-border cash movements recorded in treasury.
  (LB-027; EVID-245)

### 3.9 Sanctions (Arts. 29-39)

- **SV-CML-FR-222:** The system shall implement the administrative
  SANCTIONS VALUE MODEL in SMM *sector-comercio* units as dated
  configuration: GRAVE — legal-person multa 50-500 SMM, natural-person
  multa ≤200 SMM, responsible officer/director/manager/employee/auditor
  multa ≤100 SMM, aggravated: operation suspension ≤12 months and
  separation with inhabilitación ≤5 years; MUY GRAVE — legal-person
  multa 501-1000 SMM, natural-person 201-400 SMM, officers 101-200 SMM,
  aggravated: operation cancellation + FGR request for judicial forced
  dissolution/liquidation and separation with inhabilitación ≤10 years;
  a computed multa = SMM count × the dated sector SMM value of the
  sanction date, the SMM value being OWNED by the payroll wave
  (SV-PAY-FR-011 dated tariff rows via the SV-PAY-FR-022 sector
  mapping, consumed by id; the law's "sector comercio" ↔ 16_'s
  "comercio y servicios" row naming = SOQ-18 kin, resolved by that
  config) — never hardcoded; sanctions exposure is surfaced on the
  duty map, not imposed by the system (imposition belongs to the
  supervisors). (LB-028; EVID-245)
- **SV-CML-FR-223:** The system shall record the INFRACTION CATALOGS
  and graduation as exposure metadata mapped to this file's duties:
  grave (duty breaches — Art. 9 program items FR-199..201, no-DD
  FR-202..206, no-report FR-213/214, no-corrective adoption, no
  Oficialía FR-207, no-officer, no-Comité FR-208) and muy grave
  (confidentiality breach FR-219, supervisor obstruction, freezing
  breaches, risk-system non-application, frozen-funds disposal,
  non-conservation FR-220, no Art.-18 termination analysis FR-206,
  termination inside the Art.-18 window FR-206); graduation per Art. 36
  (amount/benefit, spontaneous cure, concealment, damage,
  gravity/duration, intentionality, cooperation);
  administrator/director personal liability surviving cessation and
  ex-partner solidarity to liquidation quotas (Art. 33); the public
  sanctions registry and the 30-day payment duty at Tesorería with
  mandamiento de pago (Arts. 37-38) as informational exposure.
  (LB-029; EVID-245)
- **SV-CML-FR-224:** The system shall implement the sanctions
  PRESCRIPTION model of Art. 39: a 10-YEAR clock per infraction counted
  from the infraction date; for continuing-activity infractions, from
  the activity's end or the last consummating act; a CONCEALMENT ANCHOR
  — where the subject incurred concealment maneuvers, the clock starts
  at the supervisor's discovery of the lack; INTERRUPTION events
  recorded per infraction (targeted supervisor inspections/document
  requirements with formal knowledge; sanctioning-procedure or
  criminal-process initiation on the same facts) with the express rule
  that GENERAL AUDITS interrupt nothing; the model surfaces
  prescribed/not-prescribed states on recorded exposure items only.
  (LB-029; EVID-245)

## 4. Data Model

Layer semantics: the AML compliance layer is Odoo-native bookkeeping of
configuration, cases and clocks — all entities live in the client (wave
default `odoo`); the only external-interface surface is the UIF/goAML
transmission (FR-218 — assumption, no shipped connector). The system
never emulates the UIF, the supervisors, CIPLAFT, the DGA or the
Tesorería; sanctions are exposure records, not impositions.

**AML profile (on res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_aml_regime | dated row | dl498_1998 (historical, pre-2025-10-17) · dl426 (current, from 2025-10-17) — with authority-chain attributes | FR-193 |
| res.company | sv_cml_aml_adaptation_windows | dated rows | instructivos ≈2026-04-09 · technical norms ≈2026-07-09 · diagnostics ≈2026-04-17 · subject adaptation ≈2026-10-17 · reglamento ≈2026-01-15 (overdue flags feed the OQ-001 watch) | FR-194 |
| res.company | sv_cml_aml_sujeto_obligado | select | inactive · cat1_financieras (a-o) · cat2_dl339 · cat3_prestamistas · cat4_casinos · cat5_inmobiliarios · cat6_metales · cat7_profesionales · cat8_transporte_valores · cat9_activos_digitales · cat10_partidos · osfl_alta_exposicion | FR-195 |
| res.company | sv_cml_aml_activity_triggers | config set | per-category activity gates (cat5 for-client real-estate; cat7 a-e activity list; cat3 exclusive systematic lending; cat4/6/8 named activity) | FR-196 |
| l10n_sv_commerce.aml.soj.resolution | scope · direction · effective_on · basis | dated rows | sector/activity in/out; basis = risk_evaluation · supervisor_conditions (empty feed; OQ-004) | FR-197 |
| res.company | sv_cml_aml_supervisor | computed | ssf · cnad · som · loteria_nacional (online casinos) · consejo_contaduria · csj · tse · gob_gobernacion (OSFL) · dl339_authority | FR-198 |
| res.company | sv_cml_aml_uif_registered_on · sv_cml_aml_supervisor_registered_on · sv_cml_aml_data_update_due | date | registration + 15-días-hábiles update clock (engine SV-FREP-FR-203 by id) | FR-199 |
| res.company | sv_cml_aml_retention_applicability | consumed flag | feeds `02` SV-CML-FR-028 rows d1/d2 by id | FR-220 |

**Program, DD and officers:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.aml.program.year | year · kind · approved_by · state | yearly rows | work_plan · training_plan · audit_evaluation · encargado_annual_report | FR-200, FR-201, FR-210 |
| l10n_sv_commerce.aml.program.checklist | component · present | checklist | manual · dd_procedures · codigo_etica · monitoreo · plan_auditoria_interna | FR-200 |
| res.partner | sv_cml_aml_risk_level | select | bajo · medio · alto (+ documented justification) | FR-202 |
| res.partner | sv_cml_aml_dd_level | computed/select | simplified · standard · enhanced (simplified barred under suspicion) | FR-202 |
| res.partner | sv_cml_aml_pep · sv_cml_aml_pep_kind · sv_cml_aml_pep_until | boolean · select · date | national · foreign; until = last-cese + 5 years; family/close-associate flag (enhanced DD, not PEP) | FR-205 |
| res.partner | sv_cml_aml_beneficiario_final_ids | many2many res.partner + chain data | natural persons; threshold = dated config (law 25%; 72_ 10% recorded, displaced); listed-company carve-out flag; own/third-account declaration | FR-203 |
| l10n_sv_commerce.aml.threshold | kind · comparator · value · currency · scope · provenance · effective window | dated config rows | cash_single >$10,000 · cash_monthly >$10,000 · other_single >$25,000 · other_monthly >$25,000 · wire_monthly ≥$1,000 · remesa_monthly ≥$200 · casino ≥$3,000 · metals_cash ≥$10,000 · lawyer_office >$10,000 · low_value_account >$1,000 · border ≥$15,000 · bf_participation ≥25% — every row carries delegation (71_ article) + instrument (71_/72_ article) + watch (OQ-001); NEVER hardcoded | FR-203, FR-206, FR-214, FR-216, FR-217, FR-221 |
| l10n_sv_commerce.aml.officer | role · appointer · appointed_on · uif_registered · resident · notice_due · accelerated_notice_due | record | oficial_titular · suplente · encargado · encargado_suplente; 15-días-hábiles notice; 5-días-hábiles for despido/traslado/renuncia/sanción; anti-retaliation invariant note | FR-207, FR-209, FR-210 |
| l10n_sv_commerce.aml.comite | members · top_governance_member · officer_member · group_entities_represented · single_acta_book | record | ≥3 members invariant; group single-Comité shape | FR-208 |

**Cases, reports and sanctions:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.aml.case | state · detected_on · analysis_due · extension_requested · determined_on · transmit_deadline · dismissed_rationale · tentativa | state machine | detected → analysis → suspicious (24h transmit) · dismissed (rationale mandatory); tentativa type; red-flag rule ref; confidential — no client-visible surface | FR-211, FR-212, FR-213 |
| l10n_sv_commerce.aml.regulated.report | period/event · component_totals · linked_flag · due_on | rows | single/monthly per client; mixed decomposition (total + cash/other-media split); digital-asset ops in scope; 5 días hábiles from day-after-operation/month-end (engine by id) | FR-214, FR-215 |
| l10n_sv_commerce.aml.aggregate.report | month · kind · rows · due_on | institution-tier | wires_intl ≥$1,000 · wires_local ≥$1,000 · remesas ≥$200 + R.16 data; first-5-hábiles after month | FR-216 |
| l10n_sv_commerce.aml.sanction.exposure | tier · duty_ref · smm_range · computed_amount · prescription | exposure rows | grave 50-500/≤200/≤100 · muy_grave 501-1000/201-400/101-200 SMM; amount = count × dated SMM (SV-PAY-FR-011/022 by id); 10y clock + concealment anchor + interruption events | FR-222, FR-223, FR-224 |
| l10n_sv_commerce.aml.watch | item · due_on · status | watch rows | pending reglamento/instructivo (OQ-001); inclusion/exclusion feed (OQ-004) | FR-194, FR-197 |

## 5. Odoo Mapping

Layer semantics for this wave: AML compliance is Odoo-native
configuration/case/clock bookkeeping — every FR maps `odoo`; none of
them touch DTE generation/transmission, so no `saas` rows are
introduced. The single architecture-adjacent surface is the UIF/goAML
transmission channel: FR-218 records it as an EXTERNAL-INTERFACE
ASSUMPTION (the Odoo side produces payloads, deadlines and
acknowledgment evidence; transmission itself is `n/a` to the shipped
product — connector-by-configuration, formats not in corpus). Model
names are stable across Odoo 17/18/19/20; no version-specific behavior
is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-193 | odoo | res.company | sv_cml_aml_regime | Dated regime rows (pre/post 2025-10-17); authority-chain attributes; dead-law values never resolvable |
| FR-194 | odoo | res.company | sv_cml_aml_adaptation_windows | Derived dated rows (2026-01-15/04-09/04-17/07-09/10-17); overdue flags feed the OQ-001 watch |
| FR-195 | odoo | res.company | sv_cml_aml_sujeto_obligado | 10-category catalog + OSFL flag; inactive default (ordinary company NOT per-se subject) |
| FR-196 | odoo | res.company | sv_cml_aml_activity_triggers | Activity-gated categories; manual assertion + reviewed evidence; never auto-inferred |
| FR-197 | odoo | l10n_sv_commerce.aml.soj.resolution | dated inclusion/exclusion rows | Empty feed (OQ-004); watch uif.gob.sv/CIPLAFT |
| FR-198 | odoo | res.company | sv_cml_aml_supervisor | Art. 12 routing incl. online-casino Lotería Nacional carve-out; Art. 13 informational |
| FR-199 | odoo | res.company | registration + update-clock fields | 15-días-hábiles update on SV-FREP-FR-203 by id |
| FR-200 | odoo | l10n_sv_commerce.aml.program.* | yearly + checklist records | Governance approval evidence; component checklist 72_ Art. 7 d) |
| FR-201 | odoo | l10n_sv_commerce.aml.program.year | audit_evaluation rows | Annual evaluation incl. regulated-report sending validation; pipeline duty points to FR-212 |
| FR-202 | odoo | res.partner | risk/dd-level fields | Ladder simplified/standard/enhanced; simplified barred under suspicion |
| FR-203 | odoo | res.partner | sv_cml_aml_beneficiario_final_ids + threshold config | Law 25% vs kept 72_ 10% (displaced); listed carve-out; verify-before-relate |
| FR-204 | odoo | res.partner | nominative invariants | KYC refusal blocks relation start; tentativa queue → FR-212 |
| FR-205 | odoo | res.partner | PEP fields + catalog config | Cese + 5y computed expiry; family/close-associate enhanced DD; UIF owns list |
| FR-206 | odoo | res.partner + l10n_sv_commerce.aml.threshold | low_value_account row + termination window | $1,000 dated config; UIF 10-días-hábiles no-termination window (engine by id); early termination = muy-grave exposure |
| FR-207 | odoo | l10n_sv_commerce.aml.officer | role/architecture | Oficialía-mandatory vs designable vs self-responsible populations; officer presents ROS |
| FR-208 | odoo | l10n_sv_commerce.aml.comite | composition invariant | ≥3 members incl. one top-governance + the officer; group single-Comité/single-acta |
| FR-209 | odoo | l10n_sv_commerce.aml.officer | notice clocks | 15 días hábiles designation/change; 5 días hábiles despido/traslado/renuncia/sanción; documentation set (72_ Art. 7 m); 17_ Art. 4 g) kin |
| FR-210 | odoo | l10n_sv_commerce.aml.officer | Encargado regime | Resident + UIF-registered + requirement tiers + anti-retaliation invariant + annual report rows |
| FR-211 | odoo | l10n_sv_commerce.aml.case (rule engine) | configurable red-flag rules | Seeded from 17_ Arts. 12-18; parameters resolve from dated thresholds; output = case creation, NEVER auto-report |
| FR-212 | odoo | l10n_sv_commerce.aml.case | state machine | detected → analysis → suspicious/dismissed(rationale); tentativa incl. KYC refusal; press-mention no trigger |
| FR-213 | odoo | l10n_sv_commerce.aml.case | clocks | 15 + one 15 extension (UIF prior request; second refused) + 24h transmit; amount-irrelevant; intelligence-only flags |
| FR-214 | odoo | l10n_sv_commerce.aml.regulated.report + threshold config | monitor + dated values | Authority chain on every row (71_ Art. 25 delegation + 72_ Art. 51 values + watch); mixed decomposition; linked flag; digital assets in scope; 5 días hábiles day-after anchors (SV-FREP-FR-203 by id) |
| FR-215 | odoo | l10n_sv_commerce.aml.regulated.report | window config | Calendar-month operative (72_ Art. 51); 17_ Art. 3 rolling-30-days variant recorded as detection config; colones/3-day values dead |
| FR-216 | odoo | l10n_sv_commerce.aml.aggregate.report | institution-tier rows | ≥$1,000/≥$1,000/≥$200 monthly, first-5-hábiles; R.16 data incl. below-threshold transfers |
| FR-217 | odoo | l10n_sv_commerce.aml.threshold | APNFD trigger rows | ≥$3,000 casino / ≥$10,000 metals-cash / >$10,000 lawyer-office + sociedad-services catalog |
| FR-218 | n/a (external-interface assumption) | — | payloads/deadlines only | UIF/goAML channel external; connector = configuration; formats not in corpus (17_ OQ-2 kin) — justification: no corpus spec exists to implement against |
| FR-219 | odoo | l10n_sv_commerce.aml.case + ACLs | confidentiality guard | Art. 28 law-level no-tip-off; reporting ≠ breach; secrecy lifted for FGR/UIF; muy-grave exposure |
| FR-220 | odoo | res.company | sv_cml_aml_retention_applicability | Feed-only FR: publishes the flag consumed by `02` SV-CML-FR-028 d1/d2 by id; periods/purge owned by 02 |
| FR-221 | odoo | l10n_sv_commerce.aml.threshold | border informational row | ≥$15,000 content note; no computation (DGA-side) |
| FR-222 | odoo | l10n_sv_commerce.aml.sanction.exposure | SMM value model | Ranges in SMM sector-comercio units; amount = count × dated SMM (SV-PAY-FR-011/022 by id; SOQ-18 naming kin); exposure only |
| FR-223 | odoo | l10n_sv_commerce.aml.sanction.exposure | catalogs + graduation | grave/muy-grave mapped to duty FRs; Art. 33/36-38 informational |
| FR-224 | odoo | l10n_sv_commerce.aml.sanction.exposure | prescription engine | 10y + concealment anchor + targeted interruption; general audits interrupt nothing |

Version-regime notes (D12): the governing version row is the D.L. 426
regime (effective 2025-10-17 — version + effective date recorded; the
dead 1998-law values are never current authority); the adaptation
windows carry their own derived dates (≈2026-01-15 Reglamento,
≈2026-04-09 UIF instructivos, ≈2026-04-17 supervisor diagnostics,
≈2026-07-09 technical norms, ≈2026-10-17 subject adaptation); every
operative threshold ($10,000/$25,000/$1,000/$200/$3,000/$15,000/25%)
is DATED CONFIG with the 71_-delegation + 72_-instrument + watch
provenance chain — on issuance of the new reglamento/instructivo the
rows re-anchor (OQ-001), with pre-cutover facts reading the historical
regime row (FR-193). The SMM feed re-seeds per SMM decree (payroll
sidecar owns the values). No other dated values live in this file.

## 6. Acceptance Criteria

- **AC-001:** Given a company whose recorded activities match NONE of
  the Art. 7 categories (an ordinary trading/manufacturing company), when
  the AML profile is evaluated, then the profile is INACTIVE — no DD,
  officer, reporting or sanctions duty activates and the retention-matrix
  AML rows d1/d2 do not apply (FR-195; SV-CML-FR-028 rule ii).
- **AC-002:** Given an active subject's client paying US$9,000 in cash
  in a single event and a further US$9,500 in cash to the same client
  within the same calendar month (each ≤ US$10,000, monthly total
  US$18,500), when the regulated-ops monitor runs, then a
  monthly-cumulative cash report row is produced (mixed totals recorded)
  due within 5 días hábiles counted from the day after month end, on the
  shared días-hábiles engine (FR-214, FR-215).
- **AC-003:** Given an unusual operation detected on day 1 with the
  analysis closed as suspicious on day 10 of the window, then the ROS
  transmit deadline is 24 hours after the analysis closes; given instead
  an extension requested once and granted, the window hardens — a second
  extension request is refused (FR-213).
- **AC-004:** Given a grave-infraction exposure of 100 SMM sanctioned
  while the comercio y servicios monthly SMM vintage US$408.80 is
  operative, when the exposure amount is computed, then it reads
  US$40,880.00 = 100 × the dated SMM row via the payroll feed (never a
  hardcoded constant), and a later sanction recomputes on the then
  current vintage (FR-222; SV-PAY-FR-011/022 by id).
- **AC-005:** Given a new AML reglamento issuing with different
  regulated-ops thresholds, when its dated row is loaded, then the
  operative values re-anchor from 72_ Art. 51 to the reglamento for
  facts from its effective date while pre-existing facts keep the
  72_-provenance row — no code change (FR-193, FR-214; OQ-001).
- **AC-006:** Given a natural-person client whose last PEP position
  ceased on 2026-02-01, when PEP status is evaluated on 2030-06-01,
  then the PEP flag is not expired (cese + 5 years = 2031-02-01 not yet
  reached — flag still live); on 2031-06-01 it is expired; the client's
  spouse receives enhanced DD without a PEP flag (FR-205).
- **AC-007:** Given a client legal person whose ownership chain shows a
  natural person indirectly holding 20% and another holding 30%, when
  the beneficiario final chain resolves, then only the 30% holder is
  flagged at the law's ≥25% threshold (kept-instructivo 10% recorded but
  displaced), and identity verification is required before the relation
  opens (FR-203).
- **AC-008:** Given a prospective client refusing to provide the
  required identification documentation, when the onboarding attempt is
  recorded, then the relation does not open and a tentativa case is
  queued for officer analysis — never silently dropped (FR-204,
  FR-212).
- **AC-009:** Given an Oficialía-mandatory subject whose Comité record
  has 3 members with none from the top governance organ, when
  composition is validated, then a violation surfaces; adding the
  top-governance member and the compliance officer satisfies the
  invariant (FR-207, FR-208).
- **AC-010:** Given a red-flag engine case created by a structuring rule
  (just-under-threshold cash pattern), when the case processes, then it
  enters the analysis pipeline with NO transmission occurring — only an
  officer's suspicious determination opens the 24h transmit clock
  (FR-211, FR-213).
- **AC-011:** Given a client-facing portal user, when access to AML
  case records is evaluated, then no case content, analysis, ROS object
  or UIF correspondence is visible (Art. 28 no-tip-off), while the ROS
  transmission itself is marked a non-breach of disclosure restrictions
  (FR-219).
- **AC-012:** Given a sujeto obligado's transaction completed in
  2026-03-31 and its client relation ending 2027-06-30, when retention
  is computed, then the transaction record keeps until 2041-03-31 and
  the client-ID file until 2042-06-30 — computed and enforced by
  `02`'s SV-CML-FR-028/029 machinery fed by this file's applicability
  flag (FR-220).
- **AC-013:** Given a subject deciding to terminate a US$600-fund
  account relation for unmanageable risk, when the termination workflow
  runs, then NO UIF closure notification is generated (funds ≤
  US$1,000); for a US$5,000-fund account the notification issues and the
  relation cannot terminate until 10 días hábiles lapse without UIF
  response (FR-206).
- **AC-014:** Given an officer designated on 2026-05-04, when the notice
  clock computes, then the UIF/supervisor notice is due by 15 días
  hábiles from designation; given her resignation effective 2026-09-01,
  then the accelerated notice is due by 5 días hábiles from that date,
  with the resignation copy attached (FR-209).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | New AML Reglamento + new UIF instructivo PENDING (71_/72_ OQ-1 chain, R28): Art. 61 keeps D.E. 2-2000 + Acuerdo 380 until they issue, and Art. 56's own deadlines (instructivos ≈Apr-2026; technical norms ≈Jul-2026; Reglamento ≈Jan-2026 per Art. 60) are already past with no issuance visible on uif.gob.sv as of 2026-08-18. Supervisor side corroborated: the CVPCPA's Res. 111-2026 (LB-031) expressly states NO methodology lineamientos issued as of 27-feb-2026 and launches the Art.-58 diagnostic collection, with the subjects' 12-month adaptation window (≈2026-10-17) standing. Watch uif.gob.sv/marco-legal/ + D.O. (feed stall at 10-ago-2026 gates any Mar-2026+ issue hunt) + cvpcpa wp-json at cadence; when issued, the threshold rows re-anchor (72_ Art. 51 → reglamento), the sujetos list, formats (goAML) and sanctions re-verify, and FR-194's overdue flags clear. | no | Takumi S5 (sources watch) | open |
| OQ-002 | Operative threshold chain post-replacement (working ruling, kin of R26 / 72_ OQ-2): law-text thresholds are GONE (71_ Art. 25 delegates to the future reglamento); the kept instructivo's $10k-cash/$25k-other-media (single + monthly, mixed-decomposition rules) + Art. 52's $1,000-wire/$200-remesa institutional aggregates remain the operative values under the Art. 61 transitory. Encoded as dated config with this provenance chain; supersession rides OQ-001. | no | Takumi S5 | resolved (working ruling) |
| OQ-003 | Dead-law citation mapping (71-73_ OQ-4 kin): 72_ and 17_ cite repealed-LCLDA article numbers (Art. 2 inc. 3°, Art. 9, Art. 10-B…); synthesis re-anchors every kept-instrument citation onto 71_'s structure. Two value-level divergences resolved as working rulings under the §2 authority order — (i) ROS transmit clock: 71_ Art. 24's 24h displaces 72_ Art. 43's 5 días hábiles; (ii) beneficiario-final participation: 71_ Art. 15's ≥25% displaces 72_ Arts. 12/20's 10% — both recorded as dated config with provenance; re-verify when the new instructivo issues (OQ-001). The 72_ rubro taxonomy ("Rubro 1 al 20", keyed to the dead Art. 2) maps onto 71_ Art. 7's 10 categories as registration-side config. | no | Takumi S5 | open |
| OQ-004 | Post-Oct-2025 UIF/CIPLAFT inclusion/exclusion resolutions extending or shrinking the sujetos list are not in the corpus (EVID-242 doubt); FR-197's feed ships empty and category applicability rests on the Art. 7 text alone. Watch UIF/CIPLAFT resolutions; acquire when visible. | no | Takumi S5 (sources watch) | open |
