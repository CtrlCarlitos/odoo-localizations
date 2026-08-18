# Evidence — 53_Tablas_Retencion_ISR_DE10_2025.pdf

Sources: `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` (MODIFICACIÓN A LAS TABLAS DE RETENCIÓN DEL ISR — DECRETO EJECUTIVO No. 10, emitido 30-IV-2025; certified copy by Secretario Jurídico de la Presidencia, same date. Deroga D.E. No. 95 del 18-XII-2015, D.O. No. 236 T. 409 del 22-XII-2015. Vigencia: 8 días después de su publicación en el D.O. — in effect from May-2025 per MH aviso).
Read: 2026-08-17 (W7). Full document (8 pp, scanned; OCR normalized spacing in table rows; [sic] marks retained where meaningful).
Citation form: literal/article + page (PDF txt page markers).
Supersession: this decree is the OPERATIVE retention-tables authority. 10_ (D.E. 75/25-1992, colones-era) is historical LB only.

## EVID-153 D.E. 10-2025 — identity, considerandos and legal basis

- **Loc:** Certification block + considerandos I-IV (p.1).
- **Verbatim:** "Que mediante Decreto Legislativo No. 293, de fecha 30 de abril de 2025, se introdujo reforma al artículo 37 de la Ley de Impuesto sobre la Renta, relacionada con la modificación de los Tramos | y II de la Tabla para el Cálculo del Impuesto de Personas Naturales, Sucesiones y Fideicomisos; mediante el cual se amplió la base exenta del referido impuesto hasta los seis mil seiscientos dólares de los Estados Unidos de América ($6,600.00) de ingresos anuales, equivalente a un ingreso mensual de hasta quinientos cincuenta dólares de los Estados Unidos de América ($550.00)." (cons. I). "Que mediante Decreto Ejecutivo No. 95, de fecha 18 de diciembre de 2015, publicado en el Diario Oficial No. 236, Tomo No. 409, del 22 de diciembre de 2015, se emitieron las Tablas de Retención del Impuesto sobre la Renta; Decreto emitido en cumplimiento a lo establecido en el artículo 65 de la Ley de Impuesto sobre la Renta" (cons. III). "Que el funcionamiento de las tablas de retención, en cumplimiento del Principio de Legalidad, se ajusta a los porcentajes y a la renta neta estipulada en el artículo 37 ... estructurándose con base a la renta neta mensual, una vez deducidos de los ingresos brutos para períodos mensuales, quincenales y semanales, las cotizaciones previsionales, remuneraciones no gravadas y las deducciones legales de seguridad social, educación y salud, reguladas en los artículos 29, numeral 7) y 33 de la referida Ley" (cons. III, continued on p.2).
- **Gloss:** tables are issued under Ley ISR Art. 65 authority; they track Art. 37 rates; the base is NET (remuneración gravada after deductions). Cross-refs D.L. 293-2025 (55_) and D.E. 95-2015 (repealed chain link).
- **Candidate CRs:** retention tables = dated legal data keyed to the operative executive decree; system must load tables by validity period (1992 colones era → 2015 era → 2025 era as separate dated rows); tables derivation follows Art. 37 of the moment.
- **Topics:** payroll, taxation.
- **Doubts/xref:** decree text is the Casa Presidencial certified copy — the D.O. issue/page that published D.E. 10 is not pinned (vigencia counts from that publication; MH aviso says effect from May-2025) → OQ-1. Chain link 1992→2015 (which decree(s) aligned tables to the D.L. 957-2011 Art. 37 table before D.E. 95-2015) not in sources → OQ-2 (historical only).

## EVID-154 D.E. 10-2025 Art. 1 a) — monthly retention table

- **Loc:** Art. 1 a) (p.2).
- **Verbatim:**

