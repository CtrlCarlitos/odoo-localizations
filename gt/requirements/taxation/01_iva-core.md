# GT — Taxation — IVA régimen general (core regime)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala *Impuesto al
Valor Agregado* (IVA, value-added tax) **régimen general** (general regime,
statutorily "Régimen Normal o General": monthly débito−crédito netting): the
*hecho generador* (taxable-event) taxonomy and minimum-base floor (Art. 3);
the *momento de pago* (tax point) rules (Art. 4); the *tarifa única* (single
rate) 12% price-inclusive model with its earmark split as dated rows (Art.
10, GOQ-64 vintage caveat); objective exemptions (Art. 7) and subjective
exemptions with the *constancia de exención* (exemption certificate) flow
(Arts. 8/9); *base imponible* (taxable base) rules (Arts. 11–13); *crédito
fiscal* (input-tax credit) procedence, documentation, registration windows
and carry-forward (Arts. 15–22 + reglamento); the débito computation
÷1.12 × 0.12 and prorrateo (Reglamento Arts. 10/19–22); the refund-channel
matrix (Arts. 23/23-A, 24/24-A/24-B, 25 + reglamento Arts. 23–27); the
document/books/declaration skeleton (Arts. 29, 32–44) as citation spine for
other waves; and the fixed-fee IVA on used vehicles/motorcycles (Arts.
55–57"D").

