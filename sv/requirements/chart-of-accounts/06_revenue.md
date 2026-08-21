# SV — Chart of accounts — Revenue: five-step engine, contract balances, contract costs, disclosures (Sección 23 + Apéndice 23A)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file encodes the *ingreso de actividades ordinarias* (revenue) engine of
the *Norma de Contabilidad NIIF para las PYMES* (Accounting Standard for SMEs,
32_) Sección 23 — the IFRS-15-aligned five-step model (contract identification,
distinct commitments, transaction price, allocation, recognition) — together
with its integral application guide Apéndice 23A (modifications, warranties,
customer options, principal-vs-agent, non-cash consideration, sales with
return, licences, royalties), the contract-balance presentation rules
(contract asset vs receivable vs contract liability), the contract-cost rules
(obtain costs expensed; fulfilment-cost asset with its special impairment),
and the disclosure set (disaggregation, balances, commitments, methods,
judgments).

It does **not** cover: financial-instrument measurement and impairment
(`03_financial-instruments-fx.md` — contract-asset/receivable impairment
consumed by id); inventory and PPE/intangible cost routing for fulfilment
costs (`04_nonfinancial-assets.md` by id); provisions for non-distinct
warranties (`05_liabilities-equity-benefits.md` by id, Sección 21); the
ESF/income-statement line architecture (`02_coa-structure.md`); deferred tax
and edition versioning (`08_deferred-tax-adoption.md`). Fiscal computations
(IVA/ISR débito-credito windows, DTE emission timing) are owned by the
e-invoicing/taxation waves BY FR ID — this file owns the ACCOUNTING book
only; book control-transfer timing NEVER overrides fiscal anchoring on the
*hecho generador* (taxable event, D15 two clocks), and book-vs-fiscal timing
differences route through `08_deferred-tax-adoption.md` (T8) by filename,
never re-derived here.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling R29):
the operative framework LB = **32_** — *Norma de Contabilidad NIIF para las
PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official Spanish
translation; effective 2027-01-01 with early adoption permitted (A1; txt PAGE
315), cited by section/párrafo as printed. **33_** (EY guide) is
SECONDARY-ONLY (R29(a), EV33 OQ-1): never the sole LB of an FR.

