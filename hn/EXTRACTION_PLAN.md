# Honduras — Requirements Extraction Plan

Execution plan per [shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md).
Started 2026-08-19 (source-research pass complete). Status: active — **evidence wave W1 in progress**.

## Wave log

- **W1a (2026-08-19, DONE):** Ley ISR `01_` evidence (EVID-001..015, 6 OQs).
  Key: PJ 25% / PN IPC-indexed progressive (FY2026 table = `07_` +4.98%);
  22-A gross-minimum regime; dividends 10% w/ 100-day deemed-anticipo;
  12.5% services retention w/ composite L257,493.16 gate; NOL 3y/50%/sector;
  **13th AND 14th month each exempt ≤10 SMM promedio (Art. 10.h)**.
- **W1b (2026-08-19, DONE):** Ley ISV `02_` evidence (EVID-016..026, 4 OQs).
  Key: 15%/18%/0 rate matrix; ISV-in-price for final consumers; OTCD card
  10%-of-tax retention + 15% no-discrimination fallback; débito/crédito with
  4-month credit window + pro-rata; L250k simplified regime; Anexo I
  SAC-coded canasta; invoice-date-first taxable event.
- **W1c (NEXT):** Código Tributario `03_` (242 pp — book-by-book units: RTN/
  deberes/books/declarations/prescripción/sanciones; Art. 206 VOID per `23_`;
  post-2020 delta = `89_` D.117-2021). Then D.17-2010 family (`04_/21_/22_`),
  Eficiencia `05_`, tabla series (`07_-12_` + plantilla formulas).
- Text extractions done for: 01/02/03/05/23/79/80/89. Pending: 04, 21 (OCR),
  87 (OCR), tables 07-12 (text+image tables), rest at their wave.

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
| 7 | `24/25/26/76/77/78` facturación stack + `18_compras_eventuales` | Régimen de facturación: documentos fiscales, CAI/rangos/vigencia, imprentas, autoimpresores (máquinas registradoras + sistemas computarizados specs), **Sistema de Emisión Electrónica + CAEE (Arts. 50-58)**, authorization procedure (Art. 59-61), compras eventuales | `24_` whole: T. I-II defs + documentos → T. IV medios (imprenta/autoimpresor/SEE) → T. V autorización → T. VI imprentas registro | e-invoicing |
| 8 | `14/15/16/17` (DJIMR, DMC chain) + `19/20` (tarjetas/retenciones mods) | Monthly informativas: retenciones detail + compras detail; ISV card-retention procedure | whole each | fiscal-reporting |
| 9 | `13_SAR-619` + `67_Ayuda_EEFF` | EEFF previo a DJ ISR (FY2024+) | whole | fiscal-reporting, chart-of-accounts |
| 10 | `29-75` Ayuda/Generalidades (42 files) | Per-código declaration mechanics (102/103/106/107/111-138/152/154/201-217/259/502-545) + regime overviews | per-código, batched by family (ISR annual / retenciones / ISV / selectivo / contribuciones / informativas) | fiscal-reporting |
| 11 | `81/27/28` (IHSS aportaciones + RAP fondo reserva + regularización) + `87_Ley_IHSS` + `88_Regl_Incapacidad` | 2024 social-security architecture: IHSS ceilings/rates, RAP-IVM 1.5+1.5, fondo reserva 4%; law-level IHSS text (scanned); sick-leave subsidy mechanics | whole each | payroll |
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
  (Reglamento 1121-2010), `87_` (Ley IHSS). Damaged text layers: `81_`
  (D. 48-2024 rates page), `26_` (partial mojibake). ISR tables in
  `07_/08_/09_/10_/12_` print as images — **OCR feasibility CONFIRMED
  2026-08-19**: gs 400dpi + tesseract PSM 4 recovered the full SAR-01-2026
  FY2026 scale (exentos ≤ L228,324.32 / 15% ≤ L348,154.10 / 20% ≤
  L809,660.75 / 25% beyond; minor spacing noise only). `11_` plantilla
  formulas remain the cross-check.
