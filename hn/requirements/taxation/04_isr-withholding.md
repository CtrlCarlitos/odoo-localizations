# HN — Taxation — ISR withholding: asalariados plantilla, scale vintages & resident retention engines

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-20 (V-HN1 validation fixes) |

## 1. Purpose

This file defines the functional requirements for Honduras' ISR withholding
layer (*retención en la fuente*, withholding at source). It owns: (a) the
**asalariados** (salaried workers) retention regime of clusters T3 — the PN
progressive-scale vintages FY2022-FY2026 published by annual SAR acuerdos as
DATED rows (Jan-1 effectivity, never overwritten) seeded in the
`isr_brackets.csv` sidecar, with the full-precision ×(1+IPC) mechanism (R-H10)
and the mid-January availability-gap no-default rule; the plantilla
(*Plantilla de Retención sobre Renta*, SAR's own withholding workbook, source
`11_`) computation contract — annualize → deduct → annual-table lookup →
÷months prorate — including the 13th/14th-month excess-only caps of 10 × SMM
*promedio* (average minimum wage, R-H47), the vacation >30-day rule with its
ISR-side 360-day divisor, the senior deduction stack (L40,000/L80,000 +
L30,000@60 + L350,000@65), the pension-contribution deductions (RAP/AFP and
public systems) and the composite sole-source gate (L257,493.16 FY2025 =
L40,000 + exempt band, R-H9); and (b) the **resident retention engines** of
cluster T6 — the 12.5% honorarios/dietas/comisiones retention by juridical
persons with its composite sole-source exception, the 1% compras anticipo
(monthly per-supplier aggregation, L15M retainer gate, supplier-exemption
catalog, waste-collection carve-out per R-H7, constancia, loss-year refund),
and the general retention entero anchor of 10 días calendario with
per-instrument hábil-vs-calendario semantics.

It does **not** cover: annual deduction semantics and deductibility gates —
the deductions file (file 02, HN-TAX-FR-046..078) owns
them and this file only consumes the stack inside the plantilla; the
non-resident 13-category gross-withholding table and the 4% real-estate buyer
retention — the rates/non-resident file (file 03, T5 zone); the DJIMR/DMR
**export contract** (código 111 casillas
2/43-46; códigos 112/135) — W2 cluster F2, future wave S-HN3, cross-referenced
by id only; payroll SMM/IHSS/Código del Trabajo mechanics (SMM bienios,
promedio rows, vacation pay bases) — future wave S-HN4 (`../payroll/`);
dividend 10%, cédular alquiler and ganancias de capital retention engines
(T5/T7 files); and CT sanctions/procedure (T11 file).

## 2. Legal Basis

