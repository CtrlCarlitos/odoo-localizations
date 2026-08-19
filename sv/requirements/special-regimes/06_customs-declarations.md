# SV — Special regimes — Customs declarations: DUCA record model, teledespacho, tasa, valuation, courier

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes) |
| Updated | 2026-08-19 |

## 1. Purpose

This file owns the customs-DECLARATION surface the regime waves move goods
on: the *Declaración Única Centroamericana* (Single Central American
Declaration, DUCA — 43_) record model — ONE model with a variant flag for
its three printed types (DUCA-D terceros países / DUCA-T *tránsito aduanero
internacional terrestre* / DUCA-F originarios de la región centroamericana),
header blocks (declarante correlativo + system-assigned registration number
+ *fecha de aceptación*; exportador/proveedor, importador/destinatario and
declarante identity blocks; aduanas registro/salida/ingreso/destino;
régimen aduanero + modalidad + clase de declaración; **fecha de
vencimiento del régimen** — the field `04_customs-clocks.md` consumes by
id; países; depósito aduanero/zona franca code; transportista/conductor/
medio blocks with marchamos and container IDs), the value block 25-29
(*valor en aduana* total = the tax base) with INCOTERM (30) and the
peso-centroamericano exchange rate (31 — SOQ-45 config-gap), lines with
per-line value + *liquidación*, soporte documents with their line-range
syntax, and the *declaración de origen* (producer) vs *certificación de
origen* (exporter) complementarity; the DUCA-F FAUCA-validity
declaration-record surface (30 días hábiles, export-country only — clock
view consumed from `04` by id); the teledespacho legal chassis (74_ Arts.
6/8: electronic transmission with authenticity/confidentiality/integrity/
no-repudiation; data messages = paper legal effects; digital signature via
*entidades certificadoras*; auxiliaries' key-confidentiality duty); the
$18 non-intrusive-inspection *tasa* (74_ Art. 12-B — IVA-included,
despacho-blocking, due at transmission, biennial ≤10% revision watch); the
presumed-valuation fallback rows (74_ Art. 2: seguro 1.25%/1.50% FOB,
flete 10% FOB or DGA periodic reference values — dated config rows feeding
fields 26/27) and the pre-arrival manifiesto duty; autoliquidación +
selectividad aleatoria + non-intrusive images as *plena prueba*; the
payment/anulación clocks (pre-transfer DM presentation + payment; 8 días
hábiles; 10-day teledespachada-unpresented; 60-day paid-unpresented with
devolución route); the 48-hour simplified withdrawal and the courier FOB
bands $200/$3,000; the fiscalización surfaces (5-year records/origin-
certificate retention, 5-year verification *caducidad* per DM, electronic
notification with agent-notification extension, 15/20-días-hábiles
alegatos/resolution clocks, recursos per LESIA pointer); and the dated
SIECA/Panamá DUCA-F interchange note (42_ — 2025-03-03, ducaf.sieca.int,
tokens, ~37-second acceptance).

It does **not** cover: the regime clocks the DUCA field 14 feeds
(`04_customs-clocks.md` — SV-SPE-FR-064..081 by id, esp. FR-080/081); the
TAN/IVA fiscal routing of declared goods (`05_tan-iva-interface.md` — its
SS-solvency gate SV-SPE-FR-102 gates this file's withdrawals by id); the
declarante-role config and consultas/advance-ruling registry
(`01_regime-framework.md` — SV-SPE-FR-020/021 by id); the descargo
registers and SMM-priced sanctions (`07_obligations-reporting-sanctions.md`);
FOVIAL/COTRANS (`08_fovial-cotrans.md`); the canonical retention matrix
(`commercial-legal/02_accounting-books.md` §3.7 SV-CML-FR-028 — the customs
5y row lands there as an update-by-note, never a restatement); and the
días-hábiles engine (SV-FREP-FR-202..204 by id). The DGA transmits and
accepts — the system mirrors, gates and tracks; it never emulates the
authority's systems.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): customs
chassis = **74_** (D.L. Nº 529, 13-ene-1999, D.O. N° 23 T.342 3-feb-1999;
consolidated through reform (4) D.L. 23-2012, D.O. N° 123 T.396 4-jul-2012;
sentence-case print); DGA frame = **13_** (D. Nº 903, 14-dic-2005, D.O.
Nº 8 T.370 12-ene-2006; consolidated through reform (2) D.L. 121-2012) —
cited here only as the institutional frame already anchored by
`01_regime-framework.md` (SV-SPE-FR-005 by id); DUCA = **43_** (Anexo II
de la Resolución No. 409-2018 (COMIECO-LXXXV), *Instructivo de llenado de
la Declaración Única Centroamericana*; 2018 print assumed current —
SOQ-36); SIECA/Panamá operational note = **42_** (CIEX/BCR/DGA
comunicado; implementation 03-mar-2025 — dated operational fact, not a
statute).

**SOQ-30 verification note (rides EVERY regime LB in this file):** the 74_
consolidation ends at D.L. 23-2012 (reforms 1) D.L. 523-2001, 2) D.L.
490-2004, 3) D.L. 906-2006, 4) D.L. 23-2012) and 43_ is the 2018 print —
post-cutoff reforms and the Res. 409-2018 supersession status are
unverified until official routes recover (SOQ-22 kin; SOQ-36); article
text is cited **as printed**. Verbatim text below is copied from the W13
evidence files (EVID-269..273) and, where the evidence abbreviates, from
the extraction txts
`sv/.extractions/74_Ley_Simplificacion_Aduanera_D529.pdf.txt`,
`sv/.extractions/43_DUCA_Instructivo_COMIECO.pdf.txt` and
`sv/.extractions/42_Comunicado_Exportaciones_Panama.docx.txt` (citable per
standing S3 ruling 25; page pointers = txt PAGE markers). D15 discipline:
the $18 tasa, the presumed percentages and every clock/window in this file
are dated config rows with instrument provenance — never global constants;
each resolves as-of its domain anchor (transmission date for the tasa; DM
acceptance for valuation and caducidad; notification for payment clocks;
emission for the DUCA-F FAUCA validity) and snapshots on the record.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Instructivo DUCA (43_), opening + types + closing note: "La Declaración Única Centroamericana (DUCA) está conformada por el conjunto de datos que integran las funciones asignadas al Formulario Aduanero Único Centroamericano (FAUCA), la Declaración de Mercancías (DM) y la Declaración Única de Mercancías para el Tránsito Aduanero Internacional Terrestre (DUT), los cuales serán empleados de conformidad con la naturaleza de la operación y el régimen aduanero al que se sometan las mercancías. Cuando se imprima la DUCA, se deberá presentar sin ningún tipo de alteración. El formato de impresión de la DUCA, será distinguido de acuerdo al tipo de operación, de la manera siguiente: 1. DUCA-D: para las mercancías originarias de terceros países y las que no apliquen DUCA-F. 2. DUCA-T: para las mercancías en tránsito aduanero internacional terrestre. 3. DUCA-F: para las mercancías originarias de la región centroamericana. Cuando sea necesario, podrá disponerse de hojas de ampliación de información. … Los campos descritos a continuación, serán utilizados según el tipo de operación que se desee realizar." Closing (p.11): "El Comité Aduanero indicará en el manual del usuario de la DUCA los ca[mpos] que serán llenados de forma obligatoria y optativa." (reverso of the DUCA = "de uso exclusivo de la Autoridad Aduanera") | The DUCA is formed by the data set integrating the functions assigned to the FAUCA (Central American Single Customs Form), the DM (goods declaration) and the DUT (Single Declaration for International Land Customs Transit), employed per the nature of the operation and the customs regime; when printed, the DUCA is presented WITHOUT ANY ALTERATION. Print format distinguished by operation type: 1. DUCA-D — goods originating in third countries and those not taking DUCA-F; 2. DUCA-T — goods in international land customs transit; 3. DUCA-F — goods originating in the Central American region. Ampliation information sheets available when necessary; fields are used per the operation type. The Comité Aduanero's user manual states which fields are mandatory and optional (manual NOT in corpus — SOQ-36); the DUCA reverse side is for exclusive use of the customs authority | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | pp.1, 11 (EVID-272; txt PAGE 1, 11; 2018 print assumed current — SOQ-36) |
| LB-002 | Instructivo DUCA (43_), fields 1-6: 1. "No. de correlativo o referencia asignado por el declarante a la DUCA: … el número correlativo o referencia que el declarante o su representante le asigna a la declaración transmitida." 2. "Número de registro de la DUCA asignado por el sistema: … el número correlativo asignado a la declaración por el sistema informático del Servicio Aduanero." 3. "Fecha de aceptación o registro: … la fecha en que el sistema informático del Servicio Aduanero válida y registra la declaración transmitida por el Declarante o su Representante." 4. "Exportador/proveedor" (4.1 número de identificación — registro tributario o de identificación; 4.2 tipo de documento de identificación; 4.3 país de emisión del documento; 4.4 nombre o razón social; 4.5 domicilio fiscal). 5. "Importador/destinatario" (5.1-5.5 same structure). 6. "Declarante/auxiliar" (6.1 "Código del auxiliar: … el código asignado por el Servicio Aduanero al auxiliar de la función pública aduanera."; 6.2 número de documento de identificación; 6.3 nombre o razón social; 6.4 domicilio fiscal) | Field 1 — correlative or reference number assigned by the declarant to the transmitted declaration; field 2 — DUCA registration number assigned by the customs service's computer system; field 3 — acceptance or registration date: the date the customs system VALIDATES AND REGISTERS the declaration transmitted by the declarant or representative; field 4 — exporter/supplier block (tax/identification registry number, ID document type, issuance country, name or corporate name, fiscal domicile); field 5 — importer/consignee block (same structure); field 6 — declarant/auxiliary block (auxiliary-of-the-customs-public-function code assigned by the customs service, ID number, name, fiscal domicile) | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 1-6 pp.1-3 (EVID-272; txt PAGE 1-3; SOQ-36 print) |
| LB-003 | Instructivo DUCA (43_), fields 7-18: 7. "Aduana de registro/inicio de tránsito: … el Código de la aduana donde se registra la DUCA o inicia la operación de tránsito." 8. "Aduana de salida: … el Código de la aduana de salida de la mercancía del país de exportación." 9. "Aduana de ingreso: … el Código de la aduana de ingreso de la mercancía del país de importación." 10. "Aduana de destino: … el Código de la aduana donde se nacionaliza o finaliza la operación de tránsito." 11. "Régimen aduanero: … el Código del régimen aduanero al que se estén sometiendo las mercancías." 12. "Modalidad: … el código de la modalidad según el Régimen aduanero que aplique. (Courier, envíos postales, encomiendas, equipajes, etc.)" 13. "Clase de declaración: … el código que identifica el tipo de declaración que se está presentando ante el Servicio Aduanero. (Simplificada, acumulada, provisional, complementaria, etc.)." 14. "Fecha de vencimiento del régimen: En este campo se consigna la fecha en la que se vence el plazo autorizado al régimen al que se están sometiendo las mercancías." 15. "País de procedencia… 16. País de exportación… 17. País de destino" (códigos). 18. "Depósito aduanero/zona franca: En este campo se consigna el código del Depósito, almacén, Zona Franca o empresas de perfeccionamiento activo donde se depositarán o destinarán las mercancías, cuando proceda." | Field 7 — customs office of registration / transit start; field 8 — exit customs office of the exporting country; field 9 — ingress customs office of the importing country; field 10 — destination customs office where the goods nationalize or the transit operation ends; field 11 — customs regime code; field 12 — modality code per the applicable regime (courier, postal shipments, encomiendas, baggage, etc.); field 13 — declaration class (simplified, accumulated, provisional, complementary, etc.); field 14 — REGIME EXPIRY DATE: the date on which the authorized term of the regime to which the goods are subjected expires (the field `04`'s clock reconciliation consumes by id); fields 15-17 — procedencia/exportation/destination country codes; field 18 — customs deposit/warehouse, ZONA FRANCA or active-perfecting-enterprise code where the goods will be deposited or destined, when applicable | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 7-18 pp.3-4 (EVID-272; txt PAGE 3-4; SOQ-36 print) |
| LB-004 | Instructivo DUCA (43_), fields 19-24: 19. "Transportista" (19.1 "Código del transportista: Código de registro del transportista asignado por el Servicio Aduanero."; 19.2 nombre del transportista). 20. "Modo de transporte: … la modalidad de transporte a través de la cual se movilizan las mercancías (aéreo, terrestre, marítimo o multimodal)." 21. "Lugar de embarque… 22. Lugar de desembarque". 23. "Conductor" (23.1 número de documento de identificación; 23.2 número de licencia de conducir; 23.3 país de expedición del documento; 23.4 nombre y apellidos). 24. "Medio de transporte" (24.1 "Identificación de la unidad de transporte: … el número de matrícula de circulación que identifica a la unidad de transporte."; 24.2 país de registro; 24.3 marca; 24.4 "Número de chasis/VIN: Consignar el número de serie del chasis o del Número de Identificación del Vehículo (VIN)…"; 24.5 identificación del remolque o semirremolque; 24.6 cantidad de unidades de carga; 24.7 "Número de dispositivo de seguridad (precintos o marchamos): En este campo se consignan los números de dispositivos de seguridad (precintos o marchamos) colocados a cada uno de los equipamientos por el Servicio Aduanero, demás autoridades o compañía de transporte o naviera, cuando proceda."; 24.8 "Equipamiento: … el código del tipo de equipamiento (por ejemplo: código 14=Tráiler) utilizado."; 24.9 tamaño del equipamiento; 24.10 tipo de carga — "refrigerada, seca, entre otros"; 24.11 "Número/Números de identificación del contenedor/es") | Field 19 — carrier block (customs-service-assigned registration code + name); field 20 — transport mode (air, land, sea or multimodal); fields 21/22 — loading and unloading places; field 23 — driver block (ID number, driver's license, expedition country, full name); field 24 — means-of-transport block: transport-unit circulation registration, country of registration, make, chassis number or VIN, trailer/semi-trailer identifications, count of cargo units, SECURITY-DEVICE NUMBERS (precintos or marchamos — seals) placed on each equipment by the customs service, other authorities or the transport/shipping company when applicable, equipment type code (e.g. code 14 = trailer) with size and load type (refrigerated, dry, others), and container identification number(s) | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 19-24 pp.4-5 (EVID-272; txt PAGE 4-5; SOQ-36 print) |
| LB-005 | Instructivo DUCA (43_), fields 25-31 (the value block): 25. "Valor de transacción: En este campo se consigna el precio realmente pagado o por pagar por las mercancías." 26. "Gastos de transporte: … la sumatoria total del costo del flete de las mercancías desde el lugar de embarque del país exportador hasta el puerto o lugar de importación." 27. "Gastos de seguro: … la sumatoria total del costo de la prima del seguro pagada o por pagar para asegurar las mercancías desde el lugar de embarque del país exportador hasta el puerto o lugar de importación." 28. "Otros gastos: … el total de los demás costos que deben adicionarse o deducirse al valor de las mercancías, que corran a cargo del importador y no estén incluidos en el precio realmente pagado o por pagar." 29. "Valor en aduana total: En este campo se consigna la sumatoria total de los elementos que conforman el valor en aduana (valor de transacción, gastos de flete, gastos de seguro y otros gastos), y será la base para el cálculo de los impuestos correspondientes." 30. "Incoterm: En este campo se consigna el incoterm internacional bajo el cual se ha pactado la transacción comercial." 31. "Tasa de cambio: En este campo se consigna el valor de cambio vigente entre peso centroamericano ($) y la moneda del país de importación, en la fecha de aceptación de la declaración de mercancías." | Field 25 — transaction value: the price actually paid or payable for the goods; field 26 — transport costs: total freight cost from the exporting country's loading place to the port or place of importation; field 27 — insurance costs: total premium paid or payable to insure the goods over that same leg; field 28 — other costs to be added to or deducted from the goods' value, borne by the importer and not included in the price actually paid or payable; field 29 — TOTAL CUSTOMS VALUE: the sum of the customs-value elements (transaction value, freight, insurance, other costs), WHICH IS THE BASE FOR COMPUTING THE CORRESPONDING TAXES; field 30 — international INCOTERM of the transaction; field 31 — exchange rate in force between the CENTROAMERICAN PESO ($) and the importing country's currency at the DM acceptance date (post-dollarization operational meaning corpus-silent — SOQ-45) | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 25-31 pp.5-6 (EVID-272; txt PAGE 5-6; SOQ-36/45 print) |
| LB-006 | Instructivo DUCA (43_), fields 32-39: 32. "Peso bruto total: … la suma total, en kilogramos, de los distintos pesos brutos declarados en las líneas de la declaración." 33. "Peso neto total" (same, net). 34. "Liquidación general." (34.1 "Tipo de tributo: … el código de cada uno de los tributos a los que están afectas las mercancías declaradas."; 34.2 "Total general por tributo: … el monto total por tributo declarado."; 34.3 "Modalidad de pago: … el código de la forma de pago de tributos correspondientes."; 34.4 "Total general: … el monto total de los tributos declarados, equivalente a la suma de todos los montos calculados."). 35. "Cantidad de bultos: Consignar la cantidad de bultos por cada línea a utilizarse en la operación solicitada." 36. "Clase de bultos: … el código del tipo de empaque o embalaje utilizado para el traslado de las mercancías, por cada línea." 37. "Peso neto: … el peso neto en kilogramos de la mercancía declarada en cada línea de mercancías. No debe incluirse el peso de los empaques, envases, embalajes y cubiertas de cualquier género." 38. "Peso bruto: … el peso bruto total de la mercancía, incluyendo el peso de los embalajes y cubiertas de cualquier género, declarada en cada línea de mercancía." 39. "Cuota/contingente: … el código para identificar la cuota o contingente al cual se acoge la mercancía." | Fields 32/33 — total gross/net weight in kilograms summed from the declaration lines; field 34 — GENERAL LIQUIDATION (settlement): per-tribute type code, total per tribute, payment-modality code, grand total equal to the sum of all computed amounts; fields 35/36 — count and class of bultos (packages) per line; fields 37/38 — net weight per line (excluding packaging, containers, packing and covers of any kind) and gross weight per line (including packing and covers); field 39 — quota or contingent code the goods take | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 32-39 pp.6-7 (EVID-272; txt PAGE 6-7; SOQ-36 print) |
| LB-007 | Instructivo DUCA (43_), fields 40-47: 40. "Número de línea: … el número correlativo de línea." 41. "País de origen: … el código del país de origen en donde las mercancías fueron fabricadas, producidas, ensambladas, cultivadas o extraídas, por cada línea de mercancías." 42. "Unidad de medida: … el código de la unidad de medida correspondiente a la mercancía declarada por línea." 43. "Cantidad: … la cantidad de la mercancía correspondiente a la línea de mercancía declarada." 44. "Acuerdo: En este campo se consigna el código para identificar un tratado o Acuerdo comercial del cual el país importador forme parte, y sirve para mostrar que la mercancía a importar cuenta con un derecho arancelario a la importación (DAI) preferencial originado de la negociación comercial a la cual se hace referencia." 45. "Clasificación arancelaria: En este campo se consigna la clasificación arancelaria que le corresponde a las mercancías declaradas, por línea, de conformidad con el Sistema Arancelario Centroamericano (SAC) y códigos nacionales adicionales." 46. "Descripción de las mercancías: … la descripción comercial de las mercancías de forma clara para su identificación y clasificación arancelaria." 47. "Origen." (47.1 "Criterio para certificar origen: … el criterio utilizado por el productor/exportador de las mercancías para certificar el origen, de acuerdo a lo establecido en el Reglamento Centroamericano sobre el Origen de las Mercancías o el Anexo 6 (a) del Protocolo de Incorporación de la República de Panamá al Subsistema de Integración Económica del Sistema de la Integración Centroamericana."; 47.2 "Reglas accesorias" — same instruments; "En caso contrario indique 'NO'") | Field 40 — line correlative number; field 41 — country-of-origin code where the goods were manufactured, produced, assembled, cultivated or extracted, per line; field 42 — unit-of-measure code per line; field 43 — quantity per line; field 44 — ACUERDO (agreement): code identifying a treaty or trade agreement of which the importing country is part, showing the goods carry a PREFERENTIAL import tariff right (DAI) originating in that commercial negotiation; field 45 — tariff classification per line under the Sistema Arancelario Centroamericano (SAC, Central American Tariff System) plus ADDITIONAL NATIONAL CODES; field 46 — commercial description clear enough for identification and tariff classification; field 47 — origin block: criterion used by the producer/exporter to certify origin per the Central American Regulation on the Origin of Goods or Annex 6(a) of Panama's Incorporation Protocol, plus accessory origin rules (else "NO") | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 40-47 p.7 (EVID-272; txt PAGE 7; SOQ-36 print) |
| LB-008 | Instructivo DUCA (43_), fields 48-53: 48. "Valor de transacción: … el precio realmente pagado o por pagar por las mercancías declaradas en cada línea, de conformidad con lo dispuesto en el Acuerdo relativo a la aplicación del Artículo VII del Acuerdo General sobre Aranceles Aduaneros." 49. "Gastos de transporte: … el valor del transporte que corresponden a cada línea." 50. "Seguro: … el valor del seguro pagado por el importador que corresponden a cada línea." 51. "Otros gastos: … el valor de otros gastos no incluidos en los campos anteriores y que forman parte del valor en aduanas que corresponden a cada línea." 52. "Valor en aduana: En este campo se consigna la base imponible para la aplicación de los derechos arancelarios a la importación (DAI), de las mercancías importadas o internadas al territorio aduanero de los Estados Parte." 53. "Liquidación por línea." (53.1 "Tipo: … el código de cada uno de los tributos declarados de mercancías por línea."; 53.2 "Alícuota: … el porcentaje de los tributos aplicados a las mercancías por línea."; 53.3 "Total: … el monto de cada tributo declarado de mercancías por línea."; 53.4 "Modalidad de Pago: … el código de la forma de pago de los tributos correspondientes por línea."; 53.5 "Total general: … el monto total, por línea, de los tributos declarados, equivalente a la suma de todos los montos calculados.") | Fields 48-51 — per-line transaction value (per the GATT Article VII Agreement), transport, insurance and other costs; field 52 — per-line customs value: the TAX BASE for applying import tariff rights (DAI) to goods imported or entered into the customs territory of the States Parties; field 53 — PER-LINE LIQUIDATION (settlement): tribute type code, alícuota (applied percentage), per-tribute total, payment-modality code, and the per-line grand total equal to the sum of all computed amounts | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 48-53 p.8 (EVID-272; txt PAGE 8; SOQ-36 print) |
| LB-009 | Instructivo DUCA (43_), field 54: "Documentos de soporte." 54.1 "Código del tipo de documento: … el código del tipo de documento de soporte que ampara las mercancías sujetas al control aduanero (Ejemplo, Facturas comerciales, Documento de Transporte, Certificados)." 54.2 "Número de documento: … el número del documento de soporte que ampara las mercancías declaradas." 54.3 "Fecha de emisión de documento: … la fecha de emisión del documento de soporte declarado." 54.4 "Fecha de vencimiento: Identificar la fecha de vencimiento del documento de soporte declarado, cuando aplique." 54.5 "País de emisión del documento: … el país de emisión del documento de soporte declarado." 54.6 "Línea (al que aplica el documento): En este campo se consigna la línea o líneas de la Declaración Única Centroamericana (DUCA) que aplica el Documento de soporte declarado. Ejemplos: '3-5'; '1, 6, 8'; '3-5, 8'." 54.7 "Nombre de la autoridad o entidad que emitió el documento de soporte: … el nombre de la entidad pública o privada que emitió el documento, por ejemplo, una Institución Gubernamental, una naviera, un proveedor, etc." 54.8 "Monto: En esta casilla se debe de indicar el monto total del documento declarado, cuando aplique." | Support-documents block: document-type code covering the goods subject to customs control (commercial invoices, transport documents, certificates), document number, emission date, expiry date when applicable, issuance country, LINE(S) the document applies to — with the printed RANGE SYNTAX "3-5"; "1, 6, 8"; "3-5, 8" — name of the issuing public or private authority/entity (governmental institution, shipping line, supplier, etc.), and total amount when applicable | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Field 54 pp.8-9 (EVID-272; txt PAGE 8-9; SOQ-36 print) |
| LB-010 | Instructivo DUCA (43_), fields 55-62: 55. "Observaciones generales: … cualquier eventualidad o circunstancia que el declarante considere necesario informar. Asimismo, deberá hacerse constar cuando determinada mercancía se exporta en régimen de libre comercio dentro del contingente arancelario aprobado de conformidad con el Apéndice a los Anexos 4.2 y 4.3 del Protocolo de Incorporación de la República de Panamá al Subsistema de Integración Económica del Sistema de la Integración Centroamericana." 56. "Válida hasta: Cuando la Declaración haga las veces de Formulario Aduanero Único Centroamericano, tendrá validez de treinta días hábiles a partir de su emisión. Esta Vigencia aplica únicamente en el país de exportación de las mercancías." 57. "Firmas y sellos de funcionario de aduanas: Consignar el nombre completo, la firma, fecha y sello de la Autoridad Aduanera que autoriza la operación aduanera." 58. "Firma o autorización de ventanilla única: (casilla de uso oficial): … la autorización, cuando corresponda, del Banco Central o la Ventanilla Única del país exportador." 59. "Código de exportador: … el código del exportador." 60. "Firma del declarante: Firma del operador de comercio o auxiliar de la función pública aduanera, conforme a lo establecido en la legislación aduanera regional." 61. "Declaración de origen: En este campo el productor declara el origen de la mercancía a exportar, anotando en el espacio correspondiente el nombre del país de origen de la mercancía. Para el efecto deberá consignarse la firma, el nombre de la persona que firma, el de la empresa, así como el cargo que ocupa en la misma. En caso que el productor sea el exportador de la mercancía no será necesario llenar este campo." 62. "Certificación de origen: En este campo el exportador certifica el origen de la mercancía a exportar, anotando en el espacio en blanco el nombre del país de origen. Para el efecto debe consignarse la firma, el nombre de la persona que firma, el de la empresa y el cargo que ocupa dentro de la misma. En caso de que el exportador sea el productor de la mercancía, no será necesaria llenar el campo de la Declaración de Origen de la mercancía a exportar." | Field 55 — general observations, recording free-trade-regime exports within the approved tariff contingent (Appendix to Annexes 4.2/4.3 of the Panama Incorporation Protocol); field 56 — VALID UNTIL: when the declaration serves as FAUCA it is valid THIRTY días hábiles from its EMISSION, and that validity applies ONLY in the country of exportation of the goods; field 57 — customs officials' signatures, seals and date (authorizing authority); field 58 — single-window/central-bank authorization (official-use box of the exporting country); field 59 — exporter code; field 60 — declarant's signature (trade operator or customs auxiliary per regional customs legislation); field 61 — DECLARATION OF ORIGIN: the PRODUCER declares the origin of the goods to be exported (country name, signatory's name, company and position) — NOT required when the producer IS the exporter; field 62 — CERTIFICATION OF ORIGIN: the EXPORTER certifies origin (same data) — when the exporter is the producer, the declaración de origen field need not be filled (the two fields are complements, never duplicates) | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 55-62 pp.9-10 (EVID-272; txt PAGE 9-10; SOQ-36 print) |
| LB-011 | Ley de Simplificación Aduanera (74_), Art. 6: "La declaración para destinar aduaneramente las mercancías, deberá efectuarse mediante transmisión electrónica de la información, conforme los lineamientos y formatos físicos y electrónicos establecidos por la Dirección General, a través del sistema conocido como teledespacho, el cual, para asegurar la integridad de los flujos de información, deberá estar estructurado por procedimientos que aseguren la autenticidad, confidencialidad, integridad y no repudiación de la información transmitida. Excepcionalmente, la declaración podrá efectuarse por otros medios legalmente autorizados o por disposiciones administrativas de carácter general dictadas por la Dirección General." "Los documentos contenidos en un soporte magnético, digital o electrónico producirá los mismos efectos jurídicos que los escritos en un soporte de papel…" "Cuando la Ley requiera que la información conste o que la misma sea presentada y conservada o archivada en su forma original, ese requisito quedará satisfecho con un mensaje de datos, siempre que la información contenida en éste sea accesible para su ulterior consulta." "…podrá administrarlo y conservarlo de manera electrónica; asimismo, potenciará la notificación de los actos administrativos por medio de mensaje de datos electrónicos." "En todo trámite legal, no se dará aplicación a disposición alguna que sea óbice para la adimisión [sic] como prueba de un mensaje de datos." | The declaration to destine goods customs-wise is made BY ELECTRONIC TRANSMISSION per the DGA-established guidelines and physical/electronic formats, through the system known as teledespacho (remote customs dispatch), which — to secure the integrity of the information flows — must be structured by procedures ensuring the AUTHENTICITY, CONFIDENTIALITY, INTEGRITY and NON-REPUDIATION of the transmitted information (other legally authorized means exceptionally). Documents in magnetic, digital or electronic support produce THE SAME LEGAL EFFECTS as paper; a legal requirement that information appear, be presented and be conserved or archived in its original form is satisfied by a data message provided its content is accessible for later consultation; the DGA may administer and conserve registers electronically and promote notification of administrative acts by electronic data message; in any legal proceeding, no provision obstructing the admission of a data message as evidence applies | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 6 pp.3-4 (EVID-269; txt PAGE 3-4; SOQ-30 print) |
| LB-012 | Ley de Simplificación Aduanera (74_), Art. 8 (key fragments): "…se establecen sistemas de certificación de la información transmitida, para lo cual, se autorizará la intermediación de empresas que provean servicios de certificación de dicha información, llamadas en adelante entidades certificadoras." (authorization, audit, sanction and revocation powers exercised by the Ministerio de Hacienda, faculties a)-i)). "…cada usuario autorizado, contará con una pareja de claves o llaves únicas y correspondientes entre si, una pública y otra privada, de manera tal que ambas se correspondan de manera exclusiva y excluyente… La vinculación de ambas llaves o clases constituye la firma digital o electrónica, que para los efectos legales se constituye en el sustituto digital de la firma manuscrita que en el marco del intercambio electrónico de datos permite al receptor de un mensaje electrónico verificar con certeza la identidad proclamada por el transmisor, impidiendo a este último desconocer en forma posterior la autoría del mensaje." "Los usuarios del sistema, conocidos además como suscriptores, tendrán la obligación de guardar secreto acerca de las llaves privadas que les hayan sido asignadas y responderán por las consecuencias legales que se deriven de un uso indebido de tales llaves, ya sea por parte de él mismo o de terceras personas no autorizadas." "Se prohíbe a los Auxiliares de la Función Pública Aduanera, revelar o permitir el uso a terceros de su clave de acceso o firma digital, inclusive revelarla o permitir el uso de la misma a sus asistentes autorizados." | Information-certification systems are established through intermediary enterprises called entidades certificadoras (certifying entities) — their authorization to operate, surveillance, audits and sanction/revocation powers rest with the Ministerio de Hacienda. Each authorized user holds a unique corresponding PUBLIC/PRIVATE KEY PAIR, exclusively and excludingly matched; the linking of both keys constitutes the firma digital (digital or electronic signature), the LEGAL DIGITAL SUBSTITUTE of the manuscrita (handwritten) signature — within electronic data interchange it lets the receiver of an electronic message verify with certainty the identity proclaimed by the transmitter, preventing the latter from later denying the authorship of the message. Users (known also as suscriptores, subscribers) must KEEP SECRET their assigned private keys and answer for the legal consequences of misuse by themselves or unauthorized third parties. Auxiliares de la Función Pública Aduanera (auxiliaries of the customs public function) are PROHIBITED from revealing or allowing third-party use of their access key or digital signature, including revealing it to or allowing its use by their own authorized assistants | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 8 pp.4-7 (EVID-269; txt PAGE 4-7; SOQ-30 print) |
| LB-013 | Ley de Simplificación Aduanera (74_), Art. 12-B: "Créase una tasa que se cobrará por la prestación de Servicios de Inspección no Intrusiva. La tasa en referencia será de un monto de dieciocho dólares de los Estados Unidos de América, la cual incluye el pago del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios. El Servicio Aduanero no podrá autorizar el despacho sin el pago de la misma. La obligación del pago se generará siempre y cuando las operaciones antes indicadas se produzcan por el ingreso o salida de mercancías o medios de transporte del territorio aduanero nacional por cualquier vía. El pago deberá efectuarse al momento de la transmisión electrónica del Manifiesto, Declaración de Mercancías a cualquiera de los Regímenes Aduaneros, Formulario Aduanero Único Centroamericano, Tránsitos Internos o Internacionales u otras declaraciones o formularios que amparen el transporte, traslado o movimiento de mercancías desde y hacia el territorio aduanero nacional, utilizando cualquiera de las plataformas autorizadas por el Servicio Aduanero que permitan la captura de dichos documentos." "…son sujetos responsables y como consecuencia están obligados al pago de la Tasa en referencia, los declarantes o el representante de éstos…" "El incumplimiento al pago de la tasa será sancionado de conformidad a lo establecido en la Ley Especial para Sancionar Infracciones Aduaneras." Art. 12-C: "…Facúltase al Ministerio de Hacienda, para que mediante la emisión del Acuerdo Ejecutivo correspondiente, que deberá ser razonado, motivado y justificado, haga los ajustes a la Tasa ya determinada. La tasa podrá ser revisada y ajustada cada dos años por el Ministerio de Hacienda, hasta un máximo de 10 por ciento, sobre el valor de la tasa establecida en el artículo anterior, considerando entre otros aspectos: el índice de inflación acumulada, el aumento o disminución de las operaciones, así como cualquier variación de los costos siguientes: a) El costo de mantenimiento rutinario…; b) …preventivo…; c) …correctivo…; d) El costo de la operación…; e) El costo de actualización o mejoramiento…" | Art. 12-B — a TASA (fee) is created for the provision of non-intrusive inspection services: EIGHTEEN DOLLARS of the United States of America (dieciocho dólares — $18 as printed in the 2012 consolidation), which INCLUDES the IVA payment; the customs service CANNOT AUTHORIZE DESPACHO (clearance) without its payment. The payment obligation arises whenever the operations occur through the entry or exit of goods or transport means into/from the national customs territory by any route; payment falls due AT THE MOMENT OF THE ELECTRONIC TRANSMISSION of the manifiesto, DM to any customs regime, FAUCA, internal or international transits, or other declarations/forms covering the transport, transfer or movement of goods into and out of the national customs territory, using any authorized capture platform. Responsible subjects: the declarants or their representatives. Nonpayment is sanctioned per LESIA (not in corpus — SOQ-32). Art. 12-C — the Ministerio de Hacienda is empowered, by a reasoned, motivated and justified Acuerdo Ejecutivo, to adjust the tasa; it may be reviewed and adjusted EVERY TWO YEARS up to a MAXIMUM OF 10 PERCENT over the value established in the preceding article, considering accumulated inflation, operation increases/decreases and cost variations (routine, preventive and corrective maintenance, operation, updating/improvement; concession requirements) | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 12-B/12-C pp.11-12 (EVID-270; txt PAGE 11-12; $18 = 2012-printed dated value — SOQ-34 watch) |
| LB-014 | Ley de Simplificación Aduanera (74_), Art. 2: "Previo al arribo de las mercancías al territorio aduanero nacional, los transportistas ya sean terrestres, marítimos o aéreos, o los agentes de transporte en su caso, están obligados a proporcionar a la aduana de ingreso, mediante transmisión electrónica u otros medio autorizados por la Dirección General, la información contenida en el manifiesto general de carga. En cuanto a la información relativa a las mercancías, deberá consignarse el peso bruto en kilogramos, la clase y cantidad de bultos, así como la clase o tipo genérico de las mercancías, detallando primero y en orden descendente las de mayor valor comercial." "En los casos en los que el importador, no pueda acreditar el valor de la prima de seguro por no haber efectuado la contratación de una póliza para el transporte de carga, el Servicio de Aduanas, podrá establecer como prima de seguro, los porcentajes que a continuación se detallan: a) Transporte regional terrestre de carga: 1.25% sobre el valor FOB de las mercancías; y b) Transporte internacional de carga, sin consideración de la modalidad de transporte: 1.50% sobre el valor FOB de las mercancías." "Para la determinación del valor de flete, el Servicio de Aduanas, podrá establecer de manera periódica valores de referencia, en consulta con las gremiales de transporte o empresas del rubro, los cuales serán publicados para conocimiento de los importadores y Auxiliares de la Función Pública Aduanera." "En los casos en los cuales no se pueda acreditar un valor de flete, por parte del importador, el Servicio de Aduanas, establecerá el 10% sobre el valor FOB de las mercancías." "Los gastos de transporte de las [mercancías] importadas hasta el puerto o lugar de importación, así como los gastos de carga, descarga y manipulación ocasionados por el transporte de las mercancías importadas hasta el puerto de importación y el costo del seguro, estarán incluidos en el valor en aduana de las mercancías, para los efectos del Número 2 del Art.8 del Acuerdo a la Aplicación del Artículo VII del Acuerdo General sobre Aranceles Aduaneros y Comercio de 1994." | BEFORE the goods' arrival at the national customs territory, transportists (land, sea or air) or transport agents must provide the ingress customs office — by electronic transmission or another DGA-authorized means — the information contained in the general cargo manifiesto; on the goods, the GROSS WEIGHT IN KILOGRAMS, the class and count of bultos (packages), and the generic class/type of goods are consigned, DETAILING FIRST AND IN DESCENDING ORDER those of greatest commercial value. When the importer cannot accredit the insurance premium (no policy contracted for the cargo transport), the customs service may set as premium: a) regional land cargo transport — 1.25% over the FOB value of the goods; b) international cargo transport regardless of transport mode — 1.50% over the FOB value. For the determination of freight value, the customs service may periodically establish REFERENCE VALUES, in consultation with transport guilds or industry companies, published for importers and customs auxiliaries; when the importer cannot accredit a freight value, the customs service sets 10% over the FOB value of the goods. Transport costs of the imported goods to the port or place of importation, loading/unloading and handling costs caused by transport to the importation port, and the insurance cost are INCLUDED in the customs value for the purposes of number 2 of Art. 8 of the 1994 GATT Article VII Agreement (the "Art.8" print is the agreement's article — [as printed]) | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 2 pp.1-2 (EVID-269; txt PAGE 1-2; percentages = dated rows — SOQ-35) |
| LB-015 | Ley de Simplificación Aduanera (74_), Art. 3: "En el sistema de autodeterminación o autoliquidación, corresponde al declarante la determinación de la obligación tributaria aduanera y el cumplimiento de las demás regulaciones establecidas en las leyes respectivas, y además, la presentación de la declaración de mercancías y el pago de los tributos que se causen." "…Cuando en el ejercicio de sus facultades de verificación inmediata o fiscalización a posteriori, establecidas en la Ley, la Autoridad Aduanera competente determine el incumplimiento de la obligación tributaria aduanera, procederá a la liquidación oficiosa de los tributos a la importación dejados de pagar y a imponer las sanciones respectivas." Art. 12: "La declaración de mercancías autoliquidada será sometida a un proceso selectivo y aleatorio que determine si corresponde efectuar la verificación inmediata de lo declarado. Dicha verificación no limita las facultades de fiscalización posterior de la autoridad aduanera." Art. 12-A: "En aquellos procesos de inspección no intrusiva que pueda advertirse que existe el cometimiento de un ilícito, se deberán certificar las imágenes que reproduzca el sistema y remitirse a las autoridades competentes. Las referidas certificaciones harán plena prueba en el proceso penal correspondiente… El mismo valor probatorio tendrán las imágenes reproducidas del sistema de inspección no intrusiva en los procesos administrativos correspondientes." | Art. 3 — under the self-determination or AUTOLIQUIDACIÓN system, the DECLARANT determines the customs tax obligation, complies with the other applicable regulations, presents the goods declaration and pays the tributes caused; exceptionally the customs authority determines the obligation ex officio on breach found in immediate verification or a-posteriori fiscalización (liquidación oficiosa of unpaid import tributes + sanctions). Art. 12 — the autoliquidated DM is submitted to a SELECTIVE AND RANDOM process deciding whether immediate verification of the declared proceeds — without limiting the authority's posterior fiscalization powers. Art. 12-A — where a non-intrusive inspection shows the commission of an ilícito (offense), the system's IMAGES are certified and remitted to the competent authorities; the certifications are PLENA PRUEBA (full proof) in the corresponding penal process, and the reproduced images of the non-intrusive inspection system carry the SAME probatory value in the corresponding administrative processes | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 3/12/12-A pp.2, 10-11 (EVID-270; txt PAGE 2, 10-11; SOQ-30 print) |
| LB-016 | Ley de Simplificación Aduanera (74_), Art. 11: "Toda mercancía para ser destinada a un régimen aduanero, deberá estar amparada en una declaración. La declaración de mercancías se considerará aceptada cuando se registre en el sistema informático autorizado por la Dirección General. La realización de dicho acto no implica avalar el contenido de la declaración, ni limita las facultades de comprobación, fiscalización y liquidación a posteriori de la autoridad aduanera." "En el caso de transferencia o venta de mercancías importadas bajo los regímenes aduaneros suspensivos y liberatorios, la declaración de importación definitiva mediante la cual se cancela el régimen, deberá presentarse y pagarse previo a la transferencia o venta realizada." "En el caso de las sanciones y liquidaciones de oficio practicadas por la autoridad aduanera competente, el pago de los tributos y multas deberá efectuarse dentro del plazo de los ocho días hábiles siguientes a la notificación de la resolución definitiva." "Las declaraciones que hayan sido teledespachadas y se encuentren registradas en el sistema informático de la Dirección General y que no se presenten dentro del plazo de diez días, serán anuladas de oficio del sistema por la autoridad aduanera competente; en el caso de las declaraciones de mercancías que se encuentren en la misma condición anterior, y que hayan sido pagados los tributos, serán anuladas del sistema de aduanas dentro del plazo de sesenta días siguientes a su registro, en este último caso el interesado podrá presentar la solicitud de devolución de impuestos ante la Autoridad Aduanera correspondiente." | Every good destined to a customs regime must be covered by a declaration; the DM is ACCEPTED when REGISTERED in the DGA-authorized computer system — that act does not endorse the declaration's content nor limit the authority's posterior verification, fiscalización and liquidación powers. For the TRANSFER OR SALE of goods imported under SUSPENSIVE and LIBERATORY customs regimes, the definitive-import declaration cancelling the regime must be PRESENTED AND PAID BEFORE the transfer or sale made. For sanctions and ex officio liquidations practiced by the competent customs authority, payment of tributes and fines must be made within EIGHT días hábiles following notification of the final resolution. Teledespachada declarations registered in the DGA system and NOT PRESENTED within the TEN-DAY term are annulled ex officio from the system by the competent authority; declarations in the same condition whose tributes were PAID are annulled from the customs system within the SIXTY DAYS following their registration — in the latter case the interested party may file the tax-return request (solicitud de devolución de impuestos) before the corresponding customs authority | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 11 pp.8-9 (EVID-270; txt PAGE 8-9; SOQ-30 print) |
| LB-017 | Ley de Simplificación Aduanera (74_), Art. 11-A: "Se entenderá por procedimiento simplificado para el retiro de mercancías, el retiro de éstas de los recintos aduaneros, sin la determinación final de los aranceles aduaneros, impuestos y cargos aplicables a la importación, dentro de las cuarenta y ocho horas posteriores a la llegada de la mercancía. Dicho procedimiento será autorizado mediante resolución razonada, por un plazo de un año, prorrogable a criterio de la Dirección General… El procedimiento simplificado también podrá ser aplicado cuando así se acuerde en un convenio suscrito entre la Dirección General y un operador de envíos de entrega rápida o courier." "…el pago de los tributos determinados en la declaración de mercancías de importación deberá efectuarse dentro del plazo de ocho días hábiles siguientes a la presentación de la misma ante la autoridad aduanera competente…" (requisitos g/h): "g) Rendir ante el fisco una garantía suficiente en forma de depósito o fianza, por el monto estimado de sus operaciones que cubra el pago definitivo de los derechos aduaneros, impuestos y cargos relacionados con la importación, la cual será autorizada por la Dirección General, por un plazo de un año…"; "h) Presentar las respectivas solvencias de pago del Instituto Salvadoreño del Seguro Social y de las diferentes Administradoras de Fondos de Pensiones, de las cotizaciones correspondientes a los treinta días anteriores, a aquel en el que se presente la solicitud;". Courier convenio bands: "b) Para envíos cuyo valor FOB sea inferior a doscientos dólares (US$ 200.00), el retiro de las mercancías de los recintos fiscales se autorizará con la presentación de la guía aérea y la factura respectiva, presentado por el operador de envíos de entrega rápida o courier; en caso de no tener factura será sometido a los valores de referencia emitidos por el Departamento de Valoración de la Dirección General." "c) Para envíos cuyo valor FOB sea superior a doscientos dólares (US$ 200.00) y no mayor a tres mil dólares (US$ 3,000.00), el retiro de las mercancías de los recintos fiscales se autorizará con la presentación de la declaración de mercancías. La declaración de mercancías podrá ser consolidada siempre que el total de la suma del valor FOB de cada una de las mercancías no supere los tres mil dólares (US$ 3,000.00) por el operador de envíos de entrega rápida o courier." (revocation: "…ante el incumplimiento por parte del sujeto pasivo de las condiciones y requisitos establecidos en la resolución de autorización o en el Convenio correspondiente, lo cual dará lugar a que se haga efectiva la garantía o fianza rendida a favor del fisco y dará lugar a la suspensión de sus operaciones aduaneras hasta que se verifique el pago correspondiente.") | Simplified goods-withdrawal procedure: withdrawal from customs precincts WITHOUT final determination of the customs tariffs, taxes and charges applicable to the importation, within the FORTY-EIGHT HOURS following the goods' arrival; authorized by reasoned resolution for ONE YEAR, extendable at the DGA's criteria; applicable in the cases set by commercial instruments or when agreed in a convenio between the DGA and a courier/express-delivery operator; determined import tributes payable within EIGHT días hábiles following the declaration's presentation. Requirements include: g) a SUFFICIENT GUARANTEE as deposit or bond, for the estimated operations amount covering definitive payment of customs duties, taxes and import-related charges, DGA-authorized, one-year term; h) the respective ISSS and AFP payment solvencies for the contributions corresponding to the THIRTY DAYS prior to that of the application. Courier bands: b) FOB value UNDER US$200.00 — withdrawal from fiscal precincts authorized on presentation of the air waybill (guía aérea) and the respective invoice by the courier operator (no invoice ⇒ subject to the DGA Valoración department's reference values); c) FOB over US$200.00 and NOT greater than US$3,000.00 — withdrawal authorized on presentation of the DM, which may be CONSOLIDATED provided the total sum of each good's FOB value does not exceed US$3,000.00 per courier operator. Breach of the authorization/convenio conditions ⇒ revocation with execution of the guarantee and suspension of customs operations until payment is verified | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 11-A pp.9-10 (EVID-270; txt PAGE 9-10; SOQ-30 print) |
| LB-018 | Ley de Simplificación Aduanera (74_), Art. 13: "…el tiempo en que se deberán tener a disposición los registros contables, registros especiales y la documentación de respaldo de los mismos, será de cinco años." "Los exportadores y productores deberán conservar por un mínimo de cinco años, a partir de la fecha de su emisión, las certificaciones o certificados de origen, así como todos los registros y documentos que demuestren que una mercancía, para la cual el productor o el exportador proporcionó una certificación de origen, de conformidad a lo establecido en los tratados, convenios, acuerdos y otros instrumentos en materia de comercio suscritos por el país." Art. 14 (final inciso): "El plazo para la verificación posterior caducará en cinco años contados desde la fecha de aceptación de la declaración de mercancías correspondientes." | Art. 13 — subjects bound by law to keep formal accounting must have it at the competent customs authority's disposal when required (those not so bound keep special registers); in both cases the accounting registers, special registers and their support documentation must remain available for FIVE YEARS; exporters and producers must conserve, for a MINIMUM OF FIVE YEARS from their emission date, the origin certifications or certificates, and all registers and documents demonstrating goods for which the producer or exporter provided an origin certification under the country's trade treaties, convenios, acuerdos and other instruments. Art. 14 (final inciso) — the posterior-verification term EXPIRES (caduca) FIVE YEARS counted from the ACCEPTANCE DATE of the corresponding DM | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 13/14 pp.12-14 (EVID-271; txt PAGE 12-14; SOQ-30 print) |
| LB-019 | Ley de Simplificación Aduanera (74_), Art. 16: "Los resultados de la fiscalización deberán ser notificados al declarante o a su agente de aduanas en su caso… Se notificará al supuesto infractor, a su representante legal, apoderado o mandatario aduanero, curador o heredero, en el lugar señalado para recibir notificaciones o en su domicilio. Tales notificaciones se harán por cualquier Delegado de la Dirección General, por la vía electrónica, telefax o telefacsímil, por correo certificado con constancia de recepción, o por los demás medios que autoricen las leyes." (substitute-recipient ladder; esquela at the door; 72-hour edicto fallback) "…Debido a la solicitud que se establece entre el declarante y su agente de aduanas en lo que respecta a sus obligaciones tributarias aduaneras y al mandato que de acuerdo con la legislación de la materia se establece entre los mismos, la notificación que se haga al agente de aduanas se entenderá extensiva para el declarante." Art. 17: "a) La apertura del proceso debe notificarse al declarante o a su Agente de Aduanas, apoderado o representante, haciéndoles saber el contenido íntegro del informe de fiscalización, hoja de discrepancia o informe de investigación correspondiente…" "b) El declarante contará con un plazo de quince días hábiles contados desde el siguiente día de la notificación para la presentación de sus alegatos y las pruebas de descargo que estime pertinente;" "c) Vencido dicho plazo, la Dirección General dictará la resolución que proceda dentro de un plazo de veinte días hábiles. La notificación de dicha resolución se hará dentro del plazo de veinte días hábiles posteriores a la fecha de su emisión, la cual deberá contener el texto íntegro de la misma." "Contra la resolución de liquidación oficiosa de impuestos que se dicte, se admitirán los recursos administrativos señalados en la Ley Especial para Sancionar Infracciones Aduaneras, ante las autoridades competentes y conforme a los requisitos, plazos y procedimientos establecidos en la misma." | Art. 16 — fiscalization results are notified to the declarant or its customs agent; the presumed infractor, legal representative, attorney or customs agent, curator or heir is notified at the place designated for notifications or their domicile, by any DGA delegate, BY ELECTRONIC MEANS, telefax or telefacsimile, certified mail with receipt of reception, or other legally authorized means (with the substitute-recipient ladder — spouse/companion, adult child, partner, employee or household member; door esquela with the resolution in extract; and the 72-hour edicto fallback); given the request relation established between declarant and customs agent regarding their customs tax obligations and the mandate established between them, NOTIFICATION MADE TO THE CUSTOMS AGENT IS UNDERSTOOD AS EXTENSIVE TO THE DECLARANT. Art. 17 — the administrative process: a) the opening is notified to the declarant or its agent, making known the FULL content of the fiscalization report, discrepancy sheet or investigation report; b) the declarant has FIFTEEN días hábiles counted from the day after notification to present alegatos (arguments) and discharge proofs it deems pertinent; c) after that term the DGA issues the resolution within TWENTY días hábiles, notified within the twenty días hábiles after its emission date with the full text; against ex officio tax-liquidation resolutions, the administrative RECOURSES of LESIA are admitted (not in corpus — SOQ-32) | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 16/17 pp.14-15 (EVID-271; txt PAGE 14-15; SOQ-30/32 print) |
| LB-020 | Comunicado 42_ (CIEX/BCR/DGA): "…en coordinación con la Secretaría de Integración Económica Centroamericana SIECA, y la Autoridad Nacional de Aduanas de Panamá, se implementará a partir del 03 de marzo de 2025, la transmisión electrónica de las operaciones de exportación e importación entre El Salvador y Panamá bajo DUCA-F, proceso para el cual los exportadores deberán asegurarse de disponer de tokens en el Portal de SIECA, para obtener de forma inmediata la aceptación de la aduana de Panamá o El Salvador según corresponda." Benefits: "Obtendrá la aceptación extranjera en un tiempo de 37 segundos."; "Podrá visualizar el número de declaración de aduana destino para facilitar el proceso de pago de impuestos."; "Tendrá un despacho de mercancías más ágil en los puntos fronterizos". Portal: "https://www.ducaf.sieca.int/PortalCapturaPanama/…". Institutions: BCR (CIEX El Salvador), DGA, SIECA, ANA Panamá | Coordinated with SIECA and Panama's Autoridad Nacional de Aduanas, from 03 MARCH 2025 the electronic transmission of export and import operations between El Salvador and Panama under DUCA-F is implemented; exporters must ensure they hold TOKENS in the SIECA portal to obtain IMMEDIATE acceptance by the Panama or El Salvador customs office as corresponds. Benefits: foreign acceptance in ~37 SECONDS; visibility of the DESTINATION customs declaration number (facilitating the tax-payment process); more agile goods despacho at border points. Capture portal ducaf.sieca.int (PortalCapturaPanama for Panama-origin registrations); participating institutions BCR/CIEX, DGA, SIECA and ANA Panamá | `sv/sources/42_Comunicado_Exportaciones_Panama.docx` | Whole comunicado (EVID-273; txt PARAGRAPHS/TABLE 1; dated operational fact 2025-03-03) |

