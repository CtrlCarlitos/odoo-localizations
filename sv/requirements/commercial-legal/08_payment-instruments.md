# SV — Commercial-legal — Payment instruments: títulos valores, pagaré, cheque, mora interest and the prescription matrix (C8; usura Art. 960-A + cheque truncation awareness per 110_/112_)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | commercial-legal |
| Status  | draft (W23 fold-in, in review) |
| Authors | Takumi synthesis wave 5 (S5 commercial-legal) + W23 T4 |
| Updated | 2026-08-23 |

## 1. Purpose

This file defines the El Salvador payment-instrument and
obligation-remedy layer of the Código de Comercio (Commercial Code, CC):
the *títulos valores* (negotiable instruments / securities) general
regime of Arts. 623-653 — the Art. 623 literal-and-autonomous-right
definition, the Art. 625 five formal requisites with their
domicilio-filling and multiple-place defaults, the Art. 626 castellano
(Spanish-language) rule, the Art. 628 words-over-figures and
lower-sum rules with *máquina protectora* (protective typing machine)
precedence, the Art. 638 deadline conventions (inhábil-day extension,
intermediate-feriados-count, exclude-the-start-day), the Art. 649
one-year enrichment action and the Art. 650 *salvo buen cobro*
(subject to collection) presumption; the *pagaré* (promissory note)
regime of Arts. 788-792 — the six-field content, the Art. 789
*vista/domicilio* (at-sight/domicile) defaults, the Art. 790
one-year vista-plazo presentation, the Art. 791 domiciled-protest
caducidad rule and the Art. 792 incorporated interest-rate fallback
ladder; the *cheque* (check) regime of Arts. 793-838 — the seven-field
form with MANDATORY *número y serie* (number and series) capture, the
Art. 794 *raspaduras* (scraped alterations) void rule, the bank-supplied
formulario discipline of Art. 806, the always-*a-la-vista* rule and the
Art. 805 presentation surface with its 72-hour agency respite, the
Art. 808 presentation clocks (15 days same-plaza / 1 month national /
3 months cross-border), the Art. 815/816 protest-or-bank-note rule with
its 15-day limit, the Art. 819 caducidad cascade, the Art. 820 one-year
cambiaria prescription, the Art. 811/821 minimum-20% bank-refusal
indemnity, and the special-cheque taxonomy of Arts. 822-837 (*cruzado*,
*para abono en cuenta*, *certificado*, *de viajero*, *limitado*,
*circular*, *de caja o de gerencia*) as payment-configuration metadata
with their own clocks (certified 6 months, traveller 2 years, circular
6 months); the mora-interest and solidarity rules of Arts. 960-962 —
pactado-then-legal interest fallback, the value-of-the-thing base, the
Economía-published legal rate as DATED CONFIG (SOQ-26 — never
hardcoded) and the solidarity of *codeudores y fiadores* (co-debtors
and guarantors); the **mercantile prescription matrix of Art. 995
(verbatim)** — 6 months cuenta-corriente rectification / 1 year
cheque-letra-regreso-vicios-transporte-corporate-nullity-admin-liability
/ 2 years compraventa-sociedad-suministro-comisión etc. / 5 years
credit contracts from the LAST RECOGNITION — with recognition-event
stamping and the Arts. 996-998 caducidad no-suspension regime, as the
receivable/payable aging defaults table; and the proof regime of
Arts. 999-1003 — *facturas* (invoices) and *registros contables*
(accounting records) as statutory proof of mercantile obligations, with
legally-kept books winning the Art. 1002 evidentiary priority.

It owns the prescription-matrix DEFAULTS table and the
recognition-event anchor for the whole localization: later
commercial-legal files (`09_sales-contracts.md` — vicios 1y and the
compraventa/suministro/comisión 2y families; the society files
consuming the corporate-nullity and admin-liability 1y rows) and the
receivables/payable aging surfaces CONSUME SV-CML-FR-160/161 by id and
never restate the Art. 995 terms.

It does **not** cover: merchant status, matrícula and the registry
architecture (`01_merchant-registration.md`); book discipline,
legalization and the retention matrix (`02_accounting-books.md` —
SV-CML-FR-025 discipline flags and SV-CML-FR-028 matrix consumed by
id: the factura-as-*anexa* retention row and the legally-kept-book
state that powers the Art. 1002 priority here); the annual statement
cycle (`03_financial-statements.md`); society types and reserves
(`04_society-types.md`); society lifecycle (`05_society-lifecycle.md`);
commercial agents (`06_commercial-agents.md`); the empresa mercantil
and EIRL (`07_empresa-mercantil-eirl.md`); sales contracts, warranties
and INCOTERM-analog clauses (`09_sales-contracts.md`, future — its
defect/warranty clocks cite this file's matrix by id, never the
reverse); AML compliance (`10_aml-compliance.md`); and the
letra-de-cambio chapter mechanics (Arts. 702-787 detail — skimmed in
the evidence; only the general chapter and the Art. 995-II regreso
prescription row are used here, §3.9/OQ-002). The días-hábiles
arithmetic is OWNED by the fiscal-reporting wave
(SV-FREP-FR-202..204, `sv/requirements/fiscal-reporting/08_filing-calendar.md`
§3.3) and consumed by id; the DTE archive surfaces are owned by the
e-invoicing wave (SV-EINV-FR-154/155) and cited by pointer only.

## 2. Legal Basis

Authority order (binding, per master evidence index S5): the Código de
Comercio = **07_** (D.L. Nº 671, 8-may-1970, D.O. 140 T.228 31-jul-1970;
29 listed reforms, last = D.L. 641-2008) — **STALE-PRINT RULING (SOQ-22,
W22 falsification 2026-08-23)**: the W12 "no post-2008 CC structural
reform" verdict is FALSIFIED — the asamblea por-anios census found and
this corpus now OWNS the six-instrument post-2008 reform set 109_-114_
(EVID-407..412: bearer-share suppression, usura, SAS, cheque
truncation, SAS-gratuidad chain); 07_/73_ consolidation texts are STALE
for the reformed articles, and THIS file's zone is hit at **Art. 960
(110_ D.L. 295-2022 — inciso tercero added + Art. 960-A intercalated;
awareness LB-028 below + the FR-158 note, §3.6) and the cheque
chapter's new Sección "F" TRUNCAMIENTO DE CHEQUES, Arts. 838-A..838-E
(112_ D.L. 972-2024 — awareness LB-029 below; no FR mechanics)** —
FOLDED IN W23 T4 as awareness rows only; every CC clock in this file
(the Art. 638 conventions, the pagaré/cheque clocks of Arts.
790-792/805/808/815-821/826/829-831/835 and the Arts. 995-998
prescription/caducidad matrix) is OUTSIDE both reforms' touch — the
07_ print stands current there. Census residual (negative watch):
por-anios carries no cards for 2010/2012-2015 and 2019 looks partial —
a 2009-2019 CC reform cannot be fully excluded from enumeration
alone; the six owned instruments carry the KNOWN post-2008 surface.
Verbatim text below is copied from the 07_ evidence file (EVID-225/226)
and — the evidence abbreviates several operative articles (625 final
inciso, 793, 806, 808, 815, 819-821, 822-837, 960, 995-1002) — from
the extraction txt `sv/.extractions/07_Codigo_Comercio.pdf.txt`
(citable per standing ruling; page pointers = txt PAGE markers); the
reformed-in-file articles quote the 110_/112_ reform texts directly
(LB-028/029 below; txts
`sv/.extractions/110_Reforma_CodigoComercio_DL295_2022_Asamblea.pdf.txt`
and `sv/.extractions/112_Reforma_CodigoComercio_DL972_2024_Asamblea.pdf.txt`,
spacing artifacts cleaned intra-word only). Editorial provenance notes:
(i) the print carries an authentic-interpretation NOTE under Art. 625
(D.L. Nº 389, 20-abr-2001, D.O. 90 T.351 16-may-2001) transcribing the
final inciso's authoritative reading — recorded in LB-001's gloss, not
quoted as article text; (ii) the Y2K transitional note printed under
Art. 794 (D.L. Nº 809, 23-dic-1999 — expired by its own terms) is not
carried; (iii) reform tick marks are stripped from quotations with
provenance noted here (Art. 995-IV carries print mark "(25)"; the
Art. 1004-1012 derogation marker retains ordinal "(21)" in LB-027
because the ordinal IS the substantive content). Truncation markers
inside LB quotations label every omission explicitly.

