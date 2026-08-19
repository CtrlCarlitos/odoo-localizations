# SV — Special regimes (ZF / DPA / LSI / customs clocks / TAN interface / DUCA / sanctions / FOVIAL) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft (S7, 2026-08-19) |
| Authors | Controller + S7 subagent wave |
| Updated | 2026-08-19 |

This directory holds the S7 (synthesis wave 7) special-regimes requirements:
the ZF/DPA/LSI beneficiary model with its D15 per-beneficiary dated-row spine
(regime × role × activity admission × location track × acuerdo D.O. date), the
ZF/DPA exemption ladders and exception-goods gates, the LSI indefinite
exemptions with 17b_ Art. 22 local-market caps and the semestral auditor
dictamen, the customs clocks (12m ZF vs 24m LSI admisión temporal, traslados,
destinación, expedición), the TAN/IVA interface (0%+Arts. 76/77 routing,
internaciones on the non-national component, 1.5%/1% retentions), the DUCA
62-field declaration model with teledespacho/$18 tasa/presumed valuation, the
regime obligations and SMM-priced sanctions, and the FOVIAL/COTRANS
quantity-based contributions. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_regime-framework.md](01_regime-framework.md) | Territorial-regime taxonomy (ZF vs DPA never unified; parque vs centro), beneficiary profile as the D15 row key, MINEC/DGA/DGII/ONI authorization architecture, activity-admission config (SAC scope + Art. 6 negative list; LSI letters a)-j) + co-located non-benefited 1)-11)), qualification requisitos as dated rows (17-A/19-A/19-B/22/23), breach state machine (revocación vs suspensión with clock running; LSI third-grave), MINEC procedure clocks, declarante roles (agente vs apoderado especial aduanero), área-metropolitana stale-static list | SV-SPE-FR-001..022 | 22 | 25 | 7 | 4 |
| [02_zf-exemption-schedules.md](02_zf-exemption-schedules.md) | THE canonical D15 consumer: usuario ISR ladder 100% 15y(metro)/20y(fuera)→60%→40%; municipal 100→90→75% indefinite; DPA 10y/15y→60%→40%; desarrollista flat; administrador via Art. 54-C grandfathering only (Arts. 14+15 derogated as printed); 12-ejercicio dividend window; +5y/+10y extensions; exception-goods DM/CCF-paid-IVA gates; capital-goods 5y free-transfer; Quincena-25 certificado consumption (SV-TAX-FR-174 by id) + F-11 v20 pointer | SV-SPE-FR-023..041 | 19 | 17 | 11 | 6 |
| [03_lsi-regime.md](03_lsi-regime.md) | LSI exemption shapes (usuario directo/centro ISR + municipal INDEFINITE until cessation — open D15 rows), franquicia arancelaria, requisito tracking, usuario-indirecto consignment liability, 17b_ Art. 22 local-market caps 50/40/30 (VENTAS basis), semestral auditor dictamen regime, 90%-Salvadoran staffing quota, CT-158-II carve-out | SV-SPE-FR-042..063 | 22 | 16 | 11 | 6 |
| [04_customs-clocks.md](04_customs-clocks.md) | ZF/DPA 12-month improrrogable per-DM clock vs LSI 24-month+1y clock (NEVER unified), traslado sub-clocks (def ≤12m / temp ≤6m / ZF→TAN 2m), 3-días-hábiles formalización, nota de remisión/NRE pointer, perfeccionamiento pasivo ≤6m, destinación 20 días hábiles → abandono, expedición status, residuales/palets disposition, DUCA field-14 regime-expiry feed, DUCA-F 30-días-hábiles FAUCA validity clock | SV-SPE-FR-064..081 | 18 | 15 | 12 | 6 |
| [05_tan-iva-interface.md](05_tan-iva-interface.md) | Internaciones pay duties on the non-national component only (entry-value/CIF floor), TAN→ZF/DPA = 0% IVA + Arts. 76/77 (annex-3 tipo-11 bucket SV-FREP-FR-073 by id), not-necessary goods full 13%, B2B intra-regime no IVA, comercializador TAN-sale incentive loss, LSI export test routing, LSI→ZF/DPA cross-regime FCF-documented services, local-LSI 1.5% ISR + 1% IVA retentions (SV-TAX-FR-121..129 by id), SS-solvency gates (Art. 9-A electronic; 74_ 11-A kin) | SV-SPE-FR-082..102 | 21 | 8 | 10 | 4 |
| [06_customs-declarations.md](06_customs-declarations.md) | DUCA 62-field record model (D/T/F; field 14 = "Fecha de vencimiento del régimen" as printed), declaración/certificación de origen, teledespacho chassis + declarante roles, autoliquidación/selectividad/inspection, $18 tasa (dated 2012 row), presumed flete/seguro 1.25/1.50/10%, manifiesto pre-arrival, anulación clocks, 48h simplified withdrawal, courier bands, consultas/advance rulings, 5-year caducidad + retention (SV-CML-FR-028 note), Panamá SIECA transmission | SV-SPE-FR-103..129 | 27 | 20 | 11 | 6 |
| [07_obligations-reporting-sanctions.md](07_obligations-reporting-sanctions.md) | ZF obligations (electronic inventory + descargo register, semestral MINEC informe, 30-day cambio/cierre, cost records for TAN-sold goods, insumo-vs-producto-compensador register), ZF sanction ladder (SMM-priced via payroll/02 by id), SS-payment breach suspension, LSI obligations (17b_ Art. 28 inventory-register contract, Art. 44 annual report), LSI sanction ladder (3/30/40 SMM; third-grave revocatoria), SMM de mayor cuantía config default (SOQ-33) | SV-SPE-FR-130..165 | 36 | 22 | 12 | 5 |
| [08_fovial-cotrans.md](08_fovial-cotrans.md) | FOVIAL $0.20/galón per-unit special contribution on diesel/gasolinas (excl. aviación) with the IVA-exclusion guard (never in base imponible), separate document fila/casilla, B2B control-account chain (RETENCIÓN/CTA POR COBRAR-FOVIAL), own-consumption ISR deductibility (SV-TAX-FR-045 by id), COTRANS value-flagged config surface (instrument absent), D1-tributo DTE wiring + F-07 fuel-annex feeds by id | SV-SPE-FR-166..175 | 10 | 7 | 6 | 5 |
| **Total** | | SV-SPE-FR-001..175 | **175** | **130** | **80** | **42** |

