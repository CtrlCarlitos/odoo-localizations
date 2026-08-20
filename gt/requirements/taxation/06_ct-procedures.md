# GT — Taxation — Código Tributario: registry, prescription, sanctions, fiscalización, procedures

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala **Código
Tributario** (CT, Tax Code, Decreto Número 6-91) procedural backbone — cluster
TX6: the *fuentes* (sources of law) hierarchy and reserve-of-law rule for
sanctions/procedures/prescription (Arts. 2–3); taxpayer registry and NIT duties
(Art. 120, with the constitutional-review traps R21); the prescription engine
for obligations (4/8 years, 9-event interruption catalog, Arts. 47–53) and for
infractions/sanctions (5 years, Arts. 74–76); the quantitative sanctions layer
(*interés resarcitorio* rate mechanism Arts. 58–61; *mora* 0.0005/day Art. 92;
omisión 100% Arts. 88–89; withheld-not-entered 100%/50% Art. 91; the Art. 94
deberes-formales multa table with Art. 94 "A" reductions; *cierre temporal*
Arts. 85–86 with commutation; reincidencia Art. 74); fiscalización powers
including systems audit and electronic means (Arts. 30 "C", 93, 98.13, 100,
112, 125 family); payment mechanics and *facilidades* (Arts. 36–43, 99 "A",
54–57 "A"); rectification/rebajas (Arts. 104, 106); the determination/defense
procedure and *recursos* clocks (Arts. 107, 145–149, 153–159); retention-agent
capacity and responsibility (Arts. 28/29/41); books currency and
prescription-anchored record retention (Arts. 94.4, 112 "A", 21 "B"); and the
CT FEL statutory hooks (Art. 98 "A") that the GT-EINV wave cites.

It does **not** cover: NIT structure/format/check-digit rules (NOT in the CT —
GOQ-54 pointer, kin GOQ-49), resarcitorio numeric rates (external Junta
Monetaria publications — GOQ-55), the retention matrices and enterar deadlines
(Task 3, cluster TX3 — this file supplies only the CT sanction/capacity hooks
those files cross-reference), ISR/IVA computation (Tasks 1–5), FEL/DTE
mechanics (GT-EINV wave — its mandate file owns the 98 "A".2 anchor), LET
electronic-books rules (R29: they live in the LAT/D-10-2012 corpus, never in
CT art. 69), the concrete archive matrix (GOQ-124, owned by the C-wave), or
declaration form generation (F-wave). Every CT citation in this file carries
the mandatory currency qualifier "D-6-91, consolidado hasta D-37-2016 +
anotaciones CC hasta el 03-12-2019" (GOQ-53).

## 2. Legal Basis