Rate discipline (**SOQ-26**, established by this file, carrying 07_
OQ-6): the mercantile LEGAL INTEREST RATE is DATED DATA fixed
periodically by the Economía office (print nomenclature "Secretaría de
Economía", Art. 960 final inciso) — the current rate instrument is
outside the corpus, so the rate is a dated configuration slot with NO
shipped default; never hardcode (OQ-001). Currency discipline
(SOQ-29): no colones-denominated value and no dated monetary threshold
occurs in this article set — the 20% indemnity floors (Arts. 821/830)
and the interest rules are currency-neutral proportions, and every
clock here is a day/month count, under the SOQ-22 residual watch.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Comercio, Art. 623: "Son títulosvalores los documentos necesarios para hacer valer el derecho literal y autónomo que en ellos se consigna." Art. 625 (encabezamiento, ordinales I-V e inciso final): "Sin perjuicio de lo dispuesto para las diversas clases de títulosvalores, tanto los reglamentados por la ley como los consagrados por el uso, deberán tener los requisitos formales siguientes: I.- Nombre del título de que se trate. II.- Fecha y lugar de emisión. III.- Las prestaciones y derechos que el título incorpora. IV.- Lugar de cumplimiento o ejercicio de los mismos. V.- Firma del emisor." "Si no se mencionare el lugar de emisión o el de cumplimiento de las prestaciones o ejercicio de los derechos que el título incorpora, se tendrá como tal, respectivamente, el que conste en el documento como domicilio del librador y el del obligado, o el lugar que aparezca junto al nombre de cada uno, en caso de no expresarse domicilio alguno; y si en el título se consignan varios lugares, se entenderá que el tenedor puede ejercitar sus derechos y el obligado cumplir las prestaciones en cualquiera de ellos." | Negotiable instruments are the documents NECESSARY to assert the LITERAL AND AUTONOMOUS right consigned in them. Without prejudice to the provisions for the diverse classes of títulos valores — both those regulated by law and those consecrated by usage — they must bear the formal requisites: I. the name of the title; II. date and place of emission; III. the prestations and rights the title incorporates; IV. place of performance or exercise; V. the emitter's signature. If the place of emission or of performance is not mentioned, the one appearing in the document as the LIBRADOR's (drawer's) domicile — and the OBLIGADO's (obligor's) — is taken as such respectively, or the place appearing next to each one's name absent any domicilio; and if SEVERAL places are consigned, the TENEDOR (holder) may exercise his rights and the obligado perform the prestations in ANY of them (the print's D.L. 389-2001 authentic interpretation confirms this reading) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 623/625 p.112 (EVID-225; txt PAGE 112) |
| LB-002 | Código de Comercio, Art. 626: "Los títulosvalores emitidos en El Salvador, deberán estar escritos en castellano, pero podrán contener, además, una traducción de su texto a otro idioma." | Títulos valores EMITTED IN EL SALVADOR must be written in SPANISH, though they may additionally contain a translation of their text into another language | `sv/sources/07_Codigo_Comercio.pdf` | Art. 626 p.113 (EVID-225; txt PAGE 113) |
| LB-003 | Código de Comercio, Art. 628: "El títulovalor que tuviere su importe escrito a la vez en palabras y cifras, valdrá, en caso de diferencia, por la suma escrita en palabras. Si la cantidad apareciere más de dos veces en palabras o en cifras, el documento valdrá, en caso de diferencia, por la suma menor consignada." "Se permite el uso de máquinas protectoras para asegurar el importe del títulovalor o las firmas que lo calcen. Siempre que se haga uso de esta facultad, la cantidad marcada por la máquina protectora tendrá preferencia sobre las demás." | A título valor bearing its amount written BOTH in words and figures valdrá, on difference, for the sum WRITTEN IN WORDS. If the quantity appears MORE THAN TWICE in words or figures, the document valdrá, on difference, for the LOWER sum consigned. Use of PROTECTOR MACHINES to secure the amount or the signatures is permitted; whenever this faculty is used, the quantity MARKED BY THE PROTECTOR MACHINE PREVAILS over the others | `sv/sources/07_Codigo_Comercio.pdf` | Art. 628 p.113 (EVID-225; txt PAGE 113) |
| LB-004 | Código de Comercio, Art. 638: "Cuando los actos que haya de realizar obligatoriamente el tenedor de un títulovalor deba efectuarlos dentro de un plazo cuyo último día fuere inhábil, el término se entenderá prorrogado hasta el primer día hábil siguiente. Los días feriados que haya en el intermedio, se contarán en el plazo. Ni en los términos legales ni en los convencionales se comprenderá el día que les sirve de punto de partida." | When the acts the HOLDER of a título valor is obliged to perform must be effected within a term whose LAST DAY IS INHÁBIL (non-business), the term is understood EXTENDED TO THE FIRST FOLLOWING HÁBIL DAY. Intermediate holidays COUNT in the term. Neither legal nor conventional terms comprise THE DAY SERVING AS THEIR POINT OF DEPARTURE (exclude-the-start-day convention) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 638 p.114 (EVID-225; txt PAGE 114) |
| LB-005 | Código de Comercio, Art. 649: "Extinguida por caducidad o por prescripción la acción cambiaria contra el emisor, el tenedor del títulovalor que carezca de acción contra éste, y de acción cambiaria o causal contra los demás signatarios, puede exigir al emisor la suma con que se enriqueció en su daño. Esta acción prescribe en un año contado desde el día en que caducó o prescribió la acción cambiaria." Art. 650: "Los títulosvalores dados en pago se presumen recibidos 'salvo buen cobro'." | Once the cambiaria (bill-of-exchange) action against the EMITTER is extinguished by caducidad or prescription, the holder lacking action against him and lacking cambiaria or CAUSAL action against the other signatories may demand from the emitter THE SUM WITH WHICH HE ENRICHED HIMSELF to the holder's detriment. This ENRICHMENT ACTION PRESCRIBES IN ONE YEAR counted from the day the cambiaria action caducated or prescribed. Títulos valores GIVEN IN PAYMENT are PRESUMED received "SALVO BUEN COBRO" (subject to collection) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 649-650 p.115 (EVID-225; txt PAGE 115) |
| LB-006 | Código de Comercio, Art. 788: "El pagaré es un títulovalor a la orden que debe contener: I.- Mención de ser pagaré, inserta en el texto. II.- Promesa incondicional de pagar una suma determinada de dinero. III.- Nombre de la persona a quien ha de hacerse el pago. IV.- Epoca y lugar del pago. V.- Fecha y lugar en que se suscriba el documento. VI.- Firma del suscriptor." Art. 789: "Si el pagaré no menciona fecha de vencimiento, se considerará pagadero a la vista; si no indica lugar de pago, se tiene como tal el domicilio de quien lo suscribe." | The pagaré (promissory note) is a título valor A LA ORDEN (to order) that must contain the SIX fields: I. mention of being a pagaré, inserted in the text; II. UNCONDITIONAL promise to pay a determined sum of money; III. name of the person to whom payment is to be made; IV. epoch (maturity) and place of payment; V. date and place of subscription; VI. the subscriber's signature. If the pagaré mentions NO maturity date it is considered PAYABLE AT SIGHT (a la vista); if it indicates no place of payment, the DOMICILE OF THE SUBSCRIBER is taken as such | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 788-789 pp.137-138 (EVID-225; txt PAGE 137-138) |
| LB-007 | Código de Comercio, Art. 790: "Los pagarés exigibles a cierto plazo de la vista, deben presentarse dentro del año que siga a su fecha. La presentación sólo tiene el efecto de fijar la fecha del vencimiento y se comprueba por acta ante Notario." Art. 791: "El pagaré domiciliado debe presentarse para su pago a la persona indicada como pagador diputado, y a falta de designación, al suscriptor mismo, en el lugar señalado como domicilio." "El protesto por falta de pago debe levantarse en el domicilio fijado en el documento, y su omisión, cuando la persona que haya de hacer el pago no sea el suscriptor, producirá la caducidad de las acciones que competan al tenedor contra los obligados en vía de regreso." Art. 792 (incisos 2 y 3; inciso 1 omitido — lista de artículos de la letra de cambio incorporados al pagaré, mecánica bancaria, §3.9/OQ-002): "Para los efectos de los artículos 768 y 769 el tenedor podrá reclamar los réditos caídos; el descuento del pagaré no vencido se calculará al tipo de interés pactado en éste, o, en su defecto, al tipo legal; los intereses moratorios se computarán al tipo estipulado para ello; a falta de esta estipulación, al tipo de rédito fijado en el documento; y en defecto de ambos, al tipo legal." "El suscriptor se considerará como aceptante para los efectos de las disposiciones enumeradas antes, salvo que se ejercite en su contra la acción causal o la de enriquecimiento sin causa, casos en los que se equipara al librador." | Pagarés exigible at a certain term FROM SIGHT must be presented WITHIN THE YEAR FOLLOWING THEIR DATE; presentation only fixes the maturity date and is proved by notarial acta. A DOMICILED pagaré is presented for payment to the person indicated as PAGADOR DIPUTADO (appointed payer) — absent designation, to the SUBSCRIBER himself at the place signaled as domicilio. The protest for non-payment must be raised at the domicile fixed in the document; its OMISSION, when the payer is not the subscriber, produces CADUCIDAD of the holder's REGRESO actions against the obligados. Art. 792: accrued interest recoverable; discount of an unmatured pagaré at the PACTADO (agreed) rate, IN DEFAULT at the LEGAL rate; mora interest at the rate STIPULATED for it, absent stipulation at the document's yield rate, and in default of both at the LEGAL rate (the pactado→legal fallback ladder). The subscriber is treated as ACEPTANTE (acceptor) for the enumerated provisions — save when the causal or enrichment action is exercised against him, cases in which he is equated to the LIBRADOR | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 790-792 p.138 (EVID-225; txt PAGE 138) |
| LB-008 | Código de Comercio, Art. 793: "El cheque debe contener: I.- Número y serie. II.- Mención 'cheque', inserta en el texto. III.- Nombre y domicilio del banco contra el cual se libra. IV.- Orden incondicional de pagar una suma determinada de dinero, indicando la cantidad en letras o en números. En caso de que la cantidad solamente conste en números, deberá estamparse con máquina protectora. Cualquier convenio inserto en el cheque se tendrá por no escrito. V.- Nombre de la persona a cuyo favor se libre o indicación de ser al portador. VI.- Lugar y fecha de expedición. VII.- Firma autógrafa del librador." | The cheque must contain the SEVEN fields: I. NUMBER AND SERIES; II. mention "cheque" inserted in the text; III. name and domicile of the bank on which it is drawn; IV. unconditional order to pay a determined sum of money, indicating the quantity IN LETTERS OR IN NUMBERS — where the quantity appears ONLY in numbers it must be stamped with a PROTECTOR MACHINE; any agreement inserted in the cheque is held AS NOT WRITTEN; V. name of the person in whose favour it is drawn or indication of being TO BEARER; VI. place and date of expedition; VII. AUTOGRAPH SIGNATURE of the librador | `sv/sources/07_Codigo_Comercio.pdf` | Art. 793 p.139 (EVID-225; txt PAGE 139) |
| LB-009 | Código de Comercio, Art. 794: "Solamente producirá efectos de cheque, el librado con sujeción a lo indicado en el artículo anterior y a cargo de una institución bancaria debidamente autorizada." "Tampoco producirá efecto de cheque, el que contenga raspaduras, testaduras, interlineados o enmiendas." Art. 796: "El cheque no es susceptible de aceptación previa. Cualquier cláusula que lo sujete a ella se tendrá por no escrita." | Only a cheque drawn in conformity with the preceding article AND on a DULY AUTHORIZED BANKING INSTITUTION produces cheque effects. A cheque containing RASPADURAS (scrapings), TESTADURAS (crossings-out), INTERLINEADOS (interlineations) or ENMIENDAS (amendments) LIKEWISE produces NO cheque effect. The cheque is not susceptible of PRIOR ACCEPTANCE; any clause subjecting it to acceptance is held as not written | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 794/796 pp.139-140 (EVID-225; txt PAGE 139-140) |
| LB-010 | Código de Comercio, Art. 804: "El cheque será siempre pagadero a la vista. Cualquier inserción en contrario se tendrá por no escrita." "Todo cheque será pagadero a su presentación, aunque aparezca con fecha posterior. En este caso, el banco queda exento de toda responsabilidad por el pago. En caso de falta de pago, el librador tendrá las mismas responsabilidades, civiles y penales, que tendría si el cheque llevase la fecha del día en que fue presentado." Art. 805: "El cheque deberá ser presentado para su pago a la institución bancaria contra la cual se ha librado, o a cualquiera de sus agencias en el país; pero en este último caso, si la agencia bancaria no tuviere fondos suficientes para hacer efectivo el cheque, gozará de un plazo de setenta y dos horas para efectuar su pago." | The cheque is ALWAYS PAYABLE AT SIGHT; any contrary insertion is held as not written. Every cheque is payable ON PRESENTATION even if bearing a LATER DATE — in that case the bank is exempt from all responsibility for payment, and on non-payment the librador bears the same civil and criminal responsibilities he would bear if the cheque carried the presentation date. The cheque must be presented for payment to the banking institution on which it is drawn OR ANY OF ITS AGENCIES IN THE COUNTRY; in the latter case, if the agency lacks SUFFICIENT FUNDS it enjoys SEVENTY-TWO HOURS to effect payment | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 804-805 pp.140-141 (EVID-225; txt PAGE 140-141) |
| LB-011 | Código de Comercio, Art. 806: "Un banco no estará obligado a pagar los cheques que no sean emitidos en los formularios que haya suministrado al librador; los formularios se entregarán mediante recibo que exprese la serie y numeración correspondientes." "En caso de extravío de los formularios de cheques recibidos, el cliente dará inmediatamente aviso por escrito al banco. El banco no pagará los cheques que en lo sucesivo se le presenten emitidos en los formularios denunciados como perdidos." "Los formularios pertenecientes al librador que hayan sido autorizados por el banco, se considerarán como suministrados por éste." Art. 810: "La compensación bancaria de un cheque surte los mismos efectos que su presentación al librado." | A bank is not obliged to pay cheques not emitted on the FORMULARIOS (forms) it SUPPLIED to the librador; the forms are delivered against a RECEIPT expressing the corresponding SERIE AND NUMERACIÓN (series and numbering). On LOSS of received cheque forms the client must IMMEDIATELY give the bank WRITTEN NOTICE; the bank will not pay cheques subsequently presented on the forms denounced as lost. Forms belonging to the librador that the bank has AUTHORIZED are considered as supplied by it. Art. 810: BANK CLEARING of a cheque produces the SAME EFFECTS as presentation to the librado (drawee bank) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 806/810 pp.141-142 (EVID-225; txt PAGE 141-142) |
| LB-012 | Código de Comercio, Art. 808: "El cheque deberá presentarse para su pago: I.- Dentro de los quince días que sigan al de su fecha, si fuere pagadero en el mismo lugar de su libramiento. II.- Dentro de un mes, si fuere expedido en el territorio nacional pagadero en plaza salvadoreña diferente de aquélla en que fue librado. III.- Dentro de tres meses, si fuere expedido en el extranjero y pagadero en el territorio nacional. IV.- Dentro de tres meses, si fuere expedido en el territorio nacional para ser pagadero en el extranjero, siempre que no fijen otro plazo las leyes del lugar de presentación." | The cheque must be presented for payment: I. within the FIFTEEN DAYS FOLLOWING ITS DATE, if payable in the SAME place of its drawing (same plaza); II. within ONE MONTH, if expedited in the national territory payable in a Salvadorean plaza DIFFERENT from that of drawing; III. within THREE MONTHS, if expedited ABROAD and payable in the national territory; IV. within THREE MONTHS, if expedited in the national territory to be payable ABROAD — provided the laws of the place of presentation fix no other term | `sv/sources/07_Codigo_Comercio.pdf` | Art. 808 p.141 (EVID-225; txt PAGE 141) |
| LB-013 | Código de Comercio, Art. 795: "El cheque librado por quien no tenga fondos disponibles en la institución a cuyo cargo se emite, protestado en tiempo, será documento ejecutivo y acarreará a su librador las responsabilidades penales consiguientes." "Si no ha sido protestado en tiempo, el cheque sin provisión de fondos disponibles, valdrá como documento privado contra su librador, sin perjuicio de la responsabilidad penal." "Se consideran como fondos disponibles, exclusivamente aquéllos de que el librador pueda disponer por medio de cheque." Art. 815: "El cheque presentado en tiempo y no pagado, debe protestarse a más tardar el décimo quinto día que siga al de su presentación, siempre que el banco no lo anotare en la forma indicada en el artículo siguiente." "El protesto se hará con las mismas formalidades que el de la letra de cambio a la vista, pero no podrá ser parcial y deberá hacerse siempre el requerimiento de pago al representante del banco librado. Se exceptúa el caso en que el tenedor legítimo del cheque haya recibido voluntariamente un pago parcial, en cuyo caso el protesto o la anotación a que se refiere el artículo siguiente, será únicamente por la parte insoluta del cheque." Art. 816: "La nota que el banco librado autorice en el cheque mismo, de que fue presentado en tiempo y no pagado, surtirá iguales efectos que el protesto." | A cheque drawn by one LACKING AVAILABLE FUNDS in the institution on which it is emitted, PROTESTED IN TIME, is an EJECUTIVO (summary-execution) DOCUMENT and brings its librador the consequent PENAL responsibilities; NOT protested in time, the unfunded cheque valdrá as a PRIVATE DOCUMENT against its librador, without prejudice to penal responsibility. Available funds are EXCLUSIVELY those of which the librador can dispose BY MEANS OF CHEQUE. A cheque presented in time and UNPAID must be protested AT THE LATEST ON THE FIFTEENTH DAY FOLLOWING ITS PRESENTATION — provided the bank has not annotated it per the following article; the protest follows the at-sight letra-de-cambio formalities, CANNOT BE PARTIAL, and payment must always be required of the drawee bank's representative — except where the legitimate holder VOLUNTARILY received partial payment, in which case protest/annotation covers only the INSOLUTA (unsolved) part. Art. 816: the NOTE the drawee bank authorizes on the cheque itself — that it was presented in time and unpaid — produces the SAME EFFECTS AS PROTEST | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 795/815-816 pp.139, 142 (EVID-225; txt PAGE 139, 142) |
| LB-014 | Código de Comercio, Art. 819: "Por no haberse presentado o protestado el cheque, en la forma y plazos previstos en este Capítulo, caducan: I.- Las acciones de regreso del último tenedor contra los endosante o avalistas. II.- Las acciones de regreso de los endosantes o avalistas entre sí. III.- La acción contra el librador en los términos del inciso cuarto del artículo 811 y contra sus avalistas." Art. 820: "Las acciones cambiarias del cheque prescriben en un año, contado: I.- Desde la presentación, la del último tenedor del documento. II.- Desde el día siguiente a aquél en que paguen el cheque, las de los endosantes y avalistas." | For NOT having presented or protested the cheque in the form and terms provided in this chapter, CADUCAN (lapse): I. the last holder's REGRESO (recourse) actions against the ENDOSERS OR AVALISTAS (guarantors) [sic — print singular "endosante"]; II. the endorsers'/avalistas' recourse actions AMONG THEMSELVES; III. the action against the LIBRADOR in the terms of Art. 811 inciso cuarto, and against his avalistas. The cheque's CAMBIARIA ACTIONS PRESCRIBE IN ONE YEAR, counted: I. from PRESENTATION, that of the last holder; II. from the DAY FOLLOWING that on which they PAY the cheque, those of the endorsers and avalistas | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 819-820 p.143 (EVID-225; txt PAGE 143) |
| LB-015 | Código de Comercio, Art. 811 (incisos 2, 4 y 5; incisos 1 y 3 omitidos — obligación del banco de cubrir conforme al convenio y deber de aviso del tenedor): "Cuando un banco se niega sin causa justificada a pagar un cheque extendido en debida forma, responderá al librador que tuviere fondos, por los daños que cause su negativa, pero el tenedor no puede compelerlo al pago, quedando los derechos de éste a salvo contra el librador. No se reputará negativa la retención prevista en el artículo 809 inciso segundo." "El tenedor de un cheque que no haya sido protestado dentro del plazo legal, sólo tendrá acción contra el librador por el valor del cheque, en los términos del inciso segundo del artículo 795." "El tenedor de un cheque protestado, sin perjuicio de la acción criminal que corresponda contra el librador, tendrá derecho a reclamar su valor, intereses legales y gastos, a cualquiera de los endosantes o al librador. El endosante que lo pagare se subrogará contra los endosantes anteriores y contra el librador." Art. 821: "La indemnización a que se refiere el artículo 811, en ningún caso podrá ser inferior al veinte por ciento del valor del cheque." | When a bank WITHOUT JUSTIFIED CAUSE refuses to pay a properly drawn cheque, it answers TO THE LIBRADOR HAVING FUNDS for the damages its refusal causes — but the holder CANNOT COMPEL payment, his rights remaining safe against the librador; the Art. 809-II retention is not deemed refusal. The holder of a cheque NOT protested within the legal term has action ONLY against the librador for the cheque's value per Art. 795-II. The holder of a PROTESTED cheque — without prejudice to the criminal action against the librador — may claim its VALUE, LEGAL INTEREST and EXPENSES from any of the endorsers or the librador; the paying endorser is SUBROGATED against prior endorsers and the librador. Art. 821: the Art. 811 indemnification may IN NO CASE be LESS THAN TWENTY PER CENT OF THE CHEQUE'S VALUE | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 811/821 pp.142-143 (EVID-225; txt PAGE 142-143) |
| LB-016 | Código de Comercio, Art. 822: "Son cheques especiales: I.- El cheque cruzado. II.- El cheque para abono en cuenta. III.- El cheque certificado. IV.- El cheque de viajero. V.- El cheque con provisión garantizada o cheque limitado. VI.- El cheque circular. VII.- El cheque de caja o de gerencia." Art. 823: "Cheque cruzado es el que contiene dos líneas paralelas en el anverso, con indicación de un banco o sin ella. En el primer caso se denominará 'cruzamiento especial'; en el segundo, 'cruzamiento general'." "Los cheques cruzados son endosables, pero sólo podrán pagarse a un banco de la República. En el caso de cruzamiento especial, el pago deberá hacerse precisamente al banco indicado entre las paralelas." "El cruzamiento general puede convertirse en especial, poniendo el nombre del banco cobrador entre las líneas paralelas, pero el especial no puede transformarse en general." "El cruzamiento es parte esencial del cheque y por consiguiente no será lícito borrarlo o alterarlo; sólo podrá adicionarse en la forma autorizada en el inciso anterior." | SPECIAL CHEQUES are: I. the CROSSED cheque (cruzado); II. the FOR CREDIT TO ACCOUNT cheque (para abono en cuenta); III. the CERTIFIED cheque (certificado); IV. the TRAVELLER's cheque (de viajero); V. the GUARANTEED-PROVISION or LIMITED cheque (con provisión garantizada / limitado); VI. the CIRCULAR cheque (circular); VII. the CASH or MANAGER's cheque (de caja o de gerencia). A crossed cheque bears TWO PARALLEL LINES on the face, with a bank indicated or without — SPECIAL crossing in the first case, GENERAL in the second. Crossed cheques are endosable but may ONLY be paid TO A BANK OF THE REPUBLIC; under special crossing payment must be made precisely to the bank indicated between the parallels. GENERAL crossing may convert to SPECIAL (writing the collecting bank's name between the lines); SPECIAL may NOT become general. The crossing is an ESSENTIAL PART of the cheque — it may NOT lawfully be erased or altered, only added to as authorized | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 822-823 pp.143-144 (EVID-225; txt PAGE 143-144) |
| LB-017 | Código de Comercio, Art. 824: "El librador o el tenedor pueden ordenar que un cheque no sea pagado en efectivo, mediante la inserción en el documento de la expresión 'para abono en cuenta'. En este caso, el librado sólo podrá hacer el pago abonando el importe del cheque en la cuenta que lleve o abra en favor del tenedor, o al banco en que éste lo haya depositado en su cuenta. El librado que pague en otra forma, es responsable de pago irregular. Cuando la expresión se encuentre en el anverso, el abono deberá hacerse al primer tenedor; cuando se encuentre a través de un endoso, el abono se hará al favorecido por dicho endoso." "El cheque no es negociable a partir de la inserción de la cláusula 'para abono en cuenta'. La cláusula no puede ser borrada. El cheque para abono en cuenta no necesitará la firma del favorecido." | The librador or holder may order that a cheque NOT be paid in cash by inserting the expression "PARA ABONO EN CUENTA" (for credit to account). The librado may then pay ONLY by crediting the cheque's amount to the account it keeps or opens in the holder's favour, or to the bank where the holder deposited it in his account; a librado paying otherwise is responsible for IRREGULAR PAYMENT. With the expression on the FACE, credit goes to the first holder; through an ENDORSEMENT, to the person favoured by that endorsement. From insertion of the clause the cheque is NOT NEGOTIABLE; the clause CANNOT BE ERASED; the abono-en-cuenta cheque does NOT require the favoured person's signature | `sv/sources/07_Codigo_Comercio.pdf` | Art. 824 p.144 (EVID-225; txt PAGE 144) |
| LB-018 | Código de Comercio, Art. 825: "El librador tiene derecho a solicitar por escrito que el banco certifique el cheque, declarando que existen en su poder fondos bastantes para pagarlo." "La certificación no puede ser parcial. El cheque certificado no es negociable." "La certificación libera de responsabilidad al librador y endosantes, quedando únicamente responsable el banco." "La inserción en el cheque de las palabras 'acepto', 'visto', 'bueno' u otras equivalentes, suscritas por el banco o la simple firma de persona autorizada por éste puesta en el cheque, equivale a una certificación." "El librador puede revocar el cheque certificado, siempre que lo devuelva al banco para su cancelación." "Desde el momento en que un cheque se certifique, el banco cargará el valor del mismo en la cuenta del librador." Art. 826: "Las acciones cambiarias contra el librado que certifique un cheque, prescriben en seis meses a partir de la fecha en que concluya el plazo de presentación." | The librador may request IN WRITING that the bank CERTIFY the cheque, declaring that SUFFICIENT FUNDS exist in its hands to pay it. Certification CANNOT BE PARTIAL; the certified cheque is NOT NEGOTIABLE. Certification RELEASES the librador and endorsers from responsibility, the BANK remaining solely responsible. Insertion of the words "acepto", "visto", "bueno" or equivalents subscribed by the bank — or the mere signature of a person authorized by it placed on the cheque — EQUALS certification. The librador may REVOKE a certified cheque by RETURNING it to the bank for cancellation. From the moment of certification the bank CHARGES the cheque's value to the librador's account. Art. 826: cambiaria actions against the librado that certified a cheque PRESCRIBE IN SIX MONTHS from the date the presentation term CONCLUDES | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 825-826 pp.144-145 (EVID-225; txt PAGE 144-145) |
| LB-019 | Código de Comercio, Art. 827: "Los cheques de viajero son expedidos por el librador a su propio cargo y pagaderos por su establecimiento principal, sus sucursales y corresponsales en la República o en el extranjero. Los cheques de viajero pueden ser puestos en circulación por el librador, o por sus sucursales y corresponsales autorizados para ello." Art. 828: "Los cheques de viajero se extenderán a favor de persona determinada. El que pague el cheque deberá verificar la autenticidad de la firma del tomador, cotejándola con la firma de éste que aparezca certificada en el mismo cheque, por el que lo haya puesto en circulación." Art. 829: "El tenedor de un cheque de viajero puede presentarlo para su pago en cualquier tiempo, a cualquiera de las sucursales y corresponsales incluídos en la lista que le proporcionará el librador, mientras no transcurra el plazo señalado para la prescripción." Art. 830: "La falta de pago inmediato dará derecho al tenedor para exigir al librador la devolución del importe del cheque de viajero y el resarcimiento de daños y perjuicios, que en ningún caso será inferior al veinte por ciento del valor del cheque no pagado." Art. 831: "El corresponsal que hubiere puesto en circulación los cheques de viajero, tendrá las obligaciones que corresponden al endosante y deberá reembolsar al tomador el importe de los cheques no utilizados que éste le devuelva." "Las acciones cambiarias contra el que expida o ponga en circulación los cheques de viajero, prescriben en dos años a partir de la fecha en que los cheques son puestos en circulación." | TRAVELLER'S CHEQUES are expedited by the librador ON HIS OWN ACCOUNT, payable by his main establishment, branches and CORRESPONSALES (correspondents) in the Republic or abroad; they may be put into circulation by the librador or by his authorized branches/correspondents. They are drawn in favour of a DETERMINED PERSON; the payer must verify the TOMADOR's (taker's) signature authenticity against the signature certified on the cheque itself by whoever put it into circulation. The holder may present it for payment AT ANY TIME to any listed branch/correspondent, while the prescription term has not run. Art. 830: failure of immediate payment entitles the holder to demand from the librador the refund of the amount and damages NEVER BELOW TWENTY PER CENT of the unpaid cheque's value. The correspondent who circulated them bears ENDORSER obligations and must reimburse the taker the amount of unused cheques returned. Art. 831: cambiaria actions against the issuer/circulator of traveller's cheques PRESCRIBE IN TWO YEARS from the date the cheques are PUT INTO CIRCULATION | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 827-831 p.145 (EVID-225; txt PAGE 145) |
| LB-020 | Código de Comercio, Art. 832: "El banco puede autorizar a una persona a librar cheques limitados o con provisión garantizada, entregándole fórmulas especiales. Cada fórmula debe contener: I.- Denominación de cheque limitado, inserta en el texto. II.- Fecha de su entrega. III.- Cantidad máxima por la que el cheque puede ser librado, impresa en letras y en números. IV.- Límite de tiempo válido para su circulación, el cual no podrá exceder de tres meses para los cheques pagaderos en El Salvador y de un año para los pagaderos en el exterior." "La entrega de fórmulas de esta clase equivale a certificar la existencia de las sumas en ellas indicadas, en poder del Banco, por el tiempo de validez de circulación." "Estos cheques no podrán ser librados al portador." Art. 833: "El cheque circular es un título a favor de persona determinada, que contiene la promesa hecha por una institución bancaria de pagar una suma de dinero en cualquiera de sus establecimientos, diversos de aquel en que el cheque fue librado." Art. 835: "Las acciones directa y de regreso derivadas de la falta de pago, no quedarán condicionadas, en cuanto al cheque circular, a su presentación para pago dentro de los términos fijados en este Código, porque el tenedor dispondrá de seis meses para cobrarlo en cualquiera de los establecimientos señalados o en la institución libradora." Art. 836: "El endoso del cheque circular no hace responsable al endosante del pago del mismo, sino sólo de la autenticidad del documento. El cheque circular, desde su emisión, producirá el efecto de transferir la propiedad de la provisión de fondos al tomador original y a los sucesivos endosatarios." Art. 837: "Sólo los establecimientos bancarios pueden expedir cheques de caja o de gerencia, a cargo de sus propias dependencias. Estos cheques deberán girarse a favor de persona determinada." | The bank may authorize a person to draw LIMITED / GUARANTEED-PROVISION cheques, delivering SPECIAL FORMULAS each containing: I. "cheque limitado" denomination inserted in the text; II. delivery date; III. the MAXIMUM amount for which the cheque may be drawn, printed in words and numbers; IV. the time limit valid for circulation — NOT exceeding THREE MONTHS for cheques payable in El Salvador and ONE YEAR for those payable abroad. Delivery of such formulas EQUALS CERTIFYING the existence of the indicated sums in the Bank's hands for the circulation-validity time. These cheques CANNOT be drawn TO BEARER. Art. 833: the CIRCULAR cheque is a title in favour of a determined person containing a BANKING INSTITUTION'S PROMISE to pay a sum at any of its establishments OTHER than that on which it was drawn. Art. 835: direct and recurso actions for non-payment of a circular cheque are NOT conditioned on presentation within the Code's terms — the holder has SIX MONTHS to collect it at any signaled establishment or the issuing institution. Art. 836: endorsement of a circular cheque does not make the endorser responsible for PAYMENT — only for the document's AUTHENTICITY; from emission it transfers OWNERSHIP OF THE FUNDS PROVISION to the original taker and successive endorsees. Art. 837: only banking establishments may issue CASH/MANAGER'S CHEQUES, chargeable to their own offices, drawn in favour of a DETERMINED PERSON | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 832-837 pp.145-146 (EVID-225; txt PAGE 145-146; Art. 834 six-field content zone) |
| LB-021 | Código de Comercio, Art. 960: "El deudor moroso deberá pagar el interés pactado y en su defecto el legal como indemnización por la mora. Cuando la obligación tuviere por objeto cosa cierta y determinada, o determinable, el interés se calculará sobre el valor de la cosa. Este valor se determinará, salvo convenio, por el precio que tuviere en plaza el día del vencimiento, o por su cotización en bolsa, y, en defecto de ambos, por peritos." "El interés legal en materia mercantil será fijado periódicamente por la Secretaría de Economía." | The MOROSO (defaulting) debtor must pay the AGREED (pactado) interest and IN DEFAULT THE LEGAL interest as mora indemnification. Where the obligation's object is a thing certain and determined, or determinable, the interest is computed on the VALUE OF THE THING — determined, save agreement, by its PLAZA PRICE on the maturity day, or its BOLSA (exchange) quotation, and failing both by PERITOS (experts). The LEGAL INTEREST in mercantile matters is FIXED PERIODICALLY BY THE ECONOMÍA SECRETARIAT (dated config — SOQ-26, never hardcoded) | `sv/sources/07_Codigo_Comercio.pdf` | Art. 960 p.165 (EVID-226; txt PAGE 165) |
| LB-022 | Código de Comercio, Art. 962: "Salvo disposición legal o pacto expreso en contrario, los codeudores y fiadores en materia de comercio son solidarios, inclusive los que no sean comerciantes." | Save legal provision or EXPRESS PACT to the contrary, CO-DEBTORS AND GUARANTORS in commercial matters are SOLIDARY (jointly and severally liable) — INCLUDING those who are not merchants | `sv/sources/07_Codigo_Comercio.pdf` | Art. 962 p.165 (EVID-226; txt PAGE 165) |
| LB-023 | Código de Comercio, Art. 995 (reform mark "(25)" del inciso IV retirado — procedencia notada en §2): "Los plazos de la prescripción mercantil son los siguientes: I.- Prescribirán a los seis meses las acciones de rectificación de los saldos de las cuentas corrientes. II.- Prescribirán en un año las siguientes acciones: la nulidad de los acuerdos de las asambleas sociales o de la celebración de los mismos; la de enriquecimiento indebido con motivo del giro de títulosvalores; las derivadas del cheque; las de regreso de la letra de cambio; las de reclamación por vicios de la cosa vendida; las concernientes al contrato de transporte; y las de reclamación de responsabilidad a los administradores, auditores e interventores de sociedades. III.- Prescriben en dos años, salvo las excepciones señaladas en los ordinales anteriores, las acciones derivadas de los siguientes contratos: de sociedad, de compraventa, de suministro, de depósito, de comisión, estimatorio, de edición, de hospedaje, de participación, de garantía y demás que no tuvieren plazos distintos previstos en este Código o en leyes especiales. IV.- Prescribirán en cinco años las acciones derivadas de los contratos de crédito, contados a partir de la fecha del último reconocimiento de la obligación por parte del deudor; en el mismo plazo prescribirán los otros derechos mercantiles." | The terms of MERCANTILE PRESCRIPTION are: I. SIX MONTHS — actions for RECTIFICATION of cuenta corriente (current-account) balances. II. ONE YEAR — nullity of sociedad assembly agreements or of their celebration; unjust enrichment from the giro of títulos valores; actions derived from the CHEQUE; REGRESO actions of the letra de cambio; claims for VICIOS (defects) of the thing sold; actions concerning the TRANSPORT contract; and liability claims against sociedad ADMINISTRATORS, AUDITORS and INTERVENTORES. III. TWO YEARS — save the exceptions in the preceding ordinals — actions derived from the contracts: sociedad, COMPRAVENTA (sale), SUMINISTRO (supply), depósito, COMISIÓN, estimatorio, edición, hospedaje, participación, garantía and OTHERS lacking distinct terms in this Code or special laws. IV. FIVE YEARS — actions derived from CREDIT contracts, counted from the date of the LAST RECOGNITION of the obligation BY THE DEBTOR; in the same term the OTHER mercantile rights prescribe | `sv/sources/07_Codigo_Comercio.pdf` | Art. 995 p.169 (EVID-226; txt PAGE 169) |
| LB-024 | Código de Comercio, Art. 996: "Cuando un derecho deba ejercerse o un requisito deba llenarse dentro de un plazo determinado bajo pena de caducidad, no se aplicarán las normas sobre interrupción y suspensión de la prescripción, contenidas en el Código Civil." "La fuerza mayor suspenderá los plazos de caducidad, pero continuarán corriendo tan pronto como cese aquélla." Art. 997: "Puede rescindirse el pacto que establezca un plazo de caducidad que, a juicio prudencial del Juez, haga excesivamente difícil para una de las partes el ejercicio del derecho." Art. 998: "Las partes no podrán modificar el régimen legal de la caducidad; tampoco podrán renunciar a ella si hubiere sido establecida por la ley." | When a right must be exercised or a requisite filled within a determinate term UNDER PENALTY OF CADUCIDAD, the Código Civil's norms on INTERRUPTION and SUSPENSION of prescription DO NOT APPLY. FORCE MAJEURE suspends caducidad terms, which resume running as soon as it ceases. A PACT establishing a caducidad term that — to the Judge's prudent judgment — makes exercising the right excessively difficult for one party MAY BE RESCINDED. The parties CANNOT MODIFY the legal caducidad regime, NOR RENOUNCE it where established by LAW (statutory caducidad: no-suspension, no-party-modification) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 996-998 p.169 (EVID-226; txt PAGE 169) |
| LB-025 | Código de Comercio, Art. 999: "Las obligaciones mercantiles y su extinción se prueban por los medios siguientes: I.- Instrumentos públicos, auténticos y privados. II.- Facturas. III.- Correspondencia postal. IV.- Correspondencia telegráfica reconocida. V.- Registros contables. VI.- Testigos. VII.- Los demás admitidos por la ley." | Mercantile obligations and their extinction are proved by: I. public, authentic and private instruments; II. FACTURAS (invoices); III. postal correspondence; IV. recognized telegraphic correspondence; V. ACCOUNTING RECORDS; VI. witnesses; VII. the other means admitted by law | `sv/sources/07_Codigo_Comercio.pdf` | Art. 999 pp.169-170 (EVID-226; txt PAGE 169-170) |
| LB-026 | Código de Comercio, Art. 1002: "Si apareciere diferencia entre los ejemplares de un contrato que presenten las partes en juicio, el asunto se dilucidará de acuerdo con los asientos de contabilidad de los contratantes; hará fe la contabilidad mercantil de aquél que la lleve en forma legal; llevándola ambos, cualquier otro medio de prueba; si ambos alegaren probanzas de igual fuerza, el Juez resolverá a favor del demandado." | If a DIFFERENCE appears between the contract copies the parties present at trial, the matter is elucidated according to the contractors' ACCOUNTING ENTRIES: the mercantile accounting of the one who keeps it IN LEGAL FORM MAKES FE (prevails as evidence); if BOTH keep it legally, any other means of proof; if both allege proofs of equal force, the Judge resolves FOR THE DEFENDANT | `sv/sources/07_Codigo_Comercio.pdf` | Art. 1002 p.170 (EVID-226; txt PAGE 170) |
| LB-027 | Código de Comercio, print markers: TÍTULO II "ARBITRAJE COMERCIAL": "Del Art. 1004 al Art. 1012.- DEROGADOS (21)" | Commercial arbitration (Arts. 1004-1012) DEROGATED by reform (21) — superseded by special arbitration legislation outside this corpus (scope note §3.9; no FRs) | `sv/sources/07_Codigo_Comercio.pdf` | Arts. 1004-1012 p.170 (EVID-226 zone; txt PAGE 170) |
| LB-028 | Reformas al Código de Comercio (110_ = D.L. N° 295, 22-feb-2022; D.O. N° 78 T.435 26-abr-2022; vigencia Art. 3: 8 days post-publication → **4-may-2022**), Arts. 1-2 (Art. 960 inciso tercero ADDED + Art. 960-A INTERCALATED — AWARENESS ROW, no FR mechanics). Art. 1: "Añádase un inciso tercero al artículo 960 de la siguiente manera:" "Para determinar si la tasa de interés efectiva pactada sobrepasa o no las tasas máximas publicadas conforme a la Ley Contra la Usura, el juez deberá consultar al Banco Central de Reserva de El Salvador." Art. 2: "Intercálese el artículo 960-A, entre los artículos 960 y 961 de la siguiente manera:" "Efectos del cobro de intereses usurarios vía judicial" "Art. 960-A.- Las obligaciones de crédito que, de conformidad con la legislación aplicable, se pacten con intereses usurarios serán nulas de pleno derecho, en lo atinante al interés pactado que constituya usura." "En caso de sentencia condenatoria en los procesos judiciales, para el cálculo de los intereses a pagar, el Juez tomará de base la Tasa Máxima Legal publicada y vigente al momento de la celebración del contrato." Art. 3: "El presente decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." | The usura layer on Art. 960 (AWARENESS ONLY — §2/§3.6): to determine whether the pactada EFFECTIVE interest rate exceeds the maxima published under the Ley Contra la Usura, the JUDGE must consult the Banco Central de Reserva de El Salvador (960 inciso tercero, added); credit obligations pactada with USURIOUS interest are NULL DE PLENO DERECHO as to the usurious slice — "en lo atinante al interés pactado que constituya usura" — and on a condemnatory judgment the judicial interest calculation bases on the TASA MÁXIMA LEGAL published and in force AT CONTRACT CELEBRATION (960-A, intercalated). Gloss: a JUDICIAL-MECHANICS layer with NO Odoo posting surface — the Economía interest-rate config of FR-158 (SOQ-26; OQ-001) is UNCHANGED by this reform; the Tasa Máxima Legal is a BCR external series, never shipped; the presidential-observations NOTA (returned 7-mar-2022, accepted in plenary 29-mar-2022) is as-printed legislative history. Effective 4-may-2022 | `sv/sources/110_Reforma_CodigoComercio_DL295_2022_Asamblea.pdf` (base print co-cited: `sv/sources/07_Codigo_Comercio.pdf`) | 110_ Arts. 1-3 (txt PAGE 1-2; EVID-408); NOTA + D.O. stamp (txt PAGE 2); 07_ Art. 960 p.165 (EVID-226; txt PAGE 165 — pre-110_ print, LB-021) |
| LB-029 | Reformas al Código de Comercio (112_ = D.L. N° 972, 19-mar-2024; D.O. N° 67 T.443 11-abr-2024; vigencia Art. 3: 8 days post-publication → **19-abr-2024**), Art. 1 (Libro Tercero, Título II, Capítulo VIII, Sección "F" TRUNCAMIENTO DE CHEQUES ADDED, Arts. 838-A..838-E — AWARENESS ROW, no FR mechanics). Art. 838-A (incisos 1, 3 y 5; incisos 2, 4 y final omitidos — compensación/sistema-informático definitions + the physical-custodia Consejo Directivo parameters: bank-exchange mechanics): "El Truncamiento de Cheques es un procedimiento por el cual el intercambio físico del cheque se reduce o se elimina como condición previa para la liberación de fondos a los beneficiarios finales, siendo reemplazado por registros electrónicos que incluyen la imagen del cheque, para su procesamiento o transmisión automática." "El Banco Central de Reserva de El Salvador reglamentará y administrará el proceso de compensación de cheques y otros sistemas de pago, entre bancos y otras instituciones del sistema financiero." "Además de lo dispuesto en el presente Capítulo, la presentación de un cheque, indistintamente del valor consignado en él, en el sistema de compensación de cheques, por medio de imágenes que contienen sus elementos esenciales en forma electrónica u otros medios que en el futuro puedan ser autorizados, surtirá los mismos efectos que la presentación de un cheque físico." Art. 838-B: "El Banco Central de Reserva de El Salvador, por medio de su Consejo Directivo, en un plazo no mayor a noventa días a partir de la entrada en vigencia de esta Sección, emitirá las normas necesarias para reglamentar el proceso de compensación de cheques, así como las disposiciones necesarias para las características y medidas de seguridad de los cheques en físico y de los registros electrónicos que contengan su imagen para efectos del truncamiento." "La normativa a la que hace referencia la presente disposición, se considera materia excluida de conformidad al artículo 7, literal b) de la Ley de Mejora Regulatoria, para los efectos pertinentes." Art. 838-C (lead verbatim; literals a)-l) summarized — full list in txt): "Son infracciones administrativas las acciones u omisiones siguientes:" [a) negarse la institución bancaria a efectuar de forma injustificada el truncamiento (justificación: cheque sin fondos, sin firmas de refrendario, falsedad, cuenta intervenida/embargada o sin disponibilidad); b) demorar o dilatar la compensación; c) alterar, intervenir o interrumpir el sistema informático; d) entregar la reproducción de la imagen digital sin requisitos o negándose a entregarla; e) no proveer medios de consulta de la imagen digital; f) "No acreditar de manera inmediata a sus clientes, una vez recibidos los fondos de parte del liquidador"; g) no entregar la certificación de la imagen del cheque; h) no informar de manera inmediata a la Superintendencia del Sistema Financiero el incumplimiento de otras instituciones participantes; i) negligencia o demora en la reparación de problemas o fallas técnicas; j) no realizar las verificaciones necesarias de los cheques transmitidos; k) exponer a riesgos operativos y financieros a otras instituciones participantes y a terceros; l) incumplir los procesos operativos y demás disposiciones administrativas del Banco Central de Reserva]. Art. 838-D: "Las infracciones que establece el artículo anterior serán sancionadas con multa, cuyo monto se determinará de conformidad a los criterios establecidos de las disposiciones generales sobre las sanciones administrativas, se impondrán multas por medio del Banco Central de Reserva desde los cien (100) hasta los un mil (1000) salarios mínimos vigentes, sin perjuicio de las demás sanciones que puedan ser determinadas de conformidad con la Ley de Supervisión y Regulación del Sistema Financiero y la Ley Orgánica del Banco Central de Reserva de El Salvador al tratarse el cheque de un sistema de pago. Lo anterior, mediante resolución motivada en la que el Banco Central de Reserva deberá respetar el principio de proporcionalidad en la imposición de la multa." "Cuando en las disposiciones legales contenidas en este título se haga referencia a la expresión salario mínimo o salario mínimo mensual, como base para la imposición de sanciones, se entenderá que se hace referencia al valor que corresponda al equivalente a treinta días del salario mínimo por jornada ordinaria de trabajo diario diurno fijado mediante decreto emitido por el Órgano Ejecutivo en el ramo de Trabajo y Previsión Social, para los que trabajan en los rubros del comercio, servicios e industria." Art. 838-E: "Para efectos de la imposición de sanciones administrativas en relación con infracciones tipificadas en el presente capitulo, se aplicará el procedimiento establecido en la Ley de Procedimientos Administrativos." Disposición Transitoria Art. 2: "Los participantes del sistema de compensación de cheques tendrán noventa días, a partir de la vigencia de las normas que emita el Consejo Directivo del Banco Central de Reserva para la regulación del proceso de compensación de cheques y disposiciones relacionadas a los cheques en físico y los registros electrónicos que hace referencia el art. 838-B, para adecuar sus procesos internos y realizar la sustitución de los cheques al formato dispuesto por el Banco Central de Reserva de El Salvador, a efecto de aplicar el Truncamiento de Cheques; posterior a dicho plazo, no se deberán aceptar cheques en formato distinto al normado." Art. 3: "El presente decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." | The cheque-truncation layer (AWARENESS ONLY — §2): truncation is the procedure by which the PHYSICAL exchange of the cheque is reduced or eliminated as a precondition for releasing funds to final beneficiaries, replaced by ELECTRONIC RECORDS INCLUDING THE CHEQUE IMAGE; presentation in the BCR-administered compensation system BY IMAGES (or future authorized means) — regardless of the consigned value — produces THE SAME EFFECTS AS PHYSICAL PRESENTATION; the BCR Consejo Directivo must issue the compensation/characteristics-and-security norms ≤90 DAYS from the Sección's vigencia (the matter EXCLUDED from Art. 7-b Ley de Mejora Regulatoria); administrative infractions a)-l) (bank-participant duties) are sanctioned with BCR multas of 100-1000 SMM under proportionality — the SMM = THIRTY DAYS of the comercio/servicios/industria ordinary-diurnal-day minimum wage — via the Ley de Procedimientos Administrativos (838-E); a 90-day transitoria substitutes the cheque format to the BCR-dispensed one, after which non-conforming formats are NOT accepted. Gloss: BANK-PARTICIPANT/BCR-SIDE duties — informational for Odoo; this file's CC clocks (Art. 808 presentation, Arts. 815-821 protest/caducidad/prescription, the Art. 995 prescription matrix) are UNTOUCHED by this reform (OQ-004 narrowed). Effective 19-abr-2024 | `sv/sources/112_Reforma_CodigoComercio_DL972_2024_Asamblea.pdf` (base print co-cited: `sv/sources/07_Codigo_Comercio.pdf`) | 112_ Arts. 1-3 + Disposición Transitoria (txt PAGE 1-5; EVID-410); D.O. stamp (txt PAGE 5); 07_ cheque chapter pp.139-143 (EVID-225 zone — untouched base print) |
## 3. Functional Requirements

