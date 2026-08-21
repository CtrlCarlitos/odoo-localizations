# SV — Commercial-legal — Sales and intermediary contracts: compraventa mercantile, defect/warranty clocks, INCOTERM-analog clauses, venta a plazos, estimatorio, permuta, suministro, comisión, mandato mercantil (C9)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador sales-contract and intermediary layer
of the Código de Comercio (Commercial Code, CC): the *compraventa
mercantile* (mercantile sale) scope of Art. 1013 — the giro-normal and
cosas-mercantiles prongs with the farm/artisan carve-out — and the
formation rules of Arts. 1014-1015: price determination
(bolsa/mercado fixed-date reference, habitual-goods presumption,
delivery-day market price) with *arras* (earnest money) ALWAYS
allocated to the price, and the signed *pedido* (order) that binds the
buyer; the delivery default of Art. 1020 (seller's establishment, else
his domicilio); the **defect/warranty clocks of Arts. 1019-1021 —
apparent-defect waiver on satisfactory examination, the 8-day
packaged-goods claim window, the hidden-vices 15-day
denounce-from-discovery clock proven by *acta notarial* (notarial
instrument) with the 1-year prescription from delivery, and the
functioning-warranty 30-day denounce under caducidad / 6-month action
/ 3-year no-term default — tracked at LOT level**; the perfection
regimes of Arts. 1022-1024 (*gusto* — things customarily tasted/tried,
with silence-equals-approval; *a prueba* — sale on approval under
suspensive condition; *muestras* — sample/known-quality sales
requiring INDIVIDUALIZATION for property transmission); the
installment-resolution mechanics of Arts. 1025-1026 with their
identifiable-goods registry opposability; the documents-over-goods
regime of Arts. 1027-1029 (delivery by remitting representative
documents, pay-at-documents, transit risk from carrier receipt, D/a
and D/P clauses); the **in-code INCOTERM-analog clauses of
Arts. 1030-1035 — CSF/CIF/CAF (cost+insurance+freight) with the
seller's three obligations and the no-insurance sanction, CF
(cost+freight), and LAB/FOB (free on board) with their risk-pass
points**; the *venta a plazos de bienes muebles* (installment sale of
movables with reserved domain) regime of Arts. 1038-1050 — Registro
de Comercio inscription within 30 days, endoso negotiability,
third-party opposability, the 10-day judicial *intimación* (demand)
before de-pleno-derecho resolution, the Art. 1045 ajuste capped by
Art. 1026, the 3-month prescription, buyer-side risks/taxes/insurance,
and the five acceleration events; the *contrato estimatorio*
(consignment sale) of Art. 1051 with its ownership invariant; the
*permuta* (exchange) rules of Arts. 1052-1054; the *suministro*
(supply) regime of Arts. 1055-1065 — periodic/continued prestations,
needs-based quantity with min-max, price per prestación, exclusivity
BOTH ways with zone binding, and the 3-month denounce of no-duration
contracts; and the intermediary contracts — *comisión* (Arts.
1066-1082: own name/foreign account, 8-day silence-acceptance, NO
credit without authorization — else cash-demandable, named-buyer
reporting with deemed-cash sanction, retention right and
commission-withholding) and *mandato mercantil* (Arts. 1083-1097:
account AND name, 8-day refusal notice, silence-ratification of
executed business).

It does **not** cover: merchant status, matrícula and the registry
architecture (`01_merchant-registration.md` — the registry-entry model
consumed here BY ID for the venta-a-plazos and resolutoria-clause
inscriptions); book/retention discipline (`02_accounting-books.md`);
the annual statement cycle (`03_financial-statements.md`); society
types (`04_society-types.md`); society lifecycle
(`05_society-lifecycle.md`); commercial agents and authority defaults
(`06_commercial-agents.md` — the dependiente-authority defaults and
the agent-side pedido-acceptance kin consumed by id; the comisión and
mandato mercantil contracts here are the own-name/foreign-account and
name-and-account layers the agentes chapter does NOT own); the
empresa mercantil and EIRL (`07_empresa-mercantil-eirl.md`); payment
instruments, mora interest and the prescription matrix
(`08_payment-instruments.md` — SV-CML-FR-145 day-count conventions,
SV-CML-FR-158 legal-rate config, SV-CML-FR-160 matrix and
SV-CML-FR-162 caducidad regime consumed by id: this file's clocks
register anchors and code-internal override rows there, never restate
the Art. 995 terms); the export-invoice INCOTERM capture, owned by the
e-invoicing wave (SV-EINV-FR-045, cited by id); and AML compliance
(`10_aml-compliance.md`). The Art. 712 documents-against mechanics,
the Art. 1036 installment sale of títulos valores and the Art. 1037
lotificadora rules are recorded as scope notes (§3.13), not FRs.

## 2. Legal Basis

