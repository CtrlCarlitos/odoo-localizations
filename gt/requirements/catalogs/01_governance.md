# GT — Catalogs — FEL catalog sidecars: authority, drift & dated storage

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | catalogs |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the governance requirements for the three SAT FEL JSON
catalogs as *data*: the CSV sidecars in this directory
([_INDEX.md](_INDEX.md)) as the machine-readable legal basis for *frases*
(legal legends), *unidades gravables* (taxable units and factors), and
*mensajes* (validation messages); the publication-channel authority rule
(GitHub 961133c as working authority, with every inter-channel difference
recorded verbatim in [_DRIFT.md](_DRIFT.md) and never silently resolved);
the dated-version storage policy (valid_from = catalog header date, append
never replace — D16); the Frases↔schema pairing rule (R6); the regeneration
procedure; and the corrections log.

It does **not** cover: how DTE structures *consume* catalog codes per field
(the e-invoicing requirement files, clusters E1/E3/E7), the XSD schema set
itself beyond the Frases pairing rule (E2 e-invoicing file), tax computation
rules that use the unidades factors (taxation wave), or the certificador
catalog-sync interface (E5, GOQ-39). Those files reference this one for
catalog data.

## 2. Legal Basis

FEL authority order (binding, per master evidence index): XSD/JSON working
authority = GitHub 961133c (ratified-official, OQ1 ruling 2026-08-18)
EXCEPT GT_Complemento_MediosdePago → cat.desa (R2); all drift recorded, never
silently resolved (GOQ-02 umbrella). Reglas y Validaciones is cited as
"Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025)" only.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CatalogoFrases-0.6.0, cabecera "FEL-CATALOGO-FRASES", "Ultima Actualizacion": "25/03/2025 14:30:00" (GitHub) | Frases catalog v0.6.0 (GitHub channel): 12 tipos / 88 frases with regime flags and legend texts — working authority for frases | `gt/sources/29_FEL_XSD_cat_github_961133c/CatalogoFrases-0.6.0.json` | cabecera + contenido.tiposFrases (EVID-027) |
| LB-002 | CatalogoFrases-0.1.2, "Ultima Actualizacion": "12/07/2019 08:00:00" (cat.desa) | Frases catalog v0.1.2 (cat.desa channel): 5 tipos / 25 frases — drift comparand only, never a sidecar source | `gt/sources/30_FEL_XSD_cat_catdesa/CatalogoFrases-0.1.2.json` | cabecera + contenido.tiposFrases (EVID-027) |
| LB-003 | catalogoUnidadesGravables-0.1.4, "Nombre": "FEL-CATALOGO-UNIDADES-GRAVABLES", "Ultima Actualizacion": "23/08/2022 11:00:00" (identical header both channels) | Taxable-units catalog v0.1.4: 12 impuestos × 43 unidades with factor / operaSobreCasilla / descuento | `gt/sources/29_FEL_XSD_cat_github_961133c/catalogoUnidadesGravables-0.1.4.json` + `gt/sources/30_FEL_XSD_cat_catdesa/catalogoUnidadesGravables-0.1.4.json` | Cabecera + Contenido (EVID-028) |
| LB-004 | catalogoMensajes-0.3.0, "Nombre": "FEL-CATALOGO-MENSAJES", "Ultima Actualizacion": "02/12/2024" (identical header both channels) | Messages catalog v0.3.0: 211 codes in 7 families (FEL_RCP 154, FEL_ANU 22, FEL_SEC 15, FEL_GEN 10, FEL_INF 6, FEL_AUT 3, FEL_ASO 1) | `gt/sources/29_FEL_XSD_cat_github_961133c/catalogoMensajes-0.3.0.json` + `gt/sources/30_FEL_XSD_cat_catdesa/catalogoMensajes-0.3.0.json` | Cabecera + Contenido (EVID-029) |
| LB-005 | Repositorio GitHub notificacioneselectfel/Catalogo-FEL, rama main @ 961133c2d62717fab415a8255e9aabaa4f57b9eb (2026-08-04) | GitHub repository snapshot pinned at commit 961133c — ratified-official channel (OQ1 ruling 2026-08-18) and working authority for the XSD/JSON set | `gt/sources/29_FEL_XSD_cat_github_961133c/` | repo snapshot (EVID-030; master-index FEL authority preamble) |
| LB-006 | Portal cat.desa.sat.gob.gt, /xsd/alfa + /catalogos/alfa (recuperado 2026-08-18) | cat.desa.sat.gob.gt /xsd/alfa + /catalogos/alfa directories (retrieved 2026-08-18) — second publication channel; drift comparand | `gt/sources/30_FEL_XSD_cat_catdesa/` | portal snapshot (EVID-030; master-index FEL authority preamble) |
| LB-007 | GT_Documento-0.2.1.xsd, Frases/Frase: "En esta sección deberá indicarse los regímenes y textos especiales que son requeridos en los DTE, de acuerdo a la afiliación del contribuyente y tipo de operación."; TipoFrase minInclusive 1, maxInclusive 12 (GH) / 9 (CD); CodigoEscenario 1..99; maxOccurs 100 | DTE schema Frases container: the (TipoFrase, CodigoEscenario) reference pair into CatalogoFrases, up to 100 frases per DTE | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 328–391 + CD copy (diff hunk 274c350) | Frases/Frase (EVID-007) |
| LB-008 | GT_Documento-0.2.1.xsd, Impuestos/Impuesto/CodigoUnidadGravable (xs:integer, totalDigits 7) y TipoImpuesto (12 nombres: "IVA", "PETROLEO", "TURISMO HOSPEDAJE", "TURISMO PASAJES", "TIMBRE DE PRENSA", "BOMBEROS", "TASA MUNICIPAL", "BEBIDAS ALCOHOLICAS", "TABACO", "CEMENTO", "BEBIDAS NO ALCOHOLICAS", "TARIFA PORTUARIA") | Schema join between line/totals taxes and the unidades gravables catalog (impuesto key = TipoImpuesto name; CodigoUnidadGravable = catalog unit code) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` | items Impuesto (lines 392–625) + TipoImpuesto (lines 1458–1480) (EVID-008, EVID-011) |
| LB-009 | Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025), §2.6 (matriz de frases: 12 tipos × 24 columnas DTE; tipos 1/2/3/6/7 derivados del RTU; escenarios de exención tipo 4: 1–35 con 34 ausente y 36 citada en 2.6.1.27) | Validation rulebook v2.0, §2.6 — the rule layer that consumes the Frases catalog (auto-derived tipos per emitter registry state; exemption scenarios) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.6 (EVID-130..133) |
| LB-010 | Política de gestión de cambios regulatorios (permanente), D15/D16: filas fechadas valid_from/to + procedencia; los cambios agregan filas; nunca se reemplaza en el lugar | Regulatory change-management standing policy, D15/D16: dated rule rows (valid_from/to + provenance); changes add rows; snapshot-on-write; no in-place replacement | `shared/docs/regulatory-change-management.md` | D15–D16 (master-index shared canon) |

## 3. Functional Requirements

### 3.1 Machine-readable authority & channel policy

- **GT-CAT-FR-001:** The system shall treat the three CSV sidecars as the
  machine-readable legal basis for FEL catalog data: `CAT-FRS_frases.csv`
  (88 rows, one per frase), `CAT-UGR_unidades-gravables.csv` (43 rows, one
  per unidad gravable across 12 impuestos), and `CAT-MSG_mensajes.csv`
  (211 rows, one per mensaje), with the file/row/column map in
  [_INDEX.md](_INDEX.md) authoritative. (LB-001; LB-003; LB-004; EVID-027,
  EVID-028, EVID-029)
- **GT-CAT-FR-002:** The sidecars shall be generated only by
  `gt/scripts/build_gt_catalogs.py` from the working-authority channel's
  JSON, as a verbatim flattening (empty cells = source `null`; unknown
  source shapes fail the build loudly); they shall never be hand-edited —
  every discrepancy against a newer official catalog is resolved by
  regeneration, not in-place correction. (LB-005; EVID-030)
- **GT-CAT-FR-003:** Catalog channel authority shall follow the master-index
  FEL authority order: GitHub 961133c (LB-005) governs the three JSON
  catalogs and the XSD set, EXCEPT `GT_Complemento_MediosdePago-0.1.0.xsd`
  which is modeled from cat.desa per R2 (the GitHub copy is an
  uncompilable TurismoPasaje overwrite); this per-file override concerns the
  XSD set only and does not alter the JSON sidecars. Confirmation of the
  channel question with SAT/TotalDoc is pending → OQ-004 (GOQ-02).
  (LB-005; LB-006; EVID-021 + drift matrix; R2; GOQ-02)
- **GT-CAT-FR-004:** Every inter-channel difference detected at generation
  time shall be recorded verbatim in [_DRIFT.md](_DRIFT.md) — the frases
  scope difference (GH 0.6.0: 12 tipos / 88 frases, 25/03/2025 vs CD 0.1.2:
  5 tipos / 25 frases, 12/07/2019), the catalogoMensajes FEL_RCP108/109 body
  swap, and the catalogoUnidadesGravables PETROLEO 15/16 divergence — and
  drift shall never be silently resolved: unresolved material cases carry
  their master-index GOQ id, and a new detection with no ruling produces a
  new GOQ, not a silent choice. (LB-001; LB-002; LB-003; LB-004; EVID-027,
  EVID-028, EVID-029 + drift matrix; GOQ-02 umbrella)

### 3.2 Version regime & regeneration

- **GT-CAT-FR-005:** Catalog regime identity shall be keyed by the tuple
  (channel, version string, "Ultima Actualizacion" header date) — never by
  version-number ordering: Frases 0.6.0 (GH) and 0.1.2 (CD) are channel
  forks of the same catalog name, not a sequence, and unidades/mensajes
  carry identical version+date on both channels while still differing in
  content. The sidecars carry `version` and `ultima_actualizacion` as
  columns on every row for this purpose. (LB-001; LB-002; LB-003; LB-004;
  EVID-030)
- **GT-CAT-FR-006:** Catalog data in the product shall be stored as dated
  rows (catalog, key, value, valid_from, valid_to) with valid_from = the
  catalog version date (Frases 0.6.0 → 2025-03-25; Unidades 0.1.4 →
  2022-08-23; Mensajes 0.3.0 → 2024-12-02); a new catalog regime APPENDS
  rows and closes the previous regime's rows, never replacing a row's value
  or reassigning a key's meaning in place (D16), so a catalog reference in a
  stored DTE always resolves against the regime in force at that document's
  emission date. (LB-010; LB-001; LB-003; LB-004; EVID-030)
- **GT-CAT-FR-007:** When a new catalog source version arrives in
  `gt/sources/`, the pipeline shall: (a) capture what changed, its version
  date, and whether drift rulings change BEFORE synthesis proceeds against
  it; (b) re-run `gt/scripts/build_gt_catalogs.py` (bumping the script's
  GENERATION_DATE constant) so sidecars and `_DRIFT.md` regenerate
  deterministically — a clean re-run against unchanged sources must be
  byte-identical (idempotent); (c) record the supersession in `_INDEX.md`.
  Sources already read are never modified, and the script exits non-zero on
  unreadable input. (LB-005; EVID-030)
- **GT-CAT-FR-008:** Any deviation between a sidecar and its source applied
  at build or regeneration time shall be recorded in the corrections log of
  `_INDEX.md`; a sidecar shall contain no deviation from its source that is
  not logged there. (LB-005; EVID-030)

### 3.3 Frases catalog & schema pairing

- **GT-CAT-FR-009:** The Frases pairing rule shall follow R6: the GitHub
  schema's TipoFrase domain (1..12) pairs with CatalogoFrases 0.6.0 (12
  tipos / 88 frases); the cat.desa-internal inconsistency (CD schema allows
  TipoFrase 1..9 while CD CatalogoFrases-0.1.2 defines only 5 tipos) is
  recorded as drift, not resolved. Which Frases catalog each channel's
  runtime actually loads is open → OQ-001 (GOQ-19); until answered,
  generation targets the GH pairing. (LB-001; LB-002; LB-007; EVID-007,
  EVID-027; R6)
- **GT-CAT-FR-010:** The frases sidecar shall carry, verbatim per frase:
  the (tipo_frase, codigo_escenario) pair the schema references, the regime
  selection flags (retenerISR, esAgenteRetenedor, esPequenoContribuyente,
  esRegimenElectronico, esAgropecuario, incluyeIVA), the
  contieneResolucion / contieneFechaResolucion flags that demand
  NumeroResolucion / FechaResolucion on the DTE, and the textoAColocar
  legend to print — the data consumed by the Reglas §2.6 frases matrix
  (tipos 1/2/3/6/7 auto-derived from emitter registry state; tipo-4
  exemption scenarios 1–35+36). (LB-001; LB-009; EVID-027)

### 3.4 Unidades gravables

- **GT-CAT-FR-011:** The unidades sidecar shall be the tax-engine input of
  record: each row's `opera_sobre_casilla` selects the formula
  (`MontoGravable` = ad-valorem factor, e.g. IVA 0.12;
  `CantidadUnidadesGravables` = per-unit Q/USD factor, e.g. CEMENTO Q1.50
  per 42.5-kg bag, TARIFA PORTUARIA USD 0.05), `factor` and `descuento`
  carried verbatim, and the TASA MUNICIPAL single free-text unidad (null
  code / null operaSobreCasilla / null factor) preserved exactly as
  published — no code or factor invented for it. (LB-003; LB-008; EVID-028)
- **GT-CAT-FR-012:** For PETROLEO unidades 15/16 the sidecar shall carry
  the GH (working-authority) reading — 15 "Super con etanol" (Superior con
  etanol) factor 4.7 descuento 0.1; 16 "Regular con etanol" factor 4.6
  descuento 0.1 — while `_DRIFT.md` records the cat.desa reading verbatim
  (15 "Gasolina regular con alcohol carburante (etanol)" 4.6/0.1; 16 "Gas
  con alcohol carburante (etanol) exento" 0/0) under the identical header
  date 23/08/2022; the divergence shall not be silently resolved (R4), and
  etanol-billing configuration against unidades 15/16 shall not be frozen
  until GOQ-25 is answered → OQ-002. (LB-003; EVID-028; R4; GOQ-25)

### 3.5 Mensajes

- **GT-CAT-FR-013:** The mensajes sidecar shall serve as the FEL runtime
  vocabulary (211 codes / 7 families) for connector error mapping and
  pre-validation diagnostics; the FEL_RCP108/FEL_RCP109 validacion/mensaje
  bodies are swapped between channels (both readings recorded verbatim in
  `_DRIFT.md`), production-correct numbering is pending → OQ-003 (GOQ-26),
  and the cross-check anchor holds either way: FEL_RCP108-family validation
  pins GALDIESEL → IDP unidad 4, GALSUPER → 1, GALREGULAR → 2 (plus
  unidad 14 as the exempt catch). (LB-004; EVID-029; R3; GOQ-26)

### 3.6 Serving & sync

- **GT-CAT-FR-014:** Catalog data is a shared contract: every serving or
  storage of catalog rows shall be regime-stamped with (channel, file,
  version string, "Ultima Actualizacion" date) so that any consumer — client
  or SaaS — selects the regime as-of a document date and resolves every key
  identically; stored rows are never mutated by a later regime load.
  (LB-001; LB-003; LB-004; LB-005; EVID-030)
- **GT-CAT-FR-015:** Catalog sync/refresh mechanics shall live SaaS-side:
  authoritative current-regime serving, detection of a newer published
  catalog (version/date change), regeneration-diff publication, and drift
  alerting; the Odoo client holds a local dated cache for capture UX and
  offline readability, refreshes it from the SaaS, and never rewrites
  stored rows. (LB-005; EVID-030; GOQ-39 kin for the provider interface)

## 4. Data Model

Sidecar file/column map: [_INDEX.md](_INDEX.md) (authoritative). Drift
record: [_DRIFT.md](_DRIFT.md). Storage shape (dated rows per FR-006):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.catalog.regime | channel | char | github_961133c · catdesa | FR-003, FR-005 |
| l10n_gt.catalog.regime | source_file + version_string | char | e.g. CatalogoFrases-0.6.0.json + "0.6.0" | FR-005 |
| l10n_gt.catalog.regime | ultima_actualizacion / valid_from | datetime / date | 25/03/2025 14:30:00 → 2025-03-25 · 23/08/2022 11:00:00 → 2022-08-23 · 02/12/2024 → 2024-12-02 | FR-005, FR-006 |
| l10n_gt.catalog.row (frases) | key | (int, int) | (tipo_frase 1–12, codigo_escenario 1–99) = schema (TipoFrase, CodigoEscenario) | FR-009; LB-007 |
| l10n_gt.catalog.row (frases) | flags | json | retenerISR, esAgenteRetenedor, esPequenoContribuyente, esRegimenElectronico, esAgropecuario, incluyeIVA, contieneResolucion, contieneFechaResolucion | FR-010 |
| l10n_gt.catalog.row (frases) | texto_a_colocar | text | verbatim legend | FR-010 |
| l10n_gt.catalog.row (unidades) | key | (char, int null) | (impuesto = TipoImpuesto 12 names, codigo_unidad_gravable; TASA MUNICIPAL null) | FR-011; LB-008 |
| l10n_gt.catalog.row (unidades) | opera_sobre_casilla / factor / descuento | char / decimal null / decimal null | MontoGravable · CantidadUnidadesGravables; verbatim factors | FR-011 |
| l10n_gt.catalog.row (mensajes) | key | char | codigo (FEL_RCP000…) + familia (7 families) | FR-013 |
| l10n_gt.catalog.row (all) | valid_from / valid_to | date / date null | regime window; null valid_to = current | FR-006 |
| drift record (_DRIFT.md) | catalog / key / gh_value / cd_value / goq | md table | verbatim JSON both channels + GOQ id when unresolved | FR-004 |

## 5. Odoo Mapping

Layer semantics: `shared` = catalog data and rules both sides must honor
identically (thin-client architecture D2 — the sidecars are the normative
code source for client and SaaS); `saas` = sync/refresh mechanics living in
the Elixir core. Per the brief: catalog data → `shared`; sync/refresh
mechanics → `saas`. No Odoo 17/18/19/20 version differences are required by
this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | shared | — | — | Sidecars = normative code source for both sides; _INDEX.md is the map |
| FR-002 | shared | — | — | Repo-side pipeline rule; no runtime component |
| FR-003 | shared | — | — | Channel authority stamped into regime metadata both sides serve/store |
| FR-004 | shared | — | — | _DRIFT.md consumed at build time by both sides; release gate for FR-012/FR-013 consumers |
| FR-005 | shared | — | — | Regime identity tuple; never sort/compare version strings |
| FR-006 | shared | l10n_gt.catalog.row (new) | catalog, key, value, valid_from, valid_to | Dated rows stored identically on client cache and SaaS; resolution as-of document date |
| FR-007 | shared | — | — | Ops procedure: capture delta → regenerate → supersession record |
| FR-008 | shared | — | — | Corrections log lives in _INDEX.md (human-audit layer) |
| FR-009 | shared | — | — | Pairing rule drives frase-validation config on both sides; GOQ-19 pending |
| FR-010 | shared | l10n_gt.catalog.row (frases) | flags, texto_a_colocar | Selection flags feed generation logic (E3 file consumes) |
| FR-011 | shared | account.tax (GT templates) | l10n_gt_unidad_gravable (new) | Tax grid seeded from sidecar; opera_sobre_casilla picks ad-valorem vs per-unit computation |
| FR-012 | shared | account.tax (PETROLEO 15/16) | factor, descuento | GH rows seeded; etanol billing config gated on GOQ-25 |
| FR-013 | shared | — (connector mapping table) | codigo → user guidance | Error-code mapping for connector UI; 108/109 annotation until GOQ-26 |
| FR-014 | shared | protocol envelope | regime version+date fields | Both sides resolve keys identically as-of date; stored rows immutable |
| FR-015 | saas | — | — | Sync/refresh authoritative server-side; client dated read-only cache (GOQ-39 kin) |

## 6. Acceptance Criteria

- **AC-001:** Given the current committed sources, when
  `~/.venvs/localizations/bin/python gt/scripts/build_gt_catalogs.py` is
  re-run, then all five outputs (3 CSVs, `_INDEX.md`, `_DRIFT.md`) are
  byte-identical to the committed set and the sidecar row counts match
  `_INDEX.md` (88 / 43 / 211). (FR-002, FR-007)
- **AC-002:** Given `_DRIFT.md`, when reviewed, then it contains verbatim:
  (a) the frases scope row — GH 0.6.0 / "25/03/2025 14:30:00" with 12
  tipos / 88 frases vs CD 0.1.2 / "12/07/2019 08:00:00" with 5 tipos / 25
  frases; (b) PETROLEO unidad 15 GH "Super con etanol" factor 4.7
  descuento 0.1 vs CD "Gasolina regular con alcohol carburante (etanol)"
  factor 4.6 descuento 0.1, and unidad 16 GH "Regular con etanol" 4.6/0.1
  vs CD "Gas con alcohol carburante (etanol) exento" 0/0; (c) the
  FEL_RCP108/109 validacion bodies swapped between channels. (FR-004,
  FR-012, FR-013)
- **AC-003:** Given any sidecar row, when read, then its first two columns
  carry the source version string and "Ultima Actualizacion" (0.6.0 /
  25/03/2025 14:30:00; 0.1.4 / 23/08/2022 11:00:00; 0.3.0 / 02/12/2024).
  (FR-005)
- **AC-004:** Given the TASA MUNICIPAL row in `CAT-UGR_unidades-gravables.csv`,
  when loaded, then codigo_unidad_gravable, opera_sobre_casilla and factor
  cells are empty (source nulls preserved) and no code or factor was
  invented. (FR-011)
- **AC-005:** Given a missing or corrupt source JSON (or a future frases
  row carrying an unknown flag key), when the build script runs, then it
  exits non-zero with a diagnostic and writes nothing under `gt/sources/`.
  (FR-002, FR-007)
- **AC-006:** Given a stored DTE emitted 2025-04-10 referencing frase
  (tipo 9, escenario 1), when its legend is displayed after any later
  catalog regime is loaded, then it resolves against the 0.6.0 /
  valid_from 2025-03-25 regime rows and no stored row was rewritten.
  (FR-006, FR-014)
- **AC-007:** Given a sidecar that deviates from its source in any way,
  when `_INDEX.md` is reviewed, then that deviation appears in the
  corrections log; otherwise the build introduced no unlogged deviation.
  (FR-008)
- **AC-008:** Given the Odoo Mapping table, when checked, then every FR row
  carries a Layer value, catalog-data FRs are `shared`, and sync/refresh
  mechanics are `saas`. (FR-014, FR-015)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text copied verbatim from the register.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-19: Which Frases catalog does each channel's runtime load (CD schema allows 1-9; CD catalog has 5 tipos; GH aligns 12/12)? (Origins: EV01a OQ-5; blocks E2/E3 synthesis frases behavior, not this file's sidecars.) | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-002 | GOQ-25: unidadesGravables PETROLEO 15/16 = different products/factors per channel under identical header date — which authoritative for etanol billing? (Blocks etanol tax config, FR-012; drift recorded, not resolved.) | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-003 | GOQ-26: catalogoMensajes FEL_RCP108/109 bodies swapped between channels — which numbering is production-correct? (Blocks connector 108/109 error mapping, FR-013; both readings recorded.) | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-004 | GOQ-02: (=OQ3 umbrella) Which channel/version does production validation key on (GitHub 961133c vs cat.desa; per-file drift set)? Ask TotalDoc/SAT (W6 partner ask). Working rule: GitHub EXCEPT MediosdePago. (Umbrella for FR-003/FR-004; blocks all e-invoicing FRs at the authority level.) | no | GT synthesis wave S-GT1 → W6 partner ask | open |
