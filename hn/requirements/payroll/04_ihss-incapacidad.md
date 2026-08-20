# HN — Payroll — IHSS incapacidad temporal: subsidy cost-split, episode semantics, maternity & refrendo (RIT)

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the IHSS *incapacidad
temporal* (temporary disability/sick-leave) subsidy layer of cluster P6, under
the Reglamento de Incapacidad Temporal (RIT, G 35,267-B 29-may-2020, in force
2020-07-29) and its authorizing statute (Ley del Seguro Social, LI). It owns:
(a) the **cost-split** — days 1-3 of each case = employer-paid full SALARY (no
unpaid *cuarentena* exists, R-H52), days 4-365 = IHSS subsidy of 66% of the
*salario base mensual de referencia* (monthly reference base salary) capped by
the regime *techo* (contribution ceiling) plus the **mandatory employer
complement** to full salary (RIT Art. 73, with the R-H53 daily-derivative
formula default); (b) **episode/case semantics** — the 35-day *prórroga*
(extension) same-case key, case-level 3-day wait, 182+183=365-day structure,
273-day alert with maternity exclusion, CTI reset, overlap and eligibility
inheritance; (c) the **maternity subsidy** — 42 prenatal + 42 postnatal days
anchored to the probable-partum date, +14 late-birth days, contribution
qualifiers, contractual excess at employer cost, and the one reconciliation
cross-reference to the CT-side maternity rest; (d) the **refrendo
(validation) workflow** and its deadline matrix with grace windows and
employer document duties; (e) the **entitlement & no-pay matrix** —
contribution qualifiers, employer-mora and uninsured-by-employer full-salary
triggers, ≤30-day liquidation tranches, 1-year prescription,
incompatibilities, and the ISR non-gravable tagging interface.

It does **not** own: IHSS cotización rates, ceilings and base-composition
mechanics — file 03 (`03_ihss-cotizaciones.md`, HN-PAYR-FR-101..135) owns the
*techo* dated rows this file consumes by id; CT-side maternity rest,
suspension of the labor contract and its 4+6-week frame — file 09
(`09_*`, HN-PAYR-FR-331..357, P11); RAP/fondo tranche computations over leave
periods — file 05 (`05_*`, HN-PAYR-FR-181..215); ISR exclusion semantics —
taxation/02 (HN-TAX-FR-046..078) and the plantilla engine taxation/04
(HN-TAX-FR-121..153), consumed by id; salary/attendance records — file 10
(HN-PAYR-FR-371..405); IHSS mora interest and multas — file 03/LI enforcement
surface; riesgos profesionales cotización rates (not in corpus, 87_ OQ-2
family acquisition lead).

## 2. Legal Basis

