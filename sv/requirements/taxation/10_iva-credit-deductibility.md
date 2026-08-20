# SV — Taxation — IVA crédito fiscal: deductibility gates, Art. 65-A non-deductibles and document routing (Ley IVA Arts. 57-61, 65, 65-A, 70; Rgto. Arts. 19-23; CT Arts. 112, 141-142-A, 161-162)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the *crédito fiscal*
(tax credit) side of El Salvador's IVA (D.L. 296-1992): the Art. 57
*traslación* root — the amount shifted to acquirers equals the débito and
constitutes their crédito, stated in the CCF *en forma separada del
precio* (separately from the price — the legal root of the FE-inclusive vs
CCF-net document contract); the importers' credit (IVA paid at
importación/internación, proven per Rgto. Art. 19 by the póliza/DUCA +
recibo pair); the Art. 58 retiros/autoconsumo NO-credit rule with its
FACTURA-only documentation and the CCF/nota-de-débito ban (Rgto. Art. 20
*como consumidor final*); the Art. 60 excluidos-purchase cost rule and
Art. 61 *naturaleza jurídica* (the credit is a structural element of the
tax, never a claim against the fisco for undue or excess payment); the
Art. 65 deductibility machinery — the four destination gates (activo
realizable; activo fijo keeping individuality and not incorporated into
inmuebles; giro services EXCLUDING construction/edification and
reconstruction/remodeling/modification of inmuebles in any modality;
gastos generales), the indispensable + gravada-generation requirement
(débito-generating operations, 0% gravadas, ISR-Art.-6 donations,
diplomatic/consular/international-organization sales), the else-branch
FACTURA rule (buyers must not request a CCF; suppliers must emit
factura), the formal requirements (original CCF with the crédito stated
separately or documentary import proof; the CT Art. 141 libro de compras;
the CT Arts. 142/142-A inventory register for goods), the
adquisiciones scope (local purchases + imports + internaciones, with the
Rgto. Art. 21 gastos-generales definition and Rgto. Art. 22
duly-registered meaning), and the retention-credit release gates
(CT-Art.-162 retentions credited to the agent in the same period as the
comprobante de retención emission if declared and entered integrally in
that same period and registered separately; CT-Art.-161 amounts credited
via mandamiento de ingreso — Rgto. Art. 23); and the FULL Art. 65-A
non-deductible catalog a)-n) (food outside giro with the
supplier-FACTURA obligation; food imports; non-strictly-indispensable
vehicles and their running costs; hotels without business-use proof; air
tickets save verifiable-employee business travel; clothing/jewelry/
calzado outside giro; personal/family-use destinations; alcohol and
cigarettes; over-rate traslados; general non-indispensables;
construction/edification inputs; the ≥58-SMM payment-form gates in the
printed l)/m)/n) structure) plus the 50% mixed-use-vehicle rule, the
unauthorized-numbering bar, the fake/irregular-document list 1)-5) with
its criminal-action reservation, the giro identity (the registration
recorded in the tarjeta de contribuyente), and the blocked-value route to
ISR cost (Art. 65 final inciso mirrored by Art. 70 and consumed by the
ISR deduction file).

