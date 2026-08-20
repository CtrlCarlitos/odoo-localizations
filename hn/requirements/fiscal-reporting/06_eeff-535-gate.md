# HN — Fiscal reporting — EEFF Informe de Estado de Situación Financiera (código 535): the gate before the ISR annual DJ and the ATN feed

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the **Informe de Estado de
Situación Financiera** (Financial-Position Status Report, OVI código 535) —
cluster F6 of the W2 evidence (EV13: EVID-072..075; EV63:
EVID-175/184/185). It owns: (a) the 535 obligation object — the annual
informative EEFF report designed to NIIF, its 1-January→30-April window
(+3 months for special fiscal periods), its subjects (personas jurídicas +
personas naturales *comerciantes individuales*, individual merchants) and
its OVI-only modality; (b) the **EEFF-before-DJ gate** internals from
FY2024 (SAR-619-2024): the same-obligation doctrine, the ≤FY2023
*omisa/rectificativa* carve-out (exemption) and the gate-status contract
consumed by the 102/103 engines; (c) the section A-D casilla contract
(A Activos / B Pasivos / C Patrimonio / D Resumen) at casilla granularity,
including the depreciation/amortization/*deterioro* (impairment) panels;
(d) the third-party detail panels — per-socio cuentas por cobrar
(receivables), per-provider cuentas por pagar (payables) with RTN +
*antigüedad* (aging, in months), per-bank/per-loan panels with the
PPE-purchase-loan linkage, and the *superávit-revaluación* (revaluation
surplus) panel; (e) the *vinculación* (cross-declaration feed) into the
103's Sección D as Activo Total Neto (ATN) inputs from period 202401;
(f) the Art. 11 estimated-CxC validation surface; (g) the certification
posture per R-H24 (NO contador-certification casilla exists); and (h)
grid-edition fidelity and the D18 historical-ingestion surfaces.

It does **not** own: the OVI/SW filing chassis — state machine, *alta de
obligación* (self-enrollment), *borrador/juramento/acuse* + QR,
rectificativa engine, boletín — fiscal-reporting file 01 (cluster F1,
HN-FREP-FR-001..040 pre-allocated, parallel write), consumed by id; the
102/103 engines, the ATN computation (1% / L3,000,000 exemption / floor
credit) and the gate's CONSUMER side — file 07 (cluster F7; gate
HN-FREP-FR-254, ATN HN-FREP-FR-257..259, window rows HN-FREP-FR-221,
dashboard HN-FREP-FR-263), consumed by id; the DJIMR/DMC/tarjetas/ISV
monthly families (files 02-05); the GC event family (file 08); selectivo
(file 09); TP 545 and the 541/542/543 informativas (file 10, cluster F10 —
the parallel related-party disclosure consumer, parallel write); the NIIF
bookkeeping obligation itself — `../taxation/01_isr-framework.md`
HN-TAX-FR-028 (CT Art. 64 anchor) and the special-fiscal-period close
(HN-TAX-FR-016), consumed by id; the Art. 11.g bad-debt provision
computation — `../taxation/02_isr-deductions.md` HN-TAX-FR-053..055,
consumed by id; the revaluation law side —
`../taxation/05_d17-2010-family.md` HN-TAX-FR-184..186, consumed by id;
and the ATN rate/instrument conflict (`74_ OQ-3`, R-H29) — file 07
OQ-010, pointer only.

## 2. Legal Basis

Authority order (master index, binding): SAR-619-2024 (`13_`) is the
primary instrument for the gate and the 535 filing regime; SAR-236-2024
(approving form 535) is UNACQUIRED as a standalone (32_ OQ-2) and stands
only as quoted in the 619 considerandos and the Ayuda; the per-código
Ayuda (`67_`) is the field/flow authority; ISR = `01_`; CT = `03_`.
Binding rulings applied: R-H24 (NO certification casilla in the 535;
ISR Art. 28 vehicle outside OVI remains open). UNACQUIRED instruments
cited below stand ONLY as evidenced inside acquired prints — LEAD-flagged,
never as acquired text: Reglamento Ley ISR ("Acuerdo N°799") Art. 84
(`13_ OQ-2`/`67_ OQ-3` — never cite Arts. 51/84 as legal basis), Acuerdo
1-1975 (depreciation/agotamiento), Acuerdo 0948-2003 (ATN reglamento),
CNBS GE-180/06-02-2012 (activos eventuales). D-H1/D-H2/D-H3 bind; the 67_
print is undated except for its period example ("202401") → grid values
load as valid-at-read edition rows pending print-run pinning.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo SAR-619-2024 (16-dic-2024, La Gaceta 36,725 27-dic-2024), PRIMERO/SEGUNDO/TERCERO: PRIMERO — "Que la Declaración Jurada del Impuesto Sobre la Renta requerirá a partir del período fiscal 2024, la presentación previa del 'Informe de Estado de Situación Financiera', integrado por el Balance General y Cuadros de Ganancias y Pérdidas. Para los períodos fiscales anteriores al 2024 no es obligatoria la presentación del Informe [...] previo a la presentación de la Declaración Jurada [...] cuando se trate de una declaración jurada omisa o rectificativa." SEGUNDO — obligados: "las personas jurídicas y las personas naturales declaradas como comerciantes individuales". TERCERO — elaboración/presentación "a través de la Oficina Virtual o por los medios que proporcione el Servicio de Administración de Rentas" | From FY2024 the ISR sworn declaration requires the PRIOR presentation of the EEFF inform (integrated by the Balance General and Ganancias y Pérdidas statements); for periods before FY2024 the inform is not required prior to an omisa (missed) or rectificativa (amended) declaration; obligated subjects = juridical persons and natural persons declared individual merchants; elaboration/presentation through the Oficina Virtual or means provided by SAR | `hn/sources/13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf` | 619-PRIMERO/SEGUNDO/TERCERO p.4 (EV13:EVID-072) |
| LB-002 | SAR-619-2024, CUARTO/QUINTO + considerando SAR-236-2024: CUARTO — "periodicidad anual y debe presentarse del uno (01) de enero al treinta (30) de abril de cada año. Para las personas jurídicas y personas naturales constituidas como comerciantes individuales con periodo fiscal especial, el vencimiento se establece en los tres (3) meses siguientes al cierre de su ejercicio fiscal." QUINTO — "constituye el complemento de la Declaración Jurada de Impuesto Sobre la Renta, siendo ambos formularios una misma obligación, por lo que, la no presentación del Informe [...] dará lugar al incumplimiento de la obligación de presentación de la Declaración Jurada antes referida y sus obligaciones conexas." Considerando — Acuerdo No. SAR-236-2024 (10-may-2024) aprobó el Formulario "535 - Informe de Estado de Situación Financiera", "a través de la Oficina Virtual como única modalidad", complemento de la DJ ISR para empresas mercantiles, "en el cual se deberá informar lo contenido en el Balance General y Cuadros de Ganancias y Pérdidas" | Annual periodicity, filed 1-January→30-April each year (special fiscal period: due within the 3 months following the FY close); the inform is the COMPLEMENT of the ISR DJ — both being ONE SAME obligation, so non-presentation of the inform constitutes non-compliance of the DJ presentation duty and its connected obligations; form 535 approved by SAR-236-2024, OVI as the only modality, informing the Balance General and Ganancias y Pérdidas content | `hn/sources/13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf` | 619-CUARTO/QUINTO p.4; considerando p.3 (EV13:EVID-073) |
| LB-003 | SAR-619-2024, SÉPTIMO/NOVENO: promulgación "a través de su publicación en el Diario Oficial 'La Gaceta' y en el portal electrónico" (CT Art. 13.4 dual-publication doctrine recited in considerandos); NOVENO — "entra en vigencia a partir de su publicación" (27-dic-2024); print defect: resolutivo numbering runs SEXTO → SÉPTIMO → NOVENO — OCTAVO absent from the print [sic] | Dual promulgation (gazette + portal aviso) as the standing form-vigencia mechanism; effectiveness from publication, 27-dic-2024 — the gate binds FY2024 declarations (filed in 2025); OCTAVO numbering gap = print defect, no substantive loss | `hn/sources/13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf` | 619-SÉPTIMO/NOVENO p.4 (EV13:EVID-074) |
| LB-004 | Ayuda Informe de Estado de Situación Financiera (`67_`, código 535), Generalidades: "Es un formulario informativo contenido en el Acuerdo SAR-619-2024 [...] en el cual se consignarán los activos corrientes y no corrientes, la depreciación, amortizaciones y deterioro, los pasivos corrientes y no corrientes y el patrimonio"; complemento/una misma obligación (as LB-002); NIIF — "diseñado conforme a las Normas Internacionales de Información Financiera (NIIF) [...] los Obligados tributarios deben llevar y mantener los registros contables [...] según lo establece el artículo 64 del código tributario"; sujetos — "las personas jurídicas y las personas naturales declaradas como comerciantes individuales"; plazo — "del uno (01) de enero al treinta (30) de abril de cada año" + especial +3 meses; tabla — "Informativa de Estado de Situación Financiera | 535 | Informativa | Única modalidad [...] (OVI)"; base legal — "Ley de Impuesto Sobre la Renta, Decreto 25-1963 Artículo 28, el reglamento sobre la Ley antes referida Acuerdo N°799 Artículo 84 y Acuerdo SAR-619-2024" | The 535 field/flow authority: informative form per SAR-619-2024 carrying current/non-current assets, depreciation, amortization and impairment, current/non-current liabilities and equity; NIIF-designed, sourced from the CT-Art. 64 books; subjects PJ + individual-merchant PN; window 1-Jan→30-Apr (+3m special FY); OVI-only informative; the Ayuda's printed base-legal list names the ISR Reglamento "Acuerdo N°799" Art. 84 (4th corpus citation, UNACQUIRED — LEAD, never as acquired text) | `hn/sources/67_Ayuda_EEFF_situacion.pdf` | 67_ pp.4-6 (EV63:EVID-184) |
| LB-005 | `67_`, IV Elaboración (pp.9-58): "el formulario [...] tiene cuatro secciones: A. Total Activos / B. Total Pasivos / C. Total Patrimonio / D. Resumen [...] al lado derecho se observará un cuadro resumen que contiene la ecuación contable (Activo = Pasivo + Patrimonio)"; CxC clientes — "Relacionados locales (transacciones del período), Relacionados exterior (transacciones del período), Relacionados locales (transacciones de periodos anteriores), Relacionados exterior (transacciones de períodos anteriores), No relacionados locales y/o No relacionados exterior"; socios detail — "Nombre del socio, Monto de la cuenta, Fecha de la transacción y % de participación en el capital"; proveedores detail — "RTN, nombre del proveedor, monto adeudado y antigü[e]dad saldo en meses"; préstamos — "nombre del banco, numero de préstamo, monto" (local/exterior, hipotecarios); "Préstamo para la compra de propiedad, planta y equipo [...] nombre del prestamista, numero de préstamo, monto y activo comprado"; vinculación — "las casillas del activo corriente y el activo no corriente viajaran en forma íntegra a la sección D de la Declaración Jurada de Impuesto Sobre la Renta persona jurídica como activos gravables para el cálculo del Activo Total Neto, cumpliendo el principio de vinculación que tienen los nuevos formularios"; Art. 11 — "la amortización de las cuentas por cobrar que establece el Artículo 11 de la Ley de Impuesto Sobre la Renta se debe consignar en la casilla denominada 'Estimaciones de Cuentas por Cobrar' ya que esta casilla es la que vinculará y trasladara el valor [...] a la sección D"; depreciación — "deben estar conforme al reglamento especial para la depreciación y agotamiento de activos [...] Acuerdo No.1 d[el] 01 de noviembre de 1975"; activos eventuales per "Resolución GE No.180/06-02-2012 emitida por la Comisión Nacional de Bancos y Seguros"; superávit — "superávit de capital por revaluación de activos [...] vinculará a la sección D [...] con base a lo que establece acuerdo 0948-2003 que contiene el reglamento del Impuesto al Activo Neto"; attestation — "Jura la exactitud y veracidad de la presente declaración" only; period example "202401" | The 535 form structure: four sections with the accounting-equation panel; the CxC related-party splits (local/foreign × current-period/prior-periods + unrelated); the third-party detail panels (per-socio, per-provider with RTN and aging, per-bank/per-loan, PPE-purchase-loan with purchased asset); the íntegra feed of asset casillas into the 103 Sección D as taxable assets for the ATN; the Estimaciones-de-CxC casilla as the Art. 11 vinculación vehicle; the Acuerdo 1-1975 / GE-180-2012 / 0948-2003 citations (all UNACQUIRED LEADs); juramento as the ONLY attestation; the "202401" edition key | `hn/sources/67_Ayuda_EEFF_situacion.pdf` | 67_ pp.9-58 (EV63:EVID-185) |
| LB-006 | `67_, V Recomendaciones (p.58) + VI Glosario (p.59): "previamente debe realizar la presentación del informe [...] 535 ya que el cumplimiento de la obligación de presentar la Declaración Jurada de Impuesto Sobre la Renta inicia con la presentación de este informe"; pre-2024 — activos gravables/provisiones "los deberá consignar en la sección D de la declaración antes referida" (omisa/rectificativa carve-out practice); Glosario — Estimaciones de CxC = ISR Art. 11 1%-of-credit-sales provision, "saldo [...] nunca será superior al diez por ciento (10%) del importe de las cuentas por cobrar a clientes al cierre [...], excluyendo [...] transacciones con empresas relacionadas"; Deterioro = NIIF 9 ECL | Filing-order guidance: the 535 comes first because DJ compliance starts with its presentation; pre-FY2024 omisa/rectificativa filers consign taxable assets/provisions directly in the DJ's Sección D; glossary pins the Estimaciones-de-CxC casilla to the Art. 11 provision (1% of credit sales, ≤10% of closing client AR, excluding related parties) and Deterioro to NIIF 9 expected-credit-loss | `hn/sources/67_Ayuda_EEFF_situacion.pdf` | 67_ pp.58-59 (EV63:EVID-185) |
| LB-007 | Ley ISR (D.L. 25-1963, texto consolidado SAR-07-2025), Art. 28 — as quoted in the SAR-619-2024 considerandos: the annual DJ and its Balance/GyP "certificadas por un contador hondureño titulado, o incorporado" (certified by a Honduran chartered or incorporated accountant); R-H24: NO certification casilla exists anywhere in the 535 structure (exhaustive A-D inventory, EV63:EVID-185) — the Art. 28 attestation vehicle outside OVI remains open (`13_ OQ-1` residue / `67_ OQ-2` synthesis note) | ISR Art. 28: the annual DJ carries Balance/GyP certified by a Honduran chartered/incorporated accountant — statutory anchor behind the certification question; NOT discharged by any 535 casilla (R-H24) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 28 (quoted in 619 considerandos, `13_` pp.2-3; EV13:EVID-073; 13_ OQ-1) |
| LB-008 | Código Tributario (D. 170-2016 act. D. 180-2020), Art. 64 — as quoted by `67_` p.5: "los Obligados tributarios deben llevar y mantener los registros contables [...] según lo establece el artículo 64 del código tributario" (bookkeeping under laws, regulations and the NIIF generally accepted in Honduras; entries posted within 30 days — NIIF-books anchor owned by taxation/01 HN-TAX-FR-028, consumed by id) | CT Art. 64: the NIIF bookkeeping obligation that sources the 535 balances — anchor consumed from `../taxation/01_isr-framework.md` by id, never re-derived here | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Art. 64 (quoted 67_ p.5; EV63:EVID-184) |
| LB-009 | Acuerdo SAR-236-2024 (UNACQUIRED standalone, 32_ OQ-2) — chassis hooks as quoted in the family: "Única modalidad para la presentación a través de la Oficina Virtual (OVI)"; Primero — "Se crea la Oficina Virtual [...]"; Segundo — "Implementar la plataforma digital denominada 'Oficina Virtual', como único medio [...]"; 619 considerando: aprobó el Formulario "535 - Informe de Estado de Situación Financiera" "a través de la Oficina Virtual como única modalidad" | OVI as the single presentation modality and the form-535 approval instrument — chassis contract owned by fiscal-reporting file 01 (F1), consumed by id; the SAR-236-2024 text itself is evidence-quoted only | `hn/sources/67_Ayuda_EEFF_situacion.pdf` | 67_ pp.5-57 (EV63:EVID-175/184; 619 considerando EV13:EVID-073) |

## 3. Functional Requirements

Numbering: HN-FREP-FR-191..218 (allocated range 191..220, contiguous;
219..220 reserved tail).

### 3.1 The 535 obligation, subjects and calendar

- **HN-FREP-FR-191:** The system shall implement the 535 as an annual
  INFORMATIVE declaration object keyed by fiscal year with the OVI
  annual period-key convention YYYY + "01" (the Ayuda's "202401" example —
  an annual form keyed by a six-digit YYYYMM period tag), whose filing
  window loads as DATED per-FY rows 1-January→30-April of the year
  following the declared FY — never a rolling computation (D-H2) —
  resolving the row as-of the declaration's period anchor and
  snapshotting it onto the record (D15). (LB-002; LB-004; LB-005;
  EV13:EVID-073; EV63:EVID-184/185)
- **HN-FREP-FR-192:** The system shall scope the 535 obligation to
  "las personas jurídicas y las personas naturales declaradas como
  comerciantes individuales" — every other persona natural carries NO 535
  obligation object — and shall reuse this subject scope as the gate scope
  input consumed by the 102/103 engines (file 07 HN-FREP-FR-254 by id).
  (LB-001; LB-004; EV13:EVID-072; EV63:EVID-184)
- **HN-FREP-FR-193:** The system shall extend the window by three months
  for PJ and individual-merchant PN with an AT-authorized special fiscal
  period — due within the 3 months following the FY close — consuming the
  special-period close date from taxation/01 HN-TAX-FR-016 by id and
  storing the extended due date as its own DATED row per FY (D-H2).
  (LB-002; LB-004; EV13:EVID-073; EV63:EVID-184)
- **HN-FREP-FR-194:** The system shall file the 535 through the Oficina
  Virtual as the "única modalidad", consuming the OVI chassis — alta de
  obligación (código 535 + "Año desde"), Pendientes/Realizadas search,
  borrador, juramento, acuse with código único + QR, estado registry,
  rectificativa reloading the original "casilla por casilla" per CT
  Art. 117 — from fiscal-reporting file 01 (cluster F1) BY ID, with zero
  chassis re-derivation in this file. (LB-004; LB-009;
  EV63:EVID-175/184)
- **HN-FREP-FR-195:** The system shall source every 535 balance from the
  NIIF accounting records — the report is "diseñado conforme a las
  Normas Internacionales de Información Financiera (NIIF)" and the books
  obligation is CT Art. 64, anchored at taxation/01 HN-TAX-FR-028 by id —
  with NO parallel non-NIIF mapping layer, and shall render the
  accounting-equation summary panel (Activo = Pasivo + Patrimonio) as a
  live balance check that blocks filing while out of balance.
  (LB-004; LB-008; EV63:EVID-184/185)
- **HN-FREP-FR-196:** The system shall publish the 535 window row on the
  shared annual-close calendar as a member of the Apr-30 package
  (535 + 102 + 103 + AS + ATN + GC 119 + TP 545 + 506 + 107 per 74_
  RESUMEN, consumed from file 07 by id), exposing per-member state to the
  compliance dashboard owned by file 07 HN-FREP-FR-263 — this file owns
  only the 535 member row. (LB-004; EV13:EVID-073; EV63:EVID-184)

### 3.2 The EEFF-before-DJ gate (FY2024+)

- **HN-FREP-FR-197:** The system shall own the gate INTERNALS as a DATED
  rule row valid_from FY2024 (SAR-619-2024 in vigencia from publication,
  27-dic-2024): the ISR annual DJ "requerirá a partir del período fiscal
  2024, la presentación previa del Informe de Estado de Situación
  Financiera" — a prerequisite-form edge binding each subject's (FR-192)
  535-for-FY-N to the ISR DJ-for-FY-N, with presentation order enforced
  (535 BEFORE DJ); the consumer-side blocking on 102/103 is owned by file
  07 HN-FREP-FR-254 by id. (LB-001; LB-003; EV13:EVID-072/074)
- **HN-FREP-FR-198:** The system shall encode the same-obligation
  doctrine — the 535 is the DJ's complement, "siendo ambos formularios una
  misma obligación": while the 535 is absent the DJ's compliance state
  renders non-filed (its non-presentation "dará lugar al incumplimiento
  [...] y sus obligaciones conexas", connected-obligations flag on);
  sanction computation itself is owned by the CT frame (taxation/01 by
  id) and stays informational here. (LB-002; LB-004;
  EV13:EVID-073; EV63:EVID-184)
- **HN-FREP-FR-199:** The system shall carry the carve-out as a DATED
  row valid_to FY2023 scoped to omisa/rectificativa filings ONLY: "para
  los períodos fiscales anteriores al 2024 no es obligatoria la
  presentación del Informe" prior to a declaración jurada omisa o
  rectificativa — a ≤FY2023 amended/missed DJ files with NO 535
  prerequisite; original-timely ≤FY2023 DJs sit outside the gate regime
  entirely (the instrument's conditionality reaches only the omisa/
  rectificativa case). (LB-001; EV13:EVID-072; EV63:EVID-185)
- **HN-FREP-FR-200:** The system shall surface the filing-order guidance
  and the pre-2024 consignación path: the Ayuda instructs that "el
  cumplimiento de la obligación de presentar la Declaración Jurada de
  Impuesto Sobre la Renta inicia con la presentación de este informe", and
  for pre-FY2024 omisa/rectificativa filings the taxpayer "deberá
  consignar en la sección D" of the DJ the activos gravables/provisiones
  directly (no 535 exists to feed them — the DJ-side manual fields are
  owned by file 07 HN-FREP-FR-259 by id). (LB-006;
  EV13:EVID-072; EV63:EVID-185)

### 3.3 Section structure A-D (the casilla contract)

- **HN-FREP-FR-201:** The system shall implement the four-section layout —
  "A. Total Activos / B. Total Pasivos / C. Total Patrimonio / D.
  Resumen" — with the right-hand summary panel showing the accounting
  equation (Activo = Pasivo + Patrimonio), and shall ship NO
  Ganancias-y-Pérdidas module: the Ayuda describes a balance-sheet-only
  form (A-D inventoried exhaustively, no GyP section or casillas) while
  SAR-619/236 define the 535 "integrado por el Balance General y Cuadros
  de Ganancias y Pérdidas" — CONFLICT `67_ OQ-1` carried OPEN, with a
  guard that blocks adding any GyP casilla group until reconciled against
  the live OVI 535. (LB-002; LB-004; LB-005; EV13:EVID-073;
  EV63:EVID-184/185; OQ-001)
- **HN-FREP-FR-202:** The system shall model the activos corrientes
  casilla tree: Efectivo (Caja; Bancos locales / exterior); Inversiones
  (al costo, a valor razonable, holding, otros); Cuentas y documentos por
  cobrar — clientes split "Relacionados locales (transacciones del
  período) / Relacionados exterior (transacciones del período) /
  Relacionados locales (transacciones de períodos anteriores) /
  Relacionados exterior (transacciones de períodos anteriores) / No
  relacionados locales y/o no relacionados exterior" — plus the
  socios-o-accionistas line (detail panel FR-207, local/foreign); otros
  activos financieros; Inventarios (mercadería en tránsito with
  descripción + "número de póliza" + monto detail, materiales y
  suministros, producto en proceso, terminados); activos no corrientes
  mantenidos para la venta y/o activos eventuales (per CNBS
  GE-180/06-02-2012 — UNACQUIRED LEAD, OQ-003); activos biológicos
  (valor razonable-menos-costo-ventas / costo); gastos pagados por
  anticipado (propaganda y publicidad, rentas pagadas por anticipado,
  primas de seguro, otros); otros. (LB-005; EV63:EVID-185)
- **HN-FREP-FR-203:** The system shall model the activos no corrientes
  casilla tree: PPE by class (Terrenos; Automotores; Maquinaria;
  Edificios y bienes inmuebles; Construcciones en curso; Mobiliario y
  equipo; Equipo de computación; Mejoras en áreas arrendadas; Mejoras en
  áreas propias; Otros); Intangibles (Crédito mercantil, Derechos de
  Autor, Marcas, Patentes, Licencias, Otros + the informativos Derechos
  conexos, Asesorías técnicas, Prestaciones similares); Propiedad de
  inversión (Terrenos/Edificios × costo/valor razonable); biológicos no
  corrientes; exploración y explotación (tangible/intangible); CxC no
  corrientes; Inversiones no corrientes; Otros. (LB-005;
  EV63:EVID-185)
- **HN-FREP-FR-204:** The system shall model the
  depreciation/amortization/deterioro panels: direct casillas (Deterioro
  de CxC; "Estimaciones de Cuentas por Cobrar" — the FR-214 vehicle;
  deterioro de inversiones/inventario; reserva de instituciones
  financieras); depreciación acumulada PPE per class (FR-203 classes);
  amortización acumulada de intangibles per class; deterioro acumulado de
  intangibles y propiedades de inversión — values that "deben estar
  conforme al reglamento especial para la depreciación y agotamiento de
  activos [...] Acuerdo No.1 del 01 de noviembre de 1975" (UNACQUIRED
  LEAD, OQ-003: the class lists stand on the Ayuda, never on the
  unacquired reglamento). (LB-005; LB-006; EV63:EVID-185)
- **HN-FREP-FR-205:** The system shall model the pasivos casilla tree:
  CxP — proveedores split related local (transacciones del período) /
  related prior-periods / exterior / no relacionados, with the
  per-provider detail panel (FR-208) — socios o accionistas; otros
  pasivos financieros; "Transferencias de casa matriz y sucursales del
  exterior"; porción corriente de obligaciones financieras (préstamos
  bancarios local/exterior with the FR-209 panel; hipotecarios; préstamo
  para la compra de PPE — FR-209); impuestos a pagar (municipales /
  estatales); emisión de obligaciones; ingreso diferido; beneficios a los
  empleados; otras provisiones; otros — with the non-current bucket
  carrying "las mismas casillas" (same casilla set, non-current
  classification). (LB-005; EV63:EVID-185)
- **HN-FREP-FR-206:** The system shall model the patrimonio casilla tree:
  Donaciones en especie; "Capital suscrito no pagado" carried with its
  stated function "de disminuir el patrimonio" (a contra-patrimonio
  sign); aportes de socios para futura capitalización; reserva legal y
  voluntaria; ganancia/pérdida del ejercicio; capital social nacional
  y/o extranjero; resultados acumulados (incl. "Ajustes acumulados por
  transición a las NIIF" + ganancias/pérdidas acumuladas per período,
  multi-period rows); otro resultado integral incl. the superávit
  panel (FR-210). (LB-005; EV63:EVID-185)

### 3.4 Third-party detail panels (the EEFF subledgers)

- **HN-FREP-FR-207:** The system shall emit, inside the CxC
  socios-o-accionistas line, the per-socio detail panel with exactly the
  printed fields — "Nombre del socio, Monto de la cuenta, Fecha de la
  transacción y % de participación en el capital" — for local and foreign
  socios, reconciled to the partner ledger; the panel is a related-party
  disclosure surface whose cross-use for the >100-day deemed-dividend
  ledger (taxation/05 HN-TAX-FR-172 by id) is NOT stated in the corpus and
  stays unlinked (OQ-008). (LB-005; EV63:EVID-185)
- **HN-FREP-FR-208:** The system shall emit, inside the CxP proveedores
  line, the per-provider detail panel with exactly the printed fields —
  "RTN, nombre del proveedor, monto adeudado y antigu[i]edad saldo en
  meses" — reconciled to the AP ledger with RTN validation (14 positions)
  and aging months computed from the ledger's due-date convention
  (semantic mapping carried as OQ-009). (LB-005; EV63:EVID-185)
- **HN-FREP-FR-209:** The system shall emit the financing panels: per
  préstamo bancario (local/exterior) and hipotecario — "nombre del banco,
  numero de préstamo, monto" — and the PPE-purchase-loan panel — "nombre
  del prestamista, numero de préstamo, monto y activo comprado" — with
  the purchased-asset link modeled as a reference to the PPE casilla/
  asset record (FR-203) and the panel flagged as a Sección-D feed
  (FR-212). (LB-005; EV63:EVID-185)
- **HN-FREP-FR-210:** The system shall emit the superávit-revaluación
  panel inside otro resultado integral — "superávit de capital por
  revaluación de activos" — reconciled BY ID to the revaluation subledger
  of taxation/05 (HN-TAX-FR-184..186: FR-186 books the elective
  increment to the Superávit de Capital por Revaluación account); a
  mismatch flags for reconciliation and never auto-overwrites; the panel's
  Sección-D feed semantics stand on the 67_ p.50 citation of "acuerdo
  0948-2003 [...] reglamento del Impuesto al Activo Neto" (UNACQUIRED
  LEAD — OQ-003/OQ-007). (LB-005; LB-006; EV63:EVID-185)

### 3.5 Vinculación: the ATN feed and the Art. 11 validation

- **HN-FREP-FR-211:** The system shall implement the principle of
  vinculación: every activo corriente and activo no corriente casilla
  "viajaran en forma íntegra a la sección D de la Declaración Jurada de
  Impuesto Sobre la Renta persona jurídica como activos gravables para el
  cálculo del Activo Total Neto" — each asset casilla carries an
  atn_feed=integral flag and the report exposes the aggregate feed
  consumed by file 07 HN-FREP-FR-257..259 by id (the ATN computation,
  rate and exemption are owned there, never here). (LB-005;
  EV63:EVID-185)
- **HN-FREP-FR-212:** The system shall carry the contra/deduction feed
  set with atn_feed=contra flags: "Estimaciones de Cuentas por Cobrar"
  (FR-214), depreciación acumulada PPE per class, amortización acumulada
  de intangibles, deterioro (inversiones, intangibles, propiedades de
  inversión) and the préstamo-PPE linkage (FR-209) — the casillas the
  Ayuda flags as the ones that "vinculará[n] y trasladará[n] el valor a
  la sección D para el cálculo del Activo Total Neto". (LB-005;
  EV63:EVID-185)
- **HN-FREP-FR-213:** The system shall publish the ATN autofill contract
  as a DATED rule valid_from period 202401: from that period the ATN
  inputs are autocompleted from the 535 with validation-only UX
  ("solamente deberá validar los valores informados" — consumer side =
  file 07 HN-FREP-FR-259 by id); for earlier periods the values consign
  manually on the DJ side (FR-200). (LB-005; LB-006; EV63:EVID-185)
- **HN-FREP-FR-214:** The system shall implement the Art. 11
  estimated-CxC validation: the "Estimaciones de Cuentas por Cobrar"
  casilla is THE casilla that vinculates the Art. 11 amortization to
  Sección D, validated against the bad-debt provision ledger computed by
  taxation/02 HN-TAX-FR-053 by id — 1% of credit sales per period, saldo
  never above 10% of closing client CxC, excluding related-party
  transactions (the base excludes the FR-202 related splits) — a mismatch
  blocks filing with a reconciliation delta, never an auto-overwrite.
  (LB-005; LB-006; EV63:EVID-185)

### 3.6 Certification posture (R-H24)

- **HN-FREP-FR-215:** The system shall encode NO contador-certification
  casilla (R-H24: the exhaustive A-D inventory shows the sole attestation
  is the generic "Jura la exactitud y veracidad de la presente
  declaración"): the ISR Art. 28 requirement that the Balance/GyP be
  "certificadas por un contador hondureño titulado, o incorporado" is
  discharged by NO vehicle within the OVI 535 — the CPA attestation is an
  EXTERNAL document workflow attached to the EEFF record, never a 535
  casilla, with the vehicle question carried open (OQ-006).
  (LB-005; LB-007; EV13:EVID-073; EV63:EVID-185; R-H24)

### 3.7 Grid fidelity, freeze and historical ingestion

- **HN-FREP-FR-216:** The system shall write-protect every filed 535
  record (D-H2.5 freeze): after juramento/acuse the casilla values are
  immutable; a rectificativa reloads the original editable "casilla por
  casilla" per the CT Art. 117 chassis (file 01 by id) and creates a NEW
  snapshot record, with the histórico view showing originals and
  rectificativas side by side. (LB-005; LB-009; EV63:EVID-175/185)
- **HN-FREP-FR-217:** The system shall load the casilla grids as
  valid-at-read EDITION rows keyed to the print cycle — current edition =
  "202401", the FY2024 first-mandatory-year print — because grids were
  reconstructed from prose over screenshot-only images and may be
  incomplete (`67_ OQ-4`) and a FY2025 edition may change casillas
  (`67_ OQ-5`): filing under a newer edition requires grid
  re-verification first (config-gated, never silent reuse); the print has
  NO comparative columns, NO payment leg and NO bulk-upload contract
  (manual casilla entry + add-record panels only — the encoded UX
  contract). (LB-005; EV63:EVID-184/185; OQ-004/OQ-005)
- **HN-FREP-FR-218:** The system shall support D18 historical ingestion
  where the EEFF inform touches go-live data: prior-FY 535 declaration
  snapshots import as `is_historical` records (prior-FY
  declaration-snapshot tier) reconciled against the historical trial
  balance (balances tier), and any rectificativa of an imported prior-FY
  535 resolves its grid against the ORIGINAL-period edition rows
  (FR-217), never the current grid — go-live straddle-FY filings use the
  straddle-FY detail tier. (LB-005; LB-006; EV13:EVID-072;
  EV63:EVID-185)

## 4. Data Model

Machine-readable sidecar next to this file: none — the casilla grid is
prose-reconstructed over screenshot-only sources (`67_ OQ-4`), so a
published CSV would assert fidelity the evidence cannot support; the grid
lives as seeded data rows tagged with their edition. Dated parameters are
additive `valid_from`/`valid_to` rows (D-H2) resolved by the declared
period, snapshot-on-write (D15).

**The 535 declaration object:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.eeff.report (new) | company_id, fiscal_year, period_key | m2o/char(4)/char(6) | period_key = YYYY + "01" (202401 convention) | FR-191 |
| l10n_hn.eeff.report | state, grid_edition, is_historical | select/char/boolean | chassis states from file 01; grid_edition default "202401"; is_historical per D18 | FR-194, FR-216..218 |
| l10n_hn.eeff.report | window_row_id, special_period_close, due_date | m2o/date/date | dated per-FY rows; +3m extension consumes taxation/01 FR-016 | FR-191, FR-193 |
| l10n_hn.eeff.report | total_activos, total_pasivos, total_patrimonio, equation_ok | monetary/computed | accounting-equation live check (Activo = Pasivo + Patrimonio) | FR-195, FR-201 |
| l10n_hn.eeff.report | gate_state, certification_attachment_id | computed/binary | gate_state: satisfied · missing · carve_out (pre-FY2024 omisa/rectificativa); external CPA evidence document (R-H24) | FR-197..199, FR-215 |

**Casilla contract and panels:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.eeff.casilla (new) | report_id, section, node_path, caption_es, amount | m2o/select/char/char/monetary | section: a_activos · b_pasivos · c_patrimonio · d_resumen; tree paths per FR-202..206 | FR-201..206 |
| l10n_hn.eeff.casilla | is_current, related_split, atn_feed | boolean/select/select | related_split: none · rel_local_period · rel_exterior_period · rel_local_prior · rel_exterior_prior · unrelated; atn_feed: none · integral · contra | FR-202, FR-211, FR-212 |
| l10n_hn.eeff.panel.socio (new) | report_id, socio_name, amount, transaction_date, capital_pct | m2o/char/monetary/date/float | per-socio CxC detail (local/foreign) | FR-207 |
| l10n_hn.eeff.panel.provider (new) | report_id, rtn, provider_name, amount, aging_months | m2o/char(14)/char/monetary/integer | per-provider CxP detail; RTN 14-position validation | FR-208 |
| l10n_hn.eeff.panel.loan (new) | report_id, lender_name, loan_number, amount, kind, purchased_asset_casilla_id | m2o/char/char/monetary/select/m2o | kind: bancario_local · bancario_exterior · hipotecario · ppe_purchase; asset link for ppe_purchase | FR-209 |
| l10n_hn.eeff.panel.transit (new) | report_id, description, poliza_number, amount | m2o/char/char/monetary | mercadería en tránsito detail | FR-202 |

**Dated parameters:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.eeff.parameter (new) | key, value, valid_from, valid_to, note | char/char/date/date/char | gate_535 (valid_from FY2024); window rows per FY (Jan-1→Apr-30; +3m special); atn_autofill (valid_from 202401); grid_edition rows (valid-at-read, "202401") | FR-191, FR-193, FR-197, FR-213, FR-217 |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` = report generation, casilla mapping
and validation logic living in the LGPL client. No SaaS rows are
introduced: HN has no XML/DTE transmission surface for declarations in the
corpus — the OVI payload is a client-side export contract owned by file 01
(clusters F1/E8 lead 1 kin). Model names stable across Odoo 17/18/19/20;
version-specific behavior recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-191, FR-193 | odoo | l10n_hn.eeff.report + l10n_hn.eeff.parameter | period_key, window rows | D12: SAR-619-2024 vigencia 27-dic-2024 (LG 36,725); window rows annual, +3m special-FY rows consume taxation/01 FR-016 close date; D15/D16 snapshot-on-write, retro filings use original-period rows |
| FR-192, FR-196 | odoo | res.company flags + l10n_hn.fiscal.calendar (file 01) | subject scope, member row | Scope feeds file 07 FR-254 gate + FR-263 dashboard by id; 74_ RESUMEN membership consumed by id |
| FR-194, FR-216 | odoo | l10n_hn.eeff.report → chassis models (file 01) | state, acuse, rectificativa snapshot | D-H2.5 freeze; rectificativa = new record, original struck-through (CT Art. 117 chassis by id) |
| FR-195 | odoo | account.move.line aggregation + computed equation check | NIIF source mapping | NIIF anchor consumed from taxation/01 HN-TAX-FR-028 by id; out-of-equation blocks filing |
| FR-197..FR-200 | odoo | l10n_hn.eeff.parameter + gate_state computed | gate_535 dated rows | valid_from FY2024 / carve-out valid_to FY2023 (omisa/rectificativa only); consumer = file 07 FR-254 by id; DJ non-filed state per same-obligation doctrine |
| FR-201..FR-206 | odoo | l10n_hn.eeff.casilla (seeded tree) | sections A-D | GyP guard (OQ-001) blocks new groups until `67_ OQ-1` reconciled; tree maps onto the HN CoA/NIIF balance structure (chart-of-accounts topic consumer) |
| FR-207..FR-210 | odoo | l10n_hn.eeff.panel.* | socio/provider/loan/transit panels | Reconciled to res.partner (socio/provider), account.loan-equivalent data and the PPE asset records; superávit panel reconciles to taxation/05 FR-186 subledger by id |
| FR-211..FR-213 | odoo | l10n_hn.eeff.casilla.atn_feed + export payload | integral/contra flags | Feed consumed by file 07 FR-257..259 by id (validation-only UX from 202401); ATN computation/rate/exemption never here (file 07 OQ-010 pointer) |
| FR-214 | odoo | validation constraint vs provision ledger | art11 delta check | Provision computed by taxation/02 HN-TAX-FR-053 by id (1%/10%/excl. related); mismatch blocks, never overwrites |
| FR-215 | odoo | ir.attachment on l10n_hn.eeff.report | certification evidence | R-H24: no casilla; external CPA attestation document workflow only |
| FR-217 | odoo | l10n_hn.eeff.parameter (grid_edition rows) | valid-at-read editions | `67_ OQ-4`/`67_ OQ-5`: current edition "202401"; new edition requires re-verification (config gate); no comparatives/payment/bulk-upload in the print |
| FR-218 | odoo | l10n_hn.eeff.report (is_historical) + ingestion jobs | D18 tiers | Prior-FY declaration snapshots + balances reconciliation; rectificativa of imported rows resolves original-period grid rows (D16 filed-period protection kin) |

Version-regime notes (D12): the gate row records SAR-619-2024 (vigencia
27-dic-2024, binding FY2024 declarations filed 2025); the ATN autofill row
records its 202401 start; grid editions are valid-at-read pending
print-run pinning. Applicability (D15/D16/D18): dated parameters resolve
as-of the declaration's period anchor and snapshot on write; retro
rectificativas use original-period config rows; historical ingestion
follows the D18 tiers with `is_historical` rows.

## 6. Acceptance Criteria

- **AC-001:** Given a FY2025 calendar-year 535, then the window row reads
  2026-01-01→2026-04-30 and period_key = "202501"; given a special fiscal
  period closing 2025-09-30, then the due date = 2025-12-30 (3 months
  post-close) on its own dated row (FR-191, FR-193).
- **AC-002:** Given a persona jurídica and a PN comerciante individual,
  then both carry the 535 obligation; given a PN profesional not declared
  a comerciante individual, then no 535 obligation object exists for her
  (FR-192).
- **AC-003:** Given a FY2024+ ISR DJ attempted while the FY's 535 is
  unfiled, then gate_state = missing and the file 07 FR-254 consumer
  blocks; given a ≤FY2023 omisa DJ, then gate_state = carve_out and no
  535 is demanded (FR-197, FR-199).
- **AC-004:** Given a filed DJ whose 535 was never presented, then the DJ
  compliance state renders non-filed with the obligaciones-conexas flag
  (same-obligation doctrine), sanctions left to the CT frame by id
  (FR-198).
- **AC-005:** Given section totals where pasivos + patrimonio ≠ activos,
  then the equation check blocks filing with the delta shown in the
  summary panel (FR-195, FR-201).
- **AC-006:** Given an attempt to add a Ganancias-y-Pérdidas casilla group
  to the 535 grid, then the guard blocks it and surfaces the `67_ OQ-1`
  conflict flag — the form ships balance-sheet-only until reconciled vs
  the live OVI (FR-201, OQ-001).
- **AC-007:** Given socio X owed L50,000 from a 2026-03-02 transaction
  with 25% capital participation, then the per-socio panel emits (X,
  50000, 2026-03-02, 25%) (FR-207).
- **AC-008:** Given provider Y (RTN 08019012345678, 14 positions) owed
  L120,000 with
  the oldest unsettled invoice 7 months old, then the per-provider panel
  emits (RTN, Y, 120000, 7) (FR-208, OQ-009).
- **AC-009:** Given a bank loan for a machinery purchase, then the
  PPE-purchase-loan panel records lender, loan number, amount AND links
  the purchased asset to the Maquinaria casilla, with atn_feed = contra
  (FR-209, FR-212).
- **AC-010:** Given a superávit-revaluación balance of L800,000 in otro
  resultado integral and a taxation/05 FR-186 subledger balance of
  L800,000, then the panel passes; given L750,000 in the subledger, then a
  reconciliation flag blocks silent filing (FR-210).
- **AC-011:** Given any asset casilla (corriente or no corriente) with a
  nonzero amount, then it carries atn_feed = integral and appears in the
  aggregate Sección-D feed consumed by file 07 FR-257 by id (FR-211).
- **AC-012:** Given an Art. 11 provision ledger (taxation/02 FR-053) of
  L45,000 = min(1% × credit sales, 10% of closing client AR excl.
  related splits) and a consigned Estimaciones casilla of L50,000, then
  filing blocks with the L5,000 delta — never an auto-overwrite (FR-214).
- **AC-013:** Given a 103 for period 202501, then the ATN inputs autofill
  from the 535 with validation-only UX (file 07 FR-259 by id); given
  period 202312, then the DJ-side fields accept manual consignación
  (FR-213, FR-200).
- **AC-014:** Given the exhaustive A-D casilla inventory, then no
  contador/CPA certification field exists; the CPA attestation attaches
  as an external document and the only in-form attestation is the
  juramento (FR-215, R-H24).
- **AC-015:** Given a filed 535, then its casillas are immutable; given a
  rectificativa, then a NEW snapshot record is created from the editable
  original "casilla por casilla" and the histórico view shows both
  (FR-216).
- **AC-016:** Given a go-live importing the FY2024 535 of an acquired
  entity, then the record imports with is_historical = true reconciled to
  the historical trial balance, and a rectificativa of it resolves against
  the "202401" grid edition — never a newer grid (FR-217, FR-218).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `67_ OQ-1` [CONFLICT]: the Ayuda describes a balance-sheet-only 535 (A Activos / B Pasivos / C Patrimonio / D Resumen — no GyP section or casillas) while SAR-619-2024/SAR-236-2024 define it "integrado por el Balance General y Cuadros de Ganancias y Pérdidas" — either the Ayuda omits a GyP module or the form dropped it; FR-201 ships the guard and never resolves silently. Reconcile vs the live OVI 535. | no (guard ships) | Takumi S-HN3 + SAR confirmation | open |
| OQ-002 | `13_ OQ-2` [LEAD]: Reglamento Ley ISR Art. 84 (= "Acuerdo N°799", 4th citation first with number — `67_ OQ-3` kin; EV13:EVID-075 quote: SAR "determinará la forma y requisitos [...] y preparará y pondrá a disposición del contribuyente [...] los formularios") remains unlocated — never cite Reglamento Arts. 51/84 as acquired legal basis; the form-format delegation stands on the 619/67_ prints until acquired. | no | acquisition queue | open |
| OQ-003 | `67_ OQ-3` [LEAD] acquisition pack, cited inside 67_ only: "Acuerdo N°799" (ISR Reglamento, p.6), "Acuerdo No.1 del 01 de noviembre de 1975" (reglamento especial de depreciación y agotamiento, p.35), "acuerdo 0948-2003" (reglamento del Impuesto al Activo Neto, p.50), CNBS "Resolución GE No.180/06-02-2012" (activos eventuales, p.18) — none in corpus; class lists/panel semantics stand on the Ayuda prints. | no | acquisition queue | open |
| OQ-004 | `67_ OQ-4` [VERIFY]: the full casilla grids for activos corrientes/dep-recruitment panels (pp.10-11, 20-21, 27-29) and pasivos/patrimonio lists (pp.36-37, 45-47) are screenshot-only; casilla sets were reconstructed from prose and may be incomplete (esp. casillas never named in prose) — FR-217 edition discipline is the mitigation. | no | Takumi S-HN3 | open |
| OQ-005 | `67_ OQ-5` [VERIFY]: the print uses período "202401" (p.8) — the FY2024 first-mandatory-year edition; whether a FY2025 edition changes casillas (e.g. adds GyP, comparatives) is unknown — new editions gate filing behind re-verification (FR-217). | no | Takumi S-HN3 | open |
| OQ-006 | `13_ OQ-1` residue / `67_ OQ-2` struck → R-H24 [synthesis note]: NO contador/CPA/certification casilla exists anywhere in the 535 (exhaustive A-D inventory, EV63:EVID-185; sole attestation = generic juramento); whether ISR Art. 28's "certificadas por un contador hondureño titulado o incorporado" is discharged by a separate document/procedure outside OVI is NOT addressed by the corpus — FR-215 keeps an external-document workflow; vehicle remains open. | no | acquisition queue + SAR ruling | open |
| OQ-007 | File-local [CONFIG]: superávit-revaluación → Sección-D feed semantics stand on the 67_ p.50 citation of 0948-2003 (unacquired): whether the superávit reduces activos gravables, enters the contra set, or is reported-only for ATN purposes is unpinned — FR-210 reports and reconciles, computes nothing ATN-side; kin = file 07 OQ-010 (ATN instrument conflict, `74_ OQ-3`/R-H29 — pointer, never resolved here). | no | acquisition queue | open |
| OQ-008 | File-local [VERIFY]: the per-socio CxC panel vs the >100-day related-receivables deemed-dividend ledger (taxation/05 HN-TAX-FR-172 by id) — a reconciliation/linkage between the two surfaces is nowhere stated in the corpus; FR-207 ships them unlinked. | no | Takumi S-HN3 + taxation wave | open |
| OQ-009 | File-local [CONFIG]: "antigüedad saldo en meses" semantics — aging anchor (due date vs invoice date) and bucketing granularity are not defined by the Ayuda; FR-208 computes from the ledger's due-date convention with the mapping exposed as config. | no | Takumi S-HN3 | open |
| OQ-010 | File-local [VERIFY]: SAR-619-2024 resolutivo numbering prints SEXTO → SÉPTIMO → NOVENO (OCTAVO absent [sic], EV13:EVID-074) — print defect, no substantive loss; recorded so no ordinal-based cross-referencing relies on OCTAVO. | no | controller | open (recorded) |
| OQ-011 | File-local [CONFIG]: chassis/catalog cross-references to S-HN3 siblings — file 07 pinned (FR-221/254/257..259/263 by id); file 10 (TP 545 + informativas, cluster F10 — the parallel related-party disclosure surface) was a parallel write in progress at drafting time (ids not yet pinned on disk) — re-pin its ids at wave validation without renumbering this file; file 01 (OVI/SW chassis, HN-FREP-FR-001..040 pre-allocated, parallel write) referenced by path/cluster only. | no | Takumi S-HN3 controller | open |
