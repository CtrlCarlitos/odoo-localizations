# Evidence — 05_Codigo_Tributario.pdf

Source: `sv/sources/05_Codigo_Tributario.pdf` (D.L. 230, 2000, reformed — 313 articles)
Read: 2026-08-16 (W4). Structure mapped; priority + substantive units read in full; procedural bulk (Titles IV-VI detail) skimmed — flagged for follow-up only where localization-relevant.
Citation form: Article + page.

---

## EVID-059 CT — registration: NIT/NRC regime

- **Loc:** Arts. 85-90 (pp.30-31). Art. 86: Registro de Contribuyentes; IVA-excluded subjects per Ley IVA Art. 28 unless opted-in (Art. 30). Change notifications: 5 hábiles for basic-data changes; 15 days for disolución/liquidación/fusión/transformación; 10 hábiles for uniones de personas modifications. Art. 87 basic data: name, establecimientos (nombre comercial), **NIT + NRC**, actividad, notification address (never a PO box, Art. 90), legal rep, addresses of matriz/sucursales/bodegas. Art. 88: NIT/NRC must appear on ALL filings/documents. Art. 89: de-oficio registration.
- **Candidate CR:** partner/company fiscal registration fields (NIT, NRC, activity, category) + DTE emission requires them.
- **Topics:** taxation, e-invoicing

## EVID-060 CT — the document-type system (core)

- **Loc:** Arts. 107-115 (pp.39-50).
  - **Art. 107:** B2B (contribuyente→contribuyente) = **Comprobante de Crédito Fiscal**; consumers = **Factura**; exports = **Factura** (non-substitutable); Ley IVA Arts. 65/65-A cases = FACTURA not CCF (non-deductible purchases). Prohibition of commercial invoices (decomiso). **Factura de Venta Simplificada**: natural persons ≤$50,000/year turnover, only for gravadas/exentas ≤ **$12.00** operations. Tax-point emission duty (Ley IVA Arts. 8/12/18). Computerized systems must **transmit online** each operation to AT servers (e-invoicing legal root).
  - **Art. 108 (Comprobante de Liquidación):** comisionistas/consignatarios/subastadores issue CCF/Factura for third-party-account sales AND a **liquidación to mandantes per period** (monthly summary if partial liquidations); the CL's tax = débito for the mandantes; CCF-numbering rules apply.
  - **Art. 109 (Nota de Remisión):** mandatory when CCF not issued at delivery — covers transit; CCF must follow **within 3 days after the period** of NR emission, referencing it. Also for consignment sends and non-transfer moves.
  - **Art. 110 (NC/ND):** post-CCF adjustments → new CCF or ND (increases) / NC (decreases); must reference the modified CCF; same Art. 114 requirements.
  - **Art. 111 (Factura adjustments):** annul + reissue facturas for decreases/annulments/rescissions (reverse-side annotation of client ID + signature); **3-month window** (matches Ley IVA Art. 62); export adjustments same window with customs docs.
  - **Art. 112 (Comprobante de Retención + Percepción + DCL):** CR content: valor sujeto, monto retenido, date/correlative/type of the subject's document; may be **consolidated monthly per supplier**; CCF requirements minus 114.7-10. Percepción by producers/manufacturers/importers/wholesalers → CCF stating impuesto percibido. **Card-issuer anticipos (162-A) → Documento Contable de Liquidación** with defined fields (correlativo, NIT/NRC both parties, dates, monto sujeto, impuesto percibido, líquido a pagar, triplicate, signature) — matches DTE DCLE structure (EVID-032).
  - **Art. 114 (formal requirements):** CCF: prenumbered talonarios (or per-establishment series), triplicate, emitter/receiver NIT+NRC+giro+address, **separation of gravadas/exentas/no sujetas**, itemization (omittable if prior NR), IVA recargado separately, NR reference, conditions of operation, pie de imprenta. >100,000 colones (~$11,428.57) → names/signatures/ID of deliverer and receiver (**$11,428.57 threshold legal root — EVID-025**). Facturas: duplicate, **IVA included in price** ("Inclusión del impuesto respectivo en el precio" — FE inclusive legal root), ≥ **$200** → client name + NIT/DUI (foreigners: passport/carnet) (**$200 threshold legal root — EVID-017**). NR requirements (título a que se remiten — CAT-025 root). Factura Simplificada requirements. Electronic docs: authorized correlative + range printed by the system.
  - **Art. 115:** registradora-machine tickets as factura substitutes (authorization, audit rolls, Z-reports, online transmission when required).
  - **Art. 115-A:** correlative number assignment is EXCLUSIVE AT power; AT sets which YEAR a document belongs to.
