# SV — Taxation — IVA framework: hechos generadores, sujetos pasivos and the excluidos regime (Ley IVA Arts. 1-32)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the core of El Salvador's
*Impuesto a la Transferencia de Bienes Muebles y a la Prestación de
Servicios* (transfer-of-movable-goods-and-services tax, "IVA", D.L.
296-1992) — the operation model and its facts: the Art. 1 scope and Art. 2
coexistence with other taxes; the Art. 5 vocabulary (*bienes muebles
corporales* as tangibles transportable by themselves or by external force;
*títulos valores* (securities) as *bienes muebles incorpóreos* save the
Art. 7-d) carve-out; the rule that *mutuos dinerarios, créditos en dinero o
cualquier forma de financiamiento* (money loans, money credit or any form of
financing) are PRESTACIÓN DE SERVICIOS); the Art. 6-7 *transferencia de
dominio a título oneroso* concept with its full a)-m) *enunciación*
(enumeration — public auctions and adjudications in payment, permutas,
daciones en pago, cession of ownership titles, mutuos of fungible things,
aportes of giro goods to societies f), reorganization transfers g), the
liquidation carve-out h) — no gravamen when the adjudicatario is the same
socio who aportó the good and the good was not IVA-charged —,
establishment transfers limited to the *activo realizable* i), usufruct and
exploitation rights j), sale-promise-followed-by-possession k), the
catch-all free-economic-disposition delivery l), and goods acquired in
payment of debts m)); the Art. 8 tax point (document emission first, earlier
payment or real/symbolical delivery, the consignment trigger at the
consignatario's acts, and causation despite price omission, mora or
non-final pricing); the Art. 9 exchange/return path (not a new transfer —
the Art. 62-1-a deduction, absent proven new-contract intent); Art. 10 goods
territoriality (*situados, matriculados o registrados en el país*, goods
shipped from El Salvador to non-contribuyente acquirers deemed situados in
SV); the Arts. 11-13 *retiro* (withdrawal/self-supply of goods — own,
socios', directivos' or personnel's use or consumption, extended by
Reglamento Art. 4 to *grupo familiar* (immediate family) and *terceros*
(third parties); raffles, sweepstakes and free promotional, propaganda or
publicity distribution *sean o no del giro* (whether or not in the business
line); the inventory-shortfall presumption with its Reglamento Art. 4 *caso
fortuito o fuerza mayor* (act-of-God/force majeure) evidence menu and
accounting-date precondition; the realizable→fixed-asset non-retiro for
giro-necessary goods and the ISR-Art.-6-c donation carve-out; caused on the
retiro date); the Arts. 14-15 import/internación of goods AND services
(aduana auctions as import acts; the services-import test as interpreted by
D.L. 645-2005 — utilization *de manera exclusiva* in El Salvador; goods
caused at the import moment, services at the earliest of prestador document,
payment or término; the special-customs-regimes devengo at free
disposability upon definitive conversion — SR4 consumer); the Arts. 16-17
services *hecho generador* (onerous prestations against *renta, honorario,
comisión, interés, prima, regalía* or any remuneration; autoconsumo;
indemnizations and qualified gratuitous irrevocable donations out); the full
Art. 17 a)-q) service catalog and the *reintegros o reembolsos de gastos*
(expense reimbursements) assimilation — taxed at payment, with the
seguros/alimentación/viáticos-laborales and Art. 51-a
mandate-no-credit-deduced exception gates; the Art. 18 service tax points
(earliest of document, término, leased-good delivery, good/obra delivery, or
payment/credit *aunque sea con anticipación* — even in advance;
permanent/periodic services at document or period-end; leasing with purchase
option at cánones exigibilidad or sale perfection); the Art. 19 services
territoriality (direct in-country performance test regardless of payment
place; partial ⇒ proportional; in-transit-related ⇒ full; foreign transport
already in the Art. 48-g import base never re-taxed); the Arts. 20-27
subject regime (*sujetos pasivos* a)-f) including unions of persons,
asocios, consorcios and government entities — *salvo actividades
bursátiles*; representation; contribuyente definitions 22-24 with importers
contribuyentes *en forma habitual o nó*; the Art. 25 *habitualidad*
calification with its *presunción de derecho* (conclusive presumption) for
the objeto social/giro principal and Código de Comercio merchant acts; the
Art. 26 ONE-taxpayer rule for local matriz with sucursales/agencias; the
Art. 27 agrupamiento solidarity); and the Arts. 28-32 *excluidos* regime
(the two 1992-colones thresholds as dated-historical text with the
administered-criteria config gap; the month-subsiguiente flip; the
sociedades/importadores/multi-local carve-outs; the Art. 30 opción from the
next January 1; no *crédito fiscal* ever; facturas *sin ningún recargo* —
enforced through the FSEE document type).

