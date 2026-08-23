# GT — Commercial-legal — Títulos valores: título de crédito framework, circulation/endoso, protesto/aval, instrument species, FACTURA CAMBIARIA + FEL-lineage guard, and the mercantile prescription matrix (C5)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-22 (GOQ-147 backfill: Código Civil 92_ EVID-931..951) |

## 1. Purpose

This file is the FIFTH of the S-GT5 chart-of-accounts/commercial-legal
wave and owns cluster **C5**, the *títulos valores* (negotiable
instruments / securities) domain plus the mercantile *prescripción*
(prescription) ladder. It converts into requirements: the *título de
crédito* (credit instrument / security) framework — the literal +
autonomous incorporated right of art. 385, the five general requisites
of art. 386 with the omission-does-not-kill-the-negocio rule, and the
words-over-figures / lesser-sum amount rules of art. 388; the
circulation taxonomy — *nominativos* (registered: endoso + inscription
in the creator's register), *a la orden* (to order: endoso + delivery,
blank endoso, the propiedad/procuración/garantía endorsement classes,
unbroken-chain legitimacy) and *al portador* (bearer: mere tradition,
with the money-paper restriction); *protesto* (formal protest) with the
*sin protesto, sin gastos* waiver and *aval* (guarantee on an
instrument); the instrument species as bounded profiles — *letra de
cambio* (bill of exchange: four maturity forms, 6% default interest),
*pagaré* (promissory note), *cheque* (bank-drawn only, always payable
at sight, 15-calendar-day presentation window, revocation only after
the window, 6-month prescription), *obligaciones/debentures*,
*certificado de depósito/bono de prenda*, *carta de porte/conocimiento
de embarque*, *cédulas hipotecarias*, *bonos bancarios*,
*certificados fiduciarios* (existence-level, corpus-bounded); the
**FACTURA CAMBIARIA** (articles 591-604: seller-drawn título on real
delivery of goods, acceptance by return of the original within 5 días
same plaza / 15 días different plaza, dispatch clocks 3 días /
≤48 h, protest within 2 días hábiles, 5-year merchant retention of
issued facturas or copies, omission of the four added requisites →
valid *negocio jurídico* but loss of *título de crédito* character)
together with the **FEL-lineage guard** (field-level ancestry ONLY —
serial number, buyer identity/domicile, goods, unit and total prices —
never citing FEL duties to arts. 591-604); and the **PRESCRIPTION
MATRIX** — one FR per clock: cambiaria directa 3 y / regreso 1 y /
obligado recourse 6 m; enriquecimiento 1 y; cheque 6 m; cheques de
viajero 2 y; debentures intereses 5 y / principal 10 y; transporte
  6 m; seguro 2 y; fianza 2 y; the D2946 old-code 5-year catch-all
  (R65-flagged); and the load-bearing finding that CCom enacts NO
  general commercial prescription period (art. 1 defers to Civil law)
  — whose Civil fallback is NOW corpus-anchored (92_, GOQ-147
  resolved): CC art. 1508's "cinco años, contados desde que la
  obligación pudo exigirse" default behind the art.-1516 special-law
  gateway — consumed forward by the Task 7 retention/destruction
  matrix and by receivables/payables aging surfaces.

It does **not** cover: the books/PCGA anchor, document-conservation
floor and destruction-gate predicate
(`../chart-of-accounts/01_books-anchor.md` GT-COA-FR-026..029 — the
destruction gate GT-COA-FR-028 consumes THIS file's per-instrument
prescription keys by id; the matrix computation lives in Task 7's
file); the consolidated retention/destruction max-per-object matrix
(`../chart-of-accounts/03_retention-destruction-matrix.md`, the
GOQ-124 deliverable, Task 7 — forward ref, file + cluster only; this
file supplies its commercial prescription rows); tax prescription
(`../taxation/06_ct-procedures.md` GT-TAX-FR-232 — prescription-
anchored tax retention is a DIFFERENT clock, cited by id, never
re-derived here); the sociedad lifecycle and acciones-as-títulos
content (`02_sociedades-lifecycle.md` GT-CML-FR-047 and the share
register GT-CML-FR-050 — consumed by id; acciones are a título
species whose certificate mechanics live there); the liquidation-USAC
escheat clock (`02_sociedades-lifecycle.md` GT-CML-FR-069 — consumed
by pointer inside the matrix data model only); the RM publication
channel and fee catalog (`01_rm-surfaces.md` GT-CML-FR-001..025); the
AML machinery (C6, `04_aml-compliance.md` — forward ref, file +
cluster only); and every FEL/DTE obligation (GT-EINV wave — the
e-invoice regime's duties come from the SAT/LAT corpus, NOT from
arts. 591-604; this file owns only the paper-ancestor lineage guard,
one pointer FR).

## 2. Legal Basis

