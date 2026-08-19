# GT — Source Research Log (Stage 0 precursor)

Deep research for the Guatemala source corpus. This log records every candidate
document found, the triage verdict, and the site coverage map — the research
record that feeds `gt/EXTRACTION_PLAN.md` (Stage 0).

**Session**: started 2026-08-18, branch `gt-research`, worktree `.worktrees/gt-research`.

## Policy (decided with product owner 2026-08-18)

- **Topic scope**: full SV mirror — e-invoicing (FEL), taxation, payroll,
  fiscal-reporting, chart-of-accounts, commercial-legal, special-regimes,
  catalogs.
- **Source policy**: official-only, strict. Official GT government sites only;
  mirrors (law firms, news, universities) are never registered — recorded as
  acquisition leads when the official copy cannot be found.
  **Exception — partner tier**: FEL operates through SAT-authorized third-party
  installers; provider technical documentation (TotalDoc = default provider,
  https://www.totaldoc.com/) registers under a `partner-technical` provenance
  tier, LB-citable only for provider-interface requirements, clearly marked
  non-government. Public docs only (no partner-portal access yet).
- **Acquisition**: acquire-as-we-go into `gt/sources/` (SV-style `NN_Name.ext`
  numbering from `01_`) + registry rows in `gt/sources/README.md`. Ambiguous
  items get FLAGGED for owner decision, never guessed.
- **Triage rubric per candidate**: relevant → current (supersession chain) →
  useful (law / manual / form / catalog / schema) → official? Verdicts:
  ACQUIRE / FLAG / REJECT(+reason).

## Official domains (coverage map)

| Domain | Covers | Sweep status |
|--------|--------|--------------|
| sat.gob.gt (+ FEL subsites/portals) | Tax authority: FEL normative + technical, forms, manuals, calendars, catalogs | pending |
| congreso.gob.gt | Law library: codes + laws + reforms | pending |
| diario.gob.gt | Diario de Centro América (official gazette) | pending |
| igssgt.org | Social security (IGSS) | pending |
| mintrabajo.gob.gt | Labor ministry: salary minimums, labor regs | pending |
| mineconomia.gob.gt | Economy ministry: zonas francas / special regimes | pending |
| irtra.org.gt | IRTRA (patronal recreation institute) | pending |
| intecap.edu.gt | INTECAP (technical training, patronal contribution) | pending |
| totaldoc.com (partner tier) | Default FEL installer — public integration docs | pending |

## Verdicts legend

- **ACQUIRED** — downloaded to `gt/sources/NN_...`, registry row added, verified
  by reading page 1 (labels lie — SV lesson).
- **FLAG** — needs owner decision (unofficial mirror, ambiguous version,
  superseded-vs-historical call, blocked URL).
- **REJECT** — with reason (superseded with no historical value, out of scope,
  duplicate).
- **LEAD** — non-official copy of an official document we still need; official
  copy still hunted.

## Wave log

### W1 — e-invoicing core (COMPLETE sweep 2026-08-18; acquisition pending rulings)

3 research agents returned. Coverage notes: **`portal.sat.gob.gt` = Cloudflare
403 to ALL non-browser clients (browser-UA curl also 403 — verified
controller-side)**; sweeps used Wayback snapshots of official URLs.
`cat.desa.sat.gob.gt` (official) serves XSD/JSON directly — verified 200.
`www2.sat.gob.gt` dead (no DNS). `diario.gob.gt` dead → gazette =
`dca.gob.gt` / `legal.dca.gob.gt` (JS-only search). `congreso.gob.gt` has NO
law library. **Terminology: certificadores (18), not instaladores.**

Key structural finds (full detail in spec §W1 findings):

- No "Anexo técnico" exists; equivalents = Reglas y validaciones (chain
  1.5.1→1.7.9→current id 85864) + Documento Técnico Servicios + 26 XSDs + 3
  JSON catalogs.
- FEL legal chain: AD 13-2018 → 26-2019 → 15-2020; incorporations SAT-DSI
  243-2019…400-2023 (11 resolutions). "Decreto 6-2021" mandate UNVERIFIED.
- TotalDoc = GRUPO CDS S.A. NIT 107902281, SAT-authorized 02/12/2021 →
  **02/12/2026 (renewal watch)**. Public API docs = FAQ flow only; manuals
  behind partner access (list in candidates T-*).
- Schema drift: GT_Documento-0.2.1.xsd cat.desa 52,176 B vs GitHub 67,278 B
  (both verified 200 by controller); endoso/GLP XSDs + CatalogoFrases 0.6.0
  GitHub-only. SAT GitHub repo (official per portal links) active through
  2026-08-04.

## Candidates

### W1-A — SAT FEL technical (all `portal.sat.gob.gt/portal/descarga/...` → CF-blocked live; Wayback-verified)

| Cand | Title | URL (path after /portal/descarga/) | Verdict |
|---|---|---|---|
| A1 | Reglas y validaciones FEL (current, id 85864) + historical chain (25542/62522/67982/71638/77259/82893) | 14852/reglas-y-validaciones/85864/reglas-y-validaciones-fel-3.pdf | ACQUIRE (current + history) |
| A2 | Documento Técnico Servicios SAT | 6524/factura-electronica-fel/25830/documento-tecnico-servicios-sat.pdf | ACQUIRE |
| A3 | Casos de prueba para certificación (ZIP) | 6524/factura-electronica-fel/25545/fel-casos-de-prueba.zip | ACQUIRE |
| A4 | XSD schemas (26: GT_Documento-0.2.1, Anulacion/Reversion/Endoso*, 15+ complements, xmldsig) | github.com/notificacioneselectfel/Catalogo-FEL/tree/main/XSD + cat.desa.sat.gob.gt/xsd/alfa/ | ACQUIRE (pending OQ1 ratification) |
| A5 | Catálogos JSON: catalogoMensajes-0.3.0, catalogoUnidadesGravables-0.1.4, CatalogoFrases-0.6.0 | github …/Catalogos + cat.desa/catalogos/alfa/ (Frases 0.1.2 there = older) | ACQUIRE (pending OQ1) |
| A6 | Modelos de esquemas PDF (v0.1.0 era, 6 files) | 6524/…/25554–25559 | FLAG (historical, superseded by XSD v2) |
| A7 | Guía requisitos mínimos DTE (repr. gráfica), latest id 77253 | 6524/…/77253/guia-de-requisitos-minimos-dte-2.pdf | ACQUIRE (latest) |
| A8 | FEL process/architecture decks (felpresentacionpublica-2, fel-tecnologia-1-3) | 6524/…/82895, 77771 | FLAG (context, not normative) |
| B1 | Procedimiento emisión contingencia | 6524/…/38418 | ACQUIRE |
| B2 | Manual anulación FEL (2023 id 72293) + reporte anulación | 6524/…/72293 | ACQUIRE |
| B3 | Manual habilitación/acreditación certificador + descarga firma (2024 id 75322) | 6524/…/75322 | ACQUIRE |
| B4 | Procedimiento autorización del certificador (id 80213) | 6524/…/80213 | ACQUIRE |
| B5 | Procedimiento autorización auditor seguridad (id 80050) | 6524/…/80050 | FLAG |
| B6 | Registro de Certificadores de DTE (HTML, 18 entries + validity dates) | portal.sat.gob.gt/portal/certificador-de-dte/ | ACQUIRE (snapshot) |
| B7 | Registro de emisores FEL (monthly XLSB) | 14792/registro-de-emisores-fel/71261 (2023-06 archive) | FLAG (data snapshot) |
| B8 | Verificador público de DTE (web app) | portal page | FLAG (app, not doc) |

### W1-B — FEL legal basis + core tax laws (portal CF-blocked; Wayback-verified)

| Cand | Instrument | URL notes | Verdict |
|---|---|---|---|
| L1 | AD 13-2018 (creates FEL) | 1897/normativa-sat/25094 | ACQUIRE |
| L2 | AD 26-2019 (reformas FEL) | 1897/normativa-sat/45898 | ACQUIRE |
| L3 | AD 15-2020 | 1897/normativa-sat/49283 | ACQUIRE |
| L4–L14 | Resoluciones SAT-DSI 243-2019, 838-2019, 639-2020⚠, 640-2020, 887-2020, 398-2021, 1074-2021, 1218-2021, 1240-2021, 1350-2022, 400-2023 | 1897/normativa-sat/{46321,39867,17662⚠,46215,47495,51799,57857,57856,57855,66005,69739} | ACQUIRE (⚠ 639-2020 link points at a 639-**2011** PDF — SAT's own label/filename mismatch; verify on download) |
| L15 | Ley IVA Dto. 27-92 | 1899/legislacion-tributaria/18270 | ACQUIRE |
| L16 | Reglamento Ley IVA AG 5-2013 | 1817/…/53919 | ACQUIRE |
| L17 | Código Tributario Dto. 6-91 | wpfd_file/codigo-tributario-decreto-numero-6-91 (archived 2026-01-12) | FLAG (fetch; reform tail unknown) |
| L18 | Reforma CT Dto. 03-04 | 2335/leyes-y-reformas/60778 | FLAG (historic fragment) |
| L19 | Ley Actualización Tributaria Dto. 10-2012 (ISR vigente) + consolidada 2017 (6432) | 1899/…/18261 + 6432 | ACQUIRE (both; tail-check) |
| L20 | Reglamento LAT AG 213-2013 | 1899/…/18250 | ACQUIRE |
| L21 | Ley Orgánica SAT Dto. 1-98 + reforma 13-2013 | 1899/…/6588 + 2335/…/18262 | FLAG (secondary) |
| L22 | "Decreto 6-2021" mandate law | NOT FOUND on any official page | REJECT (unverified — never cite; DCA browser session could settle) |
| L23 | SAT event page: "Reformas a la Ley del IVA y Código Tributario" (2025) | events/reformas-a-la-ley-del-iva-y-codigo-tributario | FLAG (post-2024 reforms — identify decrees) |
| L24 | Manual Planilla IVA-FEL 2025 | wpfd_file/manual-planilla-iva-fel-2025 | FLAG (payroll-IVA, tangential) |

### W1-C — Provider layer

| Cand | Item | Verdict |
|---|---|---|
| P1 | Certificador registry snapshot (18 entities, NIT + validity) | ACQUIRE (with B6) |
| P2 | TotalDoc FAQ (API flow: XML→base64/JSON POST; onboarding; NIT) | ACQUIRE (partner-technical) |
| P3 | Manual TotalPOS v0.3 (2023-03) | ACQUIRE (partner-technical) |
| P4 | TotalPOS/TotalDoc product pages ("certificación aprobada por SAT") | FLAG (marketing; cite for claims only) |
| P5 | app.totaldoc.io / totalpos.totaldoc.com (login SPAs) | REJECT → partner-access list |
| P6 | api.totaldoc.io (root 404; endpoints undocumented) | FLAG (confirm base URLs with partner) |
| P7 | YouTube onboarding tutorial | FLAG (reference) |
| P8 | totaldoc.com.gt (hardware store/blog) | REJECT |
| P9 | Community Odoo module aquih/fel_totaldoc (v1.0 2023; dep `fel_gt` missing) | FLAG (community precedent — hint layer only, never LB) |

**Partner-access request list (W6)**: API integration manuals (firma/
certificación/anulación endpoints), XML example pack, SDK/Postman/OpenAPI,
sandbox credentials + auth scheme, app.totaldoc.io demo, pricing, api host
confirmation.

## Open questions / blockers

1. ~~OQ1: ratify GitHub Catalogo-FEL as official?~~ **RESOLVED 2026-08-18
   (owner)**: ratified — acquire BOTH GitHub (pinned SHA) and cat.desa;
   registry carries both; drift tracked as OQ3. Done: `29_` + `30_` acquired.
2. ~~OQ2: acquisition route for portal-SAT PDFs~~ **RESOLVED 2026-08-18
   (owner)**: manual browser downloads by owner; queue at
   `gt/DOWNLOAD_QUEUE.md`; inbox staging `gt/sources/inbox/` (git-ignored
   until verified). **Wayback fallback ALSO ratified** (same day, follow-up
   ruling): archived copies of official URLs register with provenance +
   re-verify flags when no live official route exists.
3. **OQ3 (SHARPENED — material)**: cat.desa vs GitHub drift is 8-of-17 shared
   files (measured 2026-08-18): GT_Documento-0.2.1 (52,176 vs 67,278 B),
   Exportaciones, MediosdePago, PartidosPoliticos, AnulacionDocumento,
   ExportacionProvisional (1 byte), catalogoMensajes, unidadesGravables;
   plus 11 GitHub-only files + Frases 0.1.2-vs-0.6.0. Which set does
   production validation use? → ask TotalDoc (partner) / SAT.
   **W-GT1 additions (2026-08-19)**: full drift matrix + substantive
   characterizations now in `gt/.extractions/29_30_FEL_XSDs_catalogs.evidence.md`;
   NEW hard findings — GitHub's MediosdePago XSD is an uncompilable
   TurismoPasaje overwrite (cat.desa copy coherent); catalogoMensajes drift
   hides under an identical header date (RCP108/109 bodies swapped);
   unidadesGravables PETROLEO 15/16 = different products/factors. GitHub =
   working authority EXCEPT MediosdePago (use cat.desa there) until SAT answers.
4. **OQ4**: "Decreto 6-2021" — verify via DCA browser session; until then
   untouchable.
5. ~~OQ5: Reglas y validaciones current version~~ **RESOLVED 2026-08-19
   (W-GT1 evidence)**: content = **v2.0** — changelog row "2.0 19/12/2024,
   vigencia abril 2025", 146pp, adds 5 DTE types (FEPE/FARP/FCRP/FPEC/FCPC,
   Decreto 31-2024); the chain jumps 1.7.9→2.0 (no 1.7.10 row). "Versión
   1.7.10 … 1 de 132 … Febrero 2025" = stale cover footer (residual OQ in
   evidence: whether a 132-pp 1.7.10 interim ever existed). Cite as
   "Reglas v2.0".
