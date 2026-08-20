# GT — Taxation requirements index

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft (S-GT2 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

This directory holds the S-GT2 (synthesis wave 2) taxation requirements:
IVA régimen general, IVA pequeño contribuyente, IVA retenciones (with the
rate-catalog CSV sidecar), ISR rentas del trabajo, ISR lucrativas/capital/
no-residentes (with the rates CSV sidecar), Código Tributario procedures,
and the reform-chain provenance layer. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_iva-core.md](01_iva-core.md) | TX1 | IVA general regime: hecho generador, 12% + earmarks, exenciones, base, crédito/débito, prorrateo, refund channels, vehicle fees | GT-TAX-FR-001..045 | 45 | 21 | 13 | 5 |
| [02_iva-pequeno.md](02_iva-pequeno.md) | TX2 | Pequeño contribuyente: Q150,000 threshold (R20), 5% definitivo, Q50/Q2,500 floors, retention track, exit rule | GT-TAX-FR-046..068 | 23 | 15 | 12 | 4 |
| [03_iva-retenciones.md](03_iva-retenciones.md) | TX3 | IVA retenciones: six agent classes (65/15/65/25/15/1.5), de minimis, seller mechanics, dualidad model + [iva_retention_rates.csv](iva_retention_rates.csv) | GT-TAX-FR-069..110 | 42 | 23 | 14 | 7 |
| [04_isr-trabajo.md](04_isr-trabajo.md) | TX4 | ISR employment income: art. 68-82, Q48,000/Q12,000 deductions, 5%/Q15,000+7% scale, projection/12 withholding, practice forms (R46) | GT-TAX-FR-111..146 | 36 | 12 | 13 | 5 |
| [05_isr-lucrativas-capital.md](05_isr-lucrativas-capital.md) | TX5 | ISR Utilidades 25%/quarterly, Opcional Simplificado 5/7%, capital 10%/5%, no-residentes 5/3/10/15/25, facturas especiales + [isr_rates.csv](isr_rates.csv) | GT-TAX-FR-147..193 | 47 | 23 | 14 | 4 |
| [06_ct-procedures.md](06_ct-procedures.md) | TX6 | Código Tributario: registry/NIT, prescription 4/8y, mora/omisión, art. 94 multa table, cierre, fiscalización, recursos | GT-TAX-FR-194..235 | 42 | 26 | 15 | 7 |
| [07_reform-chain-provenance.md](07_reform-chain-provenance.md) | TX7 | Provenance layer: per-instrument consolidation-cutoff register, currency qualifiers, myths-as-validation-rules, D-10-2025 delta | GT-TAX-FR-236..261 | 26 | 16 | 12 | 6 |
| **Total** | | | **GT-TAX-FR-001..261** | **261** | **136** | **93** | **38** |

Cluster map (from `gt/.extractions/00_MASTER_INDEX.md` §A, wave W-GT2): the
seven TX-clusters TX1..TX7 map one-to-one onto the seven files above.

## Per-file scope (first sentence of each §1 Purpose)

- **01_iva-core.md** — "This file defines the functional requirements for the
  Guatemala *Impuesto al Valor Agregado* (IVA, value-added tax) **régimen
  general** (general regime, statutorily "Régimen Normal o General": monthly
  débito−crédito netting)…"
- **02_iva-pequeno.md** — "This file defines the functional requirements for
  the Guatemala *Impuesto al Valor Agregado* (IVA, value-added tax)
  **Régimen de Pequeño Contribuyente** (small-taxpayer regime): the
  Q150,000.00 annual-gross qualification threshold…"
- **03_iva-retenciones.md** — "This file defines the functional requirements
  for the Guatemala **IVA retention regime** (*retenciones del Impuesto al
  Valor Agregado*, IVA withholding at source) under **Decreto 20-2006
  Capítulo I (arts. 1–14)** and…"
- **04_isr-trabajo.md** — "This file defines the functional requirements for
  the Guatemala *Impuesto sobre la Renta* (ISR, income tax) on **rentas del
  trabajo en relación de dependencia** (employment income under an employment
  relationship)…"
- **05_isr-lucrativas-capital.md** — "This file defines the functional
  requirements for the Guatemala *Impuesto Sobre la Renta* (ISR, income tax)
  under the Ley de Actualización Tributaria (LAT) Libro I outside the
  employment title: the renta/régime taxonomy and…"
- **06_ct-procedures.md** — "This file defines the functional requirements
  for the Guatemala **Código Tributario** (CT, Tax Code, Decreto Número
  6-91) procedural backbone — cluster TX6: the *fuentes* (sources of law)
  hierarchy and reserve-of-law rule for…"
- **07_reform-chain-provenance.md** — "This file defines the **provenance
  layer** of the Guatemala taxation wave as machine-actionable requirements
  (cluster TX7 — the D16 instantiation for taxation): the per-instrument
  **consolidation-cutoff register** as dated rows…"

## Authority order (binding, from the master index)

Copied from `gt/.extractions/00_MASTER_INDEX.md` preamble (taxation
authority order, binding all S-GT2 files):

- **ISR = 26_ LAT D-10-2012 consolidated through Dto. 46-2022 (27-09-2022)
  governs** (28_ AG 213-2013 develops; 47_ = self-disclaimed digest —
  26_ > 28_ > 47_, law wins every delta).
- **IVA statutory layer = 23_ D-27-92 historical base ≤ D-10-2012 ONLY —
  never cite alone**; every current-law row carries "D-27-92, reformado
  por… (≥ D-4-2019 / D-31-2024 / D-10-2025)"; post-2018 consolidated text
  still missing (GOQ-01).