It does **not** cover: the pequeño contribuyente regime (thresholds, 5%
tarifa, its retention and book rules — Task 2 file, cluster TX2), the
general-regime retention matrix and seller-side netting (D-20-2006 +
AG 425-2006 — Task 3 file, cluster TX3), ISR topics (Tasks 4–5), the
Código Tributario procedure/sanction layer (Task 6), the reform-chain
provenance discipline file (Task 7, cluster TX7), declaration/filing form
generation (F-wave), or FEL document-type/validating mechanics (already in
`gt/requirements/e-invoicing/`, cited here as GT-EINV-FR ids). Those files
cross-reference this one for the IVA core values.

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): the IVA
statutory layer = **Decreto 27-92 consolidated through D-10-2012 ONLY —
never cited alone**; every current-law row below carries the qualifier
"D-27-92 (texto ≤ D-10-2012), reformado por… (≥ D-4-2019 / D-31-2024 /
D-10-2025)"; the post-2018 consolidated text is missing (GOQ-01). The IVA
reglamento = "AG 5-2013, reformado por AG 222-2019". D-20-2006 Chapter V is
cited only for the IVA articles it added/reformed (imprentas-backed credit
documentation, Art. 29 open-documents literal, Fondo IVA 8%). Dated values
(rate, earmarks, thresholds, fees, refund percentages) follow the
dated-instrument regime D15/D16 (cite together): valid_from/valid_to rows +
instrument provenance + as-of qualifier, snapshot-on-write, rate rows are
decree-bound, never constants (GOQ-50 pattern).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley del Impuesto al Valor Agregado, Decreto Número 27-92 (texto consolidado ≤ D-10-2012; reformas posteriores ≥ D-4-2019 / D-31-2024 / D-10-2025 fuera de esta copia): "LEY DEL IMPUESTO AL VALOR AGREGADO / DECRETO NÚMERO 27-92"; pie de reformas más reciente: "ARTÍCULO 181. (Del Decreto Número 10-2012…) …entrará en vigencia ocho (8) días después de la fecha de publicación…" | IVA law D-27-92 as consolidated only through D-10-2012 (given 9-Apr-1992, promulgated 7-May-1992, original vigencia 1-Jul-1992): the statutory base layer; every current-law row must pair it with the later reform instruments (GOQ-01) | `gt/sources/23_Ley_IVA_27-92.pdf` | p.1 title block; transitorios pp. 49–51 (EVID-161) |
| LB-002 | D-27-92 (texto ≤ D-10-2012), Art. 3: "El impuesto es generado por: 1) La venta o permuta de bienes muebles o de derechos reales constituidos sobre ellos. 2) La prestación de servicios en el territorio nacional. 3) Las importaciones. 4) El arrendamiento de bienes muebles e inmuebles. 5) Las adjudicaciones de bienes muebles e inmuebles en pago, salvo… la partición de la masa hereditaria o la finalización del proindiviso. 6) Los retiros de bienes muebles efectuados por un contribuyente o por el propietario, socios, directores o empleados… 7) La destrucción, pérdida o cualquier hecho que implique faltante de inventario, salvo cuando se trate de bienes perecederos, casos fortuitos, de fuerza mayor o delitos contra el patrimonio… 8) La primera venta o permuta de bienes inmuebles. 9) La donación entre vivos de bienes muebles e inmuebles. 10) La aportación de bienes inmuebles a sociedades…" + regla de cierre: "En los casos señalados en los numerales 5, 6 y 9 anteriores, para los efectos del impuesto, la base imponible en ningún caso será inferior al precio de adquisición o al costo de fabricación de los bienes." | Art. 3 taxable-event taxonomy (10 numerales: goods sales/swap, in-country services, imports, leases, in-payment adjudications, inventory withdrawals/self-supply, inventory shortfalls unless perishable/fortuitous/patrimonial crimes, first sale of real estate, inter-vivos donations, real-estate contributions to companies) + minimum-base floor for numerals 5/6/9 at acquisition or manufacturing cost | `gt/sources/23_Ley_IVA_27-92.pdf` | p.3 Art. 3, footnotes p.4 (EVID-162) |
| LB-003 | D-27-92 (texto ≤ D-10-2012), Art. 4: "1) Por la venta o permuta de bienes muebles, en la fecha de la emisión de la factura. Cuando la entrega de los bienes muebles sea anterior a la emisión de la factura, el impuesto debe pagarse en la fecha de la entrega real del bien. / Por la prestación de servicios, en la fecha de la emisión de la factura. Si no se ha emitido factura, el impuesto debe pagarse en la fecha en que el contribuyente perciba la remuneración. … 2) En las importaciones, en la fecha en que se efectúe el pago de los derechos respectivos… Las aduanas no autorizarán el retiro de los bienes del recinto aduanero sin que previamente estén debidamente cancelados los correspondientes impuestos. / 5) En los arrendamientos y en la prestación de servicios periódicos, al término de cada período fijado para el pago de la renta o remuneración efectivamente percibida. / 7) En los de seguros y fianzas, en el momento en que las primas o cuotas sean efectivamente percibidas." | Art. 4 tax point: invoice-emission date, with actual-delivery fallback (goods) and remuneration-perception fallback (services); imports at payment of duties (customs blocks release); periodic leases/services at each period actually perceived; insurance at cash perception | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 4–5 Art. 4 (EVID-163) |
| LB-004 | D-27-92 (texto ≤ D-10-2012), Art. 7 (15 numerales), p.ej. "2. Las exportaciones de bienes y las exportaciones de servicios, conforme la definición del Artículo 2 numeral 4 de esta ley." / "11. La venta al menudeo de carnes, pescado, mariscos, frutas y verduras frescas, cereales, legumbres y granos básicos a consumidores finales en mercados cantonales y municipales, siempre que tales ventas no excedan de cien quetzales (Q.100.00) por cada transacción." / "12. La venta de vivienda con un máximo de ochenta (80) metros cuadrados de construcción cuyo valor no exceda de doscientos cincuenta mil Quetzales (Q.250,000.00) y la de lotes urbanizados que incluyan los servicios básicos, con un área máxima de ciento veinte (120) metros cuadrados, cuyo valor no exceda de ciento veinte mil Quetzales (Q.120,000.00)…" / "15. La compra y venta de medicamentos denominados genéricos y alternativos de origen natural, inscritos como tales en el Registro Sanitario… así mismo… la compra y venta de medicamentos antirretrovirales…" | Art. 7 objective exemptions (15 numerales: import frictions, exports, merger/inheritance transfers, banking services, cooperatives, títulos de crédito except factura cambiaria, bursátil interest, fideicomisos, non-profit contributions, association dues, market retail ≤ Q100/transaction, social housing Q250,000/80 m² + urbanized lots Q120,000/120 m², non-profit educational/assistancial/religious services, bank-regulation assets, generic + antiretroviral medicines). Peaje/turismo/canasta families grep-ABSENT from this copy (GOQ-01) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 5–8 Art. 7, footnote block p.8 (EVID-164) |
| LB-005 | D-27-92 (texto ≤ D-10-2012), Arts. 8 y 9: Art. 8: "No deben cargar el impuesto en sus operaciones de ventas, como tampoco en la prestación de servicios, las siguientes personas: 1. Los centros educativos públicos y privados… 2. Las universidades autorizadas para funcionar en el país. 3. La Confederación Deportiva Autónoma de Guatemala y el Comité Olímpico Guatemalteco. 4. El Instituto Guatemalteco de Seguridad Social. 5. Las misiones diplomáticas y consulares… 6. Los organismos internacionales…" / Art. 9: "…están exentas de soportar el impuesto… deberán recibir de quien les venda o les preste un servicio, la factura que corresponda, pero no pagarán el monto del impuesto consignado en el documento, sino que entregarán a los mismos la constancia de exención debidamente autorizada por la Administración Tributaria." | Arts. 8/9 subjective exemptions: six exempt-person classes must still be invoiced but charged no IVA; the buyer hands the seller an SAT-authorized constancia de exención in place of the tax (reglamento Art. 13: exempt entities pay pequeño suppliers the full invoice — no constancia relief; Art. 15: sellers report these sales as gravadas and credit constancias separately) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 8–9 Arts. 8 y 9 (EVID-165) |
| LB-006 | D-27-92 (texto ≤ D-10-2012), Art. 10: "Tarifa única. Los contribuyentes afectos a las disposiciones de esta ley pagarán el impuesto con una tarifa del doce por ciento (12%) sobre la base imponible. La tarifa del impuesto en todos los casos deberá estar incluida en el precio de venta de los bienes o el valor de los servicios." / "…tres y medio puntos porcentuales (3.5%) se asignará íntegramente para el financiamiento de la paz y desarrollo…" (distribución: "1. Uno y medio puntos porcentuales (1.5%) para las municipalidades… 2. Un punto porcentual (1%)… Consejos Departamentales de Desarrollo… 3. Un punto porcentual (1%) para los Fondos para la Paz…") / "…uno y medio puntos porcentuales (1.5%) se destinará específicamente al financiamiento de gastos sociales…" (0.5% seguridad alimentaria + 0.5% educación primaria y técnica + 0.5% seguridad ciudadana) / "ARTICULO 10. bis* Derogado." (adicionado D-32-2003; declarado inconstitucional, CC expedientes acumulados 1060-2003 y 1064-2003) | Art. 10 single 12% rate, mandatorily price-inclusive; 5 of the 12 points earmarked (3.5 paz/desarrollo split 1.5/1/1 + 1.5 gasto social split 0.5/0.5/0.5) into the "Fondo para el Desarrollo, el Gasto Social y la Paz"; Art. 10 bis (differentiated petroleum rate) prints only "Derogado" with CC history. Earmark text = D-66-2002-era (GOQ-64) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 10–11 Arts. 10 y 10 bis (EVID-166) |
| LB-007 | D-27-92 (texto ≤ D-10-2012), Arts. 11–13: Art. 11: "La base imponible de las ventas será el precio de la operación menos los descuentos concedidos de acuerdo con prácticas comerciales. Debe adicionarse a dicho precio, aun cuando se facturen o contabilicen en forma separada… 1. Los reajustes y recargos financieros. 2. El valor de los envases, embalajes y de los depósitos constituidos por los compradores para garantizar su devolución… 3. Cualquier otra suma cargada… que figure en las facturas." / Art. 12 (servicios): same + "2) El valor de los bienes que se utilicen para la prestación del servicio. 3) Cualquier otra suma… salvo contribuciones o aportaciones establecidas por leyes específicas." / Art. 13: "1) En las importaciones: El valor que resulte de adicionar al precio CIF de las mercancías importadas el monto de los derechos arancelarios y demás recargos… 2) En el arrendamiento…: El valor de la renta, al cual deberá adicionarse el valor de recargos financieros… 4) En los retiros de bienes…: El precio de adquisición o el costo de fabricación…" | Arts. 11–13 taxable base: operation price minus commercial discounts, plus finance charges, packaging/deposits and any invoiced sum (services: statutory contributions excluded); imports = CIF + tariffs + other import charges; withdrawals at acquisition/manufacturing cost | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 11–12 Arts. 11–13 (EVID-167) |
| LB-008 | D-27-92 (texto ≤ D-10-2012), Arts. 15–16: Art. 15: "El crédito fiscal es la suma del impuesto cargado al contribuyente por las operaciones afectas realizadas durante el mismo período." / Art. 16: "Procede el derecho al crédito fiscal para su compensación, por la importación y adquisición de bienes y la utilización de servicios que se vinculen con la actividad económica…"; criterios: "a) Que los bienes o servicios formen parte de los productos o de las actividades necesarias para su comercialización nacional o internacional. b) Que los bienes o servicios se incorporen al servicio o a las actividades necesarias para su prestación dentro o fuera del país." / "El impuesto pagado por la adquisición, importación o construcción de activos fijos, se reconocerá como crédito fiscal cuando los mismos estén directamente vinculados al proceso de producción o de comercialización… no integrará el costo de adquisición… para los efectos de la depreciación anual en el régimen del Impuesto Sobre la Renta." / "Los contribuyentes que se dediquen a la exportación y los que vendan o presten servicios a personas exentas en el mercado interno, tendrán derecho a la devolución del crédito fiscal…" | Arts. 15–16 credit procedence: input IVA on imports/goods/services linked to the economic activity (criteria a/b); fixed-asset credit only when directly linked to production/commercialization and excluded from the ISR depreciation base; exporters and sellers-to-exempt-persons have refund rights (developed in Arts. 23–25) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 13–14 Arts. 15–16, footnotes p.14 (EVID-168) |
| LB-009 | D-27-92 (texto ≤ D-10-2012), Arts. 17–22: Art. 17: notas "deberán registrarse en la contabilidad del vendedor… dentro del plazo de dos meses, contados a partir de la fecha en que fue emitida la factura que será modificada…" / Art. 18: crédito respaldado por "facturas, facturas especiales, notas de débito o crédito impresas por las imprentas… recibos de pago cuando se trate de importaciones o en las escrituras públicas… facturas electrónicas, notas de débito y crédito electrónicas, siempre y cuando las mismas hubieren sido emitidas a través de un Generador de Facturas Electrónicas (GFACE)…" + b) "Que dichos documentos se emitan a nombre del contribuyente y que contengan su Número de Identificación Tributaria" / Art. 20: "Las fechas de las facturas y de los recibos de pago de derechos de importación… deben corresponder al mes del período que se liquida. Si por cualquier circunstancia no se reportan en el mes al que corresponden… se pueden reportar como máximo en los dos meses inmediatos siguientes… De no efectuarlo en dicho plazo, no tendrá derecho a su compensación o devolución, según proceda." / Art. 21: remanente "se acumulará a los créditos… del período impositivo siguiente." / Art. 22: "El saldo del crédito fiscal… lo puede trasladar a sucesivos períodos impositivos siguientes, hasta agotarlo… por lo que no procederá la devolución del crédito fiscal. Se exceptúan los casos a que se refiere el artículo 23…" | Arts. 17–22 credit mechanics: debit/credit notes registered within 2 months of the modified invoice; documentation backed by imprentas prints, import receipts, escrituras, or GFACE-era electronic documents (pre-FEL vintage — FEL cross-ref) issued to the taxpayer's NIT; invoices reportable only in their own month + 2 following months, else forfeited; excess credit carries forward indefinitely — refund forbidden except Arts. 23–25 channels | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 14–16 Arts. 17–22 (EVID-169) |
| LB-010 | D-27-92 (texto ≤ D-10-2012), Arts. 23 y 23 "A": "Los contribuyentes que se dediquen a la exportación, presten servicios o vendan bienes a personas exentas del impuesto, tendrán derecho a la devolución del crédito fiscal… La devolución se efectuará por períodos impositivos vencidos acumulados, en forma trimestral o semestral…" / Art. 23 "A": SAT "deberá resolver dentro del plazo máximo de treinta (30) días hábiles para el período trimestral y de sesenta (60) días hábiles para el período semestral… Si la Administración Tributaria formula ajustes… por el saldo no ajustado, emitirá la autorización para que el Banco de Guatemala haga efectiva la devolución, con cargo a la cuenta Fondo IVA… La petición se tendrá por resuelta desfavorablemente… si transcurrido el plazo… no emite y notifica la resolución respectiva." | Arts. 23/23-A general refund channel: exporters and sellers-to-exempt-persons; quarterly/semiannual accumulation; SAT resolves in 30/60 días hábiles; Banco de Guatemala pays from the Fondo IVA; presumed-denial (negative silence) escalation | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 16–20 Arts. 23 y 23 "A" (EVID-170) |
| LB-011 | D-27-92 (texto ≤ D-10-2012), Arts. 24, 24 "A", 24 "B": solicitud "dentro de los primeros diez (10) días hábiles siguientes al vencimiento para la presentación de la declaración mensual…" + "5) Dictamen sobre la procedencia del crédito fiscal solicitado, emitido por contador público y auditor independiente…" + "la Administración Tributaria resolverá dentro del plazo de diez (10) días hábiles… y enviará aviso al Banco de Guatemala para que proceda a efectuar la devolución del cien por ciento (100%) del monto del crédito fiscal que no haya sido retenido." / Art. 24 "A": cambio de régimen "siempre que lo efectúe con anticipación al inicio del siguiente período impositivo." / Art. 24 "B": Registro de Contadores y Auditores Públicos; colegiado activo; no dependency/kinship | Arts. 24/24-A/24-B optional regime: CPA-audited dictamen, 100% of unretained credit refunded, 10 días hábiles SLA, monthly cadence via the filing window; prospective-only regime switching; CPA registration/independence rules | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 20–24 Arts. 24–24 "B" (EVID-171) |
| LB-012 | D-27-92 (texto ≤ D-10-2012), Art. 25: "…podrán solicitar al Banco de Guatemala la devolución del crédito fiscal en efectivo, por período mensual calendario vencido y por un monto equivalente al setenta y cinco por ciento (75%) cuando la devolución sea hasta por la cantidad de quinientos mil quetzales (Q.500,000.00) y del sesenta por ciento (60%) cuando la devolución sea mayor de quinientos mil quetzales (Q.500,000.00), del crédito fiscal declarado…" / "El Banco de Guatemala… queda expresamente facultado para abrir una cuenta específica denominada 'Fondo IVA, para devoluciones del crédito fiscal a los exportadores', que acreditará… por un mínimo del ocho por ciento (8%) de los ingresos depositados diariamente en concepto de Impuesto al Valor Agregado -IVA-." / calificación A/B (≥50% exportaciones / menor al 50% sin poder compensar) / "descontará de cada devolución, un cuarto del uno por ciento (1/4 del 1%) del monto de crédito fiscal devuelto." / clawback: "el valor del impuesto por los ajustes será deducido temporalmente de las siguientes devoluciones solicitadas." | Art. 25 BNG special channel: monthly, self-filed at Banco de Guatemala; 75% of declared credit when the refund is ≤ Q500,000.00 and 60% above; funded from an 8% daily IVA separation into "Fondo IVA"; ¼ of 1% BNG fee; temporary deduction of adjustments from subsequent refunds | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 24–27 Art. 25 (EVID-172) |
| LB-013 | D-27-92 (texto ≤ D-10-2012; Art. 29 reformado totalmente por Art. 9 del D-4-2012 y Art. 155 del D-10-2012), Art. 29: "Documentos obligatorios. Los contribuyentes afectos al impuesto de esta Ley están obligados a emitir con caracteres legibles y permanentes o por medio electrónico… a) Facturas… incluso respecto de las operaciones exentas o con personas exentas… b) Facturas de Pequeño Contribuyente… c) Notas de débito… d) Notas de crédito… e) Otros documentos que, en casos concretos y debidamente justificados, autorice la Administración Tributaria…" + último párrafo: facultad genérica de autorizar "facturas emitidas en cintas, por máquinas registradoras, en forma electrónica u otros medios…" (SIN Art. 29-"A" en esta copia) / Arts. 30–31: especificaciones y autorización previa delegadas al reglamento | Art. 29 mandatory documents as printed (facturas incl. exempt operations, pequeño invoices, debit/credit notes, SAT-authorized otros) + the generic electronic-emission faculty fully delegated to the reglamento; NO Art. 29-"A" exists in this copy (the FEL article, added by D-4-2019 art. 6, is GOQ-01 territory; Art. 8-"A"/25 bis likewise absent) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 28–29 Arts. 26–31, footnotes p.29 (EVID-173) |
| LB-014 | D-27-92 (texto ≤ D-10-2012), Arts. 32–44: Art. 32: "En las facturas, notas de débito, notas de crédito y facturas especiales, el impuesto siempre debe estar incluido en el precio, excepto en los casos de exenciones objetivas…" / Art. 34: "En la venta de bienes muebles, las facturas… deberán ser emitidas y proporcionadas al adquirente o comprador, en el momento de la entrega real de los bienes. En el caso de las prestaciones de servicios, deberán ser emitidas en el mismo momento en que se reciba la remuneración." / Art. 37: "…los contribuyentes deberán llevar y mantener al día un libro de compras y servicios recibidos y otro de ventas y servicios prestados… podrán ser llevados en forma manual o computarizada." / Art. 40: "…dentro del mes calendario siguiente al vencimiento de cada período impositivo, una declaración del monto total de las operaciones realizadas en el mes calendario anterior, incluso las exentas…" + justificación documentada cuando ventas gravadas/exentas < compras durante tres períodos consecutivos / Art. 43 (declaración pese a inactividad salvo comunicación de suspensión); Art. 44 (sucursales: declaración y pago conjuntos "en un sólo formulario") | Arts. 32–44: price-inclusive IVA on every document (except objective exemptions); invoice emission at real delivery (goods) / remuneration receipt (services); two mandatory books (purchases + sales, manual or computerized); monthly declaration within the following calendar month incl. exempt operations; 3-period excess-purchases justification; consolidated single filing across establishments | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 29–32 Arts. 32–44 (EVID-174) |
| LB-015 | D-27-92 (texto ≤ D-10-2012), Arts. 55–57 "D": vehículos usados: "Modelo Tarifa fija / De dos a tres años anteriores al año en curso Un mil Quetzales (Q.1,000.00) / De cuatro o más años anteriores al año en curso Quinientos Quetzales (Q.500.00)"; motocicletas: "De dos a tres años… Trescientos Quetzales (Q.300.00) / De cuatro o más años… Doscientos Quetzales (Q.200.00)"; vehículos totalizados: "debiendo aplicarse la tarifa máxima específica fija establecida en los párrafos precedentes" / Art. 56 (inmuebles): base = "el precio de venta consignado en la factura, escritura pública o el que consta en la matricula fiscal, el que sea mayor" / Art. 57: pago "siempre en efectivo por el adquiriente… dentro del plazo de quince días hábiles contados a partir de la fecha en que se legalice el endoso… en el Certificado de Propiedad de Vehículos" / Art. 57 "D": contribuyentes especiales "deberán presentar en forma electrónica, cada seis meses, como máximo, informe detallado de las compras y ventas efectuadas… a) NIT…; b) El nombre…; c) El monto…; d) Fecha…" | Arts. 55–57"D": fixed-fee IVA on used-vehicle transfers (cars Q1,000 aged 2–3 model years / Q500 at 4+; motorcycles Q300 / Q200; totaled vehicles pay the maximum fixed fee — never the 12% ad-valorem); real-estate base = higher of invoice/escritura/matricula; cash payment by the acquirer within 15 días hábiles of the endoso legalization; especiales file a semi-annual electronic purchase/sales report (NIT/name/amount/date) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 37–42 Arts. 55–57 "D" (EVID-178) |
| LB-016 | Reglamento de la Ley del IVA, AG 5-2013, reformado por AG 222-2019 (Guatemala, 4 de enero de 2013; publicado 8-ene-2013; rige 9-ene-2013; Art. 63 deroga AG 424-2006): "ACUERDO GUBERNATIVO No. 5-2013…"; única cola de reformas = AG 222-2019 (Arts. 2 j, 25 bis, 26 bis–quinquies, 28 bis, 36 bis/ter, 29 ¶4, 36) + nota CC 12-ene-2015 sobre el Art. 12 | IVA reglamento identity: AG 5-2013 effective 9-Jan-2013, reformed only by AG 222-2019 (FEL cluster); replaces AG 424-2006 — the reglamento layer every operational row below cites | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.1 header; reform footnotes at Arts. 2, 25 bis–36 ter; pp. 25–26 signature block (EVID-180) |
| LB-017 | Reglamento (AG 5-2013, reformado por AG 222-2019), Arts. 19–20: Art. 19: "1) El total de las ventas o servicios gravados se divide entre uno punto doce (1.12) para determinar la base imponible. Dicha base se multiplica por cero punto doce (0.12), obteniendo así el impuesto. 2) El débito fiscal del período, se aumentará con el impuesto incluido en el precio… en las notas de débito… emitidas dentro del mismo período impositivo." / Art. 20: deducciones por devoluciones de bienes, "valores de facturas anuladas correspondientes a operaciones ya declaradas", bonificaciones/descuentos posteriores a la facturación y depósitos devueltos — "es requisito indispensable que el contribuyente emita las notas de crédito… y que las registre… dentro del plazo establecido en el párrafo tercero del artículo 17 de la Ley." | Reglamento Arts. 19–20 débito arithmetic: gross taxable sales ÷ 1.12 = base, × 0.12 = tax; debit notes add to the period; credit notes subtract (returns, annulled invoices, post-sale discounts, deposit refunds) subject to the 2-month registration rule | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.6 Arts. 19 y 20 (EVID-182) |
| LB-018 | Reglamento (AG 5-2013, reformado por AG 222-2019), Arts. 10/21/22/38–39: Art. 10: "Cuando no puedan determinar a través de sus registros contables la parte de los gastos que corresponde a cada fuente de ingresos, el impuesto que paguen a sus proveedores deberán distribuirlo proporcionalmente entre el total de ventas y prestación de servicios gravados y exentos." / Art. 22 (no generan crédito, "entre otros"): "1) La compra de bienes o adquisición de servicios destinados al uso o consumo particular… 2) Los retiros de bienes del inventario… 3) La adquisición de bienes de capital o activos fijos no destinados a dichas actividades. 4) La compra de combustibles, lubricantes, seguros, para vehículos… a los que se refiere el numeral anterior. 5) Las adquisiciones realizadas a los contribuyentes inscritos en el régimen de pequeño contribuyente…" + cierre: "…deberán distribuirlo proporcionalmente… En la declaración mensual deberán consignar, como crédito fiscal, únicamente, la proporción que corresponda a las ventas o prestación de servicios gravados." / Art. 38: libro de compras separando "ventas locales, de exportación y a personas exentas"; facturas de pequeño "se registrarán… sin consignar ningún valor en la columna correspondiente al impuesto" / Art. 21: lista ilustrativa "entre otros casos" de gastos generadores para exportadores | Reglamento prorrateo + no-credit list + book columns: proportional distribution of input IVA over gravadas+exentas with only the gravadas share claimed (no printed formula); open non-exhaustive no-credit list (personal use, self-withdrawals, unlinked assets + their fuel/lubricants/insurance, pequeño-supplier purchases); purchases book three-way separation local/export/exempt, pequeño rows without IVA column; exporter credit-generating expense list (internet/telecom, security, storage/transport, GPS, refund processing, fuels, fumigation, insurance, working-capital interest, AC/alarms, cargo leases, uniforms) | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.4 Art. 10; p.7 Art. 21; pp. 7–8 Art. 22; pp. 19–20 Arts. 38–39 (EVID-183) |
| LB-019 | Reglamento (AG 5-2013, reformado por AG 222-2019), Arts. 23–27: Art. 25 bis (régimen especial electrónico, "De conformidad con el artículo 25 bis de la Ley"): devolución "del cien por ciento (100%) del crédito fiscal… deberá… presentar… de forma electrónica…" + "la Administración Tributaria tendrá un plazo de treinta (30) días hábiles para resolver el fondo… dispondrá de diez (10) hábiles para admitir o rechazar la solicitud." / Art. 26 bis: miembros "deberán estar incorporados en el Régimen de Factura Electrónica en Línea -FEL-"; incorporación cualquier mes, actualización anual en enero / Art. 27: "…se abstendrán de tramitar las solicitudes de devolución de crédito fiscal por montos menores a diez mil quetzales (Q10,000.00), por lo que los contribuyentes deberán acumular los créditos fiscales… salvo… conforme el artículo 23 de la Ley." / Art. 24: documentación de exportadores (declaración de exportación definitiva perfeccionada, conocimiento de embarque, manifiesto, lista de embarque, "Informe de trazabilidad (tracking)… arribo en el puerto de destino final", prueba de pago) | Reglamento refund machinery: Q10,000 minimum with accumulation duty (justified exception via Ley Art. 23); FEL-gated electronic 100% regime citing "artículo 25 bis de la Ley" — an article ABSENT from the 23_ copy (adder decree unidentified, GOQ-01); export evidence pack incl. tracking-to-final-port and payment proof | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | pp. 8–12 Arts. 23–27 bis (EVID-184) |
| LB-020 | Decreto 10-2025 (emitido 21-oct-2025; DCA 4-nov-2025 No. 40; vigencia = día de publicación): "Artículo 1. Se deroga e! [sic] artículo 8 "A" de la Ley del Impuesto al Valor Agregado, Decreto Número 27-92, adicionado por el artículo 13 de ia [sic] Ley para la Integración… del Sector Productivo Primario y Agropecuario, Decreto Número 31-2024…" / "Artículo 4. Vigencia… entrará en vigencia el día de su publicación en el Diario Oficial." | D-10-2025 Art. 1 derogates IVA Art. 8-"A" (the MINEDUC alimentación-escolar retention scheme article added by D-31-2024 art. 13), effective 4-Nov-2025; no "3-'A'" text exists anywhere in the decree (OCR 8/3 residue → GOQ-13); nothing else in D-10-2025 touches D-27-92 | `gt/sources/74_Ley_IVA_EScolar_Reformas_D10-2025.pdf` | p.2 Art. 1; p.1–2 considerandos II/III/V (EVID-188; identity EVID-187) |
| LB-021 | Decreto 20-2006, Capítulo V (arts. 37–53, reformas a la Ley del IVA): art. 41 (IVA 18 a): "Que se encuentre respaldado por las facturas, facturas especiales, notas de crédito impresas por las imprentas o los contribuyentes que auto-impriman [sic] los documentos y que se encuentren inscritas en el Registro Fiscal de Imprentas…" / art. 50 (IVA 29): "Otros documentos que, en casos concretos y debidamente justificados, autorice la Administración Tributaria…" / Fondo IVA (art. 49 → IVA 25): "por un mínimo del ocho por ciento (8%) de los ingresos depositados diariamente en concepto de Impuesto al Valor Agregado -IVA-." | D-20-2006 Chapter V lineage: imprentas-registry-backed printed credit documentation (pre-FEL era foundation); the Art. 29 "otros documentos" open clause (later literal e) — the authorization route for electronic documents; the 8% Fondo IVA funding rule; vehicle fixed fees originally Q500/300/100 (cars) + Q200/100/50 (motorcycles) at 2006 vintage | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | pp. 24–25 art. 41; pp. 33–34 art. 50; rest of Chapter V pp. 21–35 (EVID-257, file EV02d) |