6. ~~OQ6: doc-type abbreviations~~ **RESOLVED 2026-08-19 (W-GT1 evidence)**:
   Reglas v2.0 §1.2 = 26 DTE types in 11 families (FACT, FCAM | FPEQ, FCAP |
   FESP, NABN, RDON, RECI, FEPE | NDEB, NCRE | FACA, FCCA | FAPE, FCPE |
   FAAE, FCAE | FARP, FCRP | FPEC, FCPC | CIVA, CAIS | NEV, RANT, FACP);
   pre-v2.0 set = 21. Tension vs GitHub XSD (six types commented out there;
   BIDP XSD-only) = evidence-file OQ.
7. **OQ7**: Grupo CDS authorization expires 02/12/2026 — renewal watch
   (registry page re-check at milestone).
8. **OQ8**: FELPLEX (utm_source seen) — unknown internal SAT/certifier
   portal; ignore unless it surfaces again.
9. **OQ9**: casos-de-prueba ZIP (17_) is vintage 2018-05-30 — may lag
   current catalogs/Reglas v1.7.10; refresh candidate (SAT may distribute
   test cases directly to certificadores now). **W-GT1 (2026-08-19)**:
   supersession watchlist now recorded — Reglas v2.0 supersedes the 2018
   values on anulación window (→ IVA-declaration due date of emission
   period), fecha-emisión 5-day rule scope, frase-tipo-4 scenarios (1–12 →
   1–35), contingencia re-send timing; 17_ stays citable as historical
   validation examples only.
