# W24 — spe/taxation Fold-in Wave (107_/108_ D.L. 201/411-2025 + SOQ-40/OQ-2 ride) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fold the two W22 SOQ-41 residual instruments into the requirements corpus: (a) **107_ D.L. 201-2025** (Aeropuerto del Pacífico capital-gains exoneración — CEPA/MOPT perimeter sellers, efectos from 8-may-2022) → spe/01 identity row + taxation/03 operative exemption; (b) **108_ D.L. 411-2025** (energía eléctrica acceso-universal contractor package — IVA exención total, Art. 66 pro-rata exception for local suppliers, ISR Art. 4.1 rentas no gravables, registros especiales, CEL-seller ganancia-de-capital exemption + no-formulario, CNR arancel exoneration) → spe/01 class-row amendment + spe/02 package family + taxation/01/03/08/11 operative rows; plus (c) the **SOQ-40/OQ-2 ride** (taxation/09 D1-tributo mapping design confirmation — unblocked since W20). Index/COVERAGE regen + wave bookkeeping close the wave.

**Architecture:** Edit wave per the standing synthesis conventions (sv/HANDOVER.md §9): sequential per-task dispatches (fresh implementer + reviewer each, fix rounds, SDD ledger) → final whole-wave review → ONE fix wave → bookkeeping → push `sv-research`. Work happens ONLY in `.worktrees/sv` (branch `sv-research`). No new source acquisitions; registry UNCHANGED (numbering stays next=115). W23's cml deferred-minor rides do NOT ride this wave (different topic dir).

**Tech Stack:** Markdown requirements files (Takumi contract: §1 scope, §2 Legal-basis LB table with verbatim Spanish + gloss + locator, §3 FRs, §4 data model, §5 Odoo mapping, §6 acceptance criteria, §7 OQ table), master index, COVERAGE regen script `shared/scripts/build_coverage.py`.

**Spec:** `sv/HANDOVER.md` §5 W22 wave log + §8.1(b)/(c) (the fold-in debt register); `sv/.extractions/00_MASTER_INDEX.md` (SOQ-41 residual verdict, SOQ-40 row, SR1/SR2 + V2/V5 cluster rows); `sv/.extractions/107_108_Aeropuerto_Energia.evidence.md` (EVID-405/406 + file OQ-1); `shared/docs/requirements-extraction-procedure.md`.

## Global Constraints (binding on every task)

- **Every FR cites an LB row** in its own file's §2 (by LB id); statutory verbatim quoted from the instrument txt with `[sic]` markers where the print is defective. Both prints are native text layers (asamblea server); intra-word spacing artifacts cleaned ONLY per the EV header discipline (107_: "CE PA"→"CEPA", "e mitir"→"emitir"; 108_: "soci ales"→"sociales", "públic o"-class splits) — no wording altered. **Quote-tail self-checks are mandatory** (W23 ruling (e)): compare the final 5+ words of every quote against the txt.
- **By-ID sibling consumption, never restatement:** the ISR no-gravables chassis = `SV-TAX-FR-173` (taxation/01) extended, not re-derived; the Art. 66 engine = taxation/11 FR-269 zone; the Quincena-25 no-proporcionalidad chassis = `SV-TAX-FR-277`; the exemption-schedule chassis = spe/02 FR-023/FR-202/203; the project-incentive class = spe/01 FR-200; días-hábiles arithmetic = SV-FREP-FR-202..204 by id; CT Art. 147 conservation + books machinery = taxation/16 by id; CT Art. 260 abuso revocation = spe/01 FR-015 state-family + 95_/97_ own-cause pattern (never merged with ZF/LSI ladders).
- **Numbering (R30(b)):** new FRs continue the ONE prefix per topic dir contiguously — spe from **204**, taxation from **417**. Allocation: T1 = **SV-SPE-FR-204** (spe/02; FR-200 amended IN PLACE, no new id); T2 = **SV-TAX-FR-417** (taxation/01) + **SV-TAX-FR-418..419** (taxation/03); T3 = **SV-TAX-FR-420** (taxation/08; FR-224 amended in place) + **SV-TAX-FR-421** (taxation/11); T4 mints NO FRs (OQ resolution only). **Total: +6 FRs → corpus 1,724 → 1,730.** Per-task review gates verify the plan's allocations against the delivered files (W23 ruling (d) lesson).
- **D15 doctrine:** every dated row carries instrument provenance. 107_ window = efectos retrotraídos al **8-may-2022** per Art. 35 as printed (the [as printed] note: one day after the base law's own 29-abr-2022+8d vigencia — no operative ambiguity, EVID-405 doubt recorded in the LB gloss, NOT an OQ); vigencia 30-ene-2025 + 8 días = 7-feb-2025. 108_ windows = decree vigencia **26-sep-2025 + 1 day → 26-sep-2031** (six years, Art. 13) AND the per-benefit event window **firma de contratos → recepción final / fin de la relación contractual con CEL** (Art. 4-II) — two layers, never collapsed.
- **Value-discipline / config-gaps ship NO defaults:** the airport Art. 2 perimeter geometry (base law D.L. 361-2022 UN-ACQUIRED — only the reform is in corpus); the DGII escrito/resolución format (Art. 5; delegated practice); MH Art. 12 directrices (acuerdos/instructivos/circulares); the documental presentation of 108_-exempt operations (no corpus guidance — OQ, never invented); microempresario-class kin gates stay config-gaps.
- **Awareness-only surfaces (no FR mechanics invented):** the airport base law's OTHER Capítulo IV exonerations (CEPA/MOPT/companies — out-of-corpus) = gloss note only; 108_ Art. 9 (deber de colaboración) + Art. 10 (red-connection) = authority-side gloss only; the 107_ formulario question rides the existing taxation/03 OQ-006 forms config-gap (no new OQ).
- **Art. 174 reconciliation (T3, recorded working reading):** taxation/08 FR-224's two-channel gate (Ley letters + ratified instruments) is AMENDED to add the third channel: exemptions anchored to a REGISTERED specific special-law instrument with express especialidad + vigencia (the 108_ class: named program, enumerated Art. 1 operations, beneficiary-bounded, Art. 11 "carácter especial y priman sobre cualquier ley especial o general que las contradiga", CT Art. 6-b exoneración power recital) — config-gated per instrument, NEVER a user-defined generic claim (the gate's rejection limb stands). Working reading recorded in the FR-224 amendment note + LB gloss; 97_ (LB-023 spe/02) is the in-corpus precedent. No new OQ.
- **Corpus count discipline:** the ONLY FR additions are FR-204 (T1) and FR-417..421 (T2/T3) — 6 new FRs → corpus 1,730. FR-200/FR-224 are in-place amendments (ids unchanged). T4/T5 mint NO FRs.
- **Commits:** short imperative, no emojis, one per task (+ plan commit + fix-wave commits). Push only at wave close (S9 ruling (c)).
- **Extraction txts are worktree-local** (`sv/.extractions/*.pdf.txt`) — implementers/reviewers read them there (S8 ruling (a)).
- **Dispatch template (S8 ruling (c), binding):** scoped evidence — the task's EVID ids + the two small instrument txts (whole) + ONE exemplar + target-file line windows; on-demand additional txt via grep + bounded window. Harness exposes no per-subagent model parameter (S7 ruling (d)).
- **SDD ledger:** `.superpowers/sdd/2026-08-24-w24-spe-taxation-foldin/` — per-task implementer reports, reviewer verdicts, fix rounds, rulings. Before ANY workspace deletion, preserve rulings into `sv/HANDOVER.md` §5 (W19 ruling (b)).
- **Reviewer gates:** every task gets a fresh reviewer vs the master index + the EV bank + the instrument txts; fix rounds until Approved (0 Critical/Important). Controller commits died-mid-task COMPLETE work UNMODIFIED after structure verification (S7 ruling (a)); re-dispatches zero-state deaths clean (S7 ruling (c)). **Rollup prose derives from the matrix** (W22/W23 ruling — no hand-computed counts in prose).

