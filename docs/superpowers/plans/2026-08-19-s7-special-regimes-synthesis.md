# S7 Synthesis Implementation Plan — sv special-regimes Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W13 special-regimes evidence base (EVID-251..274, master-index clusters SR1–SR8 + SOQ-30..45) into Takumi-contract requirements files under `sv/requirements/special-regimes/`, with FR numbering `SV-SPE-FR-nnn`, LB citations to the W13 sources under the special-regimes authority order, per-beneficiary D15 exemption schedules as the wave's spine, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S7-A (SR1–SR8) is the synthesis worklist and its SOQ-30..45 register is binding. The layering is regime-shaped: the beneficiary/qualification framework (SR1) admits a company into a regime; ZF/DPA exemption schedules (SR2) and the LSI regime (SR3) own the dated benefit rows; customs clocks (SR4) time the goods; the TAN/IVA interface (SR5) routes regime transactions into the tax engine; customs declarations (SR6) model the DUCA/teledespacho surface; obligations & DGA-facing reporting (SR7) carry the compliance/sanction layer; FOVIAL/COTRANS (SR8) is the quantity-contribution closer. Cross-topic interfaces cite FR IDs of earlier waves by id, never re-derived (SV-TAX-FR-174 certificado route; fiscal-reporting annex-3 tipo-11 + días-hábiles engine; payroll SMM sidecar; e-invoicing NRE/FEX/FCF doc types; commercial-legal retention matrix).

