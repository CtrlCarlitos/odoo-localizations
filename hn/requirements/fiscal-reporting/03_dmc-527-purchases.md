# HN — Fiscal reporting — DMC 527 (Declaración Mensual de Compras): line contract, sujetos & deadline chain

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' monthly
purchases informativa, the **Declaración Mensual de Compras del Impuesto
Sobre Ventas (DMC)** — *Monthly Purchases Declaration* — cluster F3 of the
W2 evidence. It owns: the form identity (**527**, R-H25: "Declaración
Jurada Informativa Mensual de Compras", superseding the annual
*Declaración Anual de Créditos* DEI-525 from Jan-2016); the **sujetos
obligados** rule (grandes/medianos contribuyentes + regímenes especiales
+ exempt-operations taxpayers + State institutions since Oct-2019); the
**deadline chain** as dated rows — 10 días (DEI-SG-276-2015) → 20 días
(CPAT-SG-073-2016, repealed) → **5 días calendario (SAR-237-2024,
current, R-H17)** — with the stale-manual "ocho (8) días" guard (R-H18)
and the DMC-before-ISV/DJIMR sequencing (R-H36); the field-level **line
contract** of the three sheets — 527-52 (mercado interno, casilla 600
FA/OC), 527-53 (FYDUCA), 527-54 (importaciones/DUA with the
Centroamérica vs fuera-de-la-región base split) — including the line key
(RTN 14-char + CAI ≤37 chars + 4-segment document number + dual dates
emisión/contable) and the crédito-fiscal vs costos/gastos/no-deducible
classification (casillas 270/280/290, Art. 12 pro-rata consumed by id
from taxation/06); the *compras eventuales* (occasional purchases,
DEI-279-2015 code-10 buyer-issued voucher) DMC registration interface
with its deliberately-open retention rate; the single consolidated
filing per RTN-period; and the go-live reconciliation of imported legacy
purchases against the previous system's DMC filings (D-H3).

It does **not** cover: the OVI/SW declaration chassis, acuse/estado
machinery and the fiscal-calendar due-day engine — owned by
`fiscal-reporting/01` (cluster F1) and consumed by id; the ISV
determinativa 201 and the 131/132/133 Sección-B auto-feed that the DMC
powers — owned by `fiscal-reporting/05` (cluster F5), cross-referenced
by id; the DJIMR/DMR retention declarations (cluster F2,
`fiscal-reporting/02`); ISV credit semantics themselves (4-month window,
pro-rata trichotomy, ISR-cost bar) — owned by
`../taxation/06_isv.md` (HN-TAX-FR-211..255) and consumed by id, never
re-derived here; the correlativo/CAI grammar and the code-10 collision
guard — owned by `../e-invoicing/01_document-types-numbering.md`
(HN-EINV-FR-001..031) and consumed by id; the *compras eventuales*
document-emission mechanics (type-10 format, provider-ID flexibility,
seller 10-SMM gate — EV13:EVID-085/086) — e-invoicing wave territory;
and CT sanctions computation (multa/intereses engines = taxation/01).

## 2. Legal Basis