Authority order (binding, per master evidence index S5): the Código de
Comercio = **07_** (D.L. Nº 671, 8-may-1970, D.O. 140 T.228 31-jul-1970;
29 listed reforms, last = D.L. 641-2008) — article text CURRENT per the
**SOQ-22 verification (resolved-with-residual, W12 2026-08-18)**: the
second official copy 73_ (UIF-hosted Índice Legislativo edition) also
ends its reform list at D.L. 641-2008, so no post-2008 CC structural
reform is evidenced in two official consolidations; the residual —
both copies are Asamblea-editorial artifacts without a stated as-of
date — rides every 07_ LB in this file. Governing evidence: EVID-227
(Arts. 1013-1097, pp.170-182). The evidence file compresses this
article set to gloss level, so verbatim text below is copied from the
extraction txt `sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable
per standing ruling; page pointers = txt PAGE markers); truncation
markers inside LB quotations label every omission explicitly, and
single-word deviations are defects.

Currency discipline (**SOQ-29**): ONE colones-era remnant occurs in
this article set — Art. 1038's "un mil colones" inscription-benefit
threshold, an UNREFORMED 1970 colones phrase (kin of 07_ OQ-7). It is
cited as historical text, read against dollarization with the
operative currency treated as USD, and shipped as a FLAGGED
configuration slot with NO default value (OQ-001) — never hardcoded.
No other colones-denominated value occurs here; the remaining terms
(8d/10d/15d/30d/6m/1y/3m/3y) are un-reformed statutory day/month
counts under the SOQ-22 residual watch.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 1013: "Son compraventas mercantiles: I.- Las que se realizan dentro del giro de explotación normal de una empresa mercantil. II.- Las de cosas mercantiles." "No son mercantiles las ventas hechas por los agricultores o ganaderos, de los frutos o productos de sus cosechas y ganados, o de las especies que se les den en pago, cuando no tengan almacén o tienda para su expendio, ni las que hicieren los artesanos en sus talleres de los objetos fabricados en ellos." | Mercantile sales are: I. those realized within the normal exploitation giro of an empresa mercantil; II. those of cosas mercantiles (mercantile things). NOT mercantile are: sales by farmers or livestock raisers of the fruits or products of their harvests and livestock, or of the species given them in payment, when they keep NO almacén o tienda (store or shop) for their expendio (sale); nor those made by artisans in their talleres (workshops) of the objects fabricated there | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1013 pp.170-171 (EVID-227; txt PAGE 170-171) |
| LB-002 | Código de Comercio, Art. 1014: "El precio se considerará determinado si se hace referencia al señalado o que se señale en bolsa o mercado, nacional o extranjero, en fecha fija." "Si el contrato tiene por objeto cosas vendidas habitualmente por el vendedor y las partes no hubieren convenido en el precio o en el modo de determinarlo, se presumirá que han quedado conformes con aquel exigido normalmente por el vendedor, a no ser que se trate de cosas que tengan precio de mercado o bolsa, en cuyo caso la presunción será por el que tuvieren en dichos establecimientos en el día de entrega." "Las arras, anticipos y cantidades entregadas en señal del contrato, se entenderán siempre a cuenta del precio." | The price is considered DETERMINED if reference is made to the one fixed or to be fixed at a bolsa (exchange) or market, national or foreign, at a FIXED DATE. Where the contract concerns things HABITUALLY SOLD by the seller and the parties have not agreed on the price or the mode of determining it, they are PRESUMED to have accepted the one NORMALLY REQUIRED BY THE SELLER — unless the things have a market or bolsa price, in which case the presumption is the price they bear at those establishments ON THE DELIVERY DAY. Arras (earnest money), anticipos (advances) and quantities delivered as sign of the contract are ALWAYS understood TO THE ACCOUNT OF THE PRICE | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1014 p.171 (EVID-227; txt PAGE 171) |
| LB-003 | Código de Comercio, Art. 1015: "Quien haya firmado, por sí o por medio de representante o dependiente autorizado, un pedido de mercaderías, está obligado a tomarlas, en las condiciones que el pedido exprese. La otra parte tendrá acción en juicio sumario para consignar las mercaderías a la orden del comprador y simultáneamente para exigirle el pago del precio y la indemnización de los perjuicios ocasionados por el retardo." | Whoever has signed — by himself or through a representative or AUTHORIZED DEPENDIENTE — a pedido (order) for merchandise is OBLIGED TO TAKE IT, on the conditions the pedido expresses. The other party has action in JUICIO SUMARIO (summary proceeding) to consign the merchandise to the buyer's order and SIMULTANEOUSLY demand from him payment of the price and indemnification of the damages caused by the delay | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1015 p.171 (EVID-227; txt PAGE 171) |
| LB-004 | Código de Comercio, Art. 1020: "Salvo pacto expreso en contrario, las cosas se entregarán en el establecimiento del vendedor o, si no lo tuviere, en su domicilio." | Save EXPRESS PACT to the contrary, the things are delivered at the SELLER'S ESTABLISHMENT or, if he has none, at his DOMICILIO (default delivery place) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1020 p.172 (EVID-227; txt PAGE 172) |
| LB-005 | Código de Comercio, Art. 1019: "El comprador que al tiempo de recibir las cosas las examinare a su satisfacción, no tendrá acción para repetir contra el vendedor por defecto de calidad o cantidad aparente de aquéllas." "El comprador tendrá derecho de repetir contra el vendedor por esos motivos, si hubiere recibido las cosas enfardadas o embaladas, siempre que ejercite la acción dentro de los ocho días siguientes al de su recibo, y no proceda la avería de caso fortuito, vicio propio de las cosas o fraude de tercero." "El vendedor podrá exigir, en el acto de la entrega, que se haga el reconocimiento a satisfacción del comprador." "Si los vicios fueren ocultos, el comprador deberá denunciarlos dentro de los quince días siguientes a su descubrimiento o en el plazo que las partes hubieren convenido. La denuncia se prueba por acta ante notario." "Hecha la denuncia en el término y forma indicados en el inciso anterior, el comprador tendrá los recursos que determina el Código Civil. Las acciones mencionadas prescriben en un año contado desde la entrega." | The buyer who, at the time of receiving the things, EXAMINES THEM TO HIS SATISFACTION has NO action to repeat against the seller for APPARENT quality or quantity defects. The buyer DOES have the right to repeat on those grounds if he received the things ENFARDADAS O EMBALADAS (in packs or packages), provided he exercises the action WITHIN THE EIGHT DAYS FOLLOWING THEIR RECEIPT and the avería (damage) does not proceed from caso fortuito (fortuitous event), vicio propio (inherent vice) of the things or fraud of a third party. The seller may demand, at the act of delivery, that the recognition (inspection) be made to the buyer's satisfaction. If the vices are HIDDEN, the buyer must DENOUNCE them within the FIFTEEN DAYS FOLLOWING THEIR DISCOVERY or within the term the parties agreed; the denounce is proved BY ACTA ANTE NOTARIO (notarial instrument). Denounced in the term and form indicated, the buyer has the recursos (remedies) the Código Civil determines; the actions mentioned PRESCRIBE IN ONE YEAR COUNTED FROM DELIVERY | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1019 pp.171-172 (EVID-227; txt PAGE 171-172) |
| LB-006 | Código de Comercio, Art. 1021: "Si el vendedor garantiza por tiempo determinado el funcionamiento de la cosa vendida, el comprador, salvo pacto en contrario, deberá denunciarle el defecto de funcionamiento dentro de los treinta días de haberlo descubierto, bajo pena de caducidad. La denuncia se prueba por acta ante Notario." "La acción prescribirá en seis meses contados desde la fecha de la denuncia." "El Juez, de acuerdo con las circunstancias, podrá fijar un plazo para la sustitución o reparación de la cosa, sin perjuicio del resarcimiento de los daños." "Las garantías sin determinación de plazo se dan por tres años." | Where the seller GUARANTEES FOR A DETERMINED TIME the functioning of the thing sold, the buyer — save contrary pact — must denounce the functioning defect to him WITHIN THE THIRTY DAYS OF HAVING DISCOVERED IT, UNDER PENALTY OF CADUCIDAD (lapse); the denounce is proved by acta before a Notary. The action PRESCRIBES IN SIX MONTHS counted from the date of the denounce. The Judge, according to the circumstances, may fix a term for the SUBSTITUTION OR REPAIR of the thing, without prejudice to the resarcimiento (indemnification) of damages. Warranties WITHOUT determined term are given FOR THREE YEARS | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1021 p.172 (EVID-227; txt PAGE 172) |
| LB-007 | Código de Comercio, Art. 1022: "La compraventa de cosas que se acostumbra gustar se perfeccionará cuando se comunique al vendedor la decisión correspondiente." "Si el examen de la cosa debiera hacerse en el establecimiento del vendedor, el contrato se perfeccionará si el comprador no procede a tal examen, en el plazo establecido por el contrato o en el que fijare el uso y, en defecto de ambos, dentro del término conveniente fijado por el propio vendedor." "Si la cosa estuviere en poder del comprador y éste no resolviere dentro del plazo indicado, el silencio constituirá aprobación del contrato." Art. 1023: "La compraventa a prueba se presumirá hecha bajo la condición suspensiva de que la cosa tenga las calidades necesarias para el uso a que se la destina." "La prueba deberá realizarse en el plazo y forma convenidos en el contrato o fijado por el uso." | The sale of things CUSTOMARILY GUSTADAS (tasted/tried) is PERFECTED when the corresponding decision is COMMUNICATED to the seller. If the examination of the thing must take place at the seller's establishment, the contract is perfected if the buyer does NOT proceed to that examination within the term established by the contract or fixed by usage and, failing both, within the convenient term fixed by the seller himself. If the thing is IN THE BUYER'S POWER and he does not resolve within the indicated term, THE SILENCE CONSTITUTES APPROVAL OF THE CONTRACT. The sale A PRUEBA (on approval/test) is presumed made under the SUSPENSIVE CONDITION that the thing has the qualities necessary for the use to which it is destined; the test must be realized in the term and form agreed in the contract or fixed by usage | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1022-1023 p.172 (EVID-227; txt PAGE 172) |
| LB-008 | Código de Comercio, Art. 1024: "En la compraventa sobre muestras o calidades conocidas en el comercio, la determinación del objeto se hará con referencia a la muestra o la calidad. Para la transmisión de propiedad precisa que la cosa sea individualizada. La individualización se hará por acuerdo de comprador y vendedor, a no ser que por convenio o por el uso pueda hacerse exclusivamente por el vendedor." | In the sale over MUESTRAS (samples) or qualities known in commerce, the determination of the object is made by REFERENCE TO THE SAMPLE OR THE QUALITY. For the transmission of property it is REQUIRED that the thing be INDIVIDUALIZED. The individualization is made by AGREEMENT of buyer and seller, unless by convention or usage it may be made EXCLUSIVELY BY THE SELLER | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1024 p.172 (EVID-227; txt PAGE 172) |
| LB-009 | Código de Comercio, Art. 1025: "Cuando el precio haya de ser pagado en abonos, podrá pactarse que la falta de pago de uno o varios de ellos produzca la resolución del contrato, según las reglas siguientes: I.- Tratándose de inmuebles, o de bienes muebles tales como automóviles, motores, pianos, máquinas de coser u otros que puedan ser identificados de modo indudable, la resolución de la compraventa surtirá efectos contra terceros adquirentes de dichos bienes, cuando la cláusula resolutoria hubiere sido inscrita en el Registro de Comercio o en el de la Propiedad Raíz, en su caso. II.- Si se trata de bienes muebles cuya identificación no sea posible establecer de modo indudable, la resolución del contrato no producirá efectos contra terceros de buena fe que los hayan adquirido." | When the price is to be paid in ABONOS (installments), the parties may pact that non-payment of one or several of them produces the RESOLUTION of the contract, per these rules: I. for real property, or movable goods such as automobiles, motors, pianos, sewing machines or others that can be IDENTIFIED INDUBITABLY, the resolution of the sale has effects AGAINST THIRD-PARTY ACQUIRERS of those goods when the RESOLUTORIA (resolutory) CLAUSE has been INSCRIBED in the Registro de Comercio or in that of Propiedad Raíz, as the case may be; II. for movable goods whose identification cannot be indubitably established, the resolution has NO effects against GOOD-FAITH third parties who acquired them | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1025 p.172 (EVID-227; txt PAGE 172) |
| LB-010 | Código de Comercio, Art. 1026: "Si se resolviere el contrato, deberán restituirse las prestaciones realizadas. El vendedor tendrá derecho a exigir del comprador el pago de una indemnización por el uso que hubiere hecho de la cosa y por el deterioro que haya sufrido; ambos se fijarán por peritos." "El comprador que hubiere pagado parte del precio, tendrá derecho a los intereses legales de la cantidad que entregó." "El pacto que imponga a cualquiera de las partes, condiciones más onerosas que las expresadas, será nulo." "Este artículo y el anterior son aplicables a todo caso de diferimiento en el pago del precio, aunque el contrato se haga en forma de arrendamiento con promesa de venta o en cualquiera otra análoga." | If the contract is resolved, the prestations realized must be RESTITUTED. The seller may demand from the buyer payment of an INDEMNIFICATION FOR THE USE made of the thing and for the DETERIORATION it has suffered — both fixed by PERITOS (experts). The buyer who has paid part of the price is entitled to the LEGAL INTEREST on the quantity delivered. A pact imposing on either party conditions MORE ONEROUS than those expressed is NULL. This article and the preceding one apply to EVERY case of deferral of the price's payment, though the contract be made in the form of a LEASE WITH PROMISE OF SALE or any other analogous form | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1026 p.173 (EVID-227; txt PAGE 173) |
| LB-011 | Código de Comercio, Art. 1027: "Si la compraventa es sobre documentos, el vendedor cumplirá su obligación de entrega remitiendo al comprador el título representativo de las mercancías y los demás documentos indicados en el contrato o exigidos por la costumbre. Salvo pacto en contrario, el pago del precio deberá hacerse en el momento en que se entreguen los documentos. El comprador no puede negarse a pagar alegando defectos en calidad o estado de las cosas a no ser que presente pruebas de tales defectos." | If the sale is OVER DOCUMENTS, the seller performs his delivery obligation by REMITTING to the buyer the título representativo (document of title) of the merchandise and the other documents indicated in the contract or required by custom. Save contrary pact, the price must be paid AT THE MOMENT THE DOCUMENTS ARE DELIVERED. The buyer CANNOT refuse to pay alleging defects in the quality or state of the things UNLESS he presents PROOFS of such defects | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1027 p.173 (EVID-227; txt PAGE 173) |
| LB-012 | Código de Comercio, Art. 1028: "Si las cosas se encuentran en curso de ruta, y entre los documentos entregados figura la póliza de seguro por los riesgos del transporte, éstos quedarán a cargo del comprador desde el momento de la entrega de las mercancías al porteador; a menos que el vendedor haya sabido, al tiempo de celebrar el contrato, la pérdida o avería de las cosas y lo hubiere ocultado al comprador." Art. 1029: "Si en el contrato de compraventa se inserta la cláusula 'documentos contra aceptación' (D/a), o 'documentos contra pago' (D/P), se estará a lo dispuesto en el Art. 712." | If the things are EN CURSO DE RUTA (in transit) and among the delivered documents figures the insurance policy for the transport risks, those risks are ON THE BUYER from the moment of DELIVERY OF THE MERCHANDISE TO THE CARRIER — unless the seller KNEW, at the time of contracting, of the loss or avería of the things and CONCEALED it from the buyer. If the clause "documentos contra aceptación" (documents against acceptance, D/a) or "documentos contra pago" (documents against payment, D/P) is inserted in the sale contract, the provisions of Art. 712 govern (bank-operations zone — pointer only, §3.13/OQ-002) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1028-1029 p.173 (EVID-227; txt PAGE 173) |
| LB-013 | Código de Comercio, Art. 1030: "En la compraventa 'costo seguro y flete' (csf, cif o caf) el precio comprenderá el valor de la cosa más las primas del seguro y los fletes, hasta el lugar convenido para que sea recibida por el comprador." Art. 1031: "El vendedor, en la compraventa a que se refiere el artículo anterior, se entenderá obligado: I.- A contratar el transporte en los términos convenidos, a pagar el flete y a obtener del porteador, el conocimiento de embarque o la carta de porte respectivos. II.- A tomar seguro por el valor total de la cosa vendida, a favor del comprador o la persona por éste indicada, que cubra los riesgos convenidos o los usuales, y a obtener para el comprador la póliza o certificado correspondiente. III.- A entregar al comprador o a la persona que éste designe, los documentos referidos." | In the sale "COSTO SEGURO Y FLETE" (cost, insurance and freight — csf, cif or caf) the price comprises the value of the thing PLUS the insurance PRIMAS (premiums) and the FREIGHTS, up to the agreed place for its receipt by the buyer. The seller in that sale is understood obliged: I. to CONTRACT THE CARRIAGE on the agreed terms, PAY THE FREIGHT and obtain from the carrier the conocimiento de embarque (bill of lading) or carta de porte (consignment note); II. to TAKE INSURANCE FOR THE TOTAL VALUE of the thing sold, in favour of the buyer or the person he indicates, covering the agreed or usual risks, and to obtain for the buyer the corresponding policy or certificate; III. to DELIVER the referred documents to the buyer or his designee | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1030-1031 p.173 (EVID-227; txt PAGE 173) |
| LB-014 | Código de Comercio, Art. 1032: "Si el vendedor 'csf' no contratare el seguro en los términos señalados en el artículo anterior, responderá al comprador, en caso de siniestro, como hubiere respondido el asegurador. El comprador puede contratar el seguro y deducir la prima del precio debido al vendedor." Art. 1033: "Salvo pacto o uso en contrario, el conocimiento de embarque o la carta de porte, se costearán por ambos contratantes, pero los riesgos serán a cargo del comprador desde el recibo de las mercancías por el porteador." | If the "csf" seller does NOT contract the insurance in the terms of the preceding article, he answers to the buyer, in case of SINIESTRO (casualty), AS THE INSURER WOULD HAVE ANSWERED. The buyer may contract the insurance and DEDUCT THE PREMIUM from the price due to the seller. Save contrary pact or usage, the bill of lading or consignment note is BORNE BY BOTH CONTRACTING PARTIES, but the RISKS are on the BUYER FROM RECEIPT OF THE MERCHANDISE BY THE CARRIER (risk-pass point) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1032-1033 pp.173-174 (EVID-227; txt PAGE 173-174) |
| LB-015 | Código de Comercio, Art. 1034: "Las mismas disposiciones se aplicarán a la compraventa con la cláusula 'costo, flete' (CF), menos lo que concierne al seguro." Art. 1035: "En la compraventa 'libre a bordo' (LAB o FOB), el vendedor fijará un precio que comprenderá todos los gastos hasta poner las cosas vendidas a bordo del buque o vehículo que haya de transportarlas, momento a partir del cual se transfiere el riesgo al comprador." | The same provisions apply to the sale with the clause "COSTO, FLETE" (cost and freight, CF), MINUS what concerns insurance. In the sale "LIBRE A BORDO" (free on board — LAB or FOB), the seller fixes a price comprising ALL EXPENSES UP TO PLACING the sold things ON BOARD the ship or vehicle that is to transport them — the moment FROM WHICH THE RISK TRANSFERS TO THE BUYER | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1034-1035 p.174 (EVID-227; txt PAGE 174) |
| LB-016 | Código de Comercio, Art. 1038: "Se denomina venta a plazos de bienes muebles, aquella en que se conviene que el dominio no será adquirido por el comprador, mientras no haya pagado la totalidad o parte del precio, o cumplido alguna condición." "Para gozar de los beneficios que otorga a los contratantes este Capítulo, será necesario inscribir el contrato en el Registro de Comercio, y que el valor del mismo contrato sea superior a un mil colones." | An INSTALLMENT SALE OF MOVABLE GOODS is that in which it is agreed that the DOMINIO (ownership) will NOT be acquired by the buyer while he has not paid the totality or part of the price, or fulfilled some condition (RESERVED DOMAIN). To enjoy the benefits this Chapter grants the contracting parties, it is necessary to INSCRIBE the contract in the Registro de Comercio AND that the value of the contract be superior to UN MIL COLONES [sic — unreformed 1970 colones text; SOQ-29 remnant, §2/OQ-001] | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1038 p.174 (EVID-227; txt PAGE 174) |
| LB-017 | Código de Comercio, Art. 1039: "El vendedor de objetos mobiliarios provistos de numeración u otros signos que los individualicen, o cualquier interesado, puede solicitar, dentro de los treinta días de la fecha del contrato, su inscripción en el Registro de Comercio." Art. 1040: "Los contratos inscritos y los pagarés o letras de cambio suscritos en relación con los mismos, serán negociables por el vendedor o sus causahabientes por simple endoso, una o más veces, aun después de iniciada la ejecución, pero antes de la terminación de ésta." Art. 1041: "Los contratos de venta a plazos de bienes muebles, sólo serán oponibles a terceros cuando hayan sido registrados de conformidad con este Capítulo, pudiendo entonces el propietario o sus causahabientes reivindicar las cosas vendidas que estuvieren en poder de terceros, en los mismos casos en que puedan reivindicarlos del comprador." "En los casos del inciso anterior, las enajenaciones y cargas reales consentidas por el comprador u obtenidas judicialmente, así como los embargos y secuestros hechos por deudas del comprador, cederán ante el derecho del propietario o de cualquiera de sus causahabientes." | The seller of movable objects PROVIDED WITH NUMBERING OR OTHER SIGNS THAT INDIVIDUALIZE them — or any interested party — may request their inscription in the Registro de Comercio WITHIN THE THIRTY DAYS of the contract date. Inscribed contracts and the pagarés or letras de cambio subscribed in relation to them are NEGOTIABLE by simple ENDOSO (endorsement), once or more times, even after execution has begun but before its termination. Installment-sale contracts are OPPOSABLE TO THIRD PARTIES ONLY when registered per this Chapter — the owner or his causahabientes may then REIVINDICATE (claim back) the sold things in third parties' power in the same cases as from the buyer; buyer-consented enajenaciones (alienations) and real charges, judicially obtained ones, and EMBARGOS AND SECUESTROS (attachments and seizures) for the buyer's debts YIELD before the owner's right | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1039-1041 p.175 (EVID-227; txt PAGE 175) |
| LB-018 | Código de Comercio, Art. 1042 (incisos 1 y 2): "Cuando el comprador haya dejado de pagar una cuota del precio o de cumplir otra condición a la cual esté subordinada la adquisición del dominio, en el término fijado, el propietario o sus causahabientes pueden hacerle notificar judicialmente intimación de efectuar el pago o cumplir la condición en término no menor de diez días, advirtiéndole que si no lo hiciere, la venta quedará resuelta de pleno derecho a la expiración de ese plazo, sin otra intervención judicial ni procedimiento alguno, pudiendo el propietario o sus causahabientes reivindicar la cosa vendida en cualesquiera manos en que se encuentre." "Cuando el propietario lo requiera, el Juez decretará secuestro preventivo de la cosa, desde el momento en que notifique al comprador la intimación a que se refiere el inciso anterior, dando constancia de ello en el mismo acto." Art. 1043 (inciso 1; inciso 2 omitido — alcance de la incautación sobre piezas y accesorios incorporados): "Transcurrido el plazo de la intimación hecha conforme al artículo anterior, sin que el comprador haya efectuado el pago o cumplido la condición, la venta queda resuelta de pleno derecho. El propietario puede entonces solicitar del Juez competente que dicte auto ordenando la incautación de la cosa en cualesquiera manos en que se encuentre. Este auto es ejecutorio no obstante apelación. Si la incautación afectare derechos de terceros, el Juez deberá oír a los afectados, por el término de tres días previamente a su ejecución." Art. 1044 omitido — entrega de la cosa reivindicada mediante recibo y restricciones de disposición del propietario mientras pende la apelación, autorización del Juez previa acta de solvencia para disponer de la cosa, y traspaso de la matrícula de vehículos de motor (inciso 3). Art. 1045 (incisos 3 y 4; incisos 1 y 2 omitidos — ajuste voluntario entre las partes y designación de peritos): "Ni el contrato, ni el acuerdo posterior de las partes relativo al ajuste ni el que practique el perito, puede imponer condiciones más onerosas para cualquiera de las partes, que las señaladas en el artículo 1026 de este Código." "Aquél que resulte deudor de saldo, está obligado a pagarlo en el término de diez días después de la notificación que se le haga a solicitud de la otra parte, con mandamientos de pago. La hoja de ajuste firmada por las partes o por los peritos, según el caso, y visada por el Juez, constituye título ejecutivo, para proceder al embargo de bienes del deudor." | When the buyer has failed to pay a CUOTA (installment) of the price or to fulfil another condition to which domain acquisition is subordinated, within the fixed term, the owner or his causahabientes may have him judicially notified an INTIMACIÓN (demand) to effect payment or fulfilment in a term NOT LESS THAN TEN DAYS, warning that failing which THE SALE REMAINS RESOLVED DE PLENO DERECHO (by full right) at that term's expiry, WITHOUT FURTHER JUDICIAL INTERVENTION OR PROCEDURE — the owner being able to reivindicate the sold thing in WHATEVER HANDS it is found. When the owner requires it, the Judge decrees PREVENTIVE SECUESTRO (sequestration) of the thing from the moment the intimación is notified, recording it in the same act. Art. 1043-I: with the intimación term expired without payment or fulfilment, THE SALE REMAINS RESOLVED DE PLENO DERECHO; the owner may then request the competent Judge for an auto ordering the INCAUTACIÓN (seizure) of the thing in whatever hands — ejecutorio (immediately enforceable) NOTWITHSTANDING APPEAL; if the seizure affects third-party rights, the Judge must hear the affected parties for THREE DAYS before execution. Art. 1045-III: neither the contract, nor the parties' later ajuste (settlement) agreement, nor the perito's, may impose conditions MORE ONEROUS than those of Art. 1026. IV: the SALDO (balance) debtor must pay it within TEN DAYS of notification; the ajuste sheet signed by the parties or peritos and VISADA (countersigned) BY THE JUDGE constitutes TÍTULO EJECUTIVO (execution title) to proceed against the debtor's goods | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1042-1043, 1045 pp.175-176 (EVID-227; txt PAGE 175-176) |
| LB-019 | Código de Comercio, Art. 1048: "Toda clase de derechos y acciones que genere el contrato, su negociabilidad o su ejecución, prescribirán a los tres meses de la terminación del plazo establecido en el inciso último del artículo 1045 y si no hubiere lugar a ese plazo, a partir de la incautación." Art. 1049: "En las ventas a que se refiere este Capítulo, los riesgos quedan a cargo del comprador desde el día de la venta." "Salvo convención contraria, los impuestos y el seguro sobre la cosa vendida deben ser pagados por el comprador." Art. 1050 (encabezamiento y ordinales I-V): "Sin perjuicio de lo que al respecto disponga el Código Penal, se considerarán vencidos los plazos cuando ocurra cualquiera de los acontecimientos siguientes: I.- El hecho de parte del comprador de vender o, en cualquier forma, enajenar o gravar la cosa, antes de haber adquirido el dominio y sin el consentimiento escrito del propietario. II.- El hecho de transportar o permitir que se transporte la cosa fuera del país, en las mismas circunstancias. III.- El hecho de destruir, deteriorar u ocultar la cosa en perjuicio del propietario. IV.- El de cambiar o hacer desaparecer los números u otras señales que individualicen la cosa. V.- El hecho de no entregar la cosa cuando le sea requerida en la forma prevista en el artículo 1043, salvo por causa de fuerza mayor." | EVERY class of rights and actions the contract, its negotiability or its execution generates PRESCRIBE IN THREE MONTHS from the termination of the term established in Art. 1045's final inciso — and, if there is no place for that term, FROM THE INCAUTACIÓN (special short prescription). In this Chapter's sales the RISKS are on the buyer FROM THE DAY OF THE SALE; save contrary convention, the TAXES AND INSURANCE on the sold thing must be PAID BY THE BUYER. Without prejudice to the Código Penal, the terms are considered VENCIDOS (accelerated/matured) when any of these events occurs: I. the buyer selling or in any form ENAJENING OR ENCUMBERING the thing before acquiring domain and WITHOUT THE OWNER'S WRITTEN CONSENT; II. transporting it or allowing its transport OUT OF THE COUNTRY in the same circumstances; III. DESTROYING, DETERIORATING OR HIDING the thing to the owner's prejudice; IV. CHANGING OR MAKING DISAPPEAR the numbers or other señales (marks) that individualize the thing; V. FAILING TO DELIVER the thing when required per Art. 1043, save fuerza mayor | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1048-1050 pp.176-177 (EVID-227; txt PAGE 176-177) |
| LB-020 | Código de Comercio, Art. 1051: "En virtud del contrato estimatorio o venta en consignación, una parte entrega a la otra cosas muebles, para que le pague su precio o le devuelva las mismas cosas o parte de ellas, dentro de un plazo. Se regirá por las siguientes reglas: I.- El consignatario está obligado a pagar el precio de lo recibido, cuando no devuelva las cosas, aun en el caso de que la devolución se vuelva imposible por causas que no le sean imputables. II.- El consignatario podrá disponer válidamente de las cosas, pero éstas no podrán ser embargadas por los acreedores de aquél mientras no haya pagado el precio. III.- El consignante no puede disponer de las cosas mientras no le sean restituídas." | By the CONTRATO ESTIMATORIO OR VENTA EN CONSIGNACIÓN (consignment sale), one party delivers to the other movable things so that he PAY THEIR PRICE or RETURN the same things or part of them, within a term. Governed by: I. the CONSIGNATARIO (consignee) is obliged to pay the price of what he received when he does not return the things — EVEN IF RETURN BECOMES IMPOSSIBLE through causes not imputable to him; II. the consignatario may VALIDLY DISPOSE of the things, but they CANNOT BE EMBARGOED (seized) BY HIS CREDITORS while the price is unpaid; III. the CONSIGNANTE (consignor) CANNOT DISPOSE of the things until they are restituted to him (ownership invariant) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1051 p.177 (EVID-227; txt PAGE 177) |
| LB-021 | Código de Comercio, Art. 1052: "La permuta es mercantil en los mismos casos que la compraventa." Art. 1053: "El permutante que sufra la evicción de lo que recibió, y no prefiera recuperar la cosa o el derecho que dio en cambio, podrá exigir al otro que le pague el valor de la cosa evicta, más la indemnización de los perjuicios que se le hayan causado. Para estimar el pago se tomará el valor de la cosa en el momento en que fue evicta." Art. 1054: "En todo lo no previsto en el presente Capítulo, las disposiciones relativas a la compraventa mercantil serán aplicables a la permuta mercantil, con las modificaciones que exija su naturaleza." | The PERMUTA (exchange/barter) is mercantile in the SAME CASES as the sale. A permutante suffering EVICCIÓN (eviction) of what he received — and not preferring to recover the thing or right he gave in exchange — may demand the other pay him the VALUE OF THE EVICTED THING plus indemnification of damages caused; to estimate the payment, the VALUE OF THE THING AT THE MOMENT IT WAS EVICTED is taken. In everything not foreseen, the mercantile-sale provisions apply to the mercantile permuta with the modifications its nature requires | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1052-1054 p.177 (EVID-227; txt PAGE 177) |
| LB-022 | Código de Comercio, Art. 1055: "Por el contrato de suministro, una parte se obliga, a cambio de un precio, a realizar en favor de la otra, prestaciones periódicas o continuadas." Art. 1056: "Si no se determinare la cuantía de las prestaciones, se entenderá convenida la que corresponda a las necesidades normales de la parte que las reciba, en la época de cumplir tales prestaciones." "Si se hubiere convenido un máximo y un mínimo para el suministro total o para las prestaciones aisladas, corresponderá al suministrado fijar su cuantía dentro de los límites pactados." "Si la cuantía del suministro debiere determinarse en razón de las necesidades del suministrado, éste tendrá derecho a las prestaciones necesarias, aun cuando superen el límite fijado." Art. 1057: "En el suministro de carácter periódico, si el precio debiere determinarse según las normas del artículo 1014, se tendrá en cuenta el vencimiento de las prestaciones aisladas y el lugar en que deban efectuarse." Art. 1058: "En el suministro de carácter periódico, el precio se pagará por cada prestación aislada y en proporción a su cuantía." "En los suministros de carácter continuado, el precio se pagará en los vencimientos pactados o en su defecto, en los usuales." | By the SUMINISTRO (supply) contract, one party obliges itself, in exchange for a price, to realize in favour of the other PERIODIC OR CONTINUED PRESTATIONS. If the quantity of the prestations is undetermined, the one corresponding to the NORMAL NEEDS of the receiving party at the time of performance is understood agreed. If a MAXIMUM and MINIMUM are agreed for the total supply or for isolated prestations, the SUMINISTRADO (supplied party) fixes the quantity within the pacted limits. If the quantity must be determined by the supplied party's needs, he is entitled to the NECESSARY PRESTATIONS EVEN THOUGH THEY EXCEED THE FIXED LIMIT. In periodic supply with price determined per Art. 1014, each isolated prestación's VENCIMIENTO (due date) and PLACE are taken into account. In periodic supply the price is paid PER ISOLATED PRESTACIÓN, in proportion to its quantity; in CONTINUED supplies, at the pacted vencimientos or, failing them, the usual ones | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1055-1058 p.178 (EVID-227; txt PAGE 178) |
| LB-023 | Código de Comercio, Art. 1059: "El plazo establecido para las prestaciones aisladas se entenderá pactado en interés de ambas partes." "Si el suministrado tiene facultad de fijar fecha para las prestaciones aisladas, deberá comunicarla al suministrante, con antelación suficiente." Art. 1060: "En caso de incumplimiento de una de las partes, en relación con las prestaciones aisladas, la otra podrá pedir la resolución del contrato, si el incumplimiento tiene tal importancia que sea capaz de afectar la confianza respecto al cumplimiento futuro." Art. 1061: "Si el suministrado incumpliere alguna de sus obligaciones, el suministrante no podrá suspender la ejecución del contrato sin darle aviso con quince días de antelación." | The term established for isolated prestations is understood pacted IN THE INTEREST OF BOTH PARTIES. If the supplied party may fix the date of isolated prestations, he must COMMUNICATE it to the supplier with SUFFICIENT ANTICIPATION. On one party's breach as to isolated prestations, the other may demand RESOLUTION of the contract if the breach is SO IMPORTANT as to be capable of AFFECTING CONFIDENCE in future performance. If the supplied party breaches any of his obligations, the supplier may NOT SUSPEND execution WITHOUT GIVING HIM NOTICE FIFTEEN DAYS IN ADVANCE | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1059-1061 p.178 (EVID-227; txt PAGE 178) |
| LB-024 | Código de Comercio, Art. 1062: "Si en un contrato de suministro se hubiere establecido la cláusula de exclusividad a favor del suministrante, el suministrado no podrá obtener prestaciones iguales de terceros; tampoco podrá proveer con medios propios, salvo pacto en contrario, a la producción de las cosas objeto del contrato." Art. 1063: "Si la cláusula de exclusividad se establece a favor del suministrado, el suministrante no podrá realizar, en la zona determinada y por la duración del contrato, directa ni indirectamente, prestaciones de las que constituyen el objeto del mismo." "El suministrado que asumiere la obligación de promover en la zona convenida la venta de las cosas, responderá del lucro cesante, aunque ya hubiere cumplido con la cuantía mínima fijada en el contrato." Art. 1064: "Si no se hubiere establecido la duración del suministro, cualquiera de las partes podrá denunciar el contrato, dando aviso a la otra con la anticipación pactada, o con la establecida por los usos o, en defecto de ambas, con tres meses de antelación." | If an EXCLUSIVITY clause is established in favour of the SUPPLIER, the supplied party may NOT obtain equal prestations from third parties, NOR self-provide — save contrary pact — the PRODUCTION of the things object of the contract. If the exclusivity clause favours the SUPPLIED party, the supplier may not — in the determined ZONE and for the contract's DURATION, directly or indirectly — perform prestations constituting its object. A supplied party who assumed the obligation to PROMOTE the sale of the things in the agreed zone answers for LUCRO CESANTE (lost profit), though he have already met the minimum quantity fixed in the contract. If the supply's DURATION is not established, either party may DENOUNCE (terminate on notice) the contract with the pacted anticipation, or that established by usages, or — failing both — WITH THREE MONTHS' NOTICE | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1062-1064 p.178 (EVID-227; txt PAGE 178) |
| LB-025 | Código de Comercio, Art. 1066: "Por el contrato de comisión, el comisionista desempeña en nombre propio pero por cuenta ajena, mandato para realizar actos de comercio. El comisionista actúa como agente intermediario, entre el comitente y los terceros." "Se presumirá aceptada una comisión cuando se confiera a persona que públicamente ostente el carácter de comisionista, por el solo hecho de que no la rehuse dentro de los ocho días siguientes a aquél en que recibió la propuesta respectiva." "Aunque el comisionista profesional rehuse la comisión que se le confiera, no estará dispensado de practicar las diligencias necesarias para la conservación de los efectos que el comitente le haya remitido, hasta que éste provea de nuevo encargado, sin que por ello se entienda tácitamente aceptada la comisión." Art. 1067: "Cuando sin causa legal dejare el comisionista de avisar que rehusa la comisión, o de cumplir la expresa o tácitamente aceptada, será responsable al comitente de los daños que le cause." Art. 1073: "El comisionista que tuviere en su poder efectos por cuenta ajena, responderá de ellos como depositario." Art. 1075: "Los comisionistas no pueden tener efectos de una misma especie pertenecientes a distintos dueños bajo una misma marca, sin distinguirlos por una contramarca que designe la propiedad de cada comitente." | By the COMISIÓN (commission) contract, the comisionista (commission agent) performs, IN HIS OWN NAME BUT FOR A FOREIGN ACCOUNT, a mandate to realize acts of commerce; he acts as intermediary agent between the comitente (principal) and third parties. A commission is PRESUMED ACCEPTED when conferred on a person who PUBLICLY OSTENSES the character of comisionista, by the mere fact that he does not REFUSE it within the EIGHT DAYS following that on which he received the proposal. Though the professional comisionista refuses the commission, he is not dispensed from the diligence necessary for the CONSERVATION of the effects the comitente remitted to him until the latter provides a new encargado (appointee) — without the commission being understood tacitly accepted thereby. Leaving — without legal cause — to give notice of refusal, or to fulfil the expressly or tacitly accepted commission, makes him responsible to the comitente for damages. The comisionista having effects for a foreign account in his power answers for them AS A DEPOSITARY. Comisionistas may not keep effects of the same species belonging to DIFFERENT OWNERS under ONE AND THE SAME MARCA (mark) without distinguishing them by a CONTRAMARCA (counter-mark) designating each comitente's ownership | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1066-1067, 1073, 1075 pp.179-180 (EVID-227; txt PAGE 179-180) |
| LB-026 | Código de Comercio, Art. 1076: "El comisionista no puede, sin autorización del comitente, prestar ni vender al crédito. Si lo hace, el comitente puede exigirle el pago al contado." Art. 1077: "Si el comisionista, con la debida autorización, vendiere al crédito, deberá avisarlo al comitente, participándole los nombres de los compradores, y si no lo hace, se entenderá respecto al comitente que las ventas fueron al contado." Art. 1078: "El comisionista que no verificare oportunamente la cobranza de los créditos, será responsable de los perjuicios que causare su omisión o tardanza." | The comisionista CANNOT, without the comitente's authorization, LEND OR SELL ON CREDIT; if he does it, the comitente may DEMAND CASH PAYMENT (al contado) from him. Selling on credit with due authorization, he must give notice to the comitente REPORTING THE NAMES OF THE BUYERS — failing which the sales are understood, as regards the comitente, TO HAVE BEEN FOR CASH. The comisionista not timely effecting the COBRANZA (collection) of credits is responsible for the damages his omission or tardiness causes | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1076-1078 p.180 (EVID-227; txt PAGE 180) |
| LB-027 | Código de Comercio, Art. 1079: "En caso de no existir estipulación previa, el monto de la remuneración del comisionista se regulará por el uso de la plaza donde se realice la comisión." Art. 1080: "El comitente está obligado a satisfacer al contado al comisionista, mediante cuenta justificada, el importe de todos sus gastos y desembolsos, con el interés comercial desde el día en que los hubiere hecho." Art. 1081: "Los efectos que estén en poder del comisionista, se entenderán preferentemente afectados al pago de los derechos de comisión, anticipos y gastos hechos a causa del encargo, a cuyo efecto tendrá derecho de retención en garantía del pago." "Cuando las mercaderías sean entregadas al comprador sin intervención de comisionista, éste deberá presentar su cuenta documentada a quien deba hacer el pago. En este caso, ni el comprador ni la institución bancaria que reciba el valor de las mercaderías, podrá entregar el precio al comitente, sin retener el valor de la comisión respectiva y ponerlo a disposición del comisionista. La falta de cumplimiento de esta disposición, hará al contraventor responsable frente al comisionista." Art. 1082: "Por muerte o inhabilitación del comisionista se resuelve el contrato de comisión; por muerte o inhabilitación del comitente no se resolverá, aunque pueden revocarlo sus herederos o representantes." | Absent prior stipulation, the comisionista's remuneration is regulated by the USO DE LA PLAZA (usage of the market) where the commission is realized. The comitente is obliged to satisfy the comisionista IN CASH, against a JUSTIFIED ACCOUNT, the amount of all his gastos and desembolsos (expenses and disbursements), WITH COMMERCIAL INTEREST from the day he made them. The effects in the comisionista's power are understood PREFERENTLY AFFECTED to payment of commission rights, anticipos and expenses made on account of the encargo — for which he has a RETENTION RIGHT IN GUARANTEE of payment. When the merchandise is delivered to the buyer WITHOUT the comisionista's intervention, he must present his documented account to whoever must pay: in that case NEITHER THE BUYER NOR THE BANKING INSTITUTION receiving the merchandise's value may deliver the price to the comitente WITHOUT RETAINING the respective commission's value and placing it at the comisionista's disposal — breach makes the contravener responsible to the comisionista (commission withholding). The comisionista's DEATH OR INHABILITATION RESOLVES the commission contract; the comitente's does NOT, though his herederos or representatives may revoke it | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1079-1082 pp.180-181 (EVID-227; txt PAGE 180-181) |
| LB-028 | Código de Comercio, Art. 1083: "Por el mandato mercantil, el mandatario se encarga de practicar actos de comercio por cuenta y a nombre del mandante." Art. 1086 (inciso 1; incisos 2 y 3 omitidos — depósito judicial de mercaderías y venta de las no conservables, e indemnización de daños y perjuicios por el incumplimiento): "El comerciante que rehusare el mandato mercantil deberá comunicar su negativa al mandante en el plazo de ocho días, pero queda obligado a practicar las diligencias indispensables para la conservación de las mercaderías que le hayan sido remitidas, hasta que el mandante provea lo conveniente." Art. 1092: "El mandatario está obligado a dar aviso, sin demora, de la ejecución del mandato al mandante, y cuando éste no responda inmediatamente, se presumirá ratificado el negocio, aunque el mandatario se haya excedido de los términos del mandato." Art. 1094: "El mandatario deberá exhibir el mandato escrito a los terceros con quienes contrate; no podrá oponerles las instrucciones que hubiese recibido por separado del mandante, salvo si probare que tenían conocimiento de ellas al contratar." | By the MANDATO MERCANTIL (commercial mandate), the mandatario (mandatory/attorney-in-fact) takes charge of practicing acts of commerce FOR ACCOUNT AND IN THE NAME OF the mandante (principal). The merchant REFUSING the mandate must communicate his refusal to the mandante WITHIN EIGHT DAYS, but remains obliged to practice the indispensable diligence for the CONSERVATION of the merchandise remitted to him until the mandante provides what is convenient. The mandatario is obliged to give the mandante notice, WITHOUT DELAY, of the mandate's EXECUTION — and when the latter does not respond IMMEDIATELY, the business is PRESUMED RATIFIED, though the mandatario have EXCEEDED the mandate's terms (silence-ratification). The mandatario must EXHIBIT THE WRITTEN MANDATE to the third parties he contracts with; he cannot oppose to them the instructions received SEPARATELY from the mandante, save if he proves they knew them when contracting | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1083, 1086, 1092, 1094 pp.181-182 (EVID-227; txt PAGE 181-182) |

## 3. Functional Requirements

### 3.1 Mercantile-sale scope, price and the signed pedido (Arts. 1013-1015, 1020)

- **SV-CML-FR-165:** The system shall classify every sale against the
  Art. 1013 scope: mercantile when realized within the normal
  exploitation giro of an empresa mercantil or over cosas mercantiles;
  NOT mercantile when falling in the statutory carve-outs — sales by
  *agricultores o ganaderos* (farmers/livestock raisers) of their
  harvest fruits/products, livestock or the species given them in
  payment, WHEN they keep no *almacén o tienda* (store or shop) for
  their expendio, and artisans' sales in their *talleres* of the
  objects fabricated there — stamping an informational
  mercantile-scope classification on the customer/sale record used
  for customer and invoice classification notes (the carve-out keeps
  such direct sales outside the CC merchant layer; tax and DTE
  treatment is owned by the tax/e-invoicing waves and is NOT altered
  by this flag). (LB-001; EVID-227)
- **SV-CML-FR-166:** The system shall implement the Art. 1014 price
  determination defaults: a price referencing the figure fixed or to
  be fixed at a bolsa or market, national or foreign, on a FIXED DATE
  is determined (dated-reference price basis recorded); where the
  contract concerns things habitually sold by the seller with no
  agreed price or determination mode, the seller's NORMALLY REQUIRED
  price is presumed — save things bearing a market/bolsa price, where
  the presumption is the price at those establishments ON THE DELIVERY
  DAY (delivery-day price lookup slot); and *arras*, *anticipos* and
  quantities delivered as sign of the contract shall ALWAYS be
  allocated TO THE ACCOUNT OF THE PRICE (down payments reduce the
  price balance; no forfeiture semantics by default).
  (LB-002; EVID-227)
- **SV-CML-FR-167:** The system shall implement the Art. 1015
  signed-pedido binding: a pedido de mercaderías signed by the buyer
  himself, a representative or an authorized dependiente (authority
  defaults owned by `06_commercial-agents.md`, consumed by id) creates
  the obligation to TAKE the merchandise at the pedido's expressed
  conditions — a pedido-binding state on the order record — and shall
  surface the seller's remedy exposure: acción en juicio sumario to
  consign the merchandise to the buyer's order and simultaneously
  demand the price plus indemnification of delay damages
  (informational; kin — agent-side pedido acceptance — is
  SV-CML-FR-114, never restated here). (LB-003; EVID-227)
- **SV-CML-FR-168:** The system shall resolve the Art. 1020
  delivery-place default on every sale lacking an express contrary
  pact: delivery at the SELLER'S ESTABLISHMENT or, if he has none, at
  his DOMICILIO — recorded as the defaulted delivery point with its
  provenance flagged (establishment/domicilio resolution feeding the
  delivery/warehouse surface). (LB-004; EVID-227)

### 3.2 Defect and warranty clocks, tracked at lot level (Arts. 1019-1021)

- **SV-CML-FR-169:** The system shall track, at LOT level, the
  Art. 1019 apparent/packaged-defect regime: a buyer who examines the
  things at receipt TO HIS SATISFACTION has NO action for APPARENT
  quality or quantity defects (examination event stamps the waiver on
  the lot); for things received ENFARDADAS O EMBALADAS (packed or
  packaged), the repetition right must be exercised within the EIGHT
  DAYS FOLLOWING RECEIPT (computed with the shared day-count
  conventions, SV-CML-FR-145 by id) and does not proceed where the
  avería stems from caso fortuito, vicio propio of the things or
  fraud of a third party (exclusion flags); and the seller may demand
  at the delivery act that the recognition be made to the buyer's
  satisfaction (delivery-act recognition event recorded).
  (LB-005; EVID-227)
- **SV-CML-FR-170:** The system shall track, at lot level, the
  Art. 1019 hidden-vices clock: OCULTO (hidden) vices must be
  denounced within the FIFTEEN DAYS FOLLOWING DISCOVERY (or the
  parties' agreed term — agreed-term override slot), the denounce
  being proved by ACTA ANTE NOTARIO (a notarial-instrument reference
  required on the denounce event); a timely-and-formal denounce opens
  the Código Civil recursos (surface only); and the resulting actions
  PRESCRIBE IN ONE YEAR FROM DELIVERY — the delivery date is the
  prescription anchor, registered on the vicios row of the
  prescription matrix consumed via SV-CML-FR-160 by id (anchor owned
  here; matrix terms never restated). (LB-005; EVID-227)
- **SV-CML-FR-171:** The system shall track, at lot level, the
  Art. 1021 functioning-warranty clocks: where the seller guarantees
  the functioning of the thing sold FOR A DETERMINED TIME, the buyer
  must denounce functioning defects WITHIN THE THIRTY DAYS OF
  DISCOVERY UNDER PENALTY OF CADUCIDAD (caducidad regime consumed via
  SV-CML-FR-162 by id: no suspension save fuerza mayor; no party
  modification), the denounce again proved by acta ante Notario; the
  action PRESCRIBES IN SIX MONTHS FROM THE DENOUNCE DATE; the Judge
  may fix a substitution/repair term with damages (informational
  legal note); and a warranty WITHOUT determined term runs FOR THREE
  YEARS (3y no-term default stamped when the seller guarantees
  functioning without fixing a term). (LB-006; EVID-227)

### 3.3 Gusto, a prueba and muestras: perfection (Arts. 1022-1024)

- **SV-CML-FR-172:** The system shall model the Art. 1022-1023
  perfection regimes: for things CUSTOMARILY GUSTADAS (tasted/tried),
  the contract is perfected when the decision is COMMUNICATED to the
  seller; where the examination must occur at the seller's
  establishment, the contract is perfected if the buyer does NOT
  proceed to examine within the contract term, the usage term or —
  failing both — the seller's own convenient term (exam-deadline
  clock with its three-tier source ladder); and where the thing is
  already in the buyer's power, THE SILENCE CONSTITUTES APPROVAL once
  the indicated term lapses (state machine: offered →
  decided/term-lapsed → perfected); a sale A PRUEBA is presumed made
  under the SUSPENSIVE CONDITION that the thing has the qualities
  necessary for its destined use, the test to be realized in the
  agreed or usage term and form (conditioned-sale flag blocking
  property-settlement semantics until the condition resolves).
  (LB-007; EVID-227)
- **SV-CML-FR-173:** The system shall implement the Art. 1024
  sample-sale rules: in sales over MUESTRAS or known qualities, the
  object is determined by reference to the sample or quality (sample
  reference on the order line); and property transmission REQUIRES
  the INDIVIDUALIZATION of the thing — effected by buyer-seller
  agreement, or exclusively by the seller where convenio or usage so
  allows — so the property-transfer step on sample sales carries an
  individualization event (lot/serial designation) with its author
  (agreement vs seller-alone) recorded. (LB-008; EVID-227)

### 3.4 Installment resolution and restitution (Arts. 1025-1026)

- **SV-CML-FR-174:** The system shall implement the Art. 1025
  resolutoria-clause opposability: where the parties pact that
  non-payment of one or several ABONOS resolves the sale, the
  resolution's effects against THIRD-PARTY ACQUIRERS depend on the
  goods — for goods IDENTIFIABLE INDUBITABLY (automobiles, motors and
  the like, incl. per-lot identification per FR-173), resolution is
  effective against third-party acquirers when the resolutoria clause
  has been INSCRIBED in the Registro de Comercio (or Propiedad Raíz
  for real property); for muebles NOT so identifiable, resolution has
  NO effects against good-faith third-party acquirers (identifiability
  + inscription state gate the third-party-effect stamp; registry
  entries recorded through the registry-entry model of
  SV-CML-FR-013/016 by id, never re-created here).
  (LB-009; EVID-227)
- **SV-CML-FR-175:** The system shall implement the Art. 1026
  restitution matrix on every resolution under FR-174 and under the
  venta a plazos FR-182: mutual RESTITUTION of prestations; the seller
  may demand indemnification for the USE made of the thing and its
  DETERIORATION (both fixed by peritos — perito-fixed value slots, no
  system-invented amounts); the part-paying buyer is entitled to the
  LEGAL INTEREST on the quantity delivered (rate consumed via
  SV-CML-FR-158 by id); a pact imposing MORE ONEROUS conditions on
  either party is NULL (validation warning on the contract's
  resolution terms); and the rules apply to EVERY price-deferral form,
  including arrendamiento con promesa de venta and analogous forms
  (form-agnostic application flag). (LB-010; EVID-227)

### 3.5 Documents over goods (Arts. 1027-1029)

- **SV-CML-FR-176:** The system shall implement the Art. 1027
  documents-over-goods delivery: where the sale is OVER DOCUMENTS, the
  seller performs delivery by REMITTING the título representativo de
  las mercancías and the other contract- or custom-required documents
  (document-checklist delivery semantics); save contrary pact, the
  price is payable AT THE MOMENT the documents are delivered
  (pay-at-documents default on the invoice/payment term); and the
  buyer cannot refuse payment alleging quality/state defects of the
  things UNLESS he presents PROOFS of such defects (evidence-gate on
  payment refusal). (LB-011; EVID-227)
- **SV-CML-FR-177:** The system shall record the Art. 1028 transit
  risk rule: where the things are EN CURSO DE RUTA and the delivered
  documents include the transport-risk insurance policy, the risks are
  on the BUYER from the moment of DELIVERY OF THE MERCHANDISE TO THE
  CARRIER — save the seller's known-and-concealed loss/avería
  exception (concealment exception flag anchored at contract time);
  and shall carry the Art. 1029 clause labels D/a (documentos contra
  aceptación) and D/P (documentos contra pago) as recognized
  documents-against clauses routing to Art. 712 (bank-operations
  mechanics outside this file — pointer only, §3.13/OQ-002).
  (LB-012; EVID-227)

### 3.6 In-code INCOTERM-analog clauses (Arts. 1030-1035)

- **SV-CML-FR-178:** The system shall encode the Art. 1030-1033
  CSF/CIF/CAF cluster: the price comprises the thing's value plus the
  insurance PRIMAS and the FREIGHTS up to the agreed reception place;
  the seller is understood obliged to (I) contract the carriage on
  the agreed terms, pay the flete and obtain the conocimiento de
  embarque or carta de porte, (II) take insurance for the TOTAL VALUE
  of the thing sold in favour of the buyer or his designee covering
  the agreed or usual risks and obtain the póliza/certificado, and
  (III) deliver those documents (three-obligation checklist on the
  sale); the sanction: a CSF seller not contracting the insurance
  ANSWERS AS THE INSURER WOULD HAVE in case of siniestro, while the
  buyer may contract the insurance and DEDUCT the prima from the price
  due (deduction path); and the risk-pass: save contrary pact or
  usage, conocimiento/carta costs are shared by both parties but the
  RISKS are on the buyer FROM RECEIPT OF THE MERCHANDISE BY THE
  CARRIER (risk-pass event = carrier receipt).
  (LB-013; LB-014; EVID-227)
- **SV-CML-FR-179:** The system shall encode the Art. 1034-1035 CF
  and LAB/FOB clauses with their risk-pass points: CF (costo y
  flete) carries the SAME CSF dispositions MINUS the insurance
  obligation and its sanction; LAB/FOB (libre a bordo) — the seller's
  price comprises ALL EXPENSES up to placing the sold things ON BOARD
  the ship or vehicle that is to transport them, the moment FROM
  WHICH THE RISK TRANSFERS TO THE BUYER (risk-pass event = on board) —
  and shall keep these CC clause labels, price compositions and
  risk-pass events as an in-code clause catalog on the sale; the
  export e-invoicing INCOTERM capture is OWNED by the e-invoicing wave
  (SV-EINV-FR-045 by id — INCOTERMS CAT-031 required when
  exportación = 1, `sv/requirements/e-invoicing/01_document-types.md`
  §3.10) and the system shall NOT auto-translate CC labels to or from
  Incoterms codes (OQ-003). (LB-015; EVID-227)

### 3.7 Venta a plazos de bienes muebles: reserved domain (Arts. 1038-1050)

- **SV-CML-FR-180:** The system shall model the Art. 1038 venta a
  plazos: a sale of movable goods in which the DOMINIO is NOT
  acquired by the buyer until the totality or part of the price is
  paid or a condition fulfilled (RESERVED-DOMAIN ownership state on
  the contract/goods — property transfer gated on full payment or the
  condition); the Chapter's benefits apply only where the contract is
  INSCRIBED in the Registro de Comercio (registry-entry link via
  SV-CML-FR-013 by id) AND the contract value exceeds the statutory
  threshold — the "UN MIL COLONES" [sic] figure is an unreformed
  colones-era remnant recorded as historical text under SOQ-29 and
  shipped as a FLAGGED configuration slot with NO default (OQ-001:
  the operative USD threshold is unset until a conversion rule is
  evidenced; the flag never blocks recording, only the
  chapter-benefit stamp). (LB-016; EVID-227)
- **SV-CML-FR-181:** The system shall implement the Arts. 1039-1041
  registration mechanics: for numbered objects or objects otherwise
  INDIVIDUALIZED by signs, the seller or any interested party may
  request inscription WITHIN THE THIRTY DAYS of the contract date
  (inscription-window clock with lapsed-warning); INSCRIBED contracts
  and their related pagarés/letras are negotiable by SIMPLE ENDOSO,
  once or more times, even after execution begins but before it
  terminates (endoso-negotiability state riding the payment
  instruments of `08_payment-instruments.md` by pointer); and only
  REGISTERED contracts are OPPOSABLE to third parties — enabling
  reivindicación of the sold things from third parties as from the
  buyer, with buyer-consented enajenaciones/cargas and judicial or
  creditor EMBARGOS/SECUESTROS for the buyer's debts YIELDING before
  the owner's right (priority informational stamp on the
  reserved-domain goods). (LB-017; EVID-227)
- **SV-CML-FR-182:** The system shall implement the Arts. 1042-1045
  resolution process: on a missed CUOTA or unfulfilled condition, the
  owner may have the buyer judicially notified an INTIMACIÓN with a
  term NOT LESS THAN TEN DAYS warning that the sale RESOLVES DE PLENO
  DERECHO at term expiry without further judicial intervention —
  tracked as an intimation state machine (notified → term running →
  paid/cured → resolved-de-pleno-derecho), with the preventive
  SECUESTRO available from intimation notice and the post-expiry
  INCAUTACIÓN auto (ejecutorio notwithstanding appeal; third parties
  heard 3 days) recorded as legal-event surfaces; the AJUSTE DE
  CUENTAS is subject to the Art. 1026 CAP (no more-onerous conditions
  — FR-175 validation applies), the SALDO debtor pays within TEN DAYS
  of notification, and the signed judge-visada hoja de ajuste is
  stamped TÍTULO EJECUTIVO (execution-title metadata).
  (LB-018; EVID-227)
- **SV-CML-FR-183:** The system shall implement the Arts. 1048-1050
  closing rules: every class of rights and actions generated by the
  contract, its negotiability or its execution PRESCRIBES IN THREE
  MONTHS from the termination of the Art. 1045 ten-day saldo term —
  or, failing that term, FROM THE INCAUTACIÓN (special short term
  registered as a code-internal override row on the prescription
  matrix consumed via SV-CML-FR-160 by id, anchored here); the RISKS
  are on the buyer FROM THE DAY OF THE SALE and — save contrary
  convention — the TAXES AND INSURANCE on the sold thing are PAID BY
  THE BUYER (default allocation flags); and the terms are considered
  VENCIDOS (acceleration listeners) on any of the five Art. 1050
  events: enajening or encumbering the thing before acquiring domain
  without the owner's WRITTEN consent; transporting it out of the
  country in the same circumstances; destroying, deteriorating or
  hiding it to the owner's prejudice; changing or removing the
  individualizing numbers/marks; or failing to deliver it when
  required per Art. 1043 save fuerza mayor.
  (LB-019; EVID-227)

### 3.8 Contrato estimatorio: consignment (Art. 1051)

- **SV-CML-FR-184:** The system shall model the Art. 1051 contrato
  estimatorio / venta en consignación with its ownership invariant:
  one party delivers muebles to the other to PAY THE PRICE or RETURN
  the same things (or part) within a term; (I) the CONSIGNATARIO must
  pay the price of whatever is not returned, EVEN IF return becomes
  impossible through non-imputable causes (price-or-return settlement
  with no destruction excuse); (II) the consignatario may VALIDLY
  DISPOSE of the things, but they are NOT EMBARGABLE BY THE
  CONSIGNATARIO'S CREDITORS while the price is unpaid (informational
  seizure-protection stamp); (III) the CONSIGNANTE CANNOT DISPOSE of
  the things until they are restituted (disposal block) — implemented
  as a consignment stock location whose quants retain the consignante
  as owner (ownership invariant: ownership neither passes to the
  consignatario on delivery nor returns to availability for the
  consignante until restitution), with the consignatario's valid
  disposal triggering the price-or-return settlement.
  (LB-020; EVID-227)

### 3.9 Permuta (Arts. 1052-1054)

- **SV-CML-FR-185:** The system shall recognize the Art. 1052-1054
  permuta: mercantile in the SAME CASES as the compraventa
  (classification reuses the FR-165 scope engine) and, in everything
  not foreseen, governed by this file's mercantile-sale rules with
  nature-driven modifications (inheritance flag); the Art. 1053
  evicción remedy shall be surfaced: a permutante suffering EVICCIÓN
  of what he received elects between recovering the thing or right he
  gave in exchange, or demanding from the other the VALUE OF THE
  EVICTED THING AT THE MOMENT OF EVICTION plus damages (election +
  eviction-day value basis recorded — never a current-value
  recomputation). (LB-021; EVID-227)

### 3.10 Suministro: periodic and continued supply (Arts. 1055-1065)

- **SV-CML-FR-186:** The system shall model the Arts. 1055-1058
  suministro: one party obliges itself, for a price, to realize
  PERIODIC or CONTINUED prestations in favour of the other (supply
  cadence: periodic-isolated vs continued); quantity determination —
  undetermined: the NORMAL NEEDS of the receiving party at performance
  time; with agreed MAXIMUM and MINIMUM (total or per-prestación): the
  SUMINISTRADO fixes the quantity within the limits (call-off rights);
  needs-based: entitled to the necessary prestations EVEN EXCEEDING
  the fixed limit (over-max need right); periodic price determination
  per Art. 1014 takes each prestación's VENCIMIENTO and PLACE into
  account (FR-166 consumed by id); and payment cadence — periodic:
  price paid PER ISOLATED PRESTACIÓN proportional to its quantity
  (invoice-per-prestación); continued: at the pacted vencimientos or,
  failing them, the USUAL ones. (LB-022; EVID-227)
- **SV-CML-FR-187:** The system shall implement the Arts. 1059-1061
  suministro execution rules: the term for isolated prestations is
  pacted IN THE INTEREST OF BOTH PARTIES (no unilateral-default
  reading); a supplied party fixing prestación dates must communicate
  them with SUFFICIENT ANTICIPATION (date-call notice tracking); on
  one party's breach as to isolated prestations, the other may demand
  RESOLUTION where the breach is important enough to affect CONFIDENCE
  in future performance (trust-based resolution surface — materiality
  flag, judicially appreciable, informational); and the supplier may
  NOT suspend execution for the supplied party's breach WITHOUT
  FIFTEEN DAYS' PRIOR NOTICE (suspension-notice clock).
  (LB-023; EVID-227)
- **SV-CML-FR-188:** The system shall implement the Arts. 1062-1064
  exclusivity and denounce: exclusivity in favour of the SUMINISTRANTE
  — the supplied party may not obtain equal prestations from third
  parties nor self-provide the PRODUCTION of the contracted things
  (save contrary pact); exclusivity in favour of the SUMINISTRADO —
  the supplier may not, directly or indirectly, perform the object
  prestations in the determined ZONE for the contract's DURATION
  (zone + duration fields on the exclusivity flag, both directions);
  a supplied party who assumed the obligation to PROMOTE sales in the
  zone answers for LUCRO CESANTE even after meeting the minimum
  quantity (exposure note); and where the supply's DURATION is not
  established, either party may DENOUNCE the contract with the pacted
  or usage anticipation or — failing both — with THREE MONTHS' NOTICE
  (denounce clock on no-duration supplies).
  (LB-024; EVID-227)

### 3.11 Comisión: own name, foreign account (Arts. 1066-1082)

- **SV-CML-FR-189:** The system shall model the Arts. 1066-1067,
  1073, 1075 comisión: the COMISIONISTA performs acts of commerce IN
  HIS OWN NAME BUT FOR THE FOREIGN ACCOUNT of the comitente,
  intermediating between comitente and third parties (representation
  mode distinct both from the agentes of file 06 and from the
  mandato's name-and-account mode — the name/account matrix stamped
  on the intermediary record); a commission conferred on a person who
  PUBLICLY OSTENSES the comisionista character is PRESUMED ACCEPTED
  unless refused within the EIGHT DAYS following receipt of the
  proposal (silence-acceptance clock); even a REFUSING professional
  comisionista must perform the CONSERVATION diligences on remitted
  effects until a new encargado is provided — without tacit
  acceptance (post-refusal custody state); unjustified failure to
  refuse-notice or to perform makes him liable for damages
  (responsibility stamp); effects held for a foreign account are
  answered for AS A DEPOSITARY (custody semantics); and same-species
  effects of DIFFERENT OWNERS may not share one MARCA without a
  CONTRAMARCA designating each comitente's ownership (ownership
  segregation on commission lots — kin of the FR-184 invariant).
  (LB-025; EVID-227)
- **SV-CML-FR-190:** The system shall enforce the Arts. 1076-1078
  comisión credit discipline: a comisionista CANNOT lend or sell AL
  CRÉDITO (on credit) without the comitente's AUTHORIZATION — a credit
  sale recorded without the authorization flag lets the comitente
  DEMAND CASH PAYMENT (the settlement flips demandable-to-cash with
  the flip reason recorded); WITH due authorization, credit sales must
  be reported to the comitente NAMING THE BUYERS — an unreported
  authorized credit sale is deemed, vis-à-vis the comitente, A CASH
  SALE (deemed-contado stamp with the named-buyer reporting
  checklist); and untimely COBRANZA of credits engages the
  comisionista's responsibility for omission/tardiness damages
  (collection-diligence tracking on commission receivables).
  (LB-026; EVID-227)
- **SV-CML-FR-191:** The system shall implement the Arts. 1079-1082
  comisión settlement: remuneration absent stipulation is regulated
  by the USO DE LA PLAZA where the commission is realized (config
  slot, NO shipped default — OQ-004); the comitente must satisfy IN
  CASH, against a justified cuenta, all gastos and desembolsos WITH
  COMMERCIAL INTEREST from the day made (reimbursement surface); the
  effects in the comisionista's power are PREFERENTLY AFFECTED to
  commission, anticipos and expenses — a RETENTION RIGHT in guarantee
  of payment (retention lien on held goods); where merchandise is
  delivered to the buyer WITHOUT the comisionista's intervention, the
  buyer or the banking institution receiving the value may NOT hand
  the price to the comitente WITHOUT RETAINING the commission's value
  and placing it at the comisionista's disposal — contravention makes
  the payer responsible (commission-withholding gate on commission
  settlements); and lifecycle — the comisionista's DEATH or
  INHABILIDAD RESOLVES the contract, the comitente's does NOT (his
  herederos/representatives may revoke) (resolution/revocability
  states). (LB-027; EVID-227)

### 3.12 Mandato mercantil: account and name (Arts. 1083-1097)

- **SV-CML-FR-192:** The system shall model the Arts. 1083, 1086,
  1092, 1094 mandato mercantil: the MANDATARIO practices acts of
  commerce FOR ACCOUNT AND IN THE NAME of the mandante (the
  name-and-account mode completing the intermediary matrix of
  FR-189); a merchant REFUSING the mandate must communicate the
  refusal to the mandante WITHIN EIGHT DAYS while remaining obliged
  to the indispensable CONSERVATION diligences on remitted
  merchandise until the mandante provides (8-day refusal clock +
  custody state); the EXECUTION NOTICE discipline — the mandatario
  must give the mandante notice WITHOUT DELAY of the mandate's
  execution, and a mandante not responding IMMEDIATELY triggers the
  PRESUMPTION OF RATIFICATION of the business, THOUGH THE MANDATARIO
  HAVE EXCEEDED the mandate's terms (silence-ratification stamp with
  the exceeded-terms note); and the mandatario must EXHIBIT THE
  WRITTEN MANDATE to the third parties he contracts with, being
  unable to oppose separately-received instructions unless their
  knowledge is proven (written-mandate reference on his third-party
  dealings). The Art. 1088 fire-insurance custody duty, the Art. 1093
  interest-on-delayed-funds rule and the Art. 1097 preference ranking
  are recorded as legal-note surfaces in §4.
  (LB-028; EVID-227)

### 3.13 Scope notes: Arts. 1016-1018, 712, 1036-1037 — no FRs

Five boundaries of this file's article set are recorded as scope, not
requirements: (i) Arts. 1016-1018 (seller's duty to deliver the
documents assuring the thing's goce; essential-term mora presuming the
buyer's renunciation of delivery; the good-faith purchaser's protection
from open establishments) are litigation-level defaults whose Odoo
surface is the delivery-checklist of FR-176/FR-178 and the
establishment model of FR-168 — no separate FR; (ii) Art. 712 — the
destination of the Art. 1029 D/a and D/P clauses — sits in the
bank-operations zone skimmed in the evidence (OQ-002); (iii) Art. 1036
(installment sales of títulos valores: interests, voto, exhibiciones)
rides the securities register of `08_payment-instruments.md` and is not
mechanized here; (iv) Art. 1037 (empresas lotificadoras) concerns real-
estate subdividers outside the sales-flows this file mechanizes; (v)
Art. 1065's compatibility clause routes suministro to the rules of the
contracts its isolated prestations correspond to — the inheritance
handled by FR-185's flag and the supply templates of §4.

## 4. Data Model

Layer semantics: this file's surfaces live on Odoo-native sale,
subscription, stock and partner objects plus l10n_sv_commerce
registers — wave default `odoo` (§5). External authorities (Notario
for the actas, Registro de Comercio for inscriptions, Juez for
intimación/sequestro/incautación autos, peritos for ajuste values,
bolsa/mercado for reference prices) are tracked as referenced dated
facts; the system never emulates them. Day-count and prescription
arithmetic are consumed from SV-FREP-FR-202..204 and SV-CML-FR-160 by
id. SOQ discipline: the Art. 1038 colones threshold ships as a
FLAGGED config slot with NO default (SOQ-29/OQ-001); the Art. 1079
commission rate ships as a config slot with NO default (OQ-004);
perito-fixed values are recorded, never computed.

**Sale scope, price and pedido:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| sale.order | sv_cml_mercantile_scope | computed select | mercantile_giro · mercantile_cosa · no_mercantile_farmer (no almacén/tienda) · no_mercantile_artisan (taller) | FR-165 |
| res.partner | sv_cml_direct_seller_profile | select | none · farmer_no_store · artisan_workshop | FR-165 |
| sale.order | sv_cml_price_basis | select | agreed · bolsa_mercado_fixed_date · habitual_seller_normal (delivery-day override when market-priced) | FR-166 |
| sale.order | sv_cml_arras_allocation | computed | arras/anticipos always credited to the price; balance after application | FR-166 |
| sale.order | sv_cml_pedido_binding_state · sv_cml_pedido_signed_by | select · m2o | draft · signed_binding (sumario-consignación + price + damages exposure note); signer = buyer/representative/authorized dependiente (authority per file 06) | FR-167 |
| sale.order | sv_cml_delivery_place_default | computed | seller establishment → seller domicilio (defaulted provenance flagged; express pact overrides) | FR-168 |

**Lot-level warranty clocks (Arts. 1019-1021):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| stock.lot + l10n_sv_commerce.warranty.clock | apparent_examined_on · exam_waiver | datetime · computed | satisfactory examination at receipt → NO action for apparent quality/quantity defects | FR-169 |
| stock.lot | packaged_claim_until · damage_exclusion | computed date · select | 8 days following receipt (SV-CML-FR-145 conventions by id); exclusions: caso_fortuito · vicio_propio · fraude_tercero | FR-169 |
| stock.lot | delivery_recognition_demanded | boolean | seller may demand recognition at the delivery act | FR-169 |
| stock.lot | hidden_vice_denounce_until · denounce_acta_ref · agreed_term_override | computed date · document ref · int/char | 15 days from discovery or agreed term; acta notarial reference REQUIRED | FR-170 |
| stock.lot | vicios_prescription_anchor | computed date | 1y from delivery — anchor registered on the SV-CML-FR-160 vicios row by id | FR-170 |
| stock.lot | warranty_term_stated · warranty_term · functioning_denounce_until · denounce_acta_ref (fn) | boolean · duration · computed date · ref | 30d-from-discovery denounce under caducidad (SV-CML-FR-162 regime by id); unstated term → 3y default | FR-171 |
| stock.lot | functioning_action_until | computed date | 6 months from the denounce date | FR-171 |

**Perfection, resolution and delivery clauses:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| sale.order | sv_cml_perfection_mode · sv_cml_exam_deadline_source · sv_cml_silence_approval_on | select · select · computed date | communicated_decision · exam_at_establishment (contract/uso/seller-term ladder) · silence_after_term (= approval); a_prueba suspensive-condition flag | FR-172 |
| sale.order.line | sv_cml_sample_ref · sv_cml_individualization | m2o sample · event | sample/quality reference; individualization event (lot/serial) with author = agreement / seller-alone | FR-173 |
| sale.order / l10n_sv_commerce.installment.resolution | resolutoria_registered · goods_identifiable | boolean · computed | inscribed clause + identifiable goods → third-party effects; else no effects vs good-faith acquirers (registry via SV-CML-FR-013/016 by id) | FR-174 |
| l10n_sv_commerce.resolution.settlement | use_indemnization · deterioration_indemnization · legal_interest_base · onerosa_pact_flag | perito-value slots ×2 · computed · validation | Art. 1026 matrix; interest rate via SV-CML-FR-158 by id; more-onerous pact = null warning; form-agnostic (lease-with-promise included) | FR-175 |
| sale.order | sv_cml_docs_delivery_checklist · sv_cml_pay_at_docs | checklist · boolean | título representativo + custom documents; price due at document delivery; refusal only with proof of defects | FR-176 |
| sale.order | sv_cml_transit_risk_pass · sv_cml_seller_concealment | event · boolean | carrier receipt (insurance policy among docs); known-and-concealed loss exception | FR-177 |
| l10n_sv_commerce.delivery.clause | clause_kind · price_composition · risk_pass_point · obligations_checklist | select · computed · select · checklist | csf_cif_caf (prima+flete; seller contracts carriage+total-value insurance+documents; carrier-receipt risk; uninsured-seller = insurer-responsibility; buyer self-insure + deduct) · cf (csf minus insurance) · lab_fob (all expenses to on-board; risk passes ON BOARD) · d_a · d_p (Art. 712 pointer, OQ-002) | FR-178, FR-179 |

**Venta a plazos:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.venta.plazos.contract | reserved_domain · chapter_benefits · threshold_flag | computed · computed · config | dominio gated on payment/condition; benefits = inscribed + value > threshold ("un mil colones" [sic] — SOQ-29 remnant, NO default, OQ-001) | FR-180 |
| l10n_sv_commerce.venta.plazos.contract | inscription_deadline · registry_entry_ref · endoso_state · opposable | computed date · m2o · select · computed | 30 days from contract date (registry-entry model SV-CML-FR-013 by id); simple-endoso negotiability (even post-execution-start); registered-only opposability + creditor-yield priority stamp | FR-181 |
| l10n_sv_commerce.venta.plazos.contract | intimation_state · intimation_min_term · secuestro_on · incautacion_ref · ajuste_cap · ajuste_sheet | state machine · const 10d · event · document ref · validation · execution title | notified → term → resolved_de_pleno_derecho; Art. 1026 cap (FR-175); saldo 10d; hoja de ajuste = título ejecutivo | FR-182 |
| l10n_sv_commerce.venta.plazos.contract | prescription_term · risks_on_buyer_from · taxes_insurance_payer · acceleration_events | override row · date (sale day) · buyer default · event set | 3m from Art. 1045-term end or incautación (SV-CML-FR-160 override by id); five Art. 1050 vencimiento events | FR-183 |

**Estimatorio, permuta, suministro:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| stock.location (consignment) + stock.quant | usage=consignment · owner_id = consignante | location type · m2o | ownership invariant: quants keep consignante ownership; seizure-protection stamp (not embargable by consignatario's creditors while unpaid); consignante disposal blocked until restitution; price-or-return settlement (impossibility no excuse) | FR-184 |
| sale.order (permuta) | sv_cml_exchange_mode · eviccion_election · evicction_value_basis | flag · select · date-basis | scope via FR-165; recover-given-thing vs evicted-value-at-eviction-moment + damages; sale-rules inheritance | FR-185 |
| sale.subscription (or recurring sale.order template) | supply_cadence · quantity_mode · min/max · needs_over_max · price_cadence | select · select · floats · boolean · select | periodic vs continued; normal-needs · suministrado-call-off-within-limits · needs-exceed-max right; per-prestación proportional invoicing vs pacted/usual vencimientos; Art. 1014 determination with vencimiento+place (FR-166 by id) | FR-186 |
| sale.subscription | date_call_notice · trust_resolution_flag · suspension_notice_clock | event · flag · 15d clock | sufficient-anticipation calls; confidence-affecting breach resolution (informational); no suspension without 15-day notice | FR-187 |
| sale.subscription | exclusivity_direction · exclusivity_zone · exclusivity_duration · promotion_lucro_note · denounce_clock | select · char · duration · note · 3m default clock | supplier-favour (no third-party equal prestations, no self-production save pact) · supplied-favour (zone+duration, direct and indirect); no-duration → denounce with pacted/uso/3-month notice | FR-188 |

**Comisión and mandato mercantil:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.comision | representation_mode · acceptance_state · refusal_clock · post_refusal_custody | const own_name_foreign_account · state · 8d · state | publicly-ostensible comisionista: silence 8 days = accepted; refusing comisionista still conserves effects until new encargado; damages responsibility stamp; depositary custody; contramarca segregation on multi-owner same-species lots | FR-189 |
| l10n_sv_commission.sale (link sale.order ↔ comision) | credit_authorization · credit_reported_buyers · cash_demandable | boolean · m2m list · computed | no credit without authorization → comitente may demand cash; authorized credit requires named-buyer report, else deemed cash; cobranza-diligence tracking | FR-190 |
| l10n_sv_commerce.comision.settlement | remuneration_source · expense_reimbursement · retention_right · withholding_gate · lifecycle_state | config slot (NO default, OQ-004) · computed w/ commercial interest · lien · payment gate · states | uso-de-la-plaza rate; cash reimbursement against justified cuenta; retention on held effects; buyer/bank must withhold commission when goods delivered without intervention; comisionista death/inhabilidad resolves, comitente's does not (revocable) | FR-191 |
| res.partner / l10n_sv_commerce.mandato.mercantil | representation_mode (name+account) · refusal_clock (8d) · execution_notice · ratification_state · written_mandate_ref | const · clock · event · silence-ratification stamp · document ref | refusal notice + conservation duties; unanswered execution notice → business deemed ratified though exceeded; written mandate exhibited to third parties; legal notes: Art. 1088 fire insurance, Art. 1093 interests on delayed funds, Art. 1097 preference ranking | FR-192 |

## 5. Odoo Mapping

Layer semantics for this wave: sales, subscriptions, stock and
intermediary registers are Odoo-native surfaces (sale.order,
sale.subscription, stock.lot, stock.location/quant, account.move
settlements, l10n_sv_commerce registers) — every FR maps `odoo`; none
touch DTE generation/transformation (an architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`), so no
`saas` rows are introduced. E-invoicing kin (pointer only): export
INCOTERM capture is SV-EINV-FR-045 (CAT-031), cited by id — the CC
clause catalog here never writes the DTE fields. Day/prescription
arithmetic is consumed from SV-FREP-FR-202..204 and SV-CML-FR-160 by
id; registry inscriptions ride SV-CML-FR-013/016 by id. Model names
are stable across Odoo 17/18/19/20; recurring supply uses
sale.subscription (Odoo 17 Enterprise subscription app; community
fallback = recurring sale.order templates — configuration-layer
choice, no version-specific behavior required by this file);
consignment uses stock.quant.owner_id, stable across versions.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-165 | odoo | sale.order + res.partner | sv_cml_mercantile_scope, direct_seller_profile | Farmer/artisan carve-out = informational classification; tax/DTE treatment untouched |
| FR-166 | odoo | sale.order | price_basis, arras allocation | Fixed-date bolsa/mercado reference; habitual-goods presumption; delivery-day market override; arras always to price |
| FR-167 | odoo | sale.order | pedido_binding_state | Signed pedido binds buyer; sumario remedy exposure informational; dependiente authority per file 06 by id |
| FR-168 | odoo | sale.order + stock | delivery_place_default | Establishment → domicilio ladder; feeds picking source location (establishment model per D14 design) |
| FR-169 | odoo | stock.lot | apparent waiver, packaged 8d window, exclusions | Lot-level; conventions from SV-CML-FR-145 by id; delivery-act recognition event |
| FR-170 | odoo | stock.lot | hidden 15d-from-discovery, acta ref, 1y anchor | Acta notarial reference required; anchor registered on SV-CML-FR-160 vicios row by id |
| FR-171 | odoo | stock.lot | warranty term, 30d denounce, 6m action, 3y default | Caducidad regime via SV-CML-FR-162 by id; unstated term → 3y |
| FR-172 | odoo | sale.order | perfection_mode, exam deadline ladder, silence approval | A-prueba suspensive condition blocks settlement semantics |
| FR-173 | odoo | sale.order.line + stock.lot | sample_ref, individualization event | Property transfer gated on individualization; author recorded |
| FR-174 | odoo | sale.order + l10n_sv_commerce registry link | resolutoria_registered, identifiability | Third-party effects gate; registry via SV-CML-FR-013/016 by id |
| FR-175 | odoo | l10n_sv_commerce.resolution.settlement | restitution matrix, onerosa-pact null | Interest via SV-CML-FR-158 by id; perito slots never computed; lease-with-promise included |
| FR-176 | odoo | sale.order + account.move | docs checklist, pay_at_docs | Price due at document delivery; refusal only with proofs |
| FR-177 | odoo | sale.order | transit risk pass, concealment exception, D/a D/P labels | Carrier-receipt risk pass; Art. 712 pointer only (OQ-002) |
| FR-178 | odoo | l10n_sv_commerce.delivery.clause | CSF/CIF/CAF cluster | Price = value + primas + fletes; three seller obligations; uninsured = insurer responsibility; carrier-receipt risk |
| FR-179 | odoo | l10n_sv_commerce.delivery.clause | CF, LAB/FOB risk-pass | FOB risk on board; no auto-translation to Incoterms CAT-031 (SV-EINV-FR-045 by id; OQ-003) |
| FR-180 | odoo | l10n_sv_commerce.venta.plazos.contract | reserved_domain, benefits, threshold flag | "un mil colones" [sic] = SOQ-29 flagged config, NO default (OQ-001) |
| FR-181 | odoo | l10n_sv_commerce.venta.plazos.contract | 30d inscription, endoso, opposability | Registry-entry model SV-CML-FR-013 by id; embargo-yield priority stamp |
| FR-182 | odoo | l10n_sv_commerce.venta.plazos.contract | intimation 10d, sequestro, ajuste título ejecutivo | De-pleno-derecho state machine; Art. 1026 cap via FR-175 |
| FR-183 | odoo | l10n_sv_commerce.venta.plazos.contract | 3m prescription override, risks/taxes, 5 acceleration events | Override row on SV-CML-FR-160 by id; buyer-side defaults from sale day |
| FR-184 | odoo | stock.location + stock.quant | consignment usage, owner_id invariant | Seizure-protection informational; price-or-return; disposal blocks both ways |
| FR-185 | odoo | sale.order | permuta mode, evicción election | Scope reuses FR-165; evicted-value-at-eviction-moment basis |
| FR-186 | odoo | sale.subscription / recurring template | cadence, quantity mode, min/max, price cadence | Enterprise subscription vs community recurring template — config-layer choice |
| FR-187 | odoo | sale.subscription | call notices, trust resolution, 15d suspension | Confidence-affecting breach = informational surface |
| FR-188 | odoo | sale.subscription | exclusivity both ways, zone, 3m denounce | Lucro-cesante note; no-duration denounce clock |
| FR-189 | odoo | l10n_sv_commerce.comision | own-name/foreign-account, 8d silence, custody, contramarca | Name/account matrix distinct from agentes (file 06) and mandato |
| FR-190 | odoo | commission sale link | credit_authorization, named buyers, cash flip | No credit w/o authorization → cash-demandable; unreported = deemed cash |
| FR-191 | odoo | l10n_sv_commerce.comision.settlement | uso-de-plaza slot, retention, withholding gate | Rate config NO default (OQ-004); buyer/bank withholding; lifecycle states |
| FR-192 | odoo | l10n_sv_commerce.mandato.mercantil | name+account, 8d refusal, silence-ratification, written mandate | Art. 1088/1093/1097 as legal-note surfaces |

