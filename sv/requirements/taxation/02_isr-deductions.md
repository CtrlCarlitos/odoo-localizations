# SV — Taxation — ISR deductions, non-deductibles & the Art. 28 pro-rata

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for computing El Salvador's
*renta neta* (net taxable income) under the *Impuesto sobre la Renta* (ISR,
income tax): the Art. 28 necessary-cost gate and the
gravadas ÷ (gravadas + no gravadas + no renta) pro-rata allocator for mixed
costs (with the D.L. 969-2024 carve-out that removes subjects holding
foreign-excluded concepts from the allocator); the D.L. 345-2019
interpretación auténtica on *mermas* and *pérdidas* (shrinkage and losses:
inherent, measurable, real-cost, documented, regulator-recognized, with the
zero-base guard); the Art. 29 general deduction rules (business expenses vs
perks, the payroll-deductibility gate conditioned on effected and entered
retentions, relatives-payment proof, foreign travel and domestic *viáticos*,
leases, insurance, taxes, fuel, repairs, interest, inventories/COGS,
agropecuario expenses); the Art. 29-A non-deductible classifier (retention-
linked block, interest/commissions conditions including the 3:1 thin-cap and
active-rate + 4 points tests, IVA-document defects, the 25-SMM cash-payment
disallowance, undocumented costs, fines, obsolete-inventory losses,
provisions, capital losses); the Art. 31-32 other deductions (*reserva
legal* cycle, bad debts with the Reglamento Art. 37 evidence checklist,
donations with the 20%-of-net cap and qualified-donee validation,
social-benefit expenses, employer social funds); and the Reglamento Art. 32
P&L fiscal-adjustment layer with gravable/no-gravable ledger segregation and
the 50/50 common-cost split.