It does **not** cover: the *tasa* (rate) and *base imponible* rules (Arts.
47-49 — the base/rate file of this wave owns them; this file consumes the
Art. 48-c retiro base and Art. 48-g import base as pointers, never
restating their computation); the *débito/crédito fiscal* determination
machinery (Arts. 62-66 — the determination/credit file owns it; the Art.
9 exchange/return path routes INTO its Art. 62-1-a deduction by pointer);
the exempt-operations catalogs (Arts. 42-46 and 167-A) and the
exportación/zero-rating regime (Rgto. Art. 2 definitions cited only as
vocabulary); the IVA retention matrix (CT Arts. 161/162/162-A/162-B — the
retention file of this wave); DTE emission itself, including the FSEE
electronic excluded-subject document (`e-invoicing/01_dte-types.md`
SV-EINV-FR-048/001 own it — this file supplies only the excluido status and
the no-IVA-line rule); the F-07 Anexo 5 purchases-from-excluded-subjects
annex (`fiscal-reporting/03_f07-annexes-purchases.md` SV-FREP-FR-086 —
CT-119 zone); and the special-customs-regimes clocks whose expiry produces
the definitive conversion this file taxes
(`special-regimes/04_customs-clocks.md` SV-SPE-FR-064/066 — cited by id,
never restated). The Art. 2 coexistence rule is the Ley-side anchor
consumed by the special-regimes FOVIAL/COTRANS exclusion guards (S8 files,
by id).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). Embedded *interpretaciones auténticas* (authentic
interpretations) are part of 01_ AS PRINTED: D.L. 634-1993 (Art. 173) and
D.L. 820-1994 (Art. 45-d) touch articles outside this file; **D.L.
645-2005** is load-bearing here (Art. 14-III, printed inline pp.7-8).
Articles 113/123/124/161 are void (Sala de lo Constitucional, 17-Dec-1992,
expedientes 3-92/6-92) — none in this file's range (Arts. 1-32 all live).
**SOQ-54 vintage note (rides every 01_/02_ LB in this file):** the
consolidation's last reform stamp is D.L. 71-2015 — post-2015 reforms
unverified; corpus-internal signals negative (DTE stack 44_/45_,
Quincena-25 package 66_/67_, F-07 v14 manual silent); re-verify at
implementation. **Reglamento = 02_ survivors only** (D.E. 83-1992
consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass repeal =
D.E. 117-2001 stamp (3) — ruling R30(a), R17-bis kin: repeal authority is
the D.E., not the Código Tributario); survivor articles = 1-10, 16-30,
50-51 (+ 52 vigencia); this file cites Rgto. Arts. 2, 4, 5, 8, 9, 10, 20 —
all survivors. **CT re-anchors for procedure:** ~60 Ley articles were
derogated by D.L. 230/00 (registration, documents, sanctions,
administration — now Código Tributario); where a survivor carries a stale
anchor it is cited with note (Rgto. Art. 22 → "artículo 107 de la ley"
derogated, now CT 141). **V1 citation rule:** every LB row below cites 01_
or 02_ with the EVID id and the txt page anchor (`=== PAGE n ===` markers
of `01_Ley_IVA.pdf.txt` / `02_Reglamento_IVA.pdf.txt`, verified this
task); the SOQ-54 watch rides all of them.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA (D.L. 296-1992, texto consolidado), Arts. 1-2 | Art. 1: the tax applies to "la transferencia, importación, internación, exportación y al consumo de los bienes muebles corporales; prestación, importación, internación, exportación y el autoconsumo de servicios". Art. 2: the tax applies "sin perjuicio de la imposición de otros impuestos que graven los mismos actos o hechos" — production, distribution, transfer, comercialización, import/internación of determined goods and the prestación, import/internación of certain services | `sv/sources/01_Ley_IVA.pdf` | Arts. 1-2 p.2 (EVID-305; verified 01_ txt lines 58-66) |
| LB-002 | Ley IVA, Art. 5 | "EN EL CONCEPTO DE BIENES MUEBLES CORPORALES SE COMPRENDE CUALQUIER BIEN TANGIBLE QUE SEA TRANSPORTABLE DE UN LUGAR A OTRO POR SÍ MISMO O POR UNA FUERZA O ENERGÍA EXTERNA." "LOS TÍTULOS VALORES Y OTROS INSTRUMENTOS FINANCIEROS SE CONSIDERAN BIENES MUEBLES INCORPÓREOS, SIN PERJUICIO DE LO ESTABLECIDO EN EL ARTÍCULO 7 LITERAL D) DE ESTA LEY." "PARA EFECTOS DE LO DISPUESTO EN ESTA LEY, LOS MUTUOS DINERARIOS, CRÉDITOS EN DINERO O CUALQUIER FORMA DE FINANCIAMIENTO SE CONSIDERA PRESTACIÓN DE SERVICIOS." (stamp 8) | `sv/sources/01_Ley_IVA.pdf` | Art. 5 p.2 (EVID-306; verified 01_ txt lines 86-94) |
| LB-003 | Ley IVA, Art. 6 | Transfer of dominion comprises not only the compraventa but "también las que resulten de todos los actos, convenciones o contratos en general que tengan por objeto, transferir o enajenar a título oneroso el total o una cuota del dominio de esos bienes, cualquiera que sea la calificación o denominación que le asignen las partes o interesados, las condiciones pactadas por ellos o se realice a nombre y cuenta propia o de un tercero" | `sv/sources/01_Ley_IVA.pdf` | Art. 6 p.2 (EVID-306; verified 01_ txt lines 96-102) |
| LB-004 | Ley IVA, Art. 7 a)-m) — FULL CATALOG | Acts/conventions/contracts comprising transfer, "entre otros", of bienes muebles corporales: a) "Transferencias efectuadas en pública subasta, adjudicaciones en pago o remate de bienes muebles corporales pertenecientes a contribuyentes del impuesto"; b) "Permutas"; c) "Daciones en pago"; d) "Cesión de títulos de dominio de bienes muebles corporales"; e) "Mutuos o préstamos de consumo en que una parte entrega a la otra, cosas fungibles con cargo a restituir otras tantas del mismo género y calidad"; f) "Aportes de bienes muebles corporales propios del giro a sociedades u otras personas jurídicas, sociedades nulas, irregulares o de hecho y en general, a entidades o colectividades sin personalidad jurídica"; g) "Transferencias de bienes muebles corporales propias del giro con ocasión de la modificación, ampliación, transformación, fusión u otras formas de reorganización de sociedades"; h) "ADJUDICACIONES Y TRANSFERENCIAS DE BIENES MUEBLES CORPORALES, EFECTUADAS COMO CONSECUENCIA DE DISOLUCIONES Y LIQUIDACIONES O DISMINUCIONES DE CAPITAL DE SOCIEDADES U OTRAS PERSONAS JURÍDICAS, SOCIEDADES NULAS, IRREGULARES O DE HECHO Y ENTES COLECTIVOS CON O SIN PERSONALIDAD JURÍDICA. EN LOS CASOS INDICADOS EN ESTE LITERAL NO SERÁ OBJETO A GRAVAMEN LA TRANSFERENCIA DE BIENES MUEBLES CORPORALES CUANDO EL ADJUDICATARIO FUERE EL MISMO SOCIO O ACCIONISTA QUE LO APORTÓ, Y DICHO BIEN NO SE ENCONTRABA GRAVADO CON EL IMPUESTO QUE TRATA ESTA LEY" (stamp 11); i) "Transferencias de establecimientos o empresas mercantiles, respecto únicamente de los bienes muebles corporales del activo realizable incluídos en la operación"; j) "Constitución o transferencia onerosa del derecho de usufructo, uso o del derecho de explotar o de apropiarse de productos o bienes muebles por anticipado, extraídos de canteras, minas, lagos, bosques, plantaciones, almácigos y otros semejantes"; k) "Promesa de venta seguida de la transferencia de la posesión"; l) "En general, toda forma de entrega onerosa de bienes que da a quien los recibe la libre facultad de disponer económicamente de ellos, como si fuere propietario; y,"; m) "TRANSFERENCIAS DE BIENES MUEBLES CORPORALES EFECTUADAS POR SUJETOS PASIVOS, CUYOS BIENES HAYAN SIDO ADQUIRIDOS POR ÉSTOS EN PAGO DE DEUDAS" (stamp 11) | `sv/sources/01_Ley_IVA.pdf` | Art. 7 pp.3-4 (EVID-306; verified 01_ txt lines 104-145) |
| LB-005 | Ley IVA, Art. 8 | The tax is caused "cuando se emite el documento que da constancia de la operación". "Si se pagare el precio o se entregaren real o simbólicamente los bienes antes de la emisión de los documentos respectivos, o si por la naturaleza del acto o por otra causa, no correspondiere dicha emisión, la transferencia de dominio y el impuesto se causará cuando tales hechos tengan lugar." "En las entregas de bienes en consignación el impuesto se causará cuando el consignatario realice alguno de los hechos indicados en el inciso anterior." "El impuesto se causa aún cuando haya omisión o mora en el pago del precio o que éste no haya sido fijado en forma definitiva por las partes." | `sv/sources/01_Ley_IVA.pdf` | Art. 8 p.4 (EVID-306; verified 01_ txt lines 147-155) |
| LB-006 | Ley IVA, Art. 9 | Exchange or return of goods/products/merchandise "por encontrarse en mal estado, con el plazo para su consumo vencido, averiadas, por no corresponder a las realmente adquiridas u otras causas semejantes, no constituirá una nueva transferencia, sino que producirá en la determinación del impuesto los efectos que se establecen en el artículo 62 numeral 1o.) letra a) de esta ley, a menos que se compruebe el propósito entre las partes de celebrar nuevo contrato" | `sv/sources/01_Ley_IVA.pdf` | Art. 9 p.6 (EVID-306; verified 01_ txt lines 171-175) |
| LB-007 | Ley IVA, Art. 10 | Transfers are hecho generador "cuando los respectivos bienes muebles corporales se encuentren situados, matriculados o registrados en el país, no obstante que pudieren encontrarse colocados transitoriamente en él ó en el extranjero y aún cuando los actos, convenciones o contratos respectivos se hayan celebrado en el exterior." Deemed situados in the national territory: "los bienes que se encuentren embarcados desde el país de su procedencia, al ser transferidos a adquirentes no contribuyentes del impuesto" | `sv/sources/01_Ley_IVA.pdf` | Art. 10 p.6 (EVID-306; verified 01_ txt lines 177-183) |
| LB-008 | Ley IVA, Art. 11 | Hecho generador: "el retiro o desafectación de bienes muebles corporales del activo realizable de la empresa, aún de su propia producción, efectuados por el contribuyente con destino al uso o consumo propio, de los socios, directivos o personal de la empresa." Assimilated to transfer: "los retiros de bienes muebles corporales destinados a rifas, sorteos o distribución gratuita con fines promocionales, de propaganda o publicitarios, sean o nó del giro de la empresa." Presumption: "Se considerarán retirados o desafectados todos los bienes que faltaren en los inventarios y cuya salida de la empresa no se debiere a caso fortuito o fuerza mayor o a causas inherentes a las operaciones, modalidades de trabajo o actividades normales del negocio." NOT retirados: goods moved realizable→activo fijo "siempre que sean necesarios para el giro del negocio"; donations to the entities of ISR Art. 6 literal c) inciso segundo, "calificadas previamente" and meeting Dirección General requirements | `sv/sources/01_Ley_IVA.pdf` | Art. 11 p.6 (EVID-307; verified 01_ txt lines 187-200) |
| LB-009 | Ley IVA, Arts. 12-13 | Art. 12: retiro causes the tax "en la fecha del retiro." Art. 13: retiro is hecho generador for goods "situados, matriculados, registrados o colocados permanente o transitoriamente en el país, no obstante que pudieren encontrarse transitoriamente fuera de él" | `sv/sources/01_Ley_IVA.pdf` | Arts. 12-13 p.6-7 (EVID-307; verified 01_ txt lines 202-214) |
| LB-010 | Reglamento IVA (D.E. 83-1992 consolidado), Art. 4 | Retiros for use/consumption of socios/directivos/personal "se entenderán comprendidos también, el grupo familiar de ellos y los terceros." Not taxed per Art. 11 inciso segundo: use/consumption of activo realizable goods "necesarios para el giro o actividades normales del negocio o el traslado de éstos al activo fijo del mismo." Caso fortuito o fuerza mayor = "el imprevisto que no es posible resistir, como una inundación, terremoto, incendio, accidente, robo, merma, etc.", proven "entre otros" by: a) "Anotaciones cronológicas efectuadas en el sistema de inventario permanente, directamente relacionado con la contabilidad que mantenga el contribuyente"; b) "Denuncias por robos o accidentes de cualquier naturaleza hechos a la autoridad policial y al tribunal competente"; c) "Informes de liquidaciones del seguro; y" d) "Mermas reconocidas por disposiciones legales vigentes u organismos técnicos gubernamentales." Precondition: "será condición prioritaria e ineludible, que las cantidades y valores correspondientes se encuentren contabilizados en las fechas que se produjo la pérdida, robo, merma, siniestro, etc." | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 4 pp.3-4 (EVID-334; verified 02_ txt lines 105-125) |
| LB-011 | Reglamento IVA, Art. 20 | For retiros/autoconsumo "deberá emitirse la Factura correspondiente como consumidor final" | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 20 pp.6-7 (EVID-336; verified 02_ txt line 228) |
| LB-012 | Ley IVA, Art. 14 | Hecho generador: "la importación e internación definitiva al país de bienes muebles corporales y de servicios." "Las subastas o remates realizados en las Aduanas constituyen actos de importación o internación." "Existe importación o internación de servicios cuando la actividad que generan los servicios se desarrolla en el exterior y son prestados a un usuario domiciliado en el país que los utiliza en él, tales como: asesorías o asistencias técnicas, marcas, patentes, modelos, informaciones, programas de computación y arrendamiento de bienes muebles corporales" | `sv/sources/01_Ley_IVA.pdf` | Art. 14 pp.7-9 (EVID-308; verified 01_ txt lines 218-224) |
| LB-013 | D.L. 645 (17-mar-2005, D.O. 55 T.366 18-mar-2005), interpretación auténtica del Art. 14 inciso tercero — embedded in 01_ as printed | Art. 1: "Interprétese auténticamente el inciso tercero del Art. 14 de la Ley de Impuesto a la Transferencia de Bienes Muebles y la Prestación de Servicios, en el sentido que, en la importación e internación de servicios a que se refiere la Ley … como hecho generador gravado con dicho impuesto, la utilización del servicio debe ocurrir de manera exclusiva en el territorio de la República de El Salvador." Art. 2: incorporated into the Ley's text from its vigencia. Art. 3: vigencia eight days after publication | `sv/sources/01_Ley_IVA.pdf` | D.L. 645 block pp.7-8 (EVID-308; verified 01_ txt lines 225-270) |
| LB-014 | Ley IVA, Art. 15 | "LA IMPORTACIÓN E INTERNACIÓN DEFINITIVA DE BIENES MUEBLES CORPORALES SE ENTENDERÁ OCURRIDA Y CAUSADO EL IMPUESTO EN EL MOMENTO QUE TENGA LUGAR SU IMPORTACIÓN O INTERNACIÓN. (8)" Services: earliest of "a) CUANDO SE EMITA EL DOCUMENTO QUE DÉ CONSTANCIA DE LA OPERACIÓN POR PARTE DEL PRESTADOR DEL SERVICIO; b) CUANDO SE REALICE EL PAGO; O c) CUANDO SE DÉ TÉRMINO A LA PRESTACIÓN. (8)" Special customs regimes: "el impuesto se devenga en su totalidad o por la diferencia, según fuere el caso, al quedar los bienes entregados a la libre disponibilidad de los importadores por haberse convertido la importación o internación en definitiva" | `sv/sources/01_Ley_IVA.pdf` | Art. 15 pp.8-9 (EVID-308; verified 01_ txt lines 272-292) |
| LB-015 | Ley IVA, Art. 16 | "CONSTITUYE HECHO GENERADOR DEL IMPUESTO LAS PRESTACIONES DE SERVICIOS PROVENIENTES DE ACTOS, CONVENCIONES O CONTRATOS EN QUE UNA PARTE SE OBLIGA A PRESTARLOS Y LA OTRA SE OBLIGA A PAGAR COMO CONTRAPRESTACIÓN UNA RENTA, HONORARIO, COMISIÓN, INTERÉS, PRIMA, REGALÍA, ASÍ COMO CUALQUIER OTRA FORMA DE REMUNERACIÓN." Also: "LA UTILIZACIÓN DE LOS SERVICIOS PRODUCIDOS POR EL CONTRIBUYENTE, DESTINADOS PARA EL USO O CONSUMO PROPIO, DE LOS SOCIOS, DIRECTIVOS, APODERADOS O PERSONAL DE LA EMPRESA, AL GRUPO FAMILIAR DE CUALQUIERA DE ELLOS O A TERCEROS. (8)" Excluded: "los pagos por indemnizaciones de perjuicios o siniestros"; and "NO CONSTITUYE HECHO GENERADOR LAS DONACIONES DE SERVICIOS DE CARÁCTER GRATUITO E IRREVOCABLES PRODUCIDOS POR EL CONTRIBUYENTE, REALIZADAS A LAS ENTIDADES A QUE SE REFIERE EL ART. 6 DE LA LEY DE IMPUESTO SOBRE LA RENTA, QUE HAYAN SIDO PREVIAMENTE CALIFICADAS POR LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS, Y QUE NO BENEFICIEN AL CONTRIBUYENTE SEGÚN LO ESTABLECIDO EN EL ART. 32 NUM, 4) INC. 5º DE LA LEY DE IMPUESTO SOBRE LA RENTA. (9)" | `sv/sources/01_Ley_IVA.pdf` | Art. 16 pp.9-10 (EVID-309; verified 01_ txt lines 296-309) |
| LB-016 | Ley IVA, Art. 17 a)-q) + inciso final — FULL CATALOG | "SON PRESTACIONES DE SERVICIOS TODAS AQUELLAS OPERACIONES ONEROSAS, QUE NO CONSISTAN EN LA TRANSFERENCIA DE DOMINIO DE BIENES MUEBLES CORPORALES" (stamp 1), among them: a) "Prestaciones de toda clase de servicios sean permanentes, regulares, continuos o periódicos"; b) "Asesorías técnicas y elaboración de planos y proyectos"; c) "ARRENDAMIENTOS DE BIENES MUEBLES CORPORALES CON O SIN PROMESA DE VENTA U OPCIÓN DE COMPRA, SUBARRENDAMIENTOS, CONCESIÓN O CUALQUIER OTRA FORMA DE CESIÓN DEL USO O GOCE DE BIENES MUEBLES CORPORALES. (8)"; d) "ARRENDAMIENTO, SUBARRENDAMIENTO DE INMUEBLES DESTINADOS A ACTIVIDADES COMERCIALES, INDUSTRIALES, DE SERVICIOS O DE CUALQUIER OTRA ACTIVIDAD, CON O SIN PROMESA DE VENTA U OPCIÓN DE COMPRA, USUFRUCTO, CONCESIÓN O CUALQUIER OTRA FORMA DE CESIÓN DEL USO O GOCE DE TODO TIPO DE INMUEBLES, ESTABLECIMIENTOS Y EMPRESAS MERCANTILES. (8)"; e) "Arrendamiento de servicios en general"; f) "Confeccionar o ejecutar por sí o bajo su dirección una obra material mueble, con materias primas aportadas por quien encarga la obra"; g) "Ejecución de obras de ingeniería o similares, en que se emplean materiales o medios suministrados por quien encarga la obra"; h) "Instalación, confección de obras, de especialidades o de movimientos de tierra pactados por administración o mandato, por precio alzado o unitario o en otra forma"; i) "Reparaciones, transformaciones, ampliaciones que no significan una confección o construcción de una obra inmueble nueva, y los trabajos de mantenimiento, reparación y conservación de bienes muebles e inmuebles"; j) "Contratos generales de construcción o edificación de inmuebles nuevos por administración o mandato, en que el ejecutor o constructor aporta solamente su trabajo personal y el que encarga la obra o construcción suministra los materiales"; k) "La construcción o edificación de inmuebles nuevos, convenidos por un precio alzado en los cuales los materiales principales son suministrados íntegra o mayoritariamente por el contratista"; l) "Comisión, mandato, consignación, de ventas en remate o celebrados con instituciones de subasta, ferias o bolsas"; m) "Transporte o flete de carga, terrestre, aéreo y marítimo y de pasajeros, aéreo y marítimo"; n) "Los prestados en el ejercicio liberal de profesiones universitarias y de contaduría pública o servicios independientes no subordinados … Para los efectos de esta ley, se considera profesión liberal la función del notariado"; o) "EL ARRENDAMIENTO, SUBARRENDAMIENTO, CONCESIÓN O CUALQUIER OTRA FORMA DE CESIÓN DEL USO O GOCE DE MARCAS, PATENTES DE INVENCIÓN, PROCEDIMIENTOS O FÓRMULAS INDUSTRIALES Y OTRAS PRESTACIONES DE SERVICIOS SIMILARES. (8)"; p) "EL PAGO DE DIETAS O CUALQUIER OTRO EMOLUMENTO DE IGUAL O SIMILAR NATURALEZA. NO SE ENCUENTRAN COMPRENDIDOS LAS DIETAS POR SERVICIOS REGIDOS POR LA LEGISLACIÓN LABORAL Y LOS PRESTADOS POR LOS EMPLEADOS Y FUNCIONARIOS PÚBLICOS, MUNICIPALES Y DE INSTITUCIONES AUTÓNOMAS; y, (11)"; q) "EL PAGO DE MEMBRESÍAS, CUOTAS, O CUALQUIER OTRA FORMA DE PAGO DE SIMILAR NATURALEZA QUE GENERE UNA CONTRAPRESTACIÓN DEL USO, GOCE O DISFRUTE DE BIENES O SERVICIOS, INDISTINTAMENTE LA MANERA EN QUE SE RECIBAN. (11)". Final inciso: "SE ASIMILA A PRESTACIONES DE SERVICIOS LOS REINTEGROS O REEMBOLSO DE GASTOS, LOS CUALES SE GRAVARÁN CON EL PRESENTE IMPUESTO AL MOMENTO DE SU PAGO. NO SE ENCUENTRAN COMPRENDIDOS EN ESTA DISPOSICIÓN LOS REINTEGROS O REEMBOLSO DE GASTOS EN CONCEPTO DE SEGUROS, ALIMENTACIÓN Y VIÁTICOS QUE RECIBAN LOS TRABAJADORES; ASÍ COMO AQUELLOS REINTEGROS O REEMBOLSOS QUE CUMPLAN LA EXCEPCIÓN ESTABLECIDA EN EL ARTÍCULO 51 LITERAL a) DE LA PRESENTE LEY, SIEMPRE QUE EL MANDATARIO NO SE HUBIERE DEDUCIDO CRÉDITOS FISCALES EN RELACIÓN CON DICHAS SUMAS. (11)" | `sv/sources/01_Ley_IVA.pdf` | Art. 17 pp.9-11 (EVID-309; verified 01_ txt lines 311-379) |
| LB-017 | Ley IVA, Art. 18 | Services caused per whichever occurs first: "a) Cuando se emita alguno de los documentos señalados en los artículos 97 y 100 de esta ley; b) Cuando se dé término a la prestación; c) Cuando se entregue el bien objeto del servicio en arrendamiento, subarrendamiento, uso o goce; d) Cuando se entregue o ponga a disposición el bien o la obra …; y e) CUANDO SE PAGUE TOTALMENTE EL VALOR DE LA CONTRAPRESTACIÓN O PRECIO CONVENIDO, O POR CADA PAGO PARCIAL DEL MISMO … SE ACREDITE EN CUENTA O SE PONGA A DISPOSICIÓN DEL PRESTADOR DE LOS SERVICIOS, YA SEA EN FORMA TOTAL O PARCIAL, AUNQUE SEA CON ANTICIPACIÓN A LA PRESTACIÓN DE ELLOS. (8)" Permanent/regular/continuous/periodic services: caused at any Art. 97 document or "al término de cada período establecido para el pago, según cual hecho acontezca primero, independientemente de la fecha de pago del servicio." Leasing with opción de compra or promesa de venta: "al momento de ser exigibles los cánones de arrendamiento o al perfeccionarse la venta" | `sv/sources/01_Ley_IVA.pdf` | Art. 18 pp.11-12 (EVID-310; verified 01_ txt lines 381-400) |
| LB-018 | Ley IVA, Art. 19 | Services are hecho generador "cuando ellos se presten directamente en el país, no obstante que los respectivos actos, convenciones o contratos se hayan perfeccionado fuera de él, y cualquiera que sea el lugar en que se pague o se perciba la remuneración." Performed in national territory when "la actividad que genera el servicio es desarrollada en el país." "Si los servicios se prestan parcialmente en el país, sólo se causará el impuesto que corresponda a la parte de los servicios prestados en él. Pero se causará el total del impuesto cuando los servicios son prestados en el país, aunque no sean exclusivamente utilizados en él, como por ejemplo cuando ellos se relacionan con bienes, transportes o cargas en tránsito." Final (stamp 11): foreign transport services already taxed when added to the import base per Art. 48-g "NO SERÁN GRAVADOS NUEVAMENTE CON EL REFERIDO IMPUESTO" | `sv/sources/01_Ley_IVA.pdf` | Art. 19 pp.11-12 (EVID-310; verified 01_ txt lines 402-423) |
| LB-019 | Ley IVA, Art. 20 | Sujetos pasivos o deudores, as contribuyentes or responsables: "a) Las personas naturales o jurídicas; b) Las sucesiones; c) Las sociedades nulas, irregulares o de hecho; d) Los fideicomisos; e) Las asociaciones cooperativas; y, f) LA UNIÓN DE PERSONAS, ASOCIOS, CONSORCIOS O CUALQUIERA QUE FUERE SU DENOMINACIÓN. (11)". Same quality: government-central and decentralized/autonomous entities when realizing the hechos "no obstante que las leyes por las cuales se rigen las hayan eximido de toda clase de contribuciones o impuestos; salvo cuando realicen actividades bursátiles." "Asume la calidad de sujeto pasivo, quien actúa a su propio nombre, sea por cuenta propia o por cuenta de un tercero." Acting for a third party: the represented tercero/mandante is sujeto pasivo. "POR LOS SUJETOS QUE CARECEN DE PERSONALIDAD JURÍDICA, ACTUARÁN SUS INTEGRANTES, ADMINISTRADORES O REPRESENTANTES. (11)" | `sv/sources/01_Ley_IVA.pdf` | Art. 20 pp.12-13 (EVID-311; verified 01_ txt lines 431-457) |
| LB-020 | Ley IVA, Arts. 22-24 | Art. 22: contribuyentes are those who "en carácter de productores, comerciantes mayoristas o al por menor, o en cualesquiera otras calidades realizan dentro de su giro o actividad o en forma habitual … ventas u otras operaciones que signifiquen la transferencia onerosa del dominio de los respectivos bienes muebles corporales, nuevos o usados"; also "quienes transfieran materias primas o insumos que no fueron utilizados en el proceso productivo." NOT contribuyentes: "quienes realizan transferencias ocasionales de bienes muebles corporales adquiridos sin ánimo de revenderlos." Art. 23: "Son contribuyentes del impuesto quienes, en forma habitual o nó, realicen importaciones o internaciones definitivas de bienes muebles corporales o de servicios." Art. 24: contribuyentes are "los sujetos que en forma habitual y onerosa prestan los respectivos servicios" | `sv/sources/01_Ley_IVA.pdf` | Arts. 22-24 pp.13-14 (EVID-311; verified 01_ txt lines 463-485) |
| LB-021 | Ley IVA, Art. 25 | DGII califies habitualidad "considerando la naturaleza, cantidad y frecuencia con que realice las respectivas operaciones y, en su caso, si el ánimo al adquirir los bienes muebles corporales fué destinarlos a su uso, consumo o para la reventa." "Se presume de derecho que existe habitualidad en la realización de los hechos que constituyen el objeto social o el giro o actividad principal del contribuyente. Igual presunción de derecho existirá respecto de los comerciantes que realicen actos de comercio contemplados en el Código de Comercio." The DGII calification "admitirá prueba en contrario … si éste recurriere en contra de la determinación del impuesto; pero no la admiten las referidas presunciones de derecho" | `sv/sources/01_Ley_IVA.pdf` | Art. 25 p.15 (EVID-311; verified 01_ txt lines 494-503) |
| LB-022 | Ley IVA, Arts. 26-27 | Art. 26: "Cuando el contribuyente realice sus actividades a través de una casa matriz local con sucursales o agencias, la capacidad y responsabilidad como contribuyente estará radicada en la casa matriz." Art. 27 (stamp 11): agrupamientos of Art. 20 subjects organized for a specific business/operation without own legal personality — the responsible for substantive and formal obligations "ES EL REPRESENTANTE O ADMINISTRADOR Y A FALTA DE ÉSTOS ACTUARÁN LOS ASOCIADOS, PARTÍCIPES, O SUS INTEGRANTES, QUIENES RESPONDEN SOLIDARIAMENTE DE LAS DEUDAS TRIBUTARIAS DEL AGRUPAMIENTO" | `sv/sources/01_Ley_IVA.pdf` | Arts. 26-27 p.15 (EVID-311; verified 01_ txt lines 505-514) |
| LB-023 | Ley IVA, Arts. 28-29 + Reglamento IVA, Art. 9 | Art. 28: excluded from contribuyente status are those whose prior-12-month transfers (gravadas y exentas) were "por un monto menor a cincuenta mil colones" AND whose "total de su activo sea inferior a veinte mil colones" [sic — 1992 colones, never updated in the text]. Crossing either: contribuyente "a partir del mes subsiguiente a aquel en que ello ocurra"; DGII inscribes "a petición del interesado o de oficio." No application "respecto de sociedades e importadores, ni tampoco cuando un contribuyente tenga más de un local que en conjunto excedan los límites señalados." Art. 29: start-ups excluded "siempre que su activo total inicial sea inferior a veinte mil colones; esta exclusión no será aplicable en los casos de importaciones e internaciones." Rgto. Art. 9: exclusion requires "concurrir los dos requisitos que se establecen en el artículo 28 de la ley" | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Arts. 28-29 pp.15-16 (EVID-312; verified 01_ txt lines 518-539); Rgto. Art. 9 p.5 (EVID-335; verified 02_ txt lines 183-184) |
| LB-024 | Ley IVA, Art. 30 + Reglamento IVA, Art. 10 | Art. 30: subjects may opt for contribuyente status "previo cumplimiento de los requisitos que establezca la Dirección General"; voluntary entry "operará a partir del primero de enero del año calendario siguiente; la Dirección General podrá autorizar el ingreso en cualquier tiempo." Rgto. Art. 10: optants prove sales/income "por lo menos con el libro de gastos, conpras [sic] y ventas, autorizado por el Registro de Comercio y su activo mediante un inventario valorado de bienes o por otros medios que establezca la Dirección General" | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Art. 30 p.16 (EVID-312; verified 01_ txt lines 541-545); Rgto. Art. 10 p.5 (EVID-335; verified 02_ txt lines 185-188) |
| LB-025 | Ley IVA, Arts. 31-32 | Art. 31: for excluidos, amounts recargado in CCFs on acquisitions and import-paid IVA "no constituirá para ellos crédito fiscal deducible, en los términos dispuestos en el artículo 65 de esta ley"; and in their own transfers/prestations "no trasladarán por concepto del impuesto ningún crédito fiscal deducible por éstos." Art. 32: "En las facturas o documentos equivalentes que emitan los excluídos como contribuyentes del impuesto, deberán consignar el precio de la operación, sin ningún recargo a título del presente impuesto" | `sv/sources/01_Ley_IVA.pdf` | Arts. 31-32 p.16 (EVID-312; verified 01_ txt lines 547-557) |
| LB-026 | Reglamento IVA, Arts. 2, 5 y 8 (definitional pack) | Art. 2 numerals: 18) "Activo o Activo en Giro: El total de los bienes muebles e inmuebles, créditos, y derechos que el contribuyente haya destinado para realizar el giro o actividad de su negocio … excluyéndose las pérdidas y demás cuentas que aparecen en el activo sólo para efectos contables"; 19) Activo Realizable (bienes muebles corporales propios del giro, producidos o adquiridos con ánimo de revenderlos o transferirlos); 20) Activo Fijo (bienes de naturaleza permanente … que éste no los adquiera con el ánimo de transferirlos o revenderlos); 21) "Precio Corriente de Mercado: El precio de venta que tengan los bienes o servicios, en negocios o establecimientos similares ubicados en el mismo sector, localidad o departamento." Art. 5: services produced by the contribuyente are destined to own/socios/directivos/personnel use "aún cuando se destinen al grupo familiar de éstos o a terceros." Art. 8: contribuyentes also "quienes transfieran desechos, desperdicios, residuos y otros similares, hayan sido obtenidos o no del proceso productivo" | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 2 pp.1-3 (EVID-333; verified 02_ txt lines 16-98); Art. 5 p.4 (EVID-334; verified 02_ txt lines 128-130); Art. 8 p.5 (EVID-334; verified 02_ txt lines 178-180) |
| LB-027 | Ley IVA, Art. 48 literal c) — **POINTER** | Retiro base: "En los retiros de bienes de la empresa es el valor que el contribuyente les tenga asignado como precio de venta al público según sus documentos y registros contables, y a falta de éstos, el precio corriente de mercado" — base-imponible rule owned by the base/rate file of this wave (V3); consumed here for the retiro invoice base, not restated | `sv/sources/01_Ley_IVA.pdf` | Art. 48-c p.23 (EVID-315; verified 01_ txt lines 790-792) |
| LB-028 | Ley IVA, Art. 62 numeral 1º a) — **POINTER** | Débito-fiscal deduction for "Monto del valor de los bienes, envases o depósitos devueltos o de otras operaciones anuladas o rescindidas en el período tributario, pero dentro de los tres meses de la entrega de los bienes o de la percepción del pago de los servicios, siempre que se pruebe que ese valor ha sido considerado para el cálculo del débito fiscal en el mismo período o en otro anterior, lo que deberá comprobar el contribuyente" — determination machinery owned by the débito/crédito file of this wave; the Art. 9 return path routes into it by pointer | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-a pp.27-28 (verified 01_ txt lines 948-957; no dedicated W15 EVID entry — txt-verified) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): Ley Art. 3 (interpretación del hecho generador),
Art. 21 (transmisión de calidad de contribuyente), Art. 33 (responsables
concept) and the whole D.L. 230/00-repealed procedural belt (Arts. 79-141
zone) are DEROGADO — procedures, documents, sanctions and administration
live in the Código Tributario (CT re-anchor); void-on-constitutionality
Arts. 113/123/124/161 (sentencia 17-dic-1992) sit outside this file's
range and are noted only as consolidation provenance; vetoed D.L. 24-2003
(five-year agro-input IVA exemption) never entered into force. Reglamento
non-survivors (everything outside 1-10, 16-30, 50-51) are per R30(a)
derogated and never cited. Rgto. Art. 2 numerals 11-12 and 15
(importación/internación definitiva, regímenes aduaneros especiales) are
vocabulary consumed by the special-regimes wave (SR4/SR6 by id), restated
here only as definitions. The SOQ-54 vintage watch (§2 preamble) applies
to every row above.