Authority order (binding, per master index preamble): CCom article
text = **66_** — *Código de Comercio, Decreto del Congreso 2-70* — as
consolidated inline through **Decreto 11-2006 (DCA 30-05-2006)**; the
print carries NO post-May-2006 reforms, so **every 66_-sourced row in
this file carries the GOQ-123 live-regime verification note** (kin —
owned by `01_books-anchor.md` GT-COA-FR-031). No publication-channel
or Q-amount row is load-bearing in C5 (the R64/D-18-2017 channel
tension and the R67 nominal-amount flags belong to the sibling files);
the one binding ledger row here is **R65**: pp. 215-301 of the print
are the surviving old code (Decreto 2946) maritime appendix with its
own article numbering (827-1319) colliding with D2-70's own 800s-1000s
— every citation from those pages says "D2946 (old code) art. N",
never D2-70 (load-bearing on LB-013 / FR-122). Instrument dated
identity (given 1970-01-28, promulgated 1970-04-09, **vigencia
1971-01-01** as modified by D-43-70, R45; what D-43-70 changed is
GOQ-122) is owned by `01_books-anchor.md` GT-COA-FR-030..032 and
consumed by id, never re-derived. Quotation sources: the committed
evidence files `gt/.extractions/66_CCom_sociedades_comercial.evidence.md`
(EV05b; EVID-536..569) and `gt/.extractions/66_CCom_libros_contabilidad.evidence.md`
(EV05a; EVID-517), verified against the scan text layer
`gt/.extractions/66_Codigo_Comercio_D2-70.pdf.txt`; and, for the
Civil fallback (GOQ-147, resolved 2026-08-22),
`gt/.extractions/92_Codigo_Civil.evidence.md` (EVID-931..951),
verified against `gt/.extractions/92_Codigo_Civil_DtoLey106.pdf.txt` —
the Código Civil is cited as **Decreto-Ley 106** (DCA 07-oct-1963,
vigencia 01-jul-1964 per art. 2178 as reformed by D-180), ONSEC
registry edition with **consolidation horizon ≥ 26-ago-2008** (EVID-931/932):
every CC-anchored row below carries the post-2008-staleness caveat
(reforms after 26-ago-2008 are invisible in this edition — live-text
cross-check before modeling, EVID-951). Gloss-derived
content (species article ranges, unstated-maturity default, art. 625
caducidad discipline) is marked "per the evidence gloss" throughout;
the acciones-amortizadas row is upgraded to STATUTORY (CCom art. 577
¶2 prints the dies a quo — EVID-950, GOQ-147 resolution).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CCom arts. 385-386: art. 385: "Son títulos de crédito los documentos que incorporan un derecho literal y autónomo, cuyo ejercicio o transferencia es imposible independientemente del título. Los títulos de crédito tienen la calidad de bienes muebles." / art. 386: "…los títulos de crédito que llenen los requisitos propios de cada título en particular y los generales siguientes 1º. El nombre del título de que se trate. 2º. La fecha y lugar de creación. 3º. Los derechos que el título incorpora. 4º. El lugar y la fecha de cumplimiento o ejercicio de tales derechos. 5º. La firma de quen [sic] lo crea. En los títulos en serie, podrán estamparse firmas por cualquier sistema controlado y deberán llevar por lo menos una firma autógrafa. … La omisión insubsanable de menciones o requisitos esenciales… no afectan al negocio o acto jurídico que dio origen a la emisión del documento." | Titles of credit are documents incorporating a LITERAL AND AUTONOMOUS right whose exercise or transfer is impossible independently of the title; títulos de crédito have the quality of movable property. Beyond each title's own particular requisites, the general ones are: 1º the name of the title; 2º date and place of creation; 3º the rights the title incorporates; 4º place and date of performance or exercise of those rights; 5º the signature of the creator [printed "quen" — sic]. Series titles may bear signatures by any controlled system and must carry at least one autograph signature. Unsanvable omission of essential mentions/requisites does not affect the legal act or business that gave origin to the document's issuance | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.85-86, arts. 385-386 (EVID-558) |
| LB-002 | CCom art. 388: "El título de crédito que tuviere su importe escrito en letras y cifras, valdrá, en caso de diferencia, por la suma escrita en letras. Si la cantidad estuviere expresada varias veces en letras o en cifras, el documento valdrá, en caso de diferencia, por la suma menor." | A título de crédito whose amount is written both in words and figures is worth, in case of difference, the sum written IN WORDS. If the amount is expressed several times in words or in figures, the document is worth, in case of difference, the LESSER sum | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.86, art. 388 (EVID-558) |
| LB-003 | CCom arts. 415/418/436/438: art. 415: "Son títulos nominativos los creados a favor de persona determinada cuyo nombre se consigna, tanto en el propio texto del documento, como en el registro del creador; son transmisibles mediante endoso e inscripción en el Registro." / art. 418: "Los títulos creados a favor de determinada persona se presumirán a la orden y se transmiten mediante endoso y entrega del título." / art. 436: "Son títulos al portador los que no están emitidos a favor de persona determinada… y se transmiten por la simple tradición." / art. 438: "El título de crédito que contiene la obligación de pagar una suma de dinero, no puede ser emitido a portador, sino en los casos expresamente permitidos por la ley." | Registered (nominativos) titles are those created in favour of a determined person whose name appears BOTH in the document's own text AND in the creator's register; they are transferable by endorsement AND inscription in the Register. Titles created in favour of a determined person are PRESUMED to order (a la orden) and transfer by endorsement + delivery of the title. Bearer titles (al portador) are those not issued in favour of a determined person… transferable by simple tradition (delivery). A título containing an obligation to PAY A SUM OF MONEY cannot be issued to bearer except in the cases expressly permitted by law | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.90-94, arts. 415, 418, 436, 438 (EVID-559) |
| LB-004 | CCom arts. 421/423/424/425/430: art. 421: "El endoso debe constar en el título mismo o en hoja adherida a él, y llenará los siguientes requisitos: 1º. El nombre del endosatario. 2º. La clase de endoso. 3º. El lugar y la fecha. 4º. La firma del endosante…" / art. 423: "El endoso debe ser puro y simple… El endoso parcial será nulo." / art. 424: "El endoso puede hacerse en blanco, con la sola firma del endosante." / art. 425: "El endoso puede hacerse en propiedad, en procuración o en garantía." / art. 430: "Para que el tenedor de un título a la orden pueda legitimarse, la cadena de endosos deberá ser ininterrumpida." | The endorsement must appear on the title itself or on a sheet adhered to it, and fulfils these requisites: 1º the endorsee's name; 2º the class of endorsement; 3º place and date; 4º the endorser's signature. The endorsement must be pure and simple… a PARTIAL endorsement is NULL. An endorsement may be made IN BLANK, with the sole signature of the endorser. An endorsement may be made in ownership (propiedad), for collection (procuración) or in guarantee (garantía). For the holder of an order title to legitimate itself, the chain of endorsements must be UNBROKEN | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.91-93, arts. 421, 423, 424, 425, 430 (EVID-559) |
| LB-005 | CCom arts. 399-402: art. 399: "La presentación en tiempo de un título de crédito y la negativa de su aceptación o de su pago se harán constar por medio del protesto. Salvo disposición legal expresa, ningún otro acto podrá suplir al protesto. El creador del título podrá dispensar al tenedor de protestarlo, si inscribe en el mismo la cláusula: sin protesto, sin gastos, u otra equivalente." / art. 400: "Mediante el aval, se podrá garantizar en todo o en parte el pago de los títulos de crédito que contengan obligación de pagar dinero." / art. 401: "El aval deberá constar en el título de crédito mismo o en hoja que a él seadhiera [as printed]… y deberá llevar la firma de quien lo preste. La sola firma puesta en el título, cuando no se le pueda atribuir otro significado, se tendrá por aval." / art. 402: "Si no se indica la cantidad en el aval, se entiende que garantiza el importe total del título de crédito." | Timely presentation of a título de crédito and refusal of its acceptance or payment are formalized by means of the PROTEST; save express legal provision, no other act may substitute the protest. The title's creator may dispense the holder from protesting by inscribing on it the clause "sin protesto, sin gastos" (without protest, without expenses) or an equivalent. By means of the AVAL, payment of money-obligation títulos may be guaranteed in whole or in part. The aval must appear on the título itself or on a sheet adhered to it [printed "seadhiera" — as printed] and must carry the guarantor's signature; a sole signature placed on the title, where no other meaning can be attributed to it, is held as an aval. If no amount is indicated, the aval guarantees the TOTAL amount of the título | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.87-89, arts. 399-402 (EVID-560) |
| LB-006 | CCom arts. 441/442/443/451: art. 441: "…la letra de cambio deberá contener: 1º. La orden incondicional de pagar una suma determinada de dinero. 2º. El nombre del girado. 3º. La forma de vencimiento." / art. 442: "En una letra de cambio pagadera a la vista o a varios días vista, el librador puede hacer constar que la cantidad librada producirá intereses… En la letra de cambio debe indicarse el tipo de interés. En caso de que esto falte, se entenderá que es del seis por ciento (6%)." / art. 443: "La letra de cambio puede ser librada: 1º. A la vista. 2º. A cierto tiempo vista. 3º. A cierto tiempo fecha. 4º. A día fijo." / art. 451: "Las letras de cambio pagaderas a cierto tiempo vista deberán presentarse para su aceptación dentro del año que siga su fecha." | A bill of exchange (letra de cambio) must contain: 1º the UNCONDITIONAL order to pay a determinate sum of money; 2º the drawee's name; 3º the form of maturity. In a bill payable at sight or at a term after sight, the drawer may state that the sum drawn will bear interest… the interest rate must be indicated; if missing it is understood to be SIX PER CENT (6%). A letra may be drawn: 1º at sight; 2º at a term after sight; 3º at a term after date; 4º at a fixed day. Bills payable at a term after sight must be presented for acceptance within the YEAR following their date | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.95-97, arts. 441-443, 451 (EVID-561) |
| LB-007 | CCom arts. 490-493: art. 490: "…el pagaré deberá contener: 1º. La promesa incondicional de pagar una suma determinada de dinero. 2º. El nombre de la persona a quien deba hacerse el pago." / art. 491: "En el pagaré podrán establecerse intereses convencionales. También podrá estipularse que el pago se haga mediante amortizaciones sucesivas." / art. 492: "El signatario del pagaré se considerará como aceptante de una letra de cambio…" / art. 493: "Serán aplicables al pagaré en lo conducente, las disposiciones relativas a la letra de cambio." | A promissory note (pagaré) must contain: 1º the unconditional promise to pay a determinate sum of money; 2º the name of the person to whom payment is to be made. Conventional interest may be established; it may also be stipulated that payment be made by successive amortizations (installments). The signer of a pagaré is considered as the ACCEPTING PARTY of a letra de cambio; the letra provisions apply to the pagaré as pertinent | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.104, arts. 490-493 (EVID-562) |
| LB-008 | CCom arts. 494/495/501/502/507/513: art. 494: "El cheque sólo puede ser librado contra un Banco, en formularios impresos suministrados o aprobados por el mismo. El título que en forma de cheques se libre en contravención a este artículo, no producirá efectos de título de crédito." / art. 495: "…el cheque deberá contener: 1º. La orden incondicional de pagar una determinada suma de dinero. 2º. El nombre del Banco librado. Cuando así se convenga con el Banco librado, la firma autógrafa del librador puede ser omitida en el cheque y deberá ser sustituida por su impresión o reproducción." / art. 501: "El cheque será siempre pagadero a la vista. Cualquier anotación en contrario, se tendrá por no puesta." / art. 502: "Los cheques deberán presentarse para su pago, dentro de los quince días calendario de su creación." / art. 507: "La revocación de la orden contenida en el cheque, sólo tiene efecto después de transcurrido el plazo legal para su presentación." / art. 513: "Las acciones cambiarias derivadas del cheque, prescriben en seis meses, contados desde la presentación, las del último tenedor, y desde el día siguiente a aquel en que paguen el cheque, las de los endosantes y las de los avalistas." | A cheque may ONLY be drawn against a BANK, on printed forms supplied or approved by it; a document drawn as a cheque in contravention produces NO título de crédito effects. The cheque must contain: 1º the unconditional order to pay a determinate sum; 2º the drawee bank's name — by agreement with the bank the drawer's autograph signature may be omitted and replaced by its impression/reproduction. A cheque is ALWAYS payable at sight; any contrary annotation is deemed not written. Cheques must be presented for payment within FIFTEEN CALENDAR DAYS of creation. Revocation of the cheque's order takes effect only AFTER the legal presentation period has run. Cambiaria actions on a cheque prescribe in SIX MONTHS — the last holder's from presentation; endorsers' and avalistas' from the day after they pay the cheque | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.104-107, 111, arts. 494, 495, 501, 502, 507, 513 (EVID-563) |
| LB-009 | CCom arts. 591-593: art. 591: "La factura cambiaria es el título de crédito que en la compraventa de mercaderías el vendedor podrá librar y entregar o remitir al comprador y que incorpora un derecho de crédito sobre la totalidad o la parte insoluta de la compraventa. El comprador estará obligado a devolver al vendedor, debidamente aceptada, la factura cambiaria original en las condiciones de este capítulo. No se podrá librar factura cambiaria que no corresponda a una venta efectiva de mercaderías entregadas, real o simbólicamente." / art. 592: "Quedan exceptuadas del régimen aquí dispuesto, aquellas compraventas documentadas con letras de cambio, pagarés u otros títulos de crédito." / art. 593: "Una vez que la factura cambiaria fuese aceptada por el comprador, se considerará, frente a terceros de buena fe, que el contrato de compraventa ha sido debidamente ejecutado en la forma expuesta en la misma." | The factura cambiaria (exchange invoice) is the título de crédito which, in a sale of merchandise, the seller may draw and deliver or send to the buyer, incorporating a credit right over the TOTALITY or the UNPAID PART of the sale. The buyer is OBLIGED to return to the seller, duly ACCEPTED, the original factura cambiaria under this chapter's conditions. No factura cambiaria may be drawn that does not correspond to an effective sale of merchandise delivered, REALLY or SYMBOLICALLY. Sales documented with letras de cambio, pagarés or other títulos de crédito are excepted from this regime. Once accepted by the buyer, the compraventa is deemed — vis-à-vis good-faith third parties — duly executed in the manner set out in the factura | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.122-123, arts. 591-593 (EVID-564) |
| LB-010 | CCom arts. 594-595: art. 594: "Además de los requisitos que establece el artículo 386, la factura cambiaria deberá contener: 1º. El número de orden del título librado. 2º. El nombre y domicilio del comprador. 3º. La denominación y características principales de las mercaderías vendidas. 4º. El precio unitario y el precio total de las mismas. La omisión de cualquiera de los requisitos… no afectará la validez del negocio jurídico… pero ésta perderá su calidad de título de crédito." / art. 595: "Cuando el pago haya de hacerse en abonos… 1º. El número de abonos. 2º. La fecha de vencimiento de los mismos. 3º. El monto de cada uno. Los pagos parciales se harán constar en la misma factura…" | Beyond article 386's requisites, the factura cambiaria must contain: 1º the ORDER NUMBER of the drawn title; 2º the buyer's name and domicile; 3º the denomination and principal characteristics of the merchandise sold; 4º the UNIT price and the TOTAL price. Omission of any of these requisites does not affect the validity of the legal business… but it LOSES its quality as a título de crédito. When payment is to be made in installments (abonos): 1º the number of installments; 2º their maturity dates; 3º the amount of each. PARTIAL PAYMENTS are recorded on the invoice itself | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.123, arts. 594-595 (EVID-564) |
| LB-011 | CCom arts. 596/597/599/600/601/602/604: art. 596: "…Si la factura no acompañase las mercaderías o documentos representativos de éstas, deberá ser enviada por el vendedor en un término no mayor de tres días al de su libramiento, que nunca podrá exceder en cuarenta y ocho horas al de la entrega o despacho de las mercaderías…" / art. 597: "Si el vendedor enviase la factura cambiaria por correo, deberá hacerlo por correo certificado con aviso de recepción…" / art. 599: "El comprador deberá devolver al vendedor la factura cambiaria, debidamente aceptada: 1º. Dentro de un plazo de cinco días a contar de la fecha de su recibo, si la operación se ejecuta en la misma plaza. 2º. Dentro de un término de quince días a contar de la fecha de su recibo, si la operación se ejecuta en diferente plaza." / art. 600: "El comprador podrá negarse a aceptar la factura: 1º. En caso de avería, extravío o no recibo de las mercaderías… 2º. Si hay defectos o vicios en la cantidad o calidad de las mercaderías. 3º. Si no contiene el negocio jurídico convenido. 4º. Por omisión de cualquiera de los requisitos que dan a la factura cambiaria su calidad de título de crédito." / art. 601: "La factura cambiaria podrá ser protestada por falta de aceptación o por falta de pago. La no devolución de la factura cambiaria se entenderá como falta de aceptación." / art. 602: "El protesto por falta de aceptación, deberá levantarse dentro de los dos días hábiles siguientes al vencimiento del plazo estipulado en el artículo 599…" / art. 604: "Los comerciantes deberán conservar ordenadamente, por el término de cinco años, las facturas cambiarias que hubieren librado o copias de las mismas." | If the factura does not accompany the goods or their representative documents, the seller must send it within a term NOT greater than THREE DAYS from drawing, which may never exceed FORTY-EIGHT HOURS from delivery or dispatch of the goods. If sent by mail: certified mail with acknowledgment of receipt. The buyer must return the factura cambiaria duly accepted: 1º within FIVE DAYS from receipt, if the transaction is executed in the same plaza (market/town); 2º within FIFTEEN DAYS from receipt, if in a different plaza. The buyer may refuse acceptance: 1º damage, loss or non-receipt of the goods; 2º defects in quantity or quality; 3º it does not contain the agreed legal business; 4º omission of any requisite giving the factura its título de crédito quality. The factura cambiaria may be protested for lack of acceptance or lack of payment; NON-RETURN is understood as lack of acceptance. Protest for non-acceptance must be raised within the TWO BUSINESS DAYS following expiry of art. 599's period. Merchants must conserve ORDERLY, for the term of FIVE YEARS, the facturas cambiarias they have drawn or copies thereof | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | pp.123-125, arts. 596-604 (EVID-565) |
| LB-012 | CCom arts. 626-628 + 409: art. 626: "La acción cambiaria directa, prescribe en tres años a partir del día del vencimiento." / art. 627: "La acción cambiaria de regreso del último tenedor prescribirá en un año, contado desde la fecha del vencimiento y en su caso, desde que concluyan los plazos de presentación, o si el título fuere con protesto, desde la fecha en que éste se haya levantado." / art. 628: "La acción del obligado, de regreso contra los demás obligados anterior, prescribe en seis meses, contados a partir de la fecha del pago voluntario o de la fecha de notificación de la demanda." / art. 409: "…puede exigir al creador la suma con que se haya enriquecido en su daño. Esta acción prescribe en un año, contado desde el día en que se extinguió la acción cambiaria." | The DIRECT cambiaria action prescribes in THREE YEARS from the day of maturity. The last holder's RECOURSE cambiaria action prescribes in ONE YEAR, counted from the maturity date and, where applicable, from the close of the presentation periods or — if the title is with protest — from the date the protest was raised. The obligated party's action of recourse against the other prior obligados prescribes in SIX MONTHS from the date of voluntary payment or of notification of the claim. [Art. 409] the holder may demand from the creator the sum by which he enriched himself to the holder's detriment; this ENRICHMENT action prescribes in ONE YEAR from the day the cambiaria action extinguished | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.130, arts. 626-628; p.89, art. 409 (EVID-566) |
| LB-013 | CCom arts. 541/577/799/916/1037 + D2946 (old code) art. 1313: art. 541: "Las acciones cambiarias contra el que expida o ponga en circulación cheques de viajero, prescribirán en dos años a partir de la fecha en que los cheques se hayan expedido." / art. 577: "Las acciones para el cobro de los intereses prescribirán en cinco años, y para el cobro del principal en diez. La prescripción de los títulos amortizados por sorteo correrá a partir de la fecha de la primera publicación exigida por el artículo 569." (obligaciones/debentures; ¶2 = the acciones-amortizadas dies a quo — EVID-950, GOQ-147 upgrade from gloss-only to statutory) / art. 799: "Las acciones derivadas del contrato de transporte prescribirán en seis meses, contados a partir del término del viaje, o de la fecha en que el pasajero o las cosas porteadas debieran llegar a su destino." / art. 916: "Todas las acciones que deriven de un contrato de seguro, prescribirán en dos años, contados desde la fecha del acontecimiento que les dio origen." / art. 1037: "Las acciones del beneficiario contra la afianzadora y las de esta contra los contrafiadores y reafianzadoras, prescribirán en dos años." / D2946 (old code) art. 1313: "Las acciones que proceden de las obligaciones de que trata el presente libro y que no tengan plazo señalado para prescribir, durarán cinco años." | Cambiaria actions against the issuer/circulator of TRAVELLER'S CHEQUES prescribe in TWO YEARS from the date the cheques were issued. [Debentures/obligaciones] actions to collect INTEREST prescribe in FIVE YEARS, and for collection of the PRINCIPAL in TEN; draw-amortized (sorteo) títulos: the prescription RUNS FROM the date of the FIRST publication required by art. 569 (¶2 — statutory dies a quo). Actions derived from the TRANSPORT contract prescribe in SIX MONTHS, counted from the end of the journey or the date the passenger or carried goods should have arrived at destination. ALL actions deriving from an INSURANCE contract prescribe in TWO YEARS from the date of the originating event. The beneficiary's actions against the surety (afianzadora), and the surety's against co-sureties and reinsurers, prescribe in TWO YEARS. [Old code, maritime appendix — R65: cite as D2946 (old code) art. 1313, NEVER as D2-70] actions proceeding from the obligations of the present book lacking a stated prescription term last FIVE YEARS | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.113 art. 541; p.120 art. 577; p.156 art. 799; p.185 art. 916; p.205 art. 1037; p.299 D2946 (old code) arts. 1308-1313 appendix (EVID-567) |
| LB-014 | CCom arts. 383/384/1 + transitorio X: art. 383: "Los documentos que conciernan especialmente a actos o negociaciones determinadas, podrán ser inutilizados o destruidos, pasado el tiempo de prescripción de las acciones que de ellos se deriven." / "Si hubiere pendiente alguna cuestión que se refiera a ellos directa o indirectamente, deberán conservarse hasta la terminación de la misma." / art. 384: "Queda al arbitrio del comerciante el sistema de archivo y custodia de valores, correspondencia y demás documentos del giro de su empresa." / art. 1: "Los comerciantes en su actividad profesional, los negocios jurídicos mercantiles y cosas mercantiles, se regirán por las disposiciones de este Código y, en su defecto, por las del Derecho Civil que se aplicarán e interpretarán de conformidad con los principios que inspira el Derecho Mercantil." / transitorio X: "Las disposiciones de este Código relativas a la prescripción, no se aplicarán en todos aquellos casos en que la misma ya hubiere empezado a correr conforme la ley anterior." | Documents concerning specific determined acts or negotiations may be cancelled or destroyed once the PRESCRIPTION PERIOD OF THE ACTIONS DERIVED FROM THEM has passed; if any matter concerning them directly or indirectly is PENDING, they must be conserved until its termination. The system of filing and custody of securities, correspondence and other business documents is at the merchant's discretion. Merchants, mercantile legal businesses and mercantile things are governed by this Code and, IN ITS ABSENCE, by Civil law, applied and interpreted in conformity with the principles inspiring Mercantile law. [Transitory X] this Code's prescription provisions do not apply where prescription had ALREADY begun running under the prior law | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.85, arts. 383-384; p.2, art. 1; p.209, transitorio X (EVID-517) |
| LB-015 | Código Civil (92_), identity + the fallback clock core, Dto-Ley 106: "CÓDIGO CIVIL / DECRETO-LEY NUMERO 106" (footnote: " Publicado en el Diario de Centro América el 07 de octubre de 1963."); art. 2178: "Este Código entrará en vigor el primero de julio de mil novecientos sesenta y cuatro." (texto D-180, DCA 27-Feb-1964); art. 1508: "La prescripción extintiva se verifica en todos los casos no mencionados en disposiciones especiales, por el transcurso de cinco años, contados desde que la obligación pudo exigirse; y si ésta consiste en no hacer, desde el acto contrario a la obligación." / art. 1509: "En las obligaciones a plazo y en las condiciones, se cuenta el término para la prescripción, desde que el plazo se cumple o la condición se verifica." / art. 1516: "Las disposiciones del presente capítulo se entienden sin perjuicio de lo que en este Código o en leyes especiales se establezca respecto a otros casos de prescripción." / art. 1511: "En las obligaciones con intereses, la prescri pci ón [sic split] del capital, vencido el plazo, se cuenta desde la fecha del último pago de los intereses." / art. 1512: "La prescripción de la obligación de rendir cuentas comienza a correr desde el día en que el obligado termina su administración; y la de la acción para cobrar el saldo de aquéllas, desde el día en que la cuenta sea aprobada por los interesados o por sentencia firme." / art. 2180: "…salvo el término de la prescripción que será el señalado por la ley vigente al tiempo en que la obligación fue contraída." | The Civil Code = Decreto-Ley 106 (given 14-sep-1963, DCA 07-oct-1963, VIGENCIA 01-jul-1964 per art. 2178 as reformed by D-180) — ONSEC registry print, pages 671-945, NO generation date, consolidation horizon ≥ 26-AUG-2008 (latest DCA date printed = D-39-2008): every CC-anchored row carries the post-2008-staleness caveat (EVID-931/932/951). THE FR-110 FALLBACK CLOCK (GOQ-147 resolved): extinctive prescription in all cases not covered by special provisions runs FIVE YEARS "contados desde que la obligación pudo exigirse" (from demandability; not-to-do obligations from the contrary act); plazo/condición obligations from maturity/verification (1509); interest-bearing capital (post-maturity) from the LAST INTEREST PAYMENT (1511 — rolling reset); cuentas from end of administration / approval (1512). Art. 1516 = the deference gateway: special prescriptions in this Code or special laws PREVAIL — the Civil 5y is the residual, never the override. Art. 2180 = dated-instrument conflict rule (prescription term = law in force when the obligation was contracted) | `gt/sources/92_Codigo_Civil_DtoLey106.pdf` | p.1 + fn. (identity, EVID-931); p.275 arts. 2178/2180 (EVID-932); pp.198-199 arts. 1508-1509, 1511-1512, 1516 (EVID-936/937/939) |
| LB-016 | Código Civil (92_), mechanics + the short/long specials ledger: art. 1505: "No corre el término para la prescripción: 1. Contra los menores y los incapacitados, durante el tiempo que estén sin representante legal constituido; 2. Entre padres e hijos, durante la patria potestad; 3. Entre los menores e incapacitados y sus tutores, mientras dure la tutela; 4. Entre los copropietarios, mientras dure la indivisión; y 5. Entre los cónyuges, durante el matrimonio; y entre hombre y mujer, durante la unión de hecho." / art. 1506: "La prescripción se Interrumpe [sic, capital I]: 1. Por demanda judicial debidamente notificada o por cualquier providencia precautoria ejecutada, salvo si el acreedor desistiere de la acción intentada, o el demandado fuere absuelto de la demanda, o el acto judicial se declare nulo; 2. Si la persona a cuyo favor corre la prescri pción [sic split], reconoce expresamente, depalabra [sic] o por escrito, o tácitamente por hechos indudables, el derecho de la persona contra quien prescribe; y 3. Por el pago de intereses o amortizaciones por el deudor, así como por el cumplimiento parcial de la obligación por parte de éste." / art. 1507: "El efecto de la interrupción es inutilizar para la prescripción todo el tiempo corrido antes de ella." / art. 1514 (selected): "Prescriben en dos años: … 2. La acción de cualquier comerciante para cobrar el precio de los objetos vendidos; … 4. Las pensiones, rentas, alquileres y cualesquiera otras prestaciones periódicas no cobradas, a su vencimiento…" / art. 1513: "Prescribe en un año la responsabilidad civil proveniente de delito o falta…" / art. 1515: "La obligación de rendir cuentas… y la acción para cobrar el saldo de ellos, prescriben por el término de tres años." / art. 856: "La obligación garantizada con hipoteca prescribirá a los diez años contados desde el vencimiento de la obligación o de la fecha en que se tuviere como vencido en virtud de lo estipulado." / art. 651 (disambiguation): "…el dominio sobre bienes inmuebles… se adquiere por prescripción, por el transcurso de diez años. Los bienes muebles y semovientes, por el de dos años." / art. 1628: "La acción para recobrar lo i ndebidamente pagado prescribe en un año…" / art. 1300: "La acción revocator ia [sic split] prescribe en un año…" / art. 1727: "Las acciones derivadas del mandato que no tengan término especial de prescripción, duran un año contado de la fecha en que terminó el mandato." | The fallback's MECHANICS + SPECIALS menu (each beats the 5y for its subject — EVID-934/935/938/940/941/943): SUSPENSION (1505) in exactly five status relationships (minors/incapacitated without representative; parent-child under patria potestad; tutor-ward; co-owners while indivisión lasts; spouses/uniones de hecho); INTERRUPTION (1506) by (1) duly-notified judicial demand or executed precautory measure — defeated by desistimiento/absolución/nullity — (2) express or tacit recognition, (3) payment of interests or amortizations / partial performance, with FULL RESTART effect (1507 — "inutilizar… todo el tiempo corrido antes de ella"); 2 años: ANY merchant's action to collect the price of goods sold (1514.2 — the non-title credit-sale clock; título paper goes to CCom 626/627 via 1516), fees/sueldos/salarios/jornales (1514.1), pensiones/rentas/alquileres per installment at its vencimiento (1514.4); 3 años: account rendering + saldo (1515); 1 año: delito/falta civil liability and personal-injury damages (1513), undue-payment recovery (1628 — refund claims), pauliana/revocatoria (1300), mandate-derived actions (1727); 10 años: hipoteca-guaranteed obligation from vencimiento/stipulated acceleration (856). USUCAPIÓN DISAMBIGUATION (651, 10y inmuebles / 2y muebles): arts. 643-654 are ACQUISITIVE-property rules — never cite them for debt/claim clocks (EVID-940) | `gt/sources/92_Codigo_Civil_DtoLey106.pdf` | pp.197-199 arts. 1505-1507, 1513-1515 (EVID-934/935/938); p.112 art. 856 (EVID-941); p.84 art. 651 (EVID-940); pp.174/212/218/224 arts. 1300/1628/1673/1727 (EVID-943) |

