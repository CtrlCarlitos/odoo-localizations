# SV — Chart of accounts — Framework & policies: PYME eligibility, complete FS set, policy governance, notes architecture

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the framework chassis every other file of this wave builds
on: PYME eligibility under the *Norma de Contabilidad NIIF para las PYMES*
(Accounting Standard for SMEs, 32_) — the two-prong test of no *obligación
pública de rendir cuentas* (public accountability) plus publication of
*estados financieros con propósito general* (general purpose financial
statements, GPFS), with the 1.5 compliance-declaration bar and the
separate-FS rule for full-NIIF groups; the per-company framework flag
(*marco contable*) as informational config; the complete-FS-set contract
(the five components, single vs two-statement vs the combined
retained-earnings variant, annual frequency with ≥1 comparative, going
concern with the ≥12-month lookahead, presentation uniformity with
comparative reclassification, identification disclosures, accrual basis);
the *costo o esfuerzo desproporcionado* (disproportionate cost or effort)
relief registry; the policy-governance spine of Sección 10 (hierarchy with
full NIIF as non-binding aid, change rules, the 10.10A prospective
revaluation switch, retroactive policy changes, prospective estimate
changes, prior-period error restatement) — the error-restatement FR being
EXPLICITLY DISTINCT from the e-invoicing fiscal-correction mechanics and
the Código de Comercio rectification duty, both consumed by id; and the
notes architecture of Sección 8 (declaration, material policies, judgments
vs estimation-uncertainty disclosures).

It does **not** cover: the ESF/P&L/CFS account architecture and (a)-(r)
report lines (`02_coa-structure.md`); financial instruments, fair value
and FX (`03_financial-instruments-fx.md`); non-financial assets
(`04_nonfinancial-assets.md`); liabilities, equity and employee benefits
(`05_liabilities-equity-benefits.md`); revenue (`06_revenue.md`);
consolidation, business combinations and related parties
(`07_groups-related-parties.md`); deferred tax, first-time adoption and
edition versioning (`08_deferred-tax-adoption.md`). Those files consume
this file's eligibility/config chassis and policy-event model by FR id.
Fiscal computations (ISR/IVA/payroll/special regimes) are owned by their
waves by FR id — this wave owns the ACCOUNTING book only; book-vs-fiscal
differences route through N8's deferred-tax FRs (32_ Sección 29) and are
never re-derived here.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling
R29): the operative framework LB = **32_** — *Norma de Contabilidad NIIF
para las PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official
Spanish translation, Sections 1-35 + Apéndice A (fecha de vigencia y
transición) + Apéndice B (glosario, integral part of the Norma); effective
2027-01-01 with early adoption permitted (A1; txt PAGE 315), cited by
section/párrafo as printed. **33_** (EY *Guía Práctica de NIIF y
Sostenibilidad 2024/2025*) is SECONDARY-ONLY authority per R29(a) and
EV33 OQ-1: it can NEVER be the sole LB of an FR; its LB role here is
limited to (a) version/horizon facts (the NIIF 19 reduced-disclosure
framework path effective 2027-01-01 that gives the framework flag its
third value) and (b) documented full-NIIF-vs-PYMES contrasts; where 33_
and 32_ could diverge, 32_ governs without exception.

**SOQ-46 instrument-gap note (rides every FR in this file and this
wave):** W18 identity verdict — the SV NIIF authority chain is OWNED:
78_ (Ley Reguladora de Contaduría, D.L. 828-2000/D.L. 646-2017) = the
Art. 36 authority; 77_ (Res. 462-2021) = the version-pinning adoption
(NIIF-PYMES español-2015 + full NIIF español-2020); 76_ (Res. 154-2024,
31-oct-2024) = the CURRENT NIIF-framework ratification incl. NIIF S1/S2,
deroga Res. 175-2023. The criteria instrument (WHO must apply
NIIF-PYMES vs full NIIF per CC Arts. 443-444, and any quantitative
thresholds) is STILL UNFOUND — candidates Res. 175-2023 (derogated
intermediate) / Res. 82-2024. SOQ-46 stays OPEN as an external watch
(hunt continues outside the corpus); this file's config-gap discipline
stands unchanged — NO invented SV thresholds or overrides, the
per-company framework flag informational (SOQ-53).

