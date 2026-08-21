# W18 SV Acquisition Follow-Ups Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Acquire the SOQ-register instruments queued in `sv/HANDOVER.md` §8.2, run the periodic external checks, and update the corpus memory — closing or date-stamping acquisition SOQs.

**Architecture:** Controller-run web-acquisition wave (W16 precedent: hunts + registration + SOQ verdicts; FR fold-ins are later waves). Route recipes are pinned facts verified live this session. Every task ends in a verifiable artifact: an acquired+registered+page-1-verified file, or a dated negative-hunt record in the SOQ register.

**Tech Stack:** curl (browser UA), `webfetch`, `shared/scripts/extract_text.py` (page markers), pypdf page-1 verification, `rg` over extracted text.

**Spec:** `sv/HANDOVER.md` §8 (next actions) + `sv/.extractions/00_MASTER_INDEX.md` SOQ register (SOQ-30..58) + `shared/docs/requirements-extraction-procedure.md` (Stage 1 + registry discipline).

## Global Constraints

- All work in worktree `.worktrees/sv`, branch `sv-research`. Short imperative commits, no emojis; push once at wave close; never force-push.
- **Official sources only.** Law-firm mirrors are NOT registrable (EVID-250 OQ-5 precedent). Provenance URL required per row.
- Registry numbering continues at **76**. Every acquisition: pypdf page-1 verify (factura.gob.sv wpdml-shuffle precedent), content-title-governs check (5 incidents: 29_/09_/15_/12_/31_), supersession notes.
- EVID corpus stands at 358. Same-wave evidence entries (if any) continue at 359+. Full reading passes for acquired laws are **deferred to a follow-up evidence wave** unless a SOQ verdict needs a targeted article read this wave.
- Value discipline: acquired values = dated data with instrument provenance; never arithmetic-derived. Watch-type SOQs close as dated negatives (SOQ-22/30-kin pattern: record what was checked, where, when).
- Route recipes (verified live 2026-08-21):
  - **D.O. API (PINNED this session):** `curl -d "year=YYYY&month=MM" https://www.diariooficial.gob.sv/api/v1/diarios-disponibles` (form-encoded; JSON keys fail) → `[{Id, FechaInicio, FechaInexacta, NombreArchivo}]` → PDF at `/seleccion/{Id}` (serves `application/pdf`, verified with Id 31505).
  - **uif.gob.sv:** plain GET + full browser UA; Incapsula blocks HEAD. Marco Legal = `https://www.uif.gob.sv/marco-legal/`.
  - **transparenciafiscal.gob.sv:** base redirects to `/ptf/es/`; direct PDFs at `/downloads/pdf/DC<id>_<slug>.pdf`; index is JS-opaque — discover via on-site search or factura.gob.sv/normativa links.
  - **MH formularios:** host is `www.mh.gob.sv` (`formularios.mh.gob.sv` does not resolve); wp-content direct URLs.
  - **asamblea.gob.sv:** still 000 — do not burn time there.
- OCR/D.O. recipe if scans needed: table pages PSM 4 at 400dpi, considerandos PSM 6; qpdf auto-repair for damaged PDFs; ghostscript pdfwrite rebuild for broken page trees.
- Wave close updates: `sv/EXTRACTION_PLAN.md` log + master-index SOQ register + `sv/HANDOVER.md` — all three, every close.

## Hunt register (targets → SOQs)