## 3. Functional Requirements

### 3.1 Operation model — scope, transfer concept and goods tax point (Arts. 1-10)

- **SV-TAX-FR-176:** The system shall model every IVA-relevant operation
  under the Art. 1 operation taxonomy — transfer, importación, internación,
  exportación and consumption of *bienes muebles corporales* (corporal
  movable goods); prestación, importación, internación, exportación and
  *autoconsumo* (self-consumption) of services — as a closed operation-kind
  enum on the accounting/invoice line, and shall apply IVA alongside any
  other tax over the same acts (Art. 2 coexistence: no exclusion logic
  triggered by the existence of special taxes over the same operation —
  consumed by the special-regimes exclusion guards, by id).
  (LB-001; EVID-305)
- **SV-TAX-FR-177:** The system shall classify as *bienes muebles
  corporales* every tangible good transportable from one place to another
  by itself or by an external force or energy; shall classify *títulos
  valores* (securities) and other financial instruments as *bienes muebles
  incorpóreos* — outside the goods-transfer regime save the Art. 7-d)
  cession-of-ownership-titles operation type; and shall classify *mutuos
  dinerarios* (money loans), *créditos en dinero* (money credit) and any
  form of *financiamiento* (financing) as PRESTACIÓN DE SERVICIOS — a
  financing product or loan line never resolves as a goods transfer.
  (LB-002; EVID-306)
