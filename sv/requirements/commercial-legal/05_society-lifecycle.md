# SV — Commercial-legal — Society lifecycle: capital variable, fusión, transformación, liquidación, nullity/irregularity and foreign societies (C5)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador sociedad (company/society) LIFECYCLE
regime of the Código de Comercio (Commercial Code, CC) after
constitution: the capital-VARIABLE regime of Arts. 306-314 — adoption by
any class, the "de C.V." naming duty, escritura conditions, minimum
capital floors and the announcement prohibition, the movement book
consultable by any interested person, and withdrawal notices effective
at fiscal-year end; the fusión (merger) regime of Arts. 315-321 —
universal succession, the per-society agreement/inscription/marginal
note/publication pipeline, the 90-day opposition window, the dissident
socio's retiro, and the Ley de Competencia inscription checkpoint with
personality retained until inscription; the transformación
(transformation) regime of Arts. 322-325 — any-type-to-any-type freedom,
unlimited-liability survival for pre-change operations, the auditor
valúo for personas→capital, and successor continuity without solution
of continuity; the liquidación (liquidation) regime of Arts. 326-342-A —
the "en liquidación" name suffix, the two-year cap with prorrogable
terms, liquidator appointment/transition and faculties (fiscal
obligations express), partial and final distributions, the closing
escritura and inscription, the post-liquidation TEN-YEAR bank/designee
deposit of corporate books and papers (which feeds the canonical
retention matrix by id), and the revocación de disolución; the
nullity/irregularity regime of Arts. 343-357 — illicit object/causa
nullity, the 90-120-day regularization windows, the
exteriorized-society unlimited liability, the 15-day escritura
presentation duty and 4-month registro check, the out-of-object reform
window, and the single-socio three-month collapse into an empresa
individual; and the extranjeras (foreign society) registration package
of Arts. 358-361, including the MINEC-first ordering of capital-change
inscriptions. This file also carries the SOQ-24 quiebra scope note
(Arts. 498-552 — terminology only, no FRs).

It owns, by binding forward pointer from `04_society-types.md`: the
capital-VARIABLE movement mechanics of Arts. 306-314 (FR-050/FR-057
defer them here), the Art. 354 irregularity machinery behind FR-062's
irregularity flag, and the "en liquidación" name-suffix kin (the "S. en
C." comandita suffix rules of Arts. 94/297 ship in 04's society.type
profile row and are CONSUMED here by id, never restated).