Authority order (binding, per master evidence index): CT = **"D-6-91,
consolidated through D-37-2016" + CC annotations to 03-12-2019** — the
currency qualifier is mandatory on every CT citation (GOQ-53: no 2017–2026 CT
reform verifiable from the corpus; the qualifier + caveat is the mitigation).
Void texts are never quoted as law: the Art. 120 IVA-régimen-suspension
paragraph (void per CC Exp. 680-2013 + Exp. 292-2013) and Art. 120 "A" (void,
Exp. 997-2013) — FEL suspension citations go to CT 98 "A".2 ONLY (R21); and
Art. 94 numeral 19 (void, Exp. 1898-2012). Dated sanction/prescription values
follow D15/D16 (cite together): valid_from/valid_to rows + instrument
provenance, never constants. Identity: Decreto 6-91 given 9-Jan-1991,
promulgated 25-Mar-1991, vigencia 2-Oct-1991 per Art. 189 (as reformed by
D-47-91).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código Tributario, Decreto Número 6-91 (consolidado legislativamente hasta el Decreto 37-2016, 31-08-2016; anotaciones de la Corte de Constitucionalidad hasta el 03-12-2019 — calificador GOQ-53): "DECRETO NÚMERO 6-91" / "DADO EN EL PALACIO DEL ORGANISMO LEGISLATIVO… A LOS NUEVE DIAS DEL MES DE ENERO DE MIL NOVECIENTOS NOVENTA Y UNO." / "PALACIO NACIONAL: Guatemala, veinticinco de marzo de mil novecientos noventa y uno. PUBLIQUESE Y CUMPLASE" / "ARTICULO 189.* VIGENCIA. El presente Código entrará en vigencia el 2 de octubre de 1991." (*Reformado por el Artículo 1, del Decreto… 47-91 el 01-06-1991") / Art. 7 (normas sin fecha propia): "empezarán a regir después de ocho días de su publicación en el Diario Oficial" | CT identity as dated rows: given 9-Jan-1991; promulgated 25-Mar-1991; vigencia fixed at 2-Oct-1991 (sole D-47-91 reform); default 8-days-after-publication rule for undated norms — the instrument every row below cites with the mandatory currency qualifier | `gt/sources/25_Codigo_Tributario_6-91.pdf` | p.1 title block; p.94–95 date/promulgation blocks; Art. 189 p.94; Art. 7 p.4 (EVID-191) |
| LB-002 | CT D-6-91 (consolidado hasta D-37-2016; CC hasta 03-12-2019 — GOQ-53), cola de reformas por anotaciones inline: "47-91 el 01-06-1991" / "58-96 el 15-08-1996" / "29-2001 el 10-08-2001" / "20-2006 el 06-07-2006" / "4-2012 el 25-02-2012" / "19-2013 el 21-12-2013" / "37-2016 el 31-08-2016" (último decreto integrado); CC más reciente: "*Sin Lugar la acción de Inconstitucionalidad en contra del Artículo 30 "C"… por el Expediente Número 3267-2018 el 03-12-2019" | The copy's own authority list: legislative consolidation ends at D-37-2016 (31-08-2016); latest integrated event of any kind = CC ruling 03-12-2019; nothing post-2019, no FEL-era CT reform integrated — the GOQ-53 currency window every citation must carry | `gt/sources/25_Codigo_Tributario_6-91.pdf` | inline `*` annotations throughout (135-item census, no tail block) (EVID-192) |
| LB-003 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 2 y 3: "Son fuentes de ordenamiento jurídico tributario y en orden de jerarquía: 1. Las disposiciones constitucionales. 2. Las leyes, los tratados y las convenciones internacionales que tengan fuerza de ley. 3. Los reglamentos que por Acuerdo Gubernativo dicte el Organismo Ejecutivo." / "Se requiere la emisión de una ley para: … 4. Tipificar infracciones y establecer sanciones, incluyendo recargos y multas. 5. Establecer los procedimientos administrativos y jurisdiccionales, en materia tributaria. … 7. Modificar las normas relativas a la prescripción…" | Fuentes hierarchy: Constitución > laws/treaties > AG-issued reglamentos; SAT's own instruments (the FEL resolutions/acuerdos) are not a listed fuente — derivative force only; sanctions, procedures and prescription are reserve-of-law matters — the anchor for why FEL rulebooks cannot create sanctions (xref GT-EINV EVID-074) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 2–3 Arts. 2 y 3 (EVID-193) |
| LB-004 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 98 "A" numeral 2 (Adicionado por D-20-2006; Reformado por D-4-2012): "La Administración Tributaria también podrá: … 2. Establecer procedimientos para la elaboración, transmisión y conservación de facturas, recibos, libros, registros y documentos por medios electrónicos, cuya impresión pueda hacer prueba en juicio y los que sean distintos al papel. La Administración Tributaria podrá autorizar la destrucción de los documentos, una vez se hayan transformado en registros electrónicos a satisfacción de ésta." | THE FEL statutory hook, verbatim (cross-matched against every SAT-DSI incorporation resolution's quotation of "numeral 2) del artículo 98 "A""): electronic elaboration/transmission/conservation of invoices-receipts-books-records-documents; SAT may authorize destruction of originals once converted to electronic records to its satisfaction | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 51–52 Art. 98 "A" + annotation block (EVID-194; xref `04-14_SAT-DSI_incorporaciones` EVID-073) |
| LB-005 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 98 "A" numerales 1, 6, 7, 8, 9: "1. Establecer de mutuo acuerdo con el contribuyente, una dirección electrónica en Internet, o buzón electrónico… a efecto de remitirles los acuses de recibo de las declaraciones y pagos efectuados, boletines informativos, citaciones, notificaciones y otras comunicaciones…" / "6. Requerir a los contribuyentes que presenten el pago de los tributos por medios electrónicos, teniendo en cuenta la capacidad económica, el monto de ventas y el acceso a redes informáticas de los mismos." / "7. Verificar por los medios idóneos la veracidad de la información que proporcione el contribuyente o responsable al momento de solicitar su inscripción en el Registro Tributario Unificado…" / "8. Actualizar de oficio el Registro Tributario Unificado u otros registros a su cargo, conforme a la información que proporcione el contribuyente en cualquier declaración de tributos." / numeral 9: SAT corrects form errors ex officio without touching the determined tax | Supporting e-faculties: consensual e-mailbox for notifications/receipts; SAT may REQUIRE electronic payment (economic-capacity criteria); RTU data verification at inscription; ex-officio RTU updating from any declaration (NIT/profile sync flows); ex-officio correction of formal errors | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 51–52 Art. 98 "A" (EVID-195) |
| LB-006 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 120: "Todos los contribuyentes y responsables están obligados a inscribirse en la Administración Tributaria, antes de iniciar actividades afectas." / formulario con "como mínimo lo siguiente: a) Nombres y apellidos completos de la persona individual; b) Denominación o razón social de la persona jurídica…; c) Denominación de los contribuyentes citados en el artículo 22…; d) Nombre comercial, si lo tuviere; e) … representante legal … administradores, gerentes o mandatarios…; f) Domicilio fiscal; g) Actividad económica principal; h) Fecha de iniciación de actividades afectas; i) Inscripción en cada uno de los impuestos a los que se encuentre afecto; j) …agencia, sucursal o cualquier otra forma de actuación." / "Cuando los obligados no cumplan con inscribirse, la Administración Tributaria podrá inscribirlos de oficio…" / "La Administración Tributaria asignará al contribuyente un Número de Identificación Tributaria -NIT-, el cual deberá consignarse en toda actuación que se realice ante la misma y en las facturas o cualquier otro documento que emitan de conformidad con las leyes tributarias." / NIT assignment simultaneous with DPI/Cédula delivery (individuals) and registry inscription (juridical persons — registries "abstenerse de inscribir a toda persona jurídica, sin que se le haya asignado" NIT) / "Toda modificación de los datos de inscripción, debe comunicarse… dentro del plazo de treinta (30) días de ocurrida. Asimismo, dentro de igual plazo, contado a partir del vencimiento de presentación de la última declaración que corresponda, se avisará del cese definitivo o temporal de la actividad…" / "El Registro Mercantil no autorizará la disolución de sociedades mercantiles que no acrediten encontrarse solventes ante la Administración Tributaria." | Art. 120 registry backbone: inscription BEFORE taxable activity; minimum fields a)–j); ex-officio inscription; SAT-assigned NIT mandatory on all filings and issued documents; NIT-DPI/registry simultaneity; 30-day data-change and cese notices (cese counted from the last declaration's due date); Registro Mercantil blocks dissolution without tax solvencia | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 65–67 Art. 120 (EVID-196) |
| LB-007 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 120 párrafo décimo primero — IMPRESO PERO INCONSTITUCIONAL (nunca citar como ley — R21): "*Inconstitucional / Para aquellos contribuyentes que estén omisos en el pago del Impuesto al Valor Agregado o que no sean ubicados en su domicilio fiscal, la Administración Tributaria podrá suspender su afiliación al régimen de dicho impuesto…" con anotaciones: "*Con lugar la acción de inconstitucionalidad contra el Artículo 49 párrafo décimo primero del Decreto 4-2012… por el Expediente Número 292-2013 el 03-04-2014" / "*Inconstitucional el párrafo décimo primero, por el Expediente Número 680-2013 el 05-09-2014" / párrafo siguiente (vigente): "Los contribuyentes o responsables deben actualizar o ratificar sus datos de inscripción anualmente… la actualización de su actividad o actividades económicas principales, que serán aquellas que en el período de imposición correspondiente hubieren reportado más del cincuenta por ciento (50%) de ingresos…" / "ARTICULO 120 "A".* Inconstitucional." (adicionado D-4-2012 art. 50; CC Exp. 997-2013, 23-04-2013) | The Art. 120 trap: the IVA-affiliation-suspension paragraph is printed but CC-struck (Exp. 680-2013 of 05-09-2014; Exp. 292-2013 con lugar 03-04-2014) and Art. 120 "A" is wholly void (Exp. 997-2013) — FEL suspension hooks cite CT 98 "A".2 only (R21). Separate LIVE duty: annual ratification of registration data; main activity = the one(s) with > 50% of reported income in the period | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 66–67 Art. 120 struck ¶ + annotations; Art. 120 "A" p.67 (EVID-197) |
| LB-008 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), deberes-NIT dispersos: Art. 94 numeral 2: "Omisión o alteración del Número de Identificación Tributaria -NIT- o de cualquier otro requisito exigido en declaraciones y recibos de tributos, documentos de importación o exportación y en cualquier documento que se presente o deba presentarse ante la Administración Tributaria. SANCIÓN: Multa de cien Quetzales (Q.100.00) por cada documento. El máximo de sanción no podrá exceder un mil Quetzales (Q.1,000.00) mensuales. En ningún caso la sanción máxima excederá la suma del uno por ciento (1%) de los ingresos brutos…" / Art. 150 numeral 3 (requisitos de resolución): "…su número de identificación tributaria (NIT)…" / Art. 173 numeral 2 (título ejecutivo): "…y su número de identificación tributaria." / Art. 101 "B" (sanction-sentence publication carries the NIT) | NIT duties across the CT: assignment (Art. 120), consignment on declarations/receipts/import-export documents/everything filed with SAT/judicial-execution titles, sanction Q100.00/document capped Q1,000.00/month and 1% of gross income; the CT contains NO NIT format/structure/check-digit rules — those live in the RTU/reglamento corpus (GOQ-54, kin GOQ-49) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 94.2 pp. 43–44; Art. 150.3 pp. 79–80; Art. 173.2 p.90; Art. 112 "A".6 p.62; Art. 101 "B" p.54 (EVID-198) |
| LB-009 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 58, 59 y 61: Art. 58: "…deberá pagar intereses resarcitorios, para compensar al fisco por la no disponibilidad del importe del tributo… será equivalente a la suma que resulte de aplicar a dicho tributo, la tasa de interés simple máxima anual que determine la Junta Monetaria para efectos tributarios, dentro de los primeros quince días de los meses de enero y julio de cada año, para el respectivo semestre, tomando como base la tasa ponderada bancaria para operaciones activas del semestre anterior." / Art. 59: "Los intereses resarcitorios a favor del fisco, se computarán desde el día fijado por la ley para pagar el tributo, hasta el día en que efectivamente se realice el pago del mismo." / Art. 61: taxpayer-favor interests run "desde la fecha en que el contribuyente o responsable presentó la solicitud" (or from payment date for SAT-cause refunds), "aplicando la tasa de interés anual conforme el artículo 58" | Resarcitorio rate mechanism: NO fixed numeric rate in CT — variable rate set by the Junta Monetaria each January/July (first 15 days) per semester = maximum annual simple rate based on the prior semester's weighted bank active rate; runs from statutory due date to actual payment; the same rate pays the taxpayer on refunds — numeric rates are external JM publications (GOQ-55: never hard-coded) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 30–31 Arts. 58, 59 y 61 (EVID-202) |
| LB-010 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 88–89, 91, 92 y 94 "A": Arts. 88–89 (omisión de pago de tributos, no delito): "una multa equivalente al ciento por ciento (100%) del importe del tributo omitido… sin perjuicio de cobrar los intereses resarcitorios" / Art. 91: "…agente de retención o de percepción o contribuyentes del Impuesto al Valor Agregado no enteren… dentro del plazo establecido por las leyes tributarias, los impuestos percibidos o retenidos o el Impuesto al Valor Agregado, serán sancionados con multa equivalente al ciento por ciento (100%) del impuesto retenido o percibido o el pago resultante del Impuesto al Valor Agregado. Si el responsable del pago lo hiciere efectivo antes de ser requerido…, la sanción se reducirá en un cincuenta por ciento (50%)." + "Transcurridos treinta (30) días hábiles contados a partir de la notificación del requerimiento…, se procederá conforme a lo que disponen los artículos 70 y 90" / Art. 92 (mora): "una sanción por cada día de atraso equivalente a multiplicar el monto del tributo a pagar, por el factor 0.0005, por el número de días de atraso. La sanción por mora no aplicará en casos de reparos, ajustes… o en determinaciones de oficio…, en los cuales se aplicará la sanción por omisión de pago… artículo 89." / "La sanción por mora es independiente del pago de los intereses resarcitorios." / Art. 94 "A": voluntary self-report of a pecuniary formal-duty infraction before requirement/fiscalización → "se rebajará la sanción que corresponda en un ochenta y cinco por ciento (85%), siempre que efectue el pago de forma inmediata" (not applicable on recidivism within the período impositivo) | Core quantitative sanctions: omission = 100% of omitted tax (+ resarcitorios); withheld/perceived/IVA not timely entered = 100% halved to 50% if paid pre-requirement, escalating after 30 días hábiles to the Arts. 70/90 track; mora surcharge = 0.0005 × tax × days-late (not on audit adjustments — those take the 100% omission sanction); mora and resarcitorios are cumulative, not alternative; Art. 94 "A" gives 85% voluntary reduction of formal-duty fines with immediate payment | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 39–41 Arts. 87–92; Art. 94 "A" p.47 (EVID-210; Art. 94 "A" verbatim verified against source text) |
| LB-011 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 94 (Infracciones a los deberes formales) — tabla completa, numeral → infracción → SANCIÓN: 1. omisión de aviso de modificación de datos/contador dentro de 30 días → "Multa de cincuenta Quetzales (Q.50.00) por cada día de atraso con una sanción máxima de mil quinientos Quetzales (Q.1,500.00)." / 2. omisión/alteración del NIT u otro requisito → "Q.100.00 por cada documento", máx "Q.1,000.00 mensuales", "En ningún caso… el uno por ciento (1%) de los ingresos brutos… último período mensual en que haya reportado ingresos" / 3. adquirir bienes o servicios sin exigir facturas → "Multa equivalente al monto del impuesto correspondiente a la transacción" (denunciante exonerado) / 4. no llevar al día los libros ("asentadas… dentro de los dos (2) meses calendario inmediatos siguientes de realizadas") → "Multa de cinco mil Quetzales (Q.5,000.00), cada vez que se le fiscalice" / 5. llevar los libros en forma distinta → Q.5,000.00 / 6. ofertar sin el impuesto incluido en el precio → Q.5,000.00 / 7. "No percibir o retener los tributos…" → "Multa equivalente al impuesto cuya percepción o retención omitiere. La imposición de la multa no exime la obligación de enterar el impuesto percibido o retenido, salvo que ya se hubiere efectuado el pago por el sujeto pasivo." / 8. documentos sin requisitos formales → "Q.100.00 por cada documento", máx "cinco mil Quetzales (Q.5,000.00), en cada período mensual", cap "dos por ciento (2%) de los ingresos brutos" / 9. declaraciones tardías → "Q.50.00 por cada día de atraso, con una sanción máxima de un mil Quetzales (Q.1,000.00)"; entidades exentas no lucrativas: sanción duplicada; reincidencia → "cancelación definitiva de la inscripción como persona jurídica no lucrativa" / 10. no concurrir a citación → "Q.1,000.00 por cada vez que sea citado y no concurriere" / 11. comprador sin traspaso de vehículo → "Multa equivalente al cien por ciento (100%) del impuesto… conforme a la tarifa que establece la Ley del Impuesto al Valor Agregado" / 12. aviso de cambio de características de vehículos → "Q.500.00" / 13. no presentar informes → "cinco mil Quetzales (Q.5,000.00) la primera vez; diez mil Quetzales (Q.10,000.00) la segunda vez y en caso de incumplir más de dos veces… diez mil Quetzales (Q.10,000.00) más… el uno por ciento (1%) de los ingresos brutos… durante el último mes" / 14. máquinas registradoras en establecimiento no registrado → Q.5,000.00 / 15. operar sin inscripción previa → Q.10,000.00 / 16. no pagar/no informar por "sistemas o herramientas, formas, formularios electrónicos, informáticos, digitales… de uso obligatorio" → "Multa de un mil Quetzales (Q.1,000.00)" / 17. documentos ilegibles/borrosos/incompletos → Q.5,000.00 por período mensual, cap 1% ingresos brutos / 18. agente de retención sin constancia o extemporánea → "Q.1,000.00 por cada constancia de retención no entregada en tiempo" / "*19. Inconstitucional" (Exp. 1898-2012: suspendido 26-05-2012, con lugar 29-08-2013 — el mecanismo quinquenal de actualización del valor de sanciones es NULO, nunca ley vigente) | THE deberes-formales multa table, every Q value with its numeral: Q50/day cap Q1,500; Q100/doc cap Q1,000/month + 1% ingresos; impuesto-equivalent (acquire-without-invoice); Q5,000 ×4 rows (books backlog per fiscalización / wrong-form books / offer-without-tax / cash-register mislocation); impuesto-equivalent (retention not effected); Q100/doc cap Q5,000/month + 2% ingresos; Q50/day cap Q1,000 (late declarations, doubled for non-profit entities + registration cancelation on recidivism); Q1,000 citación; 100% IVA vehicle traspaso; Q500; Q5,000/Q10,000/Q10,000+1% informes; Q10,000 unregistered operation; Q1,000 e-means; Q5,000/month cap 1% illegible documents; Q1,000 per constancia; numeral 19 VOID — amounts frozen as legislated | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 43–47 Art. 94 numerales 1–18 (+19 struck) + annotation block (EVID-209; full table verified verbatim against extracted text) |
| LB-012 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 85–86, 74, 76: Art. 86: "El cierre temporal se aplicará por un plazo mínimo de diez (10) días y por un máximo de veinte (20) días, continuos. La sanción se duplicará… si el infractor opone resistencia o… viola u oculta los dispositivos de seguridad…" — juez de paz penal competente imposes it after oral audiencia within "cuarenta y ocho (48) horas siguientes a la recepción de la solicitud"; casa-de-habitación access carve-out; labor obligations to dependents survive (CT laboral art. 61 g) cross-ref); apelación contra lo resuelto / conmutación: "A solicitud del sancionado, el juez podrá reemplazar la sanción de cierre temporal por una multa equivalente hasta el diez por ciento (10%) de los ingresos brutos obtenidos en el establecimiento… Dicha multa no podrá ser menor a diez mil Quetzales (Q.10,000.00)." / pequeño contribuyente: "se podrá reemplazar por una multa de cinco mil Quetzales (Q.5,000.00)." / Art. 74: reincidencia = nueva infracción "dentro del plazo de cuatro años"; "Al reincidente… se le aplicará ésta incrementada en un cincuenta por ciento (50%). Si la sanción se aplica en función del importe de un tributo, en ningún caso podrá ser mayor al monto del mismo."; reincidencia en art. 85 → cierre definitivo y el Registro Mercantil cancela inscripción y patente / Art. 76: "Las infracciones y sanciones tributarias prescriben por el transcurso de cinco años, contados a partir de la fecha en que se cometió la infracción o quedó firme la sanción, respectivamente." | Cierre temporal mechanics: 10–20 continuous days (duplicable on resistance/security-device violation), judge of paz penal after 48-hour audiencia; commutation up to 10% of the establishment's gross income with floor Q10,000.00 (pequeño contribuyente variant Q5,000.00); recidivism = 4-year window, +50% fine capped at the tax amount for tax-based fines; art. 85 recidivism → definitive closure + Registro Mercantil cancelation; infractions/sanctions prescribe in 5 years — the second prescription clock | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 34–38 Arts. 74–76 y 85–86 (EVID-211) |
| LB-013 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 47–53: Art. 47: "El derecho de la Administración Tributaria para hacer verificaciones, ajustes, rectificaciones o determinaciones de las obligaciones tributarias, liquidar intereses y multas y exigir su cumplimiento y pago…, deberá ejercitarse dentro del plazo de cuatro (4) años." / repetición del contribuyente, mismo plazo, "a contar desde el día siguiente a aquél en que se realizó el pago indebido o se constituyó el saldo en exceso" / "El derecho a solicitar la devolución de crédito fiscal del Impuesto al Valor Agregado… también prescribe en cuatro años…" (desde la primera fecha en que conforme la ley específica puede solicitarla) / Art. 48: "el plazo de la prescripción se ampliará a ocho años, cuando el contribuyente o responsable no se haya registrado en la Administración Tributaria." / Art. 49: "se contarán a partir de la fecha en que se produjo el vencimiento de la obligación para pagar el tributo." / Art. 50 interrupciones (1–9): determinación (fecha de declaración o notificación de determinación; la audiencia por ajustes NO interrumpe), resolución que confirma ajustes con cantidad líquida y exigible, recursos del contribuyente, reconocimiento expreso o tácito, solicitud de facilidades de pago, notificación de acción judicial + medidas desjudicializadoras/sentencias penales, pago parcial, providencia precautoria o medida de garantía ejecutada, solicitud de devolución de lo pagado en exceso o del crédito fiscal; efecto: "comenzará a computarse nuevamente el plazo, a partir de la fecha en que se produjo la interrupción." / Art. 51 (renuncia): "Se entiende renunciada la prescripción, si el deudor acepta deber sin alegar prescripción o si paga total o parcialmente la deuda prescrita. Este pago no será devuelto en ningún caso." / Art. 52: "La prescripción de la obligación principal extingue las obligaciones accesorias." | Prescription of obligations: 4 years (SAT determination AND taxpayer repetition AND IVA-credit-refund claims, each with its own start date); 8 years for unregistered taxpayers; computed from the obligation's due date; the 9-event interruption catalog with full-clock restart; paying/acknowledging prescribed debt = waiver, non-refundable; principal prescription kills accessories | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 24–26 Arts. 47–53 (EVID-212) |
| LB-014 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 28, 29 y 41: Art. 28: "Son responsables en calidad de agentes de retención o de percepción, las personas designadas por la ley, que intervengan en actos, contratos u operaciones en las cuales deban efectuar la retención or percepción del tributo correspondiente. Agentes de retención, son sujetos que al pagar o acreditar a los contribuyentes cantidades gravadas, están obligados legalmente a retener de las mismas, una parte de éstas como pago a cuenta de tributos a cargo de dichos contribuyentes. Agentes de percepción, son las personas individuales o jurídicas que por disposición legal deben percibir el impuesto y enterarlo al fisco…" / Art. 29: "Efectuada la retención o percepción, el único responsable ante la Administración Tributaria por el importe retenido o percibido, es el agente…"; responde solidariamente con el contribuyente "salvo que acredite que este último efectuó el pago"; agent liable to the taxpayer for retentions "efectuadas sin normas legales que las autoricen" / Art. 41: empresas inscritas en Registros Mercantiles o Civil "dedicadas a la producción, distribución o comercialización de mercancías, o la prestación de servicios, deberán retener las cantidades o porcentajes que en cada caso disponga la ley tributaria respectiva y enterarlos… en los plazos y condiciones que dicha ley especifique." Opt-out: "el contribuyente podrá solicitar… que no se efectúe la retención… La Administración Tributaria deberá resolver dentro del plazo de quince días; en caso contrario, la petición se tendrá por resuelta favorablemente." | Retention-agent law layer: agent capacity comes only from the specific law (who/what/how much lives in D-20-2006/LAT/IVA — cross-ref Task 3); withholding = payment on account of the taxpayer's own tax at pay/credit time; the agent is sole responsible once withheld (solidary with taxpayer unless proven payment; non-entering no exemption); unauthorized retentions actionable by the taxpayer; general enterprise-retention duty (Art. 41) with a 15-day positive-silence opt-out | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Arts. 28–29 pp. 13–14; Art. 41 p.23; sanction cross-refs Arts. 91, 94.7, 94.18, 98.13 (EVID-215) |
| LB-015 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 104 ¶2 y 106: Art. 104 ¶2: "El contribuyente o responsable podrá, bajo su absoluta responsabilidad, presentar formularios electrónicos…, para lo cual podrá contratar los servicios de un Contador Público y Auditor o un Perito Contador…" / Art. 106: "El contribuyente o responsable que hubiere omitido su declaración o quisiere corregirla, podrá presentarla o rectificarla, siempre que ésta se presente antes de ser notificado de la audiencia. Una vez se haya notificado al contribuyente de la audiencia, no podrá presentar declaración o rectificarla… y si lo hiciere, no tendrá validez legal." / "Cuando como consecuencia de la declaración extemporánea o de la rectificación resulte pago de impuesto, gozará del cincuenta por ciento (50%) de la rebaja de los intereses y de la sanción por mora reducida en un ochenta y cinco por ciento (85%), siempre y cuando efectúe el pago junto con la declaración o rectificación." / "Las rectificaciones… tendrán como consecuencia el inicio del cómputo para los efectos de la prescripción." | Rectification mechanics: free amendment ONLY before adjustment-audiencia notification (afterwards void); voluntary-late/rectified payment with simultaneous filing earns 50% interest rebate + mora cut to 15% (85% rebaja); any rectification starts the prescription-clock computation | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 104 p.56; Art. 106 p.57 (EVID-201) |
| LB-016 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 36, 40, 42, 43 y 99 "A": Art. 36 garantías: "1. Depósito en efectivo; 2. Fianza o seguro de caución; 3. Cualquier otro medio establecido en las leyes." / Art. 40: "…facilidades en el pago del impuesto, hasta por un máximo de dieciocho meses… antes del vencimiento del plazo para el pago respectivo… no podrá otorgarse a los casos establecidos en el artículo 91…" / rebaja de convenio: "cincuenta por ciento (50%) de rebaja en los intereses resarcitorios y de un ochenta y cinco por ciento (85%) de la sanción por mora… después de vencido el plazo… pero antes de haber sido notificado de un requerimiento de información para auditoría" / riesgo: incumplimiento "durante los cuatro años anteriores" de otro convenio exige garantía / Art. 42: "las cuotas acordadas se aplicarán en primer lugar al pago de los intereses causados y luego, al pago del tributo." (dos cuotas consecutivas impagas → vence la prórroga → económico coactivo) / Art. 43: compensación de créditos líquidos y exigibles "aunque provengan de distinto tributo… empezando por los más antiguos" (períodos no prescritos, mismo órgano) / Art. 99 "A": saldos líquidos y exigibles notificados se pagan "dentro del plazo de cinco (5) días, contados a partir del día siguiente de la notificación del requerimiento", else Económico Coactivo | Payment mechanics: installment ceiling 18 months (never for Art. 91 withheld-tax cases); convenio rebajas (50% interest / 85% mora) only before an audit-information requirement; risk guarantee after a prior 4-year convenio default; installment payments applied interests-first; cross-tax compensation oldest-first within SAT-administered taxes; 5-day payment window on liquid claims before ejecutivo | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 20–24 Arts. 36–44; Art. 99 "A" p.53 (EVID-203) |
| LB-017 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 54, 55, 56 y 57 "A": Art. 54: "…podrá autorizar que no se inicie el procedimiento administrativo por ajustes de auditoria… cuando no superen la suma de un mil quetzales (Q.1,000.00) en cada período impositivo anual." (siempre se inicia para tributos no determinados mediante declaración) / Art. 55.1: "Cuando el monto de la deuda sea hasta de cinco mil Quetzales (Q.5,000.00)…" (declarable incobrable, tras diligencias de localización; comprende tributos, intereses, multas y recargos de un mismo caso y período) / Art. 56: incobrabilidad/morosidad/económico-coactivo bloquean contratación estatal "por cuatro (4) años a partir de la declaratoria", lifted by full voluntary payment / Art. 57 "A": "La solvencia fiscal es el documento por medio del cual la Administración Tributaria hace constar que a la fecha de su expedición, un contribuyente se encuentra al día… El plazo para la emisión de la solvencia es de ocho días hábiles…" (anual para mantener la exención; prerrequisito para auxiliares; un párrafo D-4-2012 struck Exp. 5094-2012 07-10-2013) | De-minimis thresholds (Q1,000.00 audit-adjustment non-initiation faculty; Q5,000.00 uncollectibility) and the solvencia-fiscal institution: 8 días hábiles issuance SLA; annual solvencia keeps exemption registration; declared-uncollectible/moroso taxpayers barred from State contracting for 4 years (lifted by payment) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 27–29 Arts. 54–57 "A" (EVID-204) |
| LB-018 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 112 y 112 "A": Art. 112.1: "a) Llevar los libros y registros referentes a las actividades y operaciones que se vinculen con la tributación. b) Inscribirse en los registros respectivos… c) Presentar las declaraciones que correspondan…" / Art. 112.3: "Facilitar a los funcionarios fiscales autorizados, las inspecciones o verificaciones en cualquier local…" / Art. 112 "A": "1. Conservar en forma ordenada, mientras no haya transcurrido el plazo de prescripción, libros, documentos y archivos, estados de cuenta bancarios o sistemas informáticos… 2. Conservar por el plazo de la prescripción, los documentos en que conste el cumplimiento de sus obligaciones tributarias. 3. Los sujetos pasivos autorizados a presentar declaraciones… por vía electrónica o medios distintos al papel, deberán conservarlas por el mismo plazo en los medios en que fueron presentadas o en papel, a su elección. 4. Rehacer sus registros contables, en los casos de destrucción, pérdida, deterioro, extravío… dentro del plazo de tres meses contados a partir de la fecha en que ocurrió el hecho…" / 112 "A".5: SAT may "revisar los registros informáticos… ya sea en línea, o a determinado período de tiempo…" / 112 "A".6: third-party payments by medical facilities reported monthly within the first 10 días hábiles of the following month identifying NIT+name+invoice | Record-keeping duties: NO fixed retention-year table in CT — conservation is anchored to the plazo de prescripción (4 years general / 8 unregistered, LB-013); electronic filings conserved in the original medium or paper at the taxpayer's choice; books re-made within 3 months after loss events; SAT online systems review; medical-facility third-party-payment monthly report | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 60–62 Arts. 112 y 112 "A" (EVID-205) |
| LB-019 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 94 numerales 4–5, 85 numeral 4 y 21 "B" numeral 2: Art. 94.4: "No llevar al día los libros contables u otros registros obligatorios… Se entiende que están al día, si todas las operaciones se encuentran asentadas en los libros y registros debidamente autorizados y habilitados, dentro de los dos (2) meses calendario inmediatos siguientes de realizadas. SANCIÓN: Multa de cinco mil Quetzales (Q.5,000.00), cada vez que se le fiscalice." / Art. 85.4 (reformado por D-19-2013 el 21-12-2013): "No haber autorizado y habilitado los libros contables establecidos en el Código de Comercio y habilitado los libros que establecen las leyes tributarias específicas." [sic — "habilitado" duplicado tal como impreso; sentido por confirmar — GOQ-56] / Art. 21 "B".2 (adicionado D-37-2016): "Mantener en su domicilio fiscal o en la oficina del Contador, los libros de contabilidad y registros tributarios…, durante el plazo establecido en la ley." | Books currency: entries recorded within 2 calendar months of the operation ("al día" test); Q5,000.00 per fiscalización for backlogs (numeral 5 for wrong-form books); non-authorized/non-habilitado books are a cierre-temporal infraction (numeral 4 text garbled as printed — GOQ-56); books kept at the domicilio fiscal or accountant's office for the statutory term. CORRECTION (R29): the GT plan's "Art. 69-kin libros y registros" pointer does not exist in CT (CT art. 69 = infracciones CONCEPTO) — electronic-books rules are LET/D-10-2012 territory, cited there, never here | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 94.4–5 p.44; Art. 85.4 pp. 36–37 + annotation; Art. 21 "B".2 pp. 10–11 (EVID-206) |
| LB-020 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 98 numeral 13 y 100: Art. 98.13: "Revisar los libros, documentos y archivos de los contribuyentes y agentes de retención o de percepción…, incluyendo el sistema informático que utilice el contribuyente para registrar sus operaciones contables y tributarias. Para tales efectos podrá requerir… información o documentación relacionada con el equipamiento informático, incluyendo la de programas fuente, diseño y programas utilizados… la producción de listados e integraciones y la realización de pruebas." / Art. 100.1: "…Podrá revisar la documentación y archivos almacenados en papel o medios magnéticos, ópticos u otros dispositivos de almacenamiento digital del contribuyente, y requerir y obtener de éste toda la información necesaria, incluso por los mismos medios…" / Art. 100.3: copies, photocopies, electronic copies of documentation "almacenados en papel o medios magnéticos, ópticos u otros dispositivos de almacenamiento digital" | Fiscalización reach into systems: audit powers explicitly cover source programs, system design, digital storage media, listados/integraciones and test runs — SAT can demand extracts from the ERP itself, not just printed books (audit-export capability as a compliance feature) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 98.13 p.50; Art. 100 pp. 53–54 (EVID-207) |
| LB-021 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 125, 125 "A" y 125 "B": Art. 125: "Se reputarán legítimos los actos de la Administración Tributaria realizados mediante la emisión de documentos por sistemas informáticos, electrónicos, mecánicos u otros similares… También podrá utilizarse en los mismos firmas en forma facsimilar… Serán igualmente válidas las autorizaciones realizadas por la Administración Tributaria mediante claves electrónicas de identificación. En todos los casos, los registros de claves electrónicas… deberán ser conservados por la Administración Tributaria, durante un período no menor a diez (10) años." / Art. 125 "A": SAT may digitize received documents; certified copies "serán admisibles como medios de prueba en toda actuación administrativa o judicial y tendrán plena validez y valor probatorio." / Art. 125 "B": "La información y operaciones transmitidas por medio de comunicaciones y firmas electrónicas, serán reconocidas conforme la regulación de la materia y las disposiciones administrativas que la Administración Tributaria emita al respecto." | CT's electronic-signature layer (125 "A"/"B" added D-4-2012): SAT's own system-generated acts are legitimate (facsimilar/electronic-key signatures valid); digitized certified copies carry full probative value; electronic communications and signatures are recognized per the subject-matter regulation + SAT administrative provisions — the statutory bridge the FEL acuerdos and the communications/e-signature law build on; SAT keeps electronic-key records ≥ 10 years (asymmetric to taxpayer prescription-anchored retention) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 68–70 Arts. 125–125 "B" (EVID-208) |
| LB-022 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 30, 30 "A", 30 "C", 93, 151–152 y 170 "A": Art. 93 (resistencia a la acción fiscalizadora): "cualquier acción u omisión que obstaculice o impida la acción fiscalizadora… después de vencido el plazo improrrogable de tres (3) días, contados a partir del día siguiente de la notificación del requerimiento…", incl. blocking "el acceso inmediato a los libros, documentos y archivos, o al sistema informático del contribuyente" / "SANCIÓN: Multa equivalente al uno por ciento (1%) de los ingresos brutos obtenidos por el contribuyente durante el último período mensual, trimestral o anual declarado… Cuando la resistencia sea de las que se constituyen en forma inmediata, la sanción se duplicará." / Art. 30: deber genérico de informar sobre operaciones con terceros; SAT may require electronic periodic reporting / Art. 30 "A": SAT third-party information requests answered "dentro del plazo de veinte días de recibido el requerimiento" / Art. 30 "C" (adicionado D-37-2016): bank-movement information from Superintendencia de Bancos-supervised entities on "duda razonable", 6-step judicialized procedure — "*Sin Lugar la acción de Inconstitucionalidad en contra del Artículo 30 "C"… por el Expediente Número 3267-2018 el 03-12-2019" (provisionally suspended 17-08-2018; stands) / Arts. 151–152: "Las actas que levanten y los informes que rindan los auditores… tienen plena validez legal en tanto no se demuestre su inexactitud o falsedad."; every procedure "deberá iniciarse por funcionario o empleado, debidamente autorizado" / Art. 170 "A" (adicionado D-4-2012): judge-enforced medida cautelar with 10-day apercibimiento | Fiscalización backbone: 3-day improrrogable documentation handover deadline; 1%-of-declared-gross-income resistance fine (doubled for immediate obstruction, with Criminal Code kin); generic third-party information duties (20-day answer); judicialized bank-data avenue (CC-tested, stands); auditor actas with full probative force; judge-enforced precautionary measures | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Arts. 30–30 "C" pp. 14–18; Art. 93 pp. 41–43; Arts. 151–152 p.80; Art. 170 "A" p.89 (EVID-213) |
| LB-023 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 107, 145 "A", 146, 149, 153–157: Art. 107: pre-determination requirement of omitted declarations "fijando para ello un plazo de diez (10) días hábiles" / Art. 146: audiencia de ajustes "treinta (30) días hábiles improrrogables" (solo sanciones/intereses: 10 días hábiles); conformidad parcial → liquidación con "plazo improrrogable de diez (10) días hábiles para su pago", sanciones "se reducirán al veinticinco por ciento (25%) de su monto original"; pago voluntario sin revocatoria → "rebaja de cincuenta por ciento (50%) de la multa impuesta"; no contencioso/desistimiento → rebaja del 25% / Art. 145 "A" (adicionado D-4-2012): pre-audiencia settlement acta — pago dentro de 5 días del acta → intereses rebajados 40%, mora rebajada 80%, multas por incumplimiento a deberes formales rebajadas 80% / Art. 149: resolution within 30 días hábiles; officer sanctions if unresolved at 115 days (with prueba) / 85 days (without) / Art. 153: restitución claims resolved without procedure if uncontroversial / Art. 154: revocatoria "dentro del plazo de diez (10) días hábiles, contados a partir del día siguiente al de la última notificación. Si no se interpone… la resolución quedará firme."; elevación 5 días; el Tribunal Administrativo Tributario y Aduanero resuelve "dentro del plazo de treinta (30) días hábiles" / Art. 155: ocurso 3 días hábiles; silencio 15 días = concedido / Art. 157: "silencio administrativo" — 30 días sin resolver = resuelto desfavorablemente, abre el contencioso administrativo (facultativo esperar) | The administrative-litigation clock: requerimiento 10 dh → audiencia 30 dh (10 dh solo-sanciones) → resolución 30 dh (officer deadlines 115/85 d) → revocatoria 10 dh (firm on silence) → ocurso 3 dh (15-d silence = granted) → silencio administrativo 30 d → contencioso; the early-conformity rebate ladder (25% / 50% / 40%+80% / and the Art. 40/106 convenio-rectificación pair 50%/85% — LB-015/LB-016) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Arts. 145–150 pp. 76–80; Art. 107 p.58; Arts. 153–159 pp. 81–84 (EVID-214) |
| LB-024 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Arts. 85 numerales 1–3 y 94 numerales 8 y 17: Art. 85: "Se aplicará la sanción de cierre temporal… cuando se incurra en la comisión de cualquiera de las infracciones siguientes: 1. No emitir o no entregar facturas, notas de débito, notas de crédito o documentos exigidos por las leyes tributarias específicas… 2. Emitir… documentos exigidos por las leyes tributarias específicas, que no estén previamente autorizados por la Administración Tributaria. 3. Utilizar máquinas registradoras, cajas registradoras u otros sistemas no autorizados…" / Art. 94.8: "Extender facturas… que no cumplan con alguno de los requisitos formales según la ley específica." / Art. 94.17: emitir en forma "ilegible, borrosa o incompleta" | Pre-FEL document regime in the CT = generic hooks only: closure-temporal infractions for non-emission/non-delivery, UNAUTHORIZED documents and unauthorized systems; per-document formal-defect and illegibility fines. The concrete authorization/impresión regime (printers, ranges, machines) never lived in the CT — reglamentario, outside the corpus (GOQ-57, needed only if legacy-document requirements arise); under FEL the "authorization" concept migrated to régime qualification (IVA 29 "A" lineage + FEL acuerdos — GT-EINV wave) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 85 pp. 36–37; Art. 94 numerales 8 y 17 pp. 44–46 (EVID-199) |
| LB-025 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), Art. 105: "La Administración Tributaria podrá autorizar a los sujetos pasivos para que presenten las declaraciones… por vía electrónica o en medios distintos al papel… Dichos medios deberán cumplir con los siguientes requisitos: 1. Que identifique a través de una clave electrónica al sujeto pasivo… la clave electrónica de acceso u otros medios equivalentes a la firma autógrafa… La utilización de esta clave vinculará al sujeto pasivo al documento y lo hará responsable por su contenido. 2. Que aseguren la integridad de la información… 3. Que la Administración Tributaria entregue al sujeto pasivo una constancia de recepción… en forma física o electrónica." / declaraciones bajo juramento electrónicas con la clave / "La impresión en papel que realice la Administración Tributaria, debidamente certificada… se tendrá por auténtica y de pleno valor probatorio, salvo prueba en contrario." / anexos en papel "permanezcan en poder de los sujetos pasivos… y deban exhibirse o presentarse a requerimiento" | CT's general e-filing engine (reformed D-29-2001; 7th ¶ added D-03-04): authentication (electronic key ≈ autograph signature, binding the filer to the content), integrity, receipt acknowledgment; sworn declarations valid electronically; SAT-certified printouts with full probative value; paper attachments stay with the taxpayer, exhibible on SAT requirement — the pattern FEL/DTE filing reuses | `gt/sources/25_Codigo_Tributario_6-91.pdf` | pp. 56–57 Art. 105 (EVID-200) |
| LB-026 | CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019 — GOQ-53), DIVERGENCIA REGISTRADA (GOQ-120 — sin resolución posible en el corpus; 25_ es el CT consolidado): Art. 91: "…serán sancionados con multa equivalente al ciento por ciento (100%) del impuesto retenido o percibido o el pago resultante del Impuesto al Valor Agregado. Si el responsable del pago lo hiciere efectivo antes de ser requerido…, la sanción se reducirá en un cincuenta por ciento (50%)." (pago extemporáneo de tributos retenidos/percibidos/IVA — multa SOBRE lo retenido) VS. Art. 94 numeral 7: "No percibir o retener los tributos… SANCIÓN: Multa equivalente al impuesto cuya percepción o retención omitiere." (no percibir o retener — multa SOBRE lo omitido; "La imposición de la multa no exime la obligación de enterar el impuesto percibido o retenido, salvo que ya se hubiere efectuado el pago por el sujeto pasivo.") | GOQ-120 finding recorded verbatim, both texts as printed: SAT Criterios documents diverge on the retención-omission multa basis (file 65_ cites CT art. 91; file 64_ cites CT art. 94.7). In the consolidated CT both articles coexist — art. 91 sanctions late ENTERING of sums actually retained/perceived; art. 94.7 sanctions NOT retaining/perceiving. The divergence is recorded UNRESOLVED: no in-corpus winner is picked; sanction evaluation must key on the infraction actually committed | `gt/sources/25_Codigo_Tributario_6-91.pdf` | Art. 91 pp. 40–41; Art. 94.7 p.44 (EVID-210, EVID-209; GOQ-120 register row EV04f OQ-7) |

