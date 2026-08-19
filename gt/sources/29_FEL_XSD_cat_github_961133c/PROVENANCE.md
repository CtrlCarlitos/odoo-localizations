# PROVENANCE — 29_FEL_XSD_cat_github_961133c

FEL XSD schemas (25) + JSON catalogs (3) snapshot of the SAT-maintained
GitHub repository **notificacioneselectfel/Catalogo-FEL**, branch `main`.

- **Repo**: https://github.com/notificacioneselectfel/Catalogo-FEL
- **Pinned commit**: `961133c2d62717fab415a8255e9aabaa4f57b9eb`
  (commit date 2026-08-04T16:04:42-06:00; latest at retrieval)
- **Retrieved**: 2026-08-18 (git clone, files copied verbatim)
- **Official status**: README (as shown) — "Este repositorio es mantenido por
  la **Gerencia de Informática de la SAT** para compartir oficialmente los
  archivos de definición de esquemas (XSD) y catálogos (json)… Branch para
  versión 2 !!!". Linked from SAT's own Documentación Técnica del Régimen FEL
  portal page for every schema/catalog item. **Ratified official channel**
  (ruling OQ1, 2026-08-18: product owner approved GitHub + cat.desa dual
  acquisition; drift between the two hosts tracked as OQ3).

## Contents (verbatim from repo at pinned SHA)

- `XSD/`: 25 files — GT_Documento-0.2.1.xsd (main DTE), GT_AnulacionDocumento-0.1.0,
  GT_ReversionDocumento-0.1.0, GT_Endoso-0.1.0, GT_AnulacionEndoso-0.1.0,
  GT_PagoEndoso-0.1.0, 15 complements (Cambiaria, Exportaciones,
  ExportacionProvisional, Fac_Especial, Referencia_Nota,
  ReferenciaBoletaDespacho, ReferenciaConstancia, MediosdePago,
  CobroXCuentaAjena, Espectaculos, PartidosPoliticos, TurismoPasaje,
  GasLicuadoPetroleo, AlmacenajeGalonaje, RetencionesFacturaEspecifica),
  GT_ComplementoAlItem, GT_ComplementoDetalleProductos-0.1.0,
  GT_ComplementoTrasladoMercancias-0.1.0, xmldsig-core-schema.xsd
- `Catalogos/`: catalogoMensajes-0.3.0.json, catalogoUnidadesGravables-0.1.4.json
  (in-file header "Ultima Actualizacion": 23/08/2022 11:00:00),
  CatalogoFrases-0.6.0.json
- Filenames flattened into this directory (repo subdirs XSD/, Catalogos/
  noted above).

## Drift vs cat.desa snapshot (30_) — measured 2026-08-18

DIFF (same filename, different bytes): GT_Documento-0.2.1.xsd (67,278 vs
52,176), GT_Complemento_Exportaciones (7,897 vs 5,359),
GT_Complemento_MediosdePago (2,536 vs 3,169), GT_Complemento_PartidosPoliticos
(2,903 vs 3,198), GT_AnulacionDocumento (8,781 vs 8,771),
GT_Complemento_ExportacionProvisional (4,034 vs 4,035 — 1 byte),
catalogoMensajes-0.3.0.json, catalogoUnidadesGravables-0.1.4.json.
GitHub-only (absent on cat.desa): 3 endoso XSDs, GasLicuadoPetroleo,
AlmacenajeGalonaje, RetencionesFacturaEspecifica, ReferenciaBoletaDespacho,
ComplementoAlItem, ComplementoDetalleProductos, ComplementoTrasladoMercancias,
CatalogoFrases-0.6.0 (cat.desa hosts 0.1.2).

**Open question OQ3 (unresolved)**: which set does production validation use?
GitHub main = "versión 2" and is actively maintained; cat.desa ("desa" =
development environment naming) lags but sits on a .gob.gt host. Do not
silently prefer either until SAT/certificador confirms; requirements
synthesis must treat this as a dated-authority question.