It does **not** cover: the subject/period/method/territoriality frame
(`01_isr-framework.md`, T1 — its FRs are cited by id); rates, brackets and
special computations including the 25% separate liquidation of reduced
*reserva legal* and the capital-loss ledger (`03_isr-rates-gains.md`, T4);
withholding mechanics, the Art. 29.7 salaried fixed deduction and retention
tables (`04_isr-withholding.md`, T5); the 5% distributions regime and deemed
distributions such as preferred-share "interest"
(`05_isr-distributions.md`, T6); depreciation and amortization schedules,
including capitalized improvements and interest routed to depreciation
(`06_isr-assets.md`, T7); IVA retentions/perceptions and IVA credits
(`e-invoicing/` A10 — referenced, never duplicated); or payroll
contributions (later wave). Those files reference this one for the
deduction rules that operate inside the T1 frame.

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated
Ley ISR, current article text) with reform decrees 55_ (Art. 37), 56_
(D.L. 969-2024 — Art. 3.4 + Art. 28-final carve-out + derogations), 57_/58_
(interpretaciones auténticas) for changed articles > 03_ (historical
consolidation through D.L. 233-2012; supplies analysis via EVID ids).
Reglamento: 04_ = D.E. 101-1992 as consolidated with reforms D.E. 8-1993 /
39-1993 / **117-2001** (self-documented repeal map — R17); only survivor
articles are cited. Every Ley article below was re-verified in the 54_
consolidation text during this task (54_-verify rule; page anchors are 54_
pagination from the extraction txt `=== PAGE n ===` markers).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 28 | Renta neta = renta obtenida − necessary costs/expenses for producing the renta and conserving its source that THIS law determines, plus the deductions it establishes; ALL deductibility requirements of the Ley AND the Código Tributario must be met; costs related to no gravadas or non-renta activities NEVER deductible; mixed costs apportioned by factor = rentas gravadas ÷ (gravadas + no gravadas + no renta), deducting only the gravadas proportion | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 28 p.15 (EVID-097) |
| LB-002 | Interpretación auténtica D.L. 345-2019, Art. 28 (embedded in consolidation) | Necessary cost/expense includes mermas, pérdidas and gastos inherent to the activity, in measurable recognizable form and with real cost (e.g. perishables, consumer goods, textiles, electricity, hydrocarbons sectors), deductible when documented and recognized/accredited by the competent regulator entities; NEVER deductible when establishing renta imponible yields no tax computation (zero-base guard); effective 2019-06-08 (D.O. 31-V-2019 + 8 days) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` (embedded) / `sv/sources/58_InterpAut_Art28_DL345_DO_2019-05-31.pdf` | 54_ pp.15-17 embedded; 58_ Arts. 1-3 pp.1-2 (EVID-170) |
| LB-003 | Ley ISR, Art. 3 numeral 4, inciso final (stamp (24), D.L. 969-2024) | Subjects obtaining gravadas rents AND any Art. 3.4 foreign-excluded concept are excluded from the Art. 28-final cost/expense proportion mechanism (implements SV-TAX-FR-023) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 3.4 final p.4 (EVID-164) |
| LB-004 | Ley ISR, Art. 29 nums. 1-3 | Deductible: necessary business expenses (fletes, propaganda, libros, impresos, avisos, correspondencia, gastos de escritorio, energía eléctrica, teléfono) — NOT disbursements offered to clients/employees (boletos aéreos, servicios de cable, cuotas de clubes, joyas, prendas de vestir); remunerations for services directly producing gravada renta CONDITIONED on effected & entered social-security/previsional/ISR retentions (severance per Art. 4.3 included); relatives (4th degree consanguinity / 2nd affinity / spouse / compañeros de vida) and insider payments (legal reps, directors, advisers, apoderados, shareholders, members of sociedades de personas) require proof the work was necessary and actually performed; foreign travel (pasajes + taxes/port dues + documented food/lodging strictly business-linked; traveller = taxpayer, legal rep or employee with proven labor link); domestic viáticos per Art. 3.1 | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29.1-3 pp.17-19 (EVID-098) |
| LB-005 | Ley ISR, Art. 29 nums. 4-6 | Deductible: leases of goods used directly in production of computable income, pro-rated by time used in gravadas (seasonal-use exception); insurance premiums on renta-producing property (natural persons: only 50% of the home premium when the casa de habitación is partially used as the business office); taxes/rates/special fiscal & municipal contributions on imports, services or the income source — caused AND paid in the ejercicio (December: caused + paid within the legal deadline), EXCLUDING ISR, IVA (subject to Ley IVA Art. 70), real-estate transfer tax, fines/recargos/interest | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29.4-6 pp.19-20 (EVID-098) |
| LB-006 | Ley ISR, Art. 29 nums. 8-9 | Deductible: fuel for machinery, cargo transport and work equipment (when not part of cost per num. 11), delivery/collective-transport/salespersons' vehicles and activo realizable vehicles, documented with factura or comprobante de crédito fiscal a nombre del contribuyente; ordinary repairs/maintenance — NOT remodeling, extension of original structure, value increase or life extension (those capitalize) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29.8-9 p.20 (EVID-098) |
| LB-007 | Ley ISR, Art. 29 nums. 10-12 + inciso final | Deductible: loan interest invested in the gravable source + loan constitution/renewal/cancellation costs pro-rated over the financing term; NOT deductible: own-capital/utilities interest not owed to third parties, interest linked to non-gravable assets (capitalize into asset cost, deduct via depreciation), preferred-share "interest" that is really dividends, back-to-back excess (source interest deductible only up to the lower on-lent rate); COGS = opening inventory + production/acquisition cost − closing inventory, CT Art. 143 valuation method, CT Art. 142 registry correspondence (differences non-deductible when unmet), production cost = raw material + labor + indirect fabrication costs deductible only as finished goods sold; agropecuario indispensable expenses (own-harvest products and own labor excluded); manufacturing costs accumulated prorata via costing systems, deducted as products are sold/used/consumed | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29.10-12 + final pp.20-22 (EVID-098) |
| LB-008 | Ley ISR, Art. 29-A nums. 1-13 | Non-deductible: personal/living costs (1); remunerations for services alien to computable income — retention duty survives (2); capital yields/retiros/anticipos to partners, shareholders, titulares, spouses/relatives unless proven invested in the source (3); unproven travel/viáticos (4); acquisitions and permanent value-increasing improvements (5); personal housing/vehicles/fuel of insiders unless directly bearing on the source (6); utilities to capital increase/reserves not expressly admitted (7); preferred-share dividends (8); donations not comprised in the Ley (9); capital losses and related/preferential-regime transaction losses (10); catch-all non-indispensable (11); retention-linked block — costs over retention-subject rents when payment made and retention not effected/entered (12), cured by entering in the ejercicio; December retention values per Art. 62 inc. 2 (13) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29-A.1-13 pp.22-24 (EVID-100) |
| LB-009 | Ley ISR, Art. 29-A num. 14 | Interest, commissions and any other payment from financial, insurance or reinsurance operations non-deductible when: (a) ISR/IVA retentions not effected when due per CT; (b) related domiciled lender did not declare them as gravada renta of the devengo period; (c) exceeding the BCR-published average active rate on enterprise credits + 4 additional points with related or preferential-regime/foreign lenders; (d) thin-cap: related/preferential-regime-lender indebtedness exceeding 3 × average patrimonio o capital contable (average = (opening + closing) ÷ 2); rules (c)/(d) inapplicable to SSF-supervised subjects under other indebtedness norms and to savings-credit cooperatives and their federations | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29-A.14 pp.24-25 (EVID-100; EVID-166 verify: "POR TRES VECES" p.24) |
| LB-010 | Ley ISR, Art. 29-A nums. 15-24 | Non-deductible: IVA-control documents with defects (15: unregistered emitter; operation unproven; numbering not AT-assigned/authorized; not in acquirer's name or economic burden unproven); non-necessary acquisitions/uses (16); uninformed/unauthorized-numbering/excess/unproven donations (17); undocumented or unrecorded costs — closing figures definitive unless certified per CT Art. 134 by a Consejo-de-Vigilancia-authorized CPA (external auditor / fiscal-report auditor variants) (18); goodwill, marks and similar intangibles amortization/depreciation (19); sanctions, fines, recargos, moratory interest, penal clauses (20 — except regulator-mandated compensations/devolutions on declared renta gravada); losses on deteriorated/expired/caducidad realizable assets (21 — production-defect goods actually sold excepted); castigos/provisions not expressly permitted by the Ley (22); acquisitions/services ≥ 25 salarios mínimos mensuales paid (i) in cash or (ii) in other media without written contract/escritura pública/civil-commercial documents (23); deductions not expressly contained in the Ley (24) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29-A.15-24 pp.25-27 (EVID-100; EVID-166 verify: "VEINTICINCO SALARIOS MÍNIMOS MENSUALES" p.26) |
| LB-011 | Ley ISR, Art. 31 | Also deductible: legal reserve of domiciled societies constituted on net utilities up to the legal/official minimum (mixed gravadas/exentas societies deduct only the gravadas proportion); reduction of previously-deducted reserva legal (capitalización, loss application, distribution or any circumstance) = renta gravada liquidated SEPARATELY at 25%, with a constitution/deduction register per ejercicio; bad debts (deudas incobrables): own-business origin, previously computed as gravable income, recorded/registered, information per reglamento; recovery = renta gravable of the receipt year (in-kind: capital gain/loss at realization); bank/insurer/cooperative reserves only as SSF-proposed and DGII-approved; portfolio transfer/reclassification → transferor income in the transfer year | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 31 pp.32-35 (EVID-099) |
| LB-012 | Ley ISR, Art. 32 | Deductible social erogaciones: construction/maintenance/operation of worker viviendas, escuelas, hospitales, medical assistance, cultural promotion, retirement pensions, health & life insurance and similar benefits provided FREE and GENERALIZED, in national territory (medical/hospital/studies assistance abroad accepted); sanitation works; patronal aportaciones to worker asociaciones/cooperatives for capital formation and cesantías funds (incl. capital participations a nombre of those entities); donations to Art. 6 entities capped at 20% of (renta neta of the donor − the donation), in-kind at donor cost (depreciated assets: cost − depreciation deducted), gratuitous and irrevocable, donee AT-qualified as excluded BEFORE the donation, AT-authorized document numbering; donations benefiting donor/family (4th degree/spouse) or, for juridical persons, socios/directivos/representatives/advisers and their families NOT deductible; sindicato/gremial cuotas (Art. 6-excluded entity + AT-authorized numbering + informed per CT Arts. 115-A/146 + exclusive worker-welfare/labor-rights use); ISSS cuota patronal for domestic workers and the subsidized labor cuota paid by the patrono | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 32 pp.35-36 (EVID-099) |
| LB-013 | Ley ISR, Art. 126 | The non-deduction regulations of Art. 29 nums. 1, 4, 5, 11 + final and Art. 29-A nums. 3, 6, 16, 20 merely INCORPORATE prior rules to facilitate application — no new non-deduction rules (interpretive anchor) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 126 p.56 (EVID-100) |
| LB-014 | Ley ISR, Art. 62 inc. 2 | December retention values that the retention agent may enter: entered within the respective legal term in the December declaration of the year the cost or expense was incurred (anchor for Art. 29-A.13; remittance mechanics per SV-TAX-FR-032 and 01-file OQ-001) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 62 inc. 2 p.43 (EVID-104) |
| LB-015 | Reglamento ISR (D.E. 101-1992 consolidado), Arts. 31-32 | Renta neta = renta obtenida − necessary costs/expenses; conservation expense keeps the source in working condition WITHOUT value increase; production costs = indispensable outlays before earning the income; formally-accounting taxpayers: start from book net income of P&L accounts, add back non-deductible items and any untaxed income; MUST segregate gravable vs no-gravable activity income/outflows so no-gravable results (positive or negative) never affect gravable results; non-attributable common expenses split 50/50 ("por iguales partes") between gravable and no-gravable | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 31-32 p.11 (EVID-140) |
| LB-016 | Reglamento ISR, Arts. 37-38 | Bad-debt deduction information (implements Ley Art. 31.2 d): debtor name/profession/domicile & amount; origin/constitution with grant & maturity dates; guarantee class & fiador data; date the debt became exigible; whether judicial collection was attempted and result; formal accounting/special-record correctness; any other DGII-required data; interest-bearing obligations — no bad-debt deduction above the agreed interest percentage | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 37-38 pp.12-13 (EVID-143) |
| LB-017 | Reglamento ISR, Art. 141 | Employer social funds (aportaciones patronales within Ley Art. 32.3): the taxpayer MUST create the corresponding accounting partida named per its own catalog of accounts; foreign-situated funds of this nature NOT deductible; funds not proven really incorporated into the entity's patrimony or capital NOT deductible | `sv/sources/04_Reglamento_ISR.pdf` | Art. 141 p.19 (EVID-146) |
| LB-018 | Reglamento ISR, Art. 28 | Employer deliveries to workers implementing Ley Art. 3.1 (reasonable viáticos for transport/food/lodging, work tools, office equipment) are not renta obtenida when they do not directly benefit the worker or increase his patrimony; the EMPLOYER bears the burden to prove via documents and registries that the money/goods were used for the assigned work | `sv/sources/04_Reglamento_ISR.pdf` | Art. 28 p.10 (EVID-139) |
| LB-019 | Ley Especial Quincena Veinticinco (D.L. 499, D.O. N° 8 T.450 14-ene-2026; effective on publication; **acquired 2026-08-18 as `66_`**), Art. 4 (gasto deducible clause): "Para efectos tributarios, los montos pagados en concepto de Quincena Veinticinco constituliran [sic] gasto deducible para el patrono, siempre que hayan sido efectivamente pagados y debidamente documentados, conforme a lo dispuesto en la Ley de Impuesto sobre la Renta." (full Art. 4 — worker-side treatment — recorded in `01_isr-framework.md` LB-032; not restated) | Employer Quincena-25 payments are a deductible employer expense (gasto deducible para el patrono) conditioned on ACTUAL payment ("efectivamente pagados") and due documentation ("debidamente documentados") conforme a the Ley ISR | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 4 p.4 (EVID-237) |
| LB-020 | Guía de Orientación Quincena Veinticinco (MH.UVI.DGII/006.001/2026; **acquired 2026-08-18 as `67_`**), §4: documentation = "planilla en original... y la suscripción de la misma por beneficiarios" + the F-14 Quincena annex (January-only upload per SV-FREP-FR-210; the same artifacts serve the FY-2026 credit documentation — `01_isr-framework.md` LB-035) | The operational documentation satisfying the Art. 4 gasto-deducible conditions: the original planilla subscribed (signed) by the beneficiaries + the F-14 v17 January annex (surfaces owned by fiscal-reporting/payroll, cited by id) | `sv/sources/67_Guia_Orientacion_Quincena25.pdf` | §4 pp.2-5 (EVID-237; EVID-238) |

Dead text (never implementable as current law): none new in this cluster —
the pago mínimo block (Arts. 76-81) and the D.L. 969-2024 derogated foreign
tracks are recorded in `01_isr-framework.md` §2 and are not restated here.

## 3. Functional Requirements

### 3.1 Deduction gate, pro-rata allocator and mermas (Art. 28)

- **SV-TAX-FR-034:** The system shall determine *renta neta* (net income) as
  renta obtenida minus the *costos y gastos necesarios* (necessary costs and
  expenses) for producing the renta and conserving its source that the Ley
  determines, plus the deductions the Ley establishes, admitting a cost or
  expense only when ALL deductibility requirements of the Ley ISR AND the
  Código Tributario are met conjunctively. (LB-001; EVID-097)
- **SV-TAX-FR-035:** The system shall block deduction of any cost or expense
  incurred in relation to activities generating *rentas no gravadas* (non
  taxable rents) or amounts that do not constitute renta under the Ley, in
  all cases. (LB-001; EVID-097)
- **SV-TAX-FR-036:** The system shall apportion mixed costs and expenses —
  those bearing on gravadas, no gravadas and non-renta activity at once — by
  the factor rentas gravadas ÷ (rentas gravadas + rentas no gravadas + rentas
  que no constituyen renta), deducting only the gravadas proportion; the same
  factor is the allocator referenced by depreciation and software
  amortization (`06_isr-assets.md` §3 mixed-use pro-rata). (LB-001;
  EVID-097)
- **SV-TAX-FR-037:** The system shall exclude from the Art. 28-final
  pro-rata mechanism every subject flagged `isr_foreign_excluded_concepts`
  (per SV-TAX-FR-023: gravadas rents AND Art. 3.4 foreign-excluded
  concepts), applying no apportionment factor to such subjects. Version note
  (D12): carve-out added by D.L. 969-2024, effective 2024-03-22; periods
  before the cutover compute with the allocator on the then-applicable
  income classification (dated data). (LB-003; LB-001; EVID-164)
- **SV-TAX-FR-038:** The system shall admit *mermas, pérdidas* (shrinkage,
  losses) and analogous costs/expenses as necessary costs under Art. 28 when
  they are inherent to the activity, in a measurable and recognizable form,
  with a real cost in the activity developed, duly documented, and
  recognized or accredited by the competent regulator entities or organisms;
  and shall apply the zero-base guard — such cost/expense is in no case
  admissible when establishing the renta imponible yields no computation of
  tax (no negative base is generated through this channel; consistent with
  the no-general-NOL finding, `03_isr-rates-gains.md` §3 losses). Version
  note (D12): interpretación auténtica D.L. 345-2019, effective 2019-06-08;
  periods before that date apply the pre-interpretation Art. 28 text.
  (LB-002; EVID-170)

### 3.2 Art. 29 general deduction rules

- **SV-TAX-FR-039:** The system shall admit as deductible the *gastos del
  negocio* (necessary business expenses destined exclusively to the
  business's purposes: freight and cartage not included in cost, propaganda,
  books, printed matter, notices, correspondence, office expenses,
  electricity, telephone and similar), and shall reject disbursements offered
  to clients and employees and analogous expenses (airline tickets, cable
  services, club fees, jewels, clothing) that are not necessary for renta
  production or source conservation. (LB-004; EVID-098)
- **SV-TAX-FR-040 (payroll-deductibility gate):** The system shall admit
  remunerations and compensations (salaries, *sueldos, sobresueldos, dietas,
  honorarios*, commissions, *aguinaldos*, gratuities and other remunerations)
  for services rendered directly in the production of gravada renta as
  deductible ONLY when the corresponding social-security, previsional and ISR
  retentions have been effected and entered (*realizado y enterado*, per the
  54_ text "SE HAYAN REALIZADO Y ENTERADO") whenever subject to them under
  the respective law; the same condition
  governs dismissal indemnities and voluntary-retirement bonuses (per Art.
  4.3) and indemnities for death, accident, incapacity or illness. Retention
  mechanics and tables are specified in `04_isr-withholding.md` §3, which
  consumes this gate. (LB-004; EVID-098)
- **SV-TAX-FR-041:** The system shall require, for payments under
  SV-TAX-FR-040 concepts to relatives of the contributor within the fourth
  degree of consanguinity or second of affinity, the spouse or *compañero o
  compañera de vida* (life companion), and equally for payments to legal
  representatives, directors, advisers, *apoderados* (attorneys-in-fact) and
  shareholders of juridical persons and members of *sociedades de personas*,
  proof that the work performed was necessary for renta generation or source
  conservation AND that it was effectively performed, in addition to all
  other deduction requirements. (LB-004; EVID-098)
- **SV-TAX-FR-042:** The system shall admit foreign-travel costs (transport
  fares plus taxes and port duties paid by the employer, plus
  documentally-provable food and lodging strictly linked to business travel)
  only when the traveller is the contributor, the legal representative or an
  employee whose labor-dependency link in the business is proven; and shall
  admit domestic *viáticos* (travel per-diems) for trips within El Salvador
  under the Art. 3.1 terms (per SV-TAX-FR-004), including the employer's
  documentation burden to prove via documents and registries that the
  deliveries were used for the assigned work. (LB-004; LB-018;
  EVID-098/139)
- **SV-TAX-FR-043:** The system shall admit lease prices of muebles or
  inmuebles (movable or immovable goods) used directly in the production of
  computable income, deducting in proportion to the time the leased goods
  were used in gravadas production — except seasonal-use assets, which
  deduct without time proration. (LB-005; EVID-098)
- **SV-TAX-FR-044:** The system shall admit insurance premiums covering
  risks of property used to produce gravada renta (merchandise, transport,
  *lucro cesante* — loss of profits), and, for natural-person subjects,
  shall cap the deduction of the premium on the *casa de habitación*
  (dwelling house) at 50% when the house is insured and partially used as
  the business office directly related to obtaining the renta. (LB-005;
  EVID-098)
- **SV-TAX-FR-045:** The system shall admit taxes, rates and special fiscal
  and municipal contributions levied on the import of goods, on services
  rendered by the enterprise, or taxing the renta-producing source, when
  caused AND paid during the corresponding ejercicio — for December amounts,
  when caused and payment is proven within the legal deadline — and shall
  always exclude the ISR itself, IVA (subject to Ley IVA Art. 70 credit
  rules, `e-invoicing/` A10), the real-estate transfer tax, and fines,
  surcharges and interest incurred on any fiscal or municipal contribution.
  (LB-005; EVID-098)
- **SV-TAX-FR-046:** The system shall admit fuel expenditures only for the
  whitelisted vehicle/equipment uses — machinery, cargo transport and work
  equipment (when not part of cost per the COGS rule), delivery vehicles,
  collective personnel transport, salespersons' vehicles, and *activo
  realizable* (realizable-asset) vehicles — when used directly in renta
  generation and duly proven with a *factura* or *comprobante de crédito
  fiscal* issued in the contributor's name (electronic document types per
  SV-EINV-FR-001). (LB-006; EVID-098)
- **SV-TAX-FR-047:** The system shall admit ordinary repairs and maintenance
  (expenses keeping goods in good working, service or production condition)
  as deductible, and shall route to capitalization — not current deduction —
  repair-classified expenses that imply remodeling, extension of the original
  structure, value increase or life extension of the goods (depreciation
  treatment in `06_isr-assets.md` §3). (LB-006; EVID-098)
- **SV-TAX-FR-048:** The system shall admit loan interest paid or incurred
  when the borrowed amounts are invested in the gravable renta-producing
  source, and shall deduct the costs of constitution, renewal or cancellation
  of such loans proportionally over the agreed financing term. (LB-007;
  EVID-098)
- **SV-TAX-FR-049:** The system shall treat as non-deductible: interest
  computed on own capital or utilities invested in the business that does not
  represent charges in favor of third parties; interest linked to assets not
  producing gravable renta — capitalizing it into the acquisition cost of the
  asset, deductible only via depreciation (`06_isr-assets.md` §3);
  "interest" assigned or paid to holders of preferred shares that in reality
  constitutes dividends or distributions of utilities (5% regime routing in
  `05_isr-distributions.md` §3); and, under back-to-back financing (source
  funds on-lent at a lower rate), source-financing interest only up to the
  amount computed at the lower on-lent percentage. (LB-007; EVID-098)
- **SV-TAX-FR-050:** The system shall compute cost of goods sold as opening
  inventory plus the cost of production, fabrication, construction or
  manufacture of finished goods plus the cost of merchandise and other goods
  acquired or extracted during the ejercicio, minus closing inventory; shall
  apply the inventory valuation method adopted under CT Art. 143; shall
  verify that opening/closing inventories correspond to the CT Art. 142
  inventory-control registry and *actas* (certified inventory records),
  rejecting cost-of-sales differences when those duties are unmet; shall
  admit production cost (raw material + labor + indirect fabrication costs)
  only for finished goods sold in the period; and shall accumulate
  manufacturing/transformation costs prorata
  under the taxpayer's costing systems, deducting them as the finished
  products are sold, used or consumed in gravable-renta operations.
  (LB-007; EVID-098)
- **SV-TAX-FR-051:** The system shall admit *gastos agropecuarios*
  (agricultural/livestock expenses) indispensable for obtaining computable
  income (day wages, sowing and re-sowing, fodder, plants, seeds, fertilizers,
  paid pasturage, *terrajes o censos* (land-use royalties or perpetual
  annuity charges on property), fence conservation, pruning, cleaning
  and similar), excluding the value of products harvested in the same
  exploitation and the contributor's own labor. (LB-007; EVID-098)
- **SV-TAX-FR-175:** The system shall treat employer Quincena-25
  payments as *gasto deducible* per D.L. 499 Art. 4, conditioned on
  ACTUAL payment and documentation conforme a la Ley ISR —
  operationally the original signed planilla + the F-14 January annex
  (67_ §4; the deduction and the FY-2026 credit of SV-TAX-FR-174
  coexist per the law's cumulative text — OQ double-benefit); the
  tercerización IVA-side treatment (FCF con valor exento; no Ley IVA
  Art. 66 pro-rata) is recorded as an IVA-wave pointer (IVA-core files
  owed — OQ). (LB-019; LB-020; EVID-237; cross-ref SV-TAX-FR-174,
  SV-PAY-FR-142, SV-FREP-FR-209)

### 3.3 Art. 29-A non-deductible classifier

- **SV-TAX-FR-052:** The system shall classify every cost, expense or
  *erogación* (expenditure) against the Art. 29-A catalog and tag it with the applicable
  non-deductible head(s): personal/living costs of the contributor, family,
  partners, consultants, advisers, representatives, directors or executives
  (1); remunerations for services alien to computable-income production — the
  retention duty surviving nonetheless (2); capital yields, withdrawals or
  advances to partners, shareholders, *titulares*, their spouses or
  relatives, unless effectively proven invested in the gravable source (3);
  travel or viáticos of the contributor, partners or employees not proven
  indispensable (4); acquisitions of goods and permanent value-increasing
  improvements (depreciation preserved) (5); housing acquisition or rent,
  vehicles and their fuel, lubricants, spare parts, maintenance, improvements
  or repairs for the personal use of insiders and their families, unless the
  goods directly bear on the renta source (6); utilities destined to capital
  increase or reserve/eventuality funds whose deduction the Ley does not
  expressly admit (7); dividends paid to preferred-share holders (8);
  donations and contributions not comprised in the Ley (9); any other
  non-indispensable expense (11); acquisitions or uses of goods/services not
  necessary for gravable renta production or source conservation (16);
  donations not informed by donataries, on non-authorized numbering, above
  the legal percentage or unproven (17); amortization or depreciation of
  *derechos de llave* (goodwill), marks and similar intangibles (19 —
  software amortization under Art. 30-A remains deductible,
  `06_isr-assets.md` §3); and deductions not expressly contained in the Ley
  (24) — noting per Art. 126 that the listed incorporations are interpretive,
  not new rules. (LB-008; LB-013; EVID-100)
- **SV-TAX-FR-053:** The system shall block costs and expenses related to
  retention-subject rents when payment was made and the obligation to retain
  and enter the retained tax was not fulfilled, releasing the block only when
  the retention agent enters the corresponding retention values in the
  ejercicio or imposition period concerned, all other deductibility
  requirements also being met; December retention values follow the Art. 62
  inc. 2 rule (entered within the legal term in the December declaration of
  the year the cost or expense was incurred — scheduling per SV-TAX-FR-032;
  CT-supersession doubt tracked as 01-file OQ-001). (LB-008; LB-014;
  EVID-100/104)
- **SV-TAX-FR-054:** The system shall block interest, commissions and any
  other payment from financial, insurance or reinsurance operations
  contracted by the borrower subject when: (a) the ISR or IVA retentions
  established in the Código Tributario were not effected when due; (b) the
  lender or provider is a related domiciled subject that did not declare
  them as rentas gravadas in the ejercicio of their accrual; (c) they exceed
  the result of applying to the loans or credits the average active interest
  rate on enterprise credits published by the Banco Central de Reserva plus
  four additional points, when the lender is a related subject or is
  domiciled, constituted or located in a preferential-regime, low- or
  no-taxation jurisdiction; or (d) thin capitalization — the indebtedness
  from credit, insurance or reinsurance operations with related or
  preferential-regime lenders exceeds three times the borrower's average
  *patrimonio o capital contable* (equity: (opening + closing) ÷ 2 of the
  ejercicio); the (c)/(d) blocks shall not be applied to subjects supervised
  by the Superintendencia del Sistema Financiero that are obliged to comply
  with indebtedness norms in other legal bodies, nor to savings-credit
  cooperatives and their federations. (LB-009; EVID-100/166)
- **SV-TAX-FR-055:** The system shall block values supported by IVA-control
  documents when: the document's emitter is not registered as a contributor
  of that tax; the acquirer of the goods or services does not prove the
  effective existence of the operation and its realization by the supposed
  transferor; the document numbering was not assigned and authorized by the
  Administración Tributaria; or the documents are not in the acquirer's name
  or, being so, the acquirer does not prove having borne the economic burden
  of the expense. (IVA retention/perception regimes are owned by
  `e-invoicing/` A10 — referenced, not duplicated.) (LB-010; EVID-100)
- **SV-TAX-FR-056:** The system shall block acquisitions of goods or use of
  services whose amounts equal or exceed twenty-five *salarios mínimos
  mensuales* (25 SMM, monthly minimum wages) that: (i) are not effected by
  cheque, bank transfer, or credit or debit card; or (ii) being paid by a
  medium other than cash and the (i) media, are not formalized in written
  contract, *escritura pública* (public deed) or the other documents
  regulated by civil or mercantile law (permutas, non-monetary mutuos,
  *daciones en pago*, title cessions, debt compensations, accounting
  operations). This ISR rule is distinct from the IVA 58-SMM rule of Ley IVA
  (different tax — do not conflate; A10/EVID-050). Version note (D12): the
  threshold is SMM-indexed — the parameter takes dated salario-mínimo values
  (OQ-002). (LB-010; EVID-100/166)
- **SV-TAX-FR-057:** The system shall block costs or expenses not duly
  documented and recorded in accounting, treating the financial figures at
  the close of each period reflected in legal and auxiliary books, special
  registries, financial statements and their notes and annexes as definitive
  and unmodifiable by the subject, except where the modification is
  certified by a public accountant authorized by the Consejo de Vigilancia
  de la Profesión de la Contaduría Pública y Auditoría (the external
  financial auditor, when one must be appointed; otherwise the
  fiscal-report auditor), presented within the CT Art. 134 term.
  (LB-010; EVID-100)
- **SV-TAX-FR-058:** The system shall block sanctions, fines, surcharges,
  moratory interest, *cláusulas penales* (penal clauses) and similar
  penalties paid by judicial route, private agreement or any other
  dispute-resolution means, admitting as deductible the exception of
  compensations or devolutions effectively made to clients in compliance
  with regulator-established norms (or the regulators' arbitration process,
  inherent to the business), on values that had been declared as renta
  gravada by the paying subject. (LB-010; EVID-100)
- **SV-TAX-FR-059:** The system shall block the loss resulting from facing
  the acquisition cost against the sale value of realizable assets in a
  state of deterioration, expiry, *caducidad* (expiration) or similar —
  while NOT blocking goods with defects or damage resulting from the
  production process that are subsequently effectively sold. (LB-010;
  EVID-100)
- **SV-TAX-FR-060:** The system shall block expenses for *castigos* (write-
  offs) or provisions of any nature contained in accounting principles or
  norms, or norms issued by regulators, whose deduction the Ley does not
  expressly permit. (LB-010; EVID-100)
- **SV-TAX-FR-061:** The system shall block capital losses — from Art. 14
  and Art. 42 transactions or any others — from deduction against ordinary
  income (their restricted ledger treatment is specified in
  `03_isr-rates-gains.md` §3 losses), and shall block in all cases losses
  from acts or operations between related subjects or with persons or
  entities resident or domiciled in preferential-regime, low- or
  no-taxation jurisdictions or tax havens. (LB-008; EVID-100)

### 3.4 Arts. 31-32: reserva legal, bad debts, donations, social expenses

- **SV-TAX-FR-062:** The system shall admit the *reserva legal* (legal
  reserve) of domiciled societies constituted on the net utilities of each
  ejercicio as deductible up to the minimum limit determined in the
  respective laws or by the competent government offices per society nature;
  for societies performing both gravadas and exentas activities, the reserve
  is deductible only in the proportion corresponding to gravadas operations.
  (LB-011; EVID-099)
- **SV-TAX-FR-063:** The system shall treat any reduction of the reserva
  legal in an ejercicio or period — by capitalization, application to prior-
  year losses, distribution or any other circumstance — as renta gravada of
  the society, for the cuantía that was deducted for ISR purposes in
  ejercicios prior to the reduction, liquidated SEPARATELY from ordinary
  rents at the 25% rate (separate-liquidation computation in
  `03_isr-rates-gains.md` §3); the system shall keep a register of the
  constitution of the reserva legal and of the amount deducted in the
  determination of renta neta or imponible in each ejercicio. (LB-011;
  EVID-099)
- **SV-TAX-FR-064:** The system shall admit the value or balance of *deudas
  incobrables* (uncollectible debts) as deductible when: the debt originates
  in own-business operations producing computable income; it was in its
  opportunity computed as gravable income; it is contabilized or annotated
  in special registries; and the contributor provides DGII the Reglamento
  Art. 37 information — debtor name, profession and domicile with the
  amount; origin and constitution of the debt with grant and maturity dates;
  guarantee class and *fiador* (guarantor) data; the date the debt became
  exigible; whether judicial collection was attempted and its result; the
  correctness of formal accounting or special records; and any other
  DGII-required data — with no deduction above the agreed interest
  percentage for interest-bearing obligations (Reglamento Art. 38).
  (LB-011; LB-016; EVID-099/143)
- **SV-TAX-FR-065:** The system shall recognize recovery of amounts
  deducted as bad debts (totally or partially) as renta gravable of the
  ejercicio in which received, to the deducted cuantía; where recovery
  occurs through acquisition of goods in kind, as renta gravable for the
  total deducted regarding the recovered credit, affecting the value at the
  moment of realization of the good as capital gain or loss according to the
  definitively recovered net value (computation per `03_isr-rates-gains.md`
  §3); and shall declare as renta gravable, in the ejercicio of the
  transfer, the fiscally-claimed deduction or reserve value when a
  receivables portfolio is transferred or a receivable is reclassified to a
  lower-risk category. (LB-011; EVID-099)
- **SV-TAX-FR-066:** The system shall admit donations to Art. 6 entities up
  to the maximum cap of twenty percent of the value resulting from
  subtracting the donation from the donor's renta neta in the respective
  periodo or ejercicio (cap = 20% × (renta neta − donation)); value
  donations of services or goods in kind at the donor's incurred cost, and
  previously-depreciated assets at cost minus the depreciation deducted; and
  require donations to be gratuitous and irrevocable in all cases.
  (LB-012; EVID-099)
- **SV-TAX-FR-067:** The system shall validate donation deductibility
  requiring: the donee institution to be qualified by the Administración
  Tributaria as an excluded subject under Art. 6 WITH ANTERIORITY to the
  donation (qualification cycle per SV-TAX-FR-008); the supporting documents
  to carry numbering assigned and authorized by the Administración
  Tributaria (donataries request the authorization); and shall block
  donations to entities benefiting directly or indirectly the donor, the
  donor's family up to the fourth degree of consanguinity, spouse or life
  companion — and, for juridical-person donors, benefiting the socios or
  shareholders, directors, legal representative, attorney-in-fact, advisers
  or the families of any of them up to the fourth degree, spouse or life
  companion. (LB-012; EVID-099)
- **SV-TAX-FR-068:** The system shall admit social-benefit *erogaciones*:
  construction, maintenance and operation of worker housing, schools,
  hospitals and medical-assistance and cultural-promotion services,
  retirement pensions, health and life insurance and similar benefits
  provided gratuitously and in generalized form to workers (for their and
  their children's cultural advancement and material welfare), performed in
  national territory — medical, hospital or studies assistance abroad also
  accepted — all duly proven to DGII's satisfaction; plus construction and
  maintenance of sanitation works provided gratuitously to workers on their
  properties or enterprises, to the inhabitants of a locality, or works of
  notorious benefit to a region. (LB-012; EVID-099)
- **SV-TAX-FR-069:** The system shall admit: patronal contributions for the
  constitution and functioning of worker *asociaciones o cooperativas*
  (associations or cooperatives operating with enterprise and worker
  participation) oriented to capital formation improving workers' and
  families' living conditions and to *cesantías* (severance) and other
  eventuality funds — including enterprise contributions to enterprise
  capital in the name of those entities enabling worker participation in
  capital and administration; *cuotas o aportaciones* (fees or contributions)
  to worker unions, associations, foundations or guild entities when the
  entity is Art. 6-excluded, supports the fee on documents with
  AT-authorized correlative numbering, has informed the values received per
  CT Arts. 115-A and 146, and uses them exclusively for workers' cultural
  welfare or defense of labor rights; and the ISSS patronal quota for
  domestic workers of natural persons, together with the subsidized labor
  quota paid to that institution on the worker's account. (LB-012;
  EVID-099)
- **SV-TAX-FR-070:** The system shall require a dedicated accounting
  *partida* (line item) — named per the taxpayer's own chart of accounts —
  for employer social-fund contributions within Art. 32.3, and shall block
  deduction of funds of this nature constituted outside the country and of
  funds not duly proven as really incorporated into the entity's patrimony
  or capital. (LB-017; EVID-146)

### 3.5 Reglamento Art. 32: fiscal-adjustment layer and segregation

- **SV-TAX-FR-071:** The system shall compute the fiscal renta neta of
  formally-accounting taxpayers starting from the book net result of the
  profit-and-loss accounts, adding back the non-deductible items classified
  under Art. 29-A (SV-TAX-FR-052..061 output) and any income not subject to
  tax, per Reglamento Art. 31-32. (LB-015; EVID-140)
- **SV-TAX-FR-072:** The system shall segregate gravable-activity and
  no-gravable-activity income and outflows in the ledgers so that
  no-gravable results — positive or negative — never affect gravable
  results. (LB-015; EVID-140)
- **SV-TAX-FR-073:** The system shall split expenses not attributable to
  either activity (common costs) in equal parts — 50% to the gravable
  activity and 50% to the no-gravable activity — per Reglamento Art. 32.
  This flat Reglamento split is a rule of the ISR computation: it is NOT the
  Ley Art. 28 gravadas/total factor of SV-TAX-FR-036 (precedence question —
  OQ-001) and NOT the IVA Art. 66 sales-based proration (different tax —
  do not conflate). (LB-015; EVID-140)

## 4. Data Model

Machine-readable sidecars (e.g. the non-deductible head catalog, SMM
threshold parameters) live next to this markdown file when produced. Layer
semantics: this file introduces Odoo-side computation/bookkeeping data only
(wave default `odoo`; see §5).

**Deduction classification and pro-rata:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | isr_deductibility_status | select | deductible · non_deductible · partially_deductible · pending_evidence | FR-034, FR-052 |
| account.move.line | isr_nondeductible_head | m2m catalog | personal_living · non_business_remuneration · partner_capital_yield · unproven_travel · capital_asset_acquisition · insider_vehicles_housing · retained_profits_reserves · preferred_dividends · non_qualifying_donation · catch_all_non_indispensable · non_necessary_acquisition · donation_informal · intangible_amortization · not_in_law · retention_unpaid · interest_conditions · iva_document_defect · undocumented_unrecorded · cash_payment_25smm · fines_penalties · obsolete_inventory_loss · accounting_provision · capital_loss | FR-052..061 |
| account.move.line | isr_activity_link | select | gravadas · no_gravadas · no_renta · mixed | FR-035, FR-036 |
| l10n_sv.isr.prorata.computation (new) | fiscal_year, gravadas, no_gravadas, no_renta, factor, mixed_costs_pool, deductible_share | monetary/computed | factor = gravadas ÷ (gravadas + no_gravadas + no_renta); skipped when carve-out applies | FR-036, FR-037 |
| account.move.line | isr_merma_checklist | jsonb | inherent · measurable · real_cost · documented · regulator_recognized + zero_base_guard result | FR-038 |

**Payroll-deductibility gate (interface to `04_isr-withholding.md`):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (payroll expense) | isr_retention_gate | select | passed · failed_ss_retention · failed_isr_retention · failed_december_rule · not_subject | FR-040, FR-053 |

**Quincena-25 employer deduction (66_ Art. 4):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (Quincena-25 expense) | isr_quincena_deduction_gate | select | paid_documented · unpaid_accrual_pending | FR-175 |

**Art. 29/29-A rule fields:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | isr_insurance_home_office_cap | monetary (computed) | natural persons: 50% of the insured dwelling premium when partial business office | FR-044 |
| account.move.line | isr_tax_deduction_rule | select | caused_and_paid · december_legal_deadline · excluded_isr · excluded_iva · excluded_real_estate · excluded_fine_surcharge | FR-045 |
| account.move.line | isr_fuel_vehicle_class | select | machinery · cargo_transport · work_equipment · delivery · collective_transport · salesperson · realizable_asset | FR-046 |
| account.move.line | isr_repair_class | select | ordinary_repair · improvement_capitalized | FR-047 |
| account.move.line | isr_interest_rule | select | source_invested · own_capital · non_gravable_asset_capitalized · preferred_share_dividend · back_to_back_capped | FR-048, FR-049 |
| l10n_sv.isr.thin.cap.check (new) | lender, lender_related, preferential_regime, debt, opening_equity, closing_equity, avg_equity, bcr_active_rate, cap_rate | computed | 3:1 ratio vs average equity; BCR active average + 4 pts; supervised-entity/cooperative exemption flags | FR-054 |
| account.move.line | isr_payment_method_ok | boolean (computed) | ≥ 25 SMM: cheque/transfer/card, or non-cash non-card formalized in written contract/deed | FR-056 |
| account.move.line | isr_cogs_registry_match | boolean (computed) | inventories vs CT Art. 142 registry/actas correspondence | FR-050 |

**Arts. 31-32 registers and accounts:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.legal.reserve (new) | company, ejercicio, constituted, deducted, reduction_amount, reduction_cause, separately_taxed_25 | register per ejercicio | reduction_cause: capitalization · prior_loss_application · distribution · other | FR-062, FR-063 |
| l10n_sv.isr.baddebt.evidence (new) | move_line, debtor_name/profession/domicile, amount, origin_grant_date, maturity_date, guarantee_class, fiador, exigible_since, judicial_attempted, judicial_result, records_ok | checklist per Reglamento Art. 37 | all fields required before write-off posts | FR-064 |
| l10n_sv.isr.donation.cap (new) | ejercicio, renta_neta, donation_value, cap_amount, admissible_amount | computed | cap = 20% × (renta neta − donation) | FR-066 |
| res.partner (donee) | isr_art6_qualified + qualification dates | from the 01-file subject profile | donation validity pre-check (qualification BEFORE donation date) | FR-067 |
| account.account | isr_social_fund | boolean tag | dedicated partida per own catalog; domestic fund + incorporation proof required | FR-070 |

**Fiscal-adjustment layer and segregation dimension:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.fiscal.adjustment (new) | ejercicio, book_net_result, nondeductible_addbacks, untaxed_income_addbacks, fiscal_renta_neta | computed bridge | P&L → fiscal renta neta reconciliation | FR-071 |
| account.move.line | isr_activity_class | select | gravable · no_gravable · common | segregation dimension; common lines split 50/50 | FR-072, FR-073 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client. No SaaS rows are introduced in this file: none of these
FRs touch DTE generation/transformation (the only architecture-split surface
per `shared/docs/saas-thin-client-architecture.md` D2). Received-document
validations (FR-055) operate on bookkeeping data, not on DTE generation.
Model names are stable across Odoo 17/18/19/20; version-specific behavior is
recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-034 | odoo | account.move.line | isr_deductibility_status | Master gate; evaluation order: CT formal requirements then Ley rules |
| FR-035 | odoo | account.move.line | isr_activity_link | Hard block for no_gravadas/no_renta-linked lines |
| FR-036 | odoo | l10n_sv.isr.prorata.computation | factor | Applied at period close to mixed-cost pool; consumed by 06 file for depreciation |
| FR-037 | odoo | l10n_sv.isr.prorata.computation | carve-out skip | Reads res.company.isr_foreign_excluded_concepts (01 file FR-023); version: cutover 2024-03-22 |
| FR-038 | odoo | account.move.line | isr_merma_checklist | Zero-base guard evaluated against period renta imponible; version: interp effective 2019-06-08 |
| FR-039 | odoo | account.move.line / product.category | expense categorization | Perk blacklist seeded on category defaults, user-overridable with audit trail |
| FR-040 | odoo | account.move.line (payroll journals) | isr_retention_gate | Interface FR — `04_isr-withholding.md` retention/remittance data feeds the gate status |
| FR-041 | odoo | res.partner (employee/relative flag) + account.move.line | proof requirement flag | Kinship degrees stored on partner; blocks posting-to-deduction without evidence attachment |
| FR-042 | odoo | hr.expense | travel/viático fields | Traveler-role check (taxpayer/rep/employee); document backing cross-checks DTE types (SV-EINV-FR-001); employer burden per Reglamento Art. 28 |
| FR-043 | odoo | account.move.line (lease templates) | use-time proration | Seasonal flag exempts from time proration |
| FR-044 | odoo | account.move.line | isr_insurance_home_office_cap | Natural persons only; 50% computed on dwelling-premium lines |
| FR-045 | odoo | account.move.line | isr_tax_deduction_rule | December window check against legal deadline parameters |
| FR-046 | odoo | fleet.vehicle / account.move.line | isr_fuel_vehicle_class | Vehicle-use whitelist; document check (factura/CCF a nombre) |
| FR-047 | odoo | account.move.line / maintenance records | isr_repair_class | Improvement-classified amounts route to asset capitalization (06 file) |
| FR-048 | odoo | account.move.line / loan schedule | interest allocation + term proration | Loan constitution/renewal/cancellation costs spread over financing term |
| FR-049 | odoo | account.move.line | isr_interest_rule | Preferred-share lines route to 05 file distribution track; capitalization posts to asset cost |
| FR-050 | odoo | stock.quant / account.move | COGS engine | CT Art. 143 valuation method config; CT Art. 142 registry-match boolean blocks the difference |
| FR-051 | odoo | account.move.line | agro categorization | Own-harvest/own-labor exclusion parameters on agro expense accounts |
| FR-052 | odoo | account.move.line | isr_nondeductible_head catalog | Head catalog seeded from Art. 29-A; Art. 126 interpretive note recorded in catalog descriptions |
| FR-053 | odoo | account.move.line | retention-linked block | Cure = remittance posting within the ejercicio; December rule per SV-TAX-FR-032 (OQ-001 of 01 file may re-anchor to CT) |
| FR-054 | odoo | l10n_sv.isr.thin.cap.check | ratio/rate engine | BCR active-average rate as dated parameter feed (OQ-003); supervised-entity exemption flag on company |
| FR-055 | odoo | account.move.line | emitter/numbering checks | Cross-checks against l10n_latam partner registration + DTE numbering; IVA regime rules stay in e-invoicing modules |
| FR-056 | odoo | account.payment / account.move.line | isr_payment_method_ok | SMM parameter dated data (OQ-002); written-contract attachment alternative |
| FR-057 | odoo | account.move.line | closing-figures lock | Fiscal-year lock exception requires CPA certification attachment (CT Art. 134 term) |
| FR-058 | odoo | account.move.line | fine/penalty accounts | Regulator-compensation exception requires declared-renta-gravada link |
| FR-059 | odoo | stock.quant / account.move.line | deterioration/expiry flags | Production-defect goods actually sold exempted from the block |
| FR-060 | odoo | account.move.line | provision classification | Expressly-permitted list (e.g. Art. 31 reserves) maintained as whitelist |
| FR-061 | odoo | account.move.line | capital-loss routing | Loss ledger owned by 03 file; here only the ordinary-income block |
| FR-062 | odoo | l10n_sv.isr.legal.reserve | constitution rows | Mixed societies: gravadas-proportion proration on the deductible amount |
| FR-063 | odoo | l10n_sv.isr.legal.reserve | reduction rows | Triggers 25% separate-liquidation line in the 03-file computation; register per ejercicio |
| FR-064 | odoo | l10n_sv.isr.baddebt.evidence | checklist | Blocks write-off posting until all Reglamento Art. 37 fields complete |
| FR-065 | odoo | account.move.line | recovery recognition | Recovery posts to renta gravable; in-kind recovery defers gain/loss to realization |
| FR-066 | odoo | l10n_sv.isr.donation.cap | cap computation | Cap formula evaluated per donation and aggregated per ejercicio |
| FR-067 | odoo | res.partner (donee) | qualification pre-check | Consumes the 01-file utilidad-pública qualification dates; family-beneficiary block via partner kinship |
| FR-068 | odoo | account.move.line | social-benefit categorization | Free-and-generalized test flagged on benefit account defaults |
| FR-069 | odoo | account.move.line / res.partner (union) | union-quota validation | CT 115-A/146 informing flag on donee partner; ISSS domestic-worker quota category |
| FR-070 | odoo | account.account | isr_social_fund | Dedicated account in SV chart template; domestic + incorporation-proof validation |
| FR-071 | odoo | l10n_sv.isr.fiscal.adjustment | bridge computation | Consumes isr_nondeductible_head addbacks + untaxed-income classification (01 file territorial statuses) |
| FR-072 | odoo | account.move.line | isr_activity_class | Segregation dimension on accounts/journals; no-gravable results excluded from gravable determination |
| FR-073 | odoo | account.move.line | 50/50 split | Common lines split at period close; OQ-001 governs precedence vs Art. 28 factor |
| FR-175 | odoo | account.move.line (Quincena-25 expense journals) | isr_quincena_deduction_gate | Gate reads actual-payment state + planilla/F-14-annex documentation (67_ §4; amounts from the SV-PAY-FR-142 ledger); coexists with the FY-2026 credit (01-file SV-TAX-FR-174; OQ-008 double-benefit flag for fiscalización); IVA tercerización pointer owed to the IVA-core wave (OQ-009) |

Version-regime notes (D12): FR-037 records the D.L. 969-2024 carve-out
cutover (2024-03-22); FR-038 records the D.L. 345-2019 interpretation
effective 2019-06-08 — pre-cutover periods select the dated rule data.
FR-056's 25-SMM threshold and FR-054's BCR active-rate are indexed external
parameters: both store value + validity dates (OQ-002/OQ-003). All other
rules verified stable in the 54_ consolidation (no post-2012 reform touches
Arts. 28-32 per EVID-162/166). FR-175's Quincena-25 deduction is effective
from the 66_ publication (14-ene-2026): pre-2026 periods carry no such
expense class; from 2027 the benefit is mandatory but the FY-2026 credit
of SV-TAX-FR-174 does not continue (01-file D12 note).

## 6. Acceptance Criteria

- **AC-001:** Given gravadas rents $80,000, no gravadas $15,000, non-renta
  $5,000 and a mixed cost pool of $10,000, when the ejercicio closes, then
  factor = 0.80 and the deductible share of the pool = $8,000 (FR-036).
- **AC-002:** Given a subject with gravadas rents and any Art. 3.4
  foreign-excluded concept (flag per SV-TAX-FR-023), when the pro-rata
  computation runs for a post-2024-03-22 period, then no apportionment
  factor is applied; given the same subject computing a 2023 period, then
  the allocator applies on the dated income classification (FR-037).
- **AC-003:** Given a documented, regulator-recognized perishables merma of
  $2,000 with positive renta imponible, then it is deductible; given the
  same merma when the renta imponible computation yields zero tax, then it
  is not admitted (FR-038).
- **AC-004:** Given a salary expense whose SS and ISR retentions were
  effected and entered, then isr_retention_gate = passed and the expense is
  deductible; given the same expense with the ISR retention unpaid, then the
  line is tagged retention_unpaid and non-deductible until entered
  (FR-040, FR-053).
- **AC-005:** Given a num. 2-concept payment to the contributor's brother
  (2nd degree consanguinity) without proof of necessity and performance,
  then the payment is non-deductible (FR-041).
- **AC-006:** Given a foreign-travel expense whose food/lodging lack
  documentary support, or whose traveller has no proven labor link, then the
  food/lodging (or the whole deduction, respectively) is rejected (FR-042).
- **AC-007:** Given a seasonal-use leased harvester used 4 of 12 months,
  then the lease deducts in full; given a non-seasonal office lease used
  6 of 12 months in gravadas production, then 50% deducts (FR-043).
- **AC-008:** Given a natural person paying a $1,000 premium on the dwelling
  partially used as business office, then $500 is deductible (FR-044).
- **AC-009:** Given a municipal tax caused and paid in June, then it is
  deductible; given a December tax caused with payment proven within the
  legal deadline, then deductible, and with payment outside the deadline,
  rejected; given an ISR or IVA amount or a municipal fine, then always
  rejected (FR-045).
- **AC-010:** Given fuel documented with a factura a nombre for a delivery
  vehicle, then deductible; given fuel for a director's personal vehicle,
  then non-deductible (head insider_vehicles_housing) (FR-046, FR-052).
- **AC-011:** Given a $5,000 ordinary-repair invoice, then deductible; given
  a repair that extends the asset's useful life, then the amount is
  capitalized to the asset, not deducted (FR-047).
- **AC-012:** Given loan interest tied to an asset that produces no gravable
  renta, then the interest is capitalized into the asset cost and deducts
  only via depreciation (FR-049).
- **AC-013:** Given related-lender debt of $400,000 and average equity of
  $100,000 (3 × equity = $300,000), then the indebtedness exceeds the thin-
  cap ratio and the linked interest/commissions are non-deductible; given
  the borrower is an SSF-supervised entity, then rules (c)/(d) do not apply
  (FR-054).
- **AC-014:** Given a BCR-published average active rate of 6% (cap 10%) and
  a related preferential-regime lender charging 12%, then the excess above
  the cap-rate amount is non-deductible (FR-054).
- **AC-015:** Given a purchase equal to 25 SMM paid in cash, then
  non-deductible; given the same purchase paid by bank transfer, then
  deductible; given a barter of equal amount formalized in written contract,
  then deductible (FR-056).
- **AC-016:** Given renta neta of $100,000 and a donation of $10,000, then
  cap = 20% × $90,000 = $18,000 and the donation fully deducts; given a
  donation of $25,000, then cap = $15,000 and $10,000 is non-deductible
  excess (FR-066).
- **AC-017:** Given a donation to an entity AT-qualified as excluded one
  month after the donation date, then the donation is non-deductible;
  given qualification predating the donation, then the cap test applies
  (FR-067).
- **AC-018:** Given a reserva legal reduction of $20,000 that was fully
  deducted in prior ejercicios, then $20,000 enters as renta gravada
  liquidated separately at 25% and the register records the reduction with
  its cause (FR-063).
- **AC-019:** Given a bad debt of $5,000 deducted in 2023 and recovered in
  cash in 2025, then $5,000 is renta gravable of 2025; given recovery by
  receiving goods in kind, then renta gravable posts for the deducted amount
  and the capital gain/loss defers to the goods' realization (FR-065).
- **AC-020:** Given a no-gravable activity loss of $3,000 and a $10,000
  non-attributable common cost, then the loss never reduces the gravable
  result and the common cost splits $5,000 / $5,000 (FR-072, FR-073).
- **AC-021:** Given book net result $50,000, non-deductible addbacks $7,000
  and untaxed income $3,000, when the fiscal adjustment runs, then fiscal
  renta neta = $60,000 (FR-071).
- **AC-022:** Given closing inventory that does not correspond to the CT
  Art. 142 registry annotations, then the resulting cost-of-sales difference
  is non-deductible (FR-050).
- **AC-023:** Given a Quincena-25 employer payment of US$5,000.00 actually
  paid in January-2026 and documented with the original signed planilla +
  the F-14 January annex, then isr_quincena_deduction_gate = paid_documented
  and the expense is deductible; given the same amount merely accrued and
  unpaid at the deduction evaluation, then the gate = unpaid_accrual_pending
  and no deduction is admitted until actual payment (FR-175).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Ley Art. 28 inciso final pro-rata factor (gravadas ÷ total) vs Reglamento Art. 32 flat 50/50 split for non-attributable common costs: which governs common costs of formally-accounting taxpayers? Ley hierarchy and the (14) reform stamp suggest the Art. 28 factor prevails where it applies (Reglamento text is 1992-vintage). FR-036 and FR-073 implemented separately; reconcile if verification shows displacement (EVID-140 doubt; EVID-097). | no | Takumi S2 | open |
| OQ-002 | SMM parameter source for the 25-SMM threshold (FR-056): dated salario-mínimo values by sector/period are needed (source 16_ salarios mínimos per EVID-165 note); same feed serves the IVA 58-SMM rule (A10/EVID-050 — different tax, shared data). Confirm source registry and cadence. | no | Takumi S2 (sources registry) | open |
| OQ-003 | BCR "tasa promedio de interés activa sobre créditos a empresas" (FR-054 c): rate feed source and refresh cadence are outside the corpus; Odoo parameter needs a dated-value feed selection. | no | Takumi + Odoo implementation | open |
| OQ-004 | Art. 31.3 bank/insurer reserve regime (SSF-proposed, DGII-approved; classification exclusions; portfolio-transfer income): sector-specific — confirm deferral of FRs to the special-regimes wave rather than this generic file (EVID-099 gloss). | no | Takumi S2 (special-regimes wave) | open |
| OQ-005 | Reglamento Art. 141 requires social funds "actually transferred to legally-authorized Associations/Cooperatives": the registry of authorized entities (validation source for FR-070) is outside the corpus. | no | Takumi S2 (sources registry) | open |
| OQ-006 | Reglamento Art. 29's narrow deposit-interest exclusion (natural persons/banks only) is stale vs reformed Ley Art. 4.5 (any subject; supervised institutions incl. federations/cooperatives) — Ley governs; harmonized reading per SOQ-07 (4.5 carves out small depositors < $25,000 average balance). Recorded here so EVID-139's doubt is not dropped; substantive FRs live in `03_isr-rates-gains.md` / `04_isr-withholding.md`. | no | Takumi S2 (T4/T5 tasks) | open |
| OQ-007 | Art. 29.6 December window for deductible taxes (caused + paid within the legal deadline): confirm no CT rule re-anchors or complements the deadline — kin to 01-file OQ-001 on the Art. 62 December retention rule (LB-014 here). | no | Takumi S2 (CT pass) | open |
| OQ-008 | 2026 double benefit (66_ evidence OQ-4): an employer deducting the Quincena-25 payment (FR-175, 66_ Art. 4) ALSO records the FY-2026 100% credit (SV-TAX-FR-174, 66_ Art. 6) — the law text reads cumulative and no MH worked example says otherwise; both are encoded as written; flag for fiscalización criteria review (deduction + credit simultaneously on the same amounts). | no | Takumi S6 (fiscalización wave) | open |
| OQ-009 | IVA tercerización treatment: the tercerización contractor's separate documento fiscal for the Quincena-25 pass-through = "Factura de Consumidor Final, con valor exento" and per Ley IVA Art. 66 inciso sexto parte primera "no se aplicará la proporcionalidad del Crédito Fiscal por dicha operación" — IVA-side rules are out of ISR scope; pointer owed to the IVA-core files (future wave; deferred-by-design). | no | Takumi S6 (IVA-core wave) | resolved-by-pointer (S9 11_iva-pro-rata-remanente — R30(c) working reading) |
