# SV — Taxation — IVA adjustments and fixed assets: the Art. 62-64 débito/crédito adjustment windows (with the medicines lot registry), the Arts. 71-72 fixed-asset regime (Rgto. Art. 26 document routing) and the Art. 7-g/h reorganization-transfer taxability gates (Ley IVA Arts. 62-64, 71-72, 7 g)-i); Reglamento IVA Art. 26)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the adjustment and
fixed-asset tail of El Salvador's IVA (D.L. 296-1992): the Art. 62
*ajustes del débito fiscal* — the three-month window for subtracting the
tax of returned goods, *envases o depósitos*, annulled or rescinded
operations (measured from the ENTREGA DE LOS BIENES or the PERCEPCIÓN DEL
PAGO DE LOS SERVICIOS, always under proof that the value was already
considered in the débito calculation of the same or an earlier period —
the landing pad of the Art. 9 exchange/return path routed here by the
framework file); the MEDICINES EXTENSION — for transfers of
*medicamentos y especialidades farmacéuticas perecederos para uso y
consumo humano* the window may extend HASTA DOS AÑOS, with the twin
statutory consequences: the *caducidad* of the fiscalización and
liquidación-oficiosa faculties extends TWO YEARS counted from the tax
period of the ORIGINAL adjusted operations, and the contribuyente must
carry the detailed lot registry of products sold and returned with its
SEVEN mandatory fields (production or import-document lot number; name and
presentation; expiration date; inventory entry and exit dates; the CCF
number — which must itself print the lot number and expiration date —
and the CCF date; the client code), the credit note referencing the CCF
number PLUS the returned lot with an appropriate product description,
the accounting backing through the *cuenta de inventario de producto
vencido* and its *registro de control* annotation, and the destruction
acts levanted and subscribed by the SANITARY AUTHORITIES at the moment
of destruction with the descriptive per-medicament detail and production
lot; the Art. 62-1-b subtraction of *rebajas de precio, bonificaciones y
descuentos u otras deducciones normales del comercio, no condicionadas y
de carácter general* under the same prior-computation proof plus the
forma-y-condiciones demonstration (the related CCFs and the tax period
identified); the Art. 62-2 ADDITIONS — price increments, *reajustes*,
gastos and interests including mora interest; differences from
transferring an UNDULY LOW débito; and any sum transferred in excess
UNLESS its restitution to the acquirer or service user is proven — all
adjustments effected exclusively through the CCF and notas machinery
(Art. 100 as printed, re-anchored to CT Art. 110 — the e-invoicing
NCE/NDE stack is the document surface, cited by id); the Art. 63
*ajustes del crédito fiscal* — the subtractions (annulled/rescinded
acquisitions, price reductions and excess transfers, always previously
computed and evidenced in CCF or the CT-110 notas); the ADDITION of late
received-and-registered CCF/notas de débito tax usable up to the THREE
FOLLOWING tax periods from emission; the notas de crédito rule (reduce
the crédito in their EMISSION period, save late receipt proven — then up
to three following periods) with the overflow duty: past that term, the
contribuyente is OBLIGED to modify the declarations of the emission
period applying the whole entitled credit or diminishing it
correspondingly (the D9 freeze-at-filing interplay and the F-07
three-prior-period purchase window's legal root, both consumed by id);
and the Art. 64 determination bottom line — the tax payable is the
difference of the débito (post-Art.-62) over the crédito (post-Art.-63,
import/internación IVA included *en su caso*) of the same period. It
also owns the fixed-asset regime: the Art. 71 rule that transfers of
*activo fijo o de capital* goods are NOT hecho generador (no giro, no
habitualidad) UNLESS effected BEFORE four years of the goods' afectación
to that asset (the alta-date D15 anchor); the Art. 72 credits — the
acquisition crédito of capital goods destined to the activo fijo is
deductible against the same period's gravada débito or the following
ones until total deduction, PLUS the credits of goods and services
destined to REPAIR or to remedy the deterioration corresponding to the
normal use or enjoyment of the activo-fijo INMUEBLES, and those destined
to the REMODELING of inmuebles — owned or not — to place them in
conditions of use in the business giro WITHOUT increasing their value or
useful life; and the Reglamento Art. 26 document routing (Factura or CCF
if the transfer is a hecho generador; ANY OTHER document type
otherwise; Art. 73's certificates are DEROGADO). Finally it carries the
Art. 7 reorganization-transfer taxability gates in their determination
consequence: aportes of giro goods (7-f) and own-giro transfers on
occasion of society modification, ampliación, transformación, fusión or
other reorganization forms (7-g) are TAXED transfers; the 7-h
liquidation/disminución adjudications are NOT subject to gravamen ONLY
when the adjudicatario is the SAME socio or accionista who aportó the
good AND the good was not charged with this tax (both conditions as
recorded checks); and establecimiento/empresa-mercantile transfers are
taxed only as to the *activo realizable* bienes muebles corporales
included in the operation (7-i).

It does **not** cover: the débito/crédito base computation (rate × base
per operation — `09_iva-base-rate.md` SV-TAX-FR-241 owns the engine;
this file adjusts its output, never recomputing it); the base-side
mirror of commercial discounts (Art. 52 — `09_iva-base-rate.md`
SV-TAX-FR-237, consumed by id); the credit-eligibility gates, formal
requirements and blocked states (`10_iva-credit-deductibility.md`
SV-TAX-FR-246/251/254 — the eligible crédito this file adjusts is T4's
engine output, by id); the Art. 66 proportionality and the Arts. 67-70
remanente regime (`11_iva-pro-rata-remanente.md` SV-TAX-FR-275/278 —
the post-adjustment crédito feeds T5's pro-rata run and remanente
computation, by id); the exemption classification that bounds which
operations carry débito at all (`08_iva-exemptions.md`
SV-TAX-FR-206/224, by id); the operation taxonomy seed and the Art. 9
return ROUTING decision (`07_iva-framework.md` SV-TAX-FR-179/181 — the
framework routes the return here; this file owns the window it lands
in); the DTE emission, sealing and NCE/NDE structure rules (the
e-invoicing stack: SV-EINV-FR-015/033 related-document windows,
§3.11 SV-EINV-FR-159..164 correction accounting — FR-160 cross-month
reversal, FR-161 window-expired NCE/NDE routing, FR-164 origin-rate
reuse — all cited by id, never restated); the F-07 declaration surfaces
that consume the adjustment outputs (negative-value gate and
three-prior-period window — `fiscal-reporting/01_f07-declaration.md`
SV-FREP-FR-031/033, by id); the ISR asset-accounting kin of the
repair-vs-improvement boundary (accounting wave surfaces); and the CT
declaration-modification procedure itself (the F-07 modificatoria flow
is fiscal-reporting's; this file only flags the obligation — OQ-2).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). **SOQ-54 vintage note (rides every 01_/02_ LB in this
file):** the consolidation's last reform stamp is D.L. 71-2015 —
post-2015 reforms unverified; corpus-internal signals negative (DTE
stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual silent);
re-verify at implementation. The Art. 62 medicines block carries stamp
(10) = D.L. 183-2006 per the consolidation's reform index (dated
behavior note in §5); Art. 63 carries stamps (7)/(11); Arts. 71-72
carry stamp (11). **Reglamento = 02_ survivors only** (D.E. 83-1992
consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass repeal
= D.E. 117-2001 stamp (3) — ruling R30(a)); survivor articles = 1-10,
16-30, 50-51 (+ 52 vigencia); this file cites Rgto. Art. 26 — a
survivor. **CT re-anchor (binding reading):** the Art. 62 closing
inciso anchors the adjustment documents on "los comprobantes de crédito
fiscal y las notas emitidas de que trata el artículo 100 de esta ley" —
Art. 100 is DEROGADO (D.L. 230/00 belt); the operative notas regime is
Código Tributario Art. 110 (the Art. 63 preamble itself already cites
"EL ARTÍCULO 110 DEL CÓDIGO TRIBUTARIO" in the post-reform print). The
CT document-system co-anchor is owned by the e-invoicing file
(`e-invoicing/01_document-types.md` LB-007,
`sv/sources/05_Codigo_Tributario.pdf` Arts. 107-115, EVID-060 — cited
by id here, never restated). **V1 citation rule:** every LB row below cites 01_ or 02_
with the EVID id and the txt page anchor (`=== PAGE n ===` markers of
`01_Ley_IVA.pdf.txt` / `02_Reglamento_IVA.pdf.txt`, verified this
task); the SOQ-54 watch rides all of them. The framework file's LB-028
(Art. 62-1-a pointer) RESOLVES to this file's LB-001 — the pointer is
retired here, the window owned.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA (D.L. 296-1992, texto consolidado), Art. 62, numeral 1) letra a) inciso 1º — "1) Restar el impuesto correspondiente a las siguientes deducciones, en cuanto hubiere lugar, y no se hubiere efectuado al emitirse los comprobantes de crédito fiscal: a) Monto del valor de los bienes, envases o depósitos devueltos o de otras operaciones anuladas o rescindidas en el período tributario, pero dentro de los tres meses de la entrega de los bienes o de la percepción del pago de los servicios, siempre que se pruebe que ese valor ha sido considerado para el cálculo del débito fiscal en el mismo período o en otro anterior, lo que deberá comprobar el contribuyente." | 1) Subtract the tax corresponding to the following deductions, insofar as applicable and not already effected at the emission of the CCFs: a) the amount of the value of goods, containers or deposits returned, or of other annulled or rescinded operations, in the tax period but WITHIN THREE MONTHS of the delivery of the goods or of the perception of the services payment — provided it is proven that the value was considered in the débito fiscal calculation of the same or an earlier period, which the contribuyente must demonstrate | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-a inciso 1º p.27 (EVID-319; verified 01_ txt lines 950-957, PAGE 27) |
| LB-002 | Ley IVA, Art. 62, numeral 1) letra a) — medicinas: ventana de DOS AÑOS + extensión de la caducidad + deber de registro — "EN LAS TRANSFERENCIAS DE MEDICAMENTOS Y ESPECIALIDADES FARMACÉUTICAS PERECEDEROS PARA USO Y CONSUMO HUMANO, EL REFERIDO PLAZO PODRÁ SER AMPLIADO HASTA DOS AÑOS; EN TAL CASO, SE ENTENDERÁ EXTENDIDO EL PLAZO DE LA CADUCIDAD DE LAS FACULTADES DE FISCALIZACIÓN Y LIQUIDACIÓN OFICIOSA POR DOS AÑOS, CONTANDO DESDE EL PERÍODO TRIBUTARIO AL QUE PERTENECEN LAS OPERACIONES ORIGINALES AJUSTADAS; ASIMISMO, LOS CONTRIBUYENTES DEBEN LLEVAR UN REGISTRO DETALLADO DE LOS PRODUCTOS VENDIDOS Y DE LAS DEVOLUCIONES DE LOS MISMOS. EL REGISTRO DEBERÁ INCLUIR LA SIGUIENTE INFORMACIÓN :" [spacing before colon sic] | In transfers of perishable MEDICINES AND PHARMACEUTICAL SPECIALTIES for human use and consumption, the referenced term may be extended UP TO TWO YEARS; in such case, the term of the CADUCIDAD of the fiscalization and liquidación-oficiosa faculties is understood EXTENDED BY TWO YEARS, counted FROM THE TAX PERIOD TO WHICH THE ORIGINAL ADJUSTED OPERATIONS BELONG; likewise the contribuyentes must carry a DETAILED REGISTRY of the products sold and of their returns — the registry to include the following information (stamp (10) = D.L. 183-2006) | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-a medicinas pp.27-28 (EVID-319; verified 01_ txt lines 958-974, PAGE 27-28) |
| LB-003 | Ley IVA, Art. 62, numeral 1) letra a) — el REGISTRO DE LOTE de siete campos, VERBATIM — "• NÚMERO DE LOTE DE PRODUCCIÓN O NÚMERO DEL DOCUMENTO QUE AMPARA LA IMPORTACIÓN, EN SU CASO. • NOMBRE Y PRESENTACIÓN DEL PRODUCTO. • FECHA DE VENCIMIENTO. • FECHA DE ENTRADA Y SALIDA DE INVENTARIOS. • NÚMERO DEL COMPROBANTE DE CRÉDITO FISCAL EMITIDO POR LA TRANSFERENCIA, EL CUAL DEBERÁ CONTENER, ADEMÁS DE LOS REQUISITOS PROPIOS DE ESE TIPO DE DOCUMENTO, LA DESCRIPCIÓN APROPIADA DEL PRODUCTO, DEBIENDO SEÑALAR EL NÚMERO DEL LOTE Y FECHA DE VENCIMIENTO. • FECHA DEL COMPROBANTE DE CRÉDITO FISCAL, Y • NOMBRE DEL CÓDIGO DEL CLIENTE." | The seven mandatory registry fields, verbatim: production lot number or import-document number, as corresponds; product name and presentation; expiration date; inventory entry and exit dates; the number of the Comprobante de Crédito Fiscal issued for the transfer — which must contain, besides that document type's own requirements, the appropriate product description, stating the LOT NUMBER AND EXPIRATION DATE; the CCF date; and the client code name | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-a registro p.28 (EVID-319; verified 01_ txt lines 975-986, PAGE 28) |
| LB-004 | Ley IVA, Art. 62, numeral 1) letra a) — NC con lote; respaldo contable (cuenta de inventario de producto vencido); actas de destrucción sanitarias — "AL MOMENTO DE ACEPTARSE LA DEVOLUCIÓN, EN LA NOTA DE CRÉDITO DEBE RELACIONARSE, ADEMÁS DEL NÚMERO DEL COMPROBANTE DE CRÉDITO FISCAL CON EL CUAL SE RELACIONA LA MISMA, EL NÚMERO DEL LOTE DEL MEDICAMENTO O ESPECIALIDAD FARMACÉUTICA  DEVUELTA Y UNA DESCRIPCIÓN APROPIADA DEL PRODUCTO OBJETO DE LA DEVOLUCIÓN. LO ANTERIOR ES SIN PERJUICIO DE QUE TALES OPERACIONES TAMBIÉN DEBEN RESPALDARSE MEDIANTE LAS APLICACIONES CONTABLES, AFECTANDO EN LOS LIBROS CONTABLES LEGALES Y AUXILIARES, LA CUENTA DE INVENTARIO DE PRODUCTO VENCIDO Y SU CORRESPONDIENTE ANOTACIÓN EN EL REGISTRO DE CONTROL RESPECTIVO. TALES DEVOLUCIONES TAMBIÉN DEBERÁN RESPALDARSE CON LAS RESPECTIVAS ACTAS QUE DEBEN LEVANTARSE Y SUSCRIBIRSE POR LAS AUTORIDADES SANITARIAS RESPECTIVAS AL MOMENTO DE LA DESTRUCCIÓN DEL PRODUCTO VENCIDO, LAS QUE DEBERÁN CONTENER EN FORMA DESCRIPTIVA EL DETALLE DE CADA UNO DE LOS MEDICAMENTOS O ESPECIALIDADES FARMACÉUTICAS DESTRUIDAS Y SU CORRESPONDIENTE LOTE DE PRODUCCIÓN.(10)" [double space sic] | Upon acceptance of the return, the CREDIT NOTE must state, besides the CCF number it relates to, the LOT NUMBER of the returned medicine or pharmaceutical specialty and an appropriate description of the product object of the return — without prejudice to the accounting backing: affecting in the legal and auxiliary books the EXPIRED-PRODUCT INVENTORY ACCOUNT and its corresponding annotation in the respective control register; such returns must also be backed by the respective ACTS levanted and SUBSCRIBED BY THE RESPECTIVE SANITARY AUTHORITIES at the moment of the DESTRUCTION of the expired product, containing in descriptive form the detail of each destroyed medicine or pharmaceutical specialty and its corresponding PRODUCTION LOT (stamp (10) = D.L. 183-2006) | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-a respaldo p.28 (EVID-319; verified 01_ txt lines 987-1003, PAGE 28) |
| LB-005 | Ley IVA, Art. 62, numeral 1) letra b) — "b) El monto de las rebajas de precio, bonificaciones y descuentos u otras deducciones normales del comercio, no condicionadas y de carácter general, bajo la misma comprobación requerida en el numeral anterior. A este efecto, el contribuyente deberá demostrar la forma y condiciones en que ellas se han concedido, los comprobantes de crédito fiscal con que se relacionan y el período tributario a que corresponde la operación respectiva." | The amount of price reductions, bonuses and discounts or other deductions NORMAL OF COMMERCE, unconditional and of general character, under the same proof required in the prior numeral — for which effect the contribuyente must demonstrate the form and conditions in which they were granted, the CCFs they relate to, and the tax period the respective operation corresponds to | `sv/sources/01_Ley_IVA.pdf` | Art. 62-1-b p.29 (EVID-319; verified 01_ txt lines 1011-1016, PAGE 29) |
| LB-006 | Ley IVA, Art. 62, numeral 2) letras a)-c) + inciso final (vía documental) — "2) Sumar el impuesto correspondiente a las siguientes adiciones, si no se hubiere efectuado con anterioridad:  a) Incrementos de precio, reajustes, gastos, intereses, incluso por mora en el pago; b) Diferencias por traslación indebida de un débito fiscal inferior al que correspondía; y c) Cualquier suma trasladada como débito fiscal en  cuanto  exceda a la que legalmente corresponda, a menos que se compruebe que ella hubiere sido restituida al respectivo adquirente de bienes o usuario de los servicios. Los ajustes referidos deberán efectuarse de acuerdo a los comprobantes de crédito fiscal y las notas emitidas de que trata el artículo 100 de esta ley." [double spaces sic] | 2) ADD the tax of the following additions, if not effected before: a) price increments, readjustments, expenses, interests — including for mora in payment; b) differences from an UNDULY LOW transfer of a débito fiscal inferior to what corresponded; and c) any sum transferred as débito fiscal insofar as it EXCEEDS what legally corresponds — unless it is proven that it was RESTITUTED to the respective acquirer of goods or user of the services. The referenced adjustments must be effected per the CCFs and the emitted notes treated in ARTICLE 100 OF THIS LAW [derogated — CT Art. 110 re-anchor] | `sv/sources/01_Ley_IVA.pdf` | Art. 62-2 + inciso final p.29 (EVID-319; verified 01_ txt lines 1017-1026, PAGE 29) |
| LB-007 | Ley IVA, Art. 63, encabezado + letras a)-c) — "Artículo 63.-PARA CALCULAR EL CRÉDITO FISCAL DEL PERÍODO TRIBUTARIO, SE DEBE RESTAR EL IMPUESTO CORRESPONDIENTE A LAS SIGUIENTES PARTIDAS, EN CUANTO HAYA LUGAR, SIEMPRE QUE NO SE HUBIEREN EFECTUADO CON ANTERIORIDAD Y CONSTEN EN COMPROBANTES DE CRÉDITO FISCAL O EN LAS NOTAS REFERIDAS EN EL ARTÍCULO 110 DEL CÓDIGO TRIBUTARIO:(11) a) Las cantidades trasladadas por adquisiciones de bienes o prestaciones de servicios anuladas o rescindidas, siempre que las mismas se hubieren considerado en el cálculo del crédito fiscal correspondiente al período tributario o en otro anterior; b) El monto de las cantidades trasladadas correspondiente a reducción de precios, descuentos, bonificaciones u otras deducciones, que impliquen una disminución del precio de compra de los bienes o de la remuneración de los servicios, siempre que anteriormente se hubieran computado en el crédito fiscal; y c) Cualquier suma que hubiere sido trasladada en exceso, en la parte en que dicha suma exceda el monto que debió trasladarse." | To calculate the crédito fiscal of the tax period, the tax of the following items must be SUBTRACTED, insofar as applicable, PROVIDED they were not effected before and are evidenced in CCFs or in the notes referred to in CT ARTICLE 110: a) amounts transferred for acquisitions of goods or service prestations annulled or rescinded — provided they were considered in the crédito fiscal calculation of the tax period or an earlier one; b) the amount of transferred sums corresponding to price reductions, discounts, bonuses or other deductions implying a decrease in the purchase price or service remuneration — provided they were previously computed in the crédito fiscal; and c) any sum transferred IN EXCESS, in the part by which it exceeds what should have been transferred | `sv/sources/01_Ley_IVA.pdf` | Art. 63 encabezado + a)-c) p.29 (EVID-320; verified 01_ txt lines 1028-1040, PAGE 29) |
| LB-008 | Ley IVA, Art. 63, incisos: agregación tardía (3 períodos); régimen de las notas de crédito; modificación obligatoria de declaraciones — "Por otra parte, se deberá agregar al crédito fiscal el aumento del impuesto que proceda de acuerdo con los comprobantes de crédito fiscal y notas de débito de que trata el artículo antes mencionado, recibidas y registradas con posterioridad. RESPECTO DE LOS COMPROBANTES DE CRÉDITO FISCAL Y NOTAS DE DÉBITO QUE SE RECIBAN CON RETRASO, EL IMPUESTO QUE DE ELLAS RESULTE PODRÁ UTILIZARSE PARA AUMENTAR EL CRÉDITO FISCAL, HASTA LOS TRES PERÍODOS TRIBUTARIOS QUE SIGUEN AL DE LA EMISIÓN DE DICHOS DOCUMENTOS. EN CUANTO A LAS NOTAS DE CRÉDITO, EL IMPUESTO CONTENIDO EN ELLAS DEBERÁ UTILIZARSE PARA REDUCIR EL CRÉDITO FISCAL, EN EL PERÍODO TRIBUTARIO EN QUE FUERON EMITIDAS, SALVO QUE EL CONTRIBUYENTE DEMUESTRE HABERLAS RECIBIDO CON RETRASO, EN CUYO CASO SE REGISTRARÁN Y DECLARARÁN HASTA LOS TRES PERÍODOS TRIBUTARIOS QUE SIGUEN AL DE LA EMISIÓN DE DICHOS DOCUMENTOS. (11) TRANSCURRIDO DICHO PLAZO SIN EFECTUAR EL AJUSTE AL CRÉDITO FISCAL, EL CONTRIBUYENTE ESTARÁ OBLIGADO A MODIFICAR LAS DECLARACIONES DEL PERÍODO TRIBUTARIO DE LA EMISIÓN DE LOS REFERIDOS DOCUMENTOS, APLICANDO TODO EL CRÉDITO FISCAL A QUE SE TENDRÍA DERECHO O A DISMINUIRLO EN LA CUANTÍA CORRESPONDIENTE. (7) (11)" | Furthermore, the increase of tax proceeding from the CCFs and notas de débito treated in the aforementioned article, RECEIVED AND REGISTERED AFTERWARDS, must be added to the crédito fiscal. Regarding CCFs and notas de débito RECEIVED LATE, the tax resulting from them may be used to increase the crédito fiscal, UP TO THE THREE TAX PERIODS FOLLOWING THAT OF THE EMISSION of those documents. As for NOTAS DE CRÉDITO, the tax contained in them must be used to REDUCE the crédito fiscal IN THE TAX PERIOD THEY WERE EMITTED — UNLESS the contribuyente demonstrates having received them late, in which case they are registered and declared up to the three tax periods following emission; that term elapsed without the crédito adjustment effected, the contribuyente is OBLIGED TO MODIFY THE DECLARATIONS OF THE TAX PERIOD OF THE EMISSION of the referenced documents, applying all the crédito fiscal to which there would be right or diminishing it in the corresponding amount | `sv/sources/01_Ley_IVA.pdf` | Art. 63 incisos finales pp.29-30 (EVID-320; verified 01_ txt lines 1041-1062, PAGE 29-30) |
| LB-009 | Ley IVA, Art. 64 — "Artículo 64.- Por regla general, el impuesto que ha de ser pagado por el contribuyente será la diferencia que resulte de deducir del débito fiscal causado en el período tributario, el crédito fiscal trasladado al contribuyente al adquirir bienes o al utilizar los servicios y, en su caso, el impuesto pagado en la importación o internación definitiva de los bienes, en el mismo período tributario." | By general rule, the tax to be paid by the contribuyente is the difference resulting from deducting from the débito fiscal caused in the tax period the crédito fiscal transferred to the contribuyente on acquiring goods or using services and, where applicable, the tax paid on the import or definitive internación of the goods — in the SAME tax period | `sv/sources/01_Ley_IVA.pdf` | Art. 64 p.30 (EVID-321; verified 01_ txt lines 1066-1069, PAGE 30) |
| LB-010 | Ley IVA, Arts. 71-72 (+ Art. 73 estado) — "Artículo 71.- EN CUANTO NO FORMAN PARTE DEL GIRO O ACTIVIDAD DEL CONTRIBUYENTE Y CARECEN DE HABITUALIDAD, NO CONSTITUYEN HECHO GENERADOR DEL IMPUESTO LAS TRANSFERENCIAS DE DOMINIO DE BIENES DEL ACTIVO FIJO O DE CAPITAL DE LOS CONTRIBUYENTES, A MENOS QUE ESA TRANSFERENCIA SE EFECTÚE ANTES DE LOS CUATRO AÑOS DE ESTAR LOS BIENES AFECTADOS A DICHO ACTIVO. (11)" — "Artículo 72.-No obstante lo dispuesto en el artículo anterior, el crédito fiscal trasladado en los comprobantes de crédito fiscal por la adquisición de bienes muebles corporales de capital destinados al activo fijo, es deducible del débito  fiscal originado por las operaciones gravadas realizadas en el mismo período, o en los posteriores si restare un remanente de aquél, hasta su total deducción. INCISO SEGUNDO SUPRIMIDO (1) TAMBIÉN PROCEDE LA DEDUCCIÓN DEL CRÉDITO FISCAL PROVENIENTE DE LAS ADQUISICIONES DE BIENES MUEBLES CORPORALES O DE LA UTILIZACIÓN DE SERVICIOS DESTINADOS A LA REPARACIÓN O A SUBSANAR LOS DETERIOROS QUE CORRESPONDEN AL USO O GOCE NORMAL DE LOS BIENES INMUEBLES DEL ACTIVO FIJO, ASÍ COMO LOS DESTINADOS A LA REMODELACIÓN DE BIENES INMUEBLES SEAN O NO PROPIEDAD DEL CONTRIBUYENTE, PARA COLOCARLO EN CONDICIONES DE USO EN EL GIRO DEL NEGOCIO, SIN AUMENTAR SU VALOR O  VIDA ÚTIL.(11)" — "Artículo 73.- DEROGADO (4)" [double spaces and "72.-No" sic] | Art. 71: as they do not form part of the contribuyente's giro or activity and LACK HABITUALIDAD, transfers of dominion of ACTIVO FIJO OR CAPITAL goods are NOT a hecho generador — UNLESS the transfer is effected BEFORE FOUR YEARS of the goods being AFFECTED to that asset. Art. 72: notwithstanding the prior article, the crédito fiscal transferred in CCFs for the acquisition of capital bienes muebles corporales destined to the activo fijo is deductible from the débito fiscal originated by the gravada operations of the SAME period — or the later ones should a remanente of it remain, until its total deduction [second inciso SUPPRESSED, stamp (1)]; the credit ALSO proceeds for acquisitions of bienes muebles corporales or use of services destined to REPAIR or to remedy the deterioration corresponding to the NORMAL USE OR ENJOYMENT of the activo-fijo INMUEBLES, as well as those destined to the REMODELING of inmuebles whether or not owned by the contribuyente, to place it in conditions of use in the business giro, WITHOUT INCREASING ITS VALUE OR USEFUL LIFE. Art. 73 (certificates for remanente credit): DEROGADO (stamp 4) | `sv/sources/01_Ley_IVA.pdf` | Arts. 71-73 p.37 (EVID-326; verified 01_ txt lines 1360-1378, PAGE 37) |
| LB-011 | Reglamento IVA (D.E. 83-1992 consolidado), Art. 26 — "Artículo 26.- Si la transferencia de bienes del activo fijo o de capital constituyera hecho  generador del impuesto, deberá emitirse Factura o Comprobante de Crédito Fiscal,  según corresponda; caso contrario, de conformidad al artículo 71 de la ley, deberá  emitirse cualquier otro tipo de documento." | If the transfer of activo fijo or capital goods constitutes a hecho generador of the tax, a Factura or Comprobante de Crédito Fiscal must be emitted, as corresponds; otherwise, per Art. 71 of the law, ANY OTHER TYPE OF DOCUMENT must be emitted | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 26 p.7 (EVID-336; verified 02_ txt lines 258-261, PAGE 7) |
| LB-012 | Ley IVA, Art. 7 literales g), h) e i) — reorganización, liquidaciones y establecimientos — "g) Transferencias de bienes  muebles corporales propias del giro con ocasión de la modificación, ampliación, transformación, fusión u otras  formas de reorganización de sociedades; h) ADJUDICACIONES Y TRANSFERENCIAS  DE BIENES MUEBLES CORPORALES, EFECTUADAS COMO CONSECUENCIA DE DISOLUCIONES Y LIQUIDACIONES O DISMINUCIONES DE CAPITAL DE SOCIEDADES U OTRAS PERSONAS JURÍDICAS, SOCIEDADES NULAS, IRREGULARES O DE HECHO Y ENTES COLECTIVOS CON O SIN PERSONALIDAD JURÍDICA. EN LOS CASOS INDICADOS EN ESTE LITERAL NO SERÁ OBJETO A GRAVAMEN LA TRANSFERENCIA DE  BIENES MUEBLES CORPORALES CUANDO EL ADJUDICATARIO  FUERE EL MISMO SOCIO O ACCIONISTA QUE LO APORTÓ, Y DICHO BIEN NO SE ENCONTRABA GRAVADO CON EL IMPUESTO QUE TRATA ESTA LEY; (11) i) Transferencias de establecimientos  o empresas mercantiles, respecto únicamente de los bienes muebles corporales del activo realizable incluídos en la operación;" [double spaces and "incluídos" sic] | g) transfers of own-giro bienes muebles corporales on occasion of the modification, ampliación, transformation, fusión or OTHER forms of reorganization of societies; h) ADJUDICATIONS AND TRANSFERS of bienes muebles corporales effected as a consequence of dissolutions and liquidations or capital reductions of societies or other legal persons — null, irregular or de facto societies and collective entities with or without legal personality included; in the cases of this literal the transfer of bienes muebles corporales is NOT subject to gravamen WHEN THE ADJUDICATARY IS THE SAME SOCIO OR ACCIONISTA WHO CONTRIBUTED (aportó) IT AND SAID GOOD WAS NOT CHARGED WITH THE TAX THIS LAW TREATS; i) transfers of establishments or mercantile businesses, SOLELY as to the bienes muebles corporales of the ACTIVO REALIZABLE included in the operation | `sv/sources/01_Ley_IVA.pdf` | Art. 7 g)-i) p.4 (EVID-306; verified 01_ txt lines 124-136, PAGE 4) |

