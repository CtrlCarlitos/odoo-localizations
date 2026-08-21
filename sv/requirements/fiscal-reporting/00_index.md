# SV — Fiscal reporting (F-07/F-14/informs/calendar) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft (S3 wave + W17 fold-in, in review) |
| Authors | Takumi synthesis wave 3 + controller |
| Updated | 2026-08-20 (W17) |

This directory holds the S3 (synthesis wave 3) fiscal-reporting
requirements: the F-07 monthly IVA declaration casilla engine and its
annex upload family (sales 1-2, purchases 3/5, retentions/perceptions
4/6-12, special dated-regime annexes 13-17, anulados/emitidos), the F-14
monthly ISR retention declaration with the Quincena-25 v17 vintage, the
F-14 income-code catalog and the F-910/F-915/F-930/F-935 informs, and the
filing calendar / due-day / *días hábiles* engine — with the income-code
catalog as verbatim dated data in one CSV sidecar. The W17 fold-in
(2026-08-20) added the 75_ CT-reglamento declaration-state gate and
reception contract to 01, LB notes to 06/07/08 (SOQ-08 anchor consumed).
Source-to-requirements coverage: [../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_f07-declaration.md](01_f07-declaration.md) | F-07 v14 declaration casilla engine (77-row graph, USD-only, Art. 74-A flag, verbatim SUMA arithmetic, remanente/impuesto split, retention credits on/by the declarant, D.L. 764-2014 control-de-liquidez + FOVIAL credits, multas → TOTAL A PAGAR) + the generic annex upload engine (semicolon-CSV format, §XVI validation set, response handling, modificatoria carryover/re-upload) + the 75_ declaration-state classification gate & delegated-reception contract (FR-213: original/complementaria-correctiva/late-firm states per Arts. 31/33-34, CT 103 co-anchor; FR-214: receiver reviews-but-never-modifies per Art. 32/35) | SV-FREP-FR-001..041, 213..214 | 43 | 13 | 20 | 5 |
| [02_f07-annexes-sales.md](02_f07-annexes-sales.md) | Anexo 1 Ventas a Contribuyentes (per-document B2B rows, CCF/NC/ND, DUI-vs-NIT gate, Enero-2025 R/S renta pair feeding the F-14/F-910/F-11 family, canonical DTE identifier mapping) + Anexo 2 Ventas a Consumidor Final (aggregated B2C rows, DEL/AL pre-printed ranges, DTE day-groups with primer/último código, IVA-inclusive gravadas, export buckets) | SV-FREP-FR-042..066 | 25 | 8 | 14 | 6 |
| [03_f07-annexes-purchases.md](03_f07-annexes-purchases.md) | Anexo 3 Compras (IVA base buckets × compras internas/internaciones/importaciones, crédito fiscal N, ND+/NC− totals, Tesorería pseudo-NIT, Febrero-2024 ISR quartet Q/R/S/T) + Anexo 5 sujetos excluidos (twin quartet I-L) + the post-entero casilla-128 credit re-entry | SV-FREP-FR-067..094 | 28 | 9 | 11 | 7 |
| [04_f07-annexes-retentions-events.md](04_f07-annexes-retentions-events.md) | Anexo 4 ventas por cuenta de terceros (→ casilla 108), Anexos 6-8 retentions effected on the declarant (→ 161-163), Anexos 9-12 retentions by the declarant, §XIX anulados/emitidos annex (SOQ-10 defect ruling in LB-007; FR-118), F-930 v3 monthly retIVA informe | SV-FREP-FR-095..123 | 29 | 10 | 12 | 7 |
| [05_f07-annexes-special.md](05_f07-annexes-special.md) | The five dated-regime annexes: 13 fuel tasas diferenciadas (Decreto 321, manual-entry only, → 586-589), 14 price-cap credit notes (→ 550-553), 15/16 Decreto 357 informativo pair (→ 92/65), 17 fuel-importers closed window; the regime-validity gate engine (closed windows never re-activate) | SV-FREP-FR-124..136 | 13 | 6 | 10 | 5 |
| [06_f14-declaration.md](06_f14-declaration.md) | F-14 v16/v17 ISR retention declaration: A-W annex row model (identification, payroll devengado/bonificaciones/aguinaldo split, seven SS columns with SOQ-11 caps as dated data), export validation contract, declaration-as-pure-projection invariant, seven-tab form architecture (Pago a Cuenta with dead pago-mínimo row, Op. Financieras 501-529, No Domiciliados matrix, Agentes Extranjeros 701-780), modificatoria flow, v17 Quincena-25 casillas 417/418 (FR-166 reporting-only isolation; FR-167 amended — retention annex exports without Quincena rows) + the January-only Quincena annex upload engine (FR-209..211: 7-column `;`-delimited CSV per 69_/70_, January-window gate, 417/418 + code-73 derivation at presentation); 75_ Art. 100 detalle-anexo note (LB-013, W17 — the paper ancestor of the retention annex, MOQ-10 kin) | SV-FREP-FR-137..170, 209..211 | 37 | 13 | 17 | 9 |
| [07_codes-and-informs.md](07_codes-and-informs.md) | F-14 income-code catalog — 49 codes (48 + the 2026 Quincena-25 code 73 "Ingresos No Gravados Pagados Quincena Veinticinco", FR-212: F-910 NO GRAVADOS auto-population fed by the FR-211 upload; CSV row dated 2026-01 f17_kin) × 4 classes as dated data with row/casilla mapping and CT anchors (distributions 43-46, haven 40, CT 123 aggregate 47; CSV sidecar `f14_income_codes.csv`), the F-07 R/S ↔ F-14 ↔ F-11 coupling, F-910 v9 annual consolidation (CT 123 surface), F-915 v4 distributions inform, F-935 v1 foreign-agents inform; F-930 referenced only (homed in 04); 75_ dictamen block as HISTORICAL LB (LB-011, W17: Arts. 58-72 appointment clocks + 31-may dictamen+informe deadline + the a)-n) anexo set — OQ-009/EV75 OQ-3 vintage watch, never operative FRs) | SV-FREP-FR-171..194, 212 | 25 | 11 | 10 | 9 |
| [08_filing-calendar.md](08_filing-calendar.md) | Calendario Tributario 2026 obligation inventory as dated data (monthly/annual/registry rows, incl. F-950), due-day window mechanism as unpinned configuration (SOQ-08), asueto table 2026, the shared días hábiles engine (consumed by e-invoicing/taxation deadlines by FR id), per-company deadline/reminder model; 75_ Art. 100 co-cite (LB-006, W17 — SOQ-08 statutory 10-hábiles entero anchor consumed; by-NIT-digit windows remain dated config, OQ-001 updated) | SV-FREP-FR-195..208 | 14 | 6 | 6 | 4 |
| **Total** | | SV-FREP-FR-001..214 | **214** | **76** | **100** | **52** |

