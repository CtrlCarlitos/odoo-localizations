# GT — Fiscal reporting — Criterios Tributarios Institucionales 2-2019 (dualidad) + 6-2018 (deducibilidad): the interpretive layer

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F6 — the two SAT
*Criterios Tributarios Institucionales* (institutional tax criteria, SAT's
administrative interpretive instruments) as an **INTERPRETIVE layer ONLY**:
**Criterio 2-2019** (`64_`, "El tratamiento a otorgar cuando existe dualidad
en la calidad de los agentes de retención del IVA" — dual quality of IVA
retention agents, applies from 1-Jun-2019) and **Criterio 6-2018** (`65_`,
"Costos y gastos deducibles del ISR de los pagos … en concepto de sueldos y
salarios, aguinaldo, bono 14 y dietas" — ISR deductibility of payroll
payments, from 23-Apr-2018). The core F6 rule (binding): the criterios
**CONFIRM, never re-derive**, every statutory value — the retention-rate
matrix and dualidad model are owned by S-GT2 taxation/03 (consumed by exact
FR id + CSV row), the deduction caps and gates by taxation/05 (GT-TAX-FR-167
..169) with taxation/04 deduction-gating kin, and the operational surfaces
the criterios interpret are T2's RetWeb file (`02_retenciones-web.md`,
GT-FIN-FR-027..074, cited by id). This file carries: the instrument identity/
date rows (D16/D-GT10); the confirm-only validation contract (saas CI-gate
kin, catalogs-governance pattern); the dualidad holdings surfaced as
annotations consuming taxation/03's resolved GOQ-118/119 model (never a
second model); the retained-IVA bookkeeping interpretive notes (nil-month
duty, registro auxiliar, ledger captions, neutrality, solidarity —
confirming taxation/03); the 6-2018 deducibilidad interpretive surface
(IGSS-planilla gate, 10% related-party cap, 100% bonus caps + pacto
colectivo, dietas gate — confirming taxation/05 + feeding payroll's
planilla flag); the GOQ-121 negative-FR (no decree-number backfill of the
GOQ-09 bonus instruments); and the OCR guards (GOQ-116 clause-level citation
ban; R50 "20-2008" [sic] transcribed, never propagated; R51/GOQ-120 multa
divergence recorded unresolved — kin-cited, never re-opened).