```
DESDE       HASTA         % A APLICAR  SOBRE EL EXCESO DE:  MÁS CUOTA FIJA DE:
I TRAMO     0.01          550.00       SIN RETENCIÓN
II TRAMO    550.01        895.24       10%                   550.00               17.67
III TRAMO   895.25        2,038.10     20%                   895.24               60.00
IV TRAMO    2,038.11      En adelante  30%                   2,038.10             288.57
```

- **Gloss:** monthly withholding brackets for domiciled natural persons in dependent-service remuneraciones gravadas. Structure identical to the 1992 model (fixed quota + marginal % over stated threshold).
- **Candidate CRs:** Odoo SV payroll ISR withholding bracket data (2025-05+ vintage): 4 rows, marginal-over-excess + cuota fija; stored as dated data effective from the decree's vigencia.
- **Topics:** payroll, taxation.
- **Doubts/xref:** arithmetic consistency vs Art. 37 post-293: monthly tramo II cap 895.24 = (10,742.86 − 1,600)/12 = 742.86/12? No: (10,742.86/12 = 895.238…) → 895.24 ✓; IV threshold 2,038.10 = 24,457.14/12 = 2,038.095 → 2,038.10 ✓ (see EVID-158 derivation: recálculo tables = Art. 37 shifted by +$1,600 annual deduction).

## EVID-155 D.E. 10-2025 Art. 1 b)/c) — quincenal and weekly tables

- **Loc:** Art. 1 b), c) (p.3).
- **Verbatim:** b) quincenal: 0.01–275.00 SIN RETENCIÓN; 275.01–447.62 10% s/ exceso de 275.00 + 8.83; 447.63–1,019.05 20% s/ 447.62 + 30.00; 1,019.06 en adelante 30% s/ 1,019.05 + 144.28. c) semanal: 0.01–137.50 SIN RETENCIÓN; 137.51–223.81 10% s/ 137.50 + 4.42; 223.82–509.52 20% s/ 223.81 + 15.00; 509.53 en adelante 30% s/ 509.52 + 72.14.
- **Gloss:** half-month and one-month/4.33? sub-tables. Quincenal exempt = 550/2 = 275 exact; semanal exempt = 137.50 = 550/4 exact (NOT /4.33 — the decree uses exact quarters for the exempt band).
- **Candidate CRs:** payroll frequency-dependent bracket sets as dated data (monthly/quincenal/semanal), same engine.
- **Topics:** payroll, taxation.
- **Doubts/xref:** weekly tramo IV threshold 509.53 vs monthly 2,038.11/4 = 509.5275 (rounding up at cent 3); quincenal IV 1,019.06 vs 2,038.11/2 = 1,019.055 → printed DESDE 1,019.06 [consistent round-up]; semanal III cap 509.52 = 2,038.10/4 = 509.525 → printed 509.52 (round down) — mixed rounding directions across rows; transcribe EXACTLY, no recomputation (same discipline as W6 10_ OQ-1..3) → OQ-3.

## EVID-156 D.E. 10-2025 Art. 1 d) — retention base definition

- **Loc:** Art. 1 d) (p.3).
- **Verbatim:** "Para el cálculo de la retención, deberán ser consideradas únicamente las remuneraciones gravadas en el período respectivo. Las remuneraciones gravadas a que se refiere el inciso anterior se determinarán deduciendo al total de las remuneraciones del período, las remuneraciones no gravadas, y las cotizaciones laborales a la Seguridad Social. Las cotizaciones previsionales a las Administradoras de Fondos de Pensiones e Instituciones Públicas Previsionales se encuentran comprendidas en el concepto de remuneraciones no gravadas. Las tablas de retención de los literales a), b) y c) del presente artículo no incluyen en su estructura el valor de cotización laboral de seguridad social, por lo cual, para proceder al cálculo de la retención debe disminuirse dicho valor."
- **Gloss:** the base is NET of (i) non-taxable remunerations, (ii) employee SS contributions (ISSS), (iii) pension contributions (AFP / public pension institutes). Tables do NOT embed these → system must subtract them before bracket lookup. RESOLVES the base question the 1992 decree left open (W6 10_ OQ-4) — for the current regime the answer is explicit: bruto − no gravadas − cotizaciones laborales SS/AFP.
- **Candidate CRs:** payroll ISR withholding base = gross − non-taxable − employee SS + pension contributions; ordering of deductions before table lookup.
- **Topics:** payroll, taxation.
- **Doubts/xref:** employer-side contributions are NOT part of this netting (only laborales = worker-side). xref Ley ISR Art. 3.1 viáticos (54_); Art. 29.7 / Art. 33 (deductions NOT netted here — handled by literals e)/f)).

