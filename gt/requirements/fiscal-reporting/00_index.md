# GT — Fiscal-reporting requirements index

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft (S-GT4 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

This directory holds the S-GT4 (synthesis wave 4) fiscal-reporting
requirements: the SAT form inventory + channel model (48_ with the R46-corrected
ISR form identities and the dated-validity ledger), the Retenciones Web
operating system (IVA + ISR constancias, carga masiva, agent population), the
pequeño contribuyente regime chain + compras-y-ventas libro (55_/61_ as dated
layers), the LET electronic books + Informe Electrónico de Compras y Ventas
(record-level layouts = image-only gap, never guessed), the SAT-2390
devolución de crédito fiscal channel with its CSV annex spec (authoritative
from 63_), and the Criterios Tributarios interpretive layer (confirm-only,
never the rate source). Statutory rates/thresholds/deadline law are S-GT2
taxation-owned and consumed by exact FR id; ISR-work surfaces pair with
payroll/09. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_form-inventory-channels.md](01_form-inventory-channels.md) | F1 | Form registry data model + channel model (DG-only declarations, 27 paper-only, AsiseLight=0, apps = 5th surface); R46 ISR identities (1411/1431/1371/1331/1321); 18-string dated-validity ledger (R53 both-windows); SAT-1111 dual; SAT-2390 absence (R58); no-maquilla negative (GOQ-95); calendario ingestion (GOQ-14) | GT-FIN-FR-001..026 | 26 | 16 | 13 | 5 |
| [02_retenciones-web.md](02_retenciones-web.md) | F2 | RetWeb operational surfaces OF GT-TAX-FR-105/106/107: SAT-2340 15 dh vs SAT-2320 10 dh (R47 never-frozen); rate-matrix rendering of the taxation CSVs (R55 secondary-pending); ISR RetWeb (SAT-1331, 10 dh, constancia = factura date, 5 días w/o "hábiles" — R54/GOQ-99); constancia state machine; carga masiva engines; roster 8,447 + SAT-0261 tri-partite provenance | GT-FIN-FR-027..074 | 48 | 29 | 15 | 10 |
| [03_pequeno-libro-regime.md](03_pequeno-libro-regime.md) | F3 | Two-document chain as dated layers (55_ = as-of-~2013 banner GOQ-100; 61_ LET-era); R20 Q150k attribution; Q50 floor + Clientes Varios consolidation; single compras-y-ventas libro + SAT-7121 habilitación flow; form-drift ledger 2043/2047/2049→2046→2046/2241; LIVA art. 48 whole-month deadline (GOQ-103 — no fixed day invented); R56/R57 guards | GT-FIN-FR-075..102 | 28 | 20 | 12 | 6 |
| [04_let-electronic-books.md](04_let-electronic-books.md) | F4 | Book architecture per regime (PC + 3 especiales = ONE combined book → SAT-2046; General = TWO books/establecimiento, no form, resumen = insumo); feeds (FEL ventas immutable, compras by selection, FYDUCA/DUCA, vehicles ≤2 model years); layouts = images NEGATIVE-FR (GOQ-105); no LET resolution (GOQ-106); 4%/5%-10-dh tariff rule ≠ deadline (GOQ-107 RESOLVED W-GT8: art. 54 "E" D-7-2019, sunset 2025-08-09); informe art. 57 "D" + 100% gate (GOQ-108); masked numbers (GOQ-109); R48 RTN guard | GT-FIN-FR-103..130 | 28 | 25 | 14 | 6 |
| [05_devolucion-credito-fiscal.md](05_devolucion-credito-fiscal.md) | F5 | SAT-2390: claim window from IVA due date ≤4y trimestral/semestral (statutory = GT-TAX-FR-025/031..037); THE cross-validation gate (Libro CSV totals vs SAT-2237 declarations — reject on mismatch); CSV annex spec authoritative from 63_ (compras 16 cols A-P / ventas 11 cols A-K, TEXT cells, dd/MM/yyyy, NC−/ND+, >Q2,500 NIT+ID from 2023-01 GOQ-113); CARTERA states; R49 defects verbatim | GT-FIN-FR-131..164 | 34 | 11 | 14 | 6 |
| [06_criterios-interpretive.md](06_criterios-interpretive.md) | F6 | Criterios 2-2019 (dualidad — confirm-only vs the taxation matrix; GOQ-118/119 resolved kin) + 6-2018 (deducibilidad gates: IGSS-planilla ≥3/≥1, related-party 10%, aguinaldo/bono 100% caps + pacto homologado, dietas LAT art. 44); GOQ-116 clause-citation ban; GOQ-121 negative-FR (no decree-number backfill); R50 [sic] guard | GT-FIN-FR-165..185 | 21 | 10 | 11 | 7 |
| **Total** | | | **GT-FIN-FR-001..185** | **185** | **111** | **79** | **40** |

Cluster map (from `gt/.extractions/00_MASTER_INDEX.md` §A, wave W-GT4): F1→01,
F2→02, F3→03, F4→04, F5→05, F6→06 map one-to-one. FR numbering is
wave-sequential with no gaps or collisions (verified mechanically).

## Authority order (binding, from the master index)

Copied from `gt/.extractions/00_MASTER_INDEX.md` preamble (fiscal-reporting
authority order, binding all S-GT4 files):

- 48_ = dated registry data (as-of 2025-10-06 Wayback), SAT-published but not
  exhaustive. Manuals are primary for declaration MECHANICS, secondary for
  statutory parameters (rates/thresholds/deadlines they print are
  restatements — statutory instruments outrank them, verify vs W-GT2 before
  codifying).
