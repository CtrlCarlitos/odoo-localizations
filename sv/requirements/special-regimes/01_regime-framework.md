# SV — Special regimes — Regime framework: beneficiary model, roles, qualification and breach states

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes); W19 T3 re-verification (80_/82_); W19 T4 fold-in (95_/96_/97_); W19 T5 historical note (90_); W24 T1 fold-in (107_/108_) |
| Updated | 2026-08-24 |

## 1. Purpose

This file defines the special-regimes chassis every other file of this wave
builds on: the territorial-regime taxonomy of the Ley de Zonas Francas
Industriales y de Comercialización (Industrial and Commercial Free-Trade Zones
Law, 12_) — *zona franca* (free zone, ZF) as extra-territorial for
import/export tributes vs *depósito para perfeccionamiento activo* (active
perfecting deposit, DPA) as a suspensive perfeccionamiento regime, two DISTINCT
regimes never unified — and the Ley de Servicios Internacionales
(International Services Law, LSI, 80_ as consolidated thru D.L. 277-2013;
14_ superseded) *parque de servicios* (services park,
multi-company) vs *centro de servicios* (services center, single company)
pair with its *usuario directo/indirecto/consignación/mercancías destinadas*
role definitions; the beneficiary profile that keys every D15 dated row of
the wave (regime × role × activity admission × location track × *acuerdo*
D.O. date); the authorization architecture (MINEC authorizes, MH through DGA
+ DGII watches; ONI capital registration) and the DGA institutional frame
(13_); the activity-admission catalogs (ZF SAC scope + Art. 6 negative list;
LSI letters a)-o) with per-letter scope predicates + co-located non-benefited
1)-11)); the qualification *requisitos* as dated config rows (ZF 17-A/19-A/
19-B; LSI 22/23/24-A — parque and centros tracks); the breach state machine
(revocación vs suspensión
with tributes payable and the benefit clock running; LSI third-grave
revocation; inactivity loss); the MINEC procedure clocks; the customs
*declarante*-role config (*agente aduanero* vs *apoderado especial aduanero*
vs self-declaration); and the 13-municipio *área metropolitana* stale-static
dated list that selects the metro/fuera location track — **W19 T3
re-verification: LSI LBs re-keyed 14_→80_ (277-2013 deltas folded: letters
a)-o), placement matrix, Art. 23/24/24-A requisito rewrite) + the ZF 82_
(D.L. 493-2025) tail gates (Arts. 2/10/11/17/18/19/28/44/46-A/54-B/54-I +
2-yr grace — FR-190..194 with spe/02/spe/07)**; **W19 T4: the
project-specific D.L.-incentive class** (95_ inmobiliarios en altura;
97_ biogás Acelhuate — instrument-keyed admission/benefit families whose
D15 dated rows live in `02` as FR-202/203; **W24: 108_ energía-eléctrica
acceso-universal joins as a CURRENT member** — instrument dl411_2025,
D.O. 181 T.448 26-sep-2025, vigencia 27-sep-2025 → 26-sep-2031, not
project-spent like 97_; FR-200 amended in place, dated rows = FR-204 in
`02`) **+ the 96_ D.L. 308-2025
Ley de Agentes Extranjeros identity row** (MIGOB RAEX transparency
registro — NOT an incentive regime; resolves the 54_ tail's EVID-167
pointer); **W19 T5: the 90_ D.L. 598-2020 spent-COVID-deferral
historical note** (LB-033 — awareness only, no operative FRs; the
54_-tail pointer for this instrument resolved, ~~the 201-2025/411-2025
acquisition negatives per SOQ-41 standing~~ **both acquired W22 as
107_/108_ — EVID-405/406; W24 T1: the fold-in landed — LB-034/035
identity rows + the FR-200 108_ class-member amendment here, FR-204 in
`02`, taxation FR-417..421 in the sibling files**).

It does **not** cover: the ZF/DPA exemption ladders and exception-goods gates
(`02_zf-exemption-schedules.md`); the LSI exemption shapes, local-market caps
and auditor dictamen (`03_lsi-regime.md`); the customs clocks
(`04_customs-clocks.md`); the TAN/IVA interface (`05_tan-iva-interface.md`);
DUCA/teledespacho declarations (`06_customs-declarations.md`); obligations,
DGA-facing reporting and SMM-priced sanctions (`07_obligations-reporting-
sanctions.md`); FOVIAL/COTRANS (`08_fovial-cotrans.md`). Those files consume
this one's beneficiary-profile and benefit-state model by FR id.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF = **12_**
(D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998; consolidated through
reform (8) D.L. 318-2013; content title "Ley de Zonas Francas Industriales y
de Comercialización" — the registry title "Ley de Zonas Francas y Recintos
Comerciales" is the D.L. 461-1990 law this decree replaces, fixed W13; W19 T3:
the 12_ parity ended 23-dic-2025 — the ZF tail = **82_**, D.L. Nº 493-2025,
D.O. N° 243 T.449 23-dic-2025, vigencia 8 días después → ~31-dic-2025 —
reformed Ley Arts. 2/10/11/17/18/19/28/44 + new 46-A/54-I + 54-B inc. 1º +
the 2-yr grace transitory; co-cite pattern 12_+82_ for the tail, 12_ for
unreformed text); LSI =
**80_** (Ley de Servicios Internacionales, D.L. Nº 431, 11-oct-2007, D.O. N°
199 T.377 25-oct-2007, as reformed by D.L. Nº 277-2013, D.O. N° 28 T.398
11-feb-2013 → vigencia ~19-feb-2013 for the reformed articles; INDICE
LEGISLATIVO consolidated print, 34 pp — **supersedes 14_ thru D.L. 277-2013**;
14_ = the 2007 base print, retained as identity/provenance record; W19 T3
re-key) + **17b_** (Reglamento D. Nº 131, 4-dic-2008, D.O.
N° 235 T.381 12-dic-2008; its Art. 22 local-market caps, dictamen regime and
inventory-register contract are consumed by `03_lsi-regime.md` — this file
cites the reglamento only where the framework itself needs it); DGA frame =
**13_** (D. Nº 903, 14-dic-2005, D.O.
Nº 8 T.370 12-ene-2006; consolidated through reform (2) D.L. 121-2012);
customs chassis = **74_** (D.L. Nº 529, 13-ene-1999, D.O. N° 23 T.342
3-feb-1999; consolidated through reform (4) D.L. 23-2012).