**SOQ-46 instrument-gap note (rides every FR in this file and this wave):**
the Norma is jurisdiction-neutral on who applies it ("Las decisiones sobre
qué entidades están requeridas o autorizadas a utilizar las Normas NIIF de
Contabilidad completas o la Norma de Contabilidad NIIF para las PYMES
recaen en las autoridades legislativas y regulatorias y en los emisores de
normas de las distintas jurisdicciones", Prólogo P12; txt PAGE 22) and the
SV adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444,
or successor legislation) is NOT in the corpus (commercial-legal/03 OQ-002
tracks the acquisition). Nothing in this file invents SV thresholds; the
revenue engine encodes the Norma's own mechanics, which carry no SV-specific
parameters (Section 23's rules are all transaction-derived).

**Citation ruling (controller, binding):** where the EVID-293 evidence block
is thin for a specific párrafo, the FR cites `32_ + section/párrafo + txt
PAGE anchor` accompanied by EVID-293; otherwise EVID id + section/párrafo
normally.

**Two-track invariant (the wave's spine):** book revenue recognition anchors
on control transfer (Step 5); fiscal IVA *débito/crédito* windows and DTE
emission timing anchor on the *hecho generador* — owned by e-invoicing BY ID
(SV-EINV-FR-028; SV-EINV-FR-101; SV-EINV-FR-161; Ley IVA Arts. 62-63) — and
book timing NEVER overrides fiscal anchoring nor vice versa (D15); the two
tracks link by id and their differences route through
`08_deferred-tax-adoption.md` (T8) by filename.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 23, Paso 1: scope "Esta sección especifica cómo una entidad contabiliza un contrato individual con un cliente. Se permite que una entidad aplique esta sección a una cartera de contratos (o compromisos) similares si… no difiera materialmente o con importancia relativa…". 23.7 criteria: "(a) las partes del contrato han aprobado el contrato y se han comprometido a cumplir sus respectivas obligaciones; (b) la entidad puede identificar los derechos de cada parte…; (c) la entidad puede identificar las condiciones de pago…; (d) el contrato tiene esencia comercial; y (e) es probable que la entidad reciba la contraprestación a la que tiene derecho, cuando esta sea exigible." 23.8-23.9 re-assessment only on significant change in facts and circumstances. 23.10 non-qualifying: "reconocerá como pasivo cualquier contraprestación recibida del cliente. Si la contraprestación no es reembolsable, la entidad dará de baja el pasivo y reconocerá la contraprestación como ingreso de actividades ordinarias cuando: (a) el contrato se ha completado y la entidad ha recibido la totalidad, o casi la totalidad, de la contraprestación prometida…; o (b) el contrato se ha cancelado." 23.11 duration = present enforceable rights; 23.12 modifications → 23A.2-23A.4; 23.13 combination: "combinará dos o más contratos celebrados al mismo tiempo o casi al mismo tiempo con el mismo cliente (o con partes relacionadas del cliente)… como un único contrato si…: (a) los contratos se negocian como un paquete con un objetivo comercial único; (b) los importes que el cliente pagará en uno de los contratos dependen del precio o del rendimiento del otro contrato; o (c) los bienes o servicios comprometidos… son un compromiso único de acuerdo con el Paso 2." Scope excludes leases, insurance, financial-instruments-type contracts and non-monetary same-industry exchanges | Step 1 contract identification: portfolio application allowed if not materially different; five contract criteria (approval+commitment, identifiable rights, identifiable payment terms, commercial substance, probable collection); re-assessment only on significant change; non-qualifying → consideration held as a liability, derecognized to income only when completed-and-substantially-collected or cancelled; combination of same-time contracts as one when package / interdependent amounts / single commitment | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.2-23.13 (txt PAGE 202-204) (EVID-293) |
| LB-002 | Norma NIIF para las PYMES, Sección 23, Paso 2: 23.15 series: "esencialmente los mismos, pero en momentos discretos a lo largo del tiempo… como un compromiso único si: (a) cada bien o servicio distinto de la serie cumple los criterios para ser un compromiso cumplido a lo largo del tiempo (véase el párrafo 23.54); y (b) la entidad utilizaría el mismo método para medir su progreso…". 23.16-23.17 distinct two criteria (benefit on its own + separable promise: not highly dependent on, interrelated with or affected by the other goods/services); distinct-goods menu includes warranties (23A.5-23A.7), options for additional goods or services (23A.8-23A.13), agent-arranged third-party transfers (23A.14-23A.20) and licences (23A.28-23A.37). 23.18-23.21 implicit promises ("compromisos pueden estar implícitos en las prácticas comerciales habituales… si éstas crean una expectativa válida en el cliente"). 23.22 setup/administrative activities are not commitments unless they transfer a good or service; non-refundable upfront fees related to such activities "se incluye en el precio de la transacción y se asigna a los compromisos del contrato de acuerdo con los Pasos 3 y 4" | Step 2 distinct commitments: two-criteria test; series-of-distinct single promise; implicit promises; setup/admin activities and non-refundable upfront fees | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.14-23.22 (txt PAGE 204-206) (EVID-293) |
| LB-003 | Norma NIIF para las PYMES, Sección 23, Paso 3: 23.23 "El precio de la transacción es el importe de la contraprestación que una entidad espera tener derecho a cambio de transferir los bienes o servicios comprometidos con cliente, excluyendo los importes recaudados por la entidad en nombre de terceros (por ejemplo, algunos impuestos sobre las ventas)." 23.24 determination basis + assumptions (transfer per contract; no cancellation/renewal/modification). 23.25-23.32 variable consideration: estimate via (a) expected-value or (b) most-likely-amount methods "de forma congruente"; restriction — included only "en la medida en que sea altamente probable" (to the extent highly probable) that no significant revenue reversal will occur when the uncertainty resolves; update at each reporting date; allocated on standalone prices as at contract inception. 23.31 refund liabilities. 23.33 royalties from licences: apply 23A.37. 23.34-23.35 consideration payable to customer. 23.36-23.37 deferred payment = financing transaction (11.13B): "descontará el importe de la contraprestación comprometida a una tasa de interés de mercado para un instrumento de deuda similar, determinada al inicio del contrato… reconocerá la diferencia… como ingresos por intereses de acuerdo con el método del interés efectivo… presentará los ingresos por intereses de forma separada". 23.38 ≤1-year practical exemption: "puede no aplicar los párrafos 23.36 y 23.37 si… espera que un cliente pague… en el plazo de un año". Non-cash consideration at fair value, else standalone-selling-price fallback (23A.21-23A.22) | Step 3 transaction price: excludes third-party-collected amounts (e.g. some sales taxes — IVA never revenue); variable consideration estimate + highly-probable restriction + updates; refund liabilities; royalties last-event; significant financing → PV + separate interest with ≤1-year practical exemption; non-cash at FV else standalone-price fallback | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.23-23.38 (txt PAGE 206-208) (EVID-293) |
| LB-004 | Norma NIIF para las PYMES, Sección 23, Paso 4: 23.42-23.43 "asignará el precio de la transacción en proporción a esos precios de venta independientes (es decir, sobre la base de un precio de venta independiente relativo). La entidad no reasignará el precio… para reflejar cambios en los precios de venta independientes después del inicio del contrato"; best evidence of standalone selling price = observable price when sold separately. 23.44 estimation if not observable: "toda la información que esté razonablemente disponible… incluidas las condiciones del mercado, los factores específicos de la entidad…" — methods "el uso de los precios de los competidores… para bienes o servicios similares, o los costos esperados del bien o servicio más un margen apropiado" (adjusted-market / cost-plus), applied consistently. 23.45-23.48 discount/variable exceptions: relative-SSP default; "si la asignación… no representa el importe de la contraprestación a la que la entidad espera tener derecho… utilizará otro método… podría asignar el descuento o importe variable a uno o varios de los compromisos"; series rule variant (23.48); Step 4 not applied when all commitments satisfied in the inception period / at the same moment or single commitment (23.40-23.41) | Step 4 allocation: relative standalone selling prices (observable else estimate); discount/variable allocation exceptions including the series rule | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.39-23.48 (txt PAGE 208-209) (EVID-293) |
| LB-005 | Norma NIIF para las PYMES, Sección 23, Paso 5: 23.49-23.53 control transfer ("Una entidad cumple un compromiso al transferir el control del bien o servicio específico del compromiso al cliente"; control = present ability to direct use and obtain benefits; repurchase arrangements considered — forward/call defeat control). 23.54 over-time criteria: "(a) un cliente recibe y utiliza inmediatamente los beneficios del desempeño…; (b) un cliente controla el activo a medida que la entidad lo fabrica o mejora…; o (c) el activo creado… no puede ser fácilmente redirigido a otro cliente (véase el párrafo 23.55) y el cliente original está obligado a pagar a la entidad por el trabajo realizado hasta la fecha (véase el párrafo 23.56)". 23.55 no-alternative-use: significantly-lower-price/significant-rework-cost OR substantial contractual restrictions prohibiting sale to another customer. 23.56 right to payment: "(a) un derecho incondicional presente al pago por el trabajo realizado hasta la fecha; o (b) un derecho exigible a demandar o retener el pago… si el contrato se cancela… por cualquier motivo que no sea el incumplimiento por parte de la entidad". 23.57-23.59 point-in-time indicators: present right to payment, legal title, physical possession, risks and rewards, acceptance; absence of an indicator does not preclude control. 23.60-23.61 acceptance clauses: wait for customer acceptance if conformity cannot be determined from available information. 23.62-23.66 progress methods: output ("métodos producto": surveys, units delivered, elapsed time) / input ("métodos de recursos": elapsed time, hours, costs incurred "excluyendo los costos que no contribuyen, o no son proporcionales, al progreso… (por ejemplo, ineficiencias y materiales desperdiciados o no instalados)"); consistent application; remeasure each period, changes treated as estimate changes per Sección 10. 23.67 right to invoice: "está autorizada a reconocer los ingresos… por el importe que tiene derecho a facturar" when directly corresponding to value of work to date | Step 5 recognition: over-time three criteria with no-alternative-use + right-to-payment detail; point-in-time indicators + acceptance; progress methods (output/input, wasted costs excluded); right-to-invoice practical method | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.49-23.67 (txt PAGE 209-213) (EVID-293) |
| LB-006 | Norma NIIF para las PYMES, Sección 23, costos: 23.68 obtain costs: "reconocerá los costos de obtener un contrato con un cliente como un gasto cuando se incurra en ellos, a menos que otra sección… requiera que los costos se reconozcan como parte del costo de un activo." 23.69-23.72 fulfilment costs: other sections first (Sección 13/17/18); else asset if "(a) dichos costos se relacionan directamente con un contrato (incluidos los contratos futuros) que la entidad puede identificar específicamente…; (b) esos costos crean o mejoran los recursos de la entidad que utilizará para cumplir… compromisos en el futuro; y (c) la entidad espera recuperar los costos"; direct labor/materials/allocations qualify, general and administrative costs expensed; costs relating to already-satisfied commitments expensed (past performance). 23.73-23.76 subsequent measurement: cost less accumulated amortization and impairment; "amortizará el activo basándose en el patrón de transferencia de los bienes o servicios con los que se relaciona"; impairment per Sección 27 EXCEPT recoverable amount = "(a) el importe restante de la contraprestación que la entidad espera recibir… menos (b) los costos restantes de proporcionar esos bienes o servicios aún no incurridos"; remaining consideration includes only amounts whose receipt is probable | Contract costs: obtain costs expensed; fulfilment-cost asset three criteria; amortization per transfer pattern; impairment = remaining consideration (probable only) − remaining costs | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.68-23.76 (txt PAGE 213-214) (EVID-293) |
| LB-007 | Norma NIIF para las PYMES, Sección 23, saldos: 23.77-23.78 performed contract presented "sobre la base del contrato en su conjunto" as contract asset or contract liability per the relation between performance and payment; "Si una entidad ha recibido una contraprestación (o tiene una cuenta por cobrar) antes de transferir bienes o servicios… reconocerá un pasivo del contrato cuando se realice el pago o este venza, lo que ocurra primero", derecognized to revenue on transfer (Paso 5). 23.79 contract asset: right to consideration for transfers before payment, "excluyendo cualquier importe presentado como una cuenta por cobrar"; "evaluará el deterioro de un activo contractual y reconocerá y medirá cualquier pérdida por deterioro de acuerdo con la Sección 11 Instrumentos Financieros." 23.80 receivable = "derecho incondicional… incondicional si solo es necesario el paso del tiempo antes de que venza el pago"; refundability does not defeat unconditionality (receivable + refund liability); "presentará las cuentas por cobrar por separado de los activos y pasivos contractuales". 23.81 alternative labels allowed with sufficient distinguishing information | Contract balances: contract asset vs receivable (unconditional = passage of time only) vs contract liability; separate presentation; contract-asset impairment via Sección 11 | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.77-23.81 (txt PAGE 215) (EVID-293) |
| LB-008 | Norma NIIF para las PYMES, Sección 23, revelaciones: 23.82 disaggregation "utilizando categorías basadas en las características… relevantes para comprender su rendimiento financiero" — (a) tipo de bien o servicio; (b) región geográfica; (c) mercado o tipo de cliente; (d) tipo de contrato; (e) duración del contrato; (f) calendario de transferencia (point-in-time vs over-time); (g) naturaleza del compromiso (principal vs agente). 23.83 opening/closing balances of trade receivables and contract assets separately + Sección 11 impairment losses. 23.84 contract-liability opening/closing balances + revenue recognized out of the opening balance. 23.85 commitments description: when performance typically occurs, payment terms (incl. financing-transaction flag and variable consideration), third-party organization (agent), return/refund obligations, warranty types. 23.86 progress methods used. 23.87-23.88 judgments (timing of satisfied commitments; transaction price determination; allocation). 23.89 fulfilment-cost asset closing balances by asset category. 23.90 23.38-option and disproportionate-cost option disclosures | Disclosures: disaggregation categories; balances (receivables/contract assets/impairment; contract liabilities + release); commitments; methods; judgments; fulfilment-cost assets; option use | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.82-23.90 (txt PAGE 216-217) (EVID-293) |
| LB-009 | Norma NIIF para las PYMES, Apéndice de la Sección 23 — Guía de aplicación ("Este Apéndice es una parte integral de la Sección 23"): 23A.2-23A.4 modification taxonomy: separate contract if "(a) se comprometen bienes o servicios adicionales que son distintos…; y (b) el precio del contrato original aumenta en un importe que refleje el precio de venta independiente… y cualquier cambio apropiado…"; else future-distinct → terminate-and-new (new transaction price = unrecognized original consideration + modification increase); else "como si siempre hubiera sido parte del contrato original… ajuste a los ingresos en la fecha de la modificación… (base de actualización acumulativa)". 23A.5-23A.7 warranties: "Si un cliente puede elegir comprar el bien o servicio con o sin garantía, la garantía es distinta… asignará una parte del precio de la transacción a ese compromiso"; if not choosable → Sección 21 Provisiones y Contingencias. 23A.8-23A.13 customer options: "incentivos de venta, créditos (o puntos) de recompensa para clientes, opciones de renovación… u otros descuentos"; separate commitment if "(a) la opción otorga al cliente un derecho material… (i) solo está disponible para un cliente que haya celebrado ese contrato; y (ii) permite… adquirir… con un descuento sobre su precio de venta independiente; y (b) la opción puede contabilizarse… sin costo o esfuerzo desproporcionado"; allocate transaction price; "reconocerá ingresos… cuando la entidad transfiera esos bienes o servicios futuros o cuando la opción expire"; option standalone price = discount adjusted for the discount available without exercising + probability of exercise; renewal options measured on expected total consideration. 23A.14-23A.20 principal vs agent: principal = controls the specified good/service before transfer (indicators: primary responsibility incl. acceptability; inventory risk before/after; pricing discretion) → gross; agent → "importe de las tarifas o comisiones" net. 23A.21-23A.22 non-cash: FV "a menos que este no pueda estimarse razonablemente… medirá… sobre la base del precio de venta independiente de los bienes o servicios prometidos al cliente". 23A.23-23A.27 sales with return: recognize "(a) ingresos… por los productos… que la entidad espera que no sean devueltos; (b) un pasivo por reembolso… que espera que sean devueltos; y (c) un activo por devoluciones… clasificados como inventario" measured at former carrying amount less recovery costs and "estimaciones de las posibles disminuciones del valor… (por ejemplo, debido a daños, obsolescencia o disminución de los precios de venta)"; like-for-like and defective-product swaps excluded; remeasure each period (refund liability → revenue; return asset → expense). 23A.28-23A.36 licences: access ("derecho de acceso a la propiedad intelectual… tal como existe durante el periodo de licencia" → over-time) vs use ("tal como existe en el momento en que se concede" → point-in-time); access if entity expects activities substantially affecting the benefit "al cambiar la esencia de la propiedad intelectual" or "al exponer directamente al cliente a cualquier efecto positivo o negativo"; over-time → 23.62-23.67; point-in-time → 23.57-23.61, "no puede ser anterior al momento en que el cliente puede utilizarla y beneficiarse de ella". 23A.37 royalties: "reconocerá… dicha regalía cuando (o a medida que) ocurra el último de dos eventos: (a) el compromiso… se ha cumplido…; o (b) se produce la venta o el uso posterior" | Appendix 23A (integral): modification taxonomy; warranties distinct-if-separately-purchasable else Sec 21; customer options material right; principal-vs-agent gross vs net; sales-with-return (refund liability + return asset + NRV-adjusted inventory); licences access-vs-use; royalties last-event | `sv/sources/32_NIIF_PYMES_2025.pdf` | Apéndice de la Sección 23, párrs. 23A.1-23A.37 (txt PAGE 218-224) (EVID-293) |
| LB-010 | Norma NIIF para las PYMES, Sección 11 Instrumentos Financieros (impairment of contract assets and receivables: "evaluará el deterioro de un activo contractual… de acuerdo con la Sección 11"; 23.80/23.83) — consumed from `03_financial-instruments-fx.md` SV-COA-FR-064..066 BY ID; the impairment engine mechanics are never restated in this file | Contract-asset/receivable impairment follows Section 11 (owned by the financial-instruments file by id) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 23, párrs. 23.79-23.80, 23.83 (txt PAGE 215-216) + Sección 11 (EVID-293) |
| LB-011 | Norma NIIF para las PYMES, Sección 21 Provisiones y Contingencias (non-distinct warranties: "Si el cliente no tiene opción de comprar el bien o servicio sin garantía, la garantía no es distinta… contabilizará la garantía de acuerdo con la Sección 21") — consumed from `05_liabilities-equity-benefits.md` BY ID | Non-distinct warranties route to Section 21 provisions (owned by the liabilities file by id) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Apéndice 23A, párr. 23A.7 (txt PAGE 219) (EVID-293) |
| LB-012 | Ley IVA, Arts. 62-63 (fiscal débito/crédito adjustment windows; 3-month NCE/NDE windows) — FISCAL track, consumed from the e-invoicing wave BY ID (`e-invoicing/01_document-types.md` SV-EINV-FR-028; `e-invoicing/03_events.md` SV-EINV-FR-101; `e-invoicing/02_transmission.md` SV-EINV-FR-161). DTE emission timing anchors on the hecho generador; never re-derived or overridden here (D15) | IVA Law Arts. 62-63: fiscal adjustment windows — consumed by id; book control-transfer timing never overrides fiscal anchoring | `sv/sources/01_Ley_IVA.pdf` | Arts. 62-63 pp. 27-29 (EVID-054; consumed via e-invoicing LB rows by id) (EVID-293 xref) |

## 3. Functional Requirements

### 3.1 Scope and Step 1 — contract identification (Sección 23, 23.1-23.13)

- **SV-COA-FR-182:** The system shall apply the revenue engine per contract
  with the Sección 23 scope carve-outs — leases (Sección 20), insurance
  contracts, financial-instrument-type contracts and non-monetary exchanges
  between entities of the same industry with similar value are OUT of scope —
  and shall allow portfolio application to a portfolio of similar contracts
  (or commitments) when the entity reasonably expects the portfolio outcome
  not to differ materially (*con importancia relativa*) from
  contract-by-contract application.
  (LB-001; EVID-293)
- **SV-COA-FR-183:** The system shall apply the revenue model to a customer
  contract ONLY when ALL five Step-1 criteria are met: (a) the parties have
  approved the contract and committed to their obligations; (b) the entity
  can identify each party's rights as to the goods or services to be
  transferred; (c) the entity can identify the payment terms; (d) the
  contract has commercial substance (*esencia comercial*); and (e) it is
  probable that the entity will collect the consideration to which it is
  entitled when it becomes due — the criteria are assessed at contract
  inception and re-assessed ONLY on a significant change in facts and
  circumstances (D15: each determination snapshots as-of its assessment date
  on the record).
  (LB-001; EVID-293)
- **SV-COA-FR-184:** The system shall implement the non-qualifying-contract
  rule: when a contract fails the 23.7 criteria, any consideration received
  is recognized as a LIABILITY (never revenue); when the consideration is
  non-refundable, the liability is derecognized to revenue only when (a) the
  contract is completed AND the entity has received all or substantially all
  (*casi la totalidad*) of the promised consideration, or (b) the contract is
  cancelled.
  (LB-001; EVID-293)
- **SV-COA-FR-185:** The system shall implement contract combination: two or
  more contracts entered into at the same time or nearly the same time with
  the same customer (or with related parties of the customer) are combined
  and accounted for as a SINGLE contract when one or more of these criteria
  are met: (a) negotiated as a package with a single commercial objective;
  (b) the amounts payable in one contract depend on the price or performance
  of the other; or (c) the goods or services committed (or some of them in
  each contract) are a single commitment under Step 2.
  (32_ Sección 23, párr. 23.13, txt PAGE 204; EVID-293; LB-001)

### 3.2 Step 2 — distinct commitments and the series rule (23.14-23.22)

- **SV-COA-FR-186:** The system shall implement the two-criteria
  distinctness test: a good or service is DISTINCT only when (a) the customer
  can benefit from it on its own or together with other readily available
  resources, AND (b) the promise is separately identifiable from other
  promises in the contract — the good or service is NOT distinct when it
  highly depends on, is highly interrelated with, or is significantly
  affected by another good or service in the contract — and shall recognize
  that distinct promises may be explicit OR implicit in customary business
  practices, published policies or specific statements creating a valid
  expectation in the customer.
  (LB-002; EVID-293)
- **SV-COA-FR-187:** The system shall implement the series rule: a series of
  distinct goods or services that are substantially the same transferred at
  discrete times over time is accounted for as a SINGLE commitment when
  (a) each distinct good or service in the series meets the over-time
  criteria of 23.54, and (b) the entity would use the SAME progress-measurement
  method for each distinct good or service in the series.
  (LB-002; EVID-293)
- **SV-COA-FR-188:** The system shall implement the no-promise rule for
  setup and administrative activities: such activities are NOT commitments
  unless they transfer a good or service to the customer; a non-refundable
  upfront fee related to them does not create a commitment but IS included
  in the transaction price and allocated to the contract's commitments under
  Steps 3 and 4.
  (LB-002; EVID-293)

### 3.3 Step 3 — transaction price (23.23-23.38)

- **SV-COA-FR-189:** The system shall determine the transaction price as the
  consideration to which the entity expects to be entitled in exchange for
  the promised goods or services, EXCLUDING amounts collected on behalf of
  third parties (e.g. some sales taxes) — **IVA is NEVER revenue**: IVA
  charged on customer invoices posts to the tax-payable track (fiscal
  débito), never to an income account — and shall determine the price on the
  contract terms and customary business practices, assuming the goods or
  services transfer per the contract and that the contract is not cancelled,
  renewed or modified.
  (LB-003; EVID-293)
- **SV-COA-FR-190:** The system shall implement the variable-consideration
  estimator: when consideration includes a variable amount (discounts,
  rebates, refunds, penalties, performance bonuses), the entity estimates it
  by ONE of two methods — expected value, or the most-likely amount — applied
  consistently to similar contracts in similar circumstances.
  (LB-003; EVID-293)
- **SV-COA-FR-191:** The system shall implement the highly-probable
  restriction: variable consideration is included in the transaction price
  only to the extent it is HIGHLY PROBABLE (*altamente probable*) that no
  significant revenue reversal will occur when the uncertainty resolves — and
  shall update the estimate (and its allocation, on standalone prices as at
  contract inception) at each reporting date, treating changes as estimate
  revisions (consumed from `01_framework-policies.md` SV-COA-FR-017 by id).
  (LB-003; EVID-293)
- **SV-COA-FR-192:** The system shall recognize a REFUND LIABILITY
  (*pasivo por reembolso*) for consideration received (or receivable) that
  the entity expects to refund, with subsequent changes in refund
  expectations recognized as adjustments in revenue.
  (LB-003; EVID-293)
- **SV-COA-FR-193:** The system shall implement the royalty exception: for
  sales- or usage-based royalties from licences, revenue is recognized when
  (or as) the LAST of two events occurs — (a) the satisfaction (or partial
  satisfaction) of the commitment to which the royalty is allocated, or
  (b) the subsequent sale or use.
  (LB-003; LB-009 23A.37; EVID-293)
- **SV-COA-FR-194:** The system shall implement significant-financing
  treatment: when payment is deferred and the arrangement constitutes a
  financing transaction, the consideration is discounted to present value at
  the market interest rate for a similar debt instrument determined at
  contract inception, and the difference between the promised consideration
  and the discounted amount is recognized as INTEREST INCOME via the
  effective-interest method (11.15-11.20, consumed from
  `03_financial-instruments-fx.md` by id), presented SEPARATELY from
  customer-contract revenue — with the practical exemption that 23.36-23.37
  need NOT be applied when, at contract inception, the entity expects the
  customer to pay within one year of transfer of the goods or services (the
  election disclosed per 23.90).
  (LB-003; EVID-293)
- **SV-COA-FR-195:** The system shall measure non-cash consideration
  (*contraprestación no dineraria*, e.g. barter) at FAIR VALUE, falling back
  — when fair value cannot be reasonably estimated — to the standalone
  selling price of the goods or services promised to the customer in
  exchange.
  (LB-003; LB-009 23A.21-23A.22; EVID-293)

### 3.4 Step 4 — allocation (23.39-23.48)

- **SV-COA-FR-196:** The system shall allocate the transaction price to each
  distinct commitment on a RELATIVE STANDALONE SELLING PRICE basis,
  determined at contract inception, with the observable standalone price
  (the price at which the entity sells the good or service separately in
  similar circumstances to similar customers) as the best evidence — and
  shall NEVER reallocate the transaction price for subsequent changes in
  standalone selling prices after inception (Step 4 not applied when every
  commitment is satisfied in the same reporting period as inception, at the
  same point in time per 23.58, or the contract has a single commitment).
  (LB-004; EVID-293)
- **SV-COA-FR-197:** The system shall estimate the standalone selling price
  when it is not directly observable, considering all reasonably available
  information (market conditions, entity-specific factors, customer/class
  information) with estimation methods applied consistently — supported
  methods being the adjusted-market approach (e.g. competitor prices for
  similar goods or services) and the expected-cost-plus-margin approach
  (expected costs plus an appropriate margin).
  (LB-004; EVID-293)
- **SV-COA-FR-198:** The system shall implement the discount and
  variable-consideration allocation exceptions: a discount or variable amount
  is allocated to each commitment on the relative-standalone-price basis,
  BUT when that allocation does not represent the consideration the entity
  expects to be entitled to for satisfying each commitment, an alternative
  method is used — allocating the discount or variable amount to some (one or
  several) commitments only — including the series-rule variant: when a
  series of distinct goods or services is a single commitment and the
  transaction price includes variable consideration, the variable amount is
  allocated to the distinct goods or services in the series on relative
  standalone prices unless an alternative method better represents the
  entitled consideration.
  (LB-004; EVID-293)

### 3.5 Step 5 — recognition (23.49-23.67)

- **SV-COA-FR-199:** The system shall recognize revenue when (or as) the
  entity satisfies a commitment by transferring CONTROL of the promised good
  or service to the customer — control being the customer's present ability
  to direct the use of the asset and obtain the economic benefits from it —
  considering repurchase arrangements: the customer does NOT obtain control
  when the entity has both the right and obligation to repurchase (a
  forward) or the right to repurchase (a call).
  (LB-005; EVID-293)
- **SV-COA-FR-200:** The system shall implement the over-time criteria: a
  commitment is satisfied OVER TIME when ANY of (a) the customer receives and
  uses the benefits of the entity's performance as the entity performs
  (e.g. routine or recurring cleaning services); (b) the customer controls
  the asset as it is created or enhanced (e.g. a construction contract where
  the customer controls the work in progress); or (c) the created asset has
  no alternative use to the entity AND the customer is obliged to pay for
  work performed to date.
  (LB-005; EVID-293)
- **SV-COA-FR-201:** The system shall implement the no-alternative-use test
  (criterion (c) limb 1): the asset cannot be easily redirected to another
  customer when (a) the entity would sell the finished asset to another
  customer at a SIGNIFICANTLY LOWER price than the original customer pays, or
  would incur significant costs relative to the asset's cost to rework it
  (e.g. a highly customized asset), OR (b) substantial contractual
  restrictions prohibit selling the asset to another customer while it is
  being made or enhanced (e.g. a legal obligation to sell the WIP to the
  customer).
  (LB-005; EVID-293)
- **SV-COA-FR-202:** The system shall implement the right-to-payment test
  (criterion (c) limb 2): the customer is obliged to pay for work performed
  to date (from contract terms or applicable law) when the entity has
  (a) an UNCONDITIONAL PRESENT right to payment for work performed to date,
  or (b) an enforceable right to demand or retain payment for work performed
  to date if the contract is terminated before completion for any reason
  OTHER than the entity's non-performance.
  (LB-005; EVID-293)
- **SV-COA-FR-203:** The system shall implement point-in-time recognition
  with the control-transfer indicators: when a commitment is not satisfied
  over time, revenue is recognized at the specific point the customer
  obtains control, identified through indicators — (a) present right to
  payment; (b) legal title; (c) physical possession; (d) significant risks
  and rewards of ownership; (e) customer acceptance — the indicators not
  being conclusive: absence of one does not preclude control when other
  transaction characteristics clearly show the customer's present ability to
  direct use and obtain benefits.
  (LB-005; EVID-293)
- **SV-COA-FR-204:** The system shall implement acceptance-clause handling:
  when a contract contains a customer-acceptance clause (allowing the
  customer to cancel or require remediation of non-conforming goods or
  services) and the entity cannot determine conformity with agreed
  specifications from information available to it, the entity does NOT
  conclude control has transferred until customer acceptance is received.
  (LB-005; EVID-293)
- **SV-COA-FR-205:** The system shall implement progress measurement for
  over-time commitments: the method rationally reflects the transfer of
  control and is applied consistently to similar commitments — OUTPUT methods
  (*métodos producto*: surveys/engineering estimates of work performed when
  objectively measurable; units delivered when each unit transfers equal
  value; elapsed time when control transfers evenly) and INPUT methods
  (*métodos de recursos*: elapsed time when efforts are expended evenly;
  hours worked when related to transfer; costs incurred when related to
  transfer) — with costs that do NOT contribute or are NOT proportionate to
  progress EXCLUDED (inefficiencies, and materials wasted or not installed,
  e.g. cost-to-cost with waste excluded); progress is remeasured at each
  reporting date, changes accounted for as estimate changes (SV-COA-FR-017
  by id).
  (LB-005; EVID-293)
- **SV-COA-FR-206:** The system shall implement the right-to-invoice
  practical measure: when the entity is entitled to consideration that
  relates DIRECTLY to the value of the entity's work to date (e.g. a fixed
  rate per hour of service delivered), revenue is recognized for the amount
  the entity has the right to invoice.
  (LB-005; EVID-293)

### 3.6 Apéndice 23A applications (integral to Sección 23)

- **SV-COA-FR-207:** The system shall implement the contract-modification
  taxonomy: a modification (a change in scope or price, or both, approved by
  the parties) is accounted for as (i) a SEPARATE contract when additional
  DISTINCT goods or services are added AND the price increases by an amount
  reflecting their standalone selling prices (appropriately adjusted for the
  contract circumstances); else (ii) TERMINATE-AND-NEW when the post-modification
  goods or services are distinct from those already transferred — the
  original is treated as cancelled and a new contract created at the
  unrecognized original consideration plus the modification increase; else
  (iii) AS-IF-PART-OF-THE-ORIGINAL with a CUMULATIVE CATCH-UP: the change in
  transaction price and progress is recognized as an adjustment to revenue
  at the modification date.
  (32_ Apéndice 23A, párrs. 23A.2-23A.4, txt PAGE 218-219; EVID-293; LB-009)
- **SV-COA-FR-208:** The system shall implement the warranty split: a
  warranty sold when the customer CAN choose to purchase the good or service
  with or without it is DISTINCT — accounted for as a separate commitment
  with a portion of the transaction price allocated to it; when the customer
  CANNOT choose (warranty not separately purchasable), it is NOT distinct
  and is accounted for under Sección 21 provisions (consumed from
  `05_liabilities-equity-benefits.md` by id — mechanics never restated
  here).
  (32_ Apéndice 23A, párrs. 23A.5-23A.7, txt PAGE 219; EVID-293; LB-009;
  LB-011)
- **SV-COA-FR-209:** The system shall implement the customer-option material
  right: an option to acquire additional goods or services for free or at a
  discount (sales incentives, customer reward credits or points, renewal
  options, other future discounts) is a SEPARATE commitment when (a) it
  grants a material right (*derecho material o con importancia relativa*)
  available ONLY to contracting customers, allowing acquisition at a discount
  to the standalone selling price, and (b) it can be accounted for as a
  separate commitment without disproportionate cost or effort (relief
  registry per SV-COA-FR-012 by id) — with a portion of the transaction
  price allocated to the option (its standalone price reflecting the
  discount the customer would obtain, adjusted for discounts available
  WITHOUT exercising and the probability of exercise; renewal options
  measured on expected total consideration), recognized as revenue when the
  future goods or services transfer or when the option expires.
  (32_ Apéndice 23A, párrs. 23A.8-23A.13, txt PAGE 219-220; EVID-293; LB-009)
- **SV-COA-FR-210:** The system shall implement the principal-vs-agent
  determination: when a third party is involved in supplying the good or
  service, the entity is a PRINCIPAL when it controls the specified good or
  service before transfer — indicated by primary responsibility for
  fulfilment (including acceptability), inventory risk before or after
  transfer, and pricing discretion — recognizing revenue GROSS (the
  consideration it expects for transferring the specified good or service);
  otherwise it is an AGENT recognizing revenue NET (the fees or commissions
  it expects for arranging the transfer) as it satisfies its commitment to
  arrange.
  (32_ Apéndice 23A, párrs. 23A.14-23A.20, txt PAGE 220-221; EVID-293; LB-009)
- **SV-COA-FR-211:** The system shall implement sales with a right of
  return: for products sold with refund/credit/exchange rights, recognize
  (a) revenue for the consideration expected NOT to be returned; (b) a
  REFUND LIABILITY for consideration expected to be returned; and (c) a
  RETURN ASSET for the products expected to be returned, classified as
  INVENTORY and measured at the former carrying amount LESS expected
  recovery costs and estimated decreases in value (damage, obsolescence,
  selling-price declines — NRV-adjusted), with the corresponding cost-of-sales
  adjustment; like-for-like exchanges (same type, quality, condition, price)
  and defective-product swaps for working ones are EXCLUDED from expected
  returns; the refund liability (through revenue) and return asset (through
  expense) are remeasured at each reporting date for changed expectations.
  (32_ Apéndice 23A, párrs. 23A.23-23A.27, txt PAGE 221-222; EVID-293; LB-009)
- **SV-COA-FR-212:** The system shall implement the licence access-vs-use
  split: for a DISTINCT licence of intellectual property (software,
  technology, brands, patents, franchises, music, films), the commitment is
  satisfied OVER TIME when the licence grants a RIGHT OF ACCESS to the IP as
  it exists during the licence period — the entity expecting activities that
  substantially affect the customer's benefit by changing the essence of the
  IP (design, content, functionality) or by exposing the customer directly
  to their positive or negative effects (e.g. ongoing brand-value
  maintenance) — and at A POINT IN TIME when the licence grants a RIGHT OF
  USE of the IP as it exists at grant; over-time licences measure progress
  per 23.62-23.67 (FR-205), point-in-time licences transfer per 23.57-23.61
  (FR-203), never earlier than when the customer can first use and benefit
  from the licence.
  (32_ Apéndice 23A, párrs. 23A.28-23A.36, txt PAGE 222-223; EVID-293; LB-009)

### 3.7 Contract balances (23.77-23.81)

- **SV-COA-FR-213:** The system shall present each performed contract on a
  WHOLE-CONTRACT basis as a contract asset or contract liability, per the
  relation between (a) performance in transferring the promised goods or
  services and (b) customer payment: consideration received (or receivable)
  BEFORE transfer creates a CONTRACT LIABILITY (*pasivo del contrato*)
  recognized when payment is made or due — whichever first — derecognized to
  revenue when (or as) the goods or services transfer.
  (LB-007; EVID-293)
- **SV-COA-FR-214:** The system shall recognize a CONTRACT ASSET (*activo
  del contrato*) when goods or services transfer before payment (or before
  payment is due), EXCLUDING any amount presented as a receivable — and
  shall assess contract-asset impairment under Sección 11, recognized and
  measured per `03_financial-instruments-fx.md` SV-COA-FR-064..066 BY ID
  (mechanics never restated here).
  (LB-007; LB-010; EVID-293)
- **SV-COA-FR-215:** The system shall implement the receivable boundary and
  separate presentation: a RECEIVABLE (*cuenta por cobrar*) is an
  UNCONDITIONAL right to consideration — unconditional when ONLY the passage
  of time is required before payment falls due (an expected refund does not
  defeat unconditionality: a receivable may coexist with a refund liability);
  receivables are presented SEPARATELY from contract assets and contract
  liabilities in the statement of financial position, and alternative labels
  for "contract assets"/"contract liabilities" are permitted only with
  sufficient information for users to distinguish receivables from contract
  assets.
  (LB-007; EVID-293)

### 3.8 Contract costs (23.68-23.76)

- **SV-COA-FR-216:** The system shall recognize costs of OBTAINING a
  contract as an EXPENSE when incurred, unless another section of the Norma
  requires their inclusion in an asset's cost (e.g. those reachable under
  `04_nonfinancial-assets.md` by id).
  (LB-006; EVID-293)