### 3.1 Títulos valores: the general regime (Arts. 623-653)

- **SV-CML-FR-142:** The system shall model every *título valor*
  (negotiable instrument) record as the Art. 623 object — a document
  NECESSARY to assert the LITERAL AND AUTONOMOUS right consigned in
  it — carrying the Art. 625 five-formal-requisite checklist: (I) the
  title's name; (II) date and place of emission; (III) the prestations
  and rights the title incorporates; (IV) place of performance or
  exercise; (V) the emitter's signature — for both law-regulated and
  usage-consecrated titles; and it shall implement the Art. 625
  DEFAULT-FILLING rules: absent place of emission, the librador's
  recorded domicilio (or the place appearing next to his name absent
  any domicilio); absent place of performance, the obligado's recorded
  domicilio (same fallback); where SEVERAL places are consigned, the
  TENEDOR may exercise rights and the obligado perform in ANY of them
  (multi-place election flag). (LB-001; EVID-225)
- **SV-CML-FR-143:** The system shall flag titles emitted in El
  Salvador that are not written in CASTELLANO (Spanish) — the Art. 626
  language rule — as a form-defect warning on the instrument record
  (an additional translation into another language is permitted and
  recorded as such; no computation derives from the flag).
  (LB-002; EVID-225)
- **SV-CML-FR-144:** The system shall implement the Art. 628
  amount-precedence rules on every instrument carrying a written
  amount: where the import appears at once in WORDS and FIGURES and
  they differ, the title valdrá for the sum WRITTEN IN WORDS; where
  the quantity appears MORE THAN TWICE in words or in figures and
  they differ, the document valdrá for the LOWER sum consigned; and
  where a *máquina protectora* marking exists, the quantity MARKED BY
  THE PROTECTOR MACHINE PREVAILS over all others (computed
  effective-amount field with its precedence basis recorded).
  (LB-003; EVID-225)
