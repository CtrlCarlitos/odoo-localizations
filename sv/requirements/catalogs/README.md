# Requirements — MH Catalogs (El Salvador)

Machine-readable sidecars of the 31 official MH catalogs used across DTE
structures and events. Generated from
[sources/25_Catalogos_Transmision_v1.2.xlsx](../../sources/) (PDF overlay
where the workbook is incomplete) by
[shared/scripts/build_catalogs.py](../../../shared/scripts/). See
`_INDEX.md` for the file/row map and applied corrections.

Authoritative status: these CSVs are faithful copies of the official
catalog; any discrepancy against a newer MH catalog version is resolved by
regenerating from the new source.

- CAT-008 was eliminated by MH and is deliberately not emitted.
- CAT-015 carries a `section` column: the catalog groups tributos into
  summary-reflected (§1), body-reflected (§2), and informative ad-valorem
  (§3 — includes an extended list beyond what the structures manual's
  Anexo 5 documents).
- Known corrections are recorded in `_INDEX.md` (e.g. CAT-032 code 2
  missing from the workbook, restored from the PDF).