## 3. Functional Requirements

### 3.1 Fuentes hierarchy & citation discipline

- **GT-TAX-FR-194:** The system's legal-citation model shall rank sources per
  Art. 2 — Constitución > leyes/tratados/conventiones con fuerza de ley >
  reglamentos (Acuerdo Gubernativo) — and shall treat SAT administrative
  instruments (acuerdos de Directorio, resoluciones de Superintendencia — the
  FEL corpus) as derivative, never as fuentes: sanction amounts, procedures
  and prescription changes are reserve-of-law matters (Art. 3 numerals 4/5/7)
  and must always trace to statute (CT or specific law), never to an SAT
  rulebook. (LB-003; EVID-193)
- **GT-TAX-FR-195:** Every CT-derived configuration row, citation surface and
  computed-provenance string shall carry the currency qualifier "D-6-91,
  consolidado legislativamente hasta el Decreto 37-2016 (31-08-2016) +
  anotaciones CC hasta el 03-12-2019" — no 2017–2026 CT reform is verifiable
  from the corpus (GOQ-53); the qualifier + caveat is the mandatory
  mitigation on every CT citation in this file. (LB-001; LB-002; EVID-191,
  EVID-192; GOQ-53 → OQ-001)

### 3.2 Registry & NIT (art. 120)