## EVID-157 D.E. 10-2025 Art. 1 e) — $1,600 deduction not embedded (Tramo II only)

- **Loc:** Art. 1 e) (p.4).
- **Verbatim:** "Los valores consignados únicamente en el Tramo ll de las tablas de retención de los literales a), b) y c), no contienen las deducciones de un mil seiscientos dólares (US$1,600.00) establecidas en los artículo 29, numeral 7) inciso primero de la Ley de Impuesto sobre la Renta, a que tienen derecho las personas naturales asalariadas cuyo monto anual sea igual o inferior a nueve mil cien dólares (US$9,100.00); por lo tanto, para efectos de aplicar la respectiva retención deben ser consideradas en el cálculo correspondiente."
- **Gloss:** for earners ≤$9,100/yr entitled to the $1,600 fixed deduction (Ley ISR Art. 29.7), Tramo II values in the monthly/quincenal/semanal tables do NOT include it — the deduction must be applied in the calculation. (Tramos III/IV DO embed it — that is why their boundaries sit at Art. 37 + 1,600 offsets; see EVID-158.)
- **Candidate CRs:** conditional extra deduction for Tramo II taxpayers with annual ≤ $9,100: per-period proration (1,600/12, /2 for quincenal? — decree does not spell the proration → OQ-4).
- **Topics:** payroll, taxation.
- **Doubts/xref:** how to prorate the $1,600 across quincenal/semanal periods is not stated (monthly = /12 implied by the recálculo tables' +1,600 shift) → OQ-4.

## EVID-158 D.E. 10-2025 Art. 1 f) — June/December recalculation

- **Loc:** Art. 1 f) + tables 1)/2) (pp.4-5).
- **Verbatim:** June table: 0.01–3,300.00 SIN RETENCIÓN; 3,300.01–5,371.44 10% s/ 3,300.00 + 106.20; 5,371.45–12,228.60 20% s/ 5,371.44 + 360.00; 12,228.61 en adelante 30% s/ 12,228.60 + 1,731.42. December table: 0.01–6,600.00 SIN RETENCIÓN; 6,600.01–10,742.86 10% s/ 6,600.00 + 212.12; 10,742.87–24,457.14 20% s/ 10,742.86 + 720.00; 24,457.15 en adelante 30% s/ 24,457.14 + 3,462.86. Procedure: "Al total de retención resultante de la aplicación de la tabla que corresponda se le restará la sumatoria de las mismas efectuadas en los períodos mensuales anteriores, de enero a mayo para el primer recálculo y de enero a noviembre para el segundo recálculo, la diferencia positiva constituirá el valor a retener en el mes de junio o diciembre ... Si la diferencia es negativa no se retendrá valor alguno." Exclusions: "No deben considerarse para el recálculo de la retención las remuneraciones que hayan sido objeto de retención definitiva y las remuneraciones que hayan sido objeto de la retención del 10% que se regula en el artículo 1, literal h)". Employer change: "el responsable de efectuar el recálculo y la retención respectiva será el último patrono o empleador"; worker must obtain a retention constancia (CT Art. 145) from the prior employer within 15 días hábiles of retirement; for the recálculo the Tramo II $1,600 deduction applies (persons ≤$9,100/yr); persons >$9,100 apply Art. 33 deductions (medical/schooling).
- **Gloss:** semi-annual true-up (June: Jan–Jun cumulative on 6-month table; December: full-year on 12-month table), prior retentions netted, floor at zero. December table = Art. 37 annual table shifted by +$1,600 on Tramos II/III boundaries (9,142.86+1,600=10,742.86 ✓; 22,857.14+1,600=24,457.14 ✓) with the SAME cuotas fijas as Art. 37 (212.12/720.00/3,462.86) — i.e. the recálculo tables price in the $1,600 fixed deduction for ≤$9,100 earners. June table = December table halved (6,600/2=3,300 ✓; 10,742.86/2=5,371.43→printed 5,371.44 [sic, +0.01]; 24,457.14/2=12,228.57→printed 12,228.60 [sic, +0.03]; cuotas halved with rounding: 212.12/2=106.06→printed 106.20 [sic, ≠]; 720/2=360 ✓; 3,462.86/2=1,731.43→printed 1,731.42 [sic, −0.01]).
- **Candidate CRs:** payroll June/December recalculation engine: cumulative gravadas → table → minus prior retentions → max(0, diff); multi-employer/prior-employer constancia intake; Tramo II $1,600 handling in recálculo.
- **Topics:** payroll, taxation.
- **Doubts/xref:** printed June anomalies [sic] (5,371.44; 12,228.60; 106.20) deviate from exact halving — verify against the D.O. print of D.E. 10 before encoding (same class as W6 10_ OQ-1..3) → OQ-3.

