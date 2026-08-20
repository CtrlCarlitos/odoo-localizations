# HANDOVER — Honduras Session State & Continuation Guide

**For the next HN controller session.** Written 2026-08-20 after W1 (taxation
core), updated through round-4/D-H2/D-H3 + the merge, W2 fiscal-reporting, W3
facturación, W4 payroll, and **synthesis prep (this refresh — master index +
OQ registers done)**. Read this fully before acting; it is the authoritative HN
cross-session memory (conversation context does not survive). Update it at every
session boundary.

**Bootstrap prompt for a fresh session:** `Read hn/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/hn-research`, branch `hn-research`. **Merges to
  date: 2026-08-19 (W1) and 2026-08-20 (W2, W3 at `c1f9fa8`, W4 at `d5a2f4b`,
  and synthesis prep at `e106b1f` — rebase-then-merge per root HANDOVER §4.6,
  owner-executed; main carries HN evidence through EVID-333 + the master
  index = ALL FOUR evidence waves + synthesis prep).**
  The cross-country canon D15-D19 was adopted at the W1 merge — HN's
  D-H2/D-H3 are country instantiations of D16/D18 (see
  `shared/docs/regulatory-change-management.md`,
  `shared/docs/go-live-readiness.md`). **Country work model (binding):** every
  country works in its own branch+worktree; `main` = integration; merge at
  milestones by owner decision. NEVER touch `sv/`, `gt/`, or root
  `HANDOVER.md` from this branch; `hn/` + specs are ours.
- **Mission:** bootstrap the Honduras Odoo localization per
  `docs/superpowers/specs/2026-08-18-hn-source-research-design.md`
  (e-invoicing IN scope; acquire+register; evidence waves authorized by the
  phase-extension note in that spec). Procedure:
  `shared/docs/requirements-extraction-procedure.md`.

## 2. Read order for a new session

1. THIS file
2. `hn/EXTRACTION_PLAN.md` — wave log (W1a-W1f taxation + W2a/W2b fiscal
   reporting + W3 facturación + W4 payroll + **synthesis prep DONE — master
   index built**; EVID-001..333), reading order, risks, **Decisions (D-H1/
   D-H2/D-H3 binding; D-H2/D-H3 = D16/D18 instantiations)**
3. **`hn/.extractions/00_MASTER_INDEX.md` — THE synthesis lookup (built
   2026-08-19): authority orders per topic, 18 EV file keys, 43 clusters
   (T1-T12/F1-F11/E1-E8/P1-P12) with Governing EVIDs/LB/crossrefs, R-H1..65
   resolved-contradictions ledger, OQ registers C1-C4 (~227 open), S-wave
   plan. READ BEFORE ANY SYNTHESIS WORK.**
4. `hn/RESEARCH.md` — research dossier: sites, fetch recipes (§6), hint
   layer w/ corpus verification (§7), open leads (§5, incl. W2+W3+W4
   harvests)
5. `hn/sources/README.md` — registry, 103 files (01-104, 103 reserved-unused),
   full provenance + mislabel-correction notes (**9 incidents to date**)
6. Evidence files in `hn/.extractions/*.evidence.md` (committed): `01_`
   (ISR, EVID-001..015), `02_` (ISV, 016..026), `03_` (CT, 027..038),
   `04-21-22_` (D.17-2010 family, 039..053), `07-12+11_` (tables+plantilla,
   054..056), `05+23+79+80_` (taxation closers, 057..071),
   `13-20_fiscal-procedures.evidence.md` (W2a, 072..090),
   `29+30+46-49+68+74+75_ISR-annual.evidence.md` (091..110),
   `31-42+71_retenciones.evidence.md` (111..129),
   `43-45+69+70+72+73_ISV.evidence.md` (136..150),
   `50-55_selectivo.evidence.md` (151..158),
   `56-62_contribuciones.evidence.md` (163..173),
   `63-67_informativas.evidence.md` (175..185),
   `24-26+76-78_facturacion.evidence.md` (W3, 186..214),
   `82-84+90-92+101+102+104_salario-minimo-13-14.evidence.md` (W4a, 215..240),
   `81+87+88_IHSS.evidence.md` (W4b, 250..274),
   `27+28_RAP-fondo.evidence.md` (W4c, 275..289),
   `85+86_codigo-trabajo.evidence.md` (W4d, 295..333). **EVID numbering is
   corpus-global, next = 334. OQs are per-file/per-doc at evidence-file end
   (~227 open).**

## 3. State: corpus (research phase COMPLETE)

