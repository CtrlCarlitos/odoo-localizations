# SV — Fiscal reporting — F-07 fuel & dated-regime annexes 13-17: tasas diferenciadas, precios máximos & informativos

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the five special-regime
annexes of the F-07 annex upload manual (*Manual de Usuario para Carga de
Archivo de los Anexos*, F-07 V14, ENERO 2025 §XX-§XXIV), all of them D12
DATED regimes: **Anexo 13** (*tasas diferenciadas* — differentiated IVA
rates on fuel, Decreto 321, enabled from the Mar-2022 tax period): a
MANUAL-ENTRY grid of global, IVA-net values by fuel grade
SUPERIOR/REGULAR/DIÉSEL — the only F-07 annex WITHOUT an upload file —
wired to casillas 586/587 (sales) and 588/589 (purchases), with
general-13%-rate fuel operations staying in annexes 1-3; **Anexo 14**
(the price-cap discount detail of the *Ley Especial Transitoria para
Fijar Precios Máximos de los Combustibles* — Transitory Special Law to
Set Maximum Fuel Prices — from Abr-2022): a credit-note-ONLY detail
(tipo 05, issued and/or received) with the A-P column model including
the *galones* (gallons) column at 11 integer + 8 decimal digits and the
*sin IVA* (without IVA) convention on price/value/discount/
IVA-of-the-discount, wired by *tipo de operación* 1 COMPRAS / 2 VENTAS
into casillas 550/551 and 552/553; **Anexos 15/16** (the Decreto No. 357
*informativo* (informational) pair over casillas 92/65, window Mayo-2022
→ *finalización de la obra* — completion of the works); **Anexo 17**
(the fuel-importers price-cap detail: informativo, CCF-only, CLOSED
window Junio-Agosto 2022, no casilla); and the **dated-regime engine**
that gates all five surfaces by regime-validity windows stored as data
with a regime-active flag derived from decree status (closed windows
never re-activate).

