# SV — Fiscal reporting — F-14 income codes & related informs: catalog, F-910, F-915, F-935

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for El Salvador's F-14
income-code catalog and the related annual/monthly informs that consume
it: the complete *apéndice* (appendix) income-code catalog of the F-14
V16 user manual (OCTUBRE 2025) — all 48 codes across the four classes
*retenciones acreditables en liquidación anual del impuesto* (retentions
creditable in the annual liquidation), *retenciones no acreditables
(entero definitivo)* (non-creditable retentions, definitive remittance),
*ingresos gravados sin retención* (taxed income without retention) and
*ingresos no gravados* (non-taxed income) — as DATED DATA with the code
→ description → class → F-14 row/casilla mapping → CT anchor columns,
including the distributions codes 43/44/45/46 (the withholding leg of
the Ley ISR Arts. 72-74-A regime), the tax-haven code 40 and the CT
Art. 123 aggregate code 47 (NIT of 14 zeros + *VARIOS*); the
cross-tax classification coupling — the F-07 Anexo 1 R/S Renta pair's
code 12 ("*Ingresos que ya fueron sujetos de retención informados en el
F14 y consolidados en F910*") and the F-14 codes feeding the F-11 rentas
matrix; the **F-910 v9** *Informe Anual de Retención del ISR* (annual
ISR retentions inform — the CT Art. 123 surface): the annual
per-contribuyente consolidation over the 12 monthly F-14 annex rows with
the 01-vs-60 annual rule and the ANNUAL social-security columns; the
**F-915 v4** *Informe de Distribución o Capitalización de Utilidades*
(distribution or capitalization of utilities inform): the
DISTRIBUYÓ/CAPITALIZÓ modes with *acta* (minutes) linkage, the
socio-quality transition split and per-socio rows built over the
earnings register; and the **F-935 v1** *Informe Mensual de Retención
sobre Agentes Extranjeros* (monthly foreign-agents retention inform):
the RETENCIÓN-vs-ENTERO blocks with transfer-level rows and the
*donantes locales* (local donors) track. The F-930 v3 inform is
referenced only (already homed in `04_f07-annexes-retentions-events.md`).

It does **not** cover: the F-14 declaration engine, annex column model,
export validation contract, form-mirror vintages and modificatoria flow
(`06_f14-declaration.md` — its FR-142 consumes THIS file's §3 catalog by
the forward reference, and its FR-170 feeds this file's F-910 builder);
the retention COMPUTATION behind each code — bases, tables, rates and
the CT 154-160 matrix (`taxation/04_isr-withholding.md`
SV-TAX-FR-102..131 — this file's catalog carries NO rate column by
design); the distributions regime substance and the earnings-register
data model (`taxation/05_isr-distributions.md` SV-TAX-FR-132..149 — this
file only builds reporting surfaces over them); the F-07 sales-annex
R/S code lists themselves (`02_f07-annexes-sales.md` SV-FREP-FR-051/052
— cited by id); the F-930 IVA-retentions inform
(`04_f07-annexes-retentions-events.md`); and the filing due-day calendar
(`08_filing-calendar.md` — SOQ-08; no deadline behavior is encoded
here).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and manuals ARE the primary
authority for declaration and inform mechanics — 35_ (F-14 V16 manual,
OCTUBRE 2025) owns the apéndice income-code catalog; 61_ (F-910 v9),
62_ (F-915 v4), 63_ (F-930 v3) and 64_ (F-935 v1) own the inform
layouts; 38_ anchors the v16 form row/casilla map behind the catalog's
mapping column. Legal anchors behind the printed codes are cited per
the S2 order through the taxation files (rates NEVER restated here).
Manual/form pages are printed pages.

**75_ fold-in vintage watch (rides the 75_ row below):** the D.E.
117-2001 print (Reglamento de Aplicación del Código Tributario) carries NO
REFORMAS block and post-2001 repeal by CT Art. 344 ff is print-unresolvable
(EV75 OQ-1/OQ-8, SOQ-06-kin) — cited as printed. **OQ-3 bar:** the
dictamen block (Arts. 58-72) is HISTORICAL/awareness only — the
mandatory-dictamen regime was restructured post-2001 and corpus 05_
carries no dictamen entry (CT 130-137 zone unextracted; EV75 OQ-3) —
never operative FRs (§3.7, OQ-009).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-14 v16, APÉNDICE, catálogo de códigos de ingreso (verbat, completo): "RETENCIONES ACREDITABLES EN LIQUIDACIÓN ANUAL DEL IMPUESTO: 01- Servicios de carácter permanente · 05- Rentas de personas jurídicas domiciliadas provenientes de depósitos de dinero · 06- ... títulos valores · 07- Retenciones por actividades agropecuarias · 08- Retenciones por juicios ejecutivos · 09- Otras retenciones · 11- Servicios sin dependencia laboral · 19- Costos y gastos incurridos sujetos a retención y entero · 20- Valores garantizados por seguro dotal u otros tipos de seguros · 21- Otros servicios sin dependencia laboral · 22- Transferencia de bienes intangibles por personas naturales domiciliadas · 23- ... jurídicas domiciliadas · 24- Por uso o concesión de uso, de derechos de bienes tangibles e intangibles a personas naturales domiciliadas · 25- ... a personas jurídicas domiciliadas · 26- Operaciones de renta y asimiladas a rentas a personas domiciliadas · 27- Retenciones por servicios de arrendamiento a personas naturales · 48- Indemnizaciones por daños · 80- Servicios de Carácter Permanente con Subordinación o Dependencia Laboral Sin Contribuciones Sociales (Eje.: jubilados y pensionados) · 81- Servicios de Carácter Permanente sin retención prestado por Jubilados y Pensionados · 82- Pago de sueldos caídos con retención · 83- Pago de sueldos caídos sin retención · 84- Pago de dietas · 85- Indemnizaciones laborales. RETENCIONES NO ACREDITABLES (ENTERO DEFINITIVO): 28- Rentas de Personas Naturales Domiciliadas provenientes de títulos valores · 29- Premios o ganancia de domiciliadas ... juegos de azar o de habilidad · 30- Rentas obtenidas en el país de no domiciliadas por rendimiento de capital invertido, títulos valores, otros · 31- Por uso o concesión de uso ... a no domiciliados · 32- Transferencia de bienes intangibles por no domiciliadas · 33- Rentas obtenidas en el país por personas no domiciliadas · 34- Servicios utilizados en el país por actividades originadas en el exterior · 35- Pagos efectuados a casa matriz (no domiciliadas) por filiales y/o sucursales domiciliadas · 36- Servicio de transporte internacional a personas no domiciliadas · 37- Servicios por aseguradoras, reaseguradoras, afianzadoras, reafianzadoras y corredores de reaseguros no domiciliados · 38- Servicios de financiamiento por instituciones financieras no domiciliadas · 39- Operaciones con intangibles o uso concesión de uso ... a no domiciliados · 40- Rentas de personas constituidas, domiciliadas o residentes en países con regimenes fiscales preferentes o paraísos fiscales · 41- Premios o ganancias de no domiciliadas ... · 42- Otras retenciones · 43- Pago o Acreditación de utilidades a socios, accionistas, asociados, fideicomisarios, participes, inversionistas o beneficiarios · 44- Pago o Acreditación de utilidades a sujetos no domiciliados en El Salvador · 45- Pago o acreditación en disminución de capital o patrimonio (parte correspondiente a capitalizaciones o reinversión de utilidades) · 46- Prestamos, mutuos, anticipos o financiamientos (en dinero o bienes en especie) · 47- Rentas a Personas Naturales domiciliadas en concepto de intereses, premios y otras utilidades provenientes de Depósitos en Dinero · 49- Sobre Ingresos por remuneraciones con o sin dependencia laboral prestados a Inversionistas. 'Para la retención con el código 47, en atención al artículo 123 del Código Tributario, Inciso Tercero, la columna del NIT podrá completarla con 14 ceros ... y el campo del nombre podrá completarlo con la palabra VARIOS.' INGRESOS GRAVADOS SIN RETENCIÓN: 60- Servicios de carácter permanente con subordinación o dependencia laboral (Tramo I de las Tablas de Retención). INGRESOS NO GRAVADOS: 70- Indemnizaciones por despido, retiro voluntario, muerte, incapacidad, accidente o enfermedad (según ley) · 71- Valores garantizados por seguro dotal u otros tipos de seguros (según ley) · 72- Remuneraciones, compensaciones y gastos de representación por servicios en el exterior de funcionarios o empleados de gob. (según ley)" | F-14 v16 manual appendix, income-code catalog complete: 23 creditable codes (01, 05-09, 11, 19-27, 48, 80-85), 21 definitive codes (28-46, 49) including the distributions codes 43/44/45, the loans code 46, the tax-haven code 40 and the deposit-yield aggregate code 47 — whose printed note allows the NIT column to be filled with 14 zeros and the name field with the word VARIOS per CT Art. 123 third inciso — one sin-retención code (60, Tramo I of the retention tables) and three no-gravado codes (70-72, "según ley" (per law) as printed) | `sv/sources/35_F14_v16_manual.pdf` | APÉNDICE pp.17-18 (EVID-182) |
| LB-002 | Formulario F-14 v16 (38_), zonas de filas/casillas por clase de código: Acreditables con dependencia laboral filas 10-27 → pares 104/105 (nº sujetos/monto gravado) + zona impuesto 150/151/152/154/156/158/160/162/164, totales 221/225; sin dependencia (honorarios, arrendamientos, agropecuaria, juicios, premios, intangibles, rendimientos); fila 58 "Ingresos gravados sin retención" (zona 104/105) + filas 59-60 "INGRESOS NO GRAVADOS" (zona casilla 416 aguinaldo exento); Definitivas filas 28-46 → casillas 230-336 incl. bloque 296-328 (distribuciones 43-46, préstamos 46/81-82, otras 42/83, remuneraciones inversionistas 49/84) y totales 330-336; No Domiciliados filas 62-79 → 250-314 (pistas 20%/5%/10%) | F-14 v16 form, row/casilla zones by code class: creditable con-dependencia rows 10-27 (104/105 pairs + impuesto zone 150-164; totals 221/225); code-60 aggregate row 58; no-gravado rows 59-60; definitive rows 28-46 → 230-336 incl. the 296-328 block (distributions 43-46, loans 46/81-82, other 42/83, investor remunerations 49/84) with totals 330-336; non-domiciled rows 62-79 → 250-314 (20%/5%/10% tracks) — the mapping data behind this file's catalog column | `sv/sources/38_F14_v16_form_visual.pdf` | pp.1-3 (EVID-183) |
| LB-003 | Formulario F-910 v9 (61_), §A-§C: §C encabezado "Datos del Contribuyente a quienes se les pagaron ingresos sujetos a retención, sin retención o no gravados"; estructura de filas "CÓDIGO INGRESO / MONTO DEVENGADO / MONTO DEVENGADO ANUAL POR BONIFICACIONES Y GRATIFICACIONES / IMPUESTO RETENIDO / Aguinaldo (Aplica solo para código 01 y 60) Exento Gravado / ISSS ANUAL / AFP ANUAL / IPSFA ANUAL / CEFAFA ANUAL / INPEP ANUAL / BIENESTAR MAGISTERIAL ANUAL" con SUMAS TOTALES; regla de nómina: "Los ingresos en concepto de Servicios de carácter permanente con subordinación o dependencia laboral, deben ser reportados en su totalidad en los códigos 01 ó 60 ... 1. En el código 01, si se le retuvo en al menos un mes del ejercicio fiscal. 2. En el código 60, si no se le retuvo en todo el ejercicio fiscal"; §C imprime el mismo catálogo de códigos que el apéndice del F-14 | F-910 v9 form: §C header "data of the contributors to whom income subject to retention, without retention or non-taxed was paid"; per-contribuyente row structure = income code + accrued amount + annual bonuses/gratuities + retained tax + aguinaldo exento/gravado pair (codes 01 and 60 only) + SIX annual social-security columns (ISSS, AFP, IPSFA, CEFAFA, INPEP, BIENESTAR MAGISTERIAL — no ISSS-IVM column) with grand totals; payroll rule: permanent-service income is reported in its entirety in codes 01 or 60 — code 01 if retained in AT LEAST ONE month of the fiscal ejercicio, code 60 if NEVER retained in the whole ejercicio; §C prints the same income-code catalog as the F-14 apéndice | `sv/sources/61_F910v9_informe_anual_retenciones.pdf` | §A-§C (EVID-187) |
| LB-004 | Formulario F-915 v4 (62_, fechado 2017-11-22), §A-§C: §A "01 EJERCICIO FISCAL / 02 FOLIO MODIFICA / 03 NIT / 11 DISTRIBUYÓ [casilla] ACTA JUNTA GENERAL DE ACCIONISTAS 04 Fecha 05 Número / CAPITALIZÓ [casilla]"; §B "Calidad de Socios × Cantidad / Monto de Utilidades, Dividendos o Excedentes Distribuidos / Valor Contable de las Acciones, Aportes, Participaciones Sociales o Derechos Capitalizados": filas "Socio, Accionista o Cooperado que adquirió la calidad con anterioridad al ejercicio que informa / ... durante el ejercicio que informa / ... que ha perdido la calidad durante el ejercicio que informa" + TOTAL; §C "N° / No Domiciliado / NIT / ..." filas por socio; juramento cita CT 241 + CP 249-A | F-915 v4 form: §A fiscal ejercicio, folio-modifica, NIT, the DISTRIBUYÓ (distributed) / CAPITALIZÓ (capitalized) checkboxes with the general-shareholders-meeting acta date and number; §B socio-quality transitions — partners who acquired the quality BEFORE the reported ejercicio / DURING it / who LOST it during it — each × count / amount of distributed utilities, dividends or excesses / book value of capitalized shares, contributions, participations or rights, plus TOTAL; §C per-socio rows with the No Domiciliado flag and NIT; the juramento cites CT Art. 241 and CP 249-A | `sv/sources/62_F915v4_informe_distribucion_utilidades.pdf` | §A-§C (EVID-188) |
| LB-005 | Formulario F-935 v1 (64_, creado 2025 según fecha de página), §A-§C: §A "PERIODO TRIBUTARIO / FOLIO MODIFICA / NIT/DUI"; §B "CONCEPTO × TOTAL DE REGISTROS / MONTO SUJETO / MONTO DE RETENCION": filas "RETENCION DE IMPUESTO / ENTERO DE IMPUESTO / TOTAL"; §C "Datos de impuesto retencion / donantes locales": filas "N / NIT/NIF / Apellidos y nombres Razon social o denominación / DATOS DE TRANSFERENCIA: CONCEPTO / FECHA / NÚMERO DE TRANSACCIÓN / PAIS DE ORIGEN / MONTO SUJETO / MONTO RETENCION/ENTERO" | F-935 v1 form: §A tax period, folio-modifica, NIT/DUI; §B concept × total records / subject amount / retention amount with the RETENCION DE IMPUESTO (tax retention) / ENTERO DE IMPUESTO (tax remittance) / TOTAL rows; §C retention-tax / local-donors data: per-transfer rows with NIT/NIF, name, and TRANSFER DATA — concept, date, TRANSACTION NUMBER, COUNTRY OF ORIGIN, subject amount, retention-or-remittance amount | `sv/sources/64_F935v1_informe_mensual_agentes_extranjeros.pdf` | §A-§C (EVID-190) |
| LB-006 | Código Tributario, Arts. 123, 124: Art. 123 — informe anual de retenciones del ISR (para enero: nombre, NIT, base y monto retenido por cada sujeto retenido; su inciso tercero es el ancla impresa en la nota del código 47 del apéndice F-14); Art. 124 — informe de la lista de accionistas y de dividendos distribuidos (para enero) — las superficies legales detrás del F-910 (y kin del F-915); layouts propiedad de esta onda, sustancia de retención propiedad de los archivos de taxation | Tax Code Arts. 123-124 — the annual ISR-retention information return (by January: name, NIT, base and tax per retained subject; Art. 123's third inciso is the anchor printed in the F-14 apéndice's code-47 note) and the dividends/shareholder-list information return (by January) — the legal surfaces behind F-910 (and the F-915 kin); layouts owned by this wave, retention substance owned by the taxation files | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 123-124 (EVID-064; code-47 note printed in LB-001) |
| LB-007 | Ley ISR (texto consolidado 54_), Arts. 72, 73, 74, 74-A, 74-C — el régimen de distribuciones detrás de los códigos 43/44/45/46 y del F-915; citado POR REFERENCIA a través de `taxation/05_isr-distributions.md` LB-001..006 (la retención del 5%, las utilidades de Amplia definición, las reducciones de capital con tracing profits-first, los préstamos como distribuciones presuntas, el Registro de Control de Utilidades) — este archivo nunca reexpone el régimen | ISR Law Arts. 72-74-C (per the S2 authority order, cited through the taxation file): the distributions regime behind codes 43/44/45/46 and the F-915 inform — referenced by pointer; the regime substance, pools and earnings-register model are owned by `taxation/05_isr-distributions.md` | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 72-74-C (via taxation/05 LB-001..006; EVID-103) |
| LB-008 | Manual F-07 v14 §III, par R/S del Anexo 1 (verbat, vía `02_f07-annexes-sales.md` LB-003): códigos R TIPO DE OPERACIÓN "1 Gravada / 2 No Gravada o Exento / 3 Excluido o no Constituye Renta / 4 Mixta / 12 Ingresos que ya fueron sujetos de retención informados en el F14 y consolidados en F910 / 13 Sujetos pasivos excluidos (art. 6 LISR)"; códigos S TIPO DE INGRESO 1-10 (12/13 como R) — el ancla del acoplamiento cross-tax | F-07 v14 manual §III Renta pair (via the 02 file's LB): R operation-type codes with code 12 = income already subject to retention, reported in the F-14 and consolidated in the F-910; S income-type codes — the cross-tax coupling anchor | `sv/sources/34_F07_v14_manual.pdf` | §III pp.1-6 (EVID-174; via 02-file LB-003) |
| LB-009 | Formulario F-930 v3 (63_) — SOLO REFERENCIA: el informe mensual de retención/percepción/anticipo IVA ya está alojado en `04_f07-annexes-retentions-events.md` (vista sobre el mismo ledger de retención IVA); se cita aquí únicamente para el inventario de informes y las notas de vintage | F-930 v3 form — reference only: the monthly IVA retentions inform already homed in the 04 file (a view over the same IVA-retention ledger); cited here only for the inform inventory and vintage notes | `sv/sources/63_F930v3_informe_mensual_retIVA.pdf` | §A-§C (EVID-189) |
| LB-010 | Código 73 F-910, Quincena-25 (verbat): 67_ §3.f: "En el Informe Anual de Retenciones (F-910), el monto pagado en concepto de Quincena Veinticinco, se verá reflejado en la columna de NO GRAVADOS, el cual se identificará de conformidad al Código 73 Ingresos No Gravados Pagados Quincena Veinticinco, generado de forma automática… de acuerdo a los datos cargados en anexo… (F-14)"; 68_ p.16: "el código de ingreso 73 se asignará de manera automática al momento de presentar la declaración" | F-910 code 73 (Quincena-25): per 67_ §3.f — in the Annual Retentions Inform (F-910) the amount paid in concept of Quincena Veinticinco is reflected in the NO GRAVADOS column, identified per code 73 "Ingresos No Gravados Pagados Quincena Veinticinco", generated automatically… from the data loaded in the annex… (F-14); per 68_ p.16 — income code 73 is assigned automatically at the moment of presenting the declaration | `sv/sources/67_Guia_Orientacion_Quincena25.pdf` + `sv/sources/68_Instrucciones_Carga_Quincena25.pdf` | §3.f p.4 / p.16 (EVID-238/239) |
| LB-011 | Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001), Arts. 58-72 (dictamen e informe fiscal — HISTORICAL per EV75 OQ-3) | Art. 58: la auditoría "será realizada por Licenciados en Contaduría Pública o Contadores Públicos Certificados"; Art. 61: nombramiento "a más tardar dentro de los primeros cinco meses del período anual a dictaminar", con aviso a la Administración Tributaria "dentro del plazo de treinta días calendario siguientes de efectuado el nombramiento"; Art. 70 (CT 134): el auditor "deberá presentar a la Administración Tributaria el dictamen conjuntamente con el informe fiscal, a más tardar el treinta y uno de mayo del año siguiente al período que se dictamina"; sociedades en liquidación o fusión: "dentro de los seis meses siguientes, contados a partir de la fecha de la inscripción del acuerdo o sentencia"; Art. 65: el dictamen separa "los incumplimientos formales de los sustantivos, subsanados y no subsanados, debiendo cuantificarse monetariamente el impacto impositivo de los incumplimientos sustantivos"; Art. 66: "Los estados financieros a presentar serán los que establecen las Normas Internacionales de Contabilidad"; Art. 67: anexos a)-n) incl. la cadena de determinación del IVA (b.3 — prorrata) y las cadenas de reintegro del exportador (l) | 75_ Reglamento CT Arts. 58-72 — the 2001 mandatory fiscal-audit (dictamen e informe fiscal) blueprint: CPC auditor appointment clocks (5-month nombramiento + 30-day aviso), the 31-may dictamen+informe filing deadline (CT 134 anchor), the 6-month liquidación/fusión clock, the formal-vs-substantive incumplimiento separation with monetary quantification, NIC financial statements, and the a)-n) anexo set restating the IVA prorrata (b.3) and exporter-reintegro (l) chains — HISTORICAL blueprint only (regime status doubtful post-2001; never operative FRs — §3.7, OQ-009) | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 58-72 pp.34-47 (EVID-349; verified 75_ txt lines 1744-1746, 1830-1848, 1963-1985, 2008-2040, 2372-2385) |

