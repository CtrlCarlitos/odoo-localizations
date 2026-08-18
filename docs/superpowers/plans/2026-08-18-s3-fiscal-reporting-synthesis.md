# S3 Synthesis Implementation Plan — sv fiscal-reporting (F-07/F-14) Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W8 fiscal-reporting evidence base (EVID-172..190, master-index clusters F1–F12) into Takumi-contract requirements files under `sv/requirements/fiscal-reporting/`, with FR numbering `SV-FREP-FR-nnn`, LB citations to the forms/manuals as primary authority, period-gated column rules as dated data (R/S from Enero-2025; Q-T/S-V from Febrero-2024; Nov-2022 DTE-identifier cutover; fuel/357 regime windows; F-14 v17 Quincena-25 vintage), layer split, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S3-A (F1–F12) is the synthesis worklist and its SOQ-08..14 register is binding (SOQ-10 carries an applied ruling). The declaration layer is a two-level engine: casilla-graph computation (F1) fed by annex-row builders (F2–F7) whose CSV exports reproduce the MH upload formats exactly; F-14 mirrors the same pattern (F8–F10); the informs (F-910/F-915/F-930/F-935) are views over the same retention/distribution ledgers (F11); the deadline calendar is dated configuration data (F12). This wave is F-07/F-14 + related informs ONLY: F-11/F-06/F-971 annual-declaration internals, payroll mechanics (SS caps feed, Quincena-25 law), IVA-core reglamento files, and NIIF are out of scope.

**Tech Stack:** Markdown; FR IDs `SV-FREP-FR-nnn` (new prefix `FREP` = fiscal-reporting; wave-sequential, no gaps, no renumbering).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S3-A + SOQ-08..14 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12 version-regime policy).

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + section/page). No trace → OQ, not FR.
- **Authority rule (S3):** the MH forms and upload manuals ARE the primary authority for declaration/annex mechanics — 34_ (F-07 v14 manual, ENERO 2025) + 39_ (F-07 form, Actualizado 15-08-2025); 35_ (F-14 v16 manual, OCTUBRE 2025) + 37_ (plantilla); 38_ (F-14 v16 form) + 59_ (F-14 v17 form, 2026-06-03); 61_-64_ (inform forms). Legal anchors named on the forms (CT 111/119/123/131/134/145/154-162/241, Ley IVA 63, Ley ZF 25, D.L. 764-2014 Art. 10.7, Ley ISR 74-C) are cited as printed; do not invent article text beyond what the forms/evidence quote.
- **DTE identifier mapping (operative, from EVID-174/175/177):** Serie = sello de recepción (40 chars); Resolución = número de control (28), pre-Nov-2022 = código de generación (32); Número = código de generación (32), pre-Nov-2022 = número de control; control interno blank for DTE. One shared FR (Task 2) states it; later annex FRs reference it by ID.
- **SOQ-10 ruling (binding):** 34_ §XIX defects — col J "36 caracteres" and col A's inverted Sept/Oct cutover — are manual transcription defects; the annexes-1-12 convention (32 chars; Nov-2022 cutover) is operative. Record as LB note; never encode the inverted cutover.
- **Version regime (D12):** period-gated column rules are dated data: F-07 R/S (Tipo Operación/Ingreso Renta) from Enero-2025 (else "0"); Q-T quartet from Febrero-2024 (else "0"; codes 8/9 semantics); F-14 S-V quartet from Febrero-2024; DTE-identifier cutover Nov-2022; DUI-vs-NIT XOR from Enero-2022; fuel annexes (Decreto 321 from Mar-2022; precios máximos from Abr-2022; Anexo 17 Jun-Ago-2022 closed; Decreto 357 mayo-2022→fin-de-obra); F-14 v17 form layout from 2026-06 (Quincena-25 casillas 417/418; rows 62-105) with v16 annex format pending (SOQ-09); inform-form vintages (F-910 v9 2021 print; F-915 v4/F-930 v3 2017 prints still listed 2026 — SOQ-13 adjacent).
- **Dead/near-dead text:** pago-mínimo remnant casilla on the F-14 form (EVID-183) is printed-but-dead per R21 — form-mirror may carry it, computation never feeds it (state this explicitly in the F-14 task); FVS tipo 02 and tiquetes tipo 10 remain valid annex codes for non-DTE emitters only (post-2025 DTE emitters cannot emit them — W5 finding).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Default this wave: annex builders, declaration engines, informs, calendar = `odoo`. Do NOT invent saas Layer rows without an ARCH/D-citation justification.
- English prose, Spanish legal terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; never silently dropped.
- **Cross-topic discipline:** cite existing FR IDs by reference, never duplicate content: e-invoicing (DTE fields/identifier FRs, invalidation events FR-103/104/117, R1 IVA-inclusive FE convention) = `SV-EINV-*`; retention computation rates/bases = `SV-TAX-FR-102..131`; distributions register = `SV-TAX-FR-132..149`; catalogs = `SV-CAT-*` — the annex document-type code lists (01/02/03/.../14) are form-annex taxonomies, NOT MH CAT catalogs; do not add them to the catalogs topic. Payroll boundary: SS caps values, aguinaldo/quincena-25 mechanics = payroll wave feed; this wave only mirrors them as annex columns/validations.
- SOQ handling this wave: SOQ-10 ruling recorded in Task 4 (LB note); SOQ-08/09/11/12/13/14 recorded as OQ rows with working assumptions per the master index.
- Files land in `sv/requirements/fiscal-reporting/` following the template exactly (7 sections, none deleted).