## 3. Functional Requirements

### 3.1 Hecho generador & tax point

- **GT-TAX-FR-001:** The system shall classify every taxable operation
  against the Art. 3 *hecho generador* taxonomy (10 numerales: sale/swap of
  movable goods or real rights over them; in-country services; imports;
  leases of movable and immovable property; in-payment adjudications
  excluding inheritance partition/proindiviso termination; inventory
  withdrawals by the taxpayer/owner/partners/directors/employees;
  destruction/loss/inventory shortfall unless perishable goods, fortuitous
  events, force majeure or patrimonial crimes; first sale of real estate;
  inter-vivos donations; real-estate contributions to companies), and no
  operation outside the taxonomy shall trigger IVA. (LB-002; EVID-162)
- **GT-TAX-FR-002:** For adjudications in payment (numeral 5), inventory
  withdrawals (numeral 6) and inter-vivos donations (numeral 9), the taxable
  base shall never be lower than the acquisition price or manufacturing cost
  of the goods (minimum-base floor). (LB-002; EVID-162)
- **GT-TAX-FR-003:** The IVA tax point (*momento de pago*) shall be the
  invoice-emission date, with fallbacks: goods delivered before emission →
  the actual-delivery date; services without invoice → the date the
  remuneration is perceived; vehicles → when the acquirer's invoice is
  issued; escritura-pública-only sales → the tax-payment testimonio within
  15 days. (LB-003; EVID-163)