- **SV-COA-FR-217:** The system shall implement the fulfilment-cost asset:
  costs of fulfilling a contract are accounted for under the pertinent other
  section first (inventories, PPE, intangibles — `04_nonfinancial-assets.md`
  by id); costs OUTSIDE other sections' scope are recognized as an ASSET
  only when ALL three criteria are met: (a) directly related to a contract
  (including a future contract) the entity can specifically identify (e.g.
  costs of a contract not yet approved); (b) they create or enhance the
  entity's resources for satisfying (or continuing to satisfy) commitments
  in the future; and (c) the costs are expected to be recovered — direct
  labor, direct materials and directly-related allocations qualify, while
  general and administrative costs normally do NOT (expensed), and costs
  relating to commitments already satisfied (or partially satisfied) are
  expensed as incurred (past performance).
  (LB-006; EVID-293)
- **SV-COA-FR-218:** The system shall measure the fulfilment-cost asset
  after recognition at COST less accumulated amortization and accumulated
  impairment — amortized on the pattern of transfer of the related goods or
  services — with impairment recognized per Sección 27 EXCEPT that the
  recoverable amount equals the REMAINING CONSIDERATION the entity expects
  to receive for the related goods or services (including only amounts whose
  receipt is probable) MINUS the remaining costs of providing those goods or
  services not yet incurred.
  (LB-006; EVID-293)

