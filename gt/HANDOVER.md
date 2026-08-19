# gt/HANDOVER — Guatemala Session State & Continuation Guide

**For the next controller session.** Written 2026-08-19 at close of the GT
source-research sessions (W1–W5 + owner DCA batches); updated 2026-08-19
(convergence-audit session: shared-rules D16 reconciliation +
EXTRACTION_PLAN draft); updated 2026-08-19 again (W-GT1 evidence-pass
session: plan approved, FEL stack read, evidence committed). Read this
fully before acting; it is the authoritative cross-session memory.
**Update it at every session boundary.**

Session bootstrap command: `Read gt/HANDOVER.md and continue.`

## 1. What this work is

GT requirements-extraction for the Odoo localization, per
`shared/docs/requirements-extraction-procedure.md` (method spine) and the SV
corpus as precedent. Currently in **Stage 1/2 (evidence waves)**:
EXTRACTION_PLAN approved 2026-08-19; **W-GT1 (FEL stack) + W-GT2 (taxation
core) + W-GT3 (payroll) COMPLETE** — 14 evidence files committed
(EVID-001..370); W-GT4 (fiscal reporting) is next.
Product architecture context: root `HANDOVER.md` §1 (SaaS thin-client + Odoo;
Takumi consumes requirements).

## 2. Read order for a new session

1. This file
2. `docs/superpowers/specs/2026-08-18-gt-source-research-design.md` —
   decisions D-GT1..D-GT10 (scope, policies, FEL provider model, journal/
   document-type design, dated-instrument regime)
3. `gt/SOURCE_RESEARCH.md` — research record: wave log, candidates, verdicts,
   OQ register (OQ1–OQ17 with statuses), acquisition log
4. `gt/sources/README.md` — the registry (provenance + re-verify flags)
5. `gt/DOWNLOAD_QUEUE.md` — remaining owner-browser items (rev 5; most closed
   by the 2026-08-19 batch)
6. Root `HANDOVER.md` §GT (cross-session) + `shared/docs/` method docs

## 3. Repo/session mechanics

- **Branch `gt-research`, worktree `.worktrees/gt-research`** (same convention
  as HN; `.worktrees/` git-ignored via main commit f6f5415). Main is being
  actively committed by the SV session — never work outside the worktree;
  merge `gt-research` → `main` at milestone by owner decision.
- Commit style: short imperative, no emojis; commit per batch (precedent in
  `git log gt-research`).
- **`.gitattributes` carries `gt/sources/** -text`** — global
  `core.autocrlf=input` must never normalize source bytes (incident fixed
  2026-08-18: 24 blobs were silently CRLF-normalized; re-committed pristine).
  HN worktree should adopt the same line at merge time.
- Python: `~/.venvs/localizations/bin/python` (shared, absolute path — works
  from the worktree). Scripts in `shared/scripts/` (extract_text.py etc.).

## 4. Corpus state (2026-08-19)

**82 registered entries** (`gt/sources/`, numbering 01–83; gap 27 unused):
FEL e-invoicing stack (acuerdos 13-2018/26-2019/15-2020, incorporation
resolutions SAT-DSI 04_–14_, Reglas y validaciones **v1.7.10 Feb-2025**, Doc.
Técnico Servicios, 26 XSDs + 3 JSON catalogs × 2 channels (29_ GitHub pinned
961133c; 30_ cat.desa), manuals, casos-de-prueba 2018, contingencia 2018);
taxation core (IVA 27-92 **pre-FEL vintage — OQ10**, Reglamento IVA AG
5-2013, Código Tributario 6-91, LAT 10-2012 + AG 213-2013, **D-10-2025 IVA
reform — derogates Art. 8-"A"** (added D-31-2024; the "3-'A'" belief was a
myth — W-GT2), D-20-2006 + AG 425-2006 retenciones basis);
payroll (Código de Trabajo D-1441, IGSS set incl. Res. 08-SGF/2026, IRTRA
**D-1528 (1962) — identity corrected W-GT3**, INTECAP **D-17-72**, **bono 14
D-42-92 (40_) + incentivo D-78-89 (41_) — titles corrected W-GT3; December
aguinaldo law D-76-78 = MISSING**, salario
AG 250-2020 + **AG 256-2025 (2026 rates; CE2 maquila = Q3,221.10)** +
Historia 1995-2021); fiscal reporting
(form inventory snapshot 2025-10-06, retenciones Web pages+manuals, LET
manuals ×3, agentes roster 2025-10, criterios 6-2018/2-2019, SAT-2390 set);
COA anchor (Código de Comercio D-2-70, 301pp); special regimes (ZF D-65-89
chain **D-65-89 → D-19-2016 → D-6-2021**, maquila D-29-89 set, ZOLIC AG
65-2022); commercial-legal (AML **D-67-2001 + D-51-2001 + D-15-2026 Ley
Integral (17-jun-2026)**, RM edictos + aranceles).

