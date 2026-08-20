# GT — Payroll — Minimum wage: salario mínimo chassis, dated AG rate tables 1995–2026

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Guatemala *salario mínimo* (minimum wage) layer: the
Código de Trabajo (Labor Code, CT, Decreto 1441) fixing mechanism of Arts.
103-115 — every worker's entitlement to a minimum covering normal material,
moral and cultural needs, the annual *Acuerdo Gubernativo* (AG, governmental
accord) fixing per actividad/empresa/*circunscripción económica* (economic
circumscription) issued through MinTrabajo, and the automatic modification of
inferior contractual wages — plus THE DATED RATE TABLES as the
`salario_minimo.csv` sidecar: the 2026 AG 256-2025 six-cell table (first
CE-split instrument: CE1 = departamento de Guatemala, CE2 = all other
departments, × Agrícola (CIIU Rev. 4 section A) / No Agrícola (sections B–U,
private sector) / Exportadora y de Maquila), transcribed digit-for-digit
[sic]-faithful with words-govern resolution of the print's digit-level
defects; the 2021 AG 250-2020 COVID freeze (hourly + daily printed, single
national zone); and the official 1995–2021 history of the Departamento
Nacional del Salario (2 sectors 1995–2007 → 3 sectors 2008–2021, 26 AGs from
610-94, late-January transitions, the 1997 *prórroga*, the 2001 AG 838-2000
carryover and the 2004 Constitutional-Court suspension gap); the application
rules of AG 256-2025 Art. 8 — hourly proration to the *jornada* (workday),
the workplace → habitual-execution-place → worker-residence location
cascade, the *destajo* (piecework) floor, the indivisible incentivo add-on,
and the CT Art. 272 a) sanction + back-pay with its sanction-base rate
selector — and the consumer interfaces every other file reads (OT base floor,
inembargabilidad carve-out, IGSS estimated-salary floor). The 2022–2025 AGs
are ABSENT from the corpus and are recorded as explicit gap rows, never
interpolated (GOQ-11).

It does **not** cover: the *salario* / *salario completo* model and pay-basis
taxonomy (`01_ct-salary-model.md` — GT-PAY-FR-002, GT-PAY-FR-005,
GT-PAY-FR-010 consumed by id, never restated); jornada classification and
the overtime engine, whose +50% base consumes this file's dated floors
(`02_working-time-overtime.md` — GT-PAY-FR-033 consumed by id); statutory
bonuses — bono 14, the incentivo AMOUNT (Q250, D37-2001) and the
corpus-absent December aguinaldo (`04_statutory-bonuses.md` — this file owns
only the add-on mechanics hook); vacaciones, maternidad and menores
(`05_vacaciones-maternidad.md`); contracts, despido and indemnización
(`06_contracts-termination.md`); IGSS contributions, whose estimated-salary
floor = the salario mínimo AG vigente (`07_igss-contributions.md`);
IRTRA/INTECAP patronal charges (`08_irtra-intecap.md`); ISR/IVA payroll
interfaces — this file feeds dated rows to contracts only and computes no
tax (`09_isr-iva-interfaces.md`); or sanction values (owned by
`gt/requirements/taxation/06_ct-procedures.md` — this file records the CT
272 a) hook + back-pay only).

## 2. Legal Basis

Authority order (binding, per master evidence index P2): **salario-mínimo
rate rows = 37_ / 38_ / 39_ as DATED data with [sic] fidelity — printed
figures govern over formulas (R35)**. 37_ = AG 256-2025 (given 19-Dec-2025,
DCA 22-Dec-2025 No. 74 Tomo CCCXXVIII, effective 1-Jan-2026) is the
operative 2026 instrument; 38_ = AG 250-2020 (COVID freeze, effective
1-Jan-2021); 39_ = the official Departamento Nacional del Salario
compilation 1995–2021 — a SECONDARY authority-compiled table, so normative
rows cite the UNDERLYING AG it prints, never the compilation itself; the
monthly-conversion formula SD × 365/12 is estimation-only against its own
printed figures (GOQ-82). The fixing MECHANISM cites 32_ as "CT art. N
(texto según edición conmemorativa 2024, MinTrabajo)" — no "current through"
date claimable (GOQ-70/71; the qualifier on every CT row below IS the R44
mitigation). Digit-level defects of the 2026 print: art. 6 CE2 No Agrícolas
monthly digits "3,416.90" [sic] vs own words 3,816.90 — words govern
(R35/GOQ-78); art. 7 = 3,221.10 as printed, never "corrected" to the
project prior 3,321.10 (GOQ-77); arts. 2/4 monthly digits garbled → words
govern (GOQ-78). File-level hazard: 38_ p.3 is a different, unrelated
instrument (MinFin AG 243-2020) — R43.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT art. 103 (texto según edición conmemorativa 2024, MinTrabajo): "Todo trabajador tiene derecho a devengar un salario mínimo que cubra sus necesidades normales de orden material, moral y cultural…" | Art. 103: every worker has the right to earn a minimum wage that covers his normal needs of a material, moral and cultural order (the entitlement floor; values live in the AGs, not the CT) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 103 p.58 (EVID-285) |
| LB-002 | CT art. 104 (texto según edición conmemorativa 2024, MinTrabajo): "El sistema… se debe aplicar a todos los trabajadores, con excepción de los que sirvan al Estado o a sus instituciones y cuya remuneración esté determinada en un presupuesto público." | Art. 104: the minimum-wage system applies to ALL workers, except those serving the State or its institutions whose remuneration is determined in a public budget | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 104 pp.58-59 (EVID-285) |
| LB-003 | CT art. 113 (texto según edición conmemorativa 2024, MinTrabajo): "El Organismo Ejecutivo, con vista de los mencionados informes y dictámenes debe fijar anualmente mediante acuerdos emanados por conducto del Ministerio de Trabajo y Previsión Social, los salarios mínimos que han de regir en cada actividad, empresa o circunscripción económica." | Art. 113: the Executive Branch, on the mentioned reports and opinions, must fix ANNUALLY, via acuerdos issued through MinTrabajo, the minimum wages to govern in each activity, enterprise or economic circumscription | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 113 p.63 (EVID-285) |
| LB-004 | CT art. 115 (texto según edición conmemorativa 2024, MinTrabajo): "La fijación del salario mínimo modifica automáticamente los contratos de trabajo en que se haya estipulado uno inferior…" | Art. 115: the fixing of the minimum wage AUTOMATICALLY modifies employment contracts in which a lower wage was stipulated (no lower-than-minimum contract survives a fixing) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 115 p.63 (EVID-285) |
| LB-005 | AG 256-2025, identity + Art. 11: "ACUERDO GUBERNATIVO NÚMERO 256-2025" / "Guatemala, 19 de diciembre de 2025" / DCA print: "LUNES 22 de DICIEMBRE de 2025 No. 74 Tomo CCCXXVIII" / "ARTÍCULO 11. Vigencia. El presente acuerdo gubernativo empieza a regir el uno de enero de dos mil veintiséis y deberá publicarse en el Diario de Centro América, la cual se realizará sin costo alguno por ser de observancia general y de estricto interés del Estado." | AG 256-2025: the 2026 minimum-wage accord, given 19-Dec-2025, published DCA 22-Dec-2025 (No. 74, Tomo CCCXXVIII); rates take effect on the FIXED calendar date 2026-01-01 (not publication-relative) | `gt/sources/37_Salario_Minimo_AG_256-2025.pdf` | p.1 gazette header + instrument title/date; p.2 Art. 11 (EVID-331) |
| LB-006 | AG 256-2025, considerando III + Art. 1: "el Acuerdo Gubernativo número 285-2021, de fecha 21 de diciembre de 2021, determinó las Circunscripciones Económicas y creó las Comisiones Paritarias de Salarios Mínimos por Circunscripción y Actividad Económica; siendo éstas las comisiones paritarias para la Actividad Agricola, No Agrícola, Exportadora y de Maquila de la Circunscripción Económica Uno *CEl" delimitada al departamento de Guatemala y las comisiones paritarias para la Actividad Agrícola, No Agrícola, Exportadora y de Maquila de la Circunscripción Económica Dos "CE2", que comprende el esto [sic] de los departamentos que conforman la República de Guatemala." / "ARTÍCULO 1. Definiciones. Para los efectos del presente acuerdo se derá por: ac agricolas, las comprendidas en la sección A de la tercera parte de la Clasificación Industrial Internacional Uniforme de todas las actividades económicas [(CHU) [sic] Revisión cuatro de la Org; són de las Nact [sic] Unidas, y, actividades no agrícolas, las comprendidas en las secciones de la Ba la U [sic — "de la B a la U"] de la tercera parte de la citada clasificación, en lo concerniente al sector privado." (POR TANTO also cites "Acuerdo Gubernativo númoro 235-2021 de fecha 21 de diciembre de 2021" [sic] alongside considerando III's AG 285-2021 — divergence GOQ-79) | AG 256-2025 structure: AG 285-2021 created the Economic Circumscriptions and the paritarian commissions — CE1 delimited to the department of Guatemala, CE2 comprising the other departments of the Republic; Art. 1 definitions: actividades agrícolas = CIIU Rev. 4 (UN International Standard Industrial Classification) section A; actividades no agrícolas = sections B–U, private sector; Exportadora y de Maquila = one combined rate activity (4 paritarias per CE, only 3 rates fixed) | `gt/sources/37_Salario_Minimo_AG_256-2025.pdf` | p.1 considerando III; p.2 POR TANTO + Art. 1 (EVID-332) |
| LB-007 | AG 256-2025, Arts. 2–7 (six-cell table; words → digits as printed; defects [sic]): Art. 2 CE1 Agrícolas: "CIENTO WEINTICUATRO [sic] QUETZALES CON SESENTA Y CUATRO CENTAWOS [sic] (OQ. 124,64)" → 124.64 diarios; "TRES MIL SETECIENTOS NOWENTA [sic] Y UN QUETZALES CON VEINTE CENTAVOS (a, 3, fte 20) [sic — digits garbled; words read 3,791.20]" / Art. 3 CE1 No Agrícolas: "CIENTO TREINTA Y UN QUETZALES CON CINCUENTA Y OCHO CENTAVOS (0. 131.58)"; "CUATRO MIL DOS QUETZALES CON VEINTIOCHO CENTAVOS (O. 4,002.28)" / Art. 4 CE1 Exportadora y de Maquila: "CIENTO DOCE QUETZALES CON DIEZ CENTAVOS (Q. 112. 10)"; "TRES MIL CUATROCIENTOS NUEVE QUETZALES CON SETENTA Y TRES CENTAVOS la 3, Q. 73) [sic — digits garbled; words read 3,409.73]" / Art. 5 CE2 Agrícolas: "CIENTO DIECINUEVE QUETZALES CON VEINTIUN CENTAWOS [sic] (0. 119.21)"; "TRES MIL SEISCIENTOS VEINTICINCO QUETZALES CON OCHENTA Y NUEVE CENTAVOS (0. 3,625.89)" / Art. 6 CE2 No Agrícolas: "CIENTO VEINTICINCO QUETZALES CON CUARENTA Y NUEVE CENTAVOS (Q, 125,49)"; "TRES MIL OCHOCIENTOS DIECISEIS QUETZALES CON NOVENTA CENTAVOS (Q. 3,416.90] [sic — digit "4" defect; words read OCHOCIENTOS = 3,816.90]" / Art. 7 CE2 Exportadora y de Maquila: "CIENTO CINCO QUETZALES CON NOVENTA CENTAVOS (Q, 105.90)"; "TRES MIL DOSCIENTOS WEINTIUN [sic] QUETZALES CON DIEZ CENTAVOS (0. 3,221.10)" (diverges from project-known prior 3,321.10 — as printed, GOQ-77). Every article repeats: "que calculados por hora, se pagará la parte proporcional que corresponda dependiendo de la jornada de trabajo en la que se labore." | Arts. 2-7: the six 2026 (zone × activity) tuples, each with daily AND monthly printed — CE1 Agrícola 124.64 / 3,791.20 (words govern, GOQ-78); CE1 No Agrícola 131.58 / 4,002.28; CE1 Exportadora y Maquila 112.10 / 3,409.73 (words govern, GOQ-78); CE2 Agrícola 119.21 / 3,625.89; CE2 No Agrícola 125.49 / 3,816.90 (printed digits "3,416.90" [sic] yield to their own words — R35/GOQ-78); CE2 Exportadora y Maquila 105.90 / 3,221.10 (as printed, GOQ-77); hourly is PROPORTIONAL to the jornada, never an independent printed constant; monthly ≈ daily × 365/12 only to centavos (124.64 → 3,791.13 computed vs 3,791.20 printed) — the AG's own printed monthlies govern | `gt/sources/37_Salario_Minimo_AG_256-2025.pdf` | p.2 Arts. 2-7 (EVID-333) |
| LB-008 | AG 256-2025, Art. 8 c)-f) + Art. 9: (c) "Elmonto [sic] fijado a aplicarse para e! [sic] pago por salario mínimo se rige y determina por el lugar en el que se encuentre wbicado [sic] «l venteo de trebejo [sic — centro de trabajo], de conformidad con lo que esteblece [sic] el presente acuerdo y el respectivo contrato de trabajo. $1 [sic] no fuera posible determinar un centra de trabajo por la naturaleza del servicio o la ejecución de la obra, se tomará el lugar donde habitualmente realiza la ejecución n [sic] prestación del mismo" … "Si no es posible determinar con claridad las situaciones reguladas en los supuest [sic] anteriores, se determinará por el lugar donde resida habitualmente el trabajador." / (d) "Cuando por las peculiaridades y naturaleza de cada trabajo, se pacte el pago de la remuneración por unidad de obra o por participación en las utilidades, ventas o cobros que haga el patrono, en ningún caso saldrán perjudicados los trabajadores que ganen por pieza o precio alzado o a destajo, de conformidad con la ley. Los trabajadores en ningún caso tendrán un salario mínimo menor al fijado en el presente Acuerdo Gubernativo." / (e) "Adicionalmente al salario mínimo fijado, según corresponda, se deberá pagar al trabajador la bonificación incentivo, establecida en el Decreto número 78-89 del Congreso de la República. Queda prohibida la división de esta prestación." / (f) "El incumplimiento en el pago del salario mínimo fijado en el presente Acuerdo Gubernativo dará lugar a la sanción que corresponde de conformidad con el artículo 272 literal a) del Código de Trabajo, lo que no exime al empleador de la obligación de pagar el salario mínimo adeudado al trabajador afectado por el incumplimiento." / Art. 9: "Las sanciones administrativas de carácter pecuniario cuya unidad de medida se encuentre fijada por ley con base en salarios mini ¡ [sic] actividades no agricolas, se impondránparaa [sic] … de conformidad a la circunscripción que corresponda según lo regulado en la literal c) del artíc…" [quote truncated in the evidence as marked] (gloss: pecuniary sanctions denominated in minimum wages use the no-agrícola rate of the corresponding CE for labor matters, the CE1 no-agrícola rate for all other matters; art. 8 h) = no renuncia of acquired rights) | Art. 8 application measures: (c) rate selection by workplace location → habitual place of execution/service → worker's habitual residence; (d) piece-rate/participation workers (pieza, precio alzado, destajo) never disadvantaged and never below the fixed minimum; (e) the D78-89 incentivo must be paid ON TOP of the minimum and its DIVISION is prohibited; (f) non-payment sanction = CT art. 272 a) plus back-payment of the shortfall; Art. 9: sanctions denominated in minimum wages select the no-agrícola rate of the corresponding circumscription (labor matters) or the CE1 no-agrícola rate (other matters) | `gt/sources/37_Salario_Minimo_AG_256-2025.pdf` | p.2 Art. 8 c)-f) + Art. 9 (EVID-334) |

| LB-009 | AG 250-2020, identity + considerando II + vigencia: "ACUERDO GUBERNATIVO NÚMERO 250-2020" / "Guatemala, 29 de diciembre de 2020" / DCA print: "MIÉRCOLES 30 de diciembre 2020 [sic] DIARIO de CENTRO AMÉRICA NÚMERO 30" / "Que-los [sic] efectos económicos y sociales de la pandemia Covid-19 tienen una particular repercusión en sociedades como la guatemalteca, por ende es recomendable tomar decisiones y acciones que permitan que la política económica se oriente en forma efectiva a la recuperación de las capacidades productivas y la protección del empleo, para lo cual se deberá manténer [sic] los salarios mínimos vigentes" / "Artículo 10, Vigencia. El presente Acuerdo Gubernstivo. [sic] empieza a regir el uno de enero del año dos mil veintianio [sic] y deberá ser publicado en el Oíario [sic] de Centro América." (title as printed: "SALARIOS MINIMOS PARA ACTIVIDADES AGRICOLAS, NO AGRICOLAS Y DELA [sic] ACTIVIDAD EXPORTADORA Y DE MAQUILA.") | AG 250-2020: the 2021 accord, given 29-Dec-2020, published DCA 30-Dec-2020 (No. 30), effective 1-Jan-2021; operative content = a FREEZE (COVID-19 recovery rationale: mantener los salarios mínimos vigentes) — 2021 continues the 2020 rates, single national zone, no CE split | `gt/sources/38_Salario_Minimo_AG_250-2020.pdf` | p.1 title/date; p.1-2 considerando II; p.2 Art. 10 (EVID-335) |
| LB-010 | AG 250-2020, Arts. 2-4: Art. 2: "Para las actividades Agrícolas se fija el satario [sic] mínimo er [sic] ONCE QUETZALES CON VEINTISIETE CENTAVOS (01.11.27) [sic] POR HORA equivalente a NOVENTA QUETZALES CON DIECISÉIS CENTAVOS (Q.90.16) DIARIOS en jornada ordinarla [sic] diurna ds [sic] trabajo o lo proporcionál [sic] para las jomadas [sic] mixta o nocturna" / Art. 3: "ONCE QUETZALES CON SESENTA Y UN CENTAVOS (Q,11.61] POR HORA equivalente a NOVENTA Y DOS QUETZALES CON OCHENTA Y OCHO CENTAVOS (0.92,88] DIARIOS" / Art. 4: "DIEZ. [sic] QUETZALES CON SESENTA Y UN CENTAVOS (Q.10.61) POR HORA equivalente a OCHENTA Y CUATRO QUETZALES CON OCHENTA Y OCHO CENTAVOS (0.84.88) DIARIOS" / each article closes: "En ambos casos el salario antes establecido será aplicable a partir del uno de enero del año dos mil veintiuno." | 2021 rates (identical to 2020 by the freeze): Agrícola Q11.27/hour = Q90.16/day; No Agrícola Q11.61/h = Q92.88/day; Exportadora y Maquila Q10.61/h = Q84.88/day — this AG prints HOURLY + DAILY (proportional for mixed/nocturnal jornadas); monthly equivalents only via the 39_ table (2,742.37 / 2,825.10 / 2,581.77, LB-014); one national rate per activity, no zone split | `gt/sources/38_Salario_Minimo_AG_250-2020.pdf` | p.2 Arts. 2-4 (EVID-336) |
| LB-011 | AG 250-2020, measures articles (numbering defective in print — sequence runs 5, "8" [sic, likely 6], 7, 8, 9, 10; GOQ-80/OQ-6): "El Ministerio de Trabajo y Previsión Social deberá establecer las comisiones paritarias de salarios mínimos a nivel departamental o por circunscripción económica, de acuerdo con el artículo 105 del Código de Trabajo, según corresponda a la política salarial" / "Attículo [sic] 7. Sanelones [sic]. ta [sic] violación al pago del satario [sic] mínimo filado [sic] en el presente Acuerdo Subernativa [sic] dará lugar a la sanción que corresponde de conformidad con el artículo 272 literal aj [sic] del Código de Trabajo, lo cual no exime al empleador de su obligación de pagar el salario mínimo adeudado al trabajador afectado por el incumplimiento." / "Artículo 8. Bonificación Incentivo. Adicionalmente al salario mínimo fijado se deberá cancelar mensualmente al trabajador la Bonificación Incentivo, establecida en el Decreto Número 78-89 del Congreso de la República de Guatemala y sus Reformas." / "Artículo 9, Jerenunciabilidad [sic — Irrenunciabilidad]. El presente Acuerdo Gubemativo [sic] no implica renuncia de ningún derecho adquirido previamente por los trabajadores." | AG 250-2020 measures: paritarian commissions at departmental or circumscription level per CT art. 105; sanction = CT art. 272 a) + back-pay (same hook as AG 256-2025); the incentivo is payable MONTHLY on top of the minimum, statute cited "y sus Reformas" (as amended — today D37-2001's Q250, owned by file 04); irrenunciabilidad — no renunciation of previously acquired rights | `gt/sources/38_Salario_Minimo_AG_250-2020.pdf` | p.2 arts. as numbered 5, "8", 7, 8, 9, 10 (EVID-337) |
| LB-012 | 39_, identity: "SALARIOS MÍNIMOS FIJADOS POR EL GOBIERNO DE GUATEMALA PARA LOS AÑOS COMPRENDIDOS DE 1,995 A 2,021." / per-year block headers "AÑO 1,995:" … "AÑO 2,021:" with columns "Acuerdo Gubernativo" / "Fechas de Emis/Publ." / "ACTIVIDAD ECONOMICA SALARIO DIARIO SALARIO MENSUAL" + a "Vigente del … al …" vigencia string / "Recopilación: Mario R. de Mata Guerra. Departamento Nacional del Salario, Dirección General de Trabajo." / "Guatemala, enero de 2,021." Coverage quirks: 1997 — "NOTA: SE PRORROGAN LOS SALARIOS MINIMOS DEL AÑO ANTERIOR." (no own AG); 2001 likewise no own AG (AG 838-2000 block carries it); 2004 CC-suspension gap; compilation STOPS at 2021 — 2022-2025 AGs absent from the corpus (GOQ-11) | The official minimum-wage history compilation 1995-2021 of the Departamento Nacional del Salario: THE dated-row source for every year 1995-2021, per year = activity rows × (daily, monthly) + AG number + emisión/publicación dates + vigencia range; NOT itself a legal instrument — a secondary authority compilation whose normative rows cite the UNDERLYING AGs; 2 sectors 1995-2007, 3 sectors 2008-2021 | `gt/sources/39_Salario_Minimo_Historia.pdf` | p.1 title block + all pages; p.4 footer (EVID-339) |
| LB-013 | 39_, p.4 note below the 2021 block: "Para estimar el salario mensual se aplica la fórmula: valor del salario diario por el total de días del año dividido doce (SD X 365 / 12)" | Official monthly = daily × 365 / 12 (× 30.416̄) — explains e.g. 90.16 → 2,742.37; some printed monthlies diverge from the formula by centavos (2008 maquila 1,456.38 vs 1,452.40 computed) — PRINTED VALUES ALWAYS GOVERN; the formula is for estimation/display only | `gt/sources/39_Salario_Minimo_Historia.pdf` | p.4 note (EVID-340) |
| LB-014 | 39_, series 2008-2021 verbatim (three-sector era; values/AGs/dates as printed; defects [sic]): 2008 Agrícolas/No Agrícolas/Exportación y Maquila 47.00/48.50/47.75 diarios, 1,433.50Q/1,479.25Q/1,456.38Q [sic, GOQ-82] mensuales, AG No. 625-2007 (27/12/2007 / 31/12/2007), vigente 01-01-08 al 31/12/2008 · 2009 idem 52.00/52.00/47.75, 1,581.67Q/1,581.67Q/1,452.39Q, AG No.398-2008 (29/12/2008 / 30/12/2008), 01-01-09 al 31/12/2009 · 2010 56.00/56.00/51.75, 1,703.33Q/1,703.33Q/1,574.06Q, AG 347-2009 (29/12/2009 / 30/12/2009), 01-01-10 al 31/12/2010 · 2011 63.70/63.70/59.45, 1,937.54Q/1,937.54Q/1,808.27Q, AG 388-2010 (29/12/2010 / 30/12/2010), 01-01-11 al 31/12/2011 · 2012 68.00/68.00/62.50, 2,074.00Q/2,074.00Q/1,906.25Q, AG 520-2011 (28/12/2011 / 30/12/2011), 01-01-12 al 31/12/2012 · 2013 71.40/71.40/65.63, 2,171.75Q/2,171.75Q/1,996.25Q, AG 359-2012 (23/12/2012 / 28/12/2012), 01-01-13 al 31/12/2013 · 2014 74.97/74.97/68.91, 2,280.34Q/2,280.34Q/2,096.06Q, AG 537-2013 (26/12/2013 / 27/12/2013), 01-01-14 al 31/12/2014 · 2015 78.72/78.72/72.36, 2,394.40Q/2,394.40Q/2,200.95Q, AG 470-2014 (16/12/2014 / 23/12/2014), 01-01-15 al 31/12/2015 · 2016 ("Actividades No Agrícolas" [sic — first row mislabeled; read Agrícolas] ×2 / Exportación y Maquila) 81.87/81.87/74.89, 2,497.04Q/2,497.04Q/2,284.15Q, AG 303-2015 (29/12/2015 / 30/12/2015), 01-01-16 al 31-12-20016 [sic] · 2017 idem 86.90/86.90/79.48, 2,643.21Q/2,643.21Q/2,417.52Q, AG 288-2016 (29/12/2016 / 30/12/2016), 01-01-17 al 31-12-20017 [sic] · 2018 idem 90.16/90.16/82.46, 2,742.37Q/2,742.37Q/2,508.16Q, AG 297-2017 (27/12/2017 / 29/12/2017), 01-01-18 al 31-12-20018 [sic] · 2019 idem (freeze — same values as 2018) 90.16/90.16/82.46, 2,742.37Q/2,742.37Q/2,508.16Q, AG 242-2018 (27/12/2018 / 29/12/2018), 01-01-19 al 31-12-20019 [sic] · 2020 idem 90.16/92.88/84.88, 2,742.37Q/2,825.10Q/2,581.77Q, AG 320-2019 (27/12/2019 / 30/12/2019), 01-01-20 al 31/12/2020 · 2021 idem (freeze — same values as 2020) 90.16/92.88/84.88, 2,742.37Q/2,825.10Q/2,581.77Q, AG 250-2020 (29/12/2020 / 30/12/2020), 01-01-21 al 31/12/2021 | The three-sector series 2008-2021 (14 years × 3 rates): from 2008 the Exportación y Maquila sector appears; two freeze years — 2019 (= 2018 values) and 2021 (= 2020, COVID, cross-matching AG 250-2020 verbatim, LB-009/010); year-end vigencias 2016-2019 print a spurious extra zero ("20016"…"20019" [sic] — OCR defects, values otherwise consistent); the 2008 monthlies sit at daily × 30.5 rather than the SD × 365/12 formula — printed figures govern (GOQ-82) | `gt/sources/39_Salario_Minimo_Historia.pdf` | p.2 (2008-2011), p.3 (2012-2019), p.4 (2020-2021) (EVID-341) |
| LB-015 | 39_, series 1995-2007 verbatim (two-sector era; values/AGs/dates as printed): 1995 Agrícolas/No Agrícolas 14.50/16.00 diarios, 441.04Q/486.67Q mensuales, AG No.610-94 (4/10/1994 / 5/10/1994), "Vigente del 20-10-94 al 31-12-1995" · 1996 idem 15.95/17.60, 486.48Q/536.80Q, AG No. 667-95 (5/12/1995 / 18/12/1995), Vigente del 01-01-96 al 31-12-1996 · 1997 — "NOTA: SE PRORROGAN LOS SALARIOS MINIMOS DEL AÑO ANTERIOR." · 1998 idem 17.86/19.71, 543.24Q/599.51Q, AG No. 841-97 (10/12/1997 / 17/12/1997), Vigente del 01-01-98 al 29-01-1999 · 1999 idem 19.65/21.68, 597.69Q/659.43Q, AG No. 23-99 (13/01/1999 / 15/01/1999), Vigente del 30-01-99 al 25-01-2000 · 2000 idem 21.62/23.85, 659.41Q/727.42Q, AG No. 20-2000 (6/01/2000 / 11/01/2000), Vigente del 26-01-00 al 14-12-2000 · 2000/2001 idem 25.08/27.67, 762.85Q/841.63Q, AG No. 838-2000 (29/11/2000 / 30/11/2000), Vigente del 15-12-2000 al 31-12-2001 · 2002 idem 27.50/30.00, 836.46Q/912.50Q, AG No. 494-2001 (18/12/2001 / 19/12/2001), Vigente a partir del 01-01-02 al 31/12/02 · 2003 idem 31.90/34.20, 970.29Q/1,040.25Q, AG No. 459-2002 (28/11/2002 / 29/11/2002), Vigente del 01-01-03 al 31/12/03 · 2004 idem 38.60/39.67, 1,177.30Q/1,209.94Q, AG No. 765-2003 (27/11/2003 / 28/11/2003), vigencia split per LB-016 · 2005 idem (same values as 2004) 38.60/39.67, 1,177.30Q/1,209.94Q, AG No. 378-2004 (15/12/2004 / 17/12/2004), Vigente del 01-01-05 al 31-12-2005 · 2006 idem 42.46/43.64, 1,291.49Q/1,327.38Q, AG No. 640-2005 (1/12/2005 / 2/12/2005), Vigente del 01-01-06 al 31-12-2006 · 2007 idem 44.58/45.82, 1,355.98Q/1,393.69Q, AG No. 624-2006 (26/12/2006 / 28/12/2006), Vigente del 01-01-07 al 31-12-2007 | The two-sector series 1995-2007 (Agrícola/No Agrícola only): several transitions are NOT at 1-January — 1998's rates ran to 29-01-1999, 1999's from 30-01-99, 2000's from 26-01-00; AG 838-2000 took effect mid-December 2000 (15-12-2000) and ran 13 months to 31-12-2001, carrying all of 2001 (why 2001 has no own AG; the stray "AÑO 2,001:" header is an empty layout artifact); 1997 = prórroga of the 1996 rates; 2005 re-fixed 2004's values unchanged after the CC-suspension year | `gt/sources/39_Salario_Minimo_Historia.pdf` | p.1 (1995-2003 incl. 2001 carryover), p.2 (2004-2007) (EVID-342) |
| LB-016 | 39_, 2004 block, vigencia cell: "Vigente del 01 al 22 de enero y del 30 de julio al 31 de diciembre/2004, a causa de suspensión provisional. Ref. Exp. # 05-2004 de la Corte de Constitucionalidad." | AG 765-2003's 2004 rates were provisionally suspended by the Constitutional Court (Exp. 05-2004) from 23-Jan to 29-Jul-2004 — a six-month hole; the table does NOT state which values applied during the suspension (prima facie the 2003 rates reverted — GOQ-81); 2005 then re-fixed the identical 2004 figures | `gt/sources/39_Salario_Minimo_Historia.pdf` | p.2 AÑO 2,004 block, vigencia cell (EVID-343) |
| LB-017 | 38_ p.3 contamination (R43): after AG 250-2020's COMUNÍQUESE follows "MINISTERIO DE FINANZAS PÚBLICAS ACUERDO GUBERNATIVO NÚMERO 243-2020 Guatemala, 17 de diciembre de 2020" with budget object lines "071 — Aguinaldo … 15,000" / "072 Bonificación anual (Bono 14) Ñ [sic] … 15,000" / "073 — Bono vacacional … 15,000" / Art. 4: "El presente Acuerdo Gubernativo empieza a regir inmediatamente y deberá ser publicado en el Diario de Centro América." | Citation-hygiene guard: 38_ p.3 is a DIFFERENT, unrelated instrument (MinFin AG 243-2020, INFOM budget decrease) — never attribute its content to AG 250-2020; its expense-object nomenclature independently confirms the three-benefit taxonomy (Aguinaldo ≠ Bonificación anual (Bono 14) ≠ Bono vacacional) owned by `04_statutory-bonuses.md` | `gt/sources/38_Salario_Minimo_AG_250-2020.pdf` | p.3 (EVID-338) |

Version regime (D15/D16/D-GT10, cite with D15): every rate row carries
valid_from + instrument provenance + as-of qualifier, snapshot-on-write; the
2022–2025 vintages are ABSENT from the corpus and recorded as explicit GAP
rows with GOQ-11 flags — never interpolated; the 2004 CC-suspension window
is a dated gap (GOQ-81); lookups flag (and floor validation blocks) on any
date whose row is a gap. The CT text basis never supports a dated
consolidation claim (R44); the AG instruments are dated by their own Art. de
vigencia (fixed calendar dates 2021-01-01, 2026-01-01) and by the vigencia
strings the 39_ compilation prints for the historical years.

## 3. Functional Requirements

### 3.1 CT chassis — the fixing mechanism (CT Arts. 103-115)

- **GT-PAY-FR-051:** The system shall model every worker's entitlement to a
  *salario mínimo* covering normal needs of a material, moral and cultural
  order (CT art. 103) as THE salary-floor layer of this localization: all
  floor validation, destajo top-up and consumer interfaces of files
  02/04/07 resolve against THIS file's dated AG rows — the CT itself
  carries no monetary values (negative: no minimum-wage numeric may ever
  cite 32_). (LB-001; EVID-285)
- **GT-PAY-FR-052:** The minimum-wage system shall apply to ALL workers,
  with one recorded exception class: workers serving the State or its
  institutions whose remuneration is determined in a public budget are
  outside the system — such workers carry the state-budget exclusion flag
  and skip minimum-wage floor validation (a classification flag only; their
  payroll treatment is otherwise unchanged). (LB-002; EVID-285)
- **GT-PAY-FR-053:** The system shall record the fixing mechanism as the
  registry's cadence and dimension model: the Organismo Ejecutivo fixes
  *anualmente* (annually), via acuerdos issued through MinTrabajo, the
  minimum wages governing in each *actividad, empresa o circunscripción
  económica* — the expected re-issue cadence on the dated rows is ANNUAL,
  and the operative dimension model from 2026-01-01 is 2 circunscripciones
  (CE1/CE2, FR-056) × 3 actividades (FR-057); per-enterprise fixings
  (empresa) are admitted by the CT text as a legal possibility and appear
  as a configuration surface, never as seeded rows. (LB-003; LB-006;
  EVID-285, EVID-332)
- **GT-PAY-FR-054:** The system shall implement the automatic modification
  of CT art. 115: a minimum-wage fixing *modifica automáticamente* the
  employment contracts in which a lower wage was stipulated — when a dated
  row becomes operative (or a gap closes with a newly sourced vintage), the
  floor-validation status of every inferior contract flips to substituted
  and payroll pays the applicable minimum, without renegotiation; superior
  contractual wages are never reduced by a fixing. (LB-004; EVID-285)

### 3.2 The 2026 instrument and the CE-split structure (AG 256-2025)

- **GT-PAY-FR-055:** The system shall register AG 256-2025 as a dated
  instrument with full provenance — given 19-Dec-2025, published DCA
  22-Dec-2025 (No. 74, Tomo CCCXXVIII), rates effective on the FIXED date
  **2026-01-01** per its Art. 11 (never publication-relative) — and shall
  load its six rate tuples (FR-058) as the operative rows from that date;
  the vintage chain shall be recorded as metadata: AG 256-2025 (2026) →
  2022-2025 ABSENT (GOQ-11 gap rows, FR-070) → AG 250-2020 (2021) → the
  39_ historical series (1995-2020). (LB-005; EVID-331)
- **GT-PAY-FR-056:** The system shall implement the territorial zone model
  effective 2026-01-01: **CE1 = the departamento de Guatemala only; CE2 =
  every other department of the Republic** (the AG 285-2021
  circunscripciones; the POR TANTO variant "númoro 235-2021" [sic] is OCR
  damage — GOQ-79); pre-2026 vintages carry the single zone **Nacional**.
  Zone assignment for rate selection is resolved by the FR-060 cascade,
  never by the employer's domicile. (LB-006; EVID-332)
- **GT-PAY-FR-057:** The system shall classify employers/workers into the
  three rate actividades by CIIU Rev. 4 hooks as defined in AG 256-2025
  Art. 1: **Agrícola = section A** of the Classification's third part;
  **No Agrícola = sections B–U** (private sector); **Exportadora y de
  Maquila = one combined rate row** (although four paritarian commissions
  per CE exist — Agrícola, No Agrícola, Exportadora, Maquila — only three
  rates are fixed); the classifier is configuration over the CIIU code of
  the employer's registered activity (registration per AG 256-2025
  art. 8 b), never a free-text label. (LB-006; EVID-332, EVID-334)

### 3.3 The 2026 six-cell rate table (AG 256-2025 Arts. 2-7)

- **GT-PAY-FR-058:** The system shall load the six 2026 tuples as dated
  rows from the `salario_minimo.csv` sidecar, transcribed DIGIT-FOR-DIGIT
  [sic]-faithful to the print (daily + monthly; no hourly constant — see
  FR-059): CE1 Agrícola **124.64 / 3,791.20** (monthly digits garbled
  "(a, 3, fte 20)" [sic] — words govern, GOQ-78); CE1 No Agrícola
  **131.58 / 4,002.28**; CE1 Exportadora y de Maquila **112.10 / 3,409.73**
  (monthly digits garbled — words govern, GOQ-78); CE2 Agrícola
  **119.21 / 3,625.89**; CE2 No Agrícola **125.49 / 3,816.90** (printed
  digits "(Q. 3,416.90]" [sic] yield to their own words "TRES MIL
  OCHOCIENTOS DIECISEIS" — words govern, R35/GOQ-78); CE2 Exportadora y de
  Maquila **105.90 / 3,221.10** (words and digits agree as printed;
  diverges from the project-known prior 3,321.10 — NEVER "corrected",
  GOQ-77). The monthly figures are gazette constants: monthly ≈ daily ×
  365/12 only to centavos (124.64 → 3,791.13 computed vs 3,791.20 printed)
  and the printed monthlies ALWAYS govern (R35/GOQ-82).
  (LB-007; LB-005; EVID-333, EVID-331)
- **GT-PAY-FR-059:** The system shall derive the hourly rate of every
  2026-era tuple by PRORATION to the jornada, per the clause every rate
  article repeats — *que calculados por hora, se pagará la parte
  proporcional que corresponda dependiendo de la jornada de trabajo en la
  que se labore* (calculated by the hour, the proportional part
  corresponding to the workday worked shall be paid): hourly = daily ÷ the
  statutory ordinary hours of the worker's jornada class (file 02
  GT-PAY-FR-026 — 8 diurna / 6 nocturna / 7 mixta), never an independently
  printed constant; where a vintage PRINTS an hourly rate (2020-2021:
  Q11.27 / Q11.61 / Q10.61, "en jornada ordinaria diurna de trabajo o lo
  proporcional para las jornadas mixta o nocturna"), the printed hourly
  constant governs for ordinary diurnal jornadas and the mixed/nocturnal
  jornadas take the proportional derivation. (LB-007; LB-010; EVID-333,
  EVID-336)

### 3.4 Application rules (AG 256-2025 Art. 8; AG 250-2020 measures)

- **GT-PAY-FR-060:** The system shall select the applicable rate row by the
  location cascade of art. 8 c): (1) the place where the *centro de
  trabajo* (workplace) is located; (2) where no workplace can be determined
  by the nature of the service or the execution of the work, the place
  where its execution or provision is habitually performed; (3) where
  neither is determinable with clarity, the place where the worker
  habitually resides — in that order, each step only on failure of the
  former. (LB-008; EVID-334)
- **GT-PAY-FR-061:** The system shall guarantee the minimum-wage floor for
  *unidad de obra* and *participación* pay (pieza, precio alzado, destajo —
  the pay-basis taxonomy of `01_ct-salary-model.md` GT-PAY-FR-002): such
  workers *en ningún caso saldrán perjudicados* (shall in no case come out
  disadvantaged) and *en ningún caso* have a minimum lower than the AG fix
  — when a period's production/participation pay falls below the applicable
  dated daily minimum, payroll tops the period up to that floor (top-up
  line; the pay-basis itself is untouched).
  (LB-008; LB-001; EVID-334, EVID-285)
- **GT-PAY-FR-062:** The system shall pay the *bonificación incentivo* ON
  TOP of the applicable minimum wage as an INDIVISIBLE add-on: the D78-89
  incentivo (as amended — the Q250/month of D37-2001) must be paid
  additionally to the fixed minimum, its DIVISION is prohibited (*queda
  prohibida la división de esta prestación*), it is paid MONTHLY, and it
  shall never be netted against, absorbed into or deducted from the
  minimum — any rule that counts the incentivo toward satisfying the
  salario mínimo is rejected at definition time; the incentivo AMOUNT and
  its statutory regime are owned by `04_statutory-bonuses.md`
  (cross-reference by filename; this FR owns only the add-on mechanics
  against the minimum). (LB-008; LB-011; EVID-334, EVID-337)
- **GT-PAY-FR-063:** The system shall record the enforcement hook of art. 8
  f): non-payment of the fixed minimum gives rise to the sanction of CT
  art. 272 literal a) — WITHOUT exempting the employer from the obligation
  to pay the *salario mínimo adeudado* (minimum wage owed) to the affected
  worker: back-pay of the shortfall is a PAYROLL computation (the FR-061
  floor top-up applied retroactively over the affected periods), while the
  sanction VALUE is external (owned by
  `gt/requirements/taxation/06_ct-procedures.md` — never derived here); and
  pecuniary administrative sanctions whose unit of measure is fixed by law
  in minimum wages shall select their base rate per art. 9: the
  **no-agrícola rate of the corresponding circumscription** for labor
  matters, the **CE1 no-agrícola rate** for all other matters (selector
  configuration consuming this file's dated rows).
  (LB-008; LB-011; EVID-334, EVID-337)
- **GT-PAY-FR-064:** The system shall carry the *irrenunciabilidad*
  (non-waivability) guard: the minimum-wage acuerdos imply no renunciation
  of any right previously acquired by workers, and no contractual or
  configurational waiver of the dated floors is admissible — the FR-054
  substitution and FR-061 top-up apply regardless of contrary stipulations
  (guard row honored identically by both architecture sides).
  (LB-011; EVID-337; EVID-334 gloss art. 8 h))

### 3.5 The 2021 COVID-freeze vintage (AG 250-2020)

- **GT-PAY-FR-065:** The system shall load the 2021 vintage as dated rows
  effective **2021-01-01** with provenance given 29-Dec-2020 / DCA
  30-Dec-2020 (No. 30): a FREEZE — the 2020 rates continue unchanged
  (COVID-19 rationale) — single national zone, three activities, with the
  HOURLY and DAILY rates as printed in the AG itself (Agrícola Q11.27/h =
  Q90.16/day; No Agrícola Q11.61/h = Q92.88/day; Exportadora y Maquila
  Q10.61/h = Q84.88/day, proportional for mixed/nocturnal jornadas) and
  the monthly equivalents (2,742.37 / 2,825.10 / 2,581.77) sourced from
  the 39_ compilation (FR-066 discipline); the 2020 rows (AG 320-2019)
  carry the same daily/monthly values via 39_ — the freeze is recorded as
  provenance, not as duplicated truth (each year keeps its own dated
  rows). (LB-009; LB-010; LB-014; EVID-335, EVID-336, EVID-341)

### 3.6 The historical series 1995-2021 (39_ compilation)

- **GT-PAY-FR-066:** The system shall load the 1995-2021 series as dated
  rows from the `salario_minimo.csv` sidecar, hand-built from the official
  Departamento Nacional del Salario compilation: **2 sectors (Agrícola /
  No Agrícola) 1995-2007 → 3 sectors (plus Exportación y Maquila)
  2008-2021**, one national zone throughout, each row carrying daily +
  monthly as printed plus the AG number, emisión/publicación dates and
  vigencia range the compilation prints; because 39_ is a SECONDARY
  compilation, every normative citation of a historical row cites the
  UNDERLYING AG (instrument provenance "39_ compilation → AG nn-year"),
  never the compilation as the legal source; the 1997 *prórroga* (no own
  AG — 1996 rates continued) and the 2001 carryover (no own 2001 AG — AG
  838-2000, vigente 15-12-2000 al 31-12-2001, printed under the AÑO 2,000
  heading) are recorded as such in the instrument field.
  (LB-012; LB-014; LB-015; EVID-339, EVID-341, EVID-342)
- **GT-PAY-FR-067:** The system shall treat the monthly ⇄ daily conversion
  formula *SD × 365 / 12* (daily salary × the total days of the year ÷
  twelve) as an ESTIMATION/DISPLAY rule only: statutory rows always carry
  the PRINTED figures, which govern even where they diverge from the
  formula — the 2008 monthlies sit at daily × 30.5 rather than × 365/12
  (maquila 1,456.38 printed vs 1,452.40 computed [sic]) and the 2026
  monthlies diverge by centavos (R35/GOQ-82); no payroll computation may
  recompute a monthly from a daily (or vice versa) when both are printed.
  (LB-013; LB-007; LB-014; EVID-340, EVID-333, EVID-341)
- **GT-PAY-FR-068:** The system shall keep the effective-date ledger of the
  series EXACTLY as the instruments fix it — the 1995 rows starting
  20-10-1994; late-January transitions in the two-sector era (1998's rates
  vigente to 29-01-1999; 1999's from 30-01-99; 2000's from 26-01-00; then
  AG 838-2000 from 15-12-2000); 1-January vigencias from 2002 onward —
  as-of resolution (D16 anchors) selects rows by valid_from/valid_to and
  NEVER assumes 1-January changeovers pre-2002; the spurious year-end
  prints "31-12-20016"…"20019" [sic] are OCR defects resolved to
  31-12-2016…2019 with [sic] notes on the rows.
  (LB-015; LB-014; EVID-342, EVID-341)
- **GT-PAY-FR-069:** The system shall model the 2004 Constitutional-Court
  suspension as dated GAP segments: AG 765-2003's rates were vigente 01-22
  January 2004 and 30 July-31 December 2004 only, suspended provisionally
  (Exp. 05-2004, Corte de Constitucionalidad) 23-January to 29-July 2004 —
  the CSV carries TWO rate segments plus an explicit suspension gap row
  per actividad; the values applicable DURING the suspension are
  unresolved (prima facie the 2003 rates reverted) and are NEVER
  interpolated (GOQ-81); 2005 (AG 378-2004) re-fixed the identical 2004
  figures, which load as their own dated rows. (LB-016; LB-015; EVID-343,
  EVID-342)

### 3.7 The 2022-2025 gap regime (GOQ-11)

- **GT-PAY-FR-070:** The system shall record the 2022-2025 vintages as
  ABSENT gap rows — one explicit gap row per year, zone Nacional, all
  actividades, empty rate fields, GOQ-11 flag — because the corpus holds
  no instrument for those years (39_ stops at 2021; 37_ = 2026): lookups
  resolving to a gap year RAISE the GOQ-11 flag and BLOCK floor
  validation, OT-base flooring, destajo top-up and every consumer
  interface — no value is ever interpolated, extrapolated or carried over
  from 2021/2020 into the gap years; the rows enter only when the AGs are
  externally sourced (acquisition watch, DOWNLOAD_QUEUE rev 7).
  (LB-012; EVID-339; GOQ-11 → OQ-001)

### 3.8 Consumer interfaces and citation guards

- **GT-PAY-FR-071:** This file OWNS the minimum side of the overtime base:
  file 02's rule GT-PAY-FR-033 (*≥ +50% over max(statutory minimum, agreed
  wage)*) consumes the applicable dated daily minimum from this file's rows
  (hourly derivation per FR-059) — this file supplies values and selectors
  only, never OT arithmetic; the interface is the single dated lookup
  every OT line resolves against (consumed by id, never restated there).
  (LB-003; LB-007; LB-014; EVID-285, EVID-333, EVID-341)
- **GT-PAY-FR-072:** This file feeds the inembargabilidad carve-out of
  file 01 (GT-PAY-FR-010): *salarios mínimos* earners are fully
  unembargable — the fully-protected-floor test reads THIS file's dated
  rows (worker's salary at the applicable minimum ⇒ minimum-wage earner ⇒
  GT-PAY-FR-010's protected floor applies, save its alimony carve-out);
  file 01 owns the ladder structure, this file the earner-identification
  values. (LB-001; LB-007; EVID-285, EVID-333)
- **GT-PAY-FR-073:** This file feeds the IGSS interfaces of file 07 (by
  filename, `07_igss-contributions.md`): the estimated-salary floor of
  IGSS *revisiones contables* = the salario mínimo of the AG vigente, and
  the IGSS minimum contribution base is a floor concept on the same salary
  (master-index P2 crossref, EVID-312/317, EV03b — pointers outside this
  file's LB slice, never restated as verbatim here); this file supplies
  only the dated as-of resolution of "AG vigente" per D16 anchors.
  (LB-003; EVID-285; master index P2 crossref row)
- **GT-PAY-FR-074:** FEED-CONTRACTS-ONLY guard toward taxation: this file
  exposes dated rate rows, zone/actividad selectors and floor interfaces
  to contracts and consumer files — it computes NO ISR/IVA arithmetic; the
  payroll ISR interfaces belong to `09_isr-iva-interfaces.md` (by
  filename), which consumes whatever minimum-anchored thresholds its own
  evidence supports; no tax rule may be seeded from this file's values.
  (LB-005; LB-012; EVID-331, EVID-339)
- **GT-PAY-FR-075:** CITATION-HYGIENE GUARD (R43-kin): the third page of
  the 38_ source is a different, unrelated instrument — MinFin AG 243-2020
  (INFOM budget decrease) — and NO requirement, citation or rate row may
  attribute its content (budget lines "071 Aguinaldo / 072 Bonificación
  anual (Bono 14) / 073 Bono vacacional") to AG 250-2020; the trio's
  independent value — confirming Aguinaldo ≠ Bono 14 ≠ Bono vacacional —
  is consumed by `04_statutory-bonuses.md` (by filename); attempts to
  cite 38_ p.3 material as AG 250-2020 are rejected at definition time.
  (LB-017; EVID-338)

## 4. Data Model

Layer semantics (thin-client architecture, D15/D16/D-GT10): the rate SERIES
is `shared` dated data (both sides resolve the same row against the same D16
anchor); floor application in payslip/destajo computation is `odoo`; as-of
resolution against D16 anchors is `shared`. No CT-derived numerics exist in
this layer (values live only in the AG instruments). Dated rows follow
D15/D16: valid_from/valid_to + instrument provenance; snapshot-on-write;
2022-2025 gap rows carry the GOQ-11 flag; 2004 suspension segments carry
the GOQ-81 flag.

**Dated rate rows (the series — `salario_minimo.csv` sidecar):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.minimum.wage (shared) | year · zone · actividad | int · select · select | zone: nacional (pre-2026) · ce1 · ce2 (from 2026-01-01); actividad: agricola · no_agricola · exportadora_maquila (2 sectores 1995-2007; 3 from 2008) | FR-055, FR-056, FR-057, FR-066 |
| l10n_gt.pay.minimum.wage | rate_daily / rate_monthly / rate_hourly | monetary (nullable) | as printed — hourly only where the AG prints it (2020-2021); 2026 rows print daily+monthly only; NEVER recomputed (SD × 365/12 = estimation only, R35/GOQ-82) | FR-058, FR-059, FR-065, FR-067 |
| l10n_gt.pay.minimum.wage | valid_from / valid_to / instrument / source_evid / fidelity_note | date · date · char · char · char | instrument = AG number (e.g. "AG 256-2025") or "39_ compilation → AG nn-year" / "prórroga per 39_ NOTA"; fidelity_note carries [sic] / words-govern / gap flags (GOQ-77/78/82) | FR-055, FR-058, FR-066, FR-068 |
| l10n_gt.pay.minimum.wage (gap rows) | rate fields empty + gap flag | flag | 2022-2025 one gap row per year (GOQ-11); 2004 suspension window 2004-01-23→2004-07-29 per actividad (GOQ-81); lookups block, never interpolate | FR-069, FR-070 |

**Selection, floors and interfaces:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract / hr.work.location | gt_pay_sm_zone (computed) | select | nacional · ce1 · ce2 via the art. 8 c) cascade workplace → habitual execution place → worker habitual residence | FR-056, FR-060 |
| hr.contract | gt_pay_sm_actividad | select | CIIU Rev. 4 classifier: agricola (section A) · no_agricola (B–U, private) · exportadora_maquila | FR-057 |
| hr.contract | gt_pay_state_budget_excluded | boolean | CT art. 104 exception — outside the minimum-wage system | FR-052 |
| hr.contract | gt_pay_sm_substituted | boolean (computed, dated) | CT art. 115 auto-modification flag: contract wage < operative dated minimum → true; re-evaluated on every dated-row change | FR-054 |
| hr.payslip | gt_pay_sm_floor_topup | monetary (computed) | destajo/obra/participación period top-up to the applicable dated daily minimum; also the back-pay engine of FR-063 | FR-061, FR-063 |
| hr.payslip line | gt_pay_sm_hourly_prorate | monetary (computed) | daily ÷ jornada-class hours (8/6/7 per file 02 GT-PAY-FR-026); printed hourly constants govern where they exist (2020-2021) | FR-059 |
| hr.salary.rule | gt_pay_incentivo_addon | rule constraint | incentivo ON TOP of the minimum, indivisible, monthly — never netted/absorbed/deducted; amount owned by file 04 | FR-062 |
| l10n_gt.pay.sanction.base.selector | matter_type → rate row | config | labor matters → no-agrícola rate of the corresponding CE; other matters → CE1 no-agrícola rate (AG 256-2025 art. 9) | FR-063 |
| l10n_gt.pay.guard | negative rows | char | state_budget_excluded (CT 104) · sm_numeric_in_ct = REJECTED · waivor_of_floors = REJECTED (irrenunciabilidad) · 38_p3_attr = REJECTED (R43) | FR-051, FR-064, FR-075 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. Payroll-wave defaults
(binding for this file): the dated rate series and its as-of resolution =
`shared`; floor application in payslip/destajo computation = `odoo`; guard
rows = `shared`. Model names stable across Odoo 17/18/19/20; no
version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-051 | shared | — (dated rows §4) | floor-layer contract | Values only from AG instruments; CT cites mechanism only; both sides resolve the same rows |
| FR-052 | odoo | hr.contract | gt_pay_state_budget_excluded | CT art. 104 exception flag; validation skip only |
| FR-053 | shared | — (registry metadata §4) | annual AG cadence + 2×3 dimensions | Per-empresa fixing = configuration surface, never seeded |
| FR-054 | odoo | hr.contract | gt_pay_sm_substituted | CT 115 auto-flip on dated-row change; superior wages untouched |
| FR-055 | shared | — (instrument registry §4) | AG 256-2025 provenance | given 19-Dec-2025; DCA 22-Dec-2025 No. 74 Tomo CCCXXVIII; fixed-date vigencia 2026-01-01 |
| FR-056 | odoo | hr.contract / hr.work.location | gt_pay_sm_zone | CE1 = dept. Guatemala; CE2 = rest; Nacional pre-2026; resolved via FR-060 cascade |
| FR-057 | odoo | hr.contract | gt_pay_sm_actividad | CIIU Rev. 4 A / B–U classifier; exportadora_maquila combined row |
| FR-058 | shared | — (CSV seeding §4) | six 2026 tuples | [sic]-faithful; words govern arts. 2/4/6 (GOQ-78); art. 7 as printed (GOQ-77); printed monthlies govern (R35/GOQ-82) |
| FR-059 | odoo | hr.payslip line | gt_pay_sm_hourly_prorate | daily ÷ jornada-class hours; printed hourly constants (2020-2021) govern where they exist |
| FR-060 | odoo | hr.contract / hr.work.location | cascade selector | workplace → habitual execution place → worker residence (art. 8 c)) |
| FR-061 | odoo | hr.payslip | gt_pay_sm_floor_topup | destajo/obra/participación period top-up to the dated daily minimum |
| FR-062 | odoo | hr.salary.rule | gt_pay_incentivo_addon | indivisible, monthly, on top of the minimum; amount = file 04 (D37-2001 Q250) |
| FR-063 | odoo | hr.payslip + selector config | back-pay + sanction-base selector | CT 272 a) hook; sanction VALUE external (taxation/06); rate selector per AG art. 9 |
| FR-064 | shared | — (guard row §4) | irrenunciabilidad guard | No waiver of dated floors honored by either side |
| FR-065 | shared | — (CSV seeding §4) | 2021 freeze vintage | hourly+daily printed in AG 250-2020; monthly via 39_; single national zone; vigencia 2021-01-01 |
| FR-066 | shared | — (CSV seeding §4) | 1995-2021 series | 2→3 sectors; instrument = "39_ compilation → AG nn-year"; prórroga/2001 carryover recorded |
| FR-067 | shared | — (row fidelity §4) | printed figures govern | SD × 365/12 estimation only; 2008 ×30.5 monthlies [sic] kept (GOQ-82) |
| FR-068 | shared | — (valid_from/valid_to §4) | effective-date ledger | late-January transitions 1995-2007; "20016"…"20019" [sic] resolved with notes |
| FR-069 | shared | — (gap rows §4) | 2004 CC-suspension segments | two rate segments + gap row per actividad; suspension values unresolved (GOQ-81) |
| FR-070 | shared | — (gap rows §4) | 2022-2025 ABSENT | GOQ-11 flags; lookups block every consumer; never interpolated |
| FR-071 | shared | — (interface contract §4) | OT-base minimum feed | Consumer: file 02 GT-PAY-FR-033 (max(minimum, agreed)); values only |
| FR-072 | shared | — (interface contract §4) | minimum-wage-earner feed | Consumer: file 01 GT-PAY-FR-010 fully-protected floor |
| FR-073 | shared | — (interface contract §4) | IGSS "AG vigente" as-of feed | Consumer: file 07 by filename (EVID-312/317 pointers, EV03b) |
| FR-074 | shared | — (interface contract §4) | feed-contracts-only guard | No ISR/IVA computation here; consumer: file 09 by filename |
| FR-075 | shared | — (guard row §4) | 38_ p.3 attribution ban | R43-kin; AG 243-2020 ≠ AG 250-2020; trio consumed by file 04 |

Version-regime notes (D12/D15/D16): the only values in this file are the
AG dated rows — 2026 (AG 256-2025), 2021 (AG 250-2020), 1995-2021 (39_
compilation citing 26 AGs from 610-94); 2022-2025 are ABSENT gap rows
(GOQ-11) and the 2004 suspension window is a gap (GOQ-81) — loaders flag
and block rather than interpolating; new vintages arrive on the CT art. 113
annual cadence and append as new valid_from rows with instrument
provenance; [sic]/words-govern fidelity notes survive re-issues only as
re-printed (R35).

## 6. Acceptance Criteria

- **AC-001:** Given a 2026 CE2 No Agrícolas worker, when the applicable row
  resolves, then the daily minimum is Q125.49 and the monthly minimum is
  **Q3,816.90** — the printed digits "(Q. 3,416.90]" [sic] yield to their
  own words "TRES MIL OCHOCIENTOS DIECISEIS" (words govern, R35/GOQ-78),
  and the CSV note records the defect. (FR-058)
- **AC-002:** Given the 2026 CE2 Exportadora y de Maquila row, when any
  configuration or correction proposes Q3,321.10 (the project-known
  prior), then it is rejected — the row keeps **Q3,221.10** as printed
  (words and digits agree; GOQ-77) pending clean-scan verification.
  (FR-058)
- **AC-003:** Given a CE1 No Agrícolas worker on a 4-hour ordinary diurnal
  jornada (half the 8-hour class), when the day pays, then the hourly
  proration yields 131.58 ÷ 8 × 4 = Q65.79 — the proportional-part clause,
  never an independently printed hourly constant.
  (FR-059; file 02 GT-PAY-FR-026)
- **AC-004:** Given a worker contracted by a Guatemala-City firm whose
  centro de trabajo sits in Zacapa, when the zone resolves, then CE2 rates
  apply (workplace location governs); given no determinable workplace and
  habitual execution in Mixco, then CE1 rates apply; given neither
  determinable, then the worker's habitual residence governs.
  (FR-056, FR-060)
- **AC-005:** Given a destajo (piecework) worker whose period production
  pay totals Q1,900 against an applicable dated daily minimum of Q92.88 ×
  22 worked days = Q2,043.36, when the payslip computes, then a floor
  top-up line of Q143.36 brings the period to the floor — the pay basis is
  untouched and the worker never comes out disadvantaged.
  (FR-061)
- **AC-006:** Given a minimum-wage earner's January 2026 payslip, when the
  incentivo line books, then it appears ON TOP of the applicable minimum as
  a separate indivisible monthly add-on (Q250 per file 04's D37-2001), and
  any rule netting, dividing or absorbing it against the minimum is
  rejected at definition time. (FR-062)
- **AC-007:** Given a contract stipulating Q120.00/day for a CE1 Agrícolas
  worker, when AG 256-2025 becomes operative on 2026-01-01, then the
  contract's floor validation flips to substituted and payroll pays
  Q124.64/day automatically (CT art. 115 — no renegotiation); given a
  Q130.00/day contract, then it is untouched. (FR-054, FR-058)
- **AC-008:** Given a rate lookup for 15-May-2004 (inside the CC
  suspension window), then the GOQ-81 gap flag raises and no value returns
  — never interpolated; given lookups for 5-Jan-2004 and 15-Aug-2004, then
  AG 765-2003's values (Q38.60 / Q39.67 daily) return from the two rate
  segments. (FR-069)
- **AC-009:** Given a rate lookup for any date in 2023, then the GOQ-11
  ABSENT flag raises and floor validation, OT-base flooring and the destajo
  top-up BLOCK — no 2021/2020 value is carried over or extrapolated into
  the gap years. (FR-070)
- **AC-010:** Given the CE1 Agrícola 2026 row, when the monthly value is
  read, then it is Q3,791.20 as printed — NOT the SD × 365/12 computation
  Q3,791.13; given the 2008 Exportación y Maquila row, then its monthly
  Q1,456.38 [sic, computed at × 30.5] is kept digit-for-digit (printed
  figures govern, R35/GOQ-82). (FR-058, FR-067)
- **AC-011:** Given a 2026 CE2 Agrícolas worker with an agreed wage of
  Q100.00/day working 2 extraordinary hours, when file 02's OT rule
  (GT-PAY-FR-033) computes, then the OT base floors at this file's dated
  minimum Q119.21 (max(minimum, agreed)) and each extraordinary hour pays
  ≥ 1.5 × (119.21 ÷ 8) — values from this file, arithmetic owned by file
  02. (FR-071, FR-059; file 02 GT-PAY-FR-033)
- **AC-012:** Given a worker whose salary sits at the applicable dated
  minimum, when garnishment processing runs per file 01 (GT-PAY-FR-010),
  then the fully-protected floor applies (minimum-wage earner) save the
  alimony carve-out — the earner test reads this file's rows.
  (FR-072; file 01 GT-PAY-FR-010)
- **AC-013:** Given an employer paying below the fixed minimum in 2026,
  when enforcement hooks fire, then the record carries the CT art. 272 a)
  sanction pointer (VALUE external, taxation/06) plus the back-pay
  computation of the shortfall via the FR-061 top-up applied retroactively;
  given a labor-matter pecuniary sanction denominated in minimum wages of
  CE2, then its base rate selector picks the CE2 no-agrícola daily row
  (Q125.49). (FR-063)
- **AC-014:** Given any attempt to cite the 38_ p.3 budget lines ("071
  Aguinaldo / 072 Bonificación anual (Bono 14) / 073 Bono vacacional") as
  content of AG 250-2020, then the R43-kin citation guard rejects it at
  definition time — p.3 belongs to MinFin AG 243-2020 alone.
  (FR-075)
- **AC-015:** Given a rate lookup for 15-Jan-1999, then the 1998 vintage
  (AG 841-97) still resolves — its vigencia runs to 29-01-1999 — and the
  1999 vintage (AG 23-99) resolves only from 30-01-1999: the ledger never
  assumes 1-January changeovers pre-2002. (FR-068)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.3);
this file OWNS **GOQ-77, GOQ-78, GOQ-79, GOQ-80, GOQ-81, GOQ-82, GOQ-11** —
each carried below with Status open. No other OQ ids are used; no new OQ
ids are invented.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| GOQ-77 | 37_ art. 7 CE2 Exportadora y de Maquila monthly = **3,221.10 as printed** (words "TRES MIL DOSCIENTOS WEINTIUN [sic] … DIEZ CENTAVOS" and digits "(0. 3,221.10)" agree) vs the project-known prior 3,321.10 — clean-scan/second-source verification needed before freezing the 2026 row; the row is NEVER "corrected" in the meantime (FR-058, AC-002). | no | GT synthesis wave S-GT3 (sources watch) | open |
| GOQ-78 | 37_ digit-level defects: art. 2 monthly digits fully garbled ("(a, 3, fte 20)" — words 3,791.20 govern); art. 4 monthly digits garbled ("la 3, Q. 73)" — words 3,409.73 govern); art. 6 monthly digits "3,416.90" [sic] vs own words 3,816.90 (words govern, R35) — clean-scan confirmation of all three words-govern resolutions pending. | no | GT synthesis wave S-GT3 (sources watch) | open |
| GOQ-79 | 37_ cites both "AG 285-2021" (considerando III) and "AG númoro 235-2021" [sic] (POR TANTO), same date 21-Dec-2021, different numbers — one is OCR damage; identify the actual structural hook creating the Circunscripciones Económicas (working reading: 285-2021, FR-056). | no | GT synthesis wave S-GT3 (sources watch) | open |
| GOQ-80 | 37_/38_ metadata minors (none value-bearing): considerando garbles ("artículo 133 hiteral e]" [sic — read 183 e]); "Decreto número 330" [sic — CT is D1441]; unreadable signature block (OQ-5); 38_ double-Artículo-8 numbering (sequence 5, "8", 7, 8, 9, 10 — OQ-6). Transcribed [sic]; no requirement depends on them. | no | GT synthesis wave S-GT3 (sources watch) | open |
| GOQ-81 | 2004 CC-suspension segment (Exp. 05-2004, Corte de Constitucionalidad): which rates applied 23-Jan→29-Jul-2004 — presumably 2003's reverted (AG 459-2002 values); unresolved in the corpus, modelled as a blocking gap row (FR-069, AC-008); never interpolated. | no | GT synthesis wave S-GT3 (sources watch) | open |
| GOQ-82 | 39_/37_ internal [sic] arithmetic rows: the 2008 monthlies sit at daily × 30.5 rather than the printed SD × 365/12 formula (maquila 1,456.38 vs 1,452.40 computed); 37_ monthlies diverge from the formula by centavos (124.64 → 3,791.13 computed vs 3,791.20 printed) — PRINTED FIGURES GOVERN (R35); the CSV carries the [sic] notes (FR-058, FR-067, AC-010). | no | GT synthesis wave S-GT3 (sources registry) | open |
| GOQ-11 | Salario mínimo 2022-2025 AGs ABSENT from the corpus (39_ ends 2021; 37_ = 2026) — explicit gap rows with flags, never interpolated (FR-070, AC-009); rows enter only when the AGs are sourced externally (DOWNLOAD_QUEUE rev 7); until then every consumer interface blocks on those years. | no | GT synthesis wave S-GT3 (sources watch) | open |