- **GT-TAX-FR-196:** Taxpayer onboarding shall enforce inscription BEFORE
  starting taxable activity ("antes de iniciar actividades afectas") and
  capture the Art. 120 minimum payload fields a)–j): individual full names;
  razón social/denominación (juridical); art. 22-entity denomination; nombre
  comercial; legal representative + administrators/managers/mandataries with
  registered accreditation; domicilio fiscal; main economic activity; start
  date of taxable activities; per-tax registration (impuestos afecto); and —
  foreign juridical persons — agency/branch/other acting form. (LB-006;
  EVID-196)
- **GT-TAX-FR-197:** The registry model shall support SAT ex-officio
  inscription (regimes corresponding to the taxpayer's characteristics, with
  sanctions preserved), NIT-DPI/registry simultaneity (NIT assigned together
  with Cédula/DPI delivery for individuals; registries refuse juridical
  inscription without NIT), and the Registro Mercantil rule that corporate
  dissolution is refused without tax solvencia — recorded as external-blocker
  facts on the registry workflow. (LB-006; EVID-196)
- **GT-TAX-FR-198:** The NIT shall be required on every filing and every
  issued tax document ("toda actuación… ante la misma y en las facturas o
  cualquier otro documento que emitan"); missing/altered NIT triggers the
  Art. 94.2 sanction row (Q100.00 per document, capped at Q1,000.00/month and
  at 1% of gross income of the last declared month) as dated rows.
  (LB-006; LB-008; LB-011; EVID-196, EVID-198, EVID-209)
- **GT-TAX-FR-199:** NIT structure/format/check-digit validation shall NOT be
  sourced from the CT — the CT contains only assignment and consignment
  duties; the validation rules live in the RTU/reglamento corpus (pointer
  FR only, kin GOQ-49 NIT check-digit coefficients owned by S-GT1's
  validation file — cross-referenced, never duplicated here). (LB-008;
  EVID-198; GOQ-54 → OQ-002)
- **GT-TAX-FR-200:** Registry maintenance clocks: any change to registration
  data must be notified within 30 days of occurrence; cese temporal or
  definitivo must be notified within the same 30-day term counted from the
  due date of the last corresponding declaration (cese temporal = declared
  inactivity for an indicated term; cese definitivo = discontinuation of the
  registered activities); a ceased legal representative may file the
  registry-certified notice. The 30-day change notice is also the Art. 94.1
  sanction trigger (FR-214). (LB-006; EVID-196, EVID-209)
- **GT-TAX-FR-201:** The registry workflow shall schedule the ANNUAL
  ratification/update of registration data (live duty, post-D-4-2012 text)
  and derive actividad económica principal by the > 50%-of-income rule: the
  activity(ies) that reported more than fifty percent of income in the
  corresponding período impositivo. (LB-007; EVID-197)
- **GT-TAX-FR-202:** Void-text guards: the Art. 120 IVA-régimen-suspension
  paragraph shall be recorded as VOID (CC Exp. 680-2013 of 05-09-2014; Exp.
  292-2013 con lugar 03-04-2014) and Art. 120 "A" as void (Exp. 997-2013,
  23-04-2013) — neither may be quoted as law or implemented; every
  suspension/authorization power in the FEL chain cites CT 98 "A".2 ONLY
  (R21; cross-ref GT-EINV 04_mandate-onboarding). (LB-004; LB-007; EVID-194,
  EVID-197)

### 3.3 Prescription engine (arts. 47–53, 76)

- **GT-TAX-FR-203:** The prescription engine shall implement the 4-year term
  for obligations, covering BOTH directions: SAT's verification/adjustment/
  determination/liquidation/collection power AND the taxpayer's repetición
  for excess/undue payments (from the day after the undue payment or excess
  balance arose) AND IVA crédito-fiscal refund claims (from the first date
  the specific law allows the claim) — stored as dated rows with instrument
  provenance. (LB-013; EVID-212)
- **GT-TAX-FR-204:** The prescription term shall be extended to 8 years when
  the taxpayer/responsible is not registered with the Administración
  Tributaria (the same fact that drives the art. 94.15 unregistered-operation
  fine, FR-214). (LB-013; EVID-212)
- **GT-TAX-FR-205:** The prescription clock shall compute from the
  obligation's due date and RESTART IN FULL on any of the 9 interruption
  events (art. 50 catalog): (1) determination by declaration date or
  determination notification — but an adjustment audiencia notification does
  NOT interrupt; (2) notified resolution confirming adjustments (liquid and
  exigible); (3) taxpayer's resources; (4) express or tacit recognition;
  (5) facilidades-de-pago request; (6) judicial-action notification +
  penal desjudicialización measures/sentences; (7) partial payment; (8)
  executed precautionary/guarantee measures; (9) refund/credit-devolution
  requests. (LB-013; EVID-212)
- **GT-TAX-FR-206:** A second, independent clock: infractions and sanctions
  prescribe in 5 years — infractions from the date committed, sanctions from
  the date they became firm. (LB-012; EVID-211)
- **GT-TAX-FR-207:** Prescription renuncia and accessory effects: paying or
  acknowledging prescribed debt = waiver with no refund ever ("Este pago no
  será devuelto en ningún caso"); prescription of the principal obligation
  extinguishes accessory obligations (interests, surcharges, fines).
  (LB-013; EVID-212)
- **GT-TAX-FR-208:** Prescription-clock computation (both clocks, restart
  events, waiver detection, accessory extinction) shall run as a saas
  evaluation service consuming the shared dated prescription rows, with odoo
  surfacing prescription status/expiry dates on obligations and sanction
  records. (LB-012; LB-013; EVID-211, EVID-212)

### 3.4 Interest, mora & omission sanctions (arts. 58–61, 87–92)

- **GT-TAX-FR-209:** Late-payment interest (*interés resarcitorio*) shall be
  modeled EXCLUSIVELY as the variable JM mechanism — simple annual rate set
  by the Junta Monetaria in the first 15 days of January and July for each
  semester, based on the prior semester's weighted bank active rate,
  computed from the statutory due date to the actual payment day; the same
  art. 58 rate pays the taxpayer on refunds (from request date, or payment
  date for SAT-cause refunds). NO numeric rate shall ever be hard-coded from
  the CT: the rate table is an external-data ingestion requirement (JM
  semester publications) feeding a saas external-data service (GOQ-55).
  (LB-009; EVID-202; GOQ-55 → OQ-003)
- **GT-TAX-FR-210:** The mora sanction shall compute per day of delay as
  tax × 0.0005 × days, self-applied on late-filed/late-paid declarations
  (*opera de pleno derecho*); it shall NOT apply to reparos, adjustments to
  incorrect determinations or ex-officio determinations — those take the
  art. 89 omission sanction instead — and it is independent of and
  cumulative with resarcitorio interests. Dated rows: factor 0.0005/day
  (CT art. 92, text D-6-91 consolidado hasta D-37-2016). (LB-010; EVID-210)
- **GT-TAX-FR-211:** The omission sanction shall be 100% of the omitted tax
  amount (arts. 88–89, non-criminal cases), cumulative with resarcitorio
  interests, applied on audit adjustments/ex-officio determinations per the
  art. 92 routing. (LB-010; EVID-210)
- **GT-TAX-FR-212:** Withheld/perceived taxes and IVA payments not entered
  within the statutory term shall be sanctioned at 100% of the retained/
  perceived/IVA amount (art. 91), reduced to 50% when paid before being
  required by SAT; if still unpaid 30 días hábiles after requirement
  notification, the arts. 70/90 track applies (judicial/criminal-indicio
  escalation — never a second sanction for the same act). (LB-010; EVID-210)
- **GT-TAX-FR-213:** The retención-omission sanction divergence shall be
  recorded VERBATIM and UNRESOLVED (GOQ-120): art. 91 text (100% of the
  retained/perceived tax or IVA payment result; 50% pre-requirement
  reduction; 30-dh escalation) AND art. 94.7 text (multa equivalent to the
  tax whose perception/retention was omitted; fine does not exempt entering,
  unless the taxpayer already paid) both exist in the consolidated CT; the
  system shall key sanction evaluation on the infraction actually committed
  (late entering of sums retained vs. failure to retain) and shall NOT pick
  a corpus winner for the Criterios-level divergence. (LB-026; EVID-209,
  EVID-210; GOQ-120 → OQ-006)

### 3.5 Art. 94 deberes-formales multa table

- **GT-TAX-FR-214:** The Art. 94 multa table shall be seeded as dated rows
  (valid_from/valid_to + provenance "CT D-6-91 Art. 94, consolidado hasta
  D-37-2016"), every numeral with its exact value: 1 Q50.00/day of delay,
  max Q1,500.00 (data-change/contador notice within 30 days); 2 Q100.00 per
  document, max Q1,000.00/month, cap 1% ingresos brutos (NIT omission/
  alteration); 3 impuesto-equivalent of the transaction (acquiring without
  invoice; denouncer exonerated); 4 Q5,000.00 per fiscalización (books not
  al día — the 2-month test, FR-231); 5 Q5,000.00 (books in non-compliant
  form); 6 Q5,000.00 (offers without tax included in price); 7
  impuesto-equivalent (not retaining/perceiving — FR-213 divergence row);
  8 Q100.00 per document, max Q5,000.00/month, cap 2% ingresos brutos
  (documents missing formal requisites); 9 Q50.00/day, max Q1,000.00 (late
  declarations; doubled for exempt non-profit entities; definitive
  registration cancelation on recidivism); 10 Q1,000.00 per citation
  missed; 11 100% of the IVA per the Ley del IVA tariff (vehicle traspaso
  not registered); 12 Q500.00 (vehicle-characteristics change notice); 13
  Q5,000.00 first / Q10,000.00 second / Q10,000.00 + 1% of last-declared-
  month income beyond twice (informes not presented); 14 Q5,000.00 (cash
  registers at unregistered establishment); 15 Q10,000.00 (operating without
  prior inscription); 16 Q1,000.00 (not paying/reporting through mandatory
  electronic systems/forms); 17 Q5,000.00 per monthly period, cap 1%
  ingresos brutos (illegible/blurred/incomplete documents); 18 Q1,000.00 per
  retention constancia not delivered in time. (LB-011; EVID-209)
- **GT-TAX-FR-215:** Art. 94 table rules and guards: percent-capped rows
  (2/8/13/17) key on the último período mensual en que haya reportado
  ingresos; numeral 16 is the e-channel enforcement hook (Q1,000.00 for
  ignoring mandatory electronic systems/forms — the statutory backstop of
  the FEL/Declaraguate/RetWeb channel duties); numeral 19 (five-yearly
  value-update mechanism) is VOID (Exp. 1898-2012: provisionally suspended
  26-05-2012, inconstitucional 29-08-2013) — no value-updating mechanism
  shall be implemented and the amounts are frozen as legislated. (LB-011;
  EVID-209)

### 3.6 Cierre temporal & reincidencia (arts. 85–86, 74)

- **GT-TAX-FR-216:** Cierre temporal shall be modeled as 10 to 20 CONTINUOUS
  days, duplicable on resistance or violation/concealment of security
  devices during the procedure, imposed by the competent juez de paz penal
  after an oral audiencia held within 48 hours of the request (house-
  habitation access carve-out; labor obligations to dependents survive the
  closure; apelación lies) — the infractions list is art. 85 (non-emission/
  non-delivery of documents, unauthorized documents/systems, non-authorized
  books — FR-231) plus resistance kin. Dated rows: min 10 / max 20 days.
  (LB-012; LB-024; EVID-211, EVID-199)
- **GT-TAX-FR-217:** Commutation of cierre temporal: at the sanctioned
  party's request the judge may substitute a fine of up to 10% of the gross
  income of the sanctioned establishment (last monthly period), never below
  Q10,000.00; pequeño contribuyente variant: replaceable by a Q5,000.00
  fine. Dated rows for both floors. (LB-012; EVID-211)
- **GT-TAX-FR-218:** Reincidencia: a new infraction within 4 years of a
  notified sanction increases the fine by 50%, capped at the tax amount when
  the sanction is tax-based; recidivism on art. 85 infractions within the
  4-year term → cierre definitivo + Registro Mercantil cancelation of
  inscripción and patente. The saas sanction evaluator shall consume the
  sanction history with a 4-year lookback and non-bis-in-idem guard (art. 90:
  never sanction the same infraction twice; criminal-indicio cases referred
  to prosecutors). (LB-012; EVID-211)

### 3.7 Fiscalización, resistance & e-means (arts. 30 "C", 93, 98, 100, 112, 125)

- **GT-TAX-FR-219:** Fiscalización support: documentation required by SAT in
  a verification shall be handed over within the improrrogable 3-day term
  (from the day after requirement notification), with immediate access to
  books, documents, archives and the taxpayer's computer system; audit
  powers extend to the accounting/tax SYSTEM itself (art. 98.13: source
  programs, design and used programs, equipment information, listados and
  integraciones, test runs; art. 100: paper, magnetic, optical and digital
  storage) — the product shall provide an audit-export capability
  (listados/integraciones/pruebas) as a compliance feature. (LB-020; LB-022;
  EVID-207, EVID-213)
- **GT-TAX-FR-220:** Resistance to fiscalización (any action/omission
  obstructing the audit after the 3-day term, including blocking immediate
  access to books/systems) carries a fine of 1% of gross income of the last
  declared monthly/quarterly/annual period, DOUBLED for resistance
  constituted immediately — stored as a dated sanction row; judge-
  intervention cases route to the Criminal Code resistance provision.
  (LB-022; EVID-213)
- **GT-TAX-FR-221:** Information powers: the product shall support
  third-party information duties (art. 30: everyone must report third-party
  tax-relevant dealings; art. 30 "A": 20-day answer to SAT periodic/eventual
  requests, electronic periodic reporting possible) and record the
  judicialized bank-data avenue of art. 30 "C" (duda razonable, 6-step
  procedure; CC Exp. 3267-2018 sin lugar 03-12-2019 → stands), the full
  probative force of auditor actas/informes (arts. 151–152, until
  inexactitude/falsity is shown; procedures must be initiated by duly
  authorized personnel) and judge-enforced medidas cautelares with 10-day
  apercibimiento (art. 170 "A"). (LB-022; EVID-213)
- **GT-TAX-FR-222:** Electronic means (arts. 125/125 "A"/125 "B"): SAT
  system-generated acts are legitimate (facsimilar signatures and electronic
  identification keys valid; SAT keeps key records ≥ 10 years — asymmetric
  to the taxpayer's prescription-anchored retention); SAT-digitized
  certified copies have full probative value; electronic communications and
  signatures are recognized per the subject-matter regulation + SAT
  provisions — recorded as the CT statutory bridge under the FEL acuerdos
  and the e-signature law (cross-ref GT-EINV). (LB-021; EVID-208)
- **GT-TAX-FR-223:** E-filing engine (art. 105): electronic declarations
  require identification via electronic key (≈ firma autógrafa, binding the
  filer to the content), information integrity, and delivery of a
  constancia de recepción (physical or electronic); sworn declarations are
  valid electronically; SAT-certified printouts carry full probative value;
  paper support documentation stays in the taxpayer's power, exhibitable on
  SAT requirement — no blanket physical filing of annexes. (LB-025; EVID-200)

### 3.8 Rectification, procedure & recursos clocks (arts. 104–107, 145–159)

- **GT-TAX-FR-224:** Declaration rectification/amendment window (art. 106):
  omissions may be declared and declarations corrected ONLY before
  notification of the adjustment audiencia — after it, any
  declaration/rectification is legally void; voluntary-late or rectified
  payment made TOGETHER with the filing earns 50% rebate of resarcitorio
  interests and the mora sanction reduced to 15% (85% rebaja); every
  rectification starts the prescription-clock computation (feeds FR-205
  event routing). Electronic filing under own responsibility, optionally
  via contracted CPA/Perito Contador (art. 104 ¶2). (LB-015; EVID-201)
- **GT-TAX-FR-225:** The determination/defense procedure shall carry the
  statutory clocks as dated rows: omitted-declaration pre-determination
  requerimiento 10 días hábiles (art. 107) → adjustment audiencia 30 días
  hábiles improrrogables (10 días hábiles when only sanctions/interests are
  at stake) → conformed adjustments liquidated with 10-días-hábiles payment
  term and sanctions reduced to 25% → SAT resolution 30 días hábiles
  (officer-level sanction if unresolved at 115 days with prueba / 85 days
  without) → económico coactivo. (LB-023; EVID-214)
- **GT-TAX-FR-226:** The sanction/interest rebate ladder shall be seeded as
  dated rows keyed on trigger conditions: 25% reduction on conformity with
  adjustments/liquidation; 50% on voluntary payment without revocatoria;
  25% on no-contencioso/desistimiento (art. 146); 40% interests / 80% mora /
  80% formal-fault fines on the pre-audiencia settlement acta paid within 5
  days (art. 145 "A"); 50% interests / 85% mora on the art. 40 convenio
  (pre-audit-requirement only) and the art. 106 rectification pair (FR-224);
  85% on voluntary self-report of formal-duty infractions with immediate
  payment (art. 94 "A", not applicable on same-period recidivism).
  (LB-010; LB-015; LB-016; LB-023; EVID-210, EVID-201, EVID-203, EVID-214)
- **GT-TAX-FR-227:** Recursos clocks: revocatoria within 10 días hábiles
  from the day after the last notification (resolution firm on silence;
  elevation within 5 days; Tribunal Administrativo Tributario y Aduanero
  resolves within 30 días hábiles); ocurso within 3 días hábiles (silence 15
  días = granted); silencio administrativo after 30 days without resolution
  = unfavorably resolved, opening the contencioso administrativo (waiting
  optional); uncontroversial restitución claims resolved directly without
  procedure; execution titles carry NIT + full debtor identity (art. 173).
  (LB-023; LB-008; EVID-214, EVID-198)
- **GT-TAX-FR-228:** Payment mechanics: liquid and exigible notified balances
  pay within 5 days of the day after requirement notification, else económico
  coactivo (art. 99 "A"); facilidades de pago up to 18 months, never for
  art. 91 withheld-tax cases, applied interests-first per cuota (two
  consecutive missed cuotas terminate the plan → ejecutivo), risk guarantee
  required on prior 4-year convenio default; cross-tax compensation of
  liquid/exigible credits oldest-period-first within SAT-administered
  taxes (non-prescribed periods); garantías = cash deposit, surety bond, or
  other legal means; anticipos a cuenta allowed in annual regimes (art. 39).
  (LB-016; EVID-203)
- **GT-TAX-FR-229:** De-minimis and solvencia: SAT may decline to open audit
  procedures for adjustments ≤ Q1,000.00 per annual tax period on
  declaration-determined taxes (faculty, never a duty — and never for
  non-declaration-determined taxes); debts ≤ Q5,000.00 may be declared
  incobrable after failed location efforts (same case and period, covering
  tributes+interests+fines+surcharges); declared-uncollectible/moroso/
  económico-coactivo status bars State contracting for 4 years from the
  declaration (lifted by full voluntary payment); solvencia fiscal issuance
  SLA 8 días hábiles, annual for exemption-registration maintenance and
  auxiliary prerequisites. All thresholds as dated rows. (LB-017; EVID-204)

### 3.9 Retention agents, books & retention (arts. 28/29/41, 94.4, 112 "A")

- **GT-TAX-FR-230:** Retention-agent model (arts. 28/29/41): agent capacity
  exists only by designation of the specific law (rates/matrices/enterar
  deadlines owned by Task 3 — cross-referenced, never re-derived here);
  withholding is a payment on account of the taxpayer's own tax at pay/
  credit time; once effected, the agent is the sole responsible before SAT
  (solidary with the taxpayer unless the agent proves the taxpayer paid;
  non-entering is no exemption); unauthorized retentions make the agent
  liable to the taxpayer; Art. 41 enterprises (production/distribution/
  commercialization of goods or services, registered in the Mercantile/Civil
  registries) shall retain what the respective tax law provides; the
  no-retention opt-out resolves in 15 days with POSITIVE silence (petition
  granted if SAT does not resolve). Sanction hooks: arts. 91/94.7 (FR-212/
  FR-213) and 94.18 constancia row (FR-214). (LB-014; EVID-215; xref Task 3
  GT-TAX-FR-104/105..107; FR-110 = fuel/import edge guard)
- **GT-TAX-FR-231:** Books currency (art. 94.4): all operations must be
  recorded in duly authorized/habilitado books and registers within the 2
  calendar months immediately following their realization — the ledger-
  currency compliance metric; backlog = Q5,000.00 per fiscalización (FR-214
  row 4); non-authorized/non-habilitado books are an art. 85.4 cierre-
  temporal infraction (text as printed with the redundant "habilitado…
  y habilitado" [sic] — sense pending GOQ-56, quoted only with the sic
  flag); books and tax registers kept at the domicilio fiscal or the
  accountant's office for the statutory term (art. 21 "B".2).
  Electronic-books (LET) rules are LAT/D-10-2012 territory — cited there,
  never to CT art. 69 (R29 correction). (LB-019; EVID-206; GOQ-56 → OQ-004)
- **GT-TAX-FR-232:** Record retention is PRESCRIPTION-ANCHORED, not a fixed
  year table: books, documents, archives, bank statements and information
  systems must be conserved in orderly form while the prescription term has
  not run (4 years general / 8 years unregistered — FR-203/FR-204),
  including documents evidencing tax-obligation compliance; electronically
  filed declarations/annexes conserved in the ORIGINAL medium or paper at
  the taxpayer's choice; records re-made within 3 months of
  destruction/loss/deterioro/misplacement/patrimonial crimes; SAT may review
  computer records online or for a determined period; medical-facility
  third-party payments reported monthly within the first 10 días hábiles of
  the following month (NIT + name + invoice per professional). The concrete
  archive matrix (max-per-object retention table) is owned by the C-wave —
  cross-referenced via GOQ-124, never duplicated here. (LB-018; EVID-205;
  GOQ-124 → OQ-007)
- **GT-TAX-FR-233:** Pre-FEL document-regime guards: CT art. 85 numerales
  1–3 (cierre for non-emission/non-delivery, unauthorized documents,
  unauthorized registers/systems) and art. 94 numerales 8/17 (formal-defect
  and illegibility fines) are generic hooks ONLY — document-authorization
  mechanics shall be sourced from the specific facturación/FEL instruments
  (IVA 29 "A" lineage + AD 13-2018 chain, GT-EINV wave), never from the CT;
  the impresores-era reglamento is not in the corpus and is required only if
  legacy-document requirements arise (conditional note, GOQ-57).
  (LB-024; EVID-199; GOQ-57 → OQ-005)
- **GT-TAX-FR-234:** FEL statutory anchor: CT art. 98 "A".2 (verbatim,
  LB-004) is the statutory basis for electronic elaboration/transmission/
  conservation of facturas, recibos, libros, registros y documentos, and for
  SAT-AUTHORIZED destruction of originals after conversion to electronic
  records "a satisfacción de ésta" — no paper-destruction workflow may run
  without that authorization; every FEL-incorporation cross-reference keys
  on 98 "A".2 (added D-20-2006, reformed D-4-2012; cross-matched verbatim
  against the SAT-DSI resolutions — GT-EINV 04_mandate-onboarding owns the
  mandate chronology). Suspension powers cite 98 "A".2 only (R21 — FR-202).
  (LB-004; EVID-194)
- **GT-TAX-FR-235:** CT 98 "A" infrastructure faculties as product hooks:
  consensual electronic mailbox for notifications/acuses (taxpayer must
  report address changes); SAT may REQUIRE electronic payment by criterion
  (economic capacity, sales volume, network access) — recorded as the
  statutory basis for e-payment channel duty; RTU inscription-data
  verification; ex-officio RTU updating from any filed declaration (saas
  external-data sync surfaces, NIT/profile sync flows); SAT corrects formal
  errors ex officio without touching determined tax. (LB-005; EVID-195)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance "CT D-6-91 (consolidado hasta D-37-2016 + CC 03-12-2019)" on
EVERY sanction/prescription value (GOQ-53 qualifier); snapshot-on-write;
sanction and prescription rows are decree-bound, never constants.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.ct.prescription.rule | kind / years / computed_from | selection / integer / char | obligation 4 (determination + repetición + IVA-credit refund, each with own start); obligation_unregistered 8; infraction 5 (from date committed); sanction 5 (from firme date); computed_from = obligation due date (obligation kinds) | FR-203, FR-204, FR-206 |
| l10n_gt.ct.prescription.interruption | event_no / description / restart | integer / char / boolean | 9-event art. 50 catalog (determination, confirming resolution, recursos, recognition, facilidades request, judicial action + penal measures, partial payment, executed precautionary measures, refund/credit requests); restart = full clock; audiencia notification explicitly non-interrupting | FR-205 |
| l10n_gt.ct.sanction.rate | code / value / cap / provenance | char / decimal / decimal / char | mora 0.0005/day × tax × days; omision 1.00 (100% of tax); retained_not_entered 1.00 / 0.50 pre-requirement; escalation 30 dh → arts. 70/90; resistencia 0.01 of ingresos brutos ×2 immediate | FR-210, FR-211, FR-212, FR-220 |
| l10n_gt.ct.sanction.formal | numeral / infraction / amount_spec / caps | integer / char / char / json | Art. 94 rows 1–18 exactly as printed (Q50/day cap Q1,500; Q100/doc cap Q1,000/month + 1%; impuesto-equivalent ×2; Q5,000 ×4; Q100/doc cap Q5,000/month + 2%; Q50/day cap Q1,000; Q1,000 citación; 100% IVA vehicle traspaso; Q500; Q5,000/Q10,000/Q10,000+1% informes; Q10,000 unregistered operation; Q1,000 e-means; Q5,000/month cap 1%; Q1,000 per constancia); numeral 19 = void guard row; caps key on último período mensual con ingresos reportados | FR-214, FR-215 |
| l10n_gt.ct.cierre | min_days / max_days / commutation_pct / commutation_floor / pequeno_floor | integer / integer / decimal / decimal / decimal | 10 / 20 continuos, duplicable; commutation ≤ 10% ingresos brutos, floor Q10,000.00; pequeño floor Q5,000.00 | FR-216, FR-217 |
| l10n_gt.ct.recidivism | lookback_years / increment / cap | integer / decimal / char | 4 / +0.50 / capped at tax amount for tax-based fines; art. 85 recidivism → cierre definitivo + RM cancelation | FR-218 |
| l10n_gt.ct.resarcitorio.rate | semester / rate / provenance | char / decimal / char | EXTERNAL ingestion (JM publications, first 15 days of Jan/Jul; prior-semester weighted bank active rate) — NEVER seeded from CT; no numeric default | FR-209 |
| l10n_gt.ct.rebaja | trigger / interest_pct / mora_pct / fine_pct / condition | char / decimal / decimal / decimal / char | art. 146 conformity 25%; voluntary-no-revocatoria 50%; no-contencioso 25%; art. 145 "A" acta 40/80/80 (pay 5 days); art. 40 convenio 50/85 (pre-requirement); art. 106 rectification 50/85 (with filing); art. 94 "A" 85 (formal duties, immediate payment) | FR-226 |
| l10n_gt.ct.procedure.clock | event / deadline / unit / improrrogable | char / integer / selection / boolean | requerimiento 10 dh; audiencia 30 dh (10 dh solo-sanciones); liquidation payment 10 dh; resolution 30 dh (officer 115/85 d); revocatoria 10 dh + resolve 30 dh; elevación 5 d; ocurso 3 dh (silence 15 d granted); silencio administrativo 30 d; 99 "A" payment 5 d; resistance handover 3 d; 30 "A" answer 20 d; annual ratification; 30-day registry notices; 3-month rehacer | FR-200, FR-219, FR-221, FR-225, FR-227, FR-228, FR-232 |
| l10n_gt.ct.registry.field | key / art | char / char | art. 120 a)–j) payload: names, razón social, art. 22 entities, nombre comercial, legal rep/administrators, domicilio fiscal, main activity, start date, per-tax afflictions, foreign-entity acting form | FR-196 |
| l10n_gt.ct.void.text | article / ruling / status | char / char / selection | art. 120 décimo-primer párrafo (Exp. 680-2013 05-09-2014 + Exp. 292-2013 03-04-2014); art. 120 "A" (Exp. 997-2013 23-04-2013); art. 94.19 (Exp. 1898-2012 29-08-2013); art. 57 "A" ¶ (Exp. 5094-2012 07-10-2013, partial) | FR-202, FR-215 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = computation,
evaluation and authoritative validation in the Elixir core; `shared` =
contract items both sides must honor identically. Taxation-wave defaults per
the wave plan: sanction/prescription dated data + clocks = `shared`; NIT/
registry fields on partner/company = `odoo`; prescription-clock computation +
sanction evaluation = `saas` with odoo surfaces; resarcitorio rate ingestion =
`saas` external-data service (GOQ-55). Model names stable across Odoo
17/18/19/20; no version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-194 | shared | — | citation-hierarchy contract | Sanction/procedure/prescription rows must trace to statute on both sides; SAT-rulebook-only provenance rejected |
| FR-195 | shared | — (config data §4) | provenance strings | Every CT row carries the GOQ-53 qualifier "consolidado hasta D-37-2016 + CC 03-12-2019" |
| FR-196 | odoo | res.partner / res.company | art. 120 a)–j) onboarding payload | Pre-activity inscription gate; per-tax affliction flags |
| FR-197 | odoo | res.partner (registry facts) | ex-officio / NIT-simultaneity / RM-solvency blocker fields | External-blocker records, not locally enforced |
| FR-198 | odoo | res.partner + account.move | NIT required on filings/documents | 94.2 sanction row consumed by saas evaluator |
| FR-199 | shared | — | NIT-validation pointer guard | Structure/check-digit rules live in RTU corpus (GOQ-54; kin GOQ-49 owned by S-GT1 validation file) — never cited to CT |
| FR-200 | odoo | res.partner (registry maintenance) | 30-day change/cese clocks | Feeds FR-214 numeral-1 sanction trigger |
| FR-201 | odoo | res.partner (activity classification) | annual ratification + >50% income rule | Main-activity derivation from declared income |
| FR-202 | shared | — (config data §4) | void-text guard rows | 120 ¶ + 120 "A" void; suspension cites = 98 "A".2 only (R21; GT-EINV 04 owns the mandate layer) |
| FR-203 | shared | — (config data §4) | prescription rule rows | Both directions (SAT + taxpayer); own start dates per direction |
| FR-204 | shared | — (config data §4) | 8-year unregistered row | Registration status flag feeds term selection |
| FR-205 | shared | — (config data §4) | 9-event interruption catalog | Full-restart semantics; audiencia ≠ interruption |
| FR-206 | shared | — (config data §4) | infraction/sanction 5-year rows | Second clock, independent of obligation prescription |
| FR-207 | shared | — | waiver + accessory-extinction rules | Payment of prescribed debt never refunded |
| FR-208 | saas | prescription computation service | both clocks + restart/waiver detection | Odoo surfaces status/expiry on obligations and sanctions |
| FR-209 | saas | external-data service (resarcitorio) | JM semester rate ingestion | GOQ-55: never hard-coded; no numeric default exists on either side until ingestion |
| FR-210 | saas | sanction evaluation (mora) | 0.0005/day × tax × days | Routing: self-late = mora; audit adjustments = omisión; cumulative with resarcitorios |
| FR-211 | saas | sanction evaluation (omisión) | 100% of omitted tax | Applied on reparos/ajustes/determinaciones de oficio |
| FR-212 | saas | sanction evaluation (retained-not-entered) | 100% / 50% pre-requirement / 30-dh escalation | Escalation to arts. 70/90 recorded, non-bis-in-idem guard |
| FR-213 | shared | — (config data §4) | GOQ-120 divergence row | Both texts verbatim; evaluation keys on infraction committed; no winner picked |
| FR-214 | shared | — (config data §4) | art. 94 table dated rows | Every numeral with exact Q value; caps relative to último mes con ingresos |
| FR-215 | shared | — | 94.19 void guard + 94.16 e-means hook | No value-update mechanism; amounts frozen as legislated |
| FR-216 | shared | — (config data §4) | cierre dated rows 10–20 d | Judicial procedure — product records, never executes closures |
| FR-217 | shared | — (config data §4) | commutation rows Q10,000 / Q5,000 | ≤10% ingresos brutos of the establishment |
| FR-218 | saas | sanction evaluation (recidivism) | 4-year lookback, +50%, tax-amount cap | Consumes sanction history; non-bis-in-idem (art. 90); odoo surfaces flags |
| FR-219 | odoo | audit-export surfaces (listados/integraciones) | systems-audit support | 98.13/100 reach; 3-day handover clock surfaced |
| FR-220 | shared | — (config data §4) | resistencia sanction row 1% ×2 | Evaluation saas-side; odoo audit-trail surfaces |
| FR-221 | odoo | third-party info surfaces | 20-day answer clock; 30 "C" fact rows | Bank-data avenue + acta probative force recorded as compliance facts |
| FR-222 | shared | — | e-means recognition contract | SAT 10-year key retention vs taxpayer prescription-anchored asymmetry |
| FR-223 | shared | — | e-filing requisites contract | Key = firma autógrafa; constancia de recepción; paper annexes stay with taxpayer |
| FR-224 | shared | — (config data §4) | rectification window + 50/85 rebajas | Window closes on audiencia notification; feeds prescription routing |
| FR-225 | shared | — (config data §4) | procedure clock rows | 10/30(10)/30/115/85 dh chain; judicial steps recorded, not executed |
| FR-226 | shared | — (config data §4) | rebaja ladder rows | Trigger-condition-keyed; consumed by saas sanction evaluator |
| FR-227 | shared | — (config data §4) | recursos clock rows | Revocatoria 10 dh, ocurso 3 dh, silencio 30 d; restitución without procedure |
| FR-228 | saas | payment application engine | 5-d claim, 18-m convenios, interests-first, compensación oldest-first | Odoo surfaces payment plans/compensation proposals |
| FR-229 | shared | — (config data §4) | de-minimis/solvencia dated rows | Q1,000/Q5,000/4-year ban/8-dh SLA — faculty rows, not duties |
| FR-230 | odoo | res.partner (retention-agent config) | agent capacity + sole-responsibility flags | Rates/deadlines owned by Task 3 (GT-TAX-FR-105..107; FR-110 = fuel/import edge guard); 15-day positive-silence opt-out recorded |
| FR-231 | odoo | account books / compliance dashboard | 2-month ledger-currency metric | Q5,000 row + art. 85.4 cierre list ([sic] flag GOQ-56); LET rules cite LAT (R29) |
| FR-232 | shared | — (config data §4) | retention policy anchor (prescription-anchored) | Archive matrix owned by C-wave (GOQ-124 cross-ref); 3-month rehacer; original-medium rule |
| FR-233 | shared | — | pre-FEL guard rows | Authorization mechanics from FEL/facturación instruments only; impresores conditional (GOQ-57) |
| FR-234 | shared | — | 98 "A".2 anchor row | Destruction of originals requires SAT authorization; GT-EINV 04 owns mandate chronology |
| FR-235 | saas | external-data sync (RTU) + notification config | mailbox, e-payment, RTU update hooks | Odoo surfaces notifications and profile sync results |