Authority order (binding, per master evidence index): SAR-343-2019 +
DEI-SG-276-2015 > per-código Ayudas (`45_`/`72_`) > `71_` Generalidades
per-row (R-H27); SAR-237-2024 (`20_`) is the current DMC procedure
instrument (deadline + forma + repeal of CPAT-073-2016). Manuals are
STALE where they conflict with gazette text (R-H18 family — gazette text
is the record). D-H1/D-H2/D-H3 bind this cluster; all deadlines are días
CALENDARIO unless the instrument says hábiles.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo DEI-SG-276-2015, PRIMERO y SEGUNDO num. 1 (SUJETOS OBLIGADOS) | Creates the "Declaración Jurada Informativa denominada 'Declaración Mensual de Compras del Impuesto Sobre Ventas (DMC)'" inside DET LIVE; sujetos: "todos los sujetos pasivos obligados a la presentación y/o pago de la Declaración del Impuesto sobre Ventas, clasificados como grandes o medianos contribuyentes incluyendo los acogidos a Regímenes Especiales y demás contribuyentes que ejerzan operaciones comerciales exentas, deben informar todas las compras realizadas en el mercado interno y sus importaciones gravadas y no gravadas con el Impuesto sobre Ventas, efectuadas en el mes" | All purchases of the month (local + imports, taxed or not) reported by grandes/medianos, special regimes and exempt operators | `hn/sources/15_Acuerdo_DEI-SG-276-2015_DMC.pdf` | PRIMERO/SEGUNDO-1 pp.2-3 (EV13:EVID-081) |
| LB-002 | Acuerdo DEI-SG-276-2015, SEGUNDO nums. 2-4, TERCERO, CUARTO + considerandos | FORMA: "deben separar al momento de presentar la misma, las compras que generan Crédito Fiscal de las que son incluidas en los costos y/o gastos de su contabilidad"; original PLAZO "dentro de los primeros diez (10) días calendarios del mes siguiente en que se efectuaron las compras internas o las importaciones", first filing "en los primeros diez (10) días del mes de marzo de 2016"; SANCIONES per CT; purpose: DMC = "insumos a la Administración Tributaria para una validación automática del crédito fiscal, costos y gastos"; CUARTO repeals DEI-SG-030-2012 (form DEI-525, Declaración Anual de Créditos) | Form/purpose/original deadline/credit-vs-cost split; pre-2016 history = annual credits declaration | `hn/sources/15_Acuerdo_DEI-SG-276-2015_DMC.pdf` | SEGUNDO 2-4/TERCERO/CUARTO pp.2-3 (EV13:EVID-082) |
| LB-003 | Acuerdo CPAT-SG-073-2016, PRIMERO (16-ago-2016, G 34,127) | Considerando: day-10 saturation — "el día diez (10) de cada mes se produce el vencimiento del plazo para la presentación de la Declaración del Impuesto sobre Ventas, Declaración Mensual de Retenciones (DMR) y Declaración Mensual de Compras (DMC)"; PRIMERO rewrites the plazo: "dentro de los primeros veinte (20) días del mes siguiente en que se efectuaron las compras internas o las importaciones" | Interim 20-day regime (Sep-2016 → May-2024); side-fact: the 2016 day-10 cluster corroborates the ISV/DMR day-10 anchors; later repealed by SAR-237-2024 CUARTO | `hn/sources/16_Acuerdo_CPAT-SG-073-2016_DMC_mod.pdf` | PRIMERO p.2 (EV13:EVID-083) |
| LB-004 | Acuerdo SAR-343-2019, PRIMERO y TERCERO (22-jul-2019, G 35,014) | Adds to the sujetos "a las Instituciones del Estado, que realicen compras en el mercado interno y externo, sean estas gravadas o no ... indistintamente de su categoría"; effective "una vez transcurridos dos (2) meses contados a partir de la fecha de su publicación" (published 5-ago-2019 → effective ~5-oct-2019) | State institutions join the DMC obligados from Oct-2019 (CT Art. 30.2.b contribuyentes) | `hn/sources/17_Acuerdo_SAR-343-2019_DMC_reforma.pdf` | PRIMERO/TERCERO p.2 (EV13:EVID-084) |
| LB-005 | Acuerdo SAR-237-2024 (10-may-2024, G 36,538), rewritten ordinals numerales 2-4 + CUARTO/QUINTO | FORMA 2.I: "se deben separar las compras que generan crédito fiscal de las compras que son incluidas en los costos y/o gastos de su contabilidad"; 2.II: "La presentación de esta declaración informativa deberá realizarse a través de la Oficina Virtual o del Servicio Web"; PLAZO 3: "La ... (DMC) debe presentarse dentro de los primeros cinco (05) días calendarios del mes siguiente al que se efectuaron las compras internas o las importaciones"; SANCIONES 4 per CT + Boletín de Pago; CUARTO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo No. CPAT-SG-073-2016"; QUINTO: the rest of DEI-SG-276-2015 and SAR-343-2019 stays in force | CURRENT DMC regime (from 20-may-2024): 5 días calendario, dual channel, credit/cost split restated, CPAT-073 repealed | `hn/sources/20_Acuerdo_SAR-237-2024_retenciones_mod.pdf` | Rewritten ordinals pp.3-4 (EV13:EVID-090) |
| LB-006 | Acuerdo DEI-SG-279-2015, CUARTO y QUINTO | Buyer obligations on compras eventuales: "El contribuyente adquirente está obligado a retener y enterar al Fisco el Impuesto Sobre Venta que cause las Compras de Bienes y/o Servicios. La declaración y entero de este impuesto se hará en el plazo que la ley establece."; must "registrar las adquisiciones eventuales ... en la Declaración Jurada Informativa Mensual de Compras ... dentro de los primeros diez (10) días calendarios del mes siguiente que se efectuó la compra" (2016 text, superseded for DMC timing by LB-005); CUARTO: emission "podrá ser condicionado o limitada ... conforme al comportamiento tributario del Contribuyente Adquiriente" | Registration duty of eventual purchases in the DMC + buyer-ISV retention (rate unstated — 18_ OQ-6) | `hn/sources/18_Acuerdo_DEI-SG-279-2015_compras_eventuales.pdf` | QUINTO p.4 (EV13:EVID-087) |
| LB-007 | SAR Ayuda DMC-527 (print Agosto 2026), §I.1-I.3 | "La Declaración Mensual de Compras (DMC) es un formulario informativo contenido en el Acuerdo DEI-SG-276, de fecha 3 de diciembre de 2015, que sustituye la Declaración Anual de Créditos (DAC) a partir de enero de 2016. En este formulario se consignan, de manera cronológica, los comprobantes de venta correspondientes a las compras realizadas en el período a declarar."; sujetos restated incl. State institutions; table: "Declaración Jurada Informativa Mensual de Compras | 527 | Informativa | Oficina Virtual o Servicio Web (SW)" (citing SAR-236-2024 DÉCIMO SÉPTIMO); footnote: "podrán presentarse mediante Servicio Web u Oficina Virtual; no obstante, deberá utilizarse de forma continua una sola modalidad." | Form identity 527 (R-H25), informativa character, chronological per-comprobante content, dual channel with sticky modality | `hn/sources/45_Ayuda_DMC.pdf` | §I.1-I.3 pp.4-5 (EV43:EVID-143) |
| LB-008 | SAR Ayuda DMC-527 §I.5 + Generalidades DMC §2 vs SAR-237-2024 dispositive text | Manuals print: "debe presentarse dentro de los primeros ocho (8) días calendario del mes siguiente a[l] que [...] se efectuaron las compras internas o las importaciones, de conformidad con el Acuerdo N.º SAR-237-2024" — while the very acuerdo's text says "cinco (05) días calendarios" (LB-005); both manuals hedge "la Administración Tributaria podrá efectuar modificaciones posteriores"; 72_ §4 "El único medio de presentación ... es Oficina Virtual" likewise contradicts the dual channel (stale, R-H27); 72_ base-legal list omits SAR-237-2024 (stale cluster, 72_ OQ-3) | The stale-print conflict of record: gazette text (5 días, dual channel) governs; manuals' 8 días / OVI-only never encoded (R-H18/R-H27) | `hn/sources/45_Ayuda_DMC.pdf`, `hn/sources/72_Generalidades_DMC.pdf` | 45_ §I.5 p.6; 72_ §2/§4 pp.2-3 (EV43:EVID-144; EV43:EVID-143) |
| LB-009 | SAR Ayuda DMC-527, hoja "Detalle de Compras Locales y Otros Comprobantes de Pago (527-52)" | Casilla 600 Clase de documento: "seleccione si el documento fiscal de la compra corresponde a: a) FA-Factura; o b) OC-Otros comprobantes de pago." FA mandatory: 200-RTN "Debe contener catorce (14) caracteres y no debe incluir guiones"; 7-CAI "con una longitud máxima de treinta y siete (37) caracteres ... Debe estar separada por guiones. Ejemplo: 19AB25-ED1000-1D76E0-632D08-14ACAF-9D"; 8-N.º de documento (establecimiento/punto de emisión/tipo de documento/correlativo) "Los segmentos deben estar separados por plecas. Ejemplo: 001/007/01/00000001"; 900-Fecha de emisión; 100-Fecha contable ("correspondientes a la contabilización del documento"); optional: 140-N.º OCE (SEFIN), 110-Importe exento, 130-N.º de resolución (SEFIN), 120-Importe exonerado, 1511-Importe base 15%, 1611-Importe base 18%, 270-Monto al costo / 280-Monto al gasto ("el valor total de la base imponible más el impuesto del comprobante de compra que no será utilizado como crédito fiscal ... conforme al prorrateo del crédito fiscal establecido en el artículo 12 de la Ley del Impuesto Sobre Ventas"), 290-Valor no deducible. OC class: "podrán registrarse recibos de servicios públicos, documentos del sistema financiero y de seguros, boletos de transporte aéreo de pasajeros y otros documentos autorizados por el SAR"; OC mandatory drops CAI, uses "2. 71-N.º de documento: consigne el número del documento equivalente" | The 527-52 line contract: identity fields, fiscal-document key, dual dates, taxability bases, and the 270/280/290 classification split | `hn/sources/45_Ayuda_DMC.pdf` | Hoja 527-52 pp.11-13 (EV43:EVID-145) |
| LB-010 | SAR Ayuda DMC-527, hojas 527-53 (FYDUCA) y 527-54 (Importaciones) | 527-53 mandatory: 301-Pasaporte o identificación CA; 501-Apellidos y nombre/razón social (proveedor extranjero); 901-Fecha de emisión; 101-Fecha contable; 190-N.º FYDUCA; optional: 201-RTN, 302-N.º identificador tributario mercantil, 141-N.º OCE, 111-Importe exento, 131-N.º de resolución, 121-Importe exonerado, 1512/1612-Importe base 15%/18%, 271/281-Monto al costo/gasto, 291-Valor no deducible. 527-54 (DUA) mandatory: 202-RTN, 902-Fecha de emisión, 102-Fecha contable, 20-N.º DUA ("consigne el número de la Declaración Única Aduanera (DUA)"); optional items 9-15: 1513-Importe base 15%, 1520-Importe base 15% fuera de la región centroamericana, 1613-Importe base 18%, 1620-Importe base 18% fuera de la región centroamericana, 272/282-Monto al costo/gasto, 292-Valor no deducible (items 5-8 not described in the print — OQ-007). Negative finding: no compras-eventuales/type-10 mention, casilla 600 offers only FA/OC, no ISV-amount or retention field exists in any sheet | FYDUCA/import line contracts with origin-specific keys and the CA vs fuera-CA base split (1513/1520, 1613/1620) | `hn/sources/45_Ayuda_DMC.pdf` | Hojas 527-53/54 pp.13-15 (EV43:EVID-146) |
| LB-011 | SAR Ayuda DMC-527, §2.3-2.5 + §III | SW upload: plantilla → orden de trabajo, "La orden podrá ser recibida con errores o sin errores", error-report PDF loop "deberá repetir el proceso de carga y envío de la plantilla hasta que la orden de trabajo sea recibida sin errores"; two-stage: "esta constituye una primera validación ... Una orden de trabajo finalizada sin errores no significa que la declaración ya haya sido presentada. ... verifique en el buzón electrónico de la Oficina Virtual si se generó un informe de errores durante la segunda validación"; OVI fichas mode with identical fields; rectification (quoting SAR-236-2024 DÉCIMO NOVENO): "Las Declaraciones Juradas Informativas deberán ser rectificadas haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original"; branches: "Las empresas que tengan sucursales deberán presentar una sola declaración con la información consolidada, debido a que no podrán presentar más de una declaración original o rectificativa."; plantilla mutability: "la estructura y los campos de la plantilla pueden ser modificados por la Administración Tributaria"; extemporánea: "indicará la multa y los intereses correspondientes"; RTN/nombres/montos/CAI/fechas/números de documentos all "formato texto", fechas "DD/MM/AAAA" | Filing mechanics: two-stage SW validation, fichas parity, same-modality rectification, single consolidated filing, plantilla versioning, cell formats | `hn/sources/45_Ayuda_DMC.pdf` | §2.3-2.5/§III pp.16-28 (EV43:EVID-147) |
| LB-012 | SAR Generalidades Créditos ISV, FAQ 2-3 (pp.3-4) | "Para los Grandes y Medianos Contribuyentes, los montos correspondientes a compras se consignan automáticamente en el formulario ... con base en los datos reportados en la DMC, en las siguientes categorías: • 131 – Compras en el mercado interno • 132 – FYDUCA • 133 – Importaciones" | The DMC→201 auto-feed categories (131/132/133) — consumption side owned by fiscal-reporting/05 (F5) | `hn/sources/70_Generalidades_creditos_ISV.pdf` | FAQ 2-3 pp.3-4 (EV43:EVID-150) |
| LB-013 | SAR Ayuda ISV 201 (print Junio 2026), §2.1 selección | Sequencing note when picking the 201: "En el Tipo de la declaración selecciona determinativa, recuerde previamente es la informativa de Declaración Mensual de Compra (DMC)."; 201 plazo: "dentro de los primeros diez (10) días calendario del mes siguiente a aquel en que se efectuaron las ventas" | DMC-first dependency edge (5d < 10d, R-H36) and the ISV day-10 anchor the chain hangs from | `hn/sources/43_Ayuda_ISV_201.pdf` | §2.1 p.7; §I.5 p.5 (EV43:EVID-137) |
| LB-014 | SAR Generalidades ISV, §1 (corroboration only) | Credit window: "el crédito fiscal solo podrá contabilizarse en el período fiscal correspondiente a la fecha en que dicho crédito se causó o en uno de los tres períodos mensuales inmediatamente siguientes a dicho período"; pro-rata: gravada-linked credit 100%, mixed "derecho al crédito fiscal en el porcentaje correspondiente a las ventas gravadas del período. El crédito relacionado con las operaciones exentas constituirá un costo o gasto" | Generalidades restatement of the Art.-12 mechanics — semantics owned by taxation/06 (HN-TAX-FR-242/243), cited here only as DMC-side corroboration for the 270/280 feed | `hn/sources/69_Generalidades_ISV.pdf` | §1 pp.2-3 (EV43:EVID-148) |