---

## Pre-loop prep (controller, before Task 1 dispatch)

- [ ] **P-1:** External-check sweep recorded (done 2026-08-24, controller-direct): factura.gob.sv 200 (alive); asamblea.gob.sv 200 (`-k` route stands); uif.gob.sv **403 WAF-blocked** (HTTP layer back — improvement vs the DNS-absent state; AML reglamento re-probe stands, watch deadline 2026-10-17); **D.O. still unreachable (000/NXDOMAIN — outage since 2026-08-22 continues)**. No drift on pinned recipes; results land in HANDOVER §6 at bookkeeping. No acquisition actions unblocked.
- [ ] **P-2: Commit plan** — `git add docs/superpowers/plans/2026-08-24-w24-spe-taxation-foldin.md && git commit -m "W24 plan: spe/taxation fold-in (107_/108_) + SOQ-40/OQ-2 ride"`.

---

## Task 1: spe side — spe/01 FR-200 amendment + 107_/108_ identity LBs; spe/02 FR-204 package family

**Files:**
- Modify: `sv/requirements/special-regimes/01_regime-framework.md` (§2 LB table + §3.11 FR-200 amendment + §4 dl_incentive rows; NO new FR id in this file)
- Modify: `sv/requirements/special-regimes/02_zf-exemption-schedules.md` (§2 new LB + §3.12 new FR-204 + §4 exemption-row rows + §6 ACs + §7 OQ)

**Interfaces:**
- Consumes (BY ID): SV-SPE-FR-200 (class row — amended here); FR-015 benefit-state family (own-cause CT-260 revocation); spe/02 FR-023 chassis; SV-FREP-FR-202..204 (días-hábiles engine); taxation/16 CT-147 conservation by id; SV-TAX-FR-173 chassis (taxation/01 — the no-gravables stamp T2 mints FR-417 on); Ley ISR Art. 4.1 = 54_ by id.
- Produces: `SV-SPE-FR-204`; the amended FR-200 instrument catalog (dl411_2025 values consumed by T2/T3 pointers); spe/01 LB-034 (108_ identity) + LB-035 (107_ identity); spe/02 LB-024 (the 108_ schedule verbatim) + OQ-10.

