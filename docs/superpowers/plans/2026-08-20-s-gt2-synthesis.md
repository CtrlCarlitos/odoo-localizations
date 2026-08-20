# S-GT2 Synthesis Implementation Plan — gt taxation Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W-GT2 evidence base (EVID-161..265, file keys EV02a..EV02d) — plus the taxation-relevant W-GT4 secondary prints (EV04a/EV04b/EV04c/EV04f, consumed per R46/R55/R20 and GOQ-06/118/119/120) — into the GT Takumi-contract requirements files for taxation (IVA core, pequeño regime, IVA retenciones, ISR trabajo, ISR lucrativas/capital/no-residentes, Código Tributario procedures, reform-chain provenance), with FR numbering `GT-TAX-FR-nnn`, LB citations carrying EVID anchors, Layer split (odoo/saas/shared per S0.5 D1–D6), ACs, and coverage tracking.

**Architecture:** Requirements follow the template (7 fixed sections); Odoo Mapping carries a Layer column; the wave cites the master index (clusters TX1–TX7, GOQ-53..69 + GOQ-01/06 cross-cutting) as its citation spine, and through it the EVID anchors in the four W-GT2 evidence files. Tax statutory layers are split: law (23_/26_/25_/78_) > reglamento (24_/28_/79_) > practice digests (47_, secondary only). Filing-surface mechanics (forms, RetWeb flows, LET, SAT-2390) belong to the later fiscal-reporting wave — S-GT2 owns statutory parameters, regime definitions, computation rules and the retention-rate catalog; F-wave files will cross-reference GT-TAX FR ids. CSV sidecars ship the retention-rate matrix and ISR rate tables as dated data (SV taxation pattern: `sv/requirements/taxation/*.csv`).

**Tech Stack:** Markdown; hand-built CSV sidecars (`iva_retention_rates.csv`, `isr_rates.csv`) with a `_INDEX.md`-style provenance header comment; FR IDs `GT-TAX-FR-nnn` (sequential wave-wide across files, task order; controller assigns ranges at dispatch).

**Spec:** `gt/.extractions/00_MASTER_INDEX.md` (governing lookup: taxation authority order in the preamble, clusters TX1–TX7, GOQ register §C.2 + cross-cutting §C) + `gt/EXTRACTION_PLAN.md` + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D15/D16) + `shared/docs/odoo-localization-guide.md` (D17) + `docs/superpowers/specs/2026-08-18-gt-source-research-design.md` (D-GT1..D-GT10).

## Global Constraints