## 3. Functional Requirements

### 3.1 The DUCA record model (43_)

- **SV-SPE-FR-103:** The system shall model the DUCA as ONE declaration
  record with a variant flag — DUCA-D (goods originating in third
  countries and those not taking DUCA-F) · DUCA-T (*tránsito aduanero
  internacional terrestre*, international land customs transit) · DUCA-F
  (goods originating in the Central American region) — the record
  integrating the FAUCA/DM/DUT data functions employed per the nature of
  the operation and the customs regime; ampliation information sheets
  supported as continuation records; the print-no-alteration rule
  recorded on the print surface; this record is the DM surface the
  `04_customs-clocks.md` clock chassis links to (SV-SPE-FR-064..081 by
  id) and the declaration surface the declarante-role config of
  SV-SPE-FR-020 stamps (by id).
  (LB-001; EVID-272)
- **SV-SPE-FR-104:** The system shall carry the DUCA header registration
  and identity blocks per the 43_ field contract: field 1 declarante
  correlativo/reference; field 2 DUCA registration number ASSIGNED BY THE
  CUSTOMS SYSTEM (read-only after acceptance); field 3 *fecha de
  aceptación o registro* — the date the DGA system validates and
  registers the transmitted declaration, which per 74_ Art. 11 (LB-016)
  is the acceptance event and the D15 anchor for the caducidad tracker
  (FR-127) and the T4 clock anchors (by id); field 4
  exportador/proveedor, field 5 importador/destinatario and field 6
  declarante/auxiliar blocks, each with identification number, document
  type, issuance country, name/razón social and *domicilio fiscal* — the
  declarante block resolving from the declarante-role config consumed
  from SV-SPE-FR-020 by id (agente aduanero · apoderado especial
  aduanero · ordinary agency), never restated here.
  (LB-002; LB-016; EVID-272/270)
