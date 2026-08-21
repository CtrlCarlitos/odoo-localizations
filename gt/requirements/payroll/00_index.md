# GT — Payroll requirements index

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft (S-GT3 synthesis wave, in review) |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

This directory holds the S-GT3 (synthesis wave 3) payroll requirements: the
Código de Trabajo money rules split across four files (salary model &
protection, jornada/OT engine, vacaciones/maternidad, contracts/termination),
the salario-mínimo dated data layer with its CSV sidecar, the statutory
bonuses (bono 14 + incentivo; December aguinaldo = absence discipline per
GOQ-09), the IGSS contribution/collection cycle (rates external per GOQ-04),
the IRTRA + INTECAP flat-1% patronal charges, the payroll↔ISR/IVA interface
pointer file (incl. Planilla IVA-FEL mechanics), and the SSO/edition-provenance
hygiene layer. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Cluster | Scope | FR range | FRs | LBs | ACs | OQs |
|------|---------|-------|----------|-----|-----|-----|-----|
| [01_ct-salary-model.md](01_ct-salary-model.md) | P1 | CT salary core: pay bases, salario completo (art. 93), cadence, in-kind ≤30%, books by headcount, advances, inembargabilidad (structure-only, GOQ-73), prescription, solidarity, zero-bonus-articles negative | GT-PAY-FR-001..025 | 25 | 17 | 16 | 1 |
| [02_working-time-overtime.md](02_working-time-overtime.md) | P1 | Jornada 8/48 (45-as-48), 6/36, 7/42 + 4h test; OT ≥+50% 12h cap; excluded roles; descanso +1/6; asueto calendar; worked holiday = day + OT (no 2×, R38) | GT-PAY-FR-026..050 | 25 | 12 | 15 | 0 |
| [03_minimum-wage.md](03_minimum-wage.md) + [salario_minimo.csv](salario_minimo.csv) | P2 | Salario mínimo: CT mechanism arts. 103-115, 2026 CE1/CE2 × 3 actividades [sic]-faithful, 1995-2021 series, 2004 CC-suspension gap, 2022-2025 ABSENT (GOQ-11), 82-row CSV | GT-PAY-FR-051..075 | 25 | 17 | 15 | 7 |
| [04_statutory-bonuses.md](04_statutory-bonuses.md) | P3 | Bono 14 D-42-92 (100% ordinary-month June average, 1-15 July, proration; R30/R36); incentivo D-78-89 → D-37-2001 Q250 quoted-only (R41/R42); December aguinaldo ABSENCE-FR (GOQ-09) | GT-PAY-FR-076..100 | 25 | 14 | 14 | 2 |
| [05_vacaciones-maternidad.md](05_vacaciones-maternidad.md) | P1 | Vacaciones 15 días hábiles + 150-day gate + no-cash-out + 5-year retro + 3m/12m prepaid bases; maternidad 84d @100% (30+54, halves, adoption); inamovilidad; lactancia; nursery; menores | GT-PAY-FR-101..126 | 26 | 21 | 18 | 0 |
| [06_contracts-termination.md](06_contracts-termination.md) | P1 | Contract taxonomy + indefinite presumption + prueba; justa causa; indemnización 1 month/year UNCAPPED (6-mo salario completo base, bono 14 at 6/12, IGSS offsets, 50% rule); preaviso WORKER-side (R37); NO cesantía/doubling (R33); finiquito | GT-PAY-FR-127..152 | 26 | 15 | 17 | 0 |
| [07_igss-contributions.md](07_igss-contributions.md) | P4 | IGSS: 25/50/25 structure-only; ALL rates/base/tope external (GOQ-04); two-share delivery; base floor + NO tope (negatives); planilla electrónica lifecycle; single receipt; mora/RD/nota-de-cargo; waivers; ±1% | GT-PAY-FR-153..184 | 32 | 24 | 16 | 4 |
| [08_irtra-intecap.md](08_irtra-intecap.md) | P5 | IRTRA flat 1% totality-of-planillas (no brackets, R32; D-1528 1962, R31); INTECAP ladder → 1% (art. 9º Reglamento-1980); 20-day deadline; 2% retention; enforcement ladder; 80% rebate | GT-PAY-FR-185..206 | 22 | 17 | 12 | 8 |
| [09_isr-iva-interfaces.md](09_isr-iva-interfaces.md) | P6 | Pointer/file-of-feeds: wage-side value contracts into GT-TAX-FR-112/115/116/117/121/122/124/130..133/135..138/141/145/146/169 by exact id; Planilla IVA-FEL (SAT-1111) window/feed/last-wins; GT-EINV-FR-210 blocker; IGSS≠SAT planilla disambiguation | GT-PAY-FR-207..222 | 16 | 12 | 15 | 3 |
| [10_sso-provenance.md](10_sso-provenance.md) | P7 | SSO duties money-free (R40: comité ≥10, plan 3y, exams, CT 271-272 pointer); edition-provenance citation rules (R44/GOQ-70..72/76): CT qualifier mandatory, no "current through", art. 420/421 guard, SR boundary rows | GT-PAY-FR-223..236 | 14 | 10 | 13 | 4 |
| **Total** | | | **GT-PAY-FR-001..236** | **236** | **159** | **151** | **29** |

