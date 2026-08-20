# S9 Synthesis Implementation Plan — sv taxation IVA-core Takumi files (Ley IVA + Reglamento IVA)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W15 IVA evidence base (EVID-304..338 + the W3 legacy EVID-047..058, master-index clusters V1–V10 + R30 + SOQ-54..58) into Takumi-contract requirements files under `sv/requirements/taxation/` (files 07-15), with FR numbering **continuing `SV-TAX-FR-176`+** (R30(b) ruling), LB citations to 01_/02_ as printed (SOQ-54 vintage note rides every LB) plus CT co-cites where the retention matrix demands, ACs, and coverage tracking — closing the corpus's last pending source row (02_).

**Architecture:** Requirements follow the 7-section template; master index Section S9-A (V1–V10) is the synthesis worklist and its citation-rule preamble + SOQ-54..58 register are binding. Layering: the framework file (V1) owns the operation/hecho-generador/subject model incl. excluidos; exemptions (V2) owns the Arts. 45/46 catalogs + the Art. 174 generic-nullity gate; base & rate (V3) owns base composition incl. the FOVIAL/COTRANS base guard and the SOQ-40 B2B-chain→DTE design pass; credit deductibility (V4) owns the Art. 65/65-A gates + document routing; pro-rata & remanente (V5) owns the Art. 66 engine + Arts. 67-70 + the tercerización pointer closure; adjustments & assets (V6+V7) owns the 62-64 windows + medicines lot registry + the 71-72 four-year rule; retentions (V8) owns the CT 161/162/162-A/162-B matrix fold-in; exports & refunds (V9) owns Arts. 74-77 + ZF/LSI routing; declaration & interfaces (V10) owns the monthly engine feeds + the S3 cross-ref wiring. Cross-topic mechanics are consumed BY FR ID (e-invoicing doc types/§3.11/R1; fiscal-reporting F-07 annexes/casillas/días-hábiles; special-regimes SR5/SR8; payroll SMM) — never restated.

**Tech Stack:** Markdown; FR IDs `SV-TAX-FR-nnn` continuing at **176** (wave-sequential across the new files, no gaps, no renumbering; S6 append precedent). CSV sidecars only if a printed data table warrants one (default: none — dated values are few; the 13% rate history and [sic] colones thresholds live as in-FR dated rows).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S9-A + Section S9 authority-order preamble + R30 + SOQ-54..58 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12 + D15 as-of doctrine + D16 mechanics canon) + D18/D19 + `go-live-readiness.md` + `sv/HANDOVER.md` (country memory).

