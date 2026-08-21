# SV — Commercial-legal — Society types: taxonomy, formation, capital, statutory reserves and the SRL/S.A. profiles (SAS extensible design)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador *sociedad* (company/society) type and
formation regime of the Código de Comercio (Commercial Code, CC): the
Art. 17 definition (*contrato solemne* — solemn contract — of two or more
persons pooling *bienes o industria*, goods or industry, to share profits)
and the Art. 18 taxonomy — *sociedades de personas* (partnership-type:
*colectiva*, *comandita simple*, *SRL*) vs *sociedades de capitales*
(capital-type: *S.A.*, *comandita por acciones*), each × *capital fijo o
variable* (fixed or variable capital), with only law-regulated forms
admissible — plus the Art. 19 cooperative special profile and the **SAS
extensible-type design** (Sociedad por Acciones Simplificada —
confirmed-existing under separate legislation, statute NOT in corpus,
SOQ-23); the formation family of Arts. 21-27 — *escritura pública*
(public deed) for constitution/modification/transformation/fusión/
liquidación, the 12-field escritura content with its nullity rule, the
*estatutos* (bylaws) deposit, and **legal personality perfected ONLY at
inscription** (Art. 25) with the Art. 24/465-I inscription catalogue; the
capital regime of Arts. 29-33 — capital as the liability-side invariant
(assets ≥ capital), capital-change consent/publication/opposition,
aportation admissibility and non-money/credit valuation rules; the
distribution regime of Arts. 37-39 — the dividend ceiling (realized
per-balance profits only), the mandatory *reserva legal* (statutory legal
reserve) chassis with its restoration duty, and the per-type rates
(colectiva 5% → 1/6 limit, Art. 91; SRL/S.A./EIRL 7% → 1/5 minimum floor,
Arts. 123/295/616) with their investment constraints; the society books of
Art. 40; and the SRL (Arts. 101-125) and S.A. (Arts. 126-160, 289-295)
statutory profiles — suffix, capital denominations, subscription/
exhibition, partner and share ledgers, voting/quorum, own-share
prohibitions, preferential-subscription windows and the mandatory external
auditor with monthly duties.

It does **not** cover: merchant status, matrícula and the registry
architecture (`01_merchant-registration.md` — consumed by id: FR-004
exemption profiles, FR-008 matrícula-trigger link, FR-013 registry-entry
model, FR-017 publication engine); bookkeeping form, register
legalization, the no-alteration regime (Art. 440 extension) and retention
(`02_accounting-books.md` — society books inherit its discipline flags by
id); the annual statement cycle, certification and balance deposit
(`03_financial-statements.md` — this file supplies the Art. 236 mechanics
and the Art. 290 auditor incompatibilities that file defers to);
society-lifecycle mechanics — the capital-VARIABLE regime, fusión,
transformación, liquidación, nullity/irregularity and extranjeras
(`05_society-lifecycle.md` when it lands — Arts. 306-314/315-342 zone);
commercial agents (`06_commercial-agents.md`); the empresa mercantil
transfer package and the EIRL vehicle itself, whose profile is
`07_empresa-mercantil-eirl.md` (this file owns only EIRL's Art. 616-I
reserve rates); payment instruments (`08_payment-instruments.md`);
sales contracts (`09_sales-contracts.md`); AML compliance
(`10_aml-compliance.md`); and ISR mechanics, including the ISR *reserva
legal* — a DIFFERENT institution owned by the taxation wave by id (§2).

## 2. Legal Basis