- Every FR cites ≥1 LB row (Spanish citation + English translation + source file + location + EVID id). No trace → OQ, not FR. EVID anchors come from the master-index cluster rows (file keys EV02a..EV02d, plus EV04a/b/c/f where a cluster row names them); writers verify quotes against the committed evidence files in `gt/.extractions/`, never against memory.
- **Taxation authority order (binding, master index preamble):** ISR = **26_ LAT D-10-2012 consolidated through Dto. 46-2022 (27-09-2022)** governs (28_ AG 213-2013 develops; 47_ = self-disclaimed digest — 26_ > 28_ > 47_, law wins every delta). IVA statutory layer = **23_ D-27-92 historical base ≤ D-10-2012 ONLY — never cite alone**; every current-law row carries "D-27-92, reformado por… (≥ D-4-2019 / D-31-2024 / D-10-2025)"; post-2018 consolidated text still missing (GOQ-01). IVA reglamento = "AG 5-2013, reformado por AG 222-2019". IVA retenciones = **78_ D-20-2006 arts. 1-14 + 79_ AG 425-2006 Título II** ("resolución 2-2010" myth rejected — R23); form numbers NEVER cite these (RetWeb/48_ own them per R46). CT = "D-6-91, consolidated through D-37-2016 + CC annotations to 03-12-2019" — currency qualifier mandatory on every CT citation (GOQ-53); void texts never quoted as law (art. 120 suspension ¶ void per CC 680-2013 → cite 98"A"; R21).
- **Form identities (R46, binding every ISR-form-naming row):** ISR anual lucrativas = **SAT-1411**; asalariados anual = **SAT-1431**; SAT-1371 = ISR no-residentes pago directo mensual; ISR retenciones = **SAT-1331**; SAT-1321 = ISR capital mensual. Cite 48_/RetWeb (EV04a/EV04b) for form identities, never the 47_ digest alone; 47_ practice signals (SAT-1901 "ISR ANTE PATRONO", RETENISR2, etc.) = GOQ-61 practice-layer rows.
- **R20 consumption (mandatory, TX2):** Q150,000 pequeño threshold = D-27-92 arts. 45/46/50 as reformed by D-4-2012 arts. 12/13/18 (vigor 25-Feb-2012, de-oficio migration 1-Apr-2012); never cite LAT/28_ for pequeño thresholds; Q150,000 = D-4-2012-era figure (currency caveat rides GOQ-01).
- **R55/GOQ-06 consumption (mandatory, TX3):** the 5% additions (Pequeño suppliers ≥ Q2,500.01; Agropecuario 5% on total factura) and the 1.5% "valor total" qualifier are recorded as EV04b-sourced dated rows (secondary prints per the fiscal-reporting authority order); the statutory 54-bis text is NOT in corpus → rows stay GOQ-06-open, never frozen as constants. "54 B" (52_) vs "54 BIS" nomenclature rides GOQ-01 (R59).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs a justification line). Taxation defaults: rate/regime/threshold dated data = `shared`; invoice/line computation, retention application, regime flags on journals/partners = `odoo` (thin client) with authoritative cross-validation = `saas` (D2 dual-validation); entitlement windows (devolución channels, agent-calificación status evaluation, prescription clocks) = `saas` with `odoo` surfaces. Declaration/filing generation belongs to the F-wave — cross-reference, never re-derive.
- Dated-instrument regime (D16/D-GT10, cite with D15): every rate, bracket, cap, threshold and regime-schedule FR stores dated rows (valid_from/valid_to + instrument provenance + as-of qualifier per the authority order above); snapshot-on-write; no past-dated application; freeze-at-filing. Rate rows are decree-bound (GOQ-50 pattern), never constants.
- GOQ discipline: the 140-GOQ register is the sole open-questions authority. S-GT2 consumes **GOQ-53..69 plus GOQ-01/06** (owned set) and cites kin ids already consumed by S-GT1/F-wave where they touch taxation (GOQ-13, GOQ-14, GOQ-49, GOQ-50, GOQ-99 statutory half, GOQ-102, GOQ-118, GOQ-119, GOQ-120); affected FRs record the GOQ id in-file (FR note + §7 OQ row, Status open). GOQs are trace-pending, NOT blockers — synthesis proceeds with flagged rows. Waves write resolutions back against GOQ ids in the master index at wave close (controller only). Nothing outside the register may be treated as an open question; genuinely new gaps → flag to controller.
- Rejected myths (never implement, taxation set): "resolución 2-2010" retention basis; IVA "Art. 3-'A'" (real: 8-"A", added D-31-2024, derogated D-10-2025); "ISR anual = SAT-1371" (R46 corrections govern); Q150,000 attributed to LAT (R20); "LAT consolidated ≤2013" (real: through D-46-2022, R24); "ISR = Dto. 26-92" (superseded by D-10-2012); "2236" as current ISR-anual form; "propinas" in LAT art. 68 (47_-only unverified delta — R25); CT art. 120 IVA-suspension ¶ as law (void — R21); IVA retentions as % of base (real: % of the IVA itself, except art. 4 fuel 1.5% on total value — R/OQ13 resolution).
- Files land in `gt/requirements/taxation/` (dir exists via .gitkeep); every file follows the template exactly (7 sections, none deleted; header table with Status `draft`, Authors `GT synthesis wave S-GT2`).
- FR IDs globally unique and stable; cross-file references cite FR IDs (incl. GT-EINV-FR ids where regime↔DTE-type hooks bind — e.g. FPEQ/FCAP ↔ pequeño, FESP ↔ especiales/retenciones complement), never duplicate content. GT-TAX-FR numbering is sequential across the whole wave (Task 2 starts where Task 1 ends, etc.); the controller assigns ranges at dispatch.
- Format precedent: `sv/requirements/taxation/01_isr-framework.md` + `sv/requirements/taxation/isr_brackets.csv` (committed format exemplars — read before writing; do not copy SV substance).
- Per-file working convention (standing): controller spot-verifies 3–5 load-bearing quotes per file by grep against `gt/.extractions/*.evidence.md` before commit; where a writer contradicts a controller brief on a verbatim matter, verify against the evidence file and trust the evidence (gt/HANDOVER §10).
- English prose, Spanish legal terms inline with translation on first use.

---

### Task 1: `gt/requirements/taxation/01_iva-core.md` — IVA régimen general (TX1)

**Files:** Create `gt/requirements/taxation/01_iva-core.md`

**Covers:** cluster TX1 + GOQ-64 (earmark vintage) + GOQ-50 kin + GOQ-01 (currency qualifiers)