**R29(c)/SOQ-47 working reading (citation-rule basis):** CC Arts. 443-444
make balance formation subordinate first to the estimation criteria of
the *Consejo de Vigilancia de la Profesión de Contaduría Pública y
Auditoría* and only in default thereof to the "Normas Internacionales de
Contabilidad" (International Accounting Standards). Working assumption
(OQ-tracked, never asserted as settled): the CC's "NIC" fallback covers
the IASB's SME-level accounting standards — the NIIF para PYMES
(self-described "Norma de Contabilidad") as the NIC-default realization,
Consejo criteria first. The hook is consumed from
`commercial-legal/03_financial-statements.md` SV-CML-FR-040 by id; this
file never restates the CC hierarchy mechanics.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 1: "Las pequeñas y medianas entidades son entidades que: (a) no tienen obligación pública de rendir cuentas; y (b) publican estados financieros con propósito general para usuarios externos." "Una entidad tiene obligación pública de rendir cuentas cuando: (a) sus instrumentos de deuda o de patrimonio se negocian en un mercado público o están en proceso de emitir estos instrumentos para negociarse en un mercado público (ya sea una bolsa de valores nacional o extranjera, o un mercado fuera de la bolsa de valores, incluyendo mercados locales o regionales); o (b) posee activos en calidad de fiduciaria para un amplio grupo de terceros como uno de sus negocios principales…" Fiduciary carve-out: custody held "por motivos secundarios a la actividad principal (como podría ser el caso, por ejemplo, de las agencias de viajes o inmobiliarias, los colegios, las organizaciones no lucrativas, las cooperativas que requieran el pago de un depósito nominal para la afiliación y los vendedores que reciban el pago con anterioridad a la entrega de artículos o servicios…), esto no las convierte en entidades con obligación pública de rendir cuentas." 1.5: "Si una entidad que tiene obligación pública de rendir cuentas aplica usa [sic] esta Norma, sus estados financieros no se describirán como conformes a la Norma de Contabilidad NIIF para las PYMES —incluso si una ley o regulación en la jurisdicción de esa entidad permite o requiere que esta Norma sea utilizada…". 1.6: subsidiary of a full-NIIF controladora/group may use this Norma in its own FS "si dicha subsidiaria no tiene obligación pública de rendir cuentas por sí misma"; 1.7: "Una controladora… evaluará si cumple con los requisitos para aplicar esta Norma en sus estados financieros separados sobre la base de su propio estatus sin considerar si otras entidades del grupo tienen, o el grupo tiene como un todo, obligación pública de rendir cuentas." | SMEs are entities that: (a) do not have public accountability; and (b) publish general purpose financial statements for external users. Public accountability exists when: (a) debt or equity instruments are traded in a public market or are in process of issue for such trading (national or foreign exchange, or off-exchange including local or regional markets); or (b) the entity holds assets in a fiduciary capacity for a broad group of outsiders as one of its main businesses. Secondary-to-main-business custody (travel or real-estate agencies, schools, non-profits, nominal-deposit cooperatives, prepaid sellers) does NOT create public accountability. 1.5: FS of a publicly accountable entity that applies the Norma shall NOT be described as conforming to NIIF for SMEs — even if local law permits/requires it. 1.6: a subsidiary in a full-NIIF group may use the Norma in its own FS if not itself publicly accountable; 1.7: a controladora assesses eligibility for its separate FS on its OWN status regardless of whether other group entities or the group as a whole have public accountability. | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 1, párrs. 1.1-1.7 (txt PAGE 24-25) + Apéndice B obligación pública de rendir cuentas (txt PAGE 349-350) (EVID-275) |
| LB-002 | Norma NIIF para las PYMES, Prólogo P12: "Las decisiones sobre qué entidades están requeridas o autorizadas a utilizar las Normas NIIF de Contabilidad completas o la Norma de Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y regulatorias y en los emisores de normas de las distintas jurisdicciones." P13 (kin): jurisdictions setting applicability "suelen incluir criterios cuantificados basados en los ingresos…, activos, empleados". Apéndice A A1: "Una entidad aplicará esas modificaciones y revisiones a periodos anuales que comiencen a partir del 1 de enero de 2027. Se permite su aplicación anticipada" | Decisions on which entities are required or permitted to use full IFRS or the SME standard rest with each jurisdiction's legislative and regulatory authorities and standard-setters. Jurisdictional size criteria are usually quantified on revenue, assets, employees. Third edition applies to annual periods beginning 2027-01-01; early adoption permitted | `sv/sources/32_NIIF_PYMES_2025.pdf` | Prólogo P12/P13 (txt PAGE 22-23); Apéndice A A1 (txt PAGE 315) (EVID-275; 32_ identity block) |
| LB-003 | Norma NIIF para las PYMES, Sección 2: "Una entidad gastaría un costo o esfuerzo desproporcionado en aplicar un requisito si el costo incremental (por ejemplo, los honorarios de los tasadores) o el esfuerzo adicional (por ejemplo, los esfuerzos de los empleados) exceden sustancialmente los beneficios que los usuarios recibirían al tener la información. Esta Norma generalmente requiere que una PYME juzgue el costo o esfuerzo desproporcionado utilizando un umbral más bajo que el que otras Normas NIIF de Contabilidad requieren de las entidades con obligación pública de rendir cuentas…" "…la entidad hace un nuevo juicio de costo o esfuerzo desproporcionado en esa fecha posterior, basándose en la información disponible en esa fecha." "Si una entidad aplica una exención por esfuerzo o costo desproporcionado, la entidad revelará ese hecho y las razones por las cuales la aplicación del requerimiento implicaría un esfuerzo o costo desproporcionado. Este requerimiento no aplica a la exención… del párrafo 19.16, que está cubierto por… el párrafo 19.38." | An entity would incur disproportionate cost or effort if the incremental cost or additional effort substantially exceeds the benefit users would receive. The Norma generally requires an SME to judge disproportionate cost using a LOWER threshold than full-NIIF standards require of publicly accountable entities. The judgment is REMADE at each subsequent measurement date on then-available information. When the relief is used, the entity discloses that fact and the reasons (19.16 intangibles-in-combination relief excluded — its own 19.38 disclosures) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 2, párrs. 2.28-2.30 (txt PAGE 30-31) (EVID-276) |
| LB-004 | Norma NIIF para las PYMES, Sección 3: 3.3: "Una entidad cuyos estados financieros cumplan la Norma de Contabilidad NIIF para las PYMES efectuará en las notas una declaración, explícita y sin reservas de dicho cumplimiento. Los estados financieros no deberán señalar que cumplen la Norma… a menos que cumplan con todos los requerimientos de esta Norma." 3.7-3.8: going concern — "la gerencia tendrá en cuenta toda la información disponible sobre el futuro, que deberá cubrir al menos los doce meses siguientes a partir de la fecha de presentación, sin limitarse a dicho periodo"; 3.9 material-uncertainty and non-going-concern disclosures. 3.10: "presentará un juego completo de estados financieros (incluyendo información comparativa ―véase el párrafo 3.14) al menos anualmente" (shorter/longer period → disclose fact, reason, non-comparability). 3.11-3.13 uniformity of presentation/classification unless nature-change/Standard requires; "reclasificará los importes comparativos, a menos que resultase impracticable" + reclassification disclosures. 3.14 comparative information for ALL amounts. 3.17: FS "utilizando la base contable de acumulación (o devengo)" except cash-flow information. 3.17-3.18 complete set: (a) estado de situación financiera; (b) single estado del resultado integral OR separate estado de resultados + estado del resultado integral; (c) estado de cambios en el patrimonio; (d) estado de flujos de efectivo; (e) notas; 3.18 combined variant: "Si los únicos cambios en el patrimonio… surgen de ganancias o pérdidas, pago de dividendos, correcciones de errores de periodos anteriores, y cambios de políticas contables… un único estado de resultados y ganancias acumuladas" (véase 6.4); "un conjunto completo de estados financieros significa que la entidad presentará, como mínimo, dos de cada uno de los estados financieros requeridos y de las notas relacionadas". 3.23-3.24 identification: entity name, individual vs group, period end + length, "la moneda de presentación, tal como se define en la Sección 30", "el grado de redondeo"; notes: "el domicilio y forma legal de la entidad, el país en que se ha constituido y la dirección de su sede social… y una descripción de la naturaleza de las operaciones" | An entity whose FS comply with the SME standard makes an explicit and unreserved statement of compliance in the notes; FS must not be described as compliant unless they comply with ALL requirements. Going concern: all available future information covering AT LEAST the twelve months from the presentation date, without limitation; disclose material uncertainties, or the non-going-concern basis and reasons. A complete set of FS (with comparatives) at least annually; shorter/longer period change disclosed with non-comparability note. Uniformity of presentation period-to-period; reclassify comparatives unless impracticable, with disclosures. Comparative information for the prior period for all amounts. Accrual basis except cash-flow information. Complete set: statement of financial position; single statement of comprehensive income OR separate income statement + comprehensive-income statement; statement of changes in equity; statement of cash flows; notes; combined income-and-retained-earnings statement allowed when the ONLY equity changes are results, dividends, prior-period error corrections and policy changes (see 6.4); a complete set means AT LEAST TWO of each required statement and related notes. Identification: entity name, individual vs group, period end and length, presentation currency (Sección 30 definition), rounding degree; notes: domicile and legal form, country of incorporation, registered office, nature of operations | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 3, párrs. 3.3, 3.7-3.24 (+6.4 pointer) (txt PAGE 48-53) (EVID-277) |
| LB-005 | Norma NIIF para las PYMES, Sección 8: 8.1-8.4 notes order: "(a) una declaración de que los estados financieros se han elaborado cumpliendo con la Norma de Contabilidad NIIF para las PYMES (véase el párrafo 3.3); (b) información sobre las políticas contables materiales o con importancia relativa (véase el párrafo 8.5); (c) información de apoyo para partidas presentadas en los estados financieros, en la secuencia en que se presenta cada estado y cada partida; y (d) cualquier otra información a revelar." 8.5: "Una entidad revelará información material o con importancia relativa de política contable. La información sobre políticas contables es material… si… puede razonablemente esperarse que influya en las decisiones que toman los usuarios principales…". 8.6: "los juicios, diferentes de los que implican estimaciones (véase el párrafo 8.7), que la dirección haya realizado en el proceso de aplicación de las políticas contables… y que tengan un efecto muy significativo sobre los importes reconocidos" — examples: FV classes per 12.30, control of another entity, control conjunto/influencia significativa. 8.7: "información sobre los supuestos clave acerca del futuro y otras causas clave de incertidumbre en la estimación en la fecha de presentación, que tengan un riesgo significativo de ocasionar ajustes materiales… dentro del ejercicio contable siguiente. Con respecto a esos activos y pasivos, las notas incluirán detalles de: (a) su naturaleza; y (b) su importe en libros" | Notes order: (a) NIIF-PYMES compliance declaration (3.3); (b) material accounting policies (8.5); (c) supporting information in the sequence each statement and line item is presented; (d) any other disclosures. Policy information is material if it could reasonably be expected to influence primary users' decisions. Judgments — OTHER than estimation judgments — made in applying policies with a very significant effect on recognized amounts are disclosed (examples: fair-value asset/liability classes per 12.30, control conclusions, joint control or significant influence). Key future assumptions and other key estimation-uncertainty sources at the presentation date carrying significant risk of material adjustment WITHIN THE NEXT ACCOUNTING PERIOD are disclosed with, per affected asset/liability: (a) nature; (b) carrying amount | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 8, párrs. 8.1-8.7 (txt PAGE 73-74) (EVID-281) |
| LB-006 | Norma NIIF para las PYMES, Sección 10: 10.4 (Norma silent → management develops a policy giving "(a) relevante… y (b) fiable" information — faithful representation, substance-over-form, neutrality, prudence, completeness). 10.5 hierarchy "(a) requerimientos y guías establecidos en esta Norma que traten cuestiones similares y relacionadas; y (b) las definiciones, criterios de reconocimiento y conceptos de medición… de la Sección 2". 10.6: "la gerencia puede también considerar los requerimientos y guías en las Normas NIIF de Contabilidad completas que traten cuestiones similares y relacionadas." 10.7 uniformity "de manera uniforme para transacciones… similares". 10.8 change only if "(a) es requerido por cambios a esta Norma; o (b) da lugar a que los estados financieros suministren información fiable y más relevante". 10.9 not-changes list; 10.10 election change IS a policy change. 10.10A: "un cambio del modelo del costo al modelo de revaluación para una clase de propiedades, planta y equipo se contabilizará de forma prospectiva, en lugar de hacerlo de acuerdo con los párrafos 10.11 y 10.12." 10.11-10.12: standard-driven changes per Apéndice A transitionals; "todos los demás cambios… de forma retroactiva" — new policy applied to comparatives "como si… se hubiese aplicado siempre", else earliest-practicable opening balances + equity adjustment. 10.13-10.14 disclosures (nature, per-period adjustments, impracticability). 10.14A-10.16 estimates: measurement uncertainty; revision on new information; input/technique change = estimate change "a menos que procedan de la corrección de errores"; criteria change = policy change; "Cuando sea difícil distinguir… el cambio se tratará como si fuera un cambio en una estimación"; effect "de forma prospectiva, incluyéndolo en el resultado del periodo"; disclosures. 10.18-10.23 prior-period errors: omissions/inaccuracies from not using reliable information "(a) estaba disponible cuando se autorizó la emisión de los estados financieros…; y (b) podría esperarse razonablemente que se hubiera conseguido" — including "errores aritméticos, errores en la aplicación de políticas contables, la inadvertencia o mala interpretación de hechos, así como los fraudes"; "corregirá de forma retroactiva los errores significativos… reexpresando la información comparativa… o… reexpresando los saldos iniciales"; disclosures per 10.23 | When the Norma is silent, management develops a policy giving relevant and reliable information, referring in descending order to (a) analogous requirements and guidance IN THIS Norma and (b) Section 2 definitions, recognition criteria and measurement concepts; management MAY ALSO consider full-NIIF requirements and guidance (non-binding aid, never overriding this Norma). Policies applied uniformly to similar transactions. A policy changes ONLY if Standard-required or more reliable-and-relevant; applying a policy to substantially different/new/insignificant transactions is not a change; an FV-to-cost fallback when fair value ceases reliably measurable is not a change; changing an allowed ELECTION is a policy change. First-time PPE revaluation (cost→revaluation model, per class) is accounted for PROSPECTIVELY as a revaluation under Sección 17 — never retrospectively under 10.11-10.12. Other changes apply retrospectively to comparatives as if always applied, or to earliest-practicable opening balances, with nature/adjustment disclosures. Estimates: revised on new information; input/technique changes are estimate changes (unless error corrections); measurement-criteria changes are policy changes; hard-to-distinguish cases are treated as estimate changes; estimate changes apply prospectively through profit or loss; disclosed. Prior-period errors (information available at authorization, fraud included) are corrected retrospectively by restating comparatives or re-expressing opening balances, with nature/correction disclosures | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 10, párrs. 10.1-10.23 (txt PAGE 85-90) (EVID-283) |
| LB-007 | Guía EY (SECONDARY-ONLY per R29(a); never sole LB): NIIF 19 *Subsidiaries without Public Accountability* — "permite a las entidades elegibles optar por aplicar los requisitos de información a revelar reducidos de la NIIF 19 sin dejar de aplicar los requisitos de reconocimiento, medición y presentación de otras normas contables NIIF"; eligibility = subsidiary + no public accountability + IFRS-compliant consolidated parent; "el mismo lenguaje que la norma contable NIIF para PYMES"; effective 2027-01-01, early adoption permitted. Framework-contrast set (EVID-299): full NIIF vs PYMES divergences (NCI measurement choice, goodwill non-amortization, ECL, IFRS-16 right-of-use, R&D capitalization, borrowing-cost capitalization) documented as boundary notes for full-NIIF group entities — never dual implementations | (Secondary authority, R29(a)): NIIF 19 lets eligible subsidiaries apply reduced disclosures on full-NIIF recognition/measurement/presentation from 2027-01-01 — the third SV framework-path value behind the informational marco-contable flag; the guide's full-NIIF-vs-PYMES contrast set documents which entities fall outside the PYMES engine | `sv/sources/33_Guia_NIIF_Sostenibilidad_2024-2025.pdf` | NIIF 19 chapter (txt PAGE 170-175) + guide identity (txt PAGE 12-13) (EVID-299/301; EV33 OQ-1/OQ-3) |

