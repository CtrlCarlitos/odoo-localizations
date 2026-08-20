# Scripts — Guatemala

Country-specific parsing and extraction for Guatemalan source documents.
Format-generic helpers live in [shared/scripts](../../shared/scripts/) —
reuse them instead of duplicating here.

| Script | Purpose | Usage |
|--------|---------|-------|
| `build_gt_catalogs.py` | Build the FEL catalog sidecars (frases, unidades gravables, mensajes) from both channels' JSON in `gt/sources/29_`+`30_`; emits CSVs + `_INDEX.md` + `_DRIFT.md` into `gt/requirements/catalogs/`. Deterministic; sources never modified. | `~/.venvs/localizations/bin/python gt/scripts/build_gt_catalogs.py` |