**Inputs (exact):**
- Evidence: EV02a `23_24_74_IVA.evidence.md` EVID-162..174, 178, 182..184, 257 (Art. 3 hecho generador + floor; Art. 4 tax point; Art. 7 exenciones objetivas; Arts. 8/9 constancia; 12% + 5pp earmarks + 10 bis derogado; bases 11-13; crédito 15-22; refund channels 23/23-A/24/25; Art. 29 as printed; timing/books/monthly declaration 32-44; vehicle fixed fees 55-57"D"; ÷1.12 arithmetic; prorrateo + no-credit list + book columns; refund floors/export evidence/FEL-gated 25 bis; D-20-2006 Chapter V)
- Sources (verification layer): `gt/.extractions/23_Ley_IVA_27-92.pdf.txt`, `24_Reglamento_IVA_AG_5-2013.pdf.txt`, `74_Ley_IVA_EScolar_Reformas_D10-2025.pdf.txt`
- Master index: TX1 row verbatim; R22/R23; preamble taxation authority order

**Content requirements:**
- FRs: hecho generador taxonomy + minimum-base floor (Art. 3); momento de pago rules incl. periodic-services and fallbacks (Art. 4); tarifa única 12% price-inclusive + earmark split as dated rows with the D-66-2002-era caveat (GOQ-64); exenciones objetivas Art. 7 (15 numerales, key values: menudeo ≤Q100, vivienda Q250,000/80m² + lotes Q120,000/120m²) and subjetivas 8/9 with the constancia mechanics; base imponible 11-13 (discounts/finance/packaging/imports CIF); crédito fiscal 15-22 (vinculación criteria, NIT prerequisite, fixed-asset/ISR interaction, 2-month window + notas registration — GFACE-era documentation phrasing flagged as pre-FEL vintage with FEL cross-ref to GT-EINV files); saldo traslado-not-devolución + the three refund channels (23/23-A trimestral/semestral with 30/60 día-hábil SLA + presumed denial + Fondo IVA + bancarización; 24 optativo CPA-dictamen 10 días; 25 BNG 75%/≤Q500,000 / 60%/>Q500,000 + Q10,000 reglamento floor + FEL-gated electronic 100% regime as a dated GOQ-01-dependent row); débito computation ÷1.12 × 0.12 (24_ Art. 19); prorrateo proportional distribution (24_ Arts. 10/21/22/38-39); no-credit list; used-vehicle/motorcycle FIXED Q fees (Q1,000/500/300/200).
- Citation guard: 23_ rows always carry "D-27-92 (texto ≤ D-10-2012), reformado por…" qualifiers; Art. 29-"A"/8-"A"/25 bis absences stated as GOQ-01 facts; Art. 10 bis printed "Derogado" only.
- Layer: rate/exemption/refund-parameter dated data = shared; invoice line computation + credit registration windows = odoo; refund-entitlement evaluation + bancarización proof handling = saas surfaces.
- Cross-ref: GT-EINV-FR (FEL documentation of credits), Task 2 (pequeño rate-exception), Task 3 (seller-side retention netting Art. 11-kin), F-wave (declaration surfaces).

### Task 2: `gt/requirements/taxation/02_iva-pequeno.md` — Pequeño contribuyente regime (TX2)

**Files:** Create `gt/requirements/taxation/02_iva-pequeno.md`

**Covers:** cluster TX2 + R20 (mandatory) + GOQ-01 (currency) + GOQ-102 kin (rounding) + GOQ-103 kin (deadline shape statutory half)

**Inputs (exact):**
- Evidence: EV02a EVID-175 (Q150,000 ×3 verbatim + Régimen Normal definition), EVID-176 (5% definitivo, Q50, 15 días, constancia, no buyer credit), EVID-185 (24_ Chapter IX retention registry + Q2,500 pequeño floor + card-operator rules), EVID-186 (24_ Arts. 13/55/59: Clientes Varios/CF, single book, monthly computation, exoneration history); EV02c EVID-233 (LAT art. 155 names type only), EVID-238 (28_ art. 34 defers to IVA art. 48); EV04c EVID-432 (55_ fn.1 D-4-2012 attribution — R20 confirmation), EVID-439 (art. 48 whole-month window), EVID-442 (5% gross doctrine)
- Sources: `23_Ley_IVA_27-92.pdf.txt` arts. 44-50, `24_Reglamento_IVA_AG_5-2013.pdf.txt` arts. 13/22.5/38/49/55/59
- Master index: TX2 row verbatim; R20/R28; GOQ-01/06 rows

