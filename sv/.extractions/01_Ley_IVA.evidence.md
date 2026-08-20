# Evidence — 01_Ley_IVA.pdf + 02_Reglamento_IVA.pdf

Sources: `sv/sources/01_Ley_IVA.pdf` (D.L. 296, 1992, reformed), `sv/sources/02_Reglamento_IVA.pdf` (D.E. 83, 1992, reformed)
Read: 2026-08-16 (W3). Full documents (58pp + 11pp).
Re-read end-to-end 2026-08-20 (W15, S9-prep): EVID-304..338 below bring the
corpus to S7/S8 fidelity (verbatim + txt PAGE anchors) ahead of the IVA-core
synthesis wave. W3 entries EVID-047..058 are PRESERVED (cited by S1/S3 files).
Citation form: Article + txt PAGE n (page markers in `01_Ley_IVA.pdf.txt` /
`02_Reglamento_IVA.pdf.txt`, worktree-local).

---

## EVID-047 Ley IVA — scope and taxable events

- **Loc:** Art. 1 (p.2), Arts. 4-8 (pp.2-3), Arts. 14-19 (pp.5-12).
- **Gloss:** IVA applies to transfer/import/internación/export/consumption of bienes muebles corporales (tangible movable goods, Art. 5) and provision/import/internación/export/autoconsumo of services (Arts. 16-17: exhaustive service list a-q incl. leases, professional fees, dietas, membresías, expense reimbursements). Transfer concept broad (Arts. 6-7: permutas, daciones en pago, auction sales, consignments, reorg transfers...). Tax point: goods = document issuance or delivery/payment, whichever first (Art. 8); consignment = when consignatario acts (Art. 8 inc.3). Services = earliest of invoicing, completion, delivery, or payment/credit-to-account even in advance (Art. 18). Territoriality: service taxed where the activity is performed (Art. 19).
- **Candidate CRs:** event model covering goods+services tax points (incl. advance payments); consignment trigger.
- **Topics:** taxation

## EVID-048 Ley IVA — 13% rate; débito/crédito mechanics

- **Loc:** Art. 54 (p.26): "LA TASA DEL IMPUESTO ES EL TRECE POR CIENTO". Art. 55 (débito = rate × base per operation). Art. 57 (p.27): **"Dicha cantidad deberá constar en el Comprobante de Crédito Fiscal... en forma separada del precio o remuneración de la operación"** — CCF must show IVA SEPARATE from price. Art. 64: payable = débito − crédito of the period.
- **Gloss:** CCF (B2B) = net price + separately-stated IVA → **resolves EVID-023 doubt: CCFE prices are NET, IVA added** (structure manual's "(con inclusión de IVA)" wording in ventaGravada for CCF is copy-paste error; the FE's is deliberate). FE (consumer) IVA-inclusive per structure manual — consistent: consumers see final price; CCF separates for crédito-fiscal deduction.
- **Topics:** taxation, e-invoicing

## EVID-049 Ley IVA — base imponible rules

