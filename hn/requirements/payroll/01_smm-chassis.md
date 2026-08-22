# HN — Payroll — SMM chassis: salario mínimo machinery, bienio dated rows, maquila track & promedio supply

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

Age-boundary note (V-HN1): payroll owns NO 60+/65+ rules — the adulto-mayor
deduction/exemption tiers are taxation-owned (`../taxation/02_isr-deductions.md`
FR-066..068, consumed by id) and resolve by the worker's birthday year per
D-H2; payroll's only age-keyed rules are the minors' regimes of
`09_suspension-maternity-special.md` (FR-345..348).


This file defines the functional requirements for the Honduras *salario mínimo*
(statutory minimum wage, SMM) chassis of cluster P1. It owns: (a) the Ley D. 103
machinery as payroll outcomes — the *irrenunciabilidad* (non-waivability)
public-order floor, auto-elevation of inferior stipulations, the Art. 20
piece-rate sufficiency test (*salarios por obra/destajo* must let an
average-yield worker earn at least the SMM), the no-age/no-sex classification
invariant, applicability and exemption flags, and the institutional chain
encoded as provenance metadata; (b) the DATED SMM value rows — the
`smm_tables.csv` sidecar with the general track (11 ramas × 4 employer-size
bands), the separate maquila/zonas-libres track (R-H48) and the *salario
mínimo promedio* (average minimum wage) rows (R-H47: DGS-print-only, single
national value, never recomputed — THE feed consumed by the ISR plantilla's
13th/14th-month 10×SMM-promedio caps) — plus their loading, resolution,
supersession and config-gap discipline; (c) the bienio percentage chains
2022-2027 as metadata, the per-instrument retro-payment deadlines, and the
salvaguarda/escalator chain including the PENDING conditional 2027
IPC-escalator row (dic-2026 trigger, de-oficio).

It does **not** cover: the 13th/14th-month and bono educativo computation
engines and the bono TABLE (92_) — file 02 (`02_13th-14th-bono.md`,
HN-PAYR-FR-051..087; this file supplies only the SMM rows it consumes); IHSS
cotizaciones and incapacidad (files 03/04, HN-PAYR-FR-101..135/141..170);
RAP/fondo (file 05, HN-PAYR-FR-181..215); jornada (file 06,
HN-PAYR-FR-221..247); vacaciones (file 07, HN-PAYR-FR-261..280);
cesantía/preaviso (file 08, HN-PAYR-FR-291..325); suspension/maternity (file
09, HN-PAYR-FR-331..357); the Código del Trabajo chassis and salary/records
surfaces (file 10, HN-PAYR-FR-371..405 — CT Arts. 381-390 cited by article
only); the ISR 10×SMM-promedio cap derivation and the plantilla algorithm
(taxation/04, `HN-TAX-FR-121..153`, esp. FR-134 — this file owns only the
promedio row supply); ISR deduction semantics (taxation/02,
HN-TAX-FR-046..078); the DJIMR/DMR export contract (HN-FREP-FR-054/055) and
the OVI/SW chassis + due-day engine (HN-FREP-FR-001..032); comprobante de
retención (HN-EINV-FR-139/140); and CT sanctions/multa computation (T11 —
this file supplies only the SMM/promedio unit values by id).

## 2. Legal Basis