**SOQ-30 verification note (rides EVERY regime LB in this file and this
wave):** the regime consolidations ended 2012-2013 (12_ → D.L. 318-2013;
13_ → D.L. 121-2012; 74_ → D.L. 23-2012) — **W19 T3 (2026-08-22): the LSI
half RESOLVED — 14_ superseded by 80_ (LSI consolidated thru D.L. 277-2013;
LSI-side post-cutoff verified; LBs re-keyed 14_→80_ with 80_ pagination);
the 12_ parity ENDED by 82_ (D.L. 493-2025, vigencia ~31-dic-2025 — the ZF
tail co-cited 12_+82_)**; remaining unverified: post-2013 LSI traffic (80_
tail), post-2025 ZF traffic beyond 82_, and 13_/74_/17b_ beyond their
2012/2008 ends (SOQ-22-kin watch narrowed); article text is cited **as
printed**. Verbatim text below is copied from the W13 evidence files
(EVID-251..269) and the W19 T3 evidence (EVID-380..391, EV80/82) and, where
the evidence abbreviates, from the extraction txts
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt`,
`sv/.extractions/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf.txt`
(the LSI text of record; the superseded
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt` remains the
pre-277 provenance record),
`sv/.extractions/82_Reforma_Ley_ZF_DL493_DO_2025-12-23.pdf.txt` (forced-OCR
PSM 4 — cleaning declared in EV82 header),
`sv/.extractions/13_Ley_Organica_Aduanas.pdf.txt` and
`sv/.extractions/74_Ley_Simplificacion_Aduanera_D529.pdf.txt` (citable per
standing S3 ruling 25; page pointers = txt PAGE markers). **W19 T4 adds three
single-print current instruments (no consolidation layer; post-print reform
watch = SOQ-30 cadence kin): 95_ (D.L. 95-2024, D.O. 181 T.444 24-sep-2024,
vigencia 2-oct-2024), 97_ (D.L. 386-2025, D.O. 158 T.448 25-ago-2025,
vigencia publication-day), 96_ (D.L. 308-2025, D.O. 100 T.447 30-may-2025,
vigencia 7-jun-2025, forced-OCR PSM 4 — cleaning declared in EV95/96/97
header)** — 95_/97_ route their ISR-side effects through Ley ISR Art. 4.1
renta-no-gravable (54_ cited by id, never restated). **W19 T5 adds the
spent COVID transitory 90_ (D.L. 598-2020, D.O. N° 58 T.426 20-mar-2020,
vigencia publication-day, effects exhausted inside 2020 — LB-033
historical note, no operative FRs; forced-OCR PSM 4, cleaning declared
in the EV90-94 header).** **W24 T1 adds the two W22-acquired Salvadoran
decree instruments (native asamblea text layers — intra-word cleaning
declared in the EV header; post-print reform watch = SOQ-30 cadence kin):
107_ (D.L. 201-2025, D.O. N° 21 T.446 30-ene-2025, vigencia 7-feb-2025 —
LB-035 identity row; the operative airport seller-limb exemption =
taxation/03 SV-TAX-FR-418 by id) and 108_ (D.L. 411-2025, D.O. N° 181
T.448 26-sep-2025, vigencia 27-sep-2025 → 26-sep-2031 — LB-034
identity/instrument row; the FR-200 class-member amendment + the `02`
FR-204 dated family; ISR/IVA operative rows = taxation SV-TAX-FR-417/
419/420/421 by id).** D15 discipline:
every requisito value, threshold and list in this file is a dated config row
with instrument provenance — never a global constant.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 2 r): "ZONA FRANCA: ES EL ÁREA DEL TERRITORIO NACIONAL EN LA QUE SE PERMITE INGRESAR MERCANCÍAS QUE SE CONSIDERAN COMO SI NO ESTUVIESEN EN EL TERRITORIO ADUANERO NACIONAL, CON RESPECTO A LOS TRIBUTOS DE IMPORTACIÓN Y DE EXPORTACIÓN, PARA SER DESTINADAS SEGÚN SU NATURALEZA, A LAS OPERACIONES O PROCESOS PERMITIDOS POR LA PRESENTE LEY." Art. 2 h): "DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO O DPA: ES EL ÁREA DEL TERRITORIO NACIONAL SUJETA A UN TRATAMIENTO ADUANERO ESPECIAL, EN EL CUAL LAS MERCANCÍAS PUEDEN INGRESAR CON SUSPENSIÓN DE LOS TRIBUTOS A LA IMPORTACIÓN, PARA SER SOMETIDAS A UN PROCESO DE TRANSFORMACIÓN, ELABORACIÓN, REPARACIÓN U OTRO LEGALMENTE AUTORIZADO, PARA SU POSTERIOR REEXPORTACIÓN Y EN EL CUAL LOS BIENES DE CAPITAL PUEDEN PERMANECER INDEFINIDAMENTE…" | Free zone: the area of the national territory into which goods may enter that are considered as if NOT within the national customs territory with respect to import and export tributes, destined per their nature to the operations or processes permitted by this law. DPA: the area of national territory under special customs treatment in which goods may enter with SUSPENSION of import tributes to undergo transformation, elaboration, repair or other legally authorized process for subsequent RE-EXPORT, and in which capital goods may remain INDEFINITELY | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 2 h)/r) pp.2-4 (EVID-251; txt PAGE 2-4; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 2 d): "ÁREA METROPOLITANA: LA CONSTITUYEN LOS SIGUIENTES MUNICIPIOS: ANTIGUO CUSCATLÁN, SANTA TECLA, APOPA, AYUTUXTEPEQUE, CUSCATANCINGO, CIUDAD DELGADO, ILOPANGO, MEJICANOS, NEJAPA, SAN MARCOS SAN MARTÍN [sic], TONACATEPEQUE, SAN SALVADOR Y SOYAPANGO" | Metropolitan area: constituted by the following municipalities: Antiguo Cuscatlán, Santa Tecla, Apopa, Ayutuxtepeque, Cuscatancingo, Ciudad Delgado, Ilopango, Mejicanos, Nejapa, San Marcos San Martín [sic], Tonacatepeque, San Salvador and Soyapango | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 2 d) p.2 (EVID-251; txt PAGE 2; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 4: "EL ESTABLECIMIENTO, ADMINISTRACIÓN Y FUNCIONAMIENTO DE ZONAS FRANCAS SERÁ AUTORIZADO POR EL MINISTERIO DE ECONOMÍA. LA VIGILANCIA Y EL CONTROL DEL RÉGIMEN FISCAL DE DICHAS ZONAS CORRESPONDERÁ AL MINISTERIO DE HACIENDA, POR MEDIO DE LAS DIRECCIONES GENERALES DE ADUANAS E IMPUESTOS INTERNOS…" | The establishment, administration and operation of free zones is authorized by the Ministry of Economy (MINEC). Surveillance and control of the fiscal regime of said zones corresponds to the Ministry of Finance (MH) through the General Directorates of Customs (DGA) and Internal Taxes (DGII) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 4 p.7 (EVID-251; txt PAGE 7; SOQ-30 print) |
| LB-004 | Ley de Zonas Francas, Art. 5: "PODRÁN AMPARARSE A LA PRESENTE LEY, LAS PERSONAS NATURALES O JURÍDICAS, TITULARES DE EMPRESAS: a) QUE DESARROLLEN ZONAS FRANCAS DENOMINADOS DESARROLLISTAS; b) QUE ADMINISTREN ZONAS FRANCAS DENOMINADOS ADMINISTRADORES; c) QUE SE ESTABLEZCAN EN ZONAS FRANCAS DENOMINADOS USUARIOS; d) CUYOS ESTABLECIMIENTOS SEAN DECLARADOS DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO." | May take cover under this law natural or legal persons, holders of enterprises: a) that develop free zones, called desarrollistas (developers); b) that administer free zones, called administradores (administrators); c) that establish themselves in free zones, called usuarios (users); d) whose establishments are declared deposits for active perfecting (DPA titularities) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 5 p.7 (EVID-251; txt PAGE 7; SOQ-30 print) |
| LB-005 | Ley de Zonas Francas, Art. 3 (inciso primero + segundo): "PODRÁN ESTABLECERSE Y FUNCIONAR EN ZONA FRANCA EMPRESAS… QUE SE DEDIQUEN A: I. LA PRODUCCIÓN, ENSAMBLE O MAQUILA, MANUFACTURA, PROCESAMIENTO, TRANSFORMACIÓN O COMERCIALIZACIÓN DE BIENES INDUSTRIALES, COMPRENDIDOS EN EL CAPÍTULO 3 Y EN LOS CAPÍTULOS DEL 25 EN ADELANTE DEL SISTEMA ARANCELARIO CENTROAMERICANO, SAC, CON EXCEPCIÓN DE AQUÉLLOS QUE SE ENCUENTREN COMPRENDIDOS EN EL ARTÍCULO 6…; II. PESCA DE ESPECIES MARÍTIMAS PARA SER SOMETIDAS A TRANSFORMACIÓN INDUSTRIAL…; III. CULTIVO, PROCESAMIENTO Y COMERCIALIZACIÓN DE ESPECIES DE FLORA PRODUCIDA BAJO ESTRUCTURAS PROTEGIDAS EN INVERNADEROS Y LABORATORIOS…; IV. CRIANZA Y COMERCIALIZACIÓN DE ESPECIES DE ANFIBIOS Y REPTILES EN CAUTIVERIO…; V. DESHIDRATACIÓN DE ALCOHOL ETÍLICO." "…AQUÉLLAS NECESARIAS PARA LA PRODUCCIÓN… TALES COMO: DISEÑO, PINTADO, CORTE, ESTAMPADO, ACABADOS, SERIGRAFÍA, BORDADO, LAVADO, PLANCHADO, CONTROL DE CALIDAD, RECICLAJE Y REPARACIÓN. DICHAS ACTIVIDADES DE SERVICIOS SÓLO PODRÁN SER PRESTADAS ENTRE LOS BENEFICIARIOS DE LA PRESENTE LEY." | Enterprises established and operating in a free zone may engage in: I. production, assembly or maquila, manufacture, processing, transformation or commercialization of industrial goods comprised in Chapter 3 and Chapters 25 onward of the SAC, except those in Art. 6; II. fishing of marine species for industrial transformation; III. cultivation, processing and commercialization of flora produced under protected greenhouse and laboratory structures; IV. raising and commercialization of amphibian and reptile species in captivity; V. dehydration of ethyl alcohol. The connected services (design, painting, cutting, stamping, finishing, serigraphy, embroidery, washing, ironing, quality control, recycling and repair) may ONLY be provided AMONG the beneficiaries of this law | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 3 I-V pp.5-6 (EVID-252; txt PAGE 5-6; SOQ-30 print) |
| LB-006 | Ley de Zonas Francas, Art. 6: "NO PODRÁN ACOGERSE A LO ESTABLECIDO EN ESTA LEY, LAS PERSONAS… QUE SE DEDIQUEN A LAS ACTIVIDADES SIGUIENTES: a) EXPLORACIÓN, EXPLOTACIÓN, PROCESAMIENTO Y COMERCIALIZACIÓN DE GAS NATURAL, PETRÓLEO Y SUS DERIVADOS COMBUSTIBLES…; b) PRODUCCIÓN Y COMERCIALIZACIÓN DE CEMENTO Y CLINKER; c) COMERCIALIZACIÓN DE CHATARRA…; d) PRODUCTOS MINERALES… PROVENIENTES DE LA EXPLOTACIÓN DEL SUBSUELO SALVADOREÑO; e)… EXPLOSIVOS Y MATERIALES RADIOACTIVOS; f) LA PRODUCCIÓN O ALMACENAMIENTO DE MERCANCÍAS… CAUSANTES DE CONTAMINACIÓN…; g) …AZÚCAR, SUS SUSTITUTOS, DERIVADOS Y SUBPRODUCTOS…; h) …ALCOHOL DE CUALQUIER ORIGEN…, SALVO LO ESTABLECIDO EN EL ROMANO V, DEL Art. 3 DE ESTA LEY; i) …SACOS O COSTALES, DE FIBRAS SINTÉTICAS O ARTIFICIALES; j) SUMINISTRO DE ALIMENTOS PREPARADOS O NO…; k) IMPORTACIÓN DE MAQUINARIA Y EQUIPO CON FINES DE ARRENDAMIENTO. TAMPOCO PODRÁN ACOGERSE…: 1) LAS PERSONAS… A QUIENES SE LES HAYA SUSPENDIDO O REVOCADO LOS BENEFICIOS…; 2) LAS SOCIEDADES EN LAS QUE FIGUREN COMO DIRECTORES, REPRESENTANTES LEGALES… SOCIOS O ACCIONISTAS… QUE FUNGIERON EN TALES CARGOS… EN OTRAS SOCIEDADES A LAS CUALES LES FUERON SUSPENDIDOS O REVOCADOS LOS BENEFICIOS…; 3) CUANDO LAS ACTIVIDADES… CONLLEVEN UN OBJETO ILÍCITO…; 4) LAS PERSONAS… QUE… TENGAN OBLIGACIONES ADUANERAS Y/O TRIBUTARIAS FIRMES EN SEDE ADMINISTRATIVA PENDIENTES DE CUMPLIR." (numerals 1) and 2) inapplicable when the suspension/revocation was voluntary and not for infringements) | May NOT take cover under this law persons dedicated to: a) exploration/exploitation/processing/sale of natural gas, petroleum and fuel derivatives; b) cement and clinker; c) ferrous/non-ferrous scrap; d) subsuelo minerals; e) explosives and radioactive materials; f) polluting/health-harmful goods; g) sugar, substitutes, derivatives and byproducts (and goods incorporating them); h) alcohol of any origin EXCEPT Art. 3 V dehydration; i) synthetic-fiber sacks; j) prepared-food supply to benefited employees/enterprises; k) machinery import for leasing. Nor: 1) persons whose benefits were suspended/revoked; 2) societies whose directors/legal representatives/partners held such roles in other societies whose benefits were suspended/revoked; 3) illicit-object activities; 4) persons with firm pending customs/tax obligations (1-2 inapplicable to voluntary suspensions) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 6 a)-k) + 1)-4) pp.7-9 (EVID-252; txt PAGE 7-9; SOQ-30 print) |
| LB-007 | Ley de Zonas Francas, Art. 17-A: "…DEBERÁN CUMPLIR AL MENOS, CON UNO DE LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVO FIJO POR UN MONTO IGUAL O MAYOR A QUINIENTOS MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$500,000.00), ALCANZABLE EN LOS PRIMEROS DOS AÑOS DE OPERACIONES; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A CINCUENTA (50) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO DE OPERACIONES; c) OPERAR CON UN NÚMERO IGUAL O MAYOR A CINCO (5) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO DE OPERACIONES, EN EL CASO DE COMERCIALIZADORES." "CUANDO EL MINISTERIO DE ECONOMÍA DETERMINE QUE HA EXISTIDO INCUMPLIMIENTO DEL REQUISITO… LITERAL a)…, SE LE REVOCARÁ EL ACUERDO DE AUTORIZACIÓN AL USUARIO." "EN EL CASO DE INCUMPLIMIENTO DE LOS LITERALES b) Y c)…, SE LE SUSPENDERÁN LOS DERECHOS… HASTA QUE SUBSANE DICHO INCUMPLIMIENTO; POR TANTO, DEBERÁ PAGAR DURANTE DICHO PERÍODO LOS TRIBUTOS APLICABLES A LAS IMPORTACIONES QUE REALICE Y LOS DEMÁS IMPUESTOS RELACIONADOS." (invernaderos/laboratorios block: "…a) INVERSIÓN INICIAL… IGUAL O MAYOR A CIEN MIL DÓLARES… (US$100,000), EN EL PRIMER AÑO…; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A QUINCE (15) PUESTOS…; c) DISPONER UN ÁREA MÍNIMA DE CINCO MIL (5,000) METROS CUADRADOS, EN EL CASO DE INVERNADEROS Y DE MIL (1,000) METROS CUADRADOS, EN EL CASO DE LABORATORIOS; d) ESTRUCTURA ADMINISTRATIVA Y FINANCIERA FORMAL." — with the same revocación a)/suspensión b)-d) split; suspension block adds: "EL PLAZO DE LA SUSPENSIÓN NO INTERRUMPE EL CÓMPUTO DEL PLAZO TOTAL DE LOS BENEFICIOS.") | ZF usuario applicants must meet at least ONE of: a) initial fixed-asset investment ≥ US$500,000.00, attainable within the first two years of operations; b) ≥50 permanent jobs from the first year; c) ≥5 permanent jobs from the first year in the case of comercializadores (marketers). Breach of a) ⇒ the authorization acuerdo is REVOKED; breach of b)/c) ⇒ rights SUSPENDED until cured, paying during that period the tributes applicable to imports made and other related taxes. Greenhouse/laboratorio usuarios: a) ≥US$100,000 first-year investment; b) ≥15 permanent jobs; c) minimum area 5,000 m² (greenhouses) / 1,000 m² (laboratories); d) formal administrative and financial structure — same split, and the suspension period does NOT interrupt the total benefit term | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17-A pp.17-19 (EVID-255; txt PAGE 17-19; SOQ-30 print) |
| LB-008 | Ley de Zonas Francas, Art. 19-A: "…DPA… DEBERÁN CUMPLIR AL MENOS, UNO DE LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVO FIJO POR UN MONTO IGUAL O MAYOR A OCHOCIENTOS MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$800,000), ALCANZABLE EN LOS PRIMEROS DOS AÑOS DE OPERACIONES. NO SE CONTABILIZARÁ COMO INVERSIÓN INICIAL LA ADQUISICIÓN DE INFRAESTRUCTURA EXISTENTE; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A SETENTA Y CINCO (75) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO…; c) OPERAR CON UN NÚMERO NO MENOR A QUINCE (15) PUESTOS DE TRABAJO PERMANENTES…, EN EL CASO DE COMERCIALIZADORES." (same a)-breach revocación / b)-c)-breach suspensión split as 17-A) | DPA applicants must meet at least ONE of: a) initial fixed-asset investment ≥US$800,000 attainable within the first two years — acquisition of EXISTING infrastructure does not count as initial investment; b) ≥75 permanent jobs from the first year; c) ≥15 permanent jobs in the case of comercializadores (same revocación/suspensión enforcement split) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19-A pp.24-25 (EVID-255; txt PAGE 24-25; SOQ-30 print) |
| LB-009 | Ley de Zonas Francas, Art. 19-B: "LAS PERSONAS JURÍDICAS QUE SOLICITEN SER CALIFICADOS COMO DPA PARA DEDICARSE A ACTIVIDADES VINCULADAS CON ESPECIES DE ANFIBIOS Y REPTILES EN CAUTIVERIO, DEBERÁN CUMPLIR CON LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVOS FIJOS POR UN MONTO NO MENOR A CIEN MIL DÓLARES… (US$100,000), EN EL PRIMER AÑO…; b) OPERAR CON UN NÚMERO NO MENOR A QUINCE (15) PUESTOS DE TRABAJO PERMANENTES DESDE EL PRIMER AÑO…; c) ESTRUCTURA ADMINISTRATIVA Y FINANCIERA FORMAL." | Legal persons seeking DPA qualification for amphibian/reptile-in-captivity activities must meet: a) fixed-asset investment ≥US$100,000 in the first year; b) ≥15 permanent jobs from the first year; c) formal administrative and financial structure (Art. 3 III greenhouse/flora activities follow the 17-A seventh-inciso requirements) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19-B pp.25-26 (EVID-255; txt PAGE 25-26; SOQ-30 print) |
| LB-010 | Ley de Zonas Francas, Art. 39: "LA PERSONA… BENEFICIADA POR ESTA LEY QUE DEJARE DE OPERAR LA EMPRESA…, POR CAUSAS IMPUTABLES A ÉSTE, DURANTE UN PERÍODO DE DOCE MESES CONTINUOS, PERDERÁ LA CATEGORÍA DE USUARIO DE ZONA FRANCA O DE DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO, PREVIA AUDIENCIA AL INTERESADO POR EL TÉRMINO DE CINCO DÍAS HÁBILES… LA RESOLUCIÓN FINAL DEBERÁ PRONUNCIARSE DENTRO DE LOS DIEZ DÍAS POSTERIORES… LA DIRECCIÓN GENERAL DE ADUANAS DARÁ SEGUIMIENTO A TRAVÉS DE SU SISTEMA INFORMÁTICO, DEBIENDO DAR DE BAJA EN EL MISMO, A AQUELLAS EMPRESAS QUE INCURRIEREN EN TAL SITUACIÓN…" | A beneficiary that ceases operating its enterprise, for causes imputable to it, for a continuous TWELVE-MONTH period, loses its ZF-usuario or DPA category, after a five-días-hábiles hearing; final resolution within ten days thereafter. The DGA tracks this through its computer system and must deregister (dar de baja) affected companies in it | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 39 p.39 (EVID-258; txt PAGE 39; SOQ-30 print) |
| LB-011 | Ley de Zonas Francas, Art. 45: "EL MINISTERIO DE ECONOMÍA DEBERÁ RESOLVER EN UN PLAZO DE 25 DÍAS HÁBILES LA SOLICITUD DE CALIFICACIÓN COMO USUARIO DE ZONA FRANCA Y EN UN PLAZO DE 35 DÍAS HÁBILES LA SOLICITUD PARA OPERAR COMO DPA… EL ACUERDO RESPECTIVO DEBERÁ EMITIRSE EN UN PLAZO NO MAYOR A DIEZ (10) DÍAS HÁBILES…" (same-zone amendments inciso: usuarios not modifying their authorized activity, solvent with social-security institutions, requiring expansions/diminutions or relocation WITHIN the same zona franca, file a notarized note; the acuerdo issues within 10 días hábiles). Art. 48: "…EL MINISTRO DE ECONOMÍA DARÁ AUDIENCIA AL PRESUNTO INFRACTOR PARA QUE EN EL TÉRMINO DE CINCO DÍAS HÁBILES, POSTERIORES AL DE LA NOTIFICACIÓN, SE PRONUNCIE… LA RESOLUCIÓN FINAL DEBERÁ SER PRONUNCIADA EN EL TÉRMINO DE DIEZ DÍAS." Art. 49: "…PROCEDERÁ EL RECURSO DE REVOCATORIA… EL CUAL DEBERÁ INTERPONERSE POR ESCRITO EN UN PLAZO DE TRES DÍAS HÁBILES CONTADOS A PARTIR DE LA NOTIFICACIÓN RESPECTIVA… RESOLVERÁ EN UN PLAZO DE QUINCE DÍAS HÁBILES…" | MINEC must resolve a ZF-usuario qualification application within 25 días hábiles and a DPA application within 35 días hábiles (the MH opinion period included); same-zone amendment acuerdos issue within 10 días hábiles. Infringement procedure: five-días-hábiles audiencia, final resolution within ten days. Revocatoria recourse filed within three días hábiles of notification, resolved within fifteen días hábiles | `sv/sources/12_Ley_Zonas_Francas.pdf` | Arts. 45/48/49 pp.40-42 (EVID-258; txt PAGE 40-42; SOQ-30 print) |
| LB-012 | Ley de Servicios Internacionales, Art. 2: a) "PARQUE DE SERVICIOS: ÁREA DELIMITADA QUE FORMANDO UN SOLO CUERPO, SE ENCUENTRA CERCADA Y AISLADA, SIN POBLACIÓN RESIDENTE, DONDE LOS BIENES QUE EN ELLA SE INTRODUZCAN Y LOS SERVICIOS QUE SE PRESTEN, SE CONSIDERAN FUERA DEL TERRITORIO ADUANERO NACIONAL…"; b) "CENTRO DE SERVICIOS: ÁREA DELIMITADA Y AISLADA… QUE SE CONSIDERA FUERA DEL TERRITORIO ADUANERO NACIONAL, EN VIRTUD DE CONSIDERARSE COMO UNA ZONA QUE GOZA DE EXTRATERRITORIALIDAD ADUANERA… DONDE… SE AUTORIZA EL ESTABLECIMIENTO DE UNA EMPRESA…"; c) "USUARIO DIRECTO: PERSONA… AUTORIZADA PARA PRESTAR SERVICIOS EN EL PARQUE O CENTRO DE SERVICIO…"; d) "USUARIO INDIRECTO: PERSONA…, ACREDITADO COMO PROPIETARIO DE LAS MERCANCÍAS… DESTINADA A SER INTERNADA EN UN PARQUE DE SERVICIOS PARA SOMETARSE A LAS OPERACIONES DE DISTRIBUCIÓN O LOGÍSTICA INTERNACIONAL, A CARGO DE UN USUARIO DIRECTO CALIFICADO…"; e) "CONSIGNACIÓN DE MERCANCÍAS: ACTO JURÍDICO… CONFÍA LA CUSTODIA, MANEJO Y DISTRIBUCIÓN DE SUS MERCANCÍAS A UN USUARIO DIRECTO…"; f) "MERCANCÍAS DESTINADAS: SON AQUELLAS MERCANCÍAS QUE UNA PERSONA… NOTIFICA, ENVÍA, ENTREGA Y/O CONSIGNA AL USUARIO DIRECTO CALIFICADO…" | Services park: a delimited, fenced and isolated single-body area without resident population where introduced goods and provided services are considered OUTSIDE the national customs territory. Services center: a delimited isolated area enjoying customs extraterritoriality where the establishment of ONE enterprise is authorized. Usuario directo: person authorized to provide services in the park or center. Usuario indirecto: person accredited as owner of goods to be entered into a park for international distribution/logistics operations in charge of a qualified usuario directo. Consignación: the legal act by which goods custody, handling and distribution are entrusted to a usuario directo. Mercancías destinadas: goods notified, sent, delivered and/or consigned to the qualified usuario directo | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 2 a)-f) pp.2-3 (EVID-259; 80_ txt PAGE 2-3 — unchanged by 277-2013; 14_ re-keyed W19) |
| LB-013 | Ley de Servicios Internacionales, Art. 3: "PARA SER SUJETO A LOS BENEFICIOS…, LOS INVERSIONISTAS NACIONALES O EXTRANJEROS DEBERÁN REGISTRAR PREVIAMENTE EL CAPITAL, DE CONFORMIDAD A LA LEY DE INVERSIONES, EN LA OFICINA NACIONAL DE INVERSIONES, ONI, LA CUAL EMITIRÁ LA RESOLUCIÓN CORRESPONDIENTE EN UN PLAZO NO MAYOR A 5 DÍAS HÁBILES." Art. 7: "LA APLICACIÓN DE LA PRESENTE LEY CORRESPONDERÁ AL MINISTERIO DE ECONOMÍA. LA VIGILANCIA Y CONTROL EFECTIVO DEL RÉGIMEN ADUANERO Y FISCAL DE LOS PARQUES Y CENTROS DE SERVICIOS CORRESPONDERÁ AL MINISTERIO DE HACIENDA…" | To be subject to the benefits, national or foreign investors must PREVIOUSLY register capital per the Investment Law with the Oficina Nacional de Inversiones (National Investments Office, ONI), which issues the corresponding resolution within no more than 5 días hábiles. Application of the law corresponds to MINEC; effective surveillance and control of the customs and fiscal regime of parks and centers corresponds to MH | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Arts. 3/7 pp.3/7 (EVID-259; 80_ txt PAGE 3, 7 — unchanged; 14_ re-keyed W19) |
| LB-014 | Ley de Servicios Internacionales, Art. 5 (letters, scope fragments): a) "DISTRIBUCIÓN INTERNACIONAL: …ALMACENAMIENTO, ACOPIO, CONSOLIDACIÓN Y DESCONSOLIDACIÓN DE MERCANCÍAS DE TERCEROS… SIN TRANSFORMAR LA NATURALEZA DE LAS MISMAS…"; b) "OPERACIONES INTERNACIONALES DE LOGÍSTICA: …PLANIFICACIÓN, CONTROL Y MANEJO DE INVENTARIOS, SELECCIÓN, EMPAQUE, EMBALAJE, FRACCIONAMIENTO, CLASIFICACIÓN, ENVIÑETADO, ETIQUETADO, ROTULADOS, FACTURACIÓN, INSPECCIÓN DE CARGA Y OTRAS ACTIVIDADES QUE NO TRANSFORMEN SUSTANCIALMENTE LA NATURALEZA…"; c) "CENTRO INTERNACIONAL DE LLAMADAS… call center…"; d) "TECNOLOGÍAS DE INFORMACIÓN: …SERVICIOS PRESTADOS… A PERSONAS JURÍDICAS DOMICILIADAS FUERA DEL TERRITORIO NACIONAL, EN DISEÑO Y DESARROLLO DE SOFTWARE…"; e) "INVESTIGACIÓN Y DESARROLLO…"; f) "REPARACIÓN Y MANTENIMIENTO DE EMBARCACIONES MARÍTIMAS…"; g) "REPARACIÓN Y MANTENIMIENTO DE AERONAVES…"; h) "PROCESOS EMPRESARIALES… BPO's…"; i) "SERVICIOS MÉDICO-HOSPITALARIOS: …AQUELLOS SERVICIOS MÉDICOS GENERALES Y ESPECIALIZADOS EN EL TRATAMIENTO DE ENFERMEDADES QUE AMERITEN INTERVENCIÓN QUIRÚRGICA O SIN ELLA, INCLUSIVE LOS SERVICIOS ODONTOLÓGICOS, PRESTADOS POR UNA INSTITUCIÓN MÉDICO-HOSPITALARIA A PACIENTES CON DOMICILIO PERMANENTE FUERA DEL TERRITORIO SALVADOREÑO.(1)"; j) "SERVICIOS FINANCIEROS INTERNACIONALES…". NEW LETTERS (D.L. 277-2013): k) "REPARACIÓN Y MANTENIMIENTO DE CONTENEDORES: …SERVICIOS DE REPARACIÓN Y MANTENIMIENTO DE CONTENEDORES SECOS, REFRIGERADOS, EQUIPOS ESPECIALES E ISO TANQUES; DICHOS SERVICIOS DEBERÁN PRESTARSE A PERSONAS JURÍDICAS DEDICADAS AL TRANSPORTE INTERNACIONAL DE MERCANCÍAS, TANTO AÉREAS COMO MARÍTIMAS; LOS TRABAJOS… INCLUYEN: PINTURA, ENDEREZADO, LIMPIEZA O FUMIGACIÓN, ASÍ COMO OTROS SERVICIOS VINCULADOS A DICHA ACTIVIDAD.(1)"; l) "REPARACIÓN DE EQUIPOS TECNOLÓGICOS: …SERVICIOS DE REPARACIÓN DE EQUIPOS TECNOLÓGICOS TANGIBLES COMO COMPUTADORAS, CELULARES, TELEVISORES, CÁMARAS, IMPRESORES; O INTANGIBLES, RELACIONADOS A LA APLICACIÓN DE UN SISTEMA Y OTROS, PRESTADOS A PERSONAS JURÍDICAS DOMICILIADAS FUERA DEL TERRITORIO NACIONAL.(1)"; m) "ATENCIÓN A ANCIANOS Y CONVALECIENTES: …SERVICIOS PRESTADOS A PERSONAS CON DOMICILIO PERMANENTE FUERA DEL TERRITORIO NACIONAL, QUE DEMANDAN CUIDADOS ESPECIALES DE CUALQUIER NATURALEZA.(1)"; n) "TELEMEDICINA: …SERVICIOS PRESTADOS A DISTANCIA CONSISTENTES EN CUIDADOS A LA SALUD DE LAS PERSONAS, DESARROLLADOS A TRAVÉS DE UN MEDIO DE COMUNICACIÓN ELECTRÓNICA, REALIZADA POR PERSONAL CALIFICADO REGISTRADO PARA EJERCER EN EL PAÍS, CONSISTENTE EN ORIENTACIÓN MÉDICA POST CONSULTA E INTERCONSULTA ESPECIALIZADA DE RESULTADOS DE MEDIOS DE DIAGNÓSTICO Y ANÁLISIS, PRUEBAS DE LABORATORIO, ESTUDIOS PATOLÓGICOS E IMAGENOLÓGICOS, MANEJO DE HISTORIALES CLÍNICOS Y APOYO EN EL TRATAMIENTO, PRESTADOS A PERSONAS CON DOMICILIO PERMANENTE FUERA DEL TERRITORIO NACIONAL. SE EXCLUYE LA CONSULTA CLÍNICA.(1)"; o) "CINEMATOGRAFÍA: …SERVICIOS DE POSTPRODUCCIÓN REALIZADOS A UN MATERIAL GRABADO, QUE PUEDE INCLUIR LA SUBTITULACIÓN, ENTRE OTROS, PRESTADOS A PERSONAS JURÍDICAS DOMICILIADAS FUERA DEL TERRITORIO NACIONAL.(1)". (final inciso) "…PODRÁN INSTALARSE EN PARQUES DE SERVICIOS, SIN GOZAR DE LOS BENEFICIOS… QUEDANDO OBLIGADOS AL CUMPLIMIENTO DE LAS NORMAS TRIBUTARIAS NACIONALES VIGENTES…: 1) HOTELES. 2) LÍNEAS AÉREAS: 3) GENERACIÓN, SUMINISTRO Y DISTRIBUCIÓN DE ENERGÍA ELÉCTRICA. 4) COMUNICACIONES Y TELECOMUNICACIONES; EXCEPTO… CALL CENTERS Y LAS EMPRESAS TELEFÓNICAS QUE NO POSEAN REDES FIJAS PROPIAS… TERMINACIÓN DE TRÁFICO INTERNACIONAL ENTRANTE; SIN EMBARGO ESTAS ÚLTIMAS NO GOZARÁN DE LOS BENEFICIOS QUE CONFIEREN LOS ARTÍCULOS 21 Y 25…; 5) BANCARIOS, FINANCIEROS Y DE SEGUROS…; 6) TRANSPORTE…; 7) TURÍSTICOS… COURIES. 8) PROFESIONALES Y TÉCNICOS…; 9) SUMINISTRO DE ALIMENTOS…; 10) CUALQUIER TIPO O MECANISMO DE SEGURIDAD PRIVADA. 11) ARRENDAMIENTO DE CUALQUIER NATURALEZA, EXCEPTO EL PRESTADO POR LOS ADMINISTRADORES A LOS USUARIOS DIRECTOS…" | Benefited international-services activities: a) international distribution (third-party storage, gathering, consolidation/deconsolidation without transforming nature); b) international logistics operations (inventory planning/control/handling, selection, packing, packaging, fractioning, classification, labeling, invoicing, cargo inspection — no substantial transformation); c) international call centers; d) information technologies (software design/development TO legal persons domiciled outside the national territory); e) research and development; f) ship repair/maintenance; g) aircraft repair/maintenance; h) business processes (BPO); i) medical-hospital services — general and specialized treatment WITH or WITHOUT surgery, dental INCLUDED — provided to patients PERMANENTLY DOMICILED OUTSIDE Salvadoran territory (277-2013: was non-Central-America residents with general medicine and dental excepted); j) international financial services; NEW k) container repair/maintenance TO international-goods-transport legal persons (air and sea); l) technology-equipment repair (tangible computers/phones/TVs/cameras/printers or intangible system-related) TO foreign-domiciled legal persons; m) care of the elderly and convalescents TO persons permanently domiciled abroad; n) telemedicine (remote health care by practitioners registered to practice in SV; post-consultation guidance, specialized interconsultation of diagnostics/laboratory/pathology/imaging results, clinical-records handling, treatment support; CLINICAL CONSULTATION EXCLUDED) TO persons permanently domiciled abroad; o) cinematography postproduction (incl. subtitling) TO foreign-domiciled legal persons. Co-located NON-benefited 1)-11) (hotels, airlines, energy, communications except call centers/no-network international-traffic terminators — which also lose Arts. 21/25 benefits, banking/insurance, transport, tourism/courier, professional/technical, food supply, private security, leasing except administrator-to-usuario) operate under ordinary national tax law | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 5 a)-o) + 1)-11) pp.3-6 (EVID-381; 80_ txt PAGE 3-6 — reformed by 277-2013, re-verbatim W19) |
| LB-015 | Ley de Servicios Internacionales, Art. 6 (as reformed by D.L. 277-2013): "LAS PERSONAS NATURALES O JURÍDICAS A LAS QUE SE REFIEREN LOS LITERALES a), b), d), e), j), l), o) DEL INCISO PRIMERO DEL ARTÍCULO ANTERIOR, SOLO PODRÁN OPERAR EN PARQUES DE SERVICIOS DEBIDAMENTE CALIFICADOS DE CONFORMIDAD AL ARTÍCULO 7 DE ESTA LEY. LOS SERVICIOS A LOS QUE SE REFIEREN LOS LITERALES f) y g) QUE REQUIEREN CARACTERÍSTICAS FÍSICO-ESPACIALES PARTICULARMENTE PARA SU OPERACIÓN, PODRÁN OPTAR A DESARROLLAR SU ACTIVIDAD EN EL TERRITORIO ADUANERO NACIONAL, ASÍ COMO EN PUERTOS MARÍTIMOS Y AÉREOS, LOS CUALES DEBERÁN SER PREVIAMENTE CALIFICADOS COMO CENTRO DE SERVICIOS… DE IGUAL FORMA, EL SERVICIO REFERIDO EN EL LITERAL k) PODRÁ SER AUTORIZADO COMO CENTRO DE SERVICIOS CUANDO SE UBIQUE ALEDAÑO A UN PUERTO MARÍTIMO O AÉREO. EN EL CASO DE LAS LETRAS c), h), i), m), y n), PODRÁN OPERAR EN PARQUES DE SERVICIOS O CENTROS DE SERVICIOS. (1)" | Letters a), b), d), e), j), l) and o) may operate ONLY in parques de servicios; f) (ships) and g) (aircraft), requiring particular physical-spatial characteristics, may operate in the national customs territory and in maritime/air ports previously qualified as centros de servicios; k) (containers) may be authorized as a centro de servicios when located ADJACENT to a sea or air port; c) (call centers), h) (BPO), i) (medical-hospital), m) (elderly care) and n) (telemedicine) may operate in parks OR centers (277-2013: h)/i) moved from parque-only to the dual set; l)/o) joined the parque-only set) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 6 pp.6-7 (EVID-382; 80_ txt PAGE 6-7 — reformed by 277-2013, re-verbatim W19) |
| LB-016 | Ley de Servicios Internacionales, Art. 8 (second inciso, aeronautical export rule): "…TAMBIÉN SE CONSIDERA EXPORTACIÓN EL SERVICIO… g)… DEL ARTÍCULO 5…, PRESTADO A UNA PERSONA… DEDICADA A LA OPERACIÓN DE LÍNEAS AÉREAS QUE REALICEN VUELOS INTERNACIONALES, INDEPENDIENTE DE SU DOMICILIO Y DONDE UTILICE EL SERVICIO." | It is also considered exportation: the Art. 5 g) aircraft service provided to a person operating airlines making international flights, REGARDLESS of its domicile and where the service is used (the general export test is owned by `05_tan-iva-interface.md` by id) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 8 inc. 2 p.7 (EVID-383; 80_ txt PAGE 7 — inciso unchanged; 14_ re-keyed W19) |
| LB-017 | Ley de Servicios Internacionales, Art. 10: "GOZARÁN DE LOS BENEFICIOS… LAS PERSONAS… TITULARES DE EMPRESAS, QUE: a) DESARROLLEN PARQUES DE SERVICIOS O DESARROLLISTAS. b) ADMINISTREN PARQUES DE SERVICIOS O ADMINISTRADORES. c) SE ESTABLEZCAN Y OPEREN EN PARQUES DE SERVICIOS O USUARIOS DIRECTOS. d) SE ESTABLEZCAN Y OPEREN EN CENTROS DE SERVICIOS." | Benefit holders: enterprise holders that a) develop services parks (desarrollistas); b) administer services parks (administradores); c) establish and operate in services parks (usuarios directos); d) establish and operate in services centers | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 10 p.8 (EVID-259; 80_ txt PAGE 8 — unchanged; 14_ re-keyed W19) |
| LB-018 | Ley de Servicios Internacionales, Art. 22: "LOS USUARIOS DIRECTOS, ACTUANDO COMO DISTRIBUIDORES INTERNACIONALES U OPERADORES LOGÍSTICOS, DEBERÁN CUMPLIR CON LOS REQUISITOS SIGUIENTES: a) DISPONER DE UN MÍNIMO DE 500 METROS CUADRADOS EN PROPIEDAD O ARRENDAMIENTO; EN CASO EXCEPCIONAL, LOS MINISTERIOS DE ECONOMÍA Y DE HACIENDA PODRÁN AUTORIZAR… MENOR CANTIDAD DE METROS CUADRADOS…; b) REGISTRAR ANTE LA DIRECCIÓN GENERAL DE ADUANAS, PARA EFECTO DE RECIBIR EL CÓDIGO DE ACCESO A LOS SISTEMAS INFORMÁTICOS DE SERVICIO DE ADUANAS. c) MANTENER UN REGISTRO ELECTRÓNICO DE INVENTARIOS Y UN SISTEMA EN LÍNEA A DISPOSICIÓN DEL SERVICIO DE ADUANAS…; d) CONSERVAR LAS COPIAS DE LOS MANIFIESTOS DE CARGA CONSOLIDADA… POR UN PLAZO DE 5 AÑOS. e) PRESENTAR ANTE LA AUTORIDAD ADUANERA LOS BULTOS…; f) RESPONDER… POR DIFERENCIAS DE LOS MÁRGENES… EN TÉRMINOS DE CANTIDAD, NATURALEZA Y VALOR DE LAS MERCANCÍAS DECLARADAS…; g) RESPONDER POR EL PAGO DE IMPUESTOS DE SUS CLIENTES USUARIOS INDIRECTOS, EN CASO DE FALTANTES DE INVENTARIOS, EXTRAVÍOS, PÉRDIDAS Y MERMAS." | Usuarios directos acting as international distributors or logistics operators must: a) hold a minimum of 500 square meters owned or leased (MINEC+MH may exceptionally authorize less); b) register with the DGA to receive the access code to customs computer systems; c) keep an electronic inventory register and online system at the customs service's disposal, issuing warehouse entry/exit documents; d) keep consolidated-cargo manifest copies for 5 years; e) present the transported bultos to the customs authority and assign loading/unloading equipment and personnel; f) answer for quantity/nature/value differences between declared and actually arrived goods (recourse against the carrier when proven); g) answer for their usuario-indirecto clients' taxes in case of inventory shortfalls, losses, misplacements and shrinkage | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 22 a)-g) p.14 (EVID-262; 80_ txt PAGE 14 — unchanged; 14_ re-keyed W19) |
| LB-019 | Ley de Servicios Internacionales, Art. 23 (as rewritten by D.L. 277-2013), BPO block (parques): "…COMO USUARIOS DIRECTOS PARA PRESTAR SERVICIOS DE PROCESOS EMPRESARIALES…: a) NUEVA INVERSIÓN EN ACTIVOS POR UN MONTO NO MENOR A CIENTO CINCUENTA MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$150,000.00) EN LOS PRIMEROS SEIS MESES DE OPERACIONES, CORRESPONDIENTE A CAPITAL DE TRABAJO Y ACTIVOS FIJOS. b) OPERAR CON UN NÚMERO NO MENOR DE DIEZ PUESTOS DE TRABAJO PERMANENTES. c) POSEER CONTRATO MÍNIMO ESCRITO DE SEIS MESES. d) PRESENTAR UN PLAN DE NEGOCIOS." Médico-hospitalario block (parques): "a) NUEVA INVERSIÓN EN ACTIVOS FIJOS POR UN MONTO MÍNIMO DE UN MILLÓN DE DÓLARES… (US$1,000,000.00) EN EL PRIMER AÑO DE OPERACIONES PARA PROYECTOS CUYAS ACTIVIDADES SE DESTINEN A LA PRESTACIÓN DE SERVICIOS PARA TRATAMIENTO DE ENFERMEDADES CON INTERVENCIÓN QUIRÚRGICA O SIN ELLA, ASÍ COMO SERVICIOS DE MEDICINA GENERAL Y ODONTOLÓGICOS. b) OPERAR CON UN NÚMERO NO MENOR A DIEZ PUESTOS DE TRABAJO PERMANENTES. c) QUE LA EDIFICACIÓN O EDIFICACIONES… TENGA COMO MÍNIMO CUATRO MIL METROS CUADRADOS CONSTRUIDOS DE LA UNIDAD HOSPITALARIA. d) PRESENTAR UN PLAN DE NEGOCIOS. e) QUE LOS DISEÑOS… CUMPLAN CON LAS NORMAS Y ESPECIFICACIONES… EN MATERIA DE SEGURIDAD MÉDICO-HOSPITALARIA." Ancianos-y-convalecientes block (parques): "a) NUEVA INVERSIÓN EN ACTIVOS POR UN MONTO MÍNIMO DE DOSCIENTOS CINCUENTA MIL DÓLARES… (US$250,000.00) EN EL PRIMER AÑO DE OPERACIONES… b) OPERAR CON UN NÚMERO NO MENOR A DIEZ PUESTOS DE TRABAJO PERMANENTES. c) PRESENTAR UN PLAN DE NEGOCIOS." Closing: "EN EL CASO DE NO CUMPLIR…, LA EMPRESA NO GOZARÁ DE LOS BENEFICIOS… CORRESPONDIENTE AL EJERCICIO FISCAL DEL INCUMPLIMIENTO. (1)" (pre-277 BPO/1-year and médico $10M/$3M + fuera-del-metro + insured-patients predicates: superseded — pre-277 state at EV14 EVID-262, cited as historical provenance) | BPO usuario-directo applicants (parques): new asset investment ≥US$150,000 in the FIRST SIX MONTHS of operations (working capital + fixed assets), ≥10 permanent jobs, a written contract of at least SIX MONTHS, and a business plan — on breach the enterprise does NOT enjoy the law's benefits for the fiscal year of the breach. Medical-hospital (parques): fixed-asset investment ≥US$1,000,000 in the first year (single tier, surgical and non-surgical + general medicine and dental), ≥10 permanent jobs, ≥4,000 m² built of the hospital unit, business plan, medical-hospital security norms (the pre-277 location and insured-patients predicates are GONE). Elderly-care (ancianos y convalecientes, parques): ≥US$250,000 first-year investment, ≥10 permanent jobs, business plan | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 23 pp.14-16 (EVID-384; 80_ txt PAGE 14-16 — rewritten by 277-2013, re-verbatim W19) |
| LB-020 | Ley de Servicios Internacionales, Art. 52: "…a) LA INFRACCIÓN MENOS GRAVE SE SANCIONARÁ CON PREVENCIÓN ESCRITA… LA REINCIDENCIA… MULTA EQUIVALENTE A TRES SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA. b) LA INFRACCIÓN GRAVE… MULTA EQUIVALENTE A TREINTA SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA. EN CASO DE REINCIDENCIA… CUARENTA… AL PRESENTARSE UNA TERCERA INFRACCIÓN GRAVE SE DECRETARÁ LA REVOCATORIA DE LOS BENEFICIOS. c) LA INFRACCIÓN MUY GRAVE… SUSPENSIÓN TEMPORAL DE LOS BENEFICIOS, POR EL TÉRMINO DE TRES MESES. LA REINCIDENCIA… REVOCATORIA…" | Less-serious infringement: written prevención (warning); recidivism, a fine of three highest-amount monthly minimum wages (SMM de mayor cuantía). Serious: 30 SMM (40 on recidivism); upon a THIRD serious infringement the REVOCATION of benefits is decreed. Very serious: three-month temporary suspension of benefits; recidivism, revocation | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 52 p.29 (EVID-264; 80_ txt PAGE 29 — unchanged; 14_ re-keyed W19) |
| LB-021 | Ley de Servicios Internacionales, Art. 62: "SI ALGUNA PERSONA… ACOGIDA A LOS BENEFICIOS DE ESTA LEY DEJARA DE OPERAR, DURANTE UN PERÍODO DE TRES MESES CONTINUOS, DEBERÁN REVOCARSE LOS BENEFICIOS OTORGADOS…, SALVO FUERZA MAYOR O CASO FORTUITO, PREVIA APLICACIÓN DEL PROCEDIMIENTO… SI LA RESOLUCIÓN DETERMINA LA CANCELACIÓN DE LOS BENEFICIOS, LA DIRECCIÓN GENERAL DE ADUANAS PROCEDERÁ A INHABILITAR LOS ACCESOS AL SISTEMA INFORMÁTICO." | A beneficiary ceasing to operate for a continuous THREE-MONTH period must have its benefits revoked, save force majeure or fortuitous case, after the sanction procedure; if the resolution cancels the benefits, the DGA proceeds to DISABLE its computer-system accesses | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 62 p.31 (EVID-264; 80_ txt PAGE 31 — unchanged; 14_ re-keyed W19) |
| LB-022 | Ley Orgánica de la DGA, Art. 3: "LA DIRECCIÓN GENERAL DE ADUANAS ES EL ÓRGANO SUPERIOR JERÁRQUICO NACIONAL EN MATERIA ADUANERA, ADSCRITA AL MINISTERIO DE HACIENDA… FISCALIZAR Y RECAUDAR LOS DERECHOS E IMPUESTOS… ASÍ COMO CONTROLAR Y FISCALIZAR EL SUBSIDIO DEL GAS LICUADO DE PETRÓLEO." Art. 11: "…FORMARÁN PARTE DEL SERVICIO ADUANERO, LOS DEPÓSITOS DE ADUANAS, DELEGACIONES DE ADUANAS, ZONAS FRANCAS, DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO Y OTROS SIMILARES…" Art. 14: "LA DIRECCIÓN GENERAL, PODRÁ ESTABLECER DELEGACIONES DE ADUANAS EN LOS DEPÓSITOS, RECINTOS, ZONAS FRANCAS, PARQUES DE SERVICIOS Y OTROS LUGARES LEGALMENTE HABILITADOS…" | The DGA is the national superior hierarchical organ in customs matters, attached to MH, empowered to verify and collect duties and taxes. The customs service comprises customs deposits, customs delegations, FREE ZONES, DPAs and other similar; the DGA may establish customs delegations in deposits, precincts, free zones, SERVICES PARKS and other legally enabled places | `sv/sources/13_Ley_Organica_Aduanas.pdf` | Arts. 3/11/14 pp.2-3, 7, 8 (EVID-268; txt PAGE 2-3, 7, 8; SOQ-30 print) |
| LB-023 | Ley Orgánica de la DGA, Art. 36-A: "LA PERSONA NATURAL QUE SOLICITE LA AUTORIZACIÓN PARA ACTUAR COMO AGENTE ADUANERO, DEBERÁ ACREDITAR, ENTRE OTROS, LOS SIGUIENTES REQUISITOS: a) SER NACIONAL DE CUALQUIERA DE LOS ESTADOS PARTES; b) POSEER EL GRADO ACADÉMICO EN LICENCIATURA EN MATERIA ADUANERA; c) POSEER GRADO ACADÉMICO EN OTRAS DISCIPLINAS DE ESTUDIO, EN CUYO CASO… ACREDITAR COMO MÍNIMO DOS AÑOS DE EXPERIENCIA EN MATERIA ADUANERA; EN LOS CASOS… b) Y c)… LAS AUTORIDADES DE ADUANA PODRÁN PRACTICAR AL INTERESADO UN EXAMEN PSICOMÉTRICO." | A natural person requesting authorization to act as agente aduanero (customs agent) must, among others, accredit: a) nationality of any of the (CAUCA) States Parties; b) a licenciatura degree in customs matters, or c) a degree in other disciplines plus at least two years of customs experience; for b)/c) the customs authorities may administer a psychometric examination | `sv/sources/13_Ley_Organica_Aduanas.pdf` | Art. 36-A p.17 (EVID-268; txt PAGE 17; SOQ-30 print) |
| LB-024 | Ley de Simplificación Aduanera, Art. 9: "…PARA GARANTIZAR EL ACCESO GENERALIZADO AL TELEDESPACHO, LA PARTICIPACIÓN DE LOS AGENTES DE ADUANA O AGENTES ADUANEROS EN LA GESTIÓN DE LOS TRÁMITES ADUANEROS… SERÁ OPTATIVA PARA EL USUARIO, SIEMPRE QUE ÉSTE SEA UNA PERSONA JURÍDICA, QUIEN PODRÁ OBTENER UNA AUTORIZACIÓN DE LA DIRECCIÓN GENERAL PARA EFECTUAR POR SI MISMA SUS DECLARACIONES ADUANERAS, PARA LO CUAL DEBERÁ OTORGAR PODER DE REPRESENTACIÓN EN ESCRITURA PÚBLICA A FAVOR DE CUALQUIERA DE SUS EMPLEADOS QUE LA REPRESENTARÁ EN CALIDAD DE APODERADO ESPECIAL ADUANERO ANTE LAS ADUANAS DE LA REPÚBLICA, QUIENES SERÁN SOMETIDOS A UN EXAMEN DE SUFICIENCIA QUE VERSARÁ SOBRE MATERIAS ADUANERAS Y QUE PODRÁ COMPRENDER ADEMÁS PRUEBAS PSICOTÉCNICAS… UNA VEZ AUTORIZADO EL APODERADO ESPECIAL ADUANERO, LA PERSONA JURÍDICA PODERDANTE DEBERÁ RENDIR UNA FIANZA QUE SERÁ FIJADA POR LA DIRECCIÓN GENERAL… EL APODERADO ESPECIAL ADUANERO QUEDARÁ SUJETO… A LAS MISMAS DISPOSICIONES LEGALES QUE REGULAN… LA SUSPENSIÓN Y REVOCATORIA DE LA AUTORIZACIÓN PARA OPERAR DE LOS AGENTES DE ADUANA." | To guarantee generalized teledespacho access, the participation of customs agents in customs procedures is OPTIONAL for the user when the user is a persona jurídica, which may obtain DGA authorization to make its own customs declarations, granting a representation power in public deed (escritura pública) to any of its employees, who will represent it as apoderado especial aduanero (special customs attorney-in-fact) before the Republic's customs offices; they undergo a sufficiency examination on customs matters (possibly including psychometric tests). Once authorized, the granting legal person must post a bond (fianza) fixed by the DGA; the apoderado especial aduanero is subject to the same suspension/revocation rules as customs agents | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 9 pp.7-8 (EVID-269; txt PAGE 7-8; SOQ-30 print) |
| LB-025 | Ley de Simplificación Aduanera, Art. 5: "…DICHAS CONSULTAS SERÁN EVACUADAS POR LA AUTORIDAD ADUANERA A MÁS TARDAR DENTRO DE LOS QUINCE DÍAS HÁBILES SIGUIENTES A SU RECEPCIÓN, Y SÓLO SURTIRÁN EFECTO EN EL CASO CONCRETO ESPECÍFICAMENTE CONSULTADO; DICHO PLAZO PODRÁ SER AMPLIADO DE OFICIO POR UN PERÍODO IGUAL… LA PRESENTACIÓN DE LA CONSULTA NO SUSPENDE EL CUMPLIMIENTO DE LAS OBLIGACIONES TRIBUTARIAS Y NO TRIBUTARIAS ADUANERAS." Art. 5-A: "…LOS CRITERIOS O RESOLUCIONES ANTICIPADAS, SE ACEPTARÁN CUANDO SE PRESENTEN ANTES QUE SE REALICE LA IMPORTACIÓN DE LA MERCANCÍA EN CUESTIÓN, LOS CUALES CONSERVARÁN SU VALIDEZ POR TRES AÑOS, SIEMPRE Y CUANDO NO HAYAN CAMBIADO LAS CONDICIONES QUE FUNDAMENTARON SU EMISIÓN…" | Pre-declaration consultations by any person with legitimate interest are answered within fifteen días hábiles (extendable ex officio by an equal period), effective ONLY for the specific case consulted; filing does not suspend customs/tax obligations. Advance criteria or resolutions are accepted when presented before the importation of the goods in question and keep their validity for THREE YEARS provided the conditions underlying their issuance have not changed | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 5/5-A pp.3-4 (EVID-269; txt PAGE 3-4; SOQ-30 print) |
| LB-026 | Ley de Servicios Internacionales, Art. 24 (as rewritten by D.L. 277-2013), centros catalogue + general requisitos: "LAS PERSONAS… TITULARES DE EMPRESAS DEDICADAS A LA PRESTACIÓN DE SERVICIOS DE CENTROS INTERNACIONALES DE LLAMADAS, REPARACIÓN Y MANTENIMIENTO DE EMBARCACIONES MARÍTIMAS Y DE AERONAVES, PROCESOS EMPRESARIALES, MÉDICO-HOSPITALARIOS, REPARACIÓN Y MANTENIMIENTO DE CONTENEDORES, ATENCIÓN A ANCIANOS Y CONVALECIENTES, Y TELEMEDICINA PODRÁN OPERAR EN CENTROS DE SERVICIOS, PREVIO OTORGAMIENTO DE LOS BENEFICIOS…, DEBIENDO CUMPLIR LOS SIGUIENTES REQUISITOS: a) CONTAR CON LA AUTORIZACIÓN DE UBICACIÓN POR PARTE DE LA AUTORIDAD CORRESPONDIENTE. b) QUE LAS INSTALACIONES CUMPLAN CON CONDICIONES AMBIENTALES Y DE SEGURIDAD E HIGIENE OCUPACIONAL ADECUADAS. c) ORGANIZACIÓN ADMINISTRATIVA Y FINANCIERA FORMAL. d) EDIFICACIONES: i) ESTACIONAMIENTO DE VEHÍCULOS. ii) CONTAR CON SALIDAS DE EMERGENCIA. iii) CUALQUIER OTRA NECESARIA SEGÚN LA ACTIVIDAD A DESARROLLAR." + contenedores/embarcaciones/aeronaves centros outside a primary customs zone "DEBERÁN ASIGNAR UNA OFICINA PARA LA DELEGACIÓN ADUANERA… EL BENEFICIARIO DEBERÁ CONTRIBUIR CON EL PAGO DE LOS SERVICIOS Y DEL EQUIPO NECESARIO DE LA DELEGACIÓN ADUANERA CUANDO… LA DIRECCIÓN GENERAL DE ADUANAS LO REQUIERA." Art. 24-A (ADDED by 277-2013, centros per-activity): BPO "a) NUEVA INVERSIÓN… NO MENOR A DOSCIENTOS CINCUENTA MIL DÓLARES… (US$250,000.00) EN LOS PRIMEROS SEIS MESES… b) OPERAR CON UN NÚMERO NO MENOR A VEINTE PUESTOS DE TRABAJO PERMANENTES. c) POSEER CONTRATO MÍNIMO ESCRITO DE SEIS MESES. d) PRESENTAR UN PLAN DE NEGOCIOS."; médico "a) …DOS MILLONES DE DÓLARES… (US$2,000,000.00) EN EL PRIMER AÑO… b) …QUINCE PUESTOS… c) …MÍNIMO CUATRO MIL METROS CUADRADOS CONSTRUIDOS…; d) PLAN DE NEGOCIOS; e) SEGURIDAD MÉDICO-HOSPITALARIA"; ancianos "a) …QUINIENTOS MIL DÓLARES… (US$500,000.00) EN EL PRIMER AÑO… b) …QUINCE PUESTOS…; c) PLAN DE NEGOCIOS"; same ejercicio-loss closing | Centros de servicios (single-company track) qualification per the 277-2013 rewrite: the eight catalogued activities (call centers, ship repair, aircraft repair, BPO, medical-hospital, container repair, elderly care, telemedicine) operate in centros after MINEC grants the benefits, meeting the general requisitos (location authorization; environmental + occupational-safety/hygiene conditions; formal administrative and financial organization; buildings incl. parking and emergency exits) — container/ship/aircraft-repair centros OUTSIDE a primary customs zone must assign a customs-delegation office and contribute to its services/equipment when the DGA requires; per-activity requisitos of Art. 24-A: BPO ≥US$250,000 in the first six months + ≥20 permanent jobs + ≥6-month written contract + business plan; medical ≥US$2,000,000 first year + ≥15 jobs + ≥4,000 m² hospital unit + plan + security norms; elderly care ≥US$500,000 first year + ≥15 jobs + plan — breach loses that fiscal year's benefits (HIGHER thresholds than the parque equivalents of LB-019) | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Arts. 24/24-A pp.16-18 (EVID-384; 80_ txt PAGE 16-18 — 24 rewritten + 24-A added by 277-2013; W19 T3) |
| LB-027 | Reformas a la Ley de Zonas Francas (82_), Art. 1: "Sustitúyase en el artículo 2 el literal d) y agréguese un nuevo literal x)…: 'd) Área Metropolitana de San Salvador y de los Municipios Aledaños: La constituyen los municipios y distritos contemplados en la Ley de Desarrollo y Ordenamiento Territorial del Área Metropolitana de San Salvador y de los Municipios Aledaños, y su Reglamento, en adelante Área Metropolitana. x) Libre Internación: Es la introducción de mercancías al territorio nacional exentas del pago del Derecho Arancelario a la Importación (DAI) y del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios (IVA), u[sic OCR] cualquier otro impuesto que grave su importación.'" Art. 2: "Sustitúyase en el artículo 10 el literal b) del numeral 3…: 'Área verde: 30% del área total que incluye área verde ecológica, zona deportiva. Dicha área deberá distribuirse un 10% dentro de la Zona Franca, o en un área colindante a la Zona Franca, y el otro 20% podrá establecerse dentro o fuera de la Zona Franca, en caso se establezca fuera se estará a lo dispuesto en el artículo 46-A de esta ley.'" | ZF-law Art. 2 d) substitution: the metropolitan area is henceforth constituted by the municipios y distritos of the referenced Territorial-Development Law and its Reglamento (a dynamic external reference — replaces the printed 13-municipio enumeration of LB-002); new literal x) defines Libre Internación as entry of goods into the national territory EXEMPT from DAI, IVA and any other import tax (definitional anchor — the operative import-benefit rows already exist). ZF-law Art. 10.3.b substitution: the developer's green-area requirement (30% of total incl. ecological/sport) now SPLITS — 10% inside or adjacent to the zona franca + 20% inside OR outside (outside rides the Art. 46-A gate of LB-028) | `sv/sources/82_Reforma_Ley_ZF_DL493_DO_2025-12-23.pdf` | 82_ Arts. 1-2 pp.2-3 (EVID-385/386; 82_ txt PAGE 2-3; D.L. 493-2025 vigencia ~31-dic-2025 — co-cite 12_+82_; OCR PSM 4) |
| LB-028 | Reformas a la Ley de Zonas Francas (82_), Art. 8: "Intercálese en el artículo 44 un nuevo inciso entre el primero y el segundo…: 'Para los casos en que los Usuarios de Zona Franca requieran el cambio de tipo de beneficiario a Depósito para Perfeccionamiento Activo (DPA) o viceversa, estos deberán solicitar al Ministerio de Economía dicho cambio, debiendo cumplir con los requisitos establecidos en la Ley y su Reglamento.'" Art. 9 (nuevo Art. 46-A, "Autorización para área verde fuera del DPA o de la Zona Franca"): "Las nuevas solicitudes de los DPA que impliquen la construcción de instalaciones o naves industriales, en las que se solicite que el área verde se establezca fuera del DPA, se podrán autorizar siempre que dicha área cumpla con un porcentaje de compensación equivalente al diez por ciento del área total de su construcción. En el caso de las nuevas solicitudes de Desarrollistas de Zonas Francas…, un veinte por ciento del área total de su construcción. Los Desarrollistas… o los propietarios de DPA, deberán gestionar ante las autoridades competentes la autorización relacionada con [las] zonas verdes…, las cuales podrán establecerse en el sitio del impacto, en zonas aledañas, en zonas más propicias para su reposición o recuperación, entre otras. En lo relativo a los permisos de construcción…, se estará a lo dispuesto en las normas y especificaciones dictadas por la Dirección de Ordenamiento Territorial y Construcción (DOT), la Oficina de Planificación del Área Metropolitana de San Salvador (OPAMSS) o cualquier Otra institución con similares facultades…" | ZF-law Art. 44 intercalated inciso: a ZF usuario changing beneficiary type to DPA (or vice versa) must REQUEST the change from MINEC meeting the law + reglamento requisitos (the explicit ZF↔DPA role-change gate). New Art. 46-A: green-area-outside authorization — DPA new applications with outside green area need a compensation percentage equal to 10% of the constructed total area; ZF developers' outside green area needs 20%; the area may sit at the impact site, adjacent, or in better-suited recovery zones; construction permits before DOT/OPAMSS or equivalents | `sv/sources/82_Reforma_Ley_ZF_DL493_DO_2025-12-23.pdf` | 82_ Arts. 8-9 pp.5-7 (EVID-385/389/390; 82_ txt PAGE 5-7; vigencia ~31-dic-2025; OCR PSM 4 — "condas"→"con las" normalized) |
| LB-029 | Reformas a la Ley de Zonas Francas (82_), Art. 10 (ZF-law Art. 54-B inc. 1º sustituido): "Las personas naturales o jurídicas que hayan operado en el territorio aduanero nacional y tributado Impuesto sobre la Renta, previo a la solicitud de calificación de Desarrollista, Usuario de Zona Franca o como DPA, no podrán acogerse a la presente Ley." Art. 11 (ZF-law Art. 54-1 [sic print; = 54-I] adicionado): "Para efectos de la presente Ley, los Usuarios de Zonas Francas autorizados conforme a las disposiciones de la misma, que se instalen en Parques de Servicios autorizados de conformidad con la Ley de Servicios Internacionales, se considerarán como si estuviesen instalados en una Zona Franca." | Substituted Art. 54-B first inciso: natural or legal persons that OPERATED in the national customs territory and PAID ISR before applying for Desarrollista/Usuario/DPA qualification CANNOT take cover under the law (a prior-TAN-operation admission exclusion — bars conversions of operating TAN businesses). New Art. 54-I: ZF usuarios authorized under the law that install themselves in LSI-authorized parques de servicios are considered AS IF installed in a zona franca (the ZF-side mirror of LSI Art. 66 / SV-SPE-FR-063 iii) | `sv/sources/82_Reforma_Ley_ZF_DL493_DO_2025-12-23.pdf` | 82_ Arts. 10-11 pp.7-8 (EVID-385/390; 82_ txt PAGE 7-8; vigencia ~31-dic-2025; OCR PSM 4 — "54-1" printed = Art. 54-I) |
| LB-030 | Disposiciones Especiales … Incentivo Fiscal … Proyectos Inmobiliarios en Altura (95_), Art. 1: "…se entienden por desarrollos inmobiliarios en altura, las construcciones o edificaciones de bienes inmuebles nuevos que se realicen a partir de la entrada en vigencia de esta ley, y que cuenten con treinta y cinco pisos o niveles de altura o más, medidos desde el punto más bajo de la rasante de la calle frente a dichas edificaciones." Art. 3 inc. 2: "La exención operará por el período de quince años, los cuales serán contados a partir del ejercicio de imposición en que se comiencen a obtener tales utilidades e ingresos." Art. 4: "Las presentes disposiciones, por su carácter especial, prevalecerán sobre cualquier otra normativa que las contraríe, especialmente respecto de aquellas leyes que establecen exenciones o incentivos fiscales." Art. 6: "El presente Decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." (considerando III: Ley ISR Art. 4.1 basis) | High-rise real-estate developments: new constructions from the law's vigencia with 35+ floors/levels measured from the LOWEST point of the street rasante facing the building. The exemption operates for a FIFTEEN-YEAR period counted from the tax year in which such profits/income first begin to be obtained (TEXT-PINNED horizon — the registry's "per approval press" provenance superseded). Special character: prevails over any contrary norm, especially other exemption/incentive laws. Vigencia: 8 days after D.O. publication (24-sep-2024 → 2-oct-2024) | `sv/sources/95_Disposiciones_Inmobiliarios_Altura_DL95_2024_DGII.pdf` | 95_ Arts. 1/3/4/6 pp.1-3 (EVID-392/393; 95_ txt PAGE 1-3; W19 T4) |
| LB-031 | Disposiciones Especiales, Transitorias y Complementarias … Proyecto "…Biogás en el Río Acelhuate" (97_), Art. 1 (head): "Tanto la Comisión Ejecutiva Hidroeléctrica del Río Lempa (CEL), como las personas naturales o jurídicas involucradas como contratistas o subcontratistas, en el proyecto…, durante el período de planificación, diseño, estudios, consultorías, supervisión y construcción y hasta la completa recepción de las obras…, gozarán de las siguientes exenciones tributarias:…" Art. 2: "Los ingresos que perciban las personas naturales o jurídicas, involucradas como contratistas o subcontratistas…, se considerarán no gravadas para efectos del Impuesto sobre la Renta según lo regulado en el artículo 4, numeral 1 de la Ley de Impuesto sobre la Renta. Esta disposición estará vigente hasta la completa recepción de las obras." Art. 12: "Estas disposiciones son de carácter especial y priva sobre cualquier otra ley especial o general que la contradiga." Art. 13: "El presente decreto entrará en vigencia a partir del día de su publicación en el Diario Oficial." | Both CEL and the natural/legal persons involved as contractors or subcontractors of the named biogás project — for the planning through complete-reception-of-works period — enjoy the enumerated tax exemptions; contractor income is considered NOT TAXABLE for ISR under Ley ISR Art. 4.1, in force until complete reception of the works; special character prevails over any contrary special or general law; vigencia = publication day (25-ago-2025) | `sv/sources/97_Disposiciones_Biogas_Acelhuate_DL386_2025_DGII.pdf` | 97_ Arts. 1/2/12/13 pp.2-5 (EVID-394/395; 97_ txt PAGE 2-5; W19 T4) |
| LB-032 | Ley de Agentes Extranjeros (96_), Art. 1: "…establecer el régimen jurídico aplicable a las personas naturales o jurídicas, nacionales o extranjeras, cuyas actividades dentro de El Salvador respondan a intereses o sean financiadas, directa o indirectamente, por una persona extranjera." Art. 3: "Están obligados… toda persona natural o jurídica… que… realicen actividades que respondan a intereses, sean controladas o financiadas, directa o indirectamente por un mandante extranjero… tendrán la calidad de sujetos obligados, incluyendo a las asociaciones y fundaciones sin fines de lucro." Art. 6: "Créase el Registro de Agentes Extranjeros como una dependencia del Ministerio de Gobernación y Desarrollo Territorial, que podrá abreviarse 'RAEX'. En ese registro público deberán inscribirse, con carácter obligatorio, todos los sujetos obligados…" Art. 19: obligations breaches multa "desde CIEN MIL DÓLARES… hasta CIENTO CINCUENTA MIL DÓLARES…"; prohibitions breaches "desde CIENTO CINCUENTA MIL… hasta DOSCIENTOS CINCUENTA MIL DÓLARES…". Art. 24: "…deberán registrarse… en un plazo máximo de 90 días, a partir de la entrada en vigencia…". Art. 25: "…entrará en vigencia ocho días después de su publicación en el Diario Oficial." | Foreign-agents law: legal regime for natural/legal persons (national or foreign, non-profits included) whose in-country activities respond to, are controlled by or are financed by a foreign mandante; MIGOB's public RAEX registry with obligatory inscription (90-day transitory from vigencia; unregistered ⇒ no activities or asset movements); MIGOB-side fines US$100,000-250,000; vigencia 8 days after publication (30-may-2025 → 7-jun-2025). A TRANSPARENCY registro — not a fiscal-incentive regime (identity row; resolves the 54_ tail's EVID-167 pointer) | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30_pp3-18.pdf` | 96_ Arts. 1/3/6/19/24/25 pp.2-16 (EVID-396/397; 96_ txt PAGE 2-16; OCR PSM 4 — cleaning declared in EV header; W19 T4) |
| LB-033 | Ley Especial y Transitoria sobre la Modalidad de Pago del ISR… (90_), Arts. 1-9 (gloss-level per EVID-402; quotes there): COVID-19 emergency transitory — Art. 1 exonerates the Ley de Turismo Art. 16 contribución especial for 3 months from vigencia; Art. 2 defers turismo-sector ISR-2019 payment (impuesto ≤ US$25,000.00) to 31-may-2020 free of interests/recargos/multas (declaration still due 30-abr-2020; benefit EXCLUDED for holders of Ley-de-Turismo fiscal incentives — MITUR + MH resolution gate); Arts. 3-5 grant DGT pago a plazos up to OCHO cuotas mensuales (first cuota = 10% in May-2020, interest-free) for ISR-2019 ≤ US$10,000.00 (any sector) and, same terms, the energía-eléctrica chain and ≥2-service TV/internet/telefonía providers; Art. 6 defers the telecom sector's March-May 2020 ISR-anticipo enteros (6 cuotas, first = 10% in July-2020); Art. 7: CT governs all not regulated (sanciones, caducidad, procedimiento); Art. 9: "entrará en vigencia a partir del día de su publicación en el Diario Oficial." | HISTORICAL NOTE ONLY — a SPENT COVID-19 transitory (D.L. 598-2020, D.O. N° 58 T.426 20-mar-2020, vigencia publication-day): every deferral window ran and expired inside 2020; NO operative FR attaches (no Odoo surface for exhausted 2020 payment plans — awareness row only), and the row resolves the 54_ tail's EVID-167 pointer for this instrument (SOQ-41 W19 T5) | `sv/sources/90_Ley_Transitoria_Pagos_ISR_DL598_DO_2020-03-20_pp4-6.pdf` | 90_ Arts. 1-9 pp.4-6 (EVID-402; 90_ txt PAGE 1-3; forced-OCR PSM 4 — cleaning declared in EV header; W19 T5) |
| LB-034 | Disposiciones Especiales y Transitorias de Apoyo al "Programa de Acceso Universal a la Energía en El Salvador" (108_), Art. 1: "Las presentes disposiciones tienen por objeto establecer medidas especiales para apoyar y facilitar la implementación del "Programa de Acceso Universal a la Energía en El Salvador", que también podrá denominarse en las presentes disposiciones como "el Programa", el cual será desarrollado en todo el territorio nacional, y comprenderá el proceso de planificación, diseño, adquisición de equipos, herramientas, materiales, accesorios y repuestos, estudios, consultorías, supervisión y construcción de las obras civiles y redes de distribución de energía eléctrica, así como de sistemas de generación de energía eléctrica con base en recursos renovables; instalación y montaje de equipos; implementación de medidas ambientales y sociales; mejoramiento de accesos; adquisición de inmuebles; obras complementarias; o de cualquier actividad que sea necesaria para la completa ejecución del Programa hasta la completa recepción de las obras, bienes y servicios adquiridos localmente o en el extranjero." Art. 5: "Para el goce de los beneficios tributarios otorgados en las presentes disposiciones, los sujetos beneficiarios deberán presentar un escrito a la Dirección General de Impuestos Internos, por medio del cual se deberá informar sobre las contrataciones de obras, bienes o servicios respecto de los cuales se solicita el beneficio, adjuntando los documentos correspondientes en los que se compruebe su vinculación con el programa a que se refiere el artículo 1 de las presentes disposiciones." + "La Dirección General de Impuestos Internos, en un plazo que no exceda los diez días hábiles, contados a partir del siguiente al de la recepción del escrito al que refiere el presente artículo, emitirá la resolución correspondiente, a través de la cual podrá efectuar prevenciones o, en caso de que se cumplan todos los requisitos legales, declarará al solicitante como beneficiario de los beneficios contemplados en las presentes disposiciones." Art. 11: "Las presentes disposiciones tienen carácter especial y priman sobre cualquier ley especial o general que las contradiga." Art. 12: "Se faculta al Ministerio de Hacienda, para que, por sí, o a través de cualquiera de sus dependencias, pueda emitir los acuerdos, instructivos, circulares, resoluciones, o cualquier tipo de instrumento administrativo que garantice y viabilice la correcta y debida aplicación de lo dispuesto en las presentes disposiciones." Art. 13: "El presente decreto tendrá una vigencia de seis años contados a partir del día siguiente al de su publicación en el Diario Oficial." | Identity/instrument row (kin LB-030/031): the decree establishes special measures supporting a BID-financed, CEL-executed rural-electrification program (≈8,756 hogares per considerando V) under the CT Art. 6 literal b exoneración power (considerando VI); beneficiaries = contratistas/subcontratistas, admitted via the Art. 5 DGII escrito (informing the contrataciones + vinculación proof) with a resolución within ≤10 días hábiles counted from the day following reception (prevenciones or beneficiario declaration); special character prevails over any contrary special or general law; MH may issue acuerdos/instructivos/circulares/resoluciones to apply the decree; vigencia = six years from the day after D.O. publication (26-sep-2025 → 27-sep-2025 through 26-sep-2031). The admission mechanics are config-family inputs (escrito/resolución format = delegated practice — config-gap, no default, `02` OQ-10); the Art. 12 delegation = config-gap class (kin 96_ Art. 16); the exemption schedule lives in `02` (LB-024/FR-204); ISR/IVA operative rows = taxation SV-TAX-FR-417/419/420/421 by id | `sv/sources/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf` | 108_ Arts. 1/5/11/12/13 pp.1-5 (EVID-406; 108_ txt PAGE 1-5; native asamblea text layer — intra-word cleaning per EV header; W24 T1) |
| LB-035 | Reformas a la Ley para la Construcción, Administración, Operación y Mantenimiento del Aeropuerto Internacional del Pacífico (107_), considerando I (base-law frame): "Que mediante Decreto Legislativo No. 361, de fecha 26 de abril de 2022, publicado en el Diario Oficial No. 81, Tomo No. 435, del 29 de ese mismo mes y año, se emitió la Ley para la Construcción, Administración, Operación y Mantenimiento del Aeropuerto Internacional del Pacífico." Considerando V: "Que en la práctica, se ha podido constatar que, en gran medida, al establecer los valores de los inmuebles, con los que las personas han vendido a CEPA y se contrastan con los valores a los que estas personas los adquirieron originalmente, se advierte que se podría generar una eventual Ganancia de Capital." Considerando VI: "Que con la finalidad de no ocasionar una afectación que impacte en los recursos que las personas que han vendido a CEPA, recibieron o recibirán, por razones de un gravamen impositivo, como lo es la Ganancia de Capital, se estima necesario, por motivaciones de orden social, no incidir impositivamente a estas personas; por lo que, se vuelve necesario emitir las disposiciones legales para eximir de este gravamen a las citadas operaciones." Art. 3: "El presente decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." | IDENTITY row (CURRENT, not spent): the reform's operative articles — the added airport-law Art. 29.1.e (CEPA/MOPT seller ganancia-de-capital exoneración, perimeter-bounded) and the substituted Art. 35 (efectos retrotraídos al 8-may-2022 + orden-público-y-especial prevalence) — are quoted verbatim in taxation/03's W24 LB rows; the corpus encodes ONLY the Art. 29.1.e seller limb (operative FR = SV-TAX-FR-418, taxation/03 by id) with the Art. 35 retro-efectos window; vigencia 30-ene-2025 + 8 días = 7-feb-2025; the base law D.L. 361-2022 is UN-ACQUIRED — the Art. 2 perimeter geometry is an external config slot with NO default, and the base law's other Capítulo IV exonerations (CEPA/MOPT/companies, considerando II) are out-of-corpus — gloss only, no FR mechanics invented | `sv/sources/107_Reforma_AeropuertoPacifico_DL201_2025_Asamblea.pdf` | 107_ considerandos I/V/VI + Art. 3 pp.1-2 (EVID-405; 107_ txt PAGE 1-2; native asamblea text layer — intra-word cleaning per EV header; W24 T1) |

## 3. Functional Requirements

### 3.1 Territorial-regime taxonomy (12_ Art. 2; 80_ Art. 2)

- **SV-SPE-FR-001:** The system shall model ZF and DPA as two DISTINCT
  territorial regimes, never unified: *zona franca* — goods entering are
  considered as if NOT within the national customs territory with respect to
  import and export tributes; *depósito para perfeccionamiento activo* — an
  area under special customs treatment where goods enter with SUSPENSION of
  import tributes for transformation, elaboration, repair or other legally
  authorized process for subsequent re-export, capital goods remaining
  INDEFINITELY — the regime kind is a first-class discriminator on every
  beneficiary, customs and exemption record of this wave (consumed by
  `02`/`04`/`05` by id; the ZF/DPA 12-month clock vs LSI 24-month clock
  invariant is owned by `04_customs-clocks.md`).
  (LB-001; EVID-251)
- **SV-SPE-FR-002:** The system shall model the LSI territorial pair —
  *parque de servicios* (multi-company fenced extra-aduanal area, no resident
  population) vs *centro de servicios* (single-company customs-extraterritorial
  area, including locations in the national customs territory such as maritime
  and air ports per FR-009) — plus the four custody-role definitions of
  Art. 2: *usuario directo* (authorized service provider in park/center),
  *usuario indirecto* (accredited owner of goods entered into a park for
  distribution/logistics by a qualified usuario directo), *consignación de
  mercancías* (the act entrusting custody/handling/distribution to a usuario
  directo) and *mercancías destinadas* (goods notified/sent/delivered/
  consigned to the usuario directo) — parque vs centro is a second
  discriminator that keeps LSI rows distinct from ZF/DPA rows everywhere.
  (LB-012; EVID-259)

### 3.2 Beneficiary profile — the D15 row key (12_ Art. 5; 80_ Art. 10)

- **SV-SPE-FR-003:** The system shall carry, per beneficiary company, one
  regime profile whose fields form the D15 row key of the whole wave:
  regime (ZF · DPA · parque de servicios · centro de servicios), role
  (ZF: desarrollista · administrador · usuario · DPA titular; LSI:
  desarrollista · administrador · usuario directo · centro de servicios),
  activity admission (FR-006..009 config), location track (área
  metropolitana vs fuera — FR-022, ZF family), and *acuerdo* authorization
  date (D.O. publication of the MINEC acuerdo) — every exemption,
  requisito and clock row of `02`..`07` resolves against this key as-of its
  domain anchor and is snapshotted on the record (D15; never global
  constants).
  (LB-004; LB-017; EVID-251/259)

### 3.3 Authorization architecture + DGA institutional frame (12_ Art. 4; 80_ Arts. 3/7; 13_ Arts. 3/11/14)

- **SV-SPE-FR-004:** The system shall record the authorization architecture
  as informational state on the regime profile: MINEC authorizes
  establishment/administration/operation (ZF) and grants park/center
  benefits (LSI); MH — through DGA and DGII — holds fiscal surveillance and
  control; for LSI the PRIOR ONI capital registration (Ley de Inversiones)
  with its ≤5-*días hábiles* resolution is a precondition flag on the
  profile (días-hábiles arithmetic consumed from the fiscal-reporting
  calendar engine SV-FREP-FR-202..204 by id, never restated).
  (LB-003; LB-013; EVID-251/259)
- **SV-SPE-FR-005:** The system shall anchor the compliance surfaces of this
  wave on the DGA institutional frame as an informational note (no
  automation surface): the DGA is the superior national customs organ
  attached to MH; zonas francas, DPAs and parques de servicios form part of
  the *servicio aduanero*, and the DGA may establish on-site customs
  delegations in them — this frame grounds the DGA-facing registers of
  `07_obligations-reporting-sanctions.md` (consumed there by id).
  (LB-022; EVID-268)

### 3.4 Activity-admission config (12_ Arts. 3/6; 80_ Arts. 5/6/8)

- **SV-SPE-FR-006:** The system shall implement the ZF permitted-activity
  admission as config keyed by SAC scope: production/ensamble/maquila/
  manufacture/processing/transformation/commercialization of industrial
  goods in SAC Chapter 3 and Chapters 25 onward EXCEPT the Art. 6 negative
  list; plus romanos II-V (marine-species fishing for industrial
  transformation; greenhouse/laboratory flora cultivation; captive
  amphibian/reptile raising; ethyl-alcohol dehydration, each with the
  corresponding-authority permit flag); connected production services
  (design, painting, cutting, stamping, finishing, serigraphy, embroidery,
  washing, ironing, quality control, recycling, repair) admitted ONLY
  between beneficiaries of the law.
  (LB-005; EVID-252)
- **SV-SPE-FR-007:** The system shall implement the ZF Art. 6 exclusion
  config as a negative admission gate with two tiers: activity exclusions
  a)-k) (hydrocarbons/fuels; cement and clinker; ferrous and non-ferrous
  scrap; subsuelo minerals; explosives/radioactive; polluting goods; sugar
  and incorporations; alcohol and incorporations SALVO Art. 3 V; synthetic-
  fiber sacks; prepared-food supply; machinery import for leasing) and
  personal exclusions 1)-4) (suspended/revoked beneficiaries; societies
  with directors/representatives/partners of suspended/revoked societies;
  illicit-object activities; firm pending customs/tax obligations — with the
  voluntary-suspension carve-out for 1)-2)), each exclusion recorded as a
  dated config row with the 12_ print provenance.
  (LB-006; EVID-252)
- **SV-SPE-FR-008:** The system shall implement the LSI benefited-activity
  admission as letters **a)-o)** config (W19 T3: catalogue expanded by D.L.
  277-2013 from a)-j)), each letter carrying its statutory scope predicate
  as an admission/monitoring rule: a) distribución internacional and b)
  logística internacional without transforming the nature of the goods; d)
  tecnologías de información TO legal persons domiciled outside the
  national territory; **i) médico-hospitalario — general and specialized
  treatment with or without surgery, DENTAL INCLUDED — TO patients
  permanently domiciled outside Salvadoran TERRITORY (277-2013 re-scope:
  was outside Centroamérica with general medicine and dental excepted)**;
  k) contenedores TO international-goods-transport legal persons (air and
  sea); l) equipos tecnológicos (tangible or intangible) TO
  foreign-domiciled legal persons; m) ancianos y convalecientes TO persons
  permanently domiciled abroad; n) telemedicina (clinical consultation
  EXCLUDED; practitioners registered to practice in SV) TO persons
  permanently domiciled abroad; o) cinematografía postproduction TO
  foreign-domiciled legal persons; g) aeronáutico export-grade when
  provided to international-flight airlines regardless of domicile
  (Art. 8 inc. 2); letters **a), b), c), d), e), j)** further carry the
  local-market and retention surfaces owned by `03`/`05` (cited by id, not
  restated here — 277-2013 REMOVED h) from that set: EVID-383).
  (LB-014; LB-016; EVID-260/261; EVID-381/383 W19 T3)
- **SV-SPE-FR-009:** The system shall implement the LSI placement rule
  (Art. 6, as reformed by D.L. 277-2013) as admission validation — letters
  a), b), d), e), j), l), o) only in parques de servicios; f) ships and g)
  aircraft also in national-territory/port locations previously qualified
  as centros de servicios; **k) containers as centros when adjacent to a
  sea or air port; c) call centers, h) BPO, i) médico-hospitalario, m)
  ancianos, n) telemedicina in parks OR centers (277-2013: h)/i) moved
  from parque-only into the dual set; l)/o) joined the parque-only set)** —
  and shall flag the co-located
  NON-benefited categories 1)-11) (hotels; airlines; energy; communications
  except call centers and no-network international-traffic terminators,
  which also lose the Arts. 21/25 benefits; banking/insurance except c)/j);
  transport; tourism/courier; professional/technical except h)/j); food
  supply; private security; leasing except administrator-to-usuario) as
  operating under ordinary national tax law: full tax routing, no regime
  benefits, inside the same park (the 1)-11) list itself is unchanged by
  277-2013).
  (LB-015; LB-014 final inciso; EVID-260; EVID-382 W19 T3)

### 3.5 Qualification requisitos — dated config rows (12_ Arts. 17-A/19-A/19-B; 80_ Arts. 22/23)

- **SV-SPE-FR-010:** The system shall implement the ZF usuario
  qualification requisitos (Art. 17-A) as dated config rows resolved
  per-beneficiary (valid_from = acuerdo D.O. date; instrument = 12_ as
  printed) with at-least-one-of semantics: a) initial fixed-asset
  investment ≥US$500,000.00 attainable within the first two years of
  operations; b) ≥50 permanent jobs from the first year; c) ≥5 permanent
  jobs from the first year for comercializadores — measured values
  (investment bookings against the row; headcount from payroll records,
  payroll/05-06 by id) log against the row with the operations-year anchor.
  (LB-007; EVID-255)
- **SV-SPE-FR-011:** The system shall implement the ZF invernadero/
  laboratorio requisitos as dated config rows: ≥US$100,000 first-year
  fixed-asset investment AND ≥15 permanent jobs AND minimum area 5,000 m²
  (invernaderos) / 1,000 m² (laboratorios) AND formal administrative and
  financial structure (criterion flag), with the same breach split of
  FR-016 (a)-breach revocación; b)-d)-breach suspensión with tributes
  payable and benefit clock running).
  (LB-007; EVID-255)
- **SV-SPE-FR-012:** The system shall implement the DPA qualification
  requisitos as dated config rows: Art. 19-A at-least-one-of — a) initial
  fixed-asset investment ≥US$800,000 attainable within the first two years,
  with acquisition of EXISTING infrastructure excluded from the investment
  computation (exclusion rule on the row); b) ≥75 permanent jobs from the
  first year; c) ≥15 permanent jobs for comercializadores — and Art. 19-B
  all-of for amphibian/reptile DPAs (≥US$100,000 first-year investment, ≥15
  permanent jobs, formal structure; Art. 3 III flora activities follow the
  17-A requisito set).
  (LB-008; LB-009; EVID-255)
- **SV-SPE-FR-013:** The system shall implement the LSI distributor/
  logistics-operator requisitos (Art. 22) as dated config rows on the
  usuario-directo profile: a) ≥500 m² owned or leased (exception flag for
  the MINEC+MH lesser-area authorization); b) DGA registration with system
  access code; c) electronic inventory register + online system with
  warehouse entry/exit documents (register contract owned by
  `07_obligations-reporting-sanctions.md` by id); d) 5-year consolidated-
  manifest copies retention; e) bulto presentation/equipment duty; f)
  answer for declared-vs-arrived quantity/nature/value differences (carrier
  recourse); g) answer for usuario-indirecto clients' taxes on shortfalls,
  losses, misplacements and shrinkage (liability ledger owned by
  `03_lsi-regime.md` by id).
  (LB-018; EVID-262)
- **SV-SPE-FR-014:** The system shall implement the LSI BPO,
  médico-hospitalario and ancianos requisitos (Art. 23, as rewritten by
  D.L. 277-2013) as dated config rows: BPO (parques) — new asset
  investment ≥US$150,000 in the FIRST SIX MONTHS of operations (working
  capital + fixed assets) AND ≥10 permanent jobs AND a written contract of
  at least SIX MONTHS AND a business plan, with breach-year semantics:
  failure in any year removes the law's benefits FOR THAT FISCAL YEAR ONLY
  (per-ejercicio benefit-loss state, not revocation — the closing sanction
  is now common to all three blocks); médico-hospitalario (parques) — new
  fixed-asset investment ≥US$1,000,000 in the first year (single tier,
  surgical and non-surgical, general medicine and dental), ≥10 permanent
  jobs, ≥4,000 m² built of the hospital unit, business plan and
  medical-hospital security norms (W19 T3: the pre-277 US$10,000,000 /
  US$3,000,000 [sic] tiers and the fuera-del-metro + insured-patients
  predicates are SUPERSEDED — pre-277 beneficiaries keep their historical
  rows per D18); ancianos y convalecientes (parques) — ≥US$250,000
  first-year investment, ≥10 permanent jobs, business plan; the
  centros-track thresholds (US$250,000/20 jobs BPO · US$2,000,000/15
  jobs/4,000 m² médico · US$500,000/15 jobs ancianos — Art. 24-A) are
  owned by SV-SPE-FR-190.
  (LB-019; LB-026; EVID-262 historical; EVID-384 W19 T3)

### 3.6 Breach state machine (12_ Arts. 17-A/19-A/39; 80_ Arts. 52/62)

- **SV-SPE-FR-015:** The system shall maintain a benefit-state field on the
  regime profile — *activa* (active) · *suspendida* (suspended) ·
  *revocada* (revoked) · inactivity category-loss — that drives the
  exemption-row resolution of `02_zf-exemption-schedules.md` and
  `03_lsi-regime.md` and the routing of `05_tan-iva-interface.md` (consumed
  by id): suspension makes tributes payable during the period; revocation
  and category loss end the benefit rows; every state change records its
  statutory reason and resolution reference.
  (LB-007; LB-020; LB-021; EVID-255/264)
- **SV-SPE-FR-016:** The system shall implement the ZF/DPA breach split
  with its two invariants: investment-requisito breach (literal a) ⇒
  REVOCACIÓN of the authorization acuerdo; jobs/comercializador requisito
  breach (b)/c), and 17-A greenhouse b)-d)) ⇒ SUSPENSIÓN until cured, with
  the tributes applicable to imports made and related taxes PAYABLE during
  the suspension, AND the suspension period NOT interrupting the total
  benefit term (the ladder clock keeps running — consumed by `02` by id);
  both branches ride the Art. 48 procedure (FR-019).
  (LB-007; LB-008; EVID-255)
- **SV-SPE-FR-017:** The system shall implement the LSI breach escalations
  as state transitions only (SMM-priced sanction VALUES live in
  `07_obligations-reporting-sanctions.md`, which consumes payroll/02 SMM
  rows by id — nothing SMM-priced is encoded here): third serious
  infringement ⇒ REVOCATORIA; very-serious ⇒ three-month suspension,
  recidivism ⇒ revocation (Art. 52); the transitions stamp the
  benefit-state field of FR-015.
  (LB-020; EVID-264)
- **SV-SPE-FR-018:** The system shall implement inactivity category/benefit
  loss as dated monitors: ZF — 12 continuous months of not operating the
  incentivated activity (imports/exports under the regime), with the
  5-*días hábiles* audiencia and 10-day final resolution, DGA tracking and
  system deregistration recorded (Art. 39); LSI — 3 continuous months of
  not operating ⇒ benefits revoked (force majeure/casus fortuitus
  exception), with the DGA computer-system access disablement recorded as a
  regime-state side effect (Art. 62).
  (LB-010; LB-021; EVID-258/264)

### 3.7 MINEC procedure clocks (12_ Arts. 45/48/49)

- **SV-SPE-FR-019:** The system shall expose the MINEC procedure surfaces
  as workflow states with their statutory clocks (días-hábiles arithmetic
  consumed from SV-FREP-FR-202..204 by id): usuario qualification
  resolution 25 *días hábiles* / DPA 35 *días hábiles* (MH opinion period
  included); same-zone amendment acuerdos (no activity change, SS-solvent,
  expansions/diminutions/relocation within the same zona franca, notarized
  note) within 10 *días hábiles*; infringement audiencia 5 *días hábiles*
  with final resolution in ten days (Art. 48); revocatoria recourse filed
  within 3 *días hábiles* of notification and resolved within 15 *días
  hábiles* (Art. 49).
  (LB-011; EVID-258)

### 3.8 Customs declarante-role config (74_ Arts. 9/5/5-A; 13_ Art. 36-A)

- **SV-SPE-FR-020:** The system shall carry a declarante-role config per
  importing/exporting persona jurídica with three modes: *agente aduanero*
  (external customs agent — credential requirements recorded at evidence
  depth: Estado-Party national, licenciatura in customs matters OR other
  degree + 2 years customs experience, possible psychometric exam);
  *apoderado especial aduanero* — self-declaration route, optional for
  personas jurídicas, granted by DGA authorization: public-deed power to an
  employee, sufficiency examination on customs matters (possibly including
  psychometric tests), and the poderdante's fianza (amount fixed by the DGA
  — config-gap, no shipped default), the apoderado standing under the same
  suspension/revocation rules as agentes; and ordinary agency. Once the
  fianza is posted, the apoderado especial transmits the company's own
  declarations (transmission surface owned by `06_customs-declarations.md`
  by id).
  (LB-024; LB-023; EVID-269/268)
- **SV-SPE-FR-021:** The system shall record pre-declaration *consultas*
  and advance rulings as reference records with their statutory clocks and
  effects: consultas answered within 15 *días hábiles* extendable ex officio
  by an equal period, effective only for the specific case consulted, and
  NEVER suspending customs/tax obligations; advance criteria/resolutions
  accepted only before the importation of the goods concerned, valid for
  three years unless the underlying conditions change (validity window
  stamped on the record).
  (LB-025; EVID-269)

### 3.9 Área metropolitana — stale-static dated list (12_ Art. 2 d)

- **SV-SPE-FR-022:** The system shall implement the *área metropolitana* as
  a STALE-STATIC dated list of the 13 municipios as printed (Antiguo
  Cuscatlán, Santa Tecla, Apopa, Ayutuxtepeque, Cuscatancingo, Ciudad
  Delgado, Ilopango, Mejicanos, Nejapa, San Marcos San Martín [sic],
  Tonacatepeque, San Salvador, Soyapango) — one dated row set with the 12_
  print provenance, `valid_to` = the 82_ vigencia (~31-dic-2025), NO
  recompute against the 2023 municipal reorganization (SOQ-43) — and shall
  derive the location track of FR-003 (metro vs fuera) from it, feeding
  the shorter/longer exemption tracks of `02_zf-exemption-schedules.md` by
  id; W19 T3 (82_ Art. 1, LB-027): from ~31-dic-2025 the Art. 2 d)
  definition flips to a DYNAMIC external reference — "los municipios y
  distritos contemplados en la Ley de Desarrollo y Ordenamiento Territorial
  del Área Metropolitana de San Salvador y de los Municipios Aledaños, y su
  Reglamento" — encoded as a successor dated row whose membership resolves
  from that referenced law + reglamento (NEITHER in corpus: config slot
  with NO shipped default until acquired — OQ-5; facts before
  ~31-dic-2025 keep resolving against the 13-municipio rows).
  (LB-002; LB-027; EVID-251; EVID-386 W19 T3)

### 3.10 W19 T3 fold-in — LSI centros requisitos (80_ Arts. 24/24-A); ZF 82_ gates (82_ Arts. 8/9/10/11)

- **SV-SPE-FR-190:** The system shall implement the LSI CENTROS-de-servicios
  qualification requisitos (80_ Art. 24 general + Art. 24-A per-activity,
  both added/rewritten by D.L. 277-2013 — a corpus surface that did not
  exist under the pre-277 print) as dated config rows on the centro profile,
  resolved per-activity: general requisitos — location authorization by the
  corresponding authority; environmental and occupational-safety/hygiene
  conditions; formal administrative and financial organization; edificaciones
  (parking, emergency exits, activity-specific); per-activity — BPO
  ≥US$250,000 in the first six months + ≥20 permanent jobs + ≥6-month
  written contract + business plan; médico-hospitalario ≥US$2,000,000 first
  year + ≥15 jobs + ≥4,000 m² built hospital unit + plan + security norms;
  ancianos ≥US$500,000 first year + ≥15 jobs + plan — each carrying the
  same ejercicio-loss breach semantics as FR-014 (that fiscal year's
  benefits lost), the centros thresholds being DISTINCT from (higher than)
  the parque equivalents and never unified with them; container/ship/
  aircraft-repair centros located OUTSIDE a primary customs zone carry the
  customs-delegation-office duty + services/equipment contribution flag
  (informational compliance state; the delegation frame is FR-005's).
  (LB-026; EVID-384 W19 T3)
- **SV-SPE-FR-191:** The system shall implement the ZF↔DPA
  cambio-de-tipo-de-beneficiario gate (82_ Art. 8, intercalated in ZF-law
  Art. 44): a ZF usuario requiring change of beneficiary type to DPA, or
  vice versa, must SOLICIT the change from MINEC meeting the law +
  reglamento requisitos — recorded as a PRIOR-authorization transition
  event on the regime profile (regime/role fields never mutate without the
  granted-solicitud reference; the Art. 28 a) modification gate of
  SV-SPE-FR-199 names this cambio among its five kinds; the solicitation
  format lives in the Reglamento General — config slot, OQ-3).
  (LB-028; EVID-389 W19 T3)
- **SV-SPE-FR-192:** The system shall implement the 82_ área-verde regime
  as three dated config surfaces with valid_from = ~31-dic-2025: i) ZF
  desarrollista split (ZF-law Art. 10.3.b) — 30% green area of the total
  (incl. ecological + sport) divided 10% inside or ADJACENT to the zona
  franca + 20% inside OR outside (outside rides iii); ii) DPA split
  (ZF-law Art. 18 d).5) — 20% zona verde divided 10% inside or adjacent to
  the DPA + 10% inside or outside (outside rides iii), the same percentages
  applying to AMPLIACIONES, reductions and relocations of DPA installations
  (a physical requirement on `04`'s traslado surfaces — no clock change);
  iii) the Art. 46-A outside-authorization gate — DPA new applications:
  compensation ≥10% of the total CONSTRUCTED area; ZF desarrollista new
  applications: ≥20%; the compensating area may sit at the impact site,
  adjacent zones or better-suited reposición/recuperación zones, with
  construction permits before DOT/OPAMSS or equivalent institutions
  (recorded as qualification-time requisito flags + authorization
  references; pre-vigencia applications keep the 12_ Art. 10/18 rules as
  their dated rows).
  (LB-027; LB-028; EVID-386/388/390 W19 T3)
- **SV-SPE-FR-193:** The system shall implement the substituted ZF-law
  Art. 54-B first inciso (82_ Art. 10) as a dated negative-admission gate:
  natural or legal persons that OPERATED in the territorio aduanero
  nacional and PAID ISR before applying for qualification as
  Desarrollista, Usuario de Zona Franca or DPA cannot take cover under the
  law — an admission-time exclusion flag on the application profile (kin of
  the FR-007 personal-exclusion tier, kept a DISTINCT cause with 82_
  provenance; effective ~31-dic-2025; applications before that date
  resolve without it).
  (LB-029; EVID-390 W19 T3)
- **SV-SPE-FR-194:** The system shall implement the new ZF-law Art. 54-I
  (82_ Art. 11): ZF usuarios authorized under the law that install
  themselves in parques de servicios authorized under the Ley de Servicios
  Internacionales are considered AS IF installed in a zona franca — a
  location-equivalence discriminator on the regime profile (physical
  location = LSI parque, regime family = ZF) that keeps the ZF exemption
  ladders, clocks and routing resolving against the ZF row sets while the
  premises sit inside an LSI parque; this is the ZF-side MIRROR of the LSI
  Art. 66 rule (SV-SPE-FR-063 iii — consumed by id, never restated; the
  two equivalence rules are recorded as their own config rows, one per
  regime family, never merged).
  (LB-029; EVID-390 W19 T3)

### 3.11 W19 T4 fold-in — project-specific D.L.-incentive class (95_/97_; W24 T1: +108_) + 96_ identity (D.L. 308-2025)

- **SV-SPE-FR-200:** The system shall model PROJECT-SPECIFIC D.L.
  FISCAL-INCENTIVE instruments as a distinct regime class in the inventory —
  a THIRD family alongside the territorial regimes (ZF/DPA/LSI, FR-001/002)
  and the quantity-based contributions (`08`), never unified with either:
  admission is per-instrument and NON-territorial (95_: DGII beneficiario
  resolución on a ≥30-day prior written notice enumerating project name,
  ubicación, altura specs, titulares + socios, investment amount and
  completion date — no MINEC acuerdo, no location track; 97_: contractual —
  CEL plus its contratistas/subcontratistas for the named project; 108_:
  admission kind `dgii_escrito_vinculacion` — the Art. 5 escrito a la DGII
  informing the contrataciones de obras, bienes o servicios with the
  program-vinculación proof attached, resolved by DGII resolución within
  ≤10 días hábiles counted from the day following the escrito's reception
  (prevenciones or beneficiario declaration — días-hábiles arithmetic
  SV-FREP-FR-202..204 by id; NOT the 95_ ≥30-day prior notice; the
  escrito/resolución format is delegated practice — config-gap, NO default,
  `02` OQ-10)), and the benefit window is INSTRUMENT-KEYED with the window
  kind carried as a discriminator, never normalized: 95_ = fixed 15-AÑOS
  horizon counted from the ejercicio in which incentivized utilidades
  first obtain (TEXT-PINNED, Art. 3 inc. 2 — a standing per-beneficiary
  window, the law remaining open for new ≥35-piso projects from
  2-oct-2024); 97_ = EVENT-BOUNDED, effective from contract signature until
  the completa recepción de las obras or the end of the CEL relationship in
  any of its forms (a project-spent transitory-style window,
  publication-day vigencia 25-ago-2025); 108_ = TWO-LAYER — the fixed
  decree vigencia 27-sep-2025 → 26-sep-2031 (six years, Art. 13) as the
  outer layer, with the per-benefit event window firma de contratos →
  recepción final de las obras / fin de la relación contractual con CEL
  (Art. 4-II) inside it (the 97_ `event_bounded_recepcion` kind, now carried
  inside a still-open decree vigencia — a CURRENT member, not project-spent
  like 97_; both layers on every dated row, never collapsed). Each
  instrument lands as its own config family keyed by instrument id +
  vigencia, with its especialidad clause (95_ Art. 4; 97_ Art. 12; 108_
  Art. 11) recorded as a prevalence flag (never a conflict-resolution
  engine); the D15 dated exemption rows are consumed from `02`
  (FR-202/203/204 by id); ISR-side effects route through Ley ISR Art. 4.1
  renta-no-gravable (54_ by id — never restated here); the 108_ ISR/IVA
  side effects route to the taxation siblings BY ID only (SV-TAX-FR-417
  no-gravables stamp · SV-TAX-FR-419 CEL-seller exoneración · SV-TAX-FR-420
  IVA exemption registry · SV-TAX-FR-421 pro-rata relief — pointer
  sentences only, no restatement).
  (LB-030; LB-031; LB-034; EVID-392..395 W19 T4; EVID-406 W24 T1)
- **SV-SPE-FR-201:** The system shall carry the D.L. 308-2025 Ley de
  Agentes Extranjeros (96_) as an IDENTITY row of the regime inventory —
  NOT a fiscal-incentive regime and NEVER consumed by this wave's exemption
  machinery: a MIGOB transparency law whose operative surface is the RAEX
  registro público (obligatory inscription of sujetos obligados — persons
  whose activities respond to, are controlled by or are financed by a
  foreign mandante, non-profits included; 90-day transitory from vigencia
  7-jun-2025 with a total activity/asset freeze while unregistered; RAEX
  exclusion calificación renewable annually or per project). The Odoo
  surface is a registration-state flag on the company/partner profile
  (unregistered · registered · excluded + date) with the MIGOB sanction
  character (US$100,000-250,000 multas; suspension/cancelación of personería
  jurídica) recorded as informational metadata — the registry itself is
  authority-side, mirrored never emulated. The Chapter V 30% special levy
  on mandante-financed transactions with its Agentes de Retención Especial
  machinery (96_ Arts. 10-14) = taxation-owned since W20
  (`17_foreign-agents-levy.md`, SV-TAX-FR-405..416 by id; OQ-6
  resolved-by-pointer). This row resolves the
  54_ tail's EVID-167 pointer that named this law (SOQ-41 W19 T4).
  (LB-032; EVID-396/397 W19 T4)

## 4. Data Model

Layer semantics: the regime framework is Odoo-native (res.company profile +
config rows) — all entities live in the client (wave default `odoo`; see
§5). MINEC/DGA/ONI are external authorities: the model records
authority-issued facts (acuerdos, resolutions, registrations), it does not
emulate them. No printed data table in this file warrants a CSV sidecar
(the 13-municipio list and the requisito values are small config sets;
default none per plan).

**Regime profile (on res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_spe_regime | select | zona_franca · dpa · parque_servicios · centro_servicios · none | FR-001, FR-002 |
| res.company | sv_spe_role | select | zf: desarrollista · administrador · usuario · titular_dpa; lsi: desarrollista · administrador · usuario_directo · centro_servicios | FR-003 |
| res.company | sv_spe_activity_admission | m2o config | ZF SAC-scope/negative-list row set (FR-006/007); LSI letter + predicate (FR-008/009) | FR-006..009 |
| res.company | sv_spe_location_track | select (computed) | metro · fuera — derived from the FR-022 municipio list (ZF family) | FR-003, FR-022 |
| res.company | sv_spe_acuerdo_do_date | date | MINEC acuerdo D.O. publication date = D15 row key member | FR-003 |
| res.company | sv_spe_benefit_state | select | activa · suspendida · revocada · perdida_inactividad | FR-015 |
| res.company | sv_spe_state_reason | select + char | art17a_a_investment · art17a_bc_jobs · art52_third_grave · art52_muy_grave · art39_inactivity_12m · art62_inactivity_3m · … (resolution ref) | FR-015..018 |
| res.company | sv_spe_oni_registration | char + date + boolean | ONI capital-registration resolution + ≤5-días-hábiles clock result (LSI precondition) | FR-004 |
| res.company | sv_spe_dga_access_enabled | boolean | DGA system-access state; set false on Art. 62 cancellation / Art. 39 baja | FR-018 |

**Activity-admission config (l10n_sv_special_regime.activity):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.activity | regime_scope | select | zf_sac_chapter (Ch. 3 + Ch. 25+, minus Art. 6) · zf_romano (II pesca · III invernadero · IV anfibios · V alcohol) · zf_connected_service (beneficiaries-only) · lsi_letter a)..o) (277-2013 catalogue; W19 T3) · lsi_non_benefited 1)..11) | FR-006..009 |
| l10n_sv_special_regime.activity | scope_predicate | char/config | per-letter rule (d TI: foreign-domiciled PJ; i médical: non-SV-territory patients, dental included — 277-2013 scope; g aeronáutico: international airlines regardless of domicile; k transport PJs; l/o foreign-domiciled PJs; m/n foreign-domiciled persons) | FR-008 |
| l10n_sv_special_regime.activity | exclusion_tier | select | none · activity_art6_a_k · personal_art6_1_4 (voluntary-suspension carve-out flag) | FR-007, FR-009 |
| l10n_sv_special_regime.activity | valid_from · valid_to · provenance | date · date · char | instrument = 12_/80_ article as printed (SOQ-30; W19 T3 14_→80_); dated rows per D15 | FR-006..009 |

**Qualification-requisito rows (l10n_sv_special_regime.requisito):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.requisito | profile · kind | m2o · select | zf_usuario_17a · zf_invernadero_17a · dpa_19a · dpa_19b · lsi_distribuidor_22 · lsi_bpo_23 · lsi_medico_23 · lsi_ancianos_23 · lsi_centro_24a (per-activity centros rows — W19 T3) | FR-010..014, FR-190 |
| l10n_sv_special_regime.requisito | threshold_type | select | investment_usd · permanent_jobs · area_m2 · contract_min_months · business_plan_flag · structure_flag · registration_flag · security_norms_flag · delegation_office_flag | FR-010..014, FR-190 |
| l10n_sv_special_regime.requisito | threshold_value · horizon | monetary/int · char | US$500,000/2y · 50 jobs/1y · 5 jobs (comercializadores) · US$100,000+15+5,000/1,000 m² · US$800,000/2y (existing-infrastructure exclusion) · 75/15 jobs · US$100,000+15 (19-B) · 500 m² · US$150,000/6 months+10 jobs+6-month contract+plan · US$1,000,000 médico+10+4,000 m² · US$250,000 ancianos+10 · centros: US$250,000/6 months+20+6-month contract · US$2,000,000+15+4,000 m² · US$500,000+15 — as printed (277-2013 values; W19 T3) | FR-010..014, FR-190 |
| l10n_sv_special_regime.requisito | logic · breach_effect | select | at_least_one · all_of ; revocacion · suspension_tributes_payable_clock_runs · ejercicio_benefit_loss | FR-010..016 |
| l10n_sv_special_regime.requisito | valid_from · valid_to · provenance | date · date · char | valid_from = beneficiary acuerdo D.O. date; instrument = law article as printed | FR-010..014 |
| l10n_sv_special_regime.requisito.log | measured_value · period | monetary/int · date/char | investment bookings and headcount (payroll/05-06 feed by id) logged per operations year against the row | FR-010, FR-014 |

**Área-metropolitana list (l10n_sv_special_regime.municipio):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.municipio | name · ismetro | char · boolean (true) | the 13 municipios as printed (San Marcos San Martín [sic]) | FR-022 |
| l10n_sv_special_regime.municipio | valid_from · valid_to · provenance | date · date · char | stale-static 12_ print rows; valid_to = ~31-dic-2025 (82_ Art. 1 flips the definition to a dynamic external reference); successor row = referenced-law lookup, config slot (OQ-5); NO 2023-reorganization recompute (SOQ-43) | FR-022 |

**W19 T3 fold-in rows (80_ Art. 24-A centros requisitos; 82_ ZF tail — FR-190..194):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.requisito (centros) | kind lsi_centro_24a | config rows | per-activity: bpo (US$250,000/6 months · 20 jobs · 6-month contract · plan) · medico (US$2,000,000 · 15 · 4,000 m² · plan · security norms) · ancianos (US$500,000 · 15 · plan) + Art. 24 general flags; ejercicio-loss breach semantics; delegation-office flag for contenedores/embarcaciones/aeronaves outside primary zone | FR-190 |
| l10n_sv_special_regime.beneficiary_type_change | from_role · to_role · solicitud_ref · granted_on | select ×2 · char · date | ZF ↔ DPA cambio de tipo (82_ Art. 8 → ZF Art. 44): profile regime/role mutate only with the granted MINEC solicitud | FR-191 |
| l10n_sv_special_regime.area_verde_rule | track · split · compensation_pct · valid_from | select · config · percent · date | zf_desarrollista (30%: 10 in/adjacent + 20 in-or-out) · dpa (20%: 10/10; applies to ampliaciones/reducciones/traslados); outside gate = Art. 46-A (compensation 10% DPA / 20% ZF of constructed area; DOT/OPAMSS permit refs) | FR-192 |
| res.company (application profile) | sv_spe_prior_tan_excluded | boolean (dated) | 54-B inc. 1º (82_ Art. 10): operated in TAN + paid ISR before the qualification request ⇒ cannot take cover under the law (effective ~31-dic-2025) | FR-193 |
| res.company | sv_spe_location_equivalence | select | none · zf_user_in_lsi_parque (Art. 54-I — ZF row sets resolve while premises sit in an LSI parque; mirror of spe/03 FR-063 iii Art. 66) · lsi_user_in_zf (FR-063 iii, spe/03) | FR-194 |

**W19 T4 fold-in rows (95_/97_ project-incentive class; 96_ identity — FR-200/201; W24 T1: +108_ dl411_2025 values on FR-200):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_spe_regime | select + project_incentive | new class value project_incentive (third family alongside zona_franca/dpa/parque_servicios/centro_servicios — never unified with territorial kinds) | FR-200 |
| l10n_sv_special_regime.dl_incentive | instrument_id · vigencia · valid_to | select · date · date | dl95_2024 (2-oct-2024) · dl386_2025 (25-ago-2025) · dl411_2025 (vigencia 27-sep-2025, valid_to 26-sep-2031 — provenance 108_ Art. 13, six years from the day after D.O. publication); instrument-keyed config family (post-print reform watch = SOQ-30 cadence kin) | FR-200 |
| l10n_sv_special_regime.dl_incentive | admission_kind | select | dgii_notice_resolucion (95_: ≥30-day prior notice, content-enumerated; DGII resolución ≤10 días) · cel_contract (97_: CEL + contratistas/subcontratistas) · dgii_escrito_vinculacion (108_: Art. 5 escrito + vinculación proof, resolución ≤10 días hábiles from the day following reception; format = config-gap, NO default — `02` OQ-10) | FR-200 |
| l10n_sv_special_regime.dl_incentive | window_kind · window_params | select · config | fixed_15y_from_first_utilidades (95_ — text-pinned Art. 3 inc. 2) · event_bounded_recepcion (97_: firma de contratos → recepción final / fin de relación CEL) · event_bounded_recepcion_within_vigencia (108_ — discriminated value, never normalized to either layer alone: decree vigencia 27-sep-2025 → 26-sep-2031 (Art. 13) + per-benefit firma de contratos → recepción final / fin de relación CEL (Art. 4-II) inside it) | FR-200 |
| l10n_sv_special_regime.dl_incentive | especialidad · valid_from · provenance | boolean · date · char | prevalence flag (95_ Art. 4 / 97_ Art. 12 / 108_ Art. 11) + instrument provenance; dated rows per D15 | FR-200 |
| l10n_sv_special_regime.dl_incentive | vinculacion_contrato_ref | m2o/char | 108_: per-contract vinculación link — the Art. 5 escrito/Art. 6 registro hook consumed by `02` FR-204 by id (registros especiales keyed per contract) | FR-200, FR-204 (`02` by id) |
| res.company/res.partner | sv_raex_state · sv_raex_date | select · date | unregistered · registered · excluded (96_ identity row — MIGOB RAEX; sanction character informational; Chapter V levy = taxation-owned (SV-TAX-FR-405..416 by id)) | FR-201 |

**Declarante-role config + rulings (res.company / l10n_sv_special_regime.ruling):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_spe_declarante_mode | select | agente_aduanero · apoderado_especial · ordinary_agency | FR-020 |
| res.company/res.partner (employee) | sv_spe_apoderado_data | fields | escritura pública ref · sufficiency-exam date/result (psychometric flag) · DACG requirements pending flag (OQ-004) | FR-020 |
| res.company | sv_spe_fianza_ref · sv_spe_fianza_amount | char · monetary slot | DGA-fixed fianza — config-gap, NO shipped default (OQ-004) | FR-020 |
| l10n_sv_special_regime.ruling | kind | select | consulta · advance_ruling | FR-021 |
| l10n_sv_special_regime.ruling | filed_on · due_on · answered_on · valid_until | date | consulta: 15 días hábiles + equal ex-officio extension, case-specific; advance ruling: pre-import only, 3-year validity window | FR-021 |

## 5. Odoo Mapping

Layer semantics for this wave: the regime framework is Odoo-native
(res.company profile + dated config rows) — every FR maps `odoo`; no SaaS
rows are introduced because none of these FRs touch DTE
generation/transmission (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`); the teledespacho
transmission surface is `06_customs-declarations.md`'s. Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is required by
this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | res.company + l10n_sv_special_regime.* | sv_spe_regime | ZF vs DPA distinct discriminators; feeds 02/04/05 by id |
| FR-002 | odoo | res.company | sv_spe_regime (parque/centro) + role defs | LSI custody roles ground 03's usuario-indirecto ledger |
| FR-003 | odoo | res.company | sv_spe_role, sv_spe_activity_admission, sv_spe_location_track, sv_spe_acuerdo_do_date | THE D15 row key; anchor = acuerdo D.O. date; snapshot-on-write per D15/D16 |
| FR-004 | odoo | res.company | sv_spe_oni_registration | ONI ≤5-días-hábiles clock via SV-FREP-FR-202..204 by id; MINEC/MH split informational |
| FR-005 | odoo | (informational) | — | 13_ frame note anchoring 07's DGA-facing registers; no automation surface |
| FR-006 | odoo | l10n_sv_special_regime.activity | regime_scope zf_* | SAC scope = product-catalog config; connected services beneficiaries-only gate |
| FR-007 | odoo | l10n_sv_special_regime.activity | exclusion_tier | Art. 6 a)-k)/1)-4) dated rows, 12_ print provenance; voluntary-suspension carve-out |
| FR-008 | odoo | l10n_sv_special_regime.activity | scope_predicate | per-letter predicates (d/i/g); local-market/retention surfaces owned by 03/05 by id |
| FR-009 | odoo | l10n_sv_special_regime.activity | regime_scope lsi_* | placement validation + co-located 1)-11) full-tax-routing flag |
| FR-010 | odoo | l10n_sv_special_regime.requisito(+.log) | kind zf_usuario_17a | US$500,000/2y · 50 · 5 jobs rows; valid_from = acuerdo D.O. date; headcount feed payroll/05-06 by id |
| FR-011 | odoo | l10n_sv_special_regime.requisito | kind zf_invernadero_17a | US$100,000 + 15 jobs + 5,000/1,000 m² + structure flag; breach split per FR-016 |
| FR-012 | odoo | l10n_sv_special_regime.requisito | kinds dpa_19a/19b | US$800,000 (existing-infrastructure exclusion rule) · 75 · 15; 19-B US$100,000/15; as printed |
| FR-013 | odoo | l10n_sv_special_regime.requisito | kind lsi_distribuidor_22 | 500 m² + DGA registration + register/manifest duties; ledgers owned by 03/07 by id |
| FR-014 | odoo | l10n_sv_special_regime.requisito | kinds lsi_bpo_23/lsi_medico_23 | US$150,000+10 jobs+1-y contract (breach year ⇒ ejercicio benefit loss); $10M/$3M [sic print] médico rows |
| FR-015 | odoo | res.company | sv_spe_benefit_state, sv_spe_state_reason | drives 02/03 exemption-row resolution + 05 routing by id; D16: imported regime history keeps prior states |
| FR-016 | odoo | res.company | benefit-state transitions | suspensión: tributes payable + ladder clock keeps running (consumed by 02); Art. 48 procedure link FR-019 |
| FR-017 | odoo | res.company | benefit-state transitions (LSI) | state transitions only; SMM-priced sanction values = 07's surface (payroll/02 by id) — nothing SMM here |
| FR-018 | odoo | res.company | inactivity monitors + sv_spe_dga_access_enabled | 12m ZF / 3m LSI dated monitors; DGA access disablement recorded as side effect |
| FR-019 | odoo | l10n_sv_special_regime.procedure (workflow states) | clocks 25/35/10/5/10-day/3/15 días hábiles | días-hábiles arithmetic via SV-FREP-FR-202..204 by id; Art. 48 resolution term printed as "DIEZ DÍAS" (calendar, as printed) |
| FR-020 | odoo | res.company/res.partner | sv_spe_declarante_mode, sv_spe_apoderado_data, fianza slots | fianza amount + exam/DACG detail = config-gaps (OQ-004); transmission surface = 06 by id |
| FR-021 | odoo | l10n_sv_special_regime.ruling | kind/filed_on/due_on/valid_until | consulta 15+15 días hábiles case-specific, no suspension; advance ruling 3-y validity stamped |
| FR-022 | odoo | l10n_sv_special_regime.municipio | name/valid_from/provenance | stale-static 13-municipio rows (SOQ-43 — no 2023 recompute); valid_to ~31-dic-2025 + 82_ dynamic-reference successor slot (OQ-5); metro/fuera track feeds 02 by id |
| FR-190 | odoo | l10n_sv_special_regime.requisito | kind lsi_centro_24a rows | 80_ Arts. 24/24-A centros requisitos (277-2013): 250k/20 BPO · 2M/15/4,000 m² médico · 500k/15 ancianos + general flags; ejercicio-loss semantics; DISTINCT from parque rows |
| FR-191 | odoo | l10n_sv_special_regime.beneficiary_type_change | from/to/solicitud/granted | 82_ Art. 8 (ZF Art. 44): ZF↔DPA cambio de tipo = prior MINEC solicitud; profile mutates only on grant |
| FR-192 | odoo | l10n_sv_special_regime.area_verde_rule | track/split/compensation | 82_ Arts. 2/5/9 (ZF 10.3.b / 18 d).5 / 46-A): 30% 10+20 ZF · 20% 10+10 DPA (ampliaciones/reducciones/traslados) · outside gate 10%/20% compensation + DOT/OPAMSS refs |
| FR-193 | odoo | res.company | sv_spe_prior_tan_excluded | 82_ Art. 10 (ZF 54-B inc. 1º): prior TAN operation + ISR payment bars qualification (dated, ~31-dic-2025) |
| FR-194 | odoo | res.company | sv_spe_location_equivalence = zf_user_in_lsi_parque | 82_ Art. 11 (ZF 54-I): ZF usuarios in LSI parques = as if in a zona franca; ZF row sets keep resolving; mirror of spe/03 FR-063 iii |
| FR-200 | odoo | l10n_sv_special_regime.dl_incentive (+ sv_spe_regime = project_incentive) | instrument/vigencia/admission/window fields | 95_ D.L. 95-2024 + 97_ D.L. 386-2025 + 108_ D.L. 411-2025 class row: instrument-keyed admission + window families (fixed-15y text-pinned vs event-bounded vs 108_ two-layer within decree vigencia 27-sep-2025→26-sep-2031); D15 rows consumed from 02 (FR-202/203/204 by id); ISR side via 54_ Art. 4.1 by id; 108_ ISR/IVA sides = taxation FR-417/419/420/421 by id |
| FR-201 | odoo | res.company/res.partner | sv_raex_state/sv_raex_date | 96_ D.L. 308-2025 identity row: MIGOB RAEX registration state only — no benefit machinery; Chapter V 30% levy = taxation-owned (SV-TAX-FR-405..416 by id); resolves EVID-167 pointer |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file (US$500,000/US$800,000/US$100,000/US$150,000/US$1,000,000 médico/
US$250,000 ancianos/centros US$250,000-US$2,000,000 (277-2013 values, W19
T3 — the pre-277 US$10,000,000/US$3,000,000 [sic] médico tiers superseded,
kept on historical rows), 50/75/20/15/10/5 jobs, 5,000/1,000/500/4,000 m²,
the 13-municipio list (valid_to ~31-dic-2025), the 25/35/10/5/3/15-day
procedure clocks) are code-text
values cited as printed under the SOQ-30 verification watch (§2) and live
as dated config rows with instrument provenance — never constants; the
per-beneficiary anchor is the acuerdo D.O. date (FR-003). Mid-year go-live
(D18): a migrating regime company's requisito logs, benefit states and
ladder computations ingest as `is_historical` rows with original-period
semantics (tiered ingestion per D18; no re-derivation). No hard gates
beyond the statutory state machine (D16 no-override: regime validity is
never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given an applicant qualified as ZF usuario under the Art. 17-A
  a) requisito (US$500,000 attainable in the first two years), when its
  fixed-asset investment bookings are recorded, then each booking logs
  against the beneficiary's dated requisito row (kind zf_usuario_17a,
  threshold_type investment_usd, valid_from = acuerdo D.O. date) with the
  operations-year anchor (FR-010).
