# SV — Chart of accounts — Liabilities, equity & employee benefits: provisions, leases (dual model), employee benefits, equity, grants, borrowing costs

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file owns the N5 book-side cluster of the *Norma de Contabilidad NIIF
para las PYMES* (Accounting Standard for SMEs, 32_): **provisions and
contingencies** (Sección 21 — the three-gate recognition test, best-estimate
and present-value measurement, only-original-purpose use, remeasurement with
unwinding to finance cost, reimbursement assets, restructuring, onerous
contracts, contingency disclosure rules, gratuitous group-entity financial
guarantees); **leases** (Sección 20 — the DUAL *arrendamiento financiero /
arrendamiento operativo* (finance lease / operating lease) classification
model, lessee and lessor mechanics on both tracks, sale-and-leaseback
variants and maturity-band disclosures — explicitly NOT the IFRS-16
right-of-use model); **employee benefits** (Sección 28 — the four
categories, undiscounted short-term accruals, the
*acumulación de ausencias retribuidas* (accumulating paid absences) engine
that carries SV *vacaciones* (annual vacation) to the balance sheet, the
profit-sharing obligation gate, DC-style booking of the statutory ISSS/SIP
contributions, defined-benefit measurement with the 28.19 simplified
election, the uniform actuarial-gains policy, and termination-benefit
triggers); **equity** (Sección 22 — substance classification including the
five puttable-instrument conditions, issuance measurement with the
contra-equity receivable and its local-law override, par/excess presentation
deferred to local law, stock dividends and splits, the liability-first
convertible split, treasury shares, distributions and non-cash distributions,
plus the Código de Comercio Arts. 37-38 distribution-capacity overlay as a
SEPARATE statutory field never derived from NIIF equity); **government
grants** (Sección 24 — condition-gated income and liability, fair-value
measurement, and the tax-benefit carve-out that keeps ZF/LSI/DPA exemptions
out of this section); and **borrowing costs** (Sección 25 — ALL expensed,
no capitalization).