## 3. Functional Requirements

### 3.1 PYME eligibility and framework flag (Sección 1 + Apéndice B + Prólogo P12)

- **SV-COA-FR-001:** The system shall carry a per-company framework flag
  (*marco contable*) — niif_pymes · niif_plenas ·
  niif_plenas+NIIF19-2027 — as INFORMATIONAL configuration driving which
  engine the company's books target, never as a compliance gate (SOQ-53);
  the flag carries no shipped SV legal default because the SV adopting
  instrument is absent from the corpus (SOQ-46) and the Norma itself
  leaves applicability to each jurisdiction (Prólogo P12) — the system
  shall NOT ship any quantitative SV size/eligibility threshold (no
  revenue/asset/employee criteria invented; Prólogo P13 notes
  jurisdictions "suelen incluir criterios cuantificados", none of which
  exist for SV in the corpus).
  (LB-001; LB-002; LB-007 secondary; EVID-275/299/301)
- **SV-COA-FR-002:** The system shall implement the two-prong PYME
  definition as a per-company eligibility determination record: (a) the
  entity does NOT have *obligación pública de rendir cuentas* (public
  accountability); AND (b) it publishes *estados financieros con propósito
  general* (general purpose financial statements) for external users —
  both prongs required, each carrying its evidence basis and determination
  date (D15: the determination snapshots as-of its assessment date on the
  record; re-assessment on the entity's own events, never a periodic
  recompute).
  (LB-001; EVID-275)
