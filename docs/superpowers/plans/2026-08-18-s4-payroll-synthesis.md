# S4 Synthesis Implementation Plan — sv payroll Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W9 payroll evidence base (EVID-191..210, master-index clusters P1–P10) into Takumi-contract requirements files under `sv/requirements/payroll/`, with FR numbering `SV-PAY-FR-nnn`, LB citations to CT/ISSS/SIP/SMM sources, dated-data sidecars (SMM tariffs, SS caps), layer split, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S4-A (P1–P10) is the synthesis worklist and its SOQ-15..21 register is binding. The payroll engine is layered: the salary model (salario vs salario básico, P1) feeds every employer money obligation; SMM (P2) and SS rates/caps (P6) are dated configuration data; work-time surcharges (P3), vacations/aguinaldo (P4/P5), and termination benefits (P8) compute on salario básico; the SS declaration/remittance layer (P7) posts worker+employer shares on the first-10-días-hábiles calendar; P9 wires the payroll↔ISR/reporting interfaces strictly BY FR-ID reference to the S2/S3 files. P10 (Quincena-25) is BLOCKED on the D.L. 499 acquisition — pointer FRs only.

**Tech Stack:** Markdown; FR IDs `SV-PAY-FR-nnn` (new prefix `PAY`; wave-sequential, no gaps, no renumbering); CSV sidecars next to their owning files.

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S4-A + SOQ-15..21 + R23/R24 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12).

**Evidence inputs (read-only for implementers):**
- `sv/.extractions/16_Salarios_Minimos_2025.evidence.md` (EV16, EVID-191..192)
- `sv/.extractions/08_Ley_ISSS.evidence.md` (EV08, EVID-193..196)
- `sv/.extractions/09_Ley_Sistema_Pensiones.evidence.md` (EV09, EVID-197..200)
- `sv/.extractions/11_Codigo_Trabajo.evidence.md` (EV11, EVID-201..209)
- `sv/.extractions/65_F11_v18_form_visual.evidence.md` (EV65, EVID-210)
- Extraction txts when a verbatim table/quote is abbreviated in evidence (S3 ruling 25 applies): `16_Salarios_Minimos_2025.pdf.txt` (incl. the PSM-4 recovery section), `08_…pdf.txt`, `09_…pdf.txt`, `11_…pdf.txt`, `65_…pdf.txt`.

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article/form zone). No trace → OQ, not FR.
- **Authority rule (S4, binding):** pensions = 09_ **D.L. 614 effective 2022-12-29** (R24 — SAP-era lore such as 6.25%/6.75% splits is DEAD for current periods; cite only Art. 16's 16% = 7.25% trabajador + 8.75% empleador); ISSS law-level rates = 08_ Art. 29 (7.5%/3%; Art. 99 public 6.68%/2.67%); pensioner-health = **7.80%** (R23; 08_'s 6% is historical); labor = 11_ CT (Índice Legislativo edition); SMM = 16_ Decreto 11-2025 (effective 2025-06-01, repealed D.E. 9/10-2021).
- **Values whose instruments are absent from the corpus enter ONLY as dated data with an OQ:** ISSS base cap / exclusion threshold (Reglamento absent — SOQ-15), AFP IBC ceiling (SOQ-16; F-14 v16 print Oct-2025 = the value source: AFP $472.93, ISSS $30.00), institutos previsionales rates INPEP 7.5% / IPSFA 9.5% / CEFAFA 5% / Bienestar Magisterial 5.58% / ISSS-IVM 7.5% (SOQ-17). Never derive a cap from arithmetic inference.
- **Dead/void text (never implement, record as LB notes):** CT **Art. 311 tenure gate is VOID** (sent. 105-2014 — maternity benefit has NO tenure requirement); colon-era remnants (CT Art. 313 ¢250 floor; CT Art. 142 ¢30 cap — day counts govern); 65_ F-11 form-label stale cites ("Ley SAP Art. 22" → live rule = D.L. 614 Art. 138; "Dec. 762/2015" pago-mínimo → R21 dead); F-11 pago-mínimo casillas 630-648 printed-but-dead.
- **Version regime (D12):** SMM rows dated (valid_from 2025-06-01; prior 2021 vintages absent — OQ not invention); SS caps dated (F-14 print Oct-2025 cadence; SOQ-11); SIP rates from 2022-12-29 (pre-2023 vintages absent); asueto = dual layer (CT Art. 190 static base + calendar/decrees as dated overlay — SOQ-19 design); F-11 deduction rows = Feb-2025 form vintage.
- **Cross-topic discipline (cite FR IDs, never duplicate):** ISR retention computation = `SV-TAX-FR-102..131` (payroll supplies base inputs, never re-derives); aguinaldo ISR exento/gravado split + vintages = taxation/04 owns (R22/SOQ-05); F-14 annex column model + validations = `fiscal-reporting/06` owns (payroll = the VALUE feed per SOQ-11); F-910/F-915 builders = `fiscal-reporting/07`; días-hábiles engine = `fiscal-reporting/08` FR IDs (10-primeros-días-hábiles consumers reference it); FE receptor ≥3×SMM threshold = e-invoicing 01 OQ-007 config feed; voluntary-savings deduction ↔ Ley ISR Art. 33 kin (P9 states the payroll side; taxation reads it).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Payroll is Odoo-native (hr/hr_payroll module family) — default `odoo`; no SaaS rows without an ARCH/D-citation justification.
- English prose, Spanish legal terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; never silently dropped.
- SOQ handling this wave: SOQ-15/16/17 (instrument-absent caps/reglamentos) as OQ rows with the dated-data working assumption; SOQ-18 (SMM sector selection) as a config FR + OQ (pinned row: aguinaldo floor = comercio y servicios); SOQ-19 dual-layer asueto design FR + OQ; SOQ-20 CSV fidelity note ([sic] transcription, D.E. 10-2025 precedent); SOQ-21 CT-vintage LB note.
- Files land in `sv/requirements/payroll/` following the template exactly (7 sections, none deleted).