## 6. Acceptance Criteria

- **AC-001:** Given any CT-derived configuration row, when its provenance is
  inspected, then it carries the qualifier "D-6-91, consolidado hasta el
  Decreto 37-2016 (31-08-2016) + anotaciones CC hasta el 03-12-2019" and no
  row claims post-2016 legislative currency (GOQ-53). (FR-195; LB-001,
  LB-002)
- **AC-002:** Given a sanction row proposed with provenance citing only an
  SAT resolution/reglamento, when validated against the citation hierarchy,
  then it is rejected — sanctions, procedures and prescription trace to
  statute only (reserve-of-law). (FR-194)
- **AC-003:** Given a taxpayer first invoice or filing, when the NIT field
  is empty, then the record is blocked; and given any document with omitted/
  altered NIT, then the FR-214 numeral-2 sanction row (Q100.00/document,
  Q1,000.00/month, 1% cap) is what the evaluator references — while the NIT
  validation algorithm itself never cites the CT (GOQ-54 pointer).
  (FR-198, FR-199)
- **AC-004:** Given the void-text guards, when any surface quotes or
  implements an IVA-régimen-suspension power citing art. 120 or art. 120
  "A", then it is refused: suspension hooks cite CT 98 "A".2 only (R21);
  art. 94.19's value-update mechanism is likewise absent. (FR-202, FR-215)