Numbering note: FR numbering is wave-sequential within the `SV-FREP`
prefix (001-214, no gaps, no renumbering; 209-212 appended by the S6
Quincena-25 fold-in, 2026-08-18; 213-214 appended by the W17
CT-reglamento fold-in, 2026-08-20). The CSV
`f14_income_codes.csv` (48 code rows + header + the 2026 Quincena-25
row 73) is a dated-data sidecar of
`07_codes-and-informs.md`; it carries no FRs of its own.

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 52 OQs total —
50 open / 2 resolved (`06` OQ-001 = SOQ-09, resolved W11 + folded S6
as FR-209..211; `06` OQ-009 = `;`-delimiter resolution, resolved
in-file + live-portal verification rider; SOQ-10 is the only ruled S3 question and it is recorded as
an LB note — `04` LB-007 — not an OQ; `07` OQ-009 = W17 dictamen vintage
watch, open).

Master-index SOQ mapping: SOQ-08 = `08` OQ-001 (which owns the `06`
OQ-005 pointer — due-day windows; **W17 update: the statutory 10-hábiles
layer is now anchored by 75_ Art. 100 (LB-006, EVID-351) — only the
by-NIT-digit window assignment remains open**); SOQ-09 = `06` OQ-001 — **resolved
in-corpus (W11 + S6 fold-in, 2026-08-18): FR-209..212 own the
Quincena-25 reporting** (7-column `;` CSV per 69_/70_, January-only
upload, code 73); the v17-manual absence remains as a
doc-completeness residue (`07` OQ-008); SOQ-10 = `04` LB-007 (ruling applied and
recorded, kin FR-118); SOQ-11 = `06` OQ-002 (SS caps as dated data);
SOQ-12 = `01` OQ-001 (kin: `06` OQ-004 + `07` OQ-001); SOQ-13 = `07`
OQ-003 (F-935 donantes-locales anchor); SOQ-14 = `08` OQ-002 (F-950
frequency/applicability).