---

### Task 1: `sv/requirements/fiscal-reporting/01_f07-declaration.md`

**Files:** Create `sv/requirements/fiscal-reporting/01_f07-declaration.md`
**Covers master clusters:** F1 + F2
**FR numbering:** SV-FREP-FR-001..0NN (opens the prefix)
**Content requirements:**
- F1 casilla-graph engine (39_/EVID-179): the 77-row arithmetic as an FR family — identification block (NIT/NRC/actividad; Art. 74-A disminución flag + declaración-que-modifica number); sales buckets 5-21 → SUMA VENTAS casilla 105 (verbatim formula) and SUMA DÉBITOS 150; compras buckets 24-33 + otros créditos 34-41 → SUMA COMPRAS 100 / SUMA CRÉDITOS 145 (verbatim formulas incl. the proporcionalidad credits 132-134 and retention credit 128 = CT 162); remanente 155 vs impuesto determinado 160; al-declarante credits 161-166 (+74-A block 491-493→203); excedente 167 / total-período 168; D.L. 764-2014 control-de-liquidez credit 520 + FOVIAL credit 525 → 521; por-declarante block 169-172 (+401-405 modificatoria) → 187/188/190/189/523/524; multas 192-195 + intereses 196 → TOTAL A PAGAR 198; USD-only declaration; every casilla mapped to its Odoo source field in the Odoo Mapping table.
- F2 upload engine (34_ §II/§XVI-§XVII/EVID-173/178): semicolon-delimited CSV; all-Text cell typing; filename ≤25 chars; no headers/merged cells; 2-decimal truncation; 0.00 nils; negative-value gate (anulados only, CT 111); DD/MM/AAAA period-consistency validation; 3-prior-period acceptance windows (compras per Ley IVA Art. 63; anulados per CT 111); annex-number column on every row; per-annex structure validation; upload-response handling (success summary; line-numbered inconsistencies); modificatoria flow (annexes 3-12 carryover from the prior declaration; 1-2 must be re-uploaded; limpiar-replace semantics).
- AC examples: casilla arithmetic spot-checks (105 = 85+86+88+89+90+91+92+93+94+95+96+98+99+586−97−552; 145 formula; 198 chain); CSV export reproduces a fixture row byte-for-byte; period-mismatch row rejected.
**Special steps:** transcribe the verbatim casilla formulas from 39_ (already quoted in EVID-179 — copy from there, do not re-read the PDF).

