# HN — Fiscal reporting — The 30-abril annual package: ISR 102 (PN) / 103 (PJ) + Aportación Solidaria + Activo Total Neto + PN minimum-exempt suspension

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Honduras annual-close
declaration package due at 30 April — cluster F7 of the W2 evidence (EV29:
EVID-091..110). It owns: (a) **código 102** — the *Declaración Jurada
Determinativa* (sworn determinative declaration) of annual ISR for *personas
naturales* (natural persons): the four-section A-D layout, the
ingresos/gastos concept catalogs with their fixed subaccount menus, the
Art. 20 minimum-activities income selector, the transfer-pricing ±
adjustment lines, the Sección B *vinculación entre declaraciones*
(cross-declaration linkage) engine by which cedular / código 119 / código
120 / código 113 bases flow into *ingresos netos no gravados* (non-taxable
net income) once declared AND paid, the Sección C credit panel reconciled
to the SAR *cuenta corriente* (tax current account) including the D.
96-2012 anticipo (two loss years + gross ≥ L100M), the 3%-CIF import
advance, the D. 54-96 job-creation credit (≥ 5 new hires) and the CT
Art. 142 *cesiones* (credit assignments), plus the *empleados* block;
(b) **código 103** — the annual DJ for *personas jurídicas* (juridical
persons) liquidating THREE taxes in one form (ISR + Aportación Solidaria +
Activo Total Neto): the ISV 15/18/export-split revenue panel, commercial
and production costing blocks, the ≤ 50% loss-carryforward gate, the Art.
22-A selector (prior-year gross > L1,000,000,000), the 119/120 read-only
and DMR-113 editable cross-links, per-tax credit subpanels and the
535 prerequisite gate; (c) **Aportación Solidaria (AS)** — 5% ×
max(0, RNG − L1,000,000), PJ-only per the prints, Exportación/Turismo
excluded (R-H30); (d) **Activo Total Neto (ATN)** — the net-asset minimum
tax with the L3,000,000 exemption, floor-tax credit and the
period-202401+ autofill from the 535 EEFF report; and (e) the **75_**
*escrito de suspensión* (suspension petition) for PN whose income does not
exceed the *mínimo exento* (exempt minimum), filed 1-January→30-April of
the following year.

It does **not** own: the OVI/SW filing chassis, state machine, acuse and
rectificativa mechanics (fiscal-reporting file 01, cluster F1 — consumed
by id); the DJIMR/DMR retention-declaration export contract and the
112/113/135 linkage validation (file 02, cluster F2); the DMC 527 (file
03); the OTCD cards (file 04); the ISV 201 (file 05); the 535 EEFF report
itself and its gate internals (file 06, cluster F6 — consumed by id); the
GC 119 / ZOLITUR 120 / Tradición 152 / Revaluación 154 declaration
engines (file 08, cluster F8 — bases flow in by id); selectivo (file 09);
TP 545 and the Ajuste auto-migration (file 10, cluster F10 — consumed by
id); contribuciones 506/107 (file 11, cluster F11 — calendar members
only); every substantive rate, threshold, scale vintage, 22-A regime row
and deduction semantic — owned by the taxation wave
(`../taxation/01_isr-framework.md` HN-TAX-FR-001..045,
`../taxation/02_isr-deductions.md` HN-TAX-FR-046..078,
`../taxation/03_isr-rates-gains-minimum.md` HN-TAX-FR-081..104,
`../taxation/04_isr-withholding.md` HN-TAX-FR-121..153 and the
`../taxation/isr_brackets.csv` seed) and consumed BY ID, never restated;
and payroll mechanics (S-HN4 `../payroll/` — delivered, consumer of the
empleados block and the Art. 10 exclusions of EVID-093/096).

## 2. Legal Basis

