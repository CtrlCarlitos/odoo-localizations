# SV — Commercial-legal — Merchant registration: comerciante status, matrícula de empresa and the Registro de Comercio

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador merchant-registration chassis every other
commercial-legal requirement builds on: the Código de Comercio (Commercial
Code, CC) *comerciante* (merchant) status model of Arts. 1-7 — the
individual/social dichotomy of Art. 2, the presumption of commerce exercise
by publicity or open establishment, the Art. 7 capacity gates and the
Art. 15/Art. 20 Libro Segundo exemption profiles; the four professional
obligations of Art. 411 as the chapter map; the *matrícula de empresa*
(enterprise registration) family of Arts. 412-422 — the permanent
*registro único* (single enterprise register), registration of every
*local/agencia/sucursal* (premises/agency/branch), the constancia as sole
proof of merchant status, annual renewal, the closure sanction with its
30-*días hábiles* (business days) grace and the denial/cancellation
catalogs; and the *Registro de Comercio* (Commerce Registry) architecture
of Arts. 456-487 under the *Centro Nacional de Registros* (CNR, National
Registry Center) — its three registries and their particular registers, the
*poderes/nombramientos/credenciales* (powers of attorney/appointments/
credentials) registration surface, the matrícula-precondition gate of
Art. 469, registry publicity/presumption and presentation-time effects, and
the Art. 486 publication rule.

