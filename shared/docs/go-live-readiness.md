# Go-Live Readiness — Universal Concern Catalog

**Status: DECIDED (D19 session, 2026-08-19).** The mechanics canon lives in
[regulatory-change-management.md](regulatory-change-management.md)
(**D15 anchor/as-of doctrine, D16 date-driven mechanics, D18 mid-year
ingestion, D19 cut-over mechanics**); this document is the operational
catalog a deployment walks through, plus the per-country instantiation
registers. Country waves MUST verify their register before synthesis
sign-off; no go-live with an unverified row.

The catalog is country-neutral. Country sections are illustrative for each
other, never normative across borders (same rule as D15's instantiation
register).

## 1. Bootstrap master data

| Concern | Universal rule |
|---|---|
| Legal identity & tax registrations | NIT/RTN/NIT-DUI/RUC etc. + regime classification imported/entered as company data with instrument provenance (registration resolution number/date) |
| Establishments & points of sale | D17/D14 kin: warehouses ↔ establishments, cash registers ↔ points of sale, per-country mapping |
| Authorization ranges | Dated rows (`valid_from/valid_to` + numeric range + status); emission outside range = hard block (D16 ¶3); consumed-to counters derive from sequence-init records (D19(c)) |
| Chart of accounts | Country CoA template applied; opening balances map onto it (§3) |
| Legal sequences | Initialized from imported last-legacy documents — never typed by users (D19(c)) |

## 2. Cut-over mechanics (D18 + D19)

- **Tiered ingestion** (D18(b)): T1 straddle-FY detail (`is_historical`,
  historical journals) · T2 prior-FY filings (frozen snapshots) · T3 opening
  balances · T4 carryover dated rows.
- **Posting tiers** (D19(a)): closed items GL-neutral through the migration
  account; open items real (subledger ↔ control account); trial balance
  dated at cut-over through control accounts with residual clearing.
- **Config, never hardcode** (D19(a+)): migration/clearing + control
  accounts are `res.config.settings` fields with module-data defaults
  created under stable XML IDs; extensible control-treatment set per
  company.
- **Rounding** (D19(b)): legacy amounts verbatim; Odoo matches legacy;
  residuals absorb drift.
- **Sequence initialization** (D19(c)): canceled, GL-neutral
  `is_sequence_init` records (read-only flag, set only by server
  action/special import) in LIVE journals carry last legacy numbers;
  sequences + range counters derive from them.
- **Straddle-filing checkpoint** (D19(d)): predecessor-filed (T2 snapshot
  import) vs Odoo-files-complete — explicit deployment choice.

## 3. Regulator onboarding catalog

| Concern | Universal rule |
|---|---|
| Regime enrollment | Emitter/taxpayer registration with the country authority; recorded as dated config with instrument provenance |
| Credentials & certificates | Signing certificates, API tokens, portal credentials — vault-stored (D2 kin), expiry-dated rows |
| Test/homologation pass | Regulator sandbox or homologation environment pass before production; recorded as a checklist state, artifacts retained |
| Phased mandates | Mandatory-by-class dates (taxpayer size/sector/activity) = dated rows; voluntary-early supported |
| Provider contracts | Where a certified intermediary is required (certificadores/ PSPs), contract state + auth expiry as dated rows |
| Contingency authorization | Contingence/offline emission authorization requirements recorded; kin to each country's contingencia regime |

## 4. Country instantiation registers

### SV (verified 2026-08-24 — see `sv/requirements/GO_LIVE_READINESS.md`; one blocker: A11 onboarding synthesis gap)

- Enrollment: MH DTE emitter registration (Normativa v2.0; 27_ certificate
  obtainment manual); contingency authorization per Normativa.
- Credentials: JWS cert (ruling 9: RS512/PKCS8), per-environment.
- Sequences/ranges: numeroControl per (type, establecimiento, punto de
  venta), year-reset consecutive (D14); no authorization ranges (MH
  assigns) — sequence-init still applies.
- Straddle filings: F-07/F-14 monthly; F-11 annual (F-11 v19/v20 prints
  pending acquisition).

### GT (seeded from D-GT research — verify at GT synthesis)

- Enrollment: FEL emitter via certificador (18 authorized; TotalDoc =
  GRUPO CDS S.A., auth expiry 02/12/2026); phased mandate by taxpayer
  class (DSI resolutions 01-14_ corpus).
- Credentials: FEL firma + certificador contract.
- Sequences/ranges: SAT-assigned document types; sequence-init applies.
- Test pass: certificador pilot → production.

### HN (seeded from D-H research — verify at HN synthesis)

- Enrollment: SEE (Sistema de Emisión Electrónica) per D.31-2018 (24_
  Arts. 50-58); CAI pre-authorization ranges — the canonical authorization-
  range case (hard block D16 ¶3).
- Credentials: SEE credentials + IHSS/SAR portal credentials for filings.
- Straddle filings: DMC/DJIMR/DJI monthly (D-H3 reconciliation surface).

*(Future countries append their register at synthesis time.)*

## 5. Explicitly out of scope (recorded, not forgotten)

- Parallel-run tooling & reconciliation dashboards beyond the residual
  clearing surface (D19(e)).
- Predecessor-system decommissioning & data-retention duties (retention
  matrix applies to data living in a dead system — future session).
- Rollback doctrine for failed cut-overs (future session).