It does **not** cover: the rate and base imponible (Arts. 47-54 —
`09_iva-base-rate.md` SV-TAX-FR-225/240 own them; this file consumes the
dated rate rows for the over-rate gate by id); the exempt-operation
catalogs and their codes (`08_iva-exemptions.md` SV-TAX-FR-206/224 — the
gravada-generation gate consumes exemption classification by id, never
restating); the débito/crédito adjustment machinery (Arts. 62-63
three-month returns and late-document rules) and the Art. 64 débito−
crédito determination arithmetic, owned by the determination file of this
wave; the Art. 66 pro-rata mechanics (the pro-rata file of this wave —
this file's blocked-credit states feed it by id); the retention MATRIX
itself — who retains, at what percent, on which operations
(CT Arts. 161/162/162-A/162-B percentages, floors and designation rules
are `fiscal-reporting/04_f07-annexes-retentions-events.md`'s surface;
this file states only the credit-release gate and cites the CT articles
as co-LB); the retiro engine and its consumidor-final invoice emission
routing (`07_iva-framework.md` SV-TAX-FR-183..186 own the retiro facts
and the Rgto. Art. 20 document routing — this file supplies the
credit-side lock); the excluidos no-credit lock (`07_iva-framework.md`
SV-TAX-FR-205 owns it; this file supplies the Art. 60 cost consequence);
DTE emission mechanics (the e-invoicing stack — this file cites
SV-EINV-FR-019/024 by id as the FE-inclusive/CCF-net roots of the
separate-from-price rule); the F-07 casilla-128 post-entero re-entry and
the F-930 view (`fiscal-reporting/03_f07-annexes-purchases.md`
SV-FREP-FR-091 and `fiscal-reporting/04_f07-annexes-retentions-events.md`
SV-FREP-FR-111 — cited by id); the SMM tariff rows and sector mapping
(`payroll/02_minimum-wage.md` SV-PAY-FR-022 — the 58-SMM gate reads its
dated sidecar rows through that config, never encoding SMM values); and
the ISR-side deductibility of blocked values
(`taxation/02_isr-deductions.md` SV-TAX-FR-045 excludes IVA from ISR
deductions subject to Ley IVA Art. 70 — cited by id as the mirror).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). **SOQ-54 vintage note (rides every 01_/02_ LB in this
file):** the consolidation's last reform stamp is D.L. 71-2015 —
post-2015 reforms unverified; corpus-internal signals negative (DTE
stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual silent);
re-verify at implementation. **Reglamento = 02_ survivors only** (D.E.
83-1992 consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass
repeal = D.E. 117-2001 stamp (3)); survivor articles = 1-10, 16-30,
50-51 (+ 52 vigencia); this file cites Rgto. Arts. 19, 20, 21, 22, 23 —
all survivors. **CT re-anchors (binding on several rows):** ~60 Ley
articles were derogated by D.L. 230/00 (registration, documents,
sanctions, administration — now Código Tributario); Art. 65 as printed
already anchors its registers on CT Arts. 141, 142, 142-A, 161, 162 and
112 (the printed text is post-230/00 and self-re-anchored); Rgto.
Art. 22 carries a stale "artículo 107 de la ley" ref (derogated — now CT
141) and Rgto. Art. 23 a stale "artículo 34 de la ley" ref (derogated —
now CT 161; see EVID-332), both cited with note. **V1 citation rule:**
every LB row below cites 01_ or 02_ (and the CT co-LB row cites 05_) with
the EVID id and the txt page anchor (`=== PAGE n ===` markers of
`01_Ley_IVA.pdf.txt` / `02_Reglamento_IVA.pdf.txt` /
`05_Codigo_Tributario.pdf.txt`, verified this task); the SOQ-54 watch
rides all of them.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA, Art. 57 | "Los contribuyentes deberán trasladar a los adquirentes de los bienes y a los prestatarios de los servicios, una cantidad equivalente al monto del débito fiscal generado en cada operación gravada. Dicha cantidad deberá constar en el Comprobante de Crédito Fiscal a que se refiere el Art. 97 de esta ley, en forma separada del precio o remuneración de la operación y deberá pagarse conjuntamente a los vendedores o a quienes transfieren el dominio de los bienes o a los prestadores de los servicios, según quien haya emitido tal documento. Para los efectos del presente impuesto la suma trasladada a los adquirentes o prestatarios se denomina "Crédito Fiscal". Respecto de los importadores, constituye crédito fiscal el impuesto pagado en la importación o internación." | Contribuyentes must shift to acquirers of goods and users of services an amount EQUAL to the débito fiscal generated in each gravada operation; that amount must appear in the Comprobante de Crédito Fiscal (CCF; the Art. 97 anchor is repealed — CT/DTE regime) SEPARATELY from the price or remuneration, paid jointly with it; the shifted sum is named "Crédito Fiscal" (the acquirer's credit); for importers, the tax paid at importación/internación constitutes crédito fiscal | `sv/sources/01_Ley_IVA.pdf` | Art. 57 p.26 (EVID-317; verified 01_ txt lines 911-920, PAGE 26) |
| LB-002 | Ley IVA, Art. 58 | "No generan crédito fiscal los retiros de bienes del giro de la empresa, ni el autoconsumo de servicios, a que se refieren los artículos 11 y 16 de esta ley." "LAS OPERACIONES MENCIONADAS EN EL INCISO ANTERIOR, SEAN GRAVADAS, EXENTAS O NO SUJETAS, DEBERÁN DOCUMENTARSE CON FACTURA O DOCUMENTO EQUIVALENTE AUTORIZADO POR LA ADMINISTRACIÓN TRIBUTARIA; EN NINGÚN CASO SE UTILIZARÁ COMPROBANTE DE CRÉDITO FISCAL O NOTA DE DÉBITO. (11)" | Retiros of giro goods and autoconsumo of services (Arts. 11/16 facts) generate NO crédito fiscal; those operations — gravadas, exentas or no sujetas alike — must be documented with FACTURA or an authorized equivalent document; a CCF or nota de débito is used IN NO CASE | `sv/sources/01_Ley_IVA.pdf` | Art. 58 pp.26-27 (EVID-317; verified 01_ txt lines 921-923 + 931-934, PAGE 26-27) |
| LB-003 | Ley IVA, Arts. 60-61 | Art. 60: "Las cantidades que a título del impuesto se trasladen a los no contribuyentes indicados en el Artículo 28 de esta ley, no les generan crédito fiscal y constituirán costo de los respectivos bienes y servicios, de acuerdo con lo dispuesto en los artículos 31 y 65 de la misma." Art. 61: "El crédito fiscal constituye un elemento de la estructura tributaria y de la naturaleza del impuesto. Se rige exclusivamente por las normas de esta ley y no tiene el carácter de crédito en contra del fisco por pago indebido o en exceso de este impuesto." | Amounts shifted to the Art.-28 excluidos generate no crédito fiscal for them and constitute COST of the respective goods and services (Arts. 31/65 crossref); the crédito fiscal is a structural element of the tax, governed exclusively by this law's norms — it is NOT a credit against the fisco for undue or excess payment of this tax | `sv/sources/01_Ley_IVA.pdf` | Arts. 60-61 p.27 (EVID-318; verified 01_ txt lines 938-944, PAGE 27) |
| LB-004 | Ley IVA, Art. 65 encabezado + numerales 1-4 — FULL CATALOG | "ÚNICAMENTE SERÁ DEDUCIBLE EL CRÉDITO FISCAL TRASLADADO EN LOS COMPROBANTES DE CRÉDITO FISCAL EN LA FORMA INDICADA EN EL ARTÍCULO 64 DE ESTA LEY, EN LOS CASOS SIGUIENTES: (7) (8)" — "1.- ADQUISICIONES DE BIENES MUEBLES CORPORALES DESTINADOS AL ACTIVO REALIZABLE;(8)" — "2.- ADQUISICIONES DE BIENES MUEBLES CORPORALES DESTINADOS AL ACTIVO FIJO, CUANDO EN ÉSTE CONSERVEN SU INDIVIDUALIDAD Y NO SE INCORPOREN A UN BIEN INMUEBLE; (8)" — "3. DESEMBOLSOS EFECTUADOS PARA LA UTILIZACIÓN DE SERVICIOS EN EL GIRO DEL NEGOCIO, SIEMPRE QUE NO SE DESTINEN A LA CONSTRUCCIÓN O EDIFICACIÓN DE BIENES INMUEBLES, ASÍ COMO LA RECONSTRUCCIÓN, REMODELACIÓN O MODIFICACIÓN, YA SEA TOTAL O PARCIAL DE BIENES INMUEBLES SEAN PROPIEDAD O NO DEL CONTRIBUYENTE; INDISTINTAMENTE QUE DICHOS SERVICIOS SE CONTRATEN POR PRECIO ALZADO, POR ADMINISTRACIÓN DE OBRA O CUALQUIER OTRA MODALIDAD; (8) (11)" — "4.- GASTOS GENERALES DESTINADOS EXCLUSIVAMENTE A LOS FINES DE LA REALIZACIÓN DEL OBJETO, GIRO O ACTIVIDAD DEL CONTRIBUYENTE, TALES COMO FLETES O ACARREOS, ENERGÍA ELÉCTRICA, TELÉFONO O AGUA.(8)" | ONLY crédito fiscal shifted in CCFs is deductible (per Art. 64's form), in these cases: 1) acquisitions of bienes muebles corporales destined to the ACTIVO REALIZABLE; 2) activo fijo goods WHEN they keep their individuality in it and are not incorporated into an inmueble; 3) disbursements for services used in the giro, PROVIDED they are not destined to construction or edification of inmuebles, nor reconstruction, remodeling or modification — total or partial — of inmuebles whether or not owned by the contribuyente, regardless of contract modality (lump-sum, obra administration, any other); 4) gastos generales destined exclusively to the object/giro/activity — e.g. freight or cartage, electric energy, telephone or water | `sv/sources/01_Ley_IVA.pdf` | Art. 65 nums. 1-4 p.30 (EVID-322; verified 01_ txt lines 1071-1085, PAGE 30) |
| LB-005 | Ley IVA, Art. 65, inciso (indispensable + gravada generation) | "LAS OPERACIONES MENCIONADAS EN LOS NUMERALES ANTERIORES DEBERÁN SER INDISPENSABLES PARA EL OBJETO, GIRO O ACTIVIDAD DEL CONTRIBUYENTE Y PARA LA GENERACIÓN DE OPERACIONES GRAVADAS CON ESTE IMPUESTO Y QUE POR LO TANTO, GENEREN DÉBITO FISCAL, DE OPERACIONES GRAVADAS CON TASA CERO POR CIENTO, DE DONACIONES DE BIENES O SERVICIOS EFECTUADAS A LAS INSTITUCIONES A QUE SE REFIERE EL ARTÍCULO 6 DE LA LEY DE IMPUESTO SOBRE LA RENTA Y DE OPERACIONES DE VENTA REALIZADAS A FAVOR DE MISIONES DIPLOMÁTICAS, CONSULARES, ORGANISMOS INTERNACIONALES Y A SUS MIEMBROS ACREDITADOS ANTE EL GOBIERNO DE LA REPÚBLICA DE EL SALVADOR; CASO CONTRARIO NO SERÁ DEDUCIBLE EL CRÉDITO FISCAL. (8) (13)" | The numeral-1-4 operations must be INDISPENSABLE for the object/giro/activity AND for the GENERATION of operations gravada with this tax — i.e. generating débito fiscal, or 0%-rated gravadas operations, or donations of goods/services to the ISR-Art.-6 institutions, or sales in favor of diplomatic missions, consulates, international organizations and their accredited members (stamp 13); otherwise the crédito fiscal is NOT deductible | `sv/sources/01_Ley_IVA.pdf` | Art. 65 p.31 (EVID-322; verified 01_ txt lines 1093-1101, PAGE 31) |
| LB-006 | Ley IVA, Art. 65, inciso (else-branch FACTURA) | "LAS ADQUISICIONES DE BIENES O DE SERVICIOS QUE NO SE ENMARQUEN Y NO CUMPLAN LO DISPUESTO EN LOS INCISOS PRECEDENTES DEBERÁN SER DOCUMENTADAS POR MEDIO DE FACTURA. PARA ESE EFECTO, LOS CONTRIBUYENTES ADQUIRENTES DE BIENES O DE SERVICIOS, NO DEBERÁN SOLICITAR LA EMISIÓN O LA ENTREGA DE COMPROBANTE DE CRÉDITO FISCAL SINO QUE DE FACTURA Y LOS PROVEEDORES DE BIENES O DE SERVICIOS ESTARÁN OBLIGADOS A EMITIRLA Y ENTREGARLA. (8)" | Acquisitions of goods or services not framed in / not complying with the preceding incisos must be documented by FACTURA; for that effect the acquiring contribuyentes must NOT request emission or delivery of a CCF but of a factura, and the suppliers are OBLIGED to emit and deliver the factura | `sv/sources/01_Ley_IVA.pdf` | Art. 65 p.31 (EVID-322; verified 01_ txt lines 1102-1107, PAGE 31) |
| LB-007 | Ley IVA, Art. 65, incisos (formal requirements) | "PARA EFECTOS DE LA DEDUCIBILIDAD A QUE SE REFIERE ESTE ARTÍCULO SE REQUERIRÁ EN TODO CASO, QUE LA OPERACIÓN QUE ORIGINA EL CRÉDITO FISCAL ESTÉ DOCUMENTADA CON EL COMPROBANTE DE CRÉDITO FISCAL ORIGINAL Y QUE FIGURE LA CANTIDAD TRASLADADA COMO CRÉDITO FISCAL EN FORMA SEPARADA DEL PRECIO DE LOS BIENES O REMUNERACIÓN DE LOS SERVICIOS, O SE COMPRUEBE DOCUMENTALMENTE EL MONTO DEL IMPUESTO PAGADO EN LA IMPORTACIÓN O INTERNACIÓN DE LOS BIENES O DE LOS SERVICIOS. ADEMÁS, TODO ELLO DEBE ESTAR DEBIDAMENTE REGISTRADO EN EL LIBRO DE COMPRAS QUE ESTABLECE EL ARTÍCULO 141 DEL CÓDIGO TRIBUTARIO Y EN LA CONTABILIDAD FORMAL O EN LIBROS ESPECIALES, EN ESTE ÚLTIMO CASO, SEGÚN SE TRATE DE CONTRIBUYENTES OBLIGADOS O NO A LLEVAR CONTABILIDAD FORMAL. (8)" — "CUANDO SE TRATE DE BIENES MUEBLES CORPORALES, TAMBIÉN CONSTITUIRÁ REQUISITO PARA LA DEDUCCIÓN QUE TRATA ESTE ARTÍCULO, QUE LA COMPRA DE DICHOS BIENES ESTÉ DEBIDAMENTE ASENTADA EN EL REGISTRO DE CONTROL DE INVENTARIOS A QUE ALUDEN LOS ARTÍCULOS 142 Y 142-A DEL CÓDIGO TRIBUTARIO, HACIENDO REFERENCIA AL DOCUMENTO LEGAL CORRESPONDIENTE Y BAJO LOS REQUISITOS ESTABLECIDOS POR LOS CITADOS ARTÍCULOS. (11)" | Deductibility requires in every case that the credit-originating operation be documented with the ORIGINAL CCF showing the crédito amount SEPARATELY from the price/remuneration, OR documentary proof of the import/internación tax paid; all duly registered in the CT-Art.-141 libro de compras and in formal accounting or special books (per whether the contribuyente is obliged to formal accounting); for bienes muebles corporales the purchase must ALSO be recorded in the CT-Arts.-142/142-A inventory-control register, referencing the legal document | `sv/sources/01_Ley_IVA.pdf` | Art. 65 p.31 (EVID-322; verified 01_ txt lines 1108-1122, PAGE 31) |
| LB-008 | Ley IVA, Art. 65, incisos (retention credits) | "LOS IMPUESTOS RETENIDOS POR LOS AGENTES DE RETENCIÓN, DE CONFORMIDAD A LO ESTABLECIDO EN EL ARTÍCULO 162 DEL CÓDIGO TRIBUTARIO, CONSTITUIRÁN CRÉDITO FISCAL PARA EL AGENTE, EN EL MISMO PERÍODO QUE CORRESPONDA A LA FECHA DE EMISIÓN DEL COMPROBANTE DE RETENCIÓN A QUE SE REFIERE EL ARTÍCULO 112 DEL CÓDIGO TRIBUTARIO. ASIMISMO, LAS CANTIDADES RETENIDAS DE CONFORMIDAD AL ARTÍCULO 161 DEL CÓDIGO TRIBUTARIO, CONSTITUIRÁN CRÉDITO FISCAL PARA LOS AGENTES DE RETENCIÓN, AMPARADOS POR EL MANDAMIENTO DE INGRESO DONDE CONSTE EL PAGO DEL IMPUESTO. EN AMBOS CASOS SE RECONOCERÁ DICHO CRÉDITO, SIEMPRE Y CUANDO SE DECLARE Y ENTERE ÍNTEGRAMENTE EN EL MISMO PERÍODO DE EMISIÓN DE LOS REFERIDOS DOCUMENTOS Y SE REGISTRE SEPARADAMENTE EL IMPUESTO RETENIDO DE LOS COMPROBANTES DE CRÉDITO FISCAL RECIBIDOS DE LOS PROVEEDORES.(8)" | IVA retained by retention agents per CT Art. 162 constitutes crédito fiscal FOR THE AGENT in the same period corresponding to the emission date of the comprobante de retención (CT Art. 112); amounts retained per CT Art. 161 constitute the agent's crédito fiscal backed by the MANDAMIENTO DE INGRESO evidencing the tax payment; IN BOTH CASES the credit is recognized only if declared and entered INTEGRALLY in the same period of emission of the referred documents and the retained tax registered SEPARATELY from the CCFs received from suppliers | `sv/sources/01_Ley_IVA.pdf` | Art. 65 p.31 (EVID-322; verified 01_ txt lines 1123-1133, PAGE 31) |
| LB-009 | Ley IVA, Art. 65, incisos finales + Ley IVA, Art. 70 | "LOS VALORES QUE NO SEAN DEDUCIBLES EN CONCEPTO DE CRÉDITO FISCAL, FORMARÁN PARTE DEL VALOR DE LOS BIENES Y SERÁN DEDUCIBLES PARA EFECTOS DE IMPUESTO SOBRE LA RENTA, SIEMPRE QUE LOS BIENES O SERVICIOS ADQUIRIDOS CUMPLAN CON LOS PRESUPUESTOS ESTABLECIDOS EN LA LEY QUE RIGE ESE TRIBUTO PARA SU DEDUCCIÓN.(8)" — "DENTRO DEL TÉRMINO ADQUISICIONES A QUE SE REFIERE ESTE ARTÍCULO DEBERÁ ENTENDERSE COMPRENDIDOS LAS COMPRAS LOCALES, LAS IMPORTACIONES Y LAS INTERNACIONES. (1) (8)" — Art. 70: "El presente impuesto pagado o causado no constituye un costo de los bienes y servicios adquiridos, importados o utilizados, respectivamente, salvo cuando los bienes o servicios estén destinados al uso o consumo final, a operaciones exentas o sujetos excluidos del presente impuesto. Tampoco es un gasto deducible para los efectos del impuesto sobre la renta." | Values not deductible as crédito fiscal become PART OF THE VALUE of the goods and are ISR-deductible provided the acquired goods/services meet the ISR law's deduction requirements; "adquisiciones" comprises local purchases, imports and internaciones; Art. 70 mirror: the tax paid or caused is NOT a cost of goods/services acquired/imported/used — SAVE when destined to final use or consumption, to exempt operations, or to subjects excluded from this tax — and is never an ISR-deductible gasto | `sv/sources/01_Ley_IVA.pdf` | Art. 65 final incisos p.32 (EVID-322; verified 01_ txt lines 1141-1147, PAGE 32); Art. 70 p.36 (EVID-322 zone; verified 01_ txt lines 1342-1346, PAGE 36) |
| LB-010 | Ley IVA, Art. 65-A encabezado + inciso final (giro identity) | "NO SERÁ DEDUCIBLE EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS SOPORTADO O PAGADO POR LOS CONTRIBUYENTES EN LA ADQUISICIÓN DE BIENES O DE SERVICIOS QUE NO CUMPLAN LOS REQUISITOS QUE ESTABLECE EL ARTÍCULO 65 DE ESTA LEY, EN CASOS COMO LOS QUE SE MENCIONAN A CONTINUACIÓN:(8)" — "PARA EFECTOS DE LO DISPUESTO EN LOS ARTÍCULOS 65 Y 65- A DE ESTA LEY, EL OBJETO, GIRO O ACTIVIDAD DEL CONTRIBUYENTE LO CONSTITUYE, AQUEL REGISTRADO EN LA ADMINISTRACIÓN TRIBUTARIA Y QUE SE INDIQUE EN LA TARJETA DE CONTRIBUYENTE. LA CALIDAD DE CONTRIBUYENTE Y EL OBJETO, GIRO O ACTIVIDAD DEL MISMO, DEBERÁ ACREDITARSE EN LAS ADQUISICIONES DE BIENES O DE SERVICIOS POR MEDIO DE LA TARJETA DE CONTRIBUYENTE RESPECTIVA. (8)" | Not deductible: the IVA borne or paid by contribuyentes on acquisitions failing the Art. 65 requirements, in cases such as those enumerated (the catalog below); for Arts. 65 and 65-A purposes the contribuyente's objeto/giro/actividad is THE ONE REGISTERED with the Administración Tributaria and indicated in the TARJETA DE CONTRIBUYENTE (identity rule), and contribuyente quality + giro are accredited at acquisitions by means of the respective tarjeta | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A intro p.32 + inciso final p.34 (EVID-323; verified 01_ txt lines 1149-1152 + 1250-1255, PAGE 32/34) |
| LB-011 | Ley IVA, Art. 65-A literales a)-e) | a) "ADQUISICIÓN DE VÍVERES O DE ALIMENTOS SI SU GIRO ORDINARIO NO ES LA VENTA DE VÍVERES O ALIMENTOS. (8) EN ESTE CASO LOS PROVEEDORES DEBERÁN EMITIR FACTURA.(8)" — b) "IMPORTACIÓN O INTERNACIÓN DE VÍVERES O DE ALIMENTOS SI SU GIRO ORDINARIO NO ES LA VENTA DE COMIDA O ALIMENTOS. (8)" — c) "ADQUISICIÓN, IMPORTACIÓN, INTERNACIÓN, ARRENDAMIENTO, MANTENIMIENTO, MEJORAS O REPARACIÓN DE VEHÍCULOS NUEVOS O USADOS, QUE POR SU NATURALEZA NO SEAN ESTRICTAMENTE INDISPENSABLES PARA LA REALIZACIÓN DEL GIRO ORDINARIO DEL CONTRIBUYENTE TALES COMO: AUTOMOTORES, AVIONES, HELICÓPTEROS, BARCOS, YATES, MOTOS ACUÁTICAS, LANCHAS Y OTROS SIMILARES. (8) (11)" + "TAMPOCO SERÁ DEDUCIBLE LA ADQUISICIÓN, IMPORTACIÓN O INTERNACIÓN DE COMBUSTIBLE, LUBRICANTES, REPUESTOS Y SERVICIOS DE MANTENIMIENTO PARA LOS BIENES MENCIONADOS EN ESTE LITERAL, NI LOS SEGUROS TOMADOS PARA ÉSTOS.(8) (11)" — d) "UTILIZACIÓN DE CUALQUIER TIPO DE SERVICIOS EN HOTELES, ASÍ COMO EL ARRENDAMIENTO O SUBARRENDAMIENTO DE INMUEBLES O LA UTILIZACIÓN DE CUALQUIER OTRO SERVICIO EN EL QUE ADQUIERA EL USO O GOCE DE TALES BIENES, CUANDO EL CONTRIBUYENTE NO DEMUESTRE QUE LOS SERVICIOS HAN SIDO UTILIZADOS EN ACTIVIDADES PROPIAS DEL NEGOCIO O QUE CORRESPONDEN AL GIRO O ACTIVIDAD DEL MISMO. (8)" — e) "ADQUISICIÓN DE BOLETOS AÉREOS, SALVO AQUELLOS ESTRICTAMENTE VINCULADOS CON VIAJES PROPIOS DEL NEGOCIO, CUANDO EL VIAJERO SEA EL CONTRIBUYENTE, SU REPRESENTANTE LEGAL O EMPLEADOS DE ÉSTE, CUYO VÍNCULO LABORAL PUEDA SER COMPROBADO. (8)" | a) food/víveres acquisitions when the ordinary giro is not selling them — suppliers must emit FACTURA in this case; b) food imports/internations idem (giro not food sale); c) acquisition/import/internation/lease/maintenance/improvement/repair of new or used vehicles NOT STRICTLY INDISPENSABLE for the ordinary giro — automotores, planes, helicopters, boats, yachts, jet-skis, launches and similar — NOR the fuel, lubricants, spare parts, maintenance services or insurance for them; d) hotel services of any type and leases/subleases or other services acquiring use of such inmuebles, when business-use/giro-use is not demonstrated; e) air tickets, save those strictly linked to the business's own travel when the traveler is the contribuyente, legal representative or employees with provable employment relationship | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A a)-e) pp.32-33 (EVID-323; verified 01_ txt lines 1153-1174, PAGE 32-33) |
| LB-012 | Ley IVA, Art. 65-A literales f)-k) | f) "ADQUISICIÓN, IMPORTACIÓN O INTERNACIÓN DE PRENDAS DE VESTIR, JOYERÍA O CALZADO, SI SU GIRO ORDINARIO NO ES LA VENTA DE DICHOS PRODUCTOS. (8)" — g) "ADQUISICIONES, IMPORTACIONES O INTERNACIONES DE BIENES MUEBLES CORPORALES O DE SERVICIOS DESTINADOS A SER UTILIZADOS A LA SATISFACCIÓN DE NECESIDADES PERSONALES O PARTICULARES DEL CONTRIBUYENTE, CÓNYUGE, COMPAÑERO O COMPAÑERA DE VIDA, SUS FAMILIARES, DEL REPRESENTANTE LEGAL, DIRECTIVOS, SOCIOS, ACCIONISTAS O FAMILIARES DE CUALQUIERA DE ELLOS, ASÍ COMO EMPLEADOS O TERCEROS.(8)" — h) "ADQUISICIÓN, IMPORTACIÓN O INTERNACIÓN DE BEBIDAS ALCOHÓLICAS, INCLUSIVE CERVEZA Y CIGARRILLOS, SI SU GIRO ORDINARIO NO ES LA VENTA DE DICHOS PRODUCTOS. (8)" — i) "LA SUMA TRASLADADA EN CONCEPTO DE CRÉDITO FISCAL, EN LO QUE EXCEDA A LA TASA O ALÍCUOTA LEGALMENTE ESTABLECIDA.(8)" — j) "EN GENERAL LA ADQUISICIÓN, IMPORTACIÓN O INTERNACIÓN DE CUALQUIER BIEN O SERVICIO QUE NO SEA INDISPENSABLE PARA LA REALIZACIÓN DEL OBJETO, GIRO O ACTIVIDAD DEL CONTRIBUYENTE. (8)" — k) "LOS BIENES MUEBLES CORPORALES QUE SE UTILICEN EN LA CONSTRUCCIÓN O EDIFICACIÓN DE BIENES INMUEBLES NUEVOS, ASÍ COMO LA RECONSTRUCCIÓN, REMODELACIÓN O MODIFICACIÓN, YA SEA TOTAL O PARCIAL DE BIENES INMUEBLES USADOS, SEAN DEL PROPIETARIO O POSEEDOR DEL INMUEBLE, ARRENDATARIO O USUFRUCTUARIO DEL MISMO. (11)" | f) clothing, jewelry or footwear when the giro is not their sale; g) goods/services destined to the personal or particular needs of the contribuyente, spouse/life companion, their relatives, legal representative, officers, partners, shareholders or relatives of any of them, as well as employees or third parties; h) alcoholic beverages including beer, and cigarettes, when the giro is not their sale; i) the amount shifted as crédito fiscal IN EXCESS of the legally established rate; j) in general any acquisition not indispensable for the object/giro/activity; k) corporal movable goods used in construction or edification of NEW inmuebles and reconstruction/remodeling/modification — total or partial — of USED inmuebles, whether the acquirer is owner, possessor, lessee or usufructuary | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A f)-k) p.33 (EVID-323; verified 01_ txt lines 1182-1200, PAGE 33) |
| LB-013 | Ley IVA, Art. 65-A literales l)-n) — **PRINTED STRUCTURE NOTE** | l) "LAS ADQUISICIONES DE BIENES O UTILIZACIÓN DE SERVICIOS, CUYOS MONTOS SEAN IGUALES O MAYORES A CINCUENTA Y OCHO SALARIOS MÍNIMOS QUE:(11)" — m) "NO SE REALICEN POR MEDIO DE CHEQUE, TRANSFERENCIA BANCARIA, TARJETAS DE CRÉDITO O DÉBITO. (11)" — n) "EL MEDIO DE PAGO SEA DIFERENTE AL EFECTIVO Y A LOS MEDIOS UTILIZADOS EN ROMANO i) Y NO SE FORMALIZACEN EN CONTRATO ESCRITO, ESCRITURA PÚBLICA O DEMÁS DOCUMENTOS QUE REGULA EL DERECHO CIVIL O MERCANTIL, TALES COMO: PERMUTAS, MUTUOS DE BIENES NO DINERARIOS, DACIONES EN PAGO, CESIONES DE TÍTULO DE DOMINIO DE BIENES, COMPENSACIONES DE DEUDAS U OPERACIONES CONTABLES. (11)" **Structural note:** the printed lettering is l)/m)/n) where l) introduces the ≥58-SMM acquisition class ("...QUE:") and m)/n) are the TWO FAILURE MODES hanging from it — m) paid NOT by cheque, bank transfer or credit/debit card (i.e. cash), n) paid by a medium OTHER THAN cash and OTHER THAN the m) media ("ROMANO i)" printed — read as the payment-media letter; the operative media list is m)) without formalization in written contract, escritura pública or other civil/mercantile-law documents (statutory exemplars: permutas, non-money mutuos, daciones en pago, cesiones of ownership titles, debt compensations, accounting operations) | l) acquisitions of goods or use of services whose amounts EQUAL OR EXCEED FIFTY-EIGHT SALARIOS MÍNIMOS (minimum monthly wages) that: m) are not realized by cheque, bank transfer or credit/debit cards (the cash failure mode); n) are paid by a medium different from cash and from the m) media AND are not formalized in written contract, public deed or other civil/mercantile-law documents (the barter-like failure mode) | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A l)-n) p.33 (EVID-323; verified 01_ txt lines 1201-1209, PAGE 33) |
| LB-014 | Ley IVA, Art. 65-A inciso (mixed-use vehicles 50%) | "SIN PERJUICIO DE LO ESTABLECIDO EN EL LITERAL c) DE ESTE ARTÍCULO, EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS PAGADO O CAUSADO POR CONTRIBUYENTES DEL IMPUESTO EN LA ADQUISICIÓN DE VEHÍCULOS AUTOMOTORES NUEVOS O USADOS A QUE SE REFIERE DICHO LITERAL, ÚNICAMENTE SERÁ DEDUCIBLE HASTA UN CINCUENTA POR CIENTO (50%), CUANDO DICHOS BIENES SEAN UTILIZADOS EN SU GIRO O ACTIVIDAD Y EN ACTIVIDADES AJENAS AL NEGOCIO, TODO DEBIDAMENTE COMPROBADO POR EL SUJETO PASIVO. IGUAL TRATAMIENTO SERÁ APLICABLE A LA ADQUISICIÓN DE COMBUSTIBLES, LUBRICANTES, REPUESTOS, SERVICIOS DE MANTENIMIENTO Y SEGUROS PARA LOS VEHÍCULOS AUTOMOTORES REFERIDOS.(8)" | Without prejudice to literal c): IVA paid or caused on acquisition of the literal-c) motor vehicles is deductible ONLY UP TO FIFTY PER CENT (50%) when the goods are used BOTH in the giro/activity AND in activities foreign to the business — all duly proven by the sujet pasivo; the SAME treatment applies to fuel, lubricants, spare parts, maintenance services and insurance for those vehicles | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A p.33 (EVID-323; verified 01_ txt lines 1211-1218, PAGE 33) |
| LB-015 | Ley IVA, Art. 65-A incisos (unauthorized numbering; fake/irregular documents; criminal reservation) | "TAMPOCO SERÁ DEDUCIBLE EL CRÉDITO FISCAL CONSIGNADO EN COMPROBANTES DE CRÉDITO FISCAL QUE POSEAN NUMERACIONES QUE NO HAYAN SIDO AUTORIZADAS POR LA ADMINISTRACIÓN TRIBUTARIA.(8)" — "NO CONSTITUYE CRÉDITO FISCAL Y EN CONSECUENCIA NO SERÁN DEDUCIBLES LOS VALORES DOCUMENTADOS EN COMPROBANTES DE CRÉDITO FISCAL, COMPROBANTES DE RETENCIÓN O NOTAS DE DÉBITO, CUANDO OCURRA CUALQUIERA DE LAS CIRCUNSTANCIAS SIGUIENTES:(8)" — "1) QUE EL SUJETO QUE CONSTA COMO EMISOR DEL DOCUMENTO NO SE ENCUENTRE INSCRITO COMO CONTRIBUYENTE.(8)" — "2) QUE AÚN ESTANDO INSCRITO COMO CONTRIBUYENTE EL EMISOR DEL DOCUMENTO, EL ADQUIRENTE DE LOS BIENES O PRESTATARIO DE LOS SERVICIOS NO COMPRUEBE LA EXISTENCIA EFECTIVA DE LA OPERACIÓN.(8)" — "3) QUE LOS DOCUMENTOS CORRESPONDAN A SUJETOS DESINSCRITOS POR LA ADMINISTRACIÓN TRIBUTARIA DE LA CALIDAD DE CONTRIBUYENTES, PUBLICADOS POR MEDIO DE INTERNET, DIARIO OFICIAL O CUALQUIERA DE LOS MEDIOS DE COMUNICACIÓN DE CIRCULACIÓN NACIONAL.(8)" — "4) QUE LAS NUMERACIONES CORRELATIVAS QUE CONSTAN EN LOS DOCUMENTOS, NO HAYAN SIDO ASIGNADAS Y AUTORIZADAS POR LA ADMINISTRACIÓN TRIBUTARIA. (11)" — "5) QUE LOS DOCUMENTOS NO SE ENCUENTREN A NOMBRE DEL CONTRIBUYENTE ADQUIRENTE DE LOS BIENES MUEBLES CORPORALES O PRESTATARIO DE LOS SERVICIOS, O QUE ESTANDO A SU NOMBRE NO COMPRUEBE HABER SOPORTADO EL IMPACTO ECONÓMICO DE LA OPERACIÓN. (11)" — "LO DISPUESTO EN LOS NUMERALES ANTERIORES ES SIN PERJUICIO DE LA ACCIÓN PENAL A QUE HAYA LUGAR, CONTRA EL AUTOR, COAUTOR, CÓMPLICE O PARTÍCIPES DEL ILÍCITO.(8)" | Nor is deductible the crédito consigned in CCFs bearing numbering NOT AUTHORIZED by the Administración Tributaria; values documented in CCFs, comprobantes de retención or notas de débito constitute NO crédito fiscal when: 1) the document's stated emitter is NOT registered as contribuyente; 2) even with a registered emitter, the acquirer/user does not prove the operation's effective existence; 3) the documents belong to subjects DE-REGISTERED from contribuyente status by the AT, published via internet, Diario Oficial or any nationally circulated media; 4) the documents' correlative numbering was not assigned and authorized by the AT; 5) the documents are not in the acquiring contribuyente's name, or being so, the economic impact of the operation is not proven absorbed; all without prejudice to the criminal action against author, co-author, accomplice or participants of the illicit | `sv/sources/01_Ley_IVA.pdf` | Art. 65-A pp.33-34 (EVID-323; verified 01_ txt lines 1227-1249, PAGE 33-34) |
| LB-016 | Reglamento IVA, Arts. 19-21 | Art. 19: "El impuesto pagado por los importadores o internadores que sean contribuyentes, constituye Crédito Fiscal para éstos, de acuerdo a lo establecido en el artículo 57 inciso tercero de la ley, y los documentos que prueban el pago serán la Póliza de Importación o Formulario Aduanero y el respectivo Recibo de Pago." Art. 20: "Con relación a lo prescrito en el artículo 58 de la ley, los sujetos que retiren bienes o autoconsuman servicios, no tendrán derecho a Crédito Fiscal. En todo caso, por cada retiro de bienes o autoconsumo de servicios, deberá emitirse la Factura correspondiente como consumidor final." Art. 21: "Se entendrá como gastos generales útiles o necesarios para el objeto, giro o actividad del contribuyente, aquéllos que son indispensables para el funcionamiento del negocio, establecimiento u oficina y que guarden relación directa con su objeto, giro o actividad." ["entendrá" sic as printed] | Art. 19: the tax paid by importer/internador contribuyentes is their Crédito Fiscal (Ley Art. 57 inciso tercero), proven by the Póliza de Importación or Formulario Aduanero AND the respective Recibo de Pago (the document pair); Art. 20: retirers/autoconsumers have no Crédito Fiscal right, and for each retiro/autoconsumo the corresponding Factura must be emitted "como consumidor final" (as a final consumer — lowercase as printed); Art. 21: gastos generales útil/necessary = those INDISPENSABLE for the functioning of the business, establishment or office and keeping DIRECT relation with the object/giro/activity | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Arts. 19-21 pp.6-7 (EVID-336; verified 02_ txt lines 219-234, PAGE 6-7) |
| LB-017 | Reglamento IVA, Arts. 22-23 | Art. 22: "Para que proceda la deducción del Crédito Fiscal se entenderá que la operación se encuentra debidamente registrada, cuando se haya anotado oportunamente en el Libro o Registro de Compras a que se refiere el artículo 107 de la ley." [stale ref: Ley Art. 107 derogated by D.L. 230/00 — now CT Art. 141] Art. 23: "Constituirán Crédito Fiscal para el agente de retención, las cantidades retenidas por las compras efectuadas o servicios utilizados, amparados por los Comprobantes de Retención respectivos, en el mismo período tributario, siempre que se hayan ingresado íntegramente al Fisco. Asimismo, las cantidades retenidas de conformidad al artículo 34 de la ley, constituirán Crédito Fiscal para los contribuyentes, siempre que estén amparadas por el Mandamiento de Ingreso y el recibo correspondientes." [stale ref: Ley Art. 34 derogated — now CT Art. 161] | Art. 22: "duly registered" for credit-deduction purposes = timely annotated in the Libro o Registro de Compras (the printed "Ley Art. 107" anchor is derogated — re-anchored to CT Art. 141); Art. 23: amounts retained on purchases/services, backed by the respective Comprobantes de Retención, constitute the retention AGENT's Crédito Fiscal in the same tax period, PROVIDED they have been integrally entered to the Fisco; amounts retained per the printed Ley-Art.-34 rule (now CT Art. 161) constitute the contribuyentes' Crédito Fiscal when backed by the Mandamiento de Ingreso and the corresponding receipt | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Arts. 22-23 p.7 (EVID-336; verified 02_ txt lines 235-244, PAGE 7) |
| LB-018 | Código Tributario (D.L. 4-2004 y reformas), Arts. 161-162 — **CO-LB (retention matrix owned elsewhere)** | Art. 161: "EL ADQUIRENTE DE LOS BIENES Y EL PRESTATARIO O BENEFICIARIO DE LOS SERVICIOS, CUANDO QUIEN TRANSFIERE EL BIEN O EL PRESTADOR DE LOS SERVICIOS NO TENGA DOMICILIO NI RESIDENCIA EN EL PAÍS ES EL OBLIGADO AL PAGO DEL IMPUESTO. PARA ESTE EFECTO DEBERÁN EFECTUAR LAS RETENCIONES PERTINENTES Y ENTERARLAS MEDIANTE MANDAMIENTO DE PAGO EMITIDO POR LA ADMINISTRACIÓN TRIBUTARIA. (1)" Art. 162 (primer inciso): "TODOS LOS SUJETOS PASIVOS QUE CONFORME A LA CLASIFICACIÓN EFECTUADA POR LA ADMINISTRACIÓN TRIBUTARIA OSTENTEN LA CATEGORÍA DE GRANDES CONTRIBUYENTES Y QUE ADQUIERAN BIENES MUEBLES CORPORALES O SEAN PRESTATARIOS O BENEFICIARIOS DE SERVICIOS DE OTROS CONTRIBUYENTES QUE NO PERTENEZCAN A ESA CLASIFICACIÓN, DEBERÁN RETENER EN CONCEPTO DE ANTICIPO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS EL UNO POR CIENTO SOBRE EL PRECIO DE VENTA DE LOS BIENES TRANSFERIDOS O DE LA REMUNERACIÓN DE LOS SERVICIOS PRESTADOS, LA CUAL DEBERÁ SER ENTERADA SIN DEDUCCIÓN ALGUNA EN EL MISMO PERIODO TRIBUTARIO EN EL QUE SE EFECTÚE LA ADQUISICIÓN DE BIENES O DE SERVICIOS …" | Art. 161: when the transferor/prestador has no domicile or residence in the country, the acquirer/beneficiary is obliged to the tax payment, effecting the retentions and entering them via the AT-issued mandamiento de pago; Art. 162: grandes contribuyentes acquiring from non-grandes must retain 1% of the sale price/remuneration as IVA anticipo, entered without deduction in the same period as the acquisition — NOTE: the full retention matrix (percentages, $100 floor, designated agents, 162-A/162-B, caña/café/leche 13% rows) is owned by `fiscal-reporting/04_f07-annexes-retentions-events.md`; this row anchors only the credit-release gate's CT basis | `sv/sources/05_Codigo_Tributario.pdf` | CT Arts. 161-162 pp.90-91 (co-LB for EVID-322 retention incisos; verified 05_ txt lines 3860-3864, PAGE 90 + lines 3874-3883, PAGE 91) |

