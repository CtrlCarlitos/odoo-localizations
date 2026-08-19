# Evidence — 07-12 ISR tabla series + 11_Plantilla (asalariados scale vintages & computation semantics)

Sources: `hn/sources/07_Acuerdo_SAR-01-2026_G37051.pdf` (FY2026, +4.98%), `08_Acuerdo_SAR-07-2025_G36735.pdf` (FY2025, IPC 3.88%), `09_Acuerdo_SAR-07-2024_G36458.pdf` (FY2024, +5.19%), `10_Acuerdo_SAR-014-2023_ajuste_IPC.pdf` (FY2023, +9.80% — first IPC vintage), `12_Acuerdo_SAR-020-2022_tabla_ISR_2022.pdf` (FY2022, +5.32% — pre-mechanism print), `11_Plantilla_Retencion_Fuente_2026.xlsx` (SAR's own 2026 withholding calculator — formulas read with openpyxl; table pages OCR'd PSM 4 @400dpi).
Read: 2026-08-20 (W1e). All acuerdos: considerandos + tables; plantilla: all 4 sheets, formulas extracted.
Citation form: acuerdo FY + page/plantilla cell.
EVID numbering: continues (054).

---

## EVID-054 Tabla series — five FY vintages of the PN progressive scale (OCR-recovered)

- **Loc:** 07_ p.3, 08_ p.2, 09_ p.2, 10_ p.2, 12_ p.2.
- **Verbatim (Desde/Hasta per tasa):**

| FY | Exentos ≤ | 15% ≤ | 20% ≤ | 25% > | IPC factor | Acuerdo |
|----|-----------|-------|-------|-------|-----------|---------|
| 2022 | L181,274.56 | L276,411.57 | L642,817.63 | — | +5.32% | SAR-020-2022 |
| 2023 | L199,039.47 | L303,499.90 | L705,813.76 | — | +9.80% | SAR-014-2023 |
| 2024 | L209,369.62 | L319,251.54 | L742,445.49 | — | +5.19% | SAR-07-2024 |
| 2025 | L217,493.16 | L331,638.50 | L771,252.38 | — | +3.88% | SAR-07-2025 |
| 2026 | L228,324.32 | L348,154.10 | L809,660.75 | — | +4.98% | SAR-01-2026 |

  Every acuerdo: "Los Agentes de Retención deberán utilizar la tabla anterior para calcular el monto de la retención mensual" from Jan 1 of the FY.
- **Gloss:** dated rows, never overwritten (SV-CAT discipline); the plantilla's embedded table carries FULL-PRECISION values (e.g. 228,324.31904311673) proving the values = prior-year × (1+IPC), rounded 2dp only at print.
- **Candidate CRs:** `l10n_hn.isr.brackets` dated rows FY2022-2026 (+ mechanism row: annual IPC recompute); January-1 effectivity; agents-use-table mandate.
- **Topics:** taxation, payroll

## EVID-055 Plantilla — annualize→deduct→table→prorate withholding algorithm (the operative semantics)