### 3.9 Disclosures (23.82-23.90)

- **SV-COA-FR-219:** The system shall disaggregate revenue from contracts
  with customers into categories based on the characteristics of revenue,
  contracts or customers relevant to understanding financial performance —
  the example categories being (a) type of good or service (e.g. principal
  product lines); (b) geographic region; (c) market or customer type (e.g.
  government vs non-government); (d) contract type (fixed-price vs
  time-and-materials); (e) contract duration; (f) transfer timing
  (point-in-time vs over-time); and (g) commitment nature (principal vs
  agent revenue).
  (LB-008; EVID-293)
- **SV-COA-FR-220:** The system shall disclose the contract-balance amounts:
  (a) opening and closing balances of trade receivables and contract assets
  SEPARATELY, plus the total impairment losses recognized on them in the
  period (Sección 11, via SV-COA-FR-064..066 by id); (b) opening and closing
  contract-liability balances and the revenue recognized in the period that
  was included in the opening contract-liability balance.
  (LB-008; LB-010; EVID-293)
- **SV-COA-FR-221:** The system shall disclose its contract commitments:
  when the entity typically satisfies them (on shipment, on delivery, as
  services render or on completion); principal payment terms (when payment
  typically falls due, whether the contract constitutes a financing
  transaction, whether consideration is variable); the nature of the goods
  or services committed — highlighting any commitment to arrange transfer by
  a third party when the entity acts as agent; return, refund and similar
  obligations; and warranty types and related obligations.
  (LB-008; EVID-293)