- **SV-SPE-FR-105:** The system shall carry the DUCA customs-routing and
  regime header: aduanas of registro/inicio de tránsito (7), salida (8),
  ingreso (9) and destino (10); *régimen aduanero* (11); *modalidad* (12
  — courier, envíos postales, encomiendas, equipajes, etc.); *clase de
  declaración* (13 — simplificada, acumulada, provisional,
  complementaria, etc.); **fecha de vencimiento del régimen (14)** — the
  field-14 value the T4 clock reconciliation consumes BY ID
  (SV-SPE-FR-080: computed-vs-declared mismatch flags, never
  auto-overwrite; field numbering per the 43_ print — 04's OQ-2
  reconciliation kin); países of procedencia (15), exportación (16) and
  destino (17); and the depósito aduanero/zona franca code (18 —
  depósito, almacén, Zona Franca or empresas de perfeccionamiento
  activo), linking the declaration to the Task-1 regime profile
  (SV-SPE-FR-003 by id) when goods destine into a regime site.
  (LB-003; EVID-272)
- **SV-SPE-FR-106:** The system shall carry the DUCA transport blocks:
  transportista (19 — customs-assigned registration code + name); modo de
  transporte (20 — aéreo, terrestre, marítimo o multimodal); lugares de
  embarque and desembarque (21/22); conductor block (23 — ID, driver's
  license, expedition country, full name); and the medio-de-transporte
  block (24): unit registration + country, marca, chasis/VIN,
  remolque/semirremolque identifications, count of cargo units,
  security-device numbers (precintos o marchamos — per equipment, placed
  by the customs service, other authorities or the transport/naval
  company), equipment type code (e.g. 14 = Tráiler) + size + load type,
  and container identification numbers — marchamo and container IDs
  being the physical-control keys the `04` traslado records and the `03`
  marchamo duties consume by id.
  (LB-004; EVID-272)