- **CT consolidation currency (UPDATED 2026-08-19)**: `03_` stops at D. 180-2020;
  the SAR catalog's complete post-2020 CT instrument set = **D. 117-2021
  (interpretación Art. 113.1 — acquired as `89_`)** + the Art. 206 sentencia
  (`23_`, void). Known gap CLOSED at research level; still verify per-article
  at evidence (SV SOQ-22 lesson — catalogs can under-report).
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
- **SEE technical documentation absent**: the CAEE algorithm/specs and the
  incorporation calendarización (Acuerdo 481-2017 Arts. 57-58) are not
  publicly posted — SEE FRs can only cite the reglamento's own text until the
  docs are acquired (open lead 1, RESEARCH.md §5). Hint-layer recollection
  (CAI/ranges/expiry/overlap/exhaustion) is corpus-confirmed — see RESEARCH.md
  §7; exhaustion-alert FRs are operational derivations, flag as such.
- **LJT bill**: if passed, taxation core needs a supersession pass before
  synthesis — check status at wave start.

## Process notes

- Waves follow the shared procedure: extract → evidence → synthesis (SDD) →
  coverage. Evidence files land in `hn/.extractions/` (git-ignored except
  committed analysis artifacts — mirror SV's `.gitignore` exceptions when the
  master index is created).
- Registry additions continue numbering from 87 (`sources/README.md` §Numbering).
- Fetch recipes: RESEARCH.md §6.

## Decisions (binding for HN synthesis)

- **D-H1 (2026-08-19, product owner): Odoo journal architecture uses
  `l10n_latam_invoice_document`** — ONE journal per company carrying multiple
  `l10n_latam.document.type` entries, NOT one journal per document type.
  Consequences for synthesis:
  - Odoo Mapping sections model the facturación document taxonomy
    (24_ Arts. 5-8: Comprobantes Fiscales / Documentos Complementarios /
    Otros Comprobantes) as `l10n_latam.document.type` records, not as
    journals.
  - Sequences attach at document-type level (per punto de emisión), aligning
    with the CAI rango-autorizado + 16-digit correlativo regime (Art. 16
    structure: establecimiento/punto de emisión/tipo de documento/talomera +
    secuencia) — the CAI/authorization ledger keys on
    (punto de emisión, document type), never on journal.
  - **Numbering-structure Odoo mapping (design guidance, product-owner
    prior implementation; statutory anchor = 24_ Art. 10 num. 7 + Arts.
    48-49, 61):** the sequence identifier's two location segments map to
    inventory structures — **establecimiento ("sucursal") →
    `stock.warehouse`** (company-level branch code, casa matriz = 000;
    NOT `stock.location`), and **punto de emisión ("caja") → a child
    emission point of the warehouse** (each máquina registradora/dispositivo
    is its own punto de emisión per Art. 61; Art. 49 places puntos fijos
    within establecimientos). Synthesis must reconcile this with
    D-H1's document-type-level sequences: the full sequence key is
    (establecimiento, punto de emisión, document type) = (warehouse,
    emission point, `l10n_latam.document.type`). Note for evidence pass:
    "caja" is implementation vocabulary — the statute says punto de emisión.
  - **Emission point does NOT live on `account.journal`** (prior
    implementation put the terminal on both journal and move — incompatible
    with one-journal D-H1): it belongs on the move / a dedicated emission-
    point entity feeding the sequences. A **user ↔ emission-point
    authorization matrix** (per prior customer practice) is a legitimate
    operational-internal-control FR candidate — label non-statutory
    (24_ has no operator restrictions; hook = 76_ "acreditación de
    responsables"). See RESEARCH.md §7 item 3.
  - Cross-country propagation (GT/SV): NOT decided here — this session owns
    HN only; raise at merge for the product owner to carry into the other
    countries' plans.