Cluster map (from `gt/.extractions/00_MASTER_INDEX.md` §A, wave W-GT3): P1
maps onto files 01/02/05/06 (four-part split by computation surface); P2→03,
P3→04, P4→07, P5→08, P6→09, P7→10 map one-to-one. FR numbering is
wave-sequential with no gaps or collisions (verified mechanically).

## Authority order (binding, from the master index)

Copied from `gt/.extractions/00_MASTER_INDEX.md` preamble (payroll authority
order, binding all S-GT3 files):

- CT labor LBs cite 32_ as "CT art. N (texto según edición conmemorativa
  2024, MinTrabajo)" — no "current through" date claimable (indeterminate
  cutoff); **no CT article exists for aguinaldo/bono/incentivo/propina or
  cesantía/doubling** — bonuses cite their specific decrees only.
- IGSS mechanics cite 35_ (Res. 08-SGF/2026), law level 33_ (D-295) — but
  **ALL rate/base/tope values are external (JD reglamentos, Acuerdo 1118
  family / 1421 — GOQ-04): never cite 33_-36_ for a rate**.
- Salario-mínimo rows = 37_/38_/39_ as dated data with [sic] fidelity
  (printed figures govern over formulas — R35).
- Bonuses: 40_ = bono 14 D-42-92; 41_ = incentivo D-78-89; today's Q250 =
  D-37-2001 quoted-only — **NEVER invent December aguinaldo mechanics
  (D-76-78 absent, GOQ-09)**.
- IRTRA = flat 1% D-1528 art. 12 (as reformed by D-43-92) — no brackets;
  INTECAP = 1% (D-17-72 ceiling ladder; in-force via Reglamento-1980
  art. 9º), first 20 días with IGSS planillas.

Wave-level instantiation notes: the ISR exemption/deduction/projection
values are taxation-owned and consumed by exact FR id through
`09_isr-iva-interfaces.md` (S-GT2 final-review lesson: never family-range
guesses); form identities (SAT-1111/1331/1431/1901…) cite 48_/RetWeb per
R46; SSO (AG 229-2014) is money-free (R40).

## Open-questions rollup (§7 rows per file + master-index GOQ ids)

| File | §7 OQ rows | GOQ ids carried |
|------|-----------|-----------------|
| 01_ct-salary-model.md | 1 | GOQ-73 (owned) |
| 02_working-time-overtime.md | 0 | — (2 new gaps reported, see below) |
| 03_minimum-wage.md | 7 | GOQ-77/78/79/80/81/82/11 (all owned) |
| 04_statutory-bonuses.md | 2 | GOQ-09, GOQ-83 (owned) |
| 05_vacaciones-maternidad.md | 0 | — (8 non-OQ gap notes, see below) |
| 06_contracts-termination.md | 0 | — (6 non-OQ gap notes) |
| 07_igss-contributions.md | 4 | GOQ-04/74/75 (owned) + GOQ-10 (IGSS half) |
| 08_irtra-intecap.md | 8 | GOQ-84/85/86/87/88/89/91 (owned) + GOQ-10 (INTECAP half) |
| 09_isr-iva-interfaces.md | 3 | GOQ-90 (owned) + GOQ-61/99 (kin) |
| 10_sso-provenance.md | 4 | GOQ-70/71/72/76 (owned) |
| **Total** | **29** | |