It does **not** cover: the declaration casillas this file feeds — 586-589
and 550-553 are owned by `01_f07-declaration.md` SV-FREP-FR-005/FR-010/
FR-011, casillas 92/65 by SV-FREP-FR-004/FR-010 (cross-referenced, never
restated); the generic annex upload engine and its format/validations/
modificatoria flow (SV-FREP-FR-028..041, inherited here by reference);
the canonical document-identifier mapping (`02_f07-annexes-sales.md`
SV-FREP-FR-042/043 — this file references it by id and never restates
it); the purchase annexes 3/5 (`03_f07-annexes-purchases.md` §3 — its
§1 records the F4→F7 hand-off of Anexo 16 to this file); the retention/
perception annexes and the anulados annex
(`04_f07-annexes-retentions-events.md` §3); the F-14 family, income
codes and informs (`06_f14-declaration.md`, `07_codes-and-informs.md`);
the filing calendar (`08_filing-calendar.md` — SOQ-08); the general-13%
fuel operations themselves (annexes 1-3 territory, files 02/03); the
differentiated RATE VALUES per fuel grade and the regime substance of
Decreto 321 / the Ley Especial Transitoria / Decreto 357 (special-regimes
and taxation wave territory — consumed here as dated configuration
data, OQ-001); and the FOVIAL/COTRANS quantity-tax interplay of casilla
525 (open pointer to the taxation/special-regimes waves — 01 §7 OQ-003
kin — NOT an FR here, see OQ-003).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 34_ (Manual de Usuario
para Carga de Archivo de los Anexos, F-07 V14, ENERO 2025) §XX-§XXIV is
the governing source for annexes 13-17; the form 39_ (F-07 v14, footer
"Actualizado al 15/08/2025") anchors the casilla wiring labels (owned by
`01_f07-declaration.md`). The plantilla workbook 36_ carries NO sheets
for annexes 13-17 (12 annex sheets + ÍNDICE only — consistent with
Anexo 13's manual-entry nature). Decree names are cited as printed in
the manual; no decree text is in the corpus and none is invented. Manual
pages are printed pages (printed page N = PDF page N+2).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-07 v14 §XX, Anexo 13 (tasas diferenciadas, captura manual): "A partir del periodo tributario de marzo 2022 y durante la vigencia del Decreto 321 ... se habilita el anexo 13 mediante el cual se deberán ingresar los valores de las ventas y compras gravadas realizadas de combustibles ... de forma manual ... valores globales y netos ... no deben incluir IVA ... de acuerdo al tipo de combustible: SUPERIOR, REGULAR y DIÉSEL"; las operaciones de combustible a la tasa general del 13% permanecen en los anexos 1/2/3 | F-07 v14 upload manual §XX, Anexo 13 (differentiated rates, manual capture): from the Mar-2022 tax period and during the validity of Decreto 321, annex 13 is enabled to enter the values of taxed fuel sales and purchases manually, as GLOBAL and NET values that must not include IVA, by fuel type SUPERIOR, REGULAR and DIÉSEL; fuel operations at the general 13% rate stay in annexes 1/2/3 | `sv/sources/34_F07_v14_manual.pdf` | §XX p.59 (EVID-178) |
| LB-002 | Manual F-07 v14 §XXI, Anexo 14 (descuento por precios máximos): detail "únicamente ... las Notas de Crédito emitidas y/o recibidas relacionadas a los descuentos por la aplicación de los precios máximos de combustibles" (Ley Especial Transitoria para Fijar Precios Máximos de los Combustibles, a partir de abril 2022); columnas A-P: TIPO DE OPERACIÓN "1 COMPRAS / 2 VENTAS"; CANTIDAD DE GALONES "Máximo 11 enteros y 8 decimales"; PRECIO POR GALÓN 2 enteros + 2 decimales sin IVA; VALOR DE LA OPERACIÓN; DESCUENTO; IVA DEL DESCUENTO (valor/descuento/IVA del descuento sin IVA) | F-07 v14 upload manual §XXI, Anexo 14 (maximum-price discount): only the credit notes issued and/or received related to fuel maximum-price discounts (Transitory Special Law to Set Maximum Fuel Prices, from April 2022); columns A-P: operation type 1 purchases / 2 sales; gallon quantity with maximum 11 integer and 8 decimal digits; price per gallon 2 integer + 2 decimal digits without IVA; operation value; discount; IVA of the discount (value/discount/IVA-of-discount without IVA) | `sv/sources/34_F07_v14_manual.pdf` | §XXI pp.59-62 (EVID-178) |
| LB-003 | Manual F-07 v14 §XXII, Anexo 15 (casilla 92, informativo): detalle de las ventas internas exentas no sujetas a proporcionalidad del Decreto No. 357, "períodos tributarios de mayo 2022 hasta la finalización de la obra" | F-07 v14 upload manual §XXII, Anexo 15 (casilla 92, informational): detail of the exempt internal sales not subject to proportionality under Decreto No. 357, for the tax periods from May 2022 until completion of the works | `sv/sources/34_F07_v14_manual.pdf` | §XXII pp.63-65 (EVID-178) |
| LB-004 | Manual F-07 v14 §XXIII, Anexo 16 (casilla 65, informativo): detalle de las compras internas exentas del Decreto 357, misma ventana "períodos tributarios de mayo 2022 hasta la finalización de la obra" | F-07 v14 upload manual §XXIII, Anexo 16 (casilla 65, informational): detail of the exempt internal purchases under Decreto 357, same window — tax periods from May 2022 until completion of the works | `sv/sources/34_F07_v14_manual.pdf` | §XXIII pp.66-68 (EVID-178) |
| LB-005 | Manual F-07 v14 §XXIV, Anexo 17 (informativo): descuento por precios máximos para importadores de combustible (solo CCF), "períodos tributarios de junio 2022 a agosto 2022" | F-07 v14 upload manual §XXIV, Anexo 17 (informational): maximum-price discount for fuel importers (CCF only), tax periods June 2022 through August 2022 | `sv/sources/34_F07_v14_manual.pdf` | §XXIV pp.69-72 (EVID-178) |
| LB-006 | Formulario F-07 v14, etiquetas de cableado (39_/EVID-179): B fila 16 "Ventas Gravadas de Combustible con tasas diferenciadas de IVA 586 (Débito Fiscal ... 587)"; B fila 21 "Devoluciones ... por precios máximos de combustibles 552− (Débito ... 553)"; B fila 12 "Ventas Internas Exentas No Sujetas a Proporcionalidad 92"; C fila 31 "Compras Gravadas de Combustible con tasas diferenciadas de IVA 588 (Crédito ... 589)"; C fila 33 "... por precios máximos de combustibles 550− (Crédito ... 551−)"; C fila 24 "Compras Internas Exentas y/o No sujetas 65" | F-07 v14 form wiring labels: casillas 586/587 (differentiated-rate fuel sales + debit), 552/553 (price-cap sales returns + debit), 92 (exempt internal sales not subject to proportionality), 588/589 (differentiated-rate fuel purchases + credit), 550/551 (price-cap purchase returns + credit), 65 (exempt and/or non-subject internal purchases) — all owned by `01_f07-declaration.md` FR-004/FR-005/FR-010/FR-011 | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179) |

