# SV — Taxation — IVA exemptions: the Art. 45/46 catalogs, the Art. 174 generic-nullity gate and the 167-A kill-switch (Ley IVA Arts. 44-46, 66, 71, 167-A, 174)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller; W24 T3 fold-in (108_ instrument-channel IVA exemptions) |
| Updated | 2026-08-24 |

## 1. Purpose

This file defines the functional requirements for the exempt-operations
surface of El Salvador's *Impuesto a la Transferencia de Bienes Muebles y a
la Prestación de Servicios* (transfer-of-movable-goods-and-services tax,
"IVA", D.L. 296-1992) — the *Título III* exemption catalogs: the FULL
Art. 45 b)-i) import/internación catalog (letter a) recorded as repealed:
diplomatic and consular representations under *convenios internacionales*
(international conventions) with the reciprocity condition; institutions and
international organisms El Salvador belongs to; the *equipaje de viajero*
(traveler's baggage) exemption as construed by the embedded D.L. 820-1994
interpretación auténtica — only personal effects of normal use or
consumption, never motor vehicles; goods donated from abroad to ISR-Art.-6-c
entities *calificadas previamente* (previously qualified) and donations under
convenios; municipal imports for *obras o beneficio directo de la respectiva
comunidad* (works or direct benefit of the respective community); the public
water and *alcantarillado* (sewerage) exemption — subject to the Art. 167-A
kill-switch that nullifies it at the vigencia of a future *régimen de
políticas sectoriales* (sectoral-policies regime) instrument; and the
public-passenger-transport vehicles exemption with the Reglamento de
Transporte Terrestre spec gate and the FIVE-YEAR transfer restriction
anchored on the *legalización de internación* (internation legalization)
date — early transfer makes the transferor pay the import IVA and the
acquirer the internal-transfer IVA per Art. 71); the FULL Art. 46 a)-l)
service catalog (health by DGII-*calificadas* institutions; residential
housing leases against the taxable commercial leases of Art. 17-d;
labor-dependence services and public employees; cultural spectacles;
education — only values paid to MINED-authorized institutions; the
deposit/captación/money-loan INTEREST exemption with its bank/
SSF-supervision/BCR-qualification/savings-credit-cooperative/
public-utility-financing institution gates; emission and placement of state
and official titles plus bolsa-primary-offering private titles, in the pago o
devengo de intereses; public utilities; terrestrial-only public passenger
transport; *seguros de personas* (person insurance) premiums and reinsurance
in general; AFP administration commissions under the SAP-law citation note;
and the Lotería Nacional); the Art. 174 generic-nullity gate — exemptions
granted by other laws produce NO effect for IVA (the Ley de Imprenta
exception noted as printed), so exemption reason codes are valid ONLY from
Arts. 45/46 plus ratified international instruments (the Art. 66 diplomatic
anchor); and the Rgto. Art. 16 technical-calification informe mechanism.
Exemption qualification, diplomatic/instrument status and every dated row
resolve as-of the tax-point date (D15), consumed from the framework file of
this wave by id (`taxation/07_iva-framework.md` SV-TAX-FR-176 operation
taxonomy, SV-TAX-FR-187 imports, SV-TAX-FR-191/192 services — never
restated).

