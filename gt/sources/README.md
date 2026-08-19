# Sources — Guatemala

Original, unmodified documents from the Guatemalan tax authority (SAT) and
related official bodies. Never edit files here; parsers must treat them as
read-only.

## Registry

| File | Topic | Title | Issued | Retrieved | Provenance (URL) |
|------|-------|-------|--------|-----------|------------------|
| 01_AD_13-2018_FEL.pdf | e-invoicing | Acuerdo de Directorio 13-2018 — creates Régimen FEL (certified copy; in force 23-May-2018 per SAT) | 2018 | 2026-08-18 | https://portal.sat.gob.gt/portal/descarga/1897/normativa-sat/25094/acuerdo-de-directorio-13-2018.pdf |
| 02_AD_26-2019_FEL_reformas.pdf | e-invoicing | AD 26-2019 — reformas al Régimen FEL (DCA gazette print N° 54, 27-nov-2019; scanned, OCR OK) | 2019 | 2026-08-18 | …/1897/normativa-sat/45898/acuerdo-de-directorio-26-2019-reformas-al-regimen-de-factura-electronica-en-linea-fel.pdf |
| 03_AD_15-2020_FEL.pdf | e-invoicing | AD 15-2020 — reformas FEL; amplía requisitos Certificadores (DCA print N° 6, 25-nov-2020; scanned, OCR OK; cites Ley IVA Art. 29-"A") | 2020 | 2026-08-18 | …/1897/normativa-sat/49283/acuerdo-de-directorio-numero-15-2020.pdf |
| 15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf | e-invoicing | Reglas y Validaciones FEL, **v1.7.10 Febrero 2025** (146pp; header also prints "VERSIÓN 2.0" — evidence pass to reconcile; supersedes 1.7.9) | 2025-02 | 2026-08-18 | …/14852/reglas-y-validaciones/85864/reglas-y-validaciones-fel-3.pdf |
| 16_FEL_DocTecnico_Servicios.pdf | e-invoicing | Documento Técnico Servicios SAT (SAT↔certificador webservice spec; 27pp — updated vs 20pp 2020 archive) | n/s | 2026-08-18 | …/6524/factura-electronica-fel/25830/documento-tecnico-servicios-sat.pdf |
| 18_FEL_guia_requisitos_minimos.pdf | e-invoicing | Guía de requisitos mínimos en los DTE-FEL, representación gráfica (8pp) | n/s | 2026-08-18 | …/6524/factura-electronica-fel/77253/guia-de-requisitos-minimos-dte-2.pdf |
| 22_FEL_autorizacion_certificador.pdf | e-invoicing | Procedimiento de Autorización del Certificador (42pp — updated vs 20pp archive) | n/s | 2026-08-18 | …/6524/factura-electronica-fel/80213/procedimiento-de-autorizacion-de-certificador.pdf |
| 24_Reglamento_IVA_AG_5-2013.pdf | taxation | Reglamento de la Ley del IVA, Acuerdo Gubernativo 5-2013 (26pp, dated 4-ene-2013; considerandos cite Decretos 4-2012 + 10-2012) | 2013-01-04 | 2026-08-18 | …/1817/orientacion-legal-y-derechos-de-contribuyentes/53919/… |
| 25_Codigo_Tributario_6-91.pdf | taxation | Código Tributario, Decreto 6-91 (95pp; **reform tail UNVERIFIED — check in Stage 1**) | 1991 (reforms?) | 2026-08-18 | https://portal.sat.gob.gt/portal/wpfd_file/codigo-tributario-decreto-numero-6-91 |
| 28_Reglamento_LAT_AG_213-2013.pdf | taxation | Reglamento del Libro I (ISR) de la Ley de Actualización Tributaria Dto. 10-2012, AG 213-2013 (40pp, dated 8-may-2013) | 2013-05-08 | 2026-08-18 | …/1899/legislacion-tributaria/18250/… |
| 29_FEL_XSD_cat_github_961133c/ | e-invoicing, catalogs | FEL XSD schemas (25) + JSON catalogs (3) — SAT Gerencia de Informática GitHub channel, pinned commit 961133c (2026-08-04) | repo commit 2026-08-04 | 2026-08-18 | https://github.com/notificacioneselectfel/Catalogo-FEL (ratified official channel, ruling OQ1) — see PROVENANCE.md |
| 30_FEL_XSD_cat_catdesa/ | e-invoicing, catalogs | FEL XSD schemas (15) + JSON catalogs (3, incl. CatalogoFrases-0.1.2) — official cat.desa.sat.gob.gt host | n/a (host shows no dates) | 2026-08-18 | https://cat.desa.sat.gob.gt/xsd/alfa/ + /catalogos/alfa/ — see PROVENANCE.md |
| 31_certificadores_dte_snapshot_2026-08-18.html | e-invoicing | Registro de Certificadores de DTE — SAT registry page snapshot (18 entities incl. GRUPO CDS S.A./TotalDoc NIT 107902281, auth. 02/12/2021→02/12/2026) | live 2026-08-18 | 2026-08-18 | https://portal.sat.gob.gt/portal/certificador-de-dte/ |

Prefix `…` = `https://portal.sat.gob.gt/portal/descarga/`. "n/s" = not shown on doc/pages.

**Numbering allocation (W1, 2026-08-18)**: 01–03 FEL acuerdos de directorio,
04–14 incorporación resolutions SAT-DSI, 15 Reglas y validaciones, 16 Doc.
Técnico Servicios, 17 casos de prueba, 18 guía requisitos mínimos,
19 contingencia, 20 anulación manual, 21 firma electrónica manual,
22 autorización certificador, 23–28 core tax laws (IVA/CT/LAT + reglamentos),
29–30 acquired above, 31 certificador-registry snapshot (optional).
Files land here as manual browser downloads (portal.sat.gob.gt blocks
non-browser clients — ruling OQ2); each is verified by page-1 read before the
row is finalized. Inbox staging: `inbox/` (unverified).

When adding a document: keep its original filename (prefix with `YYYY-MM-DD_`
only if it would collide), place it in this directory, and add a registry row.