## 3. Functional Requirements

### 3.1 Anexo 13 — tasas diferenciadas (manual-entry regime; casillas 586-589)

- **SV-FREP-FR-124:** The system shall enable Anexo 13 (fuel sales and
  purchases at *tasas diferenciadas* — differentiated IVA rates) as a
  DATED regime — "A partir del periodo tributario de marzo 2022 y durante
  la vigencia del Decreto 321": the annex exists only for tax periods
  from Mar-2022 while Decreto 321 (or its successor) is in force — and
  shall capture it as a MANUAL-ENTRY grid: NO upload file exists or is
  produced for Anexo 13, the only F-07 annex without a file (the generic
  export engine of SV-FREP-FR-028..041 is bypassed; the grid is entered
  and stored on the declaration object itself). (LB-001; EVID-178)
- **SV-FREP-FR-125:** The system shall capture the Anexo 13 values as
  GLOBAL aggregates (one value per direction and fuel grade, NOT
  per-document rows) NET of IVA — "valores globales y netos ... no deben
  incluir IVA" — split by direction (ventas/compras) and by fuel grade
  SUPERIOR, REGULAR and DIÉSEL; fuel operations taxed at the GENERAL 13%
  rate shall NOT enter Anexo 13 — they stay in the general annexes 1-3
  (annexes 1/2 for sales, annex 3 for purchases) per the manual's
  printed exclusion. (LB-001; EVID-178)
- **SV-FREP-FR-126:** The system shall wire the Anexo 13 grid into the
  Task 1 fuel casillas: the net venta bases total casilla 586 with its
  fiscal debit 587, and the net compra bases total casilla 588 with its
  fiscal credit 589 (casillas owned by SV-FREP-FR-005/FR-010); the
  debit/credit companions compute as the applicable differentiated rate
  of each fuel grade × that grade's net base — the rate VALUES per grade
  are not printed in the manual and are consumed as dated regime
  configuration (OQ-001) — under the two-decimal discipline of
  SV-FREP-FR-027. (LB-001; LB-006; EVID-178; EVID-179; cross-ref
  SV-FREP-FR-005/010/027)

### 3.2 Anexo 14 — descuentos por precios máximos (NC-only detail; casillas 550-553)

- **SV-FREP-FR-127:** The system shall build Anexo 14 (the detail of
  the discounts from the application of fuel *precios máximos* —
  maximum prices) as a DATED regime from Abr-2022 under the *Ley
  Especial Transitoria para Fijar Precios Máximos de los Combustibles*
  (Transitory Special Law to Set Maximum Fuel Prices), admitting ONLY
  credit notes — "únicamente ... las Notas de Crédito emitidas y/o
  recibidas relacionadas a los descuentos por la aplicación de los
  precios máximos de combustibles": every row is a tipo 05 *Nota de
  Crédito* (credit note; issued rows = ventas, received rows =
  compras), and any non-05 document row is REJECTED before export.
  (LB-002; EVID-178)