## 3. Functional Requirements

### 3.1 The F-14 income-code catalog (the home of the catalog — consumed by 06 FR-142)

- **SV-FREP-FR-171:** The system shall maintain the F-14 income-code
  catalog as DATED DATA — the COMPLETE transcription of the v16 manual
  *apéndice* (OCTUBRE 2025 print): 48 codes — 23 *acreditables* (01,
  05-09, 11, 19-27, 48, 80-85), 21 *definitivas* (28-46, 49), one
  *sin-retención* (60) and three *no-gravados* (70-72) — as the machine
  catalog `l10n_sv.f14.income.code` seeded from the CSV sidecar
  `f14_income_codes.csv` (§4) with the columns code → description →
  class → F-14 row/casilla mapping → CT anchor, versioned by catalog
  vintage (v16_apendice, Oct-2025 print) with refresh re-checks against
  the v17 form row set and any annex-modification resolutions
  (SOQ-12 kin — OQ-001; the 06 file's OQ-004 pointer resolves HERE).
  (LB-001; EVID-182; EVID-184)
- **SV-FREP-FR-172:** The system shall give every catalog code exactly
  one CLASS driving its tax treatment and form routing —
  *acreditable* (creditable in the annual liquidation),
  *definitiva* (definitive *entero*, non-creditable), *sin-retención*
  (taxed income paid without retention) and *no-gravado*
  (non-taxable) — and shall expose the class routing to
  `06_f14-declaration.md` SV-FREP-FR-142 (membership validation +
  tab routing by class, consumed by forward reference); the class is a
  TREATMENT classification, not a retention-occurred flag: codes 81
  and 83 are class *acreditable* yet explicitly "sin retención", and
  codes 81-84 print in the form's definitivas 296-328 zone while
  remaining *acreditables* (class ≠ tab — encoded in the mapping
  column; per-code row assignment OQ-002). (LB-001; LB-002; EVID-182;
  EVID-183)
- **SV-FREP-FR-173:** The system shall wire the distributions codes —
  43 (*Pago o Acreditación de utilidades* to socios/accionistas/
  asociados/fideicomisarios/partícipes/inversionistas/beneficiarios,
  Ley Art. 72 → SV-TAX-FR-132), 44 (utilidades to non-domiciled
  subjects, Art. 73 → SV-TAX-FR-137), 45 (capital/patrimony
  reductions on the capitalized/reinvested-utilities portion, Art. 74
  → SV-TAX-FR-138) and 46 (*préstamos, mutuos, anticipos o
  financiamientos*, Art. 74-A + Art. 25 → SV-TAX-FR-139/142) — as the
  WITHHOLDING LEG of the distributions regime owned by
  `taxation/05_isr-distributions.md`: every 5%-retention posting of
  that file's `l10n_sv.isr.earnings.event` model (SV-TAX-FR-144/145)
  shall be reportable as an F-14 annex row on its code (43/44/45/46
  keyed by event type and recipient domicile), and every F-14 row on
  those codes shall trace back to an earnings-register event — the
  F-14 row reports the retention, never recomputes it (06-file
  SV-FREP-FR-168 parity). (LB-001; LB-007; EVID-182; cross-ref
  SV-TAX-FR-132/137/138/139/142/144/145)
- **SV-FREP-FR-174:** The system shall map code 40 — "Rentas de
  personas constituidas, domiciliadas o residentes en países con
  regimenes fiscales preferentes o paraísos fiscales" (rents of
  persons constituted, domiciled or resident in preferential-tax-regime
  countries or tax havens) — to the CT Art. 158-A 25% track owned by
  `taxation/04_isr-withholding.md` SV-TAX-FR-127, with the F-14-row
  exactness (neither below nor above 25%) enforced by
  `06_f14-declaration.md` SV-FREP-FR-141 and the haven classification
  fed by that file's dated country/haven table
  (SV-FREP-FR-139) — this catalog contributes only the code-40
  membership and its No-Domiciliados tab mapping. (LB-001; LB-002;
  EVID-182; EVID-183; cross-ref SV-TAX-FR-127, SV-FREP-FR-139/141)
