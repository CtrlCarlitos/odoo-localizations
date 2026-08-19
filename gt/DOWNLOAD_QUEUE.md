# GT — Manual Download Queue (ruling OQ2)

`portal.sat.gob.gt` blocks all non-browser clients (Cloudflare). Per ruling
OQ2 you download these in a normal browser; I verify (page-1 read), rename to
`NN_...`, register, and commit.

**How**: open each URL → save the PDF/ZIP (keep the original filename, or the
NN_ name — either works) → drop files into:

```
/home/carlitos/projects/CtrlCarlitos/odoo-localizations/.worktrees/gt-research/gt/sources/inbox/
```

Unverified inbox files are git-ignored; they leave the inbox only after
verification + registry.

## Priority A — laws + core specs (gate W1 evidence and W2)

| # | Save as | URL |
|---|---------|-----|
| 01 | 01_AD_13-2018_FEL.pdf | https://portal.sat.gob.gt/portal/descarga/1897/normativa-sat/25094/acuerdo-de-directorio-13-2018.pdf |
| 02 | 02_AD_26-2019_FEL_reformas.pdf | https://portal.sat.gob.gt/portal/descarga/1897/normativa-sat/45898/acuerdo-de-directorio-26-2019-reformas-al-regimen-de-factura-electronica-en-linea-fel.pdf |
| 03 | 03_AD_15-2020_FEL.pdf | https://portal.sat.gob.gt/portal/descarga/1897/normativa-sat/49283/acuerdo-de-directorio-numero-15-2020.pdf |
| 15 | 15_FEL_Reglas_y_validaciones.pdf | https://portal.sat.gob.gt/portal/descarga/14852/reglas-y-validaciones/85864/reglas-y-validaciones-fel-3.pdf |
| 16 | 16_FEL_DocTecnico_Servicios.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/25830/documento-tecnico-servicios-sat.pdf |
| 23 | 23_Ley_IVA_27-92.pdf | https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18270/decreto-numero-27-92-ley-del-impuesto-al-valor-agregado.pdf |
| 24 | 24_Reglamento_IVA_AG_5-2013.pdf | https://portal.sat.gob.gt/portal/descarga/1817/orientacion-legal-y-derechos-de-contribuyentes/53919/reglamento-de-la-ley-del-impuesto-al-valor-agregado-acuerdo-gubernativo-numero-5-2013.pdf |
| 25 | 25_Codigo_Tributario_6-91.pdf | https://portal.sat.gob.gt/portal/wpfd_file/codigo-tributario-decreto-numero-6-91 (a page — use its PDF download button; note the reform tail if the page shows one) |
| 26 | 26_LAT_10-2012.pdf | https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18261/decreto-numero-10-2012-ley-de-actualizacion-tributaria.pdf |
| 27 | 27_LAT_10-2012_consolidada_2017.pdf | https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/6432/decreto-10-2012-ley-de-actualizacion-tributaria-2017.pdf |
| 28 | 28_Reglamento_LAT_AG_213-2013.pdf | https://portal.sat.gob.gt/portal/descarga/1899/legislacion-tributaria/18250/ (exact file slug unconfirmed — if the URL 404s, portal-search "acuerdo gubernativo 213-2013" in Legislación Tributaria) |

## Priority B — FEL manuals + test vectors

| # | Save as | URL |
|---|---------|-----|
| 17 | 17_FEL_casos_de_prueba.zip | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/25545/fel-casos-de-prueba.zip |
| 18 | 18_FEL_guia_requisitos_minimos.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/77253/guia-de-requisitos-minimos-dte-2.pdf |
| 19 | 19_FEL_contingencia.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/38418/procedimiento-de-emision-de-documentos-en-contingencia.pdf |
| 20 | 20_FEL_anulacion_manual.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/72293/manual-de-usuario-factura-electronica-fel-anulacion-2.pdf |
| 21 | 21_FEL_firma_electronica_manual.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/75322/1-manual-de-usuario-fel-habilitacion-acreditacion-descarga-de-firma-electronica.pdf |
| 22 | 22_FEL_autorizacion_certificador.pdf | https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/80213/procedimiento-de-autorizacion-de-certificador.pdf |

## Priority C — incorporation resolutions (legal timeline)

| # | Save as | URL (all under …/descarga/1897/normativa-sat/) |
|---|---------|-----|
| 04 | 04_SAT-DSI-243-2019.pdf | 46321/resolucion-sat-dsi-243-2019-incorporacion-de-proveedores-del-estado-al-regimen-de-factura-electronica-en-linea-fel-2.pdf |
| 05 | 05_SAT-DSI-838-2019.pdf | 39867/resolucion-de-superintendencia-sat-dsi-838-2019-regimen-de-factura-electronica-en-linea-fel-incorpora-a-los-contribuyentes-que-proveen-servicios-profesionales-individuales-en-general.pdf |
| 06 | 06_SAT-DSI-639-2020.pdf | 17662/resolucion-superintendencia-sat-s-639-2011-funciones-de-unidad-de-informacion-publica.pdf ⚠ SAT's own link is MISLABELED (points at a 639-2011 PDF). Download what it serves; I verify. If wrong, search the portal for the real 639-2020. |
| 07 | 07_SAT-DSI-640-2020.pdf | 46215/resolucion-sat-dsi-640-2020-incorporacion-fel-emisores-face.pdf |
| 08 | 08_SAT-DSI-887-2020.pdf | 47495/sat-dsi-887-2020.pdf |
| 09 | 09_SAT-DSI-398-2021.pdf | 51799/resolucion-sat-dsi-398-2021-incorporacion-de-proveedores-del-estado-al-regimen-fel-proveedor-unico-arrendamiento-y-dragado.pdf |
| 10 | 10_SAT-DSI-1074-2021.pdf | 57857/resolucion-r-sat-dsi-1074-2021-incorporacion-por-servicios-y-bienes-relacionados-a-la-salud.pdf |
| 11 | 11_SAT-DSI-1218-2021.pdf | 57856/resolucion-r-sat-dsi-1218-2021-incorporacion-fel-contadores-auditores-y-firmas.pdf |
| 12 | 12_SAT-DSI-1240-2021.pdf | 57855/resolucion-r-sat-dsi-1240-2021-incorporacion-fel-contribuyentes-del-regimen-general-del-iva.pdf |
| 13 | 13_SAT-DSI-1350-2022.pdf | 66005/resolucion-sat-dsi-1350-2022-incorporacion-fel-de-pequenos-contribuyentes.pdf |
| 14 | 14_SAT-DSI-400-2023.pdf | 69739/resolucion-sat-dsi-400-2023-ampliacion-para-incorporacion-a-fel-de-pequenos-contribuyentes-del-iva.pdf |

(C table prefix: https://portal.sat.gob.gt/portal/ )

## Optional (grab if convenient)

- 31_certificadores_dte.html — https://portal.sat.gob.gt/portal/certificador-de-dte/ (Save page as… → single-file HTML; registry snapshot)
- While on the portal, if you pass the Legislación Tributaria listing: any post-2017 reform files for Dto. 10-2012 / 27-92 / 6-91 (W1-L23 flagged a 2025 "Reformas a la Ley del IVA y Código Tributario" SAT event — the decrees behind it are acquisition leads)
