# SV — Go-live readiness assessment

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | go-live readiness (cross-topic assessment) |
| Status  | assessment (W29: catalog walk + register verification, graded statuses, gate rollup) |
| As-of   | 2026-08-24 |
| Corpus basis | 1,732 FRs |
| Registry | 126 source-file rows (numbering 01–128, next free 129) |
| COVERAGE | 92 cited-as-LB / 9 not-applicable-this-wave / 2 superseded-not-cited / 24 pending-S2+ of 127 — gate green (W28) |
| Authors | Controller + W29 Task 1 synthesis |
| Updated | 2026-08-24 (W29) |

How to read this file: statuses are per-row; a row with a limb counts as its
worst limb for gate purposes (a `VERIFIED + WATCH limb` row gates as WATCH; a
`VERIFIED (mechanics) + BLOCKER limb` row gates as BLOCKER).

Citation key: FR/LB ids cited by id, never restated — every id below exists
verbatim in the named file (grep-verified 2026-08-24). Bare numbers `01`–`06`
= `sv/requirements/e-invoicing/` file numbers; `coa/` = chart-of-accounts,
`frep/` = fiscal-reporting, `spe/` = special-regimes, `cml/` = commercial-legal
directories.

## Gate summary

- 21 assessment rows (§1–§4): **13 VERIFIED · 6 VERIFIED-with-limb ·
  2 BLOCKER rows** (recount of record, this file).
- Limbs: WATCH limbs on §2.6, §3.2, §4.2, §4.4; BLOCKER limbs on §3.1, §4.1.
- Every BLOCKER surface (rows §3.3/§3.4 plus the §3.1/§4.1 limbs) is one
  root — the single §5.1 entry (A11 synthesis gap).
- 0 standalone CONFIG-GAP rows; §5.3 carries the canonical CONFIG-GAP list
  (non-blocking by value-discipline canon).
- Worst-limb tally: 13 VERIFIED / 4 WATCH / 4 BLOCKER-rooted (one root) →
  **NOT go-live-ready until the A11 file is minted** (§6); expected green
  after the A11 wave.

## §1 Bootstrap master data

| # | Concern | SV instantiation | Status | Citations (verified to exist) | Notes |
|---|---------|------------------|--------|-------------------------------|-------|
| 1 | Legal identity & tax registrations | NIT/DUI/CAT-022 identification; NIT+NRC active contributor profile; foreign-receptor registry IDs | VERIFIED | `SV-EINV-FR-021` (01: CAT-022: 13 DUI / 36 NIT / 02 / 37 / 03 passport), `SV-EINV-FR-023` (01: CCFE NIT 9/14 + active NRC), `SV-EINV-FR-042` (01: FEXE foreign receptor), `SV-EINV-FR-009` (01: fusion NIT AT merged list) | Emitter-side NIT/NRC ride the A11 gap row (§3.1) |
| 2 | Establishments & points of sale | numeroControl carries estab/PV; warehouses ↔ establecimientos, caja ↔ punto de venta (D17/D14) | VERIFIED | `SV-EINV-FR-004` (01: `DTE-{tipoDte:2}-{estab/PV:8}-{consecutivo:15}`, sections M/B/S/P + P-prefix PV), coa/02 template config sets | D14 canon; EVID-077 all-types-all-establishments rides §3 A11 |
| 3 | Authorization ranges | SV: NONE — MH assigns; Art. 115-A correlative authorization lifted for DTEs | VERIFIED | `SV-EINV-FR-004` (01: "no AT correlative authorization — Art. 115-A is lifted"), contrast: shared/docs/go-live-readiness.md §4 HN CAI row | Sequence-init still applies (row 5) |
| 4 | Chart of accounts | sv_coa template + opening balances | VERIFIED | coa/02 (`l10n_sv_chart` template surfaces, ~L589 "account template… Odoo-native"), coa/08 `SV-COA-FR-270` (adoption_transition: transition_date + adjustment_account, ganancias acumuladas) | Opening balances = §2 posting-tier rows |
| 5 | Legal sequences | D19(c): from imported last-legacy documents, `is_sequence_init`, never user-typed | VERIFIED | `SV-EINV-FR-004` (year-reset consecutive), coa/08 L521 (`is_sequence_init` follows D19 canon) | Corpus-thin: implementation rows are canon-level (shared docs); recorded as such |

