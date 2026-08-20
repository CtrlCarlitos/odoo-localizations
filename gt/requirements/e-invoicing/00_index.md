# GT — e-Invoicing requirements index

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft (S-GT1 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

This directory holds the S-GT1 (synthesis wave 1) e-invoicing requirements:
DTE taxonomy, XSD schema contract, Reglas v2.0 validation universe, legal
chain + mandate/onboarding, certificador/provider interface +
establishment model, anulación/contingencia, and graphic representation.
Catalog governance (frases / unidades gravables / mensajes JSON catalogs)
lives in [../catalogs/01_governance.md](../catalogs/01_governance.md) with
CSV sidecars (GT-CAT-FR-001..015). Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_document-types.md](01_document-types.md) | E1 | 26 DTE catalog codes in 11 families: legal identity, per-type rules | GT-EINV-FR-001..041 | 41 | 16 | 10 | 4 |
| [02_dte-schema.md](02_dte-schema.md) | E2 | GT_Documento-0.2.1 XSD contract, complement schemas, channel drift | GT-EINV-FR-042..070 | 29 | 27 | 12 | 6 |
| [03_validation-rules.md](03_validation-rules.md) | E3 | Reglas v2.0 validation universe: pipeline, severity, dates, NIT, frases, rates, totals | GT-EINV-FR-071..139 | 69 | 23 | 20 | 8 |
| [04_mandate-onboarding.md](04_mandate-onboarding.md) | E4 | FEL legal chain, 11 mandate resolutions, cohorts, onboarding | GT-EINV-FR-140..170 | 31 | 22 | 14 | 10 |
| [05_certificador-interface.md](05_certificador-interface.md) | E5+E7 | SAT↔certificador interface, TotalDoc boundary, establishment/dispositivo model (D-GT9) | GT-EINV-FR-171..203 | 33 | 16 | 15 | 8 |
| [06_anulacion-contingencia.md](06_anulacion-contingencia.md) | E6 | Anulación window/blockers/transport, contingencia, CF replacement, fecha-emisión states | GT-EINV-FR-204..227 | 24 | 15 | 12 | 1 |
| [07_display-representation.md](07_display-representation.md) | E8 | Representación gráfica: 9 display areas, QR, auth block, per-type print rules | GT-EINV-FR-228..243 | 16 | 10 | 8 | 4 |
| [../catalogs/01_governance.md](../catalogs/01_governance.md) | E2 (catalog half) | Three JSON catalogs as data: frases, unidades gravables, mensajes + drift record | GT-CAT-FR-001..015 | 15 | 10 | 8 | 4 |
| **Total** | | | **243 EINV + 15 CAT** | **258** | **139** | **99** | **45** |

Cluster map (from `gt/.extractions/00_MASTER_INDEX.md` §A, wave W-GT1): the
eight E-clusters E1..E8 map one-to-one onto the seven files above, except
E5 (certificador interface) + E7 (establishment model), merged into
`05_certificador-interface.md`, and E2, split between `02_dte-schema.md`
(schema half) and `../catalogs/01_governance.md` (catalog half).

## Per-file scope (first sentence of each §1 Purpose)

- **01_document-types.md** — "This file defines the functional requirements
  for the Guatemala FEL *Documento Tributario Electrónico* (DTE,
  electronic tax document) type taxonomy: the 26 catalog codes in 11
  families defined by Reglas y Validaciones v2.0 §1.2 …"
- **02_dte-schema.md** — "This file defines the functional requirements for
  the Guatemala FEL XML schema contract — the machine-readable *esquema*
  (schema) set both the Odoo client and the SaaS core serialize against:
  the GT_Documento-0.2.1 envelope …"
- **03_validation-rules.md** — "This file defines the functional
  requirements for the Guatemala FEL business-validation universe of the
  *Reglas y Validaciones* (validation rulebook) v2.0: the validation
  pipeline (XSD conformance first, then business rules) and the
  three-column severity model …"
- **04_mandate-onboarding.md** — "This file defines the functional
  requirements for the Guatemala FEL legal chain and onboarding: the
  statutory ladder that grounds the electronic invoicing obligation
  (Código Tributario arts. 98.5/98"A".2 → Ley IVA D-27-92 arts. 29-30 →
  IVA art. 29-"A" added by Decreto 4-2019 art. 6 → …)"
- **05_certificador-interface.md** — "This file defines the functional
  requirements for the Guatemala FEL certificador/provider interface and
  the establishment model: the provider architecture (SAT owns the
  standard, validates and pushes registry data; taxpayers integrate via
  *certificadores* (certifiers); TotalDoc = GRUPO CDS …)"
- **06_anulacion-contingencia.md** — "This file defines the functional
  requirements for the Guatemala FEL *anulación* (cancellation) regime,
  the *contingencia* (contingency) local emission procedure, the
  CF-replacement model, and the document-state consequences of the
  fecha-emisión (emission-date) regime …"
- **07_display-representation.md** — "This file defines the functional
  requirements for the *representación gráfica* (graphic representation —
  the printed/PDF rendering of a DTE) of the Guatemala FEL regime as
  specified by SAT's undated display guide 18_ …"
- **../catalogs/01_governance.md** — "This file defines the governance
  requirements for the three SAT FEL JSON catalogs as *data*: the CSV
  sidecars in this directory ([_INDEX.md](_INDEX.md)) as the
  machine-readable legal basis for *frases* (legal legends), *unidades
  gravables* (taxable units and factors), and …"

## Authority order (binding, from the master index)

Copied from `gt/.extractions/00_MASTER_INDEX.md` preamble (FEL authority
order, binding all S-GT1 files):