**Known-stale instruments retained deliberately** (supersession discipline):
23_ (IVA pre-FEL), 68_ (ZF reglamento pre-check), 75_ (AML, likely
superseded by 77_ D-15-2026 — derogation inventory pending), 17_/19_ (2018
vintage FEL docs). Reform chains are recorded in SOURCE_RESEARCH.md.

## 5c. W-GT3 facts a synthesis session MUST know (2026-08-19)

- **Bonus-law identity corrections (material)**: 40_ = **BONO 14** (D-42-92:
  paid "primera quincena del mes de julio"; 100% of ordinary salary averaged
  over the year ending June; prorated). 41_ = **old incentivo law** (D-78-89,
  hourly floor Q0.15/Q0.30). **The December AGUINALDO law (Decreto 76-78) is
  NOT in corpus — acquisition candidate; never invent December-bonus
  mechanics.** Current Q250/mes incentivo = D-37-2001 (also missing).
- **IRTRA = flat 1% on total planillas** (D-1528 art. 12 as reformed by
  D-43-92; no brackets — OQ12 disproven). 42_ identity = Decreto 1528
  (29-May-1962). Text layer = substituted-glyph cipher, decoded with audit
  key in the evidence file.
- **IGSS OQ11 still open**: no cuota rates anywhere in corpus (D-295 prints
  only 25/50/25 financing proportions; 08-SGF/2026 defers rates to the JD
  Reglamento de Recaudación — acquisition candidate). NO tope máximo; base
  floor = salario mínimo AG vigente; patrono delivers both shares wholesale
  (laboral + patronal); planilla electrónica lifecycle; single receipt
  IGSS+IRTRA+INTECAP; mora day-after-due + 5% admin; ±1% rounding tolerance.
- **INTECAP = 1% vigente** (law's 0.50/0.75/1.00 ladder; reglamento art. 9:
  "uno por ciento del valor de los salarios mensuales"), base = IGSS
  planillas, **first 20 días of next month** (IGSS collects, retains 2%).
- **CT money rules**: jornada diurna 8/48 (45 effective paid as 48),
  nocturna 6/36, mixta 7/42; **OT ≥ +50%** (12h/day cap; holiday work = OT
  on top, no literal 2×); **vacaciones 15 días hábiles** + 150-day
  qualification + no cash-out while employed + 5-year retro cap;
  **indemnización (despido injusto) = 1 month/year uncapped**, base = 6-month
  average, IGSS offsets; preaviso is WORKER-side (semana/10d/2sem/mes);
  **NO auxilio de cesantía exists** (SV folk model rejected); salarios
  caídos ≤12 months; maternidad 84 días @100% + inamovilidad; lactancia
  2×½h/10 months; menores ≥14; inembargabilidad ladder + 50% alimentos cap;
  **CT contains zero aguinaldo/bono/propina provisions** — those are the
  specific laws' territory exclusively.
- **Salario mínimo structure**: 2 circunscripciones (CE1 = Guatemala dept,
  CE2 = rest) × 3 actividades; 2026 values transcribed [sic]-faithful (see
  registry row 37_ — includes the internal 3,416.90-digits vs
  3,816.90-words defect); history (39_) covers 1995-2021 only — 2022-2025
  AGs missing (minor gap).