- **SV-FREP-FR-175:** The system shall implement code 47 — rents to
  domiciled natural persons as interest, prizes and other utilities
  from money deposits — as the CT Art. 123 AGGREGATE ROW, per the
  apéndice's verbatim note: "Para la retención con el código 47, en
  atención al artículo 123 del Código Tributario, Inciso Tercero, la
  columna del NIT podrá completarla con 14 ceros ... y el campo del
  nombre podrá completarlo con la palabra VARIOS" (for the code-47
  retention, per CT Art. 123 third incise, the NIT column may be
  filled with 14 zeros and the name field with the word VARIOS): when
  the deposit-yield retention is reported without individual
  recipient identification, the row shall emit NIT =
  00000000000000 and name = VARIOS as a single aggregate row; the
  underlying deposit-yield retention rule is owned by
  `taxation/04_isr-withholding.md` SV-TAX-FR-128 (CT 159 zone kin).
  (LB-001; LB-006; EVID-182; cross-ref SV-TAX-FR-128)
- **SV-FREP-FR-176:** The system shall map code 60 — permanent-service
  income with labor subordination/dependency, "Tramo I de las Tablas
  de Retención" (Tramo I of the retention tables) — as the
  *sin-retención* class whose rows aggregate into the F-14 form's row
  58 "Ingresos gravados sin retención" (taxed income without
  retention, casilla zone 104/105) and into the F-910 consolidation
  under the ANNUAL 01-vs-60 rule of FR-180; the MONTHLY code-01/60
  selection (thresholds/modes) is owned by
  `taxation/04_isr-withholding.md` SV-TAX-FR-106 — never restated
  here. (LB-001; LB-002; LB-003; EVID-182; EVID-183; cross-ref
  SV-TAX-FR-106)