**Evidence inputs (scoped, per dispatch template):**
- EV bank: `sv/.extractions/107_108_Aeropuerto_Energia.evidence.md` (29 lines — read WHOLE: EVID-405/406 verbatim + gloss + file OQ-1).
- Primary txts (both small — read WHOLE): `sv/.extractions/107_Reforma_AeropuertoPacifico_DL201_2025_Asamblea.pdf.txt` (117 lines) + `sv/.extractions/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf.txt` (287 lines).
- Exemplar (ONE): spe/02 §3.12 (lines 463-532 — the FR-202/203 per-instrument family shape) + spe/01 §3.11/§4 W19-T4 rows (lines 529-646) as the in-file anchor shapes.
- Kin corpus rows (read-only): spe/02 LB-022/LB-023 (lines 122-123); spe/01 LB-030..LB-033 (lines 155-158).

**spe/01 edits:**
- §2 preamble (lines ~40-45): the project-incentive class sentence gains 108_ as a member (instrument dl411_2025, D.O. 181 T.448 26-sep-2025, vigencia 27-sep-2025 → 26-sep-2031, CURRENT — not project-spent like 97_).
- **New LB-034** (108_ identity/instrument row — kin LB-030/031 shape): source `sv/sources/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf`. Verbatim spine: Art. 1 objeto (program scope, "hasta la completa recepción de las obras, bienes y servicios adquiridos localmente o en el extranjero"); Art. 5 (escrito a la DGII informing the contrataciones + vinculación proof; resolución ≤10 días hábiles counted from the day following reception; prevenciones or beneficiario declaration); Art. 11 ("Las presentes disposiciones tienen carácter especial y priman sobre cualquier ley especial o general que las contradiga."); Art. 12 (MH facultades — acuerdos/instructivos/circulares); Art. 13 (seis años from the day after D.O. publication). Gloss: BID-financed, CEL-executed rural-electrification program (≈8,756 hogares per considerando V); CT Art. 6-b exoneración power (considerando VI); the admission mechanics = config-family inputs; Art. 12 delegation = config-gap class (kin 96_ Art. 16).
- **New LB-035** (107_ identity row — kin LB-033 historical-note shape but CURRENT): source `sv/sources/107_Reforma_AeropuertoPacifico_DL201_2025_Asamblea.pdf`. Verbatim spine: considerandos V/VI (the ganancia-de-capital social-purpose recitals); Art. 3 vigencia (8 días post-publication); the base-law frame (D.L. 361-2022, D.O. 81 T.435 29-abr-2022 per considerando I — UN-ACQUIRED; Capítulo IV's other exonerations out-of-corpus, gloss only). Gloss: the corpus encodes ONLY the Art. 29.1.e seller limb (the operative FR = SV-TAX-FR-418, taxation/03 by id) + the Art. 35 retro-efectos window; the Art. 2 perimeter geometry = external config (no default).
- **§3.11 FR-200 amendment (in place):** the class enumeration gains the 108_ member: admission = per-instrument (dl411_2025: **dgii_escrito_vinculacion** — Art. 5 escrito + resolución ≤10 días hábiles; NOT the 95_ ≥30-day prior notice); window = TWO layers (decree vigencia 27-sep-2025 → 26-sep-2031 fixed; per-benefit event window firma→recepción/fin-relación per Art. 4-II — the 97_ event_bounded_recepción kind, now inside a still-open decree vigencia); especialidad prevalence flag = Art. 11. Dated exemption rows consumed from `02` (FR-204 by id); ISR/IVA-side effects route to taxation (FR-417/419/420/421 by id — added as pointer sentences ONLY, no restatement).
- **§4 dl_incentive rows:** instrument catalog + `dl411_2025` (select value); admission_kind `dgii_escrito_vinculacion`; window_kind `event_bounded_recepcion_within_6y_vigencia` (discriminated, never normalized); vigencia 27-sep-2025 + valid_to 26-sep-2031 + provenance 108_ Art. 13; per-contract vinculación link (the FR-204 registro hook).

**spe/02 edits:**
- **New LB-024** (the 108_ schedule verbatim — kin LB-023 shape): source 108_. Verbatim: Art. 2 literals a)/b)/c) IN FULL (incl. the no-cascade sentence and the **final paragraph — proveedores locales / Art. 66 proporcionalidad relief**); Art. 3 (rentas no gravables, Art. 4.1 basis, "hasta la completa recepción"); Art. 4 (prohibición: personal-consumption/personal-use goods of directivos/socios/personal/familiares/empresas relacionadas + activo corriente; the Art. 4-II window sentence; the Art. 4-III abuso limb: CT Art. 260 revocation + determine-and-liquidate from the ejercicio of the abuso determination); Art. 6 (registros especiales: compras/ventas/servicios per contract across the enumerated program stages; vinculación annotation; CT Art. 147 conservation; declaraciones tributarias y aduaneras duty); Art. 7 (propietarios O POSEEDORES selling voluntarily to CEL — ISR ganancia-de-capital exemption + the express no-formulario sentence); Art. 8 (CNR arancel exoneration for inscribable acts in program execution). Gloss per EVID-406.
- **NEW §3.13 "W24 fold-in — 108_ per-instrument exemption-row family" — FR-204** (ONE comprehensive FR on the FR-203 chassis; implementer mints the shall-statement, citing LB-024):
  - instrument dl411_2025 keyed to FR-200; beneficiaries = contratistas/subcontratistas (personas naturales o jurídicas), DGII-resolución-gated (Art. 5, ≤10 días hábiles — config-gap: resolución/escrito format NOT in corpus, no default; EV file OQ-1);
  - exemption rows: a) IVA exención total on Art. 1-enumerated transfers/services (operative IVA registry = **SV-TAX-FR-420, taxation/08 by id**); b) import/internación impuestos y gravámenes + DAI + IVA total exención, expressly NON-extensive to any other subject of the import operation (no-cascade flag); c) licencias/permisos tributos exención (non-IVA regulatory surface — awareness limb inside the row);
  - ISR side: contractor ingresos = renta NO GRAVADA per Ley ISR Art. 4.1 until completa recepción (operative stamp = **SV-TAX-FR-417, taxation/01 by id**); the no-retention consequence flows from no-gravada status per the 97_ OQ-9 working reading (cite spe/02 OQ-9 as kin — 108_ prints no express retention clause either);
  - window rows: per-benefit firma→recepción-final/fin-relación-CEL (Art. 4-II) inside decree vigencia 27-sep-2025→26-sep-2031 (Art. 13) — D15 dated rows, both layers carried;
  - carve-out flags: personal-consumption/personal-use + activo corriente (Art. 4-I);
  - compliance: registros especiales per contract + vinculación annotation + CT 147 conservation (taxation/16 by id) + declaraciones duty (Art. 6) — bookkeeping-segregation flag kin FR-203/FR-197;
  - abuso state: CT Art. 260 revocation of the granting resolución + liquidation of tributos from the ejercicio of determination (Art. 4-III) — own-cause state-reason row on the FR-015 family (95_/97_ pattern), never merged with ZF/LSI ladders;
  - CEL-seller limb: propietarios o poseedores voluntary sellers → ganancia-de-capital exemption + express no-formulario (operative = **SV-TAX-FR-419, taxation/03 by id**); CNR arancel exoneration (Art. 8) = dated row;
  - proveedores-locales pro-rata relief = **SV-TAX-FR-421, taxation/11 by id** (pointer only, never restated).
