# Evidence — 01_Ley_IVA.pdf + 02_Reglamento_IVA.pdf

Sources: `sv/sources/01_Ley_IVA.pdf` (D.L. 296, 1992, reformed), `sv/sources/02_Reglamento_IVA.pdf` (D.E. 83, 1992, reformed)
Read: 2026-08-16 (W3). Full documents (58pp + 11pp).
Citation form: Article + page (PDF) / line (txt).

---

## EVID-047 Ley IVA — scope and taxable events

- **Loc:** Art. 1 (p.2), Arts. 4-8 (pp.2-3), Arts. 14-19 (pp.5-12).
- **Gloss:** IVA applies to transfer/import/internación/export/consumption of bienes muebles corporales (tangible movable goods, Art. 5) and provision/import/internación/export/autoconsumo of services (Arts. 16-17: exhaustive service list a-q incl. leases, professional fees, dietas, membresías, expense reimbursements). Transfer concept broad (Arts. 6-7: permutas, daciones en pago, auction sales, consignments, reorg transfers...). Tax point: goods = document issuance or delivery/payment, whichever first (Art. 8); consignment = when consignatario acts (Art. 8 inc.3). Services = earliest of invoicing, completion, delivery, or payment/credit-to-account even in advance (Art. 18). Territoriality: service taxed where the activity is performed (Art. 19).
- **Candidate CRs:** event model covering goods+services tax points (incl. advance payments); consignment trigger.
- **Topics:** taxation

## EVID-048 Ley IVA — 13% rate; débito/crédito mechanics

- **Loc:** Art. 54 (p.26): "LA TASA DEL IMPUESTO ES EL TRECE POR CIENTO". Art. 55 (débito = rate × base per operation). Art. 57 (p.27): **"Dicha cantidad deberá constar en el Comprobante de Crédito Fiscal... en forma separada del precio o remuneración de la operación"** — CCF must show IVA SEPARATE from price. Art. 64: payable = débito − crédito of the period.
- **Gloss:** CCF (B2B) = net price + separately-stated IVA → **resolves EVID-023 doubt: CCFE prices are NET, IVA added** (structure manual's "(con inclusión de IVA)" wording in ventaGravada for CCF is copy-paste error; the FE's is deliberate). FE (consumer) IVA-inclusive per structure manual — consistent: consumers see final price; CCF separates for crédito-fiscal deduction.
- **Topics:** taxation, e-invoicing

## EVID-049 Ley IVA — base imponible rules