It does **not** cover: merchant status, matrícula, cancellation states
and the registry/publication architecture
(`01_merchant-registration.md` — consumed by id: FR-012 cancellation
cases d/f/g, FR-013 registry-entry model, FR-014 liquidator-credenciales
kind, FR-016 presentation anchor, FR-017 Art. 486 publication engine);
book discipline, register legalization and the retention matrix
(`02_accounting-books.md` — the matrix is SV-CML-FR-028, consumed by id
and never restated; SV-CML-FR-029 consumes this file's liquidation
lifecycle event by pointer); the annual statement cycle and balance
deposit (`03_financial-statements.md` — FR-035's deposit mechanics
consumed by id); society-type profiles, formation, FIXED-capital
changes, reserves and the SRL/S.A. ledgers (`04_society-types.md` —
FR-042 type/regime fields, FR-048 personality-by-inscription, FR-050
Art. 30 fixed-regime changes, FR-057 the Art. 40-IV book gate,
FR-058/FR-062 suffix and Registro-de-Socios kin); commercial agents
(`06_commercial-agents.md`); the empresa mercantil transfer package and
the EIRL vehicle itself (`07_empresa-mercantil-eirl.md` when it lands —
this file records only the Art. 620 liquidation touchpoint with the CT
solvencia pointer); payment instruments (`08_payment-instruments.md`);
sales contracts (`09_sales-contracts.md`); AML compliance
(`10_aml-compliance.md`); and ISR mechanics (taxation wave by id).
E-invoicing kin: the lifecycle name suffixes ("de C.V.", "en
liquidación") flow into DTE emitter-name data owned by the e-invoicing
wave's onboarding/authorization cluster (A11; A8 kin) — pointer note
only, never re-derived here.

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
Asamblea-editorial artifacts without a stated as-of date — rides every
07_ LB in this file. Verbatim text below is copied from the 07_ evidence
file (EVID-221/222/224) and — the evidence glosses summarize this
article range — from the extraction txt
`sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable per standing
ruling; page pointers = txt PAGE markers; reform tick marks
"(18)(24)(29)" stripped from quotations, provenance noted here).

Binding forward pointers honored (from `04_society-types.md` §2/§3):
(i) this file owns the Arts. 306-314 capital-VARIABLE movement mechanics
deferred by SV-CML-FR-050 and the Art. 40-IV book movement mechanics
gated by SV-CML-FR-057 (book existence gate consumed by id; movement
rows live here); (ii) this file owns the Art. 354 irregularity machinery
behind SV-CML-FR-062's irregularity flag (flag consumed by id); (iii)
suffix enforcement consumes 04's society.type `suffix_rule` profile row
by id — including the comandita "S. en C." (Arts. 94/297) — this file
adds only the lifecycle suffixes ("de C.V.", Art. 308; "en liquidación",
Arts. 326/620).

Kin pointers (by id, no re-derivation): the retention matrix is
SV-CML-FR-028 (`02_accounting-books.md`) — the Art. 340-3 ten-year
deposit of corporate papers FEEDS its row a and is never restated here;
SV-CML-FR-029 consumes the liquidation lifecycle event this file emits
(the row-a post-liquidation extension trigger). DTE emitter-name suffix
propagation is the e-invoicing onboarding/authorization cluster (A11;
A8 kin) — pointer only. The EIRL voluntary-liquidation CT-solvency
verification (Art. 620 → Código Tributario) is an EXTERNAL gate: the CT
corpus extraction evidences no solvencia article (OQ-003), and the EIRL
profile is `07_empresa-mercantil-eirl.md` territory (this file records
only the touchpoint). Quiebra (Arts. 498-552) is terminology-only under
SOQ-24 (§3.7).

Currency discipline (SOQ-29): no colones-denominated value occurs in
this article set; the 1/5-of-initial-capital minimum (Art. 310, personas
societies) and every other fraction/period here is currency-neutral code
text under the SOQ-22 residual watch.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 306: "Cualquier clase de sociedad podrá adoptar el régimen de sociedad de capital variable. Cuando se adopte este régimen el capital social será susceptible, tanto de aumento por aportaciones posteriores o por la admisión de nuevos socios, como de disminución por retiro parcial o total de algunas aportaciones, sin más formalidades que las establecidas en este capítulo. También podrá comprenderse, dentro del régimen adoptado en esta capítulo, el aumento de capital por capitalización de reservas y utilidades o por revalidación del activo; o la disminución del mismo capital por desvalorización del activo." Art. 307: "Las sociedades de capital variable se regirán por las disposiciones que correspondan a la especie de sociedad de que se trate; y por las de la sociedad anónima relativas a balances, responsabilidad de los administradores y vigilancia del auditor, salvo las modificaciones que se establecen en el presente capítulo." | ANY class of sociedad may adopt the capital-variable regime. Under it the social capital is susceptible of increase by later aportations or admission of new socios, and of decrease by partial or total withdrawal of some aportations, with no further formalities than those set in this chapter. The regime may also comprise capital increase by capitalization of reserves and profits or by revalidation of assets; or capital decrease by asset devaluation. Capital-variable societies are governed by the rules of their species PLUS the S.A. rules on balances, administrator liability and auditor vigilance, save this chapter's modifications | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 306-307 p.57 (EVID-221; txt PAGE 57) |
| LB-002 | Código de Comercio, Art. 308: "Deberán añadirse siempre a la razón social o denominación propia del tipo de sociedad de que se trate, las palabras 'de capital variable' o su abreviatura 'de C.V.'" Art. 309: "La escritura social de toda sociedad de capital variable debe contener, además de las estipulaciones que correspondan a la naturaleza de la sociedad, las condiciones que se fijen para el aumento y la disminución del capital social. En las sociedades por acciones, el pacto social y, en su defecto, la junta general extraordinaria, fijará los aumentos del capital, lo mismo que la forma y término en que deba hacerse la correspondiente emisión de acciones, en cada caso." | There must ALWAYS be added to the razón social or denominación proper to the society's type the words "de capital variable" or the abbreviation "de C.V.". The escritura of every capital-variable sociedad must contain, besides the stipulations of its nature, the conditions fixed for capital increase and decrease. In share societies the pacto social — or failing it the extraordinary general meeting — fixes the increases, and the form and term of the corresponding share emission in each case | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 308-309 p.57 (EVID-221; txt PAGE 57) |
| LB-003 | Código de Comercio, Art. 310: "En la sociedad anónima, en la de responsabilidad limitada y en la comandita por acciones, se indicará un capital mínimo que no podrá ser inferior al que se fija en los artículos correspondientes. En las sociedades en nombre colectivo y en comandita simple, el capital mínimo no podrá ser inferior a la quinta parte del capital inicial. Queda prohibido a las sociedades anunciar el capital cuyo aumento esté autorizado, o simplemente el capital social, sin anunciar al mismo tiempo el capital mínimo. Los administradores o cualquier otro funcionario de la sociedad que contravengan este precepto, serán responsables ilimitada y solidariamente por los daños y perjuicios que se causen." Art. 311: "En las sociedades de capital variable por acciones, éstas serán siempre nominativas." | In the S.A., SRL and comandita por acciones a MINIMUM capital is indicated, not inferior to that fixed in the corresponding articles (the type's statutory floor — profile-driven, no value invented here); in the colectiva and comandita simple the minimum capital may not be inferior to ONE-FIFTH of the initial capital. Societies are PROHIBITED from announcing the capital whose increase is authorized, or simply the social capital, without at the same time announcing the minimum capital; administrators or any other society officer contravening are unlimitedly and solidarily liable for the damages caused. In capital-variable share societies the acciones are ALWAYS nominative | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 310-311 p.57 (EVID-221; txt PAGE 57) |
| LB-004 | Código de Comercio, Art. 312: "Todo aumento o disminución del capital social deberá inscribirse en un libro de registro que al efecto llevará la sociedad, el cual podrá ser consultado por cualquier persona que tenga interés en ello." Art. 313: "El retiro parcial o total de aportaciones de socio deberá notificarse a la sociedad y no surtirá efecto hasta el fin del ejercicio anual en curso, si la notificación se hace antes del último trimestre de dicho ejercicio; y hasta el fin del ejercicio siguiente, si se hiciere después. Esta notificación deberá ser judicial o por acta notarial." Art. 314: "Los socios no podrán ejercitar el derecho de separación cuando tenga como consecuencia reducir a menos del mínimo el capital social." | Every capital increase or decrease must be entered in a registry book the society keeps for the purpose, CONSULTABLE BY ANY PERSON HAVING AN INTEREST in it. Partial or total withdrawal of a socio's aportations must be notified to the society and takes NO effect until the end of the current fiscal year if notified BEFORE the last trimester of that year — and until the end of the FOLLOWING fiscal year if notified after (working reading per evidence gloss: a notice within the last trimester runs to the following year-end). The notification must be judicial or by notarial acta. Socios may NOT exercise the right of separation when it would reduce the social capital below the minimum | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 312-314 pp.57-58 (EVID-221; txt PAGE 57-58) |
| LB-005 | Código de Comercio, Art. 315: "Hay fusión cuando dos o más sociedades integran una nueva, o cuando una ya existente absorbe a otra u otras. La nueva sociedad o la incorporante adquiere los derechos y contrae todas las obligaciones de las sociedades fusionadas o incorporadas." Art. 316: "Cuando de la fusión de varias sociedades haya de resultar una distinta, su constitución se sujetará a los principios que rijan la constitución de la sociedad a cuyo género haya de pertenecer. Si la fusión es por absorción deberá modificarse la escritura de la sociedad incorporante." Art. 321: "Los socios de las sociedades fusionadas que vengan a ser socios de la sociedad nueva o de la absorbente, recibirán participaciones sociales o acciones en la proporción equivalente a las que anteriormente tenían, salvo convenio." | There is fusión (merger) when two or more societies integrate a new one, or when an existing one absorbs another or others. The new or absorbing society ACQUIRES THE RIGHTS and contracts ALL the obligations of the merged/incorporated societies (universal succession). When a distinct society is to result, its constitution follows the principles governing constitution of the género it belongs to; if the fusión is by absorption, the absorbing society's escritura must be modified. Socios of the merged societies becoming socios of the new or absorbing one receive participaciones or acciones in the proportion equivalent to those previously held, unless otherwise agreed | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 315-316 p.58; Art. 321 p.59 (EVID-221; txt PAGE 58-59) |
| LB-006 | Código de Comercio, Art. 317: "El acuerdo de fusión deberá ser tomado por cada sociedad en la forma que corresponda resolver la modificación de su pacto social y debe inscribirse en el Registro de Comercio del domicilio de cada una de las sociedades fusionadas, debiendo anotarse marginalmente en las inscripciones de las escrituras sociales de tales sociedades. Hecho el registro, deberá publicarse dicho acuerdo y el último balance de las sociedades." | The merger agreement must be taken by EACH society in the form corresponding to resolving the modification of its pacto social, and must be REGISTERED in the Commerce Registry of the DOMICILE of each of the merging societies, with a MARGINAL NOTE on the inscriptions of their social deeds. Once registered, the agreement AND the societies' LAST BALANCE must be published (publication form not fixed by this article — Art. 486 default engine applies, SV-CML-FR-017 by id) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 317 p.58 (EVID-221; txt PAGE 58) |
| LB-007 | Código de Comercio, Art. 318: "La fusión se ejecutará después de los noventa días de las referidas publicaciones, siempre que no hubiese oposición. Dentro de dicho plazo, todo interesado puede oponerse a la fusión, que se suspenderá, en tanto no sea garantizado su interés suficientemente, conforme al criterio del Juez que conozca de la demanda; pero no será necesaria la garantía si la nueva sociedad o la incorporante la ofrecen en sí mismas, de manera notoria. Si la sentencia declara que la oposición es infundada, la fusión podrá efectuarse tan pronto como aquélla cause ejecutoria." Art. 320: "El socio que no esté de acuerdo en la fusión puede retirarse; pero su participación social y su responsabilidad personal ilimitada, si se trata de socio colectivo o comanditado, continuarán garantizando el cumplimiento de las obligaciones contraídas antes de tomarse el acuerdo de fusión. El derecho al retiro del socio consignado en este artículo, deberá ser ejercitado dentro del plazo de noventa días señalado en el artículo 318." | The fusión is executed AFTER NINETY DAYS from the referred publications, provided no opposition. Within that term ANY interested person may oppose; the fusión is suspended until his interest is sufficiently guaranteed per the criterion of the Judge hearing the demand — no guarantee needed if the new or absorbing society offers it in themselves notoriously. If the sentence declares the opposition unfounded, the fusión may proceed as soon as it becomes final. A socio disagreeing with the fusión may WITHDRAW; but his participación and his unlimited personal liability (colectivo or comanditado socio) continue guaranteeing obligations contracted BEFORE the merger agreement; the retiro right must be exercised within Art. 318's ninety days | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 318, 320 pp.58-59 (EVID-221; txt PAGE 58-59) |
| LB-008 | Código de Comercio, Art. 319: "Los representantes de las sociedades fusionadas redactarán el nuevo pacto social o las modificaciones necesarias en el de la sociedad absorbente; el nuevo pacto o las modificaciones deberán ser aprobados por las sociedades, con los mismos requisitos exigidos para el acuerdo de fusión. La ejecución de la fusión corresponderá a quienes especialmente sean designados y, en defecto de designación, a los administradores de las sociedades que van a fusionarse. La fusión se hará constar en escritura matriz y el testimonio de la misma se inscribirá en el Registro de Comercio y surtirá efectos a partir de la fecha de su inscripción. Para efectos de inscripción, el Registrador deberá comprobar, según el caso: a) Que no se trata de una fusión sujeta a notificación, según la Ley de Competencia; b) Que cuenta con la aprobación de la Superintendencia de Competencia; c) Que se ha realizado la notificación de Ley a la Superintendencia de Competencia, sin que ésta hubiese emitido resolución alguna en el plazo estipulado en la Ley de Competencia. En consecuencia, mientras la inscripción no se verifique, las sociedades fusionantes conservarán su personería jurídica, como si la misma no se hubiese llevado a cabo. Hecha la inscripción, la personería jurídica de las sociedades fusionadas o incorporadas quedará extinguida." | The representatives of the merging societies draft the new pacto social (or the necessary modifications of the absorbing society's); approved by the societies with the SAME requisites as the merger agreement. Execution falls to specially designated persons or, failing designation, the administrators. The fusión is recorded in an escritura matriz whose testimonio is REGISTERED in the Commerce Registry, taking effect FROM ITS INSCRIPTION DATE. For inscription the Registrar must verify, per the case: a) it is NOT a fusión subject to notification under the Ley de Competencia; b) it HAS the approval of the Superintendencia de Competencia; c) legal notification was made to the Superintendencia without resolution within that law's term. Consequently, until the inscription the merging societies RETAIN their legal personality as if the fusión had not occurred; upon inscription the personality of the merged/incorporated societies is EXTINGUISHED | `sv/sources/07_Codigo_Comercio.pdf` | Art. 319 pp.58-59 (EVID-221; txt PAGE 58-59) |
| LB-009 | Código de Comercio, Art. 322: "Toda sociedad de cualquier tipo que sea podrá adoptar otro tipo legal, así como las de capital fijo podrán transformarse en sociedades de capital variable, y viceversa, siempre que se cumpla con los requisitos establecidos en este capítulo." Art. 323 (incisos 1-2): "El acuerdo de transformación deberá tomarse por la sociedad con los mismos requisitos que cualquier modificación al pacto social. Si la transformación implica la conversión de la responsabilidad ilimitada de uno o varios de los socios, a responsabilidad limitada, éstos continuarán respondiendo ilimitadamente por todas las operaciones realizadas antes de la validez del acuerdo de transformación." | ANY sociedad of any type may adopt another legal type, and capital-fijo societies may transform into capital-variable and vice versa, on this chapter's requisites. The transformation agreement is taken with the SAME requisites as any pacto-social modification. Where the transformación converts one or more socios' UNLIMITED liability into limited liability, those socios CONTINUE RESPONDING UNLIMITEDLY for all operations realized before the transformation agreement's validity | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 322-323 p.59 (EVID-221; txt PAGE 59) |
| LB-010 | Código de Comercio, Art. 323 (incisos 3-4): "Para la transformación de una sociedad de personas a una sociedad de capital previamente deberá efectuarse un valúo por el auditor autorizado, emitiendo certificación del mismo, debiendo enviar dicha certificación dentro de los tres días hábiles siguientes de efectuado a la oficina que ejerza la vigilancia del Estado. Igual requisito deberá cumplirse para la ejecución del acuerdo de fusión de sociedades de esas naturalezas. Dicho valúo se hará constar en la escritura social." Art. 324: "La ejecución del acuerdo de transformación se hará por escritura pública, la cual deberá contener todos los requisitos exigidos para la nueva forma de sociedad que se adopte y se otorgará por las personas designadas para hacerlo, o a falta de designación, por los administradores de la sociedad que se transforme. La escritura de transformación se inscribirá en el Registro de Comercio y surtirá efectos a partir de la fecha de su inscripción. Mientras la inscripción no se verifique, la sociedad transformada continuará rigiéndose por las normas que le eran aplicables antes del acuerdo de transformación." Art. 325: "La nueva sociedad sucederá de pleno derecho a la anterior, en sus derechos y obligaciones, considerándose que no ha habido solución de continuidad entre ambas." | For a personas→capitales transformación a VALUATION (valúo) by the authorized auditor must FIRST be made and certified, the certification sent within THREE HÁBILES DAYS of its making to the state-vigilance office; the SAME requisite applies to executing a merger agreement between societies of those natures; the valúo is recorded in the social deed. Execution is by escritura pública containing ALL requisites of the adopted new form, granted by designated persons or, absent designation, the administrators; the transformation deed is registered and takes effect from its INSCRIPTION date; until inscription the transformed society continues governed by the norms previously applicable. The new society SUCCEEDS DE PLENO DERECHO (as of right) to the former in rights and obligations — no solution of continuity between them | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 323-325 pp.59-60 (EVID-221; txt PAGE 59-60) |
| LB-011 | Código de Comercio, Art. 326: "Disuelta la sociedad, se pondrá en liquidación; pero conservará su personalidad jurídica para los efectos de ésta. A su razón social o denominación se agregará la frase: 'en liquidación'. A quien corresponda el nombramiento de liquidadores, tendrá competencia también para fijar el plazo en que deba de practicarse la liquidación, el cual no podrá exceder de dos años. Cuando el plazo de la liquidación haya sido acordado por un periodo menor a los dos años, podrá prorrogarse hasta cumplir el plazo máximo antes señalado. Corresponderá a la junta general acordar las prórrogas respectivas. Dichos acuerdos deberán inscribirse en el Registro de Comercio." | A dissolved society enters liquidation but RETAINS its legal personality for the liquidation's effects. The phrase "en liquidación" is ADDED to its razón social or denominación. Whoever is competent to appoint the liquidators also fixes the liquidation term, which may NOT exceed TWO YEARS. A shorter agreed term may be PRORROGATED up to that maximum; prórrogas are agreed by the junta general and INSCRIBED in the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 326 p.60 (EVID-221; txt PAGE 60) |
| LB-012 | Código de Comercio, Art. 327: "La liquidación estará a cargo de uno o más liquidadores, quienes serán administradores y representantes de la sociedad, y responderán personalmente por los actos que ejecuten cuando se excedan de los límites de su cargo." Art. 328: "A falta de disposición del pacto social, el nombramiento de liquidadores se hará por acuerdo de los socios y en el mismo acto en que se acuerde o reconozca la disolución. Si por cualquier motivo el nombramiento de los liquidadores no se hiciere en los términos que fija el inciso anterior, lo hará la autoridad judicial, a petición de cualquier socio o de la Fiscalía General de la República. En los casos en que la sociedad se disuelva en virtud de sentencia, la designación de los liquidadores la hará el juez dentro de los quince días siguientes a aquel en que la sentencia quede firme y en el acto de la juramentación de los liquidadores deberá observar lo dispuesto en el Art. 189 de este Código." Art. 329: "Mientras no haya sido inscrito en el Registro de Comercio el nombramiento de los liquidadores y éstos no hayan entrado en funciones, los administradores continuarán en el desempeño de su cargo, sin perjuicio de la responsabilidad de unos o de otros, si la inscripción no se practicare por dolo o negligencia." | The liquidation is in charge of one or more LIQUIDATORS, who are administrators and representatives of the society and answer PERSONALLY for acts exceeding their charge's limits. Absent pacto-social provision, liquidators are appointed by socios' agreement IN THE SAME ACT as the dissolution is agreed or recognized; failing that, the judicial authority appoints at the request of any socio or the FGR. On dissolution by sentence, the judge designates within FIFTEEN DAYS of the sentence becoming firm (observing Art. 189 at the liquidators' swearing-in). Until the appointment is REGISTERED and the liquidators enter function, the ADMINISTRATORS continue in office — responsibility of either subsisting if inscription fails by dolo or negligence | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 327-329 p.60 (EVID-221; txt PAGE 60) |
| LB-013 | Código de Comercio, Art. 330: "La liquidación se practicará con arreglo a las normas fijadas en el pacto social y, en su defecto, de conformidad con los acuerdos de los socios tomados por las mayorías necesarias para modificar dicho pacto y con las disposiciones de este capítulo." Art. 331: "Nombrados los liquidadores, los administradores les entregarán todos los bienes, libros y documentos de la sociedad. Dicha entrega se hará constar en un inventario detallado que será suscrito por ambas partes." | The liquidation is practiced per the pacto social's norms or, failing them, per socios' agreements taken by the majorities needed to modify the pacto, plus this chapter's provisions. Once liquidators are appointed, the administrators deliver ALL goods, books and documents of the society; the delivery is recorded in a DETAILED INVENTORY subscribed by both parties | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 330-331 p.60 (EVID-221; txt PAGE 60) |
| LB-014 | Código de Comercio, Art. 332: "Los liquidadores tendrán las siguientes facultades: I.- Concluir las operaciones sociales que hubieren quedado pendientes al tiempo de la disolución. II.- Cobrar lo que se debe a la sociedad y pagar lo que ella deba, tomando en cuenta las obligaciones fiscales y las derivadas del cumplimiento de sus obligaciones de comerciante. III.- Vender los bienes de la sociedad. IV.- Practicar el balance final de la liquidación, que deberá someterse a la discusión y aprobación de los socios, en la forma que corresponda según la naturaleza de la sociedad. V.- Depositar en el Registro de Comercio el balance final, una vez aprobado por la junta general de accionistas. Dicho balance se publicará en el Órgano Oficial del Registro de Comercio para efectos de publicidad material. VI.- Liquidar a cada socio su participación en el haber social. VII.- Otorgar la escritura de liquidación y obtener su inscripción en el Registro de Comercio. Queda terminantemente prohibido a los liquidadores, iniciar operaciones sociales nuevas." | Liquidators' faculties: I. conclude operations pending at dissolution; II. collect what is owed to the society and pay what it owes, TAKING INTO ACCOUNT THE FISCAL OBLIGATIONS and those derived from compliance with its merchant obligations; III. sell the society's goods; IV. practice the FINAL BALANCE of the liquidation, submitted to the socios' discussion and approval per the society's nature; V. DEPOSIT the final balance in the Commerce Registry once approved by the junta general de accionistas — published in the Registry's Official Organ for material publicity; VI. liquidate each socio's participation in the social equity; VII. grant the liquidation escritura and obtain its inscription. It is TERMINANTLY PROHIBITED to liquidators to INITIATE NEW SOCIAL OPERATIONS | `sv/sources/07_Codigo_Comercio.pdf` | Art. 332 pp.60-61 (EVID-221; txt PAGE 60-61) |
| LB-015 | Código de Comercio, Art. 333: "Mientras dure el proceso de liquidación los socios pueden acordar los repartos parciales del haber social que sean compatibles con el interés de la sociedad y de sus acreedores. El acuerdo se tomará con la mayoría necesaria para modificar el pacto social." Art. 334: "El acuerdo sobre distribución parcial deberá publicarse en la misma forma y para los mismos efectos que el acuerdo de reducción del capital. El acuerdo no podrá ejecutarse, mientras no haya transcurrido un plazo igual al señalado en el artículo 30, con iguales efectos a los que en el mismo se expresan." | While the liquidation lasts, the socios may agree PARTIAL DISTRIBUTIONS of the social equity compatible with the interest of the society and its creditors; the agreement is taken with the majority needed to modify the pacto social. The partial-distribution agreement is published in the SAME form and for the same effects as a capital-reduction agreement (Art. 486 engine, SV-CML-FR-017 by id), and may NOT be executed until a term equal to Art. 30's (30 days from the third publication) has run, with the same effects | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 333-334 p.61 (EVID-221; txt PAGE 61) |
| LB-016 | Código de Comercio, Art. 335 (intro + ordinals I-VI): "En la liquidación de las sociedades de personas, una vez pagadas las deudas sociales, el remanente se distribuirá entre los socios conforme a las siguientes reglas: I.- Si los bienes que constituyen el haber social son fácilmente divisibles, se repartirán en la proporción que corresponda a la participación de cada socio en la masa común. II.- Si entre los bienes que constituyen el activo social se encontraren los mismos que fueron aportados por algún socio u otros de idéntica naturaleza, dichos bienes deberán ser entregados de preferencia al socio que los aportó, si se puede realizar cómodamente y el pacto social lo permite. III.- Los bienes se fraccionarán en las partes proporcionalmente respectivas, compensándose entre los socios las diferencias que hubiere. IV.- Una vez formados los lotes, el o los liquidadores convocarán a los socios a una junta, en la que se les dará a conocer el proyecto respectivo, y aquéllos gozarán de un plazo de ocho días hábiles a partir del siguiente a la fecha de la junta, para solicitar modificaciones, si creyeren perjudicados sus derechos. V.- Si los socios manifestaren expresamente su conformidad, o si durante el plazo que se acaba de indicar no formularen observaciones, se les tendrá por conformes con el proyecto y el o los liquidadores harán la respectiva adjudicación, otorgándose, en su caso, los documentos que procedan. VI.- Si durante el plazo a que se refiere el ordinal IV, los socios formularen observaciones al proyecto de división, el o los liquidadores convocarán a una nueva junta, en el plazo de ocho días, para que, de común acuerdo, se hagan al proyecto las modificaciones a que haya lugar; y si no fuere posible obtener el acuerdo, el o los liquidadores adjudicarán el lote o lotes respecto de los cuales hubiere disconformidad, en común a los respectivos socios; y la situación jurídica resultante entre los adjudicatarios se regirá por las reglas de la copropiedad." | In liquidating sociedades de personas, once the social debts are paid the REMANENT distributes per: I. easily divisible goods prorata to each socio's share in the common mass; II. goods identical to those a socio aported are delivered PREFERENTIALLY to that socio if realizable comfortably and the pacto allows; III. goods fractioned in proportional parts, differences compensated among socios; IV. once lots are formed the liquidators convene a junta presenting the project — socios have EIGHT HÁBILES DAYS from the day after the junta to request modifications if they feel prejudiced; V. express conformity or silence within the term = consent, and the liquidators adjudicate; VI. observations → a new junta within eight days for common-agreement modifications, failing which the disputed lots adjudicate IN COMMON to the respective socios under copropiedad rules | `sv/sources/07_Codigo_Comercio.pdf` | Art. 335 pp.61-62 (EVID-221; txt PAGE 61-62) |
| LB-017 | Código de Comercio, Art. 336: "En la liquidación de las sociedades de capitales, los liquidadores procederán a distribuir entre los socios el remanente, después de pagadas las obligaciones sociales, con sujeción a las siguientes reglas: I.- En el balance final se indicará la parte que a cada socio le corresponde en el haber social. II.- Dicho balance se publicará y quedará, así como los papeles y libros de la sociedad, a disposición de los accionistas, quienes gozarán de un plazo de quince días, a partir de la última publicación, para presentar sus reclamaciones a los liquidadores. III.- Transcurrido dicho plazo, los liquidadores convocarán a una junta general de accionistas, para que aprueben en definitiva el balance. Esta junta será presidida por uno de los liquidadores." | In liquidating sociedades de capitales the liquidators distribute the remanent after social obligations are paid, per: I. the FINAL BALANCE indicates each socio's part in the social equity; II. the balance is published and remains — together with the society's papers and books — at the accionistas' disposal, who have FIFTEEN DAYS from the LAST PUBLICATION to present claims to the liquidators; III. after that term the liquidators convene a junta general de accionistas to DEFINITIVELY approve the balance, presided by one of the liquidators | `sv/sources/07_Codigo_Comercio.pdf` | Art. 336 p.62 (EVID-221; txt PAGE 62) |
| LB-018 | Código de Comercio, Art. 337: "En la misma sesión de junta general de accionistas en que se apruebe el balance final, podrán los liquidadores proceder a efectuar los pagos que les correspondan a aquellos accionistas presentes o representados. Cuando las acciones a ser liquidadas sean nominativas, los pagos a que hace referencia el inciso anterior, se efectuarán a favor del último accionista que aparezca registrado como tal en el libro de registro correspondiente, cancelándose inmediatamente dicho registro, todo sin perjuicio de la responsabilidad del accionista a cuyo favor se hayan liquidado las acciones, frente a terceros de buena fe a quienes haya traspasado con anticipación a la liquidación los títulos respectivos o constituido gravámenes." [incisos 3-5 summarized — gravámenes registered on the acciones: liquidation sums consigned judicially before a Mercantile Tribunal for the accionista, judge cites the secured creditor within tercero día to prove the guaranteed obligation (delivery as necessary deposit if not yet exigible, as payment if matured; unproven → gravamen extinguished, sums delivered to the accionista); embargoes: sums placed at the disposal of the Tribunal that ordered the titles' sequestration; bearer acciones: payment only against delivery of the titles] Art. 338: "Las sumas que pertenezcan a los accionistas y que no fuere posible pagar en la sesión de junta general que aprueba el balance final, de la manera expresada en el artículo anterior, se depositarán en una institución bancaria, a la orden del accionista, si la acción fuere nominativa, o de quien presente el título, si fuere al portador, para cuyo efecto se indicará su número. Este depósito deberá efectuarse dentro del plazo de tres días hábiles contados a partir de la fecha de la aprobación del balance final. Si transcurren cinco años sin que ninguna persona reclame la entrega de las cantidades depositadas, la institución bancaria deberá entregarlas al centro de beneficencia pública que designe la Secretaría de Salud Pública y Asistencia Social." | In the same junta session approving the final balance, liquidators may pay accionistas PRESENT or represented. For NOMINATIVE acciones payment goes to the LAST accionista registered in the corresponding register book, that register CANCELLED immediately — without prejudice to the accionista's liability towards good-faith third parties to whom he transferred titles or constituted gravámenes before liquidation. [Gravamen/embargo consignment mechanics summarized above.] Sums not payable in that session are DEPOSITED in a banking institution to the accionista's order (nominative) or title-bearer (al portador, number indicated), within THREE HÁBILES DAYS of the final balance's approval; after FIVE YEARS unclaimed, the bank delivers them to the public charity designated by the Secretaría de Salud Pública y Asistencia Social | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 337-338 pp.62-63 (EVID-221; txt PAGE 62-63) |
| LB-019 | Código de Comercio, Art. 338-A: "Efectuados los pagos o realizados los depósitos a que se refieren los Arts. 337 y 338 de este Código, los liquidadores procederán a otorgar la escritura pública de liquidación y obtener su inscripción en el Registro de Comercio." Art. 339: "En lo que sea compatible con el estado de liquidación, la sociedad continuará rigiéndose por las normas correspondientes a su especie. A los liquidadores les serán aplicables las normas referentes a los administradores, con las limitaciones inherentes a su carácter." | Once the payments are made or the deposits of Arts. 337/338 realized, the liquidators grant the PUBLIC DEED OF LIQUIDATION and obtain its inscription in the Commerce Registry. To the extent compatible with the liquidation state, the society continues governed by its species' norms; the administrators' norms apply to liquidators with the limitations inherent to their character | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 338-A, 339 p.63 (EVID-221; txt PAGE 63) |
| LB-020 | Código de Comercio, Art. 340: "Las deudas a favor de la sociedad, sean de naturaleza Civil, Mercantil, Tributaria o de cualquier otra índole, que no hayan podido ser cobradas durante el período de la liquidación o cualquiera de sus prórrogas, serán liquidadas a favor de los accionistas o socios, por medio de cesión de derechos personales o cesión de derechos litigiosos, según sea el caso; las cesiones se harán a título de dación en pago en proporción a la parte que a cada socio o accionista le corresponde en el haber social. Asimismo, la venta de los bienes de la sociedad que no hayan podido celebrarse durante el período de la liquidación o cualquiera de sus prórrogas, serán liquidadas a favor de los accionistas o socios, por medio de dación en pago en proporción a la parte que a cada socio o accionista le corresponda en el haber social. Tanto en las cesiones de derechos, como en las daciones en pago de bienes, corresponderá a los liquidadores efectuar la tradición del dominio en representación de la sociedad. La notificación de la cesión de crédito a que se refiere el inciso anterior, podrá hacerse mediante publicación en extracto de la transferencia por una sola vez en dos periódicos de circulación nacional. Los documentos sociales, los libros y papeles de la sociedad, se depositarán en una institución bancaria o en la persona que designen la mayoría de los socios; el depósito durará diez años. Si no se hiciere la designación, se depositarán en el lugar que el Juez competente designe. Si la liquidación hubiere sido Judicial, el depósito se realizará siempre, en el lugar que el Juez competente designe. En caso de gravámenes existentes a favor de sociedades liquidadas, el interesado podrá solicitar su cancelación registral a la Oficina que ejerce la vigilancia del Estado, la que publicará un extracto de la solicitud por una sola vez en dos periódicos de circulación nacional, a costa del interesado. Transcurridos quince días contados a partir de la publicación, sin que se haya presentado oposición, la Oficina que ejerce la vigilancia del Estado otorgará los documentos necesarios para cancelar registralmente el gravamen correspondiente." | Debts in the society's favor — Civil, Mercantile, TRIBUTARY or any other nature — uncollectable during the liquidation or its prórrogas are liquidated in favor of the socios by CESSION of personal or litigious rights as the case may be, as DACIÓN EN PAGO pro-rata to each socio's share; likewise goods unsold during the liquidation are liquidated by dación en pago pro-rata. The liquidators effect the TRADITION of dominio representing the society. Credit-cession notification may be made by publishing an extract of the transfer ONCE in TWO nationally circulated newspapers. The society's DOCUMENTS, BOOKS AND PAPERS are DEPOSITED in a banking institution or the person designated by the MAJORITY of the socios; the deposit lasts TEN YEARS. Absent designation, deposited where the competent Judge designates; in judicial liquidations, always where the Judge designates. For gravámenes in favor of liquidated societies, the interested party may seek registry cancellation from the state-vigilance office, which publishes an extract once in two national dailies at the party's cost; fifteen days after publication without opposition, the office grants the cancellation documents | `sv/sources/07_Codigo_Comercio.pdf` | Art. 340 pp.63-64 (EVID-221/215; txt PAGE 63-64) |
| LB-021 | Código de Comercio, Art. 341: "Disuelta una sociedad de personas y estando todos los socios de acuerdo sobre la forma en que haya de liquidarse el haber social, podrán otorgar desde luego la escritura de liquidación mediante la concurrencia de todos ellos, siempre que previamente se cancelen las deudas sociales." Art. 342: "Al inscribirse en el Registro de Comercio la escritura de liquidación de una sociedad, se cancelarán las inscripciones de las escrituras de constitución y modificación de la misma y de sus estatutos si los hubiere. El Registro de Comercio deberá comunicar, por medio de oficio, la inscripción de la liquidación de toda sociedad, a cualquier institución que por la naturaleza de las actividades de las empresas de la sociedad liquidada, hayan otorgado autorizaciones de funcionamiento, a fin que se cancelen los registros correspondientes." Art. 342-A: "La junta general extraordinaria de una sociedad en liquidación, podrá revocar el acuerdo de disolución previamente adoptado, siempre y cuando la causal invocada para la misma haya desaparecido o haya sido subsanada, según corresponda, y que el período de la liquidación o cualquiera de sus prórrogas no hubiere concluido. Inscrito el acuerdo de revocatoria de disolución en el Registro de Comercio, la sociedad normalizada podrá iniciar nuevas operaciones, cesando en sus funciones los liquidadores, quienes devolverán a la junta general de la sociedad o a la persona que éstos designen, todos los bienes existentes al momento de adoptarse el acuerdo anterior, así como los libros y documentos de la sociedad, de la manera prevista en el Art. 331. Lo establecido en el presente artículo no tendrá aplicación, cuando se trate de la disolución y liquidación forzosa, a menos que lo autorice el juez competente, a petición de parte interesada." | A dissolved sociedad de personas with ALL socios agreeing on the liquidation form may grant the liquidation escritura AT ONCE by the concurrence of all, provided the social debts are first cancelled. Upon inscription of the liquidation escritura, the inscriptions of the constitution and modification deeds — and of the estatutos, if any — are CANCELLED; the Registry must notify (oficio) every institution that granted functioning authorizations to the liquidated society's enterprises, so their records are cancelled. The EXTRAORDINARY general meeting of a society in liquidation may REVOKE a previously adopted dissolution agreement when the invoked causal has disappeared or been cured and the liquidation period or any prórroga has not concluded; once the revocation is inscribed, the NORMALIZED society may initiate new operations, liquidators cease and return all existing goods, books and documents per Art. 331's manner. This does NOT apply to forced dissolution and liquidation unless the competent judge authorizes it at an interested party's request | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 341-342-A p.64 (EVID-221; txt PAGE 64) |
| LB-022 | Código de Comercio, Art. 343: "La sociedad que tenga objeto ilícito es nula; su escritura no podrá inscribirse en el Registro de Comercio. Si de hecho fuere inscrita, podrá ser declarada nula con efecto retroactivo, a pesar de lo establecido en el artículo 25. La acción de nulidad podrá ser ejercitada por cualquier persona que compruebe interés o por el Ministerio Público, y tendrá como consecuencia la disolución y liquidación de la sociedad, sin perjuicio de la responsabilidad penal que procediere. La nulidad deberá ser declarada de oficio, en todo caso en que el Juez tenga conocimiento de ella. El Juez que decrete la nulidad podrá practicar por sí mismo la liquidación o designar un liquidador; en este caso, deberá oír previamente a la oficina que ejerce la vigilancia del Estado y la designación recaerá, si ello fuere posible, en una institución bancaria. El importe resultante de la liquidación se aplicará al pago de la responsabilidad civil. El remanente, si lo hubiere, se destinará a la institución de beneficencia pública de la localidad en que la sociedad haya tenido su domicilio, a juicio del Juez." Art. 344: "La sociedad que tenga causa ilícita también es nula, ya sea que la causa conste en el instrumento o que se establezca con posterioridad por cualquier medio legal de prueba, y le serán aplicables las disposiciones del artículo anterior. Si no se expresare la causa en el instrumento, se presumirá lícita mientras no se pruebe lo contrario." Art. 345: "La falta de consentimiento de la mayoría de los socios invalida el contrato social. La acción para que se reconozca la invalidez, corresponderá al socio o socios perjudicados, o al Ministerio Público. En este caso, se aplicará lo dispuesto en el artículo 343, tanto en lo que respecta a la forma de practicar la liquidación como al destino de los fondos resultantes de la misma. La responsabilidad civil que deberá cubrirse, comprende la devolución de los aportes y la indemnización de perjuicios a los socios que no hayan consentido. La falta de consentimiento de un socio o de la minoría de ellos, se regulará por lo establecido en el inciso segundo del artículo 26." | A society with an ILLICIT OBJECT is NULL; its deed cannot be inscribed; if in fact inscribed, it may be declared null WITH RETROACTIVE EFFECT despite Art. 25 (the sole statutory override of the no-retroactive-nullity protection, SV-CML-FR-048 kin). The nullity action belongs to any person proving interest or the Ministerio Público; consequence = dissolution and liquidation, without prejudice to penal liability; nullity declared DE OFICIO whenever the Judge learns of it. The judge may liquidate himself or designate a liquidator (hearing the vigilance office first; designation preferably a banking institution); proceeds pay the civil liability; any REMANENT goes to the local public charity. A society with illicit CAUSA is also null (cause proven by any legal means; cause unexpressed is presumed lawful). Lack of consent of the MAJORITY of socios invalidates the social contract (same liquidation/destination per Art. 343; civil liability covers returning aportes and indemnifying non-consenting socios); a MINORITY's or single socio's lack of consent is governed by Art. 26 inciso 2 | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 343-345 pp.64-65 (EVID-222; txt PAGE 64-65) |
| LB-023 | Código de Comercio, Art. 346: "La sociedad que careciere absolutamente de formalidades para su otorgamiento, no tiene existencia legal, pero la adquirirá al contratar con terceros, en los términos que se indican en el artículo 348. Los interesados o el Ministerio Público tendrán acción para pedir al Juez competente que proceda a liquidar la sociedad. Previamente a la liquidación, el Juez señalará un plazo dentro del cual la sociedad deberá constituirse con las formalidades legales, si se quiere evitar su liquidación. Este plazo no podrá ser menor de noventa días, ni superior a ciento veinte. El importe resultante de la liquidación se aplicará al pago de la responsabilidad civil y el remanente, si lo hubiere, será repartido entre las personas que hicieron aportes a la sociedad de hecho, a prorrata de los mismos. Ningún aportante podrá recibir más del valor por él aportado; si hubiere utilidad, ésta se destinará a la institución de beneficiencia pública del lugar donde la sociedad tenga su domicilio, a juicio del Juez." Art. 347: "La sociedad cuya escritura social no llene los requisitos que la ley exige para la clase de sociedad de que se trate, estará en las mismas condiciones indicadas en los dos primeros incisos del artículo anterior mientras las irregularidades no hayan sido subsanadas. La escritura social deficiente no podrá ser inscrita, en tanto sus deficiencias no hayan sido corregidas. [remanent-disposition incisos summarized — like Art. 346 the liquidation proceeds pay civil liability, remanent to socios per the escritura's pertinent clause; but where the deficiency is non-made aportations in the dates/proportions the law requires, the remanent goes NOT to devolución or profit distribution but to the local public charity]" | A society ABSOLUTELY lacking formalities has NO legal existence, but acquires it upon contracting with third parties per Art. 348's terms. Interested parties or the Ministerio Público may ask the judge to liquidate; BEFORE liquidating the judge sets a term for the society to constitute with legal formalities — NOT LESS THAN NINETY NOR MORE THAN ONE HUNDRED TWENTY DAYS. Proceeds pay civil liability; remanent to the de-facto contributors pro-rata (no one receives more than contributed; profits to the local public charity). A society whose escritura fails its class's requisites stands in the SAME conditions until the irregularities are CURED; the deficient escritura CANNOT be inscribed until corrected [remanent-disposition summarized above] | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 346-347 p.65 (EVID-222; txt PAGE 65) |
| LB-024 | Código de Comercio, Art. 348: "Las sociedades a que se refieren los artículos anteriores, que se hubieren exteriorizado como tales frente a terceros, tienen personalidad jurídica únicamente en cuanto los perjudique, pero no en lo que pudiere beneficiarles. Los socios, los administradores y cualesquiera otras personas que intervengan en su funcionamiento, responderán por las obligaciones de dichas sociedades frente a terceros, personal, solidaria e ilimitadamente, sin perjuicio de las responsabilidades penales en que hubieren incurrido. Las relaciones internas de estas sociedades se regirán por el pacto social respectivo, si lo hubiere; en su defecto, por las disposiciones generales contenidas en este Código, según la clase de sociedad de que se trate." Art. 349: "La sociedad que estando legalmente organizada ejecute actos ilícitos, será declarada disuelta y se liquidará inmediatamente. La acción de disolución compete a cualquier interesado o al Ministerio Público. El Juez deberá decretarla de oficio al tener conocimiento de la actividad ilícita. El Juez podrá practicar por sí mismo la liquidación o designar un liquidador; en este caso, deberá oír previamente a la oficina que ejerce la vigilancia del Estado y la designación recaerá, si ello fuere posible, en una institución bancaria. El importe resultante de la liquidación se distribuirá conforme a lo dispuesto en el artículo 343." Art. 350: "Lo dispuesto en el artículo anterior es aplicable a la sociedad que, sin la debida autorización, se dedique o realice actividades que la requieran, tales como operaciones bancarias, de almacenes generales de depósito, de ahorro y otras similares." | Societies of the preceding articles EXTERIORIZED before third parties have legal personality ONLY insofar as it PREJUDICES them, never to their benefit; socios, administrators and anyone else intervening in their functioning answer the obligations to third parties PERSONALLY, SOLIDARILY and UNLIMITEDLY (penal liabilities preserved); internal relations follow the pacto social, failing that the Code's general provisions per class. A legally-organized society EXECUTING ILLICIT ACTS is declared dissolved and liquidated immediately (action of any interested party or the Ministerio Público; judge decrees de oficio on learning of the illicit activity; liquidation per Art. 343's distribution). Art. 349 likewise applies to a society that without due AUTHORIZATION engages in activities requiring it — banking, general-deposit warehouses, savings and similar operations | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 348-350 pp.65-66 (EVID-222; txt PAGE 65-66) |
| LB-025 | Código de Comercio, Art. 353: "Si la escritura social o sus reformas no se presentaren para su inscripción en el Registro de Comercio, dentro de los quince días siguientes a su otorgamiento, cualquier socio podrá gestionarla judicial o administrativamente. Todo interesado o el Ministerio Público, podrá requerir judicialmente a toda sociedad, la comprobación de su existencia regular. El requerimiento, además de ser notificado personalmente, se publicará. Transcurridos cuatro meses del requerimiento sin que se haya comprobado la inscripción en el Registro, la sociedad se pondrá en liquidación. [notary-duty and registry-list incisos summarized — every Notary before whom a constitution or reform deed is granted must warn the grantors of the registration duty, its effects and the sanctions for its absence; the Registro de Comercio must monthly remit the state-vigilance office a list of such instruments' inscriptions with the corresponding information; the Ministerio Público's faculty in this article confers no Art. 352-I intervention power on the vigilance office; the liquidation is practiced per the pacto social and, failing it, the Code's pertinent provisions]" | If the social deed or its reforms are NOT presented for inscription within FIFTEEN DAYS of their execution, ANY socio may procure it judicially or administratively. Any interested party or the Ministerio Público may judicially require a society to PROVE its regular existence; the requirement is personally notified AND published; FOUR MONTHS from the requirement without the inscription proved, the society enters liquidation. [Notary warning duty and the Registry's monthly lists to the vigilance office summarized; liquidation per pacto/Code.] | `sv/sources/07_Codigo_Comercio.pdf` | Art. 353 p.66 (EVID-222; txt PAGE 66) |
| LB-026 | Código de Comercio, Art. 354: "La sociedad que realice actos lícitos, pero que se encuentren fuera de su objeto social, estará obligada a reformar este último, a fin de que comprenda sus nuevas actividades. Cualquier interesado tendrá acción para exigir la reforma; el Juez señalará un plazo de cuatro meses para que ésta se verifique y, vencido dicho plazo, sin que la sociedad haya cumplido el requerimiento, la pondrá en liquidación. La liquidación se practicará de acuerdo con lo dispuesto en el artículo anterior." Art. 355: "Los que realicen actos jurídicos como representantes o mandatarios de cualquiera de las sociedades contempladas en los artículos anteriores de este capítulo, responderán solidariamente del cumplimiento de los mismos frente a terceros. También serán solidariamente responsables todos los socios y todos los que participen en alguna forma en el manejo de los asuntos sociales, aún cuando no hayan intervenido en el acto de que se trate. Cualquier interesado, incluso los socios no culpables de la irregularidad, podrán exigir daños y perjuicios a los culpables y a los que actuaren como representantes o mandatarios de la sociedad." Art. 356: "La sociedad que prolongue su existencia más allá del plazo fijado en el pacto social para su disolución, sin haber otorgado previamente la prórroga correspondiente, así como aquélla que se encuentre afectada por cualquier otra causal de disolución contemplada en este Código y no proceda a subsanarla, continuará funcionando en forma regular, hasta que se otorgue la escritura que la disuelva o se haga uso de la acción de disolución. Demandada la disolución por cualquiera de los motivos señalados en el inciso anterior, el Juez concederá, como requisito previo para tramitar el juicio, un plazo no menor de noventa días ni mayor de ciento veinte dentro del cual la sociedad podrá regularizar su existencia." | A society performing LAWFUL acts OUTSIDE its social object MUST REFORM the object to comprise the new activities; any interested party has action to demand the reform; the judge sets a FOUR-MONTH term, and on its expiry unfulfilled the society enters liquidation (practiced per the preceding article). Those performing juridical acts as representatives or attorneys of the chapter's societies answer SOLIDARILY for compliance to third parties; ALL socios and everyone participating in the society's management are likewise solidarily responsible EVEN WITHOUT intervening in the act; any interested party — including non-culpable socios — may demand damages from the culpable and from representatives/attorneys. A society prolonging existence past its pacto-fixed dissolution term without prior prórroga, or affected by any other dissolution causal it fails to cure, continues functioning REGULARLY until the dissolving escritura is granted or the dissolution action is used; once dissolution is sued, the judge grants — as a prerequisite to tramiting the suit — a term of NOT LESS THAN NINETY NOR MORE THAN ONE HUNDRED TWENTY DAYS to regularize | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 354-356 p.67 (EVID-222; txt PAGE 67) |
| LB-027 | Código de Comercio, Art. 357: "La sociedad reducida a un solo socio, dejará de existir como tal, si transcurrieren tres meses sin que se haya traspasado alguna participación social a otra persona; pero la empresa mercantil subsistirá como empresa individual perteneciente al único socio. La empresa será de responsabilidad ilimitada si en la sociedad de que proviene había, por lo menos, un socio que tuviere este tipo de responsabilidad. La empresa será de responsabilidad limitada, si en la sociedad de que proviene todos los socios, respondían de esta manera. El único socio tendrá obligación de otorgar los instrumentos necesarios para convertir legalmente la sociedad en una empresa individual dentro de los dos meses subsiguientes a la expiración del plazo previsto en el inciso primero de este artículo, bajo pena de que su empresa se considere como una sociedad irregular y se le apliquen las disposiciones previstas en el artículo 347.-" | A society reduced to a SINGLE socio CEASES TO EXIST AS SUCH if THREE MONTHS pass without some participación transferred to another person; but the empresa mercantil SUBSISTS as an individual enterprise belonging to the sole socio. The enterprise has UNLIMITED liability if the source society had at least one socio of that type; LIMITED liability if all source socios so responded. The sole socio MUST grant the instruments to convert the society into an individual enterprise within the TWO MONTHS following the first term's expiry — failing which his enterprise is deemed an IRREGULAR SOCIETY subject to Art. 347 | `sv/sources/07_Codigo_Comercio.pdf` | Art. 357 p.67 (EVID-222; txt PAGE 67) |
| LB-028 | Código de Comercio, Art. 358: "Las sociedades extranjeras que deseen realizar actos de comercio en El Salvador, fijando domicilio en el país o estableciendo sucursales, deberán registrarse en el Registro de Comercio. Para la obtención del registro mencionado, el representante legal de la sociedad extranjera o su apoderado general o especial, deberá presentar solicitud, acompañada de los documentos siguientes: a) Estatutos que comprueben que la sociedad está legalmente constituida, de acuerdo con las leyes del país en que se hubiera organizado. b) Documentación probatoria de que la decisión de fijar domicilio en El Salvador o de operar en el país, ha sido válidamente adoptada de conformidad a sus estatutos. c) Poder con que actuará el representante de la sociedad extranjera, el cual señalará las facultades de éste en forma amplia, clara y precisa. El representante nombrado deberá residir permanentemente en el país. d) El capital social suficiente para realizar sus actividades sociales, cuyo ingreso se comprobará con el registro de inversión extranjera, que para tal efecto lleva el Ministerio de Economía. e) Balance inicial certificado por Contador Público autorizado en el país, de la sociedad extranjera o de la sucursal que se pretende, en el cual se refleje su capital social. En la solicitud respectiva, la sociedad o sucursal extranjera deberá protestar sumisión a las leyes, tribunales y autoridades de la República de El Salvador, en relación a los actos, derechos y obligaciones que adquiera en el territorio salvadoreño, o que hayan de surtir efectos en el mismo." Art. 359: "Satisfechos los requisitos anteriores, el Registrador de Comercio registrará a la sociedad extranjera que fije su domicilio en el país, o en su caso, la sucursal que operará en territorio nacional, y el poder con que actúa su representante, emitiendo el registro único de empresa de conformidad a lo establecido en el Capitulo II, Título I, del Libro Segundo del presente Código." | Foreign societies wishing to perform acts of commerce in El Salvador — FIXING DOMICILE in the country or ESTABLISHING SUCURSALES — must register in the Commerce Registry. For the registry the legal representative or general/special attorney presents a solicitud with: a) STATUTES proving lawful constitution under the organizing country's laws; b) proof the decision to fix Salvadoran domicile or operate in the country was validly adopted per those statutes; c) the POWER of the representative — faculties stated broadly, clearly and precisely — the appointed representative RESIDING PERMANENTLY in the country; d) SUFFICIENT SOCIAL CAPITAL, its entry proved by the foreign-investment registry kept by the MINISTERIO DE ECONOMÍA (MINEC); e) an INITIAL BALANCE certified by a Contador Público authorized in the country, of the society or intended sucursal, reflecting its social capital. The application must PROTEST SUBMISSION to the laws, courts and authorities of El Salvador for acts, rights and obligations acquired in or affecting Salvadoran territory. Requisites satisfied, the Registrar registers the sociedad or sucursal AND the representative's power, issuing the registro único de empresa per Libro Segundo Título I Capítulo II | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 358-359 pp.67-68 (EVID-222; txt PAGE 67-68) |
| LB-029 | Código de Comercio, Art. 360: "Para todos los efectos legales, las sociedades extranjeras que operen en la República por medio de Sucursal, se considerarán domiciliadas en el lugar, en que establezcan su oficina principal. Todo aumento o disminución del capital que sufriere la sociedad o sucursal extranjera, así como su cancelación, deberán inscribirse en el Registro de la Inversión Extranjera que para tal efecto lleva el Ministerio de Economía, y posteriormente en el Registro de Comercio; quienes inmediatamente darán aviso a la Oficina que Ejerce la Vigilancia del Estado." Art. 361: "La Oficina que Ejercer la Vigilancia del Estado velará que las sociedades extranjeras cumplan con las obligaciones estrictamente mercantiles establecidas en el presente Código." [printed "Ejercer" sic] | For all legal effects, foreign societies operating through a SUCURSAL are DOMICILED where they establish their principal office. Every capital increase or decrease of the foreign society or sucursal — and its cancellation — must be inscribed FIRST in the Registro de la Inversión Extranjera kept by MINEC and AFTERWARDS in the Registro de Comercio, both immediately noticing the state-vigilance office. The state-vigilance office ensures foreign societies comply with the strictly mercantile obligations of this Code | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 360-361 p.68 (EVID-222; txt PAGE 68) |
| LB-030 | Código de Comercio, Art. 620 (incisos 1-2): "La liquidación voluntaria o forzosa de la empresa individual de responsabilidad limitada se sujetará, en cuanto fuere aplicable, a las reglas contenidas en este Código para liquidar las sociedades de personas. La liquidación voluntaria de estas empresas, quedará sujeta a la verificación del estado de solvencia o autorización tributaria, de conformidad con lo establecido en el Código Tributario." [incisos 3-4 summarized — in FORCED liquidation the judge first requests a solvency report from the tax administration and a Registro de Comercio report on the enterprise's merchant-obligations compliance (rendered within tercero día hábil), decrees liquidation even with pending obligations (warning them to the liquidator at swearing-in); the executed sentence is preventively annotated in the Registro, effective at inscription, adding "en liquidación" to the enterprise's name; at the end the liquidator reports to the judge, who orders the enterprise held liquidated and libers oficio to the Registry, which also cancels the constitution/modification inscriptions] | The voluntary or forced liquidation of the EIRL is subject, as applicable, to this Code's rules for liquidating sociedades de personas. The VOLUNTARY liquidation of these enterprises is subject to VERIFICATION OF THE STATE OF SOLVENCY or tax authorization, per the Código Tributario (external CT gate — mechanics not in this corpus, OQ-003). [Forced-liquidation judicial-report/annotation/"en liquidación"-suffix/final-cancellation mechanics summarized; full text txt PAGE 111; EIRL profile owned by `07_empresa-mercantil-eirl.md`.] | `sv/sources/07_Codigo_Comercio.pdf` | Art. 620 pp.110-111 (EVID-224; txt PAGE 110-111) |
## 3. Functional Requirements

### 3.1 Capital-variable regime (Arts. 306-314)

- **SV-CML-FR-072:** The system shall model the capital-VARIABLE regime
  (Arts. 306-307) as an attribute any sociedad class may adopt (regime
  field consumed from SV-CML-FR-042 by id): under it the capital moves by
  increase — later *aportaciones*, admission of new socios,
  capitalization of reserves and profits, asset revalidation — and by
  decrease — partial or total withdrawal of aportations, asset
  devaluation — with NO formalities beyond this chapter's (the Art. 30
  fixed-regime consent/publication/opposition mechanics of SV-CML-FR-050
  do NOT apply to variable-regime movements; only this section's rules
  do); the capital-variable sociedad is governed by its species' rules
  PLUS the S.A. rules on balances, administrator liability and auditor
  vigilance (profile flags per SV-CML-FR-070 consumed by id); the
  escritura carries the increase/decrease conditions (Art. 309), and in
  share societies the *pacto social* — or failing it the *junta general
  extraordinaria* — fixes each increase and the form and term of the
  corresponding emission; acciones of capital-variable share societies
  are ALWAYS nominative (Art. 311 — the FR-066 nominative invariant made
  absolute, no bearer conversion under this regime).
  (LB-001; LB-002; LB-003; EVID-221)
- **SV-CML-FR-073:** The system shall enforce the Art. 308 naming duty:
  every capital-variable sociedad's *razón social o denominación* carries
  "de capital variable" or its abbreviation "de C.V." appended AFTER the
  type's own suffix (consumed from 04's society.type `suffix_rule`
  profile row by id — Ltda. · S. en C. · etc.); the suffix validator
  flags a missing "de C.V." as a naming defect with the irregularity/
  unlimited-liability exposure of §3.5 of this file (Art. 101-kin
  discipline via SV-CML-FR-058's pattern); and the composed name flows
  into DTE emitter-name data as a POINTER only (e-invoicing A11 cluster;
  never re-derived here).
  (LB-002; EVID-221)
- **SV-CML-FR-074:** The system shall implement the Art. 310 minimum
  capital and disclosure discipline: the record of a capital-variable
  sociedad carries its *capital mínimo* — for S.A./SRL/comandita por
  acciones ≥ the type's statutory floor (profile-driven values consumed
  from SV-CML-FR-059/SV-CML-FR-065 by id; no value invented here), for
  colectiva/comandita simple ≥ ONE-FIFTH of the initial capital — and
  the announcement guard: any publication or announcement stating the
  authorized-increase capital or the capital social WITHOUT stating the
  minimum capital simultaneously is flagged as a prohibited announcement,
  with the administrators'/officers' unlimited-and-solidary liability
  exposure recorded (the statutory minimum is never below the floor
  validator; the *mínimo* also bounds FR-076 separation).
  (LB-003; EVID-221)
- **SV-CML-FR-075:** The system shall record every capital increase and
  decrease of a capital-variable sociedad as an entry in the Art. 40-IV
  *Libro de Registro de Aumentos y Disminuciones de Capital Social* (book
  existence gate consumed from SV-CML-FR-057 by id — this FR supplies the
  movement mechanics 04 deferred): each movement entry carries its date,
  direction, amount and legal reference (junta/escritura), the book is
  consultable BY ANY PERSON HAVING AN INTEREST (public-consultation
  access profile, no socio-only gate), and it inherits the Art. 440
  discipline flags and retention via SV-CML-FR-025/SV-CML-FR-028 by id.
  (LB-004; EVID-221)
- **SV-CML-FR-076:** The system shall compute the Art. 313 withdrawal
  effects and the Art. 314 floor: a socio's partial or total retiro of
  aportations requires a notification recorded as JUDICIAL or by NOTARIAL
  ACTA (notice-kind validation); the withdrawal takes effect at the END
  of the current fiscal year if notified before the last trimester, and
  at the end of the FOLLOWING fiscal year if notified after (working
  reading per evidence gloss: a notice within the last trimester runs to
  the following year-end) — the effective date is computed and shown,
  capital not released before it; and the right of separation is BLOCKED
  where it would reduce the capital below the FR-074 minimum (floor
  check at effect time, not notice time).
  (LB-004; EVID-221)

### 3.2 Fusión (Arts. 315-321)

- **SV-CML-FR-077:** The system shall model the Art. 315-317 fusión
  pipeline: fusión takes the forms INTEGRATION (two or more societies
  constitute a new one — constitution per the new género's principles,
  FR-046 checklist consumed by id) or ABSORPTION (an existing sociedad
  absorbs — the absorbing society's escritura is MODIFIED); the new or
  absorbing sociedad acquires ALL rights and contracts ALL obligations
  of the merged/incorporated societies (universal-succession data
  continuity — merged records are superseded and cross-referenced, never
  deleted); the agreement is taken by EACH society in its
  pacto-modification form (quorum per type profile, SV-CML-FR-063 kin),
  INSCRIBED in the Registro de Comercio of each society's domicile with
  MARGINAL NOTES on their escritura inscriptions (registry-entry kinds
  consumed from SV-CML-FR-013 by id); and once registered, the agreement
  AND each society's LAST BALANCE are PUBLISHED (Art. 486 default
  engine consumed from SV-CML-FR-017 by id — the article fixes no
  different count); socios of merged societies receive participaciones or
  acciones in EQUIVALENT proportion to those held, salvo convenio
  (Art. 321).
  (LB-005; LB-006; LB-008; EVID-221)
- **SV-CML-FR-078:** The system shall compute and gate the Art. 318/320
  opposition-and-retiro window: the fusión becomes executable only AFTER
  90 DAYS from the Art. 317 publications, and only if no opposition
  stands — the 90-day clock computed by the SV-CML-FR-017 engine (from
  the day after the LAST Diario Oficial publication); within the window
  ANY interested person's opposition suspends execution until the
  interest is sufficiently guaranteed (judge's criterion; no guarantee
  needed where the new/absorbing society notoriously offers it in
  itself — exposure flags, the judicial assessment is external); an
  unfounded-opposition sentence clears execution on becoming final; and
  the DISSENTING socio's retiro right runs INSIDE the same 90-day
  window, his participación — and, for colectivo/comanditado socios,
  his UNLIMITED personal liability — continuing to guarantee
  obligations contracted BEFORE the merger agreement.
  (LB-007; EVID-221)
- **SV-CML-FR-079:** The system shall implement the Art. 319 inscription
  checkpoint and personality regime: the fusión is executed by the
  designated persons (or the administrators failing designation),
  recorded in an ESCRITURA MATRIZ whose testimonio is inscribed in the
  Registro de Comercio, taking effect FROM THE INSCRIPTION DATE; for
  inscription the Registrador verifies one of three Ley de Competencia
  alternatives — (a) NOT subject to notification under that law, (b)
  approval by the Superintendencia de Competencia, (c) notification made
  with NO resolution within that law's term — recorded as the
  checkpoint's state (registry-side verification; the Ley de Competencia
  thresholds/terms are NOT in corpus, OQ-002 — no values invented); the
  new pacto or modifications are approved with the SAME requisites as
  the merger agreement; and until the inscription the merging societies
  RETAIN their legal personality as if the fusión had not occurred —
  upon it, the merged/incorporated societies' personality is EXTINGUISHED
  (Art. 25 kin consumed from SV-CML-FR-048 by id; presentation anchor
  SV-CML-FR-016).
  (LB-008; EVID-221)

### 3.3 Transformación (Arts. 322-325)

- **SV-CML-FR-080:** The system shall model the Art. 322-323
  transformación agreement: ANY sociedad type may adopt another legal
  type, and capital-fijo societies may transform to capital-variable and
  vice versa; the agreement is taken with the SAME requisites as any
  pacto-social modification (quorum per type profile, SV-CML-FR-063
  kin); and where the transformación converts a socio's UNLIMITED
  liability into limited liability, the converting socios' unlimited
  liability SURVIVES for ALL operations realized before the
  transformation agreement's validity — recorded as a liability-survival
  exposure on the transformed record (pre-change obligations tagged;
  the liability itself is external law).
  (LB-009; EVID-221)
- **SV-CML-FR-081:** The system shall implement the Art. 323 auditor
  valúo gate: a personas→capitales transformación (and the EXECUTION of
  a fusión agreement between societies of those natures) requires a
  PRIOR valúo by the authorized auditor, whose CERTIFICATION must be
  sent to the state-vigilance office within THREE HÁBILES DAYS of its
  making (días-hábiles calendar consumed from the fiscal calendar
  engine) — tracked as a dated compliance checkpoint on the
  transformation record — and the valúo is recorded IN the escritura
  social (deed attachment; the valuation itself is the auditor's act,
  referenced never generated).
  (LB-010; EVID-221)
- **SV-CML-FR-082:** The system shall record the Art. 324-325 execution
  and succession: the transformation agreement is executed by ESCRITURA
  PÚBLICA containing ALL requisites of the newly adopted form (Art. 22/
  FR-046 checklist consumed by id), granted by designees or the
  administrators; the escritura is INSCRIBED and takes effect from its
  INSCRIPTION date — until which the society continues governed by its
  PREVIOUS norms (old-type profile stays active until the inscription
  event); and the new sociedad SUCCEEDS DE PLENO DERECHO to the former
  in rights and obligations with NO SOLUTION OF CONTINUITY — company
  records supersede-and-reference across the transformation (ledger,
  contracts and obligations continuity), never fork into unrelated
  entities.
  (LB-010; EVID-221)
### 3.4 Liquidación, closing and post-liquidation custody (Arts. 326-342-A; Art. 620 pointer)

- **SV-CML-FR-083:** The system shall implement the Art. 326
  liquidation state: a DISSOLVED sociedad enters LIQUIDATION while
  RETAINING its legal personality for liquidation purposes (lifecycle
  state: active → en liquidación → liquidada; the FR-048
  personality-state machinery consumed by id); the phrase "en
  liquidación" is APPENDED to its razón social or denominación (suffix
  propagation to documents is this file's naming fact; its DTE
  emitter-name flow is a POINTER to the e-invoicing A11 cluster — never
  re-derived here); the liquidation TERM fixed by the
  liquidator-appointing authority may NOT exceed TWO YEARS; a shorter
  agreed term may be PRORROGATED only up to that two-year maximum, the
  prórrogas agreed by the junta general and INSCRIBED in the Registro de
  Comercio (prórroga records with registry entries per SV-CML-FR-013 by
  id); and the matrícula consequence rides SV-CML-FR-012's cancellation
  cases d/f (disolución temporal / liquidación definitiva) by id.
  (LB-011; EVID-221)
- **SV-CML-FR-084:** The system shall record the Art. 327-331 liquidator
  regime: one or more LIQUIDATORS are administrators and representatives
  of the society answering PERSONALLY for acts exceeding their charge
  (exposure flag); absent pacto provision, they are appointed by the
  socios' agreement IN THE SAME ACT as the dissolution agreement/
  recognition, failing which the judicial authority appoints at any
  socio's or the FGR's request; on dissolution by SENTENCE the judge
  designates within FIFTEEN DAYS of the sentence becoming firm; until
  the appointment is INSCRIBED and the liquidators enter function, the
  ADMINISTRATORS continue in office (transition overlap tracked; dolo/
  negligence responsibility exposure noted); liquidator credenciales
  register per SV-CML-FR-014 by id; and once appointed, the
  administrators deliver ALL goods, books and documents via a DETAILED
  INVENTORY subscribed by both parties (delivery-inventory record tied
  to the book set of SV-CML-FR-057 by id). Liquidation is practiced per
  the pacto social or, failing it, socios' agreements at
  pacto-modification majorities plus the Code's chapter (Art. 330).
  (LB-012; LB-013; EVID-221)
- **SV-CML-FR-085:** The system shall implement the Art. 332 liquidator
  faculties and prohibition: conclude operations PENDING at dissolution;
  collect and pay TAKING INTO ACCOUNT THE FISCAL OBLIGATIONS and those
  derived from the society's merchant obligations (tax duties of the
  liquidation period surfaced on the liquidator's obligation checklist —
  the tax computation itself is the taxation wave's by id); sell the
  society's goods; practice the FINAL BALANCE submitted to the socios'
  discussion and approval per the society's nature; DEPOSIT the final
  balance in the Registro de Comercio once approved (deposit mechanics
  consumed from SV-CML-FR-035 by id), the balance then published in the
  Órgano Oficial del Registro de Comercio (registry-organ publication —
  NOT the Art. 486 engine; recorded as its own publication channel);
  liquidate each socio's participation; and grant the liquidation
  escritura with its inscription; the system shall BLOCK the initiation
  of NEW social operations while the society is in liquidation (guard on
  new business documents/flows with the Art. 332 prohibition reason —
  the statutory "terminantemente prohibido").
  (LB-014; EVID-221)
- **SV-CML-FR-086:** The system shall compute the Art. 333-338/341
  distribution-and-payment mechanics: PARTIAL distributions while the
  liquidation lasts, compatible with society and creditor interests, at
  pacto-modification majority, published like capital-reduction
  agreements (SV-CML-FR-017 engine by id) and EXECUTABLE only after the
  Art. 30-equivalent 30-day window from the third publication; the
  personas-society remanent rules (prorata distribution of divisible
  goods; preferential return of aportado-kind goods; lot formation with
  an 8-DÍA-HÁBIL modification window from the junta; silence = consent;
  disputed lots adjudicated in common under copropiedad) and the
  capitales final-balance discipline (each socio's part stated;
  publication + books/papers at accionistas' disposal; 15-DAY claims
  window from the LAST publication; definitive junta approval presided
  by a liquidator); PAYMENTS at the approving junta to present/
  represented accionistas — nominative acciones paid to the LAST
  registered accionista with the register CANCELLED immediately
  (good-faith transferee/gravamen-holder exposure note), gravámenes
  handled by judicial consignment and embargoes by tribunal disposal,
  bearer acciones paid only against title delivery; sums unpayable at
  the session deposited in a BANK within THREE HÁBILES DAYS of final
  balance approval (five-year unclaimed lapse to the designated public
  charity recorded); and the Art. 341 express route — a personas society
  with ALL socios agreeing, debts first cancelled, may grant the
  liquidation escritura at once by unanimous concurrence.
  (LB-015; LB-016; LB-017; LB-018; LB-021; EVID-221)
- **SV-CML-FR-087:** The system shall record the Art. 338-A/340/342
  closing: after the Art. 337/338 payments or deposits, the liquidators
  grant the ESCRITURA PÚBLICA DE LIQUIDACIÓN and obtain its inscription
  (registry entry per SV-CML-FR-013 by id); on that inscription the
  society's constitution/modification/estatutos inscriptions are
  CANCELLED and the Registry notifies (oficio) every institution that
  granted functioning authorizations so their records cancel (tracking
  surface only — the oficios are registry-side); uncollected debts
  (civil, mercantile, TRIBUTARY or any nature) and unsold goods are
  liquidated to the socios by CESSION / DACIÓN EN PAGO pro-rata to
  their shares, the liquidators effecting the tradition of dominio in
  the society's representation, the credit-cession notification
  publishable as an extract ONCE in TWO national dailies (its own
  publication form — not the 486 engine); while the liquidation lasts,
  the society keeps its species' norms insofar as compatible, and the
  administrators' norms apply to liquidators with their inherent
  limitations (Art. 339).
  (LB-019; LB-020; EVID-221)
- **SV-CML-FR-088:** The system shall implement the Art. 340-3 post-
  liquidation custody and its matrix feed: upon closing, the society's
  DOCUMENTS, BOOKS AND PAPERS are DEPOSITED in a banking institution OR
  the person designated by the MAJORITY of socios, the deposit lasting
  TEN YEARS — absent designation, deposited where the competent judge
  designates, and in JUDICIAL liquidations always where the judge
  designates (deposit record: custodian kind, designee, deposit date,
  10-year clock); this deposit FEEDS the canonical retention matrix —
  SV-CML-FR-028 row a consumed by id, never restated — and the
  liquidation-closing event this FR emits is the lifecycle pointer that
  SV-CML-FR-029's row-a post-liquidation extension (five years after
  liquidating all businesses) consumes; the Art. 340 gravamen-cancellation
  route (registry application, once-in-two-dailies extract at the
  interested party's cost, 15-day opposition, then cancellation
  documents) is recorded as a document-workflow surface.
  (LB-020; EVID-221/215)
- **SV-CML-FR-089:** The system shall implement the Art. 342-A
  revocación de disolución: the EXTRAORDINARY general meeting of a
  sociedad in liquidación may revoke a previously adopted dissolution
  agreement when the invoked causal has DISAPPEARED or been CURED and
  the liquidation period (or any prórroga) has NOT concluded — the
  revocation recorded with its causal-cure evidence; once the revocation
  agreement is INSCRIBED, the society returns to NORMALIZED state and
  may initiate NEW operations (the FR-085 no-new-ops guard lifts only at
  this inscription), the liquidators CEASE and return all goods, books
  and documents per the Art. 331 manner (return-inventory record); and
  the revocation route is UNAVAILABLE for forced dissolution and
  liquidation unless the competent judge authorizes it at an interested
  party's request (forced/nature flag on the dissolution record gates
  the action).
  (LB-021; EVID-221)
- **SV-CML-FR-090:** The system shall record the Art. 620 EIRL
  liquidation touchpoint (profile owned by `07_empresa-mercantil-eirl.md`
  when it lands — consumed there by id): the EIRL's voluntary or forced
  liquidation applies this Code's sociedad-de-personas liquidation rules
  AS APPLICABLE (this file's §§3.4 mechanics referenced by the EIRL
  profile), and the VOLUNTARY liquidation is SUBJECT TO verification of
  the state of solvency or tax authorization PER THE CÓDIGO TRIBUTARIO —
  recorded as an EXTERNAL gate (solvencia checkpoint on the EIRL
  liquidation record; the CT mechanics are not evidenced in this corpus,
  OQ-003 — no CT rule derived here); the forced-liquidation judicial
  reports, preventive annotation, "en liquidación" name phrase and final
  inscription-cancellation of constitutive records follow Art. 620's own
  text (summarized in LB-030; file 07 owns the detail).
  (LB-030; EVID-224)

### 3.5 Null and irregular societies (Arts. 343-357)

- **SV-CML-FR-091:** The system shall implement the Art. 343-345/349-350
  nullity machinery: a sociedad with ILLICIT OBJECT is NULL — its deed
  inscribable-never (inscription blocked at the registry surface) and,
  if in fact inscribed, declarable null WITH RETROACTIVE EFFECT despite
  Art. 25 (the one statutory override of SV-CML-FR-048's
  no-retroactivity protection — flagged on the record); illicit CAUSA is
  equally null (cause unexpressed presumed lawful); lack of consent of
  the MAJORITY invalidates the social contract (minority/single-socio
  consent lack rides Art. 26-2, outside this article set); consequences
  recorded as state + exposure: nullity action of any interested person
  or the Ministerio Público, de-oficio declaration, dissolution and
  liquidation, judge-practiced or designated liquidation (vigilance
  office heard; designation preferably a banking institution), proceeds
  to civil liability and REMANENT TO PUBLIC CHARITY (devolución +
  indemnification for the consent case); and a legally-organized society
  EXECUTING ILLICIT ACTS — or engaging WITHOUT due authorization in
  activities requiring it (banking, general-deposit warehouses, savings
  and similar) — is dissolved and liquidated immediately under the same
  distribution (vigilance-office report per Arts. 351-352 noted as
  external machinery).
  (LB-022; LB-024; EVID-222)
- **SV-CML-FR-092:** The system shall compute the Art. 346-347/356
  regularization windows: a sociedad ABSOLUTELY lacking formalities has
  no legal existence (acquiring it toward third parties per FR-093) and
  a DEFICIENT escritura (failing its class's requisites — the FR-046
  checklist consumed by id) cannot be INSCRIBED until corrected; before
  liquidation the judge sets a regularization term of NOT LESS THAN 90
  NOR MORE THAN 120 DAYS (window recorded with start/end and
  cured/expired state); the same 90-120-day judicial window is a
  PREREQUISITE to tramiting any dissolution suit — including the society
  that prolonged existence past its pacto dissolution term without
  prórroga or failed to cure any other dissolution causal (Art. 356,
  which keeps it functioning REGULARLY until the dissolving escritura or
  dissolution action); expiry uncured → the liquidation state of §3.4
  opens (FR-083 machinery by id), with the charitable-remanent
  dispositions of Arts. 346-347 recorded (no aportant receives more than
  contributed; aportación-default remanent to charity).
  (LB-023; LB-026; EVID-222)
- **SV-CML-FR-093:** The system shall record the Art. 348/355
  exteriorized-society liability: societies of Arts. 343-347
  EXTERIORIZED before third parties have legal personality ONLY insofar
  as it PREJUDICES them, never for their benefit (asymmetry flag on the
  record); the socios, administrators and EVERY person intervening in
  their functioning answer the society's obligations to third parties
  PERSONALLY, SOLIDARILY and UNLIMITEDLY (penal liability preserved);
  representatives/attorneys performing juridical acts of these societies
  answer SOLIDARILY for compliance, and ALL socios and managers are
  solidarily responsible EVEN WITHOUT intervening in the particular act;
  damages are demandable by any interested party — including NON-CULPABLE
  socios — against the culpable and the representatives/attorneys
  (exposure metadata; the internal relations follow the pacto or the
  Code's class defaults); this machinery is what SV-CML-FR-062's
  Registro-de-Socios irregularity flag and every suffix-omission defect
  of FR-073 resolve into (flag consumed by id; this file owns the
  machinery per 04's forward pointer).
  (LB-024; LB-026; EVID-222)
- **SV-CML-FR-094:** The system shall compute the Art. 353 registration
  discipline clocks: the escritura social or its REFORMS must be
  presented for inscription within FIFTEEN DAYS of execution — the clock
  runs on every escritura record (FR-045 consumed by id), lapse exposes
  the duty that ANY socio may enforce judicially or administratively;
  and the regular-existence check: a judicial requirement (personally
  notified AND published) to prove regular existence starts a FOUR-MONTH
  clock — expiry without the inscription proved puts the sociedad into
  LIQUIDATION (§3.4 machinery by id); the Notary's warning duty and the
  Registry's monthly inscriptions lists to the state-vigilance office
  are recorded as external-machinery notes (no computation), and the
  matrícula-side consequence rides SV-CML-FR-012 case g (sociedad nula o
  irregular) by id.
  (LB-025; EVID-222)
- **SV-CML-FR-095:** The system shall implement the Art. 354
  out-of-object reform duty: a sociedad performing LAWFUL acts OUTSIDE
  its social object MUST REFORM the object to comprise the new
  activities — an out-of-object operation detection surfaces the reform
  duty (object-scope check against the empresa finalidad per
  SV-CML-FR-046's escritura field, warning-grade: object scope is legal
  judgment, the system surfaces divergence); any interested party has
  action to demand the reform; the judge sets a FOUR-MONTH term;
  expiry unfulfilled → LIQUIDATION per the preceding article (§3.4
  machinery by id; liquidation practiced per pacto/Code per Art. 353
  final inciso).
  (LB-026; EVID-222)
- **SV-CML-FR-096:** The system shall compute the Art. 357 single-socio
  collapse: when a sociedad is reduced to ONE socio, a THREE-MONTH clock
  runs for the traspaso of some participación to another person —
  expiry without traspaso ends the SOCIEDAD as such, the empresa
  mercantil SUBSISTING as an EMPRESA INDIVIDUAL of the sole socio; the
  surviving enterprise's liability is inherited — UNLIMITED if the
  source society had at least one unlimited-liability socio, LIMITED if
  all source socios were limited (composition check at collapse); and a
  further TWO-MONTH clock runs from the first term's expiry for the
  sole socio to grant the conversion instruments — expiry unfulfilled
  renders the enterprise an IRREGULAR SOCIETY under Art. 347 (FR-092
  machinery by id); the conversion-to-empresa-individual transition
  itself is `07_empresa-mercantil-eirl.md` / EIRL-profile territory for
  the limited-liability case (pointer only; the Art. 600 default of
  unlimited individual liability governs otherwise).
  (LB-027; EVID-222)

### 3.6 Foreign societies (Arts. 358-361)

- **SV-CML-FR-097:** The system shall implement the Art. 358-361
  foreign-society registration package: foreign societies performing
  acts of commerce in El Salvador — fixing DOMICILE or establishing
  SUCURSALES — register in the Registro de Comercio by solicitud of the
  legal representative or general/special attorney, carrying: (a)
  STATUTES proving lawful constitution under the organizing country's
  laws; (b) proof the domicile/operation decision was validly adopted
  per those statutes; (c) the representative's PODER with faculties
  stated broadly, clearly and precisely, the appointed representative
  RESIDING PERMANENTLY in the country (residency flag on the
  representative partner record; poder registered per SV-CML-FR-014 by
  id); (d) SUFFICIENT social capital with its entry PROVED by the
  MINEC foreign-investment registry (proof-reference slot — the registry
  interface is not in corpus, OQ-004); (e) a certified BALANCE INICIAL
  by an in-country Contador Público autorizado reflecting the capital
  social; plus the PROTEST of submission to Salvadoran laws, courts and
  authorities (attestation flag on the application); on satisfaction
  the Registrar registers the sociedad or sucursal AND the poder,
  issuing the registro único de empresa (matrícula machinery consumed
  from SV-CML-FR-008 by id); a SUCURSAL is domiciled, for all legal
  effects, where its PRINCIPAL OFFICE sits (domicile rule on the
  sucursal record); every capital increase/decrease — and cancellation —
  inscribes FIRST in the MINEC Registro de la Inversión Extranjera and
  AFTERWARDS in the Registro de Comercio, both noticing the
  state-vigilance office (ordering gate on capital-change registry
  entries of foreign societies); and the vigilance office's watch over
  strictly mercantile obligations is recorded as external machinery
  (Art. 361).
  (LB-028; LB-029; EVID-222)

### 3.7 Quiebra scope note (Arts. 498-552) — SOQ-24, no FRs

The Code's quiebra/suspensión-de-pagos block (Arts. 498-552) is a
classic 1970 insolvency regime whose supersession by modern
insolvency/concursos legislation is UNVERIFIED (SOQ-24, master index;
07_ OQ-3). This file therefore cites quiebra TERMINOLOGY ONLY: (i) the
matrícula cancellation case f) "judicial quiebra declaration"
(SV-CML-FR-012, consumed by id, already carries the same
terminology-only watch); (ii) the EIRL forced-liquidation trigger "por
quiebra" (Art. 619 — file 07 territory). NO quiebra mechanics,
procedural clocks, creditor ordering or discharge rules are derived
anywhere in this localization until the vintage check resolves
(acquisition candidate if insolvency FRs are ever needed). CT-side
solvency crossref: the EIRL voluntary-liquidation solvencia gate
(FR-090) is the only liquidation-solvency hook in this article set —
Código Tributario mechanics by pointer, OQ-003.
## 4. Data Model

Layer semantics: the lifecycle model is Odoo-native (res.company +
l10n_sv_commerce records) — wave default `odoo` (§5). The Registrador,
the Superintendencia de Competencia, the MINEC registry, the judge, the
Notary and the auditor are external authorities: the system tracks
their acts (inscriptions, checkpoints, certifications, oficios) as
referenced facts and emits lifecycle events for downstream consumers
(retention matrix, emitter-name pointer); it never emulates them.

**Lifecycle state (res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_lifecycle_state | computed state | active · en_liquidacion · liquidada (extinguished at liquidation-escritura inscription; FR-048 personality machinery by id) · normalized (post-revocation return) | FR-083, FR-089 |
| res.company | sv_cml_name_suffixes | computed | type suffix (04 profile) + "de C.V." (Art. 308) + "en liquidación" (Arts. 326/620) — composed name; DTE emitter-name flow = A11 pointer | FR-073, FR-083 |
| l10n_sv_commerce.liquidation | opened_on · term_deadline · prorrogas | date · date · one2many | term ≤ 2 years from appointment-authority fixing; prórroga records inscribed, cumulative cap = 2y (Art. 326) | FR-083 |
| l10n_sv_commerce.liquidation | forced_flag · revocacion_allowed | boolean · computed | forced dissolution blocks Art. 342-A revocation absent judge authorization | FR-089 |

**Capital variable (movements + withdrawal):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.capital.movement | book_ref (Art. 40-IV) · direction · amount · legal_ref | many2one (FR-057 book) · select · monetary · ref | aumento · disminucion; consultable-by-any-interested-person access profile (Art. 312) | FR-075 |
| res.company | sv_cml_capital_variable_min | monetary | floors per type (S.A./SRL/C.xA.: profile floor; colectiva/comandita simple: ≥ 1/5 initial capital — Art. 310); announcement guard pairs mínimo with any capital announcement | FR-074 |
| l10n_sv_commerce.withdrawal.notice | socio_ref · notice_kind · notified_on · effective_on | partner · select · date · computed | judicial · acta_notarial (Art. 313); effective = current-FY end (notice before last trimester) or next-FY end (after/in last trimester); blocked below mínimo (Art. 314) | FR-076 |

**Fusión / transformación:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.fusion | form · participating companies · successor_ref | select · many2many · many2one | nueva · absorcion (Arts. 315-316); successor acquires all rights/obligations; supersede-never-delete continuity | FR-077 |
| l10n_sv_commerce.fusion | agreement/inscription state · marginal_notes · publications | state · flags · one2many (FR-017 engine) | per-society inscription + marginal notes; publication of agreement + last balance; 90-day opposition clock from last D.O. publication | FR-077, FR-078 |
| l10n_sv_commerce.fusion | competencia_check · escritura_ref · executed_on | select · ref · date | not_subject_to_notification · sc_approved · notified_silent (Art. 319 a-c; Ley de Competencia values = OQ-002 config-gaps); personality retained until inscription | FR-079 |
| l10n_sv_commerce.transformacion | from_type · to_type · agreement_quorum · liability_survival | refs · refs · computed · flag | any→any incl. fijo↔variable (Art. 322); unlimited-liability survival tag on pre-agreement obligations (Art. 323-2) | FR-080 |
| l10n_sv_commerce.transformacion | auditor_valuo_ref · certified_on · vigilance_deadline | ref · date · computed date | personas→capital valúo + certification to vigilance office ≤ 3 días hábiles from making (Art. 323-3); valúo attached to escritura | FR-081 |
| l10n_sv_commerce.transformacion | escritura_ref · inscribed_on | ref · date | effects from inscription; previous-type norms until then; de-pleno-derecho succession (Arts. 324-325) | FR-082 |

**Liquidation records:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.liquidator | partner_ref · appointment_kind · inscribed_on · charge_limits | partner · select · date · text | socios_same_act · judicial_default · judge_15d_post_firme (Arts. 327-328); personal liability beyond limits; credenciales per FR-014 | FR-084 |
| l10n_sv_commerce.liquidation | delivery_inventory_ref | ref | detailed inventory of all goods/books/documents subscribed by both parties (Art. 331); return-inventory on revocation (Art. 342-A) | FR-084, FR-089 |
| l10n_sv_commerce.liquidation | liquidator_faculties_state · no_new_ops_guard | checklist · guard | Art. 332 I-VII checkpoints (fiscal obligations explicit); new-operations block while en liquidacion | FR-085 |
| l10n_sv_commerce.liquidation | final_balance_ref · approval_state · deposit_entry_ref · organ_publication | ref · state · ref (FR-035) · record | junta approval → Registro deposit → Órgano Oficial del Registro de Comercio publication (Art. 332 IV-V) | FR-085 |
| l10n_sv_commerce.partial.distribution | publications (FR-017) · execution_eligible_on | one2many · computed date | capital-reduction-form publication; executable only after 30-day window from third publication (Arts. 333-334 via Art. 30) | FR-086 |
| l10n_sv_commerce.liquidation.payment | accionista_ref · action_kind · route · bank_deposit_ref | partner · select · select · ref | nominative_last_registered (register cancelled) · gravamen_consignation · embargo_tribunal · bearer_against_title; unpayable sums bank-deposited ≤ 3 días hábiles from approval; 5-year unclaimed lapse noted (Arts. 337-338) | FR-086 |
| l10n_sv_commerce.liquidation | closing_escritura_ref · cancellations · dacion_en_pago_records | ref · one2many · one2many | escritura after payments/deposits (Art. 338-A); inscription cancels constitution/modification/estatutos inscriptions + authorizing-institution oficios (Art. 342); cessions/daciones pro-rata with liquidator tradition (Art. 340) | FR-087 |
| l10n_sv_commerce.papers.deposit | custodian_kind · designee_ref · deposited_on · deposit_until | select · ref · date · computed date | banking_institution · socios_majority_designee · judge_designated (default/judicial-liquidation cases); 10-year duration (Art. 340-3); feeds SV-CML-FR-028 row a + emits event consumed by SV-CML-FR-029 | FR-088 |
| l10n_sv_commerce.liquidation | eirl_solvencia_gate | checkpoint | Art. 620 voluntary-liquidation CT verification — external gate (OQ-003); EIRL detail owned by file 07 | FR-090 |

**Irregularity clocks:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.irregularity | cause · exposure_flags | select · flags | illicit_object · illicit_causa · majority_consent_lack · illicit_acts_dissolution · unauthorized_activity · formality_lack · deficient_escritura · out_of_object · single_socio_lapse · suffix/registry defects (Arts. 343-357); personal-solidary-unlimited exposure (Arts. 348/355); Art. 25 retroactivity override for illicit object | FR-091, FR-093 |
| l10n_sv_commerce.irregularity | regularization_window | date range | judge-set 90-120 días (Arts. 346/356); 4-month Art. 353 comprobación clock; 4-month Art. 354 objeto-reform clock; 15-day escritura-presentation clock (per escritura); cured/expired states | FR-092, FR-094, FR-095 |
| l10n_sv_commerce.single.socio | collapse_clock · conversion_clock · liability_inherited | date · date · computed | 3-month traspaso window; 2-month conversion-instruments window (Art. 357); unlimited if any unlimited socio, else limited; expiry → Art. 347 irregularity | FR-096 |

**Foreign societies:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.foreign.registration | statutes_ref · domicile_decision_ref · poder_ref · protest_flag | ref · ref · ref (FR-014) · flag | Art. 358 a-c + protest; representative residency = permanent (partner flag) | FR-097 |
| l10n_sv_commerce.foreign.registration | minec_proof_ref · balance_inicial_ref | ref · ref | MINEC foreign-investment-registry capital proof (d) + in-country-CPA certified balance inicial reflecting capital (e) — interface OQ-004 | FR-097 |
| res.company (sucursal) | sv_cml_sucursal_domicile_rule · minec_first_gate | computed · gate | domicile = principal office (Art. 360-1); capital changes/cancellation inscribe MINEC first, then Registro (ordering gate) | FR-097 |

## 5. Odoo Mapping

Layer semantics for this wave: the lifecycle model is Odoo-native
(res.company + l10n_sv_commerce records) — every FR maps `odoo`; none
touch DTE generation/transformation (an architecture-split surface
per `shared/docs/saas-thin-client-architecture.md`), so no `saas`
rows are introduced. E-invoicing kin (pointer only): the composed
company name (type suffix + "de C.V." + "en liquidación") maintained
here flows into DTE emitter-name data owned by the e-invoicing
onboarding/authorization cluster (A11; A8 kin) — consumed there by id,
never re-derived here. Model names are stable across Odoo 17/18/19/20;
no version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-072 | odoo | res.company + l10n_sv_commerce.society.type | sv_cml_capital_regime, cv flags | Variable-regime movement forms without Art. 30 formalities (FR-050 mechanics confined to fijo); S.A. balances/admin-liability/auditor flags via FR-070; nominative-absolute acciones (Art. 311) |
| FR-073 | odoo | res.company + society.type suffix_rule | composed name validator | "de capital variable"/"de C.V." after the type suffix (04 profile row — incl. S. en C. — consumed by id); defect → §3.5 exposure; DTE flow = A11 pointer |
| FR-074 | odoo | res.company + capital-change guard | sv_cml_capital_variable_min, announcement check | Type floors via 04 profiles (FR-059/065 by id); personas family ≥ 1/5 initial capital; capital announcement without mínimo flagged (Art. 310) |
| FR-075 | odoo | l10n_sv_commerce.capital.movement + book (FR-057) | movement rows | Art. 40-IV book existence gated in 04; movement entries + any-interested-person consultation here; discipline/retention via FR-025/FR-028 by id |
| FR-076 | odoo | l10n_sv_commerce.withdrawal.notice | notice_kind, effective_on | Judicial/acta-notarial validation; FY-end vs next-FY-end computation (last-trimester working reading); below-mínimo separation block (Art. 314) |
| FR-077 | odoo | l10n_sv_commerce.fusion + registry.entry (FR-013) + publication (FR-017) | form, inscriptions, marginal notes | Universal-succession continuity (supersede, never delete); per-society agreement quorum via type profile; agreement + last balance published (486 default) |
| FR-078 | odoo | l10n_sv_commerce.fusion | opposition window | 90-day clock via FR-017 engine; opposition/guarantee = exposure flags (judicial assessment external); socio retiro inside window with liability survival |
| FR-079 | odoo | l10n_sv_commerce.fusion + registry.entry | competencia_check, escritura_matriz | Checkpoint states a/b/c (Ley de Competencia values = OQ-002 config-gaps, registry-side verification); personality retained until inscription / extinguished at it (FR-048 kin; anchor FR-016) |
| FR-080 | odoo | l10n_sv_commerce.transformacion | from/to type, liability_survival | Any→any + fijo↔variable; pacto-modification quorum via type profile; unlimited-liability survival tag on pre-agreement operations |
| FR-081 | odoo | l10n_sv_commerce.transformacion | valúo certification checkpoint | 3-días-hábiles clock to vigilance office (fiscal calendar engine); same requisito for personas-natures fusión execution; valúo referenced in escritura |
| FR-082 | odoo | l10n_sv_commerce.transformacion + escritura (FR-045/046) | inscription date, succession | Old-type norms until inscription; de-pleno-derecho succession = record continuity, never fork |
| FR-083 | odoo | res.company + l10n_sv_commerce.liquidation | lifecycle_state, term/prórrogas | "en liquidación" suffix (DTE flow = A11 pointer); 2-year cap with inscribed prórrogas; matrícula consequence via FR-012 d/f by id |
| FR-084 | odoo | l10n_sv_commerce.liquidator + liquidation | appointment/transition/inventory | Appointment kinds (socios-same-act / judicial / 15-day post-firme); administrators hold until inscribed entry into function; delivery inventory signed both parties; credenciales via FR-014 |
| FR-085 | odoo | l10n_sv_commerce.liquidation + guard on sales/purchase flows | faculties checklist, no_new_ops | Fiscal obligations explicit in faculty II (tax computation = taxation wave by id); final balance → Registro deposit (FR-035 by id) → registry-organ publication (own channel, not 486); new-operations block "terminantemente prohibido" |
| FR-086 | odoo | l10n_sv_commerce.partial.distribution + liquidation.payment | windows, payment routes | Partial-distribution 30-day wait via Art. 30/486 (FR-017 engine); personas 8-día-hábil lot window; capitales 15-day claims from last publication; nominative last-registered payment + register cancellation; 3-días-hábiles bank deposits; 5-year unclaimed lapse |
| FR-087 | odoo | l10n_sv_commerce.liquidation | closing escritura, cancellations, daciones | Post-payment escritura (338-A); inscription cancels constitutive entries + authorizing-institution oficios tracked; cessions/daciones pro-rata with liquidator tradition; cession extract once in two national dailies (own form) |
| FR-088 | odoo | l10n_sv_commerce.papers.deposit | custodian, 10-year clock | Feeds SV-CML-FR-028 row a by id (never restated); emits lifecycle event consumed by SV-CML-FR-029; gravamen-cancellation workflow surface (15-day opposition) |
| FR-089 | odoo | res.company + liquidation | revocación record, normalized state | Extraordinary-junta revocation within period/prórrogas; causal-cure evidence; no-new-ops guard lifts at inscription; return inventory per Art. 331 manner; forced-dissolution judge-authorization gate |
| FR-090 | odoo | l10n_sv_commerce.liquidation (EIRL) | solvencia_gate checkpoint | Art. 620: personas-rules-as-applicable pointer + CT solvencia external gate (OQ-003); EIRL profile = file 07 (by id when it lands) |
| FR-091 | odoo | l10n_sv_commerce.irregularity | nullity causes, retroactivity override | Illicit object/causa/majority-consent + illicit-acts/unauthorized-activity dissolution; Art. 25 retroactivity override flagged against FR-048; charity-remanent destinations recorded |
| FR-092 | odoo | l10n_sv_commerce.irregularity | regularization windows | Judge-set 90-120d windows (Arts. 346/356); deficient escritura uninscribable until cured (FR-046 checklist by id); expiry → §3.4 liquidation machinery by id |
| FR-093 | odoo | l10n_sv_commerce.irregularity | liability exposures | Personality-as-prejudice asymmetry; personal-solidary-unlimited of socios/administrators/participants; representatives' solidarity; non-culpable-socio damages action; consumes FR-062 flag + FR-073 defects |
| FR-094 | odoo | l10n_sv_commerce.escritura + irregularity | 15-day presentation clock, 4-month check | Clock on every escritura/reform (FR-045 by id); requirement (personal + published) starts 4-month comprobación → liquidation; FR-012 case g by id; notary/registry duties = external notes |
| FR-095 | odoo | l10n_sv_commerce.irregularity | objeto-reform duty | Out-of-object detection = warning-grade (finalidad scope is legal judgment; divergence surfaced); 4-month judge window → liquidation by id |
| FR-096 | odoo | l10n_sv_commerce.single.socio | 3-month/2-month clocks | Traspaso window → sociedad ends, empresa individual survives with inherited liability composition; conversion-instruments window → Art. 347 irregularity; EIRL/Art. 600 side = file 07 pointer |
| FR-097 | odoo | l10n_sv_commerce.foreign.registration + res.company | package checklist, MINEC-first gate | Art. 358 a-e + protest; registro único via FR-008 by id; sucursal domicile = principal office; capital changes MINEC→Registro ordering gate; MINEC interface = OQ-004 |

Version-regime notes (D12): no dated monetary thresholds live in this
file (Art. 310's floors are profile-driven or fractional code text); the
period values (90/120 days, 15 days, 4 months, 2 years, 3 días hábiles,
10 years, 5 years) are un-reformed statutory text under the SOQ-22
residual watch — stored as code constants with provenance, and the
Ley de Competencia (OQ-002) and CT-solvency (OQ-003) instruments remain
config-gaps pending acquisition.
## 6. Acceptance Criteria

- **AC-001:** Given an SRL de capital variable named without "de C.V."
  and another with "SRL de C.V. Ltda.", when the FR-073 validator runs,
  then the first is flagged with the naming defect + §3.5
  irregularity-exposure note and the second passes; given the composed
  name record, then the type-suffix profile (incl. S. en C. rows) is
  consumed from 04's profile table by id, never restated (FR-073).
- **AC-002:** Given an announcement stating "capital social US$500,000"
  with authorized increases and no capital mínimo, when the FR-074 guard
  runs, then the announcement is flagged prohibited with the Art. 310
  unlimited-solidary exposure note; given a colectiva de C.V. with
  initial capital US$100,000, then the minimum floor computes at
  US$20,000 (1/5) (FR-074).
- **AC-003:** Given a withdrawal notice by acta notarial filed on
  10-Sep-2026 (before the last trimester) and another on 15-Nov-2026
  (within the last trimester, per the working reading), when FR-076
  computes, then the first takes effect 31-Dec-2026 and the second
  31-Dec-2027; given the retiro would take capital below the FR-074
  minimum, then the separation is blocked with the Art. 314 reason
  (FR-076).
- **AC-004:** Given a capital decrease of US$5,000 in a capital-variable
  sociedad, when recorded, then an entry lands in the Art. 40-IV book
  (FR-075) and is consultable under the any-interested-person access
  profile; given a socio without legítimo interés, then access is still
  grantable — the statute's gate is "interés", recorded not adjudicated
  (FR-075).
- **AC-005:** Given a fusión by absorción whose Art. 317 publications
  complete (last D.O. publication) on 01-Mar, when the FR-078 clock
  computes, then execution is eligible from 31-May (clock from 02-Mar,
  the day after the 01-Mar last publication, + 90 days) absent
  opposition; given an opposition filed 15-Mar, then
  execution suspends pending guarantee and the record shows the
  suspension state (FR-078).
- **AC-006:** Given a fusión whose escritura-matriz testimonio is
  presented but NOT yet inscribed, when the personality states are
  evaluated, then all merging societies retain active personality
  (Art. 319/25 kin via FR-048); upon recording the inscription with
  competencia_check = sc_approved, then the merged societies' records
  turn extinguished and the successor acquires rights/obligations by
  supersede-continuity (FR-079, FR-077).
- **AC-007:** Given a colectiva transforming to S.A., when the FR-081
  gate runs, then the record requires an auditor valúo certification
  with a 3-días-hábiles vigilance-office deadline from its making and
  blocks the escritura record until the valúo is attached; the
  unlimited-liability survival tag persists on all pre-agreement
  obligations (FR-081, FR-080).
- **AC-008:** Given a sociedad dissolved 01-Feb-2027 with a liquidation
  term fixed at 18 months, when a prórroga of 9 months is requested,
  then it is capped so term + prórroga ≤ 2 years from the term fixing
  (the prórroga inscribes; a 6-month prórroga is accepted, a 9-month one
  rejected with the Art. 326 reason); the company name renders with "en
  liquidación" appended (FR-083).
- **AC-009:** Given a sociedad en liquidación where a user attempts a
  new sales contract, when the FR-085 guard runs, then the operation is
  blocked with the Art. 332 "terminantemente prohibido" reason; given
  the final balance approved by junta, then the Registro deposit record
  (FR-035 mechanics by id) and the registry-organ publication channel
  open as faculty-V checkpoints (FR-085).
- **AC-010:** Given a partial distribution agreed 01-Apr with third
  publication 10-Apr, when FR-086 computes, then the distribution is
  executable from 11-May (30 days after the third publication,
  Art. 334 via Art. 30); given an accionista payment unpayable at the
  approving junta, then a bank-deposit record with a 3-días-hábiles
  deadline from balance approval is created (FR-086).
- **AC-011:** Given the closing of a liquidation (payments/deposits
  made, escritura inscribed), when FR-087/FR-088 run, then the
  constitution/modification/estatutos inscription cancellations are
  recorded, a papers-deposit record opens (bank or majority designee,
  judicial-liquidation → judge-designated) with a 10-year clock, and the
  liquidation-closing event is emitted for SV-CML-FR-029's row-a
  post-liquidation extension — the matrix itself never restated
  (FR-087, FR-088).
- **AC-012:** Given a sociedad en liquidación whose junta general
  extraordinaria revokes the dissolution (causal cured, prórroga
  unexpired) on 01-Jun and the revocation inscribes 05-Jun, when the
  state evaluates, then the society turns normalized, new operations
  unblock on 05-Jun (not 01-Jun), and a liquidators' return-inventory
  record per Art. 331 manner opens; given a FORCED dissolution, then
  the revocation action is unavailable absent judge authorization
  (FR-089).
- **AC-013:** Given a sociedad reduced to a single socio on 01-Jan,
  when FR-096 computes, then the traspaso window closes 01-Apr and the
  conversion-instruments window 01-Jun; given no traspaso by 01-Apr,
  then the record converts to empresa-individual survival with the
  inherited liability composition (unlimited if any unlimited socio),
  and expiry of the conversion window on 01-Jun flags Art. 347
  irregularity (FR-096).
- **AC-014:** Given an escritura de reforma granted 01-Mar and not
  presented, when FR-094 computes, then the 15-day presentation deadline
  is 16-Mar with the any-socio enforcement note; given a published
  regular-existence requirement served 01-Mar, then the 4-month
  comprobación clock closes 01-Jul, upon which unproved inscription
  opens the liquidation state (FR-094).
- **AC-015:** Given a foreign sociedad registering with statutes,
  domicile decision, poder (representative flagged permanent-resident),
  MINEC capital proof reference and certified balance inicial, but no
  protest of submission, when the FR-097 checklist runs, then the
  application is incomplete with the Art. 358 protest item identified;
  given a later capital increase recorded straight to Registro de
  Comercio, then the MINEC-first ordering gate flags the sequence error
  (FR-097).
- **AC-016:** Given an EIRL voluntary-liquidation record, when the
  FR-090 gate evaluates, then the CT solvencia/tributary-authorization
  checkpoint shows as an external gate (no CT mechanics computed) with
  the OQ-003 pointer, and the persona-rules-as-applicable reference
  points at this file's §3.4 mechanics for file 07's consumption
  (FR-090).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-24 carried: the quiebra block (Arts. 498-552) is a classic 1970 regime — whether modern insolvency/concursos legislation derogated or subsidiarized it is unverified (corpus silent). This file therefore cites quiebra terminology only (§3.7: matrícula cancellation case f via SV-CML-FR-012; EIRL Art. 619 trigger = file 07 pointer); NO insolvency mechanics derive anywhere until the vintage check resolves (acquisition candidate if insolvency FRs are ever needed). | no | Takumi S5 (sources watch) | open |
| OQ-002 | The Ley de Competencia is NOT in the corpus: Art. 319's inscription checkpoint turns on its notification thresholds, the Superintendencia de Competencia's approval and its "plazo estipulado" — none evidenced. FR-079 records the three checkpoint alternatives as registry-side states with NO values; if ever automated (e.g. a pre-execution warning), acquire the law (SOQ-25 kin: acquisition candidate, sources-registry numbering ≥74). | no | Takumi S5 (sources watch) | open |
| OQ-003 | Art. 620 subjects EIRL VOLUNTARY liquidation to "verificación del estado de solvencia o autorización tributaria, de conformidad con lo establecido en el Código Tributario" — but the CT corpus extraction (05_) evidences no solvencia article, so the verifying office, form and lapse are unknown. FR-090 ships an external gate with no computation; when the CT article is pinned (or file 07 lands), wire the gate to the taxation wave's solvencia surface by id — never hardcode. | no | Takumi S5 + taxation wave | open |
| OQ-004 | The MINEC Registro de Inversión Extranjera operational interface (application forms, capital-proof format, inscription turnaround) is not in the corpus. FR-097 records the Art. 358-d proof as a reference slot and the Art. 360 MINEC-first ordering as a sequence gate; acquire the registry's regulations if document-level automation is ever needed. | no | Takumi S5 (sources watch) | open |