It does **not** cover: the exportación/zero-rating regime (Arts. 74-77 — the
export file of the wave); the Art. 66 pro-rata machinery (the
determination/credit file owns it; the Art. 66 final inciso is cited here
ONLY as the ratified-instruments anchor); the Art. 71 four-year
fixed-asset early-transfer rule as a general surface (the adjustments-assets
file of this wave, `12_iva-adjustments-assets` — SV-TAX-FR-nnn pending,
owns it; this file cites Art. 71 directly with the 01_ LB for the 45-i
early-transfer consequence); the *tasa* (rate) and *base imponible* (Arts.
47-49 — the base/rate file of this wave; an exempt operation carries no base
computation at all); the débito/crédito determination and the
exempt-operation denominator feed (Arts. 62-67 — the determination/credit
file consumes this file's exemption codes by id); the F-07/DTE document
surfaces (e-invoicing/fiscal-reporting files, by id); and the CT procedure
belt. The excluidos regime (Arts. 28-32) is a subject-status regime, not an
exemption catalog — owned by the framework file (SV-TAX-FR-202..205, by
id).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). Embedded *interpretaciones auténticas* (authentic
interpretations) are part of 01_ AS PRINTED: **D.L. 820-1994 is
load-bearing here** (the Art. 45-d equipaje interpretation, printed inline
pp. 19-20; effective 25-mar-1994, eight days after the 17-mar-1994 D.O.
publication); D.L. 634-1993 (Art. 173 zone) and D.L. 645-2005 (Art. 14-III)
touch articles outside this file. Articles 113/123/124/161 are void (Sala de
lo Constitucional, 17-Dec-1992, expedientes 3-92/6-92) — none in this file's
range. **SOQ-54 vintage note (rides every 01_/02_ LB in this file):** the
consolidation's last reform stamp is D.L. 71-2015 — post-2015 reforms
unverified; corpus-internal signals negative (DTE stack 44_/45_,
Quincena-25 package 66_/67_, F-07 v14 manual silent); re-verify at
implementation. **Reglamento = 02_ survivors only** (D.E. 83-1992
consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass repeal =
D.E. 117-2001 stamp (3) — ruling R30(a), R17-bis kin); survivor articles =
1-10, 16-26, 29-30, 50-51 (+ 52 vigencia; corrected set per R30(a) addendum,
75_ Art. 147(b) audit 2026-08-20); this file cites Rgto. Art. 16 — a
survivor. **Version regimes recorded as rows, never silent drops:** the
transfer-side exemption chapter (Art. 44) and the Art. 45 letter a) are
DEROGADO by D.L. 877/00 (dead rows, omission markers — LB-001); the 45-h row
carries the Art. 167-A kill-switch (future instrument, not in corpus —
SOQ-58 watch); the 46-k row carries the stale SAP-law citation (D.L.
927-1996 superseded by D.L. 614 — SOQ-57, substance carried). **V1 citation
rule:** every LB row below cites 01_ or 02_ with the EVID id and the txt
page anchor (`=== PAGE n ===` markers of `01_Ley_IVA.pdf.txt` /
`02_Reglamento_IVA.pdf.txt`, verified this task); the SOQ-54 watch rides all
of them.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA (D.L. 296-1992, texto consolidado), Arts. 44 y 45 a) — **VERSION REGIME (dead rows)** | Under TÍTULO III "HECHOS EXIMIDOS DEL IMPUESTO … TRANSFERENCIAS": "Artículo 44.- DEROGADO (D.L. No. 877/00)(2)"; and within Art. 45: "a) DEROGADO (D.L. No. 877/00)". The transfer-side exemption chapter and the first import-exemption letter are repealed — the current print has NO transfer exemptions; Art. 45 opens "Estarán exentas del impuesto las siguientes importaciones e internaciones definitivas" | `sv/sources/01_Ley_IVA.pdf` | Arts. 44/45-a p.19 (EVID-313; verified 01_ txt lines 607-615) |
| LB-002 | Ley IVA, Art. 45 b)-c) | b) "Las efectuadas por las representaciones diplomáticas y consulares de naciones extranjeras y los agentes de las mismas acreditados en el país, de acuerdo con los convenios internacionales suscritos y aprobados por El Salvador y sujeto a condición de reciprocidad;" c) "Las efectuadas por instituciones u organismos internacionales a que pertenezca El Salvador y por sus funcionarios, cuando procediere de acuerdo con los convenios internacionales suscritos por El Salvador;" | `sv/sources/01_Ley_IVA.pdf` | Art. 45 b)-c) p.19 (EVID-313; verified 01_ txt lines 616-621) |
| LB-003 | Ley IVA, Art. 45 d) + D.L. 820 (23-feb-1994, D.O. 54 T.322 17-mar-1994), interpretación auténtica — embedded in 01_ as printed | Art. 45 d): "De bienes que efectuados por pasajeros, tripulantes de naves, aeronaves y otros vehículos, cuando estén bajo régimen de equipaje de viajero y tales especies se encuentren exoneradas de derechos de aduanas;" D.L. 820 Art. 1: the phrase "régimen de equipaje de viajero" refers "únicamente a la figura jurídica del equipaje de viajero y no al régimen jurídico contenido en la Ley de Equipaje de Viajeros procedentes del exterior; en consecuencia, los bienes que gozan de la exención señalada en el citado artículo, son únicamente aquellos efectos personales de uso o consumo normal del viajero, que por su naturaleza o cantidad se puede determinar que no son introducidos con fines comerciales; por lo que en ningún caso podrán considerarse incluidos en dicha figura los vehículos automotores". Art. 2: incorporated into the legal text; Art. 3: vigencia eight days after publication | `sv/sources/01_Ley_IVA.pdf` | Art. 45-d + D.L. 820 block pp.19-20 (EVID-313; verified 01_ txt lines 622-671) |
| LB-004 | Ley IVA, Art. 45 e)-f) | e) "De bienes donados desde el extranjero a las entidades a que se refiere el artículo 6 literal c) inciso segundo de la Ley de Impuesto sobre la Renta, calificadas previamente según lo dispone dicho artículo;" f) "Donaciones de acuerdo a convenios celebrados por El Salvador;" | `sv/sources/01_Ley_IVA.pdf` | Art. 45 e)-f) p.20 (EVID-313; verified 01_ txt lines 672-675) |
| LB-005 | Ley IVA, Art. 45 g) | "g) LAS EFECTUADAS POR LOS MUNICIPIOS, CUANDO LOS BIENES IMPORTADOS O INTERNADOS, SEAN PARA OBRAS O BENEFICIO DIRECTO DE LA RESPECTIVA COMUNIDAD; (1)" | `sv/sources/01_Ley_IVA.pdf` | Art. 45-g pp.20-21 (EVID-313; verified 01_ txt lines 676-685) |
| LB-006 | Ley IVA, Art. 45 h) + inciso final + Art. 167-A — **KILL-SWITCH ROW** | "h) DE SUMINISTRO DE AGUA, Y SERVICIO DE ALCANTARILLADO, PRESTADOS POR INSTITUCIONES PÚBLICAS; (4) (5)"; inciso final: "LA EXENCIÓN ESTABLECIDA EN EL LITERAL h) DE LA PRESENTE DISPOSICIÓN, ESTARÁ SUJETA A LO REGULADO EN EL ARTÍCULO 167-A DE ESTA LEY. (11)"; Art. 167-A: "LA EXENCIÓN ESTABLECIDA EN EL LITERAL h) DEL ARTÍCULO 45, QUEDARÁ SIN EFECTO A PARTIR DE LA VIGENCIA DEL INSTRUMENTO LEGAL QUE REGULE EL RÉGIMEN DE POLÍTICAS SECTORIALES. EN EL CITADO INSTRUMENTO SE DEFINIRÁ DE UNA MANERA EXPLÍCITA Y CATEGÓRICA, LA CESACIÓN DE LA EXENCIÓN CONTENIDA EN EL YA REFERIDO ARTÍCULO 45 LITERAL h) DE ESTA LEY.(11)" — the exemption dies at the vigencia of a future sectoral-policies instrument (not in corpus — watch row) | `sv/sources/01_Ley_IVA.pdf` | Art. 45-h p.21 + inciso final p.21 + Art. 167-A p.52 (EVID-313/331; verified 01_ txt lines 686-687, 701-702, 1871-1876) |
| LB-007 | Ley IVA, Art. 45 i) — **5-YEAR TRANSFER RESTRICTION** | "i) AUTOBUSES, MICROBUSES Y VEHÍCULOS DE ALQUILER DEDICADOS AL TRANSPORTE PÚBLICO DE PASAJEROS. DEL MISMO BENEFICIO GOZARÁN LAS TRANSFERENCIAS DE DOMINIO QUE REALICEN LOS IMPORTADORES DE DICHOS AUTOMOTORES, A FAVOR DE SUJETOS DEDICADOS AL TRANSPORTE PÚBLICO DE PASAJEROS. LOS AUTOBUSES, MICROBUSES Y VEHÍCULOS DE ALQUILER A QUE SE REFIERE ESTE LITERAL DEBERÁN REUNIR LAS CARACTERÍSTICAS NECESARIAS QUE, PARA EFECTOS DE SU DISTINCIÓN, SEÑALE EL REGLAMENTO DE TRANSPORTE TERRESTRE. LOS AUTOMOTORES INDICADOS ÚNICAMENTE PODRÁN SER TRANSFERIDOS HASTA DESPUÉS DE CINCO AÑOS DE LA LEGALIZACIÓN DE INTERNACIÓN Y PERMISO LEGAL CORRESPONDIENTE DE SU IMPORTACIÓN O ADQUISICIÓN, SEGÚN CORRESPONDA; SI FUEREN TRANSFERIDOS EN ESE PERÍODO PAGARÁN EL IMPUESTO POR LA IMPORTACIÓN, Y EL NUEVO ADQUIRIENTE PAGARÁ EL IMPUESTO, POR LA TRANSFERENCIA INTERNA, DE CONFORMIDAD A LO DISPUESTO EN EL ART. 71 DE ESTA LEY. (6) (12)" | `sv/sources/01_Ley_IVA.pdf` | Art. 45-i p.21 (EVID-313; verified 01_ txt lines 688-700) |
| LB-008 | Ley IVA, Art. 71 — **POINTER** | "EN CUANTO NO FORMAN PARTE DEL GIRO O ACTIVIDAD DEL CONTRIBUYENTE Y CARECEN DE HABITUALIDAD, NO CONSTITUYEN HECHO GENERADOR DEL IMPUESTO LAS TRANSFERENCIAS DE DOMINIO DE BIENES DEL ACTIVO FIJO O DE CAPITAL DE LOS CONTRIBUYENTES, A MENOS QUE ESA TRANSFERENCIA SE EFECTÚE ANTES DE LOS CUATRO AÑOS DE ESTAR LOS BIENES AFECTADOS A DICHO ACTIVO. (11)" — the early-fixed-asset-transfer taxation rule the 45-i restriction routes to; the adjustments-assets file of this wave (12_) owns the Art. 71 surface (SV-TAX-FR-nnn, pending) — consumed here for the 45-i early-transfer consequence, not restated as a general rule | `sv/sources/01_Ley_IVA.pdf` | Art. 71 p.37 (EVID-324; verified 01_ txt lines 1360-1364) |
| LB-009 | Ley IVA, Art. 46 a)-e) + inciso — FULL CATALOG (part 1) | "Estarán exentos del impuesto los siguientes servicios: a) De salud, prestados por instituciones públicas e instituciones de utilidad pública, calificadas por la Dirección General; b) De arrendamiento, subarrendamiento o cesión del uso o goce temporal de inmuebles destinados a viviendas para la habitación; c) Aquellos prestados en relación de dependencia regidos por la legislación laboral, y los prestados por los empleados públicos, municipales y de instituciones autónomas; d) De espectáculos públicos culturales calificados y autorizados por la Dirección General; e) Educacionales y de enseñanza, prestados por colegios, universidades, institutos, academias u otras instituciones similares;" + inciso: "EL BENEFICIO A QUE ALUDE EL INCISO ANTERIOR, COMPRENDERÁ ÚNICAMENTE LOS VALORES QUE COMO CONTRAPRESTACIÓN SE PAGUEN A INSTITUCIONES EDUCATIVAS PÚBLICAS O PRIVADA AUTORIZADAS POR EL MINISTERIO DE EDUCACIÓN.(11)" ["PRIVADA" sic as printed] | `sv/sources/01_Ley_IVA.pdf` | Art. 46 a)-e) pp.21-22 (EVID-314; verified 01_ txt lines 704-717) |
| LB-010 | Ley IVA, Art. 46 f) | "f) OPERACIONES DE DEPÓSITO, DE OTRAS FORMAS DE CAPTACIÓN Y DE PRÉSTAMOS DE DINERO, EN LO QUE SE REFIERE AL PAGO O DEVENGO DE INTERESES, REALIZADAS POR BANCOS O CUALQUIER OTRA INSTITUCIÓN QUE SE ENCUENTRE BAJO LA SUPERVISIÓN DE LA SUPERINTENDENCIA DEL SISTEMA FINANCIERO, ASOCIACIONES COOPERATIVAS O SOCIEDADES COOPERATIVAS DE AHORRO Y CRÉDITO, INSTITUCIONES FINANCIERAS DOMICILIADOS EN EL EXTERIOR QUE REALICEN ESTAS ACTIVIDADES AUTORIZADAS POR AUTORIDAD COMPETENTE EN SUS PAÍSES DE ORIGEN Y PREVIAMENTE CALIFICADOS POR EL BANCO CENTRAL DE RESERVA, ASÍ COMO LAS CORPORACIONES Y FUNDACIONES DE DERECHO PÚBLICO O DE UTILIDAD PÚBLICA EXCLUIDAS DEL PAGO DEL IMPUESTO SOBRE LA RENTA POR LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS DE ACUERDO AL ARTÍCULO 6 DE LA LEY QUE REGULA EL REFERIDO IMPUESTO Y QUE SE DEDIQUEN A OTORGAR FINANCIAMIENTO. EN AQUELLOS CASOS QUE SE NECESITA CALIFICACIÓN DEL BANCO CENTRAL DE RESERVA, LA ADMINISTRACIÓN TRIBUTARIA Y EL CITADO BANCO, EN CONJUNTO ELABORARÁN EL INSTRUMENTO NECESARIO, QUE INCLUIRÁ EL PROCEDIMIENTO Y REQUISITOS QUE GARANTICE EL CUMPLIMIENTO DEL PROPÓSITO DE LA EXENCIÓN REGULADA EN ESTE LITERAL; (8) (11)" ["INSTITUCIONES FINANCIERAS DOMICILIADOS" sic as printed] | `sv/sources/01_Ley_IVA.pdf` | Art. 46-f pp.21-22 (EVID-314; verified 01_ txt lines 718-741) |
| LB-011 | Ley IVA, Art. 46 g)-i) | "g) EMISIÓN Y COLOCACIÓN DE TÍTULOS VALORES POR EL ESTADO E INSTITUCIONES OFICIALES AUTÓNOMAS, ASÍ COMO POR ENTIDADES PRIVADAS CUYA OFERTA PRIMARIA HAYA SIDO PÚBLICA A TRAVÉS DE UNA BOLSA DE VALORES AUTORIZADA, EN LO QUE RESPECTA AL PAGO O DEVENGO DE INTERESES; (1)" "h) De suministro de energía eléctrica, agua y servicio de alcantarillado, prestados por instituciones públicas;" "i) De transporte público terrestre de pasajeros;" | `sv/sources/01_Ley_IVA.pdf` | Art. 46 g)-i) p.22 (EVID-314; verified 01_ txt lines 742-748) |
| LB-012 | Ley IVA, Art. 46 j)-l) | "j) DE SEGUROS DE PERSONAS, EN LO QUE SE REFIERE AL PAGO DE LAS PRIMAS; LO MISMO QUE LOS REASEGUROS EN GENERAL; (1)" "k) LAS COTIZACIONES APORTADAS POR EL PATRONO A LAS ADMINISTRADORAS DE FONDOS DE PENSIONES, EN LO QUE RESPECTA A LAS COMISIONES DE ADMINISTRACIÓN DE LAS CUENTAS DE LOS TRABAJADORES, DE ACUERDO CON LO ESTABLECIDO EN EL ARTÍCULO 16 LITERAL b) DE LA LEY DEL SISTEMA DE AHORRO PARA PENSIONES; y, (11)" "l) LOS NEGOCIOS DESARROLLADOS POR LA LOTERÍA NACIONAL DE BENEFICENCIA DE CONFORMIDAD A SU LEY Y REGLAMENTACIÓN. (11)" — 46-k cites the SAP law (D.L. 927-1996), superseded by D.L. 614: stale anchor, substance carried (SOQ-57) | `sv/sources/01_Ley_IVA.pdf` | Art. 46 j)-l) p.22 (EVID-314; verified 01_ txt lines 749-757) |
| LB-013 | Ley IVA, Art. 174 — **GENERIC-NULLITY GATE** | "DEROGATORIA DE EXENCIONES ESPECIFICAS. Artículo 174.- Las exenciones tributarias genéricas, totales o parciales otorgadas o que se otorguen por otras leyes, incluyendo las contenidas en la Ley de Creación de la Comisión Ejecutiva Hidroeléctrica del Río Lempa (CEL), exceptuando las amparadas por la Ley de Imprenta, no producirán ningún efecto en relación con este impuesto." — IVA exemptions live in this law (or ratified international instruments) only; other laws' generic exemptions are inert for IVA | `sv/sources/01_Ley_IVA.pdf` | Art. 174 p.55 (EVID-331; verified 01_ txt lines 1977-1981) |
| LB-014 | Ley IVA, Art. 66 inciso (missions/organisms) — **POINTER (instruments anchor)** | "… TAMPOCO SE INCLUIRÁN EN EL CÁLCULO DE LA PROPORCIONALIDAD, LAS OPERACIONES … LAS OPERACIONES DE VENTAS DE BIENES Y SERVICIOS QUE REALICEN LOS CONTRIBUYENTES A LAS MISIONES DIPLOMÁTICAS, CONSULARES, ORGANISMOS INTERNACIONALES Y A SUS MIEMBROS ACREDITADOS ANTE EL GOBIERNO DE LA REPÚBLICA DE EL SALVADOR, CUANDO ÉSTAS HAYAN SIDO DECLARADAS COMO EXENTAS O NO SUJETAS AL PAGO DEL IMPUESTO QUE REGULA ESTA LEY, CONFORME A LOS RESPECTIVOS INSTRUMENTOS INTERNACIONALES SUSCRITOS Y RATIFICADOS POR EL SALVADOR." — the ratified-instruments channel for exemption declarations; the pro-rata mechanics belong to the determination/credit file of this wave (cited here ONLY as the instruments anchor, never restated) | `sv/sources/01_Ley_IVA.pdf` | Art. 66 inciso p.35 (EVID-324; verified 01_ txt lines 1296-1301) |
| LB-015 | Reglamento IVA (D.E. 83-1992 consolidado), Art. 16 | "Artículo 16.- En las exenciones que, para su calificación, se requiera de conocimientos técnicos, tales como la consideración de productos en cuanto a su naturaleza, clasificación y otros, la Dirección General, solicitará, en caso de duda, informe sobre el particular a la autoridad competente. Lo dispuesto en el inciso anterior será aplicable en lo pertinente, a las prestaciones de servicios." | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 16 p.6 (EVID-335; verified 02_ txt lines 200-205) |
| LB-016 | Disposiciones Especiales y Transitorias de Apoyo al "Programa de Acceso Universal a la Energía en El Salvador" (108_), Art. 2 a)/b) + Art. 11: "Las personas naturales o jurídicas que tengan la calidad de contratistas o subcontratistas en el "Programa de Acceso Universal a la Energía en El Salvador" gozarán de las exenciones tributarias siguientes: a) Exención total del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, la cual se aplicará a las transferencias de bienes y prestaciones de servicios enunciados en el artículo 1 de las presentes disposiciones. b) Exención total por el período que realicen operaciones relacionadas con el Programa mencionado de impuestos y gravámenes a la importación e internación, de Derechos Arancelarios a la Importación, y del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios. El beneficio no podrá ser extensivo a ningún otro sujeto que pudiera intervenir en la operación de importación." Art. 11: "Las presentes disposiciones tienen carácter especial y priman sobre cualquier ley especial o general que las contradiga." | The IVA limbs of the 108_ energy-package SPECIFIC-INSTRUMENT exemption class: natural or juridical persons holding the quality of contratista or subcontratista in the Program enjoy a) TOTAL exemption of the IVA, applying to the transfers of goods and prestations of services enumerated in Art. 1 of the instrument; b) total exemption — for the period they realize Program-related operations — of importation/internación taxes and levies, of Derechos Arancelarios a la Importación, and of the IVA, with the express NO-CASCADE sentence: the benefit may not be extensive to any other subject that might intervene in the import operation. Art. 11: the provisions have especial character and PREVAIL over any special or general law that contradicts them (the express especialidad clause). GLOSS (per EVID-406): a specific-instrument grant — named program, operations bounded by the Art. 1 enumeration, beneficiary class of contratistas/subcontratistas GATED by the Art. 5 DGII resolución (≤10 días hábiles; format = config-gap, spe/02 OQ-10), windows dated per instrument (D.O. N° 181 T.448 26-sep-2025; decree vigencia 27-sep-2025 → 26-sep-2031, Art. 13 — a CURRENT operative window). ART. 174 WORKING READING (recorded here, NOT an OQ): Art. 174's nullity reaches exenciones GENÉRICAS of other laws; this grant is instrument-bounded (named program, enumerated operations, declared beneficiaries) and carries the Art. 11 express especialidad/prevalence clause under the CT Art. 6-b exoneración power recital (considerando VI) — so it encodes as a REGISTERED instrument channel on the FR-224 gate (amended W24 T3, channel (c)), never as a generic foreign-law claim. In-corpus precedent: 97_ Art. 1-a/b prints the identical clause (spe/02 LB-023 — project-spent window, no separate taxation/08 row minted in W19); operative registry FR = FR-420; the package family (beneficiary admission, per-contract vinculación, two-layer windows) = spe/02 SV-SPE-FR-204 by id, never restated here | `sv/sources/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf` | 108_ Art. 2 a)/b) p.2 + Art. 11 p.4 (EVID-406; 108_ txt PAGE 2, lines 95-114 + PAGE 4, lines 230-233; native asamblea text layer — intra-word cleaning per EV header; W24 T3) |

