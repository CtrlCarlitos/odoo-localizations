# Honduras — Source Research Dossier

**Research pass:** 2026-08-18/19, branch `hn-research` (session: HN bootstrap).
Companion to `sources/README.md` (the registry) and `EXTRACTION_PLAN.md`
(the Stage 0 plan). This file records HOW the corpus was found, what was
rejected and why, and what remains open.

---

## 1. Sites visited and what they yielded

| Site | Status | Yield |
|------|--------|-------|
| **sar.gob.hn** (WordPress + wp-download-manager) | OK | Core corpus: 84 of 85 files. `/leyes/` = 420-entry catalog of laws/acuerdos (each with wpdmdl download); topic pages (ISR, ISV, DMR, DMC, facturación, otros tributos, contribuciones, ATC, régimen simplificado, isr-2025) carry curated download sets + "Ayuda"/"Generalidades" form docs. Site-wide banner: ISR FY2025 declaration due 30-abr-2026 (calendar FY = calendar year) |
| **oficinavirtual.sar.gob.hn** (Nuxt SPA) | OK | Route table extracted from JS bundles: `declaracion-determinativa(-new-rect)`, `declaracion-informativa(-djisf/-eeff)`, `declaracion-renta-pj/pn(+rectificar)`, `csv` (Verificador de Documentos SAR), `consulta-retenciones`, `/fac/*` (facturación/imprentas workflow: inscripción, autorización, imprentas certificadas, validador-doc-fiscales, notificación no-usados, seguimiento), `calendario-fiscal`, cms/anuncios. API base: `oficinavirtualapipre.sar.gob.hn/api` (preprod name; production base to confirm). Login-walled — declaration form structures live behind auth |
| **congresonacional.gob.hn** | DOWN (000, all schemes) | Nothing. Known-flaky (like SV's asamblea outage). Law consolidations obtained via SAR instead |
| **stss.gob.hn** | DOWN (000) | Nothing. Salario mínimo instruments obtained from SAR catalog (SETRASS acuerdos); STSS reglamento del CT NOT acquired (open) |
| **ihss.hn** | OK (needs UA; 403 bare curl) | Ley del Seguro Social published as **KB page text** (not PDF) under BetterDocs (`/docs/ley-del-seguro-social/`) — D. 140-1959 base + reform D. 80-2001 typed into the page; afiliación procedures page. No rates/reglamentos PDFs found on site |
| **inprema.gob.hn** | OK | Laws section exists but downloads are JS-driven — not fetched (open lead; niche sector regime) |
| **rap.hn** (RAP institution) | OK | Institutional history (D.167-91 FOSOVI → Ley RAP D.107-2013 → D.56-2015 → D.47/48-2024), operational docs only; no law PDFs |
| **cnbs.gob.hn** + circulares.cnbs.gob.hn | OK | Financial-sector laws + circulars (previsión institutes' investment rules). No Ley RAP text |
| **tsc.gob.hn/biblioteca** (Joomla, ~1,550 docs) | OK | Código del Trabajo (CEDIJ print, `web/leyes/codigo_de_trabajo.pdf`), Código Tributario alt copy, Constitución, codes list. Search module inert (returns defaults); no Código de Comercio, no Ley RAP |
| **sefin.gob.hn** | OK | `/normativa/` exists; no comercio/trabajo yields |
| **lagaceta.hn** | — | **NOT the gazette** — a news outlet ("Información sin filtros"). No free official La Gaceta archive found; SAR's own gazette-extract PDFs (most of the corpus) are the practical route |
| tsc/cnj power-search engines (Bing/DDG-html via fetcher) | Blocked/useless | DDG captcha; Bing mangled queries. Manual navigation won |

## 2. E-invoicing scope finding (decision-relevant)

**Honduras has no national XML/DTE electronic-invoicing regime in force as of
2026-08-19.** Evidence:

- sar.gob.hn `/facturacion/` = the **paper régime** (imprentas, autoimpresores):
  Reglamento Acuerdo 481-2017 (+189-2014 superseded, +609/725/817 reforms,
  +231-2020 transitory) and its "Ayuda" workflow docs.
- Zero occurrences of facturación-electrónica technical documentation
  (no XML/XSD/catalogs/validación packages) anywhere on SAR's site; the
  wp-search API returns nothing for the phrase; news search confirms.
- The Oficina Virtual `/fac/*` app digitizes the **authorization workflow**
  (inscripción al régimen, imprentas, validador de documentos fiscales =
  verification of printed/authorized documents), plus `csv` = Verificador de
  Documentos Emitidos por el SAR. RECAEFUSAR page is an empty shell (carousel
  only).
- invoicing-relevant reporting: DMC (purchases) + DMR/DJIMR (retenciones)
  informativas are the transaction-detail pipeline (SV F-anexo kin).

**Consequence:** HN "e-invoicing" requirements = the digital administration of
the paper regime (authorization numbers, imprentas, rangos, validador checks,
notificaciones) — NOT a transmission/SEAL stack like SV. The repo-structure
spec's "HN e-invoicing: No" is superseded by the 2026-08-18 HN design spec:
topic in scope, content = paper-regime digitalization. **Watch:** SAR pilots
or an FE law could appear — re-check `/facturacion/` + wp-search quarterly.

## 3. Key landscape findings (beyond the corpus)

- **Tax authority lineage:** DEI → SAR (D. 170-2016 created SAR, 2017). Old
  DEI-era instruments remain partially operative (DEI-SG-276-2015 DMC,
  DEI-SG-279-2015 compras eventuales, DEI-9382-J-2003 tarjetas).
- **Código Tributario = D. 170-2016** (not the DEI-era D. 51-2003). Newest
  consolidation on offer: hasta D. 180-2020 (`03_`); Art. 206 void (2023
  sentencia, `23_`). Post-2020 CT reforms: verify per-article at evidence.
- **ISR = Decreto-Ley 25 (1963)** — consolidation hasta SAR-07-2025 (`01_`).
  Asalariados scale IPC-indexed annually: SAR-014-2023 (FY2023, mechanism
  start) → SAR-07-2024 → SAR-07-2025 → **SAR-01-2026 (+4.98%, operative
  now)**. Renta de capital 10% + 1% retención-anticipo family: D. 17-2010 +
  Reglamento 1121-2010 + D. 28-2019 interpretación + D. 31-2018 (22-A 1.5%).
- **ISV = Decreto-Ley 24 (1963)** — consolidation hasta D.L. 59-2022 (`02_`).
  15% standard (verify in-file); selectivo/IPC family (005-2017, 172-2022,
  014-2023, 218-2024) available in catalog for a later wave; exoneraciones
  list = Acuerdo Ejecutivo 005-2014 (+352-2022 café) — catalog, not core.
- **ISR tables print as IMAGES** in the SAR acuerdos (text layer carries
  considerandos but the table is an image on at least SAR-01-2026/SAR-07-2025)
  — OCR/PSM at extraction; the XLSX plantilla (`11_`) cross-checks the math.
- **Payroll 2024 architecture (post-D.56-2015 void):** IHSS (D. 48-2024:
  ceilings EM/IVM L.11,903.13 for 2025, Junta Directiva adjusts after) +
  RAP-IVM individual accounts (Ley RAP D.L. 107-2013; Art. 43 as reformed by
  D. 47-2024: 1.5% + 1.5%) + Fondo de Reserva Laboral (D. 47-2024: employer
  4%, ceiling 3× top SMM, RAP-administered; CT-Art.-95-pact grandfathering) +
  sector exceptions (INJUPEMP/INPREMA/IPM/INPREUNAH). D. 40-2026 adds a
  6-month RAP regularization + FOVIIF integration. **Honduras has NO
  December double-bonus law like SV/GT** — aguinaldo = 13th month (CT Art.
  376-family, "decimotercer mes"), no 14th; cesantía is the RAP fondo.
- **Salario mínimo:** bienio instrument SETRASS-109-2024 (2024-2025, `82_`)
  still current as of Feb-2026 (SAR-43-2026 cites its promedio L.13,985.16);
  2026-2027 successor NOT yet published at research date — watch.
- **LJT (Ley de Justicia Tributaria):** pending bill (transparency/MAAC/
  bearer-shares/bank-info), unapproved as of 2025-09; advocacy posts on SAR
  site. Watch for passage — would be a major reform event.
- **Chart of accounts:** no statutory PCG found; Honduran books follow Código
  de Comercio accounting articles + NIF (CPMCP private standards; cpmcp.hn
  down at research). Expected thin; open lead.
- **Special regimes available in SAR catalog for later waves:** ZOLI (Ley +
  Reglamento 041-2020), RIT (D. 37-1984 + D. 2-2026 five-year extension),
  Zonas Agrícolas de Exportación (D. 233-2001), ZOLITUR (ganancia capital
  120), ZEDE (repealed/2022+ — estudios only on site), maquila ISV
  exemptions (1375-2002 etc.).

## 4. Rejected / not pursued (with reasons)

| Candidate | Reason |
|-----------|--------|
| SAR "documentos-y-estudios" (51 items: informes mensuales de ventas, coyuntura, evasión studies, ZEDE análisis) | Economic analysis, not law — no LB value for requirements |
| 2018-2022 ISR consolidations (SAR-022-2021, SAR-020-2022, SAR-014-2023 vintages) | Superseded by `01_` (hasta SAR-07-2025). Kept only the table-acuerdo series + the 2022 table as historical |
| ISR table años 2018/2020 (SAR-009-2018, SAR-014-2020) | Superseded pre-IPC vintages; reconstructable from D. 31-2018 chain if needed |
| Energy-law family (D. 70-2007 etc., 30+ entries) | Sector-specific exoneraciones — special-regimes wave, not core |
| Presupuesto/reglamento family (dozens) | Public-budget execution — out of scope |
| Resolución DEI-9382-J-2003 (tarjetas base procedure) | **Wanted but absent** from SAR catalog (only its 2024 amendments) — open lead |
| Ley del Seguro Social (IHSS site KB text) | Page text, not PDF — capture as snapshot only if D. 140/80-2001 needed at payroll evidence; D. 48-2024 covers rates/ceilings |
| CNBS circulars (previsión investments etc.) | AFP/institutional regulation, not employer-facing |
| INPREMA laws | JS-driven downloads + niche sector (teachers) — open lead |
| honducompras / citas / denuncias / transparency portals | Not localization-relevant |

## 5. Open leads (acquisition candidates ≥87)

1. **Resolución DEI-9382-J-2003** — ISV tarjetas base procedure (La Gaceta
   01-nov-2003). Route: La Gaceta (no free archive found) or SAR re-publication.
2. **Ley del RAP, D.L. 107-2013** full text — needed for payroll wave beyond
   the Arts. 42/43/61 transcription in `27_`. Routes: TSC biblioteca deep
   crawl (pagination start=0..1510), UPAP (down), La Gaceta 06-sep-2013.
3. **Código de Comercio** (D. 4-1950 + reforms) — commercial-legal wave;
   Congreso (down) / CEDIJ (absent) / law-school mirrors (non-official).
4. **Reglamento General IHSS + rate-setting resolutions** (the 3.5%/1.5%
   EM split and current operative instruments; D. 48-2024 ceilings acquired).
5. **Salario mínimo 2026-2027** bienio instrument — expected late-2025/2026;
   watch SAR catalog + SETRASS (site down; Gaceta when published).
6. **Decreto 93-2021** (CT article derogations, La Gaceta 35,760) — fetch
   failed (wpdmdl absent); retry or Gaceta route. Number 85 reserved.
7. **Calendario fiscal (vencimientos)** — Oficina Virtual SPA (login-free
   route exists: `/calendario-fiscal`); capture at evidence pass; API base
   `oficinavirtualapipre.sar.gob.hn/api` (confirm prod).
8. **LJT bill tracking** — if passed, re-research taxation core.
9. **INPREMA / INJUPEMP / IPM** sector regimes — only if payroll scope
   includes public-sector/teachers.
10. **Reglamento del Código de Trabajo / STSS resolutions** (vales de
    alimentación L. 632-2? etc.) — STSS down; Gaceta route at payroll wave.

## 6. Fetch recipes (verified this pass)

- **SAR downloads:** resolve the target `/download/<slug>/` page live →
  extract the fresh `?wpdmdl=<id>&refresh=<token>` href (tokens rotate; IDs
  drift — never hard-code) → GET → verify page 1 with pypdf. Some slugs in
  the catalog are stale (no wpdmdl link renders) — treat as unavailable, note
  and move on. Scripts used: `/tmp/opencode/hn/{build_map,fetch_sar,batch_fetch}.py`
  (throwaway; regenerate as needed).
- **ihss.hn:** needs full browser UA (403 otherwise).
- **WordPress sites:** `/wp-json/wp/v2/search?search=...` works on sar.gob.hn
  and ihss.hn — faster than HTML grep for page discovery.
- **TSC biblioteca:** Joomla; finder search inert — use category listings +
  `?start=N` pagination; PDFs live under `/web/leyes/`.
- **La Gaceta:** no free official archive located; SAR's gazette-extract PDFs
  (most corpus files) are official republished copies and carry gazette
  numbers/dates — cite those.