Authority order (binding, per master evidence index): the SMM machinery =
D. 103 (Ley del Salario Mínimo, `104_`, compilation print with a CT
running-header artifact — 104_ OQ-2) as reformed by D. 43-97 of 28-abr-1997
(footnote year "1977" [sic] = print defect, R-H43); the bienio instruments =
STSS-308-2022 (`101_`) → SETRASS-014-2023 (`83_`, uniform 9.80% re-fix) →
SETRASS-109-2024 (`82_`, bienio 2024-2025 + 3-year maquila track) →
SETRASS-233-2026 (`90_`, current bienio 2026-2027, OCR sidecar authoritative
for damaged passages), with the maquila split instrument SETRASS-411-2023
(`84_`); the value/promedio prints = DGS tables (`91_`). D-H1/D-H2/D-H3 bind
everything (dated rows, hecho-generador/period resolution, never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley del Salario Mínimo (D. 103-1971), Arts. 1-2 | Art. 1: "La presente Ley tiene como finalidad esencial determinar los procedimientos para la aplicación del Salario Mínimo y los Organismos encargados de su establecimiento, vigilancia, control y cumplimiento. Son de orden público sus disposiciones y de aplicación general para trabajadores y patronos." Art. 2: "El Salario Mínimo es irrenunciable, por tanto no podrán pagarse sueldos o salarios inferiores a los que se fijen de acuerdo a esta Ley ni podrán ser disminuidos mediante contratación individual o colectiva u otro pacto cualquiera." | The Law's provisions are public order and of general application to workers and employers; the minimum wage is non-waivable — no salaries lower than those fixed under this Law may be paid, nor may they be diminished by individual or collective contract or any other pact | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Arts. 1-2 (p.1) (EV82:EVID-215) |
| LB-002 | Ley SMM, Arts. 15-16, 28-31 | Art. 15: "Para la fijación o revisión de los Salarios Mínimos en cualquier actividad económica, se designará una Comisión de Salario Mínimo, la cual estará integrada por tres (3) miembros representantes del interés patronal, tres (3) miembros representantes del interés obrero y tres (3) miembros por el interés público…" Art. 30: "Una vez aprobado el Proyecto de Acuerdo por la Secretaría de Trabajo y Seguridad Social, ésta ordenará su publicación en el Diario Oficial 'La Gaceta' y el Acuerdo entrará en vigencia quince (15) días después de su publicación..." | Tripartite Minimum Wage Commission (3 employer + 3 worker + 3 public members) drafts; SETRASS approves within 20 days (silence = approval); gazette publication; effectivity 15 days after publication — in tension with the bienios' retroactive 1-ene vigencia (the instruments' own clauses control) | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Arts. 15-16 (pp.5-7), 28-31 (pp.9-11) (EV82:EVID-216) |
| LB-003 | Ley SMM, Art. 20 | "Si los Salarios pagados por los patronos fuesen por jornada de trabajo u otra unidad de tiempo, por unidad de obra o por cualquiera otra modalidad de pago, la remuneración que se pague deberá ser suficiente para que un trabajador de mediano rendimiento obtenga, por lo menos el salario mínimo fijado para la actividad que se trate." | Whatever the pay modality — time, unit of work (pieza/obra), or any other — the remuneration paid must be sufficient for an average-yield worker to obtain at least the minimum wage fixed for the activity: the floor binds EFFECTIVE earnings | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 20 (p.7, printed "ARTÍCULO 201.-" fn.-run-on) (EV82:EVID-217) |
| LB-004 | Ley SMM, Art. 24 | "Podrán fijarse salarios móviles, determinados por la relación básica existente entre el precio del producto y los salarios, bien por promedios quincenales o mensuales de dicho precio, o por cualquier otro medio… En todo caso los salarios móviles no serán inferiores a los salarios básicos que se fijen para la industria de que se trate." | Mobile salaries (indexed to the product-price/salary relation, by biweekly or monthly averages or other means) may be fixed but are never below the basic salaries fixed for the industry | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 24 (p.8) (EV82:EVID-217) |
| LB-005 | Ley SMM, Art. 25 d) | "No se hará clasificación alguna según este Artículo a base de edad o sexo." | No classification shall be made on the basis of age or sex (no age/sex-differentiated SMM) | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 25 d) (p.9) (EV82:EVID-217) |
| LB-006 | Ley SMM, Arts. 47-48, 32-33 | Art. 47: "Para los efectos de esta Ley, industria significa cualquier campo de actividad económica…" Art. 48: "Quedan exceptuados de esta Ley, los empleados públicos cuyo puesto ha sido creado por la Constitución, la Ley, Decreto Ejecutivo o Acuerdo Municipal, así como también los Gerentes, Administradores y Profesionales. Los trabajadores de oficios domésticos en habitaciones o residencias particulares, estarán sujetos a un régimen especial." Art. 33: "Los Salarios Mínimos fijados no serán aplicables a los aprendices…" Art. 32: incapaces with a DGS special permit "…el porcentaje del Salario Mínimo aplicable que deberá pagársele y el período…" | "Industria" = any field of economic activity; EXEMPT from the law: constitutionally/legally created public servants, managers/administrators/professionals; domestic workers under a special regime; apprentices outside the floor (learning-period wage set by the unpublished Reglamento); DGS-certified incapaces paid a %-of-SMM under permit | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Arts. 47-48, 32-33 (pp.11-14) (EV82:EVID-220) |
| LB-007 | Ley SMM, Art. 35 (reformed D. 43-97) | "Los Salarios Mínimos deberán ser revisados por lo menos una vez (1) al año en el mes de diciembre, para que entre en vigencia en enero del siguiente año, tomando en cuenta la variación del promedio de la inflación acumulada a noviembre. También se podrá hacer una revisión en el mes de junio… para que entre en vigencia en el mes de julio… siempre y cuando el índice de inflación acumulada en el primer semestre del año exceda al doce por ciento (12%)…" (reform footnote year "1977" [sic] = 1997 print defect, R-H43) | Minimum wages must be reviewed at least once a year in December for January effectivity, keyed to accumulated inflation to November; extraordinary June review (July effectivity) only if first-semester inflation exceeds 12% | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` + `hn/sources/106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf` | 103-Art. 35 (p.12) (EV82:EVID-219); gazette original G 28,271 (EV106:EVID-374) |
| LB-008 | Acuerdo SETRASS-233-2026, Art. 1 + CONSIDERANDO (7) | Art. 1: "…el ajuste al salario mínimo que regirá en todo el país por un periodo de dos (2) años, mismo que entrará en vigencia a partir del uno (01) de enero al treinta y uno (31) de diciembre de cada año negociado…" [cuadro 2026: 6/6/7/7; 2027: 6/6/7/7.5 — R-H45]. CONS.(7): "…la inflación oficial interanual registrada por el Banco Central de Honduras (BCH) al mes de diciembre del año dos mil veinticinco (2025), alcanzó el porcentaje de 4.98%, siendo superior a los porcentajes de ajuste acordados para el año dos mil veinticuatro (2024), de 5.5% en la categoría de 1 a 10 trabajadores, de 5.50% de 11 a 50 trabajadores, de 6.5% de 51 a 150 trabajadores y de 7.00% de 151 trabajadores en adelante, plasmados en el Acuerdo Ejecutivo No. SETRASS-109-2024…" (the comparison is false — drafting defect, R-H63) | The 2026-2027 bienio percentages by size band (2026: 6/6/7/7; 2027: 6/6/7/7.5); calendar-year vigencia per negotiated year; the considerando quotes the 2024 bienio percentages and the dic-2025 IPC 4.98% trigger datum | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Art. 1 (p.3); CONS.(7) (p.2) (EV82:EVID-222; EV82:EVID-221) |
| LB-009 | Acuerdo SETRASS-233-2026, Art. 2 (tabla 2026) | "Aprobar la Nueva Tabla de Salario mínimo en razón de la negociación de porcentajes de ajuste al Salario Mínimo, que regirá en todo el país para el año 2026 y año 2027, de conformidad a las actividades económicas y número de trabajadores de la manera siguiente:" [11 ramas × 4 bands × mensual/jornada-8h/hora; e.g. manufacturera 1-10: 12,869.14 / 428.97 / 53.62; agricultura 1-10: 9,596.64 / 319.89 / 39.99] | Approves the new SMM table for 2026-2027 by economic activity and worker count: the complete operative 2026 floor matrix (44 values; jornada = mensual÷30 and hora = jornada÷8 verified on every cell); NO zonas-libres and NO promedio row in the gazette (both only in the DGS print) | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Art. 2 (p.4) (EV82:EVID-223) |
| LB-010 | Acuerdo SETRASS-233-2026, Art. 2 (tabla 2027) | Header: "TABLA DE SALARIO MÍNIMO, VIGENTE A PARTIR DEL 01 DE ENERO DEL AÑO 2027" [OCR-only print; e.g. manufacturera 151+: 20,195.35 / 673.18 / [gap]; agricultura 11-50 and financieros 11-50 rows plus 15 jornada/hora cells + 2 full rows (V-HN1 exact recount) unreadable in both layers — 90_ OQ-3] | The 2027 floors published a year ahead in the same bienio; every readable mensual cell = 2026 value × band % (6/6/7/7.5) exactly; unreadable cells remain reconstruction-blocked, never silently filled | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Art. 2 (p.5) (EV82:EVID-224) |
| LB-011 | Acuerdo SETRASS-233-2026, Art. 3 | "Que, para el sector agroindustrial el salario mínimo se clasificará conforme a la 'categoría agricultura, silvicultura, caza y pesca', entendiéndose por agroindustrias las empresas que incluyen producción en campo y transformación industrial de materias primas agrícolas. Se determina aclarar que, para el caso particular de las empresas agroindustriales dedicadas a la producción de bienes alimentarios y materias primas de origen agrícola, se pagará el nivel de salario mínimo de manufactura a los trabajadores del área industrial y el nivel de agricultura, ganadería, silvicultura, caza y pesca a los trabajadores de áreas agrícolas." | Agroindustrial companies classify under the agricultura category by default; food and agricultural-raw-material producers pay a SPLIT floor — manufactura level to industrial-area workers, agricultura level to field workers | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Art. 3 (p.6) (EV82:EVID-225) |
| LB-012 | Acuerdo SETRASS-233-2026, Art. 4 | "Que el ajuste antes acordado correspondiente a los meses de enero, febrero, marzo y abril del año 2026, será pagado en forma diferida a más tardar el 31 de julio del presente año. Asimismo, en lo que respecta a los trabajos temporales, se les garantiza el referido pago retroactivo en las mismas condiciones." | The Jan-Apr 2026 adjustment is payable deferred at the latest by 31-jul-2026; temporary workers are guaranteed the same retroactive payment under the same conditions | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Art. 4 (p.6) (EV82:EVID-226) |
| LB-013 | Acuerdo SETRASS-233-2026, Arts. 5-7 | Art. 5: "Se acuerda establecer una Cláusula de Salvaguarda que indique, que en caso que el índice de Inflación Interanual registrado al mes de diciembre de 2026 emitido por el Banco Central de Honduras (BCH), sea mayor al ajuste salarial aquí fijado para el año 2027, se deberá aplicar el ajuste salarial igual al porcentaje del índice de inflación registrado, para lo cual se deberá emitir de oficio el respectivo acuerdo… con los valores actualizados." Art. 6: DGS + Inspección vigilance "garantizando… la aplicación a todos los trabajadores del principio de igualdad de remuneración entre la mano de obra masculina y la mano de obra femenina por un trabajo de igual valor." Art. 7: "Quedan excluidos de este Acuerdo los Trabajadores del Sector Textil Maquilador Hondureño y demás Empresas de Zona Libre en virtud del Acuerdo No. SETRASS-109-2024… actualmente vigente para este rubro hasta el 31 de diciembre de 2026." | Conditional 2027 IPC escalator (de-oficio replacement rows on trigger); DGS/Inspección vigilance with the equal-remuneration guarantee; maquila/zona-libre workers excluded — they stay on the SETRASS-109-2024 track through 31-dic-2026 | `hn/sources/90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf` | 233-Arts. 5-7 (pp.6-7) (EV82:EVID-227) |
| LB-014 | DGS, Tabla de Salario Mínimo vigente 01-01-2026 (Acuerdo SETRASS-233-2026) | Ramas 1-11 identical to 233-Art. 2 (clean-amount authority); "12 ®Empresas acogidas a la Ley de Zonas Libres — De 1 en adelante — 12,930.07 / 431.00 / 53.88"; final row: "Salario Mínimo Promedio — 14,917.20 / 497.24 / 62.16". Footnotes: "⅟Acuerdo No. SETRASS-233-2026. Publicado en el Diario Oficial La Gaceta Nº 37,129… 29 de Abril del 2026." / "®Acuerdo Ejecutivo N°. SETRASS-109-2024, Publicado en el Diario Oficial La Gaceta N°.36,491 del 21 de Marzo del 2024." | Official DGS companion table: the 12-row catalog adding zonas libres (L12,930.07, sourced by footnote from SETRASS-109-2024) and the SMM promedio row (L14,917.20 / L497.24 / L62.16 — single national value, methodology unpublished, ≠ table mean, R-H47; feeds the ISR plantilla 10×SMM caps) | `hn/sources/91_Tabla_Salario_Minimo_2026-2027.pdf` | 91_ p.1 (EV82:EVID-228) |
| LB-015 | Acuerdo STSS-308-2022, Art. 1 | "…fijando el ajuste de Salario Mínimo a nivel nacional para los años 2022 y 2023 de conformidad a los porcentajes que se detallan a continuación:" Cuadro: "De 1 a 10 Trabajadores — 5.32% / 5.32%; De 11 a 50 Trabajadores — 5.50% / 5.50%; De 51 a 150 Trabajadores — 6.50% / 6.50%; De 151 Trabajadores en Adelante — 7.50% / 8.00%" | The 2022-2023 bienio percentages: 2022 = 5.32/5.50/6.50/7.50; 2023 as originally fixed = 5.32/5.50/6.50/8.00 (superseded by the 9.80% re-fix before effectivity); the 2022 amounts table is an IMAGE (values unpinned — 101_ OQ-2) | `hn/sources/101_Acuerdo_STSS-308-2022_G35892.pdf` | 308-Art. 1 (p.3); cuadro pp.3/7 (EV82:EVID-230) |
| LB-016 | Acuerdo STSS-308-2022, Art. 3 | "Aprobar la nueva Tabla de Salario Mínimo que regirá en todo el país… la cual entrará en vigencia a partir del uno (01) de enero del año dos mil veintitrés (2023), en la forma siguiente" [44 values, e.g. manufacturera 1-10: 10,462.78 / 348.76 / 43.59; p.4 caption misprints "PARA EL AÑO 2022" — R-H64] | The 2023 table AS ORIGINALLY FIXED — superseded by 014-2023's uniform 9.80% before taking effect (loaded as dated history that never governed) | `hn/sources/101_Acuerdo_STSS-308-2022_G35892.pdf` | 308-Art. 3 (pp.4-5; duplicated pp.8-9) (EV82:EVID-231) |
| LB-017 | Acuerdo STSS-308-2022, Arts. 4, 5 y 7 | Art. 4: "Que el ajuste antes acordado correspondiente a los meses de enero, febrero y marzo del año 2022, será pagado en forma diferida en los meses de abril, mayo y junio de este año." Art. 5: "En caso que el índice de inflación interanual registrado al mes de diciembre de 2022, emitido por el Banco Central de Honduras, sea mayor al ajuste aquí fijado para el año 2023, se deberá aplicar un ajuste igual al porcentaje de inflación registrado…" Art. 7: "Quedan excluidos de este Acuerdo los Trabajadores del Sector Textil Maquilador Hondureño y demás Empresas de Zona Libre en virtud del Acuerdo vigente suscrito en fecha trece (13) de diciembre del año dos mil dieciocho (2018)." | Jan-Mar 2022 differentials deferred across Apr/May/Jun 2022 (installment pattern); the dic-2022 salvaguarda trigger later executed as 014-2023's uniform 9.80%; maquila/zona-libre exclusion per the 13-dic-2018 acuerdo (STSS-006-2019's underlying instrument — acquisition lead) | `hn/sources/101_Acuerdo_STSS-308-2022_G35892.pdf` | 308-Arts. 4-8 (p.6) (EV82:EVID-232) |
| LB-018 | Acuerdo SETRASS-109-2024, Arts. 1-2 | Art. 1: "Aprobar el Ajuste al Salario Mínimo por el período dos (02) años, mismos que entrará en vigencia a partir del primero 01 de enero del año 2024 hasta el 31 de diciembre del año 2025 respectivamente…" [percentage cuadro subset-font mojibake; both years pinned at 5.5/5.5/6.5/7.0 via the 233-CONS.(7) quote + exact arithmetic — R-H46, 82_ OQ-1]. Art. 2 + "AÑO 2025" table: 44 values (41 clean + damaged cells in comunales/hospitales 1-10 and 51-150), e.g. manufacturera 1-10: 12,140.69 / 404.69 / 50.59; NO promedio and NO zonas-libres row | The 2024-2025 bienio (percentages pinned from outside the damaged print; 2024 amounts not printed at all — config gap) and the operative 2025 table, the arithmetic base of the 2026 table | `hn/sources/82_SETRASS-109-2024_salario_min_2024-2025.pdf` | 109-Arts. 1-2 (pp.1-4) (EV82:EVID-233; EV82:EVID-234) |
| LB-019 | Acuerdo SETRASS-109-2024, Arts. 3-7 | Art. 5: "Aprobar el ajuste al Salario Mínimo por un período de tres (03) años para el Sector Textil Maquilador y demás empresas que operan en Zonas Libres… Del 01 de enero al 31 de diciembre del 2024 — 6.5%; …2025 — 7.5%; …2026 — 8%." Art. 6: "El ajuste antes acordado… correspondientes a los meses de enero y febrero del año 2024, deberá ser pagado en forma diferida a más tardar el 30 [de abril del presente año]." Art. 7 (maquila salvaguarda): "…se aplicará de forma automática como incremento o reajuste salarial el porcentaje pactado más el diferencial del porcentaje interanual de inflación… La Secretaría de Trabajo y Seguridad Social (SETRASS), deberá emitir de oficio, el respectivo Acuerdo… a más tardar el 15 de enero del año que se trate." Art. 3: agroindustrial rule (same text as 233-Art. 3) | The maquila 3-year track 2024-2026 (6.5/7.5/8% over the L10,457.29 base → L12,930.07 in 2026, exact — R-H48); Jan-Feb 2024 retro by 30-abr-2024; the maquila DIFFERENTIAL escalator (automatic, de-oficio by 15-ene); the agroindustrial split rule | `hn/sources/82_SETRASS-109-2024_salario_min_2024-2025.pdf` | 109-Arts. 3-7 (pp.3-4) (EV82:EVID-235) |
| LB-020 | Acuerdo SETRASS-014-2023, CONSIDERANDO + Arts. 1-2, 4 y 6 | CONSIDERANDO: "…la inflación oficial interanual registrada por el Banco Central de Honduras (BCH) al mes de diciembre del año dos mil veintidós (2022), alcanzó el porcentaje de 9.80%, siendo superior a los porcentajes de ajuste acordados para el año dos mil veintitrés (2023), de 5.32%… 5.50%… 6.50%… y de 8.00%… plasmados en el Acuerdo Ejecutivo No. STSS 308-2022…" Art. 1 cuadro: 9.80% for every category. Art. 2: new table "…entrará en vigencia a partir del (01) de enero del año dos mil veintitrés (2023)…" [table OCR-damaged — 83_ OQ-1]. Art. 4: "…correspondiente al mes de enero de 2023, podrá ser pagado de forma total o de manera diferida a más tardar el 31 de marzo de 2023." Art. 6: maquila/zonas libres excluded | The salvaguarda EXECUTED: 2023 re-fixed at a UNIFORM national 9.80% over the 2022 values, replacing the 5.32/5.50/6.50/8.00 column; January 2023 differential payable total-or-deferred by 31-mar-2023; maquila excluded | `hn/sources/83_SETRASS-014-2023_salario_min_2023.pdf` | 014-CONSIDERANDO (p.1); Arts. 1-2 (p.2); Arts. 4, 6-7 (p.3) (EV82:EVID-236) |
| LB-021 | Acuerdo SETRASS-411-2023, Arts. 1-3 + Acta Especial | Art. 1 cuadro: "[AÑO] 2023 — [ajuste] 10.00% — [período] Junio-diciembre" + "2023 Junio-Diciembre — Salario mínimo mensual L 10,457.29 — Salario Mínimo Jornada ordinaria de 8 Horas laborales L 348.58 — Salario mínimo por hora L 43.57". Art. 3: "…correspondiente al mes de junio de 2023, deberá ser pagado de forma retroactiva y total a más tardar el 31 de agosto de 2023." Acta: "MODIFICAR la Cláusula Novena del Acuerdo Ejecutivo No. STSS-006-2019… en lo que respecta al porcentaje de ajuste al salario mínimo del sector textil maquilador y demás empresas que operan en zonas libres, aplicable para el año 2023, el cual deberá leerse de la siguiente manera: 2023 — 10.00% — Junio-diciembre." | The maquila mid-year 2023 event: 10% for Jun-Dic 2023, new floor L10,457.29 (single national value, no size bands); June differential retroactive and total by 31-ago-2023; modifies STSS-006-2019 Cláusula Novena (whose original 8% governed Jan-May 2023 — value unprinted, ≈9,506.63 derived only, 84_ OQ-1) | `hn/sources/84_SETRASS-411-2023_textil_2023.pdf` | 411-Arts. 1-3 (pp.2-3); Acta pp.3-7 (EV82:EVID-237) |
| LB-022 | Acuerdo 345 (Reglamento de las Comisiones de Salario Mínimo, `108_`, W5; 6-oct-1988, G 25,680 — publication date not printed, vigencia = day after publication, unpinned) Arts. 2/3/6/15/28/29/30: Art. 2: "Las Comisiones… son los organismos tripartitos creados temporalmente para coadyuvar a la fijación y revisión periódica de las tasas salariales mínimas…" Art. 3: "…integradas en forma tripartita, así: Tres miembros propietarios representantes del interés patronal, tres… del interés obrero y tres… del interés público… Finalizada la Fijación o Revisión para las cuales han sido integradas… se considerarán disueltas." Art. 6: "El Director General de Salarios es por ministerio de la ley el tercer miembro por el sector público, y actuará como Presidente." Art. 15: "La audiencia durará en su conjunto (15) quince días hábiles…" Art. 28: "…la publicación del proyecto por una sola vez en el periódico Oficial 'La Gaceta', juntamente con un aviso en que les concederá a Partes Interesadas un término fatal de (20) veinte días…" Art. 30: "El Secretario de Trabajo y Previsión Social, tendrá un término de (20) veinte días hábiles para pronunciarse… El Acuerdo del Poder Ejecutivo será publicado en el periódico Oficial 'La Gaceta' por una sola vez, y entrará en vigencia (15) quince días después de tal publicación." | The commissions PROCEDURE reglamento (1988): commissions are TEMPORARY — constituted per fijación/revisión and dissolved on completion (each bienio/annual acuerdo rides its own commission; ties the SETRASS-101-2026 naming evidence); Director General de Salarios chairs ex-ley; audiencia 15 días hábiles, quorum 5 incl. the President; project published ONCE in La Gaceta with a 20-day FATAL comment window; informe ≥5 votes; Secretario 20 días hábiles (silence = approval); the fijación's effectivity = 15 days after its gazette publication — REGLAMENTO-level restatement of the Ley Art. 30 default already in LB-002, displaced by the fijación instruments' own vigencia clauses (R-H62). | `hn/sources/108_Acuerdo_345_Regl_Comisiones_Salario_Minimo.pdf` | 345-Arts. 2-3/6 (pp.1-2), 14-15 (pp.4-5), 28-30 (pp.6-7), 34 (p.8) (EV106:EVID-383; EV106:EVID-384) |
| LB-023 | **THE DGS PROMEDIO-PRINT FAMILY + SAR ANCHORS ACQUIRED W10** (`156_` Tabla SMM 2022 + `157_` Tablas 2023 SMP y BE + `158_` Tabla SMM 2024 + `159_` G 37,077 SAR-43-2026 + `160_` G 36,499 SAR-125-2024): the promedio rows now printed/anchored for 2022-2025 — **2022 L11,278.75/375.96/46.99** (156_ line "Salario Minimo Promedio 11,278.75 375.96 46.99", fixer unfootnoted = lead); **2023 L12,377.73/412.59/51.57** (157_; jornada triple-pass 412.59 — sidecar "4127.59" noise adjudicated 600dpi; TWO-PRINT validation: SAR-125-2024 recites SETRASS-411-2023 "fijó el salario mínimo promedio … a partir del 01 de enero del 2023 … (L12,377.73)"; governance datum: the promedio-fixing power attaches to SETRASS/DGS oficios-acuerdos as a family, not the general re-fix acuerdos); **2024 L13,156.53/438.55/54.82** (158_, native-layer corroborated); **2025 L13,985.16** (SAR-43-2026, G 37,077 23-feb-2026 — CT-131 descargo umbral "vigente y aprobado a la fecha de emisión"; fixer = SETRASS-109-2024 + Oficio SETRASS-DGS-014-2025 [lead]; NO DGS 2025 print — the DGS-print watch carries). The descargo anchors' emission-coherence: Feb-2024 SAR-125 used the 2023 promedio (the 2024-2025 bienio published only 21-mar-2024) and Feb-2026 SAR-43 used the 2025 promedio (the 2026-2027 bienio published only 29-abr-2026) — the vigente-at-emission semantics demonstrated twice (D-H2) | FR-024/FR-025's promedio supply now 5-of-6 years printed/anchored (only 2027 pending); the ×10 cap derivations FY2022-FY2025 unblocked for taxation/04 FR-134; three promedio resolution semantics separated (FY-cap / emission-time umbral / hecho-generador-time sanctions) | `hn/sources/156_Tabla_Salario_Minimo_2022_DGS.pdf` + `hn/sources/157_Tabla_Salario_Minimo_2023_DGS_SMP.pdf` + `hn/sources/158_Tabla_Salario_Minimo_2024_DGS.pdf` + `hn/sources/159_Gaceta_37077_Acuerdo_SAR-43-2026_descargo_cta_cte.pdf` + `hn/sources/160_Gaceta_36499_Acuerdo_SAR-125-2024_descargo_cta_cte.pdf` | EV156:EVID-622..625; EV157:EVID-626..629; EV158:EVID-630..633; EV159:EVID-634..638; EV160:EVID-639..643 |

## 3. Functional Requirements

### 3.1 Statutory floor machinery (Ley D. 103)

- **HN-PAYR-FR-001:** The system shall enforce the SMM as a public-order,
  *irrenunciable* (non-waivable) hard floor: no wage rate below the
  applicable dated SMM row (FR-009/FR-010 resolution) may be saved on
  contracts or paid on payslips — below-floor values are blocked at
  validation, not merely warned. (LB-001; EV82:EVID-215)
- **HN-PAYR-FR-002:** The system shall auto-elevate inferior stipulations:
  any individual or collective contract, pact or agreement that pays below
  the floor or diminishes it is treated as satisfied at the floor value and
  is never stored as a valid lower wage; the floor VALUES are supplied here
  while the CT chassis (CT Arts. 381-390) and contract machinery are owned by
  file 10 (salario/records, HN-PAYR-FR-371..405) — cited by article, no
  re-derivation. (LB-001; EV82:EVID-215)
- **HN-PAYR-FR-003:** The system shall apply the piece-rate sufficiency test
  (Art. 20): whatever the pay modality — *jornada* (time), unit of *obra*
  (piece/work), *destajo* (task-rate) or any other — the computed EFFECTIVE
  earnings of a *trabajador de mediano rendimiento* (average-yield worker)
  must reach at least the SMM fixed for the activity; the floor check runs on
  computed effective earnings, never merely on the stated contracted rate.
  (LB-003; EV82:EVID-217)
- **HN-PAYR-FR-041:** (W5, reserved range — Acuerdo 345, `108_`) The system
  shall carry the fijación-process metadata as provenance rows on every SMM
  print (no computation engine): the commissions are TEMPORARY tripartite
  bodies (3 patronal + 3 obrero + 3 público, Director General de Salarios
  presiding ex-ley), constituted per fijación/revisión and dissolved on
  completion; the procedure = 15-días-hábiles audiencia → project published
  ONCE in La Gaceta with a 20-day fatal comment window → informe ≥5 votes →
  Secretario 20 días hábiles (silence = approval); and the effectivity
  DEFAULT = 15 days after the fijación's gazette publication (reglamento
  Art. 30 restating Ley Art. 30, LB-002) — displaced by any fijación
  instrument's OWN vigencia clause (R-H62; e.g. the bienios' 1-jan
  effectivity + retroactivity rows). Acuerdo 345's own vigencia date is
  unpinned (G 25,680 publication date not printed — `108_ OQ-1`, procedural
  instrument, no data impact).
  (LB-022; EV106:EVID-383; EV106:EVID-384)
- **HN-PAYR-FR-004:** The system shall permit *salarios móviles* (mobile
  salaries indexed to the product price, by biweekly/monthly averages or
  other means) but never below the fixed basic SMM of the industry — the
  mobile scheme's outputs remain floored by the same dated rows. (LB-004;
  EV82:EVID-217)
- **HN-PAYR-FR-005:** The system shall never key an SMM lookup on age or sex
  (Art. 25.d) and shall carry the equal-remuneration guarantee — equal pay
  between male and female labor for work of equal value (233-Art. 6) — as a
  non-differentiation invariant on every SMM resolution surface. (LB-005;
  LB-013; EV82:EVID-217; EV82:EVID-227)
- **HN-PAYR-FR-006:** The system shall carry SMM applicability flags per
  worker: EXEMPT classes — public servants in constitutionally/legally
  created posts, *gerentes, administradores y profesionales* (managers,
  administrators, professionals), and domestic workers in private residences
  (special regime, outside this chassis); OUTSIDE the floor — *aprendices*
  (apprentices; wage set by the unpublished Ley-SMM Reglamento, OQ-013) and
  DGS-certified *incapaces* (Art. 32 permits as dated rows carrying the
  %-of-SMM and validity period); NO small-employer SMM exemption exists —
  the ≤15-permanent-workers exemption belongs to the bono educativo only
  (file 02), and the 1-10 band is simply the lowest SMM band. (LB-006;
  EV82:EVID-220)
- **HN-PAYR-FR-007:** The system shall carry the rama catalog as
  configuration instantiating Art. 47's "industria = any field of economic
  activity": the 11 ramas stable 2022-2027 (catalog keys, §4) plus row 12
  zonas libres (DGS prints only); the catalog is open-ended — the law
  enumerates, instruments instantiate, and no rama is ever removed from
  history. (LB-006; LB-014; EV82:EVID-220; EV82:EVID-228)
- **HN-PAYR-FR-008:** The system shall encode the institutional chain
  (tripartite Comisión → SETRASS approval → gazette → vigencia) as OUTCOME
  provenance metadata on every dated row — instrument number, gazette
  number/date, signature date and vigencia-clause text — never as procedure
  (localization posture: the dated DATA are the requirement, not the
  government workflow). (LB-002; EV82:EVID-216)

### 3.2 Dated-row chassis: loading, resolution, print discipline

- **HN-PAYR-FR-009:** The system shall load all SMM values as DATED rows
  seeded from the `smm_tables.csv` sidecar — one row per track × rama × band
  × validity window, with `valid_from`/`valid_to`, the three printed
  denominations (mensual / jornada / hora), the `pct_adjust` bienio metadata
  and the `print_status` provenance flag — additive-only, never replaced in
  place (D-H2); unprinted cells are EMPTY in the CSV and are never filled at
  load or run time. (LB-009; LB-010; LB-014; EV82:EVID-223/224/228)
- **HN-PAYR-FR-010:** The system shall resolve the applicable SMM row by the
  D-H2 payroll resolution key — (payslip period, track, rama, band, worker
  attributes incl. the agro area of FR-014) — with the resolution date = the
  payslip period / *hecho generador* (triggering event), NEVER "today"; paid
  slips are frozen, corrections recompute with ORIGINAL-period rows, and the
  band = the employer's permanent-worker count category resolved as of that
  period. (LB-009; EV82:EVID-223; D-H2)
- **HN-PAYR-FR-011:** The system shall apply the print-faithful / never-guess
  discipline: SMM amounts load ONLY where printed in the corpus; unpinned
  vintages and cells — the 2022 and 2024 general-track amounts, the
  effective-2023 table, maquila Jan-May 2023 and maquila 2024/2025, the
  missing promedio years — are machine-visible config-gap rows
  (`derived_gap` / `reconstruction_blocked`) that BLOCK dependent lookups;
  the system shall never derive amounts as prior-value ×(1+pct), never
  average, never hardcode (D-H2 never-guess rule; 101_ OQ-2; 82_ OQ-1).
  (LB-015; LB-018; EV82:EVID-230; EV82:EVID-233/234)
- **HN-PAYR-FR-012:** The system shall encode the structural relation
  jornada = mensual ÷ 30 and hora = jornada ÷ 8 as a VALIDATION rule over
  printed cells — it reproduces the evidence-verified spot-check cells
  exactly (e.g. 9,596.64 ÷ 30 = 319.89; 319.89 ÷ 8 = 39.99; 19,919.96 ÷ 30 =
  664.00; 664.00 ÷ 8 = 83.00 = printed) and holds on all other printed cells
  within a ±L0.01 rounding-mode tolerance (isolated cent-level deviations —
  e.g. 2025 electricidad 11-50 hora prints 54.85 vs 54.89 computed — are
  FLAGGED as print anomalies, never auto-corrected) — and shall NEVER use
  the rule to fill unprinted cells: the 2027 OCR gaps and 2025 damaged
  cells stay blocked (90_ OQ-3; EVID-234 damage notes). (LB-009; LB-010;
  EV82:EVID-223; EV82:EVID-224; EV82:EVID-234)
- **HN-PAYR-FR-013:** The system shall key the band dimension on the
  employer-size categories *De 1 a 10 / De 11 a 50 / De 51 a 150 / De 151 en
  adelante* (permanent workers) for the general track; the maquila/zonas-libres
  track and the promedio carry a SINGLE national value with band = na (no
  size or rama differentiation). (LB-009; LB-014; LB-021; EV82:EVID-223;
  EV82:EVID-228; EV82:EVID-237)
- **HN-PAYR-FR-014:** The system shall implement the agroindustrial
  classification rule (Art. 3, identical text in 109-2024 and 233-2026):
  *agroindustrias* (field production + industrial transformation of
  agricultural raw materials) classify by default under the agricultura
  category; food and agricultural-raw-material producers pay a SPLIT floor —
  manufactura-level SMM to industrial-area workers and agricultura-level to
  field workers — so the lookup key is the WORKER's area classification, not
  only the company rama (014-2023's print skips its Art. 3 — applicability
  for 2023 carried as OQ-010). (LB-011; LB-019; EV82:EVID-225;
  EV82:EVID-235; EV82:EVID-236)
- **HN-PAYR-FR-015:** The system shall seed the 2026 general vintage (11
  ramas × 4 bands, valid 2026-01-01→2026-12-31, pct 6/6/7/7) print-faithful
  from 233-Art. 2, with the DGS 91_ print as clean-amount authority for the
  gazette OCR gaps (cells completed from 91_ flagged per-row in the CSV; the
  90_ OCR misread 18,444.80 corrected by 91_ + exact arithmetic); the gazette
  carries NO zonas-libres and NO promedio row — both exist only in the DGS
  print. (LB-009; LB-014; EV82:EVID-223; EV82:EVID-228)
- **HN-PAYR-FR-016:** The system shall seed the 2027 vintage (valid
  2027-01-01→2027-12-31, pct 6/6/7/7.5 — R-H45) with ONLY the cells readable
  in the gazette print (this table exists in no other corpus file): the
  agricultura 11-50 and financieros 11-50 rows (all three cells each), ~13
  jornada/hora cells and the restaurantes 1-10 digit-uncertainty load EMPTY
  as `reconstruction_blocked` rows/cells pending visual confirmation of the
  gazette or a clean DGS 2027 print (90_ OQ-3) — the arithmetic
  reconstruction candidates remain evidence metadata, never loaded silently.
  (LB-010; EV82:EVID-224)
- **HN-PAYR-FR-017:** The system shall seed the 2025 vintage (valid
  2025-01-01→2025-12-31, pct 5.5/5.5/6.5/7.0) print-faithful from 109-Art. 2,
  with the damaged cells — the comunales and hospitales 1-10 and 51-150 rows
  of the spaced-font print — loaded EMPTY as `reconstruction_blocked`, their
  arithmetic reconstruction candidates remaining evidence metadata only.
  (LB-018; EV82:EVID-234)
- **HN-PAYR-FR-018:** The system shall keep BOTH 2023 vintages: (a) the
  308-Art. 3 originally-fixed table (pct 5.32/5.50/6.50/8.00) loaded
  print-faithful as SUPERSEDED history that never governed — superseded by
  014-2023 before its 1-ene-2023 effectivity; (b) the effective 014-2023
  uniform-9.80% vintage (pct 9.80, every band) whose Art. 2 amount table is
  OCR-damaged (83_ OQ-1) — effective-2023 amount lookups are therefore
  BLOCKED (double dependency: damaged print + unpinned 2022 base; two cells
  chain-verified only). (LB-016; LB-020; EV82:EVID-231; EV82:EVID-236)
- **HN-PAYR-FR-019:** The system shall record the 2022 and 2024 bienio
  PERCENTAGES as pinned metadata — 2022: 5.32/5.50/6.50/7.50 (clean print);
  2024 and 2025: 5.5/5.5/6.5/7.0 both years (R-H46: pinned via the
  233-CONS.(7) verbatim quote of the 2024 column + exact arithmetic chains,
  the 82_ cuadro itself being mojibake) — while the 2022 and 2024 AMOUNTS
  remain config gaps (the 101_ 2022 table is an image; 82_ prints only the
  2025 table), blocking those years' SMM amount lookups. (LB-015; LB-018;
  LB-008; EV82:EVID-230; EV82:EVID-233/234; R-H46)
- **HN-PAYR-FR-020:** The system shall implement supersession additively:
  when an instrument replaces values (salvaguarda re-fix, de-oficio acuerdo,
  new bienio), NEW rows are added with supersession links and superseded rows
  are retained for audit and original-period recomputation — the 308-Art. 3 →
  014-2023 pair is the precedent; no dated row is ever edited or deleted
  (D-H2). (LB-016; LB-020; EV82:EVID-231; EV82:EVID-236)

### 3.3 Maquila / zonas-libres separate track (R-H48)

- **HN-PAYR-FR-021:** The system shall run the *Sector Textil Maquilador
  Hondureño* and demás *Empresas de Zona Libre* on a SEPARATE track
  (track=maquila; `zonas_libres` is a reserved alias value for a future
  instrument split — every corpus instrument treats both populations as one):
  excluded from every general bienio (308-Art. 7 per the 13-dic-2018 acuerdo;
  014-Art. 6; 233-Art. 7 extending SETRASS-109-2024 coverage to 31-dic-2026),
  single national value, no size bands. (LB-013; LB-017; LB-020; LB-021;
  EV82:EVID-227; EV82:EVID-232; EV82:EVID-236; EV82:EVID-237)
- **HN-PAYR-FR-022:** The system shall seed the maquila dated rows: Jun-Dic
  2023 = L10,457.29 / 348.58 / 43.57 printed (10%, mid-year split — the
  canonical D-H2 period-dated case); the 2024-2026 chain 6.5% / 7.5% / 8%
  (R-H48: 10,457.29 × 1.065 × 1.075 × 1.08 = 12,930.07 exact, closing on
  the 91_ row-12 print for 2026 = 12,930.07 / 431.00 / 53.88); Jan-May 2023
  (≈9,506.63 derived; original STSS-006-2019 Cláusula Novena 8% unprinted)
  and the 2024/2025 amounts (11,137.01 / 11,972.29 derived) = blocked
  config-gap rows, never loaded (84_ OQ-1; 82_ OQ-2); NO 2027 maquila
  instrument exists in the corpus (109-2024 coverage ends 31-dic-2026) →
  2027 maquila lookups blocked with an open-lead flag (OQ-014). (LB-021;
  LB-019; LB-014; EV82:EVID-237; EV82:EVID-235; EV82:EVID-228)
- **HN-PAYR-FR-023:** The system shall encode the maquila DIFFERENTIAL
  salvaguarda (109-Art. 7): if the BCH dic interanual IPC of a pactado year
  exceeds the pactado increase for the following year, the adjustment = the
  pactado percentage PLUS the inflation differential, applied automatically,
  with a de-oficio SETRASS acuerdo due by 15-ene — conditional config
  distinct from the general clause (FR-029); rows change only when the
  instrument arrives, never by formula. (LB-019; EV82:EVID-235)

### 3.4 The promedio supply (R-H47)

- **HN-PAYR-FR-024:** The system shall supply the *salario mínimo promedio*
  as first-class dated rows (track=promedio, single national value, band=na)
  printed ONLY in the DGS companion tables (R-H47) **or official-instrument
  anchors (W10 addition, LB-023): 2022 = L11,278.75 / L375.96 / L46.99
  (156_, DGS print; EVID-623); 2023 = L12,377.73 / L412.59 / L51.57 (157_,
  DGS print, jornada cell triple-pass-pinned, EVID-626 — TWO-PRINT
  validation with SAR-125-2024's recital: "SETRASS-411-2023 … fijó el
  salario mínimo promedio … a partir del 01 de enero del 2023 …
  (L12,377.73)", EVID-640); 2024 = L13,156.53 / L438.55 / L54.82 (158_,
  DGS print, EVID-630); 2025 = L13,985.16 (SAR-43-2026 official-instrument
  anchor — `printed_anchor` status, NOT a DGS print; fixer = SETRASS-109-2024
  + Oficio SETRASS-DGS-014-2025, lead; EVID-634/635); 2026 = L14,917.20 /
  L497.24 / L62.16 (91_, EVID-228)** — this supply is THE feed consumed by
  the ISR plantilla 13th/14th-month 10×SMM-promedio caps — HN-TAX-FR-134
  (taxation/04) — and the 10× derivations (FY2022 L112,787.50 / FY2023
  L123,777.30 / FY2024 L131,565.30 / FY2025 L139,851.60 / FY2026
  L149,172.00) belong to that consumer, NOT to this file.
  (LB-014; LB-023; EV82:EVID-228; EV156:EVID-623; EV157:EVID-626;
  EV158:EVID-630; EV159:EVID-634; R-H47)
- **HN-PAYR-FR-025:** The system shall enforce never-recompute on the
  promedio (R-H47): the value is a DGS print figure (or SAR-oficio anchor,
  2025) with unpublished methodology, NOT the table mean — disproven means
  on record: 2026 44-value mean L15,097.85, 45-value mean incl. zonas
  libres L15,049.68, 2025 44-value mean L14,177.03 vs the anchored
  L13,985.16 — so any recomputation or averaging logic is rejected; the
  only remaining missing vintage is 2027 (machine-visible config-gap row +
  DGS-print acquisition watch, 90_ OQ-4: the FY2027 cap input stays blocked
  until the DGS 2027 table issues, expected early 2027). NOTE the three
  promedio RESOLUTION semantics that exist in corpus (encode as three
  distinct consumers, never conflated): (i) FY-cap family (taxation/04
  FR-134 — the FY's own promedio); (ii) CT-131 descargo umbral
  (SAR-125-2024/SAR-43-2026 — the promedio "vigente a la fecha de
  emisión", i.e., the PREVIOUS year's during Jan-Apr bienio gaps);
  (iii) the D. 92-2015 reformed-Art.-7 sanctions measure ("vigente en la
  fecha en que se origina el incumplimiento" — hecho-generador time;
  FREP/11 LB-013). (LB-014; LB-023; EV82:EVID-228; EV82:EVID-234;
  EV159:EVID-638; EV160:EVID-640; EV149:EVID-570)
- **HN-PAYR-FR-026:** The system shall flag the 2025 promedio row as
  cited-not-printed: SAR-43-2026 cites L13,985.16 (carried as a provenance
  note on the row) but the value is printed nowhere in the corpus — the row
  stays a config gap and loads ONLY from a DGS 2025 print; SAR's May-2026
  "promedio vigente" post is transitional communication, not a legal source.
  (LB-018; LB-014; EV82:EVID-234; EV82:EVID-228)

### 3.5 Bienio mechanics: retro deadlines, salvaguarda, cadence, print defects

- **HN-PAYR-FR-027:** The system shall encode retro-payment obligations as
  per-instrument DATED obligation rows, each with its own payment-mode
  semantics: 2022 Jan-Mar → deferred in April/May/June 2022 installments
  (308-4); 2023 Jan → total or deferred by 31-mar-2023, employer option
  (014-4); 2023 maquila Jun → retroactive and total by 31-ago-2023 (411-3);
  2024 Jan-Feb → deferred by 30-abr-2024 (109-6); 2026 Jan-Apr → deferred by
  31-jul-2026, temporary workers explicitly included (233-4). (LB-012;
  LB-017; LB-019; LB-020; LB-021; EV82:EVID-226; EV82:EVID-232;
  EV82:EVID-235; EV82:EVID-236; EV82:EVID-237)
- **HN-PAYR-FR-028:** The system shall compute retro differentials as
  FORWARD payments: recompute the affected months at the new floor rows and
  pay the difference within the instrument's deadline run — never mutate
  paid slips backdated (D-H2/D16: the differential is a new posting
  referencing the original periods; original-period rows govern the
  recompute). (LB-012; EV82:EVID-226)
- **HN-PAYR-FR-029:** The system shall encode the PENDING conditional 2027
  escalator (233-Art. 5): IF the BCH interanual IPC registered at dic-2026
  exceeds the fixed 2027 adjustment (6/6/7/7.5 per band) THEN the 2027
  adjustment becomes the inflation percentage via a de-oficio SETRASS
  acuerdo with updated values — modeled as conditional dated config whose
  THEN-branch fires ONLY on instrument arrival (never auto-derived IPC
  rows); precedent: the identical 308-Art. 5 clause was executed as
  014-2023's uniform 9.80%. (LB-013; LB-020; EV82:EVID-227; EV82:EVID-236)
- **HN-PAYR-FR-030:** The system shall record the Art. 35 statutory cadence
  — December review → January vigencia keyed to accumulated inflation to
  November; extraordinary June review (July vigencia) only if
  first-semester inflation > 12% — as revision-event metadata, with R-H62
  encoded: the bienios' own vigencia clauses control (multi-year fixes since
  2019 deviate from the annual cadence; no instrument cites Art. 35 —
  doctrinal gap carried as OQ-002, resolved as a ruling). (LB-007;
  EV82:EVID-219; R-H62)
- **HN-PAYR-FR-031:** The system shall carry the bienio percentage chains
  as `pct_adjust` metadata on every row — 2022: 5.32/5.50/6.50/7.50; 2023:
  9.80 uniform (effective) over 5.32/5.50/6.50/8.00 (superseded); 2024-2025:
  5.5/5.5/6.5/7.0 (R-H46); 2026: 6/6/7/7 and 2027: 6/6/7/7.5 (R-H45);
  maquila: 8 (Jan-May 2023) / 10 (Jun-Dic 2023) / 6.5 / 7.5 / 8 (2024-2026)
  — audit metadata ONLY, never a computation source; the 233-Art. 1 cuadro
  is garbled in both layers and triple-pinned (native fragments + OCR +
  exact arithmetic — 90_ OQ-1: visually confirm the gazette original once,
  on load). (LB-008; LB-015; LB-018; LB-020; LB-021; EV82:EVID-222;
  EV82:EVID-230; EV82:EVID-233; EV82:EVID-236; EV82:EVID-237)
- **HN-PAYR-FR-032:** The system shall record R-H63 as a legal note with no
  operative surface: 233-CONS.(7)'s comparison — dic-2025 IPC 4.98% "siendo
  superior" to the 2024 adjustments 5.5/5.5/6.5/7.0 — is false for every
  band; a drafting defect; nothing is built on the comparison and the
  negotiated percentages of Arts. 1-2 govern regardless. (LB-008;
  EV82:EVID-221; R-H63)
- **HN-PAYR-FR-033:** The system shall record R-H43 as provenance: the
  D. 43-97 reform footnotes' year "1977 [sic]" in the 104_ compilation print
  is a print defect — the correct date is 28-abr-1997 (gazette 28,271 of
  29-may-1997; the 92_ footnote supplies the correct year); all citations
  and provenance rows read D. 43-97 (1997). (LB-007; EV82:EVID-219; R-H43)
- **HN-PAYR-FR-034:** The system shall record R-H64 as a caption rule: the
  101_ p.4 caption "TABLA … PARA EL AÑO 2022" on the Art. 3 2023-values
  table is a gazette print error — column headers and the Art. 3 text
  control; CSV rows are keyed by effective date and instrument, never by
  page captions. (LB-016; EV82:EVID-231; R-H64)

### 3.6 Consumer interfaces and guardrails

- **HN-PAYR-FR-035:** The system shall supply — by id, no re-derivation —
  the SMM dated rows consumed by file 02 (13th/14th-month/bono,
  HN-PAYR-FR-051..087): the *aguinaldo* (13th-month bonus) / *décimo cuarto
  mes* (14th-month salary) computation bases, the bono educativo's ≤ 2×SMM
  eligibility ceiling, and the Acuerdo 02-95 Art. 6 small-employer variant
  (*pequeña y mediana industria, artesanías, agricultura y ganadería en
  pequeña escala* — the 14th-month base = average of the SALARIOS MÍNIMOS
  received, i.e. these dated rows); the bono TABLE (92_) is file 02's P4 —
  only the SMM rows are supplied here. (LB-009; LB-014; EV82:EVID-223;
  EV82:EVID-228)
- **HN-PAYR-FR-036:** The system shall expose one pointer for the multa-unit
  interface: CT sanction tables denominated in SMM units ("SMM promedio" /
  highest-category SMM — EV81:EVID-261) consume this file's promedio/general
  rows by id; sanction computation and procedure are owned by the CT/T11
  surfaces — nothing in this file computes multas (the D. 103 Art. 40
  L100-L1,000 + 50%-recargo fine is recorded as legal-note metadata only).
  (LB-014; LB-006; EV82:EVID-228; EV82:EVID-220; EV81:EVID-261)
- **HN-PAYR-FR-037:** The system shall treat the `smm_tables.csv` rows as
  the SINGLE source for every SMM-dependent computation across the payroll
  wave — IHSS cotizaciones (file 03, HN-PAYR-FR-101..135), IHSS incapacidad
  (file 04, HN-PAYR-FR-141..170), RAP/fondo (file 05, HN-PAYR-FR-181..215),
  vacaciones (file 07, HN-PAYR-FR-261..280), cesantía/preaviso (file 08,
  HN-PAYR-FR-291..325) and salario/records (file 10,
  HN-PAYR-FR-371..405) resolve their SMM inputs against these dated rows by
  id — no sibling re-derivation, copying or local arithmetic. (LB-009;
  LB-014; EV82:EVID-223; EV82:EVID-228)
- **HN-PAYR-FR-038:** The system shall surface every config-gap and blocked
  row as an explicit flag on the consuming run (payslip batch, cap
  computation, sibling lookup): blocked vintages, `reconstruction_blocked`
  cells, missing promedio years and the maquila 2027 gap STOP the dependent
  computation with the flag reason — never a silent default to another
  vintage, a derived value or zero. (LB-009; LB-010; EV82:EVID-223;
  EV82:EVID-224; D-H2)
- **HN-PAYR-FR-039:** The system shall implement regime cutovers as
  period-dated rows without mutation: the maquila Jun-2023 mid-year split
  (Jan-May / Jun-Dic 2023 values inside one calendar year) resolves purely
  by period; filed/payrolled periods are write-protected, and later
  instruments (de-oficio re-fixes, new bienios, salvaguarda executions) only
  ADD rows. (LB-021; LB-020; EV82:EVID-237; EV82:EVID-236; D-H2/D16)
- **HN-PAYR-FR-040:** The system shall apply the availability-gap rule to
  SMM vintages: gazettes publish months after the instruments' 1-ene
  effectivity (233-2026 signed 27-abr / gazetted 29-abr-2026 for a
  1-ene-2026 effectivity; 308-2022 gazetted 6-abr-2022) — runs for a period
  whose vintage rows are not yet loaded are BLOCKED with a missing-vintage
  flag (paralleling HN-TAX-FR-124), never defaulted to the prior-year table
  nor advanced by the announced percentages; on instrument arrival the rows
  load retroactively and the FR-027/FR-028 differential machinery
  discharges the gap. (LB-008; LB-012; EV82:EVID-221; EV82:EVID-226)

## 4. Data Model

Machine-readable sidecar next to this file: `smm_tables.csv` — the dated SMM
value rows for ALL tracks (general / maquila / promedio). One row per track ×
rama × band × validity window. CSV discipline: comma-separated, header row,
LF endings; amounts as printed (2dp, comma-thousands inside double quotes —
same convention as `../taxation/isr_brackets.csv`); an EMPTY amount cell =
not print-available (never filled); `print_status` follows the weakest-cell
rule — `printed` (all three cells print-clean somewhere in the corpus),
`reconstruction_blocked` (the only print is damaged/unreadable for at least
one cell; readable cells remain populated, damaged cells empty;
reconstruction candidates live in the evidence file, never in the CSV),
`derived_gap` (the vintage/cell is unprinted anywhere — including values
that would be arithmetically derivable, or cited-but-unprinted like the 2025
promedio — blocked pending source acquisition); `pct_adjust` = the bienio
percentage that produced the row (audit metadata per FR-031; empty for
promedio rows — DGS methodology unpublished); `source_evid` = the
EV82:EVID-nnn anchor(s); `note` = provenance/gap text. `valid_to` empty =
open-ended (no such row today: every loaded vintage is closed by the
calendar year or the next instrument). Row counts: 2022 (4 placeholder
derived_gap) + 2023-superseded (44 printed) + 2023-effective (4
reconstruction_blocked) + 2024 (4 derived_gap) + 2025 (40 printed + 4
reconstruction_blocked) + 2026 (44 printed) + 2027 (26 printed + 18
reconstruction_blocked) + maquila (2 printed + 3 derived_gap) + promedio
(1 printed + 5 derived_gap) = 199 rows.

**Rama catalog (CSV keys → verbatim table names, stable 2022-2027):**

| Key | Verbatim rama name (tables) |
|-----|------------------------------|
| agricultura | Agricultura, silvicultura, caza y pesca |
| minas | Explotación de minas y canteras |
| manufacturera | Industria manufacturera |
| electricidad | Electricidad, gas y agua |
| construccion | Construcción |
| comercio | Comercio al por mayor y menor |
| restaurantes | Restaurantes y hoteles |
| transporte | Transporte, almacenamiento y comunicaciones |
| financieros | Establecimientos financieros, bienes inmuebles y servicios prestados a las empresas |
| comunales | Servicios comunales, sociales y personales, seguridad y limpieza |
| hospitales | Actividades de hospitales |
| all_11_ramas | placeholder key for vintages whose per-rama table is unprinted (2022, 2024, effective-2023) |
| na | not applicable — maquila track and promedio rows (single national values) |

**Entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.smm.row (new) | track, rama, band, valid_from, valid_to, mensual, jornada, hora, pct_adjust, print_status, source_evid, note, instrument, gazette, signed_on, superseded_by | select/char/date/monetary | track: general · maquila (zonas_libres alias reserved) · promedio; band: 1-10 · 11-50 · 51-150 · 151+ · na; print_status: printed · reconstruction_blocked · derived_gap; seeded from `smm_tables.csv`; additive-only, never edited in place (D-H2); provenance per FR-008 | FR-009..FR-020, FR-022, FR-024..FR-026 |
| l10n_hn.smm.retro.obligation (new) | instrument, affected_from, affected_to, deadline_date, payment_mode, temp_workers_included | date/select/boolean | payment_mode: installments_apr_jun · total_or_deferred · retroactive_total · deferred_lump; rows: 308-4, 014-4, 411-3, 109-6, 233-4 | FR-027, FR-028 |
| l10n_hn.smm.escalator (new) | clause_ref, track, trigger_metric, trigger_year, threshold_pct, formula, de_oficio_deadline, status, executed_instrument | select/date | formula: general_replace_ipc · maquila_differential; status: pending · executed · lapsed; rows: 233-5 (pending, dic-2026), 109-4 (general 2025), 109-7 (maquila, 15-ene) | FR-023, FR-029 |
| l10n_hn.smm.incapaz.permit (new) | employee, pct_of_smm, valid_from, valid_to, dgs_reference | %-monetary/date | Art. 32 DGS permits — floor = pct × applicable SMM for the permit period | FR-006 |
| res.company | smm_track, smm_rama, smm_band_source | select/char | smm_track: general · maquila; rama = catalog key; band derived from the permanent-worker count (period-resolved) | FR-007, FR-013, FR-021 |
| hr.employee | smm_applicability, smm_agro_area | select | applicability: covered · exempt_public_post · exempt_manager_professional · domestic_special_regime · aprendiz · incapaz_permit; agro_area: field · industrial (agroindustrial employers) | FR-006, FR-014 |
| hr.payslip / hr.contract | smm_row_id (resolved), smm_mensual, smm_jornada, smm_hora (snapshot) | m2o/monetary | snapshot-on-write of the resolved row + values (D15); frozen on paid slips; corrections re-resolve with original-period rows (D16) | FR-001, FR-003, FR-010 |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` = computation/config/bookkeeping logic
in the LGPL client. No `saas`/`shared` rows: none of these FRs touch the
thin-client/SaaS architecture split (no SEE/electronic channel exists for
SMM data in the corpus; the sidecar is Odoo-side configuration). Model names
stable across Odoo 17/18/19/20. D19: no GL go-live cut-over surface is owned
here — retro-differential payments post through standard payroll journals;
the GL cut-over chassis belongs to the accounting wave (n/a with
justification). D18: a mid-year go-live with un-discharged retro windows
(e.g. going live in May 2026 owing Jan-Apr differentials) is handled by the
FR-027/FR-028 obligation rows as historical payroll inputs under the
wave-level ingestion contract (D-H3 monthly aggregates per contract); no
separate historical-journal surface is owned by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001..FR-005 | odoo | hr.contract + hr.payslip (constraints) + hr.salary.rule | floor constraints | Block below-floor wage/rate at contract save and payslip validation; effective-earnings check for piece-rate/modalities (FR-003); no age/sex field ever enters the lookup key (FR-005); CT nullity chassis = file 10 by article crossref (FR-002) |
| FR-006, FR-007 | odoo | hr.employee (applicability, agro_area) + res.company (track/rama) | flags + catalog | Art. 32 permits as dated l10n_hn.smm.incapaz.permit rows; rama catalog config (11 ramas + ZL row 12); no small-employer exemption flag exists |
| FR-008 | odoo | l10n_hn.smm.row | provenance columns | instrument/gazette/signed_on/superseded_by; outcomes, not procedure |
| FR-009..FR-020 | odoo | l10n_hn.smm.row + CSV seeding + lookup API | dated rows | D12: bienio instruments with Jan-1 effectivity; adaptation windows = the per-instrument retro deadlines (FR-027). D15/D16: dated rows, snapshot-on-write onto payslips, original-period recompute, additive supersession (FR-020). Weakest-cell print_status discipline; jornada÷30 / hora÷8 as load-time validation only (FR-012) |
| FR-041 | odoo | l10n_hn.smm.row provenance columns + l10n_hn.legal.note | fijación-process metadata (W5, Acuerdo 345) | Provenance/process only, never computation: commission identity per print, +15-day effectivity DEFAULT displaced by own-instrument vigencia clauses (R-H62); Acuerdo 345's own vigencia unpinned (108_ OQ-1) |
| FR-021..FR-023 | odoo | res.company smm_track + l10n_hn.smm.row + l10n_hn.smm.escalator | maquila track | R-H48 chain; Jun-Dic 2023 split rows resolve by period; differential escalator as conditional config (15-ene de-oficio watch) |
| FR-024..FR-026 | odoo | l10n_hn.smm.row (track=promedio) | promedio supply | R-H47: DGS-print-only rows; consumer = HN-TAX-FR-134 (taxation/04) — the 10× cap arithmetic is NOT here; missing vintages = config-gap rows that block the consumer |
| FR-027, FR-028 | odoo | l10n_hn.smm.retro.obligation + hr.payslip (differential run) | obligation rows | D18 note: a go-live owing retro windows ingests the differential as a historical input (D-H3 aggregation contract); payment modes per instrument; no backdated mutation |
| FR-029..FR-034 | odoo | l10n_hn.smm.escalator + l10n_hn.smm.row metadata + legal-notes layer | conditional config + notes | THEN-branch fires on instrument arrival only; R-H43/R-H45/R-H46/R-H62/R-H63/R-H64 encoded as metadata/notes; 90_ OQ-1 one-time visual check on load |
| FR-035..FR-037 | odoo | lookup API consumed by sibling files | interfaces | File 02 (HN-PAYR-FR-051..087) incl. the 02/95-Art. 6 SMM-average variant; T11 multa unit via EV81:EVID-261 pointer; files 03-05/07/08/10 by FR range — id consumption only |
| FR-038..FR-040 | odoo | run-level flags + period write-protection | guardrails | Missing-vintage / reconstruction / derived-gap blocks (parallel to HN-TAX-FR-124); filed-period protection; regime cutovers as dated rows (D16) |