- **SV-SPE-FR-107:** The system shall carry the DUCA value block and
  compute the customs tax base per the printed contract: field 25 *valor
  de transacción* (price actually paid or payable) + field 26 *gastos de
  transporte* + field 27 *gastos de seguro* + field 28 *otros gastos*
  (importer-borne additions/deductions not in the price) = field 29
  **valor en aduana total — "la base para el cálculo de los impuestos
  correspondientes"** (THE customs tax base this localization computes
  duties on); field 30 INCOTERM; field 31 *tasa de cambio* between the
  peso centroamericano ($) and the importing country's currency at the
  acceptance date — a CONFIG-GAP slot with NO shipped behavior
  (post-dollarization operational meaning corpus-silent — SOQ-45/OQ-4);
  the presumed-value rows of FR-118 write fields 26/27 when the importer
  cannot accredit flete/seguro, and the parque almacenaje/conservación
  exclusion of SV-SPE-FR-077 (`04`) feeds this block by id.
  (LB-005; LB-014; EVID-272/269)
- **SV-SPE-FR-108:** The system shall carry the DUCA line model: line
  number (40); país de origen per line (41); unidad de medida (42);
  cantidad (43); ACUERDO code (44 — the treaty/agreement under which the
  line claims a preferential DAI); clasificación arancelaria (45 — SAC
  classification plus national additional codes); descripción (46);
  origen block per line (47 — criterio para certificar origen + reglas
  accesorias per the Reglamento Centroamericano sobre el Origen de las
  Mercancías or the Panamá Protocol Anexo 6(a)); per-line bultos
  count/class (35/36), peso neto/bruto (37/38) and cuota/contingente code
  (39); header totals peso bruto/neto (32/33) summing the lines; and the
  header liquidación general (34 — per-tribute totals + payment modality
  + grand total) aggregated from the per-line liquidación of FR-109.
  (LB-006; LB-007; EVID-272)
