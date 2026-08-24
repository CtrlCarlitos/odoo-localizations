# SV — Commercial-legal — Accounting books: organized system, legalization, no-alteration and the retention matrix

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador bookkeeping regime of Código de Comercio
(Commercial Code, CC) Título II (Contabilidad): the organized-system duty
and register set of Art. 435 — generally accepted accounting systems,
*Estados Financieros* (financial statements), *diario* (daybook/journal)
and *mayor* (ledger), loose-leaf and EXPRESSLY-LEGAL electronic bookkeeping
with notice to the state watchdog office; the Art. 436 language/currency/
in-country-keeping trinity; the Art. 437 keeper thresholds (US$12,000
individuals / all *sociedades*, companies); the Art. 438 legalization
regime (Contador Público / Auditor Externo authorization, folios, opening
*razón* — the first-leaf formal statement: merchant, object, sheet count,
place and delivery date); the NO-ALTERATION regime of Art. 439 and its
Art. 440 extension to every statutory register; the Art. 446
first-*Diario*-partida opening balance and register-shape freedom; the
Art. 447 labor-obligation provision; the Art. 452 simplified single bound
book for sub-US$12,000 individuals; and the retention family of
Arts. 451/454/455 — 10 years plus 5 post-liquidation, *facturas anexas*
(annexed invoices) and correspondence, and the 24-month media-migration
rule — synthesized with the AML ≥15-year regime of D.L. 426 Art. 26 into
the **SOQ-28 canonical retention matrix** (one FR, §3.7), the single
objects-×-retention table the whole localization consumes.