Dead text — never implementable as current law (recorded as notes, not FRs):
Ley Art. 59 (documentos falsos heading zone) is DEROGADO (D.L. 230/00) —
its living successor content is the Art. 65-A fake-documents list cited
from the post-reform text; Ley Arts. 97/100/107/34 anchors printed inside
Arts. 57/65 and Rgto. Arts. 22-23 are derogated references re-anchored to
the CT document/register regime (CT Arts. 110-115, 141, 161 — noted per
row). The 65-A n) "ROMANO i)" cross-reference prints as shown; it is
encoded as a printed-structure note, never as an operative pointer to a
different article. The SOQ-54 vintage watch (§2 preamble) applies to every
row above.

## 3. Functional Requirements

### 3.1 Traslación and the credit-document root (Art. 57; Rgto. Art. 19)

- **SV-TAX-FR-246:** The system shall model the crédito fiscal as the
  amount *trasladado* (shifted) by contribuyentes to acquirers of goods
  and users of services — EQUAL to the débito fiscal generated in each
  gravada operation (débito computation owned by the determination file
  of this wave; rate/base resolution owned by `09_iva-base-rate.md`
  SV-TAX-FR-225/240 — cited by id, never restated) — and shall require
  that the shifted amount appear in the Comprobante de Crédito Fiscal
  EN FORMA SEPARADA DEL PRECIO O REMUNERACIÓN (separately from the price
  or remuneration), payable jointly with it: this is the legal root of
  the document-type price contract — CCF/CCFE carry the IVA as a
  SEPARATE line over the net price
  (`e-invoicing/01_document-types.md` SV-EINV-FR-024), while the FE
  consumer document embeds it inclusively (SV-EINV-FR-019 — both cited
  by id as the R1 contract roots; this file supplies the legal gate, the
  DTE layer owns emission).
  (LB-001; EVID-317; EINV 01-file SV-EINV-FR-019/024)