- **SV-CML-FR-145:** The system shall compute every instrument
  deadline with the Art. 638 conventions, CONSUMING the shared
  días-hábiles engine BY ID (SV-FREP-FR-202..204,
  `sv/requirements/fiscal-reporting/08_filing-calendar.md` §3.3 —
  never re-implemented here): a term whose LAST DAY falls on an
  inhábil day is EXTENDED to the first following hábil day
  (next_habil); intermediate feriados COUNT in the term (the term is
  calendar-counted, only its last day shifts — unlike
  hábiles-only windows); and neither legal nor conventional terms
  comprise THE DAY SERVING AS POINT OF DEPARTURE (exclude-start-day
  on every clock in this file: the pagaré vista-plazo year, the
  cheque presentation/protest clocks, the prescription anchors).
  (LB-004; EVID-225; cross-ref SV-FREP-FR-202..204)
- **SV-CML-FR-146:** The system shall record the Art. 650 *salvo buen
  cobro* presumption on every payment allocation settled with a
  título valor — the title given in payment is PRESUMED received
  subject to collection, so the underlying receivable is NOT
  auto-extinguished at allocation time but on the instrument's
  effective collection (provisional-settlement semantics; reversal
  path preserved) — and shall track the Art. 649 enrichment-action
  clock: once the cambiaria action against the emitter is extinguished
  by caducidad or prescription and the holder lacks action against
  him and cambiaria/causal action against the other signatories, the
  action to demand from the emitter the sum of his enrichment
  prescribes in ONE YEAR from the day the cambiaria action caducated
  or prescribed (dated residual-exposure clock emitted at that
  extinction event). (LB-005; EVID-225)