- **Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025)** governs
  ALL validation behavior over every 2018-vintage manual/caso
  (17_/18_/19_/20_); never cite "v1.7.10/Febrero 2025" as content version
  (stale cover footer).
- XSD/JSON working authority = **GitHub 961133c** (ratified-official, OQ1
  ruling 2026-08-18) **EXCEPT GT_Complemento_MediosdePago → cat.desa**
  (GitHub copy = uncompilable TurismoPasaje overwrite) until SAT answers
  GOQ-02/09; all drift recorded, never silently resolved.
- **16_ Documento Técnico v1.2 = provider-boundary document only** (product
  integrates via certificador TotalDoc, never SAT directly); do not cite it
  for current schema structure (-0.1.0 refs) or production URLs (none
  printed).
- **01_ = consolidated edition of AD 13-2018** (original 2018 wordings not
  in corpus); operative text = 01_, gazette originals = OCR-degraded
  cross-checks.
- Mandate instruments = **"Resolución de Superintendencia SAT-DSI"**
  (never "Directorio Superior"); cohorts = dated rows keyed by
  incorporation resolution; **never cite them for thresholds (D-27-92 owns
  them) or sanctions (none contained)**.

## Open-questions rollup (§7 rows per file + master-index GOQ ids)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_document-types.md | 4 | GOQ-02, GOQ-13, GOQ-16, GOQ-24, GOQ-47, GOQ-48 |
| 02_dte-schema.md | 6 | GOQ-02, GOQ-15, GOQ-17, GOQ-18, GOQ-19, GOQ-20, GOQ-21, GOQ-22, GOQ-23, GOQ-24 |
| 03_validation-rules.md | 8 | GOQ-02, GOQ-13, GOQ-20, GOQ-21, GOQ-24, GOQ-44, GOQ-45, GOQ-46, GOQ-47, GOQ-48, GOQ-49, GOQ-50 |
| 04_mandate-onboarding.md | 10 | GOQ-27, GOQ-28, GOQ-29, GOQ-30, GOQ-31, GOQ-32, GOQ-33, GOQ-34, GOQ-35, GOQ-37, GOQ-39 |
| 05_certificador-interface.md | 8 | GOQ-02, GOQ-03, GOQ-17, GOQ-39, GOQ-40, GOQ-41, GOQ-42, GOQ-51, GOQ-52 |
| 06_anulacion-contingencia.md | 1 | GOQ-38 (owned); kin: GOQ-14, GOQ-37, GOQ-51 |
| 07_display-representation.md | 4 | GOQ-02, GOQ-07, GOQ-36, GOQ-37, GOQ-38, GOQ-40, GOQ-43, GOQ-45, GOQ-48 |
| ../catalogs/01_governance.md | 4 | GOQ-02, GOQ-19, GOQ-25, GOQ-26 |
| **Total** | **45** | |

### GOQ coverage check (e-invoicing register GOQ-15..52 + cross-cutting GOQ-02/03/07/13)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.1 (GOQ-15..52) + §C
cross-cutting table (GOQ-02/03/07/13). Every id is **consumed** in at
least one §7 OQ row — none remain unassigned; none listed
not-applicable.

| GOQ | Consumed in |
|-----|-------------|
| GOQ-02 | 01, 02, 03, 05, 07, catalogs/01 |
| GOQ-03 | 05 |
| GOQ-07 | 07 |
| GOQ-13 | 01, 03 |
| GOQ-15 | 02 |
| GOQ-16 | 01 |
| GOQ-17 | 02, 05 |
| GOQ-18 | 02 |
| GOQ-19 | 02, catalogs/01 |
| GOQ-20 | 02, 03 |
| GOQ-21 | 02, 03 |
| GOQ-22 | 02 |
| GOQ-23 | 02 |
| GOQ-24 | 01, 02, 03 |
| GOQ-25 | catalogs/01 |
| GOQ-26 | catalogs/01 |
| GOQ-27 | 04 |
| GOQ-28 | 04 |
| GOQ-29 | 04 |
| GOQ-30 | 04 |
| GOQ-31 | 04 |
| GOQ-32 | 04 |
| GOQ-33 | 04 |
| GOQ-34 | 04 |
| GOQ-35 | 04 |
| GOQ-36 | 07 |
| GOQ-37 | 04, 06 (kin), 07 |
| GOQ-38 | 06 (owned), 07 |
| GOQ-39 | 04, 05 |
| GOQ-40 | 05, 07 |
| GOQ-41 | 05 |
| GOQ-42 | 05 |
| GOQ-43 | 07 |
| GOQ-44 | 03 |
| GOQ-45 | 03, 07 |
| GOQ-46 | 03 |
| GOQ-47 | 01, 03 |
| GOQ-48 | 01, 03, 07 |
| GOQ-49 | 03 |
| GOQ-50 | 03 |
| GOQ-51 | 05 (owned), 06 (kin) |
| GOQ-52 | 05 |

Not in the check set but referenced: GOQ-14 (calendario perpetuo —
fiscal-reporting wave) appears in `06` §7 as a kin reference only. The
authority-order preamble's MediosdePago watch ("until SAT answers
GOQ-02/09") resolves to GOQ-02 + EV01a OQ-9 → **GOQ-23** (owned in `02`).

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_document-types.md | 16 | 10 |
| 02_dte-schema.md | 27 | 12 |
| 03_validation-rules.md | 23 | 20 |
| 04_mandate-onboarding.md | 22 | 14 |
| 05_certificador-interface.md | 16 | 15 |
| 06_anulacion-contingencia.md | 15 | 12 |
| 07_display-representation.md | 10 | 8 |
| ../catalogs/01_governance.md | 10 | 8 |
| **Total** | **139** | **99** |