**Evidence inputs (read-only for implementers; scoped per task per S8 ruling (c)):**
- `sv/.extractions/01_Ley_IVA.evidence.md` — W15 section **lines 99-357** (EVID-304..338 + W15 OQs); W3 legacy entries lines 1-97 (EVID-047..058) still citation-valid
- Extraction txts (worktree-local, on-demand grep + bounded window, NOT full reads): `sv/.extractions/01_Ley_IVA.pdf.txt` (2,104 lines), `sv/.extractions/02_Reglamento_IVA.pdf.txt` (384 lines), `sv/.extractions/05_Codigo_Tributario.pdf.txt` (CT Arts. 161@3860 / 162@3874 / 162-A@3951 / 162-B@3991 for V8 verbatim; Art. 62 FX ~line 840)
- ONE exemplar: `sv/requirements/taxation/06_isr-assets.md` (structure, LB-row format, FR/AC/OQ conventions, version-regime note)

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article + txt PAGE anchor). No trace → OQ, not FR.
- **Authority rule (binding):** Ley = 01_ (D.L. 296-1992 Asamblea consolidation through reform (14) D.L. 71-2015; embedded interpretaciones auténticas D.L. 634/820/645 are part of the text; Arts. 113/123/124/161 void — sent. 17-dic-1992); Reglamento = 02_ (D.E. 83-1992; survivors Arts. 1-10/16-30/50-52 only per R30(a) — D.E. 117-2001 repeal map; stale anchors cite-with-note). **Every file's §2 carries the SOQ-54 vintage note** (post-2015 reforms unverified; corpus-internal signals negative). CT-side mechanics cite 05_ (EVID-062 matrix + CT txt verbatim; Arts. 110/112/119/141/142-142-A/161/162/162-A/162-B).
- **FR numbering contract (R30(b)):** continue `SV-TAX-FR-176..` wave-sequential across files 07-15 in task order; NO gaps, no renumbering; tasks STRICTLY IN ORDER; the index task verifies continuity (`grep -o "SV-TAX-FR-[0-9]*"` → contiguous 176..N) and that no ISR-file FR (001-175) was touched.
- **D15 anchors:** IVA resolves as-of the hecho-generador/tax-point date (invoice date for transfers; delivery/payment whichever first; import acceptance) and snapshots on the record (account.tax versioned per D15/D7 packs); corrections use ORIGINAL-period parameters (D9 interplay with the Art. 63 3-period rules by id).
- **Hard encodings from 01_/02_ (cite as printed):** 13% (Art. 54; D.L. 370-1995 history row); CCF = IVA separate from price, FE inclusive (Art. 57 → R1 by id); **retiros/autoconsumo = FACTURA-only, CCF/ND banned (Art. 58)**; excluidos' facturas sin recargo (Art. 32); 3-month return window / medicines 2y + 6-field lot registry (Art. 62-1-a); late-doc 3-period rules + declaration-modification overflow (Art. 63); 65 gates + FACTURA-not-CCF else-branch; 65-A catalog incl. 50% mixed vehicles + 58-SMM payment gates; Art. 66 factor + accumulated recalc + **next-January redistribution** + exclusions + cost/gasto reclass; 67-70 remanente invariants (no refund at cessation; non-transferable except fusión/mandato legal; heirs get nothing); 71 four-year fixed-asset gate (alta-date anchor); exports 0% + connection/continuation/termination carve-out at 13%; reintegro 30 days + suspension + 13%-of-export-value cap (mixed/pure) + accumulation; monthly period + 10 primeros días hábiles + no prórrogas (Arts. 93/94/81); import payment constancy = credit document (Art. 94-III); **Art. 174: other laws' generic exemptions produce NO effect**; 167-A kill-switch on 45-h.
- **Pointer-only / boundary surfaces (zero invented mechanics):** Decreto 321 differentiated fuel-rate VALUES (fiscal-reporting/05 OQ-001 stays the owner — IVA files encode only the base/casilla mechanics by id); Art. 28 administered exclusion criteria (SOQ-55 config-gap; [sic] colones, NO USD conversion); Art. 46-f BCR-qualification instrument (SOQ-56); Art. 46-k SAP citation (SOQ-57 — substance carried, anchor stale); 167-A instrument (SOQ-58); COTRANS instrument (SOQ-39/MOQ-04 — guard rows only).
- **Fold-ins owed by this wave (index task wires; file tasks write the substance):** taxation/02 OQ-009 tercerización pointer (V5 → FCF-exento + no-pro-rata working reading per R30(c)); S3 fiscal-reporting/03 OQ-004 (annex-5 excluido-13% applicability — V8 defines the retention regime it consumes); S3 fiscal-reporting/02 OQ-002 rate anchor (V3 owns the 13%/base authority); **SOQ-40 FOVIAL B2B-chain→DTE-tributo design pass (V3, co-cite SR8 FR-166..175 by id)**; MOQ-03 closure (SOQ-55 footnote in V1); MOQ-04 base-guard half (V3 guard rows, 31_ co-cite).
- **Cross-topic discipline (cite FR IDs, never duplicate):** e-invoicing SV-EINV doc types/§3.11 FR-159..164/R1 (CAT-015/D1 tributo fields); fiscal-reporting SV-FREP F-07 casilla graph/annexes 1-14/días-hábiles FR-202..204/F-930 view; special-regimes SV-SPE SR5 FR-087/095 + SR8 FR-166..175; payroll SV-PAY FR-011..023 SMM feeds; ISR-side matrices stay taxation/01-06 (04's CT 154-160 rows by id — the IVA retention track NEVER merges with the ISR track); chart-of-accounts N4/N6 by id (book track separate).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). IVA-core is Odoo-native (account.tax, account.move.line, fiscal positions, partner categories) — default `odoo`.
- English prose, Spanish standard terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; in-file OQ numbering per file (OQ-1..n); SOQ-54..58 carried into their home files as OQ rows with the SOQ id noted.
- **Quote fidelity (S5 ruling 37 binding):** verbatim sweeps against the txts are the norm; silent truncation of a statutory catalog (e.g. Art. 7 a)-m), Art. 17 a)-q), Art. 45 b)-i), Art. 46 a)-l), Art. 48 a)-m), Art. 65-A a)-n)) = Important-grade defect; use the "(first N…; X omitted — topic)" marker convention when abbreviating; single-word deviations are defects.
- Files land in `sv/requirements/taxation/` following the template exactly (7 sections, none deleted).
- **Process:** execute in `.worktrees/sv` on branch `sv-research`. Commit style: short imperative, no emojis, commit per task. Push at wave close (or at session boundaries if context runs low — resume state recorded in sv/HANDOVER.md first). Dispatch template = S8 ruling (c): scoped evidence line-ranges, ONE exemplar, on-demand txt via grep + bounded window.

---

### Task 1: `sv/requirements/taxation/07_iva-framework.md`

