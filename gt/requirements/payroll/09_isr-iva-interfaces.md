# GT — Payroll — ISR/IVA interfaces: wage-side value feeds into the rentas-del-trabajo ISR and the Planilla IVA-FEL (SAT-1111) mechanics

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file is the payroll↔ISR/IVA INTERFACES file: everything here is a
POINTER or a VALUE-FEED contract. It defines the wage-side input contract
behind the rentas-del-trabajo ISR engine of
`gt/requirements/taxation/04_isr-trabajo.md` — the perception-date and
remaining-months data feeding GT-TAX-FR-112 and the projection family
GT-TAX-FR-130..133; the bonus-exemption amount feeds (the gross
prestación + payment date that `04_statutory-bonuses.md` GT-PAY-FR-098
supplies) pairing GT-TAX-FR-115/116; the severance feed from
`06_contracts-termination.md` GT-PAY-FR-142 pairing GT-TAX-FR-117; the
estimated IGSS/IPM worker-share parameters of `07_igss-contributions.md`
GT-PAY-FR-155 (external GOQ-04 rows) pairing GT-TAX-FR-124/135; the
boleta/constancia print surfaces pairing GT-TAX-FR-136/137; and the
employer deduction-gating flags (the IGSS-planilla existence flag from
GT-PAY-FR-170's PAGAR state) feeding GT-TAX-FR-146/169 — every ISR
value, exemption split, scale and computation stays in taxation/04
(and, for GT-TAX-FR-169, taxation/05) and is consumed by exact FR id,
never re-derived here. The second half owns the **Planilla IVA-FEL
mechanics** (cluster P6; 56_ = SAT's enero-2024 user manual — a
procedural manual, NEVER cited as law): the Q12,000 IVA-credit
deduction of LAT art. 72.a — owned by GT-TAX-FR-121/122 — declares THIS
file's SAT-1111 mechanics as its operational surface; the filer
eligibility set; the January filing window (01-January → 10th día hábil
23:59:59); the four-source auto-loaded credit feed (FEL DTEs + SAT-8560
+ SAT-2901 + SAT-2311 + SAT-2799) with user-side exclusion and
Exclusión Masiva by emisor NIT; the otros-impuestos exclusion; the
absence of per-document caps in the manual (statutory values = LAT
art. 72, taxation-owned); the SAT-1111 + Constancia deliverables (R46
form identity); the last-wins re-filing regime (earlier planillas =
ANULADAS); the employee→patrono notice feeding GT-TAX-FR-138's January
reconciliation; the anulación-blocker cross-ref GT-EINV-FR-210
(outcome-only); and the IGSS planilla electrónica ≠ SAT Planilla IVA-FEL
disambiguation (same word "planilla", different regimes — Task 7 owns
the IGSS side).

It does **not** cover: the ISR computation itself — hecho generador,
exemptions, Q48,000/Q12,000/Q60,000 rows, the Art. 73 scale, the
projection algorithm, constancia content sets, deadlines and the
practice form registry (`gt/requirements/taxation/04_isr-trabajo.md`
— GT-TAX-FR-111..146 own them; this file wires feeds only); the
Criterio 6-2018 interpretive layer (GT-TAX-FR-169 lives in
`taxation/05_isr-lucrativas-capital.md` — cited by id); the bonus,
severance and IGSS VALUE computations (`04_statutory-bonuses.md`
GT-PAY-FR-076..100, `06_contracts-termination.md` GT-PAY-FR-127..152,
`07_igss-contributions.md` GT-PAY-FR-153..184 — feeds consumed by id);
the IRTRA/INTECAP charges (`08_irtra-intecap.md` GT-PAY-FR-185..206);
the FEL DTE emission/anulación engine (`gt/requirements/e-invoicing/`
— GT-EINV-FR-210 cited by id); and the employer-side declaration
surfaces — RETENISR (SAT-1901), monthly retenciones (SAT-1331), the
worker annual DJ (SAT-1431) — which belong to the F-wave
(`gt/requirements/fiscal-reporting/`, not yet written) and are
cross-referenced by name only, never re-derived.

## 2. Legal Basis

Authority order (binding, per master evidence index): the wage-feed
half owns NO statutory value — every LAT/Reglamento row below is an
interface anchor consumed from `taxation/04_isr-trabajo.md` by FR id
(its LB-002..004/006/010/011 are the verbatim source of the quoted
fragments; 26_ LAT D-10-2012 consolidated ≤ D-46-2022 governs, 28_ AG
213-2013 develops — GOQ-58 caveat on every LAT value, taxation-owned).
The Planilla IVA-FEL half cites **56_ — "PLANILLA IVA-FEL — Manual
para Usuarios Externos, Guatemala, enero 2024" (SAT): a procedural
user manual, NEVER a legal instrument; its statutory hook is LAT
art. 72 (D-10-2012), whose values are owned by taxation/04**
(GT-TAX-FR-121/122). Form identities cite 48_/EV04a under the R46
guard: SAT-1111 = the PLANILLA IVA-FEL application form (paper 1111
superseded — EVID-377 framing carried in taxation/04 LB-012/FR-145;
identities are never re-derived here). GOQ-90 (owned, this file):
enero-2024 manual dating + later SAT UI changes outside the corpus +
employer-side use outside the manual — the caveat rides every
practice row below; GOQ-61 kin flags the F-wave practice-form names;
GOQ-99 requires the "día hábil" qualifier transcribed EXACTLY.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | LAT D-10-2012 (texto consolidado ≤ D-46-2022), Art. 69: "Las rentas gravadas en el presente título se imputan al período de liquidación en que sean percibidas o puestas a disposición del trabajador." / Art. 76: "Al principio de cada año o al inicio de la relación laboral, el patrono o pagador hará una proyección de la renta neta anual del trabajador, a la cual le deducirá el monto de cuarenta y ocho mil quetzales por concepto de gastos personales y el monto de las cuotas anuales estimadas por concepto de pagos al Instituto Guatemalteco de Seguridad Social, Instituto de Previsión Militar y al Estado…" — INTERFACE ANCHOR ONLY: the perception rule and projection inputs are OWNED by `taxation/04_isr-trabajo.md` GT-TAX-FR-112/130..133; this file supplies only the payroll-side dates and remaining-months data | Art. 69: taxable rents impute to the liquidation period in which they are perceived or placed at the worker's disposal; Art. 76: year-start (or hire-date) projection of annual net rent deducting Q48,000 + estimated annual IGSS/IPM/State shares — payroll supplies the perception-date and remaining-months inputs; the algorithm is taxation's by FR id | `gt/sources/26_LAT_10-2012.pdf` | p.33 art. 69; p.35 art. 76 (EVID-226, EVID-229; via taxation/04 LB-002/LB-006) |
| LB-002 | LAT D-10-2012, Art. 70: "5. El aguinaldo hasta el cien por ciento (100%) del sueldo o salario ordinario mensual. 6. La bonificación anual para trabajadores del sector privado y público… hasta el cien por ciento (100%) del sueldo o salario ordinario mensual." — INTERFACE ANCHOR ONLY: the exempt-cap split is OWNED by GT-TAX-FR-115 (aguinaldo) / GT-TAX-FR-116 (bono 14); the gross prestación + payment date are SUPPLIED by `04_statutory-bonuses.md` GT-PAY-FR-098 | Art. 70.5/70.6: aguinaldo and bono 14 each exempt up to 100% of one ordinary monthly salary — payroll feeds the gross amounts and payment dates; the exento/gravado split never computes here | `gt/sources/26_LAT_10-2012.pdf` | pp. 33-34 art. 70 (EVID-226; via taxation/04 LB-003) |
| LB-003 | LAT D-10-2012, Art. 70: "2. El pago de la indemnización por tiempo servido…" (exenta) — INTERFACE ANCHOR ONLY: the full-exemption stamp is OWNED by GT-TAX-FR-117; the settlement quantum is OWNED by `06_contracts-termination.md`; this file wires the feed of GT-PAY-FR-142 | Art. 70.2: the indemnización por tiempo servido payment is exempt — the severance amount flows from the Task 6 settlement engine to the ISR layer with no payroll-side exemption arithmetic | `gt/sources/26_LAT_10-2012.pdf` | pp. 33-34 art. 70 (EVID-226; via taxation/04 LB-003) |
| LB-004 | LAT D-10-2012, Art. 72.a: "doce mil Quetzales (Q.12,000.00) que podrá acreditar por el Impuesto al Valor Agregado pagado en gastos personales… La planilla deberá presentarse ante la Administración Tributaria, dentro de los primeros diez (10) días hábiles del mes de enero de cada año, debiendo el patrono conciliar entre las retenciones efectuadas y la liquidación o declaración definitiva que deberá presentar el trabajador." / Art. 72.c: "Las cuotas por contribuciones al Instituto Guatemalteco de Seguridad Social, al Instituto de Previsión Militar y al Estado y sus instituciones por cuotas de regímenes de previsión social." — INTERFACE ANCHOR ONLY: the Q12,000 row, its field schema and the January reconciliation are OWNED by GT-TAX-FR-121/122/138; the estimated shares by GT-TAX-FR-124/135 (parameters external, GOQ-04) | Art. 72.a: the Q12,000 IVA credit evidenced by the planilla filed within the first 10 días hábiles of January, with the employer reconciling retentions against the worker's definitive liquidation; Art. 72.c: worker-share IGSS/IPM/State previsión contributions deductible — the deduction values are taxation's; this file's SAT-1111 mechanics are their operational surface | `gt/sources/26_LAT_10-2012.pdf` | pp. 34-35 art. 72 (EVID-227; via taxation/04 LB-004) |
| LB-005 | Reglamento LAT (AG 213-2013), art. 70: monthly constancia may be embedded "en la boleta de pago" del asalariado; "constancia final del impuesto retenido durante todo el período, dentro de los diez (10) días hábiles, contados a partir de la fecha en que se efectúe el último pago correspondiente del período de liquidación definitiva anual" — INTERFACE ANCHOR ONLY: constancia content/deadlines are OWNED by GT-TAX-FR-136/137; this file owns the payslip boleta surface they print on | Reglamento art. 70: the monthly retention constancia may be embedded in the worker's payslip boleta; the final constancia issues within 10 días hábiles of the last payment — payroll supplies the print surfaces, taxation the rules | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p.32 art. 70 (EVID-239; via taxation/04 LB-010) |
| LB-006 | LAT D-10-2012, Art. 23: c) "Los que el titular de la deducción no haya cumplido con la obligación de efectuar la retención y pagar el Impuesto Sobre la Renta, cuando corresponda. Serán deducibles una vez se haya enterado la retención."; f) sueldos sin planilla IGSS — INTERFACE ANCHOR ONLY: the art. 21/23 matrices are OWNED by taxation (GT-TAX-FR-146; interpretive GT-TAX-FR-169); this file supplies only the payroll-side gating FLAGS | Art. 23: expenses are non-deductible until the omitted ISR retention is entered (23.c) and salaries off the IGSS planilla are non-deductible (23.f) — payroll exports the retention-settled and IGSS-planilla-existence flags; the deduction gating never computes here | `gt/sources/26_LAT_10-2012.pdf` | pp. 10-17 art. 23 (EVID-220; via taxation/04 LB-011) |
| LB-007 | 56_ (SAT manual, enero 2024 — NOT law): "PLANILLA IVA-FEL — Manual para Usuarios Externos — Guatemala, enero 2024" / "Requerimientos Básicos para ingreso al Sistema: ✓Usuario de Agencia Virtual ✓Actualizado en el RTU Digital ✓Afiliado al Régimen Asalariado" / "El sistema cuenta con la opción para ingresar el Número de Identificación Tributaria (NIT) del patrono con quien laboraste en relación de dependencia hasta el 31 de diciembre del año en curso. Asimismo, ingresa el correo electrónico a donde deseas recibir la notificación que contiene el Formulario SAT-1111 y Constancia de Recepción de Planilla IVA-FEL." / "Base Legal: artículo 72 del Decreto Número 10-2012 del Congreso de la República de Guatemala, Ley de Actualización Tributaria." | Planilla IVA-FEL identity and eligibility: SAT's enero-2024 external-user manual; entry requirements = Agencia Virtual user, current in RTU Digital, afiliado al Régimen Asalariado; the filer registers the patrono NIT with whom he labored in relación de dependencia up to 31-Dec plus the notification email; statutory hook = LAT art. 72 (D-10-2012) — the manual restates no art. 72 monetary condition | `gt/sources/56_SAT_Planilla_IVA_FEL_2024.pdf` | cover; pp.1, 3, 5 (EVID-368; patrono-NIT quote p.5 via EVID-370) |
| LB-008 | 56_, p.4: "…muestra el IVA Crédito y los totales de los Documentos Tributarios Electrónicos (DTE) contenidos en el sistema de FEL, así como los Formularios Declaraguate realizados por pagos del Impuesto al Valor Agregado por: ✓ Declaración Aduanera (SAT-8560), ✓ Factura y Declaración Única Centroamericana -FYDUCA- (SAT-2901) ✓ Traspasos de Vehículos (SAT-2311) ✓ Contratos Pago Directo (SAT-2799)" / "d. TOTAL: Muestra la sumatoria del IVA Crédito y el Total de los Documentos de las literales anteriores." / "NOTA: Puedes visualizar los Documentos Tributarios Electrónicos, DUCA´S y Formularios Declaraguate, los cuales se cargan de formar [sic] automática." | The credit feed is auto-loaded by SAT from four sources: FEL DTEs containing IVA + customs declaración SAT-8560 + FYDUCA SAT-2901 + vehicle transfers SAT-2311 + direct-payment contracts SAT-2799; TOTAL sums the IVA Crédito and document totals of the preceding literals | `gt/sources/56_SAT_Planilla_IVA_FEL_2024.pdf` | p.4 §§2, 4 (EVID-368 p.4; EVID-369 pp.4, 6) |
| LB-009 | 56_, pp.6-7: "IMPORTANTE: tomar en cuenta que la columna “T otalcompras” no tiene incluido el valor correspondiente a Otros Impuestos, tales como Tabaco, Turismo, Hospodaje, entre otros." / Exclusión Masiva: "Podrás excluir de forma masiva los Documentos Tributarios Electrónicos que no desees incluir en Planilla IVA-FEL o bien que estén relacionados a las compras del giro de tu negocio activo." / "f. Exclusión Masiva: Al presionar el botón, se excluirán de tu planilla las FEL del emisor que has seleccionado y se restarán del total de IVA Crédito." (on-screen rationale, p.6: excluir documentos "no razonables conforme a la capacidad de consumo" o "relacionados a las compras del giro del negocio activo") | The "Totalcompras" column EXCLUDES otros impuestos (tabaco, turismo, hospedaje); the employee may exclude documents — including mass exclusion of all FELs of a selected emisor NIT — and exclusions subtract from the IVA Crédito total; no per-document cap or amount ceiling appears anywhere in the manual (defer to LAT art. 72) | `gt/sources/56_SAT_Planilla_IVA_FEL_2024.pdf` | pp.6-7 §§4-5 (EVID-369) |
| LB-010 | 56_, pp.5, 8: "La opción Presentar Planilla, se encuentra disponible a partir del 01 de enero y se inhabilitará el décimo día hábil de enero a las 23:59:59 horas de cada año." / "Recibirás una notificación al correo electrónico ingresado, el cual contendrá un enlace para descargar el Formulario SAT-1111, así como la Constancia de Recepción de Planilla IVA-FEL." | The Presentar Planilla option is available from 01-January and disables on the 10th día hábil of January at 23:59:59 each year; deliverables = the Formulario SAT-1111 + Constancia de Recepción de Planilla IVA-FEL, delivered by email link | `gt/sources/56_SAT_Planilla_IVA_FEL_2024.pdf` | pp.5, 8 §6 (EVID-368 p.5; EVID-370 pp.5, 8) |
| LB-011 | 56_, pp.8-9: "Nota Importante: Si posterior a la presentación de Planilla IVA-FEL deseas incluir o excluir algún documento tributario, puedes realizarlo y presentar nuevamente la planilla, siempre que se encuentre dentro de los 10 días hábiles establecidos en el Artículo 72 del Decreto Número 10-2012…, Ley de Actualización Tributaria. La última Planilla IVA-FEL será la que debes informar al patrono." / "La última Planilla IVA-FEL presentada es la que deberás informar o reportar al patrono, las anteriores se mostrarán como ANULADAS." / "En esta opción te permitirá visualizar las planillas presentadas correspondientes al período de liquidación definitivo anual." | Re-filing: within the same 10 días hábiles window the employee may include/exclude documents and re-present; the LAST planilla prevails and is the one the employee must inform/report to the patrono — earlier presentations display as ANULADAS; the query view shows the planillas of the período de liquidación definitivo anual | `gt/sources/56_SAT_Planilla_IVA_FEL_2024.pdf` | pp.8-9 §§6-7 (EVID-370) |
| LB-012 | Reglas de Validación FEL v2.0, §3.17.2 (validaciones exclusivas de la SAT — anulación): a DTE appearing in "Planilla del IVA FEL" → rechaza — INTERFACE ANCHOR ONLY: the anulación-blocker family is OWNED by `e-invoicing/06_anulacion-contingencia.md` GT-EINV-FR-210 (outcome-only); this file records only the payroll-side consumption note | SAT-exclusive anulación check: if the document appears in the Planilla del IVA FEL, SAT rejects the anulación — the product can neither pre-verify nor override the check | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §3.17.2 p. 123 (EVID-143; via e-invoicing/06 LB-003 / GT-EINV-FR-210) |