## EVID-159 D.E. 10-2025 Art. 1 g) — special periods and extraordinary remunerations

- **Loc:** Art. 1 g) (p.6).
- **Verbatim:** "Se aplicará la tabla mensual, para lo cual se calculará el salario equivalente mensual mediante regla de tres simple, lo mismo para la porción del impuesto a retener mensual y por el mismo método el impuesto a retener que corresponda al período." + extraordinary remunerations (aguinaldos, vacaciones, bonificaciones, premios, gratificaciones): same method; if no period associable, treat as monthly; if computed independently → no retention, then sum with the salary and apply the monthly table; same payment date → deduct from the total; different dates → deduct from the LAST remuneration paid in the monthly period.
- **Gloss:** proportional (regla de tres) monthly-equivalence for daily/special periods; extraordinary payments join the regular salary for table application with late-payment-order deduction.
- **Candidate CRs:** proration rule for non-standard pay periods; extraordinary-payment withholding aggregation flow.
- **Topics:** payroll, taxation.
- **Doubts/xref:** xref aguinaldo exemption interplay (Ley ISR Art. 4.16 as reformed by D.L. 458-2019 — EVID-165: excess aguinaldo retention now DEDUCTS the exempt 2-SMM floor); annual transitory caps 2021–2024 ($1,100/$1,500, EVID-167).

## EVID-160 D.E. 10-2025 Art. 1 h) — multi-employer and voluntary-increase cases

- **Loc:** Art. 1 h) (pp.6-7).
- **Verbatim:** 1. Dos o más patronos: table applies to the HIGHEST-paying job; the rest bear flat 10% on sums paid/credited; if aggregate < exemption threshold → no retention; worker must inform each employer of multiple jobs and amounts (in January, or within 15 días hábiles of changes); equal rents → worker designates which gets the table; employer change in-year → prior employer issues retention constancia (CT Art. 145) within 15 días hábiles of retirement for the June/December recálculo. 2. Solicitud voluntaria: worker may request DGII (via formulario, copy to the retention agent) a HIGHER retention or inclusion of other rents in the monthly calculation.
- **Gloss:** multi-employment split mechanic (progressive table on top job + definitive-like 10% flat on others — the 10% is excluded from recalc per EVID-158); voluntary over-withholding election.
- **Candidate CRs:** employee-level multi-job configuration (designate primary employer); flat 10% secondary-job withholding; voluntary retention increase recorded via DGII form.
- **Topics:** payroll, taxation.
- **Doubts/xref:** none new.