- **Loc:** Arts. 47-53 (pp.23-25).
- **Gloss:** generic base = price/remeueration; cannot be below documented amounts. Specific bases per operation type (Art. 48 a-m: imports = CIF + tariffs + specific consumption taxes, IVA excluded from base). NOT in base: indemnifications, tips, union dues (Art. 49). ADD to base (Art. 51): price adjustments, financing interest incl. late-payment interest, freight/reimbursements (unless in the buyer's name by mandate), accessories (packaging, insurance, maintenance), special taxes; EXCLUDE IVA itself. EXCLUDE from base if already in CCF/ND (Art. 52): general unconditional commercial discounts. FX: exchange rate at tax-point date; later FX diffs not in base but deferred-payment FX diffs are (Art. 53).
- **Candidate CR:** Odoo tax base composition (exclude IVA, include specific taxes & finance charges per rules).
- **Topics:** taxation

## EVID-050 Ley IVA — créditos fiscales: deductibility rules

- **Loc:** Art. 65 (pp.30-31): deductible ONLY for (1) activo realizable goods, (2) fixed-asset goods keeping identity, (3) services in the business (not construction of real estate), (4) general expenses (freight, electricity, phone, water) — ALL must be INDISPENSABLE to the giro and generate taxable/0%/donation/diplomatic output; otherwise documented with FACTURA not CCF. Requirements: original CCF, IVA stated separately, recorded in Libro de Compras (CT Art. 141), inventory register (CT Art. 142). Retentions by agents = crédito fiscal for the agent if declared & paid in the same period (Art. 65, referencing CT Arts. 161-162, 112).
- **Art. 65-A (pp.32-34): non-deductible list** — food (if not food business), vehicles not strictly indispensable + their fuel/repairs/insurance (50% pro-deductible if mixed use), hotels (unless business use shown), plane tickets (unless business travel of verifiable employees), clothing/jewelry (if not the trade), personal/family use goods, alcohol & cigarettes (if not the trade), over-legal-rate IVA transfers, anything not indispensable, real-estate construction inputs, **purchases ≥ 58 minimum wages paid in cash or without formal contract → non-deductible**. Fake/irregular docs never credit: unregistered emitter, unproven operations, de-registered subjects, unauthorized number ranges, docs not in the buyer's name.
- **Candidate CRs:** supplier-document type enforcement (factura vs CCF by deductibility); retention credit timing; 58-minimum-wage cash payment rule; mixed-use 50% vehicle rule.
- **Topics:** taxation

## EVID-051 Ley IVA — pro-rata (Art. 66) detailed mechanics

- **Loc:** Art. 66 (pp.34-36). Factor = gravadas / (gravadas + exentas + no sujetas) per period; **accumulated** recalculation from first pro-rata period through fiscal year end; next-year first month: full-year recalculation redistributes crédito fiscal (sum difference to/against next period's credit). Excluded from denominator: no-subject ops from non-habitual activities without attributable credits, donations to ISR Art.6 institutions, diplomatic sales. No-subject = not within hechos generadores or expressly declared so. Proportion of credit for exempt/no-sujeta ops → cost or expense.
- **Candidate CR:** monthly + annual-true-up proportional credit engine (Odoo: needs custom logic beyond standard fiscal positions).
- **Topics:** taxation

## EVID-052 Ley IVA — carryforward, transfers, fixed assets

- **Loc:** Art. 67 (excess credit carries forward indefinitely), Art. 68 (no refund on cessation), Art. 69 (non-transferable except legal continuation/fusion; not inheritable), Art. 71 (fixed-asset transfers not taxable after 4 years in asset base — before that, taxable), Art. 72 (fixed-asset credit deductible; also repair/remodel credit when not increasing value/life).
- **Topics:** taxation

## EVID-053 Ley IVA — exports 0% + credit refund regime

- **Loc:** Arts. 74-77 (pp.37-40). Exports = definitive transfers for foreign use + services performed in-country for non-residents used exclusively abroad (connection/continuation/termination of services originated abroad = 13%, NOT export). Rate 0% (Art. 75). Export credit deductible against internal débito; excess: carry forward, offset against other taxes, or **reintegro** (refund) on request — DGII must resolve ≤30 days; mixed exporters refund only the export-proportional part, **capped at 13% of export value per period**; unrefunded excess accumulates. Requirements: declaration filed, not omiso, provide purchase/sales detail.
- **Reglamento Arts. 29-30:** Zonas Francas / Recintos Fiscales sales count as EXPORTS (documented via Póliza de Exportación / DM); exporters must keep purchase ledger split (export vs local vs common — common split % by sales monthly).
- **Candidate CRs:** export 0% tax + separate export credit ledger + refund workflow with 13% cap.
- **Topics:** taxation, special-regimes

## EVID-054 Ley IVA — adjustments (devolutions/discounts/rebates)

- **Loc:** Art. 62 (pp.27-29): débito adjustments — subtract returns/annulments/rescissions **within 3 months** of delivery/payment (perishable medicines: up to 2 YEARS with detailed lot registry incl. lote, vencimiento, inventory movements, CCF ref, and NC referencing lote number; destruction acts by health authority) and discounts/rebates already taxed; add price increases, under-transferred débito, excess transferred unless refunded. Via CCF + notas (ref. Art. 100 CT). Art. 63: crédito adjustments mirror for purchases; late-received CCF/ND credit usable up to **3 following periods**; late NC reduces credit in its emission period unless received late → up to 3 periods; beyond that, amend declarations.
- **Candidate CRs:** 3-month return window (medicines 2y w/ lot tracking); 3-period late-document rules — map to Odoo NC/ND period handling.
- **Topics:** taxation, e-invoicing

## EVID-055 Ley IVA — excluded taxpayers (sujetos excluidos)

- **Loc:** Arts. 28-32 (pp.15-16). Exclusion thresholds: < 50,000 colones 12-month transfers AND < 20,000 colones total assets (colon-era values — historical; actual exclusion now administered via NRC/registration; thresholds dated but the REGIME persists: FSEE document type, no crédito fiscal transfer, no IVA recargo on their invoices (Art. 32: excluded subjects' facturas show price WITHOUT any IVA surcharge)). Art. 31: IVA charged to/by them never generates credit. Optional inscription from next Jan 1.
- **Gloss:** FSEE (DTE 14) exists for this population; their facturas must NOT show IVA. Odoo mapping: partner fiscal category drives document type + tax behavior.
- **Topics:** taxation, e-invoicing

## EVID-056 Ley IVA — declaración: monthly, F-07 context

- **Loc:** Art. 93 (monthly calendar period; declaración jurada with gravadas/exentas/no sujetas, débito, crédito, carryover), Art. 94 (**first 10 hábiles of following month**; imports liquidated at customs; import payment constancy = crédito fiscal document). No extensions/installments (Art. 81 inc.2).
- **Topics:** taxation, fiscal-reporting

## EVID-057 Ley IVA — massive repeals to Código Tributario

- **Loc:** ~60 articles DEROGADO (D.L. 230/00): registration (88-92), documents emission/requirements (97-106), accounting records (107), formal obligations (108), entire sanctions regime (109-141), administration/fiscalization (142-164), payment/mora (79-80, 82-87). Effective law: substance (hechos generadores through cálculo) in Ley IVA; procedures/sanctions/documents in Código Tributario.
- **Gloss:** for requirements, document rules live in CT Arts. 110-142 range (per cross-references); next wave (W4 Código Tributario) collects them. Art. 65 refs CT 141 (libro compras), 142/142-A (inventory register); Art. 62/63 ref CT Art. 100 (notas); Art. 65 refs CT 161-162 (retention agents), CT 112 (comprobante de retención).
- **Topics:** taxation (process note for W4)

## EVID-058 Reglamento IVA — operative articles

- **Loc:** Rgto. Arts. 1-30 (surviving). Definitions (Art. 2: exportación, importación/internación definitiva, regímenes aduaneros especiales incl. zonas francas/perfeccionamiento activo); retiro de bienes scope + fuerza mayor proof (Art. 4: inventory annotations, police reports, insurance settlements, legal mermas); service definitions (Arts. 5-7: continuous services, precio alzado, comisión/mandato/consignación); desechos transferers are contributors (Art. 8); fixed-asset docs (Art. 26: Factura or CCF if taxable, else other doc); ZF sales = exports (Art. 29); export credit refund bookkeeping (Art. 30). Inventory credit in duodécimas (Art. 50, transitional 1992 — historical).
- **Gloss:** reglamento is 80% repealed (procedures moved to CT); surviving substance = definitions + export/ZF rules.
- **Topics:** taxation

## Open questions from this pass

1. **OQ:** Art. 28 thresholds in colones — verify current-status (exclusion presumably governed by registration/NRC practices now). Non-blocking for requirements (FSEE regime documented regardless).
2. **OQ:** FOVIAL/COTRANS legal basis NOT in Ley IVA (separate laws; guide 31_ covers mechanics). Confirm whether they form part of IVA base (Art. 51.d suggests specific taxes ARE in base — FOVIAL/COTRANS treatment vs "impuestos especiales" needs the FOVIAL/COTRANS laws; only guide 31_ in sources).
3. **OQ (resolves EVID-023):** DONE — CCFE net price confirmed by Art. 57 (IVA separate from price). FE inclusive confirmed by structure manual. Close the doubt; note in synthesis that ventaGravada CCF wording in manual is erroneous.

## Topic tag summary

taxation: EVID-047..058 (048, 054, 055 also e-invoicing; 053 also special-regimes; 056 also fiscal-reporting)

---

# W15 DEEP PASS (2026-08-20, S9-prep) — EVID-304..338

Full re-read of both txts (01: 58 pp; 02: 11 pp). Verbatim quoted where
load-bearing; PAGE = `01_Ley_IVA.pdf.txt` marker unless prefixed Rgto.
(= `02_Reglamento_IVA.pdf.txt`).

## EVID-304 Ley IVA — identity, reform chain, unconstitutional arts, consolidation vintage

- **Loc:** title block (PAGE 1); REFORMAS / DEROGATORIAS / INTERPRETACIONES / DECLARATORIA blocks (pp. 56-58, PAGE 56-58).
- **Verbatim (reform tail):** "(1) D.L. Nº 495, 31 DE MARZO DE 1993 … (8) D.L. Nº 495, 28 DE OCTUBRE DE 2004; D.O. Nº 217, T. 365, 22 DE NOVIEMBRE DE 2004. (9) D.L. Nº 644 … (10) D.L. No. 183 … (11) D.L. No. 224, 12 DE DICIEMBRE DE 2009 … (12) D.L. No. 498, 19 DE SEPTIEMBRE DE 2013 … (13) D.L. No. 832, 30 DE OCTUBRE DE 2014 … (14) D.L. No. 71, 29 DE JULIO DE 2015; D.O. No. 146, T. 408, 14 DE AGOSTO DE 2015."; "DECLARATORIA DE INCONSTITUCIONALIDAD: LA SALA DE LO CONSTITUCIONAL … DECLARO LOS ARTICULOS 113, 123, 124 Y 161 INCONSTITUCIONALES … RESOLUCION DEL DIA 17 DE DICIEMBRE DE 1992, … EXPEDIENTES NUMEROS 3-92 Y 6-92."; partial derogations D.L. 720/93, 516/95, 230/00, 877/00; interpretaciones auténticas D.L. 634-1993 (Art. 173), 820-1994 (Art. 45-d), 645-2005 (Art. 14); vetoed D.L. 24-2003 (5y agro-input IVA exemption — never entered).
- **Gloss:** consolidation = Asamblea Índice Legislativo edition through reform (14) **D.L. 71-2015** — NO reform stamp after Jul-2015 (contrast ISR 54_ through Jan-2026). Art. 175 vigencia 1-sep-1992. **Vintage watch (SOQ-22/30 kin): post-2015 reforms unverified until an official current consolidation is acquired; corpus-internal signals (DTE stack 44_/45_, Quincena-25 66_/67_, F-07 v14 manual) show no post-2015 substantive IVA reform, but the watch must ride every 01_ LB.**
- **Candidate CR:** version-regime note per D12; never-implement rows for void arts (already repealed by D.L. 230/00 anyway).
- **Topics:** taxation

## EVID-305 Ley IVA — Arts. 1-2: scope; coexistence with special taxes

- **Loc:** Arts. 1-2 (p.2, PAGE 2).
- **Verbatim:** Art. 1: impuesto applies to "la transferencia, importación, internación, exportación y al consumo de los bienes muebles corporales; prestación, importación, internación, exportación y el autoconsumo de servicios". Art. 2: "Este impuesto se aplicará sin perjuicio de la imposición de otros impuestos que graven los mismos actos o hechos, tales como: la producción, distribución, transferencia, comercialización, importación e internación de determinados bienes y la prestación, importación e internación de ciertos servicios."
- **Gloss:** IVA coexists with impuestos especiales (FOVIAL/COTRANS kin: separate contributions over the same fuel operations — the Art. 2 coexistence + Art. 51-d base rule are the Ley-side anchors of the SR8 exclusion guard).
- **Topics:** taxation, special-regimes

## EVID-306 Ley IVA — Arts. 4-10: transfer concept, enumeración, tax point, territoriality (goods)

- **Loc:** Arts. 4-10 (pp. 2-5, PAGE 2-6).
- **Verbatim (key):** Art. 5: "EN EL CONCEPTO DE BIENES MUEBLES CORPORALES SE COMPRENDE CUALQUIER BIEN TANGIBLE QUE SEA TRANSPORTABLE…". "LOS TÍTULOS VALORES Y OTROS INSTRUMENTOS FINANCIEROS SE CONSIDERAN BIENES MUEBLES INCORPÓREOS…". "PARA EFECTOS DE LO DISPUESTO EN ESTA LEY, LOS MUTUOS DINERARIOS, CRÉDITOS EN DINERO O CUALQUIER FORMA DE FINANCIAMIENTO SE CONSIDERA PRESTACIÓN DE SERVICIOS." Art. 7 a)-m): subasta/adjudicación en pago/remate; permutas; daciones en pago; cesión de títulos de dominio; mutuos de cosas fungibles; **aportes de bienes del giro a sociedades (f)**; **reorg-transferencias (g)**; **disolución/liquidación/disminución-de-capital adjudications — NOT taxable when the adjudicatario is the mismo socio who aportó and the bien was not IVA-charged (h)**; establecimientos (activo realizable only, i); usufructo/explotación rights (j); **promesa de venta seguida de posesión (k)**; catch-all free-disposition (l); **bienes adquiridos en pago de deudas (m)**. Art. 8: causado "cuando se emita el documento que da constancia de la operación"; earlier payment/delivery ⇒ then; **consignment: when the consignatario performs any of those acts**; caused even with omission/mora of price. Art. 9: cambio/devolución (mal estado, vencidos, averiados, wrong goods) = NOT a new transfer → Art. 62-1-a) adjustment, unless new-contract intent proven. Art. 10: goods taxable when "situados, matriculados o registrados en el país"; goods shipped from SV to non-contribuyente acquirers = situados in SV.
- **Candidate CRs:** operation-type taxonomy incl. aportes/reorgs with the (h) carve-out; consignment trigger; exchange/return → NC path.
- **Topics:** taxation

## EVID-307 Ley IVA — Arts. 11-13: retiro de bienes (self-supply)

- **Loc:** Arts. 11-13 (p.6, PAGE 6).
- **Verbatim (key):** Art. 11: retiro/desafectación from activo realizable "con destino al uso o consumo propio, de los socios, directivos o personal de la empresa"; ALSO "los retiros … destinados a rifas, sorteos o distribución gratuita con fines promocionales, de propaganda o publicitarios, sean o nó del giro". Presumption: "Se considerarán retirados o desafectados todos los bienes que faltaren en los inventarios y cuya salida … no se debiere a caso fortuito o fuerza mayor o a causas inherentes a las operaciones…". NOT retiro: realizable→fijo transfers "siempre que sean necesarios para el giro"; donations to ISR Art. 6-c entities (previously calificadas) meeting Dirección General requirements. Art. 12: caused "en la fecha del retiro". Art. 13: territoriality same situs rule.
- **Candidate CRs:** self-consumption invoice engine (price = public-sale value per Art. 48-c); inventory-shortfall presumed-retiro flag with fuerza-mayor evidence gate (Rgto. Art. 4 proof menu).
- **Topics:** taxation

## EVID-308 Ley IVA — Arts. 14-15 + D.L. 645: importación/internación of goods and services

- **Loc:** Arts. 14-15 (pp. 7-9, PAGE 7-9 incl. embedded D.L. 645 text).
- **Verbatim (key):** Art. 14: hecho generador = "la importación e internación definitiva al país de bienes muebles corporales y de servicios"; aduana auctions = import acts; "Existe importación o internación de servicios cuando la actividad que generan los servicios se desarrolla en el exterior y son prestados a un usuario domiciliado en el país que los utiliza en él". **D.L. 645 (17-mar-2005, D.O. 55 T.366 18-mar-2005) interpretación auténtica of Art. 14-III: "la utilización del servicio debe ocurrir de manera exclusiva en el territorio de la República de El Salvador"** (incorporated into the law from its vigencia). Art. 15: goods = caused at the import/internación moment (uppercase, stamp (8)); **services imports: earliest of a) prestador document emission, b) payment, c) término de la prestación**; special customs regimes: devenga in full (or the difference) "al quedar los bienes entregados a la libre disponibilidad … por haberse convertido la importación o internación en definitiva".
- **Candidate CRs:** import-service self-liquidation flow (Art. 94-IV: at DGII, paid at Tesorería); ZF/DPA definitive-conversion trigger (SR4 kin by id).
- **Topics:** taxation, special-regimes

