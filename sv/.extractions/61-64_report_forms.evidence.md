# Evidence — 61_F910v9 + 62_F915v4 + 63_F930v3 + 64_F935v1 (W8 addendum: related report forms)

Sources: the four report forms acquired 2026-08-18 from the MH formularios page after the W8 calendar read flagged them (30_/EVID-185). One page each; text layer clean.
Read: 2026-08-18 (W8 addendum).
Citation form: section of each form.

## EVID-187 F-910 v9 — Informe Anual de Retención del ISR (CT 123 annual report)

- **Loc:** 61_ §A-§C.
- **Verbatim:** §C row structure: "CÓDIGO INGRESO / MONTO DEVENGADO / MONTO DEVENGADO ANUAL POR BONIFICACIONES Y GRATIFICACIONES / IMPUESTO RETENIDO / Aguinaldo (Aplica solo para código 01 y 60) Exento Gravado / ISSS ANUAL / AFP ANUAL / IPSFA ANUAL / CEFAFA ANUAL / INPEP ANUAL / BIENESTAR MAGISTERIAL ANUAL" with SUMAS TOTALES. Payroll rule: "Los ingresos en concepto de Servicios de carácter permanente con subordinación o dependencia laboral, deben ser reportados en su totalidad en los códigos 01 ó 60 ... 1. En el código 01, si se le retuvo en al menos un mes del ejercicio fiscal. 2. En el código 60, si no se le retuvo en todo el ejercicio fiscal". §C header: "Datos del Contribuyente a quienes se les pagaron ingresos sujetos a retención, sin retención o no gravados" + the same acreditable/definitiva income-code catalog as the F-14 apéndice (35_).
- **Gloss:** the ANNUAL per-contribuyente consolidation of the F-14 monthly annexes: identical column set plus ANNUAL SS aggregates; the 01-vs-60 classification rule (retained-at-least-once → 01; never-retained → 60) is an annual-row derivation Odoo can compute from the 12 monthly rows. This is the electronic-reporting surface 04 OQ-007/MOQ-10 hunted for ISR retentions (due February per 30_).
- **Candidate CRs:** F-910 row builder = annual GROUP BY contribuyente over F-14 annex rows (code 01/60 rule; aguinaldo + SS annual sums); folio-modifica support.
- **Topics:** fiscal-reporting, taxation (04 OQ-007 answer).
- **Doubts/xref:** none.

## EVID-188 F-915 v4 — Informe de Distribución o Capitalización de Utilidades

- **Loc:** 62_ §A-§C.
- **Verbatim:** §A: "01 EJERCICIO FISCAL / 02 FOLIO MODIFICA / 03 NIT / 11 DISTRIBUYÓ [checkbox] ACTA JUNTA GENERAL DE ACCIONISTAS 04 Fecha 05 Número / CAPITALIZÓ [checkbox]". §B "Calidad de Socios × Cantidad / Monto de Utilidades, Dividendos o Excedentes Distribuidos / Valor Contable de las Acciones, Aportes, Participaciones Sociales o Derechos Capitalizados": rows "Socio, Accionista o Cooperado que adquirió la calidad con anterioridad al ejercicio que informa / ... durante el ejercicio que informa / ... que ha perdido la calidad durante el ejercicio que informa" + TOTAL. §C: "N° / No Domiciliado / NIT / ..." per-socio rows. Juramento cites CT 241 + CP 249-A.
- **Gloss:** the annual distributions report = the published reporting format behind Ley ISR Art. 74/74-C (taxation/05: FR-132..149 + `l10n_sv.isr.earnings.register`): DISTRIBUYÓ/CAPITALIZÓ modes with acta linkage, socio-quality transitions (antes/durante/perdió) × amounts × book values, per-socio detail incl. non-domiciled flag. Partially answers 05 §7 OQ-002's "DGII administrative norms" — the FORMAT exists (this form); norms-resolution still absent.
- **Candidate CRs:** F-915 builder from the earnings register: quality-transition classification per socio per ejercicio, acta data, book-value columns; CAPITALIZÓ path (no retention but informable).
- **Topics:** fiscal-reporting, taxation (05 interface).
- **Doubts/xref:** 62_ v4 is the 2017 form (page dated 2017-11-22; MH list shows no newer) — the 2026 calendar still names F-915; format assumed current.