- **SV-TAX-FR-247:** For importers/internadores that are contribuyentes,
  the system shall constitute their crédito fiscal from the IVA paid at
  the importación or internación (Art. 57 inciso tercero), with the
  credit PROVEN by the Reglamento Art. 19 document PAIR: the *Póliza de
  Importación o Formulario Aduanero* (customs declaration — DUCA family)
  AND the respective *Recibo de Pago* (payment receipt) — an import
  credit line lacking either leg of the pair shall not release to the
  credit ledger (proof fields recorded on the import move; the import
  operation classification itself is `07_iva-framework.md`
  SV-TAX-FR-187/189 — by id).
  (LB-001; LB-016; EVID-317/336)

### 3.2 No-credit operations (Arts. 58-61; Rgto. Art. 20)

- **SV-TAX-FR-248:** The system shall generate NO crédito fiscal from
  retiros of giro goods or autoconsumo of services (Arts. 11/16 facts —
  retiro engine owned by `07_iva-framework.md` SV-TAX-FR-183..186, by
  id), whatever their gravada/exenta/no-sujeta classification, and shall
  enforce the documentation ban: those operations are documented with
  FACTURA or an authorized equivalent document, and a CCF or NOTA DE
  DÉBITO is used IN NO CASE — the emission-side routing (auto factura
  *como consumidor final*, lowercase as printed, per Rgto. Art. 20)
  rides the T1 retiro engine (SV-TAX-FR-186), while THIS file owns the
  credit-side lock: any tax line on a self-retiro/autoconsumo document
  is barred from the credit ledger (hard block, no override).
  (LB-002; LB-016; EVID-317/336; cross-ref SV-TAX-FR-186)