## §2 Cut-over mechanics

| # | Concern | SV instantiation | Status | Citations | Notes |
|---|---------|------------------|--------|-----------|-------|
| 1 | Tiered ingestion (D18) | T1–T4; `is_historical` | VERIFIED | coa/08 L325-328 (D18 canon: is_historical, suppress/reallow, straddle-FY), taxation/15 (is_historical IVA surfaces), spe/02+spe/07 (is_historical files) | Canon + corpus consumers |
| 2 | Posting tiers (D19a) | GL-neutral closed / real open; control accounts | VERIFIED | coa/08 L317-321 (D19 posting-tier canon cited in-file), `SV-COA-FR-270` | |
| 3 | Config, never hardcode (D19a+) | migration/clearing + control accounts = config fields | VERIFIED | coa/08 FR-270 map row (adjustment_account m2o) | |
| 4 | Rounding (D19b) | legacy verbatim; residuals absorb | VERIFIED | frep/01 F-07 verbatim SUMA arithmetic family (casilla engine) | canon-cited |
| 5 | Sequence initialization (D19c) | canceled GL-neutral init records in LIVE journals | VERIFIED | (same as §1 row 5) | |
| 6 | Straddle-filing checkpoint (D19d) | F-07/F-14 monthly; F-11 annual | VERIFIED + WATCH limb | frep/01 `SV-FREP-FR-213/214` (declaration-state gate + delegated reception), frep/00_index scope rows | F-11 v19/v20 prints pending (MH landing watch) = the WATCH limb |

## §3 Regulator onboarding