Version-regime notes (D12): no dated values live in this file except
the deliberately-unconfigured Art. 1038 threshold (SOQ-29/OQ-001) and
the Art. 1079 uso-de-plaza commission rate (OQ-004) — both dated
configuration slots with NO shipped defaults, never hardcoded. All
day/month terms (8d/10d/15d/30d/3m/6m/1y/3y) are un-reformed statutory
text under the SOQ-22 residual watch, stored as code constants with
provenance.

## 6. Acceptance Criteria

- **AC-001:** Given a sale of harvest produce by a farmer who keeps
  no almacén or tienda, when FR-165 classifies, then the sale is
  stamped NOT mercantile (carve-out) with the classification note;
  given an artisan's workshop sale of objects fabricated there, then
  likewise NOT mercantile; given a sale within an empresa's normal
  giro, then mercantile (FR-165).
- **AC-002:** Given a contract over things habitually sold by the
  seller with no agreed price, when FR-166 resolves, then the price
  basis = the seller's normally-required price; given the thing bears
  a market price, then the basis = the market price ON THE DELIVERY
  DAY; given arras of $500 on a $5,000 price, then the balance after
  allocation is $4,500 — arras always to the account of the price
  (FR-166).
- **AC-003:** Given a pedido signed by the buyer's authorized
  dependiente, when FR-167 stamps, then the order is binding at the
  pedido's conditions with the sumario-consignación + price + delay
  damages exposure recorded; given no signature, then no binding
  state (FR-167).