- **§4 exemption-row rows:** extend the FR-202/203 chassis table with dl411_2025 rows (tax_kind iva · import_dai_iva · licencias_tributos · isr_no_gravada_until_recepcion · isr_gain_cel_seller · cnr_arancel; window_kind event_bounded_recepcion_within_vigencia; non_cascade on import rows; exclusion_flags personal_consumption/activo_corriente; contract-vinculación registro link).
- **§6:** ADD ~3 ACs: (a) a DGII-resolución-gated contractor's program purchase imports at $0 DAI/IVA with the no-cascade flag blocking extension to the freight forwarder; (b) a personal-use good acquired under the program → exemption blocked (Art. 4-I); (c) post-recepción operation → exemption rows expired by the event window even inside decree vigencia.
- **§7:** ADD **OQ-10** — 108_ operative-format config-gap: the DGII escrito/resolución format (Art. 5), the MH Art. 12 directrices, and the documental presentation of 108_-exempt operations (DTE exento emission kin the 67_ guía pattern — no corpus instrument) ship NO defaults; config slots only. (EV file OQ-1 rides here.)

**Review gate:** fresh reviewer verifies vs EVID-405/406 + both txts: verbatim fidelity INCL. QUOTE TAILS; the Art. 2 final paragraph (pro-rata relief) quoted in LB-024; two-layer windows; by-id discipline (no taxation restatement); FR-200 amended in place (no new spe/01 id); FR-204 contiguity (spe tail 203→204); config-gap discipline (no invented formats).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W24 T1: spe fold-in — FR-200 amendment + LB-034/035 identity rows (spe/01), FR-204 package family + LB-024 + OQ-10 (spe/02) — 107_/108_"`

---

## Task 2: taxation ISR side — taxation/01 FR-417 (no-gravables chassis) + taxation/03 FR-418..419 (ganancia-de-capital exonerations)

**Files:**
- Modify: `sv/requirements/taxation/01_isr-framework.md` (§2 new LB row; §3 new FR-417 at the Quincena-25-zone tail; §4 isr_no_renta_rule row; §5 FR row; §6 AC)
- Modify: `sv/requirements/taxation/03_isr-rates-gains.md` (§2 new LB rows; §3.2 new FR-418..419 at the section tail; §4/§5 rows; §6 ACs; §7 no new OQ)

**Interfaces:**
- Consumes (BY ID): SV-TAX-FR-173 + the isr_no_renta_rule chassis (taxation/01); FR-082/FR-086 (gain track + loss ledger, taxation/03); LB-006/007 (Arts. 14/42); SV-SPE-FR-204 (the package family — vinculación/window inputs, by id); OQ-006 (taxation/03 forms config-gap — rides, no new OQ); spe/02 OQ-9 working reading (no-retention flows from no-gravada).
- Produces: `SV-TAX-FR-417` (the program-income no-gravable stamp — consumed by spe/02 FR-204 by id); `SV-TAX-FR-418` (107_ airport-perimeter exoneración) + `SV-TAX-FR-419` (108_ CEL-seller exoneración + no-formulario).