- **SV-FREP-FR-177:** The system shall map the *no-gravado* codes
  70/71/72 — indemnities for dismissal/voluntary retirement/death/
  incapacity/accident/illness, values guaranteed by endowment or
  other insurance, and foreign-service remunerations of government
  officials/employees, each printed "(según ley)" (per law) — to the
  reporting-only "INGRESOS NO GRAVADOS" rows 59-60 of the F-14 form,
  entering no retention total (the aguinaldo-exento aggregate shares
  those rows per `06_f14-declaration.md` SV-FREP-FR-156); the specific
  laws behind each "(según ley)" class are NOT in the corpus and stay
  unpinned (OQ-005); the Quincena-25 no-gravado class = code 73, a
  dated 2026-01 catalog row on MH-package authority (FR-212;
  v17-apéndice inclusion unverified — OQ-008). (LB-001; LB-002;
  EVID-182; EVID-183)

### 3.2 Cross-tax classification coupling (F-07 R/S pair + F-11 rentas matrix)

- **SV-FREP-FR-178:** The system shall implement the cross-tax
  classification coupling with ONE classification source per subject
  income: the F-07 Anexo 1 Renta pair's R code 12 — "Ingresos que ya
  fueron sujetos de retención informados en el F14 y consolidados en
  F910" (income already subject to retention, reported in the F-14
  and consolidated in the F-910) — shall be defaulted from THIS
  wave's retention data: income whose retention was reported in F-14
  annex rows on this file's catalog codes and consolidated in the
  F-910 (FR-179) is classified R=12 by the canonical lists and gates
  owned by `02_f07-annexes-sales.md` SV-FREP-FR-051/052 (cited by id;
  never restated here), and the same F-14/F-910 code surfaces feed
  the F-11 rentas matrix — the annual rentas declaration keyed by the
  income-type families that the R/S code lists prefigure (the F-11
  layout itself is not in the corpus: acquisition candidate, OQ-006);
  the Quincena code-73 surface is excluded (no retention happened —
  FR-212). (LB-008; LB-010; EVID-174; EVID-182; EVID-187; EVID-238;
  cross-ref SV-FREP-FR-051, SV-FREP-FR-052, SV-FREP-FR-212)

### 3.3 F-910 v9 — Informe Anual de Retención del ISR (the CT Art. 123 surface)

- **SV-FREP-FR-179:** The system shall build the F-910 *Informe Anual
  de Retención del ISR* (annual ISR retentions inform) as an ANNUAL
  GROUP BY *contribuyente* (taxpayer/retained subject) over the 12
  monthly F-14 annex rows of the *ejercicio* (fiscal year — the feed
  guaranteed by `06_f14-declaration.md` SV-FREP-FR-170): one row per
  contribuyente per income code with the annual sums — MONTO
  DEVENGADO (accrued amount), MONTO DEVENGADO ANUAL POR
  BONIFICACIONES Y GRATIFICACIONES (annual bonuses/gratuities),
  IMPUESTO RETENIDO (retained tax), the aguinaldo exento/gravado pair
  (applying ONLY to codes 01 and 60), and the ANNUAL social-security
  columns ISSS ANUAL · AFP ANUAL · IPSFA ANUAL · CEFAFA ANUAL · INPEP
  ANUAL · BIENESTAR MAGISTERIAL ANUAL (SIX annual columns as printed
  — the F-14's seventh column ISSS-IVM has NO annual column on the
  F-910) — with SUMAS TOTALES (grand totals). (LB-003; EVID-187;
  cross-ref SV-FREP-FR-170)
- **SV-FREP-FR-180:** The system shall classify each retained
  subject's annual payroll rows by the F-910's verbatim rule —
  "Los ingresos en concepto de Servicios de carácter permanente con
  subordinación o dependencia laboral, deben ser reportados en su
  totalidad en los códigos 01 ó 60 ... 1. En el código 01, si se le
  retuvo en al menos un mes del ejercicio fiscal. 2. En el código 60,
  si no se le retuvo en todo el ejercicio fiscal" (permanent-service
  income is reported in its entirety in codes 01 or 60: code 01 if
  retained in AT LEAST ONE month of the fiscal ejercicio; code 60 if
  not retained in the WHOLE ejercicio) — computed from the subject's
  12 monthly F-14 rows: any retained month ⇒ the whole year reports
  under 01; no retained month ⇒ under 60 (the ANNUAL counterpart of
  the monthly SV-TAX-FR-106 selection). (LB-003; EVID-187; cross-ref
  SV-TAX-FR-106)
- **SV-FREP-FR-181:** The system shall scope the F-910 per its §C
  header — "Datos del Contribuyente a quienes se les pagaron ingresos
  sujetos a retención, sin retención o no gravados" (data of the
  contributors to whom income SUBJECT TO RETENTION, WITHOUT
  RETENTION or NON-TAXED was paid) — so the inform includes rows for
  sin-retención (code 60) and no-gravado (70-72) income + code 73
  (Quincena-25, MH-package authority 2026-01; §C prints the v16
  catalog as of the 61_ v9 print — 73 arrives with the v17-era
  F-14/F-910 revision; F-910 v10 watch kin — FR-212), keyed by the
  SAME income-code catalog as the F-14 apéndice (the F-910 §C prints
  the identical catalog — LB-003/LB-001; this file §3.1 is the single
  source of truth for both surfaces). (LB-001; LB-003; LB-010;
  EVID-187; EVID-182; EVID-238)
- **SV-FREP-FR-182:** The system shall support the F-910's FOLIO
  MODIFICA (amendment folio) field: an amended inform shall reference
  the folio of the prior presentation and be rebuilt as a full
  recomputation over the (corrected) F-14 rows of the ejercicio —
  clean-and-replace semantics by parity with the F-14 modificatoria
  of `06_f14-declaration.md` SV-FREP-FR-164 (no merge into prior
  output). (LB-003; EVID-187; cross-ref SV-FREP-FR-164)