- **AC-005:** Given an obligation due on date D with no interruption events,
  when the prescription clock runs, then it expires 4 years from D (8 years
  if the taxpayer is unregistered); given any of the 9 art. 50 events on
  date E, then the clock restarts in full from E; given the adjustment
  audiencia notification alone, then the clock does NOT restart. (FR-203,
  FR-204, FR-205)
- **AC-006:** Given a sanction that became firm on date F, when the sanction
  clock runs, then it expires 5 years from F — independent of the obligation
  clock; given payment of a prescribed debt, then it is never refunded
  (waiver) and accessory obligations are extinguished with the principal.
  (FR-206, FR-207)
- **AC-007:** Given a self-assessed late payment of tax T delayed d days,
  then mora = T × 0.0005 × d, stacked on resarcitorio interest at the
  ingested JM semester rate (never a hard-coded rate); given an audit
  adjustment instead, then mora does not apply and the 100% omission
  sanction does. (FR-209, FR-210, FR-211)
- **AC-008:** Given a retention agent that withheld R and entered it late
  voluntarily before any requirement, then the sanction evaluated is 50% of
  R; given entering only after requirement + 30 días hábiles, then the
  arts. 70/90 escalation path is recorded and no double sanction for the
  same act exists (art. 90). (FR-212, FR-218)