Authority order (binding, per master evidence index): ISR = `01_` (D.L. 25
consolidation SAR-07-2025) + reform decrees `79_`; scale vintages = the
`07_-12_` acuerdos + `11_` plantilla (THE computation contract, EV07); the
D. 17-2010 family = `04_` + reglamento `21_` + interpretation `22_`;
Eficiencia = `05_` (Enero-2022 consolidation print — vintage caveat, 05_
OQ-2) with E-Arts 35/52; CT = `03_` (D. 170-2016). D-H1/D-H2/D-H3 bind all
clusters (dated rows, hecho-generador/period resolution, never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 25-1963, texto consolidado SAR-07-2025), Art. 22.b y Art. 23 | PN progressive scale: exentos L0.01–L217,493.16; 15% to L331,638.50; 20% to L771,252.38; 25% above (FY2025 vintage as consolidated); "Esta escala de tasas progresivas será ajustada automáticamente de forma anual a partir del año 2017… aplicando la variación interanual del Índice de Precios al Consumidor (IPC)… Asimismo, estos valores se ajustarán en los artículos de la presente Ley que hagan referencia a los mismos"; Art. 23 exempts the first band amount (rides the auto-adjustment) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 22 pp.16-17; Art. 23 p.21 (EV01:EVID-010) |
| LB-002 | Acuerdos SAR-020-2022 / SAR-014-2023 / SAR-07-2024 / SAR-07-2025 / SAR-01-2026 (tablas ISR) | Five FY vintages of the PN scale (Exentos ≤ / 15% ≤ / 20% ≤ / 25% >): FY2022 181,274.56 / 276,411.57 / 642,817.63 (+5.32%; V-HN1 cent-fix: exempt ceiling is 181,274.56 per EVID-054 + isr_brackets.csv — .57 is the 15%-band floor); FY2023 199,039.47 / 303,499.90 / 705,813.76 (+9.80%); FY2024 209,369.62 / 319,251.54 / 742,445.49 (+5.19%); FY2025 217,493.16 / 331,638.50 / 771,252.38 (+3.88%); FY2026 228,324.32 / 348,154.10 / 809,660.75 (+4.98%); every acuerdo: "Los Agentes de Retención deberán utilizar la tabla anterior para calcular el monto de la retención mensual" from Jan 1 of the FY; the plantilla's embedded table carries FULL-PRECISION values (e.g. 228,324.31904311673) proving values = prior-year × (1+IPC), rounded 2dp only at print (R-H10) | `hn/sources/12_Acuerdo_SAR-020-2022_tabla_ISR_2022.pdf`, `10_Acuerdo_SAR-014-2023_ajuste_IPC.pdf`, `09_Acuerdo_SAR-07-2024_G36458.pdf`, `08_Acuerdo_SAR-07-2025_G36735.pdf`, `07_Acuerdo_SAR-01-2026_G37051.pdf` | 12_ p.2; 10_ p.2; 09_ p.2; 08_ p.2; 07_ p.3 (EV07:EVID-054) |
| LB-003 | Plantilla Retención Fuente 2026 (`11_`), hoja "Cálculos" + Instrucciones | THE withholding algorithm: annual gross = Σ monthly salaries + ajuste + 14th-month excess `=IF(S16>$Z$3,(S16-$Z$3),0)` + 13th-month excess (same rule, Dec) + vacation excess `=IF(W16<=30,0,(W16-30)*(R16/360))` + bonuses/overtime/commissions + other income (in-kind, dietas, fuel, school/performance bonuses, phone, housing, transport); deductions: medical L40,000 (≤64y) / L80,000 (65+) `IF(age<=64,40000,80000)`, +L30,000 age ≥60, 65+ renta bruta ≤L350,000 → L350,000 exempt, colegiación, pension/previsión contributions (public INJUPEMP/INPREUNAH/IPM and private RAP/AFP), other documented; base = gross − deductions; annual tax from the FY table; monthly retention = annual tax ÷ retention-months (10, 11 or 12); "el retenedor debe declarar los 12 meses para no generar omisos"; caps anchored to 10 × SMM promedio = Z3 = Y3×10 where Y3 = L13,985.16 with workbook note "CÁLCULO EN BASE AL SALARIO MÍNIMO 2025, SUJETO A CAMBIO CON NUEVO SALARIO MÍNIMO 2026"; DMR sheet exports per-employee RTN/ID, name, base ÷ months, tax ÷ months, concepto 111 "salarios" | `hn/sources/11_Plantilla_Retencion_Fuente_2026.xlsx` | sheet Cálculos rows 16+; Instrucciones rows 9-36 (EV07:EVID-055) |
| LB-004 | Plantilla `11_`, Instrucciones cols C/D (cross-references) | The plantilla cites: Art. 10.h Ley ISR + "Acuerdo STSS-308-2022" (13th/14th-month SMM basis), SETRASS-109-2024 (SMM), D. 199-2006 (L30k senior medical), D. 194-2002 Art. 14 (65+ ≤L350k exempt), D. 59-2020 (L80k), "Art. 51 del Reglamento de la Ley de ISR" (pension deductions — an ISR reglamento exists and is cited but NOT in corpus; acquisition lead 07_ OQ-3) | `hn/sources/11_Plantilla_Retencion_Fuente_2026.xlsx` | Instrucciones col C/D (EV07:EVID-056) |
| LB-005 | Ley ISR, Art. 10 (rentas no gravables) | Renta bruta = total yearly income; NOT in renta bruta: f) occupational-risk indemnities and IHSS benefits; g) pension-fund investment income; h) "El valor de las prestaciones laborales, bonificación por vacaciones ordinarias de conformidad con el Código del Trabajo hasta con un pago adicional de treinta (30) días, jubilaciones, pensiones y montepíos" + contributions thereto deductible; "El décimo tercer mes en concepto de aguinaldo, así como el décimo cuarto mes de salario, hasta por el monto de diez (10) salarios mínimos promedio, en cada caso, a partir de cuyo monto serán gravables" | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 10 pp.9-10 (EV01:EVID-006) |
| LB-006 | Ley ISR, Art. 13.a | Personal deduction (residents): "La suma anual hasta de CUARENTA MIL LEMPIRAS (L.40,000.00)" education + medical "sin necesidad de presentar comprobante alguno"; ≥65 years: L80,000 (fixed lempira amounts, no IPC clause in the article; last reformed D. 59-2020 — semantics owned by the deductions file) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 13.a pp.13-14 (EV01:EVID-008) |
| LB-007 | Ley ISR, Art. 28 | Annual DJ Jan-1→Apr-30; filing exemptions: PN with gross ≤ the Art. 22.b exempt band and "los contribuyentes asalariados cuyos ingresos provengan de una única fuente de trabajo y que hayan satisfecho totalmente el pago… mediante el Sistema de Retención en la Fuente" | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 28 pp.23-24 (EV01:EVID-013) |
| LB-008 | Ley ISR, Arts. 50-51 + fn.36 | "Las personas jurídicas de derecho público y derecho privado, que efectúen pagos o constituyan créditos a favor de personas naturales o jurídicas residentes en Honduras, no exoneradas del Impuesto Sobre la Renta deberán retener y enterar al Fisco el doce punto cinco por ciento (12.5%) del monto de los pagos o créditos que efectúen por concepto de honorarios profesionales, dietas, comisiones, gratificaciones, bonificaciones y remuneraciones por servicios técnicos" — exception: payments "bajo contratos de trabajo celebrados dentro del ejercicio fiscal y cuyos honorarios como única fuente de ingresos no excedan los… L257,493.16" [fn.36: = Art. 13.a L40,000 deduction + Art. 22.b exempt band L217,493.16 — the composite, R-H9]; retentions = anticipos, enter "dentro de los primeros diez (10) días siguientes del mes"; not applicable to pagos-a-cuenta subjects; State also withholds 12.5% on servidumbre/derechos de vía payments; Art. 51: failure to retain → solidary responsibility + CT interest/multa | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 50-51 pp.30-31 (EV01:EVID-015) |
| LB-009 | Ley ISR, Art. 34 | Withholding agents: monthly DJ and enter "a más tardar dentro de los diez (10) días calendario del mes siguiente" | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 34 pp.26-27 (EV01:EVID-013) |
| LB-010 | D. 59-2020 (79_), Arts. 1-2 | Art. 1 adds to ISR Art. 13.a: "En el caso de las personas mayores de sesenta y cinco (65) años… la suma es de hasta OCHENTA MIL LEMPIRAS (L 80,000.00)"; Art. 2 reforms D. 194-2002 Art. 14: persons over 65 "con una renta bruta hasta de TRESCIENTOS CINCUENTA MIL LEMPIRAS (L. 350,000.00), quedan exentos del pago de este impuesto… sin la necesidad de presentar comprobante alguno ni someterse a procedimientos administrativos autorizantes o trámite adicional… de pleno derecho, a partir del período fiscal en que cumplan los sesenta y cinco (65) años"; excluded from the renta bruta test: intereses and ganancias de capital; wrongly-retained amounts returned per the SEFIN procedure (not in corpus — 05_ OQ-5) | `hn/sources/79_Decreto_59-2020_reforma_ISR.pdf` | D59-Arts 1-2 pp.1-2 (EV05:EVID-069) |
| LB-011 | Reglamento D. 17-2010 (Acuerdo 1121-2010), R-Arts 16-19 | 1% retention as ISR ANTICIPO on purchases of goods and services; base = purchase price minus returns/discounts/rebates; monthly accumulation per supplier allowed ("podrá acumular los montos de las compras de mes, realizadas a un mismo proveedor"); consignment goods: retention only when the purchase materializes (partial allowed); exempt suppliers: pagos-a-cuenta subjects, continuous utility supply (acueducto/alcantarillado), electric energy, fuels, financial services and insurers, artisanal products, fresh seasonal fruits/vegetables bought directly from producer, + DEI-designated others; unverifiable supplier status → retain; obligated retainers: personas jurídicas y comerciantes individuales with annual sales > L15,000,000; entero within 10 days of following month; constancia de retención issued on request — creditable in the annual ISR declaration; loss-making retained companies may request devolución/credit after fiscalización | `hn/sources/21_Acuerdo_1121-2010_Regl_D17-2010.pdf` | R-Arts 16-19 pp.4-5 (EV04:EVID-045) |
| LB-012 | D. 28-2019, Art. 1 (interpretación auténtica Art. 19 D. 17-2010) | Garbage/waste-collection services (municipal garbage, public ways, door-to-door) are NOT subject to the 1% retention — no venta elements (possessio/use/enjoyment) per the ISV law; persons dedicated to waste collection are excluded (R-H7) | `hn/sources/22_Decreto_28-2019_interp_Art19_D17-2010.pdf` | D28-Art 1 p.3 (EV04:EVID-045) |
| LB-013 | Ley de Eficiencia (D. 113-2011, consolidado Enero-2022), E-Art 35 | Retentions established by law or AT designation "deberán liquidarse en una declaración jurada y enterarse al Fisco en forma mensual, a más tardar dentro de los diez (10) días calendario del mes siguiente en el que se practicó la retención. Se exceptúa de este plazo a la Contribución Especial por Transacciones Financieras Pro Seguridad Poblacional" (exception CLOSED per R-H11: that contribución = D. 105/199-2011 made permanent by D. 31-2018 Art. 4 — EV05:EVID-071) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 35 p.16 (EV05:EVID-066; vintage caveat 05_ OQ-2) |
| LB-014 | Ley de Eficiencia, E-Art 52 | Interest/dividends on loans or capital contributions for social-investment programs between banks/regulated financials or international development organisms "no estarán sujetos a las retenciones establecidas en los numerales 5) y 7) del Artículo 5 de la Ley del Impuesto Sobre la Renta" | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 52 p.19 (EV05:EVID-066) |
| LB-015 | Código Tributario (D. 170-2016 act. D. 180-2020), Art. 32 | Agente de retención = bound by law or AT designation "atendiendo a su actividad, función o posición contractual"; "La retención se debe efectuar en el momento en que se realice el pago o devengo del tributo, lo que se realice primero" (earliest-of trigger; CT frame owned by the T11 file) | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Art. 32 p.40 (EV03:EVID-029) |