## 3. Functional Requirements

### 3.1 Form identity, sujetos & scope

- **HN-FREP-FR-086:** The system shall model the DMC as the "Declaración
  Jurada Informativa Mensual de Compras" — form code **527** (R-H25),
  INFORMATIVE (no payment workflow of its own), monthly, whose content is
  the chronological listing of the purchase *comprobantes de venta*
  (supporting fiscal documents) of the period — and shall record that it
  substituted the *Declaración Anual de Créditos* (DAC, form DEI-525 under
  repealed DEI-SG-030-2012) from January 2016, with pre-2016 annual-credits
  periods resolved under the superseded regime (dated regime rows, D-H2).
  (LB-002; LB-007; EV13:EVID-082; EV43:EVID-143; R-H25)
- **HN-FREP-FR-087:** The system shall flag the DMC-obligado status for:
  (a) every taxpayer obligated to the ISV declaration classified as grande
  or mediano contribuyente; (b) taxpayers acogidos a regímenes especiales;
  and (c) demás contribuyentes exercising exempt commercial operations
  (*operaciones comerciales exentas*) — and for obligados the DMC shall
  include ALL purchases of the month: mercado interno + importaciones,
  gravadas AND no gravadas (taxability never filters line inclusion).
  (LB-001; LB-007; EV13:EVID-081; EV43:EVID-143)
- **HN-FREP-FR-088:** The system shall carry the sujetos extension as a
  DATED row: State institutions (*Instituciones del Estado*, CT Art. 30.2.b
  contribuyentes) that make internal or external purchases, taxed or not,
  regardless of category, become DMC obligados from 2019-10-05 (SAR-343-2019
  published 5-ago-2019, effective two months after publication) — no
  institution shall be treated as obligado for periods before that date.
  (LB-004; EV13:EVID-084)