**Files:** Create `sv/requirements/taxation/07_iva-framework.md`
**Covers:** V1
**FR numbering:** opens SV-TAX-FR-176
**Evidence (scoped):** EV01 W15 lines 105-169 (EVID-304..312) + 322-334 (EVID-335..336: Rgto. definitions/retiro/force-majeure) + txts on demand (Ley pp. 2-16 = txt lines 45-560; Rgto. Art. 2 = txt lines 16-102)

**Content requirements:**
- §2 preamble: the S9 authority order (01_ as printed through D.L. 71-2015 + SOQ-54 vintage note; 02_ survivors per R30(a); CT re-anchors for procedure) + the V1 citation rule.
- Operation-model FRs: Art. 1 scope; Art. 5 vocabulary (tangibles; títulos valores incorpóreos; **mutuos dinerarios/financiamiento = services**); Art. 6-7 transfer concept + a)-m) enumeración (aportes f, reorg g, liquidation carve-out h, consignment m) with full-catalog fidelity; Art. 8 tax point (document first, earlier payment/delivery, consignment trigger, caused despite non-payment); Art. 9 exchange/return → 62 path (not new transfer); Art. 10 goods territoriality (situs/matriculado/registrado; shipped-to-non-contribuyente rule).
- Retiro FRs (Art. 11-13): use/consumption of socios/directivos/personal **+ grupo familiar + terceros (Rgto. Art. 4)**; raffles/promo giveaways whether or not in giro; inventory-shortfall presumption with the Rgto. Art. 4 fuerza-mayor evidence menu (chronological permanent-inventory annotations, denuncias, insurance liquidations, recognized mermas) + accounting-date precondition; realizable→fijo no-retiro (giro-necessary); ISR-6-c donation carve-out; date-of-retiro anchor (D15).
- Import/internación FRs (Art. 14-15 + D.L. 645): goods+services; **D.L. 645 exclusive-SV-use interpretation verbatim**; services-import tax points a)-c); special-regimes definitive-conversion trigger (SR4 consumer by id); aduana auctions.
- Services FRs (Art. 16-17): hecho generador + autoconsumo; indemnizations out; qualified gratuitous donations out; the a)-q) catalog full-fidelity (leases muebles c / commercial inmuebles d; construction j/k; transport m; liberal professions + notariado n; royalties o; dietas p; membresías q); **reintegros/reembolsos = services at payment** with the seguros/alimentación/viáticos-laborales + Art. 51-a mandate/no-credit-deduced exception gates.
- Service tax-point FRs (Art. 18): a)-e) incl. advances; permanent/periodic services (document or period-end); leasing exigibilidad or sale.
- Territoriality FRs (Art. 19): performance test; partial ⇒ proportional; transit ⇒ full; foreign-transport-in-import-base no-re-tax.
- Subjects FRs (Art. 20-27): sujetos list incl. unions/consorcios + government entities (bursátiles exception); representation; contribuyente definitions 22-24 (habitual or not for importers 23); **habitualidad presumption de derecho (25)**; **matriz-sucursales ONE taxpayer (26 — D14 kin)**; agrupamientos solidarity (27).
- Excluidos FRs (Art. 28-32 + Rgto. 9-10): [sic] colones thresholds as dated-historical rows; **SOQ-55/MOQ-03 config-gap footnote** (administered criteria absent; no USD conversion); two-threshold concurrence (Rgto. Art. 9); month-subsiguiente flip; societies/importers/multi-local carve-outs; optional status from next Jan-1 (DGII discretion); Rgto. Art. 10 evidence (libro de gastos-compras-ventas + inventario valorado); no crédito ever (31); **facturas sin recargo (32)** → FSEE enforcement (e-invoicing by id).
**AC examples:** consignment goods taxed at consignatario's first document/delivery/payment; retiro invoice auto-emitted as consumidor-final with public-sale value base; mutuo dinerario classified as service; excluido partner's invoice rejects any IVA line.
**OQs to carry:** SOQ-54 (preamble), SOQ-55.

### Task 2: `sv/requirements/taxation/08_iva-exemptions.md`

**Files:** Create `sv/requirements/taxation/08_iva-exemptions.md`
**Covers:** V2
**Consumes:** T1 framework classification (by id).
**Evidence (scoped):** EV01 W15 lines 170-183 (EVID-313..314) + 294-300 (EVID-331) + txt on demand (Ley pp. 19-22 = txt lines 603-760; pp. 51-55 = lines 1840-2010)