- **SV-FREP-FR-183:** The system shall expose the F-910 as the CT
  Art. 123 electronic-reporting surface for ISR retentions — the
  annual per-subject report of name, NIT, base and retained tax
  (LB-006) — due February per the 30_ calendar (F12 cluster;
  deadline behavior owned by `08_filing-calendar.md`, SOQ-08), with
  its row set derived exclusively from the validated F-14 annex rows
  (declaration-inform consistency: the F-910 is the projection of the
  twelve F-14 declarations, never an independent entry surface).
  (LB-003; LB-006; EVID-187; EVID-064)
- **SV-FREP-FR-212:** The system shall populate the F-910's NO
  GRAVADOS surface with income code **73 'Ingresos No Gravados
  Pagados Quincena Veinticinco'** — auto-assigned at declaration
  presentation from the F-14 Quincena annex upload
  (`06_f14-declaration.md` SV-FREP-FR-211; 68_ p.16), fed by the
  SV-PAY-FR-142 ledger — reported as a NO-GRAVADO total (the
  worker-side amounts), never as a retention consolidation (no R=12
  coupling: nothing was retained) and never inside the retained-tax
  totals; the code exists in the catalog as a dated 2026-01 row whose
  print authority is the MH package, with F-14 apéndice v17 inclusion
  unverified (OQ-008). (LB-010; EVID-238; cross-ref SV-FREP-FR-211,
  SV-PAY-FR-142)

> **In-file note for the index task (taxation cross-refs to wire):**
> this file RECORDS the answer to `taxation/04_isr-withholding.md`
> §7 OQ-007 (MOQ-10 kin) — the ISR electronic-reporting surface is
> the **F-910** (CT Art. 123 annual per-contribuyente consolidation
> of the F-14 rows; due February; the DTE *reteRenta* field is
> FSEE-only per DG45 §3.1 N°147 and is NOT the channel) — and the
> kin answer for `taxation/05_isr-distributions.md` §7 OQ-006: the
> 5%-distributions retention surfaces through the F-14 codes 43-46
> rows and their F-910 consolidation (plus the F-915 inform,
> FR-184..189). The index task (`taxation/00_index.md` +
> `fiscal-reporting/00_index.md`) should mark 04-OQ-007 ANSWERED
> (surface = F-910, this file §3.3) and 05-OQ-006 ANSWERED-KIN
> (surfaces = F-14 §3.1 codes 43-46 + F-910 + F-915, this file).

### 3.4 F-915 v4 — Informe de Distribución o Capitalización de Utilidades

- **SV-FREP-FR-184:** The system shall build the F-915 *Informe de
  Distribución o Capitalización de Utilidades* with its two exclusive
  modes — §A "11 DISTRIBUYÓ" (distributed) / "CAPITALIZÓ"
  (capitalized) checkboxes with the *ACTA JUNTA GENERAL DE
  ACCIONISTAS* (general shareholders' meeting minutes) linkage "04
  Fecha / 05 Número" (date / number), plus 01 EJERCICIO FISCAL,
  02 FOLIO MODIFICA and 03 NIT — the checked mode(s) governing which
  §B/§C amount columns are populated: distributed amounts under
  DISTRIBUYÓ, capitalized book values under CAPITALIZÓ (the form
  prints both checkboxes and both column families; no presentation
  mode beyond the checkboxes is printed — single-vs-multiple
  presentation behavior is a filing-practice question).
  (LB-004; EVID-188)
- **SV-FREP-FR-185:** The system shall fill §B "Calidad de Socios"
  (partner quality) with the three transition buckets verbatim —
  "Socio, Accionista o Cooperado que adquirió la calidad con
  anterioridad al ejercicio que informa" (acquired the quality
  BEFORE the reported ejercicio) / "...durante el ejercicio que
  informa" (DURING it) / "...que ha perdido la calidad durante el
  ejercicio que informa" (LOST it during it) — each bucket carrying
  the Cantidad (count) / Monto de Utilidades, Dividendos o
  Excedentes Distribuidos (amount of distributed utilities, dividends
  or excesses) / Valor Contable de las Acciones, Aportes,
  Participaciones Sociales o Derechos Capitalizados (book value of
  capitalized shares, contributions, participations or rights)
  triple, plus the TOTAL row. (LB-004; EVID-188)
- **SV-FREP-FR-186:** The system shall emit the §C per-socio detail
  rows — "N° / No Domiciliado / NIT / ..." — one row per socio with
  the NON-DOMICILED flag and NIT identification (per-socio amounts
  consistent with the §B bucket they roll into; non-domiciled socios
  are the code-44 kin of §3.1). (LB-004; EVID-188)
- **SV-FREP-FR-187:** The system shall build the F-915 over the
  earnings register of `taxation/05_isr-distributions.md`
  (`l10n_sv.isr.earnings.register` / `l10n_sv.isr.earnings.event`,
  SV-TAX-FR-144/145): DISTRIBUYÓ amounts from the paid/credited
  event lines (SV-TAX-FR-134 event types), CAPITALIZÓ book values
  from the capitalization/reinvestment events
  (SV-TAX-FR-143 b/c — *untaxed-to-capitalized* pool effects), and
  the §B quality-transition classification derived from register and
  partner-master events: quality acquired before the ejercicio /
  during it / lost during it, per socio; where a socio's transition
  data is absent the row is flagged for manual completion rather than
  defaulted. (LB-004; LB-007; EVID-188; cross-ref SV-TAX-FR-134/
  143/144/145)
- **SV-FREP-FR-188:** The system shall render the F-915 juramento
  (sworn statement) with its printed anchors — CT Art. 241 and CP
  249-A (as printed on the form; no article text invented) — as the
  declaration's certification surface. (LB-004; EVID-188)
- **SV-FREP-FR-189:** The system shall treat the F-915 as the
  PUBLISHED REPORTING FORMAT behind the Ley ISR Arts. 74/74-C
  distributions inform — the surface that
  `taxation/05_isr-distributions.md` FR-149 exposes the earnings
  register for (CT Art. 124 dividends/shareholder-list kin per
  LB-006): the F-915 builder consumes the register per FR-187 and
  reports nothing the register does not trace.
  (LB-004; LB-006; LB-007; EVID-188; cross-ref SV-TAX-FR-149)

> **In-file note for the index task (partial answer to wire):** the
> F-915 (v4, 2017-11-22 print, still listed by MH 2026-08-18)
> PARTIALLY ANSWERS `taxation/05_isr-distributions.md` §7 OQ-002 —
> the FORMAT for the Registro de Control de Utilidades reporting
> EXISTS (this form); the DGII administrative-norms resolution
> itself is still absent (register layout norms beyond this form's
> fields remain open there). The index task should annotate
> 05-OQ-002 "partially answered by fiscal-reporting 07 §3.4
> (F-915 = published format; norms resolution still absent)".

### 3.5 F-930 v3 — reference only

The F-930 v3 *Informe Mensual de Retención/Percepción/Anticipo IVA*
(monthly IVA retentions/perceptions/anticipos inform) is ALREADY HOMED
in `04_f07-annexes-retentions-events.md` (a view over the same
IVA-retention ledger as the F-07 annexes 9-12 — document-type summary +
calidad/modalidad classifiers, per EVID-189/LB-009). No FR is written
here; this section records only the inform inventory entry and the
vintage note of FR-194.

### 3.6 F-935 v1 — Informe Mensual de Retención sobre Agentes Extranjeros

- **SV-FREP-FR-190:** The system shall build the F-935 *Informe Mensual
  de Retención sobre Agentes Extranjeros* (monthly foreign-agents
  retention inform) header §A — PERIODO TRIBUTARIO (tax period),
  FOLIO MODIFICA (amendment folio, same clean-and-replace semantics
  as FR-182) and NIT/DUI identification — as a MONTHLY inform (the
  transaction-level counterpart of the F-14's Agentes Extranjeros
  tab, `06_f14-declaration.md` SV-FREP-FR-161 — cross-referenced,
  never duplicated: both surfaces read the same foreign-agent
  retention ledger rows). (LB-005; EVID-190; cross-ref
  SV-FREP-FR-161)
- **SV-FREP-FR-191:** The system shall aggregate the §B blocks by
  CONCEPTO with the verbatim rows — "RETENCION DE IMPUESTO" (tax
  RETENTION) / "ENTERO DE IMPUESTO" (tax REMITTANCE) / "TOTAL" — each
  carrying TOTAL DE REGISTROS (record count) / MONTO SUJETO (subject
  amount) / MONTO DE RETENCION (retention amount): the RETENCIÓN
  block totals the retained-side transfers and the ENTERO block the
  remitted-side (donantes locales) transfers, matching the F-14 tab's
  two sections (701-720 retención vs 751-780 entero). (LB-005;
  EVID-190)
