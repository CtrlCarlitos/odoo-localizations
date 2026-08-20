# HN — e-Invoicing (facturación) requirements index

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | e-invoicing |
| Status  | approved (V-HN1 validation wave 2026-08-20; see EXTRACTION_PLAN wave log) |
| Authors | Takumi synthesis wave S-HN2 + controller |
| Updated | 2026-08-20 |

This directory holds the S-HN2 (synthesis wave HN-2) facturación
requirements. **Honduras has NO national XML/DTE transmission regime**:
the current regime is paper-based (CAI/rango/vigencia) under the
*Reglamento del Régimen de Facturación* (Acuerdo 481-2017 consolidado,
`24_`) administered digitally through SAR's Oficina Virtual, plus a
statutory Sistema de Emisión Electrónica (SEE) with per-document CAEE
(Arts. 50-58) whose technical documentation is UNPUBLISHED (lead 1 —
that sub-cluster ships config-gapped placeholders, `24_ OQ-4`).
Built from master-index clusters E1-E8 (W3 evidence, EVID-186..214);
D-H1 (journal/sequence architecture), D-H2 (dated rows + hard emission
gate), D-H3 (ingestion depths) bind throughout. Source-to-requirements
coverage: [../COVERAGE.md](../COVERAGE.md) (V-HN1 gate 1, script-checked).

## Files & FR ranges

| File | Scope (clusters) | FR range | FRs | LBs | ACs | OQs |
|------|------------------|----------|-----|-----|-----|-----|
| [01_document-types-numbering.md](01_document-types-numbering.md) | 3 statutory categories, type-code catalog (`document_types.csv` sidecar), 16-digit grammar + wrap, dual 14-digit historical parser, code-10 collision guard (E1+E2) | HN-EINV-FR-001..031 | 31 | 16 | 14 | 6 |
| [02_cai-ledger-emission-gate.md](02_cai-ledger-emission-gate.md) | CAI vs CAEE, rango ledger key, ONE-active-rango, renewal T-2mo, vigencia ≤1y dated rows, D-H2.2 HARD emission gate, ANULADA/no-utilizados lifecycle, imprenta registry (E3+E7) | HN-EINV-FR-046..086 | 41 | 20 | 25 | 6 |
| [03_document-mechanics.md](03_document-mechanics.md) | Two-layer print contract, L10,000 ID threshold, sales-doc mechanics (factura/export/zona-libre/prevalorada/ticket/RHP/L50), complements (boleta compra/NC-ND origin triple/guías/retención) (E4+E5+E6) | HN-EINV-FR-091..140 | 50 | 17 | 21 | 7 |
| [04_registration-topologies-medios-see.md](04_registration-topologies-medios-see.md) | Inscription matrix, topologies, medios, SFC specs, SEE/CAEE config-gapped placeholders + Art. 57 gradual mandate dated rows, contingencia, user↔punto matrix (E8) | HN-EINV-FR-141..175 | 35 | 16 | 14 | 8 |
| **Total** | | HN-EINV-FR-001..175 | **157** | **69** | **74** | **27** |

Numbering note: FR ranges pre-allocated per file; unused tails
(032-045) stay reserved; 085-090 was partially consumed at V-HN1 (FR-085
filed-period freeze + FR-086 go-live reconciliation, D-H2.5/D-H3.2
implementations — adversarial-review gap closures); 087-090 remain
reserved. The `document_types.csv` sidecar
carries the type-code catalog × grammar era (20 rows, extended status
vocabulary documented in file 01 §4 — historical, collision-guarded,
reserved-machine-prefix); it carries no FRs of its own.

## Wave notes (controller)

- **No-transmission corollary:** the D-H2.2 CAI-vigencia emission gate
  (file 02, **FR-066** — V-HN1 index fix: was mis-pointed at FR-063) is
  HN's functional counterpart to SV's transmission gate — there is no
  other emission control to model.
- **Grammar switching is date-primary with a transition window**
  (R-Art. 76: 189-2014-authorized stock runs until its own fecha
  límite) — file 01 FR-022 + OQ-006; not a pure date cutover.
- **SEE sub-cluster BLOCKED** (lead 1): FR-166..169 of file 04 are
  config-gapped placeholders citing only the reglamento's own text;
  quarterly re-check. Everything else in the wave is evidence-complete.
- **Retention rates are consumed by id** from
  `../taxation/04_isr-withholding.md` (HN-TAX-FR-137..148) — never
  restated here.
- **Code-10 collision invariant** (R-H38): file 01 FR-009 single-
  assignment guard — NEVER implement 10 as both Compras Eventuales and
  Prevalorada; resolving lead = post-2017 SAR instrument.

## Open-questions summary

27 OQ rows (wave total, 26 open — 01 OQ-005 resolved via R-H42);
blocking only the SEE sub-cluster (file 04
OQ-001). Others: ticket dual code verification, code-02 reserved
status, mid-vigencia SAR limit practice, L10,000 SEFIN modifications,
SAR-924/926/927 form-print fidelity leads. Full text per file §7;
register mapping to master-index C3 recorded per file.