### Task 2: `sv/requirements/fiscal-reporting/02_f07-annexes-sales.md`

**Files:** Create `sv/requirements/fiscal-reporting/02_f07-annexes-sales.md`
**Covers:** F3
**FR numbering:** continues SV-FREP prefix sequentially from Task 1's last FR.
**Content requirements:**
- THE shared DTE-identifier-mapping FR (column semantics per document class incl. physical: resolución/serie/preimpreso ranges; formulario único control-interno; DTE mapping per Global Constraints) + the Nov-2022 cutover as dated data.
- Anexo 1 (B2B, per-document): column model A-T (verbatim from EVID-174); clase 1/2/4; tipos 03/05/06; DUI-vs-NIT XOR (Enero-2022 gate); anulados excluded (route to the anulados annex); R/S Renta pair (Enero-2025 gate; code lists verbatim incl. 12 = F14/F910-consolidated and 13 = Art. 6 LISR excluidos; pre-2025 → "0").
- Anexo 2 (B2C, aggregated): column model A-W; tipos 01/02/10/11; physical range rows (DEL/AL; máquina registradora for tiquetes; F=G/H=I identity rules per clase); DTE rows grouped BY DAY with first/last código de generación; N/A for resolución/serie on DTE; gravadas locales IVA-INCLUSIVE (cite R1/FE convention cross-ref to e-invoicing); export buckets dentro/fuera CA (country list GT/HN/SV/NI/CR) + servicios + ZF/DPA tasa 0; Ventas Internas Exentas No Sujetas a Proporcionalidad column; negatives only anulados (CT 111); U/V pair with the same gate as R/S.
- Cross-check awareness FRs (Aduanas export/import reconciliation flags — informational, not computation).
- Odoo Mapping: row builders keyed to account.move lines (sale side) with the IVA-inclusive/net convention switch; aggregation modes (per-document vs per-day).
**Interfaces:** Task 4's anulados annex FR references Task 2's row models; Task 1's casilla FRs consume the annex totals.

### Task 3: `sv/requirements/fiscal-reporting/03_f07-annexes-purchases.md`