- **AC-009:** Given the GOQ-120 divergence, when the retención-omission
  sanction rows are inspected, then BOTH texts appear verbatim (art. 91:
  100% of retained/perceived/IVA, 50% pre-requirement; art. 94.7:
  impuesto-equivalent of the omission, no exemption from entering) with the
  divergence unresolved and evaluation keyed on the infraction committed.
  (FR-213; LB-026)
- **AC-010:** Given the art. 94 seeded table, when inspected, then all 18
  live numerals are present with the exact values of FR-214 (every Q value
  with its numeral), percent-capped rows key on the último período mensual
  con ingresos reportados, and numeral 19 exists only as a void guard.
  (FR-214, FR-215)
- **AC-011:** Given a cierre temporal sanction, then the recorded range is
  10–20 continuous days with the duplication ground, the commutation floor
  is Q10,000.00 (≤10% of the establishment's gross income; Q5,000.00 for
  pequeño contribuyente), and recidivism within 4 years raises a
  tax-based fine by 50% capped at the tax amount. (FR-216, FR-217, FR-218)
- **AC-012:** Given a rectification attempted after audiencia
  notification, then it is recorded as legally void; given one filed before
  it with simultaneous payment, then the 50% interest rebate and mora
  reduced to 15% apply and the prescription computation restarts from the
  rectification. (FR-224, FR-205)