**Tech Stack:** Markdown; FR IDs `SV-SPE-FR-nnn` (new prefix `SPE`; wave-sequential across the topic's files, no gaps, no renumbering). CSV sidecars only if a printed data table warrants one (candidate: exemption-ladder seed rows — evaluate at T2; default none).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S7-A + special-regimes authority-order paragraph + SOQ-30..45 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12 + **D15 as-of doctrine + D16 mechanics canon**) + D18/D19 (mid-year go-live + cut-over; recorded in the doc + go-live-readiness.md) + `sv/HANDOVER.md` (country memory).

**Evidence inputs (read-only for implementers):**
- `sv/.extractions/12_Ley_Zonas_Francas.evidence.md` (EV12, EVID-251..258 — SR1/SR2/SR4/SR5/SR7)
- `sv/.extractions/14_17b_Servicios_Internacionales.evidence.md` (EV14, EVID-259..267 — SR1/SR3/SR4/SR5/SR7)
- `sv/.extractions/13_42_43_74_Aduanas.evidence.md` (EV13, EVID-268..273 — SR1 frame/SR4/SR6/SR7)
- `sv/.extractions/31_Guia_FOVIAL_COTRANS.evidence.md` (EV31, EVID-274 — SR8)
- `sv/requirements/special-regimes/00_index.md` (wave-prep stub: input inventory + W11 by-id pointers — binding input)
- Extraction txts when a verbatim quote is abbreviated in evidence (S3 ruling 25 applies): `12_Ley_Zonas_Francas.pdf.txt`, `14_Ley_Servicios_Internacionales.pdf.txt`, `17b_Reglamento_Servicios_Internacionales.pdf.txt`, `13_Ley_Organica_Aduanas.pdf.txt`, `74_Ley_Simplificacion_Aduanera_D529.pdf.txt`, `43_DUCA_Instructivo_COMIECO.pdf.txt`.

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article). No trace → OQ, not FR.
- **Authority rule (S7, binding):** ZF = **12_** (D.L. 405-1998 consolidated through D.L. 318-2013; content title "Ley de Zonas Francas Industriales y de Comercialización"); LSI = **14_** (D.L. 431-2007) + **17b_** (Reglamento D. 131-2008; Art. 22 caps are reglamento-level dated parameters); DGA frame = **13_** (D. 903); customs chassis = **74_** (D. 529); DUCA = **43_** (COMIECO Res. 409-2018) + **42_** (SIECA/Panamá 2025 operational note); FOVIAL = **31_** (DGII guide = secondary authority citing D.L. 208-2000 Art. 26 as reformed D.L. 597-2001; law text NOT in corpus — SOQ-39 provenance chain). **Every regime LB carries the SOQ-30 verification note** (all consolidations end 2012-2013; article text cited as printed).
- **D15 is the wave's spine (binding, §5 ruling 42):** exemption schedules/values are ALWAYS per-beneficiary dated rows (`valid_from/valid_to`) keyed by acuerdo D.O. date + location track (metro/fuera) + role, resolved as-of the domain anchor (fiscal year for exemption percentages; DM acceptance for clocks; transaction date for tasa/valuation values) and snapshotted on the record — **never global constants**. The ZF 60/40 phase-down ladders, DPA 10/15y tracks, LSI indefinite-until-cessation rows, $18 tasa, presumed flete/seguro percentages, 50/40/30 caps, and SMM-priced sanctions are ALL dated config rows with instrument provenance.
- **D16/D18/D19:** hard gates and dated mechanics apply (no override of regime validity; `is_historical` ingestion for regime history; posting tiers at cut-over — a ZF company migrating mid-year keeps its ladder computation from imported rows).
- **Regime-distinctness invariants (never unify):** ZF/DPA admisión temporal 12 MESES IMPRORROGABLES (12_ Art. 22) vs LSI 24 MESES PRORROGABLES +1y (14_ Art. 33); ZF Art. 25 TAN-sales rule (0% + Ley IVA 76/77) vs LSI Art. 26 (exportación definitiva, Ley IVA 75-77); ZF sanction ladder (3/5 SMM) vs LSI (30/40 SMM + 3rd-grave revocation); usuario ladders (15/20y) vs DPA (10/15y) vs desarrollista flat (10/15y).
- **Value discipline:** $500k/$800k/$100k/$150k/$10M/$3M requisito amounts, $200/$3,000 courier bands, $18 tasa, 1.25/1.50/10% presumed values, 50/40/30 caps, 90% staffing quota, 5y/12m/6m/2m/20-day clocks = code-text values cited as printed; SMM "de mayor cuantía" sanctions = config default highest-16_-sector with SOQ-33 OQ; NOTHING arithmetic-derived; config-gaps (DGA reference flete values, DUCA manual field obligations, LESIA sanctions) ship NO defaults with OQs.
- **Pointer-only surfaces (zero invented mechanics — SAS-statute discipline):** F-11 v20 special-regime declaration + certificado anexo (print not acquired — cite SV-TAX-FR-174 + SOQ-41-family OQ); D.L. 598-2020 + EVID-167 tail laws (acquisition candidates — stub pointers only); LESIA sanction consequences (SOQ-32); Reglamento General ZF trámite formats (SOQ-31); DUCA mandatory-field manual (SOQ-36).
- **Cross-topic discipline (cite FR IDs, never duplicate):** taxation/01 SV-TAX-FR-174 (Quincena-25 ZF/DPA/LSI certificado route `certificado_zf_dpa_lsi` — the S7 consumer interface); taxation/05 (dividend 5% + earnings register interplay); fiscal-reporting/03 (annex-3 tipo-11 ZF/DPA bucket); fiscal-reporting/08 (días-hábiles engine SV-FREP-FR-202..204 consumed by every días-hábiles clock); payroll/02 (SMM dated sidecar for sanction units); payroll/05-06 (SS-solvency records); e-invoicing (NRE/nota-de-remisión, FCF/CCF doc rules, FEX export pairing — by id); commercial-legal/02 §3.7 (retention matrix — customs 5y row is an update-by-note, never a restatement); taxation IVA-core wave pointer for FOVIAL chain design (SOQ-40) + 1.5%/1% retention cross-check (SOQ-37).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Special-regimes is Odoo-native (res.company regime profile, account.tax dated rows, stock moves/locations for clocks, account.move for DUCA mirroring) — default `odoo`; SIECA/portal transmissions = `odoo` export + external-interface assumption note.
- English prose, Spanish legal terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; never silently dropped. In-file OQ numbering per file (OQ-1..n), S4+ precedent.
- **FR numbering contract:** wave-sequential `SV-SPE-FR-001..` across files in task order (T1 opens 001; each later task continues from the previous file's last used number; NO gaps, no renumbering). Tasks therefore execute STRICTLY IN ORDER (S4/S5 precedent). The index task (T9) verifies continuity.
- Files land in `sv/requirements/special-regimes/` following the template exactly (7 sections, none deleted).
- **Process:** execute in `.worktrees/sv` on branch `sv-research` (FIRST worktree wave — country workflow ruling 43; main is integration-only). Commit style: short imperative, no emojis, commit per task. Push at wave close.

---

### Task 1: `sv/requirements/special-regimes/01_regime-framework.md`

**Files:** Create `sv/requirements/special-regimes/01_regime-framework.md`
**Covers master clusters:** SR1
**FR numbering:** opens SV-SPE-FR-001

**Content requirements:**
- §2 preamble: the special-regimes authority order + the SOQ-30 verification note (rides every regime LB in this wave).
- Regime taxonomy FRs (12_ Art. 2 h)/r)): ZF (extra-territorial for import/export tributes, indefinite) vs DPA (suspensivo for perfeccionamiento with reexport; capital goods indefinite) — two DISTINCT territorial regimes; LSI parque de servicios (multi-company extra-aduanal) vs centro de servicios (single company, incl. within primary customs zones) + usuario directo/indirecto/consignación/mercancías destinadas definitions (14_ Art. 2).
- Beneficiary-role FR (12_ Art. 5: desarrollista/administrador/usuario/DPA titular; 14_ Art. 10 four LSI roles): a company profile carries (regime, role, activity admission, location track, acuerdo D.O. date) — the D15 row key.
- Authorization architecture FRs (12_ Art. 4: MINEC authorizes, MH DGA+DGII vigila; 14_ Art. 3: ONI capital registration ≤5 días hábiles); DGA institutional frame note (13_ Arts. 3/11/14: ZF/DPA/parques inside the servicio aduanero, on-site delegations — informational anchor for the compliance surfaces).
- **Activity-admission config FRs:** ZF permitted activities (12_ Art. 3: SAC Chapter 3 + 25+ industrial scope; romanos II-V; connected services ONLY between beneficiaries) + Art. 6 negative list (hydrocarbons, cement, **azúcar**, **alcohol** salvo Art. 3 V, explosives, etc. + personal exclusions) as config; LSI benefited letters a)-j) with per-letter scope predicates (medical = non-Centroamérica residents; TI = foreign-domiciled PJ clients; aeronáutico = international airlines regardless of domicile) + non-benefited co-located 1)-11) operating under ordinary tax law (14_ Arts. 5-6).
- **Qualification-requisito FRs (dated config rows):** ZF usuario 17-A ($500k/2y OR 50 permanent jobs OR 5 comercializadores; invernaderos/laboratorios $100k + 15 jobs + 5,000/1,000 m²); DPA 19-A ($800k OR 75 jobs OR 15; infrastructure acquisition excluded) + 19-B (reptiles/amphibians $100k/15); LSI 22 (distributors ≥500 m² + DGA registration + manifiesto duties + client-tax liability), 23 (BPO $150k first-year + 10 permanent jobs + ≥1-y written contract — breach year loses that ejercicio's benefits), médico-hospitalario ($10M quirúrgico / $3M no-quirúrgico, outside metro area + departmental capitals, surgical only to insured patients).
- **Breach state-machine FRs:** investment-requisito breach → revocación; jobs/comercializador breach → suspensión until cured with tributos payable during suspension AND the benefit clock keeps running (12_ 17-A); LSI 3rd-grave → revocación (14_ Art. 52); inactivity loss (12m ZF Art. 39 / 3m LSI Art. 62 + DGA system-access disablement); benefit-state field (activa/suspendida/revocada) driving the SR2/SR3 exemption-row resolution and SR5 routing.
- Procedure FRs (12_ Arts. 45/48/49: 25 días hábiles usuario / 35 DPA resolutions; 10-day same-zone amendments; 5-day audiencia; 49 revocatoria 3 días hábiles) — workflow surfaces, días-hábiles engine by id.
- Declarante-role config FR (74_ Arts. 9/5-5-A + 13_ Art. 36-A: agente aduanero vs apoderado especial aduanero — escritura pública + sufficiency exam + fianza — vs self-declaration for personas jurídicas; consultas 15+15 días hábiles; advance rulings 3-y validity).
- Area-metropolitana dated-list FR (12_ Art. 2 d): 13 named municipios as stale-static dated rows (SOQ-43 — no recompute vs the 2023 municipal reorganization); location-track selection metro/fuera feeding SR2.
**AC examples:** usuario admitted with $500k-in-2y requisito logs investment against the row; jobs breach at year 3 → state suspendida, tributos payable, ladder clock unaffected; LSI BPO missing the $150k investment in year 2 → benefits lost for that ejercicio only; apoderado especial transmits own declarations after fianza.
**OQs to carry:** SOQ-30 (preamble), SOQ-43, SOQ-31 (trámite formats), 74_ declarante exam mechanics if evidence-abbreviated.

### Task 2: `sv/requirements/special-regimes/02_zf-exemption-schedules.md`

**Files:** Create `sv/requirements/special-regimes/02_zf-exemption-schedules.md`
**Covers:** SR2
**Consumes:** T1's beneficiary-profile + benefit-state model (by id).

**Content requirements:**
- **The D15 ladder FR family (the wave's canonical deliverable):** per-beneficiary exemption-window rows keyed (role × location track × acuerdo D.O. date × extension flags), each row `valid_from/valid_to` + percentage:
  - usuario ISR: 100% 15y (metro) / 20y (fuera) → 60% 10y / 15y → 40% 10y (12_ Art. 17 d));
  - usuario municipal: 100% 15y/20y → 90% 10y/15y → 75% INDEFINITE tail (Art. 17 e));
  - DPA ISR: 100% 10y (metro) / 15y (fuera) → 60% 5y/10y → 40% 10y; municipal 10y/15y → 90% 5y/10y → 75% (Art. 19 d)/e));
  - desarrollista/administrador: ISR total 10y/15y + municipal 10y/15y + ITBIR (Arts. 11/13);
  - extensions: +5y ampliation (≥8 manzanas within 5km meeting Art. 10 infrastructure; Art. 11 final); +5y 100%-investment-increase (Art. 17 e) final); 17-B strategic sectors +5y (microprocessors/integrated circuits/vehicle parts/computer parts/medical devices/energy equipment); 19-C ≥$10M new investment +10y; pre-existing beneficiaries 54-C (total until 31-dic-2015 or acuerdo expiry + 5 additional years).
