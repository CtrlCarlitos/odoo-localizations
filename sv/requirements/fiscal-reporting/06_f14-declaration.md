# SV — Fiscal reporting — F-14 declaration & retention annex: ISR retention projection, financial-operations tracks & Quincena-25 vintage

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for El Salvador's F-14 —
the monthly ISR retention declaration (*Declaración de Retenciones del
Impuesto sobre la Renta*, ISR retentions declaration) and its upload
annex, the *Anexo de Retenciones* (retentions annex), per the F-14 V16
user manual (OCTUBRE 2025, `35_`), the v16 plantilla sheet "Detalle"
(`37_`), the v16 form (`38_`) and the v17 form actualized 2026-06-03
(`59_`): the annex row model with its verbatim A-W column structure —
subject identification (domiciliado flag, 4-digit country code,
NIT-vs-foreign-NIF, DUI/NIT exclusive-or), the payroll column split
(*monto devengado* (amount accrued) including AFP and social-security
contributions while EXCLUDING *aguinaldos, bonificaciones y
gratificaciones* (year-end bonuses, bonuses and gratuities) for income
codes 01/60/80, the separate *bonificaciones* column, the
*aguinaldo* exento/gravado pair), the SEVEN social-security columns
with their legal caps mirrored as dated validation parameters (AFP
US$472.93 and ISSS US$30.00 as amount caps; INPEP 7.5%, IPSFA 9.5%,
CEFAFA 5%, Bienestar Magisterial 5.58% and ISSS-IVM 7.5% as
percentage maxima), the S-V ISR cost/gasto quartet (referenced, never
restated), the tax-haven 25% exactness warning, and the per-row period
MMYYYY; the export validation contract (retention percentage = legal
rate per income code, *aguinaldo gravado* ≤ *devengado*, SS-cap
enforcement, two-decimal truncation); the DECLARATION = PURE
PROJECTION invariant (every retention casilla auto-totals from the
annex, no manual casilla entry); the seven-tab form architecture
(*Pago a Cuenta* (payment on account) with its printed-but-dead
pago-mínimo remnant row, *Retenciones Renta Acreditables* con/sin
dependencia laboral (creditable retentions with/without labor
dependency), *Retenciones Renta Definitivas* (definitive retentions)
including the distributions block, the *Renta Operaciones
Financieras* financial-operations instrument tracks 501-529,
*Contribución Especial*, the *Retenciones No Domiciliados*
non-domiciled reduced-rate matrix, and *Agentes Extranjeros* (foreign
agents) 701-780); the *declaración modificatoria* (amended return)
flow (*limpiar* + full re-upload with prior-amount anchors); and the
F-14 v17 Quincena-25 form vintage (casillas 417/418 from 2026-06,
with the annex-level representation BLOCKED pending the v17 manual).