**Content requirements:**
- Import/internación exemption FRs (Art. 45 b)-i) full catalog): diplomatic reciprocity; international organizations; **equipaje per D.L. 820 (personal effects only; never vehicles)**; donations (ISR-6-c qualified + convenios); municipal obras; public water/alcantarillado (h) **with the 167-A kill-switch dated row (SOQ-58)**; public-transport vehicles (i) **with the 5-year transfer restriction register** (legalización-date anchor; early transfer ⇒ import IVA by transferor + internal-transfer IVA by acquirer per Art. 71 — T6 consumer by id; Reglamento-de-Transporte spec gate).
- Service exemption FRs (Art. 46 a)-l) full catalog): health (DGII-calified institutions); residential housing leases (vs commercial 17-d taxable); labor-dependence services + public employees; cultural spectacles; **education = only values paid to MINED-authorized institutions (stamp 11)**; **financial deposit/loan interest (f) with SSF-supervision + BCR-qualification flags (SOQ-56 config-gap) + public-utility financing corporations/foundations**; state/official + bolsa-primary-offering titles (g); public utilities (h); terrestrial public transport (i — air/sea passengers taxable); **seguros de personas + reaseguros (j)**; AFP administration commissions (k) **with the SAP-citation note (SOQ-57; R23/R24 kin — substance carried)**; Lotería Nacional (l).
- **Art. 174 generic-nullity FR:** exemption reason codes valid ONLY from Arts. 45/46 (+ ratified international instruments — Art. 66 diplomatic anchor); config rejects foreign-law generic-exemption claims (Ley de Imprenta exception noted as printed).
- Art. 44/45-a historical note (transfer exemptions repealed D.L. 877/00) as version-regime row.
**AC examples:** education-exempt invoice from a non-MINED-authorized academy rejected (taxed); 45-i bus transferred at year 3 triggers both import-side and internal IVA; a "ley especial" exemption claim fails the 174 gate.
**OQs to carry:** SOQ-54, SOQ-56, SOQ-57, SOQ-58.

### Task 3: `sv/requirements/taxation/09_iva-base-rate.md`

**Files:** Create `sv/requirements/taxation/09_iva-base-rate.md`
**Covers:** V3
**Consumes:** T1/T2 classification + exemptions (by id).
**Evidence (scoped):** EV01 W15 lines 113-119 (EVID-305) + 184-204 (EVID-315..317) + 322-327 (EVID-335) + `sv/.extractions/31_Guia_FOVIAL_COTRANS.evidence.md` (EVID-274; SR8 co-cite) + txt on demand (Ley pp. 23-27 = txt lines 765-935)

**Content requirements:**
- Base FRs (Art. 47-48): generic = precio/remuneración or valor aduanero; **documented-amounts floor**; specific bases a)-m) full-fidelity (remates + subastador rights; leasing renta + residual [Rgto. Art. 17: última cuota o adicional; tax per renta AND residual]; retiros at assigned public-sale value else market; permutas dual-side; goods-in-payment; **service-supplied goods aggregated even if standalone-exempt unless already in contract value**; self-used services market floor; commission-only for intermediaries; imports = CIF/aduanero + aranceles + specific consumption taxes, **IVA never in base**).
- Non-base FRs (Art. 49): indemnizaciones, propinas, provisional/union dues.
- Additions FRs (Art. 51 a)-d) full): price reajustes; financing interest incl. **late-payment interest**; gastos/fletes/reembolsos EXCEPT in-name-and-account-of-buyer mandates; multas/penal-clause + third-party-interest exclusions; accessories (embalaje/flete/transporte/limpieza/seguro/garantías/colocación/mantenimiento when not independent); envases + depósitos-en-garantía; **impuestos especiales added but IVA excluded (d — the FOVIAL/COTRANS root)**; mixed gravada/exenta ⇒ prorate additions.
- Exclusion FR (Art. 52): general unconditional discounts already documented in CCF/ND/NC.
- FX FRs (Art. 53): hecho-generador-day conversion; payment FX diffs out; **installment FX diffs in** (CT Art. 62 two-clock kin by id; e-invoicing §3.11 origin-rate by id). Aduana-value FX at acceptance day (Rgto. Art. 18).
- Rate FRs (Art. 54-55): 13% dated row (+ 10% 1992→1995 history row, D.L. 370-1995); débito = rate × base per operation. **S3 02 OQ-002 rate anchor closes here** (the 13%/base authority the F-07 annex 1/2 M/O débito columns consume — wiring by the index task).
- **FOVIAL/COTRANS base-guard + SOQ-40 design pass FRs:** the per-unit quantity-tax model (account.tax amount-type per-unit, $0.20/gal dated rows with instrument provenance via 31_/D.L. 208-2000 Art. 26 chain — SR8 by id); **never-in-base guard** (Arts. 2 + 51-d + 47/48-a via 31_ §IV.1 verbatim); separate document fila/casilla from price and IVA (e-invoicing CAT-015 D1 tributo fields by id); **the B2B recovery-chain → DTE mapping design: each chain seller books RETENCIÓN-FOVIAL credit / CUENTAS-POR-COBRAR-FOVIAL re-bill rows (SR8 FR-170/171 by id), the DTE carries the D1 tributo line per operation, final consumer absorbs — design FRs state the mapping + the chain invariant, provenance-dated; COTRANS rows config-gated (SOQ-39)**.
**AC examples:** base recomputation adds 2% financing interest but rejects a penal-clause multa; permuta books two débitos (one per side); fuel line computes $0.20×gal as separate tributo, base excludes it, IVA applies to price only; installment FX delta adds to base at collection.
**OQs to carry:** SOQ-54; SOQ-40 design-pass note (chain mechanics = 2001 guide vintage, DTE mapping = design); SOQ-39/MOQ-04 guard note.