- **Planilla IVA-FEL (56_)**: asalariado IVA credit via FEL DTEs + SAT-8560
  DUCA + SAT-2901 FYDUCA + SAT-2311/2799; window 01-Jan → 10th día hábil
  enero; Formulario SAT-1111 + Constancia; re-filing last-wins (priors =
  ANULADAS) + must report to patrono.

## 5. GT facts a new session must know

- **FEL model**: SAT owns XML standard + validates; taxpayers integrate via
  **certificadores de DTE** (18 authorized; NOT "instaladores"). **TotalDoc =
  GRUPO CDS S.A., NIT 107902281**, authorized 02/12/2021 → **02/12/2026
  (OQ7 renewal watch)**. Product default provider = TotalDoc (D-GT5/D-GT6);
  public docs only so far; partner-access list in SOURCE_RESEARCH W1-C.
- **No "Anexo técnico" exists** — equivalents: Reglas y validaciones +
  Documento Técnico Servicios + XSDs + JSON catalogs.
- **Schema drift (OQ3, material)**: cat.desa vs GitHub differ in 8/17 shared
  files; GitHub main = "versión 2" actively maintained. Ask TotalDoc/SAT
  which set production validates against.
- **ISR today = LAT D-10-2012** (26-92 superseded). **ISR anual = SAT-1371**
  ("2236" = legacy, rejected). **IVA retenciones = D-20-2006 + AG 425-2006**
  ("resolución 2-2010" = rejected myth).
- **FEL legal chain**: AD 13-2018 → 26-2019 → 15-2020 + SAT-DSI incorporations
  243-2019…400-2023 (04_–14_). Ley IVA Art. 29-"A" is the law-level hook
  (cited by AD 15-2020; **provenance pinned: added by Dto. 4-2019 art. 6**)
  — post-2018 consolidated IVA still missing (OQ10).
- **D-GT8/D-GT9/D-GT10 bind synthesis**: `l10n_latam_invoice_document`
  (one journal, multi document types — now also shared default **D17** in
  `shared/docs/odoo-localization-guide.md`; D-GT8 = its GT instantiation);
  sucursales/warehouses/cash-registers → FEL establishment/dispositivo codes;
  **dated-instrument regime** — D-GT10 instantiates **shared D16**
  (`shared/docs/regulatory-change-management.md`): dated rule rows
  (valid_from/to + provenance; changes add rows), fecha-emisión rule
  selection, no past-dated transmission (certification timestamp;
  historical = non-transmittable accounting class), retro payroll with
  original-period rates, freeze-at-filing, backdating UX. **Naming note
  (2026-08-19 merge session): GT's "shared D13" proposal was renumbered
  D16** (D13/D14 = SV journal/establishment instantiations of D17); D16 was
  reconciled with D15 (as-of doctrine) and amended with HN's D-H2/D-H3
  (hard no-override emission block outside authorization-range vigencia;
  ingestion reconciliation against filed declarations). Cite D15+D16
  together; D18/D19 + `shared/docs/go-live-readiness.md` also bind
  synthesis (GT register already seeded there).

## 5a. W-GT1 facts a synthesis session MUST know (2026-08-19)

- **Reglas y validaciones = v2.0** (changelog row "2.0 19/12/2024", vigencia
  abril 2025, 146pp; the "v1.7.10 Febrero 2025" cover footer is stale —
  filename encodes it). Chain jumps 1.7.9→2.0. **26 DTE types, 11 families**
  (FACT, FCAM | FPEQ, FCAP | FESP, NABN, RDON, RECI, FEPE | NDEB, NCRE |
  FACA, FCCA | FAPE, FCPE | FAAE, FCAE | FARP, FCRP | FPEC, FCPC | CIVA,
  CAIS | NEV, RANT, FACP); v2.0 added FEPE/FARP/FCRP/FPEC/FCPC (Decreto
  31-2024). Tension vs GitHub XSD (6 types commented out; BIDP XSD-only) =
  evidence OQ.