- **AC-004:** Given a lot received enfardada on 01-Mar and examined
  to satisfaction at receipt, when FR-169 evaluates, then the
  apparent-defect waiver is stamped; given the same lot NOT examined,
  then the packaged-claim window runs to 09-Mar (the eight days
  following receipt, exclude-start-day per SV-CML-FR-145 by id), and
  a claim on 10-Mar is time-barred unless caso fortuito/vicio
  propio/fraude de tercero was flagged (FR-169).
- **AC-005:** Given a hidden vice discovered on 10-May on a lot
  delivered 01-Mar, when FR-170 tracks, then the denounce window runs
  to 25-May (fifteen days following discovery) and the denounce event
  REQUIRES an acta-notarial reference to count; given a timely
  denounce, then the action clock prescribes one year from delivery —
  anchor 01-Mar (registered on the SV-CML-FR-160 vicios row by id)
  (FR-170).
- **AC-006:** Given a seller-guaranteed functioning thing whose
  defect is discovered 01-Jul under a warranty with no stated term,
  when FR-171 evaluates, then the warranty term defaults to THREE
  YEARS, the denounce caducidad window runs to 31-Jul (thirty days
  from discovery, fuerza-mayore suspension per SV-CML-FR-162 by id),
  and a timely denounce starts the SIX-MONTH action clock from the
  denounce date (FR-171).
