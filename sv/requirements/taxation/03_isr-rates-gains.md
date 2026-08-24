# SV — Taxation — ISR rates, brackets, capital gains & special computations

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR); W24 T2 fold-in (107_/108_ ganancia-de-capital exonerations) |
| Updated | 2026-08-24 |

## 1. Purpose

This file defines the functional requirements for the rate layer of El
Salvador's *Impuesto sobre la Renta* (ISR, income tax) and its special
computations: the Art. 37 progressive bracket table for domiciled natural
persons, *sucesiones* (estates) and *fideicomisos* (trusts) — with BOTH dated
vintages of the table transcribed verbatim (D.L. 957-2011 configuration and
D.L. 293-2025 configuration, effective 2025-05-08) — the 30% flat rate for
non-domiciled natural persons/sucesiones/fideicomisos, the exclusion of
final-withheld rents from the computation base, the Art. 41 entity rate
(30% / 25% for gravadas rents ≤ US$150,000) and the Art. 40 5%-gross
per-event rate for non-domiciled *conjuntos* (ensembles); the capital-gain
regime (the 12-month rule routing between 10% separate liquidation and
ordinary inclusion, *costo básico* (basis) = acquisition cost minus
accumulated admitted depreciation, conservation improvements and transaction
expenses, donated/inherited basis carryover, the *habitualidad* (habituality)
test and holding-period counting, banks'/insurers'/official-credit
extraordinary liquidations as ordinary income, and the capital-loss ledger
with its 5-year gains-only carryforward); the no-general-NOL statement;
the 10% separate liquidations on domestic securities and deposits (domestic
tracks only, post-D.L. 969-2024) with weighted-average cost per species and
securities-loss netting; and the special computations: >24-month instalment
deferral, repossession, rent-with-promise-to-sell, in-kind rent,
percentage-of-completion for >1-year contracts, life annuities, the interest
presumption, insurer/*fianza* (guarantee/suretyship) net-income determination
and export-income valuation.

It does **not** cover: the subject/period/method/territoriality frame
(`01_isr-framework.md`, T1 — its FRs are cited by id); deductions,
non-deductibles and the Art. 28 pro-rata allocator (`02_isr-deductions.md`,
T3 — the *reserva legal* 25% separate-liquidation trigger is owned by its
SV-TAX-FR-063 and is cross-referenced here, not restated); periodic payroll
retention tables and retention mechanics (`04_isr-withholding.md`, T5 — the
PERIODIC retention tables are that file's; only the ANNUAL Art. 37 table is
here); the 5% distributions regime (`05_isr-distributions.md`, T6); and
fixed-asset depreciation schedules (`06_isr-assets.md`, T7 — which
references this file's capital-gain FRs for its depreciation-ledger
linkage). Those files reference this one for the rates and special
computations that operate inside the T1/T3 frame.

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated
Ley ISR, current article text incl. reform stamps through Jan-2026) with
reform decrees 55_ (Art. 37), 56_ (D.L. 969-2024 derogations) for changed
articles > 03_ (historical consolidation through D.L. 233-2012; supplies
analysis via EVID ids). Reglamento: 04_ = D.E. 101-1992 as consolidated with
reforms D.E. 8-1993 / 39-1993 / **117-2001** (self-documented repeal map —
R17); only survivor articles are cited. Every Ley article below was
re-verified in the 54_ consolidation text during this task (54_-verify rule;
page anchors are 54_ pagination from the extraction txt `=== PAGE n ===`
markers; stamp keys read from the 54_ reform tail pp.59-60).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 37 inc. 1 + D.L. 293-2025 (reforma), Arts. 1 y 3 | Progressive table for domiciled natural persons, sucesiones and fideicomisos; current Tramo I $0.01–$6,600.00 exento, Tramo II $6,600.01–$9,142.86 10% s/ exceso de $6,600.00 + cuota fija $212.12, Tramo III $9,142.87–$22,857.14 20% s/ $9,142.86 + $720.00, Tramo IV $22,857.15 en adelante 30% s/ $22,857.14 + $3,462.86 (stamps (1)(19)(25)); D.L. 293-2025 reformed ONLY the Tramo I ceiling and Tramo II window/offset, effective 8 days after D.O. 30-IV-2025 → 2025-05-08 | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` + `sv/sources/55_Reforma_Ley_ISR_DL293_DO_2025-04-30.pdf` | 54_ Art. 37 p.38; 55_ Arts. 1/3 pp.1-3 (EVID-163) |
| LB-002 | Ley ISR, Arts. 34, 35, 36 | Domiciled personas naturales, sucesiones and fideicomisos calculate ISR by applying the Art. 37 table on the renta neta o imponible; second incisos (old rates) DEROGADO (1)(19) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 34-36 p.38 (EVID-095 historical analysis via 03_) |
| LB-003 | Ley ISR, Art. 37 incisos 2º-3º | Non-domiciled natural persons, sucesiones or fideicomisos calculate their tax applying 30% on their renta neta o imponible; rents subject to retención definitiva (definitive withholding) are EXCLUDED from the tax calculation (stamps (1)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 37 incisos 2º-3º p.38 (EVID-163; EVID-095) |
| LB-004 | Ley ISR, Art. 41 | Personas jurídicas, uniones de personas, sociedades irregulares o de hecho, domiciled or not, apply 30% on their renta imponible; EXCEPT subjects whose gravadas rents are ≤ US$150,000, which apply 25%; final-withheld rents excluded from the calculation; distributions of domiciled subjects bear the complementary tax (→ `05_isr-distributions.md`) (stamps (13)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 41 p.39 (EVID-166 verify: verbatim p.39) |
| LB-005 | Ley ISR, Art. 40 | Non-domiciled cultural, sports, artistic and similar conjuntos calculate the tax applying 5% on the renta bruta (gross income) obtained in each event | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 40 p.39 (EVID-095) |
| LB-006 | Ley ISR, Art. 14 | Capital gain = gain of a person NOT habitually dedicated to compraventa/permuta/negotiation of muebles or inmuebles; per-transaction result = transaction value − costo básico − conservación improvements − necessary transaction expenses (improvements already admitted as production/conservation expenses excluded); capital losses deductible only against capital gains, excess usable within the following FIVE years against future capital gains provided declared on the DGII form; losses from operations other than Art. 14.1 transactions never deductible against capital gains; costo básico (onerosous acquisition) = acquisition cost − depreciaciones realizadas y admitidas; donated/inherited = donor's/causante's costo básico; banks'/insurers'/official-credit-institutions'/non-bank financial intermediaries' extraordinary-asset liquidations taxed as ORDINARY renta (stamp (14) = D.L. 496-2004) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 14 pp.9-10 (EVID-093) |
| LB-007 | Ley ISR, Art. 42 | Tax on ganancia neta de capital (one or several transactions, determined per Art. 14) = 10% flat, EXCEPT when the bien is realized within the twelve months following acquisition → the gain sums to the ordinary renta neta imponible and is taxed as ordinary renta (annual declaration + capital-gain calculation form); prior-period unused capital-loss balance may be subtracted from the current-period net gain, the positive result being subject to the 10%; the >12-month capital-gains tax is ADDED to the tax calculated on ordinary renta imponible and paid within the same term as the annual sworn declaration, attaching the capital-gain (or loss) calculation form per DGII requirements (stamp (14) = D.L. 496-2004) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 42 pp.39-40 (EVID-093) |
| LB-008 | Reglamento ISR (D.E. 101-1992 consolidado), Art. 15 | Habitualidad: acts forming the corporate object/giro with intent to engage in the negotiated dealings, merchant or not; presumption salvo prueba en contrario (unless proven otherwise) of NON-habituality for sales of own fixed assets or personal-use goods when the transfer is eventual/occasional and acquired without resell intent; same for assets sold fractioned (participation/parceling) by nature/size, provided no resell intent at acquisition | `sv/sources/04_Reglamento_ISR.pdf` | Art. 15 p.6 (EVID-133) |
| LB-009 | Reglamento ISR, Art. 16 | Years-of-possession counting: (a) acquired in H1 → whole year; (b) transferred in H2 → whole year; (c) acquired and transferred within the following six months → whole year in the enajenación (disposal) year; transaction value = contract price; rent-with-promise-to-sell = total rent price + sale price if not included; pre-1992 assets: costo básico = value declared for the patrimonio tax at 31-dic-1990 (or special year-end), donation/inheritance carryover per the donor's/causante's same rules; INCISO QUINTO SUPRIMIDO (2) | `sv/sources/04_Reglamento_ISR.pdf` | Art. 16 pp.6-7 (EVID-134) |
| LB-010 | Reglamento ISR, Art. 17 — **HISTORICAL** | 9-step media-tasa (average half-rate) computation for assets held a whole number of years: spread the gain over years possessed, add the renta del período to ordinary income, tax the total per the Art. 37 table / Art. 41 rate / 25% for non-domiciled sucesiones-fideicomisos, halve the effective coefficient, apply to the remainder; 1.0% effective-rate fallback. Rate anchors are STALE vs current Ley (Art. 41 was 25% pre-957-2011; non-domiciled now 30%). HISTORICAL LB NOTE per SOQ-01 (OQ-001): superseded as a live method by Ley Art. 42 flat 10% (D.L. 496-2004 — later in time, higher hierarchy, specific rule); never implement for current periods; retain only as dated data for pre-2004 historical liquidations | `sv/sources/04_Reglamento_ISR.pdf` | Art. 17 pp.7-8 (EVID-135; SOQ-01) |
| LB-011 | Ley ISR, Art. 13 | Each ejercicio or period liquidated independently of the preceding and following one, save the legal exceptions (the capital-loss ledger and securities-loss netting of this file; no general NOL exists — SOQ-04/OQ-002) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 13 p.9 (EVID-106) |
| LB-012 | Ley ISR, Art. 14-A | Utilities, dividends, prizes, interest, réditos, net capital gains or any other benefit obtained by a DOMICILED natural person on investments in títulos valores (securities) and other financial instruments: 10% liquidated SEPARATELY from other rents; if retained, no declaration due — retention = definitive payment; unretained: paid within the annual-declaration term attaching the rentas-de-capital calculation form; transfer result: transaction value = agreed price, never below the stock-exchange quote at the enajenación date or the emitter's book value absent a quote; deductions = acquisition cost + necessary transaction expenses; several títulos → weighted average per species (promedios ponderados); negative result = capital loss compensable ONLY with securities/other capital gains of the same period or the five immediately following years, provided declared and registered; the transfer-result rules apply equally to subjects other than natural persons; dividends framed in Art. 4 num. 13 not subject (→ 5% distributions regime, `05_isr-distributions.md`); incisos 6º-8º (foreign securities) DEROGATED by D.L. 969-2024 — stamps (18)(24) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 14-A pp.10-11 (EVID-094 domestic tracks; EVID-164 derogations) |
| LB-013 | Ley ISR, Art. 27 | Natural persons' interest, prizes and other utilities from deposits in SSF-supervised financial institutions, savings-credit asociaciones/sociedades cooperativas and their federations domiciled in-country: 10% liquidated separately; if retained per CT Art. 159, no declaration — retention = definitive payment; incisos 2º-4º (foreign deposits) DEROGATED by D.L. 969-2024 (stamps (2)(8)(18) + (24)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 27 pp.14-15 (EVID-094 domestic track; EVID-168) |
| LB-014 | Ley ISR, Art. 4 num. 5 | Rentas no gravables: interest, prizes and other utilities from deposits in SSF-supervised institutions and savings-credit cooperatives/federations, provided the beneficiary is a DOMICILED natural person, holder of the deposits, and the average monthly balance of the deposits is BELOW US$25,000.00 (stamp (18) = D.L. 236-2009). Harmonized reading (SOQ-07): Art. 4.5 carves out small depositors; Art. 27's 10% applies above the carve-out | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 4.5 p.5 (EVID-139 gloss; SOQ-07) |
| LB-015 | Reglamento ISR, Arts. 12, 13, 14 | >24-month instalment deferral: habitual traders' utilities from credit operations with terms over twenty-four months may be DEFERRED in the proportional part corresponding to uncollected quotas (legal contract required), flowing into subsequent ejercicios proportionally to quotas collected/accrued; balance interest = income when received/accrued; rent-with-promise-to-sell: cánones (rent installments) computed as income of the ejercicios when realized; THE DEFERRAL RULES DO NOT APPLY TO CAPITAL GAINS (final inciso, reform (2)). Repossession (recobro): gain/loss of the repossession year = real value of the recovered bien − (unsatisfied quotas + rescates pagados). In-kind rents compensated with productos, frutos o mejoras valued at market price at the fiscal-year-end | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 12-14 pp.5-6 (EVID-132) |
| LB-016 | Reglamento ISR, Arts. 22, 23, 24, 25, 26 | Computable income inclusions: constitution of usufruct/use/habitation/servidumbre in favor of third parties, guarantees of obligations and any consideration for ceding use/enjoyment of muebles/inmuebles (Art. 22); interest presumption — every credit is presumed, salvo prueba en contrario, to yield the legal interest; interest = excess returned over received (Art. 23); non-compete payments or activity-abandonment consideration = taxable (Art. 24); onerosa life annuity: annual fraction of the price at the legal annual interest rate = taxable income, remainder = price recovery; year base = price − prior recoveries, until exhaustion; after full recovery everything taxable; beneficiary's death before term → unrecovered balance = debtor's taxable gain (Art. 25); insurer income composition: premiums, investment income, reinsurer collections, commissions, other profits (Art. 26) | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 22-26 pp.8-9 (EVID-137) |
| LB-017 | Reglamento ISR, Art. 27 | Renta from obligaciones de hacer (contracts to perform works) to be executed over a period greater than one year: computed in proportion to the part of the obra (work) performed during each ejercicio; the SAME proportional calculation applies to the cost and other legal deductions | `sv/sources/04_Reglamento_ISR.pdf` | Art. 27 p.10 (EVID-138) |
| LB-018 | Reglamento ISR, Art. 33 | Insurance/fianza/capitalization companies: net income = total income per Art. 26 + opening mathematical/technical reserves − Ley Art. 29 deductions − enumerated items (claims paid; endowment/matured contracts; life annuities paid; special benefits; rescates; claim-adjustment expenses; premium refunds; claims paid; premiums ceded to reinsurers; raffle prizes; reinsurance/reafianzamiento commissions; closing mathematical/technical reserves; death premium refunds) | `sv/sources/04_Reglamento_ISR.pdf` | Art. 33 pp.11-12 (EVID-141) |
| LB-019 | Reglamento ISR, Art. 34 | Export income: net income from exporting goods grown/produced/manufactured/acquired in-country = wholesale price at destination − cost of goods − in-country expenses − transport & insurance − commissions/selling expenses to the extent necessary | `sv/sources/04_Reglamento_ISR.pdf` | Art. 34 p.12 (EVID-142) |
| LB-020 | Reformas a la Ley para la Construcción, Administración, Operación y Mantenimiento del Aeropuerto Internacional del Pacífico (107_), Art. 1: "Adiciónase en el artículo 29, inciso primero, la letra e), de la siguiente manera: 'e) Exonérase del pago del Impuesto a la Ganancia de Capital, a que se refieren los artículos 14 y 42 de la Ley de Impuesto sobre la Renta, a los propietarios de los inmuebles que los vendan a CEPA y/o al MOPT, siempre que estos inmuebles estén comprendidos dentro del perímetro de delimitación a que se refiere el artículo 2 de la presente Ley.'" Art. 2: "Sustitúyese el artículo 35, por el siguiente: 'Art. 35.- Esta ley es de orden público y especial, por lo que sus efectos se retrotraerán al ocho de mayo del año dos mil veintidós, y priva sobre cualquier otra ley especial o general que la contradiga.'" Art. 3: "El presente decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." | The airport seller limb: the base law's Art. 29 exemption catalogue gains literal e) — propietarios selling inmuebles to CEPA and/or MOPT, provided the inmuebles sit inside the law's Art. 2 perímetro de delimitación, are EXONERATED from the Impuesto a la Ganancia de Capital of Ley ISR Arts. 14 and 42 (the Art. 42 10% AND the ≤12-month ordinary-renta limb's ganancia component — the Art. 14 determination is lifted for exonerated transfers); the substituted Art. 35 retrotrae the LAW's efectos al 8-may-2022 with orden-público-y-especial prevalence, so the exoneración window runs from 8-may-2022 — drafted to reach already-executed CEPA/MOPT purchases (considerandos IV-V replacement-property recitals; EVID-405). [As printed] note (EVID-405 doubt recorded here, NOT an OQ): the retro anchor 8-may-2022 sits one day AFTER the base law's own original vigencia start (D.L. 361-2022, D.O. N° 81 T.435 29-abr-2022 + 8 días = 7-may-2022) — no operative ambiguity for the exemption window (efectos from 8-may-2022 as printed). The base law D.L. 361-2022 is UN-ACQUIRED (identity row = spe/01 LB-035): the Art. 2 perimeter geometry = external config slot with NO default, and the base law's other Capítulo IV exonerations (CEPA/MOPT/companies — considerando II) are out-of-corpus, gloss only. Reform vigencia: D.O. 30-ene-2025 + 8 días = 7-feb-2025 (forward-looking) + the Art. 35 retro coverage. Operative FR = FR-418 | `sv/sources/107_Reforma_AeropuertoPacifico_DL201_2025_Asamblea.pdf` | 107_ Arts. 1-3 p.2 (EVID-405; 107_ txt PAGE 2; native asamblea text layer — intra-word cleaning per EV header; W24 T2) |
| LB-021 | Disposiciones Especiales y Transitorias de Apoyo al "Programa de Acceso Universal a la Energía en El Salvador" (108_), Art. 7: "Los propietarios o poseedores que vendan voluntariamente sus inmuebles a favor de la Comisión Ejecutiva Hidroeléctrica del Río Lempa (CEL), estarán exentos del pago del Impuesto sobre la Renta que pudiera generar la venta de los mismos en concepto de Ganancia de Capital, en consecuencia, tampoco estarán obligados a presentar por dicha venta el formulario para el cómputo correspondiente a la misma." | CEL-seller exoneración (kin-class to LB-020's CEPA/MOPT limb; EVID-406 gloss (5)): propietarios O POSEEDORES voluntarily selling their inmuebles to CEL are exempt from the ISR the sale could generate in concepto de Ganancia de Capital — the seller class is BROADER than 107_'s propietarios (poseedores included) and carries no perimeter geometry (the acquirer CEL is identitary); in consequence the formulario-for-cómputo duty for that sale is EXPRESSLY LIFTED (the ganancia-cómputo form duty — the express lift distinguishes 108_ from 107_, which prints no formulario clause). Operative FR = FR-419; window = the 108_ decree vigencia with the benefit's own event limbs (spe/02 SV-SPE-FR-204 by id; identity row = spe/01 LB-034) | `sv/sources/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf` | 108_ Art. 7 p.4 (EVID-406; 108_ txt PAGE 4; native asamblea text layer — intra-word cleaning per EV header; W24 T2) |

Dead text — never implementable as current law (recorded as LB notes, not
FRs, per wave constraints; cross-referenced, not restated): Reglamento
Art. 17 media-tasa method — historical per SOQ-01 (LB-010); EVID-095's
Art. 37 Tramos I/II rows ($4,064.00 config) — superseded vintage retained
as dated data per R20 (LB-001); EVID-094's foreign-securities/deposit
paragraphs and the anti-exemption gross-up — dead per D.L. 969-2024
(`01_isr-framework.md` LB-019; R18); pago mínimo Arts. 76-81 —
unconstitutional (`01_isr-framework.md` §2; R21).

## 3. Functional Requirements

### 3.1 Rates and brackets (Arts. 34-41)

- **SV-TAX-FR-074:** The system shall compute ISR for domiciled natural
  persons, *sucesiones* and *fideicomisos* by applying the Art. 37
  progressive table (per Arts. 34-36) to the *renta neta o imponible*
  (net or taxable income): locate the row whose DESDE/HASTA interval
  contains the base, apply the row's percentage over the excess of the
  base above the row's SOBRE EL EXCESO DE anchor, and add the row's
  *cuota fija* (fixed quota). Version note (D12): TWO table vintages as
  dated data — (a) D.L. 957-2011 configuration, applicable to periods
  through 2025-05-07;   (b) D.L. 293-2025 configuration, applicable from
  2025-05-08 — both transcribed verbatim in §4; the engine selects the
  vintage by the liquidation period's close date: a period closing on or
  before 2025-05-07 uses vintage (a); a period closing on or after
  2025-05-08 — including the 2025 calendario ejercicio — uses vintage (b)
  (straddle nuance recorded as OQ-009). The PERIODIC payroll retention
  tables derived from Art. 37 are `04_isr-withholding.md` property and are
  not duplicated here. (LB-001; LB-002; EVID-163/095; R20)
- **SV-TAX-FR-075:** The system shall compute ISR for non-domiciled
  natural persons, sucesiones and fideicomisos as a flat 30% on their
  renta neta o imponible (no brackets). (LB-003; EVID-163)
- **SV-TAX-FR-076:** The system shall exclude from the ISR computation
  base — both the Art. 37 progressive table and the Art. 41 flat rates —
  every rent that was subject to *retención definitiva* (definitive
  withholding) at the legal percentages, so that no final-withheld rent is
  taxed twice; such rents remain visible in the determination worksheet as
  excluded-with-evidence lines. (LB-003; LB-004; EVID-095)
- **SV-TAX-FR-077:** The system shall compute ISR for personas jurídicas,
  *uniones de personas*, and *sociedades irregulares o de hecho*, domiciled
  or not, at 30% on the renta imponible, EXCEPT when the gravadas rents
  obtained in the ejercicio or period being liquidated are less than or
  equal to US$150,000.00, in which case it shall apply 25%; the threshold
  shall be re-evaluated on EACH ejercicio's own gravadas rents (no
  lock-in: an entity may switch 25% ↔ 30% between consecutive ejercicios
  as its gravadas rents move across the threshold), and final-withheld
  rents are excluded from the computation per SV-TAX-FR-076. (LB-004;
  EVID-166)
- **SV-TAX-FR-078:** The system shall compute ISR for non-domiciled
  conjuntos as 5% on the *renta bruta* (gross income, no cost/expense
  deduction) obtained in each event, as a per-event liquidation (filing
  mechanics per SV-TAX-FR-030, single-subject aggregation per
  SV-TAX-FR-018). (LB-005; EVID-095)

### 3.2 Capital gains and the capital-loss ledger (Arts. 14/42; Reglamento Arts. 15-17)

- **SV-TAX-FR-079:** The system shall route the disposal of muebles or
  inmuebles (movable or immovable goods) through the *habitualidad*
  (habituality) gate: disposals by a person NOT habitually dedicated to
  *compraventa* (sale-purchase), *permuta* (exchange/barter) or other
  negotiations on such goods follow the capital-gain track, and the system
  shall apply the Reglamento Art. 15 presumptions *salvo prueba en
  contrario* — eventual/occasional transfers of own fixed assets or
  personal-use goods acquired without resell intent are presumed
  NON-habitual (capital-gain track), likewise assets necessarily sold
  fractioned (participation/parceling) when acquired without resell
  intent, even if the individual transfers look massified; habitual-giro
  disposals follow the ordinary track. (LB-006; LB-008; EVID-093/133)
- **SV-TAX-FR-080:** The system shall determine each capital
  transaction's per-transaction result as: transaction value − *costo
  básico* (tax basis) − the importe of improvements made to CONSERVE the
  good's value − necessary transaction expenses; a positive result is
  *ganancia de capital* (capital gain) and a negative result is *pérdida
  de capital* (capital loss); improvements already admitted as production
  or source-conservation expenses shall be excluded from the improvement
  deduction (no double counting). This FR and SV-TAX-FR-081 are the
  capital-gain interface consumed by `06_isr-assets.md` §3 for the
  depreciation-ledger linkage. (LB-006; LB-009; EVID-093/134)
- **SV-TAX-FR-081:** The system shall determine *costo básico* as:
  (a) for goods acquired *a título oneroso* (for valuable consideration) —
  acquisition cost MINUS the depreciations effected and admitted under the
  law (accumulated admitted depreciation from the asset's depreciation
  ledger, per `06_isr-assets.md`); (b) for goods acquired by donation or
  inheritance — the donor's or *causante* (decedent) basis carried over
  (consistent with SV-TAX-FR-005's antecesor-value rule); (c) pre-1992
  assets — the value declared for the patrimonio tax at 31-Dec-1990 (or
  the special ejercicio's year-end; undeclared assets: the last valuation
  declared before that date), with no revaluation allowed (historical
  rule, dated data). (LB-006; LB-009; EVID-093/134)
- **SV-TAX-FR-082:** The system shall apply the 12-month rule to the net
  capital gain: when the good is realized WITHIN the twelve months
  following its acquisition date, the ganancia neta de capital shall be
  SUMMED to the ordinary renta neta imponible and taxed as ordinary renta
  (Art. 37 table / Art. 41 rate / 30% non-domiciled, per the subject's
  track); when realized AFTER those twelve months, the tax shall be the
  flat 10% of the ganancia neta de capital, computed as a separate
  liquidation ADDED to the tax on ordinary renta imponible for payment,
  paid within the same four-month term as the annual sworn declaration and
  accompanied by the DGII capital-gain calculation form. SOQ-01 verdict
  (OQ-001): this Art. 42 rule (D.L. 496-2004) governs ALL current periods
  and taxpayer classes; the Reglamento Art. 17 media-tasa mechanism is a
  historical method (LB-010) and shall never be applied to current
  periods. (LB-007; LB-010; EVID-093/135; SOQ-01)
- **SV-TAX-FR-083:** The system shall compute the holding period for the
  12-month rule (and year-counting generally) per Reglamento Art. 16:
  (a) acquisition in the first semester of an ejercicio counts as
  possessed for the WHOLE year; (b) transfer in the second semester counts
  as possessed for the whole year; (c) a good acquired and transferred
  within the six months following acquisition counts as possessed the
  whole year of its *enajenación*; and shall take the transaction value as
  the price stipulated in the contract — for rent-with-promise-to-sell,
  the total rent price plus the sale price when the latter is not included
  in the former. (LB-009; EVID-134)
- **SV-TAX-FR-084:** The system shall treat the extraordinary-asset
  liquidations of banks (Ley de Bancos), insurance companies, official
  credit institutions and non-bank financial intermediaries as ORDINARY
  renta of the realization ejercicio (ordinary track: progressive table /
  Art. 41 rate), never as capital gains. (LB-006; EVID-093)
- **SV-TAX-FR-085:** The system shall keep a capital-loss ledger per
  subject: capital losses (Art. 14.1 transactions, and securities
  transactions per SV-TAX-FR-089) shall offset capital gains ONLY — never
  ordinary income (deduction block per SV-TAX-FR-061); where the loss
  exceeds the gains of the period, the excess shall carry forward for use
  against future capital gains within the FIVE years following, always
  conditioned on the loss having been declared on the DGII form provided
  for that purpose; prior-period unused loss balances shall be subtracted
  from the current ganancia neta de capital before applying the 10%,
  taxing only the positive result; losses from operations other than the
  legally regulated ones shall never enter the ledger (no cross-type
  offset), and losses from related-subject or preferential-regime
  transactions are blocked outright per SV-TAX-FR-061. (LB-006; LB-007;
  EVID-093/106)
- **SV-TAX-FR-418:** The system shall apply a dated exoneración stamp
  `aeropuerto_dl201_art29_1e` on the gain-track engine (SV-TAX-FR-082):
  disposals of inmuebles sold to CEPA and/or MOPT — sellers being
  propietarios, the inmueble sitting inside the base law's Art. 2
  perímetro de delimitación (perimeter = external config slot, base law
  D.L. 361-2022 UN-ACQUIRED — NO default geometry; spe/01 LB-035 by id) —
  carry the stamp for sales with efectos from **8-may-2022** (the
  substituted Art. 35 retro window; D15 dated rows: window start
  8-may-2022, instrument 107_ (D.L. 201-2025), reform vigencia
  7-feb-2025 forward-looking PLUS the retro coverage — drafted to reach
  already-executed sales). Stamped disposals produce NO Art. 42 10%
  liability and NO ganancia entry in the annual liquidation — the Art. 14
  determination is not computed for exonerated transfers (the LB-006/
  LB-007 heads are lifted for this disposal class; nothing flows into the
  SV-TAX-FR-082 routing or the SV-TAX-FR-085/086 loss machinery). 107_
  prints no express formulario lift — the form surface rides the OQ-006
  forms config-gap (computation-annex discipline, no layout invented).
  (LB-020; LB-006; LB-007; EVID-405 W24 T2)
- **SV-TAX-FR-419:** The system shall apply the same exoneración chassis
  (FR-418) to stamp `energia_dl411_art7` on disposals of inmuebles
  voluntarily sold to the Comisión Ejecutiva Hidroeléctrica del Río Lempa
  (CEL) by propietarios O POSEEDORES — the broader 108_ seller class
  (poseedores included — the class difference vs FR-418's
  perimeter-bounded propietarios), no perimeter geometry (the acquirer
  CEL is identitary) — with window = the 108_ decree vigencia
  **27-sep-2025 → 26-sep-2031** (Art. 13; the benefit's own event limbs
  per SV-SPE-FR-204 by id). Stamped disposals produce no Ganancia de
  Capital ISR liability and no ganancia entry in the annual liquidation
  (Art. 14/42 heads not computed, kin FR-418), AND the
  formulario-for-cómputo duty for the sale is EXPRESSLY LIFTED — the
  disposal record carries a no-computation-form flag (the express text
  distinguishes this limb from FR-418, where no formulario clause is
  printed). (LB-021; EVID-406 W24 T2; cross-ref FR-418, SV-SPE-FR-204)

### 3.3 Losses: no general NOL

- **SV-TAX-FR-086:** The system shall implement NO general net-operating-
  loss carryforward: each ejercicio's ordinary renta is liquidated
  independently (per SV-TAX-FR-011), and an ordinary loss shall never
  reduce a following period's renta imponible, the ONLY loss-carryforward
  exceptions in the corpus being the capital-loss ledger (SV-TAX-FR-085)
  and the securities-loss netting (SV-TAX-FR-089). This statement is the
  no-NOL anchor cross-referenced by 02's zero-base guard (SV-TAX-FR-038:
  no negative base through the mermas channel — D.L. 345-2019) and by
  SV-TAX-FR-011. SOQ-04 verdict (OQ-002): targeted scans of the Código
  Tributario and the Reglamento found no pérdida-fiscal carryforward rule
  (only document-loss contexts and the Art. 13/14 capital-loss rules). If
  a future source adds an NOL regime, it enters as dated data plus a new
  FR. (LB-011; EVID-106; SOQ-04)

### 3.4 Securities and deposits: the 10% separate liquidations (Arts. 14-A, 27, 4.5)

- **SV-TAX-FR-087:** The system shall route DOMESTIC securities income —
  utilities, dividends, prizes, interest, réditos, net capital gains and
  any other benefit obtained by a domiciled natural person on investments
  in *títulos valores* (securities) and other financial instruments — to
  the 10% separate-liquidation track, computed outside the ordinary base;
  where the corresponding retentions were effected, the rents shall NOT be
  declared (retention = definitive payment); unretained amounts are paid
  within the same term as the annual ISR declaration, attaching the
  rentas-de-capital calculation form. FOREIGN securities/deposits shall
  NOT enter this track (dead per D.L. 969-2024; territorial routing per
  SV-TAX-FR-025). Dividends framed in Art. 4 num. 13 route to the 5%
  distributions regime (`05_isr-distributions.md` §3), not here.
  (LB-012; EVID-094; R18)
- **SV-TAX-FR-088:** The system shall determine the securities transfer
  result as: transaction value − acquisition cost − necessary transaction
  expenses, where the transaction value is the price agreed by the parties
  floored at the stock-exchange quotation at the enajenación date (or the
  emitter's book value when no exchange quote exists — i.e. the value
  shall never be booked below that floor), and where, for holdings of
  several títulos, the acquisition cost is computed by *promedios
  ponderados* (weighted averages) PER SPECIES — total acquisition costs of
  the species divided by the total number of títulos of that species
  acquired — even when only a part is transferred. (LB-012; EVID-094)
- **SV-TAX-FR-089:** The system shall net securities capital losses only
  against capital gains from títulos valores or other goods obtained in
  the same ejercicio or in the FIVE immediately following years, always
  conditioned on the loss having been DECLARED and REGISTERED (ledger
  discipline per SV-TAX-FR-085); securities losses shall never offset
  ordinary income. (LB-012; EVID-094)
- **SV-TAX-FR-090:** The system shall apply the securities transfer-result
  rules of SV-TAX-FR-088 (price floor, weighted-average cost per species)
  to subjects OTHER than natural persons as well, per the Art. 14-A
  inciso extending those ganancia-de-capital rules to such subjects.
  (LB-012; EVID-094)
- **SV-TAX-FR-091:** The system shall route DOMESTIC deposit income —
  interest, prizes and other utilities of natural persons from deposits in
  SSF-supervised financial institutions and in savings-credit
  asociaciones/sociedades cooperativas and their federations domiciled
  in-country — to the 10% separate-liquidation track: with the CT Art. 159
  retention effected, no declaration is due (definitive payment);
  unretained, declared with the annual declaration and the form. SOQ-07
  harmonized note: the Art. 4.5 carve-out makes such rentas NO gravables
  when the beneficiary is a domiciled natural person, holder of the
  deposits, whose average monthly deposit balance is BELOW
  US$25,000.00 — the system shall evaluate the carve-out first (exempt
  small depositors) and apply Art. 27's 10% only above it; FOREIGN
  deposits never enter this track (dead per D.L. 969-2024). (LB-013;
  LB-014; EVID-094/139; SOQ-07)

### 3.5 Special computations (Reglamento survivors)

- **SV-TAX-FR-092:** The system shall support the >24-month instalment
  deferral for HABITUAL traders (habituality per SV-TAX-FR-079): utilities
  from credit operations whose terms exceed twenty-four months, backed by
  a legally-celebrated contract, may be deferred in the proportional part
  corresponding to the value of the uncollected quotas, the deferred
  amounts flowing into the renta neta of subsequent ejercicios in
  proportion to the quotas collected or accrued in each; interests
  produced by the balances shall be computed as income of the ejercicios
  in which effectively received or accrued per the subject's accounting
  system; the deferral shall NEVER be applied to capital gains (final
  inciso carve-out). (LB-015; EVID-132)
- **SV-TAX-FR-093:** The system shall compute the repossession
  (*recobro*) result when a good disposed of under an instalment contract
  is recovered for any cause: gain or loss of the repossession-year
  ejercicio = real value of the recovered good − (sum of the unsatisfied
  quotas + *rescates pagados* (buyout payments made)). (LB-015; EVID-132)
- **SV-TAX-FR-094:** The system shall recognize income from
  rent-with-promise-to-sell contracts — the *cánones* (rent installments)
  as income of the ejercicios in which they are realized, and any
  stipulated interests per the balance-interest rule of SV-TAX-FR-092
  (income when received or accrued per the accounting system).
  (LB-015; EVID-132)
- **SV-TAX-FR-095:** The system shall value rents compensated in kind —
  with products, fruits or improvements of the goods — at the market price
  those products, fruits or improvements hold at the date the ejercicio
  legally closes. (LB-015; EVID-132)
- **SV-TAX-FR-096:** The system shall compute income and deductions of
  *obligaciones de hacer* (contracts to perform works) to be executed over
  a period GREATER than one year under percentage-of-completion: the
  renta of each ejercicio is calculated in proportion to the part of the
  obra (work) performed during that ejercicio, and the SAME proportional
  calculation applies to the cost and the other legal deductions (revenue
  AND costs matched to progress). (LB-017; EVID-138)
- **SV-TAX-FR-097:** The system shall compute taxable income from onerosa
  life annuities (*rentas vitalicias*) by the Art. 25 algorithm: each
  year, the taxable fraction = annuity price × legal annual interest rate;
  the remainder of the amounts paid = recovery of price; the next year's
  price base = price − prior recoveries, iterating until the price is
  fully recovered, after which EVERYTHING received is taxable income; on
  the beneficiary's death before the price is fully recovered, the
  unrecovered balance is the debtor's taxable gain. The legal-interest
  rate is outside this corpus (OQ-004). (LB-016; EVID-137)
- **SV-TAX-FR-098:** The system shall include as computable renta: any
  consideration for constituting usufruct, use, habitation or
  *servidumbre* (easement) rights in favor of third parties, for
  guaranteeing obligations, and for ceding the use or enjoyment of movable
  or immovable property (Reglamento Art. 22); payments for non-compete
  obligations (*obligaciones de no hacer*) or for abandoning an activity
  (Art. 24); and shall apply the interest presumption — every credit is
  presumed, salvo prueba en contrario, to yield the LEGAL interest, the
  interest being the excess returned over the amount received (Art. 23;
  rate source outside the corpus, OQ-004). (LB-016; EVID-137)
- **SV-TAX-FR-099:** The system shall provide the insurer/*fianza*
  net-income determination as a sector template (awareness-level): net
  income = total income per Reglamento Art. 26 composition + opening
  mathematical/technical reserves − Ley Art. 29 deductions − the Art. 33
  enumerated items (claims paid, endowment/matured contracts, life
  annuities paid, special benefits, rescates, claim-adjustment expenses,
  premium refunds, claims paid, premiums ceded to reinsurers, raffle
  prizes, reinsurance/reafianzamiento commissions, closing reserves,
  death premium refunds). (LB-018; EVID-141)
- **SV-TAX-FR-100:** The system shall value net income from exporting
  goods grown, produced, manufactured or acquired in-country as:
  wholesale price at destination − cost of the goods − expenses incurred
  in the country − transport and insurance − commissions and selling
  expenses, to the extent they are necessary. (LB-019; EVID-142)

### 3.6 Separate-liquidation computation slot

- **SV-TAX-FR-101:** The system shall compute every separate-liquidation
  track outside the ordinary ISR base and outside each other, covering at
  least: 10% capital gains realized after 12 months (SV-TAX-FR-082), 10%
  domestic securities rents (SV-TAX-FR-087), 10% domestic deposit rents
  (SV-TAX-FR-091), and the 25% *reserva legal* reduction liquidation
  (trigger and register owned by `02_isr-deductions.md` SV-TAX-FR-063 —
  cross-referenced here, not restated); each track's tax is added to the
  ordinary ISR of the same ejercicio for payment with the annual
  declaration; final-withheld tracks never re-enter any base
  (SV-TAX-FR-076), and prior-period loss balances enter only through
  their own track's netting rules (SV-TAX-FR-085/089). (LB-007; LB-012;
  LB-013; EVID-093/094; 02-file SV-TAX-FR-063)

## 4. Data Model

Machine-readable sidecars (the two Art. 37 vintages as JSON/CSV bracket
data) live next to this markdown file when produced. Layer semantics: this
file introduces Odoo-side computation/bookkeeping data only (wave default
`odoo`; see §5).

**Art. 37 progressive table — VERBATIM dated data (two vintages):**

Vintage A — D.L. 957-2011 configuration (applicable to periods through
2025-05-07; Tramos I/II superseded per R20 — historical dated data):

| Tramo | Desde | Hasta | % a aplicar | Sobre el exceso de | Más cuota fija de |
|-------|-------|-------|-------------|--------------------|-------------------|
| I | $0.01 | $4,064.00 | EXENTO | — | — |
| II | $4,064.01 | $9,142.86 | 10% | $4,064.00 | $212.12 |
| III | $9,142.87 | $22,857.14 | 20% | $9,142.86 | $720.00 |
| IV | $22,857.15 | EN ADELANTE | 30% | $22,857.14 | $3,462.86 |

Vintage B — D.L. 293-2025 configuration (applicable from 2025-05-08; the
current vintage; source: 55_ Art. 1 decree table + 54_ p.38 consolidated
table, stamps (1)(19)(25)):

| Tramo | Desde | Hasta | % a aplicar | Sobre el exceso de | Más cuota fija de |
|-------|-------|-------|-------------|--------------------|-------------------|
| I | $0.01 | $6,600.00 | EXENTO | — | — |
| II | $6,600.01 | $9,142.86 | 10% | $6,600.00 | $212.12 |
| III | $9,142.87 | $22,857.14 | 20% | $9,142.86 | $720.00 |
| IV | $22,857.15 | EN ADELANTE | 30% | $22,857.14 | $3,462.86 |

**Rate parameters and bracket engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.rate.bracket (new) | vintage, tramo, desde, hasta, rate, excess_of, fixed_quota | monetary/select | vintage: dl_957_2011 (valid_to 2025-05-07) · dl_293_2025 (valid_from 2025-05-08); tramo: I·II·III·IV; hasta nullable = EN ADELANTE | FR-074 |
| l10n_sv.isr.rate.parameter (new) | parameter, value, valid_from, valid_to | monetary/percent | nonresident_natural_30 · entity_30 · entity_25 · entity_threshold_150000 · conjunto_5_gross · capital_gain_10 · securities_10 · deposits_10 · deposit_carveout_25000 · reserva_reduction_25 | FR-075, FR-077, FR-078, FR-082, FR-087, FR-091, FR-101 |
| account.move.line | isr_final_withheld | boolean (computed) | true → excluded from ISR computation base; visible as excluded-with-evidence | FR-076 |
| res.company | isr_entity_rate_track | select (computed per ejercicio) | rate_25 · rate_30 | FR-077 |

**Capital gains and losses:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset | isr_costo_basico | monetary (computed) | acquisition cost − accumulated admitted depreciation; donation/inheritance carryover; pre-1992 patrimonio value (dated) | FR-081 |
| account.asset | isr_admitted_depreciation | monetary | fed from the depreciation ledger (`06_isr-assets.md` §3 linkage) | FR-081 |
| account.asset | isr_acquisition_date, isr_holding_years | date · integer (computed) | Art. 16 counting rules (H1 acquisition / H2 transfer full-year; ≤6-month flip full-year) | FR-083 |
| account.move (disposal) | isr_transaction_value, isr_conservation_improvements, isr_transaction_expenses, isr_capital_result | monetary | per-transaction formula; improvements already deducted excluded | FR-080 |
| account.move (disposal) | isr_gain_track | select | ordinary_inclusion_12m · separate_10 · bank_insurer_ordinary | FR-079, FR-082, FR-084 |
| account.move (disposal) | isr_habituality_status | select | presumed_non_habitual · proven_habitual · giro | FR-079 |
| l10n_sv.isr.capital.loss.ledger (new) | subject, origin_year, transaction_ref, loss_amount, declared_on_dgii_form | monetary/boolean | entries require DGII-form declaration flag | FR-085 |
| l10n_sv.isr.capital.loss.ledger | applications, balance, expiry_year | monetary/int (computed) | 5-year carryforward; gains-only application; expiry = origin + 5 | FR-085 |
| account.move (disposal) | isr_capital_gain_exoneration | select null | aeropuerto_dl201_art29_1e (107_: acquirer CEPA y/o MOPT; inmueble inside the base-law Art. 2 perimeter — external config, NO default geometry) · energia_dl411_art7 (108_ Art. 7: voluntary sale to CEL; seller class propietarios O POSEEDORES) | FR-418, FR-419 |
| account.move (disposal) | isr_capital_gain_exoneration_window · no_computation_form | config/date + boolean | 107_: efectos from 8-may-2022 (Art. 35 retro window) + reform vigencia 7-feb-2025; 108_: decree vigencia 27-sep-2025 → 26-sep-2031 (event limbs per SV-SPE-FR-204 by id); no_computation_form = true ONLY on energia_dl411_art7 rows (express formulario lift, Art. 7) | FR-418, FR-419 |

**Securities and deposits:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.security.position (new) | species, quantity, total_acquisition_cost, weighted_avg_cost | monetary (computed) | weighted average PER SPECIES; cost = acquisitions aggregated | FR-088, FR-090 |
| account.move (securities transfer) | isr_transfer_floor_value | monetary (computed) | stock-exchange quote at enajenación date, else emitter book value — transaction value floored | FR-088 |
| l10n_sv.isr.securities.loss (new) | origin_year, species, loss_amount, declared_and_registered | monetary/boolean | netting same-period + 5 years vs capital gains only | FR-089 |
| account.move.line | isr_separate_track | select null | securities_10 · deposits_10 · capital_gain_10 · reserva_25 | FR-087, FR-091, FR-101 |
| account.move.line (deposit income) | isr_small_depositor_carveout | boolean (computed) | domiciled natural person, holder, avg monthly balance < $25,000 → no gravable | FR-091 |

**Special computations:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move / sale order (instalment) | isr_instalment_deferral | boolean + computed split | >24-month credit, legal contract; deferred = proportional to uncollected quotas; capital gains excluded | FR-092 |
| account.move (repossession) | isr_repossession_result | monetary (computed) | real value − (unsatisfied quotas + rescates pagados) | FR-093 |
| account.move.line (rent-promise) | isr_canon_recognition | select | realized (cánones when realized; interests per balance rule) | FR-094 |
| account.move.line (in-kind rent) | isr_inkind_valuation_date | date (computed) | market price at fiscal-year-end | FR-095 |
| project.project / account.analytic | isr_poc_long_term | boolean | >1-year obligaciones de hacer: revenue AND costs by % of obra performed | FR-096 |
| account.move (annuity) | isr_annuity_price, isr_annuity_recovered, isr_annuity_taxable_fraction | monetary (computed) | price × legal rate; base = price − prior recoveries | FR-097 |
| account.move.line | isr_special_inclusion | select null | real_rights_consideration · guarantee_consideration · use_enjoyment_cession · non_compete · activity_abandonment · presumed_legal_interest | FR-098 |
| l10n_sv.isr.insurer.determination (new) | sector worksheet fields per Reglamento Art. 33 | monetary | Art. 26 income + opening reserves − deductions − enumerated items | FR-099 |
| account.move.line (export) | isr_export_valuation | monetary (computed) | wholesale-at-destination − goods cost − in-country expenses − transport/insurance − necessary commissions | FR-100 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living in
the LGPL client. No SaaS rows are introduced in this file: none of these FRs
touch DTE generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are stable
across Odoo 17/18/19/20; version-specific behavior is recorded per row where
a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-074 | odoo | l10n_sv.isr.rate.bracket | vintage rows | Two dated vintages seeded (957-2011 ≤2025-05-07; 293-2025 from 2025-05-08); selection by liquidation-period date; payroll retention tables NOT here (04 file) |
| FR-075 | odoo | l10n_sv.isr.rate.parameter | nonresident_natural_30 | Consumed when res.company isr_subject_type ∈ {natural_person, succession, trust} ∧ not domiciled |
| FR-076 | odoo | account.move.line | isr_final_withheld | Reads retention-definitive flags from the 04/05-file retention data; excludes from all rate applications |
| FR-077 | odoo | res.company / l10n_sv.isr.rate.parameter | entity_25/30, threshold | Threshold re-evaluated per ejercicio on own gravadas rents; no lock-in |
| FR-078 | odoo | l10n_sv.isr.filing.duty (event) + rate parameter | conjunto_5_gross | Per-event gross-base computation; filing duty per 01-file FR-030 |
| FR-079 | odoo | account.move (disposal) | isr_habituality_status | Presumptions seeded from asset class (fixed asset/personal use) + acquisition intent flag; rebuttable with evidence attachment |
| FR-080 | odoo | account.move (disposal) | isr_capital_result fields | Interface FR for 06 file (depreciation-ledger linkage) |
| FR-081 | odoo | account.asset | isr_costo_basico, isr_admitted_depreciation | Interface FR for 06 file; donation/inheritance carryover from 01-file FR-005 basis data; pre-1992 patrimonio values as dated data |
| FR-082 | odoo | account.move (disposal) + computation | isr_gain_track | SOQ-01 verdict: Art. 42 governs; Art. 17 media-tasa NEVER applied to current periods (historical only); 10% track added to ordinary tax for payment; DGII form as report annex (OQ-006) |
| FR-083 | odoo | account.asset | isr_holding_years | Art. 16 full-year counting rules; rent-with-promise transaction value composition |
| FR-084 | odoo | account.move (disposal) | isr_gain_track = bank_insurer_ordinary | Partner/sector flag on the liquidating entity (banks, insurers, official credit, non-bank intermediaries) |
| FR-085 | odoo | l10n_sv.isr.capital.loss.ledger | all | Declared-on-form flag gates carryforward; 5-year expiry computed; cross-type offset blocked (02-file FR-061 hook) |
| FR-086 | odoo | computation guard | — | Negative ordinary base never carries: period close zeroes it (01-file FR-011; 02-file FR-038 zero-base guard) |
| FR-087 | odoo | account.move.line | isr_separate_track = securities_10 | Domestic-only routing per 01-file FR-025; retained → definitive (no declaration line); dividends Art. 4.13 route to 05 file |
| FR-088 | odoo | l10n_sv.isr.security.position | weighted_avg_cost | Price-floor validation against quotation/book-value feed (OQ-005 kin: quote source outside corpus) |
| FR-089 | odoo | l10n_sv.isr.securities.loss | all | Declared-and-registered gate; netting window same period + 5 years |
| FR-090 | odoo | l10n_sv.isr.security.position | applies to all subjects | Subject-type check removed for transfer-result rules only |
| FR-091 | odoo | account.move.line | isr_separate_track = deposits_10 + carveout flag | Art. 4.5 carve-out evaluated first (avg monthly balance < $25,000 → no gravable); CT 159 retention-definitive flag consumed |
| FR-092 | odoo | sale.order / account.move | isr_instalment_deferral | >24-month credit sales of habitual traders; deferred schedule posted proportionally to collections; capital-gain exclusion enforced |
| FR-093 | odoo | account.move | isr_repossession_result | Repossession event posting on the asset/good recovery |
| FR-094 | odoo | account.move.line | isr_canon_recognition | Rent-promise contracts; interest per balance rule |
| FR-095 | odoo | account.move.line | isr_inkind_valuation_date | Market-price feed at fiscal-year close |
| FR-096 | odoo | project.project / analytic | isr_poc_long_term | POC recognition engine: revenue and cost lines generated by % of obra performed (projects module) |
| FR-097 | odoo | account.move (annuity) | annuity fields | Legal-interest rate as dated external parameter (OQ-004) |
| FR-098 | odoo | account.move.line | isr_special_inclusion | Inclusion catalog; interest presumption applied salvo prueba en contrario (rebuttal evidence attachment) |
| FR-099 | odoo | l10n_sv.isr.insurer.determination | worksheet | Awareness-level sector template; special-regimes wave may extend |
| FR-100 | odoo | account.move.line (export) | isr_export_valuation | Export valuation worksheet on export invoices |
| FR-101 | odoo | computation slot | separate tracks | Umbrella engine: tracks computed isolated from ordinary base and each other; reserva-25 consumes 02-file FR-063 register |
| FR-418 | odoo | account.move (disposal) | isr_capital_gain_exoneration (+ aeropuerto_dl201_art29_1e) | 107_ D.L. 201-2025 Art. 1 (airport-law Art. 29.1.e): CEPA/MOPT perimeter sellers exonerated from the Arts. 14/42 ganancia — efectos from 8-may-2022 (Art. 35 retro window; reform vigencia 7-feb-2025); perimeter = external config slot (base law un-acquired, NO default geometry); no formulario clause printed — form surface rides OQ-006 |
| FR-419 | odoo | account.move (disposal) | isr_capital_gain_exoneration_window · no_computation_form (+ energia_dl411_art7) | 108_ D.L. 411-2025 Art. 7: propietarios O POSEEDORES voluntary sellers to CEL exonerated (window = decree vigencia 27-sep-2025 → 26-sep-2031; event limbs per SV-SPE-FR-204 by id); formulario-for-cómputo duty EXPRESSLY lifted — the express no-form text distinguishes from FR-418 |

Version-regime notes (D12): FR-074 records the Art. 37 two-vintage regime
(957-2011 config valid through 2025-05-07; 293-2025 config from 2025-05-08 —
pre-cutover periods select the dated table). FR-082 records the SOQ-01
verdict (Art. 42 since D.L. 496-2004 governs; Art. 17 media-tasa is
pre-2004 historical data only). FR-087/FR-091 record the D.L. 969-2024
domestic-only cutover (2024-03-22) inherited from 01-file FR-025. FR-091's
$25,000 carve-out (stamp 18, D.L. 236-2009) and FR-077's $150,000 threshold
are stable unindexed amounts in the current text (OQ-003).

## 6. Acceptance Criteria

- **AC-001:** Given a domiciled natural person with renta imponible
  $6,600.00 for a 2025-06 periodo (current vintage), then the tax = $0
  (Tramo I exempt); given $6,600.01, then tax = 10% × ($6,600.01 −
  $6,600.00) + $212.12 = $212.12 (FR-074).
- **AC-002:** Given renta imponible $8,000.00 liquidated under the
  2025-05-08+ vintage, then tax = 10% × ($8,000.00 − $6,600.00) + $212.12
  = $352.12; given the same base liquidated as a 2024 periodo (957-2011
  vintage), then tax = 10% × ($8,000.00 − $4,064.00) + $212.12 = $605.72
  (FR-074).
- **AC-003:** Given renta imponible $25,000.00, then tax = 30% ×
  ($25,000.00 − $22,857.14) + $3,462.86 = $4,105.72 under both vintages
  (Tramos III/IV identical) (FR-074).
- **AC-004:** Given a non-domiciled sucesión with renta neta o imponible
  $10,000.00, then tax = 30% × $10,000.00 = $3,000.00 flat, no brackets
  (FR-075).
- **AC-005:** Given a persona jurídica whose 2025 gravadas rents total
  $150,000.00 and whose 2026 gravadas rents total $160,000.00, then 2025
  liquidates at 25% ($37,500.00) and 2026 re-evaluates and liquidates at
  30% ($48,000.00) — no rate lock-in (FR-077).
- **AC-006:** Given an entity with $200,000.00 renta imponible of which
  $20,000.00 was subject to retención definitiva, then the ISR computation
  applies 30% to $180,000.00 and the $20,000.00 line is carried as
  excluded-with-evidence (FR-076, FR-077).
- **AC-007:** Given a non-domiciled conjunto event with renta bruta
  $50,000.00, then the per-event tax = 5% × $50,000.00 = $2,500.00 and the
  event liquidation duty is the día hábil siguiente (FR-078; 01-file
  FR-030).
- **AC-008:** Given an eventual sale by a non-merchant of a fixed asset
  acquired without resell intent, then the disposal routes to the
  capital-gain track; given the same good sold by a merchant within its
  giro of compraventa, then the disposal routes to the ordinary track
  (FR-079).
- **AC-009:** Given a good acquired 10-Mar-2023 for $50,000.00 with
  $10,000.00 accumulated admitted depreciation, conservation improvements
  of $5,000.00 and transaction expenses of $1,000.00, sold 15-Jun-2025 for
  $80,000.00, then costo básico = $40,000.00, ganancia de capital =
  $80,000.00 − $40,000.00 − $5,000.00 − $1,000.00 = $34,000.00, holding >
  12 months, tax = 10% × $34,000.00 = $3,400.00 added to the ordinary ISR
  for payment (FR-080, FR-081, FR-082).
- **AC-010:** Given the same good sold 20-Nov-2025 after acquisition on
  10-Jan-2025 (within 12 months), then the ganancia neta de capital is
  summed to the ordinary renta neta imponible and taxed per the subject's
  ordinary track (progressive table or 30%) (FR-082).
- **AC-011:** Given an asset acquired 05-May-2025 and transferred
  20-Sep-2025 (acquired and transferred within the following six months),
  then it counts as possessed the whole year of enajenación for
  year-counting purposes (FR-083).
- **AC-012:** Given an insurer's extraordinary-asset disposal gain of
  $10,000.00, then it is taxed as ordinary renta of the realization
  ejercicio at the Art. 41 rate, not at the 10% capital-gain rate
  (FR-084).
- **AC-013:** Given a 2025 capital loss of $8,000.00 declared on the DGII
  form, 2026 capital gains of $5,000.00 and 2027 capital gains of
  $4,000.00, then 2026 nets to zero gain (tax $0) leaving $3,000.00
  carried, 2027 nets to $1,000.00 taxable at 10% ($100.00) with the loss
  exhausted, and any unused remainder would expire after 2030 (5-year
  window); the ledger blocks applying the loss against ordinary income in
  every year (FR-085).
- **AC-014:** Given an ordinary-income loss of $12,000.00 in 2025 and
  ordinary renta imponible of $30,000.00 in 2026, then the 2026
  liquidation ignores the 2025 loss entirely (no general NOL) (FR-086).
- **AC-015:** Given 100 títulos of species X acquired at $10.00 and
  another 100 at $14.00 (total cost $2,400.00), when 50 are transferred at
  an agreed price of $20.00 with $20.00 expenses and a stock-exchange
  quote of $18.00 at the enajenación date, then weighted-average cost =
  $12.00, floor value = 50 × $18.00 = $900.00 < agreed $1,000.00 (floor
  respected), result = $1,000.00 − $600.00 − $20.00 = $380.00 → 10% =
  $38.00 separate liquidation; if the agreed price were $850.00, then the
  transaction value is booked at the $900.00 floor (FR-087, FR-088).
- **AC-016:** Given a 2025 securities loss of $2,000.00 declared and
  registered, then it offsets only capital gains of títulos or other goods
  obtained in 2025-2030, never ordinary income (FR-089).
- **AC-017:** Given a domiciled natural person holding deposits with an
  average monthly balance of $24,000.00 earning $500.00 interest, then the
  interest is renta no gravable (Art. 4.5 carve-out); given an average
  monthly balance of $26,000.00 earning $600.00 interest with the CT 159
  retention effected, then no declaration is due and the retention is
  definitive payment (FR-091).
- **AC-018:** Given a habitual trader's $120,000.00 sale under a 60-month
  legal credit contract with $30,000.00 total profit and $24,000.00
  collected in year 1, then year 1 recognizes profit proportionally
  ($30,000.00 × 20% = $6,000.00) and the balance defers to later years as
  quotas are collected; given the same sale is a capital-gain transaction,
  then no deferral applies (FR-092).
- **AC-019:** Given a repossessed good with real value $10,000.00,
  unsatisfied quotas of $6,000.00 and rescates pagados of $500.00, then
  the repossession year posts a gain of $3,500.00 (FR-093).
- **AC-020:** Given a $200,000.00 obligación de hacer spanning two years
  with $120,000.00 budgeted costs and 40% of the obra performed in year 1,
  then year 1 recognizes $80,000.00 revenue AND $48,000.00 costs (both
  proportionally) (FR-096).
- **AC-021:** Given an onerosa life annuity of price $100,000.00 with a
  6% legal annual rate paying $12,000.00 per year, then year 1 taxable =
  $6,000.00 (recovery $6,000.00) and year 2 taxable = 6% × $94,000.00 =
  $5,640.00; after full price recovery, the entire payment is taxable
  (FR-097).
- **AC-022:** Given a $10,000.00 interest-free loan between parties, then
  the system presumes legal interest on the credit (rebuttable with
  evidence) and computes the presumed interest as computable renta
  (FR-098).
- **AC-023:** Given a subject with ordinary tax $7,000.00, a >12-month
  capital gain of $34,000.00 and unretained domestic securities rents of
  $1,000.00 in the same ejercicio, then the declaration aggregates
  $7,000.00 + $3,400.00 (10% capital gain) + $100.00 (10% securities)
  = $10,500.00 payable in the four-month window, each track computed
  isolated from the others (FR-101).
- **AC-024:** Given a disposal dated 12-aug-2023 of an inmueble inside
  the Art. 2 perimeter sold by its propietario to CEPA, then the
  disposal is exonerated retroactively (efectos from 8-may-2022): no
  Art. 42 10% liability and no ganancia entry in the annual liquidation;
  where the 2023 ejercicio was already liquidated carrying the 10%, the
  correction recomputes at original-period parameters per D15 (amend the
  2023 liquidation — never a current-period offset) (FR-418).
- **AC-025:** Given a poseedor (not the propietario) voluntarily selling
  an inmueble to CEL on 15-oct-2025 (after 27-sep-2025, inside the
  decree vigencia), then the disposal carries the energia_dl411_art7
  stamp with no ganancia liability AND the no_computation_form flag set
  (express formulario lift) (FR-419).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | **SOQ-01 verdict (recorded):** does Reglamento Art. 17's media-tasa/1.0% mechanism survive for any taxpayer class? Verified against 54_ txt: Art. 42 bears ONLY stamp (14) = D.L. 496-2004 (54_ pp.39-40, txt lines 2186-2215) — the flat 10% + 12-month rule with no media-tasa remnant, later in time than Art. 17 (D.E. 101-1992/8-39-1993 vintage) and of higher hierarchy; Art. 17 (04_ pp.7-8, no repeal marker) carries stale anchors ("tasa del Art. 41"/"la tasa del 25%" for juridical and non-domiciled sucesiones/fideicomisos — now 30% per Art. 37 inc. 2/Art. 41). **Verdict: Ley Art. 42 governs all current periods and classes; Art. 17 = historical pre-2004 method (LB-010).** FR-082 written on Art. 42. Residual: pre-D.L. 496-2004 historical liquidations would need the media-tasa as dated data — only if a customer computes historical periods. Index update flagged. | no | Takumi S2 | resolved |
| OQ-002 | **SOQ-04 verdict (recorded):** does a general pérdida-fiscal (NOL) carryforward exist? Scans run: `rg -n -i "pérdida" sv/.extractions/05_Codigo_Tributario.pdf.txt` → only document/record-loss and sanction contexts (txt lines 337, 3342 Art. 149, 5424/5433, 6461 aviso de pérdida sanction, 6705 contabilidad loss); `04_` txt → Art. 13 repossession loss (line 179) and Art. 14.1 gain/loss determination (line 234); `rg -i "traslado\|arrastre\|pérdidas fiscales"` on both → administrative/document senses only. **Verdict: NO general NOL exists — only capital losses (Art. 14/14-A, 5-year gains-only ledger) and securities netting.** FR-086 states it. Index update flagged. | no | Takumi S2 | resolved |
| OQ-003 | Art. 41's US$150,000 threshold: no indexation mechanism appears anywhere in the corpus (unindexed since D.L. 957-2011 era text); confirm no decree indexes it before freezing the parameter (FR-077). | no | Takumi S2 | open |
| OQ-004 | "Interés legal" rate (life annuity algorithm FR-097, interest presumption FR-098): defined in the Código Civil/Comercio, outside the corpus — the Odoo parameter needs a dated-value rate feed selection (kin to 02-file OQ-003). | no | Takumi + Odoo implementation | open |
| OQ-005 | Securities price-floor feed (FR-088): stock-exchange quotation at enajenación date and emitter book values come from market/emitter sources outside the corpus; feed selection needed for the floor validation. | no | Takumi + Odoo implementation | open |
| OQ-006 | DGII calculation forms (capital gain/loss form per Art. 42; rentas-de-capital form per Art. 14-A; capital-loss declaration form per Art. 14.2): field layouts are DGII administrative specs outside the corpus; system produces computation annexes — conform layout when specs are obtained (fiscal-reporting wave). | no | Takumi S2 (fiscal-reporting wave) | open |
| OQ-007 | SOQ-07 harmonized deposit reading recorded in FR-091 (Art. 4.5 carve-out below $25,000 average monthly balance; Art. 27 10% + CT 159 definitive above): consistent with 02-file OQ-006's note that Reglamento Art. 29's narrower text is stale — Ley governs. Kept as FR note; confirm no DGII circular adds operational detail on the average-balance computation (e.g. per-institution vs aggregated). | no | Takumi S2 | open |
| OQ-008 | Insurer/fianza determination (FR-099) and pre-1992 patrimonio-tax basis rows (FR-081(c)) are sector/legacy data: confirm deferral of detailed FRs to the special-regimes wave (kin to 02-file OQ-004). | no | Takumi S2 (special-regimes wave) | open |
| OQ-009 | Art. 37 vintage straddle: the 2025-05-08 cutover falls inside the 2025 calendario ejercicio — FR-074 selects the vintage by period-close date (2025 annual liquidation → 293-2025 configuration), consistent with the D.E. 10-2025 retention-tables vintage (R19/R20). Confirm no MH rule requires splitting a single annual liquidation across both tables for income earned 1-Jan–7-May-2025; if one exists, FR-074 gains a split mode. | no | Takumi S2 | open |