- **GT-TAX-FR-004:** Leases and periodic services shall accrue IVA at the
  end of each period *effectively perceived* (rent/remuneration actually
  received), and insurance/fianzas at the moment premiums are actually
  perceived — periodic billing shall not accelerate the tax point beyond
  perception. (LB-003; EVID-163)
- **GT-TAX-FR-005:** Import tax point = the date import duties are paid;
  the customs release block ("Las aduanas no autorizarán el retiro de los
  bienes…") shall be recorded as the legal release precondition for import
  flows. (LB-003; EVID-163)

### 3.2 Tarifa única & rate exceptions

- **GT-TAX-FR-006:** The default IVA rate shall be the *tarifa única* 12%
  on the taxable base, mandatorily **price-inclusive** ("deberá estar
  incluida en el precio de venta"), stored as a dated row (valid_from with
  instrument provenance "D-27-92 Art. 10, texto ≤ D-10-2012, reformado
  por… ≥ D-4-2019/D-31-2024/D-10-2025" + as-of qualifier, GOQ-01; rate
  rows are decree-bound, never constants — GOQ-50 pattern; D15/D16
  snapshot-on-write). (LB-006; EVID-166)
- **GT-TAX-FR-007:** The earmark split of the 12 points shall be stored as
  dated rows: 3.5 pp *paz y desarrollo* (peace and development) split
  1.5 pp municipalidades + 1 pp Consejos Departamentales de Desarrollo +
  1 pp Fondos para la Paz; 1.5 pp *gasto social* (social spending) split
  0.5 pp seguridad alimentaria + 0.5 pp educación primaria y técnica +
  0.5 pp seguridad ciudadana; account "Fondo para el Desarrollo, el Gasto
  Social y la Paz". The earmark architecture is D-66-2002-era text and
  post-2012 reform state is unverifiable from the corpus → earmark rows are
  informational accounting-distribution metadata, never computation inputs,
  pending GOQ-64. (LB-006; EVID-166; GOQ-64 → OQ-001)
- **GT-TAX-FR-008:** Art. 10 *bis* (differentiated petroleum rate) shall be
  recorded exactly as printed — "Derogado", with its CC history (added by
  D-32-2003; declared unconstitutional, CC expedientes acumulados
  1060-2003 y 1064-2003) — and NO differentiated petroleum IVA rate shall
  be implemented from this layer (the IDP petroleum-distribution tax is a
  separate excise owned by the e-invoicing catalog files, S-GT1).
  (LB-006; EVID-166)
- **GT-TAX-FR-009:** The rate-exception registry shall contain exactly the
  statutory exceptions evidenced in this layer: the pequeño contribuyente
  5% *tarifa* (owned by Task 2, cluster TX2 — cross-referenced, not
  re-derived) and the used-vehicle/motorcycle fixed Q fees (FR-043);
  objective exemptions of Art. 7 are exemptions, not 0% rates; the system
  shall NOT invent any other ad-valorem rate or 0% "essentials" rate —
  peaje/turismo/canasta families are absent from the statutory copy
  (GOQ-01). (LB-004; LB-006; LB-015; EVID-164, EVID-166, EVID-178)

### 3.3 Exenciones (objective Art. 7; subjective Arts. 8/9)

- **GT-TAX-FR-010:** The system shall carry the 15 Art. 7 objective
  exemption families as a seeded, dated exemption catalog (imports
  frictions a–f; exports of goods and services; fusion/inheritance/aportes
  transfers with the real-estate-development carve-out; banking/exchange
  services and bursátil interest; cooperative member operations; títulos de
  crédito except *factura cambiaria*; fideicomisos; contributions to
  non-profits; association dues; market retail; social housing/lots;
  non-profit educational/healthcare/religious services; bank-regulation
  assets; generic and antiretroviral medicines). (LB-004; EVID-164)
- **GT-TAX-FR-011:** Exemption parameter values shall be stored as dated
  rows with instrument provenance "D-27-92 Art. 7 (texto ≤ D-10-2012)":
  market retail (cantonales/municipales, fresh meats/fish/seafood/fruit/
  vegetables/cereals/legumes/grains to final consumers) only ≤
  Q100.00 per transaction; social housing ≤ 80 m² construction and ≤
  Q250,000.00 (buyer must evidence lack of own housing for self and family
  nucleus); urbanized lots ≤ 120 m² and ≤ Q120,000.00. Currency of these
  2012-era figures carries the GOQ-01 qualifier. (LB-004; EVID-164; GOQ-01
  → OQ-002)
- **GT-TAX-FR-012:** The post-2012 exemption families (peajes
  internacionales, turismo, canasta básica) shall NOT be modeled from the
  statutory copy in the corpus: they are grep-absent from it and their
  adding instruments are unacquired — a guard row records them as pending
  GOQ-01 facts, never as implemented exemptions. (LB-004; EVID-164; GOQ-01
  → OQ-002)
- **GT-TAX-FR-013:** The subjective exemption classes of Art. 8 (public/
  private educational centers on tuition and exam fees; authorized
  universities; CDAG/COG; IGSS; diplomatic/consular missions on
  reciprocity; international organisms) shall be seeded as exempt-person
  classes; the dated fact that Art. 8-"A" (MINEDUC alimentación-escolar
  retention scheme, added by D-31-2024 art. 13) was derogated by D-10-2025
  art. 1 effective 4-Nov-2025 shall be recorded so that no 8-"A"
  retention behavior is ever implemented — and no "Art. 3-'A'" ever
  existed (rejected myth; OCR residue → GOQ-13). (LB-005; LB-020; EVID-165,
  EVID-188; GOQ-13 → OQ-004)
- **GT-TAX-FR-014:** The exempt-customer invoice flow shall be: supplier
  issues the normal invoice (factura) for the operation (exempt operations
  and exempt persons are still invoiced), charges zero IVA, and receives
  from the buyer the SAT-authorized *constancia de exención* in place of
  the tax; the seller reports the sale as a *gravada* (taxable) sale and
  credits the constancia separately (reglamento Arts. 13/15). The FEL
  *Constancia de Exención de IVA* (CIVA) DTE mechanics are owned by
  GT-EINV-FR-030 — cross-referenced, not re-derived. (LB-005; EVID-165)
- **GT-TAX-FR-015:** Exempt entities buying from pequeño contribuyente
  suppliers shall pay the FULL invoice amount — no constancia relief
  applies against pequeño invoices (reglamento Art. 13; pequeño-side
  mechanics owned by Task 2). (LB-005; EVID-165)

### 3.4 Base imponible

- **GT-TAX-FR-016:** The sales base shall be the operation price minus
  commercial discounts, plus (even if invoiced/booked separately) finance
  adjustments and surcharges, packaging/embalaje value and returnable
  deposits, and any other sum charged on the invoice. (LB-007; EVID-167)
- **GT-TAX-FR-017:** The services base shall additionally include the
  value of goods used to render the service, and shall exclude
  contributions/aportaciones established by specific laws (statutory
  levies); reglamento Arts. 16–18 detail (credit-sale price/recargos split,
  tips inclusion, third-party-collection exclusion) applies at line
  computation. (LB-007; EVID-167)
- **GT-TAX-FR-018:** The import base shall be CIF value plus tariff duties
  and all other import charges; lease base = rent plus finance surcharges;
  withdrawal/donation/adjudication base = acquisition or manufacturing cost
  (floor per FR-002). (LB-007; EVID-167)

### 3.5 Crédito fiscal

- **GT-TAX-FR-019:** Input-tax credit eligibility shall apply the Art. 16
  *vinculación* (linkage) test to the *actividad económica* (economic
  activity: producing, transforming, marketing, transporting or
  distributing goods for sale, or rendering services) under criteria a)
  the goods/services form part of the products or activities necessary for
  national or international commercialization, or b) they incorporate into
  the service or activities necessary for its rendition in or out of the
  country. (LB-008; EVID-168)