Version-regime note (D12): the instrument chain STSS-308-2022 →
SETRASS-014-2023 (de-oficio re-fix) → SETRASS-411-2023 (maquila mid-year) →
SETRASS-109-2024 (bienio + 3-year maquila) → SETRASS-233-2026 (current
bienio) each carries Jan-1 (or Jun-1) effectivity with per-instrument retro
windows recorded on the obligation rows; mid-year SMM changes can straddle a
fiscal year — every consumer resolves by the row's own valid_from/valid_to
against the period anchor, never by vintage-of-the-FY (contrast with the ISR
bracket vintages of taxation/04).

## 6. Acceptance Criteria

- **AC-001:** Given a worker in industria manufacturera, band 1-10, with a
  March-2026 payslip and a contracted monthly wage of L12,000.00, then the
  floor lookup resolves L12,869.14 and the system blocks/elevates the wage
  to the floor (12,000.00 < 12,869.14) (FR-001, FR-002, FR-015).
- **AC-002:** Given a destajo worker in agricultura, band 151+, whose
  June-2026 computed effective earnings are L11,000.00, then the sufficiency
  test fails against the floor L12,349.49 and the run is flagged/blocked —
  the check ran on effective earnings, not the contracted rate (FR-003).
- **AC-003:** Given the 2026 agricultura 1-10 row (9,596.64 / 319.89 /
  39.99) on load, then the structural validation reproduces 9,596.64 ÷ 30 =
  319.89 and 319.89 ÷ 8 = 39.99 exactly; and given the 2027 minas 151+ row
  (19,919.96 / [gap] / 83.00), then jornada remains EMPTY with print_status
  reconstruction_blocked — the rule never fills it (FR-012, FR-016).