## 3. Functional Requirements

### 3.1 Título de crédito framework (arts. 385-388)

- **GT-CML-FR-086:** The system shall carry the título de crédito
  instrument catalog as shared dated config: every instrument modeled
  under this file is a *título de crédito* per art. 385 — a document
  incorporating a **literal and autonomous** right whose exercise or
  transfer is impossible independently of the title, with the quality
  of *bienes muebles* (movable property) — and the species list is the
  Libro III taxonomy as printed: letra de cambio, pagaré, cheque,
  obligaciones/debentures, certificado de depósito/bono de prenda,
  carta de porte/conocimiento, factura cambiaria, cédulas
  hipotecarias, bonos bancarios, certificados fiduciarios (species
  chapter ranges per the evidence gloss: 441+/490+/494+/544+/584+/
  588+/591-604/605+/608/609+), with acciones as a título species
  owned and consumed from `02_sociedades-lifecycle.md` GT-CML-FR-047
  by id, never re-derived here. The literal/autonomous principle is a
  modeling guard: the record's document IS the right — no
  off-document balance governs the instrument's face. (LB-001;
  EVID-558)
- **GT-CML-FR-087:** The system shall validate, on every título
  record, the five general requisites of art. 386 — (1º) the name of
  the title; (2º) date and place of creation; (3º) the rights the
  title incorporates; (4º) place and date of performance or exercise;
  (5º) the creator's signature — plus each species' own particular
  requisites (FR-096..FR-102), with the series rule (signatures by
  any controlled system carrying at least one autograph signature)
  and the omission rule recorded as validation OUTCOMES, not
  legal-effect computations: an unsubsanable omission of essential
  mentions does not affect the underlying negocio jurídico (the
  recorded receivable/payable stands), it only strips título-quality
  behaviors (negotiability, prescription classes, protest rights)
  from the record. (LB-001; EVID-558)