- **SV-COA-FR-003:** The system shall implement the public-accountability
  determination with its two alternative triggers and the secondary-custody
  carve-out: trigger (a) debt or equity instruments traded in a public
  market OR in process of issue for public trading — any market,
  exchange-listed or off-exchange including local or regional markets;
  trigger (b) assets held in a fiduciary capacity for a broad group of
  third parties as ONE OF ITS MAIN BUSINESSES (banks, credit cooperatives,
  insurance companies, brokers, securities intermediaries, pension funds,
  collective investment funds, investment banks typically meet it) —
  custody held for motives SECONDARY to the main business (travel or
  real-estate agencies holding client funds, schools, non-profits,
  cooperatives charging only a nominal affiliation deposit, sellers
  receiving advance payment for goods or services such as utilities) does
  NOT constitute public accountability and shall not flip the
  determination.
  (LB-001; EVID-275)
- **SV-COA-FR-004:** The system shall enforce the 1.5 compliance bar: when
  the public-accountability determination is positive, the FS-set
  generator shall NEVER emit or flag the statement that the FS conform to
  the *Norma de Contabilidad NIIF para las PYMES* — even where a
  jurisdiction's law permits or requires such entities to use the Norma —
  and the explicit-and-unreserved declaration slot of FR-019 stays empty
  (the 3.3 declaration "no deberán señalar que cumplen… a menos que cumplan
  con todos los requerimientos" is only emittable for fully-compliant,
  non-publicly-accountable filers).
  (LB-001; LB-004; EVID-275/277)
- **SV-COA-FR-005:** The system shall implement the separate-FS rule for
  full-NIIF groups: a subsidiary whose controladora (or group) applies
  full NIIF may run its OWN financial statements under this Norma when the
  subsidiary itself is not publicly accountable (1.6, with full compliance
  required once described as conforming); and a controladora — including
  the ultimate or any intermediate one — assesses eligibility for its
  *estados financieros separados* (separate financial statements) on its
  OWN status, disregarding whether other group entities or the group as a
  whole have public accountability, and may present separate FS under this
  Norma even when it presents consolidated FS under full NIIF or another
  GAAP set (1.7), the PYMES-prepared FS being clearly distinguished from
  the other-GAAP FS — consolidation duties, the 9.26 separate-FS policy
  menu and combined FS are owned by `07_groups-related-parties.md` by id,
  never restated here.
  (LB-001; EVID-275)

### 3.2 Complete FS set and report architecture (Sección 3)

- **SV-COA-FR-006:** The system shall model the complete FS set with its
  five components: (a) *estado de situación financiera* (statement of
  financial position) as of the reporting date; (b) EITHER a single
  *estado del resultado integral* (statement of comprehensive income)
  showing ALL income and expense items — result-period items plus *otro
  resultado integral* (other comprehensive income) — OR a separate
  *estado de resultados* (income statement) plus a separate comprehensive
  income statement that begins with the result; (c) *estado de cambios en
  el patrimonio* (statement of changes in equity); (d) *estado de flujos
  de efectivo* (statement of cash flows); (e) notes — plus the
  presentation-set variants: the combined *estado de resultados y
  ganancias acumuladas* (income and retained earnings statement)
  replacing (b)+(c) when the ONLY equity changes arise from profits or
  losses, dividend payments, prior-period error corrections and policy
  changes (3.18, mechanics per 6.4 — owned with the equity reconciliation
  by `02_coa-structure.md` by id); and the no-OCI simplification (single
  statement whose last line is named "resultado del periodo" when no OCI
  items exist in ANY period presented) — and shall present, as part of any
  complete set, at minimum TWO of each required statement and its related
  notes (comparatives make the set double).
  (LB-004; EVID-277)
- **SV-COA-FR-007:** The system shall require annual reporting with at
  least one comparative period: a complete FS set including comparative
  information at least annually; comparative information for the prior
  period for ALL amounts presented (and for narrative/descriptive
  information when relevant to understanding the current-period FS); when
  the period end changes and FS are presented for a period longer or
  shorter than one year, the generator discloses that fact, the reason,
  and that comparative amounts (including related notes) are not fully
  comparable.
  (LB-004; EVID-277)
- **SV-COA-FR-008:** The system shall implement the *negocio en marcha*
  (going concern) assessment discipline: management evaluates the entity's
  ability to continue in operation when preparing the FS (an entity is a
  going concern unless management intends to liquidate or cease trading,
  or has no realistic alternative), taking into account ALL available
  information about the future covering AT LEAST the twelve months from
  the presentation date WITHOUT being limited to that period; when the
  assessment is aware of MATERIAL uncertainties from events or conditions
  casting significant doubt on the ability to continue, those
  uncertainties are disclosed; when FS are NOT prepared on a going-concern
  basis, that fact is disclosed together with the assumptions used and the
  reasons the entity is not a going concern.
  (LB-004; EVID-277)