**Evidence inputs:**
- EV bank + txts: same as Task 1 (whole files).
- Exemplar (ONE): taxation/01 FR-173 zone (lines ~130-150 + §4 line 385 + §5 line 468) for the no-gravables shape; taxation/03 §3.2 (lines 140-218) as the in-file anchor zone.
- Kin corpus rows (read-only): taxation/03 LB-006/LB-007 (Art. 14/42, lines 71-72) + OQ-001/OQ-006 (lines 608/613).

**taxation/01 edits:**
- §2: **new LB row (after LB-036)** — 108_ Art. 3 verbatim ("Los ingresos que perciban las personas naturales o jurídicas, involucradas como contratistas o subcontratistas respecto de las actividades relacionadas con el Programa…, se considerarán como no gravables para los efectos de lo dispuesto en el artículo 4 numeral 1 de la Ley de Impuesto sobre la Renta, hasta la completa recepción de las obras, bienes y servicios adquiridos." — quote from txt lines 129-133 with the EV-declared intra-word cleaning) + gloss (kin LB-032 Quincena-25: a special-law renta-no-gravable declaration operating ALONGSIDE, not amending, the Ley ISR Art. 4 list; window = until completa recepción, event-bounded per contract vinculación — SV-SPE-FR-204 by id).
- §3 (Quincena-25 zone tail): **FR-417** — the isr_no_renta_rule classification extends to program incomes: contractor/subcontractor ingresos from 108_-enumerated activities flagged `programa_energia_dl411_art3` (renta NO GRAVADA by special law) for operations inside the per-contract event window; never in the retention base nor the annual liquidation renta (FR-173 chassis); no-retention consequence per the 97_/spe-02-OQ-9 working reading (no express retention clause printed); reporting surfaces consume by id (no-gravado reporting kin the FR-173 note).
- §4: isr_no_renta_rule catalog row gains the value; §5: FR-417 row; §6: one AC (program-contract income flagged → excluded from retention base and liquidation; post-recepción income → flag off).