## EVID-309 Ley IVA — Arts. 16-17: services hecho generador + catalog a)-q) + reintegros

- **Loc:** Arts. 16-17 (pp. 9-11, PAGE 9-11).
- **Verbatim (catalog anchors):** Art. 16: "LAS PRESTACIONES DE SERVICIOS PROVENIENTES DE ACTOS … EN QUE UNA PARTE SE OBLIGA A PRESTARLOS Y LA OTRA … A PAGAR COMO CONTRAPRESTACIÓN UNA RENTA, HONORARIO, COMISIÓN, INTERÉS, PRIMA, REGALÍA…"; autoconsumo (socios/directivos/apoderados/personal/grupo familiar/terceros) IS taxable; NOT: indemnizaciones de perjuicios o siniestros; NOT: "DONACIONES DE SERVICIOS DE CARÁCTER GRATUITO E IRREVOCABLES" to ISR-Art.-6 qualified entities. Art. 17 a)-q): a) permanentes/regulares/continuos/periódicos; b) asesorías técnicas y planos; c) arrendamiento de MUEBLES (incl. opción de compra); **d) arrendamiento de INMUEBLES destinados a actividades comerciales/industriales/servicios** (housing exempt per 46-b); f)-h) obra material/ingeniería/instalación/movimientos de tierra (administración o alzado); i) repairs/maintenance; j)-k) construcción (administración vs alzado); l) comisión/mandato/consignación/remates; **m) transporte o flete de carga terrestre, aéreo y marítimo Y de pasajeros aéreo y marítimo** (terrestrial passengers exempt per 46-i); n) profesiones liberales incl. "la función del notariado"; o) marcas/patentes/procedimientos royalties; **p) dietas o emolumentos (NOT labor-law dietas nor public employees)**; **q) membresías/cuotas**. Final: "SE ASIMILA A PRESTACIONES DE SERVICIOS LOS REINTEGROS O REEMBOLSO DE GASTOS … SE GRAVARÁN AL MOMENTO DE SU PAGO", except seguros/alimentación/viáticos to trabajadores and reembolsos meeting the Art. 51-a) mandate exception "SIEMPRE QUE EL MANDATARIO NO SE HUBIERE DEDUCIDO CRÉDITOS FISCALES EN RELACIÓN CON DICHAS SUMAS".
- **Candidate CRs:** service-product mapping (Odoo product categories → IVA gravado rules); expense-reimbursement surcharge lines with the two exception gates; notarial fees.
- **Topics:** taxation

## EVID-310 Ley IVA — Arts. 18-19: service tax points; territoriality incl. transit rule

- **Loc:** Arts. 18-19 (pp. 11-12, PAGE 11-12).
- **Verbatim (key):** Art. 18: earliest of a) documents (Arts. 97/100 refs → CT 110-115 zone); b) término; c) delivery of leased good; d) delivery of bien/obra; **e) payment/credit "AUNQUE SEA CON ANTICIPACIÓN"**. Permanent/periodic services: caused at document or "al término de cada período establecido para el pago", whichever first, "independientemente de la fecha de pago". Leasing-with-purchase: at exigibilidad of cánones or at sale perfection. Art. 19: taxed when "presten directamente en el país … cualquiera que sea el lugar en que se pague"; partial in-country ⇒ proportional, BUT full when performed in-country even if not exclusively used there, "como por ejemplo cuando ellos se relacionan con bienes, transportes o cargas en tránsito". **Final (stamp 11): foreign-transport services already added to the import base (Art. 48-g) "NO SERÁN GRAVADOS NUEVAMENTE".**
- **Candidate CRs:** advance-payment débito trigger (deposit lines); in-transit full-taxation flag; no-double-tax guard for international freight in import base.
- **Topics:** taxation

## EVID-311 Ley IVA — Arts. 20-27: sujetos pasivos; contribuyentes; habitualidad; matriz/sucursales; agrupamientos

- **Loc:** Arts. 20-27 (pp. 12-15, PAGE 12-15).
- **Verbatim (key):** Art. 20: subjects a)-f) personas naturales/jurídicas, sucesiones, sociedades nulas/irregulares/de hecho, fideicomisos, asociaciones cooperativas, **uniones de personas/asocios/consorcios (f, stamp 11)**; government entities are sujetos pasivos when realizing the hechos "no obstante que las leyes … las hayan eximido" — **EXCEPT bursátiles activities**; who acts at own name = sujeto pasivo (propio o por cuenta de tercero); acting for a tercero ⇒ the mandante; entities without personality act through integrantes/administradores. Art. 22: contribuyentes = habitual transferors (productores, comerciantes mayoristas/minoristas "u otras calidades"), incl. materias primas/insumos not consumed in production; NOT: occasional transferors without resale intent. Art. 23: importers are contribuyentes "en forma habitual o nó". Art. 25: DGII califies habitualidad (nature/quantity/frequency); **"Se presume de derecho que existe habitualidad" for the objeto social/giro principal and for comerciantes' CC acts** — presumption admits no proof-in contrario. Art. 26: matriz local + sucursales/agencias = ONE taxpayer (capacidad radicada en la matriz). Art. 27 (stamp 11): agrupamientos without personality ⇒ representante/administrador responsible; failing them the asociados responden solidariamente.
- **Candidate CRs:** company fiscal-category config (single taxpayer across warehouses/establishments — D14 kin); joint-venture/consortium solidarity flag.
- **Topics:** taxation

## EVID-312 Ley IVA — Arts. 28-32: excluidos regime (colones thresholds) [MOQ-03 resolution target]