Authority order (binding, per master evidence index): RIT = `88_` (G 35,267-B
29-may-2020; approved Res. CI IHSS-RSAS No. 213/10-04-2018, actualizada Res.
No. 1335/05-12-2019 — edition dates cited per R-H65); statute frame = `87_`
Ley del Seguro Social (D.140-1959 + D.80-2001 consolidation, TSC print; use
OCR layer only, title-page date noise per 87_ OQ-3); ceilings input = `81_`
D.48-2024 Art. 2 (rows OWNED by file 03; cited here only as the consumed
input). D-H1/D-H2 bind everything (dated rows, per-episode day-indexing,
resolution by payslip period / hecho generador, never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | RIT Arts. 1 y 3 (objeto; carve-out) | Art. 1 object: "1.1 La emisión del Certificado de Incapacidad Temporal, extendido por personal médico y odontológico del Instituto Hondureño de Seguridad Social, Sistema Médico de Empresas (SME) y Sistemas Locales de Seguridad Social (SILOSS), a los trabajadores asegurados; y, 1.2 El refrendo de las certificaciones o constancias expedidas a los trabajadores asegurados por médicos y odontólogos en el ejercicio privado o público de la profesión, a nivel nacional o en el extranjero." Art. 3: "Se exceptúan de este beneficio los asegurados del Régimen de Afiliación Especial y Progresiva, a quienes únicamente se les otorgará incapacidad temporal por reposo pre y post natal." | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 1 (pp.3-4/40); RIT-Art. 3 (p.10/40) (EV81:EVID-264) |
| LB-002 | RIT Art. 2 nums. 2.27, 2.28, 2.29, 2.44, 2.26/2.30/2.31 (definiciones) | 2.27 prenatal: "cuarenta y dos (42) días calendario incluyendo la fecha probable del parto… Este período finaliza con el parto"; 2.28 posnatal: "cuarenta y dos (42) días calendario, y que inicia en la fecha en que ocurre el parto"; 2.29 incapacidad temporal "hasta por un máximo de trescientos sesenta y cinco (365) días calendario"; 2.44 prórroga: same or related diagnosis "dentro de los treinta y cinco (35) días siguientes contados a partir de la fecha de finalización de la incapacidad temporal previa"; 2.26/2.30/2.31: retroactive/postdated special incapacity "no podrá exceder los sesenta (60) días calendario" | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 2.27-2.29 (pp.6-7/40); 2.44 (p.8/40); 2.26/2.30/2.31 (pp.7-8/40) (EV81:EVID-265) |
| LB-003 | RIT Arts. 27, 28, 31 (duración; alerta 273; reinicio) | Art. 28: "hasta por ciento ochenta y dos (182) días calendario que corresponderán al primer periodo de incapacidad temporal… Si al término de este primer periodo, persiste la incapacidad del asegurado, la jefatura o gerencia médica… designará una Comisión de Médicos Especialistas, quienes podrán autorizar un segundo periodo, hasta por ciento ochenta y tres (183) días calendario más para completar el año de incapacidad temporal." Art. 27: system alert "cuando el asegurado acumule un total de doscientos setenta y tres (273) días de incapacidad temporal"; "Los días generados por incapacidad prenatal o posnatal, no serán tomadas en cuenta para este cómputo." Art. 31 (CTI says no invalidez → reintegro): "se procederá para efecto de contabilización de los días de incapacidad a iniciar un nuevo periodo." | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 27 (pp.15-16/40); Art. 28 (p.16/40); Art. 31 (p.17/40) (EV81:EVID-266) |
| LB-004 | RIT Arts. 34, 35, 37, 45 (maternidad) | Art. 34: "abarcará cuarenta y dos (42) días de prenatal (incluyendo la fecha probable del parto) y cuarenta y dos (42) días de posnatal (a partir e inclusive la fecha del parto). Los días de reposo y/o condiciones especiales establecidas en los contratos individuales o colectivos de trabajo, en exceso de las que le concede el presente reglamento, serán por cuenta exclusiva del o los patronos de la asegurada." Art. 37 (late partum): "otro certificado de incapacidad temporal debidamente razonado, hasta por un máximo de catorce (14) días calendario". Art. 35: prenatal certificate "debe ser otorgado a partir de las veintiocho (28) semanas de gestación". Art. 45: subsidy when she proves "un mínimo de diez (10) meses cotizados previo a la fecha probable para el inicio del reposo prenatal, o un mínimo de doce (12) meses cotizados en los últimos dieciocho (18) meses, previos al inicio del reposo prenatal"; if unmet for prenatal → also unmet for posnatal (certificate still issues "sin derecho al pago de subsidio"). | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Arts. 34-35, 37 (p.18/40); Art. 45 (pp.19-20/40) (EV81:EVID-267) |
| LB-005 | RIT Arts. 54, 55, 58 (+38-39, 41) (refrendo y plazos) | Art. 54: incapacity "no mayor de tres (3) días calendario, tendrá validez por si misma ante el patrono y no necesita ser refrendada o ratificada por el Instituto". Art. 55: certs with reposo "mayor de tres (3) días calendario, deberán ser refrendadas por el médico evaluador refrendador quien generará el Certificado de Incapacidad Temporal a través del sistema informático". Art. 58.1 (private ambulatory): "dentro de los cinco (5) días hábiles siguientes a la fecha de la consulta… y cinco (5) días hábiles adicionales… para que pueda presentarlo ante su patrono, sin derecho al subsidio por incapacidad de parte del IHSS"; 58.2 (public ambulatory): 15 + 15 días hábiles; 58.3 (hospitalization): "dentro de los quince (15) días hábiles siguientes del egreso hospitalario" + 15; 58.4 (abroad): 20 + 15; prenatal (Art. 38): until 1 day before partum + 15; posnatal (Art. 39): 15 + 15; foreign birth (Art. 41): 30 + 30; late beyond grace → Instituto issues denial resolution. | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 54 (p.22/40); Art. 55 (p.23/40); Art. 58 (pp.24-25/40); Arts. 38-39 (pp.18-19/40) (EV81:EVID-268) |
| LB-006 | RIT Arts. 13, 17.1-17.2, 18, 71 ¶2-3 (deberes documentales del patrono) | Art. 13: certificates issued "en original por cada patrono, al momento de ser reclamada por el asegurado." Art. 17.1-17.2: "la copia de color rosado se entregará al paciente para que sea firmada y sellada por el patrono"; originals >3 days "se remitirá al área encargada del pago de subsidio". Art. 71 ¶2: the assured presents at the Sub Gerencia de Subsidios "la Tarjeta de Identidad y el certificado de incapacidad temporal con la información ya completada por el patrono. En caso de que la incapacidad se genere fuera del sistema… la copia rosada con la información requerida, debidamente firmada y sellada por el patrono." Art. 18: two-patrono accident: certificate for that patrono "será emitido como accidente de trabajo, y para el o los patronos restantes como accidente común (riesgo común)"; trayecto patrono-a-patrono → "la responsabilidad del riesgo será asumida por el patrono destino". | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 13 (p.12/40); Arts. 17-18 (pp.13-14/40); Art. 71 ¶2-3 (p.28/40) (EV81:EVID-269) |
| LB-007 | RIT Arts. 71-72 (reparto de costos; duplicados) | Art. 71: "El pago del salario del trabajador asegurado con incapacidad temporal, correspondiente a los primeros tres (3) días de incapacidad correrán por cuenta exclusiva del patrono del asegurado. El Instituto pagará el subsidio por incapacidad temporal a partir del cuarto (4to) día calendario, por todo el tiempo que dure la incapacidad, hasta el máximo de trescientos sesenta y cinco (365) días calendario." Art. 72: "El Instituto no realizará el pago de subsidio… por días duplicados o traslapados". | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 71 (p.28/40); Art. 72 (pp.28-29/40) (EV81:EVID-270) |
| LB-008 | RIT Art. 73 (fórmula del subsidio; complemento patronal) | "El Subsidio diario será igual al sesenta y seis por ciento (66%) del salario base mensual de referencia, de acuerdo al techo del Régimen que corresponda. El patrono pagará la diferencia hasta completar el salario total que devenga el trabajador." | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 73 (p.29/40) (EV81:EVID-271) |
| LB-009 | RIT Arts. 74-77, 80-81, 85 (derecho y matriz de no-pago) | Art. 80 (riesgo común): subsidy "siempre que acredite no menos de dos (2) meses de cotización en los cuatro (4) meses calendarios anteriores al mes en que se generó la incapacidad." Art. 81 (riesgo profesional): "sin necesidad de acreditar tiempo mínimo de cotización… Cuando el trabajador sufra un riesgo profesional sin encontrarse debidamente asegurado al IHSS por causas imputables al patrono, no tendrá derecho al pago de subsidio… y será responsabilidad del patrono el pago de su sueldo completo." Art. 75: no subsidy "cuando al momento de generarse el certificado de incapacidad temporal el patrono se encuentre en mora con sus obligaciones obrero-patronales, debiendo éste realizar el pago total del salario al asegurado". Art. 77: "El subsidio se concederá por día completo de incapacidad, con inclusión de sábados, domingos y feriados, y se liquidará por periodos vencidos no mayores de treinta (30) días, con excepción de los periodos pre y posnatal". Art. 76: the claim right "prescribe transcurrido un (1) año, contado a partir de la fecha de expedición del certificado". Art. 85: workers not assured/cotizing due to employer cause get "ni… certificado… ni… subsidio". | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Arts. 74-77 (pp.29-30/40); Arts. 80-81, 85 (pp.30-32/40) (EV81:EVID-272) |
| LB-010 | RIT Arts. 88, 106, 116, 118-119 (incompatibilidades; reposo; derogatoria; vigencia) | Art. 88: "El pago de subsidio por incapacidad temporal como consecuencia de enfermedad, maternidad o accidente, son incompatibles entre sí. Los subsidios por concepto de incapacidad temporal y descanso de maternidad (pre y posnatal) son incompatibles entre sí… El subsidio por incapacidad temporal es incompatible con el goce simultáneo de prestaciones económicas relacionadas con pensiones por vejez, invalidez (riesgo común) e incapacidad total permanente (riesgo profesional)". Art. 106: "El patrono está obligado a respetar el reposo indicado al asegurado." Art. 118: deroga el Reglamento aprobado por "Acuerdo Número 001-JD-2005… derogando además cualquier otra disposición reglamentaria que se oponga" (001-JD-2005 transitorily applicable to pre-vigencia procedures — Art. 116). Art. 119: "entrará en vigencia a los dos (2) meses calendario posterior a la fecha de su publicación" (G 35,267-B 29-may-2020 → 29-jul-2020); approved Res. CI IHSS-RSAS No. 213/10-04-2018, actualizada No. 1335/05-12-2019. | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 88 (pp.32-33/40); Art. 106 (pp.37-38/40); Arts. 116, 118-119 (p.40/40); aprobación (p.1/40) (EV81:EVID-273) |
| LB-011 | RIT Arts. 61, 82-83 (continuidad del caso) | Art. 82: "se entenderá como un mismo caso, la incapacidad temporal ininterrumpida para el trabajo, desde el día en que se origina la incapacidad hasta en que finaliza la misma. Si sobreviene una nueva incapacidad al asegurado, por un mismo diagnóstico o por diagnóstico relacionado a la primera situación incapacitante, dentro de los treinta y cinco (35) días siguientes a la finalización de la primera incapacidad, será considerada como prórroga del periodo anterior, para efecto de pago de subsidio. Toda incapacidad que se presente con posterioridad a los treinta y cinco (35) días señalados, será considerada como un nuevo caso, si el asegurado demuestra su capacidad para el trabajo mediante el reintegro a sus laborales habituales… Las incapacidades temporales interrumpidas por los asegurados, por periodos de vacaciones o licencias (remuneradas o no remuneradas), no serán considerados para el reinicio de un nuevo periodo de incapacidad temporal." Art. 83: if the first incapacidad earned no subsidio, "las prórrogas derivadas de esta incapacidad tampoco tendrán derecho al pago de subsidio". | `hn/sources/88_Reglamento_Incapacidad_Temporal_IHSS.pdf` | RIT-Art. 82 (pp.30-31/40); Art. 83 (p.31/40); Art. 61 (pp.26-27/40) (EV81:EVID-274) |
| LB-012 | Ley del Seguro Social (LI), Arts. 34.b, 39.b, 42.2 (delegación del subsidio; paridad RP) | Art. 34.b (enfermedad no profesional): "En caso de incapacidad laboral debidamente acreditada, a un subsidio en dinero cuyo monto duración y demás condiciones para su pago, serán fijadas por los Reglamentos". Art. 39.b (maternidad): "Un subsidio en dinero, siempre que la asegurada no efectúe trabajo alguno remunerado durante el tiempo que reciba dicho subsidio. Los reglamentos fijarán la fecha de iniciar el pago de este subsidio, así como su duración y monto." Art. 42.2 (riesgos profesionales): "Un subsidio diario cuando el riesgo profesional produzca al asegurado una incapacidad temporal para el trabajo, cuya cuantía será igual que en caso de enfermedad". | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 34.b (p.7/19); Art. 39.b (p.8/19); Art. 42.2 (p.8/19) (EV81:EVID-263) |
| LB-013 | LI Arts. 88 ¶2, 90, 91, 92 (mora; incompatibilidad; prescripción; no gravables) | Art. 88 ¶2: "En caso de los empleadores morosos por cotizaciones obrero patronales, todas las prestaciones previstas en la Ley y su Reglamento, serán asumidas directamente por éllos [ellos], sin responsabilidad alguna para el Instituto." Art. 90: "Los subsidios en dinero que se otorguen por enfermedad, maternidad o accidente, son incompatibles [entre sí]." Art. 91: "El derecho de reclamar un subsidio por incapacidad temporal o maternidad… prescribe al año, contando desde que se originó el derecho". Art. 92: prestaciones en dinero "no serán gravables por impuesto alguno". | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 88 ¶2 (pp.15-16/19); Arts. 90-92 (p.16/19) (EV81:EVID-261; EV81:EVID-263) |
| LB-014 | LI Art. 45 (riesgos profesionales: financiación exclusivamente patronal) | "Las Prestaciones del Seguro por Riesgos Profesionales, se financiarán exclusivamente con cargo a las cotizaciones de los empleadores, según lo determinen los Reglamentos… Podrá establecer cuotas técnicas especiales a cargo del empleador, tomando en cuenta la peligrosidad de cada actividad y la región…" | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 45 (p.9/19) (EV81:EVID-263) |
| LB-015 | D.48-2024 (81_), Art. 2 (techos 2024/2025 — INPUT consumido del archivo 03) | "Para los años 2024 y 2025 los techos de cotización serán los siguientes: — Régimen [De] Invalidez, [Vejez] y muerte (IVM) L. 11,336.32 | L. 11,903.13 — Régimen [De] Enfermedad y Maternidad (EM) L. 11,109.30 | L. 11,903.13. Para los años subsiguientes la Junta Directiva del [IHSS], con base a un estudio actuarial, deberá de fijar los techos de cotización…" — the dated techo rows are OWNED and published by file 03 (HN-PAYR-FR-101..135); this file only consumes them by id for the Art. 73 cap. | `hn/sources/81_Decreto_48-2024_IHSS_aportaciones.pdf` | D48-Art. 2 (p.3/4, G A.11) (EV81:EVID-252) |

## 3. Functional Requirements

### 3.1 Regime frame and certificate provenance

- **HN-PAYR-FR-141:** The system shall carry the RIT as a DATED regime row —
  `valid_from` 2020-07-29 (G 35,267-B of 29-may-2020 + the two-calendar-month
  post-publication vigencia of Art. 119), repealing Acuerdo 001-JD-2005
  (Art. 118) with the predecessor remaining transitorily applicable only to
  procedures initiated before vigencia (Art. 116) — and shall record the
  edition signature per R-H65 (aprobado Res. CI IHSS-RSAS No. 213/10-04-2018,
  actualizada Res. No. 1335/05-12-2019); episodes with certificate dates
  before 2020-07-29 resolve under the predecessor regime as historical
  configuration, never under RIT rows (D-H2: resolution by the hecho
  generador date, never "today"). (LB-010; EV81:EVID-273; R-H65)
- **HN-PAYR-FR-142:** The system shall model sick-leave evidence with TWO
  provenances per RIT Art. 1: (i) Certificados de Incapacidad Temporal issued
  by IHSS/SME/SILOSS medical and dental staff (system-generated), and (ii)
  *constancias* (certificates) issued by doctors/dentists in private or
  public practice, nationally or abroad, which carry subsidy eligibility ONLY
  after IHSS *refrendo* (validation) per the FR-158..160 workflow; and shall
  enforce the active-service-and-cotizing precondition on certificate
  validity (certificates only issue for workers in active service and
  contributing to the Institute). (LB-001; EV81:EVID-264)
- **HN-PAYR-FR-143:** The system shall flag workers of the *Régimen de
  Afiliación Especial y Progresiva* (Special and Progressive Affiliation
  regime) as maternity-only: their only incapacidad-temporal benefit is
  prenatal and postnatal rest; common-risk incapacidad certificates for such
  workers generate no subsidy surface and are flagged, never silently
  processed. (LB-001; EV81:EVID-264)

### 3.2 Episode and case semantics

- **HN-PAYR-FR-144:** The system shall index every episode in CALENDAR days
  running uninterruptedly through Saturdays, Sundays, holidays and vacations
  (RIT Art. 5: episodes run "por los días sábados, domingos, feriados o
  vacaciones"), with day 1 = the *fecha de inicio de la Incapacidad* = the
  consultation date that originated it (RIT def. 2.18), except approved
  retroactive/postdated certification which shall be capped at 60 días
  calendario — requests beyond 60 retro days are rejected with an explicit
  validation flag, never silently truncated. (LB-002; EV81:EVID-265;
  EV81:EVID-270)
- **HN-PAYR-FR-145:** The system shall group episodes into CASES by the
  35-day key (R-H54): a new incapacidad by the SAME diagnosis or a RELATED
  diagnosis to the first incapacitating condition, arising within 35 days of
  the end of the previous incapacidad, is a *prórroga* (extension) of the
  same case for subsidy-payment purposes (same day budget, same eligibility
  state); an incapacidad arising AFTER 35 days is a NEW CASE only if the
  worker demonstrates work capacity by actual reinstatement to habitual
  labors; and interruptions of the counting by *vacaciones* or *licencias*
  (leave, paid or unpaid) shall NEVER restart a new incapacidad period.
  (LB-011; EV81:EVID-274; R-H54)
- **HN-PAYR-FR-146:** The system shall charge the 3-day employer-paid salary
  wait ONCE PER CASE, never per certificate: prórrogas within the 35-day
  window do not restart the days 1-3 employer period (case-level reading of
  Art. 71 + Art. 82, the R-H54/88_ OQ-3 default), exposed as an explicit
  configuration toggle pending confirmation. (LB-007; LB-011; EV81:EVID-270;
  EV81:EVID-274; R-H54)
- **HN-PAYR-FR-147:** The system shall make subsidy ineligibility sticky
  across the case: when the first incapacidad earned no subsidy right
  (contribution qualifiers unmet), prórrogas derived from it carry no subsidy
  either (RIT Art. 83). (LB-011; EV81:EVID-274)
- **HN-PAYR-FR-148:** The system shall detect duplicated or overlapped days
  across concurrent certificates and generate no subsidy line for them
  ("El Instituto no realizará el pago de subsidio… por días duplicados o
  traslapados" — RIT Art. 72); overlaps surface as reconciliation flags on
  the affected episodes. (LB-007; EV81:EVID-270)
- **HN-PAYR-FR-149:** The system shall govern case duration as: 365 días
  calendario maximum per case, consumed as a 182-day FIRST period (ordinary
  medical extension) plus a 183-day SECOND period authorizable ONLY by a
  *Comisión de Médicos Especialistas* (specialist commission); a running
  alert when the worker accumulates 273 days of incapacidad temporal
  (reubicación/pension-review trigger), with prenatal and posnatal days
  EXCLUDED from that accumulated count; and a counter reset starting a new
  period when a CTI (calificación de invalidez) verdict of non-invalidez
  leads to reinstatement (RIT Art. 31). (LB-003; EV81:EVID-266)

### 3.3 The cost-split: employer salary days 1-3, IHSS 66% subsidy days 4-365, employer complement

- **HN-PAYR-FR-150:** The system shall split each case's cost so that the
  FIRST THREE DAYS are paid by the employer as FULL SALARY at the employer's
  exclusive cost ("correrán por cuenta exclusiva del patrono" — RIT Art. 71):
  these are employer-paid salary days, NOT an unpaid waiting period — no
  *cuarentena* exists in the Honduran regime (R-H52) — and no system surface
  may label or treat them as unpaid wait or subsidy days. (LB-007;
  EV81:EVID-270; R-H52)
- **HN-PAYR-FR-151:** The system shall compute, for days 4 through 365 of
  each case, the IHSS subsidy = 66% of the *salario base mensual de
  referencia* capped by the *techo del Régimen que corresponda* — the EM
  ceiling for common risk and maternity (dated techo rows consumed BY ID
  from file 03, HN-PAYR-FR-101..135: D48 Art. 2 rows IVM/EM 2024-2025, JD
  rows post-2025); for workplace risk the RP-regime ceiling applies and is
  external configuration (RP cotización/ceiling not in corpus — 87_ OQ-2
  family lead; never guessed, D-H2 never-guess rule).
  (LB-008; LB-015; LB-014; EV81:EVID-271; EV81:EVID-252)
- **HN-PAYR-FR-152:** The system shall compute the daily subsidy by DEFAULT
  as (salario base mensual de referencia ÷ 30) × 66% — the daily-derivative
  reading of RIT Art. 73's dimensionally sloppy text ("El Subsidio diario
  será igual al… 66% del salario base mensual de referencia"), per R-H53 —
  with the proration formula exposed as explicit configuration (÷30
  daily-derivative default; confirm against an IHSS subsidio worksheet
  before contest); and the *salario base mensual de referencia* itself —
  which month(s) it takes — is a configuration gap (88_ OQ-2, Reglamento
  General delegation family): NEVER derived, averaged or hardcoded (D-H2
  never-guess). (LB-008; EV81:EVID-271; R-H53)
- **HN-PAYR-FR-153:** The system shall pay the MANDATORY employer complement
  ("El patrono pagará la diferencia hasta completar el salario total que
  devenga el trabajador" — RIT Art. 73 ¶2): the payslip shows the worker's
  FULL salary with the IHSS subsidy as an offset, so the employer's net cost
  per case = 100% of salary for days 1-3 + (salary − capped-66% subsidy) for
  days 4-365, and employer-cost lines *días-1-3 salario* and *complemento*
  are reported per case. (LB-008; EV81:EVID-271)

### 3.4 Maternity subsidy

- **HN-PAYR-FR-154:** The system shall anchor maternity episodes to the
  médico-tratante's probable-partum date: 42 días calendario of prenatal rest
  INCLUDING the probable-partum date (the period ends at birth), plus 42 días
  calendario of postnatal rest from and including the actual birth date; and
  when birth occurs after the probable date, extend the prenatal rest by an
  expressly reasoned certificate up to a MAXIMUM of 14 additional días
  calendario. (LB-004; LB-002; EV81:EVID-267; EV81:EVID-265)
- **HN-PAYR-FR-155:** The system shall gate prenatal certificate emission at
  28 weeks of gestation ("debe ser otorgado a partir de las veintiocho (28)
  semanas de gestación") — earlier-dated prenatal certificates are flagged,
  not silently honored. (LB-004; EV81:EVID-267)
- **HN-PAYR-FR-156:** The system shall evaluate the maternity subsidy
  qualifiers as an entitlement gate on the IHSS cash: a minimum of 10 months
  cotizados prior to the probable start date of prenatal rest, OR a minimum
  of 12 months cotizados within the last 18 months prior to that start; if
  the qualifier is unmet for prenatal it is unmet for posnatal as well — the
  certificate still issues for retreat from work activities WITHOUT subsidy
  right, and the resulting employer-cost treatment rides the FR-160 funding
  toggle family (default: complement to full salary; OQ-005).
  (LB-004; EV81:EVID-267)
- **HN-PAYR-FR-157:** The system shall charge days of rest and/or special
  conditions granted by individual or collective labor contracts IN EXCESS of
  the reglamento's 42+42(+14) grant exclusively to the employer
  (contractual-maternity-excess cost line); and shall state the one
  reconciliation to the CT-side regime: the CT maternity rest mechanics
  (4+6-weeks frame, paid rest, employer top-up) are owned by file 09
  (HN-PAYR-FR-331..357, P11) and the IHSS 42+42 subsidy + the Art. 73 ¶2
  employer complement reconcile the two regimes — this file owns only the
  IHSS subsidy side and emits the reconciliation figures, never the CT-side
  computation. (LB-004; LB-008; EV81:EVID-267; EV81:EVID-263)

### 3.5 Refrendo workflow and deadline matrix

- **HN-PAYR-FR-158:** The system shall treat private/public-doctor
  certificates of duration ≤ 3 días calendario as valid by themselves before
  the employer — no IHSS refrendo or ratification needed (and no IHSS
  subsidy: employer-paid per FR-150) — while certificates indicating rest
  LONGER than 3 días calendario MUST be refrendada by the *médico evaluador
  refrendador*, who generates the Certificado de Incapacidad Temporal through
  the IHSS system, before any subsidy surface arises.
  (LB-005; EV81:EVID-268)
- **HN-PAYR-FR-159:** The system shall compute refrendo filing deadlines in
  DÍAS HÁBILES (business days) as a deadline matrix, each with an EQUAL
  additional grace window in which the certificate remains
  patrono-presentable (valid work excuse) WITHOUT IHSS subsidy: private
  ambulatory 5 + 5 from the consultation date; public ambulatory 15 + 15;
  hospitalization 15 from hospital discharge + 15; abroad 20 + 15; prenatal
  until 1 day before partum + 15; posnatal 15 + 15; foreign birth 30 + 30;
  filing beyond the grace window ends in the IHSS denial resolution — and
  the intake status model shall distinguish
  *refrendada-con-subsidio* / *presentable-sin-subsidio* / *denegada*.
  (LB-005; EV81:EVID-268)
- **HN-PAYR-FR-160:** The system shall fund grace-window days by DEFAULT
  through the employer complement (FR-153 applies to full salary), per 88_
  OQ-5's conservative default, with an EXPLICIT toggle — the corpus is
  silent on whether grace-window days are employer-complemented or unpaid
  under labor law, so no other default is derivable (D-H2 never-guess);
  the toggle also governs the qualifier-failure days of FR-156 (same
  configuration family). (LB-005; LB-008; EV81:EVID-268; EV81:EVID-271)
- **HN-PAYR-FR-161:** The system shall implement the employer-side document
  duties: certificates issued in ORIGINAL per patrono (one original per
  employer for multi-patrono workers); the *copia rosada* (pink copy)
  delivered to the worker for employer signature and stamp; the
  employer-completed certificate information required before the worker
  claims subsidy payment at the Sub Gerencia de Subsidios; and the
  multi-patrono risk split — a two-patrono accident is classified accidente
  de trabajo for the patrono where it occurred and riesgo común for the
  remaining patronos, with patrono-a-patrono transit risk assumed by the
  *patrono destino* (destination employer). (LB-006; EV81:EVID-269)

### 3.6 Entitlement, employer-full-cost triggers and payment rhythm

- **HN-PAYR-FR-162:** The system shall evaluate the common-risk subsidy
  qualifier: no less than 2 months of cotización in the 4 calendar months
  before the month the incapacidad arose (contribution months consumed from
  file 03's contributions ledger); failure → no IHSS subsidy, episode flagged
  subsidy-ineligible with the FR-160 funding-toggle family applied.
  (LB-009; EV81:EVID-272)
- **HN-PAYR-FR-163:** The system shall exempt profesional-risk
  (workplace-accident/illness) subsidy from ANY minimum cotización
  requirement — the subsidy right is immediate — the RP subsidy cuantía being
  equal to the illness subsidy (LI Art. 42.2) and RP prestaciones
  employer-exclusively financed (LI Art. 45, rate itself external — 87_ OQ-2
  family). (LB-009; LB-012; LB-014; EV81:EVID-272; EV81:EVID-263)
- **HN-PAYR-FR-164:** The system shall switch the full salary to the
  EMPLOYER when a profesional risk is suffered while the worker is not duly
  insured at IHSS for causes imputable to the patrono (no IHSS subsidy;
  employer pays the complete salary — RIT Art. 81 ¶2), and when the worker
  is not assured/cotizing due to employer cause gets neither certificate nor
  subsidy (RIT Art. 85) — employer-full-cost lines with cause flags, echoing
  LI Art. 88 ¶2 (moras assumunt omnia). (LB-009; LB-013; EV81:EVID-272;
  EV81:EVID-261)
- **HN-PAYR-FR-165:** The system shall switch the TOTAL salary to the
  employer when the patrono is in mora with obrero-patronal obligations at
  the moment the certificate is generated (RIT Art. 75: IHSS pays nothing;
  employer pays the full salary) — the mora flag is consumed from file 03's
  compliance surface; no IHSS subsidy line is emitted for such cases.
  (LB-009; LB-013; EV81:EVID-272; EV81:EVID-261)
- **HN-PAYR-FR-166:** The system shall grant the subsidy per FULL day of
  incapacity including Saturdays, Sundays and holidays, and liquidate it in
  VENCIDO periods not greater than 30 days, EXCEPT the prenatal and posnatal
  periods (RIT Art. 77); the ≤30-day tranche ledger is the per-episode
  payment schedule and is the export interface consumed by file 05
  (RAP/fondo, HN-PAYR-FR-181..215) for its own ≤30-day tranche computations
  — by id, no re-derivation. (LB-009; EV81:EVID-272)

### 3.7 Incompatibilities, prescription and fiscal interfaces

- **HN-PAYR-FR-167:** The system shall record the 1-year claim prescription
  from the certificate issuance date (RIT Art. 76) — with the statute's
  parallel anchor (LI Art. 91: from when the right originated) carried as
  metadata — as a claim deadline on every episode, after which subsidy
  claims are prescription-flagged. (LB-009; LB-013; EV81:EVID-272;
  EV81:EVID-263)
- **HN-PAYR-FR-168:** The system shall enforce the incompatibility engine
  (RIT Art. 88 + LI Art. 90): subsidies for illness, maternity and accident
  are mutually incompatible; incapacidad-temporal subsidies are incompatible
  with simultaneous pension economics — vejez, invalidez (riesgo común) and
  incapacidad total permanente (riesgo profesional); one cash benefit at a
  time, with the sequencing rule that a maternity incapacity starts the day
  after a running common-risk incapacity ends. (LB-010; LB-013;
  EV81:EVID-273; EV81:EVID-263)
- **HN-PAYR-FR-169:** The system shall record the employer's duty to RESPECT
  the medical reposo ("El patrono está obligado a respetar el reposo indicado
  al asegurado" — RIT Art. 106): reposo periods are leave-protected and
  cannot be countered, reassigned or offset by the employer in scheduling or
  payroll. (LB-010; EV81:EVID-273)
- **HN-PAYR-FR-170:** The system shall tag all IHSS cash subsidies and
  prestaciones en dinero of this file as ISR NON-GRAVABLE (LI Art. 92: "no
  serán gravables por impuesto alguno"; ISR Art. 10 exclusion semantics
  consumed by id from taxation/02, HN-TAX-FR-046..078; plantilla exclusion
  consumed from taxation/04, HN-TAX-FR-121..153) — payslip tagging only, no
  re-derivation of exclusion semantics here. (LB-013; LB-012; EV81:EVID-263)

## 4. Data Model

No CSV sidecar is allocated to this file (the dated techo rows consumed here
live in file 03's sidecar, HN-PAYR-FR-101..135; the RIT's own constants —
3/66%/35/182/183/365/273/42/14/60/30/1-year — are statute-printed constants
of LB-001..LB-015, encoded as regime-row metadata, not as replaceable dated
value series; only the techo input and the regime row itself are dated data).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.ihss.regime.rit (new) | valid_from, prior_regime, approval_refs, gaceta | date/char | valid_from 2020-07-29; predecessor acuerdo_001_jd_2005 transitory; Res. 213/10-04-2018 + 1335/05-12-2019; G 35,267-B 29-may-2020 | FR-141 |
| l10n_hn.ihss.certificado (new) | provenance, issuer_type, consult_date, issue_date, retro_days, risk_type, days, refrendo_status, filing_deadline, grace_deadline | select/date/int | provenance: ihss_sme_siloss · private · public · abroad; risk_type: comun · profesional · prenatal · posnatal; refrendo_status: not_required_le3 · refrendada_con_subsidio · presentable_sin_subsidio · denegada; deadlines in días hábiles per matrix | FR-142, FR-144, FR-158, FR-159 |
| l10n_hn.ihss.incapacidad.case (new) | case_key, worker, diagnosis_group, origin_date, end_date, is_maternity, accumulated_days_non_maternity, period_no, specialist_commission, cti_reset, prescription_deadline, subsidy_eligible | char/m2o/date/int/boolean | case_key = (worker, same/related diagnosis, 35-day window, reinstatement test); 273-day alert on accumulated_days_non_maternity (maternity excluded); prescription = issue + 1 year | FR-145..FR-149, FR-167 |
| l10n_hn.ihss.subsidio.line (new) | case, date, day_index, payer_bucket, base_monthly, techo_regime, techo_amount, formula_mode, daily_subsidy, employer_complement, tranche_no | m2o/date/monetary/select | payer_bucket: employer_days_1_3 · ihss_66 · employer_complement · employer_full_mora · employer_full_uninsured · employer_contractual_excess; formula_mode: daily_derivative (default, R-H53) · literal_monthly (config only); techo consumed by id from file 03 rows | FR-150..FR-153, FR-157, FR-160, FR-164..FR-166 |
| hr.payslip | ihss_it_salary_days_1_3, ihss_it_subsidy_offset, ihss_it_employer_complement, ihss_it_full_cost_flag | monetary (computed)/boolean | full-salary presentation with subsidy offset; cost-split trace per case | FR-150..FR-153 |
| hr.employee | ihss_special_regime (maternity-only), ihss_months_cotizados (evaluator feed from file 03 ledger), ihss_multi_patrono | boolean/int/boolean | special-regime carve-out; qualifier inputs (2-of-4, 10m / 12-of-18m); per-employer originals | FR-143, FR-156, FR-161, FR-162 |
| l10n_hn.ihss.config (new) | formula_mode, wait_per_case, grace_funding_mode, base_referencia_source | select | formula_mode=daily_derivative; wait_per_case=true (88_ OQ-3); grace_funding_mode=employer_complement (88_ OQ-5 toggle family); base_referencia_source = EMPTY pending Reglamento General (88_ OQ-2 — config gap, computation blocked, never guessed) | FR-146, FR-152, FR-160, FR-162 |
| account.move (employer-cost accrual) | ihss_it_cost_lines | monetary | días-1-3 salario + complemento + full-cost triggers booked as employer cost per period (D-H2 per-episode day-indexing) | FR-150, FR-153, FR-164, FR-165 |

## 5. Odoo Mapping

Layer semantics: `odoo` = computation/bookkeeping logic living in the LGPL
client. No SaaS rows: none of these FRs touch the thin-client/SaaS split
(payslip/leave computations and document workflow are client-side; no DTE
surface exists for IHSS certificates in the corpus). Model names stable
across Odoo 17/18/19/20; version-specific behavior recorded per row where a
dated parameter exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-141 | odoo | l10n_hn.ihss.regime.rit | dated regime row | Version regime (D12): valid_from 2020-07-29 (2 months post-publication); predecessor 001-JD-2005 transitory for pre-vigencia procedures; D15/D16: episodes resolve regime rows by certificate date; corrections recompute with ORIGINAL-period rows |
| FR-142, FR-158, FR-159 | odoo | l10n_hn.ihss.certificado + hr.leave (typed) | provenance/refrendo workflow | Intake status model; días hábiles deadline computation via the fiscal-calendar service; no native Odoo refrendo concept — new model |
| FR-143 | odoo | hr.employee | ihss_special_regime | Maternity-only enforcement flag on cert intake |
| FR-144..FR-149 | odoo | l10n_hn.ihss.incapacidad.case | episode engine | Case key (35-day/related-diagnosis/reinstatement), day counters, 182/183 period gates, 273 alert (maternity excluded), CTI reset, 60-day retro cap validation, overlap guard, eligibility inheritance |
| FR-150..FR-153 | odoo | hr.payslip × hr.salary.rule + l10n_hn.ihss.subsidio.line | cost-split rules | Days 1-3 salary rule; subsidy offset rule (66% techo-capped); complement rule to full salary; formula_mode config (R-H53 default base÷30×66%); techo lookup consumed by id from file 03 rows; snapshot-on-write of resolved techo/formula per line (D15) |
| FR-154..FR-157 | odoo | l10n_hn.ihss.certificado (maternity) + qualifier evaluator + hr.contract | maternity engine | 42+42 anchor to probable-partum date, +14 late birth, week-28 gate, 10m / 12-of-18m qualifiers (inputs from file 03 ledger), contractual-excess cost line; reconciliation figures emitted for file 09 crossref |
| FR-160 | odoo | l10n_hn.ihss.config | grace_funding_mode | 88_ OQ-5 toggle default employer_complement; same family for qualifier-failure days |
| FR-161 | odoo | l10n_hn.ihss.certificado + res.partner (patrono) | document duties | Per-patrono originals, copia rosada sign/stamp task, employer data-completion gate, multi-patrono risk split (AT vs común; patrono destino) |
| FR-162..FR-167 | odoo | evaluator + flags on case/subsidio.line | entitlement matrix | 2-of-4 común qualifier; profesional none; mora/uninsured full-salary switches (mora flag from file 03 compliance); ≤30-day tranches (maternity excepted) exported to file 05 by id; 1-year prescription metadata |
| FR-168..FR-170 | odoo | constraint validators + payslip tagging | interfaces | Incompatibility pairs (IT↔IT, IT↔maternity, IT↔pensions); reposo protection flag; ihss_non_gravable tag consumed by taxation/02+04 by id |

Version-regime notes (D12): FR-141 records the RIT regime row (2020-07-29)
and the transitory predecessor. FR-151 records the techo-input dependency:
D48 Art. 2 rows (valid_from 2024-05-28 for 2024; 2025-01-01 for 2025;
post-2025 = JD actuarial rows — acquisition/override path owned by file 03);
RP-side techo = external config (87_ OQ-2 family). D15/D16: every subsidy
line snapshots the resolved techo, formula mode and regime row at write time;
retro corrections recompute with original-period rows; filed periods are
write-protected. D18/D19: no mid-year go-live or cut-over surface is owned
here beyond the generic payroll ingestion depths (D-H3 does not apply — this
file owns no hire-date/FY-start aggregate accrual; the fondo/vacaciones
accrual consequences of leave days belong to files 05/07 by range).

## 6. Acceptance Criteria

- **AC-001:** Given a certificate dated (consult) 2026-03-10 for 10 days,
  then day 1 = 2026-03-10, days 2026-03-10..12 (1-3) are employer-paid FULL
  SALARY lines, and days 2026-03-13..19 (4-10) carry IHSS subsidy +
  employer complement; no day is unpaid wait (FR-144, FR-150).
- **AC-002:** Given a salario base mensual de referencia of L12,000.00 and
  the EM techo 2025 row L11,903.13 (consumed from file 03), then the capped
  base = L11,903.13 and the daily subsidy = 11,903.13 ÷ 30 × 66% =
  L261.87 (FR-151, FR-152).
- **AC-003:** Given the same worker's full monthly salary L12,000.00
  (daily L400.00), then the employer complement = 400.00 − 261.87 =
  L138.13/day for days 4-365, and days 1-3 bear L400.00/day; the payslip
  shows full salary L400.00/day throughout with the subsidy offset
  (FR-150, FR-153).
- **AC-004:** Given a reference base of L9,000.00 (below every techo row),
  then no capping applies and the daily subsidy = 9,000 ÷ 30 × 66% =
  L198.00 (FR-151, FR-152).
- **AC-005:** Given case A ending 2026-04-10 and a same-diagnosis
  certificate on 2026-05-05 (25 days later), then the engine groups it as a
  prórroga of case A: NO new 3-day employer wait, the 365-day budget
  continues, and eligibility state is inherited; given instead a
  certificate on day 40 after end WITH documented reinstatement to habitual
  labors, then a NEW case opens with fresh days 1-3; given an interruption
  filled by vacaciones, then the period never restarts (FR-145, FR-146,
  FR-147).
- **AC-006:** Given a worker with 250 accumulated non-maternity incapacidad
  days plus a completed 84-day maternity episode, then the 273-day counter
  reads 250 (maternity excluded); when the counter reaches 273, the alert
  fires (FR-149, FR-154).
- **AC-007:** Given a probable-partum date of 2026-06-15, then prenatal runs
  2026-05-05..2026-06-15 (42 days including the probable date) and postnatal
  2026-06-15..2026-07-26 (42 days from and including birth); given actual
  birth 2026-06-21 (6 days late), then the prenatal extends 6 days (≤14 cap)
  ending at birth and postnatal runs 2026-06-21..2026-08-01 (FR-154).
- **AC-008:** Given a pregnant worker with 9 months cotizados and 11 of the
  last 18 months, then both qualifiers fail (unmet prenatal → unmet
  posnatal), no IHSS subsidy line is generated, the certificate still
  records the rest, and the payslip surfaces the funding-mode config
  (default: employer complement to full salary) (FR-156, FR-160).
- **AC-009:** Given a private ambulatory certificate consulted Monday
  2026-03-02 for 6 days (>3 → refrendo required), then the subsidy deadline
  = 5 días hábiles → 2026-03-09 and the grace deadline = +5 días hábiles →
  2026-03-16; filed 2026-03-11 → status presentable-sin-subsidio with the
  employer-complement default applied; filed 2026-03-20 → denegada
  (FR-158, FR-159, FR-160).
- **AC-010:** Given the employer in mora at the certificate date, then no
  IHSS subsidy line is emitted and the TOTAL salary is booked as
  employer-full-cost with cause=mora; given a profesional risk while
  uninsured due to employer fault, then likewise full salary on the employer
  with cause=uninsured (FR-164, FR-165).
- **AC-011:** Given a común-risk certificate with only 1 cotización month in
  the prior 4 calendar months, then no subsidy line and the episode is
  flagged subsidy-ineligible; given a profesional-risk certificate with ZERO
  cotización months, then the subsidy right is immediate (FR-162, FR-163).
- **AC-012:** Given two certificates whose day ranges overlap on
  2026-05-10..12, then those days pay one subsidy at most (dedup flag on the
  second case) (FR-148).
- **AC-013:** Given a first period exhausted at 182 days, then further
  subsidy days require the specialist-commission flag for the 183-day second
  period; given day 366 of a case, then no subsidy line is emitted
  (FR-149).
- **AC-014:** Given a certificate issued 2026-02-01, then the claim
  prescription deadline = 2027-02-01 recorded on the episode (RIT Art. 76
  operative anchor; LI Art. 91 parallel anchor as metadata) (FR-167).
- **AC-015:** Given a two-patrono worker's accident at employer A, then the
  certificate for A classifies accidente de trabajo and for B riesgo común;
  a patrono-a-patrono transit event assigns risk to the patrono destino
  (FR-161).
- **AC-016:** Given a retro-dated certificate request of 70 days, then
  intake is rejected with the 60-day-cap flag, never truncated to 60
  (FR-144).
- **AC-017:** Given a running old-age pension and a concurrent sickness
  episode, then the incompatibility validator blocks simultaneous cash
  benefits (one at a time) and sequences maternity to start the day after a
  running common-risk incapacity ends (FR-168).
- **AC-018:** Given any subsidy line of this file on a payslip, then it is
  tagged ihss_non_gravable and excluded from the ISR base by the taxation/02
  + taxation/04 engines consuming the tag by id (FR-170).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Dimensional formula default (EV81:88_ OQ-1): RIT Art. 73 reads "subsidio diario = 66% del salario base mensual" — daily vs monthly sloppiness. FR-152 implements the daily-derivative default (base ÷ 30 × 66%) as configurable formula per R-H53; confirm against an IHSS subsidio worksheet/planilla before freezing. | no | Takumi S-HN4 + controller | open |
| OQ-002 | Salario base mensual de referencia definition (EV81:88_ OQ-2): which month(s) the reference takes (last cotizada month? average?) is undefined — same delegation family as LI Art. 100 / 87_ OQ-1 (Reglamento General, top acquisition lead). FR-152 leaves base_referencia_source as a config gap; computations block rather than guess. | no | acquisition queue | open |
| OQ-003 | Prórroga vs the 3-day employer wait (EV81:88_ OQ-3): Art. 71 never says the wait restarts for prórrogas within the 35-day window. FR-146 charges the wait once per CASE (R-H54 default), exposed as a toggle; confirm with IHSS practice. | no | Takumi S-HN4 | open |
| OQ-004 | Cotizabilidad of the subsidio (EV81:88_ OQ-4): whether IHSS subsidy days/amounts are themselves part of the cotizable salario during leave months is nowhere stated; affects file 03 base computation. Likely answered by the Reglamento General (87_ OQ-1 acquisition). | no | acquisition queue + file 03 | open |
| OQ-005 | Grace-window days funding (EV81:88_ OQ-5): when refrendo is filed only within the additional window the leave is justified but IHSS pays nothing; whether the employer then owes the Art. 73 ¶2 complement or the days go unpaid per labor law is unresolved by the corpus. FR-160 defaults to employer-complement with an explicit toggle; the same family governs qualifier-failure days (FR-156). | no | Takumi S-HN4 + controller | open |