Practice-row caveats (binding on every 56_-sourced FR in §3.2): the
56_ manual is SAT's enero-2024 procedural guide — GOQ-90 (owned):
monetary conditions belong to LAT art. 72 (taxation/04), employer-side
use of the SAT-1111 is outside the manual, and later SAT UI changes are
outside the corpus — no UI detail beyond the quoted mechanics may be
encoded as stable behavior; GOQ-61 kin rides the F-wave form names
(SAT-1901/1331/1431 identities anchored in taxation/04 GT-TAX-FR-141/
143/144/145 under R46); GOQ-99 requires the "día hábil" qualifier
transcribed EXACTLY as each instrument prints it (the manual's "décimo
día hábil de enero a las 23:59:59" corroborates the LAT's "primeros
diez (10) días hábiles" — statutory half owned by taxation/04
GT-TAX-FR-142). Version regime (D12): no dated VALUE is owned by this
file — the Q12,000/Q60,000 rows re-date through taxation/04
(GT-TAX-FR-120..123); the January window derives per-year from the
día-hábil calendar (configuration, §4); the 56_ mechanics carry the
enero-2024 stamp on every row.

## 3. Functional Requirements

### 3.1 Wage-side value feeds into taxation/04 (pointer contracts)

- **GT-PAY-FR-207:** The system shall supply, for every employee and pay
  period, the PERCEPTION and PROJECTION data consumed by
  `taxation/04_isr-trabajo.md` — the perception-date imputation inputs
  of GT-TAX-FR-112 (rents imputed when perceived or placed at the
  worker's disposal, LB-001 Art. 69: payslip posting/payment dates, and
  dates any remuneration was placed at disposal) and the projection
  inputs of the GT-TAX-FR-130..133 family: the projection anchor (year
  start or hire date), the remaining-months count for mid-year starts
  (GT-TAX-FR-131), and the recalculation-event dates of GT-TAX-FR-132 —
  DATES AND COUNTERS ONLY; the projection arithmetic, the Q48,000-only
  subtraction and the ÷12 rule are taxation-owned and never restated
  here. (LB-001; EVID-226, EVID-229; cross-ref GT-TAX-FR-112,
  GT-TAX-FR-130..133)