It does **not** cover: any statutory rate, threshold, deadline or cap (all
S-GT2 taxation files + CSV sidecars — every value here cites its taxation FR
id); the RetWeb operational system itself (T2); sanction amounts or
procedures (taxation/06 owns CT sanctions incl. the GOQ-120 divergence);
payroll computation (S-GT3 files); the bonus laws' own mechanics (bono 14 =
D-42-92 in `40_`; the December aguinaldo statutes remain absent, GOQ-09);
and the normative-weight formula ("obligatorio para la SAT"), which neither
criterio prints (GOQ-117).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): **criterios institucionales are SAT administrative interpretive
instruments, NOT law** — every statute they interpret outranks them, and
this file consumes each statutory value from its S-GT2 owner by exact FR
id. The criterios' own consolidated tables and summaries are quoted ONLY as
confirmation evidence; deadline rows are NEVER sourced from a criterio's
own summary (the three 64_ formulations defer to W-GT2 statutory evidence).
64_/65_ are OCR scans — blank pages and print defects are load-bearing
(GOQ-116 pages 4/5/8; R50 "20-2008" [sic]; ponente garble [sic]) and are
transcribed verbatim, never corrected. All quotes below verified verbatim
against `gt/.extractions/64-65_Criterios.evidence.md` (EVID-491..500).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Criterio 2-2019 identity + weight + dates: "CRITERIO TRIBUTARIO INSTITUCIONAL No. 2-2019" / "EL TRATAMIENTO A OTORGAR CUANDO EXISTE DUALIDAD EN LA CALIDAD DE LOS AGENTES DE RETENCIÓN DEL IMPUESTO AL VALOR AGREGADO" / "Se aprueba el presente criterio institucional, el cual debe ser aplicado a partir del 1 de junio de 2019. Guatemala, 22 de abril de 2019. Publíquese y divúlguese." / "PONENTE: GERENCIA DE CONTRIBUYENTES ESPECIALES GRANDES [sic]" / signed "Lic. Abel Francisco Cruz Calderón, Superintendente de Administración Tributaria -SAT-" | Criterio 2-2019: SAT's interpretation of dualidad (one taxpayer holding more than one D-20-2006 retention-agent quality, each with its own %); approved 22-Apr-2019, mandatory application from 1-Jun-2019; in-text weight = approval/application clauses + publication only (the "obligatorio para la SAT" formula is NOT printed — GOQ-117); ponente word-order garble retained as printed | `gt/sources/64_SAT_Criterio_2-2019.pdf` | p.1 title + PLANTEAMIENTO; p.14 approval/signature (EVID-491) |
| LB-002 | 64_ base-legal frame: CT art. 28: "Agentes de retención, son sujetos que al pagar o acreditar a los contribuyentes cantidades gravadas, están obligados legalmente a retener de las mismas, una parte de éstas como pago a cuenta de tributos a cargo de dichos contribuyentes." / CT art. 94 num. 7: "No percibir o retener los tributos, de acuerdo con las normas establecidas en este Código y en las leyes especificas de cada impuesto." / "SANCIÓN: Multa equivalente al impuesto cuya percepción o retención omitiere. La imposición de la multa no exime la obligación de enterar el impuesto percibido o retenido…" / analysis (p.12): "si solo realiza la retención por una de las calidades de agente de retención que posee, y deja de hacerlo por la otra calidad, tendrá la sanción respectiva" / CPR art. 239 nullity clause | The legality frame: rates are statutory (CT agent definition + CPR 239 nullity of contradicting lower rules); omitting to retain under ONE of two held qualities is already the CT 94-7 infraction with multa = omitted tax + duty to enter — interpretive support only; the CT art. 91 (65_) vs CT art. 94 num. 7 (64_) divergence on the same infraction is RECORDED UNRESOLVED by S-GT2 in taxation/06 (both texts verbatim there, LB-026 of that file; R51/GOQ-120) — kin-cited, never re-opened, never a winner picked here | `gt/sources/64_SAT_Criterio_2-2019.pdf` | pp.1-3 BASELEGAL [sic] block; p.12 analysis (EVID-492) |
| LB-003 | D-20-2006 art. 1 as quoted in 64_: exportadores habituales "cuya exportación mensual en promedio sea de cien mil quetzales (Q. 100,000.00) como mínimo, serán considerados agentes de retención… le dará aviso de su activación" / (agro) "pagarán al vendedor o al prestador del servicio, el treinta y cinco por ciento (35%) del impuesto al Valor Agregado (IVA) y le retendrán el sesenta y cinco por ciento (65%) de dicho impuesto… incluido en el monto total de cada factura" (products: "el café en cualquier forma, excepto tostado o soluble, azúcar de caña sin refinar, banano, cardamomo en cualquier estado, caña de azúcar, algodón, leche y otros productos agropecuarios") / (rest) "el ochenta y cinco por ciento (85%) del Impuesto al Valor Agregado (IVA) y le retendrán el quince por ciento (15%)" / (D-29-89) "le retendrán el sesenta y cinco por ciento (65%)" | Statutory text reproduced inside the criterio (not its own voice): exportador habitual = registered + monthly average exports ≥ Q100,000 + SAT activation aviso; 65% agro list / 15% everything else / 65% D-29-89 — **agrees with the S-GT2 resolved matrix (GT-TAX-FR-071/072)**; recorded as confirmation only, rates are NOT re-derived from the criterio | `gt/sources/64_SAT_Criterio_2-2019.pdf` | p.3, D-20-2006 art. 1 first base-legal article (EVID-493) |
| LB-004 | The criterio's own consolidated table (introduced "El Decreto número 20-2008 [sic]" — R50): "Exportador habitual 65% En la adquisición de productos agricolas [sic] y pecuarios…" / "Exportador habitual 15%… no detallados en el párrafo anterior." / "Exportadores calificados en el Decreto número 29-89 65%…" / "Sector público 25% En las compras de bienes y adquisición de servicios superiores a Q30,000.00." / "Emisores de tarjeta de crédito 15%… según la cantidad expresada en el voucher de compra" / "Emisores de tarjeta de crédito 1.5% En la adquisición de combustibles pagado con tarjeta de crédito o débito…" / "Contribuyentes especiales 15%…" / "Otros agentes de retención 15%…" / AG 5-2013 art. 49: "los agentes de retención… practicarán las retenciones a pequeños contribuyentes, únicamente cuando paguen bienes y servicios cuyo valor sea mayor a dos mil quinientos Quetzales" | The 2-2019 summary table CONFIRMS the S-GT2 matrix: 65/15/65/25 > Q30,000 / 15 tarjetahabientes / 1.5 card-fuel / 15 especiales / 15 otros + the Q2,500 pequeño abstention (AG 5-2013 art. 49) — all keyed to GT-TAX-FR-072/074/075/076/077/078/079/086/080 + `iva_retention_rates.csv`; the "20-2008" [sic] print defect is transcribed, never propagated (R50) | `gt/sources/64_SAT_Criterio_2-2019.pdf` | pp.10-11 analysis table; p.7 AG 5-2013 art. 49 (EVID-494) |
| LB-005 | 64_ obligations/accounting/solidarity quotes: "…mensualmente aún y cuando no hubiere efectuado retención alguna durante el mes que declara. 3. Llevar en la contabilidad un registro auxiliar con el detalle completo de las retenciones efectuadas. (...)" / "El agente de retención es solidariamente responsable con el contribuyente obligado, si el primero de los nombrados no efectuó la retención establecida en la ley." / "El impuesto retenido no constituirá débito, ni crédito fiscal para el agente de retención, ni podrá ser compensado con tributos, salvo lo dispuesto en el artículo 1 de la presente ley." / D-20-2006 art. 14: "Los agentes de retención que no enteren a la Administración Tributaria el impuesto retenido, estarán sujetos a las sanciones reguladas en el Código Tributario y el Código Penal, según lo que corresponda." / AG 5-2013 art. 43: "…la cuenta se llamará \"IVA - Retenciones por Pagar\" y para los proveedores se llamará \"IVA - Retenciones por compensar\"." / LIVA art. 48: "dentro del plazo de quince días del mes inmediato siguiente a aquel en que se efectuó el pago o acreditamiento" / analysis list: "dentro de los 15 días hábiles siguientes a aquel en que se realice la retención. La declaración debe presentarse aun cuando no tenga movimiento." | Agent-side mechanics as interpreted: nil-month declaration duty; registro auxiliar; the two named ledger accounts; retained IVA never débito/crédito for the agent (sole art. 1 exporter carve-out); solidarity; non-entering sanctioned per CT AND Código Penal (art. 14). THREE coexisting deadline formulations (OQ-4 of the evidence file): deadline CRs are NEVER sourced from here — they defer to W-GT2 statutory evidence (GT-TAX-FR-105/106, R26 single window). The D-20-2006 obligations article quote resumes mid-sentence on p.6 — its article number is LOST (blank pp.4/5/8, GOQ-116): clause-level citations from 64_ are banned (cite 78_/79_ via taxation/03) | `gt/sources/64_SAT_Criterio_2-2019.pdf` | p.6 (unnumbered article, OQ-1; art. 14; LIVA 48), pp.6-7 (AG 5-2013 art. 43), p.10 obligations list (EVID-495) |
| LB-006 | THE HOLDING — Criterios Propuestos 1-3 + operational rule: AG 5-2013 art. 45: "Cuando los contribuyentes estén comprendidos en más de uno de los grupos establecidos en la Ley para ser Agentes de Retención, deben hacer las retenciones por cada una de las actividades en las que la SAT lo haya activado como Agente de Retención y en los porcentajes que indica la Ley." / analysis: "el Acuerdo Gubernativo número 425-2006…, en el artículo 9… haciendo la aclaración que cuando los contribuyentes estén comprendidos en más de uno de los grupos… deben hacer las retenciones por cada una de las actividades…" / AG 425-2006 art. 4: "los Agentes de Retención deben ingresar el monto total de cada factura, al Sistema de Retenciones de SAT, el cual determinará el porcentaje de retención a realizar por cada factura, según está definido en la ley para cada tipo de compra y Agente de Retención. El monto de la factura incluirá el Impuesto al Valor Agregado." / "…tomando en consideración los casos en que existe diferentes tipos de productos en la misma factura, se podrá realizar el prorrateo correspondiente." / Criterio 1: "Cuando un contribuyente se encuentre calificado, con fundamento en el artículo 6 del Decreto número 1-98…, como contribuyente especial… deberá retener el 15%… Si el contribuyente especial, además, es exportador habitual, debe retener el 65%…" / Criterio 2 (otro agente per "artículo 6 del Decreto número 20-2006"): same 65-agro/15-rest structure / Criterio 3: "Cuando el contribuyente es operadora de tarjetas de crédito o de débito y a la vez esté calificado como contribuyente especial…, debe realizar la retención del 15%… a los establecimientos afiliados por ser operadora de tarjeta… y además… el 15%… como contribuyente especial en las compras o adquisiciones… a sus proveedores." | The dualidad holding: a dual-quality agent retains under EACH quality separately at each quality's statutory per-activity rate; the operative % per factura is determined by SAT's Sistema de Retenciones (AG 425-2006 art. 4; invoice amount includes IVA) with prorrateo for mixed-product invoices; grounds differ — LOSAT D-1-98 art. 6 (especial) vs D-20-2006 art. 6 (otro). AG 425-2006 "artículo 9" citation VERIFIED CORRECT in-corpus by S-GT2 (R52/GOQ-118 RESOLVED: art. 4 = Sistema procedure, art. 9 = dualidad rule — taxation/03 LB-017/FR-084); the GOQ-119 modeling call (config-driven dualidad + saas Sistema-% resolution + prorrateo) is taxation/03 FR-084/085 — consumed here, never a second model | `gt/sources/64_SAT_Criterio_2-2019.pdf` | pp.11-12 analysis (AG 425-2006 arts. 4/"9", AG 5-2013 art. 45, prorrateo); pp.12-13 V. CRITERIOS PROPUESTOS 1-3 (EVID-496) |
| LB-007 | Criterio 6-2018 identity + weight + base-legal map: "CRITERIO TRIBUTARIO INSTITUCIONAL No. * 6-2018 [sic]" / "COSTOS Y GASTOS DEDUCIBLES DEL IMPUESTO SOBRE LA RENTA DE LOS PAGOS QUE REALIZAN LOS CONTRIBUYENTES EN CONCEPTO DE SUELDOS Y SALARIOS, AGUINALDO, BONO 14 y DIETAS" / the three consultations: "I. La deducibilidad de los pagos por concepto de los sueldos y salarios cuando el patrono no está obligado a inscribirse en el Régimen de Seguridad Social. II. La deducibilidad… aguinaldo y bonificación anual… (bono 14)… III. La deducibilidad de los pagos por concepto de dietas a un pequeño contribuyente." / "Lo anterior, sin perjuicio de la formulación de ajustes e imposición de multas que procedan, derivado de las facultades que la Superintendencia de Administración Tributaria tiene para fiscalizar…" / "PONENTE: INTENDENCIA DE ASUNTOS JURÍDICOS. Se aprueba el presente criterio institucional, el cual deberá ser aplicado a partir de la presenta fecha. [sic — presente] Guatemala, 23 de abril de 2018." | Criterio 6-2018: SAT's interpretation of ISR deducibilidad of payroll payments under the LAT (D-10-2012, Régimen de Actividades Lucrativas); approved and applicable from 23-Apr-2018 itself; fiscalización/ajustes/multas powers EXPRESSLY RESERVED (interpretation does not limit audit). Base legal as printed: LOJ arts. 10-11; CT arts. 4 y 91; Código de Trabajo arts. 2, 3, 49, 88 y 102; LAT arts. 4, 10 (num. 8), 19, 21 (nums. 4-5), 22 (lit. f), 23 (lit. f), 44, 104; Timbres D-37-92 arts. 4 y 11; AG 213-2013 art. 9; IGSS Acuerdo 1123 arts. 2, 3 y 15; AG 86-2003 art. 1 | `gt/sources/65_SAT_Criterio_6-2018.pdf` | p.1 title/consultations; p.2 BASE LEGAL; p.8 approval (EVID-497) |
| LB-008 | Holding 1 — sueldos gate: Acuerdo 1123 art. 2: "todo patrono persona individual o jurídica, que ocupe tres o más trabajadores, está obligado a inscribirse en el Régimen de Seguridad Social… los patronos que se dediquen a la actividad económica del transporte terrestre de carga, de pasajeros o mixto…, están obligados a inscribirse cuando ocupen los servicios de uno (1) o más trabajadores." / art. 15: gerentes, directores, administradores "se consideran trabajadores afiliados y deben aparecer reportados como tales en las Planillas de Seguridad Social." / CT art. 102: "todo patrono que ocupe permanentemente a diez o más trabajadores, debe llevar un libro de salarios autorizado y sellado…; todo patrono que ocupe permanentemente a tres o más trabajadores, sin llegar al límite de diez, debe llevar planillas…" / LAT art. 23 lit. f: no deduction "cuando no acrediten ante la Administración Tributaria, con la copia de la planilla de las contribuciones a la seguridad social presentadas al Instituto Guatemalteco de Seguridad Social, los pagos realizados por concepto de sueldos, salarios o prestaciones laborales, cuando proceda." / "la deducción máxima por sueldos pagados a los socios o consejeros de sociedades civiles y mercantiles, cónyuges, así como a sus parientes dentro de los grados de ley, se limita a un monto total anual del diez por ciento (10%) sobre la renta bruta." / Criterion 1: "Los patronos que no estén obligados a inscribirse en el Régimen de Seguridad Social… podrán deducir del Impuesto Sobre la Renta los sueldos o salarios que paguen a sus trabajadores, si cumplen con los documentos y medios de respaldo que acrediten el pago, como lo son los libros de salarios o planillas." | Sueldos/salaries (LAT 21-4) deductible iff the art. 21/22 requirements hold AND — when the patrono is IGSS-obliged (≥3 workers; transporte terrestre ≥1) — the workers figure in the IGSS planilla (LAT 23 lit. f gate; directors/managers = trabajadores afiliados per art. 15); non-obliged patronos deduct with libros de salarios/planillas as backing; related-party sueldos (socios/consejeros/cónyuges/parientes) capped at 10% of renta bruta, total annual — CONFIRMS GT-TAX-FR-167/168/169 (taxation/05) by exact id; feeds the IGSS-planilla flag (payroll/07 GT-PAY-FR-170) and book modes (GT-PAY-FR-017/018) | `gt/sources/65_SAT_Criterio_6-2018.pdf` | pp.2-5 framework + CT 102/Acuerdo 1123; institutional criterion 1 p.7 (EVID-498) |
| LB-009 | Holding 2 — bonus caps: LAT art. 21 num. 5: deducibles "tanto el aguinaldo como la bonificación anual (bono 14) para los trabajadores del sector privado y público hasta el 100% del salario mensual, salvo lo establecido en los pactos colectivos de condiciones de trabajo debidamente homologados por el Ministerio de Trabajo y Previsión Social." / aguinaldo law (paraphrased-quoted): "todo patrono queda obligado a otorgar a sus trabajadores anualmente en concepto de aguinaldo, el equivalente al cien por ciento del sueldo o salario ordinario mensual…" / bono 14 law art. 2: "la bonificación anual será equivalente al cien por ciento (100%) del salario o sueldo ordinario devengado por el trabajador en un mes…" / excess rule: "si el patrono paga… sobre un porcentaje mayor al salario mensual, el excedente no podrá considerarse deducible… No obstante…, podrá considerarse deducible el excedente, si el contribuyente cuenta con un pacto colectivo de condiciones de trabajo, debidamente autorizado conforme el Código de Trabajo y homologado por el Ministerio de Trabajo y Previsión Social…" / respaldo: "deben estar respaldados mediante las planillas o libros de salarios o los recibos que el patrono entregue al empleado." | Both December prestaciones deductible only up to 100% of one monthly salary; any excess is NOT deductible unless mandated by a pacto colectivo validly concluded and homologado por MinTrabajo; backing = planillas/libros de salarios/recibos — CONFIRMS GT-TAX-FR-167 (100% rows) and GT-TAX-FR-169 (pacto excess rule). GOQ-121 (binding): the criterio cites BOTH laws by title only, NEVER by decree number — it cannot backfill the GOQ-09 instruments (December aguinaldo D-76-78 absent; bono 14 registry number D-42-92) and its paraphrase is interpretive support only, never a decree-number source | `gt/sources/65_SAT_Criterio_6-2018.pdf` | pp.5-6 laws + LAT 21-5 + excess rule; institutional criterion 2 p.7 (EVID-499) |
| LB-010 | Holding 3 — dietas gate: LAT art. 10 num. 8: "constituye hecho generador del Impuesto Sobre la Renta en la categoría de rentas provenientes de actividades lucrativas, la obtención de dietas" / "conforme el artículo 9 del Reglamento del Libro | [sic I] de la Ley de Actualización Tributaria, las personas que paguen dietas deben efectuar la retención del Impuesto Sobre la Renta, con carácter definitivo, aplicando los tipos impositivos establecidos en el artículo 44 de la Ley de Actualización Tributaria." / Criterion 3: "Se considerarán deducibles los gastos por concepto de dietas pagadas a un contribuyente inscrito en el Régimen del Pequeño Contribuyente, si la persona que paga o acredita la misma efectúa la retención del Impuesto Sobre la Renta, aplicando los tipos impositivos establecidos en el artículo 44… y comprueba el pago de las mismas con los recibos o comprobantes de pago, los cuales se encuentran afectos al pago del Impuesto de Timbres Fiscales y de Papel Sellado Especial para Protocolos." | Dietas paid to a pequeño contribuyente are deductible by the payer ONLY IF (i) the payer applies the ISR retention with carácter definitivo at LAT art. 44 rates (per AG 213-2013 art. 9) and (ii) payment is proven with timbre-affected recibos/comprobantes (D-37-92). The LAT art. 44 rate VALUES are not restated here — they defer to taxation/05 `isr_rates.csv` (never re-derived from this criterio) | `gt/sources/65_SAT_Criterio_6-2018.pdf` | pp.6-7 DRAE + LAT/AG 213-2013; institutional criterion 3 p.8 (EVID-500) |