Dead text — never implementable as current law (recorded as notes, not
FRs, per wave constraints): Art. 73 (certificados por remanente de
crédito fiscal) is DEROGADO (stamp 4) — the remanente regime lives in
Arts. 67-70 and T5's file, never in certificates; Art. 62's closing
"artículo 100 de esta ley" is a stale anchor (D.L. 230/00 belt — the
operative document set is CT Arts. 107-115, nota semantics at CT 110,
overlaid by the DTE stack); Art. 72's "INCISO SEGUNDO SUPRIMIDO (1)"
records a suppressed inciso, not content. The SOQ-54 vintage watch (§2
preamble) applies to every row above.

## 3. Functional Requirements

### 3.1 Ajustes del débito fiscal — Art. 62 (incl. the medicines lot regime)

- **SV-TAX-FR-284:** The system shall compute the period's débito
  fiscal as the Art. 55 per-operation débito sum produced by the
  base/rate engine (`09_iva-base-rate.md` SV-TAX-FR-241 — by id, never
  recomputed here) MINUS the Art. 62-1 deductions PLUS the Art. 62-2
  additions, and shall effect every such adjustment EXCLUSIVELY through
  the statutory document path — CCFs and the emitted notas (Art. 100 as
  printed, re-anchored to CT Art. 110; the NCE/NDE emission, structure
  and related-document windows are the e-invoicing stack's:
  SV-EINV-FR-015/033, §3.11 SV-EINV-FR-160/161 — by id) — never through
  a free-form journal entry that bypasses the correction documents; each
  adjustment line carries its adjustment kind for the determination
  aggregation and the F-07 feeds.
  (LB-006; LB-008; EVID-319/320; cross-ref SV-TAX-FR-241,
  SV-EINV-FR-015/033/160/161)