- **Percentage-of-rate computation FR:** the exemption percentage applies ONLY to income from the actividad autorizada (segregated accounting between benefited and local activity — Reglamento ISR Art. 32 gravada/no-gravable kin, taxation by id); resolution anchor = fiscal year; snapshot on the year's determination.
- **Dividend-window FR:** distributions exempt for 12 ejercicios from benefit start; from the 13th ejercicio taxed (interacts Ley ISR Art. 72 5% + taxation/05 earnings register by id — the exemption-suppresses-retention implication made explicit per EVID-253 doubt); PJ-socios exclusivity rule.
- **Exception-goods FR family (12_ Art. 17 final / Art. 19):** alimentación y bebidas (except agua envasada), tabaco, alcohol, vivienda rental, muebles/enseres, suntuarios, vehículos, hotel services — entry requires DM definitiva-a-pago or CCF/FCF showing PAID IVA, UNLESS the benefited activity requires them AND the acuerdo records it; the inverting gate (PAID-IVA evidence check on admission) with e-invoicing doc-type consumption by id.
- Capital-goods 5-year free-transfer FR (DPA Art. 20): asset-level franquicia-entry date + eligibility flag (transfer with DM importación definitiva + original DM annexed).
- No-necessary-goods tariff config FR: per-acuerdo nomenclature detail (secciones/capítulos/partidas/subpartidas) + the retroactive-acceptance modification procedure (import under suspension while the request processes; acceptance retrotrae to registration date; denial ⇒ immediate payment).
- **Quincena-25 certificado consumption FR:** FY-2026 ZF/DPA/LSI voluntary payers take the 100% ISR credit as negotiable Certificado de Crédito Tributario — cite SV-TAX-FR-174 by id (route `certificado_zf_dpa_lsi`), NEVER restated; F-11 v20 declaration interface = pointer OQ (print not acquired; SOQ-41 family); declaration-duty-survives-exemption guard (F-11 v20 kin, LSI Art. 14 explicit).
- Municipal proration FR for comercializadores (local sales / total sales over activo ratio — Art. 25 final).
**AC examples:** metro usuario with acuerdo D.O. 2020-03-02 → rows 100% (2020-2034), 60% (2035-2044), 40% (2045-2054); the 13th-ejercicio dividend crosses to taxed with 5% retention; a $408.80-sector SMM-independent check NOT here (sanctions live in 07); exception-goods invoice without paid-IVA evidence blocks admission; certificado generated only via the SV-TAX-FR-174 route.
**OQs to carry:** SOQ-43 (if not landed in T1), dividend-interaction explicitness note (EVID-253 doubt resolution), F-11 v20 acquisition watch.