- **AC-013:** Given the procedure/recursos clocks, when a dispute workflow
  runs, then the deadlines chain 10 dh (requerimiento) → 30 dh/10 dh
  (audiencia) → 30 dh (resolution; 115/85-day officer deadlines) → 10 dh
  (revocatoria) → 3 dh (ocurso, 15-d silence granted) → 30 d (silencio
  administrativo → contencioso), each as a dated row with GOQ-53 provenance.
  (FR-225, FR-227)
- **AC-014:** Given books with entries older than 2 calendar months not yet
  recorded, then the ledger-currency metric flags the backlog (Q5,000.00
  per fiscalización exposure, art. 94.4) and the art. 85.4 hook is quoted
  only with its [sic] flag (GOQ-56); electronic-books rules never cite CT
  art. 69 (R29 — LET/LAT corpus owns them). (FR-231)
- **AC-015:** Given record retention, then the policy is expressed as
  prescription-anchored (4y/8y via FR-203/204), never as a CT-printed
  "X años" table, and the concrete archive matrix is cross-referenced to
  the C-wave deliverable (GOQ-124) rather than restated here. (FR-232)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text from the register (abbreviated where noted). All rows Status
open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-53 (owned): "CT currency window: copy consolidated legislatively through D-37-2016 + CC through 03-12-2019; no 2017-2026 CT reform verifiable — verify against current consolidation before any CT citation as 'vigente'." Mitigated by the mandatory qualifier on every row of this file (FR-195). | no | GT synthesis wave S-GT2 → acquisition queue (current CT consolidation) | open |
| OQ-002 | GOQ-54 (owned) + GOQ-49 (kin): "NIT structure/format/check-digit rules: CT never housed them — source from RTU/reglamento corpus"; kin GOQ-49 "NIT check-digit coefficient table not printed… obtain before implementing mod-11" (S-GT1 owns it, `03_validation-rules §7`). Affects FR-199 (pointer FR only). | no | GT synthesis wave S-GT2 → RTU/reglamento acquisition; S-GT1 owns GOQ-49 | open |
| OQ-003 | GOQ-55 (owned): "Resarcitorio numeric rates = Junta Monetaria semester publications, external — rate table must be sourced before interest CRs are final." Affects FR-209: the ingestion feed (saas external-data service) has no seeded values until sourced. | no | GT synthesis wave S-GT2 → acquisition queue (SAT/JM semester publications) | open |
| OQ-004 | GOQ-56 (owned): "Art. 85.4 prints redundant '…autorizado y habilitado… y habilitado…' [sic] — confirm sense vs clean edition." Affects FR-231: the numeral is quoted only with the [sic] flag until confirmed. | no | GT synthesis wave S-GT2 → acquisition queue (clean CT edition) | open |
| OQ-005 | GOQ-57 (owned, conditional): "Pre-FEL facturación/impresores regime (reglamentario) not in corpus — needed only if legacy-document requirements arise." Affects FR-233 (guard row only; no legacy-document FR exists in this file). | no | GT synthesis wave S-GT2 (conditional — acquire only on legacy-document demand) | open |
| OQ-006 | GOQ-120 (record finding): "Retención-omission multa basis: CT art. 91 (65_) vs CT art. 94 num. 7 (64_) — verify vs current consolidated CT." Recorded in LB-026/FR-213 with both texts verbatim, divergence unresolved (no in-corpus resolution possible — 25_ is the consolidated CT); no winner picked. | no | GT synthesis wave S-GT2 → record standing; resolve only with a newer consolidation (folds into OQ-001) | open |
| OQ-007 | GOQ-124 (kin-pointer): "Retention/destruction max-per-object matrix (synthesis deliverable): practical floor = tax corpus (CT 112 "A", 4y+)" — the matrix itself is written in the S-GT5/C-wave file; this file only anchors the prescription basis (FR-232). | no | GT synthesis wave S-GT2 → C-wave deliverable (S-GT5 file) | open |