**taxation/03 edits:**
- §2: **two new LB rows (after LB-019)**:
  - **LB (107_)** — Art. 1 verbatim (the new Art. 29.1.e text: "Exonérase del pago del Impuesto a la Ganancia de Capital, a que se refieren los artículos 14 y 42 de la Ley de Impuesto sobre la Renta, a los propietarios de los inmuebles que los vendan a CEPA y/o al MOPT, siempre que estos inmuebles estén comprendidos dentro del perímetro de delimitación a que se refiere el artículo 2 de la presente Ley.") + Art. 2 verbatim (the new Art. 35: efectos retrotraídos al 8-may-2022 + especial-y-pública prevalence) + Art. 3 vigencia. Gloss: exoneración of the Art. 42 10% (and the ≤12-month ordinary-renta limb's ganancia component) for perimeter sellers to CEPA/MOPT; efectos window from 8-may-2022 (covers already-executed sales — drafted retroactively); the [as printed] note (8-may vs the base law's own 7-may vigencia — one day after; no operative ambiguity, EVID-405); perimeter = the un-acquired base law's Art. 2 (external config, no default); base law D.L. 361-2022 un-acquired — identity via spe/01 LB-035.
  - **LB (108_ Art. 7)** — verbatim ("Los propietarios o poseedores que vendan voluntariamente sus inmuebles a favor de la Comisión Ejecutiva Hidroeléctrica del Río Lempa (CEL), estarán exentos del pago del Impuesto sobre la Renta que pudiera generar la venta de los mismos en concepto de Ganancia de Capital, en consecuencia, tampoco estarán obligados a presentar por dicha venta el formulario para el cómputo correspondiente a la misma." — txt lines 198-202) + gloss (kin-class: CEL voluntary sellers; class includes POSEEDORES — broader than 107_'s propietarios; express formulario-duty lift).
- §3.2 tail: **FR-418** (107_ exoneration): the gain-track engine (FR-082) shall apply a dated exoneración stamp `aeropuerto_dl201_art29_1e` to disposals of inmuebles sold to CEPA and/or MOPT within the Art. 2 perimeter (perimeter = external config slot, base law un-acquired — NO default geometry), for sales with efectos from **8-may-2022** (Art. 35 retro window; D15 dated rows: window start 8-may-2022, instrument 107_, vigencia 7-feb-2025 forward-looking + retro coverage); stamped disposals produce NO Art. 42 10% liability and NO ganancia entry in the annual liquidation (the Art. 14 determination is not computed for exonerated transfers); no express formulario lift printed — the form surface rides OQ-006 (config-gap). **FR-419** (108_ exoneration): the same chassis stamps `energia_dl411_art7` for voluntary inmueble sales to CEL by propietarios O POSEEDORES (window = decree vigencia 27-sep-2025→26-sep-2031; the benefit's own event limbs per SV-SPE-FR-204 by id); stamped disposals produce no ganancia liability AND the formulario-for-cómputo duty is EXPRESSLY LIFTED (no computation form flag on the disposal record — the express text distinguishes this from FR-418).
- §4/§5: dated exoneración-stamp rows (two instruments, window fields, perimeter/acquirer class discriminators); §6: two ACs (a perimeter sale to CEPA dated 2023 → exonerated retroactively (no tax, correction-path note per D15 original-period discipline); a CEL sale by a poseedor post-27-sep-2025 → exonerated + no-form flag set).

**Review gate:** reviewer verifies verbatim + quote tails against both txts; FR-418/419 contiguity (taxation tail 416→419 after T1 — T2 mints 417..419); the class differences (perímetro/propietarios vs CEL/poseedores); the two window shapes (retro efectos vs decree vigencia); noformulario only in FR-419; by-id discipline.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W24 T2: taxation ISR fold-in — FR-417 no-gravables chassis (01), FR-418..419 ganancia exonerations (03) — 107_/108_"`

---

## Task 3: taxation IVA side — taxation/08 FR-224 amendment + FR-420 (exemption registry); taxation/11 FR-421 (pro-rata exception)

**Files:**
- Modify: `sv/requirements/taxation/08_iva-exemptions.md` (§2 new LB rows; §3.3 FR-224 amendment + new FR-420; §4/§5 rows; §6 ACs; §7 no new OQ)
- Modify: `sv/requirements/taxation/11_iva-pro-rata-remanente.md` (§2 new LB row; §3.2/§3.3 zone new FR-421; §4/§5 rows; §6 AC; §7 no new OQ)

**Interfaces:**
- Consumes (BY ID): FR-224 (the Art. 174 gate — amended here); FR-206/FR-214 (the Art. 45/46 registries — the exemption-row chassis); FR-269 (the Art. 66 engine) + FR-277 (the Quincena-25 no-proporcionalidad chassis); SV-SPE-FR-204 (beneficiary/vinculación/window inputs, by id); spe/02 LB-023 (97_ precedent — read-only kin).
- Produces: `SV-TAX-FR-420` (the 108_ IVA exemption registry + third-channel encoding — consumed by spe/02 FR-204 by id); `SV-TAX-FR-421` (the local-supplier pro-rata exception).

**Evidence inputs:**
- EV bank + txts: same as Task 1 (whole files; 108_ txt lines 95-125 = Art. 2 verbatim zone).
- Exemplar (ONE): taxation/08 §3.3 (lines 363-383) + the file's LB-013/014 rows (lines 120-121); taxation/11 §3.3 FR-277 zone (lines 258-288).
- Kin corpus rows (read-only): spe/02 LB-023 (the 97_ Art. 1-b final paragraph — the identical pro-rata-relief clause, W19 precedent).

**taxation/08 edits:**
- §2: **new LB row (after LB-015)** — 108_ Art. 2 a)/b) verbatim (both literals in full, incl. the no-cascade sentence) + Art. 11 verbatim + gloss: the specific-instrument exemption class (named program, Art. 1-enumerated operations, contratistas/subcontratistas beneficiary class, DGII-gated); the Art. 174 working reading (genéricas ≠ this instrument-bounded grant; Art. 11 express prevalence; CT Art. 6-b power recital; in-corpus precedent = 97_/LB-023 spe/02 — recorded reading, no OQ).
- §3.3: **FR-224 amendment (in place)** — the exemption SOURCE gate gains the THIRD channel: (c) a registered specific special-law instrument (instrument id + D.O. anchor + vigencia + express especialidad clause recorded on the row; beneficiary-and-operation-bounded as printed) — config-gated per instrument, never user-defined; the rejection limb stands for GENERIC foreign-law claims (unchanged); the Art. 174 reconciliation note in-row (working reading per the LB gloss).
- **NEW FR-420** (§3.3 tail or a new §3.4 — implementer follows the file's section shape): the 108_ IVA exemption registry on the FR-206/214 chassis: (a) transfers/services rows — IVA exención total for Art. 1-enumerated operations of DGII-declared beneficiaries (per-contract vinculación + event window per SV-SPE-FR-204 by id; dated rows, instrument dl411_2025); (b) import/internación rows — total exención of impuestos y gravámenes + DAI + IVA on program imports, with the non-cascade guard (the benefit does NOT extend to any other subject of the import operation — no-cascade flag on the row); the exemption reason cites the instrument channel (FR-224-c), never a generic claim.
- §4/§5: instrument-channel fields (instrument_id, do_anchor, vigencia, especialidad flag, non_cascade); §6: ACs (a program transfer by a non-declared supplier → exemption NOT applied; an import with a third-party freight forwarder → no-cascade blocks the extension; a generic "ley especial" free-text exemption reason → rejected per FR-224's rejection limb).

**taxation/11 edits:**
- §2: **new LB row (after LB-008)** — 108_ Art. 2 final paragraph verbatim (txt lines 111-114: "Los proveedores locales que realicen ventas de bienes o prestaciones de servicios a favor de los beneficiarios de las exenciones detalladas no aplicarán la proporcionalidad del crédito fiscal a que se refiere el artículo 66 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios.") + gloss: seller-side (proveedor local) relief, express statutory text (contrast FR-277's guía anchor); kin note — 97_ Art. 1-b prints the identical relief (spe/02 LB-023; project-spent, no separate row).
- §3 (§3.2/§3.3 zone tail): **FR-421** — on sales of goods/services by LOCAL SUPPLIERS to 108_-exemption beneficiaries (per SV-SPE-FR-204's vinculación/window by id), the Art. 66 engine (FR-269) shall NOT apply the proportionality to those operations for the seller (the operation is excluded from the seller's pro-rata base — FR-277 chassis, express-statutory anchor); window follows the beneficiary's exemption window (dated rows, instrument-keyed); the seller's credit on those operations is NOT blocked (the relief is denominator-side, per the printed text — record the reading in-row).
- §4/§5: operation-class exclusion rows (instrument-keyed, window fields); §6: one AC (a local supplier with mixed gravadas/exentas operations selling to a declared beneficiary → that sale's amount leaves the proportionality calculation; credits on it remain creditable per the engine's other rules).

**Review gate:** reviewer verifies verbatim + tails; FR-420/421 contiguity (taxation tail 419→421); FR-224 amended in place with the rejection limb intact; the working-reading notes recorded (not OQs); no invented chain mechanics.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W24 T3: taxation IVA fold-in — FR-224 third-channel amendment + FR-420 (08), FR-421 pro-rata exception (11) — 108_"`

---

## Task 4: SOQ-40/OQ-2 resolution — taxation/09 D1-tributo design confirmation + pointer flips (NO new FRs)

**Files:**
- Modify: `sv/requirements/taxation/09_iva-base-rate.md` (§7 OQ-2 resolution + §3.7 one-line design-confirmation note)
- Modify: `sv/requirements/special-regimes/08_fovial-cotrans.md` (§5 FR-175 row pointer note — one line)
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (SOQ-40 row verdict append — one run)

**Interfaces:**
- Consumes: the owned FOVIAL/COTRANS instruments 86_/87_/88_ (+ 89_/106_ vigencia chain, W19/W21) — verification by direct txt grep; FR-244/245 (the DESIGN rows — stand unchanged).
- Produces: OQ-2 (taxation/09) → **resolved**; SOQ-40 master-index verdict append; spe/08 FR-175 pointer flip.

**Evidence inputs:**
- Txts (grep + bounded windows, per dispatch template): `sv/.extractions/86_Ley_Fondo_Conservacion_Vial_consolidada.pdf.txt`, `sv/.extractions/87_Ley_FOVIAL_DL208_DO_2000-12-18_pp6-24.pdf.txt`, `sv/.extractions/88_Reforma_Ley_FOVIAL_DL597_DO_2001-11-09_p3.pdf.txt`, `sv/.extractions/89_Ley_COTRANS_DL257_DO_2021-12-23_pp5-19.pdf.txt` — search terms: `tributo`, `D1`, `documento tributario`, `factur`, `electrónic`, `línea`, `cadena`, `echo` (pass-through/re-bill vocabulary). Expected finding (per W19 T2's evidence pass): NO DTE/chain prescription exists in any owned instrument — the B2B re-bill chain is 31_-guide (2001) practice vintage only.
- Corpus rows (read-only): taxation/09 §3.7 (lines 452-486) + OQ-2/OQ-3 (lines 679-680); spe/08 FR-175 (lines 402-410 + §5 line 485).

**Edits:**
- taxation/09 §7 **OQ-2 → resolved**: verification record — the FOVIAL/COTRANS instruments owned since W18/W19 (86_/87_/88_/89_, + the 106_ prorroga) print the per-unit contribution and its base exclusions but NO rule mapping the B2B recovery chain onto DTE/tributo lines; the control-account chain (RETENCIÓN-FOVIAL / CUENTAS-POR-COBRAR-FOVIAL re-bill) rests on the 31_ guide (2001, pre-DTE) — therefore **the D1-line-per-operation echo (FR-244) and the COTRANS config-gated rows (FR-245) are CONFIRMED as the product design** (not statutory); standing re-validation trigger = any future MH/DGII chain rule (watch kin SOQ-30 cadence). Status: `resolved (W24; instruments verified — design confirmed)`.
- taxation/09 §3.7: one-line note after FR-245's row: "Design confirmed W24 (OQ-2 resolved): no statutory DTE-chain rule exists in the owned instruments; rows stand as labeled product design, config-gated."
- spe/08 §5 FR-175 row: the "B2B-chain-vs-DTE mapping = SOQ-40 IVA-core pointer" tail → "…pointer — resolved W24 (taxation/09 OQ-2: design confirmed, config-gated)".
- Master index SOQ-40 row: append "**W24 (2026-08-24): OQ-2 RESOLVED — instruments 86_-89_/106_ verified rule-negative; FR-244/245 confirmed as labeled product design (D1-line-per-operation echo, config-gated); re-validation trigger = any future MH/DGII chain rule.**"

**Review gate:** reviewer re-runs the txt greps independently (must reproduce the rule-negative finding); verifies OQ-2 status flip + the three pointer surfaces consistent; NO FR text changes.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W24 T4: SOQ-40/OQ-2 resolved — D1-tributo design confirmation (instruments rule-negative; FR-244/245 stand) + pointer flips"`

---

## Task 5: Topic indexes + master-index rollups + COVERAGE regen

**Files:**
- Modify: `sv/requirements/special-regimes/00_index.md`; `sv/requirements/taxation/00_index.md`; `sv/.extractions/00_MASTER_INDEX.md` (Build note + SR1/SR2/V2/V5/T-cluster rows + SOQ-41 residual verdict append)
- Modify: `sv/requirements/COVERAGE_NOTES.md` (curated refresh for the flipped rows, W20 ruling (d) precedent)
- Regenerate: `sv/requirements/COVERAGE.md` via `python3 shared/scripts/build_coverage.py sv` (gate: `python3 shared/scripts/build_coverage.py sv --check` → no drift)

**Edits:**
- **spe/00_index:** 01 row — FR range unchanged (`+ 200..201` stays) + gloss gains "W24: 108_ class-member amendment (FR-200) + LB-034/035 identity rows (107_/108_)" + LB recount (+2); 02 row — FR range `… + 202..203` → `… + 202..204` + gloss gains "W24: 108_ package family (FR-204)" + LB/OQ recount (+LB-024, +OQ-10); 08 row — gloss note (FR-175 SOQ-40 pointer resolved); totals → **204 FRs** + recounted LB/AC/OQ; numbering note gains the W24 tails (204 in 02); OQ rollup — 02 gains OQ-10.
- **taxation/00_index:** 01 row FR range gains FR-417 + gloss; 03 row gains FR-418..419 + gloss; 08 row gains FR-420 (+FR-224 amendment note) + gloss; 11 row gains FR-421 + gloss; 09 row — OQ-2 resolved note; totals → **421 FRs** + recounted LB/AC/OQ (per-file OQ tables: 09 open −1); numbering note gains the W24 tails (417 in 01; 418-419 in 03; 420 in 08; 421 in 11).
- **Master index:** header Build note — "**W24 fold-in 2026-08-24:** the W22 SOQ-41 residuals consumed — 107_/108_ → spe/01 (FR-200 amendment + identity LBs) + spe/02 (FR-204) + taxation 01/03/08/11 (FR-417..421); SOQ-40/OQ-2 resolved (taxation/09); corpus 1,724 → 1,730."; SR1 + SR2 cluster Covers appends (W24 lines); V2 (exemptions) + V5 (pro-rata) cluster appends; SOQ-41 row — append "**W24: the 107_/108_ FR fold-ins EXECUTED (EVID-405/406 → SV-SPE-FR-204 + SV-TAX-FR-417..421) — residual = the RAEX reglamento config-gap (96_) only.**"; SOQ-40 row append rides T4.
- **COVERAGE:** regen — expected flips: 107_/108_ pending → cited (spe/01+02, taxation/01/03/08/11 LB columns); rollup 88 cited / 14 pending → **90 cited / 14−2=12 pending** of 113 (verify FROM THE SCRIPT OUTPUT — rollup prose derives from the matrix, W22/W23 ruling); COVERAGE_NOTES: retire the 107_/108_ pending rationale lines; the W18 identity-only pending set rationale stands.

**Review gate:** reviewer verifies counts mechanically (grep FR/LB/OQ counts per file vs index rows; spe contiguity 001..204; taxation contiguity 001..421; `python3 shared/scripts/build_coverage.py sv --check` green; master-index appends consistent with T1-T4 diffs).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W24 T5: spe + taxation indexes, master-index rollups, COVERAGE regen (107_/108_ cited; +6 FRs -> 1,730)"`

---

## Final whole-wave review + ONE fix wave (controller)

- [ ] **F-1:** Dispatch a fresh whole-wave reviewer (read-only): all five task diffs vs the plan + EV bank + instrument txts; verdict MERGE-READY / USABLE-WITH-FIXES; log to SDD ledger.
- [ ] **F-2:** If USABLE-WITH-FIXES: execute ONE fix wave addressing all Critical/Important findings (deferred minors triaged ride/ignore per house convention); re-verify; commit.
- [ ] **F-3:** Bookkeeping (Task 6): update `sv/HANDOVER.md` (§1 wave-log entry; §3 corpus/EVID state; §4 corpus table + COVERAGE rollup; §5 W24 log + W24-process rulings; §6 external-check note [uif 403 WAF-back; D.O. still down]; §7 SOQ register [SOQ-40 resolved; SOQ-41 residual = RAEX only]; §8 next-actions) and `sv/EXTRACTION_PLAN.md` (W24 extraction-log entry); preserve W24 process rulings into HANDOVER §5 BEFORE any SDD workspace deletion (W19 ruling (b)); commit: `git commit -m "W24 close: HANDOVER + EXTRACTION_PLAN bookkeeping"`.
- [ ] **F-4:** Push `sv-research`. Merge to main = owner decision (rebase-then-merge per §8.6/§4.6; never force-push).

## Expected end state

- spe corpus: 203 → **204 FRs** (FR-204 in 02; FR-200 amended in place); taxation corpus: 416 → **421 FRs** (417 in 01; 418-419 in 03; 420 in 08 + FR-224 amendment; 421 in 11); total SV corpus **1,730**.
- SOQ-41 residual = the RAEX reglamento config-gap (96_) only — the EVID-167 named set fully dispositioned. **SOQ-40/OQ-2 RESOLVED** (design confirmed; instruments rule-negative). spe/02 OQ-10 opened (108_ operative-format config-gap).
- COVERAGE: 107_/108_ cited; rollup **90/9/2/12 of 113 — gate green** (verify from the script). Registry unchanged (111 files, next=115).
- Remaining program after W24: residual acquisitions (§8.2 — SOQ-46 criteria instrument, F-11/F-11-v19+/F14-v17 watches, asamblea census negative watch), external watches (D.O. recovery; uif 403 re-probe → 2026-10-17 AML deadline), EV-bank hygiene queue, W23 cml deferred minors (next cml touch), owner merge decisions.