- **D-GT9 refinement (material for Odoo mapping)**: NO taxpayer
  punto-de-emisión field exists in the schema — establishment =
  `Emisor/@CodigoEstablecimiento` (xs:positiveInteger 1-9999, SAT-assigned)
  + `NombreComercial`; `DatosGenerales/@Dispositivo` (APP/AV/APPVOZ) is
  SAT-apps-exclusive; Serie/Numero are UUID-derived post-certificación.
  Odoo mapping: sucursal/warehouse → CodigoEstablecimiento; dispositivo
  mapping only for SAT-app emission (out of product scope). Runtime teeth:
  mensajes RCP305/306/460/485/497 validate establishment existence/type.
- **Schema drift (OQ3) sharpened**: GitHub = working authority EXCEPT
  MediosdePago (GitHub copy = uncompilable TurismoPasaje overwrite; use
  cat.desa there); catalogoMensajes RCP108/109 bodies swapped between
  channels; unidadesGravables PETROLEO 15/16 differ. Full matrix in
  `gt/.extractions/29_30_FEL_XSDs_catalogs.evidence.md`.
- **Mandate chronology (D-GT10 dated rows)**: 243-2019 proveedores Estado →
  838-2019 serv. profesionales → 639-2020 serv. técnicos (legacy auths void
  31-dic-2020) → 640-2020 ALL FACE emisors (FACE void 31-dic-2020) →
  887-2020 compra directa/baja cuantía (excl. <Q2,500) → 398-2021 →
  1074-2021 salud → 1218-2021 contadores → **1240-2021 régimen general
  (DTE start ≤01-jul-2022; mass mandate; cohort = IVA-registration fact)**
  → 1350-2022 pequeños (≤31-mar-2023) → **400-2023 extends pequeños →
  01-jul-2023**. No sanctions articles — enforcement = authorization lapse.
  Instruments are Resoluciones de Superintendencia (not "Directorio
  Superior"). 07_ carries a 639-2020 duplicate; 11_ carries the full
  1240-2021 text (same DCA page — the portal swap incident explained).
- **IVA Art. 29-"A" provenance PINNED**: added by **Decreto 4-2019 (Ley
  Reactivación Económica del Café) art. 6** — verbatim in 02_ considerando.
  OQ10 consolidated-IVA hunt now has an exact anchor.
- **16_ Doc Técnico = Versión 1.2, undated, XSD refs at -0.1.0** (predates
  the 0.2.1 set). Scope = SAT↔certificador ONLY (getToken 60-min /
  postFactura / postAnulacionDTE / mini-RTU push; no batch/consulta/reversion
  ops). Product integration boundary = certificador (TotalDoc) API, not SAT.
  Anulación = logical annotation, never modifies the certified DTE; Adenda
  must never reach SAT. UUID v4 generated by the certificador. Crypto:
  XAdES-BES, RSA, SHA-256.
- **Anulación window (current authority)**: until the IVA-declaration due
  date of the emission period (supersedes the 2018 5-day rule) + blockers
  (NC/ND/constancia/retención origins, prescription) + cross-certificador
  anulaciones allowed. Fecha emisión: ≤5 días back (CIVA/CAIS exempt),
  same-month future only. CF (consumidor final) cap Q2,500.
- **Rates captured (Reglas v2.0 §)**: IVA 12%/0%; IDP 13 per-unit Q rates;
  ITH 10%; ITP USD30/10; TDP 0.50%; IFB 2%; IDB 6/7.5/8.5%; TAB 100%/75%;
  CEM Q1.50; IBN Q0.18-0.08; TAP USD0.05; FESP ISR 5%; FEPE ICT 1.5%;
  agropecuario 5%/1.5%/2%/10% family; tolerance ±0.01.
- **Certificador roster (31_, as-of 2026-08-18)**: 18 authorized; TotalDoc
  (GRUPO CDS, NIT 107902281) renewal 02/12/2026 = OQ7 watch; 6 more expire
  2026 (AINNOVA/CARI/DIGIFACT/FORCON/INFILE/INFORUM/MEGAPRINT/TEKRA —
  re-check roster at next milestone).

## 5b. W-GT2 facts a synthesis session MUST know (2026-08-19)

- **OQ13 RESOLVED (verbatim, both halves)**: IVA retentions = **% OF THE
  IVA**, not of base (D-20-2006 arts. 1-6): 65% exportadores
  agropecuarios/silvícolas + D.29-89 empresas; 15% otros exportaciones +
  especiales + otros agentes; 25% sector público (municipalidades
  excepted); 15% operadoras de tarjeta (afiliado liable for the 85% not
  retained); **1.5% sobre el VALOR TOTAL** for fuel paid by card (the only
  base-exception). Q2,500 de minimis (art. 10); agent-to-agent abstention;
  declare primeros 15 días hábiles even-if-zero; constancia at retention
  moment. ISR (LAT): asalariados **5% to Q300k annual + Q15,000 + 7%**
  (withholding = annual projection/12); Opcional 5/7% monthly Q30,000;
  capital 10% + dividends 5% definitive; no-residentes 5/3/10/15/25;
  facturas especiales 5% definitive.
- **OQ17 RESOLVED-AS-MYTH**: D-10-2025 derogates IVA Art. **8-"A"** (added
  by **D-31-2024** "Ley Integración Sector Productivo Primario y
  Agropecuario" art. 13 — MINEDUC alimentación-escolar retention), NOT
  Art. 3-"A". "Art. 3-'A'" joins the rejected-myths list. D-31-2024 full
  text = acquisition candidate (also the source of the 5 new DTE types).
- **Consolidation cuts (evidence-verified)**: 23_ IVA through D-10-2012/
  D-4-2012 (no 29-"A", no 8-"A"); 24_ Reglamento IVA tail = **AG 222-2019
  only — 11 FEL arts (new registrants FEL-only from 1-jul-2021; 6-month
  cap on legacy docs)**; 25_ CT through **D-37-2016** + CC annotations to
  03-12-2019 — **no FEL-era reforms; CT Art. 120 IVA-suspension ¶ VOID per
  CC 680-2013** (FEL suspension hook must cite 98"A" not 120); 26_ LAT
  through **D-46-2022** (≤2013 registry risk REFUTED); 28_ with AG 167-2014
  only; 79_ art. 32 reformed AG 125-2022.
- **IVA core values**: tarifa única 12% price-inclusive + 5pp earmarks
  (3.5+1.5); exenciones Art. 7 (15 numerales) vs constancia-based 8/9;
  crédito fiscal prorrateo verbatim (Reg. art. 20-kin ÷1.12 mechanics);
  saldo = traslado, devolución trimestral/semestral; pequeño = **Q150,000
  annual gross threshold (2012 value — dated-row discipline) + 5% pago
  definitivo** + Q2,500 op floor + Q50 planilla; used vehicles/motorcycles
  = FIXED Q fees (Q1,000/500/300/200), not ad-valorem; ISR/LAT deducciones
  caps Q48,000/Q12,000/Q60,000; LAT Utilidades 25%, transitional 31/28/25;
  no NOL carryforward for lucrativas in consolidated text.
- **CT mechanics**: prescription 4 años (8 unregistered) / sanctions 5 años;
  mora 0.0005/day; omisión/retenidos 100% (50% pre-requirement); multa
  scale Q50/day→Q10,000+1%; cierre 10-20d; resarcitorio = Junta Monetaria
  rate (external — OQ); books retention = plazo de prescripción (no fixed
  years); e-documents/signature arts. 125/A/B.

## 6. Access realities & gotchas (verified)

- `portal.sat.gob.gt`/`www.sat.gob.gt` = **Cloudflare 403 to ALL non-browser
  clients** (browser-UA curl too). Acquisition: owner browser downloads
  (ruling OQ2) or Wayback-of-official-URL with provenance + re-verify flags
  (follow-up ruling). Wayback quirks: rate-limits after bursts (sequential +
  sleep); some `id_` captures truncate at exact 1/5 MiB boundaries — try
  alternate captures (65_ fixed via 2022 capture; 66_ via 2024-06-12).
- **SAT label ≠ content**: id 17662 "639-2020" serves a 639-**2011** PDF; id
  57855 "1240-2021" serves a 1218-duplicate post-2023 (real 1240 = digest-
  verified 2022 captures, 12_). wpfd re-ids/re-categories files (manuals
  6524→15747; LAT →78389). **Verify every download by reading it.**
- `legal.dca.gob.gt` search = JS app — owner's browser works well there
  (19 docs found 2026-08-19); CDX `filter=` regex must be lowercase.
- igssgt.org / irtra.org.gt (needs browser UA + referer) / intecap.edu.gt /
  mineco.gob.gt (`mineco.gob.gt`, not mineconomia) fetch directly.
  mintrabajo 403 (use Wayback; site rebuilt ~2024 — check capture mimetypes).
  congreso + registromercantil unusable (empty/maintenance).
- Non-official leads (never registrable): atlas.com.gt calendario
  (back-years; cross-check only), corporacionbi.com calendario,
  diamantecontador forum, capacitacionessat.page Google Sites (SAT-branded,
  non-gov domain — ratify before use).
- OCR: DCA gazette prints need `--psm 6`; **table pages need PSM 4 at
  300–400dpi** (SV D.O. lesson carries over). Several corpus PDFs are scans
  (02/03, 33–35, 38, 64–65, 71, 73, 74, 76–77, 81, 83) — Stage 1 extraction
  must OCR-verify page 1 identity before reading.

## 7. Open questions register (live ones; full list in SOURCE_RESEARCH.md)

- **OQ3** schema drift cat.desa vs GitHub → ask TotalDoc/SAT (drift matrix
  complete; GitHub MediosdePago defect = use cat.desa there meanwhile).
- **OQ10** post-2018 consolidated Ley IVA 27-92 — Art. 29-"A" provenance
  pinned (Dto. 4-2019 art. 6); full text still missing. ~~OQ17~~
  RESOLVED-AS-MYTH (D-10-2025 derogated Art. 8-"A", added D-31-2024;
  "3-'A'" never existed). **D-31-2024 full text = acquisition candidate.**
- **OQ11 (SHARPENED — still open)**: IGSS cuota rates NOT in corpus — live
  in the JD Reglamento de Recaudación (Acuerdo 1118-kin, acquisition
  candidate); no tope máximo; base floor = salario mínimo.
- ~~OQ12~~ **DISPROVEN + RESOLVED W-GT3**: IRTRA = flat 1% on planillas
  (D-1528 as reformed by D-43-92; no brackets; identity corrected to 1962).
- ~~OQ13~~ **RESOLVED W-GT2** (see §5b).
- **OQ14** D-15-2026 derogation inventory; AML reglamento status; Q2,000
  threshold wording.
- **OQ15** ZF reglamento (AG 242-90) current-reform status.
- **OQ16** does a numbered Reglamento del Código de Comercio exist?
- **Evidence-file OQs (W-GT1+W-GT2)**: ~95 per-file OQ-1.. live in the 10
  evidence files — MOQ-roll into a master index at synthesis prep (SV
  pattern).

## 8. Accountant track (asked 2026-08-19; assume yes, plan B ready)

Asks: (1) current consolidated Ley IVA 27-92 print (≥2018 reforms, ideally
through D-10-2025); (2) calendario perpetuo vencimiento windows per NIT
last-digit (monthly/quarterly/annual); (3) D-15-2026 AML reglamento status +
what happens to AG 75-2006 / Q2,000 cash-documentation rule.

**Plan B (no accountant)**: proceed with corpus-as-is using the SV
gaps discipline — record missing values as OQs with instrument-provenance
notes, never guess (SV precedent: F-14 SS caps shipped as dated data with
instrument-OQs); keep owner-driven DCA browser hunts (they outperformed
every automated route); calendar windows → transcribe from SAT's JSF app in
owner browser with atlas.com.gt as cross-check only; OQ3/dated data →
surface to TotalDoc when partner access opens (W6). Requirements can be
synthesized with these as flagged open questions and back-filled later.

## 9. Next actions (ordered)

1. ~~EXTRACTION_PLAN~~ approved + ~~W-GT1~~ + ~~W-GT2~~ + ~~W-GT3~~
   **COMPLETE 2026-08-19** (see §5a/§5b/§5c + plan extraction log).
   **Next: W-GT4 — fiscal-reporting evidence pass** (48_ form inventory,
   49_/50_ RetWeb pages, 51_/52_ RetWeb manuals, 53_ agentes roster,
   54_ SAT-0261, 55_ pequeño digest, 57_/58_/82_ LET manuals, 59_ informe
   compras/ventas, 61_ libro pequeño, 62_/63_ SAT-2390, 64_/65_ criterios,
   30_ calendario-kin absent — JSF transcription rides any wave).
2. Opportunistic gap closure: queue rev-6 items (AG 75-2006 AML reglamento,
   consolidated IVA post-2018, D-19-2016); instructivos cat 15812;
   calendario transcription via SAT JSF app; accountant answers fold in
   when they arrive.
3. W-GT3 payroll → W-GT4 fiscal reporting → W-GT5 COA+commercial-legal →
   W-GT6 special regimes, per the plan's reading order.
4. Synthesis prep after each topic's evidence base completes (master index
   + MOQ roll; SV pattern) — S-GT1 (e-invoicing) is unblocked now if the
   owner prefers synthesis-first.
5. Milestone: owner decides `gt-research` → `main` merge (owner owns ALL
   merges; controller verifies branch state only). **OQ7 watch: TotalDoc
   authorization renewal 02/12/2026 — re-check the certificador roster
   (31_) at the next milestone.**
6. W6 partner follow-up when TotalDoc access exists (API manuals, sandbox,
   OQ3 + MediosdePago question).

## 10. Owner notes (2026-08-19, session close; updated same day by the
convergence session; updated again at W-GT1 close)