### 3.2 Pagaré (Arts. 788-792)

- **SV-CML-FR-147:** The system shall model the *pagaré* (promissory
  note) as a título valor A LA ORDEN with the Art. 788 SIX-field
  content checklist: (I) mention of being a pagaré inserted in the
  text; (II) unconditional promise to pay a determined sum of money;
  (III) name of the person to whom payment is to be made; (IV) epoch
  (maturity) and place of payment; (V) date and place of subscription;
  (VI) the subscriber's signature — and it shall implement the Art. 789
  DEFAULTS: a pagaré mentioning NO maturity date is PAYABLE AT SIGHT
  (*a la vista*); a pagaré indicating NO place of payment takes the
  SUBSCRIBER'S DOMICILIO as such (default fields resolved at record
  time with their defaulted provenance flagged).
  (LB-006; EVID-225)
- **SV-CML-FR-148:** The system shall compute the Arts. 790-791
  pagaré presentation clocks and caducidad: a pagaré exigible at a
  certain term FROM SIGHT must be presented WITHIN THE YEAR FOLLOWING
  ITS DATE (exclude-start-day per FR-145) — the presentation only
  fixes the maturity date and is proved by a NOTARIAL ACTA (document
  reference on the presentation event); a DOMICILED pagaré is
  presented to the designated *pagador diputado* (appointed payer) —
  absent designation to the SUBSCRIBER himself at the domicilio — and
  the protest for non-payment must be raised at the DOMICILIO FIXED IN
  THE DOCUMENT, its omission (when the payer is not the subscriber)
  producing CADUCIDAD of the holder's regreso actions against the
  obligados (state machine: open → presented → paid /
  protest-deadline → regreso-caducado); and it shall apply the Art. 792
  inciso-2 interest-rate fallback ladder on pagaré computations — mora
  interest at the rate STIPULATED for it, absent stipulation at the
  document's YIELD rate, in default of both at the LEGAL rate (the
  rate ladder consumed with FR-158's dated legal-rate config, never a
  hardcoded number), with the subscriber treated as ACEPTANTE for the
  incorporated letra provisions — equated to LIBRADOR when the causal
  or enrichment action is exercised against him (dual-role stamp).
  (LB-007; EVID-225)

### 3.3 Cheque: nature, form and the formulario discipline (Arts. 793-806)