It does **not** cover: the F-14 income-code catalog and its semantics —
acreditable/definitiva/sin-retención/no-gravado classes, the code →
rate map, the distributions codes 43/44/45, the haven code 40 and the
CT 123 aggregate code 47 — owned by `07_codes-and-informs.md` §3 and
cited forward as file+§ only; the retention COMPUTATION itself (bases,
tables, thresholds and the CT matrix, owned by
`taxation/04_isr-withholding.md`
SV-TAX-FR-102/104/106/109/120..131; this file's annex REPORTS those
values, it never recomputes them); the social-security cap VALUES and
their ceiling bases plus the Quincena-25 payment mechanics (payroll
wave — SOQ-11/SOQ-09 feeds);
the F-07 declaration engine and its generic annex upload mechanics
(files 01-05 — the F-14 upload flow is governed by its own manual
`35_`, with F-07 §II conventions consumed by parity only where noted);
the F-910 annual consolidation rules and the F-935 detail format
(`07_codes-and-informs.md`); and the filing due-day calendar
(`08_filing-calendar.md` — SOQ-08; no deadline behavior is encoded
here).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and manuals ARE the primary
authority for declaration mechanics — 35_ (Manual de Usuario, Anexo de
Retenciones, F-14 V16, OCTUBRE 2025) governs the annex column model
and validations; 37_ (plantilla sheet "Detalle") is the operative
column template; 38_ anchors the v16 form layout and 59_ the v17 delta
(MH "Actualizado el 03/06/2026"). Version regime (D12): the v16 annex
mechanics are current (no v17 manual/plantilla exists — MH checked
2026-08-18); the form layout is v17 from the 2026-06 declaration
period (EVID-184). Legal anchors behind the printed rates are cited
per the S2 order through `taxation/04_isr-withholding.md` LB-016..019
(rates owned there, never restated here). Manual pages are printed
pages.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-14 v16 §1-2, Anexo de Retenciones, tabla de columnas (verbat): "A DOMICILIADO 1 / B CÓDIGO DE PAÍS 4 / C APELLIDOS, NOMBRES; RAZÓN O DENOMINACIÓN SOCIAL 100 / D NIT/NIF 14 / E DUI 9 / F CÓDIGO DE INGRESO 2 / G MONTO DEVENGADO 12 / H MONTO DEVENGADO POR BONIFICACIONES Y GRATIFICACIONES 12 / I IMPUESTO RETENIDO 12 / J AGUINALDO EXENTO 6 / K AGUINALDO GRAVADO 12 / L AFP 6 / M ISSS 5 / N INPEP 5 / O IPSFA 5 / P CEFAFA 5 / Q BIENESTAR MAGISTERIAL 5 / R ISSS IVM 5 / S TIPO DE OPERACIÓN 1 / T CLASIFICACIÓN 1 / U SECTOR 1 / V TIPO DE COSTO / GASTO 1 / W PERÍODO 6"; A: "1 Domiciliado / 2 No Domiciliado"; B: "4 caracteres ... de acuerdo a la tabla de código de países ... Ejemplo: 9300 ... si corresponde a paraíso fiscal, el sistema le advertirá que la retención no debe ser inferior o mayor del 25%. La lista vigente de países ... se encuentra publicada en la página web del Ministerio de Hacienda"; D: NIT local o "Número de Identificación Fiscal del país de origen del Sujeto de Retención, no domiciliado"; DUI-vs-NIT/NIF XOR desde enero 2022 (personas naturales domiciliadas); S-V: códigos Renta idénticos al Anexo 3 del F-07 (1/2/3/4; 1 Costo/2 Gasto; sectores 1-4; tipo costo/gasto 1-7) — "aplica a partir del periodo de Febrero 2024"; códigos 8/9 como el F-07 (multi-anexo 8; instituciones públicas/municipalidades/no inscritos IVA/no deducibles 9); W: "Período: 6 dígitos, sin plecas, con la siguiente estructura: MMYYYY"; nota plantilla 37_ (encabezado col G): "Monto Devengado (Para código de ingreso 01, 60 y 80: incluir AFP y Cotizaciones Sociales si aplican, No Incluir Aguinaldos, Bonificaciones y Gratificaciones)" | F-14 v16 manual §1-2: the retentions-annex column table A-W verbatim with printed widths — domiciled flag (1/2), 4-digit country code with the tax-haven warning (retention must be neither below nor above 25%; the current country list is published on the MH website), name (100), NIT or the foreign Fiscal Identification Number of the non-domiciled retention subject (14), DUI (9), income code (2), accrued amount (12), accrued amount for bonuses and gratuities (12), tax retained (12), exempt year-end bonus (6), taxable year-end bonus (12), the seven SS columns (6/5/5/5/5/5/5), the ISR quartet (1/1/1/1) applying from Febrero-2024 identical to F-07 Anexo 3 with codes 8/9 as there, and the period MMYYYY (6 digits, no slashes); the plantilla header note: for income codes 01/60/80 the accrued amount INCLUDES AFP and social contributions when applicable and EXCLUDES year-end bonuses, bonuses and gratuities | `sv/sources/35_F14_v16_manual.pdf` + `sv/sources/37_F14_v16_plantilla.xls` | §1-2 pp.2-5; 37_ sheet "Detalle" (EVID-180) |
| LB-002 | Manual F-14 v16 §2, columnas L-R con topes legales (verbat): "AFP: ... siendo el monto máximo de cotización $472.93, de acuerdo a la Ley" / "ISSS: ... monto máximo de cotización 30.00" / "INPEP: ... porcentaje máximo de cotización del 7.5% del monto devengado" / "IPSFA: ... 9.5%" / "CEFAFA: ... 5%" / "Bienestar Magisterial: ... 5.58%" / "ISSS/IVM: ... 7.5%" | F-14 v16 manual §2: the seven social-security columns carry legal maxima — AFP maximum contribution amount US$472.93 and ISSS US$30.00 (amount caps); INPEP maximum contribution percentage 7.5% of the accrued amount, IPSFA 9.5%, CEFAFA 5%, Bienestar Magisterial 5.58%, ISSS/IVM 7.5% (percentage maxima); printed Oct-2025 = a dated snapshot of values whose feed and ceiling bases belong to the payroll wave (SOQ-11) | `sv/sources/35_F14_v16_manual.pdf` | §2 pp.2-5 zone (EVID-180) |
| LB-003 | Manual F-14 v16 §2-6, "NOTAS IMPORTANTES" + pantalla de inconsistencias (verbat): "1. En las columnas que contienen valores con decimales, en caso de ingresar con más de 2 decimales, el Sistema tomará únicamente 2. 2. Los ingresos en concepto de servicios de carácter permanente con subordinación o dependencia laboral, deben ser reportados en su totalidad en los códigos 01, 60 y 80, según corresponda. 3. Debe tomar en cuenta los montos máximos de las cotizaciones de seguridad social ... En caso se ingresen cantidades que superen los límites legales, el sistema le enviará mensaje de error. 4. ... los porcentajes de Retención aplicados a cada monto sujeto, deben corresponder con los porcentajes establecidos en la Ley para cada concepto, pues si ingresa montos retenidos superiores o inferiores a los montos legales, el sistema lo tomará como inconsistencia ... y no le permitirá cargar el archivo, hasta que la inconsistencia sea subsanada"; ejemplos del sistema: "Monto Aguinaldo gravado no puede ser mayor al monto devengado" / "Monto Retenido no puede ser diferente al 10% sobre el monto devengado" / "... 30% ..." / "... 20% ..." | F-14 v16 manual §2-6, important notes + system inconsistency screen: (1) decimal values with more than 2 decimals — the system takes only 2; (2) permanent-service income with labor subordination/dependency is reported IN ITS ENTIRETY in codes 01/60/80 as applicable; (3) the social-security contribution maxima apply — amounts above the legal limits trigger a system error message; (4) the retention percentages applied to each subject amount must match the legal percentages per concept — higher or lower retained amounts are an inconsistency and the file cannot be loaded until fixed (system examples print the 10%/20%/30% checks and the taxable-bonus ≤ accrued-amount check) | `sv/sources/35_F14_v16_manual.pdf` | §2-6 pp.5, 7, 9-13 (EVID-181) |
| LB-004 | Manual F-14 v16 §2-6, carga y modificatoria (verbat): "Con la carga de este anexo ... se llenarán todas las casillas correspondientes a cada concepto de Retención ... ninguna de las casillas de Retenciones o de Montos no Sujetos a Retención se llenará de forma manual"; "Previo a realizar el proceso de presentación de declaración modificatoria, debe sustituir el archivo previamente cargado, por el nuevo ... clic en el botón limpiar, esto eliminará los datos presentados en la declaración anterior"; anclas de verificación por pestaña: casilla 50 (pago a cuenta), 221 (acreditables con dependencia), 225 (acreditables sin dependencia), 332 (definitivas), 711 (agentes extranjeros retención), 761 (agentes extranjeros entero) = montos pagados en la declaración anterior | F-14 v16 manual §2-6: with the annex loaded, ALL retention casillas fill automatically and NONE of the retention or non-subjected-amount casillas is filled manually; before presenting an amended declaration the previously loaded file must be replaced by the new one via the limpiar (clear) button, which deletes the data presented in the prior declaration; per-tab verification anchors: casillas 50/221/225/332/711/761 = the amounts paid in the prior declaration | `sv/sources/35_F14_v16_manual.pdf` | §2-6 pp.5, 7, 9-13 (EVID-181) |
| LB-005 | Formulario F-14 v16 (38_), arquitectura de pestañas y casillas: pestañas "Pago a Cuenta / Retenciones Renta Acreditables / Retenciones Renta Definitivas / Renta Oper. Financieras / Contribución Especial / Retenciones No Domiciliados / Agentes Extranjeros"; Pago a Cuenta: filas 1-8 → 214/207/208 (ingresos gravables/no incluidos por retención), 215/219/220 (entero computado/excedentes), bloque 42-56 incl. "Entero Cancelado de Pago a Cuenta en Declaracion que Modifica" (42), "Acreditamiento del Excedente del Resultante del Impuesto Por Pago Minimo menos el Impuesto Computado de la Renta Ordinaria" (zona 44/45 — fila impresa), "Ajuste por Disminucion de Saldo en Declaracion del Impuesto sobre la Renta Modificada, por Aplicacion del Art 74-A del C.T." (46), "Acreditación de Reintegro de IVA Exportador Autorizado" (48), 50-56 (total a pagar / excedente próximo período); Acreditables: dependencia laboral filas 10-27 → 104/105 (nº sujetos/monto gravado) + zona impuesto 150/151/152/154/156/158/160/162/164, totales 221/225; sin dependencia (honorarios, arrendamientos, agropecuaria, juicios, premios, intangibles, rendimientos); fila 58 "Ingresos gravados sin retención" (zona 104/105) + filas 59-60 "INGRESOS NO GRAVADOS" (zona casilla 416 aguinaldo exento); Definitivas filas 28-46 → 230-336 incl. 296-328 (distribuciones 43-46, préstamos 46/81-82, otras 42/83, remuneraciones inversionistas 49/84) y totales 330-336; No Domiciliados filas 62-79 → 250-314 (pistas 20%/5%/10%); Operaciones Financieras filas 99-104 → "Para el Control de la Liquidez (Acreditable ...)" 501-504, "Al Cheque (Entero definido, no acreditable ...)" 505-507, "A las Transferencias Electrónicas" 525-529, "Por Operaciones en el Mercado de Valores" 519-521; Agentes Extranjeros filas 88-98 → retención 701-703/710-720, entero donantes locales 751-753/760-780 | F-14 v16 form, tab/casilla map: seven tabs; Pago a Cuenta rows 1-8 → 214/207/208 and 215/219/220 plus the 42-56 block (42 amount paid on account in the amended declaration; the pago-mínimo excedente row 44/45 zone still PRINTED; the Art. 74-A CT balance-diminution adjustment 46; authorized IVA-exporter refund credit 48; 50-56 totals/excedente); Acreditables with labor dependency rows 10-27 → 104/105 subject-count/taxed-amount pairs + the 150-164 impuesto zone, totals 221/225, plus the without-dependency rows and the sin-retención row 58 and INGRESOS NO GRAVADOS rows 59-60 (aguinaldo exento, casilla 416 zone); Definitivas rows 28-46 → 230-336 incl. the 296-328 distributions/loans/investor-remuneration block and totals 330-336; No Domiciliados rows 62-79 → 250-314 with the 20%/5%/10% reduced-rate tracks; Operaciones Financieras rows 99-104 → liquidity-control creditable 501-504 vs definitive cheque 505-507 / electronic transfers 525-529 / securities-market 519-521; Agentes Extranjeros rows 88-98 → retention 701-703/710-720 and local-donor remittance 751-753/760-780 | `sv/sources/38_F14_v16_form_visual.pdf` | pp.1-3 (EVID-183) |
| LB-006 | Manual F-14 v16 pp.19-23, tabla de códigos de país: 4 dígitos, "9300 EL SALVADOR ...", banda 99xx estados de EE.UU. (9900-9903 DELAWARE/NEVADA/WYOMING...); vigencia publicada en la página web del Ministerio de Hacienda | F-14 v16 manual country-code table: 4-digit codes, 9300 El Salvador, the 99xx US-states band (9900-9903 Delaware/Nevada/Wyoming...); the current list is published on the MH website (dated data) | `sv/sources/35_F14_v16_manual.pdf` | pp.19-23 (EVID-183) |
| LB-007 | Formulario F-14 v17 (59_, MH "F14v17 ... Actualizado el 03/06/2026"), sección nueva en p.2 tras la fila 58: "INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO Número de Sujetos Monto Quincena 25" + fila "61 Ingresos No Gravados Pagados por el Agente de Retención Quincena 25 417 0 0 418 0.00 5"; consecuencia: filas 61-104 de la v16 renumeradas → 62-105 en la v17; casillas aritméticas estables (330/332/334/336, 501-529, 701-780); sin otro cambio de contenido (diciembre/junio recálculo sin cambios); NO existe manual/plantilla v17 (MH verificada 2026-08-18) | F-14 v17 form, the Quincena-25 change: a new section "NON-TAXED INCOME SPECIAL LAW QUINCENA VEINTICINCO" after row 58 with row 61 — number of subjects (casilla 417) and amount (casilla 418) of Quincena-25 non-taxed income paid by the retention agent; v16 rows 61-104 renumber to 62-105; all arithmetic casillas unchanged; no other content change; no v17 manual/plantilla exists (MH checked 2026-08-18 — annex-level representation unknown) | `sv/sources/59_F14_v17_form_visual.pdf` | pp.1-3 (EVID-184) |
| LB-008 | Código Tributario, Arts. 154-160 (ancla legal de la matriz de retenciones impresa en el F-14): agentes y momento de retención (154); matriz de honorarios/arrendamientos/intangibles/rendimientos (156-156-B); no residentes 20% definitivo con tasas reducidas 5%/10% y paraísos fiscales 25% (158/158-A); instituciones financieras y operaciones financieras (159); premios (160) — citado por referencia a través de `taxation/04_isr-withholding.md` LB-016..019 (las tasas son propiedad de ese archivo) | Tax Code Arts. 154-160 — the legal anchor behind the F-14's per-code retention percentages, the non-domiciled 20%/5%/10% tracks, the tax-haven 25% exactness and the financial-operations tracks; cited by reference through the taxation file (rates never restated here) | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 154-160 pp.83-90 zone (EVID-062/063, via taxation/04 LB-016..019) |