## 3. Functional Requirements

### 3.1 PN progressive-scale vintages and the bracket engine

- **HN-TAX-FR-121:** The system shall load the PN progressive annual scale
  as DATED legal data — one vintage per fiscal year with `valid_from`
  January-1 of the FY, `valid_to` December-31 (current FY open-ended) —
  seeded from the `isr_brackets.csv` sidecar transcribed exactly as printed
  in the SAR acuerdos, never overwritten (D-H2), and shall honor the
  acuerdos' mandate that "Los Agentes de Retención deberán utilizar la tabla
  anterior para calcular el monto de la retención mensual" — monthly
  retention computations select the vintage by the fiscal-year anchor of the
  period being computed. (LB-001; LB-002; EV07:EVID-054)
- **HN-TAX-FR-122:** The system shall record the vintage mechanism at full
  precision semantics per R-H10: each vintage's values = prior-year values ×
  (1 + IPC factor) with the 2-decimal rounding being PRINT-ONLY (the
  plantilla workbook carries e.g. 228,324.31904311673); the engine shall
  store the printed 2dp rows (print-faithful default, 07_ OQ-1) plus the
  per-vintage `ipc_pct` factor as metadata, and shall never re-derive,
  re-round or mid-computation "correct" published band values.
  (LB-002; EV07:EVID-054; R-H10)
- **HN-TAX-FR-123:** The system shall encode the LAW-MECHANISM + ACUERDO
  pair (07_ OQ-4): the Art. 22.b auto-adjustment clause (annual IPC
  variation, propagated to every article referencing the same values) as the
  legal mechanism, and each published acuerdo's values as the operative
  dated rows; when both exist the published acuerdo values govern the
  agents' monthly computations. (LB-001; LB-002; EV01:EVID-010;
  EV07:EVID-054)
- **HN-TAX-FR-124:** The system shall implement the availability-gap rule:
  when a fiscal year has no published acuerdo row loaded (the mid-January
  gap — acuerdos publish after the Jan-1 effectivity, e.g. SAR-07-2025
  dated 22-ene-2025 for FY2025), computations for that period shall be
  BLOCKED with an explicit missing-vintage configuration flag, and the
  system shall NEVER silently default to the prior-year table, to
  law-auto-adjusted derived values, or to any guessed amount (D-H2
  never-guess rule; OQ-001). (LB-002; EV07:EVID-054)
- **HN-TAX-FR-125:** The system shall compute ISR on any base amount by the
  marginal progressive engine over the selected vintage: 0% on the base
  fraction up to the exempt ceiling, 15% on the excess above the exempt
  ceiling up to the second ceiling, 20% on the excess above the second
  ceiling up to the third, and 25% on the excess above the third — band
  anchors carried as `over_excess_of` in the CSV/engine rows; the exempt
  band embeds the Art. 23 first-band exemption (no separate computation).
  (LB-001; LB-002; EV01:EVID-010; EV07:EVID-054)

### 3.2 The plantilla algorithm: annualize → deduct → lookup → prorate

- **HN-TAX-FR-126:** The system shall compute the asalariados retention by
  ANNUAL aggregation (not month-by-month cumulative): annual gross = Σ
  monthly salaries of the FY + the 13th/14th-month and vacation excesses
  (FR-127..129) + bonuses, overtime and commissions + other income
  including in-kind remunerations, *dietas* (per-diems), fuel,
  school/performance bonuses, phone allowance, housing allowance and
  transport. (LB-003; EV07:EVID-055)
- **HN-TAX-FR-127:** The system shall apply the 13th-month (*décimo tercer
  mes / aguinaldo*, statutory year-end bonus, December) exemption
  excess-only: exempt up to 10 × SMM promedio; ONLY the amount exceeding
  the cap enters the annual gross (`=IF(S16>$Z$3,(S16-$Z$3),0)` semantics
  — 0 when at or below the cap; never a cliff). (LB-003; LB-005;
  EV07:EVID-055; EV01:EVID-006)