### Task 3: `sv/requirements/special-regimes/03_lsi-regime.md`

**Files:** Create `sv/requirements/special-regimes/03_lsi-regime.md`
**Covers:** SR3
**Consumes:** T1's profile/state model; T2's D15 row pattern (by id, regime-specific shapes).

**Content requirements:**
- LSI exemption-shape FRs (14_ Arts. 14/17/21/25): desarrollista/administrador 15y ISR (from parque operations start) + 10y municipal + ITBIR; **usuario directo + centro de servicios ISR + municipal INDEFINITE ("durante el período que realicen sus operaciones en el país", from first ejercicio) = open-ended D15 rows with a CESSATION event, no phase-downs** — distinct row shape from SR2 ladders, never unified; franquicia arancelaria total (centros); declaration-still-due guard (Art. 14 explicit).
- **17b_ Art. 22 local-market cap FRs (the regime's distinctive dated parameter):** caps 50% (distribución internacional a, logística b) / 40% (procesos empresariales h, financieros internacionales j, call centers c) / 30% (TI d, I+D e) of total services — measured by VENTAS per año (dictamen Art. 58.e.9.iii); annual local-share monitor with cap-breach alert; exclusion categories tracked separately (acopio para exportación de libre circulación; almacenaje nacional/nacionalizado; foreign-client reexport billed by local filial); measurement basis + straddle working assumption per SOQ-38.
- Semestral auditor-dictamen FR family (14_ Art. 47 f) + 17b_ Arts. 45-61): DGII-authorized independent firm; annual nomination within first 5 months + 10-días-hábiles DGII inform; mid-first-semester qualifier 2-month window; **dictamen content checklist** (1%/1.5% retention application verified; per-client per-service-type physical inventory verification; SS cotizaciones pagadas verification; Art. 22 percentage verification) + **anexos** (libros-vs-declaraciones IVA comparative; monthly retention analysis; monthly SS comparative laboral+patronal; compras comparative; hallazgos); periods 1-ene→30-jun (due 31-oct) and 1-jul→31-dic (due +5 months) — Odoo data-packager FRs, días-hábiles engine by id.
- Requisito-tracking FRs (22 m²/DGA registration/manifiesto duties/client-tax liability; 23 BPO investment/jobs/contract; médico thresholds — carried from T1 config, this file owns the LSI-specific monitoring).
- Usuario-indirecto liability FR: distributor responds for clients' goods taxes on inventory faltantes/extravíos/pérdidas/mermas — consignment liability ledger surface.
- 90%-Salvadoran staffing quota FR (14_ Art. 47 k): workforce-composition monitor consuming payroll records by id; MinTrabajo exception track (≤5-y training horizon).
- CT-158-II carve-out FRs (17b_ Art. 65 + 14_ Art. 4): beneficiaries do NOT apply the CT Art. 158 inciso-segundo retention on incoming services; non-domiciled foreign employees carve-out — config flags on vendor bills; cross-check note vs 05_ CT text (EVID-259 doubt).
- Fianza FR (14_ Art. 50: repeated infractions/audit incongruities); AML-conviction revocation link (commercial-legal by id).
- ZF→LSI migration note (14_ Arts. 63/66: ZF-qualified service users pass "de pleno derecho"; LSI users inside a ZF treated as in a parque) — SOQ-42 per-case config OQ.
**AC examples:** centro de servicios exempt indefinitely until cessation event stamps the row end; local share 52% for a logística usuario → cap-breach alert (50% cap) with dictamen flag; dictamen data pack assembles the 5 anexos from monthly ledgers; incoming service bill from a domestic provider skips the CT-158-II retention.
**OQs to carry:** SOQ-37/38/42 + CT-158 cross-check note.