- **SV-FREP-FR-192:** The system shall emit the §C transfer-level
  detail rows — "Datos de impuesto retencion / donantes locales" —
  one row per transfer with N / NIT-NIF / name and the DATOS DE
  TRANSFERENCIA (transfer data): CONCEPTO · FECHA (date) · NÚMERO DE
  TRANSACCIÓN (transaction number) · PAIS DE ORIGEN (country of
  origin) · MONTO SUJETO · MONTO RETENCION/ENTERO — the
  transaction-number and country-of-origin fields being the
  foreign-agent detail that the F-14 tab aggregates away; the country
  of origin consumes the same dated country-code table as
  `06_f14-declaration.md` SV-FREP-FR-139. (LB-005; EVID-190;
  cross-ref SV-FREP-FR-139)
- **SV-FREP-FR-193:** The system shall carry the *donantes locales*
  (local donors) ENTERO track with its normative anchor OPEN: the
  form prints the wording without a CT article (CT 156 zone or a
  specific regime — SOQ-13, OQ-003); the track shall be implemented
  as data (the entero-block rows keyed by their concepto class) with
  the anchor resolution deferred — no regime substance invented.
  (LB-005; EVID-190; SOQ-13)
- **SV-FREP-FR-194:** The system shall gate the four inform layouts
  by their printed vintages as DATED DATA — F-910 v9 (2021 print,
  listed current 2026-08-18), F-915 v4 (2017-11-22 print), F-930 v3
  (2017-era print, homed in the 04 file) and F-935 v1 (2025 print)
  — each layout versioned in its model with source and print date,
  and a re-check cadence when the MH formularios page updates any of
  them or a calendar year rolls (61-64-file OQ-2 kin; F-910 v10
  pending-check included — OQ-004). (LB-003; LB-004; LB-009; LB-005;
  EVID-187; EVID-188; EVID-189; EVID-190)

### 3.7 Dictamen e informe fiscal (75_ Arts. 58-72) — historical awareness (no FRs)

The 75_ *dictamen e informe fiscal* block (Arts. 58-72, LB-011) is the
2001 blueprint of a mandatory fiscal-audit inform family this corpus
records as HISTORICAL awareness only (EV75 OQ-3: the regime was
restructured at the CT level post-2001 and 05_ carries no dictamen
entry — CT 130-137 zone unextracted; OQ-009): the appointment clocks
(auditor named "a más tardar dentro de los primeros cinco meses del
período anual a dictaminar", notice to the AT within 30 días
calendario), the 31-may dictamen+informe filing deadline with the
6-month liquidación/fusión clock, the formal-vs-substantive
incumplimiento separation "debiendo cuantificarse monetariamente el
impacto impositivo", EEFF per "las Normas Internacionales de
Contabilidad" (SOQ-46 kin — Consejo-de-Vigilancia criteria first), and
the a)-n) anexo set whose IVA determination chain (b.3) and
exporter-reintegro chains (l) restate ledger-by-ledger the computations
already encoded from live instruments (SV-TAX-FR-269..283,
`11_iva-pro-rata-remanente.md` + `14_iva-exports-refunds.md`, by id —
never restated here). The blueprint's validation shape (per-ledger
determination annexes reconciled against declared values) descends to
the modern inform family of this file, and the calendar's surviving
dictamen surfaces (F-455 fusión dictámenes and CT-131 auditor
appointments) live in `08_filing-calendar.md` FR-195 — nothing in this
section is ever an operative FR.

## 4. Data Model

Machine-readable catalog: **`f14_income_codes.csv`** lives next to
this file (the taxation-CSV conventions: lowercase snake headers,
comma-delimited, quoted notes, catalog_version + valid_from vintage
columns). Layer semantics: Odoo-side computation/bookkeeping data only
(wave default `odoo`; see §5).

**Income-code catalog — l10n_sv.f14.income.code (new; THE catalog home
consumed by 06 FR-142):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| code, description_es | char(2)/char | the 48 codes of LB-001 verbatim ([sic] elisions kept in CSV notes) | FR-171 |
| class | select | acreditable · definitiva · sin_retencion · no_gravado | FR-172 |
| f14_tab, f14_row_casilla | char/char | tab + row/casilla ZONE per LB-002 (zone granularity; per-row assignment OQ-002) | FR-172, FR-174..177 |
| ct_anchor | char | printed/derived anchor (e.g. "CT 158-A", "Ley ISR Art. 72", "CT Art. 123 Inciso Tercero"); "unpinned" rows carry OQ flags | FR-173..175 |
| catalog_version, valid_from, source | char/date/char | v16_apendice · 2025-10-01 (print month) · 35_ pp.17-18; code 73 = DATED 2026-01 row (f17_kin vintage — MH-package authority 67_ §3.f + 68_ p.16, NOT the v16 apéndice which predates the law; FR-212); refresh re-check OQ-001 | FR-171, FR-212 |

**F-910 — l10n_sv.f910.report (new) + l10n_sv.f910.row:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| report: ejercicio, folio_modifica, form_version | char/m2o-char/char | v9 (2021 print); folio → prior presentation | FR-179, FR-182, FR-194 |
| row: partner (contribuyente), income_code_id | m2o/m2o | one row per contribuyente per code; code from l10n_sv.f14.income.code | FR-179, FR-181 |
| row: devengado, bonificaciones_gratificaciones, impuesto_retenido | monetary(2dp) | annual sums over the 12 monthly F-14 rows | FR-179 |
| row: aguinaldo_exento, aguinaldo_gravado | monetary(2dp) | ONLY codes 01 and 60 | FR-179 |
| row: ss_annual_isss, ss_annual_afp, ss_annual_ipsfa, ss_annual_cefafa, ss_annual_inpep, ss_annual_bienestar_mag | monetary(2dp) | SIX annual columns as printed (no ISSS-IVM annual) | FR-179 |
| row: payroll_class_01_60 | computed | 01 (retained ≥ 1 month) / 60 (never retained) from the monthly rows | FR-180 |
| row: code_73_auto | boolean + m2o income_code_id (73) | code 73 handled as a catalog row + AUTO-assignment flag (set at the FR-211 Quincena annex presentation); NO-GRAVADO total (worker-side), never inside retained-tax totals | FR-212 |

**F-915 — l10n_sv.f915.report (new) + l10n_sv.f915.socio.row:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| report: ejercicio, folio_modifica, nit, mode | char/m2o/char/select | distribuyo · capitalizo (checkbox modes) | FR-184 |
| report: acta_fecha, acta_numero | date/char | ACTA JUNTA GENERAL DE ACCIONISTAS 04/05 | FR-184 |
| socio.row: earnings_register_id (m2o l10n_sv.isr.earnings.register), partner_id, nit, no_domiciliado | m2o/m2o/char/boolean | per-socio §C rows incl. non-domiciled flag | FR-186, FR-187 |
| socio.row: quality_transition | select | antes (acquired before the ejercicio) · durante (during) · perdio (lost during) | FR-185 |
| socio.row: cantidad, utilidades_distribuidas, valor_contable_capitalizadas | integer/monetary(2dp)/monetary(2dp) | the §B triple per bucket + TOTAL | FR-185 |
| report: juramento_anchors | char (printed) | "CT 241 + CP 249-A" as printed | FR-188 |