- **Loc:** Arts. 28-32 (pp. 15-16, PAGE 15-16).
- **Verbatim (key):** Art. 28: excluidos = 12-month transfers (gravadas+exentas) "< A CINCUENTA MIL COLONES" AND total activo "< A VEINTE MIL COLONES"; crossing either ⇒ contribuyente "A PARTIR DEL MES SUBSIGUIENTE A AQUEL EN QUE ELLO OCURRA"; DGII inscribes oficio/petition. "Lo dispuesto … no tiene aplicación respecto de sociedades e importadores" nor when multiple locales jointly exceed the limits. Art. 29: start-ups excluded if initial activo < ¢20,000 (never for imports). Art. 30: optional contribuyente status "a partir del primero de enero del año calendario siguiente" (DGII may allow anytime). Art. 31: IVA recargado to excluidos / paid on their imports is NEVER crédito for them nor traslatable. Art. 32: "En las facturas o documentos equivalentes que emitan los excluídos … deberán consignar el precio de la operación, sin ningún recargo a título del presente impuesto."
- **Gloss:** thresholds are 1992 COLONES values never updated in the text (10_ kin: colones-era remnant; USD administration now via registration practice). MOQ-03 resolution = OQ row: regime persists (FSEE doc type + no-IVA facturas + no crédito); the ¢ thresholds enter as [sic] historical text with a config-gap for the administered exclusion criteria (NRC/registration practice), NO invented USD conversion (S5 ruling 39 discipline).
- **Candidate CRs:** partner l10n_sv fiscal category excluido → FSEE doc + price-without-IVA enforcement (e-invoicing by id).
- **Topics:** taxation, e-invoicing

## EVID-313 Ley IVA — Art. 45 + D.L. 820 + 167-A: import/internación exemptions

- **Loc:** Art. 45 (pp. 19-21, PAGE 19-21 incl. embedded D.L. 820), Art. 167-A (p.52, PAGE 52).
- **Verbatim (catalog):** 45: a) DEROGADO (D.L. 877/00); b) diplomatic missions (reciprocity); c) international organizations El Salvador belongs to; **d) equipaje de viajero — D.L. 820 (23-feb-1994, D.O. 54 T.322 17-mar-1994) interpretación auténtica: "únicamente … efectos personales de uso o consumo normal del viajero … en ningún caso … los vehículos automotores"**; e) donated goods from abroad to ISR-6-c entities; f) donations under convenios; g) **municipal imports for obras/beneficio directo de la comunidad (stamp 1)**; **h) suministro de agua y alcantarillado by public institutions — subject to 167-A**; **i) autobuses/microbuses/vehículos de alquiler for PUBLIC PASSENGER TRANSPORT (stamp 6/12): importers' transfers to transport subjects also exempt; vehicles must meet Reglamento de Transporte Terrestre specs; "ÚNICAMENTE PODRÁN SER TRANSFERIDOS HASTA DESPUÉS DE CINCO AÑOS DE LA LEGALIZACIÓN DE INTERNACIÓN … SI FUEREN TRANSFERIDOS EN ESE PERÍODO PAGARÁN EL IMPUESTO POR LA IMPORTACIÓN, Y EL NUEVO ADQUIRIENTE … POR LA TRANSFERENCIA INTERNA, … ART. 71"**. 167-A: the 45-h exemption "QUEDARÁ SIN EFECTO A PARTIR DE LA VIGENCIA DEL INSTRUMENTO LEGAL QUE REGULE EL RÉGIMEN DE POLÍTICAS SECTORIALES" (kill-switch; instrument not in corpus — watch row).
- **Candidate CRs:** exemption reason codes on import moves; 5-year transfer-restriction register per vehicle (legalización-date anchor — D15 dated row).
- **Topics:** taxation, special-regimes

## EVID-314 Ley IVA — Art. 46: service exemptions a)-l)

- **Loc:** Art. 46 (pp. 21-22, PAGE 21-22).
- **Verbatim (catalog):** a) salud by public + utilidad-pública institutions (DGII-calified); b) arrendamiento of inmuebles "DESTINADOS A VIVIENDAS PARA LA HABITACIÓN" (commercial leases taxable per 17-d); c) **dependence-relationship services (labor law) + public/municipal/autonomous employees**; d) cultural public spectacles (calified/authorized); e) education — **"ÚNICAMENTE LOS VALORES … PAGUEN A INSTITUCIONES EDUCATIVAS PÚBLICAS O PRIVADA AUTORIZADAS POR EL MINISTERIO DE EDUCACIÓN" (stamp 11)**; f) **deposit/loan INTEREST of banks + SSF-supervised + savings-credit cooperatives + BCR-qualified foreign institutions + ISR-6-excluded public-utility financing corporations/foundations — DGII+BCR joint instrument required for BCR qualification cases (stamp 8/11)**; g) emission/placement of state + official-autonomous titles + private primary-public-offering (bolsa) — interest (stamp 1); h) public electricity/water/alcantarillado; i) **terrestrial public passenger transport** (air/sea passengers taxable per 17-m); j) **seguros de personas (prima payment) + reaseguros general**; k) **employer cotizaciones to AFPs "EN LO QUE RESPECTA A LAS COMISIONES DE ADMINISTRACIÓN … DE ACUERDO … ARTÍCULO 16 LITERAL b) DE LA LEY DEL SISTEMA DE AHORRO PARA PENSIONES"** — cites the SAP D.L. 927-1996, superseded by D.L. 614 (R24 kin: the exemption substance survives for pension-administration commissions; the cited-law anchor is stale as printed); l) Lotería Nacional operations under its law.
- **Candidate CRs:** exemption tax codes per service family; financial-interest exemption gating on SSF/BCR qualification flags (config-gap); education-exemption limited to MINED-authorized institution payments.
- **Topics:** taxation

## EVID-315 Ley IVA — Arts. 47-50: base imponible generic + specific a)-m); non-base items

- **Loc:** Arts. 47-50 (pp. 23-24, PAGE 23-24).
- **Verbatim (key):** Art. 47: base = "el precio o remuneración pactada … o al valor aduanero en las importaciones o internaciones"; floor: base "No podrá … ser inferior a los montos que consten en los documentos" (± 51/52/53); omisión/plazo of payment no impediment. Art. 48 a)-m): a) transfers = precio (remates + subastador rights); b) leasing-with-purchase = renta periódica, then valor residual; c) retiros = assigned public-sale price per records, else mercado; d) establecimientos = value of bienes muebles comprendidos; e) permutas = each party seller on its own side's value; f) sales paid with services = value of the bienes; **g) imports = "VALOR CIF O VALOR ADUANERO + DERECHOS ARANCELARIOS + IMPUESTOS ESPECÍFICOS AL CONSUMO. EN NINGÚN CASO EL PRESENTE IMPUESTO FORMARÁ PARTE DE LA BASE IMPONIBLE"**; h) services = total contraprestación (goods-in-payment = value of goods); i)-j) installation/construction contracts = agreed price, **goods supplied by the prestador AGREGADOS even if the standalone transfer would be exempt, unless already in the contract value**; k) self-used services = assigned value, floor = mercado; l) commercial-real-estate leases = renta convenida; m) comisionistas = the commission. Art. 49: NOT base: indemnizaciones (not consideration), propinas, cotizaciones provisionales/sindicales/similares. Art. 50: DEROGADO.
- **Candidate CRs:** base-composition engine (include specific taxes, exclude IVA; goods-included-in-service rule; permuta dual-side).
- **Topics:** taxation

## EVID-316 Ley IVA — Arts. 51-53: additions, exclusions, FX

- **Loc:** Arts. 51-53 (pp. 24-26, PAGE 24-26).
- **Verbatim (key):** Art. 51 ADD: a) "REAJUSTES, ACTUALIZACIONES O FIJACIONES DE PRECIOS …; COMISIONES, DERECHOS, TASAS, INTERESES Y GASTOS DE FINANCIAMIENTO DE LA OPERACIÓN A PLAZO, INCLUYENDO LOS INTERESES POR EL RETARDO EN EL PAGO…; GASTOS DE TODA CLASE, FLETES, REEMBOLSOS DE GASTOS, EXCEPTO SI SE TRATARE DE SUMAS PAGADAS EN NOMBRE Y POR CUENTA DEL COMPRADOR … EN VIRTUD DE MANDATO DE ÉSTE. SE EXCLUYEN … LAS MULTAS O SANCIONES ESTIPULADAS EN CLÁUSULAS PENALES CONVENCIONALES, ASIMISMO LOS INTERESES PAGADOS A TERCEROS, DISTINTOS DEL VENDEDOR…" (stamp 1); b) accessories: "embalaje, flete, transporte, limpieza, seguro, garantías, colocación y mantenimiento cuando no constituyan una prestación independiente"; c) envases + depósitos-en-garantía; d) "impuestos especiales, adicionales, específicos o selectivos … PERO SE EXCLUYE … EL PRESENTE IMPUESTO" — **mixed gravada/exenta operations ⇒ prorate the additions**. Art. 52 EXCLUDE (if already in CCF/ND/NC): "reducciones de precios, bonificaciones, descuentos normales del comercio de carácter general y no condicionados, otorgados directamente". Art. 53 FX: base converts "AL TIPO DE CAMBIO QUE CORRESPONDA AL DÍA EN QUE OCURRA EL HECHO GENERADOR"; payment-date FX difference NOT base; **"se deben adicionar a la base imponible las diferencias en el tipo de cambio en el caso de ventas a plazo … ocurridas entre la fecha de celebración y el pago del saldo"** (kin CT Art. 62; e-invoicing §3.11 origin-rate family).
- **Candidate CRs:** tax-base includes/excludes matrix; mandate-reimbursement gate (name+account-of-buyer + no-credit-deduced); installment-FX delta lines.
- **Topics:** taxation