## 3. Functional Requirements

### 3.1 Annex row model and subject identification

- **SV-FREP-FR-137:** The system shall build the F-14 *Anexo de
  Retenciones* (retentions annex) with ONE ROW per retention subject
  and income code for the declared period — including rows for
  remunerations NOT retained (the below-table payroll code 60 and the
  no-gravado codes 70-72, class semantics owned by
  `07_codes-and-informs.md` §3) — emitting the verbatim v16 column
  model A-W in exactly this order with the printed widths: **A
  DOMICILIADO (1: 1 Domiciliado / 2 No Domiciliado)** · **B CÓDIGO DE
  PAÍS (4)** · **C APELLIDOS, NOMBRES; RAZÓN O DENOMINACIÓN SOCIAL
  (100)** · **D NIT/NIF (14)** · **E DUI (9)** · **F CÓDIGO DE INGRESO
  (2)** · **G MONTO DEVENGADO (12)** · **H MONTO DEVENGADO POR
  BONIFICACIONES Y GRATIFICACIONES (12)** · **I IMPUESTO RETENIDO
  (12)** · **J AGUINALDO EXENTO (6)** · **K AGUINALDO GRAVADO (12)** ·
  **L AFP (6)** · **M ISSS (5)** · **N INPEP (5)** · **O IPSFA (5)** ·
  **P CEFAFA (5)** · **Q BIENESTAR MAGISTERIAL (5)** · **R ISSS IVM
  (5)** · **S TIPO DE OPERACIÓN (1)** · **T CLASIFICACIÓN (1)** ·
  **U SECTOR (1)** · **V TIPO DE COSTO / GASTO (1)** · **W PERÍODO
  (6)** — conforming to plantilla sheet "Detalle" as the operative
  column template. (LB-001; EVID-180)
- **SV-FREP-FR-138:** The system shall fill the subject
  identification columns as: A = the domiciled flag (1 Domiciliado /
  2 No Domiciliado); B = the 4-digit country code from the MH table
  (FR-139) REQUIRED for non-domiciled rows (domiciled rows carry El
  Salvador 9300); D = the LOCAL NIT for domiciled subjects or the
  *Número de Identificación Fiscal* (Fiscal Identification Number) of
  the country of origin for non-domiciled retention subjects; C = the
  subject's name or business name. (LB-001; EVID-180)
- **SV-FREP-FR-139:** The system shall load the MH country-code table
  (4 digits; 9300 EL SALVADOR; the 99xx US-states band 9900-9903
  DELAWARE/NEVADA/WYOMING...) as DATED data with a per-code tax-haven
  flag, seedable and refreshable from the MH web publication ("La
  lista vigente de países ... se encuentra publicada en la página web
  del Ministerio de Hacienda" — acquisition cadence OQ-007); the haven
  classification feeds FR-141. (LB-001; LB-006; EVID-180; EVID-183)
- **SV-FREP-FR-140:** The system shall enforce the DUI-vs-NIT/NIF
  exclusive-or for domiciled NATURAL persons with its Enero-2022 gate:
  from the Enero-2022 period a natural person states either the DUI
  (E filled ⇒ D empty) or the NIT (D filled ⇒ E empty), never both;
  before Enero-2022 the NIT is mandatory with E empty; juridical
  persons and non-domiciliados carry D only with E empty (the DUI is a
  Salvadoran natural-person document — family-convention inference
  from the XOR's printed natural-person scope, cf. 04-file OQ-005
  kin); violations block the export. (LB-001; EVID-180)
- **SV-FREP-FR-141:** The system shall apply the tax-haven 25%
  EXACTNESS check: when a row's country code (B) carries the haven
  flag, the system shall block the export with the manual's warning —
  "si corresponde a paraíso fiscal, el sistema le advertirá que la
  retención no debe ser inferior o mayor del 25%" (the system will
  warn that the retention must be neither below nor above 25%) — i.e.
  I (IMPUESTO RETENIDO) must equal exactly 25% of the retention base
  for haven rows; the haven retention rule itself is owned by
  `taxation/04_isr-withholding.md` SV-TAX-FR-127 (CT Art. 158-A —
  consumed by reference). (LB-001; LB-008; EVID-180; cross-ref
  SV-TAX-FR-127)
- **SV-FREP-FR-142:** The system shall fill F (CÓDIGO DE INGRESO)
  with a two-digit code from the F-14 apéndice income-code catalog —
  whose code list, legal-rate map and
  acreditable/definitiva/sin-retención/no-gravado classes are OWNED by
  `07_codes-and-informs.md` §3 and cited forward by file+§ (never
  restated here) — validating membership at export and routing every
  row to its form track by class: acreditable → the Acreditables tab
  (FR-155), definitiva → the Definitivas tab (FR-157), sin-retención
  60 → row 58 (FR-156), no-gravados 70-72 + aguinaldo exento → the
  INGRESOS NO GRAVADOS rows (FR-156), distributions codes 43/44/45 →
  the 296-328 block (FR-157), and the CT 123 aggregate code 47 (NIT
  of 14 zeros + "VARIOS") emitted as its aggregation-row mechanics
  (subject identification per code-47 rules owned by 07 §3).
  (LB-001; EVID-180; EVID-182; forward-ref `07_codes-and-informs.md`
  §3)

### 3.2 Payroll columns: devengado split, aguinaldo pair, social-security caps