- **SV-FREP-FR-128:** The system shall emit every Anexo 14 row with the
  manual §XXI A-P column model, whose captured column families are:
  TIPO DE OPERACIÓN (1 COMPRAS / 2 VENTAS) · CANTIDAD DE GALONES
  (gallons) with "Máximo 11 enteros y 8 decimales" — an annex-specific
  EXCEPTION to the §II two-decimal amount discipline of
  SV-FREP-FR-030 · PRECIO POR GALÓN at 2 integer + 2 decimal digits, sin
  IVA · VALOR DE LA OPERACIÓN · DESCUENTO · IVA DEL DESCUENTO (the
  value, discount and IVA-of-the-discount columns all sin IVA); the
  remaining column families (identifiers, dates, counterparty data) are
  not captured verbatim in the evidence extract and are seeded at
  implementation from manual §XXI (OQ-002) — document-identifier slots,
  where the manual assigns them, follow the canonical mapping of
  SV-FREP-FR-042/043 and are never restated here. (LB-002; EVID-178;
  cross-ref SV-FREP-FR-042/043)
- **SV-FREP-FR-129:** The system shall wire Anexo 14 rows into the
  Task 1 price-cap casillas by their TIPO DE OPERACIÓN: tipo 1 COMPRAS
  rows (NCs received) feed the purchase pair 550 (devoluciones por
  precios máximos, subtracted by the casilla-100 formula) with its
  credit companion 551, and tipo 2 VENTAS rows (NCs issued) feed the
  sales pair 552 with its debit companion 553 (casillas owned by
  SV-FREP-FR-005/FR-011); the column basis follows the label match
  (descuento → 550/552; IVA del descuento → 551/553 — unprinted, OQ-002)
  and the casilla values are stored as POSITIVE magnitudes under the
  sign convention of SV-FREP-FR-019 (the printed formulas' minus signs
  perform the subtraction). (LB-002; LB-006; EVID-178; EVID-179;
  cross-ref SV-FREP-FR-005/011/019)

### 3.3 Anexos 15/16 — Decreto 357 informativos (casillas 92/65)

- **SV-FREP-FR-130:** The system shall build Anexo 15 (detail of the
  *ventas internas exentas no sujetas a proporcionalidad* — exempt
  internal sales not subject to proportionality — under Decreto No. 357)
  as a DATED-regime INFORMATIVO annex: its regime window runs from
  Mayo-2022 "hasta la finalización de la obra" (until completion of the
  works — an end consumed as dated data, semantics OQ-005), its rows
  detail the operations behind casilla 92 by the manual's own heading,
  and it computes NO débito/crédito companion of its own; rows dated
  outside the window are rejected under FR-133's gating (the casilla-92
  value itself is owned by SV-FREP-FR-004; auto-totalization basis
  unprinted — OQ-002). (LB-003; LB-006; EVID-178)
- **SV-FREP-FR-131:** The system shall build Anexo 16 (detail of the
  *compras internas exentas* — exempt internal purchases — under
  Decreto 357) as the purchase-side twin of FR-130's regime: the same
  Mayo-2022 → fin-de-obra window, rows detailing the operations behind
  casilla 65 (owned by SV-FREP-FR-010), informativo status with no
  credit companion; master-index cluster F4 lists it among the purchase
  annexes but this wave's file split assigns it to this file (the
  hand-off is recorded in `03_f07-annexes-purchases.md` §1).
  (LB-004; LB-006; EVID-178)

### 3.4 Anexo 17 — importadores (closed window, informativo)

- **SV-FREP-FR-132:** The system shall build Anexo 17 (informativo
  detail of the price-cap discounts of fuel *importadores* — importers)
  as a CLOSED-VINTAGE regime: its window is fixed at "períodos
  tributarios de junio 2022 a agosto 2022" (tax periods June 2022
  through August 2022 — CLOSED), its rows admit only CCF documents
  (tipo 03), it feeds NO casilla, and no period outside Jun-Ago 2022
  ever accepts a row. (LB-005; EVID-178)

### 3.5 Dated-regime engine (D12)