10. **OQ10**: **post-2018 reformed edition of Ley IVA 27-92 with Art.
    29-"A"** — 23_ is consolidated only through ~2012 (GFACE era); SAT
    removed the law from the portal; MINFIN/DCA/Congreso routes dead or
    JS-only. Interim legal basis = AD 13-2018 + 26-2019 + 15-2020 + the
    SAT-DSI incorporation chain. Hunt routes: DCA Edición Legal browser
    session (valid ≥17-12-2018), SAT re-publication request.
    **W-GT1 PROVENANCE PINNED (2026-08-19, verbatim in 02_ considerando)**:
    Art. 29-"A" was added to Dto. 27-92 by **Decreto 4-2019 (Ley para la
    Reactivación Económica del Café), art. 6** — the consolidated-IVA hunt
    now has an exact anchor. Full post-2018 text still missing (keep OQ).

## Acquisition log

- 2026-08-18 — `29_FEL_XSD_cat_github_961133c/` (25 XSD + 3 JSON, pinned
  commit 961133c 2026-08-04) + `30_FEL_XSD_cat_catdesa/` (18 files, direct
  download) acquired + PROVENANCE.md each + registry rows. Controller-side
  verification: clone SHA checked; cat.desa files probed filename-by-filename
  (misses recorded); byte-diff measured → OQ3.