- **AC-004:** Given a maquila worker's June-2023 payslip, then the lookup
  resolves the Jun-Dic 2023 row L10,457.29 (not a Jan-May value, not any
  2026 value); and given a general-track worker's June-2023 payslip, then
  the lookup is BLOCKED (effective-2023 general amounts = damaged print +
  unpinned 2022 base) with the config-gap reason surfaced (FR-010, FR-018,
  FR-022, FR-038).
- **AC-005:** Given a food-producing agroindustrial employer (band 1-10)
  with one field worker and one industrial-area worker in 2026, then the
  floors resolve to L9,596.64 (agricultura) and L12,869.14 (manufacturera)
  for the same employer and period — the key was each worker's area
  (FR-014).
- **AC-006:** Given a January-2024 general-track payslip run, then the SMM
  lookup is blocked with an explicit config-gap flag — never the 2023 table,
  never 2023 × 1.055, never the 2025 table (FR-011, FR-019, FR-038, FR-040).
- **AC-007:** Given the loaded 2026 rows, then the promedio row reads
  L14,917.20 as printed and any recomputation from the table (mean
  L15,097.85; 45-value mean L15,049.68) is rejected; the 10× cap value
  L149,172.00 appears only in the taxation consumer (HN-TAX-FR-134), never
  in this file's data (FR-024, FR-025).