### Task 4: `sv/requirements/taxation/10_iva-credit-deductibility.md`

**Files:** Create `sv/requirements/taxation/10_iva-credit-deductibility.md`
**Covers:** V4
**Consumes:** T1-T3 (by id).
**Evidence (scoped):** EV01 W15 lines 198-210 (EVID-317..318) + 231-244 (EVID-322..323) + 328-334 (EVID-336) + txt on demand (Ley pp. 26-34 = txt lines 890-1255)

**Content requirements:**
- Traslación/CCF FRs (Art. 57): credit = débito amount; **CCF states IVA separate from price (R1's root; FE inclusive by id)**; importers' paid IVA = crédito (Rgto. Art. 19: póliza/DUCA + recibo pair).
- Art. 58 FR: retiros/autoconsumo generate NO crédito; **FACTURA-only documentation; CCF/ND blocked** (Rgto. Art. 20 "como consumidor final"); Art. 60 excluidos no-crédito → cost; Art. 61 naturaleza jurídica (no pago-indebido claims).
- Art. 65 gate FRs: the four destinations (1 activo realizable; 2 activo fijo identity-keeping non-inmueble; 3 giro services EXCLUDING construction/reconstruction/remodeling of inmuebles any modality; 4 gastos generales examples) + **the indispensable + gravada-generation requirement** (débito, 0%, ISR-6 donations, diplomatic sales per stamp 13); **else-branch = FACTURA not CCF (buyer must not request, supplier must emit)**; formal requirements (original CCF with separate IVA or import proof; libro de compras CT 141; inventory register CT 142/142-A); adquisiciones = local + imports + internaciones; Rgto. Art. 21 gastos-generales definition.
- **Retention-credit FRs (Art. 65 final incisos + Rgto. Art. 23):** CT-162 retentions = agent crédito **same period as the comprobante emission IF declared + entered integrally same period + registered separately**; CT-161 route via mandamiento de ingreso (T8 ledger tie by id; F-07 casilla 128/F-930 consumer by id).
- Art. 65-A non-deductible FRs (a)-n) full catalog): food outside giro (+ supplier FACTURA note); food imports; vehicles-not-strictly-indispensable + their fuel/lubricants/repuestos/maintenance/insurance; hotels without business-use proof; air tickets except verifiable-employee business travel; clothing/jewelry outside giro; personal/family use; alcohol/cigarettes; over-rate traslados; general non-indispensables; **construction/edification inputs (k)**; **58-SMM gates: cash-or-no-formal-contract (l-m-n structure as printed)**; **50% mixed-use vehicles**; unauthorized-numbering CCFs; fake/irregular docs 1)-5) (unregistered emitter; unproven operation; de-registered published subjects; unauthorized correlativos; not-in-name / no economic-impact absorption) + criminal reservation; giro = tarjeta-de-contribuyente registration identity; blocked values → ISR cost subject to ISR rules (Art. 70 mirror; taxation/02 by id).
**AC examples:** construction-service purchase credit blocked at validation; mixed-use vehicle purchase books 50% crédito and 50% cost; ≥58-SMM cash purchase rejected; unregistered-emitter CCF never credits.
**OQs to carry:** SOQ-54; 58-SMM sector-selection kin (SOQ-18 crossref, SMM feed payroll/02 by id).

### Task 5: `sv/requirements/taxation/11_iva-pro-rata-remanente.md`

**Files:** Create `sv/requirements/taxation/11_iva-pro-rata-remanente.md`
**Covers:** V5
**Consumes:** T4 credit engine (by id).
**Evidence (scoped):** EV01 W15 lines 245-258 (EVID-324..325) + 328-334 (EVID-336 Rgto. 24-25) + `sv/.extractions/66-70_Quincena25.evidence.md` (tercerización citation, EVID-237/238) + txt on demand (Ley pp. 34-36 = txt lines 1256-1350)

