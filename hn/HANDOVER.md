# HANDOVER — Honduras Session State & Continuation Guide

**For the next HN controller session.** Written 2026-08-20 after W1 ( taxation
core), updated same day after round-4/D-H2/D-H3 + the merge, and again after
the W2 fiscal-reporting wave (this refresh). Read this fully before acting; it
is the authoritative HN cross-session memory (conversation context does not
survive). Update it at every session boundary.

**Bootstrap prompt for a fresh session:** `Read hn/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/hn-research`, branch `hn-research`. **The 2026-08-19
  merge happened** (hn-research → main, rebase-then-merge; owner-executed) and
  the cross-country canon D15-D19 was adopted — HN's D-H2/D-H3 are country
  instantiations of D16/D18 (see `shared/docs/regulatory-change-management.md`,
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
2. `hn/EXTRACTION_PLAN.md` — wave log (W1a-W1f taxation + **W2a/W2b fiscal
   reporting DONE** — EVID-001..185), reading order, risks, **Decisions
   (D-H1/D-H2/D-H3 binding; D-H2/D-H3 now also D16/D18 instantiations)**
3. `hn/RESEARCH.md` — research dossier: sites, fetch recipes (§6), hint
   layer w/ corpus verification (§7), open leads (§5, incl. W2 lead harvest)
4. `hn/sources/README.md` — registry, 103 files (01-104, 103 reserved-unused),
   full provenance + mislabel-correction notes (8 incidents to date)
5. Evidence files in `hn/.extractions/*.evidence.md` (committed): `01_`
   (ISR, EVID-001..015), `02_` (ISV, 016..026), `03_` (CT, 027..038),
   `04-21-22_` (D.17-2010 family, 039..053), `07-12+11_` (tables+plantilla,
   054..056), `05+23+79+80_` (taxation closers, 057..071),
   `13-20_fiscal-procedures.evidence.md` (W2a, 072..090),
   `29+30+46-49+68+74+75_ISR-annual.evidence.md` (091..110),
   `31-42+71_retenciones.evidence.md` (111..129),
   `43-45+69+70+72+73_ISV.evidence.md` (136..150),
   `50-55_selectivo.evidence.md` (151..158),
   `56-62_contribuciones.evidence.md` (163..173),
   `63-67_informativas.evidence.md` (175..185). **EVID numbering is
   corpus-global, next = 186. OQs are per-file/per-doc at evidence-file end
   (~160 open).**

## 3. State: corpus (research phase COMPLETE)

100 registered files, every one page-1 verified. Structure:
- **Laws/consolidations:** ISR D.L. 25 (`01_`, hasta SAR-07-2025), ISV
  D.L. 24 (`02_`, hasta D.L. 59-2022), CT D. 170-2016 (`03_`, hasta
  D. 180-2020; post-2020 = only `89_` D.117-2021 interp + `23_` Art. 206
  void), D. 17-2010 + Reglamento 1121-2010 + D.28-2019 interp
  (`04_/21_/22_`), Ley Eficiencia D. 113-2011 (`05_`)
- **ISR tables FY2022-2026** (`12/10/09/08/07_`) + **plantilla 2026**
  (`11_` XLSX = the withholding computation contract)
- **Fiscal reporting:** DJIMR SAR-238-2024 (`14_`), DMC chain
  (`15/16/17_`), tarjetas/retenciones mods (`19/20_`), compras eventuales
  (`18_`), EEFF SAR-619-2024 (`13_`), 42 per-código Ayudas/Generalidades
  (`29-75_`)
- **Facturación:** Acuerdo 481-2017 consolidado (`24_`) + 189-2014 hist
  (`25_`) + 817-2018 (`26_`) + workflow helps (`76-78_`)
- **Payroll:** IHSS rates D. 48-2024 (`81_`), RAP fondo D. 47-2024 +
  D. 40-2026 (`27/28_`), Ley IHSS (`87_`, scanned), Incapacidad Temporal
  (`88_`), **salario mínimo bienios**: 2023 (`83/84_`), 2024-2025 (`82_`),
  **2026-2027 SETRASS-233-2026 + tables (`90/91/92_` — CURRENT)**, CT D.
  189-1959 (`86_`), D. 93-2021 derogations (`85_` = Gaceta 35,760 full)
- Misc: amnistía D. 7-2026 (`06_`), ISR reforms (`79/80_`)
- **Lead-dig round 5 (2026-08-20, W2 wave-start):** `101_` = STSS-308-2022
  (G35,892 extract — the 14th-month SMM instrument; server filename said
  "STSS-38-2022", 6th mislabel), `102_` = Acuerdo 02-95 Reglamento Décimo
  Cuarto Mes (statutory origin **D. 135-94 Art. 34** — closes the W1
  "labor-side 14th-month instrument" question), `104_` = D. 103 Ley Salario
  Mínimo. **103 reserved-unused** (D. 112 aguinaldo law: STSS href dead-404,
  no Wayback — open lead, SAR-republish route). Corpus = **103 files
  (01-104, gap 103)**; next number 105. LJT still unapproved (Sep-2025
  newest SAR post). SEFIN search dead for 461-2020 (3rd dead end).

## 4. Key findings (do not re-derive)

- **E-invoicing reality:** NO national XML/DTE regime. Paper regime
  (CAI/rango/vigencia, Arts. 59-61) administered digitally + a statutory
  **Sistema de Emisión Electrónica (SEE) with per-document CAEE** (Arts.
  50-58, gradual mandatory incorporation per SEFIN calendarización) —
  technical docs NOT public (lead #1). D. 17-2010 L-Art 57 = regime's
  statutory birth (already said "factura electrónica" in 2010).
- **Document taxonomy (Arts. 5-8)**: Comprobantes Fiscales (Factura,
  Prevalorada, Ticket, Recibo Honorarios, Boleta Compra, Constancia
  Donación) / Documentos Complementarios (NC, ND, Guías Remisión,
  Comprobantes Retención) / Otros. 16-digit correlativo =
  establecimiento(3, matriz=000)+punto de emisión(3)+tipo doc(2)+consecutive(8,
  wraps 99999999).
- **Withholding:** asalariados = annualize→deduct→table→÷months (plantilla);
  composite L257,493.16 sole-source gate; 12.5% services; 1% compras
  anticipo (retainer >L15M); OTCD cards 10%-of-tax/15% fallback; non-resident
  gross table 25/10 (current = `01_` Art. 5; the 2010 all-10% window is
  historical).
- **Rates:** ISR PJ 25%, PN 15/20/25 IPC-indexed annually (law Art. 22.b
  mechanism + annual SAR acuerdos values); 22-A gross-minimum (≤L1B excluded,
  1%/0.5% sectors); ISV 15%/18%/0; mora 3%/mo cap 36%; prescription
  4/5/7y; multas = income-range × SMM-promedio fractions + ISR-late
  5→25%/month escalator.
- **Payroll:** 13th AND 14th month each exempt ≤10×SMM promedio, excess
  taxable; vacaciones >30d taxable (360-day divisor); senior deduction stack
  L40k/80k + L30k@60 + L350k@65(≤350k gross); RAP 1.5+1.5 + fondo reserva
  4% employer (ceiling 3× top SMM); IHSS ceilings L11,903.13 (2025).
- **W2 fiscal reporting (do not re-derive):** Form 535 EEFF-prior gate from
  FY2024 (SAR-619-2024; Jan-1→Apr-30; PJ + PN comerciantes individuales;
  EEFF = SAME obligation as the ISR DJ); **the Ayuda 67_ shows NO
  contador-certification field and NO GyP section** (vs SAR-619/236 text —
  OQs); DJIMR (SAR-238-2024) = monthly informativa PER retention código
  (25-code catalog), 10 días calendario, one-modality, rectificativa → SAR
  auto-rectifies the determinativa (aceptada only if tax↑); DMC = form 527,
  deadline chain 10d→20d→**5 días calendario (SAR-237-2024)**, sujetos incl.
  State institutions; **tarjetas 523 (SW informativa) + 215 (OVI
  determinativa, base = 10% of ISV − devolución 8%, Banco Central) file
  OUTSIDE the DJIMR catalog via DEI-9382-J-2003**; devolución 8% ALIVE in the
  2024 declaration text; compras eventuales = doc type 10 buyer-issued,
  buyer retains the ISV caused (rate unpinned — OQ); DMC line contract
  (casillas 200/7/8/1511/1611/1520/1620/270/280) fully extracted; TP inform:
  pequeños excluded ≤USD 1M related-party ops, TP adjustments auto-migrate
  into the ISR DJ base; AS = 5% RNG>L1M (PJ-only per prints), ATN = minimum
  tax over L3M asset exemption, both D.51-2003 Ley Equidad Tributaria
  (un-acquired — TOP lead); contribuciones: 504 1% / 502 1% / 503 0.5%
  monthly, 506 3.6% / 509 15%+0.5% floor / 511 15% / 107 10% annual;
  selectivo 203 = separate D.58-1982 tax (coexists with D.17-2010 family);
  259 = 4% turística retention.
- **W2 conflicts (open OQs — never resolve silently):** GC non-resident
  retention **2% (46_ print) vs 4% (05_ Art. 14)**; ZOLITUR rate article
  Art. 4 vs Art. 25 (D.181-2006 un-acquired); **DMC manuals print "8 días"
  citing SAR-237-2024 whose gazette text says 5** (5d = record; manuals
  stale); 506-vs-509 cooperative boundary; 39_ ≡ 37_ (both código 135).
- **Decisions:** **D-H1** (binding, in EXTRACTION_PLAN): one journal per
  company via `l10n_latam_invoice_document`; sequences key =
  (establecimiento→`stock.warehouse`, punto de emisión→child emission point,
  doc type→`l10n_latam.document.type`); emission point NOT on journal;
  user↔emission-point matrix = operational FR only (non-statutory).
  **D-H2** (2026-08-20, binding, in EXTRACTION_PLAN): temporal validity —
  every statutory value = dated row resolved by HECHO-GENERADOR/period date
  (payroll key = period + worker attributes, birthday-year rules); HARD
  BLOCK emission outside a CAI range's vigencia (no override; supervisor
  variant rejected); historical reconstruction = flagged read-only imports;
  payroll corrections recompute with ORIGINAL-period rows; filed periods
  write-protected (D9 kin); regime cutovers (SEE mandate, amnistía,
  transitorias) = dated config rows. Inherits repo D9/D11/D12; SV session
  deciding the same prompt in parallel — reconcile at merge.
  **D-H3** (2026-08-20, binding, in EXTRACTION_PLAN): go-live ingestion =
  current-FY fiscal-document detail (read-only, original CAI numbers/dates,
  D-H2-resolved) + prior-years aggregates; reconciliation vs the PREVIOUS
  system's SAR-filed declarations (DMC/DJIMR/DJI); payroll = monthly
  aggregates per contract (hire-date depth for fondo/cesantía/vacaciones,
  FY-start depth for ISR/13th/14th), no payslips; stock/banks = opening
  balances only.
- **W1f (taxation closers):** `05_` = devolución 8% ISV tarjetas (status OQ),
  OTCD complement ORIGIN (current text = 02_ Art. 8), **E-Arts 5/10 VOID
  (sentencia RI-0763-2011, 25-mar-2021 — never feed)**, ganancias de capital
  10% mechanics (per-transaction 10 días hábiles + Apr-30 annual +
  non-resident real-estate 4% buyer retention + reorg exception), exonerations
  personalísimas/in-kind-only + SEFIN single-document, RIT D.37-84 reformed
  text (suspension + per-import guarantees + 5-year machinery gate + 100%
  multa), no-simultaneidad, sacrificio-fiscal declaration, general retention
  entero monthly 10 días calendario; `23_` = Art. 206 CT void since
  22-feb-2022 (rubrica; SCO-800-2017; erga omnes) — 5/10/20% litigation
  guarantee never implement; `79_` = 65+ L80k deduction + ≤L350k gross
  exemption de pleno derecho (birthday-year rule; intereses/ganancias carved
  out of test base); `80_` = 22-A transition (FY2018/19 L300M/L600M bands →
  FY2020+ L1B/1.0%/0.5% sectors) + SEFIN-exception procedure + D.105/199-2011
  contributions permanent (= the financial-transactions contribution excepted
  in 05_ Art. 35). **Registry glosses for 05_/79_/80_ corrected (content ≠
  gloss — 4th incident after SV 29_/09_/15_; rows amended).**

## 5. Gotchas & verified lessons

- **Wrong-domain sites:** congresonacional.gob.hn / stss.gob.hn /
  upap.gob.hn / cpmcp.hn / enag.hn = NXDOMAIN. Real: `congresonacional.hn`
  (no law library), `www.trabajo.gob.hn` (STSS WordPress),
  **`enag.gob.hn` = Gaceta Digital 2015-2026** (recipe: `/index.php/gaceta-digital/<year>/<mes>`
  → `/index.php/gaceta-digital/<id>/download`). TSC biblioteca fully crawled
  (no Comercio/RAP).
- **SAR downloads:** resolve fresh wpdmdl from `/download/<slug>/` page
  (tokens rotate); some slugs dead. Registry↔file cross-check script in
  session history (trivial to rewrite).
- **OCR:** scanned gazettes OK at default PSM 6; TABLES need `gs -r400
  pnggray` + `tesseract --psm 4` (proven on all 5 tabla acuerdos + D.48-2024
  rates page is mojibake in text layer — needs PSM 6 pass at payroll wave).
- `11_` plantilla formulas read fine via openpyxl (not protected).
- IHSS site needs full browser UA. Bing/DDG useless for .hn; navigate
  catalogs directly.
- **Registry glosses can mislead (W1f):** 05_/79_/80_ glosses misdescribed
  content (05_ "impuesto mínimo/solidario" was flat wrong — content has
  neither). Page-1 verify checks the document, not the gloss; the end-to-end
  read is the authority. Glosses corrected in-place 2026-08-20.
- **Catalog TITLES can mislead too (round 4, 5th incident):** SAR's catalog
  title for Acuerdo 464-1990 said "Reglamento Art. 50 Ley ISR" but content =
  the 1990 reglamento to the D. 18-90-era reform (historical). Title ≠
  instrument identity; page-1 read caught it. Same family as 29_/09_/15_
  (SV) and 05_ (HN).

## 6. Next actions (ordered)

1. **W3 facturación/e-invoicing (NEXT):** full `24_` (Acuerdo 481-2017
   consolidado) read + `25_` (189-2014 hist) + `26_` (817-2018) + `76-78_`
   workflow helps; fold in W2a hooks (type-10 compras eventuales + 189-2014
   Arts. 10.f/21.7/69; D-H1 sequence key). D-H1 design inputs → FRs (CAI
   ledger, expiry/overlap/exhaustion guards, sequence key, emission-point
   model). OCR check first (04_/21_ were scanned; 24_ text layer believed OK
   — verify at extraction).
2. **W4 payroll:** `86_` CT (verify vintage vs `85_` derogations), bienio
   tables, IHSS/RAP architecture, D. 47-2024 OCR rates page; **NEW W2-round
   acquisitions ready: `101_` STSS-308-2022 (SMM 2022/2023 tables),
   `102_` Acuerdo 02-95 (14th-month reglamento; D. 135-94 Art. 34 origin),
   `104_` D. 103 Ley SMM.** D. 112 (aguinaldo law) still to acquire
   (SAR-republish route).
3. **Acquisition queue (W2 lead harvest, RESEARCH §5):** TOP = Ley Equidad
   Tributaria D. 51-2003 (activo neto/aportación solidaria) + Acuerdo
   SAR-236-2024 (535/OVI channels) + Reglamento Ley ISR ("Acuerdo N°799",
   4th citation) + D. 58-1982 (selectivo 203) + D. 131-98 (tasa turística) +
   TP family (D. 232-2011/027-2015/DEI-SG-004-2016) + contribuciones
   statutes (D. 105-2011, Acuerdo 1775-2011, D. 53/92-2015, D. 131-2018,
   D. 181-2006) + D. 112 + DEI-9382-J-2003 I-VIII + Código de Comercio +
   Ley RAP 107-2013. Most are SAR-catalog fetchable (recipe §6).
4. **Synthesis prep after W3/W4:** create `hn/.extractions/00_MASTER_INDEX.md`
   (SV-style; gitignore exception already in place), roll OQ families into
   MOQ/SOQ-style registers, then plan S-waves per the SV subagent pattern.
5. **Merge to main at milestone:** owner decision; rebase-then-merge; never
   force-push (root HANDOVER country model).

Session state at stop (2026-08-20, W2 close): evidence COMPLETE through
EVID-185 (~160 open OQs); corpus 103 files; W2a+W2b committed; next wave
W3 facturación.

## 7. Conventions (mirroring SV)

- Evidence: verbatim Spanish + gloss; candidate CRs + topic tags; doubts →
  OQs, never guesses. Per-file OQ numbering; corpus-global EVID (next=186).
  W2b ran subagent-dispatched with pre-allocated EVID ranges per family —
  proven pattern for large batches; controller verifies ranges + spot-checks
  verbatims afterward.
- `.gitignore`: `hn/.extractions/*` ignored EXCEPT `*.evidence.md` +
  `00_MASTER_INDEX.md` (create the master index at synthesis prep, SV-style).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from `105` (103 reserved-unused);
  page-1 verify everything. **8 mislabel incidents to date** (29_/09_/15_ SV;
  05_, 94_, 101_-server-filename, 20_, 52_ HN) — title-vs-content discipline
  on EVERY acquisition AND every evidence read.
- **Manuals can be stale vs gazettes (W2b lesson):** Ayuda prints citing an
  acuerdo can contradict its gazette text (45_/72_ "8 días" vs SAR-237-2024's
  5) — the gazette text is the record; flag manual conflicts as OQs.