## EVID-317 Ley IVA — Arts. 54-58: 13% rate; débito; Art. 57 traslación (CCF separate-from-price); Art. 58 retiros→FACTURA

- **Loc:** Arts. 54-58 (pp. 26-27, PAGE 26-27).
- **Verbatim:** Art. 54: "LA TASA DEL IMPUESTO ES EL TRECE POR CIENTO" (stamp 2 = D.L. 370-1995 — rate raised from 10% to 13% effective jun-1995; dated-value kin). Art. 55: débito = rate × base per operation. Art. 57: traslado of an amount equal to the débito; "Dicha cantidad deberá constar en el Comprobante de Crédito Fiscal … EN FORMA SEPARADA DEL PRECIO O REMUNERACIÓN DE LA OPERACIÓN" (R1's legal root; FE inclusive stands per CT 114 practice); importers: IVA paid at import IS crédito. **Art. 58: retiros/autoconsumo "NO GENERAN CRÉDITO FISCAL" … "DEBERÁN DOCUMENTARSE CON FACTURA O DOCUMENTO EQUIVALENTE AUTORIZADO; EN NINGÚN CASO SE UTILIZARÁ COMPROBANTE DE CRÉDITO FISCAL O NOTA DE DÉBITO" (stamp 11 uppercase).**
- **Candidate CRs:** account.tax 13% + price_include mapping FE vs CCF (e-invoicing by id); retiro invoice forced doc-type = FE/FSEE-class, CCF/ND blocked.
- **Topics:** taxation, e-invoicing

## EVID-318 Ley IVA — Arts. 59-61: excluidos no-crédito; crédito fiscal nature

- **Loc:** Arts. 59-61 (p. 27, PAGE 27).
- **Verbatim (key):** Art. 59 DEROGADO. Art. 60: amounts trasladado to Art.-28 excluidos "no les generan crédito fiscal y constituirán costo de los respectivos bienes y servicios" (31/65 crossref). Art. 61: crédito fiscal "constituye un elemento de la estructura tributaria … Se rige exclusivamente por las normas de esta ley y no tiene el carácter de crédito en contra del fisco por pago indebido o en exceso" (repetition/refund claims route through CT, not IVA credit).
- **Topics:** taxation

## EVID-319 Ley IVA — Art. 62: débito adjustments (3-month returns; medicines 2y + lot registry; additions)

- **Loc:** Art. 62 (pp. 27-29, PAGE 27-29).
- **Verbatim (key):** 1) SUBTRACT: a) "devueltos o de otras operaciones anuladas o rescindidas en el período tributario, PERO DENTRO DE LOS TRES MESES de la entrega … o de la percepción del pago", proof the value was débito-computed before; **medicines/perishable pharmaceuticals: plazo may extend "HASTA DOS AÑOS" ⇒ fiscalización-caducidad extended 2 years from the original period; MANDATORY detailed registry fields: lote (production or import doc), nombre y presentación, fecha de vencimiento, fechas entrada/salida inventarios, CCF number (which must print lote + vencimiento), CCF fecha, cliente código; NC must reference the CCF + the returned lote; books affected ("cuenta de inventario de producto vencido"); destruction acts "SUSCRIBIRSE POR LAS AUTORIDADES SANITARIAS" (stamp 10 = D.L. 183-2006)**; b) rebajas/bonificaciones/descuentos generales no condicionados, with forma-y-condiciones proof. 2) ADD: a) price increments/reajustes/interest incl. mora; b) "Diferencias por traslación indebida de un débito fiscal inferior"; c) any traslación in excess unless restituida. Adjustments via CCF + notas (Art. 100 → CT Art. 110 zone).
- **Candidate CRs:** return-window gate (3m default / 2y medicines) on NC emission; per-lot return tracking model; débito-adjustment journal categories.
- **Topics:** taxation, e-invoicing

## EVID-320 Ley IVA — Art. 63: crédito adjustments; late-document 3-period rules

- **Loc:** Art. 63 (pp. 29-30, PAGE 29-30).
- **Verbatim (key):** SUBTRACT from crédito (if not before, evidenced in CCF or the notas of CT Art. 110): a) anuladas/rescindidas adquisiciones previously computed; b) price reductions/discounts previously computed; c) traslados in excess. ADD: late-received CCF/ND tax "PODRÁ UTILIZARSE PARA AUMENTAR EL CRÉDITO FISCAL, HASTA LOS TRES PERÍODOS TRIBUTARIOS QUE SIGUEN AL DE LA EMISIÓN". **NC: reduce crédito IN ITS EMISSION PERIOD, "SALVO QUE EL CONTRIBUYENTE DEMUESTRE HABERLAS RECIBIDO CON RETRASO" ⇒ up to 3 following periods. Beyond: "EL CONTRIBUYENTE ESTARÁ OBLIGADO A MODIFICAR LAS DECLARACIONES DEL PERÍODO … DE LA EMISIÓN"** (stamps 7/11; the F-07 3-prior-period purchase window's legal root — S3 consumed).
- **Candidate CRs:** vendor-bill/NC period-eligibility engine with declaration-modification overflow (D9 freeze-at-filing interplay by id).
- **Topics:** taxation, fiscal-reporting

## EVID-321 Ley IVA — Art. 64: payable = débito − crédito

- **Loc:** Art. 64 (p. 30, PAGE 30).
- **Verbatim:** "el impuesto que ha de ser pagado … será la diferencia que resulte de deducir del débito fiscal causado en el período tributario, el crédito fiscal trasladado al contribuyente … y, en su caso, el impuesto pagado en la importación o internación definitiva …, en el mismo período tributario."
- **Topics:** taxation

## EVID-322 Ley IVA — Art. 65: deductibility gates, requirements, retention credits

- **Loc:** Art. 65 (pp. 30-32, PAGE 30-32).
- **Verbatim (structure):** Deductible ONLY for: 1) activo realizable goods; 2) activo fijo goods "CUANDO EN ÉSTE CONSERVEN SU INDIVIDUALIDAD Y NO SE INCORPOREN A UN BIEN INMUEBLE"; 3) services in the giro "SIEMPRE QUE NO SE DESTINEN A LA CONSTRUCCIÓN O EDIFICACIÓN DE BIENES INMUEBLES, ASÍ COMO LA RECONSTRUCCIÓN, REMODELACIÓN O MODIFICACIÓN … DE BIENES INMUEBLES" (any modality); 4) gastos generales "TALES COMO FLETES O ACARREOS, ENERGÍA ELÉCTRICA, TELÉFONO O AGUA". All: "DEBERÁN SER INDISPENSABLES PARA EL OBJETO, GIRO O ACTIVIDAD … Y PARA LA GENERACIÓN DE OPERACIONES GRAVADAS … Y QUE POR LO TANTO, GENEREN DÉBITO FISCAL, DE OPERACIONES GRAVADAS CON TASA CERO POR CIENTO, DE DONACIONES … A LAS INSTITUCIONES … ARTÍCULO 6 … ISR Y DE OPERACIONES DE VENTA … A FAVOR DE MISIONES DIPLOMÁTICAS…" (stamps 8/13). Failing the gates ⇒ "DEBERÁN SER DOCUMENTADAS POR MEDIO DE FACTURA" — buyers must NOT request CCF; suppliers obliged to emit FACTURA. Requirements: original CCF with the crédito stated separately OR documentary proof of import IVA; registered in the "LIBRO DE COMPRAS … ARTÍCULO 141 DEL CÓDIGO TRIBUTARIO"; goods purchases also in the "REGISTRO DE CONTROL DE INVENTARIOS … ARTÍCULOS 142 Y 142-A" (stamp 11). **Retentions: CT-162-retained IVA = crédito for the AGENT "EN EL MISMO PERÍODO QUE CORRESPONDA A LA FECHA DE EMISIÓN DEL COMPROBANTE DE RETENCIÓN (CT 112)" and CT-161 anticipo retentions = crédito "AMPARADOS POR EL MANDAMIENTO DE INGRESO" — both "SIEMPRE Y CUANDO SE DECLARE Y ENTERE ÍNTEGRAMENTE EN EL MISMO PERÍODO"** (the F-07 annex-5→casilla-128 post-entero route's Ley root; F5/SR5 consumer). Non-deductible values = ISR cost/gasto if ISR requirements met. "ADQUISICIONES" = local + imports + internaciones.
- **Candidate CRs:** purchase-tax credit-eligibility engine (destination + indispensable + gravada-generation gates); factura-vs-CCF enforcement both directions; retention-credit release gated on same-period entero (ledger tie to F-930/F-07 by id).
- **Topics:** taxation, fiscal-reporting

## EVID-323 Ley IVA — Art. 65-A: non-deductible créditos a)-n); 50% mixed vehicles; fake documents; tarjeta ancho

- **Loc:** Art. 65-A (pp. 32-34, PAGE 32-34).
- **Verbatim (catalog):** a) víveres/alimentos outside food giro (suppliers must emit FACTURA); b) food imports idem; c) vehicles "QUE POR SU NATURALEZA NO SEAN ESTRICTAMENTE INDISPENSABLES" (aut Motores, aviones, helicópteros, barcos, yates, motos acuáticas, lanchas…) + their combustible/lubricantes/repuestos/mantenimiento/seguros (stamps 8/11); d) hotel services + uso/goce of such inmuebles unless business-use shown; e) boletos aéreos except strictly business trips of verifiable employees; f) ropa/joyería/calzado outside giro; g) personal/family-use goods (cónyuge, familiares, directivos, socios…); h) alcohol/cigarettes outside giro; i) crédito traslado above the legal rate; j) general non-indispensables; **k) construction/edification inputs of new inmuebles + reconstruction/remodeling of used ones (whether owner/lessee/usufructuario)**; **l)-n) acquisitions ≥ 58 SALARIOS MÍNIMOS paid: m) NOT by cheque/transfer/card (cash), or n) by non-cash non-bank media without written contract/escritura/CM-law documents (permutas, mutuos de bienes, daciones, cesiones, compensaciones, operaciones contables)** — NOTE: the l)/m)/n) lettering is the printed structure (l introduces, m/n are the two failure modes). Post-catalog: **mixed-use vehicles (giro + extra-giro, evidenced) = deductible "HASTA UN CINCUENTA POR CIENTO (50%)"** + same for their fuel/spare-parts/maintenance/insurance. Unauthorized numbering CCFs = never crédito. Fake/irregular docs 1)-5): unregistered emitter; unproven operation; de-registered (published) subjects; unauthorized correlativos; docs not in the acquirer's name or without proven economic-impact absorption. Criminal-action reservation. Giro = "AQUEL REGISTRADO EN LA ADMINISTRACIÓN TRIBUTARIA … TARJETA DE CONTRIBUYENTE" (identity for all 65/65-A purposes).
- **Candidate CRs:** blocked-credit category matrix; 50%-credit tax code; 58-SMM payment-form gate (SMM feed from payroll/02 by id; the IVA-side kin of ISR 25-SMM — A10 crossref: do not conflate).
- **Topics:** taxation