- **SV-TAX-FR-285:** The system shall admit the Art. 62-1-a débito
  deduction — the tax of the value of returned goods, *envases o
  depósitos* (goods, containers or deposits), or of other annulled or
  rescinded operations — ONLY when: (a) the return/annulment/rescission
  occurs in the current tax period AND within THREE MONTHS of the
  entrega de los bienes (goods delivery) or of the percepción del pago
  de los servicios (perception of the services payment — the anchor
  being whichever applies to the operation kind); (b) it is proven that
  the value was already considered in the débito calculation of the same
  or an earlier period (prior-computation proof, the burden on the
  contribuyente — a traceable link to the origin CCF whose débito
  included it); and (c) the deduction was not already effected at
  document emission; the window anchors on the ORIGINAL operation dates
  snapshotted on the record (D15: corrections use original-period
  parameters), and the framework's Art. 9 exchange/return routing
  (`07_iva-framework.md` SV-TAX-FR-181, LB-028 pointer resolving to
  LB-001 here) lands in this gate — a return outside the window cannot
  carry the deduction and blocks as a débito-adjustment candidate.
  (LB-001; EVID-319; cross-ref SV-TAX-FR-181)
- **SV-TAX-FR-286:** For transfers of *medicamentos y especialidades
  farmacéuticas perecederos para uso y consumo humano* (perishable
  medicines and pharmaceutical specialties for human use and
  consumption), the system shall extend the FR-285 return window from
  three months to UP TO TWO YEARS (per-product/per-lot applicability of
  the perishable-medicine class), and shall — whenever the extension is
  used — record the statutory consequence: the caducidad term of the
  fiscalización and liquidación-oficiosa faculties extends TWO YEARS
  counted from the tax period to which the ORIGINAL adjusted operations
  belong (a per-period extension flag derived from the earliest adjusted
  original period, exposed to the compliance/prescription monitors);
  behavior note: the block enters with stamp (10) = D.L. 183-2006 —
  operations before that reform's vigencia apply the plain three-month
  window (dated regime, §5).
  (LB-002; EVID-319)
