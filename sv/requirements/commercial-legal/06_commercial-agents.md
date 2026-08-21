# SV — Commercial-legal — Commercial agents and authority defaults: factores, dependientes, agentes and intermediarios

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador *auxiliares de los comerciantes* (merchant
auxiliaries) regime of Código de Comercio (Commercial Code, CC) Libro I
Título III — the authority-default model that decides who may bind a
merchant and with what powers: the *factor* (business manager, Arts.
365-377) — general authority from sole appointment over the enterprise's
*giro* (line of business), registry inscription of the appointment, its
modifications and ALWAYS its terminación, the deemed-general mandate of
Art. 368, and post-revocation validity until legitimate notice or
inscription; the *dependiente* (dependent sales clerk, Arts. 378-383) —
the bind-the-principal defaults, in-store price collection unless a *caja*
(cash desk) or special-department reserve is publicly posted, the
plazos/descuentos special-authorization rule, the OUTSIDE sale/collection
rule (written authorization + identity document, or delivery of the
*recibo o la factura* — receipt or invoice — bearing the principal's
*firma y sello*, signature and stamp), and the *dependiente viajero*
(travelling salesman) order-taking/guarantee defaults; the *agente
dependiente* (dependent agent, Arts. 384-391) — plaza/region promotion
under subordination, the default exclusivity of Art. 386, exclusive-zone
participations on the principal's own deals, the per-principal *libro
especial* (special operations book) and the monthly documented-account
remuneration; the *agente representante o distribuidor*
(representative/distributor agent, Arts. 392-399-B) — continuous
designation by contract, the commission defaults of Art. 395 including
exclusive-zone commissions on the principal's own or *enviados'* (envoys')
deals, the 3-month written termination notice, the 5-head indemnification
scale of Art. 397 (verbatim table, §3.4), the just causes of Art. 398, and
the foreign-principal import bar of Art. 399-B; and the *agente
intermediario* (intermediary/broker agent, Arts. 400-410) — no
representation, remuneration conditioned on contract celebration, and the
agent's OWN statutory books (a *registro* and a *libro diario de
operaciones* kept with mercantile-accounting formalities).

It does **not** cover: merchant status, matrícula and the registry
architecture (`01_merchant-registration.md` — consumed by id: FR-013
registry-entry model, FR-014 poderes/nombramientos/credenciales
registration surface whose authority semantics THIS file owns, FR-015
matrícula-precondition gate); bookkeeping form, register legalization,
the no-alteration regime and retention (`02_accounting-books.md` —
consumed by id: FR-025 Art. 440 discipline extension, under which the
agents' libro especial and the intermediaries' books inherit the register
discipline flags; FR-028 retention matrix row a); the annual statement
cycle and balance deposit (`03_financial-statements.md`); society types
and lifecycle (`04_society-types.md`, `05_society-lifecycle.md`); the
empresa mercantil transfer package and EIRL
(`07_empresa-mercantil-eirl.md`, when it lands — Arts. 553-622 zone);
payment instruments (`08_payment-instruments.md`); sales contracts
(`09_sales-contracts.md`); AML compliance (`10_aml-compliance.md`); and
the EMPLOYMENT side of the salesperson/agent relation — hiring, salary
integration, social security and termination indemnities are Código de
Trabajo (CT, Labor Code) territory owned by the payroll wave
(`sv/requirements/payroll/01_salary-model.md` — commissions and sales
percentages are *salario integrante*, SV-PAY-FR-002;
`sv/requirements/payroll/07_contracts-termination.md` — contract taxonomy
and termination outcomes, SV-PAY-FR-101..110), cited by id only: this
file owns the CC commercial-authority layer (who binds the principal,
with which default powers, and the channel-protection machinery), never
the labor layer (boundary → OQ-001).

## 2. Legal Basis