## EVID-324 Ley IVA — Art. 66: pro-rata (full mechanics)

- **Loc:** Art. 66 (pp. 34-36, PAGE 34-36).
- **Verbatim (structure):** Mixed period ⇒ deductible crédito = "UN FACTOR … DIVIDIENDO LAS OPERACIONES GRAVADAS … ENTRE LA SUMATORIA DE LAS GRAVADAS, EXENTAS Y LAS NO SUJETAS" of the period. Following periods: factor over "LAS OPERACIONES ACUMULADAS DESDE EL PRIMER PERÍODO EN QUE SE APLICÓ LA PROPORCIONALIDAD" through fiscal-year end (even if only gravadas afterwards). **Year-end: "EN EL PRIMER MES DEL EJERCICIO COMERCIAL SIGUIENTE, SE DEBERÁ HACER UN RECÁLCULO … CON LOS VALORES ACUMULATIVOS … DEL EJERCICIO ANTERIOR, Y SE REDISTRIBUIRÁ EL CRÉDITO FISCAL"; excess ⇒ "SE SUMARÁ AL CRÉDITO FISCAL … DEL PRIMER PERÍODO … SIGUIENTE", shortfall ⇒ restado.** Records kept per CT term + exhibition duty. Denominator EXCLUDES: no-sujeta ops of non-habitual activities without attributable credits; donations (Arts. 11/16 final incisos) to ISR-6 entities; **diplomatic sales declared exempt/no-sujetas under ratified instruments (stamp 13)**. NO SUJETAS defined: ops not within hechos generadores or expressly so declared. **"LA PROPORCIÓN DEL CRÉDITO FISCAL QUE CORRESPONDA A LAS OPERACIONES EXENTAS Y NO SUJETAS FORMARÁ PARTE DEL COSTO O GASTO"** (the F-07 casillas 132-134/137-138 pro-rata block's legal root; S3 consumed).
- **Candidate CRs:** monthly accumulated pro-rata engine + January redistribution entry; denominator exclusion flags; blocked→cost reclassification journal.
- **Topics:** taxation, fiscal-reporting

## EVID-325 Ley IVA — Arts. 67-70: carryforward; cessation; non-transferability; IVA not cost

- **Loc:** Arts. 67-70 (p. 36, PAGE 36).
- **Verbatim (key):** Art. 67: credit excess "se sumará al crédito fiscal del período tributario siguiente o sucesivos HASTA SU DEDUCCIÓN TOTAL" (indefinite). Art. 68: cessation ⇒ no devolución/reintegro of remanente; not imputable to other debts nor transferable. Art. 69: crédito non-transferable EXCEPT "continuador de otro por mandato legal" or fusión/absorción continuing the giro; liquidation ⇒ no refund; universal asset/liability aport ≠ transfer of crédito; related-party traspaso banned; heirs get nothing. Art. 70: IVA never cost/gasto (incl. ISR) "salvo cuando los bienes o servicios estén destinados al uso o consumo final, a operaciones exentas o sujetos excluidos".
- **Candidate CRs:** remanente carryforward ledger; merger credit-inheritance flow; cost-reclassification rule mirror of 66.
- **Topics:** taxation

## EVID-326 Ley IVA — Arts. 71-73: fixed-asset transfers (4-year rule); fijo crédito incl. repairs

- **Loc:** Arts. 71-73 (p. 37, PAGE 37).
- **Verbatim (key):** Art. 71 (stamp 11): fixed/capital-asset transfers are NOT hecho generador (no habitualidad) "A MENOS QUE ESA TRANSFERENCIA SE EFECTÚE ANTES DE LOS CUATRO AÑOS DE ESTAR LOS BIENES AFECTADOS A DICHO ACTIVO". Art. 72: their acquisition crédito IS deductible (same or later periods); ALSO deductible: créditos of goods/services for "REPARACIÓN O A SUBSANAR LOS DETERIOROS QUE CORRESPONDEN AL USO O GOCE NORMAL DE LOS BIENES INMUEBLES DEL ACTIVO FIJO, ASÍ COMO LOS DESTINADOS A LA REMODELACIÓN … PARA COLOCARLO EN CONDICIONES DE USO EN EL GIRO DEL NEGOCIO, SIN AUMENTAR SU VALOR O VIDA ÚTIL". Art. 73 (certificados) DEROGADO (stamp 4).
- **Candidate CRs:** asset-sale IVA gate on 4-years-in-service (dated anchor = alta date, D15); repair-vs-improvement credit gate (ties ISR 30 kin; accounting N4 by id).
- **Topics:** taxation

## EVID-327 Ley IVA — Arts. 74-75: export definition; connection carve-out; 0%

- **Loc:** Arts. 74-75 (pp. 37-38, PAGE 37-38).
- **Verbatim (key):** Art. 74: exports = definitive transfers "DESTINADAS AL USO Y CONSUMO EN EL EXTERIOR" + in-country services to non-residents "DESTINADOS A SER UTILIZADOS EXCLUSIVAMENTE EN EL EXTRANJERO". Carve-out (stamp 11): services to non-residents consisting of "LA CONEXIÓN, CONTINUACIÓN O TERMINACIÓN DE SERVICIOS ORIGINADOS EN EL EXTRANJERO" = 13% (Art. 54), NOT 0%. Art. 75: "Las exportaciones estarán afectas a una tasa del cero por ciento." (ZF/DPA TAN-sale routing authority — S7 SR5 by id; LSI cites Arts. 75-77.)
- **Candidate CRs:** export 0% tax + destination/use test (Rgto. Art. 2-10 definition); connected-services 13% classification.
- **Topics:** taxation, special-regimes

## EVID-328 Ley IVA — Art. 76: export crédito deduction and offsets

- **Loc:** Art. 76 (p. 38, PAGE 38).
- **Verbatim (key):** Export-activity credits deductible against internal gravada débito of the same period; excess ⇒ carry to following periods OR "ACREDITARSE CONTRA EL IMPUESTO … RETENIDO, PERCIBIDO O GENERADO EN LAS IMPORTACIONES DE BIENES, OTROS IMPUESTOS DIRECTOS U OBLIGACIONES FISCALES, SIEMPRE QUE ASÍ LO SOLICITARE EL INTERESADO" (stamps 3/14).
- **Candidate CRs:** export credit ledger with offset-request workflow (against retained/perceived IVA, other direct taxes, fiscal obligations).
- **Topics:** taxation, fiscal-reporting

## EVID-329 Ley IVA — Art. 77: reintegro (refund) regime with 13% cap

- **Loc:** Art. 77 (pp. 38-40, PAGE 38-40).
- **Verbatim (key):** Exporter without firm enforceable debts may request REINTEGRO of the remanente; DGII resolution "EN UN PLAZO NO MAYOR DE TREINTA DÍAS"; no prior fiscalización needed; improper claims → penal actions; "EL REINTEGRO NO CONSTITUYE RENTA GRAVABLE". Clock suspends with fiscalización notification covering the periods, resuming at firmeza (stamp 11). Verification: info not provided in the granted term ⇒ "SE DECLARARÁ SIN LUGAR" (re-filable later). Procedure: **a) prove exports + credits with legal documentation; provide at filing "EL DETALLE DE TODAS LAS OPERACIONES DE COMPRAS Y CRÉDITOS FISCALES Y DE VENTAS Y DÉBITOS FISCALES Y EXPORTACIONES … EN MEDIOS MAGNÉTICOS O IMPRESOS" consistent with records; b) declaration filed + not omiso; zero-value declarations must be modified first; c) MIXED exporters: refund only "LA PARTE PROPORCIONAL DEL REMANENTE … VINCULADO A LA EXPORTACIÓN", percentage = exports / total gravada ventas, "EL CUAL NO PODRÁ EXCEDER DEL TRECE POR CIENTO (13%) DEL VALOR DE EXPORTACIÓN QUE CONSTE EN LOS DOCUMENTOS ADUANEROS"; d) pure exporters: total credits, same 13% cap; e) unrefunded excess over the cap "PODRÁN ACUMULARSE A LOS CRÉDITOS FISCALES DE LOS SIGUIENTES PERÍODOS"** under c)/d) math. Reglamento sets requirements/documentation/plazos (Rgto. Art. 30).
- **Candidate CRs:** refund-request workflow with 30-day clock, suspension events, omiso gate, mixed/pure cap computation (13% of export value), accumulation ledger (F-07 casillas 523/524/115 consumer by id).
- **Topics:** taxation, fiscal-reporting