- **Candidate CRs:** complete document-type matrix with legal thresholds; NR→CCF 3-day linkage; online-transmission obligation.
- **Topics:** e-invoicing, taxation

## EVID-061 CT — mandatory books and records

- **Loc:** Arts. 139-143 (pp.73-75). Formal accounting (Art. 139: Código de Comercio-compliant). **Art. 141: Libro/registro de Compras y Ventas** for IVA — daily chronological entries (max 15-day backlog), individualized CCF/NC/ND/facturas-exportación/CR/declaraciones records with series/correlative/supplier NIT/net/tax/total; consumer-facturas by daily ranges per establishment; totals per period signed by contador; books kept at the business. **Art. 142: inventory control registers** (individualized goods); 142-A special inventory cases. Art. 143: tax valuation of inventory.
- **Candidate CR:** Odoo books/reports must reproduce Compras/Ventas ledger content (F-07 annex feeds) — links fiscal-reporting.
- **Topics:** fiscal-reporting, taxation

## EVID-062 CT — retention agents: the full matrix

- **Loc:** Arts. 161-162-B (pp.90-93).
  - **Art. 161:** imports of services from non-residents → the LOCAL acquirer owes IVA, self-withholds via mandamiento.
  - **Art. 162 (IVA retention):** GRANDES CONTRIBUYENTES buying from non-grand taxpayers withhold **1% of price (ex-IVA), ≥$100 operations**, entered same period (10 primeros días hábiles). AT may designate other agents (state organs, municipalities, autonomous entities). Grandes buying from uniones/sociedades de hecho → 1% regardless. **Grandes/medianos buying caña/café/leche/carne or receiving financial-interest/lease/transport/dietas services from UNREGISTERED natural persons → withhold 13%** (full tax; those providers exempt from registration). Retention at tax point; enter even if supplier unpaid. Retention adjustments via NC/ND. **MH lottery prizes: MH retains 13% IVA.**
  - **Art. 162-A (card 2% perception):** card-issuers/administrators perceive **2% anticipation of IVA (ex-IVA amount)** when paying/crediting affiliates; entered first 10 hábiles; affiliate credits it against the period's IVA. (Root of DCLE + ivaPercibido fields.)
  - **Art. 162-B:** courts withhold 13% IVA on interest in ejecutivo judgments.
- **Candidate CRs:** retention/perception engine: agent designation, 1%/$100 grandes rule, 13% unregistered-agro/finance rule, 2% card perception, timing and reporting.
- **Topics:** taxation

## EVID-063 CT — ISR retentions (CT Title III ch. III)

- **Loc:** Arts. 154-160 (pp.83-90). Art. 154 agent concept; retention at payment/acreditamiento. Art. 155 permanent services → tables (payroll). **Aguinaldo exempt from ISR retention** (Dec CT Art. 155 inc.2). Art. 156: services by independent natural persons → **10%** regardless of amount (advances included); seasonal agricultural harvest labor excluded; leases to natural persons 10%. Art. 156-A intangibles: 10% natural persons / 5% entities. Art. 156-B: capital yields/dividend advances 10% (excepted: already-taxed dividends, labor indemnities within ISR limits). Art. 157: courts 10% on judgment interest. Art. 158: **non-residents → 20% definitive** (services from abroad used in-country, intangibles, capital yields; reduced 5% international transport, 5% reinsurers, 10% qualified foreign financing (20% related-party), 5% film/TV rights); ZF/ISL-exempt payers excepted; **158-A: tax-haven subjects → 25%**. Art. 159: financial institutions on deposits (definitive). Art. 160: raffles/prizes.
- **Candidate CRs:** ISR retention matrix in Odoo (10%/20%/25%/5% by partner domicile + service type).
- **Topics:** taxation

## EVID-064 CT — information returns & large-taxpayer reporting