### GOQ coverage check (payroll register GOQ-70..91 + cross-cutting GOQ-04/09/10/11)

Register: `gt/.extractions/00_MASTER_INDEX.md` §C.3 (GOQ-70..91) + §C
cross-cutting table (GOQ-04/09/10/11). Every id is **consumed** in at least
one §7 OQ row — none remain unassigned; none listed not-applicable.

| GOQ | Consumed in |
|-----|-------------|
| GOQ-04 | 07 (+ 09 kin) |
| GOQ-09 | 04 |
| GOQ-10 | 07 (IGSS half: planilla fecha límite + mora tasa) + 08 (INTECAP half: 1%-ceiling acta) |
| GOQ-11 | 03 |
| GOQ-70 | 10 |
| GOQ-71 | 10 |
| GOQ-72 | 10 |
| GOQ-73 | 01 |
| GOQ-74 | 07 |
| GOQ-75 | 07 |
| GOQ-76 | 10 |
| GOQ-77 | 03 |
| GOQ-78 | 03 |
| GOQ-79 | 03 |
| GOQ-80 | 03 |
| GOQ-81 | 03 |
| GOQ-82 | 03 |
| GOQ-83 | 04 |
| GOQ-84 | 08 |
| GOQ-85 | 08 |
| GOQ-86 | 08 |
| GOQ-87 | 08 |
| GOQ-88 | 08 |
| GOQ-89 | 08 |
| GOQ-90 | 09 |
| GOQ-91 | 08 |

Kin ids referenced beyond the owned set (all pre-existing register rows,
owned by other waves): GOQ-58 (LAT post-46-2022 caveat — carried inside
taxation/04's own rows; payroll only points), GOQ-61 (47_-digest practice
flag — 09), GOQ-99 (deadline-qualifier transcription — 09), GOQ-121
(65_-criterio paraphrase limit — inline note in 04).

**New gaps reported during synthesis (NOT register GOQs — flagged to
controller, candidates for register addition):** 02's OT hourly-base divisor
(file-03 interplay) and per-locality festividad config; 05's art. 152
a)/d)/e) + art. 154 maternity-base re-extraction needs and three
corpus-silent design defaults (daily-equivalent divisor, proration fraction,
60-day window unit — each marked never-law); 07's planilla-format-spec and
CPR-88/100-text gaps (folded into GOQ-04/74 acquisition families); 09's
día-hábil calendar provenance (config-tracked, OQ-003 there).

## CSV sidecars

| File | Rows | Content |
|------|------|---------|
| [salario_minimo.csv](salario_minimo.csv) | 82 | The salario-mínimo series as dated data: 1995-2007 two-sector + 2008-2021 three-sector (39_), 2021 freeze (AG 250-2020), 2004 CC-suspension gap segments (GOQ-81), 2022-2025 ABSENT rows (GOQ-11 — never interpolated), 2026 CE1/CE2 × 3 actividades [sic]-faithful with words-govern resolutions (GOQ-77/78); header comment carries authority order + R35 |

Hand-built from the committed evidence file (SV `smm_2025.csv` pattern);
regeneration note and authority order live in the header comment.

## LB & AC totals

| File | LB rows | AC rows |
|------|---------|---------|
| 01_ct-salary-model.md | 17 | 16 |
| 02_working-time-overtime.md | 12 | 15 |
| 03_minimum-wage.md | 17 | 15 |
| 04_statutory-bonuses.md | 14 | 14 |
| 05_vacaciones-maternidad.md | 21 | 18 |
| 06_contracts-termination.md | 15 | 17 |
| 07_igss-contributions.md | 24 | 16 |
| 08_irtra-intecap.md | 17 | 12 |
| 09_isr-iva-interfaces.md | 12 | 15 |
| 10_sso-provenance.md | 10 | 13 |
| **Total** | **159** | **151** |