- **SV-TAX-FR-249:** For amounts *trasladado* to Art.-28 excluidos
  (no contribuyentes), the system shall generate NO crédito fiscal for
  the excluido and shall post them as COST of the respective goods and
  services (Art. 60, cross-referencing Arts. 31/65) — the excluido status
  and no-credit lock are owned by `07_iva-framework.md` SV-TAX-FR-205
  (by id); this file supplies the cost-routing consequence on the
  acquirer's books.
  (LB-003; EVID-318; cross-ref SV-TAX-FR-205)
- **SV-TAX-FR-250:** The system shall treat the crédito fiscal
  exclusively as an element of the IVA structure governed by this law's
  norms (Art. 61 *naturaleza jurídica*): it shall NEVER be netted or
  claimed as a credit against the fisco for *pago indebido o en exceso*
  (undue or excess payment) of this tax — overpayment/repetition claims
  route through the Código Tributario procedure (CT re-anchor), not
  through the credit ledger; the credit engine exposes no "refund" path
  on IVA credit accounts.
  (LB-003; EVID-318)

### 3.3 Art. 65 deductibility gates

- **SV-TAX-FR-251:** The system shall make crédito fiscal deductible
  ONLY for the four Art. 65 destination gates — 1) acquisitions of
  *bienes muebles corporales* destined to the ACTIVO REALIZABLE; 2)
  activo fijo goods WHEN they keep their individuality in it and are NOT
  incorporated into a *bien inmueble*; 3) disbursements for services
  used in the GIRO, PROVIDED they are not destined to construction or
  edification of inmuebles NOR to reconstruction, remodeling or
  modification — total or partial — of inmuebles, whether or not owned
  by the contribuyente, INDISTINCTLY of contract modality (precio
  alzado, administración de obra, or any other); 4) GASTOS GENERALES
  destined exclusively to the object/giro/activity (statutory examples:
  *fletes o acarreos, energía eléctrica, teléfono o agua*) — every
  purchase line classified against this destination enum before any
  credit release.
  (LB-004; EVID-322)