- **AC-008:** Given an FY2025 13th/14th-month cap computation request, then
  the promedio supply returns a config gap (2025 row = cited-not-printed;
  L13,985.16 NOT loaded) and the consumer blocks rather than computing with
  a derived value (FR-025, FR-026).
- **AC-009:** Given the 2026 bienio (gazetted 29-abr-2026) and a
  manufacturera 1-10 worker paid Jan-Apr 2026 at the 2025 floor L12,140.69,
  then the system computes four monthly differentials of 12,869.14 −
  12,140.69 = L728.45 (total L2,913.80) payable by 31-jul-2026 as a forward
  posting, and the paid Jan-Apr slips are not mutated (FR-027, FR-028).
- **AC-010:** Given an effective-date lookup for 2023-03-15 on the general
  track, then the operative vintage is the 014-2023 uniform-9.80% set
  (amount lookups blocked) and the 308-Art. 3 originally-fixed table is
  retrievable only as superseded history that never governed (FR-018,
  FR-020).
- **AC-011:** Given a hypothetical dic-2026 interanual IPC of 8.0%
  (> the fixed 7.5% for band 151+ in 2027), then the system surfaces the
  pending-escalator flag requiring the de-oficio instrument and does NOT
  change any 2027 row by formula; when the instrument arrives, new rows are
  added with supersession links (FR-029, FR-020).
