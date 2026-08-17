# El Salvador — Requirements Extraction Plan

Execution plan per [shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md).
Started 2026-08-16. Status: active.

## Context

- 54 sources registered in [sources/README.md](sources/README.md).
- Hint layer: [tuky-workspace prior project](https://github.com/CtrlCarlitos/tuky-workspace/tree/main/projects/odoo-localization-el-salvador) — 264 AI-generated requirements + design docs. Pointers only; every requirement re-derived from source.
- NotebookLM validator: notebook `c7ca0391-4822-4d3c-8090-b0d8c147ba94` (owner c20260202@gmail.com), partial corpus. Post-synthesis gap probing only, per the usage policy.

## Source inventory and decomposition

| # | Source | Governs | Reading units | Target topics |
|---|--------|---------|---------------|---------------|
| 1 | `20/25_Catalogos_Transmision*` | 32 MH catalogs (types, IDs, codes) | whole, catalog-by-catalog | catalogs (shared), feeds all |
| 2 | `40_manual_estructuras_catalogo.md` | DTE structures, field formats | structure-by-structure | e-invoicing, catalogs |
| 3 | `01_Ley_IVA.pdf` | IVA 13%, débito/crédito, pro-rata | Art. 1–125: tax core → taxation; Art. 54–75 operations → taxation; exemptions → taxation | taxation |
| 4 | `02_Reglamento_IVA.pdf` | IVA regulation | whole (repeal-aware vs Código Tributario) | taxation |
| 5 | `05_Codigo_Tributario.pdf` | Tax procedures, taxpayer registry, document authorization, books, penalties | registry/documents → e-invoicing; books/declarations → fiscal-reporting; penalties → taxation | all |
| 6 | `06_Guia_Facturacion_Electronica.pdf` | DTE system overview | whole | e-invoicing |
| 7 | `18_Normativa_Cumplimiento_DTE.pdf` | DTE compliance normative | whole | e-invoicing |
| 8 | `19_Manual_Funcional_Transmision.pdf` | Transmission functional flow | whole | e-invoicing |
| 9 | `22_Manual_Tecnologico_Transmision.pdf` | Auth, endpoints, payloads | whole | e-invoicing |
| 10 | `26_Manual_Consola_Administrativa.pdf` | MH admin console | whole | e-invoicing |
| 11 | `27_Manual_Obtencion_Certificado.pdf` | Certificate obtainment | whole | e-invoicing |
| 12 | `41_manual_eventos_invalidacion.md` | Invalidation events | whole | e-invoicing |
| 13 | `schemas/*.json` (13) | DTE JSON structures | schema-by-schema | e-invoicing, catalogs |
| 14 | `03_Ley_ISR.pdf` + `04_Reglamento_ISR.pdf` | ISR rates, brackets, withholding | core → taxation; retention tables → taxation | taxation |
| 15 | `10_Tablas_Retencion_ISR.pdf` | Payroll withholding tables | tables as data | taxation, payroll |
| 16 | `07_Codigo_Comercio.pdf` | Commercial registry, accounting books, retention | books → chart-of-accounts, fiscal-reporting; registry → commercial-legal | commercial-legal, chart-of-accounts |
| 17 | `15/17_Lavado_Activos.pdf` | AML obligations | thresholds/KYC → commercial-legal | commercial-legal |
| 18 | `08_Ley_ISSS.pdf`, `09_Ley_Sistema_Pensiones.pdf`, `11_Codigo_Trabajo.pdf`, `16_Salarios_Minimos_2025.pdf` | Social security, pensions, labor law, minimum wage | contributions → payroll; contracts/leave/overtime → payroll | payroll |
| 19 | `29/34/35/36/37/38/39_F07/F14*` | F-07/F-14 forms, annexes, templates | annex-by-annex | fiscal-reporting |
| 20 | `30_Calendario_Tributario_2026.pdf` | Filing calendar | as data | fiscal-reporting |
| 21 | `12_Ley_Zonas_Francas.pdf`, `13_Ley_Organica_Aduanas.pdf`, `14/17b_Servicios_Internacionales.pdf`, `43_DUCA_Instructivo_COMIECO.pdf`, `42_Comunicado_Exportaciones_Panama.docx` | Free zones, customs, international services, DUCA | each law whole | special-regimes |
| 22 | `31_Guia_FOVIAL_COTRANS.pdf` | Fuel contributions | whole | taxation (quantity-based — flag for Odoo Mapping) |
| 23 | `32/33_NIIF*.pdf` | NIIF PYMES, sustainability | accounting treatment → chart-of-accounts | chart-of-accounts |

## Reading order

Dependency-aware; each batch's outputs feed the next.

1. **Foundations**: catalogs (1, 2) + schemas (13) — vocabulary everything cites
2. **IVA core**: Ley IVA (3) → Reglamento IVA (4) — gravada/exenta/no-sujeta, débito/crédito, pro-rata. Everything depends on operation types
3. **Código Tributario** (5) — procedures, documents, books; repeal authority for (4)
4. **DTE stack** (6–12) — transmission, invalidation, contingency, certificates
5. **ISR** (14, 15) — rates, withholding
6. **F-07/F-14** (19, 20) — needs DTE fields + ISR/IVA concepts in place
7. **Payroll** (18) — independent track, can run parallel after (1)
8. **Commercial/legal** (16, 17)
9. **Special regimes** (21) — needs IVA + DTE context
10. **FOVIAL/COTRANS** (22), **NIIF** (23) — closers

## Topic map (source unit → topic)

| Topic | From |
|-------|------|
| `catalogs/` | units 1, 2, 13 (sidecars CSV) |
| `taxation/` | 3, 4, 5(partial), 14, 15, 22 |
| `e-invoicing/` | 5(partial), 6–12, 13(partial) |
| `fiscal-reporting/` | 5(partial), 16(partial), 19, 20 |
| `payroll/` | 15(partial), 18 |
| `commercial-legal/` | 16(partial), 17 |
| `special-regimes/` | 21 |
| `chart-of-accounts/` | 16(partial), 23 |

## Known risks

- **Repeals**: IVA/ISR Reglamento procedural articles repealed by Código Tributario (hint layer flagged many; confirm per article during merge).
- **Wrong-document incident**: file `14_` was previously an unconstitutional version; current file is Decreto 431 (2007) + Reglamento 131 (`17b_`). Verified at import.
- **Scanned PDFs (extraction check 2026-08-16)**: `18_Normativa_Cumplimiento_DTE` (16 chars/page), `26_Manual_Consola_Administrativa` (33), `35_F14_v16_manual` (27), `43_DUCA_Instructivo_COMIECO` (15) — OCR now wired (`--ocr`); DUCA verified readable (2018 chars/page). Remaining three pending OCR run.
- **Damaged PDF (2026-08-16 resolved)**: `17_Reglamento_Lavado_Activos` has a broken xref + malformed stream (object 16) — renders in lenient viewers (pdf.js) but fails strict parsers. Not corrupt content-wise. `extract_text.py` now auto-repairs via qpdf into a temp copy (sources untouched); extracts cleanly (6 pp, 3.3k chars/page). No re-download needed.
- **Unsupported formats**: `36/37_*.xls` (F-07/F-14 templates), `42_*.docx` (Panama comunicado) — add converter or manual transcription when read.
- **FOVIAL/COTRANS**: quantity-based taxes ($/gallon) — no native Odoo tax; Odoo Mapping needs explicit design decision. Confirmed mechanics in 40_manual Anexo 5 (EVID-007).
- **Catalog version drift**: catalogs v1.2 (03/2022) predates SV's 2023 municipal reorganization (262 municipios → 44); CAT-013 lists only 45 entries. Check MH for v1.3+ before synthesis; DTE references may require current municipio codes.
- **Sello/estado dual management**: MH state vs Odoo state — likely cross-topic FR cluster; assign home in synthesis.
- **OUTDATED CT COPY (RESOLVED 2026-08-16)**: `44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` added — D.L. 487-2022 adds Arts. 119-A..119-H + 239-A (the DTE legal base). Evidence pass pending (W5.5).
- **Catalog v1.2 → v1.3+ drift (RESOLVED — and bigger than expected)**: MH re-versioned catalogs entirely: `50_/51_` = Catálogos Facturación Electrónica **v1.1** (05/2026, rev 07/2026) REPLACING the Sistema de Transmisión catalogs; CAT-023 sustituido (Operaciones Especiales), new CAT-038+, CAT-013 municipio changes. Also `52_` JSON schemas (2026-08-11): CCF v4, FEX v3, F/CD/CL/CR/DCL/FSE v2, NC/ND/NR v4, contingencia v4 + **NEW event types: Operaciones Especiales (fe-eop-v1), Retorno (fe-eret-v1)**. Sidecars must be regenerated from 51_; W5 evidence (authority order, NCE-contingency, item caps, FEXE fields) must be re-validated against the 2026 set.

## Extraction log

- 2026-08-16 — Stage 1 check: 36/41 PDFs extract clean; 4 scanned (see risks), 1 corrupt (17_). Catalogs batch (20_, 25_ PDF+XLSX, 40_) extracted to scratch. **Pilot evidence pass done**: `40_manual_estructuras_catalogo.evidence.md` (15 EVID entries; §V per-DTE structures still unread — next unit). Evidence format validated: Loc + verbatim + gloss + candidate CR + topics + xref + doubts; OQs collected at file end.
- 2026-08-16 (W1 complete) — **40_ manual FULLY READ**: all 11 §V structures; evidence file now 35 EVID entries. Key per-doc findings: FE=IVA-inclusive prices vs CCFE=net+IVA (schema arbitrates); receptor thresholds ($200 FE name; $11,428.57 responsible parties on CCFE/NRE/NCE/NDE/CLE/CRE); NC adjusts CCF/CR, ND adjusts CCF/NC/ND/CR; CLE liquidates docs net-of-IVA with negative re-entry of annulled; DCLE=2% card perception; FEXE foreign receptor + C3 0% mandatory + seguro/flete + INCOTERMS; FSEE simplified + retentions; CDE mandatory qualification resolution, async seal 24-72h. **41_ events manual FULLY READ** (10 EVID entries, 036-045): invalidation deadlines confirmed (1 day / 3 months); 24h/24h/72h contingency clocks; 5s timeout trigger; 3 open questions (retry-policy doc missing, contingency type list 6-vs-7, motivo length).
- 2026-08-16 (W2 complete) — **Catalogs sidecars generated**: 31 CSVs in `requirements/catalogs/` via new `shared/scripts/build_catalogs.py` (XLSX primary, PDF overlay). Resolved OQ: contingency types = 7 (FSE included, CAT-023). Found: CAT-032 workbook missing code 2 (restored from PDF); CAT-015 extended informative list (~30 product-category codes beyond manual); **NEW RISK: CAT-013 municipios v1.2 (03/2022) may predate SV's 2023 municipal reorganization (262→44) — check MH for catalogs v1.3+.** Evidence: EVID-046 in 25_XLSX evidence file. Next: W3 IVA core (Ley IVA → Reglamento).
- 2026-08-16 (W3 complete) — **Ley IVA + Reglamento FULLY READ** (EVID-047..058 in `01_Ley_IVA.evidence.md`). Key: 13% rate (Art. 54); **CCFE net-price arbitration RESOLVED via Art. 57** (IVA separate from price in CCF; FE inclusive stands; manual wording defect noted). Art. 65/65-A deductibility matrix (indispensable-only, 58-min-wage cash rule, 50% vehicles); Art. 66 pro-rata with monthly + annual true-up; Art. 62/63 adjustment windows (3-month returns, medicines 2y w/ lot registry; 3-period late-doc rule); Arts. 74-77 exports 0% + refund capped 13% of export value; Art. 28-32 excluidos regime (FSEE = no IVA recargo). Massive repeals → procedures/sanctions/documents now in Código Tributario (W4 must collect CT Arts. ~110-142 + 161-162 refs). New OQs: colones thresholds status; FOVIAL/COTRANS base interaction (only guide 31_ in sources). Next: W4 Código Tributario (187pp — biggest read).
- 2026-08-16 (W5 complete) — **DTE stack read** (EVID-069..082 in `18_Normativa_DTE_W5.evidence.md`). **Authority order: 18_ Normativa v1.2 (17-NOV-2025) > 19_ Funcional v1.2 (10-OCT-2025) > 40_/41_/22_/25_ (2022).** Major finds: (1) **CT Arts. 119-A..119-H + 239-A missing from our CT copy** — updated CT/reform decree is a REQUIRED source (blocking OQ); (2) invalidation taxonomy REDEFINED by Cuadro 2 (all-docs errors 1d / rescission 1d / FE-FEX adjustments 3mo — supersedes CAT-024 semantics); (3) rejected docs: 24h same-code fix then new-code; (4) **tiquetes banned for DTE emitters since 01-Jan-2025**; physical docs must be destroyed on DTE adoption; (5) FEXE new Sección 7 fields 72-73 (Nov-2025); item caps 2000/500; (6) full API surface from 22_ (auth 24h/48h token, recepciondte/lote, consultas, eventos, QR URL, 8s/2-retry — 41_'s 5s superseded); (7) NCE-contingency contradiction (Cuadro 1 vs Anexo IV vs CAT-023) — default prohibited; (8) holgura computed from ITEM decimals. Evidence total: 82 entries.
- 2026-08-16 (source refresh complete) — **Files 44-52 added from factura.gob.sv** (registry updated, supersession noted): D.L. 487-2022 CT reform (RESOLVES CT gap), **Normativa v2.0 (25-May-2026, 137pp)**, **Manual Tecnológico v2.0**, Manual Funcional 2026-05, official PDFs of 40_/41_ (v1.6/v1.1), **catalogs v1.1 2026 re-versioning** (CAT-023 sustituido → Operaciones Especiales; CAT-038+; CAT-013 changes; PDF+XLSX), **JSON schemas 2026-08-11** (version bumps + NEW event types fe-eop Operaciones Especiales, fe-eret Retorno). OCR banked for 44/45/46. **Consequence: W5.5 required** — re-read 45_ (v2.0 deltas vs v1.2), 46_ v2.0 deltas, regenerate catalog sidecars from 51_, re-validate W5 evidence (esp. NCE-contingency, CAT-024 taxonomy, new event types) before S1 synthesis.
- 2026-08-16 (W5.5 complete) — **2026 regulatory update READ** (EVID-083..087 in `44-52_RegulatoryUpdate2026.evidence.md` + supersession map): D.L. 487 in full (119-A..119-H, 239-A sanctions 50/30/100%/9-SMM, CT 141/147/173/179-181/199/206 reforms, **FE receptor threshold now ≥3 SMM — supersedes $200**; NC/ND as post-window adjustment path; DTEs exempt from 115-A correlative authorization). Normativa v2.0: **FOUR events** (Invalidación, Contingencia, **Retorno** (3-month window, no receptor crédito, not invalidating), **Operaciones Especiales** (FVS monthly reporting — FVS ALIVE as physical regime + EOP; resolves simplificada OQ)); transmission-ordering rule (affected before affecting). Manual Tecnológico v2.0: same API surface, token validity configurable (24h guidance). **Catalogs v1.1: sidecars REGENERATED (33 CSVs)** — CAT-002 absorbs event codes 17/18; CAT-008 = Distrito (un-deleted); CAT-013 = 44-municipio model (RESOLVES drift risk); CAT-023 = Operaciones Especiales; CAT-024 = "Motivo del evento"; CAT-033 Tipo de Régimen new. Schemas 2026-08-11: full version matrix (CCF v4, FEX v3...). Open OQs: Retorno/EOP endpoints (not in 46_ v2.0 read), 45_ Anexos II-IV full read pending (S1 prep), FVS Odoo flow decision. **E-invoicing evidence base COMPLETE — S1 synthesis ready** (pending 45_ Anexos read as part of S1 prep).
- 2026-08-16 (architecture pivot) — Plan updated for the **SaaS thin-client product direction** (see `shared/docs/saas-thin-client-architecture.md`): open-source Odoo thin client + paid Elixir/Phoenix SaaS core. **S0.5 (architecture-split socratic session) inserted BEFORE S1** — the Layer split (odoo/saas/shared) must be decided before Odoo Mapping sections are written; template now carries a Layer column; S1 must also produce the client↔SaaS API-contract FRs. S1 order: S0.5 session → 45_ Anexos II-IV read → merge pass → Takumi files.

## Deliverables

1. `requirements/COVERAGE.md` — generated, kept current per synthesis wave
2. Topic files per the Takumi template; FR IDs `SV-<TOPIC>-FR-<nnn>`
3. `requirements/catalogs/` with machine-readable sidecars from catalogs XLSX/structures

## Session protocol

Massive task; executed in waves over multiple sessions. Each session:
extract text for the batch → evidence pass → merge → synthesize → update this
plan and the coverage matrix → commit. Never leave a session with evidence
unmerged; scratch dies with context.