| # | Instrument | SOQ | Why | Primary routes |
|---|---|---|---|---|
| A | SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC 443-444 or successor) | 46 (gating) + cml/03 OQ-002 | who applies NIIF-PYMES vs full NIIF | Consejo/Colegio sites, transparenciafiscal, D.O., MINED |
| B | LESIA — Ley Especial para Sancionar Infracciones Aduaneras | 32 | customs sanction/expiry + defraudación elements | uif.gob.sv Marco Legal (customs found there ×2), transparenciafiscal, D.O. |
| C | Reglamento General Ley ZF (mandated by 12_ Art. 51) | 31 | solicitud/informe formats, DACG structures | uif.gob.sv, MINEC, transparenciafiscal, D.O. |
| D | Ley del Fondo de Conservación Vial D.L. 208-2000 (+ D.L. 597-2001) | 39 (FOVIAL half) | the $0.20/gal instrument text | D.O. API (Nov-Dec 2000, Oct-Dec 2001), fovial.gob.sv, transparenciafiscal |
| E | Ley COTRANS — Contribución Especial de las Empresas Transportistas de carga ($0.10/gal, CAT-015 C8) | 39 (COTRANS half; MOQ-04) | the $0.10/gal instrument text | same as D; DGA/DGM sites |
| F | $18-tasa adjusting Acuerdos Ejecutivos (74_ Art. 12-C biennial ≤10% since 2012) | 34 | current tasa value | D.O. scan (2013-2014 first window), DGA site, search |
| G | D.L. 598-2020 + EVID-167 tail laws | 41 | small-taxpayers transitory set | D.O. API (Dec 2020) |
| H | Current Reglamento IVA consolidation (post-D.E. 117-2001) | 54 Rgto side | vintage watch | transparenciafiscal DC catalog, MH |
| I | Art. 46-f DGII+BCR joint qualification instrument | 56 | financial-exemption flag | BCR site, D.O. 1990s, DGII |
| J | Art. 167-A "régimen de políticas sectoriales" instrument | 58 | kill-switch watch | search, D.O. |
| K | NIIF PYMES 2nd edition (2015) text | 48 (optional) | 2025-2027 vintage books | IFRS Foundation, source of 32_ (tuky) |
| L | SOQ-30 consolidation sweep: 12_/13_/14_/17b_/74_ post-cutoff prints | 30 | verification watch | transparenciafiscal, uif.gob.sv |
| M | DUCA user manual (Comité Aduanero) + Res. 409-2018 supersession status | 36 | mandatory-vs-optional field model | SIECA (www.sieca.int), DGA |

External checks (standing §8.4): factura.gob.sv LB drift; uif.gob.sv new AML reglamento; MH formularios (F-11 v19/v20, F14 v17 manual, F07 v15+); D.O. recipe record.

---

### Task 1: External-check sweep + D.O. recipe record

**Files:** Modify: `sv/HANDOVER.md` §6 (D.O. line), `sv/EXTRACTION_PLAN.md` (log), `sv/sources/README.md` (only if new MH files acquired).

- [ ] **Step 1: factura.gob.sv drift check** — GET `https://factura.gob.sv/normativa/`; compare Normativa (v2.0, 25-May-2026), Catálogos (v1.1 rev 07/2026), JSON schemas (2026-08-11), manual set vs HANDOVER §1 baseline. Any LB change → acquire (numbering 76+).
- [ ] **Step 2: uif.gob.sv AML watch** — GET `https://www.uif.gob.sv/marco-legal/` with browser UA; diff vs 71_/72_/73_ generation (new reglamento/instructivo under D.L. 426 → acquire; watch deadline 2026-10-17).
- [ ] **Step 3: MH formularios check** — locate the formularios page under `www.mh.gob.sv` (follow nav links; `formularios.mh.gob.sv` does not resolve); compare F-11 (v18), F-14 manual (v16 manual/v17 form), F-07 (v14), F-910 (v9), F-915 (v4), F-930 (v3), F-935 (v1), F-06 (v9), F-30 (v3), F-987 (v3). New versions → acquire (76+), page-1 pypdf verify, register.
- [ ] **Step 4: Record the D.O. recipe** — HANDOVER §6 D.O. entry gets: API = form-encoded `year`/`month` POST (JSON body 400s; keys are English), response `{Id, FechaInicio, NombreArchivo}`, PDF via `/seleccion/{Id}` (re-verified 2026-08-21).

**Verify:** findings (positive or dated-negative) captured for Task 8; acquisitions registered+verified.

### Task 2: SOQ-46 — NIIF-adopting instrument hunt (gating)

**Files:** possibly Create: `sv/sources/76_...` + registry row. Modify: master-index SOQ-46, HANDOVER §7.