It does **not** cover: annual financial statements, their certification and
the balance deposit (`03_financial-statements.md`, Arts. 441-445, 474 —
including the US$34,000 auditor threshold); society-type rules and the
content of society books (`04_society-types.md` — this file supplies only
the Art. 440 discipline that extends to them); society lifecycle mechanics
(`05_society-lifecycle.md`, incl. the Art. 340 post-liquidation deposit of
corporate papers); merchant status, matrícula and the registry
(`01_merchant-registration.md`, consumed for the Art. 451 sanction);
AML compliance beyond the retention row — sujetos obligados
classification, DD, ROS and thresholds (`10_aml-compliance.md`, which
feeds this file's matrix by id); or the DTE-side conservation mechanics
owned by the e-invoicing wave (`02_transmission.md` §3.11 account.move
invariants; `04_signing_delivery.md` §3.7 archive tiers) — cited here
by id, never restated.

## 2. Legal Basis

Authority order (binding, per master evidence index S5): the Código de
Comercio = **07_** (D.L. Nº 671, 8-may-1970, D.O. 140 T.228 31-jul-1970;
29 listed reforms, last = D.L. 641-2008) — **STALE-PRINT RULING (SOQ-22,
W22 falsification 2026-08-23)**: the W12 "no post-2008 CC structural
reform" verdict is FALSIFIED — the asamblea por-anios census found and
this corpus now OWNS the six-instrument post-2008 reform set 109_-114_
(EVID-407..412: bearer-share suppression, usura, SAS, cheque
truncation, SAS-gratuidad chain — reformed-article surface: 111_ Arts.
17/18 + Capítulo VIII-Bis 305-A..Z + 315-319 + 358; 109_ Arts.
134/153/155/158/164/212/219/337/338; 110_ Art. 960-III + 960-A; 112_
Arts. 838-A..E); 07_/73_ consolidation texts are STALE for the
reformed articles, and **NO article of this file's LB set is in the
reformed set** — this file's bookkeeping chapter (Arts. 435-455) is
OUTSIDE the six instruments' touch and the 07_ print STANDS CURRENT
for this article range (W23 T5 grep-verified). Census residual
(negative watch): por-anios carries no cards for 2010/2012-2015 and
2019 looks partial — a 2009-2019 CC reform cannot be fully excluded
from enumeration alone; the six owned instruments carry the KNOWN
post-2008 surface. Verbatim text below is copied from the 07_ evidence file
(EVID-213/215/216) and, where the evidence abbreviates (Arts. 437-439,
446-447, 451-455), from the extraction txt
`sv/.extractions/07_Codigo_Comercio.pdf.txt` (citable per standing ruling;
page pointers = txt PAGE markers; reform tick marks "(7)(18)(29)" stripped
from quotations, provenance noted here).

The AML retention row's authority: **71_** — Ley Contra el Lavado de
Dinero y de Activos, D.L. N° 426 (7-oct-2025, D.O. N° 190 T.449 9-oct-2025;
effective 17-oct-2025), a wholesale replacement of D.L. 498-1998 (Art. 61).
Its Art. 26 installs the UNIFORM ≥15-year rule (transaction records AND
client-ID/account docs — the W12 finding): the old 5y-docs/15y-registers
split of the dead 1998 law is DEAD and is never cited as authority.

Currency discipline (SOQ-29): Art. 436's "en Colones o en Dólares"
alternative is pre-dollarization code text kept by reform (18)(19) —
historical remnant; the operative account currency is USD, and no
colones-denominated value occurs anywhere in this file's article set.
Thresholds: the US$12,000 keeper/simplified-book threshold (Arts. 437,
452) is 2008-reform (29) USD code text — dated-but-current under the
SOQ-22 residual watch (same treatment as the Art. 15 threshold in
`01_merchant-registration.md` §2); the US$34,000 auditor threshold
(Art. 474) is 2008 USD code text of the same family and lands in
`03_financial-statements.md`.

Kin pointers (by id, no re-derivation): the Odoo-side correction
invariants kin to the Art. 439 regime are e-invoicing
`02_transmission.md` §3.11 (SV-EINV-FR-159..164) — the CC text is the LB
root here; DTE/RG conservation mechanics and archive tiers are e-invoicing
`04_signing_delivery.md` §3.7 (SV-EINV-FR-152..158) under CT 147 as
reformed by D.L. 487-2022, with SaaS custody tiers per
`shared/docs/saas-thin-client-architecture.md` D3 — both consumed by id in
the §3.7 matrix and never restated.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 435: "El comerciante está obligado a llevar contabilidad debidamente organizada de acuerdo con alguno de los sistemas generalmente aceptados en materia de Contabilidad y aprobados por quienes ejercen la función pública de Auditoria. Los comerciantes deberán conservar en buen orden la correspondencia y demás documentos probatorios. El comerciante debe llevar los siguientes registros contables: Estados Financieros, diario y mayor, y los demás que sean necesario por exigencias contables o por Ley. Los comerciantes podrán llevar la contabilidad en hojas separadas y efectuar las anotaciones en el Diario en forma resumida y también podrán hacer uso de sistemas electrónicos o de cualquier otro medio técnico idóneo para registrar las operaciones contables. Todo lo anterior lo hará del conocimiento de la Oficina que ejerce la vigilancia del Estado." | The merchant must keep duly organized accounting under one of the generally accepted accounting systems approved by those who exercise the public audit function. Merchants must keep correspondence and other probative documents in good order. The merchant must keep the following accounting registers: financial statements, daybook and ledger, and any others required by accounting exigency or by law. Merchants may keep accounting on loose sheets, make summarized daybook annotations, and also use electronic systems or any other suitable technical means to record accounting operations; all of the foregoing must be noticed to the Office exercising the State's vigilance | `sv/sources/07_Codigo_Comercio.pdf` | Art. 435 pp.82-83 (EVID-213; txt PAGE 82-83) |
| LB-002 | Código de Comercio, Art. 436: "Los registros deben llevarse en castellano. Las cuentas se asentarán en Colones o en Dólares de los Estados Unidos de América. Toda contabilidad deberá llevarse en el país, aún la de las agencias, filiales, subsidiarias o sucursales de sociedades extranjeras. La contravención será sancionada por la oficina que ejerce la vigilancia del Estado de conformidad a su Ley. Toda autoridad que tenga conocimiento de la infracción, está obligada a dar aviso inmediato a la oficina antes mencionada." | The registers must be kept in Spanish (castellano). Accounts are entered in Colones or in US Dollars (historical pre-dollarization alternative — operative currency USD, §2). ALL accounting must be kept in the country, including that of agencies, branches, subsidiaries or sucursales of foreign companies. Contravention is sanctioned by the office exercising the State's vigilance per its law; every authority learning of the infraction must immediately report it to that office | `sv/sources/07_Codigo_Comercio.pdf` | Art. 436 p.83 (EVID-213; txt PAGE 83) |
| LB-003 | Código de Comercio, Art. 437: "Los comerciantes individuales con activo inferior a los doce mil dólares de los Estados Unidos de América, llevarán la contabilidad por sí mismos o por personas de su nombramiento. Si el comerciante no la llevare por si mismo, se presumirá otorgado el nombramiento por quien la lleve, salvo prueba en contrario. Sin embargo, los comerciantes individuales cuyo activo en giro sea igual o superior a doce mil dólares y los comerciantes sociales en general, están obligados a llevar su contabilidad por medio de contadores, de empresas legalmente autorizadas, bachilleres de comercio y administración o tenedores de libros, con títulos reconocidos por el Estado, debiendo estos dos últimos acreditar su calidad de la forma como establece el Art. 80 del Reglamento de Aplicación del Código Tributario." | Individual merchants with assets below twelve thousand US dollars keep their accounting themselves or through persons of their own appointment (if not kept by the merchant himself, the appointment is presumed granted by whoever keeps it, absent proof to the contrary). However, individual merchants whose business assets equal or exceed twelve thousand dollars and ALL social merchants must keep their accounting through accountants, legally authorized firms, commerce-and-administration bachilleres (high-school graduates) or bookkeepers, with State-recognized credentials — the latter two accrediting their status as set by Art. 80 of the Tax Code Application Regulations | `sv/sources/07_Codigo_Comercio.pdf` | Art. 437 p.83 (EVID-213; txt PAGE 83) |
| LB-004 | Código de Comercio, Art. 438: "Los registros obligatorios deben llevarse en libros empastados o en hojas separadas, todas las cuales estarán foliadas, y serán autorizadas por el Contador Público autorizado que hubiere nombrado el comerciante. Tratándose de comerciantes sociales, será el Auditor Externo quien autorizará los libros o registros, debiendo el administrador designado en los estatutos, avalar dicha autorización. Las hojas de cada libro deberán ser numeradas y selladas por el Contador Público autorizado, debiendo poner en la primera de ellas una razón firmada y sellada, en la que se exprese el nombre del comerciante que las utilizará, el objeto a que se destinan, el número de hojas que se autorizan y el lugar y fecha de la entrega al interesado. La Oficina que ejerce la vigilancia del Estado fiscalizará el cumplimiento de esta obligación, pudiendo sancionar las deficiencias que existieren contra el Auditor, el comerciante o sus administradores, según el caso todo de conformidad a la Ley." | Obligatory registers are kept in bound books (libros empastados) or on loose sheets, all folioed, and are authorized by the authorized Contador Público (public accountant) the merchant has appointed; for social merchants it is the Auditor Externo (external auditor) who authorizes the books or registers, with the administrador designated in the estatutos (bylaws) endorsing the authorization. Each book's sheets must be numbered and stamped by the authorized Contador Público, the first sheet carrying a signed-and-stamped razón stating the merchant's name, the object to which the sheets are destined, the number of sheets authorized, and the place and date of delivery to the interested party. The State-vigilance office inspects compliance and may sanction deficiencies against the Auditor, the merchant or its administrators, per the law | `sv/sources/07_Codigo_Comercio.pdf` | Art. 438 p.83 (EVID-213; txt PAGE 83) |
| LB-005 | Código de Comercio, Art. 439: "Los comerciantes deben asentar sus operaciones diariamente y llevar su contabilidad con claridad, en orden cronológico, sin blancos, interpolaciones, raspaduras, ni tachaduras, y sin presentar señales de alteración. Se salvarán a continuación, inmediatamente de advertidos, los errores u omisiones en que se incurriere al escribir en los registros, explicando con claridad en qué consisten, y extendiendo el concepto tal como debiera haberse escrito. Inmediatamente después de haberse descubierto el yerro o reconocida la omisión en que se incurrió, se hará el oportuno asiento de rectificación." | Merchants must enter their operations daily and keep accounting clearly, in chronological order, with no blanks, interpolations, scrapings or strike-throughs, and showing no signs of alteration. Errors or omissions made in writing the registers are saved immediately below, as soon as noticed, clearly explaining what they consist of and extending the concept as it should have been written. Immediately after the error is discovered or the omission recognized, the opportune rectification entry (asiento de rectificación) is made | `sv/sources/07_Codigo_Comercio.pdf` | Art. 439 p.83 (EVID-213; txt PAGE 83) |
| LB-006 | Código de Comercio, Art. 440: "Las disposiciones de los artículos 436, 438 y 439 son aplicables a todos los registros que por ley, deban llevar los comerciantes, aunque no sean de contabilidad." | The provisions of Articles 436, 438 and 439 apply to ALL registers merchants must keep by law, even if not accounting registers | `sv/sources/07_Codigo_Comercio.pdf` | Art. 440 p.83 (EVID-213; txt PAGE 83) |
| LB-007 | Código de Comercio, Art. 446: "En el Diario se asentará, como primera partida, el balance que muestre la situación económica y financiera del comerciante al principiar sus operaciones, anotando las cuentas del activo, pasivo y capital. Se asentarán inmediatamente después en orden cronológico, las partidas correspondientes a las operaciones que haga el comerciante, por cuenta propia o ajena. Cuando las necesidades del negocio lo requieran, el Diario y Mayor a que se refiere el artículo 435, podrán estar constituidos por varios registros, siempre que se llenen los requisitos exigidos por este Código. También podrán llevarse el Diario y el Mayor en un solo registro." | The Diario's FIRST entry (partida) is the balance showing the merchant's economic and financial situation at the start of operations, stating the asset, liability and capital accounts. Immediately after, the entries for the merchant's operations — on own or third-party account — follow in chronological order. When business needs require, the Diario and Mayor of Art. 435 may consist of several registers, provided this Code's requirements are met; the Diario and Mayor may also be kept in a single register | `sv/sources/07_Codigo_Comercio.pdf` | Art. 446 p.85 (EVID-214 zone; txt PAGE 85) |
| LB-008 | Código de Comercio, Art. 447: "Debe constituirse una provisión o reserva para proveer al cumplimiento de las obligaciones que respecto a su personal tenga el comerciante en virtud de la ley o de los contratos de trabajo." | A provision or reserve must be constituted to provide for compliance with the obligations the merchant owes its personnel by virtue of law or employment contracts | `sv/sources/07_Codigo_Comercio.pdf` | Art. 447 p.85 (EVID-214; txt PAGE 85) |
| LB-009 | Código de Comercio, Art. 451: "Los comerciantes y sus herederos o sus sucesores conservarán los registros de su giro en general por diez años y hasta cinco años después de la liquidación de todos sus negocios mercantiles. Todo sin perjuicio de lo dispuesto en el Art. 445. El Registrador no concederá matricula de empresa, o cancelará la ya concedida, al que haya infringido lo dispuesto en este artículo. Cualquier autoridad que tenga conocimiento de la infracción deberá librar inmediatamente oficio al Registrador, haciéndola de su conocimiento." | Merchants and their heirs or successors must conserve the registers of their business for TEN YEARS and up to five years after the liquidation of all their mercantile businesses (without prejudice to Art. 445). The Registrar will not grant an enterprise matrícula, or will cancel one already granted, to whoever infringes this article; any authority learning of the infraction must immediately notify the Registrar | `sv/sources/07_Codigo_Comercio.pdf` | Art. 451 p.85 (EVID-215; txt PAGE 85) |
| LB-010 | Código de Comercio, Art. 452: "Los comerciantes individuales cuyo activo en giro sea inferior a los doce mil dólares de los Estados Unidos de América, llevarán un libro encuadernado para asentar separadamente los gastos, compras y ventas, al contado y al crédito. En dicho libro harán, al final de cada año, un balance general de todas las operaciones de su giro, con especificación de los valores que forman el activo y el pasivo." | Individual merchants whose business assets are below twelve thousand US dollars keep ONE bound book entering separately expenses, purchases and sales, in cash and on credit; in that book they make, at the end of each year, a balance general of all the year's operations, specifying the values forming assets and liabilities | `sv/sources/07_Codigo_Comercio.pdf` | Art. 452 p.86 (EVID-216; txt PAGE 85-86) |
| LB-011 | Código de Comercio, Art. 454: "Las cartas, telegramas y facturas que reciban y las copias de las que expidan los comerciantes, que sirvan de comprobantes para los aspectos contables, se considerarán anexas a la contabilidad y deberán conservarse durante el tiempo indicado en el Art. 451." | The letters, telegrams and invoices (facturas) merchants receive, and the copies of those they issue, that serve as supporting documents for accounting purposes, are considered ANNEXED to the accounting and must be conserved for the period indicated in Art. 451 | `sv/sources/07_Codigo_Comercio.pdf` | Art. 454 p.85 (EVID-215; txt PAGE 85) |
| LB-012 | Código de Comercio, Art. 455: "Los comerciantes podrán hacer uso de microfilm, de discos ópticos o de cualquier otro medio que permita archivar documentos e información, con el objeto de guardar de una manera más eficiente los registros, documentos e informes que le correspondan, una vez transcurridos por lo menos veinticuatro meses desde la fecha de su emisión. Las copias o reproducciones que deriven de microfilm, disco óptico o de cualquier otro medio, tendrán el mismo valor probatorio que los originales siempre que tales copias o reproducciones sean certificadas por Notario, previa confrontación con los originales. En caso de falsedad, se estará a lo dispuesto en el Código Penal." | Merchants may use microfilm, optical discs or any other means permitting archival of documents and information, to store more efficiently the registers, documents and reports they owe, once AT LEAST TWENTY-FOUR MONTHS have elapsed from the date of emission. Copies or reproductions derived from microfilm, optical disc or any other means have the same probative value as the originals, provided they are certified by a Notary after confrontation with the originals. In case of falsity, the Penal Code applies | `sv/sources/07_Codigo_Comercio.pdf` | Art. 455 p.86 (EVID-215; txt PAGE 86) |
| LB-013 | Ley Contra el Lavado de Dinero y de Activos (D.L. 426), Art. 26: "Los sujetos obligados deben mantener por un período no menor de quince años los registros necesarios sobre transacciones realizadas, tanto nacionales como internacionales, sean originadores o beneficiarios, que permitan responder de forma inmediata las solicitudes de información de los entes de supervisión correspondientes, de la Fiscalía General de la República y de los tribunales competentes, relacionados al lavado de activos, el financiamiento del terrorismo y financiamiento de la proliferación de armas de destrucción masiva, tales registros servirán para reconstruir cada transacción, a fin de proporcionar, de ser necesario, pruebas de conducta delictiva. Los sujetos obligados deben archivar y conservar la documentación de las operaciones de las que sean originadores o beneficiarios, por el plazo mencionado en el inciso anterior, el cual se empezará a contar a partir de la fecha de la finalización de cada transacción. Los datos de identificación del cliente y archivos de cuentas también deberán conservarse por el mismo plazo, contado a partir de la terminación de la relación comercial o cierre de cuentas. Los sujetos obligados podrán hacer uso de medios electrónicos u otros mecanismos, para el debido resguardo de todo tipo de información que sea objeto de la presente ley." | Obligated subjects (sujetos obligados) must maintain for a period of NOT LESS THAN FIFTEEN YEARS the records necessary on transactions performed, national or international, as originators or beneficiaries, allowing immediate response to information requests from supervisors, the FGR and the competent courts (AML/CFT/CPF-related), records that serve to RECONSTRUCT each transaction. They must archive and conserve the documentation of operations of which they are originators or beneficiaries for the same period, counted from the date of FINALIZATION OF EACH TRANSACTION. Client identification data and account files must also be conserved for the same period, counted from TERMINATION OF THE COMMERCIAL RELATIONSHIP OR ACCOUNT CLOSURE. Obligated subjects may use electronic means or other mechanisms for the due safekeeping of every type of information that is the object of this law | `sv/sources/71_Ley_LavadoActivos_DL426_2025.pdf` | Art. 26 pp.20-21 (EVID-244; txt PAGE 20-21) |

## 3. Functional Requirements

### 3.1 Organized system and electronic legality (Arts. 435-436)

- **SV-CML-FR-018:** The system shall maintain, per merchant record, the
  Art. 435 bookkeeping posture: accounting organized under a generally
  accepted accounting system approved by the public audit function
  (recorded as informational configuration — approval is the profession's
  act, not the system's); the statutory register set = *Estados
  Financieros*, *diario* and *mayor*, PLUS every additional register
  demanded by accounting exigency or by law (additions tracked as register
  records, §4); and correspondence plus probative documents kept in good
  order (document-order/completeness surfaced as a compliance attribute of
  the archive, consumed by the §3.7 retention matrix).
  (LB-001; EVID-213)
- **SV-CML-FR-019:** The system shall treat electronic bookkeeping as
  EXPRESSLY LEGAL per Art. 435: accounting may be kept on *hojas separadas*
  (loose sheets), Diario annotations may be summarized, and electronic
  systems or any other suitable technical means may record the accounting
  operations — NO paper duplication is required — provided everything is
  made known (*del conocimiento*) to the *Oficina que ejerce la vigilancia
  del Estado* (the office exercising the State's vigilance); the system
  shall expose the notice date and acknowledgment as compliance metadata
  (notice mechanics are a config-gap, OQ-001 — no computation derives from
  the field). (LB-001; EVID-213)
- **SV-CML-FR-020:** The system shall enforce the Art. 436 trinity on the
  ledger: records kept in *castellano* (Spanish); accounts entered in US
  Dollars (the Colones alternative is pre-dollarization code text —
  historical remnant, operative currency USD per §2); and ALL accounting
  kept in El Salvador, including the accounting of agencies, branches,
  subsidiaries or *sucursales* of foreign *sociedades* — contravention
  being sanctionable by the vigilance office with a mandatory report duty
  on any authority learning of it. Odoo deployment posture: the
  client-held Odoo database is the merchant's *contabilidad* and its
  custody satisfies in-country keeping; the SaaS layer of the thin-client
  architecture operates DTE transmission/archive-convenience, not la
  contabilidad (D2 split; Tier B residency residual → OQ-002).
  (LB-002; EVID-213)

### 3.2 Keeper thresholds (Art. 437)

- **SV-CML-FR-021:** The system shall derive the keeper profile from the
  Art. 437 thresholds: individual merchants with *activo* (assets) below
  US$12,000 keep the accounting themselves or through persons of their own
  appointment (appointment presumed for whoever actually keeps it, absent
  proof to the contrary); individual merchants with *activo en giro*
  (business assets) ≥ US$12,000 and ALL *comerciantes sociales* must keep
  their accounting through *contadores* (accountants), legally authorized
  firms, *bachilleres* de comercio y administración or *tenedores de libros*
  (bookkeepers) with State-recognized títulos — the latter two accrediting
  per Art. 80 of the Reglamento de Aplicación del Código Tributario
  (mechanics = taxation-wave corpus pointer). The US$12,000 threshold is
  2008-reform (29) USD code text — dated-but-current (§2); the profile is
  recorded metadata (keeper identity + credential basis), read together
  with the exemption profiles of SV-CML-FR-004.
  (LB-003; EVID-213)

### 3.3 Legalization and Diario structure (Arts. 438, 446)

- **SV-CML-FR-022:** The system shall record, per statutory register, the
  Art. 438 legalization data: physical form (*libros empastados* or *hojas
  separadas*), folioed sheets; authorization by the *Contador Público
  autorizado* appointed by the merchant — for *comerciantes sociales*, by
  the *Auditor Externo* with the *aval* (endorsement) of the
  *administrador* designated in the *estatutos*; sheets numbered and
  stamped; and the first-leaf *razón* content (merchant name, object,
  number of sheets authorized, place and date of delivery). The system
  tracks these as registry-side facts (who/when/folios) on the register
  record — the physical act is external; the vigilance office's
  fiscalization and sanctions (against Auditor, merchant or
  administrators) are recorded as compliance exposure, not computed.
  (LB-004; EVID-213)
- **SV-CML-FR-023:** The system shall support the Art. 446 Diario
  structure: the FIRST *partida* (entry) of the Diario is the opening
  balance showing the merchant's economic and financial situation at the
  start of operations, stating the *activo*, *pasivo* and capital accounts
  (Odoo native opening entry); subsequent entries follow in chronological
  order for own- and third-party-account operations; and the Diario and
  Mayor may be constituted by SEVERAL registers or kept in a SINGLE
  combined register, provided the Code's requirements are met (multiple
  Odoo journals are legal; the opening-partida invariant applies to the
  merchant's first journal).
  (LB-007; EVID-214)

### 3.4 No-alteration regime and extension (Arts. 439-440)

- **SV-CML-FR-024:** The system shall implement the Art. 439 no-alteration
  regime as the CC root of ledger discipline: operations entered DAILY,
  clear, chronological, *sin blancos, interpolaciones, raspaduras, ni
  tachaduras* (no blanks, interpolations, scrapings or strike-throughs)
  and showing no signs of alteration; errors or omissions saved
  immediately below upon notice, clearly explaining what they consist of
  and extending the concept as it should have been written; and the
  *asiento de rectificación* (rectification entry) made IMMEDIATELY after
  the error is discovered or the omission recognized. The Odoo-side
  mechanics — posted-entry immutability, lock-by-transmission-state and
  correction-as-reversal-entry — are owned by the e-invoicing wave
  (`02_transmission.md` §3.11, SV-EINV-FR-159..164) and are consumed BY
  ID here as the kin implementation; this FR's own surface is the
  CC-anchored requirement (chronology, no-gaps, same-day rectification
  stamp, error explanation) that those invariants satisfy for the fiscal
  ledger. (LB-005; EVID-213)
- **SV-CML-FR-025:** The system shall extend the Arts. 436/438/439
  disciplines to EVERY statutory register merchants must keep by law, even
  non-accounting ones (Art. 440): castellano/USD/in-country keeping,
  legalization data and the no-alteration regime apply to society books
  (*actas* — minutes —, registro de socios/accionistas, capital-variable movements —
  content owned by `04_society-types.md`), the agentes' *libro especial*
  (Art. 388, `06_commercial-agents.md`) and any other statutory register —
  each register record inheriting the §3.1/§3.3/§3.4 discipline flags.
  (LB-006; EVID-213)

### 3.5 Labor-obligation provision (Art. 447)

- **SV-CML-FR-026:** The system shall provide the Art. 447 accounting
  anchor: a *provisión o reserva* (provision or reserve) must be
  constituted for compliance with the obligations the merchant owes its
  personnel by virtue of law or employment contracts. Provision account,
  computation method and payroll-side accruals are owned by the payroll
  and chart-of-accounts waves (consumed by pointer); this FR records the
  CC obligation and its presence check on the obligation map
  (SV-CML-FR-005 II kin), with no value-level rule derived here.
  (LB-008; EVID-214)

### 3.6 Simplified book for sub-US$12,000 individuals (Art. 452)

- **SV-CML-FR-027:** The system shall provide the Art. 452 simplified
  ledger profile for individual merchants whose *activo en giro* is below
  US$12,000 (dated-but-current threshold, §2): ONE bound book entering
  SEPARATELY expenses, purchases and sales, in cash and on credit, plus an
  annual *balance general* of all operations specifying *activo* and
  *pasivo* values — no Diario/Mayor formality. The profile coexists with
  the Art. 15 exemption profile (SV-CML-FR-004: below-US$12,000
  individuals keep only obligation 411-IV): Art. 15 removes the full
  Libro Segundo professional-obligation set while Art. 452 installs the
  simplified book for the same threshold population — both texts are
  current under SOQ-22; the simplified book is the survivor of the
  obligation, not a contradiction (working reading — the Art. 15 Título I
  exemption for the below-US$12,000 single-book population coexists with
  Art. 452's simplified book; no corpus instrument arbitrates the pairing).
  (LB-010; EVID-216)

### 3.7 Retention matrix (Arts. 451, 454, 455; D.L. 426 Art. 26; CT 147) — SOQ-28 deliverable

- **SV-CML-FR-028:** The system shall implement the SOQ-28 CANONICAL
  RETENTION MATRIX — the single objects-×-retention table every other
  file consumes by id (never restated); for each retained object class the
  effective floor is the LONGEST applicable row:

  | Row | Object class | Regime | Retention floor | Clock anchor | Authority |
  |-----|--------------|--------|-----------------|--------------|-----------|
  | a | Statutory books and registers of the giro: Diario, Mayor, Estados Financieros registro, additional accounting registers (Art. 435), every Art. 440 statutory register (incl. society books and the Art. 452 simplified book) | CC | 10 years, extended up to 5 years after liquidation of ALL the merchant's mercantile businesses; binds merchants AND their heirs/successors | Art. 451 fixes no express start; system uses register close (last entry) as the conservative anchor — OQ-003 | LB-009 (+LB-006); EVID-215 |
  | b | *Facturas anexas*: received letters, telegrams and facturas + copies of issued ones serving as accounting *comprobantes* (supporting/voucher documents; DTE-era: issued/received DTEs, their RG and declaration-annex files are this factura/comprobante class — row e owns the DTE-specific mechanics) | CC | same clock as row a — *anexas a la contabilidad* (incl. the post-liquidation extension) | via Art. 454 → Art. 451; per-document emission anchor for the copy/received date | LB-011; EVID-215 |
  | c | Media migration of records (microfilm, optical disc, any archival medium) | CC | original-medium preservation required ≥24 months from emission before migrating; notarized copy (certified by *Notario* after confrontation with originals) carries the SAME probatory value as the original | emission date + 24 months | LB-012; EVID-215 |
  | d1 | AML transaction records (of *sujetos obligados*, obligated subjects) | AML | ≥15 years — the uniform W12 rule; the pre-2025-10-17 law's 5y-docs/15y-registers split is DEAD | finalization of EACH transaction (operation end) | LB-013; EVID-244 |
  | d2 | AML client-identification data and account files (of *sujetos obligados*) | AML | ≥15 years, same uniform rule | termination of the commercial relation or account closure (relation end) | LB-013; EVID-244 |
  | e | DTE and RG electronic documents | CT 147 as reformed (D.L. 487-2022) | 10 years, exact structure and format conserved (incl. untransmitted and rejected documents) — mechanics owned by e-invoicing, cited by id, never restated | GENERATION date (not seal date) | e-invoicing `04_signing_delivery.md` §3.7 SV-EINV-FR-152..158 (esp. FR-154/155/156); D3 |

  Rules under the table: (i) LONGEST-PER-OBJECT GOVERNS — an object's
  effective *retention-until* = max of all applicable rows (e.g. a
  sujeto obligado's invoice: AML 15y > CC 10y > DTE 10y ⇒ 15y; its
  client-ID file: 15y from relation end even after the relation ends).
  (ii) Applicability: rows a-c bind every merchant (and heirs/successors);
  rows d1/d2 bind sujetos obligados only — applicability fed by
  `10_aml-compliance.md` by id when it lands (no AML-profile logic
  here); row e binds DTE emitters. (iii) Regime version: the AML rows
  are D.L. 426 (effective 2025-10-17); records predating the cutover
  are conservatively kept 15y too (longest-per-object discipline).
  (iv) D3 AUTHORITY NOTE: the SaaS archive tiers
  (`shared/docs/saas-thin-client-architecture.md` D3 — Tier A mandatory
  local mirror, Tier B paid hosting) MUST satisfy this matrix; Tier B is
  a convenience atop the emitter's non-delegable duty and never shortens
  any row; the Tier A local mirror satisfies row e's conservation and
  rows a/b's in-country posture (FR-020). (v) Sanction: Art. 451
  inciso 2 — the Registrador refuses or cancels the matrícula of
  violators (cross-ref SV-CML-FR-012).
  (LB-009; LB-011; LB-012; LB-013; EVID-215/244)
- **SV-CML-FR-029:** The system shall compute and enforce per-object
  retention from the FR-028 matrix: every retained object (journal entry,
  invoice/comprobante, statutory register, AML client file, archived DTE)
  carries its applicable regime tags and a computed *retention-until* =
  the longest applicable row's clock anchor plus its period; premature
  purge shall be refused with the governing row identified; the row-a
  post-liquidation extension shall extend every CC-row floor to five
  years after liquidation of all mercantile businesses upon the
  liquidation event (lifecycle event consumed from
  `05_society-lifecycle.md` by pointer when it lands); heirs/successors
  continuity is recorded as the retention owner's succession note; and
  the Art. 451 sanction exposure surfaces as a warning linked to
  SV-CML-FR-012's cancellation machinery. DTE purge protection is owned
  by SV-EINV-FR-155 (consumed by id; not reimplemented).
  (LB-009; LB-011; LB-013; EVID-215/244)
- **SV-CML-FR-030:** The system shall implement the Art. 455 media-
  migration guard: no record's original medium may be discarded or
  replaced by microfilm/optical/other archival means before 24 months
  have elapsed from its emission date (eligibility date computed per
  object); once eligible, the migrated copy carries the SAME probatory
  value as the original ONLY if certified by a Notario after
  confrontation with the originals — the notarial certification is
  recorded as document metadata (external act; the system never
  self-certifies equivalence), and falsity falls to the Penal Code.
  DTE objects are governed by row e's CT 147 exact-structure duty
  (owned by e-invoicing by id) — the Art. 455 equivalence route is not
  applied to them (reading → OQ-004). (LB-012; EVID-215)

## 4. Data Model

Layer semantics: bookkeeping is Odoo-native — all entities live in the
client (wave default `odoo`; see §5). Legalization and retention track
external facts (who authorized, until when, under which regime); the
system does not emulate the vigilance office, the Notary or the registry.

**Accounting posture (on res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_cml_accounting_system | char | generally accepted system basis (informational; approval = public audit function) | FR-018 |
| res.company | sv_cml_registers_set | computed list | estados_financieros · diario · mayor + exigency/law additions | FR-018 |
| res.company | sv_cml_electronic_notice_on | date | Art. 435 notice to the vigilance office (mechanics = OQ-001) | FR-019 |
| res.company | sv_cml_ledger_language · sv_cml_ledger_currency | const | castellano · USD (Colones alternative = historical remnant, §2) | FR-020 |
| res.company | sv_cml_keeper_profile | select | self_below_12k · own_appointee_below_12k · qualified_mandatory | FR-021 |
| res.company | sv_cml_simplified_book | boolean (computed) | Art. 452 profile (<US$12k individuals; coexists with SV-CML-FR-004 Art. 15 profile) | FR-027 |
| res.company | sv_cml_labor_provision_account | many2one account.account | Art. 447 anchor; method owned by payroll/COA waves (pointer) | FR-026 |

**Register legalization (l10n_sv_commerce.book):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.book | register_kind | select | diario · mayor · estados_financieros · libro_simplificado · sociedad_register · agente_libro_especial · otro | FR-022, FR-025 |
| l10n_sv_commerce.book | physical_form | select | empastado · hojas_separadas · electronico | FR-022 |
| l10n_sv_commerce.book | folio_from · folio_to | integer | folioed/numbered/stamped sheets | FR-022 |
| l10n_sv_commerce.book | authorized_by_kind · authorized_by | select · many2one res.partner | contador_publico (individuals) · auditor_externo (sociedades) | FR-022 |
| l10n_sv_commerce.book | aval_administrador | many2one res.partner | sociedades: estatutos-designated administrador endorsement | FR-022 |
| l10n_sv_commerce.book | razon_merchant · razon_object · razon_sheets · razon_place · razon_delivered_on | char · integer · date | first-leaf razón content (Art. 438 inciso 2) | FR-022 |
| l10n_sv_commerce.book | sv_cml_discipline_flags | computed | castellano/USD/in-country + no-alteration + legalization apply (Art. 440 extension) | FR-025 |
| account.move | opening partida | native | first Diario partida = opening balance (activo/pasivo/capital); no custom field — invariant + Odoo opening entry | FR-023 |

**Retention matrix (l10n_sv_commerce.retention):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.retention | object_ref | reference | journal entry · invoice/comprobante · statutory register · client-ID file · DTE archive object | FR-028, FR-029 |
| l10n_sv_commerce.retention | regimes | tags | cc_451_register · cc_454_anexas · aml_426_26_txn · aml_426_26_client · dte_ct147 (dte row mechanics owned by SV-EINV-FR-152..158, cited) | FR-028 |
| l10n_sv_commerce.retention | anchor dates | date | last-entry/close (a) · received/issued date (b) · emission date (c) · transaction end (d1) · relation end (d2) · generation date (e, owned by SV-EINV-FR-155) | FR-028, FR-029 |
| l10n_sv_commerce.retention | retention_until | computed date | max of applicable rows; liquidation extension (+5y) applied on lifecycle event | FR-029 |
| l10n_sv_commerce.retention | media_migration_eligible_on | date | emission + 24 months (Art. 455) | FR-030 |
| l10n_sv_commerce.retention | notarized_copy_ref | document reference | Notario certification after confrontation = probatory equivalence | FR-030 |
| res.company | sv_cml_sujeto_obligado_applicability | consumed | AML-row applicability fed by `10_aml-compliance.md` by id (no AML profile here) | FR-028 |

## 5. Odoo Mapping

Layer semantics for this wave: bookkeeping is Odoo-native — every FR maps
`odoo`; none of them touch DTE generation/transformation (an
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`), so no `saas` rows are
introduced. The SaaS side is constrained, not implemented, by FR-028's D3
authority note. Model names are stable across Odoo 17/18/19/20; no
version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-018 | odoo | res.company | sv_cml_accounting_system, sv_cml_registers_set | Register set = Odoo journals + financial-statement surfaces; additions tracked |
| FR-019 | odoo | res.company | sv_cml_electronic_notice_on | Electronic ledger legal without paper duplication given notice; notice mechanics = OQ-001 config slot |
| FR-020 | odoo | res.company | sv_cml_ledger_language/currency | In-country posture satisfied by client-held DB (D2 split); Tier B residency → OQ-002 (D3 legal-review fold) |
| FR-021 | odoo | res.company | sv_cml_keeper_profile | ≥US$12k individuals + all sociedades ⇒ qualified keeper; Art. 80 Reglamento CT accreditation = taxation-wave pointer; threshold dated-but-current (§2) |
| FR-022 | odoo | l10n_sv_commerce.book | legalization + razón fields | Registry-side facts tracked; physical act external; vigilance sanctions recorded as exposure |
| FR-023 | odoo | account.move (journal) | opening entry invariant | First partida = opening balance; several-journals and single-register shapes both legal (Art. 446 III) |
| FR-024 | odoo | account.move | (kin: SV-EINV-FR-159..164 by id) | CC root (chronology, no-gaps, immediate rectification entry + explanation); Odoo immutability mechanics owned by e-invoicing §3.11 — never restated |
| FR-025 | odoo | l10n_sv_commerce.book | sv_cml_discipline_flags | Art. 440 extension to society books etc.; content owned by 04/06 files |
| FR-026 | odoo | res.company + account.move | sv_cml_labor_provision_account | Art. 447 anchor; computation owned by payroll/COA waves (pointer) |
| FR-027 | odoo | res.company | sv_cml_simplified_book | Art. 452 single bound book + annual balance; coexists with SV-CML-FR-004 Art. 15 profile |
| FR-028 | odoo | l10n_sv_commerce.retention | regimes/anchors/retention_until | SOQ-28 canonical matrix; consumed by 10_aml-compliance.md and D3 by id; longest-per-object governs |
| FR-029 | odoo | l10n_sv_commerce.retention | retention_until, purge guard | Liquidation +5y extension hook (05 pointer); DTE purge protection = SV-EINV-FR-155 by id |
| FR-030 | odoo | l10n_sv_commerce.retention | media_migration_eligible_on, notarized_copy_ref | 24-month original-medium guard; notarial equivalence as metadata; DTE carve-out → OQ-004 |

Version-regime notes (D12): the US$12,000 thresholds (Arts. 437/452) are
2008-reform (29) USD code text — dated-but-current under the SOQ-22
residual watch (§2); the AML matrix rows carry the D.L. 426 regime
(effective 2025-10-17 — version + effective date recorded; the dead
1998-law 5y/15y split is never cited); the DTE row's 10y-from-generation
regime is CT 147 as reformed by D.L. 487-2022 (owned by e-invoicing LB,
cited by id). No other dated values live in this file; the vigilance-
office notice mechanics carry no shipped defaults (OQ-001).

## 6. Acceptance Criteria

- **AC-001:** Given a merchant keeping its accounting entirely in the
  Odoo electronic ledger with a recorded vigilance-office notice date,
  when its bookkeeping compliance posture is evaluated, then electronic
  bookkeeping is legal with NO paper duplication of the registers
  (FR-018, FR-019).
- **AC-002:** Given a posted Diario entry containing an error discovered
  the same day, when the correction is recorded, then a rectification
  *asiento* is stamped immediately after discovery, carrying a clear
  explanation of the error and the concept as it should have been
  written, while the original entry shows no blank, interpolation,
  scraping or strike-through (FR-024, kin SV-EINV-FR-159..160 by id).
- **AC-003:** Given a received *factura* and the copy of an issued one,
  both serving as accounting comprobantes, when retention is computed,
  then both are classified *anexas a la contabilidad* with the row-b
  10-year floor (longest applicable row applied) and purge is refused
  before the computed *retention-until* (FR-028, FR-029).
- **AC-004:** Given a *sujeto obligado* whose client relation ended in
  2026 and who performed a transaction in 2024, when retention is
  computed, then the transaction record is kept 15 years from the 2024
  operation end and the client-ID file 15 years from the 2026 relation
  end — the transaction record OUTLIVES the relation, longest-per-object
  with different anchors (FR-028).
- **AC-005:** Given a paper register emitted 2026-01-15, when a
  microfilm migration is attempted on 2027-06-01, then it is blocked
  (emission + 24 months = 2028-01-15 not reached); attempted again on
  2028-02-01, then it is eligible and the notarized-copy reference is
  recorded as the probatory-equivalence condition (FR-030).
- **AC-006:** Given a *comerciante individual* with *activo en giro*
  US$9,000, when the accounting profile applies, then the simplified
  single-bound-book profile (expenses/purchases/sales, cash and credit
  separate + annual balance general) replaces the full register
  formality while the Art. 15 exemption profile keeps only obligation
  411-IV (FR-027; SV-CML-FR-004).
- **AC-007:** Given a *sociedad* legalizing its Diario, when the
  legalization record is saved, then the authorizer is the Auditor
  Externo with the estatutos administrador's *aval*, the folio range is
  recorded, and the first-leaf *razón* fields (merchant, object, sheet
  count, place, delivery date) are complete (FR-022).
- **AC-008:** Given a merchant's first Diario, when the first entry
  posts, then it is the opening balance partida stating activo, pasivo
  and capital accounts, and subsequent entries follow chronologically;
  splitting the Diario and Mayor across several Odoo journals remains
  legal (FR-023).
- **AC-009:** Given a sociedad's actas book (a non-accounting statutory
  register), when register discipline is evaluated, then castellano/USD/
  in-country keeping, legalization data and the no-alteration regime all
  apply to it via the Art. 440 extension flags (FR-025).
- **AC-010:** Given a merchant recorded as liquidating all its mercantile
  businesses in 2030, when the lifecycle event applies, then every CC-row
  retention floor extends to 2035 (liquidation + 5 years) and the
  Art. 451 sanction exposure surfaces linked to the matrícula-cancellation
  machinery (FR-029; SV-CML-FR-012).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | The *Oficina que ejerce la vigilancia del Estado* (state watchdog office) notice mechanics for Art. 435 electronic bookkeeping — office identity, form and channel of the *del conocimiento* notice — are not in the corpus (Arts. 443-444 point to the Consejo de Vigilancia de la Profesión de Contaduría Pública y Auditoría for valuation criteria; the vigilance office's own ley is absent). FR-019 exposes the notice as a dated compliance slot with NO computation; acquire the vigilance-office law if notice mechanics ever need automation. | no | Takumi S5 (sources watch) | open |
| OQ-002 | Art. 436 in-country keeping vs cloud custody: the client-held Odoo database (system of record) satisfies in-country keeping, and the Tier A mandatory local mirror (SV-EINV-FR-154) keeps the DTE archive local; residual = whether SaaS Tier B hosted DTE copies alone would satisfy Art. 436 for *facturas anexas* — product keeps Tier A mandatory so the question never binds. Data-residency review is folded into D3's ToS/legal-review work item (`shared/docs/saas-thin-client-architecture.md`). | no | Takumi + legal review | open |
| OQ-003 | Art. 451 fixes no express clock anchor for the 10-year books retention. The matrix uses register close (last entry) as the conservative anchor; registry/supervisory practice may compute from fiscal-year close or another anchor — verify when a vigilance-office or CNR source lands. | no | Takumi S5 | open |
| OQ-004 | Art. 455 notarized-copy probatory equivalence vs CT 147 exact-structure conservation for DTE objects: working reading = the DTE row (e) governs electronic documents (original medium = the sealed JSON structure; SV-EINV-FR-155 conserves it exactly), while Art. 455 governs CC-side records; the equivalence route is not applied to DTEs. Confirm with the taxation/DTE corpus owners at implementation. | no | Takumi S5 + S1 owners | open |
