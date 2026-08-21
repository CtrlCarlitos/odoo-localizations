# GT — Payroll — IRTRA and INTECAP patronal charges: impuesto de recreación and tasa patronal (flat 1% each, IGSS-collected)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the two IGSS-collected patronal charges every
IGSS-registered Guatemalan private employer carries alongside its
contributions: the IRTRA *impuesto de recreación* (recreation tax) —
created by **Decreto Número 1528 of 1962** (NOT "Decreto 15 de 1928",
R31), a **flat 1% on the TOTALITY of planillas** (sueldo/salario
ordinario y extraordinario devengado monthly per worker), patronal-only,
with **NO bracket table anywhere** (R32 myth rejection — negative FR) —
and the INTECAP *tasa patronal* (employer rate) of **Decreto 17-72**
art. 28 — monthly, on the *totalidad de las planillas de sueldos y
salarios*, with the 0.50%→0.75%→1.00% ceiling ladder as dated rows, the
in-force **1%** evidenced via the Reglamento de Recaudación of 1980
art. 9º (the escalonado-confirmation acta is absent — GOQ-89). It
carries the payer universes (private employers in the lucrative
production-of-goods/services process; agropecuario permanentes with the
≥10/<10 threshold and the >1-year permanente test), the exceptions
(universities, non-lucrative privates, non-IGSS-subject employers), the
up-to-80% own-training rebate as a per-employer effective-rate
mechanism, the deadline — **within the first 20 days of the month
following the planilla month, together with the IGSS contributions on
presenting the planillas** (the only printed planilla-window value in
the corpus) — the base = salaries stated in the IGSS planillas (Task 7
feed), the IGSS collection fees (INTECAP's clean 2% retention vs
IRTRA's arithmetically ambiguous art. 16 "0.25% DEL 1%" — never
resolved by guess, GOQ-85), the single-receipt ride (file 07), the
INTECAP enforcement ladder (de-oficio +5% cap Q500; mora 1–15%;
multa Q25–Q250; convenios 24 months @ 11%) with its GOQ-89
OCR-restoration flags, and the incentivo non-contributory interplay
consumed by id from file 04.