- 2026-08-18 — Manual queue (28 items + optional) handed to owner
  (`gt/DOWNLOAD_QUEUE.md`); inbox/ staged + git-ignored.
- 2026-08-18 (owner downloads batch 1 + 2) — **19 files registered**:
  01/02/03 (FEL acuerdos), 15 (Reglas y validaciones **v1.7.10 Febrero 2025**
  — newer than the agent's 1.7.9 chain; header also prints "VERSIÓN 2.0" →
  reconcile in evidence pass), 16 (Doc. Técnico Servicios, 27pp = updated vs
  20pp 2020 archive), 18, 22 (42pp = updated), 24, 25 (CT 95pp), 28,
  31 (certificadores snapshot), 05/07/08/09/10/11/13/14 (FEL incorporation
  resolutions; all DCA gazette prints, OCR-verified content). **Registry note:
  AD 15-2020 cites Ley IVA Art. 29-"A" → the 23_ Ley IVA acquisition MUST be
  a post-2018 reformed edition.**
- 2026-08-18 (SAT portal defects recorded) — three incidents: (a) id 17662
  labeled SAT-DSI-639-2020 serves **Resolución SAT-S-639-2011** (rejected);
  (b) id 57855 labeled SAT-DSI-1240-2021 serves **1218-2021 content**
  (duplicate of 11_; rejected — the real 1240 mass-mandate resolution still
  needed); (c) ids 46321/18261/18270/6432/25545 → "unpublished file(s)".
  Lesson recorded: **SAT portal label ≠ content — verify every download**
  (kin to SV factura.gob.sv wpdmdl shuffle).

