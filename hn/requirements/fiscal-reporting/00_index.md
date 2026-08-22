# HN — Fiscal reporting requirements index

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | approved (V-HN1 validation wave 2026-08-20; see EXTRACTION_PLAN wave log) |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

This directory holds the S-HN3 (synthesis wave HN-3) fiscal-reporting
requirements: the OVI/SW declaration chassis and shared due-day engine, the
DJIMR/DMR per-código retention engine with the 25-code catalog as a dated CSV
sidecar, the DMC form-527 purchases line contract, the OTCD tarjetas 215/523
pair, the ISV determinativa 201 + credit engine + Régimen Simplificado 202,
the EEFF form-535 gate, the 30-abril ISR annual package (102/103/AS/ATN),
the ganancias-de-capital event family (119/120/152/154), the selectivo
declaration family (203/211/210/205/204/259) with the IPC value chain, the
TP 545 + informativas 541/542/543, and the contribuciones sector family
(502/503/504/506/509/511/107). Built from master-index clusters F1-F11 (W2
evidence, EVID-072..185); S-HN1 rates and S-HN2 document mechanics are
consumed by id, never re-derived. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md) (V-HN1 gate 1, script-checked).

## Files & FR ranges

| File | Scope (clusters) | FR range | FRs | LBs | ACs | OQs |
|------|------------------|----------|-----|-----|-----|-----|
| [01_filing-chassis-due-days.md](01_filing-chassis-due-days.md) | OVI/SW chassis, declaration lifecycle (alta→borrador→juramento→acuse/CSV+QR→estado→Pagar/Boletín), dual-channel sticky modality, rectificativa frame, D-H3.2 go-live reconciliation + the SHARED due-day/hábil-calendario engine (F1) | HN-FREP-FR-001..032 | 32 | 21 | 16 | 14 |
| [02_djimr-retention-declarations.md](02_djimr-retention-declarations.md) | DJIMR/DMR per-código monthly informativa → SER determinativa, 25-code catalog (`djimr_retention_codes.csv` sidecar), de-oficio rectificativa propagation, per-código casilla surfaces 111-138/217 (F2); **W6: D. 110-93 original `117_` — código-115 Art. 12 L50,000 monto activated (FR-073)** | HN-FREP-FR-041..076 | 36 | 22 | 18 | 24 |
| [03_dmc-527-purchases.md](03_dmc-527-purchases.md) | DMC form 527 all-purchases informativa: sheets 527-52/53/54, CAI+4-segment line key, dual dates, crédito/costos/gastos/no-deducible, deadline chain 10d→20d→5d, sujetos, compras-eventuales registration duty (F3) | HN-FREP-FR-086..115 | 30 | 14 | 16 | 9 |
| [04_otcd-tarjetas-215-523.md](04_otcd-tarjetas-215-523.md) | OTCD card-family declarations: 215 determinativa (10%-of-ISV − devolución 8%, pago-parcial) + 523 SW-only per-transaction informativa + SAR-240-2024 IX-XIII per-merchant detail; both OUTSIDE the DJIMR catalog (R-H16) (F4) | HN-FREP-FR-121..148 | 28 | 13 | 15 | 9 |
| [05_isv-201-202.md](05_isv-201-202.md) | ISV determinativa 201: débito engine, 30-casilla crédito map, DMC-fed Sección B, retention-credit editability, hecho-generador period assignment + 202 Régimen Simplificado annual INFORMATIVE (R-H23) (F5) | HN-FREP-FR-151..187 | 37 | 18 | 19 | 14 |
| [06_eeff-535-gate.md](06_eeff-535-gate.md) | EEFF inform 535 (A-D panels, Jan-1→Apr-30), EEFF-before-DJ gate FY2024+ (SAR-619-2024), per-socio/per-provider/per-bank detail, Art. 11 CxC validation, ATN autofill feed (F6) | HN-FREP-FR-191..218 | 28 | 9 | 16 | 11 |
| [07_isr-annual-102-103.md](07_isr-annual-102-103.md) | The 30-abril package: 102 PN (vinculación auto-flow, credit panel) + 103 PJ (ISV-split revenue, 50% loss gate, 535 prerequisite) + AS 5% RNG>L1M PJ-only + ATN 1% w/ L3M exemption + 75_ minimum-exempt suspension (F7); **W6: D. 54-96 `118_` job-credit statute (LB-015)**; **W9: the AS FY2014+ re-establisher statute-anchored (D. 278-2013 Art. 15, LB-018)** | HN-FREP-FR-221..264 | 44 | 17 | 18 | 16 |
| [08_gc-events-119-120-152-154.md](08_gc-events-119-120-152-154.md) | GC event declarations: 119 (10% único, base max(agreed,market)−mejoras−legalización), ZOLITUR 120 4%, Tradición 152 1.5%, Revaluación 154 6% elective (F8) | HN-FREP-FR-266..295 | 30 | 10 | 17 | 13 |
| [09_selectivo-declarations.md](09_selectivo-declarations.md) | Selectivo declarations 203 (**W6: D. 58-1982 acquired `115_` — 1982 cc-tier canasta + 1995 flat-20% states in corpus, live-period gap narrowed OQ-001**) / 211 cigarettes per-millar / 210 gaseosas / 205 alcoholes / 204 cerveza / 259 turística 4% (**W6: D. 131-98 acquired `116_` — Art. 43 original, anti-cascading exclusion encoded, OQ-010 resolved**) + the IPC value chain 172-2022→014-2023→218-2024 as DIRECT-cited dated rows (F9) | HN-FREP-FR-296..325 | 30 | 12 | 20 | 14 |
| [10_tp-545-informativas.md](10_tp-545-informativas.md) | TP 545 DJIAPT (USD 1M pequeño gate, 56 op types → 10 annexes, interquartile range, Ajuste-PT write-back) + informativas 541 socios / 542 alquiler / 543 municipalidades (F10) | HN-FREP-FR-326..360 | 35 | 13 | 16 | 24 |
| [11_contribuciones-sector.md](11_contribuciones-sector.md) | LSP/sector family: monthly trio 502 telefonía 1% / 503 franquicias 0.5% / 504 casinos 1% + annual quartet 506 coops 3.6% / 509 CONSUCOOP 15%+0.5% floor / 511 sector social 15% / 107 educativas 10%; 506-vs-509 boundary BLOCKED on statutes (F11) | HN-FREP-FR-361..393 | 33 | 12 | 18 | 21 |
| **Total** | | HN-FREP-FR-001..393 | **363** | **164** | **189** | **170** |