---

### Task 1: `sv/requirements/payroll/01_salary-model.md`

**Files:** Create `sv/requirements/payroll/01_salary-model.md`
**Covers master clusters:** P1
**FR numbering:** SV-PAY-FR-001..0NN (opens the prefix)
**Content requirements:**
- Salario definition FR (CT Art. 119): money retribution; integrantes (habitual bonuses/sobresueldos, overtime pay, rest/asueto-day pay, profit participation); exclusions (occasional gratuities, representation/transport/tool reimbursements, CT prestaciones sociales).
- Salario básico FR family (CT Arts. 140-143): the universal base for employer money obligations; the SEVEN derivation rules of Art. 142 A/B verbatim-glossed (hourly×jornada; period-total÷period-days; mixed 6-day average; unidad-de-obra 6-day; destajo ÷ days-used; a domicilio; commission/other = last-6-months ordinary salaries ÷ días laborables) + the weekly-excess hourly-base rule (Art. 142 final inciso) + Art. 143 complete-the-week day.
- Equal-pay FR (Art. 123) + salary-credit priority FR (Art. 121; 08_ Art. 36 first-class ISSS; 09_ Art. 25 privileged cotizaciones) as metadata/notes.
- Earning-category model (Data Model): categories = salario-integrante / non-salario (reimbursement) / prestación; flags feeding IBC (09_ Art. 14), ISR base (53_ literal d), and F-14 columns (devengado vs bonificaciones vs aguinaldo split) — the mapping matrix FR (one canonical table; P9 consumers reference it).
- The colon-era remnant LB note (Art. 142 ¢30 cap — day counts govern).
**AC examples:** commission earner's básico = 6-month sum ÷ días laborables; overtime hour rate derivation; category→IBS/ISR/F-14 column classification.

### Task 2: `sv/requirements/payroll/02_minimum-wage.md`

**Files:** Create `sv/requirements/payroll/02_minimum-wage.md` + CSV sidecar `smm_2025.csv`
**Covers:** P2
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- SMM chassis FRs (CT Arts. 144-148): time-based SMM refers to the 8-hour day; jornada 5-8h → full SMM; <5h proportional unless completing the week; piece-rate floor per jornada guaranteed; SMM substitutes inferior stipulations de pleno derecho (never reduces better acquired rights); triennial review (Art. 159) → dated-data cadence note.
- Dated table FR + CSV (16_ Decreto 11-2025, effective 2025-06-01, verbatim EXACT-AS-PRINTED incl. three-decimal daily/hourly values with [sic] flags — SOQ-20): 4 time-based sectors (Agrícola $305.23/$10.035/$1.254; Industria $408.80/$13.440/$1.680; Comercio y servicios $408.80/$13.440/$1.680; Maquila $402.32/$13.227/$1.653) + piece rates (caña $5.018/t, $2.007/arroba; café $0.080/lb) + Art. 6 descanso prestación table (tarea $1.673; tonelada $0.836; arroba café $0.335); monthly pays regardless of month length (16_ inciso).
- Piece-rate FRs (16_ Arts. 3/6 + CT Art. 90 inc. 3º anchor): fraction proportionality; rendimiento caps (2 t/jornada; tarea geometry 6-surcos×14-brazadas resiembras / 6×10 plantillas); additional-cut remuneration; descanso prestación accrual.
- Benefits-base FR (16_ Art. 7): CT benefits (asueto/vacaciones/aguinaldo/indemnización) base on max(sector daily SMM, actual salary).
- Home-worker routing (16_ Art. 4); SMM-indexed anchors interface FR: aguinaldo floor = 2×"comercio y servicios" (pinned, $817.60 with the 2025-06-01 row); FE-threshold + 25-SMM sectors UNPINNED → config FR + OQ (SOQ-18).
- Prior-vintage absence OQ (2021 pair not in corpus — rows only needed for pre-2025-06 recomputation).
**AC examples:** wage-floor validation flip on SMM dated row; piece-rate day with 1.5t output; aguinaldo floor value from the CSV row.