- [ ] **Step 1: Identify the Council** — search "Consejo de Vigilancia de la Profesión de Contaduría Pública y Auditoría El Salvador" (CC Art. 435-444 names the watchdog; find its site/official gazette channel).
- [ ] **Step 2: Hunt the instrument** — in order: council site + its acuerdos/publications; Colegio de Contadores Públicos ( ccpces ); transparenciafiscal search "NIIF"/"Contaduría"; D.O. API scan of likely adoption windows ONLY if a dated lead exists; MINED/CNR. Keywords: "Normas Internacionales de Contabilidad", "NIIF", "Contabilidad", "auditoría", "Consejo de Vigilancia".
- [ ] **Step 3: Verdict** — found: acquire (76+), page-1 verify, register, SOQ-46 → resolved-pending-read (evidence next wave). Not found: dated negative record (routes checked, dates, negative signals) — SOQ-46 stays open as external watch.

### Task 3: SOQ-31/32/30/36 — LESIA + Reglamento General ZF + consolidation sweep + DUCA manual

**Files:** possibly Create: `sv/sources/7x_...` + rows. Modify: master-index SOQ-30/31/32/36.

- [ ] **Step 1: uif.gob.sv Marco Legal full index** — GET the marco-legal page(s); enumerate ALL law titles; grep for "Aduaneras" (LESIA), "Zonas Francas" (reglamento), "Simplificación"/"Orgánica de Aduanas"/"Servicios Internacionales" (SOQ-30 newer prints). Acquire hits.
- [ ] **Step 2: transparenciafiscal sweep** — on-site search per law name (12_/13_/74_/LESIA/Rgto-ZF); DC-catalog PDFs; compare reform tails vs corpus cutoffs (12_→D.L. 318-2013, 13_→D.L. 121-2012, 74_→D.L. 23-2012, 14_→S/R).
- [ ] **Step 3: SIECA DUCA hunt (SOQ-36)** — www.sieca.int (Comité Aduanero / DUCA / instructivo section); look for the user manual (mandatory-vs-optional field list) + any resolution superseding COMIECO Res. 409-2018; acquire official SIECA/COMIECO PDFs only.
- [ ] **Step 4: D.O. fallback for LESIA/Rgto-ZF only if a dated lead emerges** (decree number/year); bound the blind scan accordingly.
- [ ] **Step 5: Verdicts** — per instrument: acquired (register, page-1 verify, supersession notes) or dated negative. SOQ-30: newer-consolidation found → acquire + note; else negative-signal refresh with this wave's date. SOQ-36: manual found → register + note; Res. 409-2018 supersession signal recorded either way.

### Task 4: SOQ-39 — FOVIAL + COTRANS instruments

**Files:** possibly Create: `sv/sources/7x_...` + rows. Modify: master-index SOQ-39, MOQ-04.

- [ ] **Step 1: Non-D.O. routes first** — fovial.gob.sv (legal/normativa section), transparenciafiscal ("Conservación Vial", "Transportistas"), uif.gob.sv, DGA/DGM (Gobernación) for COTRANS; MOP/MOPUT.
- [ ] **Step 2: D.O. API hunt D.L. 208-2000** — enumerate Nov+Dec 2000 (`year=2000&month=11`, `=12`); fetch candidates; `pdftotext` + rg "Fondo de Conservación Vial" / "208". Note: D.O. issues are full-volume PDFs — extract to scratch, never commit extractions.
- [ ] **Step 3: D.O. API hunt D.L. 597-2001** — same over Oct-Dec 2001, rg "597".
- [ ] **Step 4: COTRANS hunt** — rg corpus first for its full printed name (40_/31_ anchors); then D.O. windows around the FOVIAL reform era (2001-2002) + search engines; COTRANS admin route (Viceministerio de Transporte).
- [ ] **Step 5: Verdicts** — acquired → register (76+), page-1 verify, note reform tails; else dated negatives. MOQ-04/COTRANS + SOQ-39 register rows updated.

### Task 5: SOQ-41/34 — D.L. 598-2020 + $18-tasa acuerdos

**Files:** possibly Create: `sv/sources/7x_...` + rows. Modify: master-index SOQ-34/41.