- **SV-COA-FR-009:** The system shall implement presentation uniformity
  with comparative reclassification: presentation and classification of
  items are maintained from one period to the next unless a significant
  change in the nature of operations or a FS review shows another
  presentation is more appropriate (per the Sección 10 policy criteria) or
  the Norma itself requires a change; on any presentation/classification
  change the comparative amounts are RECLASSIFIED unless impracticable,
  disclosing the nature of the reclassification, the amount of each item
  or group of items reclassified and the motive; when reclassification is
  impracticable, the system discloses why.
  (LB-004; EVID-277)
- **SV-COA-FR-010:** The system shall emit the identification disclosures
  on every FS set, prominently and repeated as needed: entity name and any
  change in denomination since the prior period end; whether the FS belong
  to the individual entity or to a GROUP of entities; the closing date of
  the reporting period and the period covered; the *moneda de
  presentación* (presentation currency) as defined in Sección 30; and the
  degree of *redondeo* (rounding), if any, practiced in presenting
  amounts — and in the notes: the entity's domicile and legal form, its
  country of incorporation and the address of its registered office (or
  principal place of business if different), and a description of the
  nature of its operations and principal activities.
  (LB-004; EVID-277)
- **SV-COA-FR-011:** The system shall prepare the FS on the *base
  contable de acumulación (devengo)* (accrual basis of accounting) —
  items are recognized as assets, liabilities, equity, income or expenses
  when they satisfy the definitions and recognition criteria of the Norma
  — EXCEPT cash-flow information, which follows Sección 7 (owned by
  `02_coa-structure.md` by id).
  (LB-004; EVID-276/277)

### 3.3 Disproportionate-cost relief registry (Sección 2)

- **SV-COA-FR-012:** The system shall keep a disproportionate-cost relief
  registry: one row per application of the *costo o esfuerzo
  desproporcionado* (disproportionate cost or effort) exemption, recording
  the requirement relieved, the item/measurement/disclosure concerned, the
  judgment basis and the date — implementing the PYME rule that the
  threshold is judged at a LOWER level than full NIIF requires of publicly
  accountable entities (incremental costs such as appraiser fees, or
  additional effort such as employee effort, substantially exceeding the
  user benefit justify relief), with the judgment REMADE at each
  subsequent measurement date on then-available information (a new dated
  registry row, never a standing exemption); every use surfaces the
  disclosure "ese hecho y las razones" (that fact and the reasons) through
  the notes builder — the registry is the feed every later file's
  disproportionate-cost relief cites (investment-property FV measurability
  and FV-of-equities fallbacks among others, consumed by id), with the
  19.16 business-combination intangibles relief EXCLUDED (its disclosures
  live in 19.38, owned by `07_groups-related-parties.md` by id).
  (LB-003; EVID-276)

### 3.4 Policy governance (Sección 10)

- **SV-COA-FR-013:** The system shall implement the policy-selection
  hierarchy: where the Norma specifically deals with a transaction, event
  or condition, its requirement applies (immaterial-effect caveat
  aside); where the Norma is SILENT, management develops a policy giving
  information that is (a) relevant and (b) reliable (faithful
  representation of position, performance and cash flows; substance over
  legal form; neutrality; prudence; completeness in all significant
  respects), referring — in descending order — to (a) requirements and
  guidance in THIS Norma dealing with similar and related questions, and
  (b) the Sección 2 definitions, recognition criteria and measurement
  concepts; the requirements and guidance of FULL NIIF (10.6) may ALSO be
  considered as a NON-BINDING aid only — recorded as a supporting
  reference on the policy record, never as an overriding source (where
  full NIIF and this Norma could diverge, this Norma governs; R29(a)).
  (LB-006; EVID-283)
- **SV-COA-FR-014:** The system shall implement the policy-change rules:
  policies are selected and applied UNIFORMLY to similar transactions,
  events and conditions unless the Norma requires or allows item
  categories (then one adequate policy per category, uniform within it);
  a policy change is permitted ONLY when (a) required by a change in this
  Norma (applied per the Apéndice A transitional provisions) or (b) the
  change makes the FS provide reliable and MORE relevant information; the
  system shall classify as NOT policy changes: applying a policy to
  transactions substantially different from previous ones, applying a NEW
  policy to transactions that did not occur previously or were
  insignificant, and a cost-model fallback when a reliable fair-value
  measure ceases to be available (or vice versa) for an asset the Norma
  would otherwise measure at fair value; changing an ELECTION the Norma
  permits (including a measurement basis election) IS a policy change.
  (LB-006; EVID-283)
- **SV-COA-FR-015:** The system shall implement the 10.10A revaluation
  switch as PROSPECTIVE: the first-time application of a revaluation
  policy for *propiedades, planta y equipo* (property, plant and
  equipment) is a policy change treated as a REVALUATION under Sección 17
  — a change from the cost model to the revaluation model for a PPE class
  posts prospectively (revalued amounts become the new basis going
  forward), NEVER as a retrospective 10.11-10.12 restatement with
  comparative rewriting; the revaluation mechanics (class-wide scope,
  *superávit de revaluación* OCI routing) are owned by
  `04_nonfinancial-assets.md` by id.
  (LB-006; EVID-283)
- **SV-COA-FR-016:** The system shall implement retroactive application
  for policy changes other than the 10.10A switch and
  standard-transition cases: standard-driven changes follow the Apéndice
  A transitional provisions; ALL other policy changes apply
  RETROSPECTIVELY — the new policy is applied to prior-period comparative
  information from the earliest practicable date as if it had always
  applied, or, where period-specific effects are impracticable to
  determine, to the carrying amounts of assets and liabilities at the
  beginning of the earliest period for which retrospective application is
  practicable (which may be the current period) with the corresponding
  adjustment to opening balances of each affected equity component — and
  the generator discloses the nature of the change and, per affected FS
  line, the adjustment amounts for the current and each prior period
  presented (and aggregate pre-presented periods), or why determination is
  impracticable; no repetition in later periods' FS.
  (LB-006; EVID-283)
- **SV-COA-FR-017:** The system shall implement accounting-estimate
  changes as PROSPECTIVE: an *estimación contable* (accounting estimate)
  develops when a policy requires measurement involving measurement
  uncertainty (estimation and valuation techniques with inputs, judgment
  based on the latest reliable information); estimates are revised for
  changes in circumstances, new information, developments or added
  experience; a change in an INPUT or measurement TECHNIQUE is an
  estimate change UNLESS it stems from a prior-period error correction;
  and a change in measurement CRITERIA applied is a policy change — where
  hard to distinguish, the change is treated as an ESTIMATE change; the
  effect is recognized prospectively in profit or loss of the period of
  change (or that period and future periods if both affected), or by
  adjusting the carrying amount of the corresponding asset, liability or
  equity item in the period of change (per 10.17) — comparatives are NEVER
  rewritten; the nature of the change and its effect on assets,
  liabilities, income and expenses for the current period (and estimable
  future periods) are disclosed.
  (LB-006; EVID-283)