- **SV-CML-FR-149:** The system shall model the *cheque* register with
  the Art. 793 SEVEN-field content checklist — (I) NÚMERO Y SERIE
  (number and series), captured as MANDATORY structured fields, never
  free text; (II) the "cheque" mention inserted in the text; (III)
  name and domicilio of the bank on which it is drawn; (IV)
  unconditional order to pay a determined sum, the quantity in letters
  or numbers — numbers-only quantities requiring a MÁQUINA PROTECTORA
  stamp (flag + effective-amount precedence per FR-144) — with ANY
  agreement inserted in the cheque held AS NOT WRITTEN (non-written
  clause class, informational); (V) beneficiary name or to-bearer
  indication; (VI) place and date of expedition; (VII) autograph
  signature of the librador — and the Art. 794 gate: only instruments
  drawn in conformity with the seven fields AND on a DULY AUTHORIZED
  BANKING INSTITUTION produce cheque effects.
  (LB-008; LB-009; EVID-225)
- **SV-CML-FR-150:** The system shall VOID cheque effects for
  instruments bearing *raspaduras* (scrapings), *testaduras*
  (crossings-out), *interlineados* (interlineations) or *enmiendas*
  (amendments) — an alteration-state flag that blocks payment
  processing and surfaces the Art. 794 no-cheque-effect consequence
  (the record may persist as evidence of the underlying relation;
  only the INSTRUMENT effects are void) — and shall record that the
  cheque is NOT susceptible of PRIOR ACCEPTANCE, any clause subjecting
  it to acceptance being held as not written (Art. 796).
  (LB-009; EVID-225)
- **SV-CML-FR-151:** The system shall track the Art. 806 bank-supplied
  formulario discipline on the checkbook record: cheques are emitted
  on the formularios the bank SUPPLIED to the librador (or the
  librador-owned forms the bank AUTHORIZED — deemed supplied), each
  delivery captured with its receipt-expressed SERIE AND NUMERACIÓN
  range; the cheque register's número/serie fields validate against
  the checkbook ranges (FR-149); and a LOSS of received forms opens
  the IMMEDIATE WRITTEN NOTICE duty to the bank, after which cheques
  presented on the DENOUNCED forms are NOT PAID (blocked-formulary
  state consulted by the payment surface; Art. 810 bank CLEARING of a
  cheque produces the SAME EFFECTS as presentation to the librado —
  clearing events feed the presentation clocks of FR-153/154).
  (LB-011; EVID-225)

### 3.4 Cheque: presentation, protest and the action clocks (Arts. 804-821)

- **SV-CML-FR-152:** The system shall encode the Art. 804-805
  presentation surface: the cheque is ALWAYS PAYABLE AT SIGHT — any
  contrary insertion held as not written — and payable ON
  PRESENTATION even bearing a POST-DATED face, in which case the bank
  is exempt from responsibility for payment and the librador bears the
  same civil-and-penal responsibilities as if the cheque carried the
  presentation date (post-dated flag with the exposure note);
  presentation is to the DRAWN BANK or ANY OF ITS NATIONAL AGENCIES —
  an agency lacking SUFFICIENT FUNDS enjoying SEVENTY-TWO HOURS to
  effect payment (agency-presentation state with its 72-hour respite
  clock, engine-consumed per FR-145).
  (LB-010; EVID-225)
- **SV-CML-FR-153:** The system shall compute the Art. 808
  PRESENTATION CLOCKS by plaza type, each anchored to the expedition
  date with exclude-start-day (FR-145) and shifting only an inhábil
  LAST day: (I) FIFTEEN DAYS following its date when payable in the
  SAME place of drawing (same-plaza); (II) ONE MONTH when expedited
  nationally, payable in a DIFFERENT Salvadorean plaza; (III) THREE
  MONTHS when expedited ABROAD, payable nationally; (IV) THREE MONTHS
  when expedited nationally, payable ABROAD — unless the laws of the
  place of presentation fix another term (foreign-law override slot,
  never defaulted) — surfaced as a countdown state on the cheque
  register (in-time / expiring / expired).
  (LB-012; EVID-225)
- **SV-CML-FR-154:** The system shall track the Arts. 815-816
  protest-or-note requirement and its Art. 795 consequences: a cheque
  PRESENTED IN TIME and unpaid must be protested AT THE LATEST ON THE
  FIFTEENTH DAY FOLLOWING PRESENTATION (exclude-start-day; not
  partial, payment required of the drawee bank's representative —
  except a voluntary partial payment, where protest/annotation covers
  only the insoluta part) — OR the NOTE the drawee bank authorizes on
  the cheque itself (presented in time and unpaid) produces the SAME
  EFFECTS AS PROTEST (equivalent-evidence class); bank CLEARING
  counts as presentation (FR-151); and the Art. 795 documentary
  character follows the timeliness: an unfunded cheque PROTESTED IN
  TIME is a DOCUMENTO EJECUTIVO (summary-execution document) with the
  librador's consequent PENAL responsibilities; NOT protested in time,
  it valdrá only as a PRIVATE DOCUMENT against the librador (document
  character stamp; available funds = those disposable BY CHEQUE,
  informational scope note).
  (LB-013; EVID-225)
- **SV-CML-FR-155:** The system shall implement the Art. 819
  CADUCIDAD CASCADE and the Art. 820 prescription anchors on the
  cheque register: failure to present or protest in the form and terms
  of this chapter CADUCATES (I) the last holder's regreso actions
  against endorsers or avalistas, (II) the endorsers'/avalistas'
  regreso actions among themselves, and (III) the action against the
  librador in the Art. 811-inciso-4 terms and against his avalistas —
  the surviving surface after caducidad being the librador value
  action per Art. 795-II (LB-013/LB-015 kin); the CAMBIARIA ACTIONS
  PRESCRIBE IN ONE YEAR — the LAST HOLDER'S from PRESENTATION, the
  endorsers' and avalistas' from the DAY FOLLOWING their payment —
  with the SPECIAL-CHEQUE overrides consumed by id from §3.5
  (certified 6 months from conclusion of the presentation term,
  FR-157/LB-018; traveller 2 years from circulation, FR-157/LB-019;
  circular 6-month collection, FR-157/LB-020) and the enrichment
  residual clock of FR-146 behind them; the Art. 995-II "acciones
  derivadas del cheque" row of the prescription matrix defaults to
  these same anchors (consumed from FR-160 by id, never restated
  there).
  (LB-014; EVID-225)
- **SV-CML-FR-156:** The system shall compute the Art. 811/821
  bank-refusal indemnity floor: when a bank refuses WITHOUT JUSTIFIED
  CAUSE to pay a properly drawn cheque, it answers to the LIBRADOR
  HAVING FUNDS for the damages of its refusal (the holder cannot
  compel payment, his rights remaining safe against the librador; the
  Art. 809-II retention is not deemed refusal) — and the
  indemnification may IN NO CASE be LESS THAN TWENTY PER CENT of the
  cheque's value (computed floor surfaced on the refusal event; the
  Art. 830 traveller's-cheque analogue — damages never below 20% of
  the unpaid value, against the LIBRADOR — carries the same floor);
  the protested holder's claim set (value + LEGAL interest + expenses
  against any endorser or the librador, paying endorser subrogated)
  is recorded as the exposure surface.
  (LB-015; LB-019; EVID-225)
### 3.5 Special cheques: the payment-configuration taxonomy (Arts. 822-837)

- **SV-CML-FR-157:** The system shall carry the Art. 822 special-cheque
  taxonomy as PAYMENT-CONFIGURATION METADATA on the cheque register
  (kind + its configuration constraints and own clocks, each blocking
  or relaxing the §3.3/3.4 defaults as stated): **cruzado** — two
  parallel lines on the face, GENERAL (no bank indicated) or ESPECIAL
  (bank indicated); endosable but payable ONLY to a bank of the
  Republic — under special crossing precisely to the indicated bank;
  general may convert to special, special never to general; the
  crossing is an ESSENTIAL PART that may not be erased or altered;
  **para abono en cuenta** — the "para abono en cuenta" insertion
  forbids cash payment (credit only to the holder's account or
  deposit bank; face insertion credits the first holder,
  endorsement-insertion the person favoured by that endorsement;
  other-form payment = irregular-payment responsibility), makes the
  cheque NON-NEGOTIABLE from insertion, the clause being unerasable,
  and the favoured person's signature NOT required; **certificado** —
  written certification request, declaration of sufficient funds;
  certification NEVER partial, the certified cheque NON-NEGOTIABLE,
  the bank solely responsible (librador and endorsers released);
  "acepto"/"visto"/"bueno" or equivalents subscribed by the bank, or
  an authorized person's mere signature, EQUAL certification;
  revocable by RETURNING the cheque for cancellation; the bank
  CHARGES the value to the librador's account from certification; its
  cambiaria actions against the certifying librado prescribe in SIX
  MONTHS from conclusion of the presentation term; **de viajero** —
  issued by the librador on his own account, payable by his main
  establishment, branches and correspondents in the Republic or
  abroad; to a DETERMINED PERSON, the payer verifying the tomador's
  signature against the signature certified on the cheque by whoever
  circulated it; presentable AT ANY TIME while prescription has not
  run; non-immediate payment → refund + damages ≥20% (FR-156); the
  circulating correspondent bears endorser obligations and reimburses
  unused cheques; cambiaria actions against issuer/circulator
  prescribe in TWO YEARS from circulation; **limitado / con provisión
  garantizada** — special formulas containing the denomination,
  delivery date, MAXIMUM amount printed in words and numbers, and a
  circulation time limit NOT exceeding THREE MONTHS (payable in El
  Salvador) / ONE YEAR (payable abroad); formula delivery EQUALS
  certifying the sums for the validity time; NEVER drawable to
  bearer; **circular** — a banking institution's PROMISE to pay at
  any of its establishments other than the drawing one, to a
  determined person; the holder has SIX MONTHS to collect at any
  signaled establishment or the issuing institution (the Art. 808
  presentation terms do NOT condition the direct and recurso actions);
  endorsement warranties AUTHENTICITY only, and from emission the
  OWNERSHIP of the funds provision transfers to the original tomador
  and successive endorsees; **de caja o de gerencia** — ONLY banking
  establishments may issue them, chargeable to their own offices,
  ALWAYS drawn to a determined person.
  (LB-016; LB-017; LB-018; LB-019; LB-020; EVID-225)

### 3.6 Mora interest and solidarity (Arts. 960-962)