- **AC-002:** Given a ZF usuario whose jobs requisito (50 permanent posts)
  is breached in year 3, when the breach determination is recorded, then
  the benefit state becomes suspendida with reason art17a_bc_jobs, the
  system marks import tributes and related taxes payable during the
  suspension, and the benefit-term computation continues accumulating
  (suspension does not interrupt the total benefit term) (FR-015, FR-016).
- **AC-003:** Given an LSI BPO usuario that fails to reach the US$150,000
  first-year investment in its second operations year, when the ejercicio
  closes, then the benefits for that fiscal year only are flagged lost
  (ejercicio_benefit_loss) with no revocation and no effect on other
  years' rows (FR-014).
- **AC-004:** Given a persona jurídica whose employee is authorized as
  apoderado especial aduanero (escritura pública + sufficiency exam
  recorded), when the poderdante's fianza is posted (DGA-fixed amount
  config slot), then the declarante mode apoderado_especial is active and
  the company's own customs declarations carry that declarante identity
  (transmission mechanics owned by `06` by id) (FR-020).
- **AC-005:** Given a ZF applicant located in Antiguo Cuscatlán, when its
  profile is saved, then its location track resolves to metro via the
  stale-static 13-municipio dated rows (no 2023-reorganization recompute),
  and the metro track is handed to `02`'s exemption-track resolution by id
  (FR-022, FR-003).