- **Loc:** `11_` sheet "Cálculos" formulas (rows 16+, headers Instrucciones rows 9-36).
- **Verbatim (formulas):** Annual gross = Σ monthly salaries + ajuste (13th+ salaries) + **excess-over-10-SMM of 14th month (June)** `=IF(S16>$Z$3,(S16-$Z$3),0)` + **excess of 13th month (Dec)** same rule + **vacaciones excess** `=IF(W16<=30,0,(W16-30)*(R16/360))` — i.e. vacation bonus over 30 days taxable at daily = annual-salary/360 + bonuses/overtime/commissions + other income (depreciations-in-kind, dietas, fuel, school/performance bonuses, phone, housing allowance, transport). Deductions: **medical L40,000 (≤64y) / L80,000 (65+)** `IF(age<=64,40000,80000)` (Art. 13.a + D. 59-2020); **+L30,000 if age ≥60** (D. 199-2006 Ley del Adulto Mayor, col AC); **65+ with renta bruta ≤ L350,000 → L350,000 exempt deduction** (D. 194-2002 Art. 14, col AD); colegiación profesional (if practicing); **pension/previsión contributions: public (INJUPEMP/INPREUNAH/IPM) and private (RAP/AFP) annual amounts deductible** (Art. 10.h ISR + "Art. 51 del Reglamento de la Ley de ISR"); other documented deductions. Base = gross − deductions; **annual tax from the FY table**; monthly retention = annual tax ÷ retention-months (10, 11 or 12 — "el retenedor debe declarar los 12 meses para no generar omisos"). DMR sheet exports per-employee: RTN/ID, name, base ÷ months, tax ÷ months, concepto 111 "salarios" → feeds código 111 DJIMR/DMR.
- **Gloss:** THE computation contract for asalariados withholding: ANNUAL aggregation (not month-by-month cumulative), excess-only taxation of 13th/14th/vacación (360-day divisor for vacation), senior deduction stack, pension-contribution deduction (both systems), annual-table-then-prorate. Caps anchored to **10 × SMM promedio mensual = Z3 = Y3×10 where Y3 = L13,985.16** (SMM promedio, SETRASS-109-2024 vintage; workbook note: "CÁLCULO EN BASE AL SALARIO MÍNIMO 2025, SUJETO A CAMBIO CON NUEVO SALARIO MÍNIMO 2026" — i.e. the cap rides the SMM bienio, and FY2026's cap should update under SETRASS-233-2026's promedio — OQ-2).
- **Candidate CRs:** payroll-withholding engine (annualize/deduct/table/prorate); 10-SMM cap with dated SMM promedio; 360-day vacation proration; senior-deduction stack (40k/80k + 30k@60 + 350k@65) with the L350k gross-renta cliff; pension-contribution deduction lines (RAP/AFP/public); DMR (código 111) export row contract.
- **Topics:** taxation, payroll, fiscal-reporting

## EVID-056 Plantilla — cross-references that name further instruments

- **Loc:** `11_` Instrucciones col C/D.
- **Verbatim:** cites: Art. 10.h Ley ISR + **"Acuerdo STSS-308-2022"** (13th/14th-month SMM basis), SETRASS-109-2024 (SMM), **D. 199-2006** (L30k senior medical), **D. 194-2002 Art. 14** (65+ ≤L350k exempt), D. 59-2020 (L80k), **"Art. 51 del Reglamento de la Ley de ISR"** (pension deductions — an ISR REGLAMENTO exists and is cited but NOT in corpus).
- **Gloss:** acquisition leads: Reglamento de la Ley ISR (pre/re-post 17-2010 vintage unknown), Acuerdo STSS-308-2022 (14th-month SMM instrument — likely the 2022-2023 bienio companion), D. 199-2006 + D. 194-2002 (senior-benefit laws).
- **Topics:** payroll, taxation
- **Doubts/xref:** OQ-3 below.

---

## File-level OQs

- **OQ-1 (printed-value fidelity):** printed tables round to cents; workbook keeps full precision (228,324.319043...). Which does SAR validation expect on DMR upload? (Default: print-faithful 2dp rows; flag for fiscal-reporting wave.)
- **OQ-2 (FY2026 SMM cap vintage):** plantilla uses SMM promedio L13,985.16 (2024-2025 bienio) with an explicit "sujeto a cambio" note; SETRASS-233-2026 (`90_`) bienio supersedes from its effective dates → FY2026 cap must re-derive from the NEW promedio. Compute both and pin at payroll wave (needs 90_'s exact effective date + promedio).
- **OQ-3 (Reglamento Ley ISR Art. 51):** the plantilla cites an ISR reglamento for pension deductions — not in corpus, not in SAR catalog under that name (the 1990 Acuerdo 464 Art. 50 reglamento `92_`-candidate? no — that's Art. 50-specific). Acquisition lead: identify + fetch (catalog grep "reglamento" ISR yielded only Acuerdo 464-1990). Possibly superseded by D. 47-2024/107-2013 text; verify at payroll wave.
- **OQ-4 (acuerdo binding character):** the annual SAR acuerdos say agents "deberán utilizar la tabla" — the LAW's auto-adjustment (Art. 22.b) vs the acuerdo's own numbers: if an acuerdo is late/absent (e.g. 2025 gap SAR-07-2024→2025 printed Feb-2024 for FY2024 etc.), does the law auto-adjust without the acuerdo? (Practice: acuerdos always issue; encode law-mechanism + acuerdo-values as the pair.)