### Task 4: `sv/requirements/special-regimes/04_customs-clocks.md`

**Files:** Create `sv/requirements/special-regimes/04_customs-clocks.md`
**Covers:** SR4

**Content requirements:**
- **ZF/DPA perfeccionamiento clock FR:** 12 MESES IMPRORROGABLES per DM acceptance (12_ Art. 22) — per-DM tracker; expiry ⇒ tribute obligations + LESIA sanctions (SOQ-32 pointer).
- **Traslado sub-clock FRs:** definitive ≤12m from first admisión; temporales ≤6m within the 12m envelope; ZF→DPA ≤12m from the ZF-cancelling DM liquidación; ZF/DPA→TAN temporales 2 meses; formalización ≤3 días hábiles after ingreso; non-dominion traslados need NOTA DE REMISIÓN (e-invoicing NRE doc type by id).
- TAN→ZF/DPA passive-processing FR (12_ Art. 24): exportación temporal for processing, reimport ≤6 months, duties ONLY on the non-national value-added aggregate; NMF tariff; asimilación to exportación temporal para perfeccionamiento pasivo.
- **LSI clock FRs (NEVER unified with ZF — invariant):** parque permanencia INDEFINITE (liberatorio character); centros materias-primas/insumos 1 year from DM acceptance; capital goods liquidados a franquicia definitiva; **admisión temporal 24 MESES CALENDARIO prorrogable +1y periods with prior DGA authorization** (14_ Art. 33); destinación window 20 días hábiles post-discharge (expiry ⇒ abandono); regímenes optables menu (14_ Art. 34: importación/exportación definitiva, temporal mismo estado, tránsito, reexportación; ZF/DPA/depósito via aduana interna tránsito).
- Expedición FR (14_ Art. 41): status ≤20 días hábiles post-DM + information duty.
- Customs-value edge FR (14_ Art. 43): storage/conservation costs excluded when expressed separately from the price.
- Certificados de Control Aduanero FR (14_ Art. 44): reexport certificate records for TLC-origin benefits.
- Residuales disposition FRs (14_ Art. 45): palets/bidones to TAN = duties on valor facturado a precios de mercado + DM simplificada; authorized botaderos free; donations exonerated via MINEC + Asamblea.
- **DUCA linkage FRs:** the DUCA "fecha de vencimiento del régimen" field feeds these clocks (43_ by id from T6); DUCA-F 30-días-hábiles validity when serving as FAUCA, export-country only.
**AC examples:** DM accepted 2026-03-10 → ZF clock expires 2027-03-10 irreextendable, warning at 30 days; same goods under LSI → 24m + renewal windows; traslado temporal out 5 months within a 12m envelope passes, 7 months fails; NRE attached to every non-dominion traslado; destinación at day 21 post-discharge ⇒ abandono state.
**OQs to carry:** SOQ-32 (LESIA expiry consequences), SOQ-36/45 (DUCA fields kin — crossfile with T6).

### Task 5: `sv/requirements/special-regimes/05_tan-iva-interface.md`

**Files:** Create `sv/requirements/special-regimes/05_tan-iva-interface.md`
**Covers:** SR5

