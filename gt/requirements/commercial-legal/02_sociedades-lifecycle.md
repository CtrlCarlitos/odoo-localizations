# GT — Commercial-legal — Sociedades lifecycle: comerciante calificación, matrícula, the five society forms, capital/governance, disolución/liquidación/fusión, extranjeras, auxiliares + CC-reform AML hooks (C4)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-21 |

## 1. Purpose

This file is the FOURTH of the S-GT5 chart-of-accounts/commercial-legal
wave and owns cluster **C4**, the comerciante + sociedades mercantiles +
Registro Mercantil **lifecycle** domain. It converts into requirements:
the *comerciante* (merchant) calificación test — *en nombre propio y con
fines de lucro* (in one's own name and for profit) over four activity
classes, the art. 9 negative list, art. 6 capacity, and the
entity-type-driven rule that EVERY mercantile-form society is a
comerciante whatever its object; the *matrícula* (registry enrollment)
engine — the registration universe (individual comerciantes ≥ Q2,000
1970-nominal capital, ALL sociedades, empresas/establecimientos,
auxiliares), the 1-month windows, the free displayed *patente de
comercio* (commerce license), the registrador fine Q25–Q1,000 and the
gremial-chamber lockout; the closed list of exactly FIVE society forms
with their liability defaults, mandatory name suffixes and the
suffix-omission liability flip; the constitution solemnities
(*escritura pública* + RM inscription = legal personality); capital and
governance profiles (reserva legal 5%→15%; S.A. autorizado/suscrito/
pagado tiers with the Q5,000 1970-nominal minimum and notary-certified
bank deposit; acciones as títulos de crédito and the Registro de
Acciones Nominativas; asamblea cadence/quorum/convocation;
administración terms revocable ad nutum; capital ± with the 30-day
creditor opposition); foreign societies (US$50,000 fianza, RM sole
authorizer); irregulares/de hecho; disolución → "En liquidación" →
liquidation waterfall → USAC escheat → registry close-out;
fusión/transformación; auxiliares de comercio (bounded — licensing
reglamentos absent); and the **AML Código-de-Comercio reform hooks** of
D-15-2026 (reformed CC arts. 45/125: shareholder registry, RM notices
≤10 días hábiles, the 5–50 SMM fine, the RM confidential database,
art. 121 administrator sanction with RM-operation block) as dated
cutover rows operative 17-sep-2026.

It does **not** cover: the RM publication channel, fee catalog and
provisional→definitiva state machine
(`01_rm-surfaces.md` GT-CML-FR-001..025 — consumed by exact id;
lifecycle events here PUBLISH THROUGH that channel); the books/PCGA
anchor and dual-track legalization model
(`../chart-of-accounts/01_books-anchor.md` GT-COA-FR-001..033 and
`02_dual-track-habilitation.md` GT-COA-FR-034..060 — the contador duty
GT-COA-FR-014 and the art. 380 balance-publication duty GT-COA-FR-021
are consumed by id); títulos valores and the prescription ladder (C5,
`03_titulos-valores-prescripcion.md` — forward ref, file + cluster
only); the AML machinery itself (C6, `04_aml-compliance.md` — forward
ref, file + cluster only; this file owns only the CC-side duty rows);
the consolidated retention/destruction matrix
(`../chart-of-accounts/03_retention-destruction-matrix.md`, the GOQ-124
deliverable, Task 7 — forward ref, file + cluster only; the USAC escheat
row feeds it by pointer); and tax-side sanction machinery (GT-TAX-FR-
216/217 consumed by exact id via `01_rm-surfaces.md` GT-CML-FR-025).

## 2. Legal Basis

Authority order (binding, per master index preamble): CCom article text
= **66_** — *Código de Comercio, Decreto del Congreso 2-70* — as
consolidated inline through **Decreto 11-2006 (DCA 30-05-2006)**; the
print carries NO post-May-2006 reforms, so **every 66_-sourced row in
this file carries the GOQ-123 live-regime verification note** (kin —
owned by `01_books-anchor.md` GT-COA-FR-031), load-bearing here through
**R64**: every CCom-mandated publication (convocation, disolución,
final balance, fusión) is executed on the RM electronic portal per
current art. 343 = D-18-2017 art. 12 (channel owned by
`01_rm-surfaces.md` GT-CML-FR-001 — the 66_ print's newspaper/Diario
Oficial texts below are cited "as printed, pre-D18-2017"). Instrument
dated identity (given 1970-01-28, promulgated 1970-04-09, **vigencia
1971-01-01** as modified by D-43-70, R45; D-2946 old-code appendix
guard, R65) is owned by `01_books-anchor.md` GT-COA-FR-030..032 and
consumed by id, never re-derived. **R67**: every Q-amount in this file
(Q2,000 matrícula threshold; Q5,000 S.A. minimum, printed "Q5, 000.00"
[sic]; Q25–Q1,000 registrador multa; Q25–Q500 art. 93 multa) is a
1970-nominal figure never indexed in this print — dated rows under D16
with the GOQ-126 verify-before-config flag. The AML CC-reform rows cite
**77_** (D-15-2026) as dated cutover rows operative **17-sep-2026**
(R60 — never 17-jun-2026; pre-cutover facts resolve against the 66_
printed text). Quotation sources: the committed evidence files
`gt/.extractions/66_CCom_sociedades_comercial.evidence.md` (EV05b;
EVID-536..569) and `gt/.extractions/75-77_AML.evidence.md` (EV05d;
EVID-634), verified against the scan text layers
`gt/.extractions/66_Codigo_Comercio_D2-70.pdf.txt` and
`gt/.extractions/77_AML_LeyIntegral_D15-2026.pdf.txt` (77_ text layer
recovered by forced OCR — quotes are taken from the evidence file, the
verified surface).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CCom arts. 2 y 3: art. 2: "Son comerciantes quienes ejercen en nombre propio y con fines de lucro, cualesquiera actividades que se refieren a lo siguiente: 1º La industria dirigida a la producción o transformación de bienes y a la prestación de servicios. 2º La intermediación en la circulación de bienes y a la prestación de servicios. 3º La Banca, seguros y fianzas. 4º Las auxiliares de las anteriores." / art. 3: "Las sociedades organizadas bajo forma mercantil tienen la calidad de comerciantes, cualquiera que sea su objeto." | Merchants are those who conduct in their own name and for profit any of the following activities: 1º industry directed at production or transformation of goods and provision of services; 2º intermediation in the circulation of goods and provision of services; 3º banking, insurance and fianzas (guaranty bonds); 4º auxiliaries of the foregoing. Societies organized in mercantile form have the quality of merchants, whatever their object | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.2, arts. 2-3 (EVID-537) |
| LB-002 | CCom arts. 6 y 9: art. 6: "Tienen capacidad para ser comerciantes las personas individuales y jurídicas que, conforme al Código Civil, son hábiles para contratar y obligarse." / art. 9: "No son comerciantes: 1º Los que ejercen una profesión liberal. 2º Los que desarrollen actividades agrícolas, pecuarias o similares en cuanto se refiere al cultivo y transformación de los productos de su propia empresa. 3º Los artesanos que sólo trabajen por encargo o que no tengan almacén o tienda para el expendio de sus productos." | Individual and juridical persons capable, under the Civil Code, of contracting and binding themselves have capacity to be merchants. NOT merchants: 1º liberal professionals; 2º those doing agricultural, livestock or similar activity as regards cultivation and transformation of their own enterprise's products; 3º artisans who work only on order or have no almacén/tienda (store/shop) for sale of their products | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.3, arts. 6, 9 (EVID-537) |
| LB-003 | CCom art. 334: "Es obligatoria la inscripción en el Registro Mercantil jurisdiccional: 1º. De los comerciantes individuales que tengan un capital de dos mil quetzales o más. 2º. De todas las sociedades mercantiles. 3º. De empresas y establecimientos mercantiles comprendidos dentro de estos extremos. 4º. De los hechos y relaciones jurídicas que especifiquen las leyes. 5º. De los auxiliares de comercio. La inscripción de comerciantes individuales, auxiliares de comercio y de las empresas y establecimientos mercantiles, deberá solicitarse dentro de un mes de haberse constituido como tales o de haberse abierto la empresa o el establecimiento. El de las sociedades, dentro del mes siguiente al otorgamiento de la escritura de constitución." | Enrollment in the jurisdictional Mercantile Registry is obligatory for: 1º individual merchants with capital of two thousand quetzales or more; 2º ALL mercantile societies; 3º commercial enterprises and establishments within these extremes; 4º facts and legal relations specified by law; 5º auxiliaries of commerce. Individual merchants/auxiliaries/enterprises: within one month of becoming such or opening; societies: within the month following execution of the constitution deed | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.73, art. 334 (EVID-538) |
| LB-004 | CCom arts. 344/356/357: art. 344: "El registrador expedirá sin costo alguno la patente de comercio a toda sociedad, comerciante individual, auxiliar de comercio, empresa o establecimiento que haya sido debidamente inscrito. Esta patente deberá colocarse en lugar visible de toda empresa o establecimiento." / art. 356: "…la falta de inscripción y el incumplimiento de cualquiera de las obligaciones que establece el mismo para los comerciantes, se sancionará con multa de veinticinco a mil Quetzales, la cual será impuesta por el registrador." / art. 357: "Ninguna Cámara o Asociación Gremial podrá inscribir a comerciante alguno, en tanto no acredite su inscripción en el Registro Mercantil." | The registrar issues free of charge the patente de comercio to every duly enrolled society, individual merchant, auxiliary, enterprise or establishment; it must be displayed in a visible place of every enterprise or establishment. Failure to enroll or breach of any Code obligation for merchants: fine of twenty-five to one thousand quetzales, imposed by the registrar. No chamber or guild association may enroll any merchant who does not prove RM enrollment | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.76 art. 344; p.79 arts. 356-357 (EVID-538) |
| LB-005 | CCom derogatoria I.1º + identity blocks: "Se derogan: 1º. El Código de Comercio contenido en el Decreto gubernativo número 2946, con excepción de Títulos I, II, III, IV, V, VI, y VIII, del Libro III, Comercio Marítimo." / "Decreto del Congreso Número 2-70 … Código de Comercio de Guatemala" / Transitoria XI: "El presente Decreto entrará en vigor el primero de enero de 1971." | Repealed: the Commercial Code contained in governmental decree 2946, EXCEPT Titles I-VI and VIII of its Book III (maritime commerce, arts. 827-1319 as printed pp. 215-301 — numbering colliding with D2-70's own 800s-1000s). D2-70: given 28-Jan-1970, promulgated 9-Apr-1970, in force 1-Jan-1971 (as modified by D43-70) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.1 title block; p.214 date blocks + derogatoria art. I núm. 1º; pp.214-215 (EVID-536) |
| LB-006 | CCom art. 10 + definitions: art. 10: "Son sociedades organizadas bajo forma mercantil, exclusivamente las siguientes: 1º La sociedad colectiva. 2º La sociedad en comandita simple. 3º La sociedad de responsabilidad limitada. 4º La sociedad anónima. 5º La sociedad en comandita por acciones." / art. 59: "Sociedad colectiva es la que existe bajo una razón social y en la cual todos los socios responden de modo subsidiario, ilimitada y solidariamente, de las obligaciones sociales." / art. 68: "Sociedad en comandita simple, es la compuesta por uno o varios socios comanditados que responden en forma subsidiaria, ilimitada y solidaria de las obligaciones sociales; y por uno o varios socios comanditarios que tienen responsabilidad limitada al monto de su aportación. Las aportaciones no pueden ser representadas por títulos o acciones." / art. 78: "Sociedad de responsabilidad limitada es la compuesta por varios socios que sólo están obligados al pago de sus aportaciones. Por las obligaciones sociales responde únicamente el patrimonio de la sociedad y, en su caso, la suma que a más de las aportaciones convenga la escritura social. El capital estará dividido en aportaciones que no podrán incorporarse a títulos de ninguna naturaleza ni denominarse acciones." / art. 86: "Sociedad anónima es la que tiene el capital dividido y representado por acciones. La responsabilidad de cada accionista está limitada al pago de las acciones que hubiere suscrito." / art. 195: "Sociedad en comandita por acciones, es aquélla en la cual uno o varios socios comanditados responden de forma subsidiara [sic], ilimitada y solidaria por las obligaciones sociales y uno o varios socios comanditarios tienen la responsabilidad limitada al monto de las acciones que han suscrito, en la misma forma que los accionistas de una sociedad anónima. Las aportaciones deben estar representadas por acciones." | Societies organized in mercantile form are EXCLUSIVELY the following five: colectiva (general partnership — all partners subsidiarily, unlimitedly and solidarily liable); comandita simple (limited partnership — comanditados unlimited/solidary, comanditarios limited to their contribution; contributions may NOT be represented by títulos or acciones); responsabilidad limitada (R.L. — partners obliged only to pay their contributions; only the society's patrimony answers, plus any extra sum pacted in the deed; capital divided into aportaciones that may not be incorporated into titles of any nature nor called acciones); anónima (S.A. — capital divided and represented by acciones; each shareholder liable only up to the shares subscribed); comandita por acciones (mixed with shares — comanditarios liable like S.A. shareholders; contributions must be represented by acciones) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.4 art. 10; p.14 art. 59; p.15 art. 68; p.17 art. 78; p.19 art. 86; p.42 art. 195 (EVID-542) |
| LB-007 | CCom arts. 61/69/80/87/197 + 79: art. 61: "La razón social se forma con el nombre y apellido de uno de los socios o con los apellidos de dos o más de ellos, con el agregado obligatorio de la leyenda: y Compañía Sociedad Colectiva, leyenda que podrá abreviarse: y Cía. S. C." / art. 69: "…con el agregado obligatorio de la leyenda: y Compañía, Sociedad en Comandita, la que podrá abreviarse: y Cía. S. en C." / art. 80: "…En ambos casos es obligatorio agregar la palabra Limitada o la leyenda: y Compañía Limitada, las que podrán abreviarse: Ltda. O [sic] Cía. Ltda., respectivamente. Si se omiten esas palabras o leyendas, los socios responderán de modo subsidiario, ilimitado y solidariamente, de las obligaciones sociales." / art. 87: "La sociedad anónima se identifica con una denominación, la que podrá formarse libremente, con el agregado obligatorio de la leyenda: Sociedad Anónima, que podrá abreviarse S.A." / art. 197: "…con el agregado obligatorio de la leyenda: y Compañía Sociedad en Comandita por Acciones, la cual podrá abreviarse: y Cía., S.C.A." / art. 79: "El número de los socios no podrá exceder de veinte." | Mandatory name suffixes per form: colectiva — razón social (partnership name) formed from a partner's name and surname or two partners' surnames + "y Compañía Sociedad Colectiva" (abbrev. y Cía. S.C.); comandita simple — + "y Compañía, Sociedad en Comandita" (y Cía. S. en C.); R.L. — the word "Limitada" or "y Compañía Limitada" (Ltda. / Cía. Ltda.) MUST be added; if omitted the partners respond subsidiarily, unlimitedly and solidarily; S.A. — freely formed denominación + "Sociedad Anónima" (S.A.); comandita por acciones — + "y Compañía Sociedad en Comandita por Acciones" (y Cía., S.C.A.). R.L.: the number of partners may not exceed twenty | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.14 art. 61; p.15 art. 69; pp.17-18 art. 80; p.19 art. 87; p.42 art. 197; p.17 art. 79 (EVID-543) |
| LB-008 | CCom arts. 14/16/17/18/24: art. 14: "La sociedad mercantil constituida de acuerdo a las disposiciones de este Código e inscrita en el Registro Mercantil, tendrá personalidad jurídica propia y distinta de la de los socios individualmente considerados." / art. 16: "La constitución de la sociedad y todas sus modificaciones, incluyendo prórrogas, aumento o reducción de capital, cambio de razón social o denominación, fusión, disolución o cualesquiera otras reformas o ampliaciones, se harán constar en escritura pública. … Salvo en las sociedades por acciones, la modificación de la escritura constitutiva requerirá el voto unánime de los socios." / art. 17: "El testimonio de la escritura constitutiva, el de ampliación y sus modificaciones, deberá presentarse al Registro Mercantil, dentro del mes siguiente a la fecha de la escritura." / art. 18: "La persona que contrate en nombre de la sociedad, antes de que ésta pueda actuar como persona jurídica, será considerada como gestor de negocios de aquélla y queda personalmente responsable de los efectos del contrato celebrado." / art. 24: "El plazo de la sociedad principia desde la fecha de inscripción de la misma en el Registro Mercantil. Las sociedades mercantiles pueden constituirse para plazo indefinido." | A mercantile society constituted per this Code AND enrolled in the Mercantile Registry has a legal personality of its own, distinct from its partners'. Constitution and every modification (prórrogas, capital ±, name change, fusión, disolución, any reform) are effected in escritura pública (public deed); except in share societies, reforming the constitutive deed requires the partners' UNANIMOUS vote. The testimonio must be presented to the RM within the month following the deed's date. Whoever contracts in the society's name before it can act as a juridical person is treated as gestor de negocios (negotiorum gestor) and remains PERSONALLY responsible. The society's term runs from the RM inscription date; societies may be constituted for an indefinite term | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.4 arts. 14-15; p.5 arts. 16-18; p.6 art. 24 (EVID-544) |
| LB-009 | CCom arts. 32/35/36/37: art. 32: "Si hubiere pérdida de capital de una sociedad, éste deberá ser reintegrado o reducido cuando menos en el monto de las pérdidas, antes de hacerse repartición o distribución alguna de utilidades." / art. 35: "Queda prohibida la distribución de utilidades que no se hayan realmente obtenido conforme el balance general del ejercicio. … Los administradores que autoricen pagos en contravención de lo anterior y los socios que los hubieren percibido, responderán solidariamente de su reintegro…" / art. 36: "De las utilidades netas de cada ejercicio de toda sociedad, deberá separarse anualmente el cinco por ciento (5%) como mínimo para formar la reserva legal." / art. 37: "La reserva legal no podrá ser distribuida en forma alguna entre los socios, sino hasta la liquidación de la sociedad. Sin embargo, podrá capitalizarse cuando exceda del quince por ciento (15%) del capital al cierre del ejercicio inmediato anterior, sin perjuicio de seguir capitalizando el cinco por ciento (5%) anual…" | On capital loss, capital must be restored or reduced at least by the loss amount BEFORE any profit distribution. Distribution of profits not actually obtained per the fiscal-year balance general is prohibited; managers authorizing and partners receiving such payments are solidarily liable for restitution. From every society's net profits of each fiscal year, at least five percent (5%) must be separated annually to form the reserva legal (legal reserve). The reserve may not be distributed among partners until liquidation; it MAY be capitalized when it exceeds fifteen percent (15%) of capital at the prior fiscal-year close, without prejudice to continuing the annual 5% accrual | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.8 arts. 32, 35; p.9 arts. 36-37 (EVID-545) |
| LB-010 | CCom arts. 88/89/90/92/93: art. 88: "El capital autorizado de una sociedad anónima es la suma máxima que la sociedad puede emitir en acciones, sin necesidad de formalizar un aumento de capital. El capital autorizado podrá estar total o parcialmente suscrito al constituirse la sociedad y debe expresarse en la escritura constitutiva de la misma." / art. 89: "En el momento de suscribir acciones es indispensable pagar por lo menos el veinticinco por ciento (25%) de su valor nominal." / art. 90: "El capital pagado inicial de la sociedad anónima debe ser por lo menos de cinco mil quetzales (Q5, 000.00)." [sic] / art. 92: "Las aportaciones en efectivo deberán depositarse en un banco a nombre de la sociedad y en la escritura constitutiva el notario deberá certificar ese extremo." / art. 93: "No podrá anunciarse el capital autorizado, sin indicar al mismo tiempo el capital pagado. La infracción de este artículo se sancionará de oficio por el Registro Mercantil con una multa de veinticinco a quinientos quetzales…" | The authorized capital of an S.A. is the maximum sum the society may issue in shares without formalizing a capital increase; it may be totally or partially subscribed at constitution and must be expressed in the deed. At subscription at least 25% of nominal value must be paid. Initial paid capital must be at least five thousand quetzales (Q5,000.00) [as printed "Q5, 000.00" — sic]. Cash contributions must be deposited in a bank in the society's name and the notary must certify that fact in the constitutive deed. Authorized capital may not be advertised without simultaneously stating paid capital; breach sanctioned ex officio by the RM with a fine of 25 to 500 quetzales | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.19 arts. 88-90; p.20 arts. 92-93 (EVID-546) |
| LB-011 | CCom arts. 99-102/107/108: art. 99: "Las acciones en que se divide el capital social de una sociedad anónima estarán representadas por títulos que servirán para acreditar y transmitir la calidad y los derechos de socio. A los títulos de las acciones, en lo que sea conducente, se aplicarán las disposiciones de los títulos de crédito." / art. 100: "Todas las acciones de una sociedad serán de igual valor y conferirán iguales derechos. Sin embargo, en la escritura social podrá estipularse que el capital se divida en varias clases de acciones con derechos especiales para cada clase…" / art. 101: "Cada acción confiere derecho a un voto a su tenedor. … No pueden emitirse acciones con voto múltiple." / art. 102: "Se prohibe a las sociedades anónimas emitir acciones por una suma menor de su valor nominal y emitir títulos definitivos si la acción no está totalmente pagada." / art. 107: "Los títulos de acciones deben contener por lo menos: 1º La denominación, el domicilio y la duración de la sociedad. 2º La fecha de la escritura constitutiva, lugar de su otorgamiento, notario autorizante y datos de su inscripción en el Registro Mercantil. 3º El nombre del titular de la acción, si son nominativas. 4º El monto del capital social autorizado y la forma en que éste se distribuirá. 5º El valor nominal, su clase y número de registro. 6º Los derechos y las obligaciones particulares de la clase… 7º La firma de los administradores…" / art. 108: "Las acciones pueden ser nominativas o al portador, a elección del accionista, si la escritura social no establece lo contrario." | Shares are represented by títulos (certificates) that evidence and transmit partner quality and rights; the títulos de crédito provisions apply as pertinent. All shares equal value and equal rights, unless the deed divides capital into classes with special rights. One share = one vote; multiple-vote shares prohibited. Issuing below nominal value prohibited; definitive certificates only when the share is fully paid. Certificate minimum content: 7 items (denominación/domicilio/duration; deed date, place, notary + RM inscription data; holder name if nominative; authorized capital + distribution; nominal value, class, registration number; class rights/obligations; administrators' signature). Shares may be nominativas (registered) or al portador (bearer) at the shareholder's choice unless the deed says otherwise | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.21 arts. 99-102; pp.21-23 arts. 103-108 (EVID-547) |
| LB-012 | CCom arts. 119/125/126/128: art. 119: "La sociedad considerará como accionista al inscrito como tal en el Registro de Accionistas, si las acciones son nominativas y al tenedor de éstas, si son al portador." / art. 125: "Las sociedades anónimas que emitieren acciones nominativas o certificadas [sic] provisionales, llevarán un registro de los mismos que contendrá: 1º El nombre y el domicilio del accionista, la indicación de las acciones que le pertenezcan, expresándose los números, series, clases y demás particularidades. 2º En su caso, los llamamientos efectuados y los pagos hechos. 3º Las transmisiones que se realicen. 4º La conversión de las acciones nominativas o certificados provisionales en acciones al portador. 5º Los canjes de títulos. 6º Los gravámenes que afecten a las acciones. 7º Las cancelaciones de éstos y de los títulos." / art. 126: "La negativa o demora injustificada de la sociedad para inscribir a un accionista en el Registro de Acciones Nominativas, la obliga solidariamente con sus administradores, al pago de los daños y perjuicios… el juez ordenará la inscripción." / art. 128: "Las acciones nominativas son transferibles mediante endoso del título que el interesado, para que se le tenga como accionista, hará registrar en el libro correspondiente. Las acciones al portador son transferibles por la mera tradición." | The society considers as shareholder the person inscribed in the Registro de Accionistas (for nominative shares) or the bearer (for bearer shares). S.A.s issuing nominative or provisional certificates keep a register containing: 1º holder name and domicile + share numbers, series, classes and particulars; 2º llamamientos (calls) made and payments made; 3º transmissions effected; 4º conversion of nominative/provisional into bearer shares; 5º title exchanges (canjes); 6º gravámenes (encumbrances) affecting the shares; 7º cancellations of these and of the titles. Unjustified refusal or delay to inscribe a shareholder binds the society solidarily with its administrators to pay damages; the judge orders the inscription. Nominative shares transfer by endoso (endorsement) + registration in the book; bearer shares by mere tradition (delivery) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.25 arts. 117-119; p.27 arts. 125-126, 128 (EVID-548) |
| LB-013 | CCom arts. 132/134/135/138/148/149/153: art. 132: "La asamblea general formada por los accionistas legalmente convocados y reunidos, es el órgano supremo de la sociedad…" / art. 134: "La asamblea ordinaria se reunirá por lo menos una vez al año, dentro de los cuatro meses que sigan al cierre del ejercicio social… 1º Discutir, aprobar o improbar el estado de pérdidas y ganancias, el balance general y el informe de la administración…" / art. 135: "Son asambleas extraordinarias, las que se reunan [as printed] para tratar cualquiera de los siguientes asuntos: 1º Toda modificación de la escritura social, incluyendo el aumento o reducción de capital o prórroga del plazo. 2º Creación de acciones de voto limitado o preferentes y la emisión de obligaciones o bonos…" / art. 138: "La asamblea general deberá convocarse mediante avisos publicados por lo menos dos veces en el Diario Oficial y en otro de los de mayor circulación en el país, con no menos de quince días de anticipación a la fecha de su celebración. … En las sociedades que hayan emitido acciones nominativas, deberá enviarse a los tenedores de éstas… un aviso escrito… por correo certificado…" / art. 148: "Para que una asamblea ordinaria se considere reunida, deberán estar representadas, por lo menos, la mitad de las acciones que tengan derecho a voto. Las resoluciones sólo serán válidas cuando se tomen, por lo menos, por la mayoría de votos presentes." / art. 149: "…en las asambleas extraordinarias deberán estar representadas para que se consideren legalmente reunidas, un mínimo del sesenta por ciento (60%) de las acciones que tengan derecho a voto. Las resoluciones se tomarán con más del cincuenta por ciento (50%) de las acciones con derecho a voto, emitidas por la sociedad." / art. 153 (3º ¶): "Dentro de los quince días siguientes a cada asamblea extraordinaria, los administradores deberán enviar al Registro Mercantil, una copia certificada de las resoluciones…" | The general assembly of legally convened shareholders is the society's supreme organ. The ORDINARY assembly meets at least once a year, within the four months following the close of the fiscal year (discusses/approves/disapproves the P&L, balance general and management report). EXTRAORDINARY assemblies treat: any modification of the deed (incl. capital increase/reduction, term extension), creation of limited-vote or preferred shares, bond issues, own-share acquisition, nominal-value changes. Convocation: notices published at least TWICE in the Diario Oficial and in another paper of major circulation, ≥15 days ahead [as printed, pre-D18-2017]; written notice by certified mail to nominative holders. Quorum: ordinary — half of voting shares represented, resolutions by majority of votes present; extraordinary — minimum 60% of voting shares represented, resolutions by MORE than 50% of all issued voting shares. Within 15 days after each extraordinary assembly the administrators must send the RM a certified copy of the resolutions | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.28-30 arts. 132-138; p.31 art. 141; p.32 arts. 148-149; p.33 art. 153 (EVID-549; art. 153 3º ¶ also EVID-568) |
| LB-014 | CCom arts. 162/178/184/185: art. 162: "Un administrador único o varios administradores, actuando conjuntamente constituidos en consejo de administración, serán el órgano de la administración de la sociedad… Los administradores pueden ser o no socios; serán electos por la asamblea general y su nombramiento no podrá hacerse por un período mayor de tres años, aunque su reelección es permitida… El nombramiento de administrador es revocable por la asamblea general en cualquier tiempo." / art. 178: "Los administradores pueden ser removidos, sin necesidad de expresión de causa, mediante acuerdo adoptado por una asamblea general." / art. 184: "Las operaciones sociales serán fiscalizadas por los propios accionistas, por uno o varios contadores o auditores, o por uno o varios comisarios, de acuerdo con las disposiciones de la escritura social…" / art. 185: "Los contadores, auditores o los comisarios, deberán ser designados por la asamblea ordinaria anual que practique la elección de administradores…" | A sole administrator or several administrators acting jointly as a board of administration are the society's administration organ; they may be partners or not, are elected by the general assembly for a period NOT exceeding three years (reelection permitted), and the appointment is revocable by the assembly AT ANY TIME (ad nutum). Administrators may be removed WITHOUT expression of cause by general agreement. Fiscalization is flexible: by the shareholders themselves, by one or more contadores (accountants) or auditores, or by comisarios (commissioners), per the deed; these are designated by the annual ordinary assembly that elects the administrators | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.35 art. 162; p.38 art. 178; pp.39-40 arts. 184-185 (EVID-550) |
| LB-015 | CCom arts. 206/207/210/211/212: art. 206: "La resolución de aumento de capital se elevará a escritura pública y se inscribirá en el Registro Mercantil." / art. 207: "El pago del aumento podrá realizarse… 3º Por capitalización de utilidades o de reservas." / art. 210: "El capital podrá reducirse por disminución del valor de las aportaciones sociales, por disminución del valor nominal de todas las acciones o por amortización de algunas de ellas. Bajo la responsabilidad personal del administrador… la resolución se comunicará por el correo más rápido, con aviso de recepción a todos los acreedores de la sociedad cuya dirección sea conocida." / art. 211: "La resolución de reducción de capital deberá ser inscrita en el registro Mercantil. Para el trámite deberá presentarse acta notarial en la que se transcriba la respectiva resolución y la declaración de cumplimiento de la obligación mencionada en el segundo párrafo del artículo anterior." / art. 212: "Dentro de los treinta días siguientes a la última publicación, cualquier interesado podrá oponerse a la reducción del capital en juicio sumario… La escritura pública que contenga la reducción del capital social, sólo podrá otorgarse después de vencido el plazo mencionado, si no hay oposición…" | A capital-increase resolution is elevated to escritura pública and inscribed in the RM; payment may be made (3º) by capitalization of profits or reserves. Capital may be reduced by diminishing contributions' value, all shares' nominal value, or amortizing some; under the administrator's PERSONAL responsibility the resolution is communicated by fastest mail with acknowledgment to all creditors whose address is known. The reduction resolution must be inscribed in the RM; the filing requires a NOTARIAL ACTA transcribing the resolution and declaring compliance with the creditor-notice obligation [arts. 211/212 as reformed D104-70/D42-78]. Within THIRTY days after the last publication any interested party may oppose the reduction in summary proceedings; the reduction deed may be executed only after that window if no opposition | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.43 arts. 203-204; p.44 arts. 205-209; p.45 arts. 210-212 (EVID-551) |
| LB-016 | CCom arts. 215/218/220/352/355: art. 215 (selected): "…deberá: 1º Comprobar que está debidamente constituida… 4º Constituir en la República un mandatario con representación… 5º. Constituir un capital asignado para sus operaciones en la República y una fianza a favor de terceros por una cantidad no menor al equivalente en quetzales de cincuenta mil dólares de los Estados Unidos de América, (US$ 50,000.00), que fijará el Registro Mercantil… 8º Presentar una copia certificada de su último balance general y estado de pérdidas y ganancias. Los documentos necesarios… deberán presentarse al Registro Mercantil, para los efectos de obtener la autorización gubernativa… La documentación debe llevar un timbre de Q0.10 por hoja como único impuesto." / art. 218: "…el Registro Mercantil después de presentar: a) Estados Financieros certificados por Contador o Auditor Público, colegiado activo, y acompañar declaración jurada en acta notarial en la que el representante legal haga constar que su representada cumplió con todas sus obligaciones tributarias hasta la fecha de su retiro… b) Comprobación de que las obligaciones y negocios contraídos en la República han sido cumplidos o están garantizados." / art. 220: "Una sociedad legalmente constituida en el extranjero, no está obligada a obtener autorización ni registrarse en el país, cuando solamente: 1. Es parte de cualquier gestión o juicio… 2. Abre o mantiene cuentas bancarias… 3. Efectúa ventas o compras únicamente a agente de comercio independiente…" / art. 352: "…deberán solicitarlo al Registro Mercantil, único encargado de otorgar la autorización respectiva… previa comprobación de la efectividad del capital asignado a sus operaciones y de la constitución de la fianza hará la inscripción definitiva… y extenderá la Patente de Comercio correspondiente." / art. 355: "La autorización… caducará si la sociedad no iniciare sus operaciones dentro de un plazo de un año…" | A foreign society must: prove due constitution; constitute in the Republic a mandatario (attorney-in-fact) with representation; constitute assigned capital for its Guatemalan operations AND a fianza (guaranty bond) in favor of third parties for no less than the quetzal equivalent of US$50,000.00, fixed by the RM; present a certified copy of its last balance general and P&L; documents filed at the RM to obtain governmental authorization; the documentation carries a Q0.10-per-sheet timbre (stamp) as its only tax [numerals 5º/6º reformed D62-95]. Withdrawal: certified financial statements + sworn notarial acta that the society met all tax obligations to the withdrawal date + proof that Guatemalan obligations are fulfilled or guaranteed. No authorization/registration needed when the foreign society only: is party to a proceeding; opens/maintains bank accounts; buys/sells through an independent commercial agent. The RM is the SOLE authorizer; after verifying assigned capital and fianza it makes the definitive inscription and issues the Patente de Comercio. Authorization lapses if operations do not start within one year | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.45-47 arts. 213-221; p.78 arts. 352, 355 (EVID-552) |
| LB-017 | CCom arts. 223/224: art. 223: "Las sociedades no inscritas en el Registro Mercantil, aun cuando se hayan exteriorizado como tales frente a terceros, no tienen existencia legal y sus socios responderán solidaria e ilimitadamente de las obligaciones sociales." / art. 224: "La omisión de la escritura social y de las solemnidades prescritas, produce nulidad absoluta. Los socios, sin embargo, responderán solidaria e ilimitadamente frente a terceros…" | Societies not inscribed in the RM, even if they have appeared as such before third parties, have NO legal existence and their partners respond solidarily and unlimitedly for the society's obligations. Omission of the social deed and prescribed solemnities produces absolute nullity; the partners nevertheless respond solidarily and unlimitedly towards third parties | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.47-48 arts. 222-224 (EVID-553) |
| LB-018 | CCom arts. 237/238/239/241: art. 237: "Las sociedades se disuelven totalmente por cualquiera de las siguientes causas: 1º. Vencimiento del plazo fijado en la escritura. 2º. Imposibilidad de seguir realizando el objeto principal… 4º. Pérdida de más del sesenta por ciento (60%) del capital pagado. 5º. Reunión de las acciones o las aportaciones de una sociedad en una sola persona…" / art. 238: "…Si en la junta o asamblea general se decide subsanar la causa de disolución y modificar la escritura social para continuar sus operaciones o alternativamente acordar la disolución de la sociedad, lo resuelto se elevará a escritura pública que se inscribirá en el Registro Mercantil." / art. 239: "La declaratoria de disolución se publicará de oficio por el Registro Mercantil, tres veces duran te [sic] un término de quince días en el Diario Oficial y en otro de los de mayor circulación en el país." / art. 241: "Disuelta la sociedad entrará en liquidación, pero conservará su personalidad jurídica, hasta que aquélla se concluya y durante ese tiempo, deberá añadir a su denominación o razón social las palabras: En liquidación. El término para la liquidación no excederá de un año…" | Societies dissolve totally by any of the causes: expiry of the deed's term; impossibility of pursuing the main object; … loss of MORE THAN SIXTY PERCENT (60%) of paid capital; concentration of all shares/aportaciones in one person… The general meeting may either cure the cause (reforming the deed to continue) or agree dissolution — either way elevated to escritura pública inscribed in the RM. The dissolution declaration is published EX OFFICIO by the RM, three times within fifteen days in the Diario Oficial and a major paper [as printed, pre-D18-2017]. Dissolved, the society enters liquidation but KEEPS its legal personality until liquidation concludes, and during that time must add the words "En liquidación" (in liquidation) to its name; the liquidation term may not exceed one year (judicially extendable) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.51-52 arts. 237-241 (EVID-554) |
| LB-019 | CCom arts. 243/247/248/249/251/253: art. 243: "Nombrados los liquidadores y aceptados los cargos, el nombramiento se inscribirá en el Registro Mercantil. … El Registro Mercantil pondrá en conocimiento del público que la sociedad ha entrado en liquidación y el nombre de los liquidadores, por medio de avisos que se publicarán tres veces en el término de un mes…" / art. 247 (11º): "Depositar en el Registro Mercantil el balance general final, una vez aprobado y obtener del propio Registro la cancelación de la inscripción de la escritura social." / art. 248: "En los pagos, los liquidadores observarán en todo caso el orden siguiente: 1º. Gastos de liquidación. 2º. Deudas de la sociedad. 3º. Aportes de los socios. 4º. Utilidades." / art. 249: "Los liquidadores no pueden distribuir entre los socios… mientras no hayan sido pagados los acreedores… o no hayan sido separadas las sumas necesarias…" / art. 251: "…2º. Dicho balance se publicará en el Diario Oficial y en otro de los de mayor circulación en el país, por tres veces durante un término de quince días. … La asamblea deberá celebrarse, por lo menos, un mes después de la primera publicación…" / art. 253: "Las sumas que pertenezcan a los accionistas y que no fueren cobradas en el transcurso de dos meses contados desde la aprobación del balance general final, se depositarán en una institución bancaria… Si transcurrieren cinco años sin que ninguna persona reclamare… la institución bancaria deberá adjudicarlas gratuitamente a la Universidad de San Carlos de Guatemala." | Liquidators appointed and accepted are inscribed at the RM, which notifies the public (3 notices within one month) that the society entered liquidation and names the liquidators. Liquidators' duties include: deposit the final approved balance general at the RM and obtain cancellation of the inscription of the social deed (the close-out). Payments observe the order: 1º liquidation costs; 2º society's debts; 3º partners' contributions; 4º profits. No distribution to partners until creditors are paid or necessary sums separated. The final balance is published 3× within 15 days [pre-D18-2017 text]; the approving assembly is held at least one month after the first publication. Shareholder sums unclaimed for two months from approval of the final balance are deposited in a bank; after FIVE years unclaimed they are gratuitously adjudicated to the Universidad de San Carlos de Guatemala (USAC escheat) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.52-55 arts. 242-253 (EVID-555) |
| LB-020 | CCom arts. 256/259/260/262: art. 256: "La fusión de varias sociedades puede llevarse a cabo…: 1º. Por la creación de una nueva sociedad y la disolución de todas las anteriores… 2º. Por la absorción de una o varias sociedades por otra… la nueva sociedad o aquella que ha absorbido a las otras, adquiere los derechos y obligaciones de las sociedades disueltas." / art. 259: "…Los acuerdos de fusión deben inscribirse en el Registro Mercantil, siendo título suficiente para ello, actas notariales en las que se transcriba lo acordado por cada sociedad. Hecho el registro, deberán publicarse conjuntamente los acuerdos de fusión y el último balance general de las sociedades en el Diario Oficial y en otro de los de mayor circulación en el país por tres veces en el término de quince días." / art. 260: "La fusión no podrá llevarse a cabo antes de transcurridos dos meses, contados desde la última publicación de los acuerdos… y hasta entonces se podrá otorgar la correspondiente escritura pública, salvo que conste el consentimiento escrito de los respectivos acreedores… Dentro de los términos de dos meses los acreedores… pueden oponerse a la fusión… La oposición suspenderá la fusión…" / art. 262: "Las sociedades constituidas conforme a este Código, pueden transformarse en cualquier otra clase de sociedad mercantil. La sociedad transformada mantiene la misma personalidad jurídica de la sociedad original." | Fusion may be carried out by creation of a new society (all predecessors dissolving) or by absorption; the new/absorbing society acquires the rights and obligations of the dissolved societies (universal succession). The fusion agreements are inscribed at the RM — notarial actas transcribing each society's accord suffice as title — then the fusion agreements and the last balance general are JOINTLY published 3× within 15 days [pre-D18-2017 text]. Fusion may not be effected before TWO MONTHS from the last publication (earlier deed only with written creditor consent); within the two months creditors may oppose, and opposition suspends the fusion. Transformation: societies constituted under this Code may transform into ANY other mercantile society class; the transformed society KEEPS the same legal personality | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.56-57 arts. 256-262 (EVID-556) |
| LB-021 | CCom arts. 265/272/280/293/304 + transitoria XI: art. 265: "El factor se constituye mediante mandato con representación, otorgado por el comerciante, por nombramiento que le extenderá este último o por contrato de trabajo escrito. El mandato, nombramiento o contrato de trabajo del factor deberá inscribirse en el Registro Mercantil." / art. 272: "Los actos y contratos ejecutados por el factor serán válidos respecto del principal… y, con relación a terceros, mientras no se haya inscrito en el Registro Mercantil la revocatoria, cancelación, terminación o enajenación." / art. 280: "Son agentes de comercio, las personas que actúen de modo permanente, en relación con uno o varios principales, promoviendo contratos mercantiles o celebrándolos en nombre y por cuenta de aquéllos…" [reformed D8-98] / art. 293: "Para poder ejercer como corredor, es indispensable tener autorización legal, la que el interesado deberá obtener de acuerdo con los requisitos que establezca el reglamento respectivo." / art. 304: "Si el comisionista actuare como tal habitualmente, deberá obtener patente de acuerdo con el reglamento respectivo." / transitoria XI: "El Organismo Ejecutivo emitirá, por el órgano del Ministerio de Economía, los reglamentos necesarios para la obtención de licencia de comisionista, de corredor, martillero y otros…" | The factor (commercial manager) is constituted by mandate with representation granted by the merchant, by appointment, or by written employment contract — the mandate/appointment/contract MUST be inscribed in the RM. The factor's acts remain valid towards third parties until the revocation, cancellation, termination or alienation is inscribed at the RM. Agentes de comercio act permanently for one or more principals promoting or concluding mercantile contracts [D8-98 text; no RM matrícula clause of its own]. A corredor (broker) needs legal authorization per the respective reglamento; a habitual comisionista (commission agent) needs a patente per the respective reglamento. Transitoria XI: the Executive through MinEconomía issues the licensing reglamentos (comisionista, corredor, martillero, others) — NOT in this corpus | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.58-59 arts. 263-266, 272; p.61 art. 280 + tag; pp.64-65 arts. 292-294; p.67 arts. 303-304; p.210 transitoria XI (EVID-557) |
| LB-022 | CCom arts. 27/116/153(3º¶)/345 (firma/protocolización hooks): art. 27: "Los bienes que no consistan en dinero, aportados por los socios, pasan al dominio de la sociedad, sin necesidad de tradición y se detallarán y justipreciarán en la escritura constitutiva o en el inventario previamente aceptado por los socios, el que deberá protocolizarse." / art. 116: "…deberán constar en escritura pública y el notario autorizante deberá dar aviso de la existencia de un pacto… a la sociedad y al Registro Mercantil, razonando brevemente los títulos de las acciones." / art. 153 (3º ¶): "Dentro de los quince días siguientes a cada asamblea extraordinaria, los administradores deberán enviar al Registro Mercantil, una copia certificada de las resoluciones…" / art. 345: "…las firmas de los otorgantes de documentos privados, deberán ser legalizadas." | Non-cash contributions pass into the society's dominion without tradition, detailed and valued in the constitutive deed or in a previously partner-accepted inventory that must be PROTOCOLIZED. Shareholder-vote pacts are set in escritura pública and the authorizing notary must give notice of the pact's existence to the society and the RM, briefly recording (razonando) the share titles. Certified copies of extraordinary-assembly resolutions go to the RM within 15 days. Signatures of grantors of private documents must be legalized | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.7 art. 27; p.25 art. 116; p.33 art. 153; p.74 art. 335; p.76 art. 345 (EVID-568) |
| LB-023 | CCom transitoria I/VII + derogatoria II: transitoria I: "Las sociedades mercantiles constituidas al amparo de leyes anteriores, continuarán regidas por las mismas." / transitoria VII: "Es obligatoria la inscripción en el Registro Mercantil jurisdiccional, de todas las personas, empresas, actos… del 334 al 338 de este Código, dentro de un plazo que vencerá al 30 de junio de 1974. … Después del primero de marzo de mil novecientos setenta y uno, ningún tribunal y oficina pública admitirá documentos sujetos a inscripción que no estuvieren razonados por el Registro Mercantil." / derogatoria II: "Artículo 72. La Dirección General del Impuesto sobre la Renta debe llevar un registro especial de las personas jurídicas sujetas a fiscalización. Para inscribirse en dicho Registro, las sociedades mercantiles… presentarán… una certificación de las inscripciones correspondientes en el Registro Mercantil junto con su balance general de apertura, lo cual deberán hacer dentro de los treinta días siguientes a su inscripción definitiva en este último Registro." | Mercantile societies constituted under prior laws continue governed by those laws (transitoria I). The original adaptation window (enrollment of all pre-Code persons/enterprises/acts, arts. 334-338, by 30-Jun-1974, with extensions) and the court/office bar on non-razonado documents from 1-Mar-1971 (transitoria VII). The tax-registry linkage is original design: the revenue directorate's special register of juridical persons required, for society enrollment, a CERTIFICATION of RM inscriptions together with the opening balance general, within 30 days of the definitive RM inscription (derogatoria II rewriting D Ley 229 art. 72 — ancestor of the RM→RTU interplay) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.207-214 transitorias I-XX + derogatorias (EVID-569) |
| LB-024 | D-15-2026 (77_) arts. 112/113/120/121 — CC arts. 45/125 reformed + transitorias: art. 112 (CC art. 45): "El nombramiento y la remoción del órgano de administración de todas las sociedades mercantiles… se harán por resolución de los socios. Este deberá inscribirse en el Registro Mercantil mediante la presentación de acta notarial…" / art. 113 (CC art. 125 reformed): "Las sociedades cuyo capital se divide en acciones, deberán llevar un registro de acciones o certificados provisionales de las mismas, con la información mínima siguiente: 1. Accionistas que sean personas individuales: nombre completo, nacionalidad y datos del documento de identificación. 2. Accionistas que sean personas jurídicas: razón o denominación social completa, identificación de la persona jurídica que sea accionista y el país o jurisdicción bajo cuyas leyes se constituyó. 3. Acciones, participaciones o aportaciones que se encuentren dentro del patrimonio de fideicomisos, estructuras jurídicas u otra figura legal de naturaleza patrimonial: información que permita su identificación…, así como la o las personas quienes actúan como fiduciarias o administradores de estas. 4. La dirección física y correo electrónico de cada accionista. 5. En sucaso [sic], los llamamientos efectuados y los pagos hechos. 6. Las transmisiones de titularidad de acciones… En los casos de los numerales 1 y 2, será necesario detallar la cantidad de acciones… / …el referido registro… deberá llevarse en un libro autorizado por el Registro Mercantil, el cual podrá ser físico o electrónico… bajo la responsabilidad del secretario del órgano de administración…, o en su caso por el Administrador Unico [sic]… Las sociedades deberán dar aviso al Registro Mercantil…, de la primera inscripción y demás transmisiones sobre la titularidad de acciones…, dentro de los diez (10) días hábiles siguientes de realizarla… El incumplimiento… se sancionará con multa equivalente de cinco a cincuenta salarios mínimos para actividades no agrícolas de la circunscripción económica uno, la cual será impuesta por el Registrador Mercantil. Las sociedades mercantiles cuyas acciones estén inscritas para oferta pública bursátil, están exentas… siempre y cuando el registro… se lleve… dentro del sistema o registros de una central depositaria de valores… / El Registro Mercantil deberá llevar y resguardará de manera segura una base de datos electrónica… confidencial; en consecuencia, no podrá proporcionar dicha información… excepto y únicamente a la Superintendencia de Bancos y el Ministerio Público…" / art. 120: "…deberán cumplir en un plazo máximo de un (1) año…, las obligaciones establecidas en el artículo 125 del Código de Comercio… y remitir al Registro Mercantil certificación de la información a la que se refieren los numerales del 1) al 3)…" / art. 121: "…deberán inscribir en el Registro Mercantil, dentro de un plazo no mayor a seis (6) meses, contados a partir de la entrada en vigencia de la presente Ley, a todos los miembros del órgano de administración, con o sin representación legal… Vencido el plazo…, las sociedades mercantiles que no hubieran cumplido…, no podrán realizar ninguna operación en el Registro Mercantil, mientras no se haya presentado la solicitud de registro de todos sus miembros del órgano de administración." | D-15-2026 (Ley Integral AML) reforms the Commercial Code. CC art. 45 (new text): appointment and removal of the administration organ of ALL mercantile societies is done by resolution of the socios, inscribed at the RM upon presentation of a notarial acta. CC art. 125 (new text): societies whose capital is divided into shares must keep a register of shares/provisional certificates with minimum information: 1. individual shareholders — full name, nationality, ID-document data; 2. juridical-person shareholders — full razón/denominación, identification and country/jurisdiction of constitution; 3. shares inside fideicomisos (trusts) or patrimonial structures — identifying information plus the fiduciaries/administrators; 4. each shareholder's PHYSICAL ADDRESS AND E-MAIL; 5. calls made and payments made where applicable; 6. transmissions of title (numerals 1-2 require detailing the quantity of shares). The register is kept in an RM-AUTHORIZED BOOK, physical or electronic, under the responsibility of the secretary of the administration organ or the sole administrator; societies must give the RM notice of the first inscription and further transmissions within 10 días hábiles (business days); breach sanctioned with a fine equivalent to 5 to 50 salarios mínimos (minimum wages) for non-agricultural activities of economic circumscription one (CE1), imposed by the Registrador Mercantil; public-offer shares held through a central securities depositary are exempt. The RM must keep a secure CONFIDENTIAL electronic database, accessible only to the Superintendencia de Bancos and the Ministerio Público. Transitorias: art. 120 — art.-125 compliance within one year of vigencia + certification of numerals 1-3 to the RM; art. 121 — ALL administration-organ members inscribed at the RM within six months of vigencia, failing which the society may perform NO operation at the RM until the registration request for all members is filed | `gt/sources/77_AML_LeyIntegral_D15-2026.pdf` | pp.15-16, arts. 112-114, 116-124 (EVID-634; text layer = forced OCR, quoted from the evidence file) |

## 3. Functional Requirements

### 3.1 Comerciante calificación model (arts. 2/3/6/9)

- **GT-CML-FR-026:** The system shall carry the comerciante calificación
  (qualification) catalog as shared dated config: an individual is a
  comerciante when acting *en nombre propio y con fines de lucro* (in
  one's own name and for profit) in any of the FOUR activity classes of
  art. 2 — (1º) industry directed at production/transformation of goods
  and provision of services; (2º) intermediation in the circulation of
  goods and provision of services; (3º) banking, insurance and fianzas;
  (4º) auxiliaries of the foregoing — the two-element test (own name +
  profit) being cumulative and the class list closed as printed.
  (LB-001; EVID-537)
- **GT-CML-FR-027:** The system shall carry the art. 9 negative list
  and the art. 6 capacity rule as classification guards: NOT
  comerciantes — (1º) liberal professionals; (2º) agricultural/
  livestock/similar producers as regards cultivation and transformation
  of their OWN enterprise's products; (3º) artisans working only on
  order or without almacén/tienda for sale of their products; capacity
  follows the Civil Code's *hábil para contratar y obligarse* (capable
  of contracting and binding oneself) test for individual and juridical
  persons (the evidence gloss adds art. 13: the State and public
  entities are not comerciantes though their commercial acts remain
  subject to the Code). (LB-002; EVID-537)
- **GT-CML-FR-028:** The system shall implement the entity-type-driven
  rule of art. 3 as an override: EVERY society organized under a
  mercantile form (FR-035's five-form list) has comerciante quality
  *cualquiera que sea su objeto* (whatever its object) — no activity
  test and no negative-list screening applies to sociedades; the
  registration obligation and Code applicability follow from the form
  alone. (LB-001; EVID-537)
- **GT-CML-FR-029:** The system shall surface comerciante
  classification on the partner/company record (odoo data surface): a
  classification field resolving individual-comerciante (FR-026 test,
  minus FR-027 exclusions, plus the FR-030 capital-threshold flag)
  vs sociedad mercantil (FR-028) vs non-comerciante, driving the
  matrícula obligation flags (FR-030) and the CCom applicability note —
  a recorded classification with basis and as-of date, never a silent
  default. (LB-001; LB-002; EVID-537)

### 3.2 Matrícula engine (arts. 334/344/356-358)

- **GT-CML-FR-030:** The system shall model the matrícula universe and
  thresholds as dated config: RM enrollment obligatory for (1º)
  individual comerciantes with capital ≥ **Q2,000** — a 1970-nominal
  figure never indexed in this print (R67), stored as a D16 dated row
  with valid_from 1971-01-01, no valid_to, instrument D2-70, and the
  **GOQ-126 verify-before-config flag** (never treated as a current
  value; rejected myth, wave set); (2º) ALL sociedades mercantiles —
  no threshold; (3º) empresas y establecimientos mercantiles within
  these extremes; (4º) law-specified facts and legal relations; (5º)
  auxiliares de comercio. (LB-003; EVID-538; R67; GOQ-126)
- **GT-CML-FR-031:** The system shall implement the 1-month matrícula
  windows as lifecycle calendars on the party/company record:
  individual comerciantes, auxiliaries and empresas/establecimientos —
  within one month of becoming such or of opening; sociedades — within
  the month following the *otorgamiento de la escritura de
  constitución* (execution of the constitution deed); deadlines surface
  as dated reminders/exposure, with the sociedad window keyed to the
  recorded escritura date (FR-041) and the enrollment event tracked
  through the RM-event states owned by `01_rm-surfaces.md`
  (GT-CML-FR-012, consumed by id). (LB-003; EVID-538)
- **GT-CML-FR-032:** The system shall record the patente de comercio
  duty: the registrar issues the patente FREE OF CHARGE to every duly
  enrolled sociedad, comerciante individual, auxiliar, empresa or
  establecimiento, and it must be *colocada en lugar visible*
  (displayed in a visible place) of every empresa/establecimiento —
  modeled as a patente-issue fact + display-attestation flag on the
  establishment record; NO patente fee is modeled (the
  matrícula/renovación fee-row absence is owned by
  `01_rm-surfaces.md` GT-CML-FR-006, consumed by id).
  (LB-004; EVID-538; GT-CML-FR-006)
- **GT-CML-FR-033:** The system shall record the matrícula-enforcement
  exposures: (i) failure of inscription or breach of any Code
  obligation for comerciantes → registrador-imposed *multa* (fine)
  **Q25–Q1,000** — 1970-nominal (R67), a dated exposure row kin to the
  RM multa track owned by `01_books-anchor.md` GT-COA-FR-020 (consumed
  by id; separate from and never netted with the taxation sanction
  track, R62); (ii) the gremial lockout — no Cámara or Asociación
  Gremial may enroll a merchant without proof of RM inscription,
  surfaced as a precondition flag on chamber-membership records.
  (LB-004; EVID-538; R67; GT-COA-FR-020)
- **GT-CML-FR-034:** The system shall enforce the R65 citation guard
  over this file's territory (consumed from
  `01_books-anchor.md` GT-COA-FR-030..032 by id, never re-derived): any
  citation drawn from pp. 215-301 of the 66_ print — the surviving
  D-2946 old-code maritime appendix (Libro III arts. 827-1319, whose
  numbers collide with D2-70's own 800s-1000s) — must be recorded as
  "D2946 (old code) art. N", never as D-2-70; the society-lifecycle
  corpus of this file cites only D2-70's own text (Título Preliminar,
  Libro I, Libro II Título I, transitorias/derogatorias).
  (LB-005; EVID-536; R65; GT-COA-FR-030..032)

### 3.3 The five-form taxonomy and name-suffix catalog (arts. 10/59/68/78/86/195 + 61/69/80/87/197/79)

- **GT-CML-FR-035:** The system shall seed the society-type catalog as
  shared dated config implementing the CLOSED list of art. 10 — a GT
  sociedad mercantil is EXCLUSIVELY one of: sociedad colectiva ·
  sociedad en comandita simple · sociedad de responsabilidad limitada
  (R.L.) · sociedad anónima (S.A.) · sociedad en comandita por
  acciones; no sixth form is configurable from this instrument (any
  non-listed mercantile entity type is outside the Code's sociedad
  universe — its later-reform possibility is the GOQ-127 watch, §7).
  (LB-006; EVID-542)
- **GT-CML-FR-036:** The system shall carry per-form liability and
  structure profiles as shared dated config (the Odoo company-type
  seed): colectiva — ALL socios respond *subsidiario, ilimitada y
  solidariamente* (subsidiarily, unlimitedly, solidarily); comandita
  simple — comanditados unlimited/solidary + comanditarios limited to
  their aportación, contributions NOT representable by títulos or
  acciones, capital fully contributed at constitution (art. 71, per the
  evidence gloss), comanditarios barred from administration (art. 73,
  per the evidence gloss); R.L. — socios
  obliged only to pay their aportaciones, only the society's patrimony
  answers (plus any pacted extra), capital divided into aportaciones
  that may NOT be incorporated into titles of any nature nor called
  acciones, capital 100% paid before the escritura (art. 81, per the
  evidence gloss), no socio industrial (art. 82, per the evidence
  gloss); S.A. — capital divided and represented by
  acciones, each accionista limited to the shares subscribed; comandita
  por acciones — mixed with comanditarios liable like S.A.
  shareholders, aportaciones represented by acciones, S.A. rules apply
  (art. 196, per the evidence gloss) and a fiscalization organ named by
  the comanditarios is mandatory (art. 199, per the evidence gloss). The R.L. profile must FORBID share-certificate
  issuance (art. 78). (LB-006; EVID-542)
- **GT-CML-FR-037:** The system shall carry the mandatory name-suffix
  catalog as shared dated config: colectiva — razón social formed from
  one partner's name and surname or two partners' surnames, with the
  obligatory legend *y Compañía Sociedad Colectiva* (abbreviable
  **y Cía. S.C.**); comandita simple — *y Compañía, Sociedad en
  Comandita* (**y Cía. S. en C.**); R.L. — the word *Limitada* or the
  legend *y Compañía Limitada* (**Ltda.** / **Cía. Ltda.**); S.A. —
  freely formed denominación with the obligatory legend *Sociedad
  Anónima* (**S.A.**); comandita por acciones — *y Compañía Sociedad en
  Comandita por Acciones* (**y Cía., S.C.A.**). Name validation accepts
  full and abbreviated forms; inscription grants exclusive use of the
  name against same/similar-object societies (art. 26, per the evidence
  gloss), with RM-side distinguishability denial consumed from
  `01_rm-surfaces.md` GT-CML-FR-012 (kin, by id).
  (LB-007; EVID-543; GT-CML-FR-012)
- **GT-CML-FR-038:** The system shall enforce the R.L. structural
  constraints: the number of socios may not exceed **twenty** (art. 79)
  — validated at partner add/join and at aportación transfer (FR-050
  kin); and no increase-of-capital deed for an R.L. until the increase
  is fully and effectively paid (art. 205, per the evidence gloss of
  EVID-551). The 20-socio cap is text as printed — its interaction with
  later SRL reforms (single-member societies are unknown to this text)
  is the GOQ-127 watch, recorded as a flag, never silently relaxed.
  (LB-007; EVID-543; EVID-551 gloss; GOQ-127)
- **GT-CML-FR-039:** The system shall implement the suffix-omission
  liability rule for R.L. as a load-bearing risk flag: if the words or
  legends of art. 80 are omitted from the society's name, the socios
  respond *de modo subsidiario, ilimitado y solidariamente* for the
  society's obligations — a company record whose R.L. name lacks the
  suffix carries the unlimited-solidary-liability exposure flag (name
  validation warns; the liability consequence is recorded, never
  emulated). (LB-007; EVID-543)
- **GT-CML-FR-040:** The system shall reject any silent modernization
  of the five-form regime (negative config row, GOQ-127 guard): bearer
  shares remain LAWFUL in the printed text (arts. 108/128 — FR-049
  carries the field); single-member SRL is unknown to this text (the
  all-shares-in-one-person situation is a DISSOLUTION cause, art.
  237.5º — FR-063); no dematerialization rule exists in the corpus —
  all such modern-reform questions stay open in the register (§7
  OQ-002) and never configure behavior.
  (LB-006; LB-007; LB-011; EVID-542/543/547; GOQ-127)

### 3.4 Constitution solemnities and personality (arts. 14-18/24)

- **GT-CML-FR-041:** The system shall implement the escritura-pública
  checklist for every structural act: constitution AND all
  modifications — prórrogas, capital increase/reduction, razón
  social/denominación change, fusión, disolución, any other reform or
  ampliation — are set in *escritura pública*; except in share
  societies (sociedades por acciones), reform of the constitutive deed
  requires the socios' UNANIMOUS vote (a validation rule on the reform
  resolution). (LB-008; EVID-544)
- **GT-CML-FR-042:** The system shall model personality as
  inscription-constituted: a sociedad has *personalidad jurídica propia
  y distinta* only when constituted per the Code AND inscribed in the
  RM; the *plazo* (term) runs from the inscription date (indefinite
  terms allowed); the testimonio of the constitutive/ampliation deed
  and its modifications must be presented to the RM **within the month
  following the escritura date** (FR-031's sociedad window) — the
  provisional→edicto→definitiva machinery and third-party-effect rules
  are owned by `01_rm-surfaces.md` (GT-CML-FR-012/013, consumed by
  id). (LB-008; EVID-544; GT-CML-FR-012/013)
- **GT-CML-FR-043:** The system shall flag pre-personality contracting
  exposure: a person contracting in the society's name before it can
  act as a juridical person is a *gestor de negocios* and remains
  PERSONALLY responsible for the contract's effects — surfaced as a
  personal-liability warning on commitments recorded before the
  personality state (with FR-062's irregularity flag as the chronic
  case). (LB-008; EVID-544)
- **GT-CML-FR-044:** The system shall emit every society-lifecycle
  event of this file (constitution, modificación, capital ±,
  disolución, liquidador appointment, fusión, transformación) as a
  publication request through the RM channel owned by
  `01_rm-surfaces.md` — channel charter GT-CML-FR-001, event tracking
  GT-CML-FR-022, templates GT-CML-FR-014..018, portal ingestion
  GT-CML-FR-023, all consumed by exact id; this file owns the EVENT
  CONTENT (what happened to which society), that file owns the CHANNEL
  (how it publishes). The art.-380 balance-publication duty consumed
  from `01_books-anchor.md` GT-COA-FR-021 discharges through the same
  channel (GT-CML-FR-018, kin). (LB-008; LB-013; GT-CML-FR-001/018/
  022/023; GT-COA-FR-021)

### 3.5 Capital and governance profiles

- **GT-CML-FR-045:** The system shall carry the reserva legal rule for
  ALL society forms as dated config: annually separate at least **5%**
  of the net utilities of each ejercicio to form the reserva legal; the
  reserve may NOT be distributed among the socios except at
  liquidation; it MAY be capitalized when it exceeds **15% of capital
  at the close of the immediately prior ejercicio**, without prejudice
  to continuing the 5% annual accrual — rates stored as dated rows
  (instrument D2-70, arts. 36/37, valid_from 1971-01-01); the
  appropriation posting surface lives in the accounting domain (kin to
  the GT-COA-FR-021 balance basis). (LB-009; EVID-545)
- **GT-CML-FR-046:** The system shall implement the distribution
  gates: (i) on capital loss, capital must be reinstated or reduced at
  least by the loss amount BEFORE any profit distribution — a blocking
  precondition on dividend workflows; (ii) distribution of utilities
  not actually obtained per the ejercicio's balance general is
  prohibited, and managers authorizing plus socios receiving such
  payments respond SOLIDARILY for restitution — a clawback exposure
  flag on distributions not backed by an approved balance.
  (LB-009; EVID-545)
- **GT-CML-FR-047:** The system shall model S.A. capital in three
  tiers — *capital autorizado* (the maximum issuable without a capital
  increase, expressed in the escritura, subscribable totally or
  partially at constitution), *capital suscrito* and *capital pagado* —
  with the issuance validation: at the moment of subscribing acciones
  it is indispensable to pay at least **25% of nominal value** (each
  subscription row records paid-in ≥ 25%). (LB-010; EVID-546)
- **GT-CML-FR-048:** The system shall carry the S.A. capital constants
  as dated config with the 1970-nominal discipline: initial paid
  capital ≥ **Q5,000** (art. 90 prints "Q5, 000.00" [sic] — R67
  amount-precision note; GOQ-126 verify-before-config, never a current
  value; rejected myth, wave set); cash aportaciones deposited in a
  bank in the society's name with the NOTARY CERTIFYING the deposit in
  the constitutive escritura (art. 92 — a constitution-checklist
  item); and the advertising rule of art. 93 — capital autorizado may
  not be advertised without simultaneously stating capital pagado,
  breach sanctioned ex officio by the RM with a multa **Q25–Q500**
  (1970-nominal exposure row, R67). (LB-010; EVID-546; R67; GOQ-126)
- **GT-CML-FR-049:** The system shall model acciones (shares) as
  *títulos de crédito* (credit titles): certificates evidence and
  transmit partner quality and rights, with the títulos-de-crédito
  provisions applying as pertinent (the títulos machinery itself is
  C5's — `03_titulos-valores-prescripcion.md`, forward ref, file +
  cluster only); default equal value and equal rights with
  deed-pactable classes; one share = one vote, multiple-vote issuance
  PROHIBITED; issuance below nominal value PROHIBITED; definitive
  títulos only when the acción is fully paid (provisional certificates
  meanwhile); certificate minimum content = the 7-item checklist of
  art. 107 (incl. the RM-inscription data of the deed); nominativas OR
  al portador at the accionista's choice unless the escritura says
  otherwise — the al-portador option is lawful AS PRINTED and carries
  the GOQ-127 modern-reform watch flag (never silently removed; the
  D-15-2026 shareholder-registry duties of FR-075 layer identification
  duties on top from 17-sep-2026 without abolishing the printed form
  rules). (LB-011; EVID-547; GOQ-127)
- **GT-CML-FR-050:** The system shall implement the Registro de
  Acciones Nominativas (register of nominative shares) as the society's
  own book for S.A.s issuing nominative acciones or provisional
  certificates, recording the seven art.-125 classes: (1º) accionista
  name and domicile + the acciones belonging to them with numbers,
  series, classes and particulars; (2º) llamamientos (calls) effected
  and payments made; (3º) transmissions effected; (4º) conversion of
  nominative/provisional into al-portador acciones; (5º) canjes (title
  exchanges); (6º) gravámenes (encumbrances) affecting the acciones;
  (7º) cancellations of these and of the títulos. The society considers
  as accionista the person INSCRIBED (nominativas) or the bearer (al
  portador); nominative transfer = endoso + registration in the book;
  al-portador transfer = mere tradition. Pre-cutover this book follows
  the 1970 art. 125 text; from 17-sep-2026 the reformed art. 125
  registry of FR-075 governs (dated rows per FR-082).
  (LB-012; EVID-548; EVID-634)
- **GT-CML-FR-051:** The system shall implement the optional
  transfer-approval workflow of art. 117 (per the evidence gloss): a
  deed clause may require administrator authorization to transfer
  nominative acciones, with a 30-day window and silence = consent —
  surfaced as an optional approval step on the share-transfer flow
  (never a default; only when the recorded escritura opts in).
  (LB-012; EVID-548 gloss art. 117)
- **GT-CML-FR-052:** The system shall implement the asamblea
  (assembly) calendar: the ORDINARY general assembly meets at least
  once a year **within the four months following the close of the
  ejercicio social**, with competence to discuss and approve/improve
  the estado de pérdidas y ganancias, the balance general and the
  administration report (the balance-publication duty that follows
  approval is GT-COA-FR-021, consumed by id, discharged via
  GT-CML-FR-018); the assembly is the órgano supremo of the society.
  Deadline = FY-close + 4 months, surfaced as an annual lifecycle
  calendar row. (LB-013; EVID-549; GT-COA-FR-021; GT-CML-FR-018)
- **GT-CML-FR-053:** The system shall implement the extraordinary-
  assembly competence list and the RM-filing duty: EXTRAORDINARY
  assemblies treat (art. 135) every modificación of the escritura
  social (incl. capital increase/reduction and prórroga del plazo),
  creation of voto-limitado or preferente acciones, emisión de
  obligaciones o bonos, own-share acquisition and nominal-value
  changes (competence list per the evidence gloss); and within **15
  days** after each extraordinary assembly the administrators must send
  the RM a **copia certificada** of the resolutions — an RM-filing task
  on the resolution record (tracked through GT-CML-FR-022, kin; actas
  of extraordinary assemblies are a 73_ fee row owned by
  `01_rm-surfaces.md` GT-CML-FR-004, kin by id).
  (LB-013; LB-022; EVID-549; EVID-568; GT-CML-FR-004/022)
- **GT-CML-FR-054:** The system shall implement the convocation model
  with the R64 verification note: as printed (pre-D18-2017 texts) the
  general assembly is convened by notices published at least TWICE in
  the Diario Oficial and in another paper of major circulation, at
  least **15 days** before the meeting, plus written notice by
  certified mail to nominative-acción holders — CURRENT mechanics:
  publication goes through the RM electronic portal (D-18-2017 art.
  12), consumed from `01_rm-surfaces.md` GT-CML-FR-001, with the
  convocatoria event class and its non-prejudice boilerplate owned
  there (GT-CML-FR-019, kin; convocatoria content never asserted from
  83_ — GOQ-131). (LB-013; EVID-549; R64; GT-CML-FR-001/019; GOQ-123
  kin)
- **GT-CML-FR-055:** The system shall implement the quorum and
  majority rules: ORDINARY assembly — legally constituted with at
  least **half** of the voting acciones represented, resolutions by at
  least the majority of votes PRESENT; EXTRAORDINARY assembly —
  legally constituted with a minimum of **60%** of the voting acciones
  represented, resolutions taken with MORE THAN **50%** of the issued
  acciones with voting right — validation rules on assembly records
  computed from the share register (FR-050), recorded as facts.
  (LB-013; EVID-549)
- **GT-CML-FR-056:** The system shall implement the actas (minutes)
  discipline: assembly actas are entered in the respective book and
  signed by the assembly's presidente and secretario (art. 153), with
  the 15-day RM certified-copy duty of FR-053 attached to each
  extraordinary acta; actas of asambleas extraordinarias also carry the
  RM-portal publication exposure through GT-CML-FR-004 (fee row, kin).
  (LB-013; LB-022; EVID-549; EVID-568)
- **GT-CML-FR-057:** The system shall implement the administración
  (administration) and fiscalización (oversight) model: administration
  = administrador único (sole administrator) or several administrators
  acting jointly as consejo de administración; elected by the general
  assembly for terms NOT exceeding **three years** (reelection
  permitted); appointment revocable by the assembly AT ANY TIME and
  administrators removable WITHOUT expression of cause (*ad nutum*);
  fiscalization flexible per the escritura — by the accionistas
  themselves, one or more contadores or auditores, or comisarios —
  designated by the annual ordinary assembly that elects the
  administrators. Officer records carry term + revocability semantics;
  appointment/removal are RM-registrable acts (art. 338.1 via
  `01_rm-surfaces.md` GT-CML-FR-011, kin; from 17-sep-2026 the
  acta-notarial requirement of reformed art. 45 — FR-079 — governs).
  (LB-014; EVID-550; GT-CML-FR-011)
- **GT-CML-FR-058:** The system shall implement the capital-increase
  workflow: assembly resolution → *escritura pública* → RM inscription
  (published through GT-CML-FR-044's channel); payment of the increase
  may be realized in cash or kind, by compensation, or **by
  capitalization of utilidades or reservas** (art. 207.3º — feeding
  FR-045's capitalization path); increases by new acciones or higher
  nominal value (art. 204, per the evidence gloss); R.L. increases
  gated by FR-038's full-payment rule. (LB-015; EVID-551)
- **GT-CML-FR-059:** The system shall implement the capital-reduction
  workflow with the creditor gate: reduction by diminishing
  aportaciones' value, all acciones' nominal value, or amortization of
  some; the resolution communicated — under the administrator's
  PERSONAL responsibility — by the fastest mail with acknowledgment to
  all known creditors; **30 days after the last publication** any
  interested party may oppose in juicio sumario; the reduction
  escritura pública may be executed ONLY after the window closes
  without opposition; the RM filing requires a NOTARIAL ACTA
  transcribing the resolution and declaring compliance with the
  creditor-notice obligation (arts. 211/212 as reformed D104-70/D42-78
  — reform tags recorded as provenance). The publication rides the RM
  channel (GT-CML-FR-001 kin) and the reduction event is a 73_
  "modificaciones mayores" fee class (GT-CML-FR-007, kin).
  (LB-015; EVID-551; GT-CML-FR-001/007)

### 3.6 Sociedades extranjeras (arts. 213-221/352/355)

- **GT-CML-FR-060:** The system shall carry the foreign-society branch
  checklist: the RM is the SOLE authorizer (art. 352 — after verifying
  the effectiveness of the assigned capital and the fianza it makes
  the definitive inscription and issues the Patente de Comercio);
  requirements include proof of due constitution, a GT *mandatario con
  representación*, **capital asignado** for GT operations plus a
  *fianza* in favor of third parties for no less than the quetzal
  equivalent of **US$50,000** (fixed by the RM — a dated threshold
  row, instrument D2-70 as reformed D62-95, US$-denominated), a
  certified copy of the last balance general and P&L, and the
  Q0.10-per-hoja timbre as the only tax on the filing (fee exposure
  kin to the 73_ sociedad-extranjera row, GT-CML-FR-004 by id).
  Temporary (≤2-year) autorización especial also requires the
  ≥US$50,000 fianza (art. 221, per the evidence gloss).
  (LB-016; EVID-552; GT-CML-FR-004)
- **GT-CML-FR-061:** The system shall carry the foreign-society
  boundary rules: the negative list of art. 220 — no GT authorization
  or registration needed when the foreign society ONLY is party to a
  gestión or juicio, opens/maintains bank accounts, or buys/sells
  through an independent agente de comercio; the withdrawal flow of
  art. 218 — certified financial statements + sworn notarial acta that
  the society met ALL tax obligations to the withdrawal date + proof
  that GT obligations are performed or guaranteed; and the 1-year
  lapse — authorization caduces if operations do not begin within one
  year of the provisional inscription (art. 355).
  (LB-016; EVID-552)

### 3.7 Irregularity, disolución, liquidación, fusión, transformación

- **GT-CML-FR-062:** The system shall implement the irregularity flag:
  a sociedad NOT inscribed in the RM — even if exteriorized as such to
  third parties — has NO legal existence and its socios respond
  solidarily and unlimitedly (art. 223); omission of the escritura
  social and prescribed solemnities produces ABSOLUTE NULLITY with the
  same liability fallback (art. 224) — company records without a
  definitive-inscription fact carry the *irregular/de hecho* flag with
  unlimited-solidary-liability semantics (and FR-043's
  gestor-de-negocios exposure for pre-personality acts).
  (LB-017; EVID-553)
- **GT-CML-FR-063:** The system shall implement the disolución-causes
  model with the >60% trigger: societies dissolve totally by any of
  the art.-237 causes — including expiry of the deed's term,
  impossibility of pursuing the main object, **loss of MORE THAN 60%
  of paid capital** (an accounting-linked trigger evaluated on the
  balance), and concentration of all acciones/aportaciones in one
  person; the general junta/asamblea decides EITHER to cure the cause
  (deed reform to continue) OR to agree dissolution — either way
  elevated to escritura pública inscribed in the RM (published via
  GT-CML-FR-044; the 60%-loss evaluation consumes balance facts of the
  accounting domain, GT-COA-FR-021 kin). (LB-018; EVID-554)
- **GT-CML-FR-064:** The system shall record the ex-officio RM
  publication of the disolución declaration — three times within
  FIFTEEN days, as printed in the Diario Oficial and a major paper
  (art. 239) — as a channel event whose CURRENT execution is the RM
  electronic portal (R64; GT-CML-FR-001 kin; the RM publishes de
  oficio — the system tracks the event, never performs it), with the
  73_ disolución fee row (GT-CML-FR-004, kin) as recorded exposure.
  (LB-018; EVID-554; R64; GT-CML-FR-001/004)
- **GT-CML-FR-065:** The system shall implement the liquidation state:
  a dissolved society enters liquidation, KEEPS its legal personality
  until liquidation concludes, and must add the words **"En
  liquidación"** to its denominación or razón social (a name-suffix
  rule on the company record, distinct from the FR-037 form suffixes);
  the liquidation term may not exceed **one year** (judicially
  extendable, per the evidence gloss) — surfaced as a lifecycle
  deadline. (LB-018; EVID-554)
- **GT-CML-FR-066:** The system shall implement the liquidator
  pipeline: liquidators appointed (deed default → majority → judge,
  per the evidence gloss) and accepting, the appointment is INSCRIBED
  at the RM, which notifies the public (three avisos within one month)
  that the society entered liquidation, naming the liquidators —
  tracked as an RM event (the 83_-observed auxiliares-register
  liquidador template and Q150 fee are owned by
  `01_rm-surfaces.md` GT-CML-FR-016/004, kin by id).
  (LB-019; EVID-555; GT-CML-FR-004/016)
- **GT-CML-FR-067:** The system shall implement the liquidation
  payment waterfall and creditor-first rule: in payments the
  liquidators observe the order (1º) *gastos de liquidación*
  (liquidation costs), (2º) *deudas de la sociedad* (society's debts),
  (3º) *aportes de los socios* (partners' contributions), (4º)
  *utilidades* (profits); and NO distribution among the socios until
  creditors are paid or the necessary sums separated — validation
  rules on liquidation-period payment/distribution records.
  (LB-019; EVID-555)
- **GT-CML-FR-068:** The system shall implement the liquidation
  close-out: the final balance general is published three times within
  fifteen days (as printed — R64; RM-portal execution via
  GT-CML-FR-018's balance-final family, kin); the approving asamblea
  is held at least ONE MONTH after the first publication; then the
  approved final balance is DEPOSITED at the RM and the inscription of
  the escritura social is CANCELLED (art. 247.11º — the registry
  close-out fact, recorded; RM cancellation slots kin to
  GT-CML-FR-025 for the taxation-recidivism path, a distinct cause).
  (LB-019; EVID-555; GT-CML-FR-018/025)
- **GT-CML-FR-069:** The system shall implement the unclaimed-funds
  escheat rule: sums belonging to accionistas unclaimed for TWO MONTHS
  from approval of the final balance general are deposited in a bank
  institution; after FIVE years with no claimant the bank adjudicates
  them gratuitously to the **Universidad de San Carlos de Guatemala** —
  a dated exposure row on liquidation distributions (pointer only to
  the retention/destruction matrix: the GOQ-124 deliverable,
  `../chart-of-accounts/03_retention-destruction-matrix.md`, forward
  ref, file + cluster only). (LB-019; EVID-555; GOQ-124 context)
- **GT-CML-FR-070:** The system shall implement the fusión (merger)
  workflow: two modes — creation of a new sociedad (all predecessors
  dissolving) or absorption — with UNIVERSAL SUCCESSION (the
  new/absorbing society acquires the dissolved societies' rights and
  obligations); process = per-society acuerdos → RM inscription via
  notarial actas → JOINT publication of the fusion agreements + last
  balance general, 3× within 15 days (as printed — R64; the
  paired-mirror-entry balance family is owned by
  `01_rm-surfaces.md` GT-CML-FR-018, kin by id) → **2-month creditor
  window** from the last publication (earlier escritura only with
  written creditor consent or bank-deposit guarantee; opposition
  suspends; court may allow with guarantee — evidence gloss) →
  escritura pública; dissenting partners may separate (art. 261, the
  guarantee surviving for pre-fusion obligations, evidence gloss).
  (LB-020; EVID-556; GT-CML-FR-018)
- **GT-CML-FR-071:** The system shall implement transformación
  (transformation) as an in-place type change: a society constituted
  under the Code may transform into ANY other mercantile society class
  and the transformed society KEEPS the same legal personality as the
  original — modeled as a company-type switch (FR-035 profile change)
  with NO new legal entity, the arts. 258-261 fusión-style protections
  applying per the evidence gloss. (LB-020; EVID-556)

### 3.8 Auxiliares de comercio (bounded — GOQ-128)

- **GT-CML-FR-072:** The system shall implement the factor model: the
  factor is constituted by mandate with representation, appointment, or
  written employment contract — and the mandato, nombramiento or
  contrato de trabajo MUST be inscribed in the RM; the factor's acts
  remain valid towards third parties until the revocatoria,
  cancelación, terminación or enajenación is RM-inscribed —
  appointment AND termination as RM-registrable events on the company
  record (art. 338.1 kin via GT-CML-FR-011). (LB-021; EVID-557;
  GT-CML-FR-011)
- **GT-CML-FR-073:** The system shall record the agentes/
  distribuidores/representantes registration surface: agentes de
  comercio act permanently for one or more principals (D8-98 text —
  no RM matrícula clause of its own); their RM registration arises
  from art. 338 literal 9 (texto D-11-2006), whose schema and
  ongoing-act classes are owned by `01_rm-surfaces.md` GT-CML-FR-011
  (consumed by id) — this file records only the contract/agency event
  on the company record that feeds it. (LB-021; EVID-557;
  GT-CML-FR-011)
- **GT-CML-FR-074:** The system shall implement the auxiliares
  licensing surface as a BOUNDED hook (GOQ-128): corredores require
  legal autorización per the respective reglamento; habitual
  comisionistas require patente per the respective reglamento; the
  reglamentos issue from MinEconomía per transitoria XI and are ABSENT
  from this corpus — no licensing requirement, fee or procedure shall
  be configured beyond a licensing-status placeholder + the GOQ-128
  flag (never invented). (LB-021; EVID-557; GOQ-128)

### 3.9 AML Código-de-Comercio reform hooks (D-15-2026; dated cutover 17-sep-2026)

- **GT-CML-FR-075:** The system shall implement the reformed CC art.
  125 shareholder registry as an odoo partner/company data surface,
  operative **17-sep-2026** (dated cutover row, R60): societies whose
  capital is divided into acciones keep a registro of acciones or
  provisional certificates with the minimum information — (1)
  individual accionistas: full name, nationality, ID-document data;
  (2) juridical-person accionistas: full razón/denominación social,
  identification and country/jurisdiction of constitution; (3)
  acciones/participaciones/aportaciones inside fideicomisos or
  patrimonial structures: identifying information plus the
  fiduciaries/administrators; (4) each accionista's PHYSICAL ADDRESS
  AND E-MAIL; (5) llamamientos effected and payments made where
  applicable; (6) transmissions of title — with the quantity of
  acciones detailed for cases (1) and (2); the registry is kept in an
  RM-AUTHORIZED BOOK, physical or electronic, under the responsibility
  of the secretary of the administration organ or the administrador
  único. From the cutover this registry GOVERNS over the 1970-text
  book of FR-050 (pre-cutover facts resolve against the 1970 art. 125;
  the seven 1970 record classes remain the operational spine, now
  loaded with the identification minimums). (LB-024; EVID-634; R60)
- **GT-CML-FR-076:** The system shall implement the RM-notice duty of
  reformed art. 125: societies must give the Registro Mercantil
  **aviso within 10 días hábiles** of the FIRST inscription in the
  shareholder registry and of every further transmission of share
  ownership — a deadline-tracked filing task per registry event
  (through GT-CML-FR-022's tracking, kin; RM-side confirmation of the
  filing state is ingested per the architecture's saas monitor, kin
  GT-CML-FR-023); the exemption row: societies whose acciones are
  inscribed for public bursátil offer are EXEMPT while the registry is
  kept within a central depositaria de valores system.
  (LB-024; EVID-634; GT-CML-FR-022/023)
- **GT-CML-FR-077:** The system shall record the art.-125 sanction as
  a dated cutover exposure row: breach sanctioned with a multa
  equivalent to **5 to 50 salarios mínimos** for actividades no
  agrícolas of circunscripción económica uno (CE1), imposed by the
  Registrador Mercantil — the SMM base is resolved by consuming
  `gt/requirements/payroll/03_minimum-wage.md` by exact id
  (**GT-PAY-FR-058**, the six-cell dated rows loaded from
  `salario_minimo.csv` — CE1 No Agrícola; **GT-PAY-FR-063**, the
  art.-9 selector: non-labor matters → CE1 no-agrícola rate) — the
  amounts are NEVER hardcoded here (the payroll rows carry their own
  vintage caveats, GOQ-11/GOQ-77/78, kin); this is the ONLY
  quetzal-denominated fine of the D-15-2026 regime (all other fines
  are US$ — wave constraint), recorded exposure only, never computed
  or charged. (LB-024; EVID-634; GT-PAY-FR-058; GT-PAY-FR-063; R60)
- **GT-CML-FR-078:** The system shall implement the RM confidential-
  database guard: the RM must keep a secure CONFIDENTIAL electronic
  database of the shareholder-registry information, which it may
  provide ONLY to the Superintendencia de Bancos and the Ministerio
  Público — the system's surfaces never expose, publish or export the
  shareholder-registry data beyond the RM-aviso filing of FR-076 and
  the registry-keeper surfaces (confidentiality flag on the data
  model; the C6 AML file owns the SB/MP-facing machinery — forward
  ref, file + cluster only). (LB-024; EVID-634)
- **GT-CML-FR-079:** The system shall implement reformed CC art. 45
  (operative 17-sep-2026): the appointment and removal of the
  administration organ of ALL sociedades mercantiles is done by
  resolución de los socios and must be inscribed in the RM upon
  presentation of a NOTARIAL ACTA — layering onto FR-057's
  assembly-elected officer model a mandatory acta-notarial filing form
  for the appointment/removal event (pre-cutover facts resolve against
  the 1970 arts. 162/178 texts; art. 338.1 registration kin via
  GT-CML-FR-011). (LB-024; LB-014; EVID-634; EVID-550; R60)
- **GT-CML-FR-080:** The system shall implement the art.-121
  transitory sanction with RM-ingested state (saas): all members of
  the administration organ (with or without legal representation) must
  be inscribed in the RM within **six months from 17-sep-2026** (i.e.
  by 17-mar-2027); societies failing this may perform **NO operation
  in the Registro Mercantil** until the registration request for ALL
  members is filed — the block state is INGESTED from RM-side facts
  (D2 dual-validation; the system never emulates the registrar), and
  the deadline surfaces as a cutover-calendar exposure row on every
  sociedad. (LB-024; EVID-634; R60)
- **GT-CML-FR-081:** The system shall implement the art.-120
  transitory compliance calendar: societies must comply with the
  reformed art.-125 obligations within a maximum of **one year from
  17-sep-2026** (i.e. by 17-sep-2027) and REMIT to the RM a
  certificación of the information of numerals 1)-3) (shareholder
  identification incl. trust/structure data) — a cutover-keyed
  deadline + filing checklist row feeding FR-075/FR-076.
  (LB-024; EVID-634; R60)
- **GT-CML-FR-082:** The system shall store every EVID-634 row of
  this section as D16 dated cutover rows keyed **2026-09-17**
  (instrument D-15-2026; R60 — never 17-jun-2026): pre-cutover facts
  resolve against the 66_ printed texts (FR-050's 1970 registry;
  FR-057's 1970 officer texts), post-cutover facts against the
  reformed arts. 45/125; transitorias 116-124 run from the cutover
  (FR-080/FR-081 calendars); snapshot-on-write with instrument
  provenance. The AML machinery itself (personas obligadas, KYC/UBO,
  reporting, fines architecture) is the C6 file
  `04_aml-compliance.md` — forward ref, file + cluster only; this
  file owns only the CC-side duties. (LB-024; EVID-634; R60)

### 3.10 Notarial-registry spine and provenance rows

- **GT-CML-FR-083:** The system shall carry the registry-filing
  attachment checklist per lifecycle event (the notarial-registry
  spine): testimonio of the escritura (constitution/modification);
  notarial acta transcribing the resolution + creditor-notice
  compliance declaration (capital reduction, art. 211); notarial
  actas transcribing each society's fusion acuerdo (art. 259);
  certified copy of extraordinary-assembly resolutions (art. 153 3º
  ¶); protocolized inventory for non-cash aportaciones (art. 27 —
  non-cash contributions pass to the society's dominion without
  tradición, detailed and valued in the deed or the partner-accepted
  protocolized inventory); notary notice of shareholder-vote pactos to
  the society and the RM with razonado share títulos (art. 116);
  legalized signatures for private documents (art. 345 — provenance
  attribute owned by GT-CML-FR-013, kin). (LB-022; EVID-568;
  GT-CML-FR-013)
- **GT-CML-FR-084:** The system shall record the provenance rows of
  the transitorias/derogatorias: pre-1971 societies continued under
  their prior laws (transitoria I); the original adaptation window
  (enrollment of all arts. 334-338 subjects by 30-Jun-1974 with four
  prorrogas — count per the evidence gloss, and the court/office bar on
  non-razonado documents from
  1-Mar-1971 — transitoria VII) as historical context only; and the
  RM→tax-registry linkage of derogatoria II (society enrollment at the
  revenue directorate required RM-inscription certifications + the
  opening balance within 30 days of the definitive RM inscription —
  ancestor of the modern RM/RTU interplay, recorded as lineage; the
  adaptation-deed 1/3-arancel honorarios discount is owned by
  `01_rm-surfaces.md` GT-CML-FR-002, kin by id).
  (LB-023; EVID-569; GT-CML-FR-002)
- **GT-CML-FR-085:** The system shall record the books/contador kin
  pointers for sociedades (consumed by id, never re-derived): every
  sociedad mercantil must operate its accounting through Contadores
  (`01_books-anchor.md` GT-COA-FR-014 — art. 371 texto D-58-96); the
  per-ejercicio balance-publication duty of art. 380 (GT-COA-FR-021)
  discharges through the C3 channel (GT-CML-FR-018); the RM-side
  cancellation surface for CT art.-85 recidivism (GT-CML-FR-025
  consuming GT-TAX-FR-216/217) is the taxation-LB-012 kin tie-in —
  separate from this file's liquidation close-out cancellation
  (FR-068, distinct cause and distinct filing).
  (LB-013; LB-019; GT-COA-FR-014; GT-COA-FR-021; GT-CML-FR-018/025)

## 4. Data Model

Layer semantics: the society-type profiles, suffix catalog, capital
constants, thresholds and cutover rows are dated config shared across
the architecture; the partner/company classification surfaces,
lifecycle calendars, resolution tracking, share register and
shareholder registry live in the Odoo client; RM-side ingestion of
filing states (the art.-121 operation block) lives on the SaaS side.
The system records compliance facts and prepares filings — it never
emulates the Registro Mercantil (its resolutions are ingested as
facts) and never computes legal effects (liability flips, nullity,
personality). Machine-readable sidecars: the society-type profile and
suffix catalog warrant a CSV/JSON sidecar only when seeded for load;
the 1970-nominal and cutover values are D16 dated config rows, not
free data — amounts are stored as printed with [sic] provenance and
never normalized.

**Society-type profile (l10n_gt_commerce.society_type — shared dated
config, instrument D2-70, valid_from 1971-01-01):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.society_type | form | select | colectiva · comandita_simple · responsabilidad_limitada · anonima · comandita_por_acciones (closed list — no sixth form) | FR-035 |
| l10n_gt_commerce.society_type | liability_profile | select | all_unlimited_solidary (colectiva) · mixed_no_shares (comandita simple: comanditados unlimited/solidary, comanditarios ≤ aporte) · patrimony_only (R.L. + pacted extra) · limited_to_shares (S.A.) · mixed_with_shares (comandita por acciones, S.A. rules art. 196) | FR-036 |
| l10n_gt_commerce.society_type | shares_allowed | boolean | false for colectiva/comandita simple/R.L. (R.L. aportaciones may not be titles nor called acciones); true for S.A./comandita por acciones | FR-036 |
| l10n_gt_commerce.society_type | suffix_rule | config | y Cía. S.C. · y Cía. S. en C. · Ltda. / Cía. Ltda. · S.A. · y Cía., S.C.A. (full + abbreviated forms; razón-social vs denominación formation; omission-liability flag for R.L.) | FR-037, FR-039 |
| l10n_gt_commerce.society_type | structural_constraints | config | R.L.: max_socios = 20, capital 100% paid pre-escritura, no socio industrial, no increase deed until fully paid; comandita simple: capital fully contributed at constitution, comanditarios barred from administration; comandita por acciones: mandatory comanditarios-named fiscalization organ | FR-036, FR-038 |

**Dated values (l10n_gt_commerce.dated_value — shared, D16 rows;
1970-nominal set flagged GOQ-126/R67, never indexed, never
current-value asserted):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.dated_value | key | char | cc_matricula_threshold (Q2,000, art. 334) · cc_sa_min_paid (Q5,000 [printed "Q5, 000.00" sic], art. 90) · cc_registrador_multa (Q25–Q1,000, art. 356) · cc_art93_multa (Q25–Q500) · cc_reserva_legal_min (5%) · cc_reserva_legal_cap (15%) · cc_sa_subscription_min_paid (25%) · cc_extranjera_fianza (US$50,000-eq, arts. 215/221 D62-95 text) — instrument D2-70, valid_from 1971-01-01, re_verify (GOQ-126) | FR-030, FR-045, FR-047, FR-048, FR-033, FR-060 |
| l10n_gt_commerce.dated_value | key (cutover) | char | aml_cc125_smm_fine (5–50 × SMM CE1 no-agrícola; base resolved via GT-PAY-FR-058/GT-PAY-FR-063, never hardcoded) — instrument D-15-2026 art. 113, valid_from 2026-09-17 (R60) | FR-077 |
| l10n_gt_commerce.dated_value | deadline rows | config | matrícula windows (1 month; sociedades from escritura) · testimonio filing (1 month) · RM copy of art.-135 resolutions (15 days) · convocation (≥15 days + certified mail) · ordinary assembly (FY close + 4 months) · capital-reduction opposition (30 days) · liquidation term (1 year) · final-balance assembly (≥1 month after first publication) · unclaimed sums (2 months → bank; 5 years → USAC) · fusión creditor window (2 months) · art.-125 RM aviso (10 días hábiles) · art. 121 admin registration (6 months from 2026-09-17) · art. 120 art.-125 compliance (1 year from 2026-09-17) · extranjera operations start (1 year) | FR-031, FR-042, FR-052, FR-053, FR-054, FR-059, FR-065, FR-068, FR-069, FR-070, FR-076, FR-080, FR-081, FR-061 |

**Partner/company surfaces (odoo):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner | gt_comerciante_class | select + basis | comerciante_individual (art. 2 test − art. 9 list + threshold flag) · sociedad_mercantil (art. 3 override) · no_comerciante · state/public entity note (art. 13 gloss) | FR-026..029 |
| res.partner | gt_matricula_state | select + dates | obligation flag · window deadline · enrolled (RM coordinates consumed from GT-CML-FR-010) · patente_issued + display_attestation | FR-030..032 |
| res.partner | gt_exposure_flags | flags | registrador multa Q25–Q1,000 exposure (kin GT-COA-FR-020) · gremial lockout precondition · R.L. suffix-omission unlimited-liability flag · irregular/de hecho flag (no legal existence, unlimited solidary) · pre-personality gestor-de-negocios warning · "En liquidación" name suffix + ≤1-year term · art.-121 RM-operation block (ingested) | FR-033, FR-039, FR-043, FR-062, FR-065, FR-080 |
| res.company | gt_sa_capital | monetary ×3 | autorizado · suscrito · pagado (validation: paid ≥ 25% of nominal per subscription; min paid Q5,000 dated row) + notary-certified bank-deposit checklist item + paired autorizado/pagado advertising rule | FR-047, FR-048 |
| res.company | gt_lifecycle_state | select | en_constitución (escritura → RM filing ≤1 month) · inscrita (personality + plazo from inscription — states consumed from GT-CML-FR-012) · disuelta_en_liquidación ("En liquidación", waterfall active) · liquidada (final balance deposited + inscription cancelled) · fusionada/absorbida · transformada (same personality, type switched) | FR-042, FR-044, FR-063..071 |

**Registro de Acciones Nominativas + reformed art.-125 shareholder
registry (odoo; dated rows keyed 2026-09-17 per FR-082):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.share_register_entry | record_class | select | ownership (name + domicile; share numbers/series/classes/particulars) · llamamientos_pagos · transmisiones · conversiones_al_portador · canjes · gravamenes · cancelaciones — the 1970 art.-125 seven classes (pre-cutover spine) | FR-050 |
| l10n_gt_commerce.share_register_entry | transfer_mechanics | select | nominativa = endoso + book registration (optional art.-117 approval window, 30 days, silence = consent) · al_portador = mere tradition | FR-050, FR-051 |
| l10n_gt_commerce.shareholder_registry | identification_minimum | fields | individual: full name, nationality, ID-document data + share quantity · juridical: full razón/denominación, identification, constitution jurisdiction + share quantity · trust/structure holdings: identification + fiduciaries/administrators · EVERY accionista: physical address + e-mail · llamamientos/pagos · transmissions — reformed art. 125, valid_from 2026-09-17 | FR-075 |
| l10n_gt_commerce.shareholder_registry | book_authorization · keeper | config + select | RM-authorized book, physical or electronic · keeper = secretary of the órgano de administración or administrador único | FR-075 |
| l10n_gt_commerce.shareholder_registry | rm_notice_state | select + dates | per-event aviso ≤10 días hábiles (first inscription + each transmission); public-offer/central-depositary exemption flag; RM filing-state confirmation ingested (saas monitor, kin GT-CML-FR-023) | FR-076 |
| l10n_gt_commerce.shareholder_registry | confidentiality | flag | data accessible ONLY via the RM-aviso path; never exported/published elsewhere (RM database = SB + MP only) | FR-078 |

**Asamblea/administración tracking (odoo):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.asamblea | type · quorum | select + computed-recorded | ordinaria (≤4 months post-cierre; 50% quorum, majority-present resolutions) · extraordinaria (art.-135 competence list; 60% quorum, >50% of all issued voting shares) — computed from the share register, recorded as facts | FR-052, FR-053, FR-055 |
| l10n_gt_commerce.asamblea | convocation · actas | config + fields | 2× publication ≥15 days ahead + certified mail to nominatives (as printed, R64 note; channel = GT-CML-FR-001) · actas book + presidente/secretario signatures · RM certified-copy task ≤15 days per extraordinary assembly | FR-054, FR-056 |
| l10n_gt_commerce.officer | term · revocability · filing | fields | term ≤3 years, renewable · revocable ad nutum / removable without cause · from 2026-09-17: socios resolution + RM inscription via acta notarial (reformed art. 45); art.-121 registration deadline + RM-operation block (ingested) | FR-057, FR-079, FR-080 |
| l10n_gt_commerce.capital_change | flow | select | increase (resolution → escritura → RM; funding incl. capitalization of utilidades/reservas) · reduction (creditor notice under administrator's personal responsibility → publication → 30-day opposition gate → escritura; acta notarial filing) | FR-058, FR-059 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2, wave defaults): `shared`
= society-type profiles, suffix catalog, capital/threshold constants
and cutover rows — dated config both sides must honor identically;
`odoo` = the partner/company classification surfaces, lifecycle
calendars, asamblea/officer tracking, share register and shareholder
registry in the LGPL client; `saas` = RM-side ingestion of filing
states (the art.-121 operation block; D2 dual-validation on the shared
dated rows — the RM-portal snapshot ingestion itself is
`01_rm-surfaces.md` GT-CML-FR-023, consumed by id). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-026 | shared | calificación catalog config | art. 2 four-class list + two-element test | Closed list as printed; GOQ-123 kin |
| FR-027 | shared | calificación catalog config | art. 9 negative list + art. 6 capacity | art. 13 State note (gloss) |
| FR-028 | shared | society_type → comerciante override | art. 3 entity-type rule | Object irrelevant; no activity test |
| FR-029 | odoo | res.partner | gt_comerciante_class + basis | Drives FR-030 obligation flags |
| FR-030 | shared | l10n_gt_commerce.dated_value | cc_matricula_threshold Q2,000 | 1970-nominal, GOQ-126/R67; valid_from 1971-01-01, no valid_to |
| FR-031 | odoo | res.partner calendar rows | 1-month windows | Sociedad window keyed to escritura date; GT-CML-FR-012 tracking |
| FR-032 | odoo | res.partner (establishment) | patente fact + display flag | No patente fee (GT-CML-FR-006 kin) |
| FR-033 | odoo | res.partner exposure | multa Q25–Q1,000 + gremial lockout | Kin GT-COA-FR-020; R62 track separation; R67 band |
| FR-034 | shared | citation-guard config | R65 D2946 appendix rule | Consumes GT-COA-FR-030..032 by id |
| FR-035 | shared | l10n_gt_commerce.society_type | five-form closed list | GOQ-127 watch flag |
| FR-036 | shared | l10n_gt_commerce.society_type | liability/structure profiles | R.L. forbids share certificates |
| FR-037 | shared | society_type.suffix_rule | 5 suffixes + abbreviations | Full + abbreviated accepted; art. 26 exclusivity |
| FR-038 | shared | society_type.structural_constraints | R.L. ≤20 socios; art. 205 gate | GOQ-127 on the cap |
| FR-039 | shared | suffix_rule omission flag | unlimited-solidary liability exposure | Recorded consequence, never emulated |
| FR-040 | shared | negative-config guard | no silent modernization | GOQ-127; bearer shares lawful as printed |
| FR-041 | odoo | lifecycle checklist | escritura pública per structural act | Unanimity for non-share societies |
| FR-042 | odoo | res.company.gt_lifecycle_state | personality from inscription; testimonio ≤1 month | GT-CML-FR-012/013 consumed by id |
| FR-043 | odoo | res.partner exposure | gestor-de-negocios warning | Pre-personality commitments |
| FR-044 | odoo | lifecycle event → channel | publication request per event | GT-CML-FR-001/018/022/023 by id; GT-COA-FR-021 |
| FR-045 | shared | l10n_gt_commerce.dated_value | reserva 5% / cap 15% | Posting surface in accounting domain (kin) |
| FR-046 | odoo | distribution workflow gates | capital-loss restitution + approved-balance backing | Clawback exposure flag |
| FR-047 | odoo | res.company.gt_sa_capital | autorizado/suscrito/pagado; ≥25% per subscription | Validation recorded as fact |
| FR-048 | shared | dated_value + checklist | Q5,000 min [sic]; notary-certified deposit; art. 93 rule | GOQ-126/R67; multa Q25–Q500 exposure |
| FR-049 | odoo | share/certificate model | art.-107 7-item content; issuance validations | Al portador lawful (GOQ-127 flag); C5 forward ref |
| FR-050 | odoo | share_register_entry | 1970 art.-125 seven classes | Cutover succession per FR-082 |
| FR-051 | odoo | transfer workflow | optional art.-117 approval, 30 days, silence = consent | Opt-in from the recorded escritura only |
| FR-052 | odoo | asamblea calendar | FY close + 4 months | GT-COA-FR-021/GT-CML-FR-018 kin |
| FR-053 | odoo | asamblea resolution tracking | art.-135 list; RM copy ≤15 days | GT-CML-FR-004/022 kin |
| FR-054 | odoo | convocation workflow | 2× publication ≥15 days + certified mail | R64 note; GT-CML-FR-001/019; GOQ-131/123 kin |
| FR-055 | odoo | asamblea quorum validation | 50%/majority-present; 60%/>50% issued | Computed from FR-050 register |
| FR-056 | odoo | actas book | signatures + RM-copy task | — |
| FR-057 | odoo | officer model | ≤3-year terms; ad nutum; flexible fiscalización | GT-CML-FR-011 kin; FR-079 layer from cutover |
| FR-058 | odoo | capital_change flow (increase) | escritura → RM; capitalization funding | Feeds FR-045 capitalization path |
| FR-059 | odoo | capital_change flow (reduction) | creditor gate, 30-day opposition, acta notarial | D104-70/D42-78 tags as provenance; GT-CML-FR-001/007 kin |
| FR-060 | odoo | res.company checklist (extranjera) | mandatario; capital asignado; fianza ≥US$50,000; Q0.10/hoja | GT-CML-FR-004 kin (Q1,500 fee row) |
| FR-061 | odoo | extranjera boundary rules | art. 220 negative list; withdrawal; 1-year lapse | — |
| FR-062 | odoo | res.partner flag | irregular/de hecho; unlimited solidary | — |
| FR-063 | odoo | lifecycle disolución causes | 7 causes; >60% paid-capital-loss trigger | GT-COA-FR-021 kin (balance facts) |
| FR-064 | odoo | channel event (RM ex officio) | 3×/15-day publication tracked | R64; GT-CML-FR-001/004 kin |
| FR-065 | odoo | res.company lifecycle | "En liquidación" suffix; ≤1-year term | Distinct from FR-037 form suffixes |
| FR-066 | odoo | liquidator pipeline | RM-inscribed appointment; RM avisos 3×/1 month | GT-CML-FR-004/016 kin |
| FR-067 | odoo | waterfall validation | 4-step order; creditor-first | — |
| FR-068 | odoo | close-out tracking | final balance 3×/15d; assembly ≥1 month; RM deposit + cancellation | GT-CML-FR-018/025 kin |
| FR-069 | odoo | dated exposure row | 2 months → bank; 5 years → USAC | GOQ-124 matrix pointer (file + cluster) |
| FR-070 | odoo | fusión workflow | actas → RM → joint publication → 2-month window → escritura | Mirror entries via GT-CML-FR-018 kin |
| FR-071 | odoo | transformación | in-place type switch; same personality | arts. 258-261 protections (gloss) |
| FR-072 | odoo | factor events | appointment + termination RM-inscribed | GT-CML-FR-011 kin |
| FR-073 | odoo | agency event surface | art. 338.9 (D-11-2006) registration | GT-CML-FR-011 consumed by id |
| FR-074 | shared | bounded licensing hook | placeholder + GOQ-128 flag | Reglamentos absent — never invent |
| FR-075 | odoo | shareholder_registry | reformed art.-125 identification minimums | valid_from 2026-09-17 (FR-082 rows) |
| FR-076 | odoo | rm_notice_state per event | aviso ≤10 días hábiles; depositary exemption | saas ingestion kin GT-CML-FR-023 |
| FR-077 | shared | dated_value (cutover) | 5–50 SMM CE1 no-agrícola | GT-PAY-FR-058/GT-PAY-FR-063 by id; never hardcoded |
| FR-078 | odoo | confidentiality guard | no export beyond RM-aviso path | C6 forward ref (file + cluster) |
| FR-079 | odoo | officer filing form | socios resolution + acta notarial | Pre-cutover: 1970 arts. 162/178 |
| FR-080 | saas | RM-ingested block state | art. 121: registration ≤17-mar-2027 else block | Ingested facts; D2 dual-validation; never emulated |
| FR-081 | odoo | cutover compliance calendar | art. 120: ≤17-sep-2027 + certification 1)-3) | Feeds FR-075/FR-076 |
| FR-082 | shared | cutover row discipline | all EVID-634 rows keyed 2026-09-17 | R60; pre/post fact resolution; C6 forward ref |
| FR-083 | odoo | attachment checklist | testimonio/actas/certified copies/protocolized inventory | GT-CML-FR-013 kin |
| FR-084 | shared | provenance rows | transitorias I/VII; derogatoria II RM→tax chain | GT-CML-FR-002 kin (1/3 arancel) |
| FR-085 | shared | kin-pointer row | GT-COA-FR-014; GT-COA-FR-021; GT-CML-FR-018/025 | Consumed by id, never re-derived |

Version-regime notes (D12/D15/D16): the 66_-sourced rows resolve
as-of the domain anchor date with instrument provenance (D2-70 as
consolidated to 30-05-2006) and the GOQ-123 kin verification note —
load-bearing through R64 on every printed publication text (current
channel = D-18-2017 art. 12 via `01_rm-surfaces.md` GT-CML-FR-001);
the 1970-nominal amounts (Q2,000; Q5,000 [sic]; Q25–Q1,000;
Q25–Q500) are D16 dated rows with the GOQ-126 verify-before-config
flag and no valid_to supersession asserted from this corpus; the
EVID-634 rows are regime-cutover rows keyed 2026-09-17 (R60 —
pre-cutover facts against 66_, post against 77_'s reformed CC arts.
45/125; transitorias 116-124 run from the cutover);
snapshot-on-write stores the resolved value + instrument on every
recorded fact; no legal effect (personality, liability flips,
nullity, the RM-operation block) is ever computed — RM resolutions
are ingested as facts.

## 6. Acceptance Criteria

- **AC-001:** Given a partner record, when the comerciante
  classification is evaluated, then an individual resolves through the
  cumulative own-name + profit test over the four art.-2 classes minus
  the art.-9 exclusions with the Q2,000 dated-threshold flag
  (GOQ-126), while ANY mercantile-form society resolves comerciante
  whatever its object — and the classification carries basis and
  as-of date. (FR-026..029)
- **AC-002:** Given the matrícula config, when inspected, then the
  Q2,000 threshold row reads instrument D2-70 / valid_from 1971-01-01
  with the GOQ-126 re-verify flag and NO current-value assertion, the
  registrador band reads Q25–Q1,000 as 1970-nominal exposure, and the
  1-month windows key on the recorded escritura/constitution dates
  with reminders — never computed sanctions. (FR-030, FR-031, FR-033)
- **AC-003:** Given the society-type catalog, when a sixth mercantile
  form or a share-bearing R.L. is attempted, then both are rejected;
  each of the five forms carries its liability profile, mandatory
  suffix (full + abbreviated forms accepted) and structural
  constraints (R.L. ≤ 20 socios, no titles, capital fully paid
  pre-escritura); and an R.L. name without "Limitada"/"Cía. Ltda."
  raises the unlimited-solidary-liability flag. (FR-035..039)
- **AC-004:** Given a sociedad without a definitive-inscription fact,
  when its record is inspected, then it carries the irregular/de hecho
  flag with unlimited-solidary-liability semantics and the
  pre-personality gestor warning, and no personality-derived behavior
  (plazo, exclusivity) is active. (FR-042, FR-043, FR-062)
- **AC-005:** Given an S.A. capital record, when a subscription is
  entered at less than 25% of nominal paid, or an advertisement states
  autorizado without pagado, then validation/exposure rows fire; the
  Q5,000 minimum row prints the art.-90 [sic] provenance with the
  GOQ-126 flag; and the notary-certified bank-deposit checklist item
  is present at constitution. (FR-047, FR-048)
- **AC-006:** Given a fiscal-year close, when the asamblea calendar
  runs, then the ordinary-assembly deadline = close + 4 months with
  the balance/publication chain consumed from GT-COA-FR-021 via
  GT-CML-FR-018; and after each extraordinary assembly a 15-day
  RM-certified-copy task appears with its completion state tracked.
  (FR-052, FR-053, FR-044)
- **AC-007:** Given a share transfer on the register, when processed,
  then nominative transfers require endoso + book registration (with
  the optional art.-117 30-day approval only if the escritura opts
  in), the seven art.-125 record classes update, and — from
  2026-09-17 — the reformed-art.-125 identification minimums
  (incl. physical address + e-mail and trust/fiduciary data) are
  mandatory fields with a 10-días-hábiles RM-aviso task per
  transmission. (FR-050, FR-051, FR-075, FR-076)
- **AC-008:** Given the art.-125 fine exposure, when resolved, then
  the amount derives from the payroll wave's dated rows consumed by
  exact id (GT-PAY-FR-058 via `salario_minimo.csv`; GT-PAY-FR-063
  selector) — no hardcoded SMM value exists anywhere in this file's
  config — and the row is recorded exposure, never charged.
  (FR-077)
- **AC-009:** Given the cutover regime, when a fact dated before
  2026-09-17 is evaluated, then it resolves against the 66_ printed
  texts (1970 art.-125 register; arts. 162/178 officer texts); the
  same fact after the cutover resolves against the reformed arts.
  45/125, with the art.-121 registration deadline (17-mar-2027) and
  art.-120 compliance deadline (17-sep-2027) surfaced as calendars and
  the RM-operation block INGESTED from RM facts, never emulated.
  (FR-079..082)
- **AC-010:** Given a society entering liquidation, when the
  lifecycle runs, then the name gains "En liquidación", the ≤1-year
  term clock starts, payments validate against the 4-step waterfall
  with the creditor-first rule, and the close-out requires the
  published final balance (3×/15 days, RM-portal channel), the
  assembly ≥1 month after first publication, and the RM deposit +
  inscription-cancellation facts; unclaimed sums carry the 2-month
  bank-deposit and 5-year USAC-escheat exposure rows.
  (FR-065..069)
- **AC-011:** Given a fusión, when executed, then both modes are
  supported with universal succession, the acuerdos are filed via
  notarial actas at the RM, the joint publications run 3×/15 days as
  paired mirror entries through the C3 channel, and the escritura is
  blocked until the 2-month creditor window closes (or written
  consent is recorded). (FR-070; GT-CML-FR-018 kin)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md`
§C); this file owns **GOQ-126/GOQ-127/GOQ-128** for the C4 rows, with
GOQ-123 as kin on every 66_ citation family (owned by
`01_books-anchor.md` GT-COA-FR-031) and GOQ-12 as kin on the
reglamento-watch discipline of the EVID-634 cutover rows (C6 owns the
threshold CRs). GOQ-124 (retention/destruction matrix) is the Task 7
deliverable — context only here: FR-069's USAC-escheat row feeds its
matrix by pointer (`../chart-of-accounts/03_retention-destruction-
matrix.md`, forward ref, file + cluster only). GOQ-131 rides the
convocatoria-stub guard consumed from `01_rm-surfaces.md` GT-CML-FR-
019 (kin). The payroll vintage caveats (GOQ-11 absence rows; GOQ-77/78
words-govern) ride the SMM rows consumed by id (GT-PAY-FR-058/063) —
nothing outside the register is treated as an open question.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-126 (owned): "Matrícula Q2,000 / S.A. Q5,000 1970-nominal thresholds: whether later instruments or RTU practice supersede — verify before config." FR-030/FR-048 store both as dated rows with the verify flag; no current value is asserted and no validation hard-fails on the 1970 figures until verified against modern instruments/RTU. | no | GT synthesis wave S-GT5 → W6 partner ask (acquisition queue: current arancel/RTU practice) | open |
| OQ-002 | GOQ-127 (owned): "Company-type modern reforms absent: bearer shares still lawful (108/128) vs dematerialization; R.L. 20-socio cap vs later SRL reforms (single-member) — outside corpus." FR-040/FR-038/FR-049 carry the watch flags; the printed regime configures and no silent modernization ships; any post-1970 company-law reform re-opens FR-035..040/049/050. | no | GT synthesis wave S-GT5 → W6 partner ask | open |
| OQ-003 | GOQ-128 (owned): "Auxiliares licensing reglamentos (corredor/comisionista patente/martillero, MinEconomía per transitoria XI) not in corpus." FR-074 keeps the licensing surface a bounded placeholder + flag; no requirement, fee or procedure is invented. | no | GT synthesis wave S-GT5 (acquisition queue) | open |
| OQ-004 | GOQ-123 (kin): "CCom post-May-2006 reform watch: consolidation horizon D-11-2006; later reforms absent (known: art. 343 = D-18-2017) — verification note rides every 66_ citation." This file's 66_ rows are the pre-D18-2017 print where they touch publications (arts. 138/239/251/259 — R64 note; channel = GT-CML-FR-001); the D-15-2026 CC reforms of arts. 45/125 ARE in corpus and handled as cutover rows (FR-075..082) — any further post-2006 reform of the sociedad/RM titles re-opens the affected FRs. | no | GT synthesis wave S-GT5 → W6 partner ask (owner: `01_books-anchor.md` FR-031; this file kin-cites) | open |
| OQ-005 | GOQ-12 (kin): "AML reglamento watch ≈17-mar-2027 defers ALL operational thresholds" — the CC-side rows here are statutory (art.-125 registry, 10-días-hábiles notices, 5–50 SMM fine, art.-121 block) and NOT deferred, but any reglamento operationalization (book formats, aviso forms, SMM computation detail) lands with the C6 owner and may re-open FR-075..081. | no | GT synthesis wave S-GT5 → C6 writer (`04_aml-compliance.md`, forward ref, file + cluster) | open |