Dead text — never implementable as current law (recorded as notes/omission
markers, not FRs, per wave constraints): Art. 44 (the TRANSFERENCIAS
exemption chapter) and Art. 45 letter a) are DEROGADO by D.L. 877/00 — the
registry keeps the a)-row as an omission marker, never selectable (LB-001);
the D.L. 634-1993 interpretación auténtica embeds repealed-law sanctions for
pre-vigencia acts only (outside this file's operative surface); Art. 165's
incorporation note touches the Art. 17 regulation-mergers, not exemptions.
The 167-A instrument and the Reglamento de Transporte Terrestre specs are
NOT in the corpus — config-gap rows with watches (SOQ-58; OQ-5). The SOQ-54
vintage watch (§2 preamble) applies to every row above.

## 3. Functional Requirements

### 3.1 Import/internación exemptions — the Art. 45 catalog

- **SV-TAX-FR-206:** The system shall seed an IVA exemption-reason registry
  with the FULL Art. 45 b)-i) import/internación exemption catalog — every
  letter present, none dropped: b) diplomatic/consular reciprocity; c)
  international organizations; d) *equipaje de viajero*; e) donations from
  abroad to ISR-6-c entities; f) *convenio* donations; g) municipal obras;
  h) public water/alcantarillado; i) public-transport vehicles — with the
  letter-a row recorded as DEROGADO (D.L. 877/00 omission marker, present in
  the registry as `derogado_877_00`, never selectable); every exemption
  claim on an import/internación move must carry exactly one of these codes
  on top of the framework operation classification
  (`taxation/07_iva-framework.md` SV-TAX-FR-176/187 — by id).
  (LB-001; LB-002; LB-003; LB-004; LB-005; LB-006; LB-007; EVID-313)
