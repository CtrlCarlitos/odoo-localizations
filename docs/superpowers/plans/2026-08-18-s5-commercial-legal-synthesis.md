# S5 Synthesis Implementation Plan — sv commercial-legal Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W10 + W12 commercial-legal evidence base (EVID-211..235 + EVID-241..250, master-index clusters C1–C10) into Takumi-contract requirements files under `sv/requirements/commercial-legal/`, with FR numbering `SV-CML-FR-nnn`, LB citations to CC/AML sources under the W12-rebased authority order, the SOQ-28 retention-matrix deliverable, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S5-A (C1–C10, **C10 rebased W12 on D.L. 426**) is the synthesis worklist and its SOQ-22..29 register is binding (SOQ-22/27 already resolved by W12). The commercial-legal layer is company-shaped: merchant status/registry (C1) and the accounting regime (C2) frame every company's statutory duties; annual statements deposit (C3) closes the FY loop; the society data model (C4) + lifecycle (C5) + auxiliares (C6) + empresa mercantil/EIRL (C7) model entity mechanics; payment instruments & prescription (C8) and sales/intermediary contracts (C9) govern transactional defaults; AML compliance (C10, current regime = D.L. 426 + kept Acuerdo 380 + kept D.E. 2-2000) is the risk/compliance layer. Cross-topic interfaces cite FR IDs of earlier waves by id, never re-derived (e-invoicing §3.11 correction kin; D3 archive tiers; fiscal-reporting días-hábiles engine; payroll SMM feed for AML sanctions units).