## EVID-330 Ley IVA — Arts. 81, 93-94: no facilities; monthly declaración; 10 días hábiles; import liquidation venues

- **Loc:** Art. 81 (pp. 40-41, PAGE 40-41); Arts. 93-94 (pp. 42-43, PAGE 42-43).
- **Verbatim (key):** Art. 81-I: oficio liquidations pay within DOS MESES of firme resolution; II: "Respecto del presente impuesto NO PROCEDEN PRÓRROGAS NI FACILIDADES O PLAZOS DIFERIDOS para su pago." Art. 93: "EL PERÍODO TRIBUTARIO SERÁ DE UN MES CALENDARIO"; monthly declaración jurada covering gravadas/exentas/no sujetas + monthly débito + crédito + "LOS REMANENTES DE ÉSTE TRASPASADOS DE PERÍODOS ANTERIORES"; forms from DGII. Art. 94: declaration includes payment, at DGII/Tesorería/authorized banks, "DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES DEL MES SIGUIENTE"; same lap for agent retentions/perceptions; goods imports: liquidated at Aduanas with customs taxes, "LA CONSTANCIA DEL PAGO DE ESTE IMPUESTO CONSTITUIRÁ EL COMPROBANTE DE CRÉDITO FISCAL"; oficio-liquidation of goods imports = Aduanas, paid at Tesorería; **services imports: liquidated at DGII, paid at Tesorería** (stamp 8).
- **Candidate CRs:** F-07 monthly engine consumers (S3 by id); import-payment-constancy as credit document; días-hábiles engine feed (SV-FREP-FR-202..204 by id).
- **Topics:** taxation, fiscal-reporting

## EVID-331 Ley IVA — Arts. 165, 167-A, 173-175: incorporation note; kill-switch; derogations incl. Art. 174 generic-exemption nullity

- **Loc:** Arts. 165/167-A (pp. 51-52, PAGE 51-52); Arts. 173-175 (pp. 52-55, PAGE 52-55).
- **Verbatim (key):** Art. 165: the 7-m/17-p/q/final + 65-A-c/fourth regulations "SE INCORPORAN PARA EFECTOS DE FACILITAR … Y NO CONSTITUYEN NUEVOS HECHOS GENERADORES". Art. 174: "Las exenciones tributarias genéricas, totales o parciales otorgadas o que se otorguen por otras leyes … EXCEPTUANDO LAS AMPARADAS POR LA LEY DE IMPRENTA, NO PRODUCIRÁN NINGÚN EFECTO EN RELACIÓN CON ESTE IMPUESTO" — IVA exemptions live in this law (or specific treaties) only; other laws' generic exemptions are inert. Art. 173 repeals the stamp-tax family; D.L. 634-1993 interpretación auténtica embeds repealed-law sanctions for pre-vigencia acts. Art. 175: vigencia 1-sep-1992.
- **Candidate CR:** exemption source gate — only Arts. 45/46 (or international instruments) may exempt; config rejects foreign-law exemption claims.
- **Topics:** taxation

## EVID-332 Reglamento IVA — identity + repeal map (D.E. 117-2001) + stale anchors

- **Loc:** title (Rgto. PAGE 1); REFORMAS block (Rgto. PAGE 11).
- **Verbatim:** "REGLAMENTO DE LA LEY DE IMPUESTO A LA TRANFERENCIA DE BIENES MUEBLES Y A LA PRESTACION DE SERVICIOS. DECRETO Nº 83" (22-sep-1992, D.O. 174 T.316 same day); "REFORMAS: (1) D.E. Nº 60, del 7 de junio de 1993 …; (2) D.E. Nº 10, del 2 de febrero de 1996 …; (3) D.E. N° 117, del 11 de diciembre del 2001, D.O. N° 234, Tomo 353, del 11 de diciembre del 2001."
- **Gloss:** the SAME D.E. 117-2001 mass repeal as the ISR Reglamento (R17 kin): survivor articles = 1-10, 16-30, 50-51 (+ 52 vigencia); everything else chapter-marked DEROGADO (3). **R17-bis ruling candidate: Reglamento IVA provenance = D.E. 83-1992 consolidated incl. 60-1993/10-1996/117-2001; repeal authority = D.E. 117-2001, not the CT.** Stale anchors inside survivors, cite-with-note only: Art. 22 → "artículo 107 de la ley" (derogated; now CT 141); Art. 23 → "artículo 34 de la ley" (derogated; now CT 161-162 zone); **Art. 29 → D.L. 461-1990 ZF/recintos law (superseded by D.L. 405-1998 = 12_; the export-equivalence substance survives via 12_ Art. 25 + Ley IVA 76/77, S7 by id)**.
- **Topics:** taxation

## EVID-333 Reglamento — Art. 2 definitions (customs + asset vocabulary)

- **Loc:** Rgto. Art. 2 (Rgto. PAGE 1-3).
- **Verbatim (selected):** 10) Exportación: "envío legal de mercancías en libre circulación para su uso o consumo definitivo en el exterior y la prestación de servicios en el país a usuarios sin domicilio ni residencia … utilizados exclusivamente en el exterior"; 11) Importación Definitiva (incl. "utilización de servicios procedentes del exterior"); 12) Internación Definitiva (originating in Tratado General de Integración Económica Centroamericana signatories); 15) Regímenes Aduaneros Especiales: a) zonas francas; b) importación temporal/reexportación mismo estado; c) recintos o depósitos fiscales/aduaneros; d) tiendas libres; e) **admisión temporal para perfeccionamiento activo** ("recibir … con suspensión de derechos … destinadas a ser devueltas … después de un proceso de transformación, elaboración o reparación"); f) tránsito aduanero (stamp 1); 16)-18) objeto social / giro / activo-en-giro ("excluyéndose las pérdidas y demás cuentas … sólo para efectos contables"); 19) Activo Realizable; 20) Activo Fijo; 21) Precio Corriente de Mercado ("negocios o establecimientos similares ubicados en el mismo sector, localidad o departamento").
- **Candidate CRs:** asset-classification vocabulary consumed by 65/65-A/71 gates; customs-regime taxonomy (SR4/SR6 kin by id).
- **Topics:** taxation, special-regimes

## EVID-334 Reglamento — Arts. 4-8: retiro extensions; fuerza-mayor proof; service definitions; desechos