**Files:** Create `sv/requirements/fiscal-reporting/03_f07-annexes-purchases.md`
**Covers:** F4 (annexes 3 + 5)
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Anexo 3: column model A-U (verbatim EVID-176); clase 1/2/3/4; tipos 03/05/06/11/12/13 (11 = ZF/DPA buyers only, Ley ZF Art. 25 anchor; 12 = Declaración de Mercancías; 13 = Mandamiento de Ingreso); IVA buckets G-M (internal/internación/importación × exenta/gravada; importaciones de servicios from mandamiento); crédito fiscal = 13% of J..M (validation FR); total G..M with ND+/NC− semantics; Tesorería pseudo-NIT 06140108140066 for foreign 12/13 suppliers; DUI-vs-NIT XOR; Q/R/S/T ISR quartet (Febrero-2024 gate; code lists verbatim; code 8 = multi-annex dedup excluded from ISR cost/gasto sums; code 9 = public institutions/municipalities/non-deductibles) — the quartet is the SAME taxonomy as F-14's S-V (reference, do not duplicate the code lists twice in this file — one canonical FR here, F-14 file references it).
- Anexo 5 (compras a sujetos excluidos, casilla 66): column model; CT 119 anchor; 13% retention column; I-L quartet; the post-entero crédito re-entry into casilla 128 (cross-ref Task 1's 128 FR).
- AC examples: crédito = 13% of gravadas bucket sum; Tesorería NIT substitution; quartet gating by period.
**Interfaces:** Task 1's casilla 65/66/128/130 FRs; taxation T3 pro-rata credits (132-134) stay in Task 1 (declaration level), not here.

### Task 4: `sv/requirements/fiscal-reporting/04_f07-annexes-retentions-events.md`

**Files:** Create `sv/requirements/fiscal-reporting/04_f07-annexes-retentions-events.md`
**Covers:** F5 + F6 (annexes 4, 6-12; anulados/emitidos)
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Anexo 4 (cuenta de terceros domiciliados, casilla 108): mandante identification + CCF/factura row + comprobante-de-liquidación linkage columns; monto sin IVA for consumer-final facturas; reference Task 2's identifier-mapping FR.
- Annexes 6-8 (al declarante: 161 anticipo 2%, 162 retención 1% incl. tipo 07 CRE, 163 percepción 1% incl. tipo 12 DUA): column models; agent NIT/DUI; credit-side aggregation into Task 1's casillas.
- Annexes 9-12 (por el declarante: 169 percepción 1%, 170 retención 1%, 171 anticipo 2%, 172 retención 13%): column models; tipos 05/06/07 (and 03/12 where printed); % validation (1/2/13 — the MH-side validator parity FR); anulados excluded.
- F-930 v3 view (EVID-189): document-typed summary + per-contribuyente rows with calidad/modalidad — one FR family defining the F-930 as a VIEW over the same retention ledger (no second ledger).
- F6 anulados/emitidos: XIX column model A-J (verbatim EVID-178); detail codes A/X/D (anulado/extraviado/DTE-invalidado); clase 1/2/4 with DTE zeros/blank rules; serie = sello 40c on DTE; the full 12-type document list (01-14 incl. 04 NRE, 08 CLE, 09 DCL, 14 FSE — the only place NRE/CLE/DCL/FSE appear in F-07); **SOQ-10 ruling LB note** (defects: 36-char + inverted cutover — annexes-1-12 convention operative); Documentos EMITIDOS auto-derivation FR (system derives the emitidos detail from annexes 1/2/9/10/11/12 uploads — Odoo replicates by deriving the same view); invalidation-event feed interface FR (source = e-invoicing events FR-103/104/117; invalid DTEs enter as detail code D — closes e-invoicing 02 OQ-008's F-07 side; note the retorno gap stays open with e-invoicing).
**Interfaces:** e-invoicing 03_events FR IDs (cite, never restate); Task 1 casillas 108/161-163/169-172/187-190.

### Task 5: `sv/requirements/fiscal-reporting/05_f07-annexes-special.md`

**Files:** Create `sv/requirements/fiscal-reporting/05_f07-annexes-special.md`
**Covers:** F7 (annexes 13-17)
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Anexo 13 (tasas diferenciadas, from Mar-2022, Decreto 321): MANUAL-entry regime (no CSV structure — the only F-07 annex without a file); global NET-of-IVA values by fuel grade SUPERIOR/REGULAR/DIÉSEL; 13% fuel ops stay in annexes 1-3; casillas 586-589 wiring.
- Anexo 14 (descuento precios máximos, from Abr-2022, Ley Especial Transitoria): NC-only column model A-P (galones 11+8 decimals; precio 2+2 sin IVA; valor/descuento/IVA-del-descuento sin IVA); tipo operación 1 compras / 2 ventas; casillas 550-553 wiring.
- Anexos 15/16 (Decreto 357 informativos, casillas 92/65, mayo-2022→fin-de-obra window): column models; informativo status.
- Anexo 17 (importadores, Jun-Ago-2022 CLOSED window, informativo): column model; closed-vintage note.
- All as D12 dated regimes: validity windows as data; regime-active flag derived from decree status; FOVIAL/COTRANS credit interplay pointer (casilla 525; 31_ guide — quantity-tax design decision stays open with the taxation/special-regimes waves).
**Special steps:** this file is intentionally compact; keep FR count proportional (est. 8-14 FRs).

### Task 6: `sv/requirements/fiscal-reporting/06_f14-declaration.md`

**Files:** Create `sv/requirements/fiscal-reporting/06_f14-declaration.md`
**Covers:** F8 + F10
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Annex column model A-W (verbatim EVID-180): domiciliado 1/2 + país code (4-digit; haven 25% exactness warning) + NIT/NIF (foreign NIF for no-domiciliados) + DUI XOR; código de ingreso; monto devengado vs bonificaciones-gratificaciones vs aguinaldo exento/gravado split (codes 01/60/80 include AFP+cotizaciones, EXCLUDE aguinaldo/bonificaciones — 37_ plantilla note); SEVEN SS columns with legal caps (AFP $472.93, ISSS $30.00 as $-caps; INPEP 7.5%, IPSFA 9.5%, CEFAFA 5%, Bienestar Magisterial 5.58%, ISSS-IVM 7.5% as %-maxima — dated data, payroll-wave feed per SOQ-11); S-V quartet references Task 3's canonical FR (Febrero-2024 gate); periodo MMYYYY.
- Validation contract (EVID-181): retention % must equal the legal rate per income code (MH rejects otherwise — Odoo export pre-validates; rate source = SV-TAX-FR-121..131 matrix by ID); aguinaldo gravado ≤ devengado; SS-cap enforcement; 2-decimal truncation; DUI/NIT XOR.
- Declaration = pure projection of the annex (no manual casilla entry; every casilla auto-totals) — the invariant FR.
- Form architecture (EVID-183): seven tabs; acreditables con/sin dependencia laboral; definitivas; no-domiciliados matrix tracks; Operaciones Financieras liquidity tracks 501-529 (acreditable control-de-liquidez vs definitive cheque/transferencias/mercado-de-valores — instrument taxonomy FR with OQ on the CT 159 anchor); contribución especial; agentes extranjeros 701-780 (retención + entero donantes locales blocks — F-935 cross-ref Task 7); pago-a-cuenta block 42-56 incl. excedentes and the 74-A ajuste; **pago-mínimo remnant casilla: printed-but-dead (R21) — form-mirror carries it, computation never feeds it (explicit FR note)**.
- Modificatoria flow: limpiar + full re-upload; prior-amount anchors (casillas 50/221/225/332/711/761).
- F10 Quincena-25 vintage (EVID-184): v17 form adds the INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO section (row 61, casillas 417/418; rows 62-105 renumbered) — form-level FR with vintage gate from 2026-06; annex-level representation BLOCKED (no v17 manual; SOQ-09 OQ row with working assumption: v16 columns + new income code expected, unconfirmed).
- AC examples: payroll-row column split (devengado excludes aguinaldo for code 01); %-per-code rejection parity; haven-25% warning; Quincena-25 casilla isolation (417/418 do not enter 330-336 arithmetic).
**Interfaces:** SV-TAX-FR-104 (base), FR-106 (thresholds), FR-102 (retention posting) cited as the computation sources; payroll wave = SS-cap + quincena-25 feed owner.

### Task 7: `sv/requirements/fiscal-reporting/07_codes-and-informs.md`

**Files:** Create `sv/requirements/fiscal-reporting/07_codes-and-informs.md`
**Covers:** F9 + F11
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Income-code catalog as dated data (EVID-182, full code list transcribed): code → description → class (acreditable/definitiva/sin-retención 60/no-gravado 70-72) → F-14 row/casilla mapping → CT anchor where the apéndice prints one; code 43/44/45 = distributions leg (interface to SV-TAX-FR-132..149 + the earnings register — the F-14 row is the withholding leg); code 40 = haven 25%; code 47 = CT 123 aggregate row (NIT 14 zeros + VARIOS).
- Cross-tax classification coupling: F-07 R/S pair (code 12 wording "consolidados en F910") + F-14 codes feed the F-11 rentas matrix — one FR stating the coupling and referencing F3's code lists.
- F-910 v9 (EVID-187): annual per-contribuyente consolidation over the 12 monthly F-14 annex rows — GROUP BY semantics + the 01-vs-60 annual rule (retained-at-least-once → 01; never → 60); ANNUAL SS columns; folio-modifica; **records the answer to taxation 04 OQ-007/MOQ-10's ISR side — note for the index task to add the cross-ref in taxation 00_index.md**.
- F-915 v4 (EVID-188): DISTRIBUYÓ/CAPITALIZÓ modes + acta fecha/número; socio-quality transition split (antes/durante/perdió) × cantidad/utilidades-distribuidas/valor-contable-capitalizadas; per-socio rows incl. no-domiciliado flag; builder over `l10n_sv.isr.earnings.register`; CT 241 + CP 249-A juramento note; **partially answers taxation 05 OQ-002 (format published; norms resolution still absent) — index-task cross-ref**.
- F-935 v1 (EVID-190): RETENCIÓN vs ENTERO blocks; transfer-level rows (concepto/fecha/número-de-transacción/país-de-origen/monto sujeto/retención-entero); donantes-locales track (SOQ-13 OQ row); counterpart of F-14's agentes-extranjeros tab.
- F-930 already homed in Task 4 — reference only.
- AC examples: 01-vs-60 classification from 12 monthly rows; F-915 quality-transition buckets from register events.

### Task 8: `sv/requirements/fiscal-reporting/08_filing-calendar.md`

**Files:** Create `sv/requirements/fiscal-reporting/08_filing-calendar.md`
**Covers:** F12
**FR numbering:** continues SV-FREP prefix.
**Content requirements:**
- Obligation inventory as dated data (EVID-185): monthly core (F-07/F-14/F-06/F-930/F-935/F-945/F-960); annual anchors (F-910/F-915/F-986/F-987-primer-semestre Feb; F-455 CT 134 Mar; F-11/F-971/F-944/F-30/F-40/F-982 Apr; auditor-fiscal appointments CT 131 + LSI May; F-987 second half Jul; F-950 quarterly pattern — SOQ-14 OQ); third-party reports (F-985/F-975/F-995) = informational only, not taxpayer FRs.
- Deadline engine: asuetos table (2026 list verbatim) feeding the días-hábiles computation shared with e-invoicing deadlines + taxation remittance; calendar as dated data with the Asamblea-modification disclaimer (versioned annually).
- Due-day windows: SOQ-08 OQ row — working assumption: window configuration data unpinned (visual calendar layer); FR states the config-driven window mechanism without hard dates; AC uses placeholder-config tests, not real dates.
- Odoo Mapping: deadline/reminder model keyed to obligation inventory; config interface for the window data.

### Task 9: `sv/requirements/fiscal-reporting/00_index.md` + `sv/requirements/COVERAGE.md` + README updates + taxation cross-refs

**Files:** Create `sv/requirements/fiscal-reporting/00_index.md`; update `sv/requirements/COVERAGE.md` (fiscal-reporting rows 29_/30_/34_-39_/59_/61_-64_ → cited-as-LB; rollup counts + total rows); update `sv/README.md` topic status fiscal-reporting → In review (+ source count 56 → recheck); add cross-ref notes to `sv/requirements/taxation/00_index.md` (04's OQ-007 and 05's OQ-002 get "partially answered by S3 F-910/F-915 — see fiscal-reporting 07" pointers, minimal edit) and to `sv/.extractions/00_MASTER_INDEX.md` coverage totals (S3 delivered line).
**Content requirements:** index file (per-file FR ranges/counts/LBs/ACs/OQs; numbering note: wave-sequential within SV-FREP prefix; OQ rollup with the SOQ-08..14 mapping to file OQ ids); COVERAGE rollup updated; README flips.

## Standing review gates (every task)

1. Fresh implementer subagent per task; reviewer subagent verifies against master index F-clusters + SOQ-08..14 + this plan's Global Constraints (SDD loop).
2. Reviewer checks: every FR has an LB citing the form/manual EVID (34_/35_/38_/39_/59_/61_-64_) or a printed legal anchor; period-gate/version notes present wherever the Global Constraints list a cutover; SOQ-10 ruling applied (no inverted cutover anywhere); pago-mínimo dead-casilla note present in Task 6; Layer column complete; OQs recorded; template's 7 sections intact; cross-file references by FR ID not content duplication (esp. the identifier-mapping FR referenced, not restated; the quartet taxonomy canonical in Task 3).
3. Fix rounds per SDD; findings ledger kept in the SDD workspace; at wave close, rulings copied to HANDOVER.md BEFORE workspace deletion.
