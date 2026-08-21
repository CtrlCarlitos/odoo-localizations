# GT — Chart of accounts — Retention/destruction max-per-object matrix (the GOQ-124 deliverable)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-21 |

## 1. Purpose

This file is the GOQ-124 deliverable: the consolidated
RETENTION/DESTRUCTION MAX-PER-OBJECT MATRIX — the single canonical
objects-×-regime table the corpus waves consume by id, never restated. It is
a PURE CONSUMER: it assembles the conservation/retention rules of the S-GT5
wave's own files (C1 books conservation GT-COA-FR-026..029; C5 prescription
ladder + factura cambiaria GT-CML-FR-108/110..122/124/125; C6 AML retention
GT-CML-FR-156) and of the earlier waves (taxation GT-TAX-FR-230 family,
esp. GT-TAX-FR-232 prescription-anchored conservation — the practical floor;
fiscal-reporting GT-FIN-FR-104/118 LET surfaces; e-invoicing GT-EINV-FR-203
emitter-side XML retention) by exact FR id, asserts NO new statutory claim,
and adds only the synthesis layer: the per-object-class matrix (§4), the
longest-per-object (MAX) resolution, the destruction-gate engine (no
execution while any applicable row is unexpired or any matter is pending),
the per-row retention clock start-events, and dated-row discipline on every
value. GOQ-124 closes in-file (§7, OQ-001 → resolved): the matrix is the
deliverable; taxation's OQ-007 pointer (GT-TAX-FR-232) and the GT-EINV
OQ-005/GOQ-41 reconciliation land here (OQ-003).

It does **not** cover: the underlying duties themselves (owned by their
files — this file cites by id, never restates); the Civil-law prescription
values behind the art. 1 fallback (Código Civil not in the corpus — OQ-002,
never guessed); IGSS planilla retention (no owning FR exists in
`payroll/07_igss-contributions.md`, controller grep 2026-08-21 — ABSENCE
row FR-071, never invented); prescription-interruption mechanics, aging and
sanction surfaces (owned by GT-CML-FR-123/124 and GT-TAX-FR-205/206/208,
consumed by id); and DTE archive-tier architecture (D3-owned, e-invoicing
wave — outcome cross-refs only).

## 2. Legal Basis