It does **not** cover: the ESF/P&L line architecture and equity
reconciliation (`02_coa-structure.md`); financial instruments, fair value
and FX (`03_financial-instruments-fx.md`); non-financial assets and their
depreciation/impairment engines (`04_nonfinancial-assets.md`); revenue and
contract balances (`06_revenue.md`); consolidation, business combinations
and related parties (`07_groups-related-parties.md`); deferred tax,
first-time adoption and edition versioning (`08_deferred-tax-adoption.md`).
**Two-track invariant (binding):** this file owns the ACCOUNTING book only.
The payroll statutory engine (vacaciones/aguinaldo/indemnización
computations, ISSS/SIP rates, caps and bases) is S4's, consumed BY FR ID;
ZF/LSI/DPA fiscal exemptions are the special-regimes wave's, consumed BY ID;
ISR deductibility of provisions, lease payments and interest is taxation's;
wherever book and fiscal treatment differ, the difference routes through
N8's deferred-tax FRs (`08_deferred-tax-adoption.md`, T8, by filename) —
never re-derived and never overridden here.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling
R29): the operative framework LB = **32_** — *Norma de Contabilidad NIIF
para las PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official
Spanish translation, Sections 1-35 + Apéndice A (fecha de vigencia y
transición) + Apéndice B (glosario, integral part of the Norma); effective
2027-01-01 with early adoption permitted (A1; txt PAGE 315), cited by
section/párrafo as printed. **33_** (EY *Guía Práctica de NIIF y
Sostenibilidad 2024/2025*) is SECONDARY-ONLY authority per R29(a): it can
NEVER be the sole LB of an FR; its LB role here is limited to the
documented full-NIIF-vs-PYMES contrast set (IFRS-16 right-of-use leasing and
IAS 23 borrowing-cost capitalization among the full-NIIF treatments this
file's engines deliberately do NOT implement); where 33_ and 32_ could
diverge, 32_ governs without exception.

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
stands unchanged — the engines ship the Norma's own machinery with NO
invented SV thresholds, the framework flag consumed from
`01_framework-policies.md` SV-COA-FR-001 by id (informational config).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 20 Arrendamientos: 20.3 in-substance leases — subcontracting arrangements, capacity in telecom networks and take-or-pay contracts "son arrendamientos"; contracts without a right of use are service contracts, not leases. 20.4-20.5: financiero when "transfiere sustancialmente todos los riesgos y ventajas inherentes a la propiedad"; situations that individually or in combination normally lead to financiero (transfer of ownership by end of term; bargain purchase option sufficiently certain; term for the major part of the asset's economic life; PV of minimum payments "sustancialmente todo" its fair value; specialized nature only the lessee can use) + indicators (lessee bears cancellation losses; residual fair-value fluctuations accrue to lessee; bargain-renewal rents). 20.7: classification made "en el inicio del arrendamiento" and reassessed only when "el plazo del arrendamiento cambia" (not for changed estimates of residual life or option likelihood). Lessee financiero 20.8-20.9: recognize asset + liability "al menor importe entre su valor razonable y el valor presente de los pagos mínimos" at "la tasa de interés implícita en el arrendamiento" when determinable "si no, a la tasa de interés incremental de financiamiento del arrendatario"; direct costs added to the asset. 20.10-20.12: minimum payments split so finance charge reflects "una tasa de interés constante en cada periodo sobre el saldo del pasivo"; contingent rents expensed when incurred; depreciation per the asset's section over useful life or shorter lease term unless ownership transfer reasonably certain. Lessee operativo 20.13-20.15: straight-line expense "a menos que: (a) otra base sistemática sea más representativa…; o (b) los pagos al arrendador se estructuren para incrementarse en línea con la inflación general esperada (basada en índices o estadísticas publicadas)" — then expense as incurred; worked example 100.000→146.000 u.m. over five years at 10% expected inflation. 20.16 maturity disclosures per band (hasta un año; entre uno y cinco años; más de cinco años). Lessor financiero 20.17-20.20: net investment receivable; constant periodic return; manufacturer-dealer lessors recognize selling result restricted to market price with the rest as finance income over the term, initial direct costs expensed. Lessor operativo 20.24: asset retained by nature class, straight-line income, direct costs added to the asset and amortized over the term. 20.31-20.34 sale-and-leaseback: financiero → excess of proceeds over fair value deferred and amortized; operativo at fair value → recognize; below-fair-value difference deferred when offset by below-market rents; above-fair-value excess deferred & amortized | SMEs retain the IAS-17-style DUAL lease model: in-substance lease identification (telecom capacity, take-or-pay, subcontracting); finance-vs-operating classification by substantial transfer of risks and rewards, with criteria and indicators, set at inception and reassessed only on a negotiated term change; lessee finance = asset and liability at the lower of fair value and PV of minimum payments at the implicit rate (else the lessee's incremental borrowing rate), EIR-split subsequent measurement, depreciation over the shorter of useful life and term unless ownership transfers; lessee operating = straight-line expense unless a systematic basis is more representative or payments are structured to escalate with expected general inflation (then expense as incurred); lessor finance = net-investment receivable with manufacturer-dealer splitting selling result (market-price-capped) from finance income; lessor operating = asset kept by class, straight-line income; sale-and-leaseback variants deferring or recognizing per classification; maturity-band disclosures ≤1y / 1-5y / >5y. Explicitly NOT IFRS 16 | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 20 whole (txt PAGE 171-179); 20.15(b) worked example (txt PAGE 174-175) (EVID-290) |
| LB-002 | Norma NIIF para las PYMES, Sección 21 Provisiones y Contingencias: 21.1A scope — financial-guarantee contracts issued gratuitously (and gratuitous loan commitments) are within this section's provision rules. 21.4 provision iff "(a) la entidad tiene una obligación presente como resultado de un suceso pasado; (b) es probable… que la entidad tenga que desprenderse de recursos…; y (c) puede realizarse una estimación fiable del importe". 21.5 → charge to "gasto… a menos que otra sección requiera que se reconozca como parte del costo de un activo". 21.6 no past event → no obligation (future operating losses never a provision — indicative of impairment questions); 21.6A-21.6B restructuring provision requires "un plan formal y detallado" (main features: business activities/locations affected, functions, approximate number of employees, expenditures by category, timing) + "una expectativa válida" in those affected (execution begun or main features announced). 21.7 best estimate (weighted for large populations; most-likely for a single obligation with other outcomes considered); 21.8-21.9 PV "si el efecto del valor del dinero en el tiempo es significativo" at "una tasa antes de impuestos que refleje las evaluaciones del mercado sobre… el pasivo" with risk "en la tasa de descuento o… en la estimación de los flujos de efectivo", NOT both; expected disposal gains not netted; significant classes measured separately. 21.10 charges only for "los desembolsos para los cuales fue reconocida originalmente"; remeasured each reporting date; unwinding = "un costo de financiamiento". 21.11 reimbursement: separate asset when "prácticamente cierto", never netted, ≤ the provision, related expense presentable net. 21.12 contingent liabilities not recognized (except assumed in business combinations, 19.19) — disclose unless remote; joint-and-several own-best-estimate share = provision, rest contingent; 21.13 contingent assets not recognized — disclose if probable (asset only when virtually certain). 21.17 prejudicial-disclosure carve-out: dispute nature + the fact of non-disclosure. 21.18-21.19 gratuitous group-entity guarantees: disclose nature/purpose, uncertain timing/amount, maximum exposure. Apéndice 21A: warranties worked PV example; onerous contracts = "el menor de entre el costo de cumplir con el contrato y el de compensarlo por incumplirlo"; court-case evidence judged at FS authorization date; division-closure timing | Provisions: three-gate recognition (present obligation from a past event + probable outflow + reliable estimate); expense or asset-cost posting; no provision without a past event (future operating losses excluded); restructuring needs a formal detailed plan plus valid expectation; best-estimate measurement with PV at a pre-tax market rate carrying the risk either in the rate or in the cash flows, never both; provisions used only for their original purpose and remeasured with unwinding as finance cost; reimbursement assets separate and virtually certain; contingent liabilities disclosed unless remote and contingent assets disclosed if probable; prejudicial-disclosure carve-out; gratuitous financial guarantees to group entities inside Sec 21 with nature/purpose/uncertainty/maximum disclosures; Apéndice onerous-contract lesser-of rule | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 21 whole + Apéndice 21A (txt PAGE 181-191) (EVID-291) |
| LB-003 | Norma NIIF para las PYMES, Sección 22 Pasivos y Patrimonio: 22.3-22.3A classify by "la esencia del acuerdo contractual, no simplemente por su forma legal"; absent "un derecho incondicional a evitar la entrega de efectivo u otro activo financiero" the obligation is a financial liability. 22.4 instrumento con opción de venta (puttable instrument) = equity only with ALL of: (i) "participación proporcional de los activos netos… en caso de su liquidación"; (ii) in "la clase de instrumentos que está subordinada a todas las demás clases"; (iii) "todos los instrumentos… de la clase… subordinada… tienen características idénticas"; (iv) no other contractual obligation to deliver cash/another financial asset or to exchange on potentially unfavorable terms (beyond the put/repurchase itself), nor settleable in own equity; (v) "los flujos de efectivo totales esperados… se basan sustancialmente en los resultados, en el cambio en los activos netos reconocidos o en el cambio en el valor razonable de los activos netos reconocidos y no reconocidos". 22.4(b): most-subordinate obligations due only at liquidation = equity. 22.5 liability examples: (a) liquidation distribution subject to a ceiling; (b) put redemption measured on a basis other than the Norma; (c) mandatory pre-liquidation payments ("un dividendo obligatorio"); (d) puttable instrument equity in a subsidiary → liability in the controladora's FS; (e) "una acción preferente que estipula un rescate obligatorio" at fixed/determinable amount or date → liability. 22.6 cooperative/partner interests = equity if unconditional refusal right or local-law prohibition on redemption. 22.7(a) equity issued before cash received → contra-equity "importe por cobrar" "a menos que las leyes o regulaciones locales prohíban dicha presentación"; 22.7(c) subscribed-unissued-unpaid → no equity increase. 22.8 measure at "el valor razonable de los recursos recibidos o por recibir, neto de los costos de transacción" (PV when deferred + material). 22.9 equity transaction costs "se deducirán del patrimonio". 22.11 par/excess presentation per applicable law. 22.12 capitalization/stock dividends/splits: "ningún cambio en el total del patrimonio"; reclassify per applicable law. 22.13-22.15 convertibles/composites: "primero se debe valorar el componente de pasivo" (FV of a similar non-convertible), residual → equity; transaction costs pro-rata on FV; no re-split later; 22.15A-C debt-for-equity settlements (FV; linked modifications split; in-substance same-control distributions/contributions excluded). 22.16 treasury shares: deduct equity at the FV of the consideration; "no reconocerá ganancias o pérdidas" on purchase, sale, issue or cancellation. 22.17 distributions reduce equity; related income tax per Sección 29. 22.18-22.18A non-cash distributions → liability at FV (carrying amount when FV not measurable without disproportionate cost), remeasured through equity, settlement difference → P&L. 22.18B same-ultimate-control distributions excluded. Apéndice a la Sección 22 (example, not part of the Norma): 500 bonos convertibles at par 100 u.m., 5 years, 4% coupon, 6% market rate for similar non-convertible debt → PV of liability 45.788 u.m. (37.363 principal + 8.425 interest), residual equity 4.212 u.m. | Equity: substance classification with the puttable five-condition equity carve-out and its liability-preference counter-examples (caps, non-Norma-measured redemption, mandatory dividends, puttable-in-subsidiary, mandatory-redeemable preference shares); cooperative interests; issuance booked at fair value net of transaction costs with an equity-deducted receivable for issued-but-unpaid equity subject to a local-law presentation override; par/excess presentation and inter-class reclassifications left to local law; stock dividends and splits never change total equity; convertible/composite split liability-first with the worked 6%/45.788/4.212 calibration and no later re-split; debt-for-equity conversions; treasury shares contra-equity with no P&L; distributions reduce equity (their tax charge per Sec 29); non-cash distributions at FV with the carrying-amount disproportionate-cost fallback | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 22 whole + Apéndice (txt PAGE 192-201); 22.4-22.5 prints (txt PAGE 193-194); Apéndice 22 worked example (txt PAGE 197-199) (EVID-292) |
| LB-004 | Norma NIIF para las PYMES, Sección 32 Hechos ocurridos después del periodo sobre el que se informa, 32.11: "Si una entidad acuerda distribuir dividendos a los tenedores de sus instrumentos de patrimonio después del final del periodo sobre el que se informa, no reconocerá esos dividendos como un pasivo al final del periodo sobre el que se informa. El importe del dividendo se puede presentar como un componente segregado de ganancias acumuladas al final del periodo sobre el que se informa." | Dividends agreed after the reporting-period end are NOT a liability at the reporting date; the amount may be presented as a segregated component of retained earnings | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 32, párr. 32.11 (txt PAGE 294; EVID-292/296 kin) |
| LB-005 | Norma NIIF para las PYMES, Sección 24 Subvenciones del Gobierno: grant = transfer of resources in return for past or future compliance with conditions; excluded — "las exenciones fiscales, los créditos fiscales por inversiones, las depreciaciones aceleradas y las tasas impositivas reducidas… En la Sección 29… tratamiento contable de los impuestos basados en las ganancias" (benefits arising from tax computations are not Sec 24 grants). 24.3: (a) no future conditions attached → income when the grant is "exigible"; (b) performance conditions → income "cuando se cumplan" the conditions; (c) "si la subvención se recibe en efectivo… antes de cumplir" → liability until the conditions are met. 24.4 measure "al valor razonable del activo recibido o por recibir". Disclosures: nature and amounts, unfulfilled conditions, other forms of government aid. Sección 25 Costos por préstamos: 25.1 scope = interest and other costs per the EIR, finance-lease charges, and FX differences treated as interest; 25.2: "Una entidad reconocerá todos los costos por préstamos como un gasto en resultados del periodo en el que se incurren" | Grants are condition-gated income (or a liability while received-in-advance of condition satisfaction) measured at fair value; tax-benefit "assistance" (fiscal exemptions, investment tax credits, accelerated depreciation, reduced rates) is EXCLUDED from Sec 24 and routes to the Sec 29 income-tax engine. Borrowing costs are ALL expensed as incurred — no capitalization | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 24, párrs. 24.1-24.5 + Sección 25, párrs. 25.1-25.2 (txt PAGE 225-226) (EVID-294) |
| LB-006 | Norma NIIF para las PYMES, Sección 28 Beneficios a los Empleados: four categories — beneficios a corto plazo (due ≤12 months after the service), post-empleo, otros beneficios a largo plazo, beneficios por terminación; 28.3 recognize pasivo net of amounts already paid + gasto unless asset-cost; prepayment → asset only to extent of refund or future reduction. Short-term 28.5-28.9 undiscounted in the service period; accumulating paid absences ("ausencias retribuidas que se acumulan") recognized as service is rendered — liability = "el importe adicional sin descontar que la entidad espera pagar como resultado del derecho no utilizado" (additional UNDISCOUNTED cost of unused rights); non-accumulating absences when the absence occurs; profit-sharing and bonuses when a present obligation + reliable estimate. Post-employment DC 28.10-28.11: fixed contributions to a separate fund, no further obligation → expense as incurred; 28.12 multi-employer/state plans with insufficient information → DC treatment + disclosure of surplus/deficit character; insured = DC unless direct-payment/reinsurance obligation. DB 28.15-28.29: net liability = PV of the obligation − FV of plan assets; 28.17 discount at "tasas de mercado de bonos corporativos de alta calidad" currency and term matched (government bonds where no deep market); 28.16 projected unit credit "si tiene posibilidad de hacerlo sin un costo o esfuerzo desproporcionado" reflecting future salary increases + actuarial assumptions incl. non-vested service; 28.26 obligations accrue even if conditional on future employment (probability affects measurement not existence); 28.19 simplified election when PUC disproportionate: "suponiendo que todos los empleados de la entidad cesen en su empleo en la fecha de presentación de la información e ignorando: (i) la estimación de futuros aumentos salariales. (ii) el servicio futuro. (iii) la posible mortalidad en servicio… (b) sin descontar esa obligación", including vested AND non-vested benefits, assumptions disclosed; independent actuary NOT required, full valuation not annual (roll-forward when key assumptions stable). 28.20-28.21 introductions/changes → expense; curtailments/settlements → gain/loss in result. 28.22 surplus → asset only to extent recoverable (reduced contributions/refunds). 28.23-28.25 cost = net change in the DB liability other than benefits paid and contributions (service cost, interest, plan-asset returns, actuarial gains/losses, intro/curtailment); actuarial gains/losses → "resultados… o… otro resultado integral" as a uniform accounting-policy election. 28.28-28.29 reimbursements: separate asset at FV when virtually certain; expense presentable net. Otros largo plazo 28.27: PV − plan-asset FV, "en su totalidad en el resultado" (no OCI option). Terminación 28.30-28.36: immediate expense (no future benefit); liability at the EARLIER of the non-withdrawable offer (acceptance or restriction in force; communicated termination plan meeting the criteria) and the Sec 21 restructuring recognition date; termination benefits payable ≥12 months after the reporting date → discounted (PV) | Employee benefits: four categories; short-term benefits undiscounted; accumulating absences (vacaciones) accrued at the additional undiscounted cost of unused rights; profit-sharing obligation gate; DC classification (incl. insufficient-information multi-employer/state plans and insured plans); DB net measurement at high-quality corporate-bond discount rates under projected unit credit, or the 28.19 simplified all-terminate-today undiscounted election under disproportionate cost; uniform P&L-or-OCI actuarial-gains policy; reimbursements as separate FV assets; long-term benefits wholly to P&L; termination benefits expensed immediately with the earlier-of recognition trigger and PV beyond twelve months | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 28 whole (txt PAGE 249-263); 28.19 simplified print (txt PAGE 255); 28.24-28.26 prints (txt PAGE 256-257); 28.30-28.36 prints (txt PAGE 258-259) (EVID-295) |
| LB-007 | Guía EY (SECONDARY-ONLY per R29(a); never sole LB): framework-contrast set — full NIIF vs PYMES divergences documented for full-NIIF entities, including the IFRS 16 right-of-use single-lessee lease model (replacing the dual classification for full-NIIF filers) and IAS 23 borrowing-cost capitalization on qualifying assets; PYMES are NOT amended by NIIF 18/19 or IFRS 16 | The documented full-NIIF contrast boundary: IFRS-16 leasing and IAS-23 capitalization are full-NIIF treatments only — never implemented by, or configured onto, the PYMES engines of this file | `sv/sources/33_Guia_NIIF_Sostenibilidad_2024-2025.pdf` | Framework-contrast chapter (EVID-299; EV33 OQ-1) |

## 3. Functional Requirements

### 3.1 Provisions and contingencies (Sección 21)

- **SV-COA-FR-135:** The system shall implement the provision recognition
  gate with all three conditions required together: (a) a *obligación
  presente* (present obligation, legal or constructive) as a result of a
  past event; (b) it is *probable* ("más posible que no" — more likely than
  not) that settling the obligation will require an outflow of resources;
  and (c) a reliable estimate of the amount is possible — and shall NEVER
  recognize a provision without a past-event obligation, specifically
  refusing provisions for future operating losses (which instead indicate
  impairment questions owned by `04_nonfinancial-assets.md` by id).
  (LB-002; EVID-291)
- **SV-COA-FR-136:** The system shall post a recognized provision as a
  liability with the corresponding charge to expense — or to the cost of
  asset when another section requires inclusion in an asset's cost
  (dismantling/site-restoration initial estimates per 17.10(c) are
  `04_nonfinancial-assets.md` by id) — and shall allow charges against a
  provision ONLY for the expenditures for which it was originally
  recognized (*desembolsos para los cuales fue reconocida originalmente*),
  recording each use against the original purpose; expenditures outside
  that purpose post as current-period expense, never against the provision.
  (LB-002; EVID-291)
- **SV-COA-FR-137:** The system shall measure each provision at the best
  estimate of the expenditure required to settle the obligation at the
  reporting date — for a large population of items, the statistically
  weighted expected value; for a single obligation, the most-likely
  outcome with other possible outcomes taken into account — and, when the
  effect of the time value of money is material, at the present value of
  the expenditures discounted at a PRE-TAX rate reflecting the market's
  assessments of the time value of money and the liabilities' specific
  risk, carrying that risk adjustment EITHER in the discount rate OR in
  the estimated cash flows, never in both; expected gains from the
  disposal of assets shall not be netted; each significant class of
  obligation shall be measured separately.
  (LB-002; EVID-291)
- **SV-COA-FR-138:** The system shall remeasure every provision at each
  reporting date on current best estimates, and shall route the unwinding
  of the discount to *costo de financiamiento* (finance cost) of the
  period — never back through the original expense account.
  (LB-002; EVID-291)
- **SV-COA-FR-139:** The system shall recognize a reimbursement for some
  or all of the expenditure required to settle a provision as a SEPARATE
  asset when (and only when) the reimbursement is virtually certain, never
  netting it against the provision, capped at the provision's carrying
  amount; the related provision expense may be presented net of the
  reimbursement in the income statement.
  (LB-002; EVID-291)
- **SV-COA-FR-140:** The system shall recognize a restructuring provision
  ONLY when BOTH elements are recorded: a FORMAL AND DETAILED PLAN whose
  main features are recorded (the main characteristics of the
  plan/program — business activities affected and locations; functions;
  approximate number of employees per function; expenditures by category;
  timing) AND a VALID EXPECTATION in those affected that the entity will
  carry it out (implementation begun, or the plan's main features
  announced) at the reporting date — a mere board commitment, a net-zero
  intention or a budget in preparation alone creates NO provision.
  (LB-002; EVID-291)
- **SV-COA-FR-141:** The system shall implement the *contratos onerosos*
  (onerous contracts) provision: a present obligation from a contract in
  which the unavoidable costs of meeting the obligations exceed the
  economic benefits expected to be received → provision at the LOWER of
  the cost of fulfilling the contract and the penalty for failing to
  fulfill it — detecting onerous leases (both FR-144 tracks) and onerous
  customer contracts (the contract-balance surfaces are
  `06_revenue.md` by filename, consumed never duplicated); idle-capacity
  losses and future operating losses stay excluded under FR-135.
  (LB-002; EVID-291)
- **SV-COA-FR-142:** The system shall implement the contingency rules:
  *pasivos contingentes* (contingent liabilities — possible, or present
  but not probable or not reliably measurable) are NEVER recognized — the
  sole exception being contingent liabilities assumed in a business
  combination (19.19, owned by `07_groups-related-parties.md` by id) — and
  are disclosed unless the probability of outflow is remote; for
  jointly-and-severally-binding obligations the entity's own share
  (reliably estimable + probable) is a provision and the remainder a
  contingent liability; *activos contingentes* (contingent assets) are
  never recognized, disclosed when a probable inflow exists, and
  recognized as an asset only when realization is virtually certain; and
  in the extremely rare case where disclosure can be expected to
  seriously prejudice the dispute's outcome, the system emits the
  prejudicial-disclosure carve-out (nature of the dispute + the fact and
  reason that information is not disclosed).
  (LB-002; EVID-291)
- **SV-COA-FR-143:** The system shall bring *contratos de garantía
  financiera* (financial guarantee contracts) issued to group entities at
  nil or nominal consideration — and gratuitous loan commitments to any
  entity — inside the Sección 21 engine (21.1A): recognized as a provision
  when the FR-135 gate is met, and disclosed per 21.18-21.19 with the
  nature and purpose of the arrangement, the uncertain timing and amount,
  and the maximum potential exposure (the related-party routing is
  `07_groups-related-parties.md` by id).
  (LB-002; EVID-291)

### 3.2 Leases — DUAL model (Sección 20; explicitly NOT IFRS 16)

- **SV-COA-FR-144:** The system shall identify a *arrendamiento* (lease)
  as a contract conveying the right to use a specific asset for a period
  of time in exchange for consideration, INCLUDING in-substance leases —
  the Norma's worked examples (subcontracting arrangements, agreements
  conveying rights to capacity in telecom networks, take-or-pay
  contracts) are leases when they convey a right of use — while service
  contracts without a conveyed right of use remain services, never lease
  records.
  (LB-001; EVID-290)
- **SV-COA-FR-145:** The system shall classify each lease
  *arrendamiento financiero* (finance lease) vs *arrendamiento operativo*
  (operating lease) by whether it transfers substantially all the risks
  and rewards incidental to ownership — recording as classification
  evidence the situations that individually or in combination normally
  indicate financiero (title transfer by end of term; bargain purchase
  option sufficiently certain to be exercised; term covering the major
  part of the asset's economic life; PV of minimum lease payments
  amounting to substantially all of the asset's fair value; specialized
  nature such that only the lessee can use it without major modification)
  and the supporting indicators (lessee bears losses from cancellation or
  residual-value fluctuation; bargain-renewal rents) — with the
  classification DETERMINED AT INCEPTION and reassessed ONLY when the
  lease term is changed by negotiation between the parties, never for
  changed estimates of residual life or option-exercise likelihood.
  (LB-001; EVID-290)
- **SV-COA-FR-146:** The system shall record a lessee's finance lease at
  inception as an asset and a liability at the LOWER of the leased
  asset's fair value and the present value of the minimum lease payments,
  discounted at the interest rate implicit in the lease when practicable
  to determine and otherwise at the lessee's incremental borrowing rate;
  initial direct costs of the lessee are added to the recognized asset.
  (LB-001; EVID-290)
- **SV-COA-FR-147:** The system shall subsequently split a lessee's
  finance-lease minimum payments so that the finance charge reflects a
  constant periodic rate of interest (EIR) on the remaining liability
  balance, and shall depreciate the leased asset under its asset's own
  section (`04_nonfinancial-assets.md` by id) over the SHORTER of the
  useful life and the lease term — unless ownership reasonably certain to
  transfer by the end of the term, in which case over the useful life —
  with contingent rents (non-indexed variable payments) expensed as
  incurred.
  (LB-001; EVID-290)
- **SV-COA-FR-148:** The system shall recognize a lessee's operating-lease
  payments (excluding service components such as insurance or maintenance)
  as an expense on a STRAIGHT-LINE basis over the lease term, with two
  encoded exceptions: (a) another systematic basis when more
  representative of the time pattern of the user's benefit; and (b)
  payments structured to increase in line with expected general inflation
  (based on published indices or statistics) to compensate the lessor for
  expected cost inflation —   which the system recognizes AS INCURRED (the
  20.15(b) worked example: 100.000→146.000 u.m. five-year escalator at
  10% expected inflation → annual expense = amounts payable each year;
  unstructured increases → straight-line 122.000 u.m.).
  (LB-001; EVID-290; 20.15(b) worked example, txt PAGE 174-175)
- **SV-COA-FR-149:** The system shall record a lessor's finance lease as
  the NET INVESTMENT in the lease as a receivable, recognizing finance
  income to reflect a constant periodic rate of return on the
  net investment; for manufacturer-or-dealer lessors the selling result
  is recognized at inception restricted to the market price of the asset
  (no supra-market selling profit), with the remainder recognized as
  finance income over the lease term, and initial direct costs expensed
  at inception (non-dealer lessors include them in the net investment).
  (LB-001; EVID-290)
- **SV-COA-FR-150:** The system shall keep a lessor's operating-leased
  asset on the statement of financial position under its nature class
  (PPE/investment property engines owned by
  `04_nonfinancial-assets.md` by id), recognizing lease income on a
  straight-line basis over the term (or another systematic basis more
  representative of the benefit-consumption pattern), adding initial
  direct costs to the asset's carrying amount and expensing them over the
  term on the same basis, with depreciation under the asset's own
  section.
  (LB-001; EVID-290)
- **SV-COA-FR-151:** The system shall route *venta con arrendamiento en
  retroceso* (sale and leaseback) through the classification engine: (i)
  when the leaseback is financiero, the difference between the sale price
  and the carrying amount is financing in substance — the excess of sale
  proceeds over fair value is deferred and amortized over the lease term
  (never recognized as income at once); (ii) when the leaseback is
  operativo and the transfer is at fair value, the gain or loss on
  disposal is recognized immediately; (iii) when the transfer price is
  BELOW fair value, the pre-compensation difference is deferred and
  amortized (in substance a prepayment of future below-market rents) when
  the shortfall is offset by contractually below-market rent, and
  recognized immediately otherwise; and (iv) proceeds ABOVE fair value in
  excess of the FV-based gain are deferred and amortized over the term.
  (LB-001; EVID-290)
- **SV-COA-FR-152:** The system shall emit the Sección 20 disclosures,
  including the lessee's total future minimum payments under
  non-cancellable operating leases analyzed by maturity band — hasta un
  año · entre uno y cinco años · más de cinco años — and the lessor's
  finance-lease investment maturities; and the lease engine shall carry
  the DUAL classification model ONLY: the IFRS-16 right-of-use
  single-lessee model is a full-NIIF treatment (LB-007 secondary
  contrast, full-NIIF group entities per the `01_framework-policies.md`
  framework flag) and the system shall offer NO configuration path that
  turns it on under the PYMES engine. Two-track note: fiscal
  deductibility of lease payments follows ordinary ISR rules (taxation
  wave by id) — book-vs-fiscal differences route through
  `08_deferred-tax-adoption.md` (T8) by filename.
  (LB-001; LB-007 secondary; EVID-290/299)

### 3.3 Employee benefits (Sección 28)

- **SV-COA-FR-153:** The system shall classify every employee benefit
  into one of four categories — *beneficios a corto plazo* (short-term
  benefits, due to be settled wholly within twelve months of the service
  period), *beneficios post-empleo* (post-employment benefits), *otros
  beneficios a largo plazo* (other long-term benefits) and *beneficios
  por terminación* (termination benefits) — recognizing the liability
  NET of amounts already paid and the corresponding expense as the
  service is rendered (or the asset cost when another section so
  requires), with a prepayment recorded as an asset only to the extent of
  a cash refund right or a reduction in future contributions.
  (LB-006; EVID-295)
- **SV-COA-FR-154:** The system shall recognize short-term employee
  benefits (wages, employer-side statutory contributions, paid leave,
  profit-sharing and bonuses payable within twelve months, non-monetary
  benefits) at the UNDISCOUNTED amount of the benefit expected to be paid
  in exchange for service rendered during the period — no present-value
  measurement for the ≤12-month settlement category.
  (LB-006; EVID-295)
- **SV-COA-FR-155:** The system shall implement the accumulating-absence
  accrual engine for *ausencias retribuidas que se acumulan*
  (accumulating paid absences) — SV *vacaciones* (annual vacation) being
  the operative case: as the employee renders service that increases the
  entitlement to future paid absence, the system accrues the liability at
  the ADDITIONAL UNDISCOUNTED amount the entity expects to pay as a
  result of the UNUSED right accumulated at the reporting date (unused
  entitlement × expected settlement rate, ignoring future absences);
  non-accumulating absences are expensed when the absence occurs.
  **Two-track:** the CT vacation computation (fifteen days + 30%
  surcharge, bases, Art. 188 no-accumulation constraints) is S4's
  statutory engine consumed BY ID from `payroll/04_statutory-benefits.md`
  (SV-PAY-FR-044..049, vacation daily base SV-PAY-FR-047) — this file
  consumes the accrued-right quantum and books the balance-sheet
  liability, NEVER re-deriving the labor computation, and the book
  accrual of unused rights stands regardless of the CT prohibition on
  cash-compensating vacations (payout mechanics stay in S4).
  (LB-006; EVID-295; via payroll/04 SV-PAY-FR-044..049 by id)
- **SV-COA-FR-156:** The system shall recognize profit-sharing and bonus
  obligations only when the obligation GATE is satisfied: the entity has
  a PRESENT obligation from past service (a formal plan or announced
  formula, or a constructive obligation from past practice) AND a
  reliable estimate is possible — a mere intention or a plan under exit
  consideration creates no liability; amounts payable more than twelve
  months after the service period route to the long-term-benefit rules
  (FR-162).
  (LB-006; EVID-295)
- **SV-COA-FR-157:** The system shall book the statutory social-security
  and pension contributions (ISSS health, SIP/AFP pension cotizaciones
  and the public-institute schemes) DC-STYLE: employer contributions as a
  period expense + payable when incurred, with NO defined-benefit
  obligation and NO plan-asset measurement for the individually funded
  SIP/AFP accounts; every rate, cap, base and split is consumed BY ID
  from the S4 statutory engine (`payroll/05_social-security-contributions.md`
  SV-PAY-FR-063..085 with its `ss_contributions.csv` sidecar; the IBC
  classification matrix `payroll/01_salary-model.md` SV-PAY-FR-004) —
  never re-derived, never overridden here.
  (LB-006; EVID-295; via payroll/05 SV-PAY-FR-063..085 and payroll/01
  SV-PAY-FR-004 by id)
- **SV-COA-FR-158:** The system shall classify post-employment schemes
  *aportaciones de planta de beneficios definidos* (defined contribution,
  DC) vs *beneficios definidos* (defined benefit, DB): DC = no legal or
  constructive obligation beyond fixed, determinable contributions to a
  separate entity/fund → period expense as incurred, no further
  liability; multi-employer or state-administered plans where
  insufficient information prevents identifying the obligation share →
  treated as DC with disclosure of the available surplus/deficit and
  funding character; insured plans = DC unless a direct-payment
  obligation remains (premiums unpaid at term or retirement) or
  reinsurance retains significant risk — then DB.
  (LB-006; EVID-295)
- **SV-COA-FR-159:** The system shall measure defined-benefit obligations
  as the NET of the present value of the obligation minus the fair value
  of plan assets, discounted at market rates of HIGH-QUALITY corporate
  bonds consistent with the currency and estimated term of the
  obligation (government-bond rates where no deep corporate market),
  measured under the PROJECTED UNIT CREDIT method reflecting estimated
  future salary increases and actuarial assumptions (employee turnover,
  mortality including in-service, medical cost trend) over both vested
  and non-vested service — the obligation accruing even where benefits
  are conditional on future employment, probability affecting
  measurement not existence — UNLESS disproportionate cost or effort is
  registered (the 2.28-2.30 relief registry, `01_framework-policies.md`
  SV-COA-FR-012 by id), in which case the entity may elect the 28.19
  SIMPLIFIED measurement: assume ALL employees terminate at the
  reporting date, IGNORING future salary increases, future service and
  possible in-service mortality (post-service mortality/life expectancy
  still counts), with NO DISCOUNTING, still including both vested and
  non-vested benefits, and disclosing the assumptions used; an
  independent actuary is NOT required and a full actuarial valuation is
  NOT required annually — between full valuations a roll-forward of the
  prior measurement (adjusted for demographic change) suffices when key
  assumptions are not significantly different.
  (LB-006; EVID-295; 28.19 print, txt PAGE 255)
- **SV-COA-FR-160:** The system shall account for DB events and cost as
  follows: plan introductions or changes → the resulting
  increase/decrease of the DB liability recognized as current-period
  expense/income; curtailments and settlements → the resulting gain or
  loss in current-period result; a plan SURPLUS recorded as a DB asset
  only to the extent recoverable through reduced future contributions or
  refunds; the period's DB cost = the NET change in the DB liability
  other than benefits paid to employees and employer contributions —
  comprising service cost, interest on the obligation, plan-asset
  returns, actuarial gains and losses, and introduction/curtailment
  effects — recognized as expense (or partly as asset cost when another
  section requires) and presentable net of reimbursements; reimbursement
  rights when virtually certain are a SEPARATE asset measured at fair
  value.
  (LB-006; EVID-295)
- **SV-COA-FR-161:** The system shall implement the actuarial-gains
  policy election: ALL actuarial gains and losses of the period are
  recognized either entirely in PROFIT OR LOSS or entirely in OTHER
  COMPREHENSIVE INCOME — an accounting-policy election applied UNIFORMLY
  to every defined-benefit plan and every actuarial gain and loss of the
  entity (any switch governed by the Sección 10 policy-change rules,
  `01_framework-policies.md` SV-COA-FR-014..016 by id), with
  OCI-routed amounts presented in the *estado del resultado integral*.
  (LB-006; EVID-295)
- **SV-COA-FR-162:** The system shall measure other long-term employee
  benefits (long-service leave and sabbaticals, long-term disability
  benefits, long-term service benefits, profit-sharing and incentives
  payable beyond twelve months of period close, deferred benefits) as the
  present value of the defined-benefit-style obligation minus the fair
  value of any plan assets, recognizing the ENTIRE net-period change in
  profit or loss — with NO OCI option available on this category.
  (LB-006; EVID-295)
- **SV-COA-FR-163:** The system shall recognize termination benefits as
  EXPENSE IMMEDIATELY when recognized (they provide no future economic
  benefit), recording the liability at the EARLIER of: (a) the first
  date the offer can no longer be withdrawn — for offers in exchange for
  the employee's termination decision, the earlier of ACCEPTANCE and the
  date a legal, regulatory or contractual RESTRICTION on withdrawal
  enters force (the offer date itself when the restriction pre-exists);
  for terminations from the entity's own decision, the COMMUNICATED plan
  meeting the criteria (significant plan changes improbable; the number
  and classes of affected employees identified; per-employee termination
  benefits estimable; execution due to begin without undue delay) — and
  (b) the recognition date of the linked Sección 21 restructuring costs
  involving termination benefits (FR-140); knock-on reductions to other
  benefit obligations are accounted for together. **Two-track:** the CT
  *indemnización* (termination indemnity) statutory computation is S4's
  (`payroll/07_contracts-termination.md` SV-PAY-FR-105..107 BY ID —
  FR-105 indefinite quantum, FR-106 4×SMM cap, FR-107 plazo variant) —
  this file's recognition
  TIMING is independent of the fiscal/labor payout calendar.
  (LB-006; EVID-295; via payroll/07 SV-PAY-FR-105..107 by id)
- **SV-COA-FR-164:** The system shall discount termination benefits
  expected to be settled NO EARLIER than twelve months after the
  reporting date, presenting the liability at present value with
  remeasurement each reporting date; benefits settled within twelve
  months remain undiscounted under FR-154.
  (LB-006; EVID-295)

### 3.4 Equity (Sección 22 + 32.11 + the CC distribution-capacity overlay)

- **SV-COA-FR-165:** The system shall classify a financial instrument as
  a financial liability or as equity according to the SUBSTANCE of the
  contractual arrangement, not simply its legal form, and the Sección
  11/22 definitions: unless the entity has an UNCONDITIONAL right to
  avoid delivering cash or another financial asset to settle a
  contractual obligation, the instrument is a financial liability — the
  sole carve-out being the puttable-class equity test of FR-166; the
  financial-instrument measurement engines (amortized cost, FV, EIR) are
  `03_financial-instruments-fx.md` by id.
  (LB-003; EVID-292)
- **SV-COA-FR-166:** The system shall classify an *instrumento con opción
  de venta* (puttable instrument — the holder may require the issuer to
  redeem it for cash or another financial asset, including automatic
  redemption on an uncertain future event or the holder's death or
  retirement) as EQUITY only when ALL FIVE conditions are recorded as
  satisfied: (i) it entitles the holder to a PROPORTIONAL share of the
  entity's net assets on liquidation; (ii) it belongs to the class of
  instruments SUBORDINATE to all other classes; (iii) ALL instruments in
  that most-subordinate class have IDENTICAL characteristics; (iv) apart
  from the repurchase/redemption obligation itself, the instrument
  creates no other contractual obligation to deliver cash or another
  financial asset, nor to exchange financial assets or liabilities on
  potentially unfavorable terms, and it is not a contract settleable in
  the entity's own equity instruments; and (v) the instrument's total
  expected cash flows over its life are based SUBSTANTIALLY on the
  results, the change in recognized net assets, or the change in fair
  value of recognized and unrecognized net assets — failing ANY
  condition, it is a liability; instruments whose only obligation is a
  proportional share of net assets AT liquidation are equity
  (22.4(b)).
  (LB-003; EVID-292; 22.4 print, txt PAGE 193-194)
- **SV-COA-FR-167:** The system shall implement the Norma's
  liability-preference examples as classification outcomes: (a) a
  liquidation distribution subject to a MAXIMUM amount (ceiling) →
  liability; (b) a puttable instrument whose redemption amount on
  exercise is measured on a basis OTHER than this Norma (e.g., local
  GAAP) → liability; (c) an instrument obliging payments before
  liquidation, such as a *dividendo obligatorio* (mandatory dividend) →
  liability; (d) a puttable instrument classified as equity in a
  subsidiary's FS → LIABILITY in the controladora's FS; and (e) a
  *acción preferente* (preference share) stipulating MANDATORY REDEMPTION
  by the issuer at a fixed or determinable amount on/at a fixed or
  determinable date, or giving the holder the right to require redemption
  from a particular date → liability.
  (LB-003; EVID-292)
- **SV-COA-FR-168:** The system shall classify interests in *cooperativas*
  (cooperatives) or similar partnership interests as EQUITY when the
  holder has an UNCONDITIONAL right to refuse redemption, or when local
  law or regulation PROHIBITS redemption — either basis recorded on the
  instrument's classification record.
  (LB-003; EVID-292)
- **SV-COA-FR-169:** The system shall record equity issuance as follows:
  equity issued BEFORE cash is received → presented as a contra-equity
  *importe por cobrar* (amount receivable), NOT as an asset — UNLESS
  local law or regulation prohibits that presentation (the 3rd-edition
  local-law override), in which case the alternative presentation
  prescribed by local law applies with the override basis recorded (CC
  Art. 29 — social capital must sit on the liability side with patrimony
  of at least equal value — consumed BY ID from
  `commercial-legal/04_society-types.md` SV-CML-FR-049; the
  assets-≥-capital warning state is that file's engine, never restated
  here); and shares subscribed but NOT issued and NOT paid → NO increase
  in equity until the deed-regime issuance and payment conditions
  complete.
  (LB-003; EVID-292; via commercial-legal/04 SV-CML-FR-049 by id)
- **SV-COA-FR-170:** The system shall measure an equity issuance at the
  FAIR VALUE of the resources received or receivable, NET of transaction
  costs (discounted to present value when settlement is deferred and the
  financing effect is material, at a market rate); transaction costs of
  EQUITY transactions are deducted from EQUITY — never routed through
  profit or loss.
  (LB-003; EVID-292)
- **SV-COA-FR-171:** The system shall leave the presentation split
  between capital at *valor nominal* (par) and the excess to the issuing
  price (prima/superávit de aportación) — and any reclassification
  between equity classes — to LOCAL LAW and the entity's *escritura
  social / estatutos* (social deed and bylaws; CC regime), encoding it as
  per-entity presentation configuration over the equity account classes
  (the class architecture and per-class disclosures — rights,
  restrictions, par values — are `02_coa-structure.md` by id), with no
  NIIF-mandated par/excess mechanics invented.
  (LB-003; EVID-292)
- **SV-COA-FR-172:** The system shall record capitalization of retained
  earnings (*dividendos en acciones* / stock dividends), share splits and
  consolidations with NO change in the TOTAL equity amount — only
  reclassifications between equity classes and mechanical per-share par
  adjustments, per the applicable local-law routing.
  (LB-003; EVID-292)
- **SV-COA-FR-173:** The system shall split *deuda convertible*
  (convertible debt) and other composite instruments LIABILITY-FIRST at
  issuance: FIRST measure the liability component at the fair value of a
  similar NON-convertible instrument (present value at its market rate),
  assign the RESIDUAL of the total issuance proceeds to equity, allocate
  transaction costs between the components pro-rata on fair value, and
  NEVER re-split the instrument after issuance (conversion or settlement
  extinguishes the liability component on its own book terms; the equity
  component persists) — calibrated to the Apéndice worked example: 500
  bonds at par 100 u.m., five years, 4% coupon, 6% market rate for
  similar non-convertible debt → liability component 45.788 u.m. (PV of
  principal 37.363 + PV of interest 8.425), residual equity 4.212 u.m.;
  *conversión de deuda en capital* (debt-for-equity conversions, 22.15A-C)
  are measured at fair value of the equity instruments issued, with
  linked modifications split and in-substance distributions/contributions
  between entities under the same ultimate control excluded from these
  mechanics.
  (LB-003; EVID-292; Apéndice 22 worked example, txt PAGE 197-199)
- **SV-COA-FR-174:** The system shall record *acciones en tesorería*
  (treasury shares) as a deduction from equity at the fair value of the
  consideration paid, and shall post NO profit or loss on the purchase,
  sale, issue or cancellation of the entity's own equity instruments —
  all differences remaining within equity, with the carrying amount and
  the reasons for holding treasury shares disclosed.
  (LB-003; EVID-292)
- **SV-COA-FR-175:** The system shall book distributions to owners as a
  reduction of EQUITY when declared (never routed through P&L), with
  their related income taxes accounted per Sección 29 — the 29.33
  dividend-withholding-charged-to-equity mechanics and the Ley ISR 5%
  interplay are `08_deferred-tax-adoption.md` (T8) and
  `taxation/05` by filename, never re-derived here; dividends AGREED
  after the reporting-period end shall NOT be recognized as a liability
  at the reporting date — the amount MAY be presented as a segregated
  component of *ganancias acumuladas* (retained earnings) at the
  reporting date (32.11; the statement-of-changes-in-equity presentation
  surfaces are `02_coa-structure.md` by id; the events-after-period
  surfaces are T7's `07_groups-related-parties.md` by filename).
  (LB-003; LB-004; EVID-292)
- **SV-COA-FR-176:** The system shall record a NON-CASH distribution
  (distributing assets other than cash) as a liability at the FAIR VALUE
  of the assets to be distributed — falling back to their CARRYING
  amount only when fair value cannot be measured without disproportionate
  cost (the 2.28-2.30 relief registry, `01_framework-policies.md`
  SV-COA-FR-012 by id) — remeasuring the liability through EQUITY as the
  distribution approaches, and recognizing in PROFIT OR LOSS at
  settlement the difference between the carrying amount of the assets
  distributed and the recorded liability (asset-derecognition mechanics
  per the asset's own section, `04_nonfinancial-assets.md` by id);
  distributions between entities under the same ultimate control
  (in-substance distributions/contributions) are excluded from these
  mechanics.
  (LB-003; EVID-292)
- **SV-COA-FR-177:** The system shall implement the Código de Comercio
  Arts. 37-38 distribution-capacity overlay as a LEGAL OVERLAY track
  (SOQ-49): distribution capacity under the CC is measured against
  *utilidades realmente obtenidas, conforme al balance general y estado
  de pérdidas y ganancias* (profits really obtained per the balance sheet
  and P&L) with any CAPITAL LOSS restored (or capital reduced per CC Art.
  444 ordinal 7) BEFORE any distribution — a realized-profit concept
  ABSENT from NIIF comprehensive income; the system shall therefore carry
  distribution capacity as a SEPARATE statutory ledger field maintained
  under the CC/estatutos discipline, consumed BY ID from
  `commercial-legal/04_society-types.md` (dividend ceiling SV-CML-FR-053,
  solidary restitution exposure included; reserva legal mechanics
  SV-CML-FR-054..056), kin to the `taxation/05` earnings register and
  the 29.33 withholding charge by filename — and shall NEVER auto-derive
  the distributable amount from NIIF equity, comprehensive income or
  retained-earnings balances; NIIF amounts never substitute the CC
  ceiling, and a ceiling breach triggers the SV-CML-FR-053 restitution
  flag without touching the book equity records.
  (LB-003; EVID-292; SOQ-49; via commercial-legal/04 SV-CML-FR-053/054..056
  by id)

### 3.5 Government grants (Sección 24)

- **SV-COA-FR-178:** The system shall scope the *subvención del gobierno*
  (government grant) engine to resource transfers against past or future
  compliance conditions, and shall EXCLUDE government assistance arising
  from tax computations — *exenciones fiscales* (fiscal exemptions),
  *créditos fiscales por inversiones* (investment tax credits),
  *depreciaciones aceleradas* (accelerated depreciation) and *tasas
  impositivas reducidas* (reduced rates) — whose accounting belongs to
  the Sección 29 income-tax engine (`08_deferred-tax-adoption.md`, T8, by
  filename); specifically, the ZF/LSI/DPA exemption ladders are TAX
  benefits owned by the special-regimes wave BY ID
  (`special-regimes/02_zf-exemption-schedules.md` SV-SPE-FR-023 exemption-row
  engine and its D15 dated schedules) — this file shall book NO grant
  income and NO grant liability for them, and no other fiscal exemption.
  (LB-005; EVID-294; via special-regimes/02 SV-SPE-FR-023 by id)
- **SV-COA-FR-179:** The system shall recognize grant income strictly
  condition-gated: (a) a grant imposing NO future performance conditions
  → income when the right to receive it becomes *exigible* (receivable);
  (b) a grant attaching performance conditions → income when the
  conditions are MET; and (c) consideration received BEFORE the attached
  conditions are met → a LIABILITY until they are satisfied (with the
  repayment duty restored if conditions are later breached).
  (LB-005; EVID-294)
- **SV-COA-FR-180:** The system shall measure a government grant at the
  FAIR VALUE of the asset received or receivable, and shall emit the
  Sec 24 disclosures: the nature and extent (amounts) of the grant
  programs benefiting the entity, any unfulfilled or breached conditions
  attached, and other forms of government aid received.
  (LB-005; EVID-294)

### 3.6 Borrowing costs (Sección 25)

- **SV-COA-FR-181:** The system shall recognize ALL *costos por
  préstamos* (borrowing costs — interest and other costs per the
  effective interest rate, finance-lease charges from the FR-149 engine,
  and exchange differences treated as interest characteristics per the
  FX engines owned by `03_financial-instruments-fx.md` by id) as an
  EXPENSE of the period in which they are incurred ("Una entidad
  reconocerá todos los costos por préstamos como un gasto en resultados
  del periodo en el que se incurren", 25.2), providing NO
  capitalization posting path and NO capitalization configuration on the
  PYMES engine (contrast: the IAS 23 qualifying-asset capitalization is
  a full-NIIF treatment, LB-007 secondary contrast — full-NIIF group
  entities only); fiscal ISR interest treatment (deductibility,
  withholding) is taxation's by id — book-vs-fiscal differences route
  through `08_deferred-tax-adoption.md` (T8) by filename.
  (LB-005; LB-007 secondary; EVID-294)

## 4. Data Model

Layer semantics: all entities are Odoo-native (account/account.move
posting engines, hr surfaces, dated config rows) — wave default `odoo`
(see §5). The model records the company's OWN book measurements; fiscal
engines (payroll statutory, ISR, ZF/LSI/DPA) are referenced by FR id and
never duplicated here. No printed data table in this file warrants a CSV
sidecar (the maturity bands, categories and classification flags are
small fixed config sets; default none per plan).

**Provisions (l10n_sv_chart.provision):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.provision | kind | select | restructuring · onerous_contract · warranty · dismantling_17_10c · litigation · group_guarantee_21_1A · other | FR-135..143 |
| l10n_sv_chart.provision | gate_present_obligation · gate_probable · gate_reliable_estimate | boolean + basis text | all three required (21.4); no-past-event block for future-loss cases | FR-135 |
| l10n_sv_chart.provision | charge_target | select | expense · asset_cost (asset link when another section requires) | FR-136 |
| l10n_sv_chart.provision | use_line | one2many | expenditure rows, each validated against the ORIGINAL purpose | FR-136 |
| l10n_sv_chart.provision | best_estimate_basis | select | weighted_expected_value · most_likely (other outcomes recorded) | FR-137 |
| l10n_sv_chart.provision | pv_flag · pretax_market_rate · risk_in | boolean · monetary(rate) · select rate · cash_flows (never both) | PV when time value material (21.8-21.9) | FR-137 |
| l10n_sv_chart.provision | unwind_line | one2many | per-period unwinding → finance-cost account | FR-138 |
| l10n_sv_chart.provision | reimbursement | m2o l10n_sv_chart.reimbursement | virtually-certain flag, separate asset, ≤ provision cap, net-presentation option | FR-139 |
| l10n_sv_chart.provision | restructuring_plan | json/text | activities/locations/functions, headcount per function, expenditures by category, timing + valid_expectation basis (begun/announced) | FR-140 |
| l10n_sv_chart.provision | onerous_measure | monetary/computed | lower of fulfilment cost and penalty | FR-141 |
| l10n_sv_chart.contingency | kind · outflow_probability | select contingent_liability · contingent_asset / remote · possible · probable · virtually_certain | never recognized; disclosed unless remote (liabilities) / if probable (assets); prejudicial carve-out flag | FR-142 |
| l10n_sv_chart.provision | guarantee_scope_21_1A | boolean + group-entity link | gratuitous financial guarantee / loan commitment; nature/purpose/uncertainty/maximum disclosure feed (07 by id) | FR-143 |

**Leases (l10n_sv_chart.lease):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.lease | party | select | lessee · lessor | FR-144..152 |
| l10n_sv_chart.lease | classification | select | financiero · operativo | FR-145 |
| l10n_sv_chart.lease | classification_evidence | flags/records | five situations + indicators, snapshotted at inception | FR-145 |
| l10n_sv_chart.lease | inception_date · reassessment_event | date · event rows | reassessment ONLY on negotiated term change | FR-145 |
| l10n_sv_chart.lease | lessee_initial | computed | lower of FV and PV of minimum payments; rate: implicit · incremental_borrowing; direct costs added | FR-146 |
| l10n_sv_chart.lease | eir_schedule · depreciation_rule | schedule · select | constant-periodic finance charge; shorter_of (life vs term) unless ownership-transfer-certain flag; contingent rents expensed | FR-147 |
| l10n_sv_chart.lease | operating_mode | select | straight_line · systematic_representative · inflation_indexed_as_incurred (20.15(b)) | FR-148 |
| l10n_sv_chart.lease | lessor_net_investment · manufacturer_dealer | schedule · boolean | constant periodic return; market-price-capped selling result; dealer direct costs expensed | FR-149 |
| l10n_sv_chart.lease | sale_leaseback_variant | select | financing_excess_deferred · operativo_fv_recognized · below_fv_deferred_offset · above_fv_deferred | FR-151 |
| l10n_sv_chart.lease | maturity_bands | computed/disclosure feed | ≤1y · 1-5y · >5y on non-cancellable minimums | FR-152 |

**Employee benefits (l10n_sv_chart.benefit_plan + hr accrual surfaces):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.benefit_plan | category | select | corto_plazo · post_empleo · largo_plazo · terminacion | FR-153 |
| l10n_sv_chart.benefit_plan | plan_type | select | dc · db · multi_employer_insufficient_info_dc · insured_dc (direct-payment flag flips to DB) | FR-157, FR-158 |
| l10n_sv_chart.benefit_plan | statutory_link | config | ISSS/SIP consumed from payroll/05 SV-PAY-FR-063..085 by id (rates/caps never copied) | FR-157 |
| l10n_sv_chart.benefit_plan | db_measurement | select | projected_unit_credit · simplified_28_19 | FR-159 |
| l10n_sv_chart.benefit_plan | db_relief_ref | m2o disproportionate-cost use | 28.19 election requires a 2.28-2.30 registry row (01 SV-COA-FR-012 by id) | FR-159 |
| l10n_sv_chart.benefit_plan | discount_rate · rate_basis | monetary(rate) · select | high-quality corporate bonds (currency/term matched) · government_no_deep_market | FR-159 |
| l10n_sv_chart.benefit_plan | actuarial_gains_policy | select | profit_or_loss · oci (UNIFORM across all plans; policy-change rules per 01 by id) | FR-161 |
| l10n_sv_chart.benefit_plan | valuation_mode | select | full_valuation · roll_forward (key assumptions stable) | FR-159 |
| hr leave/accrual surface | vacation_unused_rights | monetary(computed) | additional UNDISCOUNTED cost of unused rights; quantum consumed from payroll/04 SV-PAY-FR-044..049 by id | FR-155 |
| l10n_sv_chart.termination_benefit | trigger | select | acceptance · restriction_in_force · communicated_plan (criteria recorded) · restructuring_recognition (FR-140 link) — EARLIER of the offer track and the restructuring date | FR-163 |
| l10n_sv_chart.termination_benefit | settlement_horizon | select | ≤12m_undiscounted · >12m_pv (remeasured) | FR-164 |
| l10n_sv_chart.benefit_plan | profit_sharing_gate | flags | present obligation (plan/formula/practice) + reliable estimate | FR-156 |

**Equity (equity instrument + distribution records):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.equity_instrument | classification | select | equity · financial_liability (substance test) | FR-165 |
| l10n_sv_chart.equity_instrument | puttable_checklist | 5 booleans + result | conditions (i)-(v) ALL required; 22.4(b) at-liquidation-only class | FR-166 |
| l10n_sv_chart.equity_instrument | liability_preference_case | select | liquidation_ceiling · non_norma_measured_redemption · mandatory_dividend · puttable_in_subsidiary · mandatory_redeemable_preference | FR-167 |
| l10n_sv_chart.equity_instrument | cooperative_basis | select | unconditional_refusal · local_law_prohibition | FR-168 |
| l10n_sv_chart.equity_instrument | issued_unpaid_receivable | boolean + basis | contra-equity receivable; local-law override basis when prohibited (SV-CML-FR-049 by id) | FR-169 |
| l10n_sv_chart.equity_instrument | measurement | computed | FV of resources net of transaction costs; PV when deferred-material | FR-170 |
| l10n_sv_chart.equity_instrument | par_excess_presentation | config | per CC/escritura/estatutos (local law decides; 02 by id for class surface) | FR-171 |
| l10n_sv_chart.equity_event | kind | select | stock_dividend_capitalization · split · consolidation (no total-equity change) · treasury_buyback · treasury_redisposal (no P&L) | FR-172, FR-174 |
| l10n_sv_chart.convertible_split | liability_fv · residual_equity · cost_allocation | computed | liability-first at similar non-convertible FV; residual; pro-rata costs; NO-resplit flag; worked-example calibration | FR-173 |
| l10n_sv_chart.distribution | declared_on · amount · equity_reduction | date · monetary · move link | reduces equity at declaration; tax charge = 08 by filename | FR-175 |
| l10n_sv_chart.distribution | post_period_declaration | boolean | 32.11: not a liability at reporting date; optional segregated retained-earnings presentation (02 by id) | FR-175 |
| l10n_sv_chart.distribution | noncash_measure | select | fv · carrying_fallback (relief-registry link, 01 by id); remeasure-through-equity; settlement difference → P&L | FR-176 |
| l10n_sv_chart.distribution_capacity | distributable_ceiling · basis · capital_loss_restored_gate | monetary · config · checkpoint | CC Arts. 37-38 realized-balance track consumed from SV-CML-FR-053 by id; NEVER derived from NIIF equity (SOQ-49); restitution flag | FR-177 |

**Grants + borrowing costs:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.grant | condition_state | select | unconditional_exigible · conditions_pending (liability) · conditions_met (income) · breached (repayable) | FR-179 |
| l10n_sv_chart.grant | fv_measure · disclosure_feed | monetary · link | FV of asset received/receivable; nature/amounts, unfulfilled conditions, other aid | FR-180 |
| l10n_sv_chart.grant | fiscal_benefit_exclusion | boolean/config | ZF/LSI/DPA rows NEVER create grant records (special-regimes/02 by id) | FR-178 |
| res.company (engine config) | borrowing_cost_capitalization | absent (guard) | NO capitalization path/config ships; expense-only routing is the hard encoding | FR-181 |

## 5. Odoo Mapping

Layer semantics for this wave: the chart-of-accounts engines are
Odoo-native (account.account templates, account.move posting and
scheduling engines, hr accrual surfaces, res.company config) — every FR
maps `odoo`; no SaaS rows are introduced because none of these FRs touch
DTE generation/transmission (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Odoo 17+ native
leases (account.move long-term contract entries + automatic deferred
entries) fit the finance-lease side of the DUAL model; operating leases
run on scheduled expense entries; benefit accruals build on
hr.holidays/hr.payslip-adjacent accrual records feeding account.move.
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-135 | odoo | l10n_sv_chart.provision | gate fields | three-gate validation; no-past-event block; future operating losses → impairment flag (04 by id) |
| FR-136 | odoo | l10n_sv_chart.provision (+account.move) | charge_target · use_line | expense or asset-cost posting; original-purpose-only charges |
| FR-137 | odoo | l10n_sv_chart.provision | best_estimate · pv fields | pre-tax market rate; risk in rate XOR cash flows; no disposal-gain netting; per-significant-class |
| FR-138 | odoo | l10n_sv_chart.provision | unwind_line | remeasure each date; unwinding → finance cost account |
| FR-139 | odoo | l10n_sv_chart.reimbursement | separate-asset link | virtually certain; ≤ provision; net presentation option |
| FR-140 | odoo | l10n_sv_chart.provision | restructuring_plan | formal detailed plan + valid expectation; commitment alone rejected |
| FR-141 | odoo | l10n_sv_chart.provision | onerous_measure | lower of fulfil/penalty; leases + customer contracts (06 by filename) |
| FR-142 | odoo | l10n_sv_chart.contingency | register + disclosure feed | disclosed unless remote / if probable; 19.19 exception = 07 by id; prejudicial carve-out |
| FR-143 | odoo | l10n_sv_chart.provision | guarantee_scope_21_1A | gratuitous group guarantees; nature/purpose/uncertainty/maximum (07 by id) |
| FR-144 | odoo | l10n_sv_chart.lease | identification fields | in-substance leases (telecom capacity, take-or-pay, subcontracting); services excluded |
| FR-145 | odoo | l10n_sv_chart.lease | classification + evidence | criteria + indicators snapshot at inception; reassess on negotiated term change only |
| FR-146 | odoo | l10n_sv_chart.lease + account.move | lessee_initial | lower(FV, PV minimums); implicit else incremental rate; direct costs added |
| FR-147 | odoo | l10n_sv_chart.lease + account.move | eir_schedule + depreciation | constant-periodic charge; shorter-of rule + ownership flag; contingent rents expensed |
| FR-148 | odoo | l10n_sv_chart.lease + account.move | operating_mode | straight-line; systematic alternative; inflation-indexed → as-incurred (20.15(b)) |
| FR-149 | odoo | l10n_sv_chart.lease + account.move | net_investment | manufacturer-dealer split; dealer direct costs expensed |
| FR-150 | odoo | account.asset surface (04 by id) + account.move | lessor operating | by-nature class retention; straight-line income; direct costs amortized |
| FR-151 | odoo | l10n_sv_chart.lease | sale_leaseback_variant | four variant routings per 20.31-20.34 |
| FR-152 | odoo | report layer (l10n_sv_chart) | maturity_bands | ≤1y/1-5y/>5y; NOT-IFRS-16 guard (no config path); ISR deductibility = taxation by id; bridge = 08 by filename |
| FR-153 | odoo | l10n_sv_chart.benefit_plan | category | four categories; net-of-paid recognition; prepayment asset cap |
| FR-154 | odoo | l10n_sv_chart.benefit_plan + account.move | short-term accrual | undiscounted ≤12m |
| FR-155 | odoo | hr leave/accrual surface + account.move | vacation_unused_rights | additional UNDISCOUNTED unused-right cost; quantum from payroll/04 SV-PAY-FR-044..049 by id, never re-derived |
| FR-156 | odoo | l10n_sv_chart.benefit_plan | profit_sharing_gate | present obligation + reliable estimate; >12m → FR-162 rules |
| FR-157 | odoo | l10n_sv_chart.benefit_plan + account.move | statutory DC booking | ISSS/SIP via payroll/05 SV-PAY-FR-063..085 + payroll/01 SV-PAY-FR-004 by id; no DB liability for individually funded SIP |
| FR-158 | odoo | l10n_sv_chart.benefit_plan | plan_type | DC/DB; insufficient-info multi-employer/state → DC + disclose; insured direct-payment flip |
| FR-159 | odoo | l10n_sv_chart.benefit_plan | db_measurement | PUC or 28.19 simplified (relief-registry gated); high-quality corporate-bond discount; roll-forward mode |
| FR-160 | odoo | l10n_sv_chart.benefit_plan + account.move | db events/cost | intro/curtailment; surplus asset cap; net-change cost; reimbursement separate FV asset |
| FR-161 | odoo | l10n_sv_chart.benefit_plan | actuarial_gains_policy | P&L or OCI uniform election; switch = policy change (01 by id); OCI in ERI |
| FR-162 | odoo | l10n_sv_chart.benefit_plan + account.move | long-term rules | PV − plan assets; all-P&L; no OCI option |
| FR-163 | odoo | l10n_sv_chart.termination_benefit | trigger | earlier-of offer/restriction/communicated-plan vs restructuring date; CT indemnización = payroll/07 SV-PAY-FR-105..107 by id |
| FR-164 | odoo | l10n_sv_chart.termination_benefit | settlement_horizon | ≥12m → PV remeasured; ≤12m undiscounted |
| FR-165 | odoo | l10n_sv_chart.equity_instrument | classification | substance test; measurement engines = 03 by id |
| FR-166 | odoo | l10n_sv_chart.equity_instrument | puttable_checklist | five conditions ALL; 22.4(b) at-liquidation class |
| FR-167 | odoo | l10n_sv_chart.equity_instrument | liability_preference_case | five printed examples incl. mandatory-redeemable preference |
| FR-168 | odoo | l10n_sv_chart.equity_instrument | cooperative_basis | refusal right or local-law prohibition |
| FR-169 | odoo | l10n_sv_chart.equity_instrument | issued_unpaid_receivable | contra-equity receivable; local-law override recorded (SV-CML-FR-049 by id); subscribed-unpaid no equity |
| FR-170 | odoo | l10n_sv_chart.equity_instrument | measurement | FV net of costs; PV deferred-material; equity-only cost deduction |
| FR-171 | odoo | l10n_sv_chart.equity_instrument + account.account | par_excess_presentation | CC/escritura presentation config; class surface = 02 by id |
| FR-172 | odoo | l10n_sv_chart.equity_event | no-total-change kinds | stock dividends/splits reclassify only |
| FR-173 | odoo | l10n_sv_chart.convertible_split | liability-first split | 45.788/4.212 calibration; pro-rata costs; no re-split; 22.15A-C debt-for-equity |
| FR-174 | odoo | l10n_sv_chart.equity_event | treasury | contra-equity at FV; no P&L anywhere |
| FR-175 | odoo | l10n_sv_chart.distribution + account.move | declaration + 32.11 flag | equity reduction at declaration; tax charge = 08 by filename; post-period dividends segregated, not liability |
| FR-176 | odoo | l10n_sv_chart.distribution | noncash_measure | FV (carrying fallback via relief registry); remeasure through equity; settlement diff → P&L |
| FR-177 | odoo | l10n_sv_chart.distribution_capacity | CC ceiling field | realized-balance track (SV-CML-FR-053/054..056 by id); NEVER derived from NIIF equity (SOQ-49); kin taxation/05 by filename |
| FR-178 | odoo | l10n_sv_chart.grant | fiscal exclusion | tax-computation benefits out of scope; ZF/LSI/DPA = SV-SPE-FR-023 by id |
| FR-179 | odoo | l10n_sv_chart.grant + account.move | condition_state | exigible / met / advance-liability / breached-repay |
| FR-180 | odoo | l10n_sv_chart.grant | fv + disclosures | nature/amounts, unfulfilled conditions, other aid |
| FR-181 | odoo | account.move engine + res.company guard | expense-only routing | ALL borrowing costs expensed (25.2 verbatim); NO capitalization config ships; contrast IAS 23 = full-NIIF only |

Version-regime notes (D12/D15): the NIIF edition is a DATED regime row —
3rd edition (Feb-2025) applies to annual periods beginning 2027-01-01,
early adoption permitted (A1; `01_framework-policies.md` LB-002); SV
2025-2027 books may still run under the 2nd (2015) edition (SOQ-48 — the
Tabla A1 delta map and the company-level edition flag are
`08_deferred-tax-adoption.md` by id). All section prints cited here are
3rd-edition as printed; edition-sensitive wording used in this file: the
22.7(a) local-law override clause ("a menos que las leyes o regulaciones
locales prohíban dicha presentación") is the 3rd-edition formulation
whose CC Art. 29 kin hook is consumed by id (FR-169). D15 anchors:
classification snapshots at lease inception (FR-145), provision
remeasurement at each reporting date (FR-137/138), grant condition
gating as-of condition satisfaction (FR-179), actuarial and 28.19
elections as-of adoption/policy dates (FR-159/161) — each resolved value
snapshots on the record. Mid-year go-live (D18): a migrating company's
provision balances, lease schedules, vacation accruals and equity
histories ingest as `is_historical` rows with original-period semantics
(tiered ingestion per D18; no re-derivation of the S4 statutory engines).
Hard no-override gates: the 25.2 no-capitalization guard (FR-181) and
the NOT-IFRS-16 guard (FR-152) are never disabled by configuration.

## 6. Acceptance Criteria

- **AC-001:** Given an employee with accumulated unused vacation days at
  year end whose statutory vacation quantum comes from the payroll engine
  (15 days × daily base × 1.30, SV-PAY-FR-044..049), when the book
  accrual runs, then the balance-sheet vacaciones liability equals the
  ADDITIONAL UNDISCOUNTED cost of the unused rights at the expected
  settlement rate — no present value, no re-derivation of the CT
  computation (FR-155).
- **AC-002:** Given the Apéndice 22 issuance — 500 convertible bonds at
  par 100 u.m., five years, 4% coupon, 6% market rate for similar
  non-convertible debt, no transaction costs — when the split engine
  runs, then the liability component books at 45.788 u.m. (PV principal
  37.363 + PV interest 8.425), the residual equity component at
  4.212 u.m., and no later re-split occurs on any subsequent
  measurement (FR-173).
- **AC-003:** Given a dividend declared by the junta on 15 March after a
  31 December reporting date, when the prior-year books close, then NO
  liability is recognized at 31 December; the amount optionally appears
  as a segregated component of ganancias acumuladas, and the
  distribution reduces equity on its declaration date in the new period
  (FR-175).
- **AC-004:** Given a board resolution committing to close a division
  with a net-zero cost budget but neither a formal detailed plan nor an
  announced execution, when the provision engine evaluates it, then NO
  restructuring provision is recognized — the FR-140 gate rejects
  commitment alone (FR-140).
- **AC-005:** Given a five-year operating lease escalating 100.000 →
  146.000 u.m. structured against published 10% expected inflation, when
  the expense scheduler runs, then the annual expense equals the amounts
  payable each year (as-incurred); the same lease WITHOUT a clear
  inflation structure expenses straight-line at 122.000 u.m. per year
  (FR-148).
- **AC-006:** Given a zona-franca usuario with 100% ISR exemption rows
  from the special-regimes engine (SV-SPE-FR-023), when the grant
  engine's exclusion runs, then NO grant income and NO grant liability
  record is created — the exemption stays a Sec 29/special-regimes
  surface and never enters Sección 24 (FR-178).
- **AC-007:** Given an entity constructing a qualifying asset while
  incurring bank interest, when the borrowing-cost posting runs under
  the PYMES engine, then ALL interest posts to current-period expense —
  and no user or configuration can route borrowing costs to an asset
  account (the capitalization path does not exist) (FR-181).
- **AC-008:** Given an employer electing the 28.19 simplified DB
  measurement with a disproportionate-cost registry row in place, when
  the obligation is measured, then it is computed assuming all employees
  terminate at the reporting date, ignoring future salary increases,
  future service and in-service mortality (post-service mortality
  counted), UNDISCOUNTED, including both vested and non-vested benefits,
  with the assumptions disclosed (FR-159).
- **AC-009:** Given a puttable instrument satisfying four of the five
  22.4 conditions, when its classification is recorded, then it books as
  a financial liability — the checklist requires ALL five (FR-166).
- **AC-010:** Given an entity with positive NIIF retained earnings but a
  CC realized-balance distribution capacity of zero (capital loss not
  yet restored), when a distribution is attempted, then the CC ceiling
  blocks it from the SEPARATE capacity field (SV-CML-FR-053 by id) — the
  NIIF equity figure never substitutes the ceiling and is never
  auto-read into the capacity field (FR-177).
- **AC-011:** Given non-cancellable operating leases with minimum
  payments across the bands ≤1y / 1-5y / >5y, when the lessee
  disclosures are emitted, then the maturity-band analysis discloses
  the totals per band per 20.16 (FR-152).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-49 carried: CC Arts. 37-38 distribution capacity is a realized-profit ("utilidades realmente obtenidas, conforme al balance") concept ABSENT from NIIF comprehensive income. Working assumption (never asserted as settled): CC governs as legal overlay — distribution capacity lives in a SEPARATE statutory ledger field (kin to the taxation/05 earnings register; ceiling + restitution mechanics consumed from SV-CML-FR-053 by id) and is NEVER auto-derived from NIIF equity (FR-177). How "utilidades realizadas por balance" is computed from NIIF-PYMES books (which profit measure, which realización criterion under the 2027 regime) is an open interpretive bridge until the Consejo/SV instrument lands. | no | Takumi S8 (interpretive bridge; sources watch) | open |
| OQ-2 | DB-applicability rarity note for SV: defined-benefit plans are rare in the SV private sector (EVID-295 gloss) — statutory ISSS/SIP schemes are DC-style book treatments (FR-157) and SIP pensions are individually funded accounts. The DB engine (FR-159..161) ships config-gated OFF by default; whether any SV multi-employer/state scheme's insufficient-information cases or a private DB plan require DB book treatment is a usage-rarity watch, not a corpus gap. | no | Takumi S8 (usage watch) | open |
| OQ-3 | SOQ-46 carried: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — this file's engines ship the Norma's machinery with NO invented SV thresholds (§2 note). Acquisition candidate ≥75 (same instrument as commercial-legal/03 OQ-002). | no | Takumi S8 (sources watch) | open |
| OQ-4 | SV government cash-grant instruments absent: no corpus source identifies an operative SV cash-grant program (the corpus's grant-adjacent items — ZF/LSI/DPA ladders, the Quincena-25 tax credit — are tax-computation benefits excluded by FR-178). The grant engine encodes the Norma's condition-gating machinery with NO SV-specific grant catalog; any SV grant program discovered later lands as dated configuration, never as new mechanics. | no | Takumi S8 (sources watch) | open |