- **SV-TAX-FR-207:** The system shall exempt the imports/internations of
  *representaciones diplomáticas y consulares* (diplomatic and consular
  representations) of foreign nations and their accredited agents ONLY when
  performed *de acuerdo con los convenios internacionales suscritos y
  aprobados por El Salvador* AND *sujeto a condición de reciprocidad*
  (subject to the condition of reciprocity — a recorded reciprocity flag on
  the mission); and the imports of institutions or international organisms
  to which El Salvador pertains, and of their *funcionarios*, only when
  proceeding per the suscrito convenios; both gates resolve as-of the
  tax-point date (D15: the convenio's and the reciprocity status at the
  import moment govern — later changes never re-classify a caused
  operation).
  (LB-002; EVID-313)
- **SV-TAX-FR-208:** The system shall exempt goods effected by passengers,
  crews of ships, aircraft and other vehicles ONLY under the *régimen de
  equipaje de viajero* AND while *exoneradas de derechos de aduanas*
  (exonerated from customs duties — the customs-exoneration precondition
  recorded on the entry), and shall construe "equipaje de viajero" per the
  D.L. 820 interpretación auténtica: ONLY *efectos personales de uso o
  consumo normal del viajero* (personal effects of the traveler's normal
  use or consumption) determinable by nature or quantity as NOT introduced
  with commercial ends — and NEVER *vehículos automotores* (motor
  vehicles): the system shall REJECT an equipaje-exemption claim on any
  motor-vehicle line (vehicle lines fall out of the exemption and post as
  taxed import).
  (LB-003; EVID-313)
- **SV-TAX-FR-209:** The system shall exempt donated goods from abroad
  ONLY when the recipient entity is one of the ISR Art. 6 literal c)
  inciso segundo entities *calificadas previamente* según dicho artículo —
  the prior ISR calificación reference recorded on the exemption claim; and
  shall exempt *donaciones de acuerdo a convenios celebrados por El
  Salvador* (donations under conventions celebrated by El Salvador) only
  with the convenio reference recorded; absent the respective reference the
  donation posts as a taxed import.
  (LB-004; EVID-313)
- **SV-TAX-FR-210:** The system shall exempt imports/internations effected
  by *los municipios* (the municipalities) only when the imported/interned
  goods are *para obras o beneficio directo de la respectiva comunidad*
  (for works or the direct benefit of the respective community) — a
  municipal acquirer plus the obras/community-direct-benefit destination
  recorded on the exemption claim.
  (LB-005; EVID-313)
- **SV-TAX-FR-211:** The system shall exempt the *suministro de agua y
  servicio de alcantarillado* (water supply and sewerage service) prestados
  por instituciones públicas as an import/internación exemption SUBJECT TO
  the Art. 167-A kill-switch: the exemption row ships as a DATED row with
  `valid_to` NULL and a kill-switch watch — the exemption *quedará sin
  efecto* (becomes without effect) at the *vigencia* of the instrumento
  legal regulating the *régimen de políticas sectoriales* (which must
  define the cessation *de una manera explícita y categórica*); the
  instrument is NOT in the corpus (SOQ-58 watch): when a dated instrument
  is configured, qualification resolves as-of the tax-point date (D15 —
  operations whose tax point precedes the vigencia remain exempt; at or
  after it, taxed; no retroactive re-classification).
  (LB-006; EVID-313/331)
- **SV-TAX-FR-212:** The system shall exempt *autobuses, microbuses y
  vehículos de alquiler dedicados al transporte público de pasajeros*
  (buses, microbuses and rental vehicles dedicated to public passenger
  transport) only when the vehicles REUNIR the distinguishing
  characteristics señaled by the *Reglamento de Transporte Terrestre*
  (terrestrial-transport regulation — spec gate: a config surface, the
  regulation is not in the corpus, OQ-5); and shall EXTEND the same benefit
  to the dominion transfers realized by the IMPORTERS of those vehicles in
  favor of subjects dedicated to public passenger transport (the
  importer→transporter link is exempt, not only the border entry).
  (LB-007; EVID-313)
- **SV-TAX-FR-213:** The system shall keep a per-vehicle 5-year transfer
  restriction register anchored on the *legalización de internación y
  permiso legal correspondiente* date (D15 dated row —
  `restriction_until` = legalización date + 5 years): the exempted vehicles
  *únicamente podrán ser transferidos hasta después de cinco años* de la
  legalización; if transferred within that period, the system shall
  generate BOTH tax events — the TRANSFEROR pays the IVA *por la
  importación* (the import-side IVA on the vehicle) and the NEW ACQUIRER
  pays the IVA *por la transferencia interna* (the internal-transfer IVA),
  *de conformidad a lo dispuesto en el Art. 71* (the early-transfer
  taxation rule — general surface owned by the adjustments-assets file of
  this wave, `12_iva-adjustments-assets` SV-TAX-FR-nnn pending; consumed
  here directly via the 01_ LB, not restated); the exemption flag is
  withdrawn from the vehicle record at the early-transfer event.
  (LB-007; LB-008; EVID-313)

### 3.2 Service exemptions — the Art. 46 catalog

- **SV-TAX-FR-214:** The system shall seed the service-exemption registry
  with the FULL Art. 46 a)-l) catalog — all 12 letters present, none
  dropped: a) salud; b) residential housing leases; c) labor-dependence
  services and public employees; d) cultural spectacles; e) education;
  f) deposit/captación/loan interest; g) state and bolsa-primary-offering
  titles; h) public utilities; i) terrestrial public passenger transport;
  j) seguros de personas and reaseguros; k) AFP administration commissions;
  l) Lotería Nacional — every exempt service line must carry exactly one of
  these codes on top of the framework service classification
  (`taxation/07_iva-framework.md` SV-TAX-FR-191/192 — by id).
  (LB-009; LB-010; LB-011; LB-012; EVID-314)