**Content requirements:**
- FRs: threshold Q150,000 annual gross with R20 provenance (entry 45 / switch 46 / exit 50 + de-oficio migration + prior-year excess rule); 5% pago definitivo on monthly gross; retention-by-agents track = PAGO DEFINITIVO at 5% of total invoiced + constancia + remission first 15 días + mandatory monthly filing even if fully withheld; no-retention fallback self-pay mes calendario siguiente (LIVA art. 48 — no fixed day/hábiles printed; GOQ-103 statutory half answered here); Q50 invoice floor + daily consolidated "Clientes Varios"/NIT CF (R28 complementary framings both recorded); single compras-y-ventas book (statutory hook; mechanics → F-wave); buyer side: NO crédito fiscal on pequeño invoices, exempt-entity buyers pay in full; monthly liability = (gross × 5%) − retentions soportadas; ISR/ISO relief bundle; LAT art. 155 guard (document type only, never thresholds — R20 guard row).
- Rounding: no statutory rounding rule in corpus — record GOQ-102 kin note; never copy the 55_ Q179.00 defect (R56).
- Layer: regime dated data = shared; regime flag on journal/partner + invoice legend "No genera derecho a crédito fiscal" = odoo; threshold-monitoring/exit evaluation = saas with odoo surfaces.
- Cross-ref: Task 3 (the pequeño 5% retention row), GT-EINV FPEQ/FCAP FRs, F3-wave files (libro/2046 mechanics).

### Task 3: `gt/requirements/taxation/03_iva-retenciones.md` + `iva_retention_rates.csv` — IVA retention matrix (TX3)

**Files:** Create `gt/requirements/taxation/03_iva-retenciones.md`, `gt/requirements/taxation/iva_retention_rates.csv`

**Covers:** cluster TX3 + R55/GOQ-06 (mandatory) + GOQ-65/66/67 + GOQ-118/119 (in-corpus verification + modeling call) + R23/R26