| # | Concern | SV instantiation | Status | Citations | Notes |
|---|---------|------------------|--------|-----------|-------|
| 1 | Regime enrollment | MH DTE emitter registration; acreditamiento once per environment | VERIFIED (mechanics) + BLOCKER limb | `SV-EINV-FR-138` (04: portal info.dtes.mh.gob.sv → verification → cert generation → API user), LB-008 (04: 27_ manual) | AT authorization program (groups/dates) = A11 gap (below). BLOCKER limb: the mechanics are corpus-VERIFIED but the program-level rows are unsynthesized — the row gates as BLOCKER |
| 2 | Credentials & certificates | JWS RS512/PKCS8; per-env vault; env separation | VERIFIED + WATCH limb | `SV-EINV-FR-136` (04: one ACTIVE cert per ambiente, cross-env refused), `SV-PROT-FR-021` (06: const RS512 opaque full-bytes), `SV-EINV-FR-054` (02: pruebas/producción separation), `SV-PROT-FR-013/023` (06: signing round-trip) | WATCH limb: 04 OQ-006 renewal/revocation procedure unobtained |
| 3 | Test/homologation pass | minimum tests per DTE type + event; test-env windows | **BLOCKER** | Gap: master-index A11 (8 governing EVIDs: 001/036/045/080/081/077/074/083) has NO requirements file — every e-invoicing file scopes "(A11)" out to a file never synthesized (S1 plan file list 01/02/03/04/05-cat/06 has no A11; FR-138's own citation dangles: "owned by the A11 onboarding file") | Closing condition: mint the A11 onboarding requirements file (S-wave; evidence owned; GT S-GT1 Task 5 `04_mandate-onboarding.md` = pattern) |
| 4 | Phased mandates | AT sets groups/dates; early adoption | **BLOCKER** (same root) | Gap: EVID-077 rows unsynthesized (A11) | Same closing condition as row 3 — ONE §5 inventory entry |
| 5 | Provider contracts | SV model = MH-direct; no certified intermediary | VERIFIED (negative) | `SV-EINV-FR-138` (portal-direct acquisition flow; no certificador surface anywhere in corpus) | Contrast GT (18 certificadores) |
| 6 | Contingency authorization | contingencia CAT-005 tipos 1-5; clocks; invalidación deadlines | VERIFIED | `SV-EINV-FR-103` (03: 1d/10háb/4d/3mo/2y differentiated), `SV-EINV-FR-111/112` (03: contingencia 24h/72h clocks), 03 §4 map rows (event.contingencia) | NCE contingency-eligible; CLE/DCLE/CDE excluded |

## §4 Register verification (shared-docs §4 SV rows)

Disposition rows from the shared-docs register walk; citations ride the
mirrored §1–§3 rows named in each disposition.

| Register row | Status | Disposition |
|--------------|--------|-------------|
| Enrollment | VERIFIED (mechanics) + BLOCKER limb | Verified w/ A11 caveat (mechanics VERIFIED; program rows = BLOCKER §3.3/3.4) |
| Credentials | VERIFIED + WATCH limb | Verified (JWS RS512/PKCS8; OQ-006 renewal watch) |
| Sequences/ranges | VERIFIED | Verified (no ranges — MH assigns; sequence-init applies) |
| Straddle filings | VERIFIED + WATCH limb | Verified (F-07/F-14 monthly, F-11 annual; v19/v20 prints WATCH) |

## §5 Blocking-gaps inventory

### 5.1 BLOCKER — A11 onboarding/authorization never synthesized

Surfaces: acreditamiento minimum tests (EVID-081 consola mandatory-starred;
EVID-036/045 per-event), AT authorization groups/dates + early adoption
(EVID-077), no physical/DTE coexistence + stock destruction + range reporting
(EVID-074/083), 7-step onboarding (EVID-001 carried).

Closing condition: one S-wave minting the A11 onboarding requirements file —
`sv/requirements/e-invoicing/05_onboarding.md` or the next free number
(controller decides at mint; numbering per R30(b) SV-EINV continuation) —
evidence already in bank (pattern: GT S-GT1 Task 5 `04_mandate-onboarding.md`).
The gate flips green when that file lands and the dangling pointers below
resolve.

Dangling in-corpus pointers to "(A11)" (file:line anchors, exhaustive;
grep-reproducible 2026-08-24): `e-invoicing/01:30` · `01:201` ·
`e-invoicing/02:38` · `e-invoicing/03:42` · `03:211` ·
`e-invoicing/04:34` · `04:77` · `04:189` · `e-invoicing/06:36`; plus
cross-topic pointer notes in commercial-legal (cml/01:354 · cml/04:136,
1006 · cml/05:82, 134, 213, 411, 750, 816, 823, 835 · cml/07:88, 693)
and the COVERAGE 26_ consola-manual row (A11-wave candidate) — all
resolve at mint.

### 5.2 WATCH items (each: pointer + cadence/deadline)

- F-11 v19/v20 prints (MH landing; §6 recipe of the W28 handdown).
- Cert renewal/revocation procedure (04 OQ-006; 27_/46_ gap).
- AML reglamento D.L. 426 (deadline 2026-10-17; uif WAF; 128_ corroboration
  no-lineamientos).
- SOQ-46 criteria instrument (negative at full-enumeration strength; cvpcpa +
  D.O. re-probe).
- D.O. gazette-feed stall (re-probe before any 2026-instrument hunt).

### 5.3 CONFIG-GAP items (non-blocking by value-discipline canon)

Canonical instances cited; per-file OQ registers own the long tail:

- RAEX reglamento (96_; SOQ-41 residual)
- Interés legal mercantil rate (Economía; SOQ-26)
- Ley Registro de Comercio + reglamento (SOQ-25)
- Quiebra vintage (SOQ-24)
- 108_ operative format (spe/02 OQ-10)
- FE receptor ≥3 SMM amount (FR-020 → OQ-007)
- SMM-mayor-cuantía sector (SOQ-33)
- BCR Tasa Máxima Legal (cml/08)

## §6 Gate statement

1 BLOCKER (A11 synthesis gap; single root, one closing wave) →
**NOT go-live-ready until closed**; all other rows VERIFIED / CONFIG-GAP /
WATCH. Expected post-A11: gate green for planning.

Rollup arithmetic (worst limb per row, 21 rows): 13 VERIFIED · 4 WATCH ·
4 BLOCKER-rooted (§3.3/§3.4 rows + §3.1/§4.1 limbs; all one §5.1 root) ·
0 CONFIG-GAP rows. Closing the single §5.1 entry flips every BLOCKER surface
at once.