### 01_f07-declaration.md (5)

- OQ-001 — SOQ-12 carried: DGII annex-modification resolutions not in the corpus; manual (34_) + form (39_) are the only authority. open
- OQ-002 — Manual §II heading "CSV (delimitado por comas)" vs the operative semicolon list separator; semicolon encoded (FR-028). open
- OQ-003 — Casilla 525 FOVIAL credit: no printed formula/source; computation stays with the special-regimes/taxation waves. open
- OQ-004 — IVA retention rates (1%/2%/13%) anchored as form labels only; index task wires cross-references when the IVA taxation file lands. open
- OQ-005 — Casillas 146/151 negative-balance carriers printed on the form but in no formula — recorded-unwired. open

### 02_f07-annexes-sales.md (6)

- OQ-001 — Anexo 2 DTE day-group row ordering unstated (EV34 OQ-3 carried). open
- OQ-002 — Anexo 1 inferences: L net-of-IVA convention + P = J+K+L+N total addition label-inferred. open
- OQ-003 — R/S lengths: column table's "10" vs text "máximo dos caracteres" — manual typo, 2 encoded. open
- OQ-004 — Anexo 2 U/V code lists not printed; same-lists-as-R/S assumption. open
- OQ-005 — Terceros wiring N/O → 88/141 and S → 89 label-matched. open
- OQ-006 — Anexo 2 H/I primer/último código per-column assignment on day-group rows. open

### 03_f07-annexes-purchases.md (7)