- **SV-TAX-FR-178:** The system shall determine transfer character by
  substance over form: any act, convention or contract whose object is to
  transfer or alienate *a título oneroso* (for consideration) the total or
  a quota of the dominion of bienes muebles corporales is a transferencia —
  whatever label the parties assign, whatever conditions they pact, and
  whether performed in own name and account or for a third party; no
  document type or contract name may bypass the transfer classifier.
  (LB-003; EVID-306)
- **SV-TAX-FR-179:** The system shall seed its transfer-operation-type
  taxonomy with the FULL Art. 7 a)-m) catalog — every letter present, none
  dropped: a) pública subasta, adjudicaciones en pago y remate of goods
  belonging to contribuyentes; b) permutas; c) daciones en pago; d) cesión
  de títulos de dominio; e) mutuos or consumption loans of fungible things
  (restitution of others of the same genus and quality); f) aportes of
  own-giro goods to societies and other persons jurídicas, nulas,
  irregulares or de hecho, and to entities or collectivities without legal
  personality; g) own-giro transfers on occasion of modificación,
  ampliación, transformación, fusión or other forms of society
  reorganization; h) adjudications/transfers on disolución, liquidación or
  capital reduction of societies and other persons jurídicas — WITH the
  carve-out: NOT taxed when the adjudicatario is the SAME socio or
  accionista who aportó the good AND the good was not IVA-charged (both
  conditions required); i) establishment/mercantile-business transfers
  limited to the *activo realizable* goods included in the operation; j)
  constitution or onerous transfer of usufruct, use, or the right to
  exploit or appropriate products or goods by anticipation, extracted from
  canteras, minas, lagos, bosques, plantaciones, almácigos and similar; k)
  sale promise followed by transfer of possession; l) the catch-all — every
  form of onerous delivery giving the receiver free economic disposition
  as if owner; m) transfers by sujetos pasivos of goods acquired in
  payment of debts. The catalog ships as an OPEN list ("entre otros"):
  the letter-l catch-all classification is always available.
  (LB-004; EVID-306)