- **Loc:** Art. 123 (annual ISR-retention report by January — name/NIT/base/tax), **Art. 123-A: IVA retentions/perceptions report — first 15 hábiles of following month** (agent report + subject-of-retention counter-report), Art. 124 (dividends/shareholder list by January), **Art. 125: subjects with income ≥ 2,753 minimum wages: semi-annual (Jan & Jul) magnetic/electronic operations report** (providers, clients, third-party collections, creditors, debtors — with doc date/number/kind; also purchases from excluded subjects), Art. 126 (exhibit info/allow control).
- **Candidate CRs:** periodic information returns calendar + data model.
- **Topics:** fiscal-reporting, taxation

## EVID-065 CT — sanctions regime (localization-relevant subset)

- **Loc:** Arts. 226-247 (pp.139-159). Key: **Art. 238**: declaration omission 40% of determined tax (min 1 SMM); late 5%/10%/15% by month tier; incorrect 20%. **Art. 239 (documents)**: omission of emission/delivery **50% of operation per document** (min 2 SMM); non-compliant formal requirements **30%** (min 2 SMM); CCF for food to non-food-business 10%; duplicated numbering 25%; unauthorized registradora 3 SMM; consolidated facturas 50%. **Art. 240**: printing violations 4 SMM. **Art. 242 (records)**: omit books 4 SMM; false entries 9 SMM; **IVA book backlog >15 days: C4,970 + C490/day** capped 9 SMM; falsified docs backing entries 30% of operation (min 9 SMM); books elsewhere 9-16 SMM; refusal to exhibit 0.5% of equity (min 20 SMM). Art. 247: non-entered retentions **75%**; late-entered 50%; late partial 30%; omitted declaration 50%. **Art. 246-A: FOVIAL-specific sanctions** (100% not entered by retaining agent / 50% late / 100% misuse of DIF exclusion / 100% improper refund claims). SMM = salario mínimo mensual (Art. 228: highest of applicable activities... see art. for rule).
- **Candidate CR:** sanctions reference table for compliance module context (awareness-level requirement).
- **Topics:** taxation, fiscal-reporting

## EVID-066 CT — estimation & presumptions

- **Loc:** Art. 199 (missing correlative documents presumed issued & taxed — average-value method; lost-doc use = nonexistent operations, no credit), **Art. 199-A/199-B: market-price estimation** when prices not fidables or off-market (both taxes) — AT power, and taxpayer-side market valuation for ISR; 192-A loan-contract presumptions; 193 inventory-difference presumption.
- **Topics:** taxation

## EVID-067 CT — conservation of records

- **Loc:** Art. 147 (pp.77-78): keep 10 YEARS — books, IVA books, vouchers, retention/perception proofs, declarations, **related-party & tax-haven ops docs, bank/card statements, cancelled cheques**, auditor workpapers. After 4 years may convert to microfilm/optical with external-auditor-certified conversion.
- **Topics:** taxation, fiscal-reporting

## EVID-068 CT — procedure skim (Titles IV-VI)

- **Loc:** Título IV (notifications Arts. 165+, fiscalization 173+: inspection with judicial order off-hours, and others); Título V (deuda, cobro administrativo via Tesorería Art. 267+); Título VI transitorias (Art. 278 old documents 1-year grace; 279 prior laws keep applying; 280 temporal application rules). Details are administrative-procedure; relevant to Odoo only as context (fiscalización windows, verification).
- **Topics:** taxation (context)

## Open questions from this pass

1. **OQ:** Art. 114 CCF duplicate/copies + >C100,000 colones = $11,428.57 — colones conversion fixed at 8.75/USD; confirm the exact current USD statement in DTE regs (structures manual uses $11,428.57 directly — consistent).
2. **OQ:** "Factura de Venta Simplificada" (≤$12) has NO electronic counterpart in CAT-002 (no simplified DTE type) — electronic regime presumably absorbed it; confirm in 06_ guide or normativa DTE (18_).
3. **OQ:** Art. 115-A: AT assigns correlative RANGES and the YEAR a document belongs to → DTE numeroControl resets yearly (Anexo 3) — but transition-period branch codes; check 26_ consola manual for how electronic correlatives are assigned (W5).

## Topic tag summary

taxation: EVID-059..068 · e-invoicing: 059, 060 · fiscal-reporting: 061, 064, 065, 067