- **SV-TAX-FR-215:** The system shall exempt *servicios de salud* (health
  services) only when prestados by *instituciones públicas* (public
  institutions) or *instituciones de utilidad pública* (public-utility
  institutions) *calificadas por la Dirección General* (qualified by the
  DGII — calification reference recorded), and *espectáculos públicos
  culturales* (public cultural spectacles) only when both CALIFICADOS and
  AUTORIZADOS by the Dirección General (two distinct gates, both recorded);
  where the exemption calification requires technical knowledge (product
  nature, classification and similar), the system shall model the Rgto.
  Art. 16 mechanism: the Dirección General, in case of doubt, solicits an
  *informe* from the competent authority (equally applicable to service
  prestations) — the informe reference attaches to the calification record.
  (LB-009; LB-015; EVID-314/335)
- **SV-TAX-FR-216:** The system shall exempt *arrendamiento, subarrendamiento
  o cesión del uso o goce temporal* (lease, sublease or cession of
  temporary use or enjoyment) only of *inmuebles destinados a viviendas
  para la habitación* (immovables destined to dwellings for habitation —
  the residential-habitation destination test recorded on the lease), and
  shall NOT exempt leases of immovables destined to commercial, industrial,
  services or any other activity — that surface stays TAXED under the
  Art. 17-d service catalog (`taxation/07_iva-framework.md` SV-TAX-FR-192
   by id); a mixed-use immovable requires destination allocation,
   exemption applying only to the residential-habitation part **[DESIGN —
   default allocation; statute silent]**.
   (LB-009; EVID-314)
- **SV-TAX-FR-217:** The system shall exempt services *prestados en
  relación de dependencia regidos por la legislación laboral* (rendered
  under an employment relationship governed by labor legislation) and
  services rendered by *empleados públicos, municipales y de instituciones
  autónomas* (public, municipal and autonomous-institution employees) — the
  labor-dependence link or the public-employee status recorded as the
  exemption ground.
  (LB-009; EVID-314)
- **SV-TAX-FR-218:** The system shall exempt *servicios educacionales y de
  enseñanza* (educational and teaching services) per the stamp-11 inciso:
  the benefit comprises *ÚNICAMENTE los valores que como contraprestación
  se paguen a instituciones educativas públicas o privada [sic] autorizadas
  por el Ministerio de Educación* — ONLY the values paid as consideration
  to public or private educational institutions AUTHORIZED BY MINED; the
  MINED-authorization flag on the payee institution is a hard gate — a
  payment to a colegio, universidad, instituto, academia or similar
  institution WITHOUT the MINED authorization is TAXED (the base-catalog
  sentence is narrowed by the inciso; no orphan "educational services"
  exemption exists).
  (LB-009; EVID-314)
- **SV-TAX-FR-219:** The system shall exempt *operaciones de depósito, de
  otras formas de captación y de préstamos de dinero* (deposit, other
  capture-form and money-loan operations) ONLY in *lo que se refiere al
  pago o devengo de intereses* (as to the payment or accrual of INTEREST —
  the exemption scope is the interest component, never the principal), and
  only when realized by an institution in one of the statutory families:
  bancos or ANY institution under the supervision of the
  *Superintendencia del Sistema Financiero* (SSF); *asociaciones
  cooperativas o sociedades cooperativas de ahorro y crédito*
  (savings-and-credit cooperatives); foreign financial institutions
  authorized by the competent authority of their origin country AND
  *previamente calificados por el Banco Central de Reserva* (previously
  qualified by the BCR); and *corporaciones y fundaciones de derecho
  público o de utilidad pública* excluded from ISR by DGII per ISR Art. 6
  that dedicate to granting financing — the institution-family and
  qualification flags recorded per payee (`ssf_supervised` ·
  `cooperativa_ahorro_credito` · `bcr_calificada` — sourced from the
  BCR qualification list (SOQ-56 resolved, W18: 101_-105_ = the
  DGII+BCR joint Instructivo the law mandates + circulars CD-39/2021 /
  CD-24/2023 + the live lists; the exemption flag = BCR-list membership
  with current per-institution vigencia; dated data — 104_/105_ as-of
  08-ago-2026, refresh at wave cadence); `isr6_excluded_financing`); a
  payee without the corresponding flag yields a TAXED interest line.
  (LB-010; EVID-314)
- **SV-TAX-FR-220:** The system shall exempt the *emisión y colocación de
  títulos valores* (emission and placement of securities) by the Estado
  (the State) and *instituciones oficiales autónomas* (official autonomous
  institutions), and by private entities whose *oferta primaria haya sido
  pública a través de una bolsa de valores autorizada* (primary offering
  was public through an authorized securities exchange) — ONLY in *lo que
  respecta al pago o devengo de intereses* (as to the payment or accrual of
  interest); issuer-kind flag (`estado` · `oficial_autonoma` ·
  `bolsa_primary_public_offering`) required — a private title placed
  outside a bolsa primary public offering yields a TAXED interest line.
  (LB-011; EVID-314)
- **SV-TAX-FR-221:** The system shall exempt public utilities —
  *suministro de energía eléctrica, agua y servicio de alcantarillado*
  (electricity supply, water and sewerage) prestados por instituciones
  públicas (the 46-h SERVICE-side row; the 45-h IMPORT-side
  water/alcantarillado exemption is a DISTINCT row carrying its own 167-A
  kill-switch — the 46-h row is NOT subject to 167-A as printed) — and
  shall exempt *transporte público terrestre de pasajeros* (terrestrial
  public passenger transport) ONLY: aerial and maritime PASSENGER transport
  remains TAXED under the Art. 17-m catalog
  (`taxation/07_iva-framework.md` SV-TAX-FR-192 by id) — the
  transport-mode gate (terrestrial · aerial · maritime) is a hard switch on
  the exemption claim.
  (LB-011; EVID-314)
- **SV-TAX-FR-222:** The system shall exempt *seguros de personas* (person
  insurance) in *lo que se refiere al pago de las primas* (as to the
  payment of premiums — person-insurance branch only; other insurance
  branches' premiums are TAXED) and *los reaseguros en general* (reinsurance
  in general); and shall exempt *los negocios desarrollados por la Lotería
  Nacional de Beneficencia* (the businesses developed by the National
  Charity Lottery) *de conformidad a su ley y reglamentación* (per its law
  and regulation — the Lotería-law conformity recorded as the ground).
  (LB-012; EVID-314)