**Tech Stack:** Markdown; FR IDs `SV-CML-FR-nnn` (new prefix `CML`; wave-sequential across the topic's files, no gaps, no renumbering). No CSV sidecars this wave (no printed data tables beyond code-text values).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S5-A + commercial-legal authority-order paragraph + SOQ-22..29 + R25/R26(+addendum)/R28 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12).

**Evidence inputs (read-only for implementers):**
- `sv/.extractions/07_Codigo_Comercio.evidence.md` (EV07, EVID-211..227 — C1-C9)
- `sv/.extractions/15_Ley_Lavado_Activos.evidence.md` (EV15, EVID-228..231 — **HISTORICAL**; 15_ derogated by 71_ Art. 61)
- `sv/.extractions/17_Reglamento_Lavado_Activos.evidence.md` (EV17, EVID-232..235 — kept-mechanics citable: window mechanics, no-tip-off, red-flag catalogs)
- `sv/.extractions/71-73_AML_DL426_Instructivo380_CCverify.evidence.md` (EV71, EVID-241..250 — **C10's governing evidence**; also EVID-250 = the SOQ-22 verification note for C1-C9)
- Extraction txts when a verbatim quote is abbreviated in evidence (S3 ruling 25 applies): `07_Codigo_Comercio.pdf.txt`, `71_Ley_LavadoActivos_DL426_2025.pdf.txt`, `72_Instructivo_UIF_Acuerdo380_reform2023.pdf.txt`.

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article). No trace → OQ, not FR.
- **Authority rule (S5, binding, W12-rebased):** Código de Comercio = **07_** article text current (verified vs second official copy 73_ — both reform lists end at D.L. 641-2008; SOQ-22 resolved-with-residual: C1-C9 LBs cite 07_ and MAY co-cite 73_ for verification; the residual note rides the files' §2 preamble). AML = **71_ (D.L. 426, effective 2025-10-17)** FIRST, then **72_ (kept UIF Instructivo Acuerdo 380-as-reformed-2023)**, then **17_ (kept reglamento D.E. 2-2000 — mechanics only: rolling-30-day window, no-tip-off, red-flag catalogs)**; **15_ is HISTORICAL ONLY** (derogated wholesale by 71_ Art. 61 — R28). AML thresholds = 72_ Art. 51 values as DATED CONFIG under the R28 authority chain (71_ Art. 25 delegation + 72_ operative values + pending-reglamento watch) — never hardcoded.
- **Dead/void/superseded text (never implement, record as LB notes):** 15_'s Art. 9 law-text thresholds (superseded by the R28 chain); 17_'s colones ¢500k threshold + 3-day clock (R26); quiebra block Arts. 498-552 = classic 1970 regime, cite terminology-only with SOQ-24 OQ; nombre comercial/distintivos/patentes/edición (Arts. 570-599, 1501-1516) DEROGATED to IP laws — OQ-5 scope note recorded, no FRs; colones remnants ("moneda nacional" Art. 31; "un mil colones" Art. 1038; ¢5,000 Art. 19-II) = historical text with USD operative currency, flag each value-level use (SOQ-29).
- **Version regime (D12):** AML regime cutover 2025-10-17 (dated config: pre/post regimes for subjects list, clocks, retention); adaptation clocks (instructivos ≈2026-04-09, technical norms ≈2026-07-09, subjects' adaptation ≈2026-10-17) as dated rows; sanctions units = SMM sector-comercio (16_ feed — the "comercio" vs "Comercio y servicios" naming rides SOQ-18's config note); interés legal mercantil = Economía-published dated config (SOQ-26 — never hardcode); SAS company-type = extensible-type design + SOQ-23 OQ (existence confirmed via creaempresa; statute not in corpus); Registro-de-Comercio epochs/fees = config-gaps + SOQ-25 OQ.
- **SOQ-28 retention matrix (synthesis deliverable, lives in 02):** the longest-per-object matrix across CC (books 10y + 5y post-liquidation; facturas anexas; microfilm ≥24mo), AML (uniform ≥15y transaction records + client docs from relation end — Art. 26), and DTE conservation (CT 147 reformed — RG original format; D3 archive tiers) — one canonical table FR; consumers cite by id.
- **Cross-topic discipline (cite FR IDs, never duplicate):** e-invoicing 02 §3.11 FR-159..164 (no-alteration + immediate-rectification kin — cite as kin, never restate the account.move invariants); D3 archive tiers (shared/docs/saas-thin-client-architecture.md); fiscal-reporting/08 días-hábiles engine FR-195..208 (5/15-días-hábiles AML clocks consume it by id); payroll 02 SMM sidecar (sanctions units feed); taxation/05 (reserva legal ISR 25% separate liquidation vs CC reserva legal 5%→1/6 & 7%→1/5 — DIFFERENT institutions, a disambiguation note is mandatory); 29_ CNR F985/F-975 (third-party report format, C1 consumer note).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Commercial-legal is Odoo-native (res.company/res.partner/sale/payment/account families) — default `odoo`; external reporting interfaces (UIF goAML) = `odoo` export + external-interface assumption note.
- English prose, Spanish legal terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; never silently dropped.
- **FR numbering contract:** wave-sequential `SV-CML-FR-001..` across files in task order (T1 opens 001; each later task continues from the previous file's last used number; NO gaps, no renumbering). Tasks therefore execute STRICTLY IN ORDER (S4 precedent). The index task (T11) verifies continuity.
- Files land in `sv/requirements/commercial-legal/` following the template exactly (7 sections, none deleted).
- **Process:** execute on `main` (S2-S4/S6 precedent — no worktree). Commit style: short imperative, no emojis, commit per task.

---

### Task 1: `sv/requirements/commercial-legal/01_merchant-registration.md`

**Files:** Create `sv/requirements/commercial-legal/01_merchant-registration.md`
**Covers master clusters:** C1
**FR numbering:** opens SV-CML-FR-001

**Content requirements:**
- Comerciante status FRs (07_ Arts. 1-6): individual/social comerciante definitions; presumption by publicity/establishment (capacity gates 18y/ emancipation glossed); Art. 20 ag/professional-collective exemption from L.II except obligations I/IV — scope note for coops/professionals.
- The four professional obligations FR (Art. 411 A-D: matrícula, contabilidad conforme, inscripción documentos, conservación correspondence) as the chapter's map.
- Matrícula de empresa FR family (Arts. 412-420): registro único (commerce + establecimientos; locales/sucursales/agencias registration), permanent + ANNUAL renewal duty (epoch/fee = config-gap SOQ-25 OQ), 30-hábiles grace after closure sanction (Art. 419), constancia = sole proof of matrícula status (Art. 418), cancellation cases (Art. 422).
- Registro de Comercio architecture FR (Arts. 456-487 under CNR): the registry books (matrículas/documentos/balances; poderes/nombramientos/credenciales); matrícula-precondition-to-document-registration (Art. 469); publication rule 3× alternate D.O. + daily + deadlines from last D.O. publication (Art. 486); registration effects (third-party effect dates kin — Art. 472 zone as evidence carries).
- 29_ consumer note (CNR F985/F-975 third-party report format — CT 121 a)2 crossref) + SOQ-25 OQ row (Ley Registro de Comercio + Reglamento absent — renewal epochs/fees/sanctions = config-gaps).
- §2 preamble: SOQ-22 verification note (07_ text current, verified vs 73_).
**AC examples:** empresa with 2 sucursales registers all three matrículas; renewal inside 30-hábiles grace avoids closure sanction; a balance deposit rejected without matrícula (Art. 469 precondition).

### Task 2: `sv/requirements/commercial-legal/02_accounting-books.md`

**Files:** Create `sv/requirements/commercial-legal/02_accounting-books.md`
**Covers:** C2 (+ SOQ-28 deliverable)

**Content requirements:**
- Organized-system FRs (Arts. 435-436): accepted standards + electronic systems EXPRESSLY legal with watchdog notice; castellano + USD accounts + in-country keeping.
- Keeper thresholds FR (Art. 437): ≥$12k individuals / all sociedades (2008 USD wording — dated-but-current note).
- Legalization FR (Art. 438): Contador Público/Auditor Externo legalization + folios + opening razón.
- **No-alteration regime FR (Art. 439) + extension to ALL statutory registers (Art. 440)** — cite e-invoicing 02 §3.11 FR-159..164 as the Odoo-side kin by id (never restate the invariants); the CC text is the LB root.
- **SOQ-28 retention-matrix FR (the deliverable):** one canonical table — objects × retention: CC books 10y + 5y post-liquidation (Arts. 451/454); received/issued facturas + correspondence anexas to the books; media migration microfilm/optical only ≥24 months after emission + notarized-copy equivalence (Art. 455); <$12k single bound book + annual balance (Art. 452); AML ≥15y transaction records (from operation end) + client ID/account docs (from relation end) — 71_ Art. 26 (W12 uniform rule; the old 5y/15y split is dead); DTE/RG conservation (CT 147 reformed, e-invoicing FR family + D3 Tier A/B tiers cited by id) — longest-per-object governs; SaaS archive tiers must satisfy it (D3 crossref).
- Inventory/balance first-Diario-partida FR (Art. 446); labor-obligation provision FR (Art. 447).
**AC examples:** electronic books legal without paper duplication given watchdog notice; facturas anexas retained 10y alongside books; a rectification asiento same-day stamped (kin of §3.11); AML transaction records retained 15y from operation end even after client relation ends (longest-per-object).

### Task 3: `sv/requirements/commercial-legal/03_financial-statements.md`

**Files:** Create `sv/requirements/commercial-legal/03_financial-statements.md`
**Covers:** C3

**Content requirements:**
- FY-close statements FR family (Arts. 282-286): balance general + estado de resultados + cambios en patrimonio within 3 months IMPRORROGABLE; auditor externo handoff; dictamen 30d; junta approval → DEPOSIT in Registro de Comercio = third-party effect ("no deposit, no fe" — Art. 286/441); MH exception for ISR declarations (Art. 286 final).
- Threshold ladder FR (Art. 474): individuals ≥$12k signed propietario+contador; ≥$34k + auditor-certified; sociedades + EIRL always full set with dictamen.
- Registro de balances (Art. 459) + registro de Estados Financieros contents (Art. 442) FRs.
- Valuation-criteria FR (Arts. 443-444): Consejo de Vigilancia → NIC fallback = **the NIIF hook** (chart-of-accounts wave consumer note by id-pointer); revaluation reserva (Art. 445) + the disambiguation note vs ISR reserva legal 25% (taxation/03 by id — DIFFERENT institutions).
**AC examples:** sociedad deposits full set with dictamen by 31-Mar (3-month gate, improrrogable); individual $13k → propietario+contador signed, no auditor; $40k → auditor-certified; NIC fallback applies absent Consejo criteria.

### Task 4: `sv/requirements/commercial-legal/04_society-types.md`

**Files:** Create `sv/requirements/commercial-legal/04_society-types.md`
**Covers:** C4

**Content requirements:**
- Type taxonomy FR (Art. 18 + colectiva/comandita profiles as evidence carries): personas/capitales × fijo/variable; cooperative special rules (Art. 19, ¢5,000 remnant flag — SOQ-29).
- Formation FRs (Arts. 21-25): escritura pública + 12-field content; estatutos deposit; **personality ONLY at inscription (Art. 25)** + inscription catalogue (Art. 24/465).
- Capital FRs (Arts. 29-33): capital = pasivo-side invariant, assets ≥ capital; non-money apportation valuation rules.
- Dividend ceiling FR (Arts. 37-38: realized per-balance profit) + **reserva legal FRs: colectiva 5%→1/6 capital (Art. 91); SRL/S.A./EIRL 7%→1/5 floor (Arts. 123/295/616)** with restoration duty (Art. 39) + the disambiguation vs ISR 25% reserva (taxation by id).
- Society books FR (Art. 40 incl. capital-variable movements book).
- SRL profile FRs (Arts. 101-125): Ltda. suffix, $2,000 min capital, participaciones $1+ multiples, 5% exhibit, voto-por-dólar, 3/4 quorum, Registro de Socios 7-field book, auditor mandatory.
- S.A. profile FRs (Arts. 126-160, 289-293): acciones $1+, nominativas-until-paid, no below-par, **no self-acquisition/no own-share loans**, share-ledger 8 fields, 15-day preferential windows, auditor monthly duties.
- **SAS FR (extensible-type design):** company-type model MUST be extensible (selection + profile driven); SAS = confirmed-existing type whose statute is NOT in corpus (SOQ-23 OQ; creaempresa evidence note) — the select carries sas with statute-pending OQ, no invented mechanics.
**AC examples:** SRL formed at $2,000 with participaciones $1+ multiples; S.A. cannot acquire own shares below the exceptions; reserva legal fills to 1/5 before dividend distribution; sas selectable but mechanics carry the OQ flag.

### Task 5: `sv/requirements/commercial-legal/05_society-lifecycle.md`

**Files:** Create `sv/requirements/commercial-legal/05_society-lifecycle.md`
**Covers:** C5

**Content requirements:**
- Capital-variable FRs (Arts. 306-314): de C.V. suffix, movement book consultable, withdrawal year-end effects, minimum disclosure.
- Fusión FRs (Arts. 315-321): 90-day opposition window, publication of agreement+last balance, **Ley de Competencia inscription checkpoint**, personality until inscription.
- Transformación FRs (Arts. 322-325): successor continuity, unlimited-liability survival for pre-change ops, auditor valúo for personas→capital.
- Liquidación FRs (Arts. 326-342 + 342-A): "en liquidación" suffix, ≤2y cap, liquidator faculties incl. fiscal obligations, final balance deposited, **post-liquidation books+papers bank deposit 10y** (feeds the 02 retention matrix by id); CT-solvency-checked EIRL voluntary liquidation (Art. 620 crossref).
- Nullity/irregularity FRs (Arts. 343-357): illicit object, 90-120d regularization windows, unlimited liability, 15-day escritura-presentation duty, 4-month registro check, out-of-object reform, **single-socio 3-month collapse → empresa individual**.
- Extranjeras FRs (Arts. 358-361): registration package (statutes, domicile decision, resident representative + poder, MINEC investment-registry capital proof, balance inicial certified; sucursal domicile).
- Quiebra scope note (SOQ-24 OQ — terminology-only, no FRs) + CT solvencia crossref.
**AC examples:** fusión personality only at inscription after Competencia checkpoint; liquidation suffix propagates to company name (e-invoicing emitter-name kin by id); single-socio collapse within 3 months or empresa-individual conversion.

### Task 6: `sv/requirements/commercial-legal/06_commercial-agents.md`

**Files:** Create `sv/requirements/commercial-legal/06_commercial-agents.md`
**Covers:** C6

**Content requirements:**
- Factores FRs (Arts. 365-377): general authority from appointment, registry inscription of powers + terminación, post-revocation validity until notice/inscription.
- Dependientes FRs (Arts. 378-383): bind-the-principal defaults; in-store collection unless caja-reserve posted; **outside sale/collection = written authorization + ID or recibo/factura with firma y sello**.
- Agentes dependientes FRs (Arts. 384-391): plaza exclusivity default, operations book per principal, monthly documented-account remuneration.
- Agentes representantes/distribuidores FRs (Arts. 392-399-B): continuous designation, exclusive-zone commissions incl. principal's own deals, 3-month termination notice, **5-head indemnification scale** (verbatim table), just causes, foreign-principal import bar until compliance.
- Intermediarios FRs (Arts. 400-410): own registro + diario books, no representation.
- Payroll interface note: employment side = CT (payroll wave owns; cite by id) — this file owns the CC commercial-authority layer only.
**AC examples:** dependiente collects outside store only with written authorization + ID; distribuidor terminated without 3-month notice → indemnity scale applies; factor's revoked power still binds until inscription/notice.

### Task 7: `sv/requirements/commercial-legal/07_empresa-mercantil-eirl.md`

**Files:** Create `sv/requirements/commercial-legal/07_empresa-mercantil-eirl.md`
**Covers:** C7

**Content requirements:**
- Empresa mercantil FRs (Arts. 553-569): transferable bien mueble; statutory element package (establecimiento, clientela+fama, nombre+distintivos, arrendamientos, mobiliario/maquinaria, labor contracts, mercancías/créditos); debt succession on transmission; >6-month inactivity kills empresa character; transferor 2-year non-compete; local-change publication 15d.
- IP-derogation scope note (Arts. 570-599 → IP laws — no FRs; OQ-5 kin).
- EIRL FRs (Arts. 600-622): E. de R. L. suffix, auditor-certified pre-constitution inventory, free capital, formulario-based 7-field registration, capital down not below 1/4 paid, 30-day opposition on inventory publication, reserve/profit/statements/vigilancia incorporation by reference (04/03 files by id), forced-liquidation triggers, **CT-solvency-checked voluntary liquidation** (05 crossref).
**AC examples:** empresa transfer carries the statutory element package by default; 7-month inactivity strips empresa character; EIRL capital paid ≥3/4 at constitution via formulario.

### Task 8: `sv/requirements/commercial-legal/08_payment-instruments.md`

**Files:** Create `sv/requirements/commercial-legal/08_payment-instruments.md`
**Covers:** C8

**Content requirements:**
- Títulos valores general FRs (Arts. 623-653): castellano; words-over-figures + lower-sum; máquina protectora precedence; inhábil-day extension (días-hábiles engine consumer by id); salvo buen cobro presumption; enrichment action 1y.
- Pagaré FRs (Arts. 788-792): 6-field content, default vista/domicilio rules.
- Cheque FRs (Arts. 793-838): número+serie mandatory capture; 7-field form; raspaduras void; **presentation clocks 15d same-plaza / 1m national / 3m cross-border; agency 72h; protest ≤15d or bank note; caducidad cascade; 1y prescription; ≥20% refusal indemnity**; special-cheque taxonomy (cruzado, abono-en-cuenta, certificado, viajero 2y, limitado, circular, caja/gerencia) as payment-configuration metadata.
- Mora-interest FR (Art. 960): pactado→legal fallback; **legal rate = Economía-published dated config (SOQ-26 OQ — never hardcode)**; solidarity of codeudores/fiadores (Art. 962).
- **Prescription-matrix FR (Art. 995 verbatim):** 6m cta-cte rectification / 1y cheque-letra-regreso-vicios-transporte-corporate-nullity-admin-liability / 2y compraventa-sociedad-suministro-comisión-etc. / **5y credit contracts from LAST RECOGNITION (recognition events must stamp)**; caducidad no-suspension (Arts. 996-998) — the receivable/payable aging defaults table.
- Proof FRs (Arts. 999/1002): facturas + registros contables = statutory proof; legally-kept books win evidentiary priority (DTE archive kin by id).
**AC examples:** cheque register tracks presentation clock by plaza type; prescription clock restarts on debtor recognition (payment/partial-payment acknowledgment); factura + legally-kept books as evidence.

### Task 9: `sv/requirements/commercial-legal/09_sales-contracts.md`

**Files:** Create `sv/requirements/commercial-legal/09_sales-contracts.md`
**Covers:** C9

**Content requirements:**
- Mercantile-sale scope FR (Art. 1013 incl. farm/artisan carve-out — customer/invoice classification note) + price determination + arras-to-price (Art. 1014) + signed-pedido-binds (Art. 1015) + delivery defaults (Art. 1020).
- **Defect/warranty clocks FRs (Arts. 1019-1021):** apparent-on-examination waiver; packaged 8d; hidden 15d-from-discovery (acta notarial) + 1y-from-delivery; functioning-warranty 30d-denounce / 6m-action / 3y-default — lot-level tracking.
- Sample/gusto/perfection (Arts. 1022-1024); resolution-on-installments + identifiable-goods registry (Arts. 1025-1026); documents-over-goods D/a D/P (Arts. 1027-1029).
- **In-code INCOTERM-analog clauses FR (Arts. 1030-1035): CSF/CIF/CAF, CF, LAB/FOB with risk-pass points** — crossref e-invoicing FEX INCOTERM fields by id.
- Venta a plazos FRs (Arts. 1038-1050): reserved domain, registry, 10-day intimate resolution, 3-month prescription, colones-remnant threshold flag (SOQ-29).
- Estimatorio/consignment FR (Art. 1051: ownership-invariant — consignment-location kin); permuta (Arts. 1052-1054); suministro FRs (Arts. 1055-1065: periodic/continued, min-max, exclusivity both ways, 3-month denounce).
- Comisión FRs (Arts. 1066-1082): own-name/foreign-account; 8-day silence-acceptance; **no credit without authorization — else cash-demandable**; named-buyer reporting; retention + commission-withholding. Mandato mercantil (Arts. 1083-1097: account+name, silence-ratification).
**AC examples:** lot warranty clock 8d packaged / hidden 15d+1y; FOB risk passes on board; comisión credit sale without authorization = principal may demand cash; consignment stock not seizable by consignatario's creditors.

### Task 10: `sv/requirements/commercial-legal/10_aml-compliance.md`

**Files:** Create `sv/requirements/commercial-legal/10_aml-compliance.md`
**Covers:** C10 (REBASED — current regime = D.L. 426 + kept Acuerdo 380 + kept D.E. 2-2000)

**Content requirements:**
- §2 authority preamble: the R28 chain + regime cutover 2025-10-17 (dated config; pre/post regimes) + 15_ historical note.
- **Sujeto-obligado classification FRs (71_ Art. 7):** 10 named categories incl. activity-triggered professionals/real-estate/metals/digital-asset providers — an ordinary company is NOT per-se subject; activity-trigger config; dynamic inclusion/exclusion via UIF→CIPLAFT (Art. 8) as a watch-feed; supervisor routing table (Arts. 12-13).
- Compliance-program FRs (Art. 9 + 72_ Arts. 5-8): registration before supervisor + UIF (universal, 72_ Art. 3) with data currency; annual work plans; risk-based approach; annual training; internal-unusual-report pipeline.
- DD FRs (71_ Arts. 15-19 + 72_ Arts. 10-21): DD ladder simplified/standard/enhanced; PEP tier; **low-value accounts DD only >US$1,000 funds**; nominative-only; beneficiario final to the natural person; KYC-refusal → abstention.
- Officer architecture FRs: Oficialía de cumplimiento + **Comité de Prevención ≥3 members incl. one top-governance member + the officer (71_ Art. 23)**; APNFD Encargado regime (72_ Arts. 71-80: resident, UIF-registered, anti-retaliation); 15-días-hábiles designation/change notice; 17_ liaison-mechanics co-cite.
- **Reporting FRs:** ROS (71_ Art. 24: 15 días hábiles analysis, ONE same-length extension, then **24h report clock**; amount-irrelevant; intelligence-only/confidential); regulated-ops (71_ Art. 25 delegation + **72_ Art. 51 operative values: cash >$10,000 / other-media >$25,000, single + monthly-cumulative + mixed-payment decomposition; 5 días hábiles clocks** consuming the fiscal-reporting días-hábiles engine by id); institutions' monthly aggregates $1,000 wires / $200 remesas (72_ Art. 52 — institution-tier config); APNFD GAFI triggers ($3,000 casino / $10,000 metals-cash / $10,000 lawyer-office — 72_ Art. 77); 17_ rolling-30-day window mechanics co-cite + red-flag catalogs as configurable detection (case-creation, never auto-report); goAML/UIF formats = external-interface assumption.
- Retention FR (71_ Art. 26 uniform ≥15y) — feeds the 02 matrix by id (never restate).
- Border-declaration content note ($15,000 — informational; Aduanas/DGA interface kin).
- Sanctions FRs (71_ Arts. 29-39): SMM sector-comercio-indexed multa config (50-500/501-1000; persons ≤200/201-400; officers ≤100/101-200 + suspension/cancellation + inhabilitación 5y/10y) consuming payroll 02 SMM by id; 10y prescription with concealment-anchor; no-tip-off/confidentiality law-level guard (Art. 28).
- Adaptation-window FR (71_ Arts. 56/58 dated rows) + pending-reglamento watch OQ (R28 chain; EV71 OQ-1).
**AC examples:** company NOT in any Art. 7 category → AML profile inactive; single $9,000 cash + $9,500 same month same client → monthly-cumulative report due 5 días hábiles after month end; ROS analysis closed day 10 → transmit within 24h; multa at 100 SMM computed from the dated SMM row.

### Task 11: index + coverage + registry flips

**Files:**
- Create: `sv/requirements/commercial-legal/00_index.md`
- Modify: `sv/requirements/COVERAGE.md` (rows 07_/15_/17_/71_/72_/73_ → cited-as-LB/pending flips + rollup counts)
- Modify: `sv/README.md` (topic status → In review (draft, S5))
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (coverage-totals note: S5 delivered)

**Content requirements:**
- Index: file table (per-file FR ranges), totals (FRs/LBs/ACs/OQs open-resolved), topic-prefix note (SV-CML), cross-topic consumer map (which earlier-wave FRs consume CML ids and vice versa), OQ rollup.
- COVERAGE: 07_ cited-as-LB (C1-C9 files), 15_ stays pending-S2+ with historical note OR flips to a historical-cited row style used for 03_/10_ (cite-as-historical-LB; follow the 03_ row pattern), 17_ cited-as-LB (10 co-cites), 71_/72_ cited-as-LB (10), 73_ cited-as-LB (verification co-cites in 01-09 §2 preambles) — rollup recount (expect total 72, cited-as-LB 46→~52).
- Numbering-continuity verification: `grep -o "SV-CML-FR-[0-9]*" sv/requirements/commercial-legal/*.md | sort -u` → contiguous 001..N with no gaps; per-file LB-citation presence: every FR block cites ≥1 LB.
- Commit + push.

## Execution protocol

Per-task: fresh implementer subagent (reads this plan's Global Constraints + its task + the evidence files fully) → controller review → reviewer subagent (verifies FRs against the master index + evidence; numbering; LB citations; layer column; cross-refs by id) → fix round if findings → commit. Final whole-wave review subagent → ONE fix wave → push. Rulings discovered in-wave are recorded in the task's fix commit and summarized to the controller for the HANDOVER update (copy before workspace deletion). Tasks 1-10 STRICTLY sequential (numbering chain); Task 11 last.