- **GT-TAX-FR-020:** Fixed-asset IVA (acquisition, import or construction)
  shall be creditable only when the asset is directly linked to the
  production or commercialization process, and the credited IVA shall be
  excluded from the acquisition cost for ISR annual depreciation purposes
  (ISR-side effects owned by the ISR files, Tasks 4–5). (LB-008; EVID-168)
- **GT-TAX-FR-021:** No credit shall be recognized unless the supporting
  document is issued in the taxpayer's name and carries its NIT (*Número de
  Identificación Tributaria*, tax identification number). (LB-009; EVID-169)
- **GT-TAX-FR-022:** Credit documentation shall be the statutory set:
  facturas, facturas especiales, debit/credit notes, import-duty payment
  receipts, escrituras públicas, and electronic invoices/notes. The
  statutory phrasing ties electronic documents to a SAT-authorized
  *Generador de Facturas Electrónicas (GFACE)* — pre-FEL vintage: current
  electronic credit documentation is FEL DTEs per the e-invoicing wave
  (GT-EINV files; the live statutory hook Art. 29-"A" is absent from the
  corpus copy — GOQ-01); the imprentas-registry lineage (D-20-2006 art. 41)
  is history, never a requirement. (LB-009; LB-021; EVID-169, EVID-257;
  GOQ-01 → OQ-002)
- **GT-TAX-FR-023:** Credit invoices and import-duty receipts shall be
  reportable only in the month they belong to plus the two following
  months; on expiry of that window the right to compensate or refund is
  forfeited ("no tendrá derecho a su compensación o devolución"). The
  registration window shall be enforced at document-registration time with
  a dated eligibility flag. (LB-009; EVID-169)
- **GT-TAX-FR-024:** Debit and credit notes modifying an invoice shall be
  registered in the seller's accounting within two months counted from the
  emission of the modified invoice (Art. 17 ¶3, the deadline the reglamento
  Art. 20 deductions requisites key on). (LB-009; LB-017; EVID-169,
  EVID-182)
- **GT-TAX-FR-025:** Excess credit (*saldo del crédito fiscal*) shall
  carry forward indefinitely to successive periods until exhausted through
  débito compensation — refund is forbidden except through the Arts.
  23/23-A, 24 and 25 channels (FR-031..036); retention-specific netting
  (seller subtracts retained IVA from period liability) and the 2-year
  stranded-remanente track are owned by the retenciones file (Task 3,
  cluster TX3 — cross-referenced). (LB-009; EVID-169)
- **GT-TAX-FR-026:** The no-credit list shall be implemented as an open
  ("entre otros" — among others) rule set: goods/services for the personal
  use or consumption of the taxpayer, partners, directors, administrators
  or employees; inventory withdrawals; capital goods/fixed assets not
  linked to the activities; fuels, lubricants and insurance for such
  unlinked vehicles; and purchases from pequeño contribuyente suppliers
  (which additionally register without IVA column, FR-041). The list is
  non-exhaustive — exclusions beyond it require evidence-based
  configuration, not code. (LB-018; EVID-183)
- **GT-TAX-FR-027:** *Prorrateo* (proration) shall implement the printed
  rule only — proportional distribution of input IVA over total gravadas +
  exentas sales/services with only the gravadas proportion claimed as
  crédito fiscal in the monthly declaration (reglamento Arts. 10 and 22
  final ¶). NO numerator/denominator formula is printed in the sources; the
  implemented formula IVA × gravadas ÷ (gravadas + exentas) shall be tagged
  as the operationalization of the verbal rule, applicable when the
  accounting records cannot separate the expense per income source.
  (LB-018; EVID-183)