- **SV-TAX-FR-287:** For the medicines class the system shall carry the
  MANDATORY detailed registry of products sold and returns, with the SEVEN
  statutory fields — none dropped, none renamed: 1) *número de lote de
  producción o número del documento que ampara la importación, en su
  caso* (production lot or import-document number); 2) *nombre y
  presentación del producto*; 3) *fecha de vencimiento* (expiration
  date); 4) *fecha de entrada y salida de inventarios* (inventory entry
  and exit dates); 5) *número del comprobante de crédito fiscal emitido
  por la transferencia*; 6) *fecha del comprobante de crédito fiscal*
  (CCF date); 7) *nombre del código del cliente* (client code) — the
  registry entry created at sale and completed at return, and its
  absence or incompleteness blocking the FR-286 extended-window
  deduction.
  (LB-003; EVID-319)
- **SV-TAX-FR-288:** The system shall enforce the medicines DOCUMENT
  requirements: the CCF emitted for the transfer of a perishable
  medicine shall contain, besides that document type's own requirements
  (the DTE layer's CCFE structure — e-invoicing by id), the appropriate
  product description STATING THE LOT NUMBER AND THE EXPIRATION DATE;
  and the credit note accepting the return shall state, besides the CCF
  number it relates to, the LOT NUMBER of the returned medicine and an
  appropriate description of the product object of the return (the NCE
  emission surface is e-invoicing's — this file owns the
  content-validation gate the NCE must pass before the deduction
  releases).
  (LB-003; LB-004; EVID-319; cross-ref SV-EINV-FR-015)
- **SV-TAX-FR-289:** The system shall back every accepted
  expired-medicine return with BOTH statutory evidences: (a) the
  ACCOUNTING backing — the applications affecting the legal and
  auxiliary books, charging the *cuenta de inventario de producto
  vencido* (expired-product inventory account) and its corresponding
  annotation in the respective control register (the inventory-control
  register surface of CT Arts. 142/142-A consumed by id from T4's
  FR-254); and (b) the DESTRUCTION ACTS — records that they were
  levanted and subscribed by the respective SANITARY AUTHORITIES at the
  moment of destruction of the expired product, containing in
  descriptive form the detail of EACH destroyed medicine or
  pharmaceutical specialty and its corresponding production lot; the
  deduction release is conditioned on the act's presence, authority and
  per-lot detail.
  (LB-004; EVID-319; cross-ref SV-TAX-FR-254)
- **SV-TAX-FR-290:** The system shall admit the Art. 62-1-b débito
  deduction — the tax amount of price reductions (*rebajas de precio*),
  bonuses, discounts or other deductions NORMAL OF COMMERCE,
  unconditional and of general character — under the same
  prior-computation proof as FR-285 (already considered in the débito of
  the same or an earlier period, not already effected at emission), PLUS
  the specific demonstration: the form and conditions in which they were
  granted, the CCFs they relate to, and the tax period of the respective
  operation — all three recorded on the deduction's backing; this is the
  deduction-side mirror of the Art. 52 base exclusion
  (`09_iva-base-rate.md` SV-TAX-FR-237 — by id: discounts already
  excluded from the base at emission deduct nothing here; only
  post-emission reductions on previously taxed values flow through this
  gate).
  (LB-005; EVID-319; cross-ref SV-TAX-FR-237)
- **SV-TAX-FR-291:** The system shall ADD to the period's débito fiscal
  the Art. 62-2 additions, if not effected with anteriority: a) price
  increments, *reajustes*, expenses and interests — INCLUDING mora
  interest in payment (the deferred-price increments kin of the Art.
  51-a base additions, by id from T3); b) the differences from an
  unduly-low transfer — where a débito fiscal INFERIOR to what
  corresponded was transferred, the shortfall is added; and c) any sum
  transferred as débito insofar as it exceeds what legally corresponds —
  UNLESS restitution to the respective acquirer of goods or user of the
  services is proven (a recorded restitution proof suppresses the
  addition); each addition rides the FR-284 document path (CCF/notas),
  never a bare journal line.
  (LB-006; EVID-319; cross-ref SV-TAX-FR-284)