- **SV-TAX-FR-252:** The system shall require, IN ADDITION to the
  destination gate, that the acquisition be INDISPENSABLE for the
  object/giro/activity AND for the generation of gravada operations —
  accepting as gravada-generation: operations generating DÉBITO FISCAL;
  operations gravada at TASA CERO (0% — dated rate rows
  `09_iva-base-rate.md` SV-TAX-FR-240, by id); donations of goods or
  services to the ISR-Art.-6 institutions; and sales in favor of
  misiones diplomáticas, consulates, international organizations and
  their members accredited before the Government (stamp 13) — failing
  either limb (indispensable OR gravada-generation), the credit is NOT
  deductible and falls to the blocked state (the exemption-vs-0%
  classification feed is `08_iva-exemptions.md` SV-TAX-FR-206/224, by
  id; partial-generation pro-rata is the Art. 66 file's surface, never
  restated here).
  (LB-005; EVID-322; cross-ref SV-TAX-FR-206/224/240)
- **SV-TAX-FR-253:** For acquisitions of goods or services that do NOT
  frame in / comply with the preceding gates, the system shall route
  documentation to FACTURA (the else-branch): the purchasing
  contribuyente must NOT request emission or delivery of a CCF but of a
  factura, and the supplier is OBLIGED to emit and deliver it — enforced
  on the purchase line as a document-type constraint (credit expected ⇒
  CCF; credit barred ⇒ factura), with the counterpart warning surfaced
  at validation (DTE emission mechanics owned by the e-invoicing stack,
  by id).
  (LB-006; EVID-322)
- **SV-TAX-FR-254:** The system shall require the Art. 65 FORMAL
  requirements before any credit release: (a) the credit-originating
  operation documented with the ORIGINAL CCF showing the crédito amount
  EN FORMA SEPARADA from the price/remuneration — OR documentary proof
  of the import/internación tax paid (FR-247 pair); (b) all duly
  registered in the LIBRO DE COMPRAS of CT Art. 141 AND in formal
  accounting or special books (per obligation to carry formal
  accounting — Rgto. Art. 22: duly registered = timely annotated in the
  Libro o Registro de Compras, stale Ley-107 anchor re-anchored to CT
  141); and (c) for BIENES MUEBLES CORPORALES, the purchase also
  recorded in the REGISTRO DE CONTROL DE INVENTARIOS of CT Arts.
  142/142-A, referencing the legal document — the CT register surfaces
  are the fiscal-books wave's; this file states the credit-blocking
  check and consumes their registration states by id.
  (LB-007; LB-017; EVID-322/336)
- **SV-TAX-FR-255:** The system shall scope the Art. 65 term
  ADQUISICIONES as comprising COMPRAS LOCALES, IMPORTACIONES and
  INTERNACIONES (all three acquisition kinds eligible for the gates),
  and shall resolve GASTOS GENERALES per Reglamento Art. 21: those
  indispensable for the functioning of the business, establishment or
  office AND keeping direct relation with the object, giro or activity
  (["entendrá" sic as printed] — the gate-4 classification hint).
  (LB-009; LB-016; EVID-322/336)

### 3.4 Retention credits (Art. 65 final incisos; Rgto. Art. 23; CT Arts. 161-162)

- **SV-TAX-FR-256:** The system shall credit CT-Art.-162 IVA retentions
  to the retention AGENT as crédito fiscal IN THE SAME PERIOD
  corresponding to the emission date of the comprobante de retención
  (CT Art. 112 document), releasing the credit ONLY IF: (a) the
  retention is DECLARED and ENTERED ÍNTEGRAMENTE (integrally) to the
  fisco in that SAME period of emission, AND (b) the retained tax is
  registered SEPARATELY from the CCFs received from providers — the
  release gate emits the credit in the agent's declaration only upon
  both conditions (declaration+entero state from the retention ledger;
  the RETENTION MATRIX — agents, percentages, floors — is owned by
  `fiscal-reporting/04_f07-annexes-retentions-events.md`, by id, and the
  post-entero re-entry into F-07 casilla 128 by
  `fiscal-reporting/03_f07-annexes-purchases.md` SV-FREP-FR-091 and the
  F-930 view by SV-FREP-FR-111 — both cited by id as consumers).
  (LB-008; LB-017; LB-018; EVID-322/336; FREP 03-file SV-FREP-FR-091;
  FREP 04-file SV-FREP-FR-111)
- **SV-TAX-FR-257:** The system shall credit amounts retained under CT
  Art. 161 (non-domiciled transferor/prestador operations, where the
  acquirer is obligado al pago) to the retaining contribuyente ONLY via
  the MANDAMIENTO DE INGRESO evidencing the tax payment, together with
  the corresponding receipt (Rgto. Art. 23, stale Ley-34 anchor
  re-anchored to CT 161), under the same EN AMBOS CASOS conditions as
  FR-256 (declared + integrally entered in the same emission period +
  separately registered) — the credit posts against the mandamiento
  reference, never against the bare operation record.
  (LB-008; LB-017; LB-018; EVID-322/336)

### 3.5 Art. 65-A non-deductible catalog

- **SV-TAX-FR-258:** The system shall apply the Art. 65-A catalog to IVA
  borne or paid on acquisitions failing the Art. 65 requirements, and
  shall resolve the contribuyente's OBJETO/GIRO/ACTIVIDAD for ALL
  Art. 65/65-A purposes as THE ONE REGISTERED with the Administración
  Tributaria and indicated in the TARJETA DE CONTRIBUYENTE (identity
  rule) — contribuyente quality and giro accredited at acquisitions by
  the respective tarjeta — so every giro-relative gate (a/b/f/h/j and
  the indispensable test) evaluates against the registered giro, never
  against a self-declared activity.
  (LB-010; EVID-323)
- **SV-TAX-FR-259:** The system shall block the credit for: a)
  acquisition of *víveres o alimentos* when the ordinary giro is not
  their sale — WITH the supplier-side obligation flag: in this case the
  PROVIDERS must emit FACTURA (the Art. 65-A a) routing note); and b)
  importación or internación of *víveres o alimentos* when the ordinary
  giro is not the sale of *comida o alimentos* — the blocked state
  carries letter reason a) or b).
  (LB-011; EVID-323)
- **SV-TAX-FR-260:** The system shall block the credit for acquisition,
  importación, internación, lease, maintenance, improvements or repair
  of new or used VEHICLES that by their nature are not ESTRICTAMENTE
  INDISPENSABLES for the ordinary giro (statutory class: *automotores,
  aviones, helicópteros, barcos, yates, motos acuáticas, lanchas y
  otros similares*), AND equally for the acquisition, importación or
  internación of COMBUSTIBLE, LUBRICANTES, REPUESTOS and MAINTENANCE
  SERVICES for such goods, NOR the SEGUROS taken for them (letter c)
  with its running-costs extension).
  (LB-011; EVID-323)
- **SV-TAX-FR-261:** The system shall block the credit for: d) use of
  any type of HOTEL services — and leases/subleases of such inmuebles
  or any other service acquiring their use or enjoyment — UNLESS the
  contribuyente demonstrates use in the business's own activities or
  correspondence with the giro (business-use evidence flag lifts the
  block); e) AIR TICKETS, save those strictly linked to the business's
  own travel when the traveler is the contribuyente, its legal
  representative or EMPLOYEES whose *vínculo laboral* (employment
  relationship) is provable (employee link recorded on the expense).
  (LB-011; EVID-323)
- **SV-TAX-FR-262:** The system shall block the credit for: f)
  acquisition/importación/internación of *prendas de vestir, joyería o
  calzado* when the giro is not their sale; g) goods or services
  destined to the satisfaction of PERSONAL OR PARTICULAR needs of the
  contribuyente, *cónyuge, compañero o compañera de vida*, their
  relatives, the legal representative, *directivos, socios, accionistas*
  or relatives of any of them, as well as employees or third parties
  (destination-enum gate); h) *bebidas alcohólicas, inclusive cerveza,*
  and *cigarrillos* when the giro is not their sale.
  (LB-012; EVID-323)
- **SV-TAX-FR-263:** The system shall block the credit for: i) the suma
  trasladada as crédito fiscal IN EXCESS of the legally established rate
  (over-rate excess — the rate resolved from the dated rows of
  `09_iva-base-rate.md` SV-TAX-FR-240, by id; only the excess portion
  blocks, the legal-rate portion remains creditable when otherwise
  eligible); j) IN GENERAL any acquisition, importación or internación
  of goods or services NOT indispensable for the object/giro/activity;
  k) bienes muebles corporales used in the CONSTRUCTION OR EDIFICATION
  of NEW inmuebles, and in the RECONSTRUCTION, REMODELING or
  MODIFICATION — total or partial — of USED inmuebles, whether the
  acquirer is owner, possessor, *arrendatario* or *usufructuario* of the
  inmueble (mirrors the Art. 65-3 service exclusion on the goods side —
  construction-service and construction-input purchases block alike).
  (LB-012; EVID-323; cross-ref SV-TAX-FR-240)
- **SV-TAX-FR-264:** The system shall block the credit for acquisitions
  of goods or use of services whose amounts EQUAL OR EXCEED FIFTY-EIGHT
  SALARIOS MÍNIMOS (58 SMM) that fail either payment-form gate, encoded
  in the PRINTED l)/m)/n) structure — l) introduces the ≥58-SMM
  acquisition class; m) the CASH failure mode: not realized by cheque,
  bank transfer, or credit/debit cards; n) the NON-BANK-MEDIA failure
  mode: paid by a medium other than cash and other than the m) media —
  *permutas, mutuos de bienes no dinerarios, daciones en pago, cesiones
  de título de dominio, compensaciones de deudas, operaciones
  contables* — WITHOUT formalization in contrato escrito, escritura
  pública or the documents civil/mercantile law regulates (the n)
  "ROMANO i)" printed cross-reference is encoded as a structure note,
  its operative reading being the m) media list); the 58-SMM threshold
  resolves as-of the operation date from the DATED SMM tariff rows of
  `payroll/02_minimum-wage.md` through its sector-mapping configuration
  (SV-PAY-FR-022, by id — SOQ-18 sector selection, OQ-2 below); the
  payment media and formal-document reference record on the payment, and
  the threshold compares against the operation amount (which sector
  feeds the gate rides the SOQ-18 config — never an encoded SMM value).
  (LB-013; EVID-323; cross-ref SV-PAY-FR-022)