- **SV-SPE-FR-109:** The system shall carry the per-line value and
  liquidación contract: fields 48-51 per-line valor de transacción (per
  the GATT Art. VII Agreement), gastos de transporte, seguro and otros
  gastos; field 52 per-line *valor en aduana* — the base imponible for
  DAI application; and field 53 *liquidación por línea* as per-line tax
  rows: tipo (tribute code), alícuota (applied percentage), total per
  tribute, modalidad de pago and the per-line grand total — the
  line-level tax computation surface the regime duty bases of
  `05_tan-iva-interface.md` resolve against by id (non-national
  component, entry-CIF floor), never restated here.
  (LB-008; EVID-272)
- **SV-SPE-FR-110:** The system shall carry DUCA soporte (support)
  documents per the field-54 contract: tipo de documento code (commercial
  invoices, transport documents, certificates), número, fecha de emisión,
  fecha de vencimiento when applicable, país de emisión, issuing
  authority/entity name, and monto when applicable — each document
  attached to lines through the printed LINE-RANGE SYNTAX ("3-5"; "1, 6,
  8"; "3-5, 8"), stored verbatim AND parsed into line references (range
  expansion + list), with an invalid-range rejection naming the offending
  expression.
  (LB-009; EVID-272)
- **SV-SPE-FR-111:** The system shall carry the origin-declaration
  complementarity per fields 61/62: *declaración de origen* (61) — the
  PRODUCER declares the origin of the goods to be exported (country +
  signatory name, company and position) — and *certificación de origen*
  (62) — the EXPORTER certifies origin (same data) — as complementary
  records where, when the producer IS the exporter, field 61 need not be
  filled (both prints agree); plus field 59 código de exportador and
  field 60 firma del declarante on the same surface; fields 57/58
  (aduanas signatures/seals; ventanilla única/BCR authorization) are
  authority-side read-only boxes mirrored but never system-generated.
  (LB-010; EVID-272)
- **SV-SPE-FR-112:** The system shall treat the 43_ 62-field instructivo
  as the COMPLETE printed field contract of the DUCA record — mirroring
  every printed field — while inventing NO mandatory-vs-optional
  obligation beyond it: which fields are obligatory or optional per
  operation lives in the Comité Aduanero DUCA user manual, NOT in the
  corpus (SOQ-36/OQ-3), so field-level requiredness ships as config
  slots with NO defaults; the DUCA reverso (tránsito-side aduana de
  partida/paso/destino, dispositivos de seguridad, ruta, plazos en
  horas) is *de uso exclusivo de la Autoridad Aduanera* and is mirrored
  read-only for DUCA-T records.
  (LB-001; EVID-272)