- **GT-PAY-FR-208:** The system shall supply the bonus-exemption feeds
  pairing GT-TAX-FR-115 (aguinaldo) and GT-TAX-FR-116 (bono 14): for
  each bonus payment the GROSS prestación amount and its payment date
  — produced by `04_statutory-bonuses.md` GT-PAY-FR-098 (its ISR
  exemption interface; by exact id) — with NO exento/gravado split, cap
  or vintage computed on this side (the ≤100%-of-one-ordinary-monthly-
  salary exemption arithmetic is taxation's, LB-002; the aguinaldo
  regime itself is corpus-absent per that file's GOQ-09 discipline and
  its absence flows through unchanged). (LB-002; EVID-226; cross-ref
  GT-PAY-FR-098, GT-TAX-FR-115, GT-TAX-FR-116)
- **GT-PAY-FR-209:** The system shall supply the severance feed pairing
  GT-TAX-FR-117: the indemnización por tiempo servido settlement amount
  as computed by `06_contracts-termination.md` (its GT-PAY-FR-142 ISR
  feed flag — full exemption, no split), stamped on the settlement
  lines exactly as that file emits it; no exemption arithmetic,
  retention line or deductibility computation attaches on this side
  (the employer-side 8.33% cap and the retention↔deduction dependency
  are GT-TAX-FR-146/169 — flag feeds only, FR-212).
  (LB-003; EVID-226; cross-ref GT-PAY-FR-142, GT-TAX-FR-117,
  GT-TAX-FR-146, GT-TAX-FR-169)