- **Loc:** Arts. 47-53 (pp.23-25).
- **Gloss:** generic base = price/remeueration; cannot be below documented amounts. Specific bases per operation type (Art. 48 a-m: imports = CIF + tariffs + specific consumption taxes, IVA excluded from base). NOT in base: indemnifications, tips, union dues (Art. 49). ADD to base (Art. 51): price adjustments, financing interest incl. late-payment interest, freight/reimbursements (unless in the buyer's name by mandate), accessories (packaging, insurance, maintenance), special taxes; EXCLUDE IVA itself. EXCLUDE from base if already in CCF/ND (Art. 52): general unconditional commercial discounts. FX: exchange rate at tax-point date; later FX diffs not in base but deferred-payment FX diffs are (Art. 53).
- **Candidate CR:** Odoo tax base composition (exclude IVA, include specific taxes & finance charges per rules).
- **Topics:** taxation

## EVID-050 Ley IVA — créditos fiscales: deductibility rules

- **Loc:** Art. 65 (pp.30-31): deductible ONLY for (1) activo realizable goods, (2) fixed-asset goods keeping identity, (3) services in the business (not construction of real estate), (4) general expenses (freight, electricity, phone, water) — ALL must be INDISPENSABLE to the giro and generate taxable/0%/donation/diplomatic output; otherwise documented with FACTURA not CCF. Requirements: original CCF, IVA stated separately, recorded in Libro de Compras (CT Art. 141), inventory register (CT Art. 142). Retentions by agents = crédito fiscal for the agent if declared & paid in the same period (Art. 65, referencing CT Arts. 161-162, 112).
- **Art. 65-A (pp.32-34): non-deductible list** — food (if not food business), vehicles not strictly indispensable + their fuel/repairs/insurance (50% pro-deductible if mixed use), hotels (unless business use shown), plane tickets (unless business travel of verifiable employees), clothing/jewelry (if not the trade), personal/family use goods, alcohol & cigarettes (if not the trade), over-legal-rate IVA transfers, anything not indispensable, real-estate construction inputs, **purchases ≥ 58 minimum wages paid in cash or without formal contract → non-deductible**. Fake/irregular docs never credit: unregistered emitter, unproven operations, de-registered subjects, unauthorized number ranges, docs not in the buyer's name.
- **Candidate CRs:** supplier-document type enforcement (factura vs CCF by deductibility); retention credit timing; 58-minimum-wage cash payment rule; mixed-use 50% vehicle rule.
- **Topics:** taxation

## EVID-051 Ley IVA — pro-rata (Art. 66) detailed mechanics

- **Loc:** Art. 66 (pp.34-36). Factor = gravadas / (gravadas + exentas + no sujetas) per period; **accumulated** recalculation from first pro-rata period through fiscal year end; next-year first month: full-year recalculation redistributes crédito fiscal (sum difference to/against next period's credit). Excluded from denominator: no-subject ops from non-habitual activities without attributable credits, donations to ISR Art.6 institutions, diplomatic sales. No-subject = not within hechos generadores or expressly declared so. Proportion of credit for exempt/no-sujeta ops → cost or expense.
- **Candidate CR:** monthly + annual-true-up proportional credit engine (Odoo: needs custom logic beyond standard fiscal positions).
- **Topics:** taxation

## EVID-052 Ley IVA — carryforward, transfers, fixed assets

- **Loc:** Art. 67 (excess credit carries forward indefinitely), Art. 68 (no refund on cessation), Art. 69 (non-transferable except legal continuation/fusion; not inheritable), Art. 71 (fixed-asset transfers not taxable after 4 years in asset base — before that, taxable), Art. 72 (fixed-asset credit deductible; also repair/remodel credit when not increasing value/life).
- **Topics:** taxation

## EVID-053 Ley IVA — exports 0% + credit refund regime

- **Loc:** Arts. 74-77 (pp.37-40). Exports = definitive transfers for foreign use + services performed in-country for non-residents used exclusively abroad (connection/continuation/termination of services originated abroad = 13%, NOT export). Rate 0% (Art. 75). Export credit deductible against internal débito; excess: carry forward, offset against other taxes, or **reintegro** (refund) on request — DGII must resolve ≤30 days; mixed exporters refund only the export-proportional part, **capped at 13% of export value per period**; unrefunded excess accumulates. Requirements: declaration filed, not omiso, provide purchase/sales detail.
- **Reglamento Arts. 29-30:** Zonas Francas / Recintos Fiscales sales count as EXPORTS (documented via Póliza de Exportación / DM); exporters must keep purchase ledger split (export vs local vs common — common split % by sales monthly).
- **Candidate CRs:** export 0% tax + separate export credit ledger + refund workflow with 13% cap.
- **Topics:** taxation, special-regimes

## EVID-054 Ley IVA — adjustments (devolutions/discounts/rebates)

- **Loc:** Art. 62 (pp.27-29): débito adjustments — subtract returns/annulments/rescissions **within 3 months** of delivery/payment (perishable medicines: up to 2 YEARS with detailed lot registry incl. lote, vencimiento, inventory movements, CCF ref, and NC referencing lote number; destruction acts by health authority) and discounts/rebates already taxed; add price increases, under-transferred débito, excess transferred unless refunded. Via CCF + notas (ref. Art. 100 CT). Art. 63: crédito adjustments mirror for purchases; late-received CCF/ND credit usable up to **3 following periods**; late NC reduces credit in its emission period unless received late → up to 3 periods; beyond that, amend declarations.
- **Candidate CRs:** 3-month return window (medicines 2y w/ lot tracking); 3-period late-document rules — map to Odoo NC/ND period handling.
- **Topics:** taxation, e-invoicing

## EVID-055 Ley IVA — excluded taxpayers (sujetos excluidos)

- **Loc:** Arts. 28-32 (pp.15-16). Exclusion thresholds: < 50,000 colones 12-month transfers AND < 20,000 colones total assets (colon-era values — historical; actual exclusion now administered via NRC/registration; thresholds dated but the REGIME persists: FSEE document type, no crédito fiscal transfer, no IVA recargo on their invoices (Art. 32: excluded subjects' facturas show price WITHOUT any IVA surcharge)). Art. 31: IVA charged to/by them never generates credit. Optional inscription from next Jan 1.
- **Gloss:** FSEE (DTE 14) exists for this population; their facturas must NOT show IVA. Odoo mapping: partner fiscal category drives document type + tax behavior.
- **Topics:** taxation, e-invoicing

## EVID-056 Ley IVA — declaración: monthly, F-07 context

- **Loc:** Art. 93 (monthly calendar period; declaración jurada with gravadas/exentas/no sujetas, débito, crédito, carryover), Art. 94 (**first 10 hábiles of following month**; imports liquidated at customs; import payment constancy = crédito fiscal document). No extensions/installments (Art. 81 inc.2).
- **Topics:** taxation, fiscal-reporting

## EVID-057 Ley IVA — massive repeals to Código Tributario

- **Loc:** ~60 articles DEROGADO (D.L. 230/00): registration (88-92), documents emission/requirements (97-106), accounting records (107), formal obligations (108), entire sanctions regime (109-141), administration/fiscalization (142-164), payment/mora (79-80, 82-87). Effective law: substance (hechos generadores through cálculo) in Ley IVA; procedures/sanctions/documents in Código Tributario.
- **Gloss:** for requirements, document rules live in CT Arts. 110-142 range (per cross-references); next wave (W4 Código Tributario) collects them. Art. 65 refs CT 141 (libro compras), 142/142-A (inventory register); Art. 62/63 ref CT Art. 100 (notas); Art. 65 refs CT 161-162 (retention agents), CT 112 (comprobante de retención).
- **Topics:** taxation (process note for W4)

## EVID-058 Reglamento IVA — operative articles

- **Loc:** Rgto. Arts. 1-30 (surviving). Definitions (Art. 2: exportación, importación/internación definitiva, regímenes aduaneros especiales incl. zonas francas/perfeccionamiento activo); retiro de bienes scope + fuerza mayor proof (Art. 4: inventory annotations, police reports, insurance settlements, legal mermas); service definitions (Arts. 5-7: continuous services, precio alzado, comisión/mandato/consignación); desechos transferers are contributors (Art. 8); fixed-asset docs (Art. 26: Factura or CCF if taxable, else other doc); ZF sales = exports (Art. 29); export credit refund bookkeeping (Art. 30). Inventory credit in duodécimas (Art. 50, transitional 1992 — historical).
- **Gloss:** reglamento is 80% repealed (procedures moved to CT); surviving substance = definitions + export/ZF rules.
- **Topics:** taxation

## Open questions from this pass

1. **OQ:** Art. 28 thresholds in colones — verify current-status (exclusion presumably governed by registration/NRC practices now). Non-blocking for requirements (FSEE regime documented regardless).
2. **OQ:** FOVIAL/COTRANS legal basis NOT in Ley IVA (separate laws; guide 31_ covers mechanics). Confirm whether they form part of IVA base (Art. 51.d suggests specific taxes ARE in base — FOVIAL/COTRANS treatment vs "impuestos especiales" needs the FOVIAL/COTRANS laws; only guide 31_ in sources).
3. **OQ (resolves EVID-023):** DONE — CCFE net price confirmed by Art. 57 (IVA separate from price). FE inclusive confirmed by structure manual. Close the doubt; note in synthesis that ventaGravada CCF wording in manual is erroneous.

## Topic tag summary

taxation: EVID-047..058 (048, 054, 055 also e-invoicing; 053 also special-regimes; 056 also fiscal-reporting)