- 2026-08-18 (Wayback acquisitions — owner ruling "accept with provenance") —
  6 files registered with re-verify flags: 04 (243-2019), 06 (real 639-2020 —
  the mislabeled-17662 hole closed), 12 (real 1240-2021 mass mandate —
  digest-verified 2022 captures; post-2023 captures of id 57855 serve the
  1218-duplicate), 17 (casos de prueba ZIP, 25 FEL test cases, vintage
  2018-05-30), 19 (contingencia, Mayo 2018), 23 (Ley IVA 27-92, 52pp —
  **consolidated only through ~2012: NO Art. 29-"A"** → OQ10). Registry
  carries Wayback snapshot URLs as provenance.
- 2026-08-18 (structural find — wpfd re-id/re-category pattern) — wpfd serves
  files under their CURRENT category: manuals moved 6524→15747 (anulación
  id 72293, firma id 75322), LAT 10-2012 re-id'd 18261→78389 (live, captured
  2026). SAT REMOVED entirely: 243-2019, 639-2020, 1240-2021 (pre-swap),
  Ley IVA 27-92, casos ZIP, contingencia (Dec-2025/Jan-2026 listings show
  them gone). Lesson: portal URLs rot; pin Wayback snapshots in provenance.
- 2026-08-18 (design notes) — D-GT8 (l10n_latam_invoice_document: one journal
  multi-doc-type) + D-GT9 (sucursales/warehouses/cash-registers → FEL
  establishment/dispositivo codes) recorded in spec at owner request.
- 2026-08-18 (owner downloads batch 3 — W1 manual queue COMPLETE) — 26 (LAT
  10-2012, live re-id 78389; reform tail cites only Dto. 14-2013 →
  consolidation ≤2013, post-2013 reforms unverified — Stage 1 check), 20
  (anulación manual, live re-category 15747), 21 (firma electrónica manual,
  live re-category 15747). **Corpus: 30 registered entries (01–31 minus
  dropped 27; +29/30 dirs +31 html)**. W1 acquisition phase CLOSED.

## Wave log (continued)

### W3 — payroll sweep (COMPLETE 2026-08-18; acquisition DONE)

3 parallel sweeps returned (W3 payroll / W4 fiscal-reporting+W2-residuals /
W5 COA+commercial-legal+special-regimes). Domain findings: igssgt.org,
irtra.org.gt, intecap.edu.gt, mineco.gob.gt fetch DIRECT (live); mintrabajo
403 (Wayback); congreso + registromercantil unusable (empty / maintenance);
legal.dca.gob.gt live but JS-only search (owner browser items queued).

