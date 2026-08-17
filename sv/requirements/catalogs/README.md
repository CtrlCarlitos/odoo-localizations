# Requirements — MH Catalogs (El Salvador)

Machine-readable sidecars of the official MH catalogs used across DTE
structures and events. Generated from
[sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx](../../sources/)
(**Catálogos v1.1, 2026 re-versioning**, PDF overlay where the workbook is
incomplete) by [shared/scripts/build_catalogs.py](../../../shared/scripts/).
See `_INDEX.md` for the file/row map and applied corrections.

**Supersession:** v1.1 (2026) REPLACES the 2022 "Catálogo Sistema de
Transmisión" v1.2 set — not a minor bump: CAT-002 now includes event codes
(17 Operaciones Especiales, 18 Retorno), CAT-008 is Distrito (previously
"eliminado"), CAT-013 municipios was restructured to the 44-municipio model
(codes re-assigned), CAT-023 was repurposed to Operaciones Especiales, CAT-024
renamed "Motivo del evento", CAT-033 (Tipo de Régimen) is new. The version
number went DOWN (1.2 → 1.1): trust dates, not version numbers.

Authoritative status: these CSVs are faithful copies of the official
catalog; any discrepancy against a newer MH catalog version is resolved by
regenerating from the new source (then recording the supersession — see
[regulatory-change-management.md](../../../shared/docs/regulatory-change-management.md)).

- CAT-015 carries a `section` column: the catalog groups tributos into
  summary-reflected (§1), body-reflected (§2), and informative ad-valorem
  (§3 — includes an extended list beyond what the structures manual's
  Anexo 5 documents).
- Known corrections are recorded in `_INDEX.md`.