- **GT-PAY-FR-210:** The system shall supply the ESTIMATED IGSS/IPM
  worker-share parameters consumed by GT-TAX-FR-124/135 (Art. 72.c /
  Art. 76 "cuotas anuales estimadas"): loaded exclusively from the
  external-parameter rows of `07_igss-contributions.md` GT-PAY-FR-155
  (GOQ-04 — JD reglamentos outside the corpus; valid_from/valid_to +
  instrument provenance), consumed as estimated configuration ONLY —
  never constants seeded from this corpus, never a re-derivation of
  rates or bases (the no-deduction invariant of that file's
  GT-PAY-FR-156 is untouched). (LB-004; EVID-227, EVID-229; cross-ref
  GT-PAY-FR-155, GT-TAX-FR-124, GT-TAX-FR-135; GOQ-04 kin)
- **GT-PAY-FR-211:** The system shall provide the CONSTANCIA/BOLETA
  print surfaces pairing GT-TAX-FR-136/137: the monthly payslip boleta
  into which the monthly retention constancia may be embedded ("en la
  boleta de pago", LB-005) and the year-end surface carrying the final
  constancia — CONTENT SETS, delivery deadlines and the 10-días-hábiles
  qualifier are taxation-owned (GT-TAX-FR-136/137; GT-TAX-FR-142
  deadline registry); this file owns only the payroll print surfaces
  and the data plumbing (worker name, employer/worker NIT, rent,
  amount withheld read from the taxation engine's postings).
  (LB-005; EVID-239; cross-ref GT-TAX-FR-136, GT-TAX-FR-137,
  GT-TAX-FR-142)
- **GT-PAY-FR-212:** The system shall supply the employer
  deduction-GATING flags consumed by GT-TAX-FR-146 (art. 23.c/f) and
  the interpretive layer GT-TAX-FR-169: (a) the IGSS-planilla
  EXISTENCE flag per employee-period — true only when the worker's
  salaries are declared in a Planilla de Seguridad Social that reached
  the PAGAR state of `07_igss-contributions.md` GT-PAY-FR-170 (its own
  GT-TAX-FR-146 evidence pairing, by id; payment completion evidenced
  by the single Recibo Electrónico of its GT-PAY-FR-174); and (b) the
  retention-settled flag — the employer expense rows carry the
  suspension stamp until the corresponding ISR retention is entered
  (art. 23.c). FLAGS ONLY: the deduction matrices, caps and the
  criterio planilla-gate scope are taxation's, never re-derived.
  (LB-006; EVID-220, EVID-313; cross-ref GT-PAY-FR-170,
  GT-PAY-FR-174, GT-TAX-FR-146, GT-TAX-FR-169)

### 3.2 Planilla IVA-FEL mechanics (56_; GOQ-90 on every row — procedural manual, never law)

- **GT-PAY-FR-213:** The system shall model the Planilla IVA-FEL FILER
  ELIGIBILITY set exactly as the enero-2024 manual states it (LB-007):
  an Agencia Virtual user, current in the RTU Digital, afiliado al
  Régimen Asalariado, registering the PATRONO NIT with whom the worker
  labored in relación de dependencia up to 31-December of the liquidation
  year, plus a notification email — the statutory population and the
  Q12,000 conditions are LAT art. 72's (taxation/04 GT-TAX-FR-121/122;
  the manual restates no art. 72 monetary threshold — never encode one
  from the manual). GOQ-90: enero-2024 manual; later UI changes outside
  the corpus. (LB-007; LB-004; EVID-368; cross-ref GT-TAX-FR-121,
  GT-TAX-FR-122; GOQ-90 → OQ-001)
- **GT-PAY-FR-214:** The system shall compute the annual filing WINDOW
  as state: opens 01-January and closes on the 10th día hábil of
  January at 23:59:59 of each year ("se inhabilitará el décimo día
  hábil de enero a las 23:59:59 horas" — qualifier transcribed
  EXACTLY, GOQ-99; corroborating the statutory "primeros diez (10)
  días hábiles" of LAT art. 72.a owned by GT-TAX-FR-121) — the
  día-hábil resolution runs in the saas core over a maintained
  holiday-calendar configuration; no filing-event timestamp outside
  the window is accepted as a current-year presentation, and the
  window row carries its per-year derivation provenance. GOQ-90:
  enero-2024 manual. (LB-010; LB-004; EVID-368, EVID-370; cross-ref
  GT-TAX-FR-121, GT-TAX-FR-142; GOQ-90 → OQ-001, GOQ-99 kin → OQ-003)
- **GT-PAY-FR-215:** The system shall mirror the AUTO-LOADED credit
  feed of the Planilla IVA-FEL as read-only intake metadata: the IVA
  Crédito and document totals SAT consolidates automatically from the
  four sources — FEL DTEs containing IVA, DUCA customs declarations
  (SAT-8560), FYDUCA (SAT-2901), vehicle transfers (SAT-2311) and
  direct-payment contracts (SAT-2799) — grouped per the manual's
  literals (FEL / DUCA / FORMULARIOS DG / TOTAL); the FEL-DTE intake
  pairs with the e-invoicing wave's document model (GT-EINV cross-ref;
  a DTE's appearance in this feed is what GT-EINV-FR-210 consumes);
  this file NEVER recomputes a credit total (the Q12,000 cap is
  GT-TAX-FR-121/123's). GOQ-90: enero-2024 manual; feed composition
  may change with the SAT UI. (LB-008; EVID-368, EVID-369; cross-ref
  GT-TAX-FR-121, GT-TAX-FR-123, GT-EINV-FR-210; GOQ-90 → OQ-001)
- **GT-PAY-FR-216:** The system shall model the EMPLOYEE-side
  exclusion semantics as captured state (never employer-recomputed):
  the filer may exclude documents from the planilla — including the
  Exclusión Masiva of all FELs of a selected emisor NIT, which
  subtracts from the IVA Crédito total ("se restarán del total de IVA
  Crédito", LB-009) — with the manual's on-screen rationale (documents
  not razonables conforme a la capacidad de consumo or related to the
  giro del negocio activo) recorded as rationale metadata only; the
  employer/payroll side may neither apply nor undo an exclusion — it
  consumes the FINAL planilla state of FR-219/220. GOQ-90: enero-2024
  manual. (LB-009; EVID-369; GOQ-90 → OQ-001)
- **GT-PAY-FR-217:** GUARD (no caps, otros impuestos): the system shall
  implement the feed's composition guards EXACTLY as printed — the
  "Totalcompras" column EXCLUDES the value of otros impuestos (tabaco,
  turismo, hospedaje, entre otros; LB-009), and NO per-document cap or
  amount ceiling from the manual shall ever be encoded (none exists in
  the 56_ text): every monetary condition of the credit defers to LAT
  art. 72 as owned by taxation/04 (GT-TAX-FR-121/122/123 — the Q12,000
  cap, the field schema and the reasonable-consumption rule of 28_
  art. 68 are GT-TAX-FR-122's, cited by id). GOQ-90: enero-2024
  manual. (LB-009; LB-004; EVID-369; cross-ref GT-TAX-FR-121,
  GT-TAX-FR-122, GT-TAX-FR-123; GOQ-90 → OQ-001)
- **GT-PAY-FR-218:** The system shall model the filing DELIVERABLES as
  identity-guarded document intake: the Formulario SAT-1111 + the
  Constancia de Recepción de Planilla IVA-FEL, delivered by email link
  to the registered address (LB-010) — form identity under the R46
  guard: SAT-1111 = the PLANILLA IVA-FEL APPLICATION form (paper 1111
  superseded; identities cite 48_/EV04a framing carried in
  taxation/04 GT-TAX-FR-145 — never re-derived here, never sourced to
  the manual); captured as employee-submitted documents on the
  worker's record with receipt metadata. GOQ-90/GOQ-61 kin: enero-2024
  manual + F-wave practice dating. (LB-010; EVID-368, EVID-370;
  cross-ref GT-TAX-FR-145; GOQ-90 → OQ-001, GOQ-61 kin → OQ-002)
- **GT-PAY-FR-219:** The system shall model RE-FILING as last-wins
  state: within the same 10-días-hábiles window the filer may include
  or exclude documents and re-present the planilla (LB-011); the LAST
  Planilla IVA-FEL presented is the current one and every earlier
  presentation of the same período de liquidación definitivo anual
  displays as ANULADAS — the planilla-state resolution (which
  presentation is current per worker-year) is authoritative saas state
  recomputed on each presentation event; no earlier presentation may
  feed any consumer once superseded. GOQ-90: enero-2024 manual.
  (LB-011; EVID-370; GOQ-90 → OQ-001)
- **GT-PAY-FR-220:** The system shall implement the EMPLOYEE→PATRONO
  notice as the employer-side intake feeding the January reconciliation
  of GT-TAX-FR-138: the worker reports/informs the LAST planilla
  (LB-011; the SAT-1111 + Constancia of FR-218 captured as evidence),
  and the reconciliation surface consumes it as the Q12,000-credit
  evidence input alongside the retention records — the reconciliation
  arithmetic, the informe and the up-to-Q12,000 credit computation are
  GT-TAX-FR-138/121's (by id); the employer-side declaration outputs
  (RETENISR SAT-1901 DEFINITIVA mode, SAT-1331 monthly, SAT-1431
  worker annual) are F-wave surfaces cross-referenced by name ONLY
  (identities owned by taxation/04 GT-TAX-FR-141/143/144 under R46 —
  GOQ-61 kin). GOQ-90: enero-2024 manual (employer-side use of the
  SAT-1111 is outside the manual's scope). (LB-011; LB-004; EVID-370,
  EVID-227; cross-ref GT-TAX-FR-138, GT-TAX-FR-121, GT-TAX-FR-141,
  GT-TAX-FR-143, GT-TAX-FR-144; GOQ-90 → OQ-001, GOQ-61 kin → OQ-002)
- **GT-PAY-FR-221:** DISAMBIGUATION GUARD: the system shall keep the
  IGSS Planilla de Seguridad Social electrónica
  (`07_igss-contributions.md` GT-PAY-FR-170 — the employer's monthly
  social-security declaration, four-state GENERAR/TRANSMITIR/VALIDAR/
  PAGAR lifecycle, D-295/08-SGF-2026 regime) and the SAT Planilla
  IVA-FEL (THIS §3.2 — the employee's annual IVA-credit planilla, LAT
  art. 72 regime) as STRICTLY SEPARATE regimes and records despite the
  shared word "planilla": different filers (patrono vs asalariado),
  different collectors (IGSS vs SAT), different periods (monthly vs
  annual-January), different legal bases (D-295 family vs LAT art. 72)
  — no record, flag, deadline or state of one may ever be read as the
  other's; the ONLY sanctioned pairing is FR-212's IGSS-planilla
  existence flag → GT-TAX-FR-146 (art. 23.f), which stays IGSS-side.
  (LB-007; EVID-368; cross-ref GT-PAY-FR-170, GT-PAY-FR-018,
  GT-TAX-FR-146; GOQ-90 → OQ-001)
- **GT-PAY-FR-222:** ANULACIÓN CROSS-REF (outcome-only): a FEL DTE
  that appears in the Planilla del IVA FEL feed BLOCKS its anulación
  at SAT — modeled exclusively as the outcome-only blocker family
  owned by `e-invoicing/06_anulacion-contingencia.md` GT-EINV-FR-210
  (by exact id): the product shall neither pre-verify the block
  (appearance in this file's FR-215 feed raises advisory awareness,
  never a promise) nor override the SAT rejection; rejection surfaces
  carry the GT-EINV-FR-210 blocker-family label. POINTER ONLY — the
  anulación engine is e-invoicing's. (LB-012; EVID-143; cross-ref
  GT-EINV-FR-210, GT-PAY-FR-215)

## 4. Data Model

Layer semantics: payroll is Odoo-native for computation and capture;
feed contracts are `shared` (both sides resolve the same rows); the
FEL-invoice intake mirror is `odoo` (GT-EINV pairing); window-state and
planilla-state computation are `saas` (odoo emits the captured events).
No dated VALUE lives in this file — the Q12,000/Q60,000/deduction rows
re-date through taxation/04 (GT-TAX-FR-120..123); the estimated IGSS/IPM
parameters re-date through `07_igss-contributions.md` (GT-PAY-FR-155);
the January window derives per-year from the día-hábil calendar
configuration below (D15/D16: valid_from/valid_to + provenance;
snapshot-on-write).

**Wage-side ISR feed record (per employee-period):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.isr.feed (new) | employee_id · period · perception_dates[] · placed_at_disposal_dates[] | m2o/char/date[] | the GT-TAX-FR-112 imputation inputs (pay posting/payment + at-disposal events) | FR-207 |
| l10n_gt.pay.isr.feed | projection_anchor · remaining_months · recalc_event_dates[] | selection/date/integer/date[] | year_start · hire_date; mid-year counter (GT-TAX-FR-131); change events (GT-TAX-FR-132) — dates/counters only, arithmetic taxation-side | FR-207 |
| l10n_gt.pay.isr.feed | bonus_gross_prestaciones[] · payment_dates[] | monetary[]/date[] | pointer rows to `04_statutory-bonuses.md` GT-PAY-FR-098 (aguinaldo/bono 14 gross + date; no split) | FR-208 |
| l10n_gt.pay.isr.feed | severance_amount · exemption_flag | monetary/boolean (pointer) | from `06_contracts-termination.md` GT-PAY-FR-142 — the GT-TAX-FR-117 full-exemption stamp, feed only | FR-209 |
| l10n_gt.pay.isr.feed | estimated_igss_ipm_params | config ref | external rows of `07_igss-contributions.md` GT-PAY-FR-155 (GOQ-04; estimated only, never corpus constants) | FR-210 |
| hr.payslip (report) | boleta constancia embedding · final-constancia surface | report view | print surfaces pairing GT-TAX-FR-136/137; content/deadlines taxation-owned | FR-211 |
| l10n_gt.pay.isr.gating.flag | employee_id · period · igss_planilla_exists · retention_settled | m2o/char/boolean/boolean | IGSS-planilla existence = PAGAR state of 07 GT-PAY-FR-170 (evidence: Recibo Electrónico of its GT-PAY-FR-174); retention-settled per art. 23.c — flags only, gating arithmetic = GT-TAX-FR-146/169 | FR-212 |

**Planilla IVA-FEL (employee-side annual; GOQ-90 on every row):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.planilla_iva_fel.filer (new) | worker_id · agencia_virtual_user · rtu_digital_current · regimen_asalariado · patrono_nit · relacion_hasta · notify_email | m2o/boolean/boolean/boolean/char(12)/date/char | eligibility set + patrono NIT (relación de dependencia up to 31-Dec of the liquidation year) + email | FR-213 |
| l10n_gt.pay.planilla_iva_fel.window (saas) | year · opens_at · closes_at · closes_rule · derivation_provenance | int/datetime/datetime/char/char | opens 01-Jan 00:00; closes 10th día hábil of January 23:59:59 (rule "décimo día hábil", GOQ-99 exact); resolved over the holiday-calendar config | FR-214 |
| config (shared) | l10n_gt.pay.dia_habil.calendar | dated rows | per-year Guatemalan holiday calendar feeding the día-hábil resolution (external maintenance; provenance recorded) | FR-214 |
| l10n_gt.pay.planilla_iva_fel.document (new) | worker_id · year · source · form_code · dte_ref · iva_credito · total · excluded · exclusion_kind · emisor_nit | m2o/int/select(FEL·DUCA·FORMULARIOS_DG)/char/m2o/monetary/monetary/boolean/select(single·masiva)/char(12) | read-only mirror of the SAT auto-loaded feed (FEL DTEs + SAT-8560/2901/2311/2799); exclusions incl. Exclusión Masiva by emisor NIT (subtract from IVA Crédito — captured state, never employer-recomputed); otros-impuestos guard (no-cap row below) | FR-215, FR-216 |
| l10n_gt.pay.planilla_iva_fel.guard | no_per_document_cap · otros_impuestos_excluded | boolean guard rows | no monetary cap from the manual ever encoded (defer to LAT art. 72 = GT-TAX-FR-121/122/123); Totalcompras excludes tabaco/turismo/hospedaje | FR-217 |
| l10n_gt.pay.planilla_iva_fel.filing (new) | worker_id · year · presented_at · sat_1111_doc · constancia_doc · state | m2o/int/datetime/attachment/attachment/select(current·anulada) | deliverables captured (SAT-1111 + Constancia; R46 identity via GT-TAX-FR-145); last-wins: exactly one current per worker-year, earlier = anulada | FR-218, FR-219 |
| l10n_gt.pay.planilla_iva_fel.informe (new) | worker_id · year · current_filing_id · reported_to_patrono_at · reconciliation_feed_ref | m2o/int/m2o/datetime/ref | the employee→patrono notice intake; consumed as Q12,000-credit evidence by GT-TAX-FR-138's January reconciliation | FR-220 |
| l10n_gt.pay.planilla.disambiguation | guard row | char | IGSS planilla electrónica (07 GT-PAY-FR-170) ≠ SAT Planilla IVA-FEL — regimes never conflated | FR-221 |
| l10n_gt.pay.planilla_iva_fel.anulacion.pointer | cross-ref row | char | DTE-in-feed → GT-EINV-FR-210 outcome-only blocker (never pre-verified) | FR-222 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. Per the wave plan:
feed contracts = `shared`; FEL-invoice intake = `odoo` (GT-EINV
pairing); window/planilla-state computation = `saas`. Model names
stable across Odoo 17/18/19/20; no version-specific behavior required.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-207 | shared | — (contract over hr.payslip events) | perception/projection data set | Dates/counters only; arithmetic = GT-TAX-FR-112/130..133 by id |
| FR-208 | shared | — (pointer over 04 GT-PAY-FR-098) | gross prestación + payment date | Split/caps = GT-TAX-FR-115/116 by id; GOQ-09 aguinaldo absence flows through |
| FR-209 | shared | — (pointer over 06 GT-PAY-FR-142) | severance amount + exemption flag | Full exemption = GT-TAX-FR-117; deductibility = GT-TAX-FR-146/169 flags only |
| FR-210 | shared | — (config ref to 07 GT-PAY-FR-155) | estimated IGSS/IPM parameters | GOQ-04 external rows; consumed by GT-TAX-FR-124/135; never constants |
| FR-211 | shared | — (report-surface contract) | boleta embedding + final-constancia surface | Content/deadlines = GT-TAX-FR-136/137/142 by id |
| FR-212 | shared | — (flag contract §4) | igss_planilla_exists + retention_settled | PAGAR state of 07 GT-PAY-FR-170; gating = GT-TAX-FR-146/169 by id |
| FR-213 | shared | — (eligibility contract §4) | filer eligibility set + patrono NIT | LAT art. 72 population = GT-TAX-FR-121/122; GOQ-90 flag |
| FR-214 | saas | — (odoo surfaces config) | window state per year | Día-hábil resolution authoritative in saas; "décimo día hábil" transcription exact (GOQ-99); GOQ-90 flag |
| FR-215 | odoo | l10n_gt.pay.planilla_iva_fel.document | four-source feed mirror | FEL intake pairs GT-EINV doc model; appearance feeds GT-EINV-FR-210 awareness; GOQ-90 flag |
| FR-216 | odoo | l10n_gt.pay.planilla_iva_fel.document | exclusion/exclusión-masiva state | Captured employee-side state; never employer-recomputed; GOQ-90 flag |
| FR-217 | shared | — (guard rows §4) | no-cap + otros-impuestos guards | Monetary conditions defer to LAT art. 72 (GT-TAX-FR-121/122/123); GOQ-90 flag |
| FR-218 | odoo | l10n_gt.pay.planilla_iva_fel.filing | SAT-1111 + Constancia capture | R46 identity via GT-TAX-FR-145 (48_/EV04a); GOQ-90/61 flags |
| FR-219 | saas | — (odoo emits presentation events) | last-wins planilla state | Exactly one current per worker-year; earlier = ANULADAS; GOQ-90 flag |
| FR-220 | shared | — (informe feed contract §4) | final-planilla notice intake | Feeds GT-TAX-FR-138 reconciliation; F-wave outputs by name only (SAT-1901/1331/1431 = GT-TAX-FR-141/143/144, R46); GOQ-90/61 flags |
| FR-221 | shared | — (disambiguation guard §4) | regime separation guard | IGSS planilla (07 GT-PAY-FR-170) ≠ SAT Planilla IVA-FEL; GOQ-90 flag |
| FR-222 | shared | — (pointer row §4) | anulación blocker cross-ref | Outcome-only = GT-EINV-FR-210; never pre-verified |

## 6. Acceptance Criteria

- **AC-001:** Given a worker hired 1-July whose payslip posts a
  commission on 15-July, when the ISR feed assembles, then the feed
  carries perception_dates = [15-July] (Art. 69 imputation data),
  projection_anchor = hire_date and remaining_months = 6 — and the
  retention computed by GT-TAX-FR-130/131 over them is consumed by id
  with no arithmetic executed in this file. (FR-207)
- **AC-002:** Given a July bono 14 payment of Q3,500 with ordinary
  monthly salary Q3,500, when the feed exports, then the ISR feed
  carries the gross prestación Q3,500 + payment date and NOTHING else —
  the exento/gravado split (here Q3,500 exempt ≤ 100% cap) resolves
  entirely inside GT-TAX-FR-116 via `04` GT-PAY-FR-098's interface.
  (FR-208)
- **AC-003:** Given a termination settlement paying indemnización por
  tiempo servido Q18,000, when the settlement posts, then the feed
  carries the amount with the GT-PAY-FR-142 full-exemption stamp from
  GT-TAX-FR-117 and no retention line, no split and no deductibility
  computation arises payroll-side. (FR-209)
- **AC-004:** Given a year whose configured GT-PAY-FR-155 rows set the
  estimated worker IGSS share at X%, when the projection runs, then
  taxation's engine consumes X as an estimated parameter with its
  valid_from provenance — and no rate constant exists anywhere in this
  file's code or seed data (GOQ-04). (FR-210)
- **AC-005:** Given a monthly payslip, when the boleta prints, then the
  GT-TAX-FR-136 constancia block (worker name, employer/worker NIT,
  rent, amount withheld) is embeddable in it ("en la boleta de pago"),
  and at year-end the final constancia surfaces per GT-TAX-FR-137's
  10-días-hábiles rule — deadlines read from taxation's registry, never
  restated. (FR-211)
- **AC-006:** Given a worker whose January–March salaries were declared
  in an IGSS Planilla de Seguridad Social that reached PAGAR (Recibo
  Electrónico generated), when the gating flags export, then
  igss_planilla_exists = true for those periods and the employer
  expense rows pass GT-TAX-FR-146's art. 23.f gate; given a period with
  no paid planilla, the flag is false and GT-TAX-FR-146/169 gating
  suspends deductibility — computed taxation-side from this flag only.
  (FR-212)
- **AC-007:** Given a worker who is an Agencia Virtual user, current in
  RTU Digital and afiliado al Régimen Asalariado, with patrono NIT
  1234567-8 registered (relación de dependencia through 31-Dec-2026),
  when the filer record assembles for liquidation year 2026, then the
  eligibility set is complete and the record carries the patrono NIT +
  notification email; given any missing eligibility element, the
  Planilla IVA-FEL surface is not offered for that worker. (FR-213)
- **AC-008:** Given a year whose first ten días hábiles of January end
  on 16-January (holiday-shifted calendar), when the window state
  resolves, then the window closes 16-January 23:59:59 — the rule
  "décimo día hábil" applied over the configured calendar (GOQ-99
  exact), with the derivation provenance stamped; given a presentation
  timestamp 17-January 00:00:01, it is rejected as outside the window.
  (FR-214)
- **AC-009:** Given a worker's feed containing a FEL DTE with IVA
  Q120, a SAT-8560 with IVA Q80, a SAT-2901 with IVA Q60, a SAT-2311
  and a SAT-2799, when the mirror assembles, then the documents group
  under the manual's literals (FEL / DUCA / FORMULARIOS DG) with the
  TOTAL summing them — and no credit cap is applied or validated at
  this layer (the Q12,000 cap is GT-TAX-FR-121/123's, January-side).
  (FR-215, FR-217)
- **AC-010:** Given the filer runs Exclusión Masiva on emisor NIT
  8877665-4, when the captured state lands, then every FEL of that
  emisor is flagged excluded (kind = masiva) and the excluded amounts
  subtract from the mirrored IVA Crédito total — and no employer-side
  process may re-include or recompute them; the consumer reads only the
  final planilla state. (FR-216)
- **AC-011:** Given a "Totalcompras" value, when inspected, then it
  never includes tabaco/turismo/hospedaje otros-impuestos amounts
  (guard row), and given a proposal to seed any per-document cap from
  the 56_ manual, when validated, then it is rejected — no monetary
  condition of the credit exists in this file (LAT art. 72 deferral).
  (FR-217)
- **AC-012:** Given a presentation on 8-January (within the window)
  followed by a re-presentation on the last día hábil, when the
  planilla state resolves, then the second filing is current with its
  SAT-1111 + Constancia captured, and the first shows state = anulada —
  exactly one current filing exists per worker-year. (FR-218, FR-219)
- **AC-013:** Given the worker reports the final planilla to the
  patrono, when the informe record saves, then the January
  reconciliation of GT-TAX-FR-138 consumes it as the Q12,000-credit
  evidence input alongside the retention postings — and the
  reconciliation/informe arithmetic executes entirely in taxation/04,
  with F-wave surfaces (SAT-1901/1331/1431) referenced by name only.
  (FR-220)
- **AC-014:** Given a user searching payroll records for "planilla",
  when the IGSS Planilla de Seguridad Social (07 GT-PAY-FR-170) and the
  SAT Planilla IVA-FEL (this §3.2) surface, then they carry distinct
  models, filers, collectors, periods and legal bases with the
  disambiguation guard row on both — and no state of one ever feeds the
  other save FR-212's IGSS-planilla existence flag into GT-TAX-FR-146.
  (FR-221)
- **AC-015:** Given a FEL DTE present in the mirrored Planilla IVA-FEL
  feed for which the emisor requests anulación, when SAT rejects it per
  §3.17.2, then the rejection surfaces with the GT-EINV-FR-210
  blocker-family label — and the product never asserted a pre-verified
  block (advisory awareness only, never a promise). (FR-222)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md`
§C); allowed set for this file: GOQ-90 (owned), GOQ-61/99 (kin, flagged
where they bite). All rows Status open; GOQs are trace-pending, not
blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-90 (owned): "56_ (Planilla IVA-FEL) = enero-2024 manual: monetary conditions owned by LAT art. 72 (W-GT2); employer-side use + later UI changes outside corpus." Affects FR-213..221 (every 56_-sourced practice row carries the dating caveat; UI mechanics may have changed after enero-2024 — no SAT-app detail beyond the quoted mechanics may be encoded as stable behavior; employer-side consumption of the SAT-1111 beyond the manual's "informar al patrono" is unwritten). | no | GT synthesis wave S-GT3 → F-wave catalog/manual-version confirmation | open |
| OQ-002 | GOQ-61 (kin): F-wave practice-form surfaces named here (RETENISR SAT-1901 DEFINITIVA mode, SAT-1331 monthly, SAT-1431 worker annual) carry the undated-digest dating caveat; identities are R46-anchored in taxation/04 GT-TAX-FR-141/143/144/145 and the filing surfaces land with the F-wave — re-verify form vintages when `gt/requirements/fiscal-reporting/` files are written. | no | F-wave (form vintage watch) | open |
| OQ-003 | GOQ-99 (kin): the "día hábil" qualifier is transcribed EXACTLY on both sources (manual: "décimo día hábil de enero a las 23:59:59"; LAT art. 72.a: "primeros diez (10) días hábiles" — statutory half owned by taxation/04 GT-TAX-FR-142); the día-hábil CALENDAR itself (Guatemalan holiday set per year) is external configuration with no corpus source — provenance of each year's calendar row must be recorded at implementation. | no | GT synthesis wave S-GT3 → implementation config (holiday-calendar provenance) | open |
