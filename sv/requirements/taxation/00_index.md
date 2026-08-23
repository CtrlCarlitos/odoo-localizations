# SV — Taxation (ISR + IVA) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S2 ISR + S9 IVA synthesis waves + W17 CT-reglamento fold-in + W19 identity-notes pass, in review) |
| Authors | Takumi synthesis waves 2 + 9 + controller |
| Updated | 2026-08-22 (W19 T6: 08/09 identity notes — SOQ-56/58 refreshed, 09 OQ-3 resolved; no new FRs) |

This directory holds the S2 (synthesis wave 2) ISR (*Impuesto sobre la
Renta*, income tax) requirements: the subject/period/territoriality/filing
framework, renta neta deductions, rates & special computations, withholding
(payroll tables + CT retention matrix), the 5% distributions regime, and
fixed-asset depreciation/software amortization — with the retention/bracket
tables as verbatim dated data in two CSV sidecars. Since the S9 synthesis
wave (2026-08-20) it also holds the IVA (*Impuesto a la Transferencia de
Bienes Muebles y a la Prestación de Servicios*) core: the operation
framework & excluidos regime, the Art. 45/46 exemption catalogs, base &
13% rate (with the FOVIAL/COTRANS guard), crédito fiscal deductibility,
the Art. 66 pro-rata & remanente engine, débito/crédito adjustments &
the fixed-asset four-year rule, the CT 161-162-B IVA retention matrix,
exports & reintegro refunds, and the declaration-interfaces file. The
W17 fold-in (2026-08-20) added file 16, the CT application-reglamento
procedural layer (75_ D.E. 117-2001), with 75_ retention/declaration
anchors folded into 01/04/13.
Source-to-requirements coverage: [../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_isr-framework.md](01_isr-framework.md) | Subjects, renta obtenida categories, Art. 6 exclusions, periods & cash/accrual methods, territoriality (D.L. 969-2024 exclusion, Art. 127 apportionment), FX, Art. 92 filing duties; Quincena-25 renta no gravada (FR-173) + FY-2026 employer credit/certificado (FR-174); Ley Art. 62 retention-remittance corroborated by 75_ Arts. 99-100 (LB-027/036, OQ-001 resolved W17) | SV-TAX-FR-001..033, 173..174 | 35 | 36 | 20 | 7 |
| [02_isr-deductions.md](02_isr-deductions.md) | Renta neta: Art. 28 pro-rata (+969 carve-out), Art. 29 deductions, Art. 29-A non-deductibles (thin-cap, 25-SMM cash ban), Arts. 31-32 (reserva legal, bad debts, donations), mermas (D.L. 345-2019), Reglamento segregation; Quincena-25 employer gasto deducible (FR-175) | SV-TAX-FR-034..073, 175 | 41 | 20 | 23 | 9 |
| [03_isr-rates-gains.md](03_isr-rates-gains.md) | Art. 37 brackets (both dated vintages), Art. 41 entity rates, capital gains (10% separate, 12-month rule, no general NOL), securities/deposits 10%, special computations (instalments, repossession, annuities, export valuation); SOQ-01/04 verdicts in §7 | SV-TAX-FR-074..101 | 28 | 19 | 23 | 9 |
| [04_isr-withholding.md](04_isr-withholding.md) | Salaried retention regime (base, $1,600 fixed deduction, Art. 33 deductions), D.E. 10-2025 periodic + June/December recálculo tables, aguinaldo vintages, multi-employer split, CT 154-160 non-payroll matrix; 75_ retention-agent layer (Arts. 94-97/99/103: permanent-service sweep, in-specie market valuation at delivery, retention moment & mes-calendario period, non-domiciled 20% credit awareness — FR-397..400, LB-022..026); CSVs `withholding_tables.csv` (20 rows) + `isr_brackets.csv` (23 rows) | SV-TAX-FR-102..131, 397..400 | 34 | 26 | 22 | 8 |
| [05_isr-distributions.md](05_isr-distributions.md) | Art. 72 5% definitive retention on utilidades, Arts. 73-74-C (permanent establishments, capital reductions, partner-loan deemed distributions, no-retention cases), Registro de Control de Utilidades | SV-TAX-FR-132..149 | 18 | 11 | 18 | 7 |
| [06_isr-assets.md](06_isr-assets.md) | Art. 30 depreciation (rates, used-asset caps, mixed-use pro-rata, seasonal quota), Art. 30-A software 25%, Reglamento Art. 84 per-asset register, Art. 35 maquinaria | SV-TAX-FR-150..172 | 23 | 11 | 20 | 7 |
| [07_iva-framework.md](07_iva-framework.md) | IVA operation model: transfer concept & goods tax point (Arts. 1-10), retiro self-supply (11-13; FACTURA-only root), importación/internación + D.L. 645-2005 exclusive-use services (14-15), prestaciones catalog, tax points & territoriality (16-19), sujetos pasivos (20-27), excluidos regime with the 1992-colones thresholds as [sic] dated rows (28-32; Rgto. 9-10; SOQ-55 = MOQ-03 closure) | SV-TAX-FR-176..205 | 30 | 28 | 21 | 5 |
| [08_iva-exemptions.md](08_iva-exemptions.md) | Art. 45 import/internación + Art. 46 service exemption catalogs as dated rows (46-f BCR-qualification config gate, 46-k stale-SAP anchor, 45-h/167-A sectorial-politics kill-switch, 45-i transport 5-year restriction) + the Art. 174 generic-nullity gate | SV-TAX-FR-206..224 | 19 | 15 | 15 | 5 |
| [09_iva-base-rate.md](09_iva-base-rate.md) | Art. 47 documented-amounts floor, the FULL Art. 48 a)-m) specific-base catalog (Rgto. 17), non-base additions/exclusions (49, 51-52), FX bases (53; Rgto. 18), 13% rate & débito fiscal (54-55, D.L. 370 cutover unpinned), FOVIAL/COTRANS never-in-base guard + the SOQ-40 B2B recovery design pass on DTE tributo lines | SV-TAX-FR-225..245 | 21 | 13 | 18 | 4 |
| [10_iva-credit-deductibility.md](10_iva-credit-deductibility.md) | Art. 57 traslación + credit-document root, no-credit operations (58-61), Art. 65 deductibility gates (58-SMM cash/written-contract, 50% vehicles), retention credits (65 final incisos; Rgto. 23; CT 161-162 same-period gate), Art. 65-A non-deductible catalog (58-SMM via SV-PAY-FR-022 config, SOQ-18 kin) | SV-TAX-FR-246..268 | 23 | 18 | 14 | 3 |
| [11_iva-pro-rata-remanente.md](11_iva-pro-rata-remanente.md) | Art. 66 proportionality engine (factor, accumulated base, January redistribution), denominator composition & no-sujetas exclusions, Quincena-25 tercerización closure (D.L. 499 Art. 6; guía 67_; R30(c) working reading — closes 02's OQ-009 by pointer), remanente indefinite carryforward + cessation lock (67-68; Rgto. 24), credit non-transferability (69), IVA never cost nor gasto (70) | SV-TAX-FR-269..283 | 15 | 8 | 12 | 3 |
| [12_iva-adjustments-assets.md](12_iva-adjustments-assets.md) | Art. 62 débito adjustments (incl. the medicines lot regime), Arts. 63-64 crédito adjustments + determination (modificatoria flag, D9-kin), fixed-asset/capital four-year rule & fijo credits (71-72; Rgto. 26), reorganization transfer gates (Art. 7 f)-i)) | SV-TAX-FR-284..302 | 19 | 12 | 13 | 4 |
| [13_iva-retentions.md](13_iva-retentions.md) | CT 161 non-domiciled transferors/prestadores (acquirer as obligado), CT 162 grandes/medianos 1%/2% matrix + $100 floor, CT 162-A card 2% anticipo, CT 162-B juicios ejecutivos, credit-release same-period tie-in, F-930 reporting surfaces, ISR-track separation vs `04` (closes frep/03 OQ-004); 75_ procedural development of the matrix (Arts. 104-107: non-domiciled reverse-charge entero + mandamiento/nómina, import-temporal lease "recio" [sic], AT designation of domestic agents, percepción-agent price reporting — FR-401..404, LB-016..019) | SV-TAX-FR-303..319, 401..404 | 21 | 19 | 18 | 4 |
| [14_iva-exports-refunds.md](14_iva-exports-refunds.md) | Export definition & zero rate (74-75; Rgto. 2-10), ZF/recintos export-equivalence (Rgto. 29; 12_ Art. 25 co-cite), export credits & on-request offsets (76), reintegro workflow (77; Rgto. 30) with the 13%-of-export-value cap (mixed/pure), three-way purchase ledger (Rgto. 30) | SV-TAX-FR-320..337 | 18 | 10 | 15 | 4 |
| [15_iva-declaration-interfaces.md](15_iva-declaration-interfaces.md) | Monthly declaration chassis (Arts. 93-94; Art. 81 pair), operation-classification interface (R/S fold-in + F-07 annex feed contract, días-hábiles via SV-FREP-FR-200/201), version-regime & historical notes (165, 167-172, 175) | SV-TAX-FR-338..353 | 16 | 8 | 12 | 3 |
| [16_ct-procedures.md](16_ct-procedures.md) | CT application-reglamento procedural layer (75_ D.E. 117-2001, W17): definitions & the caducidad/prescripción clock vocabulary (Arts. 1-2), representation & domicilio fiscal (5-8, 28-30), registration & agent designation (24-27), the declaration-state model with the amendment classification gate (31-35; CT 103 co-anchor), payments & extinction modes (13-18), compensación + the Art. 23/133 retention imprescriptibilidad/caducidad pair (19-23, 133), refunds (129-135), sanctions & deuda tributaria (136-143), books & records (73-90), notifications/fiscalización awareness (3-4, 9, 108-128), print-era historical blocks — dictamen/máquinas — norm hierarchy (36-72, 144-146, historical only per EV75 OQ-3/OQ-4) | SV-TAX-FR-354..396 | 43 | 41 | 10 | 5 |
| **Total** | | SV-TAX-FR-001..404 | **404** | **295** | **274** | **87** |