**W3 acquisitions (12)**: 32 Código de Trabajo D-1441 (ed. Digital, 188pp),
33 IGSS Ley Orgánica D-295 + D-11-2004, 34 IGSS SSO AG 229-2014 (+33-2016,
57-2022), 35 IGSS Res. 08-SGF/2026 recaudación (the cuota apparatus), 36 IGSS
guía Recaudación, 38 AG 250-2020 salario, 39 Historia salarios, 40 Aguinaldo
D-42-92, 42 IRTRA D-15-1928 (disproves "AG 795"), 43/44 IRTRA AG 5/6-2005,
45 INTECAP Ley Orgánica **D-17-72** (disproves AG 445-86), 46 INTECAP
Reglamento tasa patronal, 47 SAT patronos-retención-ISR 2025.
**Pending**: 37 AG 256-2025 (salario 2026 — amounts verified via DCA news:
C1 agrícola Q3,791.20/no-agrícola Q4,002.28/maquila Q3,409.73; C2
Q3,625.89/Q3,816.90/Q3,321.10; eff 2026-01-01 + bonificación incentivo
D-78-89 Q250/mes), 41 D-78-89 PDF — both DCA-browser items.

### W4 — fiscal reporting sweep (COMPLETE 2026-08-18; acquisition DONE)

**Form family verified** (master inventory snapshot 48_; **row-level
re-verification W-GT4 corrected the W4-era misread — authoritative mapping:
IVA general = SAT-2237; ISR anual lucrativas = SAT-1411; asalariados anual =
SAT-1431; ISR no-residentes pago directo mensual = SAT-1371 (the old "ISR
anual = 1371" was wrong; 2236 = legacy pre-2013, REJECTED); ISR retenciones
= SAT-1331 (1321 = ISR capital mensual); ISR trimestral (anticipos) =
SAT-1361; pequeño = 2046/2241(FEL); retenciones IVA = 2340/2320; boleta
2000**);
**Retenciones basis = Decreto 20-2006 + Reglamento AG 425-2006** ("resolución
2-2010" REJECTED — no official trace). IVA-retention 15 días hábiles; ISR
10 días + constancias 5 días (49_/50_ page snapshots). Acquisitions (16):
48-57, 59-65. **Pending**: 58 LET IVA-General manual (live URL, never
archived); form instructivos cat 15812 (AJAX-gated); calendario tributario =
JSF app only, no static PDF exists (FLAG: transcribe windows via browser);
Dto 20-2006 + AG 425-2006 PDFs (not in CDX descarga tree — DCA browser);
retention percentages + anticipo article live inside law texts we hold
(26_/28_) → evidence pass.

### W5 — COA/commercial-legal/special-regimes sweep (COMPLETE 2026-08-18; acquisition DONE)

Acquisitions (8): 66 Código de Comercio D-2-70 (MINFIN copy, 301pp), 67-72
MINECO zonas-francas/maquila set (D-65-89 + AG 242-90 [reformed by AG 65-2022
per MINFIN — successor-regime question open], D-29-89 + AG 533-89 + AG
253-2001[?] reforms + AG 296-94 fondo), 73 RM aranceles.
**No statutory PCGA codification exists** — GAAP anchor = Código de Comercio
libros/contabilidad provisions (professional-body standards non-registrable
per policy). **AML = MAIN GAP**: Decreto 67-2001 + AG 75-2006 + Q2,000
threshold all UNVERIFIED from instrument text — only route =
legal.dca.gob.gt interactive (owner browser). "Decreto 16-2022" ZF-replacement
law UNVERIFIED (AG 222-2022 = ZOLIC-specific, not the national regime; AG
65-2022 reformed the 1990 reglamento → D-65-89 regime still alive as of
2022). Reglamento del Código de Comercio: no numbered instrument found (OQ).
RM site in maintenance.

## Open questions (additions, W3-W5)

11. **OQ11 (SHARPENED — W-GT3, still open)**: IGSS cuota split (patronal
    12.67% / laboral 4.83% priors) — **NOT verifiable from the corpus**: the
    08-SGF/2026 instructivo prints NO rates (rates live in the Junta
    Directiva Reglamento de Recaudación, Acuerdo 1118-kin — NOT in corpus);
    D-295 prints only the 25/50/25 financing proportions; **no tope máximo
    exists; base floor = salario mínimo AG vigente**. Acquisition
    candidate: the JD reglamento (igssgt.org legislación section).
12. ~~OQ12: IRTRA cuota mensual brackets~~ **DISPROVEN + RESOLVED
    2026-08-19 (W-GT3)**: no bracket table exists — IRTRA = **flat 1% on
    total planillas** (D-1528 art. 12 as reformed by D-43-92). Identity
    correction: the law is **Decreto 1528 (29-May-1962)**, not "Decreto
    15 de 1928" (registry misread; source URL filename itself carries
    1528). AG 5/6-2005 = governance only. Pre-reform D-43-92 text outside
    corpus (minor).
13. ~~OQ13: IVA-retention percentage + ISR retention rates~~ **RESOLVED
    2026-08-19 (W-GT2 evidence, both halves, verbatim)**: IVA = D-20-2006
    arts. 1-6 (**% OF THE IVA**, not base): 65% exportadores agropecuarios +
    D.29-89 empresas / 15% otros exportaciones + especiales + otros agentes /
    25% sector público (munis excepted) / 15% operadoras de tarjeta (afiliado
    liable for 85% not retained) / 1.5% sobre el VALOR TOTAL for fuel-card;
    Q2,500 de minimis (art. 10); declare primeros 15 días hábiles. ISR =
    LAT arts. 44/73/75-82/90-94/104: asalariados 5%/Q15,000+7% (annual
    Q300,000 bracket, projection/12), Opcional 5/7% monthly Q30,000, capital
    10% + dividends 5%, no-residentes 5/3/10/15/25, facturas especiales 5%
    definitive. Full tables in `gt/.extractions/78_79_Retenciones_IVA…` and
    `26_28_47_LAT_ISR…`.
14. **OQ14**: AML identifiers (D-67-2001? AG 75-2006? Art. 51 Q2,000
    efectivo-documentation rule?) — legal.dca.gob.gt browser hunt.
15. **OQ15**: ZF successor law ("Decreto 16-2022"?) unverified; AG 65-2022
    reformed AG 242-90 reglamento (our copy predates it) — acquire AG 65-2022
    (MINFIN page → PDF) + verify successor-law status via DCA.
16. **OQ16**: Reglamento del Código de Comercio — does a numbered instrument
    exist? (No candidate found in any official sweep.)

## Acquisition log (additions)

- 2026-08-18 (W3/W4/W5 bulk acquisition) — **36 files registered** (32-36,
  38-40, 42-57, 59-66, 67-73; gaps 37/41/58 reserved-pending). Live-direct:
  igssgt/irtra/intecap/mineco. Wayback: SAT portal + mintrabajo + minfin + RM
  (each with snapshot provenance + re-verify flags). Incidents: (a) web
  .archive.org rate-limited mid-batch — sequential retry recovered all; (b)
  large-file truncation at exact 1/5MiB boundaries on some id_ captures —
  fixed via alternate captures (65 via 2022 capture; 66 via 2024-06-12; 32
  via plain re-fetch); (c) 39's 2024 capture = HTML stub (mintrabajo site
  rebuild) — 2022 PDF capture used; (d) IRTRA wp-content 403s plain curl —
  browser-UA + referer worked. **Corpus now 66 files + 2 dirs.**