- **GT-CML-FR-088:** The system shall resolve instrument amounts per
  art. 388 as face-value rules: words-and-figures conflict → the sum
  written in words prevails; the amount expressed several times
  (whether in words or in figures) → the document is worth the LESSER
  sum; both rules run on the recorded face amount with the resolution
  basis stored, never silently normalizing a discrepancy. (LB-002;
  EVID-558)

### 3.2 Circulation classes and endoso (arts. 415-438)

- **GT-CML-FR-089:** The system shall carry the three-class
  circulation taxonomy as instrument-profile config driving transfer
  mechanics: **nominativos** — created in favour of a determined
  person named in the document text AND in the creator's register,
  transferable by endoso PLUS inscription in that register (art. 415);
  **a la orden** — the DEFAULT for titles created in favour of a
  determined person, transferable by endoso plus delivery (art. 418);
  **al portador** — not issued in favour of a determined person,
  transferable by simple tradition (art. 436). (LB-003; EVID-559)
- **GT-CML-FR-090:** The system shall record every endoso
  (endorsement) as a bookkeeping object carrying the art.-421
  requisites — endorsee name, endorsement class, place and date,
  endorser signature — placed on the title record or its adhered
  sheet (allonge), with nominativo-class transfers additionally
  requiring the register-inscription step (FR-089) before the
  transfer is complete. (LB-004; EVID-559)
- **GT-CML-FR-091:** The system shall enforce endorsement form
  rules: an endoso must be pure and simple — a PARTIAL endoso is NULL
  and must be rejected at entry (art. 423); a BLANK endoso (sole
  endorser signature, no endorsee) is lawful and leaves the title
  effectively transferable by delivery (art. 424); the endorsement
  CLASS is one of **propiedad** (ownership), **procuración**
  (collection) or **garantía** (guarantee) (art. 425), recorded per
  endoso and driving holder-role semantics. (LB-004; EVID-559)
- **GT-CML-FR-092:** The system shall validate the UNBROKEN CHAIN of
  endorsements for a la orden legitimacy (art. 430): the current
  holder of an order title legitimizes itself only through a
  contiguous endoso chain reaching back to the creator; a gap breaks
  legitimacy and blocks holder-derived workflows (protest, cobro,
  re-transfer) pending cure by recording the missing links.
  (LB-004; EVID-559)
- **GT-CML-FR-093:** The system shall enforce the bearer money-paper
  restriction as an issuance guard: a título containing an obligation
  to pay a sum of money may NOT be issued al portador except in the
  cases expressly permitted by law (art. 438) — creating a
  money-payable bearer instrument without a law-permission basis
  configured raises the guard; non-money titles are unaffected.
  (LB-003; EVID-559)

### 3.3 Protesto and aval (arts. 399-405)

- **GT-CML-FR-094:** The system shall track protesto state on every
  instrument: timely presentation plus refusal of acceptance or
  payment is formalized by means of the protest, and — save express
  legal provision — no other act substitutes it (art. 399); the
  creator's dispensa clause "sin protesto, sin gastos" (without
  protest, without expenses) or equivalent is a recorded waiver flag
  suppressing the protest-requirement consequence, never the
  underlying default. Protocolized protest copies carry the
  execution-title (título ejecutivo) exposure flag (art. 1039, per
  the evidence gloss). (LB-005; EVID-560)