Numbering note: FR numbering is wave-sequential within the `SV-TAX` prefix
(001-175 ISR, no gaps, no renumbering; 173-175 appended by the S6 Quincena-25
fold-in, 2026-08-18) — unlike S1's per-cluster EINV ranges. **176-353 = the
S9 IVA-core continuation (2026-08-20): per ruling R30(b) the topic dir keeps
ONE prefix — the IVA files continue `SV-TAX` from 176 (files 07-15) instead
of opening a `SV-IVA` prefix** (S6 append precedent; the corpus consistently
books 01_/02_ as "owed to `taxation/`"; HANDOVER §4's new-topic-prefix rule
applies only to genuinely new topics). **354-404 = the W17 CT-reglamento
fold-in continuation (2026-08-20): file 16 (354-396) + the 04/13 retention
FR zones (397-404), one prefix per R30(b).**
The two CSVs are dated-data sidecars of `04_isr-withholding.md`
(`isr_brackets.csv` additionally carries the historical D.E. 25-1992
colones-era vintage rows); they carry no FRs of their own.
Cross-ref (S4 payroll): the F-11 v18 casillas 711-725 personal-deduction
feed VALUES are owned by `../payroll/08_isr-interfaces.md` (source
`65_F11_v18_form_visual.pdf` acquired 2026-08-18).