- **HN-TAX-FR-128:** The system shall apply the same excess-only 10 × SMM
  promedio cap INDEPENDENTLY ("en cada caso") to the 14th-month
  (*décimo cuarto mes*) salary paid in June. (LB-003; LB-005;
  EV07:EVID-055; EV01:EVID-006)
- **HN-TAX-FR-129:** The system shall compute the vacation rule: the
  ordinary vacation *bonificación* (vacation bonus) is exempt up to a
  payment additional of 30 days; the excess over 30 days is taxable valued
  at daily rate = annual salary ÷ 360 (`=IF(W16<=30,0,(W16-30)*(R16/360))`);
  the 360-day divisor is an ISR-side rule of the plantilla and shall NEVER
  be applied as a Código del Trabajo rule (the CT contains no 360-day
  divisor — regimes kept separate; payroll mechanics = S-HN4 `../payroll/`).
  (LB-003; LB-005; EV07:EVID-055; EV01:EVID-006)
- **HN-TAX-FR-130:** The system shall exclude from the plantilla annual
  gross the Art. 10 non-grossable items as consumed by the plantilla —
  IHSS benefits and occupational-risk indemnities (f), pension-fund
  investment income (g), *jubilaciones, pensiones y montepíos* and the
  vacation bonus within the 30-day additional payment (h) — with the
  exclusion SEMANTICS owned by the deductions file (file 02,
  HN-TAX-FR-046..078; no re-derivation here).
  (LB-005; EV01:EVID-006)
- **HN-TAX-FR-131:** The system shall apply the senior/personal deduction
  STACK inside the plantilla: (a) L40,000 (≤64 years) or L80,000 (65+) —
  age resolved by birthday-year rule, from the FY the worker turns the
  threshold age; (b) +L30,000 when age ≥ 60 (D. 199-2006, cited by the
  plantilla — statute IN CORPUS as `95_`+`96_`, evidence pass pending,
  OQ-002; kin of file 02 OQ-008/FR-067 — the plantilla-side row follows
  the same activation-blocked status until the `95_`/`96_` evidence read);
  (c) 65+ with renta bruta ≤ L350,000 (intereses and ganancias de capital
  excluded from the test base) → the worker is exempt from ISR *de pleno
  derecho* — a CLIFF, not a cap (V-HN1 evidence fix per EVID-069: "renta
  bruta hasta de L350,000, quedan exentos del pago de este impuesto" — at
  or below the threshold the tax is L0.00 with no voucher and no
  administrative procedure; above it the normal regime applies in full, no
  partial exemption; wrongly-withheld amounts are returned per the SEFIN
  procedure); (d) *colegiación profesional* (professional
  association dues, if practicing);   (e) other documented deductions;
  deductibility semantics and gates = file 02 (HN-TAX-FR-046..078).
  (LB-003; LB-006; LB-010; EV07:EVID-055/056;
  EV01:EVID-008; EV05:EVID-069)
- **HN-TAX-FR-132:** The system shall deduct pension/previsión
  contributions — public systems (INJUPEMP/INPREUNAH/IPM) and private
  (RAP/AFP) — as ANNUAL amounts in the plantilla, per ISR Art. 10.h + "Art.
  51 del Reglamento de la Ley de ISR" (the ISR reglamento is cited by the
  plantilla but NOT in the corpus — LEAD, OQ-003; the deduction stands on
  Art. 10.h + plantilla contract). (LB-003; LB-004; LB-005;
  EV07:EVID-055/056; EV01:EVID-006)
- **HN-TAX-FR-133:** The system shall compute the annual taxable base =
  annual gross (FR-126..129) − deduction stack (FR-131..132), obtain the
  annual tax by the FR-125 marginal engine on the FR-121-selected vintage,
  and prorate: monthly retention = annual tax ÷ retention-months, with
  December as the settlement month recomputing on full-year data and
  monthly rows emitted for all 12 months of the FY (plantilla note: "el
  retenedor debe declarar los 12 meses para no generar omisos" — 12 DMR
  rows even when retention is zero); the exact divisor convention
  (elapsed-months 10/11/12 per the plantilla examples vs months-served for
  mid-year hires) is carried as OQ-004. (LB-003; EV07:EVID-055)
- **HN-TAX-FR-134:** The system shall source the 13th/14th-month cap input
  — 10 × SMM promedio mensual — as IMPORTED DATED DATA owned by the
  payroll wave (P1, S-HN4 `../payroll/`): the promedio is printed ONLY in
  the DGS companion tables (R-H47: single national value, methodology
  unpublished, ≠ table mean — 2026 promedio L14,917.20 → cap L149,172.00;
  FY2022-2025 and FY2027 promedios NOT in corpus = DGS-print leads); the
  system shall NEVER recompute the promedio from the bienio tables and
  shall treat a missing promedio vintage as a configuration gap, never a
  derived value. (LB-003; LB-004; LB-005; EV07:EVID-055/056; R-H47;
  EV82:EVID-228)
- **HN-TAX-FR-135:** The system shall compute the composite sole-source
  gate as DATED CONFIG per R-H9: gate = Art. 13.a L40,000 (fixed, no IPC
  clause) + the Art. 22.b exempt band of the FY (IPC-indexed, rides the
  scale vintages) — FY2025: 40,000 + 217,493.16 = L257,493.16; FY2026 ≈
  40,000 + 228,324.32 = L268,324.32 computed but NOT pinned by any SAR
  print (01_ OQ-6 — dated config, OQ-005); the gate shall always be
  computed from current-year components, never hardcoded.
  (LB-008; EV01:EVID-015 fn.36; R-H9)
- **HN-TAX-FR-136:** The system shall flag the Art. 28 filing exemption
  for asalariados whose income comes from a SINGLE labor source
  (*única fuente de trabajo*) and whose tax was fully satisfied through the
  withholding system, and for PN with gross ≤ the Art. 22.b exempt band —
  the sole-source leg consuming the FR-135 composite gate; the flag is an
  output consumed by the annual-declaration surfaces (S-HN1 rates file /
  S-HN3 fiscal-reporting wave), which own the filing mechanics.
  (LB-007; EV01:EVID-013)

### 3.3 Resident services retention: 12.5% honorarios engine