### 3.2 Ajustes del crédito fiscal and the Art. 64 determination (Arts. 63-64)

- **SV-TAX-FR-292:** The system shall SUBTRACT from the period's crédito
  fiscal (T4's eligible-credit output, `10_iva-credit-deductibility.md`
  SV-TAX-FR-246/251 — by id) the Art. 63 a)-c) items, insofar as
  applicable, ONLY when: they were not effected with anteriority (no
  double subtraction), they are evidenced in CCFs or in the notas of CT
  Art. 110, and — for a) annulled or rescinded acquisitions and b)
  price-reduction/discount/bonus deductions implying a decrease of the
  purchase price or service remuneration — the amounts were previously
  computed in the crédito fiscal of the tax period or an earlier one;
  item c) — any sum transferred in excess, in the part exceeding what
  should have been transferred — subtracts without the
  prior-computation condition but with the same documentary evidence;
  the subtraction rides the credit-note reception path with its
  CT-110-nota or CCF reference recorded.
  (LB-007; EVID-320; cross-ref SV-TAX-FR-246/251)
- **SV-TAX-FR-293:** The system shall ADD to the crédito fiscal the tax
  of CCFs and notas de débito RECEIVED AND REGISTERED WITH POSTERIORITY
  (late documents), usable to increase the crédito UP TO THE THREE TAX
  PERIODS FOLLOWING THAT OF THE EMISSION of those documents — the
  eligibility window computed against the DOCUMENT's emission period
  (snapshotted on the document record; D15: original-period parameters
  govern), so a vendor CCF/ND emitted in period M may increase the
  crédito of M+1, M+2 or M+3 but never M+4; the same three-period
  ceiling is the legal root the F-07 purchase window consumes
  (`fiscal-reporting/01_f07-declaration.md` SV-FREP-FR-033 — by id, the
  current + 3 prior periods upload rule).
  (LB-008; EVID-320; cross-ref SV-FREP-FR-033)
- **SV-TAX-FR-294:** The system shall apply the notas de crédito rule:
  the tax contained in a received NC reduces the crédito fiscal in the
  tax period of ITS EMISSION — UNLESS the contribuyente demonstrates
  having received it late (late-receipt flag with proof), in which case
  it registers and declares up to the THREE tax periods following the
  emission; and once that term is elapsed without the crédito adjustment
  effected, the system shall raise the OBLIGATION to MODIFY THE
  DECLARATIONS of the emission period of the referenced documents —
  applying all the crédito fiscal to which there would be right, or
  diminishing it in the corresponding amount — as a flagged
  declaration-modification requirement on the period (the modification
  flow itself is the F-07 modificatoria surface, fiscal-reporting's;
  under the D9 freeze-at-filing corollary the filed period is never
  silently mutated — the flag drives the modificatoria filing, OQ-2).
  (LB-008; EVID-320; cross-ref SV-FREP-FR-031/033, D9 corollary)