- **AC-006:** Given an LSI beneficiary with two recorded serious
  infringements, when a third serious infringement is recorded, then the
  benefit state becomes revocada per Art. 52 (third-grave rule) — with NO
  SMM-priced fine computed in this file (sanction values live in `07`)
  (FR-017).
- **AC-007:** Given a ZF beneficiary with 12 continuous months without
  regime operations (imports/exports), when the inactivity monitor fires,
  then the category-loss procedure opens with the 5-días-hábiles audiencia
  window (calendar engine by id) and, on final resolution, the state
  perdida_inactividad is stamped with the DGA deregistration recorded
  (FR-018, FR-019).
- **AC-008:** Given a BPO applicant qualifying as a parque usuario directo
  in 2026 with US$160,000 invested by month six, 12 permanent jobs and a
  9-month written contract, when the requisitos resolve, then all four
  277-2013 rows pass (US$150,000/6 months · 10 jobs · 6-month contract ·
  plan) — while the same applicant on the centros track needs US$250,000
  and 20 jobs (FR-014, FR-190; pre-277 1-year/US$10M rows never resolve
  for post-reform facts).
- **AC-009:** Given a TAN-operating company that paid ISR through 2025 and
  applies for ZF-usuario qualification in February 2026, when the
  application profile saves, then the 54-B prior-TAN exclusion flag
  (effective ~31-dic-2025) blocks the qualification, and a cambio of type
  from ZF usuario to DPA never mutates the profile without a granted
  MINEC solicitud reference (FR-193, FR-191).