Cross-ref (S6 Quincena-25): the Ley Especial Quincena Veinticinco (D.L.
499, D.O. N° 8 T.450 14-ene-2026; acquired 2026-08-18 as `66_` with the
67_ guía — EVID-236..239) lands here as **SV-TAX-FR-173..175**:
**SV-TAX-FR-173** (01 §3.1 — renta no gravada, the ISR-side rule) and
**SV-TAX-FR-174** (01 §3.5 — FY-2026-only employer credit ledger +
remanent + tercerización + ZF/DPA/LSI certificado + F-11 v19
casilla-319 feed) in `01_isr-framework.md`; **SV-TAX-FR-175** (02
§3.2 — employer gasto deducible conditioned on actual payment +
documentation) in `02_isr-deductions.md`.
Feed chain: payroll/08 FR-137/142/143 (worker-side no-gravada stamp +
seven-field ledger + 417/418 aggregates) → fiscal-reporting/06+07
FR-209..212 (January annex engine + F-910 code 73) → taxation
FR-173/174 (FR-175 consumes the same paid+documented ledger). F-11
v19/v20 prints = acquisition watch (numbering ≥71; 01 OQ-007; kin
payroll/08 OQ-004) — casillas 630-648 stay unfed on v19 too (R21).
Special-regimes consumer note: the ZF/DPA/LSI Certificado de Crédito
Tributario (FR-174 route `certificado_zf_dpa_lsi`) is the future
special-regimes wave's consumption anchor, cited by id.