- **SV-TAX-FR-265:** For the literal-c) motor vehicles used BOTH in the
  giro/activity AND in activities AJENAS al negocio (mixed use), all
  duly proven by the sujet pasivo, the system shall cap the deductible
  credit at FIFTY PER CENT (50%) — the other 50% routing to cost — and
  shall apply the SAME 50% treatment to the acquisition of COMBUSTIBLES,
  LUBRICANTES, REPUESTOS, MAINTENANCE SERVICES and SEGUROS for those
  vehicles (the mixed-use evidence flag on the vehicle record drives
  both the acquisition split and the running-cost split; fully-extra-giro
  use remains 100% blocked per FR-260, fully-giro use remains 100%
  creditable when otherwise eligible).
  (LB-014; EVID-323)
- **SV-TAX-FR-266:** The system shall block the credit consigned in
  CCFs bearing NUMBERING NOT AUTHORIZED by the Administración
  Tributaria — validated at ingestion against the DTE authorization
  ranges (the numbering-authorization registry surface, e-invoicing
  stack by id; a CCF outside authorized ranges never enters the credit
  ledger, whatever its other merits).
  (LB-015; EVID-323)
- **SV-TAX-FR-267:** The system shall treat as constituting NO crédito
  fiscal — and hence never deductible — values documented in CCFs,
  comprobantes de retención or notas de débito when ANY of the five
  circumstances occurs: 1) the stated EMITTER is not registered as
  contribuyente; 2) even with a registered emitter, the
  acquirer/prestatario does not prove the operation's EFFECTIVE
  EXISTENCE; 3) the documents belong to subjects DE-REGISTERED from
  contribuyente status by the AT and published (internet, Diario Oficial
  or nationally circulated media — de-registration feed consumed, by
  id); 4) the CORRELATIVE NUMBERING was not assigned and authorized by
  the AT; 5) the documents are NOT in the acquiring contribuyente's
  name, or being so, the ECONOMIC IMPACT of the operation is not proven
  absorbed — each a hard block with its numeral reason recorded, and all
  WITHOUT prejudice to the criminal action against author, co-author,
  accomplice or participants (the criminal reservation is a recorded
  note, never a system action).
  (LB-015; EVID-323)
- **SV-TAX-FR-268:** Values blocked from the crédito fiscal (any
  blocked state of FR-251..267) shall form PART OF THE VALUE of the
  goods (or the expense) and be ISR-deductible ONLY IF the acquired
  goods/services meet the deduction requirements of the ISR law —
  mirrored by Art. 70 (IVA is no cost save final-use/exempt/excluded
  destinations and never an ISR gasto) and consumed by the ISR
  deduction file (`taxation/02_isr-deductions.md` SV-TAX-FR-045 excludes
  IVA from ISR deductions subject to Ley IVA Art. 70 — by id): the
  blocked-credit reclassification entry (IVA → asset/expense value)
  fires automatically at block resolution, its ISR-deductibility
  governed by the ISR rules, never by this file.
  (LB-009; EVID-322; cross-ref taxation/02-file SV-TAX-FR-045)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the 58-SMM threshold is COMPUTED (58 × the
dated SMM row selected through `payroll/02_minimum-wage.md`
SV-PAY-FR-022's configuration — values never encoded here); the 50% and
catalog rules are enums/logic, not tables. The only version regimes are
the SOQ-54 consolidation watch riding every LB (§2) and the D15
as-of-date resolution of the SMM feed and rate feed (both snapshotted on
the record). Layer semantics: this file introduces Odoo-side
credit-eligibility computation data only (wave default `odoo`; see §5).

**Credit eligibility engine (purchase side):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (purchase, SV extension) | l10n_sv_iva_credit_state | select (computed, stored) | eligible · blocked · fifty_percent · pending_formal · pending_retention_release | FR-251..254, FR-256, FR-265 |
| account.move.line (purchase, SV extension) | l10n_sv_iva_credit_block_reason | select | destination_gate · not_indispensable · no_gravada_generation · else_branch_factura · formal_requirement · a_food · b_food_import · c_vehicle · c_vehicle_running · d_hotel · e_air_ticket · f_clothing · g_personal_family · h_alcohol_tobacco · i_over_rate · j_non_indispensable · k_construction_input · lmn_smm_cash · lmn_smm_no_formal_doc · unauthorized_numbering · fake_doc_1..5 · retention_not_released · retiro_autoconsumo · excluido_cost | FR-248, FR-249, FR-251..267 |
| account.move.line (purchase, SV extension) | l10n_sv_iva_credit_pct | integer (computed) | 100 · 50 · 0 — from state (fifty_percent ⇒ 50; blocked ⇒ 0) | FR-265 |
| account.move.line (purchase, SV extension) | l10n_sv_iva_destination_gate | select | activo_realizable · activo_fijo_individual · servicio_giro (excl. construction/reconstruction/remodeling/modification of inmuebles) · gasto_general · outside_gates | FR-251 |
| account.move.line (purchase, SV extension) | l10n_sv_iva_indispensable, l10n_sv_iva_gravada_generation | boolean / select | gravada-generation sources: débito · tasa_cero · isr6_donation · diplomatic_sale | FR-252 |
| account.move.line (hotel/air-ticket, SV extension) | l10n_sv_iva_business_use_proof, l10n_sv_iva_employee_link | char ref / m2o | d) business-use evidence; e) provable vínculo laboral (employee record) | FR-261 |
| account.move.line (vehicle-related, SV extension) | l10n_sv_iva_vehicle_class_c | boolean (computed from product) | literal-c) vehicle or its running cost (fuel/lubricants/repuestos/mantenimiento/seguros) | FR-260, FR-265 |
| account.move.line (mixed-use vehicle, SV extension) | l10n_sv_iva_mixed_use_50 | boolean | giro + extra-giro use, duly proven by the sujet pasivo ⇒ 50% split | FR-265 |
| account.asset / fleet link (SV extension) | l10n_sv_iva_mixed_use_50 | boolean | drives both acquisition and running-cost splits for that vehicle | FR-265 |

**58-SMM payment-form gate:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.payment / account.move.line (payment, SV extension) | l10n_sv_iva_payment_media | select | cheque · transferencia_bancaria · tarjeta_credito · tarjeta_debito · efectivo · otro_no_bancario | FR-264 |
| account.payment (SV extension) | l10n_sv_iva_formal_doc_ref | m2o / char | contrato escrito / escritura pública / civil-mercantile document backing non-bank media | FR-264 |
| account.move.line (purchase, SV extension) | l10n_sv_iva_smm_gate_result | computed | threshold = 58 × SMM (SV-PAY-FR-022 config, dated rows — as-of operation date, D15 snapshot); fail modes: m_cash · n_media_no_formal_doc | FR-264 |

**Import credit proof (FR-247):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (import, SV extension) | l10n_sv_iva_import_credit_docs | 2× char ref (required pair) | Póliza de Importación / Formulario Aduanero (DUCA) + Recibo de Pago | FR-247 |

**Retention credit release (FR-256/257; ledger owned by FREP 04-file):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.retention (SV extension on FREP ledger) | l10n_sv_iva_agent_credit_release | select | pending → released · failed_period | release IF declared + entered integrally same emission period + separately registered (CT 162 / CT 161 routes) |
| l10n_sv.iva.retention (CT-161 route) | l10n_sv_iva_mandamiento_ref | char ref | mandamiento de ingreso + recibo evidencing payment | FR-257 |

**Giro identity (FR-258):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner (SV extension) | l10n_sv_tarjeta_giro | char (from tarjeta de contribuyente) | the registered objeto/giro/actividad — identity for ALL Art. 65/65-A gates | FR-258 |