- **SV-TAX-FR-223:** The system shall exempt *las cotizaciones aportadas
  por el patrono a las administradoras de fondos de pensiones* (the
  employer's contributed quotations to the pension-fund administrators) in
  *lo que respecta a las comisiones de administración de las cuentas de los
  trabajadores* (as to the administration commissions on the workers'
  accounts) — the employer-cotization/commission component only, not the
  cotizaciones themselves; SOQ-57 dated note: the printed anchor cites
  "Artículo 16 literal b) de la Ley del Sistema de Ahorro para Pensiones"
  (the SAP law, D.L. 927-1996), superseded by D.L. 614 (SIP, effective
  2022-12-29 — R23/R24 kin): the exemption SUBSTANCE is carried for
  pension-administration commissions under the current regime and the
  stale anchor is recorded as printed, re-verification under the SIP
  regime riding the OQ.
  (LB-012; EVID-314)

### 3.3 The Art. 174 generic-nullity gate

- **SV-TAX-FR-224:** The system shall enforce the exemption SOURCE gate:
  an IVA exemption may rest ONLY on (a) an Art. 45 or Art. 46 letter of
  this law (the registries of FR-206/FR-214), (b) a ratified
  international instrument — the Art. 66 anchor channel: sales of goods
  and services to *misiones diplomáticas, consulares, organismos
  internacionales y a sus miembros acreditados* declared exempt or
  no-sujetas *conforme a los respectivos instrumentos internacionales
  suscritos y ratificados por El Salvador* (instrument registration
  with ratification reference required), or (c) — **W24 T3
  amendment** — a REGISTERED specific special-law instrument of the
  108_ class: an instrument-bounded grant whose row records the
  instrument id, its D.O. anchor, its vigencia and its EXPRESS
  especialidad clause (108_ Art. 11, LB-016), the exemption bounded to
  the declared beneficiary class and the instrument-enumerated
  operations AS PRINTED (named program; operative registry = FR-420) —
  the channel is config-gated PER INSTRUMENT, never user-defined.
  GENERIC total or partial exemptions granted — or to be granted — by
  OTHER LAWS (the printed statutory exemplar: the Ley de Creación de la
  Comisión Ejecutiva Hidroeléctrica del Río Lempa (CEL)) produce NO
  effect whatsoever for this tax, SAVE the *excepción amparada por la
  Ley de Imprenta* (the Printing-Law exception — noted as printed, a
  recorded carve-out row); the configuration shall REJECT any
  foreign-law generic-exemption claim (a "ley especial" exemption
  reason never validates) and shall expose no user-defined exemption
  source beyond the three channels. ART. 174 RECONCILIATION (working
  reading per the LB-016 gloss, recorded in-row — not an OQ): the
  nullity clause reaches *exenciones genéricas*; channel (c) admits
  only instrument-bounded grants with express especialidad + vigencia
  (in-corpus precedent 97_ = spe/02 LB-023; 108_ the first CURRENT
  member), so the rejection limb stands UNCHANGED for generic
  foreign-law claims.
  (LB-013; LB-014; LB-016; EVID-331/324/406)

### 3.4 Instrument-channel exemptions — the 108_ specific-instrument registry (W24 T3)

- **SV-TAX-FR-420:** The system shall extend the exemption-reason
  registry (the FR-206/FR-214 chassis) with dated instrument-channel
  rows for the 108_ energy-package IVA exemptions (instrument
  `dl411_2025`, D.O. N° 181 T.448 26-sep-2025, decree vigencia
  27-sep-2025 → 26-sep-2031 — Art. 13; the per-contract event window
  inside it consumed from spe/02 SV-SPE-FR-204 by id, both layers
  stamped on every dated row, never collapsed): (a) TRANSFERS/SERVICES
  rows — IVA exención TOTAL on the transfers of bienes and
  prestaciones of servicios enumerated in Art. 1 of the instrument,
  for operations of DGII-DECLARED beneficiaries only (the
  contratista/subcontratista declared per the Art. 5 resolución;
  per-contract vinculación + event window per SV-SPE-FR-204 by id,
  never restated here); (b) IMPORT/INTERNACIÓN rows — exención total
  de impuestos y gravámenes a la importación e internación + Derechos
  Arancelarios a la Importación + IVA on Program-related imports for
  the period of Program-related operations, carrying the NON-CASCADE
  GUARD: the benefit does NOT extend to *ningún otro sujeto que
  pudiera intervenir en la operación de importación* (no-cascade flag
  on the row — a third-party freight forwarder, agent or intermediary
  never inherits the exemption). Every 108_ exemption claim cites the
  instrument channel — FR-224-(c): the registered instrument row with
  its D.O. anchor, vigencia and especialidad clause (LB-016) — NEVER a
  generic free-text claim, and resolves as-of the tax-point date (D15)
  against the beneficiary's per-contract event window inside the
  decree vigencia.
  (LB-016; EVID-406 W24 T3; cross-ref SV-SPE-FR-204, FR-224, FR-206,
  FR-214)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the Art. 45/46 letters ship as registry seed
rows; the 167-A kill-switch ships as a dated row with NULL `valid_to` plus
watch; the 5-year restriction anchors per vehicle on its legalización date
(D15 dated rows computed at record time). Layer semantics: this file
introduces Odoo-side exemption-classification data only (wave default
`odoo`; see §5). **Interface entity for the wave's later files
(determination/credit, base/rate, adjustments-assets) and Task 7's index:**
the exemption-reason registry + qualification flags + the vehicle
restriction register below.

**Exemption-reason registry:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.exemption.reason (new) | code, name, legal_anchor, side | char / char / char / select | Art. 45 letters b)-i) (side=import) + Art. 46 letters a)-l) (side=service); anchor string per row | FR-206, FR-214 |
| l10n_sv.iva.exemption.reason | letter, status, valid_from, valid_to | char / select / date / date | letter: b..i (Art. 45) / a..l (Art. 46); status: active · derogado_877_00 (the Art. 45-a omission marker — never selectable) | FR-206 |
| l10n_sv.iva.exemption.reason (45-h row) | kill_switch_art | char + watch flag | 167-A: `valid_to` NULL until the sectoral-policies instrument is dated; instrument reference field (SOQ-58 watch) | FR-211 |
| l10n_sv.iva.international.instrument (new) | name, kind, ratification_ref, vigencia | char / select / char / date | kind: convenio_suscrito_aprobado · convenio_suscrito · instrumento_ratificado; D15: qualification resolves as-of tax-point date | FR-207, FR-209, FR-224 |
| l10n_sv.iva.special.instrument (new) | instrument_id, do_anchor, vigencia_from, vigencia_to, especialidad_clause | char / char / date / date / char | REGISTERED specific special-law instruments — FR-224 channel (c), config-gated per instrument, never user-defined; dl411_2025: D.O. 181 T.448 26-sep-2025, vigencia 27-sep-2025 → 26-sep-2031, Art. 11 especialidad as recorded | FR-224, FR-420 |
| l10n_sv.iva.exemption.reason (instrument rows) | instrument_id, non_cascade, beneficiary_declaration | m2o / boolean / m2o | 108_ dated rows (dl411_2025): transfers/services (IVA exención total, Art. 1-enumerated) + import/internación (impuestos y gravámenes + DAI + IVA) — import rows carry non_cascade = true (the benefit never extends to any other subject of the import operation); beneficiary = DGII-declared per the Art. 5 resolución; vinculación + event window per SV-SPE-FR-204 by id | FR-420 |

**Import-side exemption claims (account.move — SV extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (import/internación) | l10n_sv_iva_exempt_reason_id | m2o | Art. 45 b)-i) registry rows only | FR-206 |
| account.move (45-b/c claim) | l10n_sv_iva_reciprocity_ok, l10n_sv_iva_convenio_id | boolean / m2o | reciprocity flag + convenio reference (both required for 45-b; convenio for 45-c/funcionarios) | FR-207 |
| account.move (45-d claim) | l10n_sv_iva_equipaje_gate | select | personal_effects_non_commercial · customs_exonerated (both required); motor-vehicle lines hard-rejected | FR-208 |
| account.move (45-e/f claim) | l10n_sv_iva_isr6c_calificacion_ref, l10n_sv_iva_convenio_id | char / m2o | prior ISR-6-c calificación reference (45-e) or convenio reference (45-f) | FR-209 |
| account.move (45-g claim) | l10n_sv_iva_municipal_benefit | select | obras_comunidad · beneficio_directo_comunidad + municipal acquirer | FR-210 |
| account.move (45-h claim) | l10n_sv_iva_kill_switch_snapshot | date + boolean | 167-A status snapshotted as-of tax-point date; instrument vigencia from config | FR-211 |
| account.move (45-i claim) | l10n_sv_iva_transport_spec_ok, l10n_sv_iva_transporter_transfer | boolean / boolean | Reglamento-de-Transporte-Terrestre spec gate (config); importer→transporter link extension | FR-212 |

**Vehicle 5-year restriction register:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.vehicle.restriction (new) | vehicle_lot_id, legalizacion_date, restriction_until | m2o / date / date (computed) | `restriction_until` = legalización + 5 years (D15 dated row, snapshot-on-write) | FR-213 |
| l10n_sv.iva.vehicle.restriction | transfer_events | one2many | early_transfer events: import-IVA assessment (transferor) + internal-transfer-IVA assessment (acquirer) per Art. 71 | FR-213 |

