# GT — Taxation — IVA retenciones (general retention regime: D-20-2006 + AG 425-2006)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-22 |

## 1. Purpose

This file defines the functional requirements for the Guatemala **IVA
retention regime** (*retenciones del Impuesto al Valor Agregado*, IVA
withholding at source) under **Decreto 20-2006 Capítulo I (arts. 1–14)** and
its **Reglamento, Acuerdo Gubernativo 425-2006 Título II (arts. 2–25)**:
the six statutory agent classes and their rates — all percentages **of the
IVA itself** except the single fuel-card base exception; agent calificación
and lifecycle (carné, SAT Web list, activation/suspension); the
Sistema de Retenciones percentage-resolution model with *dualidad*
(multiple simultaneous agent qualities) and *prorrateo* (proration) for
mixed invoices; de-minimis and agent-to-agent abstention rules; card-scheme
mechanics (operator retention, exclusivity, Pago Total/Parcial); the
*constancia de retención* (retention certificate) document model; seller-side
netting with the 2-year stranded-remanente special account; and the
declaration/enterar chassis (monthly even-zero declaración jurada, first
15 días hábiles). It also carries the mandatory R55/GOQ-06 secondary-print
additions (pequeño 5% ≥ Q2,500.01; agropecuario 5% on total factura;
sector-público 25/5/5 provider-regime split) as dated rows marked
secondary-print-pending, never frozen, plus the in-corpus GOQ-118
verification (AG 425-2006 art. 4 vs art. 9) and the GOQ-119 modeling call.
The retention-rate matrix ships as the CSV sidecar
`gt/requirements/taxation/iva_retention_rates.csv` (one row per agent
class × rate × base qualifier, with status and provenance).