Authority order (binding, per master evidence index S5): the Código de
Comercio = **07_** (D.L. Nº 671, 8-may-1970, D.O. 140 T.228 31-jul-1970;
29 listed reforms, last = D.L. 641-2008) — article text CURRENT per the
**SOQ-22 verification (resolved-with-residual, W12 2026-08-18)**: the
second official copy 73_ (UIF-hosted Índice Legislativo edition, 280 pp.)
ALSO ends its reform list at D.L. 641-2008, so no post-2008 CC structural
reform is evidenced in two official consolidations; the residual — both
copies are Asamblea-editorial artifacts without a stated as-of date —
rides every 07_ LB in this file. Verbatim text below is copied from the
extraction txt `sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable per
standing ruling; page pointers = txt PAGE markers; reform tick marks
"(5)" (Section B, D.L. 247 substitution) and "(18)" stripped from
quotations, provenance noted here). EVID-223 is the governing evidence
for the whole cluster; its verbatim field abbreviates, so the txt is the
primary verbatim source for every LB here.

Provenance notes from the print itself: Art. 401 is DEROGADA (reform
(18)); Sección "B" (Agentes Representantes o Distribuidores) was
substituted by D.L. Nº 247 (9-ene-1973, D.O. Nº 23 T.238 2-feb-1973 per
the print's NOTA considerando I). That NOTA also transcribes the 1985
authentic interpretation of Art. 392 (D. Nº 237, D.O. 244-Bis T.289
23-dic-1985) — DECLARED UNCONSTITUTIONAL by the Sala de lo Constitucional
(sent. 15-feb-1988, D.O. Nº 41 T.298 29-feb-1988) — which is therefore
NOT cited as authority anywhere in this file (→ OQ-004 records the
exclusion).

Payroll interface note (pointer by id/file only, no labor rule derived):
commissions and sales percentages received by dependent workers are
*salario integrante* per `sv/requirements/payroll/01_salary-model.md`
SV-PAY-FR-002, and contract taxonomy/termination outcomes are
`sv/requirements/payroll/07_contracts-termination.md` SV-PAY-FR-101..110
(CT = `sv/sources/11_Codigo_Trabajo.pdf`, payroll-wave corpus). The CC
texts below govern only the commercial-authority and channel-protection
layer.

Currency discipline (SOQ-29): no colones-denominated values and no
monetary amounts occur in this file's article set — only periods (15
days, 3 months, 6 months, 3 years) and the indemnification valuation
formulas (cost + *fletes* (freight) + taxes), which are computation
rules, not fixed values.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 365: "Son factores quienes dirigen por cuenta ajena, una empresa, una rama especial de ella o un establecimiento de la misma." Art. 366: "El solo nombramiento de un factor lo faculta para realizar todas las operaciones concernientes al objeto de la empresa o del establecimiento que dirija, las cuales se reputarán ejecutadas en nombre y por cuenta del principal, aún cuando el factor no lo haya expresado así al celebrarlas, haya transgredido instrucciones o cometido abuso de confianza, siempre que tales contratos recaigan sobre objetos comprendidos en el giro y tráfico de la empresa o del establecimiento, o si, aun siendo de otra naturaleza, resultare que el factor obró con orden de su principal, o que éste aprobó su gestión en términos expresos o por hechos positivos." "Las limitaciones a estas facultades del factor no producirán efectos contra tercero, a menos que se compruebe que éste las conocía al celebrar el respectivo negocio." | Factors are those who direct, on another's account, an enterprise, a special branch of it or an establishment of it. The SOLE APPOINTMENT of a factor authorizes him to perform all operations concerning the object of the enterprise or establishment he directs — deemed executed in the name and on the account of the principal even if the factor did not so express it, transgressed instructions or committed abuse of trust — provided the contracts fall on objects within the giro and traffic of the enterprise, or, being of another nature, the factor acted on the principal's order or the principal approved the gestión expressly or by positive facts. LIMITATIONS on these faculties produce NO effects against third parties unless it is proven the third party knew them when celebrating the business | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 365-366 p.69 (EVID-223; txt PAGE 69) |
| LB-002 | Código de Comercio, Art. 367: "El nombramiento del factor y sus modificaciones posteriores deberán inscribirse en el Registro de Comercio en que esté inscrita la empresa y, en su caso, el establecimiento." "La terminación de los poderes del factor deberá inscribirse siempre en el Registro de Comercio, aun cuando no se haya registrado el nombramiento." "La falta de inscripción hará que los actos mencionados no surtan más efectos que los expresamente señalados en los restantes artículos de este capítulo." | The factor's appointment and its later modifications must be INSCRIBED in the Commerce Registry where the enterprise — and, where applicable, the establishment — is registered. The TERMINATION of the factor's powers must ALWAYS be inscribed in the Commerce Registry, even when the appointment was never registered. Lack of inscription leaves the acts with no effects other than those expressly stated in the remaining articles of this chapter | `sv/sources/07_Codigo_Comercio.pdf` | Art. 367 p.70 (EVID-223; txt PAGE 70) |
| LB-003 | Código de Comercio, Art. 368: "El principal que haya designado el factor, es responsable de los actos de éste y de las obligaciones que contraiga en los términos del artículo 371." "Si el mandato conferido de modo expreso al factor no se otorgare por escrito o no se inscribiere, se reputará, respecto a tercero, general para todos los actos concernientes a la rama de comercio de que el factor esté encargado, sin que el mandante pueda alegar frente al tercero ninguna limitación de tal mandato, a menos que compruebe que el tercero la conocía en el momento en que se celebró la operación respectiva." "Cuando los principales sean varios, tendrán responsabilidad solidaria por los actos del factor. Si el principal fuere una sociedad, la responsabilidad de los socios se regulará de conformidad con la naturaleza de la misma." | The principal who designated the factor is responsible for the factor's acts and obligations in the terms of Art. 371. If an EXPRESS mandate was neither granted in writing nor inscribed, it is deemed — towards third parties — GENERAL for all acts of the branch of commerce the factor is in charge of, and the mandant cannot allege any limitation against the third party unless he proves the third party knew it when the operation was celebrated. Where there are several principals they are SOLIDARILY responsible for the factor's acts; if the principal is a sociedad, the socios' responsibility follows the sociedad's nature | `sv/sources/07_Codigo_Comercio.pdf` | Art. 368 p.70 (EVID-223; txt PAGE 70) |
| LB-004 | Código de Comercio, Art. 369: "El factor actuará a nombre de su principal, expresándolo así en los documentos que con tal carácter suscriba." Art. 370: "Si a pesar de lo dispuesto en el artículo anterior, el factor contratare expresamente en nombre propio, pero la otra parte demostrare que lo hizo por cuenta del principal, podrá dirigir su acción contra el factor o contra el principal, quienes serán solidariamente responsables." | The factor acts in his principal's NAME, so expressing it in the documents he signs in that character. If despite the foregoing the factor contracts expressly in his own name, but the other party demonstrates he did so on the principal's account, that party may direct its action against the factor OR against the principal, who are SOLIDARILY responsible | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 369-370 p.70 (EVID-223; txt PAGE 70) |
| LB-005 | Código de Comercio, Art. 371: "Aunque se haya revocado el poder a un factor, o éste haya de cesar en sus funciones por haberse enajenado el establecimiento que dirigía, serán válidos los actos y contratos que celebre después de la revocación o enajenación, hasta que lleguen a su noticia por un medio legítimo." "Con relación a terceros, serán igualmente válidos mientras la revocación o enajenación no se haya inscrito en el Registro de Comercio." | Even if a factor's power has been revoked, or he is to cease functions because the establishment he directed was alienated, the acts and contracts he celebrates AFTER revocation or alienation are VALID until they reach his notice by a legitimate means. Towards third parties they are equally valid while the revocation or alienation is not INSCRIBED in the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 371 p.70 (EVID-223; txt PAGE 70) |
| LB-006 | Código de Comercio, Art. 372: "Si fueren varios los factores, se presumirá que deberán decidir por mayoría, a no ser que del nombramiento aparezca, expresa o tácitamente, que cada uno podrá obrar con independencia de los otros en todos los negocios o en algunos de su exclusiva competencia." Art. 373: "Aunque el principal interesare en las utilidades del giro al factor, éste no podrá oponerse a que se lleven a cabo las operaciones ordenadas por el primero." Art. 374: "El factor responderá a su principal de los daños y perjuicios que le ocasione por su culpa en las gestiones propias de su encargo, sin perjuicio de la responsabilidad directa del principal frente a terceros." Art. 376: "El factor es responsable solidariamente con su principal del cumplimiento de las disposiciones de este Código y demás leyes que se refieren al ejercicio del comercio o a la explotación de la rama mercantil que tenga a su cargo." | If there are SEVERAL factores, they are presumed to decide BY MAJORITY unless the appointment shows, expressly or tacitly, that each may act independently of the others in all business or in some of his exclusive competence. Even if the principal gives the factor an interest in the giro's profits, the factor cannot oppose the operations ordered by the principal. The factor answers to his principal for damages caused by his FAULT in the gestión proper to his charge, without prejudice to the principal's direct responsibility towards third parties. The factor is SOLIDARILY responsible with his principal for compliance with this Code and other laws on the exercise of commerce or the exploitation of the mercantile branch in his charge | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 372-374, 376 pp.70-71 (EVID-223; txt PAGE 70-71) |
| LB-007 | Código de Comercio, Art. 375: "El factor no podrá traficar por su cuenta, ni interesarse en nombre propio o de tercero en negocios del mismo género de los que realice a nombre de su principal, a menos que éste lo autorice para ello, expresamente y por escrito." "Si negociare sin esta autorización, el principal podrá hacer suya la operación, dentro de los quince días siguientes a la fecha en que tuvo conocimiento de ella, sin perjuicio de dar por terminado el mandato, conforme a lo establecido en el artículo 377." Art. 377: "Además de los casos de terminación normal del mandato conferido al factor, el poder expirará: I.- Por parte del principal: a) Cuando el factor incurra en fraude o abuso de confianza en las gestiones que tenga encomendadas. b) Cuando el factor haga alguna negociación que fuere contraria a las prohibiciones estipuladas en el contrato o a las que la ley establece. c) Cuando el factor observare mala conducta pública o privada. II.- Por parte del factor: a) Cuando el principal faltare al pago puntual de los respectivos estipendios o cuando incumpliere cualquiera de las cláusulas sobre la cuantía y forma de la remuneración. b) Por malos tratamientos personales." | The factor may NOT trade on his own account nor take an interest, in his own or a third party's name, in business of the same kind he performs for his principal, unless the principal authorizes it EXPRESSLY AND IN WRITING. If he negotiates without this authorization, the principal may MAKE THE OPERATION HIS OWN within FIFTEEN DAYS from the date he learned of it, without prejudice to terminating the mandate per Art. 377. Besides normal termination, the power expires: I. by the principal — a) factor fraud or abuse of trust in the entrusted gestión; b) a negotiation contrary to contractual or legal prohibitions; c) public or private misconduct of the factor; II. by the factor — a) the principal's failure to pay the respective stipends punctually or breach of any clause on the remuneration's amount and form; b) personal ill-treatment | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 375, 377 p.70-71 (EVID-223; txt PAGE 70-71) |
| LB-008 | Código de Comercio, Art. 378: "El dependiente obliga al principal." "Los dependientes encargados de ventas tienen facultad para percibir dentro del establecimiento el pago del precio de las mercancías vendidas, a no ser que tal percepción se haya reservado a una caja o a un departamento especial, haciéndolo saber al público por medio de anuncio colocado en lugar visible del establecimiento. Para conceder plazos o descuentos, necesitan estar especialmente autorizados; cuando no lo estuvieren, la operación será válida con respecto al comprador, pero los dependientes quedan responsables para con su principal de los daños y perjuicios que pudieren resultarle. Lo dicho en este inciso se extiende a las empresas de servicios y sus dependientes." "Para vender o cobrar fuera del establecimiento, los dependientes necesitarán exhibir autorización escrita, acompañada de documento de identidad, o entregar a cambio del pago el recibo o la factura con la firma y sello del principal o de sus representantes." "Los que presten sus servicios fuera de los locales de la empresa, son dependientes viajeros." | The dependiente BINDS the principal. Sales dependientes may collect, WITHIN the establishment, the price of goods sold — unless such perception is reserved to a caja (cash desk) or special department, made known to the public by an announcement posted in a visible place of the establishment. To grant plazos (credit terms) or descuentos (discounts) they must be SPECIALLY authorized; when not, the operation is valid towards the buyer but the dependientes remain liable to their principal for resulting damages. What this inciso says EXTENDS to service enterprises and their dependientes. To sell or collect OUTSIDE the establishment, dependientes must exhibit a WRITTEN AUTHORIZATION accompanied by an identity document, OR deliver in exchange for payment the receipt or invoice with the firma y sello (signature and stamp) of the principal or its representatives. Those rendering services outside the enterprise's premises are dependientes viajeros | `sv/sources/07_Codigo_Comercio.pdf` | Art. 378 p.71 (EVID-223; txt PAGE 71) |
| LB-009 | Código de Comercio, Art. 379: "Los actos de los dependientes obligan a sus principales en todas las operaciones que tuvieren a su cargo, en razón del puesto que ocupan frente al público." | The acts of dependientes bind their principals in ALL the operations in their charge, by reason of the post they occupy before the public | `sv/sources/07_Codigo_Comercio.pdf` | Art. 379 p.71 (EVID-223; txt PAGE 71) |
| LB-010 | Código de Comercio, Art. 380: "Salvo que comprueben autorización expresa, los dependientes viajeros no podrán percibir el precio anticipado de las mercancías, cuando ellos no hicieren la entrega de las mismas en el momento de celebrar la operación con el comprador de aquéllas, ni conceder esperas, plazos, quitas o descuentos; pero tendrán facultad de recibir las órdenes de pedido y pactar las garantías o seguridades que consideren prudente, en interés del principal y en previsión de que la otra parte dejare de cumplir lo que prometa." Art. 381: "Se prohíbe a los dependientes viajeros suscribir documentos de obligación con carácter de apoderados del principal, salvo que tuvieren mandato para ello; en cuyo caso, indicarán el nombre completo con que el principal opere comercialmente y su domicilio." | Unless express authorization is proven, dependientes viajeros may NOT collect the ADVANCED price of goods when they do not deliver them at the moment of celebrating the operation with the buyer, NOR grant esperas (forbearances), plazos, quitas (partial remissions) or descuentos; but they have faculty to RECEIVE PURCHASE ORDERS and to agree the guarantees or securities they deem prudent, in the principal's interest and in anticipation of the other party's non-performance. Dependent travellers are FORBIDDEN to subscribe obligation documents as the principal's apoderados (attorneys-in-fact) unless mandated for it — in which case they indicate the full name under which the principal commercially operates and its domicile | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 380-381 pp.71-72 (EVID-223; txt PAGE 71-72) |
| LB-011 | Código de Comercio, Art. 382: "Se prohíbe a los dependientes ejercer, por cuenta propia o ajena, actos aislados o tener empresas en las mismas materias similares al comercio de sus principales; y divulgar informaciones acerca de la clientela, situación económica del negocio u otras de carácter reservado, del principal." Art. 383: "Son aplicables a los dependientes, en lo que fueren compatibles, las disposiciones relativas a los factores." | Dependent clerks are FORBIDDEN to perform, on their own or another's account, isolated acts or hold enterprises in the same matters similar to their principals' commerce, and to divulge information on the clientele, the business's economic situation or other reserved information of the principal. The provisions on factores apply to dependientes insofar as compatible | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 382-383 p.72 (EVID-223; txt PAGE 72) |
| LB-012 | Código de Comercio, Art. 384: "Es agente dependiente la persona encargada de promover, en determinada plaza o región, negocios por cuenta de un principal, con domicilio en la República o en el extranjero, y de transmitirle las propuestas para su aceptación. El agente dependiente está subordinado al principal." Art. 385 (incisos 1-2): "El agente dependiente no tendrá facultad, salvo mandato expreso, para celebrar contratos, hacer cobros, o conceder descuentos, quitas o plazos por cuenta del principal; sin embargo, podrá recibir quejas o reclamaciones por defectos de calidad o de cantidad de las mercancías y obtener fianzas en interés del principal, que garanticen el cumplimiento de las obligaciones del solicitante, cuando le sean entregadas las mercancías que haya pedido." "Los agentes de empresas de seguros, capitalización, ahorro y préstamos, ahorro para adquisición de bienes y otras similares, están obligados a presentar al cliente con quien contraten la credencial que los acredita como tales. Se presume que tienen facultad para celebrar contratos, recibir solicitudes, rechazar declaraciones escritas de los proponentes, cobrar primas vencidas y proceder a la comprobación de los siniestros que se realicen, salvo que la empresa por cuenta de quienes actúen haya limitado expresamente sus facultades en la credencial respectiva, pero no podrá hacerlo en la medida en que haga imposible el ejercicio de la agencia. Pero, a menos que conste expresamente en la credencial, no tendrán autorización para modificar en ningún sentido el texto del contrato que figure en la solicitud." | The agente dependiente is the person charged with PROMOTING, in a determined plaza (market territory) or region, business on a principal's account — the principal domiciled in the Republic or abroad — and transmitting proposals for acceptance; he is SUBORDINATE to the principal. Absent express mandate, the agente dependiente has NO faculty to celebrate contracts, make collections, or grant discounts, quitas or credit terms on the principal's account; however, he may receive complaints or claims for quality or quantity defects and obtain fianzas (bonds) in the principal's interest guaranteeing the applicant's obligations when the goods he ordered are delivered to him. Agents of insurance, capitalization, savings-and-loan, savings-for-acquisition and similar enterprises must present the client the credential accrediting them; they are PRESUMED empowered to celebrate contracts, receive applications, reject proponents' written declarations, collect due premiums and verify claims — unless the enterprise expressly limited the faculties in the credential (not to the point of making the agency's exercise impossible); and, unless expressly stated in the credential, they have NO authorization to modify in any sense the contract text figuring in the application | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 384-385 p.72 (EVID-223; txt PAGE 72) |
| LB-013 | Código de Comercio, Art. 386: "Salvo pacto en contrario, ningún principal puede utilizar los servicios, en la misma plaza o en la misma región para un mismo ramo del comercio, de agente diverso de aquél con quien tenga ya contrato en vigor, que se considerará exclusivo. Tampoco puede ningún agente asumir el encargo de promover o tratar asuntos de otros principales." | Save contrary pact, NO principal may use the services — in the same plaza or region, for the same ramo (branch) of commerce — of an agent other than the one with whom he already has a contract in force, WHICH IS DEEMED EXCLUSIVE; nor may any agent assume the charge of promoting or handling affairs of OTHER principals | `sv/sources/07_Codigo_Comercio.pdf` | Art. 386 p.72 (EVID-223; txt PAGE 72) |
| LB-014 | Código de Comercio, Art. 387: "Cuando el principal promoviere por sí mismo o por medio de otro, operaciones en una plaza o región en la que tenga agente con carácter exclusivo, éste tendrá derecho a que el principal le pague las participaciones que le hubieren correspondido si el negocio de que se trate lo hubiera promovido el agente." Art. 389: "Salvo lo que estipule el contrato entre el principal y el agente, éste proveerá a sus expensas todos los gastos e impuestos que exija el ejercicio de la agencia. Su remuneración se calculará a base de un porcentaje sobre los pagos que cada cliente haga en relación con las operaciones en que el agente haya intervenido." Art. 390: "Si el principal desiste de cualquier contrato celebrado por el agente, o lo modifica, el agente tendrá derecho a percibir el porcentaje estipulado, como si la operación se hubiera llevado a cabo sobre las bases por él pactadas." | When the principal promotes operations — by himself or through another — in a plaza or region where he has an agent with exclusive character, that agent is entitled to the participations that would have corresponded to him had the business been promoted by the agent. Save contractual stipulation, the agent bears at his own expense all expenses and taxes the agency's exercise demands; his remuneration is computed as a PERCENTAGE on the payments each client makes on operations in which the agent intervened. If the principal desists from any contract celebrated by the agent, or modifies it, the agent is entitled to the stipulated percentage AS IF the operation had been carried out on the bases he agreed | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 387, 389-390 pp.72-73 (EVID-223; txt PAGE 72-73) |
| LB-015 | Código de Comercio, Art. 388: "Todo agente tiene obligación de proporcionar a sus principales las informaciones que puedan interesarles. El agente deberá anotar en un libro especial, con la separación conveniente, las operaciones relativas a cada principal y expresar los detalles necesarios que permitan distinguir los pedidos y las mercancías que a cada uno correspondan." | Every agent must furnish his principals the information that may interest them. The agent must record in a libro especial (special book), with the proper separation, the operations relative to EACH PRINCIPAL, expressing the necessary details distinguishing the pedidos (orders) and the goods corresponding to each | `sv/sources/07_Codigo_Comercio.pdf` | Art. 388 p.73 (EVID-223; txt PAGE 73) |
| LB-016 | Código de Comercio, Art. 391: "Cuando en el contrato entre el principal y el agente no se estipule otra cosa, la remuneración del agente le será cubierta al final de cada mes, contra la remisión de la cuenta respectiva, debidamente documentada." | When the principal-agent contract does not stipulate otherwise, the agent's remuneration is paid AT THE END OF EACH MONTH, against the remission of the respective account, DULY DOCUMENTED | `sv/sources/07_Codigo_Comercio.pdf` | Art. 391 p.73 (EVID-223; txt PAGE 73) |
| LB-017 | Código de Comercio, Art. 392: "Para los efectos de este Código se entiende por agente representante o distribuidor, la persona natural o jurídica que, en forma contínua [sic], con o sin representación legal y mediante contrato, ha sido designada por un principal para la agencia-representación o distribución de determinados productos o servicios en el país." "Cuando el agente representante o distribuidor no actúa por su cuenta y riesgo sino siguiendo instrucciones de su principal, no será responsable por el incumplimiento en que éste haya incurrido; su responsabilidad se limita, en este caso, al estricto cumplimiento de las instrucciones que reciba del principal." "La agencia-representación o distribución, podrá ser exclusiva o de cualquiera otra forma que acuerden las partes." (the print's NOTA transcribing the 1985 authentic interpretation of this article was declared UNCONSTITUTIONAL — §2 provenance; not cited as authority) | For the purposes of this Code, agente representante o distribuidor is the natural or juridical person who, CONTINUOUSLY, with or without legal representation and by CONTRACT, has been designated by a principal for the agency-representation or distribution of determined products or services in the country. When the representative/distributor does not act on his own account and risk but following his principal's instructions, he is NOT responsible for the principal's non-performance — his responsibility limiting itself, in that case, to strict compliance with the instructions received from the principal. The agency-representation or distribution may be EXCLUSIVE or in any other form the parties agree | `sv/sources/07_Codigo_Comercio.pdf` | Art. 392 p.73 (EVID-223; txt PAGE 73) |
| LB-018 | Código de Comercio, Art. 393: "El Agente representante o distribuidor está en libertad de dedicarse a cualquiera otra clase de negocios o actividad mercantil distintos de aquéllos que realice en virtud del contrato de agencia-representación o distribución, con la única obligación de evitar la concurrencia con su principal. Sin embargo, el principal puede autorizarlo para realizar negocios de la misma clase de los que le tiene encomendados." "Cuando el agente fuere representante o distribuidor de varios principales y uno de ellos introdujere una línea competitiva de otra que el agente distribuya o represente, deberá éste hacerlo del conocimiento de los principales respectivos, con el objeto de realizar las negociaciones pertinentes en relación con la línea." Art. 394: "Las condiciones generales en que el agente representante o distribuidor puede tramitar proposiciones o, en su caso, contratar, podrán ser alterados por el principal, siempre que no contraríen los términos del contrato. Las modificaciones serán obligatorias para el agente representante o distribuidor desde el momento en que lleguen a su conocimiento, siempre que sea por carta." | The representative/distributor is FREE to engage in any other class of business or mercantile activity distinct from those performed under the agency/distribution contract, with the sole duty of AVOIDING CONCURRENCE with his principal; the principal may however authorize him for same-class business. When the agent represents or distributes for SEVERAL principals and one introduces a line competitive with another the agent distributes or represents, he must make it known to the respective principals, to conduct the pertinent negotiations on the line. The GENERAL CONDITIONS under which the agent may process proposals or, where applicable, contract may be altered by the principal provided they do not contradict the contract's terms; modifications are BINDING on the agent from the moment they reach his knowledge, provided it is BY LETTER (carta) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 393-394 pp.75-76 (EVID-223; txt PAGE 75-76) |
| LB-019 | Código de Comercio, Art. 395: "A falta de convenio especial, el agente representante o distribuidor percibirá una comisión proporcional a la cuantía del negocio que se realice con su intervención, de acuerdo con los usos del lugar." "Si por culpa del principal no se ejecutare el negocio, en todo o en parte, el agente representante o distribuidor conservará el derecho a reclamar el importe total de la comisión." "Si el agente representante o distribuidor tuviere asignada en forma exclusiva una zona determinada, le corresponderá una comisión por los negocios de igual índole a los encomendados a su agencia que realice el principal o sus enviados en dicha zona, aunque aquel no haya intervenido en los mismos." Art. 396: "El agente representante o distribuidor transmitirá sin dilación al principal las proposiciones que reciba y dará cuenta inmediata de los contratos que realice, cuando estuviere autorizado para ello." "Los pedidos que reciba el agente representante o distribuidor serán obligatorios para el principal desde el momento en que conteste aceptándolos." "El principal no tendrá obligación de dar a conocer los motivos que lo determinen a aceptar o rechazar las proposiciones de contratación." | Absent special agreement, the representative/distributor receives a COMMISSION PROPORTIONAL to the amount of the business realized with his intervention, according to the usos del lugar (local usage). If through the PRINCIPAL's fault the business is not executed, wholly or partly, the agent keeps the right to claim the TOTAL commission. If the agent has an EXCLUSIVE ZONE assigned, he is due a commission on same-kind business that the principal or his enviados (envoys) realize in that zone, even though the agent did not intervene in them. The agent transmits proposals WITHOUT DELAY and accounts immediately for contracts he celebrates when authorized. The pedidos (orders) the agent receives are BINDING on the principal from the moment he replies accepting them. The principal has no duty to disclose the motives determining acceptance or rejection of contracting proposals | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 395-396 p.76 (EVID-223; txt PAGE 76) |
| LB-020 | Código de Comercio, Art. 397: "El contrato de agencia-representación o distribución podrá denunciarse por cualquiera de las partes, por escrito, con tres meses de anticipación." "En caso de terminación del contrato, el agente representante o distribuidor tendrá derecho al valor de las comisiones pendientes, devengadas durante la vigencia del contrato." "Si el principal diere por terminado, modificare o se negare a prorrogar un contrato de agencia representación o distribución, sin que se haya incurrido en alguna de las causales determinadas en el Artículo 398 de este Código, el Agente representante o distribuidor tendrá derecho a que se le indemnice por los perjuicios que se le irroguen." "La indemnización se extiende a: 1º) Los gastos efectuados por el agente representante o distribuidor en beneficio del negocio del cual se le priva, siempre que, debido a la expiración unilateral del contrato, tales gastos no puedan ser recuperados. 2º) El valor de las inversiones en local, equipo, instalaciones, mobiliario y útiles en la medida en que tales inversiones sean únicamente aprovechables para el negocio del cual se le priva. 3º) El valor de las existencias en mercaderías y accesorios, en la medida en que, debido a la expiración del contrato, el agente representante o distribuidor ya no puede continuar vendiéndolas o su venta se haga especialmente difícil. Este valor se calculará tomando en cuenta el costo de adquisición, más los fletes hasta el lugar del establecimiento del agente representante o distribuidor y los impuestos y cargos que éste haya tenido que pagar por tener las existencias en su poder. Pagado el valor de las existencias, el principal que indemniza tendrá derecho a hacerlas suyas. 4º) El monto de la utilidad bruta obtenida por el agente representante o distribuidor, en el ejercicio de la representación o distribución, durante los últimos tres años, o durante el lapso menor en que la haya ejercido. 5º) El valor de los créditos que el agente representante o distribuidor haya concedido a terceros, para pagar el valor de las mercaderías que distribuya. Pagado el valor de los créditos, el principal que indemniza se subrogará en los derechos del agente representante o distribuidor." | The agency-representation/distribution contract may be denounced (terminated on notice) by either party, IN WRITING, with THREE MONTHS' anticipation. Upon termination the agent is entitled to the value of PENDING COMMISSIONS earned during the contract's validity. If the principal terminates, modifies or refuses to renew an agency/distribution contract without any of the causes determined in Art. 398 having been incurred, the agent is entitled to INDEMNIFICATION for the damages caused. The indemnification extends to: 1st) the agent's expenses in benefit of the business of which he is deprived, to the extent they cannot be recovered due to the unilateral expiry of the contract; 2nd) the value of investments in premises, equipment, installations, furniture and implements, to the extent solely exploitable for that business; 3rd) the value of merchandise and accessory inventories, to the extent the agent can no longer sell them or their sale becomes especially difficult — computed on acquisition cost plus fletes (freight) to the agent's establishment and the taxes and charges paid to hold the inventory; once paid, the indemnifying principal may take them as his own; 4th) the amount of GROSS PROFIT obtained in the representation/distribution exercise during the LAST THREE YEARS, or the shorter period exercised; 5th) the value of credits the agent granted third parties to pay for distributed merchandise — once paid, the indemnifying principal is SUBROGATED in the agent's rights | `sv/sources/07_Codigo_Comercio.pdf` | Art. 397 pp.76-77 (EVID-223; txt PAGE 76-77) |
| LB-021 | Código de Comercio, Art. 398: "Para los efectos del artículo anterior, sólo se considerarán justas causas para dar por terminados, modificar o negarse a prorrogar el contrato de agencia representación o distribución las siguientes: a) Incumplimiento del contrato de agencia representación o distribución. b) Fraude de parte del agente representante o distribuidor, sin perjuicio de la sanción penal a que hubiere lugar. c) Ineptitud o negligencia graves del agente representante o distribuidor. d) Disminución continuada de la venta o distribución de los artículos por motivo imputable al agente representante o distribuidor. e) Divulgación de información confidencial, sin perjuicio de la sanción penal y de la indemnización a que hubiere lugar. f) Actos imputables al agente representante o distribuidor que redunden en perjuicio de la introducción, venta o distribución de los productos que le han sido confiados." Art. 399: "Se presume justa causa para que el agente representante o distribuidor pueda dar por terminado su contrato con el principal, con responsabilidad para este último, de conformidad a lo dispuesto en el Art. 397, toda modificación introducida al mismo unilateralmente por el principal que lesione los derechos o intereses del agente representante o distribuidor." Art. 399-A: "Las controversias que se susciten en la aplicación de lo dispuesto en esta Sección, se tramitarán en juicio sumario por los tribunales competentes del domicilio del agente representante o distribuidor." Art. 399-B: "Si el principal fuere extranjero y hubiere sido condenado por sentencia ejecutoriada, no podrá seguir importando los productos o marcas u ofreciendo servicios mientras no le dé debido cumplimiento a la sentencia. Esta restricción cesará, si el principal consigna en el tribunal la cantidad a que fue condenado a pagar o si el beneficiado manifiesta que se ha cumplido dicha sentencia." "El Tribunal a quien corresponda el cumplimiento de la sentencia, deberá librar a petición de parte, oficio a los organismos administrativos competentes, para que den cumplimiento a lo dispuesto en el inciso anterior." | For the purposes of the preceding article, the ONLY just causes to terminate, modify or refuse to renew an agency/distribution contract are: a) breach of the contract; b) fraud on the agent's part (without prejudice to criminal sanction); c) grave ineptitude or negligence of the agent; d) continued decrease of sale or distribution imputable to the agent; e) disclosure of confidential information (without prejudice to criminal sanction and indemnification); f) acts imputable to the agent that redound to the prejudice of the introduction, sale or distribution of the entrusted products. Art. 399: every modification the principal introduces UNILATERALLY that injures the agent's rights or interests is PRESUMED just cause for the agent to terminate with responsibility for the principal, per Art. 397. Art. 399-A: controversies under this Section proceed in JUICIO SUMARIO (summary proceeding) before the competent courts of the AGENT'S DOMICILE. Art. 399-B: a FOREIGN principal condemned by executed judgment may not continue importing the products or marks, or offering the services, until it duly complies with the judgment; the restriction ceases if the principal consigns in the court the condemned amount or the beneficiary states the judgment is fulfilled; the court libers office to the competent administrative organisms to enforce | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 398, 399, 399-A, 399-B p.77 (EVID-223; txt PAGE 77) |
| LB-022 | Código de Comercio, Art. 400: "Los agentes intermediarios no obligan a las partes entre sí. Los contratos que se celebren con intervención de ellos, se comprobarán y ejecutarán conforme a su naturaleza, sin atribuir a los intermediarios función pública alguna. Puede ser personas naturales o jurídicas." Art. 402: "Los agentes intermediarios están obligados a: 1) Dar a conocer a las partes con imparcialidad todos los detalles y circunstancias del negocio. 2) Responder a sus clientes de la autenticidad de los títulos relacionados con la operación en que intervienen. 3) Abstenerse de promover negocios en que intervengan personas de insolvencia notoria o cuya incapacidad les sea conocida, y en general las operaciones contrarias a las leyes." Art. 403: "Los agentes intermediarios no tienen la representación de sus clientes. Quien actuare como apoderado perderá la calidad de intermediario." | Intermediary agents do NOT bind the parties to each other; contracts celebrated with their intervention are proven and executed according to their nature, attributing no public function to the intermediaries. They may be natural or juridical persons. Intermediaries are obliged to: 1) make known to the parties IMPARTIALLY all details and circumstances of the business; 2) answer to their clients for the AUTHENTICITY of the titles related to the operation; 3) abstain from promoting business involving notoriously insolvent persons or persons whose incapacity is known to them, and in general operations contrary to the laws. Intermediaries have NO representation of their clients: whoever acts as apoderado LOSES the character of intermediary | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 400, 402-403 p.78 (EVID-223; txt PAGE 78; Art. 401 DEROGADA) |
| LB-023 | Código de Comercio, Art. 404: "El derecho del intermediario a la remuneración convenida, queda sujeto a la condición de que el contrato se celebre. Si el contrato se estipula bajo condición suspensiva, el intermediario solamente podrá cobrar su remuneración si la condición se cumple." "Cada contratante responderá por la mitad de la remuneración convenida, salvo acuerdo diverso entre ellos." "A falta de convenio se deberá pagar la comisión usual en el lugar en que se celebró el contrato." Art. 405: "El intermediario tiene derecho a cobrar la remuneración, siempre que el negocio convenido se lleve a cabo dentro del plazo de seis meses, contado a partir de la aceptación de las partes, sobre las bases por él propuestas." Art. 406: "El intermediario carece de derecho a exigir que se le reembolsen los gastos hechos al ejercitar su intermediación, salvo pacto en contrario." Art. 407: "Siempre que el intermediario omita dar a conocer a una de las partes el nombre de la otra, quedará responsable para con esa parte de los daños y perjuicios que se deriven de la falta de celebración del contrato." | The intermediary's right to the agreed remuneration is subject to the CONDITION THAT THE CONTRACT IS CELEBRATED; under a suspensive condition, the intermediary may collect only if the condition fulfills. Each contracting party answers for HALF the agreed remuneration, save diverse agreement between them. Absent agreement, the USUAL commission of the place of celebration is due. The intermediary may collect the remuneration whenever the agreed business is carried out within SIX MONTHS counted from the parties' acceptance on the bases he proposed. The intermediary has NO right to demand reimbursement of expenses made in exercising the intermediation, save contrary pact. Whenever the intermediary omits to make known to one party the other's NAME, he is liable to that party for the damages deriving from the contract's non-celebration | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 404-407 p.78 (EVID-223; txt PAGE 78) |
| LB-024 | Código de Comercio, Art. 408: "Todo intermediario deberá llevar: I- Un registro en que anotará, en el momento en que se cierre cada operación, el objeto y las bases esenciales del contrato. II- Un libro diario de operaciones para anotar en detalle, con las formalidades establecidas para la contabilidad mercantil, todas las condiciones relativas a cada una de las operaciones que se lleven a cabo con su mediación." "El intermediario está obligado a proporcionar a las partes que lo soliciten, una copia exacta de las anotaciones que el presente artículo indica." Art. 409: "La autoridad judicial podrá, de oficio, exigir al intermediario que exhiba los documentos a que se refiere el artículo anterior, para cotejar con las respectivas anotaciones las copias que el agente haya entregado a las partes. También podrá exigir la presentación de la correspondencia cruzada con las partes." "Estos documentos constituyen un principio de prueba por escrito, si reúnen las condiciones del Art. 1582 C." Art. 410: "Los intermediarios no podrán reclamar contra sus clientes, sin presentar a la autoridad que corresponda los documentos a que se refiere el artículo 408." | Every intermediary must keep: I- a registro (register) noting, at the moment each operation closes, the object and essential bases of the contract; II- a libro diario de operaciones (daily operations book) recording in detail, WITH THE FORMALITIES ESTABLISHED FOR MERCANTILE ACCOUNTING, all the conditions relative to each operation carried out through his mediation. The intermediary must furnish the requesting parties an EXACT COPY of the annotations this article indicates. The judicial authority may, ex officio, demand exhibition of those documents to collate the copies delivered to the parties with the respective annotations, and also the crossed correspondence with the parties; those documents constitute a beginning of written proof if they meet the conditions of Art. 1582 C. Intermediaries may NOT claim against their clients without presenting to the corresponding authority the documents of Art. 408 | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 408-410 pp.78-79 (EVID-223; txt PAGE 78-79) |

## 3. Functional Requirements

### 3.1 Factores (Arts. 365-377)

- **SV-CML-FR-098:** The system shall model the *factor* role and its
  Art. 366 GENERAL authority default: the factor is whoever directs, on
  another's account, an empresa, a special branch of it or an
  establishment of it (Art. 365); the SOLE APPOINTMENT authorizes all
  operations concerning the object of the enterprise or establishment
  directed — deemed executed in the principal's name and account even
  when the factor did not so express it, transgressed instructions or
  committed abuse of trust, provided the contracts fall on objects
  within the giro and traffic of the enterprise (or, being of another
  nature, the factor acted on the principal's order or the principal
  approved the gestión expressly or by positive facts). Limits recorded
  on the factor's authority profile shall be treated as INOPPOSABLE to
  third parties unless third-party knowledge is recorded (knowledge
  flag on the operation), and the viajero/dependiente/agent roles below
  distinguish themselves from the factor precisely by NOT carrying this
  general authority. (LB-001; EVID-223)
- **SV-CML-FR-099:** The system shall track the Art. 367 registry
  discipline for factor appointments on the factor's authority record:
  the nombramiento and its later modifications are inscribed in the
  Registro de Comercio where the empresa (and, where applicable, the
  establishment) is registered — recorded via the registry-entry model
  of SV-CML-FR-013, kind poder_nombramiento_credencial, subkind
  nombramiento_factor per SV-CML-FR-014 (consumed by id); the
  TERMINACIÓN of the factor's powers is ALWAYS inscribable and shall be
  recorded as a revocación entry EVEN when the appointment itself was
  never registered; and the absence of inscription shall surface as the
  limited-effects state (the acts produce only the effects expressly
  stated in the remaining articles of the chapter — i.e. the default
  rules of FR-098/FR-100 still govern, but the publicity effects do not
  run). (LB-002; EVID-223)
- **SV-CML-FR-100:** The system shall implement the Art. 368
  mandate-form rule: the principal who designated the factor is
  responsible for the factor's acts and obligations in the terms of
  Art. 371 (FR-102); an EXPRESS mandate that was neither granted in
  writing NOR inscribed shall be computed as DEEMED-GENERAL — for all
  acts of the branch of commerce in the factor's charge — with no
  limitation opposable to third parties unless third-party knowledge is
  recorded at the operation; and where there are SEVERAL principals,
  the factor's acts bind them SOLIDARILY (a sociedad-principal's socio
  responsibility follows the sociedad's nature — society-type rules are
  `04_society-types.md` territory, consumed by id). (LB-003; EVID-223)
- **SV-CML-FR-101:** The system shall record the Art. 369-370
  signature semantics on factor-executed documents: the factor acts in
  the principal's NAME, so expressing it in the documents subscribed in
  that character; and when the factor contracts expressly in his OWN
  name but the counterparty demonstrates the contract was made on the
  principal's account, the counterparty may direct its action against
  the factor OR the principal, who are SOLIDARILY responsible —
  surfaced as an optional-defendant (solidarity) marker on the
  document/operation record, informational for liability routing (no
  computation derives). (LB-004; EVID-223)
- **SV-CML-FR-102:** The system shall implement the Art. 371
  post-revocation validity rule as a power-state computation: acts and
  contracts celebrated by the factor AFTER revocation of his power (or
  after cessation by ENAJENACIÓN — alienation — of the establishment he
  directed) remain VALID until they reach the factor's notice by a
  legitimate means (notice date tracked); and towards THIRD PARTIES the
  acts remain equally valid while the revocation or alienation is not
  INSCRIBED in the Registro de Comercio — the third-party-validity flag
  clears only upon recording the revocación/enajenación registry entry
  (FR-099) or the legitimate-notice event, whichever the operative
  audience requires (notice for the factor, inscription for third
  parties). (LB-005; EVID-223)
- **SV-CML-FR-103:** The system shall provide the Art. 372-377 factor
  governance-and-discipline defaults as authority-profile metadata:
  (a) several factores are presumed to decide BY MAJORITY unless the
  appointment expresses (expressly or tacitly) independence in all
  business or in some of exclusive competence (decision-mode field);
  (b) a profit interest in the giro gives the factor NO veto over
  operations ordered by the principal; (c) the factor answers to the
  principal for damages caused by his culpa in the gestión of his
  charge (liability note); (d) the factor is SOLIDARILY responsible
  with the principal for compliance with this Code and the other laws
  on the exercise of commerce or the exploitation of the branch in his
  charge (compliance-exposure note, informational); (e) the Art. 375
  self-dealing prohibition — the factor may not trade on his own
  account nor interest himself, in his own or a third party's name, in
  business of the same kind as the principal's, absent EXPRESS WRITTEN
  authorization — with the principal's appropriation window (make the
  operation his own within FIFTEEN DAYS from knowledge, computed) and
  the link to mandate termination; and (f) the Art. 377 expiry-cause
  catalog — I. principal-side: a) fraude o abuso de confianza · b)
  negotiation contrary to contractual or legal prohibitions · c) mala
  conducta pública o privada; II. factor-side: a) principal's failure
  to pay estipendios punctually or breach of remuneration clauses · b)
  malos tratamientos personales — as the reason catalog for terminating
  a factor power record beyond normal mandate termination.
  (LB-006; LB-007; EVID-223)

### 3.2 Dependientes and viajeros (Arts. 378-383)

- **SV-CML-FR-104:** The system shall model the *dependiente*
  bind-the-principal defaults of Arts. 378-379: the dependiente OBLIGA
  al principal, and his acts bind the principal in ALL the operations
  in his charge by reason of the post he occupies before the public
  (post-based authority scope, not appointment-based general authority
  — the contrast with FR-098 is the design point); and sales
  dependientes may collect the price of sold merchandise WITHIN the
  establishment by default — the system shall invert that collection
  authority per establishment only when the perception is reserved to a
  *caja* or special department AND made known to the public by an
  announcement posted in a visible place (caja-reserve flag + posting
  evidence on the establishment record; the rule extends to service
  enterprises and their dependientes).
  (LB-008; LB-009; EVID-223)
- **SV-CML-FR-105:** The system shall implement the Art. 378
  plazos/descuentos authorization rule: granting plazos (credit terms)
  or descuentos (discounts) requires SPECIAL authorization on the
  dependiente's authority profile; without it the operation remains
  VALID towards the buyer (no customer-side invalidation — the sale
  stands) but the dependiente is liable to the principal for resulting
  damages — surfaced as an unauthorized-credit-term/discount warning on
  the operation with the internal-liability marker, never as a blocking
  validation. (LB-008; EVID-223)
- **SV-CML-FR-106:** The system shall implement the Art. 378
  OUTSIDE-sale/collection rule: to sell or collect OUTSIDE the
  establishment, a dependiente shall exhibit a WRITTEN AUTHORIZATION
  accompanied by an identity document, OR deliver against payment the
  *recibo o la factura* bearing the *firma y sello* (signature and
  stamp) of the principal or its representatives — recorded as the
  outside-operation authority package (authorization document
  reference + ID, or the stamped recibo/factura link) whose absence
  flags the operation as outside-authority (defect warning with the
  two statutory cures identified); and dependientes rendering services
  outside the enterprise's premises are classified *dependientes
  viajeros* (travelling clerks). (LB-008; EVID-223)
- **SV-CML-FR-107:** The system shall implement the viajero authority
  defaults and the dependiente prohibitions: (a) Art. 380 — absent
  proven EXPRESS authorization, the dependiente viajero may NOT collect
  the ADVANCED price of merchandise when not delivering it at the
  moment of celebrating the operation, NOR grant esperas, plazos,
  quitas or descuentos; but he CAN receive purchase orders
  (*órdenes de pedido*) and agree guarantees or securities he deems
  prudent in the principal's interest (order-taking + guarantee flags
  default-true; advance-collection and credit-term flags default-
  false); (b) Art. 381 — the viajero may NOT subscribe obligation
  documents as the principal's apoderado absent mandate, and when
  mandated must indicate the full commercial name and domicile under
  which the principal operates (document-signature guard); (c)
  Art. 382 — the dependiente prohibitions: no own- or third-party-
  account isolated acts or enterprises in the same matters similar to
  the principal's commerce, and no divulging of clientela, economic
  situation or other reserved principal information (conflict/
  confidentiality exposure flags, informational); (d) Art. 383 — the
  factor provisions apply to dependientes insofar as COMPATIBLE (the
  FR-098/FR-100/FR-103 semantics import with the viajero/dependiente
  restrictions as the compatibility filter). (LB-010; LB-011; EVID-223)

### 3.3 Agentes dependientes (Arts. 384-391)

- **SV-CML-FR-108:** The system shall model the *agente dependiente*
  role and its Art. 385 authority defaults: the agent charged with
  promoting business in a determined plaza or region on a principal's
  account (principal domiciled in the Republic or abroad) and
  transmitting proposals for acceptance, SUBORDINATED to the principal;
  absent EXPRESS mandate the agent has NO faculty to celebrate
  contracts, make collections, or grant discounts, quitas or credit
  terms on the principal's account — but MAY receive complaints or
  claims for quality/quantity defects and obtain fianzas guaranteeing
  the applicant's obligations upon delivery of the goods he ordered;
  and the insurance-family credencial variant: agents of seguros,
  capitalización, ahorro y préstamos, ahorro para adquisición de bienes
  and similar enterprises must present the accrediting credential, are
  PRESUMED empowered to celebrate contracts, receive applications,
  reject proponents' written declarations, collect due premiums and
  verify siniestros (claims) — unless the enterprise expressly limited
  the faculties in the credential (never to the point of making the
  agency's exercise impossible) — and, absent express credencial
  statement, may NOT modify the contract text figuring in the
  application (credentialed-authority profile for that sector).
  (LB-012; EVID-223)
- **SV-CML-FR-109:** The system shall enforce the Art. 386 plaza
  exclusivity default in BOTH directions, salvo pacto en contrario: a
  principal may NOT engage a second agent in the same plaza or region
  for the same ramo of commerce while a contract with another agent is
  in force — that contract being DEEMED EXCLUSIVE (creation of a second
  same-plaza/same-ramo engagement for the same principal raises a
  blocking exclusivity validation unless an express contrary pact is
  recorded); and an agent may NOT assume the charge of promoting or
  handling affairs of OTHER principals (second-principal engagement
  raises the mirrored validation). (LB-013; EVID-223)
- **SV-CML-FR-110:** The system shall implement the Art. 387/389/390
  commission economics of the dependent agent: (a) when the principal
  promotes operations — by himself or through another — in a plaza or
  region where he has an EXCLUSIVE agent, that agent is owed the
  participations that would have corresponded had the agent promoted
  the business (zone-exclusivity accrual on principal-side deals);
  (b) salvo contractual stipulation, the agent bears at his own expense
  the expenses and taxes of the agency's exercise, and his remuneration
  is computed as a PERCENTAGE on the payments each client actually
  makes on operations in which the agent intervened (payment-based
  accrual basis, not order-based); and (c) if the principal DESISTS
  from any contract celebrated by the agent, or MODIFIES it, the agent
  is entitled to the stipulated percentage AS IF the operation had been
  carried out on the bases he agreed (desistimiento/modification
  protection accrual). Commission rates and percentage values are
  contract/config data — no statutory rate exists (→ OQ-002).
  (LB-014; EVID-223)
- **SV-CML-FR-111:** The system shall implement the Art. 388/391
  book-and-settlement duties of the agent: a *libro especial* (special
  book) recording, with the proper separation, the operations relative
  to EACH PRINCIPAL, with the details distinguishing the pedidos and
  goods corresponding to each (one book-segment per principal; register
  record instantiated via `02_accounting-books.md` SV-CML-FR-025
  Art. 440 discipline flags, consumed by id, and retained under its
  SV-CML-FR-028 matrix row a) — plus the information duty to principals
  (interesting-information flag on operations); and the default
  remuneration settlement: absent contrary stipulation, remuneration is
  paid AT THE END OF EACH MONTH against the remission of the respective
  account DULY DOCUMENTED (monthly settlement cycle gated on the
  documented account — payroll-side integration = SV-PAY-FR-002 by id,
  §2 note). (LB-015; LB-016; EVID-223)

### 3.4 Agentes representantes o distribuidores (Arts. 392-399-B)

- **SV-CML-FR-112:** The system shall model the *agente representante o
  distribuidor* channel contract of Art. 392: a natural or juridical
  person designated BY CONTRACT, CONTINUOUSLY (en forma contínua [sic]
  as printed), with or without legal representation, for the
  agency-representation or distribution of determined products or
  services in the country; the channel form may be EXCLUSIVE or any
  other form the parties agree (exclusivity here is CONTRACTUAL, unlike
  the Art. 386 default of FR-109); and the instruction-following
  liability limit: an agent not acting on his own account and risk but
  following the principal's instructions is NOT responsible for the
  principal's non-performance — his responsibility limiting itself to
  strict compliance with the instructions received (instruction-bound
  flag distinguishing the instruction-following distributor from the
  own-account distributor).
  (LB-017; EVID-223)
- **SV-CML-FR-113:** The system shall record the Art. 393-394
  relationship mechanics: the agent is FREE to engage in any OTHER
  class of business or mercantile activity, with the sole duty of
  AVOIDING CONCURRENCE with his principal (same-class business requires
  the principal's authorization; multi-principal competitive-line
  introductions must be made known to the respective principals —
  disclosure tracking); and the general conditions under which the
  agent may process proposals or contract may be ALTERED by the
  principal provided they do not contradict the contract's terms,
  modifications becoming BINDING on the agent from the moment they
  reach his knowledge, PROVIDED it is BY LETTER (carta) — the system
  shall track the modification channel (letter/mail record) and the
  knowledge date as the binding anchor. (LB-018; EVID-223)
- **SV-CML-FR-114:** The system shall implement the Art. 395-396
  commission-and-order defaults of the representative/distributor:
  (a) absent special agreement, a COMMISSION PROPORTIONAL to the amount
  of the business realized with the agent's intervention, per the usos
  del lugar (local usage — config-gap, no shipped rate, → OQ-002);
  (b) if through the PRINCIPAL's fault the business is not executed,
  wholly or partly, the agent keeps the right to claim the TOTAL
  commission; (c) with an EXCLUSIVE ZONE assigned, the agent is due a
  commission on same-kind business realized by the principal or his
  enviados in that zone EVEN WITHOUT the agent's intervention
  (exclusive-zone accrual on principal's own deals); (d) the agent
  transmits proposals WITHOUT DELAY and accounts immediately for
  contracts when authorized; (e) the pedidos the agent receives are
  BINDING on the principal from the moment he replies ACCEPTING them
  (order-acceptance semantics: agent-originated orders become
  obligations at the principal's acceptance reply — tracked as the
  binding event on the order); and (f) the principal has NO duty to
  disclose motives for accepting or rejecting proposals.
  (LB-019; EVID-223)
- **SV-CML-FR-115:** The system shall implement the Art. 397
  termination-and-indemnification machinery: (a) the contract may be
  denounced by either party IN WRITING with THREE MONTHS' anticipation
  (notice-period tracking; a termination recorded without the 3-month
  written notice and without an Art. 398 just cause flags
  unjustified-termination exposure); (b) upon termination the agent is
  entitled to the value of PENDING COMMISSIONS earned during the
  contract's validity (accrued-unpaid commission settlement); (c) if
  the principal terminates, modifies or refuses to renew WITHOUT an
  Art. 398 just cause having been incurred (FR-116 catalog), the agent
  is entitled to INDEMNIFICATION extending to the 5-head scale,
  reproduced VERBATIM as the computation worksheet basis:

  | Head | Verbatim (Spanish) | Gloss |
  |------|--------------------|-------|
  | 1º) | "Los gastos efectuados por el agente representante o distribuidor en beneficio del negocio del cual se le priva, siempre que, debido a la expiración unilateral del contrato, tales gastos no puedan ser recuperados." | Expenses made in benefit of the business of which the agent is deprived, to the extent unrecoverable due to the unilateral expiry |
  | 2º) | "El valor de las inversiones en local, equipo, instalaciones, mobiliario y útiles en la medida en que tales inversiones sean únicamente aprovechables para el negocio del cual se le priva." | Value of investments in premises, equipment, installations, furniture and implements, to the extent solely exploitable for that business |
  | 3º) | "El valor de las existencias en mercaderías y accesorios, en la medida en que, debido a la expiración del contrato, el agente representante o distribuidor ya no puede continuar vendiéndolas o su venta se haga especialmente difícil. Este valor se calculará tomando en cuenta el costo de adquisición, más los fletes hasta el lugar del establecimiento del agente representante o distribuidor y los impuestos y cargos que éste haya tenido que pagar por tener las existencias en su poder. Pagado el valor de las existencias, el principal que indemniza tendrá derecho a hacerlas suyas." | Value of merchandise/accessory inventory the agent can no longer sell (or whose sale becomes especially difficult), at acquisition cost + freight to the agent's establishment + taxes/charges paid to hold it; once paid, the indemnifying principal may take the goods |
  | 4º) | "El monto de la utilidad bruta obtenida por el agente representante o distribuidor, en el ejercicio de la representación o distribución, durante los últimos tres años, o durante el lapso menor en que la haya ejercido." | Gross profit of the last three years of the representation/distribution (or the shorter period exercised) |
  | 5º) | "El valor de los créditos que el agente representante o distribuidor haya concedido a terceros, para pagar el valor de las mercaderías que distribuya. Pagado el valor de los créditos, el principal que indemniza se subrogará en los derechos del agente representante o distribuidor." | Value of credits the agent granted third parties for distributed merchandise; once paid, the principal is subrogated in the agent's rights |

  The system provides the 5-head worksheet as a computation surface
  (inputs recorded, heads summed; head 3 carrying the principal-takes-
  goods flag, head 5 the subrogation flag) — quantification inputs
  (gross utility, costs) are accounting data, never invented
  (→ OQ-002). (LB-020; EVID-223)
- **SV-CML-FR-116:** The system shall implement the Art. 398/399/399-A/
  399-B just-cause and enforcement layer: (a) the ONLY just causes for
  the principal to terminate, modify or refuse to renew are the
  six-literal catalog — a) incumplimiento del contrato · b) fraude ·
  c) ineptitud o negligencia graves · d) disminución continuada de la
  venta imputable al agente · e) divulgación de información
  confidencial · f) acts imputable to the agent prejudicing the
  introduction, sale or distribution of the entrusted products —
  recorded as the termination reason catalog gating FR-115's
  indemnity; (b) Art. 399 — every UNILATERAL principal modification
  injuring the agent's rights or interests is PRESUMED just cause for
  the AGENT to terminate with the principal responsible per Art. 397;
  (c) Art. 399-A — controversies under this Section proceed in juicio
  sumario before the competent courts of the AGENT'S DOMICILE (forum
  metadata, informational); and (d) Art. 399-B — a FOREIGN principal
  condemned by executed judgment may not continue importing the
  products or marks or offering the services until due compliance,
  the bar ceasing on consignment of the condemned amount in the court
  or the beneficiary's statement of fulfillment — recorded as an
  import-bar status on the foreign principal's record (informational
  flag; the enforcement organisms are administrative/customs side,
  outside this corpus → OQ-003). (LB-021; EVID-223)

### 3.5 Agentes intermediarios (Arts. 400-410)

- **SV-CML-FR-117:** The system shall model the *agente intermediario*
  with the Art. 400/402/403 no-representation defaults: the
  intermediary does NOT bind the parties to each other (contracts
  celebrated with his intervention are proven and executed according
  to their nature, no public function attributed); the intermediary
  has NO representation of his clients — whoever acts as apoderado
  LOSES the character of intermediary (role exclusivity guard: a
  representation mandate on an intermediary record raises the
  role-loss flag); and the three statutory duties as compliance
  exposure: impartial disclosure of all details and circumstances of
  the business; answerability to clients for the authenticity of the
  titles related to the operation; and abstention from promoting
  business involving notoriously insolvent persons or known
  incapables, or operations contrary to the laws (Art. 401 DEROGADA —
  §2 provenance; no FR derives from it).
  (LB-022; EVID-223)
- **SV-CML-FR-118:** The system shall implement the Art. 404-407
  remuneration defaults of the intermediary as settlement conditions:
  the right to the agreed remuneration is CONDITIONED on the contract
  being celebrated (and, under a suspensive condition, on the
  condition fulfilling — no settlement accrues before the condition
  event); each contracting party answers for HALF the agreed
  remuneration salvo acuerdo diverso (50/50 default split); absent
  agreement, the USUAL commission of the place of celebration applies
  (config-gap — no shipped rate, → OQ-002); the remuneration right
  subsists whenever the agreed business is carried out within SIX
  MONTHS from the parties' acceptance on the bases the intermediary
  proposed (six-month eligibility window computed from acceptance);
  the intermediary has NO right to demand reimbursement of expenses
  salvo pacto en contrario (expense-reimbursement default-false); and
  omitting to disclose one party's name to the other makes the
  intermediary liable for damages from the contract's non-celebration
  (name-disclosure tracking on the intermediation record).
  (LB-023; EVID-223)
- **SV-CML-FR-119:** The system shall implement the Art. 408-410
  intermediary books and proof discipline: every intermediary keeps
  (I) a *registro* noting, at the moment each operation CLOSES, the
  object and essential bases of the contract, and (II) a *libro diario
  de operaciones* recording in detail, with the FORMALITIES ESTABLISHED
  FOR MERCANTILE ACCOUNTING (castellano/USD/in-country + legalization
  + no-alteration, all via `02_accounting-books.md` SV-CML-FR-025
  Art. 440 extension and its SV-CML-FR-028 retention matrix row a —
  consumed by id, never restated), all conditions of each operation
  carried out through his mediation; the intermediary must furnish
  requesting parties an EXACT COPY of those annotations (copy-exact
  duty tracked); the judicial authority may ex officio demand
  exhibition of the documents (and the crossed correspondence) for
  collation, the documents constituting a beginning of written proof
  if they meet Art. 1582 C. (exhibition/probatory metadata); and
  intermediaries may NOT claim against their clients without
  presenting the Art. 408 documents to the corresponding authority —
  a claim record on an intermediary matter without the book/registro
  references raises the incomplete-claim warning.
  (LB-024; EVID-223)

## 4. Data Model

Layer semantics: the auxiliares regime is Odoo-native — all entities live
in the client (wave default `odoo`; see §5). Registry inscription, notice
and judicial acts are EXTERNAL events: the system tracks dates,
references and effect states; it never emulates the Registro de Comercio
or the courts. The employment side of the same persons is payroll-wave
territory (§2 note) — the res.partner authority profile here links to,
never duplicates, hr/payroll records.

**Auxiliary role + authority profile (on res.partner):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner | sv_cml_auxiliary_kind | select | none · factor · dependiente · dependiente_viajero · agente_dependiente · agente_representante_distribuidor · intermediario (persona natural o jurídica, Arts. 392/400) | FR-098, FR-104, FR-106, FR-108, FR-112, FR-117 |
| res.partner (factor) | sv_cml_factor_authority | select | general_from_appointment (Art. 366 default) · limited (third-party-opposable only with knowledge flag) | FR-098 |
| res.partner (factor) | sv_cml_factor_mandate_form | select | written_inscribed · express_unwritten (deemed general, Art. 368) | FR-100 |
| res.partner (factor) | sv_cml_factor_principals | many2many res.partner | several principals ⇒ solidary responsibility | FR-100 |
| res.partner (factor) | sv_cml_factor_decision_mode | select | majority_presumed · independent_all · independent_exclusive (Art. 372) | FR-103 |
| res.partner (factor) | sv_cml_factor_self_dealing_auth | boolean + document ref | express WRITTEN authorization (Art. 375); appropriation window = knowledge + 15 days | FR-103 |
| res.partner (factor) | sv_cml_factor_power_state | select + dates | vigente · revoked (notice date) · alienated · expired (Art. 377 reason catalog: I.a fraude_abuso · I.b prohibited_negotiation · I.c mala_conducta · II.a estipendio/remuneration_breach · II.b malos_tratos) | FR-102, FR-103 |
| res.partner (factor) | sv_cml_factor_third_party_valid | computed boolean | TRUE while revocation/enajenación not inscribed (registry link below) | FR-099, FR-102 |
| res.partner (dependiente) | sv_cml_collect_in_store · sv_cml_discount_credit_authorized | boolean | Art. 378 defaults; special authorization flag for plazos/descuentos | FR-104, FR-105 |
| res.company (establishment) | sv_cml_caja_reserve_posted | boolean + announcement ref | reserve to caja/special department + public announcement in visible place | FR-104 |
| res.partner (dependiente) | sv_cml_outside_auth_package | document refs | written authorization + identity document, OR stamped recibo/factura (firma y sello) | FR-106 |
| res.partner (viajero) | sv_cml_can_take_orders · sv_cml_can_pact_guarantees · sv_cml_advance_collection · sv_cml_apoderado_mandate | boolean | Art. 380-381: orders+guarantees default TRUE; advance collection / credit terms / apoderado signature default FALSE absent express mandate | FR-107 |
| res.partner (dependiente) | sv_cml_noncompetite_confidentiality | flags | Art. 382 prohibitions — compliance exposure, informational | FR-107 |
| res.partner (agente dependiente) | sv_cml_agent_authority | flags | no contracts/collections/discounts/quitas/plazos absent express mandate; complaints + fianzas OK; credentialed variant (seguros family) with presumption set | FR-108 |

**Agency contracts, commissions and indemnity:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.agency.contract | kind | select | agente_dependiente · agente_representacion · distribucion (continuous, by contract, Art. 392) | FR-108, FR-112 |
| l10n_sv_commerce.agency.contract | principal_id · agent_id | many2one res.partner | principal may be domiciled abroad (Art. 384) | FR-108 |
| l10n_sv_commerce.agency.contract | plaza · region · ramo | char/select | exclusivity dimensions (same plaza/region/ramo) | FR-109 |
| l10n_sv_commerce.agency.contract | exclusive | boolean | agente dependiente: TRUE by default (Art. 386); representante/distribuidor: contractual (Art. 392); exclusive-zone flag for Art. 395-III | FR-109, FR-112, FR-114 |
| l10n_sv_commerce.agency.contract | instruction_bound | boolean | Art. 392-II liability limit | FR-112 |
| l10n_sv_commerce.agency.contract | modification_channel · known_on | select · date | carta (letter) + knowledge date = binding anchor (Art. 394) | FR-113 |
| l10n_sv_commerce.agency.contract | notice_period_months | const 3 | Art. 397 written notice; unjustified termination without it ⇒ indemnity | FR-115 |
| l10n_sv_commerce.agency.contract | state · termination_reason | select | in_force · noticed · terminated (just_cause catalog a-f, Art. 398 · presumed 399 · normal) | FR-115, FR-116 |
| l10n_sv_commerce.agency.commission | basis | select | percentage_on_client_payments (Art. 389) · proportional_usos (Art. 395-I) · contractual · usual_place (Art. 404-III) | FR-110, FR-114, FR-118 |
| l10n_sv_commerce.agency.commission | accrual_event | select | client_payment · business_realized · principal_culpa_total (Arts. 390/395-II) · exclusive_zone_deal (Arts. 387/395-III) · contract_celebrated (Art. 404, intermediario) | FR-110, FR-114, FR-118 |
| l10n_sv_commerce.agency.commission | settlement_cycle | select | monthly_against_documented_account (Art. 391 default) · contractual · six_month_window (Art. 405, intermediario) | FR-111, FR-118 |
| l10n_sv_commerce.agency.commission | split | select | single_payer · half_each (Art. 404-II default, intermediario) | FR-118 |
| l10n_sv_commerce.agency.indemnity | heads 1-5 | monetary + flags | Art. 397 scale (FR-115 verbatim table); head 3 = cost+fletes+impuestos with principal_takes_goods; head 5 = credits with subrogation | FR-115 |
| l10n_sv_commerce.agency.contract (intermediario link) | import_bar_status | select | none · barred_until_compliance · lifted_consignment · lifted_beneficiary_statement (Art. 399-B, foreign principal — informational) | FR-116 |
| l10n_sv_commerce.book | register_kind | select (extended) | agente_libro_especial (per-principal separation, Art. 388) · intermediario_registro (Art. 408-I) · intermediario_diario (Art. 408-II) — discipline flags via SV-CML-FR-025 (by id) | FR-111, FR-119 |
| l10n_sv_commerce.registry.entry | link | consumed | nombramiento_factor / revocación entries per SV-CML-FR-013/014 (by id); presentation anchor per SV-CML-FR-016 | FR-099, FR-102 |

## 5. Odoo Mapping

Layer semantics for this wave: the auxiliares regime is Odoo-native
(res.partner authority profiles, agency contracts, commission/indemnity
records, statutory books) — every FR maps `odoo`; none touch DTE
generation/transformation (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2), so no `saas` rows are
introduced. Model names are stable across Odoo 17/18/19/20; no
version-specific behavior is required by this file. Commission settlement
postings reuse the payroll interface pointer (SV-PAY-FR-002 by id) for
the salary-integration side; no payroll computation lives here.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-098 | odoo | res.partner | sv_cml_auxiliary_kind, sv_cml_factor_authority | Art. 366 general-authority default; limits third-party-opposable only with knowledge flag |
| FR-099 | odoo | l10n_sv_commerce.registry.entry + res.partner | nombramiento_factor/revocación kinds | Consumes SV-CML-FR-013/014 by id; terminación ALWAYS inscribable; limited-effects state when uninscribed |
| FR-100 | odoo | res.partner | sv_cml_factor_mandate_form, sv_cml_factor_principals | Express-unwritten/uninscribed mandate ⇒ deemed general vs third parties; several principals solidary |
| FR-101 | odoo | res.partner (document metadata) | signature-character + optional-defendant marker | Art. 369-370 semantics; informational liability routing |
| FR-102 | odoo | res.partner | sv_cml_factor_power_state, sv_cml_factor_third_party_valid | Post-revocation acts valid until legitimate notice (factor) / inscription (third parties) |
| FR-103 | odoo | res.partner | decision_mode, self_dealing_auth, power_state reasons | Arts. 372-377: majority presumption, no-veto, culpa damages, Code solidarity, self-dealing ban + 15-day appropriation, expiry catalog |
| FR-104 | odoo | res.partner + res.company | collection flags, sv_cml_caja_reserve_posted | Post-based binding (Art. 379); in-store collection default inverted only by posted caja-reserve |
| FR-105 | odoo | res.partner + sale.order/account.move | sv_cml_discount_credit_authorized | Unspecial plazo/descuento: valid vs buyer, internal-liability warning — never blocking |
| FR-106 | odoo | res.partner | sv_cml_outside_auth_package | Written authorization + ID OR stamped recibo/factura; absence ⇒ outside-authority defect warning |
| FR-107 | odoo | res.partner | viajero + prohibition flags | Art. 380 order/guarantee TRUE defaults; advance-collection/credit-terms/apoderado FALSE defaults; Art. 382 exposure flags; Art. 383 factor-rules compatibility |
| FR-108 | odoo | res.partner + l10n_sv_commerce.agency.contract | agent_authority flags | No contract/collection/discount/quita/plazo absent express mandate; complaints+fianzas OK; credentialed seguros-family variant |
| FR-109 | odoo | l10n_sv_commerce.agency.contract | plaza/region/ramo + exclusive (default TRUE) | Blocking validation on second same-plaza/same-ramo agent or second principal, salvo pacto en contrario |
| FR-110 | odoo | l10n_sv_commerce.agency.commission | accrual_event | Exclusive-zone participations on principal's own deals; payment-based percentage; desistimiento/modification protection |
| FR-111 | odoo | l10n_sv_commerce.book + agency.commission | agente_libro_especial; monthly documented-account cycle | Discipline flags via SV-CML-FR-025; retention via SV-CML-FR-028 row a (by id) |
| FR-112 | odoo | l10n_sv_commerce.agency.contract | kind, exclusive (contractual), instruction_bound | Continuous designation by contract; Art. 392-II instruction-following liability limit |
| FR-113 | odoo | l10n_sv_commerce.agency.contract | modification_channel (carta) + known_on | Non-concurrence freedom/duty; competitive-line disclosure; modifications binding from carta knowledge |
| FR-114 | odoo | l10n_sv_commerce.agency.commission + sale.order | basis + acceptance event | Usos del lugar rate = config-gap (OQ-002); principal-culpa total commission; exclusive-zone accrual; pedido binding at acceptance reply |
| FR-115 | odoo | l10n_sv_commerce.agency.indemnity | 5-head worksheet | 3-month written notice; pending commissions; verbatim Art. 397 scale; head-3 takes-goods + head-5 subrogation flags |
| FR-116 | odoo | l10n_sv_commerce.agency.contract | termination_reason (398 a-f) + import_bar_status | Presumed just cause on injuring unilateral modification; agent-domicile sumario forum note; 399-B import bar informational |
| FR-117 | odoo | res.partner | intermediario role + duty flags | No representation — apoderado mandate ⇒ role-loss flag; impartial-disclosure/authenticity/abstention exposure |
| FR-118 | odoo | l10n_sv_commerce.agency.commission | settlement conditions | Celebration condition; 50/50 split; usual-commission config-gap; 6-month window from acceptance; expenses default-false; name-disclosure tracking |
| FR-119 | odoo | l10n_sv_commerce.book | intermediario_registro + intermediario_diario | Mercantile-accounting formalities via SV-CML-FR-025 (by id); exact copies; exhibition metadata; no-claim-without-documents warning |

Version-regime notes (D12): no dated values live in this file. All
periods are code text (15 days, 3 months, 6 months, 3 years — Art. 397/375/
405); commission rates ("usos del lugar", "comisión usual") are
config-gaps with NO shipped defaults (OQ-002). The 07_ text basis carries
the SOQ-22 verification note (§2); Sección "B" is D.L. 247 (1973) text
carried through reform (5) ticks; the 1985 authentic interpretation of
Art. 392 is excluded as unconstitutional (§2, OQ-004).

## 6. Acceptance Criteria

- **AC-001:** Given a factor appointed with no recorded limits, when his
  authority profile resolves, then general authority over the
  enterprise's giro applies from the sole appointment, and a later
  recorded limit does not bind a third-party operation unless the
  third-party-knowledge flag is set on it (FR-098).
- **AC-002:** Given a factor whose power was revoked today with neither
  registry inscription of the revocation nor legitimate notice to him,
  when he celebrates an act tomorrow, then the act is flagged valid —
  and it remains third-party-valid until the revocación registry entry
  (or the enajenación entry) is recorded, at which point the
  third-party-validity flag clears (FR-099, FR-102).
- **AC-003:** Given a factor holding an express mandate that was never
  granted in writing nor inscribed, when he operates beyond the
  principal's intended limits, then the mandate computes as DEEMED-
  GENERAL for the branch of commerce and the principal cannot oppose
  the limits to the third party absent a recorded knowledge fact
  (FR-100).
- **AC-004:** Given an establishment with no posted caja reserve, when a
  sales dependiente collects the price in-store, then the collection is
  within his default authority; given a posted caja-reserve
  announcement, then in-store collection by the dependiente is flagged
  outside his authority (FR-104).
- **AC-005:** Given a dependiente collecting payment OUTSIDE the
  establishment, when his record carries no written-authorization +
  identity-document package and no stamped recibo/factura delivered
  against payment, then the collection is flagged outside-authority
  with the two statutory cures identified; given either cure recorded,
  then the flag clears (FR-106).
- **AC-006:** Given a dependiente viajero, when he takes an order and
  agrees a guarantee, then both are within his default faculty; when he
  grants an espera or descuento without express authorization or
  collects the advanced price without simultaneous delivery, then the
  operation is flagged contrary to the Art. 380 defaults (advance
  collection blocked-warning; credit-term operation valid towards the
  buyer with internal-liability marker per FR-105) (FR-105, FR-107).
- **AC-007:** Given a principal with an in-force agente dependiente
  contract for plaza San Salvador / ramo X (deemed exclusive), when the
  principal records his own deal in that plaza and ramo, then the
  agent's participations accrue as if he had promoted the business;
  and when a second agent is engaged for the same plaza/ramo, then the
  exclusivity validation blocks the engagement absent an express
  contrary pact (FR-109, FR-110).
- **AC-008:** Given an agente dependiente serving two principals, when
  his libro especial is evaluated, then the operations of each
  principal are recorded with proper separation and distinguishing
  pedido/merchandise details, the register carries the SV-CML-FR-025
  discipline flags, and the default remuneration settles monthly only
  against the duly documented account (FR-111).
- **AC-009:** Given a distribuidor contract terminated by the principal
  without the 3-month written notice and without any Art. 398 cause
  recorded, when the termination is recorded, then the unjustified-
  termination state opens the Art. 397 indemnity worksheet with ALL
  FIVE heads present — head 3 computed on cost + fletes + impuestos
  with the principal-takes-goods flag, head 5 with the subrogation
  flag — plus settlement of pending commissions (FR-115, FR-116).
- **AC-010:** Given a foreign principal condemned by executed judgment
  under the Sección "B" rules, when the import-bar status is evaluated,
  then the barred state shows on the principal's record until the
  consignment or beneficiary-statement lift event is recorded
  (FR-116).
- **AC-011:** Given an intermediario whose mediated contract was
  celebrated under a suspensive condition, when the condition fails,
  then no remuneration settlement accrues; given the business realized
  within six months of the parties' acceptance on his proposed bases,
  then the settlement accrues split half/half absent contrary agreement
  (FR-118).
- **AC-012:** Given an intermediario, when his statutory registers are
  evaluated, then a registro (object + essential bases at each
  operation close) and a libro diario de operaciones exist with the
  mercantile-accounting formalities of SV-CML-FR-025, exact copies are
  trackable to requesting parties, and a claim recorded without the
  Art. 408 document references raises the incomplete-claim warning
  (FR-119).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | CC/CT boundary for the same natural persons: this file owns the commercial-authority layer (who binds the principal, default powers, channel protection); the payroll wave owns the employment relation (CT corpus, `sv/sources/11_Codigo_Trabajo.pdf` — salary integration of commissions SV-PAY-FR-002, contract taxonomy/termination SV-PAY-FR-101..110, by id). Residual: Art. 384 calls the agente dependiente "subordinado al principal" — subordination language kin to CT dependency; whether a given dependiente/agente is an EMPLOYEE (CT rights: aguinaldo, indemnización, social security) versus an independent channel contractor is a classification fact the system records but does not decide. Confirm the classification workflow with the payroll wave at implementation so the res.partner authority profile and the hr.employee/payroll record interlock without double-governance. | no | Takumi S5 + payroll wave | open |
| OQ-002 | Commission rates are "usos del lugar" / "comisión usual" (Arts. 389, 395, 404) — no statutory rate exists in the corpus; FR-110/FR-114/FR-118 expose rates as contract/config slots with NO shipped defaults. Same discipline for the Art. 397 indemnity quantification inputs (3-year gross utility, unrecovered gastos, inventory cost+fletes+impuestos, conceded credits): the worksheet records accounting data, it never invents values. Acquire usos evidence or client contract data at implementation; never hardcode. | no | Takumi S5 | open |
| OQ-003 | Art. 399-B foreign-principal import bar: enforcement runs through oficios from the executing court to the "organismos administrativos competentes" (customs/administrative side) — that operational interface is NOT in this corpus. FR-116 records the bar as an informational status; if an import/customs corpus later lands (Ley Orgánica de Aduanas = 13_), verify whether the bar can be wired to an operational gate and update by id. | no | Takumi S5 (sources watch) | open |
| OQ-004 | Art. 392's 1985 authentic interpretation (D. Nº 237, transcribed in the print's NOTA) was declared UNCONSTITUTIONAL (Sala de lo Constitucional, sent. 15-feb-1988, D.O. 41 T.298 29-feb-1988) and is excluded as authority here (§2). Residual: whether any post-1988 jurisprudence or reform reshaped the "cualquiera otra forma que acuerden las partes" breadth of Art. 392 is unverified — rides the SOQ-22 consolidation-cutoff watch; re-verify if an agency-law dispute surface is ever built. | no | Takumi S5 | open |