- **GT-TAX-FR-028:** For exporters and sellers-to-exempt-persons, the
  reglamento Art. 21 illustrative credit-generating expense list (internet/
  telecom in production areas, production security, storage/transport, GPS,
  refund-processing costs, transport fuels/materials, fumigation, warehouse/
  plant improvements, equipment maintenance, vehicle/machinery/installation/
  merchandise insurance, working-capital loan interest, AC/alarms in
  production/storage areas, cargo-vehicle leases, process uniforms) shall be
  seeded as open ("entre otros casos") eligibility guidance. (LB-018;
  EVID-183)

### 3.6 Débito computation

- **GT-TAX-FR-029:** For price-inclusive (gross) invoicing, the débito
  shall be computed by the statutory arithmetic: total gravadas sales/
  services ÷ 1.12 = taxable base; base × 0.12 = tax. This extraction
  formula applies to every gross amount subject to the 12% tarifa (per-FEL
  validation kin: Reglas v2.0 §2.7 — cross-ref GT-EINV validation file).
  (LB-017; EVID-182)
- **GT-TAX-FR-030:** Period débito adjustments: debit notes issued in the
  same period add their included IVA; credit-note deductions apply for
  returned goods, annulled-invoice values of already-declared operations,
  post-invoice bonifications/discounts and returned container deposits —
  each conditional on issuing the credit note and registering it within the
  FR-024 window. (LB-017; EVID-182)

### 3.7 Devolución del crédito fiscal (refund channels)

- **GT-TAX-FR-031:** Refund entitlement evaluation shall apply: exporters,
  and taxpayers rendering services or selling goods to exempt persons,
  qualify for refund of credit generated from inputs or expenses directly
  linked to those operations; taxpayers with exports < 50% of total annual
  sales qualify when they cannot compensate the credit against the débito
  of local sales. Denial grounds: invoice-authorization obtained on false
  documentation; exporter cannot document/demonstrate that invoice payments
  were effectively made (bancarización). (LB-010; LB-011; EVID-170,
  EVID-171)
- **GT-TAX-FR-032:** Channel A (general, Arts. 23/23-A): accumulated
  expired periods, quarterly or semiannual; SAT resolution SLA 30 días
  hábiles (trimestral) / 60 días hábiles (semestral); presumed denial on
  silence (petition taken as unfavorably resolved) with escalation;
  payment by the Banco de Guatemala charged to the *Fondo IVA*; adjustment
  handling = authorization only for the unadjusted balance. The Fondo IVA
  8% daily-separation funding rule (Art. 25/D-20-2006 art. 49) is its
  funding lineage. (LB-010; LB-012; LB-021; EVID-170, EVID-172, EVID-257)
- **GT-TAX-FR-033:** Channel B (optional, Arts. 24/24-A/24-B): election by
  exporters; application within the first 10 días hábiles after the monthly
  declaration deadline; CPA dictamen (independent public accountant and
  auditor, registered, colegiado activo, independent) on the procedence of
  the credit; 100% of the unretained credit refunded; SAT resolves in 10
  días hábiles and instructs the Banco de Guatemala; regime switching
  (into/out of, toward 23-"A"/25 regimes) only prospectively — before the
  next período impositivo starts; denial grounds (unregistered/inactive
  CPA, non-conforming dictamen, dependency/kinship). (LB-011; EVID-171)
- **GT-TAX-FR-034:** Channel C (Art. 25 BNG) parameter rows shall be
  stored as dated data with instrument provenance "D-27-92 Art. 25 (texto
  ≤ D-10-2012; Fondo IVA 8% rule added D-20-2006 art. 49)": monthly per
  expired calendar period, requested directly from the Banco de Guatemala
  in cash; 75% of declared credit when the refund is ≤ Q500,000.00; 60%
  when above; BNG fee ¼ of 1% deducted from each refund; qualification
  tests A (≥ 50% of annual sales destined to export) / B (< 50% with
  un-compensable credit); adjustments temporarily deducted from subsequent
  refunds (clawback); refunded amounts re-enter as débito fiscal of the
  next period (self-reversal posting); registry updates January/July.
  (LB-012; EVID-172; GOQ-50 pattern → OQ-003)
- **GT-TAX-FR-035:** The Q10,000.00 refund-application minimum shall be
  stored as a dated row (reglamento Art. 27): requests below it are not
  processed — the taxpayer accumulates credit until reaching the floor;
  justified exception via Ley Art. 23; BNG may still refund below the floor
  when the original request was above it and verification adjustments
  reduced the amount. (LB-019; EVID-184)
- **GT-TAX-FR-036:** The electronic 100% refund regime (*régimen especial
  electrónico*, reglamento Art. 25 bis citing "artículo 25 bis de la Ley")
  shall be recorded as a GOQ-01-dependent dated row: its statutory basis
  (Ley Art. 25 bis) is ABSENT from the corpus law copy — adder decree
  unidentified; mechanics as printed: electronic filing on the SAT
  platform, 10 días hábiles admission/rejection window, 30 días hábiles
  fondo resolution, FEL-incorporation precondition + annual January
  update. Entitlement evaluation is blocked from hard-coding until GOQ-01
  resolves; mechanics interface with the FEL mandate layer (GT-EINV
  mandate file). (LB-019; EVID-184; GOQ-01 → OQ-002)
- **GT-TAX-FR-037:** Export refund evidence handling shall require the
  reglamento Art. 24 pack: perfected definitive export declaration,
  bill of lading (*conocimiento de embarque*), manifest, packing list,
  traceability (tracking) report to arrival at the final destination port,
  and payment proof — the bancarización (payment-through-financial-system)
  evidence layer. (LB-019; EVID-184)

### 3.8 Documents, books & declaration skeleton

- **GT-TAX-FR-038:** The statutory document skeleton shall be recorded as
  Art. 29 prints it (after the D-4-2012/D-10-2012 total reforms):
  mandatory legible/permanent or electronic documents — a) facturas (incl.
  exempt operations and exempt persons), b) facturas de pequeño
  contribuyente, c) notas de débito, d) notas de crédito, e) otros
  documentos SAT authorizes in justified cases (lineage: literal added by
  D-20-2006 art. 50, re-lettered by the 2012 total reforms) — plus the
  generic electronic/other-means emission faculty delegated to the
  reglamento. The absences of Art. 29-"A" (FEL article, added D-4-2019
  art. 6), Art. 8-"A" and Ley Art. 25 bis in the corpus law copy are
  GOQ-01 facts; FEL DTE obligations come exclusively from the GT-EINV
  files — this layer never re-derives them. (LB-013; LB-021; EVID-173,
  EVID-257; GOQ-01 → OQ-002)
- **GT-TAX-FR-039:** On facturas, notas de débito, notas de crédito and
  facturas especiales the tax shall always be included in the price,
  except objective-exemption cases (Art. 32; pairs with FR-006).
  (LB-014; EVID-174)
- **GT-TAX-FR-040:** Invoice emission timing (Art. 34): goods invoices at
  the moment of actual delivery; services invoices at the moment the
  remuneration is received — pairs with the FR-003 tax point; FEL
  fecha-emisión validation is owned by GT-EINV (cross-ref). (LB-014;
  EVID-174)
- **GT-TAX-FR-041:** Books: general-regime taxpayers shall keep and
  maintain current a purchases-and-services-received book and a
  sales-and-services-rendered book (manual or computerized); the purchases
  book shall separate local, export and exempt-person sales operations
  (three-way separation, reglamento Art. 38) and pequeño-supplier
  invoices shall register with no value in the IVA column; monthly summary
  per reglamento Art. 39. Electronic-books surfaces (LET) are owned by the
  fiscal-reporting wave — cross-referenced. (LB-014; LB-018; EVID-174,
  EVID-183)
- **GT-TAX-FR-042:** Declaration skeleton (values cross-referenced to the
  F-wave, never re-derived here): monthly declaration of total operations
  of the prior calendar month — exempt included — filed and paid within the
  following calendar month; multi-establishment taxpayers declare and pay
  jointly on a single form; the duty survives inactivity unless
  suspension/termination is communicated in writing; taxpayers whose
  gravadas+exentas sales were below purchases for three consecutive
  periods must attach documented justification. The per-NIT due-date
  calendar is external (GOQ-14). (LB-014; EVID-174; GOQ-14 → OQ-005)

### 3.9 Fixed-fee IVA on used vehicles & especiales report