- **GT-CML-FR-095:** The system shall record avals (third-party
  guarantees) on instruments bearing a money obligation: the aval
  guarantees payment in whole or part (art. 400); it is placed on the
  título or adhered sheet with the guarantor's signature, and a sole
  signature on the title to which no other meaning can be attributed
  is held an aval (art. 401); with no amount indicated, the aval
  guarantees the instrument's TOTAL amount (art. 402) — the record
  stores avalista, guaranteed amount (default full) and placement,
  with co-signatories of a same act carrying the solidarity exposure
  note (art. 398, per the evidence gloss). (LB-005; EVID-560)

### 3.4 Instrument species — bounded profiles

- **GT-CML-FR-096:** The system shall carry the letra de cambio
  profile: requisites on top of art. 386 — unconditional order to pay
  a determinate sum of money, drawee name, form of maturity
  (art. 441); exactly FOUR maturity forms — a la vista (at sight), a
  cierto tiempo vista (term after sight), a cierto tiempo fecha (term
  after date), a día fijo (fixed day) (art. 443), with an unstated
  maturity defaulting to a la vista (per the evidence gloss); bills
  payable at a term after sight must be presented for acceptance
  within the YEAR following their date (art. 451), surfaced as an
  acceptance-presentation clock. (LB-006; EVID-561)
- **GT-CML-FR-097:** The system shall carry the letra interest rule:
  an interest stipulation is recordable only on letras payable a la
  vista or a varios días vista (art. 442); the interest TYPE must be
  indicated on the title, and where it is missing the rate resolves
  to the SIX PER CENT (6%) statutory default — stored as a dated
  config row (instrument D2-70, valid_from 1971-01-01 per
  GT-COA-FR-030..032) with snapshot-on-write of the resolved rate.
  (LB-006; EVID-561)
- **GT-CML-FR-098:** The system shall carry the pagaré profile:
  requisites — unconditional promise to pay a determinate sum of
  money plus the payee's name (art. 490); conventional interest and
  installment amortization schedules (amortizaciones sucesivas)
  recordable (art. 491); maker semantics — the signatario is treated
  as the ACCEPTING PARTY of a letra de cambio (art. 492) — so the
  maker sits on the direct-action side of the prescription ladder
  (FR-111); letra provisions apply supplementarily (art. 493).
  (LB-007; EVID-562)
- **GT-CML-FR-099:** The system shall carry the cheque profile as
  dated config with hard guards: bank-drawn ONLY, on printed forms
  supplied or approved by the drawee bank — a cheque-form document
  drawn in contravention produces no título de crédito effects
  (art. 494); requisites — unconditional payment order + drawee bank
  name, with facsimile signature permissible by agreement with the
  bank (art. 495); ALWAYS payable at sight, any contrary annotation
  deemed unwritten (art. 501); presentation for payment within
  FIFTEEN CALENDAR DAYS of creation (art. 502), surfaced as the
  presentation-window clock; revocation (stop order) effective only
  AFTER the legal presentation window has run (art. 507), enforced as
  a dated stop-payment gate keyed to the creation date; prescription
  6 months per FR-115. (LB-008; EVID-563)
- **GT-CML-FR-100:** The system shall carry the remaining species as
  existence-level bounded profiles (name, art.-386/388 validation,
  circulation class, prescription-class binding; no mechanics
  invented beyond the corpus): obligaciones/debentures (interest
  5 y / principal 10 y clocks FR-117/FR-118), certificado de
  depósito and bono de prenda (almacenes generales de depósito),
  carta de porte and conocimiento (transport documents — transporte
  clock FR-119), cédulas hipotecarias, bonos bancarios, certificados
  fiduciarios — chapter placement per the evidence gloss; species
  detail beyond this file's rows stays open until its corpus
  instruments land (non-OQ gap discipline — flagged, never invented).
  (LB-001; EVID-558)

### 3.5 FACTURA CAMBIARIA (arts. 591-604) + FEL-lineage guard

- **GT-CML-FR-101:** The system shall carry the factura cambiaria as
  an instrument profile: a título de crédito which, in the
  compraventa de mercaderías, the SELLER may draw and deliver or send
  to the buyer, incorporating a credit right over the totality or the
  unpaid part (parte insoluta) of the sale (art. 591); it may ONLY be
  drawn on an effective sale of merchandise delivered, REALLY or
  SYMBOLICALLY — a real-delivery precondition recorded on the
  instrument; the buyer is obliged to RETURN the original duly
  accepted (the acceptance workflow, FR-105); sales already
  documented with letras, pagarés or other títulos de crédito are
  EXCEPTED from the regime (art. 592) — surfaced as a
  one-instrument-per-sale guard; once accepted, the compraventa is
  deemed duly executed vis-à-vis good-faith third parties (art. 593)
  — an evidentiary note on the accepted record. (LB-009; EVID-564)
- **GT-CML-FR-102:** The system shall validate the four factura
  cambiaria requisites added to art. 386: (1º) the número de orden
  (order/serial number) of the drawn title; (2º) the buyer's name and
  domicile; (3º) the denomination and principal characteristics of
  the goods sold; (4º) the unit and total prices — and record the
  omission consequence exactly: the document's validity as a negocio
  jurídico is UNAFFECTED, but it LOSES its quality as título de
  crédito (art. 594), i.e. the record degrades to a non-negotiable
  receivable document (no endoso chain, no cambiaria prescription
  classes, no protest rights). (LB-010; EVID-564)
- **GT-CML-FR-103:** The system shall carry installment data on the
  face of credit-term facturas cambiarias: number of abonos
  (installments), each one's maturity date, and each one's amount
  (art. 595.1º-3º), with PARTIAL PAYMENTS recorded on the same
  factura (annotation surface on the instrument record, art. 595
  final clause) — the installment rows drive the per-installment
  maturity anchors of the prescription ladder (FR-111/FR-112).
  (LB-010; EVID-564)
- **GT-CML-FR-104:** The system shall surface the factura cambiaria
  dispatch clocks as tasks: where the factura does not accompany the
  goods or their representative documents, the seller must send it
  within a term not greater than THREE DAYS from drawing, which may
  never exceed FORTY-EIGHT HOURS from the delivery or dispatch of the
  goods (art. 596); mailing is by certified mail with acknowledgment
  of receipt (art. 597) — recorded as the dispatch-channel state on
  the instrument. (LB-011; EVID-565)
- **GT-CML-FR-105:** The system shall compute the acceptance clocks
  from the recorded receipt date: the buyer must return the original
  factura cambiaria duly accepted within FIVE DAYS if the transaction
  is executed in the same plaza, or FIFTEEN DAYS if in a different
  plaza (art. 599) — the same-plaza/different-plaza flag on the
  instrument selects the clock; non-return within the window is
  understood as lack of acceptance (art. 601, with FR-107).
  (LB-011; EVID-565)
- **GT-CML-FR-106:** The system shall carry the four bounded
  rejection grounds on which the buyer may refuse acceptance
  (art. 600): (1º) damage, loss or non-receipt of the goods; (2º)
  defects or vicios in the quantity or quality of the goods; (3º) the
  document does not contain the agreed negocio jurídico; (4º) omission
  of any requisite giving the factura its título de crédito quality
  (ties to FR-102's degradation) — a closed reason catalog on the
  acceptance-refusal event. (LB-011; EVID-565)
- **GT-CML-FR-107:** The system shall track factura cambiaria
  protest: protest lies for lack of acceptance OR lack of payment,
  and NON-RETURN of the factura is understood as lack of acceptance
  (art. 601); the protest for non-acceptance must be raised within
  the TWO BUSINESS DAYS (días hábiles) following expiry of the
  art.-599 period (art. 602) — a hábiles-day clock distinct from
  the calendar clocks of FR-104/FR-105, feeding FR-094's protest
  state and FR-112's regreso anchor. (LB-011; EVID-565)
- **GT-CML-FR-108:** The system shall carry the merchant retention
  duty for facturas cambiarias as a dated config row: merchants must
  conserve, ORDERLY, for the term of FIVE YEARS, the facturas
  cambiarias they have drawn or copies thereof (art. 604) — recorded
  as instrument D2-70, valid_from 1971-01-01, object = issued
  facturas cambiarias + copies, with NO supersession asserted from
  this corpus and the max-per-regime resolution (vs CCom art. 382's
  floor and the tax corpus via GT-TAX-FR-232) owned by the Task 7
  retention/destruction matrix, consumed by pointer. CLOCK-SEMANTICS
  RETYPE (GOQ-147, EVID-950): art. 604 is a CONSERVATION/RETENTION
  duty (keep the documents 5 años), NOT a claim-prescription clock —
  the claim clocks for facturas cambiarias as títulos are CCom arts.
  626/627 (FR-111/FR-112: directa 3 años from vencimiento / regreso
  1 año), the destruction gate stays CCom art. 383 (FR-125), and the
  Civil Code supplies nothing here (arts. 1508/1516 confirm no
  fallback runs where CCom fixes the period — residual only for
  non-cambiaria factura-derived claims, e.g. the precio claim at CC
  art. 1514.2).
  (LB-011; EVID-565; EVID-950; GOQ-124 kin)
- **GT-CML-FR-109:** FEL-lineage guard (load-bearing negative row):
  the factura cambiaria of arts. 591-604 is the PAPER ANCESTOR of the
  Guatemalan electronic invoice — lineage factura cambiaria (D2-70,
  1971) → fiscalized factura mercantil (IVA-era paper/printers) →
  DTE/FEL — and the ancestry is FIELD-LEVEL ONLY: the art.-594 field
  set (serial number; buyer identification + domicile; goods
  denomination/characteristics; unit and total prices) survives
  conceptually in modern DTE mandatory fields; the system shall NEVER
  cite FEL/DTE emission, validation, certification, archive or
  contingency duties to arts. 591-604 — all FEL obligations live in
  the GT-EINV wave (`../../e-invoicing/`, file-level pointer; e.g.
  `01_document-types.md`, which carries the FCAM lineage citations)
  and this file records the relationship without conflating it.
  (LB-009; LB-010; EVID-564)

### 3.6 The mercantile prescription matrix — one FR per clock

- **GT-CML-FR-110:** FALLBACK-CLOCK FR (load-bearing; was a
  negative-FR, CLOSED by GOQ-147/92_): the system shall NOT model any
  general commercial prescription period INSIDE the CCom — the Código
  de Comercio enacts none; art. 1 defers gaps to the Derecho Civil
  (applied and interpreted per mercantile-law principles) — and the
  Civil fallback now has corpus anchors: the general extinctive
  prescription of CC art. 1508 — "cinco años, contados desde que la
  obligación pudo exigirse" (five years from demandability;
  not-to-do obligations from the contrary act) — applies to every
  commercial claim lacking a special CCom/special-law period, BEHIND
  the art.-1516 gateway ("Las disposiciones del presente capítulo se
  entienden sin perjuicio de lo que en este Código o en leyes
  especiales se establezca respecto a otros casos de prescripción." —
  special law prevails; 1508 is the residual, never the override over
  FR-111..FR-122 or another enumerated special); pointer rows owned by
  sibling files ride the same precedence: acciones amortizadas — now
  STATUTORY, not gloss-only: CCom art. 577 ¶2, "La prescripción de los
  títulos amortizados por sorteo correrá a partir de la fecha de la
  primera publicación exigida por el artículo 569." (10 años riding
  ¶1's principal rule; owned cml02) — and liquidation-USAC escheat
  GT-CML-FR-069. The cc_fallback
  config row carries: term 5 años; dies-a-quo kit — 1508 (exigibility),
  1509 (plazo from maturity / condición from verification), 1511
  (interest-bearing capital, post-maturity, from the last interest
  payment), 1512 (cuentas: end of administration / approval); the
  SHORT specials that beat the 5y for their subjects (LB-016 menu):
  2 años merchant price of goods sold (1514.2 — non-title credit
  sales; título paper goes to 626/627 via 1516), fees/sueldos/jornales
  (1514.1), pensiones/rentas/alquileres at each vencimiento (1514.4);
  3 años cuentas render+saldo (1515); 1 año delito/daño personal
  (1513), pago indebido (1628), pauliana (1300), mandato (1727); 10
  años hipoteca-guaranteed obligation (856); mechanics — interruption
  1506/1507 (notified judicial demand / recognition / interest-
  amortization payment or partial performance, each RESTARTING the
  clock from zero) and suspension 1505 (five enumerated status
  relationships only); USUCAPIÓN GUARD: arts. 643-654 (651: 10 y
  inmuebles / 2 y muebles) are acquisitive-property rules, never
  debt/claim clocks. DATED-INSTRUMENT CAVEAT on every CC-anchored
  value: Dto-Ley 106 as consolidated ≥ 26-ago-2008 (ONSEC edition, no
  print date) — post-2008 reforms unverifiable from this edition
  (live-text cross-check before modeling, EVID-951); CC art. 2180
  conflict rule (prescription term = law in force when the obligation
  was contracted). Never a guessed default such as a generic
  CCom-sourced 5-year commercial period.
  (LB-014; LB-015; LB-016; EVID-517; EVID-931..951)