It does **not** cover: the salario/salario-completo model feeding the
ordinary/extraordinary tagging (`01_ct-salary-model.md` — GT-PAY-FR-005
consumed by id); the salario mínimo chassis (`03_minimum-wage.md`);
statutory bonuses and the incentivo flag's own regime
(`04_statutory-bonuses.md` — GT-PAY-FR-091 consumed by id);
IGSS contributions, the Planilla Electrónica lifecycle, the payment
event/single Recibo Electrónico and the IGSS-side mora/RD apparatus
(`07_igss-contributions.md` — GT-PAY-FR-170/174/177/181 consumed by
id); ISR/IVA payroll interfaces (`09_isr-iva-interfaces.md`); or SSO
obligations (`10_sso-provenance.md`). The only external ids cited are
GT-TAX-FR-146 (salaries off the IGSS planilla are employer-non-
deductible) and GT-TAX-FR-167 (the ISR deduction-cap surface consuming
both charges' deductibility).

## 2. Legal Basis

Authority order (binding, per master evidence index P5): **IRTRA =
flat 1%, D-1528 art. 12 as reformed by "Decreto 43.92" — NO brackets
(R32; EVID-353)**; identity = Decreto Número 1528 of 1962 (R31 — never
"Decreto 15 de 1928"); **INTECAP = 1% in force (D-17-72 art. 28 ceiling
ladder; in-force confirmation ONLY via Reglamento-1980 art. 9º —
GOQ-89)**, deadline within the **first 20 días** together with the IGSS
planillas (Reglamento-1980 art. 7º). Provenance guards: the `42_`
source is a substituted-glyph cipher print — all numbers, rates, dates
and article numbers quoted from it are digit-glyph deterministic
(cipher appendix, EVID file); its file NAME carries the R31 mislabel
("D15-1928") while its CONTENT is Decreto 1528 of 1962. Rejected myths
never implemented: no IRTRA bracket table of any shape (R32), no
pre-reform (pre-"Decreto 43.92") art. 12 text assertion (GOQ-84), no
AG 5-2005/6-2005 rate content (governance only, EVID-357/359).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Decreto Número 1528, Congreso de la República (identity + date blocks): "DECRETO NUMERO 1528" / "EL PRESENTE DECRETO ENTRARA EN VIGOR EL DIA PRIMERO DE JULIO DE MIL NOVECIENTOS SESENTA Y DOS." / "DADO EN EL PALACIO DEL ORGANISMO LEGISLATIVO, EN GUATEMALA, A LOS VEINTINUEVE DIAS DEL MES DE MAYO DE MIL NOVECIENTOS SESENTA Y DOS." / "PALACIO NACIONAL, GUATEMALA, TREINTA Y UNO DE MAYO DE MIL NOVECIENTOS SESENTA Y DOS. PUBLIQUESE Y CUMPLASE." / "MIGUEL YDIGORAS FUENTES" | IRTRA's creating law = congressional Decreto 1528 (given 29-May-1962; promulgated 31-May-1962 by President Miguel Ydígoras Fuentes; effective 1-Jul-1962 fixed by art. 28, a calendar date independent of the unprinted DCA publication) — the corpus file label "D15-1928" is a misreading; every date in the document is 1962 (R31) | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | p.1; header at end of text layer; art. 28 + date/signature blocks, raw lines 213-234 (EVID-351) |
| LB-002 | Decreto 1528, ARTICULO 12º (texto según reforma "Decreto 43.92"): "SE CREA UN IMPUESTO EQUIVALENTE AL UNO POR CIENTO (1%), SOBRE EL MONTO DEL SUELDO O SALARIO ORDINARIO Y EXTRAORDINARIO DEVENGADO MENSUALMENTE POR CADA TRABAJADOR DE LAS EMPRESAS PRIVADAS, PORCENTAJE QUE SERA CALCULADO SOBRE LA TOTALIDAD DE LAS PLANILLAS. EL IMPUESTO SERA PAGADO POR LAS EMPRESAS O PATRONOS PARTICULARES QUE ESTEN INSCRITOS O SE INSCRIBAN EN EL REGIMEN DE SEGURIDAD SOCIAL. LA JUNTA DIRECTIVA DEL INSTITUTO DE RECREACION DE LOS TRABAJADORES DE LA EMPRESA PRIVADA DE GUATEMALA, EMITIRA LOS ACUERDOS QUE INDIQUEN LAS ACTIVIDADES ECONOMICAS AFECTAS AL PAGO DEL IMPUESTO. ESTE IMPUESTO NO AFECTA LOS EMOLUMENTOS DE LOS TRABAJADORES." + trailing tag "[REFORMADO POR EL ARTICULO 2 DEL DECRETO NUMERO 43.92 DEL ONGRESO [sic CONGRESO] DE LA REPUBLICA]" | THE IRTRA charge: a tax equal to 1% on the monthly earned ordinary and extraordinary salary/wage of each worker of private enterprises, computed on the totality of the planillas; paid by private enterprises/patrons registered (or registering) in the social-security regime; the Junta Directiva issues the acuerdos indicating the economic activities affected; the tax does NOT affect the workers' emoluments (patronal-only). As printed = post-"Decreto 43.92" text (reform tag; pre-reform wording unrecoverable, GOQ-84) | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | Art. 12º p.1, raw lines 122-131 + reform tag (EVID-352) |
| LB-003 | NEGATIVE FINDING, Decreto 1528 whole text (decoded end-to-end, arts. 1-28): exhaustive inventory of every monetary/quantitative string in the law: "(1%)" (art. 12); "EL 0.25% DEL 1% DEL PRODUCTO DEL IMPUESTO" (art. 16); "NUMERO 495," [sic — Acuerdo Presidencial number, art. 19]; "TREINTA DIAS" / "SETENTA DIAS" (art. 26); "DOS VECES AL MES" (art. 8); "DOS ANOS" (art. 7); digits otherwise appear only in article numbers 1-28 and date blocks | NO bracket table, no per-worker-count brackets, no capital tiers exist in D-1528 as printed; neither AG 5-2005 nor AG 6-2005 contains any cuota table or rate change (the "AG 5-2005 = bracket update" hypothesis is disproven); the IRTRA charge is a flat 1% — any bracket structure could only have lived in the pre-D-43-92 art. 12 wording, NOT in this corpus (R32 verdict) | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | Whole text (decoded), arts. 1-28 (EVID-353) |
| LB-004 | Decreto 1528, arts. 14-16: art. 14: "LA RECAUDACION DEL IMPUESTO QUE SE CREA EN EL ARTICULO 12 DE ESTA LEY, LA HARA EL INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL EN EL ACTO DE RECAUDAR ESTE [SUS] PROPIAS CONTRIBUCIONES ORDINARIAS, DEBIENDO DICHA ENTIDAD, PONER A DISPOSICION DEL INSTITUTO, EL IMPORTE DE LOS FONDOS PERCIBIDOS MENSUALMENTE DURANTE EL MES SIGUIENTE A SU RECAUDACION…" / art. 15: "LOS PATRONOS QUE NO HICIEREN EL PAGO… DENTRO DEL TERMINO QUE EJE [sic FIJE] EL INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL PARA SUS PROPIAS CONTRIBUCIONES, SERAN SANCIONADOS DE ACUERDO CON LAS NORMAS ESTABLECIDAS POR ESTE, PARA SUS AFILIADOS." / art. 16: "EL INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL DEVENGARA EL 0.25% DEL 1% DEL PRODUCTO DEL IMPUESTO QUE ESTABLECE ESTA LEY, POR LOS GASTOS QUE LE OCASIONE EL COBRO Y MANEJO DE LAS CUENTAS RESPECTIVAS." | IGSS collects the IRTRA tax in the act of collecting its own ordinary contributions and must place the funds at IRTRA's disposal monthly during the month following collection; the employer deadline is whatever term IGSS fixes for its own contributions, with late payers sanctioned under IGSS's own afiliado rules; IGSS earns a collection fee reading "0.25% DEL 1%" of the tax product — glyph-deterministic but arithmetically ambiguous drafting (0.25% of the 1% tax vs a quarter of the 1% = 0.25 pp of payroll), flagged never resolved (GOQ-85) | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | Arts. 14-16 p.1, raw lines 148-163 (EVID-354) |
| LB-005 | Decreto 1528, arts. 2, 3 y 22: art. 2: "SE CREA EL INSTITUTO DE RECREACION DE LOS TRABAJADORES DE LA EMPRESA PRIVADA DE GUATEMALA, QUE PODRA SER DENOMINADO IRTRA, COMO UNA INSTITUCION AUTONOMA, DE DERECHO PUBLICO…" / art. 3: "NINGUN TRABAJADOR ESTA OBLIGADO A AELIARSE [sic AFILIARSE] NI A CONCURRIR CONTRA SU VOLUNTAD A LOS CENTROS DE RECREACION. EL INSTITUTO DARA A SUS AELIADOS UN CARNET, SIN COSTO NI TRAMITE ALGUNO, PARA TENER DERECHO A RECIBIR LOS BENEFICIOS QUE CONCEDA." / art. 22: "EL IMPUESTO CREADO POR EL ARTICULO 12 DE ESTE DECRETO, SERA DEDUCIBLE DE LAS UTILIDADES LIQUIDAS DE LAS EMPRESAS O ENTIDADES AFECTAS POR ESTA LEY." | IRTRA = autonomous public-law entity (short name added by D-43-92 art. 1); NO worker is obliged to affiliate or to attend the recreation centers against his will, and the affiliation carnet issues free, without any formality, as the right to receive the benefits granted; the art. 12 tax is deductible from the net profits ("utilidades líquidas") of the affected enterprises/entities — pre-LAT income-tax language, read against modern ISR deducibility | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | Arts. 2-3 p.1, raw lines 38-49; art. 22, raw lines 180-186 (EVID-355) |
| LB-006 | Decreto 1528, arts. 7, 8 y 26: art. 26: "LA JUNTA DIRECTIVA DEL INSTITUTO DEBERA ORGANIZARSE DENTRO DE LOS TREINTA DIAS POSTERIORES A LA VIGENCIA DE ESTA LEY, Y SUS ESTATUTOS Y REGLAMENTOS, LOS QUE DEBERAN SER APROBADOS POR ACUERDO GUBERNATIVO, DEBERAN EMITIRLOS DENTRO DE SETENTA DIAS CONTADOS DESDE LA FECHA DE SU ORGANIZACION." | 1962 governance: Junta of 9 propietarios (Ejecutivo 1, Cámara de Comercio 1, Cámara de Industria 2, AGC 1, AGA 2, trabajadores organizados 2) + a suplente each; ordinary sessions at least twice a month; art. 26 is the statutory hook making estatutos/reglamento subject to Acuerdo Gubernativo approval — the lineage AG 689-1963 / AG 735-1964 that AG 5-2005/6-2005 later replace (governance numbers, never payroll values) | `gt/sources/42_IRTRA_Ley_D15-1928.pdf` | Arts. 7-8 p.1, raw lines 88-106; art. 26, raw lines 200-206 (EVID-356) |
| LB-007 | Acuerdo Gubernativo 5-2005: "ARTICULO 1. Aprobar los Estatutos del Instituto de Recreación de los Trabajadores de la Empresa Privada de Guatemala -IRTRA- contenido en el Acuerdo de la institución número 02-2004 de fecha 20 de julio del año 2004." / "ARTICULO 2. Se deroga el Acuerdo Gubernativo número 689 de fecha 27 de septiembre del año 1963." / "ARTICULO 3. El presente Acuerdo surte sus efectos a partir de la fecha de su publicación en el Diario de Centro América, órgano oﬁcial del Estado." / signed "OSCAR BERGER" (MinTrabajo: Ing. Jorge Gallardo Flores) | AG 5-2005 approves IRTRA's new Estatutos (Junta Acuerdo 02-2004, adopted 20-Jul-2004) and repeals AG 689-1963; effects from DCA publication (date not printed; the only printed date is the INFILE generation stamp 12-Jan-2005 — GOQ-86); contains NO cuota amounts, rates or brackets anywhere — pure governance (disproves the bracket-update hypothesis) | `gt/sources/43_IRTRA_AG_5-2005.pdf` | p.1, ACUERDA block + signature block (EVID-357) |
| LB-008 | IRTRA Estatutos (2004, approved by AG 5-2005) art. 7: "Todos los patronos y empresas particulares que forman parte del proceso lucrativo de producción de bienes y prestación de servicios en el país, están obligados a contribuir al sostenimiento del IRTRA, de conformidad con la ley y los acuerdos de aplicación que para el efecto se emitan. Los trabajadores al servicio de patronos y empresas particulares que forman parte del proceso lucrativo de producción y prestación de servicios, afectos al pago del Impuesto de Recreación, de conformidad con los Acuerdos que para el efecto emita la Junta Directiva, tendrán derecho de percibir para sí y sus familiares los servicios que ofrezca la Institución…" | Operative 2005-era scope: every employer forming part of the LUCRATIVE production-of-goods/services process in the country owes the IRTRA contribution; the charge is consistently called Impuesto de Recreación; afectación detail lives in Junta Directiva acuerdos (activity lists — not in corpus, GOQ-91); workers (and family) of affected employers receive the services; no rates here | `gt/sources/43_IRTRA_AG_5-2005.pdf` | p.1, Estatutos CAPITULO II CAMPO DE APLICACIÓN, ARTICULO 7 (also art. 6) (EVID-358) |
| LB-009 | Acuerdo Gubernativo 6-2005: "ARTICULO 1. Aprobar el Reglamento de la Junta Directiva del Instituto de Recreación de los Trabajadores de la Empresa Privada de Guatemala IRTRA- contenido en el Acuerdo de la institución número 01-2004 de fecha 20 de julio del año 2004." / "ARTICULO 2. Se deroga el Acuerdo Gubernativo número 735 de fecha 15 de abril del año 1964." / Reglamento art. 7: "La Junta Directiva debe reunirse por lo menos una vez a la semana en sesiones ordinarias… Cinco directores propietarios… formarán quórum…" | AG 6-2005 approves the Junta's Reglamento (Acuerdo 01-2004, 20-Jul-2004) and repeals AG 735-1964; governance deltas: weekly sessions (law: ≥2/month), 9 propietarios + 6 suplentes; budget approved before 30-Jun effective 1-Jan; NO cuota/rate content; its POR TANTO cites D1528 "artículos 8o. y 26º" with meanings mismatching the 42_ print's numbering (renumbering outside corpus — GOQ-87) | `gt/sources/44_IRTRA_AG_6-2005.pdf` | p.1, ACUERDA block; Reglamento arts. 2, 7, 8 (EVID-359) |
| LB-010 | Ley Orgánica INTECAP, Decreto No. 17-72, art. 38 + date blocks: "El presente Decreto entrará en vigor el día de su publicación en el Diario Oﬁcial." / "Dado en el Palacio del Organismo Legislativo, en la ciudad de Guatemala, a los veintiséis días del mes de abril de mil novecientos setenta y dos." / "Palacio Nacional: Guatemala, diez y ocho de mayo de mil novecientos setenta y dos. — Publíquese y cúmplase, CARLOS ARANA OSORIO…" / reform tags: "(Art. 1º. Decreto Ley 783)" [sic] (art. 13), "(Art. 2º. Decreto Ley 7 -83)" (art. 14) | INTECAP's organic law: given 26-Apr-1972, promulgated 18-May-1972; effective on DCA publication — the DCA date is NOT printed, so the effective date is not derivable from this file (GOQ-88); consolidated print with Decreto Ley 7-83 reform tags (Junta-side arts. 13-14); INTECAP = Instituto Técnico de Capacitación y Productividad, substitutes CENDAP (art. 36), derogates D57-69 (art. 37) | `gt/sources/45_INTECAP_Ley_Organica.pdf` | Title block p.1; art. 38 + date blocks pp.10-11 (EVID-360) |
| LB-011 | Decreto 17-72, ARTICULO 28: "…se establece a su favor una tasa patronal que será pagada mensualmente por las empresas y entidades privadas, y por las entidades públicas que realicen actividades con ﬁnes lucrativos, sobre la totalidad de las planillas de sueldos y salarios, exceptuándose aquellas que no sean sujeto de contribución del Instituto Guatemalteco de Seguridad Social (IGSS)." / "1. Las empresas de los sectores industrial, comercial y de servicios, principiarán a pagar a partir del 1º de junio de 1972, una tasa de 0.50% del valor de sus planillas mensuales de sueldos y salarios. Durante el año de 1973 el monto del pago de la tasa se elevará a 0.75%, y a partir del 1º de enero de 1974 podrá alcanzar su límite máximo del 1.00%…" / "2. Las empresas del sector agropecuario comenzarán a pagar la tasa a partir del 1º de enero de 1973, por un monto del 0.5 0% [sic] del valor mensual de sus planillas de sueldos y salarios de sus trabajadores permanentes. Durante el año 1974 el monto de la tasa se podrá elevar a 0.75%, y a partir del 1º de enero de 1975 podrá alcanzar su valor máximo del 1.00%, de sus trabajadores permanentes, exclusivamente… Asimismo, se exonera de la tasa reversible [sic]… a las empresas agropecuarias con menos de 10 trabajadores permanentes." / closing: "…deberá entenderse por trabajadores permanentes, aquellos que presten sus servicios en una empresa agropecuaria por más de un año sin interrupción en sus labores." | THE INTECAP rate clause: monthly tasa patronal on the totality of the salary planillas; liable = private empresas/entidades + public entities with lucrative activities; carve-out = employers not subject to IGSS contribution. Staircase: industrial/comercial/servicios 0.50% (1-Jun-1972) → 0.75% (during 1973) → 1.00% ceiling (1-Jan-1974); agropecuario permanentes-only 0.50% (1-Jan-1973) → 0.75% (during 1974) → 1.00% ceiling (1-Jan-1975); any rise above 0.50% required prior Junta verification recorded in acta (inciso 3 — acta not in corpus, GOQ-89); agro entities with <10 permanent workers exonerated; permanente = >1 year uninterrupted service | `gt/sources/45_INTECAP_Ley_Organica.pdf` | Art. 28 intro + incisos 1-2 + closing definition, pp.9-10 (EVID-361) |
| LB-012 | Decreto 17-72, arts. 29, 30 y 33: art. 29: "Se exceptúan del pago de esta tasa las Universidades legalmente establecidas en el país y las empresas o entidades privadas que no persiguen ﬁnes lucrativos." / art. 30: "El monto y pago de la tasa podrá ser rebajado hasta en un 80% cuando una empresa o entidad, mediante convenio suscrito con el Instituto, realice sus propios programas de formación profesional. El monto de la rebaja se establecerá de acuerdo con el número de trabajadores que la empresa pueda adiestrar con sus propios medios, siempre que dicho adiestramiento sea aprobado y supervisado por el Instituto. Esta rebaja tomará la forma de reembolso trimestral del Instituto basado en el convenio referido." / art. 33: "Las contribuciones legales, donaciones o pagos que hagan las empresas o personas individuales a favor del Instituto serán consideradas como deducciones permitidas de la declaración y pago del impuesto sobre la renta." | Exceptions: legally established universities and non-profit private entities; up-to-80% rebate for INTECAP-approved own-training programs (rebate size by trainable-worker count, INTECAP-approved and supervised), paid as QUARTERLY reimbursement under the convenio; contributions are permitted ISR deductions | `gt/sources/45_INTECAP_Ley_Organica.pdf` | Arts. 29, 30 y 33 p.10 (EVID-362) |
| LB-013 | Decreto 17-72, arts. 31 y 32: art. 31: "La tasa será recaudada por el Instituto Guatemalteco de Seguridad Social, IGSS, al mismo tiempo que recaude sus propias contribuciones, depositándose el monto cobrado directamente en la cuenta bancaria del INTECAP. Queda entendido que quedarán excluidas del cobro las empresas o entidades exceptuadas en esta ley. El IGSS recibirá por este servicio el 2% del monto de las sumas recaudadas, que deducirá de las mismas." / art. 32: "El incumplimiento a cualquiera de las disposiciones de la presente ley constituye falta a las leyes de trabajo y previsión social, aplicándose lo preceptuado en el inciso C del artículo 272 del Código de Trabajo. El incumplimiento en el pago de las tasas da lugar a su cobro por la vía económico-coactiva por el Instituto. Un reglamento específico normará lo relativo a multas y recargos." | IGSS collects the tasa together with its own contributions and deposits directly to INTECAP's bank account; IGSS's fee = a clean 2% of sums collected, deducted from them (contrast IRTRA's ambiguous art. 16, LB-004); noncompliance = a falta to labor/social-security laws under CT art. 272 inc. C, unpaid tasas collectible via the económico-coactivo path; multas/recargos delegated to a specific reglamento (= the 1980 Reglamento) | `gt/sources/45_INTECAP_Ley_Organica.pdf` | Arts. 31 y 32 p.10 (EVID-363) |
| LB-014 | Reglamento de Recaudación de la Tasa Patronal a favor del INTECAP (Junta Directiva): "…de conformidad con el artículo 32 de la Ley Orgánica… un reglamento especíﬁco normará lo relativo a la recaudación de la Tasa Patronal y a las multas y recargos que se causen" / "ARTICULO 32.- Se deroga el Acuerdo de esta Junta emitido el veintidós de abril de mil novecientos setenta y siete…" / "ARTICULO 33.- El presente Reglamento entra en vigencia treinta días después de su publicación en el Diario Oﬁcial." / "Dado en el Salón de Sesiones de la Junta Directiva del Instituto Técnico de Capacitación y Productividad, el día veintitrés del mes de abril de mil novecientos ochenta." | The operational rulebook issued by INTECAP's Junta under art. 32 of the law: given 23-Apr-1980; replaces the 22-Apr-1977 reglamento; vigencia 30 days after DCA publication (date not printed); transitory 60-day amnesty — patrons paying all arrears within 60 days of vigencia pay no recargos (art. 31º); OCR is rough (lost ordinals, garbled amounts — restorations flagged per EVID-367) | `gt/sources/46_INTECAP_Reglamento_Tasa_Patronal.pdf` | Cover + considerandos + arts. 1º, 31-33 + date block, pp.1-3 (EVID-364) |
| LB-015 | Reglamento de Recaudación, arts. 2º/4º/5º: art. 2º: "Esta Tasa deberá pagarse por las empresas y entidades privadas de los sectores industrial, comercial y de servicios y por las entidades públicas que realicen actividades con ﬁnes lucrativos sobre latotalidad [sic] de los salarios, exceptuándose aquellas que no sean sujeto de contrivución [sic contribución] del Instituto Guatemalteco de Seguridad Social. También están obligadas al pago de la Tasa Patronal las empresas del sector agropecuario con 10 o más trabajadores permanentes. Se entiende por trabajadores permanentes, aquellos que presten sus servicios en una empresa agropecuaria por más de un ano [sic año] sin interrupciones en sus labores." / art. 4º: "Están exoneradas de la Tasa Patronal las empresas agropecuarias con menos de diez trabajadores permanentes." / art. 5º: "La Tasa Patronal es exclusivamente a cargo de las empresas o entidades patronales, por lo que en ningún caso podrá descontarse de los salarios de los trabajadores." | Payer universe restated: private industrial/comercial/servicios + lucrative public entities, on the totality of salaries, except non-IGSS-subject employers; agropecuarias with ≥10 permanent workers OBLIGED (permanente = >1 year uninterrupted — same test as the law); <10 EXONERATED (same threshold from both sides); hard guard: the tasa is exclusively the employer's charge and may NEVER be discounted from workers' salaries | `gt/sources/46_INTECAP_Reglamento_Tasa_Patronal.pdf` | Arts. 2º, 4º, 5º p.2 (EVID-365) |
| LB-016 | Reglamento de Recaudación, arts. 7º/8º/9º: art. 7º: "La Tasa Patronal deberá pagarse juntamente con las contribuciones del Instituto Guatemalteco de Seguridad Social, al presentarse las planillas que sirven de base para el cálculo y pago de dichas contribuciones, dentro de 'os [sic los] primeros veinte días del mes siguiente al que correspondan." / art. 8º: "La Tasa Patronal se calculará y liquidará sobre el monto de los salarios consignados en las planillas de seguridad social, utilizando para el efecto las mismas planillas." / art. 9º: "La Tasa Patronal vigente se calculará y pagará a razón del uno por ciento del valor de los salarios mensuales." | THE operational anchors: deadline = together with the IGSS contributions, on presenting the planillas, within the FIRST 20 DAYS of the month following the planilla month (the IGSS planilla window — the only printed planilla-window value in the corpus); base/liquidation = the salaries stated in the security-social planillas, using the same planillas; rate in force = 1% (uno por ciento) of monthly salaries — the corpus' cleanest in-force 1% statement for INTECAP, confirming the escalonado ceiling was reached by 1980 (acta itself absent, GOQ-89) | `gt/sources/46_INTECAP_Reglamento_Tasa_Patronal.pdf` | Arts. 7º, 8º, 9º p.2, CAPITULO II (EVID-366) |
| LB-017 | Reglamento de Recaudación, arts. 13º/18º/21º/22º/24º/25º/28º: art. 13º: "…El Instituto podrá liquidar de oﬁcio dicha Tasa con base en los salarios consignados en la última planilla de Seguridad Social presentada, cuyos resultados serán operados, en el registro contable de El Instituto, sin previa notificación al patrono." / art. 18º: "A las liquidaciones de oﬁcio… un recargo adicional equivalente al cinco por ciento de su monto… en ningún caso podrá ser mayor de 0.500.00 [sic — Q.500.00] en cada liquidación." / art. 21º: "El Gerente queda facultado para conceder a los patronos un plazo hasta de veinticuatro meses, para pagar la Tasa Patronal en mora…" / art. 22º: "Los convenios de pago devengarán intereses a razón de once por ciento anual sobre la Tasa Patronal…" / art. 24º: mora recargo per the scale "Primer mes… Décimo quinto mes" with values "10/0 20/0 30/0 … 150/0" [sic — 1%…15%], "En ningún caso el recargo por mora podrá exceder el quince por ciento (150/0) [sic] del monto global del pago omitido… Los porcentajes de recargo no son acumulativos y se aplicarán al monto global de la tasa…" / art. 25º: "…aplicándose para el efecto una multa entre veinticinco (0.25) [sic — Q.25.00] y doscientos cincuenta quetzales, (Q.250.00l [sic], mediante el procedimiento establecido en el Código de Trabajo para el juzgamiento de faltas, sin perjuicio del cobro de la Tasa Patronal por la vía económico-coactiva." / art. 28º: on substitution of patrono, both must notify El Instituto "dentro de los diez días hábiles siguientes"; the substituted patrono is "solidariamente responsable… hasta el término de seis meses" | Enforcement ladder: de-oficio liquidation from the last IGSS planilla presented (no prior notification), +5% surcharge capped Q500 per liquidation; mora surcharge 1%→15% by elapsed month (15-month scale), NON-cumulative, applied to the global omitted amount, global cap 15%; multa Q25–Q250 via the CT faltas procedure (plus económico-coactivo); moratory payment convenios up to 24 months at 11% annual interest; employer-substitution notice within 10 días hábiles with 6-month solidary liability. OCR-garbled amounts restored in brackets — verify against a clean copy (GOQ-89) | `gt/sources/46_INTECAP_Reglamento_Tasa_Patronal.pdf` | Arts. 13º-28º, CAPITULOs III, V, VI, VII, pp.2-3 (EVID-367) |

Dead print — never implementable as current-period values (LB note, not
FRs): (i) the D-1528 governance numbers (30/70-day organizing windows,
≥2/month sessions) and the 2005 Reglamento's weekly-session/budget
calendar — governance provenance only; (ii) the Reglamento-1980
transitory 60-day recargo amnesty (art. 31º) — a 1980 boundary row,
never a live waiver; (iii) the art. 16 IGSS fee "0.25% DEL 1%" —
ambiguous drafting, NO numeric value encoded (GOQ-85); (iv) the ladder
rows above the in-force anchor (0.50%/0.75% and the ceiling transition
dates) are historical dated rows — the in-force rate resolves ONLY
through the Reglamento-1980 art. 9º anchor (GOQ-89 acta gap). Edition
discipline: the `42_` print is a consolidated text (post-"Decreto
43.92" reform tags) read through the digit-deterministic glyph decode —
all quoted numbers are glyph-proven; D-1528 article numbers are cited
only against this print (GOQ-87); `43_`/`44_` print no AG/DCA dates
(GOQ-86); `45_` prints no DCA date (GOQ-88); `46_` restorations flagged
(GOQ-89).

## 3. Functional Requirements

### 3.1 Instruments, identity and citation guards

- **GT-PAY-FR-185:** The system shall register the IRTRA instrument
  lineage as dated rows with the R31 identity verbatim: the creating
  law = **Decreto Número 1528 del Congreso de la República** of 1962
  (given 29-May-1962; promulgated 31-May-1962, Miguel Ydígoras
  Fuentes; vigencia **fixed 1-Jul-1962** by art. 28 — a calendar date
  independent of the unprinted DCA publication). The label "Decreto 15
  de 1928" (carried by the corpus file name) is a MISREADING and shall
  never be cited; no 1928 instrument is in play. Governance lineage:
  art. 26 statutory hook (Junta organizes within 30 days of vigencia;
  estatutos/reglamentos via Acuerdo Gubernativo within 70 days of
  organizing) → AG 689-1963 (estatutos) / AG 735-1964 (Reglamento de
  la Junta) → AG 5-2005 / AG 6-2005 (approving the Junta's Acuerdos
  02-2004 / 01-2004, both of 20-Jul-2004; effects from DCA
  publication — dates not derivable, GOQ-86) — pure governance with
  ZERO rate content (EVID-357/359 disproves the bracket-update
  hypothesis; see FR-188). (LB-001; LB-006; LB-007; LB-009;
  EVID-351, EVID-356, EVID-357, EVID-359)
- **GT-PAY-FR-186:** CITATION GUARDS (ride both catalogs): (a) the
  42_ D-1528 print is CONSOLIDATED — reform tags cite "DECRETO NUMERO
  43.92" at arts. 2, 12 and 13; that decree is not in the corpus and
  the PRE-reform text of arts. 2/12/13 is unrecoverable (GOQ-84) —
  no requirement may assert pre-reform content, and the art. 12 rate
  row carries the post-reform vintage stamp; (b) D-1528 article
  numbers are cited ONLY against the 42_ print — 43_/44_ cite D1528
  "artículo 24" and "artículos 8º. y 26º." with meanings that do NOT
  match this print's numbering (intervening renumbering reforms
  outside corpus, GOQ-87); (c) 42_ quotes come from the
  substituted-glyph decode — every number, rate, date and article
  number in them is digit-glyph deterministic (cipher appendix), and
  the letter-layer decode is flagged where C/F glyph-drops occur; (d)
  AG 5-2005 / AG 6-2005 (43_/44_) contain NO cuota/rate provisions —
  never sources for IRTRA values.
  (LB-001; LB-002; LB-007; LB-009; EVID-351, EVID-352, EVID-357,
  EVID-359; GOQ-84 → OQ-001, GOQ-87 → OQ-004)

### 3.2 The IRTRA impuesto — flat 1% of the totality of planillas

- **GT-PAY-FR-187:** The system shall model the IRTRA patronal charge
  as an **impuesto** (the *impuesto de recreación* per the 2004
  Estatutos) — never a cuota — at a **flat 1%** on the *monto del
  sueldo o salario ordinario y extraordinario devengado mensualmente
  por cada trabajador*, calculated *sobre la totalidad de las
  planillas* of the private employer, monthly, per the art. 12 text
  as reformed (tag: art. 2 of "Decreto 43.92"). Payer = *empresas o
  patronos particulares* registered or registering in the IGSS
  *régimen de seguridad social*. The 1% rate is a dated shared row
  (valid_from 1962-07-01 charge creation; text vintage =
  post-"Decreto 43.92" consolidated print, GOQ-84); the base takes
  the ordinary + extraordinary salary components exactly as printed —
  operationally fed by the `01_ct-salary-model.md` GT-PAY-FR-005
  component tagging (consumed by id, never re-derived), noting R36
  kin: unlike bonus-law bases, BOTH components are in.
  (LB-002; EVID-352; cross-ref GT-PAY-FR-005)
- **GT-PAY-FR-188:** NEGATIVE FR (R32 myth rejection): NO bracket
  table exists anywhere in the IRTRA regime — the charge shall NEVER
  be modeled as size-based brackets, per-worker-count tiers, capital
  tiers or any progressive scale: the exhaustive monetary inventory
  of D-1528 contains only the art. 12 "(1%)", the art. 16 fee and
  governance numbers, and AG 5-2005/6-2005 carry no rate content. Any
  bracket claim requires an instrument OUTSIDE this corpus — until
  then, bracket-shaped IRTRA configuration is rejected at seed time
  (guard row; both catalogs).
  (LB-003; EVID-353)
- **GT-PAY-FR-189:** PATRONAL-ONLY invariant: *este impuesto no
  afecta los emolumentos de los trabajadores* — no salary-rule
  configuration may generate a worker-side deduction line for the
  IRTRA charge, and any payslip attempt to charge it (or any part of
  it) to the worker blocks posting (engine constraint; the INTECAP
  leg of the same invariant is FR-201).
  (LB-002; EVID-352)
- **GT-PAY-FR-190:** Payer universe and affected activities: the
  IRTRA liability test = a private employer, IGSS-registered (or
  registering), forming part of the *proceso lucrativo de producción
  de bienes y prestación de servicios* (Estatutos art. 7 — the
  2005-era scope kin of the art. 12 payer clause); the *actividades
  económicas afectas* are fixed by **Junta Directiva acuerdos** that
  are NOT in the corpus (GOQ-91) — the activity-list registry ships
  EMPTY as configurable dated rows, no default list is seeded, and
  afectación resolves only when a JD acuerdo row is loaded; worker
  and family service-eligibility metadata ties to the same
  afectación. (LB-002; LB-008; EVID-352, EVID-358; GOQ-91 → OQ-007)

### 3.3 IRTRA collection, worker-side and tax treatment

- **GT-PAY-FR-191:** IGSS joint collection and the ambiguous fee: IGSS
  collects the impuesto *en el acto de recaudar sus propias
  contribuciones ordinarias* and places the funds at IRTRA's disposal
  *mensualmente durante el mes siguiente a su recaudación*; the
  employer's deadline is the term IGSS fixes for its own
  contributions (art. 15 — the window VALUE owned by file 07
  GT-PAY-FR-177), with late payers sanctioned under IGSS's own
  afiliado rules (IGSS-side apparatus owned by
  `07_igss-contributions.md`). The IGSS collection fee reads *el
  0.25% del 1% del producto del impuesto* — glyph-deterministic but
  ARITHMETICALLY AMBIGUOUS (0.25% of the 1% tax vs a quarter of the
  1% = 0.25 percentage points of payroll): it shall be recorded as an
  ambiguity-flagged row with NO numeric value ever posted (GOQ-85 —
  never resolved by guess).
  (LB-004; EVID-354; GOQ-85 → OQ-002)
- **GT-PAY-FR-192:** Worker-side voluntariness: *ningún trabajador
  está obligado a afiliarse ni a concurrir contra su voluntad a los
  centros de recreación*, and the affiliation *carnet* issues *sin
  costo ni trámite alguno* — affiliation and facility use are NEVER
  payroll-driven worker obligations: modeled as HR metadata only (no
  payslip computation, no deduction, no auto-affiliation from payroll
  events). (LB-005; EVID-355)
- **GT-PAY-FR-193:** ISR deductibility feed: the IRTRA impuesto is
  *deducible de las utilidades líquidas* (art. 22 — pre-LAT
  income-tax language read against the modern ISR deducibility
  regime) and INTECAP contributions are *deducciones permitidas* for
  ISR (art. 33): both charge lines post with the
  employer-deduction tag consumed by **GT-TAX-FR-167** (the
  deduction-cap surface; values owned by `taxation/05`) — never
  re-derived here; kin feed **GT-TAX-FR-146** (salaries off the IGSS
  planilla are employer-non-deductible — the planilla surface of
  file 07 GT-PAY-FR-170).
  (LB-005; LB-012; EVID-355, EVID-362; cross-ref GT-TAX-FR-146,
  GT-TAX-FR-167)

### 3.4 INTECAP — instruments, payer universe and the tasa

- **GT-PAY-FR-194:** The system shall register the INTECAP instrument
  dated rows: Ley Orgánica = **Decreto No. 17-72** (given 26-Apr-1972;
  promulgated 18-May-1972, Carlos Arana Osorio; art. 38: vigencia on
  DCA publication — the date is NOT printed, so the effective date is
  not derivable: the dated row carries the GOQ-88 gap and asserts NO
  date); consolidated print with Decreto Ley 7-83 reform tags (arts.
  13-14, Junta-side); INTECAP substitutes CENDAP (art. 36) and
  derogates D57-69 (art. 37).
  (LB-010; EVID-360; GOQ-88 → OQ-005)
- **GT-PAY-FR-195:** INTECAP payer universe and exceptions: the *tasa
  patronal* is owed monthly by *empresas y entidades privadas* and by
  public entities conducting *actividades con fines lucrativos*, on
  the *totalidad de las planillas de sueldos y salarios*, EXCEPTING:
  (a) employers *que no sean sujeto de contribución del IGSS* (the
  non-IGSS-subject carve-out — the IGSS-subject test consumed from
  file 07's registration surface), (b) *las Universidades legalmente
  establecidas en el país*, and (c) private empresas/entities *que no
  persiguen fines lucrativos* (art. 29; reglamento art. 2º restates
  the universe and carve-out). The exemption tests are configuration
  flags on the employer record; no exemption is invented beyond the
  printed three. (LB-011; LB-012; LB-015; EVID-361, EVID-362,
  EVID-365)
- **GT-PAY-FR-196:** Agropecuario scope and the permanentes
  threshold: for the agro sector the tasa covers ONLY *trabajadores
  permanentes* — those serving *en una empresa agropecuaria por más
  de un año sin interrupción en sus labores* (law art. 28 closing =
  reglamento art. 2º, both sides); agropecuarias with **10 or more**
  permanentes are OBLIGED (reglamento art. 2º) and with **fewer than
  10** are EXONERATED (law art. 28 inc. 2 + reglamento art. 4º — the
  same threshold printed from both sides). The permanente test
  (>1 year uninterrupted) computes from contract-continuity data, and
  the permanente headcount gates the agro employer in/out; non-
  permanent agro workers never enter the INTECAP base.
  (LB-011; LB-015; EVID-361, EVID-365)
- **GT-PAY-FR-197:** The tasa ladder shall be stored as DATED ROWS
  (art. 28): *industrial/comercial/servicios* 0.50% from
  **1-Jun-1972** → 0.75% during **1973** → 1.00% ceiling from
  **1-Jan-1974**; *agropecuario permanentes* 0.50% from **1-Jan-1973**
  → 0.75% during **1974** → 1.00% ceiling from **1-Jan-1975**. Every
  rise above 0.50% required prior Junta Directiva verification
  recorded in *acta* (art. 28 inciso 3) — that acta is NOT in the
  corpus (GOQ-89): all rows above 0.50% carry the acta-gap flag. The
  IN-FORCE rate = **1%**, evidenced ONLY via Reglamento-1980 art. 9º
  (*la Tasa Patronal vigente… a razón del uno por ciento del valor de
  los salarios mensuales*) — the in-force row is anchored to art. 9º,
  never to an acta (GOQ-10 INTECAP half).
  (LB-011; LB-016; EVID-361, EVID-366; GOQ-89 → OQ-006, GOQ-10 →
  OQ-008)
- **GT-PAY-FR-198:** Own-training rebate: the *monto y pago de la
  tasa* may be reduced *hasta en un 80%* when the employer, *mediante
  convenio suscrito con el Instituto*, runs its own
  formación-profesional programs — approved and supervised by INTECAP
  — with the rebate taking the form of *reembolso trimestral* based
  on the convenio: modeled as a per-employer effective-rate reduction
  mechanism — a recorded convenio (rebaja_pct ≤ 80%, quarterly
  reimbursement postings, effective rate floor 0.2%); the convenio's
  approval/supervision state is INTECAP-side data imported as
  configuration, never self-declared.
  (LB-012; EVID-362)
- **GT-PAY-FR-199:** The Reglamento de Recaudación de la Tasa Patronal
  (1980) shall be registered as the operational-instrument dated row:
  issued by INTECAP's Junta Directiva under law art. 32's delegation
  (*un reglamento específico normará lo relativo a la recaudación…
  y a las multas y recargos*), given **23-Apr-1980**; derogates the
  Junta Acuerdo of 22-Apr-1977; vigencia 30 days after DCA
  publication (date not printed — gap-flagged); TRANSITORY 60-day
  amnesty (patrons paying ALL arrears within 60 days of vigencia pay
  no recargos) carried as a dead transitory boundary row for period
  computations spanning 1980, never a live waiver.
  (LB-013; LB-014; EVID-363, EVID-364)

### 3.5 Operational anchors — window, base, fee and the single receipt

- **GT-PAY-FR-200:** The INTECAP planilla window: *la Tasa Patronal
  deberá pagarse juntamente con las contribuciones del IGSS, al
  presentarse las planillas… dentro de los primeros veinte días del
  mes siguiente al que correspondan* — the due date = within the
  FIRST 20 DAYS of the month following the planilla month, aligned to
  the presentation of the IGSS planillas. This is the ONLY printed
  planilla-window value in the corpus: IGSS's own *fecha límite*
  lives in Acuerdo 1421 (external — file 07 GT-PAY-FR-177 owns that
  GOQ-10 half; this file owns the INTECAP half). The 20-day row rides
  the shared due-date registry; odoo computes each planilla's window
  from it, and while the IGSS-side row remains unacquired the system
  invents no default — the difference between the two rows (when the
  IGSS instrument arrives) surfaces as a compliance note, never a
  silent override.
  (LB-016; EVID-366; GOQ-10 → OQ-008; cross-ref GT-PAY-FR-177)
- **GT-PAY-FR-201:** Base and the never-from-workers guard: *la Tasa
  Patronal se calculará y liquidará sobre el monto de los salarios
  consignados en las planillas de seguridad social, utilizando para
  el efecto las mismas planillas* (art. 8º) — the INTECAP base = the
  salaries stated in the IGSS planillas, computed using the SAME
  planillas (the planilla assembly of file 07 GT-PAY-FR-170 consumed
  by id; IRTRA kin = FR-187's ordinary+extraordinary totality). And
  the guard: the tasa is *exclusivamente a cargo de las empresas o
  entidades patronales, por lo que en ningún caso podrá descontarse
  de los salarios de los trabajadores* (art. 5º) — no worker-side
  line ever (the FR-189 engine constraint, INTECAP leg).
  (LB-015; LB-016; EVID-365, EVID-366; cross-ref GT-PAY-FR-170)
- **GT-PAY-FR-202:** Collection fee: IGSS collects the tasa *al
  mismo tiempo que recaude sus propias contribuciones*, deposits the
  amounts *directamente en la cuenta bancaria del INTECAP*, and
  receives *el 2% del monto de las sumas recaudadas, que deducirá de
  las mismas* — a clean printed value (contrast IRTRA's ambiguous
  art. 16 fee, FR-191): the settlement split (INTECAP 98% / IGSS 2%
  of collected sums) is shared dated data honored identically by
  both sides. (LB-013; EVID-363)
- **GT-PAY-FR-203:** Single-receipt ride: both patronal charges settle
  inside the ONE IGSS payment event — the single *Recibo Electrónico
  de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa
  INTECAP* computed on the total salaries reported in the planilla
  (payment integration OWNED by file 07 GT-PAY-FR-174, consumed by
  id; THIS file owns the IRTRA/INTECAP VALUES feeding it), and
  IRTRA/INTECAP arrears inside a *reconocimiento de deuda* settle
  simultaneously with the first installment (file 07 GT-PAY-FR-181,
  consumed by id). No separate remittance channel exists in the
  corpus — none is modeled.
  (LB-004; LB-013; LB-016; EVID-354, EVID-363, EVID-366; cross-ref
  GT-PAY-FR-174, GT-PAY-FR-181)

### 3.6 Enforcement and interlocks

- **GT-PAY-FR-204:** The INTECAP enforcement ladder shall be stored as
  dated rows, each carrying its GOQ-89 OCR-restoration flag
  ("0.500.00" [sic → Q500.00]; "(0.25)" [sic → Q25.00];
  "10/0…150/0" [sic → 1%…15%]): (a) liquidation **de oficio** from
  the salaries in the last IGSS planilla presented, *sin previa
  notificación al patrono* (art. 13º), with a **+5%** recargo capped
  at **Q500** per liquidation (art. 18º); (b) **mora** recargo
  **1%→15%** by elapsed month from vencimiento (15-month scale),
  NON-cumulative, applied to the global omitted amount, global cap
  **15%** (art. 24º); (c) **multa Q25–Q250** via the CT faltas
  procedure (art. 25º); (d) moratory payment **convenios up to 24
  months at 11% annual interest** (arts. 21º-22º; the Gerente may
  exonerate recargos, art. 27º). Clocks and liquidation evaluate in
  the saas core; exposure and payment surfaces in odoo.
  (LB-017; EVID-367; GOQ-89 → OQ-006)
- **GT-PAY-FR-205:** Enforcement frame and substitution of patrono:
  noncompliance *constituye falta a las leyes de trabajo y previsión
  social* under **CT art. 272 inciso C**, with unpaid tasas collectible
  *por la vía económico-coactiva* (art. 32) — the CT-side procedural
  pointer mirrored, sanction VALUES owned by
  `gt/requirements/taxation/06_ct-procedures.md`, never re-derived
  here; on substitution of patrono, BOTH must notify INTECAP *dentro
  de los diez días hábiles siguientes*, and the substituted patrono
  remains *solidariamente responsable… hasta el término de seis
  meses* (reglamento art. 28º) — a substitution-notice watchdate plus
  a 6-month solidarity flag on the successor/successor-pair record.
  (LB-013; LB-017; EVID-363, EVID-367)
- **GT-PAY-FR-206:** Incentivo non-contributory interplay (consumed by
  id): the *bonificación incentivo* shall NOT enter the IRTRA or
  INTECAP base — per D-78-89 art. 2 it is *no [será] sujeta ni afecta
  al pago de las cuotas patronales ni laborales del IGSS, IRTRA e
  INTECAP, salvo que patronos y trabajadores acuerden pagar dichas
  cuotas*: the recorded joint-agreement flag of
  `04_statutory-bonuses.md` **GT-PAY-FR-091** alone admits incentivo
  lines into the charge bases; when the flag is unset, both engines
  compute exactly as if the incentivo were absent (R42; the flag
  itself is owned by file 04, never restated here).
  (LB-002; LB-016; EVID-352, EVID-366; cross-ref GT-PAY-FR-091)

## 4. Data Model

Layer semantics: payroll is Odoo-native for computation and books;
rate/ladder/window/fee dated rows are `shared` (both sides resolve the
same row); enforcement/clock evaluation is `saas` with odoo surfaces.
Dated rows follow D15/D16: valid_from/valid_to + instrument provenance;
snapshot-on-write. No bracket data exists for IRTRA at any layer (R32);
the activity-list and acta registries ship EMPTY until their GOQ
instruments are acquired.

**Charge parameter feeds (dated rows):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.irtra.rate | rate_pct · valid_from · provenance | decimal / date / char | 0.01 flat; 1962-07-01 (charge creation); base = sueldo/salario ordinario+extraordinario devengado per worker, totality of planillas; text vintage post-"Decreto 43.92" (GOQ-84 stamp) | FR-187 |
| l10n_gt.pay.irtra.guard | no_brackets | guard row | R32: bracket-shaped seeds rejected | FR-188 |
| l10n_gt.pay.irtra.igss.fee | art16_ambiguous | flag row | "0.25% DEL 1%" — NO numeric value; GOQ-85 | FR-191 |
| l10n_gt.pay.intecap.rate.ladder | sector · rate_pct · valid_from · acta_gap | select / decimal / date / boolean | industrial_comercial_servicios: 0.005 (1972-06-01) → 0.0075 (1973-01-01) → 0.01 ceiling (1974-01-01); agropecuario_permanentes: 0.005 (1973-01-01) → 0.0075 (1974-01-01) → 0.01 ceiling (1975-01-01); acta_gap = TRUE on every row > 0.50% (GOQ-89); in-force anchor = Reglamento-1980 art. 9º | FR-197 |
| l10n_gt.pay.intecap.igss.fee | retention_pct | decimal | 0.02 (art. 31; settlement split INTECAP 98% / IGSS 2%) | FR-202 |
| l10n_gt.pay.patronal.activity.list | activity · afecta · valid_from · provenance | dated rows | EMPTY until IRTRA JD acuerdos acquired (GOQ-91); no default seeded | FR-190 |

**Employer configuration and tests:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company (gt payroll) | gt_pay_patronal_sector | select | industrial · comercial · servicios · agropecuario | FR-195, FR-196, FR-197 |
| res.company | gt_pay_lucrative_process · gt_pay_igss_registered | boolean | payer-universe tests (Estatutos art. 7 + art. 12 registration clause) | FR-187, FR-190 |
| res.company (INTECAP exemptions) | gt_pay_intecap_exempt_reason | select | none · non_igss_subject · university · non_lucrative · agro_under_10_permanentes | FR-195, FR-196 |
| hr.contract (agro) | gt_pay_permanente (computed) | boolean | >1 year uninterrupted service in the agropecuaria | FR-196 |
| hr.employee (IRTRA) | gt_pay_irtra_affiliation_voluntary · carnet_free | metadata | no payroll-driven worker obligation | FR-192 |
| l10n_gt.pay.intecap.convenio | rebaja_pct (≤0.80) · reimbursement_freq · supervision_state | per-employer row | effective-rate mechanism (floor 0.2%); quarterly reembolso postings; INTECAP-side approval imported, never self-declared | FR-198 |

**Window, base and settlement:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.planilla.window (shared registry) | window_days · anchor · scope | int / select / select | 20; month following the planilla month; scope=intecap (this file's GOQ-10 half; the scope=igss row is file 07 GT-PAY-FR-177's) | FR-200 |
| hr.payslip.line (patronal charges) | gt_pay_charge | select | irtra_impuesto · intecap_tasa — employer-cost lines only; worker-side forbidden | FR-187, FR-189, FR-201 |
| hr.payroll (aggregator) | gt_pay_intecap_base | monetary (computed) | salaries stated in the IGSS planillas (file 07 GT-PAY-FR-170 feed; incentivo gated per FR-206) | FR-201 |
| l10n_gt.pay.igss.payment (file 07) | receipt legs irtra/intecap | monetary | single Recibo Electrónico event owned by GT-PAY-FR-174; values from this file | FR-203 |

**Enforcement (saas core, odoo surfaces):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.intecap.enforcement | de_oficio_surcharge_pct · cap_amount · ocr_flag | decimal / monetary / boolean | 0.05; Q500 per liquidation ("0.500.00" restored, GOQ-89) | FR-204 |
| l10n_gt.pay.intecap.mora.scale | month_offset · recargo_pct · ocr_flag | dated rows | 1%…15% ("10/0…150/0" restored), non-cumulative, global cap 15% | FR-204 |
| l10n_gt.pay.intecap.multa | floor · ceiling | monetary | Q25.00–Q250.00 (CT faltas procedure) | FR-204 |
| l10n_gt.pay.intecap.convenio.pago | max_months · annual_interest | int / decimal | 24; 11% | FR-204 |
| l10n_gt.pay.patrono.substitution | notice_days_habiles · solidarity_months | int / int | 10; 6 (successor + substituted jointly exposed) | FR-205 |
| l10n_gt.pay.guard (citation) | rows | char | D-1528 article numbers only vs 42_ print; pre-"Decreto 43.92" text unrecoverable; 43_/44_ no-rate; R31 identity | FR-186 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. Payroll-wave bindings
for this file (binding): rate/ladder/window/fee dated rows = `shared`;
planilla-window computation + rebate accounting = `odoo`;
enforcement/clock evaluation = `saas` with `odoo` surfaces. Model names
stable across Odoo 17/18/19/20; no version-specific behavior required
by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-185 | shared | — (instrument registry §4) | D-1528 + AG lineage dated rows | R31 identity stamp; AG 5/6-2005 dates GOQ-86 (no date asserted) |
| FR-186 | shared | — (guard rows §4) | citation guards | GOQ-84/87; 42_ glyph-decode provenance; both catalogs carry the guards |
| FR-187 | shared | — (l10n_gt.pay.irtra.rate) | 1% flat row + base definition | Post-"Decreto 43.92" vintage stamp; components fed by GT-PAY-FR-005 tags |
| FR-188 | shared | — (guard row §4) | no_brackets | R32 negative; bracket seeds rejected; no exceptions until out-of-corpus instrument |
| FR-189 | odoo | salary-rule constraint + payslip check | patronal-only invariant | No worker-side IRTRA line; blocks posting |
| FR-190 | odoo | res.company + activity-list registry | lucrative/IGSS-registered tests | Registry EMPTY until JD acuerdos (GOQ-91); worker/family eligibility metadata |
| FR-191 | shared | — (mechanics + fee-flag rows §4) | IGSS joint collection; art. 16 ambiguous | Monthly transfer following month; fee = flag only, NO value (GOQ-85) |
| FR-192 | odoo | hr.employee | voluntary affiliation + free carnet | HR metadata; no payslip computation |
| FR-193 | odoo | hr.payslip.line / account.move.line | employer-deduction tag | Feeds GT-TAX-FR-167 by id; kin GT-TAX-FR-146 via file 07 FR-170 |
| FR-194 | shared | — (instrument registry §4) | D-17-72 dated rows | GOQ-88: vigencia = unprinted DCA date; row carries gap, asserts no date |
| FR-195 | odoo | res.company | exemption flags | non_igss_subject · university · non_lucrative (printed three only) |
| FR-196 | odoo | hr.contract + res.company | permanente test + ≥10 headcount gate | >1 year uninterrupted; <10 exonerated (both-sides threshold) |
| FR-197 | shared | — (l10n_gt.pay.intecap.rate.ladder) | ladder dated rows | acta_gap on >0.50% rows (GOQ-89); in-force 1% anchored to Reglamento-1980 art. 9º |
| FR-198 | odoo | l10n_gt.pay.intecap.convenio | rebate accounting | ≤80% rebate; quarterly reembolso postings; effective floor 0.2% |
| FR-199 | shared | — (instrument registry §4) | Reglamento-1980 rows | 23-Apr-1980; DCA+30 gap; 60-day amnesty = dead transitory boundary |
| FR-200 | odoo | planilla window computation (row shared §4) | 20-day window resolver | Row rides shared registry (scope=intecap); IGSS half external GOQ-10 (file 07 FR-177); no invented default |
| FR-201 | odoo | hr.payroll / payslip-line rules | intecap base + worker-side block | Base = IGSS planilla salaries (file 07 FR-170 feed); art. 5º guard |
| FR-202 | shared | — (fee row §4) | 2% IGSS retention | Clean printed value; settlement split 98/2 |
| FR-203 | saas + odoo | l10n_gt.pay.igss.payment (file 07) | single-receipt legs | Event owned by GT-PAY-FR-174; this file supplies IRTRA/INTECAP values; RD first-installment ride per GT-PAY-FR-181 |
| FR-204 | saas | l10n_gt.pay.intecap.enforcement / mora.scale | de-oficio +5% (Q500) · mora 1-15% · multa Q25-Q250 · convenio 24m @ 11% | GOQ-89 OCR flags on every row; odoo surfaces exposure/alerts |
| FR-205 | saas | substitution watchdate + solidarity flag | 10 dh notice · 6-month solidarity | CT 272 inc. C + económico-coactivo pointer; sanction values external (taxation/06) |
| FR-206 | odoo | payslip base builder | incentivo gate | GT-PAY-FR-091 joint-agreement flag consumed by id; unset → incentivo absent from both bases |

Version-regime notes (D15/D16): the dated rows owned here are
instrument/parameter data — the D-1528/D-17-72/Reglamento-1980
provenance sets (FR-185/194/199, each with its GOQ gap stamp), the 1%
IRTRA rate row (FR-187), the INTECAP ladder (FR-197, acta-gap flagged)
and the in-force anchor via art. 9º, the 20-day window row (FR-200) and
the 2% fee (FR-202) — each with valid_from/provenance; the activity
list (GOQ-91), the escalonado acta (GOQ-89) and the art. 16 fee value
(GOQ-85) remain unencoded until their instruments are acquired.

## 6. Acceptance Criteria

- **AC-001:** Given an IGSS-registered private employer in the
  lucrative production-of-goods/services process and a month with one
  worker earning Q5,000 ordinary + Q500 extraordinary salary, when the
  payslip computes, then a single employer-cost line irtra_impuesto =
  1% × Q5,500 = Q55.00 posts, and NO worker-side line exists.
  (FR-187, FR-189)
- **AC-002:** Given an attempt to seed IRTRA bracket rows (e.g. 0.5% /
  1% / 2% by worker count or capital tiers), when the rate registry is
  inspected, then no bracket-shaped row exists and the seed is
  rejected (R32 — any bracket claim needs an out-of-corpus
  instrument). (FR-188)
- **AC-003:** Given period May-1973 (industrial sector), when the
  ladder resolves, then rate = 0.75%; given Jan-1974 (industrial) →
  1.00% ceiling row with acta_gap = TRUE; given Jan-1975
  (agropecuario permanentes) → 1.00% ceiling row with acta_gap = TRUE;
  given any current-period date, then the in-force rate resolves to 1%
  anchored to Reglamento-1980 art. 9º — never to an acta.
  (FR-197)
- **AC-004:** Given an agropecuaria with 9 permanentes (each >1 year
  uninterrupted), when the exemption evaluates, then no INTECAP line
  posts (<10 exonerated); given 10 permanentes plus 2 workers with 11
  months' service, then the tasa computes over the 10 permanentes'
  planilla salaries only, the 11-month workers excluded from both the
  count and the base. (FR-196)
- **AC-005:** Given an employer holding an INTECAP convenio with
  rebaja 80% and a monthly planilla base of Q10,000, when the charge
  computes, then the accrued tasa = Q100.00 with an effective charge
  of Q20.00 and a Q80.00 quarterly-reimbursement posting; given no
  convenio, then Q100.00 stands in full. (FR-198)
- **AC-006:** Given a March planilla period, when the window computes,
  then the INTECAP due date falls within the first 20 days of April
  aligned to IGSS planilla presentation; given the IGSS-side fecha
  límite row is still unacquired (GOQ-10), then no default due date is
  invented for the IGSS leg and the 20-day INTECAP row stands alone as
  the only printed window. (FR-200)
- **AC-007:** Given a collected INTECAP sum of Q100.00, when the
  settlement splits, then Q98.00 deposits to INTECAP and Q2.00 (2%)
  retains at IGSS; given the IRTRA leg of the same cycle, when the
  art. 16 fee row is inspected, then it carries the ambiguity flag
  with NO numeric value posted. (FR-191, FR-202)
- **AC-008:** Given a period's payment event, when the receipt
  generates per file 07's integration, then ONE Recibo Electrónico de
  Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa INTECAP
  settles the IGSS cuotas + the IRTRA Q55.00 (AC-001) + the INTECAP
  charge (AC-005 base) — no separate channel exists.
  (FR-203)
- **AC-009:** Given a Q1,000 omitted tasa paid three months after
  vencimiento, when the enforcement evaluates, then the mora recargo =
  3% (third-month row, non-cumulative, on the global amount, cap 15%);
  had INTECAP liquidated de oficio, then +5% capped at Q500 applies;
  given a subscribed convenio, then ≤24 months at 11% annual with the
  Gerente's recargo-exoneration option recorded.
  (FR-204)
- **AC-010:** Given a worker earning Q3,000 salary + Q250 incentivo
  without a joint agreement, when the bases compute, then both charges
  compute on Q3,000 (the incentivo is absent); given the recorded
  GT-PAY-FR-091 joint-agreement flag set, then the incentivo enters
  both bases. (FR-206)
- **AC-011:** Given a legally established university employer and a
  non-IGSS-subject employer, when the universes evaluate, then no
  INTECAP lines post for either (university exception; non-IGSS-subject
  carve-out), and the non-IGSS-subject employer is likewise outside the
  IRTRA payer set (registration test). (FR-190, FR-195)
- **AC-012:** Given any requirement or row citing the IRTRA law, when
  inspected, then it cites "Decreto Número 1528" (1962) with article
  numbers only against the 42_ print — never "Decreto 15 de 1928",
  never pre-"Decreto 43.92" art. 12 content, never a rate sourced to
  AG 5-2005/6-2005. (FR-186)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
owned set for this file: GOQ-84, GOQ-85, GOQ-86, GOQ-87, GOQ-88,
GOQ-89, GOQ-91 and the INTECAP half of GOQ-10 (the IGSS fecha-límite/
mora-tasa halves of GOQ-10 are owned by
`07_igss-contributions.md` GT-PAY-FR-177/FR-179). All rows Status
open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-84 (owned): IRTRA — "Decreto 43.92" identity beyond the glyph reading; the PRE-reform text of D1528 arts. 2/12/13 is unrecoverable (consolidated print only). Affects FR-186 (guard) and FR-187 (rate row vintage stamp). If a bracket structure ever existed it could only be in that unrecoverable text — R32 stands until the instrument is acquired. | no | GT synthesis wave S-GT3 → acquisition queue (D-43-92 consolidated text) | open |
| OQ-002 | GOQ-85 (owned): D1528 art. 16 IGSS fee "0.25% DEL 1% DEL PRODUCTO DEL IMPUESTO" — arithmetically ambiguous (0.25% of the 1% tax vs 0.25 pp of payroll). FR-191 ships a flag-only row; NO value is ever encoded or derived by guess. | no | GT synthesis wave S-GT3 → acquisition queue (clarifying instrument) | open |
| OQ-003 | GOQ-86 (owned): AG 5-2005/6-2005 print no AG signature date and no DCA date (INFILE stamp 12-ene-2005 only) — effective dates not derivable; FR-185 lineage rows carry no vigencia for the 2005 instruments. | no | GT synthesis wave S-GT3 → sources watch | open |
| OQ-004 | GOQ-87 (owned): D-1528 renumbering — 43_/44_ cite D1528 arts. 24 and "8º. y 26º." with meanings mismatching the 42_ print; intervening renumbering reforms absent from corpus. FR-186 guard: article numbers cited only vs the 42_ print; re-key on acquiring a current consolidated D1528. | no | GT synthesis wave S-GT3 → acquisition queue (current consolidated D-1528) | open |
| OQ-005 | GOQ-88 (owned): D-17-72 effective date — art. 38 makes DCA publication the vigencia and no DCA date is printed. FR-194 dated row carries the gap; no date asserted (ladder rows dated from their own printed article-28 dates, independent of the gap). | no | GT synthesis wave S-GT3 → acquisition queue (DCA 1972 publication) | open |
| OQ-006 | GOQ-89 (owned): INTECAP — 46_ OCR restorations to verify against a clean copy (Q500 de-oficio cap; Q25 multa floor; 1%…15% mora scale; lost ordinals), and the escalonado-confirmation acta (art. 28 inc. 3, 1974/1975) is NOT in corpus: the in-force 1% is evidenced only via Reglamento-1980 art. 9º. FR-197/FR-204 rows carry ocr_flag/acta_gap. | no | GT synthesis wave S-GT3 → evidence re-read + acquisition (Junta actas 1974/1975) | open |
| OQ-007 | GOQ-91 (owned): IRTRA Junta Directiva acuerdos listing the "actividades económicas afectas" (D1528 art. 12) and the IGSS-side operational resolutions implementing the joint collection of both charges are not in corpus. FR-190's activity registry ships EMPTY; no default afectación seeded. | no | GT synthesis wave S-GT3 → acquisition queue (IRTRA JD acuerdos; IGSS resolutions) | open |
| OQ-008 | GOQ-10 (INTECAP half, shared with file 07): the instrument confirming the INTECAP escalonado rise to the 1.00% ceiling (Junta acta) is absent — the in-force 1% anchors to Reglamento-1980 art. 9º only (FR-197); and IGSS's own planilla fecha límite (Acuerdo 1421 arts. 31 c)/38) remains external — FR-200's 20-day row is the only printed planilla-window value; the IGSS half is owned by file 07 GT-PAY-FR-177. | no | GT synthesis wave S-GT3 → acquisition queue (INTECAP Junta actas; Acuerdo 1421) | open |