- **SV-TAX-FR-295:** The system shall determine the period's tax
  payable per Art. 64 as the difference resulting from deducting from
  the débito fiscal caused in the tax period (post-FR-284..291
  adjustments) the crédito fiscal transferred to the contribuyente on
  acquiring goods or using services (post-FR-292..294 adjustments) and,
  where applicable, the tax paid on the import or definitive
  internación of goods — all in the SAME tax period; a crédito in
  excess of the débito produces NO payable and flows to the remanente
  carryforward engine (`11_iva-pro-rata-remanente.md` SV-TAX-FR-278 —
  by id), and the post-adjustment crédito is likewise the input of the
  Art. 66 pro-rata run (SV-TAX-FR-275 — by id).
  (LB-009; EVID-321; cross-ref SV-TAX-FR-275/278)

### 3.3 Bienes del activo fijo o de capital — the 4-year rule, fijo credits and document routing (Arts. 71-72; Rgto. Art. 26)

- **SV-TAX-FR-296:** The system shall treat transfers of dominion of
  *bienes del activo fijo o de capital* (fixed or capital-asset goods)
  as NOT a hecho generador of IVA — they do not form part of the
  contribuyente's giro or activity and lack habitualidad — UNLESS the
  transfer is effected BEFORE four years of the goods being affected to
  that asset: the gate computes against the ALTA DATE (the
  afectación-to-activo-fijo date recorded on the asset, the D15
  anchor — parameters resolve as-of that date and the four-year clock
  never re-anchors on corrections); a transfer at any moment before the
  four-year mark is a TAXED transfer (débito per FR-241's engine on the
  resolved base), from the mark onward it is not a hecho generador.
  (LB-010; EVID-326)
- **SV-TAX-FR-297:** The system shall make the crédito fiscal
  transferred in CCFs for the acquisition of capital *bienes muebles
  corporales* destined to the activo fijo deductible — notwithstanding
  FR-296's non-giro character — against the débito fiscal originated by
  the gravada operations of the SAME period, or of the LATER ones
  should a remanente of that credit remain, until its TOTAL deduction
  (the same-or-future window riding T5's remanente machinery,
  SV-TAX-FR-278 by id; eligibility gates and formal requirements are
  T4's, SV-TAX-FR-251/254 by id).
  (LB-010; EVID-326; cross-ref SV-TAX-FR-251/254/278)
- **SV-TAX-FR-298:** The system shall ALSO admit the crédito fiscal of
  acquisitions of *bienes muebles corporales* or the use of services
  destined to: a) the REPAIR of the *inmuebles del activo fijo*
  (fixed-asset real property) or to remedy (*subsanar*) the
  deterioration corresponding to their NORMAL USE OR ENJOYMENT; and b)
  the REMODELING of inmuebles — WHETHER OR NOT property of the
  contribuyente — destined to place them in conditions of use in the
  business giro WITHOUT INCREASING THEIR VALUE OR USEFUL LIFE — the
  value/life-increase test being a recorded classification on the
  expense (any remodeling that increases value or useful life fails the
  gate and lands in T4's Art. 65 gate-3 block,
  SV-TAX-FR-251 construction/reconstruction/remodeling exclusion —
  mirror by id).
  (LB-010; EVID-326; cross-ref SV-TAX-FR-251)
- **SV-TAX-FR-299:** The system shall route the DOCUMENT of an
  activo-fijo/capital-asset transfer per Reglamento Art. 26: if the
  transfer constitutes a hecho generador (FR-296's before-four-years
  case), a FACTURA or COMPROBANTE DE CRÉDITO FISCAL must be emitted, as
  corresponds (the FE/CCFE choice per the e-invoicing type rules, by
  id); in the contrary case (the not-a-hecho-generador case), ANY OTHER
  TYPE OF DOCUMENT must be emitted — the routing flag derived from the
  same four-year computation, never a manual override; and Art. 73's
  certificate regime is recorded as DEROGADO — no certificate surface
  may be configured from it.
  (LB-010; LB-011; EVID-326/336)

### 3.4 Reorganization transfers — aportes, fusion moves, liquidation adjudications and establecimiento scope (Art. 7 f)-i) determination gates)