- **SV-COA-FR-222:** The system shall disclose the methods and judgments:
  the progress-measurement methods used (input/output methods and how they
  were applied); the judgments with a significant effect on recognized
  amounts in (a) determining the transaction price and (b) allocating it to
  identified commitments; the closing balance of fulfilment-cost assets
  (23.70) by principal asset category (e.g. pre-contract and set-up costs);
  the use of the 23.38 one-year financing exemption; and the
  disproportionate-cost facts when an option meeting 23A.9(a) is not
  accounted for as a separate commitment (SV-COA-FR-012 by id).
  (LB-008; LB-006; LB-009; EVID-293)

### 3.10 Fiscal two-track: book timing vs fiscal anchoring (binding invariant)

- **SV-COA-FR-223:** The system shall keep the book revenue track and the
  fiscal track strictly separate: book recognition timing follows control
  transfer (Step 5, FR-199..206) and NEVER overrides, delays or re-times
  fiscal IVA *débito/crédito* recognition or DTE emission — which anchor on
  the *hecho generador* (taxable event) and the Ley IVA Arts. 62-63
  adjustment windows owned by the e-invoicing wave BY ID
  (SV-EINV-FR-028; SV-EINV-FR-101; SV-EINV-FR-161), never re-derived here —
  and conversely no fiscal document event (emission, invalidation, NCE/NDE
  adjustment) by itself constitutes book revenue recognition or
  derecognition; where book and fiscal timing/amount differ (e.g. over-time
  revenue spanning invoices, return adjustments outside fiscal windows),
  the policy-event record links the two tracks by id and the difference
  routes through `08_deferred-tax-adoption.md` (T8) by filename.
  (LB-012; LB-001; LB-005; EVID-293 xref/D15)