- **GT-TAX-FR-043:** Used-vehicle transfer IVA shall be charged as FIXED
  quetzal fees by model age, never as 12% ad valorem: automobiles
  Q1,000.00 (2–3 model years before the current year) / Q500.00 (4 or
  more); motorcycles Q300.00 (2–3) / Q200.00 (4+); totaled vehicles pay
  the maximum fixed fee; new vehicles (current/next/prior model year) and
  all maritime/aircraft transfers apply the Art. 10 rate on SAT's annual
  *tabla de valores imponibles* (taxable-value table). Stored as dated
  rows: values as of the ≤ D-10-2012 text; D-20-2006-era originals
  (Q500/300/100 cars; Q200/100/50 motorcycles) recorded as history — the
  raising instrument is not isolated in the corpus (GOQ-50 decree-bound
  watch; GOQ-01 currency qualifier). (LB-015; LB-021; EVID-178, EVID-257;
  OQ-003)
- **GT-TAX-FR-044:** Used-vehicle IVA is paid always in cash by the
  acquirer within 15 días hábiles counted from the legalization of the
  endorsement (*endoso*) in the Certificado de Propiedad de Vehículos;
  real-estate transfers base = the higher of the invoice price, escritura
  pública value or matrícula fiscal value (Art. 56); aportaciones valued
  by an authorized appraiser. (LB-015; EVID-178)
- **GT-TAX-FR-045:** Taxpayers qualified by SAT as *contribuyentes
  especiales* (special taxpayers) shall support a semi-annual electronic
  detailed purchase/sales report with per-counterparty fields: NIT, name,
  amount, date (Art. 57 "D" — statutory ancestor of the F-wave Informe
  Electrónico de Compras y Ventas; cross-referenced to the F-wave file,
  never duplicated). (LB-015; EVID-178)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance + as-of qualifier; snapshot-on-write; rate/fee/threshold rows
are decree-bound, never constants (GOQ-50 pattern); historical rows are
non-transmittable class.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.iva.rate | amount | decimal | 0.12 (tarifa única; price-inclusive) | FR-006 |
| l10n_gt.iva.rate | price_included | boolean | true (mandatory) | FR-006, FR-039 |
| l10n_gt.iva.rate | valid_from / valid_to / instrument | date / date / char | provenance "D-27-92 Art. 10, texto ≤ D-10-2012, reformado por… (≥ D-4-2019/D-31-2024/D-10-2025)"; GOQ-01 as-of qualifier | FR-006 |
| l10n_gt.iva.earmark | points / destination / account | decimal / char / char | 1.5 municipalidades; 1 Consejos Departamentales de Desarrollo; 1 Fondos para la Paz; 0.5 seguridad alimentaria; 0.5 educación primaria y técnica; 0.5 seguridad ciudadana; account "Fondo para el Desarrollo, el Gasto Social y la Paz"; provenance D-66-2002-era (GOQ-64); metadata-only, never computation input | FR-007 |
| l10n_gt.iva.exemption | numeral / kind / params | integer / selection objetiva-subjetiva / json | 15 objective families; params: menudeo max Q100.00/transaction; vivienda max Q250,000.00 + 80 m²; lote max Q120,000.00 + 120 m²; dated provenance "Art. 7, texto ≤ D-10-2012" (GOQ-01 qualifier) | FR-010, FR-011 |
| l10n_gt.iva.exempt.person.class | class_no / description | integer / char | 6 Art. 8 classes; guard rows: 8-"A" derogated 2025-11-04 (D-10-2025 art. 1); "3-'A'" never existed | FR-013 |
| l10n_gt.iva.credit.policy | report_window_months / nota_window_months | integer | 2 / 2 (forfeit after) | FR-023, FR-024 |
| l10n_gt.iva.credit.exclusion | rule_key | char | open list: personal_use, retiros, unlinked_assets, unlinked_vehicle_fuel_lub_insurance, pequeno_supplier_purchases (non-exhaustive) | FR-026 |
| l10n_gt.iva.prorrateo | method | selection | proportional over gravadas+exentas, gravadas share claimed (verbal rule; formula = operationalization tag) | FR-027 |
| l10n_gt.iva.refund.channel | code / cadence / sla_dias_habiles / pct_or_floor | char / char / integer / decimal | A general: trimestral/semestral, 30/60, Fondo IVA-BNG; B optativo: mensual (post-declaration 10-dh filing window), 10 dh, 100% CPA-dictamen; C BNG: mensual, 75% ≤ Q500,000.00 / 60% >, fee ¼ of 1%; E electrónico: 100%, 10 dh admission + 30 dh fondo, FEL-gated (GOQ-01-dependent row) | FR-032..036 |
| l10n_gt.iva.refund.parameter | key / value / provenance | char / decimal / char | min_request Q10,000.00 (reglamento Art. 27); qualification_export_share 0.50 (Art. 25 A/B) | FR-034, FR-035 |
| l10n_gt.iva.vehicle.fee | vehicle_class / age_band / fee / valid_from / provenance | selection / selection / decimal / date / char | auto: 2-3y Q1,000.00, 4+y Q500.00; moto: 2-3y Q300.00, 4+y Q200.00; totaled = max fixed; history rows D-20-2006 Q500/300/100 + Q200/100/50 | FR-043 |
| l10n_gt.iva.hecho.generador | numeral / description | integer / char | 10 numerales; floor numerals = 5, 6, 9 | FR-001, FR-002 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Taxation
defaults per wave plan: rate/exemption/refund-parameter dated data =
`shared`; invoice/line computation, credit registration windows, regime
flags = `odoo`; refund-entitlement evaluation and bancarización proof
handling = `saas` with odoo surfaces. Model names stable across Odoo
17/18/19/20; no version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | account.move.line / product config | tax-affected operation classifier | Drives whether IVA applies per operation type; retiros/faltantes flow through stock moves → invoice lines (Art. 3 núms. 6/7) |
| FR-002 | odoo | account.move (valuation) | price unit floor = acquisition/manufacturing cost | Floor applied at line creation for numerales 5/6/9 |
| FR-003 | odoo | account.move | invoice_date / delivery-date fallback field | Tax point = earlier of invoice date / actual delivery (goods) or remuneration perception (services) |
| FR-004 | odoo | account.move.line (deferred/periodic) | period perception flag | Leases + periodic services accrue per perceived period |
| FR-005 | odoo | account.invoice import flow (customs) | payment-of-duties date | Import base & duty receipt (FR-018/FR-021/FR-023) ride the customs invoice line |
| FR-006 | shared | — (config data §4) | l10n_gt.iva.rate rows | Both sides resolve the same dated 12% row as-of the document date; price-inclusive contract |
| FR-007 | shared | — (config data §4) | l10n_gt.iva.earmark rows | Metadata-only (GOQ-64); never a computation input on either side |
| FR-008 | shared | — | guard row | "Derogado" only — no differentiated petroleum rate exists in this layer on either side |
| FR-009 | shared | — (config data §4) | rate-exception registry | pequeño 5% row owned by Task 2 file; vehicle fixed fees FR-043; no other ad-valorem rate |
| FR-010 | shared | — (config data §4) | l10n_gt.iva.exemption catalog | Same exemption catalog consumed by odoo invoice lines and saas validation |
| FR-011 | shared | — (config data §4) | exemption params | Q100/Q250,000/80 m²/Q120,000/120 m² dated rows; GOQ-01 currency qualifier |
| FR-012 | shared | — | guard row | peaje/turismo/canasta NOT modeled; pending GOQ-01 |
| FR-013 | shared | — (config data §4) | exempt person classes | 8-"A" derogation fact row; "3-'A'" myth guard |
| FR-014 | odoo | account.move + res.partner (exempt flag) | fiscal position / constancia handling | Zero-IVA invoice to exempt buyer; sale reported gravada + constancia credit; CIVA DTE side = GT-EINV-FR-030 |
| FR-015 | odoo | account.move (pequeño supplier) | no-constancia rule | Exempt buyer pays full pequeño invoice; pequeño side = Task 2 |
| FR-016 | odoo | account.move.line | base computation | price − commercial discounts + finance + packaging/deposits + invoiced sums |
| FR-017 | odoo | account.move.line | service-base additions | Statutory contributions excluded; tips included (reglamento detail) |
| FR-018 | odoo | account.invoice import line | CIF + duties base | Customs import lines |
| FR-019 | odoo | account.tax / product | vinculación flag | Credit eligibility criteria a/b |
| FR-020 | odoo | account.asset | IVA-out-of-cost flag | Credited IVA excluded from ISR depreciation base; ISR files consume |
| FR-021 | odoo | account.move (supplier) | partner VAT/NIT validation | No credit without taxpayer-name + NIT on document |
| FR-022 | shared | — | documentation contract | GFACE phrasing = pre-FEL vintage; current electronic credit docs = FEL DTEs (GT-EINV); both sides key on the same set |
| FR-023 | odoo | account.move (credit eligibility) | 2-month report window flag | Forfeit after window; dated eligibility computed at registration |
| FR-024 | odoo | account.move (notes) | 2-month nota registration | Enforced on NC/ND registration timing |
| FR-025 | odoo | account.move / credit carryforward | saldo traslado | Indefinite carry-forward; refund blocked except channels; retention netting = Task 3 |
| FR-026 | odoo | account.tax / expense config | no-credit rules | Open list config; pequeño purchases auto-excluded |
| FR-027 | odoo | account.tax computation | prorrateo method | Proportional distribution; formula operationalization tagged |
| FR-028 | odoo | product/expense config | exporter credit list | Seeded open guidance list |
| FR-029 | odoo | account.tax computation | ÷1.12 × 0.12 extraction | Applies to gross amounts; mirrors Reglas §2.7 (GT-EINV validation file) |
| FR-030 | odoo | account.move (NC/ND adjustments) | débito add/subtract cases | Conditional on FR-024 registration |
| FR-031 | saas | res.company / refund eligibility module | entitlement evaluation | Exporter / seller-to-exempt evaluation; odoo surfaces the flags |
| FR-032 | saas | refund request flow | 30/60 dh SLA + presumed denial | BNG/Fondo IVA payment instruction data; odoo records request + escalation state |
| FR-033 | saas | refund request flow (optativo) | CPA dictamen attach + 10 dh | Odoo surfaces election + regime-switch prospective-only rule |
| FR-034 | shared | — (config data §4) | BNG channel dated parameter rows | 75/60/Q500,000/8%/¼ of 1% decree-bound rows (GOQ-50); procedure surfaces saas-side |
| FR-035 | shared | — (config data §4) | Q10,000 floor row | Accumulation duty until floor; odoo accumulates, saas validates |
| FR-036 | saas | refund request flow (electronic) | 100%/10 dh/30 dh, FEL gate | GOQ-01-dependent dated row — entitlement not hard-coded; FEL incorporation check via GT-EINV mandate data |
| FR-037 | saas | refund evidence pack | export docs + payment proof | Bancarización proof handling; odoo upload surface |
| FR-038 | shared | — | document skeleton citation spine | Absence facts (29-"A"/8-"A"/25 bis) = GOQ-01; FEL DTE duties = GT-EINV only |
| FR-039 | odoo | account.move | price-inclusive display | Except objective exemptions |
| FR-040 | odoo | account.move | emission timing | Pairs FR-003; FEL fecha validation = GT-EINV |
| FR-041 | odoo | account books / reporting | purchases/sales book separation | Three-way split; pequeño rows no-IVA column; LET surfaces = F-wave |
| FR-042 | odoo | account.move (declaration skeleton) | monthly window + consolidation | Form generation = F-wave; per-NIT calendar external (GOQ-14) |
| FR-043 | shared | — (config data §4) | vehicle fee dated rows | Q1,000/500/300/200 + D-20-2006 history rows; never 12% ad valorem |
| FR-044 | odoo | vehicle transfer flow | 15-dh payment + base rules | Cash-by-acquirer; inmuebles higher-of base |
| FR-045 | odoo | especiales report surface | semi-annual report fields | F-wave Informe Electrónico owns the filing surface (cross-ref) |