- **SV-TAX-FR-180:** The system shall fix the transfer tax point at the
  EARLIEST of: emission of the document evidencing the operation; payment
  of the price; or real or symbolic delivery of the goods — and where by
  the act's nature or another cause no document corresponds, at the
  happening of those facts; for goods delivered on consignment, at the
  moment the CONSIGNATARIO performs any of those acts (document, payment
  or delivery by the consignatario); and causation shall never be deferred
  by price omission, mora in payment, or the price not being finally fixed
  by the parties. The resolved tax point is snapshotted on the record
  (D15: values resolve as-of the tax-point date; corrections use
  original-period parameters).
  (LB-005; EVID-306)
- **SV-TAX-FR-181:** The system shall treat the exchange or return of
  goods, products or merchandise — bad state, expired consumption term,
  damaged, not corresponding to those really acquired, or similar causes —
  as NOT a new transfer, routing it to the Art. 62 numeral 1º a)
  débito-fiscal deduction path (three-month window from delivery/payment
  perception, prior-débito proof) owned by the determination file of this
  wave (LB-028 pointer — cited, not restated), UNLESS the purpose of
  celebrating a new contract between the parties is proven (flag
  `new_contract_intent` flips the routing to a fresh transfer).
  (LB-006; LB-028; EVID-306)
- **SV-TAX-FR-182:** The system shall territorialize goods transfers by
  the *situados, matriculados o registrados* (situated, enrolled or
  registered) test — goods situated, matriculated or registered in El
  Salvador are taxable even if transiently placed abroad and even if the
  act was celebrated abroad — and shall deem goods EMBARKED from the
  country of provenance, when transferred to acquirers who are NOT
  contribuyentes, as situated in the national territory (taxable).
  (LB-007; EVID-306)

### 3.2 Retiro de bienes — self-supply of goods (Arts. 11-13; Rgto. Art. 4)

- **SV-TAX-FR-183:** The system shall treat as a taxed retiro
  (self-supply) the withdrawal or *desafectación* of bienes muebles
  corporales from the *activo realizable* — including the company's own
  production — destined to the use or consumption of the company itself,
  its *socios* (partners), *directivos* (officers) or *personal*
  (personnel), EXTENDED per Reglamento Art. 4 to the *grupo familiar*
  (immediate family) of any of them and to *terceros* (third parties); and
  equally the retiros destined to raffles, sweepstakes or free
  distribution with promotional, propaganda or publicity purposes,
  WHETHER OR NOT of the company's giro. Every retiro destination is an
  enum: propio · socio · directivo · personal · grupo_familiar · tercero ·
  rifa_sorteo · promocional.
  (LB-008; LB-010; EVID-307/334)
- **SV-TAX-FR-184:** The system shall presume as RETIRED every good
  failing in the inventories whose exit from the company is not due to
  *caso fortuito o fuerza mayor* (unforeseeable accident or force majeure
  — inundation, earthquake, fire, accident, robbery, merma and similar) or
  to causes inherent to the operations, working modalities or normal
  activities of the business; the presumption is rebutted ONLY by evidence
  from the Reglamento Art. 4 menu — a) chronological annotations in the
  permanent-inventory system directly related to the accounting; b)
  *denuncias* (reports) for robberies or accidents to the police authority
  and competent tribunal; c) insurance-liquidation reports; d) *mermas*
  (shrinkage) recognized by prevailing legal provisions or governmental
  technical bodies — under the CONDITION (*prioritaria e ineludible*)
  that the quantities and values be accounted for ON THE DATES the loss,
  robbery, merma or siniestro occurred; absent menu evidence with the
  accounting-date check, the shortfall posts as a retiro.
  (LB-008; LB-010; EVID-307/334)
- **SV-TAX-FR-185:** The system shall NOT treat as retiro: (a) the
  transfer of goods from activo realizable to activo fijo when they are
  NECESSARY for the giro of the business — nor the use or consumption of
  realizable goods necessary for the giro or normal activities (Rgto.
  Art. 4 inciso 2), the necessity being a recorded classification with
  ground; and (b) goods donated to the entities of ISR Art. 6 literal c)
  inciso segundo, PREVIOUSLY calificadas under that article and meeting
  the additional Dirección General requirements — the donation carve-out
  requiring the calificación reference recorded on the donation event.
  (LB-008; LB-010; EVID-307/334)
- **SV-TAX-FR-186:** The system shall cause the retiro tax at the DATE OF
  THE RETIRO (Art. 12 — the D15 as-of anchor; parameters snapshotted on
  the retiro record), apply the Art. 13 situs rule (goods situated,
  matriculated, registered or placed permanently or transiently in the
  country, even if transiently outside it), and auto-emit the retiro
  invoice as CONSUMIDOR FINAL per Reglamento Art. 20 — a *factura*
  (consumer-final document, never a CCF), with the base taken per the
  Art. 48-c pointer (the value the contribuyente has assigned as public
  sale price per its documents and accounting records, else the *precio
  corriente de mercado* — LB-027; base computation owned by the base/rate
  file, consumed here).
  (LB-009; LB-011; LB-027; EVID-307/336)

### 3.3 Importación e internación of goods and services (Arts. 14-15; D.L. 645)

- **SV-TAX-FR-187:** The system shall treat as hecho generador the
  importación and internación DEFINITIVA into the country of bienes
  muebles corporales AND of services, and shall treat subastas or remates
  realized in the Aduanas (customs) as import/internation ACTS (auction
  acquisition = import operation kind).
  (LB-012; EVID-308)
- **SV-TAX-FR-188:** The system shall detect a services import when the
  activity generating the services is developed ABROAD and the services
  are rendered to a *usuario domiciliado* (domiciled user) in the country
  who utilizes them in it — the statutory exemplars (asesorías or
  asistencias técnicas, marcas, patentes, modelos, informaciones,
  programas de computación, arrendamiento de bienes muebles corporales)
  shipping as classification hints — CONSTRUED per the D.L. 645
  interpretación auténtica: the utilization of the service must occur *de
  manera exclusiva* (exclusively) in the territory of the Republic of El
  Salvador; any non-SV utilization blocks the import classification (the
  boundary with Art. 19 partial-performance proportionality is OQ-4).
  (LB-012; LB-013; EVID-308)
- **SV-TAX-FR-189:** The system shall fix the import tax point as: goods —
  at the moment the importación/internación takes place; services — at the
  EARLIEST of a) emission by the prestador of the document evidencing the
  operation, b) payment, c) término de la prestación (completion of the
  rendition); each trigger recorded with its source so the earliest
  governs.
  (LB-014; EVID-308)
- **SV-TAX-FR-190:** For goods imported or interned under special customs
  regimes, the system shall devengar the tax — in FULL or by the
  DIFFERENCE, as corresponds — at the moment the goods are delivered to
  the importers' FREE DISPOSABILITY upon the import/internation converting
  into definitive, consuming the definitive-conversion events produced by
  the special-regimes clock machinery
  (`special-regimes/04_customs-clocks.md` SV-SPE-FR-064/066 — cited by
  id, never restated: clock-expiry and definitive-traslado events are
  this file's trigger feed).
  (LB-014; EVID-308; SPE 04-file SV-SPE-FR-064/066)

### 3.4 Prestaciones de servicios — hecho generador and catalog (Arts. 16-17)

- **SV-TAX-FR-191:** The system shall treat as the services hecho
  generador the onerous prestaciones arising from acts, conventions or
  contracts where one party obliges to render them and the other to pay as
  consideration a *renta, honorario, comisión, interés, prima, regalía* or
  ANY other form of remuneration; shall equally tax the AUTOCONSUMO of
  services — utilization by the contribuyente itself, its socios,
  directivos, *apoderados* (attorneys-in-fact) or personnel, the grupo
  familiar of any of them, or terceros (Rgto. Art. 5); and shall EXCLUDE
  payments of *indemnizaciones de perjuicios o siniestros* (damages or
  casualty indemnities) and qualified gratuitous IRREVOCABLE service
  donations to ISR-Art.-6 entities previously calificadas by DGII that do
  not benefit the donor per ISR Art. 32 num. 4) inc. 5º.
  (LB-015; LB-026; EVID-309/334)