**Service-side exemption claims (account.move.line / res.partner — SV extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | l10n_sv_iva_exempt_reason_id | m2o | Art. 46 a)-l) registry rows only | FR-214 |
| res.partner | l10n_sv_iva_dgii_calificada, l10n_sv_iva_espectaculo_autorizado | boolean / boolean | 46-a utilidad-pública calification; 46-d double gate (calificado + autorizado) | FR-215 |
| res.partner | l10n_sv_iva_mined_authorized | boolean (validated) | hard gate for 46-e education payments | FR-218 |
| res.partner | l10n_sv_iva_fin_family | multi-select + flags | banco · ssf_supervised · cooperativa_ahorro_credito · bcr_calificada (sourced from BCR qualification list — 101_-105_; dated list, as-of 08-ago-2026, refresh at cadence) · isr6_excluded_financing | FR-219 |
| res.partner | l10n_sv_iva_title_issuer_kind | select | estado · oficial_autonoma · bolsa_primary_public_offering (46-g) | FR-220 |
| product.template (SV extension) | l10n_sv_iva_transport_mode, l10n_sv_iva_insurance_branch | select / select | terrestrial · aerial · maritime (46-i gate); personas · reaseguro vs taxed branches (46-j) | FR-221, FR-222 |
| account.move.line | l10n_sv_iva_interest_scope_only | boolean | 46-f/46-g exempt the interest component only (pago o devengo de intereses) | FR-219, FR-220 |
| res.partner (AFP) | l10n_sv_iva_afp_commission_exempt | boolean + stale-anchor note | 46-k employer-cotization administration commissions; SAP citation note (SOQ-57) | FR-223 |
| account.move.line (exemption claim) | l10n_sv_iva_exemption_source | select | art45_letter · art46_letter · instrumento_ratificado · instrumento_especial_ley (FR-224-c, W24 T3 — registered instrument row required, never user-typed) — the Art. 174 gate rejects any other source | FR-224, FR-420 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = exemption-classification/gating
logic living in the LGPL client. No SaaS rows are introduced in this file:
nothing here touches DTE generation/transformation — exemption reason codes
flow to the document surfaces as data consumed by the e-invoicing file (by
id). Model names are stable across Odoo 17/18/19/20 (`account.move`,
`account.move.line`, `product.template`, `res.partner`; the two new
registries are client-side master data). D15 doctrine (binding): exemption
qualification, instrument/reciprocity status and every dated row resolve
as-of the tax-point date snapshotted on the record; corrections use
ORIGINAL-period parameters; the vehicle restriction anchors on the
legalización date (a fact date, not a parameter date).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-206 | odoo | l10n_sv.iva.exemption.reason | Art. 45 b)-i) seed | FULL catalog, no letter dropped; a-row = derogado_877_00 omission marker (D.L. 877/00), never selectable; rides T1 SV-TAX-FR-176/187 import ops |
| FR-207 | odoo | account.move (import) + l10n_sv.iva.international.instrument | reciprocity_ok + convenio ref | 45-b: convenio suscrito Y aprobado + reciprocity; 45-c: convenio suscrito; D15 as-of tax-point resolution |
| FR-208 | odoo | account.move (import) | equipaje_gate | D.L. 820 (effective 25-mar-1994): personal effects only, non-commercial by nature/quantity; customs-exoneration precondition; motor vehicles NEVER — hard reject |
| FR-209 | odoo | account.move (import) | isr6c_calificacion_ref / convenio ref | 45-e prior ISR-6-c calificación reference; 45-f convenio reference; absent ref ⇒ taxed |
| FR-210 | odoo | account.move (import) | municipal_benefit | 45-g: municipal acquirer + obras/beneficio-directo destination |
| FR-211 | odoo | l10n_sv.iva.exemption.reason (45-h) + account.move snapshot | kill_switch_art + snapshot | 167-A: exemption dies at the sectoral-policies instrument vigencia; `valid_to` NULL + SOQ-58 watch; D15 as-of tax-point |
| FR-212 | odoo | account.move (import) + product.template | transport_spec_ok + transporter-transfer extension | Reglamento-de-Transporte-Terrestre specs = config surface (OQ-5); importer→transporter dominion transfers share the benefit |
| FR-213 | odoo | l10n_sv.iva.vehicle.restriction | legalizacion_date + restriction_until + transfer_events | 5-year window per vehicle (D15 dated row); early transfer ⇒ import IVA (transferor) + internal-transfer IVA (acquirer) per Art. 71 — general Art. 71 surface owned by 12_iva-adjustments-assets (SV-TAX-FR-nnn pending) |
| FR-214 | odoo | l10n_sv.iva.exemption.reason | Art. 46 a)-l) seed | FULL catalog, all 12 letters, no drops; rides T1 SV-TAX-FR-191/192 service classification |
| FR-215 | odoo | res.partner + calification record | dgii_calificada / espectaculo autorizado + informe ref | 46-a utilidad-pública calification; 46-d calificado AND autorizado; Rgto. Art. 16 informe mechanism in technical-doubt cases |
| FR-216 | odoo | product.template (lease) + account.move.line | residential destination test | 46-b viviendas-para-la-habitación only; commercial/industrial/services leases stay taxed per 17-d (T1 FR-192 by id); mixed-use allocation [DESIGN — default allocation; statute silent] |
| FR-217 | odoo | account.move.line | dependence/public-employee ground | 46-c labor-law relación de dependencia + public/municipal/autonomous employees |
| FR-218 | odoo | res.partner (institution) | mined_authorized hard gate | 46-e stamp-11 inciso: ONLY values paid to MINED-authorized public/private institutions; non-authorized academies taxed |
| FR-219 | odoo | res.partner + account.move.line | fin_family flags + interest_scope_only | 46-f: interest only (pago o devengo); SSF supervision · cooperativas · BCR-qualified foreign (flag sourced from BCR qualification list — 101_-105_) · ISR-6-excluded financing corporations/foundations |
| FR-220 | odoo | res.partner + account.move.line | title_issuer_kind + interest_scope_only | 46-g: Estado/oficiales autónomas + bolsa-primary-public-offering privates; interest only; non-bolsa private titles taxed |
| FR-221 | odoo | product.template | transport_mode + utilities row | 46-h service-side utilities (NOT 167-A-subjected, unlike 45-h import-side); 46-i terrestrial only — air/sea passengers taxed per 17-m (T1 FR-192 by id) |
| FR-222 | odoo | product.template (insurance/lottery) | insurance_branch + lottery ground | 46-j seguros de personas premiums + reaseguros general; other branches taxed; 46-l Lotería Nacional per its law |
| FR-223 | odoo | res.partner (AFP) + account.move.line | afp_commission_exempt + stale-anchor note | 46-k employer-cotización administration commissions; SAP citation D.L. 927-1996 stale (superseded by D.L. 614) — substance carried, SOQ-57 re-verification under SIP |
| FR-224 | odoo | account.move.line + exemption-reason registry | exemption_source gate | Art. 174: sources = Art. 45/46 letters + ratified instruments (Art. 66 anchor) + **W24 T3 channel (c)** registered specific special-law instruments (108_ class: instrument id + D.O. anchor + vigencia + express especialidad on the row; config-gated per instrument, never user-defined); other laws' GENERIC exemptions (CEL exemplar) NO effect; Ley de Imprenta exception as printed; foreign-law GENERIC claims rejected — rejection limb unchanged |
| FR-420 | odoo | l10n_sv.iva.special.instrument + exemption.reason (instrument rows) | 108_ registry rows | Transfers/services (IVA exención total, Art. 1-enumerated, DGII-declared beneficiaries) + import/internación (impuestos y gravámenes + DAI + IVA, non-cascade flag — never extends to any other subject of the import operation); exemption reason cites the FR-224-c instrument row, never a generic claim; vinculación + event window per SV-SPE-FR-204 by id; D15 as-of tax-point |

Version-regime notes (D12/D15): FR-208 records the D.L. 820-1994
authentic-interpretation cutover (effective 25-mar-1994 — eight days after
the 17-mar-1994 D.O. publication; equipaje imports before that date apply
the uninterpreted Art. 45-d text — dated behavior note). FR-206/LB-001
record the D.L. 877/00 version regime (Art. 44 + 45-a dead rows). FR-211
carries the 167-A kill-switch regime: NULL `valid_to` + watch until the
sectoral-policies instrument is dated, then a dated exemption row with
D15 as-of-tax-point qualification (SOQ-58). FR-213 anchors the 5-year
window on the legalización date (dated row per vehicle, snapshot-on-write).
FR-420's instrument rows are regime-dated (108_ dl411_2025: decree vigencia
27-sep-2025 → 26-sep-2031 with the per-contract event window inside it —
both layers on every dated row, never collapsed; spe/02 SV-SPE-FR-204 by
id); the FR-224 channel-(c) Art. 174 reconciliation is recorded in-row,
not as an OQ.
FR-223 carries the SOQ-57 stale-anchor note (SAP → SIP, substance carried).
FR-219's `bcr_calificada` is sourced from the BCR qualification list
(SOQ-56 resolved, 101_-105_: exemption flag = list membership with
current vigencia — dated data, refresh at wave cadence).
The SOQ-54 consolidation watch rides every LB (§2 preamble) — re-verify
against a current official consolidation at implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a diplomatic mission's import with a recorded convenio
  suscrito y aprobado and the reciprocity flag set, when the exemption
  claim resolves, then the import posts EXEMPT under 45-b; given the
  reciprocity flag unset, then the claim is REJECTED and the import posts
  taxed (FR-207).