## S9 cross-topic consumer map (files 07-15)

- **e-invoicing:** the IVA operation taxonomy rides the DTE document-type
  set (SV-EINV-FR-001 by id throughout — FE/CCF/FEX emission is the
  operative document layer over Arts. 18-a/97-100's repealed anchors); the
  12_ adjustment windows gate document admissibility against the §3.11
  fiscal-immutability family (SV-EINV-FR-159..164 — invalidation reversal,
  NCE/ND routing by id); FOVIAL/COTRANS lines surface as CAT-015
  product-category tributo rows (09 §3.6/§3.7, 14, 15).
- **fiscal-reporting:** the F-07 annex engine consumes these files'
  classifications by id — sales value/débito buckets (SV-FREP-FR-048),
  annex-5 excluido purchases (SV-FREP-FR-086 — applicability now defined
  by FR-313), Decreto 321 *combustible diferenciado* rows
  (SV-FREP-FR-124..126/133), the Art. 66 pro-rata inputs casillas
  132-134 (FR-275), the upload-engine surfaces (SV-FREP-FR-004/012); the
  Art. 94 declaration deadlines consume the días-hábiles engine
  (SV-FREP-FR-200/201); F-930 = the retention reporting surface (10/13 —
  SV-FREP-FR-104..111).
- **special-regimes:** SR5 (`../special-regimes/05_tan-iva-interface.md`)
  rides the export-equivalence machinery homed in 14_ (SV-SPE-FR-087:
  0% + Arts. 76/77; Rgto. Art. 29 co-cited in LB-009); SR8
  (`../special-regimes/08_fovial-cotrans.md`, SV-SPE-FR-166..175) and
  09_'s SOQ-40 design pass (FR-244/245) are the two sides of the
  FOVIAL/COTRANS recovery-chain handoff — one design, cited both ways by
  id.
- **payroll (SMM):** the Art. 65-A l) 58-SMM threshold reads the
  payroll/02 SMM dated rows through the SV-PAY-FR-022 sector-mapping
  configuration (10 OQ-002; SOQ-18 kin — a DIFFERENT threshold from the
  ISR 25-SMM rule of 02 OQ-002; never conflated).
