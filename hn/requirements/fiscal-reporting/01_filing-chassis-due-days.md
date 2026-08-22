# HN — Fiscal reporting — OVI/SW filing chassis, declaration lifecycle & the shared due-day engine

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F1 of the master
index: the generic SAR **declaration-filing chassis** — the *Oficina Virtual
Interactiva* (OVI, SAR's interactive virtual office) and *Servicio Web* (SW,
the batch plantilla channel) framed by Acuerdo SAR-236-2024 — plus the
**shared due-day engine** (the consolidated fiscal calendar that every other
S-HN3 file's deadline rows feed). It owns: (a) the declaration-lifecycle
state machine shared by every form family — login → *alta de obligación* /
*Nueva Declaración Eventual* → *pendiente* → *borrador* (draft) → *juramento*
(sworn-accuracy attestation) → *acuse electrónico* (electronic
acknowledgment: código único + QR, CSV on form 527) → estado pill →
Pagar / *Boletín de Pago* (payment slip with caducidad) — with the rechazo
terminal state and the rectificativa lifecycle (new record superseding a
frozen original snapshot, D-H2.5; same-modality routing, CT Art. 117 frame
consumed by id); (b) the dual-channel contract — OVI *o* SW with the STICKY
single-modality rule (SAR-236-2024 DÉCIMO SÉPTIMO/OCTAVO + SAR-237-2024
numeral 2.II — R-H27: older manuals/Ayudas claiming "único medio OVI" are
stale, cited per-row only) and the SW plantilla two-stage validation
pipeline; (c) the per-instrument **due-day engine**: días calendario by
default unless the instrument says hábiles (`04_ OQ-3` discipline),
per-instrument semantics stored as dated config rows on one consolidated
fiscal-calendar model resolved by period/*hecho generador* date (D-H2) —
siblings own their instruments' rows, this file owns the engine, the model
and the corpus deadline inventory; and (d) the D-H3 go-live reconciliation
surface: the previous system's SAR filings imported as frozen authoritative
aggregates plus the delta-report engine.

It does **not** cover: per-código casilla/line contracts, retention rates or
declaration payloads — file 02 (DJIMR, HN-FREP-FR-041..075), file 03 (DMC
527, FR-086..115), file 04 (tarjetas 215/523, FR-121..148), file 05 (ISV
201/202, FR-151..187), file 06 (EEFF 535, FR-191..218), file 07 (ISR annual
102/103, FR-221..264), file 08 (GC events, FR-266..295), file 09 (selectivo,
FR-296..325), file 10 (TP 545 + informativas 541/542/543, FR-326..360) and
file 11 (contribuciones, FR-361..393) — all consumed **by id**, never restated; tax rates,
computation engines, sanctions, mora, prescription, buzón electrónico,
cuenta corriente and the February depuración ≤ 1 SMM — the Código Tributario
chassis of `../taxation/01_isr-framework.md` (HN-TAX-FR-001..045) and the
entero anchor of `../taxation/04_isr-withholding.md`
(HN-TAX-FR-150/151), consumed by id; the *comprobante de retención*
emission mechanics (`../e-invoicing/03_document-mechanics.md`,
HN-EINV-FR-139/140); and the SAR-236-2024 instrument itself (ACQUIRED W9 as `133_` + its
SAR-256-2024 date-fix `134_` — LB-001/LB-019 upgraded; the ordinals are
now statute-anchored, with the 535-approval limb adjudicated to DÉCIMO
QUINTO and the DMC 8-day chain re-seeded in FREP/03).

## 2. Legal Basis

Authority order (binding, per master evidence index): SAR-236-2024 (OVI/SW
channel chassis — UNACQUIRED, quoted only via the Ayudas) and
SAR-237/-238/-240-2024 (G 36,538, 20-may-2024 family) are primary for
declaration mechanics; per-código Ayudas/Generalidades are the field/flow
authority; `71_` Generalidades DMR is a compilation — cite **per row, never
§4** (R-H27); manuals are STALE vs gazettes where they conflict (R-H18).
CT = `03_` (D. 170-2016) via the manuals' own quotes. D-H1/D-H2/D-H3 bind
throughout (dated rows; period/*hecho-generador* resolution; filed-period
freeze D-H2.5; go-live ingestion D-H3).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo SAR-236-2024 — **ACQUIRED W9 as `133_` (Dado 10-may-2024, G 36,538 20-may-2024, vigencia publication-day; OVI implementation postponed to 28-jun-2024 by SAR-256-2024 `134_` EV134:EVID-505/506)**: PRIMERO/SEGUNDO/TERCERO a-b + DÉCIMO SÉPTIMO now verbatim-pinned (EV133:EVID-500..504) — PRIMERO creates the Oficina Virtual; SEGUNDO installs it as the "único medio" for elaboration/rectification/presentation + boletines + solicitudes + buzón; TERCERO a) ACUSE ELECTRÓNICO = the filing-proof electron ("no acuse ⇒ deemed NOT presented" carve-out = SÉPTIMO's Declaraciones-module registration); OCTAVO no-excuse rule (connection/password failures never justify extemporaneity); NOVENO all obligados regardless of categorización; VIGÉSIMO PRIMERO deroga the whole e-filing ancestry (DEI-en-línea G 31,608 / DET-Live G 33,327 / SAR-007-2017 G 34,353 / SAR-088-2019 G 34,977 / SAR-084-2021 G 35,596); DÉCIMO SEGUNDO/TERCERO pin the 53-determinativa + 31-informativa catalogs + 4 informes (532/533/534/**535**) + 7 facturación forms (SAR-920/924/926/927/928); DÉCIMO SÉPTIMO/OCTAVO + ANEXO I-III = the SW modality (523/524 SW-only; 527/116/111 dual, single-continuity) — PRIMERO: "Se crea la Oficina Virtual… como la herramienta que facilita a los obligados tributarios el cumplimiento voluntario…"; SEGUNDO: "Implementar la plataforma digital denominada 'Oficina Virtual', como único medio…"; TERCERO a/b define "Acuse Electrónico" and "Boletín de Pago" (with caducidad date); DÉCIMO SÉPTIMO: SW modality via "la plantilla proporcionada por el Servicio de Administración de Rentas (SAR)" | the chassis instrument now statute-anchored with its full operative content; dual-promulgation protocol (portal + Gaceta aviso) per CT Art. 13-4 explains SAR-256's pre-Gacette operative dates | `hn/sources/133_Acuerdo_SAR-236-2024_Oficina_Virtual.pdf` | SAR236-PRIMERO..VIGÉSIMO TERCERO pp.16-31 A. (EV133:EVID-500..504; manual quotes EV31:EVID-128; EV43:EVID-136) |
| LB-002 | SAR-236-2024, DÉCIMO OCTAVO + DÉCIMO NOVENO, as quoted in 32_/36_/45_ — DÉCIMO OCTAVO: informativas "podrán ser presentadas por Servicio Web u Oficina Virtual; no obstante, se deberá implementar el uso continuo de una sola modalidad"; DÉCIMO NOVENO: "Las Declaraciones Juradas Informativas deberán ser rectificadas haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original… Exceptuando las Declaraciones Juradas que fueron presentadas previo a la entrada en vigor del presente acuerdo" | Dual channel for listed informativas; continuous single modality; same-modality rectification with a pre-vigencia exception | `hn/sources/32_Ayuda_retencion_asalariados_111.pdf` + `hn/sources/45_Ayuda_DMC.pdf` | 32_ §I.4 footnote p.5; 45_ §2.5 p.24 (EV31:EVID-127; EV43:EVID-147) |
| LB-003 | Acuerdo SAR-237-2024 (10-may-2024, G 36,538), PRIMERO..QUINTO — "2. FORMA DE PRESENTACIÓN: I. … II. La presentación de esta declaración informativa deberá realizarse a través de la Oficina Virtual o del Servicio Web." "3. PLAZO DE PRESENTACIÓN: La … (DMC) debe presentarse dentro de los primeros cinco (05) días calendarios del mes siguiente…"; CUARTO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo No. CPAT-SG-073-2016"; QUINTO: "Quedan vigentes las demás disposiciones de los Acuerdos DEI SG-276-2015 y SAR-343-2019…" | DMC: dual channel OVI o SW, 5 días calendario deadline (current), CPAT-073-2016 repealed, survivors expressly kept — gazette text is the record over the manuals' "8 días" (R-H18) | `hn/sources/20_Acuerdo_SAR-237-2024_retenciones_mod.pdf` | 237-PRIMERO..QUINTO pp.3-4 (EV13:EVID-090) |
| LB-004 | Acuerdo SAR-238-2024 (DJIMR), QUINTO/SEXTO/SÉPTIMO — QUINTO: DJIMR "podrán presentarse a través de Servicio Web u Oficina Virtual; no obstante, los obligados tributarios deberán implementar una sola modalidad"; SEXTO: rectifications "deberán ser rectificadas haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original"; SÉPTIMO: rectificativas of original DJIMR "tendrán una vinculación directa con su Declaración Jurada Determinativa … declaraciones rectificativas de las Declaraciones Juradas Determinativas de oficio por parte del Servicio de Administración de Rentas, quedando en estado aceptada cuando el valor del impuesto a pagar sea mayor…, caso contrario… estado rechazo" | One-modality rule + same-modality rectification at chassis level; SAR's de-oficio supersession of the determinativa with aceptada/rechazo states | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-QUINTO..SÉPTIMO pp.4-5 (EV13:EVID-078/079) |
| LB-005 | Código Tributario (D. 170-2016), Art. 117 — rectificativa frame as quoted by the manuals — "Rectificativa per 'Artículo No.117 del Decreto No.170-2016 contentivo del Código Tributario'": two entry points, original values shown left / corrections right, originals tachados, purple "Rectificativa OT Aprobada OT" | Amended-declaration mechanics under CT Art. 117 — the statutory frame is owned by taxation/01 (HN-TAX-FR-035: reductions route through prior AT verification); this file owns only the declaration-surface engine | `hn/sources/56_Ayuda_casinos_504.pdf` (frame quoted family-wide) | 56_ §6 Funcionalidad (EV56:EVID-163; EV63:EVID-175) |
| LB-006 | CT Arts. 160/163 sanction hooks, as quoted in 69_ §7 and 71_ §7 — "no-presentation → 'sanción según el Artículo 160 del Código Tributario'; late payment → 'intereses conforme … el Artículo 163 del Código Tributario'"; 71_: "La no presentación de la Declaración Mensual de Retenciones (DMR) en la forma y plazo establecido, dará lugar a la sanción según el Artículo 160 del Código Tributario" | Non-filing multa (CT 160) and moratory interest (CT 163) attach to missed declaration deadlines — computation owned by taxation/01 (HN-TAX-FR-041/043), consumed by id | `hn/sources/69_Generalidades_ISV.pdf` + `hn/sources/71_Generalidades_DMR.pdf` | 69-§7 p.6; 71-§7 p.9 (EV43:EVID-149; EV31:EVID-129) |
| LB-007 | CT Arts. 2/142 credit-application anchors (manuals' glossary) — Section B credits: "'Importe a compensar' y 'Cesiones de crédito', se utilizará solo cuando se tengan créditos autorizados por el [SAR]" — glossary: compensación = CT Art. 2; cesiones de crédito = CT Art. 142; credits "se alimentan directamente de la cuenta corriente" | Compensation/cession of credits are permission-gated SAR operations feeding from the cuenta corriente — ledger owned by taxation/01 (HN-TAX-FR-036/039), consumed by id | `hn/sources/56_Ayuda_casinos_504.pdf` | 56_ §B Créditos + glossary (EV56:EVID-163; EV50:EVID-151) |
| LB-008 | D.L. 66-2015 Art. 2 + instrument chain DEI-SG-155-2011 (repealed) / SAR-007-2017, as recited by SAR-238-2024 — D.L. 66-2015 Art. 2: DMR "a más tardar dentro de los diez (10) días calendarios del mes siguiente en que se efectuó la retención"; DEI-SG-155-2011 (27-jul-2011) approved the DET-MR module → "Declaración Jurada Informativa DEI-540"; SAR-007-2017 (01-jun-2017) temporarily kept CPAT-era formats; DÉCIMO PRIMERO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo No. DEI-SG-155-2011" | The declaration-regime chain DMR→DJIMR (R-H31: same obligation, dated regime rows; DEI-SG-155-2011 = dead text, never an LB); SAR-007-2017 = transitional format instrument | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | considerandos pp.2-3; 238-NOVENO/DÉCIMO PRIMERO pp.3, 5 (EV13:EVID-080) |
| LB-009 | Monthly day-10 anchors: SAR-238-2024 SEGUNDO; Ayuda 201 §I.5; SAR-240-2024 XI — "dentro del plazo de los primeros diez (10) días calendarios del mes siguiente al que se efectuó la retención" (238-SEGUNDO); "La presentación y pago del Impuesto Sobre Ventas se debe realizar dentro de los primeros diez (10) días calendario del mes siguiente a aquel en que se efectuaron las ventas" (43_); tarjetas "dentro de los primeros diez (10) días calendario del mes siguiente al que se efectuó la liquidación" (240-XI) | The corpus-wide monthly 10-días-calendario anchor for the DJIMR/retentions family, ISV 201 and tarjetas 215/523 — presentation and payment share the deadline | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` + `hn/sources/43_Ayuda_ISV_201.pdf` + `hn/sources/19_Acuerdo_SAR-240-2024_ISV_tarjetas_mod.pdf` | 238-SEGUNDO p.3; 43-§I.5 p.5; 240-XI p.3 (EV13:EVID-076/089; EV43:EVID-137) |
| LB-010 | DMC deadline chain: DEI-SG-276-2015 numeral 3 → CPAT-SG-073-2016 PRIMERO → SAR-237-2024 PLAZO — 276 original: "antes de la Declaración Determinativa del Impuesto Sobre Ventas dentro de los primeros diez (10) días calendarios del mes siguiente…" (considerando: day-10 cluster of "Impuesto Sobre Ventas, Declaración Mensual de Retenciones (DMR) y Declaración Mensual de Compras (DMC)" saturated the systems); 073-PRIMERO: "dentro de los primeros veinte (20) días del mes siguiente…" (no "calendario"); 237: "cinco (05) días calendarios" (current) | The dated deadline chain 10d (2016-02) → 20d (2016-09) → 5d (2024-05-20) — R-H17; the manuals' "ocho (8) días" is stale (R-H18); the DMC-before-201 edge appears in the 276 original text | `hn/sources/15_Acuerdo_DEI-SG-276-2015_DMC.pdf` + `hn/sources/16_Acuerdo_CPAT-SG-073-2016_DMC_mod.pdf` + `hn/sources/20_Acuerdo_SAR-237-2024_retenciones_mod.pdf` | 276-SEGUNDO num.3; 073-PRIMERO p.2 + considerando; 237-PLAZO p.4 (EV13:EVID-082/083/090) |
| LB-011 | Selectivo family plazos (per-instrument hábiles vs calendario) — 203: "dentro de los primeros diez (10) días hábiles siguientes al mes a que corresponda la declaración… Artículo 8 del Decreto No 58-1982"; 211: "dentro de los primeros diez (10) días hábiles del mes siguiente a aquel en que se causó el hecho generador, según el Artículo 26 del Decreto No 17-2010"; 210/205/204: "dentro de los primeros diez (10) días calendario del mes siguiente… conforme el Artículo 38"; 259: "dentro de los primeros diez (10) días calendario del mes siguiente… Artículo 43 del Decreto No. 131-98" | The corpus's live hábiles/calendario split inside ONE form family — the proof that due-day semantics are per-instrument, never normalized (04_ OQ-3) | `hn/sources/50_Ayuda_selectivo_203.pdf` … `hn/sources/55_Ayuda_turistico_259.pdf` | each Generalidades p.4 (EV50:EVID-152..158) |
| LB-012 | Annual windows: SAR-619-2024 CUARTO; 545 plazo (Reglamento Art. 31 as quoted); RS 202 — 535: "periodicidad anual y debe presentarse del uno (01) de enero al treinta (30) de abril de cada año. Para las … con periodo fiscal especial, el vencimiento se establece en los tres (3) meses siguientes al cierre de su ejercicio fiscal"; 545: "el plazo … es el 30 de abril o siguiente día hábil de cada año. Para los … período fiscal especial … dentro de los 3 meses siguientes al cierre del período fiscal"; 202: "a más tardar el 31 de enero del año siguiente al período que se declara" | Annual fixed-date windows with next-hábil shift and the special-FY close+3m extension; RS 31-ene | `hn/sources/13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf` + `hn/sources/63_Ayuda_precios_transf_545.pdf` + `hn/sources/44_Ayuda_simplificado_202.pdf` | 619-CUARTO p.4; 63-f. Plazo p.5; 44-§III p.19 (EV13:EVID-073; EV63:EVID-177; EV43:EVID-141) |
| LB-013 | Código 541 socios/utilidades: ISR Art. 47 as quoted + Recomendación — Art. 47: "…estarán en la obligación de suministrar a la Administración Tributaria, antes del último día del mes de febrero de cada año, un informe que contenga el nombre de sus accionistas…"; Rec.: "a más tardar el ultimo día del mes de febrero del año siguiente al período que informa" | End-of-February annual inform — the statute says "antes del último día" while the manual says "a más tardar el último día" (Feb-27/28 vs Feb-28/29 drift, `64_ OQ-2` — both encoded as dated data, never silently resolved) | `hn/sources/64_Ayuda_socios_utilidades_541.pdf` | 64-I.6 p.6; III Rec.1 p.20 (EV63:EVID-181) |
| LB-014 | Código 542 alquileres: Acuerdo 034/99 Sexto as quoted + SAR-236-2024 Décimo Tercero + Recomendación — Channel/catalog anchor: "Acuerdo No. SAR-236-2024 Ordinal Décimo Tercero — Se establecen las siguientes Declaraciones Juradas Informativas con sus respectivos códigos … 29) 542-Declaracion Jurada Informativa Contratos de Alquileres"; cuerpo: "dentro de los tres meses siguientes al cierre del ejercicio fiscal"; Rec.: "plazo máximo de presentación al 30 de marzo del año siguiente al cierre" | First corpus sighting of SAR-236-2024's numbered informativa catalog; close+3m vs Mar-30 drift (`65_ OQ-2`) | `hn/sources/65_Ayuda_alquileres_542.pdf` | 65-I pp.4-5; 1.3 p.6; III Rec.1 p.17 (EV63:EVID-182) |
| LB-015 | Contribuciones family deadlines (502/503/504 monthly; 506/509/511/107 annual) — 502/503/504: "periodicidad mensual debiendo presentarse y pagarse dentro de los primeros diez días del mes siguiente de la generación de los ingresos" (qualifier calendario/hábiles NOT printed); 509/511: "anualmente a más tardar dentro de los (3) meses siguientes al cierre del período fiscal anterior" + Rec. "30 de marzo"; 509 CyC: "deben acreditar estos cambios financieros negativos… a más tardar el 31 de Mayo del mismo Ejercicio Fiscal, a través de un informe financiero elaborado por una Firma Auditora debidamente autorizada"; 107: due "en el plazo establecido por el Servicio de Administración de Rentas" (not printed) | The monthly trio's unstated day-kind defaults to calendario (04_ OQ-3 discipline, flagged); the annual quartet's close+3m vs Mar-30 drifts; the 509 audit report May-31 row | `hn/sources/57_Ayuda_telefonia_502.pdf` … `hn/sources/62_Ayuda_educativas_107.pdf` | §1-§5 + Recomendaciones of each (EV56:EVID-164..171) |
| LB-016 | Servicio Web plantilla two-stage validation (32_ pipeline; 45_ second-validation text) — "el formato de celda debe ser texto en cada fila llenada… la versión de las plantillas puede cambiar, según lo considere la Administración Tributaria… debe asegurarse de que sea la última versión"; "podrá visualizar el número de la orden de trabajo … puede ser recibida con o sin errores… 'Generar Informe' … hasta que la orden de trabajo sea recibida sin errores"; 45_: "Tenga en cuenta que esta constituye una primera validación del cumplimiento de las especificaciones técnicas. Una orden de trabajo finalizada sin errores no significa que la declaración ya haya sido presentada. Validación en la OVI: verifique en el buzón electrónico … la segunda validación"; "la estructura y los campos de la plantilla pueden ser modificados por la Administración Tributaria" | SW bulk channel: versioned text-cell plantillas; orden-de-trabajo acceptance loop; TWO validations (portal-side technical + OVI-side/buzón); plantilla mutability = version registry | `hn/sources/32_Ayuda_retencion_asalariados_111.pdf` + `hn/sources/45_Ayuda_DMC.pdf` | 32-§2.1C..2.2.1 pp.9-16; 527-§2.3 pp.16-19 (EV31:EVID-114; EV43:EVID-147) |
| LB-017 | Vector-fiscal alta + Nueva Declaración Eventual (Ayudas 31/33/34/35/37/38/39/40) — "Deberá acceder al botón 'Alta de Obligaciones'… seleccionar el impuesto y el periodo que dará alta a la obligación… '+Añadir Obligación'… 'Se ha agregado una obligación'"; "Esta opción se realizará en los casos que la obligación sea eventual; aplica para la presentación de ambas declaraciones Informativa/Determinativa… 'Nueva Declaración Eventual'… mostrará una pantalla con las diferentes declaraciones y sus códigos respectivos"; SW caveat: eventual "esta solo permitirá su ingreso mediante tarjeta" | Two on-ramps: per-taxpayer vector-fiscal alta (unregistered códigos never appear as pending) and the one-off eventual path (card-entry only, both declaration types) | `hn/sources/34_Ayuda_ret_dividendos_113.pdf` (+ same sections in 31/33/35/37/38/39/40_) | 34-§2.1B pp.9-11; 31-§2.4 pp.23-25; 38-§2.1 p.7 (EV31:EVID-126) |
| LB-018 | Chassis UI contract: juramento, acuse, estados, rechazo, Pagar/Boletín (43_/50_/56_/63-67_ family) — Login "con su Registro Tributario Nacional y contraseña tributaria"; tabs "Pendientes / Realizadas" filtered by "Nombre de la Declaración, Tipo de Declaración y Período"; submission modal "Jura la exactitud y veracidad de la presente declaración" with "Presentar declaración" / "No, en otro momento" (saves draft); "se genera el PDF del acuse … el documento muestra el código único de este y su respectivo QR" (45_ adds "el Código Seguro de Verificación (CSV) y el código QR"); estado "Original OT. Aprobada OT", rectified "Rectificativa OT Aprobada OT" "en color fuente morado", rechazo "Esta declaración queda rechazada. Debe ponerse en contacto con la Administración Tributaria"; payment "Pagar" (bank pick-list) or "Boletín de Pago" (print + ventanilla); "un histórico donde podrá verificar las declaraciones originales y rectificativas" | The lifecycle evidence shared by EVERY form family (ISV/retenciones/selectivo/contribuciones/annual informativas — chassis intros EV43:EVID-136, EV31:EVID-111, EV50:EVID-151, EV56:EVID-163, EV63:EVID-175, and the ISR-annual family EV29:EVID-091) | `hn/sources/43_Ayuda_ISV_201.pdf` + `hn/sources/50_Ayuda_selectivo_203.pdf` + `hn/sources/56_Ayuda_casinos_504.pdf` | 43-§2.1-2.3 pp.5-23; 50_ §§2.1-2.3; 56_ §6 (EV43:EVID-136; EV50:EVID-151; EV56:EVID-163; EV63:EVID-175) |
| LB-019 | Stale-channel/deadline guards: 72_ §4, 45_/72_ "8 días", 71_ §4 — **W9: the 8-day leg RETIRED from the guard list** (SAR-256-2024 `134_` makes 8 días the CURRENT DMC plazo from the august-2024 period, and the OVI-only prints match the cutover — FREP/03 FR-091/092 re-seeded); remaining guards: 71_ §4's "único medio Oficina Virtual" stays OVERBROAD for the SW-only codes (523/524) and the dual-modality set; 45_/72_'s INSTRUMENT ATTRIBUTION (SAR-237) stays imprecise (the 8d = SAR-256's rewrite) — value loadable, attribution corrected in-row | `hn/sources/72_Generalidades_DMC.pdf` + `hn/sources/45_Ayuda_DMC.pdf` + `hn/sources/71_Generalidades_DMR.pdf` | 72-§2/§4; 45-§I.5 p.6; 71-§4 p.8 (EV43:EVID-143/144; EV31:EVID-125) |
| LB-020 | Annual period-key encoding + alta year (63_) — Search: "en la casilla 'Período' deberá seleccionar 202501"; alta: "en la casilla 'Año desde' deberá ingresar el período 2025 … 'Añadir obligación'"; rectification/consult screens likewise "del período fiscal 202501" | ANNUAL declarations are keyed by the six-digit YYYYMM period code (YYYY + "01" month-tag) — same OVI convention as monthly periods; the alta flow carries an Año-desde value | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-II.3 p.12; alta p.9; consult pp.78-79 (EV63:EVID-175/177) |
| LB-021 | Extemporaneous multa + fallas-de-conexión boilerplate (45_/56_) — "Cuando la declaración sea extemporánea, indicará la multa y los intereses correspondientes."; "Fallas de conexión" and lost passwords never justify extemporaneity; compliance = possession of the acuse electrónico | Late filings auto-carry multa + intereses surfaced through the same Pagar/Boletín pair (computation consumed from taxation/01 by id); connectivity failures are never a defense | `hn/sources/45_Ayuda_DMC.pdf` + `hn/sources/56_Ayuda_casinos_504.pdf` | 527-§2.5; 56_ boilerplate (EV43:EVID-147; EV56:EVID-163) |

## 3. Functional Requirements

### 3.1 The declaration lifecycle chassis (OVI)

- **HN-FREP-FR-001:** The system shall model every HN fiscal declaration on
  ONE chassis record keyed (company, form código, tipo
  informativa/determinativa, period) with the OVI period-key convention
  YYYYMM — monthly periods YYYYMM, annual periods YYYY + "01" (e.g. FY2025
  = 202501) — and the taxpayer identity resolved from the RTN +
  *contraseña tributaria* (tax password) login profile, never free-typed
  per declaration. (LB-018; LB-020; EV43:EVID-136; EV63:EVID-175/177)
- **HN-FREP-FR-002:** The system shall implement the lifecycle state
  machine *alta/pendiente* → *borrador* (draft, saved via the "No, en otro
  momento" path) → juramento → presentada → acuse → estado pill, with the
  "Pendientes / Realizadas" work queues filtered by Nombre de la
  Declaración × Tipo de Declaración × Período and the "Realizar" action
  opening the form. (LB-018; EV43:EVID-136; EV50:EVID-151; EV56:EVID-163)
- **HN-FREP-FR-003:** The system shall require the *juramento* (sworn
  attestation) step before any submission — the attestation modal "Jura la
  exactitud y veracidad de la presente declaración" with explicit
  Presentar/No-en-otro-momento choices — and shall never transmit a
  declaration record whose attestation is absent.
  (LB-018; EV43:EVID-136; EV50:EVID-151)
- **HN-FREP-FR-004:** The system shall generate and archive the *acuse
  electrónico* (electronic acknowledgment) PDF for every presented
  declaration, carrying the código único + QR code (form 527 variant: the
  Código Seguro de Verificación CSV + QR), and shall record that the acuse
  is proof of presentation but NOT concurrence — SAR reserves its
  determination faculty ("este acuse no implica manifestación de
  conformidad con el contenido"). (LB-001; LB-018;
  EV31:EVID-128; EV43:EVID-136/147)
- **HN-FREP-FR-005:** The system shall maintain the estado registry per
  declaration — "Original OT. Aprobada OT", purple "Rectificativa OT
  Aprobada OT" for rectified filings — with the histórico of originals and
  rectificativas per period and the Excel detail download surface.
  (LB-018; EV43:EVID-136; EV63:EVID-175)
- **HN-FREP-FR-006:** The system shall treat rechazo ("Esta declaración
  queda rechazada. Debe ponerse en contacto con la Administración
  Tributaria") as a TERMINAL state: no automated retry, no silent
  resubmission; the record is frozen and surfaced for operator contact
  with the AT. (LB-018; EV43:EVID-136; EV31:EVID-111)
- **HN-FREP-FR-007:** The system shall expose the dual payment route on
  every determinativa — "Pagar" (online bank pick-list, SAR-certified
  banks) or "Boletín de Pago" (print + ventanilla payment) — and shall
  store the Boletín's *fecha de caducidad* (expiry date) as payment-window
  data; code-specific routing exceptions (e.g. 215's Banco Central row)
  are owned by their per-código files and consumed by id.
  (LB-001; LB-018; EV43:EVID-136; EV31:EVID-111; EV50:EVID-151)
- **HN-FREP-FR-008:** The system shall monitor the *buzón electrónico*
  (electronic mailbox) for second-validation error reports (the SW
  pipeline's OVI-side validation) and attach error-report PDFs to the
  declaration record — the enrollment/notification frame itself consumed
  from taxation/01 by id (HN-TAX-FR-033), never re-derived here.
  (LB-016; EV31:EVID-114; EV43:EVID-147)

### 3.2 Channels: OVI o Servicio Web, sticky single modality

- **HN-FREP-FR-009:** The system shall implement the two filing channels
  over ONE field contract: OVI interactive entry (*fichas*/cards) and the
  SW batch plantilla — "los campos a digitar son los mismos que se
  contemplan en la plantilla del portal web" — with the channel recorded
  on every filing. (LB-003; LB-016;
  EV13:EVID-090; EV31:EVID-114; EV43:EVID-143/147)