- **AC-010:** Given a company admitted as a 95_ project titular via DGII
  resolución (prior notice filed, resolution issued) whose first
  exclusively-project utilidades arrive in ejercicio 2027, when the profile
  saves, then the regime resolves project_incentive with instrument
  dl95_2024 and window kind fixed_15y_from_first_utilidades anchored at
  2027, the dated rows hand off to `02` FR-202 by id, and no territorial
  machinery (acuerdo D.O. date, location track) engages (FR-200); given a
  partner covered by 96_, when its RAEX state is stamped registered, then
  only the identity flag records — no exemption row, no retention row, no
  benefit state ever engages for it in this wave (FR-201).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-30 carried: the regime consolidations ended 2012-2013 (12_ → D.L. 318-2013; 13_ → D.L. 121-2012; 74_ → D.L. 23-2012) — **W19 T3: the 14_/LSI half RESOLVED (80_ = consolidated thru D.L. 277-2013; LBs re-keyed 14_→80_) and the 12_ tail acquired as 82_ (D.L. 493-2025, vigencia ~31-dic-2025 — Arts. 2/10/11/17/18/19/28/44/46-A/54-B/54-I + 2-yr grace)**; remaining unverified: post-2013 LSI traffic (80_ tail), post-2025 ZF traffic beyond 82_, 13_/74_ beyond 2012 and 17b_ beyond 2008; all LBs cite as printed; re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-2 | SOQ-43 carried: the Art. 2 d) área-metropolitana 13-municipio list predates the 2023 municipal reorganization (CAT-013 kin); legal effect on membership unstated. FR-022 ships the list as stale-static dated rows (valid_to ~31-dic-2025) with NO recompute; the 82_ Art. 1 reform REPLACED the enumeration with a dynamic reference to the Ley de Desarrollo y Ordenamiento Territorial + Reglamento (see OQ-5) — the successor row lands when that law is acquired. | no | Takumi S7 (config watch) | open |