It does **not** cover: the pequeño contribuyente 5% *tarifa* and its Art. 48
pago-definitivo track (Task 2 file `02_iva-pequeno.md`, GT-TAX-FR-046..068 —
cross-referenced), the seller-side crédito/débito core mechanics and
Art. 25 refund channels (Task 1 file `01_iva-core.md`), facturas especiales
and their ISR side (Task 5), RetWeb/Declaraguate form mechanics, carga-masiva
formats and per-form declaration generation (F2-wave files; form numbers are
NEVER cited to D-20-2006/AG 425-2006 — R46), Código Tributario procedure and
sanctions (Task 6), or the FEL RETENC/FESP DTE complement mechanics (owned by
`gt/requirements/e-invoicing/`, cross-referenced by GT-EINV-FR id).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): IVA
retenciones = **78_ D-20-2006 arts. 1–14 + 79_ AG 425-2006 Título II**; the
"resolución 2-2010" myth is rejected (R23 — grep-verified absence in both
instruments). Form numbers never cite these instruments (RetWeb/48_ own
them — R46). Dated values (rates, thresholds, deadlines) follow the
dated-instrument regime D15/D16 (cite together): valid_from/valid_to rows +
instrument provenance, snapshot-on-write, rate rows are decree-bound, never
constants. EV04b prints (49_/52_) are SECONDARY sources:
manuals/portals are primary for mechanics, secondary for statutory
parameters — every EV04b-sourced rate row below is marked
secondary-print-pending pending GOQ-06/GOQ-01 reconciliation.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Decreto Número 20-2006, "Disposiciones Legales para el Fortalecimiento de la Administración Tributaria" (emitido 6-jun-2006; sancionado 20-jun-2006), Artículo 76: "Los artículos 38, 51, 52, 5 3 [sic], 58, 59, 60 y 62 del presente Decreto empezarán a regir ocho (8) días después de su publicación en el Diario Oficial, y el articulado restante empezará a regir el 1 de agosto del año 2006." Regime-basis verdict: neither 78_ nor 79_ cites any "Resolución 2-2010" as basis (grep-verified) | D-20-2006 identity + split vigencia: the entire retention regime (arts. 1–14) rules from the fixed date 1-Aug-2006; the 8-day articles are vehicle-tariff/defraudación reforms outside this file; the "2-2010" regime-basis myth is rejected (R23) | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.1 title; p.44 dates + Art. 76 (EVID-246; art. 74 reglamento mandate + art. 75 six-month SAT implementation window, EVID-256) |
| LB-002 | D-20-2006, Art. 1: "Las personas individuales o jurídicas que se inscriban ante la Administración Tributaria como exportadores habituales y cuya exportación mensual en promedio sea de cien mil quetzales (Q. 100,000.00) como mínimo, serán considerados agentes de retención, por lo que la Superintendencia de Administración Tributaria le dará aviso de su activación…" / (agro) "pagarán al vendedor o al prestador del servicio, el treinta y cinco por ciento (35%) del Impuesto al Valor Agregado (IVA) y le retendrán el sesenta y cinco por ciento (65%) de dicho impuesto, incluido en el monto total de cada factura." — products: "el café en cualquier forma, excepto tostado o soluble, azúcar de caña sin refinar, banano, cardamomo en cualquier estado, caña de azúcar, algodón, leche y otros productos agropecuarios" / (general) "…el ochenta y cinco por ciento (85%) del Impuesto al Valor Agregado (IVA) y le retendrán el quince por ciento (15%) de dicho impuesto…" / (D.29-89 firms) "…le retendrán el sesenta y cinco por ciento (65%) de dich o [sic] impuesto…" | Art. 1 exporter agents: registered habitual exporters with monthly average exports ≥ Q.100,000.00, activated by SAT aviso; three rates, all of the IVA itself: 65% on agricultural/livestock products (enumerated list, open with "otros productos agropecuarios"), 15% on other goods and services, 65% for D.29-89 enterprises | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.2 Art. 1 ¶1–4 (EVID-247; interpretive confirmation EVID-493) |
| LB-003 | D-20-2006, Art. 1 (crédito/deadline): "En todos los casos, la totalidad del impuesto retenido por el exportador será compensable con su crédito fiscal sujeto a devolución. De resultar tributo a favor de la Administración Tributaria, deberá enterarlo al fisco dentro del plazo de quince (15) días hábiles siguientes al período impositivo en que realizó la retención." / DJ "aún y cuando no tenga tributo qu e [sic] enterar al fisco…" / "la Superintendencia de Administración Tributaria creará un registro de exportadores, cuyo promedio mensual de exportaciones sea igual o mayor a cien mil quetzales…" | Art. 1 mechanics: exporter-retained IVA is compensable against refundable crédito fiscal (the sole exception to the non-compensation rule); enterar within 15 días hábiles following the período impositivo; even-zero declaración jurada; SAT creates the exporters' registry | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.2–3 Art. 1 crédito ¶ + párrafos 2–4 (EVID-248) |
| LB-004 | D-20-2006, Art. 2: "En las compras de bienes y adquisición de servici os [sic] que realicen los Organismos del Estado, las entidades descentralizadas, autónomas y semi -autónomas [sic] y sus empresas, con excepción de las municipalidades, pagarán al vendedor del bien o prestador del servicio, el setenta y cinco por ciento (75%) del Impue sto [sic] al Valor Agregado y le retendrán el veinticinco por ciento (25%) de dicho impuesto, incluido en el monto total facturado." / abstention: "…se abstendrá de realizar retenciones del Impuesto al Valor Agregado, cuando el monto de la compra de bienes o la prestación de servicios sea inferior a treinta mil quetzales (Q.30,000.00)." / "*Reformado el cuarto párrafo por el Artículo 24, del Decreto Del Congreso Número 4-2012 el 25-02-2012" / CURE (crédito): "…en el momento de la solicitud del pago del Comprobante Único de Registro de Egresos…" / penal: "…presentará la denuncia penal que en derecho corresponda…" | Art. 2 sector público: State entities (Organismos + decentralized/autonomous/semi-autonomous + their enterprises; **municipalidades excepted**) retain 25% of the IVA (pay 75%); abstention floor Q.30,000.00 (¶4 as reformed by D-4-2012 on 25-02-2012 — pre-2012 wording not in corpus, GOQ-65); credit operations retain at CURE payment request; penal denuncia for officials who fail to enter | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.3–4 Art. 2 + reform note (EVID-249) |
| LB-005 | D-20-2006, Art. 3: "…serán quienes actuarán como agentes de retención del Impuesto al Valor Agregado que pagu en [sic] los tarjeta-habientes, a los establecimientos afiliados… retendrán el quince por ciento (15%) del Impuesto al Valor Agregado incluido en el precio de venta… según la cantidad expresada en el voucher de compra…" / "Los establecimientos afiliados… serán los responsables ante el fisco por el ochenta y cinco por ciento (85%) del Impuesto al Valor Agregado no retenido…" / "deberán entregar la constancia mensual de retención a sus establecimientos afiliados…" / exclusivity: "Los otros agente s [sic] de retención… no procederán a efectuar la retención… cuando la compra… se hubiere efectuado utilizando tarjeta de crédito o de débito…" | Art. 3 card operators: retain 15% of the IVA included in the sale price per voucher amount; the affiliated merchant remains liable to the fisco for the 85% not retained; monthly consolidated constancia; exclusivity — card-paid purchases escape every other agent's retention | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.4 Art. 3 (EVID-250) |
| LB-006 | D-20-2006, Art. 4: "En el caso de la adquisición de combustible que sea pagado con tarjetas de crédito o de débito, el agente de retención retendrá el uno punto cinco por ciento (1.5 %) sobre el valor total de la transacción, siempre que en el precio de venta, también este incluido el Impuesto a la Distribución del Petróleo Crudo y Combustibles Derivados del Petróleo. El monto de lo retenido, se aplicará al pago del Impuesto al Valor Agregado a que está afecta la venta de dicho producto." | Art. 4 fuel-by-card: THE sole base exception — 1.5% **of the total transaction value** (which includes the petroleum-distribution tax), the withheld amount then applied against the fuel-sale IVA; never a % of IVA | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.5 Art. 4 (EVID-251; mirrored reglamento art. 24, EVID-265) |
| LB-007 | D-20-2006, Arts. 5–6: Art. 5: "Los contribuyentes que conforme a la normativa de la Administración Tributaria, se encuentren calificados como contribuyentes especiales, se constituyen en agentes de retención… Desde el momento en que la Administración Tributaria le hubiere notificado… su activación como ag ente [sic] de retención… pagará… el ochenta y cinco por ciento (85%)… y le retendrá el quince por ciento (15%) de dich o [sic] impuesto…" / Art. 6: "…podrán solicitar autorización para actuar como agentes de retención… quien después de evaluar su comportamiento tributario, resolverá dentro de un plazo de treinta (30) días hábiles…" / "…podrá designar como agentes de retención, a las personas individuales o jurídicas que estime pertinente." | Arts. 5–6: contribuyentes especiales (SAT-calified per its own normativa, agents from notification) at 15%; otros at 15% — either voluntary application (SAT resolves in 30 días hábiles) or open-ended SAT designation "que estime pertinente"; both with the 85/15 split and 15-días-hábiles enterar | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.5–6 Arts. 5 y 6 (EVID-252) |
| LB-008 | D-20-2006, Art. 7: "2. Enterar la totalidad del impuesto retenido y presentar… dentro de los primeros quince (15) días hábiles del mes inmediato siguiente, a aquel en que se realice la retención, una declaración jurada como agente retenedor que contenga el Número de Identificación Tributaria, nombre, denominación o razón social del proveedor…, el porcentaje de retención y valor retenido y la fecha de cada retenc ión [sic] realizada. La referida declaración deberá ser presentada mensualmente aún y cuando no hubiere efectuado retención alguna…" / "3. Llevar en la contabilidad un registro auxiliar con el detalle completo de las retenciones efectuadas." / "4. Entregar, la constancia de retención prenumerada y autorizada por cada operación sujeta a retención…, o de forma consolidada cuando el proveedor haya realizado más de una transacción… durante el mismo mes calendario…" / "El impuesto retenido no consti tuirá [sic] débito, ni crédito fiscal para el agente de retención, ni podrá ser compensado con tributos, salvo lo dispuesto en el articulo [sic] 1…" + solidarity + forms "en los formularios que proporcione la Superintendencia de Administración Tributaria…" | Art. 7 obligations chassis (all agents): enterar + monthly declaración jurada with per-provider fields {NIT, name, %, value, date}, due the first 15 días hábiles of the following month, mandatory even at zero; auxiliary retention registry in accounting; prenumerada/autorizada constancia per operation or monthly-consolidated; retained IVA fiscally neutral to the agent (no débito/crédito/compensation — sole exception art. 1 exporters); solidary liability; NO form number printed (R46) | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.6–7 Art. 7 nums. 1–5 + closing (EVID-253; interpretive confirmation EVID-495) |
| LB-009 | D-20-2006, Arts. 8–10: Art. 8: "…deberán operar la retención en el mismo periodo impositivo del Impuesto al Valor Agregado, en el que se declare la factura correspondiente." / Art. 9: "Cuando se realicen compras de bienes o se adquieran servicios entre personas individuales o jurídicas con la calidad de agentes de retención, deben abstenerse de efectuar la retención correspondiente. Si el pago se realizare utilizando tarjeta de crédito o débito se aplicará la retención establecida en los artículos 3 y 4…" / Art. 10: "…a excepción de los establecidos en los artículos 2, 3 y 4…, no practicarán la retención que corresponda, cuando les presten servicios o hagan compras menores a dos mil quinientos quetzales (Q 2,500.00)." | Arts. 8–10: seller books the suffered retention in the same período impositivo as the invoice declaration; agent-to-agent purchases abstain (card payments excepted → arts. 3/4); de minimis Q.2,500.00 per operation for arts. 1/5/6 agents — sector público (art. 2, Q.30,000), card operators and fuel-card excluded | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.7–8 Arts. 8, 9 y 10 (EVID-254) |
| LB-010 | D-20-2006, Arts. 11–14: Art. 11: "…al monto que resulte deberá restar el monto de l [sic] impuesto que le fue retenido… En caso no resulte impuesto a pagar, deberá sumarse al crédito que resulte en el siguiente periodo impositivo… sin que el mismo pueda ser objeto de compensación con otro tributo." / 2 años: "…que en un lapso de dos años consecutivos tengan un remanente de crédito fiscal… podrá solicitar… que le aperture una cuenta bancaria especial a su nombre… exclusivamente pagos de otros impuestos" / annex: "…se acompañarán las constancias de retención prenumeradas recibidas o se consignaran detalladamente en el formulario… si la declaración se presenta por medios electrónicos, se detallarán el monto de cada retención, datos de los contribuyentes que le hayan retenido…" / Art. 12 prohibitions (sentenciados no rehabilitados; fallidos o concursados; exportadores no inscritos) / Art. 13: "También podrá activar, desactivar o suspender la calidad de agentes de retención…" / Art. 14: "…estarán sujetos a las sanciones reguladas en el Código Tributario y el Código Penal…" | Arts. 11–14 seller mechanics: subtract retained IVA from period liability, excess rolls forward (never compensable with other taxes except the 2-year special-account route); declaration annexes constancias or itemizes each retention electronically (ancestor of FEL IVA-ret reporting); agent prohibitions; SAT activar/desactivar/suspender faculties; sanctions cite CT + Código Penal generically (no article — citation hygiene) | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.8–10 Arts. 11–14 (EVID-255; D-4-2012 reform notes arts. 12/13) |
| LB-011 | Acuerdo Gubernativo No. 425-2006 (Guatemala, 26 de julio de 2006), Reglamento de la Ley… Fortalecimiento: Art. 1 scope "desarrollar los capítulos I, II y III… Decreto número 20-2006…" / Art. 39: "El presente Reglamento empezará a regir el uno de agosto de dos mil seis…" | AG 425-2006 identity: issued 26-Jul-2006 (within the law's art. 74 30-day mandate), rige 1-Aug-2006 same day as the law's chapters I–III; develops only retenciones (Título II), imprentas (III) and bancarización (IV); retention articles show no reform notes (art. 32 imprentas carries the AG 125-2022 reform — now in corpus as 86_, primary-read: AG 125-2022 art. 25 reforms AG 425-2006 art. 32, vigente 25-nov-2022; see 07/LB-017 + FR-258, EVID-833) | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.1 header + Art. 1; p.16 Arts. 37–39; art. 32 note (EVID-260) |
| LB-012 | AG 425-2006, Arts. 2–5: Art. 2: "9. Período impositivo:… un mes calendario." / "12. Sistema de retenciones de SAT: Sistema informático que permite a los Agentes de Retención elaborar e imprimir las constancias de retención del IVA, así como la declaración jurada de retenciones." / Art. 3: "…designadas por la Ley y activadas por la Administración Tributaria… les extenderá un carné que los identifique como Agentes de Retención." / Art. 4: "…los Agentes de Retención deben ingresar el monto total de cada factura, al Sistema de Retenciones de SAT, el cual determinará el porcentaje de retención a realizar por cada factura, según está definido en la ley para cada tipo de compra y Agente de Retención. El monto de la factura incluirá el Impuesto al Valor Agregado." / "…se deberá excluir del monto total de la factura, dichos impuestos específicos, excepto en las compras de combustibles que se efectúen con tarjeta de crédito o de débito." / Art. 5: 'la cuenta se llamará "IVA - Retenciones por Pagar" y para los proveedores se llamará "IVA -Retenciones por compensar" [sic spacing].' | Reglamento arts. 2–5: período impositivo = calendar month (the R26 key); the Sistema de Retenciones computes the % per factura (agent feeds total incl. IVA; specific non-IVA taxes excluded except fuel-card); carné issued to agents; named ledger accounts both sides | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.2–3 Arts. 2–5 (EVID-261) |
| LB-013 | AG 425-2006, Arts. 6–8: Art. 6 constancia minimum content: "1. Número correlativo… 2. Nombre, razón o denominación social del Agente Retenedor. 3. NIT del Agente Retenedor. 4. Nombre… del contribuyente a quien se le efectuó la retención. 5. NIT del contribuyente… 6. Importe neto del bien o servicio adquirido. 7. Cantidad y número de la (s) [sic] factura (s). 8. Porcentaje de retención aplicado. 9. Monto del impuesto retenido. 10. Código de verificación o autenticación de cada constancia." + "…no es aplicable a las retenciones efectuadas por los operadores de tarjetas…" / Art. 8: "…deben presentar una declaración jurada en forma consolidada… mensualmente aún y cuando no hubiere efectuado retención alguna…" | Reglamento arts. 6–8: constancia = 10 minimum fields (correlativo, both parties' names+NITs, net amount, invoice numbers, %, amount, verification code); operators exempt from art. 6 (art. 20 regime); multi-establishment agents file ONE consolidated monthly DJ, even at zero | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.4–5 Arts. 6–8 (EVID-262) |
| LB-014 | AG 425-2006, Arts. 11–15: Art. 11: "…deben abstenerse de practicar la respectiva retención; para el efecto, el vendedor… deberá acreditar… por medio del respectivo carné… consultando la página Web de la SAT…" / Art. 12: "…a partir del período impositivo… inmediato siguiente de recibida ésta, proceda a efectuar las retenciones…" + "La SAT publicará en su página Web… una lista de los Agentes de Retención… que se encuentren activos." / Art. 13 (suspensión): "…a partir del día hábil siguiente…", solo "declaraciones… pendientes… así como las rectificaciones", "debe devolver… el carné" / Art. 15: SAT "resolverá en un plazo de treinta (30) días hábiles"; cuenta "de giros restringidos"; deposit "dentro de un plazo máximo de diez (10) días hábiles"; "giro… el pago exclusivo de impuestos, multas e intereses." | Reglamento arts. 11–15 lifecycle: between-agents abstention verified via carné + SAT Web list; activation by notification effective the NEXT monthly período; suspension operative the next día hábil, suspended agents may only file pending declarations/rectifications and must return the carné; 2-year remanente → devolución: 30 dh resolution + 10 dh deposit into a restricted account spendable only on taxes/fines/interest | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.6–8 Arts. 11–15 (EVID-263) |
| LB-015 | AG 425-2006, Arts. 16–19: Art. 17: "…tomará el valor total, libre a bordo (FOB por sus siglas en inglés) de las exportaciones realizadas durante el año calendario inmediato anterior." / Art. 18: "…utilizará de base el Registro de Exportadores existente, tomando en cuenta como mínimo…: 1. Que esté debidamente actualizado ante el Registro Tributario Unificado. 2. Que sea usuario del sistema BancaSAT. 3. El cumplimiento de sus obligaciones tributarias. 4. El total de sus exportaciones anuales y el promedio mensual…" | Reglamento arts. 16–19 exporters: Q100,000 monthly average = total FOB exports of the PRIOR calendar year ÷ 12; activation de oficio off the Registro de Exportadores with 4 minimum prerequisites (RTU current, BancaSAT user, compliance, export totals); named cuentas to evidence retentions | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.8–9 Arts. 16–19 (EVID-264) |
| LB-016 | AG 425-2006, Arts. 20–25: Art. 20: operators' "constancia consolidada mensual… además de los requisitos… artículo 6…, debe contener el detalle de las liquidaciones…" / Art. 21: exempt card ops — "implementarán los mecanismos necesarios para identificar la transacción, a efecto que no se realice la retención." / Art. 22: "operadores que sean también especiales [retienen] bajo ambas calidades" / Art. 23: card payment → "la misma estará a cargo de los Operadores" / Art. 24: "únicamente procederán a retener a sus afiliados el uno punto cinco por ciento (1.5%) sobre el valor total de la compra pagada con tarjeta…" / Art. 25: "Si la Administración Tributaria no emite la resolución… dentro del plazo…, la misma se tendrá por resuelta en forma desfavorable…" | Reglamento arts. 20–25: operator constancia = art. 6's 10 fields PLUS per-liquidación detail; exempt/unaffect card transactions pre-identified so no retention; operators with a second quality retain under both; card purchases retained only by the operator; fuel 1.5% mirror; voluntary-agent silence = negative resolution (appeal opens); NO form number anywhere (grep-verified) | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.9–11 Arts. 20–25 (EVID-265) |
| LB-017 | AG 425-2006, Art. 9 (verified in-corpus from the 79_ text layer, GOQ-118): "ARTICULO 9. Dualidad de calidades como agentes de retención. Cuando los contribuyentes estén comprendidos en más de uno de los grupos establecidos en la Ley, para ser Agentes de Retención, deben hacer las retenciones por cada una de las actividades en las que la SAT lo haya activado como Agente de Retención y en los porcentajes que indica la Ley." / Art. 10 (crédito): constancia "en el momento de recibir la factura" + "El importe a retener…, se determinará ingresando el valor de cada factura al sistema de retenciones de la SAT…" | Reglamento art. 9 = the multi-group rule (dualidad): retain under EACH activated quality at the law's percentages — the article the 64_ criterio cites as "artículo 9"; art. 4 (LB-012) is the distinct Sistema-de-Retenciones procedure article. GOQ-118 finding: both citations are correct for their own rules; no conflict (R52 dissolved) | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` + text layer `gt/.extractions/79_Fortalecimiento_Reglamento_AG_425-2006.pdf.txt` | p.7 Art. 9 (txt lines 148–153, verified 2026-08-20); Art. 10 (EVID-262 gloss; 64_ quote EVID-496) |
| LB-018 | Código Tributario (D-6-91 consolidado), Arts. 28, 29 y 41: Art. 28: "Son responsables en calidad de agentes de retención o de percepción, las personas designadas por la ley… Agentes de retención, son sujetos que al pagar o acreditar a los contribuyentes cantidades gravadas, están obligados legalmente a retener de las mismas, una parte de éstas como pago a cuenta de tributos a cargo de dichos contribuyentes." / Art. 29: "Efectuada la retención…, el único responsable ante la Administración Tributaria por el importe retenido o percibido, es el agente…" / Art. 41: mercantile-registry enterprises "deberán retener las cantidades o porcentajes que en cada caso disponga la ley tributaria respectiva…" + opt-out: "…podrá solicitar… que no se efectúe la retención… La Administración Tributaria deberá resolver dentro del plazo de quince días; en caso contrario, la petición se tendrá por resuelta favorablemente." | CT capacity layer: agent status is always designated by the specific law (here D-20-2006); withholding = payment on account of the taxpayer's own tax; once withheld, the agent is sole responsible (solidary until the taxpayer's payment is proven); 15-day constructive-approval opt-out procedure; pairs with CT 40 (no payment facilities for retained amounts, added via D-20-2006 art. 24 — EVID-258) | `gt/sources/25_Codigo_Tributario_6-91.pdf` | arts. 28–29 p.13–14; art. 41 p.23 (EVID-215; EVID-258 EV02d) |
| LB-019 | Reglamento de la Ley del IVA (AG 5-2013, reformado por AG 222-2019), Capítulo IX (Arts. 41–52): Art. 41: "La SAT contará con un registro de los Agentes de Retención a que se refiere el Decreto número 20-2006…" / Art. 43: captions "IVA-Retenciones por Pagar" / "IVA - Retenciones por compensar" / Art. 45: multi-group agents retain "en los porcentajes que indica la Ley" / Art. 47: devolución del remanente "…no ha podido ser compensado con sus débitos fiscales por el lapso de dos (2) años", cuenta de giros restringidos / Art. 49: "…practicarán las retenciones a pequeños contribuyentes, únicamente cuando paguen bienes y servicios cuyo valor sea mayor a dos mil quinientos Quetzales (Q 2,500.00)." / Art. 50: operadoras "constancia de retención consolidada mensual" / Art. 52: card payments by agents → retention "estará a cargo de los Operadores de Tarjeta de Crédito o Débito." | IVA reglamento Chapter IX anchor: the retention SYSTEM (registry, constancias, declarations) is anchored to D-20-2006; no general-regime rate lives in AG 5-2013; pequeño retention floor Q2,500 "mayor a" (exclusive); card-operator consolidation and no-double-retention; 2-year un-compensated remanente refund with restricted account; ledger captions (mirror of AG 425-2006 art. 5). CURRENCY (2026-08-22): the 24_ copy PREDATES AG 125-2022 (vigente 25-Nov-2022) — AG 125-2022 (86_) arts. 10–11 reform AG 5-2013 arts. 48–49: art. 48 gains a second paragraph excepting invoices issued by simplified-regime taxpayers ("De esa obligación de retención se exceptúan las facturas que emitan contribuyentes inscritos bajo los regímenes de [Tributación Simplificada —]"), and reformed art. 49 keys retention on the contribuyente agropecuario brutas-modality to invoices "mayor a dos mil Quinientos quetzales (Q2,500.00)" (EVID-827) — the Q2,500 exclusive boundary survives the reform; current-reglamento citations carry "AG 5-2013, reformado por AG 222-2019 y AG 125-2022" (07/FR-240, EVID-820) | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.20–22 Arts. 41–52 (EVID-185; art. 45 quote also via EVID-496); 86_ arts. 10–11 = `gt/sources/86_AG_125-2022_Reglamento_D7-2019.pdf` p.3 (EVID-827) |
| LB-020 | SAT portal "Sistema Retenciones Web -IVA-" (49_, content as-of ≥ 01-06-2025): "La retención para facturas del Régimen de Pequeño Contribuyente será del (5%) y el monto debe ser mayor o igual a dos mil quinientos quetzales con un centavo (Q 2,500.01)." / "…menores a dos mil quinientos quetzales (Q2,500.00), con excepción del Sector Público, las Operadoras de Tarjeta de Crédito o Débito y adquisición de combustibles pagada con tarjeta…" / "La retención para facturas del Régimen Especial de Contribuyente Agropecuario será del (5%)… La retención será aplicada al monto total de la factura." / rate list: "Exportador (Decreto 29-89) con Dualidad: 15%, 65%" / "Exportador Habitual con Dualidad: 15%, 15%, 65%" / forms: "…formulario SAT-2340… dentro de los primeros quince (15) días hábiles…" / "…formulario SAT-2320… Agropecuario… dentro de los primeros diez (10) días hábiles…" | RetWeb portal print (SECONDARY for statutory parameters): PC-provider invoices 5% when ≥ Q2,500.01; agropecuario-regime providers 5% applied to the total factura (processed in Retenciones Web); Q2,500 de minimis with sector-público/operator/fuel exceptions; dualidad multi-rate prints; declaration forms SAT-2340 (General + PC, 15 dh) and SAT-2320 (agropecuario, 10 dh) with boleta SAT 2000 — the 10-día agro variant's instrument is NOT in the corpus (GOQ-01-context note, R47) | `gt/sources/49_SAT_RetWebIVA_page.html` | p.1 lines 30–48, 33–40 (EVID-389, EVID-390, EVID-391) |
| LB-021 | SAT Manual "Sistema Retenciones Web… Usuarios manuales — Sector público" (52_, portal date 29-11-2024): rate table "según régimen de afiliación del IVA del proveedor…: General 25% / Pequeño Contribuyente 5% / Especial de Contribuyente Agropecuario 5%" / statutory agents: "…aplica únicamente para los Agentes de Retención establecidos en el primer párrafo del artículo 54 B del Decreto Número 27-92…, que llevan contabilidad completa y no han sido calificados por la Administración Tributaria como Agentes de Retención… actúan como Agentes de Retención cuando paguen, acreditan en cuenta ingresos a contribuyentes inscritos en el Régimen Especial de Contribuyente Agropecuario." / line model + "NOTA: el monto de retención se deriva de la aplicación del porcentaje según el tipo de Agente de Retención y el régimen del proveedor… validación de retención entre agentes, montos mínimos, montos exentos o no afectos. Si la factura… fuere emitida en moneda distinta a Quetzal (Q), el cálculo… al tipo de cambio publicado por el Banco de Guatemala con base a la fecha de certificación de la factura." / card: "3.1.1 Pago Total — …la factura ya no estará disponible en la opción de emisión de constancia…" / "3.1.2 Pago Parcial — …con el valor que no fue pagado con tarjeta, toda vez supere el monto mínimo…" / constancia: "el sistema asigna como fecha de constancia la fecha asignada en el campo Emisión al…" | RetWeb IVA manual (SECONDARY for statutory parameters, primary for mechanics): sector público retains by provider regime 25/5/5; the statutory-agent path — D-27-92 art. "54 B" [printed as such; presumably 54 BIS, rides GOQ-01/R59]: full-accounting entities not SAT-qualified retain only when paying agropecuario-regime suppliers (NIT login, RetenIVA2 credentials for active agents); retention-line model with per-regime base semantics and agent/minimum/exempt validations; FX = Banguat rate at the factura's certification date; card Pago Total drops the invoice from the retention pool, Pago Parcial leaves the non-card residual subject to the minimum; IVA constancia date = the agent-chosen "Emisión al" date (vs ISR = invoice date — R54 asymmetry) | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` | p.2–3 rate table + §1; pp.9–10 §3 + NOTA; pp.10–12 §3.1; pp.12–15 (EVID-407, EVID-408, EVID-410, EVID-411, EVID-412) |
| LB-022 | Criterio Tributario Institucional 2-2019 (64_, approved 25-mar-2019, interpretive layer only): Criterio 1: "…el contribuyente especial, además, es exportador habitual, debe retener el 65%… En las compras… no detallados anteriormente… el 15%… Cuando este tipo de exportador [D.29-89] sea, además, contribuyente especial, deberá, retener el 15%…" / AG 5-2013 art. 45: "Cuando los contribuyentes estén comprendidos en más de uno de los grupos…, deben hacer las retenciones por cada una de las actividades… y en los porcentajes que indica la Ley." / AG 425-2006 art. 4 quote (Sistema) + "…tomando en consideración los casos en que existe diferentes tipos de productos en la misma factura, se podrá realizar el prorrateo correspondiente." / criterio's own table: "Exportador habitual 65%… 15%… / Exportadores… 29-89 65%… / Sector público 25%… superiores a Q30,000.00 / Emisores de tarjeta de crédito 15%… / …1.5%… combustibles… / Contribuyentes especiales 15% / Otros agentes 15%", introduced "El Decreto número 20-2008 [sic]" | SAT institutional criterion confirming (never re-deriving) the statutory matrix: dualidad holdings (criterios 1–3) — multi-quality agents retain under each activated quality at the per-activity statutory rate; operative % per factura resolved by SAT's Sistema de Retenciones with prorrateo for mixed-product invoices; the criterio's confirming rate table carries the "20-2008" [sic] defect (R50) and cites AG 425-2006 "artículo 9" for the multi-group rule — verified correct (LB-017, GOQ-118) | `gt/sources/64_SAT_Criterio_2-2019.pdf` | pp.3, 7, 10–13 (EVID-493, EVID-494, EVID-495, EVID-496) |
| LB-023 | SAT "LISTADO DE AGENTES DE RETENCIÓN DEL IVA AL 01/10/2025" (53_): title line + columns "No. NIT NOMBRE FECHA INICIO", last row "8447"; / Formulario "SAT- 0261" (54_): "SOLICITUD DE INSCRIPCIÓN COMO AGENTE DE RETENCIÓN DEL IVA" — ""Otros Agentes de Retención" (Art.6. Disposiciones Legales para el Fortalecimiento…)" | Official agent roster as-of 2025-10-01: 8,447 numbered agents (NIT, name, per-agent FECHA INICIO; range 1/09/2006…1/07/2025), NO agent-type column (cannot seed exportador/especial/público/otros distinctions) and 25 OCR-concatenated rows (verify before seeding); SAT-0261 = the voluntary-inscription form under D-20-2006 art. 6 (motive + declarations) | `gt/sources/53_SAT_Agentes_RetIVA_2025-10-01.pdf`; `gt/sources/54_SAT-0261_form.pdf` | 53_ p.1 title + p.127; 54_ p.1 (EVID-413, EVID-414, EVID-415) |

## 3. Functional Requirements

### 3.1 Instruments & rate-base contract

- **GT-TAX-FR-069:** The IVA retention regime shall be recorded as resting
  solely on **D-20-2006 Capítulo I (arts. 1–14)** + **AG 425-2006 Título II
  (arts. 2–25)**, both vigente 2006-08-01 (dated instrument rows:
  D-20-2006 given 2006-06-06, sanctioned 2006-06-20; AG 425-2006 issued
  2006-07-26), and the string "resolución 2-2010" shall never appear as a
  regime basis anywhere in seeded data (myth rejected — R23; art. 74
  reglamento mandate fulfilled 26-Jul-2006; art. 75 gave SAT a 6-month
  progressive-implementation window from 1-Aug-2006). (LB-001; LB-011;
  EVID-246, EVID-256, EVID-260)
- **GT-TAX-FR-070:** Every retention rate shall be computed as a
  percentage **of the IVA itself** ("de dicho impuesto… incluido en el
  monto total de cada factura / facturado / en el precio de venta"), never
  of the base imponible — with exactly ONE statutory base exception:
  fuel paid by card at 1.5% **sobre el valor total de la transacción**
  (FR-077). A guard shall reject any retention computation that applies a
  %-of-IVA rate to a non-IVA base or the fuel 1.5% to the IVA amount.
  (LB-002, LB-004, LB-005, LB-006; EVID-247, EVID-249, EVID-250,
  EVID-251)

### 3.2 Statutory agent classes & rate matrix (D-20-2006 arts. 1–6)

- **GT-TAX-FR-071:** Exporter-agent calificación shall require all three:
  inscription before SAT as *exportador habitual*, monthly average exports
  ≥ Q.100,000.00 — computed as the total FOB value of the prior calendar
  year's exports averaged monthly (reglamento art. 17) — and SAT's aviso
  of activation (de oficio, off the Registro de Exportadores, with the
  four art. 18 prerequisites: RTU current, BancaSAT user, tax compliance,
  export totals); activation is effective from the período impositivo
  immediately following notification (reglamento art. 12). Stored as
  dated rows. (LB-002; LB-015; LB-014; EVID-247, EVID-264, EVID-263)
- **GT-TAX-FR-072:** Exporter rates shall be stored as dated rows
  (valid_from 2006-08-01, instrument "D-20-2006 art. 1"): **65%** of the
  IVA on agricultural/livestock products (enumerated list: café in any
  form except toasted or soluble, unrefined cane sugar, banana, cardamomo
  in any state, sugar cane, cotton, milk + open class "otros productos
  agropecuarios" — classification concern, open list), **15%** of the IVA
  on all other goods and services, **65%** of the IVA for D.29-89
  enterprises (buying for export). (LB-002; EVID-247; EVID-493
  interpretive confirmation)
- **GT-TAX-FR-073:** The exporter-only credit exception shall be
  implemented: the totality of IVA retained by an exporter agent is
  **compensable against its refundable crédito fiscal** (the sole
  exception to the FR-093 neutrality rule); exporter enterar deadline =
  15 días hábiles following the período impositivo (same window as
  FR-105 per R26). (LB-003; EVID-248)
- **GT-TAX-FR-074:** Sector-público agents by law (Organismos del Estado,
  entidades descentralizadas, autónomas y semi-autónomas and their
  enterprises) shall retain **25% of the IVA** in the total facturado;
  **municipalidades are excepted — never agents under art. 2**; credit
  operations retain at the moment of the CURE (*Comprobante Único de
  Registro de Egresos*) payment request; failure to enter retained tax
  triggers the penal-denuncia hook for the responsible public officials.
  (LB-004; EVID-249)
- **GT-TAX-FR-075:** The sector-público abstention floor shall be a dated
  row: abstain when the operation is **inferior a Q.30,000.00** (art. 2
  ¶4, wording as reformed by D-4-2012 art. 24 on 25-02-2012 — the
  pre-2012 paragraph is not in the corpus; historical rows requiring it
  are blocked pending GOQ-65). (LB-004; EVID-249; GOQ-65 → OQ-002)
- **GT-TAX-FR-076:** Card operators (credit/debit) shall retain **15% of
  the IVA** included in the sale price, measured per the amount expressed
  in the voucher of purchase; the affiliated merchant remains liable to
  the fisco for the **85% not retained**; the operator's constancia is
  monthly-consolidated (FR-099); and card-paid purchases are retained
  ONLY by the operator (**exclusivity** — every other agent abstains;
  reinforced by arts. 9 ¶2 and reglamento art. 23). (LB-005; LB-009;
  LB-016; EVID-250, EVID-254, EVID-265)
- **GT-TAX-FR-077:** Fuel acquired by credit/debit card shall be retained
  at **1.5% of the total transaction value** — the sole base exception
  (FR-070) — with the base including the petroleum-distribution tax
  whenever it is in the sale price, and the withheld amount applied
  against the IVA of the fuel sale (mirror: reglamento art. 24; rides the
  art. 3 operator cycle). The petroleum-tax regime itself is outside the
  corpus and post-2006 base changes unverifiable (GOQ-67). (LB-006;
  LB-016; EVID-251, EVID-265; GOQ-67 → OQ-004)
- **GT-TAX-FR-078:** Contribuyentes especiales shall be modeled as agents
  at **15% of the IVA** (85/15 split) from the moment SAT notifies their
  activation; the calificación itself is SAT's own normativa (criteria
  not in these instruments — external, never hard-coded), activation
  effective the next período impositivo. (LB-007; LB-014; EVID-252,
  EVID-263)
- **GT-TAX-FR-079:** Otros agentes shall be modeled at **15% of the IVA**
  through two channels: voluntary application (SAT resolves within 30 días
  hábiles from the day after filing; **silence = resolved unfavorably**
  per reglamento art. 25, opening the next administrative instance) and
  SAT's open-ended designation of "las personas… que estime pertinente";
  the inscription instrument is form SAT-0261 (art. 6 hook; form identity
  owned by the RetWeb/F-wave layer — R46). (LB-007; LB-016; LB-023;
  EVID-252, EVID-265, EVID-415)

### 3.3 R55 secondary-print additions (GOQ-06 — never frozen)

- **GT-TAX-FR-080:** Retention on invoices of *pequeño contribuyente*
  suppliers shall be a dated row at **5%** applied only when the invoice
  amount is **≥ Q2,500.01** (exclusive boundary — same as the statutory
  "mayor a Q2,500.00" floor, GT-TAX-FR-057), recorded as **secondary
  print — statutory text pending GOQ-01/06, never frozen**: the rate is
  printed by the RetWeb portal (49_, as-of ≥ 2025-06-01) and the
  sector-público manual (52_, 2024-11-29) but its statutory instrument
  (LIVA art. 54-bis / D-27-92 text) is not in the corpus. The 5% on
  pequeño invoices is a **pago definitivo at the 5% tarifa** whose
  pequeño-side track is owned by Task 2 (GT-TAX-FR-056..058) — this file
  owns only the agent-side rate row. (LB-020; LB-021; EVID-391, EVID-407;
  GOQ-06 → OQ-001; cross-ref GT-TAX-FR-057)
- **GT-TAX-FR-081:** Retention on invoices of *Régimen Especial de
  Contribuyente Agropecuario* suppliers shall be a dated row at **5%
  applied to the monto total de la factura** (invoice carries no
  separable IVA), processed through Retenciones Web (Agencia Virtual)
  per the portal print; recorded as **secondary print — statutory text
  pending GOQ-01/06, never frozen** (49_/52_ prints; statutory basis =
  LIVA art. 54-bis territory). (LB-020; LB-021; EVID-391, EVID-407;
  GOQ-06 → OQ-001)
- **GT-TAX-FR-082:** The sector-público rate shall resolve by **provider
  IVA regime** as printed by 52_: General 25% (statutory, art. 2) /
  Pequeño Contribuyente 5% / Especial de Contribuyente Agropecuario 5% —
  the 5/5 rows recorded as **secondary print — statutory text pending
  GOQ-01/06, never frozen**. The interplay between the art. 2 Q.30,000
  abstention floor and the 5% provider-regime rows (which floor applies
  to pequeño/agro providers of a sector-público agent) is not stated in
  any instrument — flag only, resolved by configuration, never hard-coded
  (GOQ-66 discipline). (LB-021; LB-020; EVID-407, EVID-391; GOQ-06 →
  OQ-001; GOQ-66 → OQ-003)
- **GT-TAX-FR-083:** The statutory-agent subtype shall be modeled per the
  52_ print: entities under **D-27-92 art. "54 B" [printed as such;
  presumably 54 BIS — nomenclature rides GOQ-01 (R59)] first paragraph**,
  carrying full accounting and NOT SAT-calified, act as retention agents
  only when paying or accrediting income to **agropecuario-regime**
  suppliers (system access by plain NIT; active agentes retenedores use
  RetenIVA2 credentials); recorded as **secondary print — statutory text
  pending GOQ-01/06, never frozen** (the art. 54 BIS body text is absent
  from the corpus law copy). (LB-021; EVID-408; GOQ-01 → OQ-007; R59)

### 3.4 Dualidad & the Sistema de Retenciones (GOQ-118/GOQ-119)

- **GT-TAX-FR-084:** The retention configuration shall support **multiple
  simultaneous agent qualities** (*dualidad*): a taxpayer activated under
  more than one group retains **under EACH activated quality
  separately**, at the per-activity statutory rate of each quality —
  AG 425-2006 **art. 9** "Dualidad de calidades como agentes de
  retención" (verified in-corpus from the 79_ text layer: the 64_
  criterio's "artículo 9" citation is CORRECT; R52 tension dissolved —
  GOQ-118, OQ-005), mirrored by AG 5-2013 art. 45 and held in Criterio
  2-2019 (an operator that is also especial retains under both
  qualities, reglamento art. 22). The operative quality set per taxpayer
  is SAT-activation-driven dated data, never hard-coded. Same-invoice
  co-application of two qualities is not reconciled in the sources —
  modeled per FR-085 only (GOQ-119 → OQ-006). (LB-017; LB-019; LB-022;
  LB-016; EVID-496, EVID-185, EVID-265)
- **GT-TAX-FR-085:** The operative retention percentage per factura shall
  resolve as SAT's **Sistema de Retenciones** does (AG 425-2006 art. 4,
  saas-side configuration service): the agent feeds the **total invoice
  amount including IVA** (minus specific non-IVA taxes, except
  fuel-by-card), and the system determines the percentage per law-defined
  agent/purchase type — rates are never user-picked. For
  mixed-product invoices (e.g. agro + other goods) the system shall
  support **prorrateo** (proration) of the invoice amount across product
  classes ("se podrá realizar el prorrateo correspondiente", Criterio
  2-2019 analysis); the rate matrix itself is configuration-driven dated
  data (CSV sidecar), not hard-coded (GOQ-119 modeling call).
  (LB-012; LB-022; EVID-261, EVID-496)