## 4. Data Model

Layer semantics: all entities are Odoo-native posting/config surfaces on
account.move and its contract engine — no SaaS rows (see §5). Amounts are
transaction-derived; no SV-specific parameters exist to encode (SOQ-46
config-gap discipline: Section 23 mechanics carry no SV thresholds). No
printed data table warrants a CSV sidecar (default none per plan).

**Revenue contract engine (l10n_sv_chart.revenue_contract):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.revenue_contract | step1_state | select + snapshot date | qualifying (5 criteria + evidence) · non_qualifying_liability · completed_substantially_collected · cancelled — D15 snapshot-on-write; re-assessed only on significant change | FR-183, FR-184 |
| l10n_sv_chart.revenue_contract | portfolio_flag | boolean | portfolio application when outcome not materially different | FR-182 |
| l10n_sv_chart.revenue_contract | combination_group | m2m | combined same-time contracts (package / interdependence / single-commitment criterion recorded) | FR-185 |
| l10n_sv_chart.revenue_contract | modification_state | select + date + linked contract | separate_contract · terminate_and_new · cumulative_catchup (23A.2-4 taxonomy) | FR-207 |
| l10n_sv_chart.commitment | distinct_basis | select | explicit · implicit_practice · implicit_policy · implicit_statement | FR-186 |
| l10n_sv_chart.commitment | series_single | boolean + method | series-of-distinct single commitment (over-time + same progress method) | FR-187 |
| l10n_sv_chart.commitment | kind | select | good · service · warranty_distinct · option_material_right · agent_arranged · licence_access · licence_use · series | FR-186, FR-208, FR-209, FR-210, FR-212 |
| l10n_sv_chart.commitment | setup_admin_no_promise | boolean | non-refundable upfront fee in transaction price, no commitment | FR-188 |

**Transaction price components (l10n_sv_chart.price_component):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.price_component | third_party_collected | boolean | amounts collected for third parties (IVA) excluded — posts to tax-payable, never income | FR-189 |
| l10n_sv_chart.price_component | variable_method | select | expected_value · most_likely (applied consistently) | FR-190 |
| l10n_sv_chart.price_component | restriction_basis | text + date | highly-probable no-significant-reversal basis; updated each period; allocation as-at inception | FR-191 |
| l10n_sv_chart.price_component | refund_liability | monetary | expected-refund liability + adjustment account | FR-192 |
| l10n_sv_chart.price_component | royalty_last_event | boolean | sales/usage-based licence royalties — last of satisfaction or sale/use | FR-193 |
| l10n_sv_chart.price_component | financing | boolean + rate + PV + dates | market rate for similar debt instrument at inception; effective-interest split; ≤1y practical exemption election (23.38; disclosure per 23.90) | FR-194 |
| l10n_sv_chart.price_component | noncash_measure | select | fair_value · ssp_fallback (23A.21-22) | FR-195 |