## Wave log (continued)

### 2026-08-19 — owner DCA browser batch (12 registered, 6 rejected/dropped)

Registered: 37 (AG 256-2025 salario 2026), 41 (D-78-89 bono 14), 58 (LET
IVA-General manual), 74 (**D-10-2025 — Reformas Ley Alimentación Escolar +
LEY IVA: derogates Art. 3-"A"** — the W1-L23 "2025 IVA reform" lead
CONFIRMED), 75 (D-67-2001 AML), 76 (D-51-2001 AML-penal, título to pin),
77 (**D-15-2026 Ley Integral AML — NEW 2026 regime**, activos virtuales,
casas de empeño; likely supersedes 75_), 78 (D-20-2006, 45pp — the
IVA-retenciones basis), 79 (AG 425-2006 reglamento), 80 (**D-6-2021 =
Reformas Ley Zonas Francas** — OQ4 RESOLVED: NOT an e-invoicing mandate; ZF
chain = D-65-89 → D-19-2016 → D-6-2021), 81 (AG 65-2022 = **ZOLIC** reform —
the W5 "ZF reglamento reform AG 65-2022" hypothesis RETIRED), 82 (LET
regímenes especiales manual), 83 (RM edictos gazette snapshot).
Rejected: D-73-2000 (treaty approval), D-7-2000 (aviation treaty), SINAS
reglamento (off-scope); dropped 3 duplicates (20-2006 10pp scan, 242-90 7pp,
LET-pequeño md5-identical).

