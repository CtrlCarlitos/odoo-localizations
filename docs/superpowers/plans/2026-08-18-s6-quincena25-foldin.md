# S6 Quincena-25 FR Fold-in Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fold the W11 Quincena-25 package (D.L. 499 + MH guía/manual/instrucciones/plantilla, sources 66_-70_, EVID-236..239) into the existing requirements corpus as FRs across payroll, fiscal-reporting and taxation, replacing every BLOCKED/absence invariant that the acquisition unblocked.

**Architecture:** Edit wave (no new requirement files except a `special-regimes/00_index.md` wave-prep stub). Amendments in place (FR ids stable) + appended FRs per prefix. Numbering contract pinned below so tasks are order-independent. Per-task implementer + reviewer subagents; final whole-wave review; one fix wave; push.

**Tech Stack:** Markdown requirements files (7-section Takumi template), CSV sidecars. No code. "Tests" = structural verification commands (numbering continuity, LB-citation presence, cross-ref resolution, CSV parse).

**Spec:** `sv/.extractions/66-70_Quincena25.evidence.md` (EVID-236..239, the sole new-evidence input) + `sv/.extractions/00_MASTER_INDEX.md` clusters P10/F10 + rulings R21/R24 + SOQ-09 (resolved). Implementers MUST read the evidence file fully before editing; reviewers verify every FR against it.

## Global Constraints

- **Template discipline:** 7-section format (Purpose / Legal Basis / FRs / Data Model / Odoo Mapping / ACs / OQs). Every new/amended FR cites at least one LB and, where applicable, `EVID-nnn`. LBs carry verbatim Spanish + English translation (file convention; copy verbatim from the evidence file — never paraphrase law).
- **Numbering contract (pinned — do not deviate):**
  - `SV-PAY-FR-138..141` → `payroll/04_statutory-benefits.md` (new §3.4)
  - `SV-PAY-FR-137` → REWRITTEN in place in `payroll/08_isr-interfaces.md` (absence invariant → positive income-treatment FR); `SV-PAY-FR-142..143` new in 08
  - `SV-FREP-FR-166/167` → AMENDED in place in `fiscal-reporting/06_f14-declaration.md`; `SV-FREP-FR-209..211` new in 06
  - `SV-FREP-FR-212` new in `fiscal-reporting/07_codes-and-informs.md` (+ `f14_income_codes.csv` row 73)
  - `SV-TAX-FR-173..174` new in `taxation/01_isr-framework.md`; `SV-TAX-FR-175` new in `taxation/02_isr-deductions.md`
  - No other FR renumbered; AC/OQ numbering continues each file's existing sequence.
- **In-file rulings that MUST be carried** (from the evidence file's OQ resolutions):
  1. Casilla **724 operative**; 734 = guía body typo `[sic]` (label extended with "Quincena Veinticinco").
  2. Annex-CSV delimiter = **semicolon** (70_ header; 69_ list-separator note) — the "delimitado por comas" type-label is superseded.
  3. January-window = **every January from 2026** (67_ Anexo 3 + 69_); 68_'s "exclusivamente Enero 2026" reflects its publication moment (durable rule reading).
  4. 66_ Art. numbering `[sic]`: "Art. 5" prints twice; Condición especial cited as **Art. 3 positional** with [sic] note (OQ carried).
- **Dead-print discipline (R21):** F-11 v19 still prints pago-mínimo rows — the never-feed guard extends to v19.
- **Evidence-only:** no facts beyond the corpus; doubts become OQs, never guesses. Known carried OQs: double benefit 2026 (deduction+credit, 66-70_ OQ-4 → taxation); F-11 v19/v20 acquisition ≥71 (watch); F-14 apéndice v17 code-73 presence unverified (no v17 manual).
- **Cross-file refs by FR id** (ids pinned above, so cite ids directly — e.g. `SV-FREP-FR-209`). Interfaces between payroll feeds and FREP consumers are by id, values never restated (SOQ-11 discipline).
- **Version regime (D12):** dated rules (2026 voluntary/2027 mandatory, credit FY-2026-only, annex window from 2026) encoded as dated configuration with effective dates from the law, never hardcoded conditionals without dates.
- **Process:** execute on `main` (S2/S3/S4 precedent — no worktree). Commit style: short imperative, no emojis, commit per task.

---

### Task 1: payroll/01 — canonical matrix gains the Quincena-25 row

**Files:**
- Modify: `sv/requirements/payroll/01_salary-model.md` (FR-004 matrix ~line 192+, §4 selects ~line 187, §5 FR-004 row ~line 257, §6 ACs)

**Interfaces:**
- Consumes: `SV-PAY-FR-004` (matrix), EVID-236 (66_ Arts. 1/4/5), new FRs `SV-PAY-FR-138..143` (cited by id as the mechanics/files owning them).
- Produces: matrix row + `sv_pay_earning_class` value `quincena_25` consumed by files 04/05/08 and `SV-TAX-FR-104`/`SV-FREP-FR-143` consumers.

- [ ] **Step 1: Read the evidence + file.** Read `sv/.extractions/66-70_Quincena25.evidence.md` EVID-236 fully; read `01_salary-model.md` end-to-end to match conventions (matrix column semantics, select-value lists, AC style).
- [ ] **Step 2: Amend FR-004's matrix.** Add one row to the canonical matrix table:

  | Concept (English) | class | salario? | IBC | ISR gravada? | F-14 column family |
  |---|---|---|---|---|---|
  | Quincena Veinticinco annual complement (D.L. 499; paid 15–25 Jan; 50% of monthly salario básico o nominal, gate ≤ US$1,500.00) | quincena_25 | no — ingreso complementario independiente del salario ordinario, aguinaldo y otras prestaciones (66_ Art. 1) | no — never in any benefit-calculation base nor SS/pension cotización (66_ Arts. 1/5) | no_gravada (66_ Art. 4) | none — surfaces ONLY in the separate January-only Quincena annex (SV-FREP-FR-209), never in the G/H/J-K retention-annex families |

  Match the existing matrix's exact column headers/format (copy the neighboring row's shape). Extend the FR-004 bullet text with one clause naming the Quincena-25 row and citing `SV-PAY-FR-138..143` + `SV-FREP-FR-209..212` as the by-id consumers.