- **HN-FREP-FR-089:** The system shall classify every DMC line by ORIGIN
  CLASS exactly as the sheets do — `local` (sheet 527-52), `fyduca` (sheet
  527-53), `import` (sheet 527-54) — where FYDUCA covers *Factura y
  Declaración Única Centroamericana* purchases from foreign CA suppliers
  and import covers DUA-based importations, so that the three-sheet export
  never mixes origin classes in one row. (LB-007; LB-010;
  EV43:EVID-143/146)
- **HN-FREP-FR-090:** The system shall resolve the taxpayer-segment input
  (grande/mediano/pequeño + régimen especial + exempt-operator flags) as
  company-level dated configuration (snapshot-on-write, D15) feeding
  FR-087/FR-088, and shall surface a DMC-obligación checklist per
  RTN-period derived from it; segment classification itself is SAR-side
  attribute data, never computed by the system. (LB-001; LB-004;
  EV13:EVID-081/084)

### 3.2 Deadline chain & sequencing (dated rows, D-H2)

- **HN-FREP-FR-091:** The system shall encode the DMC presentation deadline
  as DATED rows resolved by the month following the purchase period, never
  overwritten: {valid 2016-02 (first filing: first 10 days of March 2016)
  → 2016-09: first **10 días calendario**} → {2016-09 → 2024-05-19:
  first **20 días** of the following month (hábil-vs-calendario default =
  calendario, OQ-002)} → {from 2024-05-20 (SAR-237-2024, G 36,538):
  first **5 días calendario** — CURRENT}, with CPAT-SG-073-2016 repealed
  (CUARTO) and the non-modified parts of DEI-SG-276-2015 + SAR-343-2019
  expressly surviving (QUINTO). (LB-002; LB-003; LB-005; EV13:EVID-082/
  083/090; R-H17)
- **HN-FREP-FR-092:** The system shall implement the stale-manual guard
  (R-H18): the deadline value for any period on or after 2024-05-20 is 5
  días calendario per the gazette text of SAR-237-2024, and the "ocho (8)
  días calendario" printed by the Agosto-2026 Ayuda (`45_`) and by
  `72_` — both attributing it to SAR-237-2024 — shall NEVER be loaded as a
  row; if a post-May-2024 instrument setting 8 días is ever acquired
  (LEAD, OQ-004), it enters as a NEW dated row appended to the chain, never
  by editing SAR-237-2024's. (LB-005; LB-008; EV13:EVID-090;
  EV43:EVID-144; R-H17/R-H18)
- **HN-FREP-FR-093:** The system shall enforce DMC-FIRST sequencing
  (R-H36; V-HN1 anchor trim: only the ISV-201 leg is evidenced — LB-010's
  276 text places the DMC "antes de la Declaración Determinativa [del
  ISV]"; the DJIMR/DMR-family ordering extension is an OQ, not law): the
  DMC (day-5) must be presented before the ISV determinativa
  201 of the same period (any ordering vs the day-10 DJIMR family =
  workflow configuration, never enforced), and
  the 201's Sección B purchase figures for grandes/medianos are
  auto-populated from the filed DMC in categories 131 (compras mercado
  interno) / 132 (FYDUCA) / 133 (importaciones) — the 201-side
  consumption, gate mechanics and non-obligado manual-entry fallback are
  owned by `fiscal-reporting/05` (F5, HN-FREP-FR-164..170 zone: Sección B
  credit map, DMC-fed lock vs manual entry) and consumed by id; this file
  owns only the DMC→131/132/133 feed shape. (LB-012; LB-013;
  EV43:EVID-137/150; EV13:EVID-083; R-H36)

### 3.3 Channel, consolidation & plantilla contract