- **SV-COA-FR-018:** The system shall implement prior-period error
  correction — the ACCOUNTING-book restatement track: *errores de
  periodos anteriores* (prior-period errors) are omissions and
  inaccuracies arising from failure to use, or misuse of, reliable
  information that (a) was available when the FS for those periods were
  AUTHORIZED for issue and (b) could reasonably have been obtained and
  taken into account — including arithmetic errors, misapplication of
  accounting policies, oversight or misinterpretation of facts, and
  FRAUD; significant errors are corrected RETROACTIVELY in the first
  authorized FS after discovery by restating the comparative information
  for the prior period(s) in which the error arose, or — when the error
  predates the earliest presented period — by re-expressing the opening
  balances of assets, liabilities and equity for that earliest period
  (impracticability falls back to the earliest practicable period), with
  the 10.23 disclosures (nature; correction amount per affected line for
  each prior period presented; opening-balance correction; impracticability
  explanation); corrections post through *ganancias acumuladas* (retained
  earnings)/affected equity components, never through current-period
  income. **Two-track invariant (binding):** this restatement track is
  DISTINCT from, and never merged with, the FISCAL correction tracks —
  (i) e-invoicing DTE fiscal immutability and correction accounting
  (D9; invalidation full-mirror reversals in the event's period, NCE/NDE
  window adjustments, retorno credit entries, origin-rate USD derivation)
  is owned by `e-invoicing/02_transmission.md` §3.11, SV-EINV-FR-159..164,
  consumed BY ID here — those mechanics post NEW-period fiscal entries
  and never rewrite a filed period's fiscal documents; (ii) the Código de
  Comercio Art. 439 *asiento de rectificación* (immediate same-register
  rectification under the no-alteration regime) is owned by
  `commercial-legal/02_accounting-books.md` SV-CML-FR-024 (extension
  FR-025), consumed BY ID — their mechanics are never restated in this
  wave; where one underlying operation triggers BOTH an accounting error
  restatement AND a fiscal correction, the policy-event record links the
  two tracks by id without routing one through the other's documents, and
  book-vs-fiscal differences route through N8's deferred-tax FRs
  (`08_deferred-tax-adoption.md` by id).
  (LB-006; EVID-283)

### 3.5 Notes architecture (Sección 8)

- **SV-COA-FR-019:** The system shall build the notes in the statutory
  order: (a) the compliance declaration — an explicit and unreserved
  statement that the FS comply with the *Norma de Contabilidad NIIF para
  las PYMES* (3.3; emittable only when FR-004's bar is not engaged and ALL
  requirements are met); (b) the material accounting-policy information
  (FR-020); (c) supporting information for items presented in the FS, in
  the sequence each statement and each line item is presented; (d) any
  other disclosures — each note clearly identified and distinguished from
  other information in the same document.
  (LB-005; LB-004; EVID-281/277)
- **SV-COA-FR-020:** The system shall disclose MATERIAL accounting-policy
  information: policy information is material (3rd-ed. wording
  "material o con importancia relativa") when, considered together with
  the other information in the FS, it can reasonably be expected to
  influence the decisions primary GPFS users make on the basis of those
  FS — the materiality call recorded per policy on the policy record, so
  the notes builder emits exactly the material set.
  (LB-005; EVID-281)
- **SV-COA-FR-021:** The system shall implement the judgments vs
  estimation-uncertainty disclosure split as two DISTINCT note feeds:
  JUDGMENTS (8.6) — judgments, OTHER than those involving estimates, that
  management made in applying the entity's accounting policies and that
  have a VERY SIGNIFICANT effect on the amounts recognized in the FS
  (worked examples from the Norma: the appropriate classes of assets and
  liabilities for fair-value disclosure under 12.30; whether the entity
  controls another entity; whether it has joint control of an arrangement
  or significant influence over another entity); ESTIMATION UNCERTAINTY
  (8.7) — information on key assumptions about the future and other key
  sources of estimation uncertainty AT THE PRESENTATION DATE that have a
  significant risk of resulting in a material adjustment to the carrying
  amounts of assets and liabilities WITHIN THE NEXT *ejercicio*
  (accounting period), disclosing for each such asset and liability its
  NATURE and its CARRYING AMOUNT at the period end — the judgment feed
  never absorbs the estimation feed and vice versa (an item may feed both
  only through its two distinct aspects).
  (LB-005; EVID-281)

## 4. Data Model

Layer semantics: the framework chassis is Odoo-native (res.company
config + dated config rows + posting-policy records on account.move
surfaces) — all entities live in the client (wave default `odoo`; see
§5). The IASB/Consejo are external authorities: the model records the
company's OWN determinations (eligibility, policies, events), it does not
emulate any regulator. No printed data table in this file warrants a CSV
sidecar (the eligibility triggers and policy-event kinds are small config
sets; default none per plan).