- **GT-CML-FR-111:** The system shall carry the acción cambiaria
  directa clock: prescribes in THREE YEARS from the day of
  *vencimiento* (maturity) — anchor = the instrument's maturity date
  (per-installment for pagaré/factura installment paper, FR-103);
  binds holder vs acceptor/maker-side obligados (letra aceptante,
  pagaré signatario FR-098, avalista-reinforced amounts FR-095).
  (LB-012; EVID-566)
- **GT-CML-FR-112:** The system shall carry the acción cambiaria de
  regreso clock (last holder): prescribes in ONE YEAR, counted from
  the maturity date and, where applicable, from the close of the
  presentation periods or — if the title is with protest — from the
  date the protest was raised; the anchor selector records which of
  the three starting points applies per instrument state
  (presentation-window closure feeds from FR-096/FR-099 clocks;
  protest date from FR-094/FR-107). (LB-012; EVID-566)
- **GT-CML-FR-113:** The system shall carry the obligado-recourse
  clock: the obligated party's regreso action against the other
  prior obligados prescribes in SIX MONTHS, counted from the date of
  voluntary payment or the date of notification of the demanda
  (claim) — anchor = payment event or service-of-claim event on the
  recourse chain, recorded per paying obligado. (LB-012; EVID-566)
- **GT-CML-FR-114:** The system shall carry the enriquecimiento
  (unjust enrichment) follow-on clock: the holder's action to demand
  from the creator the sum by which the creator enriched itself to
  the holder's detriment prescribes in ONE YEAR from the day the
  cambiaria action extinguished — a chained clock whose anchor is the
  expiry of the applicable FR-111/FR-112 clock, computed only after
  that expiry is recorded. (LB-012; EVID-566)
- **GT-CML-FR-115:** The system shall carry the cheque clock: cambiaria
  actions derived from the cheque prescribe in SIX MONTHS — the last
  holder's counted from PRESENTATION, the endorsers' and avalistas'
  from the DAY AFTER the day they pay the cheque; dual anchor per
  party role on the cheque record (presentation event feeds from the
  art.-502 window, FR-099). (LB-008; EVID-563)
- **GT-CML-FR-116:** The system shall carry the cheques de viajero
  clock: cambiaria actions against the issuer or circulator of
  traveller's cheques prescribe in TWO YEARS from the date the
  cheques were issued — anchor = issuance date on the traveller
  cheque record. (LB-013; EVID-567)
- **GT-CML-FR-117:** The system shall carry the obligaciones/
  debentures INTEREST clock: actions to collect the interests
  prescribe in FIVE YEARS (anchor per the evidence gloss: no
  statutory anchor printed — the config row carries the term with the
  anchor left to the instrument's own terms/Civil fallback, flagged
  in §7). GOQ-147 annotation (EVID-950): the 5y period is CCom-FIXED
  special law (CC art. 1516 defers — the Civil 5y of art. 1508 is NOT
  its source); the Civil Code supplies only the MECHANICS CCom 577
  omits where silent — interruption causes and full restart (CC
  1506/1507), suspension (CC 1505) — with the CC post-2008
  consolidation caveat riding the mechanics, not the period.
  (LB-013; EVID-567; EVID-950)
- **GT-CML-FR-118:** The system shall carry the obligaciones/
  debentures PRINCIPAL clock: actions to collect the principal
  prescribe in TEN YEARS (same anchor note as FR-117). GOQ-147
  annotation (EVID-950): the 10y is CCom's own for debenture
  principal — CC art. 856 (10-year hipoteca clock, LB-016) is NOT its
  source (coincidental match only); same Civil-mechanics note as
  FR-117. (LB-013; EVID-567; EVID-950)
- **GT-CML-FR-119:** The system shall carry the transporte clock:
  actions derived from the transport contract prescribe in SIX
  MONTHS, counted from the end of the journey or from the date the
  passenger or the carried goods should have arrived at destination —
  dual anchor (journey-end event / expected-arrival date) on
  transport-backed records incl. carta de porte/conocimiento
  (FR-100). (LB-013; EVID-567)
- **GT-CML-FR-120:** The system shall carry the seguro clock: ALL
  actions deriving from an insurance contract prescribe in TWO YEARS
  from the date of the originating event (acontecimiento que les dio
  origen). (LB-013; EVID-567)
- **GT-CML-FR-121:** The system shall carry the fianza clock: the
  beneficiary's actions against the afianzadora (surety), and the
  surety's against contrafiadores and reafianzadoras, prescribe in
  TWO YEARS. (LB-013; EVID-567)
