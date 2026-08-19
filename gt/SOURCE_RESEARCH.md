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
   `gt/DOWNLOAD_QUEUE.md` (01–28 + optional 31); inbox staging
   `gt/sources/inbox/` (git-ignored until verified).
3. **OQ3 (SHARPENED — material)**: cat.desa vs GitHub drift is 8-of-17 shared
   files (measured 2026-08-18): GT_Documento-0.2.1 (52,176 vs 67,278 B),
   Exportaciones, MediosdePago, PartidosPoliticos, AnulacionDocumento,
   ExportacionProvisional (1 byte), catalogoMensajes, unidadesGravables;
   plus 11 GitHub-only files + Frases 0.1.2-vs-0.6.0. Which set does
   production validation use? → ask TotalDoc (partner) / SAT.
4. **OQ4**: "Decreto 6-2021" — verify via DCA browser session; until then
   untouchable.
5. **OQ5**: Reglas y validaciones current internal version + date — read
   from PDF after acquisition (pages show nothing).
6. **OQ6**: doc-type abbreviations (FPEQ/FCEQ/RD…) — confirm inside Reglas
   PDF; never hard-code from hearsay.
7. **OQ7**: Grupo CDS authorization expires 02/12/2026 — renewal watch
   (registry page re-check at milestone).
8. **OQ8**: FELPLEX (utm_source seen) — unknown internal SAT/certifier
   portal; ignore unless it surfaces again.

## Acquisition log

- 2026-08-18 — `29_FEL_XSD_cat_github_961133c/` (25 XSD + 3 JSON, pinned
  commit 961133c 2026-08-04) + `30_FEL_XSD_cat_catdesa/` (18 files, direct
  download) acquired + PROVENANCE.md each + registry rows. Controller-side
  verification: clone SHA checked; cat.desa files probed filename-by-filename
  (misses recorded); byte-diff measured → OQ3.
- 2026-08-18 — Manual queue (28 items + optional) handed to owner
  (`gt/DOWNLOAD_QUEUE.md`); inbox/ staged + git-ignored.