- **AC-007:** Given an LAB/FOB sale, when FR-179 records the clause,
  then the price composition covers all expenses to ON BOARD and the
  risk-pass event = goods placed on board; given a CSF sale, then the
  composition includes primas + fletes to the reception place and the
  risk passes at CARRIER RECEIPT; given a CF sale, then the CSF
  composition MINUS insurance (FR-178, FR-179).
- **AC-008:** Given a CSF seller who did not contract the insurance
  and a siniestro occurs, when FR-178 evaluates, then the seller's
  responsibility surface shows AS-THE-INSURER exposure and the
  buyer's self-insurance path allows DEDUCTING the prima from the
  price due (FR-178).
- **AC-009:** Given a venta a plazos contract above the (unset)
  threshold and not inscribed, when FR-180/FR-181 evaluate, then the
  chapter-benefits stamp is OFF with the SOQ-29 threshold flag noted
  (OQ-001 — no default value blocks nothing but the stamp); given
  inscription requested on day 25 of the contract, then the
  30-day window is met and opposability + endoso negotiability turn
  on (FR-180, FR-181).
- **AC-010:** Given a missed cuota and a judicial intimation
  notified 01-Jun with a ten-day term, when FR-182 tracks, then
  expiry on 11-Jun without payment flips the contract to
  RESOLVED-DE-PLENO-DERECHO with the sequestro/incautación surfaces;
  given an ajuste sheet attempting indemnization beyond the Art. 1026
  matrix, then the FR-175 more-onerous validation flags it NULL; and
  the judge-visada sheet carries the título-ejecutivo stamp
  (FR-182, FR-175).