Authority order (binding, per master evidence index): SAR/DEI acuerdos are
primary for declaration mechanics; per-código Ayudas are the field/flow
authority; `71_` per-row only (R-H27); manuals are STALE vs gazettes where
they conflict (R-H18). Binding rulings applied: R-H9 (composite
sole-source gate), R-H29 (ATN rate 1% pinned only by 74_ p.10; instrument
conflict open), R-H30 (AS = 5% × max(0, RNG − L1,000,000), PJ-only per
prints, Exportación/Turismo excluded per 74_ only), R-H32 (22-A = three
dated regimes; "(1.05%)" defect, 1% text-primary). Unacquired instruments
cited below stand ONLY as evidenced in EV29 prints — LEAD-flagged, never
as asserting LBs: D. 199-2006 (95_/96_), D. 194-2002 (97_), D. 96-2012,
D. 54-96, D. 110-93 Art. 9, LET D. 51-2003.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ayuda DJ ISR PN código 102 (29_, print Agosto 2026), Generalidades 1-2/5-6/11-12: sujetos Art. 2 — "Toda persona domiciliada o residente en Honduras [...] deberá pagar este Impuesto sobre la Renta"; plazo — "Todo contribuyente está obligado a presentar ante la Administración Tributaria (AT), por si o por medio de mandatario o de representante legal, del uno de enero al treinta de abril o siguiente día hábil de cada año, una Declaración Jurada de las Rentas que haya obtenido el año anterior"; período — "principia el uno (1) de enero y termina el treinta y uno (31) de diciembre"; especial — "el contribuyente podrá tener un período fiscal especial, el que deberá notificar previamente por escrito a la Administración Tributaria"; tarifa PN progresiva Art. 22.b ajustada por IPC; form 102 = "Determinativa"; base legal: Ley ISR D.25-1963, CT D.170-2016, Acuerdo SAR-236-2024 | PN annual ISR Ayuda (code 102): subjects per Art. 2 (domiciled/resident persons incl. State concessionaires); filing window 1-Jan→30-Apr (or next business day) of the following year, personally or via mandatory/legal representative; calendar fiscal year; special fiscal year requires prior written notice to SAR; PN progressive IPC-adjusted tariff; the form is determinative | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ pp.4-9, 66 (EV29:EVID-092) |
| LB-002 | 29_, sección 2.2 + Sección D: "La declaración está compuesta por secciones [...] A- Cálculo del ISR; B- Datos informativos de carácter tributario; C- Créditos; D- Resumen"; contador obligatorio para "personas naturales declaradas como Comerciante Individual" (nombre, RTN de catorce (14) posiciones, número de colegiación); B — "Esta sección no afecta para el cálculo del impuesto"; D autogenerada + ventana informativa de "Períodos normales, especiales, beneficios fiscales" | 29_ §2.2 + D: four-section layout; accountant identification (name, 14-position RTN, college number) mandatory only for Comerciante-Individual PNs; Sección B informative-only; the D summary and its fiscal-period/benefits info window are system-generated | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ pp.13-14, 32, 56 (EV29:EVID-095) |
| LB-003 | 29_, Sección A catálogos: Ingresos — "sueldos, salarios, bonificaciones / actividades mercantiles / servicios / alquileres / intereses no bancarios / otros ingresos gravables / Actividades del Artículo 20 / Honorarios Profesionales / Ajustes de precios de transferencia Positivo"; Art. 20 — "agropecuarias, agroindustriales, manufactureras, mineras y de turismo" + dropdown de actividad; Gastos espejo (9 conceptos) con subcuentas — "Cuotas AFP, Cuota de colegios profesionales, Cuota o instituciones de jubilación y pensiones privadas o públicas, Cotizaciones RAP 1,5%"; AFP deducibles "siempre y cuando estas no sean retiradas en el período fiscal que está reportando" (Reglamento Arts. 19 y 51); alquileres per "Decreto 17-2010 artículo 5" | 29_ §A catalogs: nine mirrored income/expense concepts with fixed subaccount menus (TP positive on income / negative on expenses; AFP/college/pension/RAP-1.5% payroll-cost subaccounts); the Art. 20 income concept carries an activity dropdown limited to five activities; AFP contributions deductible only if not withdrawn in the reported FY (ISR reglamento cited but unacquired); rental income managed per D. 17-2010 Art. 5 | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ pp.15-31 (EV29:EVID-096) |
| LB-004 | 29_, Generalidad 4 + §2.2 intro: deducciones Art. 13 — "a. La suma anual hasta de CUARENTA MIL LEMPIRAS (L.40,000.00) por gastos educativos y por honorarios pagados a médicos. b. En el caso de las personas mayores de sesenta y cinco (65) años [...] OCHENTA MIL LEMPIRAS (L80,000.00), reformado en el Art. 1 del Decreto Legislativo No.59-2020 [...] c. gastos incurridos en el ejercicio de una profesión [...] d. agricultores y ganaderos [...] e. donaciones [...] hasta por un monto que no exceda al diez por ciento (10%) de la Renta Neta Gravable"; auto-behavior — "el formulario determina de manera automática la Utilidad (Ingresos - Gastos), igualmente la Renta neta gravable (RNG) y otorga las Deducciones relacionadas con Gastos médicos y Otros, Artículo 30, numeral 14 Decreto (199 - 2006) y Renta Bruta por Art.14 Decreto (194-2002) en los casos que aplique" | 29_ deductions: the Art. 13 stack (L40,000 education/medical; L80,000 for 65+ per D. 59-2020; profession costs; farmer/rancher costs; donations ≤ 10% of RNG); the form auto-computes utilidad and RNG and auto-applies the senior hooks of D. 199-2006 and the D. 194-2002 Art. 14 renta-bruta exclusion where applicable — the citation is garbled (29_ OQ-1) and no amount is restated | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ p.6 + p.13 (EV29:EVID-094) |
| LB-005 | 29_+68_, Art. 10 restatement (rentas no gravadas a-h), incl. — "El décimo tercer mes en concepto de aguinaldo, así como el décimo cuarto mes de salario, hasta por el monto de diez (10) salarios mínimos promedio, en cada caso, a partir de cuyo monto serán gravables" | The Art. 10 exclusion list restated in both manuals: 13th and 14th month exempt up to 10 × average minimum wage EACH, excess taxable; IHSS/occupational-risk/pension-fund/prestaciones exclusions; Honduran-institution conditions (payroll mechanics = S-HN4 consumer) | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` + `hn/sources/68_Generalidades_ISR.pdf` | 29_ pp.5-6; 68_ p.3 (EV29:EVID-093) |
| LB-006 | 29_, Sección B: vinculación — "se genera un enlace de información entre declaraciones informativas y declaraciones determinativas [...] la información que se consigne en las declaraciones informativas afectara las declaraciones determinativas relacionadas"; casillas habilitadas: "Dividendos y participación de utilidades / Ganancias de capital / Ganancias de capital (ZOLITUR) / Impuesto cedular sobre la renta por alquiler habitacional"; precondición — "deben declarar y pagar el Impuesto cedular [...] y Ganancias de capital, Ganancias de capital (ZOLITUR), en los casos que aplique"; entonces "las bases imponibles se reflejarán automáticamente en la subsección de Ingresos Netos no gravados"; tasas reiteradas: cedular 10% > L15,000/mes (D. 17-2010 Art. 5); ZOLITUR "tasa diferenciada del (4%) [...] Decreto 181 -2006 [...] Artículo 4"; dividendos 10% retenido por la sociedad (Art. 25); ingresos bancarios 10% (D. 110-93 Art. 9); premios lotería = ganancias de capital (Reglamento Art. 32) | 29_ §B: the cross-declaration linkage engine — informativa values propagate into the determinativa; enabled lines: dividends, GC, GC-ZOLITUR, cedular rental; hard precondition: the linked tax must be declared AND paid before its base auto-flows into no-gravados; restated rates are consumed from taxation/05+03 by id (ZOLITUR article conflict carried); bank interests 10% per D. 110-93 Art. 9 (acquired W6, `117_` EVID-426) | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ pp.32-40 (EV29:EVID-097) |
| LB-007 | 29_, Sección C: panel — "Pagos realizados para el período / Excedente del período anterior / Cesiones de crédito / Importe a compensar / Créditos aplicados a pagos a cuenta / Pagos a cuenta / Créditos aplicados a anticipos 1% / Anticipos 1% ISR / Retención en la fuente de asalariados / Retención art. 50 de la ley ISR / Retención anticipo 1% ISR art 19 Decreto 17/2010 / Retención anticipo ISR importaciones / Crédito por generación de nuevos empleos / Importe por exoneración o reducción"; "Todas las casillas anteriores se derivan de la información existente en la cuenta corriente del obligado tributario"; D. 96-2012 — anticipo 1% para quien "en dos (2) de ellos hayan tenido pérdidas operacionales consecutivas o alternas y que en el último período fiscal hayan obtenido ingresos brutos igual o superior a Cien Millones de Lempiras (L.100,000,000.00)"; importaciones — "un tres por ciento (3%) del Impuesto Sobre la Renta, aplicado sobre la base referencial del valor CIF"; D. 54-96 — crédito habilitado si "suman 5 o más empleados"; cesiones — "Artículo No.142 del Decreto 170-2016 Código Tributario" | 29_ §C: the 14-line credit panel derived from the SAR current account; retention credits auto-linked from the agents' informativas; D. 96-2012 anticipo eligibility (2 loss years within non-prescribed FYs + last-FY gross ≥ L100M) and the 3%-CIF import advance; D. 54-96 job credit unlocked at ≥ 5 new employees (incl. disability, per §B counts); cessions per CT Art. 142; exoneración per pre-registered resolution. D. 96-2012 + D. 54-96 unacquired (LEADs — amounts evidenced only here) | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` | 29_ pp.50-56, 66 (EV29:EVID-098) |
| LB-008 | Ayuda DJ ISR PJ + Activo Neto + AS código 103 (30_, print Febrero 2026), Sección A: contador — "esta información es obligatoria para presentar la declaración"; ingresos — "únicamente los ingresos a los cuales les aplique la tarifa del artículo 22 literal a) y 22-A [...] en caso de que en una misma línea de ingreso registren ingresos gravables con art. 22 y no gravables por estar sujetos a otra norma, estos deberán excluirse [...] e informarlos en la sección B"; "Si no selecciona el concepto de ingresos, no podrá continuar"; líneas "gravadas con tarifa 15% de ISV [...] 18% [...] (Exportaciones)" con "Ventas brutas" y "Rebajas, descuentos y devoluciones" → "ventas netas anuales"; costos comerciales y de producción (materia prima local/importada, mano de obra directa/indirecta, GIF, inventarios en proceso/terminados); regla proporcional — "deberá consignar únicamente en esta sección la proporción deducible"; depreciación incl. "Depreciación de la revaluación de propiedades, planta y equipo"; arrastre de pérdidas ≤ 50% de la RNG actual validado por resolución; donaciones bloqueadas sin constancia fiscal; selector 22-A por ingreso bruto del año anterior > L1,000,000,000 | Ayuda 103 §A: accountant data unconditionally obligatory; only Art. 22.a/22-A-tariff income enters A (other-norm income → B); income-concept selection is a hard gate; revenue split by ISV rate (15/18/export), gross − rebates/discounts/returns → net annual sales; commercial vs manufacturing costing blocks; shared expense lines carry only the deductible proportion; depreciation includes a revaluation line; loss carryforward capped at 50% of current RNG and resolución-gated; donations require fiscal constancia; 22-A branch keyed to prior-year gross > L1B | `hn/sources/30_Ayuda_ISR_PJ_activo_net_codigo103.pdf` | 30_ pp.9-31 (EV29:EVID-099) |
| LB-009 | 30_, secciones 1.2.3-1.2.4: AS — "Esta sección se muestra autocompletada por el sistema, aplicando el 5% sobre el exceso de un millón de lempiras (1,000,0000.00) [sic] de la Renta Neta Gravable"; ATN — "el sistema determina el Total activo gravable, y realiza el cálculo considerando el importe exonerado de los L3,000,000.00"; floor/credit — "Cuando el valor determinado en Activo neto sea superior al valor calculado en Impuesto Sobre la Renta y Aportación Solidaria, lo determinado en [...] Aportación Solidaria constituirá un crédito al determinar el Impuesto a pagar por Activo Neto"; autofill — "a partir del periodo fiscal 202401 la información necesaria para la determinación del Impuesto Activo Total Neto será autocompletada del Informe de Estado de Situación Financiera [...] solamente deberá validar los valores informados"; pre-202401: consignación manual | 30_ §C-D: AS system-computed at 5% of the RNG excess over L1,000,000; ATN computed on total taxable assets (gross − provisions/accumulated depreciation) with a L3,000,000 exemption; when ATN exceeds ISR+AS, the pair is a credit against the ATN payable; from period 202401 ATN inputs autofill from the 535 EEFF report (validation-only UX); earlier periods consigned manually. The ATN RATE is never printed in 30_ — pinned only by 74_ p.10 (R-H29) | `hn/sources/30_Ayuda_ISR_PJ_activo_net_codigo103.pdf` | 30_ pp.44-48 (EV29:EVID-100) |
| LB-010 | 30_, secciones 1.2.2/1.2.5: GC links — "En caso de existir una Declaración 119 [...] o una Declaración 120 [...], el valor correspondiente se vinculará automáticamente en esta sección y no podrá ser editado"; DMR 113 — "los montos provenientes de la DMR 113 – Retención por Dividendos o Utilidades Distribuidas se vincularán de forma automática en la casilla 'Dividendos y participación de utilidades', la cual permanecerá editable"; créditos per-tax autocompletados de la cuenta corriente; DMR 112 vinculada (editable); anticipo 1% — "deberá agregar el valor correspondiente según los comprobantes de retención"; validación — "de tener créditos por estas dos retenciones usted debe consignar la fuente de los ingresos que las originan de lo contrario no le permitirá avanzar"; B extras: "Ganancias por Mediciones o por Ajustes a Valor Razonable" (inversiones corrientes/no corrientes, propiedades de inversión, activos biológicos, activos no corrientes mantenidos para la venta), "premios de lotería y ventas netas de activos"; 535 prerequisito FY2024+ | 30_ §B/E: 119/120 values hard-linked read-only; the DMR-113 dividend base soft-linked editable; per-tax credit subpanels (ISR/AS/ATN) fed by the current account with editable retention legs (112 per comprobantes; import advance); the source-of-income validation blocks progress when retention credits lack their originating income; B adds NIIF fair-value gains and lottery/asset-sale informative lines; 535-before-103 sequencing FY2024+ | `hn/sources/30_Ayuda_ISR_PJ_activo_net_codigo103.pdf` | 30_ pp.32-53, 64 (EV29:EVID-101) |
| LB-011 | Generalidades ISR (68_) + Generalidades 30-Abril (74_, print Junio 2026): 22.a PJ 25%; 22.b PN progresiva IPC "a partir del año 2017" (escala FY2025 en 74_ = IMAGEN); 22.c transporte presunto 10%; 22-A evolución fechada: FY2018 gross >L300M → 1.5% (sectores 0.75%); FY2019 L300-600M → 0.75%, >L600M → "el 1% [...] resultaren menores al uno por ciento (1.05%) [sic]" (sectores 0.5%); FY2020+ ≤L1,000M no sujetos, >L1,000M → 1% (sectores 0.5%, previa comunicación a la AT); exclusiones num. 4; paquete 30-abril (74_ RESUMEN): 535 + 102 + 103 + AS + ATN + GC 119 + TP 545 + 506 + 107; 535 gate — "siendo ambos formularios una misma obligación, por lo que, la no presentación del Informe dará lugar al incumplimiento"; AS — "Las personas jurídicas, excepto las incluidas en los Regímenes Especiales de Exportación y de Turismo [...] pagarán una Aportación Solidaria del 5% [...] a partir del período fiscal 2014 en adelante. La Aportación Solidaria constituye una sobretasa del Impuesto Sobre la Renta, por lo que no será deducible [...] sujeta al Régimen de Pagos a Cuenta"; ATN 1% anclado en "Capítulo II del Decreto Legislativo No.51-2003" (conflicto con LET Art. 7) | 68_/74_: the Art. 22/22-A dated evolution behind R-H32 (22-A regimes consumed from taxation/03 by id; PN scale prints IMAGE-ONLY — consume the taxation CSV); the Apr-30 package membership (9 obligations); the 535 same-obligation gate FY2024+ with the pre-2024 omisa/rectificativa carve-out; AS = 5% over the RNG excess of L1M, PJ-only, Exportación/Turismo excluded, from FY2014, a non-deductible ISR surtax under the pagos-a-cuenta regime; the ATN 1% pinned only here (R-H29), instrument conflict open (74_ OQ-3) | `hn/sources/68_Generalidades_ISR.pdf` + `hn/sources/74_Generalidades_vence_30abril.pdf` | 68_ pp.4-9; 74_ pp.3-11 (EV29:EVID-109/110) |
| LB-012 | Escrito 75_ "NOTIFICACIÓN DE SUSPENSIÓN DE OBLIGACIONES ISR PERSONA NATURAL (QUE NO SUPERAN EL MÍNIMO EXENTO)": comparecencia "en mi condición ( Personal, Representante, Apoderado Legal )"; DNI + RTN; "presentando notificación de suspensión de obligaciones ISR persona natural por no superar el mínimo exento del período fiscal"; adjuntos — "Fotocopia de los documentos fiscales emitidos que respaldan el nivel de ingresos percibidos durante el período fiscal. (Si aplica) / Original de los documentos fiscales (Para cotejar). Aplica únicamente si lo notifica de forma presencial. / Formulario de notificación de documentos no utilizados. (Si aplica)"; nota — "La notificación debe corresponder al período fiscal ya finalizado. Por ejemplo, para el período fiscal 2025, la notificación debe presentarse entre el 01 de enero al 30 de abril, 2026" | The 75_ suspension petition: a PN whose income did not exceed the IPC-indexed exempt minimum notifies SAR to suspend ISR obligations for an ALREADY-CLOSED fiscal year, filed 1-Jan→30-Apr of the following year, personally or via representative/attorney (DNI + RTN), with the attachment checklist (photocopies of fiscal documents; originals for in-person cotejo; unused-documents form); effect scope and recurrence NOT stated (75_ OQ-1/3); the mínimo exento amount is NOT printed (75_ OQ-2) | `hn/sources/75_Escrito_suspension_ISR_PN.pdf` | 75_ p.1 (EV29:EVID-110) |
| LB-013 | Ayuda family (29_/30_ et al., consolidated): "Única modalidad para la presentación a través de la Oficina Virtual (OVI)"; rectificativa per "Artículo No.117 del Decreto No.170-2016 contentivo del Código Tributario" — "los valores originales aparecerán tachados"; estado "Rectificativa OT Aprobada OT"; acuse "con [...] el código único de este y su respectivo QR"; Boletín de Pago "con una fecha de caducidad" | The annual family's OVI chassis evidence: OVI the only channel; rectificativa framed by CT Art. 117 with side-by-side strikethrough; declaration states; acuse with unique code + QR; payment slip with expiry — the chassis CONTRACT is owned by fiscal-reporting file 01 (F1) and consumed by id | `hn/sources/29_Ayuda_ISR_PN_codigo102.pdf` + `hn/sources/30_Ayuda_ISR_PJ_activo_net_codigo103.pdf` | 29_ pp.7-8, 57-65; 30_ pp.5, 56-62 (EV29:EVID-091) |
| LB-014 | Ley ISR (D.L. 25-1963 consolidada SAR-07-2025), Arts. 27-28: período anual 1-ene→31-dic; DJ anual del 1-ene al 30-abr; exenciones de presentación (PN ≤ banda exenta Art. 22.b; asalariados de única fuente plenamente retenidos) — statutory anchor as restated by 29_ p.9 ("Según artículos 27 y 28 de la Ley"); the filing-exemption FLAG is owned by taxation/04 FR-136 (composite gate FR-135, R-H9) | ISR Arts. 27-28: the annual period and the Jan-1→Apr-30 window (statutory anchor behind LB-001); filing exemptions consumed from `../taxation/04_isr-withholding.md` by id — never restated here | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 27-28 (as restated 29_ p.9, EV29:EVID-092; flag = taxation/04 FR-135..136) |
| LB-015 | **D. 54-96 ORIGINAL (W6, `118_`)** — Ley de Equidad Tributaria e Incentivos al Empleo, G 27,941 26-abr-1996 (Dado/Ejecútese/vigencia per print, EVID-427): Art. 2 "INCENTIVOS AL EMPLEO" — the job-creation fiscal credit (10%/25% crédito fiscal fractions keyed to permanent-new-job counts, ≥5-job gate; still visible in the modern 102 form's "Crédito por generación de nuevos empleos" line) + reformed Ley ISR Art. 10 (renta bruta + ganancias de capital 10% único), Art. 22-b PN brackets, Art. 23 L50,000 exempt floor, Art. 5-6 derogations (D. 138-94 = CAFICULTURA law — NOT an ISR-law citation, prompt-discrepancy flag EVID-428) | The FIRST Equidad Tributaria (ancestor of the queued D. 51-2003) now in corpus: the FR-244 job-credit gate/amounts trace to statute (not just the EV29 print); the 1996 ISR snapshot (brackets/floors) is HISTORICAL config feeding the ISR-law lineage (D.L. 25-1963 chain); D. 138-94 identity flag prevents a caficultura-law mis-citation. | `hn/sources/118_Gaceta_27941_Decreto_54-96_reformas_tributarias.pdf` | 54-96-Art. 1-6 + signatures (pp.1-2) (EV115:EVID-427; EV115:EVID-428) |

## 3. Functional Requirements

### 3.1 Package chassis: the 30-abril window and the annual objects

- **HN-FREP-FR-221:** The system shall schedule the annual-close package
  obligations with the window row 1-January→30-April of the year following
  the declared fiscal period, shifting to the next business day when
  April-30 falls non-hábil ("del uno de enero al treinta de abril o
  siguiente día hábil"), and shall extend the window by three months for
  AT-authorized special-fiscal-period taxpayers, consuming the
  special-period close date from taxation/01 FR-016 by id — window rows
  stored as DATED per-FY rows (D-H2), never a rolling computation.
  (LB-001; LB-014; EV29:EVID-092; EV29:EVID-110)
- **HN-FREP-FR-222:** The system shall implement código 103 as ONE
  declaration liquidating THREE taxes — ISR (Art. 22.a / 22-A comparator),
  Aportación Solidaria (FR-255) and Activo Total Neto (FR-257) — with the
  per-tax credit subpanels and resumen branch of FR-253; AS and ATN shall
  not be filable as separate declarations.
  (LB-009; LB-010; EV29:EVID-100/101/110)
- **HN-FREP-FR-223:** The system shall implement código 102 as the
  determinativa annual ISR declaration for personas naturales — subjects
  per Art. 2 (domiciled/resident, incl. State concessionaires), filed
  personally or via mandatario/representante legal, on the calendar FY
  (special FY only with prior written SAR notice, taxation/01 FR-016 by
  id) — and código 103 as its persona-jurídica counterpart (contador data
  unconditionally obligatory, FR-227). (LB-001; LB-008;
  EV29:EVID-092/099)
- **HN-FREP-FR-224:** The system shall consume the OVI/SW declaration
  chassis — state machine (borrador → Original OT. Aprobada OT →
  Rectificativa/Rectificada OT → rechazada), acuse with unique code + QR,
  boletín with expiry, CT-Art. 117 rectificativa flow — from
  fiscal-reporting file 01 (cluster F1) BY ID, with zero re-derivation in
  this file. (LB-013; EV29:EVID-091)
- **HN-FREP-FR-225:** The system shall write-protect every filed 102/103
  record (D-H2.5 freeze): after juramento/acuse, values are immutable; a
  rectificativa creates a NEW record from a snapshot of the original
  (side-by-side presentation with the original values struck through),
  leaving the original's filed values untouched. (LB-013; EV29:EVID-091)

### 3.2 Form 102 — Sección A (computation)

- **HN-FREP-FR-226:** The system shall implement the 102 four-section
  layout — A Cálculo del ISR, B Datos informativos de carácter tributario,
  C Créditos, D Resumen — with utilidad (ingresos − gastos) and RNG
  auto-computed by the form engine, the D summary (ISR, créditos,
  impuesto a pagar) auto-generated from A and C, and the informative
  window detailing normal/special fiscal periods and fiscal benefits
  applied; Sección B values shall never affect the tax computation.
  (LB-002; EV29:EVID-095)
- **HN-FREP-FR-227:** The system shall require the accountant block
  (name, RTN of exactly 14 positions, colegiación number) on 102 ONLY for
  personas naturales declared Comerciante Individual; on 103 the block is
  unconditionally required to present. (LB-002; LB-008;
  EV29:EVID-095/099)
- **HN-FREP-FR-228:** The system shall implement the 102 income taxonomy
  as the printed nine concepts (sueldos/salarios+bonificaciones;
  actividades mercantiles; servicios; alquileres; intereses no bancarios;
  otros ingresos gravables; actividades del Artículo 20; honorarios
  profesionales; ajuste TP positivo) each with its fixed subaccount menu,
  and shall render the Art. 20 selector as an economic-activity dropdown
  limited to agropecuaria, agroindustrial, manufacturera, minera and
  turismo; the Art. 20 regime mechanics (thresholds/treatment) are NOT
  pinned by the print and stay OQ-gated — never guessed. Rental income
  lines carry the D. 17-2010 Art. 5 cedular-management note with rates
  consumed from taxation/05 by id. (LB-003; EV29:EVID-096; OQ-016)
- **HN-FREP-FR-229:** The system shall mirror the expense taxonomy (nine
  concepts incl. sueldos y salarios, honorarios profesionales — resident
  and non-resident — depreciation, amortization, interest, costo de
  ventas, otros) with the printed subaccount menus — AFP quotas,
  professional-college quotas, jubilation/pension quotas and
  "Cotizaciones RAP 1,5%" as salary-cost subaccounts (payroll posting
  semantics = S-HN4 `../payroll/`, consumer note only).
  (LB-003; EV29:EVID-096; EV29:EVID-093)
- **HN-FREP-FR-230:** The system shall carry transfer-pricing adjustment
  lines on 102 as SIGNED annual lines — positive ajuste in the income
  panel, negative ajuste in the expense panel — whose amounts consume the
  Ajuste PT auto-migration into the ISR DJ base owned by
  fiscal-reporting file 10 (cluster F10) by id; this file owns only the
  line placement, never the adjustment computation.
  (LB-003; EV29:EVID-096)
- **HN-FREP-FR-231:** The system shall compute 102 ISR using the PN
  progressive engine and the per-FY scale vintages consumed BY ID from
  `../taxation/04_isr-withholding.md` (HN-TAX-FR-121..125) seeded in
  `../taxation/isr_brackets.csv` (sar_020_2022 … sar_01_2026) — the
  Ayudas print the scale as IMAGE ONLY (68_ p.4; 74_ p.7 FY2025), so no
  bracket value is ever restated, re-derived or transcribed here; a
  missing FY vintage is a config gap (never-guess, D-H2).
  (LB-001; LB-011; EV29:EVID-092/109/110; OQ-007)
- **HN-FREP-FR-232:** The system shall auto-apply the PN deduction stack
  on 102 — L40,000 education/medical; L80,000 for age ≥ 65 (D. 59-2020);
  profession/office costs; farmer/rancher production costs; donations
  capped at 10% of RNG — with all deductibility semantics, gates and the
  senior stack components consumed from taxation/02 (HN-TAX-FR-046..078)
  by id; the form engine only orders the auto computation (utilidad →
  RNG → deducciones). (LB-004; EV29:EVID-094)
- **HN-FREP-FR-233:** The system shall implement the printed form hooks
  that auto-grant the senior deductions "Artículo 30, numeral 14 Decreto
  (199-2006)" and the renta-bruta exclusion "Art.14 Decreto (194-2002)"
  where applicable — encoding the HOOKS only: the amounts (L30,000@60,
  65+ ≤ L350,000) are NOT restated in 29_ and are consumed from
  taxation/02 by id; the 29_ citation itself is garbled (29_ OQ-1) and
  both statutes are unacquired LEADs — the hooks never assert decree
  content beyond the print. (LB-004; EV29:EVID-094; OQ-001)
- **HN-FREP-FR-234:** The system shall gate AFP-contribution
  deductibility on 102/103 payroll-cost lines: deductible only when
  (a) not withdrawn within the reported fiscal year, (b) CNBS-regulated
  and (c) maintained in Honduran institutions; the cited Reglamento
  Arts. 19/51 ("Acuerdo N°799") is unacquired — LEAD, the gate stands on
  the printed contract. (LB-003; EV29:EVID-096; OQ-014)

### 3.3 Sección B — vinculación, no-gravados, disclosure blocks

- **HN-FREP-FR-235:** The system shall implement the 102 no-gravados
  subledger with the printed renta-fuente-hondureña catalog — bank
  interests (D. 110-93 Art. 9, sujetos al 10% — **ACQUIRED W6 as `117_`,
  EVID-426: the intereses block is FULL verbatim in corpus, STILL cited
  live by 35_/71_; the L50,000 savings-exemption monto of its Art. 12 is
  now statutory — see fiscal-reporting/02 FR-073**), seguros,
  herencias/legados/donaciones, rentas de títulos valores
  (State/districts/municipalities), subvenciones/subsidios, otras rentas
  no gravadas, otros ingresos del exterior — plus the vinculación-fed
  lines of FR-236; lotería prizes classify as ganancias de capital per
  Reglamento Art. 32 while national-lottery prizes stay exempt per
  Reglamento Art. 18 (both citations unacquired — flag-only).
  (LB-006; EV29:EVID-097; EV115:EVID-426; OQ-014 partial)
- **HN-FREP-FR-236:** The system shall implement the vinculación engine
  on 102: the enabled cross-declaration casillas (dividendos y
  participación de utilidades; ganancias de capital; ganancias de capital
  ZOLITUR; impuesto cedular por alquiler habitacional) auto-flow the
  LINKED declaration's taxable base into Sección B no-gravados ONLY when
  the linked tax is both DECLARED AND PAID — a hard prerequisite check
  against the cuenta corriente before any base flows (populating without
  the precondition is blocked); the dividend base variant on 103 is the
  FR-237 DMR-113 editable link. (LB-006; LB-010; EV29:EVID-097/101)
- **HN-FREP-FR-237:** The system shall implement the 103 hard/soft link
  split: código 119 and código 120 values that exist vinculan
  automatically into Sección B and CANNOT be edited (read-only), while
  the DMR-113 (retención por dividendos) amounts pre-fill the
  "Dividendos y participación de utilidades" casilla and REMAIN editable;
  when 120 must be filed first, its cadence is owned by file 08 (47_
  OQ-3 pointer) — this file blocks 103 completion on an unpaid linked
  119/120 rather than resolving the cadence. (LB-010; EV29:EVID-101;
  OQ-006)
- **HN-FREP-FR-238:** The system shall implement the Sección B
  informative blocks on both forms without any computation effect:
  non-deductible-expense tagging (Art. 12 list per the print — incl.
  pro-seguridad-populacional contributions, multas, related-party
  interest) and the related-party disclosure cube (four operation types ×
  three counterparty zones, per the printed matrices); the vinculación
  CRITERIA themselves (participation percentages) are image-only in 74_
  p.15 (Reglamento Arts. 11-13 LEAD) and are consumed, never transcribed.
  (LB-002; LB-006; LB-011; EV29:EVID-095/097/110; OQ-009)
- **HN-FREP-FR-239:** The system shall implement the empleados block
  (per-period headcount movement, including new employees and new
  employees with disability as separate counters) as the SOLE feed of the
  FR-244 job-credit gate; the payroll-side semantics of those counts
  (hires vs starts) and the Art. 10 exclusion mechanics of EVID-093
  (13th/14th month up to 10 SMM promedio, IHSS, prestaciones) belong to
  S-HN4 `../payroll/` and are consumed there by id — this file stores
  the counters, never derives them from payslips.
  (LB-005; LB-006; LB-007; EV29:EVID-093/097/098)
- **HN-FREP-FR-240:** The system shall implement the 103-only Sección B
  informative cards: premios de lotería, ventas netas de activos,
  donaciones (exteriores/locales), otras rentas no gravables, and the
  "Ganancias por Mediciones o por Ajustes a Valor Razonable" panel over
  the five NIIF classes (inversiones corrientes/no corrientes,
  propiedades de inversión, activos biológicos, activos no corrientes
  mantenidos para la venta). (LB-010; EV29:EVID-101)

### 3.4 Sección C — the credit panel (102) and subpanels (103)

- **HN-FREP-FR-241:** The system shall implement the 102 credit panel
  with the printed fourteen lines (pagos realizados; excedente del
  período anterior; cesiones de crédito; importe a compensar; créditos
  aplicados a pagos a cuenta; pagos a cuenta; créditos aplicados a
  anticipos 1%; anticipos 1% ISR; retención asalariados; retención
  Art. 50; retención anticipo 1% Art. 19 D. 17-2010; retención anticipo
  importaciones; crédito por nuevos empleos; importe por exoneración o
  reducción) — every line derived from the taxpayer's cuenta corriente
  (ledger contract consumed from taxation/01 FR-036 by id).
  (LB-007; EV29:EVID-098)
- **HN-FREP-FR-242:** The system shall auto-populate the retention
  credit lines from the retaining agents' informativas — asalariados
  (código 111, from the patrono's informativa), Art. 50 (código 112) and
  anticipo 1% (código 135) — consuming the record data shape from
  taxation/04 FR-153 by id and the DJIMR linkage from fiscal-reporting
  file 02 (cluster F2) by id, and shall run the comprobante-vs-form
  mismatch check (Recomendación 8): retained amounts supported by a
  constancia but absent from the informativa are flagged for
  reconciliation, never silently credited. (LB-007; EV29:EVID-098)
- **HN-FREP-FR-243:** The system shall implement the D. 96-2012 anticipo
  legs as evidenced by the print: (a) the 1%-of-declared-gross ANTICIPO
  applies to naturales/jurídicas that, within non-prescribed fiscal
  periods, had operating losses in TWO consecutive or alternate years AND
  obtained last-FY gross income ≥ L100,000,000; (b) the import advance =
  3% of ISR applied on the referential CIF base of goods imports; D.
  96-2012 itself is unacquired (LEAD) — amounts and gates stand on the
  EV29 print only, and the loss-pattern flag is consumed from taxation/03
  FR-086 by id. (LB-007; EV29:EVID-098; OQ-014)
- **HN-FREP-FR-244:** The system shall unlock the "Crédito por
  generación de nuevos empleos" (D. 54-96) line ONLY when the Sección B
  counters for new employees and new employees with disability,
  separately or jointly, sum to five or more; below five the line stays
  disabled. **W6: D. 54-96 acquired as `118_` (Ley de Equidad Tributaria
  e Incentivos al Empleo, G 27,941 26-abr-1996) — its Art. 2 statutory
  credit rows (10%/25% fiscal-credit fractions keyed to job counts) load
  as dated config per LB-015; the never-guess gate on any amount NOT in
  the statute row stays.** (LB-007; LB-015; EV29:EVID-098;
  EV115:EVID-428; OQ-014 partial)
- **HN-FREP-FR-245:** The system shall implement cesiones de crédito on
  the credit panels exclusively through the CT Art. 142 assignment gates
  consumed from taxation/01 FR-039 by id (credits liquid, exigible,
  non-prescribed), and the exoneración/reducción import line ONLY for
  taxpayers holding a registered exoneración resolution for the exact
  impuesto and período presented (amount entry gated on the resolution
  record). (LB-007; LB-010; EV29:EVID-098/101)

### 3.5 Form 103 — Sección A (computation)

- **HN-FREP-FR-246:** The system shall enforce the 103 income-concept
  gate — presentation is blocked until a revenue concept is selected
  ("Si no selecciona el concepto de ingresos, no podrá continuar") — and
  the A/B split rule: Sección A carries ONLY income subject to the
  Art. 22.a or 22-A tariffs; income covered by another norm (exempt,
  cedular, GC, etc.) is EXCLUDED from A and informed in Sección B
  (feeding FR-236/240). (LB-008; EV29:EVID-099)
- **HN-FREP-FR-247:** The system shall implement the 103 revenue panel
  split by ISV rate — Ventas y/o servicios netos locales gravadas con
  tarifa 15% de ISV; ídem 18%; Ventas y/o servicios (Exportaciones) —
  each line captured as Ventas brutas minus Rebajas, descuentos y
  devoluciones with ventas netas anuales computed by the engine, plus
  free-form "Otras rentas gravables" cards; ISV rate semantics are
  consumed from taxation/06 by id (no rate re-derivation here).
  (LB-008; EV29:EVID-099)
- **HN-FREP-FR-248:** The system shall implement both costing blocks:
  costo de ventas comercial (inventario inicial de bienes; compras brutas
  locales; compras por importaciones; descuentos y devoluciones de
  compras; inventario final) and costo de producción y ventas (materia
  prima local/importada with inventories; mano de obra directa e
  indirecta; gastos indirectos de fabricación; inventarios en proceso y
  terminados). (LB-008; EV29:EVID-099)
- **HN-FREP-FR-249:** The system shall implement the gastos operativos
  catalog (comisiones de ventas; sueldos y salarios; honorarios
  profesionales y dietas; honorarios a extranjeros por servicios
  ocasionales; arrendamientos; mantenimiento y reparaciones; publicidad y
  propaganda; vigilancia; etc.) with the proportional rule — a shared
  line carrying deductible and non-deductible proportions consigns ONLY
  the deductible proportion in A (the remainder tagged in B) — and the
  depreciation/amortization family including the dedicated
  "Depreciación de la revaluación de propiedades, planta y equipo" line
  (revaluation event = file 08 código 154, by id).
  (LB-008; EV29:EVID-099)
- **HN-FREP-FR-250:** The system shall gate the loss carryforward on
  103: the absorbed loss amount may not exceed 50% of the current-year
  RNG, AND the carryforward is valid only where validated by resolution
  (the print's resolución/RTN-validated gate); the underlying NOL
  semantics (3-year/50%/same-activity) are owned by taxation/02 by id —
  this file encodes only the form-side validator, with the sparse-print
  mechanics carried as OQ. (LB-008; EV29:EVID-099; OQ-015)
- **HN-FREP-FR-251:** The system shall block donation deductions on 103
  where no fiscal constancia supports them (server-side gate per the
  print); the 10%-of-RNG cap semantics are consumed from taxation/02 by
  id. (LB-008; EV29:EVID-099)
- **HN-FREP-FR-252:** The system shall implement the 103 tariff selector
  — Art. 22 literal a), the 22-A branch, and the printed "Literal c)"
  third option (foreign-transport presumed base) — with the 22-A branch
  keyed to PRIOR-year gross income > L1,000,000,000 for post-2020
  periods and the THREE dated regimes, comparator engine, sector
  reductions and exclusions consumed BY ID from taxation/03
  (HN-TAX-FR-081..092, R-H32); the "Literal c)" label is a print defect
  (30_ OQ-2 — never encoded as a PJ rate), and the FY2019 "(1.05%)"
  figure is never seeded (1% text-primary, R-H32).
  (LB-008; LB-011; EV29:EVID-099/109; OQ-003; OQ-008)
- **HN-FREP-FR-253:** The system shall implement the 103 per-tax credit
  subpanels (ISR / AS / ATN) auto-filled from the cuenta corriente with
  the editable legs: DMR-112 values link into "Retención Art. 50"
  (editable), the anticipo-1% line is completed per retention
  comprobantes, and the import advance is editable; the exoneración line
  requires the registered resolution (FR-245); and the source-of-income
  validation BLOCKS advance whenever Art. 50 / anticipo-1% credits exist
  without the income source that originated them consigned.
  (LB-010; EV29:EVID-101)

### 3.6 The 535 prerequisite gate

- **HN-FREP-FR-254:** The system shall gate 103 (FY2024+) on the prior
  presentation of the 535 Informe de Estado de Situación Financiera —
  both being "una misma obligación", so a missing 535 constitutes
  non-compliance of the DJ itself — with the pre-2024 carve-out: the
  informe is not required for omisa or rectificativa declarations of
  periods before FY2024; gate internals, PJ/Comerciante-Individual
  subject scope and the EEFF panel contract are consumed from
  fiscal-reporting file 06 (cluster F6) by id. (LB-010; LB-011;
  EV29:EVID-101/110)

### 3.7 Aportación Solidaria (AS)

- **HN-FREP-FR-255:** The system shall compute AS as a system-completed
  section: AS = 5% × max(0, RNG − L1,000,000), applicable from período
  fiscal 2014 onward (dated parameter row), encoded as a SOBRETASA del
  ISR — non-deductible for ISR and subject to the pagos-a-cuenta regime,
  annual declaration and the ISR's demás disposiciones (credit subpanel
  and floor interaction per FR-258). (LB-009; LB-011;
  EV29:EVID-100/110; R-H30)
- **HN-FREP-FR-256:** The system shall scope AS to personas jurídicas
  only — 102 (persona natural) carries NO AS section and 74_ p.9 says
  "Las personas jurídicas" — and shall exclude taxpayers under the
  Regímenes Especiales de Exportación y de Turismo per 74_ p.9 ONLY (the
  exclusion appears in NO other print — 30_ Feb-2026 omits it; cross-doc
  CONFIG dependency carried, never silently generalized).
  (LB-009; LB-011; EV29:EVID-100/110; OQ-004; R-H30)

### 3.8 Activo Total Neto (ATN)

- **HN-FREP-FR-257:** The system shall compute ATN on 103 as: rate 1%
  (pinned ONLY by 74_ p.10 per R-H29) applied over total activos
  gravables (gross taxable assets reduced by provisiones, depreciaciones
  acumuladas y otros) minus the L3,000,000 exemption — with the
  instrument conflict (D. 51-2003 Capítulo II per 74_ vs Ley de Equidad
  Tributaria Art. 7 per the corpus lead) carried OPEN as 74_ OQ-3: the
  1%/L3M parameters ship as dated config rows standing on R-H29, the
  instrument identity is NEVER asserted, and acquiring D. 51-2003 is the
  resolving lead. (LB-009; LB-011; EV29:EVID-100/110; OQ-010; R-H29)
- **HN-FREP-FR-258:** The system shall implement the ATN floor-tax
  credit: where the determined ATN exceeds the ISR + AS determined
  values, the ATN payable = ATN − (ISR + AS) (the pair constituting a
  credit against ATN); where ATN is equal or lower, NO ATN payable is
  determined and the ISR + AS values stand (credit display only).
  (LB-009; EV29:EVID-100)
- **HN-FREP-FR-259:** The system shall autofill the ATN inputs from the
  535 EEFF report (activos gravables; depreciaciones, amortizaciones y
  deterioro) for periods from 202401, rendering the section
  validation-only ("solamente deberá validar los valores informados");
  for periods before 202401 the taxpayer consigns total activos
  gravables and total provisiones/depreciaciones acumuladas y otros
  manually. (LB-009; EV29:EVID-100)

### 3.9 The 75_ PN minimum-exempt suspension escrito

- **HN-FREP-FR-260:** The system shall implement the suspension petition
  wizard: only for an ALREADY-FINALIZED fiscal period (window
  1-January→30-April of the following year — FY2025 example:
  01-ene→30-abr-2026), with filer identity (name, DNI, RTN), role
  selector (Personal / Representante / Apoderado Legal), petition text
  ("pido: admitir [...] tener como notificado y en definitiva resolver
  de conformidad") and the attachment checklist — photocopies of issued
  fiscal documents supporting the income level (if applicable);
  ORIGINALS for cotejo only when filed in person; the unused-documents
  notification form (if applicable). (LB-012; EV29:EVID-110)
- **HN-FREP-FR-261:** The system shall resolve the "mínimo exento"
  threshold from the SCALE FAMILY by id: the first-band exempt ceiling of
  the FY's PN vintage in `../taxation/isr_brackets.csv` (e.g. FY2025 =
  L217,493.16) — the amount is printed NOWHERE in 75_ (75_ OQ-2) and is
  never a hardcoded constant; the wizard compares the declared income
  level against the resolved threshold. (LB-012; LB-011;
  EV29:EVID-110; OQ-012)
- **HN-FREP-FR-262:** The system shall encode the suspension as a
  REQUEST with unpinned effect: no RTN-status change, no obligation-state
  mutation and no informativa-suppression is encoded anywhere (effect
  scope = 75_ OQ-1; recurrence/persona-turnover, incl. re-notification
  per year and the named-addressee turnover = 75_ OQ-3) — the record is
  a petition document with status tracking only.
  (LB-012; EV29:EVID-110; OQ-011; OQ-013)

### 3.10 Package roll-up and the 102 obligation gate

- **HN-FREP-FR-263:** The system shall render the annual-close
  compliance dashboard for the Apr-30 family — 102/103/AS/ATN (this
  file), 535 (file 06), DJ anual GC 119 + Boletín de Pago Libre 119
  (file 08), TP 545 (file 10), contribuciones 506 cooperative and 107
  educativas (file 11) — as DATED window rows on one calendar (FR-221),
  with per-member state consumed from each owner file by id; this file
  owns only the roll-up view. (LB-011; EV29:EVID-110)
- **HN-FREP-FR-264:** The system shall gate the 102 obligation on the
  filing-exemption flag consumed from taxation/04 FR-136 by id — PN with
  gross ≤ the Art. 22.b exempt band, and single-source asalariados fully
  satisfied by withholding (composite gate FR-135, R-H9) — and shall
  offer the FR-260 suspension petition as the sub-mínimo PN's compliance
  path (declaration suppressed + petition tracked), never auto-filing a
  102 for a sub-mínimo PN without an explicit choice.
  (LB-014; LB-012; EV29:EVID-110/092)

## 4. Data Model

Machine-readable sidecars: none of this file's own — the PN scale vintages
are consumed from `../taxation/isr_brackets.csv` by id. Dated parameters
are additive `valid_from`/`valid_to` rows (D-H2) resolved by the declared
period, snapshot-on-write (D15).

**Annual declaration objects (código 102 / 103):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.annual.declaration (new) | código · fiscal_year · special_period · state · accountant_name / accountant_rtn(14) / colegiación | select(102·103)/year/boolean/select/char | state per file-01 chassis (borrador → Original OT. Aprobada OT → Rectificativa…); contador gate: 102 = Comerciante Individual only, 103 = always | FR-223, FR-225..227 |
| l10n_hn.annual.declaration.line (new) | declaration_id · section(a·b·c·d) · concept · subaccount · amount · tp_signed | m2o/select/char/char/monetary/boolean | concepts = the printed 9+9 catalogs (102) / A-blocks (103); tp_signed places ajuste + (ingresos) / − (gastos) | FR-228..230, FR-247..249 |
| l10n_hn.annual.declaration | art20_activity | select | agropecuaria · agroindustrial · manufacturera · minera · turismo (mechanics OQ-gated) | FR-228, OQ-016 |
| l10n_hn.annual.declaration | isv_class (revenue lines) | select | local_15 · local_18 · export · otras (net = brutas − rebajas/descuentos/devoluciones) | FR-247 |
| l10n_hn.annual.declaration | loss_carryforward_amount · loss_carryforward_capped · resolución_ref | monetary/computed/char | capped ≤ 50% × current RNG; blocked without resolución | FR-250 |
| l10n_hn.annual.declaration | tariff_selector | select | art_22_a · art_22_a_minimum_22A · transport_presumed ("Literal c)" = print-defect label only) | FR-252, OQ-003 |

**Sección B — vinculación / no-gravados / empleados:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.annual.nogravado.line (new) | declaration_id · rule · amount · source_link | m2o/select/monetary/m2o | rule per LB-006 catalog (bank_110_93 · seguros · herencias · titulos_valores · subvenciones · otras · exterior · dividends · gc · gc_zolitur · cedular) | FR-235, FR-236 |
| l10n_hn.declaration.vinculo (new) | declaration_id · linked_código(113·119·120·cedular·136) · linked_declaration_id · declared_and_paid (constraint) · base_flowed | m2o/select/m2o/boolean/monetary | base flows into no-gravados only when declared AND paid (cuenta corriente check) | FR-236, FR-237 |
| l10n_hn.annual.declaration | empleados: headcount_initial/final · new_employees · new_employees_disability | integer | feeds FR-244 gate; derivation = S-HN4 consumer | FR-239, FR-244 |
| l10n_hn.relatedparty.disclosure (new) | declaration_id · op_type(4) · zone(3) · amount | m2o/select/select/monetary | informative cube; criteria consumed (74_ p.15 image — Reglamento 11-13 LEAD) | FR-238, OQ-009 |

**Credit panels, AS/ATN, suspension:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.annual.credit.line (new) | declaration_id · panel(isr·as·atn) · line_key (14 printed keys) · amount · source(cuenta_corriente · agent_informativa · comprobante · resolution) · editable | m2o/select/char/monetary/select/boolean | read-only by default; editable legs: 103 DMR-112, anticipo-1% per comprobantes, import advance | FR-241..245, FR-253 |
| l10n_hn.annual.declaration | as_base_rng · as_excess = max(0, RNG−1,000,000) · as_amount (5%) | monetary/computed | dated row: as_rate 5% valid_from FY2014 | FR-255, FR-256 |
| l10n_hn.annual.declaration | atn_gross_assets · atn_provisions · atn_exemption (L3,000,000) · atn_rate (1%, R-H29) · atn_tax · atn_payable = max(0, atn − (isr+as)) · autofill_source_535 | monetary/computed/m2o | rate/exemption = dated config rows (instrument conflict open); autofill from 535 for period ≥ 202401 | FR-257..259 |
| l10n_hn.isr.pn.suspension (new) | fiscal_year · filed_on (01-ene→30-abr window) · role(personal·representante·apoderado) · dni · rtn · attachments(json) · status | year/date/select/char/char/json/select | request-character only; no RTN/obligation mutation | FR-260..262 |
| l10n_hn.annual.parameter (dated rows) | key · value · valid_from · valid_to · note | char/monetary/date/date/char | as_rate=5% (FY2014+); as_rng_floor=1,000,000; atn_rate=1%; atn_exemption=3,000,000; gate_535 (FY2024+); atn_autofill (202401+); window rows per FY (Apr-30/next-hábil; +3m special FY) | FR-221, FR-254..259 |

## 5. Odoo Mapping

Layer semantics: `odoo` = declaration data model, computation and
bookkeeping in the LGPL client; the SAR-side OVI/SW interaction (upload,
acuse reception, estado polling) is the chassis contract of
fiscal-reporting file 01 and is `n/a` here with that justification — this
file mirrors and prepares, never transmits. Models stable across Odoo
17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-221 | odoo | l10n_hn.annual.parameter + date.range | window rows | D12: per-FY dated rows (Apr-30 + next-hábil shift; +3m special-FY via taxation/01 FR-016 close date) |
| FR-222, FR-223 | odoo | l10n_hn.annual.declaration | código, fiscal_year, special_period | 103 computes ISR+AS+ATN in one object; 102 obligation gate per FR-264 |
| FR-224 | n/a (chassis = file 01) | — | — | OVI/SW transmission/state machine owned by fiscal-reporting file 01 by id; this file emits the payload only |
| FR-225 | odoo | l10n_hn.annual.declaration | state + snapshot fields | D-H2.5: states ≥ filed are read-only (ORM constraint); rectificativa = new record copying the snapshot |
| FR-226..234 | odoo | l10n_hn.annual.declaration.line + res.partner (contador) | concepts, subaccounts, art20_activity | Scale vintages consumed from `../taxation/isr_brackets.csv` via taxation/04 FR-121..125 by id (D15 snapshot of resolved band values); D. 199-2006/194-2002 hooks consume taxation/02 by id |
| FR-235..240 | odoo | l10n_hn.annual.nogravado.line + l10n_hn.declaration.vinculo + relatedparty.disclosure | declared_and_paid constraint | Prerequisite check hits the cuenta corriente mirror (taxation/01 FR-036); 119/120 read-only vs DMR-113 editable enforced on the link record |
| FR-241..245 | odoo | l10n_hn.annual.credit.line | line_key, source | Retention feeds consume taxation/04 FR-153 record shape + file 02 DJIMR links by id; D. 96-2012 / D. 54-96 amounts = config gaps (LEADs) |
| FR-246..253 | odoo | l10n_hn.annual.declaration(.line) | tariff_selector, isv_class, loss_carryforward | 22-A regimes consumed from taxation/03 FR-081..092 by id (R-H32; "1.05%" never seeded); source-of-income validation = ORM constraint on credit lines |
| FR-254 | odoo | l10n_hn.annual.declaration | prerequisite_535_id (m2o, required FY2024+) | Carve-out rows pre-FY2024 omisa/rectificativa; gate internals = file 06 by id |
| FR-255..259 | odoo | l10n_hn.annual.declaration | as_*, atn_* + parameter rows | Dated parameters (AS from FY2014; ATN autofill 202401+); ATN rate row carries the R-H29/74_-OQ-3 conflict marker in `note` |
| FR-260..262 | odoo | l10n_hn.isr.pn.suspension | window + attachments | Mínimo exento resolved from the CSV first band by id (never stored as law); effect/recurrence unencoded (OQ-gated) |
| FR-263, FR-264 | odoo | l10n_hn.annual.parameter + dashboard action | calendar rows, obligation gate | Members consumed by id from files 06/08/10/11; FR-264 consumes taxation/04 FR-135..136 flags |

Version-regime notes (D12): the FR-221 window rows, the FR-252 22-A
regime rows (via id) and the FR-255/257 AS/ATN parameters are dated rows
with explicit effectivity (AS from FY2014; ATN autofill from 202401; 535
gate FY2024+) — no adaptation windows exist in the instruments. D15/D16:
every dated parameter resolves as-of the declared period and snapshots on
write; a rectificativa of a filed period re-uses the ORIGINAL period's
resolved values (filed-period protection), never the current rows.

## 6. Acceptance Criteria

- **AC-001:** Given fiscal year 2025, then the package window row is
  2026-01-01→2026-04-30; given April-30 falling on a non-business day,
  then the row shifts to the next business day; given a special-FY
  taxpayer, then the window extends three months from the special close
  (FR-221).
- **AC-002:** Given a 102 where the cedular declaration exists but is
  unpaid at filing time, then the cedular base does NOT flow into
  no-gravados and the vinculación precondition is surfaced; given the
  same declaration subsequently paid, then the base flows automatically
  (FR-236).
- **AC-003:** Given a filed código 119 and a filed DMR 113 on a 103, then
  the 119 value appears read-only while the dividend casilla is
  pre-filled but editable (FR-237).
- **AC-004:** Given a 103 with RNG L1,500,000, then AS = 5% × 500,000 =
  L25,000; given RNG L800,000, then AS = L0; given an Exportación-regime
  PJ, then no AS section computes (exclusion per 74_ only, OQ-004 marker
  attached) (FR-255, FR-256).
- **AC-005:** Given ATN-determined L20,000 against ISR+AS of L15,000,
  then ATN payable = L5,000; given ISR+AS of L25,000, then ATN payable =
  L0 with L20,000 shown as credit (FR-258).
- **AC-006:** Given a FY2025 103 attempted without the 535, then filing
  is blocked (same-obligation doctrine); given a pre-2024 omisa 103, then
  no 535 is required (carve-out) (FR-254).
- **AC-007:** Given prior-FY gross L1.2B, then the 103 tariff selector
  offers the 22-A branch (regime C, 1%/0.5% consumed by id); given
  prior-FY gross L900M, then it does not; given a back-dated FY2019
  computation, then regime B applies and a "1.05%" rate never occurs
  (FR-252, R-H32).
- **AC-008:** Given a taxpayer with two qualifying loss years and last-FY
  gross L120M, then the D. 96-2012 anticipo leg activates at 1% of
  declared gross, with the amount flagged config-gap-evidenced (FR-243).
- **AC-009:** Given Sección B counts of 3 new employees + 1 with
  disability, then the job-credit line stays locked; given 4 + 1, then it
  unlocks with the unprinted credit amount as a config gap (FR-244).
- **AC-010:** Given the 15% ISV line with ventas brutas L1,000,000 and
  devoluciones L100,000, then ventas netas = L900,000 on that line only,
  with separate 18%/export lines unaffected (FR-247).
- **AC-011:** Given current RNG L1,000,000 and a L600,000 loss
  carryforward, then the deductible carryforward caps at L500,000; given
  no resolución on record, then the carryforward is blocked and flagged
  (FR-250).
- **AC-012:** Given a FY2025 102 computation, then the scale resolves to
  the sar_07_2025 CSV vintage by id (217,493.16 / 331,638.50 / 771,252.38)
  and no bracket is transcribed from the image-only Ayuda prints
  (FR-231).
- **AC-013:** Given a suspension petition for FY2025 filed 2026-06-15,
  then it is rejected (window closed); given the same filed 2026-03-15
  with the attachment checklist complete, then it is accepted for
  processing, the mínimo exento resolves at L217,493.16 from the scale
  family, and no RTN-state change is encoded (FR-260..262).
- **AC-014:** Given a 103 for period 202403, then ATN inputs autofill
  from the 535 with validation-only UX; given period 202312, then the
  fields are manually consigned (FR-259).
- **AC-015:** Given a 103 with Art. 50 and anticipo-1% credits but no
  income source consigned for them, then advance is blocked (FR-253).
- **AC-016:** Given a filed 102 in state Original OT. Aprobada OT, then
  all writes are rejected; given a rectificativa initiated, then a new
  record opens from the snapshot with original values shown struck
  through and the original untouched (FR-225).
- **AC-017:** Given a PN with FY2025 gross L200,000 (below the exempt
  band L217,493.16), then the filing-exemption flag (taxation/04 FR-136)
  suppresses the 102 obligation and the suspension petition path is
  offered (FR-264).
- **AC-018:** Given Sección B edits on a 102, then the ISR computation is
  unchanged (informative-only invariant) (FR-226).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | D. 199-2006 citation garbled (origin `29_ OQ-1`): 29_ p.13 cites "Artículo 30, numeral 14 Decreto (199-2006)" — the decree has no Art. 30; the manual also omits the L30k@60 component and never restates the 65+ ≤L350k amount (corpus-pinned via taxation/02 only). D. 199-2006 (95_/96_) + D. 194-2002 (97_) unacquired LEADs; FR-233 encodes hooks only. | no | acquisition queue | open |
| OQ-002 | ZOLITUR 4% article conflict (origins `29_ OQ-2` + `47_ OQ-1`, register C2 — CONFLICT): D. 181-2006 Art. 4 (29_ p.37) vs Art. 25 (47_ p.4); decree unacquired. Primary home = fiscal-reporting file 08; carried here because the restated 4% rides the FR-236 vinculación flow — never resolve silently. | no | file 08 + acquisition queue | open (pointer) |
| OQ-003 | Tariff selector "Literal c)" ambiguity (origin `30_ OQ-2`): Art. 22.c is the foreign-transport presumed base, not a PJ rate — print defect; FR-252 labels it as such and never encodes it as a rate. | no | Takumi S-HN3 | open (verify) |
| OQ-004 | AS exclusion cross-doc dependency (origin `30_ OQ-3`, R-H30): the Exportación/Turismo exclusion appears ONLY in 74_ p.9 (Jun-2026), not in 30_ (Feb-2026); FR-256 encodes it as 74_-anchored config pending corroboration. | no | Takumi S-HN3 | open |
| OQ-005 | Undated 47_ print (origin `47_ OQ-2`): treat content as vigente-at-read only; primary home file 08 — affects how far back the 103 read-only 120 link can be trusted. | no | file 08 | open (pointer) |
| OQ-006 | Código 120 filing cadence unpinned (origin `47_ OQ-3`): per-transaction/eventual mechanics vs the Apr-30 statement — determines when the 103 read-only link populates; FR-237 blocks on paid-and-declared rather than resolving cadence. Primary home file 08. | no | file 08 | open (pointer) |
| OQ-007 | PN scale image-only (origins `68_ OQ-1` + `74_ OQ-1`): the Ayudas print the progressive scale as IMAGE (68_ p.4; 74_ p.7 FY2025) — amounts are consumed BY ID from `../taxation/isr_brackets.csv` (taxation/04 FR-121..125); never transcribe an image. | no | resolved by construction (CSV by id) | open (register carry) |
| OQ-008 | FY2019 "1.05%" internal inconsistency (origin `68_ OQ-3`, R-H32 flag): 68_ p.5 prints "resultaren menores al uno por ciento (1.05%)" — 1% text-primary; regime rows consumed from taxation/03 by id, the defect never seeded. | no | resolved (1% text-primary) | open (register carry) |
| OQ-009 | Vinculación criteria table image-only (origin `74_ OQ-2`): participation percentages (Reglamento Arts. 11-13, "criterios de vinculación, Artículo 3 de la Ley") not extractable — LEAD; FR-238 consumes the cube structure, criteria stay unencoded. | no | acquisition queue | open |
| OQ-010 | ATN instrument conflict (origin `74_ OQ-3`, R-H29 — CONFLICT/LEAD): D. 51-2003 "Capítulo II" (74_ p.11) vs LET "Art. 7" (corpus lead) — chapter- vs article-level citation; D. 51-2003 unacquired. FR-257 ships 1%/L3M as dated config on R-H29; acquiring D. 51-2003 resolves. | no | acquisition queue | open |
| OQ-011 | Suspension effect scope unpinned (origin `75_ OQ-1`): what obligations are suspended, RTN/estado consequences, whether informativas remain due — SAR resolution terms unstated; FR-262 encodes request-character only. | no | Takumi S-HN3 | open |
| OQ-012 | Mínimo exento amount (origin `75_ OQ-2`): never printed in 75_ — depends on the per-FY scale family; FR-261 resolves the first-band ceiling from the CSV by id (FY2025 = L217,493.16); confirm SAR's own threshold basis (band vs composite) on first live filing. | no | Takumi S-HN3 | open |
| OQ-013 | Suspension recurrence/persona-turnover (origin `75_ OQ-3`): whether re-notification is annual and whether turnover personas require it; the escrito is addressed to a named Ministro Director (dated official) — subject to turnover. | no | Takumi S-HN3 | open |
| OQ-014 | Unacquired-decree pack (NEW, EV29 synthesis; **W6 update: D. 54-96 acquired as `118_` + D. 110-93 acquired as `117_` — FR-235/FR-244 anchors upgraded to statute, LB-015; D. 199-2006/D. 194-2002 were already evidenced V-HN1b as `95_`/`97_`**): remaining unacquired = D. 96-2012 (anticipo legs, FR-243) + LET D. 51-2003 (ATN instrument, OQ-010; its ancestor D. 54-96 now in corpus). Amounts/gates stand on the prints or statute, never on asserted text, until acquired. | no | acquisition queue | open (narrowed) |
| OQ-015 | 103 loss-carryforward mechanics sparse (NEW): the print gates the carryforward at ≤ 50% of current RNG with resolución/RTN validation but does not restate which resolución, the same-activity rule or the interaction with the 3-year NOL chassis (taxation/02 by id); FR-250 encodes the form-side validator only — verify vs live form. | no | Takumi S-HN3 | open |
| OQ-016 | Art. 20 selector mechanics unpinned (NEW): the print gives the five-activity dropdown and the income concept only — thresholds/treatment of the Art. 20 regime are stated nowhere in EV29; FR-228 ships the selector OQ-gated and never guesses the regime. | no | Takumi S-HN3 + taxation wave | open |

Register-mapping note: origins carried — `29_ OQ-1` (OQ-001), `29_ OQ-2` +
`47_ OQ-1` (OQ-002), `30_ OQ-2` (OQ-003), `30_ OQ-3` (OQ-004), `47_ OQ-2`
(OQ-005), `47_ OQ-3` (OQ-006), `68_ OQ-1` + `74_ OQ-1` (OQ-007),
`68_ OQ-3` (OQ-008), `74_ OQ-2` (OQ-009), `74_ OQ-3` (OQ-010), `75_
OQ-1/2/3` (OQ-011/012/013). `30_ OQ-1` was resolved pre-synthesis (ATN 1%
pinned by 74_ per R-H29; instrument conflict carried as OQ-010). `68_
OQ-2` (cosmetic OCR section-garble) is intentionally not carried — no FR
impact.