- **HN-TAX-FR-137:** The system shall implement the 12.5% retention engine:
  personas jurídicas of public and private law that make payments or
  constitute credits to resident naturales or jurídicas not exonerated from
  ISR shall retain and enter 12.5% of the amount of payments or credits for
  *honorarios profesionales* (professional fees), *dietas*, *comisiones*,
  *gratificaciones*, *bonificaciones* and *remuneraciones por servicios
  técnicos* (technical-services remunerations). (LB-008; EV01:EVID-015)
- **HN-TAX-FR-138:** The system shall apply the sole-source exception to
  FR-137: payments under labor contracts (*contratos de trabajo*) celebrated
  within the fiscal year whose *honorarios* constitute the recipient's sole
  income source and do not exceed the FR-135 composite gate → NO 12.5%
  retention (gate rides IPC through the band leg; FY2025 L257,493.16;
  FY2026 ≈ L268,324.32 unpinned, OQ-005). (LB-008; EV01:EVID-015; R-H9)
- **HN-TAX-FR-139:** The system shall treat 12.5% retentions as
  *anticipos* (advance payments) creditable against the recipient's annual
  ISR determination — never as definitive tax — and shall NOT apply the
  retention to recipients who are pagos-a-cuenta subjects (advance
  installment filers). (LB-008; EV01:EVID-015)
- **HN-TAX-FR-140:** The system shall apply the State-side 12.5% retention
  to payments for *servidumbre* (easements) and *derechos de vía*
  (right-of-way) made by State institutions. (LB-008; EV01:EVID-015)
- **HN-TAX-FR-141:** The system shall enter 12.5% retentions within the
  first 10 días calendario of the following month and shall record (flag,
  informational) that failure to retain or enter creates solidary
  responsibility plus CT interest/multa per Art. 51 — sanction collection
  itself owned by the CT/T11 file. (LB-008; LB-009; EV01:EVID-015/013)

### 3.4 Purchases anticipo: the 1% retention engine

- **HN-TAX-FR-142:** The system shall implement the 1% ISR *anticipo*
  (advance-credit) retention on purchases of goods and services: base =
  purchase price minus returns, discounts and rebatas; retained amounts are
  advance credits against the supplier's annual ISR. (LB-011;
  EV04:EVID-045)
- **HN-TAX-FR-143:** The system shall support monthly per-supplier
  aggregation: the retainer may accumulate the month's purchases from the
  same supplier and retain 1% on the accumulated base; for consignment
  goods the retention arises only when the purchase materializes (partial
  materialization → partial retention). (LB-011; EV04:EVID-045)
- **HN-TAX-FR-144:** The system shall gate the 1%-retainer obligation on
  annual sales > L15,000,000: personas jurídicas and comerciantes
  individuales above the gate are obligated retainers; at or below → no
  1%-retention duty. (LB-011; EV04:EVID-045)
- **HN-TAX-FR-145:** The system shall carry the supplier-exemption catalog:
  NO 1% retention on purchases from (a) pagos-a-cuenta subjects; (b)
  continuous utility supply — acueducto/alcantarillado (water/sewer); (c)
  electric energy; (d) fuels; (e) financial services and insurers; (f)
  artisanal products; (g) fresh seasonal fruits/vegetables bought directly
  from the producer; (h) DEI-designated others (dated catalog rows); and
  when the supplier's status cannot be verified the system shall RETAIN
  (default-to-retain rule). (LB-011; EV04:EVID-045)
- **HN-TAX-FR-146:** The system shall exclude waste-collection services
  from the 1% retention per the authentic interpretation of D. 28-2019
  (R-H7): garbage/waste-collection services (municipal garbage, public
  ways, door-to-door) are NOT subject — no *venta* elements — and persons
  dedicated to waste collection are excluded suppliers.
  (LB-012; EV04:EVID-045; R-H7)
- **HN-TAX-FR-147:** The system shall issue the *constancia de retención*
  (retention certificate) for 1% (and 12.5%) retentions on supplier/recipient
  request, recording retained amounts creditable in the annual ISR
  declaration of the retained party. (LB-011; EV04:EVID-045)
- **HN-TAX-FR-148:** The system shall support the loss-year refund workflow
  pointer: retained companies in loss-making fiscal years may request
  devolución or credit of retained amounts after fiscalización (procedure
  = CT/T11 refunds surface; here only the retained-balance ledger and the
  request flag). (LB-011; EV04:EVID-045)

### 3.5 General timing/entero anchors and declaration interfaces

- **HN-TAX-FR-149:** The system shall effect every retention of this file
  at the moment of payment or *devengo* (accrual) of the underlying
  obligation, whichever occurs first (CT Art. 32.2 earliest-of trigger —
  CT frame consumed from the T11 file by cross-reference, no re-derivation).
  (LB-015; EV03:EVID-029)
- **HN-TAX-FR-150:** The system shall anchor every retention liquidation
  and entero of this file to the general rule: monthly declaración jurada
  and deposit at the latest within the first 10 días CALENDARIO of the
  month following the month in which the retention was practiced (ISR
  Arts. 34/26 + Eficiencia E-Art 35); the E-Art 35 sole exception — the
  Contribución Especial por Transacciones Financieras Pro Seguridad
  Poblacional — is CLOSED per R-H11 (D. 105/199-2011 permanent, D. 31-2018
  Art. 4) and outside ISR scope: recorded as a never-implement note, no ISR
  engine derives from it. (LB-009; LB-013; EV01:EVID-013; EV05:EVID-066;
  R-H11)
- **HN-TAX-FR-151:** The system shall encode due-day semantics PER
  INSTRUMENT as dated configuration — días calendario unless the instrument
  says hábiles (04_ OQ-3 discipline): all engines of this file (111/112/135
  enteros) = días calendario; instruments elsewhere in the corpus that
  deviate (e.g. selectivo cigarettes días hábiles, air tickets 15 días
  calendario) are owned by their own files and never silently normalized
  to this anchor. (LB-013; LB-009; EV05:EVID-066; EV04:04_ OQ-3)
- **HN-TAX-FR-152:** The system shall exempt from ISR Art. 5 numeral-5/7
  retentions the interest and dividends on loans or capital contributions
  for social-investment programs between banks/regulated financials or
  international development organisms (Eficiencia E-Art 52 flag on the
  payer/recipient pair; the Art. 5 rate table itself = file 03).
  (LB-014; EV05:EVID-066)