### 3.5 Thresholds & abstentions

- **GT-TAX-FR-086:** The de-minimis guard shall be a dated row: agents of
  arts. 1/5/6 do NOT retain when the service or purchase is **"menores a"
  (strictly below) Q.2,500.00** per operation — the boundary value itself
  (exactly Q.2,500.00 general-regime) is a textual edge flagged for
  product-side testing, while the pequeño-provider boundary is ≥
  Q.2,500.01 (FR-080); EXCEPTED from the Q2,500 rule: sector público
  (art. 2, Q.30,000 floor), card operators (art. 3) and fuel-by-card
  (art. 4). (LB-009; LB-020; EVID-254, EVID-391)
- **GT-TAX-FR-087:** No retention shall be applied when buyer and seller
  are BOTH active retention agents; the buyer-side check shall verify the
  seller's agent status via the carné **and** the SAT Web active-agent
  list (reglamento art. 11 — the counterpart lookup the product must
  support); card payments escape the abstention (arts. 3/4 operator
  retention applies). (LB-009; LB-014; EVID-254, EVID-263)
- **GT-TAX-FR-088:** Card-settlement mechanics shall follow the RetWeb
  print (EV04b, secondary layer — mechanics primary): **Pago Total** —
  the card-paid invoice leaves the retention pool entirely (no constancia
  emission; the card voucher documents the factura) and the operator
  retains instead (FR-076); **Pago Parcial [sic mechanics as printed]** —
  the non-card residual remains subject to retention **iff it exceeds
  the applicable minimum**. Mixed card/invoice settlements therefore
  split the retention base. (LB-021; EVID-411; GOQ-06 → OQ-001)