- **AC-012:** Given two workers in the same rama, band and period who
  differ in sex and age, then the SMM resolution is identical for both
  (FR-005).
- **AC-013:** Given a worker flagged exempt_manager_professional, a domestic
  worker, and an aprendiz, then SMM floor enforcement is skipped per their
  applicability flags; and given an incapaz with an active Art. 32 permit of
  75% for Q3-2026 in restaurantes 1-10, then the applicable floor = 0.75 ×
  L13,292.06 for that period only (FR-006).
- **AC-014:** Given a January-2027 run for a zona-libre worker, then the
  maquila lookup is blocked with the 2027-coverage gap flag (109-2024
  coverage ended 31-dic-2026; no 2027 instrument in corpus) — never the
  2026 value L12,930.07 silently reused (FR-022, FR-038, FR-040).
- **AC-015:** Given a CT sanction computed in SMM units by the sanctions
  consumer, then the unit value is fetched from this file's dated
  promedio/general rows by id and no sanction arithmetic exists in this file
  (FR-036).
- **AC-016:** Given an employer in restaurantes y hoteles with 60 permanent
  workers, then the 2027 lookup uses band 51-150 (L17,459.80 mensual as
  printed); given the same employer grows to 160 permanent workers in the
  next period, then the band 151+ row applies from that period — bands
  resolve per period, never retroactively (FR-013, FR-010).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | 104_ OQ-2 print provenance: D. 103 exists in the corpus only as a compilation print with the running-header artifact "CÓDIGO DEL TRABAJO VIGENTE" and no gazette reference for the 1971 original; text is clean and LB quoting stands — acquire the original gazette cite for the registry. | no | acquisition queue | open |