- ~~Owner will handle the `gt-research` → `main` merge personally~~
  **SUPERSEDED by root HANDOVER §4.6** (standard session-close & merge
  protocol, 2026-08-19): at session close the controller drives the
  rebase-then-merge + §3 merge record. GT waves 1-3 merged to main
  2026-08-20 under §4.6.
- ~~NEXT SESSION PRIORITY: uniform shared rules for all 3 countries~~
  **EXECUTED on main 2026-08-19**; residue closed by the GT convergence
  session (see above). Remaining convergence surface: keep country
  instantiations current at each synthesis close (go-live-readiness
  registers + D15/D16 registers); converge variant texts via root
  HANDOVER.md.
- **W-GT1 session rulings (2026-08-19)**: EXTRACTION_PLAN approved
  as-drafted; **evidence files COMMIT** (gitignore exceptions, SV/HN
  pattern — standing policy for all GT waves); W-GT1 executed
  subagent-driven with controller spot-verification (quote checks against
  the txt sources passed; one agent retry needed — the incorporations
  agent returned empty the first time, watch for that failure mode).
  Reglas v2.0 naming ruling: cite as "Reglas v2.0 (19/12/2024, vigencia
  abril 2025)" — never "v1.7.10" (stale footer). D-GT9 dispositivo
  refinement recorded (§5a) — flag to product owner at S-GT1 synthesis.
- **W-GT2/W-GT3 session addenda (same day, same session)**: the
  subagent-per-reading-unit + controller spot-check pattern held for 3
  waves (14 evidence files, EVID-001..370, no collisions; gaps 077-080,
  326-330). Working conventions: agents get EVID ranges pre-assigned per
  wave (W-GT2: 161-265; W-GT3: 266-370; next wave starts at EVID-371);
  agents read a committed evidence file as the format template (context
  saver); controller verifies 3-5 load-bearing quotes per wave by grep
  before commit. Registry title corrections are batched into the wave
  commit. **Next wave (W-GT4) note: 48_/49_/50_ are HTML snapshots +
  64_/65_ are scans — Stage 1 needs the HTML text dump + OCR; calendario
  JSF transcription still rides any wave (owner browser).**
