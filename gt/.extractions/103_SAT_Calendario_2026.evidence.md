# Evidence — 103_ SAT Calendario Mensual Tributario, Enero–Agosto 2026 (8 monthly PDFs, text layers; W-GT8 deadline-practice unit)

Source: 8 app-printed PDFs (`103_SAT_Calendario_2026-01.pdf` … `-08.pdf`), text extractions `103_SAT_Calendario_2026-01.pdf.txt` … `-08.pdf.txt` in `gt/.extractions/`. Read: 2026-08-23, end-to-end each. Shorthand below: `103_-01` = Enero file … `103_-08` = Agosto file; page cites are the PDF's own "Página X de Y".

**Extraction-method notes (this file only):**
- Every file is a print of SAT's **"Calendario Mensual Tributario"** web app (header block "Calendario Mensual Tributario / [Mes] 2026"; table columns "Fecha Vencimiento / Nombre Impuesto Concepto / Asiste Web / Declaraguate"). Each page footer carries the print timestamp: all 8 generated **23/08/2026 between 00:26:16 and 00:27:58** (one capture session; owner-generated, registry 103_).
- Every page of every file carries an identical "Nota Importante" footer (35 pages total: 5+4+5+5+3+4+5+4). Byte-identical across all 8 files (verified); quoted once at EVID-1093/1094. The footer's resolution is dated 10-Aug-2026 yet appears in the Enero–Julio prints too — an artifact of the 23-Aug-2026 generation date (EVID-1094).
- Form-code column ambiguity: the text layer collapses the two code columns; rows printing a lone code (e.g. `2237`) cannot be attributed to Asiste Web vs Declaraguate from this extraction; rows printing `----- 5100`, `1111 -------` or `541 Agencia Virtual` are unambiguous. Lone codes reported without column attribution (OQ-7).
- Text-layer double spaces and line wraps reproduced as printed; `[sic]` only where load-bearing. No OCR defects detected (clean text layers).