- **SV-TAX-FR-300:** The system shall tax as TRANSFERS — generating
  débito per the base/rate engine (SV-TAX-FR-241 by id) under the
  framework's operation classification (SV-TAX-FR-179's Art. 7 catalog
  seed — by id): a) the APORTES of own-giro *bienes muebles
  corporales* to societies and other legal persons (Art. 7-f); and b)
  the own-giro transfers effected on occasion of the modification,
  ampliación, transformation, fusión or other forms of REORGANIZATION of
  societies (Art. 7-g) — each carried with its reorg kind on the
  operation record so the débito, the document emission and the F-07
  feeds classify correctly; no reorganization form bypasses the transfer
  classifier (FR-178's substance-over-form, by id).
  (LB-012; EVID-306; cross-ref SV-TAX-FR-178/179/241)
- **SV-TAX-FR-301:** The system shall apply the Art. 7-h carve-out to
  adjudications and transfers effected as a consequence of disolutions
  and liquidations or DISMINUCIONES DE CAPITAL of societies and the
  other listed entities: NO gravamen — not a hecho generador — ONLY
  when BOTH recorded conditions hold: (a) the adjudicatario is the SAME
  socio or accionista who APORTÓ the good (an identity trace from the
  asset's aportación record), AND (b) the good was NOT charged
  ("gravado") with this tax at its aportación (the not-charged status on
  the acquisition/aportación record); failing either condition, the
  adjudication is a TAXED transfer under FR-300's engine; the two
  conditions are computed facts with their evidence links, never a bare
  checkbox.
  (LB-012; EVID-306)
- **SV-TAX-FR-302:** The system shall scope a transfer of
  *establecimientos o empresas mercantiles* (establishments or
  mercantile businesses, Art. 7-i) as taxable SOLELY as to the
  *bienes muebles corporales del activo realizable* included in the
  operation — the operation's lines partitioned by asset class
  (realizable vs fijo vs other), only the realizable-goods portion
  entering the transfer base and débito (per the Art. 48-d
  establecimiento base rule, T3 by id); the fixed-asset goods inside
  the same operation route instead through the FR-296 four-year gate on
  their own alta dates.
  (LB-012; EVID-306; cross-ref SV-TAX-FR-296)

## 4. Data Model

No CSV sidecars ship for this file (wave constraint: NO CSV sidecars).
The only dated legal parameter regimes are: the medicines two-year
window/caducidad extension (stamp (10) = D.L. 183-2006 — a behavior
note, not a table); the three-month/three-period statutory windows
(fixed statutory constants, not dated rows — SOQ-54 watch rides them);
and the four-year activo-fijo gate (fixed statutory constant anchored on
the per-asset alta date — D15 snapshot). Layer semantics: this file
introduces Odoo-side adjustment/validation/classification data only
(wave default `odoo`; see §5). **Interface entity for the wave's index
(Task 7):** the adjustment-kind enum + window-check fields + asset
transfer gate below.

**Débito-adjustment carriers (Art. 62):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (SV extension) | l10n_sv_iva_adjustment_kind | select | devolucion_anulacion_rescision · rebaja_bonificacion_descuento · incremento_reajuste_interes · traslacion_inferior · traslacion_exceso (débito side); credito_anulacion_rescision · credito_reduccion_precio · credito_traslado_exceso · credito_tardio_ccf_nd · nc_credito_reduction (crédito side) | FR-284, FR-290, FR-291, FR-292, FR-293, FR-294 |
| account.move (NC débito, SV extension) | l10n_sv_iva_return_anchor_date, l10n_sv_iva_return_anchor_kind | date / select | entrega_bienes · percepcion_pago_servicios; the ORIGINAL operation date snapshot (D15) | FR-285 |
| account.move (NC débito) | l10n_sv_iva_prior_debito_proof_move_id | m2o account.move | origin CCF whose débito already considered the value (prior-computation proof) | FR-285, FR-290 |
| account.move (NC débito) | l10n_sv_iva_return_window_state | select (computed) | within_3m · within_2y_medicines · expired; medicines flag from product class perecedero uso humano | FR-285, FR-286 |
| account.move (additions ND) | l10n_sv_iva_restitution_proof_ref | char / attachment | proof of restitution to the adquirente/usuario suppressing the 2-c excess addition | FR-291 |

**Medicines lot registry (Art. 62 stamp 10):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.lot.registry.line (new) | lote_produccion_import_doc, nombre_y_presentacion, fecha_vencimiento | char / char / date | statutory fields 1-3 (production or import-document lot; name and presentation; expiration) | FR-287 |
| l10n_sv.iva.lot.registry.line | fecha_entrada_inventario, fecha_salida_inventario | date ×2 | statutory field 4 (inventory entry and exit dates) | FR-287 |
| l10n_sv.iva.lot.registry.line | ccf_move_id (number + fecha), cliente_codigo | m2o account.move / char | statutory fields 5-7 (CCF emitted by the transfer, its date; client code) | FR-287 |
| account.move (CCF medicines) | l10n_sv_iva_lot_registry_line_id | m2o | links the CCF to its registry line; the CCF print/validation requires lote + fecha de vencimiento stated | FR-288 |
| account.move (NCE medicines) | l10n_sv_iva_nc_lot_ref, l10n_sv_iva_nc_origin_ccf_id | m2o lot registry line / m2o account.move | NC states the related CCF number + the returned lot + appropriate description | FR-288 |
| l10n_sv.iva.destruction.act (new) | act_date, sanitary_authority, descriptive_detail, lot_refs, scrap/picking link | date / char / text / m2m / refs | acts levanted and subscribed by the sanitary authorities at destruction; per-medicament detail + production lot | FR-289 |
| account.move (vencido return) | l10n_sv_iva_vencido_inventory_account_id | m2o account.account | the cuenta de inventario de producto vencido charge + control-register annotation | FR-289 |
| res.company (SV extension) | l10n_sv_iva_caducidad_extension_periods | one2many (period, extended_until) | per-period 2-year caducidad extension from the earliest adjusted original period | FR-286 |

**Crédito-adjustment carriers and determination (Arts. 63-64):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (vendor CCF/ND, SV extension) | l10n_sv_iva_emission_period | char (YYYY-MM, snapshot) | the document's emission period — the 3-following-periods clock anchor | FR-293, FR-294 |
| account.move (vendor NC) | l10n_sv_iva_nc_late_receipt_proven | boolean + proof ref | late receipt demonstrated ⇒ register/declare up to 3 following periods | FR-294 |
| account.move (vendor CCF/ND/NC) | l10n_sv_iva_credit_window_state | select (computed) | current · within_3_following · beyond ⇒ declaration_modification_required | FR-293, FR-294 |
| l10n_sv.iva.period.determination (new) | period, debito_ajustado, credito_ajustado, import_iva_credit, payable | char / monetary ×4 | Art. 64 row: débito (post-62) − crédito (post-63) − import IVA, same period; negative ⇒ remanente hand-off | FR-284, FR-295 |

**Fixed assets (Arts. 71-72; Rgto. Art. 26):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset (SV extension) | l10n_sv_iva_alta_date | date | afectación al activo fijo date — the 4-year clock anchor (D15 snapshot; legacy-asset sourcing → OQ-4) | FR-296 |
| account.asset | l10n_sv_iva_transfer_taxable | boolean (computed) | true before 4 years from alta; false from the mark onward | FR-296, FR-299 |
| account.move (asset sale) | l10n_sv_iva_asset_doc_routing | select (computed) | factura_o_ccf · otro_documento (Rgto. Art. 26) | FR-299 |
| account.move.line (purchase/expense) | l10n_sv_iva_fijo_credit_class | select | adquisicion_capital_fijo · reparacion_deterioro_normal · remodelacion_condiciones_uso; remodel value/life-increase test recorded (blocked ⇒ T4 gate-3) | FR-297, FR-298 |

**Reorganization transfers (Art. 7 f)-i)):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (reorg, SV extension) | l10n_sv_iva_reorg_kind | select | aporte_giro_7f · reorganizacion_7g (modificacion · ampliacion · transformacion · fusion · otra) · liquidacion_adjudicacion_7h · disminucion_capital_7h · establecimiento_7i | FR-300, FR-301, FR-302 |
| account.move (7-h adjudication) | l10n_sv_iva_adjudicatario_is_aportador, l10n_sv_iva_bien_not_charged | boolean (computed/recorded) ×2 | BOTH required for the no-gravamen carve-out (aportación trace + not-charged status) | FR-301 |
| account.move (7-i establecimiento) | l10n_sv_iva_realizable_scope_lines | one2many filter | only the activo realizable bienes muebles corporales enter the transfer base | FR-302 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = adjustment/validation/classification
computation logic living in the LGPL client. No SaaS rows are introduced
in this file: nothing here touches DTE generation/transformation (the
NCE/NDE emission, structure and related-document windows are the
e-invoicing stack's — SV-EINV-FR-015/033, §3.11 SV-EINV-FR-159..164, by
id; the shared-row routing decision of SV-EINV-FR-161 consumes this
file's window states as its input); this file supplies the statutory
window computations, the lot registry and the adjustment aggregation the
client and the DTE layer both consume. Model names are stable across
Odoo 17/18/19/20 (`account.move`, `account.move.line`, `account.asset`,
`res.company`, `account.account`; `account.asset` is core in 17/18 — the
l10n_sv extension rides it; the new `l10n_sv.iva.*` models follow T5's
naming). D15 doctrine (binding): the three-month, two-year and
three-period windows anchor on the ORIGINAL operation/emission dates
snapshotted on the records; corrections use original-period parameters.
D9 corollary (interplay by id): the filed period is never silently
mutated — FR-294's declaration-modification obligation drives a
modificatoria filing, not an in-place edit (e-invoicing §3.11 FR-159/160
lock family, by id).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-284 | odoo | account.move.line + l10n_sv.iva.period.determination | adjustment_kind + adjusted totals | Aggregates T3's FR-241 débito; document path = CCF/notas (Art. 100 → CT 110 re-anchor); EINV NCE/NDE by id |
| FR-285 | odoo | account.move (NC débito) | return_anchor_date/kind + prior_debito_proof + window_state | 3-month window from entrega/percepción; prior-computation proof; FR-181's return routing lands here |
| FR-286 | odoo | account.move + res.company | window_state within_2y_medicines + caducidad_extension_periods | Stamp (10) D.L. 183-2006 dated note: pre-reform operations keep 3m; extension flag per earliest adjusted original period |
| FR-287 | odoo | l10n_sv.iva.lot.registry.line | the 7 statutory fields | MANDATORY registry — none dropped; incompleteness blocks the 2y deduction |
| FR-288 | odoo | account.move (CCF/NCE medicines) | lot_registry_line_id + nc_lot_ref/origin_ccf | CCF prints lote + vencimiento; NC relates CCF + lote + description; NCE emission surface = EINV (by id) |
| FR-289 | odoo | l10n_sv.iva.destruction.act + account.move | act fields + vencido_inventory_account | Sanitary-authority acts with per-medicament detail + lot; cuenta de inventario de producto vencido + control register (CT 142/142-A via T4 FR-254) |
| FR-290 | odoo | account.move (NC débito) | prior_debito_proof + forma-y-condiciones backing | Rebajas/bonificaciones/descuentos normales, no condicionados, carácter general; mirror of T3 FR-237 (Art. 52) |
| FR-291 | odoo | account.move.line (additions) | adjustment_kind + restitution_proof_ref | 2-a/b/c additions incl. under-transferred differences; excess suppressed only by restitution proof |
| FR-292 | odoo | account.move.line (crédito subtractions) | adjustment_kind crédito side | a)-c) with prior-computation + CT-110-nota/CCF evidence; adjusts T4 FR-246/251 output |
| FR-293 | odoo | account.move (vendor CCF/ND) | emission_period + credit_window_state | +crédito up to 3 following periods from EMISSION; F-07 window root (SV-FREP-FR-033 by id) |
| FR-294 | odoo | account.move (vendor NC) | nc_late_receipt_proven + credit_window_state beyond | NC reduces in emission period; late ⇒ 3 periods; beyond ⇒ declaration_modification_required flag (D9 corollary; modificatoria = FREP surface, OQ-2) |
| FR-295 | odoo | l10n_sv.iva.period.determination | Art. 64 payable row | débito − crédito − import IVA, same period; excess ⇒ T5 remanente (FR-278) and pro-rata input (FR-275), by id |
| FR-296 | odoo | account.asset | alta_date + transfer_taxable (computed) | 4-year gate from afectación date (D15); <4y taxed transfer, ≥4y not a hecho generador; legacy alta sourcing → OQ-4 |
| FR-297 | odoo | account.move.line (purchase) | fijo_credit_class adquisicion_capital_fijo | Same-or-later periods until total deduction; rides T5 remanente (FR-278) and T4 gates (FR-251/254) |
| FR-298 | odoo | account.move.line (expense) | fijo_credit_class reparacion/remodelacion + value/life test | Repairs + normal use/goce deterioration + remodel-in-conditions WITHOUT value/life increase; increase ⇒ T4 gate-3 block (FR-251) |
| FR-299 | odoo | account.move (asset sale) | asset_doc_routing | Taxable ⇒ Factura o CCF; else cualquier otro documento (Rgto. 26); Art. 73 DEROGADO — no certificate surface |
| FR-300 | odoo | account.move (reorg) | reorg_kind aporte/reorganizacion | 7-f/7-g taxed transfers; débito per T3 FR-241; classification from 07 FR-178/179 |
| FR-301 | odoo | account.move (7-h adjudication) | adjudicatario_is_aportador + bien_not_charged | BOTH conditions for no gravamen; identity trace + not-charged status recorded |
| FR-302 | odoo | account.move (7-i establecimiento) | realizable_scope_lines | Only activo realizable portion taxed; fixed-asset lines route to FR-296 gate |

