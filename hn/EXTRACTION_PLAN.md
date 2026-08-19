# Honduras — Requirements Extraction Plan

Execution plan per [shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md).
Started 2026-08-19 (source-research pass complete). Status: active.

## Context

- 85 sources registered (01-86, gap 85) in [sources/README.md](sources/README.md);
  every file page-1 verified. Research dossier: [RESEARCH.md](RESEARCH.md).
- No prior-project hint layer exists for HN (unlike SV's tuky-workspace import).
- NotebookLM validator: none yet (corpus young; revisit at first synthesis).
- Fiscal year = calendar year. Currency: lempira (HNL, L).

## Source inventory and decomposition

| # | Source | Governs | Reading units | Target topics |
|---|--------|---------|---------------|---------------|
| 1 | `01_Ley_ISR` (D.L. 25 cons. SAR-07-2025, 50 pp) | ISR: rentas, deducciones, tasas 25/30%, retenciones (Arts. 20-23), 22-A asalariados, ganancias de capital (23-24), renta extranjera | Art. 1-9 concepts → taxation; Art. 10-18 deducciones → taxation; Art. 20-31 retenciones/pagos a cuenta → taxation + payroll; anexos → taxation | taxation, fiscal-reporting |
| 2 | `07/08/09/10/12` (tabla series + plantilla 11) | Asalariados progressive scale vintages FY2022-2026 (IPC-indexed from 2023) | each as data; 11_ formulas = computation semantics | taxation, payroll |
| 3 | `04/21/22/80` (D. 17-2010 + Reglamento + interp + 22-A reform) | Renta de capital 10%, retención 1% anticipo, impuesto neto base | whole each | taxation |
| 4 | `05_Ley_Eficiencia` (D. 113-2011 cons.) | Impuesto mínimo (1.5% activo neto), 5% solidario, pagos a cuenta | whole | taxation |
| 5 | `02_Ley_ISV` (D.L. 24 cons. D.L. 59-2022) | ISV 15%, base, exenciones Art. 15, débito/crédito, retenciones Art. 8 | Art. 1-8 core → taxation; Art. 15 exemptions → taxation; regimen simplificado → taxation | taxation, fiscal-reporting |
| 6 | `03_Codigo_Tributario` (D. 170-2016 act. 2020) + `23_sentencia` | RTN, obligaciones, declaraciones, prescripción, sanciones, deberes formales; Art. 206 VOID | libros/deberes → all; sanciones → taxation; RTN → all | all |
| 7 | `24/25/26/76/77/78` facturación stack + `18_compras_eventuales` | Régimen de facturación: documentos fiscales, imprentas, autoimpresores, autorizaciones, límites/validez, notificaciones | whole (consolidado 68 pp main) | e-invoicing |
| 8 | `14/15/16/17` (DJIMR, DMC chain) + `19/20` (tarjetas/retenciones mods) | Monthly informativas: retenciones detail + compras detail; ISV card-retention procedure | whole each | fiscal-reporting |
| 9 | `13_SAR-619` + `67_Ayuda_EEFF` | EEFF previo a DJ ISR (FY2024+) | whole | fiscal-reporting, chart-of-accounts |
| 10 | `29-75` Ayuda/Generalidades (42 files) | Per-código declaration mechanics (102/103/106/107/111-138/152/154/201-217/259/502-545) + regime overviews | per-código, batched by family (ISR annual / retenciones / ISV / selectivo / contribuciones / informativas) | fiscal-reporting |
| 11 | `81/27/28` (IHSS aportaciones + RAP fondo reserva + regularización) | 2024 social-security architecture: IHSS ceilings/rates, RAP-IVM 1.5+1.5, fondo reserva 4% | whole each | payroll |
| 12 | `82/83/84` salario mínimo instruments | Wage floors: sector tables 2023, bienio 2024-2025 | tables as data | payroll |
| 13 | `86_Codigo_Trabajo` (D. 189-1959, 271 pp) | Jornada, salario, aguinaldo (13th), vacaciones, cesantía/preaviso (vs RAP fondo), terminación, mujeres/menores | Books: contrato/jornada/salario → payroll units; prestaciones (T. II) → payroll; SMT (sindicatos) skim | payroll, commercial-legal |
| 14 | `06_D.7-2026`, `75`, `22`, `79/80` misc | Amnistía (ancillary), suspensión PN, interp Art. 19, reforms | light reads | taxation |

## Reading order

Dependency-aware (SV-proven pattern: core law vocabulary first, reporting on
top, payroll parallel, facturación standalone):

1. **Foundations — taxation core**: ISR (1) + tabla series (2) + D.17-2010
   family (3) + Eficiencia (4) → ISV (5) → CT (6). Everything cites these.
2. **Fiscal reporting**: DMR/DJIMR + DMC (8) → Ayuda per-código (10) →
   SAR-619/EEFF (9). Needs ISR/ISV concepts in place.
3. **Facturación** (7): standalone; can run parallel after (1).
4. **Payroll**: tabla/retención consumer side rides (1-2); then IHSS/RAP
   architecture (11) → salario mínimo (12) → Código del Trabajo (13).
5. **Chart of accounts**: thin — Código de Comercio (NOT yet acquired, open
   lead) + EEFF inform (9); decide whether a wave is warranted at synthesis.
6. **Closers**: misc (14), special regimes (later corpus additions).

## Topic map (source unit → topic)

| Topic | From |
|-------|------|
| `taxation/` | 1, 2, 3, 4, 5, 6(partial), 14 |
| `fiscal-reporting/` | 6(partial), 8, 9, 10 |
| `e-invoicing/` | 7, 18_ |
| `payroll/` | 2(partial), 11, 12, 13 |
| `chart-of-accounts/` | 9 + Código de Comercio (open) |
| `commercial-legal/` | 13(partial) + Código de Comercio (open) |

## Known risks

- **Scanned/no-text-layer sources (OCR needed)**: `04_` (D. 17-2010), `21_`
  (Reglamento 1121-2010). Damaged text layers: `81_` (D. 48-2024 rates page),
  `26_` (partial mojibake). ISR tables in `07_/08_/09_/10_/12_` print as
  images — OCR with PSM-4-at-400dpi table discipline (SV lesson); `11_`
  plantilla formulas are the cross-check.
- **CT consolidation currency**: `03_` stops at D. 180-2020; post-2020 CT
  reforms unverified — per-article verification at evidence (SV SOQ-22 kin).
  Art. 206 void (`23_`) must never be implemented.
- **Código del Trabajo vintage**: `86_` print's consolidation date unknown —
  pin key articles (aguinaldo 376-family, vacaciones 328-family, cesantía,
  preaviso, jornada) against reform chain; D. 93-2021 derogations are
  repeal-only (numbered articles dead — do not implement; list in `85` gap).
- **IPC-indexed table vintages**: FY2026 table (SAR-01-2026) is operative;
  each annual FR must carry valid_from/valid_to — dated rows, never replace
  (SV CAT-013 lesson). Watch for SAR-xx-2027 (Jan-2027) for FY2027.
- **Salario mínimo 2026-2027**: bienio 2024-2025 still current (Feb-2026
  evidence via SAR-43-2026); successor instrument watch — wage floors are
  dated data.
- **D. 48-2024 rate split**: ceilings captured; the EM/IVM rate articles sit
  in the damaged-text page — OCR before any FR trusts a rate value. The
  Ley Seguro Social itself (D. 140-1959 + D. 80-2001) is only on IHSS's KB
  pages (open lead) — capture if payroll wave needs law-level text.
- **RAP framework**: Ley RAP D.L. 107-2013 full text not acquired — `27_`
  Art. 16 transcription covers the operative payroll articles (42/43/61);
  acquire the full law before any deeper RAP FRs.
- **No retenciones-master reglamento**: HN retenciones live in Ley ISR Arts.
  20-23 + D. 17-2010 + per-código helps + DJIMR — do not expect an SV-anexo
  style single instrument.
- **La Gaceta archive absent**: gazette originals only via SAR republications
  (fine — official copies with gazette numbers); pin publication dates from
  the PDFs themselves.
- **LJT bill**: if passed, taxation core needs a supersession pass before
  synthesis — check status at wave start.

## Process notes

- Waves follow the shared procedure: extract → evidence → synthesis (SDD) →
  coverage. Evidence files land in `hn/.extractions/` (git-ignored except
  committed analysis artifacts — mirror SV's `.gitignore` exceptions when the
  master index is created).
- Registry additions continue numbering from 87 (`sources/README.md` §Numbering).
- Fetch recipes: RESEARCH.md §6.