- [ ] **Step 3: Update §4 selects.** Add `quincena_25` to the `sv_pay_earning_class` select values row (~line 187). No new fields: `sv_pay_ibc_included`=false and `sv_pay_isr_gravada_input`=no_gravada and `sv_pay_f14_column_family`=none are existing values set by the matrix row.
- [ ] **Step 4: Update §5 + §6.** §5 FR-004 row: append "quincena_25 row added S6 (D.L. 499; EVID-236)". §6: add one AC (continuing the file's AC numbering): *Given a January payslip with an ordinary salary line and a Quincena-25 line of US$750.00, then the Quincena line classifies quincena_25 with ibc_included=false, isr=no_gravada and f14_column_family=none, and it appears in NO retention-annex export column (only in the Quincena annex feed of SV-PAY-FR-142)* (FR-004; EVID-236).
- [ ] **Step 5: Verify.** Run: `grep -c "quincena" sv/requirements/payroll/01_salary-model.md` (expect ≥4 hits); `grep -n "SV-PAY-FR-004" sv/requirements/payroll/01_salary-model.md` (row intact). Confirm no other matrix row changed: `git diff --stat sv/requirements/payroll/01_salary-model.md` shows a small diff.
- [ ] **Step 6: Commit.** `git add sv/requirements/payroll/01_salary-model.md && git commit -m "S6 fold-in: payroll/01 matrix gains quincena_25 row (FR-004 amendment)"`

### Task 2: payroll/04 — Quincena-25 benefit mechanics (FR-138..141)

**Files:**
- Modify: `sv/requirements/payroll/04_statutory-benefits.md` (new §3.4 after §3.3, §2 LB table, §4, §5, §6, §7)
- Possibly touch: `sv/requirements/payroll/05_social-security-contributions.md` (one note, Step 6 — only if FR-075's IBC definition enumerates exclusions)

**Interfaces:**
- Consumes: EVID-236 (66_ Arts. 1/2/3[ sic]/5/6), the §3.2 aguinaldo eligibility rules (FR-053..059 mirrored by reference), `sv/requirements/payroll/02_minimum-wage.md` sidecar (not consumed — gate is the law's own US$1,500.00, not SMM), `SV-PAY-FR-004` matrix row.
- Produces: `SV-PAY-FR-138..141` — the benefit quantum/eligibility/regime/invariants consumed by `payroll/08` FR-137/142/143, `SV-TAX-FR-173..175` and `SV-FREP-FR-166/209..212`.

- [ ] **Step 1: Read evidence + files.** EVID-236/237 fully; `04_statutory-benefits.md` end-to-end; skim `05` FR-074/075 for the IBC enumeration check.
- [ ] **Step 2: Add LBs to §2.** Append rows (verbatim from evidence, with translations, `sv/sources/66_Ley_Quincena25_DL499.pdf`):
  - **LB-0xx (66_ Art. 1):** "Quincena Veinticinco... ingreso complementario, que deberá pagarse entre el quince y el veinticinco de enero de cada año... cincuenta por ciento..." — actually split: Art. 1 = nature/window/invariants ("de forma integra y sin ningún descuento... independiente del salario ordinario, aguinaldo... no formará parte de la base de cálculo de otras prestaciones... en ningún caso deberá ser objeto de retención ni descuento alguno por concepto de aportes u otras obligaciones de Seguridad Social o del Régimen Previsional"); Art. 2 = amount + gate ("cincuenta por ciento (50%) sobre el salario básico o nominal mensual... solo será aplicable para aquellos trabajadores cuyo salario básico o nominal mensual sea igual o inferior a mil quinientos dólares"); Art. 3 [printed "Art. 5" — sic, positional] = termination proportional right; Art. 4 invariants (inembargable + fiscal) live in taxation-side LBs here only as the inembargable clause; Art. 6 = 2026 transitory split. Use FOUR LB rows (Art. 1, Art. 2, Art. 3 [sic], Art. 6) with location "Arts. 1-3, 5-6 pp.2-6 (EVID-236)". Mark the file's §2 authority note: 66_ = the law (current, effective 14-ene-2026).
- [ ] **Step 3: Write §3.4 "Quincena Veinticinco (D.L. 499)" FRs.** Near-final wording (implementer polishes to file style):

  - **SV-PAY-FR-138:** The system shall compute, for every eligible worker, the annual Quincena-25 benefit as **50% of the monthly *salario básico o nominal*** the worker is perceiving at the moment the prestación materializes, with the law's OWN base (salario básico o nominal — NOT the CT 119 salario integrante; the law names its base), gated to workers whose monthly salario básico o nominal is **≤ US$1,500.00**, and shall schedule payment inside the **15–25 January** window each year. The gate threshold is the law's printed constant as dated data (D12). (LB Art. 2; LB Art. 1; EVID-236)
  - **SV-PAY-FR-139:** The system shall derive eligibility by MIRRORING the aguinaldo/compensación-adicional requirements of the worker's sector regime (the law's express cross-reference, "sin que ello implique equiparar" — requirements mirrored, never the benefit equated; aguinaldo rules of §3.2 consumed by reference): continuous/duracionales gates per §3.2 FR-053/054 kin; public-sector and municipal workers must be *laborando* for the entity at the moment of payment; special-regime institutions follow the Ley Compensación Adicional supletoria; and a worker terminated with employer responsibility or *despido de hecho* before/on 25-January retains a PROPORTIONAL right computed per the aguinaldo/CAE proportional rules (66_ Art. 3 [printed Art. 5 — sic]; positional attribution per the evidence OQ-1). (LB Art. 3; EVID-236; cross-ref FR-053..059)
  - **SV-PAY-FR-140:** The system shall drive the payment duty by a dated regime flag (D12): **ejercicio 2026 = public sector MANDATORY (budget modification) / private sector VOLUNTARY** (voluntary payment due at the latest 25-Jan-2026 and carrying the employer credit of `SV-TAX-FR-174`); **from ejercicio 2027 = MANDATORY for ALL employers** public and private. The flag is configuration dated by ejercicio, never a global constant. (LB Art. 6; EVID-236/238)
  - **SV-PAY-FR-141:** The system shall enforce the payment invariants: the Quincena-25 is paid IN FULL — no ISR retention, no SS or pension cotización, no deduction or discount of any kind; it NEVER enters the calculation base of any other prestación (aguinaldo daily base FR-055, vacaciones base FR-047, indemnización bases `07` FR-105, SMM-derived gates) nor the SS IBC (`05` FR-075); and it is *inembargable* (66_ Art. 4). The not-in-any-base invariant is a negative test (AC). (LB Art. 1; LB Art. 3; EVID-236)
- [ ] **Step 4: §4 Data Model + §5 Odoo Mapping.** DM: `hr.salary.rule` uses the existing matrix flags (no new rule fields); add config entity row: `l10n_sv.pay.quincena.regime (config)` — `regime` select `mandatory · voluntary_2026 · public_2026` computed by ejercicio (2026 split / 2027+ mandatory) + `payment_window` derived 15–25 Jan. §5: map FR-138..141 to `hr.payroll` rule + config rows; note Odoo-native.
- [ ] **Step 5: §6 ACs + §7 OQ.** Four ACs (continue numbering):
  - *AC:* básico nominal US$1,500.00 in January 2027 → benefit US$750.00 paid 15–25 Jan; básico US$1,500.01 → no entitlement line at all (FR-138).
  - *AC:* worker hired 1-Nov-2026 continuously employed to 25-Jan-2027 → proportional right per the §3.2 aguinaldo proportional mechanics; despido de hecho 10-Jan → proportional right preserved (FR-139).
  - *AC:* private employer ejercicio 2026 without the voluntary opt-in → no accrual; with opt-in → payment ≤ 25-Jan-2026 and the credit feed of SV-TAX-FR-174 activates; ejercicio 2027 → accrual mandatory without opt-in (FR-140).
  - *AC:* a worker with ordinary salary + aguinaldo accrued + Quincena US$750.00 → the aguinaldo daily base (FR-055) and the IBC (05 FR-075) compute EXACTLY as if the Quincena were absent; no retention line appears on the Quincena line (FR-141; negative test).
  §7 OQ (carry): *OQ-00x — 66_ print article numbering [sic] ("Art. 5" twice); Condición especial cited as Art. 3 positionally; pin from a cleaner D.O. print if the /seleccion route recovers (volume Id 31679)* (open, sources-watch).
- [ ] **Step 6: IBC note check in 05.** Read `05` FR-075: IF its IBC definition enumerates exclusions (aguinaldo/viáticos/ocasionales list), append "…and the Quincena-25 (66_ Art. 1; SV-PAY-FR-141)" to that enumeration + the LB-kin note; if it defines IBC generically, make NO edit (the exclusion rides on 04 FR-141 + the matrix row). Record which branch you took in the commit message body.
- [ ] **Step 7: Verify.** `grep -o "SV-PAY-FR-1[0-9][0-9]" sv/requirements/payroll/*.md | sort -u` — 138,139,140,141 present exactly once each as definitions; every new FR block contains "(LB-" (LB citation). Markdown tables well-formed (no broken pipes in preview).
- [ ] **Step 8: Commit.** `git add sv/requirements/payroll/04_statutory-benefits.md sv/requirements/payroll/05_social-security-contributions.md 2>/dev/null; git commit -m "S6 fold-in: payroll/04 quincena-25 mechanics (FR-138..141) + 05 IBC note (if applicable)"` (adjust if 05 untouched; single-line message).

### Task 3: payroll/08 — income treatment + feeds (FR-137 rewrite, FR-142..143)

**Files:**
- Modify: `sv/requirements/payroll/08_isr-interfaces.md` (title, §1, §2 LB-009 + new LBs + notes, §3.7, §4, §5, §6 AC-015 rewrite + new, §7 OQ-002/OQ-004)

**Interfaces:**
- Consumes: `SV-PAY-FR-138..141` (mechanics by id), `SV-FREP-FR-165/166` (417/418, existing), NEW `SV-FREP-FR-209..212` (annex engine + code 73), `SV-TAX-FR-173` (renta no gravada, taxation-owned), EVID-236/237/238/239.
- Produces: `SV-PAY-FR-137` (rewritten: worker-side treatment), `SV-PAY-FR-142` (per-worker annual Quincena ledger record = the annex-CSV field contract), `SV-PAY-FR-143` (417/418 aggregate feed). Consumed by FREP 06/07 and taxation.

- [ ] **Step 1: Read evidence + file.** All four EVIDs; `08_isr-interfaces.md` end-to-end (it is the file most rewritten — treat gently: keep every non-Quincena section byte-identical).
- [ ] **Step 2: Title + §1.** Title: drop "and the Quincena-25 pointer" → "…and the Quincena-25 income treatment". §1's final clause: replace the BLOCKED sentence ("and the Quincena-25 pointer — BLOCKED: …NO payroll income-treatment FRs") with: "and the Quincena-25 income treatment (P10 — law acquired as 66_, D.L. 499, D.O. N° 8 T.450 14-ene-2026): the renta-no-gravada/no-retention/no-cotización classification and the per-worker ledger + 417/418 aggregate feeds into the F-14 v17 January annex (SV-FREP-FR-209..211) and the F-910 code-73 surface (SV-FREP-FR-212)."
- [ ] **Step 3: §2 LB updates.** LB-009: rewrite the trailing parenthetical — law now IN corpus: "**acquired 2026-08-18 as `66_`** (official DGII copy `700-DGII-LY-2025-008` via transparenciafiscal; D.O. `/seleccion` outage workaround); current authority for the Quincena-25". Add THREE LB rows (verbatim from evidence, source `sv/sources/66_Ley_Quincena25_DL499.pdf` + `sv/sources/67_Guia_Orientacion_Quincena25.pdf`):
  - **66_ Art. 4** (fiscal): rentas no gravables declaration + no ISR retention + inembargable + gasto deducible (paid+documented) — full quote from EVID-237 (translation provided there).
  - **66_ Art. 1** (invariants quote): "de forma integra y sin ningún descuento… no formará parte de la base de cálculo… en ningún caso… retención ni descuento… Seguridad Social o del Régimen Previsional" (EVID-236).
  - **67_ §3.f/§3.g + Anexo 3** (reporting chain quote): F-910 NO GRAVADOS column + Código 73 auto + renta-en-línea ingreso no gravado; annex January-only (EVID-238). Note in the row: *casilla 724 operative, 734 = guía typo [sic] (in-file resolution, evidence OQ-3)*.
  Also extend the LB-004..006 area note + §2 version-regime paragraph: **65_ F-11 v18 superseded as current print by v19 (casilla 319 Quincena credit; still prints dead pago-mínimo rows — R21 extends) and v20 (special-regime subjects)** — acquisition candidates ≥71 (OQ-004 sharpened, stays open).
- [ ] **Step 4: §3.7 rewrite (heading + FRs).** Heading: "### 3.7 Quincena Veinticinco income treatment and feeds (P10 — 66_ acquired)". REWRITE **SV-PAY-FR-137** (id stable) from the absence invariant to:

  > **SV-PAY-FR-137:** The system shall classify every Quincena-25 payment as *renta no gravada* per D.L. 499 Art. 4 (the special-law declaration prevailing per its Art. 8; `taxation/01` SV-TAX-FR-173 owns the ISR-side rule — cited by id): stamped no_gravada by the matrix (FR-004 row), EXCLUDED from the retention base and from the June/December recálculo aggregation (never in the SV-TAX-FR-104 inputs of FR-121), generating NO ISR retention line, NO worker SS/pension cotización (out of IBC per `05` and FR-141) and NO entry in any benefit base — replacing this file's former absence invariant (the law was acquired as 66_ on 2026-08-18; the invariant is withdrawn). (LB-0xx Art. 4; LB-0xx Art. 1; EVID-236/237; cross-ref SV-TAX-FR-173, SV-PAY-FR-121, SV-PAY-FR-141)

  NEW **SV-PAY-FR-142:** The system shall maintain, per worker and ejercicio, the Quincena-25 ledger record carrying EXACTLY the seven annex fields of the F-14 v17 January annex (consumed by SV-FREP-FR-209): A *apellidos y nombres* (≤100 chars, uppercase, no commas/quotes) · B *NIT* (≤14 digits, no hyphens/plecas) XOR C *DUI* (≤9 digits) · D *fecha de pago* dd/mm/aaaa · E *salario nominal* (4 enteros + 2 decimales, no thousands separator) · F *quincena veinticinco* amount (3+2) · G *período* mmaaaa — the payroll-owned value source; amounts from FR-138; the XOR rule validated payroll-side before export. (EVID-239; cross-ref SV-FREP-FR-209)
  NEW **SV-PAY-FR-143:** The system shall produce the declaration aggregates consumed by SV-FREP-FR-166: casilla **417** = count of workers paid and casilla **418** = total amount, per declaración period — reporting-only, never in retention arithmetic (SV-FREP-FR-166's isolation by id); reporting window January-only per SV-FREP-FR-210. (EVID-238; cross-ref SV-FREP-FR-166, SV-FREP-FR-210)
- [ ] **Step 5: §4 + §5.** DM: add entity `l10n_sv.pay.quincena.feed (new)` with the seven fields (types: char(100)/char(14)/char(9)/date-format char/monetary-string/monetary-string/char(6)) + `ejercicio`; note "string-typed to mirror the export contract (SV-FREP-FR-209 truncation discipline)". §5: rewrite the FR-137 row (`l10n_sv.pay.quincena feed stamps — renta no gravada; no retention/cotización/base entry`) and add FR-142/143 rows (`l10n_sv.pay.quincena.feed`, `l10n_sv.pay.quincena.feed aggregate`). Update the FR-165 citation sentence in §5's version-regime notes (gate still cited; add FR-209..212).
- [ ] **Step 6: §6 + §7.** REWRITE **AC-015** (positive): *Given a January-2027 payroll with Quincena payments to 10 workers totalling US$5,000.00 (all gates passed), then each payment line stamps no_gravada with no retention line and no IBC/base effect, and the ledger yields 10 feed records + aggregates 417=10 / 418=5,000.00 consumed by SV-FREP-FR-166/209 — the by-id pointers replace the former absence invariant.* Add one AC: *Given a worker with NIT 22222222222222 and DUI both present, the feed record fails payroll-side validation (XOR) and is not exported; given name "Prueba Persona", the export field renders `PRUEBA PERSONA` uppercase with the amount `250.00` and período `012027` — mirroring the 70_ example-row contract (FR-142).* §7: flip **OQ-002** status → `resolved (acquisition)` — text: acquired 66_ 2026-08-18; FR-137/142/143 landed (this wave); FREP 06 OQ kin resolved by FR-209..211. Sharpen **OQ-004**: v19/v20 CONFIRMED to exist (67_ Anexos 1/8); feed keys 713-725/734 re-verify on acquisition (≥71); R21 dead rows extend to v19.
- [ ] **Step 7: Verify.** `grep -n "BLOCKED\|NOT in the corpus" sv/requirements/payroll/08_isr-interfaces.md` → only historical-context hits (LB-009's acquisition note may mention the outage — acceptable if factual); FR-137 block contains "renta no gravada"; `git diff` shows no changes outside Quincena sections + LB/version notes.
- [ ] **Step 8: Commit.** `git commit -m "S6 fold-in: payroll/08 quincena-25 income treatment + feeds (FR-137 rewrite, FR-142..143)"` (with `git add` of the file).

### Task 4: fiscal-reporting/06 — the January annex upload engine (FR-166/167 amended, FR-209..211)

**Files:**
- Modify: `sv/requirements/fiscal-reporting/06_f14-declaration.md` (§2 LB table, §3.8, §4, §5, §6, §7; title row §1 mentions)

**Interfaces:**
- Consumes: `SV-PAY-FR-142/143` (ledger + aggregates), `SV-FREP-FR-165` (vintage gate, unchanged), EVID-238/239 (67_ Anexo 3, 68_ pp.3/11/13/16, 69_ §§1-3/H, 70_ header), SOQ-09 (resolved).
- Produces: `SV-FREP-FR-209` (annex CSV export contract), `SV-FREP-FR-210` (January-window upload gate + replacement), `SV-FREP-FR-211` (417/418 derivation + code-73 wiring); amended `SV-FREP-FR-166/167`.

- [ ] **Step 1: Read evidence + file.** EVID-238/239 fully; `06_f14-declaration.md` end-to-end (esp. §3.7-3.9, §7 OQs — locate the SOQ-09-kin OQ-001).
- [ ] **Step 2: §2 LBs.** Add FOUR LB rows (source files 67_/68_/69_/70_ respectively, verbatim quotes from the evidence):
  - 67_ Anexo 3 + §3: January-only rule + F-14 v17 section labels + casillas 417/418 auto-sum from the annex upload.
  - 68_ pp.3/11/13/16: upload enabled only January periods from 2026; "exclusivamente Enero 2026" publication-moment phrasing (durable-rule reading noted in-row); "independiente del anexo de retenciones"; line-numbered validation; code 73 auto at presentation.
  - 69_ §1-3: the 7-column spec (field-by-field widths/formats/XOR verbatim).
  - 70_ header line: `APELLIDOS Y NOMBRES;NIT;DUI;FECHA DE PAGO;SALARIO NOMINAL;QUINCENA VEINTICINCO;PERIODO` — semicolon operative (69_'s "delimitado por comas" type-label superseded by its own list-separator instruction; in-file resolution carried in-row).
- [ ] **Step 3: Amend §3.8.** FR-165: unchanged. **FR-166 amend:** replace "provisionally computed from an internal Quincena-25 ledger classification under the FR-167 working assumption" → "computed from the payroll-owned Quincena ledger and aggregates (SV-PAY-FR-142/143)"; keep the isolation clause verbatim. **FR-167 rewrite:** from BLOCKED/working-assumption to RESOLVED: "The v17 annex-level representation of Quincena-25 rows is a SEPARATE January-only planilla upload — NOT an income code in, nor columns of, the v16 retention annex (68_ p.3: 'independiente del anexo de retenciones'; SOQ-09 resolved by the W11 package): the retention annex (FR-137 structure) is exported WITHOUT any Quincena row for ALL periods, and the Quincena surface is exclusively the FR-209..211 upload engine. The former working assumption (v16 columns + new income code) is WITHDRAWN." New FRs:

  - **SV-FREP-FR-209:** The system shall export the Quincena-25 annex as a 7-column CSV, semicolon-delimited, one row per paid worker, exactly per the 69_ §1-2 + 70_ spec: A apellidos y nombres ≤100 uppercase no-commas/no-quotes · B NIT ≤14 numeric no separators XOR C DUI ≤9 numeric · D fecha dd/mm/aaaa · E salario 4+2 decimals no-thousands-separator (max 7 chars) · F monto 3+2 (max 6) · G período mmaaaa — from the SV-PAY-FR-142 ledger; two-decimal truncation discipline at export (kin FR-027/030: computation rounds never, export truncates); the delimiter is semicolon regardless of the "comas" type-label (70_ header operative).
  - **SV-FREP-FR-210:** The system shall gate the Quincena annex upload to the January declaración period of each ejercicio from 2026 (67_ Anexo 3 + 69_ durable rule; 68_'s "exclusivamente Enero 2026" = its publication moment), offered only when the ledger holds payments for that ejercicio (68_ p.3), with replacement by clear-then-reupload (68_ Limpiar mechanics) and a line-numbered validation report mirroring the portal's per-record errors (68_ p.13; 69_ §H structure-and-montos validation).
  - **SV-FREP-FR-211:** The system shall derive, at annex presentation: casillas 417 (subject count) / 418 (total) auto-summed from the uploaded rows (67_ Anexo 3; FR-166's isolation intact) and the F-910 code-73 auto-assignment (68_ p.16) wired to SV-FREP-FR-212 — single data entry point: everything downstream (F-910, renta-en-línea 724-kin, F-11 v19 casilla 319) derives from this upload; a payroll-side cross-check warns when F ≠ 50%×E or E > US$1,500.00 (warning only — MH validates structure + montos, not the benefit formula; 69_ §H; OQ below).
- [ ] **Step 4: §4 + §5.** DM: `l10n_sv.f14.quincena.upload (new)`: `state` select `loaded · inconsistencies · presented`, `declaration_period`, `row_count`, `total_amount`, `validation_errors` (line-numbered). §5: map FR-209..211 (odoo; upload-state model) + amend FR-166/167 rows' notes (drop "annex-level BLOCKED").
- [ ] **Step 5: §6 + §7.** ACs (continue numbering): *AC:* the two 70_ example rows export verbatim (`PRUEBA PERSONA;22222222222222;;15/01/2026;500.00;250.00;012026` and `PRUEBA PRUEBA PERSONA;;444444444;25/01/2026;1500.00;750.00;012026` — semicolons, empty XOR column); *AC:* February period → upload option absent; January with prior presentation → replacement requires clear first; *AC:* 10 rows totalling 5,000.00 presented → 417=10, 418=5,000.00, F-910 code-73 row appears (with SV-FREP-FR-212), and casillas 330-336 unchanged (isolation negative test). §7: flip the SOQ-09-kin OQ-001 → resolved (text: resolved by W11 66_-70_; FR-209..211); add OQ: *MH-side validation depth — whether the portal rejects F ≠ 0.5×E or E > 1,500 (structural-only per 69_ §H reading); FR-211 ships warning-only* (open, MH-guidance watch); add OQ: *live-portal delimiter verification (AC tests both if ever verified live — 69_ OQ-2 kin resolved-in-file as `;`)* — optional, fold into the same OQ row if cleaner.
- [ ] **Step 6: Verify.** `grep -n "working assumption\|BLOCKED" sv/requirements/fiscal-reporting/06_f14-declaration.md` → no Quincena-context hits remain; `grep -c "SV-FREP-FR-2[01][0-9]" file` → 209/210/211 defined once each; markdown tables intact.
- [ ] **Step 7: Commit.** `git commit -m "S6 fold-in: frep/06 quincena-25 january annex engine (FR-166/167 amend, FR-209..211)"` (with add).

### Task 5: fiscal-reporting/07 — F-910 code 73 (FR-212 + CSV row)

**Files:**
- Modify: `sv/requirements/fiscal-reporting/07_codes-and-informs.md` (§2 LB, §3.3 FR-179/181 notes, new FR-212 in §3.3, §4, §5, §6, §7)
- Modify: `sv/requirements/fiscal-reporting/f14_income_codes.csv` (row 73)

**Interfaces:**
- Consumes: `SV-FREP-FR-211` (auto-assignment at presentation), `SV-PAY-FR-142` (per-worker amounts), EVID-238 (67_ §3.f + 68_ p.16).
- Produces: `SV-FREP-FR-212` + catalog row 73 (class no_gravado; F-910-side authority) consumed by the F-910 builder FR-179/180.

- [ ] **Step 1: Read evidence + file.** EVID-238; `07_codes-and-informs.md` §3.3 + catalog FRs (171/172/181); the CSV header + rows 70-72 for format.
- [ ] **Step 2: §2 LB.** Add LB: 67_ §3.f verbatim ("En el Informe Anual de Retenciones (F-910), el monto pagado… NO GRAVADOS… Código 73 Ingresos No Gravados Pagados Quincena Veinticinco, generado de forma automática… de acuerdo a los datos cargados en anexo… (F-14)") + 68_ p.16 ("el código de ingreso 73 se asignará de manera automática al momento de presentar la declaración") — source `sv/sources/67_Guia_Orientacion_Quincena25.pdf` / `68_…pdf`, location "§3.f p.4 / p.16 (EVID-238/239)".
- [ ] **Step 3: CSV row 73.** Append to `f14_income_codes.csv` (match quoting/format exactly):
  `73,"Ingresos No Gravados Pagados Quincena Veinticinco",no_gravado,ingresos_no_gravados,"section 'INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO' casillas 417/418","D.L. 499 Art. 4 (via 66_); F-910 auto-population per 67_ §3.f + 68_ p.16",f17_kin,2026-01,"Authority = MH package (67_/68_), NOT the v16 apéndice (35_ predates the law); F-14 apéndice v17 inclusion unverified (no v17 manual — OQ); auto-assigned from the F-14 Quincena annex upload (SV-FREP-FR-211)"`
- [ ] **Step 4: FR-212 + amendments.** New **SV-FREP-FR-212** in §3.3 (after FR-183 block or at §3.3's end — follow file flow): "The system shall populate the F-910's NO GRAVADOS surface with income code **73 'Ingresos No Gravados Pagados Quincena Veinticinco'** — auto-assigned at declaration presentation from the F-14 Quincena annex upload (SV-FREP-FR-211; 68_ p.16), fed by the SV-PAY-FR-142 ledger — reported as a NO-GRAVADO total (the worker-side amounts), never as a retention consolidation (no R=12 coupling: nothing was retained) and never inside the retained-tax totals; the code exists in the catalog as a dated 2026-01 row whose print authority is the MH package, with F-14 apéndice v17 inclusion unverified (OQ)." Amend FR-179/FR-181 notes: catalog scope sentence gains "+ code 73 (Quincena-25, MH-package authority 2026-01; §C prints the v16 catalog as of the 61_ v9 print — 73 arrives with the v17-era F-14/F-910 revision; F-910 v10 watch kin)". FR-178 (R=12): add clause "the Quincena code-73 surface is excluded (no retention happened — FR-212)".
- [ ] **Step 5: §4 + §5 + §6 + §7.** DM: catalog row note (73 dated row); f910.row: `code_73` handled as catalog row + auto flag. §5: map FR-212. AC: *given the Task-4 fixture (10 subjects, US$5,000.00 presented in January 2027), the F-910 §C renders a code-73 row NO GRAVADOS with US$5,000.00, zero retained tax, and the R=12 surface is untouched* (FR-212). §7 OQ: *73 in the F-14 apéndice v17 unverified — no v17 manual (SOQ-09 doc-completeness residue); re-check at the v17 manual / F-910 v10 acquisition (≥71 watch)*.
- [ ] **Step 6: Verify.** `~/.venvs/localizations/bin/python -c "import csv; rows=list(csv.reader(open('sv/requirements/fiscal-reporting/f14_income_codes.csv'))); print(len(rows), rows[-1][:3])"` → 49 data rows + header, last row starts `73,...`; CSV eol=lf respected (`git diff` shows no CRLF).
- [ ] **Step 7: Commit.** `git commit -m "S6 fold-in: frep/07 F-910 code 73 + catalog row (FR-212)"` (with add, including CSV).

### Task 6: taxation — renta no gravada + 2026 credit/certificado + gasto deducible (FR-173..175)

**Files:**
- Modify: `sv/requirements/taxation/01_isr-framework.md` (§2 LB, §3.1 FR-173 after FR-005, §3.5 FR-174 after FR-033, §4, §5, §6, §7)
- Modify: `sv/requirements/taxation/02_isr-deductions.md` (§2 LB, §3 FR-175 placement per its section logic — gasto-deductions territory, §4, §5, §6, §7)
- Modify: `sv/requirements/taxation/00_index.md` (cross-refs block)

**Interfaces:**
- Consumes: EVID-236/237 (66_ Arts. 4/6/8; 67_ §§3-4 + Anexos 1/7/8), `SV-PAY-FR-137/142` (worker-side feed), `SV-FREP-FR-211/212` (reporting chain tail).
- Produces: `SV-TAX-FR-173` (renta no gravada — ISR-side rule), `SV-TAX-FR-174` (FY-2026 employer credit + remanent + ZF/DPA/LSI certificado + tercerización + F-11 v19 casilla-319 feed key), `SV-TAX-FR-175` (gasto deducible + double-benefit OQ + IVA-pointer OQ). The certificado is the future special-regimes wave's consumer anchor (cited).

- [ ] **Step 1: Read evidence + files.** EVID-236/237/238; `01_isr-framework.md` §3.1/§3.5 + `02_isr-deductions.md` end-to-end (place FR-175 in the deductions-costs section matching its structure — likely the "otros gastos deducibles"/requirements-driven zone; follow the file's own section logic).
- [ ] **Step 2: 01 §2 LBs.** Add THREE LB rows (66_ source, verbatim from evidence): Art. 4 (rentas no gravables + no retention + inembargable + gasto deducible), Art. 6 transitory (2026 credit full quote: "crédito tributario acreditable contra el pago del Impuesto sobre la Renta del ejercicio fiscal dos mil veintiséis, por el monto total pagado" + remanent + tercerización + ZF/DPA/LSI certificado + "no representa la aplicación de un régimen especial tributario"), Art. 8 (special + public-order law prevailing). Plus one 67_ LB: §§3-4 (credit documentation: planilla en original + suscripción; Anexo 7 checkbox; Anexo 1 F-11 v19 casilla 319 inside the casilla-330 subtraction; Anexo 8 v20).
- [ ] **Step 3: FR-173 (01 §3.1).** "The system shall classify amounts received by workers as Quincena-25 as *rentas no gravadas* excluded from the renta computation per D.L. 499 Art. 4 — a special-law declaration that prevails over contrary norms per its Art. 8 (public-order), operating alongside (not amending) the Ley ISR Art. 4 exemption list; consequently the amounts never enter the retention base (the SV-PAX-FR-104 exclusion input is fed by SV-PAY-FR-137), never appear in the annual liquidation renta, and surface only as no-gravado reporting (F-910 code 73 / renta-en-línea 724-kin — SV-FREP-FR-212)." (fix the SV-PAX typo → SV-TAX-FR-104 when writing)
- [ ] **Step 4: FR-174 (01 §3.5).** "The system shall maintain, for FY-2026 only, the employer Quincena-25 tax CREDIT ledger: employers who paid the (voluntary private / mandatory public) Quincena-25 record a credit of 100% of amounts actually paid, creditable against the FY-2026 ISR payment; a remanent after crediting is applicable to OTHER substantive ISR obligations; tercerización contractors that paid the full amount record the same credit (with the separate documento fiscal to the contratante + planilla copy — 66_ Art. 6); ZF/DPA/LSI users route the excess to the transferable Certificado de Crédito Tributario issued by MH (auto-generated at the FY-2026 declaration presentation; 'no representa la aplicación de un régimen especial tributario' — special-regimes wave consumes this by id); the credit's declaration surface is F-11 v19 casilla 319 'Crédito Tributario Quincena Veinticinco' inside the casilla-330 IMPUESTO DETERMINADO subtraction (v19/v20 prints = acquisition candidates ≥71; layout builder future); documentation = original signed planilla + the F-14 annex (67_ §4); the renta-en-línea ZF/DPA/LSI checkbox routes certificado seekers (67_ Anexo 7). Dated regime: valid for ejercicio 2026 payments only (no continuation in 2027+ — the credit is Art. 6 transitory)." (LB Art. 6; LB 67_; EVID-237/238)
- [ ] **Step 5: FR-175 (02).** "The system shall treat employer Quincena-25 payments as *gasto deducible* per D.L. 499 Art. 4, conditioned on ACTUAL payment and documentation conforme a la Ley ISR — operationally the original signed planilla + the F-14 January annex (67_ §4; the deduction and the FY-2026 credit of SV-TAX-FR-174 coexist per the law's cumulative text — OQ double-benefit); the tercerización IVA-side treatment (FCF con valor exento; no Ley IVA Art. 66 pro-rata) is recorded as an IVA-wave pointer (IVA-core files owed — OQ)." Add §2 LBs to 02 (Art. 4 gasto clause + 67_ §4 documentation; may reference 01's LBs by id per file conventions if the file prefers cross-LB refs — follow 02's own pattern).
- [ ] **Step 6: 01/02 §4-§7.** DM (01): `l10n_sv.tax.quincena.credit (new)` — `ejercicio` (2026), `amount_paid`, `credit_amount` (=100%), `applied_against`, `remanent`, `route` select `isr_payment · other_isr_obligations · certificado_zf_dpa_lsi`, `certificado_ref`. ACs (01, continue numbering): *employer paid US$5,000.00 voluntarily in Jan-2026 with FY-2026 ISR payable US$4,000.00 → credit 5,000.00 applies 4,000.00, remanent 1,000.00 routed to other ISR obligations*; *ZF user with excess → certificado route + entitlement recorded (issuance = MH external)*; *F-11 v19 feed: casilla 319 = 5,000.00 inside the 330 subtraction; casillas 630-648 still never fed (R21 extends to v19)*. AC (02): *paid + documented → deductible; unpaid accrual → no deduction until paid.* OQs: (a) double benefit 2026 (deduction+credit simultaneously — law cumulative, no MH contra; encode both, flag for fiscalización criteria) (open); (b) F-11 v19/v20 acquisition ≥71 (open, sources-watch); (c) IVA tercerización FCF-exento + Art.-66 pro-rata exemption → IVA-core wave pointer (open, deferred-by-design).
- [ ] **Step 7: taxation/00_index.md.** Add cross-ref block: S6 Quincena-25 — FR-173..175; feed chain payroll/08 FR-137/142/143 → frep/06+07 FR-209..212 → taxation FR-173/174; F-11 v19/v20 acquisition watch; special-regimes certificado consumer note.
- [ ] **Step 8: Verify.** `grep -o "SV-TAX-FR-17[0-9]" sv/requirements/taxation/*.md | sort -u` → 173/174/175 defined once each; every new FR cites an LB; 00_index mentions all three.
- [ ] **Step 9: Commit.** `git commit -m "S6 fold-in: taxation quincena-25 renta no gravada + 2026 credit + deduction (FR-173..175)"` (with add).

### Task 7: indexes, COVERAGE, master index, special-regimes stub

**Files:**
- Modify: `sv/requirements/payroll/00_index.md`, `sv/requirements/fiscal-reporting/00_index.md`, `sv/requirements/COVERAGE.md`, `sv/.extractions/00_MASTER_INDEX.md`
- Create: `sv/requirements/special-regimes/00_index.md` (wave-prep stub)
- Possibly modify: `sv/README.md` (only if it states per-wave FR totals)

**Interfaces:**
- Consumes: all prior tasks' FR ids + the W11 state already recorded in the indexes.
- Produces: consistent corpus-level state (totals, OQ statuses, coverage flips, master-index cluster closures).

- [ ] **Step 1: payroll/00_index.md.** Update: file 04 row (FR-044..062 → FR-044..062 + FR-138..141), file 08 row (+FR-142/143, FR-137 rewritten), totals block (137 → **143** payroll FRs), evidence note (law folded), OQ-002 → resolved-acquisition.
- [ ] **Step 2: fiscal-reporting/00_index.md.** Update: 06 row (FR-137..170 → +FR-209..211; FR-166/167 amended), 07 row (FR-171..194 → +FR-212), totals 208 → **212**, SOQ-09 pointer sentence → "resolved in-corpus: FR-209..212" (keep the doc-completeness residue note: v17 manual still absent).
- [ ] **Step 3: taxation/00_index.md totals.** 172 → **175** + S6 note (done in Task 6 Step 7 — verify only; edit here if missed).
- [ ] **Step 4: COVERAGE.md.** Flip rows 66_..70_ from `pending-S2+` to `cited-as-LB` with destinations: 66_ → payroll/04+08, taxation/01+02 (law LBs); 67_ → fiscal-reporting/06+07, taxation/01 (guía LBs incl. F-11 v19/v20 discovery); 68_ → fiscal-reporting/06+07 (upload-flow); 69_ → fiscal-reporting/06 (CSV spec); 70_ → fiscal-reporting/06 (delimiter). Update the totals row (pending 5 → 0 for these; recount cited).
- [ ] **Step 5: master index.** F10 cluster: append resolution note (annex representation = separate January-only 7-col `;` CSV per 69_/70_; SOQ-09 resolved W11; FR-209..212 own the engine; the v16-annex-new-code working assumption WITHDRAWN). P10: append "folded S6 (FR-138..143 payroll; 173..175 taxation)". Section B log: new entry "S6 Quincena-25 fold-in (2026-08-18): FR numbering + in-file rulings carried (724 operative/734 [sic]; `;` delimiter; durable January window; Art. 3 [sic])". SOQ-09 row already resolved — verify wording still accurate (amend "FR fold-ins queued" → "folded S6").
- [ ] **Step 6: special-regimes/00_index.md stub.** Create: title + status stub table (Country sv / Topic special-regimes / Status pre-wave (no requirement files yet) / Updated 2026-08-18); purpose = wave-prep anchor: lists the wave's input inventory (12_/13_/14_/17b_/42_/43_, D.L. 598-2020 + EVID-167 tail laws per HANDOVER §8.5b) + the W11 discoveries that feed it (ZF/DPA/LSI Certificado de Crédito Tributario from D.L. 499 Art. 6 — consumer of SV-TAX-FR-174; F-11 v20 "Sujetos con Régimen Especial" + certificado anexo — 67_ Anexo 8) with by-id pointers; explicitly NOT a requirements file (no FRs).
- [ ] **Step 7: README check.** `grep -n "137\|208\|172\|FRs" sv/README.md` — update per-wave FR totals if stated; source counts (68 files) unchanged — verify no accidental change.
- [ ] **Step 8: Verify all.** Cross-ref resolution sweep: for every NEW id (`SV-PAY-FR-138..143`, `SV-FREP-FR-209..212`, `SV-TAX-FR-173..175`) `grep -rl "<id>" sv/requirements/` and confirm each id is (a) defined exactly once and (b) every mention resolves to that definition. Totals arithmetic: payroll 143 = 10+13+20+19+23+15+20+(17→20 FRs in 08: FR-121..137 + 142..143)... recompute from the index tables and make the stated totals match the tables (the index is authoritative; if my arithmetic here is off, fix the index text not the files).
- [ ] **Step 9: Commit.** `git commit -m "S6 fold-in: indexes, coverage flips, master-index closures, special-regimes stub"` (with add).

### Task 8: Whole-wave review + fix wave + close (controller-executed)

- [ ] Fresh reviewer subagent over the whole diff (`git diff 4da5a78..HEAD`): every FR/LB/AC/OQ against the evidence file; numbering contract; in-file rulings carried; no evidence paraphrase in LBs; cross-refs resolve; SOQ-11 no-value-restatement discipline; template integrity.
- [ ] One fix wave for findings; re-verify.
- [ ] Update `HANDOVER.md` (§3 S6 section, §5 rulings if any new, §8 next actions: strike the fold-in item, keep F-11 v19/v20 ≥71 watch + S5-ready), commit, push.

---

## Self-Review (done at plan time)

- **Spec coverage:** EVID-236 → Tasks 1/2/3/6 (benefit + invariants + fiscal worker-side). EVID-237 → Task 6 (credit/deduction/certificado/tercerización-IVA-pointer). EVID-238 → Tasks 3/4/5/6 (reporting chain + v19/v20). EVID-239 → Tasks 3/4 (CSV contract + window). All five OQs from the evidence file: OQ-1 → Task 2 §7; OQ-2 → Task 4 (in-row + AC note); OQ-3 → Task 3 LB row; OQ-4 → Task 6 OQ; OQ-5 → Tasks 3/5/6 OQs. HANDOVER §8.5(a) fold-in list fully mapped (special-regimes = Task 7 stub + Task 6 consumer pointer).
- **Numbering:** pinned contract, no collisions (PAY 138..143 with 137 rewritten in place; FREP 209..212; TAX 173..175 — all continue existing maxima).
- **Type consistency:** ledger entity named `l10n_sv.pay.quincena.feed` in Tasks 3/4 (07 consumes via FR id, no model restatement); upload entity `l10n_sv.f14.quincena.upload` only in Task 4.
- **Placeholders:** none — every step carries content or exact verification commands.