- **SV-FREP-FR-133:** The system shall gate every annex 13-17 surface
  by a regime-validity window stored as DATED DATA — annex 13: Mar-2022
  → end of Decreto 321's vigencia; annex 14: Abr-2022 → end of the Ley
  Especial Transitoria's vigencia; annexes 15/16: Mayo-2022 →
  fin-de-obra; annex 17: Jun-2022 → Ago-2022 (fixed) — with a
  regime-active flag DERIVED from the decree status: a period inside
  the window accepts rows; a period before the window start or after
  the window end rejects them and leaves the surface unavailable.
  (LB-001; LB-002; LB-003; LB-004; LB-005; EVID-178)
- **SV-FREP-FR-134:** The system shall encode Anexo 17's window as
  CLOSED — the regime-active flag is permanently false for periods
  after Ago-2022 — while the annex remains available for declarations
  of periods INSIDE the window (historical and amended filings):
  closed-vintage regimes never re-activate, and the open-ended regimes
  (13/14/15/16) close only by decree-status update, never by
  hard-coded dates. (LB-005; EVID-178)

### 3.6 Export, declaration integration and regime interplay

- **SV-FREP-FR-135:** The system shall export annexes 14-17 under the
  generic upload engine of SV-FREP-FR-028..041 (semicolon CSV, Text
  cells, ≤25-character filename, clean-replace semantics, annex number
  in the last column — 14/15/16/17 respectively), with the Anexo 14
  galones column as the printed exception to the two-decimal discipline
  (FR-128); Anexo 13 produces NO file under any condition (FR-124); the
  *declaración modificatoria* carryover of SV-FREP-FR-040 prints
  "anexos 3 al 12" only — the 13-17 carryover behavior is unprinted and
  not asserted (OQ-004). (LB-001; LB-002; LB-005; EVID-178; EVID-173;
  cross-ref SV-FREP-FR-028..041/040)
- **SV-FREP-FR-136:** The system shall expose this file's feeds as the
  §4 wiring interface into the Task 1 casilla engine — Anexo 13 →
  586/587 and 588/589 (FR-126); Anexo 14 → 550/551 and 552/553
  (FR-129); Anexos 15/16 → the informativo detail of casillas 92/65
  (owned by SV-FREP-FR-004/FR-010); Anexo 17 → no casilla — with no
  manual casilla fill anywhere (SV-FREP-FR-038); the FOVIAL/COTRANS
  quantity-tax interplay of casilla 525 stays OPEN with the
  taxation/special-regimes waves (OQ-003; 01 §7 OQ-003 kin — its
  per-gallon design decision is NOT encoded here). (LB-006; EVID-179;
  cross-ref SV-FREP-FR-004/005/010/011/038)

## 4. Data Model

No CSV sidecars live next to this file: the regime windows, row models
and wiring below are in-file §4 seed data. Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Regime window seed — l10n_sv.f07.fuel.regime (D12 dated data):**

| Annex | Instrument (as printed) | Window start | Window end | End kind | Status |
|-------|--------------------------|--------------|------------|----------|--------|
| 13 | Decreto 321 (tasas diferenciadas) | 2022-03 | null | decree vigencia (regime-active from decree status; 2026 successor status unpinned — OQ-001) | open [?] |
| 14 | Ley Especial Transitoria para Fijar Precios Máximos de los Combustibles | 2022-04 | null | decree vigencia | open [?] |
| 15 | Decreto No. 357 (ventas exentas no sujetas a proporcionalidad) | 2022-05 | fin de la obra | dated data, semantics unpinned (OQ-005) | open [?] |
| 16 | Decreto No. 357 (compras internas exentas) | 2022-05 | fin de la obra | dated data, semantics unpinned (OQ-005) | open [?] |
| 17 | precios máximos importadores | 2022-06 | 2022-08 | fixed | CLOSED (FR-134 — never re-activates) |

**Anexo 13 manual grid — l10n_sv.f07.annex13.entry (no file surface):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| declaration_id, fuel_grade, direction, base_neto | m2o/select/select/monetary(2dp) | grade: SUPERIOR · REGULAR · DIÉSEL; direction: venta → 586/587 · compra → 588/589; base_neto = global net-of-IVA aggregate | FR-124, FR-125 |
| debit_credit_computed | monetary(2dp) | grade rate × base_neto; rate values from regime configuration (not in corpus — OQ-001) | FR-126 |