## 3. Functional Requirements

### 3.1 Instruments, dates & normative weight (reference data)

- **GT-FIN-FR-165:** Criterio 2-2019 shall be recorded as a dated reference
  instrument (D16/D-GT10): approved **2019-04-22**, applicable **from
  1-Jun-2019** ("debe ser aplicado a partir del 1 de junio de 2019"),
  ponente "GERENCIA DE CONTRIBUYENTES ESPECIALES GRANDES" [sic — word-order
  garble retained as printed], with its in-text weight clauses (approval +
  application date + "Publíquese y divúlguese") stored as the ONLY weight
  assertions this file may make. It is an interpretive instrument, never a
  statute: no rate, threshold, deadline or obligation may cite it as
  statutory authority. (LB-001; EVID-491; GOQ-117 → OQ-002)
- **GT-FIN-FR-166:** Criterio 6-2018 shall be recorded as a dated reference
  instrument: approved and applicable **from 23-Apr-2018 itself** ("deberá
  ser aplicado a partir de la presenta fecha" [sic — presente]), ponente
  INTENDENCIA DE ASUNTOS JURÍDICOS, with the express reservation that it
  does NOT limit SAT's fiscalización/adjustment/multa powers ("sin
  perjuicio de la formulación de ajustes e imposición de multas que
  procedan") carried on the instrument row. Same interpretive-only status
  as FR-165. (LB-007; EVID-497)
- **GT-FIN-FR-167:** The base-legal maps of both criterios shall be stored
  as citation-routing reference data: 64_ rests on CPR 239, LOJ 10, CT
  4/28/94-7, D-20-2006 arts. 1/14 (+ an unnumbered obligations article —
  GOQ-116), LIVA D-27-92 arts. 23/48, AG 5-2013 arts. 43/45/49/51, AG
  425-2006 arts. 4 and 9, LOSAT D-1-98 art. 6 — with **NO citation of the
  LAT (D-10-2012) anywhere in 64_** (its IVA statute is D-27-92); 65_ rests
  on the LAT arts. 4/10-8/19/21-4,5/22-f/23-f/44/104 + CT + Código de
  Trabajo + Timbres D-37-92 + AG 213-2013 art. 9 + IGSS Acuerdo 1123 + AG
  86-2003. System citations for statutory content always route to the
  underlying instrument (via the taxation files' LB rows), never to the
  criterio. (LB-001, LB-007; EVID-491, EVID-497)
- **GT-FIN-FR-168:** Normative-weight guard (GOQ-117): neither criterio
  prints the "obligatorio para la SAT / no genera derechos subjetivos a
  favor de terceros" formula — no product surface, label or prose may
  assert that characterization from these files; any requirement needing
  the internal-binding weight must source it externally (SAT's criterios
  framework / LOSAT), recorded as an acquisition-flagged gap, never
  invented. (LB-001, LB-007; EVID-491, EVID-497; GOQ-117 → OQ-002)

### 3.2 The interpretive-layer contract (confirm-only)

- **GT-FIN-FR-169:** CONFIRM-ONLY GUARD (the core F6 rule): both criterios
  shall enter the product ONLY as interpretive reference data and
  confirmation cross-checks — a validation gate (saas CI-gate kin,
  catalogs-governance pattern) shall reject any configuration row, ledger
  seed or declaration surface whose ONLY statutory anchor is a criterio.
  Every statutory value interpreted by the criterios cites its S-GT2
  taxation owner by exact FR id: the retention matrix (GT-TAX-FR-070..082 +
  `iva_retention_rates.csv`), the dualidad model (GT-TAX-FR-084/085), the
  declaration chassis and deadlines (GT-TAX-FR-105/106), the deduction caps
  and gates (GT-TAX-FR-167/168/169 + `isr_rates.csv`), the deadline
  qualifier registry (GT-TAX-FR-142); the criterio's own tables are quoted
  only as confirmation evidence attached to those rows.
  (LB-001..LB-010; EVID-491..500)
- **GT-FIN-FR-170:** The 2-2019 consolidated rate table shall be recorded
  as ONE confirmation annotation keyed — value by value — to its taxation
  owners: 65 agro-exportador / 15 exportador-general / 65 D-29-89
  (GT-TAX-FR-072), 25 sector público > Q30,000 (GT-TAX-FR-074/075), 15
  tarjetahabientes (GT-TAX-FR-076), 1.5 card-fuel (GT-TAX-FR-077), 15
  especiales / 15 otros (GT-TAX-FR-078/079), plus the **Q2,500 pequeño
  abstention via AG 5-2013 art. 49** (GT-TAX-FR-080/086) — each mapping
  carrying its `iva_retention_rates.csv` row reference and the EVID id, and
  NO independent rate row of its own. The introducing sentence's print
  defect "El Decreto número 20-2008" [sic] is transcribed verbatim in the
  annotation (R50) and is governed by FR-185. (LB-003, LB-004; EVID-493,
  EVID-494; R50)

### 3.3 Dualidad holdings (consumption of taxation/03's resolved model)

- **GT-FIN-FR-171:** The dualidad holding (Criterios 1-3) shall be surfaced
  as an interpretive annotation that CONSUMES taxation/03's model by exact
  id — never a second model: an agent holding multiple retention-agent
  qualities retains under EACH activated quality at that quality's
  per-activity statutory rate (especial 15 + exportador habitual
  65-agro/15-rest; otro agente 15 + exportador 65/15; operadora 15 to
  afiliados + especial 15 to own proveedores), per AG 5-2013 art. 45 and
  AG 425-2006 **art. 9** — whose in-corpus verification is the S-GT2
  RESOLVED GOQ-118/R52 finding (art. 4 = Sistema procedure, art. 9 =
  dualidad rule; taxation/03 LB-017/FR-084), cited here as a resolved
  annotation and never re-opened. The differing statutory grounds for the
  non-exporter quality (LOSAT D-1-98 art. 6 for contribuyente especial vs
  D-20-2006 art. 6 for otro agente) are recorded as distinct provenance,
  never merged. (LB-006; EVID-496; R52/GOQ-118 resolved kin → OQ-004;
  cross-ref GT-TAX-FR-084)
- **GT-FIN-FR-172:** The operative-percentage rule shall be consumed from
  GT-TAX-FR-085 (Sistema-de-Retenciones model, saas resolution service):
  the agent keys each invoice's total amount **including IVA** and the
  system determines the retention percentage per law-defined
  agent/purchase type — rates are never user-picked from the criterio;
  mixed-product invoices support prorrateo ("se podrá realizar el
  prorrateo correspondiente"). The GOQ-119 S-GT2 modeling call
  (configuration-driven dualidad + saas Sistema-% resolution + prorrateo)
  is consumed by id; the residual same-invoice co-application tension
  (65% AND 15% both stated for a D-29-89 exporter who is also especial)
  remains a deployment-configuration decision under that call. The RetWeb
  operational surfaces rendering this interpretation are consumed by exact
  id: the dualidad multi-rate presentation rows (GT-FIN-FR-038), the
  retention line model with its validations (GT-FIN-FR-043/044) and the
  IVA carga-masiva monto agrícola decomposition (GT-FIN-FR-074).
  (LB-006; EVID-496; GOQ-119 kin → OQ-005; cross-ref GT-TAX-FR-085,
  GT-FIN-FR-038, GT-FIN-FR-043, GT-FIN-FR-044, GT-FIN-FR-074)
- **GT-FIN-FR-173:** The omission sanction shall be carried as an
  interpretive support annotation ONLY: failing to retain under one of two
  held qualities is already the retention-omission infraction ("si solo
  realiza la retención por una de las calidades de agente de retención que
  posee… tendrá la sanción respectiva"), with multa = the omitted tax plus
  the duty to enter — supporting the sanction rows owned by taxation/06.
  The CT article divergence (65_ cites CT art. 91; 64_ quotes CT art. 94
  num. 7 + SANCIÓN for the same infraction) is RECORDED UNRESOLVED by
  S-GT2 in taxation/06 (LB-026 there, both texts verbatim, no winner —
  evaluation keys on the infraction committed): this file kin-cites that
  record, never re-opens it, never picks a winner, and never sources a
  multa amount. (LB-002; EVID-492; R51/GOQ-120 kin → OQ-006)

### 3.4 Retained-IVA bookkeeping interpretive notes (confirming taxation/03)

- **GT-FIN-FR-174:** The nil-month duty shall be surfaced as a bookkeeping
  confirmation of GT-TAX-FR-105: the retention declaration is due monthly
  **even when no retention was effected** ("La declaración debe presentarse
  aun cuando no tenga movimiento") — the deadline value itself is consumed
  from the taxation chassis (GT-TAX-FR-105/106, R26 single window), never
  from this criterio (FR-178). (LB-005; EVID-495; cross-ref GT-TAX-FR-105,
  GT-FIN-FR-034/035/036)
- **GT-FIN-FR-175:** The agent's accounting surface shall carry the
  interpretive confirmations of GT-TAX-FR-091/FR-109: the **registro
  auxiliar** with the complete detail of retentions effected, and the
  named ledger captions **"IVA - Retenciones por Pagar"** (agent side) /
  **"IVA - Retenciones por compensar"** (provider side; AG 5-2013 art. 43)
  — seeded exactly as the statutory captions owned by taxation/03, with
  the criterio attached as confirmation evidence only.
  (LB-005; EVID-495; cross-ref GT-TAX-FR-091, GT-TAX-FR-109)
- **GT-FIN-FR-176:** The retained-IVA neutrality posting rule shall carry
  the interpretive confirmation of GT-TAX-FR-093: retained IVA is **never
  débito nor crédito fiscal for the agent** and may not be compensated
  with other tributes (sole exception: art. 1 exporters, GT-TAX-FR-073),
  and the agent is **solidariamente responsable** with the retained
  taxpayer when it failed to retain — enforced on the agent's ledger
  posting surface, confirming (never restating) the taxation contract.
  (LB-005; EVID-495; cross-ref GT-TAX-FR-093)
- **GT-FIN-FR-177:** The non-entering sanction pointer shall confirm
  GT-TAX-FR-104's generic citation-hygiene row: agents failing to enter
  retained tax are subject to the sanctions of the **Código Tributario and
  the Código Penal** "según lo que corresponda" (D-20-2006 art. 14 as
  quoted in 64_) — no article numbers are asserted beyond what taxation/06
  owns, and the multa-basis divergence stays under FR-173's kin-note.
  (LB-005; EVID-495; cross-ref GT-TAX-FR-104)
- **GT-FIN-FR-178:** DEADLINE GUARD: the three coexisting deadline
  formulations printed in 64_ — the D-20-2006 fragment "mensualmente aún y
  cuando no hubiere efectuado retención alguna", the LIVA art. 48 quote
  "dentro del plazo de quince días del mes inmediato siguiente", and the
  criterio's own analysis list "dentro de los 15 días hábiles siguientes a
  aquel en que se realice la retención" — shall NEVER source a deadline
  row: they are recorded verbatim as citation-precision variance only, and
  the operative deadline is consumed from W-GT2 statutory evidence
  (GT-TAX-FR-105/106, R26 single 15-días-hábiles window; RetWeb surfaces
  GT-FIN-FR-034/035 consume the same rows). (LB-005; EVID-495; cross-ref
  GT-TAX-FR-105, GT-TAX-FR-106, GT-FIN-FR-034, GT-FIN-FR-035)

### 3.5 6-2018 deducibilidad interpretive surface (confirming taxation/05 + payroll feeds)

- **GT-FIN-FR-179:** The sueldos IGSS-planilla gate shall be surfaced as a
  confirmation of GT-TAX-FR-169 (with GT-TAX-FR-168 lit. f), by exact id:
  sueldos/salaries are deductible only if, **when the patrono is
  IGSS-registration-obliged — ≥ 3 workers, or ≥ 1 for transporte terrestre
  de carga/pasajeros/mixto (IGSS Acuerdo 1123 art. 2)** — the workers
  figure in the **IGSS planilla** (LAT art. 23 lit. f: the planilla copy
  presented to IGSS is the acreditation before SAT); patronos NOT obliged
  (< 3 workers, non-transport) may still deduct backed by **libros de
  salarios o planillas**; directors/managers/gerentes/administradores are
  **trabajadores afiliados** reportable in the IGSS planillas (Acuerdo
  1123 art. 15; CT art. 102 fixes the book modes: libro de salarios ≥ 10
  workers, IGSS-model planillas 3-9). The gate's data feed is the payroll
  planilla flag (GT-PAY-FR-170) and the payroll book-mode rows
  (GT-PAY-FR-017/018) — consumed by id, never re-derived here.
  (LB-008; EVID-498; cross-ref GT-TAX-FR-169, GT-TAX-FR-168,
  GT-PAY-FR-170, GT-PAY-FR-017, GT-PAY-FR-018)
- **GT-FIN-FR-180:** The related-party sueldos cap shall be surfaced as a
  confirmation of GT-TAX-FR-167's related-party row: sueldos paid to
  socios or consejeros of civil/mercantile societies, cónyuges and
  parientes within the legal degrees are deductible up to a **total annual
  10% of renta bruta** — the cap value, scope and dated provenance stay
  with taxation/05; this layer attaches only the criterio's confirming
  interpretation. (LB-008; EVID-498; cross-ref GT-TAX-FR-167)
- **GT-FIN-FR-181:** The aguinaldo/bono 14 deduction caps shall be
  surfaced as a confirmation of GT-TAX-FR-167 (100% rows) and GT-TAX-FR-169
  (excess rule): each December prestación is deductible **up to 100% of one
  monthly salary**; any excess paid is NOT deductible **unless** backed by
  a **pacto colectivo de condiciones de trabajo debidamente homologado por
  el Ministerio de Trabajo y Previsión Social** (a config-identifiable
  pacto-linked excess); respaldo = planillas / libros de salarios / recibos
  — values and cap rows owned by taxation/05; payroll kin: the
  three-benefit taxonomy and December-absence regime of
  `04_statutory-bonuses.md` (GT-PAY-FR-095/097). (LB-009; EVID-499;
  cross-ref GT-TAX-FR-167, GT-TAX-FR-169, GT-PAY-FR-095, GT-PAY-FR-097)
- **GT-FIN-FR-182:** NEGATIVE-FR (GOQ-121): Criterio 6-2018 cites the Ley
  Reguladora de la Prestación del Aguinaldo and the Ley de Bonificación
  Anual **by title only — no decree numbers anywhere** — therefore this
  criterio shall NEVER backfill the GOQ-09 instruments: no instrument row,
  citation surface or seeded reference may attach a decree number to
  either bonus law with 65_ as its only anchor (the December aguinaldo
  statutes D-76-78/D-1633 remain absent — payroll/04's absence regime
  GT-PAY-FR-095 stands; bono 14's registry identity D-42-92 rests on 40_,
  never on 65_). The criterio's arts. 1-2 paraphrase is usable as
  interpretive support ONLY; a validation gate shall reject any
  decree-number assertion whose sole provenance is this criterio.
  (LB-009; EVID-499; GOQ-121 → OQ-003; GOQ-09 kin payroll/04 OQ-001)
- **GT-FIN-FR-183:** The dietas gate shall be surfaced as a confirmation
  row: dietas paid to a **pequeño contribuyente** are deductible by the
  payer ONLY IF the payer effects the ISR retention **con carácter
  definitivo** at the LAT art. 44 rate types (per AG 213-2013 art. 9) AND
  the payment is proven with recibos/comprobantes **afectos al Impuesto de
  Timbres Fiscales y de Papel Sellado Especial para Protocolos** (D-37-92);
  dietas are themselves rentas de actividades lucrativas (hecho generador
  LAT art. 10 num. 8). The LAT art. 44 rate VALUES are never restated from
  the criterio — they resolve from taxation/05 `isr_rates.csv`; RetWeb kin
  surfaces consumed by id: the ISR retention catalog's dietas conceptos
  (GT-FIN-FR-060) and the carga-masiva RECIBO use case for non-invoice-
  backed dietas (GT-FIN-FR-072). (LB-010; EVID-500; cross-ref
  GT-FIN-FR-060, GT-FIN-FR-072, `isr_rates.csv`)

### 3.6 OCR & citation-hygiene guards

- **GT-FIN-FR-184:** CLAUSE-LEVEL CITATION BAN (GOQ-116): pages 4, 5 and 8
  of 64_ are EMPTY in the OCR — the D-20-2006 obligations/solidarity/
  retained-IVA clauses (the unnumbered article whose quote resumes
  mid-sentence on p.6) lose their article numbers. No requirement, LB row
  or citation surface may cite those clauses BY ARTICLE NUMBER from 64_:
  the obligations chassis cites 78_/79_ via taxation/03 (LB-008 = D-20-2006
  art. 7 obligations; LB-012 = AG 425-2006 arts. 2-5, FR-093/FR-105/
  FR-109) instead; the 64_ fragment is stored with a `number_lost` flag
  and its clean-copy acquisition rides OQ-001. (LB-005 loc.; EVID-495;
  GOQ-116 → OQ-001)
- **GT-FIN-FR-185:** R50 PROPAGATION GUARD: the print defect "El Decreto
  número 20-2008" [sic] — where every contextual indicator demands 20-2006
  — is transcribed verbatim wherever the 2-2019 table is quoted
  (companion of FR-170), and NO seeded instrument row, regime label,
  citation surface or generated document may propagate "20-2008" as the
  retention-regime decree; a data-hygiene check rejects any such seeding.
  (LB-004; EVID-494; R50)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance; snapshot-on-write. This file stores NO statutory constants —
only instrument reference rows, confirmation annotations keyed to taxation
FR ids/CSV rows, interpretive notes and hygiene guards. Criterio texts and
dates are reference data (`shared`); confirm-only validation gates are saas
CI-gate kin; bookkeeping confirmations surface on the odoo ledger.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.criterio.instrument | criterio_no / approved / applicable_from / ponente / weight_clauses / fiscalizacion_reserved | char / date / date / char / char list / boolean | 2-2019: 2019-04-22 / 2019-06-01 / "GERENCIA DE CONTRIBUYENTES ESPECIALES GRANDES" [sic]; 6-2018: 2018-04-23 / 2018-04-23 / INTENDENCIA DE ASUNTOS JURÍDICOS / true; weight = in-text clauses only (GOQ-117) | FR-165, FR-166 |
| l10n_gt.criterio.baselegal.map | criterio_no / instrument / articles / note | char / char / char list / char | 64_: NO LAT anywhere; 65_: LAT-based map as printed; routing target = taxation LB rows, never the criterio | FR-167 |
| l10n_gt.criterio.confirmation | criterio_no / target_fr / csv_row / evid / direction / sic_flags | char / char (taxation FR id) / char / char / selection=confirms / char list | rate-table confirmation keyed GT-TAX-FR-072/074..080/086 + `iva_retention_rates.csv`; deduction caps keyed GT-TAX-FR-167/168/169 + `isr_rates.csv`; sic_flags carry R50 "20-2008" | FR-169, FR-170, FR-180..183 |
| l10n_gt.criterio.dualidad | quality_pairs / grounds / sistema_pct_ref / prorrateo / resolved_annotations | char pairs / selection LOSAT D-1-98 art. 6 vs D-20-2006 art. 6 / char (GT-TAX-FR-085) / boolean / json | per-quality retention at per-activity statutory rates (GT-TAX-FR-084); GOQ-118 resolved (art. 4 + art. 9 both correct); GOQ-119 modeling call; same-invoice tension = deployment config | FR-171, FR-172 |
| l10n_gt.criterio.bookkeeping | nil_month / registro_auxiliar / cuentas / neutrality / solidarity / penal_art14 | boolean ×6 + char pair | captions exactly "IVA - Retenciones por Pagar" / "IVA - Retenciones por compensar" (GT-TAX-FR-091/091-kin); exporter art. 1 carve-out GT-TAX-FR-073 | FR-174..177 |
| l10n_gt.criterio.deducibilidad | sueldos_gate / planilla_feed / related_cap / bonus_caps / pacto_excess / dietas_gate | json / char (GT-PAY-FR-170) / char (GT-TAX-FR-167) / json / boolean / json | gate scope ≥3 workers / transporte ≥1; 10% renta bruta; 100% caps + homologado pacto; dietas = definitive LAT 44 + timbre receipts | FR-179..183 |
| l10n_gt.criterio.guard | key | char | no_statutory_from_criterio; no_clause_level_from_64 (GOQ-116); sic_20-2008_never_propagated (R50); no_deadline_from_criterio; no_decree_backfill (GOQ-121); no_weight_formula (GOQ-117); sanction_kin_only (GOQ-120) | FR-168, FR-169, FR-173, FR-178, FR-182, FR-184, FR-185 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = ingestion,
transformation and authoritative validation in the Elixir core; `shared` =
contract items both sides must honor identically. Wave defaults (binding):
interpretive-layer validation rules (confirm-only guards) = `saas` CI-gate
kin (catalogs-governance pattern); bookkeeping-account surfacing = `odoo`;
criterio texts + dates as reference data = `shared`. Model names stable
across Odoo 17/18/19/20; no version-specific behavior required by this
file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-165 | shared | — (reference data §4) | criterio.instrument row 2-2019 | Dated rows per D16/D-GT10; ponente [sic] retained; interpretive-only status flag |
| FR-166 | shared | — (reference data §4) | criterio.instrument row 6-2018 | fiscalización_reserved=true carried; "presenta fecha" [sic] kept in the clause store |
| FR-167 | shared | — (reference data §4) | baselegal.map rows | Citation routing to taxation LBs; 64_ no-LAT fact recorded |
| FR-168 | saas | — (CI gate) | no_weight_formula guard | GOQ-117; external sourcing flagged, never invented |
| FR-169 | saas | — (CI gate) | no_statutory_from_criterio guard | Fails config rows anchored only to a criterio; keyed to taxation FR ids + CSV rows |
| FR-170 | shared | — (reference data §4) | rate-table confirmation annotation | Keyed GT-TAX-FR-072/074..080/086 + CSV; R50 [sic] transcription rides FR-185 |
| FR-171 | saas | — (CI gate / annotation) | dualidad confirmation vs GT-TAX-FR-084 | GOQ-118 resolved kin-note attached; grounds LOSAT vs D-20-2006 kept distinct |
| FR-172 | saas | — (CI gate / annotation) | Sistema-% + prorrateo confirmation vs GT-TAX-FR-085 | GOQ-119 call consumed; RetWeb surfaces cited by id (GT-FIN-FR-038/043/044/074) |
| FR-173 | shared | — (annotation) | sanction interpretive support | taxation/06 owns sanctions; GOQ-120 kin-note, no winner, no multa amount |
| FR-174 | shared | — (annotation) | nil-month confirmation | Deadline value consumed (GT-TAX-FR-105/106); never from the criterio |
| FR-175 | odoo | account books / account.account (captions) | registro auxiliar + cuentas seeding | Confirms GT-TAX-FR-091/109; captions exact |
| FR-176 | odoo | account.move.line (agent ledger) | neutrality + solidarity posting | Confirms GT-TAX-FR-093; exporter carve-out via GT-TAX-FR-073 |
| FR-177 | shared | — (annotation) | penal/CT sanction pointer | Confirms GT-TAX-FR-104 citation hygiene |
| FR-178 | saas | — (CI gate) | no_deadline_from_criterio guard | Three formulations stored verbatim as variance only; R26 window consumed |
| FR-179 | saas | — (CI gate / annotation) | sueldos gate confirmation | GT-TAX-FR-169/168 + GT-PAY-FR-170/017/018 feeds consumed by id |
| FR-180 | saas | — (annotation) | 10% related-party cap confirmation | GT-TAX-FR-167 owns value/scope |
| FR-181 | saas | — (annotation) | 100% caps + pacto confirmation | GT-TAX-FR-167/169 own values; GT-PAY-FR-095/097 kin |
| FR-182 | saas | — (CI gate) | no_decree_backfill guard (GOQ-121) | Rejects decree numbers anchored only to 65_; GOQ-09 kin |
| FR-183 | saas | — (annotation) | dietas gate confirmation | LAT 44 values from `isr_rates.csv`; GT-FIN-FR-060/072 kin |
| FR-184 | saas | — (CI gate) | no_clause_level_from_64 guard | GOQ-116; obligations cite 78_/79_ via taxation/03 LB-008/LB-012 |
| FR-185 | saas | — (data-hygiene check) | sic_20-2008_never_propagated guard | R50; transcription verbatim, propagation rejected |

## 6. Acceptance Criteria

- **AC-001:** Given the instrument rows, when inspected, then Criterio
  2-2019 carries approved 2019-04-22 + applicable_from 2019-06-01 with the
  ponente garble [sic] retained, and Criterio 6-2018 carries 2018-04-23 for
  both dates with the fiscalización reservation flagged — and neither row
  asserts any normative-weight formula. (FR-165, FR-166, FR-168)
- **AC-002:** Given a configuration row whose only statutory anchor is a
  criterio quote, when the confirm-only gate runs, then the row is rejected
  with a pointer to the owning taxation FR id/CSV row.
  (FR-169)
- **AC-003:** Given the 2-2019 rate-table confirmation annotation, when
  inspected, then every value (65/15/65/25>Q30,000/15/1.5/15/15 + Q2,500)
  maps to a GT-TAX-FR id + CSV row with its EVID id, the quote carries
  "El Decreto número 20-2008" [sic] verbatim, and no surface anywhere
  prints 20-2008 as the regime decree. (FR-170, FR-185)
- **AC-004:** Given the dualidad annotations, when resolved, then they
  consume GT-TAX-FR-084/085 as the single model, carry the GOQ-118
  resolved note (art. 4 = Sistema procedure, art. 9 = dualidad) without
  re-opening it, keep the LOSAT-art. 6 vs D-20-2006-art. 6 grounds
  distinct, and route operative % per factura through the Sistema model
  with prorrateo — the RetWeb render surfaces (GT-FIN-FR-038/043/044/074)
  are cited, never duplicated. (FR-171, FR-172)
- **AC-005:** Given the sanction annotation, when read, then it supports
  taxation/06's rows without stating a multa amount or article winner, and
  the CT 91 vs CT 94-7 divergence appears only as the recorded-unresolved
  kin-note. (FR-173)
- **AC-006:** Given an agent month with zero retentions and the agent's
  ledger, then the nil-month duty surfaces from GT-TAX-FR-105, the
  registro auxiliar and the exact captions "IVA - Retenciones por Pagar" /
  "IVA - Retenciones por compensar" are present, and retained IVA posts
  fiscally neutral (no débito/crédito; exporter art. 1 exception routed per
  GT-TAX-FR-073) with solidarity recorded. (FR-174, FR-175, FR-176)
- **AC-007:** Given the three 64_ deadline formulations, when the deadline
  engine resolves any retention declaration, then the operative window
  comes from GT-TAX-FR-105/106 (R26) and no deadline object is generated
  from a criterio sentence. (FR-174, FR-178)
- **AC-008:** Given a deduction under audit view, then the sueldos
  IGSS-planilla gate (obliged ≥3 / transporte ≥1; trabajadores afiliados
  incl. directors), the 10% related-party cap and the 100% bonus caps +
  pacto-homologado excess rule each display their taxation/05 anchor
  (GT-TAX-FR-167/168/169) with the 6-2018 confirmation attached.
  (FR-179, FR-180, FR-181)
- **AC-009:** Given any instrument reference to the aguinaldo or bono 14
  laws, when its provenance is traced, then a decree number whose only
  anchor is 65_ is rejected (GOQ-121); the December-absence regime
  (GT-PAY-FR-095) and the D-42-92 identity (from 40_) remain untouched by
  this criterio. (FR-182)
- **AC-010:** Given a dietas payment to a pequeño contribuyente, then the
  deducibility confirmation requires the definitive LAT-art. 44 retention
  and timbre-affected receipts, with rate values resolved from
  `isr_rates.csv` — never from the criterio. (FR-183)
- **AC-011:** Given any citation of the D-20-2006 obligations/solidarity/
  retained-IVA clauses, then it cites 78_/79_ via taxation/03 and never an
  article number attributed to 64_ (whose pp.4/5/8 are blank); the 64_
  fragment carries the `number_lost` flag. (FR-184)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.4);
question text verbatim from the register (abbreviated where noted). This
file OWNS GOQ-116/117/121 and carries the S-GT2-resolved kin GOQ-118/119/
120 as resolved/recorded annotations (never re-opened) plus the GOQ-09 kin
(via GOQ-121). Nothing outside this register is treated as an open
question; new gaps are flagged to the controller as non-OQ notes (no
invented ids).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-116 (owned; register lists F6, TX3 citations): "64_ OCR: pages 4/5/8 blank — the D-20-2006 obligations/solidarity/retained-IVA clauses (presumably arts. 5-8) lose article numbers; clean copy needed for clause-level citations." Affects FR-184 (clause-level citation ban active; obligations chassis cites 78_/79_ via taxation/03 LB-008/LB-012) and the `number_lost` fragment store of LB-005. | no | GT synthesis wave S-GT4 → acquisition queue (clean 64_ scan) | open |
| OQ-002 | GOQ-117 (owned; register lists F6 minor): "Criterios normative weight: neither prints the 'obligatorio para la SAT' formula — source externally if needed." Affects FR-168 (no surface asserts the internal-bind characterization from these files; in-text weight clauses only) and FR-165/166 weight_clauses fields. | no | GT synthesis wave S-GT4 → external sourcing (SAT criterios framework / LOSAT) if a weight assertion is ever required | open |
| OQ-003 | GOQ-121 (owned; register lists F6 × P3): "65_ cites bono-14/aguinaldo laws by title only (no decree numbers) — cannot backfill GOQ-09 instruments; paraphrase usable only as interpretive support." Affects FR-182 (negative-FR: decree-number backfill rejected; interpretive support only) and FR-181's confirmation scope. | no | GT synthesis wave S-GT4 (negative-FR standing; acquisition unchanged — GOQ-09 instruments via payroll/04 OQ-001 queue) | open |
| OQ-004 | GOQ-118 (S-GT2-resolved kin; register lists F6, TX3): "AG 425-2006 art. 4 vs 'art. 9' (64_ analysis) for the multi-group retention rule — instrument IS in corpus (79_); re-verify article contents at synthesis." RESOLVED S-GT2 (taxation/03 §7 OQ-005): art. 4 = Sistema-de-Retenciones procedure AND art. 9 = dualidad rule — both citations correct, R52 dissolved. Cited here as a resolved annotation on FR-171/LB-006; never re-opened. | no | GT synthesis wave S-GT2 (resolved; register annotation) | resolved |
| OQ-005 | GOQ-119 (S-GT2 modeling-call kin; register lists F6, TX3): "Dualidad same-invoice co-application: Criterios 1-2 state 65% (exporter quality) + 15% (second quality) on the same object without reconciling co-application; operative % per factura = SAT's Sistema de Retenciones — modeling call at synthesis." Modeling call MADE S-GT2 (taxation/03 FR-084/085): configuration-driven dualidad + saas Sistema-% resolution + prorrateo. Consumed here by exact id (FR-171/FR-172); the textual co-application tension remains a deployment-configuration decision — not re-litigated in this file. | no | GT synthesis wave S-GT2 (modeling call recorded; textual tension open) | open |
| OQ-006 | GOQ-120 (S-GT2-recorded kin; register lists F6, TX6): "Retención-omission multa basis: CT art. 91 (65_) vs CT art. 94 num. 7 (64_) — verify vs current consolidated CT." Recorded UNRESOLVED S-GT2 (taxation/06 LB-026, both texts verbatim, no winner; evaluation keys on the infraction committed). Cited here as a kin-note on FR-173 only; this file never re-opens it, never picks a winner, never sources a multa amount. | no | GT synthesis wave S-GT2 → record standing; resolve only with a newer CT consolidation | open |
| OQ-007 | GOQ-09 (kin via GOQ-121; register lists P3): "Missing bonus laws: December aguinaldo D-76-78 + D-1633, Q250 incentivo D-37-2001, D-7-2000 (all quoted-only/absent). NEVER invent December mechanics until acquired." This file's half is discharged by the GOQ-121 negative-FR (FR-182: 65_ cannot backfill the instruments); the acquisition queue and December-absence regime are owned by payroll/04 (its OQ-001). | no | GT synthesis wave S-GT3 → acquisition queue (payroll/04 OQ-001; this file kin-only) | open |
