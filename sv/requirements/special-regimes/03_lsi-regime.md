# SV — Special regimes — LSI regime: indefinite exemptions, local-market caps, auditor dictamen

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes); W19 T3 re-verification (80_) |
| Updated | 2026-08-22 |

## 1. Purpose

This file owns the Ley de Servicios Internacionales (International Services
Law, LSI) benefit regime: the LSI exemption shapes as D15 dated rows —
*desarrollista*/*administrador* finite 15-year ISR / 10-year municipal
windows anchored on parque-operations start, and the *usuario directo* /
*centro de servicios* ISR + municipal exemptions that are INDEFINITE
("durante el período que realicen sus operaciones en el país") = open-ended
rows with a CESSATION event and no phase-downs, a row shape DISTINCT from
the ZF/DPA ladders of `02_zf-exemption-schedules.md` and never unified with
them; the *franquicia arancelaria total* (total tariff franchise) of
centros; the declaration-duty-survives-exemption guard (LSI native text);
the 17b_ Art. 22 local-market percentage caps (50/40/30 — the regime's
distinctive reglamento-level dated parameter) with their exclusion
categories and annual local-share monitor; the semestral auditor-*dictamen*
(opinion report) family — nomination lifecycle, periods, deadlines, content
checklist and the five *anexos* (attachments) as Odoo data-packager
surfaces; the LSI requisito monitors (m², BPO investment/jobs/contract,
médico thresholds); the *usuario indirecto* consignment-liability ledger;
the 90%-Salvadoran staffing quota monitor; the CT-158-*inciso-segundo*
carve-outs (beneficiaries and non-domiciled foreign employees); the fianza
(bond) event; the AML-conviction revocation link; and the ZF→LSI migration
*transitorias* as per-case config (no mechanics).

It does **not** cover: the ZF/DPA exemption ladders, dividend window,
exception-goods gate mechanics and capital-goods/flat-track extensions
(`02_zf-exemption-schedules.md` — the paid-tax-evidence inverting gate
SV-SPE-FR-036 and the exemption-row chassis SV-SPE-FR-023 are consumed by
id); the customs clocks, 24-month admisión temporal and destinación windows
(`04_customs-clocks.md`); the export test, the 1.5%/1% retention VALUES and
IVA routing (`05_tan-iva-interface.md` + taxation/04 by id — this file only
verifies their application inside the dictamen pack); DUCA/teledespacho
(`06_customs-declarations.md`); the general obligations-of-record
(electronic registers, manifiesto custody, notices), sanction ladders and
SMM-priced values (`07_obligations-reporting-sanctions.md`); FOVIAL/COTRANS
(`08_fovial-cotrans.md`). The Quincena-25 certificado consumption stays
with SV-SPE-FR-039 (it already covers LSI profiles). This file consumes
Task 1's beneficiary-profile and benefit-state model by FR id (SV-SPE-FR-003,
FR-013, FR-014, FR-015, FR-017, FR-018) and never restates it.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): LSI = **80_**
(Ley de Servicios Internacionales, D.L. Nº 431, 11-oct-2007, D.O. N° 199
T.377 25-oct-2007, as reformed by D.L. Nº 277-2013, D.O. N° 28 T.398
11-feb-2013 → vigencia ~19-feb-2013 for the reformed articles; INDICE
LEGISLATIVO consolidated print, 34 pp — **W19 T3: supersedes 14_ thru D.L.
277-2013**; 14_ = the 2007 base print, retained as identity/provenance
record; LBs re-keyed 14_→80_) + **17b_** (Reglamento de Aplicación, D. Nº
131, 4-dic-2008, D.O. N° 235 T.381 12-dic-2008; vigencia 8 days (Art. 67)
→ effective 20-dic-2008; W18 sweep: text-identical to the live TF print —
parity; its Art. 22 local-market caps, Arts. 45-61
auditor-dictamen regime and Art. 65 CT-158-II carve-out are THIS file's
governing reglamento legs — the caps are reglamento-level dated parameters
absent from the law). Pointer LBs of this file: the CT retention family =
**05_** Código Tributario (05_ read W4; taxation/04 LB-018 / SV-TAX-FR-126
is the CT-side anchor consumed by id for the Art. 158 inciso-segundo
cross-check — OQ-4); the 1.5% ISR / 1% IVA retention values and their
withholding-engine rows = `05_tan-iva-interface.md` (T5) + taxation/04 by
id, never restated here; payroll staffing/SS records = payroll wave by id;
the AML-conviction surface = commercial-legal by id.

**SOQ-30 verification note (rides EVERY regime LB in this file):** the LSI
half is RESOLVED W19 T3 — 80_ is the consolidated print thru D.L. 277-2013
(the W13 14_/17b_ prints were the 2007/2008 originals with no reform
block; the 277-2013 reform is now folded: Arts. 5/6/8/23/24/24-A deltas
re-verified against 80_, LBs re-keyed 14_→80_); remaining unverified:
post-2013 LSI traffic (80_ tail) and 17b_ beyond its 2008 print (W18
parity-verified text-identical — SOQ-22-kin watch narrowed); article text
is cited **as printed**. Verbatim text below is copied
from the W13 evidence file (EVID-259/262/264/265/267), the W19 T3 evidence
(EVID-380..384 of `80_82_LSI_ZF.evidence.md`) and, where the
evidence abbreviates, from the extraction txts
`sv/.extractions/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf.txt`
(the text of record; the superseded
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt` remains the
pre-277 provenance record) and
`sv/.extractions/17b_Reglamento_Servicios_Internacionales.pdf.txt` (citable
per standing S3 ruling 25; page pointers = txt PAGE markers). D15
discipline: every cap value, year-count, deadline, quota and threshold in
this file is a dated config row with instrument provenance — never a global
constant.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Servicios Internacionales, Art. 14: "LOS DESARROLLISTAS AUTORIZADOS… GOZARÁN DE LOS SIGUIENTES BENEFICIOS E INCENTIVOS FISCALES: a) EXENCIÓN TOTAL DEL IMPUESTO SOBRE LA RENTA POR EL PERÍODO DE QUINCE AÑOS CONTADOS A PARTIR DEL INICIO DE SUS OPERACIONES EL PARQUE DE SERVICIOS DEBIDAMENTE CALIFICADO. ESTA EXENCIÓN EN EL CASO DE LAS SOCIEDADES SE APLICARÁ TANTO A LA SOCIEDAD PROPIETARIA DEL PARQUE, COMO A LOS SOCIOS O ACCIONISTAS INDIVIDUALMENTE CONSIDERADOS, RESPECTO A LAS UTILIDADES O DIVIDENDOS PROVENIENTES DE LA ACTIVIDAD BENEFICIADA. EN CASO QUE UNO O MÁS SOCIOS SEAN PERSONAS JURÍDICAS, ESTE BENEFICIO SERÁ EXCLUSIVO DE ÉSTAS, EL CUAL NO PODRÁ TRASLADARSE A LOS SOCIOS. LA EXENCIÓN A QUE SE REFIERE ESTE LITERAL, NO LIBERA AL BENEFICIARIO, DE LA OBLIGACIÓN DE PRESENTAR LA RESPECTIVA DECLARACIÓN TRIBUTARIA EN CADA EJERCICIO IMPOSITIVO DE LA OPERACIÓN DEL PARQUE DE SERVICIOS. b) EXENCIÓN TOTAL DE LOS IMPUESTOS MUNICIPALES SOBRE EL ACTIVO DE LA EMPRESA, POR EL PERÍODO DE DIEZ AÑOS, A PARTIR DEL INICIO DE SUS OPERACIONES. c) EXENCIÓN TOTAL DEL IMPUESTO SOBRE TRANSFERENCIA DE BIENES RAÍCES, POR LA ADQUISICIÓN DE AQUELLOS BIENES RAÍCES A SER UTILIZADOS EN LA ACTIVIDAD SUJETA A DICHO INCENTIVO." | Desarrollistas enjoy: a) TOTAL ISR exemption for FIFTEEN years counted from the start of their operations of the duly qualified services park; for societies the exemption applies both to the owning society and to the socios or accionistas individually considered, re utilidades/dividends from the benefited activity; where one or more socios are personas jurídicas the benefit is EXCLUSIVE of those and not transferable to their socios; the exemption does NOT release the beneficiary from presenting the respective tax declaration in each ejercicio impositivo of the park's operation; b) TOTAL municipal-tax exemption ON THE COMPANY'S ASSETS (activo) for TEN years from the start of operations; c) total ITBIR (real-estate transfer tax) exemption on acquisitions of real estate to be used in the incentivated activity | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 14 p.11 (EVID-262; 80_ txt PAGE 11 — unchanged; 14_ re-keyed W19) |
| LB-002 | Ley de Servicios Internacionales, Art. 17: "LOS ADMINISTRADORES DE LOS PARQUES DE SERVICIOS… GOZARÁN DE LOS BENEFICIOS… SIGUIENTES: a) EXENCIÓN TOTAL DEL IMPUESTO SOBRE LA RENTA POR EL PERÍODO DE QUINCE AÑOS CONTADOS A PARTIR DEL INICIO DE SUS OPERACIONES POR LA ACTIVIDAD DE ADMINISTRACIÓN DEL PARQUE DE SERVICIOS… [misma cláusula de sociedad/socios + exclusividad de personas jurídicas y mismo párrafo de declaración tributaria que el Art. 14 a)]. b) EXENCIÓN TOTAL DE LOS IMPUESTOS MUNICIPALES SOBRE EL ACTIVO DE LA EMPRESA, POR EL PERÍODO DE DIEZ AÑOS, A PARTIR DEL INICIO SUS OPERACIONES. SE EXCEPTÚAN DE ESTOS BENEFICIOS LA OPERACIÓN DE ACTIVIDADES COMPLEMENTARIAS SEÑALADAS EN ESTA LEY." Art. 18: "EN EL CASO QUE LA MISMA PERSONA OBTENGA LAS CALIFICACIONES DE DESARROLLISTA Y DE ADMINISTRADOR DE UN PARQUE DE SERVICIOS, ÉSTA GOZARÁ DE LOS BENEFICIOS ESTABLECIDOS EN LOS ARTÍCULOS 14 Y 17 DE ESTA LEY." | Administradores enjoy: a) total ISR exemption for FIFTEEN years counted from the start of their operations FOR THE PARK-ADMINISTRATION activity (same sociedad/socios clause, PJ-socio exclusivity and declaration-duty paragraph as Art. 14 a)); b) total municipal-tax exemption on the activo for TEN years from operations start; the operation of complementarias (complementary) activities is EXCEPTED from these benefits. Art. 18: a person holding BOTH desarrollista and administrador qualifications enjoys BOTH benefit sets (Arts. 14 and 17) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Arts. 17-18 pp.12-13 (EVID-262; 80_ txt PAGE 12-13 — unchanged; 14_ re-keyed W19) |
| LB-003 | Ley de Servicios Internacionales, Art. 21: "EL USUARIO DIRECTO DE UN PARQUE DE SERVICIOS TENDRÁ DERECHO A GOZAR DE LOS SIGUIENTES BENEFICIOS…: a) LIBRE INTERNACIÓN AL PARQUE DE SERVICIOS, POR EL PERÍODO QUE REALICEN SUS OPERACIONES EN EL PAÍS, DE MAQUINARIA, EQUIPO, HERRAMIENTAS, REPUESTOS, ACCESORIOS, MOBILIARIO Y EQUIPO DE OFICINA Y DEMÁS BIENES, QUE SEAN NECESARIOS PARA LA EJECUCIÓN DE LA ACTIVIDAD DE SERVICIOS INCENTIVADA. SE EXCEPTÚAN DE ESTE BENEFICIO LOS BIENES Y SERVICIOS SIGUIENTES: ALIMENTACIÓN Y BEBIDAS, PRODUCTOS QUE CONTENGAN TABACO, BEBIDAS ALCOHÓLICAS, ARRENDAMIENTO DE VIVIENDA, MUEBLES Y ENSERES DEL HOGAR, ARTÍCULOS DE LIMPIEZA, ARTÍCULOS SUNTUARIOS O DE LUJO, VEHÍCULOS PARA TRANSPORTE DE PERSONAS DE FORMA INDIVIDUAL O COLECTIVA Y MERCANCÍAS, SERVICIOS DE HOTEL, EN CUYO CASO, SU INGRESO AL PARQUE DE SERVICIOS ESTARÁ SUPEDITADO A LA PRESENTACIÓN DE LA DECLARACIÓN DE MERCANCÍAS DEFINITIVA A PAGO… O… COMPROBANTES DE CRÉDITO FISCAL O FACTURA DE CONSUMIDOR FINAL… EN LOS CUALES CONSTE QUE SE HA PAGADO EL IMPUESTO CORRESPONDIENTE. b) EXENCIÓN DEL IMPUESTO SOBRE LA RENTA, EXCLUSIVAMENTE POR LOS INGRESOS PROVENIENTES DE LA ACTIVIDAD INCENTIVADA, DURANTE EL PERÍODO QUE REALICEN SUS OPERACIONES EN EL PAÍS, CONTADOS A PARTIR DEL EJERCICIO IMPOSITIVO EN QUE EL BENEFICIARIO INICIE SUS OPERACIONES. ESTA EXENCIÓN, EN CASO DE LAS SOCIEDADES, SE APLICARÁ TANTO A LA SOCIEDAD TITULAR COMO A LOS SOCIOS INDIVIDUALMENTE CONSIDERADOS… EN CASO QUE UNO O MÁS SOCIOS SEAN PERSONAS JURÍDICAS, ESTE DERECHO SERÁ EXCLUSIVO DE ÉSTAS… DICHA EXENCIÓN NO LIBERA AL BENEFICIARIO, DE LA OBLIGACIÓN DE PRESENTAR LA RESPECTIVA DECLARACIÓN TRIBUTARIA EN CADA EJERCICIO IMPOSITIVO DE SU OPERACIÓN. c) EXENCIÓN DE LOS IMPUESTOS MUNICIPALES SOBRE EL ACTIVO DE LA EMPRESA, DURANTE EL PERÍODO QUE REALICEN SUS OPERACIONES EN EL PAÍS, CONTADOS A PARTIR DEL EJERCICIO FISCAL EN QUE EL BENEFICIARIO INICIE SUS OPERACIONES." | The usuario directo of a services park enjoys: a) FREE INTERNATION into the park, for the period it performs operations in the country, of machinery, equipment, tools, spare parts, accessories, furniture and office equipment and other goods necessary for the incentivated service activity — EXCEPT the listed goods/services (food and beverages; tobacco products; alcoholic beverages; housing rental; home furniture and furnishings; CLEANING ARTICLES; sumptuary or luxury articles; vehicles for individual/collective person and goods transport; hotel services), whose entry is conditioned on a definitive-payment DM or a CCF/FCF evidencing the tax PAID; b) ISR exemption EXCLUSIVELY on income from the incentivated activity, DURING THE PERIOD it performs operations in the country, counted from the EJERCICIO IMPOSITIVO in which the beneficiary starts operations (for societies: sociedad titular + socios individually; PJ-socio exclusivity; the exemption does NOT release the beneficiary from presenting the respective tax declaration in each ejercicio); c) municipal-tax exemption on the activo, during the same indefinite period counted from the first ejercicio fiscal of operations | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 21 pp.13-14 (EVID-262; 80_ txt PAGE 13-14 — unchanged; 14_ re-keyed W19) |
| LB-004 | Ley de Servicios Internacionales, Art. 25: "EL TITULAR DE UNA EMPRESA, CUYO ESTABLECIMIENTO HAYA SIDO DECLARADO CENTRO DE SERVICIOS, TENDRÁ DERECHO A GOZAR DE LOS SIGUIENTES BENEFICIOS…: a) EXENCIÓN TOTAL DE DERECHOS ARANCELARIOS Y DEMÁS IMPUESTOS QUE GRAVEN LA IMPORTACIÓN DE LA MAQUINARIA, EQUIPO, HERRAMIENTAS, REPUESTOS, ACCESORIOS, MOBILIARIO Y EQUIPO DE OFICINA, Y DEMÁS BIENES, QUE SEAN NECESARIOS PARA LA EJECUCIÓN DE LA ACTIVIDAD INCENTIVADA. [mismo inciso de excepciones y prueba de impuesto pagado que el Art. 21 a), aplicado al ingreso al centro de servicios]. b) EXENCIÓN DEL IMPUESTO SOBRE LA RENTA, EXCLUSIVAMENTE POR LOS INGRESOS PROVENIENTES DE LA ACTIVIDAD INCENTIVADA, DURANTE EL PERÍODO QUE REALICEN SUS OPERACIONES EN EL PAÍS, CONTADOS A PARTIR DEL INICIO DE OPERACIONES. [misma cláusula de sociedad/socios, exclusividad y declaración tributaria]. c) EXENCIÓN DE LOS IMPUESTOS MUNICIPALES SOBRE EL ACTIVO DE LA EMPRESA, DURANTE EL PERÍODO QUE REALICEN SUS OPERACIONES EN EL PAÍS, CONTADOS A PARTIR DEL INICIO DE OPERACIONES." | The holder of an enterprise declared a centro de servicios enjoys: a) TOTAL exemption of tariff duties and the other taxes levied on the IMPORT of machinery, equipment, tools, spare parts, accessories, furniture and office equipment and other goods necessary for the incentivated activity (the franquicia arancelaria total), with the same exception list and paid-tax evidence condition as Art. 21 a), applied to entry into the centro; b) ISR exemption exclusively on incentivated-activity income, during the period operations are performed in the country, counted from the start of operations (same sociedad/socios, PJ-exclusivity and declaration-duty clauses); c) municipal-tax exemption on the activo over the same indefinite period from the start of operations | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 25 p.18 (EVID-262; 80_ txt PAGE 18 — unchanged; 14_ re-keyed W19) |
| LB-005 | Reglamento de Servicios Internacionales (17b_), Art. 21: "…DEBERÁN CUMPLIR CON EL REQUISITO QUE SUS SERVICIOS SEAN DESTINADOS A LA EXPORTACIÓN, CONSIDERANDO POR ÉSTA, EL SERVICIO UTILIZADO EXCLUSIVAMENTE EN EL EXTERIOR O EN TERRITORIO EXTRA-ADUANAL Y PRESTADO A UN CLIENTE DOMICILIADO EN EL EXTRANJERO O EN TERRITORIO EXTRA-ADUANAL Y PODRÁN DESTINAR PARTE DE SUS SERVICIOS AL MERCADO NACIONAL." Art. 22: "PARA AQUELLOS SERVICIOS AUTORIZADOS POR EL MINEC, QUE CON BASE AL INCISO 3º DEL ART. 8 DE LA LEY, DESTINEN PARTE DEL SERVICIO AL MERCADO NACIONAL, PODRÁN HACERLO SEGÚN SE ESPECIFICA A CONTINUACIÓN: a) DISTRIBUCIÓN INTERNACIONAL Y OPERACIONES INTERNACIONALES DE LOGÍSTICA, HASTA UN MÁXIMO DEL 50% DEL TOTAL DE LOS SERVICIOS PRESTADOS. — LOS PORCENTAJES DE VENTA LOCAL NO APLICARÁN… OPERACIONES DE ACOPIO PARA EXPORTACIÓN DE MERCANCÍAS DE LIBRE CIRCULACIÓN Y ALMACENAMIENTO DE MERCANCÍAS NACIONALES Y NACIONALIZADAS. TAMPOCO APLICARÁN, CUANDO LAS MERCANCÍAS PROVENGAN DE UN CLIENTE RESIDENTE EN EL EXTRANJERO CON FINES DE RE-EXPORTACIÓN, Y SEAN FACTURADOS POR SU FILIAL RESIDENTE EN EL PAÍS. b) PROCESOS EMPRESARIALES, SERVICIOS FINANCIEROS INTERNACIONALES, CENTRO INTERNACIONAL DE LLAMADAS, HASTA UN MÁXIMO DEL 40%… c) TECNOLOGÍAS DE INFORMACIÓN, INVESTIGACIÓN Y DESARROLLO, HASTA UN MÁXIMO DEL 30% DEL TOTAL DE LOS SERVICIOS PRESTADOS." | Applicants must satisfy the requirement that their services be destined to exportation (the export test) and MAY destine PART of their services to the national market, within the caps: a) distribución internacional and logística internacional — up to a MAXIMUM of 50% of the total services rendered; the local-sale percentages DO NOT apply to acopio-para-exportación operations on goods of libre circulación and the warehousing of national and nacionalizada goods, NOR when the goods come from a client resident abroad for re-export and are billed by its local filial; b) procesos empresariales, servicios financieros internacionales, centros internacionales de llamadas — up to 40%; c) tecnologías de información, investigación y desarrollo — up to 30% of total services rendered | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Arts. 21-22 p.8 (EVID-265; txt PAGE 8; SOQ-30 print) |
| LB-006 | Ley de Servicios Internacionales, Art. 47 f): "CONTAR CON LOS SERVICIOS DE UNA FIRMA INDEPENDIENTE DE AUDITORÍA DEBIDAMENTE AUTORIZADA POR LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS, LA QUE DEBERÁ EMITIR DICTÁMENES SEMESTRALES. DICHOS DICTÁMENES CONTENDRÁN PRONUNCIAMIENTOS ACERCA DEL CUMPLIMIENTO DEL BENEFICIARIO DE LAS OBLIGACIONES ESTABLECIDAS EN LA PRESENTE LEY, ASÍ COMO DE LA VERACIDAD Y CONFORMIDAD DE LA INFORMACIÓN PROPORCIONADA POR EL BENEFICIARIO ACERCA DE LAS VENTAS EFECTUADAS Y DEBERÁN SER REMITIDOS POR LA FIRMA DE AUDITORÍA DIRECTAMENTE A LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS Y AL MINISTERIO DE ECONOMÍA." (closing line of Art. 47: "EL INCUMPLIMIENTO A LO ESTABLECIDO EN ESTE ARTÍCULO SERÁ CONSIDERADO COMO INFRACCIONES GRAVES.") | The beneficiary must retain an independent audit firm duly authorized by the DGII, which shall issue SEMESTRAL dictámenes containing pronouncements on the beneficiary's compliance with the law's obligations and on the truthfulness and conformity of the information provided about the VENTAS made; the dictámenes are remitted by the audit firm DIRECTLY to the DGII and MINEC. Non-compliance with Art. 47 counts as GRAVE infringements (sanction values owned by `07` by id) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 47 f) + closing line pp.26-27 (EVID-264; 80_ txt PAGE 26-27 — unchanged; 14_ re-keyed W19) |
| LB-007 | Reglamento (17b_), Art. 47: "…SE ENCUENTRAN OBLIGADAS A NOMBRAR A UNA FIRMA INDEPENDIENTE DE AUDITORÍA AUTORIZADA POR LA DGII, PARA QUE EMITA DICTAMEN QUE CONTENGA PRONUNCIAMIENTOS SOBRE EL CUMPLIMIENTO DE SUS OBLIGACIONES ESTABLECIDAS EN LA LEY Y LA VERACIDAD Y CONFORMIDAD DE LAS CIFRAS DE INGRESOS POR VENTAS." Art. 48: "EL NOMBRAMIENTO DE AUDITOR… SE REALIZARÁ ANUALMENTE DENTRO DE LOS PRIMEROS CINCO MESES DEL AÑO… EN EL CASO QUE EL BENEFICIARIO FUERE AUTORIZADO POR EL MINEC EN EL TRANSCURSO DEL PRIMER SEMESTRE DEL AÑO, NOMBRARÁ AUDITOR PARA QUE EMITA DICTAMEN PARA EL SEGUNDO SEMESTRE DEL AÑO, DENTRO DEL PLAZO DE DOS MESES CONTADOS A PARTIR DEL DÍA SIGUIENTE DE LA AUTORIZACIÓN… EL NOMBRAMIENTO DEL AUDITOR SERÁ INFORMADO… A LA DGII… DENTRO DEL PLAZO DE DIEZ DÍAS HÁBILES SIGUIENTES CONTADOS A PARTIR DEL SIGUIENTE DE EFECTUADO EL NOMBRAMIENTO, MEDIANTE FORMULARIOS… BAJO LAS ESPECIFICACIONES QUE DISPONGA LA DGII. [renuncia/remoción:] …SE INFORMARÁ, INDICANDO LAS CAUSALES… DENTRO DE LOS CINCO DÍAS HÁBILES SIGUIENTES DE OCURRIDA. EL BENEFICIARIO NOMBRARÁ NUEVO AUDITOR DENTRO DE DIEZ DÍAS HÁBILES SIGUIENTES… [los nombramientos exhibirán] EL NÚMERO DE AUTORIZACIÓN DEL CONSEJO DE VIGILANCIA DE LA PROFESIÓN DE CONTADURÍA PÚBLICA Y AUDITORÍA Y LA RESOLUCIÓN EMITIDA POR LA DGII…" | Beneficiaries must appoint a DGII-authorized independent audit firm to issue the dictamen. The auditor is appointed ANNUALLY WITHIN THE FIRST FIVE MONTHS of the year; a beneficiary authorized by MINEC during the first semester appoints (for the second-semester dictamen) within TWO MONTHS counted from the day after the authorization; the appointment is INFORMED to the DGII within TEN días hábiles counted from the day after it is made, on DGII-specified formularios; resignation/removal is informed within FIVE días hábiles with causes, a new auditor is appointed within TEN días hábiles and that appointment informed likewise; the appointment exhibits the auditor's Consejo de Vigilancia and DGII authorization numbers | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Arts. 47-48 pp.16-18 (EVID-267; txt PAGE 16-18; SOQ-30 print) |
| LB-008 | Reglamento (17b_), Art. 58 (dictamen content, verificación items): "…e) …SE REALIZARON PROCEDIMIENTOS PARA VERIFICAR EL CUMPLIMIENTO… SEÑALÁNDOSE ENTRE ELLOS LOS SIGUIENTES: …4. QUE SE VERIFICÓ QUE POR LOS SERVICIOS PRESTADOS EN EL TERRITORIO ADUANERO NACIONAL, LES FUE APLICADO LOS PORCENTAJES DE RETENCIÓN DEL 1% DE [IVA], POR EL SERVICIO PRESTADO Y EL 1.5% DE [ISR], ESTABLECIDOS EN EL ART. 8 DE LA LEY, ASÍ COMO QUE DICHAS RETENCIONES FUERON REGISTRADAS, DECLARADAS Y ACREDITADAS POR LOS VALORES CORRESPONDIENTES. 5. LA REALIZACIÓN DE PROCEDIMIENTOS CORRESPONDIENTES A LA VERIFICACIÓN DEL INVENTARIO FÍSICO… RELATIVO A SUS CLIENTES, CON LOS RESPECTIVOS REGISTROS DETALLADOS Y SEPARADOS POR CADA CLIENTE Y POR TIPO DE SERVICIO… 6. LA VERIFICACIÓN… DE QUE LOS VALORES DESCONTADOS A LOS EMPLEADOS EN CONCEPTO DE COTIZACIONES DE PENSIONES Y DE SEGURIDAD SOCIAL Y LAS CUOTAS PATRONALES EN DICHOS CONCEPTOS FUERON DEBIDAMENTE PAGADAS. …9. …: i. INFORMAR AL ORGANISMO CORRESPONDIENTE EL CAMBIO EN LA ESTRUCTURA DE LA EMPRESA…; ii. VERIFICAR EL REQUISITO DEL NÚMERO NO MENOR A DIEZ PUESTOS DE TRABAJO PERMANENTE… PROCESOS EMPRESARIALES; iii. VERIFICAR EL PORCENTAJE ESTABLECIDO EN EL ART. 22 DEL PRESENTE REGLAMENTO, POR MEDIO DE LAS VENTAS EFECTUADAS DURANTE CADA AÑO; iv. LLEVAR CONTROLES Y REGISTROS CONTABLES…" (also e.1 acuerdo-conformity, e.2 income documentation/registration/declaration ISR+IVA, e.3 retention calculation and payment, e.7 compras/importaciones free-of-tax and destined to the benefited activity, e.8 original/modifying declarations examination) | Dictamen content items the auditor pronounces on, including verification that: e.4 local-market (territorio aduanero nacional) services had the 1% IVA and 1.5% ISR retention percentages of the law's Art. 8 APPLIED, and that those retentions were REGISTERED, DECLARED and CREDITED for the corresponding values; e.5 the physical-inventory verification performed by distributor/logistics usuarios, with detailed and separate records PER CLIENT and PER SERVICE TYPE; e.6 the values discounted to employees for pension and social-security cotizaciones and the PATRONAL quotas were duly PAID; e.9.i structure-change inform; e.9.ii the ≥10 permanent jobs requisito for procesos empresariales; e.9.iii the Art. 22 cap percentage, BY MEANS OF THE VENTAS (sales) EFFECTED DURING EACH YEAR; e.9.iv accounting records (plus e.1 acuerdo-conformity, e.2 income documentation/declaration, e.3 retention calculation/payment, e.7 compras, e.8 declarations) | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Art. 58 pp.22-24 (EVID-267; txt PAGE 22-24; SOQ-30 print) |
| LB-009 | Reglamento (17b_), Art. 59: "EL DICTAMEN E INFORME SE ACOMPAÑARÁ DE LOS SIGUIENTES ANEXOS: a) ANÁLISIS COMPARATIVO DE INGRESOS: …COMPARACIÓN ENTRE: 1) LOS INGRESOS REGISTRADOS EN LIBROS DE VENTAS Y DECLARACIONES DEL [IVA] Y, 2) LOS INGRESOS REGISTRADOS PARA EFECTOS CONTABLES Y LOS DECLARADOS…; b) ANÁLISIS COMPARATIVO MENSUAL DE RETENCIONES DE LOS TRIBUTOS RELACIONADOS CON LAS VENTAS AL MERCADO NACIONAL: …1. [IVA]: LAS RETENCIONES QUE LE FUERON EFECTUADAS AL BENEFICIARIO SEGÚN REGISTROS CONTABLES, COMPARANDO DICHOS VALORES CON LOS ACREDITADOS EN LAS RESPECTIVAS DECLARACIONES MENSUALES. 2. [ISR]: IGUAL COMPARACIÓN…; c) ANÁLISIS COMPARATIVO DE COTIZACIONES DE SEGURIDAD SOCIAL Y PREVISIONAL: …DETALLE MENSUAL DE LOS VALORES REGISTRADOS CONTABLEMENTE CON LOS VALORES MENSUALES PAGADOS SEGÚN PLANILLAS DEL INSTITUTO SALVADOREÑO DEL SEGURO SOCIAL Y DE LAS ADMINISTRADORAS DE FONDOS DE PENSIONES… SE DESGLOSARÁN DE FORMA MENSUAL LOS VALORES DE LOS APORTES LABORAL Y PATRONAL…; d) ANÁLISIS COMPARATIVO DE COMPRAS: …COMPARACIÓN MENSUAL DE LAS COMPRAS AL MERCADO NACIONAL E IMPORTACIONES REGISTRADAS EN EL LIBRO DE COMPRAS… CON LAS COMPRAS E IMPORTACIONES DECLARADAS…; e) DETALLE DE HALLAZGOS DETERMINADOS EN AUDITORÍA: …INCUMPLIMIENTOS…, MONTO DEL HALLAZGO, CUANTIFICACIÓN DEL IMPUESTO, REFERENCIA PROBATORIA… FECHA Y NÚMERO DE COMPROBANTE CONTABLE O DOCUMENTO LEGAL Y ARTÍCULOS INFRINGIDOS… SÍ LOS INCUMPLIMIENTOS… YA FUERON SUBSANADOS…; f) CUALQUIER ANEXO ADICIONAL QUE A JUICIO TÉCNICO DEL AUDITOR CONSIDERE NECESARIO… LOS ANEXOS… DEBERÁN PRESENTARSE NUMERADOS EN FORMA PROGRESIVA EN EL MISMO ORDEN EN QUE SON MENCIONADOS." | The dictamen and report carry the anexos: a) income comparative — sales-ledger vs IVA-declared, and accounting vs declared; b) MONTHLY comparative analysis of the retentions on national-market sales — IVA retentions effected on the beneficiary per accounting records vs credited in the monthly declarations, and the same for ISR; c) SS/previsional cotizaciones comparative — monthly detail of recorded values vs paid per ISSS and AFP planillas, desglosada monthly into LABORAL and PATRONAL aportes; d) compras comparative — monthly local purchases + imports per the purchases ledger vs declared; e) audit-hallazgos (findings) detail — infringements, amount, tax quantification, evidentiary reference (date + accounting voucher/legal document number + infringed articles), whether already cured; f) any additional anexo the auditor deems necessary; anexos presented numbered progressively in the order mentioned | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Art. 59 pp.24-25 (EVID-267; txt PAGE 24-25; SOQ-30 print) |
| LB-010 | Reglamento (17b_), Art. 60: "LOS PERÍODOS QUE COMPRENDERÁ EL DICTAMEN…: a) PERÍODO SEMESTRAL, DEL UNO DE ENERO AL TREINTA DE JUNIO DEL AÑO QUE CORRESPONDA; b) PERÍODO SEMESTRAL, DEL UNO DE JULIO AL TREINTA Y UNO DE DICIEMBRE…; c) EN EL CASO DE LIQUIDACIÓN DE SOCIEDADES, CUYA APROBACIÓN DEL BALANCE FINAL… SE DA EN EL TRANSCURSO DEL SEMESTRE, EL PERÍODO DEL DICTAMEN COMPRENDERÁ DEL UNO DE ENERO HASTA LA FECHA DE LA APROBACIÓN DEL BALANCE, SI LA APROBACIÓN SE DA EN EL PRIMER SEMESTRE… EN CASO QUE LA APROBACIÓN SE REALICE EN EL SEGUNDO SEMESTRE…, DEL UNO DE JULIO HASTA LA FECHA DE LA APROBACIÓN." Art. 61: "EL AUDITOR NOMBRADO DEBERÁ PRESENTAR A LA DGII… Y A LA DIRECCIÓN, EL DICTAMEN CONJUNTAMENTE CON EL INFORME Y ANEXOS, EN LOS PLAZOS SIGUIENTES: a) EL… PERÍODO COMPRENDIDO DEL UNO DE ENERO AL TREINTA DE JUNIO, DEBERÁ PRESENTARSE A MÁS TARDAR EL DÍA TREINTA Y UNO DE OCTUBRE DEL AÑO EN CURSO; b) EL… PERÍODO… DEL UNO DE JULIO AL TREINTA Y UNO DE DICIEMBRE, DEBERÁ PRESENTARSE A MÁS TARDAR DENTRO DE LOS CINCO MESES SIGUIENTES DE FINALIZADO EL PERÍODO QUE SE DICTAMINA; c) PARA EL BENEFICIARIO PERSONA JURÍDICA… EN PROCESO DE LIQUIDACIÓN, …DENTRO DEL PLAZO DE DOS MESES SIGUIENTES CONTADOS A PARTIR DEL DÍA SIGUIENTE DE LA FECHA EN QUE SE APROBÓ EL BALANCE FINAL DE LIQUIDACIÓN." | Dictamen periods: a) semester 1 January-1 to June-30; b) semester 2 July-1 to December-31; c) society liquidation — if the final balance is approved in the first semester the period runs January-1 to the approval date, if in the second semester July-1 to the approval date. Deadlines: semester-1 dictamen AT LATEST October-31 of the current year; semester-2 dictamen at latest within the FIVE MONTHS following the end of the period dictated; liquidation cases within TWO MONTHS counted from the day after final-balance approval | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Arts. 60-61 p.26 (EVID-267; txt PAGE 26; SOQ-30 print) |
| LB-011 | Ley de Servicios Internacionales, Art. 22 f)-g): "f) RESPONDER ANTE LAS AUTORIDADES ADUANERAS, POR DIFERENCIAS DE LOS MÁRGENES ESTABLECIDOS EN LA NORMATIVA ADUANERA, EN TÉRMINOS DE CANTIDAD, NATURALEZA Y VALOR DE LAS MERCANCÍAS DECLARADAS, RESPECTO A LO EFECTIVAMENTE ARIBADO AL PARQUE DE SERVICIOS; NO OBSTANTE, LA RESPONSABILIDAD POR LOS FALTANTES, DERECHOS E IMPUESTOS, O MULTAS QUE RESULTEN, PODRÁ EXIGIRLE EL PAGO AL TRANSPORTISTA PRINCIPAL EN CASO DE COMPROBARSE LA RESPONSABILIDAD DE ESTE ÚLTIMO. g) RESPONDER POR EL PAGO DE IMPUESTOS DE SUS CLIENTES USUARIOS INDIRECTOS, EN CASO DE FALTANTES DE INVENTARIOS, EXTRAVÍOS, PÉRDIDAS Y MERMAS." Art. 46 b): "MANTENER EN UN MÍNIMO DE 500 METROS CUADRADOS LA EXTENSIÓN DEL INMUEBLE EN QUE REALIZA LA ACTIVIDAD ECONÓMICA, O EL MÍNIMO AUTORIZADO DE CONFORMIDAD CON EL ARTÍCULO 22, LITERAL a) DE ESTA LEY." | The distributor/logistics usuario directo must: f) answer to the customs authorities for differences in quantity, nature and value between the declared and the actually arrived goods — though liability for shortfalls, duties, taxes or fines may be charged to the principal CARRIER where the carrier's responsibility is proven; g) answer for the PAYMENT OF THEIR USUARIO-INDIRECTO CLIENTS' TAXES in case of inventory shortfalls (faltantes), misplacements (extravíos), losses (pérdidas) and shrinkage (mermas). Art. 46 b): MAINTAIN the premises at a minimum of 500 square meters (or the authorized lesser minimum) — the ongoing maintenance obligation | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 22 f)-g) p.14 + Art. 46 b) p.25 (EVID-262/264; 80_ txt PAGE 14, 25 — unchanged; 14_ re-keyed W19) |
| LB-012 | Ley de Servicios Internacionales, Art. 23 (as rewritten by D.L. 277-2013): BPO block: "…COMO USUARIOS DIRECTOS PARA PRESTAR SERVICIOS DE PROCESOS EMPRESARIALES…: a) NUEVA INVERSIÓN EN ACTIVOS POR UN MONTO NO MENOR A CIENTO CINCUENTA MIL DÓLARES… (US$150,000.00) EN LOS PRIMEROS SEIS MESES DE OPERACIONES, CORRESPONDIENTE A CAPITAL DE TRABAJO Y ACTIVOS FIJOS. b) OPERAR CON UN NÚMERO NO MENOR DE DIEZ PUESTOS DE TRABAJO PERMANENTES. c) POSEER CONTRATO MÍNIMO ESCRITO DE SEIS MESES. d) PRESENTAR UN PLAN DE NEGOCIOS." Médico-hospitalario block: "a) NUEVA INVERSIÓN EN ACTIVOS FIJOS POR UN MONTO MÍNIMO DE UN MILLÓN DE DÓLARES… (US$1,000,000.00) EN EL PRIMER AÑO… PARA TRATAMIENTO DE ENFERMEDADES CON INTERVENCIÓN QUIRÚRGICA O SIN ELLA, ASÍ COMO SERVICIOS DE MEDICINA GENERAL Y ODONTOLÓGICOS. b) …DIEZ PUESTOS…; c) …MÍNIMO CUATRO MIL METROS CUADRADOS CONSTRUIDOS DE LA UNIDAD HOSPITALARIA; d) PLAN DE NEGOCIOS; e) SEGURIDAD MÉDICO-HOSPITALARIA." Ancianos block: "a) …DOSCIENTOS CINCUENTA MIL DÓLARES… (US$250,000.00) EN EL PRIMER AÑO…; b) …DIEZ PUESTOS…; c) PLAN DE NEGOCIOS." Closing: "EN EL CASO DE NO CUMPLIR…, LA EMPRESA NO GOZARÁ DE LOS BENEFICIOS… CORRESPONDIENTE AL EJERCICIO FISCAL DEL INCUMPLIMIENTO. (1)" (pre-277 BPO first-year/one-year-contract and médico US$10,000,000.00 quirúrgico / US$3,000,000.00 no-quirúrgico [print "$3,000.000,00" sic] + fuera-del-metro + insured-patients predicates: SUPERSEDED — pre-277 state at EV14 EVID-262, historical provenance; centros thresholds = Art. 24-A, spe/01 LB-026/FR-190) | BPO usuario-directo requisitos (post-277): new asset investment ≥US$150,000 in the FIRST SIX MONTHS of operations (working capital + fixed assets); ≥10 permanent jobs; a written contract of at least SIX MONTHS; a business plan — on breach the enterprise does NOT enjoy the law's benefits for the FISCAL YEAR of the breach (closing sanction common to all three blocks); médico-hospitalario ≥US$1,000,000 first year + 10 jobs + 4,000 m² + plan + security norms; ancianos ≥US$250,000 + 10 jobs + plan (monitoring anchor; config rows owned by SV-SPE-FR-014, consumed by id) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 23 pp.14-16 (EVID-384; 80_ txt PAGE 14-16 — rewritten by 277-2013, re-verbatim W19) |
| LB-013 | Ley de Servicios Internacionales, Art. 47 k): "INTEGRAR EL PERSONAL DE SU EMPRESA CON UN NOVENTA POR CIENTO DE SALVADOREÑOS, POR LO MENOS. CUANDO POR EL NÚMERO DEL PERSONAL EL TANTO POR CIENTO DÉ POR RESULTADO UN NÚMERO MIXTO, LA FRACCIÓN SE TOMARÁ COMO UNIDAD. SIN EMBARGO, EN CIRCUNSTANCIAS ESPECIALES QUE EL MINISTERIO DE TRABAJO Y PREVISIÓN SOCIAL CALIFICARÁ, LOS PATRONOS PODRÁN SER AUTORIZADOS PARA EMPLEAR MÁS DE UN DIEZ POR CIENTO DE EXTRANJEROS, CON EL OBJETO DE OCUPAR A PERSONAS DE DIFÍCIL O IMPOSIBLE SUSTITUCIÓN POR SALVADOREÑOS, QUEDANDO OBLIGADOS LOS PATRONOS A CAPACITAR PERSONAL SALVADOREÑO BAJO LA VIGILANCIA Y CONTROL DEL CITADO MINISTERIO, DURANTE UN PLAZO NO MAYOR DE CINCO AÑOS." (Art. 47 closing: breach = infracciones graves) | Integrate the enterprise's personnel with at least NINETY PERCENT Salvadorans; when the percentage over the headcount yields a mixed number, the fraction is taken as a unit (rounding rule cited as printed). EXCEPTION: in special circumstances qualified by the Ministerio de Trabajo y Previsión Social (MinTrabajo), employers may be authorized to employ MORE than 10% foreigners, to occupy persons of difficult or impossible substitution by Salvadorans, remaining obliged to train Salvadoran personnel under that Ministry's vigilance for a term NOT longer than FIVE years. Breach of Art. 47 = grave infringements | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 47 k) p.27 (EVID-264; 80_ txt PAGE 27 — unchanged; 14_ re-keyed W19) |
| LB-014 | Ley de Servicios Internacionales, Art. 4 (inciso segundo): "…EN EL CASO DE LOS EXTRANJEROS NO DOMICILIADOS NO LES SERÁ APLICABLE LO ESTABLECIDO EN EL ARTÍCULO 158, INCISO SEGUNDO, DEL CÓDIGO TRIBUTARIO." Reglamento (17b_), Art. 65: "DE CONFORMIDAD A LO ESTABLECIDO EN EL INCISO SEGUNDO DEL ART. 4 DE LA LEY, LOS BENEFICIARIOS DE LA MISMA NO APLICARÁN LA RETENCIÓN PREVISTA EN EL INCISO SEGUNDO DEL ARTÍCULO 158 DEL CÓDIGO TRIBUTARIO." | Law Art. 4: every employee of a beneficiary working in a park/centro is subject to the corresponding taxes and fiscal obligations — EXCEPT that NON-DOMICILED FOREIGNERS are not subject to Código Tributario Art. 158 inciso segundo. Reglamento Art. 65: per the law's Art. 4 second inciso, the LAW'S BENEFICIARIES do not apply the retention provided in CT Art. 158 inciso segundo (incoming-services retention carve-out) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` + `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | 80_ Art. 4 p.3 + 17b_ Art. 65 p.27 (EVID-259/267; 80_ txt PAGE 3 — unchanged; 14_ re-keyed W19) |
| LB-015 | Ley de Servicios Internacionales, Art. 50 (incisos primero y tercero): "EN LOS CASOS QUE LA [DGA] O LA [DGII]… HAYAN DETERMINADO LA EXISTENCIA DE INFRACCIONES TRIBUTARIAS REITERADAS A LA LEGISLACIÓN ADUANERA O A LA LEGISLACIÓN TRIBUTARIA INTERNA, O HAYA TENIDO CONOCIMIENTO DE LA EXISTENCIA DE SENTENCIA PENAL FIRME POR VIOLACIÓN A DICHAS LEGISLACIONES; ASÍ COMO EN EL CASO EN QUE LAS AUDITORÍAS A QUE SE REFIERE EL LITERAL f) DEL ART. 47 DE ESTA LEY REFLEJEN INCONGRUENCIAS, LOS MINISTERIOS DE HACIENDA Y DE ECONOMÍA PODRÁN EXIGIR AL BENEFICIARIO RENDIR FIANZA PARA RESPONDER POR EL CUMPLIMIENTO DE LAS OBLIGACIONES DERIVADAS DE LOS BENEFICIOS RECIBIDOS." "EN CASO DE LA EXISTENCIA DE SENTENCIA FIRME Y DEFINITIVA POR LOS ILÍCITOS ESTABLECIDOS EN LA LEY CONTRA EL LAVADO DE DINERO Y ACTIVOS, POR PARTE DE LAS PERSONAS NATURALES O JURÍDICAS BENEFICIADAS POR ESTA LEY, EL JUEZ COMPETENTE DEBERÁ INFORMAR AL MINISTRO PARA QUE SE PROCEDA A LA REVOCATORIA DE LOS BENEFICIOS." | Where DGA/DGII fiscalización determines REPEATED tax/customs infringements, or knows of a firm criminal sentence for violating said legislation, or the Art. 47 f) audits reflect INCONGRUITIES, MH and MINEC MAY require the beneficiary to post a fianza (bond) answering for compliance with the obligations derived from the benefits received. Where a FIRM AND FINAL sentence exists for the ilícitos of the Ley Contra el Lavado de Dinero y Activos (AML law) against a benefited person, the competent judge informs the Ministro so the REVOCATION of the benefits proceeds | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 50 incisos 1º/3º pp.28-29 (EVID-264; 80_ txt PAGE 28-29 — unchanged; 14_ re-keyed W19) |
| LB-016 | Ley de Servicios Internacionales, Art. 63: "…BENEFICIADOS POR ESTA LEY… QUE AL MOMENTO DE LA ENTRADA EN VIGENCIA DE LA MISMA SE ENCUENTREN CALIFICADOS COMO USUARIOS, GOZANDO DE LOS BENEFICIOS… DE LA LEY DE ZONAS FRANCAS INDUSTRIALES Y DE COMERCIALIZACIÓN, PASARÁN DE PLENO DERECHO A GOZAR DE LOS BENEFICIOS… OTORGADOS POR LA PRESENTE LEY. LO MISMO APLICARÁ… EN DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO… SE EXCEPTÚAN… AQUELLOS SERVICIOS QUE ÚNICAMENTE PUEDEN PRESTARSE EN PARQUE DE SERVICIOS… EN EL CASO DE LOS DISTRIBUIDORES U OPERADORES LOGÍSTICOS DEBERÁN CUMPLIR CON… LOS LITERALES a), b) Y c) DEL ARTÍCULO 22… EN UN PLAZO MÁXIMO DE SEIS MESES CALENDARIO…" Art. 64: "LOS DESARROLLISTAS Y ADMINISTRADORES DE ZONAS FRANCAS… GOZARÁN DE LOS BENEFICIOS… EN LOS TÉRMINOS Y PLAZOS QUE LES HAN SIDO OTORGADOS POR LA LEY DE ZONAS FRANCAS… [NO] GOZARÁN DE LOS BENEFICIOS… DE LA PRESENTE LEY…" Art. 66: "LOS USUARIOS DIRECTOS AUTORIZADOS CONFORME A LAS DISPOSICIONES DE LA MISMA, QUE SE INSTALEN EN ZONAS FRANCAS AUTORIZADAS…, SE CONSIDERARÁN COMO SI ESTUVIESEN INSTALADAS EN UN PARQUE DE SERVICIOS." | Transitorias: Art. 63 — persons qualified as ZF usuarios at the law's entry into force who render LSI services pass DE PLENO DERECHO (by full right) to the LSI benefits (DPA kin included; services that can ONLY be rendered in a parque excepted per Art. 6; distributors/logistics operators had a maximum SIX CALENDAR MONTHS to comply with Art. 22 a)-c)); Art. 64 — ZF desarrollistas/administradores rendering benefited services inside the zona keep their ZF benefits and do NOT enjoy the LSI benefits for those activities; Art. 66 — LSI usuarios directos installed in an authorized zona franca are considered AS IF installed in a parque de servicios | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Arts. 63/64/66 pp.31-32 (EVID-264; 80_ txt PAGE 31-32 — unchanged; 14_ re-keyed W19) |

## 3. Functional Requirements

### 3.1 LSI exemption shapes — open-ended D15 rows (80_ Arts. 14/17/21/25)

- **SV-SPE-FR-042:** The system shall model every LSI tax benefit as a
  per-beneficiary dated exemption row on the Task-2 chassis entity
  `l10n_sv_special_regime.exemption_row` (SV-SPE-FR-023 consumed by id),
  keyed by the Task-1 profile (regime parque de servicios · centro de
  servicios × role × activity admission × *acuerdo* D.O. date —
  SV-SPE-FR-003 by id; NO location-track member: metro/fuera is a ZF-only
  dimension of SV-SPE-FR-022), with `row_shape` = **lsi_open_ended** for
  usuario-directo/centro ISR and municipal rows — `valid_from` = the
  statutory start (the *ejercicio impositivo* in which the beneficiary
  starts operations for Art. 21; the inicio de operaciones for Art. 25) and
  `valid_to` = NULL BY DESIGN, ended only by a CESSATION event
  (benefit-state end per SV-SPE-FR-015/017/018 by id — revocación,
  inactivity loss — stamped as the row end), or stamped per-ejercicio by a
  benefit-loss year (SV-SPE-FR-014 by id: the BPO breach year suppresses
  that year's effective exemption without ending the row) — with NO
  phase-down percentages and NO ladder windows EVER: this row shape is
  DISTINCT from the ZF/DPA ladders of SV-SPE-FR-024..028 and the two shapes
  are never unified (regime-distinctness invariant; the finite
  desarrollista/administrador rows of FR-043/FR-044 are the only LSI
  fixed-term rows, `row_shape` = lsi_fixed_term); benefit-state suspension
  spans yield a 0% effective exemption for the span with the open row's
  dates unchanged; the resolution anchor is the fiscal year with
  snapshot-on-write at each year's determination (D15/D16).
  (LB-003; LB-004; EVID-262)
- **SV-SPE-FR-043:** The system shall generate, for an LSI
  *desarrollista*, the FLAT fixed-term rows as printed — ISR total
  exemption for FIFTEEN years counted from the INICIO DE SUS OPERACIONES EL
  PARQUE (the parque-operations-start anchor, its own anchor kind), total
  municipal exemption ON THE ACTIVO of the empresa for TEN years from
  operations start, and total ITBIR exemption on acquisitions of real
  estate to be used in the incentivated activity — with the
  sociedad-plus-socios dividend exemption riding the ISR row and the
  PJ-socios exclusivity rule enforced per socio (same per-socio flag
  semantics as SV-SPE-FR-035, consumed by id — never restated).
  (LB-001; EVID-262)
- **SV-SPE-FR-044:** The system shall generate, for an LSI
  *administrador*, the same-shape fixed-term rows — ISR total exemption for
  FIFTEEN years from the start of operations FOR THE ADMINISTRATION
  activity, municipal total on the activo for TEN years — with: the
  both-roles rule (Art. 18: a person qualified as BOTH desarrollista and
  administrador gets BOTH row sets) as a per-beneficiary row-set
  multiplier, and the complementarias-activities exclusion recorded as an
  exclusion flag on the row set (operations of complementarias activities
  never resolve exempt).
  (LB-002; EVID-262)
- **SV-SPE-FR-045:** The system shall generate, for a *usuario directo*,
  the open-ended row set of Art. 21 — a) the LIBRE INTERNACIÓN open row
  (free entry into the parque, for the period operations are performed in
  the country, of machinery, equipment, tools, spare parts, accessories,
  furniture, office equipment and other goods necessary for the incentivated
  service activity) with the nine-category exception list as printed config
  rows carrying 14_ provenance — alimentación y bebidas; tabaco; bebidas
  alcohólicas; arrendamiento de vivienda; muebles y enseres del hogar;
  ARTÍCULOS DE LIMPIEZA (an LSI-only category vs the ZF list of
  SV-SPE-FR-036); artículos suntuarios o de lujo; vehículos; servicios de
  hotel — whose entry gate consumes the paid-tax-evidence inverting-gate
  mechanics of SV-SPE-FR-036 BY ID (DM definitiva a pago or paid-tax
  CCF/FCF, e-invoicing doc types by id), only the LIST rows being defined
  here; b) the ISR exemption row EXCLUSIVELY on income from the actividad
  incentivada, open-ended from the first EJERCICIO IMPOSITIVO of
  operations, with actividad-only segregation consumed from
  SV-TAX-FR-035/036 by id (kin of SV-SPE-FR-034, never restated); c) the
  municipal row on the activo, open-ended from the first EJERCICIO FISCAL;
  and the socio-level dividend exemption RIDING these rows (sociedad
  titular + socios; PJ-socios exclusivity) with NO ZF-style
  13th-ejercicio crossing — unlike SV-SPE-FR-035's 12-ejercicio window, the
  LSI socio-level exemption lasts exactly as long as the society's open
  rows (distinction made explicit, never unified).
  (LB-003; EVID-262)
- **SV-SPE-FR-046:** The system shall generate, for a *centro de
  servicios*, the Art. 25 row set — a) the FRANQUICIA ARANCELARIA TOTAL row
  (total exemption of tariff duties and the other import taxes on
  machinery, equipment, tools, spare parts, accessories, furniture, office
  equipment and other goods necessary for the incentivated activity) with
  the same nine-category exception list and paid-tax-evidence gate as
  FR-045 (list rows with 80_ Art. 25 provenance; gate mechanics consumed
  from SV-SPE-FR-036 by id); b) the ISR exemption row exclusively on
  incentivated-activity income, open-ended from the INICIO DE OPERACIONES;
  c) the municipal row on the activo, open-ended from the inicio de
  operaciones — with the socio-level exemption riding the rows as in
  FR-045.
  (LB-004; EVID-262)
- **SV-SPE-FR-047:** The system shall enforce the
  declaration-duty-survives-exemption guard as LSI-NATIVE text: no LSI
  exemption row ever suppresses or satisfies filing duties — Art. 14 a)
  (desarrollista), Art. 17 a) (administrador), Art. 21 b) (usuario directo)
  and Art. 25 b) (centro) each state expressly that the exemption does NOT
  release the beneficiary from presenting the respective tax declaration in
  each ejercicio/period of operation; the ZF-side twin guard is
  SV-SPE-FR-040 (consumed by id, never restated); the F-11 v20
  special-regime declaration remains a pointer surface (T2 LB-016; print
  not acquired — OQ family of `02`, no layout mechanics invented here).
  (LB-001; LB-002; LB-003; LB-004; EVID-262)

### 3.2 Local-market caps — 17b_ Art. 22 (dated reglamento parameters)

- **SV-SPE-FR-048:** The system shall implement the local-market service
  caps as dated config rows on `l10n_sv_special_regime.local_market_cap`
  keyed by activity-letter group with 17b_ provenance (reglamento-level
  dated parameters, values as printed): letters a) distribución
  internacional + b) operaciones internacionales de logística → cap 50% of
  the total servicios prestados; letters h) procesos empresariales + j)
  servicios financieros internacionales + c) centro internacional de
  llamadas → cap 40%; letters d) tecnologías de información + e)
  investigación y desarrollo → cap 30% — **W19 T3 (80_ Art. 8 inc. 3, as
  reformed by D.L. 277-2013): the LAW's local-market letter set is now
  {a), b), c), d), e), j)} — h) BPO was REMOVED (pre-277 set included h);
  the 17b_ 40%-cap row naming procesos empresariales is therefore
  INOPERATIVE for post-~19-feb-2013 facts (lex superior — the reglamento
  cannot authorize what the reformed law no longer permits; the cap row is
  retained as a dated pre-reform row; OQ-7), and the h-letter local-share
  monitor resolves 0%-allowed from the reform date (dated rows both sides
  of ~19-feb-2013)**; the measurement basis being VENTAS
  (sales) effected during each year (17b_ Art. 58.e.9.iii), never service
  counts; letters f)/g)/i) carry NO printed cap (empty config slots, no
  defaults invented); the caps operationalize the 17b_ Art. 21 rule that
  services must be destined to exportación (the export test itself owned by
  `05_tan-iva-interface.md` by id) with part of the service allowed into
  the national market up to the cap; the resolution anchor is the year with
  snapshot-on-write, and the fiscal-year measurement basis is the labeled
  SOQ-38 working assumption (OQ-2).
  (LB-005; LB-008; EVID-265/267; EVID-383 W19 T3)
- **SV-SPE-FR-049:** The system shall track the three cap-exclusion
  categories separately from the local-share numerator, each on its own
  ledger tag: i) services from operaciones de ACOPIO PARA EXPORTACIÓN of
  mercancías de libre circulación; ii) ALMACENAMIENTO of mercancías
  nacionales y nacionalizadas; iii) mercancías coming from a CLIENTE
  RESIDENTE EN EL EXTRANJERO for re-exportación, billed by its FILIAL
  RESIDENTE EN EL PAÍS — as printed, applicable to the 50% group's
  percentages (the print ties the exclusion paragraph to literal a); no
  other exclusion is inferred).
  (LB-005; EVID-265)
- **SV-SPE-FR-050:** The system shall run an annual local-share monitor:
  per year and per capped letter group, compute local ventas ÷ total ventas
  of the group's services (FR-049 exclusions out of the numerator), store
  the result as a dated computed row snapshotted on the year's
  determination, and raise a CAP-BREACH ALERT when the share exceeds the
  group's cap row — the alert flags the beneficiary record and sets the
  dictamen Art. 22-percentage flag consumed by the FR-053 checklist; the
  corpus prescribes NO consequence mechanics for a cap breach (no
  benefit-loss text, no per-operation blocking) — none are invented; the
  sanction-facing surfaces live in `07_obligations-reporting-sanctions.md`
  by id (breach consequence + excess carryover = OQ-2).
  (LB-005; LB-008; EVID-265/267)

### 3.3 Semestral auditor-dictamen family (80_ Art. 47 f); 17b_ Arts. 45-61)

- **SV-SPE-FR-051:** The system shall record the auditor-nomination
  lifecycle per beneficiary: the DGII-authorized independent audit firma
  with its Consejo de Vigilancia de la Profesión de Contaduría Pública y
  Auditoría and DGII authorization numbers (as consigned on the
  nombramiento); the annual nomination window = within the FIRST FIVE
  MONTHS of the year; the mid-first-semester qualifier window = a
  beneficiary authorized by MINEC during the first semester nominates
  within TWO MONTHS counted from the day after the authorization (for the
  second-semester dictamen); the nomination INFORMED to the DGII within 10
  *días hábiles* counted from the day after it is made (días-hábiles
  arithmetic consumed from SV-FREP-FR-202..204 by id); renuncia/remoción
  informed within 5 *días hábiles* with causes, a new auditor nominated
  within 10 *días hábiles* and that nomination informed within 10 *días
  hábiles*; annual ratification or replacement; the DGII-side registry and
  auditor-suspension mechanics (17b_ Arts. 50-55) are informational only
  (no emulation); the nomination formularios are DGII-specified and not in
  corpus — config slots, no defaults (OQ-6).
  (LB-006; LB-007; EVID-264/267)
- **SV-SPE-FR-052:** The system shall maintain the dictamen periods and
  deadlines as dated monitor rows: semester 1 = January 1 → June 30, due AT
  LATEST October 31 of the current year; semester 2 = July 1 → December 31,
  due within the FIVE MONTHS following the period's end; the liquidación
  special periods (final-balance approval in semester 1 → period January 1
  → approval date; in semester 2 → July 1 → approval date; due within two
  months from the day after approval) — each row carrying its period
  boundaries, due-date stamp and presented/not-presented state consumed by
  the FR-053 checklist's e.8 item.
  (LB-010; EVID-267)
- **SV-SPE-FR-053:** The system shall assemble the dictamen content
  checklist data per semester, one surface item per 17b_ Art. 58.e
  verification: e.1 operations conforming to the benefit *acuerdo*; e.2
  service income documented, registered in the books and correctly declared
  in ISR and IVA (with the legal-compliance and paid-tributes check for
  services rendered in the national customs territory); e.3 calculation and
  payment of the retention tributes per ejercicio or period, detailing any
  determined difference or omitted payment; e.4 VERIFICATION that
  local-market services had the 1% IVA and 1.5% ISR retentions of 14_
  Art. 8 APPLIED and that those retentions were registered, declared and
  credited — the VALUES and withholding-engine rows owned by
  `05_tan-iva-interface.md` + taxation/04 BY ID, this file only verifying
  their application (the dictamen verification hook); e.5 per-client,
  per-service-type physical-inventory verification data (distributors and
  logistics operators), consuming the register contract of
  `07_obligations-reporting-sanctions.md` by id; e.6 the SS cotizaciones
  (laboral + patronal) duly-paid verification data (payroll records by id);
  e.7 compras locales and importaciones effectively tax-free and destined
  to the benefited activity; e.8 original/modifying declarations examined
  (extemporaneous / not-presented flags); e.9.i structure-change inform
  duty; e.9.ii the ≥10 permanent jobs BPO requisito (consumes FR-056);
  e.9.iii the Art. 22 cap percentage by VENTAS (consumes FR-050); e.9.iv
  accounting records.
  (LB-006; LB-008; EVID-264/267)
- **SV-SPE-FR-054:** The system shall assemble the five mandatory dictamen
  ANEXOS (plus the free-form f slot) from the monthly ledgers: a) ingresos
  comparative — sales-ledger vs IVA declarations AND accounting records vs
  declared; b) monthly retention analysis for national-market sales — IVA
  (1%) and ISR (1.5%) retentions effected on the beneficiary per
  accounting records vs the amounts credited in the respective monthly
  declarations; c) monthly SS and previsional cotizaciones comparative —
  recorded vs paid per ISSS and AFP planillas, desglosada monthly into
  LABORAL and PATRONAL aportes; d) monthly compras comparative — local
  purchases + imports per the purchases ledger vs declared (with the
  primary-zone centros note: no customs introduction documents required
  there); e) hallazgos detail — infringements, amount, tax quantification,
  evidentiary reference (date + accounting voucher or legal document
  number + infringed articles) and subsanación state; anexos numerated
  progressively in the mentioned order.
  (LB-009; EVID-267)
- **SV-SPE-FR-055:** The system shall expose an exportable dictamen data
  pack per semester assembling the FR-053 checklist items and FR-054 anexos
  from the monthly ledgers, addressed to the audit firma — which remits the
  dictamen DIRECTLY to the DGII and MINEC (external-interface assumption:
  Odoo produces and exports the data pack; it does not generate, sign or
  transmit the dictamen itself); the carta-de-presentación twin-originals
  formality is recorded informationally.
  (LB-006; LB-009; EVID-264/267)
### 3.4 Requisito monitors — LSI-specific tracking (80_ Arts. 22/23/46)

- **SV-SPE-FR-056:** The system shall monitor the LSI qualification
  requisitos by consuming the Task-1 config rows SV-SPE-FR-013/FR-014 by id
  and logging measured values per period: the ≥500 m² area MAINTENANCE
  monitor (Art. 46 b: the premises stay at the minimum area or the
  MINEC+MH-authorized lesser minimum — exception flag consumed from T1's
  row); the BPO per-period monitors — **post-277 values (80_ Art. 23, W19
  T3): investment ≥US$150,000 within the FIRST SIX MONTHS of operations
  (working capital + fixed assets), ≥10 permanent jobs, ≥6-month written
  contract, business plan presented (pre-277 first-year/1-year-contract
  rows superseded — historical rows per D18)** —
  with the breach-year stamp consumed from SV-SPE-FR-014 (that ejercicio's
  benefits lost, the open rows otherwise unaffected); the médico
  thresholds (post-277 parque track: ≥US$1,000,000 first-year fixed-asset
  investment, 10 permanent jobs, ≥4,000 m² built hospital unit, business
  plan, security norms — the pre-277 $10,000,000.00/$3,000,000.00 [sic]
  tiers and location/insured-patients predicates superseded) and the
  ancianos track (≥US$250,000 + 10 jobs + plan)
  as admission-time checks logged against the T1 rows (the centros track's
  Art. 24/24-A monitors belong to spe/01 FR-190 — consumed by id); the DGA
  registration/access-code and 5-year manifiesto-copies custody duties are
  compliance surfaces owned by `07_obligations-reporting-sanctions.md` by
  id (pointers only here, never restated).
  (LB-011; LB-012; EVID-262/264 historical; EVID-384 W19 T3)

### 3.5 Usuario-indirecto consignment liability (80_ Art. 22 f)-g))

- **SV-SPE-FR-057:** The system shall provide a consignment-liability
  ledger surface for a usuario directo acting as distribuidor internacional
  or operador logístico: per usuario-indirecto client and per consignment
  lot, liability entries of kind faltante de inventario · extravío ·
  pérdida · merma, each computing and recording the CLIENT's goods taxes
  the distributor RESPONDS FOR (the distributor pays its usuario-indirecto
  clients' taxes on those events) with the statutory source stamped; plus
  the declared-vs-arrived márgenes difference surface (quantity, nature,
  value of declared vs effectively arrived goods) with the
  carrier-recourse flag — liability for shortfalls, duties, taxes or fines
  may be charged to the TRANSPORTISTA PRINCIPAL where its responsibility is
  proven (recourse state + proof reference per entry).
  (LB-011; EVID-262)

### 3.6 Staffing quota — 90% Salvadoran (80_ Art. 47 k))

- **SV-SPE-FR-058:** The system shall run a workforce-composition monitor
  per period consuming payroll records by id (payroll/05-06): the
  enterprise's personnel must integrate at least NINETY PERCENT Salvadorans,
  computed over the headcount with the printed mixed-number rule ("LA
  FRACCIÓN SE TOMARÁ COMO UNIDAD") recorded and applied as printed (no
  rounding direction invented beyond the text); the MinTrabajo exception
  track: dated exception rows authorizing MORE than 10% foreigners for
  persons of difícil o imposible sustitución por salvadoreños, each
  carrying the obligation to train Salvadoran personnel under MinTrabajo
  vigilance for a term not longer than FIVE years (horizon end date on the
  row); a breach feeds the infracción-grave classification → the Task-1
  state machine (SV-SPE-FR-017) by id; NOTHING SMM-priced is computed here
  (sanction values owned by `07` consuming payroll/02 by id).
  (LB-013; EVID-264)

### 3.7 CT-158-II carve-outs (17b_ Art. 65; 80_ Art. 4 inc. 2)

- **SV-SPE-FR-059:** The system shall suppress, on the vendor bills of an
  LSI beneficiary for services received, the Código Tributario Art. 158
  inciso-segundo retention: beneficiaries of the law DO NOT APPLY that
  retention (17b_ Art. 65 per 80_ Art. 4 inc. 2) — a suppression config
  flag on the beneficiary's vendor-bill retention application, resolved as
  a dated config row keyed to the regime profile; the CT-side retention
  machinery is consumed from taxation/04 (SV-TAX-FR-126 family) by id and
  never restated; the cross-check against the current 05_ CT text of the
  inciso is carried as OQ-4 (EVID-259 doubt).
  (LB-014; EVID-259/267)
- **SV-SPE-FR-060:** The system shall suppress the same CT Art. 158
  inciso-segundo treatment for NON-DOMICILED FOREIGN EMPLOYEES of a
  beneficiary working in a parque or centro (80_ Art. 4 inc. 2 — the law's
  own carve-out text): a flag on the non-domiciled-foreign-person records
  feeding the payroll/vendor retention resolution, while every OTHER
  employee of the beneficiary remains fully subject to the corresponding
  taxes and fiscal obligations (Art. 4 inc. 1 — no exemption invented for
  them); same OQ-4 cross-check.
  (LB-014; EVID-259)

### 3.8 Fianza + AML-conviction revocation link (80_ Art. 50)

- **SV-SPE-FR-061:** The system shall record the fianza requirement event:
  when DGA/DGII fiscalización determines REITERADAS tax/customs
  infringements, or a firm criminal sentence for violating said legislation
  is known, or the Art. 47 f) audits REFLECT INCONGRUITIES (the dictamen
  link), MH + MINEC MAY require the beneficiary to render a fianza
  answering for compliance with the obligations derived from the benefits
  received — recorded as a dated compliance event with cause class
  (reiterated_infractions · penal_sentence · audit_incongruities),
  resolution reference and an amount config slot with NO shipped default
  (the statute fixes no amount).
  (LB-015; EVID-264)
- **SV-SPE-FR-062:** The system shall implement the AML-conviction
  revocation link as a state-transition trigger: a firme y definitiva
  sentence for the ilícitos of the Ley Contra el Lavado de Dinero y
  Activos against a benefited person (natural or jurídica) — the competent
  judge informing the Ministro — drives the Task-1 benefit-state machine to
  revocada (reason art50_aml_conviction; SV-SPE-FR-015 by id), which stamps
  the cessation event on every open/fixed row of FR-042; the
  AML-conviction surface itself is consumed from commercial-legal by id
  (never restated here); the SAME article's SS-payment-breach
  3-month-suspension / reincidencia-revocation twin is owned by
  `07_obligations-reporting-sanctions.md` by id (pointer only).
  (LB-015; EVID-264)

### 3.9 ZF→LSI migration transitorias (80_ Arts. 63/64/66)

- **SV-SPE-FR-063:** The system shall record the ZF→LSI migration
  transitorias as per-case config with ZERO transition mechanics (SOQ-42):
  i) Art. 63 — persons qualified as ZF usuarios (or DPA kin) at the LSI's
  entry into force who render LSI services pass DE PLENO DERECHO to the
  LSI benefits (services renderable ONLY in a parque excepted per Art. 6;
  distributors/logistics operators carried a 6-calendar-month window to
  meet Art. 22 a)-c)) — the migration is a regime-profile transition
  stamping the LSI row set, whose benefit-START computation is
  corpus-silent: a per-case config slot (OQ-3), no default computed; ii)
  Art. 64 — ZF desarrollistas/administradores rendering benefited services
  inside the zona keep their ZF benefits and get NO LSI benefits for those
  activities (dual-regime exclusion flag); iii) Art. 66 — LSI usuarios
  directos installed in an authorized zona franca are treated AS IF
  installed in a parque de servicios (parque-equivalent location
  discriminator feeding FR-042's key and the clock surfaces of `04` by id).
  (LB-016; EVID-264)

## 4. Data Model

Layer semantics: all entities are Odoo-native config/ledger rows on the
Task-1 regime profile (wave default `odoo`; see §5). The dictamen data pack
is an Odoo export consumed by an EXTERNAL audit firma (external-interface
assumption — no dictamen generation/transmission surface). Cap values,
deadlines and quotas are code-text values as printed (SOQ-30 watch), stored
as dated rows with instrument provenance, never constants. CSV sidecar
evaluated per plan: the cap matrix is 3 rows and the checklist a fixed
Art. 58/59 structure — §4 config rows suffice and NO sidecar ships
(default none; judgment noted in the task report).

**LSI exemption rows (on the T2 chassis `l10n_sv_special_regime.exemption_row`):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.exemption_row | row_shape | select | lsi_open_ended (usuario directo/centro ISR + municipal + libre internación/franquicia) · lsi_fixed_term (desarrollista/administrador) — NEVER the ZF ladder shapes of `02` | FR-042..046 |
| l10n_sv_special_regime.exemption_row | anchor_kind · anchor_date | select · date | first_ejercicio_operations (Art. 21) · inicio_operaciones (Art. 25) · parque_operations_start (Art. 14/17) | FR-042..046 |
| l10n_sv_special_regime.exemption_row | valid_to · cessation_event | date-null · select | null by design (open); ended by revocación · inactivity_loss (SV-SPE-FR-015/017/018 by id); AML = art50_aml_conviction | FR-042, FR-062 |
| l10n_sv_special_regime.exemption_row | benefit_loss_ejercicios | year list | BPO breach years stamped off the effective exemption (SV-SPE-FR-014 by id) — rows NOT ended | FR-042, FR-056 |
| l10n_sv_special_regime.exemption_row | socio_level_rides | boolean | LSI socio-level exemption rides the society's rows; PJ-socios exclusivity flag (no 13th-ejercicio crossing — distinct from SV-SPE-FR-035) | FR-043, FR-045, FR-046 |

**LSI exception-goods list rows (on the T2 entity `l10n_sv_special_regime.exception_good`):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.exception_good | category (LSI rows) | select + provenance 14_ | nine categories as printed incl. articulos_de_limpieza (LSI-only vs the ZF list); gate mechanics consumed from SV-SPE-FR-036 by id | FR-045, FR-046 |
**Local-market caps (l10n_sv_special_regime.local_market_cap / .local_share_log):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.local_market_cap | letter_group · cap_percent | select · percent | ab_distribucion_logistica: 50 · hjc_bpo_financieros_callcenter: 40 · de_ti_investigacion: 30 — of total servicios prestados; f/g/i = empty slots (no printed cap); W19 T3: the h-letter 40% row is INOPERATIVE for post-~19-feb-2013 facts (80_ Art. 8 removes h) from the local-market set — dated pre-reform row retained; OQ-7) | FR-048 |
| l10n_sv_special_regime.local_market_cap | measurement_basis · valid_from · provenance | char · date · char | ventas per año (17b_ Art. 58.e.9.iii); instrument = 17b_ Art. 22 as printed (SOQ-30); fiscal-year assumption labeled (OQ-2) | FR-048, FR-050 |
| l10n_sv_special_regime.local_market_cap.exclusion | kind | select | acopio_exportacion_libre_circulacion · almacenamiento_nacional_nacionalizado · foreign_client_reexport_local_filial | FR-049 |
| l10n_sv_special_regime.local_share_log | fiscal_year · local_ventas · total_ventas · share · cap · breach | year · monetary · monetary · percent · percent · boolean | dated computed row per group per year, snapshot-on-write; breach ⇒ alert + dictamen flag (FR-053 e.9.iii feed) | FR-050 |

**Auditor-dictamen surfaces (l10n_sv_special_regime.auditor_nomination / .dictamen_period / .dictamen_anexo):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.auditor_nomination | firm · authorization_refs | m2o partner · char×2 | Consejo de Vigilancia + DGII authorization numbers as consigned | FR-051 |
| l10n_sv_special_regime.auditor_nomination | window_kind · nominated_on · inform_due_on | select · date · date | annual_first_5_months · mid_first_semester_2m (from day after MINEC authorization) · replacement_10dh; DGII inform 10 días hábiles from day after (SV-FREP-FR-202..204 by id); renuncia/remoción 5/10 días hábiles | FR-051 |
| l10n_sv_special_regime.dictamen_period | semester · period_from · period_to · due_on · state | select · date · date · date · select | s1 (1-ene→30-jun, due 31-oct current year) · s2 (1-jul→31-dic, due +5 months) · liquidacion_s1/s2 (to balance-approval date, due +2 months); state presented/not_presented (e.8 feed) | FR-052 |
| l10n_sv_special_regime.dictamen_period.checklist | item · data_ref | select · config | e.1..e.9.iv per 17b_ Art. 58 (e.4 = 1%/1.5% retention-application verification hook — values owned by `05`/taxation-04 by id; e.5 per-client per-service-type inventory; e.6 SS cotizaciones; e.9.iii cap percentage) | FR-053 |
| l10n_sv_special_regime.dictamen_anexo | kind · order · data_ref | select · int · config | a ingresos comparative · b monthly retention analysis (IVA 1% / ISR 1.5%) · c monthly SS comparative laboral+patronal (ISSS/AFP planillas) · d compras comparative · e hallazgos · f auditor-free-form; progressive numbering as printed | FR-054, FR-055 |

**Requisito monitors + liability + staffing (l10n_sv_special_regime.* / T1 entities consumed):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.requisito.log (T1, consumed) | measured_value · period | monetary/int · date | area_m2 maintenance (Art. 46 b); BPO investment/jobs/contract per year; médico admission checks — logged against T1 rows SV-SPE-FR-013/014 by id | FR-056 |
| l10n_sv_special_regime.indirect_liability_entry | client · lot · kind | m2o · m2o · select | faltante_inventario · extravio · perdida · merma — the distributor answers for usuario-indirecto clients' goods taxes | FR-057 |
| l10n_sv_special_regime.indirect_liability_entry | taxes_due · carrier_recourse · proof_ref | monetary · boolean · char | márgenes differences surface; recourse against transportista principal when responsibility proven | FR-057 |
| l10n_sv_special_regime.staffing_composition | period · headcount · salvadoran_count · share · in_rule | date · int · int · percent · char | ≥90% rule; mixed-number clause recorded as printed; payroll records feed by id | FR-058 |
| l10n_sv_special_regime.staffing_exception | authorized_share · grounds · training_obligation_end | percent · char · date | MinTrabajo >10% foreigners authorizations (difícil/imposible sustitución); ≤5-year Salvadoran-training horizon | FR-058 |

**Carve-outs + fianza + migration (config rows / flags):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (vendor bill) | sv_spe_ct158ii_suppressed | boolean (dated config row) | LSI beneficiary incoming services: CT Art. 158 inciso-segundo retention NOT applied (17b_ Art. 65); taxation/04 rows by id | FR-059 |
| res.partner / hr.employee | sv_spe_nondomiciled_foreign | boolean | extranjeros no domiciliados of a beneficiary: same CT-158-II suppression (80_ Art. 4 inc. 2); all other employees fully taxed | FR-060 |
| l10n_sv_special_regime.fianza_event | cause_class · resolution_ref · amount_slot | select · char · monetary (no default) | reiterated_infractions · penal_sentence · audit_incongruities; statute fixes no amount | FR-061 |
| res.company (T1 state catalog, consumed) | sv_spe_state_reason (additions) | catalog additions | art50_aml_conviction (revocada trigger); art47k_staffing (grave-infracción feed to SV-SPE-FR-017) | FR-058, FR-062 |
| res.company | sv_spe_migration_origin | select + config | zf_de_pleno_derecho (Art. 63; benefit-start = per-case config slot, SOQ-42) · zf_desarrollista_no_lsi (Art. 64) · lsi_in_zf_parque_equivalent (Art. 66) | FR-063 |

## 5. Odoo Mapping

Layer semantics for this wave: the LSI regime is Odoo-native
(regime-profile config rows, dated exemption rows, monitors and ledger
surfaces) — every FR maps `odoo`; no SaaS rows (no DTE
generation/transmission introduced; the dictamen pack is an EXPORT consumed
by the external audit firma — external-interface assumption noted on
FR-055). Model names are stable across Odoo 17/18/19/20; no
version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-042 | odoo | l10n_sv_special_regime.exemption_row | row_shape, anchor_kind/date, valid_to-null, cessation_event | THE LSI open-row shape; key = T1 profile (FR-003 by id, NO location track — ZF-only dimension); suspension ⇒ 0% effective, dates unchanged; NEVER unified with FR-024..028 ladders |
| FR-043 | odoo | l10n_sv_special_regime.exemption_row | lsi_fixed_term desarrollista rows | ISR 15y + municipal 10y from parque-operations start + ITBIR; socio-level rides the row (PJ exclusivity via FR-035 semantics by id) |
| FR-044 | odoo | l10n_sv_special_regime.exemption_row | lsi_fixed_term administrador rows | 15y/10y from administration-activity start; both-roles ⇒ both row sets (Art. 18); complementarias exclusion flag |
| FR-045 | odoo | l10n_sv_special_regime.exemption_row + .exception_good | usuario-directo open rows + 9-category list (incl. artículos de limpieza) | gate mechanics = SV-SPE-FR-036 by id; segregation = SV-TAX-FR-035/036 by id; NO 13th-ejercicio dividend crossing (≠ FR-035) |
| FR-046 | odoo | l10n_sv_special_regime.exemption_row + .exception_good | centro rows incl. franquicia arancelaria total | same exception list/gate with Art. 25 provenance; anchor = inicio de operaciones |
| FR-047 | odoo | l10n_sv.isr.filing.duty (guard flag) | exemption-active never clears duty | LSI-native text Arts. 14/17/21/25; ZF twin = SV-SPE-FR-040 by id; F-11 v20 pointer only |
| FR-048 | odoo | l10n_sv_special_regime.local_market_cap | letter_group/cap_percent/measurement_basis | 50/40/30 as printed (17b_ provenance); VENTAS basis per 58.e.9.iii; f/g/i empty slots; fiscal-year assumption labeled (OQ-2) |
| FR-049 | odoo | l10n_sv_special_regime.local_market_cap.exclusion | kind | 3 exclusion categories tied to the a)-group paragraph as printed |
| FR-050 | odoo | l10n_sv_special_regime.local_share_log | share/cap/breach | annual monitor; breach ⇒ alert + dictamen flag; NO consequence mechanics invented (OQ-2) |
| FR-051 | odoo | l10n_sv_special_regime.auditor_nomination | windows/informs/authorization refs | días-hábiles via SV-FREP-FR-202..204 by id; DGII-side registry informational; formularios config-gap (OQ-6) |
| FR-052 | odoo | l10n_sv_special_regime.dictamen_period | semester/from/to/due_on/state | 31-oct / +5-months / liquidación +2-months as printed |
| FR-053 | odoo | l10n_sv_special_regime.dictamen_period.checklist | items e.1..e.9.iv | e.4 verifies 1%/1.5% APPLICATION (values = `05`/taxation-04 by id); e.5 inventory via 07's register by id; e.6 payroll by id |
| FR-054 | odoo | l10n_sv_special_regime.dictamen_anexo | kinds a..f, progressive order | assembled from monthly ledgers (sales/purchases/retention/SS feeds by id) |
| FR-055 | odoo | dictamen data-pack export | export surface | external-interface assumption: firma remits to DGII+MINEC directly; Odoo does not generate/sign/transmit the dictamen |
| FR-056 | odoo | l10n_sv_special_regime.requisito.log (T1 consumed) | measured values per period | T1 rows FR-013/014 by id; area maintenance Art. 46 b; DGA-registration/manifiesto-custody = 07 pointers |
| FR-057 | odoo | l10n_sv_special_regime.indirect_liability_entry | client/lot/kind/taxes/recourse | consignment liability ledger; carrier recourse per Art. 22 f) |
| FR-058 | odoo | l10n_sv_special_regime.staffing_composition(+.exception) | share/in_rule/exception rows | payroll records by id; mixed-number rule as printed; breach → grave feed (FR-017 by id); nothing SMM here |
| FR-059 | odoo | account.move | sv_spe_ct158ii_suppressed | beneficiary incoming-services CT-158-II suppression (17b_ Art. 65); taxation/04 SV-TAX-FR-126 family by id; OQ-4 cross-check |
| FR-060 | odoo | res.partner / hr.employee | sv_spe_nondomiciled_foreign | extranjeros no domiciliados carve-out (80_ Art. 4 inc. 2); other employees fully taxed; OQ-4 cross-check |
| FR-061 | odoo | l10n_sv_special_regime.fianza_event | cause_class/resolution_ref/amount_slot | MAY-require event; amount = config slot, NO default (statute fixes none) |
| FR-062 | odoo | res.company (T1 state machine consumed) | revocada trigger art50_aml_conviction | AML surface consumed from commercial-legal by id; SS-breach twin = 07 by id; cessation stamps FR-042 rows |
| FR-063 | odoo | res.company | sv_spe_migration_origin | de pleno derecho transition = per-case config slot (SOQ-42 — OQ-3); Art. 64 exclusion flag; Art. 66 parque-equivalent discriminator feeding `04` by id |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file (the 50/40/30 caps, 15/10-year windows, 5-month/2-month/31-oct/10-5-10
días-hábiles clocks, 90% quota, ≤5-year training horizon, 6-month Art. 63
window) are code-text values cited as printed under the SOQ-30 verification
watch (§2) and live as dated config rows with instrument provenance —
never constants; the per-beneficiary anchors are the acuerdo D.O. date
(profile key) and the operations-start ejercicio (row starts). Mid-year
go-live (D18): a migrating LSI company ingests its open rows, monitors and
dictamen-pack history as `is_historical` rows with original-period
semantics (tiered ingestion; no re-derivation). No hard gates beyond the
statutory state machine (D16 no-override: regime validity is never
overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a centro de servicios whose operations started in
  2024 with open ISR and municipal rows, when no cessation event occurs
  through 2034, then the rows remain active (`valid_to` null) with the
  exemption effective every ejercicio — and when a third-grave revocación
  is stamped 2035-06-01, then the cessation event stamps the row end at
  the resolution date and no later ejercicio resolves exempt (FR-042,
  FR-046; SV-SPE-FR-017 by id).
- **AC-002:** Given a logística (letter b) usuario with annual ventas
  local US$520,000 / total US$1,000,000 of its services (52%), when the
  annual local-share monitor runs, then a cap-breach alert fires against
  the 50% cap row and the dictamen Art. 22-percentage flag is set for the
  FR-053 checklist — with NO consequence mechanics applied (corpus-silent;
  OQ-2) (FR-048, FR-050).
- **AC-003:** Given semester 1 closed (January 1 → June 30), when the
  dictamen data pack is assembled, then the five anexos a)-e) build from
  the monthly ledgers — ingresos comparative, 1%/1.5% retention analysis,
  SS comparative laboral+patronal, compras comparative, hallazgos — with
  progressive numbering, and the period's due monitor shows October 31 of
  the current year (FR-052..055).
- **AC-004:** Given an LSI beneficiary entering a vendor bill for services
  received from a domestic provider, when the bill's retention application
  resolves, then the CT Art. 158 inciso-segundo retention is suppressed by
  the beneficiary carve-out flag and no such retention is booked
  (FR-059).
- **AC-005:** Given a desarrollista (parque operations start 2025) and a
  usuario directo (first ejercicio 2025) in the same parque, when their
  rows generate, then the desarrollista carries finite lsi_fixed_term rows
  (ISR 2025-2039, municipal 2025-2034) while the usuario carries
  lsi_open_ended rows — the two shapes never unified and neither ever
  taking a ZF ladder form (FR-042..045).
- **AC-006:** Given a BPO usuario below the ≥10 permanent jobs in 2027 but
  cured in 2028, when the requisito monitor runs, then 2027 is stamped as
  a benefit-loss ejercicio (effective exemption off for that year only)
  while the open rows continue and 2028 resolves exempt (FR-056;
  SV-SPE-FR-014 by id).
- **AC-007:** Given a distributor storing mercancías nacionales y
  nacionalizadas (exclusion category ii) with US$300,000 of such local
  ventas, when the annual local share computes, then those ventas stay out
  of the numerator and are reported on their exclusion tag (FR-049).
- **AC-008:** Given a beneficiary with 45 employees of whom 40 Salvadoran
  (88.9%), when the composition monitor computes, then the quota breach
  flags and feeds the infracción-grave classification to the Task-1 state
  machine (FR-058; SV-SPE-FR-017 by id) — with no SMM-priced value
  computed in this file.
- **AC-009:** Given a beneficiary authorized by MINEC on 2026-04-10 (mid
  first semester), when the nomination window computes, then the auditor
  must be nominated by 2026-06-11 (two months from the day after) and the
  DGII inform due date resolves via the días-hábiles engine within 10 días
  hábiles of the nomination (FR-051).
- **AC-010:** Given a consignment lot of a usuario indirecto showing a
  faltante at the physical inventory, when the liability entry records,
  then the client's goods taxes are computed on the consignment-liability
  ledger with the carrier-recourse flag unset until carrier responsibility
  is proven (FR-057).
- **AC-011:** Given a ZF-qualified service user passing de pleno derecho
  at the LSI's entry into force, when the regime-profile transition stamps,
  then the LSI open row set activates with benefit-start left as a per-case
  config slot and NO transition computation shipped (FR-063; SOQ-42/OQ-3).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-37 carried: the 1.5% ISR / 1% IVA retention values are dated 2007 (80_ Art. 8) — their ownership and withholding rows live in `05_tan-iva-interface.md` + taxation/04 by id; FR-053.e.4 only VERIFIES their application in the dictamen pack. Verify no later CT (Arts. 157/158 family) or Ley-ISR reform superseded them — cross-check vs 54_ + the 05_ CT text at implementation (EVID-261/EVID-259 doubts). | no | Takumi S7 (taxation cross-check) | open |
| OQ-2 | SOQ-38 carried: 17b_ Art. 22 cap measurement — base = VENTAS per año (dictamen Art. 58.e.9.iii), not service counts; straddle-year alignment and excess carryover are unstated — FR-048/FR-050 ship the fiscal-year basis as a LABELED working assumption; the corpus also prescribes NO consequence mechanics for a cap breach (EVID-265 gloss suggests Art. 23 benefit-year-loss kin — text absent) — none invented; sanction-side resolution belongs to `07`. | no | Takumi S7 (fiscalización watch) | open |
| OQ-3 | SOQ-42 carried: the ZF→LSI "de pleno derecho" transition (80_ Art. 63) — benefit-start computation for migrating ZF service users is corpus-silent (Art. 21 rows run from the first ejercicio of operations; the pre-LSI ZF operations' effect unstated); FR-063 ships a per-case config slot with ZERO transition mechanics. | no | Takumi S7 (config watch) | open |
| OQ-4 | CT-158-II cross-check (EVID-259 doubt): 80_ Art. 4 inc. 2 and 17b_ Art. 65 carve beneficiaries and non-domiciled foreign employees out of CT Art. 158 inciso segundo — the inciso's CURRENT content must be cross-checked against the 05_ CT text (taxation/04 LB-018 / SV-TAX-FR-126 anchor) at implementation to confirm exactly which retention is suppressed and that no post-2008 CT reform moved it. | no | Takumi S7 (taxation cross-check) | open |
| OQ-5 | SOQ-30 carried — **W19 T3 update: the LSI half RESOLVED — 80_ acquired (consolidated thru D.L. 277-2013; Arts. 5/6/8/23/24/24-A deltas folded; LBs re-keyed 14_→80_)**; remaining: post-2013 LSI traffic unverified (80_ tail) and the 17b_ reglamento beyond its 2008 print (W18 parity: text-identical); every LB cites as printed; re-verify the caps, dictamen deadlines and staffing quota before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-6 | DGII-side dictamen formalities: the auditor-nomination formularios ("BAJO LAS ESPECIFICACIONES QUE DISPONGA LA DGII", 17b_ Art. 48) and the registry/suspension mechanics of Arts. 50-55 are not in corpus — FR-051 records the clocks and authorization refs at evidence depth with the formularios as config slots, NO defaults; DGII-side registry is informational only. | no | Takumi S7 (sources watch) | open |
| OQ-7 | 17b_ Art. 22 b) cap row vs the reformed law (W19 T3, EV80/82 OQ-2): the 2008 reglamento still caps "PROCESOS EMPRESARIALES… 40%" (and Art. 58 e.4 verifies retentions "SEGÚN EL ART. 8 DE LA LEY") while 80_ Art. 8 (277-2013) REMOVES h) from the local-market and retention letter sets; working ruling: lex superior — the law's letter set {a,b,c,d,e,j} controls post-~19-feb-2013 facts, the reglamento's h-row retained as a dated pre-reform row; FR-048/FR-097/FR-098 encode the dated split; confirm at implementation (reglamento-reform watch). | no | Takumi S7 (fiscalización watch) | open |