- **GT-TAX-FR-089:** Exempt or unaffected card transactions (cardholder
  or affiliate exempt per IVA art. 8) shall be pre-identified so that no
  retention is performed on them (operator + affiliate mechanisms,
  reglamento art. 21). (LB-016; EVID-265)
- **GT-TAX-FR-090:** The Q.30,000 pairing (art. 2 abstention floor vs
  art. 20 bancarización threshold vs art. 10 Q2,500) shall be recorded as
  a **flag only** — the interplay is not stated in any instrument and the
  values shall never be modeled as linked (GOQ-66; bancarización itself
  is owned by `01_iva-core.md`-adjacent deduction rules, not this file).
  (LB-004; LB-009; EVID-249, EVID-254; GOQ-66 → OQ-003)

### 3.6 Retention computation, bases & neutrality

- **GT-TAX-FR-091:** The retention computation base shall be the total
  factura amount **including IVA**, minus specific taxes that the law
  excludes from the IVA base — except fuel-by-card, whose 1.5% base
  INCLUDES the specific petroleum tax; retention ledger accounts shall be
  seeded with the statutory captions **"IVA - Retenciones por Pagar"**
  (agent side) / **"IVA - Retenciones por compensar"** (provider side;
  reglamento art. 5, mirrored AG 5-2013 art. 43; exporters open both to
  trace retention vs. refundable credit). (LB-012; LB-019; EVID-261,
  EVID-185)