**Allocation and recognition (l10n_sv_chart.allocation / .recognition):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.allocation | ssp_basis | select | observable · adjusted_market · cost_plus — no post-inception reallocation | FR-196, FR-197 |
| l10n_sv_chart.allocation | exception_method | select | relative_ssp · alternative_some_commitments (discount/variable, incl. series variant) | FR-198 |
| l10n_sv_chart.recognition | mode | select | over_time · point_in_time | FR-200, FR-203 |
| l10n_sv_chart.recognition | overtime_criterion | select | simultaneous_receipt_use · customer_controls_wip · no_alternative_use_plus_payment (23.55/23.56 basis recorded) | FR-200, FR-201, FR-202 |
| l10n_sv_chart.recognition | pit_indicators | tags + acceptance flag | right_to_payment · legal_title · possession · risks_rewards · acceptance (wait-for-acceptance when conformity indeterminable) | FR-203, FR-204 |
| l10n_sv_chart.recognition | progress_method | select | output_survey · output_units · output_elapsed · input_elapsed · input_hours · input_costs — input costs exclude wasted/non-contributing | FR-205 |
| l10n_sv_chart.recognition | right_to_invoice | boolean | direct-correspondence invoiced-amount measure | FR-206 |
| l10n_sv_chart.recognition | progress_changes | one2many | remeasure rows treated as estimate changes (SV-COA-FR-017 by id) | FR-205 |

**23A applications (l10n_sv_chart.license / .return_scheme):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.return_scheme | refund_liability · return_asset | monetary | expected returns split; return asset = former carrying amount − recovery costs − value decreases (NRV-adjusted inventory) | FR-211 |
| l10n_sv_chart.return_scheme | exclusions | boolean set | like-for-like swaps; defective-for-working swaps | FR-211 |
| l10n_sv_chart.return_scheme | remeasure | one2many | refund liability → revenue; return asset → expense | FR-211 |
| l10n_sv_chart.option_right | material_right | boolean + basis | only-for-contracting-customer + discount vs SSP; disproportionate-cost relief → FR-012 registry by id | FR-209 |
| l10n_sv_chart.option_right | ssp_estimate | computed | discount adjusted (non-exercise discount + exercise probability); renewal options on expected total consideration | FR-209 |
| l10n_sv_chart.license | access_use | select | access_over_time · use_point_in_time (essence-change / direct-exposure basis) | FR-212 |

**Balances and costs (posting surfaces on account.move):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.account (template) | contract_balance_class | select | receivable · contract_asset · contract_liability · refund_liability · return_asset_inventory — separate presentation labels | FR-213, FR-214, FR-215, FR-192, FR-211 |
| l10n_sv_chart.fulfill_cost | criteria | boolean set + snapshot | identifiable contract (incl. future) · creates/enhances resources · expected recovery; G&A excluded | FR-217 |
| l10n_sv_chart.fulfill_cost | impairment_inputs | monetary | remaining consideration (probable only) − remaining costs; amortization per transfer pattern | FR-218 |
| l10n_sv_chart.obtain_cost | expensed | boolean | expensed when incurred unless another section captures | FR-216 |
| l10n_sv_chart.revenue_contract | fiscal_track_link | m2m by id | e-invoicing DTE/correction surfaces (SV-EINV-FR-028/101/161 kin) — linked, never merged; differences → 08 by filename | FR-223 |