Numbering note: FR numbering is wave-sequential within the **SV-SPE** prefix
(001-175, no gaps, no renumbering); consumers cite by FR id, never by
restatement. D15 per-beneficiary dated rows (acuerdo D.O. date + location
track + role) are the wave's spine — every exemption value, requisito,
percentage, tasa and SMM figure is a dated config row with instrument
provenance, never a global constant.

## Cross-topic consumer map

**Consumed FROM this wave** (other topics' FRs consume SV-SPE ids or wave
authorities by id):

- **SV-TAX-FR-174** (taxation/01 — Quincena-25 FY-2026 Certificado de Crédito
  Tributario route `certificado_zf_dpa_lsi`) consumes the regime-profile
  discriminator contributed by **SV-SPE-FR-039** (`02` §3.9): this wave
  contributes ONLY the ZF/DPA/LSI profile link; computation, remanent,
  issuance and negotiability stay owned by taxation.
- **SV-FREP-FR-073** (fiscal-reporting/03 — F-07 annex-3 tipo-11 ZF/DPA
  purchases bucket) consumes **SV-SPE-FR-087** (`05`): 12_ Art. 25 (0% IVA +
  Ley IVA Arts. 76/77) is that bucket's printed authority.
- **SV-CML-FR-028** (commercial-legal/02 §3.7 — canonical retention matrix)
  receives the customs 5-year caducidad/records row as a note from
  **SV-SPE-FR-126** (`06`): update-by-note only, matrix never restated.

**Consumed BY this wave** (by id, never restated):

- **SV-FREP-FR-202..204** — días-hábiles calendar engine (`01`/`02`/`03`/
  `04`/`06`/`07` procedure clocks and dictamen deadlines).
- **SV-PAY-FR-022 + `smm_2025.csv`** — SMM sidecar rows for the
  SMM-de-mayor-cuantía sanction config default (`07`, SOQ-33); payroll/05-06
  SS cotización/payment records feed the solvencia gates (SV-PAY-FR-066/072/
  093, `05` FR-102).
- **SV-TAX-FR-121..129** — retention engine for the LSI local-service
  1.5%/1% pair (`05`); **SV-TAX-FR-045** — Art. 29.6 own-consumption FOVIAL
  deductibility (`08`).
- **SV-EINV-FR-001/017/019..021/026/042/046** — DTE type contracts, D1
  tributo wiring and emitter gates consumed by `02`/`04`/`05`/`06`/`08`;
  the e-invoicing doc surfaces are read as references: NRE for non-dominion
  traslados (`04` FR-070), FCF for LSI→ZF/DPA cross-regime services
  documentation (`05`), FEX/FEXE for the DUCA-F export pairing (`06`).