- **HN-TAX-FR-153:** The system shall produce, per retention month, the
  machine-readable retention records this file's engines owe the
  fiscal-reporting layer: (a) código 111 rows per employee — RTN/ID, name,
  monthly base (annual base ÷ months), monthly tax (annual tax ÷ months),
  concepto "salarios"; (b) código 112 rows per 12.5%-retained payment; (c)
  código 135 rows per 1%-retained supplier aggregate; the DJIMR/DMR EXPORT
  contract (casillas, validation, filing chassis) is owned by S-HN3 (W2
  cluster F2) and consumed by id — this file owns only the data shape of
  the records. (LB-003; LB-008; LB-011; EV07:EVID-055; EV31:EVID-113/115/
  119)

## 4. Data Model

Machine-readable sidecar next to this file: `isr_brackets.csv` — the PN
progressive-scale vintages FY2022-FY2026 (one row per band per vintage,
`valid_from` = Jan-1 of the FY, `valid_to` = Dec-31 except the current FY
which is open-ended). CSV discipline: comma-separated, header row, LF
endings; amounts as printed (2dp, print-faithful per R-H10/07_ OQ-1);
empty `to_amount` = open-ended (25% band); `over_excess_of` = the prior
band's ceiling (marginal anchor); `fixed_quota` EMPTY — the HN scale prints
band ceilings only, and cumulative quotas are NOT printed (the engine
derives them arithmetically; never store derived values as legal data);
`ipc_pct` column = the vintage's ×(1+IPC) factor as printed in each
acuerdo (mechanism metadata per R-H10); `scope` = pn_annual_progressive.
The printed tables give upper bounds only ("Exentos ≤ / 15% ≤ / 20% ≤ /
25% >"); the `.01` lower bounds follow the SV CSV interval convention and
are encoding, not legal text. Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Scale vintages and dated parameters:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.bracket (new) | vintage, valid_from, valid_to, tramo, from_amount, to_amount, rate_pct, over_excess_of, ipc_pct, scope | char/date/monetary | vintages sar_020_2022 … sar_01_2026; seeded from `isr_brackets.csv`; never overwritten (D-H2); snapshot-on-write of resolved band values onto computations (D15) | FR-121..FR-125 |
| l10n_hn.isr.parameter (new) | parameter, value, valid_from, valid_to, note | monetary/date | sole_source_gate_composite (derived per FY from L40,000 + band — never stored as hardcoded law); supplier_exemption designations (DEI-designated rows, dated) | FR-135, FR-138, FR-145 |
| l10n_hn.smm.promedio (payroll-owned P1 feed) | valid_from, valid_to, promedio_amount, source_print | date/monetary/char | IMPORTED read-only: 2026 = L14,917.20 (DGS print, R-H47); cap = 10 × promedio computed, never a stored law value; missing vintages = config gap | FR-127, FR-128, FR-134 |

**Plantilla engine (payslip-side):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip | isr_annual_gross, isr_13m_excess, isr_14m_excess, isr_vacation_excess, isr_annual_base, isr_annual_tax, isr_retention_months, isr_monthly_retention | monetary (computed) | annualize → deduct → lookup → prorate trace; 12 rows per FY even when zero | FR-126..FR-133 |
| hr.payslip | isr_deduction_medical_40k_80k, isr_deduction_senior_30k, isr_deduction_exempt_350k, isr_deduction_colegiacion, isr_deduction_pension_public, isr_deduction_pension_private | monetary (computed) | deduction-stack trace; age gates resolved by birthday-year (D-H2 payroll resolution key) | FR-131, FR-132 |
| hr.employee | birthday (age gates), isr_sole_source_employer | date/boolean | drives 60/65 tiers and the single-source filing-exemption flag | FR-131, FR-136 |

**Retention engines (AP-side):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner | isr_retention_agent_125, isr_retention_agent_1pct, isr_annual_sales_band, isr_supplier_exemption, isr_waste_collector | boolean/monetary/select | 12.5% agency = PJ/public entities; 1% agency gate annual sales > L15M; exemption catalog values: pagos_a_cuenta · utility_water_sewer · electric_energy · fuels · financial_insurer · artisanal · fresh_produce_direct · dei_designated · waste_collector | FR-137, FR-144..FR-146 |
| account.move.line / account.payment | isr_retention_rule, isr_retention_base, isr_retention_amount, isr_retention_character | select/monetary | rule: services_12_5 · compras_1pct; character: anticipo (both engines — never definitive); base net of returns/discounts/rebates (1%) | FR-137..FR-143 |
| l10n_hn.isr.retention.constancia (new) | retention_id, retained_partner, period, amount, issued_on_request | m2o/date/monetary | constancia issuance ledger (12.5% + 1%) | FR-147 |
| l10n_hn.isr.retention.record (new) | código, period, per-line payload | select/json | 111 (per-employee monthly), 112 (per-payment), 135 (per-supplier aggregate); export contract = S-HN3 | FR-153 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client. No SaaS rows are introduced: none of these FRs touch
the thin-client/SaaS architecture split (HN SEE/electronic-invoicing
channel is blocked on unpublished technical docs — W3 E8 lead 1 — and no
DTE-like surface exists for retentions in the corpus). Model names stable
across Odoo 17/18/19/20; version-specific behavior recorded per row where
a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-121 | odoo | l10n_hn.isr.bracket + ir.sequence-free config | dated rows | Version regime (D12): vintages FY2022-FY2026, each valid_from Jan-1; D15/D16: dated rows + snapshot-on-write of resolved values onto payslips/moves; CSV seeding; current FY open-ended |
| FR-122 | odoo | l10n_hn.isr.bracket | ipc_pct metadata | R-H10 full-precision mechanism; print-faithful 2dp storage (07_ OQ-1 default); never re-round published values |
| FR-123 | odoo | l10n_hn.isr.parameter | law mechanism + acuerdo pair | Art. 22.b IPC clause recorded as mechanism metadata; acuerdo rows operative when present (07_ OQ-4 encoding) |
| FR-124 | odoo | l10n_hn.isr.bracket lookup | missing-vintage block | D-H2: no fallback, no auto-derive; explicit config-gap flag surfaced on January runs pre-acuerdo (OQ-001) |
| FR-125 | odoo | account.tax (computation type) + python compute | marginal engine | 0/15/20/25 over over_excess_of anchors; reusable for any base (payroll annual + PN annual declaration surfaces by id) |
| FR-126..FR-133 | odoo | hr.payslip × hr.salary.rule (ISR retention) + l10n_hn.isr.bracket | plantilla compute | Annualize→deduct→lookup→prorate; hr.salary.rule categories for 13th/14th/vacation excess tagging; December settle run; 12 monthly rows; divisor convention OQ-004; retro payroll uses original-period vintages (D16) |
| FR-127, FR-128, FR-134 | odoo | hr.payslip cap fields + l10n_hn.smm.promedio (P1 import) | 10×SMM-promedio caps | R-H47: promedio DGS-print-only, never recomputed (2026 cap L149,172.00); missing promedio vintages = config gap (FY2022-2025, 2027 = DGS-print leads, P1 owns rows) |
| FR-131 | odoo | hr.employee age gates + payslip deduction lines | senior stack | Birthday-year resolution (D-H2 payroll key); L30k@60 leg carries D. 199-2006 LEAD flag (OQ-002); L350k test excludes intereses/GC |
| FR-135, FR-136 | odoo | l10n_hn.isr.parameter | composite gate | R-H9: computed per FY = L40,000 fixed + band (IPC); FY2026 ≈ L268,324.32 unpinned (01_ OQ-6, OQ-005); filing-exemption flag output for S-HN3 |
| FR-137..FR-141 | odoo | res.partner flags + account.payment/account.move.line retention + account.tax (12.5%) | services engine | Retention at payment/credit; anticipo character; sole-source gate consumes FR-135; State-side servidumbre flow; solidary-responsibility informational flag |
| FR-142..FR-148 | odoo | account.move.line (purchase-side) + res.partner exemption flags + l10n_hn.isr.retention.constancia | compras engine | Monthly per-supplier aggregation job; L15M gate on company sales; default-to-retain on unverifiable status; waste-collector exclusion (R-H7); loss-year refund ledger pointer |
| FR-149 | odoo | retention stamper on payment/devengo | earliest-of | CT Art. 32.2 consumed from T11 file by crossref |
| FR-150, FR-151 | odoo | l10n_hn.fiscal.calendar config | due-day rows | 10 días calendario anchor (E-Art 35 + Art. 34); per-instrument hábil/calendario select (04_ OQ-3); R-H11 closed-exception note |
| FR-152 | odoo | res.partner exemption pair flag | E-Art 52 | Social-program interest/dividend exemption flag; Art. 5 table = file 03 |
| FR-153 | odoo | l10n_hn.isr.retention.record | payload rows | Código 111/112/135 data shape; DJIMR export chassis owned by S-HN3 (W2 F2, EV31:EVID-111/113/115/119) — consumed by id |

Version-regime notes (D12): FR-121 records the acuerdo chain SAR-020-2022 →
SAR-01-2026 with per-FY dated rows and Jan-1 effectivity; no adaptation
windows exist in the instruments (annual cycle). FR-127/128/134 record the
promedio feed dependency (payroll bienio cycle — mid-year SMM changes can
straddle an FY; promedio rows resolve by their own valid_from/valid_to,
P1-owned). FR-135 records the composite-gate IPC ride (band leg only).

## 6. Acceptance Criteria

- **AC-001:** Given a payslip month of January 2026, then the bracket
  lookup selects the sar_01_2026 vintage (exentos ≤ 228,324.32 / 15% ≤
  348,154.10 / 20% ≤ 809,660.75); given January 2025, then sar_07_2025
  (217,493.16 / 331,638.50 / 771,252.38) (FR-121).
- **AC-002:** Given an annual base of L500,000.00 under the FY2026
  vintage, then the annual tax = 15% × (348,154.10 − 228,324.32) + 20% ×
  (500,000.00 − 348,154.10) = 17,974.47 + 30,369.18 = L48,343.65, and the
  monthly retention at 12 months = L4,028.64 (FR-125, FR-133).
- **AC-003:** Given the FY2026 exentos ceiling 228,324.32, then the row
  stores the printed 2dp value with ipc_pct 4.98 and the engine performs no
  re-rounding of the ×(1+IPC) mechanism (workbook full precision
  228,324.319043… is provenance metadata, not a stored row) (FR-122).
- **AC-004:** Given a 14th-month payment of L180,000.00 in June 2026 with
  the promedio feed at L14,917.20 (cap L149,172.00), then the excess
  entering annual gross = L30,828.00; given a 13th-month payment of
  L120,000.00 in December, then L0.00 enters (independent caps, "en cada
  caso") (FR-127, FR-128, FR-134).
- **AC-005:** Given a vacation bonus of 45 days with annual salary
  L360,000.00, then daily = 360,000 ÷ 360 = L1,000.00 and the taxable
  excess = (45 − 30) × 1,000 = L15,000.00; the 360 divisor never appears in
  any CT-side (labor prestaciones) computation (FR-129).
- **AC-006:** Given a worker aged 67 with renta bruta L300,000.00, then
  the L350,000 exemption applies as a cliff (base → L0, retention L0 —
  intereses/GC excluded from the test); given age 67 and renta bruta
  L400,000.00, then the normal regime applies in full (deduction L80,000,
  no partial L350k exemption); given age 62 (with the L30,000 senior row
  ACTIVATED — file 02 OQ-008/FR-067; while activation-blocked the stack is
  L40,000 only), then L40,000 + L30,000 = L70,000 (FR-131).
- **AC-007:** Given a single-source salaried worker with FY2025 gross
  L250,000.00 fully retained, then the filing-exemption flag is set
  (250,000 ≤ composite 257,493.16); given L260,000.00, then the flag is not
  set (FR-135, FR-136).
- **AC-008:** Given a PJ paying L100,000.00 honorarios to a resident
  professional with multiple clients, then L12,500.00 is retained as an
  anticipo creditable at the annual DJ; given an otherwise-identical
  payment under a labor contract that is the recipient's sole source
  totaling L250,000.00 for FY2025, then no retention (gate L257,493.16)
  (FR-137..FR-139).
- **AC-009:** Given a retainer with annual sales L20M purchasing from
  supplier X three invoices in one month (L20,000 + L20,000 + L10,000,
  after discounts), then the 1% retention = 1% × L50,000 = L500.00 on the
  monthly per-supplier aggregate; given the same buyer with annual sales
  L14M, then no 1%-retention duty arises (FR-142..FR-144).
- **AC-010:** Given invoices from the electric utility, a waste-collection
  service provider (R-H7), and a supplier whose status flag is unset, then
  no retention on the first two and 1% retained on the third
  (default-to-retain) (FR-145, FR-146).
- **AC-011:** Given retentions practiced in January 2026, then the entero
  deadline = 2026-02-10 (first 10 días calendario of the following month);
  the per-instrument due-day config shows calendario for códigos
  111/112/135 (FR-150, FR-151).
- **AC-012:** Given a January 2027 payroll run with no SAR-2027 acuerdo
  row loaded, then the computation is blocked with a missing-vintage flag —
  never the 2026 table, never an auto-IPC-derived table (FR-124).
- **AC-013:** Given an FY2025 13th-month computation, then the cap input
  is a configuration gap (2025 promedio not in corpus — never the table
  mean, never the 2024-2025 bienio arithmetic mean) and the payslip is
  flagged rather than computed with a derived value (FR-134).
- **AC-014:** Given a payment and an earlier accrual book for the same
  honorarios obligation, then the retention stamps at the earliest of the
  two (FR-149).
- **AC-015:** Given a social-program loan between two regulated banks, then
  no ISR Art. 5 numeral-5/7 retention is applied (E-Art 52 flag)
  (FR-152).
- **AC-016:** Given a December settlement with full-year data changing the
  annual base, then December recomputes annual tax and the December row =
  annual tax − retentions Jan..Nov, with 12 monthly rows emitted for the
  DMR feed even when months retained zero (FR-133, FR-153).
- **AC-017:** Given 12.5% retentions practiced in March 2026, then the
  entero deadline = 2026-04-10 and the exposure record flags solidary
  responsibility + CT interest/multa for failure to retain or enter
  (FR-141).
- **AC-018:** Given a 1%-retained supplier requesting a constancia for
  January 2026, then the constancia issues with the retained amount
  creditable in that supplier's annual ISR declaration (FR-147).
- **AC-019:** Given a supplier in a verified loss-making FY with retained
  1% balances, then the retained-balance ledger exposes the
  devolución-or-credit request flag routed to the CT/T11 refunds surface
  (no automatic refund) (FR-148).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Annual-table availability gap (07_ OQ-4 residual): acuerdos take effect Jan-1 but publish mid-January (SAR-07-2025 = 22-ene-2025 for FY2025). FR-124 blocks with a config flag (never-guess). Confirm SAR practice for January runs made before the acuerdo publishes (prior-table provisionally? retro-recompute?) before enabling January payroll without manual config. | no | Takumi S-HN1 + controller | open |
| OQ-002 | D. 199-2006 (+L30,000 @ age ≥60 senior medical tier) and Acuerdo STSS-308-2022 (13th/14th-month SMM instrument) are cited by the plantilla (`11_`, EVID-056) — V-HN1 status fix: BOTH now in corpus (D. 199-2006 = `95_` + reforma `96_`, evidence pass pending; Acuerdo STSS-308-2022 = `101_`, evidenced EVID-230..232 in the payroll wave); the L30k tier stays activation-blocked until the `95_`/`96_` read (kin file 02 OQ-008) and the SMM-basis citation is encoded in payroll/01. | no | acquisition queue | open |
| OQ-003 | "Art. 51 del Reglamento de la Ley de ISR" (pension-contribution deduction; modern reglamento = "Acuerdo N°799" per 13_ OQ-2/67_ OQ-3) not in corpus — LEAD; FR-132 stands on Art. 10.h + plantilla. | no | acquisition queue | open |
| OQ-004 | Retention-months divisor convention: plantilla prints "10, 11 or 12" with a declare-12-months note — elapsed-months recomputation (Oct/Nov/Dec runs) vs months-served for mid-year hires. FR-133 implements prorate with the divisor exposed; verify vs the live plantilla/DMR omisos behavior before freezing. (01_ OQ-1 residual after its EVID-055 resolution.) | no | Takumi S-HN1 + payroll wave | open |
| OQ-005 | FY2026 composite sole-source gate (01_ OQ-6, R-H9): 40,000 + 228,324.32 = L268,324.32 computed, no SAR print yet — dated config, recompute-from-components enforced (FR-135); pin when SAR/Ayuda prints the value. | no | Takumi S-HN1 | open |
| OQ-006 | 07_ OQ-1 carried: printed 2dp vs workbook full precision for DMR-upload validation — default print-faithful 2dp rows (FR-122); the DMR validation surface is S-HN3's, re-verify there. | no | Takumi S-HN3 | open |
| OQ-007 | 07_ OQ-2 → RESOLVED at synthesis for FY2026 via R-H47/EVID-228: promedio = L14,917.20 (DGS companion print) → cap L149,172.00 — never recompute (≠ table mean L15,097.85). Residual open: FY2022-FY2025 and FY2027 promedios not in corpus (DGS-print leads 90_ OQ-4 / 91_ OQ-1) — P1 owns the promedio rows; missing vintages stay config gaps (AC-013). | no | Takumi S-HN4 (P1) | resolved (FY2026) / open (missing vintages) |
| OQ-008 | 04_ OQ-3 carried: per-instrument due-day semantics (hábil vs calendario) = dated config (FR-151); this file's engines are all calendario — no local resolution needed; the config family is owned by the fiscal-calendar FRs (S-HN3). | no | Takumi S-HN3 | open (config family) |
| OQ-009 | 05_ OQ-2 caveat: E-Arts 35/52 cited from the Enero-2022 Eficiencia consolidation (reforms through D. 7-2017 + 2021 sentencia annotations; post-2017 unverified). The 10-días-calendario anchor is triple-anchored (ISR Art. 34/26 + E-Art 35) so the risk is low; re-verify if any post-2022 Eficiencia reform surfaces. | no | Takumi S-HN1 | open (verify) |
| OQ-010 | Register resolutions carried: `01_ OQ-1` (monthly asalariados mechanics) and `01_ OQ-4` (13th/14th excess semantics) → RESOLVED by EV07:EVID-055 (plantilla formulas prove annualize→deduct→table→prorate and excess-only caps `=IF(S16>$Z$3,(S16-$Z$3),0)`); `01_ OQ-5` (L40k/L80k vintage) → RESOLVED by EVID-055 + Cuadro 2 (fixed amounts, no IPC clause post-D.59-2020; composite gate rides IPC only through the band leg — encoded in FR-135). No further action. | no | — | resolved |