- 55_ = as-of-~2013 digest still live at 2024 capture — every number a dated
  value, never current; 61_ = ~2018+ LET-era procedure; current-generation
  forms from 48_.
- LET record-level layouts = image-only gap (EVID-473): NEVER guessed.
- Criterios = interpretive layer only (confirm, never re-derive, the rate
  matrix); deadline CRs never sourced from a criterio's own summary.
- Form identities (corrected W-GT4, binding): ISR anual lucrativas =
  **SAT-1411**; asalariados anual = **SAT-1431**; SAT-1371 = no-residentes
  pago directo mensual; ISR retenciones = **SAT-1331**; 1321 = ISR capital
  mensual (R46 — carried on every ISR-form-naming row).

Wave-level instantiation notes: retention deadlines/form identities = the
statutory layer GT-TAX-FR-105/106/107 (S-GT2) with 02 as the operational
surface; the refund statutory channels = GT-TAX-FR-025/031..037 with 05 as
the SAT-2390 surface; rate catalogs `taxation/iva_retention_rates.csv` +
`isr_rates.csv` consumed read-only (secondary-print-pending rows never
frozen, GOQ-06); Planilla IVA-FEL mechanics = payroll-owned (GT-PAY-FR-213..222);
anulación blockers = GT-EINV-FR-210 (outcome-only).

## Open-questions rollup (§7 rows per file + master-index GOQ ids)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_form-inventory-channels.md | 5 | GOQ-92/93/94/95 + GOQ-14 (all owned) |
| 02_retenciones-web.md | 10 | GOQ-96/97/98/99 (owned; GOQ-99 mechanics half) + kin GOQ-01/06/14/94 + resolved kin GOQ-118/119/120 |
| 03_pequeno-libro-regime.md | 6 | GOQ-100/101/102/103 (owned) + kin GOQ-06/14 |
| 04_let-electronic-books.md | 6 | GOQ-104/105/106/107/108/109 (owned) + kin GOQ-14/101 |
| 05_devolucion-credito-fiscal.md | 6 | GOQ-110/111/112/113/114/115 (owned) + kin GOQ-105 |
| 06_criterios-interpretive.md | 7 | GOQ-116/117/121 (owned) + resolved kin GOQ-118/119/120 + kin GOQ-09 |
| **Total** | **40** | |

### GOQ coverage check (fiscal-reporting register GOQ-92..121 + cross-cutting GOQ-14)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.4 (GOQ-92..121) + §C
cross-cutting table (GOQ-14). Every id is **consumed** in at least one §7 OQ
row — none remain unassigned; none listed not-applicable.

| GOQ | Consumed in |
|-----|-------------|
| GOQ-14 | 01 + 02 + 03 + 04 (calendar ingestion surfaces) |
| GOQ-92 | 01 |
| GOQ-93 | 01 |
| GOQ-94 | 01 (+ 02 kin) |
| GOQ-95 | 01 |
| GOQ-96 | 02 |
| GOQ-97 | 02 |
| GOQ-98 | 02 |
| GOQ-99 | 02 (mechanics half; statutory half answered in taxation/04) |
| GOQ-100 | 03 |
| GOQ-101 | 03 (+ 04 kin) |
| GOQ-102 | 03 |
| GOQ-103 | 03 |
| GOQ-104 | 04 |
| GOQ-105 | 04 (+ 05 kin) |
| GOQ-106 | 04 |
| GOQ-107 | 04 |
| GOQ-108 | 04 |
| GOQ-109 | 04 |
| GOQ-110 | 05 |
| GOQ-111 | 05 |
| GOQ-112 | 05 |
| GOQ-113 | 05 |
| GOQ-114 | 05 |
| GOQ-115 | 05 |
| GOQ-116 | 06 |
| GOQ-117 | 06 |
| GOQ-121 | 06 |

Kin ids referenced beyond the owned set (all pre-existing register rows,
owned by other waves): GOQ-01 (54-bis text absent — 02/03), GOQ-06 (R55
secondary prints via the CSVs — 02/03), GOQ-09 (missing bonus laws — 06 via
GOQ-121), GOQ-66/67 (fuel/bancarización edges — 02, flag-only), GOQ-94
(49_/50_ as-of stamping — 02 kin), GOQ-101 (55_/61_ provenance — 04 kin),
GOQ-105 (layout images — 05 kin), GOQ-118/119/120 (S-GT2-resolved — 02/06
carried as resolved/recorded annotations, never re-opened).

**New gaps reported during synthesis (NOT register GOQs — flagged to
controller, candidates for register addition):** ISR-constancia form code
unprinted by 50_ (rides GOQ-98); D27-92 Cap. VIII/IX primary texts absent
(04's electrónico-tariff rows anchor-pending); informe periodicity tension
(monthly print vs semestral glossary hint — recorded under GOQ-108);
51_ state-list slash normalization (02 report); 63_ rule-6c ventas col-D
omission flagged-not-corrected (05).

## CSV sidecars

None in this wave — the two rate catalogs consumed read-only live in
`gt/requirements/taxation/` (`iva_retention_rates.csv`, `isr_rates.csv`).

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_form-inventory-channels.md | 17 | 13 |
| 02_retenciones-web.md | 29 | 15 |
| 03_pequeno-libro-regime.md | 20 | 12 |
| 04_let-electronic-books.md | 26 | 14 |
| 05_devolucion-credito-fiscal.md | 11 | 14 |
| 06_criterios-interpretive.md | 10 | 11 |
| **Total** | **113** | **79** |