- **ISR-side separation:** the CT 154-160 ISR retention matrix stays
  owned by `04_isr-withholding.md` (ISR track); 13_ owns only the
  IVA-side CT 161/162/162-A/162-B matrix — the two tracks are kept
  formally distinct (13 §3.5).

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. ISR files (01-06): 41
open / 6 resolved (SOQ-01 and SOQ-04 in `03_isr-rates-gains.md` §7;
SOQ-03 in `04` OQ-002 + `01` OQ-005 — D.O. pin + digit-fidelity
verification against the gazette print, source `60_`/EVID-171,
2026-08-18; 02's OQ-009 resolved-by-pointer to S9 11, R30(c) working
reading, 2026-08-20; 01's OQ-001 resolved W17 2026-08-20 — 75_ Arts.
99-100 corroborate Ley Art. 62, LB-027/036, EVID-351). S9 IVA files
(07-15): 35 open — including the SOQ-54 vintage watch as every file's
OQ-1. W17 file 16: 5 open. Wave total: **81 open / 6 resolved
(87 OQs)**.

Master-index SOQ mapping: 04's OQ-001 = SOQ-02; 04's OQ-002 = SOQ-03;
04's OQ-003 = SOQ-05; SOQ-06 lives in 01's OQ-004 + 06's OQ-001; SOQ-07
in 03's OQ-007 (kin: 02's OQ-006). SOQ-01/SOQ-04 = 03's OQ-001/OQ-002,
resolved. S9: SOQ-54 = OQ-1 of EVERY file 07-15 (01_/02_ consolidation
vintage watch, rides every LB); SOQ-55 = 07's OQ-2 (MOQ-03 closure —
colones thresholds as config); SOQ-56 = 08's OQ-2 (BCR-qualification
instrument found, 101_-105_); SOQ-57 = 08's OQ-3 (stale SAP anchor);
SOQ-58 = 08's OQ-4 (167-A kill-switch). Kin: 09's OQ-2 = SOQ-40 design
pass; 09's OQ-3 = SOQ-39/MOQ-04 kin; 10's OQ-2 = SOQ-18 kin; 13's OQ-2
= SOQ-21 kin.

### 01_isr-framework.md (7)

- OQ-001 — Ley Art. 62 retention-remittance deadline vs CT retention-agent regime (CT re-anchor check). **resolved** (W17 2026-08-20: 75_ Arts. 99-100 corroborate — 10 días hábiles after the mes-calendario + monthly consolidation of sub-monthly cycles; LB-027/036, EVID-351; by-NIT-digit windows remain SOQ-08)
- OQ-002 — Art. 92 num. 9 obsolete stamp-tax duty; CT-era restatement of the filing-duty list. open
- OQ-003 — Art. 105-A stale sanction (repealed anchor, colon minimum) disposition. open
- OQ-004 — SOQ-06 carried: D.E. 117-2001 survivors vs later CT Art. 344 ff. repeals. open
- OQ-005 — SOQ-03 (partial): D.E. 10-2025 publishing D.O. issue unpinned (vigencia 2025-05-08 assumed). **resolved** (60_/EVID-171: D.O. 79 T.447 30-abr-2025, effective 2025-05-08)
- OQ-006 — CT Art. 62 FX conversion: operational rate source/feed selection. open
- OQ-007 — F-11 v19/v20 prints not acquired (casilla 319 + certificado anexo; R21 extends to v19; numbering ≥71 watch). open

### 02_isr-deductions.md (9)

- OQ-001 — Art. 28 inciso final pro-rata factor vs Reglamento Art. 32 flat 50/50 common-cost split. open
- OQ-002 — SMM parameter source for the 25-SMM cash-payment ban threshold. open
- OQ-003 — BCR active-rate feed for the thin-cap active-rate + 4 points test. open
- OQ-004 — Art. 31.3 bank/insurer reserve regime: deferral to special-regimes wave. open
- OQ-005 — Registry of legally-authorized associations/cooperatives (social funds validation). open
- OQ-006 — Reglamento Art. 29 deposit-interest exclusion stale vs Ley Art. 4.5 (SOQ-07 kin). open
- OQ-007 — Art. 29.6 December window for deductible taxes vs CT deadline rules. open
- OQ-008 — 2026 Quincena-25 double benefit (FR-175 deduction + FR-174 credit simultaneously; law cumulative; fiscalización criteria flag). open
- OQ-009 — IVA tercerización (FCF exento; no Ley IVA Art. 66 pro-rata): pointer owed to the IVA-core wave. **resolved-by-pointer** (S9 `11_iva-pro-rata-remanente` OQ-2 — R30(c) working reading, 2026-08-20)

