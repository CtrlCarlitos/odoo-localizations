# SV — Special regimes — Obligations, DGA-facing reporting and sanctions

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes); W19 T1 fold-in (79_ LESIA) |
| Updated | 2026-08-22 |

## 1. Purpose

This file owns the compliance and enforcement layer of the special-regimes
wave (master cluster SR7): the ZF/DPA obligation register of the Ley de
Zonas Francas Industriales y de Comercialización (12_ Art. 28) — the
10-*días hábiles* (business days) modification notice, the electronic
inventory register of entries, exits and balances plus the *cuadro
demostrativo de descargo* (demonstrative discharge statement — the
per-import cancellation reconciliation table) online at the DGA's disposal
with its ≤20-*días hábiles* annual fallback remittance, the semestral
MINEC informe with its five data groups, the 30-day cambio/cierre
notices, the damaged/lost/destroyed goods registry, the DPA physical
segregation of suspensive vs nationalized inventories with destination
*trazabilidad* (traceability), cost records for TAN-sold goods, the
annual pending-cancellation report and the pormenorized *insumo*
(production input) vs *producto compensador* (compensating product)
register with yield/*merma* (shrinkage) tracing; the 17b_ Art. 28
DGA-facing inventory-register contract for LSI distributors (the ten
mandatory consultas/reportes, per-declaración/régimen/destinación/
contribuyente queries, SAC 6-digit classification on every item and the
Excel-transferable export) plus the Art. 29 minimum-areas note and the
Art. 44 annual consolidated operations+inventory report; the LSI
obligation catalogs (14_ Arts. 46-49: annual electronic-records
remittance, ≥500 m², 5-year manifiesto copies, custody, 8-day
irregularities notice, *marchamo* (customs seal) entry/exit duties); and
the SMM-priced sanction ladders of both laws (ZF 3/5 SMM with the
muy-grave destino-authorized breach suspension; LSI 30/40 SMM with
third-grave revocation — NEVER unified), the Art. 36-A MH regularization
clock with its customs system-access suspension, the SS-payment-breach
suspensions, the inactivity category/benefit-loss sanction consequences
and the Art. 40-A closure-with-open-DMs *defraudación de la renta de
aduanas* (customs-revenue fraud) crime pointer (LESIA Art. 22 — SOQ-32,
zero invented mechanics), all under the 13_ Art. 19 a-posteriori/
permanente control backdrop; and — W19 fold-in (79_ LESIA acquired,
SOQ-32 consumed) — the LESIA sanction taxonomy itself: the
administrativa/tributaria/penal class triad with the
independent-sanctioning-per-DM rule, the administrativa multa formulas
($50 flat / 0.5%-of-patrimonio floor 1 SMM / 3-SMM and 6-SMM tiers with
the +50% tránsito reincidencia and annual fianza), the tributaria
pricing (300%/200% of evaded duties with the 5%/3% tolerance margins and
the US$25,000 crime split), the exemption-caducidad and
3-infracciones-in-1-year suspension consequences (MINEC-imposed for
ZF/ATPA), the self-correction and 50%-attenuation modifiers, the
auxiliares suspension/cancelación ladder, and the sanctioning procedure
riding the `06` FR-128 chassis with the Art. 33/55 prescripción and
Art. 37/38 payment-enforcement clocks (consumed from `06` FR-177/178 by
id).

It does **not** cover: the beneficiary profile, benefit-state machine and
inactivity monitors it stamps (`01_regime-framework.md` — SV-SPE-FR-015..
018 by id); the ZF/DPA exemption ladders and their suspension interplay
(`02_zf-exemption-schedules.md`); the LSI auditor-dictamen family and its
data pack (`03_lsi-regime.md` — SV-SPE-FR-051..055 by id — consumed by
this file's registers, never restated); the customs clocks and DUCA
record model feeding the descargo registers (`04_customs-clocks.md` —
SV-SPE-FR-064..081; `06_customs-declarations.md` — SV-SPE-FR-103..129 +
FR-176..178 by id — the latter the tasa exemption set and the LESIA
sanction/expiry anchors on the declaration surfaces, consumed here for
pricing and never restated); the TAN/IVA internación surfaces the cost records serve
(`05_tan-iva-interface.md` by id, incl. the SS-solvency gate
SV-SPE-FR-102); FOVIAL/COTRANS (`08_fovial-cotrans.md`); the SMM tariff
values themselves (`payroll/02_minimum-wage.md` — SV-PAY-FR-022 + the
dated sidecar rows, consumed by id); the canonical retention matrix
(`commercial-legal/02_accounting-books.md` §3.7 SV-CML-FR-028 — the
customs 5y row already noted there by `06`'s SV-SPE-FR-126,
update-by-note only); and the días-hábiles engine (SV-FREP-FR-202..204
by id).

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF = **12_**
(D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998; consolidated
through reform (8) D.L. 318-2013; content title "Ley de Zonas Francas
Industriales y de Comercialización"); LSI = **14_** (D.L. Nº 431,
11-oct-2007, D.O. N° 199 T.377 25-oct-2007; 2007 print, header "Reformas:
S/R") + **17b_** (Reglamento D. Nº 131, 4-dic-2008, D.O. N° 235 T.381
12-dic-2008; this file owns its Art. 28 inventory-register contract,
Art. 29 areas note and Art. 44 annual report — the dictamen family of
the same reglamento belongs to `03_lsi-regime.md`); DGA frame = **13_**
(D. Nº 903, 14-dic-2005, D.O. Nº 8 T.370 12-ene-2006; consolidated
through reform (2) D.L. 121-2012 — cited here for the Art. 19
control-classes backdrop already anchored by `01`'s SV-SPE-FR-005);
retention kin = **74_** (D.L. Nº 529, 13-ene-1999, D.O. N° 23 T.342
3-feb-1999; consolidated through reform (4) D.L. 23-2012 — cited only as
the 5-year records floor kin of the LSI retention obligations; the
customs 5y matrix row itself is `06`'s SV-SPE-FR-126, never restated
here); sanctions = **79_** (W19; D.L. N° 551, 20-sep-2001, D.O. N° 204
T.353 29-oct-2001, vigencia 8 días → 6-nov-2001; INDICE LEGISLATIVO
print consolidated through reform (5) D.L. 588-2008, D.O. 71 T.379
18-abr-2008 — **the SOQ-32 instrument**, cited by 12_ Arts. 26/40-A +
74_ Arts. 15/17 + 14_ Art. 51; owns the LESIA class taxonomy, multa
formulas, tolerance margins, crime split, consequences, auxiliares
ladder and procedure; the prescripción/payment-enforcement clocks it
shares with the declaration surfaces live in `06` FR-177/178 by id).

**SOQ-30 verification note (rides EVERY regime LB in this file):** all
regime consolidations end 2012-2013 (12_ → D.L. 318-2013; 13_ → D.L.
121-2012; 74_ → D.L. 23-2012; 14_/17b_ → 2007/2008 prints with no reform
block; 79_ → D.L. 588-2008) — post-cutoff reforms are unverified until
official routes recover
(SOQ-22 kin); article text is cited **as printed**. Verbatim text below
is copied from the W13 evidence files (EVID-258/264/266/268/271) and,
where the evidence abbreviates, from the extraction txts
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt`,
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt`,
`sv/.extractions/17b_Reglamento_Servicios_Internacionales.pdf.txt`,
`sv/.extractions/13_Ley_Organica_Aduanas.pdf.txt` and
`sv/.extractions/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf.txt`
(W19 — EVID-359..370 of `79_100_AduanasSancciones.evidence.md`;
citable per standing
S3 ruling 25; page pointers = txt PAGE markers). D15 discipline: every
sanction multiplier, SMM unit, clock and report spec in this file is a
dated config row with instrument provenance — never a global constant;
the SMM "de mayor cuantía" unit (12_/14_ ladders, FR-141) resolves
against the payroll/02 dated
sidecar rows and snapshots on the sanction record, while the LESIA SMM
unit is a DIFFERENT statutory lookup — "el salario mínimo mensual para
el comercio y la industria en la ciudad" at the infraction date (79_
Art. 53, FR-180) — the two units are never merged.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 28 a): "COMUNICAR AL ADMINISTRADOR DE LA ZONA FRANCA, EN EL CASO DE LOS USUARIOS, O AL MINISTERIO DE ECONOMÍA, TRATÁNDOSE DE DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO, LAS MODIFICACIONES QUE HUBIERE REALIZADO EN LOS PLANES Y PROYECTOS DE SU EMPRESA, DENTRO DEL PLAZO DE DIEZ DÍAS HÁBILES CONTADOS A PARTIR DEL DÍA DE LA MODIFICACIÓN". b): "MANTENER UN REGISTRO ELECTRÓNICO DE ENTRADAS, SALIDAS Y SALDOS DE INVENTARIOS Y CUADRO DEMOSTRATIVO DE DESCARGO POR LAS IMPORTACIONES EN LÍNEA A DISPOSICIÓN DE LA DIRECCIÓN GENERAL DE ADUANAS. CUANDO EL REGISTRO NO SE LLEVE EN LÍNEA ANTE LA DIRECCIÓN GENERAL DE ADUANAS, EL BENEFICIARIO DEBERÁ REGISTRAR EN MEDIOS ELECTRÓNICOS Y MAGNÉTICOS O EN CUALQUIER OTRO MEDIO EXIGIDO POR EL MINISTERIO DE HACIENDA, A TRAVÉS DE LA DIRECCIÓN GENERAL DE ADUANAS, DE CONFORMIDAD A LA NORMATIVA APLICABLE, EL MOVIMIENTO DE INVENTARIOS, CUADRO DEMOSTRATIVO DE DESCARGO POR LAS IMPORTACIONES, MOVIMIENTO DE IMPORTACIÓN, ASÍ COMO TODA LA INFORMACIÓN RELATIVA A LAS OPERACIONES DE IMPORTACIÓN, EXPORTACIONES, TRÁNSITOS Y TRASLADOS QUE REALICE PARA EL CONTROL FISCAL RESPECTIVO, LOS CUALES DEBERÁN REMITIRSE UTILIZANDO LOS MISMOS MEDIOS, DENTRO DE LOS VEINTE DÍAS HÁBILES SIGUIENTES AL DEL VENCIMIENTO DEL EJERCICIO FISCAL A LA DIRECCIÓN GENERAL DE ADUANAS, SIN PERJUICIO QUE DEBA REMITIRLA CUANDO ÉSTA LO REQUIERA. (6) (8)" | a) Communicate to the free-zone administrador (for usuarios) or to MINEC (for DPAs) the modifications made to the company's plans and projects, within TEN días hábiles counted from the day of the modification. b) Maintain an electronic register of inventory ENTRIES, EXITS AND BALANCES and the demonstrative discharge statement (cuadro demostrativo de descargo) for imports, ONLINE at the DGA's disposal. When the register is not kept online before the DGA, the beneficiary must record in electronic and magnetic media (or any other medium required by MH through the DGA per the applicable normativa) the inventory movement, the discharge statement for imports, the import movement, and all information on import, export, transit and traslado operations for the respective fiscal control — which must be REMITTED using the same media within TWENTY días hábiles following the end of the fiscal year to the DGA, without prejudice to the duty to remit it whenever the DGA requires | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 a)/b) pp.32-33 (EVID-258; txt PAGE 32-33; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 28 c): "PROPORCIONAR AL MINISTERIO DE ECONOMÍA UN INFORME SEMESTRAL, RELACIONADO CON SUS OPERACIONES, EL CUAL DEBERÁ CONTENER: VALOR Y ORIGEN DE LAS IMPORTACIONES, VALOR Y DESTINO DE LAS EXPORTACIONES, GENERACIÓN DE EMPLEO, VENTAS AL MERCADO NACIONAL Y MONTO DE LA INVERSIÓN REALIZADA. (6)". e): "INFORMAR A LA DEPENDENCIA DEL MINISTERIO DE ECONOMÍA QUE DETERMINE EL REGLAMENTO DE ESTA LEY, Y A LA DIRECCIÓN GENERAL DE ADUANAS, CON 30 DÍAS DE ANTICIPACIÓN, EL CAMBIO DE DOMICILIO O CIERRE DE OPERACIONES. (6)" | c) Provide MINEC a SEMESTRAL report on operations, which must contain: VALUE AND ORIGIN of imports, VALUE AND DESTINATION of exports, employment generation, sales to the national market and the amount of investment made. e) Inform the MINEC dependency determined by the law's reglamento, and the DGA, 30 DAYS IN ADVANCE, of any change of domicile or closure of operations | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 c)/e) p.33 (EVID-258; txt PAGE 33; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 28 j): "RESPONDER ANTE EL FISCO POR EL PAGO DE LAS OBLIGACIONES TRIBUTARIAS Y ADUANERAS RELACIONADAS CON LAS MERCANCÍAS PERDIDAS O DE AQUELLAS QUE SE HUBIESEN DESTINADO INDEBIDAMENTE O POR LA FALTA DE CONTROLES AL TERRITORIO ADUANERO NACIONAL, INCLUYENDO LAS DAÑADAS O LAS DESTRUIDAS QUE HAYAN SIDO IGUALMENTE DESTINADAS AL MERCADO NACIONAL, SALVO QUE EXISTA CAUSA FORTUITA O FUERZA MAYOR DEBIDAMENTE COMPROBADAS POR EL BENEFICIARIO ANTE LA DIRECCIÓN GENERAL DE ADUANAS. (6)". l): "LLEVAR UN REGISTRO DE LAS MERCANCÍAS DAÑADAS, PERDIDAS, DESTRUIDAS Y DEMÁS IRREGULARIDADES OCURRIDAS DURANTE EL TIEMPO QUE PERMANEZCAN EN EL DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO Y PONERLO A DISPOSICIÓN DE LA DIRECCIÓN GENERAL DE ADUANAS, CUANDO ÉSTA LO REQUIERA. (6)" | j) Answer to the fisc for payment of the tax and customs obligations related to LOST goods, goods MISDIRECTED, or failures of controls toward the national customs territory — including DAMAGED or DESTROYED goods likewise destined to the national market — save fortuitous cause or force majeure duly proven by the beneficiary before the DGA. l) Keep a register of damaged, lost, destroyed goods and other irregularities occurring while they remain in the DPA, and place it at the DGA's disposal whenever it requires | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 j)/l) p.34 (EVID-258; txt PAGE 34; SOQ-30 print) |
| LB-004 | Ley de Zonas Francas, Art. 28 n): "EN EL CASO DE LOS DPA, MANTENER SUS INSTALACIONES TOTAL Y COMPLETAMENTE DELIMITADAS E INDEPENDIENTES DE CUALQUIER OTRA EMPRESA; EN CASO DE COMPARTIR ESPACIOS FÍSICOS CON OTRAS, ÉSTAS DEBERÁN CONTAR CON ÁREAS DE ALMACENAJE Y OPERACIÓN SEPARADAS Y PERSONAL INDEPENDIENTE, DE FORMA TAL QUE NO EXISTA POSIBILIDAD DE CONFUSIÓN DE MATERIAS PRIMAS, PROCESOS PRODUCTIVOS, NI DE TERRITORIO ADUANERO NACIONAL Y EXTRA ADUANAL… DEBERÁN MANTENER EN LA BODEGA, DEBIDAMENTE SEPARADAS, LAS MERCANCÍAS DEL RÉGIMEN SUSPENSIVO, DE AQUÉLLAS NACIONALIZADAS CUANDO DICHAS MERCANCÍAS SEAN COMBINADAS O MEZCLADAS EN EL PROCESO PRODUCTIVO Y LLEVAR UN CONTROL DE INVENTARIO QUE PERMITA IDENTIFICARLAS EN EL PRODUCTO COMPENSADO, CON LA FINALIDAD DE ESTABLECER LA TRAZABILIDAD DE SU DESTINO. (6) (8)" | For DPAs: keep installations totally and completely delimited and independent of any other company; where physical spaces are shared, the others must have separate storage and operation areas and independent personnel so that NO confusion of raw materials, production processes, or national vs extra-aduanal customs territory is possible. The warehouse must keep goods of the SUSPENSIVE REGIME duly SEPARATED from NATIONALIZED goods when such goods are combined or mixed in the production process, and carry an inventory control that permits identifying them in the compensated product, with the purpose of establishing the TRACEABILITY of their destination | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 n) p.34 (EVID-258; txt PAGE 34; SOQ-30 print) |
| LB-005 | Ley de Zonas Francas, Art. 28 p): "LLEVAR REGISTROS DE COSTOS POR LAS MERCANCÍAS QUE VENDAN AL MERCADO NACIONAL, CUANDO ESTÉ DEBIDAMENTE AUTORIZADO PARA TAL EFECTO Y ADEMÁS, CUMPLIENDO CON EL PAGO DE LOS TRIBUTOS CORRESPONDIENTES. (8)". q): "EN EL CASO DE LOS USUARIOS DE ZONA FRANCA, INFORMAR AL SERVICIO ADUANERO, DENTRO DE LOS VEINTE DÍAS HÁBILES SIGUIENTES AL VENCIMIENTO DEL EJERCICIO FISCAL, SOBRE LOS BIENES PENDIENTES DE CANCELAR, PUDIENDO INCLUIR ESTA INFORMACIÓN EN EL REGISTRO AL QUE SE REFIERE EL LITERAL b) DEL PRESENTE ARTÍCULO. (8)". r): "CUMPLIR CON EL DESTINO AUTORIZADO DE LOS BIENES. (8)". s): "LLEVAR UN REGISTRO PORMENORIZADO DE LOS INSUMOS UTILIZADOS EN EL PROCESO PRODUCTIVO, EN RELACIÓN A LOS PRODUCTOS COMPENSADORES Y EXHIBIR DICHO REGISTRO, A REQUERIMIENTO DE LA DIRECCIÓN GENERAL DE ADUANAS, EN EL EJERCICIO DE SUS FACULTADES DE FISCALIZACIÓN, EN RELACIÓN CON LAS OPERACIONES OBJETO DE INVESTIGACIÓN. (8)" | p) Keep COST RECORDS for the goods sold to the national market, when duly authorized for that purpose and, additionally, in compliance with payment of the corresponding tributes. q) For ZF usuarios: inform the customs service, within TWENTY días hábiles following the close of the fiscal year, of the goods PENDING CANCELLATION — this information may be included in the register of literal b). r) Comply with the AUTHORIZED DESTINATION of the goods. s) Keep a PORMENORIZED (detailed) register of the production inputs used in the productive process in relation to the compensating products, and exhibit that register at the DGA's requirement, in the exercise of its fiscalization powers, in relation with the operations under investigation | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 p)/q)/r)/s) pp.34-35 (EVID-258; txt PAGE 34-35; SOQ-30 print) |
| LB-006 | Ley de Zonas Francas, Art. 28 final: "SE CONSIDERAN INFRACCIONES A LA PRESENTE LEY, LAS SIGUIENTES: 1. INFRACCIONES LEVES: EL INCUMPLIMIENTO A LO ESTABLECIDO EN LOS LITERALES a), c), f), g), h), i) Y q); DEL PRESENTE ARTÍCULO. 2. INFRACCIONES GRAVES: EL INCUMPLIMIENTO A LO ESTABLECIDO EN LOS LITERALES b), d), e), j), k), l), m), n), o), p) Y s) DE ESTE ARTÍCULO. 3. INFRACCIONES MUY GRAVES: EL INCUMPLIMIENTO AL LITERAL r) DEL PRESENTE ARTÍCULO. (6) (8)" | The following are considered infringements of this law: 1. MINOR infringements (leves): noncompliance with literals a), c), f), g), h), i) and q) of this article. 2. SERIOUS infringements (graves): noncompliance with literals b), d), e), j), k), l), m), n), o), p) and s). 3. VERY SERIOUS infringements (muy graves): noncompliance with literal r) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 28 final pp.34-35 (EVID-258; txt PAGE 34-35; SOQ-30 print) |
| LB-007 | Ley de Zonas Francas, Art. 36: "LAS INFRACCIONES MENCIONADAS EN LOS ARTÍCULOS ANTERIORES SERÁN SANCIONADAS ADMINISTRATIVAMENTE POR EL MINISTERIO DE ECONOMÍA, DE LA MANERA SIGUIENTE: a) LA INFRACCIÓN LEVE, SE SANCIONARÁ CON PREVENCIÓN ESCRITA AL INFRACTOR EN LA QUE DEBERÁ ESTABLECERSE PLAZO PARA QUE CUMPLA CON LA OBLIGACIÓN DE QUE SE TRATE. LA REINCIDENCIA EN ALGUNA INFRACCIÓN LEVE SERÁ SANCIONADA CON MULTA EQUIVALENTE A TRES SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA; b) LA INFRACCIÓN GRAVE, SE SANCIONARÁ CON MULTA EQUIVALENTE DE CINCO SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA; c) LA INFRACCIÓN MUY GRAVE SE SANCIONARÁ CON SUSPENSIÓN TEMPORAL POR UN MÁXIMO DE 3 MESES. LA REINCIDENCIA EN UNA INFRACCIÓN MUY GRAVE, DARÁ LUGAR A LA SUSPENSIÓN DEFINITIVA DE LOS BENEFICIOS. (2) (6)". Art. 37: "LAS RESOLUCIONES FIRMES Y DEFINITIVAS QUE DE CONFORMIDAD A ESTE CAPÍTULO IMPONGAN SANCIÓN DE MULTA, DEBERÁN HACERSE EFECTIVAS DENTRO DE LOS TREINTA DÍAS SIGUIENTES DE HABERSE NOTIFICADO LA SANCIÓN. EL PAGO DE LA MULTA SE HARÁ EFECTIVO EN LA DIRECCIÓN GENERAL DE TESORERÍA O EN LAS INSTITUCIONES AUTORIZADAS POR ÉSTA. (6)" | Art. 36 — infringements are sanctioned administratively by MINEC as follows: a) a minor infringement is sanctioned with a WRITTEN PREVENCIÓN (warning) to the infractor establishing a term to comply with the obligation in question; REINCIDENCIA (recidivism) in a minor infringement is sanctioned with a FINE EQUIVALENT TO THREE HIGHEST-AMOUNT MONTHLY MINIMUM WAGES (salarios mínimos mensuales de mayor cuantía); b) a serious infringement is sanctioned with a fine of FIVE such wages; c) a very serious infringement is sanctioned with TEMPORARY SUSPENSION for a MAXIMUM OF 3 MONTHS; recidivism in a very serious infringement gives rise to the DEFINITIVE SUSPENSION of the benefits. Art. 37 — firm and definitive resolutions imposing a fine must be made effective within THIRTY DAYS following notification of the sanction; payment is made effective at the Dirección General de Tesorería or institutions it authorizes | `sv/sources/12_Ley_Zonas_Francas.pdf` | Arts. 36/37 p.38 (EVID-258; txt PAGE 38; SOQ-30 print) |
| LB-008 | Ley de Zonas Francas, Art. 36-A: "EN EL CASO QUE EL MINISTERIO DE HACIENDA, A TRAVÉS DE LAS DIRECCIONES GENERALES DE ADUANA E IMPUESTOS INTERNOS, CONSTATE INFRACCIONES GRAVES, SEGÚN LO ESTABLECIDO EN EL ARTÍCULO 28 DE LA PRESENTE LEY O VENTAS EFECTUADAS AL MERCADO LOCAL, SIN EL CORRESPONDIENTE PAGO DE DERECHOS E IMPUESTOS, NOTIFICARÁ DICHA SITUACIÓN AL MINISTERIO DE ECONOMÍA. ASIMISMO, LA DIRECCIÓN GENERAL DE ADUANAS OTORGARÁ AL USUARIO DE LA ZONA FRANCA O DPA UN PLAZO DE 30 DÍAS CALENDARIO PARA REGULARIZAR LA SITUACIÓN DETECTADA, ESTE PLAZO SE CONTARÁ A PARTIR DEL DÍA SIGUIENTE DE LA NOTIFICACIÓN RESPECTIVA, MISMA EN LA QUE DEBERÁ CONSTAR QUE DE NO SOLVENTARSE DICHA SITUACIÓN EN EL PLAZO ANTES SEÑALADO, LA DIRECCIÓN GENERAL DE ADUANAS PROCEDERÁ COMO MEDIDA PRECAUTORIA A LA SUSPENSIÓN DE LOS ACCESOS A SUS SISTEMAS INFORMÁTICOS PARA OPERACIONES ADUANERAS. EL USUARIO DE LA ZONA FRANCA O DPA SERÁ REHABILITADO EN SU ACCESO A LOS SISTEMAS INFORMÁTICOS HASTA QUE REGULARICE LA SITUACIÓN DETECTADA. (8)" | When MH, through the DGA and DGII, finds SERIOUS infringements per Art. 28 of this law, or sales made to the local market WITHOUT the corresponding payment of duties and taxes, it notifies that situation to MINEC. The DGA grants the ZF usuario or DPA a term of 30 CALENDAR DAYS to regularize the detected situation, counted from the day after the respective notification — which must state that, absent cure within that term, the DGA will proceed AS A PRECAUTIONARY MEASURE to SUSPEND ITS ACCESSES TO THE COMPUTER SYSTEMS for customs operations. The ZF usuario or DPA is REHABILITATED in its access to the computer systems ONLY ONCE it regularizes the detected situation | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 36-A p.38 (EVID-258; txt PAGE 38; SOQ-30 print) |
| LB-009 | Ley de Zonas Francas, Art. 31 (incisos 2-3): "CUANDO SE INFRINGIERE LA OBLIGACIÓN DE PAGAR LAS COTIZACIONES PATRONALES DE PENSIONES O DE SEGURIDAD SOCIAL DE LOS TRABAJADORES, ASÍ COMO LA DE TRASLADAR LAS SUMAS DESCONTADAS A ÉSTOS POR TALES CONCEPTOS, LAS RESPECTIVAS RESOLUCIONES FIRMES Y DEFINITIVAS EMITIDAS POR LOS FUNCIONARIOS DEL MINISTERIO DE TRABAJO Y PREVISIÓN SOCIAL O LA AUTORIDAD CORRESPONDIENTE DEL INSTITUTO SALVADOREÑO DEL SEGURO SOCIAL, O DE LA SUPERINTENDENCIA DE PENSIONES, SEGÚN EL CASO, DEBERÁN SER NOTIFICADAS AL MINISTRO DE ECONOMÍA, A FIN QUE ÉSTE DECIDA SI PROCEDE LA SUSPENSIÓN TEMPORAL DE LOS BENEFICIOS POR UN PERÍODO DE TRES MESES, Y, EN CASO DE REINCIDENCIA, EL MINISTRO DECRETARÁ LA SUSPENSIÓN DEFINITIVA DE LOS BENEFICIOS. (2) (6)" | When the obligation to pay the EMPLOYER pension or social-security contributions of the workers, or to TRANSFER THE SUMS WITHHELD from them for such concepts, is infringed, the respective firm and definitive resolutions issued by MTPSS officials or the corresponding ISSS or Superintendencia de Pensiones authority must be notified to the Minister of Economy, so that the latter decides whether a TEMPORARY SUSPENSION OF THE BENEFITS FOR A PERIOD OF THREE MONTHS proceeds — and, in case of REINCIDENCIA, the Minister decrees the DEFINITIVE SUSPENSION of the benefits | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 31 incs. 2-3 p.37 (EVID-258; txt PAGE 37; SOQ-30 print) |
| LB-010 | Ley de Zonas Francas, Art. 37-A: "EN LOS CASOS QUE LAS DIRECCIONES GENERALES DE ADUANAS E IMPUESTOS INTERNOS EN USO DE SUS FACULTADES DE FISCALIZACIÓN DETERMINEN LA EXISTENCIA DE INFRACCIONES TRIBUTARIAS REITERADAS A LA LEGISLACIÓN ADUANERA O HAYAN TENIDO CONOCIMIENTO DE LA EXISTENCIA DE SENTENCIA PENAL FIRME POR VIOLACIÓN A DICHA LEGISLACIÓN, LOS MINISTERIOS DE HACIENDA Y DE ECONOMÍA PODRÁN EXIGIR AL BENEFICIARIO RENDIR FIANZA PARA RESPONDER POR EL CUMPLIMIENTO DE LAS OBLIGACIONES DERIVADAS DE LOS BENEFICIOS RECIBIDOS. (6)" | Where the DGA and DGII, in the exercise of their fiscalization powers, determine the existence of REPEATED tax infringements of customs legislation, or learn of a firm criminal sentence for violating said legislation, MH and MINEC MAY require the beneficiary to render a BOND (fianza) answering for compliance with the obligations derived from the benefits received | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 37-A pp.38-39 (EVID-258; txt PAGE 38-39; SOQ-30 print) |
| LB-011 | Ley de Zonas Francas, Art. 39 (operative sanction fragment): "LA PERSONA NATURAL O JURÍDICA BENEFICIADA POR ESTA LEY QUE DEJARE DE OPERAR LA EMPRESA DE LA CUAL FUERE TITULAR, POR CAUSAS IMPUTABLES A ÉSTE, DURANTE UN PERÍODO DE DOCE MESES CONTINUOS, PERDERÁ LA CATEGORÍA DE USUARIO DE ZONA FRANCA O DE DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO, PREVIA AUDIENCIA AL INTERESADO POR EL TÉRMINO DE CINCO DÍAS HÁBILES… LA RESOLUCIÓN FINAL DEBERÁ PRONUNCIARSE DENTRO DE LOS DIEZ DÍAS POSTERIORES A LA FINALIZACIÓN DEL TÉRMINO ANTES MENCIONADO… LAS OPERACIONES… ESTARÁN REFERIDAS A LAS PROPIAS DE LA ACTIVIDAD INCENTIVADA, PARTICULARMENTE IMPORTACIONES Y EXPORTACIONES BAJO EL RÉGIMEN DE ESTA LEY. LA DIRECCIÓN GENERAL DE ADUANAS DARÁ SEGUIMIENTO A TRAVÉS DE SU SISTEMA INFORMÁTICO, DEBIENDO DAR DE BAJA EN EL MISMO, A AQUELLAS EMPRESAS QUE INCURRIEREN EN TAL SITUACIÓN… (6)" | A beneficiary that ceases operating the enterprise of which it is holder, for causes imputable to it, for a continuous TWELVE-MONTH period, LOSES its ZF-usuario or DPA category, after a five-días-hábiles hearing; final resolution within the ten days following the end of that term. Operations means those of the incentivated activity, particularly IMPORTS AND EXPORTS UNDER THE REGIME; the DGA tracks through its computer system and must deregister (dar de baja) the affected companies | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 39 p.39 (EVID-258; txt PAGE 39; SOQ-30 print; full text quoted at 01 LB-010) |
| LB-012 | Ley de Zonas Francas, Art. 40-A: "CUANDO UN BENEFICIARIO DE ESTA LEY NOTIFIQUE EL CIERRE DEFINITIVO DE OPERACIONES A LA DIRECCIÓN GENERAL DE ADUANAS, DEBERÁ PRESENTAR LA INFORMACIÓN Y DOCUMENTACIÓN QUE DEMUESTRE LAS CANCELACIONES DE LAS DECLARACIONES DE MERCANCÍAS POR IMPORTACIONES BAJO EL RÉGIMEN DE ZONA FRANCA O ADMISIÓN TEMPORAL PARA PERFECCIONAMIENTO ACTIVO Y EL PAGO DE LOS DERECHOS E IMPUESTOS PARA LAS MERCANCÍAS AMPARADAS EN AQUELLAS QUE NO HAYA DEMOSTRADO SU CANCELACIÓN O DESCARGO. EL CIERRE O ABANDONO SIN NOTIFICAR A LA DIRECCIÓN GENERAL DE ADUANAS Y SIN EFECTUAR LAS CANCELACIONES QUE EL RÉGIMEN ADUANERO LE IMPONE, CONSTITUYE EL DELITO DE DEFRAUDACIÓN DE LA RENTA DE ADUANAS, SANCIONADO CONFORME AL ARTÍCULO 22 DE LA LEY ESPECIAL PARA SANCIONAR INFRACCIONES ADUANERAS, SIN PERJUICIO A LA RESPONSABILIDAD CIVIL Y PENAL A QUE DIERE LUGAR." | When a beneficiary notifies the DEFINITIVE CLOSURE of operations to the DGA, it must present the information and documentation demonstrating the CANCELLATIONS of the goods declarations for imports under the ZF or active-perfecting temporary-admission regime, and the PAYMENT of duties and taxes for the goods covered by those declarations whose cancellation or discharge has not been demonstrated. CLOSURE OR ABANDONMENT WITHOUT NOTIFYING the DGA and WITHOUT EFFECTING the cancellations the customs regime imposes constitutes the CRIME OF DEFRAUDACIÓN OF THE CUSTOMS REVENUE, sanctioned per Art. 22 of the Ley Especial para Sancionar Infracciones Aduaneras (LESIA), without prejudice to the civil and criminal liability that may arise | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 40-A p.40 (EVID-258; txt PAGE 40; SOQ-30 print; LESIA acquired as 79_ — SOQ-32 consumed W19; Art. 22 anchored at LB-025) |
| LB-013 | Ley de Servicios Internacionales, Art. 46: "Son obligaciones para los usuarios directos de parques de servicios y centros de servicios, las siguientes: a) Comunicar al administrador del parque de servicios y a la dependencia del Ministerio de Economía que determine el Reglamento de esta Ley, o únicamente a esta última en el caso de los centros de servicios, los planes, proyectos y las modificaciones de su empresa y sus operaciones, dentro del plazo de diez días hábiles contados a partir del día de la modificación. b) Mantener en un mínimo de 500 metros cuadrados la extensión del inmueble en que realiza la actividad económica, o el mínimo autorizado de conformidad con el artículo 22, literal a) de esta Ley. c) Conservar para el caso de lo establecido en el artículo 22 de la presente Ley, las copias de los Manifiestos de Carga Consolidada, de las operaciones en las que intervenga, por un plazo de 5 años. d) Disponer de los medios que aseguren la efectiva custodia y conservación de las mercancías… e) Informar al servicio aduanero sobre la pérdida, destrucción, daño o abandono; así como de las demás irregularidades respecto de las mercancías, en el plazo de ocho días contados a partir del respectivo acontecimiento. f) Destinar temporalmente espacios para el examen previo o la verificación inmediata de las mercancías depositadas; así como para el almacenamiento de las mercancías caídas en abandono o retenidas… El incumplimiento a lo establecido en este artículo será considerado Infracciones Menos Graves." | Obligations of usuarios directos of parques and centros de servicios: a) communicate plans/projects and modifications to the parque administrador and the MINEC dependency (the latter alone for centros) within TEN días hábiles from the day of the modification; b) keep the property where the economic activity is performed at a MINIMUM OF 500 SQUARE METERS, or the authorized minimum per Art. 22 a); c) keep copies of consolidated-cargo manifests of operations in which it intervenes for FIVE YEARS (per Art. 22); d) have means assuring effective custody and conservation of the goods; e) inform the customs service of loss, destruction, damage or abandono (abandonment) and other irregularities regarding the goods within EIGHT DAYS of the respective event; f) temporarily dedicate spaces for prior examination or immediate verification of deposited goods, and for storage of goods fallen in abandono or retained. Noncompliance = MENOS GRAVES (less-serious) infringements | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 46 a)-f) pp.21-22 (EVID-264; txt PAGE 21-22; SOQ-30 print) |
| LB-014 | Ley de Servicios Internacionales, Art. 47: "a) Registrar en medios electrónicos y magnéticos o en cualquier otro medio exigido por los Ministerios de Economía y de Hacienda, a través de la Dirección General de Aduanas… toda la información relativa a las operaciones que realice, inventarios y sus movimientos, y cualquier otra información que se considere necesaria para el control fiscal y administrativo respectivo. Dichos registros deberán remitirse anualmente a dichas Instituciones, o cuando éstas lo soliciten, y estarán sujetos además, a la fiscalización o inspección de los respectivos Ministerios… adicionalmente en el caso de los registros informáticos deberá permitir la auditoría de sistemas de los mismos. b) Informar a los Ministerios de Economía y de Hacienda, a través de la Dirección de Aduanas, con 30 días de anticipación, el cambio de domicilio o cierre de operaciones, señalando… si se trata de un cierre temporal o definitivo y las razones y justificaciones respectivas. c) Permitir el ingreso a las instalaciones… a delegados… d) Establecer controles y registros contables de sus operaciones, de conformidad con la Ley. e) Establecer el inventario físico de las mercancías bajo su custodia y responsabilidad, para el caso de los distribuidores y operadores logísticos, quienes deberán llevar su control en su sistema informático especializado. f) Contar con los servicios de una firma independiente de auditoría… dictámenes semestrales… g) No desarrollar actividades fuera de las instalaciones del parque o centro de servicios autorizado. h) Cumplir con las leyes… laborales y de seguridad social… i) Pagar indemnización, aguinaldo y vacación proporcional… j) En caso extraordinario de cierre total… los activos… servirán preferentemente para cancelar el pasivo… laboral… k) Integrar el personal de su empresa con un noventa por ciento de salvadoreños, por lo menos… El incumplimiento… será considerado como Infracciones Graves." | Obligations of usuarios directos: a) register in electronic and magnetic media (or any medium required by MINEC and MH through the DGA) all information on operations, inventories and their movements, and any other information necessary for fiscal and administrative control; said records are REMITTED ANNUALLY to those institutions, or when they request it, and are subject to fiscalization/inspection — computer records must additionally permit SYSTEMS AUDIT; b) inform MINEC and MH through the DGA, 30 days in advance, of change of domicile or closure of operations, stating whether the closure is TEMPORARY OR DEFINITIVE with reasons; c) allow delegado ingress and provide truthful information; d) establish accounting controls and records per the Law; e) establish the PHYSICAL INVENTORY of goods under custody — distributors and logistics operators carrying the control in their specialized computer system; f) engage a DGII-authorized independent audit firm emitting SEMESTRAL dictámenes (owned by `03` by id); g) NOT develop activities outside the authorized parque/centro; h) comply with labor and social-security laws; i) pay indemnización, aguinaldo and proportional vacation on closures; j) extraordinary total closure without justification: assets serve PREFERENTLY to pay labor liabilities; k) ≥90% Salvadoran staffing (owned by `03` by id). Noncompliance = GRAVES (serious) infringements | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 47 a)-k) pp.22-23 (EVID-264; txt PAGE 22-23; SOQ-30 print) |
| LB-015 | Ley de Servicios Internacionales, Art. 48 (fragments): "Son obligaciones de los administradores de parques de servicios… d) Conservar y mantener a disposición del Servicio Aduanero, los documentos y la información relativa a la relación contractual con los usuarios directos, por un plazo de cinco años… g) Informar al servicio aduanero de las mercancías dañadas, perdidas, destruidas, caídas en abandono y demás irregularidades… El incumplimiento… será considerado Infracciones Menos Graves." Art. 49: "Los administradores de parques de servicios están obligados a permitir la entrada al parque de servicios, de los medios de transporte, previa comprobación de las condiciones y estados de los marchamos y demás medidas de seguridad, cuando no haya presencia aduanera, lo cual no incluirá la ruptura del marchamo; y comunicar oportunamente al Servicio Aduanero de su ingreso, así como cualquier irregularidad encontrada… asimismo permitir la salida de las mercancías únicamente con la autorización de la autoridad aduanera, a las horas y días habilitados para tal efecto. El incumplimiento de las anteriores obligaciones constituirá infracción grave, y la reincidencia será considerada infracción muy grave." | Art. 48 — parque-administrador obligations (among others): d) conserve and keep at the customs service's disposal the documents and information on the contractual relation with usuarios directos for FIVE YEARS; g) inform the customs service of damaged, lost, destroyed and abandoned goods and other irregularities occurring in their parque; noncompliance = menos graves. Art. 49 — administradores must allow transport vehicles into the parque after verifying the condition and state of the MARCHAMOS (customs seals) and other security measures when there is no customs presence (NOT including breaking the seal), timely communicate their entry and any irregularity found, and allow the EXIT of goods ONLY with customs-authority authorization, at the enabled hours and days; noncompliance = GRAVE infringement, and REINCIDENCIA = VERY SERIOUS (muy grave) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Arts. 48 d)/g) + 49 pp.23-24 (EVID-264; txt PAGE 23-24; SOQ-30 print) |
| LB-016 | Ley de Servicios Internacionales, Art. 50 (incisos 2-3): "Cuando se infringiere la obligación de pagar las cotizaciones patronales de pensiones o de seguridad social de los trabajadores, así como la de trasladar las sumas descontadas a éstos por tales conceptos, las respectivas resoluciones emitidas por los funcionarios del Ministerio de Trabajo y Previsión Social o la autoridad correspondiente del Instituto Salvadoreño del Seguro Social, o de la Superintendencia de Pensiones, según el caso, deberán ser notificadas al Ministro de Economía, a fin que éste decida si procede la suspensión temporal de los beneficios por un período de tres meses, y, en caso de reincidencia atribuible al beneficiario, el Ministro decretará la revocatoria de los beneficios." Art. 51: "Cuando existan infracciones reiteradas que tuvieren como consecuencia la omisión del pago de derechos o impuestos directamente o indirectamente, o los montos dejados de pagar correspondan a los establecidos para la configuración de delito en la legislación correspondiente, la autoridad aduanera o tributaria… enviará la resolución definitiva y firme correspondiente al Ministro de Economía, a fin que éste decida la procedencia de la suspensión temporal de los beneficios por tres meses, y en caso de reincidencia atribuible al beneficiario la revocatoria, de los mismos." | Art. 50 — when the employer pension/social-security contribution or transfer obligation is infringed, the respective resolutions are notified to the Minister of Economy, who decides a THREE-MONTH TEMPORARY SUSPENSION of benefits and — on recidivism ATTRIBUTABLE TO THE BENEFICIARY — decrees the REVOCATION of the benefits (the same article's fianza and AML-conviction twins are owned by `03` by id). Art. 51 — where REPEATED infringements cause omission of payment of duties or taxes directly or indirectly, or the unpaid amounts correspond to crime-configuration thresholds, the customs or tax authority sends the firm definitive resolution to the Minister of Economy, who decides a three-month temporary suspension and — on attributable recidivism — revocation | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Arts. 50 incs. 2-3/51 pp.24-25 (EVID-264; txt PAGE 24-25; SOQ-30 print) |
| LB-017 | Ley de Servicios Internacionales, Art. 52: "Las infracciones establecidas en la presente Ley, serán sancionadas administrativamente por el Ministerio, de la manera siguiente: a) La Infracción Menos Grave se sancionará con prevención escrita al Infractor, en la que deberá establecerse plazo para que cumpla con la obligación de que se trate. La reincidencia en alguna infracción menos grave será sancionada con multa equivalente a tres salarios mínimos mensuales de mayor cuantía. b) La Infracción Grave se sancionará con multa equivalente a treinta salarios mínimos mensuales de mayor cuantía. En caso de reincidencia, se impondrá multa equivalente a cuarenta salarios mínimos mensuales de mayor cuantía. Al presentarse una tercera infracción grave se decretará la revocatoria de los beneficios. c) La Infracción Muy Grave se sancionará con suspensión temporal de los beneficios, por el término de tres meses. La reincidencia en este tipo de infracciones dará lugar a la revocatoria de los beneficios." Art. 62 (operative fragment): "SI ALGUNA PERSONA… ACOGIDA A LOS BENEFICIOS DE ESTA LEY DEJARA DE OPERAR, DURANTE UN PERÍODO DE TRES MESES CONTINUOS, DEBERÁN REVOCARSE LOS BENEFICIOS OTORGADOS…, SALVO FUERZA MAYOR O CASO FORTUITO… SI LA RESOLUCIÓN DETERMINA LA CANCELACIÓN DE LOS BENEFICIOS, LA DIRECCIÓN GENERAL DE ADUANAS PROCEDERÁ A INHABILITAR LOS ACCESOS AL SISTEMA INFORMÁTICO." | Art. 52 — a) a less-serious infringement: written prevención with a compliance term; recidivism, a fine of THREE highest-amount monthly minimum wages; b) serious: a fine of THIRTY such wages, FORTY on recidivism — and upon a THIRD serious infringement, REVOCATION of the benefits is decreed; c) very serious: TEMPORARY suspension of benefits for THREE MONTHS; recidivism gives rise to revocation. Art. 62 — a beneficiary ceasing to operate for THREE CONTINUOUS MONTHS has its benefits revoked (save force majeure or fortuitous case); if the resolution cancels the benefits, the DGA DISABLES its computer-system accesses (full text at 01 LB-021) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 52 p.25 + Art. 62 p.26 (EVID-264; txt PAGE 25-26; SOQ-30 print) |
| LB-018 | Reglamento de la Ley de Servicios Internacionales (17b_), Art. 28: "Es obligación del beneficiario mantener un registro electrónico de inventarios actualizado con acceso en línea a disposición de la DGA para asegurar el control de las operaciones, referido a depósito temporal, admisión temporal, mercancías en estado de abandono, retenidas administrativamente, entre otras, debiendo contener como mínimo, las siguientes consultas y reportes, según corresponda: a) Registro diario de ingresos y egresos de mercancías, independientemente del tipo de operación; b) Saldo de inventario; c) Reporte de declaraciones de mercancías con sus respectivas cancelaciones o destinaciones; d) Reporte de declaraciones que reflejen saldos; e) Reporte de mercancías en abandono, con detalle de las declaraciones afectadas; f) Reporte de mercancías sometidas al depósito temporal; g) Reporte de mercancías bajo el régimen de admisión temporal; h) Reporte de mercancías retenidas administrativamente, entendiéndose mercancías decomisadas por ser de naturaleza prohibidas o restringidas; i) Reporte de las mercancías en acopio para la exportación, en caso de estar autorizada la operación; y, j) Reporte de las mercancías de almacenaje simple por contribuyente, en caso de estar autorizada la operación. Los reportes deberán permitir, entre otros, efectuar consultas por Declaración de Mercancías, Régimen, destinación, por contribuyente. Las mercancías deben estar registradas por su nombre comercial, código e identificación con la partida arancelaria a nivel de seis dígitos; asimismo, el número de documento de ingreso al usuario directo del Parque de Servicios. La información de los reportes deberá estar elaborada en sistemas compatibles que permitan ser transferidos electrónicamente a hojas electrónicas de uso común, por ejemplo, Excel. La DGA a través de disposiciones administrativas de carácter general, podrá establecer otras consultas y reportes, así como la estructura de los mismos…" | It is the beneficiary's obligation to keep an UPDATED electronic inventory register with ONLINE access at the DGA's disposal to assure control of operations — covering temporary deposit, temporary admission, goods in state of abandono, administratively retained goods, among others — containing AT MINIMUM the following consultas (queries) and reportes (reports), as applicable: a) DAILY register of goods ingresos (entries) and egresos (exits), regardless of operation type; b) inventory saldo (balance); c) report of goods declarations with their respective cancellations or destinaciones (destinations); d) report of declarations reflecting balances; e) report of goods in abandono, WITH DETAIL of the affected declarations; f) report of goods under temporary deposit; g) report of goods under the temporary-admission regime; h) report of administratively retained goods — meaning goods seized (decomisadas) as prohibited or restricted in nature; i) report of goods in acopio (collection/consolidation) for export, when the operation is authorized; j) report of simple-storage (almacenaje simple) goods PER CONTRIBUTUYENTE (taxpayer), when authorized. The reports must permit, among others, queries BY goods declaration, BY regime, BY destinación and BY contribuyente. Goods must be registered by their commercial name, code and identification with the tariff heading AT THE SIX-DIGIT LEVEL, plus the entry-document number to the parque's usuario directo. Report information must be produced in compatible systems permitting ELECTRONIC TRANSFER to common electronic spreadsheets, e.g., Excel. The DGA, through disposiciones administrativas de carácter general (DACG), may establish other queries and reports and their structure | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Art. 28 pp.10-11 (EVID-266; txt PAGE 10-11; SOQ-30 print) |
| LB-019 | Reglamento de la Ley de Servicios Internacionales (17b_), Art. 29: "Los beneficiados deberán contar con áreas delimitadas para las operaciones que efectuarán, con la finalidad de mantener un control efectivo de las mercancías y que el manejo del inventario sea expedito. Entre las áreas mínimas… están: a) Área de carga y descarga de mercancías; b) Área de depósito temporal; c) Área de admisión temporal; d) Área de expedición; e) Área especial (verificación previa, inmediata y de abandono); f) Área de mercancías retenidas administrativamente…; g) Área de consolidación de exportaciones, en caso de estar autorizada la operación; y, h) Área de almacenaje simple, en caso de estar autorizada la operación. El área especial… será autorizada por la DGA… Los beneficiarios podrán desistir de brindar algunos de los servicios… comunicando expresamente a la DGA… la cual emitirá la Resolución que corresponda." | Beneficiaries must have DELIMITED AREAS for their operations, to keep effective control of the goods and expeditious inventory handling. Minimum areas include: a) loading/unloading area; b) temporary-deposit area; c) temporary-admission area; d) dispatch (expedición) area; e) special area (prior and immediate verification and abandono); f) administratively-retained goods area; g) export-consolidation area (when authorized); h) simple-storage area (when authorized). The special area is authorized by the DGA; beneficiaries may desist from providing some services by expressly communicating to the DGA, which issues the corresponding resolution (PHYSICAL layout duty — informational for the system) | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Art. 29 pp.11-12 (EVID-266; txt PAGE 11-12; SOQ-30 print) |
| LB-020 | Reglamento de la Ley de Servicios Internacionales (17b_), Art. 44: "Para la aplicación de las obligaciones establecidas en el literal a) del Art. 47 de la Ley, se entenderá por operaciones la información consolidada anual referida a exportaciones e importaciones de mercancías propias o de terceros, que hayan sido realizadas por cualquier Usuario Directo del Parque de Servicios o Centro de Servicios. Asimismo, se entenderá por inventario y sus movimientos, toda la información relacionada a mercancías consolidadas anuales, en el formulario que determine la Dirección. En caso de requerirse otra información, deberá ser solicitada por escrito al Usuario Directo, la cual deberá ser entregada en un plazo de 15 días hábiles. La remisión anual de la información a la Dirección, deberá hacerse a más tardar 30 días hábiles después de finalizado el año. La DGA se reserva la facultad de requerir información documental diferente y/o adicional…" | For the Art. 47 a) obligations, "operations" means the ANNUAL CONSOLIDATED information on exports and imports of the beneficiary's own or third parties' goods performed by any usuario directo of the parque or centro; "inventory and its movements" means all information on goods consolidated annually, IN THE FORM (formulario) THE DIRECCIÓN DETERMINES. Other information, if required, is requested IN WRITING from the usuario directo and delivered within 15 días hábiles. The ANNUAL REMISSION of the information is made AT LATEST 30 días hábiles AFTER THE END OF THE YEAR. The DGA reserves the power to require different and/or additional documentary information | `sv/sources/17b_Reglamento_Servicios_Internacionales.pdf` | Art. 44 pp.15-16 (EVID-266; txt PAGE 15-16; SOQ-30 print) |
| LB-021 | Ley Orgánica de la DGA (13_), Art. 19: "El control aduanero podrá desarrollarse de las siguientes maneras: a) Control inmediato; b) Control a posteriori; y, c) Control permanente… Por control a posteriori, se entenderá aquél que se ejerce respecto de las operaciones aduaneras, los actos derivados de ellas, las declaraciones aduaneras, las determinaciones de las obligaciones tributarias aduaneras, los pagos de los tributos y la actuación de los auxiliares de la función pública aduanera… dentro del plazo de caducidad… Asimismo, dentro de las actividades de control a posteriori, las autoridades fiscalizadoras podrán verificar el manejo de inventarios, los métodos de valuación y registro del mismo… Por control permanente, se entenderá aquél que se ejerce en cualquier momento sobre los auxiliares de la función pública aduanera, respecto del cumplimiento de sus requisitos de operación, deberes y obligaciones. Se ejercerá también sobre las mercancías que, con posterioridad al levante o retiro, permanezcan sometidas a alguno de los regímenes aduaneros suspensivos o liberatorios, a efecto de fiscalizar y verificar el cumplimiento de las condiciones de permanencia, uso y destino de tales mercancías." | Customs control may develop as: a) immediate control; b) A-POSTERIORI control; c) PERMANENTE control. A-posteriori control is exercised over customs operations, their derivative acts, customs declarations, determinations of customs tax obligations, tribute payments and the performance of the customs auxiliaries — within the caducidad term; within a-posteriori activities the fiscalization authorities may VERIFY INVENTORY HANDLING, VALUATION AND REGISTRATION METHODS. Permanente control is exercised at any moment over the auxiliaries' operating requirements, duties and obligations, and ALSO over goods that, after levante or withdrawal, remain under SUSPENSIVE OR LIBERATORY customs regimes — to fiscalize and verify compliance with the conditions of PERMANENCE, USE AND DESTINATION of such goods | `sv/sources/13_Ley_Organica_Aduanas.pdf` | Art. 19 pp.10-11 (EVID-268; txt PAGE 10-11; SOQ-30 print) |
| LB-022 | Ley de Simplificación Aduanera (74_), Art. 13 (retention-kin fragment): "…EL TIEMPO EN QUE SE DEBERÁN TENER A DISPOSICIÓN LOS REGISTROS CONTABLES, REGISTROS ESPECIALES Y LA DOCUMENTACIÓN DE RESPALDO… SERÁ DE CINCO AÑOS." | The time during which accounting records, special records and support documentation must remain at the customs authority's disposal is FIVE YEARS (the customs retention floor — kin anchor for the LSI 5-year manifiesto/contractual-document retention flags of this file; the canonical retention-matrix row is commercial-legal/02 §3.7 by id, noted there by `06`'s SV-SPE-FR-126 — never restated here) | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 13 p.12 (EVID-271; txt PAGE 12; SOQ-30 print) |
| LB-023 | LESIA (79_), Art. 3: "las infracciones aduaneras se clasifican en administrativas, tributarias y penales. SON INFRACCIONES ADMINISTRATIVAS AQUELLOS ACTOS U OMISIONES… SIN QUE PUEDAN OCASIONAR UN PERJUICIO FISCAL. SON INFRACCIONES TRIBUTARIAS… QUE PUEDAN OCASIONAR UN PERJUICIO FISCAL, SIN QUE LLEGUEN A TIPIFICARSE COMO DELITO. SON INFRACCIONES PENALES LAS ACCIONES U OMISIONES DOLOSAS O CULPOSAS TIPIFICADAS COMO DELITO…". "LAS CONDUCTAS… SE SANCIONARÁN EN FORMA INDEPENDIENTE, AUN CUANDO TENGAN ORIGEN EN UNA MISMA DECLARACIÓN DE MERCANCÍAS, APLICANDO LA SANCIÓN PREVISTA PARA CADA INFRACCIÓN ESPECÍFICA, SIN PERJUICIO QUE PUEDA HACERSE EN UN SOLO ACTO." Art. 6: "LAS INFRACCIONES TIPIFICADAS EN EL ARTÍCULO ANTERIOR SERÁN SANCIONADAS CON UNA MULTA EQUIVALENTE A CINCUENTA DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$50.00), SALVO LAS INFRACCIONES ESTABLECIDAS EN LOS LITERALES c), d), e), f), m), n), o), p), Y y) LAS QUE SERÁN SANCIONADAS CON UNA MULTA EQUIVALENTE AL 0.5% SOBRE EL PATRIMONIO O CAPITAL CONTABLE QUE FIGURE EN EL BALANCE GENERAL MENOS EL SUPERÁVIT POR REVALÚO DE ACTIVOS NO REALIZADO, LA QUE NO PODRÁ SER INFERIOR A UN SALARIO MÍNIMO MENSUAL, CORRESPONDIENTE AL SECTOR COMERCIO. ASIMISMO, LAS INFRACCIONES CONTEMPLADAS EN LOS LITERALES i), j), k), Y ñ) SERÁN SANCIONADAS CON UNA MULTA EQUIVALENTE A TRES SALARIOS MÍNIMOS MENSUALES CORRESPONDIENTES AL SECTOR COMERCIO…" (registry-inexactitude: "LA DIRECCIÓN GENERAL SUSPENDERÁ EL ACCESO DEL INFRACTOR AL SISTEMA INFORMÁTICO…"; balance mechanics + auditor signature + refusal-fallback 3 SMM; tránsito literal a): "MULTA EQUIVALENTE A SEIS SALARIOS MÍNIMOS MENSUALES ASIGNADOS AL SECTOR COMERCIO… LA REINCIDENCIA… INCREMENTARÁ LA MULTA EN UN CINCUENTA POR CIENTO" + annual fianza "EQUIVALENTE AL VALOR TOTAL DE LA MERCADERÍA TRANSPORTADA EN EL AÑO ANTERIOR… MÁS LOS CORRESPONDIENTES DERECHOS E IMPUESTOS"; courier: "LOS CASOS DE ENVÍOS DE BAJO VALOR… NO ESTARÁN SUJETOS A LAS MULTAS… MONTOS IGUALES O MENORES A CINCUENTA DÓLARES… (US$50.00) DEL VALOR FOB"). Art. 53: "Para la cuantificación de las sanciones pecuniarias cuya aplicación se establezca con base en el salario mínimo fijado por la autoridad competente, deberá considerarse el salario mínimo mensual para el comercio y la industria en la ciudad, vigente a la fecha en que se haya cometido la infracción." | Art. 3 — customs infringements classify as ADMINISTRATIVE (no fiscal damage possible), TAX (fiscal damage below crime) and PENAL (statutory crimes); conducts are sanctioned INDEPENDENTLY even when originating in the same DM, applying each specific infraction's sanction (single administrative act permitted). Art. 6 — administrativa multas: flat US$50.00 default; 0.5% of equity/contable capital per the general balance (minus unrealized revaluation surplus), floor ONE comercio-sector SMM, for literals c)/d)/e)/f)/m)/n)/o)/p)/y); THREE comercio-sector SMM for literals i)/j)/k)/ñ) [k) repealed — as printed] and as the no-balance/refusal fallback; registry inexactitude additionally suspends the infractor's DGA-system access; literal a) tránsito breaches: SIX comercio-sector SMM, recidivism +50%, recidivist transportists render an ANNUAL BOND for the value of goods transported in the prior year plus duties/taxes; express-courier low-value shipments (≤ US$50.00 FOB) NOT subject to these multas. Art. 53 — SMM-based pecuniary sanctions quantify against the COMERCIO E INDUSTRIA (city) monthly minimum wage current at the infraction date | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 3 p.3; Art. 6 pp.7-8; Art. 53 p.28 (EVID-359/360; txt PAGE 3/7-8/28; INDICE print through D.L. 588-2008 — OQ-6) |
| LB-024 | LESIA (79_), Art. 8 a) (fragment, tolerance regime): granel "se considerará una tolerancia máxima del 5% del peso total… pero se hará efectivo el cobro de los derechos e impuestos"; non-granel "MARGEN DE TOLERANCIA MÁXIMA DEL 3% SOBRE LOS PARÁMETROS DE CANTIDAD, VOLUMEN, PESO O VALOR… APLICÁNDOSE EL MÁS FAVORABLE AL IMPORTADOR… PERO SE HARÁ EFECTIVO EL COBRO…", both "SIEMPRE Y CUANDO EL IMPORTADOR HAYA EFECTUADO LA DECLARACIÓN DE MERCANCÍAS PREVIAMENTE AL INGRESO… Y NO HAYA EFECTUADO INSPECCIÓN PREVIA ALGUNA"; "EN EL CASO QUE EL EXCEDENTE SEA MAYOR DEL 3% PERO EL IMPUESTO QUE SE DEBE PAGAR NO EXCEDA DE CIEN DÓLARES… (US$100.00), SE APLICARÁ UNA SANCIÓN EQUIVALENTE AL 100% DEL IMPUESTO DEJADO DE PAGAR". Art. 8 f): "LA TRANSFERENCIA DE DOMINIO O LA ENTREGA DE MERCANCÍAS AMPARADAS EN LOS REGÍMENES DE ZONAS FRANCAS, ADMISIÓN TEMPORAL PARA PERFECCIONAMIENTO ACTIVO Y DEPÓSITO DE ADUANAS, A PERSONAS DOMICILIADAS EN EL PAÍS, SIN LA AUTORIZACIÓN CORRESPONDIENTE O EL PAGO DE DERECHOS E IMPUESTOS APLICABLES CUANDO PROCEDA". Art. 9: "LAS CONDUCTAS TIPIFICADAS EN LOS LITERALES a), b), c), d) Y e) DEL ARTÍCULO ANTERIOR, SOLAMENTE CONSTITUIRÁN INFRACCIÓN TRIBUTARIA CUANDO EL PERJUICIO FISCAL PROVOCADO NO SOBREPASE LA CANTIDAD DE DOSCIENTOS DIECIOCHO MIL SETECIENTOS CINCUENTA COLONES (¢218,750.00) O SU EQUIVALENTE EN DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA. CUANDO EL PERJUICIO FISCAL SEA SUPERIOR A DICHA SUMA, SE ESTARÁ A LO DISPUESTO EN EL ART. 22 DE ESTA LEY." + "En el caso de los literales c), e), f) y h) del artículo anterior, se presumirá legalmente que ha existido transferencia de dominio, cuando al practicar fiscalizaciones en los almacenes, bodegas o instalaciones de los beneficiarios del régimen aduanero respectivo, se determinen faltantes de mercancías que no hubieran sido debidamente justificados." Art. 10: "Sin perjuicio del pago de los derechos e impuestos que se adeuden, las infracciones tributarias serán sancionadas con una multa equivalente al 300% de los derechos e impuestos evadidos o que se pretendieron evadir. Cuando el perjuicio fiscal ocasionado sea inferior a cinco mil colones o su equivalente en Dólares…, la multa aplicable será equivalente al doscientos por ciento…". Art. 11: vehicles — literal j) "tres salarios mínimos por cada mes o fracción de mes que el vehículo usado permanezca en el país…"; literal n) "cien por ciento de los derechos e impuestos a la importación que correspondan al vehículo, calculado a la fecha de vencimiento del plazo de noventa días" | Art. 8 a) — tolerance margins (granel 5% weight; non-granel 3% of quantity/volume/weight/value, most favorable to the importer) conditioned on PRE-ARRIVAL declaration and no prior inspection: they suppress the SANCTION but never the collection of duties/taxes on the excess; excess >3% with tax ≤ US$100 → sanction = 100% of the unpaid tax. Art. 8 f) — transfer/delivery of ZF/ATPA/depósito goods to domestically-domiciled persons without authorization or payment = tax infraction (the descargo-register/prevention kin). Art. 9 — Art. 8 a)-e) conducts stay TAX infractions only while perjuicio fiscal ≤ ¢218,750.00 (= US$25,000; pegged print — Art. 22 states USD directly); above that → Art. 22 CRIME; unjustified FALTANTES at regime beneficiaries' premises legally PRESUME transfer of dominio (couples literal f) to the inventory registers). Art. 10 — multa = 300% of evaded duties/taxes (200% when damage < ¢5,000 ≈ US$571.43), besides the duties owed. Art. 11 — used-vehicle specials: 3 SMM per month-or-fraction overstaying; 100% of the vehicle's duties for the 90-day distributor breach | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 8 pp.9-12; Art. 9 p.12; Art. 10 p.12; Art. 11 p.12 (EVID-361/362; txt PAGE 9-12; INDICE print through D.L. 588-2008 — OQ-6) |
| LB-025 | LESIA (79_), Art. 22: "CUANDO LAS CONDUCTAS CONTEMPLADAS EN LOS LITERALES a), b), c), d) Y e), DEL ART. 8 DE ESTA LEY, PROVOQUEN UN PERJUICIO FISCAL SUPERIOR A VEINTICINCO MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA ($25,000.00), DICHAS CONDUCTAS CONSTITUIRÁN DELITO DE DEFRAUDACIÓN DE LA RENTA DE ADUANAS, EL CUAL SE SANCIONARÁ CON UNA PENA DE CUATRO A SEIS AÑOS DE PRISIÓN. EN IGUAL SANCIÓN INCURRIRÁ QUIEN CON LA INTENCIÓN DE OBTENER EXENCIONES O BENEFICIOS FISCALES O EVADIR LOS DERECHOS E IMPUESTOS Y DEMÁS CARGOS QUE SE COBRAN EN RAZÓN DE LA IMPORTACIÓN, PRESENTE DOCUMENTOS DE ACOMPAÑAMIENTO DE LA DECLARACIÓN DE MERCANCÍAS, FALSOS O ALTERADOS, SIN IMPORTAR LA CUANTÍA DEL PERJUICIO FISCAL. SE ENTENDERÁN DOCUMENTOS DE ACOMPAÑAMIENTO DE LA DECLARACIÓN, AQUELLOS QUE RESPALDEN LA OPERACIÓN ADUANERA DE IMPORTACIÓN Y SIRVAN DE SUSTENTO DE LOS DATOS CONSIGNADOS EN LA MISMA, TALES COMO: CERTIFICADO O CERTIFICACIÓN DE ORIGEN, FACTURA, DOCUMENTO DE TRANSPORTE, DECLARACIÓN DE VALOR, CUANDO PROCEDA Y OTROS DOCUMENTOS EXIGIDOS… EN LA LEGISLACIÓN NACIONAL Y EN LOS ACUERDOS, CONVENIOS, TRATADOS Y OTROS INSTRUMENTOS EN MATERIA DE COMERCIO VIGENTES. (1) (3) (4)" | Art. 8 a)-e) conducts with fiscal damage OVER US$25,000.00 constitute the CRIME OF DEFRAUDACIÓN DE LA RENTA DE ADUANAS — penalty FOUR TO SIX YEARS' IMPRISONMENT; the SAME penalty applies to whoever, intending to obtain exemptions/fiscal benefits or evade import duties/taxes/charges, presents FALSE OR ALTERED accompanying documents of the DM REGARDLESS of the damage amount — accompanying documents = those supporting the importation and sustaining the declared data: origin certificate/certification, invoice, transport document, declaration of value when applicable, and other documents required by national legislation and trade instruments | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 22 pp.17-18 (EVID-365; txt PAGE 17-18; the article 12_ Art. 40-A cites — LB-012's consumer anchor; INDICE print through D.L. 588-2008 — OQ-6) |
| LB-026 | LESIA (79_), Art. 13: "a) La caducidad de la exención de derechos e impuestos, en la importación de las mercancías objeto de las infracciones previstas en los literales c) y d) del artículo 8 de esta Ley, y como consecuencia, el infractor estará obligado al pago de los derechos e impuestos a la importación, vigentes a la fecha en que se aceptó la correspondiente Póliza o Declaración de Mercancías de Importación Definitiva a Franquicia; y, b) Suspensión temporal de las autorizaciones para operar bajo los regímenes de admisión temporal para perfeccionamiento activo, zonas francas, y tiendas libres, así como para administrar zonas francas, hasta por seis meses, cuando el infractor hubiere incurrido en la comisión de tres infracciones tributarias en un lapso de un año. La reincidencia en la causal de suspensión… se constituirá en una causal de revocatoria… se considerará reincidente quien incurra por segunda ocasión en una causal de suspensión dentro del período de cinco años… El Director General, será la autoridad competente… tiendas libres… En el caso de los regímenes de admisión temporal para perfeccionamiento activo y Zonas Francas, las suspensiones o revocatorias… serán impuestas por el Ministerio de Economía." Art. 14: "a) NO SE APLICARÁ SANCIÓN ALGUNA, CUANDO EL QUE COMETIERE UNA INFRACCIÓN ADMINISTRATIVA O TRIBUTARIA, LA RECONOCIERE Y SUBSANARE POR VOLUNTAD PROPIA Y SIEMPRE QUE NO SE HAYA DISPUESTO O INICIADO EL EJERCICIO DE LA VERIFICACIÓN INMEDIATA, VERIFICACIÓN DE ORIGEN, FISCALIZACIÓN A POSTERIORI O SE HAYA EMITIDO UNA RESOLUCIÓN MODIFICANDO O REVOCANDO UNA RESOLUCIÓN O CRITERIO ANTICIPADO BASADO EN INFORMACIÓN INCORRECTA O FALSA…; b) Cuando el que cometiere… aceptara por escrito los cargos durante la audiencia de 15 días… la sanción será atenuada en un cincuenta por ciento. No se aplicará la atenuante… a quien sea reincidente… dentro del plazo de seis meses…" | Art. 13 — consequences for tax-infraction subjects: a) EXEMPTION CADUCITY for Art. 8 c)/d) goods, obliging payment of import duties at the rates current on the ACCEPTANCE date of the corresponding franquicia definitive-import declaration/policy; b) TEMPORARY SUSPENSION up to SIX MONTHS of the authorizations to operate ATPA, ZONAS FRANCAS and tiendas libres (and to administer zonas francas) upon THREE tax infractions within ONE year; recidivism (a second suspension causal within FIVE years of the first) = REVOCATION ground — tiendas libres imposed by the Director General; ATPA/ZF by the MINISTERIO DE ECONOMÍA. Art. 14 — responsibility modifiers: NO sanction when the infractor recognizes and cures the breach voluntarily BEFORE any immediate verification, origin verification, a-posteriori fiscalization or advance-ruling revocation has been initiated; 50% ATTENUATION for written acceptance of charges during the 15-day hearing (barred for recidivists within six months of having enjoyed the benefit) | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 13 p.13; Art. 14 pp.13-14 (EVID-363; txt PAGE 13-14; INDICE print through D.L. 588-2008 — OQ-6) |
| LB-027 | LESIA (79_), Art. 29: "La Dirección General suspenderá a los auxiliares de la función pública aduanera hasta por noventa días en el ejercicio de su función…" causes a)-h) incl. d) inexact declaration injuring fiscal interest (safe harbor for documents delivered by the declarant without reason to doubt); e) inexact suspensive-regime declarations when suspended duties "exceda de cien mil colones o su equivalente en dólares"; f) firm unpaid tributary obligations (suspension while the incumplimiento subsists); g) un-renewed fianza; h) "HABER COMETIDO MÁS DE DOS INFRACCIONES TRIBUTARIAS EL AGENTE DE ADUANAS O DESPACHANTE ADUANERO EN UN LAPSO DE 6 MESES…" + "el auxiliar no podrá iniciar nuevas operaciones, sino solamente concluir las que tuviera ya iniciadas". Art. 30: cancelación causes a)-f) incl. b) consigning the name/domicilio/NIT/NRC of a person who did not request the auxiliar's services; f) "POR DELEGAR SUS FUNCIONES A PERSONAS NO AUTORIZADAS POR LA DIRECCIÓN GENERAL PARA REALIZAR LA TRANSMISIÓN ELECTRÓNICA DE LA DECLARACIÓN, MEDIANTE LA REVELACIÓN Y ACCESO DE SU CLAVE O FIRMA ELECTRÓNICA". Art. 54: "…son considerados como auxiliares de la función pública aduanera los agentes de aduana, los despachantes o apoderados especiales aduaneros, los transportistas y agentes de transporte, los depositarios, los administradores de zonas francas y cualquier otra persona a quien la legislación aduanera le otorgue expresamente esa calidad" + DGA keeps "un registro actualizado de los funcionarios… y de los auxiliares… que han sido objeto de sanciones" | Art. 29 — DGA suspends customs-public-function AUXILIARIES up to NINETY DAYS for the listed causes (provisional detention; mandate breach; unaccredited representation; inexact declarations — with the declarant-document safe harbor; suspensive-regime inexactitude over ¢100,000 (≈ US$11,428.57 — colones print); firm unpaid obligations, while subsisting; un-renewed bond, until renewed; agentes/despachantes with MORE THAN TWO tax infractions in SIX months); suspended auxiliaries may only conclude operations already initiated. Art. 30 — CANCELATION of the authorization (firm participation with prohibited goods; consigning an un-engaged person's data; condemnation for crimes against the Hacienda Pública; letting third parties act under the authorization; 5-year recidivism in the f) cause; DELEGATING electronic-declaration transmission by revealing the access key/electronic signature). Art. 54 — auxiliares = customs agents, despachantes/special customs attorneys, transportists and transport agents, depositaries, FREE-ZONE ADMINISTRATORS and others expressly qualified; DGA maintains a sanctions registry | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 29 pp.20-21; Art. 30 p.21; Art. 54 p.28 (EVID-367; txt PAGE 20-21/28; INDICE print through D.L. 588-2008 — OQ-6) |
| LB-028 | LESIA (79_), Art. 31: the attributed infractor may contest "CONFORME AL PROCEDIMIENTO ESTABLECIDO EN EL ART. 17 DE LA LEY DE SIMPLIFICACIÓN ADUANERA", apertura notified with "EL CONTENIDO INTEGRO DE LA HOJA DE DISCREPANCIAS O DE UN INFORME DE FISCALIZACIÓN O INVESTIGACIÓN"; express written acceptance → resolution "INMEDIATAMENTE DESPUÉS DE DICHA ACEPTACIÓN"; "EL PLAZO DE QUINCE DÍAS HÁBILES QUE OTORGA EL ART.17 DE LA LEY DE SIMPLIFICACIÓN ADUANERA, OPERARÁ COMO PLAZO DE AUDIENCIA Y PRUEBA"; goods release "PREVIO RENDIMIENTO DE LA GARANTÍA O FIANZA RESPECTIVA… CONFORMADO POR LOS DERECHOS E IMPUESTOS QUE HABRÍAN DEJADO DE PERCIBIRSE Y LA MULTA APLICABLE". Art. 32: rights a)-f) (charge notification; petition; contradiction — legal evidence, hearing, reasoned decision, recursos; expediente access; innocence presumption; prior procedure). Art. 36: for Art. 5 c)/d)/e)/f), the sealed request and the technician's act/informe "CONSTITUIRÁN PLENA PRUEBA"; "EL REQUERIDO CONTARÁ CON UN PLAZO DE DIEZ DÍAS HÁBILES, CONTADOS A PARTIR DEL DÍA SIGUIENTE AL RECIBO DE DICHA SOLICITUD". Art. 33 (final ¶): "La facultad sancionatoria de la autoridad aduanera prescribirá en un plazo de cinco años contados a partir de la fecha de la comisión de la infracción… o de la fecha en que se descubra… Dicho término de prescripción se interrumpirá desde que se notifique… la Hoja de Discrepancias o el Informe de Fiscalización…". Art. 37 (final ¶): "…la multa deberá ser cancelada dentro de los ocho días hábiles siguientes a la fecha en que dicha resolución adquiera estado de firmeza. Vencido dicho plazo, se causarán los intereses moratorios respectivos." Art. 38: "…suspensión de nuevos despachos de mercancías de los consignatarios o declarantes que hayan sido sancionados pecuniariamente, en tanto no cancelen… salvo que exista recurso pendiente de resolución." | Art. 31 — LESIA's sanctioning PROCEDURE rides the 74_ Art. 17 chassis (the same clocks `06`'s FR-128 owns): apertura with the FULL discrepancy sheet/fiscalization/investigation report; the 15-días-hábiles term operates as hearing-and-proof term; express written acceptance yields an IMMEDIATE resolution; contested goods releasable any time on a guaranty covering unperceived duties + applicable multa. Art. 32 — due-process rights (charge notice, petition, contradiction with evidence/hearing/reasoned decision/recourses, expediente access, innocence presumption, prior procedure). Art. 36 — for the document-custody/control/refusal literals the sealed information request or the technician's act/informe is FULL PROOF; 10 días hábiles to answer DGA requests. Art. 33 — sanctioning power prescribes in FIVE years from commission (or discovery), interrupted by notification of the discrepancy sheet/fiscalization report (tracker consumed from `06` FR-178 by id). Art. 37 — multas payable within EIGHT días hábiles of FIRMEZA, moratory interest after. Art. 38 — suspension of NEW despachos for pecuniarily sanctioned consignees/declarants until paid, save pending recourse (consumed from `06` FR-177 by id) | `sv/sources/79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf` | Art. 31 pp.21-22; Art. 32 pp.22-23; Art. 33 p.23; Art. 36 p.24; Art. 37 p.24; Art. 38 p.24 (EVID-368/369; txt PAGE 21-24; INDICE print through D.L. 588-2008 — OQ-6) |

## 3. Functional Requirements

### 3.1 ZF/DPA obligations — the Art. 28 register chassis (12_ Art. 28)

- **SV-SPE-FR-130:** The system shall carry the 12_ Art. 28 obligation
  set as a dated obligation catalog per ZF usuario / DPA titular, one row
  per literal a)-s), each row carrying: the addressee (administrador for
  usuarios / MINEC for DPAs where the text splits), a compliance-state
  field (met · pending · breached) with evidence reference, and its
  statutory infringement tier per the Art. 28 final classification
  (leves: a), c), f), g), h), i), q); graves: b), d), e), j), k), l),
  m), n), o), p), s); muy graves: r)) — the tier is the hook the
  sanction family of FR-140..142 prices; literals whose automation
  surface is owned by sibling files are catalogued here WITHOUT
  restating them (k) traslados = `04`'s clocks by id; o) Art. 9
  compliance = `01`'s authorization frame by id); the
  physical/administrative-only duties (d) delegado ingress, f)/g)
  custody means, h) transmission equipment, i) DPA area for
  servicio-aduanero personnel, m) bulto-differences communication) are
  catalog rows with manual compliance states and no automation surface.
  (LB-001; LB-003; LB-004; LB-005; LB-006; EVID-258)
- **SV-SPE-FR-131:** The system shall record the plan/project
  modification notice of Art. 28 a) as a workflow notice event with its
  statutory clock: addressed to the ZF administrador (usuarios) or MINEC
  (DPAs), due within 10 *días hábiles* counted from the day of the
  modification (días-hábiles arithmetic consumed from SV-FREP-FR-202..204
  by id); the notice event carries the modification description, the
  addressed authority and the presented/date-stamped state, feeding the
  a)-literal compliance row of FR-130 (tier: leve).
  (LB-001; EVID-258)
- **SV-SPE-FR-132:** The system shall maintain, per ZF usuario / DPA
  titular, the electronic inventory register of ENTRIES, EXITS AND
  BALANCES plus the *cuadro demostrativo de descargo* per import, as one
  DGA-facing register surface reconciling PER-DM cancellations: each
  import (DUCA record of `06` by id — SV-SPE-FR-104 acceptance anchor)
  carries its saldo under the regime, its descargo events (export,
  traslado, internación, destruction — the disposition surfaces of
  `04`/`05` by id) and a computed pending balance, so the cuadro
  demonstrates the discharge of each declaration against the per-DM
  clock of `04` (SV-SPE-FR-064..081 by id — never restated); the
  register is produced for ONLINE availability at the DGA's disposal,
  with the statutory FALLBACK mode recorded: when not kept online, the
  movement records (inventory movement, descargo cuadro, import
  movement, and all import/export/tránsito/traslado operation
  information for fiscal control) are remitted in the required
  electronic/magnetic media within 20 *días hábiles* following the
  fiscal-year end — the remittance state (due date from the calendar
  engine by id; presented; on-request remittance events) stamps the
  register record (external-interface note: Odoo produces the register
  and its exports; DGA systems consume them).
  (LB-001; EVID-258)
- **SV-SPE-FR-133:** The system shall assemble the semestral MINEC
  informe per ZF/DPA beneficiary as a dated report record with the FIVE
  statutory data groups, each group sourced from its ledger of record by
  id and never hand-keyed: i) importaciones — VALUE AND ORIGIN (DUCA
  import records of `06` by id); ii) exportaciones — VALUE AND
  DESTINATION (DUCA export records by id); iii) generación de empleo
  (payroll headcount records, payroll/05-06 by id); iv) ventas al
  mercado nacional (the TAN-sale/internación surfaces of `05` by id);
  v) monto de la inversión realizada (the requisito investment log of
  `01` SV-SPE-FR-010 by id); the informe carries its semester window,
  presented state and MINEC addressee (the report FORMAT is delegated
  to the Reglamento/DACG layer — config slot, no default; OQ-4).
  (LB-002; EVID-258)
- **SV-SPE-FR-134:** The system shall record the cambio/cierre notice
  of Art. 28 e) as a dated notice event due 30 DAYS IN ADVANCE
  (calendar days, as printed) before any change of domicile or closure
  of operations, addressed to the MINEC dependency determined by the
  reglamento and to the DGA; the closure branch links the FR-148
  Art. 40-A checklist by id (never restated there).
  (LB-002; EVID-258)
- **SV-SPE-FR-135:** The system shall maintain the damaged/lost/
  destroyed goods registry of Art. 28 l): one irregularity record per
  event (goods dañadas, perdidas, destruidas, and demás irregularidades)
  occurring while goods remain in the DPA, carrying quantity/value,
  cause, the *fuerza mayor/caso fortuito* proven-to-DGA flag of literal
  j) (which switches off the fisco-liability state), and the
  at-DGA's-disposal presentation state; each record links its goods to
  the descargo register of FR-132 so unexplained losses surface as
  pending balances, and the fisco-liability state (literal j) flags the
  tribute obligations payable to the fisc for lost/misdirected/
  miscontrolled goods absent proven fortuity (payment computation owned
  by `05`'s duty surfaces by id).
  (LB-003; EVID-258)
- **SV-SPE-FR-136:** The system shall model the DPA physical-segregation
  duty of Art. 28 n) as warehouse and traceability config: separate
  stock locations for goods of the SUSPENSIVE regime vs NATIONALIZED
  goods (which must remain duly separated in the bodega whenever both
  are combined or mixed in the production process), the installation
  delimitation/independence flags as manual compliance states on the
  FR-130 row, and an inventory control that identifies the suspensive
  vs nationalized components IN THE COMPENSATED PRODUCT — lot-level
  tracing through the production order so the DESTINATION of each
  component remains traceable (trazabilidad), consumed by the FR-139
  insumo register and auditable under the FR-165 backdrop.
  (LB-004; EVID-258)
- **SV-SPE-FR-137:** The system shall maintain cost records for goods
  sold to the national market (Art. 28 p): per TAN-sold good, a cost
  record assembling the cost components backing the internación duty
  base — consuming `05`'s internación surfaces by id (valor en aduana =
  materias primas + gastos indirectos de fabricación for transformed
  goods; comercializador full-value-minus-national-component), gated on
  the row's two statutory preconditions (duly authorized for the sale;
  tributes paid) as flags with their evidence references.
  (LB-005; EVID-258)
- **SV-SPE-FR-138:** The system shall generate, per ZF usuario, the
  annual pending-cancellation goods report of Art. 28 q): goods
  pendientes de cancelar as of fiscal-year end, drawn from the FR-132
  descargo register's pending balances, due to the servicio aduanero
  within 20 *días hábiles* following the fiscal-year end (calendar
  engine by id) — with the statutory option recorded that this
  information MAY be included in the FR-132 b)-literal register
  remittance (one consolidated remittance event where both are filed
  together).
  (LB-005; EVID-258)
- **SV-SPE-FR-139:** The system shall maintain the pormenorized
  insumo-vs-producto-compensador register of Art. 28 s): per production
  lot, the detailed record of *insumos* consumed in the productive
  process IN RELATION TO the *productos compensadores* obtained —
  quantity consumed per input, output quantity, and the implied yield
  and *merma* (shrinkage/loss) tracing — linked lot-to-lot with the
  FR-136 segregation control and the per-DM descargo of FR-132, and
  exhibitable at DGA fiscalization request (presentation state per
  investigation reference); the register reconciles input totals
  against import saldos so unaccounted consumption surfaces as pending
  balance.
  (LB-005; EVID-258)

### 3.2 ZF/DPA sanctions + enforcement states (12_ Arts. 28 final/31/36/36-A/37/37-A/39/40-A)

- **SV-SPE-FR-140:** The system shall implement the ZF/DPA sanction
  ladder of Art. 36 as sanction-consequence rows keyed by infringement
  class: LEVE → written *prevención* (warning) with a statutory cure
  term; reincidencia in a leve → multa of 3 SMM "de mayor cuantía";
  GRAVE → multa of 5 SMM "de mayor cuantía"; MUY GRAVE (the literal-r
  destino-autorizado breach) → temporary suspension for a MAXIMUM of
  3 months; reincidencia in a muy grave → DEFINITIVE suspension of the
  benefits — every suspension/definitive-suspension consequence stamps
  the benefit-state field of `01` (SV-SPE-FR-015/016 by id: suspensión
  makes tributes payable and the benefit clock keeps running), and the
  ladder is kept DISTINCT from the LSI 30/40-SMM ladder of FR-162
  (never unified, per the regime-distinctness invariant).
  (LB-007; LB-006; EVID-258)
- **SV-SPE-FR-141:** The system shall resolve the SMM unit "de mayor
  cuantía" (highest-amount monthly minimum wage) for every SMM-priced
  sanction of this file as a DATED config lookup consumed from
  `payroll/02_minimum-wage.md` BY ID (the SV-PAY-FR-022 sector-mapping
  configuration + the dated SMM sidecar rows — this file NEVER encodes
  SMM values): working assumption (SOQ-33, labeled) = the HIGHEST
  monthly sector row of the operative 16_ vintage — which selects
  comercio y servicios at the current vintage (industria ties at the
  same printed value; the tie-break is part of the labeled assumption)
  — resolved as-of the sanction's anchor date and SNAPSHOT on the
  sanction record with the sidecar row reference (D15: dated row +
  provenance; never a global constant); the unit is shared by the ZF
  (FR-140) and LSI (FR-162) ladders while their multipliers remain
  distinct.
  (LB-007; EVID-258; SOQ-33)
- **SV-SPE-FR-142:** The system shall classify every recorded ZF/DPA
  breach as an infracción record carrying its statutory class (leve ·
  grave · muy grave per the Art. 28 final map, from the FR-130 catalog
  row's tier), its basis literal, the open/cured state and a
  per-beneficiary per-class reincidencia counter that feeds FR-140's
  escalations (prevención → multa for leves; muy-grave reincidencia →
  suspensión definitiva); the same record family receives the Art. 37-A
  fianza consequence as a dated event flag (MH+MINEC MAY require a
  fianza on repeated customs/tax infringements or a firm penal sentence
  — amount authority-set, config slot, NO shipped default), and the
  Art. 48 procedure of `01` (SV-SPE-FR-019 by id) wraps every
  determination (5-días-hábiles audiencia, 10-day resolution — never
  restated here).
  (LB-006; LB-010; EVID-258)
- **SV-SPE-FR-143:** The system shall run the Art. 36-A MH
  regularization clock as a dated enforcement record: when MH (DGA/DGII)
  detects graves per Art. 28 or local-market sales without the
  corresponding payment of duties and taxes, a notification event opens
  a 30-DÍAS-CALENDARIO cure window counted from the day after
  notification (CALENDAR days, as printed — NOT the días-hábiles
  engine); the notification must carry the printed warning that failure
  to cure leads the DGA, as a precautionary measure, to SUSPEND THE
  BENEFICIARY'S ACCESSES to its computer systems for customs operations;
  expiry without cure stamps the customs system-access suspension state
  (the DGA-access field of `01`'s profile, SV-SPE-FR-018 by id — same
  field the inactivity disablements stamp), and rehabilitation is
  recorded ONLY upon regularization of the detected situation.
  (LB-008; EVID-258)
- **SV-SPE-FR-144:** The system shall stamp every firm multa sanction
  with its Art. 37 payment window: made effective within 30 DAYS
  (calendar, as printed) following notification of the sanction, payable
  at the Dirección General de Tesorería or its authorized institutions —
  carried as payment metadata (due date, payment state, payment
  reference) on the FR-142 infracción record.
  (LB-007; EVID-258)
- **SV-SPE-FR-145:** The system shall implement the Art. 37-A fianza
  link for ZF/DPA as a dated consequence event: repeated customs/tax
  infringements determined by DGA/DGII fiscalization, or a firm penal
  sentence for violating customs legislation known to them, MAY trigger
  the MH+MINEC fianza requirement — event record with cause class and
  resolution reference, amount = config slot with NO shipped default
  (LSI twin = `03`'s SV-SPE-FR-061 by id, never restated).
  (LB-010; EVID-258)
- **SV-SPE-FR-146:** The system shall implement the ZF/DPA
  SS-payment-breach sanction of Art. 31 as a state-stamping consequence
  consuming the SS records by id (payroll/06 payment/remittance records;
  the solvency gate SV-SPE-FR-102 of `05` by id): when a firm and
  definitive resolution of MTPSS/ISSS/Superintendencia de Pensiones for
  unpaid patronal cotizaciones or un-transferred withheld sums is
  notified to the Minister of Economy, the record carries the Minister's
  decision — temporary suspension of benefits for THREE MONTHS, and on
  reincidencia the DEFINITIVE suspension — stamping `01`'s benefit state
  (SV-SPE-FR-015 by id) with reason art31_ss_breach (the ZF
  reincidencia consequence is suspensión definitiva; the LSI twin's is
  revocatoria — FR-163, kept distinct).
  (LB-009; EVID-258)
- **SV-SPE-FR-147:** The system shall stamp the inactivity sanction
  consequences consuming `01`'s monitors BY ID (SV-SPE-FR-018 — the
  12-month ZF and 3-month LSI inactivity monitors; their procedure
  clocks live there and are never restated): when the ZF monitor fires
  at the 13th month of continuous inactivity (regime imports/exports),
  the category-loss state perdida_inactividad stamps with the DGA
  system deregistration (dar de baja) recorded as a side effect; when
  the LSI monitor fires at the 3rd continuous month, the revocation
  state stamps with the DGA computer-system access disablement recorded
  — both as sanction-consequence records linking the monitor event, the
  audiencia/resolution references and the state stamped.
  (LB-011; LB-017 (Art. 62 fragment); EVID-258/264)
- **SV-SPE-FR-148:** The system shall implement the Art. 40-A
  closure-with-open-DMs surface as a closure checklist record: on a
  definitive-closure notification to the DGA, the checklist inventories
  the beneficiary's OPEN DMs under the ZF/admisión-temporal-perfecting
  regime (from `04`'s per-DM clocks and `06`'s DUCA records by id),
  their cancellation/descargo demonstration state (linked to the FR-132
  register) and the duties-and-taxes payment state for goods whose
  cancellation or discharge is NOT demonstrated; **W19 anchor (SOQ-32
  consumed — 79_ Art. 22 = LB-025):** the statutory crime consequence —
  closure or abandonment WITHOUT notifying the DGA and effecting the
  imposed cancellations constitutes the DELITO DE DEFRAUDACIÓN DE LA
  RENTA DE ADUANAS per Art. 22 LESIA — is recorded as an ANCHORED
  pointer flag: elements = Art. 8 a)-e) conduct with perjuicio fiscal
  OVER US$25,000.00 (dated literal; the colones twin ¢218,750.00 noted
  as printed) → pena 4-6 años prisión, OR false/alterated accompanying
  documents (origin certificate/certification, factura, transport
  document, declaración de valor, otros exigidos) with
  exemption/evasion intent REGARDLESS of amount — penal procedure and
  pena execution stay authority-side (zero mechanics restated); the
  crime-threshold gate on sanction records is owned by FR-181 by id;
  the Art. 40
  judicial abandono procedure is an informational note (judicial forum,
  not an Odoo surface).
  (LB-012; LB-025; EVID-258/365)

### 3.3 LSI obligations — Arts. 46-49 catalogs (14_ Arts. 46-49)

- **SV-SPE-FR-149:** The system shall carry the Art. 46 obligation set
  as a dated catalog per LSI usuario directo (parques and centros), one
  row per literal a)-f), each with class = MENOS GRAVE and a compliance
  state: a) the 10-*días hábiles* modification notice (to the parque
  administrador AND the MINEC dependency — the latter ALONE for centros;
  calendar engine by id); b) the ≥500 m² minimum property extent (or
  the lesser area authorized per Art. 22 a) — exception flag from
  `03`'s requisito rows by id); c) the 5-YEAR retention of
  consolidated-cargo manifiesto copies (retention flag with the
  customs-5y floor kin — LB-022 — and the canonical matrix consumed
  from commercial-legal/02 by id, never restated); d) custody/
  conservation means (manual state); e) the 8-DAY (calendar, as
  printed) notice to the servicio aduanero of loss, destruction,
  damage, abandono and other goods irregularities — a dated notice
  event from the occurrence date; f) the temporary exam/verification/
  abandono/retained storage spaces (manual state).
  (LB-013; LB-022; EVID-264/271)
- **SV-SPE-FR-150:** The system shall implement the Art. 47 a)
  electronic-records ANNUAL remittance as a dated report obligation:
  all information on the beneficiary's operations, inventories and
  their movements (plus any other information required for fiscal and
  administrative control) recorded in electronic/magnetic media (or any
  medium MINEC/MH require through the DGA), REMITTED ANNUALLY to those
  institutions — or when they request it — with the request-driven
  remittance events, the fiscalización/inspection exposure and the
  SYSTEMS-AUDIT permission (the computer records must permit audit of
  the systems themselves) recorded as capability flags on the record
  (external-interface note: Odoo produces the records/exports; the
  ministries consume them; the 17b_ Art. 28 register of FR-154..157
  and the Art. 44 report of FR-159 are THIS obligation's
  reglamento-defined content for distributors — consumed by id).
  (LB-014; EVID-264)
- **SV-SPE-FR-151:** The system shall carry the remaining Art. 47
  obligations as catalog rows with class = GRAVE and compliance states:
  b) the 30-day (calendar, as printed) cambio/cierre notice stating
  whether the closure is TEMPORAL or DEFINITIVA with reasons (dated
  notice event; the records remittance rides FR-150); c) delegado
  ingress + truthful information (manual state); d) accounting controls
  and records per the Law (flag; the accounting surfaces belong to
  accounting topics by id); e) the PHYSICAL inventory of goods under
  custody for distributors/logistics operators, carried in their
  specialized computer system (linked to the FR-154 register by id);
  g) NO activities outside the authorized parque/centro (validation
  flag on operating locations); h)-j) labor/social-security compliance,
  closure payouts and assets-first-to-labor rules (manual states;
  payroll kin by id); f) the semestral dictamen and k) the
  90%-Salvadoran quota are consumed from `03` BY ID (SV-SPE-FR-051..055
  and SV-SPE-FR-058 — never restated here).
  (LB-014; EVID-264)
- **SV-SPE-FR-152:** The system shall carry the Art. 48
  parque-administrador obligations as a dated catalog (class = MENOS
  GRAVE): the 5-YEAR retention of the contractual-relation documents
  and information with usuarios directos at the servicio aduanero's
  disposal (retention flag, LB-022 kin, canonical matrix by id); the
  damaged/lost/destroyed/abandoned-goods irregularities information
  duty to the servicio aduanero (notice-event surface sharing FR-149 e)
  semantics, administrador-addressed); plus the remaining literals
  (authority requirements, delegation equipment, legal-representative
  accreditation, custody means) as manual compliance states.
  (LB-015; LB-022; EVID-264)
- **SV-SPE-FR-153:** The system shall record the Art. 49 marchamo
  entry/exit duties as gate-and-event records for parque administradores
  (class = GRAVE; reincidencia = MUY GRAVE): vehicle entry into the
  parque only after verifying the condition and state of the marchamos
  and other security measures when there is no customs presence (the
  verification NEVER including breaking the seal), the timely
  communication of the entry and any irregularity found to the servicio
  aduanero, and goods EXIT only with customs-authority authorization at
  the enabled hours and days — entry/exit event records carrying the
  marchamo verification state, the authorization reference and the
  hours/days validation.
  (LB-015; EVID-264)

### 3.4 17b_ Art. 28 inventory-register contract + annual report (LSI distributors)

- **SV-SPE-FR-154:** The system shall implement the 17b_ Art. 28
  electronic inventory register for LSI distribution/logistics
  beneficiaries as ONE DGA-facing register surface, updated, with
  ONLINE access at the DGA's disposal, covering depósito temporal,
  admisión temporal, mercancías en abandono, retenidas
  administrativamente, entre otras — and exposing the TEN mandatory
  consultas/reportes verbatim as report specifications: a) daily
  register of goods ingresos/egresos regardless of operation type; b)
  inventory saldo; c) report of goods declarations with their
  respective cancelaciones or destinaciones; d) report of declarations
  reflecting saldos; e) report of goods in abandono WITH DETAIL of the
  affected declarations; f) report of goods under depósito temporal;
  g) report of goods under admisión temporal; h) report of mercancías
  retenidas administrativamente (goods decomisadas as
  prohibited/restricted in nature); i) report of goods in acopio para
  la exportación (when the operation is authorized — the 17b_ Art. 30
  authorization flag); j) report of almacenaje simple goods PER
  CONTRIBUYENTE (when authorized) — report items i)/j) activate only on
  their DGA-authorization flags; this register is the surface `03`'s
  dictamen checklist consumes for its per-client per-service-type
  physical-inventory verification (SV-SPE-FR-053 e.5 by id) and the
  FR-150 annual remittance feeds.
  (LB-018; EVID-266)
- **SV-SPE-FR-155:** The system shall implement the register's query
  dimensions per the printed contract: the reportes shall permit
  consultations BY goods declaration (Declaración de Mercancías), BY
  regime (Régimen), BY destinación and BY contribuyente — as filter
  facets on every report of FR-154 a)-j), each facet resolvable against
  the DUCA record (declaration), the regime discriminators of `01`
  (regime/destinación — SV-SPE-FR-001/002 by id) and the partner record
  (contribuyente).
  (LB-018; EVID-266)
- **SV-SPE-FR-156:** The system shall enforce the item-identification
  contract on every register entry: goods recorded by their nombre
  comercial (commercial name), código (code), identification with the
  partida arancelaria (tariff heading) AT THE SIX-DIGIT LEVEL (SAC-6),
  and the número de documento de ingreso (entry-document number) to the
  parque's usuario directo — the SAC-6 classification is MANDATORY on
  every item (no register line without it), sharing the SAC code source
  with the DUCA line classification of `06` (SV-SPE-FR-108 by id — same
  code family, never restated).
  (LB-018; EVID-266)
- **SV-SPE-FR-157:** The system shall provide an Excel-transferable
  export of every report of FR-154: the report information produced in
  compatible systems permitting ELECTRONIC TRANSFER to common electronic
  spreadsheets ("por ejemplo, Excel" as printed) — the export is the
  DGA-facing external interface (Odoo produces the transferable file;
  the DGA's consuming systems are external; the file format ships as the
  printed compatibility requirement with no invented DGA-side structure
  — OQ-3).
  (LB-018; EVID-266)
- **SV-SPE-FR-158:** The system shall record the Art. 29
  minimum-delimited-areas duty as an INFORMATIONAL physical-compliance
  catalog (no automation surface): the eight minimum areas as printed —
  a) carga y descarga; b) depósito temporal; c) admisión temporal;
  d) expedición; e) área especial (verificación previa, inmediata y de
  abandono — DGA-authorized, a single physical space permitted with
  delimited sections); f) mercancías retenidas administrativamente;
  g) consolidación de exportaciones (when authorized); h) almacenaje
  simple (when authorized) — as manual compliance states with the
  service-desistimiento route (express communication to the DGA, which
  issues the resolution) recorded as the config link that deactivates
  the corresponding FR-154 i)/j) report rows.
  (LB-019; EVID-266)
- **SV-SPE-FR-159:** The system shall generate the Art. 44 ANNUAL
  consolidated operations+inventory report per usuario directo: the
  OPERACIONES group = annual consolidated information on exports and
  imports of own or third-party goods; the INVENTARIO Y SUS MOVIMIENTOS
  group = annual consolidated goods information in the formulario the
  Dirección determines (config slot — DACG layer, NO shipped structure;
  OQ-3); the remission due AT LATEST 30 días hábiles AFTER THE END OF
  THE YEAR (calendar engine by id), with presented state; the DGA's
  written-request channel recorded: additional information requested in
  writing is deliverable within 15 días hábiles of the request
  (request/delivery event records), and the DGA's reserved power to
  require different/additional documentary information recorded as an
  informational note (zero invented mechanics).
  (LB-020; EVID-266)
- **SV-SPE-FR-160:** The system shall carry the DACG extension clause
  of the register contract as a config-gap surface with NO defaults
  (SOQ-44): the DGA, through disposiciones administrativas de carácter
  general, may establish OTHER consultas y reportes and THE STRUCTURE of
  them (17b_ Art. 28 final), determine the annual-report formulario
  (Art. 44) and require different/additional information — extension
  rows land as dated config (DACG reference + valid_from) upon
  acquisition; nothing beyond the printed minimum ships.
  (LB-018; LB-020; EVID-266; SOQ-44)

### 3.5 LSI sanctions (14_ Arts. 50-52/62)

- **SV-SPE-FR-161:** The system shall classify every recorded LSI breach
  as an infracción record carrying its statutory class from the
  per-article catalogs (Art. 46 set and Art. 48 = MENOS GRAVES;
  Art. 47 set = GRAVES; Art. 49 = GRAVE with reincidencia = MUY GRAVE),
  its basis literal, open/cured state, and per-beneficiary per-class
  reincidencia counters — including the GRAVE-OCCURRENCE counter whose
  third event triggers revocatoria (FR-162) and the muy-grave
  reincidencia counter; the counters consume the breach feeds of
  sibling files (e.g. `03`'s staffing-quota breach → grave, its
  SV-SPE-FR-058 by id) and stamp `01`'s benefit-state transitions
  (SV-SPE-FR-017 by id); NOTHING SMM-priced is computed in the catalogs
  — pricing lives in FR-162 with FR-141's unit.
  (LB-013; LB-014; LB-015; LB-017; EVID-264)
- **SV-SPE-FR-162:** The system shall implement the LSI sanction ladder
  of Art. 52 as sanction-consequence rows keyed by class — MENOS GRAVE:
  written prevención with cure term, reincidencia → multa of 3 SMM "de
  mayor cuantía"; GRAVE: multa of 30 SMM "de mayor cuantía", 40 SMM on
  reincidencia, and upon the THIRD grave occurrence the REVOCATORIA of
  the benefits; MUY GRAVE: temporary suspension of the benefits for
  THREE MONTHS, reincidencia → revocatoria — with every SMM amount
  resolved through FR-141's dated unit (payroll/02 by id, snapshot on
  the record) and the multipliers kept DISTINCT from the ZF 3/5-SMM
  ladder of FR-140 (regime-distinctness invariant; never unified
  config).
  (LB-017; EVID-264)
- **SV-SPE-FR-163:** The system shall implement the LSI
  SS-payment-breach sanction of Art. 50 as a state-stamping consequence
  consuming the SS records by id (payroll/06; the solvency gate
  SV-SPE-FR-102 of `05` by id): firm MTPSS/ISSS/Superintendencia de
  Pensiones resolutions for unpaid patronal cotizaciones or
  un-transferred withheld sums, notified to the Minister of Economy,
  drive the Minister's decision record — temporary suspension of
  benefits for THREE MONTHS, and on reincidencia ATTRIBUTABLE TO THE
  BENEFICIARY the REVOCATORIA — stamping `01`'s benefit state
  (SV-SPE-FR-015/017 by id; the LSI reincidencia consequence is
  revocatoria vs the ZF twin's suspensión definitiva — FR-146, kept
  distinct); the same article's fianza and AML-conviction twins are
  consumed from `03` BY ID (SV-SPE-FR-061/062 — never restated).
  (LB-016; EVID-264)
- **SV-SPE-FR-164:** The system shall implement the Art. 51
  repeated-infringements escalation as a state-stamping consequence:
  where REITERADAS infringements cause omission of payment of duties or
  taxes directly or indirectly, or the unpaid amounts correspond to
  crime-configuration thresholds in the corresponding legislation, the
  customs or tax authority's firm definitive resolution is sent to the
  Minister of Economy, who decides a THREE-MONTH temporary suspension of
  the benefits and — on reincidencia attributable to the beneficiary —
  revocatoria; the Odoo surface records the incoming resolution
  reference, the Minister's decision and the state stamp (`01` by id) —
  **W19 anchor (SOQ-32 consumed):** the "montos… para la configuración
  de delito" threshold = the LESIA Art. 22 US$25,000.00 perjuicio-fiscal
  literal (LB-025; the crime-threshold gate is owned by FR-181 by id) —
  penal procedure mechanics stay authority-side (pointer discipline).
  (LB-016; LB-025; EVID-264/365)

### 3.6 DGA a-posteriori/permanente control backdrop (13_ Art. 19)

- **SV-SPE-FR-165:** The system shall anchor every register and report
  of this file on the 13_ Art. 19 control-classes backdrop as an
  INFORMATIONAL note (no automation surface): under CONTROL A
  POSTERIORI the fiscalization authorities may verify the handling of
  inventories and their valuation and registration methods within the
  caducidad term (the per-DM verification-caducidad tracker consumed
  from `06` by id — SV-SPE-FR-127), and under CONTROL PERMANENTE the
  authority verifies at any moment the permanence, use and destination
  conditions of goods under suspensive or liberatory regimes (the
  regime clocks of `04` by id — SV-SPE-FR-064..081) — the FR-132
  descargo register, the FR-154 LSI register, the FR-136 segregation
  and the FR-139 insumo register are the audit-readiness surfaces this
  frame makes load-bearing.
  (LB-021; EVID-268)

### 3.7 LESIA sanction taxonomy (79_ — W19; SOQ-32 consumed)

- **SV-SPE-FR-179:** The system shall model the LESIA (Ley Especial
  para Sancionar Infracciones Aduaneras) sanction domain as a
  customs-infracción record family DISTINCT from the ZF/LSI
  own-regime sanction ladders of FR-140/162 (parallel families, never
  shared config): every recorded customs infraction carries its
  statutory CLASS per the Art. 3 triad — administrativa (conducts
  unable to cause fiscal damage), tributaria (fiscal damage below the
  crime threshold), penal (statutory crimes — pointer records only) —
  with the INDEPENDENT-SANCTIONING rule encoded: conducts originating
  in the same DM sanction separately, each under its own priced row,
  single administrative act permitted (one procedure, N sanction rows);
  the principles of Art. 1 ride the family as metadata (tipicidad = no
  analogy-imposed sanctions; non bis in idem = one sanction per
  conduct-subject-fundament identity; favorable-retroactivity
  exception), and the record's prescripción, payment and enforcement
  clocks are consumed from `06` FR-177/178 BY ID (never restated).
  (LB-023; LB-028; EVID-359)
- **SV-SPE-FR-180:** The system shall carry the LESIA administrativa
  multa formulas as DATED pricing rows keyed by conduct literal (Art.
  5 conducts, Art. 6 pricing): flat US$50.00 default; 0.5% of the
  patrimonio o capital contable per the signed general balance (minus
  unrealized revaluation surplus) — balance of the infraction's
  economic year (prior year if unclosed), CVCPA-authorized-auditor
  signature, refusal-or-no-balance fallback 3 SMM — with a floor of 1
  SMM, for the c)/d)/e)/f)/m)/n)/o)/p)/y) tier; 3 SMM for the
  i)/j)/ñ) tier (the print also names repealed k) — as-printed note,
  no k)-conduct priced); 6 SMM for literal-a) tránsito breaches with
  +50% on reincidencia and the recidivist's ANNUAL FIANZA (prior-year
  transported-goods value + duties/taxes, 1-year clean-record release)
  as a consequence event; express-courier shipments ≤ US$50.00 FOB
  exempt from these multas; registry-inexactitude adds the
  DGA-system-access suspension state; and the LESIA SMM UNIT resolves
  as its OWN dated lookup — "salario mínimo mensual para el comercio y
  la industria en la ciudad" at the infraction date (Art. 53; dated
  row, snapshot on the sanction) — DISTINCT from the FR-141
  mayor-cuantía unit consumed from payroll/02 (never merged, never
  restated).
  (LB-023; EVID-360)
- **SV-SPE-FR-181:** The system shall carry the LESIA tributaria
  pricing and jurisdiction gates as dated rows: multa = 300% of the
  evaded duties and taxes (200% when perjuicio fiscal < ¢5,000 ≈
  US$571.43 — colones print noted), always ON TOP of the duties owed;
  the TOLERANCE MARGINS gate — granel 5% of total weight; non-granel
  3% of quantity/volume/weight/value (most favorable to the importer),
  conditioned on pre-arrival declaration AND no prior inspection —
  suppresses the sanction but never the collection of duties/taxes on
  the excess, and an excess >3% with unpaid tax ≤ US$100.00 prices at
  100% of that tax; the CRIME-THRESHOLD gate — Art. 8 a)-e) conducts
  with perjuicio fiscal OVER US$25,000.00 (¢218,750.00 twin as
  printed) leave the tributaria class for the Art. 22 defraudación
  crime (penal referral record; pena 4-6 años authority-side — FR-148/
  164 consume this gate by id); the FALTANTES PRESUMPTION —
  unjustified inventory shortfalls found at regime beneficiaries'
  premises legally presume transfer of dominio for the c)/e)/f)/h)
  conducts, consuming the FR-132 descargo pending balances and FR-135
  irregularity registry by id as its evidence surface; and the
  used-vehicle specials (3 SMM per month-or-fraction overstaying;
  100% of the vehicle's duties at the 90-day expiry) as dated literal
  rows.
  (LB-024; LB-025; EVID-361/362/365)
- **SV-SPE-FR-182:** The system shall implement the LESIA consequence
  and modifier set: the EXEMPTION CADUCIDAD consequence for Art. 8
  c)/d) conducts — the exemption lapses and the infractor owes import
  duties at the rates of the franquicia DM's ACCEPTANCE date (dated
  rate-anchor rule on the sanction record); the 3-TRIBUTARIAS-IN-1-YEAR
  suspension — temporary suspension up to SIX MONTHS of the
  authorizations to operate ATPA, zonas francas and tiendas libres
  (and administer zonas francas), with revocatoria on a second
  suspension causal within FIVE years — imposed by MINEC for
  ATPA/ZF (stamping `01`'s benefit state by id; a LESIA-sourced
  consequence family kept DISTINCT from the 12_/14_ Art. 36/52
  ladders of FR-140/162, never merged config) and by the Director
  General for tiendas libres; the SELF-CORRECTION modifier — no
  sanction when the breach is recognized and cured voluntarily BEFORE
  any verification/fiscalization/advance-ruling-revocation initiates
  (event-state guard on the record); and the 50% ATTENUATION for
  written acceptance of charges during the 15-day hearing (per the
  FR-183 procedure), barred on six-month reincidencia.
  (LB-026; EVID-363)
- **SV-SPE-FR-183:** The system shall record the LESIA sanctioning
  procedure states on the infracción family, consuming `06`'s FR-128
  chassis BY ID (Art. 31 LESIA explicitly rides the 74_ Art. 17
  procedure — 15-días-hábiles hearing-and-proof term, 20-días-hábiles
  resolution and notification; never restated here): the aperture with
  the FULL hoja de discrepancias/informe content; the EXPRESS WRITTEN
  ACCEPTANCE fast track (resolution immediately after acceptance —
  pricing per FR-182's attenuation); the GARANTÍA-RELEASE of contested
  goods at any time (bond = unperceived duties + applicable multa) as
  a release-reference field; the Art. 32 due-process rights as record
  metadata; the Art. 36 plena-prueba rule (sealed information request
  or technician's act/informe = full proof for the document-custody
  and control literals) with the 10-días-hábiles request-response
  clock; and the Art. 33 prescripción tracker + Art. 37/38
  payment-enforcement states consumed from `06` FR-177/178 by id
  (firmeza payment clock, moratory interest, new-despacho suspension
  with the recurso-pendiente carve-out per the FR-128 recourse
  metadata).
  (LB-028; EVID-368/369/370)
- **SV-SPE-FR-184:** The system shall carry the LESIA
  auxiliares-enforcement ladder for the customs-auxiliary profiles of
  the declarante-role config (`01` SV-SPE-FR-020 by id — agentes de
  aduana, despachantes/apoderados especiales aduaneros, transportistas
  and agentes de transporte, depositarios, administradores de zonas
  francas per the Art. 54 definition): an authorization state (active ·
  suspended ≤90d · cancelled) with its cause catalog per Arts. 29/30 —
  suspension causes incl. the declarant-document safe harbor for
  inexact declarations, the ¢100,000-colones suspensive-inexactitude
  threshold (as printed), firm-unpaid-obligation and un-renewed-fianza
  causes (suspension while the cause subsists), and the
  agente/despachante >2-tributarias-in-6-months cause, with the
  suspended auxiliary only concluding initiated operations;
  cancelación causes incl. consigning an un-engaged person's
  name/domicilio/NIT/NRC and DELEGATING the electronic-declaration
  transmission by revealing the access key or electronic signature
  (the penal twin of `06`'s FR-115 confidentiality flags); plus the
  Art. 54 DGA sanctions-registry reference as authority-side mirrored
  metadata (never emulated).
  (LB-027; EVID-366/367)

## 4. Data Model

Layer semantics: the obligations/reporting/sanction surfaces are
Odoo-native records and dated config rows under the
`l10n_sv_special_regime.*` namespace (segregation rides stock locations/
lots); every FR maps `odoo` (see §5). **W19 namespace note:** the LESIA
sanction family of §3.7 lives under `l10n_sv_customs.*` — customs
sanctions attach to declarations/declarants (the `06` namespace), not to
regime beneficiaries; this file owns their specification, `06`'s
FR-177/178 own the shared declaration-side clocks. The DGA/MINEC/MH are
external
authorities: the model produces registers, reports and exports at their
disposal and records authority-issued facts (notifications, resolutions,
deregistrations) — it does not emulate their systems. No printed data
table in this file warrants a CSV sidecar (the obligation letters,
report specs and sanction classes are small config sets; the SMM values
live in payroll/02's sidecar — consumed by id, never duplicated; default
none per plan).

**Obligation catalogs (l10n_sv_special_regime.obligation):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.obligation | regime_scope · basis_literal | select · char | zf_art28 (a-s) · lsi_art46 (a-f) · lsi_art47 (a-e,g-j) · lsi_art48 · lsi_art49 | FR-130, FR-149, FR-151, FR-152, FR-153 |
| l10n_sv_special_regime.obligation | tier | select | zf: leve (a,c,f,g,h,i,q) · grave (b,d,e,j,k,l,m,n,o,p,s) · muy_grave (r); lsi: menos_grave (46, 48) · grave (47, 49) · muy_grave (49 reincidencia) | FR-130, FR-161 |
| l10n_sv_special_regime.obligation | compliance_state · evidence_ref | select · char | met · pending · breached; notice/resolution references | FR-130, FR-149..153 |
| l10n_sv_special_regime.obligation | retention_flag | boolean + int | 5-year manifiesto copies (46 c) / contractual docs (48 d) — customs-5y floor kin (LB-022); canonical matrix commercial-legal/02 by id | FR-149, FR-152 |
| l10n_sv_special_regime.obligation | valid_from · valid_to · provenance | date · date · char | instrument = 12_/14_ article as printed (SOQ-30); dated rows per D15 | FR-130..153 |

**ZF/DPA registers (l10n_sv_special_regime.\*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.descargo_register | duca_id · fiscal_year | m2o l10n_sv_customs.duca · year | per-import ledger; acceptance anchor = `06` FR-104 by id | FR-132 |
| l10n_sv_special_regime.descargo_register | saldo · descargo_events · pending_balance | monetary · o2m · computed (monetary) | entries/exits/saldos; dispositions per `04`/`05` by id; cuadro demostrativo per DM | FR-132 |
| l10n_sv_special_regime.descargo_register | mode · remittance_due · remittance_state | select · date · select | online · fallback_media; 20 días hábiles post-fiscal-year (engine by id); pending · presented; on-request events | FR-132 |
| l10n_sv_special_regime.minec_informe | semester · groups (5) | period · computed assemblies | importaciones valor/origen; exportaciones valor/destino; empleo (payroll by id); ventas nacionales (`05` by id); inversión (`01` FR-010 log by id) | FR-133 |
| l10n_sv_special_regime.goods_irregularity | kind · causa_fortuita_flag · liability_state | select · boolean · select | dañada · perdida · destruida · otra; fuerza mayor proven-to-DGA; fisco_liability on/off (j) | FR-135 |
| l10n_sv_special_regime.insumo_register | lot · insumo_qty · compensador_qty · yield · merma | m2o lot · qty · qty · computed · computed | pormenorized insumo-vs-producto-compensador tracing; reconciliation vs import saldos | FR-139 |
| stock.location / stock.lot | segregation_zone · component_origin | select · select | suspensivo · nacionalizado; identification in the producto compensado (trazabilidad of destination) | FR-136 |
| product.template | sv_spe_cost_record_link | o2m | cost records for TAN-sold goods (authorization + tributes-paid flags; components from `05` by id) | FR-137 |

**Sanction family (l10n_sv_special_regime.sanction + kin):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.sanction | regime · class · basis_literal | select · select · char | zf: leve/grave/muy_grave (28 final); lsi: menos_grave/grave/muy_grave (46-49) | FR-140, FR-142, FR-161, FR-162 |
| l10n_sv_special_regime.sanction | smm_multiplier · smm_row_ref · smm_value_snapshot | int · m2o payroll sidecar row · monetary | ZF 3/5; LSI 3/30/40; unit resolved as-of sanction date from payroll/02 by id (SV-PAY-FR-022 + sidecar), snapshot-on-write (D15) | FR-140, FR-141, FR-162 |
| l10n_sv_special_regime.sanction | consequence | select | prevención · multa · suspension_3m · suspension_definitiva (ZF) · revocatoria (LSI) · category_loss (39) · access_suspension (36-A) | FR-140, FR-146, FR-147, FR-162, FR-163 |
| l10n_sv_special_regime.sanction | payment_due · payment_state · payment_ref | date · select · char | Art. 37: 30 calendar days from notification; Tesorería route | FR-144 |
| l10n_sv_special_regime.sanction | reincidencia_counter_ref · state_stamp | m2o counter · select+char | per-class counters (FR-142/161); benefit-state stamp via `01` FR-015/016/017/018 by id with reason code | FR-142, FR-146, FR-147, FR-161..164 |
| l10n_sv_special_regime.regularization_notice | detected_on · notified_on · due_on (30 días calendario) · cured_on · access_suspended | date · date · date · date · boolean | Art. 36-A; stamps the DGA-access field (`01` FR-018 by id); rehabilitation only upon cure | FR-143 |
| l10n_sv_special_regime.fianza_event | cause_class · amount_slot | select · monetary slot | zf_repeated_customs_tax · zf_penal_sentence (37-A); lsi twins = `03` FR-061 by id; NO default amount | FR-145 |
| l10n_sv_special_regime.closure_checklist | open_dm_ids · cancellation_state · unpaid_duties_state · lesia_pointer | o2m · select · select · flag | Art. 40-A; DMs from `04`/`06` by id; defraudación crime = ANCHORED pointer (Art. 22 elements per LB-025/EVID-365 — $25,000 threshold + false-docs branch; penal mechanics authority-side) | FR-148 |

**LSI register contract (l10n_sv_special_regime.lsi_register_\*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.lsi_register_report | spec | select | a diario_ingresos_egresos · b saldo · c declaraciones_cancelaciones_destinaciones · d declaraciones_con_saldos · e abandono_detalle · f deposito_temporal · g admision_temporal · h retenidas_administrativas · i acopio_exportacion (auth-gated) · j almacenaje_simple_contribuyente (auth-gated) | FR-154 |
| l10n_sv_special_regime.lsi_register_report | query_facets | m2m/multi | declaración (DUCA) · régimen · destinación · contribuyente | FR-155 |
| l10n_sv_special_regime.lsi_register_item | nombre_comercial · código · sac6 · ingreso_doc_no | char · char · char(6) REQUIRED · char | SAC-6 mandatory on every item (no line without it); code family shared with `06` FR-108 by id | FR-156 |
| l10n_sv_special_regime.lsi_register_report | export_format | char | Excel-transferable electronic export (printed compatibility; DGA-side structure = DACG, no default) | FR-157, FR-160 |
| l10n_sv_special_regime.annual_ops_report | year · operaciones_group · inventario_group · due_on · presented | year · computed · config slot · date (30 días hábiles post-year; engine by id) · select | formulario de la Dirección = DACG config slot (SOQ-44); written-request items deliverable ≤15 días hábiles | FR-159 |
| l10n_sv_special_regime.dacg_extension | reference · valid_from · scope | char · date · select | Art. 28 final / Art. 44 extension rows — dated config on acquisition, NO shipped defaults | FR-160 |

**LESIA sanction family (l10n_sv_customs.lesia_* — W19; specification owned here, namespace shared with `06`):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_customs.lesia_infraccion | class · conduct_literal · duca_id | select · char · m2o l10n_sv_customs.duca | administrativa · tributaria · penal (Art. 3 triad; penal = pointer record); independent sanctioning per DM (N rows per declaration); principles metadata (tipicidad / non bis in idem) | FR-179 |
| l10n_sv_customs.lesia_infraccion | multa_basis · amount · smm_unit_snapshot | select · monetary · monetary | usd_50_flat · pct_05_patrimonio (floor 1 SMM; auditor-signed balance, refusal-fallback 3 SMM) · smm_3 (i/j/ñ tier) · smm_6_transit (+50% reincidencia; fianza event) · pct_300_evaded · pct_200_evaded_minor · pct_100_excess_le_100 · vehicle specials — LESIA SMM unit = comercio-y-industria city row at infraction date (Art. 53; DISTINCT from FR-141 mayor-cuantía), snapshot-on-write | FR-180, FR-181 |
| l10n_sv_customs.lesia_infraccion | tolerance_margin_state · crime_threshold_state | computed · computed | granel 5% weight / non-granel 3% (pre-declared + no-prior-inspection flags; duty collection on excess never suppressed); perjuicio > US$25,000 ⇒ Art. 22 penal referral (¢218,750 twin as printed) | FR-181 |
| l10n_sv_customs.lesia_infraccion | faltantes_presumption_ref · exemption_caducidad | m2o descargo/irregularity · boolean + rate_anchor_date | unjustified shortfalls presume transfer of dominio (c/e/f/h conducts; evidence = FR-132/135 by id); caducidad prices duties at franquicia-DM acceptance-date rates | FR-181, FR-182 |
| l10n_sv_customs.lesia_infraccion | self_correction_state · attenuation_50 · acceptance_fasttrack | select · boolean · boolean | cured-before-verification = no sanction; written acceptance in the 15-day hearing = 50% (barred on 6-month reincidencia); immediate resolution on acceptance | FR-182, FR-183 |
| l10n_sv_customs.lesia_infraccion | procedure_state · garantia_release_ref · plena_prueba_ref · request_response_due | select · char · char · date | FR-128 chassis by id (apertura/audiencia/resolution); bond = unperceived duties + multa; Art. 36 plena prueba; 10 días hábiles to answer DGA requests; prescripción/payment/despacho-suspension = `06` FR-177/178 by id | FR-183 |
| l10n_sv_customs.lesia_auxiliar | profile · authorization_state · cause · cause_ref | m2o declarante-role config (`01` FR-020) · select · select · char | active · suspended_90d · cancelled; Art. 29 a)-h) suspension causes (safe-harbor, ¢100,000 colones print, subsisting-cause semantics) / Art. 30 a)-f) cancelación causes (incl. key-revelation delegation); Art. 54 sanctions-registry reference mirrored | FR-184 |

## 5. Odoo Mapping

Layer semantics for this wave: the obligations/reporting/sanction
surfaces are Odoo-native (config rows + stock/lot tracing + report
exports under `l10n_sv_special_regime.*`) — every FR maps `odoo`; the
DGA/MINEC-facing outputs (descargo register, MINEC informe, LSI register
reports, annual ops report) are Odoo-produced EXPORTS whose consuming
authority systems are external interfaces (assumption notes in the rows
below; no SaaS rows — none of these FRs touch DTE generation/transmission,
an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is required
by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-130 | odoo | l10n_sv_special_regime.obligation | regime_scope/basis_literal/tier/compliance_state | Art. 28 a)-s) catalog; tiers per 28 final; k)/o) = sibling-owned, catalogued only; physical duties = manual states |
| FR-131 | odoo | l10n_sv_special_regime.obligation (notice event) | due_on (10 días hábiles; SV-FREP-FR-202..204 by id) | administrador vs MINEC addressee split per print |
| FR-132 | odoo | l10n_sv_special_regime.descargo_register | duca_id/saldo/pending_balance/remittance | per-DM cuadro; anchors `06` FR-104 + `04` clocks by id; fallback 20 días hábiles; external-interface export note |
| FR-133 | odoo | l10n_sv_special_regime.minec_informe | semester/5 groups | groups from ledgers by id (06/payroll/05/01); format = Reglamento/DACG slot (OQ-4) |
| FR-134 | odoo | l10n_sv_special_regime.obligation (notice event) | due 30 calendar days in advance | links FR-148 closure checklist |
| FR-135 | odoo | l10n_sv_special_regime.goods_irregularity | kind/causa_fortuita/liability_state | linked to FR-132 pending balances; j)-liability payment = `05` by id |
| FR-136 | odoo | stock.location + stock.lot | segregation_zone/component_origin | suspensivo vs nacionalizado; trazabilidad into producto compensado |
| FR-137 | odoo | product.template (+ o2m cost records) | cost components + auth/tributes-paid flags | components from `05` internación surfaces by id |
| FR-138 | odoo | l10n_sv_special_regime.descargo_register (report view) | pending-cancellation view | 20 días hábiles; may consolidate into the b) remittance event |
| FR-139 | odoo | l10n_sv_special_regime.insumo_register | lot/insumo_qty/compensador_qty/yield/merma | reconciliation vs import saldos; exhibitable per investigation ref |
| FR-140 | odoo | l10n_sv_special_regime.sanction | class/consequence | ZF 3/5 SMM + muy-grave ≤3m/definitive; stamps `01` FR-015/016 by id; DISTINCT from LSI FR-162 |
| FR-141 | odoo | l10n_sv_special_regime.sanction (SMM unit resolver) | smm_row_ref/smm_value_snapshot | payroll/02 by id (SV-PAY-FR-022 + sidecar); highest-sector default = labeled assumption (SOQ-33/OQ-1); snapshot-on-write D15 |
| FR-142 | odoo | l10n_sv_special_regime.sanction (+ counters) | class/basis/reincidencia counters | tiers from 28 final; Art. 37-A fianza flag (no default amount); procedure = `01` FR-019 by id |
| FR-143 | odoo | l10n_sv_special_regime.regularization_notice | notified_on/due_on (30 días CALENDARIO)/access_suspended | stamps DGA-access field (`01` FR-018 by id); calendar arithmetic as printed |
| FR-144 | odoo | l10n_sv_special_regime.sanction | payment_due/payment_state | Art. 37: 30 calendar days; Tesorería route metadata |
| FR-145 | odoo | l10n_sv_special_regime.fianza_event | cause_class/amount_slot | ZF Art. 37-A; LSI twin = `03` FR-061 by id; NO default amount |
| FR-146 | odoo | l10n_sv_special_regime.sanction (SS-breach consequence) | consequence/reason art31_ss_breach | consumes payroll/06 + `05` FR-102 by id; 3-month suspension / reincidencia definitiva (ZF) |
| FR-147 | odoo | l10n_sv_special_regime.sanction (inactivity consequence) | state_stamp perdida_inactividad / revocada + baja/access-disablement record | consumes `01` FR-018 monitors by id; 13th-month ZF / 3rd-month LSI semantics live there |
| FR-148 | odoo | l10n_sv_special_regime.closure_checklist | open_dm_ids/cancellation_state/lesia_pointer | DMs from `04`/`06` by id; W19: defraudación = ANCHORED pointer (Art. 22 elements — $25,000 + false-docs branch, LB-025; penal mechanics authority-side); Art. 40 judicial = informational |
| FR-149 | odoo | l10n_sv_special_regime.obligation (LSI Art. 46 set) | tier menos_grave | 8-day notice = calendar as printed; 5y manifiesto retention flag (LB-022 kin; matrix by id) |
| FR-150 | odoo | l10n_sv_special_regime.obligation (Art. 47 a record) | annual remittance + systems-audit flags | feeds FR-154..157/159 by id; external-interface export note |
| FR-151 | odoo | l10n_sv_special_regime.obligation (Art. 47 b-j set) | tier grave | f)/k) = `03` FR-051..055/058 by id, never restated |
| FR-152 | odoo | l10n_sv_special_regime.obligation (Art. 48 set) | tier menos_grave (admin) | 5y contractual-docs retention; irregularities info duty |
| FR-153 | odoo | l10n_sv_special_regime.obligation (Art. 49 marchamo gates) | entry/exit events + marchamo verification | grave; reincidencia muy grave (counter feeds FR-161) |
| FR-154 | odoo | l10n_sv_special_regime.lsi_register_report | spec a)-j) | 10 mandatory reportes verbatim; i)/j) auth-gated (17b_ Art. 30 flag); consumed by `03` FR-053 e.5 by id |
| FR-155 | odoo | l10n_sv_special_regime.lsi_register_report | query_facets | por declaración/régimen/destinación/contribuyente |
| FR-156 | odoo | l10n_sv_special_regime.lsi_register_item | sac6 REQUIRED + nombre/código/ingreso_doc_no | SAC-6 mandatory; code family shared with `06` FR-108 by id |
| FR-157 | odoo | l10n_sv_special_regime.lsi_register_report (export) | Excel-transferable export | external-interface note; no invented DGA-side structure (OQ-3) |
| FR-158 | odoo | l10n_sv_special_regime.obligation (Art. 29 informational) | 8 minimum-areas manual states | desistimiento route deactivates i)/j) rows; physical — informational |
| FR-159 | odoo | l10n_sv_special_regime.annual_ops_report | year/due_on (30 días hábiles; engine by id)/presented | formulario = DACG slot (OQ-3); written-request ≤15 días hábiles events |
| FR-160 | odoo | l10n_sv_special_regime.dacg_extension | reference/valid_from/scope | SOQ-44: dated rows on acquisition, NO shipped defaults |
| FR-161 | odoo | l10n_sv_special_regime.sanction (LSI classifiers/counters) | class/grave-occurrence counter | classes from 46/47/48/49; feeds FR-162; state stamps via `01` FR-017 by id |
| FR-162 | odoo | l10n_sv_special_regime.sanction | smm_multiplier 3/30/40 + consequences | LSI ladder; unit via FR-141 (payroll/02 by id); DISTINCT from ZF FR-140 |
| FR-163 | odoo | l10n_sv_special_regime.sanction (SS-breach consequence) | consequence/reason (revocatoria on reincidencia) | consumes payroll/06 + `05` FR-102 by id; fianza/AML twins = `03` FR-061/062 by id |
| FR-164 | odoo | l10n_sv_special_regime.sanction (Art. 51 escalation) | resolution ref/decision/state stamp | W19: crime thresholds = LESIA Art. 22 US$25,000 anchored (LB-025; gate owned by FR-181 by id); penal procedure = pointer discipline |
| FR-165 | odoo | (informational) | — | 13_ Art. 19 backdrop anchoring FR-132/136/139/154 as audit-readiness surfaces; caducidad view = `06` FR-127 by id |
| FR-179 | odoo | l10n_sv_customs.lesia_infraccion | class/conduct_literal/duca_id + principles metadata | Art. 3 triad; independent sanctioning per DM; DISTINCT from ZF/LSI FR-140/162 families; clocks consumed from `06` FR-177/178 by id |
| FR-180 | odoo | l10n_sv_customs.lesia_infraccion (pricing rows) | multa_basis/amount/smm_unit_snapshot | $50 flat / 0.5% patrimonio floor 1 SMM / 3 SMM / 6 SMM +50% + fianza; courier ≤$50 FOB carve-out; LESIA SMM unit = Art. 53 comercio-y-industria dated lookup (DISTINCT from FR-141) |
| FR-181 | odoo | l10n_sv_customs.lesia_infraccion (gates) | tolerance_margin_state/crime_threshold_state/faltantes_presumption | 5%/3% margins (pre-declared + no-prior-inspection); >$100→100% rule; US$25,000 Art. 22 split (consumed by FR-148/164); faltantes presume transfer (FR-132/135 evidence by id); vehicle specials |
| FR-182 | odoo | l10n_sv_customs.lesia_infraccion (consequences/modifiers) | exemption_caducidad/3-in-1y suspension/self_correction/attenuation | caducidad at franquicia-DM acceptance rates; ≤6-month suspension + 5-year-window revocatoria (MINEC for ATPA/ZF; stamps `01` by id; DISTINCT from FR-140/162); cured-before-verification = no sanction; 50% written acceptance |
| FR-183 | odoo | l10n_sv_customs.lesia_infraccion (procedure) | procedure_state/garantia_release/plena_prueba/request_response_due | FR-128 chassis by id (LESIA Art. 31 rides 74_ Art. 17); acceptance fast track; garantía-release = duties + multa; 10-días request clock; prescripción/payment/suspension = `06` FR-177/178 by id |
| FR-184 | odoo | l10n_sv_customs.lesia_auxiliar | authorization_state/cause/cause_ref | ≤90d suspension (a-h causes; safe harbor; subsisting-cause semantics) / cancelación (a-f; key-revelation); administradores ZF inside Art. 54 definition; declarante-role config `01` FR-020 by id |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file (the 10/20/30-días-hábiles clocks, the 30-day calendar notices, the
30-días-calendario regularization window, the 8-day notice, the 30-day
multa payment window, the 5-year retention flags, the 3/5 vs 3/30/40 SMM
multipliers, the ≤3-month suspension ceilings; W19 LESIA additions: the
US$50/0.5%/3-SMM/6-SMM administrativa multas, the 300%/200%/100%
tributaria percentages, the 5%/3% tolerance margins, the US$25,000 crime
threshold with its colones twins, the 90-day auxiliar suspension ceiling
and the 15/20/10-días-hábiles procedure/recourse clocks riding `06`'s
engine) are code-text values cited
as printed under the SOQ-30 verification watch (§2) and live as dated
config rows with instrument provenance — never constants; the SMM unit
resolves as-of the sanction date against payroll/02's dated sidecar and
snapshots on the record (D15) — EXCEPT the LESIA SMM unit, which
resolves as-of the infraction date against the Art. 53
comercio-y-industria lookup (its own dated row, same snapshot
discipline). Mid-year go-live (D18): a migrating
regime company's obligation compliance states, sanction history and
register balances ingest as `is_historical` rows with original-period
semantics (tiered ingestion per D18; no re-derivation of past sanctions
or remittance states). No hard gates beyond the statutory state machine
(D16 no-override: benefit states and access suspensions are never
overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a ZF usuario's import under a DM acceptance with
  regime saldo, when a descargo event (export/traslado/internación) is
  recorded against it, then the FR-132 register updates the per-DM
  pending balance and the cuadro demostrativo de descargo demonstrates
  the cancellation — and at fiscal-year end the fallback remittance
  event carries the 20-días-hábiles due stamp (calendar engine by id).
- **AC-002:** Given a ZF/DPA beneficiary closing its first semester,
  when the semestral MINEC informe is generated, then it assembles the
  FIVE data groups from their ledgers of record (imports value/origin
  and exports value/destination from DUCA records by id; employment
  from payroll by id; national-market sales from `05`'s surfaces by id;
  investment from `01`'s requisito log by id) with no hand-keyed group.
- **AC-003:** Given a grave ZF infringement recorded against a
  beneficiary, when the sanction is priced, then the multa computes as
  5 × the SMM "de mayor cuantía" row resolved as-of the sanction date
  from payroll/02 by id (current-vintage example: 5 × the dated
  highest-sector monthly row) with the sidecar row reference and value
  snapshotted on the sanction record (D15) — never a hardcoded amount.
- **AC-004:** Given a ZF beneficiary with a firm ISSS resolution for
  unpaid patronal cotizaciones notified to MINEC, when the Art. 31
  consequence is recorded, then the benefit state suspends for three
  months with tributes payable during the suspension and the exemption
  ladder clock continuing to accumulate (`01` FR-016 invariants by id)
  — while the LSI twin with attributable recidivism stamps revocatoria
  (FR-163), the two consequences never sharing config.
- **AC-005:** Given a ZF beneficiary whose last regime import/export
  occurred 12 continuous months ago, when the 13th month completes,
  then the inactivity sanction consequence stamps the
  perdida_inactividad state with the DGA system deregistration (dar de
  baja) recorded (consumed from `01`'s FR-018 monitor by id).
- **AC-006:** Given an LSI beneficiary with one recorded grave
  infringement, when a second grave is recorded, then the multa prices
  at 40 SMM "de mayor cuantía" (dated unit via FR-141) — and when a
  THIRD grave occurs, the revocatoria consequence stamps the benefit
  state via `01`'s FR-017 by id.
- **AC-007:** Given an MH notification of grave Art. 28 infringements
  with the printed warning, when the 30-días-calendario window lapses
  without cure, then the customs system-access suspension state stamps
  (the `01` profile access field by id) and remains stamped until a
  regularization event records the cure, at which point rehabilitation
  is stamped.
- **AC-008:** Given an LSI distributor's register with movements under
  two declarations and three contribuyentes, when the a)-report (daily
  ingresos/egresos) is queried by declaración and contribuyente, then
  it returns only the matching items, each showing nombre comercial,
  código, SAC 6-digit classification and ingreso-document number — and
  the export produces a spreadsheet-transferable file (e.g., Excel).
- **AC-009:** Given a production lot consuming imported insumos, when
  the compensating product is output, then the FR-139 register traces
  the lot's insumo quantities against the producto compensador with
  the implied yield and merma recorded, and the FR-136 control
  identifies the suspensive vs nationalized components in the
  compensated product.
- **AC-010:** Given a ZF usuario recording its definitive closure, when
  the closure checklist runs, then every open DM under the regime lists
  with its cancellation/descargo demonstration state and the
  duties-payment state for undischarged goods — and the defraudación
  crime consequence appears as an ANCHORED pointer flag carrying the
  Art. 22 elements (perjuicio fiscal over US$25,000, or false/alterated
  accompanying documents regardless of amount — LB-025/EVID-365), with
  penal procedure and pena execution authority-side.
- **AC-011:** Given goods damaged inside an LSI parque, when the
  irregularity is recorded, then the 8-day notice event carries its due
  date counted from the occurrence (calendar days as printed) for the
  usuario-directo row and the administrador information duty of
  FR-152.
- **AC-012:** Given an LSI usuario directo at fiscal year end, when
  the annual consolidated report is generated, then the operaciones and
  inventory groups assemble with the 30-días-hábiles due stamp — and a
  later DGA written request for additional information opens a delivery
  event due within 15 días hábiles.
- **AC-013:** Given a US$40,000 perjuicio-fiscal understatement on a
  definitive import DM (Art. 8 a) conduct, non-granel, declared
  pre-arrival without prior inspection, when the excess measures 6% of
  value, then the tolerance gate stays closed (margin 3%), the multa
  prices at 300% of the evaded duties and the crime-threshold gate
  opens the Art. 22 penal referral (perjuicio > US$25,000) — while its
  US$18,000 twin prices identically but stays tributaria (FR-181).
- **AC-014:** Given a ZF beneficiary recording a third LESIA
  tributaria infraction within a 12-month span, when the third
  resolution firms, then the Art. 13 consequence opens the ≤6-month
  suspension record addressed to MINEC (stamping `01`'s benefit state
  by id) — and a second suspension causal within the following five
  years escalates to the revocatoria consequence, all as a
  LESIA-sourced family distinct from the Art. 36/52 ladder rows of
  FR-140/162 (never shared config) (FR-182).
- **AC-015:** Given an agente de aduanas with three tributaria
  infractions recorded in a six-month window, when the FR-184 ladder
  evaluates, then the authorization stamps suspended_90d with the
  >2-infringements cause and only already-initiated operations may
  conclude — while revelation of the transmission key to an unauthorized
  third party would stamp cancelled (Art. 30 f) with the penal-twin
  note), mirroring `06`'s FR-115 confidentiality flags (FR-184).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-33 carried: "salarios mínimos mensuales de mayor cuantía" (12_ Art. 36; 14_ Art. 52) is undefined in the corpus — FR-141 ships the working assumption as a LABELED config default: the HIGHEST monthly sector row of the operative 16_ vintage consumed from payroll/02 by id (SV-PAY-FR-022 + the dated sidecar); at the current vintage industria and comercio y servicios TIE at the same printed monthly value, so the default's sector choice (comercio y servicios) is itself part of the assumption. The ZF 3/5 and LSI 3/30/40 multipliers stay distinct config regardless. Confirm the reading (and any administering practice fixing the sector) before implementation. | no | Takumi S7 (config watch) | open |
| OQ-2 | SOQ-32 carried: the Ley Especial para Sancionar Infracciones Aduaneras (LESIA) was NOT in the corpus though cited by 12_ Art. 40-A (Art. 22 — the defraudación de la renta de aduanas crime for closure-with-open-DMs) and by the crime-configuration thresholds of 14_ Art. 51 — **CONSUMED W19 (2026-08-22): LESIA acquired as 79_ (D.L. 551, INDICE print through D.L. 588-2008); FR-148/FR-164 pointers ANCHORED (Art. 22 elements — LB-025) and the gated sanction inventory extended as FR-179..184 (class taxonomy, multa formulas, tolerance margins, crime split, consequences, auxiliares ladder, procedure); the declaration-side clocks live in `06` FR-177/178**; residual = the 79_ print's own post-2008 vintage watch (OQ-6). | no | Takumi S7 (sources watch) | consumed (W19; EVID-359..370) |
| OQ-3 | SOQ-44 carried: the DGA's living administrative layer (disposiciones administrativas de carácter general) may extend the 17b_ Art. 28 consultas/reportes and their STRUCTURE, determine the Art. 44 annual-report formulario, and require different/additional documentary information — FR-160 ships the extension surface as dated config slots with NO defaults; the descargo-register media/normativa (12_ Art. 28 b) and the MINEC informe format are the same DACG/Reglamento family (kin of SOQ-31, OQ-4). Re-verify every export contract at implementation. | no | Takumi S7 (DACG watch) | open |
| OQ-4 | SOQ-31 kin: the Reglamento General de la Ley de Zonas Francas (12_ Art. 51 mandates it) is NOT in the corpus — the semestral MINEC informe format, the descargo cuadro structure and the MINEC dependency designations are delegated there; FR-133/FR-134 expose the printed clocks and data groups with the formats as config slots, NO defaults. Acquisition candidate ≥75. | no | Takumi S7 (sources watch) | open |
| OQ-5 | SOQ-30 carried: the 12_ consolidation ends at D.L. 318-2013, 14_/17b_ are the 2007/2008 prints, and 13_/74_ end at D.L. 121-2012/D.L. 23-2012 — post-cutoff reforms unverified until official routes recover; every LB in this file cites as printed; a post-cutoff reform may move obligation letters, sanction multipliers, the 30-días-calendario window, the report specs or the inactivity thresholds — re-verify before implementation. **W19 addition: 79_ ends at D.L. 588-2008 (see OQ-6).** | no | Takumi S7 (sources watch) | open |
| OQ-6 | 79_ LESIA (LB-023..028) is the INDICE LEGISLATIVO print consolidated through reform (5) D.L. 588-2008 — post-2008 LESIA reforms unverified until official routes recover (SOQ-30 kin; same watch family as OQ-5); FR-179..184 values (multa tiers, tolerance margins, thresholds, clocks) cite as printed; re-verify before implementation (kin of `06`'s OQ-7). | no | Takumi S7 (sources watch) | open |
| OQ-7 | Colones-era prints inside 79_ (as-printed discipline, operative currency USD at the 8.75 peg): Art. 9 "¢218,750.00 O SU EQUIVALENTE EN DÓLARES" (= the Art. 22 US$25,000.00); Art. 10 "cinco mil colones" (≈ US$571.43 — the 200%-multa boundary); Art. 29 e) "cien mil colones" (≈ US$11,428.57 — the suspensive-inexactitude suspension threshold) — FR-181/184 encode the USD figures with the colones prints noted; confirm the peg reading at implementation. | no | Takumi S7 (config watch) | open |
| OQ-8 | 79_ Art. 6 as-printed inconsistency: the 3-SMM tier enumerates "i), j), k), Y ñ)" though literal k) is DEROGADO (2) — FR-180 transcribes verbatim and prices no k)-conduct (an as-printed note, not an interpretation). | no | Takumi S7 (config watch) | open |