- **Loc:** Rgto. Arts. 4-8 (Rgto. PAGE 3-5).
- **Verbatim (key):** Art. 4: retiro use/consumption includes "el grupo familiar de ellos y los terceros"; NOT taxed: realizable goods' own use "necesarios para el giro o actividades normales" + realizable→fijo transfers; fuerza mayor = "el imprevisto que no es posible resistir, como una inundación, terremoto, incendio, accidente, robo, merma, etc." proven by: a) "Anotaciones cronológicas … en el sistema de inventario permanente, directamente relacionado con la contabilidad"; b) denuncias to policía/tribunal; c) insurance-liquidation reports; d) "Mermas reconocidas por disposiciones legales vigentes u organismos técnicos gubernamentales" — plus the accounting precondition "en las fechas que se produjo la pérdida…". Art. 5: self-used services include family/third parties. Art. 6: a) continuous/periodic services = CC L.IV T.IV suministro; b) empresa mercantil; c) administración/mandato services = solo trabajo físico o intelectual; d) precio alzado = materials+services+equipment included; e) contrato general de construcción (≥2 especialidades, obra civil); f) instalación/confección de especialidades; g)-i) comisión/mandato/consignación definitions. Art. 7: a) acredita-en-cuenta = "por medio de una operación contable … a la cuenta corriente … o por medio de un reconocimiento escrito"; b)-c) opción de compra vs promesa de venta contracts. Art. 8: **desechos/desperdicios/residuos transferors ARE contribuyentes** (obtained from production or not).
- **Candidate CRs:** retiro-exemption evidence menu; residual/scrap product line flagged IVA-contribuyente.
- **Topics:** taxation

## EVID-335 Reglamento — Arts. 9-10, 16-18: exclusion concurrence; opción evidence; exención calification; residual value; aduana FX

- **Loc:** Rgto. Arts. 9-10, 16-18 (Rgto. PAGE 5-6).
- **Verbatim (key):** Art. 9: exclusion requires "CONCURRIR LOS DOS REQUISITOS … ARTÍCULO 28 DE LA LEY". Art. 10: opción evidence = "el libro de gastos, conpras [sic] y ventas, autorizado por el Registro de Comercio" + "un inventario valorado de bienes" (or DGII means). Art. 16: exemption calification with technical doubt ⇒ informe of the competent authority. Art. 17: residual value = "el valor de la última cuota o de una adicional … pactado"; tax caused per renta periódica + residual. Art. 18: aduanero value in foreign currency converts "AL TIPO DE CAMBIO DEL DÍA DE ACEPTACIÓN DE LA PÓLIZA DE IMPORTACIÓN O DEL FORMULARIO ADUANERO CORRESPONDIENTE" (DUCA-acceptance kin, SOQ-45 kin).
- **Topics:** taxation, special-regimes

## EVID-336 Reglamento — Arts. 19-26: import credit docs; retiro factura; gastos generales; agent-retention credit; remanente; crédito-not-cost; fijo docs

- **Loc:** Rgto. Arts. 19-26 (Rgto. PAGE 6-7).
- **Verbatim (key):** Art. 19: importer credit proven by "LA PÓLIZA DE IMPORTACIÓN O FORMULARIO ADUANERO Y EL RESPECTIVO RECIBO DE PAGO". Art. 20: retiros/autoconsumo "deberá emitirse la Factura correspondiente COMO CONSUMIDOR FINAL" (Ley 58's operative echo). Art. 21: gastos generales útiles/necesarios = "indispensables para el funcionamiento del negocio … relación directa con su objeto, giro o actividad". Art. 22: duly registered = "anotado oportunamente en el Libro o Registro de Compras" (stale ref to Ley 107 — see EVID-332). Art. 23: agent-retained amounts = crédito "EN EL MISMO PERÍODO TRIBUTARIO, SIEMPRE QUE SE HAYAN INGRESADO ÍNTEGRAMENTE AL FISCO" (CT-162 side); CT-161-kin amounts via "MANDAMIENTO DE INGRESO Y EL RECIBO" (stale ref to Ley 34 — see EVID-332). Art. 24: remanente definition (carry to following periods). Art. 25: crédito not part of cost "SALVO … DESTINADOS A OPERACIONES EXENTAS O NO GRAVADAS"; unusable crédito (pro-rata 66 or cessation) "PASARÁ A CONSTITUIR UN GASTO GENERAL". Art. 26: taxable fixed-asset transfers ⇒ Factura o CCF; non-taxable (Art. 71) ⇒ "CUALQUIER OTRO TIPO DE DOCUMENTO".
- **Candidate CRs:** import-credit document pair (DUCA + payment receipt) validation; asset-sale document routing by taxability.
- **Topics:** taxation

## EVID-337 Reglamento — Arts. 29-30: ZF exports = exports (D.L. 461 anchor, stale); reintegro bookkeeping

- **Loc:** Rgto. Arts. 29-30 (Rgto. PAGE 8).
- **Verbatim (key):** Art. 29 (stamp 1): per D.L. 461-1990 Art. 26, "SE CONSIDERARÁ COMO EXPORTACIÓN la transferencia de dominio definitivo de bienes muebles corporales y la prestación de servicios destinados al uso y consumo de las empresas acogidas al Régimen de Zonas Francas y Recintos Fiscales", documented "MEDIANTE LA PÓLIZA DE EXPORTACIÓN O DECLARACIÓN DE MERCANCÍAS" + accompaniment docs. **Art. 30 (stamps 1/2): refund request "PREVIA PRESENTACIÓN DE LA DECLARACIÓN DEL PERÍODO"; requests complete per DGII Instructivos; separate purchase-ledger registration of export vs local credits, commons "SE DISTRIBUIRÁN PORCENTUALMENTE … EN RELACIÓN A LAS VENTAS QUE CADA UNA HAYA GENERADO" monthly; local exempt ventas ⇒ records per Ley Art. 66; "ÚNICAMENTE PROCEDERÁ LA DEVOLUCIÓN RESPECTO AL PERÍODO TRIBUTARIO DE LA EXPORTACIÓN"; fehaciente verification duty on demand.**
- **Gloss:** the D.L. 461 anchor is stale-as-printed (superseded by 12_ D.L. 405-1998; S7 SR5 encoded the current ZF/DPA routing); the export-equivalence SUBSTANCE remains the operative reglamento rule for ZF-family sales documentation (SR5 by id).
- **Candidate CRs:** export/local/common credit ledger split (three-way) + monthly percentage distribution; per-period-only refund rule.
- **Topics:** taxation, special-regimes

## EVID-338 Reglamento — Arts. 50-51: transitory inventory credit (1992, historical); pre-1992 contracts

- **Loc:** Rgto. Arts. 50-51 (Rgto. PAGE 10).
- **Verbatim (key):** Art. 50: 168-III inventory credit in "DUODÉCIMAS PARTES durante los doce períodos tributarios de vigencia del impuesto" (1992 transitory — HISTORICAL, is_historical ingestion kin only); exporters may add undeductible duodécimos to same-period credits. Art. 51: pre-1-sep-1992 contracts taxed "POR AQUELLA PARTE QUE NO ESTUVIERE PERFECCIONADA"; parties free to adjust otherwise.
- **Gloss:** both transitory to the 1992 cutover; encode only as historical notes (D18 kin), zero operative FRs.
- **Topics:** taxation (historical)

## W15 open questions (S9-prep; fold into master-index SOQ register as SOQ-54+)

1. **OQ (SOQ-54 candidate):** 01_ consolidation vintage — last reform stamp D.L. 71-2015; no later official consolidation acquired. Corpus-internal signals negative for post-2015 substantive reforms (DTE stack, Quincena-25, F-07 v14 manual all silent), but SOQ-22/30-kin verification watch must ride every 01_/02_ LB until a current consolidation is acquired (acquisition candidate ≥75, asamblea/D.O. recovery watch).
2. **OQ (MOQ-03 resolution):** Art. 28 colones thresholds — historical text as printed; administered exclusion criteria (NRC/registration practice) not in corpus. Encode regime + [sic] thresholds + config-gap; no USD conversion invented (S5 ruling 39 discipline). RESOLVES MOQ-03.
3. **OQ:** Art. 46-f BCR-qualification instrument (for foreign-institution deposit/loan interest exemption) absent — config-gap.
4. **OQ:** Art. 46-k cites the SAP law (D.L. 927-1996) — superseded by D.L. 614 (R24); exemption substance for pension-administration commissions assumed carried; re-verify under SIP regime (R23 kin).
5. **OQ:** Art. 167-A kill-switch instrument (régimen de políticas sectoriales) not in corpus — watch row for the 45-h water/alcantarillado exemption.
6. **OQ:** Decreto 321 differentiated fuel rates (S3 05 OQ-001 kin) — the dated-regime VALUES stay a fiscal-reporting-side config gap; IVA-core encodes only the base/casilla mechanics (by id).
7. **OQ (SOQ-40 design-pass input):** FOVIAL/COTRANS — Ley-side anchors now fully in evidence (Arts. 2 + 51-d + 47/48-a via 31_ guide); the B2B-chain→DTE-tributo mapping design lands in this wave as FRs; COTRANS instrument still absent (MOQ-04 half-open).
8. **OQ:** Rgto. stale anchors (Arts. 22/23/29 → derogated Ley 107/34 + superseded D.L. 461) — cite-with-note rule (R17-bis).