- **HN-FREP-FR-094:** The system shall offer both filing channels — Oficina
  Virtual (interactive) o Servicio Web (batch plantilla upload) — per
  SAR-236-2024 DÉCIMO SÉPTIMO/OCTAVO + SAR-237-2024 numeral 2.II, with a
  STICKY single-modality setting per taxpayer ("deberá utilizarse de forma
  continua una sola modalidad"), and shall never encode `72_` §4's
  "único medio ... Oficina Virtual" (stale, R-H27); channel machinery
  itself (login, acuse CSV+QR, estado pill) is consumed from
  `fiscal-reporting/01` (F1) by id. (LB-005; LB-007; LB-008;
  EV13:EVID-090; EV43:EVID-143; R-H27)
- **HN-FREP-FR-095:** The system shall model the Servicio Web two-stage
  validation pipeline: plantilla upload → *orden de trabajo* receipt (con
  errores / sin errores) with downloadable error-report PDF and a
  correct-and-reupload loop until error-free — noting that a clean orden is
  only the FIRST validation ("Una orden de trabajo finalizada sin errores
  no significa que la declaración ya haya sido presentada") — followed by a
  SECOND validation whose error report lands in the OVI *buzón
  electrónico*; the interactive OVI *fichas* mode shall expose exactly the
  same fields as the plantilla (parity invariant). (LB-011;
  EV43:EVID-147)
- **HN-FREP-FR-096:** The system shall produce ONE consolidated DMC filing
  per RTN per period: companies with branches (*sucursales*) consolidate
  all establishment data into a single declaration and "no podrán presentar
  más de una declaración original o rectificativa" — a second original for
  the same RTN-period is structurally impossible, and branch-level detail
  survives only as internal line attributes, never as separate filings.
  (LB-011; EV43:EVID-147)
- **HN-FREP-FR-097:** The system shall lock DMC rectification to the
  modality of the original filing (SAR-236-2024 DÉCIMO NOVENO, quoted by
  the Ayuda): a declaration presented via SW is rectified via SW, one via
  OVI via OVI; the filed original is a frozen snapshot (D-H2.5) and the
  rectificativa supersedes it as a new dated record, with the side-by-side
  original-vs-corrected diff surface owned by `fiscal-reporting/01` (F1).
  (LB-011; EV43:EVID-147)
- **HN-FREP-FR-098:** The system shall pin a plantilla VERSION for every
  SW export: the structure and fields "pueden ser modificados por la
  Administración Tributaria", so each export records the plantilla version
  it targeted, and a plantilla change is a new version row — never an
  in-place mutation of a version already used by a filed declaration; all
  identity/amount cells serialize as TEXT ("formato texto") with dates as
  DD/MM/AAAA. (LB-011; EV43:EVID-147; OQ-009)

### 3.4 Sheet 527-52 line contract (local purchases)

- **HN-FREP-FR-099:** The system shall classify every local-purchase line
  through casilla 600 *Clase de documento* with exactly two values: **FA**
  (*Factura* — fiscal invoice carrying a CAI) or **OC** (*Otros
  comprobantes de pago* — other payment documents: "recibos de servicios
  públicos, documentos del sistema financiero y de seguros, boletos de
  transporte aéreo de pasajeros y otros documentos autorizados por el
  SAR", an open-ended list — OQ-006); no third class exists in the print
  and none shall be invented. (LB-009; LB-010; EV43:EVID-145/146)
- **HN-FREP-FR-100:** The system shall key every FA line by the supplier
  identity triple: (a) 200-RTN validated as exactly 14 characters, no
  guiones; (b) 7-CAI stored and validated at ≤37 characters, guion-separated
  (example of record: `19AB25-ED1000-1D76E0-632D08-14ACAF-9D`); (c)
  8-N.º de documento as the 4-segment
  establecimiento/punto-de-emisión/tipo-de-documento/correlativo value,
  pleca-separated (example of record: `001/007/01/00000001`). Grammar
  composition, wrap, no-FY-reset and the 14↔16-digit historical parser are
  consumed BY ID from `../e-invoicing/01_document-types-numbering.md`
  (HN-EINV-FR-012..FR-019, FR-020..FR-022) — never re-implemented here;
  the DMC stores and validates the printed value against that grammar.
  (LB-009; EV43:EVID-145)
- **HN-FREP-FR-101:** The system shall record BOTH dates on every line —
  *fecha de emisión* (900/901/902 per sheet) and *fecha contable*
  (100/101/102 per sheet, "correspondientes a la contabilización del
  documento") — and shall feed the *fecha contable* as the credit-window
  anchor consumed from taxation/06 (HN-TAX-FR-242: cause month + 3
  following months) when classifying expired-window credits; the choice of
  which date assigns a line to the declaration month is carried as OQ-008.
  (LB-009; LB-010; LB-014; EV43:EVID-145/146/148)
- **HN-FREP-FR-102:** The system shall carry the exempt/exonerated buckets
  with their legal backing: 110/111-*Importe exento* plus (optional)
  140/141-*N.º OCE* (the SEFIN-issued *Orden de Compra Exenta*) and
  120/121-*Importe exonerado* plus (optional) 130/131-*N.º de resolución*
  (SEFIN); exonerated amounts shall not be accepted without their
  resolution/OCE reference fields offered by the sheet. (LB-009; LB-010;
  EV43:EVID-145/146)
- **HN-FREP-FR-103:** The system shall model the taxability bases as
  SHEET-SPECIFIC casillas with NO ISV-amount column anywhere (negative
  finding: bases only, credit derived by SAR): 527-52 → 1511 (base 15%) /
  1611 (base 18%); 527-53 → 1512/1612; 527-54 → 1513 (base 15% CA) / 1520
  (base 15% fuera de la región centroamericana) / 1613 (base 18% CA) /
  1620 (base 18% fuera de la región centroamericana); no line shall carry
  a computed ISV figure into the DMC export. (LB-009; LB-010;
  EV43:EVID-145/146)
- **HN-FREP-FR-104:** The system shall compute the mandatory
  classification split per line — 270/271/272 *Monto al costo* and
  280/281/282 *Monto al gasto* = "el valor total de la base imponible más
  el impuesto del comprobante de compra que no será utilizado como crédito
  fiscal ... conforme al prorrateo del crédito fiscal establecido en el
  artículo 12 de la Ley del Impuesto Sobre Ventas", plus 290/291/292
  *Valor no deducible* — by CONSUMING the Art.-12 classifier from
  taxation/06 by id (HN-TAX-FR-237..FR-243: credit composition, grant/deny
  gates, ISR-cost bar, 4-month window, mixed pro-rata) with the
  base+ISV-total semantics stated by the sheet; the DMC stores the
  classification result, never the classifier itself. (LB-005; LB-009;
  EV13:EVID-090; EV43:EVID-145; LB-014 corroboration EV43:EVID-148)
- **HN-FREP-FR-105:** The system shall implement the OC line contract as
  the FA contract MINUS the CAI: mandatory fields drop 7-CAI and replace
  the 4-segment document number with 71-*N.º de documento* ("el número del
  documento equivalente"); all optional fields (OCE, exento, resolución,
  exonerado, bases, 270/280/290) are identical to FA. (LB-009;
  EV43:EVID-145)

### 3.5 Sheets 527-53 (FYDUCA) and 527-54 (importaciones)

- **HN-FREP-FR-106:** The system shall implement the FYDUCA line contract
  (sheet 527-53) for Central-American foreign suppliers: mandatory
  301-*Pasaporte o identificación CA* + 501-*Apellidos y nombre/razón
  social* + 901/101 dual dates + 190-*N.º FYDUCA*; optional 201-RTN, 302
  *N.º identificador tributario mercantil*, OCE/exento and
  resolución/exonerado pairs (111/141, 121/131), bases 1512/1612, and
  271/281/291 classification — the supplier-ID variety (passport/CA-ID
  primary, RTN optional) mirrors the cross-border document reality and
  shall not be forced into the 14-char RTN validation of 527-52.
  (LB-010; EV43:EVID-146)
- **HN-FREP-FR-107:** The system shall implement the import line contract
  (sheet 527-54) keyed on 20-*N.º DUA* (Declaración Única Aduanera) with
  mandatory 202-RTN + 902/102 dual dates, and the CA/fuera-CA base split —
  1513/1520 (15%) and 1613/1620 (18%) — because the same rate differs in
  credit treatment by origin on the 201 side; 272/282/292 classification
  as elsewhere. The optional items 5-8 of the sheet are NOT described in
  the Ayuda print (numbering jumps 4 → 9) and are carried as OQ-007 —
  never guessed into the export. (LB-010; EV43:EVID-146)
- **HN-FREP-FR-108:** The system shall map the DMC base casillas to their
  201 Sección B consumers BY ID via `fiscal-reporting/05` (F5,
  HN-FREP-FR-164..170): import
  CA/fuera-CA split feeds the 201's "Importaciones ... (Fuera Región
  Centroamérica)" lines and the origin classes feed 131/132/133 — the
  mapping table lives with the consumer, the DMC guarantees only the
  origin-split integrity (a line's origin class and CA/fuera-CA flag shall
  be consistent with its sheet and its FYDUCA/DUA key). (LB-010; LB-012;
  EV43:EVID-146/150)

### 3.6 Credit-validation interface (SAR cross-check)

- **HN-FREP-FR-109:** The system shall implement the presentation-time
  separation as a data invariant: every line resolves to either
  crédito-fiscal-bound amounts (bases 1511/1512/1513/1520/1611/1612/1613/
  1620 whose credit WILL be claimed) or costos/gastos/no-deducible amounts
  (270-family/280-family/290-family), mirroring SAR-237-2024 numeral 2.I
  and DEI-SG-276-2015 numeral 2 — the split is mandatory at presentation
  and a line cannot be left unclassified. (LB-002; LB-005; LB-009;
  EV13:EVID-082/090; EV43:EVID-145)
- **HN-FREP-FR-110:** The system shall expose a validation DELTA surface:
  the DMC exists to give SAR "una validación automática del crédito
  fiscal, costos y gastos" against the determinativa, so the system shall
  report per period the DMC-declared credit-eligible bases (by origin
  class and rate) versus the 201 Sección B values actually auto-fed via
  131/132/133, flagging any divergence introduced by rectification or
  manual entry — read-only reconciliation report, no recomputation of
  SAR-side results. (LB-002; LB-012; EV13:EVID-082; EV43:EVID-150)

### 3.7 Compras eventuales interface (DEI-279-2015)

- **HN-FREP-FR-111:** The system shall implement the registration duty of
  *adquisiciones eventuales* (occasional purchases documented by the
  buyer-issued code-10 voucher) in the DMC per 279-QUINTO, with the DMC
  deadline cited from SAR-237-2024 (5 días, FR-091) and NOT from the
  2016 "10 días" text embedded in DEI-279-2015 (superseded for DMC
  timing); because the 527 sheets offer only FA/OC at casilla 600 and
  never mention eventuales, the line class for such purchases (FA, OC, or
  exclusion) is UNRESOLVED (45_ OQ-3) and shall ship as a configuration
  flag with no default forced. (LB-006; LB-009; LB-010; EV13:EVID-087;
  EV43:EVID-145/146; OQ-005/OQ-006)
- **HN-FREP-FR-112:** The system shall model the buyer-ISV retention on
  compras eventuales as a SEPARATE engine from the DMC export: the
  acquiring contributor "está obligado a retener y enterar al Fisco el
  Impuesto Sobre Venta que cause las Compras de Bienes y/o Servicios",
  but the rate/base mechanics are stated by NO corpus text (18_ OQ-6 —
  LEAD) and the 527 sheets carry no ISV or retention field (negative
  finding) — the retention rule shall ship activation-blocked as a
  configuration gap and the system shall NEVER guess a rate or base into
  it. (LB-006; LB-010; EV13:EVID-087; EV43:EVID-146; OQ-003)
- **HN-FREP-FR-113:** The system shall consume the code-10 collision guard
  BY ID from `../e-invoicing/01_document-types-numbering.md`
  (HN-EINV-FR-009, R-H38): code 10 in the 16-digit grammar maps to
  exactly ONE assignment, and the DMC line-classification logic shall
  never assume a type-10 document segment means *Comprobante de Compras
  Eventuales* — the resolving lead is any post-2017 SAR instrument, and
  until it lands the eventual-10 claim stays collision-open and
  non-emittable. (LB-009; EV43:EVID-145; R-H38; crossref EV13:EVID-086)

### 3.8 History, sanctions & go-live (D-H3)

- **HN-FREP-FR-114:** At go-live, the system shall reconcile imported
  legacy purchase records against the previous system's FILED DMC
  declarations per RTN-period, using the reconciliation engine of
  `fiscal-reporting/01` (F1) consumed by id: legacy filings are frozen
  externs (D-H2.5 — never edited, only superseded by a proper
  rectificativa in the legacy channel of record), historical periods
  resolve their deadline rows per FR-091's chain (e.g. a Sep-2016..Apr-2024
  period was due day-20), and unexplained deltas surface on the FR-110
  report rather than being silently absorbed. (LB-003; LB-005; LB-011;
  EV13:EVID-083/090; EV43:EVID-147)
- **HN-FREP-FR-115:** The system shall surface the extemporáneo regime on
  late DMC filing — the declaration "indicará la multa y los intereses
  correspondientes" — by consuming the CT sanction/interest engines from
  taxation/01 by id and generating the *Boletín de Pago* artifact for the
  sanction payment; sanctions never exempt the filing obligation ("sin
  eximirlo de la obligación de presentar la misma"). (LB-005; LB-011;
  EV13:EVID-090; EV43:EVID-147)

## 4. Data Model

No machine-readable sidecar is created by this file (single-file scope);
the casilla map below is the authoritative inline catalog and may be
extracted to a CSV at wave assembly. Layer semantics: Odoo-side
bookkeeping/export data only (see §5).

**DMC filing header:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.dmc.filing (new) | period (month), company/RTN, channel, plantilla_version, state, original_id | char/date/select/m2o | channel: ovi · sw (sticky per FR-094); state: draft · en_proceso · con_errores · sin_errores · presentada · rectificada (two-stage, FR-095); ONE per RTN-period (FR-096); rectification locks to original channel (FR-097) | FR-094..FR-098 |
| l10n_hn.dmc.deadline.row (fiscal-calendar family, file 01) | valid_from, valid_to, day_count, day_kind, instrument | date/int/select/char | 10d-calendario (DEI-276) · 20d (CPAT-073, default calendario — OQ-002) · 5d-calendario (SAR-237-2024, from 2024-05-20) · NEVER an 8d row (R-H18) | FR-091, FR-092 |
| res.company | dmc_obligado_segment, is_state_institution, exempt_operator_flag | select/boolean | grande · mediano · regimen_especial · exentas (FR-087); state-institution dated from 2019-10-05 (FR-088); snapshot-on-write (D15) | FR-087..FR-090 |

**DMC line (shared spine + per-sheet casillas):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.dmc.line (new) | origin_class, sheet | select | local (527-52) · fyduca (527-53) · import (527-54) | FR-089 |
| l10n_hn.dmc.line | doc_class (casilla 600) | select | fa · oc — local sheet only; eventuales class = config flag, no default (OQ-006) | FR-099, FR-111 |
| l10n_hn.dmc.line | supplier_rtn (200/201/202), supplier_name (501), supplier_ca_id (301), mercantil_id (302) | char | RTN = 14 chars no guiones (local FA mandatory); FYDUCA = passport/CA-ID primary, RTN optional; import = RTN mandatory | FR-100, FR-106, FR-107 |
| l10n_hn.dmc.line | cai (7), doc_number (8 / 71 / 190 / 20) | char | CAI ≤37 guion-separated; FA number 4-segment pleca-separated validated against e-invoicing/01 grammar by id; OC = documento equivalente; FYDUCA key = 190; import key = DUA number | FR-100, FR-105..FR-107 |
| l10n_hn.dmc.line | fecha_emision (900/901/902), fecha_contable (100/101/102) | date | dual dates; contable = credit-window anchor feed (taxation/06 FR-242 by id); month-assignment date = OQ-008 | FR-101 |
| l10n_hn.dmc.line | importe_exento (110/111), no_oce (140/141), importe_exonerado (120/121), no_resolucion (130/131) | monetary/char | exonerado pairs with SEFIN resolución; OCE optional | FR-102 |
| l10n_hn.dmc.line | base_15, base_18, ca_origin | monetary/boolean | casillas 1511/1512 (15%) · 1611/1612 (18%) · 1513+1520 / 1613+1620 (import split by CA origin); NO isv_amount field exists (negative finding) | FR-103, FR-107 |
| l10n_hn.dmc.line | monto_costo (270/271/272), monto_gasto (280/281/282), valor_no_deducible (290/291/292) | monetary | base+ISV of non-credit comprobantes per Art.-12 pro-rata — classifier consumed from taxation/06 by id; mandatory classification (no NULL bucket) | FR-104, FR-109 |
| l10n_hn.dmc.line | eventual_flag | boolean | marks DEI-279-2015 adquisiciones eventuales registration duty (class unresolved — OQ-005/OQ-006); retention engine separate + blocked (OQ-003) | FR-111, FR-112 |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` = computation/export logic living in
the LGPL client; the SW plantilla generation and OVI fichas parity are
client-side artifacts. No SaaS rows: the DMC is an export/declaration
surface with no server-side determination (HN has no DTE transmission
regime — see e-invoicing wave). Model names stable across Odoo
17/18/19/20; version notes per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-086 | odoo | l10n_hn.dmc.filing | form_code=527, tipo=informativa | D12: regime rows DAC (annual, pre-2016) → DMC-527 monthly; no payment workflow on 527 (cf. 202 informative kin) |
| FR-087, FR-088, FR-090 | odoo | res.company segment flags + l10n_hn.fiscal.calendar hookup | obligado derivation | D15/D16: segment snapshot-on-write; State-institution row valid_from 2019-10-05 (2-month deferred vigencia); checklist surface per RTN-period |
| FR-091, FR-092 | odoo | l10n_hn.dmc.deadline.row (fiscal-calendar family owned by file 01) | dated rows | D12: chain 10d → 20d (2016-09) → 5d (2024-05-20) with instruments recorded; 8d NEVER loaded (R-H18); resolution key = month following purchase period; retro/legacy periods use their own rows (D16) |
| FR-093 | odoo | filing dependency edge (prerequisite gate) | 527-before-201/540 | Gate mechanics owned by file 05 (F5); this file exports the 131/132/133 feed; day-5 < day-10 makes the edge acyclic (R-H36) |
| FR-094..FR-097 | odoo | l10n_hn.dmc.filing + declaration-chassis consumed from file 01 (F1) | channel/state/original_id | Sticky modality; two-stage SW states incl. buzón second-validation check job; single consolidated filing blocks second originals structurally (unique RTN×period); rectification = new record superseding frozen snapshot (D-H2.5) |
| FR-098 | odoo | l10n_hn.plantilla.version (reference row on filing) | version pinning | Plantilla mutable by AT: new-version rows only; text-format serialization (RTN/montos/CAI/números), dates DD/MM/AAAA |
| FR-099..FR-105 | odoo | account.move.line (purchase) → l10n_hn.dmc.line mapper | 527-52 contract | FA/OC class from document model (l10n_latam.document.type consumed by id from e-invoicing/01); grammar validation delegated to HN-EINV-FR-012..022 by id — no local regex beyond the 37-char/pleca format checks printed in the Ayuda; bases from tax grids (15/18), no ISV column; 270/280/290 from the taxation/06 classifier output |
| FR-106..FR-108 | odoo | l10n_hn.dmc.line (fyduca/import) + account move import docs | 527-53/54 contract | Supplier-ID variety per sheet; DUA/FYDUCA keys; CA-origin split flag; consumer mapping (131/132/133, 201 import lines) owned by file 05 — feed-shape guarantee only |
| FR-109, FR-110 | odoo | l10n_hn.dmc.line classification constraint + reconciliation report (SQL/action) | invariant + delta | Mandatory classification (CHECK no unclassified presented lines); delta report DMC-bases vs 201-fed values, read-only |
| FR-111..FR-113 | odoo | l10n_hn.dmc.line eventual_flag + blocked retention rule stub | config-gapped | Eventuales class = flag, no default (45_ OQ-3); retention rule activation-blocked (18_ OQ-6 LEAD); code-10 guard consumed by id (HN-EINV-FR-009) — line classification never derives meaning from a type-10 segment |
| FR-114 | odoo | historical import job + FR-110 delta surface | D-H3 reconciliation | Engine consumed from file 01 (F1) by id; legacy filings = frozen externs; `is_historical` purchase lines map to DMC lines for continuity without re-filing |
| FR-115 | odoo | sanction surfacing on late filing + Boletín generation | CT hookup | Multa/intereses engines consumed from taxation/01 by id; Boletín artifact via the chassis (file 01) |

Version-regime notes (D12): FR-091 records the three-deadline chain with
per-instrument vigencia (incl. CPAT-073's Sep-2016 effectivity and
SAR-237-2024's 20-may-2024 publication date); FR-088 records the delayed
2-month vigencia of SAR-343-2019. No adaptation windows exist beyond
publication dates (immediate-on-publication for SAR-237-2024, deferred for
SAR-343-2019 — both encoded as dated rows, never as edits).

## 6. Acceptance Criteria

- **AC-001:** Given purchase period January 2016, then the DMC deadline row
  resolves to the first 10 días calendario of March 2016 (first filing per
  DEI-SG-276-2015); given period August 2017, then day-20 (CPAT-073 row,
  calendario default); given period June 2024, then 2024-07-05 (5 días
  calendario per SAR-237-2024) (FR-091).
- **AC-002:** Given any period ≥ 2024-05-20 and the Agosto-2026 Ayuda's
  "ocho (8) días" text, then the loaded deadline stays 5 días calendario —
  the 8d print is flagged, never encoded (FR-092; R-H18).
- **AC-003:** Given a State-institution company with purchases in August
  2019, then no DMC obligación is derived; given the same company in
  October 2019, then the obligación checklist includes the DMC (FR-087,
  FR-088).
- **AC-004:** Given an FA line whose supplier RTN is `0801-1990-123456` or
  13 characters, then export validation rejects it (14 chars, no guiones);
  given CAI `19AB25-ED1000-1D76E0-632D08-14ACAF-9D` (37 chars,
  guion-separated), then it passes (FR-100).
- **AC-005:** Given an FA line with document number `001/007/01/00000001`,
  then the 4-segment pleca format passes and the embedded grammar is
  validated by the e-invoicing/01 engine by id; given a pre-2018 historical
  document with a 14-digit number, then the dual parser (HN-EINV-FR-022)
  accepts it per its era rules (FR-100).
- **AC-006:** Given a purchase invoice issued 2026-05-28 and contabilized
  2026-06-02, then the DMC line carries both dates and the credit-window
  check consumes fecha contable (June cause month + 3) per taxation/06
  FR-242 by id (FR-101).
- **AC-007:** Given a local FA purchase of base L10,000 at 15% with exempt
  L500 backed by OCE 141-00123, then the line exports 1511=10,000.00,
  110=500.00, 140=00123 — and no ISV-amount field exists anywhere in the
  export (FR-102, FR-103).
- **AC-008:** Given a mixed-taxpayer purchase whose Art.-12 pro-rata yields
  60% gravada-linked credit, then the non-credit remainder (base+ISV) is
  exported to 270 (costo) or 280 (gasto) per its accounting destination and
  any no-deducible fraction to 290; the classifier itself is consumed from
  taxation/06 by id, not recomputed (FR-104).
- **AC-009:** Given a FYDUCA purchase from a Guatemalan supplier identified
  by passport, then the 527-53 row carries 301/501/190 + bases 1512/1612
  and is NOT routed through the 14-char RTN validation (FR-106).
- **AC-010:** Given an import with base 15% L50,000 originated outside
  Centroamérica, then the 527-54 row fills casilla 1520 (not 1513) and the
  line's ca_origin flag is consistent with its DUA key; the 201-side
  consumer mapping is resolved by file 05 by id (FR-107, FR-108).
- **AC-011:** Given a company with three sucursales filing period
  2026-06, then exactly one consolidated DMC 527 exists for the RTN-period
  and a second original is refused structurally (FR-096).
- **AC-012:** Given a DMC originally presented via Servicio Web, then the
  rectificativa is offered only via Servicio Web and is stored as a new
  record superseding the frozen original (same-modality lock) (FR-097).
- **AC-013:** Given an SW upload whose orden de trabajo returns errors,
  then the error-report PDF is downloadable, the declaration state stays
  con_errores, and presentation is impossible until a clean orden passes
  BOTH validations (the buzón second-stage check included) (FR-095).
- **AC-014:** Given an eventual-purchase line flagged per DEI-279-2015,
  then the registration duty surfaces on the DMC checklist but the
  buyer-ISV retention rule remains activation-blocked with an explicit
  config-gap marker — no rate or base value exists in the system for it
  (FR-111, FR-112).
- **AC-015:** Given go-live import of 2023 legacy purchases, then the
  reconciliation report compares them against the previous system's filed
  2023 DMC declarations (deadline row: day-20 era), flags deltas, and
  treats the legacy filings as frozen externs (FR-114).
- **AC-016:** Given a DMC presented after the day-5 deadline, then the
  filing surface shows the computed multa + intereses (CT engines by id)
  and generates the Boletín de Pago, while the filing obligation remains
  open (FR-115).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `15_ OQ-3` carried: DEI-SG-276-2015 gazette number — OCR header reads 33,955 (9-feb-2016) vs SAR catalog 33,995; gazette arithmetic favors 33,955. Pin only via the ENAG original; citation strings keep the catalog value flagged suspect. | no | acquisition queue (ENAG) | open |
| OQ-002 | `16_ OQ-5` carried: CPAT-073-2016's replacement text says "veinte (20) días" WITHOUT "calendario" (base text said días calendarios). Moot for current law (5 días calendario explicit), but the 2016-09→2024-05 dated-row reconstruction needs the ruling — DEFAULT calendario (context: decongestion of a calendario day-10 cluster); flag if ever material (retro omisas). | no | Takumi S-HN3 | open (default calendario) |
| OQ-003 | `18_ OQ-6` carried (LEAD, kin `45_ OQ-2`): compras-eventuales buyer-ISV retention rate/base unstated by DEI-279-2015 QUINTO and unresolved by 45_/72_ (no ISV/retention field in any 527 sheet). FR-112 ships the rule activation-blocked; BLOCKING for the retention engine only, never for the DMC export. Lead: SAR procedural guidance / facturación-reglamento doc-type catalog. | yes (retention engine only) | acquisition queue | open |
| OQ-004 | `45_ OQ-1` residual (also `72_ OQ-1`): 8-vs-5 días RULED — 5 días calendario per R-H18 (gazette text is the record; FR-092 encodes the guard). Record-only residual: acquire any post-May-2024 acuerdo setting 8 días (both manuals hedge "modificaciones posteriores"); if found, append a dated row — never edit SAR-237-2024's. | no | acquisition queue | ruled (R-H18) / lead open |
| OQ-005 | `45_ OQ-2` carried (LEAD): compras eventuales are ABSENT from the DMC helps — casilla 600 offers FA/OC only; the Ayuda's silence on how eventuales are registered is itself the finding. Lead: SAR guidance on eventual purchases in the DMC; kin of OQ-003. | no | acquisition queue | open |
| OQ-006 | `45_ OQ-3` carried: OC class scope is open-ended ("...y otros documentos autorizados por el SAR") and whether an eventual-purchases document enters the DMC as FA, OC, or not at all is undefined. FR-111 ships a config flag with no default; verify vs live plantilla/SAR guidance. | no | Takumi S-HN3 | open |
| OQ-007 | File-local: 527-54 optional items 5-8 are not described in the Ayuda print (numbering jumps from mandatory 4 to optional 9); by 527-53 analogy they are presumably the OCE/exento/resolución/exonerado pair — UNVERIFIED. Never export guessed casilla numbers; verify against the live SW plantilla (ties to FR-098 version pinning). | no | Takumi S-HN3 | open |
| OQ-008 | File-local: which date assigns a purchase line to the declaration month — the deadline texts run from "el mes ... en que se efectuaron las compras", the sheets carry fecha emisión AND fecha contable, and the credit window keys to causación. Default: fecha contable (bookkeeping month, consistent with the window anchor of FR-101/taxation/06 FR-242); verify vs SAR validator behavior before freezing. | no | Takumi S-HN3 | open |
| OQ-009 | File-local: plantilla version management — the AT may modify structure/fields at any time; FR-098 pins a version per export. Which versions exist historically, and whether OVI fichas and SW plantilla ever diverge in field sets, is unverifiable from the corpus (single Agosto-2026 print); re-verify at implementation against the live portal. | no | Takumi S-HN3 | open |

Register mapping (master index C2 slice): `15_ OQ-3` → OQ-001;
`16_ OQ-5` → OQ-002; `18_ OQ-6` → OQ-003; `45_ OQ-1` (+`72_ OQ-1`)
→ OQ-004; `45_ OQ-2` → OQ-005; `45_ OQ-3` → OQ-006. Resolved-of-record
and encoded as guards, not OQs: `20_ OQ-7` (R-H19 — the `20_` filename's
"retenciones" gloss was a mislabel; content modifies the DMC procedure;
correction of record in EV13), `72_ OQ-2`/`72_ OQ-3` (R-H27 — dual
channel stands; 72_ §4/§5 stale cluster, FR-094 note), `70_ OQ-2`
(131/132/133 provenance — consumer-side, owned by fiscal-reporting/05,
crossref only). Rulings consumed: R-H17 (deadline chain), R-H18 (stale
manuals), R-H19 (mislabel note), R-H25 (form 527), R-H27 (dual channel),
R-H36 (DMC-first), R-H38 (code-10 collision).