### 03_isr-rates-gains.md (9)

- OQ-001 — **SOQ-01 verdict (recorded):** Ley Art. 42 flat 10% governs all current periods/classes (54_ pp.39-40, stamp (14) = D.L. 496-2004); Reglamento Art. 17 media-tasa = historical pre-2004 method (LB-010). **resolved**
- OQ-002 — **SOQ-04 verdict (recorded):** NO general NOL carryforward exists (CT/04_ scans negative); only capital losses per Arts. 14/14-A (5-year gains-only ledger). **resolved**
- OQ-003 — Art. 41 US$150,000 threshold: no indexation mechanism in corpus. open
- OQ-004 — "Interés legal" rate feed (life annuities, interest presumption). open
- OQ-005 — Securities price-floor feed (exchange quotation / emitter book values). open
- OQ-006 — DGII calculation-form layouts (capital gain/loss, rentas de capital, capital-loss declaration). open
- OQ-007 — SOQ-07 deposit reading: average-balance computation detail (per-institution vs aggregated). open
- OQ-008 — Insurer/fianza determination + pre-1992 patrimonio-tax basis rows: deferral check. open
- OQ-009 — Art. 37 vintage straddle: single 2025 annual liquidation across the 2025-05-08 cutover (period-close selection rule as working assumption). open

### 04_isr-withholding.md (8)

- OQ-001 — SOQ-02: $1,600 fixed-deduction proration (quincenal/semanal Tramo II) + ordering vs SS/AFP netting. open — working assumption implemented (FR-103/104)
- OQ-002 — SOQ-03: D.E. 10-2025 provenance (publishing D.O. issue) + printed-digit anomalies. **resolved** (60_/EVID-171: effective 2025-05-08 confirmed; all anomaly digits gazette-original)
- OQ-003 — SOQ-05: 2025/2026 aguinaldo transitory (standing 2-SMM rule assumed for 2025+). open
- OQ-004 — Part-time without subordination: retention tables vs 10% honorarios rule. open
- OQ-005 — Retention-decree chain gap D.E. 25-1992 → D.E. 95-2015 (pre-2025-05-08 tables absent). open
- OQ-006 — 10_ 1992 vintage print anomalies (row-3 offsets, quincenal overlap, semanal typo). open
- OQ-007 — MOQ-10 kin: electronic reporting surface for ISR retentions (CT 123/123-A). open (answered for the ISR side by S3: F-910 — see `../fiscal-reporting/07_codes-and-informs.md` §3.3)
- OQ-008 — Art. 37 straddle kin for WITHHOLDING: wages earned 1-Jan–7-May-2025. open

### 05_isr-distributions.md (7)

- OQ-001 — CT Art. 158-A carve-out scope beyond the 25% tax-haven rate. open
- OQ-002 — Art. 74-C Registro de Control de Utilidades: DGII administrative norms. open (partially answered by S3: F-915 — see `../fiscal-reporting/07_codes-and-informs.md` §3.4)
- OQ-003 — Art. 74-A override mechanics (total-consideration reading, mora/quota measurement). open
- OQ-004 — Pool-consumption ordering for ordinary distributions (untaxed-pool default). open
- OQ-005 — Art. 25 inciso 1 vs inciso 2 deemed-loan overlap (exception sets). open
- OQ-006 — Electronic reporting surface for the 5% retention (MOQ-10 kin). open (answered-kin by S3: surfaces = F-14 codes 43-46 + F-910 + F-915 — see `../fiscal-reporting/07_codes-and-informs.md` §3)
- OQ-007 — Exemption-proof artifact class for Art. 74-B final inciso. open