**Disclosure feeds (l10n_sv_chart.note_slot extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.note_slot | kind (revenue extensions) | select | rev_disaggregation · rev_balances · rev_commitments · rev_progress_methods · rev_judgments · rev_fulfill_cost_asset · rev_23_38_option · rev_option_disproportionate | FR-219..222 |
| l10n_sv_chart.note_slot | disaggregation_categories | tags | good_service_type · geography · market · contract_type · duration · transfer_timing · principal_agent | FR-219 |

## 5. Odoo Mapping

Layer semantics for this wave: the revenue engine is Odoo-native
(account.move posting, deferred-revenue/contract surfaces, analytic-based
progress, account.account template) — every FR maps `odoo`; no SaaS rows are
introduced because none of these FRs touch DTE generation/transmission (the
only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names stable
across Odoo 17/18/19/20 unless noted.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-182 | odoo | l10n_sv_chart.revenue_contract | scope + portfolio_flag | scope carve-outs static; portfolio allowed when not materially different |
| FR-183 | odoo | l10n_sv_chart.revenue_contract | step1_state + evidence | 5 criteria; re-assess only on significant change; D15 snapshot-on-write |
| FR-184 | odoo | account.move + contract liability account | non-qualifying liability posting | derecognition to income only on completed+substantially-collected or cancelled |
| FR-185 | odoo | l10n_sv_chart.revenue_contract | combination_group | 23.13 three criteria; combination is book-only, never a fiscal document merge (FR-223) |
| FR-186 | odoo | l10n_sv_chart.commitment | distinct_basis | two-criteria test + implicit promises |
| FR-187 | odoo | l10n_sv_chart.commitment | series_single | over-time + same method precondition |
| FR-188 | odoo | l10n_sv_chart.commitment / price_component | setup_admin_no_promise | upfront fee in price, allocated Steps 3-4 |
| FR-189 | odoo | account.move line engine + tax grids | third_party_collected | **IVA never revenue**: Odoo native tax lines already route IVA to tax payable; revenue lines post net of third-party-collected amounts — AC-005 |
| FR-190 | odoo | l10n_sv_chart.price_component | variable_method | expected-value vs most-likely, consistent per contract class |
| FR-191 | odoo | l10n_sv_chart.price_component | restriction_basis | highly-probable no-significant-reversal; per-period update; allocation as-at inception; estimate-change link FR-017 |
| FR-192 | odoo | account.account + account.move | refund_liability | changes through revenue |
| FR-193 | odoo | l10n_sv_chart.price_component | royalty_last_event | last of satisfaction or sale/use (23A.37) |
| FR-194 | odoo | account.move + interest income account | financing (rate/PV) | market rate at inception; effective interest 11.15-11.20 (03 by id); ≤1y election; 23.90 disclosure — AC-002 |
| FR-195 | odoo | l10n_sv_chart.price_component | noncash_measure | FV else SSP fallback (23A.21-22) |
| FR-196 | odoo | l10n_sv_chart.allocation | ssp_basis observable | relative SSP at inception; no reallocation |
| FR-197 | odoo | l10n_sv_chart.allocation | ssp_basis estimate | adjusted-market / cost-plus, consistently |
| FR-198 | odoo | l10n_sv_chart.allocation | exception_method | discount/variable to some commitments; series variant |
| FR-199 | odoo | account.move revenue posting | control-transfer trigger | repurchase forward/call defeat control |
| FR-200 | odoo | l10n_sv_chart.recognition | mode + overtime_criterion | three criteria, any-one-suffices |
| FR-201 | odoo | l10n_sv_chart.recognition | 23.55 basis | lower-price/rework OR contractual restriction |
| FR-202 | odoo | l10n_sv_chart.recognition | 23.56 basis | unconditional present right OR enforceable retain/demand |
| FR-203 | odoo | account.move + recognition | pit_indicators | five indicators, non-conclusive |
| FR-204 | odoo | l10n_sv_chart.recognition | acceptance flag | wait-for-acceptance when conformity indeterminable |
| FR-205 | odoo | analytic + l10n_sv_chart.recognition | progress_method | output/input menu; wasted-cost exclusion; remeasure = estimate change (FR-017) — AC-004; mapping gap → OQ-2 |
| FR-206 | odoo | account.move (invoicing) | right_to_invoice | invoiced-amount measure for direct-correspondence work |
| FR-207 | odoo | l10n_sv_chart.revenue_contract | modification_state | separate/terminate-new/cumulative-catchup (23A.2-4); book-only — DTE credit notes stay on the fiscal track (FR-223) |
| FR-208 | odoo | l10n_sv_chart.commitment | warranty_distinct | distinct → allocated price; else Sec 21 (05 by id) |
| FR-209 | odoo | l10n_sv_chart.option_right | material_right + ssp_estimate | reward credits/points, renewal options; revenue on transfer or expiry — AC-001; Odoo loyalty/wallet apps model discounts, not deferred material rights → OQ-3 |
| FR-210 | odoo | product/account.move revenue accounts | principal_agent | gross vs net account routing |
| FR-211 | odoo | l10n_sv_chart.return_scheme + accounts | refund_liability + return_asset | NRV-adjusted return inventory; exclusions; per-period remeasure — AC-003 |
| FR-212 | odoo | l10n_sv_chart.license | access_use | essence-change/direct-exposure basis; point-in-time not before usable |
| FR-213 | odoo | account.move + contract_liability account | whole-contract balance | payment-or-due-first trigger |
| FR-214 | odoo | account.account contract_asset + impairment | contract asset | impairment = 03 SV-COA-FR-064..066 by id |
| FR-215 | odoo | account.account receivable vs contract_asset | presentation split | unconditional = passage-of-time only; refund coexistence |
| FR-216 | odoo | account.move expense | obtain costs | expensed unless captured by 04's sections |
| FR-217 | odoo | l10n_sv_chart.fulfill_cost | criteria | three-criteria asset; G&A expensed; past-performance expensed |
| FR-218 | odoo | l10n_sv_chart.fulfill_cost | amortization + impairment_inputs | pattern-of-transfer amortization; impairment = remaining consideration (probable) − remaining costs |
| FR-219 | odoo | report layer + note_slot | disaggregation | seven example categories |
| FR-220 | odoo | report layer + note_slot | balances | receivables/contract assets separate + impairment; contract liabilities + opening-balance release |
| FR-221 | odoo | report layer + note_slot | commitments | timing/payment terms/agent/returns/warranties |
| FR-222 | odoo | report layer + note_slot | methods + judgments | progress methods; price/allocation judgments; fulfill-cost balances; 23.38 election; disproportionate-cost option |
| FR-223 | odoo | l10n_sv_chart.revenue_contract | fiscal_track_link | book control-transfer timing NEVER overrides fiscal hecho-generador anchoring (D15; SV-EINV-FR-028/101/161 by id); differences → `08_deferred-tax-adoption.md` (T8) by filename — AC-006 |

Version-regime notes (D12/D15): the encoded Sección 23 is the 3rd-edition
(Feb-2025) REVISED text (effective for annual periods beginning 2027-01-01,
early adoption permitted, A1; txt PAGE 315); the 3rd-edition change list
records consequent amendments (e.g. Sección 11 initial-measurement and
13.2/13.2A/13.14 inventory changes "derivadas de la Sección 23 revisada")
and the dividend-revenue relocation to Sección 11 (11.14A/11.55) — SV
2025-2027 books may still run the 2nd (2015) edition, whose Section 23
deltas route through the Tabla A1 paragraph-change map (txt PAGE 325-329)
owned by `08_deferred-tax-adoption.md` by id (SOQ-48; 2nd-edition full text
not in corpus). D15 anchors: all Step-1 determinations, restriction
assessments, progress remeasurements and modification classifications
resolve as-of their own event dates and snapshot on the record. The
dividend-revenue rules live in Sección 11 (03 by id), not here. Fiscal
débito windows and DTE timing never synchronize the book clock (D16
no-override). Mid-year go-live (D18): a migrating company's open contracts
ingest with their already-determined step states as `is_historical`
supporting rows (balances carried, no re-derivation of historical
recognition).

## 6. Acceptance Criteria

- **AC-001:** Given a customer loyalty scheme over a 10-pan (bread) purchase
  cycle priced at 2.00 per pan (cycle consideration 20.00) whose reward
  credits grant a material right, with the Step-4 allocation assigning
  2.00 (0.20 per pan) to the option commitment and leaving 1.80 per pan
  (18.00) as recognized revenue (guide-verified pattern, 32_
  23A.9-23A.13), when each of the ten pans transfers to the customer, then
  revenue recognizes at 1.80 per transferred pan, the option allocation sits
  in the contract liability, and the deferred amount recognizes as revenue
  only when the reward pan transfers or the option expires (FR-209,
  FR-213).
- **AC-002:** Given a two-year interest-free deferred-payment sale of goods,
  when the sale is booked, then revenue recognizes at the PRESENT VALUE of
  the consideration discounted at the market rate for a similar debt
  instrument determined at inception, and the difference between promised
  and discounted consideration accrues as interest income via the effective
  interest method, presented on a separate line from customer-contract
  revenue (FR-194).
- **AC-003:** Given a product sale where returns are expected, when the sale
  is booked, then the entry splits into (a) revenue for products expected
  not to be returned, (b) a refund liability for the expected-returned
  consideration, and (c) a return asset classified as inventory at the
  former carrying amount less recovery costs and estimated value decreases —
  with like-for-like exchanges excluded from expected returns (FR-211).
- **AC-004:** Given an over-time construction contract measured on
  cost-to-cost input method, when progress is computed, then the numerator
  includes only costs contributing to (proportionate with) progress —
  wasted materials and inefficiency costs are excluded from both cumulative
  and total-expected-cost denominators' progress contribution — and period
  remeasurements book as estimate changes, never policy changes or
  restatements (FR-205).
- **AC-005:** Given a customer invoice charging 13% IVA on a taxable sale,
  when the invoice posts, then the IVA amount routes to the tax-payable
  track and the income account receives only the net transaction price —
  no IVA amount ever posts to any revenue account, in any recognition
  scenario including deferred and over-time revenue (FR-189).
- **AC-006:** Given an over-time construction contract whose invoices are
  emitted on milestone dates that differ from control-transfer progress,
  when the month closes, then book revenue recognizes per progress
  (control transfer) while the fiscal débito posts per DTE emission on the
  hecho generador windows (Ley IVA 62-63, SV-EINV-FR-028/101/161 by id) —
  neither track re-times the other, and any period/amount difference routes
  to `08_deferred-tax-adoption.md` (T8) by filename (FR-223).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | Odoo deferred-revenue mapping gap: Odoo's native deferred/recognized revenue (unearned revenue accounts + recognition schedule templates on account.move) models a single "deferred revenue" bucket per journal item, with no per-contract classification of contract liability vs contract asset vs receivable and no whole-contract netting per 23.77 — how much of FR-213/214/215 needs a custom l10n_sv_chart contract-balance ledger vs account-level templates, and does the analytic account carry the contract identity? | no | Takumi (odoo-localizations) | open |
| OQ-2 | Percentage-mapping gap: which Odoo surface implements input progress with the wasted-cost exclusion (FR-205) — analytic-line cost aggregation, timesheet-based %, or project milestones — and does the right-to-invoice measure (FR-206) conflict with native invoicing-triggered revenue recognition (invoice on delivery/time = point-in-time default), requiring a per-commitment recognition-mode override? | no | Takumi (odoo-localizations) | open |
| OQ-3 | Loyalty/material-right gap: Odoo loyalty/wallet/coupon apps model rewards as price discounts on future orders, with no transaction-price allocation to a material-right commitment (FR-209) nor contract-liability deferral until transfer/expiry — custom allocation engine on top, or config-gap accepted with manual accrual? | no | Takumi (odoo-localizations) | open |
| OQ-4 | SV adoption instrument (SOQ-46, rides the wave): the revenue engine encodes 32_ Sección 23 with no SV-specific parameters; if the Consejo de Vigilancia instrument (CC Arts. 443-444 kin, commercial-legal/03 OQ-002) introduces SV revenue-related guidance, this file config-gaps it — no thresholds or exceptions invented here. | no | controller (acquisition tracked) | open |