- **SV-TAX-FR-192:** The system shall classify service products under the
  FULL Art. 17 a)-q) catalog — every letter present, none dropped: a)
  permanent, regular, continuous or periodic services; b) technical
  advisories and elaboration of plans and projects; c) leases of bienes
  muebles corporales with or without sale promise or purchase option,
  subleases, concession or any other form of ceding use or enjoyment of
  movable goods; d) leases/subleases of INMUEBLES destined to commercial,
  industrial, services or any other activity — with or without sale
  promise or purchase option, usufruct, concession or any other form of
  cession of use/enjoyment of every type of inmuebles, establishments and
  mercantile businesses (housing leases are the Art. 46-b exemption file's
  surface, by pointer); e) leasing of services in general; f) making or
  executing a movable material work with raw materials supplied by the
  commissioner; g) engineering works or similar employing materials or
  means supplied by the commissioner; h) installation, work confection,
  specialties or earth movements pacted by administration or mandate, at
  lump-sum (*precio alzado*) or unit price or otherwise; i) repairs,
  transformations and amplifications not constituting a new immovable
  work, and maintenance, repair and conservation work on movable and
  immovable goods; j) general contracts of construction or edification of
  new inmuebles by administration or mandate (executor contributes only
  personal labor, commissioner supplies materials); k) construction or
  edification of new inmuebles at lump-sum price with main materials
  supplied wholly or majoritarily by the contractor; l) comisión,
  mandato, consignación, remate sales or those celebrated with auction
  institutions, fairs or bolsas; m) cargo transport — terrestrial, aerial
  and maritime — AND passenger transport aerial and maritime (terrestrial
  passengers are the Art. 46-i exemption file's surface, by pointer); n)
  liberal professions including university professions and contaduría
  pública, independent non-subordinated services of professions or
  oficios requiring title or license or not, by natural or jurídical
  persons — the NOTARIADO function being a liberal profession; o) lease,
  sublease, concession or any form of cession of use or enjoyment of
  marks, invention patents, industrial procedures or formulas and similar
  services (royalties); p) payment of *dietas* (director's fees) or any
  other emolument of equal or similar nature — EXCLUDING dietas governed
  by labor legislation and services of public, municipal and
  autonomous-institution employees and functionaries; q) payment of
  membresías, cuotas or any similar payment generating consideration for
  the use, enjoyment or disposal of goods or services, regardless of how
  received. The catalog is seeded OPEN ("se señalan entre ellas") — the
  general onerous-non-transfer classification is always available.
  (LB-016; EVID-309)
- **SV-TAX-FR-193:** The system shall assimilate *reintegros o
  reembolsos de gastos* (expense reimbursements) to service prestations,
  taxed AT THE MOMENT OF THEIR PAYMENT — not at document or completion —
  with two exception gates that keep a reimbursement OUT of IVA: (a)
  reimbursements of seguros (insurance), alimentación (food) and viáticos
  (travel allowances) received by trabajadores (workers); and (b)
  reimbursements meeting the Art. 51 literal a) mandate exception, ALWAYS
  PROVIDED the mandatario had NOT deducted créditos fiscales in relation
  to those sums (the no-credit-deduced condition verified on the
  reimbursement line).
  (LB-016; EVID-309)

### 3.5 Service tax points and territoriality (Arts. 18-19)

- **SV-TAX-FR-194:** The system shall fix the service tax point at the
  EARLIEST of: a) emission of any of the documents the law señala
  (Arts. 97/100 as printed — repealed anchors, re-anchored to the CT
  document regime, OQ-3); b) término de la prestación; c) delivery of the
  good object of the lease, sublease, use or enjoyment; d) delivery or
  placing at disposal of the good or obra where the prestación includes
  one; e) total payment of the consideration, EACH partial payment, credit
  to account or placing at the prestador's disposal — total or partial,
  EVEN IN ADVANCE of the prestación (advance/deposit lines carry the
  débito trigger at receipt).
  (LB-017; EVID-310)
- **SV-TAX-FR-195:** For permanent, regular, continuous or periodic
  service supplies, the system shall cause the tax at the earliest of any
  Art. 97 document emission OR the término of each period established for
  payment — whichever happens first, INDEPENDENTLY of the payment date;
  and for leases with purchase option or sale promise, at the moment the
  lease *cánones* become exigible or the sale perfects (two independent
  triggers, earliest governs).
  (LB-017; EVID-310)
- **SV-TAX-FR-196:** The system shall territorialize services by the
  direct-performance test — taxed when rendered directly in the country,
  regardless of where the contract perfected or where the remuneration is
  paid or perceived; the service is rendered in the national territory
  when the ACTIVITY generating it is developed in the country; partial
  in-country rendition ⇒ only the tax corresponding to the in-country PART
  (proportional flag with factor); BUT full taxation when the services are
  rendered in the country though not exclusively used there — the
  statutory exemplar being services related to goods, transports or
  cargoes IN TRANSIT (in-transit flag ⇒ full); and foreign-transport
  services already taxed when added to the import base per Art. 48-g
  shall NEVER be taxed again (no-double-tax guard against the import
  base).
  (LB-018; EVID-310)

### 3.6 Sujetos pasivos and contribuyentes (Arts. 20-27)

- **SV-TAX-FR-197:** The system shall model as sujetos pasivos: natural or
  jurídical persons; *sucesiones* (estates); nulas, irregular or de hecho
  societies; *fideicomisos* (trusts); asociaciones cooperativas; and the
  unión de personas, asocios, consorcios or whatever their denomination
  (stamp 11); PLUS government-central and decentralized or autonomous
  public entities when realizing the hechos — NOTWITHSTANDING laws
  exempting them from every class of contribution — SAVE when they realize
  *actividades bursátiles* (securities-market activities); and shall
  attribute sujeto-pasivo quality to whoever acts in their OWN name (own
  account or a third party's), while when acting in a third party's name
  the REPRESENTED tercero/mandante assumes it; subjects lacking legal
  personality act through their integrantes, administradores or
  representantes.
  (LB-019; EVID-311)
- **SV-TAX-FR-198:** The system shall classify contribuyente status per
  the operation family: goods transferors — productores, comerciantes
  mayoristas or al por menor or ANY other quality, acting within their
  giro or habitually, through themselves or mandatarios at their name, in
  onerous transfers of new or used bienes muebles corporales — plus
  transferors of materias primas or insumos not utilized in the
  productive process, plus transferors of desechos, desperdicios and
  residuos whether or not obtained from the productive process (Rgto.
  Art. 8); NOT contribuyentes — occasional transferors of goods acquired
  without resale intent; importers — contribuyentes WHETHER OR NOT
  habitual (any definitive import makes one); service renderers —
  contribuyentes when acting habitually AND onerously.
  (LB-020; LB-026; EVID-311/334)
- **SV-TAX-FR-199:** The system shall seed habitualidad as DGII's
  calification over the nature, quantity and frequency of the operations —
  and, where applicable, the acquisition intent (use/consumption vs
  resale) — with TWO CONCLUSIVE presumptions (*presunción de derecho*,
  admitting NO proof in contrario): habitualidad exists for the hechos
  constituting the contribuyente's objeto social or main giro or
  activity, and for Código de Comercio merchants' acts of commerce; the
  DGII calification itself admits contrary proof only through
  remonstration against the determination (a recorded ground
  `presumed_de_derecho` locks the flag against taxpayer-side rebuttal).
  (LB-021; EVID-311)
- **SV-TAX-FR-200:** The system shall treat a local casa matriz with
  sucursales or agencias as ONE taxpayer — capacity and responsibility as
  contribuyente radicated in the matriz, a single fiscal identity and a
  single determination across all establishments (the
  establishments/points-of-sale split is operational only — D14
  single-taxpayer-across-establishments kin; warehouse/cash-register
  mapping per the go-live readiness surface, never a per-branch
  taxpayer).
  (LB-022; EVID-311)
- **SV-TAX-FR-201:** For agrupamientos of Art. 20 subjects organized for
  a specific or particular business or operation WITHOUT own legal
  personality, the system shall radicate the substantive and formal
  obligations in the REPRESENTANTE or ADMINISTRADOR — and, failing them,
  in the asociados, partícipes or integrantes, who respond SOLIDARIAMENTE
  (jointly and severally) for the agrupamiento's tax debts (solidarity
  flag on the grouping record with the responsible-partner designation).
  (LB-022; EVID-311)

### 3.7 The excluidos regime (Arts. 28-32; Rgto. Arts. 9-10)

- **SV-TAX-FR-202:** The system shall encode the Art. 28 exclusion as a
  TWO-THRESHOLD CONCURRENCE (Rgto. Art. 9: both Art. 28 requisites must
  concur): prior-12-month transfers of goods/services — gravadas AND
  exentas — under fifty thousand colones AND total activo under twenty
  thousand colones; the thresholds ship as DATED-HISTORICAL rows in 1992
  colones [sic — never updated in the text], currency-flagged historical,
  with the administered exclusion criteria ABSENT from the corpus
  (SOQ-55/MOQ-03 config-gap: registration/NRC practice — configurable
  monitored criteria, NO invented USD conversion, per S5 ruling 39
  discipline); the activo measure follows the Rgto. Art. 2 num. 18
  activo-en-giro definition (losses and accounting-only active accounts
  excluded).
  (LB-023; LB-026; EVID-312/335/333)
- **SV-TAX-FR-203:** The system shall flip an excluido to contribuyente
  status effective the MONTH SUBSIGUIENTE to the month either threshold is
  crossed (either transfers or activo — the concurrence breaks), with the
  DGII inscription de oficio or on petition recorded as the registration
  event; the exclusion NEVER applies to sociedades or to importadores,
  nor where the contribuyente holds more than one local whose AGGREGATE
  exceeds the limits (multi-local aggregation check); start-ups are
  excluded while their INITIAL total activo is under the twenty-thousand
  threshold — NEVER for imports/internations.
  (LB-023; EVID-312/335)
- **SV-TAX-FR-204:** The system shall implement the opción: an excluded
  subject may assume contribuyente status voluntarily — effective the
  first of January of the FOLLOWING calendar year, with DGII empowered to
  authorize entry at ANY time (discretionary earlier entry recorded with
  its authorization reference) — and shall demand the Rgto. Art. 10
  evidence set for the opción: the Registro-de-Comercio-authorized *libro
  de gastos, compras y ventas* ["conpras" sic as printed] plus a valued
  inventory of goods (or DGII-established means).
  (LB-024; EVID-312/335)
- **SV-TAX-FR-205:** For excluido subjects the system shall: (a) NEVER
  generate crédito fiscal from IVA recargado to them on acquisitions nor
  from IVA paid on their imports/internations (Art. 31 — no credit, no
  translation of credit, per the Art. 65 crossref owned by the credit
  file), and never trasladar credit-deducible IVA in their own operations;
  and (b) emit their invoices or equivalent documents with the operation
  price SIN NINGÚN RECARGO a título del impuesto — the system shall
  REJECT any IVA tax line on an excluido-emitted invoice, enforcing
  through the FSEE document type (`e-invoicing/01_dte-types.md`
  SV-EINV-FR-048; FSEE = type 14 per SV-EINV-FR-001 — by id); purchases
  FROM excluidos flow to the F-07 Anexo 5 surface
  (`fiscal-reporting/03_f07-annexes-purchases.md` SV-FREP-FR-086 — CT-119
  zone, by id).
  (LB-025; EVID-312; EINV 01-file SV-EINV-FR-048/001; FREP 03-file
  SV-FREP-FR-086)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the Art. 28 colones thresholds enter as [sic]
dated-historical config rows with the SOQ-55 config-gap noted in OQ-2 —
administered criteria are a configuration surface, never an invented
conversion. The only version regime is the D.L. 645-2005 authentic
interpretation (effective 2005-03-26, eight days after the 18-Mar-2005
publication — a behavior note on the import-service test, not a table
vintage) and the SOQ-54 consolidation watch riding every legal parameter.
Layer semantics: this file introduces Odoo-side classification/timing/
subject data only (wave default `odoo`; see §5). **Interface entity for
the wave's later files (base/rate, determination, credit) and Task 7's
index:** the IVA operation taxonomy + tax-point snapshot + subject-category
fields below.