**Identity verdicts (from the prints themselves):**
- `103_-01`..`103_-08` = CONFIRMED SAT Calendario Mensual Tributario for Enero–Agosto 2026 respectively (each file's own header; generation timestamps above). No DCA/legal-document identity involved: this unit is administrative practice evidence (deadline tables), not normative text.

---

## EVID-1092 — Unit identity, provenance and row-count inventory of the 8 monthly calendars
- **Loc:** all 8 files, p.1 headers + per-page footers; row counts verified per file
- **Verbatim:** (header, each file p.1) "Calendario Mensual Tributario / Enero 2026" ["Febrero"…"Agosto" respectively] / (footer, every page) "Página 1 de 5, 23/08/2026 00:27:58" [times 00:26:16–00:27:58 across the set] / (column header) "Fecha Vencimiento Nombre Impuesto Concepto Asiste Web Declaraguate"
- **Gloss:** 8 monthly prints, 3–5 pages each, generated in one 102-second session on 23-Aug-2026. Vencimiento-row counts: Enero 30 rows (incl. 4 duplicate constancia rows), Febrero 25, Marzo 28, Abril 29, Mayo 20, Junio 25, Julio 31, Agosto 25. Obligation families present: petróleo (weekly/monthly/annual), IVA general, IVA pequeño 5%, IVA facturas especiales, IVA retenciones (2 kinds), cable, timbre-protocolo retenciones, ISR monthly family (6 rows), ISO quarterly, ISR trimestral/semestral/anual, specific consumptions (tabaco, cemento, bebidas, imprentas), vehículos anuales, ICT (Jul/Ago only). Legal-basis cites printed per row in full Decreto/Acuerdo + artículo form.
- **Candidate CRs:** none (provenance)
- **Topics:** SAT calendar; provenance; deadline practice
- **Doubts/xref:** OQ-1 (Sep–Dic 2026 not captured)

## EVID-1093 — Recurring "Nota Importante" footer, part 1: the Código Tributario art. 8.2 inhábil boilerplate (verbatim, all 35 pages)
- **Loc:** every page of `103_-01`..`103_-08` (35 occurrences, byte-identical)
- **Verbatim:** "Nota Importante: De conformidad con lo establecido en el Artículo 8, numeral 2 del Código Tributario, Decreto Número 6-91, se consideran inhábiles tanto los días declarados o que se declaren feriados legalmente, como aquellos en los que la Administración Tributaria no haya prestado servicio al público por cualquier causa, debiendo llevarse un registro riguroso de ello."
- **Gloss:** Standing inhábil doctrine printed on every calendar page: statutory feriados + any day SAT does not serve the public (any cause) = inhábil for plazo computation. This is SAT's own framing of CT D-6-91 art. 8.2 — the rule any Odoo deadline engine for GT must apply on top of every date in this file.
- **Candidate CRs:** guard CR: all SAT deadline dates are subject to CT art. 8.2 inhábil displacement (feriados + SAT non-service days, registro-based) — never model a fixed date without an inhábil-roll rule (LB: D-6-91 art. 8.2 as printed by SAT)
- **Topics:** inhábiles; deadline computation; Código Tributario
- **Doubts/xref:** xref EVID-1094

## EVID-1094 — Inhábil rulings: THE ONLY ruling text in the set — Res. SAT-DSI-1328-2026 (14-ago-2026 inhábil, 3 municipalities); count = 1 distinct ruling, repeated 35×
- **Loc:** every page of `103_-01`..`103_-08` (same footer block as EVID-1093, second sentence)
- **Verbatim:** "Conforme a la Resolución SAT-DSI-1328-2026 de fecha 10 de agosto de 2026, se otorga permiso laboral con goce de salario al personal de la SAT el día 14 de agosto de 2026. Por lo tanto, para el cómputo de plazos tributarios, aduaneros y administrativos, dicho día debe considerarse inhábil para el municipio de Guatemala, Departamento de Guatemala, municipio de Chiquimula, Departamento de Chiquimula y municipio de Sololá, Departamento de Sololá."
- **Gloss:** **Inhábil-ruling inventory verdict: exactly ONE distinct ruling text appears anywhere in the 8 months** — Res. **SAT-DSI-1328-2026** (dated 10-ago-2026), declaring **14-ago-2026** inhábil **only for three named municipalities** (Guatemala/Guatemala, Chiquimula/Chiquimula, Sololá/Sololá) because SAT staff there got paid leave. Two structural facts: (a) **per-locality scoping** — the inhábil is municipality-specific, not national (a same-date deadline can be inhábil in Guatemala city and hábil elsewhere); (b) the identical footer is stamped on ALL months' pages including Enero–Julio — an artifact of the 23-Aug-2026 generation (a resolution dated 10-Aug-2026 cannot have informed the January print as originally published); **no feriado-specific rulings, no SAT-closure notes, and no other inhábil paragraphs exist anywhere in the set** (full-text search: "Resolución" occurs only in this footer; "feriado"/"inhábil" only in the EVID-1093/1094 boilerplate).
- **Candidate CRs:** guard CR: 14-ago-2026 = inhábil for plazos tributarios/aduaneros/administrativos in municipios Guatemala, Chiquimula, Sololá only (LB: Res. SAT-DSI-1328-2026 as printed); localize inhábil rolls by municipality, not nationally
- **Topics:** inhábiles; per-locality scoping; SAT resolution
- **Doubts/xref:** OQ-6 (resolution instrument itself not in corpus)

## EVID-1095 — THE KEY STRUCTURAL QUESTION, verdict: FLAT — every monthly obligation prints exactly ONE date per period; NO staggered dates, NO NIT-digit/group language anywhere
- **Loc:** `103_-01` p.1; `103_-02` p.1; `103_-03` pp.1, 4; `103_-04` p.4; `103_-05` (absent); `103_-06` pp.1, 4; `103_-07` p.4; `103_-08` p.4 — full IVA-general row set
- **Verbatim:** (complete art. 40 row inventory, as printed — "Fecha / período 'Durante'":) Enero file: "05/01/2026 … Durante Noviembre de 2025"; Febrero file: "02/02/2026 … Durante Diciembre de 2025"; Marzo file: "02/03/2026 … Durante Enero de 2026" AND "31/03/2026 … Durante Febrero de 2026"; Abril file: "30/04/2026 … Durante Marzo de 2026"; Mayo file: **no art. 40 row printed**; Junio file: "01/06/2026 … Durante Abril de 2026" AND "30/06/2026 … Durante Mayo de 2026"; Julio file: "31/07/2026 … Durante Junio de 2026"; Agosto file: "31/08/2026 … Durante Julio de 2026". Full-text search across all 8 files for "NIT", "dígito"/"digito", "grupo", taxpayer-class qualifiers: **zero hits**.
- **Gloss:** **VERDICT (mission item): SAT's 2026 calendars print FLAT deadlines — one single date per obligation per period, applicable to all taxpayers alike; no trace of the historic NIT-digit stagger exists in any of the 8 months.** The only months showing two art. 40 rows (Marzo: 02/03 + 31/03; Junio: 01/06 + 30/06) are two DIFFERENT periods whose flat deadlines happen to fall in the same calendar month — each row still covers one period at one date with no taxpayer-group qualifier. Same flat structure holds for IVA pequeño art. 48 (EVID-1097), facturas especiales art. 54 (EVID-1098) and ISR retenciones arts. 16 y 48 (EVID-1100): always exactly one date per period, never 05/06/07-style date ladders. Reported as printed; no editorializing.
- **Candidate CRs:** guard CR: 2026 GT monthly deadlines are FLAT single dates per obligation+period (no NIT-digit windowing) — model one deadline per obligation-period, never a digit-keyed date ladder (LB: SAT Calendario Mensual Tributario Ene–Ago 2026, as printed; cf. owner-verified note EVID-1115)
- **Topics:** deadline structure; flat vs stagger; IVA
- **Doubts/xref:** xref EVID-1096, EVID-1113, EVID-1115

## EVID-1096 — IVA general art. 40, full row text verbatim from TWO different months (Enero and Agosto)
- **Loc:** `103_-01` p.1 (first data row); `103_-08` p.4
- **Verbatim:** Enero: "05/01/2026 Al Valor Agregado (Operaciones afectas y exentas). Declaración jurada y recibo de pago mensual del Impuesto al Valor Agregado, para contribuyentes que realizan operaciones afectas a este impuesto, incluyendo las exentas (locales y de exportación). Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 40. Durante Noviembre de 2025 2237" — Agosto: "31/08/2026 Al Valor Agregado (Operaciones afectas y exentas). Declaración jurada y recibo de pago mensual del Impuesto al Valor Agregado, para contribuyentes que realizan operaciones afectas a este impuesto, incluyendo las exentas (locales y de exportación). Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 40. Durante Julio de 2026 2237"
- **Gloss:** The two verbatim rows required by the mission. Text is identical month-to-month except date + period ("Durante [mes]"), plus the lone form code 2237. **No "último dígito", no taxpayer-group, no qualifier of any kind beyond the period reference** — the row addresses "contribuyentes que realizan operaciones afectas a este impuesto" as a single class. This is the printed basis for the flat-deadline verdict (EVID-1095).
- **Candidate CRs:** workflow CR: IVA general mensual (D-27-92 art. 40, form 2237) — one flat SAT-published date per monthly period (LB: D-27-92 art. 40; deadline practice per `103_`)
- **Topics:** IVA; deadlines; verbatim anchor
- **Doubts/xref:** xref EVID-1095

## EVID-1097 — IVA pequeño contribuyente 5% (D-27-92 art. 48, form 2046): flat rows, same dates as IVA general every month
- **Loc:** `103_-01` p.1; `103_-02` p.1; `103_-03` pp.1, 4; `103_-04` p.4; `103_-05` (absent); `103_-06` pp.1, 4; `103_-07` p.4; `103_-08` p.4
- **Verbatim:** (Enero, p.1) "05/01/2026 Al Valor Agregado (Régimen de Pequeño Contribuyente) Declaración jurada y pago mensual del pequeño contribuyente cuota fija del 5%. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 48. Correspondiente al mes de Noviembre de 2025 2046" / (Agosto, p.4) "31/08/2026 Al Valor Agregado (Régimen de Pequeño Contribuyente) Declaración jurada y pago mensual del pequeño contribuyente cuota fija del 5%. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 48. Correspondiente al mes de Julio de 2026 2046"
- **Gloss:** Pequeño contribuyente 5% cuota fija: **10 period-rows across the 8 files, each exactly one flat date, always the SAME date as that period's IVA general row** (05/01, 02/02, 02/03, 31/03, 30/04, —, 01/06, 30/06, 31/07, 31/08; periods Nov-25…Jul-26; absent from the Mayo file like the whole IVA trio). Qualifier is "Correspondiente al mes de…" (not "Durante") — no group/digit language. Historic note for the registry: art. 48's statutory window is a single legal deadline; SAT prints it flat for all pequeños.
- **Candidate CRs:** workflow CR: IVA pequeño 5% mensual (D-27-92 art. 48, form 2046) — flat date, same date as IVA general (LB: D-27-92 art. 48; deadline practice per `103_`)
- **Topics:** IVA; pequeño contribuyente; deadlines
- **Doubts/xref:** xref EVID-1095, EVID-1113

## EVID-1098 — IVA retenciones en facturas especiales 12% (D-27-92 **art. 54**, form 2085) — NOT D-7-2019 54"A"-"F"; flat rows
- **Loc:** `103_-01` p.1; `103_-02` p.1; `103_-03` pp.1, 4; `103_-04` p.4; `103_-05` (absent); `103_-06` pp.1, 4; `103_-07` p.4; `103_-08` p.4
- **Verbatim:** (Enero, p.1) "05/01/2026 Al Valor Agregado (Retenciones en facturas especiales) Pago mensual de retenciones del 12%, sobre el monto de facturas especiales emitidas. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 54. emitidas durante Noviembre de 2025. 2085" [sic — lowercase "emitidas" after the artículo cite, as printed] / (Agosto, p.4) "31/08/2026 Al Valor Agregado (Retenciones en facturas especiales) Pago mensual de retenciones del 12%, sobre el monto de facturas especiales emitidas. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 54. emitidas durante Julio de 2026. 2085"
- **Gloss:** The 12% retention on facturas especiales: D-**27-92** art. 54, form 2085, same 10 flat dates as art. 40/48 each month. **This is the only "artículo 54" in the entire set — the RECA/electrónico 4% regime of D-7-2019 arts. 54 "A"-"F" never appears (EVID-1112)**, consistent with its 2025-08-09 derogation by D-31-2024 art. 25 (registry cross-ref; not printed in this unit).
- **Candidate CRs:** workflow CR: IVA retenciones facturas especiales 12% mensual (D-27-92 art. 54, form 2085) — flat date, same as IVA general (LB: D-27-92 art. 54)
- **Topics:** IVA; retenciones; facturas especiales
- **Doubts/xref:** xref EVID-1112

## EVID-1099 — IVA third-batch pair: aviso legalización de firmas (D-27-92 art. 57 4º párrafo, 411 Ag. Virtual) and IVA pago de retenciones (D-20-2006 art. 7 num. 2, Declaraguate 2340) — same flat date each month
- **Loc:** `103_-01` p.4–5; `103_-02` p.4; `103_-03` p.4; `103_-04` p.4; `103_-05` p.3; `103_-06` p.4; `103_-07` p.4; `103_-08` p.3
- **Verbatim:** (Enero) "23/01/2026 Al Valor Agregado (Aviso de legalización de firmas en certificados de propiedad de vehículos terrestres) Aviso de Legalización de firmas en Certificados de Propiedad de Vehículos Terrestres. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 57, cuarto párrafo. Correspondientes al mes de Diciembre de 2025. 411 Ag. Virtual" / "23/01/2026 Al Valor Agregado (pago de retenciones) Declaración jurada y pago de retenciones del Impuesto al Valor Agregado. Decreto Número 20-2006, Disposiciones Legales para el Fortalecimiento de la Administración Tributaria. Artículo 7 numeral 2. Correspondiente al mes de Diciembre de 2025. ----- 2340"
- **Gloss:** Monthly third-batch (≈ day 19–24), period = previous month: dates 23/01, 20/02, 20/03, 24/04, 22/05, 19/06, 21/07, 24/08 for BOTH rows in every month. The general IVA-retention payment (D-20-2006 art. 7.2, form 2340, Declaraguate-only channel) is distinct from the facturas-especiales retention (EVID-1098) and sits on the aviso's date, one flat date each.
- **Candidate CRs:** workflow CR: IVA retenciones mensuales (D-20-2006 art. 7.2, form 2340) + aviso firmas vehículos (D-27-92 art. 57 4º, 411 Agencia Virtual) — flat monthly (LB: D-20-2006 art. 7.2; D-27-92 art. 57)
- **Topics:** IVA; retenciones; aves; third batch
- **Doubts/xref:** none open

## EVID-1100 — ISR retenciones sobre actividades lucrativas (D-10-2012 arts. 16 y 48, form 1331): flat mid-month rows all 8 months
- **Loc:** `103_-01` p.4; `103_-02` p.3; `103_-03` p.3; `103_-04` p.3; `103_-05` p.3; `103_-06` p.3; `103_-07` p.2; `103_-08` p.2
- **Verbatim:** (Enero) "16/01/2026 Sobre la Renta. Retenciones Sobre actividades lucrativas residentes y no residentes Declaración jurada y pago mensual de Retenciones. Decreto Número 10-2012, Ley de Actualización Tributaria.  Artículos 16 y 48. Correspondiente al mes de Diciembre de 2025. 1331" [double space before "Artículos" as printed] / (Agosto) "17/08/2026 Sobre la Renta. Retenciones Sobre actividades lucrativas residentes y no residentes Declaración jurada y pago mensual de Retenciones. Decreto Número 10- 2012, Ley de Actualización Tributaria.  Artículos 16 y 48. Correspondiente al mes de Julio de 2026. 1331" [wrap "10- 2012" as printed]
- **Gloss:** ISR retention declarations (resident + non-resident lucrativas): **8 rows, one flat mid-month date per month, period = previous month**: 16/01 (Dic-25), 13/02 (Ene), 13/03 (Feb), 17/04 (Mar), 15/05 (Abr), 12/06 (May), 14/07 (Jun), 17/08 (Jul). No stagger, no digits — part of the flat verdict (EVID-1095). Mid-month date drifts (12–17) with no fixed día printed; the calendar assigns one date per month for the whole mid-month batch (EVID-1114).
- **Candidate CRs:** workflow CR: ISR retenciones mensuales (D-10-2012 arts. 16 y 48, form 1331) — flat mid-month date (LB: D-10-2012 arts. 16, 48)
- **Topics:** ISR; retenciones; deadlines
- **Doubts/xref:** xref EVID-1101, EVID-1114

## EVID-1101 — ISR mid-month family (forms 1311/1321/1341/1352/1371 + médicos CT 112"A".6, codeless): six more flat rows sharing the 1331 date every month
- **Loc:** `103_-01` pp.2–4; `103_-02` p.3; `103_-03` pp.2–3; `103_-04` pp.1–3; `103_-05` pp.1–3; `103_-06` pp.2–3; `103_-07` pp.1–3; `103_-08` pp.1–3
- **Verbatim:** (selected, Enero) "16/01/2026 Sobre la Renta. (Rentas provenientes de dietas, loterías, rifas, sorteos, bingos o eventos similares) … Decreto Número 10-2012, Ley de Actualización Tributaria. Artículo 95. Correspondiente al mes de Diciembre de 2025. 1341" / "16/01/2026 Sobre la Renta. Pago de contribuyentes no residentes (Autoliquidación y pago) … Artículo 106. … 1371" / "16/01/2026 Sobre la Renta. Pago de retenciones efectuadas a contribuyentes no residentes. … Artículo 105. … 1352" / "16/01/2026 Sobre la Renta. Rentas de Capital, Ganancias y Pérdidas de Capital … Artículo 95 primero y segundo párrafo. … 1321" / "16/01/2026 Sobre la Renta. Régimen Opcional Simplificado Sobre Ingresos de Actividades Lucrativas … Artículo 49. … 1311" / "16/01/2026 Al Valor Agregado (Pagos de terceros a favor de médicos, profesionales, técnicos u otros dedicados a la salud) Declaración jurada mediante documento o vía electrónica, del detalle de los pagos de terceros a favor de médicos, profesionales, técnicos u otros dedicados a la salud. Decreto Número 6-91, Código Tributario. Artículo 112 "A" numeral 6. Correspondiente al mes de Diciembre de 2025. -----"
- **Gloss:** Six further obligations riding the same flat mid-month date as EVID-1100 every month: dietas/loterías (art. 95, 1341), no-resident self-liquidation (art. 106, 1371), no-resident retentions (art. 105, 1352), rentas de capital (art. 95 1º-2º párrafo, 1321), optativo simplificado mensual (art. 49, 1311), and the third-party payments to health professionals report (**CT art. 112 "A" numeral 6 — printed codeless "-----", both channels**; titled under IVA but legally a CT information duty). Periods = previous month throughout.
- **Candidate CRs:** workflow CR: ISR monthly cluster (forms 1341/1371/1352/1321/1311) + médicos report (CT 112"A".6, codeless) on the flat mid-month date (LB: D-10-2012 arts. 95, 106, 105, 49; D-6-91 art. 112"A".6)
- **Topics:** ISR; monthly cluster; information duties
- **Doubts/xref:** xref EVID-1114

## EVID-1102 — Petróleo weekly cadence (D-38-92 art. 16, form 6051): complete Jan–Aug inventory of the weekly declaración y pago rows
- **Loc:** `103_-01` pp.1–2, 4–5; `103_-02` pp.1–4; `103_-03` pp.1–4; `103_-04` pp.1–3; `103_-05` pp.1, 3; `103_-06` pp.1–4; `103_-07` pp.1, 3–4; `103_-08` pp.1, 3
- **Verbatim:** (model row, Enero p.1) "05/01/2026 A la Distribución del Petróleo Crudo y Combustibles Derivados del Petróleo. Declaración jurada y pago semanal sobre ventas efectuadas. Decreto Número 38-92, Ley del Impuesto a la Distribución de Petróleo Crudo y Combustibles Derivados del Petróleo. Artículo 16. Correspondiente a la semana del 15 al 21 de Diciembre de 2025. 6051"
- **Gloss:** Full weekly inventory (deadline → week covered): Enero: 05/01→15–21 Dic-25, 07/01→22–28 Dic-25, 09/01→29 Dic–04 Ene, 16/01→05–11 Ene, 23/01→12–18 Ene, 30/01→19–25 Ene. Febrero: 06/02→26 Ene–01 Feb, 13/02→02–08 Feb, 20/02→09–15 Feb, 27/02→16–22 Feb. Marzo: 06/03→23 Feb–01 Mar, 13/03→02–08 Mar, 20/03→09–15 Mar, 27/03→16–22 Mar. Abril: 08/04→23–29 Mar, 10/04→30 Mar–05 Abr, 17/04→06–12 Abr, 24/04→13–19 Abr. Mayo: 04/05→20–26 Abr, 08/05→27 Abr–03 May, 15/05→04–10 May, 22/05→11–17 May, 29/05→18–24 May. Junio: 05/06→25–31 May, 12/06→01–07 Jun, 19/06→08–14 Jun, 30/06→15–21 Jun. Julio: 06/07→22–28 Jun, 10/07→29 Jun–05 Jul, 17/07→06–12 Jul, 24/07→13–19 Jul, 31/07→20–26 Jul. Agosto: 07/08→27 Jul–02 Ago, 17/08→03–09 Ago, 21/08→10–16 Ago, 28/08→17–23 Ago. (35 weekly rows total; weeks run Mon–Sun; several week-boundaries are covered by no listed deadline in the set — e.g. semana del 26 Ene–01 Feb appears in Febrero's file, so cross-month splicing is required; coverage gaps between files noted without inference, OQ-8.)
- **Candidate CRs:** workflow CR: petróleo weekly declaración y pago (D-38-92 art. 16, form 6051), rolling Mon–Sun weeks with per-week flat deadlines (LB: D-38-92 art. 16)
- **Topics:** petróleo; weekly cadence
- **Doubts/xref:** OQ-8

## EVID-1103 — Petróleo monthly informativa (art. 16 "A", form 6080) and annual liquidación (art. 6 "B", form 6090)
- **Loc:** 16"A": `103_-01` p.2; `103_-02` p.2; `103_-03` p.1; `103_-04` p.1; `103_-05` p.1; `103_-06` p.1; `103_-07` p.1; `103_-08` p.1. 6"B": `103_-01` p.2 only
- **Verbatim:** (Enero, both) "12/01/2026 A la Distribución de Petróleo Crudo y Combustibles Derivados del Petróleo Declaración jurada informativa mensual de saldos, compras y ventas. Decreto Número 38-92, … Artículo 16 "A". correspondiente al mes de Diciembre de 2025. 6080" [lowercase "correspondiente" as printed] / "16/01/2026 A la Distribución del Petróleo Crudo y Combustibles Derivados del Petróleo Declaración jurada informativa anual de liquidación de cuenta corriente. Decreto Número 38-92, … Artículo 6 "B". Correspondiente  al período del 1 de Enero al 31 de Diciembre de 2025. 6090" [double space "Correspondiente  al" as printed]
- **Gloss:** Monthly saldos/compras/ventas informativa, flat ~day 10–12 each month: 12/01 (Dic-25), 10/02 (Ene), 10/03 (Feb), 10/04 (Mar), 11/05 (Abr), 10/06 (May), 10/07 (Jun), 10/08 (Jul). Annual cuenta-corriente liquidación for calendar-2025: 16/01/2026 only (Enero file).
- **Candidate CRs:** workflow CR: petróleo monthly informativa (16"A", 6080) ~day 10 + annual liquidación (6"B", 6090) mid-January (LB: D-38-92 arts. 16"A", 6"B")
- **Topics:** petróleo; informativa; annual
- **Doubts/xref:** none open

## EVID-1104 — Impuesto al Servicio del Cable (D-41-92 art. 9, form 9031): flat rows glued to the IVA-general dates; absent from the Mayo print
- **Loc:** `103_-01` p.1; `103_-02` p.1; `103_-03` pp.1, 4; `103_-04` pp.4–5; `103_-05` (absent); `103_-06` pp.1, 4; `103_-07` p.5; `103_-08` p.4
- **Verbatim:** (Enero) "05/01/2026 Impuesto al Servicio del Cable.  Declaración y pago mensual del Impuesto al Servicio del Cable. Declaración y pago mensual del impuesto a la distribución de señal por cable.  Decreto Número  41-92, Ley Reguladora del Uso y Captación de Señales Vía Satélite y su Distribución por Cable. Artículo 9. Correspondiente al mes de Noviembre de 2025. 9031" [double spaces after "Cable." and "Número" as printed]
- **Gloss:** Cable (señal vía satélite): same 10 flat dates and periods as IVA general/pequeño/facturas-especiales in every month where the family appears (05/01 Nov, 02/02 Dic, 02/03 Ene, 31/03 Feb, 30/04 Mar, —, 01/06 Abr, 30/06 May, 31/07 Jun, 31/08 Jul) — the "first batch" family. Absent from the Mayo file together with the whole IVA trio (EVID-1113). Note the doubled description line (concept repeats itself) as printed.
- **Candidate CRs:** workflow CR: cable mensual (D-41-92 art. 9, form 9031) — flat date, same as IVA general batch (LB: D-41-92 art. 9)
- **Topics:** cable; IVA batch; deadlines
- **Doubts/xref:** xref EVID-1113

## EVID-1105 — Timbre de papel sellado especial para protocolos: retenciones por loterías, rifas y sorteos (AG 4-2013 art. 11, form 7130): flat mid-month rows
- **Loc:** `103_-01` p.3; `103_-02` p.2; `103_-03` p.2; `103_-04` p.2; `103_-05` p.2; `103_-06` p.2; `103_-07` p.1; `103_-08` p.1
- **Verbatim:** (Enero) "16/01/2026 De Timbres Fiscales y de Papel Sellado Especial para Protocolos. (Retenciones por loterias, rifas y sorteos) Declaración jurada y pago de retenciones por  loterías, rifas y sorteos efectuadas mensualmente. Acuerdo Gubernativo 4-2013, Reglamento de la Ley del Impuesto de Timbres Fiscales y de Papel Sellado Especial para Protocolos. Artículo 11. Correspondientes al mes de Diciembre de 2025. 7130" ["loterias" unaccented in title, double space "por  loterías" as printed]
- **Gloss:** The only timbre-family row in the set: monthly retention declaration for loterías/rifas/sorteos under the **reglamento** (AG 4-2013 art. 11), riding the flat mid-month batch (same dates as EVID-1100/1101: 16/01, 13/02, 13/03, 17/04, 15/05, 12/06, 14/07, 17/08; period = previous month). No other timbre obligations (no papel sellado purchase rows, no otros actos) appear in these 8 calendars.
- **Candidate CRs:** workflow CR: timbre-protocolo retenciones loterías/rifas/sorteos (AG 4-2013 art. 11, form 7130) — flat mid-month (LB: AG 4-2013 art. 11)
- **Topics:** timbre; retenciones; loterías
- **Doubts/xref:** none open

## EVID-1106 — Specific-consumption family: tabaco (D-61-77 art. 25, 5100), cemento (D-79-2000 art. 9, 9208), bebidas alcohólicas (D-21-2004 art. 20, 3109), imprentas informe (D-20-2006 art. 17, 541 Agencia Virtual) — flat mid-month batch
- **Loc:** tabaco: `103_-01` p.2 … `103_-08` p.1 (all 8); cemento, bebidas, imprentas: same pages as EVID-1101 batch in all 8 files
- **Verbatim:** (Enero, one per family) "16/01/2026 Al Tabaco y sus Productos. Declaración jurada y pago mensual sobre ventas efectuadas. Decreto Número 61-77, Ley de Tabacos y sus Productos. Artículo 25. Correspondiente al mes de Diciembre de 2025. ----- 5100" / "16/01/2026 Específico a la Distribución de Cemento Declaración jurada y pago mensual sobre ventas efectuadas. Decreto Número 79-2000, Ley del Impuesto Específico a la Distribución de Cemento. Artículo 9. Correspondiente al mes de Diciembre de 2025. ----- 9208" / "16/01/2026 Sobre la distribución de bebidas alcohólicas destiladas, cervezas y otras bebidas fermentadas … Decreto Número 21-2004, … Artículo 20. … 3109" / "16/01/2026 Informe de servicios de impresión (Imprentas y servicios de impresión) Informe mensual de servicios de impresión de documentos. Decreto Número 20-2006, Disposiciones Legales para el Fortalecimiento de la Administración Tributaria. Artículo 17. Correspondientes al mes de Diciembre de 2025. 541 Agencia Virtual"
- **Gloss:** Four consumption/admin families, each one flat mid-month row per month, period = previous month, on the identical dates as EVID-1100/1101 (16/01, 13/02, 13/03, 17/04, 15/05, 12/06, 14/07, 17/08). Channel split as printed: tabaco and cemento are **Declaraguate-only** ("----- 5100" / "----- 9208"); imprentas is **Agencia Virtual** ("541 Agencia Virtual"); bebidas prints lone code 3109.
- **Candidate CRs:** workflow CR: tabaco/cemento/bebidas monthly declarations + imprentas informe on the flat mid-month date (LB: D-61-77 art. 25; D-79-2000 art. 9; D-21-2004 art. 20; D-20-2006 art. 17)
- **Topics:** specific consumption; imprentas; deadlines
- **Doubts/xref:** xref EVID-1114

## EVID-1107 — ISO Impuesto de Solidaridad trimestral (D-73-2008 art. 10, form 1608): three flat quarterly dates
- **Loc:** `103_-02` p.1 (02/02); `103_-04` p.4 (30/04); `103_-07` p.5 (31/07)
- **Verbatim:** (Febrero) "02/02/2026 De Solidaridad, (Pagos trimestrales). Pago trimestral. Decreto Número 73-2008, Ley del Impuesto de Solidaridad. Artículo 10. Correspondiente al trimestre del 1 de Octubre al 31 de Diciembre de 2025 1608" / (Julio) "31/07/2026 De Solidaridad, (Pagos trimestrales). … Correspondiente al trimestre del 1 de Abril al 30 de Junio de 2026 1608"
- **Gloss:** ISO quarterly rows: 02/02 (Q4-2025), 30/04 (Q1-2026), 31/07 (Q2-2026) — one flat date per quarter, riding the first-batch dates of the month following quarter-end (+1 month). No Q3-2026 row (Sept capture absent, OQ-1).
- **Candidate CRs:** workflow CR: ISO trimestral (D-73-2008 art. 10, form 1608) — flat, ≈ first batch of month after quarter (LB: D-73-2008 art. 10)
- **Topics:** ISO; quarterly
- **Doubts/xref:** OQ-1

## EVID-1108 — ISR trimestral utilidades (D-10-2012 art. 38, form 1361) and semestral inventarios (art. 42 num. 3, form 1391)
- **Loc:** 1361: `103_-04` p.5 (30/04); `103_-07` p.5 (31/07). 1391: `103_-02` p.1 (02/02); `103_-07` p.5 (31/07)
- **Verbatim:** (Abril) "30/04/2026 Sobre la Renta. Régimen Sobre las Utilidades de Actividades Lucrativas Declaración jurada y pago trimestral, Régimen Sobre las Utilidades de Actividades Lucrativas. Decreto Número 10-2012, Ley de Actualización Tributaria. Artículo 38. Correspondientes al trimestre del 1 de Enero al 31 de Marzo de 2026. 1361" / (Febrero) "02/02/2026 Sobre la Renta. Informe de existencias en inventarios Informe de existencias en inventarios al 30 de junio y 31 de diciembre de cada año. Decreto Número 10-2012, Ley de Actualización Tributaria. Artículo 42 numeral 3. Correspondiente al semestre 1 de Julio al 31 de Diciembre de 2025. 1391"
- **Gloss:** Utilidades trimestral: 30/04 (Q1), 31/07 (Q2) — no Q4-2025 row in Enero/Febrero prints (as printed; the Febrero file carries ISO for Q4-2025 but no 1361 — noted without inference, OQ-5). Inventories: half-yearly informe due 02/02 (for Jul–Dic-25) and 31/07 (for Ene–Jun-26), both riding first-batch dates.
- **Candidate CRs:** workflow CR: ISR utilidades trimestral (art. 38, 1361) + inventarios semestral (art. 42.3, 1391) — flat quarter/semester dates (LB: D-10-2012 arts. 38, 42.3)
- **Topics:** ISR; quarterly; semestral
- **Doubts/xref:** OQ-5

## EVID-1109 — Annual rows: planilla IVA acreditable al ISR (D-10-2012 art. 72, 1111), ISR renta-trabajo anual (art. 81 4º, 1431), ISR anual optativo/utilidades (arts. 39 y 49, 1411), circulación de vehículos aéreos (D-70-94 art. 29.a, 4131) y marítimos (4121)
- **Loc:** `103_-01` p.2 (planilla, 16/01); `103_-03` p.5 (both ISR anuales, 31/03); `103_-07` p.5 (both vehículos, 31/07)
- **Verbatim:** (Enero) "16/01/2026 AL VALOR AGREGADO (Planilla del IVA acreditable al Impuesto Sobre la Renta.) Planilla para crédito por IVA en el ISR. Decreto Número 10-2012, Ley de Actualización Tributaria. Artículo 72. Del período del 1 de Enero al 31 de Diciembre de 2025. 1111 -------" / (Marzo) "31/03/2026 Sobre la Renta. Renta del Trabajo en Relación de Dependencia Declaración jurada y pago anual.  Renta del Trabajo en Relación de Dependencia. Decreto Número 10-2012, … Artículo 81 cuarto párrafo. Correspondientes al período de 1 de Enero al 31 de Diciembre de 2025 1431" + "31/03/2026 Sobre la Renta. Régimen Opcional Simplificado Sobre Ingresos y Régimen Sobre Utilidades de Actividades Lucrativas Declaración jurada anual. … Artículos 39 y 49. Correspondiente  al período del 1 de Enero al 31 de Diciembre de 2025. 1411" / (Julio) "31/07/2026 Sobre Circulación de Vehículos Aéreos Declaración y pago anual … Decreto Número 70-94, Ley del Impuesto Sobre Circulación de Vehículos Terrestres, Marítimos y Aéreos. Artículo 29 inciso a). Correspondiente a 1 de Enero al 31 de Diciembre de 2026. 4131" + "31/07/2026 Sobre Circulación de Vehículos Marítimos … Correspondiente 1 de Enero al 31 de Diciembre de 2026. 4121"
- **Gloss:** Five annual-cycle rows in the set, each one flat date: planilla IVA (16/01, Asiste-Web-only channel "1111 -------"); both ISR annual declarations (31/03, calendar-2025 periods); aéreos and marítimos circulation taxes (31/07, calendar-2026 periods). Note: the 70-94 vehicle rows are the ONLY rows in the set whose period is FUTURE to the deadline year (annual 2026 tax due 31/07/2026, as printed). Terrestre circulation (placas) does not appear in these calendars.
- **Candidate CRs:** workflow CR: annual flat dates — planilla IVA (Jan-16), ISR anual pair (Mar-31), vehículos aéreos/marítimos (Jul-31) (LB: D-10-2012 arts. 72, 81, 39 y 49; D-70-94 art. 29.a)
- **Topics:** annual; ISR; vehículos
- **Doubts/xref:** none open

## EVID-1110 — Constancias de exención del IVA (AG 5-2013 art. 14): quarterly, printed FOUR duplicate rows per quarter with alternating channels (2118 / 2360)
- **Loc:** `103_-01` pp.4–5 (23/01, ×4); `103_-04` pp.3–4 (24/04, ×4); `103_-07` pp.3–4 (21/07, ×4)
- **Verbatim:** (Enero, one of the four) "23/01/2026 Al Valor Agregado (Informe de constancias de exención emitidas trimestralmente). Informe trimestral de Constancias de Exención. Acuerdo Gubernativo Número 5-2013, Reglamento de la Ley del Impuesto al Valor Agregado. Artículo 14. Constancias emitidas del 1 de Octubre al 31 de Diciembre de 2025. ----- 2360" — the four 23/01 rows print codes: "----- 2360", "2118 -----", "2118 -----", "----- 2360" (same order pattern at 24/04 and 21/07; quarter windows 1 Ene–31 Mar and 1 Abr–30 Jun respectively)
- **Gloss:** Quarterly informe de constancias de exención: **each quarter prints FOUR identical rows** — two in the Asiste-Web-only variant (2118) and two in the Declaraguate-only variant (2360) — same date, same period, same legal basis. Reported as printed; whether the quadruplication reflects two informes × two channels or an app artifact is not determinable from the print (OQ-3). Date rides the third batch (23/01, 24/04, 21/07).
- **Candidate CRs:** workflow CR: quarterly constancias-de-exención informe (AG 5-2013 art. 14, forms 2118/2360) — flat third-batch date (LB: AG 5-2013 art. 14)
- **Topics:** IVA; constancias de exención; quarterly; duplication anomaly
- **Doubts/xref:** OQ-3

## EVID-1111 — ICT Impuesto a la Confianza Tributaria (D-31-2024) rows appear ONLY in Julio (form 2540) and Agosto (2540 + 2530/2520/2510) — verbatim
- **Loc:** `103_-07` p.1 (10/07, 2540); `103_-08` p.1 (10/08, 2540) and p.4 (31/08: 2530, 2520, 2510)
- **Verbatim:** (Julio) "10/07/2026 Retenciones efectuadas al emitir Facturas Específicas ICT Regímenes Primario/Pecuario Impuesto a la Confianza Tributaria Decreto 31-2024 Art. 9 declaración y pago mensual de retenciones por emisión de Facturas Específicas del régimen primario/pecuario durante Junio de 2026. 2540" / (Agosto, p.4) "31/08/2026 Declaración consolidada ICT Primario / Pecuario ¿ IVA General. Declaración jurada y recibo de pago mensual Consolidada del IVA. Decreto Número 27-92. Artículo 40-ICT régimen primario y pecuario Decreto Número 31-2024 Art.8 de operaciones efectuadas durante Julio de 2026 2530" / "31/08/2026 Impuesto a la Confianza Tributaria Declaración y pago mensual, Régimen Pecuario Impuesto a la Confianza Tributaria Decreto 31-2024 declaración y pago mensual del régimen pecuario sobre ventas y/o prestación de servicios efectuadas durante Julio de 2026. 2520" / "31/08/2026 Impuesto a la Confianza Tributaria Declaración y pago mensual, Régimen Primario … régimen primario sobre ventas y/o prestación de servicios efectuadas durante Julio de 2026. 2510" [title glyph "¿" as printed]
- **Gloss:** The post-D-31-2024 ICT regime surfaces in the calendar as: (i) monthly retention on Facturas Específicas of the primary/pecuary regimes (**D-31-2024 art. 9**, form 2540) on the ~10th, first appearing in the Julio print (period Junio) and repeating 10/08 (period Julio); (ii) three 31/08 rows for the Julio period: the **consolidated IVA+ICT return** (dual basis "Decreto Número 27-92. Artículo 40 - ICT régimen primario y pecuario Decreto Número 31-2024 Art.8", form 2530) plus separate ICT mensual rows for régimen pecuario (2520) and primario (2510). **None of these four ICT row-types appears in Enero–Junio prints** (presence, not start-date, is what the corpus shows — OQ-4). All flat single dates.
- **Candidate CRs:** workflow CR: ICT monthly set (D-31-2024 arts. 8/9, forms 2540/2530/2520/2510) — flat dates, day-10 retentions + day-31 regime declarations from the Julio/Agosto prints (LB: D-31-2024 arts. 8, 9)
- **Topics:** ICT; D-31-2024; primario/pecuario; deadlines
- **Doubts/xref:** OQ-4; xref EVID-1112

## EVID-1112 — D-7-2019 arts. 54 "A"-"F" (RECA / electrónico 4%) ABSENCE verdict: zero rows in all 8 months; the only art. 54 is D-27-92's facturas especiales
- **Loc:** full-text search of `103_-01`..`103_-08`: strings "7-2019", "RECA", "54 \"A\""…"54 \"F\"" — zero hits; the sole "Artículo 54" rows are the D-27-92 facturas-especiales rows (EVID-1098) in all 8 months
- **Verbatim:** (absence evidence; nearest printed strings) "Pago mensual de retenciones del 12%, sobre el monto de facturas especiales emitidas. Decreto Número 27-92, Ley del Impuesto al Valor Agregado. Artículo 54." (every month) — no row anywhere cites "Decreto Número 7-2019" in any form
- **Gloss:** **Per-month presence/absence: D-7-2019 arts. 54 "A"-"F" (régimen electrónico / RECA, 4%) = ABSENT in Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio y Agosto 2026 (0/8 months).** The calendar's only 12%-facturas-especiales retention cites D-27-92 art. 54. This is consistent with (but does not itself print) the D-31-2024 art. 25 derogation of that regime effective 2025-08-09 (registry cross-ref, EVID-1111 context); reported strictly as absence from these administrative tables, not as a legal finding.
- **Candidate CRs:** guard CR: no RECA/electrónico-4% obligation is calendared Ene–Ago 2026 — do not model a D-7-2019 54"A"-"F" deadline row for 2026 (LB: absence in SAT Calendario Ene–Ago 2026; derogation per D-31-2024 art. 25 [registry])
- **Topics:** RECA; D-7-2019; absence; ICT replacement
- **Doubts/xref:** xref EVID-1098, EVID-1111

## EVID-1113 — The Mayo anomaly: the IVA first-batch family (arts. 40, 48, 54, cable 9031) is entirely ABSENT from the Mayo print; Abril-period deadlines appear as 01/06 in the Junio print; period→deadline lag is mixed M+1/M+2
- **Loc:** `103_-05` whole file (3 pp., no art. 40/48/54/9031 rows); `103_-06` p.1 (01/06 rows for Abril) and p.4 (30/06 rows for Mayo)
- **Verbatim:** (Junio, p.1) "01/06/2026 Al Valor Agregado (Operaciones afectas y exentas). … Artículo 40. Durante Abril de 2026 2237" — (complete period→deadline map for art. 40, as printed): Nov-25→05/01; Dic-25→02/02; Ene-26→02/03; Feb-26→31/03; Mar-26→30/04; Abr-26→01/06; May-26→30/06; Jun-26→31/07; Jul-26→31/08. **No art. 40 row for any period appears in the Mayo file.**
- **Gloss:** Two findings, reported without inference: (a) the Mayo print omits the entire first-batch family (IVA general, pequeño, facturas especiales, cable) — the Abril-period deadlines surface as 01/06 in the Junio print instead, and no Mayo-file row covers them; (b) the printed period→deadline lag is MIXED — Nov–Ene periods fall two months later (05/01, 02/02, 02/03), Feb–Jul periods one month later (31/03, 30/04, 30/06, 31/07, 31/08), with Abril again at M+2 (01/06). Whether (a) is an app/print omission or reflects an actual re-scheduling, and whether the lag shift reflects a regime change or reprint artifacts, cannot be decided from these prints (OQ-2, OQ-5). The flat verdict (EVID-1095) is unaffected: every row is still one date per period.
- **Candidate CRs:** tracking CR: verify Mayo-2026 IVA family deadlines (absent from `103_-05`; Abril period prints as 01/06) against SAT before hardcoding M+1 vs M+2 lags (LB: `103_-05`/`103_-06` as printed)
- **Topics:** calendar gaps; lag structure; IVA
- **Doubts/xref:** OQ-2, OQ-5

## EVID-1114 — The three-batch monthly architecture + date-drift table (one flat date per batch per month, mid-batch dates drift)
- **Loc:** compiled from all 8 files (each batch's rows share one date within a month: first batch EVID-1096/1097/1098/1104/1107; mid batch EVID-1100/1101/1105/1106; third batch EVID-1099/1110)
- **Verbatim:** (batch-date table, as printed) First batch: 05/01, 02/02, 02/03 & 31/03, 30/04, —, 01/06 & 30/06, 31/07, 31/08. Mid batch: 16/01, 13/02, 13/03, 17/04, 15/05, 12/06, 14/07, 17/08. Third batch: 23/01, 20/02, 20/03, 24/04, 22/05, 19/06, 21/07, 24/08.
- **Gloss:** Within each month, all obligations of a batch print the SAME single date (e.g. in Agosto everything mid-batch = 17/08: tabaco, médicos, timbre, cemento, imprentas, ISR 1341/1371/1352/1321/1331/1311, bebidas). Batch dates are not a fixed día fijo — first batch ranges 01–31 (month-end/early-month), mid batch 12–17, third batch 19–24. The calendar thus assigns 3 flat dates + weekly petróleo Mondays-ish + day-10 petróleo informativa/ICT-2540 per month. Modelling consequence: GT deadline engine = per-month SAT-published date table, not computable day-of-month rules.
- **Candidate CRs:** guard CR: GT 2026 deadlines are SAT-published per-month flat batch dates (3 batches + weekly petróleo) — do not derive them from fixed day-of-month formulas; consume the calendar (LB: `103_` as printed)
- **Topics:** deadline architecture; batches
- **Doubts/xref:** xref EVID-1095, EVID-1113

## EVID-1115 — CONTEXT NOTE (owner-verified, NOT document-printed): SAT's current Calendario Tributario app exposes no NIT-digit-keyed windows
- **Loc:** controller instruction recorded in this file on 2026-08-23; NOT a quote from any `103_` document
- **Verbatim:** (controller instruction, cited as such) owner verified on 2026-08-23 that SAT's current Calendario Tributario app exposes NO NIT-digit-keyed deadline windows.
- **Gloss:** **Owner-verified context note, clearly marked as such (not document-printed):** the app that produced these PDFs presents deadline rows without any NIT-digit parameter — corroborating, from the tooling side, the flat-deadline verdict drawn from the prints (EVID-1095/1096). Kept out of the verbatim record of the calendars themselves; no candidate CR is drawn from it beyond the EVID-1095 guard.
- **Candidate CRs:** none from this note alone (see EVID-1095 guard CR)
- **Topics:** deadline structure; owner-verified context
- **Doubts/xref:** xref EVID-1095

## EVID-1116 — Filing-channel inventory: Asiste Web vs Declaraguate vs Agencia Virtual column usage as printed
- **Loc:** all 8 files, code columns; unambiguous rows only
- **Verbatim:** (channel-attributed codes, as printed) Asiste-Web-only: "1111 -------" (planilla IVA, Ene); Declaraguate-only: "----- 5100" (tabaco, all months), "----- 9208" (cemento, all months), "----- 2340" (IVA retenciones D-20-2006, all months), "----- 2360" (constancias, quarters); Agencia Virtual: "541 Agencia Virtual" (imprentas, all months), "411 Ag. Virtual" (aviso firmas, all months); codeless both channels: "-----" (médicos CT 112"A".6, all months). Lone codes without printed "-----" counterpart (column not attributable from the text layer): 2237, 2085, 2046, 9031, 6051, 6080, 6090, 1608, 1391, 1341, 1371, 1352, 1321, 1331, 1311, 1361, 1431, 1411, 4131, 4121, 7130, 3109, 2540, 2530, 2520, 2510, 2118.
- **Gloss:** Channel map as printed: some obligations are single-channel by design (tabaco/cemento/2340 → Declaraguate; planilla → Asiste Web; imprentas/aviso → Agencia Virtual; médicos → no form code at all). For 27 lone-code rows the collapsed text layer cannot attribute the column (OQ-7) — codes recorded, columns left unasserted.
- **Candidate CRs:** guard CR: per-obligation filing channel is form-code-specific (Declaraguate/Asiste Web/Agencia Virtual/codeless) — map channels per form, never assume one portal (LB: `103_` code columns as printed)
- **Topics:** filing channels; form codes
- **Doubts/xref:** OQ-7

## EVID-1117 — CLOSING SYNTHESIS: what the 8 calendars establish about SAT's 2026 deadline practice
- **Loc:** all 8 files, mapped against mission items
- **Verbatim:** (anchors) "Artículo 40. Durante Noviembre de 2025" (`103_-01` p.1) / "Artículo 40. Durante Julio de 2026" (`103_-08` p.4) / "dicho día debe considerarse inhábil para el municipio de Guatemala…" (all pages) / zero "7-2019"/"NIT"/"dígito" hits (all files)
- **Gloss:** (1) **Flat-deadline practice confirmed across all 8 months and every obligation family** — one date per obligation-period, no NIT-digit/group staggers, corroborated by the owner's app check (EVID-1095/1096/1115); the historic stagger cannot be sourced from 2026 practice. (2) The monthly architecture is 3 flat batch-dates + weekly petróleo + day-10 informativas, with drifting day-numbers — deadlines are table data, not formulas (EVID-1114). (3) The only inhábil ruling printed is SAT-DSI-1328-2026, **municipality-scoped** (EVID-1094) — inhábil logic must be per-locality. (4) The D-7-2019 RECA regime is absent from every month's calendar, its 12%-retention slot occupied by D-27-92 art. 54, while D-31-2024 ICT rows surface in Julio/Agosto (EVID-1112/1111) — the calendars reflect the post-cutover regime landscape. (5) Calendar-specific anomalies to carry forward: Mayo first-batch omission, mixed M+1/M+2 IVA lag, constancias 4× duplication, ICT first-appearance (EVID-1113/1110/1111; OQ-2/3/4/5).
- **Candidate CRs:** guard CR: model GT 2026 deadlines as SAT-published flat per-period dates + CT 8.2 inhábil roll (municipality-scoped rulings) + per-form channels; no digit ladders, no day-of-month formulas, no RECA rows (LB: `103_` set as printed; D-6-91 art. 8.2)
- **Topics:** synthesis; deadline practice; registry feed
- **Doubts/xref:** OQ-1..OQ-8

---

## Deadline inventory (per month, grouped by family; dates as printed)

| Month (file) | Petróleo weekly (6051) | Petróleo 16"A" (6080) / 6"B" (6090) | IVA general 40 (2237) | IVA pequeño 48 (2046) | Fact. espec. 54 (2085) | Cable 9 (9031) | ISR ret. 16 y 48 (1331) + mid batch | Third batch (2340 / 411 / constancias) |
|---|---|---|---|---|---|---|---|---|
| Enero (`103_-01`) | 05, 07, 09, 16, 23, 30/01 | 12/01 (Dic) / 16/01 (anual 2025) | 05/01 (Nov-25) | 05/01 (Nov-25) | 05/01 (Nov-25) | 05/01 (Nov-25) | 16/01 (Dic-25) | 23/01 (Dic-25; constancias ×4, Q4-25) |
| Febrero (`103_-02`) | 06, 13, 20, 27/02 | 10/02 (Ene) | 02/02 (Dic-25) | 02/02 (Dic-25) | 02/02 (Dic-25) | 02/02 (Dic-25) | 13/02 (Ene-26) | 20/02 (Ene-26) |
| Marzo (`103_-03`) | 06, 13, 20, 27/03 | 10/03 (Feb) | 02/03 (Ene) + 31/03 (Feb) | same ×2 | same ×2 | same ×2 | 13/03 (Feb) | 20/03 (Feb); **31/03: ISR anual 1431 + 1411 (año 2025)** |
| Abril (`103_-04`) | 08, 10, 17, 24/04 | 10/04 (Mar) | 30/04 (Mar) | 30/04 (Mar) | 30/04 (Mar) | 30/04 (Mar) | 17/04 (Mar) | 24/04 (Mar; constancias ×4, Q1) |
| Mayo (`103_-05`) | 04, 08, 15, 22, 29/05 | 11/05 (Abr) | **— none —** | **—** | **—** | **—** | 15/05 (Abr) | 22/05 (Abr) |
| Junio (`103_-06`) | 05, 12, 19, 30/06 | 10/06 (May) | 01/06 (Abr) + 30/06 (May) | same ×2 | same ×2 | same ×2 | 12/06 (May) | 19/06 (May) |
| Julio (`103_-07`) | 06, 10, 17, 24, 31/07 | 10/07 (Jun); **ICT 2540 10/07 (Jun)** | 31/07 (Jun) | 31/07 (Jun) | 31/07 (Jun) | 31/07 (Jun) | 14/07 (Jun) | 21/07 (Jun; constancias ×4, Q2); 31/07: ISO 1608 (Q2) + utilidades 1361 (Q2) + inventarios 1391 (1S-26) + vehículos 4131/4121 (año 2026) |
| Agosto (`103_-08`) | 07, 17, 21, 28/08 | 10/08 (Jul); **ICT 2540 10/08 (Jul)** | 31/08 (Jul) | 31/08 (Jul) | 31/08 (Jul) | 31/08 (Jul) | 17/08 (Jul) | 24/08 (Jul); **31/08: ICT 2530/2520/2510 (Jul)** |

Quarterly/annual/semestral rows also appearing: ISO 1608 — 02/02 (Q4-25), 30/04 (Q1), 31/07 (Q2); utilidades 1361 — 30/04 (Q1), 31/07 (Q2); inventarios 1391 — 02/02 (2S-25), 31/07 (1S-26); planilla 1111 — 16/01 (2025); ISR anual 1431/1411 — 31/03 (2025); petróleo anual 6090 — 16/01 (2025); vehículos 4131/4121 — 31/07 (2026).

## Legal-basis cite inventory (every distinct basis printed in the set)

| Instrument | Arts. cited | Rows |
|---|---|---|
| D-6-91 Código Tributario | 8.2 (nota); 112 "A" num. 6 | footer ×35; médicos monthly |
| D-10-2012 LAT | 16 y 48; 38; 39 y 49; 42.3; 49; 72; 81 4º; 95; 95 1º-2º; 105; 106 | ISR family, trimestral, anual, planilla, inventarios |
| D-20-2006 Fortalecimiento Adm. Trib. | 7 num. 2; 17 | IVA retenciones 2340; imprentas 541 |
| D-21-2004 bebidas | 20 | 3109 monthly |
| D-27-92 IVA | 40; 48; 54; 57 4º | IVA trio monthly; aviso 411; ICT-consolidada 2530 (joint cite with D-31-2024 art. 8) |
| D-31-2024 ICT | 8; 9 | 2530/2520/2510 (31/08); 2540 (10/07, 10/08) |
| D-38-92 petróleo | 16; 16 "A"; 6 "B" | 6051 weekly; 6080 monthly; 6090 annual |
| D-41-92 cable | 9 | 9031 monthly |
| D-61-77 tabacos | 25 | 5100 monthly |
| D-70-94 circulación vehículos | 29 inc. a) | 4131/4121 annual |
| D-73-2008 ISO | 10 | 1608 quarterly |
| D-79-2000 cemento | 9 | 9208 monthly |
| AG 4-2013 reglamento timbre | 11 | 7130 monthly |
| AG 5-2013 reglamento IVA | 14 | constancias 2118/2360 quarterly |
| Res. SAT-DSI-1328-2026 | — | inhábil 14-ago-2026, 3 municipios (footer) |

**D-7-2019: absent entirely (0 cites, 0/8 months).**

## Dated rows (D16-style, selection of load-bearing ones)

| Date | Event (as printed) |
|---|---|
| 05/01/2026 | First-batch flat deadline: IVA 40 (Nov-25) / pequeño 48 / fact. espec. 54 / cable |
| 16/01/2026 | Mid batch (Dic-25) + planilla IVA 1111 + petróleo anual 6090 (2025) |
| 23/01/2026 | Third batch (Dic-25) + constancias ×4 (Q4-25) |
| 02/02/2026 | First batch (Dic-25) + ISO 1608 (Q4-25) + inventarios 1391 (2S-25) |
| 02/03 y 31/03/2026 | Two flat IVA dates in one month (periods Ene y Feb) — NOT a stagger |
| 31/03/2026 | ISR anual 1431/1411 (año 2025) |
| 30/04/2026 | First batch (Mar) + ISO (Q1) + utilidades 1361 (Q1) |
| 10/07/2026 | First ICT row in the set: 2540 retenciones (Junio) |
| 31/07/2026 | First batch (Jun) + ISO/utilidades (Q2) + inventarios (1S-26) + vehículos aéreos/marítimos (2026) |
| 10/08/2026 | ICT 2540 (Julio) |
| 31/08/2026 | First batch (Jul) + ICT 2530/2520/2510 (Julio) |
| 14/08/2026 | Inhábil (municipios Guatemala, Chiquimula, Sololá only) per Res. SAT-DSI-1328-2026 |

---

## Open questions

- **OQ-1:** Sep–Dic 2026 calendars not captured; Q3/Q4 rows (ISO Q3, utilidades Q3, constancias Q3, IVA Ago–Nov periods, any ICT expansion) remain un-sourced.
- **OQ-2:** The Mayo print omits the entire IVA first-batch family (arts. 40/48/54, cable); the Abril-period deadlines print as 01/06 in the Junio file. Print omission vs actual re-scheduling is undecidable from the corpus.
- **OQ-3:** Constancias-de-exención rows print 4× per quarter (2× channel 2118, 2× channel 2360), identical date/period/basis — duplication semantics (two informes vs app artifact) unknown.
- **OQ-4:** ICT rows first appear in the Julio (2540) and Agosto (2530/2520/2510) prints; whether the ICT calendar rows existed before Julio 2026 (and simply aren't in this capture) is unknown — the prints show presence, not start date.
- **OQ-5:** Printed IVA period→deadline lag is mixed (M+2 for Nov-25–Ene-26 and Abr-26 periods; M+1 for Feb/Mar/May–Jul-26); likewise no Q4-2025 utilidades-1361 row appears while ISO Q4-2025 does. Cause (regime change, reprint, app data) not determinable from the prints.
- **OQ-6:** Res. SAT-DSI-1328-2026 itself is not in the corpus — its full text, derivation (permiso laboral → inhábil) and any companion rulings for other localities/dates are un-sourced; the calendars quote only its effect.
- **OQ-7:** Text-layer column collapse: for 27 lone form codes the Asiste-Web vs Declaraguate attribution is not recoverable from these extractions (needs the PDF layout or SAT form catalogue).
- **OQ-8:** Petróleo weekly coverage: week-boundaries spliced across monthly files leave inter-file weeks (e.g. semana 26 Ene–01 Feb in the Febrero file) and at least one week per file boundary unlisted; whether SAT's week-to-deadline mapping is exhaustive is unverified.