- [ ] **Step 1: D.O. Dec-2020 enumeration** — API `year=2020&month=12`; daily PDFs; rg "598" + "pequeños contribuyentes" candidates; verify decree identity on page 1.
- [ ] **Step 2: EVID-167 tail laws** — from `54_` evidence (EVID-167 = reform-chain tail list): identify any remaining named-but-absent instruments; acquire the ones D.O. can serve.
- [ ] **Step 3: $18-tasa acuerdos** — search engines + DGA site for Acuerdos Ejecutivos under D. 529 Art. 12-C ("tasa", "inspección no intrusiva", "dieciocho dólares"); D.O. blind scan ONLY the 2013-2014 first biennial window if search fails; bound: stop after one window + record negative.
- [ ] **Step 4: Verdicts** — SOQ-41 closed by acquisition or dated negative; SOQ-34: acuerdo found → targeted read of the value article (same-wave verdict OK, cite EVID-359+ if recorded) or stays config-with-2012-provenance + dated negative.

### Task 6: SOQ-54 Rgto / 56 / 58 / 48 — S9 rides + optional

**Files:** possibly Create: `sv/sources/7x_...` + rows. Modify: master-index SOQ-48/54/56/58.

- [ ] **Step 1: Rgto IVA consolidation** — transparenciafiscal + MH search "Reglamento" + "Transferencia de Bienes Muebles"; check for a post-117-2001 consolidated print (negative signals so far). Verdict updates SOQ-54 Rgto side.
- [ ] **Step 2: Art. 46-f instrument** — BCR site (normativa/compilación), D.O. 1990s ONLY with a dated lead; expected negative → dated watch record; SOQ-56 stays config-gap.
- [ ] **Step 3: Art. 167-A instrument** — search "régimen de políticas sectoriales" agua/alcantarillado; expected not-yet-issued → refresh watch date on SOQ-58.
- [ ] **Step 4: NIIF PYMES 2nd ed (optional)** — IFRS Foundation site (32_ source); if paywalled/registration-walled, record negative and close SOQ-48 as optional-not-acquired.

### Task 7: Registration + verification pass (all acquisitions)

**Files:** Create/Modify: `sv/sources/*`, `sv/sources/README.md`.

- [ ] **Step 1:** For each acquired file: pypdf page-1 identity check (title, decree number, D.O. anchor), content-title-governs check vs registry row, provenance URL + retrieval date, supersession/notes.
- [ ] **Step 2:** Registry rows numbered 76+ in acquisition order; numbering gaps never back-filled.
- [ ] **Step 3:** Decide evidence disposition per instrument: same-wave identity EVID (EVID-359+) only where a verdict needed it; full passes → W19 backlog list in the wave log.

### Task 8: Bookkeeping + push

**Files:** Modify: `sv/EXTRACTION_PLAN.md`, `sv/.extractions/00_MASTER_INDEX.md`, `sv/HANDOVER.md`.

- [ ] **Step 1:** EXTRACTION_PLAN W18 log entry (finds, verdicts, route intel).
- [ ] **Step 2:** Master index: SOQ register verdicts + Build note line.
- [ ] **Step 3:** sv/HANDOVER.md: §1 corpus status, §5 wave log summary, §6 gotchas (route facts incl. D.O. recipe), §7/§8 refresh.
- [ ] **Step 4:** Commit all + push `sv-research`. Merge decision stays with owner. COVERAGE untouched (no new LB citations this wave; registered-but-uncited sources enter COVERAGE at their evidence/fold-in wave — W16 precedent used same-wave citation, W18 has none).

## Self-review notes

- Spec coverage: HANDOVER §8.2 S7/S8/S9 acquisition items → hunts A-M (all present; SOQ-36 = hunt M/Task 3 Step 3); §8.4 external checks → Task 1; §8.3 numbering-76 → Global Constraints + Task 7; §8.6 close bookkeeping → Task 8.
- Placeholder scan: none; every step carries its route/recipe/rg-pattern.
- Consistency: numbering single stream 76+; EVID continuation only via Task 5/7 rule; no plan step touches requirements/ files (no FR changes in W18).