**Operation taxonomy and classification:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.operation.type (new) | code, name, legal_anchor | char / char / char | Art. 1 kinds (transferencia · importacion · internacion · exportacion · consumo · prestacion_servicio · autoconsumo) + Art. 7 letters a)-m) + Art. 11 retiro + Art. 14 import + Art. 17 letters a)-q) — anchor string per row | FR-176, FR-179, FR-192 |
| l10n_sv.iva.operation.type | kind, letter, open_list | select / char / boolean | kind: transfer · retiro · import_internacion · service · export; letter: a..m (Art. 7) / a..q (Art. 17) / null; open-list rows for Art. 7-l catch-all and general Art. 17 | FR-179, FR-192 |
| product.template (SV extension) | l10n_sv_iva_operation_type_id | m2o | default operation type per product (service letters, import-service exemplars as hints) | FR-177, FR-192 |
| product.template (SV extension) | l10n_sv_iva_mutuo_financiamiento | boolean | mutuos dinerarios / créditos en dinero / financiamiento → forced service classification (Art. 5 inciso 3) | FR-177 |
| account.move.line (SV extension) | l10n_sv_iva_operation_type_id, l10n_sv_iva_new_contract_intent | m2o / boolean | per-line operation type; return routing to the Art. 62-1-a path unless new-contract intent proven | FR-178, FR-181 |

**Tax point (snapshot — D15):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (SV extension) | l10n_sv_iva_tax_point_date | date (computed, stored) | earliest trigger per operation kind; snapshot — corrections keep original-period parameters | FR-180, FR-186, FR-189, FR-194, FR-195 |
| account.move (SV extension) | l10n_sv_iva_tax_point_source | select | document · payment · delivery_real_symbolic · consignatario_act · retiro_date · import_moment · prestador_doc · payment_import · termino_prestacion · period_end · canone_exigibilidad · sale_perfection · reimbursement_payment | FR-180, FR-186, FR-189, FR-193, FR-194, FR-195 |
| account.move.line (advance/deposit) | l10n_sv_iva_advance_trigger | boolean | payment/credit-at-disposition lines carry the débito trigger aunque sea con anticipación | FR-194 |

**Retiro engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.stock.usage (SV extension) | l10n_sv_retiro_kind | select | propio · socio · directivo · personal · grupo_familiar · tercero · rifa_sorteo · promocional · inventory_shortfall_presumed | FR-183, FR-184 |
| account.stock.usage (SV extension) | l10n_sv_fuerza_mayor_evidence | refs / m2m | menu: permanent_inventory_chronological_annotation · denuncia_policial_tribunal · insurance_liquidation_report · recognized_merma | FR-184 |
| account.stock.usage (SV extension) | l10n_sv_fuerza_mayor_accounting_date_ok | boolean (validated) | precondition: quantities/values accounted on the loss dates | FR-184 |
| account.stock.usage (SV extension) | l10n_sv_no_retiro_ground | select | realizable_to_fijo_giro_necessary · giro_normal_activity_use · isr6c_donation (with calificación ref) | FR-185 |
| account.move (retiro invoice, auto) | l10n_sv_retiro_consumidor_final, l10n_sv_retiro_base_source | boolean / select | factura as consumidor final (Rgto. Art. 20); base source: assigned_public_price_records · precio_corriente_mercado (Art. 48-c pointer) | FR-186 |

**Imports:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (import) | l10n_sv_iva_import_kind | select | good_definitive · service_import · aduana_auction | FR-187 |
| account.move (import, services) | l10n_sv_iva_exclusive_sv_use | boolean | D.L. 645: utilization exclusively in SV (blocks import classification when false) | FR-188 |
| account.move (import) | l10n_sv_iva_customs_clock_id, l10n_sv_iva_definitive_conversion_event | m2o / event | SR4 clock link (`l10n_sv_special_regime.customs_clock` — SV-SPE-FR-064/066 by id); free-disposability devengo event (full or difference) | FR-190 |

**Subjects:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner (SV extension) | l10n_sv_iva_subject_kind | select | persona_natural · persona_juridica · sucesion · sociedad_nula_irregular_hecho · fideicomiso · cooperativa · union_asocios_consorcio · government_entity (bursátiles-exception flag) | FR-197 |
| res.partner (SV extension) | l10n_sv_iva_habitualidad_source | select | presumed_de_derecho_objeto_social · presumed_de_derecho_cc_merchant · dgii_calification (remonstration-proof only) | FR-198, FR-199 |
| res.company (SV extension) | l10n_sv_iva_matriz_sucursales | boolean + matriz ref | ONE taxpayer: capacity radicated in the local matriz (D14 kin) | FR-200 |
| res.partner (agrupamiento) | l10n_sv_iva_grouping_responsibility | select + m2m | representante_administrador responsible; else asociados/partícipes/integrantes solidarios | FR-201 |

**Excluidos:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.exclusion.threshold (new) | valid_from, currency, transfers_limit, activo_limit, status | date / char / monetary / monetary / select | 1992-09-01 · CRC [sic historical] · 50000 · 20000 · historical_sic_config_gap (administered criteria absent — SOQ-55) | FR-202 |
| res.partner (SV extension) | l10n_sv_iva_exclusion_state | select | excluido · contribuyente · option_pending; monitored rolling-12m transfers + activo (configurable criteria); flip effective the month subsiguiente | FR-202, FR-203 |
| res.partner (SV extension) | l10n_sv_iva_option_date, l10n_sv_iva_option_effective, evidence refs | date / select / refs | opción effective next Jan-1 (dgii_anytime with authorization ref); Art. 10 evidence: libro de gastos/compras/ventas (RC-authorized) + inventario valorado | FR-204 |
| res.partner (SV extension) | l10n_sv_iva_no_credit_lock + invoice line guard | boolean | Art. 31 no crédito ever; Art. 32 guard rejects any IVA line on excluido-emitted invoices (FSEE by id) | FR-205 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = classification/timing/subject
computation logic living in the LGPL client. No SaaS rows are introduced
in this file: nothing here touches DTE generation/transformation (the only
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2) — the FSEE emission
itself is the e-invoicing file's row (SV-EINV-FR-048, cited by id); this
file supplies the excluido status and the no-IVA-line rule the client and
the DTE layer both consume. Model names are stable across Odoo
17/18/19/20 (`account.move`, `account.move.line`, `product.template`,
`res.partner`, `res.company`; `account.stock.usage` exists in core
inventory accounting for goods usage — the retiro engine rides it with SV
extension fields); version-specific behavior is recorded per row where a
legal vintage exists. D15 doctrine (binding): every IVA parameter resolves
as-of the tax-point date snapshotted on the record; corrections use
ORIGINAL-period parameters — the tax-point snapshot fields of §4 are the
anchor.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-176 | odoo | l10n_sv.iva.operation.type + account.move.line | operation-kind enum | Art. 1 taxonomy root; Art. 2 coexistence — no exclusion vs special taxes (SR8 guards consume, by id) |
| FR-177 | odoo | product.template | mutuo_financiamiento flag | Money loans/credit/financing = SERVICES; títulos valores = incorpóreos save Art. 7-d |
| FR-178 | odoo | computation guard | — | Substance-over-form classifier; label/contract-name never bypasses |
| FR-179 | odoo | l10n_sv.iva.operation.type | Art. 7 a)-m) seed | FULL catalog, no letter dropped; (h) carve-out = same-socio aportante + not-charged good (both required); open list via letter l |
| FR-180 | odoo | account.move | tax_point_date + source | Earliest of document/payment/delivery; consignment at consignatario's acts; caused despite mora/non-final price; D15 snapshot |
| FR-181 | odoo | account.move.line | return_path + new_contract_intent | → Art. 62-1-a deduction (determination file, LB-028 pointer); 3-month window owned there |
| FR-182 | odoo | computation | situados/matriculados/registrados test | Contract venue and transient placement abroad irrelevant; shipped-to-non-contribuyente = situados in SV |
| FR-183 | odoo | account.stock.usage | retiro_kind enum | Destinations incl. grupo familiar + terceros (Rgto. Art. 4) and rifa/promo sea o no del giro |
| FR-184 | odoo | account.stock.usage | fuerza_mayor_evidence + accounting_date_ok | Shortfall presumed retiro unless Rgto. Art. 4 menu evidence with the accounting-date precondition |
| FR-185 | odoo | account.stock.usage | no_retiro_ground | realizable→fijo giro-necessary; ISR-6-c donation with calificación ref |
| FR-186 | odoo | account.stock.usage → account.move (auto) | retiro invoice consumidor final | Tax at retiro date (Art. 12); Art. 13 situs; Rgto. Art. 20 factura; base per Art. 48-c pointer (V3 file owns computation) |
| FR-187 | odoo | account.move (import) | import_kind | Definitive import of goods AND services; aduana auctions = import acts |
| FR-188 | odoo | account.move (import) | exclusive_sv_use | D.L. 645 interpretation (effective 2005-03-26): utilization exclusively in SV; boundary with Art. 19 partial = OQ-4 |
| FR-189 | odoo | account.move (import) | tax_point_source | Goods: import moment; services: earliest of prestador document/payment/término |
| FR-190 | odoo | account.move (import) + customs_clock link | definitive_conversion_event | Full-or-difference devengo at free disposability; trigger feed = SPE 04-file SV-SPE-FR-064/066 (by id) |
| FR-191 | odoo | account.move.line | service hecho-generador gates | Autoconsumo incl. grupo familiar/terceros (Rgto. Art. 5); indemnizaciones and qualified donations out |
| FR-192 | odoo | product.template + l10n_sv.iva.operation.type | Art. 17 a)-q) seed | FULL catalog, no letter dropped; notariado = liberal profession (n); labor-law dietas and public-employee services out (p); 46-b/46-i exemption surfaces by pointer |
| FR-193 | odoo | account.move.line (reimbursement) | reintegro gates + payment trigger | Taxed at payment; exceptions: seguros/alimentación/viáticos of trabajadores; Art. 51-a mandate with no-credit-deduced condition |
| FR-194 | odoo | account.move | tax_point_source | Earliest of a)-e incl. advances/acreditación-en-cuenta; Art. 18-a document anchors repealed → CT re-anchor (OQ-3) |
| FR-195 | odoo | account.move | period_end / canone_exigibilidad | Permanent/periodic: document or period-end first, regardless of payment; leasing: exigibilidad or sale perfection |
| FR-196 | odoo | account.move.line | territorial flags | Partial ⇒ proportional; in-transit ⇒ full; foreign transport in import base never re-taxed (48-g guard) |
| FR-197 | odoo | res.partner | subject_kind enum | a)-f) incl. unions/consorcios; government entities notwithstanding exemptions, save bursátiles; representation attribution |
| FR-198 | odoo | res.partner | contribuyente classification | Transferors habitual; importers habitual-or-not; services habitual+onerosa; desechos transferors in (Rgto. Art. 8); occasional sellers out |
| FR-199 | odoo | res.partner | habitualidad_source | Presunción de derecho (objeto social / CC merchants) locks the flag — no proof in contrario; DGII calification reversible only via remonstration |
| FR-200 | odoo | res.company | matriz_sucursales | ONE taxpayer (Art. 26); establishments/points-of-sale operational only — D14 kin |
| FR-201 | odoo | res.partner | grouping_responsibility | Representante/administrador; else asociados solidarios (Art. 27) |
| FR-202 | odoo | l10n_sv.iva.exclusion.threshold | [sic] CRC historical rows | Two-threshold concurrence (Rgto. Art. 9); config-gap for administered criteria (SOQ-55); NO USD conversion invented |
| FR-203 | odoo | res.partner | exclusion_state monitor | Month-subsiguiente flip; sociedades/importadores/multi-local aggregate carve-outs; start-ups never for imports |
| FR-204 | odoo | res.partner | option_date/effective/evidence | Next Jan-1 default; DGII anytime with authorization; Rgto. Art. 10 libro + inventario valorado |
| FR-205 | odoo | res.partner + account.move guard | no_credit_lock + line guard | Art. 31 no crédito ever; Art. 32 no-IVA-line guard; FSEE enforcement = EINV 01-file SV-EINV-FR-048 (by id); Anexo 5 feed = FREP 03-file SV-FREP-FR-086 (by id) |