- **AC-002:** Given an equipaje-line entry of a passenger's personal
  effects (clothing, used items) exonerated from customs duties, when the
  claim resolves, then it posts EXEMPT under 45-d; given a motor vehicle
  declared as equipaje, then the claim is HARD-REJECTED (D.L. 820: "en
  ningún caso … los vehículos automotores") and the vehicle posts as a
  taxed import (FR-208).
- **AC-003:** Given donated medical equipment from abroad to an ISR-Art.-6-c
  entity WITHOUT the prior calificación reference, when the claim resolves,
  then it is REJECTED and the import posts taxed; given the calificación
  reference recorded, then it posts EXEMPT under 45-e (FR-209).
- **AC-004:** Given a municipality's import of pipes destined for a
  community water project (obras de la respectiva comunidad), when the
  claim resolves, then it posts EXEMPT under 45-g (FR-210).
- **AC-005:** Given a 167-A sectoral-policies instrument configured with
  vigencia 2027-01-01, when a public-institution water-supply import with
  tax point 2026-12-15 resolves, then it posts EXEMPT under 45-h; given the
  same import with tax point 2027-01-05, then it posts TAXED (kill-switch
  at vigencia, D15 as-of resolution) (FR-211).
- **AC-006:** Given a 45-i-exempt bus whose legalización de internación
  date is 2024-06-01 (restriction until 2029-06-01), when its transfer is
  recorded at 2027-06-01 (year 3), then BOTH events generate: the
  transferor owes the IMPORT IVA and the new acquirer owes the
  internal-transfer IVA per Art. 71, and the vehicle's exemption flag is
  withdrawn; given the same bus transferred at 2029-07-01, then the
  transfer is exempt (5-year window elapsed) (FR-213).
- **AC-007:** Given a cultural spectacle authorized AND calificadas by the
  Dirección General, when the service line resolves, then it posts EXEMPT
  under 46-d; given a spectacle with only one of the two gates, then it
  posts TAXED (FR-215).
- **AC-008:** Given a lease of an apartment destined to vivienda para la
  habitación, when the line resolves, then it posts EXEMPT under 46-b;
  given a lease of the same building's ground-floor storefront for retail
  activity, then it posts TAXED per Art. 17-d (FR-216).
- **AC-009:** Given a $120.00 tuition payment to a MINED-authorized private
  academy, when the line resolves, then it posts EXEMPT under 46-e; given
  the same payment to a non-MINED-authorized academy, then the exemption
  is REJECTED and the line posts TAXED (stamp-11 inciso) (FR-218).
- **AC-010:** Given a loan-interest accrual of a bank under SSF
  supervision, when the line resolves, then the INTEREST component posts
  EXEMPT under 46-f (principal never exempt); given the same interest from
  a foreign financial institution WITHOUT the BCR-qualification flag, then
  the interest line posts TAXED (config-gap flag absent) (FR-219).
- **AC-011:** Given interest from a private bond whose primary offering was
  public through an authorized bolsa, when the line resolves, then it
  posts EXEMPT under 46-g; given interest from a privately placed private
  title (no bolsa primary offering), then it posts TAXED (FR-220).
- **AC-012:** Given a terrestrial public bus passenger ticket, when the
  line resolves, then it posts EXEMPT under 46-i; given an international
  air passenger ticket, then it posts TAXED per Art. 17-m (transport-mode
  gate) (FR-221).
- **AC-013:** Given a person-insurance (seguro de vida) premium payment,
  when the line resolves, then it posts EXEMPT under 46-j; given a vehicle
  damage-insurance premium, then it posts TAXED (person branch only);
  given a reinsurance premium (any branch), then it posts EXEMPT
  (reaseguros en general) (FR-222).
- **AC-014:** Given an employer's AFP cotización line, when the
  administration-commission component resolves, then it posts EXEMPT under
  46-k (substance carried under the SIP regime; stale SAP citation noted)
  (FR-223).
- **AC-015:** Given an invoice line claiming an exemption because "a ley
  especial exime a la empresa" (a CEL-kin special-law claim), when the
  Art. 174 gate runs, then the claim FAILS — the line posts TAXED (other
  laws' generic exemptions produce no effect; only Art. 45/46 letters,
  ratified instruments and REGISTERED instrument rows — W24 T3 channel
  (c) — validate) (FR-224).
- **AC-016:** Given a program-related transfer of Art. 1-enumerated
  goods by a supplier WITHOUT a DGII beneficiario declaration (no Art. 5
  resolución), when the exemption claim resolves, then the 108_
  exemption is NOT applied and the transfer posts TAXED (FR-420).
- **AC-017:** Given a declared beneficiary's program import whose
  dispatch runs through a third-party freight forwarder, when the import
  resolves, then the beneficiary's entry posts the import EXEMPT
  (impuestos y gravámenes + DAI + IVA) while the no-cascade guard BLOCKS
  the extension — the forwarder's own legs of the operation remain
  TAXED (the benefit is never extensive to any other subject of the
  import operation) (FR-420).
- **AC-018:** Given an invoice line whose exemption reason is the
  user-typed free text "ley especial exime esta operación", when the
  Art. 174 gate runs after the W24 T3 amendment, then the claim STILL
  FAILS — channel (c) validates only a registered instrument row
  (instrument id + D.O. anchor + vigencia + especialidad), never a
  user-defined generic claim; the line posts TAXED (FR-224).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 44-46/66/71/167-A/174 + Rgto. Art. 16 at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | SOQ-56 (Art. 46-f BCR-qualification instrument): **RESOLVED W18 (2026-08-22, instruments 101_-105_)** — the "instrumento necesario" the statute orders DGII+BCR to elaborate jointly EXISTS and is owned: 101_ Instructivo (DGII+BCR joint cover, base legal citing LIVA 46-f; CD-39/2021 → CD-24/2023 authorization per 102_/103_) + live qualification lists 104_/105_ (as-of 08-ago-2026). The exemption flag = BCR-list membership with current per-institution 1-year vigencia (Art. 46-f "PREVIAMENTE CALIFICADOS POR EL BANCO CENTRAL DE RESERVA" + the joint instrument — NOT an SSF banking-supervision flag); FR-219's `bcr_calificada` gains the dated-list data source (104_/105_, dated data — refresh at wave cadence); onboarding loads the current list instead of hand-keying qualifications. | no | Takumi S9 (list refresh) | **resolved** (W18; 101_-105_) |
| OQ-3 | SOQ-57 (Art. 46-k stale SAP citation): the printed anchor cites Art. 16-b of the Ley del Sistema de Ahorro para Pensiones (D.L. 927-1996), superseded by D.L. 614 (SIP, effective 2022-12-29 — R23/R24 kin). FR-223 carries the exemption substance (pension-administration commissions) under the current regime with the stale anchor recorded as printed; re-verify the SIP-equivalent commission regime before final wiring of the AFP flags. | no | Takumi S9 (payroll/pension cross-check) | open |
| OQ-4 | SOQ-58 (Art. 167-A kill-switch): the 45-h public water/alcantarillado import exemption dies at the vigencia of a future instrumento legal regulating the régimen de políticas sectoriales — the instrument is NOT in the corpus. FR-211 ships a NULL-valid_to dated row + watch; when the instrument is identified, configure its vigencia (and the explicit/categorical cessation it must define) and the D15 as-of-tax-point resolution does the rest; no retroactive re-classification. **W18 (2026-08-22) watch refresh: instrument NOT issued as of 2026-08-22** (TF DC catalog CDX 15,385 URLs + DDG exact-phrase ×3 + Bing all negative); exemption ALIVE, kill-switch config slot stands, next check at wave cadence. | no | Takumi S9 (sources registry) | open |
| OQ-5 | Reglamento de Transporte Terrestre spec gate: Art. 45-i conditions the vehicle exemption on meeting the distinguishing characteristics that regulation señala — the regulation is not in the corpus. FR-212 ships the spec gate as a config surface (spec checklist per vehicle class); obtain the current Reglamento de Transporte Terrestre vehicle specs (and the legalización/permiso-legal document feed for FR-213's 5-year register) before go-live. | no | Takumi S9 + Odoo implementation | open |