**Blocked-value reclassification (FR-268):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (auto, SV extension) | l10n_sv_iva_blocked_to_cost_entry | boolean + m2o | auto journal entry: blocked IVA → asset/expense value (ISR-deductibility per taxation/02 rules, by id) | FR-268 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = credit-eligibility computation
logic living in the LGPL client. No SaaS rows are introduced: nothing
here touches DTE generation/transformation (the FE-inclusive/CCF-net
price contract and the authorization-range checks are the e-invoicing
stack's surfaces — cited by id; this file supplies the legal gates the
client applies at purchase validation). Model names are stable across
Odoo 17/18/19/20 (`account.move`, `account.move.line`, `account.payment`,
`res.partner`, `account.asset`); version-specific behavior is recorded
per row where a legal vintage exists. D15 doctrine (binding): the
58-SMM threshold and any rate-dependent check resolve as-of the
operation's tax-point date from dated parameter rows and snapshot on the
record; corrections use original-period parameters.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-246 | odoo | account.tax + computation guard | CCF separate-IVA contract root | CCF/CCFE net + separate IVA (EINV SV-EINV-FR-024); FE inclusive (SV-EINV-FR-019) — by id; débito/rate from determination + base/rate files |
| FR-247 | odoo | account.move (import) | import_credit_docs pair | Póliza/DUCA + recibo required pair; credit lock until both legs; import classification from SV-TAX-FR-187/189 |
| FR-248 | odoo | account.move.line guard | retiro/autoconsumo no-credit lock | CCF/ND ban; emission routing on T1 retiro engine (SV-TAX-FR-186 — Rgto. Art. 20 factura consumidor final); hard block, no override |
| FR-249 | odoo | account.move.line | excluido-purchase → cost | Excluido status from SV-TAX-FR-205 (by id); Art. 60 cost posting |
| FR-250 | odoo | computation guard | no refund path on credit accounts | Art. 61 naturaleza jurídica; overpayment claims route CT procedure |
| FR-251 | odoo | account.move.line | destination_gate enum | Four gates; gate 3 excludes construction/reconstruction/remodeling/modification of inmuebles any modality; gate 4 examples fletes/acarreo, energía, teléfono, agua |
| FR-252 | odoo | account.move.line | indispensable + gravada_generation | Sources: débito · 0% (SV-TAX-FR-240 rows) · ISR-6 donations · diplomatic (stamp 13); either limb fails ⇒ blocked; pro-rata = Art. 66 file |
| FR-253 | odoo | account.move.line constraint | else-branch factura routing | Credit barred ⇒ FACTURA; buyer must not request CCF; supplier obliged to emit; counterpart warning at validation |
| FR-254 | odoo | account.move.line checks | formal requirements | Original CCF w/ separate crédito or import proof; libro de compras CT 141 + contabilidad (Rgto. 22 re-anchor); goods ⇒ CT 142/142-A inventory register ref |
| FR-255 | odoo | computation | adquisiciones scope + gasto_general def | Local + imports + internaciones; Rgto. 21 definition (["entendrá" sic]) |
| FR-256 | odoo | l10n_sv.iva.retention (SV ext) | agent_credit_release | Same emission period IF declared + entered integrally + separately registered; matrix owned by FREP 04-file; consumers SV-FREP-FR-091 (casilla 128) + SV-FREP-FR-111 (F-930) |
| FR-257 | odoo | l10n_sv.iva.retention (CT-161 route) | mandamiento_ref | CT 161 non-domiciled route; mandamiento de ingreso + recibo; same EN AMBOS CASOS conditions |
| FR-258 | odoo | res.partner | tarjeta_giro identity | Registered giro from tarjeta de contribuyente — identity for every giro-relative gate |
| FR-259 | odoo | account.move.line | blocks a)/b) + supplier-factura flag | Food local (a, supplier FACTURA obligation) and imports (b) outside giro |
| FR-260 | odoo | account.move.line + product.template | c) vehicle + running costs | Not-strictly-indispensable vehicles (statutory class) + fuel/lubricants/repuestos/mantenimiento/seguros |
| FR-261 | odoo | account.move.line | d)/e) evidence gates | Hotel business-use proof lifts d); air ticket save provable-vínculo-laboral business travel (e) |
| FR-262 | odoo | account.move.line | f)/g)/h) blocks | Clothing/jewelry/calzado; personal-family destinations (full statutory list); alcohol incl. cerveza + cigarettes — all outside-giro-conditioned |
| FR-263 | odoo | account.move.line | i)/j)/k) blocks | Over-rate excess (legal-rate portion stays creditable); general non-indispensable; construction/edification inputs (new) + reconstruction/remodeling (used), any real-right capacity |
| FR-264 | odoo | account.payment + account.move.line | 58-SMM gate (l/m/n printed structure) | m) cash failure; n) non-bank media without formal doc; threshold 58 × SMM from payroll/02 dated rows via SV-PAY-FR-022 config (SOQ-18 → OQ-2); D15 snapshot |
| FR-265 | odoo | account.asset/fleet + move.line | mixed_use_50 | 50% credit / 50% cost for giro+extra-giro vehicles AND their running costs, proven by sujet pasivo |
| FR-266 | odoo | account.move.line ingestion check | unauthorized-numbering block | Validated vs DTE authorization ranges (e-invoicing registry surface, by id) |
| FR-267 | odoo | account.move.line ingestion checks | fake-doc 1)-5) blocks | Emitter unregistered; operation unproven; de-registered published subject; unauthorized correlativos; not-in-name / economic impact unabsorbed; criminal reservation = recorded note only |
| FR-268 | odoo | account.move (auto) | blocked_to_cost_entry | Blocked IVA → asset/expense value; ISR-deductibility per taxation/02 SV-TAX-FR-045 (Art. 70 mirror, by id) |

Version-regime notes (D12/D15): FR-264's threshold is a computed dated
parameter (58 × the sector SMM row selected through SV-PAY-FR-022's
configuration; Decreto rows and their vigencia windows live in
payroll/02 — by id; the as-of resolution and snapshot ride D15, the
sector selection gap rides OQ-2/SOQ-18). FR-263's over-rate check
consumes the dated rate rows of SV-TAX-FR-240 (10% → 13% D.L. 370-1995
history — by id). The SOQ-54 consolidation watch rides every LB (§2
preamble) — re-verify against a current official consolidation at
implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a CCF purchase line where the document shows the IVA
  inside the price (no separate crédito line), when validation runs,
  then the line is flagged formal-requirement-failed and NO credit
  releases until the original CCF with the separately-stated crédito (or
  the import-proof pair) is recorded (FR-246, FR-254).
- **AC-002:** Given a definitive import of goods with IVA $1,300.00 paid
  at aduana, when the import move carries the DUCA/póliza reference but
  NO recibo de pago, then the $1,300.00 stays credit-locked; given the
  recibo leg recorded, then the credit releases to the ledger as
  importer crédito fiscal (FR-247).
- **AC-003:** Given a retiro of giro goods by the owner's family member
  (Art. 11 fact, T1 engine), when the auto-document is generated, then
  it is a consumidor-final FACTURA (never CCF/ND) and NO crédito fiscal
  line is ever created from it — any attempt to reference it in the
  credit ledger is rejected (FR-248).
- **AC-004:** Given a purchase of construction services for the
  remodeling of the company's own warehouse (Art. 65 numeral 3
  exclusion, any modality), when validation runs, then the IVA on the
  line is BLOCKED at validation with reason `destination_gate`/
  `k_construction_input` semantics and the else-branch FACTURA routing
  applies (no CCF may be requested) (FR-251, FR-253, FR-263).
- **AC-005:** Given a purchase whose IVA $260.00 fails the
  gravada-generation limb (destination: an exempt-only activity), when
  the block resolves, then an automatic entry reclassifies $260.00 into
  the asset/expense value and its ISR-deductibility is evaluated under
  the ISR rules (taxation/02 by id), never as IVA credit (FR-252,
  FR-268).
- **AC-006:** Given a CT-162 retention of $100.00 with comprobante de
  retención emitted in period P and the entero declared AND integrally
  paid in P with separate registration, when P's declaration builds,
  then the $100.00 enters the agent's crédito for P; given the entero
  paid in P+1, then the credit does NOT release in P (release gate
  failed; casilla-128 post-entero route per SV-FREP-FR-091, by id)
  (FR-256).
- **AC-007:** Given a CT-161 retention on a non-domiciled supplier's
  service, when only the operation record exists without mandamiento de
  ingreso, then NO credit posts; given the mandamiento + recibo
  recorded, then the credit posts against that reference (FR-257).
- **AC-008:** Given a mixed-use motor vehicle (giro AND proven
  extra-giro use) acquired with IVA $1,950.00, when the acquisition
  posts, then $975.00 books as crédito fiscal and $975.00 as cost; given
  its fuel purchase of IVA $13.00, then $6.50 / $6.50 splits the same
  way (FR-265).
- **AC-009:** Given an acquisition of $25,000.00 (≥ 58 SMM at the
  operation date, SMM from the payroll/02 dated rows) paid IN CASH,
  when the payment registers, then the credit is BLOCKED with fail mode
  `m_cash`; given the same amount paid by bank transfer, then no 58-SMM
  block applies; given $25,000.00 paid by permuta without contrato
  escrito/escritura pública, then the block applies with fail mode
  `n_media_no_formal_doc` (FR-264).
- **AC-010:** Given a CCF received whose emitter is not registered as
  contribuyente, when ingestion validates the document, then it NEVER
  credits — hard block reason `fake_doc_1` with the criminal-reservation
  note recorded; the same one-document check fires for
  de-registered-published emitters, unauthorized correlativos, and
  not-in-name documents (FR-267).
- **AC-011:** Given a CCF whose numbering falls outside the
  AT-authorized ranges, when the line enters the purchase journal, then
  the crédito is barred (FR-266).
- **AC-012:** Given a food purchase by a software company (giro not food
  sale), when the line classifies, then the credit blocks with reason
  `a_food` and the supplier-side FACTURA obligation flag surfaces (the
  supplier must emit factura, not CCF); given the same purchase by a
  restaurant, then the gate does not fire (FR-259).
- **AC-013:** Given an air ticket of $800.00 for the owner's personal
  trip, when the expense posts, then the credit blocks (`e_air_ticket`);
  given a ticket for an employee with recorded vínculo laboral on a
  business trip strictly linked to the negocio, then the block lifts
  (FR-261).
- **AC-014:** Given a supplier invoice shifting IVA at 15% over a 13%
  legal rate, when the over-rate check runs against the dated rate row
  (SV-TAX-FR-240, by id), then only the 2-point excess blocks
  (`i_over_rate`); the legal-rate IVA remains creditable when otherwise
  eligible (FR-263).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 57-61, 65, 65-A, 70 + the Rgto. survivors cited here at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | 58-SMM sector selection (SOQ-18 kin, A10 discipline): which sector's SMM feeds the Art. 65-A l) threshold (58 × SMM) — the article names no sector, exactly like the ISR 25-SMM rule (taxation/02 OQ-002 — a DIFFERENT threshold and a different tax; do not conflate). FR-264 reads the dated rows of payroll/02 through the SV-PAY-FR-022 sector-mapping configuration and registers itself as a named consumer of that config; the default sector selection (and whether MH guidance pins one) is pending — confirm before wiring the threshold. | no | Takumi S9 + payroll/02 consumer pass | open |
| OQ-3 | CT re-anchors and printed oddities: Rgto. Art. 22's "artículo 107 de la ley" and Art. 23's "artículo 34 de la ley" are stale (D.L. 230/00) — read as CT 141 and CT 161 respectively (EVID-332 note); Art. 65-A n) prints "LOS MEDIOS UTILIZADOS EN ROMANO i)" where the operative media list is literal m) — encoded as a printed-structure note (FR-264/LB-013), but a current consolidation should confirm whether later reforms re-lettered the catalog. Also confirm the CT 141/142/142-A register surfaces this file's formal-requirement checks consume (fiscal-books wave) expose per-line registration states. | no | Takumi S9 (CT re-anchor pass) | open |