100 registered files, every one page-1 verified; 103 on disk (01-104, gap
103 reserved-unused for D. 112 — SAR routes exhausted 2026-08-20, see
RESEARCH §5). Structure:
- **Laws/consolidations:** ISR D.L. 25 (`01_`, hasta SAR-07-2025), ISV
  D.L. 24 (`02_`, hasta D.L. 59-2022), CT D. 170-2016 (`03_`, hasta
  D. 180-2020), D. 17-2010 + Reglamento 1121-2010 + D.28-2019 interp
  (`04_/21_/22_`), Ley Eficiencia D. 113-2011 (`05_`)
- **ISR tables FY2022-2026** (`12/10/09/08/07_`) + **plantilla 2026**
  (`11_` XLSX = the withholding computation contract)
- **Fiscal reporting:** DJIMR SAR-238-2024 (`14_`), DMC chain
  (`15/16/17/20_`), tarjetas mods (`19_`), compras eventuales (`18_`),
  EEFF SAR-619-2024 (`13_`), 42 per-código Ayudas/Generalidades (`29-75_`)
- **Facturación:** Acuerdo 481-2017 consolidado (`24_`) + 189-2014 hist
  (`25_`) + 817-2018 (`26_`) + workflow helps (`76-78_`)
- **Payroll (W4-complete):** IHSS D. 48-2024 (`81_`, rates OCR'd) + Ley
  IHSS (`87_`, OCR'd — native layer junk) + incapacidad (`88_`); RAP fondo
  D. 47-2024 (`27_`) + D. 40-2026 (`28_`); salario mínimo bienios 2023
  (`83/84_`), 2024-2025 (`82_`), **2026-2027 CURRENT (`90_` OCR'd + `91_`
  tabla + `92_` bono + `101_` 2022/2023 vintages + `104_` D.103 machinery +
  `102_` 14th-month reglamento)**; CT D. 189-1959 (`86_`, vintage through
  D.278-2013) + **85_ = D.93-2021 PENAL-side derogations only (9th mislabel
  — NOT CT, no CT gap ever existed)**
- Misc: amnistía D. 7-2026 (`06_`), ISR reforms (`79/80_`), Adulto Mayor
  family (`95/96_`), 22-A chain (`80/93_`), selectivo IPC chain
  (`98/99/100_`), ISR-reglamento ancestor 464-1990 (`94_`), D.194-2002
  original (`97_`). LJT still unapproved (Sep-2025 newest SAR post).

## 4. Key findings (do not re-derive)

- **E-invoicing reality:** NO national XML/DTE regime. Paper regime
  (CAI/rango/vigencia, Arts. 59-61) administered digitally + a statutory
  **Sistema de Emisión Electrónica (SEE) with per-document CAEE** (Arts.
  50-58, gradual mandatory incorporation per SEFIN calendarización) —
  technical docs NOT public (lead 1). D. 17-2010 L-Art 57 = regime's
  statutory birth.
- **Document taxonomy (Arts. 5-8)**: Comprobantes Fiscales (Factura,
  Prevalorada, Ticket, Recibo Honorarios, Boleta Compra, Constancia
  Donación) / Documentos Complementarios (NC, ND, Guías Remisión,
  Comprobantes Retención) / Otros. 16-digit correlativo =
  establecimiento(3, matriz=000)+punto de emisión(3)+tipo doc(2)+consecutive(8,
  wraps 99999999).
- **Withholding:** asalariados = annualize→deduct→table→÷months (plantilla);
  composite L257,493.16 sole-source gate; 12.5% services; 1% compras
  anticipo (retainer >L15M); OTCD cards 10%-of-tax/15% fallback; non-resident
  gross table 25/10 (current = `01_` Art. 5).
- **Rates:** ISR PJ 25%, PN 15/20/25 IPC-indexed annually; 22-A gross-minimum
  (≤L1B excluded, 1%/0.5% sectors); ISV 15%/18%/0; mora 3%/mo cap 36%;
  prescription 4/5/7y; multas = income-range × SMM-promedio fractions +
  ISR-late 5→25%/month escalator.
- **W2 fiscal reporting (do not re-derive):** Form 535 EEFF-prior gate from
  FY2024 (SAR-619-2024); DJIMR = monthly informativa PER retention código
  (25-code catalog), 10 días calendario, rectificativa auto-rectifies the
  determinativa; DMC = form 527, deadline **5 días calendario
  (SAR-237-2024)**; tarjetas 523 (SW informativa) + 215 (OVI determinativa,
  base = 10% of ISV − devolución 8%) file OUTSIDE the DJIMR catalog;
  compras eventuales = doc type 10 buyer-issued (rate unpinned — OQ);
  TP pequeños excluded ≤USD 1M; AS = 5% RNG>L1M (PJ-only), ATN = minimum tax
  over L3M exemption, both D.51-2003 (un-acquired — TOP lead);
  contribuciones: 504 1% / 502 1% / 503 0.5% monthly, 506 3.6% / 509 15%+0.5%
  floor / 511 15% / 107 10% annual; selectivo 203 = separate D.58-1982 tax;
  259 = 4% turística retention.
- **W2 conflicts (open OQs — never resolve silently):** GC non-resident
  retention 2% (46_) vs 4% (05_ Art. 14); ZOLITUR Art. 4 vs Art. 25; DMC
  manuals "8 días" vs gazette 5 (5d = record); 506-vs-509 cooperative
  boundary; 39_ ≡ 37_ (both código 135).
- **W3 facturación (do not re-derive):** D-H1 FR cluster evidence-complete.
  16-digit correlativo grammar + wrap rule; type codes 01/03(Ticket machine
  prefix 09)/04/05/06/07/08/10(Prevalorada)/11/12, **02 unassigned**;
  **code-10 collision: DEI-279-2015 "10 = Compras Eventuales" (introduced
  the 16-digit grammar) vs 481-2017 "10 = Prevalorada" — OQ-2, never
  implement 10 as both**; 189-2014 = 14-digit grammar → dual historical
  parser; CAI ledger contract (Arts. 59-63): per punto × doc type, ONE active
  rango, renewal T-2mo, vigencia ≤1y, consumo starts at Activada; emission
  gate = momento-de-emisión earliest-of (Art. 14) + vigencia/fecha límite;
  two-layer print contract; L50 consolidation (imprenta only); L10,000 ID
  threshold (SEFIN-modifiable, dated row); boleta compra 5%-of-opex +
  per-provider caps, no crédito; NC/ND origin triple; guía 12-motivo + SAR
  copy; retención comprobante at hecho generador (patronos exempt unless
  requested, EVID-200); no-utilizados 12 causes/10 días hábiles; topologies
  centralizado/regional/sucursal; SEE/CAEE = medium of autoimpresor, docs
  unpublished (lead 1); helps' Base-Legal sections defective — cite the
  reglamento.
- **W4 payroll (do not re-derive):** IHSS matrix = **IVM 3.5% employer /
  2.5% worker / 0.5% State (81_ Art. 1) + EM 5%/2.5%/0.5% (87_ Art. 55-A) ⇒
  worker 5.0%, employer 8.5%**; TWO regime ceilings (2024: 11,336.32 IVM /
  11,109.30 EM; 2025: both 11,903.13 — coincidence, not merger); post-2025 =
  JD per actuarial study (dated rows); "porcentajes sobre los techos" =
  drafting ambiguity, coherent reading min(salario, techo) per 55-B;
  **contribution BASE (13th/14th/OT inclusion?) delegated to unacquired
  Reglamento General — config flag, TOP lead**; riesgos profesionales rate
  not in corpus; incapacidad: NO cuarentena — days 1-3 employer salary,
  4-365 IHSS 66% + mandatory employer complement (RIT 71/73). RAP side:
  **STACKED fondo 4% + RAP 1.5% employer (=5.5%) + worker 1.5% retention
  above IVM techo, ≤15 días entero; base "salario ordinario" undefined in
  law (OQ); ceiling 3× top-SMM (instrument unnamed, OQ); fondo coexists-
  with-offset vs CT cesantía (despido injusto: compute, deduct saldo, pay
  excess; other causes: fondo 100% prima + 35%/75% complement floors, CT
  Art. 120 lit. f); vigencia 28-may-2024, no retro**. Ley RAP = doubly
  load-bearing (truncated transcription). SMM: bienio 2026-2027 % 6/6/7/7
  (2026) · 6/6/7/7.5 (2027), full tables pinned; 2027 IPC-escalator
  de-oficio + Jan-Apr-2026 retroactivity; **promedio ONLY in DGS companion
  tables (2026: L14,917.20 → 10×SMM cap L149,172; NOT the table mean — never
  recompute); 2025 (L13,985.16) + 2027 promedios NOT in corpus = OQ +
  DGS-print lead**; 14th month (102_): June, 30-jun year-gate 100%-else-
  proportional, average-of-ordinary-salaries base, small-employer SMM-average
  variant, proportional on exit; bono educativo ≤2×SMM, ≤15-worker
  exemption, non-salary. CT: **NO aguinaldo in the CT — D. 135-94 special
  law (TOP lead; subsumes D. 112)**; vacaciones Arts. 345-356 (10/12/15/20
  días laborables at 1/2/3/4+y; 6-month ordinary average ÷ days worked; no
  360 divisor CT-side); preaviso 24h/1w/2w/1m/2m; cesantía 10d/20d/1mo/yr +
  fraction, cap 25 months (15 for micro ≤10), ≥15y vol-quit 35% / death 75%,
  last-6-month average base; jornada diurna 8h/44h-worked paid-48, nocturna
  6h/36h +25%, OT ×1.25/×1.50/×1.75, ≤12h/day, OT ≤4×/week, planillas book
  OT separately; maternity 4+6w at 180-day average + top-up, nursing
  2×30min, unauthorized firing = 60 days + 10 weeks + 2× rests; **NO general
  final-pay deadline in CT (negative — LB elsewhere)**; extra finds: Art.
  95.12-13+60-A mandatory union/non-union/coop deductions; Art. 104 sickness
  half-pay schedule; 10 paid feriados ÷6 average + collision rule; Art. 368
  pay-frequency caps; "salario completo" (ord+OT) indemnity base; Libro de
  Salarios (Art. 380). **85_ = 9th mislabel: D.93-2021 derogates PENAL
  (D.130-2017, 31 arts) + CPP + Lavado — ZERO CT articles; penal numbers
  collide with LIVE CT payroll articles — guard table EVID-333.**
- **Decisions:** **D-H1** (binding, EXTRACTION_PLAN): one journal per company
  via `l10n_latam_invoice_document`; sequence key = (establecimiento→
  `stock.warehouse`, punto de emisión→child emission point, doc type→
  `l10n_latam.document.type`); emission point NOT on journal;
  user↔emission-point matrix = operational FR only. **D-H2** (2026-08-20,
  binding): temporal validity — dated rows resolved by HECHO-GENERADOR/
  period date; payroll key = (payslip period, worker attributes,
  birthday-year rules); HARD BLOCK emission outside CAI vigencia; historical
  = flagged read-only imports; payroll corrections recompute with
  ORIGINAL-period rows; filed periods write-protected; regime cutovers =
  dated config rows. **D-H3** (2026-08-20, binding): go-live ingestion =
  current-FY fiscal-document detail (read-only, original CAI numbers/dates) +
  prior-years aggregates; reconcile vs PREVIOUS system's SAR filings;
  payroll = monthly aggregates per contract (hire-date depth fondo/cesantía/
  vacaciones, FY-start depth ISR/13th/14th); stock/banks = opening balances.

## 5. Gotchas & verified lessons

- **Wrong-domain sites:** congresonacional.gob.hn / stss.gob.hn / upap.gob.hn
  / cpmcp.hn / enag.hn = NXDOMAIN. Real: `congresonacional.hn` (no law
  library), `www.trabajo.gob.hn` (STSS WordPress), **`enag.gob.hn` = Gaceta
  Digital 2015-2026** (recipe: `/index.php/gaceta-digital/<year>/<mes>` →
  `/index.php/gaceta-digital/<id>/download`). TSC biblioteca fully crawled.
- **SAR downloads:** resolve fresh wpdmdl from `/download/<slug>/` page
  (tokens rotate); some slugs dead. **SAR REST search endpoint works
  (wp-json/wp/v2/search) but only indexes posts/pages — validated empty for
  aguinaldo/séptimo día while returning hits for salario; absence of results
  ≠ absence on site (catalog crawl is the real check).**
- **OCR (proven recipes):** scanned gazettes OK at default PSM 6; TABLES
  need `gs -r400 pnggray` + `tesseract --psm 4` (proven on tabla acuerdos +
  91_/92_ rama columns); mojibake text layers (81_ rates, 90_ full, 87_
  font-mangled) re-covered by PSM 6 at 400dpi — sidecar `.OCR.txt` files
  live in hn/.extractions/ and are the AUTHORITATIVE text for those pages.
  102_'s run-on damage is legible as-is.
- `11_` plantilla formulas read fine via openpyxl (not protected).
- IHSS site needs full browser UA. Bing/DDG useless for .hn; navigate
  catalogs directly.
- **Registry glosses and catalog TITLES can mislead — 9 incidents to date**
  (29_/09_/15_ SV; 05_, 94_, 101_-server-filename, 20_, 52_, **85_** HN —
  85_ was believed "CT derogations" for two sessions before W4d read it:
  Penal-only. Title ≠ content; the end-to-end read is the authority. Numeric
  article collisions across codes (Penal vs CT) make "derogates Art. N"
  claims worthless until the code is named in the text.)
- **Manuals can be stale vs gazettes (W2b):** the gazette text is the
  record; flag manual conflicts as OQs. Same class: 101_ p.4 caption
  misprints the 2023 table as "AÑO 2022"; 102_ p.1 prints D. 135-94 "de
  fecha 12 de Octubre de 1991 [sic]" (print error for 1994).

## 6. Next actions (ordered)

1. **S-waves (NEXT):** topic synthesis per the SV subagent pattern, planned in
   `00_MASTER_INDEX.md` coverage section — **S-HN1 taxation (T1-T12) first
   (everything cites it), S-HN2 e-invoicing (E1-E8; SEE/CAEE sub-cluster
   blocked on lead 1) parallel-able, S-HN3 fiscal-reporting (F1-F11, needs
   S-HN1 rates), S-HN4 payroll (P1-P12, needs S-HN1 retention interfaces;
   aguinaldo FRs config-gapped until D. 135-94 lands)**; S-HN5 thin closes
   (chart-of-accounts/commercial-legal) decided at milestone. Requirements
   files land in `hn/requirements/<topic>/` mirroring SV. Synthesis consumes
   the master index (clusters + R-ledger + OQ registers) — never re-derives
   evidence; cite `EVxx:EVID-nnn`. Acquisition waves interleave (config
   flags/OQs open, never blocked except SEE).
2. **Acquisition queue (W2+W3+W4 lead harvests, RESEARCH §5 + master-index
   C-registers):** TOP = **D. 135-94 + Acuerdo 201-96 (aguinaldo/compensación
   social — the 13th-month statutory home; P2 blocker)** + **Reglamento
   General IHSS (contribution-base definition)** + **Ley RAP D.L. 107-2013
   (doubly load-bearing)** + Ley Equidad Tributaria D. 51-2003 (AS/ATN +
   tarjetas Art. 18) + Acuerdo SAR-236-2024 + Reglamento Ley ISR ("Acuerdo
   N°799") + DGS SMM companion prints (2022-2025 + 2027 when exists) +
   D. 58-1982 + D. 131-98 + TP family (D. 232-2011 + 027-2015 +
   DEI-SG-004-2016) + contribuciones statutes + D. 54-95 + Código de
   Comercio + DEI-9382-J-2003 I-VIII + W3 adds (462-2014, 424-2018,
   post-2017 compras-eventuales instrument if any) + riesgos-profesionales
   reglamento. D. 112 = routes exhausted (mirror-only at synthesis).
   Most SAR-catalog fetchable (recipe §6).
 3. **Merge to main at milestone:** owner decision; rebase-then-merge; never
    force-push (root HANDOVER country model). **Synthesis prep merged
    2026-08-19 at `e106b1f` — branch and main are level; future waves branch
    from here.**

Session state at stop (2026-08-19, synthesis prep close): evidence COMPLETE
through EVID-333 (~227 open OQs); corpus 103 files; W1+W2+W3+W4 committed and
merged (d5a2f4b); **master index built (43 clusters, R-H1..65, OQ registers
C1-C4, S-wave plan); next = S-HN1 taxation synthesis (or S-HN2 in parallel).**

## 7. Conventions (mirroring SV)

- Evidence: verbatim Spanish + gloss; candidate CRs + topic tags; doubts →
  OQs, never guesses. Per-file OQ numbering; corpus-global EVID (next=334).
  W2b + W4 ran subagent-dispatched with pre-allocated EVID ranges per
  family — proven pattern for large batches; controller verifies ranges +
  spot-checks verbatims afterward (done for W4: ranges + 8 source-level
  spot-checks incl. all OCR-derived quotes).
- `.gitignore`: `hn/.extractions/*` ignored EXCEPT `*.evidence.md` +
  `00_MASTER_INDEX.md` (**created 2026-08-19 — committed; update it at every
  wave/milestone that adds EVIDs, rulings, or resolves OQs**).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from `105` (103 reserved-unused);
  page-1 verify everything. **9 mislabel incidents to date** — title-vs-
  content discipline on EVERY acquisition AND every evidence read.
- **Manuals can be stale vs gazettes (W2b):** gazette text is the record.
- **OCR sidecars:** for any file with an `.OCR.txt` in `.extractions/`, the
  OCR sidecar (not the native-layer txt) is authoritative for the damaged
  passages (81_, 87_, 90_, 91_, 92_ as of W4).