- **SV-CML-FR-158:** The system shall compute mora interest with the
  Art. 960 fallback ladder: the moroso debtor pays the PACTADO
  (agreed) interest and IN DEFAULT THE LEGAL interest as mora
  indemnification; where the obligation's object is a thing certain
  and determined or determinable, the interest computes on the VALUE
  OF THE THING — determined save convenio by the PLAZA PRICE on the
  maturity day, or the BOLSA quotation, failing both by PERITOS
  (valuation-basis metadata; the perito appraisal is external); and
  the LEGAL mercantile interest rate is DATED CONFIGURATION fixed
  periodically by the Economía office (print: "Secretaría de
  Economía") — a dated rate table with valid_from/valid_to and
  instrument reference, NO shipped default (SOQ-26; OQ-001): mora
  computations requiring the legal rate BLOCK with a
  configuration-missing flag until the rate is loaded, and NEVER fall
  back to a hardcoded number (the pagaré ladder of FR-148 consumes
  this same config); the Art. 960 base text cited (LB-021) is the
  pre-110_ print for the pactado/legal ladder limbs — the 110_
  (D.L. 295-2022) inciso tercero (BCR consultation) and Art. 960-A
  (nullity of the usurious-interest slice) ride the awareness LB-028,
  adding no computation mechanics here.
  (LB-021; EVID-226; awareness LB-028; EVID-408)
- **SV-CML-FR-159:** The system shall record the Art. 962 solidarity
  default on mercantile obligation records: save legal provision or
  EXPRESS contrary pact, CO-DEBTORS AND GUARANTORS in commercial
  matters are SOLIDARY — including non-merchants — so a multi-debtor
  mercantile obligation carries solidary-liability metadata (full
  claim against each co-debtor/guarantor; the pacto-expreso and
  legal-provision exceptions recorded when present, flipping the
  default). (LB-022; EVID-226)

### 3.7 The mercantile prescription matrix (Arts. 995-998)

- **SV-CML-FR-160:** The system shall implement the Art. 995
  prescription matrix VERBATIM as the receivable/payable AGING
  DEFAULTS table — the classification and term assigned to every
  mercantile claim/obligation record: **6 months** — actions for
  RECTIFICATION of cuenta-corriente balances; **1 year** — nullity of
  sociedad assembly agreements or of their celebration; unjust
  enrichment from the giro of títulos valores; actions derived from
  the CHEQUE; REGRESO actions of the letra de cambio; claims for
  VICIOS of the thing sold; actions concerning the TRANSPORT
  contract; and liability claims against sociedad administrators,
  auditors and interventores; **2 years** (save the preceding
  exceptions) — actions derived from the contracts of sociedad,
  compraventa, suministro, depósito, comisión, estimatorio,
  edición, hospedaje, participación, garantía AND OTHERS lacking
  distinct terms in this Code or special laws (catch-all row with
  special-law override slot); **5 years** — actions derived from
  CREDIT contracts, counted from the date of the LAST RECOGNITION of
  the obligation BY THE DEBTOR, and in the same term the OTHER
  mercantile rights — with each row's anchor event: the 6m/1y/2y rows
  anchor to their action-specific start (the cheque row consuming
  FR-155's anchors by id); the 5y row anchors to the recognition
  stamp of FR-161; the matrix is the DEFAULT layer — a special law or
  this Code fixing a distinct term for a contract family overrides
  the row (dated override slot), and consumers
  (`09_sales-contracts.md` vicios/compraventa/suministro/comisión
  surfaces, the society files' nullity/admin-liability rows, the
  aging reports) CITE SV-CML-FR-160 BY ID and never restate the
  terms. (LB-023; EVID-226)
- **SV-CML-FR-161:** The system shall STAMP recognition events on the
  obligation ledger for the 5-year credit-contract clock: the
  Art. 995-IV term runs from the date of the LAST RECOGNITION of the
  obligation BY THE DEBTOR — every recorded debtor-side recognition
  event (a payment, a partial payment acknowledged as such, an
  explicit acknowledgment recorded on the obligation) sets
  last_recognized_on = event date, RESTARTING the 5-year prescription
  anchor (recognition events on payments/partials are captured by the
  payment flow itself; the clock never advances past the newest
  stamp); the classification of other candidate events (interest
  capitalization, dunning entries) stays open (OQ-003 — the
  Civil-Code interruption catalog is not in the corpus).
  (LB-023; EVID-226)
- **SV-CML-FR-162:** The system shall encode the Arts. 996-998
  caducidad regime on every deadline object whose miss carries a
  caducidad penalty (the cheque presentation/protest clocks of
  FR-153/154, the pagaré protest clock of FR-148, and future
  caducidad-class clocks citing this FR by id): the Código Civil's
  prescription INTERRUPTION/SUSPENSION norms DO NOT APPLY to
  caducidad terms — no suspension or interruption is computed, the
  only statutory suspension being FORCE MAJEURE (recorded as a dated
  suspension with automatic resumption when it ceases); a PACT fixing
  a caducidad term that makes the right's exercise excessively
  difficult MAY BE RESCINDED (judicial — flag only); and the parties
  CANNOT modify the LEGAL caducidad regime nor renounce
  law-established caducidad (pact-override attempts on statutory
  caducidad surfaces marked void-of-effect).
  (LB-024; EVID-226)

### 3.8 Proof of mercantile obligations (Arts. 999-1003)

- **SV-CML-FR-163:** The system shall mark the Art. 999 statutory
  proof classes on the evidence objects it holds for a mercantile
  obligation: I. public/authentic/private instruments; II. FACTURAS —
  the invoice record (DTE-era included) carries the statutory-proof
  class with its retention duties consumed from SV-CML-FR-028 row b
  BY ID (the anexas-a-la-contabilidad clock) and the DTE archive kin
  as POINTER ONLY (SV-EINV-FR-154 Tier-A local mirror,
  SV-EINV-FR-155 exact-structure conservation — the e-invoicing wave
  owns the mechanics, never restated here); III./IV. postal and
  recognized telegraphic correspondence; V. REGISTROS CONTABLES — the
  accounting records, whose evidentiary fitness rides the
  legally-kept discipline consumed from SV-CML-FR-025 BY ID; VI.
  witnesses; VII. other legally admitted means (class catalog as
  document metadata; no hierarchy computed beyond FR-164).
  (LB-025; EVID-226; cross-ref SV-CML-FR-025, SV-CML-FR-028,
  SV-EINV-FR-154, SV-EINV-FR-155)
- **SV-CML-FR-164:** The system shall implement the Art. 1002
  evidentiary priority for DIVERGING COPIES of one contract: the
  matter is elucidated against the contractors' ACCOUNTING ENTRIES —
  the mercantile accounting of the party keeping it IN LEGAL FORM
  makes fe (prevails); where BOTH keep it legally, any other means of
  proof; where both allege proofs of equal force, the Judge resolves
  for the DEFENDANT — recorded as a resolution-priority surface keyed
  to the legally-kept state (FR-163/SV-CML-FR-025 by id): a
  diverging-copy dispute record computes which party's books are
  legally kept and surfaces the prevailing side (or the both-legal →
  other-proof → judge-favors-defendant cascade as informational law,
  never adjudicated).
  (LB-026; EVID-226)

### 3.9 Scope notes: letra de cambio detail and the arbitraje derogation — no FRs

Two boundaries of this file's article set are recorded as scope, not
requirements: (i) the LETRA DE CAMBIO chapter mechanics (Arts. 702-787
zone) were skimmed in the evidence (EVID-225 doubts) — this file uses
only the general chapter (Arts. 623-653), the pagaré's Art. 792
incorporation references and the Art. 995-II regreso-prescription row;
no letra-specific FR derives until the detail is acquired (OQ-002);
(ii) TÍTULO II ARBITRAJE COMERCIAL (Arts. 1004-1012) is printed
DEROGATED (reform (21), LB-027) — superseded by special arbitration
legislation outside this corpus; no arbitration FR derives here.
## 4. Data Model

Layer semantics: payment instruments live on Odoo-native payment and
accounting objects (account.payment family + l10n_sv_commerce
registers) — wave default `odoo` (§5). The drawee bank, the Notario
(protest/actas), the Economía office (rate publication) and the courts
are external authorities: the system tracks their acts and
publications as referenced dated facts; it never emulates them.
Day-count arithmetic is consumed from the fiscal-reporting engine
(SV-FREP-FR-202..204 by id).

**Título valor base (pagaré/cheque/common):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.payment.instrument | instrument_kind | select | pagaré · cheque · otro_titulo_valor (letra kin = OQ-002) | FR-142 |
| l10n_sv_commerce.payment.instrument | art625_checklist · castellano_ok | computed checklist · boolean | I name · II date+place of emission · III prestaciones/derechos · IV place of performance · V emitter signature; emission/performance domicilio defaults (librador/obligado) + multi-place election flag | FR-142, FR-143 |
| l10n_sv_commerce.payment.instrument | amount_words · amount_figures · protectora_marked · effective_amount · amount_basis | monetary ×3 · computed · select | words-over-figures; >2 mentions → lower sum; máquina protectora marking prevails | FR-144 |
| l10n_sv_commerce.payment.instrument | salvo_buen_cobro · enrichment_deadline | boolean · computed date | given-in-payment presumption (provisional settlement); 1y from cambiaria extinction | FR-146 |

**Pagaré register:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.pagare | art788_checklist | computed checklist | 6 ordinals: pagaré mention · unconditional promise · payee · epoch+place of payment · subscription date+place · subscriber signature | FR-147 |
| l10n_sv_commerce.pagare | vencimiento_state · lugar_pago | computed · computed | sin fecha → a la vista; sin lugar → subscriber's domicilio (defaulted provenance flagged) | FR-147 |
| l10n_sv_commerce.pagare | vista_plazo_deadline · presentation_acta_ref · domiciled_state · protest_deadline · regreso_state | date · document ref · flag · date · select | 1-year vista-plazo window (exclude start day); notarial acta; pagador diputado or subscriber; protest at fixed domicilio; omission (non-subscriber payer) → regreso caducado | FR-148 |

**Cheque register + checkbook:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.cheque | numero · serie | char · char | MANDATORY capture (Art. 793-I); validated against checkbook ranges | FR-149, FR-151 |
| l10n_sv_commerce.cheque | art793_checklist · drawee_bank_ref · bearer | computed checklist · many2one · boolean | 7 ordinals incl. letters-or-numbers rule + protectora when numbers-only; convenios = non-written class; authorized banking institution gate | FR-149 |
| l10n_sv_commerce.cheque | alteration_state | select | none · raspaduras/testaduras/interlineados/enmiendas → NO cheque effects (Art. 794) | FR-150 |
| l10n_sv_commerce.checkbook | serie · numeracion_from/to · receipt_ref · loss_notice_on · blocked | char · int ×2 · ref · date · computed | bank-supplied/authorized formulas with receipt-expressed ranges; loss → immediate written notice → denounced forms not paid | FR-151 |
| l10n_sv_commerce.cheque | presentation_state · agency_72h_until · postdated | select · datetime · boolean | drawn bank or any national agency; agency short-of-funds 72h respite; post-dated still payable at presentation | FR-152 |
| l10n_sv_commerce.cheque | plaza_type · presentation_deadline | select · computed date | same_plaza 15d · national_cross_plaza 1m · issued_abroad_payable_sv 3m · issued_sv_payable_abroad 3m (foreign-law override slot) | FR-153 |
| l10n_sv_commerce.cheque | presented_on · protest_deadline · protest_kind · document_character | datetime · computed date · select · select | 15th day following presentation (exclude start); protesto vs bank-note equivalence (Art. 816); clearing = presentation (Art. 810); ejecutivo (protested in time) vs privado (Art. 795) | FR-154 |
| l10n_sv_commerce.cheque | caducidad_state · prescription_anchor | computed · computed date | Art. 819 cascade (regreso I/II + librador 811-IV); Art. 820 1y — holder from presentation, endorsers/avalistas from day after payment; special-kind overrides | FR-155 |
| l10n_sv_commerce.cheque | refusal_indemnity_floor | computed monetary | ≥20% of cheque value (Arts. 821/830) | FR-156 |
| l10n_sv_commerce.cheque | special_kind · special_config · special_clock | select · json/config · computed date | cruzado (general/especial; bank-only payment; unerasable) · abono_en_cuenta (credit-only; non-negotiable; unerasable; no signature) · certificado (non-partial; non-negotiable; bank-only responsibility; charge-at-certification; revoke-by-return; 6m from presentation-term end) · viajero (any-time presentation; ≥20%; 2y from circulation) · limitado (max amount words+numbers; 3m national / 1y abroad; never bearer) · circular (bank promise; 6m collection; endorsement = authenticity only) · caja_gerencia (bank-issued; determined person) | FR-157 |

**Mora interest + solidarity:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_commerce.legal.interest.rate | valid_from · valid_to · rate · instrument_ref | date · date · float/percent · char | Economía-published DATED CONFIG (SOQ-26; OQ-001) — NO shipped default; empty table ⇒ mora legal-rate computations BLOCK with config-missing flag | FR-158 |
| account.move.line (mora exposure) | mora_rate_basis · valuation_basis | computed · select | pactado → legal fallback; cosa cierta/determinable → plaza price / bolsa / peritos | FR-158 |
| account.move.line / obligation record | solidarity_state · contrary_pact | computed · boolean | codeudores/fiadores solidarios incl. non-merchants (Art. 962); legal-provision/pacto-expreso exceptions flip | FR-159 |

**Prescription matrix + recognition events:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line / account.move | prescription_class · prescription_term · prescription_anchor | select · computed · computed date | cta_cte_rectificacion 6m · cheque_1y · enriquecimiento_titulos_1y · letra_regreso_1y · vicios_1y · transporte_1y · asambleas_nulidad_1y · admin_auditores_interventores_1y · contrato_2y (sociedad/compraventa/suministro/depósito/comisión/estimatorio/edición/hospedaje/participación/garantía/catch-all) · credito_5y (from last recognition) · otros_derechos_5y; special-law override slot per row | FR-160 |
| l10n_sv_commerce.recognition.event | event_date · event_kind · obligation_ref | date · select · many2one | payment · partial_payment_acknowledgment · explicit_acknowledgment (debtor-side acts; Art. 995-IV anchor) | FR-161 |
| account.move.line | last_recognized_on | computed date | newest recognition stamp restarts the 5y anchor | FR-161 |
| l10n_sv_commerce.deadline (caducidad class) | caducidad_regime · force_majeure_suspensions | computed · one2many dated | no CC interruption/suspension; fuerza mayor suspends with auto-resumption; statutory-caducidad pacts void; excessive-difficulty rescission = judicial flag | FR-162 |

**Proof metadata:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| invoice / document record | art999_proof_class | select | instrumento_publico_autentico_privado · factura · correspondencia_postal · telegrafica_reconocida · registro_contable · testigos · otros_admitidos (factura + registros contables = the system-held statutory classes) | FR-163 |
| document/invoice record | retention_link · dte_archive_pointer | many2one · pointer | SV-CML-FR-028 row b (anexas clock) BY ID; DTE archive = SV-EINV-FR-154/155 POINTER ONLY | FR-163 |
| l10n_sv_commerce.copy.divergence | party_books_legal · resolution_surface | computed ×2 · select | Art. 1002 cascade: legally-kept books make fe → both legal → other proof → equal force → judge favors defendant (informational) | FR-164 |
## 5. Odoo Mapping

Layer semantics for this wave: payment instruments, aging and proof
metadata are Odoo-native surfaces (account.payment +
account.payment.register, account.move/line, l10n_sv_commerce
registers) — every FR maps `odoo`; none touch DTE
generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`), so no `saas` rows
are introduced. E-invoicing kin (pointer only): the factura proof
class rides the invoice/DTE documents owned by the e-invoicing wave;
the DTE archive mechanics are SV-EINV-FR-154/155, cited by id. Day
arithmetic is consumed from SV-FREP-FR-202..204 by id. Model names
are stable across Odoo 17/18/19/20; cheque-printing surfaces ride the
check-printing module family (check numbering/serie = the Art. 793-I
capture), with no version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-142 | odoo | l10n_sv_commerce.payment.instrument | art625_checklist, domicilio defaults | Literal-and-autonomous object; multi-place election flag |
| FR-143 | odoo | l10n_sv_commerce.payment.instrument | castellano_ok | Form-defect warning; permitted translation recorded |
| FR-144 | odoo | l10n_sv_commerce.payment.instrument | effective_amount, amount_basis | Words > figures; >2 mentions → lower; protectora prevails |
| FR-145 | odoo | l10n_sv_commerce.payment.instrument (+ every clock in this file) | deadline conventions | Art. 638: last-day-inhábil extension, intermediate feriados count, exclude start day — hábil arithmetic consumed from SV-FREP-FR-202..204 by id |
| FR-146 | odoo | account.payment + l10n_sv_commerce.payment.instrument | salvo_buen_cobro, enrichment_deadline | Provisional settlement on instrument payments; 1y residual clock from cambiaria extinction |
| FR-147 | odoo | l10n_sv_commerce.pagare | art788_checklist, vista/domicilio defaults | 6-field content; no-date → a la vista; no-place → subscriber's domicilio |
| FR-148 | odoo | l10n_sv_commerce.pagare | vista_plazo_deadline, protest_deadline, regreso_state | 1-year vista-plazo window; domiciled protest at fixed domicilio; omission → regreso caducidad; Art. 792 rate ladder via FR-158 config |
| FR-149 | odoo | l10n_sv_commerce.cheque | numero, serie, art793_checklist | Número+serie MANDATORY structured capture; 7-field checklist; authorized-bank gate |
| FR-150 | odoo | l10n_sv_commerce.cheque | alteration_state | Raspaduras/testaduras/interlineados/enmiendas → no cheque effects; no-prior-acceptance class |
| FR-151 | odoo | l10n_sv_commerce.checkbook | serie/numeración ranges, loss_notice, blocked | Bank-supplied formulario discipline; clearing = presentation (Art. 810) feeds FR-153/154 |
| FR-152 | odoo | l10n_sv_commerce.cheque | presentation_state, agency_72h_until, postdated | Always a la vista; post-dated payable on presentation; agency 72h respite |
| FR-153 | odoo | l10n_sv_commerce.cheque | plaza_type, presentation_deadline | 15d same-plaza / 1m national / 3m-3m cross-border; foreign-law override slot; countdown state |
| FR-154 | odoo | l10n_sv_commerce.cheque | protest_deadline, protest_kind, document_character | 15th day after presentation; protest vs bank-note equivalence; ejecutivo vs privado per timeliness |
| FR-155 | odoo | l10n_sv_commerce.cheque | caducidad_state, prescription_anchor | Art. 819 cascade; Art. 820 1y anchors; special-kind overrides from FR-157 |
| FR-156 | odoo | l10n_sv_commerce.cheque | refusal_indemnity_floor | ≥20% floor (Arts. 811/821/830); holder claim-set exposure |
| FR-157 | odoo | l10n_sv_commerce.cheque | special_kind, special_config, special_clock | 7-kind taxonomy as payment-configuration metadata with own clocks (6m/2y/6m) |
| FR-158 | odoo | l10n_sv_commerce.legal.interest.rate + account.move.line | dated rate table; mora_rate_basis | SOQ-26: Economía DATED CONFIG, NO shipped default; pactado→legal; cosa-value base (plaza/bolsa/peritos); blocks when unconfigured |
| FR-159 | odoo | account.move.line | solidarity_state, contrary_pact | Codeudores/fiadores solidarios incl. non-merchants; exceptions flip the default |
| FR-160 | odoo | account.move.line / account.move | prescription_class/term/anchor | Art. 995 matrix VERBATIM as aging defaults; special-law override slot; consumed by 09/society files by id |
| FR-161 | odoo | l10n_sv_commerce.recognition.event + account.move.line | last_recognized_on | Recognition events (payment/partial/acknowledgment) stamp and restart the 5y anchor |
| FR-162 | odoo | l10n_sv_commerce.deadline (caducidad class) | caducidad_regime, force_majeure_suspensions | No CC interruption/suspension; fuerza-mayor-only suspension; statutory-caducidad pacts void |
| FR-163 | odoo | invoice/document records | art999_proof_class, retention_link | Facturas + registros contables = statutory proof; SV-CML-FR-025/028 and SV-EINV-FR-154/155 by id/pointer |
| FR-164 | odoo | l10n_sv_commerce.copy.divergence | party_books_legal, resolution_surface | Art. 1002: legally-kept books make fe; both-legal → other proof; equal force → judge for defendant |

Version-regime notes (D12): no dated values live in this file except
the deliberately-unconfigured legal interest rate (SOQ-26; OQ-001 —
dated config with NO shipped default, never hardcoded). All day/month
terms (15d/1m/3m/72h/1y/2y/5y/6m) and proportions (≥20%) are
un-reformed statutory text under the SOQ-22 residual watch, stored as
code constants with provenance. Modern payment-system evolution beyond
the CC truncation layer of 112_ (LB-029 — the BCR Consejo Directivo
compensation norms and the current interbank rules) remains outside the
corpus (OQ-004, narrowed W23); the CC clocks remain the evidenced
defaults.

## 6. Acceptance Criteria

- **AC-001:** Given a título valor whose amount reads "mil dólares"
  in words and "$10,000.00" in figures, when the FR-144 precedence
  computes, then the effective amount is the WORDS sum (US$1,000);
  given the amount appearing twice in figures ($1,200 and $1,000),
  then the effective amount is the LOWER (US$1,000); given a
  máquina-protectora marking of $1,500, then the marking prevails
  over words and figures alike (FR-144).
- **AC-002:** Given an instrument deadline whose last day falls on a
  Sunday or asueto, when FR-145 computes, then the term extends to
  the next hábil day via the shared engine (SV-FREP-FR-203 by id);
  given intermediate feriados inside the term, then they COUNT (no
  hábil-only compression); and given any clock in this file, then the
  day serving as point of departure is never counted (FR-145).
- **AC-003:** Given a pagaré recorded without maturity date and
  without place of payment, when the FR-147 defaults resolve, then
  the record shows pagadero A LA VISTA with place of payment = the
  subscriber's domicilio, both flagged as defaulted (FR-147).
- **AC-004:** Given a same-plaza cheque expedited 01-Jun, when the
  FR-153 clock computes, then the presentation deadline is 16-Jun
  (the fifteen days FOLLOWING its date); given a nationally expedited
  cheque payable in another Salvadorean plaza, then the deadline is
  one month from expedition; given one expedited abroad payable in
  El Salvador (or nationally payable abroad), then three months —
  each shifting only an inhábil last day (FR-153).
- **AC-005:** Given a cheque presented in time on 01-Jul and not
  paid, when FR-154 tracks, then the protest deadline is 16-Jul (the
  fifteenth day following presentation); given instead the drawee
  bank's note on the cheque itself (presented in time, unpaid), then
  the note produces the same effects as protest and no separate
  protest is required; given bank clearing of the same cheque, then
  the clearing counts as presentation (FR-154; FR-151).
- **AC-006:** Given an unfunded cheque protested within the legal
  term, when the FR-154 character stamps, then it is a DOCUMENTO
  EJECUTIVO with the librador penal-exposure note; given the same
  cheque NOT protested in time, then it valdrá as a PRIVATE DOCUMENT
  against the librador and the FR-155 cascade caducates the regreso
  actions (endorsers/avalistas/among themselves) and the
  Art. 811-inciso-4 librador action (FR-154, FR-155).
- **AC-007:** Given a bank's unjustified refusal to pay a properly
  drawn US$5,000 cheque of a funded librador, when FR-156 computes,
  then the indemnity floor surfaced is ≥20% = US$1,000 (never below),
  with the holder's rights noted as safe against the librador
  (FR-156).
- **AC-008:** Given a cheque record flagged with raspaduras, when
  FR-150 evaluates, then payment processing is blocked with the
  Art. 794 no-cheque-effect reason while the record persists as
  underlying-relation evidence (FR-150).
- **AC-009:** Given a traveller's cheque whose immediate payment
  failed, when FR-156/FR-157 evaluate, then the refund + damages
  surface carries the ≥20% floor and the 2-year prescription clock
  runs from the recorded circulation date; given a certified cheque,
  then its clock is 6 months from conclusion of the presentation
  term; given a circular cheque, then the holder has 6 months to
  collect unconstrained by the Art. 808 terms (FR-156, FR-157).
- **AC-010:** Given a mora exposure with no pactado rate and an EMPTY
  legal-rate table, when FR-158 computes, then the computation BLOCKS
  with the configuration-missing flag (no number is produced); given
  a dated Economía rate loaded with valid_from ≤ the maturity date,
  then that rate applies as the legal fallback (FR-158).
- **AC-011:** Given a compraventa receivable and a credit-contract
  receivable, when FR-160 classifies, then the former carries the 2y
  contract class and the latter the 5y credit class; given a partial
  payment recorded 01-Mar on the credit receivable, when the FR-161
  stamp applies, then last_recognized_on = 01-Mar and the 5y
  prescription anchor RESTARTS from that date (FR-160, FR-161).
- **AC-012:** Given two parties presenting diverging copies of one
  contract where only party A's books are legally kept (FR-163/
  SV-CML-FR-025 by id), when FR-164 resolves, then A's accounting
  entries make fe; given BOTH parties' books legally kept, then the
  cascade surfaces other-proof → equal-force → judge-favors-defendant
  as informational law (FR-164).
- **AC-013:** Given an invoice record and the accounting records of a
  legally-kept ledger, when FR-163 marks proof classes, then the
  invoice carries the Art. 999-II factura class with its retention
  link (SV-CML-FR-028 row b by id) and the ledger the V registro
  contable class, the DTE archive appearing as pointer only
  (SV-EINV-FR-154/155) (FR-163).
- **AC-014:** Given a cheque presentation clock with a recorded
  force-majeure suspension window, when FR-162 evaluates, then the
  caducidad term suspends for exactly that window and resumes
  automatically; given a recorded pact attempting to modify the
  statutory caducidad regime, then the surface flags it
  void-of-effect (FR-162).
- **AC-015:** Given a payment allocation settled with a pagaré, when
  FR-146 applies, then the receivable settles PROVISIONALLY under the
  salvo-buen-cobro presumption and extinguishes only on the
  instrument's effective collection; given the instrument's cambiaria
  action extinguished 01-Feb, then the enrichment residual clock
  runs to 01-Feb + 1 year (FR-146).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-26 (carrying 07_ OQ-6): the mercantile LEGAL INTEREST RATE is fixed periodically by the Economía office (Art. 960 final inciso, print "Secretaría de Economía") but the current rate instrument — publication vehicle, current values, effective dating — is outside the corpus. FR-158 ships the dated config slot with NO shipped default and blocks legal-rate computations while unconfigured; when the instrument is pinned (sources-registry acquisition), load the dated table and keep it SOQ-26-governed — never hardcode. | no | Takumi S5 (sources watch) | open |
| OQ-002 | The letra de cambio chapter (Arts. 702-787 zone) was skimmed in the 07_ evidence (EVID-225 doubts): only the general chapter, the pagaré's Art. 792 incorporation list and the Art. 995-II regreso row are used here. If a sales-flow or letra register surface is ever required, acquire/extract the letra detail before writing FRs; the Art. 792 inciso-1 incorporation list is recorded but not mechanized. | no | Takumi S5 (sources watch) | open |
| OQ-003 | Art. 995-IV anchors the 5y credit-contract term on the "último reconocimiento de la obligación por parte del deudor" without defining recognition events, and Art. 996 excludes the Código Civil's interruption/suspension norms from caducidad (implying they govern prescription) — the Civil Code's interruption catalog is not in the corpus. FR-161 stamps the canonical events (payment, partial-payment acknowledgment, explicit acknowledgment); the classification of further candidate events (interest capitalization, dunning) and any interruption semantics beyond the recognition anchor stay open until the CC corpus lands. | no | Takumi S5 + legal review | open |
| OQ-004 | (narrowed W23 T4) Cheque truncation is NOW evidenced in the corpus — 112_ D.L. 972-2024 Sección "F" Arts. 838-A..838-E rides the awareness LB-029 (image presentation = physical-presentation effects; BCR reglamenta y administra compensation; no FR mechanics). Still un-acquired — ACQUISITION CANDIDATES: the BCR Consejo Directivo compensation norms (owed ≤90 días from the 19-abr-2024 vigencia) and the current interbank rules implementing them, plus electronic clearing beyond truncation (watch). The CC clocks and the clearing-equals-presentation rule (Art. 810) remain the evidenced defaults; any clearing-house rule set must be acquired first and wired as a dated override, never as an edit of the CC defaults. | no | Takumi S5 (sources watch) | open |