- **AC-011:** Given a resolved and executed venta a plazos whose
  Art. 1045 saldo term ended 01-Aug, when FR-183 computes, then every
  contract-generated action prescribes 01-Nov (three months); given
  no saldo term, then the anchor is the INCAUTACIÓN date; and given
  the buyer transports the thing abroad without the owner's written
  consent, then the acceleration listener stamps the plazos VENCIDOS
  (FR-183).
- **AC-012:** Given goods consigned under an estimatorio contract,
  when FR-184 evaluates, then the quants at the consignment location
  retain the CONSIGNANTE as owner, the lot carries the
  not-embargable-by-consignatario's-creditors stamp while the price
  is unpaid, and a consignante disposal attempt is blocked until
  restitution; given return becoming impossible without the
  consignatario's fault, then the price-or-return settlement still
  demands the PRICE (FR-184).
- **AC-013:** Given a comisión credit sale recorded without the
  comitente's authorization, when FR-190 evaluates, then the
  settlement flips DEMANDABLE-AT-CASH with the flip reason recorded;
  given an authorized credit sale reported without the buyer's name,
  then it is stamped deemed-CASH vis-à-vis the comitente; given an
  authorized credit sale with the named-buyer report, then credit
  stands and the cobranza-diligence tracking begins (FR-190).