### 2026-08-19 — owner-supplied link leads (assessed, NOT registered)

- `sites.google.com/capacitacionessat.page/...` (SAT-2237 llenado course) —
  Google Sites on custom .page domain, SAT-branded. **LEAD pending
  ratification** (like OQ1 GitHub): verify it's linked from sat.gob.gt or
  SAT-owned before any use; then it could yield instructivo-equivalent
  material.
- `portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/` —
  official FAQ; optional page snapshot (browser save) — queue C item.
- `diamantecontador.com` (2 forum threads re SAT-1321/ISR exterior) —
  non-official forum: LEAD only, never registrable; useful as hint for
  instructivo content gaps.
- `corporacionbi.com` calendario SAT agosto-2026 + `atlas.com.gt`
  calendario-tributario (year/month selector, works back from 2026-08) —
  non-official reproductions of SAT vencimiento windows. **LEAD**: atlas's
  back-year selector could let us transcribe the per-NIT-digit windows for
  validation; MUST be confirmed against SAT's JSF app or by the GT
  accountant before any FR trusts it (non-official data can lag/err).

## Open questions (updates)

- ~~OQ4 (D-6-2021 e-invoicing mandate?)~~ **RESOLVED 2026-08-19**: D-6-2021
  = reformas a la Ley de Zonas Francas (80_). NOT an e-invoicing mandate;
  the FEL mandate chain remains AD 13-2018 + SAT-DSI resolutions 04_-14_.
- OQ14 (AML): PARTIALLY RESOLVED — D-67-2001 (75_) + D-51-2001 (76_) +
  D-15-2026 (77_) acquired; REMAINS: derogation inventory of D-15-2026, its
  reglamento status, AG 75-2006 applicability, Q2,000-cash threshold wording
  → evidence pass + possible accountant confirm.
- OQ15 (ZF successor): AMENDED — no "Decreto 16-2022" replacement; chain =
  D-65-89 → D-19-2016 → D-6-2021 (80_); AG 242-90 reglamento reform status
  still open (AG 65-2022 turned out ZOLIC-specific).
- ~~OQ17 (new): Ley IVA 27-92 Art. 3-"A" history~~ **RESOLVED-AS-MYTH
  2026-08-19 (W-GT2, verbatim in 74_ resolutivo)**: D-10-2025 derogates IVA
  **Art. 8-"A"** — "Se deroga el artículo 8 'A' de la Ley del Impuesto al
  Valor Agregado" — NOT "Art. 3-'A'" (the W1-L23 lead was wrong; join the
  rejected-myths list). Art. 8-"A" was added by **D-31-2024 (Ley para la
  Integración del Sector Productivo Primario y Agropecuario) art. 13**
  (MINEDUC alimentación-escolar retention); D-10-2025 also deroga the LAE
  D-16-2017 art. 16 final ¶ (same D-31-2024 lineage). **D-31-2024 full text
  = new acquisition candidate** (it is also the Reglas-v2.0 DTE-type source:
  FEPE/FARP/FCRP/FPEC/FCPC). The consolidated-IVA hunt (OQ10) continues for
  Art. 29-"A" text + D-31-2024 layers.
- **OQ18 (new, W-GT4)**: 5% IVA-retention rates printed by 49_/52_
  (Pequeño Contribuyente suppliers, ops ≥ Q2,500.01; Régimen Especial
  Agropecuario, on total factura) vs the W-GT2-resolved D-20-2006/AG
  425-2006 matrix (65/15/25/15/1.5 + Q2,500 abstention, AG 5-2013 art. 49).
  The 5% rows look like additional regimes, not contradictions — reconcile
  against LIVA/Reglamento law text (23_/24_, both in corpus) before
  synthesis merges them into the retention-rate catalog. Related: 52_ prints
  the "art. 54 B" D-27-92 full-accounting agent path ("54 B" vs "54 BIS"
  nomenclature needs the post-2018 consolidated IVA print, OQ10 kin).
- **W-GT4 evidence-file OQs**: ~45 per-file OQ-1..OQ-n live across the 6
  W-GT4 evidence files — MOQ-roll into a master index at synthesis prep
  (SV pattern; same as W-GT1..3's ~95).