- **GT-CML-FR-122:** The system shall carry the old-code catch-all
  clock with the R65 citation guard: actions proceeding from the
  obligations of the old code's surviving maritime book lacking a
  stated prescription term last FIVE YEARS — cited as **D2946 (old
  code) art. 1313** (appendix pp. 298-301), NEVER as D2-70 (numbering
  collision with D2-70's own arts. 800s-1000s); the row applies only
  to old-code maritime obligations and never seeds a general
  commercial 5-year period (FR-110 guards). (LB-013; EVID-567; R65)
- **GT-CML-FR-123:** The system shall carry the prescription-regime
  discipline rows: caducidad terms are never interrupted and are
  suspended only by fuerza mayor (art. 625, per the evidence gloss);
  the títulos prescription articles run through an interruption
  regime (arts. 626-629 per the EV05a specials inventory — gloss);
  where CCom is silent on mechanics, the Civil Code now supplies them
  (GOQ-147, EVID-934/935/950 via CCom art. 1 + CC 1516): suspension in
  the five art.-1505 status relationships, interruption by the three
  art.-1506 causes (notified judicial demand / recognition /
  interest-amortization or partial payment) with the full-restart
  effect of art. 1507 — EXCEPT where CCom fixes its own divergence
  (CCom art. 629: cambiaria interruption against one co-debtor does
  NOT extend to the others, unlike the CC solidarity mechanics of
  arts. 1351/1361-1362 — CCom governs for títulos; CC mechanics ride
  with the post-2008 consolidation caveat); and transitorio X non-retroactivity — this Code's
  prescription provisions do NOT apply where prescription had already
  begun running under the prior law, so pre-vigencia (pre-1971-01-01)
  instruments resolve their clocks against the prior regime
  (informational; no candidate computation derives from it per the
  evidence gloss). (LB-014; EVID-517; EVID-566)
- **GT-CML-FR-124:** The system shall surface prescription aging on
  receivables/payables: each instrument-backed and contract-backed
  open item carries its prescription class (FR-111..FR-122), the
  computed anchor date, the computed expiry date
  (snapshot-on-write: class + term + anchor + instrument provenance
  stored on the record), and an expired/pending-state readable by the
  aging surfaces and by the Task 7 retention/destruction matrix
  (forward ref, file + cluster — it consumes these ids); anchor
  selection per class follows the FR text exactly (maturity /
  presentation-close / protest / payment / issuance / journey-end /
  originating-event / enrichment-chaining), never a single global
  anchor. (LB-012; LB-013; EVID-566; EVID-567)
- **GT-CML-FR-125:** The system shall key the destruction gate to the
  per-instrument prescription ladder: documents concerning determined
  acts or negotiations may be cancelled or destroyed only once the
  prescription period of the actions derived from them has elapsed
  (art. 383.1) AND never while any matter concerning them directly or
  indirectly is pending (art. 383.2 — pending-matter hold), with the
  archive/custody system at the merchant's discretion (art. 384);
  the prescription keys are THIS file's FR-111..FR-122 rows and the
  gate predicate is consumed from `../chart-of-accounts/01_books-anchor.md`
  GT-COA-FR-028 by id — commercial prescription here is DISTINCT
  from tax prescription (`../taxation/06_ct-procedures.md`
  GT-TAX-FR-232, cited by id: CT 112/112-"A" prescription-anchored
  conservation), and the max-per-regime resolution per document type
  is owned by the Task 7 matrix, never computed in this file.
  (LB-014; EVID-517)

## 4. Data Model

The dated rows of the ladder serialize as machine-readable config at
Task 7's matrix deliverable (consumption contract for
`../chart-of-accounts/03_retention-destruction-matrix.md`: columns
class, term, unit, anchor_kind, instrument, article, valid_from,
flags — one row per FR-111..FR-122 clock).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.titulo | instrument_type | select | letra_cambio · pagaré · cheque · cheques_viajero · obligacion_debenture · cert_deposito · bono_prenda · carta_porte · conocimiento · factura_cambiaria · cedula_hipotecaria · bono_bancario · cert_fiduciario · accion (pointer → GT-CML-FR-047) | FR-086 |
| l10n_gt_commerce.titulo | circulation_class | select | nominativo · a_la_orden (default, art. 418) · al_portador | FR-089 |
| l10n_gt_commerce.titulo | general_requisites_state | json | art.-386 five items checklist + series-signature mode; omission outcome = negotiability strip, negocio stands | FR-087 |
| l10n_gt_commerce.titulo | face_amount_resolution | selection + basis | words_prevail · lesser_sum (art. 388) + stored basis | FR-088 |
| l10n_gt_commerce.endoso | endosatario · class · place · date · endorser_sig · blank | m2o / select / char / date / char / bool | class: propiedad · procuración · garantía; partial → rejected (nulo); chain-integrity state per art. 430 | FR-090, FR-091, FR-092 |
| l10n_gt_commerce.aval | avalista · amount · amount_is_total_default | m2o / monetary / bool | default = full importe (art. 402); solidarity note art. 398 (gloss) | FR-095 |
| l10n_gt_commerce.protesto | kind · date · waiver_sin_protesto · titulo_ejecutivo_flag | select / date / bool / bool | kind: falta_aceptación · falta_pago; art. 399 dispensa; art. 1039 gloss flag | FR-094, FR-107 |
| l10n_gt_commerce.titulo (letra) | maturity_form · acceptance_due | select / date | a_la_vista · tiempo_vista · tiempo_fecha · día_fijo; tiempo_vista → +1 year presentation (art. 451) | FR-096 |
| l10n_gt_commerce.titulo (letra) | interest_rate · rate_source | monetary / select | stipulated · default_6pct (art. 442; vista/tiempo-vista only) | FR-097 |
| l10n_gt_commerce.titulo (pagaré) | installment_schedule_ids | o2m | number/due/amount rows (art. 595 analog via art. 491 amortizaciones) | FR-098 |
| l10n_gt_commerce.titulo (cheque) | drawee_bank · creation_date · presentation_window_end · revocable_from | m2o / date / date / date | bank-only; 15 calendar days (art. 502); revocation gate post-window (art. 507) | FR-099 |
| l10n_gt_commerce.factura_cambiaria | real_delivery_basis · accepted_original_state · plaza_class | selection / selection / select | actual · simbólica; pending/returned-accepted/refused; misma_plaza · diferente_plaza | FR-101, FR-105 |
| l10n_gt_commerce.factura_cambiaria | requisites_state · titulo_character | json / bool | art.-594 four items; false → degraded document (negocio valid, título lost) | FR-102 |
| l10n_gt_commerce.factura_cambiaria | abono_ids · partial_payment_notes | o2m / text | número/vencimiento/monto (art. 595); on-face partial payments | FR-103 |
| l10n_gt_commerce.factura_cambiaria | dispatch_state · dispatch_deadline | select / datetime | certified-mail w/ aviso (art. 597); 3 días from libramiento, ≤48 h from despacho (art. 596) | FR-104 |
| l10n_gt_commerce.factura_cambiaria | acceptance_deadline · rejection_reason | date / select | 5 d misma plaza / 15 d diferente (art. 599); art.-600 four grounds | FR-105, FR-106 |
| l10n_gt_commerce.prescription_class (dated config) | class · term · anchor_kind · instrument · article · valid_from · flags | config rows | cambiaria_directa_3y (626) · cambiaria_regreso_1y (627) · obligado_recourse_6m (628) · enriquecimiento_1y (409) · cheque_6m (513) · viajero_2y (541) · debenture_intereses_5y (577) · debenture_principal_10y (577) · transporte_6m (799) · seguro_2y (916) · fianza_2y (1037) · oldcode_maritime_5y (D2946 art. 1313, R65 flag) · cc_fallback (art. 1 → CC 1508: 5y from exigibility; Dto-Ley 106 consolidated ≥26-ago-2008 — post-2008 caveat; dies-a-quo kit 1508/1509/1511/1512; mechanics 1505-1507; specials menu LB-016: 1514.1/.2/.4 2y, 1515 3y, 1513/1628/1300/1727 1y, 856 10y) · pointer rows: acciones_amortizadas_10y (STATUTORY: CCom 577 ¶2 — 10 años desde la primera publicación exigida por art. 569; owned cml02) · liquidation_usac_5y (253, GT-CML-FR-069) | FR-110..FR-123 |
| account.move.line (aging surface) | prescription_class · anchor_date · expiry_date · regime_snapshot | m2o / date / date / json | computed + snapshot-on-write; readable by aging + the T7 matrix | FR-124 |
| retention config (pointer) | destruction-gate keys | pointer | per-instrument prescription keys (this file) + pending-matter hold (art. 383.2); gate predicate = GT-COA-FR-028; max-per-regime = T7 matrix | FR-125 |

## 5. Odoo Mapping

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-086 | shared | l10n_gt_commerce.titulo catalog | instrument_type + art.-385 guard | Species list per evidence gloss; acciones pointer GT-CML-FR-047 |
| FR-087 | shared | l10n_gt_commerce.titulo | requisites_state | Validation outcomes recorded; no legal-effect computation |
| FR-088 | shared | l10n_gt_commerce.titulo | face_amount_resolution | Words/lesser-sum with stored basis |
| FR-089 | shared | instrument profile config | circulation_class → mechanics | a la orden default (art. 418) |
| FR-090 | odoo | l10n_gt_commerce.endoso | art.-421 four requisites | Nominativo register-inscription step included |
| FR-091 | odoo | l10n_gt_commerce.endoso | class/blank/purity checks | Partial endoso rejected at entry |
| FR-092 | odoo | endoso chain validation | unbroken-chain state | Gap blocks holder workflows pending cure |
| FR-093 | shared | issuance guard | money-bearer restriction | Needs law-permission basis configured |
| FR-094 | odoo | l10n_gt_commerce.protesto | kind/date/waiver | "sin protesto" waiver flag; art. 1039 gloss flag |
| FR-095 | odoo | l10n_gt_commerce.aval | avalista/amount | Default full (art. 402); art. 398 gloss note |
| FR-096 | shared | letra profile | maturity_form ×4 + art.-451 clock | Unstated → a la vista per gloss |
| FR-097 | shared | letra interest config | 6% default dated row | valid_from 1971-01-01; snapshot rate |
| FR-098 | shared | pagaré profile | maker = aceptante semantics | Feeds FR-111 direct-action side |
| FR-099 | shared | cheque profile | bank-only/sight/15 d/revocation gate | Stop-payment gate keyed to creation date |
| FR-100 | shared | species bounded profiles | existence-level rows | Detail deferred — non-OQ gap discipline |
| FR-101 | shared | factura cambiaria profile | real-delivery + acceptance workflow | Art. 592 one-instrument guard |
| FR-102 | shared | factura requisites config | art.-594 four items | Omission → negotiability strip only |
| FR-103 | odoo | factura abono rows + annotations | installment schedule | Drives per-installment anchors |
| FR-104 | odoo | factura dispatch tasks | 3 d / ≤48 h clocks | Certified-mail state (art. 597) |
| FR-105 | odoo | factura acceptance clock | 5 d / 15 d by plaza | From receipt date; non-return = refusal |
| FR-106 | shared | rejection-reason catalog | art.-600 four grounds | Closed catalog on refusal event |
| FR-107 | odoo | protesto (factura) | 2 días hábiles clock | Feeds FR-094 state + FR-112 anchor |
| FR-108 | shared | retention config row | 5 y issued facturas/copies | GOQ-124 kin; max-per-regime = T7; conservation duty, NOT a claim clock (EVID-950) — claim clocks 626/627 |
| FR-109 | shared | lineage guard config | field-ancestry map only | FEL duties = GT-EINV wave (file-level) |
| FR-110 | shared | fallback-clock row | no general CCom period; cc_fallback = CC 1508 5y from exigibility (dated, ≥26-ago-2008 caveat) | GOQ-147 resolved (92_); specials menu LB-016; R65-safe |
| FR-111 | shared | prescription_class row | directa 3y ← vencimiento | Snapshot-on-write |
| FR-112 | shared | prescription_class row | regreso 1y ← maturity/presentation/protest | Anchor selector per state |
| FR-113 | shared | prescription_class row | recourse 6m ← payment/demanda notice | Per paying obligado |
| FR-114 | shared | prescription_class row | enriquecimiento 1y ← cambiaria expiry | Chained clock |
| FR-115 | shared | prescription_class row | cheque 6m ← presentation / day-after-payment | Dual anchor by party role |
| FR-116 | shared | prescription_class row | viajero 2y ← issuance | — |
| FR-117 | shared | prescription_class row | debentures intereses 5y | Anchor open (gloss — §7); period CCom-fixed, mechanics CC 1505-1507 (EVID-950) |
| FR-118 | shared | prescription_class row | debentures principal 10y | Anchor open (gloss — §7); CC 856 NOT its source (EVID-950) |
| FR-119 | shared | prescription_class row | transporte 6m ← journey-end / expected arrival | Dual anchor |
| FR-120 | shared | prescription_class row | seguro 2y ← originating event | — |
| FR-121 | shared | prescription_class row | fianza 2y | — |
| FR-122 | shared | prescription_class row | old-code 5y catch-all | R65: "D2946 (old code) art. 1313" only |
| FR-123 | shared | regime-discipline rows | caducidad 625 (gloss) + 626-629 inventory (gloss) + CC mechanics 1505-1507 (EVID-934/935) + transitorio X | CCom 629 divergence governs for títulos |
| FR-124 | odoo | account.move.line aging fields | class/anchor/expiry/snapshot | Feeds aging surfaces + T7 matrix by id |
| FR-125 | shared | destruction-gate keys (pointer) | art.-383 gate keys + pending-matter hold | GT-COA-FR-028 consumes; GT-TAX-FR-232 disambiguation; T7 owns max-per-regime |