**Content requirements:**
- Pro-rata FRs (Art. 66): monthly factor gravadas/(gravadas+exentas+no sujetas); **accumulated base from first pro-rata period through fiscal-year end**; **next-January full-year recalc + redistribution (sum-to/rest-from the first period's credit)**; record conservation + exhibition; denominator exclusions (no-habitual no-attributable-credit no-sujetas; donations per 11/16 finals; diplomatic sales under ratified instruments); no-sujetas definition; **exenta/no-sujeta proportion → cost or gasto** (fiscal-reporting casillas 132-134/137-138 by id).
- **Tercerización FCF-exento FR + taxation/02 OQ-009 closure:** the R30(c) working reading (67_ cites Art. 66 "inciso sexto parte primera" = pre-224-2009 numbering → current print's no-habitual exclusion; OQ-tracked) — FCF con valor exento document (e-invoicing FCF/FSEE-kin by id), no pro-rata application for the Quincena-25 pass-through operation, planilla-copy attachment duty (SV-PAY-FR-142 by id).
- Remanente FRs (Art. 67-70 + Rgto. 24): indefinite carryforward; **cessation: no refund, no offset, no transfer (68)**; non-transferable EXCEPT continuador-por-mandato-legal + fusión/absorción continuing the giro; liquidation no refund; universal aport ≠ transfer; related parties banned; heirs banned (69); IVA-never-cost/gasto except final-use/exempt/excluded destinations (70; Rgto. 25 unusable-credit → gasto general).
**AC examples:** mixed month computes factor over accumulated base; January redistribution posts the true-up to the first period's credit; fusión inherits the absorbed company's remanente; cessation leaves remanente unusable; Quincena-25 tercerización FCF stays out of the pro-rata denominator.
**OQs to carry:** SOQ-54; the R30(c) inciso-mapping OQ; no-sujeta-denominator attribution test config note.

### Task 6: `sv/requirements/taxation/12_iva-adjustments-assets.md`

**Files:** Create `sv/requirements/taxation/12_iva-adjustments-assets.md`
**Covers:** V6 + V7
**Consumes:** T3/T4 (by id).
**Evidence (scoped):** EV01 W15 lines 120-126 (EVID-306 7-g/h) + 211-230 (EVID-319..321) + 259-265 (EVID-326) + 328-334 (EVID-336 Rgto. 26) + txt on demand (Ley pp. 27-29/37 = txt lines 946-1065 + 1355-1380)

**Content requirements:**
- Débito-adjustment FRs (Art. 62): 3-month return/annulment/rescission subtraction with prior-computation proof; **medicines 2-year window: the 6-field lot registry verbatim (lote, nombre y presentación, vencimiento, entrada/salida, CCF number printing lote+vencimiento, CCF fecha, cliente código), NC referencing CCF + lote, inventory-vencido account, sanitary-authority destruction acts, 2-year caducidad extension**; discount/rebaja subtractions with form-and-condition proof; additions (increments; under-transferred differences; excess-unless-restituted); CCF + notas mechanics (CT 110).
- Crédito-adjustment FRs (Art. 63): anuladas/discount subtractions if previously computed; late CCF/ND ⇒ +crédito up to **3 following periods**; NC ⇒ reduce in emission period unless late-received ⇒ 3 periods; **beyond ⇒ mandatory declaration modification** (D9 freeze-at-filing by id; F-07 3-prior-period window consumer by id); payable = débito − crédito (Art. 64).
- Fixed-asset FRs (Art. 71-72 + Rgto. 26): transfers not hechos generadores **unless < 4 years in activo fijo (alta-date D15 anchor)**; fijo-acquisition crédito deductible same/future periods; **repairs + normal-deterioro + remodel-without-value/life-increase credits**; document routing (Factura/CCF if taxable else other doc); Art. 73 repealed note.
- Reorg FRs (Art. 7 g/h): aportes + modification/fusion transfers = transfers; liquidation/disminución adjudications NOT taxable when returned to the aportador-socio and not previously charged; establecimiento transfers = activo-realizable portion only.
**AC examples:** 4-month-old return rejected from the deduction (outside 3m); vencido-medicine return at month 20 passes with lot-registry validation and destruction act; late vendor ND booked in period+2; asset sold at year 3 = taxable transfer, at year 5 = not a hecho generador.
**OQs to carry:** SOQ-54; declaration-modification procedural config (D9 kin).

### Task 7: `sv/requirements/taxation/13_iva-retentions.md`

**Files:** Create `sv/requirements/taxation/13_iva-retentions.md`
**Covers:** V8
**Consumes:** T4 retention-credit release gates (by id).
**Evidence (scoped):** EV05 EVID-062 (`sv/.extractions/05_Codigo_Tributario.evidence.md` lines ~36-50) + **CT txt lines 3860-4030 (Arts. 161/162/162-A/162-B verbatim)** + EV01 W15 lines 231-244 (EVID-322 retention incisos) + 328-334 (EVID-336 Rgto. 23)

**Content requirements:**
- **CT 161 FRs:** import-of-services self-liquidation (the local acquirer owes IVA; mandamiento de ingreso; Art. 94-IV venues by id).
- **CT 162 FRs (verbatim-faithful matrix):** grandes contribuyentes buying from non-grand ⇒ **1% ex-IVA retention on ≥$100 operations**, entered same period (10 primeros días hábiles); AT-designated agents (state organs, municipalities, autonomous entities); grandes buying from uniones/sociedades de hecho ⇒ 1% regardless; **grandes/medianos buying caña/café/leche/carne or receiving financial-interest/lease/transport/dietas services from UNREGISTERED natural persons ⇒ 13%** (providers exempt from registration); retention at tax point; enter even if supplier unpaid; NC/ND adjustment path; MH lottery prizes 13%.
- **CT 162-A FRs:** card-issuer/administrator **2% perception ex-IVA** when paying/crediting affiliates; first-10-hábiles entero; affiliate credits it against the period's IVA (DCLE/ivaPercibido root — e-invoicing by id).
- **CT 162-B FR:** courts withhold 13% on interest in ejecutivo judgments.
- Excluidos-purchases 13% applicability FR (F-07 annex 5 H — **closes S3 03 OQ-004 by defining the CT-119/162-side regime the annex consumes**; fiscal-reporting by id).
- Retention-credit release tie-in (Art. 65 gate by id — declare+entero same period); F-930/F-07 annexes 9-12 as the reporting views (by id — no re-derivation); **ISR-side matrix (CT 154-160) stays taxation/04 by id — the two tracks never merge**.
**AC examples:** $150 purchase by a grande from a small supplier books 1% retention and a comprobante; unregistered caña seller triggers 13%; card payment books 2% perception creditable next period; services import self-liquidates via mandamiento.
**OQs to carry:** SOQ-54; AT-designation list config-gap; the CT-vintage note (CT copy Índice Legislativo edition, SOQ-21 kin).

### Task 8: `sv/requirements/taxation/14_iva-exports-refunds.md`

**Files:** Create `sv/requirements/taxation/14_iva-exports-refunds.md`
**Covers:** V9
**Consumes:** T3/T4/T5 (by id).
**Evidence (scoped):** EV01 W15 lines 266-286 (EVID-327..329) + 308-321 (EVID-333/335 Rgto. definitions) + 335-342 (EVID-337) + txt on demand (Ley pp. 37-40 = txt lines 1380-1495; Rgto. pp. 8 = txt lines 267-302)

**Content requirements:**
- Export-definition FRs (Art. 74 + Rgto. Art. 2-10): definitive transfers for foreign use; non-resident exclusively-abroad services; **connection/continuation/termination of foreign-originated services = 13% carve-out**; export test consumer (SR5 FR-095 by id).
- 0% rate FR (Art. 75) — the ZF/DPA TAN-sale routing authority (SR5 FR-087 by id; 12_ Art. 25 co-cite) and the LSI 75-77 route (SR3 by id).
- Credit FRs (Art. 76): export credits vs internal débito same period; excess ⇒ carryforward OR **offset vs retained/perceived/import-generated IVA + other direct taxes + fiscal obligations on request**.
- **Reintegro FRs (Art. 77 + Rgto. Art. 30):** request only after period declaration; complete-file rule (DGII instructivos); **30-day resolution clock + fiscalización suspension + sin-lugar-then-refile mechanics**; omiso/zero-declaration-modification gates; fehaciente evidence + purchases/sales/débitos/créditos detail in magnetic/printed media; **mixed exporters: proportion = exports/total-gravadas-ventas, refund capped at 13% of export value per customs documents; pure exporters: total credits same cap; unrefunded excess accumulates**; refund only for the export period (Rgto. 30); three-way purchase ledger (export/local/common) + monthly common-percentage distribution + Art. 66 adequacy for local exempt ventas; reintegro not renta gravable; F-07 casillas 115/523-524 consumer (by id).
- ZF/recintos export-equivalence FR (Rgto. Art. 29): documented via póliza de exportación/DM; **D.L. 461-1990 anchor stale — R30(a) note; substance via 12_ Art. 25 (SR5 by id)**.
**AC examples:** mixed exporter (exports 40% of gravadas) with 100 remanente linked to exports refunds ≤ 13% × export value, excess carries; connected-services invoice for a foreign telecom rated 13% not 0%; refund request blocked while omiso; January declaration required before the request.
**OQs to carry:** SOQ-54; DUCA/póliza terminology-drift note (modern DUCA-F SR6 by id); DGII instructivo formats config-gap.

### Task 9: `sv/requirements/taxation/15_iva-declaration-interfaces.md`

**Files:** Create `sv/requirements/taxation/15_iva-declaration-interfaces.md`
**Covers:** V10
**Consumes:** T1-T8 (by id — this file wires the feeds).
**Evidence (scoped):** EV01 W15 lines 105-112 + 287-300 (EVID-304/330/331) + txt on demand (Ley pp. 40-43/51-55 = txt lines 1500-1605 + 1840-2010)

**Content requirements:**
- Declaration FRs (Art. 93-94): monthly calendar period; declaración jurada content (gravadas/exentas/no sujetas + débito + crédito + remanentes traspasados); forms/online surface (F-07 by id); **10 primeros días hábiles filing+payment** (días-hábiles engine SV-FREP-FR-202..204 by id); agents' same-lap entero; **goods imports liquidated at Aduanas with customs taxes — payment constancy = comprobante de crédito fiscal (credit document)**; services imports at DGII/Tesorería; **no prórrogas ni facilidades (Art. 81-II)**; oficio-liquidation 2-month payment window (81-I).
- **Operation-classification interface FRs (the R/S + retention cross-ref fold-in):** the per-operation classification model (gravada-local/exenta/no-sujeta/0%-export/ZF-DPA-0/differentiated-fuel) that feeds F-07 annexes 1/2/3 buckets + the R/S Tipo-Operación/Tipo-Ingreso pair (S3 by id — classification FEED, codes 12/13 ISR-side kin) + débito/crédito casilla graph (F1 by id) + DTE tributo fields/CAT-015 (e-invoicing by id); MOQ-04 closure note (FOVIAL/COTRANS never in base nor charged — guard by id from T3).
- Version-regime rows: Art. 175 vigencia; transitorios 167-172 as historical notes (D18 is_historical kin); Art. 165 incorporation note; unconstitutional-arts note (113/123/124/161 — already repealed, historical note only).
- §5 version-regime note: the 01_/02_ print vintage (SOQ-54) + Decreto 321 kin pointer (dated regime rows owned by fiscal-reporting/05 by id).
**AC examples:** monthly declaration derives 100% from the ledgers (no manual casillas); import payment constancy accepted as the credit document for a goods import; a fuel sale at differentiated rate routes to annex 13 (by id) with base net of the FOVIAL tributo.
**OQs to carry:** SOQ-54; pre-DTE physical-invoice ingestion kin (D15 history contract); Decreto 321 kin pointer.

### Task 10: index + coverage + registry flips

**Files:**
- Modify: `sv/requirements/taxation/00_index.md` (retitle "Taxation (ISR + IVA)"; add files 07-15 rows; totals; the R30(b) numbering note; the consumer map)
- Modify: `sv/requirements/COVERAGE.md` (01_/02_ rows → per-file LB citations incl. new 07-15; rollup: 02_ pending row FLIPS to cited — final state 64 cited / 0 pending / 9 N/A / 1 superseded; 05_ row extended with 13_ retention cites)
- Modify: `sv/README.md` (taxation status note)
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (S9 delivered note + coverage totals)
- Modify: `sv/EXTRACTION_PLAN.md` (log entry: S9 synthesis COMPLETE)
- Modify cross-refs wired in-wave: `sv/requirements/taxation/02_isr-deductions.md` OQ-009 status → resolved-by-pointer (one-line edit, S1-precedent controller exception applies if trivial); `sv/requirements/fiscal-reporting/03_f07-annexes-purchases.md` OQ-004 + `02_f07-annexes-sales.md` OQ-002 status notes → point at the new SV-TAX ids (one-line edits each)

**Content requirements:** Index: file table (FR ranges 176..N), totals, numbering note (SV-TAX continuation per R30(b)), cross-topic consumer map (e-invoicing/fiscal-reporting/special-regimes/payroll/chart-of-accounts), OQ rollup in-file ↔ SOQ-54..58. COVERAGE flips with named citing files; numbering-continuity verification (`grep -o "SV-TAX-FR-[0-9]*" sv/requirements/taxation/*.md | sort -u` → contiguous 001..N, ISR files untouched 001-175); per-FR LB check (every FR row has an LB cell). Commit + push sv-research.

## Execution protocol

Per-task: fresh implementer subagent (reads this plan's Global Constraints + its task + its scoped evidence line-ranges fully + the ONE exemplar `06_isr-assets.md`; txts on demand via grep + bounded window) → controller review → reviewer subagent (verifies vs master index + evidence; numbering continuity; LB citations incl. SOQ-54 note; layer column; cross-refs by id; quote fidelity vs extraction txt — S5 ruling 37) → fix round if findings → commit. Final whole-wave review subagent → ONE fix wave → push. Rulings discovered in-wave recorded in fix commits + summarized for the sv/HANDOVER update BEFORE any workspace deletion. Tasks 1-9 STRICTLY sequential; Task 10 last. Structural verification commands per task (no repo test suite — S2 ruling 23): FR-id contiguity, per-FR LB presence, §1-§7 presence, OQ-table presence.
