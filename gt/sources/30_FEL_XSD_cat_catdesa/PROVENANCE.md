# PROVENANCE — 30_FEL_XSD_cat_catdesa

FEL XSD schemas + JSON catalogs as served by the official SAT host
**cat.desa.sat.gob.gt** (direct download, no bot block; "desa" = development
environment naming — see OQ3).

- **Base URLs**: `https://cat.desa.sat.gob.gt/xsd/alfa/<file>` (XSD) and
  `https://cat.desa.sat.gob.gt/catalogos/alfa/<file>` (JSON)
- **Retrieved**: 2026-08-18 (direct curl; HTTP 200, bytes verbatim)
- **Coverage**: 18 files present out of the 28 published on the SAT GitHub
  channel (see 29_). Files NOT served by cat.desa (probed, missing):
  GT_Endoso-0.1.0, GT_AnulacionEndoso-0.1.0, GT_PagoEndoso-0.1.0,
  GT_Complemento_GasLicuadoPetroleo, GT_Complemento_AlmacenajeGalonaje-0.1.0,
  GT_Complemento_RetencionesFacturaEspecifica,
  GT_Complemento_ReferenciaBoletaDespacho-0.1.0, GT_ComplementoAlItem,
  GT_ComplementoDetalleProductos-0.1.0, GT_ComplementoTrasladoMercancias-0.1.0,
  CatalogoFrases-0.6.0 (cat.desa hosts **0.1.2** instead — included here).

## Contents

15 XSD + 3 JSON (see drift table in 29_/PROVENANCE.md). No directory listing
exists on the host; the file list was enumerated by probing every filename
from the GitHub snapshot (200 = present, 403/404 = absent).

**Open question OQ3 (unresolved)**: cat.desa content differs from the GitHub
channel for 8 of 17 shared files (different bytes, same filename/version
label) — including the main GT_Documento-0.2.1.xsd (52,176 B here vs 67,278 B
on GitHub). Which set production validation uses is unconfirmed. Treat both
as dated-pending until SAT or a certificador (TotalDoc) answers.