Authority order (binding, per master evidence index S5): the Código de
Comercio = **07_** (D.L. Nº 671, 8-may-1970, D.O. 140 T.228 31-jul-1970;
29 listed reforms, last = D.L. 641-2008) — article text CURRENT per the
**SOQ-22 verification (resolved-with-residual, W12 2026-08-18)**: the
second official copy 73_ (UIF-hosted Índice Legislativo edition, 280 pp.)
ALSO ends its reform list at D.L. 641-2008 (20-item vs 29-item editorial
counting; decree-date print conflict 12- vs 26-jun-2008 [sic], same D.O.
120 T.379 27-jun-2008), so no post-2008 CC structural reform is evidenced
in two official consolidations; the residual — both copies are
Asamblea-editorial artifacts without a stated as-of date — rides every 07_
LB in this file. Verbatim text below is copied from the 07_ evidence file
(EVID-218/219/220) and, where the evidence abbreviates (Arts. 17-25,
27-33, 37-40, 91-92, 100-125, 129-160, 236, 289-295, 465-I, 616), from
the extraction txt `sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable
per standing ruling; page pointers = txt PAGE markers; reform tick marks
"(2)(3)(10)(16)(18)(29)" stripped from quotations, provenance noted
here).

SAS extensible design (SOQ-23, open): the Sociedad por Acciones
Simplificada (SAS, simplified joint-stock company) is NOT in this Código
— 07_ OQ-2 and the W12 verification (EVID-250) both leave it under
separate legislation; its EXISTENCE is confirmed via the official CNR
creaempresa portal (LB-032), but the statute itself (number/date) is
unpinned because asamblea.gob.sv and the D.O. route are down. Per the
wave design ruling: the company-type model is EXTENSIBLE (selection +
profile-driven), the type select carries `sas` with a statute-pending
flag, and NO mechanics (suffix, capital, quorum, reserve) are invented —
OQ-001.

Currency discipline (SOQ-29): the US$2,000 SRL minimum capital and the
US$1 participación/acción denominations (Arts. 103/129) and the
US$100,000 subscription-payment extension trigger (Art. 106) are
2008-reform (18)(29) USD code text — dated-but-current under the SOQ-22
residual watch (same family as the Art. 15 threshold in
`01_merchant-registration.md` §2 and the Art. 437/452/474 thresholds).
The cooperative per-action cap "¢5,000.00" (Art. 19-II) is a COLONES
remnant (kin of 07_ OQ-7): historical code text, operative reading USD —
every value-level use is flagged (OQ-002). Art. 31's "moneda nacional"
(the value of non-money aportations expressed in national currency) is
the same colones-era remnant, read against dollarization.

Reserva disambiguation (by id, DIFFERENT institutions — never conflate):
(i) the society **statutory reserva legal** (THIS file, FR-055:
5%→1/6 colectiva family; 7%→1/5 SRL/S.A./EIRL family — capital-based
chassis of Art. 39); (ii) the Art. 445 CC **revaluation reserve**
(`03_financial-statements.md` FR-041); (iii) the **ISR reserva legal**
book reserve — a taxation institution whose constitution register and
25% separate-liquidation reduction trigger are owned by
`sv/requirements/taxation/02_isr-deductions.md` SV-TAX-FR-063 with the
25% computation in `sv/requirements/taxation/03_isr-rates-gains.md` §3.6
SV-TAX-FR-101 — cited here by id only, never restated.

E-invoicing kin (pointer only, no re-derivation): company-type suffixes
and the razón social/denominación flow into DTE emitter-name data owned
by the e-invoicing wave's onboarding/authorization cluster (A11) — no
norm in this article set ties DTE emission to society type; the
"en liquidación" name-suffix kin is `05_society-lifecycle.md` territory.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 17: "Son comerciantes sociales todas las sociedades independientemente de los fines que persiguen, sin perjuicio de lo preceptuado en el artículo 20." "Sociedad es el ente jurídico resultante de un contrato solemne, celebrado entre dos o más personas, que estipulan poner en común, bienes o industria, con la finalidad de repartir entre sí los beneficios que provengan de los negocios a que van a dedicarse." "Tales entidades gozan de personalidad jurídica, dentro de los límites que impone su finalidad, y se consideran independientes de los socios que las integran." (inciso 3 excludes transitory, parentesco-conditioned, decree-created and other non-contractual association forms) Art. 18: "Las sociedades se dividen en sociedades de personas y sociedades de capitales; ambas clases pueden ser de capital variable." "Son de personas: I.- Las sociedades en nombre colectivo o Sociedades Colectivas. II.- Las sociedades en comandita simple o sociedades comanditarias simples. III.- Las sociedades de responsabilidad limitada." "Son de capital: I.- Las sociedades anónimas. II.- Las sociedades en comandita por acciones o sociedades comanditarias por acciones." "Solamente podrán constituirse sociedades dentro de las formas reguladas por la Ley." | All sociedades are social merchants regardless of the ends they pursue (without prejudice to Art. 20). A sociedad is the juridical entity resulting from a solemn contract between two or more persons who stipulate pooling goods or industry in order to share among themselves the profits of the business they will engage in. Such entities enjoy legal personality within the limits imposed by their purpose and are independent of the socios composing them (third inciso excludes transitory/parentage-conditioned/decree-created forms). Societies divide into sociedades de personas and sociedades de capitales; both classes may be of variable capital. Person-type: colectivas; comanditarias simples; de responsabilidad limitada (SRL). Capital-type: anónimas (S.A.); comanditas por acciones. Societies may ONLY be constituted within the forms regulated by law | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 17-18 pp.4-5 (EVID-218; txt PAGE 4-5) |
| LB-002 | Código de Comercio, Art. 19 (intro + ordinals I-III, XII-XIII; ordinals IV-XI summarized): "Las Sociedades Cooperativas existentes a la fecha de entrar en vigencia este Código, así como las que en lo sucesivo se constituyan, para los cuales se requerirá, por lo menos, de un número de diez socios, funcionarán con sujeción a las normas que se expresan a continuación: I.- Las sociedades cooperativas se regirán por las disposiciones que correspondan a la especie de sociedades que hayan adoptado en su constitución; y por el de la sociedad anónima relativa a balances, responsabilidad de los administradores y vigilancia del auditor salvo las modificaciones que se establecen en el presente artículo. II.- Las acciones no podrán ser, cada una, de más de ¢5,000.00, serán nominativas y sólo trasmisibles por inscripción en el respectivo Libro, con autorización de la Sociedad. III.- El socio tendrá un solo voto, cualquiera que sea el número de acciones que tenga en propiedad. [ordinals IV-XI omitted — guaranty floor of subscribed amount even on destitución/exclusión; socio book at the domicile (name/profession/domiciliio, admission/destitution/exclusion dates, aportación current account) examinable by anyone; admission by signature in that book; nominative titles; post-constitution admits answer for prior operations; separation notice 8 days; exclusion by Junta General; exonerated/excluded socio withdraws per last balance EXCLUDING the Fondo de Reserva.] XII.- Las Sociedades Cooperativas deberán hacer que proceda o siga a su firma o denominación las palabras 'Sociedad Cooperativa de Responsabilidad Limitada' o 'Ilimitada', según ésta sea. XIII.- Las Sociedades Cooperativas estarán sujetas al pago de todo impuesto o contribución fiscal o municipal, pero quedan exentas de cualquier imposición directa su capital y los rendimientos del mismo." (the 07_ print carries a NOTA: the ordinal-XIII ISR exemption was DEROGATED as of 1-ene-1990 by D.L. Nº 385, D.O. 227 of 7-12-1989) | Cooperative societies — existing at the Code's entry into force or thereafter constituted — require AT LEAST TEN socios and function subject to: I. the rules of the society species adopted in their constitution AND the S.A. rules on balances, administrator liability and auditor vigilance, save the modifications of this article; II. actions may each be of no more than ¢5,000.00 (COLONES remnant — §2), are nominative and transmissible ONLY by inscription in the respective Book with the Society's authorization; III. each socio has ONE VOTE regardless of the number of actions owned. [IV-XI omitted — see citation column.] XII. cooperatives must carry after their name the words "Sociedad Cooperativa de Responsabilidad Limitada" or "Ilimitada" as applicable; XIII. cooperatives are subject to all fiscal/municipal taxes; the capital-and-yields direct-tax exemption printed in the code text was REPEALED (D.L. 385-1989, effective 1-ene-1990) — cooperatives are tax subjects | `sv/sources/07_Codigo_Comercio.pdf` | Art. 19 pp.5-7 (EVID-218; txt PAGE 5-7) |
| LB-003 | Código de Comercio, Art. 21: "Las sociedades se constituyen, modifican, transforman, fusionan y liquidan por escritura pública." | Societies are constituted, modified, transformed, fused (merged) and liquidated by escritura pública (public deed) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 21 p.7 (EVID-218; txt PAGE 7) |
| LB-004 | Código de Comercio, Art. 22: "La escritura social constitutiva deberá contener: I.- Nombre, edad, ocupación, nacionalidad y domicilio de las personas naturales; y nombre, naturaleza, nacionalidad y domicilio de las personas jurídicas, que integran la sociedad. II.- Domicilio de la sociedad que se constituye, con expresión del municipio y departamento al cual pertenece. III.- Naturaleza jurídica. IV.- Finalidad. V.- Razón social o denominación, según el caso. VI.- Duración o declaración expresa de constituirse por tiempo indeterminado. VII.- Importe del capital social; cuando el capital sea variable se indicará el mínimo. VIII.- Expresión de lo que cada socio aporte en dinero o en otros bienes, y el valor atribuido a éstos. IX.- Régimen de administración de la sociedad, con expresión de los nombres, facultades y obligaciones de los organismos respectivos. X.- Manera de hacer distribución de utilidades y, en su caso, la aplicación de pérdidas, entre los socios. XI.- Modo de constituir reservas. XII.- Bases para practicar la liquidación de la sociedad; manera de elegir liquidadores cuando no fueren nombrados en el instrumento y atribuciones y obligaciones de éstos." "Además de los requisitos aquí señalados, la escritura deberá contener los especiales que para cada clase de sociedad establezca este Código." | The constitutive social deed must contain: I. name, age, occupation, nationality and domicile of the natural persons, and name, nature, nationality and domicile of the juridical persons, integrating the society; II. the society's domicile, expressing the municipio and departamento; III. juridical nature (type); IV. purpose; V. razón social (firm name) or denominación, as the case may be; VI. duration or express declaration of indeterminate term; VII. the amount of the social capital — when variable, the MINIMUM is indicated; VIII. expression of what each socio contributes in money or other goods, and the value attributed to the latter; IX. the administration regime, with the names, faculties and obligations of the respective organs; X. how profits (and losses) are distributed among socios; XI. how reserves are constituted; XII. bases for liquidation and how liquidators are chosen when not named in the instrument, with their attributes and obligations. In addition, the deed must contain the special requirements this Code sets for each class of society | `sv/sources/07_Codigo_Comercio.pdf` | Art. 22 pp.7-8 (EVID-218; txt PAGE 7-8) |
| LB-005 | Código de Comercio, Art. 23: "Los estatutos de la sociedad desarrollarán los derechos y obligaciones que existen entre ella y sus socios, fundamentándose en las cláusulas del pacto social y no podrán contradecirlas en forma alguna." "Corresponde a la junta general extraordinaria de la sociedad decretar los estatutos, debiendo aparecer íntegramente en el acta de la sesión en que fueron aprobados." "Una certificación del acta de la sesión en que se aprueben y aparezcan redactados los estatutos, se deberá depositar en el Registro de Comercio." "Una copia de los estatutos deberá ser entregada a cada socio, la cual podrá ser reproducida por cualquier medio y en la que deberá aparecer el número del depósito en el Registro de Comercio." | The society's estatutos (bylaws) develop the rights and obligations between it and its socios, grounded on the pacto social clauses, which they may not contradict in any way. The EXTRAORDINARY general meeting decrees the estatutos, which must appear integrally in the minutes of the session approving them. A certification of the approving acta must be DEPOSITED in the Commerce Registry. A copy of the estatutos must be delivered to each socio — reproducible by any means — showing the Registry deposit number | `sv/sources/07_Codigo_Comercio.pdf` | Art. 23 p.8 (EVID-218 zone; txt PAGE 8) |
| LB-006 | Código de Comercio, Art. 24: "Se inscribirán en el Registro de Comercio las escrituras de constitución, modificación, transformación, fusión y liquidación de sociedades, lo mismo que las certificaciones de las sentencias ejecutoriadas que contengan disolución o liquidación judiciales de alguna sociedad." Art. 25: "La personalidad jurídica de las sociedades se perfecciona y se extingue por la inscripción en el Registro de Comercio de los documentos respectivos." "Dichas inscripciones determinan, frente a terceros, las facultades de los representantes y administradores de las sociedades, de acuerdo con su contenido." "Las sociedades inscritas no pueden ser declaradas nulas con efectos retroactivos, en perjuicio de terceros." Art. 465-I: "En el Registro de instrumentos sociales: Las escrituras de constitución, modificación, transformación, fusión y liquidación de sociedades, así como las ejecutorias de las sentencias o las certificaciones de las mismas que reconozcan la disolución de la sociedad o practiquen la liquidación de la misma y las certificaciones de los puntos de acta, en los casos en que deban inscribirse y la ley no señale otro registro al efecto." | There shall be registered in the Commerce Registry the deeds of constitution, modification, transformation, fusión and liquidation of sociedades, and the certifications of executed judgments containing judicial dissolution or liquidation. The legal personality of sociedades is PERFECTED and EXTINGUISHED by the inscription of the respective documents in the Commerce Registry; those inscriptions determine, towards third parties, the faculties of the societies' representatives and administrators according to their content; inscribed societies cannot be declared null with retroactive effects to the prejudice of third parties. Art. 465-I: in the register of social instruments — the constitution/modification/transformation/fusión/liquidation deeds, the executed judgments or certifications recognizing dissolution or practising liquidation, and acta-point certifications where inscribable and no other register is assigned | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 24-25 p.8 (EVID-218); Art. 465-I p.87 (EVID-217; txt PAGE 8, 87-88) |
| LB-007 | Código de Comercio, Art. 27: "La omisión de los requisitos señalados en el Art. 22, produce nulidad de la escritura a excepción de los contenidos en los ordinales X, XI y XII, cuya omisión dará lugar a que se apliquen las disposiciones pertinentes de este Código." | Omission of the Art. 22 requirements produces NULLITY of the deed, EXCEPT ordinals X, XI and XII (profit/loss distribution, reserves, liquidation bases), whose omission instead triggers application of this Code's pertinent provisions | `sv/sources/07_Codigo_Comercio.pdf` | Art. 27 p.9 (EVID-218 zone; txt PAGE 9) |
| LB-008 | Código de Comercio, Art. 29: "El capital social está representado por la suma del valor establecido en la escritura social para las aportaciones prometidas por los socios. Figura siempre del lado del pasivo del balance, de modo que en el patrimonio debe existir un conjunto de bienes de igual valor, por lo menos, al monto del capital." | The social capital is represented by the sum of the values set in the social deed for the aportations PROMISED by the socios. It ALWAYS figures on the liability side of the balance, so that in the patrimony there must exist a set of goods of value at least equal to the amount of the capital | `sv/sources/07_Codigo_Comercio.pdf` | Art. 29 p.8 (EVID-218; txt PAGE 8) |
| LB-009 | Código de Comercio, Art. 30: "Toda sociedad podrá aumentar o disminuir su capital." "El aumento o reducción del capital requiere el consentimiento de los socios, dado en la forma correspondiente a la clase de sociedad de que se trate." "El aumento del activo por revalorización del patrimonio es lícito, y su importe puede pasar a la cuenta de capital de la sociedad o a una reserva especial, la que no podrá repartirse entre los socios sino cuando se enajenen los bienes revalorizados y se perciba en efectivo el importe de la plusvalía." "El acuerdo de aumento del capital social se publicará por una vez en un diario de circulación nacional y en el Diario Oficial. El acuerdo de disminución del capital social se publicará de conformidad a lo establecido en el Art. 486 de este Código. Ambos acuerdos serán comunicados a la Oficina que ejerce la vigilancia del Estado." "En el caso del inciso anterior, los acreedores y cualquier tercero interesado, así como el Ministerio Público, podrán oponerse a la reducción del capital, en un plazo de treinta días a contar de la tercera publicación; toda oposición se tramitará en forma sumaria, pero la de cualquier acreedor concluirá de pleno derecho por el pago del crédito respectivo." "Transcurrido el plazo de que trata el inciso precedente sin que medie oposición, o extinguidas las que se hubieren formulado, o bien desechadas judicialmente por sentencia ejecutoriada, podrá la sociedad formalizar la reducción de su capital." | Every sociedad may increase or diminish its capital. Increase or reduction requires the socios' consent given in the form corresponding to the society's class. Asset increase by patrimony revaluation is lawful, and its amount may pass to the capital account or to a SPECIAL reserve which may not be distributed among socios until the revalued goods are alienated AND the surplus value received in cash. The capital-INCREASE agreement is published ONCE in a nationally circulated daily and in the Diario Oficial; the capital-REDUCTION agreement is published per Art. 486; both are communicated to the state vigilance office. Creditors, any interested third party and the Ministerio Público may OPPOSE the reduction within THIRTY DAYS from the third publication; opposition proceeds summarily, and any creditor's opposition ends as of right by payment of the respective credit. Once the term lapses without opposition (or oppositions are extinguished or judicially dismissed by final judgment), the society may formalize the reduction | `sv/sources/07_Codigo_Comercio.pdf` | Art. 30 pp.9-10 (EVID-218; txt PAGE 9) |
| LB-010 | Código de Comercio, Art. 31: "Son admisibles como aportaciones todos los bienes que tengan un valor económico, el cual debe expresarse en moneda nacional." "No es lícita la aportación de trabajo en las sociedades de capital. La simple asunción de responsabilidad no es válida como aportación." "Salvo pacto en contrario, las aportaciones de bienes distintos del dinero se entienden traslativas de dominio. En consecuencia, el riesgo de los mismos está a cargo de la sociedad desde que se hace la entrega y el aportante responde de la evicción y saneamiento de conformidad con las disposiciones del Código Civil relativas al contrato de compraventa." Art. 33: "Los socios deben realizar las aportaciones al momento de otorgarse la escritura social o en la época y forma estipuladas en la misma." "La mora de aportar, autoriza a la sociedad a exigirla judicialmente por la vía ejecutiva. Ningún socio puede invocar el cumplimiento de otro para no realizar su propia aportación." "El socio, inclusive el que aporta trabajo, responde de los daños y perjuicios que ocasione a la sociedad por su incumplimiento." | Admissible as aportations are all goods having economic value, which must be expressed in national currency (colones-era remnant — operative reading USD, §2). Contribution of WORK is not lawful in capital societies; mere assumption of liability is not a valid aportation. Absent contrary pact, aportations of goods other than money are understood as TRANSLATIVE OF OWNERSHIP — the goods' risk is on the society from delivery, and the aportante answers for eviction and warranty (evicción y saneamiento) under the Civil Code's sale-of-goods provisions. Art. 33: socios must make their aportations at the deed's execution or at the epoch and in the form stipulated in it; default authorizes the society to demand them judicially by the ejecutivo route; no socio may invoke another's non-performance to withhold his own aportation; every socio — including one contributing work — answers for damages caused by non-performance | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 31, 33 p.9 (EVID-218; txt PAGE 9) |
| LB-011 | Código de Comercio, Art. 32: "Cuando la aportación de algún socio consiste en créditos, el que la hace responde de la existencia y legitimidad de ellos, así como de la solvencia del deudor; responde igualmente de que, tratándose de títulos valores, no han sido objeto de algún procedimiento de cancelación o reivindicación. Se prohíbe pactar contra el tenor de este artículo." "Cuando se aportan acciones de sociedades de capitales, el valúo de ellas no puede exceder de su valor contable mientras no exista en el país una Bolsa de Valores." | When a socio's aportation consists of CREDITS, the contributor answers for their existence and legitimacy and for the debtor's solvency; he equally answers that, in the case of títulos valores, they have not been subjected to any cancellation or reivindication proceeding. Pact against the tenor of this article is prohibited. When shares of capital societies are contributed, their valuation may not exceed their BOOK VALUE so long as no securities exchange exists in the country | `sv/sources/07_Codigo_Comercio.pdf` | Art. 32 p.9 (EVID-218; txt PAGE 9) |
| LB-012 | Código de Comercio, Art. 37: "Si hubiere pérdida del capital deberá reintegrarse, o reducirse en el caso del ordinal 7º del Art. 444, antes del reparto o asignación de utilidades." Art. 38: "El reparto de utilidades nunca podrá exceder del monto de las que realmente se hubieren obtenidos, conforme al balance general y estado de pérdidas y ganancias." "Los administradores que autoricen pagos en contravención a lo dispuesto en el inciso que antecede; y los socios que los hubieren percibido, responderán solidariamente de su devolución. La devolución podrá ser exigida, por la sociedad, por los acreedores o por los socios disidentes." (incisos 3-4 — the sole exception: socio industrial periodic alimentary sums, judicially fixable absent agreement, computed against profits without restitution when profits are insufficient, transferred to general-expenses account in the balance) | If there is LOSS OF CAPITAL it must be restored — or reduced per Art. 444 ordinal 7 — BEFORE any distribution or assignment of profits. The distribution of profits may NEVER exceed the amount of profits REALLY obtained, per the balance general and the profit-and-loss statement. Administrators authorizing payments contrary to the first inciso, and socios having received them, answer SOLIDARILY for their return — return demandable by the society, the creditors or the dissenting socios. (Third/fourth incisos — unique exception: the socio industrial's periodic alimentary sums, judicially fixable, accounted against profits without restitution duty when profits fall short, transferred to general expenses) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 37-38 p.10 (EVID-218; txt PAGE 10) |
| LB-013 | Código de Comercio, Art. 39: "De las utilidades netas de toda sociedad deberá separarse anualmente un porcentaje para formar la reserva legal, hasta que ésta alcance una cantidad determinada. El porcentaje y la cuantía de la reserva legal serán determinados por este Código para cada clase de sociedad." "La reserva legal deberá ser restaurada en la misma forma, cuando disminuya por cualquier motivo." "Contra lo dispuesto en este artículo no puede invocarse estipulación o pacto en contrario; los administradores quedarán solidariamente responsables de su cumplimiento, y por ello obligados a restituir en su totalidad o parte la reserva legal, si por cualquier motivo no existiere o sólo la hubiere en parte, sin perjuicio del derecho que asista a los administradores para repetir en contra de quienes hubieren recibido el dinero. Para el exacto cumplimiento de este precepto, se concede acción a los socios, a los acreedores o al Ministerio Público." | From every society's NET profits a percentage must be separated ANNUALLY to form the reserva legal, until it reaches a determined quantity; the percentage and quantum are set by this Code for each class of society. The reserva legal must be RESTORED in the same form when it diminishes for any motive. No stipulation or pact to the contrary may be invoked; administrators are SOLIDARILY responsible for compliance — obliged to restitute the reserve wholly or partly if it does not exist or exists only in part — without prejudice to their recourse against those who received the money; action is granted to the socios, the creditors or the Ministerio Público | `sv/sources/07_Codigo_Comercio.pdf` | Art. 39 p.10 (EVID-218; txt PAGE 10) |
| LB-014 | Código de Comercio, Art. 91: "La cantidad que se destinará anualmente para integrar la reserva legal será el cinco por ciento de las utilidades netas y el límite legal de dicha reserva será la sexta parte del capital social." Art. 92: "La mitad de las cantidades que aparezcan en la reserva legal deberá tenerse disponible o invertirse en valores mercantiles salvadoreños de fácil realización; la otra mitad podrá invertirse de acuerdo con la finalidad de la sociedad." Art. 100 (first sentence): "Son aplicables a la sociedad en Comandita Simple los artículos 75, 76, 77, 83, 91 y 92; también le serán aplicables, sin perjuicio de lo dispuesto en el artículo 96, los artículos del 88 al 90 inclusive." | The quantity destined annually to integrate the legal reserve of the COLECTIVA is FIVE PERCENT of net profits, and the LEGAL LIMIT of that reserve is ONE-SIXTH of the social capital. HALF of the amounts appearing in the reserve must be kept available or invested in readily realizable Salvadoran mercantile securities; the other half may be invested per the society's purpose. The comandita simple is governed by Arts. 91/92 (with 75-77, 83, 88-90) — the colectiva reserve family extends to it | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 91-92 p.19; Art. 100 p.20 (EVID-218 zone; txt PAGE 19-20) |
| LB-015 | Código de Comercio, Art. 123: "La cantidad que se destinará anualmente para formar la reserva legal de la sociedad de responsabilidad limitada, será el siete por ciento de las utilidades netas y el límite mínimo legal de dicha reserva será la quinta parte del capital social." Art. 124: "Las dos terceras partes de las cantidades que aparezcan en la reserva legal deberán tenerse disponibles o invertirse en valores mercantiles salvadoreños o centroamericanos de fácil realización; la otra tercera parte podrá invertirse de acuerdo con la finalidad de la sociedad." | The quantity destined annually to form the SRL legal reserve is SEVEN PERCENT of net profits, and the MINIMUM LEGAL limit of that reserve is ONE-FIFTH of the social capital. TWO-THIRDS of the amounts appearing in the reserve must be kept available or invested in readily realizable SALVADORAN OR CENTRAL-AMERICAN mercantile securities; the remaining third may be invested per the society's purpose | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 123-124 pp.24-25 (EVID-219; txt PAGE 24-25) |
| LB-016 | Código de Comercio, Art. 295: "Son aplicables a las sociedades anónimas las disposiciones contenidas en los artículos 123 y 124 de este Código." Art. 616: "La empresa individual de responsabilidad limitada funcionará con sujeción a las disposiciones siguientes: I.- En materia de reservas, los artículos 39, 123 y 124. II.- En materia de utilidades, el artículo 37 y el inciso primero del artículo 38. III.- En materia de estados financieros, del artículo 282 al 284; el inciso final del artículo 286; y el artículo 287, en lo pertinente. IV.- En materia de vigilancia, del artículo 289 al artículo 293, en lo conducente." | The S.A. is governed by Arts. 123 and 124 (7% net profits annual separation; minimum legal limit one-fifth of capital; two-thirds in readily realizable Salvadoran/Central-American securities). The EIRL functions subject to: I. reserves — Arts. 39, 123, 124; II. profits — Art. 37 and Art. 38 inciso primero; III. financial statements — Arts. 282-284, 286 final inciso, 287 as pertinent; IV. vigilance — Arts. 289-293 as conducent | `sv/sources/07_Codigo_Comercio.pdf` | Art. 295 p.55 (EVID-220); Art. 616 p.110 (EVID-224; txt PAGE 55, 110) |
| LB-017 | Código de Comercio, Art. 40: "Todas las sociedades llevarán los libros siguientes: I. Libro de Actas de las Juntas Generales, en el cual se asentarán los acuerdos adoptados en las sesiones respectivas. II. Libro de Actas de Juntas Directivas o de Consejos de Administración, según la naturaleza de la sociedad y el régimen de administración adoptado o regulado por este Código. III. Libro de Registro de Socios o de Accionistas, según la naturaleza de la sociedad. IV. Libro de Registro de Aumentos y Disminuciones de Capital Social, cuando el régimen adoptado sea el de capital variable. Los libros serán legalizados por contadores públicos o por el Registro de Comercio." | ALL societies keep the following books: I. minutes book of the general meetings (juntas generales), recording the agreements adopted; II. minutes book of boards of directors or administrative councils, per the society's nature and administration regime; III. Registro de Socios (partners) or de Accionistas (shareholders) book, per the society's nature; IV. book registering capital-social increases and decreases, when the capital-VARIABLE regime is adopted. The books are legalized by public accountants or by the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 40 p.11 (EVID-218; txt PAGE 11) |
| LB-018 | Código de Comercio, Art. 101: "La sociedad de responsabilidad limitada puede constituirse bajo razón social o bajo denominación. La razón social se forma con el nombre de uno o más socios. La denominación se forma libremente, pero debe ser distinta a la de cualquier sociedad existente." "Una u otra debe ir inmediatamente seguida de la palabra 'Limitada' o su abreviatura 'Ltda.' La omisión de este requisito en la escritura social, hará responsables solidaria e ilimitadamente a todos los socios; y en cualquier acto posterior de la sociedad también a los administradores por las obligaciones sociales que así se hubieren contraído, sin perjuicio del derecho de repetición de lo pagado en exceso por los socios o administradores inocentes contra los socios o administradores culpables." | The SRL may be constituted under a razón social (formed with the name of one or more socios) or under a denominación (freely formed, but distinct from any existing society). Either must be immediately followed by the word "Limitada" or its abbreviation "Ltda." Omission of this requirement in the social deed renders ALL socios jointly and severally and unlimitedly liable — and, for any later act of the society, the administrators too — for obligations so contracted, without prejudice to innocent socios'/administrators' recourse for excess paid against the culpable ones | `sv/sources/07_Codigo_Comercio.pdf` | Art. 101 p.21 (EVID-219; txt PAGE 21) |
| LB-019 | Código de Comercio, Art. 102: "Las participaciones sociales nunca estarán representadas por títulos valores y no pueden cederse sino en los casos y con los requisitos que establece el presente Código." "Puede estipularse que haya una o varias categorías de participaciones sociales determinando en qué consisten las modalidades respectivas." Art. 103: "El capital social no puede ser inferior a dos mil dólares de los Estados Unidos de América; se dividirá en participaciones sociales que pueden ser de valor y categoría diferentes, pero que en todo caso serán de un dólar o de un múltiplo de uno. No se admite aporte industrial." | Social participaciones are NEVER represented by títulos valores and may only be transferred in the cases and with the requirements this Code establishes. The escritura may stipulate one or several categories of participaciones, defining the respective modalities. The social capital may not be less than TWO THOUSAND US DOLLARS; it divides into participaciones which may be of different value and category, but in every case of ONE DOLLAR or a multiple of one. Industrial (work) aportation is not admitted | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 102-103 p.21 (EVID-219; txt PAGE 21) |
| LB-020 | Código de Comercio, Art. 106: "Al constituirse la sociedad, el capital social deberá estar íntegramente suscrito. Deberá exhibirse como mínimo el cinco por ciento del valor de cada participación social. El pacto social establecerá la manera y plazo en que deberá pagarse la parte insoluta del capital suscrito, el cual no podrá exceder de un año a partir de la fecha de inscripción de la escritura de constitución en el Registro de Comercio, salvo que el capital social suscrito fuere superior a cien mil dólares, en cuyo caso el plazo será de cinco años." "El pago en efectivo debe acreditarse ante el Notario que autoriza la escritura social por medio de cheque certificado o cheque de caja o de gerencia, librado contra un banco autorizado por la Superintendencia del Sistema Financiero para operar en el país. El Notario relacionará en el instrumento los datos que identifiquen el cheque." "Los que suscriben el contrato social responden solidariamente respecto de terceros por la parte del capital que no se pagare íntegramente en dinero efectivo y por el valor atribuido a los bienes aportados en especie." | At constitution the social capital must be WHOLLY SUBSCRIBED; at least FIVE PERCENT of the value of each participación must be exhibited (paid in). The pacto social fixes the manner and term for paying the unpaid balance — not exceeding ONE YEAR from the inscription date of the constitutive deed, unless the subscribed capital exceeds one hundred thousand dollars, in which case the term is FIVE YEARS. Cash payment must be evidenced before the Notary authorizing the deed by certified cheque, cashier's cheque or gerencia cheque drawn on a bank authorized by the SSF to operate in the country; the Notary records the cheque's identifying data in the instrument. The subscribers answer SOLIDARILY towards third parties for the part of capital not wholly paid in cash and for the value attributed to goods contributed in kind | `sv/sources/07_Codigo_Comercio.pdf` | Art. 106 pp.21-22 (EVID-219; txt PAGE 21-22) |
| LB-021 | Código de Comercio, Art. 112: "En los aumentos de capital social se observarán las mismas reglas de la constitución de la sociedad, y los socios tendrán preferencia para suscribirlo, en proporción a sus participaciones sociales; a este efecto, si no hubieran asistido a la Asamblea en que se aprobó el aumento, deberá comunicárseles el acuerdo respectivo por medio de carta certificada, con acuse de recibo. Si algún socio no ejerce el derecho que este artículo le confiere, dentro de los quince días siguientes a la celebración de la Asamblea o al de la notificación en su caso, se entenderá que renuncia a él, y el aumento de capital podrá ser suscrito, bien por los otros socios, bien por personas extrañas a la sociedad, en los casos y con los requisitos que señala el artículo 50. Ni la escritura social, ni la Asamblea de la sociedad puede privar a los socios de la facultad de suscribir preferentemente los aumentos de capital." | Capital INCREASES follow the same rules as constitution, and socios have PREFERENCE to subscribe them in proportion to their participaciones; if they did not attend the assembly approving the increase, the agreement must be communicated by CERTIFIED LETTER with acknowledgment of receipt. If a socio does not exercise this right within FIFTEEN DAYS of the assembly or of the notification, he is deemed to renounce it, and the increase may be subscribed by the other socios or by outsiders in the cases and with the requirements of Art. 50. Neither the escritura nor the assembly may deprive socios of the preferential-subscription faculty | `sv/sources/07_Codigo_Comercio.pdf` | Art. 112 p.22 (EVID-219; txt PAGE 22) |
| LB-022 | Código de Comercio, Art. 113: "La sociedad llevará un libro especial de Registro de Socios que permanecerá en poder del administrador, quien será responsable de su existencia, de su conservación y de las oportunas y exactas anotaciones que en él se hagan. El libro podrá ser consultado por los socios y aún por quien demuestre legítimo interés en ello, y contendrá: I.- Las generales de cada uno de los socios y su dirección postal. II.- El número, valor y categoría de las participaciones sociales, incluyéndose los datos del caso en materia de copropiedad y el nombre del representante común. III.- Los datos relativos a la suscripción y exhibición del capital, así como el plazo que se hubiere concedido para la liquidación de la participación insoluta y las garantías otorgadas por los suscriptores respectivos. IV.- La referencia a todo aumento y reducción de capital y al modo en que ello afecte al número y valor de las participaciones sociales. V.- Los datos relativos a enajenación y adquisición de cuotas sociales, gravámenes sobre los derechos que éstas confieren, sucesiones hereditarias de los socios y cualesquiera otros análogos. VI.- Los efectos producidos en cuanto a las participaciones sociales, en los casos de retiro y exclusión de socios. VII.- Los demás datos que conforme a la ley o a juicio del administrador o de la asamblea, hayan de incluirse." "Corresponde al administrador extender las certificaciones del Registro a su cargo." "La falta de Registro de Socios hará que se considere la Sociedad como irregular y se le imponga la sanción que establece el Art. 354." | The SRL keeps a special Registro de Socios (partners' register) book remaining in the ADMINISTRATOR's custody, responsible for its existence, conservation and the opportune and exact annotations made in it; consultable by the socios and by anyone showing legitimate interest. Contents: I. the particulars of each socio and postal address; II. number, value and category of the participaciones, including copropiedad data and the common representative's name; III. subscription and exhibition (payment-in) data, the term granted for settling the unpaid participación and the guarantees granted by the respective subscribers; IV. reference to every capital increase and reduction and how it affects the number and value of participaciones; V. data on transfer and acquisition of cuotas, encumbrances over the rights they confer, hereditary successions and any analogous events; VI. effects on participaciones in cases of socio retirement and exclusion; VII. further data required by law or judged includable by the administrator or the assembly. The administrator extends the register's certifications. ABSENCE of the Registro de Socios renders the society IRREGULAR, sanctionable per Art. 354 | `sv/sources/07_Codigo_Comercio.pdf` | Art. 113 pp.22-23 (EVID-219; txt PAGE 22-23) |
| LB-023 | Código de Comercio, Art. 119 (first inciso): "La junta se instalará válidamente si concurren socios que representen, por lo menos, la mitad del capital social, a no ser que la escritura social exija una asistencia más elevada. Salvo estipulaciones en contrario, si dicha asistencia no se obtiene en la primera reunión, los socios serán convocados por segunda vez, con intervalo de dos días, y la Asamblea funcionará válidamente cualquiera que sea el número de los concurrentes." Art. 120: "Todo socio tiene derecho a participar en las juntas y goza de un voto por cada dólar de los Estados Unidos de América de su aportación, salvo lo que el pacto social establezca sobre participaciones privilegiadas." Art. 121: "Las resoluciones se tomarán por mayoría de los votos de los que concurran a la asamblea, excepto en los casos de modificación de la escritura social, para la cual se requerirá, por lo menos, el voto de las tres cuartas partes del capital social a no ser que se trate del cambio de los fines de la sociedad o que la modificación aumente las obligaciones de los socios, casos en los que se requerirá la unanimidad de votos." [final sentence] | The SRL junta is validly installed if socios representing at least HALF the social capital attend, unless the escritura requires higher attendance; absent contrary stipulation, if that attendance is not obtained at the first meeting, socios are reconvened with a two-day interval and the assembly validly functions with ANY number of attendees. Every socio has the right to participate in juntas and enjoys ONE VOTE PER DOLLAR of his aportation, save what the pacto social establishes on privileged participaciones. Resolutions are taken by majority of the votes of those attending — EXCEPT escritura-social modifications, which require at least THREE-FOURTHS of the social capital, unless it is a change of the society's ends or a modification increasing the socios' obligations, which require UNANIMITY | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 119-121 p.24 (EVID-219; txt PAGE 24) |
| LB-024 | Código de Comercio, Art. 122: "Cuando la escritura social lo establezca, se procederá al nombramiento de un Consejo de Vigilancia. Los miembros de este Consejo podrán ser socios o personas extrañas a la sociedad." "En todo caso, se nombrará un auditor que fiscalizará las operaciones de la sociedad; dictaminará sobre los estados contables de la misma y los certificará cuando los encuentre correctos." | When the escritura so establishes, a Consejo de Vigilancia (vigilance council) is appointed — members may be socios or outsiders. IN EVERY CASE an auditor is appointed who inspects (fiscaliza) the society's operations, issues his dictamen on the accounting statements and certifies them when he finds them correct — the SRL auditor is MANDATORY | `sv/sources/07_Codigo_Comercio.pdf` | Art. 122 p.24 (EVID-219; txt PAGE 24) |
| LB-025 | Código de Comercio, Art. 127: "En las sociedades de capitales, los accionistas limitarán su responsabilidad al valor de sus acciones." Art. 129: "Las acciones serán de un valor nominal de un dólar de los Estados Unidos de América o múltiplos enteros de uno." Art. 133: "Se prohíbe a las sociedades de capitales colocar sus acciones a un precio inferior a su valor nominal." "También se les prohíbe emitir acciones cuyo valor no sea el producto de una aportación real, presente o futura." | In capital societies, accionistas LIMIT their liability to the value of their acciones. Acciones carry a nominal value of ONE US DOLLAR or whole multiples of one. Capital societies are PROHIBITED from placing acciones at a price below nominal value, and from issuing acciones whose value is not the product of a real aportation, present or future | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 127, 129 p.25; Art. 133 p.26 (EVID-220; txt PAGE 25-26) |
| LB-026 | Código de Comercio, Art. 134: "Las acciones serán siempre nominativas, mientras su valor no se haya pagado totalmente." "Una vez satisfecho por completo el valor nominal de las acciones, los interesados podrán exigir que se les extiendan títulos al portador, siempre que la escritura social no lo prohíba." "Antes de la entrega de las acciones a los suscriptores, la sociedad podrá extenderles títulos provisionales representativos de las suscripciones hechas, los cuales quedarán para todos los efectos equiparados a las acciones." "Los títulos representativos a que se refiere el inciso anterior, tendrán una vigencia máxima de un año a partir de la fecha de su expedición y transcurrido el mismo, los administradores de la sociedad tendrán la obligación de canjearlos por títulos definitivos a favor de los accionistas que aparezcan inscritos como tales en el Libro de Registro respectivo." "Los administradores que contravengan la obligación del inciso precedente, serán personal y solidariamente responsables de los daños y perjuicios que se causen a los accionistas." | Acciones are ALWAYS NOMINATIVE while their value is not wholly paid. Once the nominal value is completely satisfied, interested parties may demand bearer titles, provided the escritura does not forbid it. Before delivering acciones to subscribers, the society may issue PROVISIONAL titles representing the subscriptions, equated for all effects to acciones; those titles have a maximum validity of ONE YEAR from issuance, after which the administrators are OBLIGED to exchange them for definitive titles in favour of the accionistas inscribed in the respective register book. Administrators contravening that obligation are personally and solidarily liable for damages to the accionistas | `sv/sources/07_Codigo_Comercio.pdf` | Art. 134 p.26 (EVID-220; txt PAGE 26) |
| LB-027 | Código de Comercio, Art. 141: "Se prohíbe a las sociedades de capitales adquirir sus propias acciones, salvo por remate o adjudicación judicial." "En este caso, la sociedad venderá las acciones dentro de tres meses, a partir de fecha en que legalmente pueda disponer de ellas; y si no lo hiciere en ese plazo, se procederá a la reducción de capital y a la consiguiente cancelación de las acciones." "En tanto pertenezcan las acciones a la sociedad, no podrán ser representadas en las asambleas de accionistas." Art. 142: "En ningún caso podrán las sociedades de capitales hacer préstamos o anticipos sobre las acciones que emitan." Art. 143: "Los administradores que contravengan las disposiciones de los dos artículos precedentes, serán personal y solidariamente responsables de los daños y perjuicios que se causen a la sociedad o a sus acreedores." | Capital societies are PROHIBITED from acquiring their OWN acciones, except by judicial auction (remate) or adjudication. In that case the society must SELL the acciones within THREE MONTHS from the date it may lawfully dispose of them; failing that, capital is reduced and the acciones cancelled. While the acciones belong to the society they may NOT be represented in the accionistas' assemblies. In NO case may capital societies make LOANS OR ADVANCES on the acciones they issue. Administrators contravening the two preceding articles are personally and solidarily liable for damages to the society or its creditors | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 141-143 p.27 (EVID-220; txt PAGE 27) |
| LB-028 | Código de Comercio, Art. 149 (ordinals I-VII): "Los títulos de las acciones y los certificados provisionales o definitivos, deben contener: I.- La denominación, domicilio y plazo de la sociedad. II.- La fecha de la escritura pública, el nombre del Notario que la autorizó y los datos de la inscripción en el Registro de Comercio, aunque éstos podrán omitirse en los certificados provisionales, si no se hubiere efectuado el registro. III.- El nombre del accionista, en el caso de que los títulos sean nominativos. IV.- El importe del capital social, el número total y el valor nominal de las acciones. V.- La serie y número de la acción o del certificado, con indicación del número total de acciones que corresponda a la serie. VI.- Los llamamientos que sobre el valor de la acción haya pagado el accionista, o la indicación de estar totalmente pagada. VII.- La firma de los administradores que conforme a la escritura social deban suscribir el título." [following incisos omitted — capital-change annotations required on titles: new capital amount and circulating acción count; under capital variable, the junta-agreement date/acta data; under capital fijo, the modification deed, notary and registry data — per Art. 151 exchange rules] Art. 155: "Las sociedades de capitales que emitieren acciones nominativas llevarán un registro de las mismas, que contendrá: I.- El nombre y el domicilio del accionista; la indicación de las acciones que le pertenezcan, expresándose los números, series, clases y demás particularidades. II.- Los llamamientos que se efectúen. III.- Los traspasos que se realicen. IV.- La conversión de las acciones nominativas en acciones al portador. V.- Los canjes de títulos. VI.- Los gravámenes que afecten a las acciones y los embargos que sobre ellas se trabaren. VII.- Las cancelaciones de los gravámenes y embargos. VIII.- Las cancelaciones de los títulos." | Action titles and provisional/definitive certificates must contain: I. the society's denominación, domicile and term; II. the public deed's date, the authorizing Notary's name and the Commerce Registry inscription data (omissible in provisional certificates if not yet registered); III. the accionista's name for nominative titles; IV. the social capital amount, total number and nominal value of acciones; V. the acción/certificate series and number, with the series' total acción count; VI. the llamamientos (call payments) the accionista has made, or the indication of being fully paid; VII. the signature of the administrators who per the escritura must subscribe the title. (Following incisos: capital-change annotations on titles per regime, exchanged per Art. 151.) Societies issuing NOMINATIVE acciones keep a register of them containing: I. accionista name and domicile; indication of his acciones with numbers, series, classes and other particulars; II. the llamamientos effected; III. traspasos (transfers) realized; IV. conversion of nominative into bearer acciones; V. title exchanges (canjes); VI. encumbrances (gravámenes) affecting the acciones and attachments (embargos) laid on them; VII. cancellations of encumbrances and attachments; VIII. cancellations of titles | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 149, 155 pp.28-30 (EVID-220; txt PAGE 28-30) |
| LB-029 | Código de Comercio, Art. 157: "Salvo pacto en contrario, los accionistas tienen derecho preferente, en proporción a sus acciones, para suscribir las que se emitan en caso de aumento del capital social. Este derecho debe ejercitarse dentro de los quince días siguientes a la publicación del acuerdo respectivo." | Save contrary pact, accionistas have a PREFERENTIAL RIGHT, in proportion to their acciones, to subscribe those issued upon capital increase. This right must be exercised within FIFTEEN DAYS following the publication of the respective agreement | `sv/sources/07_Codigo_Comercio.pdf` | Art. 157 p.30 (EVID-220; txt PAGE 30) |
| LB-030 | Código de Comercio, Art. 289: "La vigilancia de la sociedad anónima, estará confiada a un auditor designado por la junta general, la cual señalará también su remuneración. El auditor ejercerá sus funciones por el plazo que determine el pacto social y, en su defecto, por el que señale la junta general en el acto del nombramiento." Art. 290: "La Auditoría a que se refiere el artículo anterior es la externa. Una Ley especial regulará su ejercicio." "La vigilancia de los contadores públicos será ejercida por un Consejo de Vigilancia que tendrá la organización y atribuciones que dicha ley le confiera." "El cargo de auditor es incompatible con el de administrador, gerente o empleado subalterno de la sociedad. No podrán ser auditores los parientes de los administradores o gerentes de la sociedad, dentro del cuarto grado de consanguinidad o segundo de afinidad." Art. 291: "Son facultades y obligaciones del auditor: I.- Cerciorarse de la constitución y vigencia de la sociedad. II.- Cerciorarse de la constitución y subsistencia de la garantía de los administradores y tomar las medidas necesarias para corregir cualquiera irregularidad. III.- Exigir a los administradores un balance mensual de comprobación. IV.- Comprobar las existencias físicas de los inventarios. V.- Inspeccionar una vez al mes, por lo menos, los libros y papeles de la sociedad, así como la existencia en caja. VI.- Revisar el balance anual, rendir el informe correspondiente en los términos que establece la ley y autorizarlo al darle su aprobación. VII.- Someter a conocimiento de la administración social y hacer que se inserten en la agenda de la junta general de accionistas, los puntos que crea pertinentes. VIII.- Convocar las juntas generales ordinarias y extraordinarias de accionistas, en caso de omisión de los administradores y en cualquiera otro en que lo juzgue conveniente. IX.- Asistir, con voz, pero sin voto, a las juntas generales de accionistas. X.- En general, comprobar en cualquier tiempo las operaciones de la sociedad." | S.A. vigilance is confided to an auditor designated by the junta general, which also sets his remuneration; he serves the term fixed by the pacto social or, failing it, by the junta at appointment. The audit is EXTERNAL; a special law governs its exercise and a Vigilance Council watches public accountants. The auditor office is INCOMPATIBLE with being administrator, gerente or subordinate employee of the society; relatives of administrators/gerentes within the fourth degree of consanguinity or second of affinity may not be auditors. Auditor faculties and duties: I. verify the society's constitution and vigencia; II. verify the administrators' guarantee and correct irregularities; III. demand from the administrators a MONTHLY verification balance (balance mensual de comprobación); IV. verify physical inventory existence; V. inspect at least ONCE A MONTH the society's books and papers and the cash on hand; VI. revise the ANNUAL balance, render the report the law establishes and authorize it by approval; VII. submit points to the administration and the junta agenda; VIII. convene ordinary/extraordinary juntas on administrators' omission or when he judges convenient; IX. attend juntas with voice but without vote; X. verify the society's operations at any time | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 289-291 pp.54-55 (EVID-220; txt PAGE 54-55) |
| LB-031 | Código de Comercio, Art. 236: "A partir de la publicación de la convocatoria, los libros y documentos relacionados con los fines de la junta estarán en las oficinas de la sociedad, a disposición de los accionistas, para que puedan enterarse de ellos." "Si el pacto social hubiere subordinado el ejercicio de los derechos de participación al depósito de los títulos de las acciones con cierta anticipación, el plazo de la convocatoria se fijará de tal modo que los accionistas dispongan, por lo menos, de ocho días para practicar el depósito en cuestión, el cual podrá hacerse en cualquiera institución bancaria, si no se hubiere indicado una determinada en la convocatoria." | From the publication of the convocatoria (meeting call), the books and documents related to the junta's purposes are at the society's offices AT THE ACCIONISTAS' DISPOSAL for their information. If the pacto social subordinated participation rights to depositing the action titles with some anticipation, the convocatoria term is fixed so accionistas have at least EIGHT DAYS to make the deposit — doable at any banking institution unless one is designated in the call | `sv/sources/07_Codigo_Comercio.pdf` | Art. 236 p.45 (txt PAGE 45; mechanics deferred to this file by `03_financial-statements.md` LB-005) |
| LB-032 | SAS existence evidence (non-statutory pointer LB): 71-73_ evidence EVID-250 gloss: "SAS existence (creaempresa.cnr.gob.sv 'Asesoría virtual SAS' + btn-sas) under separate legislation remains consistent with BOTH lists (no CC reform) — SOQ-23 open." And OQ-5: "SAS law identity still unpinned (SOQ-23): official CNR creaempresa portal confirms SAS services exist (Asesoría virtual SAS; eCNR login for constitution flow); the statute itself (number/date) not identifiable with asamblea + D.O. down; law-firm mirrors are NOT official (do not register). Keep open; company-type menu FR gets an extensible-type design + OQ." | The simplified joint-stock company (SAS) EXISTS as a company type under separate legislation (official CNR creaempresa portal confirmation), but its statute is not in the corpus and its identity is unpinned; two official CC consolidations list no SAS-amending reform. Consequence: extensible-type design with statute-pending flag; no invented mechanics | `sv/.extractions/71-73_AML_DL426_Instructivo380_CCverify.evidence.md` (pointer LB per task design; statutory SAS text NOT in corpus) | EVID-250 gloss + OQ-5 (SOQ-23; origin: 07_ OQ-2 carried) |

## 3. Functional Requirements

### 3.1 Type taxonomy and the extensible company-type model (Arts. 17-19; SAS)

- **SV-CML-FR-042:** The system shall model the sociedad as the Art. 17
  *comerciante social* — the juridical entity resulting from a *contrato
  solemne* between two or more persons pooling *bienes o industria* to
  share profits, enjoying legal personality within its purpose limits —
  and shall classify every sociedad record with the Art. 18 taxonomy:
  class ∈ {*de personas* (colectiva · comandita simple · SRL) · *de
  capitales* (S.A. · comandita por acciones)} × capital regime ∈
  {capital fijo · capital variable}, remembering that BOTH classes may be
  of variable capital; the Art. 18 closing rule — ONLY law-regulated
  forms may be constituted — is the textual basis of the EXTENSIBLE,
  profile-driven type model (§4): the type list is a data table, not a
  hardcoded enum, so law-created types (e.g. SAS, FR-044) attach without
  schema change. (LB-001; EVID-218)
- **SV-CML-FR-043:** The system shall carry the Art. 19 cooperative
  profile as a distinct society type with its special rules: minimum TEN
  socios; governance = the rules of the adopted species PLUS the S.A.
  rules on balances, administrator liability and auditor vigilance (save
  Art. 19's modifications); actions nominative and transmissible ONLY by
  inscription in the respective book with the society's authorization;
  per-action cap — each action of no more than ¢5,000.00 (COLONES
  remnant, SOQ-29: historical code text, operative reading USD —
  value-level use flagged, OQ-002); ONE VOTE per socio regardless of
  actions owned (overriding voto-por-dólar defaults); the Art. 19-V
  socio book at the domicile (examinable by anyone); the mandatory
  suffix "Sociedad Cooperativa de Responsabilidad Limitada" o
  "Ilimitada"; and tax-subject status (the printed capital/yields
  exemption was derogated by D.L. 385-1989 — no exemption logic ships).
  (LB-002; EVID-218)
- **SV-CML-FR-044:** The system shall implement the SAS
  extensible-type design per the SOQ-23 ruling: the company-type
  selection carries `sas` (Sociedad por Acciones Simplificada) as a
  CONFIRMED-EXISTING type — existence evidenced by the official CNR
  creaempresa portal (LB-032) — whose statute is NOT in the corpus; the
  `sas` type record ships with a statute-pending flag and the OQ-001
  pointer, and with NO mechanics of its own: no suffix rule, no capital
  minimum, no quorum rule, no reserve rate, no ledger profile are
  invented — every such field renders as statute-pending config-gaps
  until the SAS law lands (acquisition candidate, sources registry
  numbering ≥74). (LB-001; LB-032; SOQ-23)

### 3.2 Formation (Arts. 21-27)

- **SV-CML-FR-045:** The system shall record every sociedad lifecycle
  act of the Art. 21 family — constitution, modification,
  transformation, fusión and liquidation — as executed by *escritura
  pública* (public deed), tracking the deed (notary, date, instrument
  reference) as the formality anchor of each act; acts of the family
  without a recorded deed are flagged as formally defective.
  (LB-003; EVID-218)
- **SV-CML-FR-046:** The system shall capture the constitutive deed
  against the Art. 22 twelve-field content checklist: (I) identity of
  integrating persons — naturals with name/age/occupation/nationality/
  domicile, juridicals with name/nature/nationality/domicile; (II)
  society domicile WITH municipio and departamento; (III) naturaleza
  jurídica (type); (IV) finalidad; (V) razón social o denominación;
  (VI) duration or express indeterminate-term declaration; (VII)
  capital amount — when variable, the MINIMUM; (VIII) each socio's
  aportation in money or other goods WITH the value attributed to the
  latter; (IX) administration regime with organs' names/faculties/
  obligations; (X) profit-distribution and loss-application manner;
  (XI) mode of constituting reserves; (XII) liquidation bases and
  liquidator selection/attribution — plus the per-class special
  requirements this Code adds (SRL/S.A. profiles, §3.6/3.7); omission
  of any ordinal I-IX marks the deed NULL (Art. 27) while omission of
  X, XI or XII instead falls back to the Code's pertinent provisions —
  the checklist computes the nullity/fallback outcome per field.
  (LB-004; LB-007; EVID-218)
- **SV-CML-FR-047:** The system shall track the Art. 23 estatutos
  (bylaws) regime: estatutos develop the socios-society rights and
  obligations GROUNDED ON the pacto social clauses and may not
  contradict them (contradiction check surfaces as a validation
  warning — substantive review is legal, not computational); estatutos
  are decreed by the *junta general extraordinaria* and must appear
  integrally in the approving acta; a certification of that acta is
  DEPOSITED in the Registro de Comercio (registry-entry link, kind
  instrumento_social per SV-CML-FR-013); and a copy of the estatutos
  is delivered to each socio — reproducible by any means — carrying
  the Registry deposit number.
  (LB-005; EVID-218)
- **SV-CML-FR-048:** The system shall encode legal personality as an
  INSCRIPTION-PERFECTED attribute (Art. 25): a sociedad record's
  personality is perfected ONLY by the inscription of the respective
  document in the Registro de Comercio — and extinguished the same
  way — so pre-inscription records carry a no-personality marker and
  cannot hold personality-dependent states; inscriptions determine,
  towards third parties, the representatives'/administrators'
  faculties per their content (presentation timestamp = effect anchor
  per SV-CML-FR-016); inscribed societies cannot be declared null
  with retroactive effect against third parties. The inscription
  catalogue (Arts. 24/465-I) — deeds of constitution, modificación,
  transformación, fusión and liquidación + certifications of executed
  dissolution/liquidation judgments + acta-point certifications — maps
  onto the registry-entry model of SV-CML-FR-013 (book documentos,
  particular register instrumentos sociales); constitution
  inscription opens the matrícula obligation per SV-CML-FR-008
  (consumed by id). The matrícula-precondition gate (SV-CML-FR-015)
  binds participating-merchant documents, not the society's own
  constitutive inscription.
  (LB-006; EVID-217/218)

### 3.3 Capital (Arts. 29-33)

- **SV-CML-FR-049:** The system shall implement the Art. 29 capital
  invariant: *capital social* = the SUM of the values set in the deed
  for the aportations PROMISED by the socios (subscribed, not
  necessarily paid); capital figures ALWAYS on the liability side of
  the balance (Odoo capital accounts on the credit side — pasivo-side
  presentation); and the patrimony must contain a set of goods of
  value at least EQUAL to the capital amount — surfaced as an
  assets-≥-capital guard (computed check: net assets backing ≥ capital
  social; breach = warning state, since valuation is the auditor's
  act, not the system's).
  (LB-008; EVID-218)
- **SV-CML-FR-050:** The system shall record capital changes per
  Art. 30: increase/reduction requires the socios' consent in the
  form of the society's class (quorum rules per type profile,
  FR-063/070 kin); revaluation-driven asset increases may pass to the
  capital account or to a special reserve NOT distributable until the
  revalued goods are alienated AND the plusvalía received in cash
  (consumes the Art. 445 discipline of SV-CML-FR-041 by id); the
  capital-increase agreement publishes ONCE in a national daily AND
  the Diario Oficial; the capital-reduction agreement publishes per
  Art. 486 (engine = SV-CML-FR-017 by id) with a 30-day opposition
  window for creditors, interested third parties and the Ministerio
  Público counted from the THIRD publication (creditor opposition
  ends as of right by payment); both agreements are communicated to
  the state vigilance office; and only past the unopposed/
  extinguished/dismissed stage may the reduction be formalized — the
  deeper capital-VARIABLE movement mechanics (Arts. 306-314) are
  owned by `05_society-lifecycle.md` when it lands (pointer, never
  restated).
  (LB-009; EVID-218/221)
- **SV-CML-FR-051:** The system shall validate aportation
  admissibility per Arts. 31/33: every aportation must be a good of
  economic value (value expressed in national currency = colones-era
  remnant read against dollarization — recorded in USD, §2); WORK
  aportation is prohibited in *sociedades de capitales* (and SRL,
  Art. 103 — no aporte industrial) while remaining the *socio
  industrial* figure elsewhere (Art. 35 profit rules); mere
  assumption of liability is never a valid aportation; absent contrary
  pact, non-money aportations are ownership-transferring, with risk on
  the society from delivery and the aportante answering evicción y
  saneamiento per the Civil-Code sale rules (warranty metadata, not
  computation); aportations fall due at deed execution or at the
  stipulated epoch/form — *mora* unlocks judicial enforcement by the
  ejecutivo route, no socio may invoke another's non-performance to
  withhold his own, and non-performance damages liability attaches.
  (LB-010; EVID-218)
- **SV-CML-FR-052:** The system shall apply the Art. 32 special
  valuation/warranty rules to non-cash aportations: CREDIT aportations
  carry the contributor's warranty of existence, legitimacy and
  debtor solvency plus the no-cancellation/reivindication warranty for
  títulos valores (recorded as warranty metadata on the aportation;
  pact against this article is prohibited — no waiver field); and
  aportations consisting of capital-society ACCIONES are valued at no
  more than their *valor contable* (book value) so long as no Bolsa de
  Valores exists in the country — an over-book-value valuation is
  blocked with the article reason (existence of a Bolsa = dated
  config slot, no shipped value).
  (LB-011; EVID-218)

### 3.4 Dividend ceiling and the statutory reserva legal (Arts. 37-39, 91-92, 123-124, 295, 616)

- **SV-CML-FR-053:** The system shall enforce the Arts. 37-38 dividend
  ceiling: NO distribution or assignment of profits may exceed the
  profits REALLY obtained, per the *balance general* and *estado de
  pérdidas y ganancias* (the realized-per-balance ceiling computed
  against the FY's statements — the approved/deposited cycle of
  `03_financial-statements.md` by id); any CAPITAL LOSS must be
  restored (or reduced per Art. 444-7º) BEFORE any distribution;
  payments contrary to the ceiling engage the administrators'
  (authorization) and socios' (receipt) SOLIDARY restitution duty,
  demandable by the society, creditors or dissenting socios (the
  system computes the ceiling and flags excess; the restitution
  cause of action is external law); the UNIQUE exception — the socio
  industrial's periodic alimentary sums, judicially fixable, accounted
  against profits without restitution when profits fall short and
  transferred to general expenses — is recorded as the only permitted
  payment class outside the ceiling.
  (LB-012; EVID-218)
- **SV-CML-FR-054:** The system shall implement the Art. 39 reserva
  legal CHASSIS (mandatory, non-waivable — "contra lo dispuesto en
  este artículo no puede invocarse estipulación o pacto en
  contrario"): from every sociedad's NET profits a percentage is
  separated ANNUALLY until the reserve reaches the determined
  quantity (percentage and quantum per class — FR-055); when the
  reserve DIMINISHES for any motive it must be RESTORED in the same
  form (restoration duty = recomputation trigger on any reserve
  decrease); administrators are solidarily responsible and must
  restitute a missing or partial reserve (recourse against receivers
  preserved); and the statutory action belongs to socios, creditors
  or the Ministerio Público (exposure recorded, not litigated).
  (LB-013; EVID-218)
- **SV-CML-FR-055:** The system shall configure the reserva legal
  rates PER TYPE from the Code's type profiles: (a) *colectiva* AND
  *comandita simple* (via Art. 100) — 5% of net profits annually, to
  a LEGAL LIMIT of ONE-SIXTH of capital social (Arts. 91/100:
  separation STOPS at 1/6); (b) *SRL*, *S.A.* (via Art. 295) and
  *EIRL* (via Art. 616-I, profile owned by
  `07_empresa-mercantil-eirl.md`) — 7% of net profits annually, to a
  MINIMUM LEGAL limit of ONE-FIFTH of capital social (Arts. 123/295/
  616: the 1/5 is a floor — separation continues until at least 1/5
  is reached); (c) the cooperative's *Fondo de Reserva* interacts with
  the Art. 19-XI exclusion-withdrawal rule (withdrawal per last
  balance EXCLUDES the Fondo de Reserva — recorded as the cooperative
  profile's reserve-exclusion flag); types without Code rates (e.g.
  SAS, statute-pending) carry config-gap slots with NO shipped
  values. Disambiguation (by id, §2): this statutory reserve is a
  DIFFERENT institution from the Art. 445 revaluation reserve
  (SV-CML-FR-041) and from the ISR *reserva legal* book reserve
  (SV-TAX-FR-063 constitution register + SV-TAX-FR-101 25%
  separate-liquidation computation — taxation wave by id; no ISR rule
  is derived or restated here).
  (LB-014; LB-015; LB-016; EVID-218/219/220/224)
- **SV-CML-FR-056:** The system shall record the reserve DEPLOYMENT
  constraints: colectiva-family reserves (Arts. 91/92 via 100) — HALF
  kept available or invested in readily realizable SALVADORAN
  mercantile securities, half investible per the society's purpose;
  SRL/S.A./EIRL reserves (Arts. 124 via 295/616-I) — TWO-THIRDS kept
  available or invested in readily realizable Salvadoran OR
  CENTRAL-AMERICAN mercantile securities, the remaining third
  investible per the society's purpose (deployment classification
  metadata on the reserve account; realizability is an auditor
  judgment, recorded not computed).
  (LB-014; LB-015; EVID-218/219)

### 3.5 Society books (Art. 40)

- **SV-CML-FR-057:** The system shall maintain the Art. 40 society
  book set as statutory registers: (I) *Libro de Actas de las Juntas
  Generales* (general-meeting minutes — the agreements adopted);
  (II) *Libro de Actas de Juntas Directivas o de Consejos de
  Administración*, per the society's nature and administration
  regime; (III) *Libro de Registro de Socios o de Accionistas*, per
  the society's nature (content profiles per type — FR-062 SRL,
  FR-068 S.A.); (IV) *Libro de Registro de Aumentos y
  Disminuciones de Capital Social*, REQUIRED when the capital-variable
  regime is adopted (book existence gate keyed to the capital-regime
  field; movement mechanics owned by `05_society-lifecycle.md` when it
  lands); books are legalized by *contadores públicos* or by the
  Registro de Comercio (legalization tracked via the book model of
  SV-CML-FR-022, whose register_kind set gains the society kinds);
  and every society book inherits the Art. 440 discipline flags
  (castellano/USD/in-country, no-alteration — SV-CML-FR-025 by id)
  plus retention row a (SV-CML-FR-028 by id).
  (LB-017; EVID-213/218)

### 3.6 SRL profile (Arts. 101-125)

- **SV-CML-FR-058:** The system shall enforce the SRL naming rule:
  the sociedad may constitute under *razón social* (name of one or
  more socios) or *denominación* (freely formed, distinct from any
  existing society), either IMMEDIATELY followed by "Limitada" or its
  abbreviation "Ltda."; omission in the escritura renders ALL socios
  — and for later acts the administrators — solidarily and
  unlimitedly liable for obligations so contracted (suffix-validation
  warning with the liability-exposure note; innocent-party recourse
  recorded). (LB-018; EVID-219)
- **SV-CML-FR-059:** The system shall validate SRL capital structure:
  capital social ≥ US$2,000 (2008-reform USD code text —
  dated-but-current, dated config, never hardcoded); divided into
  participaciones of different value/category allowed but EACH of
  US$1 or a whole multiple of US$1 (denomination validator:
  participación value mod 1 = 0); participaciones NEVER represented
  by títulos valores (no share-certificate objects for SRL — ledger
  only); categories with their modalities only as escritura-stipulated;
  and NO aporte industrial (work aportation blocked — read with
  FR-051's capital-society prohibition). (LB-019; EVID-219)
- **SV-CML-FR-060:** The system shall enforce SRL subscription and
  exhibition discipline (Art. 106): at constitution the capital must
  be INTEGRALLY subscribed; at least 5% of each participación's value
  exhibited; the unpaid balance payable per the pacto social within
  ONE YEAR of the deed's inscription — FIVE YEARS if subscribed
  capital exceeds US$100,000 (threshold = 2008 USD code text,
  dated-but-current config); cash payments evidenced before the
  authorizing Notary by certified/cashier/gerencia cheque drawn on an
  SSF-authorized bank (cheque identifying data recorded on the
  aportation); and the subscribers' solidarity for the non-cash-paid
  part and for in-kind valuations recorded as exposure metadata.
  (LB-020; EVID-219)
- **SV-CML-FR-061:** The system shall implement the SRL
  capital-increase preference (Art. 112): increases follow the
  constitution rules (FR-060 discipline re-applied); socios hold
  PREFERENTIAL subscription in proportion to their participaciones;
  absent socios are notified by carta certificada with acuse de
  recibo; the preference window is FIFTEEN DAYS from the approving
  assembly or from the notification, lapse = renunciation (then other
  socios or outsiders per Art. 50); and neither escritura nor
  assembly may strip the preference (no waiver flag).
  (LB-021; EVID-219)
- **SV-CML-FR-062:** The system shall implement the SRL *Libro de
  Registro de Socios* with the Art. 113 seven-field content: (I)
  socios' particulars + postal address; (II) number, value and
  category of participaciones, incl. copropiedad data + common
  representative; (III) subscription and exhibition data + unpaid-
  participación settlement term + subscriber guarantees; (IV)
  references to every capital increase/reduction and their effect on
  participación number/value; (V) transfers and acquisitions of cuotas,
  gravámenes on their rights, hereditary successions and analogues;
  (VI) effects of socio retirement/exclusion on participaciones;
  (VII) further data per law or administrator/assembly judgment. The
  book stays in the administrator's custody (responsible for
  existence, conservation and opportune exact annotations) and is
  consultable by socios and by anyone showing legitimate interest;
  the administrator extends its certifications; and ABSENCE of the
  book renders the sociedad IRREGULAR with the Art. 354 sanction
  (irregularity flag + sanction exposure; irregularity machinery
  owned by `05_society-lifecycle.md` when it lands — pointer).
  (LB-022; EVID-219/222)
- **SV-CML-FR-063:** The system shall encode SRL voting and quorum:
  installation quorum = socios representing at least HALF the capital
  (higher only if the escritura requires), with second convocation
  after a two-day interval valid at ANY attendance (absent contrary
  stipulation); every socio votes with ONE VOTE PER DOLLAR of his
  aportation (voto-por-dólar default), save escritura-stipulated
  privileged participaciones; resolutions by majority of attending
  votes — EXCEPT escritura-social modification, requiring at least
  THREE-FOURTHS of the capital social, and cambio de fines or
  obligation-increasing modifications, requiring UNANIMITY (quorum
  engine keyed to resolution class).
  (LB-023; EVID-219)
- **SV-CML-FR-064:** The system shall record the SRL vigilance
  configuration (Art. 122): a Consejo de Vigilancia ONLY when the
  escritura establishes it (members may be socios or outsiders); and
  an AUDITOR APPOINTED IN EVERY CASE — mandatory for every SRL — who
  fiscalizes the operations, dictaminates on the accounting
  statements and certifies them when correct (appointment data on the
  company record; the S.A. auditor-incompatibility rules apply to SRL
  via Art. 125's incorporation of Arts. 289-293 — FR-070 consumed by
  id; dictamen content is the auditor's professional act, referenced
  never generated).
  (LB-024; EVID-219)

### 3.7 S.A. profile (Arts. 126-160, 289-295) + junta document availability (Art. 236)

- **SV-CML-FR-065:** The system shall validate S.A. capital structure:
  accionistas limit liability to the value of their acciones; acciones
  carry a nominal value of US$1 or WHOLE multiples of US$1 (validator:
  nominal mod 1 = 0, 2008 USD code text dated-but-current); placement
  BELOW nominal value is PROHIBITED (issue-price ≥ nominal check); and
  issuing acciones whose value is not the product of a REAL aportation
  (present or future) is prohibited (no empty-issue flag — paired with
  FR-049's assets-≥-capital guard).
  (LB-025; EVID-220)
- **SV-CML-FR-066:** The system shall enforce the S.A. nominative
  regime (Art. 134): acciones are ALWAYS NOMINATIVE while their value
  is not wholly paid (registered-holder invariant until full payment —
  the share ledger's accionista field is mandatory for unpaid
  acciones); once nominal value is fully satisfied, interested parties
  may demand BEARER titles unless the escritura forbids them
  (bearer-conversion gate keyed to payment state + escritura
  permission); provisional titles issued before delivery are equated
  to acciones, valid for at most ONE YEAR from issuance, after which
  administrators MUST exchange them for definitive titles in favour of
  the registered accionistas (exchange clock tracked; contravention =
  administrators' personal-and-solidary liability exposure).
  (LB-026; EVID-220)
- **SV-CML-FR-067:** The system shall implement the own-share
  prohibitions (Arts. 141-143): the society's acquisition of its OWN
  acciones is BLOCKED except by *remate o adjudicación judicial*
  (judicial auction/adjudication — the only exception classes);
  exception-acquired shares must be SOLD within THREE MONTHS from the
  date the society may lawfully dispose of them, failing which
  capital reduction + cancellation follows (resale clock tracked);
  while the acciones belong to the society they carry NO
  representation in the accionistas' assemblies (excluded from voting
  computation); and loans or advances ON the society's own acciones
  are prohibited IN EVERY CASE (no exception class — payment lines
  secured on own acciones blocked outright); contravention engages
  the administrators' personal-and-solidary liability to the society
  and its creditors (exposure recorded).
  (LB-027; EVID-220)
- **SV-CML-FR-068:** The system shall implement the S.A. share
  register with the Art. 155 eight-field content: (I) accionista name
  and domicile + his acciones' numbers, series, classes and other
  particulars; (II) llamamientos effected; (III) traspasos realized;
  (IV) nominative→bearer conversions; (V) title canjes; (VI)
  gravámenes affecting the acciones and embargos laid on them;
  (VII) cancellations of gravámenes/embargos; (VIII) cancellations of
  titles — the ledger (not the certificate) is the S.A. register of
  record; and the Art. 149 title-content profile (7 ordinals:
  denominación/domicilio/plazo; deed date/notary/registry data;
  accionista name for nominative; capital/total acciones/nominal
  value; serie+número with series count; llamamientos paid or
  fully-paid indication; signatures) governs title/certificate
  rendering, including the capital-change annotation incisos (new
  capital + circulating count; regime-specific deed/junta data)
  applied via Art. 151 exchange rules — exchange, never overwrite
  (no-alteration kin, SV-CML-FR-024 by id).
  (LB-028; EVID-220)
- **SV-CML-FR-069:** The system shall implement the S.A.
  preferential-subscription window (Art. 157): save contrary pact,
  accionistas hold a PREFERENTIAL right, proportional to their
  acciones, to subscribe new emissions on capital increase —
  exercisable within FIFTEEN DAYS following publication of the
  respective agreement (window clock anchored to the publication
  record — publication engine consumed from SV-CML-FR-017 by id;
  lapse = window closed; the SRL's Art. 112 fifteen-day assembly/
  notification window of FR-061 is the SRL analogue).
  (LB-029; EVID-220)
- **SV-CML-FR-070:** The system shall implement the S.A. auditor
  regime (Arts. 289-291; incorporated into SRL via Art. 125 and EIRL
  via Art. 616-IV): vigilance confided to an auditor DESIGNATED BY
  THE JUNTA GENERAL, which also sets remuneration, term per pacto
  social or junta; the audit is EXTERNAL (a special law governs its
  exercise — outside corpus, pointer only); INCOMPATIBILITIES — the
  auditor may not be administrator, gerente or subordinate employee,
  and not a relative of administrators/gerentes within the fourth
  degree of consanguinity or second of affinity (appointment-time
  incompatibility check surfaces as a warning; kinship is external
  data); and the auditor's MANDATORY DUTY CALENDAR: a monthly
  *balance mensual de comprobación* demandable from the
  administrators, physical-inventory verification, at-least-monthly
  inspection of books/papers and cash, the annual balance revision +
  report + authorization (cycle consumed from
  `03_financial-statements.md` by id), agenda-insertion and
  junta-convocation rights, voice-without-vote attendance, and
  at-any-time operation verification — tracked as dated duty
  checkpoints on the vigilance record (dictamen/report content is
  the auditor's act; the system tracks existence and dates).
  (LB-030; EVID-220)
- **SV-CML-FR-071:** The system shall implement the Art. 236 junta
  document-availability mechanics (deferred to this file by
  `03_financial-statements.md` LB-005): from the PUBLICATION of the
  convocatoria, the books and documents related to the junta's
  purposes are at the society's offices AT THE ACCIONISTAS'
  DISPOSAL (availability start = convocatoria publication date);
  and if the pacto social subordinates participation rights to
  depositing action titles, the convocatoria term must leave at
  least EIGHT DAYS for the deposit — acceptable at any banking
  institution unless one is designated (deposit-window computation
  and bank-designation slot on the junta/assembly record).
  (LB-031; EVID-214 zone)

## 4. Data Model

Layer semantics: the society-type model is Odoo-native — all entities
live in the client (wave default `odoo`; see §5). The registry (CNR),
the Notary and the auditor are external authorities: the system tracks
their acts (inscriptions, deeds, dictámenes, cheques) as referenced
facts; it never emulates them. The EXTENSIBLE-TYPE design lives in a
profile table consumed by res.company — new law-created types (SAS
today) attach as data rows, never schema changes.

**Society-type model (extensible profile + res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.society.type | code · name · class | char · char · select | shipped rows: colectiva · comandita_simple · srl · sa · comandita_acciones · cooperativa · sas; class = personas · capitales (cooperativa = species-adopted per Art. 19-I — informational) | FR-042 |
| l10n_sv_commerce.society.type | statute_status · pending_oq | select · char | in_corpus · statute_pending (sas → SOQ-23/OQ-001 pointer; mechanics fields render as config-gaps) | FR-044 |
| l10n_sv_commerce.society.type | suffix_rule · suffix_liability_note | char · text | Ltda. (Art. 101) · S. en C. (Arts. 94/297 — 05-consumed) · Sociedad Cooperativa de R.L./Ilimitada (Art. 19-XII); only evidenced suffixes ship | FR-043, FR-058 |
| l10n_sv_commerce.society.type | min_capital_usd · participation_denomination_usd | monetary (dated config) | srl: 2,000 · 1+multiples (Art. 103); sa: n/a · 1+multiples (Art. 129); 2008 USD code text dated-but-current | FR-059, FR-065 |
| l10n_sv_commerce.society.type | reserve_rate · reserve_limit_kind · reserve_limit_fraction | float · select · fraction | colectiva/comandita_simple: 0.05 · legal_limit · 1/6 (Arts. 91/100); srl/sa/eirl: 0.07 · minimum_legal · 1/5 (Arts. 123/295/616); sas: config-gap | FR-055 |
| l10n_sv_commerce.society.type | reserve_investment_rule | select | half_salvadoran_realizable (Art. 92) · two_thirds_salvadoran_centralamerican (Art. 124); cooperative fondo-de-reserva exclusion flag (Art. 19-XI) | FR-056 |
| l10n_sv_commerce.society.type | votes_rule · escritura_change_quorum · auditor_required | select · fraction/enum · boolean | srl: vote_per_dollar · 3/4 (unanimity: fin-change/obligation-increase) · true (Art. 122); sa: one_per_accion (Art. 160 kin) · type-specific · true (Art. 289); cooperative: one_per_socio (Art. 19-III) | FR-043, FR-063, FR-064, FR-070 |
| res.company | sv_cml_society_type · sv_cml_capital_regime | many2one profile · select | fijo · variable (variable-regime mechanics owned by 05) | FR-042 |

**Formation records (escritura/estatutos/inscription):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.escritura | act_kind · notary_ref · granted_on | select · ref · date | constitución · modificación · transformación · fusión · liquidación (Art. 21/24) | FR-045 |
| l10n_sv_commerce.escritura | art22_checklist · nullity_outcome | computed | 12 ordinals present?; I-IX missing ⇒ nullity; X/XI/XII missing ⇒ Code-fallback (Art. 27) | FR-046 |
| l10n_sv_commerce.estatutos | deposit_entry_ref · deposit_no · copies_delivered | registry entry · char · count | junta-extraordinaria acta certification deposited; per-socio copy carries deposit number (Art. 23) | FR-047 |
| res.company | sv_cml_personality_state | computed | pre_inscription (no personality) · inscribed (perfected at inscription) · extinguished (Art. 25) | FR-048 |
| l10n_sv_commerce.registry.entry (consumed) | entry_kind = instrumento_social | — | Art. 24/465-I catalogue on SV-CML-FR-013's model; presentation anchor per SV-CML-FR-016 | FR-048 |

**Capital + aportations:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_capital_social · sv_cml_capital_variable_min | monetary | sum of promised aportaciones; variable → mínimo stated (Art. 22-VII/29) | FR-049 |
| res.company | sv_cml_assets_ge_capital | computed | patrimony goods ≥ capital guard (warning state; valuation = auditor's act) | FR-049 |
| l10n_sv_commerce.aportacion | socio_ref · kind · value_usd · warranty_flags | partner · select · monetary · flags | dinero · bienes (credit warranties + evicción/saneamiento; acciones ≤ valor contable absent Bolsa — Bolsa-exists = dated config slot) | FR-051, FR-052 |
| l10n_sv_commerce.capital.change | direction · consent_class · publication_state · opposition_window | select · enum · state · date range | aumento: 1× national-daily+D.O.; reducción: Art. 486 engine + 30-day opposition from third publication (Arts. 30/486 via SV-CML-FR-017) | FR-050 |

**Distribution + reserva legal:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.dividend.distribution | distributable_ceiling | computed | realized per-balance profit; capital loss restored first; socio-industrial alimentary exception class | FR-053 |
| l10n_sv_commerce.dividend.distribution | excess_restitution_exposure | computed flag | solidary restitution duty (administrators + recipients) on ceiling breach | FR-053 |
| l10n_sv_commerce.reserve | annual_rate · limit_kind · limit_fraction · restoration_duty | from type profile | 5%→1/6 limit · 7%→1/5 floor; recomputation trigger on any decrease (Art. 39); ISR disambiguation note = SV-TAX-FR-063/101 by id | FR-054, FR-055 |
| l10n_sv_commerce.reserve | deployment_classification | select | disponible · salvadoran_realizable_securities · centralamerican_realizable_securities · purpose_investment (Art. 92/124 constraints) | FR-056 |

**Society books + partner/share ledgers (consumes 02's book model):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.book | register_kind (society additions) | select | actas_juntas_generales · actas_juntas_directivas · registro_socios · registro_accionistas · movimientos_capital_variable (IV gated on capital-regime = variable) | FR-057 |
| l10n_sv_commerce.participation | socio_ref · count · unit_value_usd · category · copropiedad_repr | partner · int · monetary · char · partner | Art. 113 ordinals I-II; $1-multiple validator; no títulos-valor objects for SRL | FR-059, FR-062 |
| l10n_sv_commerce.participation | subscription/exhibición data · insoluta_term · guarantees | dates · monetary · refs | Art. 113-III; Art. 106 discipline (5% exhibit; 1y/5y insoluta term; Notary cheque data) | FR-060, FR-062 |
| l10n_sv_commerce.share.register.entry | accionista_ref · action numbers/series/classes | partner · ints/chars | Art. 155-I | FR-068 |
| l10n_sv_commerce.share.register.entry | entry_kind | select | llamamientos · traspasos · nominative_to_bearer · canjes · gravamenes_embargos · gravamen_cancellations · title_cancellations (Art. 155 II-VIII) | FR-068 |
| l10n_sv_commerce.share.title | art149_content_profile | computed checklist | 7 ordinals + capital-change annotations (Art. 149); exchange-per-151, never overwrite | FR-068 |
| l10n_sv_commerce.share.holding | holder_kind · own_share_exception · resale_deadline | select · select · date | society_own (only remate/adjudicación judicial; 3-month resale clock; no assembly representation) · socio (default) — loan/advance-on-own-shares blocked outright | FR-067 |

**Vigilance + juntas:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.auditor.appointment | designating_body · term_basis · incompatibility_check | select · select · computed | junta_general (Art. 289; SRL mandatory Art. 122); not admin/gerente/subalterno; no 4°-consanguinity/2°-affinity kin of admins | FR-070 |
| l10n_sv_commerce.auditor.appointment | monthly_duty_calendar | dated checkpoints | monthly comprobación balance · monthly books/caja inspection · inventory checks · annual revision (Art. 291 III-VI) | FR-070 |
| l10n_sv_commerce.junta | convocatoria_published_on · docs_available_from | date · computed | Art. 236 availability start = convocatoria publication | FR-071 |
| l10n_sv_commerce.junta | title_deposit_window · bank_designation | computed date · char | ≥8 days for pacto-subordinated title deposits (Art. 236 inciso 2) | FR-071 |

## 5. Odoo Mapping

Layer semantics for this wave: the society-type model is Odoo-native
(res.company/res.partner families) — every FR maps `odoo`; none of them
touch DTE generation/transformation (the only architecture-split surface
per `shared/docs/saas-thin-client-architecture.md` D2), so no `saas`
rows are introduced. E-invoicing kin (pointer only): company-type
suffixes and the razón social/denominación maintained here flow into DTE
emitter-name data owned by the e-invoicing wave's onboarding/
authorization cluster (A11) — consumed there by id, never re-derived
here. Model names are stable across Odoo 17/18/19/20; no
version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-042 | odoo | res.company + l10n_sv_commerce.society.type | sv_cml_society_type, class/regime | Extensible profile table (Art. 18 closed-form rule as DATA, not enum); type profiles drive suffix/capital/reserve/vote rules |
| FR-043 | odoo | l10n_sv_commerce.society.type (cooperativa row) | Art. 19 flags | 10-socio min; one-vote-per-socio override; nominative-only + inscription-transfer; ¢5,000 cap = colones remnant (value flagged, OQ-002); tax-subject (D.L. 385-1989 derogation note) |
| FR-044 | odoo | l10n_sv_commerce.society.type (sas row) | statute_status=statute_pending | Existence = LB-032 (creaempresa CNR); NO mechanics invented — all profile fields render config-gap with OQ-001 pointer |
| FR-045 | odoo | l10n_sv_commerce.escritura | act_kind, notary_ref | Art. 21 family; deed = formality anchor of every lifecycle act (05 consumes by id) |
| FR-046 | odoo | l10n_sv_commerce.escritura | art22_checklist, nullity_outcome | 12-ordinal completeness; Art. 27 nullity (I-IX) vs Code-fallback (X-XII) computed per field |
| FR-047 | odoo | l10n_sv_commerce.estatutos + l10n_sv_commerce.registry.entry | deposit_entry_ref, deposit_no, copies | Contradiction check = warning (legal review external); deposit via instrumento_social entry (SV-CML-FR-013) |
| FR-048 | odoo | res.company + l10n_sv_commerce.registry.entry | sv_cml_personality_state | Perfected/extinguished ONLY at inscription (Art. 25); catalogue Art. 24/465-I; opens matrícula per SV-CML-FR-008; presentation anchor SV-CML-FR-016 |
| FR-049 | odoo | res.company (account.account capital) | sv_cml_capital_social, assets_ge_capital check | Pasivo-side presentation = Odoo equity/capital accounts credit side; assets≥capital = computed warning (valuation = auditor's) |
| FR-050 | odoo | l10n_sv_commerce.capital.change + l10n_sv_commerce.publication (consumed) | direction, publication, opposition_window | Aumento 1× daily+D.O.; reducción per Art. 486 (SV-CML-FR-017 engine by id) + 30-day opposition from 3rd publication; variable-regime mechanics = 05's |
| FR-051 | odoo | l10n_sv_commerce.aportacion | kind, value_usd, warranty_flags | Work aportation blocked for capitales/SRL; moneda nacional = colones remnant read USD; mora → external ejecutivo enforcement (exposure only) |
| FR-052 | odoo | l10n_sv_commerce.aportacion | credit warranties, book-value cap | Acciones aportadas ≤ valor contable (no-Bolsa precondition = dated config slot, no shipped value); no-waiver (pact contra prohibited) |
| FR-053 | odoo | l10n_sv_commerce.dividend.distribution | distributable_ceiling | Realized per-balance profit ceiling (03's cycle by id); capital-loss-restored-first gate; socio-industrial alimentary exception class |
| FR-054 | odoo | l10n_sv_commerce.reserve | restoration_duty trigger | Art. 39 chassis: annual separation + restore-on-diminution; non-waivable; administrator solidarity = exposure |
| FR-055 | odoo | l10n_sv_commerce.society.type → reserve | rate/limit per profile | 5%→1/6 limit (91/100) vs 7%→1/5 floor (123/295/616); cooperative Art. 19-XI flag; sas config-gap; ISR disambiguation SV-TAX-FR-063/101 by id |
| FR-056 | odoo | l10n_sv_commerce.reserve | deployment_classification | Art. 92 half / Art. 124 two-thirds realizable-securities constraints (metadata; realizability = auditor judgment) |
| FR-057 | odoo | l10n_sv_commerce.book | society register kinds | Art. 40 four-book set; capital-variable book gated on regime; Art. 440 discipline via SV-CML-FR-025 + retention row a via SV-CML-FR-028 (by id) |
| FR-058 | odoo | res.company + l10n_sv_commerce.society.type (srl) | suffix_rule validator | "Limitada"/"Ltda." immediate-suffix check; omission ⇒ unlimited-solidary exposure note (Art. 101) |
| FR-059 | odoo | res.company + l10n_sv_commerce.participation | min_capital, denomination validator | $2,000 floor + $1-multiple participaciones (dated config, §2); no títulos-valor objects; no aporte industrial |
| FR-060 | odoo | l10n_sv_commerce.participation | subscription/exhibición fields | 100% subscribed; ≥5% exhibit; 1y/5y ($100k trigger) insoluta term; Notary + SSF-bank cheque data recorded |
| FR-061 | odoo | l10n_sv_commerce.capital.change (increase) | preference window | 15-day window from assembly/certified-letter notice (Art. 112); lapse = renuncia; preference unwaivable |
| FR-062 | odoo | l10n_sv_commerce.book (registro_socios) + participation | Art. 113 7 fields | Administrator custody + certifications; missing book ⇒ irregular flag (Art. 354 exposure; machinery in 05) |
| FR-063 | odoo | l10n_sv_commerce.junta | quorum/vote computation | Half-capital install quorum (2nd call any); voto-por-dólar; 3/4 escritura-change; unanimity fin-change/obligation-increase |
| FR-064 | odoo | l10n_sv_commerce.auditor.appointment | mandatory appointment | SRL auditor in every case (Art. 122); S.A. incompatibilities incorporated via Art. 125 → FR-070 by id |
| FR-065 | odoo | l10n_sv_commerce.share (S.A.) | nominal/issue validators | $1+ whole multiples; issue ≥ nominal; real-aportation pairing with FR-049 guard |
| FR-066 | odoo | l10n_sv_commerce.share | nominative invariant | Nominative-until-paid; bearer conversion gated (payment + escritura); provisional titles ≤1y + exchange clock |
| FR-067 | odoo | l10n_sv_commerce.share.holding + account.payment guard | own-share blocks | Self-acquisition blocked except remate/adjudicación judicial; 3-month resale clock; no assembly representation; loans/advances on own acciones blocked outright |
| FR-068 | odoo | l10n_sv_commerce.share.register.entry + share.title | Art. 155 ledger (8 kinds) | Ledger = register of record; Art. 149 title profile + capital-change annotations exchanged per Art. 151 (no-alteration kin SV-CML-FR-024 by id) |
| FR-069 | odoo | l10n_sv_commerce.capital.change (increase) + publication | 15-day preference window | Anchored to agreement PUBLICATION (Art. 157); publication engine = SV-CML-FR-017 by id |
| FR-070 | odoo | l10n_sv_commerce.auditor.appointment | designation/incompatibilities/duty calendar | Junta-designated external auditor; 4°/2° incompatibility check (warning); monthly comprobación-balance + books/caja checkpoints; annual cycle = 03 by id; SRL/EIRL incorporation (125/616-IV) |
| FR-071 | odoo | l10n_sv_commerce.junta | availability start + deposit window | Art. 236: docs available from convocatoria publication; ≥8-day title-deposit window; any-bank default |

Version-regime notes (D12): the dated values in this file — US$2,000
SRL minimum, US$1 participación/acción denominations, US$100,000
extension trigger (Arts. 103/106/129) — are 2008-reform (18)(29) USD
code text, dated-but-current under the SOQ-22 residual watch, stored as
dated configuration (§2). The ¢5,000 cooperative action cap (Art. 19-II)
is a COLONES remnant (SOQ-29/OQ-7 kin): historical text, operative
reading USD, every value-level use flagged (OQ-002); Art. 31's "moneda
nacional" rides the same discipline. The SAS statute-pending flag is a
version-regime slot by design: when the SAS law lands (SOQ-23), its
profile row populates without schema change (acquisition numbering ≥74).
No renewal-epoch, fee or rate instrument lives in this file.

## 6. Acceptance Criteria

- **AC-001:** Given an SRL constituted with capital US$2,000 divided
  into 2,000 participaciones of US$1 (and another of US$500 each), when
  the FR-059 validators run, then both pass the floor and the
  $1-multiple denomination checks; given capital US$1,999 or a
  participación of US$0.50, then each is rejected with the Art. 103
  reason (FR-059).
- **AC-002:** Given an S.A. recording (i) a purchase of its own acciones
  outside the remate/adjudicación-judicial classes and (ii) a loan
  secured on its own acciones, when the FR-067 guards run, then (i) is
  blocked with the Art. 141 exception catalogue shown and (ii) is
  blocked outright with the Art. 142 no-exception reason; given
  acciones acquired by judicial adjudication, then a 3-month resale
  deadline is computed and the shares are excluded from assembly
  representation while held (FR-067).
- **AC-003:** Given an SRL with utilidades netas US$100,000, reserve
  balance below 1/5 of capital, when distribution is attempted before
  the separation posts, then it is blocked; when the reserve separation
  runs, then US$7,000 (7%) is separated and the distribution becomes
  eligible up to the realized-per-balance ceiling; given a later
  reserve decrease, then the restoration duty recomputes the 7%
  separation (FR-053, FR-054, FR-055).
- **AC-004:** Given the company-type selection, when `sas` is chosen,
  then the record saves with statute_status = statute_pending, the
  OQ-001 pointer surfaces, and NO suffix/capital/quorum/reserve
  mechanics render — every profile field shows as a config-gap
  (FR-044).
- **AC-005:** Given a sociedad whose escritura de constitución is
  granted but not yet inscribed, when its state is evaluated, then the
  record carries the pre-inscription no-personality marker and no
  personality-dependent state; upon recording the inscription
  (instrumento_social entry, presentation timestamp stamped), then
  personality is marked perfected and the matrícula obligation opens
  immediately (SV-CML-FR-008 by id) (FR-048).
- **AC-006:** Given a constitutive deed missing ordinal VII (capital)
  and another missing ordinal XI (reserves), when the Art. 27 rule
  applies, then the first is marked NULL and the second falls back to
  the Code's reserve provisions (Code-default fallback flag)
  (FR-046).
- **AC-007:** Given a cooperative sociedad record, when the profile
  applies, then the 10-socio minimum is enforced, voting computes one
  vote per socio regardless of actions, the per-action cap renders as
  the colones-remnant historical text with the USD-operative flag
  (SOQ-29), and the "Sociedad Cooperativa de Responsabilidad
  Limitada/Ilimitada" suffix rule is enforced with NO tax-exemption
  logic (D.L. 385-1989 derogation note) (FR-043).
- **AC-008:** Given a sociedad whose recorded patrimony goods fall
  below the capital social, when the FR-049 guard runs, then the
  assets-≥-capital warning state surfaces with the Art. 29 reason
  (valuation itself remains the auditor's act) (FR-049).
- **AC-009:** Given an aportation of capital-society acciones valued
  above their valor contable with no Bolsa configured, when the FR-052
  check runs, then the valuation is blocked with the Art. 32 reason;
  given a credit aportation, then the existence/legitimacy/solvency
  warranty flags attach to the aportation record (FR-052).
- **AC-010:** Given an SRL without a Registro de Socios book, when
  compliance is evaluated, then the sociedad is flagged irregular with
  the Art. 354 sanction exposure (FR-062).
- **AC-011:** Given an SRL escritura-modification junta with 80% of
  capital voting in favour, when the FR-063 quorum engine runs, then
  the resolution passes (≥3/4); given a fin-change junta at 90%, then
  it fails (unanimity required); given a first-call junta at 40% of
  capital, then installation fails and a second call is scheduled
  after two days valid at any attendance (FR-063).
- **AC-012:** Given an S.A. capital-increase agreement published on
  01-Mar, when the FR-069 window computes, then the proportional
  preferential-subscription window closes 16-Mar (publication + 15
  days); given an SRL increase approved in assembly with certified
  letters sent, then the window anchors to assembly/notification per
  Art. 112 (FR-061, FR-069).
- **AC-013:** Given an S.A. auditor appointed, when the vigilance
  record is built, then the monthly checkpoints (comprobación balance
  demand, books/papers/caja inspection), the inventory checks and the
  annual revision linkage to the 03 cycle are scheduled, and an
  appointment of an administrator's 2nd-degree-affinity relative
  surfaces the Art. 290 incompatibility warning (FR-070).
- **AC-014:** Given a colectiva with reserve already at 1/6 of
  capital, when the annual separation computes, then NO further 5%
  separation is required (legal limit reached); given an SRL at 1/5 of
  capital, then the 7% separation likewise stops (minimum floor
  satisfied) — the limit-vs-floor semantics differ per family
  (FR-055).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-23 carried: the SAS statute (Sociedad por Acciones Simplificada) is NOT in the corpus — existence is confirmed via the official CNR creaempresa portal (LB-032) but the law's number/date is unpinned (asamblea.gob.sv + D.O. down; law-firm mirrors NOT official). FR-044 ships `sas` as statute_pending with NO mechanics; suffix, capital, reserve, quorum and ledger profiles for SAS remain config-gaps until the law is acquired and read (acquisition candidate, sources-registry numbering ≥74). | no | Takumi S5 (sources watch) | open |
| OQ-002 | SOQ-29/OQ-7 kin: the Art. 19-II cooperative per-action cap "¢5,000.00" is colones-era code text — historical value, operative reading USD (dollarization). Working reading: record the cap as historical text with the USD-operative flag at every value-level use (FR-043); the operative per-action ceiling in practice rides the dollarized acción-denomination discipline. Additionally, whether a special cooperatives statute (outside corpus) supersedes or complements the Art. 19 regime is unverified — watch when a cooperatives law surfaces. | no | Takumi S5 | open |