### Task 3: `sv/requirements/payroll/03_working-time-surcharges.md`

**Files:** Create `sv/requirements/payroll/03_working-time-surcharges.md`
**Covers:** P3
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- Jornada model (CT Arts. 161-167): diurno 8/44, nocturno 7/39; >4h-nocturna classification; peligrosas 7/39-6/36 (+MTP authorization exception); effective-time definition; ≥8h inter-jornada rest.
- Surcharges: nocturnal +25% (Art. 168); overtime +100% of salario básico/hour (Art. 169) with the weekly-excess base (Art. 142 final) and fuerza-mayor plain-básico exception; permanent-extra pacts (Art. 170: 24h enterprises; 6th-day-recovery 4h + Director approval).
- Séptimo día FRs (Arts. 171-176): accrual per complete week (just-cause absence preserves; unjustified incomplete week loses); no-horario 6-day rule (Art. 172); presumed-included decomposition for period salaries (Art. 174) — explicit invariant: weekly/quincenal/monthly salary DECOMPOSES into días laborados + séptimos for proration, never double-pays; rest-day work = básico + ≥50% + compensatorio same/next week counted as effective work (Arts. 175-176); Sunday-default + exceptions (Art. 173).
- Asueto FRs (Arts. 190-195): the static legal set (with the San Salvador 3&5-Aug + local-festivity rows); pay = salario básico presumed included in period salaries (191); asueto work = ordinario +100% (2×) with overtime-on-extraordinary base (192); essential-services stay-open sectors (193); coincidence-with-descanso no-double-pay + compensatorio (194); exclusions a domicilio/commission/destajo (195).
- Dual-layer calendar FR (SOQ-19): CT Art. 190 base + dated overlay from the published calendar (30_ cross-ref to fiscal-reporting/08's engine by FR id); the extras (2-Jan, Día del Padre, patronales pattern, fin-de-año) are decree-driven dated data, not CT rows.
**AC examples:** mixed jornada classification; overtime rate on commission earner; séptimo proration on a mid-week hire; asueto-worked 2× pay + no-double-pay on coincidence.

### Task 4: `sv/requirements/payroll/04_statutory-benefits.md`

**Files:** Create `sv/requirements/payroll/04_statutory-benefits.md`
**Covers:** P4 + P5
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- Vacaciones FRs (CT Arts. 177-189): 15 days + 30% surcharge after 1 year continuous; 200-worked-days gate (suspension days don't count but don't break continuity — Art. 181); anniversary accounting; scheduling windows (4 months ≤100 workers / 6 months >100) + 30-day notice; base = current básico (time pay) or 6-month ÷ días laborables (variable); lodging/food +25% each; paid immediately before starting; termination proration (with-responsibility or despacho de hecho; completed year → full pay regardless — Art. 187); cash-compensation prohibition + collective/fractional schemes (188-189: 2×≥10d / ≥3×≥7d).
- Aguinaldo FRs (CT Arts. 196-203): annual prima; tiers 15/19/21 days (1-<3y / 3-<10y / ≥10y — seniority at payment date); proportional for <1 year AT DEC-12; base derivation (199); payment window 12-20 December (200); no disciplinary forfeiture (201); termination proration before Dec-12 (202); justifiable-absence days count as worked (203).
- ISR interface FRs (BY REFERENCE): exento/gravado split owned by taxation/04 (R22 vintages; 2-SMM comercio-y-servios floor from Task 2's CSV); payroll supplies the gross prima; June/December recálculo interplay pointer (53_).
- IBC exclusion LB note (09_ Art. 14 b: aguinaldo out of IBC; CT Art. 119: prestaciones out of salario) + ISR gravada classification nuance (vacation pay = remuneración gravada for ISR — mapping matrix from Task 1 governs; record the mapping row, do not re-derive taxation).
**AC examples:** tier flip at 3-year anniversary; <1-year worker paid Dec-10 proportional; vacation +30% computation; aguinaldo net of no-forfeiture invariant.

### Task 5: `sv/requirements/payroll/05_social-security-contributions.md`

**Files:** Create `sv/requirements/payroll/05_social-security-contributions.md` + CSV sidecar `ss_contributions.csv`
**Covers:** P6
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- ISSS FRs (08_): affiliation scope (Art. 3 all dependent workers; reglementary high-income exception as dated-data OQ — SOQ-15); rates Art. 29 (salud 7.5% patrono / 3% trabajador; Art. 99 public special 6.68%/2.67% medical-only; voluntary = both shares); base = "remuneración afecta" with reglementary variable/in-kind/presumed-SMM fallbacks (Art. 34); employer-share no-deduction invariant (Art. 33 + fine/restitution).
- SIP FRs (09_ D.L. 614): cotización 16% = 7.25% trabajador + 8.75% empleador with destination split 9.0/6.0/1.0 (Art. 16) + the 1%-increment never-pass-through invariant; IBC FRs (Art. 14: salario mensual or subsidy; ordinary-services money retribution — vacations/commissions IN; aguinaldo/viáticos/ocasionales/prestaciones OUT; SMM floor with sector-associated exceptions per Normativa Técnica; calendar-day months 30/31; multi-job per-salary; pensioner-risk-professional base) — reference Task 1's mapping matrix, do not restate; independent workers full-share declared-income mode (Art. 15); affiliation/routing (Art. 8 choice + 20-day default; Art. 11 exclusions IPSFA/IvD; subsidy-month handling Art. 16 inciso).
- Caps as dated data + CSV: AFP $472.93 / ISSS $30.00 ($-caps) + INPEP 7.5% / IPSFA 9.5% / CEFAFA 5% / Bien. Mag. 5.58% / ISSS-IVM 7.5% (%-maxima) — source = F-14 v16 print Oct-2025 (SOQ-11: payroll owns the VALUES, F-14 mirrors as validations); instruments absent (SOQ-15/16/17 OQ rows); pensioner-side rows (7.80% health R23; 7% solidarity >6×PM) as adjacent config.
- CSV schema: regime/institution × worker%/employer% × cap-type × cap-value × valid_from × instrument-OQ.
**AC examples:** 16% split posting with correct destination legs; IBC excludes aguinaldo but includes commissions; cap clamp at $1,000-implied ISSS base → $30 worker share (value-level only via F-14 print); regime routing by employee.

### Task 6: `sv/requirements/payroll/06_ss-declaration-remittance.md`

**Files:** Create `sv/requirements/payroll/06_ss-declaration-remittance.md`
**Covers:** P7
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- Declare+pay FR (09_ Art. 21): within the FIRST 10 DÍAS HÁBILES of the following month; electronic; carries BOTH the AFP previsional declaration and the ISSS obrero-patronal planilla (planilla-única mechanism pointer, Art. 27 — spec absent OQ); per-AFP routing by affiliation; subsidy-payer variant.
- Omisión/inconsistencia procedure FRs (09_ Art. 22: Administradora notice ≤20 días hábiles; cure ≤10 días hábiles; MTP inspection/certification chain) — Odoo-side: discrepancy-response workflow.
- Sanctions/mora FRs: ISSS late recargo 1%/month-or-fraction (08_ Art. 33); SIP late-declaration 5% ≤20d / 10% > / non-enrollment 15% (Art. 143); incomplete $600/$1,200 (144); non-payment 20% + 2%/mo, underpayment 10% + 5%/mo (145) — accrual model FR + privileged/imprescriptible credit notes (09_ Arts. 24-25).
- Work-accident report FR (08_ Art. 75 ≤48h, Institute forms, Alcaldía filing where no ISSS office).
- Employer record duties FR (16_ Art. 11 planillas/asistencia/recibos + CT Art. 160 inspection access) — retention/audit surface.
**AC examples:** deadline falls on 11th día hábil due to asuetos (consumes fiscal-reporting/08 engine by FR id); mora accrual at 3.5 months; planilla export carries both regimes.

### Task 7: `sv/requirements/payroll/07_contracts-termination.md`

**Files:** Create `sv/requirements/payroll/07_contracts-termination.md`
**Covers:** P8
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- Contract taxonomy FRs (CT Arts. 25-28): indefinite presumption + plazo validity gates (transitory/temporary/eventual); obra contracts (7-day notice or 7 days' pay); interinos (return-termination; >15-day permanence presumption); 30-day trial (no-cause termination; no second trial within a year) — routing termination outcomes.
- Indemnización FRs (Arts. 58-59): 30 days salario básico per year + prorated fractions; minimum 15 days; **countable salary capped at 4× daily legal SMM** (feed from Task 2 CSV; sector unpinned → OQ kin SOQ-18); fixed-term variant capped at indefinite equivalent.
- Termination constancia FR (Art. 60 content model); despacho presumption (Art. 55).
- Illness/maternity FRs (Arts. 307-313): illness subsidy 75% básico with seniority-tier day caps (60/40/20) + grave-fault exception; chronic-illness stability + full-ISSS-subsidy (308-A/B); maternity 16 weeks @75% básico (10 post-partum mandatory; prenatal supplement; late-birth extension; ISSS subsidy deduction; no obligation beyond limits) + **Art. 311 VOID LB note (no tenure gate — never implement)**; lactancia 1h/d (2×30m) paid work time; post-licencia sickness continuation; sepelio 60 days básico (colon floor LB note).
- Termination proration cross-refs (vacations Art. 187 / aguinaldo Art. 202 — reference Task 4 FRs by id).
**AC examples:** indemnización with 4×SMM clamp; maternity scheduling 6+10 weeks; no-tenure-gate benefit; tier-1 illness cap at 60 days.

### Task 8: `sv/requirements/payroll/08_isr-interfaces.md`

**Files:** Create `sv/requirements/payroll/08_isr-interfaces.md`
**Covers:** P9 + P10 pointer
**FR numbering:** continues SV-PAY prefix.
**Content requirements:**
- ISR retention-base interface FR: worker SS/pension cotizaciones excluded from remuneraciones gravadas (53_ literal d via SV-TAX-FR-104 — BY REFERENCE; this file only states the payroll-side input contract).
- F-14 value-feed FRs (SOQ-11): payroll produces the 7 SS column values + Renta quartet S-V + devengado/bonificaciones/aguinaldo-split per employee-period; fiscal-reporting/06 owns the column model/validations (reference by FR id); haven-25% flag feed.
- F-910 annual feed (fiscal-reporting/07 by id): 12-month consolidation inputs; 01-vs-60 classification rule input flag (retained-at-least-once).
- F-11 personal-deduction feeds (65_/EVID-210): SS rows 713-724 values; AFP voluntary 717 with the stale-label LB note (live rule = D.L. 614 Art. 138 ≤10% IBC + 5-year withdrawal clawback — FR); deducción fija 722 pointer to taxation.
- Voluntary pension savings FRs (09_ Art. 138): ≤10% IBC deductibility (employer + employee contributions); transfers tax-free; <5-year withdrawal → renta gravable reversal flag; non-affiliated ≤10% declared-renta variant.
- Rentas no gravadas LB note (09_ Art. 26 cotizaciones/rendimientos; F-11 casilla 734 surface).
- Quincena-25 pointer FR (P10): BLOCKED — D.L. 499 (D.O. 14-ene-2026) not in corpus; known surface = F-14 v17 casillas 417/418 (EVID-184, FREP FR-165/166 by id); no payroll income-treatment FRs until acquisition (OQ row; acquisition queued as source 66).
**AC examples:** payslip netting worker-cotizaciones before retention base; 717 deduction capped at 10% IBC; withdrawal-before-5y flags reversal; Quincena-25 absent → no rows.

### Task 9: index + coverage + registry flips

**Files:** Create `sv/requirements/payroll/00_index.md`; update `sv/requirements/COVERAGE.md` (rows 08_/09_/11_/16_/65_ → cited-as-LB; rollup), `sv/README.md` + `sv/requirements/README.md` if present (topic-dir flip), cross-ref pointers: taxation/00_index (F-11 711-725 feed note on 04's aguinaldo zone), fiscal-reporting/00_index (SOQ-11 back-pointer resolved-kin).
**Content requirements:** index = S2/S3 pattern (files & FR ranges table, numbering note, OQ rollup with SOQ-15..21 mapping); coverage rollup recount; totals verified by the structural checks below.
**Verification (all tasks):** template 7-section integrity; every FR has ≥1 LB row; FR numbering wave-sequential no gaps; CSVs parse (`python -c "import csv;list(csv.DictReader(open(...)))"`); OQ ids unique per file; cross-file references resolve to real FR ids/OQ ids.

---

## Execution protocol

Subagent-driven: one fresh implementer per task; per-task reviewer against the master index + evidence files; fix rounds as findings demand; final whole-wave review; ONE fix wave; push; ledger rulings copied to HANDOVER before workspace deletion.