### 06_isr-assets.md (7)

- OQ-001 — Reglamento Art. 84 vs CT Arts. 139-143 books/records regime (SOQ-06 carried). open
- OQ-002 — Seasonal-activity qualification list ("actividades estacionales"). open
- OQ-003 — Part-year pro-rata convention: months vs day-count. open
- OQ-004 — Used-asset "AÑOS DE VIDA" measurement + new-price cap evidence classes. open
- OQ-005 — Depreciation-register format norms beyond Art. 84's minimum field list. open
- OQ-006 — Mejoras/adiciones mechanics: own forward quota vs life extension vs restart. open
- OQ-007 — Software schedule span: >25% authorizations and slower-schedule practice. open

### 07_iva-framework.md (5)

- OQ-1 — SOQ-54 (vintage): 01_ last reform stamp D.L. 71-2015 / 02_ D.E. 117-2001; re-verify Arts. 1-32 + Rgto. survivors. open
- OQ-2 — SOQ-55 (MOQ-03 closure): Arts. 28-29 1992-colones exclusion thresholds as [sic] dated rows + configurable administered criteria, no invented USD conversion. open
- OQ-3 — Art. 18-a stale anchor ("Arts. 97 y 100" derogated by D.L. 230/00): the live document events starting the service tax point (CT 110-115 zone + DTE stack). open
- OQ-4 — Exclusive-use (D.L. 645 Art. 14-III) vs Art. 19 proportional in-country rendition boundary. open
- OQ-5 — Exclusion measurement mechanics: 12-month transfers figure + activo-en-giro valuation conventions. open

### 08_iva-exemptions.md (5)

- OQ-1 — SOQ-54 (vintage): re-verify Arts. 44-46/66/71/167-A/174 + Rgto. Art. 16. open
- OQ-2 — SOQ-56: Art. 46-f BCR-qualification instrument FOUND (101_-105_); `bcr_calificada` = BCR-list membership (dated list, as-of 08-ago-2026). resolved (W18)
- OQ-3 — SOQ-57: Art. 46-k stale SAP citation (D.L. 927-1996 vs current D.L. 614 SIP); substance carried under the current regime. open
- OQ-4 — SOQ-58: Art. 167-A sectorial-politics kill-switch instrument not issued as of 2026-08-22; NULL-valid_to dated row + watch. open
- OQ-5 — Art. 45-i Reglamento de Transporte Terrestre spec gate + the 5-year register's document feed. open

### 09_iva-base-rate.md (4)

- OQ-1 — SOQ-54 (vintage): load-bearing on the 13% rate row (FR-240); re-verify Arts. 47-55 + Rgto. 17-18. open
- OQ-2 — SOQ-40 (design pass): the 2001 FOVIAL control-account chain mapped onto DTE-embedded D1 tributo lines = THIS file's design (FR-244/245); confirm at FOVIAL-law acquisition. open
- OQ-3 — SOQ-39/MOQ-04 (guard note): FOVIAL + COTRANS instruments owned (86_-89_); FR-242's guard unchanged, provenance re-dated ($0.20 = 88_; $0.10 = 89_ Art. 3). resolved (W19)
- OQ-4 — Rate-cutover precision: D.L. 370 (1995) exact vigencia day unpinned; pre-reform 10% rests on the EVID-317 gloss. open

### 10_iva-credit-deductibility.md (3)

- OQ-1 — SOQ-54 (vintage): re-verify Arts. 57-61, 65, 65-A, 70 + the Rgto. survivors. open
- OQ-2 — 58-SMM sector selection (SOQ-18 kin): reads payroll/02 through SV-PAY-FR-022's sector-mapping config; distinct from the ISR 25-SMM rule (02's OQ-002). open
- OQ-3 — CT re-anchors (Rgto. Art. 22 → CT 141; Art. 23 → CT 161; stale Ley anchors) + the printed "ROMANO i)" oddity + CT register surfaces. open

