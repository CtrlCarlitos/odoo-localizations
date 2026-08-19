# HANDOVER — Honduras Session State & Continuation Guide

**For the next HN controller session.** Written 2026-08-20 after evidence
wave W1e, updated same day after W1f (taxation core CLOSED), and again same
day (lead-dig round 4: sources 93-100 + decision D-H2). Read this fully
before acting; it is the authoritative HN cross-session memory (conversation
context does not survive). Update it at every session boundary.

**Bootstrap prompt for a fresh session:** `Read hn/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/hn-research`, branch `hn-research` (pushed,
  through commit `f642e15`). The SV session works on `main` concurrently —
  NEVER touch `main`, root `HANDOVER.md`, or `sv/` from this branch; `hn/`
  + `docs/superpowers/specs/` are ours. Merge to `main` only at the
  milestone, coordinated with the user, after the SV session winds down.
- **Mission:** bootstrap the Honduras Odoo localization per
  `docs/superpowers/specs/2026-08-18-hn-source-research-design.md`
  (e-invoicing IN scope; acquire+register; evidence waves authorized by the
  phase-extension note in that spec). Procedure:
  `shared/docs/requirements-extraction-procedure.md`.

## 2. Read order for a new session

1. THIS file
2. `hn/EXTRACTION_PLAN.md` — wave log (W1a..W1f DONE — taxation core
   COMPLETE), reading order, risks, **Decisions (D-H1 binding)**
3. `hn/RESEARCH.md` — research dossier: sites, fetch recipes (§6), hint
   layer w/ corpus verification (§7), open leads (§5, retry round 3 results)
4. `hn/sources/README.md` — registry, 100 files (01-100, no gaps), full
    provenance
5. Evidence files in `hn/.extractions/*.evidence.md` (committed):
   `01_` (ISR, EVID-001..015), `02_` (ISV, 016..026), `03_` (CT, 027..038),
   `04-21-22_` (D.17-2010 family, 039..053), `07-12+11_` (tables+plantilla,
   054..056), `05+23+79+80_` (taxation closers, 057..071). **EVID numbering
   is corpus-global, next = 072. OQs are per-file (OQ-1..n at file end);
   27 open.**

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
- **Lead-dig round 4 (2026-08-20, 93-100):** D. 31-2019 22-A interp/reforma
  (`93_`; gazette header prints 34,932 vs catalog 34,934 [sic] — pin at
  evidence), Acuerdo 464-1990 (`94_` = the 1990 ISR-withholding reglamento
  ancestor: L10k gate, 5% services, 20-day entero — HISTORICAL; NOT the
  modern Reglamento Ley ISR, which stays open), D. 199-2006 Adulto Mayor
  (`95_` = L30k@60 source) + **D. 45-2025 (`96_` = NEW: Jan-2026 reform,
  Arts. 31/31-A/31-B)**, D. 194-2002 original (`97_` = Art. 14 65+ ≤L350k
  origin), selectivo IPC chain (`98/99/100_` = 172-2022 → 014-2023 →
  218-2024, current 5.19%). Dead ends: Instructivo 461-2020 (not on SEFIN),
  STSS-308-2022 (not on STSS site) — both need Gaceta dates → ENAG route.

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

1. **Lead-dig round 4 residue (Gaceta-date-dependent):** modern Reglamento
     Ley ISR (plantilla cites its Art. 51 — 94_ proved to be the 1990
     ancestor), Acuerdo STSS-308-2022 (14th-month SMM), Instructivo
     461-2020 (22-A exceptions), DEI-9382-J-2003 + 8%-devolution reglamento,
     Ley RAP 107-2013, Código de Comercio, STSS reglamentos app (ASP.NET
     shell — interactive). Most need a La Gaceta date → ENAG
     `/index.php/gaceta-digital/<year>/<mes>` route. All logged in
     RESEARCH §5.
2. **W2 fiscal reporting:** `13-20_` procedures + 42 Ayudas batched by
     family. OCR not needed (text layers fine). D-H2 rules apply (period-
     correct parameter resolution; freeze at filing).
3. **W3 facturación/e-invoicing:** full `24_` read + `76-78_`; D-H1 design
    inputs → FRs (CAI ledger, expiry/overlap/exhaustion guards, sequence
    key).
4. **W4 payroll:** `86_` CT (verify vintage vs `85_` derogations),
    bienio tables, IHSS/RAP architecture, D. 47-2024 OCR rates page.
5. **Merge coordination** (user call): review `hn-research` → merge to
    `main`; AT MERGE update root `HANDOVER.md` §"GT / HN" (stale: says
    "scaffolded only") and fold HN rulings into its register per repo
    convention.

## 7. Conventions (mirroring SV)

- Evidence: verbatim Spanish + gloss; candidate CRs + topic tags; doubts →
  OQs, never guesses. Per-file OQ numbering; corpus-global EVID.
- `.gitignore`: `hn/.extractions/*` ignored EXCEPT `*.evidence.md` +
  `00_MASTER_INDEX.md` (create the master index at synthesis prep, SV-style).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from `101`; page-1 verify everything.