**Inputs (exact):**
- Evidence: EV02d `78_79_Retenciones_IVA.evidence.md` EVID-246..265 (full matrix: identity/split vigencia; exporter 65-agro/15/65-D.29-89 + Q100k FOB + 15 días hábiles; sector público 25% + Q30,000 + municipalidades excepted; card operators 15% + 85% afiliado; fuel 1.5% VALOR TOTAL; especiales/otros 15%; obligations chassis + even-zero DJ + constancia fields; seller same-period booking + 2-year remanente special account; agent-to-agent abstention; Q2,500 de minimis; AG 425-2006 Título II: carné, Sistema computes %, constancia 10 fields, agent lifecycle, 2-year rule, FOB averaging, negative silence); EV02b EVID-215 (CT agent capacity); EV02a EVID-185 (24_ Chapter IX registry anchor); EV04b `49-54_RetWeb_agentes.evidence.md` EVID-390/391 (R55: PC 5% ≥Q2,500.01; agro 5% total factura; de minimis exceptions), EVID-407 (sector público 25/5/5 by provider regime), EVID-410/411 (line model + card Pago Total/Parcial mechanic), EVID-408 ("art. 54 B" statutory-agent path); EV04f `64-65_Criterios.evidence.md` EVID-496 (dualidad + Sistema de Retenciones + art. 4), EVID-493/494 (criterio's confirming rate table)
- Sources: `78_Fortalecimiento_D20-2006.pdf.txt`, `79_Fortalecimiento_Reglamento_AG_425-2006.pdf.txt` (GOQ-118: re-verify art. 4 contents here)
- Master index: TX3 row verbatim; R23/R26/R47/R54/R55/R59; GOQ-06/65/66/67/118/119 rows

**Content requirements:**
- FRs: the six agent classes with rates as % OF THE IVA (exportadores habituales incl. Q100,000/month FOB + aviso; sector público 25% + Q30,000 abstention + municipalidades exception; operadoras de tarjeta 15% + 85% afiliado liability + exclusivity + monthly consolidated constancia; combustibles-by-card 1.5% sobre el VALOR TOTAL as the sole base exception; especiales 15%; otros 15% voluntary/30-día-hábil resolution + negative silence); de minimis Q2,500 per operation with the boundary-edge flag; agent-to-agent abstention (carné + Web verification); seller mechanics (same-period suffered-retention booking, subtract from liability, roll-forward, 2-year stranded remanente → restricted account); enterar primeros 15 días hábiles (R26 same-window ruling) + even-zero monthly DJ + per-provider constancia fields; **R55 additions as separate EV04b-sourced dated rows (5% pequeño ≥Q2,500.01; 5% agro on total factura; sector-público provider-regime split 25/5/5; card Pago Total/Parcial [sic] exit mechanics) marked "secondary print — statutory text pending GOQ-01/06, never frozen"**; GOQ-118 resolution attempt (79_ art. 4 contents verified in-corpus — record the finding); GOQ-119 modeling call (dualidad: multi-quality agents retain under EACH quality; operative % per factura from SAT's Sistema de Retenciones configuration + prorrateo for mixed invoices — model as configuration-driven dated data, not hard-coded); Q30,000 interplay flag only, never modeled as linked (GOQ-66); fuel-base + import-side absence notes (GOQ-67); deadline variants: statutory 15 días hábiles; the SAT-2320 agro 10-día form variant recorded as RetWeb-layer with instrument not in corpus (R47 deferral answer + GOQ-01 note; form identities cite 48_/RetWeb per R46).
- `iva_retention_rates.csv`: one row per (agent class × rate × base qualifier × valid_from + provenance + source EVID + status[statutory|secondary-print-pending]); header comment documents authority order + R55 caveat; hand-built from evidence (SV `withholding_tables.csv` pattern).
- Layer: retention-rate matrix + agent-calificación status = shared dated data; retention computation at invoice/payment + constancia issuance surfaces = odoo; DJ/enterar generation = F-wave cross-ref; Sistema-de-Retenciones % resolution = saas config service.
- Cross-ref: Task 1 (seller-side netting), Task 2 (pequeño 5% track), Task 5 (facturas especiales ISR side), F2-wave files (RetWeb mechanics/forms), GT-EINV FESP/RETENC complement FRs.

### Task 4: `gt/requirements/taxation/04_isr-trabajo.md` — ISR rentas del trabajo (TX4)

**Files:** Create `gt/requirements/taxation/04_isr-trabajo.md`

**Covers:** cluster TX4 + GOQ-58/60/61 + R46 (form identities) + GOQ-99 statutory half + GOQ-04 kin (rates are payroll-side but the LAT projection mechanics land here)

**Inputs (exact):**
- Evidence: EV02c `26_28_47_LAT_ISR.evidence.md` EVID-226 (arts. 68/70 exenciones incl. aguinaldo/bono-14 100%-monthly caps + indemnización exempt), EVID-227 (art. 72 Q48,000/Q12,000/Q60,000 + January planilla), EVID-228 (art. 73 bracket table verbatim + art. 74 annual period), EVID-229 (arts. 75-82 projection/12 + constancias + 10-day pay + February refund + delegation), EVID-239 (28_ arts. 67-73: Q48,000-only projection, no pro-rata, planilla field schema, January reconciliation, refunds in cuotas), EVID-219/220 (deduction↔retention gating), EVID-243 (47_ numeric cross-check ALL match), EVID-244 (47_ deltas: "propinas" R25 guard, sanctions block → CT/CP), EVID-245 (practice signals SAT-1901/1331/RETENISR2/Planilla IVA-FEL/BancaSAT)
- Sources: `26_LAT_10-2012.pdf.txt` Libro I arts. 68-82, `28_Reglamento_LAT_AG_213-2013.pdf.txt` arts. 67-73, `47_SAT_Patronos_Retencion_ISR_2025.pdf.txt` (secondary)
- Master index: TX4 row verbatim; R25/R46; GOQ-58/60/61 rows

**Content requirements:**
- FRs: hecho generador art. 68 (en dinero, relación de dependencia; the 47_ "propinas" delta recorded as R25-unverified); exenciones art. 70 (aguinaldo + bono 14 each ≤100% one ordinary monthly salary — cross-ref P3 wave for the bonus laws themselves; indemnización fully exempt; pensions removed by 14-2013); deductions art. 72 as dated rows (Q48,000 personal + Q12,000 IVA-credit via January planilla first 10 días hábiles + IGSS/IPM/previsión worker shares + donaciones 5% + no-surrender life insurance); rate table art. 73 (5% ≤Q300,000; Q15,000 + 7% over) as the single annual scale for withholding AND liquidation; projection algorithm arts. 75-82 (annual projection − Q48,000-only − estimated IGSS/IPM → scale → ÷12; mid-year start remaining-months; recalc without worker declaration; multi-employer highest-patrono rule; partial-year workers keep FULL Q48,000 no pro-rata; constancia ≤10 días + final constancia 10 días hábiles; DJ + pago first 10 días of following month even if omitted; refund ≤ first 2 months; worker DJ ≤ first 3 months; 28_ refunds-in-cuotas).
- GOQ-99 statutory half: LAT/28_ print "días hábiles" or plain "días" per deadline — transcribe exactly per instrument, note the RetWeb constancia-delivery asymmetry (R54) as F-wave cross-ref.
- Practice layer (GOQ-61): SAT-1901 (PROYECTADA/DEFINITIVA) + SAT-1331 monthly retenciones DJ as 47_-sourced practice rows with R46 identity guard (ISR retenciones = SAT-1331; asalariados anual = SAT-1431) — never cite 47_ as law.
- Layer: bracket/cap dated data = shared; payroll withholding computation + constancia = odoo (payroll engine, cross-ref P-wave); DJ surfaces = F-wave cross-ref.
- Cross-ref: P-wave (bonus laws, IGSS shares feeding the projection), Task 5 (single art. 73 scale reuse), Task 6 (CT 94.7/94.18 sanction hooks), F-wave (RETENISR/1901 mechanics).

### Task 5: `gt/requirements/taxation/05_isr-lucrativas-capital.md` + `isr_rates.csv` — ISR lucrativas/capital/no-residentes (TX5)

**Files:** Create `gt/requirements/taxation/05_isr-lucrativas-capital.md`, `gt/requirements/taxation/isr_rates.csv`

**Covers:** cluster TX5 + GOQ-58/59 + R46 kin (form identities in annual/quarterly rows)

**Inputs (exact):**
- Evidence: EV02c EVID-217 (taxonomy + D-26-92 derogation + vigencia 1-Jan-2013), EVID-218 (exenciones 8/11/87), EVID-219 (art. 21 caps matrix), EVID-220 (arts. 23-24 gating + thin cap JM×3×equity), EVID-221 (depreciation 5-33.33% line-recta table), EVID-222 (Utilidades 25%/quarterly/legend/inventory Jan+Jul), EVID-223 (transitional 31/28/25 + 6/7), EVID-224 (Opcional 5%/7% Q30,000 + Q2,500 floor + retention collection), EVID-225 (lifecycle switch December-only), EVID-230 (capital bases 30%/15%), EVID-231 (10%/5% + 2-year capital losses + 10-day cycles), EVID-232 (no-resident matrix 5/3/10/15/25), EVID-234 (facturas especiales 5% + Q30,000/month presumption), EVID-235 (NO multi-year NOL absence finding), EVID-240 (28_ arts. 74-89: no-DJ-when-retained, capital-loss fencing, transportistas, Banguat FX, Q2,500 amnesty), EVID-241 (28_ quarterly accumulation, depreciation floor, donations, construction annexes)
- Sources: `26_LAT_10-2012.pdf.txt` arts. 1-107/172-174, `28_Reglamento_LAT_AG_213-2013.pdf.txt` arts. 7-9/19/24-27/34-35/74-89
- Master index: TX5 row verbatim; R24/R25/R46; GOQ-58/59/60 rows

**Content requirements:**
- FRs: taxonomy + régime default (Utilidades when silent) + December-switch lifecycle; Utilidades 25% annual + quarterly payments (real closings OR 8%-of-gross presumptive with exclusions; Q4 with annual DJ first 3 months) + invoice legend "sujeto a pagos trimestrales" + inventory reporting Jan+Jul + quarterly-loss YTD accumulation + **NO multi-year NOL carryforward absence finding as an explicit negative-FR** (capital losses 2 years same-nature only); Opcional Simplificado monthly 5% ≤Q30,000 / Q1,500 + 7% over on gross, collected THROUGH retention by payers + Q2,500 per-operation floor + 5-day constancia + 10-day enter + monthly DJ + annual informative DJ; deductions art. 21 caps matrix as dated rows (sueldos socios/parientes 10%; aguinaldo/bono 14 100% monthly each; IGSS/IRTRA/INTECAP patronal fully; indemnizaciones 8.33%; incobrables 3%; donaciones 5%/Q500,000; asesoría 5%; viáticos 3%; regalías 5%; organización 5 cuotas); no-deducibles art. 23 (incl. unpaid-retention gating + no-IGSS-planilla gating cross-ref EV04f EVID-498/499 as interpretive layer); thin cap art. 24; depreciation table + land-never + 70% building presumption + irrevocable lower rates; capital 10% definitive + dividends 5% definitive + 30% presumed expenses (70% base) + transaction costs ≤15% + SIB carve-out + 2-year capital-loss fencing; no-residentes matrix 5/3/10/15/25 as dated rows; facturas especiales ISR 5% definitive (cross-lock 23_ Art. 52/52"A" IVA side — EVID-177) + Q30,000/month presumption; dieta retention recorded GOQ-60-open.
- `isr_rates.csv`: one row per (régimen/category × bracket/rate × valid_from + provenance + EVID); includes transitional 31/28/25 rows with valid_to; SV `isr_brackets.csv` pattern.
- Layer: rates/caps dated data = shared; régime selection on company + quarterly-payment computation + legends = odoo; no-resident/factura-especial retention application = odoo with saas validation; annual/quarterly DJ surfaces = F-wave cross-ref (form identities per R46: anual lucrativas = SAT-1411; capital mensual = SAT-1321; no-residentes mensual = SAT-1371).
- Cross-ref: Task 3 (facturas especiales dual retention), Task 4 (art. 73 scale reuse), Task 6 (sanctions/gating), SR-wave (exemption windows are per-beneficiary — never global), F-wave.

### Task 6: `gt/requirements/taxation/06_ct-procedures.md` — Código Tributario: registry, prescription, sanctions, fiscalización (TX6)

**Files:** Create `gt/requirements/taxation/06_ct-procedures.md`

**Covers:** cluster TX6 + GOQ-53/54/55/56/57 + GOQ-120 (record finding) + R21 guard

**Inputs (exact):**
- Evidence: EV02b `25_Codigo_Tributario.evidence.md` EVID-191..215 (identity/dated rows; reform-tail authority; fuentes hierarchy; 98"A".2 FEL hook; inscription art. 120 + unconstitutional ¶ + annual ratification; NIT duties no structure rules; pre-FEL document hooks; e-filing 105; rectification 104/106; resarcitorio mechanism; payment mechanics; de-minimis/solvencia; prescription-anchored retention; books 2-month rule; systems audit; e-means 125/125"A"/125"B"; art. 94 multa table; mora/omisión; cierre/recidivism; prescription 4/8 + interruptions; fiscalización; procedure + recursos clocks; agents 28/29/41)
- Sources: `25_Codigo_Tributario_6-91.pdf.txt`
- Master index: TX6 row verbatim; R21/R29; GOQ-53..57/120 rows

**Content requirements:**
- FRs: fuentes hierarchy note (sanctions/procedures/prescription reserve-of-law); registry (inscription BEFORE activity, fields, ex-officio, 30-day change/cese notices, NIT on all filings/documents, annual ratification + >50% activity rule; NO NIT structure/check-digit in CT — GOQ-54 pointer, kin GOQ-49); prescription 4/8 años + 9-event interruption catalog + sanctions 5 años + paying-prescribed-debt-waiver; mora 0.0005/day; omisión 100%; retained-not-entered 100% (50% pre-requirement halving); art. 94 multa table as dated rows (every Q value with its numeral; art. 94.19 void note); cierre temporal 10-20 días + judicial procedure + commutation ≤10% floor Q10,000 (pequeño Q5,000); reincidencia +50% capped; resarcitorio = JM variable rate external (GOQ-55 — never hard-code); fiscalización powers incl. systems audit + e-means arts. 125 family; rectification/rebajas; recursos clocks; retention-agent capacity arts. 28/29/41; FEL hooks: 98"A".2 verbatim + the art. 120 suspension trap (cite 98"A" NEVER 120 — R21); books 2-month rule + 112"A" prescription-anchored retention (archive matrix owned by C-wave GOQ-124 — cross-ref); art. 85.4 [sic] sense note (GOQ-56); pre-FEL impresores conditional note (GOQ-57); CT-91 vs 94.7 divergence recorded verbatim with GOQ-120 open (no in-corpus resolution possible — 25_ is the consolidated CT).
- Layer: sanction/prescription dated data + clocks = shared; NIT/registry fields on partner/company = odoo; prescription-clock computation + sanction evaluation = saas with odoo surfaces; resarcitorio rate ingestion = saas external-data service (GOQ-55).
- Cross-ref: Tasks 3/4/5 (all retention sanction/deadline hooks), GT-EINV 98"A".2 anchor, F-wave (procedures/archive), C-wave (books/112"A").

### Task 7: `gt/requirements/taxation/07_reform-chain-provenance.md` — dated-instrument discipline (TX7)

**Files:** Create `gt/requirements/taxation/07_reform-chain-provenance.md`

**Covers:** cluster TX7 + GOQ-62/63/68/69 + GOQ-01/13 kin — the provenance layer as machine-actionable requirements (D16 instantiation for taxation)

**Inputs (exact):**
- Evidence: EV02a EVID-161 (23_ identity + cutoff + absent articles), EVID-179 (transitorios/derogatorias tail + per-reform vigencia strings), EVID-180/181 (24_ identity + AG 222-2019 tail + FEL cluster 28 bis/29 ¶4/36 bis-ter), EVID-187/188/189/190 (D-10-2025 identity/urgencia/vigencia + Art. 1 deroga 8-"A" + LAE + budget); EV02c EVID-216 (26_ stamps through 46-2022), EVID-236 (28_ identity), EVID-242 (47_ digest provenance); EV02d EVID-246 (78_ dates + split vigencia), EVID-256 (derogations + reglamento mandate), EVID-260 (79_ identity + AG 125-2022 stamp); EV02b EVID-192 (CT authority table)
- Sources: all six taxation source txt files (verification layer)
- Master index: TX7 row verbatim; R19..R23/R26/R59; GOQ-01/13/62/63/68/69 rows

**Content requirements:**
- FRs: per-instrument consolidation-cutoff register as dated rows (23_ ≤ D-10-2012 + absent-articles inventory 3-"A"/7-"A"/8-"A"/25 bis/29-"A"; 24_ AG 5-2013 + AG 222-2019 tail exactly; 26_ through D-46-2022; 28_ AG 167-2014 only; 78_/79_ split vigencia + DCA+8d articles; 25_ D-37-2016 + CC 03-12-2019); currency-qualifier FR (every citation emitted by the system carries its cutoff); D-10-2025 delta register (derogates 8-"A" added D-31-2024 art. 13; LAE art. 16 ¶; vigencia = publication 4-Nov-2025; OCR-noise values not citable — GOQ-62); **GOQ-68 in-corpus action: verify whether 24_ art. 29 ¶6 prints the AG 125-2022 FEL-transition text; record the finding + the acquisition need**; "Mayo 8 de 1992" unlabelled-string rule (GOQ-63); citation-guard FRs (23_ never alone; ISR = D-10-2012 not 26-92; form numbers cite 48_/RetWeb; myths list enforced as validation rules on requirement data); 74_ title "168-2017" [sic] defect ledger.
- Layer: provenance register = shared (governs all dated-row emission); citation validation = saas CI gate on requirements data (kin to catalogs governance pattern).
- Cross-ref: every S-GT2 file (the qualifiers this file defines), GT-CAT governance file (drift/policy kin), F-wave (dated-validity strings from 48_).

### Task 8: `00_index.md` + COVERAGE/README updates + master-index GOQ write-back (controller)

**Files:**
- Create: `gt/requirements/taxation/00_index.md`
- Modify: `gt/requirements/COVERAGE.md` (taxation source rows cited/pending re-map), `gt/requirements/README.md` (taxation row → In review)
- Modify: `gt/.extractions/00_MASTER_INDEX.md` (GOQ write-back annotations ONLY at wave close, controller-executed; synthesis-order line updated: S-GT2 COMPLETE)

**Content requirements:**
- `00_index.md` (S-GT1 pattern): file list with FR-id ranges per file (assigned at dispatch), LB/AC/OQ totals, per-file scope sentences, taxation authority-order summary, GOQ coverage check — every id in **GOQ-53..69 + GOQ-01/06** consumed in ≥1 §7 row or explicitly not-applicable with reason; kin ids (GOQ-13/14/49/50/99/102/118/119/120) listed with their owning file.
- COVERAGE: taxation-owned registry rows (23_/24_/25_/26_/28_/47_/74_/78_/79_ + EV04a/b/c/f secondary citations) → cited; remaining F/P/C/SR rows stay pending with owning S-wave named.
- Master-index write-back: for each consumed GOQ append "(cited S-GT2 <file> FR-nnn)" style annotation; GOQ-118 records the verification finding; R47 deferral answer noted where TX3 states it.
- Session close: update `gt/HANDOVER.md` (§1 state, §5 addenda section, §9 next actions, §10 session addenda) + `gt/EXTRACTION_PLAN.md` log entry; commit per repo convention (short imperative, no emojis).

---

## Execution notes (controller)

- Dispatch order: Tasks 1→2→…→7 sequential (FR numbering is wave-sequential); Task 8 last (needs final ranges). Tasks 1–7 are subagent-writable; Task 8 is controller work except the index/COVERAGE bodies which may be delegated after files freeze.
- Each dispatched brief carries: the task text above + Global Constraints + assigned FR range + the relevant master-index cluster rows verbatim (TX1–TX7 + the GOQ rows + R19..R26/R46/R47/R54..R56/R59/R20/R55) + format-exemplar paths (`sv/requirements/taxation/01_isr-framework.md`, `sv/requirements/taxation/isr_brackets.csv`). Agents read evidence files directly (`gt/.extractions/*.evidence.md` — committed) and verify quotes against source txt layers (`gt/.extractions/*_*.pdf.txt`).
- Verification per file (controller): 3–5 load-bearing quotes grep-checked verbatim against evidence files; template 7-section completeness; FR/LB/OQ id hygiene; Layer column non-blank; GOQ id set matches the register. Known failure modes: agents returning empty final messages while files were written — `ls` + `git log` before re-dispatching; finisher pattern (verify existing artifact → commit → report) when an agent dies post-write.
- Commit cadence: plan doc first commit; then one commit per task (or 2–3 small related files); HANDOVER/log at session close. Never commit outside the `gt-research` worktree.
- Estimated FR budget (controller adjusts at dispatch): T1 ~40 · T2 ~28 · T3 ~42 · T4 ~36 · T5 ~46 · T6 ~40 · T7 ~22 ≈ 254 total.