Numbering note: FR ranges pre-allocated per file (subagent dispatch
pattern); unused tails (033-040, 077-085, 116-120, 149-150, 188-190,
219-220, 265... reserved) stay reserved for later additions — no
renumbering. V-HN1 corrections: 076 consumed (FR-076 código-111 12-months
split from FR-041); 294-295 were NEVER reserved — file 08's allocation runs
266..295 contiguous (index misprint). The `djimr_retention_codes.csv` sidecar carries the 25-code
retention catalog (EVID-077, SAR-238-2024 CUARTO) with rates/bases/
channels/deadlines/regime-validity columns; it carries no FRs of its own.

## Wave rulings & carries (controller notes)

- **Consumption discipline (verified):** every rate/engine owned by
  S-HN1/S-HN2 is cited by id — ISR retention engines + export data shape
  (HN-TAX-FR-121..153), 22-A three dated regimes (HN-TAX-FR-081..092), GC
  10%/4% (HN-TAX-FR-093..100), ISV core (HN-TAX-FR-211..255), selectivo
  law side (HN-TAX-FR-194..200), CAI/grammar/code-10 guard
  (HN-EINV-FR-009..022), comprobante-retención (HN-EINV-FR-139/140);
  the plantilla↔código-111 casilla mapping (origin `32_ OQ-1`) is the
  DMR-validation surface owning taxation/04 OQ-006's carry.
- **Rulings applied:** R-H16 (tarjetas outside catalog — FR-075 guard),
  R-H17/R-H18 (DMC 5 días, manuals stale), R-H25 (form 527), R-H27
  (71_ per-row), R-H28 (monthly 502/503/504), R-H31 (DMR≡DJIMR dated
  regime rows), R-H32 (22-A by id), R-H33 (116 = 100%-of-ISV), R-H36
  (DMC-first), R-H22 (devolución 8% alive), R-H23 (202 informative),
  R-H29/R-H30 (ATN 1% / AS 5%), R-H9 (composite gate by id).
- **One sanctioned direct-cite exception:** file 09's IPC value chain
  (98_/99_/100_) has NO evidence pass — cited as direct source LBs
  (LB-008..010), page-1-verified at synthesis 2026-08-20, flagged in
  file 09 OQ-013; values as printed, never re-derived. Controller
  re-verified values against the raw extractions (571.34 / 600.99 /
  5.32% / per-liter rows — all present).
- **Open conflicts of record (never resolved silently):** GC non-resident
  2% vs 4% (`46_ OQ-1`); ZOLITUR Art. 4 vs Art. 25 (`29_ OQ-2`); 138
  deadline duality (both modeled, `38_ OQ-2`); 541/542 deadline drifts;
  535 balance-only vs Balance+GyP (`67_ OQ-1`); 509 Mar-30 vs "3 meses";
  116 base-legal moving budget-law target (`36_ OQ-1`). **D. 117-2021
  identity (`63_ OQ-4`) RESOLVED at V-HN1** via the `89_` evidence read
  (EVID-334; LB-012; OQ-004 resolved) — TP obligation reaches only
  related parties, never the regime entities themselves.
- **Blocking OQs (V-HN1 wording fix — three, not one, all scope-qualified):**
  file 11's 506-vs-509 boundary (`60_ OQ-1`, statute texts unacquired — the
  only UNQUALIFIED yes); file 03's OQ-003 (yes, retention-engine scope —
  compras-eventuales rate) and file 09's OQ-001 (yes, 203-computation
  scope — D. 58-1982 canasta) are qualified yes-blockers inside their
  engines; SEE remains the cross-wave blocker (S-HN2, lead 1).
- **Cross-wave dependencies:** S-HN4 payroll (delivered) consumes file
  02's 111 columns + file 01's chassis; the V-HN1 validation wave
  (COVERAGE.md + adversarial review) ran 2026-08-20 — findings adjudicated
  in the EXTRACTION_PLAN wave log; `01_ OQ-6`
  FY2026 composite gate re-pins from file 07's window rows when SAR
  prints the value.

## Open-questions summary

169 OQ rows (wave total, 168 open — OQ-004 resolved at V-HN1;
the D. 117-2021 lead leg is retired), highest-leverage LEADs: Reglamento Ley ISR
("Acuerdo N°799" — Art. 84 CxC validation + Arts. 31/32 GC + Arts. 11-13
vinculación), SAR-236-2024 DÉCIMO OCTAVO (channel list), D. 51-2003
(AS/ATN instruments), D. 58-1982 (203 canasta/tarifas), D. 131-98
(259), TP family (D. 232-2011 + 027-2015 + DEI-SG-004-2016 +
SAR-653-2023), LSP statutes (D. 105-2011 + 1775-2011 + D. 31-2018 +
D. 53/92-2015 + D. 131-2018), compras-eventuales retention rate
(`18_ OQ-6`), devolución-8% when-it-applies instruments. Full text per
file §7; register mapping to master-index C2 recorded per file.