| OQ-3 | SOQ-31 carried: the Reglamento General de la Ley de Zonas Francas (mandated by 12_ Art. 51) is NOT in the corpus — solicitud/informe formats and DACG structures are delegated there. FR-019 exposes the procedure clocks as printed; the format-level details ship as config slots with NO defaults. Acquisition candidate ≥75. **W19 T3: FR-191's cambio-de-tipo requisitos and FR-192's permit surfaces also cite "su Reglamento" (82_ Arts. 8-9) — same config-slot family.** | no | Takumi S7 (sources watch) | open |
| OQ-4 | 74_ declarante exam mechanics: the statute (Art. 9) delegates the sufficiency-exam requirements and the fianza amount to DGA disposiciones administrativas de carácter general (not in corpus, 13_ Art. 36-A similar); FR-020 records escritura/exam/fianza at evidence depth with the exam content and fianza value as config-gaps — no invented procedural detail. | no | Takumi S7 (sources watch) | open |
| OQ-5 | 82_ Art. 1 (ZF-law Art. 2 d) substitution, W19 T3): the área metropolitana is now constituted by "los municipios y distritos contemplados en la Ley de Desarrollo y Ordenamiento Territorial del Área Metropolitana de San Salvador y de los Municipios Aledaños, y su Reglamento" — NEITHER instrument is in corpus; FR-022 ships the successor track as a config slot with NO shipped default (facts before ~31-dic-2025 resolve against the 13-municipio rows); acquisition candidate. | no | Takumi S7 (sources watch) | open |
| OQ-6 | 96_ Chapter V = a REAL 30%-withholding surface (W19 T4, EVID-397): D.L. 308-2025 Arts. 10-14 create a 30% tax on mandante-financed transactions collected by RETENCIÓN at source — Agentes de Retención Especial under a TWO-LIMB scope (Arts. 12/13): SSF-supervised financial-system institutions (general limb) +, ONLY for funds desde el exterior a favor de organizaciones sin fines de lucro, any other reception/canalization/transfer entity (NPO-qualified catch-all limb); DGT enteros within the 10 first días hábiles; electronic reports within 15; monthly 30% self-entero on domestic donations; CT 246/247/241 sanction routing — refuting the pre-reading "NOT a tax-withholding surface" hypothesis. OUT of this wave's scope bars: no retention FRs minted here; routed to a future taxation pass. Adjacent config-gaps: the RAEX reglamento (transparencia.gob.sv "versión pública" seen in search, not acquired) + the AT-provided forms of Arts. 13/14. | no | Takumi S7 (taxation-wave pointer) | **resolved-by-pointer** (W20: taxation/17 SV-TAX-FR-405..416 owns the retention engine) |
| OQ-7 | 97_ Art. 1 d) "el impuesto exclusivo de acuerdo al tipo de internación": WHICH exclusive tax(s) the phrase covers is corpus-silent — the `02` FR-203 arancel/gravamen row names the printed phrase as a config-gap with NO default enumeration (value discipline; `02` OQ-8); resolve when the operative DGA/DGII disposition or a later aclaración lands. | no | Takumi S7 (sources watch) | open |