- **SV-FREP-FR-124..129 + SV-FREP-FR-020** — F-07 fuel annexes 13-14 and the
  casilla-525 credit surface fed by `08` (data feed only, computation stays
  fiscal-reporting's).

## Open-questions rollup (in-file OQ-n ↔ master-index SOQ-30..45)

Status legend: all **42 OQs open** (0 resolved; `08` OQ-5 records its MOQ-04
linkage — FOVIAL half resolved-by-chain, COTRANS half stays open with the
instrument). Master-index SOQ register:
[§S7 open questions](../../.extractions/00_MASTER_INDEX.md).

| File | OQs | Mapping (in-file OQ → SOQ / kin) |
|------|-----|----------------------------------|
| 01 | 4 | OQ-1 SOQ-30 · OQ-2 SOQ-43 · OQ-3 SOQ-31 · OQ-4 declarante config-gap (74_ Art. 9 exam/fianza DACG delegation — no SOQ) |
| 02 | 6 | OQ-1 dividend-interaction express-suppression encoding (EVID-253, in-wave) · OQ-2 F-11 v20 acquisition watch (kin taxation/01 OQ-007 + payroll/08 OQ-004) · OQ-3 SOQ-30 · OQ-4 administrador benefit authority (Arts. 14+15 derogated; 54-C only — SOQ-30 kin) · OQ-5 transitorias 54-D/54-E/54-F config scope · OQ-6 concejos-municipales benefit slots (config) |
| 03 | 6 | OQ-1 SOQ-37 · OQ-2 SOQ-38 · OQ-3 SOQ-42 · OQ-4 CT-158-II cross-check (vs taxation/04 LB-018 / SV-TAX-FR-126) · OQ-5 SOQ-30 · OQ-6 DGII dictamen formularios config-gap (17b_ Arts. 48/50-55) |
| 04 | 6 | OQ-1 SOQ-32 · OQ-2 SOQ-36 kin + DUCA field-anchor correction (field 14 as printed) · OQ-3 SOQ-45 kin (field 31) · OQ-4 SOQ-30 · OQ-5 pre-expiry warning = operational default · OQ-6 T4/T6 DUCA-F-FAUCA ownership split |
| 05 | 4 | OQ-1 SOQ-37 · OQ-2 non-national-component determination = DGA-practice config-gap · OQ-3 SOQ-30 (+ IVA-core wave verification of Arts. 54/75-77 anchors) · OQ-4 Art. 9-A electronic-solvency DACG mechanics |
| 06 | 6 | OQ-1 SOQ-34 · OQ-2 SOQ-35 · OQ-3 SOQ-36 · OQ-4 SOQ-45 · OQ-5 SOQ-30 · OQ-6 SOQ-32 kin (shared with `04` OQ-1) |
| 07 | 5 | OQ-1 SOQ-33 · OQ-2 SOQ-32 · OQ-3 SOQ-44 · OQ-4 SOQ-31 kin · OQ-5 SOQ-30 |
| 08 | 5 | OQ-1 SOQ-39 (FOVIAL law absent; provenance chain via 31_) · OQ-2 SOQ-39 COTRANS half + MOQ-04 half-open · OQ-3 SOQ-40 (B2B chain design pass → IVA-core wave) · OQ-4 SOQ-30 adapted (2001 vintage, SOQ-22 kin) · OQ-5 MOQ-04 linkage note (master index Section C row) |

SOQ-30 rides every regime LB of the wave as the verification preamble (all
consolidations end 2012-2013; text cited as printed). Acquisition candidates
opened by the wave: Reglamento General Ley ZF (SOQ-31), LESIA (SOQ-32), DUCA
user manual (SOQ-36), FOVIAL/COTRANS instruments (SOQ-39), D.L. 598-2020 +
tail laws (SOQ-41), F-11 v20 print.

## Wave-prep provenance

Built from W13 evidence (EVID-251..274) via master-index clusters SR1-SR8 and
the SOQ-30..45 register — see
[§S7-A](../../.extractions/00_MASTER_INDEX.md) (special-regimes authority
order, citation rule and per-cluster covers). The former wave-prep stub's
input inventory, binding decisions (D15 as-of doctrine, §5 ruling 42) and W11
discoveries (Quincena-25 certificado, F-11 v20) are consumed into the files
above; outstanding acquisition candidates live in the master index (SOQ
register + `sources/README.md` numbering watch). Cross-topic source coverage:
[../COVERAGE.md](../COVERAGE.md).