Version-regime notes (D12/D15/D16): all 66_-sourced rows resolve
as-of the domain anchor date with instrument provenance (D2-70 as
consolidated to 30-05-2006, GOQ-123 verification note riding every
citation family; vigencia 1971-01-01 per R45, consumed from
GT-COA-FR-030..032); the prescription ladder and species profiles are
D16 dated rows (valid_from 1971-01-01, no valid_to supersession
asserted from this corpus) with snapshot-on-write of class + term +
anchor + instrument on every recorded fact; the 6% default interest
and every clock term are stored values, never hardcoded constants;
transitorio X (FR-123) keys pre-1971 instruments to the prior regime
without computing it. No saas-layer row arises in C5: all logic is
dated config (shared) or bookkeeping/aging surfaces (odoo); no
SAT/RM portal interaction, screening ingestion or regime-cutover state
machine exists in this cluster.

## 6. Acceptance Criteria

- **AC-001:** Given any instrument record, when the art.-386
  requisites are evaluated, then all five general items plus the
  species particulars are checked with the outcome recorded, an
  unsubsanable omission leaves the underlying receivable/payable
  valid while stripping título-quality behaviors, and a
  words-vs-figures or repeated-amount discrepancy resolves
  words-prevail / lesser-sum with the basis stored.
  (FR-086..FR-088)
- **AC-002:** Given an a la orden title, when transfers are recorded,
  then each endoso carries the four art.-421 requisites, partial
  endosos are rejected, blank endosos and the three classes are
  supported, and a holder legitimizes only through an unbroken chain
  — a gap blocks protest/cobro/re-transfer pending cure. (FR-089..FR-092)
- **AC-003:** Given a money-payable instrument, when issuance as al
  portador is attempted without a configured law-permission basis,
  then the art.-438 guard fires; a nominativo transfer completes only
  with endoso AND register inscription. (FR-089, FR-093)
- **AC-004:** Given an instrument defaulting on acceptance or payment,
  when the protest workflow runs, then presentation + refusal is
  formalized as a protesto record (or suppressed only by a recorded
  "sin protesto, sin gastos" waiver), and an aval without an amount
  guarantees the full importe with the art.-1039 execution-title
  exposure flag available. (FR-094, FR-095)
- **AC-005:** Given a letra, when maturity is left unstated, then it
  resolves a la vista (per the evidence gloss); the four forms are
  the closed list; a tiempo-vista letra carries the 1-year
  acceptance-presentation clock; and an interest stipulation on a
  non-vista letra is rejected while a vista/tiempo-vista letra
  without a stated rate resolves to the 6% dated row with
  snapshot-on-write. (FR-096, FR-097)
- **AC-006:** Given a cheque record, when validated, then the drawee
  is a bank on bank forms, sight-only maturity cannot be overridden,
  the 15-calendar-day presentation window is computed from creation,
  and a stop order before the window's close is blocked by the
  art.-507 gate. (FR-099)
- **AC-007:** Given a factura cambiaria, when drawn without real
  (actual or symbolic) delivery or for a sale already documented with
  another título, then the guards fire; when issued missing any
  art.-594 requisite, then the record degrades to a non-negotiable
  document while the negocio stays valid; and when payment is in
  abonos, then the installment rows (number/due/amount) and on-face
  partial-payment annotations drive the maturity anchors.
  (FR-101..FR-103)
- **AC-008:** Given an issued factura cambiaria, when the lifecycle
  clocks run, then dispatch shows 3 días/≤48 h with the
  certified-mail state, the acceptance deadline reads 5 or 15 days by
  plaza from receipt, non-return past the window reads as refusal,
  refusal carries one of exactly four art.-600 grounds, and the
  non-acceptance protest clock reads 2 días hábiles past the window.
  (FR-104..FR-107)
- **AC-009:** Given the prescription config, when inspected, then
  exactly the per-instrument clocks exist (3 y / 1 y / 6 m cambiaria;
  1 y enriquecimiento; 6 m cheque; 2 y viajero; 5 y / 10 y
  debentures; 6 m transporte; 2 y seguro; 2 y fianza; D2946 old-code
  5 y flagged R65) each with its statutory anchor selector — and NO
  general commercial period exists anywhere in the CCom, the CC
  fallback row carrying the CC-1508 5-year value with its
  dated-instrument caveat (Dto-Ley 106 consolidated ≥ 26-ago-2008,
  GOQ-147 resolved), the acciones-amortizadas row carrying its
  statutory anchor (CCom 577 ¶2 — first art.-569 publication) and the
  USAC row consumed by GT-CML-FR-069 pointer. (FR-110..FR-123)
- **AC-010:** Given an open item, when aging is computed, then the
  record carries prescription class, anchor and expiry as a
  snapshot (class + term + anchor + instrument provenance), the
  cheque/transporte dual anchors select by party role or event, the
  enriquecimiento clock computes only after the cambiaria expiry is
  recorded, and pre-1971 instruments carry the transitorio-X
  prior-regime note instead of a computed D2-70 clock. (FR-124, FR-123)
- **AC-011:** Given a document covered by this cluster, when
  destruction is evaluated, then the gate reads the per-instrument
  prescription expiry AND the pending-matter hold (art. 383),
  resolves commercial keys from this file — never from GT-TAX-FR-232's
  tax clocks — and defers the max-per-regime outcome to the Task 7
  matrix by pointer. (FR-125)
- **AC-012:** Given any FEL/DTE behavior (emission, validation,
  certification, archive, contingency), when its legal basis is
  inspected, then nothing in this file's rows cites arts. 591-604 for
  it — the lineage row records only the field-level ancestry
  (serial number, buyer ID/domicile, goods, unit/total prices) and
  points to the GT-EINV wave files. (FR-109)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md`
§C); this file owns NO new GOQ (no unregistered question is treated
as an open question). GOQ-123 rides every 66_ citation family above
(kin — owned by `01_books-anchor.md` GT-COA-FR-031). GOQ-124 (the
retention/destruction max-per-object matrix) is the Task 7
deliverable — this file's ladder rows FR-108/FR-110..FR-125 feed it
by pointer and its open texture (Civil fallback, art.-604 supersession
by the tax corpus, max-per-regime) is absorbed there. GOQ-122 (D-43-70
dated-row completion) is consumed from GT-COA-FR-030..032 by id.
GOQ-147 (the Civil-fallback/scattered-clocks question) is RESOLVED
below (OQ-003) — the Código Civil landed in-corpus as 92_ on
2026-08-22.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-123 (kin): "CCom post-May-2006 reform watch: consolidation horizon D-11-2006; later reforms absent (known: art. 343 = D-18-2017) — verification note rides every 66_ citation." All C5 rows cite the consolidated print; any post-2006 reform of Libro III arts. 385-628 or the prescription articles re-opens the affected FRs (esp. the clocks and the art.-604 retention row). | no | GT synthesis wave S-GT5 → W6 partner ask (owner: `01_books-anchor.md` FR-031; this file kin-cites) | open |
| OQ-002 | GOQ-124 (kin): "Retention/destruction max-per-object matrix (synthesis deliverable): art. 383 keys destruction to 'prescripción de las acciones' but CCom enacts no general period (art. 1 → Civil); practical floor = tax corpus (CT 112'A, 4y+); factura cambiaria art. 604 5y likely superseded — write the matrix in the S-GT5 file." The matrix is Task 7's file (`../chart-of-accounts/03_retention-destruction-matrix.md`, forward ref); FR-108/FR-110/FR-125 supply this file's commercial keys and never resolve max-per-regime locally. | no | GT synthesis wave S-GT5 → Task 7 writer (matrix file) | open |
| OQ-003 | GOQ-147 (kin; owner: S-GT5 gap report/HANDOVER §5l): "CCom scattered prescription clocks lack corpus-anchored starting events: art. 604 factura-cambiaria retention (drawing-date = system convention); art. 577 debentures intereses/principal clocks; acciones-amortizadas 10y gloss-only — and the Código Civil corpus is absent, so fallback clocks (commercial-legal/03 FR-110 negative-FR) stay open. [ACQUIRED 2026-08-22: Código Civil Dto-Ley 106 = 92_.]" **RESOLVED by 92_ (EVID-931..951)**: FR-110 rewritten in place as the fallback-clock FR (CC art. 1508 "cinco años, contados desde que la obligación pudo exigirse" + 1516 gateway + dies-a-quo kit 1509-1512 + mechanics 1505-1507 + specials menu LB-016); art. 604 retyped as a conservation/retention duty, not a claim clock (claim clocks = 626/627 — EVID-950); acciones-amortizadas upgraded to statutory (CCom 577 ¶2); 577 periods CCom-fixed with Civil mechanics only (CC 856 not the 10y source). SURVIVING SUB-GAPS: (i) consolidation horizon = 26-ago-2008 — post-2008 CC reforms unverifiable from the ONSEC edition (verify arts. 1500-1516, 856 and the garantías zone against a current consolidated text before modeling — EVID-951 OQ-3); (ii) LGM-deference tension in the prenda/hipoteca zone (D51-2007 footnotes on arts. 916/1124 — EVID-932 OQ-1); (iii) 1514.2 vs título-clock boundary for semi-formalized credits (facturas no cambiarias) stated as a modeling assumption, not resolved by text (EVID OQ-7). | no | Controller (register write-back) + S-GT5 (rows landed); acquisition queue: current consolidated CC text | resolved |
