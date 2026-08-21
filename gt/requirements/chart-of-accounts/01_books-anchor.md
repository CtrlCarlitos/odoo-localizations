# GT — Chart of accounts — CCom books/PCGA anchor: no statutory chart, the four-book registry, entry invariants, conservation

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-21 |

## 1. Purpose

This file is the anchor of the GT chart-of-accounts/commercial-legal wave: it
converts the merchant-books title of the *Código de Comercio* (Commercial
Code, CCom, Decreto 2-70) LIBRO II Título III (arts. 368-384, art. 368 as
reformed by Decreto 40-99) into requirements — starting from the load-bearing
NEGATIVE anchor: **no statutory Guatemalan plan de cuentas (chart of
accounts) exists anywhere in the CCom**; art. 368 makes *partida doble*
(double-entry bookkeeping) and *PCGA* (*principios de contabilidad
generalmente aceptados*, generally accepted accounting principles) mandatory
and leaves the chart itself to PCGA practice, so the chart is a
PCGA-governed configuration surface, never a legally-enumerated catalog. On
that base it fixes: the mandatory four-book registry (*Inventarios*;
*De primera entrada o diario*; *Mayor o centralizador*; *De Estados
Financieros*) with its Q25,000 *activo total* (total assets) omission floor
as a 1970-nominal dated row; voluntary auxiliary books as the statutory hook
by which SAT/CT books attach; the entry invariants (Spanish + *moneda
nacional* (national currency, GTQ); foreign-branch duplicate with conversion
column; chronological, no blanks/*raspaduras* (scrapings), immediate error
salvation; *documento fehaciente* (authentic/reliable supporting document)
backing); the balance/P&G signature cycle (≥1×/year, signed by *comerciante*
(merchant) + *contador* (accountant)); the single-*contabilidad* prohibition;
the mandatory-contador thresholds; the sociedades balance-publication duty
(art. 380, channel consumed from the C3 file); the corredores/descontador
auxiliary-book regimes; the conservation family (books until full
liquidation, documents ≥5 años, destruction gated on prescription) as the C1
rows the retention/destruction matrix consumes; and the instrument's dated
identity rows (vigencia 1971-01-01 — R45; consolidation horizon 30-05-2006
with the GOQ-123 verification note; the D-2946 old-code appendix guard —
R65).

It does **not** cover: the dual-track book-legalization model (RM
*autorización* vs SAT *habilitación* (authorization vs legalization/
enablement), the SAT-7121 flow, tax-law book specs, the IVA art. 29-"A"
electronic-books bridge — `02_dual-track-habilitacion.md`, cluster C2); the
RM arancel fee catalog and edicto/publication channel execution
(`../../commercial-legal` C3 `01_rm-surfaces.md` — this file only states the
art. 380 duty and hands the channel off); the comerciante/sociedades
lifecycle (C4); títulos valores, factura cambiaria and the per-instrument
prescription ladder (C5 `03_titulos-valores-prescripcion.md` — this file's
destruction gate consumes its outputs); the AML chain (C6); the consolidated
retention/destruction matrix itself
(`03_retention-destruction-matrix.md`, the GOQ-124 deliverable, which
consumes this file's C1 rows by id); and tax-side books duties, which are
owned by the taxation wave and consumed here by exact FR id
(GT-TAX-FR-230/231/232), never re-derived.

## 2. Legal Basis

Authority order (binding, per master index preamble): CCom article text =
**66_** — *Código de Comercio, Decreto del Congreso 2-70* — as consolidated
inline through **Decreto 11-2006 (DCA 30-05-2006)**; the print carries NO
post-May-2006 reforms, so **every 66_-sourced row carries the GOQ-123
live-regime verification note** (known case: art. 343's current text =
D-18-2017 art. 12 via 83_ — R64). Dated rows (EVID-502): given
1970-01-28, promulgated 1970-04-09, **vigencia 1971-01-01** (Disposiciones
Derogatorias y Modificatorias art. XI "as modified by D-43-70"; the tag date
01-07-1970 is NOT the vigencia — R45; what D-43-70 changed = GOQ-122).
Article texts are dated: art. 368 = *texto D-40-99* (the four-book list is
cited only as "art. 368, texto D-40-99" — pre-reform wording unrecoverable,
R63); art. 371 = *texto D-58-96*. Pp. 215-301 of the print are the old
D-2946 *Comercio Marítimo* appendix (arts. 827-1319, kept vigente by
Derogatoria art. I num. 1º) — every citation from those pages says "D2946
(old code) art. N", never D-2-70 (R65). Vocabulary: *autorización* = Registro
Mercantil (art. 372); *habilitación* = SAT/CT — parallel tracks, both needed
per book, never merged (R62; the word "habilitación" never appears in the
CCom — EVID-521). 1970-nominal amounts (Q25,000 omission floor; Q20,000
contador floor; Q100-Q1,000 multa) were never indexed in this print — dated
rows under D16, GOQ-126 verify-before-config (R67); art. 371's "Dirección
General de Rentas Internas" is cited as historical text and applied as SAT
(R67). Books-family LBs cite 66_ + 60_ jointly per the wave authority order
(60_ = undated illustrative SAT orientation, never law — GOQ-129); the 60_
corpus itself is loaded by `02_dual-track-habilitacion.md` (C2), which owns
the dual-track model. Quotation source: the committed evidence file
`gt/.extractions/66_CCom_libros_contabilidad.evidence.md` (EVID-501..522),
verified against the scan text layer `gt/.extractions/66_Codigo_Comercio_D2-70.pdf.txt`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CCom art. 368 (texto D-40-99): "Los comerciantes están obligados a llevar su contabilidad en forma organizada, de acuerdo con el sistema de partida doble y usando principios de contabilidad generalmente aceptados." / "Para ese efecto deberán llevar, los siguientes libros o registros: 1.- Inventarios; 2.- De primera entrada o diario; 3.- Mayor o centralizador; 4.- De Estados Financieros." / "Además podrán utilizar los otros que estimen necesarios por exigencias contables o administrativas o en virtud de otras leyes especiales." / "Los comerciantes que tengan un activo total que no exceda de veinticinco mil quetzales (Q. 25,000.00), pueden omitir en su contabilidad los libros o registros enumerados anteriormente, a excepción de aquellos que obliguen las leyes especiales." / tag: "* Reformado por el Artículo 1 del Decreto Número 40-99 del Congreso de la República de Guatemala." | Merchants must keep their accounting organized, under double entry and using generally accepted accounting principles. For that purpose they shall keep the following books or registers: 1.- Inventarios (inventories); 2.- De primera entrada o diario (daybook/journal); 3.- Mayor o centralizador (general/centralizing ledger); 4.- De Estados Financieros (financial statements). They may also use such others as they deem necessary for accounting or administrative exigency or by virtue of other special laws. Merchants whose total assets do not exceed twenty-five thousand quetzales (Q. 25,000.00) may omit the books or registers enumerated above, except those compelled by special laws. (Reformed by art. 1 of Decreto 40-99) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.82, LIBRO II Título III Capítulo I (EVID-503) |
| LB-002 | CCom art. 369: "Los libros y registros deben operarse en español y las cuentas en moneda nacional." / "Las sucursales y agencias de empresas cuya sede esté en el extranjero, pueden llevar un duplicado en el idioma y moneda que deseen, con una columna que incluya la conversión a moneda nacional, previo aviso al registrador mercantil." | Books and registers must be kept in Spanish and the accounts in the national currency (quetzal). Branches and agencies of foreign-headed enterprises may keep a duplicate in any language and currency, with a column including the conversion to national currency, on prior notice to the commercial registrar | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.82, art. 369 (EVID-504) |
| LB-003 | CCom art. 370: "La infracción a lo dispuesto en el artículo anterior, lo mismo que a lo determinado en el artículo 368 de este Código, hará incurrir al empresario en una multa no menor de cien quetzales, ni mayor de mil, en cada caso. El Registro Mercantil impondrá las multas anteriores y deberá exigir el cumplimiento de este artículo, pudiendo compeler judicialmente a la traducción, conversión y corrección en su caso, a costa del infractor." | Infringement of the preceding article (369) and of art. 368 makes the empresario (business owner) liable to a fine of not less than one hundred quetzales nor more than one thousand, in each case. The Registro Mercantil (Mercantile Registry) imposes these fines and shall enforce the article, able to judicially compel translation, conversion and correction, at the infractor's cost | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.82, art. 370 (EVID-505) |
| LB-004 | CCom art. 371 (texto D-58-96): "Los comerciantes operarán su contabilidad por sí mismos o por persona distinta designada expresa o tácitamente, en el lugar donde tenga su domicilio la empresa o en donde tenga su domicilio fiscal el contribuyente, a menos que el registrador mercantil autorice para llevarla en lugar distinto dentro del país. Sin embargo, aquellos comerciantes individuales cuyo activo total exceda de veinte mil quetzales (Q. 20,000.00), y toda sociedad mercantil, están obligados a llevar su contabilidad por medio de Contadores." / "Los libros exigidos por las leyes tributarias deberán mantenerse en el domicilio fiscal del contribuyente o en la oficina del contador del contribuyente que esté debidamente registrado en la Dirección General de Rentas Internas." / tag: "* Reformado por el Artículo 49 del Decreto Número 58-96 del Congreso de la República de Guatemala." | Merchants operate their accounting themselves or through a person expressly or tacitly designated, at the enterprise's domicile or at the taxpayer's tax domicile, unless the commercial registrar authorizes another location in-country. However, individual merchants whose total assets exceed twenty thousand quetzales (Q. 20,000.00), and every mercantile society, must keep their accounting through Contadores (accountants). Books required by tax laws must be kept at the taxpayer's tax domicile or at the office of the taxpayer's accountant duly registered with the Dirección General de Rentas Internas (pre-SAT revenue authority — applied as SAT, R67). (Reformed by art. 49 of Decreto 58-96) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.82-83, art. 371 (EVID-506) |
| LB-005 | CCom art. 372 + Disposiciones Transitorias art. IX: "Los libros de inventarios y de primera entrada o diario, el mayor o centralizador y el de estados financieros, deberán ser autorizados por el Registro Mercantil." / "La autorización de libros y de registros establecida en el artículo 372 comenzará a hacerse por el Registro Mercantil de la capital a partir de la fecha de vigencia de esta ley. En los demás registros se hará desde la fecha que el Ministerio de Economía determine." | The inventarios and daybook, the mayor/centralizador and the estados-financieros books must be authorized by the Registro Mercantil. (Transitory IX: this authorization began at the RM of the capital from the law's vigencia; at other registries from the date the Ministry of the Economy set) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83 art. 372; p.209 transitorio IX (EVID-507) |
| LB-006 | CCom art. 373: "Los comerciantes deben llevar su contabilidad con veracidad y claridad, en orden cronológico, sin espacios en blanco, interpolaciones, raspaduras, ni tachaduras. Los libros no deberán presentar señales de haber sido alterados, sustituyendo o arrancando folios o de cualquier otra manera." / "Los errores u omisiones en que se incurriere al operar en los libros o registros, se salvarán inmediatamente después de advertidos, explicando con claridad en qué consisten y extendiendo o complementando el concepto, tal como debiera haberse escrito." | Merchants must keep their accounting truthfully and clearly, in chronological order, with no blank spaces, interpolations, scrapings or strike-outs. The books must show no signs of alteration, substituting or tearing out folios or in any other way. Errors or omissions made in operating the books are saved immediately after notice, clearly explaining what they consist of and extending or completing the wording as it should have been written | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83, art. 373 (EVID-508) |
| LB-007 | CCom art. 374: "El comerciante deberá establecer, tanto al iniciar sus operaciones como por lo menos una vez al año, la situación financiera de su empresa, a través del balance general y del estado de pérdidas y ganancias que deberán ser firmados por el comerciante y el contador." | The merchant must establish, both when starting operations and at least once a year, the financial position of the enterprise through the balance general (balance sheet) and the estado de pérdidas y ganancias (profit and loss statement), which must be signed by the merchant and the accountant | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83, art. 374 (EVID-509) |
| LB-008 | CCom art. 375: "Es prohibido llevar más de una contabilidad para la misma empresa. La infracción de esta prohibición es causa de que ninguna de las contabilidades haga prueba, sin perjuicio de las demás responsabilidades a que haya lugar." | Keeping more than one accounting for the same enterprise is prohibited. Infringement causes NONE of the accountings to make proof (loss of probative value), without prejudice to other liabilities | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83, art. 375 (EVID-510) |
| LB-009 | CCom art. 376: "Los comerciantes, sus herederos o sucesores, conservarán los libros o registros del giro en general de su empresa por todo el tiempo que ésta dure y hasta la liquidación de todos sus negocios y dependencias mercantiles." | Merchants, their heirs or successors shall conserve the books or registers of the enterprise's business for the whole time it lasts and until the liquidation of all its businesses and mercantile dependencies | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83, art. 376 (EVID-511) |
| LB-010 | CCom art. 377: "El libro o registros de estados financieros, contendrá: 1º. El balance general de apertura y los ordinarios y extraordinarios que por cualquier circunstancia se practiquen. 2º. Los estados de pérdidas y ganancias o los que hagan sus veces, correspondientes al balance general de que se trate. 3º. Cualquier otro estado que a juicio del comerciante sea necesario para mostrar su situación financiera." | The financial-statements book or register shall contain: 1º. The opening balance general and the ordinary and extraordinary ones practised under any circumstance. 2º. The P&L statements (or their equivalents) corresponding to each balance general. 3º. Any other statement the merchant judges necessary to show the financial position | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.83-84, art. 377 (EVID-512) |
| LB-011 | CCom arts. 378-379: "El comerciante podrá llevar los libros o registros auxiliares que estime necesarios." / "El balance general deberá expresar con veracidad y en forma razonable, la situación financiera del comerciante y los resultados de sus operaciones hasta la fecha de que se trate." | The merchant may keep whatever auxiliary books or registers deemed necessary. The balance general must express truthfully and reasonably the merchant's financial position and the results of operations up to the date in question | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.84, arts. 378-379 (EVID-513) |
| LB-012 | CCom art. 380: "Toda sociedad mercantil y las sociedades extranjeras autorizadas para operar en la República, deben publicar su balance general en el Diario Oficial al cierre de las operaciones de cada ejercicio contable, llenando para el efecto, los requisitos que establezcan otras leyes." | Every mercantile society and the foreign societies authorized to operate in the Republic must publish their balance general in the Diario Oficial (official gazette) at the close of each accounting period's operations, meeting the requirements other laws establish. (Channel today: RM electronic portal per D-18-2017 art. 12 — R64; consumed from the C3 file) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.84, art. 380 (EVID-514) |
| LB-013 | CCom art. 381: "Toda operación contable deberá estar debidamente comprobada con documentos fehacientes, que llenen los requisitos legales y sólo se admitirá la falta de comprobación en las partidas relativas a meros ajustes, traslado de saldos, pases de un libro a otro o rectificaciones." | Every accounting operation must be duly supported by authentic documents (documentos fehacientes) meeting legal requirements; lack of support is admitted only for entries of mere adjustments, balance transfers, postings from one book to another, or rectifications | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.84, art. 381 (EVID-515) |
| LB-014 | CCom art. 382: "Todo comerciante debe conservar, en forma ordenada y organizada, durante no menos de cinco años, los documentos de su empresa, salvo lo que dispongan otras leyes especiales." | Every merchant must conserve the enterprise's documents in an orderly, organized form for not less than five years, except as provided by other special laws (the deference clause by which longer regimes extend the floor) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.84, art. 382, Capítulo II (EVID-516) |
| LB-015 | CCom arts. 383-384 + art. 1: "Los documentos que conciernan especialmente a actos o negociaciones determinadas, podrán ser inutilizados o destruidos, pasado el tiempo de prescripción de las acciones que de ellos se deriven." / "Si hubiere pendiente alguna cuestión que se refiera a ellos directa o indirectamente, deberán conservarse hasta la terminación de la misma." / "Queda al arbitrio del comerciante el sistema de archivo y custodia de valores, correspondencia y demás documentos del giro de su empresa." / "Los comerciantes en su actividad profesional, los negocios jurídicos mercantiles y cosas mercantiles, se regirán por las disposiciones de este Código y, en su defecto, por las del Derecho Civil que se aplicarán e interpretarán de conformidad con los principios que inspira el Derecho Mercantil." | Documents concerning specific acts or transactions may be destroyed once the prescription period of the actions derived from them has elapsed; if any matter concerning them directly or indirectly is pending, they must be conserved until it ends. The archive/custody system is at the merchant's discretion. Art. 1: merchants, mercantile legal business and things are governed by this Code and, in its default, by Civil law — the CCom enacts no general commercial prescription period | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.85 arts. 383-384; p.2 art. 1 (EVID-517) |
| LB-016 | CCom arts. 296-299: art. 296.2º: "Se prohibe a los corredores: … 2º. Desempeñar en el comercio el oficio de cajero, tenedor de libros o contador o dependiente, cualquiera que sea la denominación que llevare." / art. 297: "Los corredores llevarán los siguientes libros: 1º. Un libro de registro encuadernado y foliado, en el cual asentarán, día por día, por orden de fecha y bajo numeración seguida, todos los negocios ejecutados por su mediación. 2º. Un libro en el cual consignarán los nombres y domicilio de los contratantes, la materia del negocio y las condiciones en que se hubiere celebrado. Los asientos se harán en el acto de ajustarse el negocio." / "Los libros deberán ser previamente autorizados por el Registro Mercantil y se llevarán sin abreviaturas, espacios en blanco, ni alteraciones." / "Los corredores deben entregar a cada uno de los contratantes, dentro de las veinticuatro horas siguientes a la conclusión del negocio, un extracto firmado por ellos y por los interesados, del asiento que hubieren verificado en su registro. Este extracto, firmado por las partes, prueba el contrato." / art. 298: "Los registros de los corredores no prueban la verdad del contrato a que ellos se refieren, pero estando las partes de acuerdo acerca de la existencia de éste, se estará, para determinar su carácter y condiciones, a lo que conste de los mismos registros." / art. 299: "Los tribunales de oficio o a requerimiento de parte, podrán ordenar la exhibición en juicio de los libros de los corredores y exigirles los informes que creyeren convenientes." | Brokers (corredores) are barred from acting as cashier, bookkeeper, accountant or clerk. They keep two books: a bound, foliated day-register under consecutive numbering of all mediated business, and a counterparties/terms register, entered at the moment the deal is closed; both previously authorized by the Registro Mercantil, kept without abbreviations, blank spaces or alterations. Within 24 hours of concluding a deal the corredor delivers each contracting party a signed extracto (extract) of the register entry — the signed extracto proves the contract; the registers themselves do not prove the contract's truth (only its character and conditions once existence is agreed); courts may order judicial exhibition of corredores' books | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.66, arts. 296 num. 2º, 297, 298, 299 (EVID-518) |
| LB-017 | CCom arts. 731-732: "Los créditos abiertos en los libros de comerciantes, podrán ser objeto de descuento, siempre que se satisfagan los siguientes requisitos: 1º. Que los créditos sean exigibles a término o con previo aviso. 2º. Que haya prueba escrita de la existencia del crédito. 3º. Que el descuento se haga constar por escrito en que se mencionen el nombre y domicilio de los deudores, el importe de los créditos, el tipo de interés pactado y los términos y condiciones de pago. 4º. Derogado." (tag: "* Derogado el inciso 4º por el Artículo 14 del Decreto Número 62-95 del Congreso de la República de Guatemala.") / "El descontador de créditos en libros tendrá derecho de examinar los libros y correspondencia del descontatario, en cuanto se refiere a las operaciones relacionadas con los créditos descontados." | Credits opened on merchants' books may be discounted if: (1) exigible at term or on notice; (2) written proof of the credit exists; (3) the discount is recorded in writing naming debtors, amounts, interest rate and payment terms; (4) [repealed by D-62-95]. The discounter of book credits has the right to examine the discountor's books and correspondence as far as they relate to the discounted credits | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.150, arts. 731-732 (EVID-519) |
| LB-018 | CCom Disposiciones Transitorias X, XII, XIX: X: "Las disposiciones de este Código relativas a la prescripción, no se aplicarán en todos aquellos casos en que la misma ya hubiere empezado a correr conforme la ley anterior." / XII: "Los comerciantes deben ajustar su contabilidad a lo ordenado en este Código, al iniciar su primer ejercicio social siguiente a la entrada en vigencia del mismo." / XIX: "El plazo de prescripción que establece el artículo 253 de este Código, principiará a correr a partir de su entrada en vigor…" | Transitory X: prescription provisions do not apply to periods already running under the prior law. XII: merchants adjusted their accounting to the Code at the start of their first fiscal period after vigencia (the 1971 adaptation template). XIX: art. 253's prescription term runs from the Code's vigencia | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.209-211, transitorios X/XII/XIX (EVID-520) |
| LB-019 | NEGATIVE findings (full-file term sweeps of 66_): the only medium clause is art. 368 ¶3 "También podrán llevar la contabilidad por procedimientos mecanizados, en hojas sueltas, fichas o por cualquier otro sistema, siempre que permita su análisis y fiscalización."; "habilita" appears only in quiebra/seguro "rehabilitación" senses; "plan de cuentas|catalogo de cuentas|catálogo" → zero hits; the art. 368 list (raw lines 4288-4289) contains no copiador de correspondencia | No electronic/digital/computerized bookkeeping provision exists in this consolidated text (electronic books live in CT/LET/FEL instruments); "habilitación" never appears in the CCom (RM "autorización" is the CCom word); no statutory plan/catalog of accounts exists anywhere; no copiador de correspondencia (correspondence-copy book) in the current four-book list — R63 | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | full-file sweeps; art. 368 ¶3 (EVID-521) |
| LB-020 | Instrument identity + dated rows: "ARTICULO XI. * El presente Decreto entrará en vigor el primero de enero de 1971." / "* Modificado por el Artículo 1 del Decreto Del Congreso Número 43-70 el 01-07-1970." / "Dado en el Palacio del Organismo Legislativo, en la ciudad de Guatemala, a los veintiocho días del mes de enero de mil novecientos setenta." / "PALACIO NACIONAL: Guatemala, nueve de abril de mil novecientos setenta. Publíquese y cúmplase." / appendix header: "LIBRO III DEL DECRETO 2946 (ANTIGUO CODIGO DE COMERCIO), TITULOS I, II, III, IV, V, VI, VIII, VIGENTES; POR EL DECRETO NUMERO 2-70 DEL CONGRESO DE LA REPUBLICA "DISPOSICIONES DEROGATORIAS Y MODIFICATORIAS" ARTICULO I NUMERAL 1o." / derogatoria: "Se derogan: 1º. El Código de Comercio contenido en el Decreto gubernativo número 2946, con excepción de Títulos I, II, III, IV, V, VI, y VIII, del Libro III, Comercio Marítimo." / last inline reform tags: D-11-2006, DCA 30-05-2006 | D2-70 given 28-Jan-1970, promulgated (Palacio Nacional) 9-Apr-1970, vigencia 1º-Jan-1971 (transitoria XI as modified by D-43-70, tag dated 01-07-1970 — the tag date is NOT the vigencia, R45); no DCA publication date of D2-70 printed; consolidation horizon = D-11-2006 (DCA 30-05-2006); pp. 215-301 = old D-2946 Código de Comercio Libro III kept vigente as appendix (R65) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.1; p.214 date block; pp.211-212 derogatoria; p.215 appendix header (EVID-501/502) |

## 3. Functional Requirements

### 3.1 The negative anchor and the book set (art. 368 texto D-40-99; art. 372)

- **GT-COA-FR-001:** NEGATIVE ANCHOR (load-bearing guard): the system shall
  NOT ship, seed or imply any statutory Guatemalan chart of accounts — no
  *plan de cuentas* or *catálogo de cuentas* exists anywhere in the CCom
  (zero term hits, EVID-521); the chart is a PCGA-governed configuration
  surface. The GT chart seed shall be a generic PCGA/IFRS-conformant
  template carrying an informational framework note, and no code path shall
  treat any GT chart structure as legally enumerated or legally mandated in
  structure. Rejected myth (wave set): "GT has a statutory chart of
  accounts" — never implemented. (LB-001; LB-019; EVID-503/521; R63)
- **GT-COA-FR-002:** The system shall carry the mandatory legal-book set as
  a fixed four-entry dated catalog — *Inventarios*; *De primera entrada o
  diario*; *Mayor o centralizador*; *De Estados Financieros* — cited only as
  "art. 368, texto D-40-99" (the pre-reform wording is unrecoverable,
  R63), with *partida doble* (double entry) + PCGA as the mandatory
  accounting basis of every GT company. The four books instantiate the
  per-company legal-book registry (§4); no fifth mandatory CCom book
  exists. (LB-001; LB-019; EVID-503/521; R63)
- **GT-COA-FR-003:** The system shall implement the small-merchant omission
  floor as a 1970-nominal DATED row (D16: instrument = D-40-99, value
  Q25,000.00 activo total, never indexed — nominal flag set, GOQ-126
  verify-before-config kin, R67): merchants whose activo total does not
  exceed the floor may omit the four books of FR-002 in their registry,
  EXCEPT books compelled by special laws (tax-law books always survive the
  omission — e.g. the pequeño contribuyente single book owned by
  GT-TAX-FR-066, consumed by id). The floor drives a deactivation guard on
  the four-book registry only; it never disables tax-law or other
  special-law books. (LB-001; EVID-503; R67; GOQ-126 kin)
- **GT-COA-FR-004:** The system shall implement voluntary auxiliary books as
  the statutory attach surface: books additional to the four may be used
  "por exigencias contables o administrativas o en virtud de otras leyes
  especiales" (art. 368 ¶2) and the auxiliary registers of art. 378 need no
  per-book RM authorization — this is the hook by which SAT/CT book duties
  attach (tax-law book specs, the RM-autorizado/SAT-habilitado dual-track
  status model and the IVA art. 29-"A" electronic-books bridge are owned by
  `02_dual-track-habilitacion.md` (C2); tax-side duties are consumed by
  exact id: GT-TAX-FR-230 books family §3.9, GT-TAX-FR-231 books currency,
  GT-TAX-FR-066 pequeño libro — never re-derived here). The registry shall
  record each auxiliary book's legal basis (voluntary vs
  special-law-compelled). (LB-001; LB-011; EVID-503/513)
- **GT-COA-FR-005:** The system shall treat the CCom medium clause as the
  legality basis for computerized bookkeeping: contabilidad may be kept "por
  procedimientos mecanizados, en hojas sueltas, fichas o por cualquier otro
  sistema, siempre que permita su análisis y fiscalización" — the Odoo
  database as the merchant's contabilidad is legal under this clause with NO
  paper duplication required by the CCom. The CCom itself contains NO
  electronic/digital/computerized-books provision (EVID-521): electronic-
  books regimes shall be cited to the CT/LET/FEL instruments (CT 98-"A".2
  FEL anchor = GT-TAX-FR-234, consumed by id), never to the CCom.
  (LB-001; LB-019; EVID-503/521)
- **GT-COA-FR-006:** The system shall NOT model a *copiador de
  correspondencia* (correspondence-copy book) as a required or seeded book
  — it is absent from the current consolidated art. 368 list (R63);
  correspondence is covered by the documents-conservation duty of FR-027
  (art. 382), never as a book. Rejected myth (wave set), enforced as a
  registry-seed guard. (LB-001; LB-014; LB-019; EVID-503/516/521; R63)
- **GT-COA-FR-007:** The system shall track, per legal book, the CCom
  authorization state: the four books of FR-002 "deberán ser autorizados por
  el Registro Mercantil" (art. 372) — recorded as registry-side facts
  (authorized by/when, folios) on the book record, the physical act being
  external. Vocabulary guard (R62): *autorización* = the Registro Mercantil
  track (the CCom's word); *habilitación* = the SAT/CT track; the two are
  PARALLEL and never merged — no code path shall model a single
  "book legalization" status or fee. The full dual-track status model
  (RM-autorizado + SAT-habilitado per book, sanctions gates, fee rows) is
  owned by `02_dual-track-habilitacion.md` (C2), which consumes this FR.
  (LB-005; LB-019; EVID-507/521; R62)

### 3.2 Entry invariants (arts. 369, 373, 381) — account.move level

- **GT-COA-FR-008:** The system shall enforce the language/currency
  invariant on the ledger: books and registers are operated in Spanish and
  the accounts in *moneda nacional* (GTQ) — the GT company's legal books
  render in Spanish with GTQ account balances (secondary-currency amounts
  allowed as information, never as the account balance). Tax-side books
  currency discipline (CT 94.4 "al día" 2-month test) is owned by
  GT-TAX-FR-231, consumed by id. (LB-002; EVID-504)
- **GT-COA-FR-009:** The system shall support the foreign-branch duplicate:
  sucursales/agencias of foreign-headed enterprises may keep a duplicate in
  any language and currency ONLY with a column including the conversion to
  moneda nacional (GTQ), and ONLY after *aviso al registrador mercantil*
  (notice to the commercial registrar) — the duplicate surface records the
  notice date and renders the mandatory GTQ conversion column; a
  foreign-language/foreign-currency book without the conversion column is
  non-compliant. (LB-002; EVID-504)
- **GT-COA-FR-010:** The system shall enforce the entry-integrity regime on
  legal journals: contabilidad kept "con veracidad y claridad, en orden
  cronológico, sin espacios en blanco, interpolaciones, raspaduras, ni
  tachaduras", books showing no signs of alteration (folio substitution or
  tearing or otherwise) — posted legal-book entries are immutable (no
  hard deletes, no overwrites of posted entries, no backdating that breaks
  chronology), implementing the 1970 honest/dated-entries cluster as
  account.move invariants. (LB-006; EVID-508)
- **GT-COA-FR-011:** The system shall implement error correction as
  IMMEDIATE SALVATION entries: errors/omissions are "salvados
  inmediatamente después de advertidos, explicando con claridad en qué
  consisten y extendiendo o complementando el concepto, tal como debiera
  haberse escrito" — a correction posts a new dated entry that explains the
  error and restates the correct wording, linked to the original entry;
  erasure, overwrite and deletion of recorded entries are never available
  in legal books. (LB-006; EVID-508)
- **GT-COA-FR-012:** The system shall enforce *documento fehaciente*
  backing: every accounting operation shall be duly supported by documents
  meeting legal requirements (attachment/validation on the account.move);
  unbacked entries are admitted ONLY for the enumerated technical types —
  *meros ajustes* (mere adjustments), *traslado de saldos* (balance
  transfers), *pases de un libro a otro* (book-to-book postings) and
  *rectificaciones* (rectifications) — modeled as a closed entry-type
  exemption list. Tax-side backing tests (criterio/ISR, CT documents) are
  other waves' surfaces, cited not restated. (LB-013; EVID-515)

### 3.3 Contador, place and the signature cycle (arts. 371, 374, 377-379)

- **GT-COA-FR-013:** The system shall record the books-location posture per
  company: contabilidad operated at the enterprise's domicile or the
  taxpayer's *domicilio fiscal* (tax domicile), unless the registrador
  mercantil authorizes another location — in-country only (waiver scope
  recorded). (LB-004; EVID-506)
- **GT-COA-FR-014:** The system shall implement the contador-mandatory
  thresholds as 1970-nominal DATED rows (D16: instrument = D-58-96 art. 49;
  Q20,000.00 activo total for individual merchants, never indexed — nominal
  flag, GOQ-126 verify-before-config kin, R67): individual merchants with
  activo total above the floor and EVERY *sociedad mercantil* (mercantile
  society) must operate their contabilidad through Contadores — surfaced as
  a compliance-profile field (keeper identity + credential basis), never as
  a posting gate. (LB-004; EVID-506; R67; GOQ-126 kin)
- **GT-COA-FR-015:** The system shall record the placement rule for
  tax-law books: books required by tax laws are kept at the taxpayer's
  domicilio fiscal or at the office of the taxpayer's contador registered
  with the "Dirección General de Rentas Internas" — the 1996 pre-SAT
  authority named in the D-58-96 text, cited as historical text and
  APPLIED AS SAT (R67). Kin: GT-TAX-FR-231 carries the tax-corpus placement
  family (CT 21-"B".2), consumed by id — this FR owns only the CCom row.
  (LB-004; EVID-506; R67)
- **GT-COA-FR-016:** The system shall implement the balance/P&G cycle:
  financial position established at the start of operations and AT LEAST
  once a year via *balance general* + *estado de pérdidas y ganancias*,
  EACH statement DUAL-SIGNED by the comerciante and the contador — modeled
  as a dated financial-statement record per cycle (opening + annual +
  extraordinary closes) carrying both sign-off slots and the responsible
  parties (contador presence per FR-014). (LB-007; EVID-509)
- **GT-COA-FR-017:** The system shall implement the estados-financieros
  book contents (art. 377): the financial-statements register holds the
  *balance general de apertura* (opening balance), every ordinary and
  extraordinary balance practised under any circumstance, each with its
  MATCHING P&L statement (or equivalent), plus any further statement the
  merchant judges necessary — every statement record carries its balance
  counterpart link. (LB-010; EVID-512)
- **GT-COA-FR-018:** The system shall carry the substantive truthfulness
  standard on statement generation: the balance general must express "con
  veracidad y en forma razonable" the financial position and the results of
  operations — the balance-standard tie-in to art. 368's PCGA mandate
  (statement-quality flag + PCGA framework note on the FS record; no
  separate computation derived here). (LB-011; EVID-513)
- **GT-COA-FR-019:** The system shall enforce the single-contabilidad
  prohibition: ONE legal contabilidad per empresa — a second, parallel
  official book set for the same empresa is prohibited; configuring one
  shall be blocked/flagged, because infringement causes NONE of the
  contabilidades to make proof (*fe probatoria*, probative force) plus
  other liabilities. Off-books management views that do not constitute a
  second contabilidad are out of scope and must never be modeled as legal
  books. (LB-008; EVID-510)

### 3.4 Sanction and publication (arts. 370, 380)

- **GT-COA-FR-020:** The system shall carry the CCom books-sanction band as
  1970-nominal DATED rows (D16: multa no menor de Q100 ni mayor de Q1,000,
  per case, never indexed — nominal flag, GOQ-126 kin, R67), imposed by the
  REGISTRO MERCANTIL for infringement of arts. 368/369, with remediation =
  compelled *traducción, conversión y corrección* (translation, conversion,
  correction) at the infractor's cost. This is the RM sanction track —
  SEPARATE from the SAT/CT track (CT 94.4 books fines and 85.4 cierre
  seeds = GT-TAX-FR-214/216, consumed by id); the two tracks are never
  merged (R62). Sanction values are recorded exposure, not computed
  workflows. (LB-003; EVID-505; R62/R67; GOQ-126 kin)
- **GT-COA-FR-021:** The system shall record the sociedades
  balance-publication duty: every *sociedad mercantil* and every foreign
  society authorized to operate in Guatemala publishes its balance general
  at the close of each *ejercicio contable* (accounting period), subject to
  other laws' requirements. CHANNEL GUARD (R64): the 66_ print (consolidated
  to 30-05-2006) names the Diario Oficial, but current art. 343 mechanics =
  D-18-2017 art. 12 (all CCom-mandated publications via the RM electronic
  portal) — publication-channel execution, fee classes and edicto payload
  are owned by `commercial-legal/01_rm-surfaces.md` (C3), which consumes
  this duty via GT-CML-FR-001; this FR owns only the per-ejercicio
  publication obligation
  flag on the sociedad's FS cycle records (individual merchants: no
  publication duty). (LB-012; EVID-514/522; R64; GOQ-123)

### 3.5 Auxiliary-commerce book regimes (arts. 296-299, 731-732) — bounded, minor

- **GT-COA-FR-022:** The system shall provide the corredor book profile:
  TWO RM-authorized books — a *libro de registro encuadernado y foliado*
  (bound, foliated register) of all mediated business entered day-by-day,
  in date order under consecutive numbering, and a counterparties register
  (names, domicile, subject-matter, conditions) with entries made IN THE
  ACT of closing the deal — both kept without abbreviations, blank spaces
  or alterations. Stricter than the merchant regime: bound and foliated (no
  hojas sueltas for corredores). (LB-016; EVID-518)
- **GT-COA-FR-023:** The system shall model the corredores evidentiary
  rules: a signed *extracto* delivered to each contracting party within 24
  hours of concluding the business PROVES the contract; the corredores' own
  registers do NOT prove the contract's truth (only its character and
  conditions once existence is agreed, art. 298); and per art. 299, courts
  (de oficio or at party request) may order the exhibition in judgment of
  the corredores' books and require their reports. Surfaces: extracto
  record (parties, timestamp, signature slots) + exhibition log.
  (LB-016; EVID-518)
- **GT-COA-FR-024:** The system shall enforce the corredor
  incompatibility guard: a corredor cannot simultaneously hold the office
  of cajero, tenedor de libros, contador or dependiente of a merchant
  (whatever its denomination) — a role-conflict check between the partner's
  corredor profile and any bookkeeping-responsible role (FR-014 keeper
  fields). (LB-016; EVID-518)
- **GT-COA-FR-025:** The system shall record the descontador's contractual
  examination right as a third-party access row: where book credits are
  discounted (exigible at term/on notice + written proof + written discount
  deed naming debtors, amounts, interest and payment terms — inciso 4º
  repealed by D-62-95), the descontador may examine the descontatario's
  books AND correspondence, limited to the operations related to the
  discounted credits. Recorded as scoped, read-only, purpose-limited access
  metadata on the books registry — never a general access grant.
  (LB-017; EVID-519)

### 3.6 Conservation, documents, destruction (arts. 376, 382-384) — the C1 rows the matrix consumes

- **GT-COA-FR-026:** The system shall implement books conservation as a
  liquidation-anchored duty (NO year count): merchants, their heirs and
  successors conserve the books/registers of the enterprise's giro for the
  whole life of the enterprise AND until the liquidation of all its
  businesses and mercantile dependencies — the books registry carries a
  conservation state that ends only at full-liquidation close (succession
  of custody to heirs/successors recorded); no destruction of books derives
  from the CCom alone. This row feeds the retention/destruction matrix
  (`03_retention-destruction-matrix.md`, the GOQ-124 deliverable) by id.
  (LB-009; EVID-511)
- **GT-COA-FR-027:** The system shall implement the documents floor:
  enterprise documents conserved in an orderly, organized form for NOT
  LESS than five years, "salvo lo que dispongan otras leyes especiales" —
  the explicit deference clause by which longer special-law regimes extend
  the floor (the tax corpus' prescription-anchored conservation =
  GT-TAX-FR-232, consumed by id as the practical floor; the consolidated
  max-per-object rule is owned by the matrix file — never re-derived here).
  Correspondence is this documents duty, not a book (FR-006).
  (LB-014; EVID-516)
- **GT-COA-FR-028:** The system shall implement the destruction gate:
  documents concerning specific acts/transactions may be destroyed only
  AFTER the prescription of the actions derived from them elapses, and
  NEVER while any matter concerning them directly or indirectly is pending.
  The CCom itself enacts NO general prescription period (art. 1 defers to
  Civil law) — per-instrument prescription keys are consumed from
  `commercial-legal/03_titulos-valores-prescripcion.md` (C5) and the
  operative gate computation is owned by the matrix file (GOQ-124
  deliverable); this FR owns the CCom gate predicate (prescribed AND
  no-pending-matter). (LB-015; EVID-517)
- **GT-COA-FR-029:** The system shall record archive-medium freedom: the
  system of archive and custody of valores, correspondence and other giro
  documents is at the merchant's discretion (art. 384) — no CCom-mandated
  archive medium or format exists for documents; electronic archives are
  legal under this freedom plus FR-005's analysis/fiscalización condition
  (specific electronic-regime conservation duties, e.g. DTE archives,
  belong to their owning waves). (LB-015; EVID-517)

### 3.7 Instrument identity and citation guards (R45/R64/R65, transitorios)

- **GT-COA-FR-030:** The system shall carry the CCom instrument identity as
  D16 dated rows: given 1970-01-28; promulgated 1970-04-09; vigencia
  **1971-01-01** (transitoria XI as modified by D-43-70 — the tag date
  01-07-1970 is NOT the vigencia and shall never be modeled as such,
  R45); no DCA publication date printed; consolidation horizon
  **D-11-2006 (DCA 30-05-2006)** — the last instrument named in the print.
  What D-43-70 changed is open → GOQ-122 (OQ-002). (LB-020; EVID-501/502;
  R45; GOQ-122)
- **GT-COA-FR-031:** The system shall attach the live-regime verification
  note (GOQ-123) to every 66_-derived configuration row: the print is
  consolidated to 30-05-2006 only; post-May-2006 reforms are absent (known
  case: art. 343 = D-18-2017 art. 12 via 83_ — R64), so every dated row
  from this instrument carries provenance + verification flag, and
  supersession against the current corpus is re-checked before any row is
  used as operative config. (LB-020; EVID-502/522; R64; GOQ-123)
- **GT-COA-FR-032:** The system shall enforce the D-2946 appendix citation
  guard (R65): pp. 215-301 of the print are the old Decreto 2946 Código de
  Comercio Libro III (Comercio Marítimo, arts. 827-1319), kept vigente by
  Derogatoria art. I num. 1º with numbering colliding with D2-70's own
  800s-1000s articles — any requirement sourced from those pages shall be
  cited as "D2946 (old code) art. N" and NEVER as D-2-70; the corpus
  import layer tags article numbers ≥827 with the dual-ancestry flag.
  (LB-020; EVID-502/517; R65)
- **GT-COA-FR-033:** The system shall record the books-relevant
  transitional pattern as provenance rows (no current-operative
  computation): prescription changes are non-retroactive for periods
  already running (transitorio X); merchants adjusted their contabilidad
  to the Code at the start of their FIRST ejercicio after vigencia
  (transitorio XII — the 1971 adaptation template mirrored by later
  electronic-books migrations, owned by C2); art. 253's prescription term
  runs from vigencia (transitorio XIX). (LB-018; EVID-520)

## 4. Data Model

Layer semantics: bookkeeping invariants and registry surfaces live in the
Odoo client; the book set, thresholds, sanction band and conservation rules
are dated config rows shared across the architecture (see §5). The system
records compliance facts (authorization, signatures, custody) — it never
emulates the Registro Mercantil, SAT or the courts. No printed data table in
this file warrants a CSV sidecar (small config sets; the four-book catalog
and dated values are seed rows).

**Legal-book registry (l10n_gt_commerce.book):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.book | kind | select | inventarios · diario · mayor_centralizador · estados_financieros · auxiliar · corredor_registro · corredor_contratantes | FR-002, FR-004, FR-022 |
| l10n_gt_commerce.book | mandatory | boolean | true for the four; false for auxiliaries | FR-002, FR-004 |
| l10n_gt_commerce.book | legal_basis | select | cc_art368_d40_99 · special_law (auxiliaries attached by other laws — spec owned by C2) · cc_art297 (corredores) | FR-004, FR-022 |
| l10n_gt_commerce.book | rm_authorization_state | select + date + folios | the RM *autorización* facts (registry-side); the dual-track status model = C2 by id | FR-007 |
| l10n_gt_commerce.book | conservation_state | select | active · liquidation_hold (until full liquidation, FR-026) — successor-custody note field (heirs/successors) | FR-026 |
| l10n_gt_commerce.book | location_basis | select | empresa_domicilio · domicilio_fiscal · registrar_waiver_in_country (tax-law books: domicilio_fiscal · contador_office_sat_registered) | FR-013, FR-015 |
| l10n_gt_commerce.book | third_party_access_rows | one2many | descontador examination grants (scoped read, discounted-credits-only) + judicial exhibition log (corredores) | FR-023, FR-025 |

**Dated config rows (l10n_gt_commerce.dated_value — D16: instrument + article + valid_from/valid_to + nominal flag + verification note):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.dated_value | key | char | cc_omission_floor (Q25,000.00 activo total) · cc_contador_floor (Q20,000.00 activo total) · cc_multa_band (Q100–Q1,000 per case) — all instrument=D2-70 (arts. 368 texto D-40-99 / 371 texto D-58-96 / 370), 1970-nominal, never indexed | FR-003, FR-014, FR-020 |
| l10n_gt_commerce.dated_value | nominal_1970_flag · goq126_flag | boolean | true for all three keys (R67; GOQ-126 verify-before-config kin) | FR-003, FR-014, FR-020 |
| l10n_gt_commerce.dated_value | instrument_identity | json | D2-70: given 1970-01-28, promulgated 1970-04-09, vigencia 1971-01-01 (transitoria XI as modified by D-43-70 — tag 01-07-1970 is NOT the vigencia, R45); consolidation horizon D-11-2006 DCA 30-05-2006; no DCA date printed (GOQ-122) | FR-030 |
| l10n_gt_commerce.dated_value | goq123_verification_flag | boolean | true on every 66_-derived row (post-May-2006 reform watch; art. 343 = D-18-2017 known case — R64) | FR-031 |
| l10n_gt_commerce.dated_value | d2946_ancestry_flag | boolean | true for article numbers ≥827 sourced from pp. 215-301 ("D2946 (old code) art. N") | FR-032 |

**Entry invariants + FS cycle (on account.move / FS records):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move | gt_legal_book_discipline | computed/invariant | chronological, no blanks/alterations; posted = immutable; Spanish + GTQ rendering | FR-008, FR-010 |
| account.move | correction_link · salvation_explanation | m2o + text | immediate-salvation entries: new dated entry explaining the error + restating the concept; linked to the original, never overwriting | FR-011 |
| account.move | backing_exempt_type | select | none (documento fehaciente required) · mero_ajuste · traslado_saldos · pase_libro · rectificacion (closed exemption list) | FR-012 |
| account.move (foreign-branch duplicate surface) | gtq_conversion_column · rm_notice_date | monetary + date | foreign duplicate legal only with the GTQ conversion column + prior aviso al registrador | FR-009 |
| l10n_gt_commerce.fs_statement | kind · balance_link · signed_comerciante/signed_contador + dates | select + m2o + signature slots | apertura · ordinario · extraordinario; each balance carries its matching P&L; dual signature at start + ≥1×/year; sociedad rows carry the publication-obligation flag (channel = C3 by id) | FR-016, FR-017, FR-021 |
| res.company | gt_contabilidad_single_guard · keeper_profile | boolean + select | one legal contabilidad per empresa (second set flagged/blocked — fe probatoria loss) · self · designated · contador_mandatory (>Q20,000 individual / all sociedades, dated row) | FR-014, FR-019 |
| res.partner | corredor_profile · incompatibility_guard | boolean + check | corredor roles: two-book regime, 24h signed extracto; barred from cajero/tenedor de libros/contador/dependiente roles | FR-022, FR-023, FR-024 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2): `odoo` = bookkeeping
invariants, registry and signature-cycle surfaces in the LGPL client;
`shared` = dated contract items both sides must honor identically (book set,
thresholds, sanction band, conservation rules, instrument identity). Per the
wave defaults this file introduces NO `saas` rows: none of its FRs touch a
portal/emission state machine — the only hand-off is FR-021's publication
duty, whose RM-portal channel (payload generation = odoo, portal ingestion =
saas) is owned by `commercial-legal/01_rm-surfaces.md` (C3) and is consumed
there, not implemented here. Model names are stable across Odoo 17/18/19/20;
no version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | account.account / chart template | PCGA framework note | No statutory-chart artifact seeded; generic PCGA/IFRS-conformant template; negative guard rides every chart-surface test |
| FR-002 | shared | l10n_gt_commerce.book seed | kind, mandatory | The four-book catalog as dated config (art. 368 texto D-40-99); consumed identically by both sides |
| FR-003 | shared | l10n_gt_commerce.dated_value | cc_omission_floor | Q25,000 1970-nominal, GOQ-126 flag; deactivation guard scoped to the four books only; special-law books survive |
| FR-004 | odoo | l10n_gt_commerce.book | legal_basis | Auxiliaries attach surface; dual-track/tax-book specs = C2 by id; GT-TAX-FR-230/231/066 consumed |
| FR-005 | odoo | res.company | medium-basis note | Computerized bookkeeping legal via art. 368 ¶3; electronic-books citation guard (CT 98-"A".2 = GT-TAX-FR-234, by id) |
| FR-006 | odoo | l10n_gt_commerce.book seed guard | — | No copiador seeded (R63); registry seed test |
| FR-007 | odoo | l10n_gt_commerce.book | rm_authorization_state | RM-track facts only; vocabulary guard R62; dual-track model = C2 |
| FR-008 | odoo | account.move / res.company | language/currency invariant | Spanish + GTQ balances; CT 94.4 test = GT-TAX-FR-231 by id |
| FR-009 | odoo | account.move (report surface) | gtq_conversion_column, rm_notice_date | Foreign-branch duplicate profile |
| FR-010 | odoo | account.move | posted-entry immutability | Chronological, no blanks/alterations; 17-20 native immutability + guard |
| FR-011 | odoo | account.move | correction_link, salvation_explanation | Immediate-salvation correction entries; never deletion/overwrite |
| FR-012 | odoo | account.move | backing_exempt_type | Closed exemption list (ajustes/traslados/pases/rectificaciones) |
| FR-013 | odoo | res.company / book registry | location_basis | Enterprise domicile / domicilio fiscal / registrar in-country waiver |
| FR-014 | shared | l10n_gt_commerce.dated_value + res.company | cc_contador_floor, keeper_profile | Q20,000 1970-nominal (texto D-58-96), GOQ-126 flag; all sociedades = contador mandatory |
| FR-015 | odoo | book registry | tax-books placement | DGRI historical text applied as SAT (R67); CT 21-"B".2 kin = GT-TAX-FR-231 by id |
| FR-016 | odoo | l10n_gt_commerce.fs_statement | signature slots | Start + ≥1×/year dual signature (comerciante + contador) |
| FR-017 | odoo | l10n_gt_commerce.fs_statement | kind, balance_link | Art. 377 contents: apertura + ordinarios/extraordinarios + matching P&L |
| FR-018 | odoo | l10n_gt_commerce.fs_statement | veracity standard flag | "veracidad y forma razonable" + PCGA tie-in; no computation |
| FR-019 | odoo | res.company | single-contabilidad guard | Second legal book set blocked/flagged (fe probatoria loss) |
| FR-020 | shared | l10n_gt_commerce.dated_value | cc_multa_band | Q100–Q1,000 per case, RM-imposed, 1970-nominal (GOQ-126 kin); RM track ≠ CT track (GT-TAX-FR-214 by id); recorded exposure |
| FR-021 | shared | l10n_gt_commerce.fs_statement + dated config | publication-obligation flag | Per-ejercicio balance-publication duty (sociedades + authorized foreign societies); channel = C3 (RM portal via D-18-2017, R64); GOQ-123 note |
| FR-022 | odoo | l10n_gt_commerce.book | corredor kinds | Two RM-authorized bound/foliated registers; entry-at-act |
| FR-023 | odoo | corredor extracto record + exhibition log | — | 24h signed extracto proves the contract; registers' limited proof; judicial exhibición |
| FR-024 | odoo | res.partner | incompatibility guard | Corredor vs bookkeeping-role conflict check |
| FR-025 | odoo | l10n_gt_commerce.book | third_party_access_rows | Descontador scoped examination grant (discounted operations only) |
| FR-026 | shared | l10n_gt_commerce.book | conservation_state | Liquidation-anchored conservation; heirs/successors custody; feeds the matrix (GOQ-124 deliverable) by id |
| FR-027 | shared | retention config | documents floor row | ≥5 años + deference clause; practical floor = GT-TAX-FR-232 by id; matrix owns max-per-object |
| FR-028 | shared | retention config | destruction-gate predicate | Prescribed AND no-pending-matter; prescription keys = C5 file; gate computation = matrix file |
| FR-029 | shared | retention config | archive-medium freedom | No CCom-mandated document medium; electronic archives legal |
| FR-030 | shared | l10n_gt_commerce.dated_value | instrument_identity | Vigencia 1971-01-01 (R45 — never 01-07-1970); consolidation horizon 2006-05-30; GOQ-122 open |
| FR-031 | shared | all 66_-derived rows | goq123_verification_flag | Live-regime verification note rides every row (R64) |
| FR-032 | shared | corpus import layer | d2946_ancestry_flag | "D2946 (old code) art. N" citations only (R65) |
| FR-033 | shared | provenance rows | transitorios X/XII/XIX | Transition pattern, no operative computation |

Version-regime notes (D12/D15/D16): the CCom rows are a dated-instrument
regime — every 66_-sourced value resolves as-of the domain anchor date and
carries instrument provenance (D2-70 as consolidated to 30-05-2006); the
1970-nominal amounts (Q25,000 / Q20,000 / Q100–Q1,000) store as dated rows
with the nominal flag and GOQ-126 verify-before-config kin (R67 — never
treated as current market thresholds); the GOQ-123 verification flag guards
post-consolidation reform drift (known: art. 343 = D-18-2017 — R64). No
hard emission/posting gates exist in this file beyond the entry invariants
(FR-010..012) and the single-contabilidad guard (FR-019); sanction values
are recorded exposure (FR-020), never computed fines.

## 6. Acceptance Criteria

- **AC-001:** Given any GT company chart configuration, when inspected, then
  no statutory-chart flag, legally-enumerated account catalog or
  "official GT COA" artifact exists — the chart carries only the
  PCGA-framework note, and the rejected myth "GT has a statutory chart of
  accounts" is enforced as a guard. (FR-001)
- **AC-002:** Given a seeded GT legal-book registry, when listed, then it
  holds exactly the four mandatory books with their Spanish names
  (Inventarios; De primera entrada o diario; Mayor o centralizador; De
  Estados Financieros) cited as "art. 368, texto D-40-99" — and NO copiador
  de correspondencia row is seeded. (FR-002, FR-006)
- **AC-003:** Given an individual merchant with activo total Q25,000.00 or
  less (dated row, nominal flag set), when the omission guard runs, then the
  four CCom books may be deactivated — while every special-law book (e.g.
  the pequeño contribuyente book of GT-TAX-FR-066) remains active.
  (FR-003, FR-004)
- **AC-004:** Given a legal journal rendered for a GT company, when entries
  are displayed, then they are in Spanish with GTQ account balances; and
  given a foreign-parent branch configuring an English/USD duplicate, when
  the duplicate renders, then it carries the GTQ conversion column and the
  recorded aviso date, or the profile is rejected as non-compliant.
  (FR-008, FR-009)
- **AC-005:** Given a posted legal-book entry containing an error, when the
  correction is recorded, then it posts as a new dated salvation entry
  explaining the error and restating the concept, linked to the original —
  the original shows no blank, interpolation, scraping, strike-out or
  overwrite. (FR-010, FR-011)
- **AC-006:** Given an accounting entry with no supporting document, when
  posting is attempted, then it is blocked unless its type is one of the
  four exempt kinds (mere adjustment, balance transfer, book-to-book
  posting, rectification). (FR-012)
- **AC-007:** Given a GT company's fiscal-year close (and its opening at
  start of operations), when the FS cycle is generated, then the balance
  general and estado de pérdidas y ganancias each carry both the
  comerciante and contador signature slots (contador presence enforced per
  the dated Q20,000/sociedades profile), and each balance links its
  matching P&L statement. (FR-014, FR-016, FR-017)
- **AC-008:** Given a company with an active legal-book set, when a second
  official book set for the same empresa is configured, then it is
  blocked/flagged with the fe-probatoria warning (none of the
  contabilidades makes proof). (FR-019)
- **AC-009:** Given a sociedad mercantil's ejercicio close, when the FS
  cycle record is saved, then it carries the balance-publication obligation
  flag handed to the C3 channel (RM electronic portal per D-18-2017 —
  R64); an individual merchant's record carries no such flag. (FR-021)
- **AC-010:** Given books of a merchant whose enterprise liquidation has not
  completed, and giro documents less than five years old whose underlying
  actions have not prescribed (or with a pending matter), when destruction
  is attempted, then it is refused by the conservation state and the
  destruction-gate predicate (prescribed AND no-pending-matter not met).
  (FR-026, FR-027, FR-028)
- **AC-011:** Given a corredor partner, when its book profile is set up,
  then the two bound/foliated RM-authorized registers are configured with
  the entry-at-act rule, the 24h signed-extracto duty is exposed, and the
  same partner cannot hold a merchant's contador/tenedor-de-libros role.
  (FR-022, FR-023, FR-024)
- **AC-012:** Given any dated row derived from 66_, when inspected, then it
  carries instrument provenance (D2-70 as consolidated to 30-05-2006), the
  GOQ-123 verification flag, and — for the vigencia row — the value
  1971-01-01 (never the 01-07-1970 tag date, R45); and any row sourced
  from pp. 215-301 prints "D2946 (old code) art. N", never D-2-70.
  (FR-030, FR-031, FR-032)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
this file owns GOQ-122 and GOQ-123 for the C1 rows (with GOQ-05 as headline
kin and GOQ-126 as threshold kin). GOQ-124 (retention/destruction matrix) is
the Task 7 deliverable that consumes FR-026/027/028 by id — not an open
question of this file.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-05 (=OQ16, kin): "Does a numbered Reglamento del Código de Comercio exist? (No candidate found in any sweep.)" No candidate instrument found in any corpus sweep — the books rules live in the Code itself plus the RM arancel (73_, C3 file); if a numbered reglamento surfaces, FR-004/FR-007 registry mechanics re-verify against it. Affects the C1/C2 registry surfaces (minor). | no | GT synthesis wave S-GT5 → W6 partner ask | open |
| OQ-002 | GOQ-122 (owned): "D2-70 dated-row completion: what D-43-70 changed in transitoria XI; no DCA publication date printed (last printed date = promulgation 9-abr-1970)." The vigencia row (FR-030) stores 1971-01-01 "as modified by D-43-70" (R45); the content of the D-43-70 modification is not derivable from the corpus and stays open. | no | GT synthesis wave S-GT5 (acquisition queue) | open |
| OQ-003 | GOQ-123 (owned): "CCom post-May-2006 reform watch: consolidation horizon D-11-2006; later reforms absent (known: art. 343 = D-18-2017) — verification note rides every 66_ citation." FR-031 carries the flag on every 66_-derived row; any post-2006 reform that touches arts. 368-384 (e.g. an electronic-books reform of the books title) re-opens the affected FRs. | no | GT synthesis wave S-GT5 → W6 partner ask | open |
| OQ-004 | GOQ-126 (kin): "Matrícula Q2,000 / S.A. Q5,000 1970-nominal thresholds: whether later instruments or RTU practice supersede — verify before config." The register's C4 values (matrícula Q2,000 / S.A. Q5,000) belong to the C4 file; its rule binds THIS file's C1 1970-nominal rows the same way: the Q25,000 omission floor (FR-003), Q20,000 contador floor (FR-014) and Q100–Q1,000 multa band (FR-020) are stored as dated rows with the goq126 flag and are verified against modern instruments/RTU before configuration. | no | GT synthesis wave S-GT5 (verify-before-config gate) | open |