### 3.2 DUCA-F FAUCA validity — declaration-record surface (43_ field 56)

- **SV-SPE-FR-113:** The system shall stamp, on the DUCA declaration
  record, field 56 *válida hasta*: when the declaration serves as FAUCA
  (Formulario Aduanero Único Centroamericano), it is valid for 30 días
  hábiles from its EMISSION, and that validity applies ONLY in the
  country of exportation of the goods — the record carries the computed
  validity date (días-hábiles arithmetic consumed from
  SV-FREP-FR-202..204 by id) plus the export-country-only scope flag;
  the CLOCK view of this same rule is consumed BY ID from SV-SPE-FR-081
  (`04_customs-clocks.md` — ownership split per its OQ-6: this FR owns
  the declaration-record field surface, that FR owns the expiry
  computation row; the two reference each other by id and duplicate
  nothing).
  (LB-010; EVID-272)

### 3.3 Teledespacho legal chassis (74_ Arts. 6/8)

- **SV-SPE-FR-114:** The system shall implement the teledespacho legal
  chassis on every declaration-transmission surface: declarations are
  effected by electronic transmission per the DGA-established
  lineamientos and formatos, under procedures ensuring the AUTENTICIDAD,
  CONFIDENCIALIDAD, INTEGRIDAD and NO REPUDIACIÓN of the information
  transmitted; documents in magnetic/digital/electronic support produce
  the SAME legal effects as paper (including the customs-value
  declaration and every attached electronic document); a statutory
  requirement that information be presented or conserved in its original
  form is satisfied by a data message whose content is accessible for
  later consultation; DGA registers may be electronic and administrative
  acts may be notified by electronic data message; and no provision
  barring the admission of a data message as evidence applies — the
  mirroring surfaces (DUCA records, soporte attachments, notification
  receipts) are stored with accessibility-for-later-consultation
  guarantees, never as inferior-grade copies.
  (LB-011; EVID-269)
- **SV-SPE-FR-115:** The system shall implement the digital-signature
  layer of the teledespacho: transmission identity is established
  through the certifying-entity regime (entidades certificadoras —
  authorized, audited and sanctioned by the Ministerio de Hacienda),
  where each authorized user holds a unique corresponding PUBLIC/PRIVATE
  key pair whose linking constitutes the *firma digital* — the legal
  digital substitute of the handwritten signature, letting the receiver
  verify the transmitter's identity with certainty and barring later
  denial of authorship; the system records the declarante's
  signature/certificate references on each transmitted declaration
  (never managing keys itself — certifying entities are external); and it
  carries the statutory confidentiality duties as user-profile flags:
  suscriptores must keep their private keys secret and answer for
  misuse, and Auxiliares de la Función Pública Aduanera are PROHIBITED
  from revealing or allowing third-party use of their clave de acceso or
  firma digital, including to their own authorized assistants.
  (LB-012; EVID-269)

### 3.4 The $18 non-intrusive-inspection tasa (74_ Arts. 12-B/12-C)

- **SV-SPE-FR-116:** The system shall carry the non-intrusive-inspection
  tasa as a DATED fee row consumed per transmission: amount $18.00
  (dieciocho dólares de los Estados Unidos de América — the 2012-printed
  value, IVA-INCLUDED), charged per electronic transmission of a
  manifiesto, DM to any customs regime, FAUCA, or internal/international
  tránsito (or other declaration/form covering the transport, traslado
  or movement of goods into/out of the national customs territory) via
  any authorized capture platform; the obligation arises on the entry or
  exit of goods or transport means by any route; payment is due AT THE
  MOMENT of transmission (anchor = transmission date; snapshot on the
  declaration); the fee is DESPACHO-BLOCKING — despacho authorization is
  not available while the tasa is unpaid — with responsible subjects the
  declarants or their representatives; nonpayment sanction consequences
  are a LESIA pointer only (SOQ-32/OQ-6 — zero mechanics); and the row
  carries the Art. 12-C REVISION MECHANISM as a dated-value watch:
  revisable and adjustable every two years by the Ministerio de Hacienda
  up to a maximum of 10 percent over the prior value, by reasoned
  Acuerdo Ejecutivo (SOQ-34/OQ-1 — the shipped row keeps $18 with the
  2012-print provenance until an adjusting acuerdo is acquired).
  (LB-013; EVID-270)

### 3.5 Pre-arrival manifiesto + presumed valuation (74_ Art. 2)

- **SV-SPE-FR-117:** The system shall carry the pre-arrival manifiesto
  duty as a manifest-record surface: BEFORE the goods' arrival at the
  national customs territory, transportists (land, sea or air) or
  agentes de transporte provide the ingress aduana — by electronic
  transmission or another DGA-authorized means — the general cargo
  manifiesto information, where the goods information consigns the peso
  bruto in kilograms, the clase and cantidad of bultos, and the generic
  class/type of goods DETAILING FIRST AND IN DESCENDING ORDER those of
  greatest commercial value (an ordered goods list on the manifiesto
  record, not a free-text note).
  (LB-014; EVID-269)
- **SV-SPE-FR-118:** The system shall carry the presumed-valuation
  fallbacks as DATED config rows (SOQ-35/OQ-2) feeding DUCA fields 26/27
  of FR-107 when the importer cannot accredit the real amounts: seguro —
  1.25% over FOB value for transporte regional terrestre de carga, and
  1.50% over FOB value for transporte internacional de carga regardless
  of transport mode, applicable when no póliza was contracted; flete —
  10% over FOB value when unaccredited, with the DGA's periodically
  established reference values (published, consulted with transport
  guilds) as the LIVING alternative carried as a config-gap slot with NO
  shipped values; each presumed line is flagged presumed (not accredited)
  on the value block; anchor = DM acceptance date, snapshot on the
  record; and transport, loading/unloading/handling and insurance costs
  to the port/place of importation are included in valor en aduana per
  the GATT Article VII Agreement number-2 rule as printed ("Art.8 del
  Acuerdo" — agreement-article numbering, [as printed]).
  (LB-014; EVID-269)

### 3.6 Autoliquidación + selectividad + non-intrusive inspection (74_ Arts. 3/12/12-A)

- **SV-SPE-FR-119:** The system shall implement autoliquidación
  (self-determination): the DECLARANT determines the customs tax
  obligation, complies with the other applicable regulations, presents
  the goods declaration and pays the tributes caused — the declaration's
  liquidación rows (FR-109) are the declarant's own determination, and
  DGA liquidación oficiosa is recorded as an exceptional authority
  determination on breach found by immediate verification or
  a-posteriori fiscalización (feeding the FR-122 payment clock and the
  FR-128 procedure clocks), never as a system-side recomputation.
  (LB-015; EVID-270)
- **SV-SPE-FR-120:** The system shall record the selectividad and
  non-intrusive-inspection surfaces as authority-side read-only data on
  the declaration: autoliquidated DMs are submitted to a SELECTIVE AND
  RANDOM process deciding whether immediate verification proceeds (which
  never limits posterior fiscalización); non-intrusive inspection
  equipment is used per risk analysis; and where an inspection evidences
  an ilícito, the certified images remitted to competent authorities are
  PLENA PRUEBA in the penal process, with the reproduced images carrying
  the same probatory value in administrative processes — the system
  stores inspection-result references and never generates or alters
  them.
  (LB-015; EVID-270)

### 3.7 Payment and anulación clocks (74_ Art. 11)

- **SV-SPE-FR-121:** The system shall implement the acceptance rule and
  the pre-transfer gate: every good destined to a customs regime is
  covered by a declaration, accepted upon REGISTRATION in the
  DGA-authorized system (the DUCA field-3 stamp of FR-104) — an
  acceptance that does not endorse content and never limits posterior
  verification/fiscalización/liquidación; and for the TRANSFER OR SALE of
  goods imported under SUSPENSIVE and LIBERATORY customs regimes, the
  definitive-import declaration cancelling the regime must be PRESENTED
  AND PAID BEFORE the transfer or sale — a blocking gate on the
  goods-transfer surfaces consumed by the `04` traslado records and the
  `05` internación routing by id (a regime-goods transfer whose
  cancelling DM is not presented-and-paid stays blocked).
  (LB-016; EVID-270)
- **SV-SPE-FR-122:** The system shall run the 8-días-hábiles payment
  clock: tributes and fines of SANCIONES and LIQUIDACIONES DE OFICIO are
  payable within eight días hábiles following notification of the
  resolución definitiva (días-hábiles arithmetic consumed from
  SV-FREP-FR-202..204 by id; anchor = notification date; the
  8-días-hábiles payment of the simplified procedure of FR-124 rides the
  same engine with its presentation anchor).
  (LB-016; LB-017; EVID-270)
- **SV-SPE-FR-123:** The system shall run the declaration anulación
  clocks from registration: a teledespachada declaration registered in
  the DGA system and NOT presented within the plazo de diez días (as
  printed — no hábiles qualifier) is annulled de oficio (state
  annulled_10d); a declaration in the same condition whose tributes were
  PAID is annulled within the plazo de sesenta días (as printed)
  following its registration (state annulled_60d) — in the latter case
  the record opens the DEVOLUCIÓN route: the interested party may file
  the solicitud de devolución de impuestos before the corresponding
  customs authority (a devolución-request flag + filing reference on the
  declaration; the refund computation itself is not modeled — authority
  process).
  (LB-016; EVID-270)

### 3.8 Simplified withdrawal + courier bands (74_ Art. 11-A)

- **SV-SPE-FR-124:** The system shall carry the 48-hour simplified
  withdrawal as an authorization-tracked procedure: withdrawal of goods
  from customs precincts WITHOUT final determination of tariffs, taxes
  and charges, within the FORTY-EIGHT HOURS following the goods' arrival;
  authorization by resolución razonada for ONE YEAR, prorrogable at DGA
  criteria (or per a DGA-courier convenio — WCO immediate-release
  directrices kin); the requisito set recorded on the authorization
  (solicitud data, personería, justification by volumes/recaudation,
  no pending fiscal debts, no recidivist customs sanctions in the last
  six months, adequate installations, and the sufficient GARANTÍA —
  depósito or fianza, one-year, DGA-authorized, covering definitive
  payment of duties, taxes and charges); the SS-solvency requirement
  (ISSS + AFPs cotizaciones of the THIRTY DAYS prior to the application)
  consumed from the SS-solvency gate SV-SPE-FR-102 (`05`) by id, never
  restated; determined import tributes payable within 8 días hábiles of
  the declaration's presentation (FR-122 engine); and breach of the
  authorization/convenio conditions recording revocation with garantía
  execution and suspension of customs operations until payment.
  (LB-017; EVID-270)
- **SV-SPE-FR-125:** The system shall route courier shipments by their
  FOB bands on the withdrawal surface (DGA-courier convenio frame):
  FOB value UNDER US$200.00 — withdrawal authorized on presentation of
  the guía aérea and the factura by the courier operator (no factura ⇒
  the DGA Valoración department's reference values — config-gap slot, no
  shipped values); FOB value OVER US$200.00 and NOT exceeding
  US$3,000.00 — withdrawal authorized on presentation of the
  declaración de mercancías; and CONSOLIDATION of declarations permitted
  only while the summed FOB of every consolidated merchandise stays at
  or under US$3,000.00 per courier operator — a consolidation that would
  cross US$3,000.00 is rejected naming the band breach.
  (LB-017; EVID-270)

### 3.9 Fiscalización: caducidad, retention, notification, procedure (74_ Arts. 13-17)

- **SV-SPE-FR-126:** The system shall implement the customs 5-year
  retention floors as record-retention metadata: formal-accounting
  subjects' registros contables (and non-formal subjects' registros
  especiales) plus their support documentation remain at the customs
  authority's disposal for FIVE YEARS; and exporters/producers conserve
  certificaciones o certificados de origen plus all records and
  documents demonstrating origin for a MINIMUM OF FIVE YEARS FROM
  EMISSION — the customs 5y row is NOTED into the canonical retention
  matrix of `commercial-legal/02_accounting-books.md` §3.7 BY ID
  (SV-CML-FR-028 — update-by-note only: this file adds the customs row's
  existence, objects and anchor to that matrix; the matrix, its
  longest-per-object rule and its purge machinery are NEVER restated
  here).
  (LB-018; EVID-271)