**Framework/eligibility profile (on res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_framework_flag | select | niif_pymes · niif_plenas · niif_plenas_niif19_2027 | FR-001 |
| res.company | sv_coa_flag_basis | char/config | provenance note — SV instrument absent (SOQ-46); informational only (SOQ-53); Consejo criteria → SV-CML-FR-040 by id | FR-001 |
| res.company | sv_coa_pyme_eligible | boolean + date + basis | two-prong determination snapshot (FR-002/003); D15 snapshot-on-write, re-assessed on entity events only | FR-002, FR-003 |
| res.company | sv_coa_public_accountability | select + evidence | none · traded_or_in_issue (market scope recorded) · fiduciary_main_business (secondary-custody carve-out flag: custody_secondary_to_main) | FR-003 |
| res.company | sv_coa_gpfs_published | boolean | GPFS publication prong | FR-002 |
| res.company | sv_coa_separate_fs_rule | select | own_status (1.6/1.7 kin: subsidiary-in-full-NIIF-group / controladora own-status) — informational; consolidation surfaces owned by 07 by id | FR-005 |

**FS-set config (res.company / reporting period):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_fs_set_variant | select | single_eri · two_statement · combined_retained_earnings · no_oci_single | FR-006 |
| res.company | sv_coa_comparative_periods | int | ≥1 (3.14); annual frequency 3.10 | FR-007 |
| res.company | sv_coa_going_concern_state | select + date | assumed · material_uncertainty_disclosed · not_going_concern (assumptions + reasons captured) | FR-008 |
| res.company | sv_coa_presentation_currency | m2o res.currency | *moneda de presentación* (Sec 30 definition; 03 file owns translation mechanics by id) | FR-010 |
| res.company | sv_coa_rounding | selection/monetary | rounding degree disclosed (units/thousands) | FR-010 |
| l10n_sv_chart.reclassification (close surface) | item/group · amount · motive · impracticable | char · monetary · char · boolean | comparative reclassification rows (3.12-3.13), linked to the affected moves/report lines | FR-009 |

**Disproportionate-cost registry (l10n_sv_chart.disproportionate_cost_use):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.disproportionate_cost_use | requirement_ref · item_ref | char/m2o | the Norma requirement relieved + the item/measurement/disclosure | FR-012 |
| l10n_sv_chart.disproportionate_cost_use | judgment_date · basis | date · text | incremental-cost/effort vs user-benefit basis; re-judged per subsequent measurement date (new row, never standing) | FR-012 |
| l10n_sv_chart.disproportionate_cost_use | disclosed_in | m2o | notes-builder emission (fact + reasons) | FR-012 |

**Policy records + events (l10n_sv_chart.policy / l10n_sv_chart.policy_event):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.policy | topic · source_refs | char | per developed policy when the Norma is silent: hierarchy refs (this-Norma analogues; Sec 2 concepts) + full-NIIF aid refs marked non-binding (10.6) | FR-013 |
| l10n_sv_chart.policy | uniform_category | char | category-scoped uniformity (10.7) | FR-014 |
| l10n_sv_chart.policy_event | kind | select | standard_change_appendix_a · voluntary_change_retroactive · estimate_change_prospective · error_correction_restatement · revaluation_switch_prospective · not_a_change (substantially-different / new-insignificant / fv-cost-fallback) · election_change | FR-014..018 |
| l10n_sv_chart.policy_event | application | select | retroactive_comparatives · retroactive_earliest_practicable_opening · prospective_pl · prospective_carrying · prospective_revaluation | FR-015..017 |
| l10n_sv_chart.policy_event | restatement_entries | one2many account.move | comparative restatement / opening-balance re-expression entries through ganancias acumuladas (accounting-book track ONLY) | FR-016, FR-018 |
| l10n_sv_chart.policy_event | linked_fiscal_track | m2o/m2m by id | optional pointer to e-invoicing correction surfaces (SV-EINV-FR-159..164 kin) / CC 439 rectification (SV-CML-FR-024 kin) when the same operation has a fiscal track — linked, never merged | FR-018 |
| l10n_sv_chart.policy_event | disclosure_state | select | per 10.13/10.14/10.18/10.23/8.x — emitted once, not repeated in later FS | FR-016..019 |

**Notes slots (l10n_sv_chart.note_slot):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.note_slot | kind | select | declaration_3_3 · material_policy_8_5 · judgment_8_6 · estimation_uncertainty_8_7 · supporting_in_order · other | FR-019..021 |
| l10n_sv_chart.note_slot | seq | int | statutory order (a)-(d); supporting slots follow statement/line order | FR-019 |
| l10n_sv_chart.note_slot | judgment_source | m2o/config | 8.6 examples: fv_classes_12_30 · control_conclusion · control_conjunto_influencia | FR-021 |
| l10n_sv_chart.note_slot | estimation_items | one2many | 8.7 rows: asset/liability + nature + carrying amount at period end | FR-021 |

## 5. Odoo Mapping

Layer semantics for this wave: the chart-of-accounts framework is
Odoo-native (res.company config, account.account/account.move engines,
dated config rows) — every FR maps `odoo`; no SaaS rows are introduced
because none of these FRs touch DTE generation/transmission (an
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are
stable across Odoo 17/18/19/20; the notes/FS-set generator builds on
Odoo's report layouts, no version-specific behavior required by this
file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | res.company | sv_coa_framework_flag (+basis) | informational (SOQ-53); SOQ-46 config-gap — no SV thresholds shipped; NIIF19 value provenance = 33_ secondary (LB-007, never sole) |
| FR-002 | odoo | res.company | sv_coa_pyme_eligible (+date/basis) | D15 snapshot-on-write; both prongs with evidence |
| FR-003 | odoo | res.company | sv_coa_public_accountability, sv_coa_gpfs_published | traded/in-issue scope + fiduciary-main trigger; secondary-custody carve-out flag |
| FR-004 | odoo | report layer (l10n_sv_chart) | declaration gate | 1.5 bar auto-block; 3.3 declaration emittable only for compliant non-PACC filers |
| FR-005 | odoo | res.company | sv_coa_separate_fs_rule | 1.6/1.7 own-status rule; consolidation menu = 07 by id |
| FR-006 | odoo | res.company + report layouts | sv_coa_fs_set_variant | five components; combined variant gated on the only-changes test (3.18/6.4); ≥2 of each statement |
| FR-007 | odoo | res.company + fiscal periods | sv_coa_comparative_periods | ≥1 comparative; period-length-change disclosures (3.10/3.14) |
| FR-008 | odoo | res.company + period close | sv_coa_going_concern_state | ≥12-month lookahead not limited to it; uncertainty/non-GC disclosures (3.7-3.9) |
| FR-009 | odoo | account.move close + report | reclassification rows | uniformity + comparative reclass unless impracticable (3.11-3.13) |
| FR-010 | odoo | res.company + report header | currency, rounding, identification | presentation currency per Sec 30 (03 by id); domicile/legal-form notes |
| FR-011 | odoo | account.move engine | accrual basis | native; CFS exception per Sec 7 (02 by id) |
| FR-012 | odoo | l10n_sv_chart.disproportionate_cost_use | registry rows | lower PYME threshold; per-use disclosure with reasons; re-judged per measurement date (2.28-2.30); 19.16/19.38 excluded (07 by id) |
| FR-013 | odoo | l10n_sv_chart.policy | hierarchy refs | 10.4-10.5 sources descending; full-NIIF aid non-binding (10.6; R29(a)) |
| FR-014 | odoo | l10n_sv_chart.policy_event | kind gating | change only if Standard-required or more-reliable-and-relevant (10.8); not-a-change + election-change classification (10.9/10.10) |
| FR-015 | odoo | l10n_sv_chart.policy_event + asset model | revaluation_switch_prospective | 10.10A: prospective, never 10.11-10.12; revaluation mechanics = 04 by id |
| FR-016 | odoo | account.move + report | retroactive restatement entries | comparative restatement or earliest-practicable opening (10.11-10.14); disclosures once |
| FR-017 | odoo | account.move | prospective estimate entries | 10.14A-10.16 (+10.17 carrying-amount route); comparatives never rewritten |
| FR-018 | odoo | l10n_sv_chart.policy_event + account.move | error_correction_restatement | 10.18-10.23; ganancias-acumuladas routing; two-track invariant: SV-EINV-FR-159..164 and SV-CML-FR-024/025 linked by id, mechanics never restated; deferred-tax bridge = 08 by id |
| FR-019 | odoo | report layer | note_slot ordering | (a)-(d) statutory order (8.1-8.4); declaration = 3.3 via FR-004 gate |
| FR-020 | odoo | l10n_sv_chart.policy | materiality flag | 8.5 3rd-ed. "material o con importancia relativa" wording — version note below |
| FR-021 | odoo | l10n_sv_chart.note_slot | judgment vs estimation feeds | 8.6 vs 8.7 distinct; next-ejercicio risk + nature + carrying amount |

Version-regime notes (D12/D15): the NIIF edition is a DATED regime row —
3rd edition (Feb-2025) applies to annual periods beginning 2027-01-01,
early adoption permitted (A1; LB-002); SV 2025-2027 books may still run
under the 2nd (2015) edition (SOQ-48 — the Tabla A1 delta map and the
company-level edition flag are owned by `08_deferred-tax-adoption.md`
by id; 2nd-edition full text not in corpus). Edition-sensitive wording
in THIS file: 8.5's "material o con importancia relativa" is a 3rd-ed.
rewording vs the 2nd-ed. "significativas" (EVID-281) — FR-020 cites the
3rd-ed. print. D15 anchors: eligibility determinations, policy elections
and policy events resolve as-of their own assessment/change dates and
snapshot on the record; the Apéndice A transitional rows are T8's
surface. Mid-year go-live (D18): a migrating company's policy-event
history and restatement entries ingest as `is_historical` rows with
original-period semantics (tiered ingestion per D18; no re-derivation;
D19 sequence-init kin = T8's Sec 35 surface). No hard gates beyond the
1.5 declaration bar and the statutory change rules (D16 no-override:
never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a travel agency (or utility-style prepaid seller)
  that holds client funds in custody as an activity secondary to its main
  business, when its eligibility determination is recorded, then it does
  NOT acquire public accountability through trigger (b) — the
  secondary-custody carve-out flag keeps trigger (b) off — and, with the
  GPFS prong met, the PYME determination stands eligible (FR-003,
  FR-002).
- **AC-002:** Given a company switching its building PPE class from the
  cost model to the revaluation model, when the policy event is posted,
  then it records as revaluation_switch_prospective: the revaluation
  posts per Sección 17 mechanics at the switch date (04 by id) with NO
  comparative restatement and NO opening-balance re-expression — the
  10.11-10.12 restatement path stays closed (FR-015).
- **AC-003:** Given a 2025 fraud-induced overstatement of sales
  discovered in 2026 before FS authorization, when the error correction
  posts, then the accounting-book track restates: the 2025 comparatives
  are re-expressed through ganancias acumuladas with 10.23 disclosures —
  while any fiscal-side correction (an NCE for the DTE, or a CC Art. 439
  rectification entry) posts as its OWN track linked by id
  (SV-EINV-FR-159..164 / SV-CML-FR-024 mechanics, never restated), its
  entries landing in the new period only and never rewriting the
  restated comparatives (FR-018).
- **AC-004:** Given a company whose shares trade on a regional
  off-exchange market, when it prepares FS under the Norma's engine, then
  the notes carry NO "conforme a la Norma de Contabilidad NIIF para las
  PYMES" declaration — the 1.5 bar blocks the declaration slot regardless
  of any permissive local config (FR-004, FR-019).
- **AC-005:** Given a company whose ONLY equity movements are result,
  dividends and one error correction, when the FS set is generated, then
  the combined estado de resultados y ganancias acumuladas variant is
  selectable; when a PPE revaluation later posts OCI (superávit de
  revaluación), then the combined variant becomes unavailable and the
  full ERI + cambios-en-patrimonio pair is required (FR-006).
- **AC-006:** Given an investment property whose fair value cannot be
  measured without disproportionate appraisal cost (04 file's surface,
  by id), when the relief is applied, then a registry row records
  requirement, item, judgment basis and date, and the notes builder
  emits the fact-and-reasons disclosure; at the NEXT measurement date a
  fresh judgment row is required — the old row never stands as a
  permanent exemption (FR-012).
- **AC-007:** Given a controladora without public accountability of its
  own whose group consolidates under full NIIF, when its separate FS are
  prepared, then they may run under this Norma flagged on its OWN-status
  determination, clearly distinguished from the group's full-NIIF FS
  (FR-005).
- **AC-008:** Given a revised expected-credit-loss-style bad-debt
  percentage (estimate input change) vs the discovery that last year's
  provision was computed on the wrong aging table (error), when each is
  recorded, then the first posts prospectively through current-period
  P&L with no comparative rewrite, while the second opens the
  error-correction track restating comparatives through retained
  earnings — the two never share posting mechanics (FR-017, FR-018).
- **AC-009:** Given FS notes being assembled, when the judgment and
  estimation feeds run, then a 12.30 fair-value class judgment appears
  ONLY in the 8.6 judgment slot, and a next-ejercicio risky assumption
  (e.g. NRV key input) appears ONLY in the 8.7 estimation-uncertainty
  slot with its nature and carrying amount — the declaration and
  material policies preceding both in the statutory order (FR-019,
  FR-021).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-46 carried: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — who must apply NIIF-PYMES vs full NIIF, with which (if any) quantitative thresholds, is external dated law (32_ Prólogo P12 leaves it to jurisdictions). FR-001..005 encode the determination machinery as a config-gap with NO invented SV thresholds; the framework flag ships informational (SOQ-53). Criteria-instrument hunt open (candidates Res. 175-2023 [derogated intermediate] / Res. 82-2024; authority chain 76_-78_ owned W18; registry numbering ≥127; same instrument as commercial-legal/03 OQ-002). | no | Takumi S8 (sources watch) | open |
| OQ-2 | SOQ-47 carried (R29(c) working reading): CC Arts. 443-444 subordinate balance formation to Consejo criteria first and only in default to the "Normas Internacionales de Contabilidad" — whether the NIIF para PYMES (an IFRS Foundation "Norma de Contabilidad") satisfies the CC's "NIC" reference is an interpretive reading, OQ-tracked until the Consejo instrument lands. Working assumption: yes (IASB SME-level standards as the NIC-default realization; Consejo criteria first). The hook is consumed from SV-CML-FR-040 by id; never asserted as settled. | no | Takumi S8 (sources watch) | open |
| OQ-3 | SOQ-52 carried: sustainability reporting (NIIF S1/S2, ESG, emissions inventories) has NO SV adoption instrument in the corpus and is OUT of Odoo-localization core scope — boundary note only, no FRs invented (SAS discipline); any future SV adoption (or full-NIIF-group demand) = external watch. Kin: 33_ EVID-302 documents the S1/S2 landscape as distinct from the financial-statement layer. | no | Takumi S8 (boundary watch) | open |
| OQ-4 | SOQ-53 carried: framework-flag design — the per-company marco-contable flag (niif_pymes \| niif_plenas \| niif_plenas+NIIF19-2027) is informational config, not compliance-blocking, given SOQ-46 gates the legal boundary; the NIIF 19 third value rests on secondary authority only (33_ EVID-301, effective 2027-01-01). Design review at implementation: whether the flag should ever drive report-set selection once the SV instrument lands. | no | Takumi S8 (config design) | open |