- **HN-FREP-FR-010:** The system shall enforce the STICKY single-modality
  rule: where a declaration family is dual-channel ("podrán ser
  presentadas por Servicio Web u Oficina Virtual; no obstante, se deberá
  implementar el uso continuo de una sola modalidad" — SAR-236-2024 DÉCIMO
  OCTAVO; SAR-237-2024 numeral 2.II; SAR-238-2024 QUINTO), the modality
  first used binds subsequent filings of that family for the taxpayer;
  switching requires an explicit configuration action, never a silent
  channel change. (LB-002; LB-003; LB-004;
  EV31:EVID-127; EV13:EVID-078/090)
- **HN-FREP-FR-011:** The system shall carry the per-código channel matrix
  as DATED operational reference data — informativa channel set per código
  (e.g. 111/113/115/116 dual per the 37_ print; 112/136/138/217 OVI-only;
  523 SW-only; 215 OVI-only) with the determinativa-OVI invariant — never
  encoding any "único medio OVI" blanket sentence (R-H27), and carrying
  the unresolved 135 channel conflict (37_ vs 39_) as flagged data until
  SAR-236-2024 is acquired. (LB-002; LB-019; EV31:EVID-121/125/127;
  EV43:EVID-143)
- **HN-FREP-FR-012:** The system shall implement the SW plantilla pipeline:
  download the latest plantilla version per impuesto/periodo (text-format
  cells), fill, upload, receive the *orden de trabajo* (work order) with
  con/sin errores state, download the error-report PDF via "Generar
  Informe", and loop until the orden is received sin errores.
  (LB-016; EV31:EVID-114; EV43:EVID-147)