- **SV-SPE-FR-127:** The system shall run a per-DM verification-caducidad
  tracker: the DGA's posterior-verification term CADUCA five years
  counted from the ACCEPTANCE date of the corresponding DM (anchor = DUCA
  field 3 of FR-104) — each declaration carries an open/closed
  verification-window state stamped from its acceptance date; this
  tracker is DISTINCT from every T4 regime clock (SV-SPE-FR-064..081 by
  id — those time the GOODS' permanence under a regime; this times the
  AUTHORITY's verification power over the declaration) and the two are
  never merged into one clock family.
  (LB-018; EVID-271)
- **SV-SPE-FR-128:** The system shall record fiscalización notifications
  and run the procedure clocks: results notified to the declarante or
  their agente de aduanas per the Art. 16 channels — including la vía
  electrónica — with the substitute-recipient ladder, door esquela and
  72-hour edicto fallbacks as notification-method metadata; and the rule
  that notification to the AGENTE EXTENDS TO THE DECLARANT (the mandate
  relation) recorded as a notification-scope flag; the administrative
  process clocks (días-hábiles engine by id): apertura notified with the
  FULL fiscalization informe; 15 días hábiles from the day after
  notification for alegatos and discharge proofs; DGA resolution within
  20 días hábiles, notified within 20 días hábiles of emission with the
  full text; recursos against liquidación oficiosa per LESIA — POINTER
  ONLY (SOQ-32/OQ-6: LESIA absent; zero recourse mechanics invented).
  (LB-019; EVID-271)

### 3.10 SIECA/Panamá DUCA-F interchange — dated operational row (42_)

- **SV-SPE-FR-129:** The system shall carry the DUCA-F SV↔Panamá
  electronic-transmission surface as a DATED OPERATIONAL row with an
  external-interface assumption: since 2025-03-03, export/import
  operations between El Salvador and Panamá under DUCA-F transmit
  electronically via SIECA (capture portal ducaf.sieca.int —
  PortalCapturaPanama for Panama-origin registrations); exporters ensure
  SIECA-portal TOKEN availability; foreign acceptance arrives in ~37
  seconds; the destination aduana's declaration number is visible
  (facilitating tax payment) with more agile border despacho;
  participating institutions BCR/CIEX, DGA, SIECA and ANA Panamá; the
  Odoo surface records the DUCA-F↔export-invoice pairing (FEXE —
  SV-EINV-FR-042 by id), the token/acceptance metadata and the
  destination declaration-number reference on the DUCA-F record — the
  portal itself is an EXTERNAL INTERFACE (integration mechanics are an
  assumption note, not a statutory surface; valid_from = 2025-03-03
  dated row).
  (LB-020; EVID-273)

## 4. Data Model

Layer semantics: the customs-declaration surfaces are Odoo-native records
and dated config rows, living under the `l10n_sv_customs.*` namespace —
this file owns the customs-declaration layer of the localization
(deliberate namespace split: DUCA covers ordinary terceros-países imports
too, not only regime traffic), while the regime module of files 01-05
(`l10n_sv_special_regime.*`) links to it by m2o (the `04` clock chassis
points at the DUCA record; the `05` SS-solvency gate gates this file's
withdrawals). Every FR maps `odoo` (see §5). The DGA/SIECA systems are
external authorities: the model mirrors declaration data and
authority-issued facts (registration numbers, acceptance, inspections,
notifications), it does not emulate them. No printed data table warrants
a CSV sidecar (the 62-field instructivo is the field contract itself —
mirrored as model fields; the tasa/presumed rows are few; default none
per plan, judgment noted in the task report).

**DUCA header (l10n_sv_customs.duca):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_customs.duca | variant | select | d (terceros países / not DUCA-F) · t (tránsito internacional terrestre) · f (originarios región centroamericana) | FR-103 |
| l10n_sv_customs.duca | declarante_correlativo · registration_number · acceptance_date | char · char (readonly) · date | field 1 declarant-assigned; field 2 DGA-system-assigned; field 3 = acceptance (74_ Art. 11 registration event; anchor for FR-127 caducidad + T4 clocks by id) | FR-104 |
| l10n_sv_customs.duca | exportador_proveedor_id · importador_destinatario_id · declarante_id | m2o res.partner ×3 + doc-type/país-emisión/domicilio-fiscal fields | fields 4/5/6 blocks; declarante resolves from SV-SPE-FR-020 config by id | FR-104 |
| l10n_sv_customs.duca | aduana_registro · aduana_salida · aduana_ingreso · aduana_destino | m2o catalog ×4 | fields 7-10 (customs-office codes) | FR-105 |
| l10n_sv_customs.duca | regimen_aduanero · modalidad · clase | m2o catalogs ×3 | field 11 regime; field 12 modality (courier, envíos postales, encomiendas, equipajes…); field 13 class (simplificada, acumulada, provisional, complementaria…) | FR-105 |
| l10n_sv_customs.duca | regimen_expiry_date | date | **field 14 fecha de vencimiento del régimen** — consumed by SV-SPE-FR-080 by id (mismatch flag; field numbering as printed — 04 OQ-2 kin) | FR-105 |
| l10n_sv_customs.duca | pais_procedencia · pais_exportacion · pais_destino · deposito_zf_code | m2o ×3 · char | fields 15-17; field 18 depósito/almacén/ZF/perfeccionamiento-activo code (links SV-SPE-FR-003 profile by id) | FR-105 |
| l10n_sv_customs.duca | transportista_code · transportista_name · modo_transporte · lugar_embarque · lugar_desembarque · conductor_* | char/select/date fields | fields 19-23 (conductor: ID, licencia, país, nombre) | FR-106 |
| l10n_sv_customs.duca | medio_transporte_* | char fields + int | field 24: matrícula, país, marca, chasis/VIN, remolques, cargo-unit count, **marchamos/precintos**, equipamiento código/tamaño/tipo carga, **contenedor IDs** | FR-106 |
| l10n_sv_customs.duca | valor_transaccion · gastos_transporte · gastos_seguro · otros_gastos · valor_en_aduana_total | monetary ×5 | fields 25-29; field 29 = THE tax base (computed 25+26+27+28; presumed rows flag 26/27) | FR-107 |
| l10n_sv_customs.duca | incoterm · tasa_cambio | char · monetary (config-gap) | field 30; field 31 peso-centroamericano exchange rate — NO shipped behavior (SOQ-45/OQ-4) | FR-107 |
| l10n_sv_customs.duca | peso_bruto_total · peso_neto_total · liquidacion_general | monetary · monetary · one2many | fields 32/33 line-summed totals; field 34 general liquidación (tipo/total por tributo/modalidad/total general) | FR-108 |
| l10n_sv_customs.duca | observaciones · valida_hasta · valida_scope_export_country | text · date · boolean | field 55; field 56 computed 30 días hábiles from emission in the FAUCA role, export-country-only (clock view = SV-SPE-FR-081 by id; ownership-split OQ) | FR-113 |
| l10n_sv_customs.duca | codigo_exportador · declaracion_origen · certificacion_origen | char · block · block | field 59; fields 61/62 complementarity (producer declares / exporter certifies; 61 suppressed when producer = exporter) | FR-111 |
| l10n_sv_customs.duca | state · tasa_paid | select · boolean | draft · accepted · presented · paid · annulled_10d · annulled_60d · devolucion_requested; $18 tasa payment flag (despacho-blocking) | FR-116, FR-121, FR-123 |
| l10n_sv_customs.duca | firma_refs · authority_boxes | char (readonly) ×2 | field 60 declarant signature/certificate refs (FR-115); fields 57/58 authority-side read-only | FR-111, FR-115 |
| l10n_sv_customs.duca | field_requiredness | config slots | mandatory-vs-optional per the absent Comité Aduanero manual — NO defaults (SOQ-36/OQ-3) | FR-112 |

**DUCA lines + per-line liquidación (l10n_sv_customs.duca.line / .line.liquidacion):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_customs.duca.line | numero · pais_origen · unidad · cantidad · cuota_contingente | int · m2o · m2o · qty · char | fields 40-43 + 39 | FR-108 |
| l10n_sv_customs.duca.line | acuerdo · clasificacion_sac · codigos_nacionales · descripcion | m2o · char (SAC) · char · text | field 44 preferential-DAI agreement; field 45 SAC + national additional codes; field 46 description | FR-108 |
| l10n_sv_customs.duca.line | origen_criterio · reglas_accesorias | char · char | field 47 (Reglamento Centroamericano de Origen / Panamá Anexo 6(a)) | FR-108 |
| l10n_sv_customs.duca.line | cantidad_bultos · clase_bultos · peso_neto · peso_bruto | int · m2o · monetary · monetary | fields 35-38 (per line) | FR-108 |
| l10n_sv_customs.duca.line | valor_transaccion · gastos_transporte · seguro · otros_gastos · valor_en_aduana | monetary ×5 | fields 48-52; field 52 = per-line base imponible for DAI | FR-109 |
| l10n_sv_customs.duca.line.liquidacion | tipo · alicuota · total · modalidad_pago · total_general | char · pct · monetary · char · monetary | fields 53.1-53.5 per-line tax rows | FR-109 |

**Soporte documents (l10n_sv_customs.duca.soporte):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_customs.duca.soporte | tipo · numero · fecha_emision · fecha_vencimiento · pais_emision | m2o · char · date · date · m2o | fields 54.1-54.5 (invoices, transport documents, certificates) | FR-110 |
| l10n_sv_customs.duca.soporte | line_range · line_refs | char (verbatim) · m2m duca.line | field 54.6 — printed syntax "3-5"; "1, 6, 8"; "3-5, 8" stored verbatim AND parsed; invalid ranges rejected | FR-110 |
| l10n_sv_customs.duca.soporte | autoridad_emisora · monto | char · monetary | fields 54.7/54.8 | FR-110 |

**Dated config rows + trackers (l10n_sv_customs.*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_customs.inspection_tasa | amount · valid_from · provenance · revision_rule | monetary · date · char · char | $18.00 (dieciocho dólares, IVA-included) per manifiesto/DM/FAUCA/tránsito transmission; valid_from = 74_ Art. 12-B 2012 print; biennial ≤10% Acuerdo Ejecutivo watch (SOQ-34/OQ-1); anchor = transmission date | FR-116 |
| l10n_sv_customs.presumed_value | kind · pct · basis · valid_from · provenance | select · pct · select (FOB) · date · char | seguro_regional_1_25 · seguro_internacional_1_50 · flete_10 (74_ Art. 2 reform-3 print — SOQ-35/OQ-2); DGA periodic flete reference values = config-gap slot, NO shipped values; anchor = DM acceptance | FR-118 |
| l10n_sv_customs.manifiesto | transportista/agente · arrival_ref · peso_bruto_kg · bultos_clase/cantidad · goods_descending_value | fields | pre-arrival manifiesto record (descending-commercial-value ordered goods list) | FR-117 |
| l10n_sv_customs.verification_window | dm · anchor_date · expiry_date · state | m2o · date · date (+5y) · select | per-DM caducidad: 5 years from DM acceptance (DUCA field 3); open · closed — NEVER merged with T4 regime clocks | FR-127 |
| l10n_sv_customs.simplified_withdrawal | authorization_ref · valid_from/to (1y) · garantia_ref · solvencias_refs · convenio_flag · payment_due | char · dates · char · m2o payroll by id · boolean · date | 48-hour withdrawal authorization (resolución razonada; SS gate = SV-SPE-FR-102 by id); payment 8 días hábiles from presentation | FR-124 |
| l10n_sv_customs.duca (courier routing) | courier_band · withdrawal_route · consolidation_group | computed select · select · m2o | under_200 (guía aérea + factura; no-invoice ⇒ DGA reference-values slot) · 200_to_3000 (DM withdrawal); consolidation cap ≤ US$3,000 summed FOB per courier operator | FR-125 |

## 5. Odoo Mapping

Layer semantics for this wave: the customs-declaration surfaces are
Odoo-native (DUCA records mirroring declarations, dated config rows for
the tasa/presumed values, trackers on the acceptance anchors) — every FR
maps `odoo`; no SaaS rows are introduced because none of these FRs touch
DTE generation/transmission (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2 — the FEXE pairing of
FR-129 READS the e-invoicing document by id). The SIECA portal and the
DGA systems are EXTERNAL interfaces: the system records their
authority-issued outputs (registration numbers, acceptance, inspection
references, notifications), it never emulates transmission authority.
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-103 | odoo | l10n_sv_customs.duca | variant d/t/f | ONE model, variant flag; FAUCA/DM/DUT function integration; ampliation sheets; the DM surface the 04 clock chassis links to by id |
| FR-104 | odoo | l10n_sv_customs.duca | correlativo/registration_number/acceptance_date + identity blocks | field 3 = acceptance anchor (caducidad FR-127 + T4 anchors by id); declarante resolves from SV-SPE-FR-020 by id |
| FR-105 | odoo | l10n_sv_customs.duca | aduanas/regimen/modalidad/clase/regimen_expiry_date/países/depósito code | field 14 consumed by SV-SPE-FR-080 by id (mismatch flag, no auto-overwrite; 04 OQ-2 field-numbering kin); field 18 links the regime profile by id |
| FR-106 | odoo | l10n_sv_customs.duca | transport/conductor/medio blocks incl. marchamos + container IDs | marchamo/container keys consumed by 03 duties + 04 traslados by id |
| FR-107 | odoo | l10n_sv_customs.duca | value block 25-29 + incoterm + tasa_cambio | field 29 = THE tax base; presumed rows write 26/27 flagged; SV-SPE-FR-077 exclusion feeds by id; field 31 = config-gap NO default (SOQ-45/OQ-4) |
| FR-108 | odoo | l10n_sv_customs.duca.line | fields 35-47 + header totals 32/33 + liquidación general 34 | SAC + national codes; ACUERDO preferential DAI; origen criterio/reglas accesorias |
| FR-109 | odoo | l10n_sv_customs.duca.line(.liquidacion) | fields 48-52 + 53.1-53.5 | per-line valor en aduana = DAI base; per-line tax rows feed 05 duty bases by id |
| FR-110 | odoo | l10n_sv_customs.duca.soporte | tipo/número/fechas/país + line_range verbatim + parsed m2m | printed syntax "3-5"; "1, 6, 8"; "3-5, 8"; invalid ranges rejected |
| FR-111 | odoo | l10n_sv_customs.duca | declaración/certificación de origen + código exportador + firma refs | 61/62 complementarity (61 suppressed when producer = exporter); 57/58 authority boxes read-only |
| FR-112 | odoo | l10n_sv_customs.duca | field_requiredness config slots | 62-field instructivo = the complete contract; NO invented mandatory/optional (SOQ-36/OQ-3); reverso read-only (DUCA-T) |
| FR-113 | odoo | l10n_sv_customs.duca | valida_hasta + export-country scope flag | 30 días hábiles from emission, FAUCA role; clock view = SV-SPE-FR-081 by id (ownership split, 04 OQ-6); engine SV-FREP-FR-202..204 by id |
| FR-114 | odoo | l10n_sv_customs.duca (+attachment surfaces) | electronic-legal-effects storage | data message = paper; accessibility-for-later-consultation guarantee; electronic registers/notifications mirrored |
| FR-115 | odoo | res.users/res.partner (declarante profiles) | signature/certificate refs + confidentiality-duty flags | certifying entities external; key-pair/firma-digital refs recorded, never managed; auxiliaries' disclosure prohibition flagged |
| FR-116 | odoo | l10n_sv_customs.inspection_tasa (+duca.tasa_paid) | $18.00 dated row | IVA-included; due AT transmission; DESPACHO-BLOCKING; biennial ≤10% revision watch (SOQ-34/OQ-1); LESIA pointer only (OQ-6) |
| FR-117 | odoo | l10n_sv_customs.manifiesto | pre-arrival fields | peso bruto kg, clase/cantidad bultos, goods by DESCENDING commercial value |
| FR-118 | odoo | l10n_sv_customs.presumed_value | 1.25%/1.50%/10% FOB dated rows | feeds fields 26/27 flagged presumed; DGA reference flete values = config-gap (SOQ-35/OQ-2); anchor = DM acceptance |
| FR-119 | odoo | l10n_sv_customs.duca | liquidación ownership = declarant | autoliquidación; liquidación oficiosa = authority determination record only |
| FR-120 | odoo | l10n_sv_customs.duca | selectividad/inspection refs (read-only) | selective-random channel result; certified images = plena prueba, never system-generated |
| FR-121 | odoo | l10n_sv_customs.duca + transfer surfaces | acceptance stamp + pre-transfer presented-and-paid gate | blocks 04 traslado / 05 internación surfaces by id until the cancelling DM is presented AND paid |
| FR-122 | odoo | l10n_sv_customs.duca (payment clock) | 8 días hábiles from notification | engine SV-FREP-FR-202..204 by id; rides also the simplified-procedure presentation anchor |
| FR-123 | odoo | l10n_sv_customs.duca | annulled_10d / annulled_60d + devolución flag | 10 and 60 days AS PRINTED (no hábiles qualifier in the text); devolución route = request flag + filing ref (refund not modeled) |
| FR-124 | odoo | l10n_sv_customs.simplified_withdrawal | 1-y authorization + garantía + solvencias + 48h window | SS gate = SV-SPE-FR-102 by id; payment 8 días hábiles from presentation; revocation ⇒ garantía execution + operations suspension |
| FR-125 | odoo | l10n_sv_customs.duca | courier_band/withdrawal_route/consolidation_group | $200 guía+factura / ≤$3,000 DM withdrawal; consolidation cap ≤ US$3,000 summed FOB per courier operator |
| FR-126 | odoo | retention metadata on records + origin certificates | 5y availability rows | customs 5y row noted into SV-CML-FR-028 by id (update-by-note; matrix never restated) |
| FR-127 | odoo | l10n_sv_customs.verification_window | per-DM 5y caducidad tracker | anchor = DUCA field 3; NEVER merged with the T4 regime-clock family |
| FR-128 | odoo | l10n_sv_customs.duca (notification/procedure metadata) | electronic channels + agent-extends flag + 15/20 días hábiles clocks | engine SV-FREP-FR-202..204 by id; recursos = LESIA pointer only (SOQ-32/OQ-6) |
| FR-129 | odoo | l10n_sv_customs.duca (DUCA-F export records) | SIECA tokens/acceptance metadata + destination declaration-number ref | EXTERNAL-INTERFACE assumption (ducaf.sieca.int); FEXE pairing = SV-EINV-FR-042 by id; dated row valid_from 2025-03-03 |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file ($18.00 tasa with its biennial ≤10% revision mechanism, the
1.25%/1.50%/10% presumed percentages, the $200/$3,000 courier bands, the
30-días-hábiles DUCA-F FAUCA validity, the 8-días-hábiles payment clock,
the 10-day and 60-day anulación plazos, the 5-year retention/caducidad
terms, the 15/20-días-hábiles procedure clocks) are code-text values
cited as printed under the SOQ-30 verification watch (§2) and live as
dated config rows with instrument provenance — never constants; each
resolves as-of its domain anchor (transmission · DM acceptance ·
notification · emission · registration) with snapshot-on-write. Mid-year
go-live (D18): a migrating company's DUCA records, open anulación and
verification-window states ingest as `is_historical` rows with
original-period semantics (tiered ingestion; no re-derivation — the
caducidad anchors of imported declarations keep their original acceptance
dates). No hard gates beyond the statutory blocks (D16 no-override: the
despacho-blocking tasa gate and the pre-transfer presented-and-paid gate
are never bypassed by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a DUCA-F emitted 2026-06-01 serving as FAUCA, when
  the record stamps field 56, then válida hasta computes 30 días hábiles
  from emission with the export-country-only scope flag set — an
  in-country use at día hábil 31 never consumes this validity, and the
  expiry computation row is the one SV-SPE-FR-081 (`04`) owns by id
  (FR-113).
- **AC-002:** Given a US$10,000 FOB importation with unaccredited flete
  and unaccredited international-cargo seguro, when the value block
  builds, then field 26 receives the $1,000 (10% FOB) presumed line and
  field 27 the $150 (1.50% FOB) presumed line — both flagged presumed —
  and the valor en aduana total (field 29) grows accordingly as the tax
  base (FR-107, FR-118).
- **AC-003:** Given goods imported under a suspensive regime whose
  holder attempts a transfer or sale, when the cancelling
  definitive-import DM is not yet presented AND paid, then the transfer
  stays blocked; once the DM is presented and paid, the gate opens
  (FR-121).
- **AC-004:** Given a manifiesto transmission with the $18 inspection
  tasa unpaid, when despacho authorization is requested, then it is
  refused — the fee row is despacho-blocking — and the payment stamp
  lands on the declaration at transmission time (FR-116).
- **AC-005:** Given a teledespachada declaration registered 2026-04-01
  with tributes PAID and never presented, when day 61 arrives, then the
  state stamps annulled_60d with the devolución route open (solicitud
  de devolución flag + filing reference); its unpaid twin stamps
  annulled_10d on day 11 with no devolución route (FR-123).
- **AC-006:** Given a liquidación de oficio notified 2026-05-04
  (resolución definitiva), when the payment deadline computes, then it
  falls 8 días hábiles after notification via the días-hábiles engine
  consumed by id (FR-122).
- **AC-007:** Given courier shipments of FOB $150, $2,500, $1,800 and
  $1,500, when routed, then the $150 shipment withdraws on guía aérea +
  factura, the $2,500 on its DM, the pair $1,800+$1,100 ($2,900)
  consolidates under the US$3,000 per-operator cap — and a $1,800+
  $1,500 ($3,300) consolidation is rejected naming the band breach
  (FR-125).
- **AC-008:** Given a soporte document whose line-range field reads
  "3-5, 8", when saved, then the document links lines 3, 4, 5 and 8 with
  the verbatim expression preserved; a range "3-5; 9x" fails with the
  offending expression named (FR-110).
- **AC-009:** Given a DM accepted (field 3) 2026-01-10, when the
  verification-window tracker computes, then the caducidad closes
  2031-01-10 and the window is a tracker of its own — never one of the
  T4 regime clock kinds (FR-127).
- **AC-010:** Given a DUCA-F export to Panamá transmitted via SIECA on
  2026-07-15, when the acceptance metadata records, then the ~37-second
  foreign-acceptance timestamp and the destination declaration number
  land on the DUCA-F record, paired with its FEXE by id, under the
  external-interface assumption note (FR-129).
- **AC-011:** Given an export where the producer IS the exporter, when
  the origin block fills, then only the certificación de origen (field
  62) is completed and the declaración de origen (field 61) stays
  suppressed per both prints; a third-party producer export fills BOTH
  (FR-111).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-34 carried: the $18 inspection tasa is the 2012-printed value (74_ Art. 12-B as consolidated through D.L. 23-2012) — Art. 12-C biennial ≤10% Acuerdo Ejecutivo revisions since 2012 could have compounded it. FR-116 ships $18.00 as a dated row with the 2012 print provenance and the revision mechanism recorded; hunt the adjusting acuerdos before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-2 | SOQ-35 carried: the presumed percentages (seguro 1.25% regional-land / 1.50% international; flete 10% FOB) are dated rows from the 74_ Art. 2 print, and the DGA's periodic flete reference values are LIVING data — FR-118 carries them as dated config rows + a config-gap slot with NO shipped values; verify currency at implementation. | no | Takumi S7 (config watch) | open |
| OQ-3 | SOQ-36 carried: the Comité Aduanero DUCA user manual (mandatory-vs-optional fields per operation) is NOT in the corpus, and the Res. 409-2018 supersession status is unverified (2018 text assumed current). FR-112 mirrors the 62-field contract with NO invented field obligations; field-numbering reconciliation kin with 04's OQ-2 (this file cites fields 14/56 as printed). Acquisition candidate. | no | Takumi S7 (sources watch) | open |
| OQ-4 | SOQ-45 carried: DUCA field 31 "tasa de cambio" (peso centroamericano vs import-country currency at acceptance) — operational meaning post-dollarization is corpus-silent; FR-107 ships it as a config-gap slot with NO default behavior. | no | Takumi S7 (config watch) | open |
| OQ-5 | SOQ-30 carried: the 74_ consolidation ends at D.L. 23-2012 and 43_/42_ are the 2018 print / 2025 comunicado — post-cutoff reforms unverified until official routes recover; every LB in this file cites as printed; a post-cutoff reform may move the tasa, the presumed percentages, the anulación plazos, the procedure clocks or the DUCA field layout — re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-6 | SOQ-32 kin (shared with 04's OQ-1): LESIA is cited by 74_ Art. 12-B (tasa-nonpayment sanctions) and Art. 17 (recursos against liquidación oficiosa) but is NOT in the corpus — FR-116/FR-128 record pointers ONLY, zero sanction/recourse mechanics invented; shared acquisition candidate with the 12_/74_ family (consumed by `07` for the sanction ladders). | no | Takumi S7 (sources watch) | open |