- **SV-FREP-FR-143:** The system shall fill the payroll-remuneration
  columns of income codes 01/60/80 per the 37_ plantilla header note —
  G (MONTO DEVENGADO) INCLUDES the AFP and social-security
  contributions when applicable and EXCLUDES the *aguinaldos,
  bonificaciones y gratificaciones* ("Para código de ingreso 01, 60 y
  80: incluir AFP y Cotizaciones Sociales si aplican, No Incluir
  Aguinaldos, Bonificaciones y Gratificaciones"); H carries the
  accrued amount for *bonificaciones y gratificaciones* separately;
  and permanent-service income with labor subordination or dependency
  is reported IN ITS ENTIRETY in codes 01/60/80 as corresponds
  ("deben ser reportados en su totalidad en los códigos 01, 60 y 80,
  según corresponda"). (LB-001; LB-003; EVID-180; EVID-181)
- **SV-FREP-FR-144:** The system shall fill the aguinaldo pair J
  (AGUINALDO EXENTO) / K (AGUINALDO GRAVADO) implementing the
  Art. 4.16 two-SMM split computed by
  `taxation/04_isr-withholding.md` SV-TAX-FR-120 (the exempt floor
  and the floor-deducted excess — consumed by reference; the SMM feed
  belongs to the payroll wave): J carries the exempt portion and K
  the retained portion of each subject's aguinaldo, subject to the
  K ≤ G validation of FR-149. (LB-001; EVID-180; cross-ref
  SV-TAX-FR-120)
- **SV-FREP-FR-145:** The system shall fill the SEVEN social-security
  columns L AFP · M ISSS · N INPEP · O IPSFA · P CEFAFA · Q BIENESTAR
  MAGISTERIAL · R ISSS IVM and validate them against the legal caps
  mirrored as DATED validation parameters: amount caps AFP
  US$472.93 and ISSS US$30.00; percentage maxima over the accrued
  amount INPEP 7.5%, IPSFA 9.5%, CEFAFA 5%, Bienestar Magisterial
  5.58%, ISSS-IVM 7.5% — the printed Oct-2025 values are a snapshot
  whose feed, cadence and ceiling bases belong to the payroll wave
  (SOQ-11/OQ-002); this file mirrors them for collection-side
  validation only and encodes no cap theory. (LB-002; EVID-180)

### 3.3 Classification and period columns

- **SV-FREP-FR-146:** The system shall fill the S/T/U/V columns
  (TIPO DE OPERACIÓN / CLASIFICACIÓN / SECTOR / TIPO DE COSTO/GASTO)
  under the CANONICAL ISR cost/gasto quartet owned by
  `03_f07-annexes-purchases.md` SV-FREP-FR-079..085 — the
  Febrero-2024 gate ("0" before), the verbatim code lists, and codes
  8 (multi-annex dedup) and 9 (public institutions/municipalities/
  non-IVA-registered/non-deductible) — referenced by id only; the F-14
  manual prints the quartet as identical to F-07 Anexo 3 and this
  file RESTATES none of it. (LB-001; EVID-180; cross-ref
  SV-FREP-FR-079..085)
- **SV-FREP-FR-147:** The system shall fill W (PERÍODO) as 6 digits,
  no slashes, structure MMYYYY ("W. Período: 6 dígitos, sin plecas,
  con la siguiente estructura: MMYYYY"), and shall validate that
  every row's period matches the declaration's declared tax period —
  rows of other periods are rejected (period consistency by parity
  with the upload-family convention of `01_f07-declaration.md`
  SV-FREP-FR-032; the F-14 notas print the W structure, not the
  mismatch rejection). (LB-001; EVID-180; cross-ref SV-FREP-FR-032)

### 3.4 Export validation contract (MH-parity pre-validation)

- **SV-FREP-FR-148:** The system shall pre-validate every row's I
  (IMPUESTO RETENIDO) against the LEGAL RATE of the row's income code
  — "los porcentajes de Retención aplicados a cada monto sujeto,
  deben corresponder con los porcentajes establecidos en la Ley para
  cada concepto" — with MH rejection parity: an inconsistent file
  cannot be loaded into MH ("no le permitirá cargar el archivo, hasta
  que la inconsistencia sea subsanada"), so Odoo shall refuse the
  EXPORT until every row's retained amount equals the code's rate ×
  its base (the system's printed 10%/20%/30% checks); the rate per
  code is CONSUMED from the ISR matrix of
  `taxation/04_isr-withholding.md` by FR id — the CT 154-160 matrix
  rules SV-TAX-FR-121..131 and the payroll-table engine SV-TAX-FR-109
  on the SV-TAX-FR-104 base — never redefined here.
  (LB-003; LB-008; EVID-181; cross-ref SV-TAX-FR-104/109/121..131)
- **SV-FREP-FR-149:** The system shall reject any row whose K
  (AGUINALDO GRAVADO) exceeds G (MONTO DEVENGADO) — "Monto Aguinaldo
  gravado no puede ser mayor al monto devengado" — with the manual's
  inconsistency-message parity. (LB-003; EVID-181)
- **SV-FREP-FR-150:** The system shall reject any row whose
  social-security column values exceed the legal caps of FR-145 —
  "En caso se ingresen cantidades que superen los límites legales, el
  sistema le enviará mensaje de error" — surfacing the cap error per
  column before export. (LB-002; LB-003; EVID-180; EVID-181)
- **SV-FREP-FR-151:** The system shall apply the printed numeric
  discipline to every decimal-valued column: values entered or
  computed with more than two decimals are TRUNCATED to two ("el
  Sistema tomará únicamente 2"), nil amounts are emitted as 0.00, and
  the FR-140 DUI/NIT exclusive-or is enforced as an export gate
  alongside. (LB-003; LB-001; EVID-181)

### 3.5 The declaration as pure projection of the annex

- **SV-FREP-FR-152:** The system shall implement the F-14 declaration
  as a PURE PROJECTION of the annex: with the annex loaded, ALL
  casillas corresponding to each retention concept fill automatically,
  and NO retention or non-subjected-amount casilla is ever manually
  editable — "se llenarán todas las casillas correspondientes a cada
  concepto de Retención ... ninguna de las casillas de Retenciones o
  de Montos no Sujetos a Retención se llenará de forma manual";
  non-annex input casillas exist ONLY in the Pago a Cuenta block
  (FR-162: prior-modified-declaration amounts, the Art. 74-A CT
  adjustment, the IVA-exporter refund credit), never on the retention
  tabs. (LB-004; EVID-181)
- **SV-FREP-FR-153:** The system shall aggregate the annex rows into
  the form casillas per income code: each code's track receives the
  subject COUNT (número de sujetos), the gravado amount and the
  retained tax of its rows — count from distinct subjects, amounts
  summed under the FR-151 two-decimal discipline — so that every
  casilla of FR-155..163 is a total over annex rows and nothing else.
  (LB-005; LB-004; EVID-183; EVID-181)

### 3.6 Form architecture: the seven tabs

- **SV-FREP-FR-154:** The system shall render the F-14 form as a
  casilla-keyed, VINTAGE-GATED form mirror with the seven printed
  tabs — Pago a Cuenta · Retenciones Renta Acreditables ·
  Retenciones Renta Definitivas · Renta Oper. Financieras ·
  Contribución Especial · Retenciones No Domiciliados · Agentes
  Extranjeros — every casilla labeled and positioned per the form
  layout of the declaration period's vintage: v16 (38_) for periods
  before 2026-06 and v17 (59_) from 2026-06 (FR-165); casilla
  values are projections per FR-152/153. (LB-005; LB-007; EVID-183;
  EVID-184)
- **SV-FREP-FR-155:** The system shall project the acreditable rows
  into the Retenciones Renta Acreditables tab: the CON DEPENDENCIA
  LABORAL rows 10-27 with their per-code subject-count / gravado
  pairs (casilla zone 104/105) and the impuesto zone (150/151/152/
  154/156/158/160/162/164 as printed), totaling casillas 221 (with
  dependency) and 225 (without dependency); the SIN DEPENDENCIA rows
  (honorarios, arrendamientos, agropecuaria, juicios, premios,
  intangibles, rendimientos) follow the same per-code pair pattern;
  the code→row/casilla assignment within each family follows the
  income-code catalog (`07_codes-and-informes.md` §3, forward ref).
  (LB-005; EVID-183; forward-ref `07_codes-and-informes.md` §3)
- **SV-FREP-FR-156:** The system shall project the non-retained and
  non-taxed rows into row 58 "Ingresos gravados sin retención"
  (taxed income without retention — the code-60 aggregate, in the
  104/105 casilla zone) and into the "INGRESOS NO GRAVADOS" rows
  59-60 (the aguinaldo-exento aggregate in the casilla-416 zone and
  the no-gravado codes 70-72) — reporting-only tracks that enter no
  retention total. (LB-005; EVID-183; EVID-182; forward-ref
  `07_codes-and-informs.md` §3)
- **SV-FREP-FR-157:** The system shall project the definitiva rows
  into the Retenciones Renta Definitivas tab (rows 28-46 → casillas
  230-336), including the 296-328 block — the distributions codes
  43-46, loans 46/81-82, otras 42/83 and remuneraciones
  inversionistas 49/84 (the distributions codes' semantics and their
  earnings-register feed are owned by `07_codes-and-informes.md` §3
  and `taxation/05_isr-distributions.md` §3 respectively — forward
  references) — with the tab totals 330-336 computed per the printed
  formulas over the projected casillas. (LB-005; EVID-183;
  forward-ref `07_codes-and-informes.md` §3)
- **SV-FREP-FR-158:** The system shall project the non-domiciled
  rows (A = 2) into the Retenciones No Domiciliados tab (rows 62-79
  v16 numbering → casillas 250-314) through its reduced-rate tracks —
  the 20% general track and the 5%/10% reduced tracks — keyed to the
  CT Art. 158 matrix consumed from `taxation/04_isr-withholding.md`
  SV-TAX-FR-126 (rate assignment by reference; no rate restated).
  (LB-005; LB-008; EVID-183; cross-ref SV-TAX-FR-126)
- **SV-FREP-FR-159:** The system shall classify financial-operations
  retentions by INSTRUMENT into the Renta Oper. Financieras tracks
  (rows 99-104 → the 501-529 zone): *Para el Control de la Liquidez*
  (for liquidity control — ACREDITABLE) → casillas 501-504; *Al
  Cheque* (by check — *entero definido*, definitive non-creditable)
  → 505-507; *A las Transferencias Electrónicas* (electronic
  transfers) → 525-529; *Por Operaciones en el Mercado de Valores*
  (securities-market operations) → 519-521 — the instrument class
  determines the track and its acreditable-vs-definitive character;
  the CT article anchor and rates of the liquidity-control-vs-
  definitive split are re-checked against the CT 159 zone (OQ-003).
  (LB-005; LB-008; EVID-183)
- **SV-FREP-FR-160:** The system shall render the Contribución
  Especial tab as a form-mirror surface per the v16/v17 layout, its
  casillas projected from the annex rows whose income codes the
  catalog (`07_codes-and-informes.md` §3, forward ref) assigns to the
  contribución especial track. (LB-005; EVID-183; forward-ref
  `07_codes-and-informs.md` §3)
- **SV-FREP-FR-161:** The system shall project the foreign-agent rows
  into the Agentes Extranjeros tab (rows 88-98 → casillas 701-780):
  the RETENCIÓN block (701-703/710-720) and the ENTERO donantes
  locales (local donors' remittance) block (751-753/760-780); the
  transfer-level detail behind this tab is the F-935 inform, owned by
  `07_codes-and-informs.md` (forward reference); the donantes-locales
  normative anchor stays open with that file (SOQ-13 kin — cf.
  35_-file OQ-4 family). (LB-005; EVID-183; forward-ref
  `07_codes-and-informs.md`)
- **SV-FREP-FR-162:** The system shall render the Pago a Cuenta tab
  (rows 1-8) with casillas 214/207/208 (gravable income / income not
  included by retention), 215/219/220 (computed remittance /
  excedentes) and the 42-56 block — 42 *Entero Cancelado de Pago a
  Cuenta en Declaración que Modifica* (amount paid on account in the
  amended declaration), 46 *Ajuste por Disminución de Saldo ... por
  Aplicación del Art. 74-A del C.T.* (balance-diminution adjustment
  on an amended ISR declaration, per the printed CT 74-A anchor —
  consumed as an input from the amended-declaration flow, regime
  substance cross-file), 48 *Acreditación de Reintegro de IVA
  Exportador Autorizado* (authorized IVA-exporter refund credit), and
  the 50-56 total-a-pagar / excedente-próximo-período casillas —
  these being the declaration's ONLY non-annex input casillas (per
  FR-152), each stored with its printed source reference.
  (LB-005; EVID-183)
- **SV-FREP-FR-163:** The system shall carry the pago-mínimo remnant
  row of the Pago a Cuenta tab — "Acreditamiento del Excedente del
  Resultante del Impuesto Por Pago Minimo menos el Impuesto Computado
  de la Renta Ordinaria" (44/45 zone) — as PRINTED-BUT-DEAD: the form
  mirror renders the row at 0.00 for visual fidelity and NO
  computation path, user input or annex feed may ever populate it,
  because the pago mínimo regime is void (R21: struck by sentencias
  18-2012/98-2014, re-enactment D.L. 762-2014 void per sentencia
  96-2014; no successor in the 54_ reform tail through Jan-2026);
  any value landing in that casilla is a defect. (LB-005; EVID-183;
  R21)

### 3.7 Declaración modificatoria

- **SV-FREP-FR-164:** The system shall implement the F-14
  *declaración modificatoria* (amended return) flow as
  clean-and-replace: before presenting an amendment the previously
  loaded annex file must be REPLACED by the new one via the *limpiar*
  (clear) action, which deletes the data presented in the prior
  declaration ("clic en el botón limpiar, esto eliminará los datos
  presentados en la declaración anterior") — a FULL re-upload, never
  a merge; and the amendment shall surface the per-tab verification
  anchors recording the amounts paid in the prior declaration:
  casilla 50 (pago a cuenta), 221 (acreditables con dependencia),
  225 (acreditables sin dependencia), 332 (definitivas), 711
  (agentes extranjeros retención) and 761 (agentes extranjeros
  entero). (LB-004; EVID-181)

### 3.8 F-14 v17 Quincena-25 vintage (D12)

- **SV-FREP-FR-165:** The system shall gate the form layout by
  declaration period with the v17 vintage from 2026-06 (MH
  actualization "F14v17 ... Actualizado el 03/06/2026"): periods from
  2026-06 render the v17 layout, which inserts the section "INGRESOS
  NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO" after row 58 — row
  61 *Ingresos No Gravados Pagados por el Agente de Retención
  Quincena 25* with casilla 417 (número de sujetos) and casilla 418
  (monto) — and renumbers the v16 rows 61-104 to 62-105; ALL
  arithmetic casillas are stable across the vintage (330/332/334/336,
  501-529, 701-780), the casilla keys of FR-155..163 are therefore
  vintage-invariant, and periods before 2026-06 keep the v16 layout
  with no 417/418 row. (LB-007; EVID-184)
- **SV-FREP-FR-166:** The system shall project the Quincena-25
  no-gravado class into casillas 417/418 as a reporting-only
  aggregate — subject count and amount of the *Ley Especial Quincena
  Veinticinco* payments made by the retention agent — ISOLATED from
  the retention arithmetic: 417/418 never enter the 330-336
  definitivas totals, any impuesto casilla or the Pago a Cuenta
  computation (the Quincena-25 income is no-gravado; its payment
  mechanics belong to the payroll wave — SOQ-09 cross-topic);
  provisionally computed from an internal Quincena-25 ledger
  classification under the FR-167 working assumption.
  (LB-007; EVID-184)
- **SV-FREP-FR-167:** The system shall TARGET the v16 annex export
  structure (FR-137) for all periods — the v17 annex-level
  representation of Quincena-25 rows is BLOCKED because no v17
  manual or plantilla exists (MH checked 2026-08-18): whether the
  Quincena-25 rows enter the annex CSV as a NEW income code, new
  columns or otherwise is UNKNOWN; the working assumption (v16
  columns + a new income code, unconfirmed — SOQ-09/OQ-001) drives
  FR-166's provisional internal classification, and NO Quincena-25
  annex row is emitted until the v17 manual pins the format.
  (LB-007; EVID-184; SOQ-09)

### 3.9 Computation-source interfaces and export surface

- **SV-FREP-FR-168:** The system shall source every annex value from
  the taxation layer by FR id and never recompute: I (IMPUESTO
  RETENIDO) from the retention postings of
  `taxation/04_isr-withholding.md` SV-TAX-FR-102 (payroll retention
  posts) and SV-TAX-FR-121..131 (matrix retentions); the payroll
  bases from SV-TAX-FR-104 (retention base) and the mode/threshold
  selection behind codes 01/60 from SV-TAX-FR-106 ($9,100/$60,000
  thresholds); the aguinaldo split from SV-TAX-FR-120 — the F-14
  annex is the REPORTING projection of those computations (their
  interface contract), and any base mismatch is flagged to the
  source layer, not adjusted here. (LB-003; LB-008; EVID-180;
  cross-ref SV-TAX-FR-102/104/106/120/121..131)
- **SV-FREP-FR-169:** The system shall export the annex from the
  plantilla "Detalle" structure (the v16 column template of FR-137)
  under the printed numeric discipline (FR-151) and the validation
  contract (FR-140..151), with the file mechanics (delimiter,
  filename policy, Text-cell typing) consumed by parity with the F-07
  §II engine conventions of `01_f07-declaration.md`
  SV-FREP-FR-028..031 — the 35_ extract does not transcribe the F-14
  file-format section and the plantilla governs (OQ-006).
  (LB-001; EVID-180; cross-ref SV-FREP-FR-028..031)
- **SV-FREP-FR-170:** The system shall expose the validated F-14
  annex rows as the monthly feed of the F-910 annual retentions
  consolidation (the CT Art. 123 surface, including the annual
  01-vs-60 rule and the ANNUAL social-security columns) — the
  consolidation rules are OWNED by `07_codes-and-informes.md` and
  cited forward by file+§; this file guarantees only that the monthly
  rows carry the fields that consolidation consumes (subject, code,
  amounts, SS columns, period). (LB-001; EVID-180; EVID-182;
  forward-ref `07_codes-and-informs.md`)

## 4. Data Model

No CSV sidecars live next to this file: the seeds below are in-file §4
data; the country-code/haven table and the SS-cap parameters are dated
data refreshed from their owning sources (MH web / payroll wave).
Layer semantics: Odoo-side computation/bookkeeping data only (wave
default `odoo`; see §5).

**F-14 declaration — l10n_sv.f14.declaration (new):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| period (MMYYYY), form_version | char/computed | v16 (< 2026-06) · v17 (≥ 2026-06) — computed from period | FR-154, FR-165 |
| prior_declaration_id, clean_replaced_on | m2o/datetime | modificatoria linkage; limpiar timestamp (full re-upload, never merge) | FR-164 |
| anchor_c50, anchor_c221, anchor_c225, anchor_c332, anchor_c711, anchor_c761 | monetary(2dp) | prior-declaration amounts paid, per the printed per-tab verification anchors | FR-164 |

**Annex row model — l10n_sv.f14.annex.row (new; the A-W verbatim
projection):**

| Field (column) | Type | Catalog / values | Reference |
|----------------|------|------------------|-----------|
| domiciliado (A) | select | 1 Domiciliado · 2 No Domiciliado | FR-137, FR-138 |
| country_code_id (B) | m2o → l10n_sv.f14.country.code | required for A=2; 9300 default for A=1 | FR-138, FR-139 |
| subject_name (C), nit_nif (D), dui (E) | char(100)/char(14)/char(9) | D = local NIT or foreign NIF; DUI/NIT XOR (Enero-2022 gate) | FR-138, FR-140 |
| income_code (F) | char(2) | membership validated; semantics owned by `07_codes-and-informs.md` §3 | FR-142 |
| monto_devengado (G), bonificaciones_gratificaciones (H), impuesto_retenido (I), aguinaldo_exento (J), aguinaldo_gravado (K) | monetary(2dp) | payroll split for codes 01/60/80; I validated per legal rate; K ≤ G | FR-143, FR-144, FR-148, FR-149 |
| ss_afp (L), ss_isss (M), ss_inpep (N), ss_ipsfa (O), ss_cefafa (P), ss_bienestar_mag (Q), ss_isss_ivm (R) | monetary(2dp) | validated against l10n_sv.f14.ss.cap (amount and percentage caps) | FR-145, FR-150 |
| tipo_operacion (S), clasificacion (T), sector (U), tipo_costo_gasto (V) | char(1) | CANONICAL quartet codes via `l10n_sv.isr.costgasto.classification` (03 file model — single source of truth; "0" pre-Feb-2024; codes 8/9) | FR-146 |
| periodo_mmyyyy (W) | char(6) | MMYYYY, no slashes; = declaration period | FR-147 |

**Social-security cap parameters — l10n_sv.f14.ss.cap (new; dated
data, payroll-wave feed mirror — SOQ-11):**

| Institution | Cap type | Seed value (Oct-2025 print) | Reference |
|-------------|----------|----------------------------|-----------|
| afp | amount | 472.93 | FR-145, FR-150 |
| isss | amount | 30.00 | FR-145, FR-150 |
| inpep | percent | 7.5 | FR-145, FR-150 |
| ipsfa | percent | 9.5 | FR-145, FR-150 |
| cefafa | percent | 5.0 | FR-145, FR-150 |
| bienestar_magisterial | percent | 5.58 | FR-145, FR-150 |
| isss_ivm | percent | 7.5 | FR-145, FR-150 |

(fields: institution, cap_type amount/percent, value, valid_from,
source_note — ceilings re-dated by the payroll wave's feed; this table
only mirrors them for validation.)

**Country/haven table — l10n_sv.f14.country.code (new; dated data
from the MH web list):** code (4-digit) · name · is_haven (boolean) ·
notes (US-states band 99xx seeded: 9900-9903 DELAWARE/NEVADA/WYOMING
per the manual extract; 9300 EL SALVADOR). Reference FR-139, FR-141.

**Form-mirror spec — l10n_sv.f14.casilla.spec (new; vintage-gated
seed):** vintage (v16/v17) · tab · row · casilla · label · role
(annex_total / subject_count / input_non_annex / total_formula /
printed_dead / no_gravado_report) · source. Seeds: the seven-tab map
of LB-005 with the v17 delta rows (row 61 → casillas 417/418;
renumbering 62-105; all arithmetic casillas vintage-invariant). The
44/45-zone pago-mínimo row carries role printed_dead (FR-163); the
Pago a Cuenta inputs 42/46/48 carry role input_non_annex (FR-162).
Reference FR-154..166.

**Projection engine — l10n_sv.f14.casilla.value:** declaration_id,
casilla, value — written exclusively by the per-code aggregation of
FR-153 (plus the FR-162 non-annex inputs); retention/no-gravado
casillas have no manual write path. Reference FR-152, FR-153.

**Income-code routing:** consumed from the catalog model owned by
`07_codes-and-informs.md` §3/§4 (code → class → tab/casilla zone);
this file stores no code list of its own. Reference FR-142,
FR-155..161.

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transmission (the only architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`). Model
names are stable across Odoo 17/18/19/20; version-specific behavior
is recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-137 | odoo | l10n_sv.f14.annex.row | A-W column model | v16 annex mechanics current (no v17 manual — SOQ-09); plantilla "Detalle" the operative template; AC-001 |
| FR-138 | odoo | l10n_sv.f14.annex.row + res.partner | domiciliado/country/NIT-NIF | Foreign NIF for non-domiciliados; partner master feeds the subject fields |
| FR-139 | odoo | l10n_sv.f14.country.code | dated data + is_haven | MH web list; refresh cadence OQ-007; US-states 99xx band seeded |
| FR-140 | odoo | l10n_sv.f14.annex.row | DUI/NIT XOR | Enero-2022 gate (natural persons domiciled); export-blocking |
| FR-141 | odoo | l10n_sv.f14.annex.row + l10n_sv.f14.country.code | haven 25% exactness | Exactly 25% of base — neither below nor above; haven RULE owned by taxation/04 FR-127 (CT 158-A); AC-003 |
| FR-142 | odoo | l10n_sv.f14.annex.row | income_code | Membership + class routing; catalog semantics OWNED by `07_codes-and-informs.md` §3 (forward ref — never restated) |
| FR-143 | odoo | hr.payslip → annex row builder | G/H split | Codes 01/60/80: devengado includes AFP+cotizaciones, EXCLUDES aguinaldo/bonificaciones (37_ plantilla note); totality rule nota 2; AC-001 |
| FR-144 | odoo | hr.payslip (aguinaldo lines) | J/K pair | 2-SMM split consumed from taxation/04 FR-120; SMM feed = payroll wave; AC-001 |
| FR-145 | odoo | l10n_sv.f14.ss.cap | validation parameters | DATED data (Oct-2025 print); $-caps AFP 472.93 / ISSS 30.00; %-maxima 7.5/9.5/5/5.58/7.5; payroll-wave feed per SOQ-11/OQ-002 |
| FR-146 | odoo | l10n_sv.isr.costgasto.classification (03 file model) | S-V quartet | CANONICAL FR-079..085 consumed by id (Febrero-2024 gate; codes 8/9); nothing restated; AC-014 |
| FR-147 | odoo | l10n_sv.f14.annex.row | periodo MMYYYY | Row period = declaration period (no prior-period windows printed for F-14) |
| FR-148 | odoo | l10n_sv.f14.annex.row (constraint) + taxation rate matrix | %-per-code parity | Rate per code FROM SV-TAX-FR-109/121..131 (CT matrix + D.E. 10-2025 tables); MH rejection parity — export blocked; AC-002 |
| FR-149 | odoo | l10n_sv.f14.annex.row (constraint) | K ≤ G | Message parity "Monto Aguinaldo gravado no puede ser mayor al monto devengado"; AC-005 |
| FR-150 | odoo | l10n_sv.f14.annex.row + l10n_sv.f14.ss.cap | cap rejection | Per-column error before export; AC-004 |
| FR-151 | odoo | l10n_sv.f14.annex.row | 2-decimal truncation | "el Sistema tomará únicamente 2"; nils 0.00; XOR export gate; AC-010 |
| FR-152 | odoo | l10n_sv.f14.declaration + casilla.value | pure projection | THE invariant — no manual write path on retention/no-gravado casillas; non-annex inputs ONLY 42/46/48 (FR-162); AC-006 |
| FR-153 | odoo | l10n_sv.f14.casilla.value | per-code aggregation | sujetos count + gravado + impuesto per code; sole writer of retention casillas |
| FR-154 | odoo | l10n_sv.f14.casilla.spec + l10n_sv.f14.declaration | vintage-gated mirror | D12: v16 (< 2026-06) / v17 (≥ 2026-06, MH actualization 03-06-2026); AC-008 |
| FR-155 | odoo | l10n_sv.f14.casilla.spec/value | Acreditables tab | 104/105 pairs + impuesto zone 150-164; totals 221/225; row/casilla assignment per 07 §3 (forward ref) |
| FR-156 | odoo | l10n_sv.f14.casilla.value | row 58 + rows 59-60 | Code-60 aggregate; aguinaldo-exento 416 zone; 70-72 no-gravados; reporting-only |
| FR-157 | odoo | l10n_sv.f14.casilla.spec/value | Definitivas 230-336 | Distributions block 296-328 (codes 43-46; earnings-register feed = taxation/05, forward); totals 330-336 |
| FR-158 | odoo | l10n_sv.f14.casilla.spec/value | No Domiciliados 250-314 | 20%/5%/10% tracks keyed to SV-TAX-FR-126 (rates by reference); AC-013 |
| FR-159 | odoo | l10n_sv.f14.annex.row (instrument class) + casilla.value | Op. Financieras 501-529 | 4 instrument tracks: liquidity-control creditable 501-504 vs definitive cheque 505-507 / transferencias 525-529 / mercado de valores 519-521; CT 159-zone anchor re-check OQ-003; AC-012 |
| FR-160 | odoo | l10n_sv.f14.casilla.spec | Contribución Especial | Form-mirror surface; track assignment per 07 §3 (forward ref) |
| FR-161 | odoo | l10n_sv.f14.casilla.spec/value | Agentes Extranjeros 701-780 | Retención 701-703/710-720 + entero donantes locales 751-753/760-780; F-935 detail = 07 file (forward); SOQ-13 kin |
| FR-162 | odoo | l10n_sv.f14.declaration + casilla.value | Pago a Cuenta 42-56 | ONLY non-annex inputs: 42 prior-modified-declaration amount, 46 Art. 74-A CT adjustment (anchor printed; regime substance cross-file), 48 IVA-exporter reintegro; 50-56 totals |
| FR-163 | odoo | l10n_sv.f14.casilla.spec (role printed_dead) | pago-mínimo remnant | R21: void regime — row rendered 0.00, NO computation path ever feeds it; AC-011 |
| FR-164 | odoo | l10n_sv.f14.declaration | modificatoria flow | limpiar = full data replacement + full re-upload; anchors 50/221/225/332/711/761 = prior-declaration amounts; AC-009 |
| FR-165 | odoo | l10n_sv.f14.casilla.spec (vintage v17) | Quincena-25 form rows | D12: from 2026-06; 417 sujetos / 418 monto; rows 62-105 renumbered; arithmetic casillas stable; AC-008 |
| FR-166 | odoo | l10n_sv.f14.casilla.value | 417/418 isolation | Reporting-only; NEVER enters 330-336/impuesto/pago-a-cuenta arithmetic; provisional internal classification per FR-167; AC-007 |
| FR-167 | odoo | l10n_sv.f14.annex.row (export gate) | annex-level BLOCKED | No v17 manual/plantilla (MH 2026-08-18); v16 structure exported for all periods; working assumption v16+new-code (SOQ-09/OQ-001); no Quincena-25 annex row emitted |
| FR-168 | odoo | hr.payslip / account.move.line → annex row builder | computation-source interface | I from SV-TAX-FR-102/121..131; bases from SV-TAX-FR-104; thresholds SV-TAX-FR-106 (01-vs-60 monthly); annex REPORTS, never recomputes |
| FR-169 | odoo | l10n_sv.f14 annex export | file surface | Plantilla "Detalle" structure; F-07 §II mechanics by parity (01 FR-028..031) — F-14-specific format untranscribed, OQ-006 |
| FR-170 | odoo | l10n_sv.f14.annex.row (read API) | F-910 feed | Consolidation rules OWNED by `07_codes-and-informs.md` (CT 123 surface; annual 01-vs-60; annual SS columns) — forward ref |

Version-regime notes (D12): three dated layers govern this file —
(1) the FORM vintage (v16 before 2026-06, v17 from 2026-06 per the MH
03-06-2026 actualization; the annex mechanics stay v16 until a v17
manual publishes — SOQ-09); (2) the SS-cap parameters (Oct-2025
print; payroll-wave feed — SOQ-11); (3) the country/haven list (MH
web, undated in the corpus — OQ-007). The income-code catalog vintage
(Oct-2025 apéndice vs the v17 row set) is owned by
`07_codes-and-informs.md` §3 (OQ-004 pointer). Filing due days stay
unpinned (`08_filing-calendar.md`; SOQ-08 — OQ-005 pointer).

## 6. Acceptance Criteria

- **AC-001:** Given a code-01 employee row with gross salary 1,000.00
  (already including AFP 63.00 and ISSS 21.00 employee
  contributions), a bonus 150.00 and an aguinaldo of 1,000.00 split
  800.00 exempt / 200.00 taxable, then the annex row reads G =
  **1,000.00** (AFP and cotizaciones INCLUDED, aguinaldo and
  bonificaciones EXCLUDED), H = **150.00**, J = **800.00**, K =
  **200.00** — never G = 2,150.00 or the bonus inside G (FR-143,
  FR-144).
- **AC-002:** Given a code-11 honorarios row with devengado 2,000.00
  and impuesto retenido 300.00 (15%), then the export is BLOCKED with
  the rate-parity inconsistency ("Monto Retenido no puede ser
  diferente al 10% sobre el monto devengado" family); given 200.00,
  then the row passes (FR-148).
- **AC-003:** Given a non-domiciled row whose country code carries
  the haven flag with base 4,000.00 and retention 800.00 (20%), then
  the export is blocked with the warning that the retention must be
  neither below nor above 25%; given 1,000.00 (exactly 25%), then the
  row passes (FR-141).
- **AC-004:** Given an annex row with ss_afp = 500.00 or ss_isss =
  30.01, then the row is rejected with the per-column cap error; given
  ss_afp = 472.93 and ss_isss = 30.00, then the row passes; given
  ss_inpep = 8% of devengado, then the row is rejected (7.5% maximum)
  (FR-145, FR-150).
- **AC-005:** Given a row with K (aguinaldo gravado) = 500.00 and G
  (devengado) = 400.00, then the export is blocked with the message
  "Monto Aguinaldo gravado no puede ser mayor al monto devengado"
  (FR-149).
- **AC-006:** Given a loaded and validated annex, then every
  retention and no-gravado casilla of all seven tabs is populated by
  the per-code aggregation; and given an attempt to hand-edit any of
  those casillas, then the write is rejected — the only editable
  input casillas are 42/46/48 in the Pago a Cuenta block (FR-152,
  FR-153, FR-162).
- **AC-007:** Given a v17-period declaration (07/2026) whose payroll
  recorded Quincena-25 payments of 5,000.00 to 10 subjects, then
  casilla 417 = **10** and casilla 418 = **5,000.00**, and the
  definitivas totals 330-336 and every impuesto casilla are IDENTICAL
  with and without the Quincena-25 amounts (reporting-only isolation)
  (FR-166).
- **AC-008:** Given a declaration for period 05/2026, then the form
  renders the v16 layout (no 417/418 row; rows 61-104); given period
  06/2026, then the form renders the v17 layout (row 61 Quincena-25
  with casillas 417/418; rows 62-105) while casillas 330/332/334/336,
  501-529 and 701-780 keep their keys (FR-165).
- **AC-009:** Given a modificatoria presentation, then the limpiar
  action deletes the prior declaration's annex data, the new file
  fully replaces it (no merge), and the anchors record the prior
  declaration's amounts at casillas 50/221/225/332/711/761
  (FR-164).
- **AC-010:** Given a domiciled natural-person row (period ≥
  Enero-2022) carrying BOTH dui and nit, then the export is blocked;
  given either one alone, then it passes; and given a devengado
  computed as 100.005, then the exported cell reads 100.00 (FR-140,
  FR-151).
- **AC-011:** Given the printed pago-mínimo remnant row (44/45 zone),
  then the form mirror renders it at **0.00** and no amended-
  declaration excedente, computation or user action can change it —
  any nonzero value in that casilla is a defect (FR-163).
- **AC-012:** Given a financial-operations retention over a CHECK
  instrument, then it projects into the 505-507 definitive track; over
  a liquidity-control operation, then into the 501-504 creditable
  track; over an electronic transfer, then into 525-529; over a
  securities-market operation, then into 519-521 (FR-159).
- **AC-013:** Given a non-domiciled row retained at 20%, then it
  projects into the 250-314 zone's 20% track casilla of its income
  code; given a reduced-rate transport row at 5%, then into its 5%
  track (rates keyed to SV-TAX-FR-126 by reference) (FR-158).
- **AC-014:** Given an annex row dated Enero-2024, then S/T/U/V
  export as "0"; given the same classification dated Mar-2024, then
  the canonical quartet codes from `l10n_sv.isr.costgasto.classification`
  (03 file FR-079..085) fill S/T/U/V with no code list duplicated in
  this file (FR-146).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-09: F-14 v17 annex format unknown — no v17 manual/plantilla exists (MH checked 2026-08-18): how do Quincena-25 rows enter the annex CSV (a NEW income code? new columns?)? Working assumption recorded in FR-167: v16 columns + a new income code, UNCONFIRMED; FR-166's provisional 417/418 classification and any Quincena-25 annex emission stay blocked until the v17 manual publishes. The Ley Especial Quincena Veinticinco itself is not in the corpus (acquisition candidate, numbering ≥ 65; payroll co-dependency for payment mechanics). | yes (Quincena-25 annex-level representation only) | Takumi S3 (sources registry) + payroll wave | open |
| OQ-002 | SOQ-11: SS caps as dated data — AFP US$472.93 / ISSS US$30.00 ($-caps) and INPEP 7.5% / IPSFA 9.5% / CEFAFA 5% / Bienestar Magisterial 5.58% / ISSS-IVM 7.5% (%-maxima) printed Oct-2025: the cap feed/cadence and the legal ceiling bases belong to the PAYROLL wave (16_/08_/09_ sources); this file mirrors them as validation parameters (l10n_sv.f14.ss.cap). Payroll wave re-dates the values at encoding. | no | Takumi payroll wave | open |
| OQ-003 | Op. Financieras tracks (casillas 501-529; 35_-file OQ-4 kin): the instrument taxonomy (control-de-liquidez creditable vs definitive cheque/transferencias electrónicas/mercado de valores) and the acreditable-vs-definitivo RATES need a CT 159/164-165-zone article re-check — the LB anchor is incomplete in the W8 read (form labels only). FR-159 encodes the printed track split; the CT anchor and rates stay open. | no | Takumi S3 (CT matrix re-check) | open |
| OQ-004 | Income-code catalog fidelity (pointer): the apéndice catalog transcribed in EVID-182 is the v16 manual (Oct-2025) — verify against the v17 form's row set and any annex-modification resolutions (SOQ-12 kin; 29_-file OQ-1 kin). OWNED by `07_codes-and-informs.md` §3; this file consumes the catalog by forward reference only. | no | Takumi S3 (Task 7) | open |
| OQ-005 | SOQ-08 (pointer): F-14 due-day scheduling — the 2026 calendar's due-day windows are a visual layer with no normative anchor in the corpus; deadline behavior is owned by `08_filing-calendar.md`. No deadline FR exists in this file. | no | Takumi S3 (Task 8) | open |
| OQ-006 | F-14 export file mechanics: the 35_ W8 extract does not transcribe the F-14 file-format section (delimiter, ≤-character filename policy, Text-cell discipline); plantilla sheet "Detalle" carries the column template and FR-169 consumes the F-07 §II conventions (01 file SV-FREP-FR-028..031) by PARITY. Verify against the plantilla/MH upload validation before certifying byte-exact exports. | no | Takumi S3 | open |
| OQ-007 | MH country-code + tax-haven list cadence: both tables are web-published and undated in the corpus ("La lista vigente de países ... se encuentra publicada en la página web del Ministerio de Hacienda"); FR-139 seeds them as dated data with the haven flag. Pin a refresh source/schedule; the haven CLASSIFICATION consumed by taxation/04 FR-127 must stay consistent with this table. | no | Takumi S3 (sources registry) | open |
