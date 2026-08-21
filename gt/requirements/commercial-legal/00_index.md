# GT — Commercial-legal requirements index

| Field   | Value |
|--------|-------|
| Country | gt |
| Topic   | commercial-legal |
| Status  | draft (S-GT5 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT5 + controller |
| Updated | 2026-08-21 |

This directory holds the commercial-law half of the S-GT5 (synthesis wave 5)
chart-of-accounts/commercial-legal wave: the *Registro Mercantil* outward
surfaces (arancel fee catalog as dated-2022-label data + the electronic
edicto publication channel created by D-18-2017 reforming CC art. 343), the
comerciante qualification + five-form society taxonomy with capital/
governance rules and the full society lifecycle (including the CC-reform AML
cutover hooks), the títulos valores framework with the factura cambiaria
(FEL-lineage guard) and the one-per-clock prescription ladder that keys the
destruction gate of the sibling matrix, and the AML chain D-51-2001 →
D-67-2001 → D-15-2026 on its dated cutover spine — pre-cutover facts resolve
against 75_ (operative until 16-sep-2026), post-cutover law from 77_
(17-sep-2026), never mixed (R60). The *Código de Comercio* (66_) is cited as
the print consolidated through D-11-2006 with the GOQ-123 verification banner
on every consolidation-sensitive row; the books/legalization half of the same
wave lives in
[../chart-of-accounts/](../chart-of-accounts/00_index.md). Source-to-requirements
coverage: [../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_rm-surfaces.md](01_rm-surfaces.md) | C3 | RM arancel fee catalog (dated-2022-label, re-verify every row — R66) + electronic edicto portal (D-18-2017 → CC art. 343 reform, R64) + edición-6022 channel anatomy (GOQ-131 single-snapshot) | GT-CML-FR-001..025 | 25 | 14 | 9 | 2 |
| [02_sociedades-lifecycle.md](02_sociedades-lifecycle.md) | C4 | Comerciante qualification + five-form society taxonomy + capital/governance (Q-amounts as dated rows — R67) + lifecycle (inscripción→disolución→liquidación) + AML CC-reform cutover hooks (art. 113 SMM fine keyed 2026-09-17) | GT-CML-FR-026..085 | 60 | 24 | 11 | 5 |
| [03_titulos-valores-prescripcion.md](03_titulos-valores-prescripcion.md) | C5 | Títulos valores framework + factura cambiaria (FEL-lineage guard — the comerciante's five-year art. 604 duty) + one-per-clock prescription ladder (cheque 6m, regreso 1y, directa 3y, enriquecimiento 1y …) feeding the destruction gate | GT-CML-FR-086..125 | 40 | 14 | 12 | 3 |
| [04_aml-compliance.md](04_aml-compliance.md) | C6 | AML chain D-51-2001 → D-67-2001 → D-15-2026 on the dated 17-sep-2026 cutover spine (R60): PO catalog, retention ≥5y(+10y digital for financial POs), thresholds deferred to reglamento (GOQ-12), D-62-2001 relationship OPEN (GOQ-132) | GT-CML-FR-126..163 | 38 | 26 | 14 | 4 |
| **Total** | | | **GT-CML-FR-001..163** | **163** | **78** | **46** | **14** |

Cluster map (S-GT5): C3→01, C4→02, C5→03, C6→04 here; C1→`../chart-of-accounts/01`,
C2→`../chart-of-accounts/02` in the sibling directory, whose
`03_retention-destruction-matrix.md` is the wave's GOQ-124 deliverable (a
pure consumer of this directory's C5 prescription clocks and C6 AML retention
rows). FR numbering is sequential per the `GT-CML-FR-` prefix with no gaps
and no renumbering (verified mechanically; totals grep-verified 2026-08-21).

## Authority order (binding, from the wave anchors)

- 66_ = the CCom print, **consolidated through D-11-2006** — every
  consolidation-sensitive row carries the GOQ-123 verification banner (the
  print is current only to the 30-05-2006 consolidation horizon; D-18-2017 on
  CC art. 343 is handled as a dated layer — R64).
- 73_ = RM arancel fee catalog, dated-2022-label: no date or instrument
  number printed — re-verify every row (R66).
- 83_ = single-édición RM portal snapshot (edición 6022, 19-ago-2026) —
  channel anatomy only, never a standing register (GOQ-131).
- 75_/76_/77_ = the dated-layer AML chain keyed to the 17-sep-2026 cutover
  (R60): pre-cutover facts resolve against 75_ (operative until 16-sep-2026),
  never 77_; post-cutover law from 77_ (thresholds deferred to its
  reglamento — GOQ-12); 76_ = lineage only (urgencia window 15-nov-2001 →
  16-dic-2001).

## Open-questions rollup (§7 rows per file, wave-wide)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_rm-surfaces.md | 2 | GOQ-131 (owned) + kin GOQ-122/123/124 |
| 02_sociedades-lifecycle.md | 5 | GOQ-126/127/128 (owned) + kin GOQ-12/123/124/131 |
| 03_titulos-valores-prescripcion.md | 3 | kin GOQ-122/123/124 (no owned id) |
| 04_aml-compliance.md | 4 | GOQ-12/132/133/134 (owned) |
| ../chart-of-accounts/01_books-anchor.md | 4 | GOQ-05/122/123 (owned) + kin GOQ-126/129 |
| ../chart-of-accounts/02_dual-track-habilitacion.md | 6 | GOQ-125/129/130 (owned) + kin GOQ-01/56/126 |
| ../chart-of-accounts/03_retention-destruction-matrix.md | 3 | GOQ-124 (resolved — the deliverable) + kin GOQ-41/123 |
| **Wave total** | **27** | CML 14 + COA 13 |

### GOQ coverage check (S-GT5 register GOQ-122..134 + cross-cutting GOQ-05 + GOQ-12)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.5 (W-GT5). Every id is
**consumed** in at least one §7 OQ row of the wave's files or explicitly
carried kin — none remain unassigned; none listed not-applicable
(grep-verified 2026-08-21).

| GOQ | Consumed in |
|-----|-------------|
| GOQ-05 | ../chart-of-accounts/01 |
| GOQ-12 | 04 (+ 02 here kin) |
| GOQ-122 | ../chart-of-accounts/01 (+ 01/03 here kin) |
| GOQ-123 | ../chart-of-accounts/01 (wave-wide consolidation banner, all seven files) |
| GOQ-124 | ../chart-of-accounts/03 (RESOLVED — the retention/destruction matrix deliverable) |
| GOQ-125 | ../chart-of-accounts/02 |
| GOQ-126 | 02 (+ ../chart-of-accounts/01/02 kin) |
| GOQ-127 | 02 |
| GOQ-128 | 02 |
| GOQ-129 | ../chart-of-accounts/02 (+ 01 there kin) |
| GOQ-130 | ../chart-of-accounts/02 |
| GOQ-131 | 01 (+ 02 here kin) |
| GOQ-132 | 04 |
| GOQ-133 | 04 |
| GOQ-134 | 04 |

Kin ids referenced beyond the owned set (all pre-existing register rows,
owned by other waves): GOQ-01 + GOQ-56 (GT-TAX-FR-231 exposure —
../chart-of-accounts/02), GOQ-41 (../chart-of-accounts/03), GOQ-53
(../chart-of-accounts/03 FR-074 — CT-consolidation-currency kin, owned
by taxation/06), GOQ-104 (../chart-of-accounts/03 FR-068 + §5 — LET
undated-print caveat kin, owned by fiscal-reporting/04), GOQ-11 +
GOQ-77/78 (payroll SMM vintage caveats kin, owned by payroll/03 —
referenced in 02 FR-077/§7 + 04 §7). No other GOQ ids are named by this
wave's files.

## Consumed cross-topic FR ids (read-only)

Consumed by exact FR id, never re-derived: taxation GT-TAX-FR-066, 214, 216,
217, 230, 231, 232, 234; fiscal-reporting GT-FIN-FR-020, 086, 087, 088, 089,
104, 118; payroll GT-PAY-FR-058, 063 (SMM fine base for the art. 113
CC-reform row — consumed by id, never hardcoded); e-invoicing GT-EINV-FR-203
(pointer only, outcome-only).

## R-ledger bindings (as instantiated in this wave)

- R45 — CCom dated identity (vigencia 1971-01-01; consolidation horizon
  30-05-2006) — ../chart-of-accounts/01.
- R60 — AML dated cutover spine: regime rows keyed 2026-09-17; pre-cutover
  facts from 75_, post-cutover from 77_, never mixed — 04 (+ 02 art. 113 row,
  + the sibling matrix's AML retention rows).
- R61 — no quetzal-denominated AML threshold in the 2001 layer — 04.
- R62 — CCom vocabulary guard: "autorización" (art. 372) is the CCom word;
  "habilitación" never appears in the CCom — ../chart-of-accounts/02.
- R63 — negative sweep of the consolidated CCom text: no statutory plan de
  cuentas, no copiador de correspondencia, no electronic-bookkeeping clause
  — ../chart-of-accounts/01 (+ 03 there).
- R64 — pre-D-18-2017 CC arts. 341/343 print texts superseded by the
  electronic-publication reform — 01 (+ 02).
- R65 — D-2946 old-code appendix guard (pp. 215-301 never current law) —
  03 (+ ../chart-of-accounts/01/03).
- R66 — RM arancel dated-2022-label: re-verify every fee row — 01 (+
  ../chart-of-accounts/02 books-fee row).
- R67 — Q-amounts in the sociedades file carried as dated rows (figures
  unindexed in the print) — 02.
- R68 — the 2001 one-day urgencia layer of the AML chain — 04.
- R69 — ML offence intentional-only — 04.
- R70/R71 — D-62-2001 relationship stays OPEN (GOQ-132, never modeled as
  law-sourced) — 04.

R46 note (n/a here): this wave names no ISR forms — SAT-7121 is a SAT
habilitación form, NOT an ISR form, and the R46 ISR-identity ledger does not
attach to any row of this wave.

## CSV sidecars

None in this wave — SMM values are consumed by id from the payroll CSV
sidecars (via GT-PAY-FR-058/063), never hardcoded.

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_rm-surfaces.md | 14 | 9 |
| 02_sociedades-lifecycle.md | 24 | 11 |
| 03_titulos-valores-prescripcion.md | 14 | 12 |
| 04_aml-compliance.md | 26 | 14 |
| **Total** | **78** | **46** |