### 11_iva-pro-rata-remanente.md (3)

- OQ-1 — SOQ-54 (vintage): re-verify Arts. 66-70 + Rgto. Arts. 24-25. open
- OQ-2 — R30(c) inciso mapping (tercerización): guía 67_'s pre-D.L.-224-2009 "inciso sexto" vs the current-print exclusion inciso (ordinal discrepancy recorded, substance identical); closes 02's OQ-009 by pointer. open
- OQ-3 — No-sujeta denominator attribution test (config) + F-07 pro-rata casilla set re-verify (132-134 attested vs the 137-138 gloss). open

### 12_iva-adjustments-assets.md (4)

- OQ-1 — SOQ-54 (vintage): re-verify Arts. 62-64, 71-72, 7 g)-i) + Rgto. Art. 26 (medicines lot regime + 3-period windows). open
- OQ-2 — Declaration-modification procedural config (Art. 63 overflow duty; D9-kin; FREP modificatoria surfaces). open
- OQ-3 — Window-anchor divergence: Ley entrega/percepción clock vs the DTE related-document window — both must pass. open
- OQ-4 — Alta-date sourcing for legacy assets (the four-year gate anchor; onboarding config). open

### 13_iva-retentions.md (4)

- OQ-1 — SOQ-54 (vintage, 01_/02_): Art. 94 plazo/venue + Art. 65/Rgto. 23 pointer rows. open
- OQ-2 — CT vintage (SOQ-21 kin): the CT 161/162/162-A/162-B matrix values re-verify. open
- OQ-3 — AT-designation list config-gap (administered data absent from corpus). open
- OQ-4 — $100-floor family scope + the 13% ex-IVA parity reading + Anexo 5 H boundary (FR-313: no extension beyond the inciso-7° catalog). open

### 14_iva-exports-refunds.md (4)

- OQ-1 — SOQ-54 (vintage): re-verify Arts. 74-77 + Rgto. Arts. 2/29/30 (and the 13% cap constant). open
- OQ-2 — Customs-document terminology drift: póliza → DUCA family (SR6 by id); the cap's document set. open
- OQ-3 — DGII Instructivo refund-request formats (config-gap). open
- OQ-4 — Art. 76-2 offset mechanics against other direct taxes (CT-practice confirmation). open

### 15_iva-declaration-interfaces.md (3)

- OQ-1 — SOQ-54 (vintage): Arts. 93-94 most exposed to post-2015 administrative overlay; re-verify + the Art. 81 pair. open
- OQ-2 — Pre-DTE physical-invoice ingestion (D15/D18 history contract; identifier slots per SV-FREP-FR-042/043, no DTE seals). open
- OQ-3 — Decreto 321 kin pointer: *combustible_diferenciado* config owned by fiscal-reporting/05 (rate values = that file's OQ-001). open

### 16_ct-procedures.md (5)

- OQ-1 — EV75 OQ-1: no REFORMAS block in the 75_ print — whether any post-2001 reform of D.E. 117-2001 exists is print-unresolvable; verification note rides every 75_-citing LB. open
- OQ-2 — EV75 OQ-2: Art. 21 10-year prescription + Art. 137 3y/5y reincidencia windows are 2001-print values — inert dated config rows (FR-374/381) until the current CT text is pinned. open
- OQ-3 — EV75 OQ-3: dictamen block (Arts. 58-72) restructured at the CT level post-2001 — FR-395 stays historical/awareness. open
- OQ-4 — EV75 OQ-7: Art. 42 export-factura cross-ref "arts. 81 y 82" looks mis-pointed (consumer-sales book = Art. 83) — print anomaly [sic], no behavior keyed. open
- OQ-5 — EV75 OQ-8, SOQ-06 kin: post-2001 repeal watch (CT Art. 344 ff) — extends to every 75_-cited LB. open