- **AC-014:** Given commission merchandise delivered to the buyer
  without the comisionista's intervention, when FR-191 gates the
  payment, then the price cannot pass to the comitente WITHOUT the
  commission value being retained and placed at the comisionista's
  disposal — the payer's breach surfaces its responsibility to the
  comisionista; and given effects in the comisionista's power, then
  the retention right shows them preferently affected to commission,
  anticipos and gastos (FR-191).
- **AC-015:** Given a suministro with no duration clause, when
  FR-188 computes the denounce, then the notice clock defaults to
  THREE MONTHS (pacted/uso anticipations overriding when present);
  given an exclusivity clause in favour of the suministrado with a
  zone, then the supplier's same-object sales in that zone for the
  contract's duration — direct or indirect — carry the breach
  surface (FR-188).
- **AC-016:** Given a mandato execution notice sent to the mandante
  who does not respond immediately, when FR-192 evaluates, then the
  business is stamped PRESUMED RATIFIED — including where the
  mandatario exceeded the mandate's terms (exceeded-terms note
  carried); and given the mandatario contracting with a third party,
  then the written-mandate reference is present on the dealing
  (FR-192).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-29 (carrying 07_ OQ-7): Art. 1038 conditions the venta-a-plazos chapter benefits on the contract value exceeding "un mil colones" — an unreformed 1970 colones phrase with NO evidenced USD conversion rule in the corpus (the dollarization statute is not among the sources). FR-180 ships the threshold as a FLAGGED config slot with NO default: the flag never blocks recording, only the chapter-benefit stamp. When a conversion/equivalence instrument is pinned, load the value as dated configuration — never hardcode. | no | Takumi S5 (sources watch) | open |