**Content requirements:**
- **Internación FR family (12_ Art. 3 I) final block):** ZF/DPA production sold into TAN pays import duties ONLY on the non-national component; valor en aduana for transformed goods = materias primas + gastos indirectos de fabricación (verbatim cost rule); comercializadores pay on full value minus demonstrated national component; NMF tariff (TLC-origin goods untouched); minimum-value floor = the entry value/CIF (declared value never below either).
- **TAN→ZF/DPA sales FR (12_ Art. 25 — the F-07 annex-3 tipo-11 authority):** 0% IVA rate + Ley IVA Arts. 76/77 applicability (fiscal-position routing; consumption of the IVA-core computation by pointer — that wave owns Ley IVA mechanics); not-necessary goods = full 13% (Ley IVA Art. 54); market-price rule with DGII adjustment powers (CT procedure); fiscal-reporting/03 annex-3 tipo-11 bucket by id.
- B2B intra-regime FR: sales/purchases of activity-necessary goods between beneficiaries = NO derechos ni impuestos INCLUIDO IVA (12_ Art. 3; LSI cross-regime below).
- Comercializador TAN-sales FR: ISR/municipal incentives INAPPLICABLE (Art. 17 d)/e) excluded); municipal taxes prorated local-sales/total-sales-over-activo.
- Materia-prima TAN-consumption FR (12_ Art. 27): duties on valor facturado ≥ proportional CIF; desperdicios/subproducts/defectuosos to national market = duties on valor en aduana; to authorized botaderos = free.
- **LSI export-test FR (14_ Art. 8):** service used EXCLUSIVELY abroad or in extra-aduanal territory AND provided to a foreign/extra-aduanal-domiciled client → export treatment; local sales only to IVA-registered contribuyentes (ISR + IVA + municipal).
- **LSI dual-retention FRs:** local services (letters a-e,h,j) — prestatario withholds **1.5% ISR anticipo** (such rentas NOT subject to the CT anticipo system — suppression flag) and **1% IVA** on service value (14_ Art. 8); dated 2007 values with SOQ-37 cross-check; withholding-engine rows consumed from taxation/04 by id; dictamen verification hook (T3 by id).
- **Cross-regime services FR (14_ Art. 8 — the S6 IVA-tercerización-FCF-exento pointer's authority):** LSI a)/b) services to ZF/DPA beneficiaries = no taxes incl. IVA when directly export-linked; documented via FACTURA DE CONSUMIDOR FINAL consigning the prestatario's name (e-invoicing FCF doc rule by id).
- LSI goods-interface FRs: TAN→parque/centro = exportación definitiva with Ley IVA Arts. 75-77 (vs ZF's 0%+76/77 — keep the distinction explicit); goods from distribución/logística into TAN = importación definitiva (importer = sujeto pasivo).
- **SS-solvency gate FR (12_ Art. 9-A + 74_ Art. 11-A):** every regime sale/import gated on prior-month SS solvency verified by electronic means (payroll/06 records by id); LSI simplified-withdrawal solvencias valid 30 days.
**AC examples:** ZF producer interns goods — duty base = non-national component only, floor at entry CIF; TAN vendor delivers to a ZF usuario → 0% + 76/77 routing + annex-3 tipo-11 row; B2B ZF sale books no IVA; LSI call center bills a domestic bank → 1.5% + 1% retention rows fire; LSI logistics service to a ZF maquila export-linked → FCF issued naming prestatario, no taxes; SS arrear month blocks the gate with cure path.
**OQs to carry:** SOQ-37 + non-national-component method doubt (EVID-252 — DGA practice corpus-silent).

### Task 6: `sv/requirements/special-regimes/06_customs-declarations.md`

**Files:** Create `sv/requirements/special-regimes/06_customs-declarations.md`
**Covers:** SR6

**Content requirements:**
- **DUCA record-model FRs (43_):** three variants (DUCA-D terceros-países / DUCA-T tránsito internacional / DUCA-F originarios región) as one model with a variant flag; header blocks (declarante correlativo; system-assigned registration number; fecha de aceptación; exportador/proveedor + importador/destinatario + declarante identity blocks; aduanas registro/inicio/salida/ingreso/destino; régimen aduanero + modalidad + clase de declaración; **fecha de vencimiento del régimen** — feeds T4 clocks; países; depósito aduanero/zona franca code; transportista/conductor/medio blocks with marchamos/container IDs); **value block 25-29** (valor de transacción + flete + seguro + otros = valor en aduana total = the tax base) + INCOTERM (30) + peso-centroamericano exchange rate (31 — SOQ-45 config-gap); lines (país origen, unidad, cantidad, ACUERDO preferential DAI, SAC classification + national additional codes, descripción, per-line value + liquidación tipo/alíquota/total/modalidad); soporte documents with tipo/número/fechas/país + line-range syntax ("3-5", "1, 6, 8"); declaración de origen (producer) vs certificación de origen (exporter) complementarity.
- **DUCA-F validity FR:** 30 días hábiles from emission when serving as FAUCA, export-country only (43_ field 56).
- Teledespacho legal-chassis FRs (74_ Arts. 6/8): electronic transmission with authenticity/confidentiality/integrity/no-repudiation; data messages = paper legal effects; digital signature via certifying entities (public-key pairs); auxiliaries' key-confidentiality duty.
- **$18 inspection-tasa FR (74_ Art. 12-B):** per manifiesto/DM/FAUCA/tránsito transmission, IVA-INCLUDED, despacho-blocking (no despacho authorization without payment), due at transmission; biennial ≤10% revision mechanism as dated-value watch (SOQ-34; $18 = the 2012-printed provenance).
- Presumed-valuation FRs (74_ Art. 2): insurance 1.25% FOB (regional land transport) / 1.50% (international cargo) when not accredited; flete 10% FOB or DGA periodic reference values when not accredited — dated config rows feeding the value block (SOQ-35); pre-arrival manifiesto duty (peso bruto kg, clase/cantidad bultos, goods by descending value).
- Autoliquidación + selectividad FRs (74_ Arts. 3/12/12-A): declarant self-determines; selective-random inspection; non-intrusive inspection images = plena prueba.
- Payment/anulación clock FRs (74_ Art. 11): suspensive/liberatorio-regime goods transfers require DM presentation + payment BEFORE transfer/sale; liquidaciones/sanciones payable ≤8 días hábiles from notification; teledespachada-unpresented anulled at 10 days; paid-unpresented anulled at 60 days with devolución route.
- Simplified/courier FRs (74_ Art. 11-A): 48-hour withdrawal (1-y authorization + garantía + SS solvencias 30 days); courier $200 (guía aérea + factura withdrawal) / ≤$3,000 (declaration withdrawal), consolidable ≤$3,000 per courier.
- **Fiscalización/caducidad/retention FRs (74_ Arts. 13-17):** records + origin certificates retained ≥5 years (exporters/producers); verification caducidad 5 years from DM acceptance — per-DM tracker; electronic notification (agent notification extends to declarant); 15-días-hábiles alegatos + 20-días-hábiles resolution; recursos per LESIA (SOQ-32 pointer). **Customs 5y row noted into the commercial-legal/02 §3.7 retention matrix by id (update-by-note only).**
- SIECA/Panamá integration note FR (42_): DUCA-F electronic transmission SV↔Panamá since 2025-03-03 via ducaf.sieca.int (tokens, ~37-second acceptance, destination declaration-number visibility) — dated operational row + external-interface assumption; e-invoicing FEX export pairing by id.
**AC examples:** DUCA-F as FAUCA expires after 30 días hábiles in-country only; unaccredited flete on $10,000 FOB → $1,000 presumed line into valor en aduana; regime-goods transfer blocked until DM paid; $18 tasa unpaid blocks despacho; 61-day-old paid-unpresented declaration auto-annulled with devolución route.
**OQs to carry:** SOQ-34/35/36/45.

### Task 7: `sv/requirements/special-regimes/07_obligations-reporting-sanctions.md`

**Files:** Create `sv/requirements/special-regimes/07_obligations-reporting-sanctions.md`
**Covers:** SR7

**Content requirements:**
- **ZF obligations FRs (12_ Art. 28):** 10-días-hábiles modification notice; **electronic inventory + entries/exits/saldo + cuadro demostrativo de descargo register online at DGA's disposal** (fallback: remittance ≤20 días hábiles after fiscal-year end); semestral MINEC informe (importaciones valor/origen + exportaciones valor/destino + empleo generado + ventas al mercado nacional + inversión); 30-day cambio/cierre notice; damaged/lost/destroyed goods registry; **DPA physical segregation of suspensivo vs nacionalizado inventories (trazabilidad)**; **cost records for TAN-sold goods**; annual pending-cancellation goods report (20 días hábiles); **pormenorized insumo-vs-producto-compensador register (yield/merma tracing)**.
- **17b_ Art. 28 inventory-register contract FRs (LSI distributors):** the 10 mandatory consultas/reportes (daily ingresos/egresos; saldos; declaraciones con cancelaciones/destinaciones; declaraciones con saldos; abandono detail; depósito temporal; admisión temporal; retenidas administrativamente; acopio para exportación; almacenaje simple por contribuyente); queries per declaración/régimen/destinación/contribuyente; **every item carries SAC 6-digit classification**; Excel-transferable export; Art. 29 minimum-áreas note (physical — informational); Art. 44 annual consolidated ops+inventory report ≤30 días hábiles post-year.
- LSI obligations FRs (14_ Arts. 46-48): electronic records annual remittance; ≥500 m²; 5-year manifiesto copies; custody; 8-day irregularities notice; marchamo entry/exit duties (reincidencia muy grave).
- **Sanction-ladder FRs:** ZF (12_ Art. 36: leves→prevención, reincidencia 3 SMM; graves 5 SMM; muy-grave destino-authorizado breach → suspensión ≤3 meses, reincidencia definitiva) + Art. 36-A MH 30-días-calendario regularization → system-access suspension until cured + Art. 39 12m-inactivity category loss + Art. 40-A closure-with-open-DMs = defraudación crime (LESIA Art. 22 pointer, SOQ-32); LSI (14_ Art. 52: menos-grave reincidencia 3 SMM; graves 30/40 SMM; 3rd grave → revocatoria; muy grave 3-mo suspension) — **SMM "de mayor cuantía" = highest 16_ sector row config default consuming payroll/02 by id (SOQ-33)**; SS-payment breach → 3-month benefits suspension / reincidencia revocation (12_ Art. 31; 14_ Art. 50).
- DGA a-posteriori frame note (13_ Art. 19): permanente control over suspensive/liberatorio regimes — the audit-readiness backdrop for the registers above.
**AC examples:** descargo register reconciles per-DM cancellations; semestral informe assembles the five data groups from ledgers; grave ZF infringement prices 5 × dated SMM-mayor-cuantía row; SS arrear → benefits suspend 3 months while ladder clock runs; 13th month of inactivity → category-loss state.
**OQs to carry:** SOQ-32/33/44.

### Task 8: `sv/requirements/special-regimes/08_fovial-cotrans.md`

**Files:** Create `sv/requirements/special-regimes/08_fovial-cotrans.md`
**Covers:** SR8

**Content requirements:**
- FOVIAL contribution FRs (31_ citing D.L. 208-2000 Art. 26 as reformed D.L. 597-2001 — provenance chain in §2): **$0.20/galón** on diesel/gasolinas y mezclas (aviation gasoline EXCLUDED); hechos generadores = (a) sale/any transfer-of-ownership by importadores/refinadores + (b) direct imports for own consumption; quantity-based (galones) — Odoo `account.tax` amount-type per-unit design (the EXTRACTION_PLAN-flagged decision: D15 dated value rows with instrument provenance, $0.20 = the 2001-printed value consistent with CAT-015 v1.1 2026-07).
- **IVA-base exclusion guard FR:** the contribution is NOT base imponible nor an addition to it (Ley IVA Arts. 47/48-a/51-d via the guide) — never charge/recargar 13% on it; IVA computes on the price only; e-invoicing CAT-015 code D1 tributo-line wiring by id.
- Documentation FR: separate fila/casilla on documents, separate from price AND from IVA.
- **B2B chain control-account FRs (31_ ledger examples):** refinería/importador sale books RETENCIÓN FOVIAL credit; each intermediate books CUENTAS POR COBRAR-FOVIAL at purchase and re-bills the $0.20×gal at sale, through to the final consumer; final consumer/consuming contribuyente classifies as fuel cost / operating expense / manufacturing expense; own-consumption acquisition ISR-deductible (Ley ISR Art. 29.6 — taxation by id).
- COTRANS gap FR-scope: $0.10/galón (CAT-015 C8) contribution exists as a DTE tributo surface but its INSTRUMENT is absent (MOQ-04 half-open; SOQ-39) — same quantity-tax model, dated rows when acquired; no invented values beyond the CAT-015 print anchor (dated-data note).
- Fiscal-reporting feed note: F-07 fuel annexes 13-14 (fiscal-reporting/05 by id); B2B-chain-vs-DTE mapping design pass = IVA-core wave pointer (SOQ-40).
**AC examples:** 1,000-gal distributor sale books the $200 receivable re-bill; FE line shows D1 tributo with IVA computed on price only; own-consumption 500 gal imported → $100 FOVIAL + ISR cost classification; COTRANS row selectable but value-flagged with the instrument OQ.
**OQs to carry:** SOQ-39/40 + MOQ-04 linkage note.

### Task 9: index + coverage + registry flips

**Files:**
- Modify: `sv/requirements/special-regimes/00_index.md` (stub → real index)
- Modify: `sv/requirements/COVERAGE.md` (rows 12_/13_/14_/17b_/42_/43_/31_/74_ pending → cited-as-LB + rollup counts; 02_/32_/33_ stay pending for their waves)
- Modify: `sv/README.md` (special-regimes status → In review (draft, S7))
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (coverage-totals note: S7 delivered)
- Modify: `sv/EXTRACTION_PLAN.md` (extraction log entry: S7 synthesis COMPLETE)

**Content requirements:**
- Index: file table (per-file FR ranges), totals (FRs/LBs/ACs/OQs open-resolved), topic-prefix note (SV-SPE), cross-topic consumer map (SV-TAX-FR-174 certificado; annex-3 tipo-11; días-hábiles engine; SMM sidecar; NRE/FCF/FEX; retention matrix), OQ rollup mapping in-file OQs ↔ SOQ-30..45.
- COVERAGE flips: 12_/13_/14_/17b_/42_/43_ cited-as-LB (S7 files named); 31_ cited-as-LB (08 file + provenance chain); 74_ cited-as-LB (01/06/07 files) — rollup recount (expect 72 rows, cited-as-LB 52→60, pending 10→2 (02_/32_/33_)).
- Numbering-continuity verification: `grep -o "SV-SPE-FR-[0-9]*" sv/requirements/special-regimes/*.md | sort -u` → contiguous 001..N no gaps; per-FR LB-citation presence check.
- Commit + push sv-research.

## Execution protocol

Per-task: fresh implementer subagent (reads this plan's Global Constraints + its task + the evidence files fully) → controller review → reviewer subagent (verifies FRs against the master index + evidence; numbering; LB citations; layer column; cross-refs by id; quote fidelity vs extraction txt) → fix round if findings → commit. Final whole-wave review subagent → ONE fix wave → push. Rulings discovered in-wave are recorded in the task's fix commit and summarized to the controller for the sv/HANDOVER update (copy before workspace deletion). Tasks 1-8 STRICTLY sequential (numbering chain); Task 9 last.
