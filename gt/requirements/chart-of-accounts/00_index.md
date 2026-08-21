# GT — Chart-of-accounts requirements index

| Field   | Value |
|--------|-------|
| Country | gt |
| Topic   | chart-of-accounts |
| Status  | draft (S-GT5 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT5 + controller |
| Updated | 2026-08-21 |

This directory holds the chart-of-accounts half of the S-GT5 (synthesis wave
5) chart-of-accounts/commercial-legal wave: the CCom merchant-books anchor
(no statutory plan de cuentas — *partida doble* + PCGA make the chart a
PCGA-governed configuration surface, with the four-book registry, entry
invariants and the balance/signature cycle as the negative-anchored C1 base),
the dual-track legalization model (RM *autorización* under CCom art. 372 +
SAT *habilitación* under CT/RLIVA/LET instruments, tax-law books, RLIVA book
specs and the art. 29-"A" electronic-books bridge), and the wave's GOQ-124
deliverable — the 8-row max-per-object retention/destruction matrix + gate
engine, a pure consumer of the wave's conservation/prescription rows. The
*Código de Comercio* (66_) is cited as the print consolidated through
D-11-2006 with the GOQ-123 verification banner on every consolidation-sensitive
row; the commercial-law half of the same wave (RM surfaces, sociedades,
títulos valores, AML) lives in
[../commercial-legal/](../commercial-legal/00_index.md). Source-to-requirements
coverage: [../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_books-anchor.md](01_books-anchor.md) | C1 | CCom books/PCGA anchor: art. 368 (texto D-40-99) four-book set, voluntary auxiliary books, entry invariants (Spanish/moneda nacional, no blanks, documento fehaciente), balance/signature cycle, mandatory-contador thresholds, conservation/destruction rows for the matrix; NEGATIVES: no statutory COA, no copiador de correspondencia (R63), no electronic-bookkeeping clause | GT-COA-FR-001..033 | 33 | 20 | 12 | 4 |
| [02_dual-track-habilitacion.md](02_dual-track-habilitacion.md) | C2 | RM autorización + SAT habilitación dual-track model (R62 vocabulary guard); tax-law books (IVA/ISR/IGSS), RLIVA book specs, SAT-7121 habilitación mechanics from 60_ (GOQ-129 banner), art. 29-"A" electronic-books bridge, 73_ books-fee row (R66) | GT-COA-FR-034..060 | 27 | 11 | 11 | 6 |
| [03_retention-destruction-matrix.md](03_retention-destruction-matrix.md) | GOQ-124 | GOQ-124 deliverable: 8-row max-per-object retention/destruction matrix + gate engine (pure consumer — CCom conservation LBs, per-clock prescription ladders from `../commercial-legal/03_titulos-valores-prescripcion.md`, AML retention regimes keyed to the 17-sep-2026 cutover) | GT-COA-FR-061..074 | 14 | 9 | 9 | 3 |
| **Total** | | | **GT-COA-FR-001..074** | **74** | **40** | **32** | **13** |

Cluster map (S-GT5): C1→01, C2→02 here; C3→`../commercial-legal/01`,
C4→`../commercial-legal/02`, C5→`../commercial-legal/03`, C6→`../commercial-legal/04`
in the sibling directory. `03_retention-destruction-matrix.md` is not a
cluster file — it is the wave's GOQ-124 deliverable, built as a pure consumer
of C1 conservation rows, C5 prescription clocks and C6 AML retention rows. FR
numbering is sequential per the `GT-COA-FR-` prefix with no gaps and no
renumbering (verified mechanically; totals grep-verified 2026-08-21).

## Authority order (binding, from the wave anchors)

- 66_ = the CCom print, **consolidated through D-11-2006** — every
  consolidation-sensitive row carries the GOQ-123 verification banner (the
  print is current only to the 30-05-2006 consolidation horizon; later
  reforms of the same code, e.g. D-18-2017 on CC art. 343, are handled as
  dated layers in the sibling directory — R64).
- 60_ = undated illustrative orientation (≥30-oct-2019 SAT print) —
  orientation only, never statutory (GOQ-129 banner).
- 73_ = RM arancel fee catalog, dated-2022-label: no date or instrument
  number printed — re-verify every row (R66).
- 75_/76_/77_ = the dated-layer AML chain keyed to the 17-sep-2026 cutover
  (R60); pre-cutover facts resolve against 75_, never 77_, and vice versa.
- 83_ = single-édición RM portal snapshot (edición 6022, 19-ago-2026) —
  channel anatomy only (GOQ-131).

## Open-questions rollup (§7 rows per file, wave-wide)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_books-anchor.md | 4 | GOQ-05/122/123 (owned) + kin GOQ-126/129 |
| 02_dual-track-habilitacion.md | 6 | GOQ-125/129/130 (owned) + kin GOQ-01/56/126 |
| 03_retention-destruction-matrix.md | 3 | GOQ-124 (resolved — the deliverable) + kin GOQ-41/123 |
| ../commercial-legal/01_rm-surfaces.md | 2 | GOQ-131 (owned) + kin GOQ-122/123/124 |
| ../commercial-legal/02_sociedades-lifecycle.md | 5 | GOQ-126/127/128 (owned) + kin GOQ-12/123/124/131 |
| ../commercial-legal/03_titulos-valores-prescripcion.md | 3 | kin GOQ-122/123/124 (no owned id) |
| ../commercial-legal/04_aml-compliance.md | 4 | GOQ-12/132/133/134 (owned) |
| **Wave total** | **27** | COA 13 + CML 14 |

### GOQ coverage check (S-GT5 register GOQ-122..134 + cross-cutting GOQ-05 + GOQ-12)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.5. Every id is **consumed**
in at least one §7 OQ row of the wave's files or explicitly carried kin —
none remain unassigned; none listed not-applicable (grep-verified 2026-08-21).

| GOQ | Consumed in |
|-----|-------------|
| GOQ-05 | 01 |
| GOQ-12 | ../commercial-legal/04 (+ 02 there kin) |
| GOQ-122 | 01 (+ ../commercial-legal/01/03 kin) |
| GOQ-123 | 01 (wave-wide consolidation banner, all seven files) |
| GOQ-124 | 03 (RESOLVED — the retention/destruction matrix deliverable) |
| GOQ-125 | 02 |
| GOQ-126 | ../commercial-legal/02 (+ 01/02 here kin) |
| GOQ-127 | ../commercial-legal/02 |
| GOQ-128 | ../commercial-legal/02 |
| GOQ-129 | 02 (+ 01 kin) |
| GOQ-130 | 02 |
| GOQ-131 | ../commercial-legal/01 (+ 02 there kin) |
| GOQ-132 | ../commercial-legal/04 |
| GOQ-133 | ../commercial-legal/04 |
| GOQ-134 | ../commercial-legal/04 |

Kin ids referenced beyond the owned set (all pre-existing register rows,
owned by other waves): GOQ-01 + GOQ-56 (GT-TAX-FR-231 exposure — 02),
GOQ-41 (03), GOQ-53 (03 FR-074 — CT-consolidation-currency kin, owned by
taxation/06), GOQ-104 (03 FR-068 + §5 — LET undated-print caveat kin,
owned by fiscal-reporting/04), GOQ-11 + GOQ-77/78 (payroll SMM vintage
caveats kin, owned by payroll/03 — referenced in
../commercial-legal/02 FR-077/§7 + ../commercial-legal/04 §7). No other
GOQ ids are named by this wave's files.

## Consumed cross-topic FR ids (read-only)

Consumed by exact FR id, never re-derived: taxation GT-TAX-FR-066, 214, 216,
217, 230, 231, 232, 234; fiscal-reporting GT-FIN-FR-020, 086, 087, 088
(via the `086/087/088` set in 02), 089, 104, 118; payroll GT-PAY-FR-058,
063 (SMM fine base in the sibling directory's CC-reform rows); e-invoicing
GT-EINV-FR-203 (pointer only, outcome-only).

## R-ledger bindings (as instantiated in this wave)

- R45 — CCom dated identity (vigencia 1971-01-01; consolidation horizon
  30-05-2006) — 01.
- R60 — AML dated cutover spine: regime rows keyed 2026-09-17; pre-cutover
  facts from 75_, post-cutover from 77_, never mixed —
  ../commercial-legal/04 (+ 03 here for the AML retention rows).
- R61 — no quetzal-denominated AML threshold in the 2001 layer —
  ../commercial-legal/04.
- R62 — CCom vocabulary guard: "autorización" (art. 372) is the CCom word;
  "habilitación" never appears in the CCom — 02.
- R63 — negative sweep of the consolidated CCom text: no statutory plan de
  cuentas, no copiador de correspondencia, no electronic-bookkeeping clause
  — 01 (+ 03).
- R64 — pre-D-18-2017 CC arts. 341/343 print texts superseded by the
  electronic-publication reform — ../commercial-legal/01 (+ 02 there).
- R65 — D-2946 old-code appendix guard (pp. 215-301 never current law) —
  01, 03 (+ ../commercial-legal/03).
- R66 — RM arancel dated-2022-label: re-verify every fee row —
  ../commercial-legal/01 (+ 02 here, books-fee row).
- R67 — Q-amounts in the sociedades file carried as dated rows (figures
  unindexed in the print) — ../commercial-legal/02.
- R68 — the 2001 one-day urgencia layer of the AML chain —
  ../commercial-legal/04.
- R69 — ML offence intentional-only — ../commercial-legal/04.
- R70/R71 — D-62-2001 relationship stays OPEN (GOQ-132, never modeled as
  law-sourced) — ../commercial-legal/04.

R46 note (n/a here): this wave names no ISR forms — SAT-7121 is a SAT
habilitación form, NOT an ISR form, and the R46 ISR-identity ledger does not
attach to any row of this directory.

## CSV sidecars

None in this wave — SMM values are consumed by id from the payroll CSV
sidecars (via GT-PAY-FR-058/063), never hardcoded.

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_books-anchor.md | 20 | 12 |
| 02_dual-track-habilitacion.md | 11 | 11 |
| 03_retention-destruction-matrix.md | 9 | 9 |
| **Total** | **40** | **32** |