- **GT-TAX-FR-092:** Retention timing shall be: cash operations — the
  constancia is issued when the seller delivers the factura; credit
  operations — at "el momento de la entrega y emisión de la factura"
  (arts. 1/5) or at the CURE payment request (art. 2), and per reglamento
  art. 10 the constancia is emitted at invoice receipt regardless of
  installment terms, with the retention amount determined by feeding each
  factura to the Sistema de Retenciones. (LB-004; LB-017; LB-020;
  EVID-249, EVID-388, EVID-262)
- **GT-TAX-FR-093:** Retained IVA shall be **fiscally neutral to the
  agent**: it is neither débito nor crédito fiscal, and may not be
  compensated with other tributes — sole exception: art. 1 exporters
  (FR-073); the agent is solidarily responsible with the taxpayer if it
  failed to retain, and (CT layer) once retained, the agent is sole
  responsible for entering, with no payment facilities ever available for
  retained amounts (CT 40 as reformed by D-20-2006 art. 24).
  (LB-008; LB-018; EVID-253, EVID-215, EVID-258)
- **GT-TAX-FR-094:** For invoices issued in a currency other than
  quetzales, the retention shall be computed from the quetzal amount at
  the Banco de Guatemala exchange rate of the factura's **fecha de
  certificación** (RetWeb print — mechanics layer, F2 cross-ref).
  (LB-021; EVID-410)