## EVID-189 F-930 v3 — Informe Mensual de Retención/Percepción/Anticipo IVA

- **Loc:** 63_ §A-§C + codificación.
- **Verbatim:** §B "DOCUMENTOS × TOTAL DE DOCUMENTOS / MONTO SUJETO / MONTO DE LA RETENCIÓN, PERCEPCIÓN O ANTICIPO A CUENTA": "1. Comprobante de Crédito Fiscal / 2. Documento Contable de Liquidación / 3. Comprobante de Retención / 4. Nota de Débito / 5. Nota de Crédito / 6. Factura / 7. Documento Emitido por Sujeto Excluido". §C per-contribuyente rows: "Correl / NIT / Apellidos y Nombres, Razón Social o Denominación / Calidad en que Actúa / Modalidad / Código / DATOS DOCUMENTOS RECIBIDOS: Fecha / Serie / Número / Monto Sujeto / Monto Retención, Percepción o Anticipo IVA". Codificación includes "CALIDAD EN LA QUE ACTÚA" (agente/perceptor categories).
- **Gloss:** the standalone monthly IVA-retention report (separate from the F-07 declaration): document-typed summary + per-contribuyente detail with calidad/modality codes. Data source identical to F-07 annexes 9-12 (retenciones/percepciones/anticipos por el declarante) — Odoo builds both views from one retention-ledger model.
- **Candidate CRs:** F-930 view over the same IVA-retention ledger (document-type summary + calidad/modalidad classifiers).
- **Topics:** fiscal-reporting, taxation (IVA retentions).
- **Doubts/xref:** 63_ v3 2017-era form — currency/current-codes assumption as F-915.

## EVID-190 F-935 v1 — Informe Mensual de Retención sobre Agentes Extranjeros

- **Loc:** 64_ §A-§C.
- **Verbatim:** §A: "PERIODO TRIBUTARIO / FOLIO MODIFICA / NIT/DUI". §B "CONCEPTO × TOTAL DE REGISTROS / MONTO SUJETO / MONTO DE RETENCION": "RETENCION DE IMPUESTO / ENTERO DE IMPUESTO / TOTAL". §C "Datos de impuesto retencion / donantes locales": rows "N / NIT/NIF / Apellidos y nombres Razon social o denominación / DATOS DE TRANSFERENCIA: CONCEPTO / FECHA / NÚMERO DE TRANSACCIÓN / PAIS DE ORIGEN / MONTO SUJETO / MONTO RETENCION/ENTERO".
- **Gloss:** the agentes-extranjeros monthly inform (created 2025 per the Oct-2025 page date) = the transaction-level counterpart of F-14's Agentes Extranjeros tab (701-780 retención / 751-780 entero blocks): transfer-level rows (transaction number + country of origin) split RETENCIÓN vs ENTERO — matching the F-14 form's two sections (88-94 retención; 93-98 entero donantes locales).
- **Candidate CRs:** F-935 view over the foreign-agent retention ledger; donantes-locales entero track.
- **Topics:** fiscal-reporting, taxation (non-domiciled matrix pointer).
- **Doubts/xref:** "donantes locales" wording ties the entero block to donor-side payments — CT anchor to verify at synthesis (CT 156 zone or specific agreement regime).

## Open questions (61_-64_ addendum)

- OQ-1: F-910 v9 (2021 print) vs the D.E. 10-2025 tables interplay: the F-910 row set has no June/December recálculo notion (annual consolidation only) — no conflict, but confirm no v10 pending (MH list showed v9 current as of 2026-08-18).
- OQ-2: F-915 v4 / F-930 v3 are 2017-era prints still listed by MH (2026-08-18) — assume current; re-check at synthesis if a calendar year rolls.
- OQ-3: F-935's "donantes locales" entero track: normative anchor (which CT article / regime) unstated in the form — chase in the CT matrix during S3 synthesis.
