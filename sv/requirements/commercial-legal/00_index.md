# SV — Commercial & legal (merchant registration / books / statements / societies / agents / EIRL / payment instruments / sales contracts / AML) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft (S5 commercial-legal synthesis wave + W23 fold-in, in review) |
| Authors | Takumi synthesis wave 5 + controller + W23 fold-in |
| Updated | 2026-08-23 |

This directory holds the S5 (synthesis wave 5) commercial-legal
requirements, built on the Código de Comercio (**07_**, D.L. Nº 671,
8-may-1970 — article text verified against the second official copy
**73_**; ~~SOQ-22 resolved-with-residual~~ **SOQ-22 FALSIFIED W22:
the post-2008 CC reform set 109_-114_ is owned and rides as the
operative LB over the 07_ base print (STALE-PRINT RULING); the
falsification was swept W23 — re-anchors landed in 04/05/08, files
01/02/03/06/07/09 grep-verified no-overlap; SOQ-23 resolved — the SAS
statute = 111_ D.L. 905-2023**) for files 01-09, and on the
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
| [04_society-types.md](04_society-types.md) | Society taxonomy (colectiva, en comandita simple/por acciones, SRL, S.A., SAS) with formation, capital and governance profiles, statutory reserves (5%→1/6 limit vs 7%→1/5 floor, cooperative Art. 19-XI), colones-era cap discipline (SOQ-29) and the SAS profile per 111_ Capítulo VIII-Bis (SOQ-23 RESOLVED W23: formulario constitution without escritura pública, "S.A.S." suffix, capital from US$1 fully subscribed, free reserva legal, ≤180-day dividend payout, $12,000-activo accounting-mode threshold, microempresario auditor gate, gratuidad window → 31-dic-2026) + 109_ acciones re-anchors (nominative-absolute rule; CT-124 information-duty interface) | SV-CML-FR-042..071 + 225..242 | 48 | 39 | 19 | 2 |
| [05_society-lifecycle.md](05_society-lifecycle.md) | Capital variable, fusión/transformación/escisión, liquidation (incl. the +5y retention hook feeding FR-028), nullity/irregularity, quiebra terminology only (SOQ-24 unverified supersession), foreign societies and the Art. 358-d MINEC investment-proof slot; W23: fusión transnacional (111_ Arts. 4-8, FR-243..244) + Art. 338 escheat → Fondo General del Estado + Art. 358 foreign-society domicilio-fixing with personality continuity (FR-245) | SV-CML-FR-072..097 + 243..245 | 29 | 33 | 20 | 4 |
| [06_commercial-agents.md](06_commercial-agents.md) | Factors/dependientes/agentes/intermediarios: authority defaults (who binds the principal), channel protection, agency book, commission model (integrante-salarial interface to payroll SV-PAY-FR-002 by id; rates = usos del lugar config slots), Art. 399-B foreign-principal import bar; employment side owned by payroll SV-PAY-FR-101..110 | SV-CML-FR-098..119 | 22 | 24 | 12 | 4 |
| [07_empresa-mercantil-eirl.md](07_empresa-mercantil-eirl.md) | The empresa mercantil as transferable enterprise (Art. 553 ff. reckoning) and the EIRL vehicle (Arts. 600-622: one-owner limited liability, capital/estatutos, voluntary/forced liquidation, CT-solvency OQ carried from 05); derogated IP names (nombre comercial etc.) noted, never cited as authority | SV-CML-FR-120..141 | 22 | 25 | 16 | 4 |
| [08_payment-instruments.md](08_payment-instruments.md) | Títulos valores framework, pagaré, cheque (protest/endorsement/refusal ≥20%, traveller's cheques), mora interest (interés legal = SOQ-26 dated config, never hardcoded) and the Art. 995 mercantile PRESCRIPTION MATRIX (FR-160/161) that the receivables/payables aging surfaces consume by id; días-hábiles clocks from the fiscal-reporting engine; W23: 110_ Art. 960/960-A usura nullity + 112_ cheque-truncation (Arts. 838-A..E) AWARENESS LBs — no FR mechanics, CC clocks untouched | SV-CML-FR-142..164 | 23 | 29 | 15 | 4 |
| [09_sales-contracts.md](09_sales-contracts.md) | Compraventa mercantile + defect/warranty clocks, INCOTERM-analog clauses (Arts. 1030-1035 — capture stays with SV-EINV-FR-045 CAT-031 by id), venta a plazos (colones threshold SOQ-29), estimatorio, permuta, suministro, comisión, mandato mercantil; delivery-place ladder on the D14 establishment model | SV-CML-FR-165..192 | 28 | 28 | 16 | 5 |
| [10_aml-compliance.md](10_aml-compliance.md) | D.L. 426 (71_) AML layer, C10 REBASED W12: sujetos obligados registry + 15-*días hábiles* update clock, dated-regime adaptation (15_ historical row for pre-cutover facts), compliance program (UIF registration, officer, manual), KYC/CDD/EDD + beneficiary owner, ROS/STR reporting with no-tip-off, threshold monitor as DATED CONFIG under the R28 authority chain (71_ Art. 25 delegation + 72_ Art. 51 values), record retention (FR-028 rows), and sanctions in SMM units (SV-PAY-FR-011/022 by id) with the 10y/50y prescription ladder | SV-CML-FR-193..224 | 32 | 30 | 14 | 4 |
| **Total** | | SV-CML-FR-001..245 | **245** | **255** | **141** | **35** |

Numbering note: FR numbering is wave-sequential within the `SV-CML`
prefix (001-245, no gaps, no renumbering; 001-017 = C1, 018-030 = C2,
031-041 = C3, 042-071 = C4, 072-097 = C5, 098-119 = C6, 120-141 = C7,
142-164 = C8, 165-192 = C9, 193-224 = C10-rebased). No dated-data CSV
sidecars in this wave (the SMM values consumed by FR-222 live in
`../payroll/` sidecars, cited by id). W23 tails (2026-08-23): FR-225..242
appended in `04` (SAS profile + 109_ acciones re-anchors), FR-243..245 in
`05` (fusión transnacional + 338-escheat/358-domicilio) — no renumbering;
consumers cite by FR id.

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
- **SV-CML-FR-242** (CT Art. 124 shareholder/dividend information-duty
  INTERFACE, `04` §3.8 — 109_ Art. 3 final inciso riding the re-anchored
  Art. 155 registro de acciones nominativas) — the taxation/05
  distributions zone (`62_` F-915 / Art. 74-C duty kin) consumes the
  feed interface by id; cml owns the record side, taxation the reporting
  duty.
- **Sociedad books** (`02` FR-018..023 register set = Odoo journals +
  financial-statement surfaces; `04` statutory registers) — the
  sociedad-side statutory-book model the fiscal-reporting/COA waves
  build on; `03`'s balance-deposit objects are the e-invoicing/D3
  retention consumers of the statements layer.

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 35 OQs total — 33 open /
2 resolved (04's OQ-001 SAS fold-in W23; 10's OQ-002 threshold-chain
working ruling). Non-blocking across the wave (config-gap discipline:
slots ship empty, no invented defaults).

Master-index SOQ mapping: SOQ-23 = `04` OQ-001 (SAS statute; **RESOLVED
W23 — D.L. 905-2023 CC reform = 111_ owned as statute + the fold-in
executed: FR-044 flip + FR-225..240 profile + LB-032 retirement**);
SOQ-24 = `05` OQ-001 (quiebra vintage; kin
`07` OQ-002 terminology-only); SOQ-25 = `01` OQ-001 (Ley de Registro de
Comercio absent); SOQ-26 = `08` OQ-001 (interés legal rate instrument);
SOQ-27 = RESOLVED-BY-RESTRUCTURE W12/R28 (`10` OQ-001 carries the
residual watch); SOQ-28 = the `02` FR-028 matrix deliverable (resolved in
synthesis; anchor-choice residual = `02` OQ-003); SOQ-29 = colones-era
remnants (`04` OQ-002, `09` OQ-001; operative USD, historical text kept);
SOQ-22 residual = the census negative watch only (the W12 "no post-2008
CC reform" verdict was falsified W22 and the falsification swept W23 —
see ruling notes).

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

- OQ-001 — SOQ-23 carried: SAS statute not in corpus (CNR-portal existence confirmed; extensible-type design). **RESOLVED W23 (2026-08-23): statute owned as 111_ (D.L. 905-2023 CC reform) + fold-in executed — FR-044 flip, FR-225..240 profile (§3.8), LB-033..038; LB-032 retired; residual CNR-formulario shape watch carried in the LB-038 gloss, not an OQ.** resolved (W23)
- OQ-002 — SOQ-29/OQ-7 kin: Art. 19-II cooperative per-action cap "¢5,000.00" colones-era — operative USD, historical text kept. open

### 05_society-lifecycle.md (4)

- OQ-001 — SOQ-24 carried: quiebra block (Arts. 498-552) 1970 vintage, supersession unverified — cited terminology-only. open
- OQ-002 — Ley de Competencia absent (Art. 319 fusion checkpoint thresholds). reshaped-open W23: the 111_-replaced Art. 319 moved the checkpoint to notary/formulario-suscriptor comprobar-or-declarar before the Registrador (FR-079 ships the two states, values = config-gaps); the law itself stays an acquisition candidate. open
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
- OQ-004 — Modern payment-system evolution (electronic clearing, truncation, interbank rules) not evidenced. narrowed-open W23: cheque truncation NOW evidenced (112_ Arts. 838-A..E awareness LB-029, no FR mechanics); residual = the BCR Consejo-Directivo compensation norms + interbank rules (acquisition candidates). open

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
- **SOQ-22 (~~resolved-with-residual~~ FALSIFIED W22 — falsification SWEPT
  W23):** the W12 verdict ("both official copies end at D.L. 641-2008 →
  no post-2008 CC reform") was falsified by the W22 asamblea census: the
  post-2008 reform set 109_-114_ is owned, and 07_/73_ are STALE for the
  reformed articles. W23 sweep (2026-08-23): the C1-C9 verification notes
  flipped corpus-wide (STALE-PRINT RULING pattern — reform instrument =
  operative LB, 07_ co-cited as base print); re-anchors landed per file —
  `04`: Arts. 17/18/134/155 (FR-042/044/066/068 amends + FR-225..242);
  `05`: Arts. 315-319/337/338/358 (FR-077/079/086/097 amends +
  FR-243..245); `08`: Arts. 960/960-A + 838-A..E (usura + truncation
  awareness LBs); files 01/02/03/06/07/09 grep-verified no-overlap with
  the reformed article set. Residual = the census negative watch only
  (2009-2019 enumeration gaps; SOQ-22 register row in the master index).
- **W23 routing corrections (plan Global Constraints over the W22 EV-409
  OQ-1 gloss, pre-flight ruling R-1):** fusión transnacional + Art. 358
  domicilio-fixing + Art. 338 escheat fold into `05` — NOT into `02`/`03`
  (fusión) or `08` (358/338) as the W22 evidence gloss routed; evidence =
  corpus LB ownership (LB-005..008/018/028 own Arts. 315-319/337-338/358,
  all in `05`). The EV file's OQ-1 row rides untouched as historical; the
  correction record lives in HANDOVER §5 (W17 ruling (a) kin).
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