Authority note: this file is a pure consumer — every LB row below is
carried from a consumed file's OWN citation (marked "via GT-XX-FR-nnn");
the full Spanish texts, evidence verification against
`gt/.extractions/*.evidence.md` and the GOQ-123 live-regime note on every
66_-family citation live in the owning files (`01_books-anchor.md` §2 for
the CCom authority order; `03_titulos-valores-prescripcion.md` §2 for the
ladder; `04_aml-compliance.md` §2 for the AML cutover spine). Where this
table and an owning file diverge, the owning file governs. Dated-instrument
discipline (D15/D16) applies to every row: instrument, article,
valid_from/valid_to and flags are stored on the matrix config rows (FR-074).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CCom art. 376: "Los comerciantes, sus herederos o sucesores, conservarán los libros o registros del giro en general de su empresa por todo el tiempo que ésta dure y hasta la liquidación de todos sus negocios y dependencias mercantiles." (via GT-COA-FR-026) | Merchants, their heirs or successors shall conserve the books/registers of the enterprise's giro for the whole time it lasts and until the liquidation of all its businesses and mercantile dependencies | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83, art. 376 (EVID-511; LB-009 of `01_books-anchor.md`) |
| LB-002 | CCom art. 382: "…deberá conservar, en forma ordenada y organizada, durante no menos de cinco años, los documentos de su empresa, salvo lo que dispongan otras leyes especiales." (via GT-COA-FR-027) | Enterprise documents conserved in orderly, organized form for not less than five years, except as other special laws provide (the deference clause by which longer regimes extend the floor) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.84, art. 382 (EVID-516; LB-014 of `01_books-anchor.md`) |
| LB-003 | CCom arts. 383-384 + art. 1: "Los documentos que conciernan especialmente a actos o negociaciones determinadas, podrán ser inutilizados o destruidos, pasado el tiempo de prescripción de las acciones que de ellos se deriven." / "Si hubiere pendiente alguna cuestión que se refiera a ellos directa o indirectamente, deberán conservarse hasta la terminación de la misma." (via GT-COA-FR-028; GT-CML-FR-125) | Documents concerning determined acts/negotiations may be destroyed once the prescription of the derived actions has elapsed; pending-matter hold (direct or indirect); art. 1 defers CCom gaps to Civil law — no general commercial prescription period exists | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.85 arts. 383-384; p.2 art. 1 (EVID-517; LB-015 of `01_books-anchor.md` / LB-014 of `03_titulos-valores-prescripcion.md`) |
| LB-004 | CCom art. 604: "Los comerciantes deberán conservar ordenadamente, por el término de cinco años, las facturas cambiarias que hubieren librado o copias de las mismas." (via GT-CML-FR-108) | Merchants must conserve orderly, for the term of five years, the facturas cambiarias they have drawn or copies thereof | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.123-125, arts. 596-604 (EVID-565; LB-011 of `03_titulos-valores-prescripcion.md`) |
| LB-005 | CCom per-clock prescription texts: art. 626: "La acción cambiaria directa, prescribe en tres años a partir del día del vencimiento." + arts. 627/628/409 (regreso 1 año; obligado recourse 6 meses; enriquecimiento 1 año) + arts. 513/541/577/799/916/1037 (cheque 6 meses; cheques de viajero 2 años; obligaciones intereses 5 años / capital 10 años; transporte 6 meses; seguro 2 años; fianza 2 años) + D2946 (old code) art. 1313 (5 años, R65) (via GT-CML-FR-110..FR-122) | The per-instrument mercantile prescription clocks — terms and anchors — that key the destruction gate for instrument-backed documents (full texts at the owning file's LB-008/LB-012/LB-013) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | cml03 LB-012/LB-013 (EVID-566/567); cheque LB-008 (EVID-563); D2946 appendix pp. 298-301 (R65) |
| LB-006 | CT D-6-91 Arts. 112 y 112 "A": conservation of books, documents, archives, bank statements and information systems in orderly form while the prescription term has not run; electronically filed declarations/annexes conserved in the original medium or paper at the taxpayer's choice (via GT-TAX-FR-232; prescription terms via GT-TAX-FR-203/204) | Prescription-anchored tax conservation — the practical floor of the matrix (4 years general / 8 years unregistered, with the interruption engine) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 60-62, Arts. 112 y 112 "A" (EVID-205; LB-018 of `taxation/06_ct-procedures.md`) |
| LB-007 | AD 13-2018 art. 21: "El emisor debe conservar los archivos en formato XML de los DTE certificados mientras no haya transcurrido el plazo de prescripción que establece el Código Tributario, de igual forma el receptor, cuando corresponda." (via GT-EINV-FR-203) | The emitter must conserve the certified-DTE XML files while the Código Tributario prescription period has not run; likewise the receiver, where applicable (the certificador's 14-month "hasta conciliación" backup is provider-side — excluded) | `gt/sources/01_AD_13-2018_FEL.pdf` | Art. 21, p. 10 (EVID-046; LB-015 of `e-invoicing/05_certificador-interface.md`) |
| LB-008 | LET manuals (57_/58_/82_): "Contar con habilitación de libros computarizados de compras y de ventas … en estado Activo" / folio assignment "…reconociendo el número de hojas habilitadas por el contribuyente, de conformidad con el artículo 5 numeral 4 de la ley de Timbres Fiscales…" (via GT-FIN-FR-104/FR-118) | LET adoption requires an active computerized-books habilitación; folios assigned automatically against the hojas habilitadas (Ley de Timbres Fiscales art. 5 num. 4); first-use último folio immutable | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` et al. (via txt) | 57_ pp.6,15,22; 58_ pp.6,12,17,23; 82_ pp.6,14,21-22 (EVID-475; LB-025 of `fiscal-reporting/04_let-electronic-books.md`) |
| LB-009 | D-15-2026 Art. 34: "Las Personas Obligadas deberán conservar toda la documentación, expedientes y registros físicos, digitales o electrónicos relacionados con las transacciones u Operaciones realizadas, por un plazo mínimo de cinco (5) años contados a partir de la finalización…" + the art. 3.a/b financial-PO additional 10-year digital continuation; pre-cutover layer: D-67-2001 art. 23 (5-year retention, integral-reconstruction standard) (via GT-CML-FR-156) | AML retention: ALL POs ≥ 5 years from transaction finalization (compliance-obligation records from relation end / occasional transaction); financial POs (art. 3.a/b) continue ≥ 10 further years on optical/magnetic/electronic media — effective 15-year archive; regime rows keyed 2026-09-17 (R60) | `gt/sources/77_AML_LeyIntegral_D15-2026.pdf`; pre-cutover `gt/sources/75_AML_D67-2001.pdf` | 77_ Art. 34 (EVID-622; LB-013 of `04_aml-compliance.md`); 75_ art. 23 (EVID-639; LB-023 there) |

## 3. Functional Requirements

### 3.1 The canonical matrix and the max-per-object rule

- **GT-COA-FR-061:** The system shall implement THE canonical
  retention/destruction matrix (§4) — the single objects-×-regime table
  every wave consumes by id: one row per object class (CCom books; CCom
  giro documents; factura cambiaria issued-facturas/copies; CT tax
  books/documents/e-filings; DTE/FEL certified XML + acuses; LET/libros
  electrónicos; AML records; the IGSS planilla absence row), each row
  carrying its regime, basis instrument + FR-id citation, retention rule,
  clock start and destruction gate. EFFECTIVE RULE = MAX across applicable
  regimes per object (longest-per-object): an object's retention floor is
  the longest of every applicable row, never any single row's term. The
  matrix is a pure consumer — every row cites the owning FR ids
  (GT-COA-FR-026..029; GT-CML-FR-108/110..122/125/156;
  GT-TAX-FR-230..232; GT-FIN-FR-104/118; GT-EINV-FR-203) and no statutory
  content is asserted beyond them. This is the GOQ-124 deliverable (OQ-001
  → resolved): taxation OQ-007 (GT-TAX-FR-232's pointer) and cml03 OQ-002
  resolve against THIS table. (LB-001..LB-009; GOQ-124)
- **GT-COA-FR-062:** The system shall compute and enforce per-object
  retention FROM the matrix: every retained object (legal book, giro
  document, factura cambiaria, tax book/declaration, certified DTE
  XML/acuse, LET book record, AML record) carries its applicable regime
  tags, the applicable rows' anchor dates, and a computed
  *retention-until* = MAX of the applicable rows (clock anchor + term);
  the resolved value is stored on the record (snapshot-on-write, D16) with
  the governing row identified. Premature purge shall be REFUSED with the
  governing row named. Regime applicability is fed by the owning files
  (AML PO applicability = GT-CML-FR-130/133 by id; DTE emitter scope =
  GT-EINV-FR-203; tax-book scope = GT-TAX-FR-230..232) — never recomputed
  here. (LB-001..LB-009)

### 3.2 Matrix rows — one FR per object class

- **GT-COA-FR-063:** ROW — CCom legal books (the four mandatory books of
  GT-COA-FR-002, voluntary auxiliaries, corredor registers): conservation
  is LIQUIDATION-ANCHORED with NO year count — the whole life of the
  enterprise AND until the liquidation of all its businesses and mercantile
  dependencies, binding merchants, heirs and successors (custody
  succession recorded per GT-COA-FR-026). Clock start = full-liquidation
  close. Destruction gate = full-liquidation close AND the art.-383
  predicate (FR-072); no destruction of books derives from the CCom alone.
  (LB-001; via GT-COA-FR-026; GOQ-123 rides the 66_ citation)
- **GT-COA-FR-064:** ROW — CCom giro documents (correspondence, valores,
  comprobantes/documents fehacientes of the giro): conserved orderly and
  organized for NOT LESS than five años, "salvo lo que dispongan otras
  leyes especiales" — the explicit deference clause by which longer
  special-law regimes (tax corpus row FR-066; AML row FR-069; DTE row
  FR-067) extend this floor, with the effective rule = MAX. Correspondence
  is this documents duty, never a book (GT-COA-FR-006/R63); archive medium
  is free (GT-COA-FR-029). Clock start = per-document issue/receipt.
  Destruction gate = art.-383 prescription of the underlying action +
  no-pending-matter (FR-070 keys, FR-072 engine). (LB-002; LB-003; via
  GT-COA-FR-027/028/029)
- **GT-COA-FR-065:** ROW — factura cambiaria issued-facturas/copies:
  merchants conserve orderly, for FIVE años, the facturas cambiarias they
  have drawn or copies thereof (art. 604, dated row: instrument D2-70,
  valid_from 1971-01-01 — R45). GOQ-124 NOTE RECORDED: this 5-year term is
  "likely superseded" by the longer applicable rows — where a factura
  cambiaria backs tax operations or an AML-reportable transaction, the CT
  prescription-anchored row (FR-066) and/or the AML row (FR-069) are longer
  and MAX governs; NO supersession is asserted from the corpus itself (per
  GT-CML-FR-108's own no-supersession note) — the matrix resolves
  max-per-object, it never cancels the art.-604 row. Anchor: art. 604
  fixes no express start; the system uses the drawing (libramiento) date
  as the conservative anchor, flagged as a system convention, not
  statutory text. Destruction gate = FR-070 keys + FR-072 engine.
  (LB-004; via GT-CML-FR-108; GOQ-124; GOQ-123 rides the 66_ citation)
- **GT-COA-FR-066:** ROW — CT tax books, documents, archives, bank
  statements, information systems and e-filed declarations/annexes:
  conservation is PRESCRIPTION-ANCHORED, not a fixed year table — books,
  documents, archives, bank statements and information systems are
  conserved in orderly form WHILE THE PRESCRIPTION TERM HAS NOT RUN (4
  años general / 8 años unregistered — GT-TAX-FR-232 → GT-TAX-FR-203/204),
  including documents evidencing tax-obligation compliance; e-filed
  declarations/annexes are conserved in the ORIGINAL medium or paper at
  the taxpayer's choice; records destroyed/lost/deteriorated/misplaced or
  hit by patrimonial crimes are RE-MADE within 3 months. Clock start =
  the tax prescription engine's anchors (obligation due date +
  interruption restarts, GT-TAX-FR-205; the independent 5-year
  infraction/sanction clock, GT-TAX-FR-206) — with the filing event
  recorded as the freeze-at-filing anchor for declarations (D16).
  Destruction gate = ALL applicable tax clocks run out + no-pending-matter
  (a pending determination/liquidation is itself an unexpired row —
  FR-072). Placement kin: books/registers at the domicilio fiscal or the
  contador's office (GT-TAX-FR-231, art. 21 "B".2); family context:
  GT-TAX-FR-230 heads the §3.9 family — VOCABULARY GUARD: its
  "retention" = agentes de retención (withholding agents), a payment
  mechanism NEVER to be conflated with record conservation. (LB-006; via
  GT-TAX-FR-230/231/232 → GT-TAX-FR-203/204/205/206)
- **GT-COA-FR-067:** ROW — DTE/FEL certified XML + acuses (emitter-side;
  receiver-side "cuando corresponda"): the emitter conserves the certified
  XML files while the Código Tributario prescription period has not run
  (AD 13-2018 art. 21) — i.e. this row's retention anchor IS the CT
  prescription anchor of FR-066 (terms via GT-TAX-FR-203/204, clock
  mechanics GT-TAX-FR-205/206). GOQ-41/OQ-005 CLOSURE (named rule): the
  resolved reconciliation = emitter-side retention of certified XML +
  acuses runs to the CT prescription period via GT-EINV-FR-203 anchored on
  GT-TAX-FR-232's prescription-anchored conservation; the certificador's
  14-month "hasta conciliación" backup is PROVIDER-side and shall never be
  modeled as the emitter's duty (vocabulary guard carried from
  GT-EINV-FR-203). Destruction gate = FR-066's tax clocks + no-pending
  matter (FR-072); DTE purge protection and archive-tier mechanics are
  owned by the GT-EINV wave — outcome-only cross-refs here. Kin: the
  SAT-AUTHORIZED destruction route for paper originals converted to
  electronic records (CT 98-"A".2 via GT-TAX-FR-234) is a distinct,
  authorization-gated destruction path — no paper-destruction workflow
  runs without it. (LB-007; LB-006; via GT-EINV-FR-203, GT-TAX-FR-232;
  GOQ-41 kin → OQ-003)
- **GT-COA-FR-068:** ROW — LET/libros electrónicos (electronic tax books
  and their resumen/folio surfaces): retention is TAX-PRESCRIPTION-ANCHORED
  as row FR-066 (LET books and their filings are CT books/e-filings —
  GT-TAX-FR-232), with the fin04 lifecycle surfaces consumed as gates, not
  periods: adoption requires an ACTIVE computerized-books habilitación
  (GT-FIN-FR-104) and the first-use último-folio capture is immutable with
  folios assigned against the hojas habilitadas under Ley de Timbres
  Fiscales art. 5 num. 4 (GT-FIN-FR-118). NO LET-specific retention period
  is printed in the consumed manuals — none is invented; the row inherits
  the FR-066 anchor and gates. Clock start/gate = per FR-066, plus the
  book's habilitación/folio lifecycle states recorded (dual-track model =
  `02_dual-track-habilitacion.md` by id). Vocabulary guard: the manuals'
  *constancias de retención* are withholding certificates (a document
  type), never a record-retention rule. (LB-008; LB-006; via
  GT-FIN-FR-104/118, GT-TAX-FR-232)
- **GT-COA-FR-069:** ROW — AML records (all POs: documentation,
  expedientes and registros — physical, digital or electronic — of
  transactions/operaciones; compliance-obligation records): ≥ 5 años from
  the FINALIZATION of the transaction (compliance records from the END of
  the business relation or of the occasional transaction), with the
  integral-reconstruction sufficiency standard; FINANCIAL POs (art. 3.a/b
  only) continue after the 5-year minimum on optical/magnetic/electronic
  media guaranteeing integrity, correct reading, inalterability and
  adequate conservation for an ADDITIONAL ≥ 10 años (effective 15-year
  archive). Dated regime rows (R60): post-cutover facts (from
  2026-09-17) resolve against 77_ (D-15-2026 art. 34); pre-cutover facts
  (17-dic-2001 → 16-sep-2026) resolve against 75_ (D-67-2001 art. 23:
  5-year retention with reconstruction standard — NO 10-year digital
  extension pre-cutover). Clock start = transaction end / relation end /
  occasional transaction. Destruction gate = row expiry + no-pending
  matter (an open inusual/sospechosa case or RTS is a pending matter —
  FR-072). (LB-009; via GT-CML-FR-156 + the cml04 regime spine; R60)
- **GT-COA-FR-070:** The system shall key every document-class row's
  destruction gate to the PER-INSTRUMENT PRESCRIPTION KEYS, never to a
  guessed general period: commercial keys = the GT-CML-FR-111..FR-122
  ladder (cambiaria directa 3y from maturity; regreso 1y;
  obligado-recourse 6m; enriquecimiento 1y chained; cheque 6m dual-anchor;
  cheques de viajero 2y; debenture intereses 5y / principal 10y;
  transporte 6m; seguro 2y; fianza 2y; D2946 old-code maritime 5y with the
  R65 citation guard) consumed via GT-CML-FR-124 (aging surface:
  class + anchor + expiry per record) and GT-CML-FR-125 (gate); tax keys =
  GT-TAX-FR-203/204/205/206 via GT-TAX-FR-232; AML keys = the FR-069
  terms. GT-CML-FR-110's NEGATIVE anchor binds: the CCom enacts NO
  general commercial prescription period (art. 1 → Civil) — the cc_fallback
  key carries an OPEN value (OQ-002) and NO Civil-code period is modeled
  or defaulted. (LB-003; LB-005; LB-006; via GT-CML-FR-110..FR-125,
  GT-TAX-FR-232)
- **GT-COA-FR-071:** ROW — IGSS planilla records (ABSENCE row,
  load-bearing): NO owning retention FR exists in
  `payroll/07_igss-contributions.md` (controller grep 2026-08-21; writer
  sweep agrees — no conservation/archive term in that file). The system
  shall assert NO IGSS-specific retention period and shall not seed an
  IGSS row with an invented term; planilla/IGSS records fall under the
  generic applicable rows (CCom giro documents FR-064; CT corpus FR-066
  where they back tax obligations) with MAX governing. Landing an owning
  instrument (IGSS/acuerdo/Ley orgánica del IGSS retention clause)
  re-opens this row via acquisition. (LB-002; LB-006; absence verified
  2026-08-21)

### 3.3 Destruction-gate engine, clock starts, dated rows

- **GT-COA-FR-072:** The system shall implement the DESTRUCTION-GATE
  ENGINE: the destruction workflow shall NOT execute for an object while
  (i) ANY applicable regime row is unexpired (MAX rule — every row must be
  past its retention-until, including interruption-restarted tax clocks
  and chained commercial clocks), or (ii) ANY matter concerning the object
  directly or indirectly is pending (art. 383.2 pending-matter hold —
  judicial/administrative proceedings, SAT determinations/liquidations,
  AML cases, corredores exhibición orders). The gate predicate =
  GT-COA-FR-028 (prescribed AND no-pending-matter) + GT-CML-FR-125
  (per-instrument keys); a pending matter is recorded as a hold row on the
  object and blocks execution until terminated. Destruction itself
  remains a human/merchant act at the merchant's archive discretion
  (GT-COA-FR-029): the system computes ELIGIBILITY and refuses premature
  execution — it never auto-destroys. The SAT-authorized paper-destruction
  route (GT-TAX-FR-234 kin, FR-067) additionally requires the recorded
  authorization. (LB-003; via GT-COA-FR-028/029, GT-CML-FR-125,
  GT-TAX-FR-232/234)
- **GT-COA-FR-073:** The system shall record the per-row RETENTION CLOCK
  START-EVENTS exactly as the owning FRs state them — never a single
  global anchor: CCom books → full-liquidation close (FR-063);
  declarations/e-filings → the tax prescription engine's anchors
  (obligation due date + interruption restarts via GT-TAX-FR-205) with the
  filing event as freeze-at-filing anchor (FR-066); giro documents and
  facturas cambiarias → per-document issue/receipt and drawing date
  respectively (FR-064/FR-065, the latter a flagged system convention);
  AML records → transaction finalization / relation end / occasional
  transaction (FR-069); instrument-backed commercial documents → the
  per-class anchors of GT-CML-FR-111..122 via GT-CML-FR-124 (maturity,
  presentation-close, protest, payment, issuance, journey-end,
  originating-event, enrichment-chaining). (LB-001..LB-009; via the
  consumed FR ids above)
- **GT-COA-FR-074:** The system shall carry DATED-ROW DISCIPLINE (D15/D16)
  on EVERY matrix value: each config row stores instrument, article,
  valid_from/valid_to, flags and provenance; snapshot-on-write of the
  resolved retention-until on each object; freeze-at-filing where a
  filing exists. Dated families: CCom rows = instrument D2-70, valid_from
  1971-01-01 (R45), GOQ-123 verification flag on every 66_-derived row;
  factura cambiaria row = same instrument (GOQ-124 no-supersession note);
  tax rows = CT D-6-91 as consolidated through D-37-2016 + CC 03-12-2019
  (per taxation/06 LB-018, GOQ-53 kin); DTE row = AD 13-2018; AML rows =
  regime-cutover rows keyed 2026-09-17 (pre-cutover 75_ / post 77_ — R60);
  LET gates = the 57_/58_/82_ manuals' undated-print caveat (GT-FIN-FR-105
  kin — GOQ-104, currency unverifiable from the documents). The ladder
  rows serialize under the cml03 §4 consumption contract (columns: class,
  term, unit, anchor_kind, instrument, article, valid_from, flags — one
  row per GT-CML-FR-111..122 clock) plus the matrix rows themselves
  (§4). (LB-001..LB-009; via the consumed FR ids; R45/R60/R65)

## 4. Data Model

**THE MATRIX (l10n_gt_commerce.retention_rule — dated config rows; the
canonical table other files consume by id):**

| Row | Object class | Regime | Basis instrument + consumed FR id | Retention rule (dated) | Clock start (anchor) | Destruction gate |
|-----|--------------|--------|-----------------------------------|------------------------|----------------------|------------------|
| a | CCom legal books (four mandatory + auxiliaries + corredor registers) | CCom | CCom art. 376 via GT-COA-FR-026 | whole enterprise life + until liquidation of ALL businesses/mercantile dependencies — NO year count; heirs/successors bound | full-liquidation close | liquidation complete AND art.-383 predicate (FR-072) |
| b | CCom giro documents (correspondence, valores, comprobantes) | CCom | CCom art. 382 via GT-COA-FR-027 | ≥ 5 años floor + deference clause ("salvo lo que dispongan otras leyes especiales") — MAX with rows d/e/g | per-document issue/receipt | art.-383 prescription of the underlying action + no-pending-matter (keys FR-070; engine FR-072) |
| c | Factura cambiaria issued-facturas/copies | CCom | CCom art. 604 via GT-CML-FR-108 | 5 años orderly (instrument D2-70, valid_from 1971-01-01, R45); GOQ-124: likely superseded by longer rows — no supersession asserted; MAX governs | drawing date (system convention — art. 604 prints no anchor; flagged) | FR-070 keys + FR-072 engine |
| d | CT tax books, documents, archives, bank statements, information systems, e-filed declarations/annexes | CT | CT arts. 112/112-"A" via GT-TAX-FR-232 (terms GT-TAX-FR-203/204; placement GT-TAX-FR-231; family head GT-TAX-FR-230 — withholding guard) | prescription-anchored: while the term has not run (4y general / 8y unregistered + interruptions); e-filings in original medium or paper; re-make ≤ 3 months after loss | obligation due date + interruption restarts (GT-TAX-FR-205); infraction/sanction clock 5y (GT-TAX-FR-206); filing = freeze-at-filing anchor | ALL applicable tax clocks run out + no-pending-matter (FR-072) |
| e | DTE/FEL certified XML + acuses (emitter-side; receiver "cuando corresponda") | FEL/AD + CT | AD 13-2018 art. 21 via GT-EINV-FR-203, anchored on GT-TAX-FR-232 (GOQ-41/OQ-005 closure — named rule) | while the CT prescription period has not run (= row d terms); certificador 14-month backup = PROVIDER-side, excluded | row-d tax clocks | row-d gate; paper-original destruction additionally SAT-authorized only (GT-TAX-FR-234 kin) |
| f | LET/libros electrónicos (electronic tax books + resumen/folio surfaces) | CT/LET | GT-FIN-FR-104 (habilitación-precondition gate) + GT-FIN-FR-118 (folio-continuity bridge, Ley de Timbres Fiscales art. 5 num. 4) + retention anchor GT-TAX-FR-232 | prescription-anchored as row d (no LET-specific period printed — none invented); lifecycle gates: active habilitación + immutable último folio | row-d anchors | row-d gate + habilitación/folio lifecycle states recorded (dual-track model by id) |
| g | AML records — all POs (transactions/operaciones documentation, expedientes, registros; compliance records); financial POs art. 3.a/b | AML | 77_ D-15-2026 art. 34 via GT-CML-FR-156 (pre-cutover 75_ D-67-2001 art. 23; cutover rows keyed 2026-09-17 — R60) | ≥ 5 años from transaction finalization (compliance records from relation end / occasional transaction); + ≥ 10 años digital for financial POs = effective 15-year archive (post-cutover only); reconstruction standard | transaction end / relation end / occasional transaction | row expiry + no-pending-matter (open inusual/sospechosa case or RTS = pending — FR-072) |
| h | IGSS planilla records | ABSENCE | none — no owning FR in `payroll/07_igss-contributions.md` (controller grep 2026-08-21) | NO IGSS-specific period asserted — never invented; falls under rows b/d as applicable (MAX) | per applicable rows | per applicable rows; owning instrument re-opens via acquisition |

Rules under the table: (i) **LONGEST-PER-OBJECT GOVERNS** — an object's
effective retention-until = max of all applicable rows (e.g. a financial
PO's factura: AML 15y > CT prescription row > CCom 5y floors ⇒ 15y; its
client file: 5y from relation end, extended by any longer applicable row).
(ii) **Applicability** feeds from the owning files by id: rows a-c bind
every merchant (and heirs/successors); row d binds taxpayers; row e binds
DTE emitters (receivers "cuando corresponda"); row f binds LET populations
(GT-FIN-FR-104 gates); row g binds POs (GT-CML-FR-130/133); row h records
the absence. (iii) **Per-instrument prescription keys** (row b/c/e/g
documents): the GT-CML-FR-111..122 ladder via GT-CML-FR-124/125 and the
GT-TAX-FR-203..206 clocks via GT-TAX-FR-232 key the art.-383 gate — the
cc_fallback key stays OPEN (OQ-002). (iv) **Dated rows** (FR-074): every
value carries instrument + valid_from/valid_to + flags (R45/R60/R65); AML
pre/post-cutover resolution; GOQ-123 flag on every 66_-derived row.
(v) **Single-source discipline**: this table is the ONLY max-per-object
computation in the corpus — sibling files (taxation OQ-007; cml03 OQ-002;
fin04 pointers) cite it by id and never restate rows.

**Per-object retention state (l10n_gt_commerce.retention):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.retention | object_ref | reference | legal book · giro document · factura cambiaria · tax book/declaration · certified DTE XML/acuse · LET book record · AML record · IGSS planilla record | FR-062 |
| l10n_gt_commerce.retention | regimes | tags | cc_books_376 · cc_docs_382 · cc_factura_604 · ct_112A_prescription · dte_ad13_art21 · let_ct_anchor · aml_art34 (5y / 5y+10y digital) · igss_absence | FR-061..FR-071 |
| l10n_gt_commerce.retention | anchor_date · anchor_kind | date + select | per FR-073 (liquidation-close · issue/receipt · drawing [convention] · due-date+filing · transaction/relation end · per-instrument ladder anchors) | FR-073 |
| l10n_gt_commerce.retention | retention_until · governing_row | computed date + m2o | MAX of applicable rows; snapshot-on-write with the governing row identified | FR-062 |
| l10n_gt_commerce.retention | pending_matter_holds | o2m | art.-383.2 holds (proceeding, determination, AML case, exhibición) — each blocks the gate until terminated | FR-072 |
| l10n_gt_commerce.retention | destruction_eligibility · destruction_log | computed + o2m | eligibility computed (never auto-executed); destruction events audited with gate evidence | FR-072 |
| l10n_gt_commerce.retention_rule | class · term · unit · anchor_kind · instrument · article · valid_from/valid_to · flags | config | the §4 matrix rows + the serialized GT-CML-FR-111..122 ladder per the cml03 §4 consumption contract (R45/R60/R65 flags; GOQ-123 flag on 66_ rows) | FR-061, FR-074 |

No CSV sidecar is committed with this requirements file: the matrix rows
are few and fully specified in-table; the machine-readable serialization
(FR-074 column contract) lands as config seed rows at implementation.

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2): the matrix table and the
destruction-gate predicate are `shared` dated contract data both sides must
honor identically (a SaaS-side archive tier may never shorten any row —
D3-constrained, e-invoicing-owned); the per-object retention state, purge
guards and destruction-workflow execution on records are `odoo`. Per the
wave defaults this file introduces NO `saas` rows and no `n/a` rows: every
FR either configures shared dated data or executes record-side workflow in
the client; the only saas-adjacent surface (tax prescription-clock
evaluation, GT-TAX-FR-208) is consumed by id and not implemented here.
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-061 | shared | l10n_gt_commerce.retention_rule seed | the §4 matrix rows | Canonical table; consumed by taxation OQ-007, cml03 OQ-002, fin04 pointers by id; GOQ-124 deliverable |
| FR-062 | odoo | l10n_gt_commerce.retention | regimes, anchors, retention_until | MAX computation + snapshot-on-write; purge refusal names the governing row; applicability fed by owning FRs |
| FR-063 | shared | retention_rule row a + book registry | conservation_state tie-in | Liquidation-anchored; feeds GT-COA-FR-026's conservation_state (by id) |
| FR-064 | shared | retention_rule row b | 5-años floor + deference clause | MAX with rows d/e/g; correspondence ≠ book (R63); medium free (FR-029) |
| FR-065 | shared | retention_rule row c | 5 años art. 604, D2-70 1971-01-01 (R45) | GOQ-124 no-supersession note; anchor = drawing date as flagged convention |
| FR-066 | shared | retention_rule row d | prescription-anchored CT row | Terms via GT-TAX-FR-203/204; withholding-vocabulary guard on GT-TAX-FR-230; re-make ≤ 3 months |
| FR-067 | shared | retention_rule row e | DTE XML/acuses row | GOQ-41/OQ-005 closure named; provider-side 14-month backup excluded; GT-TAX-FR-234 SAT-authorized paper route kin |
| FR-068 | shared | retention_rule row f | LET row | FR-066 anchor + GT-FIN-FR-104/118 lifecycle gates; no LET period invented; GOQ-104 undated-print caveat |
| FR-069 | shared | retention_rule row g | AML 5y + 10y digital | Cutover rows 2026-09-17 (R60); pre-cutover 75_ art. 23 = 5y only |
| FR-070 | shared | retention_rule key rows | ladder + tax clock keys | cc_fallback OPEN (OQ-002); anchors via GT-CML-FR-124; R65 guard on the D2946 row |
| FR-071 | shared | retention_rule row h | IGSS ABSENCE | No owning FR (grep 2026-08-21); falls under rows b/d; acquisition re-opens |
| FR-072 | odoo | l10n_gt_commerce.retention | pending_matter_holds, destruction_eligibility/log | No execution while any row unexpired or any matter pending; never auto-destroy; SAT-authorization route recorded |
| FR-073 | odoo | l10n_gt_commerce.retention | anchor_date/kind per row | Per-row start-events; freeze-at-filing (D16); ladder anchors via GT-CML-FR-124 |
| FR-074 | shared | l10n_gt_commerce.retention_rule | dated columns + flags | D15/D16 on every value; cml03 §4 serialization contract; snapshot-on-write |

Version-regime notes (D12/D15/D16): the matrix is itself a dated-instrument
regime — every row resolves as-of the domain anchor date with instrument
provenance (FR-074); the AML rows are regime-cutover rows (2026-09-17,
R60); the 66_-derived rows carry the GOQ-123 verification flag; no fixed
emission or posting gates exist in this file beyond the destruction-gate
refusals (FR-062/FR-072).

## 6. Acceptance Criteria

- **AC-001:** Given any retained GT object, when its applicable regime rows
  are evaluated, then its retention-until equals the MAX of all applicable
  matrix rows (longest-per-object), the governing row is identified, and a
  premature purge is refused naming that row. (FR-061, FR-062)
- **AC-002:** Given a GT company whose enterprise liquidation has not
  completed, when destruction of its legal books is attempted, then it is
  refused by row a (liquidation-anchored, no year count), with the
  heirs/successors custody note carried. (FR-063)
- **AC-003:** Given a giro document less than five years old, or one whose
  underlying action has not prescribed, or with a pending matter, when
  destruction is attempted, then it is refused by row b plus the FR-070
  keys — and given a document also covered by the CT or AML rows, then the
  longer row governs (deference clause). (FR-064, FR-070, FR-072)
- **AC-004:** Given an issued factura cambiaria (or copy) also backing a
  tax operation, when retention is computed, then the effective floor is
  the CT prescription-anchored row (MAX), while the art.-604 5-year row
  remains on the books with the GOQ-124 no-supersession note and the
  flagged drawing-date convention anchor. (FR-065)
- **AC-005:** Given tax books/e-filings of a registered taxpayer, when
  row d is evaluated, then conservation runs while the 4-year prescription
  (8-year unregistered) has not run — restarted per GT-TAX-FR-205's
  interruption catalog — and a pending SAT determination blocks the gate as
  both an unexpired clock and a pending matter. (FR-066, FR-072)
- **AC-006:** Given a certified DTE's XML and acuses on the emitter side,
  when retention is computed, then the row runs to the CT prescription
  period (row d anchor), the certificador's 14-month backup is nowhere
  modeled as the emitter's duty, and the GOQ-41/OQ-005 reconciliation is
  recorded as resolved by this named rule. (FR-067)
- **AC-007:** Given an AML financial-PO transaction record post-cutover,
  when row g is evaluated, then retention = 5 años from transaction
  finalization plus the 10-year digital continuation (effective 15-year
  archive); and given the same class of record with a pre-cutover
  (pre-2026-09-17) anchor, then it resolves against the 75_ 5-year row
  with no digital extension. (FR-069)
- **AC-008:** Given any IGSS planilla record, when the matrix is queried,
  then NO IGSS-specific retention row exists (absence row h) and its floor
  computes only from rows b/d as applicable — no invented period is
  seeded. (FR-071)
- **AC-009:** Given any matrix value, when inspected, then it carries
  instrument, article, valid_from/valid_to and flags (R45 vigencia; R60
  AML cutover; R65 old-code guard; GOQ-123 flag on 66_-derived rows), and
  the destruction workflow has never executed while any regime row was
  unexpired or any pending matter existed. (FR-072, FR-074)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C).
This file OWNS GOQ-124 and closes it in-file (OQ-001 → resolved: the
matrix is the deliverable). GOQ-123 rides every 66_-derived citation
(kin — owned by `01_books-anchor.md` GT-COA-FR-031). GOQ-41 is kin-cited
because its reconciliation lands here (OQ-003 → resolved in-file; register
write-back to the owning waves' files is the controller's). Nothing
outside the register is treated as an open question.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-124 (owned): "Retention/destruction max-per-object matrix (synthesis deliverable): art. 383 keys destruction to 'prescripción de las acciones' but CCom enacts no general period (art. 1 → Civil); practical floor = tax corpus (CT 112'A, 4y+); factura cambiaria art. 604 5y likely superseded — write the matrix in the S-GT5 file." RESOLVED BY THIS FILE: §4 is the matrix — per-object rows a-h, MAX resolution (FR-061), destruction-gate engine (FR-072), the tax corpus as practical floor (row d via GT-TAX-FR-232), and the art.-604 row carried with the no-supersession note (row c per GOQ-124). Taxation OQ-007 (GT-TAX-FR-232's pointer) and cml03 OQ-002 resolve against this table. | no | GT synthesis wave S-GT5 (this file = the deliverable) | resolved |
| OQ-002 | Corpus boundary (kin of cml03 OQ-003 cc_fallback): the Civil-law prescription periods behind the art. 1 fallback — the values that would key destruction for non-instrument merchant documents with no tax/AML row — are EXTERNAL to this corpus (the Código Civil is not among the extracted instruments). FR-070 carries the cc_fallback key with an OPEN value; no Civil-code period (e.g. a generic civil term) is modeled, defaulted or guessed until the CC corpus lands (controller → acquisition queue). | no | Controller → acquisition queue (Código Civil); S-GT5 records the flag | open |
| OQ-003 | GOQ-41 (kin; owning file e-invoicing/05 OQ-005): "Certificador 14-month backup retention ('hasta conciliación') vs emitter-side retention duties (CT/LIBRO I) — reconcile for the Odoo archiving requirement." RESOLVED IN-FILE by FR-067's named rule: emitter-side retention of certified XML + acuses = the CT prescription period (AD 13-2018 art. 21 via GT-EINV-FR-203) anchored on GT-TAX-FR-232's prescription-anchored conservation (row d terms/clocks); the certificador's 14-month backup is provider-side and excluded from the emitter model. Register write-back to e-invoicing/05 §7 and taxation/06 is the controller's. | no | GT synthesis wave S-GT5 (closure recorded; write-back = controller) | resolved |