### 3.7 Seller-side mechanics (the retained taxpayer)

- **GT-TAX-FR-095:** The seller shall book the suffered retention in the
  **same período impositivo** in which the invoice is declared (art. 8);
  monthly determination shall **subtract the retained IVA** from the
  period's tax; if no tax results, the retention adds to the next
  period's credit and rolls forward successively — never compensable
  with other tributes (cross-ref GT-TAX-FR-025 for the crédito-side
  chassis owned by Task 1). (LB-009; LB-010; EVID-254, EVID-255)
- **GT-TAX-FR-096:** The 2-year stranded-remanente track shall be
  implemented as dated rows: when a crédito remanente remains
  un-compensable against débitos for **two consecutive years**, the
  taxpayer may request a special restricted bank account (SAT resolves
  in 30 días hábiles; deposit within 10 días hábiles; "de giros
  restringidos" — spendable exclusively on taxes, fines and interest;
  reglamento art. 15, mirrored AG 5-2013 art. 47). (LB-010; LB-014;
  LB-019; EVID-255, EVID-263, EVID-185)
- **GT-TAX-FR-097:** The seller's IVA declaration shall annex the
  received prenumerada constancias, or itemize them in the SAT-provided
  formulario; **electronic declarations must detail each retention**
  (amount, retaining taxpayers' data, amounts retained) — the statutory
  ancestor of per-document IVA-retention reporting; FEL FESP
  "Retenciones de factura especial" field mapping is owned by the
  e-invoicing wave (GT-EINV-FR-036) and the FESP retention semantics by
  Task 5, whose statutory cross-lock anchor is 05_'s LB-021 (Ley IVA
  Arts. 52/52"A" verbatim, EVID-177) — cross-referenced, never
  re-derived here. (LB-010; EVID-255)

### 3.8 Constancia de retención (document model)

- **GT-TAX-FR-098:** The constancia shall be a **prenumerada y
  autorizada** document (correlative numbering) carrying the 10 minimum
  fields of reglamento art. 6: 1 correlativo number; 2 agent name/razón
  social; 3 agent NIT; 4 retained taxpayer name/razón social; 5 retained
  taxpayer NIT; 6 net amount of the good/service; 7 quantity and
  invoice number(s); 8 retention percentage applied; 9 retained tax
  amount; 10 **código de verificación o autenticación** — issued per
  operation OR consolidated monthly for the same provider in the same
  calendar month (operators always monthly, FR-099); art. 7.4 field set
  {nombre/razón social, NIT, importe neto, %, monto retenido, no.
  factura/transacción} is the law-level subset. (LB-008; LB-013;
  EVID-253, EVID-262)
- **GT-TAX-FR-099:** The operator constancia shall be **monthly and
  consolidated** (exempt from the art. 6 per-operation shape via art. 20):
  the art. 6 ten fields PLUS the detail of the liquidaciones subject to
  retention in the same calendar month. (LB-016; EVID-265, EVID-250)
- **GT-TAX-FR-100:** RetWeb constancia semantics (secondary print,
  mechanics layer) shall be supported: document date = the agent-chosen
  **"Emisión al"** search date (vs the ISR constancia dated with the
  factura date — intentional asymmetry, keep both rules, R54); grouping =
  one constancia per retained contribuyente per emission batch, carrying
  the count and detail of bundled facturas. (LB-021; EVID-412)

### 3.9 Agent lifecycle, capacity & registry

- **GT-TAX-FR-101:** Agent status shall be SAT-registry-driven dated
  data: **activation** by notification, effective from the período
  impositivo immediately following receipt (reglamento arts. 12/25);
  **carné** issued as the physical evidence; SAT publishes the **Web
  list of active agents** (the FR-087 lookup counterpart);
  **suspension/inactivación** effective the día hábil following
  notification — the suspended agent may only file pending declarations
  and rectifications of erroneous retentions, and must return the carné;
  SAT may activar/desactivar/suspender at any time (art. 13). Agent-type
  classification (exportador/especial/público/otros) is NOT available
  from the roster source (53_ has no category column) — it comes from
  SAT calificación data, never guessed. (LB-014; LB-023; EVID-263,
  EVID-413)
- **GT-TAX-FR-102:** Agent eligibility shall exclude: persons sentenced
  for patrimonial or tax-regime crimes while unrehabilitated;
  fallidos/concursados while unrehabilitated; exporters not inscribed in
  the art. 1 registro de exportadores (art. 12; D-4-2012 wording of the
  suspension mechanics). (LB-010; EVID-255; GOQ-65 → OQ-002)
- **GT-TAX-FR-103:** Agents retaining at more than one establishment
  shall request prior authorization (written or electronic via the
  SAT-provided formulario, reglamento art. 7) and shall file **one
  consolidated declaración jurada** across all authorized establishments
  (reglamento art. 8; multi-branch exporter cuentas per art. 19).
  (LB-013; LB-015; EVID-262, EVID-264)