- OQ-001 — Anexo 3 D-column DTE fill: single NÚMERO slot by label match. open
- OQ-002 — Q/R/S/T pre-gate fill ("0") and lengths unprinted — parity encoding. open
- OQ-003 — Anexo 5 I-L code lists: same-lists assumption (twin of 02's OQ-004). open
- OQ-004 — Anexo 5 H 13%-retention applicability — future IVA taxation file matter. open
- OQ-005 — Post-entero credit re-entry: own vs following period (own encoded). open
- OQ-006 — Wiring label-inferences: H/I → 70; N split → 125/126/127/130; tipo-12/13 channels; O unwired. open
- OQ-007 — Code-8 all-four-columns fill by parity with code 9 (§V prints the all-four rule for 9 only). open

### 04_f07-annexes-retentions-events.md (7)

- OQ-001 — F-930 codificación values not in corpus; code lists to seed. open
- OQ-002 — Anexo 4 amounts: casilla-108 basis H-only; H/I split on CCF/NC/ND rows. open
- OQ-003 — §XIX printed-model gaps: no trailing annex-number/date column. open
- OQ-004 — §XIX anulados/emitidos modificatoria carryover fate unprinted. open
- OQ-005 — Annexes 6-12 column letters/lengths by printed position + family conventions. open
- OQ-006 — F-930 v3 vintage: 2017 print still listed by MH 2026-08-18. open
- OQ-007 — F-930 §B class↔tipo mapping label-matched (7 classes ↔ annex tipos). open

### 05_f07-annexes-special.md (5)

- OQ-001 — Decreto 321 regime status + differentiated rate values not in corpus. open
- OQ-002 — Auto-complement bases: which columns total 550-553; anexos 15/16 vs casillas 92/65. open
- OQ-003 — FOVIAL/COTRANS interplay (casilla 525): pointer only — taxation/special-regimes waves own the design. open
- OQ-004 — Annexes 13-17 modificatoria carryover unprinted. open
- OQ-005 — "Fin de la obra" window-end semantics (per-project vs decree-level). open

### 06_f14-declaration.md (9)

- OQ-001 — SOQ-09: F-14 v17 annex format — **RESOLVED 2026-08-18 (W11, sources 66_-70_)**: 7-column semicolon CSV (APELLIDOS 100 uppercase; NIT 14 XOR DUI 9; dd/mm/aaaa; SALARIO 4+2; QUINCENA 3+2; mmaaaa), January-only upload via F-14 v17, independent of retention annex, code 73 auto-assigned at presentation (EVID-238/239). Folded S6 (2026-08-18) as FR-209..211 (this file) + FR-212 (`07`). resolved (folded S6)
- OQ-002 — SOQ-11: SS caps as dated data; feed/cadence owned by the payroll wave. open (S4: the cap VALUES are owned by `../payroll/05_social-security-contributions.md` + its `ss_contributions.csv` sidecar)
- OQ-003 — Op. Financieras tracks 501-529: CT 159/164-165 anchor + rates re-check. open
- OQ-004 — Income-code catalog fidelity pointer (owned by 07's OQ-001). open
- OQ-005 — SOQ-08 pointer: F-14 due-day scheduling owned by `08_filing-calendar.md`. open
- OQ-006 — F-14 export file mechanics untranscribed in 35_; F-07 §II conventions by parity. open
- OQ-007 — MH country-code + tax-haven list refresh cadence (web-published, undated). open
- OQ-008 — MH-side validation depth: whether the live portal rejects rows with F ≠ 0.5×E or E > US$1,500.00 — 69_ §H reads structure-and-montos-only, so FR-211 ships the payroll-side cross-check as WARNING-only. open
- OQ-009 — Live-portal delimiter verification (69_ OQ-2 kin): the semicolon is operative (70_ header + 69_ §3 — LB-012); AC-015 assumes `;`. resolved (in-file: `;` — live-portal verification if ever possible)

### 07_codes-and-informs.md (9)

- OQ-001 — Income-code catalog fidelity (owns 06's OQ-004; SOQ-12 kin): v16 apéndice vs v17 rows + resolutions. open
- OQ-002 — Per-code row/casilla assignment granularity: zone-level only in the corpus. open
- OQ-003 — SOQ-13 (owns the anchor): F-935 "donantes locales" entero track's governing article. open
- OQ-004 — Inform vintage re-check cadence: F-910 v9 / F-915 v4 / F-930 v3 / F-935 v1; F-910 upload format not in corpus. open
- OQ-005 — "(Según ley)" anchors (codes 70-72) + unpinned matrix-zone codes. open
- OQ-006 — F-11 rentas matrix acquisition (coupling counterpart). open
- OQ-007 — Index-task wiring row: answers to taxation/04 OQ-007 (F-910), taxation/05 OQ-006 and the partial answer to taxation/05 OQ-002 (F-915) recorded in `07_codes-and-informs.md` §3.3/§3.4. open
- OQ-008 — Code 73 in the F-14 apéndice v17 unverified (no v17 manual exists — SOQ-09 doc-completeness residue): the catalog carries 73 as a dated 2026-01 f17_kin row on MH-package authority (67_ §3.f + 68_ p.16); re-check at the v17-manual / F-910-v10 acquisition (≥71 watch). open
- OQ-009 — Dictamen regime vintage watch (EV75 OQ-3; W17 fold-in LB-011): the 75_ Arts. 58-72 mandatory fiscal-audit regime was restructured at the CT level post-2001 — carried as HISTORICAL blueprint only; pin the current CT text before any operative dictamen encoding. open

### 08_filing-calendar.md (4)

- OQ-001 — SOQ-08 (owns 06's OQ-005 pointer): due-day windows unpinned — visual layer only; **W17 (2026-08-20): the statutory 10-días-hábiles entero layer is now anchored by 75_ Art. 100 (LB-006, EVID-351 — monthly consolidation of sub-monthly pay cycles), corroborated by taxation/01 LB-027; the by-NIT-digit window assignment remains unpinned dated config**. open
- OQ-002 — SOQ-14: F-950 frequency (Ene/Abr/Jul? +Agosto) and applicability. open
- OQ-003 — Asueto exact-date pinning + the fixed-day next-día-hábil shift anchor. open
- OQ-004 — Calendar provenance for years ≠ 2026 (30_ covers 2026 only). open