| OQ-002 | 104_ OQ-3 → RESOLVED by ruling R-H62: Art. 35's at-least-annual December cadence vs the multi-year bienio practice since 2019 — the bienios' own vigencia clauses control (later, specific executive instruments); doctrinal gap noted, nothing further to resolve here. | no | — | resolved (R-H62) |
| OQ-003 | 90_ OQ-3: 2027 gazette table OCR gaps — agricultura 11-50 (full row), financieros 11-50 (full row), 15 jornada/hora cells + 2 full rows (V-HN1 exact recount) and the restaurantes 1-10 digit uncertainty are reconstruction_blocked; reconstruction candidates exist arithmetically (EVID-224) but load only after visual confirmation of the gazette or a clean DGS 2027 print. | no | Takumi S-HN4 (P1) | open |
| OQ-004 | 90_ OQ-4: no 2027 promedio exists anywhere in the corpus → the FY2027 13th/14th 10×SMM-promedio cap input (consumer HN-TAX-FR-134) stays blocked until the DGS 2027 table issues (expected early 2027); never derive. | no | Takumi S-HN4 (P1) + acquisition | open |
| OQ-005 | 91_ OQ-1: promedio methodology unpublished (2026 printed L14,917.20 ≠ computed means 15,097.85 / 15,049.68; 2025 mean 14,177.03 ≠ cited 13,985.16) — the promedio is a first-class DGS-print datum; acquisition: DGS "Tabla de Salario Mínimo" prints for 2022-2025 (+ 2023 = 83_ OQ-3, 101_ OQ-4 same family) to unblock FY2022-FY2025 cap inputs. | no | acquisition queue | open |
| OQ-006 | 101_ OQ-2: the 308-Art. 2 2022 amounts table is an image (zero values extracted) → 2022 SMM amounts unpinned; also blocks the effective-2023 amounts (014-2023 fixed 9.80% OVER the 2022 table). Options: higher-dpi re-OCR of 101_ pp.3/8, or acquire the DGS 2022 print. | no | acquisition queue | open |
| OQ-007 | 82_ OQ-1: 2024 general-track amounts not printed in the extract (only the 2025 table follows Art. 2) and the bienio percentage cuadro is mojibake (pinned via 233-CONS.(7) + exact arithmetic — R-H46 derivation-flagged); acquire the DGS 2024 print / gazette original to pin both. | no | acquisition queue | open |
| OQ-008 | 82_ OQ-2: maquila 2024 (11,137.01) and 2025 (11,972.29) amounts are derived only (percentages printed; the chain closes exactly on the printed 2026 L12,930.07 — R-H48); blocked rows until DGS prints pin them with citation fidelity. | no | acquisition queue | open |
| OQ-009 | 83_ OQ-1: the 014-2023 Art. 2 effective-2023 table is heavily OCR-damaged (parenthesis-for-comma artifacts; ~2 cells chain-verified); re-OCR pp.2-3 at 400dpi/PSM 6 or use the DGS 2023 print to unblock effective-2023 amount rows. | no | acquisition queue | open |
| OQ-010 | 83_ OQ-2: the 014-2023 print's article numbering skips Art. 3 (sibling instruments 109-3 / 233-3 carry the agroindustrial classification) — whether the agro split applies for 2023 is unverified; blocked-year effect only (2023 amounts are blocked anyway, OQ-009). | no | acquisition queue | open |
| OQ-011 | 84_ OQ-1: the Jan-May 2023 maquila SMM (pre-modification STSS-006-2019 Cláusula Novena, 8%) is unprinted (≈9,506.63 derived only); acquire STSS-006-2019 (G 34,840, 9-ene-2019) — also the maquila track's base instrument. | no | acquisition queue | open |
| OQ-012 | 90_ OQ-1: the 233-Art. 1 percentage cuadro is garbled in both layers; values triple-pinned (native fragments + OCR + exact arithmetic on all readable cells, residual risk ≈ nil); perform the one-screenshot visual confirmation of the gazette original when the sidecar is loaded to production. | no | Takumi S-HN4 (P1) | open |
| OQ-013 | Reglamento leads: the Ley del Salario Mínimo's own Reglamento (cited "y su Reglamento" in 233-CONS.(8); governs aprendiz wages, Art. 33) and the Reglamento de las Comisiones de Salario Mínimo (cited in 233 POR TANTO) are unacquired; D. 43-97 (G 28,271, 29-may-1997) itself is cited only via footnotes — same acquisition family as the commission instruments (SETRASS-563-2021/-647-2023/-101-2026, Acuerdos 25-2022/029-2026, Actas 002-2024/004-2026). | no | acquisition queue | open |
| OQ-014 | Maquila 2027: no source instrument exists (109-2024 coverage ends 31-dic-2026; 233-Art. 7 excludes maquila from the 2026-2027 bienio) → 2027 maquila lookups blocked; watch for a new maquila instrument in the 2027 cycle. | no | Takumi S-HN4 (P1) + acquisition | open |
