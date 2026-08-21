# SV — Commercial & legal (merchant registration / books / statements / societies / agents / EIRL / payment instruments / sales contracts / AML) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft (S5 commercial-legal synthesis wave, in review) |
| Authors | Takumi synthesis wave 5 + controller |
| Updated | 2026-08-18 |

This directory holds the S5 (synthesis wave 5) commercial-legal
requirements, built on the Código de Comercio (**07_**, D.L. Nº 671,
8-may-1970 — article text verified against the second official copy
**73_**; SOQ-22 resolved-with-residual) for files 01-09, and on the
REBASED W12 AML regime for file 10: current law **71_** (D.L. 426,
effective 2025-10-17 — wholesale replacement of D. 498), operative
development **72_** (kept UIF Instructivo Acuerdo 380 as reformed 2023)
and **17_** (kept reglamento D.E. 2-2000, R26 addendum), with **15_**
(the 1998 law) cited as historical LB only (R28 chain). Scope: comerciante
status and matrícula registration, the legalized accounting books and the
SOQ-28 canonical retention matrix, the financial-statement FY-close cycle,
society taxonomy/lifecycle, commercial agents and authority defaults, the
empresa mercantil + EIRL vehicle, títulos valores / pagaré / cheque and
the mercantile prescription matrix, sales and intermediary contracts, and
the D.L. 426 AML compliance layer. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_merchant-registration.md](01_merchant-registration.md) | Comerciante status (CC Art. 2 presumption, Arts. 14-19 capacity/registration duties) and the matrícula de empresa/establecimiento engine (Arts. 415-426 zone): inscription, annual renewal (epoch = config-gap, SOQ-25), Art. 419 no-matrícula closure with the 30-*días hábiles* grace (calendar consumed from fiscal-reporting by id), Art. 422-e cancellation; inalienable-availability and sujeto-obligado applicability hooks | SV-CML-FR-001..017 | 17 | 22 | 8 | 1 |
| [02_accounting-books.md](02_accounting-books.md) | CC Arts. 427-457: organized accounting system + legalization + no-alteration invariants (kin of the e-invoicing §3.11 account.move rules, cited by id), inventory/valuation register, Art. 447 labor-provision anchor (payroll/COA pointer), and the SOQ-28 CANONICAL retention matrix (FR-028, longest-per-object: CC 10y books + 5y anexas + 5y post-liquidation + AML 15y txn/5y docs + CT 147 DTE row) consumed by 10_ and the D3 archive tiers | SV-CML-FR-018..030 | 13 | 13 | 10 | 4 |
| [03_financial-statements.md](03_financial-statements.md) | FY-close cycle (Arts. 433/438-447; S.A. Arts. 282-286 generalized per Art. 474): 3-month balance formation, CPA dictamen, junta general, Registro deposit, publication/dictaminación surface, valuation criteria (Art. 445 — CPA-criteria OQ) and revaluation model disambiguated from the ISR-side reserve (SV-TAX-FR-063/101 by id) | SV-CML-FR-031..041 | 11 | 12 | 11 | 3 |
| [04_society-types.md](04_society-types.md) | Society taxonomy (colectiva, en comandita simple/por acciones, SRL, S.A.) with formation, capital and governance profiles, statutory reserves (5%→1/6 limit vs 7%→1/5 floor, cooperative Art. 19-XI), colones-era cap discipline (SOQ-29) and the SAS extensible-type design (SOQ-23 open — LB-032 pointer) | SV-CML-FR-042..071 | 30 | 32 | 14 | 2 |
| [05_society-lifecycle.md](05_society-lifecycle.md) | Capital variable, fusión/transformación/escisión, liquidation (incl. the +5y retention hook feeding FR-028), nullity/irregularity, quiebra terminology only (SOQ-24 unverified supersession), foreign societies and the Art. 358-d MINEC investment-proof slot | SV-CML-FR-072..097 | 26 | 30 | 16 | 4 |
| [06_commercial-agents.md](06_commercial-agents.md) | Factors/dependientes/agentes/intermediarios: authority defaults (who binds the principal), channel protection, agency book, commission model (integrante-salarial interface to payroll SV-PAY-FR-002 by id; rates = usos del lugar config slots), Art. 399-B foreign-principal import bar; employment side owned by payroll SV-PAY-FR-101..110 | SV-CML-FR-098..119 | 22 | 24 | 12 | 4 |
| [07_empresa-mercantil-eirl.md](07_empresa-mercantil-eirl.md) | The empresa mercantil as transferable enterprise (Art. 553 ff. reckoning) and the EIRL vehicle (Arts. 600-622: one-owner limited liability, capital/estatutos, voluntary/forced liquidation, CT-solvency OQ carried from 05); derogated IP names (nombre comercial etc.) noted, never cited as authority | SV-CML-FR-120..141 | 22 | 25 | 16 | 4 |
| [08_payment-instruments.md](08_payment-instruments.md) | Títulos valores framework, pagaré, cheque (protest/endorsement/refusal ≥20%, traveller's cheques), mora interest (interés legal = SOQ-26 dated config, never hardcoded) and the Art. 995 mercantile PRESCRIPTION MATRIX (FR-160/161) that the receivables/payables aging surfaces consume by id; días-hábiles clocks from the fiscal-reporting engine | SV-CML-FR-142..164 | 23 | 27 | 15 | 4 |
| [09_sales-contracts.md](09_sales-contracts.md) | Compraventa mercantile + defect/warranty clocks, INCOTERM-analog clauses (Arts. 1030-1035 — capture stays with SV-EINV-FR-045 CAT-031 by id), venta a plazos (colones threshold SOQ-29), estimatorio, permuta, suministro, comisión, mandato mercantil; delivery-place ladder on the D14 establishment model | SV-CML-FR-165..192 | 28 | 28 | 16 | 5 |
| [10_aml-compliance.md](10_aml-compliance.md) | D.L. 426 (71_) AML layer, C10 REBASED W12: sujetos obligados registry + 15-*días hábiles* update clock, dated-regime adaptation (15_ historical row for pre-cutover facts), compliance program (UIF registration, officer, manual), KYC/CDD/EDD + beneficiary owner, ROS/STR reporting with no-tip-off, threshold monitor as DATED CONFIG under the R28 authority chain (71_ Art. 25 delegation + 72_ Art. 51 values), record retention (FR-028 rows), and sanctions in SMM units (SV-PAY-FR-011/022 by id) with the 10y/50y prescription ladder | SV-CML-FR-193..224 | 32 | 30 | 14 | 4 |
| **Total** | | SV-CML-FR-001..224 | **224** | **243** | **132** | **35** |

Numbering note: FR numbering is wave-sequential within the `SV-CML`
prefix (001-224, no gaps, no renumbering; 001-017 = C1, 018-030 = C2,
031-041 = C3, 042-071 = C4, 072-097 = C5, 098-119 = C6, 120-141 = C7,
142-164 = C8, 165-192 = C9, 193-224 = C10-rebased). No dated-data CSV
sidecars in this wave (the SMM values consumed by FR-222 live in
`../payroll/` sidecars, cited by id).

## Cross-topic consumer map

CML consumes (earlier-wave FRs cited by id, never restated):

- **e-invoicing** — `02` account-move invariants = SV-EINV-FR-159..164
  (`e-invoicing/02` §3.11, kin rows in `02`/`08`/`09`); DTE-archive row (e)
  of the FR-028 matrix = SV-EINV-FR-152..158 esp. FR-154/155/156
  (`04_signing_delivery.md` §3.7) with the FR-029 purge guard on
  SV-EINV-FR-155; `08` FR-163 statutory-proof pointers to
  SV-EINV-FR-154/155; `09` INCOTERM capture = SV-EINV-FR-045 (CAT-031,
  FR-179 + OQ-003).
- **fiscal-reporting** — días-hábiles engine SV-FREP-FR-202..204
  (`fiscal-reporting/08` §3.3): every clock in `08`, the prescription and
  deadline arithmetic in `09`, the 30-day closure countdown in `01`
  (FR-010, engine band SV-FREP-FR-195..208) and the 5/10/15-day AML
  anchors in `10` (FR-199/FR-214 via SV-FREP-FR-203).
- **payroll** — SMM dated tariffs + sector selection SV-PAY-FR-011/022
  (`10` FR-222 sanction amounts, SOQ-18 naming kin); commission-salary
  interface SV-PAY-FR-002 and contract taxonomy/termination
  SV-PAY-FR-101..110 (`06`, CC/CT boundary OQ-001).
- **taxation** — reserva-legal disambiguation SV-TAX-FR-063/101 (`03`
  FR-041, `04` FR-055; constitution-register vs 25% computation, by id).

CML produces (CML-owned ids consumed downstream):

- **SV-CML-FR-028** (SOQ-28 canonical longest-per-object retention
  matrix, `02` §3.7) — consumed by `10_aml-compliance.md` (AML rows feed
  the matrix), by the SaaS archive tiers (`shared/docs/
  saas-thin-client-architecture.md` D3 must satisfy it) and by `08`
  FR-163 (invoice/document retention_link); the e-invoicing archive (D3)
  is the compliance-bound consumer.
- **SV-CML-FR-160/161** (Art. 995 mercantile prescription matrix + pagaré
  rows, `08` §3.9) — the receivables/payables AGING surfaces consume the
  defaults table by id (also `09` clock arithmetic, with FR-160).
- **Sociedad books** (`02` FR-018..023 register set = Odoo journals +
  financial-statement surfaces; `04` statutory registers) — the
  sociedad-side statutory-book model the fiscal-reporting/COA waves
  build on; `03`'s balance-deposit objects are the e-invoicing/D3
  retention consumers of the statements layer.

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 35 OQs total — 34 open /
1 resolved (10's OQ-002 threshold-chain working ruling). Non-blocking
across the wave (config-gap discipline: slots ship empty, no invented
defaults).

Master-index SOQ mapping: SOQ-23 = `04` OQ-001 (SAS statute; CNR-existence
confirmed, identity unpinned); SOQ-24 = `05` OQ-001 (quiebra vintage; kin
`07` OQ-002 terminology-only); SOQ-25 = `01` OQ-001 (Ley de Registro de
Comercio absent); SOQ-26 = `08` OQ-001 (interés legal rate instrument);
SOQ-27 = RESOLVED-BY-RESTRUCTURE W12/R28 (`10` OQ-001 carries the
residual watch); SOQ-28 = the `02` FR-028 matrix deliverable (resolved in
synthesis; anchor-choice residual = `02` OQ-003); SOQ-29 = colones-era
remnants (`04` OQ-002, `09` OQ-001; operative USD, historical text kept);
SOQ-22 residual rides every 07_-citing file (editorial artifacts, no
as-of date — verified vs 73_).

### 01_merchant-registration.md (1)

- OQ-001 — SOQ-25 carried: Ley de Registro de Comercio + Reglamento absent (Arts. 415/420/456 delegation) — matrícula solicitud, renewal epoch/fees/sanctions are config slots with no shipped defaults; acquisition candidate ≥74. open

### 02_accounting-books.md (4)

- OQ-001 — Art. 435 watchdog-office (*del conocimiento*) notice mechanics not in corpus. open
- OQ-002 — Art. 436 in-country keeping vs cloud custody (Tier A mandatory mirror; residual folded into D3 legal review). open
- OQ-003 — Art. 451 10y books anchor (matrix uses last-entry/close; practice may differ). open
- OQ-004 — Art. 455 notarized copy vs CT 147 exact-structure conservation for DTE objects (working reading: row (e) governs electronic). open

### 03_financial-statements.md (3)

- OQ-001 — "registro de Estados Financieros" (Art. 442) vs "Registro de balances" (Arts. 456-III/459) — same register, two names (working reading). open
- OQ-002 — Consejo de Vigilancia CPA estimation criteria not in corpus (Arts. 443-444; NIC default only). open
- OQ-003 — 3-month/dictamen/junta/deposit cycle generalized from the S.A. title to sociedades + EIRL (Art. 474 working reading). open

### 04_society-types.md (2)

- OQ-001 — SOQ-23 carried: SAS statute not in corpus (CNR-portal existence confirmed; extensible-type design). open
- OQ-002 — SOQ-29/OQ-7 kin: Art. 19-II cooperative per-action cap "¢5,000.00" colones-era — operative USD, historical text kept. open

### 05_society-lifecycle.md (4)

- OQ-001 — SOQ-24 carried: quiebra block (Arts. 498-552) 1970 vintage, supersession unverified — cited terminology-only. open
- OQ-002 — Ley de Competencia absent (Art. 319 fusion checkpoint thresholds). open
- OQ-003 — Art. 620 EIRL voluntary-liquidation solvence/CT authorization verificación — CT corpus extraction silent. open
- OQ-004 — MINEC Registro de Inversión Extranjera operational interface absent (Art. 358-d proof = reference slot). open

### 06_commercial-agents.md (4)

- OQ-001 — CC/CT boundary for the same natural persons (commercial authority here; employment in payroll). open
- OQ-002 — Commission rates = usos del lugar (Arts. 389/395/404) — config slots, no shipped defaults. open
- OQ-003 — Art. 399-B foreign-principal import bar enforcement interface (oficios to customs/admin) not evidenced. open
- OQ-004 — Art. 392's 1985 authentic interpretation declared unconstitutional (sent. 15-feb-1988) — excluded as authority. open

### 07_empresa-mercantil-eirl.md (4)

- OQ-001 — Carried from `05` OQ-003: Art. 620-2 EIRL voluntary-liquidation solvency/CT verificación. open
- OQ-002 — SOQ-24 kin (05 OQ-001): quiebra terminology-only citation (Art. 619-I/II triggers). open
- OQ-003 — 07_ OQ-5 carried: nombre comercial/distintivos/patentes derogated to special IP laws outside corpus. open
- OQ-004 — Registro formulario current shape (Arts. 607/609; eCNR channels) rides the SOQ-22 residual — seven statutory fields fixed. open

### 08_payment-instruments.md (4)

- OQ-001 — SOQ-26 (carrying 07_ OQ-6): mercantile interés legal rate instrument absent — dated config, never hardcoded. open
- OQ-002 — Letra de cambio chapter skimmed in evidence (EVID-225 doubts) — re-read trigger if a cambiaria FR lands. open
- OQ-003 — Art. 995-IV "último reconocimiento" events undefined; Art. 996 excludes CC interruption/suspension. open
- OQ-004 — Modern payment-system evolution (electronic clearing, truncation, interbank rules) not evidenced. open

### 09_sales-contracts.md (5)

- OQ-001 — SOQ-29 (carrying 07_ OQ-7): Art. 1038 "un mil colones" venta-a-plazos threshold — no evidenced USD conversion rule. open
- OQ-002 — Art. 1029 D/a-D/P routing to Art. 712 documentary-collection mechanics (bank-operations zone skimmed). open
- OQ-003 — CC clause labels (csf/cif/caf, CF, LAB/FOB) vs CAT-031 Incoterms mapping not evidenced (SV-EINV-FR-045 by id). open
- OQ-004 — Comisión default rate = uso de la plaza (Art. 1079; kin of 06 OQ-002). open
- OQ-005 — Ley de Protección al Consumidor overlay outside corpus — CC merchant-layer clocks only. open

### 10_aml-compliance.md (4)

- OQ-001 — New AML Reglamento + new UIF instructivo PENDING (R28 chain; 71_ Art. 56 deadlines past) — watch uif.gob.sv + D.O.; thresholds/subjects/formats re-verify on issuance. open
- OQ-002 — Operative threshold chain post-replacement (kin of R26 / 72_ OQ-2): law-text thresholds GONE (71_ Art. 25 delegates); 72_ Art. 51 $10k-cash/$25k-other + Art. 52 institutional aggregates = dated config; supersession rides OQ-001. resolved (working ruling)
- OQ-003 — Dead-law citation mapping (71-73_ OQ-4 kin): kept instruments cite repealed-LCLDA article numbers — two value-level anchors re-anchored onto 71_. open
- OQ-004 — Post-Oct-2025 UIF/CIPLAFT inclusion/exclusion resolutions absent — FR-197 feed ships empty. open

## Ruling notes (chains affecting this wave)

- **R25 (W10):** 15_ registry title vs content — content governs (Ley
  Contra el Lavado de Dinero y de Activos, D. 498-1998, consolidated
  through reform (6) D.L. 104-2015); third title-vs-content incident,
  standing lesson reconfirmed.
- **R26 + W12 addendum:** originally ruled 15_ governed AML thresholds
  over the stale 17_ (D.E. 2-2000); the addendum records that NO
  post-D.L.-568-2013 reglamento ever issued — 17_ stayed the operative
  reglamento until the law itself was replaced.
- **R28 (W12, binding on `10`):** D.L. 426 (71_) replaces D. 498
  wholesale (Art. 61, effective 2025-10-17); 15_ = historical LB only
  (pre-cutover facts row); 17_ + 72_ KEPT in force by Art. 61; threshold
  authority chain = 71_ Art. 25 (delegation) + 72_ Art. 51 (operative
  values) — DATED CONFIG, never hardcoded; W10 evidence EVID-228..231
  historical, C10 rebased on EVID-241..250.
- **SOQ-22 (resolved-with-residual):** 07_ article text verified against
  the second official copy 73_ (both reform lists end at D.L. 641-2008);
  residual = Índice Legislativo editorial artifacts with no as-of date —
  rides every 07_ LB (files 01-09) and the 08_ payment-system OQ-004.
- **SOQ-28:** the retention-matrix reconciliation deliverable IS `02`
  FR-028 (canonical longest-per-object matrix incl. the CT 147 DTE row
  and uniform AML 15y); the SaaS archive tiers (D3) must satisfy it.
- **Shared-docs design pointers (consumed, not restated):**
  `shared/docs/saas-thin-client-architecture.md` D2 (client-held
  system-of-record DB — why files carry no `saas` layer rows) and D3
  (SaaS archive tiers — FR-028 consumer + Tier-B residency fold into
  `02` OQ-002); `shared/docs/odoo-localization-guide.md` D13
  (journal & document-type model — `02` FR-018/FR-023 register set =
  Odoo journals, several-journals shapes legal per Art. 446 III) and
  D14 (establishment & point-of-sale model — `09` FR-168 delivery-place
  ladder and `01` establecimiento records).