- IVA reglamento = "AG 5-2013, reformado por AG 222-2019" (FEL-only for new
  registrants 1-Jul-2021; 6-month non-FEL sunset).
- IVA retenciones = **78_ D-20-2006 arts. 1-14 + 79_ AG 425-2006 Título
  II** ("resolución 2-2010" myth rejected); form numbers NEVER cite these
  (RetWeb/48_ own them).
- CT = "D-6-91, consolidated through D-37-2016" + CC annotations to
  03-12-2019 — currency qualifier mandatory; void texts never quoted as law
  (art. 120 suspension ¶ per CC 680-2013 → cite 98"A"; art. 120"A"; art.
  94.19).
- Form identities (R46, binding): ISR anual lucrativas = **SAT-1411**;
  asalariados anual = **SAT-1431**; SAT-1371 = no-residentes pago directo
  mensual; ISR retenciones = **SAT-1331**; 1321 = ISR capital mensual.

## Open-questions rollup (§7 rows per file + master-index GOQ ids)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_iva-core.md | 5 | GOQ-64 (owned), GOQ-01/13/14/50 (kin) |
| 02_iva-pequeno.md | 4 | GOQ-01/06, GOQ-102/103 (kin), GOQ-14/50 (references) |
| 03_iva-retenciones.md | 7 | GOQ-06/65/66/67 (owned), GOQ-118/119 (**118 resolved in-corpus**), GOQ-01 |
| 04_isr-trabajo.md | 5 | GOQ-58/60/61 (owned), GOQ-99 (kin — statutory half answered), GOQ-04 (kin) |
| 05_isr-lucrativas-capital.md | 4 | GOQ-58/59/60 (owned), GOQ-61 (kin) |
| 06_ct-procedures.md | 7 | GOQ-53/54/55/56/57 (owned), GOQ-120 (recorded unresolved), GOQ-49 (kin), GOQ-124 (pointer) |
| 07_reform-chain-provenance.md | 6 | GOQ-62/63/68/69 (owned; **68 resolved-negative in-corpus**), GOQ-01/13 (kin) |
| **Total** | **38** | |

### GOQ coverage check (taxation register GOQ-53..69 + cross-cutting GOQ-01/06)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.2 (GOQ-53..69) + §C
cross-cutting table (GOQ-01/06). Every id is **consumed** in at least one §7
OQ row — none remain unassigned; none listed not-applicable.

| GOQ | Consumed in |
|-----|-------------|
| GOQ-01 | 01, 02, 03, 07 |
| GOQ-06 | 02, 03 |
| GOQ-53 | 06 |
| GOQ-54 | 06 |
| GOQ-55 | 06 |
| GOQ-56 | 06 |
| GOQ-57 | 06 |
| GOQ-58 | 04, 05 |
| GOQ-59 | 05 |
| GOQ-60 | 04, 05 |
| GOQ-61 | 04, 05 |
| GOQ-62 | 07 |
| GOQ-63 | 07 |
| GOQ-64 | 01 |
| GOQ-65 | 03 |
| GOQ-66 | 03 |
| GOQ-67 | 03 |
| GOQ-68 | 07 (resolved-negative: 24_ art. 29 ¶6 ≠ AG 125-2022 text; ¶4 = AG 222-2019 rule; acquisition stands) |
| GOQ-69 | 07 |

Kin ids referenced beyond the owned set (all pre-existing register rows,
owned by other waves): GOQ-04 (04), GOQ-13 (01, 07 — S-GT1-owned), GOQ-14
(01, 02 — F-wave-owned), GOQ-49 (06 — S-GT1-owned), GOQ-50 (01, 02, 04 —
S-GT1-owned), GOQ-99 (04 — statutory half answered; F-wave owns the
mechanics half), GOQ-102/103 (02 — F-wave-owned), GOQ-118 (03 — resolved
in-corpus: AG 425-2006 art. 4 = Sistema procedure, art. 9 = dualidad; both
citations correct; R52 tension dissolved), GOQ-119 (03 — modeling call
made: configuration-driven dualidad), GOQ-120 (06 — both texts recorded,
divergence unresolved pending a post-2016 CT consolidation), GOQ-124 (06 —
archive-matrix pointer, C-wave-owned).

## CSV sidecars

| File | Rows | Content |
|------|------|---------|
| [iva_retention_rates.csv](iva_retention_rates.csv) | 16 | The IVA retention-rate matrix as dated data: 8 statutory rows (D-20-2006/AG 425-2006) + 8 secondary-print-pending rows (EV04b 5% additions, sector-público split, dualidad combos — GOQ-06 open, never frozen) |
| [isr_rates.csv](isr_rates.csv) | 17 | ISR rates as dated rows: art. 73 scale, Opcional 5%/7% + transitional 6%, Utilidades 25% + transitional 31/28, capital 10%/5%, no-residentes matrix, facturas especiales (4 transitional rows carry valid_to) |

Both sidecars are hand-built from the committed evidence files (SV taxation
CSV pattern); regeneration note and authority order live in each file's
header comment.

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_iva-core.md | 21 | 13 |
| 02_iva-pequeno.md | 15 | 12 |
| 03_iva-retenciones.md | 23 | 14 |
| 04_isr-trabajo.md | 12 | 13 |
| 05_isr-lucrativas-capital.md | 23 | 14 |
| 06_ct-procedures.md | 26 | 15 |
| 07_reform-chain-provenance.md | 16 | 12 |
| **Total** | **136** | **93** |