## 6. Acceptance Criteria

- **AC-001:** Given any operation of an Art. 3 numeral class (1–10), when
  invoiced, then it carries IVA per this file; given an operation outside
  the taxonomy, then no IVA is applied. (FR-001)
- **AC-002:** Given an inventory withdrawal, in-payment adjudication or
  inter-vivos donation valued below acquisition/manufacturing cost, when
  the invoice line is created, then the base is floored at that cost.
  (FR-002)
- **AC-003:** Given goods delivered before invoice emission (or a service
  paid without invoice), when the tax point is resolved, then it is the
  delivery date (or the remuneration-perception date), not a later
  invoice date. (FR-003, FR-004)
- **AC-004:** Given the rate registry, when read as-of any document date,
  then it resolves one dated 12% price-inclusive row with instrument
  provenance "D-27-92 Art. 10, texto ≤ D-10-2012, reformado por…" and no
  other ad-valorem rate exists besides the Task-2 pequeño 5% row and the
  FR-043 fixed fees. (FR-006, FR-009)
- **AC-005:** Given the earmark rows, when inspected, then the 3.5 + 1.5
  pp splits match LB-006 verbatim, carry the D-66-2002-era provenance
  flag, and no computation path consumes them (GOQ-64). (FR-007)
- **AC-006:** Given a market-retail sale over Q100.00 per transaction, a
  social-housing sale over Q250,000.00 or 80 m², or an urbanized lot over
  Q120,000.00 or 120 m², when exemption is attempted, then it is refused
  (dated parameter rows). (FR-011)
- **AC-007:** Given an Art. 8 exempt-person buyer, when the invoice is
  issued, then it is a normal factura at zero IVA and the flow requires
  the constancia de exención; given the same buyer purchasing from a
  pequeño supplier, then the full invoice is payable with no constancia.
  (FR-014, FR-015)
- **AC-008:** Given a gross (price-inclusive) taxable invoice, when the
  débito is computed, then tax = base × 0.12 with base = gross ÷ 1.12,
  matching the statutory arithmetic to the centavo. (FR-029)
- **AC-009:** Given a supplier invoice document dated more than two months
  before the reporting period being closed (or a nota not registered
  within two months of its modified invoice), when credit is claimed, then
  the claim is rejected as forfeited. (FR-023, FR-024)
- **AC-010:** Given a taxpayer with gravadas and exentas sales and
  unseparable input IVA, when the monthly credit is computed, then only
  the gravadas proportion (IVA × gravadas ÷ (gravadas + exentas)) is
  claimed, with the formula tagged as operationalization of the printed
  verbal rule. (FR-027)
- **AC-011:** Given excess credit, when period closing runs, then the
  saldo carries forward indefinitely and no refund path opens except the
  Arts. 23/23-A/24/25(+25 bis GOQ-01-dependent) channels with their dated
  parameter rows (30/60 dh, 10 dh, 75/60% keyed to Q500,000.00,
  Q10,000.00 floor). (FR-025, FR-032..036)
- **AC-012:** Given a used-vehicle transfer aged 2–3 model years (car) or
  4+ years (motorcycle), when invoiced, then the fixed fee is Q1,000.00 /
  Q500.00 (cars) or Q300.00 / Q200.00 (motorcycles) — never 12% ad
  valorem — and payment is recorded as cash by the acquirer within 15 días
  hábiles of the endoso legalization. (FR-043, FR-044)
- **AC-013:** Given any surface citing the IVA law, when citations are
  generated, then every 23_-derived row carries the "D-27-92 (texto ≤
  D-10-2012), reformado por…" qualifier and no myth string ("resolución
  2-2010", "Art. 3-'A'") appears anywhere in the seeded data. (LB-001;
  FR-013, FR-038)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text verbatim from the register (abbreviated where noted). All
rows Status open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-64 (owned): "Art. 10 earmark architecture = D-66-2002-era text; post-2012 earmark reforms unverifiable from 23_." Affects FR-007 (earmark rows are metadata-only until resolved). | no | GT synthesis wave S-GT2 → acquisition queue (post-2012 reform instruments) | open |
| OQ-002 | GOQ-01 (kin, register lists TX1/TX2/TX3 freeze): "Post-2018 consolidated Ley IVA 27-92 text: Art. 29-'A' body, Ley 25 bis adder (electronic 100% refund), art. 54 B/BIS nomenclature, post-2012 exemption families (peaje/turismo/canasta), Q150,000 currency." Affects FR-011 (currency), FR-012 (absent families), FR-022 (FEL documentation hook), FR-036 (25 bis channel), FR-038 (29-'A' absence). | no | GT synthesis wave S-GT2 → acquisition queue (DCA Edición Legal / accountant) | open |
| OQ-003 | GOQ-50 (pattern kin): "Rate rows (IDP Q4.70…, IBN, CEM, TAP, regime %) are decree-bound dated values ('Sujeta a la vigencia de leyes y reglamentos') — D-GT10 watchlist, never constants." Applied here to FR-006/FR-034/FR-035/FR-043 (12%, 75/60, Q10,000, vehicle fees): each stores dated rows with instrument provenance; the vehicle-fee raising instrument (Q500/300/100 → Q1,000/500/300/200) is not isolated in the corpus. | no | GT synthesis wave S-GT2 (dated-row discipline) | open |
| OQ-004 | GOQ-13 (kin): "D-31-2024 full text acquisition (added IVA 8-'A'; …) + clean-DCA verification of D-10-2025's '8 A' reading (OCR 8/3 residue)." Affects FR-013's 8-"A" derogation fact row (recorded as printed; "3-'A'" never existed). | no | GT synthesis wave S-GT2 → acquisition queue (shared with S-GT1) | open |
| OQ-005 | GOQ-14 (kin): accountant asks pending — consolidated IVA print (folds into GOQ-01) and calendario perpetuo vencimiento windows per NIT last-digit. Affects FR-042 (per-NIT due-date calendar is external; only the "following calendar month" statutory window is modeled here; FEL anulación window consumes the same calendar — GT-EINV 06 file). | no | GT synthesis wave S-GT2 → W6 partner ask (accountant) | open |