Version-regime notes (D12/D15): FR-188 records the D.L. 645-2005
authentic-interpretation cutover (effective 2005-03-26 — eight days after
the 18-Mar-2005 D.O. publication; service imports before that date apply
the uninterpreted Art. 14-III text — dated behavior note). FR-180/186/189/
194/195 carry the D15 snapshot doctrine: tax-point-dated resolution with
original-period correction parameters. The Art. 28 colones thresholds
(FR-202) carry the SOQ-55 config-gap regime: dated-historical [sic] rows,
administered criteria as configuration, never an invented conversion. The
SOQ-54 consolidation watch rides every LB (§2 preamble) — re-verify
against a current official consolidation at implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a product configured as *mutuo dinerario* (money
  loan) of $10,000.00, when the operation is classified, then it resolves
  as PRESTACIÓN DE SERVICIOS — never as a goods transfer — and the
  service regime (Arts. 16-19) applies to it (FR-177).
- **AC-002:** Given a contributor aporting own-giro machinery worth
  $15,000.00 to a sociedad (Art. 7-f aportación), when the aportación is
  recorded, then it is classified as a TAXED transfer operation (FR-179).
- **AC-003:** Given a society in liquidation adjudicating a good to the
  SAME socio who aportó it, where the good was NOT IVA-charged when
  aportado, when the adjudication is classified, then NO gravamen applies
  (Art. 7-h carve-out — both conditions met); given instead a different
  adjudicatario or a previously charged good, then the adjudication is a
  taxed transfer (FR-179).
- **AC-004:** Given goods delivered on consignment, when the consignatario
  emits the delivery document (before any payment or third-party
  delivery), then the tax is caused AT THAT MOMENT; given instead the
  consignatario first pays or delivers to the buyer, then the earliest of
  those acts causes it (FR-180).
- **AC-005:** Given a sale where the price is paid before any document is
  emitted, when the payment posts, then the tax point is the PAYMENT date
  (earlier-trigger rule) and the later document emission does not move it
  (FR-180).
- **AC-006:** Given a buyer returning damaged goods within three months
  of delivery with no new-contract intent proven, when the return is
  recorded, then NO new transfer is generated and the operation routes to
  the Art. 62-1-a débito deduction path (LB-028 pointer); given the
  new-contract intent flag set, then a fresh taxed transfer is generated
  (FR-181).
- **AC-007:** Given a vehicle registered (matriculado) in El Salvador
  sold under a contract celebrated abroad while the vehicle sits
  transiently abroad, when territoriality resolves, then the transfer is
  TAXABLE (situados/matriculados/registrados test) (FR-182).
- **AC-008:** Given goods embarked from the country of provenance to an
  acquirer who is NOT a contribuyente, when the embarkation fact is
  recorded, then the goods are deemed SITUADOS in El Salvador and the
  transfer is taxable (FR-182).
- **AC-009:** Given a warehouse shortfall of $2,500.00 with NO Rgto.
  Art. 4 evidence recorded, when the inventory closes, then the shortfall
  posts as a PRESUMED retiro (taxable); given instead a chronological
  permanent-inventory annotation tied to the accounting AND the loss
  values accounted on the loss dates, then the shortfall is fuerza mayor
  and NOT a retiro (FR-184).
- **AC-010:** Given a raffle prize of goods NOT of the company's giro,
  when the raffle retiro is recorded, then it is TAXED as retiro (sean o
  no del giro) with kind `rifa_sorteo` (FR-183).
- **AC-011:** Given goods moved from activo realizable to activo fijo
  that are necessary for the giro, when the transfer posts, then NO
  retiro is generated (ground `realizable_to_fijo_giro_necessary`)
  (FR-185).
- **AC-012:** Given a retiro by a socio's family member (grupo familiar)
  of goods with an assigned public-sale price of $130.00 in the records,
  when the retiro executes, then the system causes the tax at the RETIRO
  DATE and auto-emits a consumidor-final FACTURA (never a CCF) with base
  $130.00 — or, absent an assigned price, the precio corriente de mercado
  (Art. 48-c pointer) (FR-183, FR-186).
- **AC-013:** Given a foreign-rendered software-license service
  (programas de computación exemplar) billed to a domiciled SV user and
  utilized exclusively in El Salvador, when classification runs, then it
  is a SERVICE IMPORT (D.L. 645 exclusive-use test passed) and the tax
  point is the EARLIEST of prestador document, payment or término — an
  advance payment made first fixes it (FR-188, FR-189).
- **AC-014:** Given goods under a special customs regime whose clock
  expires converting the import into definitive (SR4 clock event, by id),
  when the goods reach free disposability, then the tax devengas IN FULL
  (or by the difference where duties were partially covered) at that
  moment (FR-190).
- **AC-015:** Given a periodic cleaning contract (permanent service) with
  monthly $1,000.00 periods, when January ends with no document emitted
  and payment received only in March, then the tax is caused at the
  JANUARY period-end (término de cada período), independently of the
  payment date (FR-195).
- **AC-016:** Given an advance deposit of 50% on a future service
  prestación, when the advance is received, then the débito trigger fires
  AT RECEIPT (aunque sea con anticipación) (FR-194).
- **AC-017:** Given a consulting service rendered 60% in-country and 40%
  abroad, when territoriality resolves, then only the 60% in-country part
  is taxed; given the same service related to cargo IN TRANSIT though
  used partly abroad, then the FULL service is taxed; given a
  foreign-transport charge already inside an Art. 48-g import base, then
  it is NEVER taxed again (FR-196).
- **AC-018:** Given a company with a San Salvador matriz and three
  sucursales, when fiscal identity resolves, then all four establishments
  constitute ONE taxpayer with capacity radicated in the matriz — a
  single determination, never four (FR-200).
- **AC-019:** Given an excluido whose trailing-12-month operations cross
  a monitored exclusion criterion in March, when the flip runs, then the
  partner becomes a contribuyente effective APRIL (the month
  subsiguiente) with the DGII inscription event recorded (FR-203).
- **AC-020:** Given an excluido emitting an invoice, when any IVA tax
  line is added, then the system REJECTS the line (sin ningún recargo)
  and the document resolves as FSEE (type 14 — e-invoicing file's
  surface, by id); given an excluido's purchase carrying recargado IVA,
  then NO crédito fiscal is ever generated from it (FR-205).
- **AC-021:** Given a reimbursement of $150.00 for a worker's viático,
  when the expense line posts, then NO IVA applies (labor exception
  gate); given a generic $150.00 client-expense reimbursement under a
  mandate where the mandatario deducted no créditos fiscales on those
  sums and the Art. 51-a exception is met, then NO IVA applies; given a
  generic reimbursement failing both gates, then it is taxed as a service
  AT ITS PAYMENT (FR-193).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 1-32 + the Rgto. survivors cited here at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | SOQ-55 (MOQ-03 resolution — colones thresholds config-gap): Arts. 28-29 thresholds print 1992 colones values never updated in the text; the administered exclusion criteria (registration/NRC practice) are outside the corpus. FR-202 encodes [sic] dated-historical rows + configurable monitored criteria with NO invented USD conversion (S5 ruling 39 discipline). Onboarding must configure the real administered criteria before the exclusion monitor is trusted; MOQ-03 closes as this footnote-OQ. | no | Takumi S9 + Odoo implementation | open |
| OQ-3 | Art. 18-a anchors the service document tax point on "los artículos 97 y 100 de esta ley" — both DEROGADO by D.L. 230/00; the operative document set is now the CT document regime (CT Arts. 110-115 zone) overlaid by the DTE stack (44_/45_: FE/CCFE emission). Confirm the exact live document events that start the a) trigger (DTE emission? contingency rules?) before wiring FR-194's document source. | no | Takumi S9 (CT re-anchor pass) | open |
| OQ-4 | Exclusive-use vs proportionality boundary: D.L. 645 requires SV utilization *exclusivamente* for the SERVICES-IMPORT test (Art. 14-III), while Art. 19 taxes partial in-country rendition proportionally (save the in-transit full rule). For a service rendered partly abroad and used partly in SV by a domiciled user, FR-188 blocks import classification while FR-196 would tax the in-country part as a domestic prestación — confirm the intended overlap (import blocked + domestic partial taxation, or a single exclusive-use gate) with DGII practice before final wiring. | no | Takumi S9 | open |
| OQ-5 | Exclusion measurement mechanics: the 12-month transfers figure (gravadas + exentas) and the "total de su activo" (Rgto. Art. 2 num. 18 activo-en-giro definition) need measurement conventions — valuation basis for transfers at threshold check, activo measurement date, and the rolling-window aggregation for multi-local subjects; FR-203 implements the flip mechanics, the measurement basis rides the OQ-2 configurable criteria (no statutory USD-era guidance in corpus). | no | Takumi + Odoo implementation | open |