It does **not** cover: the bookkeeping, legalization, no-alteration and
retention regime (`02_accounting-books.md`); the annual financial
statements and balance deposit (`03_financial-statements.md`); society
types, formation, capital and reserves (`04_society-types.md`); society
lifecycle — capital variable, fusión, transformación, liquidación,
nullity, extranjeras (`05_society-lifecycle.md`); commercial agents and
authority defaults (`06_commercial-agents.md`); the empresa mercantil
transfer package and EIRL (`07_empresa-mercantil-eirl.md`, which owns the
Art. 417 transfer mechanics); payment instruments (`08_payment-instruments.md`);
sales contracts (`09_sales-contracts.md`); or AML compliance
(`10_aml-compliance.md`). Those files consume this one for merchant
status, matrícula state and the registry-entry model by FR id.

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
(EVID-211/212/217) and, where the evidence abbreviates, from the
extraction txt `sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable per
standing ruling; page pointers = txt PAGE markers). Currency discipline
(SOQ-29): no colones-denominated values occur in this file's article set;
the twelve-thousand-dollar threshold (Arts. 15) is 2008-reformed USD code
text — dated-but-current under the SOQ-22 residual watch.

Consumer note (29_, EVID-172, pointer only — no re-derivation): the CNR's
F985/F-975 semi-annual report is the registry's OWN third-party filing to
DGII under CT Art. 121 a)2 (society/comerciante constitution,
transformation, fusión, dissolution, liquidation and matrícula events) —
NOT a taxpayer obligation; no FR is derived from it in this file.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 2: "Son comerciantes: I.- Las personas naturales titulares de una empresa mercantil, que se llaman comerciantes individuales. II.- Las sociedades, que se llaman comerciantes sociales." "Se presumirá legalmente que se ejerce el comercio cuando se haga publicidad al respecto o cuando se abra un establecimiento mercantil donde se atienda al público." "Los extranjeros y las sociedades constituidas con arreglo a las leyes extranjeras, podrán ejercer el comercio en El Salvador con sujeción a las disposiciones de este Código y demás leyes de la República." | Merchants are: I. natural persons holding an empresa mercantil (commercial enterprise), called individual merchants; II. sociedades (companies), called social merchants. It is legally presumed that commerce is exercised when publicity is made to that effect or when a commercial establishment is opened where the public is attended. Foreigners and companies formed under foreign laws may engage in commerce in El Salvador subject to this Code and the other laws of the Republic | `sv/sources/07_Codigo_Comercio.pdf` | Art. 2 p.1 (EVID-211; foreigners inciso txt PAGE 2) |
| LB-002 | Código de Comercio, Art. 7: "Son capaces para ejercer el comercio: I.- Las personas naturales que, según el Código Civil son capaces para obligarse. II.- Los menores que teniendo dieciocho años cumplidos hayan sido habilitados de edad. III.- Los mayores de dieciocho años que obtengan autorización de sus representantes legales para comerciar, la cual deberá constar en escritura pública. IV.- Los mayores de dieciocho años que obtengan autorización judicial." "Estas autorizaciones son irrevocables y deben ser inscritas en el Registro de Comercio." | Capable of engaging in commerce: I. natural persons civilly capable of binding themselves; II. minors who, having turned eighteen, have been granted habilitación de edad (age emancipation); III. persons over eighteen holding their legal representatives' authorization to trade, which must be recorded in a public deed; IV. persons over eighteen holding judicial authorization. These authorizations are irrevocable and must be registered in the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 7 p.3 (EVID-211 zone; txt PAGE 3) |
| LB-003 | Código de Comercio, Art. 20: "No obstante su calidad de mercantiles, las sociedades que se constituyan como colectivas o comanditarias simples, de capital fijo, y que tienen exclusivamente una o más de las finalidades que se indican a continuación, una vez inscritas quedarán exentas de las obligaciones profesionales de los comerciantes contempladas en el Libro Segundo de este Código, excepto las mencionadas en los números I y IV del Art. 411 de este mismo Código." "Las finalidades a que se refiere el inciso anterior son: I. El ejercicio de la agricultura y ganadería. II. La construcción y arriendo de viviendas urbanas, siempre que no se construya con ánimo de vender en forma regular y constante las edificaciones. III. El ejercicio de las profesiones liberales." | Notwithstanding their mercantile character, colectivas and comanditarias simples of fixed capital pursuing exclusively one or more of these purposes are, once registered, exempt from the professional obligations of merchants in Book Two of this Code, EXCEPT those in numbers I and IV of Art. 411 (matrícula and fair competition). The purposes are: I. agriculture and livestock; II. construction and rental of urban housing (provided there is no intent to sell the buildings regularly and constantly); III. the practice of the liberal professions | `sv/sources/07_Codigo_Comercio.pdf` | Art. 20 p.6 (EVID-211/216; txt PAGE 7) |
| LB-004 | Código de Comercio, Art. 15: "No están sujetos al cumplimiento de las obligaciones profesionales contenidas en el Libro Segundo que este Código impone, los comerciantes e industriales individuales en pequeño cuyo activo sea inferior a doce mil dólares de los Estados Unidos de América. Cumplirán únicamente con la contenida en el romano IV del Art. 411 de este mismo Código." | Small individual merchants and industrialists whose assets are below twelve thousand US dollars are not subject to the professional obligations of Book Two; they need only comply with Art. 411 IV (fair competition) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 15 p.4 (EVID-211/216 zone; txt PAGE 4) |
| LB-005 | Código de Comercio, Art. 411: "Son obligaciones del comerciante individual y social: I. Matricular su empresa mercantil y registrar sus respectivos locales, agencias o sucursales. II. Llevar la contabilidad y la correspondencia en la forma prescrita por este Código. III. Depositar anualmente en el Registro de Comercio el balance general de su empresa, los estados de resultados y de cambio en el patrimonio correspondientes al mismo ejercicio del balance general, acompañados del dictamen del Auditor y sus respectivos anexos; y cumplir con los demás requisitos de publicidad mercantil que la ley establece. IV. Realizar su actividad dentro de los limites de la libre competencia establecidos en la Ley, los usos mercantiles y las buenas costumbres, absteniéndose de toda competencia desleal." | The obligations of individual and social merchants are: I. register (matricular) their empresa mercantil and register its locales, agencies or branches; II. keep accounting and correspondence in the form prescribed by this Code; III. deposit annually in the Commerce Registry the balance general, the resultados and patrimonio-change statements of the same fiscal year, with the Auditor's dictamen (opinion) and annexes, and comply with the other statutory publicity requirements; IV. conduct activity within the limits of free competition set by law, mercantile usage and good customs, abstaining from all unfair competition | `sv/sources/07_Codigo_Comercio.pdf` | Art. 411 p.79 (EVID-211; txt PAGE 79) |
| LB-006 | Código de Comercio, Art. 412: "La Matrícula de Comercio que regula el presente Código es la de empresa, que será de carácter permanente, estará a cargo del Registro de Comercio y se llevará en registros especiales en cualquier forma que la técnica indique. La matrícula de empresa mercantil constituirá el registro único de empresa." | The Matrícula de Comercio regulated by this Code is the enterprise matrícula, permanent in character, in the charge of the Commerce Registry, kept in special registers in whatever form technique indicates. The enterprise matrícula constitutes the single enterprise register (registro único de empresa) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 412 p.80 (EVID-212; txt PAGE 80) |
| LB-007 | Código de Comercio, Art. 414: "El comerciante, aunque ejerza distintas actividades mercantiles, podrá desarrollarlas bajo una sola empresa; pero si la empresa tuviere varios locales, agencias o sucursales, deberá registrar cada uno de ellos en el Registro de Comercio." | A merchant, even if exercising distinct mercantile activities, may develop them under a single empresa; but if the empresa has several locales, agencies or branches, each of them must be registered in the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 414 p.80 (EVID-212; txt PAGE 80) |
| LB-008 | Código de Comercio, Art. 415: "El comerciante individual deberá matricular su empresa mercantil mediante solicitud que presentará al Registro de Comercio, con la información y demás requisitos que señale la Ley de Registro de Comercio y su respectivo Reglamento." "La empresa mercantil de todo comerciante social se matriculará inmediatamente después de quedar inscrita su escritura de constitución en el Registro de Comercio, para lo cual deberá presentar a dicho Registro, conjuntamente con el pacto social constitutivo, la solicitud correspondiente de conformidad a lo señalado en el inciso anterior." | The individual merchant must matriculate his empresa by solicitud (application) filed with the Commerce Registry, with the information and other requirements set by the Ley de Registro de Comercio and its Reglamento. The empresa of every social merchant is matriculated immediately after its constitutive deed is registered, filing with the Registry, together with the constitutive pacto social, the corresponding application | `sv/sources/07_Codigo_Comercio.pdf` | Art. 415 p.80 (EVID-212; txt PAGE 80) |
| LB-009 | Código de Comercio, Art. 416: "Cumplidos los requisitos respectivos, el Registrador de Comercio ordenará que se asiente la matricula y extenderá constancia a su titular, para los efectos legales pertinentes. Un extracto del asiento de cada matrícula se publicará en el órgano oficial del Registro de Comercio, para el solo efecto de información." | Once the requirements are met, the Registrar of Commerce orders the matrícula entered and extends the constancia (certificate) to its holder for the pertinent legal effects. An extract of each matrícula entry is published in the Registry's official organ, for information purposes only | `sv/sources/07_Codigo_Comercio.pdf` | Art. 416 p.80 (EVID-212; txt PAGE 80) |
| LB-010 | Código de Comercio, Art. 418: "La constancia que de la matrícula extienda el Registrador, será la única prueba: a) para establecer su calidad de comerciante; y, b) para comprobar la propiedad de la empresa." "Cualquier autoridad judicial o administrativa puede, de oficio o a petición de parte, solicitar al Registrador de Comercio que extienda constancia del asiento de las matriculas de empresa." | The constancia of the matrícula extended by the Registrar is the sole proof: a) to establish merchant status; and b) to prove ownership of the empresa. Any judicial or administrative authority may, ex officio or at a party's request, ask the Registrar to extend a constancia of the enterprise matrícula entry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 418 p.81 (EVID-212; txt PAGE 81) |
| LB-011 | Código de Comercio, Art. 419 (first two incisos; inciso 3 omitted — Registrador→Juez de Paz oficio mechanics): "Ninguna empresa mercantil podrá funcionar sin tener su respectiva matrícula vigente." "A petición del Registrador de Comercio, los locales, agencias o sucursales de la empresa no matriculada serán cerrados temporalmente por el Juez de Paz del lugar, previa audiencia oral conferida al titular de la empresa, mientras éste no obtenga o renueve la matrícula correspondiente. Antes del cierre de los locales, agencias o sucursales, se concederá un plazo máximo de treinta días hábiles para que su titular obtenga o renueve la matrícula correspondiente." | No empresa may operate without its vigente (valid/current) matrícula. At the Registrar's request, the locales, agencies or branches of an unmatriculated empresa are temporarily closed by the local Juez de Paz (Justice of the Peace) after an oral hearing with the holder, until the matrícula is obtained or renewed. Before closure, a maximum period of thirty días hábiles is granted for the holder to obtain or renew the matrícula | `sv/sources/07_Codigo_Comercio.pdf` | Art. 419 p.81 (EVID-212; txt PAGE 81) |
| LB-012 | Código de Comercio, Art. 420: "Las matrículas deberán renovarse anualmente, en la época que se señale en la Ley de Registro de Comercio. La solicitud de renovación servirá para actualizar la información que señale el Reglamento de la Ley de Registro de Comercio, respecto de su titular, de la empresa y de sus locales, agencias o sucursales." "La falta de renovación de la matricula dentro del plazo legal correspondiente, será sancionada por el Registro de Comercio de conformidad a su ley." | Matrículas must be renewed ANNUALLY, at the epoch fixed in the Ley de Registro de Comercio; the renewal application updates the information on holder, empresa and locales/agencias/sucursales set by that law's Reglamento. Non-renewal within the legal deadline is sanctioned by the Registry per its law | `sv/sources/07_Codigo_Comercio.pdf` | Art. 420 p.81 (EVID-212; txt PAGE 81) |
| LB-013 | Código de Comercio, Art. 421: "El Registrador de Comercio denegará la inscripción de una matricula o la inscripción de la transferencia de la misma, en los casos siguientes: a) Si su titular fuere una persona incapaz o inhábil para ejercer el comercio. b) Tratándose de sociedades irregulares." | The Registrar denies inscription of a matrícula or of its transfer: a) if the holder is a person incapable or disqualified from engaging in commerce; b) in the case of irregular sociedades | `sv/sources/07_Codigo_Comercio.pdf` | Art. 421 p.81 (EVID-212; txt PAGE 81) |
| LB-014 | Código de Comercio, Art. 422: "La cancelación temporal o definitiva de la matrícula de empresa, será ordenada administrativamente por el Registrador de Comercio o Judicialmente por el Juez de lo Mercantil, siguiendo el procedimiento establecido en la ley, en los siguientes casos: a) Por sentencia ejecutoriada, que se emita en el proceso judicial correspondiente. b) Por haberlo solicitado su titular o sus herederos, en caso éste sea un comerciante individual y hubiera fallecido. c) Por incapacidad o inhabilidad sobreviniente de su titular para ejercer actos de comercio. d) Por disolución voluntaria o judicial de la sociedad, en cuyo caso la cancelación será temporal; y definitiva, por liquidación voluntaria o judicial de la sociedad mercantil titular de la empresa. e) Por la falta de renovación de la matrícula, si el titular dejó transcurrir cinco meses luego de vencido el plazo establecido en la Ley. f) Por la declaratoria judicial de quiebra de su titular. g) Por haberse declarado nula o irregular la sociedad mercantil titular de la empresa. h) Tratándose de comerciantes individuales, por existir más de dos acusaciones iniciadas en su contra, por delitos contra el patrimonio en las cuales se haya hecho uso de las excusas absolutorias establecidas en la Ley correspondiente; o por haber cometido el titular de la empresa cualquier clase de delitos, conforme sentencia judicial. i) Por haber cometido su titular actos de competencia desleal, conforme sentencia judicial. j) Por haberlo solicitado el Representante Legal de la sociedad extranjera, como consecuencia de su retiro voluntario del país." "En el caso del literal b) si el heredero quisieren seguir operando la empresa o empresas mercantiles heredadas, deberán solicitar el cambio de la titularidad y cualquier otra modificación que consideren conveniente ante el Registro de Comercio." | Temporal or definitive cancellation of the enterprise matrícula is ordered administratively by the Registrar or judicially by the Mercantile Judge, per the statutory procedure, in these cases: a) final judgment; b) request of the holder or, for a deceased individual merchant, his heirs; c) supervening incapacity/disqualification of the holder; d) voluntary or judicial dissolution of the sociedad (temporal) and voluntary or judicial liquidation (definitive); e) non-renewal if the holder let five months pass after the statutory deadline; f) judicial declaration of quiebra (bankruptcy — terminology only; SOQ-24 vintage watch); g) the sociedad declared null or irregular; h) for individual merchants, more than two accusations brought against them for patrimony crimes in which the excusas absolutorias (exculpatory grounds) of the corresponding law were applied, or any crime committed by the enterprise holder per judicial sentence; i) the holder's acts of unfair competition per judicial sentence; j) request of the legal representative of a foreign sociedad upon its voluntary withdrawal from the country. Closing proviso: under b), an heir wishing to continue operating the inherited empresa(s) must request the change of titularity and any other convenient modification before the Commerce Registry | `sv/sources/07_Codigo_Comercio.pdf` | Art. 422 p.81-82 (EVID-212; txt PAGE 81-82) |
| LB-015 | Código de Comercio, Art. 456: "Se establece el Registro de Comercio, como oficina administrativa, dependiente del Centro Nacional de Registros, destinada a garantizar la publicidad formal de los actos y contratos mercantiles que de conformidad con la ley la requieran. El Registro de Comercio podrá contar con una o varias oficinas, cuya ubicación, número y competencia territorial serán fijados en el Reglamento de la Ley de Registro de Comercio." "El Registro de Comercio comprenderá: I.- Registro de matrículas de comercio. II.- Registro de documentos de comercio. III.- Registro de balances." (ordinal IV DEROGADO by reform (29)) | The Commerce Registry is established as an administrative office dependent on the Centro Nacional de Registros, to guarantee the formal publicity of mercantile acts and contracts that by law require it; it may have one or several offices per the Reglamento of its law. It comprises: I. the register of commerce matrículas; II. the register of commerce documents; III. the register of balances (ordinal IV repealed) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 456 p.86 (EVID-217; txt PAGE 86) |
| LB-016 | Código de Comercio, Art. 457: "El registro de matriculas de comercio se llevará de conformidad con lo establecido en el Titulo I de este Libro. Con ese fin, se llevarán los siguientes registros particulares: I.- Matriculas de Empresas. II.- Registro de locales, agencias o sucursales." Art. 459: "En el registro de balances se conservarán los balances de fin de ejercicio, los estados de resultados y de cambio en el patrimonio, junto al dictamen de Auditor y sus anexos, de aquellos comerciantes que estén obligados a remitirlos al Registro de Comercio." | The matrículas register is kept per Title I of this Book, in two particular registers: I. enterprise matrículas; II. the register of locales, agencies or branches. In the balances register are conserved the fiscal-year-end balances, resultados and patrimonio-change statements, with the Auditor's dictamen and annexes, of those merchants obliged to send them | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 457/459 p.86 (EVID-217 zone; txt PAGE 86-87) |
| LB-017 | Código de Comercio, Art. 458: "El registro de documentos mercantiles se llevará en cuatro registros particulares: I.- Registro de instrumentos sociales. II.- Registro de poderes, nombramientos y credenciales. III.- Registro de contratos de venta a plazos de bienes muebles. IV.- Registro de todos los demás documentos sujetos a tal formalidad." | The commerce-documents register is kept in four particular registers: I. social instruments (constitución, modificación, transformación, fusión, liquidation deeds et al.); II. poderes, nombramientos y credenciales; III. installment-sale contracts over movable goods; IV. all other documents subject to that formality | `sv/sources/07_Codigo_Comercio.pdf` | Art. 458 p.86 (EVID-217; txt PAGE 86-87) |
| LB-018 | Código de Comercio, Art. 465-II: "En el Registro de poderes, nombramientos y credenciales: Los poderes que los comerciantes otorguen para objetos mercantiles o aquéllos que los mismos comerciantes otorguen para otros fines, pero que contengan cláusulas mercantiles, así como la revocación de dichos poderes; los nombramientos de factores o agentes de comercio; las credenciales de los directores, liquidadores o gerentes y en general, administradores, auditores externos y fiscales de las sociedades." | In the register of poderes, nombramientos and credenciales: the powers merchants grant for mercantile objects, or grant for other purposes but containing mercantile clauses, and their revocation; the appointment of factores or agentes de comercio (business managers/commercial agents); the credentials of directors, liquidators or managers and in general administrators, external auditors and fiscales (fiscal inspectors) of sociedades | `sv/sources/07_Codigo_Comercio.pdf` | Art. 465-II p.87-88 (EVID-217; txt PAGE 87-88) |
| LB-019 | Código de Comercio, Art. 469 (first inciso): "Cuando se suscriban documentos en que participen comerciantes, no podrán asentarse en el Registro, si no están previamente matriculadas sus empresas mercantiles." | When documents in which merchants participate are subscribed, they cannot be entered in the Registry unless their empresas are previously matriculated | `sv/sources/07_Codigo_Comercio.pdf` | Art. 469 p.89 (EVID-217; txt PAGE 89) |
| LB-020 | Código de Comercio, Art. 461: "El Registro de Comercio es público. Comprende tanto los asientos que aparezcan, como las anotaciones marginales que se hagan en los mismos. El Registrador expedirá, a quien lo solicite, certificación literal o en extracto de los asientos. En toda certificación, el Registrador hará constar las anotaciones marginales que figuren en la inscripción de que se trate." Art. 462: "Se presume legalmente que las relaciones jurídicas y los derechos existen tal como aparecen en las inscripciones." | The Commerce Registry is public; the Registrar issues, to whoever requests it, literal or extract certification of the entries, stating the marginal annotations. It is legally presumed that the legal relations and rights exist as they appear in the inscriptions | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 461/462 p.87 (EVID-217; txt PAGE 87) |
| LB-021 | Código de Comercio, Art. 475 (first inciso): "La inscripción producirá efectos legales a partir del día y hora de presentación, siempre que aquélla sea seguida de inscripción. El día y hora del asiento de presentación deberá constar en el asiento principal." (ordinals I-VI route the effects of each particular register to their governing articles: instrumentos sociales → Arts. 24/25 et al.; poderes → Arts. 367/371; venta a plazos → L.IV T.IV Cap.II; demás documentos → no effect against third parties until registered (Art. 475-IV exception: escrituras de emisión de bonos y obligaciones negociables, and their modification/cancellation, route to ordinal I as instrumentos sociales); matrículas → L.II T.I Cap.IV; balances → Arts. 286/441; VII DEROGADO) | An inscription produces legal effects from the day and hour of presentation, provided it is followed by inscription; the presentation day and hour must appear in the principal entry. The ordinals route per-register third-party effects to their governing articles | `sv/sources/07_Codigo_Comercio.pdf` | Art. 475 p.90-91 (EVID-217; txt PAGE 90-91) |
| LB-022 | Código de Comercio, Art. 486: "Siempre que la ley determina que un acto debe publicarse, este se hará en el Diario Oficial y en un diario de circulación nacional, por tres veces en cada uno, a menos que la ley determine un número diferente. Las publicaciones deberán ser alternas. Los plazos consiguientes se contarán desde el día siguiente al de la última publicación en el Diario Oficial." | Whenever the law determines that an act must be published, it is published in the Diario Oficial (Official Gazette) and in a nationally circulated daily, three times in each, unless the law sets a different number; publications must be ALTERNATE, and consequent deadlines count from the day following the last Diario Oficial publication | `sv/sources/07_Codigo_Comercio.pdf` | Art. 486 p.92 (EVID-217; txt PAGE 92) |

## 3. Functional Requirements

### 3.1 Comerciante status (Arts. 1-7, 15, 20)

- **SV-CML-FR-001:** The system shall classify every merchant record as
  exactly one *comerciante* kind: *comerciante individual* (individual
  merchant — a natural person titular of an *empresa mercantil*, commercial
  enterprise) or *comerciante social* (social merchant — a *sociedad*,
  company), per the Art. 2 dichotomy; foreigners and foreign-formed sociedades may engage in
  commerce under the same Code (Art. 2 final inciso — no nationality-based
  split of the obligation model). (LB-001; EVID-211)
- **SV-CML-FR-002:** The system shall treat a merchant record as
  *presumed commerce exercise* — activating the Art. 411 obligation set of
  FR-005 subject to the FR-004 exemption profiles — when the enterprise
  makes publicity of its commerce or opens a commercial establishment
  attending to the public (Art. 2 legal presumption), recorded as a
  boolean derived from public establishment/operation data.
  (LB-001; EVID-211)
- **SV-CML-FR-003:** The system shall record, for *comerciantes
  individuales*, the capacity basis as informational metadata with exactly
  one Art. 7 value — civil capacity · *habilitación de edad* (age
  emancipation, ≥18) · notarized legal-representative authorization (≥18)
  · judicial authorization (≥18) — with authorizations flagged irrevocable
  and registration-bound; no computation derives from this field.
  (LB-002; EVID-211)
- **SV-CML-FR-004:** The system shall implement the two Libro Segundo
  exemption profiles that reduce the Art. 411 obligation set: (a)
  *perfil Art. 20* — colectivas/comanditarias simples of fixed capital
  pursuing exclusively agriculture/livestock, urban-housing
  construction-and-rental (no regular sale intent) or the liberal
  professions, once inscribed: obligations I and IV survive, II and III
  are exempt; (b) *perfil Art. 15* — small individual merchants/industrialists
  with activo below US$12,000 (2008-reformed USD code text, dated-but-
  current per §2): only obligation IV survives. (LB-003; LB-004; EVID-211/216)

### 3.2 The four professional obligations map (Art. 411)

- **SV-CML-FR-005:** The system shall maintain, per merchant record, the
  four-obligation map of Art. 411 as the chassis of this wave, filtered by
  the FR-004 profiles: I. matrícula of the empresa + registration of its
  locales, agencias, sucursales (owned by this file, FR-006..012); II.
  contabilidad and correspondence in Code form (owned by
  `02_accounting-books.md`); III. annual balance deposit with auditor
  dictamen and annexes (owned by `03_financial-statements.md`); IV.
  activity within free-competition limits (a conduct rule — no automation
  surface, recorded for map completeness only). (LB-005; EVID-211)

### 3.3 Matrícula de empresa family (Arts. 412-422)

- **SV-CML-FR-006:** The system shall model the *matrícula de empresa* as
  a PERMANENT registration forming the *registro único de empresa* (single
  enterprise register) in the charge of the Registro de Comercio — one
  matrícula record per empresa, with number, state and dates stored on the
  merchant record; the registry, not the system, is the source of truth.
  (LB-006; EVID-212)
- **SV-CML-FR-007:** The system shall support one empresa carrying
  distinct mercantile activities, and shall require that every *local,
  agencia o sucursal* (premises, agency or branch) of the empresa be
  registered individually — each establishment record linked to its parent
  empresa matrícula and carrying its own registration data (Art. 414);
  same-department establishments remain one for giro-valuation purposes
  (Art. 453, gloss; valuation is registry-side).
  (LB-007; EVID-212/216)
- **SV-CML-FR-008:** The system shall open the matrícula obligation at
  the Art. 415 triggers: for *comerciantes individuales*, upon solicitud
  filing (content and requirements = Ley de Registro de Comercio +
  Reglamento — config-gap, OQ-001); for *comerciantes sociales*,
  immediately after inscription of the escritura de constitución, filing
  the solicitud together with the pacto social constitutivo.
  (LB-008; EVID-212)
- **SV-CML-FR-009:** The system shall store the registrar-extended
  *constancia* (matrícula certificate) as the SOLE proof document of (a)
  comerciante status and (b) ownership of the empresa (Art. 418),
  referencing the registry-issued constancia (issued once requirements are
  met per Art. 416, whose extract publication is registry-side
  information); system-generated matrícula reports shall be marked as
  non-probatory convenience output. (LB-009; LB-010; EVID-212)
- **SV-CML-FR-010:** The system shall track matrícula vigencia and the
  Art. 419 closure-risk window: an empresa may not operate without a
  vigente matrícula; upon a closure proceeding initiated at the
  Registrador's request (Juez de Paz, oral hearing, temporal closure of
  locales/agencias/sucursales), a maximum 30-*días hábiles* grace period
  runs for obtaining or renewing the matrícula before closure — the
  system shall expose the expiry/grace countdown as a warning state
  (días-hábiles arithmetic consumed from the fiscal-reporting wave's
  calendar engine by id, never restated). (LB-011; EVID-212)
- **SV-CML-FR-011:** The system shall implement the matrícula renewal
  state machine: matrículas renew ANNUALLY at the epoch fixed by the Ley
  de Registro de Comercio; each renewal updates the recorded information
  on titular, empresa and locales/agencias/sucursales per its Reglamento;
  non-renewal within the legal deadline is sanctioned per that law —
  epoch, fees and sanctions are config-gaps (OQ-001) exposed as dated
  configuration slots with NO shipped defaults (never hardcode).
  (LB-012; EVID-212)
- **SV-CML-FR-012:** The system shall model matrícula denial and
  cancellation states with the statutory reason catalogs: denial (Art. 421)
  — titular incapaz/inhábil · sociedad irregular; cancellation (Art. 422,
  temporal or definitive, administratively by the Registrador or
  judicially) — a) final judgment · b) titular/heirs request (deceased
  individual merchant; heirs continuing the inherited empresa must request
  titularity change before the Registry, closing proviso) · c) supervening
  incapacity/inhabilidad · d) disolución (temporal) / liquidación
  (definitive) · e) non-renewal after five months past the statutory
  deadline (the 5-month lapse escalates FR-011's expired state to
  cancellation) · f) judicial quiebra declaration (terminology only —
  SOQ-24 vintage watch rides `05_society-lifecycle.md`) · g) sociedad nula
  o irregular · h) individual merchant with more than two patrimony-crime
  accusations resolved via excusas absolutorias, or any delito by the
  holder per judicial sentence · i) competencia desleal by the holder per
  judicial sentence · j) foreign sociedad's legal-representative request
  upon voluntary withdrawal from the country.
  (LB-013; LB-014; EVID-212)

### 3.4 Registro de Comercio architecture (Arts. 456-487)

- **SV-CML-FR-013:** The system shall model registry entries against the
  Art. 456-459 registry architecture: the Registro de Comercio (a CNR-
  dependent administrative office guaranteeing formal publicity) comprises
  the matrículas register (two particular registers: Matrículas de
  Empresas · Registro de locales, agencias o sucursales), the commerce-
  documents register (four particular registers per Art. 458: instrumentos
  sociales · poderes/nombramientos/credenciales · venta a plazos de bienes
  muebles · demás documentos) and the balances register (fiscal-year-end
  balances + resultados + patrimonio-change + auditor dictamen + annexes)
  — every registry-entry record carries its book and particular register.
  (LB-015; LB-016; LB-017; EVID-217)
- **SV-CML-FR-014:** The system shall record *poderes, nombramientos y
  credenciales* per Art. 465-II on merchant/representative records:
  merchant powers for mercantile objects (or other-purpose powers
  containing mercantile clauses) and their revocations; nombramientos of
  factores and agentes de comercio; credenciales of directors,
  liquidators, gerentes and in general administrators, external auditors
  and fiscales of sociedades — the authority-default semantics of those
  appointments are owned by `06_commercial-agents.md` (consumed there by
  reference; no re-derivation here). (LB-018; EVID-217)
- **SV-CML-FR-015:** The system shall enforce the Art. 469 precondition
  gate on registry entries: a document in which merchants participate
  cannot be entered in the Registry unless the participating empresas are
  previously matriculated — registry-entry recording shall surface a
  blocking validation (with the unmatriculated empresa identified) for
  instrument registrations and balance deposits alike.
  (LB-019; EVID-217)
- **SV-CML-FR-016:** The system shall treat the registry's own data as
  authoritative per the publicity rules: the Registro de Comercio is
  public with literal/extract certifications (system exports are
  conveniences, never certifications); registered relations and rights are
  presumed to exist as inscribed; every registry entry shall carry its
  presentation day and hour, from which its legal effects run when
  followed by inscription (per-register third-party effect routing per
  Art. 475 ordinals is registry-side law; the system records the
  presentation timestamp as the effect anchor). (LB-020; LB-021; EVID-217)
- **SV-CML-FR-017:** The system shall implement the Art. 486 publication
  rule as a reusable notice engine: whenever a statutory publication duty
  attaches to a registry act, publication runs in the *Diario Oficial*
  (Official Gazette) AND a nationally circulated daily, three times in
  each, in ALTERNATE
  sequence, with any different count fixed by a specific law taking
  precedence; all consequent deadlines count from the day following the
  LAST Diario Oficial publication — consumed by later files of this wave
  (e.g. `05_society-lifecycle.md` fusión/capital-reduction notices) by FR
  id, never restated. (LB-022; EVID-217)

## 4. Data Model

Layer semantics: merchant registration is Odoo-native — all entities live
in the client (wave default `odoo`; see §5). The registry itself is an
external authority (CNR): the model tracks registry-issued facts
(numbers, dates, states, constancia), it does not emulate the registry.

**Merchant status + obligation profile (on res.company / res.partner):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_merchant_kind | select | comerciante_individual · comerciante_social | FR-001 |
| res.company | sv_cml_commerce_presumed | boolean (computed) | publicity / public-establishment presumption active | FR-002 |
| res.partner (individual merchant) | sv_cml_capacity_basis | select | civil_capacity · habilitacion_edad · notarized_rep_auth · judicial_auth (Art. 7) | FR-003 |
| res.company | sv_cml_lii_exemption_profile | select | none · art20_collective · art15_small_individual | FR-004 |
| res.company | sv_cml_art20_finalidades | tags | agriculture_livestock · urban_housing_rental · liberal_professions | FR-004 |
| res.company | sv_cml_obligations_411 | computed list | subset of {I matrícula, II contabilidad, III balance deposit, IV free competition} after FR-004 filtering; II/III owned by files 02/03 | FR-005 |

**Matrícula state machine (on res.company + establishments):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_matricula_number · sv_cml_matricula_state | char · select | unregistered · pending · vigente · expired · cancelled_temporal · cancelled_definitive · denied | FR-006, FR-012 |
| res.company | sv_cml_matricula_registered_on · sv_cml_renewal_epoch | date · config slot | epoch/fees/sanctions = Ley Registro de Comercio config-gaps (OQ-001) — no shipped defaults | FR-011 |
| res.company | sv_cml_constancia_ref | document reference | registrar-issued constancia = sole proof (Arts. 416/418) | FR-009 |
| res.company | sv_cml_closure_risk | computed state | none · proceeding_grace (≤30 días hábiles countdown, calendar engine by id) | FR-010 |
| res.company (establishment child) | sv_cml_establishment_kind | select | local · agencia · sucursal (each individually registered; Art. 453 same-department gloss) | FR-007 |
| res.company | sv_cml_matricula_cancel_reason | select | art422_a judgment · art422_b holder_heirs · art422_c supervening_incapacity · art422_d disolucion_liquidacion · art422_e non_renewal_5m · art422_f quiebra · art422_g sociedad_nula_irregular · art422_h patrimony_delitos · art422_i competencia_desleal · art422_j foreign_rep_withdrawal; denial: art421_a incapaz_inhabil · art421_b sociedad_irregular | FR-012 |

**Registry-entry model (Arts. 456-459 architecture):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.registry.entry | entry_kind | select | matricula_empresa · matricula_establecimiento · instrumento_social · poder_nombramiento_credencial · balance_deposit · venta_plazos · otro_documento | FR-013 |
| l10n_sv_commerce.registry.entry | registry_book · presented_at | select · datetime | book per Art. 456 (matrículas/documentos/balances) + particular register per Arts. 457/458/459; presentation day+hour = effect anchor (Art. 475) | FR-013, FR-016 |
| l10n_sv_commerce.registry.entry (poder subclass) | sv_cml_power_kind | select | poder_mercantil · poder_mercantile_clauses · revocacion · nombramiento_factor · nombramiento_agente · credencial_director · credencial_liquidador · credencial_gerente · credencial_administrador · credencial_auditor_externo · credencial_fiscal | FR-014 |
| l10n_sv_commerce.registry.entry | sv_cml_matricula_precondition_ok | computed | Art. 469 gate result + blocking reason | FR-015 |

**Publication engine (Art. 486):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.publication | channel · published_on · sequence | select · date · integer | diario_oficial · diario_nacional; alternation enforced; override count when a specific law fixes one | FR-017 |
| l10n_sv_commerce.publication | sv_cml_deadline_anchor | computed date | deadlines run from the day after the LAST D.O. publication | FR-017 |

## 5. Odoo Mapping

Layer semantics for this wave: merchant registration is Odoo-native
(res.company/res.partner families) — every FR maps `odoo`; no SaaS rows
are introduced because none of these FRs touch DTE
generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are stable
across Odoo 17/18/19/20; no version-specific behavior is required by this
file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | res.company | sv_cml_merchant_kind | Individual vs social merchant stamp; drives the obligation chassis |
| FR-002 | odoo | res.company | sv_cml_commerce_presumed | Derived from establishment/publicity data; activates FR-005 map subject to FR-004 |
| FR-003 | odoo | res.partner | sv_cml_capacity_basis | Informational Art. 7 metadata; no computation attached |
| FR-004 | odoo | res.company | sv_cml_lii_exemption_profile, sv_cml_art20_finalidades | Art. 20 keeps 411 I/IV; Art. 15 keeps only IV; $12,000 activo threshold = 2008 USD code text (dated-but-current, §2 note) |
| FR-005 | odoo | res.company | sv_cml_obligations_411 | Chassis consumed by 02/03 (files cite by FR id); IV = conduct rule, no surface |
| FR-006 | odoo | res.company | sv_cml_matricula_number/_state | Permanent registro único tracked, registry = source of truth |
| FR-007 | odoo | res.company (establishment children) | sv_cml_establishment_kind | Each local/agencia/sucursal registered individually and linked to the empresa matrícula |
| FR-008 | odoo | res.company | matrícula obligation trigger | Social: opens at escritura-constitution inscription (link to 04_society-types.md when it lands); solicitud content = config-gap OQ-001 |
| FR-009 | odoo | res.company | sv_cml_constancia_ref | Sole-proof document; reports marked non-probatory |
| FR-010 | odoo | res.company | sv_cml_closure_risk | 30-días-hábiles grace countdown; días-hábiles arithmetic consumed from the fiscal-reporting calendar engine (SV-FREP-FR-195..208) by id |
| FR-011 | odoo | res.company + ir.config_parameter | renewal state machine + epoch/fee/sanction slots | Config-gaps (OQ-001): NO shipped defaults; renewal updates titular/empresa/establecimiento info |
| FR-012 | odoo | res.company | sv_cml_matricula_state, sv_cml_matricula_cancel_reason | Art. 421/422 catalogs; 5-month lapse escalates FR-011 expired → cancelled; quiebra = terminology only (SOQ-24 in 05) |
| FR-013 | odoo | l10n_sv_commerce.registry.entry | entry_kind, registry_book | Arts. 456-459 architecture: 3 books, particular registers as catalog |
| FR-014 | odoo | l10n_sv_commerce.registry.entry + res.partner | sv_cml_power_kind | 465-II set; authority semantics owned by 06_commercial-agents.md |
| FR-015 | odoo | l10n_sv_commerce.registry.entry | sv_cml_matricula_precondition_ok | Blocking validation incl. balance deposits (AC-003) |
| FR-016 | odoo | l10n_sv_commerce.registry.entry | presented_at | Publicity/presumption metadata; presentation timestamp = effect anchor |
| FR-017 | odoo | l10n_sv_commerce.publication | channel/sequence/deadline_anchor | Reusable 3×-alternate D.O.+daily engine; consumers (05 lifecycle notices) cite by FR id |

Version-regime notes (D12): no dated values live in this file. The 07_
text basis carries the SOQ-22 verification note (§2); the only code-text
value, the US$12,000 Art. 15 threshold, is 2008-reformed USD wording —
dated-but-current under the SOQ-22 residual watch. Renewal epoch/fees/
sanctions are deliberately absent (OQ-001 config-gaps). Consumer pointer
(29_, EVID-172): the CNR F985/F-975 semi-annual third-party report to
DGII (CT 121 a)2) is registry-side; no surface is built for it here.
E-invoicing kin (pointer only, no re-derivation): DTE emitter-identity
data (nombre/NIT/NRC/actividad) flows from these res.company records;
the DTE-side contract is owned by the e-invoicing wave's
onboarding/authorization cluster (A11) — no norm in this corpus ties
DTE emission to matrícula vigencia.

## 6. Acceptance Criteria

- **AC-001:** Given an empresa operating its main local plus 2 sucursales,
  when its registry data is recorded, then one matrícula de empresa
  registration and TWO establishment registrations (each linked to the
  empresa matrícula, kinds sucursal) exist — three registrations in all
  (FR-007).
- **AC-002:** Given a merchant whose matrícula is expired and against whom
  a Registrador-initiated closure proceeding is recorded, when the
  matrícula renewal is recorded within the 30-*días hábiles* grace
  window, then sv_cml_closure_risk clears and no closure state is reached;
  when the grace lapses without renewal, then the closure-proceeding state
  persists (FR-010, FR-011).
- **AC-003:** Given a merchant without a vigente matrícula, when a
  registry entry of kind balance_deposit (or instrumento_social) involving
  that merchant is recorded, then the entry is blocked with the Art. 469
  precondition reason identifying the unmatriculated empresa (FR-015).
- **AC-004:** Given a comerciante social whose escritura de constitución
  inscription is recorded, when the registry-entry data is saved, then the
  matrícula obligation is open immediately, with the filing package
  referencing the pacto social constitutivo (FR-008).
- **AC-005:** Given a matrícula whose statutory renewal deadline (config
  slot, OQ-001) passed more than five months ago without renewal, when the
  state machine runs, then the matrícula state becomes cancelled with
  reason art422_e non_renewal_5m (FR-011, FR-012).
- **AC-006:** Given (i) a colectiva sociedad of fixed capital whose
  recorded finalidades are exclusively agriculture and (ii) a small
  comerciante individual with activo US$9,000, when the FR-004 profiles
  apply, then (i) keeps obligations 411 I and IV only and (ii) keeps
  obligation IV only; a default merchant keeps all four (FR-004, FR-005).
- **AC-007:** Given a registry act with a statutory publication duty and
  no law fixing a different count, when its publication record is built,
  then three Diario Oficial and three national-daily publications are
  scheduled in alternate sequence and every derived deadline anchors to
  the day after the LAST Diario Oficial publication (FR-017).
- **AC-008:** Given a vigente matrícula, when its proof documents are
  inspected, then the sole-proof reference is the registrar-issued
  constancia (sv_cml_constancia_ref) and system-generated matrícula
  reports carry the non-probatory marker (FR-009).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-25 carried: the Ley de Registro de Comercio and its Reglamento are NOT in the corpus, yet Arts. 415/420/456 delegate to them the matrícula solicitud requirements, the ANNUAL renewal epoch, the renewal information set, fees and the non-renewal sanctions (and registry office organization). FR-008/FR-011 expose these as config slots with NO shipped defaults; the renewal clock and the Art. 422-e five-month cancellation trigger cannot compute until the epoch is configured from the law. Acquisition candidate ≥74 (numbering per sources registry). | no | Takumi S5 (sources watch) | open |