| OQ-002 | Art. 1029 routes the D/a (documentos contra aceptación) and D/P (documentos contra pago) clauses to Art. 712 — the documentary-credit/collection mechanics in the bank-operations zone skimmed in the 07_ evidence. FR-177 carries the clause labels only. If documents-against settlement flows must be mechanized, acquire/extract the Art. 712 zone first. | no | Takumi S5 (sources watch) | open |
| OQ-003 | The CC clause labels (csf/cif/caf, CF, LAB/FOB, Arts. 1030-1035) predate modern Incoterms; the FEX e-invoice requires an INCOTERMS code from CAT-031 when exportación = 1 (SV-EINV-FR-045 by id). The mapping between CC labels and CAT-031 codes (e.g. whether "csf" maps to CIF) is NOT evidenced in the corpus and current Incoterms definitions are outside scope: FR-179 forbids auto-translation and stores both sides with provenance; a curated mapping table is needed at implementation after CAT-031 is enumerated. | no | Takumi S5 + legal review | open |
| OQ-004 | The comisión remuneration defaults to the "uso de la plaza" where the commission is realized (Art. 1079) — no statutory rate in the corpus (kin of file-06 OQ-002: usos del lugar rates). FR-191 ships the config slot with NO default; commission computations that depend on it surface a config-missing flag. Acquire usos evidence or client contract data at implementation; never hardcode. | no | Takumi S5 | open |
| OQ-005 | Consumer-protection legislation (Ley de Protección al Consumidor) commonly overlays warranty terms and reversal rights on merchant-layer sales; it is outside this corpus. The Arts. 1019-1021 clocks are the CC merchant-layer defaults; if the consumer law is acquired, register its overrides as dated configuration on the FR-169..171 clock registry — never as edits of the CC defaults. | no | Takumi S5 (sources watch) | open |