**Anexo 14 row — l10n_sv.f07.annex14.row:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| declaration_id, tipo_operacion | m2o/select | 1 COMPRAS · 2 VENTAS | FR-127, FR-129 |
| tipo_documento | select | 05 NC ONLY (non-05 rejected) | FR-127 |
| galones | decimal(11,8) | "Máximo 11 enteros y 8 decimales" — exception to FR-030's 2dp | FR-128, FR-135 |
| precio_galon / valor_operacion / descuento / iva_del_descuento | decimal | precio 2+2; all sin IVA | FR-128 |
| identifier/date/counterparty columns | char/date | families seeded at implementation from manual §XXI (OQ-002); identifier slots per SV-FREP-FR-042/043 | FR-128 |
| annex_no | computed | literal 14 on every row | FR-135 |

**Anexos 15/16/17 rows — l10n_sv.f07.annex15.row / annex16.row / annex17.row:**
declaration_id · date (window-validated, FR-133) · amounts and
counterparty/identifier column families seeded at implementation from
manual §XXII-§XXIV (not captured verbatim in evidence — OQ-002);
annex17.tipo = 03 CCF only, no casilla feed (FR-132); annex_no = 15/16/17
on every row (FR-135). All three are informativo: no débito/crédito
companion fields exist.

**Wiring interface into 01 §3.1 (casillas owned by Task 1):**

| Feed | Casilla(s) | Notes |
|------|-----------|-------|
| Anexo 13 venta bases (net, by grade) | 586 + débito 587 | companions = grade rate × base (rates = regime config, OQ-001); AC-002/AC-003 |
| Anexo 13 compra bases | 588 + crédito 589 | same |
| Anexo 14 tipo 1 (compras) descuento / IVA del descuento | 550 / 551 | label-match basis (OQ-002); positive magnitude — the 100/145 formulas' minus signs subtract (01 FR-013/FR-014) |
| Anexo 14 tipo 2 (ventas) | 552 / 553 | same; the 105/150 formulas subtract (01 FR-007/FR-008) |
| Anexo 15 | 92 (informativo detail) | casilla owned by 01 FR-004; auto-total basis unprinted (OQ-002) |
| Anexo 16 | 65 (informativo detail) | casilla owned by 01 FR-010; F4→F7 hand-off per 03 §1 |
| Anexo 17 | — (no casilla) | informativo, closed window |