- **HN-FREP-FR-013:** The system shall implement the TWO-STAGE validation
  state machine: stage 1 = portal-side technical validation of the plantilla
  (an orden "recibida sin errores" does NOT mean presented); stage 2 =
  OVI-side validation whose error reports land in the buzón electrónico —
  states en-proceso / con-errores / sin-errores / presentada, with the
  second-stage check as an explicit verification step before a filing is
  marked presented. (LB-016; EV31:EVID-114; EV43:EVID-147)
- **HN-FREP-FR-014:** The system shall maintain a plantilla VERSION
  registry per impuesto ("la versión de las plantillas puede cambiar…
  asegurarse de que sea la última versión"; "la estructura y los campos de
  la plantilla pueden ser modificados por la Administración Tributaria"):
  every export pins the version used, and a stale version blocks upload
  with a re-download instruction. (LB-016; EV31:EVID-114; EV43:EVID-147)

### 3.3 Vector-fiscal on-ramps: alta and Nueva Declaración Eventual

- **HN-FREP-FR-015:** The system shall gate the per-código pendiente
  calendar on the company's *vector fiscal* registration state: a código
  not *dado de alta* never appears as pending; the Alta de Obligaciones
  flow (impuesto + "Año desde" + "Añadir obligación") is modeled as a
  first-class operation on the obligation registry.
  (LB-017; LB-020; EV31:EVID-126; EV63:EVID-175)
- **HN-FREP-FR-016:** The system shall offer the *Nueva Declaración
  Eventual* one-off path for obligations not registered or not recurrent —
  card-entry only ("esta solo permitirá su ingreso mediante tarjeta"),
  covering both informativa and determinativa — as the mandatory route for
  event-driven filings (e.g. código 138 transaction-triggered
  declarations, file 02 FR-063 by id). (LB-017; EV31:EVID-126/120)
- **HN-FREP-FR-017:** The system shall expose an alta-state reconciliation
  surface: expected obligations (per taxpayer segment and engines) vs
  vector-fiscal alta state, flagging missing altas so the operator can
  register them before the filing window closes.
  (LB-017; EV31:EVID-126)

### 3.4 Rectificativa: generic lifecycle, freeze and supersession

- **HN-FREP-FR-018:** The system shall implement the generic rectificativa
  (amended declaration) engine: a NEW record superseding the frozen
  original snapshot, editing original values side-by-side (originals left,
  corrections right), flipping the estado to the purple "Rectificativa OT
  Aprobada OT", within the CT Art. 117 frame consumed from taxation/01 by
  id — HN-TAX-FR-035 (rectifications that REDUCE tax or INCREASE a credit
  route through prior AT verification, never silently re-booked).
  (LB-005; EV56:EVID-163; EV43:EVID-136; EV63:EVID-175)
- **HN-FREP-FR-019:** The system shall route rectifications through the
  SAME modality as the original declaration (SAR-236-2024 DÉCIMO NOVENO)
  with the pre-vigencia exception as a dated flag: declarations presented
  before SAR-236-2024's entry into force are exempt from the
  same-modality requirement. (LB-002; LB-004;
  EV31:EVID-127; EV13:EVID-078; EV43:EVID-147)
- **HN-FREP-FR-020:** The system shall enforce the filed-period freeze
  (D-H2.5): periods covered by a presented declaration are
  write-protected — posting, editing or canceling source records in a
  filed período is blocked, and corrections flow exclusively through the
  rectificativa flow from the frozen snapshot (per-family move freezes —
  e.g. file 02 FR-071 retention moves — consume this engine by id).
  (LB-004; LB-005; EV13:EVID-079; EV31:EVID-111)
- **HN-FREP-FR-021:** The system shall import extern supersession states:
  where SAR rectifies a filed declaration *de oficio* (the DJIMR
  determinativa propagation — aceptada only when tax payable increases,
  else rechazo), the client-side chain records the SAR-rectified state
  against the frozen snapshot and reconciles (file 02 FR-047/FR-048
  consume this engine by id). (LB-004; EV13:EVID-079; EV31:EVID-111)
- **HN-FREP-FR-022:** The system shall surface the extemporáneo regime on
  late filings: multa + intereses computed by the CT engines consumed from
  taxation/01 by id (HN-TAX-FR-041/042/043) and payable through the same
  Pagar/Boletín pair; connection failures and lost passwords are recorded
  as never justifying extemporaneity. (LB-006; LB-021;
  EV43:EVID-147; EV31:EVID-111; EV56:EVID-163)
- **HN-FREP-FR-023:** The system shall block a second original per
  RTN × código × period (one consolidated filing per taxpayer-period —
  branches consolidate; "no podrán presentar más de una declaración
  original o rectificativa"), with a structural unique constraint rather
  than a UI advisory. (LB-016; EV43:EVID-147)

### 3.5 The shared due-day engine (fiscal calendar)

- **HN-FREP-FR-024:** The system shall encode per-instrument due-day
  semantics as DATED configuration rows (valid_from/valid_to, additive,
  never replaced — D-H2): day count + day kind, where the kind is días
  CALENDARIO by default and días hábiles ONLY where the instrument says so
  (`04_ OQ-3` discipline; kin HN-TAX-FR-151) — the selectivo family's
  hábil/calendario split (203/211 hábiles vs 204/205/210/259 calendario)
  is the corpus proof and is never normalized.
  (LB-011; EV50:EVID-152..158; EV43:EVID-149)
- **HN-FREP-FR-025:** The system shall maintain ONE consolidated
  fiscal-calendar model (the wave-shared `l10n_hn.fiscal.calendar` row
  family) that every S-HN3 sibling file's deadline rows feed: each row =
  código/obligation + due rule + day kind + instrument + valid_from/to +
  owner reference; rows are seeded by their owning file (02: DJIMR; 03:
  DMC; 04: 215/523; 05: 201/202; 06: 535; 07: annual package; 08:
  GC-events 119/120/152/154 — V-HN1 omission fix: per-transaction
  10-días-hábiles BPL clock (FR-267), 152 tercer-día (FR-284), 120
  cadence rows (FR-282), 154 config-gap row (FR-293); 09:
  selectivo; 10: 541/542/543/545; 11: contribuciones) and this file owns
  ONLY the engine and the model, never the siblings' instruments.
  (LB-009; LB-010; EV13:EVID-076/082/090)
- **HN-FREP-FR-026:** The system shall compute monthly deadlines as "first
  N days of the following month" windows anchored to the declared period
  (retention month / purchase month / sales month / liquidation month —
  per instrument), counting días hábiles against a Honduran holiday
  calendar carried as configuration where the instrument says hábiles, and
  shall resolve the applicable row by the period/*hecho generador* date —
  never "today" (D-H2). (LB-009; LB-010; LB-011;
  EV13:EVID-076/090; EV50:EVID-152..158)
- **HN-FREP-FR-027:** The system shall compute annual deadlines as fixed
  windows: Jan-1 → Apr-30 with next-hábil shift when Apr-30 falls on a
  non-working day; the RS 202 31-ene row; end-of-February rows
  (leap-year-aware); close + 3 months rows for special fiscal periods
  (close date consumed from taxation/01 HN-TAX-FR-016 by id); and the
  509 CyC audit-report May-31 row.
  (LB-012; LB-013; LB-015; EV13:EVID-073; EV63:EVID-177/181;
  EV56:EVID-167)
- **HN-FREP-FR-028:** The system shall model PREREQUISITE EDGES on the
  fiscal calendar — declaration A must be presented before declaration B
  for the same period — with enforcement semantics owned by the consuming
  file: DMC-before-201/DMR (file 03 FR-093; the 276 original text already
  placed the DMC "antes de la Declaración Determinativa"), 523-before-215
  (file 04 FR-145), EEFF-535-before-DJ-ISR FY2024+ (file 06 gate, consumed
  by file 07). (LB-010; LB-012; EV13:EVID-073/082; EV43:EVID-137)
- **HN-FREP-FR-029:** The system shall encode deadline DRIFT as dated data
  plus an open question — never resolving silently: 541 "antes del último
  día" (statute) vs "a más tardar el último día" (manual) = Feb-27/28 vs
  Feb-28/29; 542/509 "tres meses siguientes al cierre" vs the manuals'
  "30 de marzo"; the 45_/72_ "ocho (8) días" prints are NEVER loadable
  (R-H18 — the gazette's 5 días is the record).
  (LB-013; LB-014; LB-015; LB-019;
  EV63:EVID-181/182; EV56:EVID-167/171; EV43:EVID-144)
- **HN-FREP-FR-030:** The system shall BLOCK any deadline computation
  whose instrument row is missing for the resolved period (explicit
  configuration flag — e.g. the 502/503/504 monthly rows' unstated
  day-kind defaults to calendario ONLY as a flagged default), never
  guessing, defaulting to a sibling instrument's semantics, or falling
  back to a superseded row (D-H2 never-guess; availability-gap kin of
  HN-TAX-FR-124). (LB-009; LB-015; EV13:EVID-083/090; EV56:EVID-171)

### 3.6 D-H3 go-live reconciliation surface

- **HN-FREP-FR-031:** The system shall implement the extern SAR-filing
  registry for go-live (D-H3): the declarations the PREVIOUS system filed
  with SAR — DMC compras, DJIMR/DMR retenciones, DJI mensual — imported as
  FROZEN authoritative aggregates per código × period (acuse identifiers
  where available), resolved to their own regime rows (DMR pre-2024 /
  DJIMR post-May-2024 per R-H31; historical DMC deadlines per their dated
  chain), never editable and never re-filed.
  (LB-008; LB-009; LB-010; EV13:EVID-076/080/082)
- **HN-FREP-FR-032:** The system shall produce the go-live DELTA report:
  Odoo-side recomputed period aggregates vs the imported extern filings —
  SAR's filed declarations are the external truth (D-H3.2) — flagging
  every mismatch (period, código, base, tax) for reconciliation before the
  first Odoo-filed period; the DMC-specific delta surface of file 03
  (FR-110) consumes this engine by id.
  (LB-008; LB-009; EV13:EVID-076/082)

## 4. Data Model

Machine-readable sidecars: none of this file's own — the fiscal-calendar
rows are seeded by the sibling files (file 02 seeds
`djimr_retention_codes.csv` for its catalog; files 03-09 seed their
deadline rows); this file owns the model, not the data. Layer semantics:
Odoo-side filing/state machinery (wave default `odoo`; see §5).

**Declaration chassis (lifecycle):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.declaration (new) | company_id, código, tipo, period_key (YYYYMM), fiscal_year | m2o/char/select/char | tipo: informativa · determinativa; annual keys YYYY+"01" | FR-001 |
| l10n_hn.declaration | state, draft_payload, juramento_at, presented_at | select/json/datetime | state: alta · pendiente · borrador · jurada · presentada · acuse · rectificativa · rechazada (terminal) | FR-002, FR-003, FR-005, FR-006 |
| l10n_hn.declaration | acuse_codigo_unico, acuse_csv, acuse_qr, acuse_pdf, estado_pill | char/char/binary(char)/char | pill: "Original OT. Aprobada OT" · "Rectificativa OT Aprobada OT" (morado) · rechazo; acuse ≠ conformidad note | FR-004, FR-005 |
| l10n_hn.declaration | channel, modality_locked, original_id, rectification_diff | select/boolean/m2o/json | channel: ovi_card · ovi_ficha · sw_plantilla; same-modality routing + pre-236-2024 exception flag | FR-009, FR-010, FR-018, FR-019 |
| l10n_hn.declaration | payment_route, boletin_id, boletin_caducidad | select/char/date | route: pagar_online · boletin; caducidad = payment-window data | FR-007 |
| l10n_hn.declaration | buzón_error_report_ids, ot_number, ot_state | m2m/char/select | ot_state: en_proceso · con_errores · sin_errores · presentada (two-stage) | FR-008, FR-013 |
| l10n_hn.declaration | extemporaneous_multa_ids, intereses_ids | m2m | CT engines consumed from taxation/01 by id (FR-041/042/043) | FR-022 |
| _uniqueness_ | unique(company, código, tipo, period_key, generation) | constraint | ONE original per RTN × código × period; branches consolidate | FR-023 |

**Channels, plantillas, on-ramps:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.declaration.channel.matrix (new) | código, tipo, channel_set, valid_from, valid_to, conflict_flag | select[]/date/boolean | e.g. 111 informativa {ovi,sw}; 112 {ovi} (anomaly flag); 523 {sw}; determinativa {ovi} invariant; 135 conflict UNRESOLVED (37_ vs 39_) | FR-011 |
| l10n_hn.plantilla.version (new) | impuesto, version, structure_hash, valid_from, downloaded_at | char/date | always-latest enforcement; stale version blocks upload | FR-012, FR-014 |
| l10n_hn.obligation.alta (new) | company_id, código, year_from, state, eventual_only | m2o/char/int/select/boolean | vector-fiscal mirror; gates the pendiente calendar; eventual path = card-only | FR-015..FR-017 |

**The fiscal calendar (due-day engine — wave-shared model owned here):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.fiscal.calendar (new, wave-shared) | obligation (código/form family), due_rule, day_count, day_kind, window_open, window_close, next_habil_shift, instrument, valid_from, valid_to, owner_ref | char/select/int/select/date/date/boolean/char/date/date/char | due_rule: first_n_days_next_month · fixed_window · close_plus_3m · fixed_date; day_kind: calendario · hábiles (per instrument, 04_ OQ-3); rows seeded by owner files | FR-024..FR-027 |
| l10n_hn.fiscal.calendar.prerequisite (new) | predecessor, successor, enforcement, owner_ref | m2o/m2o/select/char | enforcement: hard · soft · advisory (semantics owned by consumers: file 03 FR-093, file 04 FR-145, file 06 gate) | FR-028 |
| resource.calendar.leaves (HN config) | holiday rows for hábiles counting | date | Honduran holiday calendar as configuration (never hardcode) | FR-026 |

**Corpus deadline inventory (seed rows — owners by id; evidence-anchored):**

| Obligation (código) | Cadence / deadline (dated) | day_kind | Instrument chain | Owner (by id) | Evidence |
|---|---|---|---|---|---|
| DJIMR per-código (111-113, 115-116, 118, 122-134, 135-138, 217, 254) | monthly, first 10 días of M+1 (retention month) | calendario | D.L. 66-2015 Art. 2 → SAR-238-2024 SEGUNDO | file 02 FR-041/FR-042 | EV13:EVID-076/080 |
| 138 event-driven | transaction + 10d vs month + 10d duality (open, modeled both) | calendario | D. 273-2013 → Eficiencia Art. 14 vs SAR-238-2024 | file 02 FR-063 (OQ-016 there) | EV31:EVID-120 |
| ISV 201 | monthly, first 10 días of M+1 (sales month); presentation AND payment | calendario | Ley ISV D.L. 24 + SAR-236-2024 | file 05 FR-152 | EV43:EVID-137/149 |
| DMC 527 | monthly: 10d (2016-02) → 20d (2016-09) → **5d (2024-05-20, current)**; NEVER 8d | calendario (20d window default calendario — OQ-002) | DEI-SG-276-2015 → CPAT-SG-073-2016 (repealed) → SAR-237-2024 | file 03 FR-091/FR-092 (R-H17/R-H18) | EV13:EVID-082/083/090 |
| Tarjetas 215 / 523 | monthly, first 10 días of M+1 (retention month / liquidation month) | calendario | Ley ISV Art. 8 + DEI-9382-J-2003 + SAR-240-2024 XI | file 04 FR-144 | EV13:EVID-088/089 |
| Selectivo 203, 211 | monthly, first 10 días of M+1 | **hábiles** | D. 58-1982 Art. 8; D. 17-2010 Art. 26 | file 09 FR-302 | EV50:EVID-152/153/158 |
| Selectivo 204, 205, 210; tasa 259 | monthly, first 10 días of M+1 | calendario | D. 17-2010 Art. 38; D. 131-98 Art. 43 | file 09 FR-302 | EV50:EVID-154..158 |
| Annual package (ISR DJ 102/103 + AS/ATN + GC annual + package members 506/107) | annual, Jan-1 → Apr-30 (next hábil if weekend); special FY close + 3m | calendario | ISR Art. 28 + SAR-236/619-2024 | file 07 FR-221 (window rows) | EV13:EVID-073; EV63:EVID-177 |
| EEFF 535 | annual, Jan-1 → Apr-30; special FY close + 3m | calendario | SAR-619-2024 CUARTO | file 06 FR-193/FR-196 | EV13:EVID-073; EV63:EVID-184 |
| RS 202 | annual, 31-ene of the following year | calendario | Ley ISV Art. 11-A | file 05 FR-180 | EV43:EVID-141/149 |
| 541 socios/utilidades | annual, end-February (Feb-27/28 vs Feb-28/29 drift — OQ-011) | calendario | ISR Art. 47 + Acuerdo 034/99 family | file 10 FR-350 (its OQ-012) | EV63:EVID-181 |
| 542 alquileres | annual, close + 3m vs "30 de marzo" (drift — OQ-012) | calendario | Acuerdo 034/99 Sexto + SAR-236-2024 Décimo Tercero | file 10 FR-355 (its OQ-016) | EV63:EVID-182 |
| 543 municipalidades | annual, close + 3m (no explicit day printed) | calendario | Acuerdo 034/99 family | file 10 FR-359 | EV63:EVID-183 |
| 545 precios de transferencia | annual, Apr-30 or next hábil; special FY close + 3m | calendario | Reglamento PT Art. 31 (Acuerdo 027-2015) | file 10 FR-328 | EV63:EVID-177 |
| Contribuciones 502/503/504 | monthly, first 10 días of M+1 (qualifier NOT printed — default calendario, OQ-014) | calendario (flagged default) | D. 105-2011 Arts. 13/23 + Acuerdo 1775-2011 | file 11 FR-374 (R-H28) | EV56:EVID-164..166/171 |
| 506 / 509 / 511 | annual, close + 3m (Rec. prints "30 de marzo" — drift, OQ-013) | calendario | D. 166-2011 + Acuerdo 1775-2011 Art. 40; D. 53/92-2015 Art. 4; D. 131-2018 Art. 3 | file 11 FR-376/381/385 (its OQ-005) | EV56:EVID-167..171 |
| 509 CyC audit report | annual, May-31 (fuerza-mayor accreditation) | calendario | D. 92-2015 (as quoted 59_) | file 11 FR-380 | EV56:EVID-167 |
| 107 educativas | annual; due date "establecido por el SAR" — NOT printed (no independent row) | — | D. 17-2010 Art. 6 + Acuerdo 1121-2010 Art. 14 | file 11 FR-389 | EV56:EVID-170/171 |

**Go-live extern registry (D-H3):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.extern.filing (new) | company_id, código, period_key, regime (dmr · djimr · dmc_chain), aggregates (json), acuse_ref, source_system, is_frozen | m2o/char/select/json/char/char/boolean | the PREVIOUS system's SAR filings as authoritative aggregates; never editable, never re-filed | FR-031 |
| l10n_hn.extern.filing.delta (new) | filing_id, recomputed_aggregate, delta_lines, status | m2o/json/json/select | status: match · mismatch · unresolved; consumed by file 03 FR-110 by id | FR-032 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = filing/state machinery in the LGPL
client. No SaaS rows are introduced: HN has no transmission regime (W3 E8
lead 1 — SEE technical docs unpublished), so the chassis is an export/import
contract against SAR's OVI/SW surfaces, not a government API integration;
`shared` marks the calendar/period concepts reused by sibling files and
taxation. Model names stable across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | shared | l10n_hn.declaration | period_key YYYYMM | Annual keys YYYY+"01" (LB-020); consumed by all sibling files by id |
| FR-002, FR-003 | odoo | l10n_hn.declaration + mail template (attestation wizard) | state, juramento_at | Draft = "No, en otro momento" semantics; wizard blocks submit without attestation |
| FR-004, FR-005 | odoo | l10n_hn.declaration + ir.attachment | acuse_* fields | PDF + código único/CSV + QR archived; OQ-006 for artifact format details |
| FR-006 | odoo | l10n_hn.declaration | state=rechazada | Terminal; no cron retry — operator task generated |
| FR-007 | odoo | l10n_hn.declaration + account.payment | payment_route, boletin_caducidad | Payment posting stays standard Odoo; boletín caducidad drives overdue flag (OQ-010) |
| FR-008 | odoo | l10n_hn.declaration + buzón import job | buzón_error_report_ids | CT frame consumed from taxation/01 FR-033 by id |
| FR-009..FR-011 | odoo | l10n_hn.declaration.channel.matrix | channel_set rows dated | D12: channel rows are operational DATED DATA (Ayudas undated, ≥2024); 135 conflict + 112 anomaly flagged (OQ-001/OQ-004); R-H27 lint |
| FR-012..FR-014 | odoo | l10n_hn.plantilla.version + export mapper | version pinning | Text-cell formatting (LB-016); two-stage states incl. buzón second validation; stale-version upload block |
| FR-015..FR-017 | odoo | l10n_hn.obligation.alta | alta gating | Pendiente queue derived from alta state; eventual = card-only path (138 consumption by id) |
| FR-018..FR-020 | odoo | l10n_hn.declaration (original_id, diff) + base write-protection | freeze engine | D-H2.5: filed periods write-protected at move level via consuming files (e.g. file 02 FR-071); CT Art. 117 + HN-TAX-FR-035 by id |
| FR-021 | odoo | l10n_hn.declaration | extern supersession import | SAR de-oficio states (aceptada/rechazo) synced; file 02 FR-047/048 consume |
| FR-022 | odoo | l10n_hn.declaration + account.move.line (multa/intereses) | extemporaneous hookup | Engines consumed from taxation/01 by id (FR-041/042/043); fallas-de-conexión note recorded |
| FR-023 | odoo | SQL constraint on l10n_hn.declaration | unique original | Branches consolidate (LB-016); rectificativa generation counter |
| FR-024..FR-027 | shared | l10n_hn.fiscal.calendar (+ resource.calendar.leaves config) | due_rule rows | D12: every row dated (valid_from/to) with instrument; hábil counting needs holiday config; resolution by period date (D-H2). Model name is the wave-shared one already referenced by taxation/04 FR-150/151 mapping and files 03/05/09 |
| FR-028 | shared | l10n_hn.fiscal.calendar.prerequisite | edges | Enforcement owned by consumers: file 03 FR-093 (DMC-first, R-H36), file 04 FR-145 (soft), file 06 gate (hard FY2024+) |
| FR-029, FR-030 | shared | l10n_hn.fiscal.calendar | drift rows + missing-row block | Both prints stored with OQ flags (OQ-011..OQ-013); 8d row structurally unloadable (R-H18); never-guess block (kin HN-TAX-FR-124) |
| FR-031, FR-032 | odoo | l10n_hn.extern.filing (+ delta) | frozen aggregates | D-H3.2: previous system's SAR filings = authoritative aggregates; D18 kin (`is_historical`); file 03 FR-110 consumes by id |

Version-regime notes (D12): the chassis instruments themselves carry the
2024 regime boundary — SAR-236/237/238/240-2024 all effective from
publication (20-may-2024, G 36,538) with the DÉCIMO NOVENO pre-vigencia
rectification exception encoded as a dated flag (FR-019); the DMC deadline
chain and the DMR→DJIMR regime rows are the other dated boundaries (R-H17 /
R-H31). Channel matrix and manual-sourced values are print-vintage DATED
DATA (Ayudas undated except 43_/45_/54_/65_ prints 2026).

## 6. Acceptance Criteria

- **AC-001:** Given a monthly DJIMR-112 filing for January 2026, then the
  declaration record keys period 202601; given the annual 545 for FY2025,
  then the record keys 202501 (FR-001).
- **AC-002:** Given an operator completing a 201 determinativa, then
  submission is impossible without the juramento step, and on success the
  acuse PDF stores the código único + QR and the estado pill reads
  "Original OT. Aprobada OT" (FR-003, FR-004, FR-005).
- **AC-003:** Given a company that filed January's 111 informativa via SW
  plantilla, then a February attempt through OVI cards is blocked with a
  modality-lock message, and the March rectification routes through SW
  (FR-010, FR-019).
- **AC-004:** Given a plantilla upload failing stage-1 validation, then the
  orden de trabajo shows "con errores", the error PDF is downloadable, and
  the declaration is NOT presented; given a clean orden, then presentation
  still waits for the buzón second-validation check before state
  "presentada" (FR-012, FR-013).
- **AC-005:** Given a código not dado de alta in the vector fiscal, then it
  never appears in Pendientes; given a one-off 138 retention event, then
  the Nueva Declaración Eventual path creates the declaration card-only
  (FR-015, FR-016).
- **AC-006:** Given a presented DJIMR original for 202601 and a correction
  request, then the original snapshot is write-protected, the rectificativa
  record shows the side-by-side diff with originals tachados and the purple
  "Rectificativa OT Aprobada OT" pill, and a tax-REDUCING rectification
  additionally carries the prior-AT-verification flag (FR-018, FR-020).
- **AC-007:** Given SAR's de-oficio rectification of a filed determinativa
  importing as aceptada (tax increased), then the extern supersession state
  replaces the assumed-original state on the chain; given a decrease, then
  the imported state is rechazo and the chain surfaces the contact-AT task
  (FR-021).
- **AC-008:** Given purchase month May 2024, then the DMC deadline computes
  2024-06-05 (5 días calendario row, valid_from 2024-05-20) and the 201
  deadline computes 2024-06-10; given a cigarette declaration for the same
  month, then the 211 deadline counts 10 días hábiles skipping weekends
  and configured holidays (FR-026, FR-024).
- **AC-009:** Given purchase month February 2024, then the DMC deadline
  resolves the 20-day row (2016-09 → 2024-05-19); given any attempt to load
  an "8 días" row from the manuals, then the load is rejected (R-H18
  guard) (FR-026, FR-029).
- **AC-010:** Given FY2025 with an Apr-30 2026 falling on a Thursday, then
  the annual package window closes 2026-04-30; given a special fiscal
  period closing 2026-03-31, then the window closes 2026-06-30 (close+3m)
  (FR-027).
- **AC-011:** Given the 541 rows for FY2025, then both the
  statute reading (Feb-27/28) and the manual reading (Feb-28/29) exist as
  dated rows with the drift OQ attached, and the operative default is the
  manual row flagged — never a silently merged value (FR-029, OQ-011).
- **AC-012:** Given an obligation whose instrument prints no SAR-published
  due date (the 107 case), then the engine raises a missing-row
  configuration flag — never a guessed date and never engine-side Apr-30
  inference (107 reaches the annual window only through file 11 FR-389/390's
  dated package-membership config) (FR-030).
- **AC-013:** Given a go-live import of the previous system's 2023 DMR and
  DMC filings, then they load as frozen extern aggregates under their own
  regime rows (DMR; DMC 20-day chain), and the delta report flags any
  Odoo-recomputed period aggregate that differs (FR-031, FR-032).
- **AC-014:** Given a late DJIMR filing for 202601 presented 2026-02-14,
  then the extemporaneous multa and intereses surface on the declaration
  payable through Pagar/Boletín, computed by the CT engines consumed by id
  (FR-022).
- **AC-015:** Given a second original DMC for the same RTN and period
  attempted after the first was presented, then the attempt is rejected by
  the structural uniqueness constraint with the branch-consolidation
  message (FR-023).

- **AC-016:** Given a grande contribuyente whose vector-fiscal alta state
  lacks the DJIMR alta while the obligation generator expects it for the
  current period, then the alta-state reconciliation surface lists the
  missing alta with its código and window before filing opens
  (FR-017).
## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SAR-236-2024 UNACQUIRED (origin `32_ OQ-2`, LEAD): the DÉCIMO OCTAVO ordinal's numbered list of dual-channel informativas pins the definitive channel matrix; acquiring it resolves the 135 channel conflict (`39_ OQ-1` — file 02 OQ-018) and the 112 anomaly (OQ-004 below). Until then channel rows ship as dated operational data per the Ayuda matrix. | no | acquisition queue | open |
| OQ-002 | CPAT-073 "20 días" day-kind (origin `16_ OQ-5`, DECIDE): the 2016-09→2024-05 DMC window's replacement text omits "calendario" (base text said calendarios). Default = calendario (context: decongestion of a calendario day-10 cluster); the DMC rows themselves are owned by file 03 (its OQ-002) — engine records the default flag only. | no | Takumi S-HN3 + controller | open (default calendario) |
| OQ-003 | 71_/72_ §4 vintage mix (origin `71_ OQ-1`, VERIFY; R-H27): "único medio OVI" sentences are stale vs SAR-236-2024 DÉCIMO SÉPTIMO/OCTAVO + SAR-237-2024 2.II — per-row citation enforced (FR-011 lint); never encode §4 as channel authority. | no | Takumi S-HN3 | open (lint) |
| OQ-004 | 112 OVI-only anomaly (origin `33_ OQ-2`, VERIFY): the highest-volume retention lacks the SW path while siblings have it — stale manual or real restriction? Crossref file 02 OQ-005; resolves with OQ-001. | no | Takumi S-HN3 | open |
| OQ-005 | 523-before-215 ordering enforcement (origin `42_ OQ-2`, CONFIG): whether OVI blocks 215 when 523 is unfiled is unpinned; the prerequisite-edge engine (FR-028) carries it as soft (file 04 OQ-005/FR-145) pending a live OVI check. | no | Takumi S-HN3 | open |
| OQ-006 | Acuse artifact spec (file-local, VERIFY): código único vs CSV (527 adds "Código Seguro de Verificación (CSV)"), QR format/layout and the acuse PDF structure are known only through Ayuda screenshots — SAR-236-2024 TERCERO a/b definitions now verbatim-pinned (W9, `133_` EV133:EVID-502; the artifact CONTRACT itself remains live-portal knowledge); pin the artifact contract before any QR/CSV generation is promised. | no | live-portal capture | open (narrowed W9) |
| OQ-007 | Estado-pill catalog completeness (file-local, VERIFY): observed states = "Original OT. Aprobada OT", "Rectificativa/Rectificada OT, Aprobada OT" (morado), rechazo; the full OVI state vocabulary (in-process/conditional states, per-family variants) is unverified — catalog rows ship extensible. | no | Takumi S-HN3 | open |
| OQ-008 | SAR-236-2024 ordinal structure → **RESOLVED W9** (`133_` acquired, EV133:EVID-503): the ordinal map is PRIMERO…VIGÉSIMO TERCERO; the catalogs = DÉCIMO SEGUNDO (53 determinativas) + DÉCIMO TERCERO (31 informativas) — 66_'s "sección séptima/octava" = manual-side paraphrase. Residuals: body-vs-ANEXO code drift (154/164; anexo-only 507/508; 155 in no anexo — `133_` OQ-1, never encode without PDF-side re-read) + the 542 item-numbering one-off (`133_` OQ-3: cite by CODE, never by item number). | no | — | resolved (W9; residuals flagged) |
| OQ-009 | SAR-007-2017 residual status → **RESOLVED W9** (EV133:EVID-500): SAR-236-2024 VIGÉSIMO PRIMERO.3 leaves SAR-007-2017 "sin valor y efecto" on SAR-236's entry into force (20-may-2024/operative 28-jun-2024), with DÉCIMO NOVENO's pre-vigencia rectification exception preserving old-modality originals; historical imports resolve to DMR rows regardless (R-H31). | no | — | resolved (W9) |
| OQ-010 | Boletín caducidad semantics (file-local, CONFIG): the payment slip carries a "fecha de caducidad" but the consequence of expiry (re-issue, revalidation, penalty) is unpinned; FR-007 stores the date and flags overdue — no expiry effect encoded without an instrument. | no | Takumi S-HN3 | open |
| OQ-011 | 541 deadline drift (origin `64_ OQ-2`, CONFLICT): ISR Art. 47 "antes del último día del mes de febrero" vs manual "a más tardar el ultimo día" — Feb-27/28 vs Feb-28/29; both encoded as dated rows (FR-029), default = manual row flagged; which does OVI enforce? Owner file 10 (written — its OQ-012). | no | Takumi S-HN3 (file 10) | open |
| OQ-012 | 542 deadline drift (origin `65_ OQ-2`, CONFLICT): "dentro de los tres meses siguientes al cierre" (≈Mar-31) vs Recomendación "30 de marzo" — both dated data; encode close+3m as statute row and Mar-30 as operative row, flag; owner file 10 (written — its OQ-016). | no | Takumi S-HN3 (file 10) | open |
| OQ-013 | 509/506 deadline drift (origin `59_ OQ-1`, CONFLICT): statute "3 meses siguientes al cierre" vs Rec. "30 de marzo" (same 1-day family as OQ-012); 509 additionally carries the May-31 CyC audit-report row (encoded, EV56:EVID-167); owner file 11 (written — its OQ-005). | no | Takumi S-HN3 (file 11) | open |
| OQ-014 | 502/503/504 day-kind unstated (origin `56_ OQ-1` family, R-H28; CONFIG): the monthly trio prints "primeros diez (10) días" without calendario/hábiles — default calendario per 04_ OQ-3 discipline, carried as a flagged default (FR-030); ruled monthly by R-H28, confirmed by file 11 FR-374. | no | Takumi S-HN3 (file 11) | open (default calendario) |