**F-935 — l10n_sv.f935.report (new) + l10n_sv.f935.transfer.row:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| report: period, folio_modifica, nit_dui, form_version | char/m2o/char/char | monthly; v1 (2025 print) | FR-190, FR-194 |
| report: block_retencion totals, block_entero totals | monetary+integer | TOTAL DE REGISTROS / MONTO SUJETO / MONTO DE RETENCION per §B row (RETENCION / ENTERO / TOTAL) | FR-191 |
| transfer.row: block | select | retencion · entero (donantes locales) | FR-191, FR-193 |
| transfer.row: nit_nif, name | char | per-transfer subject | FR-192 |
| transfer.row: concepto, fecha, numero_transaccion, pais_origen (m2o l10n_sv.f14.country.code), monto_sujeto, monto_retencion_entero | char/date/char/m2o/monetary(2dp) | DATOS DE TRANSFERENCIA | FR-192 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transmission (the only architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`). Model
names are stable across Odoo 17/18/19/20; version-specific behavior is
recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-171 | odoo | l10n_sv.f14.income.code + f14_income_codes.csv | catalog seed | D12: v16_apendice vintage (Oct-2025 print), 48 codes complete; refresh re-check vs v17 row set + resolutions (OQ-001; resolves 06-OQ-004 pointer); AC-001 |
| FR-172 | odoo | l10n_sv.f14.income.code | class | 4 classes; consumed by 06 FR-142 routing; class ≠ tab nuance (81-84) encoded in mapping column (OQ-002); AC-002 |
| FR-173 | odoo | l10n_sv.isr.earnings.event → annex row builder | codes 43/44/45/46 | Withholding leg: 43=Art.72/FR-132, 44=Art.73/FR-137, 45=Art.74/FR-138, 46=74-A+25/FR-139/142; bidirectional trace register-event ↔ F-14 row; AC-003 |
| FR-174 | odoo | l10n_sv.f14.income.code (code 40) | haven row | CT 158-A rule = SV-TAX-FR-127; exactness = 06 FR-141; haven table = 06 FR-139; this file contributes membership + No-Domiciliados mapping only |
| FR-175 | odoo | l10n_sv.f14.annex.row builder (code 47) | nit=00000000000000, name=VARIOS | CT Art. 123 Inciso Tercero verbatim; deposit-yield rule = SV-TAX-FR-128; AC-004 |
| FR-176 | odoo | l10n_sv.f14.income.code (code 60) + l10n_sv.f910.row | payroll_class_01_60 | Monthly selection = SV-TAX-FR-106; annual rule FR-180; row 58 aggregate = 06 FR-156; AC-005 |
| FR-177 | odoo | l10n_sv.f14.income.code (70-72) | no-gravado rows | "(según ley)" laws unpinned (OQ-005); reporting-only (06 FR-156 kin); Quincena-25 class = code 73 dated row (FR-212) |
| FR-178 | odoo | l10n_sv.f07.renta.classification (02-file model) + F-910 read API | R=12 default | Coupling FR: canonical lists/gates = SV-FREP-FR-051/052 (by id); F-910 output backs the R=12 classification; F-11 feed = acquisition candidate (OQ-006); AC-006 |
| FR-179 | odoo | l10n_sv.f910.report/row | GROUP BY contribuyente × code | Annual sums over 12 monthly F-14 rows (06 FR-170 feed); catalog scope + code 73 (Quincena-25, MH-package authority 2026-01; §C prints the v16 catalog as of the 61_ v9 print — 73 arrives with the v17-era F-14/F-910 revision; F-910 v10 watch kin); 6 annual SS columns as printed (no ISSS-IVM); AC-005 |
| FR-180 | odoo | l10n_sv.f910.row | payroll_class_01_60 | Verbatim rule: retained ≥1 month → 01; never → 60; AC-005 |
| FR-181 | odoo | l10n_sv.f910.row | scope | Includes sin-retención (60) + no-gravado (70-72) rows + code 73 (Quincena-25, MH-package authority 2026-01; §C prints the v16 catalog as of the 61_ v9 print — 73 arrives with the v17-era F-14/F-910 revision; F-910 v10 watch kin); same catalog (§3.1) for F-14 + F-910; AC-001 |
| FR-182 | odoo | l10n_sv.f910.report | folio_modifica | Clean-and-replace by parity with 06 FR-164 |
| FR-183 | odoo | l10n_sv.f910.report (read/export surface) | CT 123 exposure | The CT 123 electronic surface (records taxation 04-OQ-007 answer — in-file note §3.3); due-February wiring = 08 file (SOQ-08); 04-OQ-006 kin |
| FR-212 | odoo | l10n_sv.f910.row (code_73_auto) + l10n_sv.f14.income.code (73) | NO GRAVADOS surface | Code 73 auto-assigned at presentation from the FR-211 upload (fed by SV-PAY-FR-142); NO-GRAVADO total — no R=12 coupling, never in retained-tax totals (FR-178 exclusion); catalog row dated 2026-01 (f17_kin; v17 apéndice inclusion OQ-008); AC-010 |
| FR-184 | odoo | l10n_sv.f915.report | mode + acta | DISTRIBUYÓ/CAPITALIZÓ checkboxes; acta fecha/número; folio-modifica; v4 vintage (FR-194) |
| FR-185 | odoo | l10n_sv.f915.socio.row | quality_transition triple | antes/durante/perdió × cantidad/utilidades/valor-contable + TOTAL; AC-007 |
| FR-186 | odoo | l10n_sv.f915.socio.row | §C per-socio rows | No-Domiciliado flag + NIT; code-44 kin; AC-007 |
| FR-187 | odoo | l10n_sv.isr.earnings.register/.event → f915 builder | register interface | DISTRIBUYÓ from paid/credited events (FR-134 types); CAPITALIZÓ from capitalization events (FR-143 b/c); missing transition data flagged, never defaulted; AC-007 |
| FR-188 | odoo | l10n_sv.f915.report | juramento anchors | CT 241 + CP 249-A as printed; no article text invented |
| FR-189 | odoo | l10n_sv.f915.report (read/export surface) | earnings-register exposure | The published format behind Art. 74/74-C inform (05 FR-149 interface; CT 124 kin); records 05-OQ-002 partial answer — in-file note §3.4 |
| FR-190 | odoo | l10n_sv.f935.report | header + folio | Monthly; counterpart of F-14 Agentes Extranjeros tab (06 FR-161) — same ledger, two views |
| FR-191 | odoo | l10n_sv.f935.report | RETENCIÓN/ENTERO blocks | Counts + montos per §B row; maps to F-14 701-720 vs 751-780; AC-008 |
| FR-192 | odoo | l10n_sv.f935.transfer.row | transfer-level fields | CONCEPTO/FECHA/NÚMERO DE TRANSACCIÓN/PAÍS DE ORIGEN/MONTO SUJETO/RETENCIÓN-ENTERO; country via l10n_sv.f14.country.code (06 FR-139); AC-008 |
| FR-193 | odoo | l10n_sv.f935.transfer.row (block=entero) | donantes-locales track | SOQ-13 anchor OPEN (OQ-003); data-only implementation |
| FR-194 | odoo | all four report models | form_version fields | D12 dated vintages: F-910 v9 (2021), F-915 v4 (2017-11-22), F-930 v3 (2017, 04 file), F-935 v1 (2025); re-check cadence OQ-004 (61-64-file OQ-1/OQ-2 kin) |

Version-regime notes (D12): the income-code catalog is a DATED table
(v16 apéndice, Oct-2025 print — the operative authority for annex
mechanics per the S3 version regime; re-check against the v17 row set
and any annex-modification resolutions, OQ-001); the code-73 row is a
dated 2026-01 vintage on MH-package authority, NOT the v16 apéndice
(FR-212); the four inform layouts are vintage-gated prints (FR-194);
the catalog's mapping column carries zone-granularity values pending a
form-visual per-row pass (OQ-002). Filing due days stay unpinned
(`08_filing-calendar.md`; SOQ-08).

## 6. Acceptance Criteria

- **AC-001:** Given the catalog seed, then `f14_income_codes.csv`
  loads exactly 48 codes — 23 acreditable, 21 definitiva, 1
  sin-retención (60), 3 no-gravado (70/71/72) — PLUS the dated
  2026-01 code-73 row (Quincena-25, f17_kin vintage — FR-212; 49 rows
  total), each with class, tab,
  row/casilla zone and CT-anchor columns populated (unpinned anchors
  flagged, not blank), and the F-910 §C consumes the SAME code list
  as the F-14 apéndice (codes 43 and 60 resolve identically on both
  surfaces) (FR-171, FR-181).
- **AC-002:** Given an F-14 annex row on code 81 (*Servicios de
  Carácter Permanente sin retención prestado por Jubilados y
  Pensionados*), then the catalog classifies it class =
  *acreditable* while its mapping column places it in the
  definitivas 296-328 print zone — class and tab disagree by design
  and the row totals to the printed zone's casillas, never to the
  acreditable totals 221/225 (FR-172).
- **AC-003:** Given a $10,000 dividend distribution retained at 5%
  ($500.00) recorded as an earnings-register paid_credited event
  (taxation/05 FR-132/134), then the F-14 annex builder emits one row
  — code 43 for a domiciled socio (code 44 for a non-domiciled
  recipient; code 45 for the capitalized-earnings portion of a
  capital reduction; code 46 for a 74-A loan) — with I = 500.00 and
  a trace to the register event; and given the same event queried
  from the F-14 side, the register event is recovered (FR-173).
- **AC-004:** Given a bank's code-47 deposit-yield retention of
  $1,200.00 retained across unidentified depositors, then the F-14
  annex emits ONE aggregate row: code 47, NIT =
  **00000000000000** (14 zeros), name = **VARIOS**, I = 1,200.00 —
  and no per-depositor identification is required (FR-175).
- **AC-005:** Given an employee with 12 monthly F-14 code-01/60 rows
  for ejercicio 2026 — retained in March through June only, never
  otherwise, with annual devengado 14,400.00, bonuses 600.00,
  retained tax 850.00, aguinaldo 1,000.00 (800.00 exento / 200.00
  gravado), ISSS 252.00 and AFP 1,830.00 — then the F-910 emits ONE
  row for the contribuyente with payroll class = **01** (retained in
  at least one month), devengado 14,400.00, bonificaciones 600.00,
  impuesto retenido 850.00, aguinaldo exento 800.00 / gravado 200.00,
  ISSS ANUAL 252.00 and AFP ANUAL 1,830.00; and given a second
  employee never retained in any month, then that row reports under
  class **60** (FR-179, FR-180, FR-176).
- **AC-006:** Given a B2B sale of $5,000 to a client whose ISR
  retention on an honorarios invoice (code 11, $500.00 retained) was
  reported in the F-14 and consolidated in the F-910, then the F-07
  Anexo 1 Renta classification defaults that client's operation to
  R = 12 ("Ingresos que ya fueron sujetos de retención informados en
  el F14 y consolidados en F910") under the FR-051/FR-052 lists;
  given no retention trace exists, then the default is NOT 12
  (FR-178).
- **AC-007:** Given an earnings register where Socio A held shares
  before 2026 and received $12,000 of utilidades, Socio B acquired
  quality in March 2026 and received $8,000, and Socio C lost quality
  in September 2026 after a $20,000 capitalization of utilidades at a
  $20,000 book value, then the F-915 §B fills: bucket *antes* —
  cantidad 1, utilidades distribuidas 12,000.00; bucket *durante* —
  cantidad 1, 8,000.00; bucket *perdió* — cantidad 1, valor contable
  capitalizadas 20,000.00 — and §C carries one row per socio with
  the No Domiciliado flag false (or true for a non-domiciled socio,
  code-44 kin) (FR-185, FR-186, FR-187).
- **AC-008:** Given a July foreign-agent month with two transfers —
  (a) a RETENCIÓN-side transfer of $50,000 subject amount with
  $10,000.00 retained, transaction number T-001 from country 9301;
  (b) an ENTERO-side donantes-locales transfer of $30,000 subject
  with $6,000.00 remitted, transaction T-002 from country 9900 —
  then the F-935 §B reports RETENCION DE IMPUESTO (1 record,
  50,000.00, 10,000.00), ENTERO DE IMPUESTO (1 record, 30,000.00,
  6,000.00) and TOTAL (2 records, 80,000.00, 16,000.00), and §C
  carries both transfer rows with their fecha, número de
  transacción and país de origen intact (FR-191, FR-192).
- **AC-009:** Given the four inform models, then each carries its
  form_version vintage field — F-910 v9 (2021 print), F-915 v4
  (2017-11-22), F-935 v1 (2025), F-930 v3 (2017, homed in the 04
  file) — and a folio_modifica amendment of an F-910 rebuilds the
  whole ejercicio from the corrected F-14 rows without merging prior
  output (FR-194, FR-182).
- **AC-010:** Given the Task-4 fixture (10 subjects, US$5,000.00
  presented in January 2027), then the F-910 §C renders a code-73 row
  NO GRAVADOS with US$5,000.00, zero retained tax, and the R=12
  surface is untouched (FR-212).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Income-code catalog fidelity (OWNS the 06-file OQ-004 pointer; SOQ-12 kin): the catalog transcribed in EVID-182 is the v16 manual apéndice (Oct-2025 print) — verify against the v17 form's row set (EVID-184 shows no catalog change, only the Quincena-25 section + renumbering) and against any DGII annex-modification resolutions (29_-file OQ-1 kin — the resolutions behind v14/v16/v17 are not in the corpus). FR-171 seeds the catalog with catalog_version gating; a resolution-driven change re-dates the vintage. | no | Takumi S3 (sources registry) | open |
| OQ-002 | Per-code row/casilla assignment granularity: LB-002 pins tab + row-ZONE assignments but not a clean per-code row map for every zone (the 296-328 block groups codes 42/43-46/49/81-84; the con-dependencia impuesto zone 150-164 has more casillas than pinned code assignments). The CSV mapping column carries zone values; a form-visual per-row pass (or plantilla/MH validation) must pin exact rows before byte-exact form-mirror certification. | no | Takumi S3 | open |
| OQ-003 | SOQ-13 (OWNS the anchor): F-935's "donantes locales" entero track — which CT article or specific regime governs (CT 156 zone? a donor-agreement regime?) — is unstated in the form; FR-193 implements the track as data with the anchor open; chase in the CT matrix before encoding any regime substance. | no | Takumi S3 (CT matrix re-check) | open |
| OQ-004 | Inform vintage re-check cadence (61-64-file OQ-1/OQ-2 kin): F-910 v9 (2021 print; no v10 pending on the MH list 2026-08-18 — confirm no v10 publishes), F-915 v4 / F-930 v3 (2017 prints still listed 2026-08-18 — assume current, re-check when a calendar year rolls or the MH formularios page updates) and F-935 v1 (2025). Also: the F-910 upload/annex FORMAT (the per-contribuyente upload file structure) is not in the corpus — acquire when DGII/MH publishes the F-910 manual (35_-file OQ-6 kin). | no | Takumi S3 (sources registry) | open |
| OQ-005 | "(Según ley)" anchors (codes 70-72) and unpinned codes (49/84 investor remunerations; 19/20/26/42/48 matrix-zone codes): the specific laws behind the no-gravado classes and the per-code CT articles for the matrix-zone codes are not pinned in the corpus — catalog rows carry "unpinned"/"matrix zone" anchors; pin during the CT matrix re-check pass without inventing article text. | no | Takumi S3 (CT matrix re-check) | open |
| OQ-006 | F-11 rentas matrix acquisition (coupling counterpart): FR-178 states the F-14/F-910 → F-11 feed at coupling level per the R/S code lists, but NO F-11 form or manual is in the corpus (the F12 calendar lists F-11 among the April annuals) — acquisition candidate; the coupling FR stays at the classification-source level until the F-11 layout lands. | no | Takumi S3 (sources registry) | open |
| OQ-007 | Index-task wiring (tracking row, not a doubt): the in-file notes of §3.3/§3.4 record (a) the ANSWER to taxation/04 §7 OQ-007 / MOQ-10 (ISR electronic-reporting surface = F-910) and the kin answer for taxation/05 OQ-006, and (b) the PARTIAL answer to taxation/05 §7 OQ-002 (F-915 = published format; norms resolution absent) — the index task (taxation/00_index.md + fiscal-reporting/00_index.md) must wire these cross-references. | no | Takumi S3 (index task) | open |
| OQ-008 | Code 73 in the F-14 apéndice v17 unverified — no v17 manual exists (SOQ-09 doc-completeness residue): the W11 package pins code 73's F-910 side (67_ §3.f + 68_ p.16, EVID-238) but no v17 apéndice print is in the corpus, so the catalog carries 73 as a dated 2026-01 f17_kin row on MH-package authority; re-check at the v17 manual / F-910 v10 acquisition (≥71 watch; OQ-004 kin). | no | Takumi S6 (sources registry) | open |
| OQ-009 | Dictamen regime vintage watch (EV75 OQ-3; W17 fold-in LB-011/§3.7): the 75_ Arts. 58-72 mandatory fiscal-audit regime (appointment clocks, 31-may dictamen+informe deadline, a)-n) anexo set incl. the IVA prorrata b.3 / reintegro l chains, NIC EEFF) was restructured at the CT level post-2001 — corpus 05_ carries NO dictamen entry (CT 130-137 zone unextracted). Carried as HISTORICAL blueprint only (never operative FRs); pin the current CT text before any operative encoding of dictamen surfaces. | no | Takumi W17 (CT re-anchor pass) | open |