Integration note: the generic upload entity of 01 §4
(l10n_sv.f07.annex.upload) serves annexes 14-17 here — its annex_no
domain extends to 17; Anexo 13 never appears in it (manual grid,
FR-124).

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transformation (the only architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`). Model
names are stable across Odoo 17/18/19/20; version-specific behavior is
recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-124 | odoo | l10n_sv.f07.annex13.entry + l10n_sv.f07.fuel.regime | manual-grid enablement | D12: window Mar-2022 + Decreto 321 vigencia; NO file surface (01 upload engine bypassed); successor status for 2026 unpinned — OQ-001; AC-001 |
| FR-125 | odoo | l10n_sv.f07.annex13.entry | direction/grade/net base | Global aggregates net of IVA; 13%-rate ops excluded (files 02/03 territory); AC-002 |
| FR-126 | odoo | l10n_sv.f07.annex13.entry + l10n_sv.f07.casilla.value (01 file) | 586/587, 588/589 | Companions = grade rate × base; rate values = regime configuration (OQ-001); 2dp per 01 FR-027; AC-001/AC-003 |
| FR-127 | odoo | l10n_sv.f07.annex14.row + l10n_sv.f07.fuel.regime | NC-only gate + window | D12: Abr-2022 + Ley Especial Transitoria vigencia; tipo 05 only, issued and/or received; AC-004 |
| FR-128 | odoo | l10n_sv.f07.annex14.row | column families A-P | Galones 11+8 = printed exception to 01 FR-030; precio 2+2 sin IVA; A-P letter map seeded at implementation (OQ-002); identifier slots per canonical 02 FR-042/043; AC-005 |
| FR-129 | odoo | l10n_sv.f07.annex14.row + l10n_sv.f07.casilla.value (01 file) | 550-553 wiring | Tipo 1 → 550/551; tipo 2 → 552/553; positive-magnitude convention (01 FR-019); label-match basis — OQ-002; AC-004 |
| FR-130 | odoo | l10n_sv.f07.annex15.row + l10n_sv.f07.fuel.regime | informativo + window | Casilla 92 owned by 01 FR-004; no companion; fin-de-obra end semantics — OQ-005; AC-006 |
| FR-131 | odoo | l10n_sv.f07.annex16.row + l10n_sv.f07.fuel.regime | informativo + window | Casilla 65 owned by 01 FR-010; F4→F7 hand-off recorded in 03 §1; AC-006 |
| FR-132 | odoo | l10n_sv.f07.annex17.row + l10n_sv.f07.fuel.regime | closed window + CCF-only | No casilla feed; informativo; AC-007 |
| FR-133 | odoo | l10n_sv.f07.fuel.regime | window-gating engine | Windows as dated data; regime-active flag from decree status; AC-001/AC-006/AC-007 |
| FR-134 | odoo | l10n_sv.f07.fuel.regime | closed-vintage semantics | Anexo 17 permanently closed post-Ago-2022; historical-window filings still served; open regimes close by decree-status update only; AC-007 |
| FR-135 | odoo | l10n_sv.f07.annex.upload (01 engine) + annex14-17 rows | export inheritance | 01 FR-028..041 apply unchanged; galones 8-decimal exception; 13-17 modificatoria carryover unprinted — OQ-004; AC-008 |
| FR-136 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring | wiring interface | No manual casilla fill (01 FR-038); FOVIAL/COTRANS pointer open — OQ-003; AC-009 |

Version-regime notes (D12): this file is entirely dated-regime
territory — every surface's availability is governed by the
l10n_sv.f07.fuel.regime seed (FR-133), so a decree change re-dates the
behavior by data, not code. Anexo 13's force status for 2026 (Decreto
321 successor) and the differentiated-rate values per grade are unpinned
(OQ-001). Anexo 17 is the one fixed closed vintage (Jun-Ago 2022). The
v14 manual vintage governs the row models (a future manual revision
re-seeds them). The filing due-day windows remain F12 territory
(`08_filing-calendar.md`; SOQ-08) — no deadline behavior is encoded
here. Cross-file canonicality: SV-FREP-FR-042/043 (02) own the
identifier mapping; SV-FREP-FR-004/005/010/011 (01) own every casilla
this file feeds.

## 6. Acceptance Criteria

- **AC-001:** Given the Decreto 321 regime-active flag true with window
  start Mar-2022, when an Anexo 13 grid is saved for period 03/2022,
  then the values are accepted; for period 02/2022 the grid is
  unavailable (pre-window); and given the decree status turns inactive
  with end month E, then periods after E leave the annex unavailable
  and casillas 586-589 read 0.00 (FR-124, FR-133).
- **AC-002:** Given June sales of SUPERIOR fuel at differentiated rates
  with net base 1,000.00 and DIÉSEL purchases with net base 500.00,
  then casilla 586 = **1,000.00** and casilla 588 = **500.00**, neither
  including IVA; and given a fuel sale at the general 13% rate, then it
  produces NO Anexo 13 entry and lands in the annex 1/2 rows (casillas
  95/96) per the printed exclusion (FR-125).
- **AC-003:** Given a SUPERIOR rate configuration of 0.05, then casilla
  587 = 0.05 × 1,000.00 = **50.00** rounded to two decimals (rate
  values consumed as configuration — OQ-001) (FR-126).
- **AC-004:** Given an Anexo 14 row whose document is a CCF (03), then
  the row is rejected — only tipo 05 NC rows are admitted; given a
  received NC (tipo operación 1 COMPRAS) with descuento 100.00 and IVA
  del descuento 13.00, then casilla 550 = **100.00** and 551 =
  **13.00** (positive magnitudes; the 100/145 formulas' minus signs
  subtract); and given an issued NC (tipo 2 VENTAS) with the same
  values, then 552 = **100.00** and 553 = **13.00** (FR-127, FR-129).
- **AC-005:** Given an Anexo 14 row with galones 150.12345678 and
  precio 4.56, when the row is exported, then the galones cell reads
  exactly `150.12345678` (the 8-decimal exception) while every monetary
  cell keeps the two-decimal discipline (FR-128, FR-135).
- **AC-006:** Given a Decreto 357 exempt-internal-sale row dated
  06/2022, then the Anexo 15 row is accepted as informativo detail of
  casilla 92 with NO débito companion; given the same row dated 04/2022,
  then it is rejected (pre-window); and given an exempt purchase row
  dated 07/2023 with the obra still open, then the Anexo 16 row is
  accepted as informativo detail of casilla 65 (FR-130, FR-131,
  FR-133).
- **AC-007:** Given an Anexo 17 CCF row dated 07/2022, then it is
  accepted (informativo, no casilla); given the same row dated 09/2022
  or 05/2026, then it is rejected — the closed vintage never
  re-activates; and given a non-CCF row dated 07/2022, then it is
  rejected (FR-132, FR-134).
- **AC-008:** Given a validated Anexo 14 export, then the file follows
  the generic engine (semicolon delimiter, Text cells, filename ≤25
  characters + .CSV, last column = 14, full replace on re-upload) with
  the galones cell as the only 8-decimal exception; and no file is ever
  produced for Anexo 13 (FR-124, FR-135).
- **AC-009:** Given Anexo 13/14 feeds for a period, then casillas
  586/587/588/589 and 550-553 re-total automatically with no manual
  casilla edit (SV-FREP-FR-038), and Anexos 15/16/17 add no term to any
  SUMA formula beyond their informativo detail (FR-136).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Decreto 321 dated-regime status and rates (34_-file OQ-4 carried): (a) is Decreto 321 (or a successor) still in force for 2026 — the regime-active flag of FR-133 and the Mar-2022+ availability of Anexo 13 depend on it; (b) the differentiated IVA rate VALUES per fuel grade (SUPERIOR/REGULAR/DIÉSEL) are not in the corpus — FR-126 consumes them as dated regime configuration, and 587/589 cannot compute until seeded. Acquire Decreto 321 (and the Ley Especial Transitoria's rate/duration text) via the special-regimes wave / sources registry. | no | Takumi S3 (sources registry) + special-regimes/taxation waves | open |
| OQ-002 | Anexo 14-17 column models vs the evidence extract: manual §XXI-§XXIV names the captured families (tipo operación, galones 11+8, precio 2+2 sin IVA, valor/descuento/IVA-del-descuento; 15/16 topics + windows; 17 CCF-only) but the full A-P letter assignment of Anexo 14 and the complete column models of 15/16/17 were not captured verbatim; likewise unprinted: the exact column basis wiring 550-553 (descuento vs valor-operación; FR-129 encodes the label match) and whether 15/16 auto-total casillas 92/65 or only detail them. Seed at implementation from a §XXI-§XXIV re-read and confirm wiring against MH behavior. | no | Takumi S3 | open |
| OQ-003 | FOVIAL/COTRANS interplay (casilla 525; 31_ guide pointer): the per-gallon quantity-tax credit design decision stays OPEN with the taxation/special-regimes waves (01 §7 OQ-003 kin). This file's fuel surfaces record the pointer only — no FR encodes the interplay. | no | special-regimes/taxation waves (pointer recorded by Takumi S3) | open |
| OQ-004 | Annexes 13-17 modificatoria carryover: manual §XVII prints the carryover for "anexos 3 al 12" only — the fate of annexes 13-17 (and the Anexo 13 manual grid) in amended returns is unprinted. FR-135 does not assert it (kin to `04_f07-annexes-retentions-events.md` OQ-004 for §XIX). Confirm against MH system behavior. | no | Takumi S3 | open |
| OQ-005 | "Fin de la obra" window-end semantics for Anexos 15/16: whether the Decreto 357 window ends per-taxpayer/per-project (an obra-completion fact Odoo must store per company) or by a global decree-level end date is not elaborated in the manual extract. FR-133/FR-130 encode the end as dated data; the seed table leaves end_kind open. Confirm from Decreto 357 text (acquisition candidate; special-regimes wave kin). | no | Takumi S3 (sources registry) + special-regimes wave | open |