## EVID-161 D.E. 10-2025 Arts. 1 i), 2-4 — declaration duty, online filing, repeal, vigencia

- **Loc:** Art. 1 i), Arts. 2-4 (pp.7-8).
- **Verbatim:** i) if exercise-year retentions do not match the Art. 37 liquidation, the taxpayer declares/pays per Arts. 37 & 48 or requests refund; in any case subjects with rents > $60,000 MUST file the ISR declaration. Art. 2: "Las personas naturales domiciliadas en el país, que hayan sido sujetos de retención, presentarán sus declaraciones de Impuesto sobre la Renta en línea, por medio de Internet, en el sitio web del Ministerio de Hacienda utilizando los aplicativos informáticos que para tal efecto disponga la Dirección General de Impuestos Internos." Art. 3: deroga D.E. No. 95 (18-XII-2015, D.O. 236 T.409 22-XII-2015). Art. 4: vigencia 8 días después de su publicación en el D.O. Signatures: Casa Presidencial, 30-IV-2025 (Bukele / Posada).
- **Gloss:** $60,000 mandatory-declaration threshold (consistent with Ley ISR Art. 37 regime per W6 EVID-096); withheld persons file ONLINE on MH aplicativos (system-side: no paper path); D.E. 95-2015 repealed; effective 8 days after D.O. publication → 2025-05-08 per press/D.O. dating of the containing issue (verify — OQ-1).
- **Candidate CRs:** payroll-year-end declaration reminder rule at >$60,000; system assumption: on-line filing (out of Odoo scope, informational).
- **Topics:** payroll, taxation, fiscal-reporting (informational).
- **Doubts/xref:** D.E. 10's own D.O. publication reference not stated in the certified copy → OQ-1.

## Open questions (53_Tablas_Retencion_ISR_DE10_2025)

- OQ-1: D.O. publication of D.E. 10: the certified copy (30-IV-2025) does not cite its D.O. issue/number; vigencia runs 8 days after publication (MH aviso: effect from May-2025; press ties the containing D.O. to 30-IV-2025 → effective 2025-05-08 assumed). Pin the D.O. number/pages for the registry (scan May-2025 D.O. volumes) before citing vigencia as LB.
- OQ-2: Historical chain completeness: which decree(s) fixed retention tables between the 1992 D.E. 25 set and D.E. 95-2015 (in particular after the D.L. 957-2011 Art. 37 reform)? Historical-only relevance (dated-data rows for past periods); low priority.
- OQ-3: Printed-table digit anomalies [sic]: June table 5,371.44 (vs exact 5,371.43), 12,228.60 (vs 12,228.57), cuota 106.20 (vs 106.06); semanal IV DESDE 509.53 (vs 509.5275); quincenal IV 1,019.06. Confirm against the D.O. print of D.E. 10 before encoding as data (same fidelity class as W6 10_ OQ-1..3). NOTE: the cuota 106.20 anomaly is the largest (0.14 deviation from halving) and appears deliberate-looking (matches 2×53.10?) — verify.
- OQ-4: Proration of the $1,600 (Art. 29.7) deduction for quincenal/semanal Tramo II calculations — literal e) mandates "serán consideradas en el cálculo" but gives no factor (monthly /12 implied by recálculo-table shifts; quincenal/semanal unstated). Also: interaction ordering with the d) SS netting. Define for Odoo with an MH-guidance check.
- OQ-5: Does a 2025/2026 aguinaldo transitory exist (capping the Art. 4.16 2-SMM exemption at a fixed $ like 2021-2024's $1,100/$1,500)? The 54_ related-laws tail lists none after D.L. 159 (Nov-2024). Verify before the payroll wave encodes the standing 2-SMM rule.