- **GT-TAX-FR-104:** The CT capacity layer shall frame all of the above:
  agent status is always designated by law (CT art. 28 — withholding is
  payment on account of the taxpayer's own tax); once effected, the agent
  is sole responsible before the Administration (CT art. 29, solidarity
  unless the taxpayer's payment is proven); registered mercantile
  enterprises must retain per the specific law (CT art. 41) with the
  15-day constructive-approval no-retention opt-out; sanctions for
  non-entering cite CT + Código Penal generically (art. 14 — no article
  numbers, citation hygiene; specific sanction rows owned by Task 6).
  (LB-010; LB-018; EVID-255, EVID-215)

### 3.10 Declaration, enterar & deadlines

- **GT-TAX-FR-105:** The agent declaration chassis shall be: monthly
  **declaración jurada with the totality of the retained tax**, per-provider
  fields {NIT, nombre/denominación/razón social, porcentaje de retención,
  valor retenido, fecha de cada retención}, due within the **primeros 15
  días hábiles del mes inmediato siguiente** to the retention month,
  **mandatory even at zero retentions**; the retained tax is entered in
  full alongside (declaration/enterar FORM generation is owned by the
  F2-wave RetWeb files — cross-referenced, never re-derived). (LB-008;
  LB-013; EVID-253, EVID-262)
- **GT-TAX-FR-106:** The two statutory deadline phrasings shall be
  recorded as ONE window (R26): art. 1 exporters "quince (15) días
  hábiles siguientes al período impositivo" = arts. 2/3/5/6/7 "primeros
  quince (15) días hábiles del mes inmediato siguiente", because
  período impositivo = mes calendario (reglamento art. 2 num. 9) —
  wording choice is citation-precision only; the deadline is a dated
  row, never a constant. (LB-003; LB-004; LB-008; LB-012; EVID-248,
  EVID-249, EVID-253, EVID-261)
- **GT-TAX-FR-107:** Form identities shall be owned by the RetWeb layer
  (R46 — form numbers NEVER cite D-20-2006/AG 425-2006, which print
  none): per the portal print, **SAT-2340** serves General + Pequeño
  Contribuyente provider invoices (15 días hábiles) and **SAT-2320**
  serves Régimen Especial de Contribuyente Agropecuario (10 días
  hábiles), both paid via boleta SAT 2000 (bank/Bancasat, Declaraguate).
  The statutory layer owns only the uniform 15-días-hábiles window
  (FR-105/FR-106, R26); the **SAT-2320 10-día variant is a RetWeb-layer
  printed value whose instrument is NOT in the corpus** — recorded as a
  GOQ-01-context note (R47 deferral answer), never as a new GOQ and
  never frozen. (LB-020; EVID-389; R26, R46, R47; GOQ-01 → OQ-007)
- **GT-TAX-FR-108:** Agent master-data seeding shall use the official
  roster (53_, as-of 2025-10-01): 8,447 numbered agents with per-agent
  NIT + FECHA INICIO (dated seed, range 2006-09-01…2025-07-01), treated
  as seed data only — 25 rows carry OCR NIT/name/date concatenation
  defects (verify against checksum/RTU on import) and the roster carries
  NO agent-type column; voluntary inscriptions carry the SAT-0261
  record (motive + declarations, art. 6 hook). (LB-023; EVID-413,
  EVID-414, EVID-415)
- **GT-TAX-FR-109:** The agent shall keep the **registro auxiliar** (full
  detail of retentions effected, art. 7.3) in accounting, anchored with
  the AG 5-2013 Chapter IX registry (art. 41) — the ledger surface the
  declaration chassis (FR-105) reads; electronic-books surfaces are
  owned by the F-wave (cross-ref). (LB-008; LB-019; EVID-253, EVID-185)
- **GT-TAX-FR-110:** Edge-notes guard row (GOQ-67): (a) the art. 4 fuel
  base includes the *Impuesto a la Distribución del Petróleo Crudo y
  Combustibles Derivados* — that tax's own regime and any post-2006 base
  composition change are outside the corpus: the 1.5% row stays
  decree-bound and unverifiable for drift; (b) D-20-2006 contains **NO
  IVA-retention rule for imports** nor for hydrocarbon producers outside
  the card scheme (retentions attach to compras/adquisiciones from
  suppliers) — the system shall never assert an import-side IVA
  retention without external verification. (LB-006; EVID-251; GOQ-67 →
  OQ-004)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance + as-of qualifier; snapshot-on-write; rate/threshold/deadline
rows are decree-bound, never constants; rows sourced from
EV04b prints carry `status = secondary-print-pending` and are never frozen
(GOQ-06). The rate matrix ships as the machine-readable sidecar
`iva_retention_rates.csv` (one row per agent class × rate × base
qualifier).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.iva.retention.rate | agent_class / provider_context / rate_pct / base_qualifier | selection / selection / decimal / selection | exportador_habitual 65 (agro list) & 15 (otros); exportador_D29-89 65; sector_publico 25; operadora_tarjeta 15; operadora_tarjeta_fuel 1.5 (valor_total_transaccion — sole base exception); contribuyente_especial 15; otros_agente 15; SECONDARY: sector_publico 5 (pequeño) & 5 (agropecuario); agentes 5 (pequeño ≥ Q2,500.01) & 5 (agropecuario total factura); dualidad combos | FR-070..082; CSV sidecar |
| l10n_gt.iva.retention.rate | valid_from / valid_to / instrument / source_evid / status | date / date / char / char / selection | statutory rows 2006-08-01 "D-20-2006 art. N" [statutory]; EV04b rows as-of 2024-11-29 / 2025-06-01 "49_/52_ print" [secondary-print-pending] | FR-080..082; GOQ-06 |
| l10n_gt.iva.retention.agent | agent_class[] / status / fecha_inicio / carne_no | m2o→rate classes / selection activo-suspendido-inactivo / date / char | multiple simultaneous classes (dualidad); SAT-activation-driven; carné returned on suspension | FR-084, FR-101 |
| l10n_gt.iva.retention.deminimis | threshold / operator / scope | decimal / selection <,≥ / char | Q2,500.00 exclusive arts. 1/5/6 ("menores a" boundary flag); Q30,000.00 sector público (D-4-2012 wording; GOQ-65); Q2,500.01 pequeño-provider floor; exceptions: sector público, operadoras, fuel-card | FR-075, FR-086, FR-080 |
| l10n_gt.iva.retention.dualidad | quality_set / prorrateo | m2m / boolean | per-quality retention at per-activity statutory rates; mixed-invoice prorrateo; % resolution = Sistema de Retenciones model (saas config) | FR-084, FR-085 |
| l10n_gt.iva.retention.constancia | fields 1–10 / granularity / date_rule | char list / selection operacion-mensual_operador / selection | art. 6 ten fields incl. correlativo + código de verificación; operators monthly + liquidaciones detail; date = "Emisión al" (IVA) vs factura date (ISR — R54) | FR-098..100 |
| l10n_gt.iva.retention.declaration | window / even_zero / provider_fields / consolidated | char / boolean / char list / boolean | primeros 15 días hábiles mes siguiente (R26 both phrasings); true; {NIT, nombre, %, valor, fecha}; multi-establishment single DJ | FR-105, FR-106, FR-103 |
| l10n_gt.iva.retention.seller.netting | same_period / subtract / rollforward / two_year_account | boolean ×4 + json | same período as invoice declaration; subtract from liability; roll-forward; 2-year restricted account (30 dh + 10 dh, tax/fine/interest-only) | FR-095, FR-096 |
| l10n_gt.iva.retention.card | exclusivity / pago_total / pago_parcial / exempt_flag | boolean ×4 | card pool exit mechanics (secondary print); exempt-card pre-identification | FR-076, FR-088, FR-089 |
| l10n_gt.iva.retention.guard | key | char | no_2-2010_myth; fuel_base_valor_total_only; no_import_side_retention; q30000_flag_only (GOQ-66); boundary_q2500_edge; roster_no_category | FR-069, FR-070, FR-110, FR-090, FR-086, FR-108 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Taxation
defaults per wave plan: retention-rate matrix + agent-calificación status =
`shared` dated data; retention computation at invoice/payment +
constancia issuance surfaces = `odoo`; DJ/enterar generation = F-wave
cross-ref; Sistema-de-Retenciones % resolution = `saas` config service.
Model names stable across Odoo 17/18/19/20; no version-specific behavior
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-069 | shared | — (guard/config) | instrument dated rows + myth guard | "resolución 2-2010" never seeded; both sides key on the same instrument rows |
| FR-070 | shared | — (config data §4) | rate base contract | %-of-IVA everywhere except fuel 1.5% valor total; guard on both sides |
| FR-071 | shared | — (config data §4) | exporter calificación dated rows | FOB prior-calendar-year averaging; SAT aviso effective next período |
| FR-072 | shared | — (config data §4 + CSV) | exporter rate rows 65/15/65 | Open agro list ("otros productos agropecuarios") = classification config |
| FR-073 | shared | — (config data §4) | exporter credit-exception row | Sole exception to FR-093 neutrality; enterar 15 dh (R26) |
| FR-074 | shared | — (config data §4 + CSV) | sector público 25% row | municipalidades never agents; CURE timing + penal hook recorded |
| FR-075 | shared | — (config data §4) | Q30,000 abstention dated row | D-4-2012 wording; pre-2012 blocked (GOQ-65) |
| FR-076 | shared | — (config data §4 + CSV) | operator 15% + 85% liability rows | Exclusivity contract consumed at odoo invoice/payment level |
| FR-077 | shared | — (config data §4 + CSV) | fuel 1.5% valor-total row | Sole base exception; petroleum-tax inclusion note (GOQ-67) |
| FR-078 | shared | — (config data §4 + CSV) | especiales 15% row | Calificación criteria external; activation-notification dated fact |
| FR-079 | shared | — (config data §4 + CSV) | otros 15% row | 30-dh resolution + negative silence; SAT-0261 surface = F-wave |
| FR-080 | shared | — (config data §4 + CSV) | pequeño 5% ≥ Q2,500.01 row | status=secondary-print-pending (GOQ-06); never frozen; pequeño track = Task 2 |
| FR-081 | shared | — (config data §4 + CSV) | agro 5% total-factura row | status=secondary-print-pending (GOQ-06); RetWeb processing noted |
| FR-082 | shared | — (config data §4 + CSV) | sector público 25/5/5 rows | 5/5 rows secondary-print-pending; floor interplay flag-only (GOQ-66) |
| FR-083 | shared | — (config data §4) | statutory-agent 54 B [54 BIS] row | Nomenclature rides GOQ-01 (R59); NIT-login population recorded |
| FR-084 | shared | — (config data §4) | dualidad quality-set config | Multi-quality per partner; per-activity statutory rates; GOQ-119 |
| FR-085 | saas | % resolution service (Sistema model) | total-incl.-IVA input → % per factura | saas config service mirrors the law matrix; prorrateo for mixed invoices; odoo surfaces line input |
| FR-086 | shared | — (config data §4) | de-minimis dated rows | Q2,500 "menores a" boundary edge flagged; exceptions list |
| FR-087 | odoo | account.move.line / res.partner | agent-status check (carné + Web list) | Abstention enforced at invoice/payment; card exception branch |
| FR-088 | odoo | account.move / account.payment.register | card pago total/parcial split | Secondary-print mechanics (EV04b); residual-over-minimum retains |
| FR-089 | odoo | account.move.line | exempt-card flag | Pre-identification skips retention |
| FR-090 | shared | — (guard) | q30000_flag_only guard | Never modeled as linked (GOQ-66) |
| FR-091 | shared | — (config data §4) | base rules + ledger captions | Captions seeded both sides; fuel-card base exception |
| FR-092 | odoo | account.move / constancia timing | retention moment + constancia emission | Cash/credit/CURE/reglamento art. 10 timing branches |
| FR-093 | shared | — | neutrality contract | No débito/crédito/compensation for agent; exporter exception; CT 40 no-facilities |
| FR-094 | odoo | account.move (currency) | Banguat rate at fecha de certificación | Secondary mechanics print; F2 cross-ref |
| FR-095 | odoo | account.move (seller declaration) | same-period netting + roll-forward | Cross-ref GT-TAX-FR-025 (Task 1 chassis) |
| FR-096 | shared | — (config data §4) | 2-year account dated rows 30/10 dh | Procedure surface odoo-side |
| FR-097 | odoo | account.move (annex) | constancias annex / e-declaration itemization | GT-EINV-FR-036 FESP mapping = e-invoicing wave; FESP semantics = Task 5 |
| FR-098 | odoo | l10n_gt retention constancia model | 10 fields + correlativo + código verificación | Issuance surface odoo; document contract shared via §4 |
| FR-099 | odoo | constancia (operator variant) | monthly consolidated + liquidaciones detail | Art. 20 shape |
| FR-100 | odoo | constancia (date/grouping) | "Emisión al" date + per-supplier batching | R54 asymmetry vs ISR kept; secondary print |
| FR-101 | shared | — (config data §4) + res.partner | lifecycle dated data + agent flag | Activation next período; suspension next día hábil; carné return; roster seed |
| FR-102 | shared | — (guard/config) | prohibition classes | D-4-2012 wording (GOQ-65 historical block) |
| FR-103 | odoo | res.company / multi-branch config | prior authorization + consolidated DJ | Reglamento arts. 7/8 |
| FR-104 | shared | — | CT capacity framing | CT 28/29/41 + CT 40; sanction rows = Task 6 |
| FR-105 | shared | — (config data §4) | DJ chassis dated rows | Even-zero monthly; per-provider fields; form generation = F2-wave |
| FR-106 | shared | — | single-window deadline row (R26) | Wording variance recorded, one window computed |
| FR-107 | shared | — (config data) | form-identity rows SAT-2340/2320 + boleta 2000 | R46/R47: statutory layer owns 15 dh only; agro 10-dh = RetWeb print, instrument not in corpus (GOQ-01 context) |
| FR-108 | shared | — (seed data) | roster seed 8,447 agents as-of 2025-10-01 | No category column; 25 OCR defects; SAT-0261 record |
| FR-109 | odoo | account books / auxiliary registry | registro auxiliar | AG 5-2013 Chapter IX anchor; F-wave owns e-books |
| FR-110 | shared | — (guard) | GOQ-67 edge guards | Fuel-base drift unverifiable; no import-side retention assertion |

## 6. Acceptance Criteria

- **AC-001:** Given the rate catalog, when any statutory rate row is
  resolved, then it is expressed as a % of the IVA included in the factura
  total and only the fuel-card row (1.5% of valor total) uses a non-IVA
  base; a fuel computation against the IVA amount is rejected.
  (FR-070, FR-077)
- **AC-002:** Given an exporter agent's purchase of an enumerated agro
  product (e.g. cardamomo), of another good, and of a D.29-89-firm supply,
  when retentions compute, then 65% / 15% / 65% of the respective IVA
  apply as dated rows valid from 2006-08-01. (FR-072)
- **AC-003:** Given a State-entity purchase ≥ Q.30,000.00 or <
  Q.30,000.00, when retention is attempted, then 25% of IVA applies or the
  agent abstains respectively; given a municipalidad buyer, then it never
  retains as an art. 2 agent. (FR-074, FR-075)
- **AC-004:** Given a card-paid purchase, when retention is resolved,
  then only the operator retains (15% per voucher), the merchant carries
  the 85% non-retained liability, and no buyer-side agent retains on the
  card-settled amount. (FR-076, FR-087, FR-088)
- **AC-005:** Given the de-minimis guard, when an art. 1/5/6 agent's
  operation is below Q.2,500.00 (or a sector-público operation below
  Q.30,000.00), then no retention applies; given a pequeño-provider
  invoice of Q2,500.00, then no 5% retention applies (boundary: ≥
  Q2,500.01 only). (FR-086, FR-080)
- **AC-006:** Given both buyer and seller are active agents, when the
  seller evidences status via carné + SAT Web list, then the buyer
  abstains — except card payments, which route to arts. 3/4.
  (FR-087)
- **AC-007:** Given the EV04b-sourced rows (pequeño 5% ≥ Q2,500.01; agro
  5% total factura; sector-público 5/5 provider split; dualidad combos),
  when inspected, then every one carries
  `status = secondary-print-pending` with its print provenance
  (49_/52_) and none is frozen as a constant (GOQ-06 open).
  (FR-080..082, FR-088)
- **AC-008:** Given a taxpayer activated under two agent qualities, when
  it buys within each quality's activity classes, then it retains under
  EACH quality at that quality's statutory rate, the quality set is
  configuration-driven dated data, and a mixed-product invoice resolves
  through prorrateo per the Sistema-de-Retenciones model — never a
  single hard-coded rate. (FR-084, FR-085)
- **AC-009:** Given a retained seller closing a month, then the suffered
  retention books in the same período as the invoice declaration, the
  liability nets against it, excess rolls forward, and only a 2-year
  stranded remanente opens the restricted-account track (30 dh + 10 dh;
  tax/fine/interest-only spending). (FR-095, FR-096)
- **AC-010:** Given an agent month with zero retentions, when the
  declaration calendar runs, then the even-zero declaración jurada is
  still due within the first 15 días hábiles of the following month with
  the per-provider field set; the art. 1 phrasing resolves to the same
  window (R26); the SAT-2320 agro 10-día variant appears only as a
  RetWeb-layer note, never as a statutory constant. (FR-105, FR-106,
  FR-107)
- **AC-011:** Given a constancia, then it carries the 10 art. 6 fields
  including correlativo numbering and the código de verificación; given an
  operator constancia, then it is monthly, consolidated and adds the
  liquidaciones detail; given several same-provider invoices in one
  month, then one consolidated constancia may bundle them.
  (FR-098, FR-099)
- **AC-012:** Given an agent's activation or suspension notification,
  when dated, then retention duties start the next período impositivo or
  stop the next día hábil respectively, and a suspended agent can only
  file pending declarations/rectifications. (FR-101)
- **AC-013:** Given the agent's own IVA ledger, when retained tax is
  posted, then it is fiscal-neutral (no crédito/débito/compensation) with
  the exporter exception routed to refundable crédito fiscal; ledger
  captions are exactly "IVA - Retenciones por Pagar" /
  "IVA - Retenciones por compensar". (FR-073, FR-091, FR-093)
- **AC-014:** Given any citation surface of this regime, then no form
  number cites D-20-2006/AG 425-2006 (RetWeb owns forms — R46), no
  "resolución 2-2010" string exists anywhere, and the GOQ-118 finding is
  recorded: AG 425-2006 art. 4 (Sistema procedure) and art. 9 (dualidad)
  are distinct articles, both correctly cited. (FR-069, FR-107, FR-084;
  LB-017)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text verbatim from the register (abbreviated where noted). GOQs
are trace-pending, not blockers; statuses as marked.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-06 (owned; register lists TX3, F2 rate catalog): "5% IVA-retention additions (Pequeño suppliers ≥ Q2,500.01; Agropecuario on total factura) + 1.5% 'valor total' qualifier vs the D-20-2006/AG 425-2006 matrix — reconcile vs LIVA art. 54-bis text (GOQ-01 kin) before freezing the retention-rate catalog." Affects FR-080/081/082 (+ FR-088 card mechanics, EV04b print): all carry status secondary-print-pending, never frozen. Task 2's OQ-002 is the same GOQ (pequeño-side view). | no | GT synthesis wave S-GT2 → acquisition queue (LIVA art. 54-bis text; GOQ-01 kin) | open |
| OQ-002 | GOQ-65 (owned; register lists TX3 historical): "78_ pre-2012 original wordings (art. 2 ¶4, 12, 13, 20, 21) not in corpus (D-4-2012 footnotes only) — historical CRs needing pre-2012 text must source the 2006 first print." Affects FR-075 (Q30,000 paragraph vintage) and FR-102 (prohibition wording): the Q30,000 floor's pre-2012 state is unknowable from the corpus. | no | GT synthesis wave S-GT2 → acquisition queue (2006 first print) | open |
| OQ-003 | GOQ-66 (owned; register lists TX3 flag): "Art. 2 Q30,000 retention-abstention floor vs art. 20 Q30,000 bancarización vs art. 10 Q2,500 — interplay unstated; flag only, do not model as linked." Affects FR-090 guard and FR-082's floor-interplay note (which Q-floor governs sector-público 5% rows — unresolved, config-resolved per deployment). | no | GT synthesis wave S-GT2 (flag discipline) | open |
| OQ-004 | GOQ-67 (owned; register lists TX3 fuel/import edges): "Art. 4 fuel 1.5% base includes the petroleum-distribution tax — its own regime + post-2006 base changes external; also NO import-side retention rule anywhere in D-20-2006 (verify externally before asserting)." Affects FR-077/FR-110 guards. | no | GT synthesis wave S-GT2 → external verification (petroleum-tax regime; import-side absence) | open |
| OQ-005 | GOQ-118 (owned-kin; register lists F6, TX3): "AG 425-2006 art. 4 vs 'art. 9' (64_ analysis) for the multi-group retention rule — instrument IS in corpus (79_); re-verify article contents at synthesis." RESOLVED in-corpus 2026-08-20 from the 79_ text layer: **art. 4 = "Procedimiento de aplicación de los porcentajes de retención"** (Sistema computes % per factura) and **art. 9 = "Dualidad de calidades como agentes de retención"** (multi-group rule) are distinct articles; the 64_ criterio's "artículo 9" citation for the multi-group rule is CORRECT and EVID-261's art. 4 attribution for the Sistema rule is correct — R52 tension dissolved (the EV02d extraction carried no dedicated EVID for art. 9, which explains the tension). Finding recorded at LB-017/FR-084. | no | GT synthesis wave S-GT2 (resolved; register annotation pending) | resolved |
| OQ-006 | GOQ-119 (owned-kin; register lists F6, TX3): "Dualidad same-invoice co-application: Criterios 1-2 state 65% (exporter quality) + 15% (second quality) on the same object without reconciling co-application; operative % per factura = SAT's Sistema de Retenciones — modeling call at synthesis." Modeling call MADE (FR-084/FR-085): per-quality retention at per-activity statutory rates, configuration-driven dated data, per-factura % via the Sistema model with prorrateo; the residual same-invoice co-application tension (e.g. D.29-89 exporter also especial: 65% AND 15% both stated) remains unresolved in text and stays a deployment-configuration decision. | no | GT synthesis wave S-GT2 (modeling call recorded; textual tension open) | open |
| OQ-007 | GOQ-01 (kin; register lists TX1/TX2/TX3 freeze): "Post-2018 consolidated Ley IVA 27-92 text: … art. 54 B/BIS nomenclature …". Affects FR-083 (statutory-agent article body absent; 52_ prints "54 B" [sic] — equating with 54 BIS requires the post-2018 text, R59) and FR-080/081 (5% statutory basis). Context note (never a new GOQ): the RetWeb SAT-2320 agropecuario 10-días-hábiles deadline variant (FR-107) is a printed value whose instrument is not in the corpus — R47 deferral answered here with the statutory half (15 días hábiles uniformly, R26). The IVA-side FESP retention rate/mechanics row (FR-097 handoff ↔ 05_ LB-021/GT-TAX-FR-188) likewise rides this missing post-2018 consolidated IVA text. | no | GT synthesis wave S-GT2 → acquisition queue (DCA Edición Legal / accountant; shared with Tasks 1–2) | open |