Version-regime notes (D12/D15): FR-286 carries the D.L. 183-2006
medicines-block cutover (stamp (10); the reform's vigencia date is not
in this corpus — the pre/post behavior switch is configured from the
reform instrument at implementation; SOQ-54 re-verify). FR-285/293/294
carry the D15 snapshot doctrine: window clocks computed against the
original operation/emission dates, never the correction date. FR-294
carries the D9 corollary interplay: the emission-period declaration
modification is a flagged filing obligation — the e-invoicing §3.11
locks (SV-EINV-FR-159/160) and the F-07 modificatoria flow (FREP, by
id) are the enforcement surfaces. The SOQ-54 consolidation watch rides
every LB (§2 preamble) — re-verify against a current official
consolidation at implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a buyer returning goods four months after the
  entrega date (no medicines class, no new-contract intent), when the
  NC deduction candidate is evaluated, then the deduction is REJECTED
  (outside the three-month window) and no Art. 62-1-a subtraction enters
  the period's débito (FR-285).
- **AC-002:** Given a vencido perishable-medicine return at month 20
  from the entrega, with a complete seven-field lot registry line, an NC
  referencing the origin CCF number AND the returned lot, the
  cuenta de inventario de producto vencido charge recorded and a
  sanitary-authority destruction act with per-medicament detail and
  production lot attached, when the deduction is evaluated, then it
  PASSES under the two-year window and the period's caducidad-extension
  flag is set two years from the ORIGINAL operation's period
  (FR-286, FR-287, FR-288, FR-289).
- **AC-003:** Given the same medicine return attempted at month 25,
  when the NC deduction candidate is evaluated, then it is REJECTED
  (beyond the two-year window) (FR-286).
- **AC-004:** Given a post-emission rebaja de precio of a previously
  taxed sale, with the forma-y-condiciones demonstration, the related
  CCF and the operation's tax period recorded, when the deduction is
  evaluated, then the Art. 62-1-b subtraction enters the débito — while
  a discount already excluded from the base at emission (Art. 52, T3
  FR-237) deducts NOTHING here (FR-290).
- **AC-005:** Given a vendor that transferred a débito inferior to what
  corresponded, when the addition runs, then the shortfall is ADDED per
  Art. 62-2-b; given a sum transferred in excess WITH recorded proof of
  restitution to the acquirer, then the Art. 62-2-c addition is
  SUPPRESSED (FR-291).
- **AC-006:** Given a vendor NC for an annulled acquisition whose tax
  was previously computed in the crédito fiscal, when the NC is
  registered, then the Art. 63-a subtraction reduces the period's
  crédito — and a subtraction already effected with anteriority never
  subtracts twice (FR-292).
- **AC-007:** Given a vendor ND emitted in period M and received late,
  registered in M+2, when the crédito adjustment runs, then the tax is
  ADDED to M+2's crédito (within the three following periods M+1..M+3);
  given the same ND registered in M+4, then the in-period addition is
  refused (FR-293).
- **AC-008:** Given a vendor NC emitted in period M and first adjusted
  only in M+5 (no timely adjustment within M+1..M+3), when the window
  check runs, then the record is flagged
  `declaration_modification_required` against period M — the filed M
  figures are never silently mutated (D9 corollary; the modificatoria
  filing is the F-07 surface, by id) (FR-294).
- **AC-009:** Given a period with adjusted débito $1,130.00, adjusted
  crédito $500.00 and import IVA $100.00, when the determination row
  computes, then the payable is $530.00 (Art. 64); given instead
  débito $300.00 and crédito $500.00, then NO payable results and the
  $200.00 excess flows to the remanente carryforward (T5 by id)
  (FR-295).
- **AC-010:** Given a delivery vehicle with alta date 2023-06-15 sold
  on 2026-08-01 (year 3), when the asset sale is classified, then the
  transfer is a TAXED hecho generador documented with Factura or CCF;
  given the same vehicle sold on 2028-01-10 (past four years from
  alta), then it is NOT a hecho generador and the document routes to
  cualquier otro tipo de documento (FR-296, FR-299).
- **AC-011:** Given a remodeling service of a leased premises that
  increases the property's value and useful life, when the credit
  candidate is evaluated, then the crédito is BLOCKED (T4 gate-3
  mirror); given a repair subsanating the normal-use deterioration of an
  owned activo-fijo inmueble, then the crédito PROCEEDS (FR-298).
- **AC-012:** Given an aporte of own-giro machinery to a sociedad and a
  fusión-triggered transfer of giro goods, when classified, then BOTH
  are taxed transfers with débito on the resolved base; given a
  liquidation adjudication of a good to the SAME socio who aportó it
  where the good was NOT IVA-charged, then NO gravamen applies — and
  given either condition failing (different adjudicatario, or a
  previously charged good), then the adjudication is taxed (FR-300,
  FR-301).
- **AC-013:** Given the transfer of an establecimiento whose operation
  includes realizable inventory and fixed-asset equipment, when the
  transfer computes, then ONLY the activo realizable bienes muebles
  corporales enter the base and débito, the equipment routing separately
  through the four-year gate on its own alta date (FR-302, FR-296).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 62-64, 71-72, 7 g)-i) + Rgto. Art. 26 at implementation — in particular whether the medicines lot regime and the 3-period crédito windows have been touched by post-2015 instruments; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | Declaration-modification procedural config (D9-kin): Art. 63's overflow duty ("EL CONTRIBUYENTE ESTARÁ OBLIGADO A MODIFICAR LAS DECLARACIONES DEL PERÍODO TRIBUTARIO DE LA EMISIÓN") requires amending an ALREADY-FILED period — the modificatoria mechanics (F-07 modificatoria flow, complementary-sworn-declaration practice, DGII form routing, interest/surcharge treatment on the resulting difference) are outside this corpus and are fiscal-reporting surfaces. FR-294 ships the obligation flag only; wire the actual modification workflow against the FREP modificatoria surfaces (01-file family) at implementation, honoring the D9 freeze-at-filing corollary (no silent in-place mutation of filed periods; e-invoicing §3.11 lock family by id). | no | Takumi S9 + Odoo implementation | open |
| OQ-3 | Window-anchor divergence (Ley vs DTE): the Art. 62 statutory window runs from the ENTREGA DE LOS BIENES or PERCEPCIÓN DEL PAGO, while the NCE/NDE related-document window of the DTE stack (SV-EINV-FR-015/033) runs from the RELATED DOCUMENT (3 months from the origin document). Where delivery materially postdates the origin CCF (or precedes it), the two clocks diverge; the working reading is that the DTE window gates document ADMISSIBILITY and the Ley window gates the DEDUCTION — both must pass — but confirm against DGII criteria before final wiring (a return admissible as NCE yet outside the Ley window deducts nothing, and vice versa needs a document path). | no | Takumi S9 | open |
| OQ-4 | Alta-date sourcing for legacy assets: the FR-296 four-year gate anchors on the afectación al activo fijo date; assets acquired before implementation (historical import per D18) may lack a recorded alta date. Configure the anchor sourcing (acquisition invoice date · depreciation-start date · go-live snapshot with declared alta) as onboarding config — never a hardcoded guess; the D15 snapshot discipline applies once recorded (the clock never re-anchors). | no | Takumi + Odoo implementation | open |
