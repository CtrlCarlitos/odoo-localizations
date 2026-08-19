# Evidence — 13_SAR-619 + 14_SAR-238 + 15_DEI-276 + 16_CPAT-073 + 17_SAR-343 + 18_DEI-279 + 19_SAR-240 + 20_SAR-237 (W2a fiscal-reporting procedures)

Sources: `hn/sources/13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf` (SAR-619-2024, 16-dic-2024, La Gaceta 36,725, 27-dic-2024; gazette extract pp.2-4 = the acuerdo, pp.1/unrelated = CAF-loan Acuerdo 176-2022/626-2024), `14_Acuerdo_SAR-238-2024_DJIMR.pdf` (SAR-238-2024, 10-may-2024, La Gaceta 36,538, 20-may-2024), `15_Acuerdo_DEI-SG-276-2015_DMC.pdf` (DEI-SG-276-2015, 03-dic-2015, La Gaceta print header reads **33,955** 9-feb-2016 [catalog said 33,995 — see OQ-3]; scanned, OCR'd), `16_Acuerdo_CPAT-SG-073-2016_DMC_mod.pdf` (CPAT-SG-073-2016, 16-ago-2016, La Gaceta 34,127, 1-sep-2016), `17_Acuerdo_SAR-343-2019_DMC_reforma.pdf` (SAR-343-2019, 22-jul-2019, La Gaceta 35,014, 5-ago-2019; extract also carries unrelated Acuerdo Ministerial 064-2019 maíz blanco), `18_Acuerdo_DEI-SG-279-2015_compras_eventuales.pdf` (DEI-SG-279-2015, 17-dic-2015, La Gaceta 33,991, 22-mar-2016), `19_Acuerdo_SAR-240-2024_ISV_tarjetas_mod.pdf` (SAR-240-2024, 10-may-2024, La Gaceta 36,538, 20-may-2024), `20_Acuerdo_SAR-237-2024_retenciones_mod.pdf` (SAR-237-2024, 10-may-2024, La Gaceta 36,538, 20-may-2024).
Read: 2026-08-20 (W2a). All eight read end-to-end (4+5+3+2+2+4+4+4 pp).
Citation form: 619-`<ordinal>` (p.x); 238-`<ordinal>`; 276-`<ordinal/numeral>`; 073-`<ordinal>`; 343-`<ordinal>`; 279-`<ordinal/numeral>`; 240-`<numeral/ordinal>`; 237-`<ordinal>`.
EVID numbering: HN corpus-global, continues (072 here onward).

---

## EVID-072 13_ — EEFF-prior gate on the ISR declaration, from FY2024 (619-PRIMERO/SEGUNDO/TERCERO, p.4)

- **Loc:** 619-PRIMERO, SEGUNDO, TERCERO (p.4).
- **Verbatim:** PRIMERO: "Que la Declaración Jurada del Impuesto Sobre la Renta requerirá a partir del período fiscal 2024, la presentación previa del 'Informe de Estado de Situación Financiera', integrado por el Balance General y Cuadros de Ganancias y Pérdidas. Para los períodos fiscales anteriores al 2024 no es obligatoria la presentación del Informe ... previo a la presentación de la Declaración Jurada ... cuando se trate de una declaración jurada omisa o rectificativa." SEGUNDO: obligados = "las personas jurídicas y las personas naturales declaradas como comerciantes individuales". TERCERO: elaboración/presentación "a través de la Oficina Virtual o por los medios que proporcione el Servicio de Administración de Rentas".
- **Gloss:** HN's sequence gate: the EEFF inform (Form 535) must be filed BEFORE the ISR DJ for FY2024+; the prior-years carve-out applies only to omisa/rectificativa filings (late/original annual DJs for ≤FY2023 need no EEFF). D16 kin: a filing-order dependency between two annual forms — the DJ submission engine must model "prerequisite form" edges, not just deadlines.
- **Candidate CRs:** EEFF-before-DJ sequence gate (FY2024+); omisa/rectificativa ≤FY2023 EEFF exemption flag.
- **Topics:** fiscal-reporting

## EVID-073 13_ — EEFF inform: annual window + complement nature + form 535 chain (619-CUARTO/QUINTO, considerando SAR-236, pp.3-4)

- **Loc:** 619-CUARTO, QUINTO (p.4); considerando citing Acuerdo SAR-236-2024 (p.3).
- **Verbatim:** CUARTO: "periodicidad anual y debe presentarse del uno (01) de enero al treinta (30) de abril de cada año. Para las personas jurídicas y personas naturales constituidas como comerciantes individuales con periodo fiscal especial, el vencimiento se establece en los tres (3) meses siguientes al cierre de su ejercicio fiscal." QUINTO: "constituye el complemento de la Declaración Jurada de Impuesto Sobre la Renta, siendo ambos formularios una misma obligación, por lo que, la no presentación del Informe ... dará lugar al incumplimiento de la obligación de presentación de la Declaración Jurada antes referida y sus obligaciones conexas." Considerando: Acuerdo No. SAR-236-2024 (10-may-2024) aprobó el Formulario "535 - Informe de Estado de Situación Financiera", "a través de la Oficina Virtual como única modalidad", complemento de la DJ ISR for empresas mercantiles, "en el cual se deberá informar lo contenido en el Balance General y Cuadros de Ganancias y Pérdidas".
- **Gloss:** the inform = Form **535** (code matches Ayuda `67_`); window Jan-1→Apr-30 (special-FY: 3 months post-close); legally the SAME obligation as the ISR DJ (non-filing of 535 = non-filing of the DJ — sanction engine treats them as one). Statutory anchors quoted in considerandos: ISR Art. 28 (DJ + Balance/GyP certified by contador hondureño titulado o incorporado) + Reglamento Ley ISR Art. 84 (see OQ-2) + Ley Equidad Tributaria Art. 7 (see EVID-075).
- **Candidate CRs:** annual Form-535 calendar row (Jan-1→Apr-30; special-FY +3m); single-obligation enforcement flag (535-missing ⇒ DJ-nonfiled).
- **Topics:** fiscal-reporting

## EVID-074 13_ — publication/vigencia mechanics + print defects (619-SÉPTIMO/NOVENO, p.4)

- **Loc:** 619-SÉPTIMO, NOVENO (p.4).
- **Verbatim:** SÉPTIMO: promulgación "a través de su publicación en el Diario Oficial 'La Gaceta' y en el portal electrónico" (CT Art. 13.4 dual-publication doctrine recited in considerandos: portal publication + gazette aviso). NOVENO: "entra en vigencia a partir de su publicación" (27-dic-2024). Resolutivo numbering prints SEXTO → SÉPTIMO → NOVENO — **OCTAVO absent from the print [sic]**.
- **Gloss:** CT 13.4's dual promulgation pattern (portal + gazette aviso) is the standing form-vigencia mechanism for every SAR form approval — the forms-catalog FR family should encode it. Print defect noted, no substantive loss.
- **Candidate CRs:** (pattern-level: portal-publication vigencia rows for form approvals).
- **Topics:** fiscal-reporting

## EVID-075 13_ — new leads surfaced: impuesto al activo neto 1% (Ley Equidad Tributaria) + Reglamento Ley ISR Art. 84 (619-considerandos, pp.2-3)

- **Loc:** considerandos citing Ley de Equidad Tributaria Art. 7 and Reglamento de la Ley ISR Art. 84 (pp.2-3).
- **Verbatim:** "el Artículo 7 de la Ley de Equidad Tributaria establece la tasa del Impuesto al Activo Neto el cual será del uno por ciento (1.0%) sobre el valor del activo total neto determinado en el Balance General." / "el Artículo 84 del Reglamento de la Ley de Impuesto Sobre la Renta establece que el Servicio de Administración de Rentas determinará la forma y requisitos con que el contribuyente debe formular su declaración, y preparará y pondrá a disposición del contribuyente oportunamente, los formularios correspondientes."
- **Gloss:** TWO authority gaps surface: (1) **Ley de Equidad Tributaria NOT in corpus** — source of the 1% activo neto (the tax behind Ayuda `30_`'s "Activo Neto y Aportación Solidaria PJ" código 103 declaration); acquisition candidate ≥105. (2) **Reglamento Ley ISR Art. 84** — third independent citation of the modern Reglamento (plantilla's Art. 51; W1f) yet the instrument remains unlocated (RESEARCH §5 lead 12). The quote also shows the Reglamento delegates form/format to SAR — consistent with the CT 13.4 pattern.
- **Topics:** fiscal-reporting, taxation

## EVID-076 14_ — DJIMR system: per-código monthly informativa replacing the DMR (238-PRIMERO/SEGUNDO/TERCERO, pp.3-4)

- **Loc:** 238-PRIMERO, SEGUNDO, TERCERO (pp.3-4).
- **Verbatim:** PRIMERO: "Establecer un sistema automatizado para que los Agentes de Retención informen a la Administración Tributaria el detalle de las retenciones efectuadas a terceros, mediante la 'Declaración Jurada Informativa Mensual de Retenciones (DJIMR)', que proporcionará la determinación de la obligación de presentar y pagar el tributo en la Declaración Jurada Determinativa de los impuestos retenidos." SEGUNDO: deadline "dentro del plazo de los primeros diez (10) días calendarios del mes siguiente al que se efectuó la retención." TERCERO: "deben elaborar y presentar una ... DJIMR **por cada código de impuesto de retención**, y ésta a su vez, proporcionará la información en su declaración determinativa y la de terceros."
- **Gloss:** the retenciones reporting pipeline (D.L. 66-2015 Art. 2 DMR 10-day rule carried forward): one informativa PER retention code per month, feeding both the agent's own determinativa and SAR's third-party cross-check (the "información de terceros" = SAR credits the retained-against tax to the retenido's account). Kin to SV F-910/F-07 annex engines. Deadline = first 10 días calendario.
- **Candidate CRs:** monthly per-código DJIMR generator keyed on retention moves; third-party attribution ledger (retenido ↔ retention record) feeding consulta-retenciones surfaces.
- **Topics:** fiscal-reporting, taxation

## EVID-077 14_ — the 25-code DJIMR catalog (238-CUARTO, pp.3-4)

- **Loc:** 238-CUARTO (pp.3-4), list items 1-25.
- **Verbatim:** "Las retenciones que se informen en cada una de las DJIMR, serán conforme a los siguientes Códigos de Impuestos: 1) DJIMR-111 Retención en la Fuente Asalariados; 2) DJIMR-112 Retención por Servicios, Honorarios, y otros (Art. 50); 3) DJIMR-113 Retención por Dividendos o Utilidades Distribuidas (Art. 25); 4) DJIMR-115 Retención por Intereses y Rendimientos Financieros (Art. 9); 5) DJIMR-116 Retención por Impuesto a las Ventas (Sólo Sector Público); 6) DJIMR-118 Retención a Contribuyentes en Mora; 7) DJIMR-122 Retención Renta de Bienes Muebles e Inmuebles (Art. 5 ISR); 8) DJIMR-123 Retención por Ingresos de Espectáculos Públicos (Art. 5 ISR); 9) DJIMR-124 Retención por Salarios, Comisiones por Servicios (Art. 5 ISR); 10) DJIMR-125 Retención por Regalías por Marcas de Patentes y Similares (Art. 5 ISR); 11) DJIMR-126 Retención por Intereses sobre Operaciones Comerciales (Art. 5 ISR); 12) DJIMR-127 Retención por Películas, Videos, Cines, Televisión (Art. 5 ISR); 13) DJIMR-128 Retención por Primas de Seguros y Similares (Art. 5 ISR); 14) DJIMR-129 Retención por Renta obtenida por Empresas Extranjeras (Art. 5 ISR); 15) DJIMR-130 Retención por Utilidades y Dividendos (Art. 5 ISR); 16) DJIMR-131 Retención por Regalías por canteras, minas y similares (Art. 5 ISR); 17) DJIMR-132 Retención por Operaciones de naves aéreas, marítimas y autos (Art. 5 ISR); 18) DJIMR-133 Retención por Ingresos empresas de comunicaciones (Art. 5 ISR); 19) DJIMR-134 Otras Retenciones diferentes a las anteriores (Art. 5 ISR); 20) DJIMR-135 Retención Anticipo ISR o ATN (1%); 21) DJIMR-136 Retención Impuesto Cedular sobre Alquiler Habitacional (10%); 22) DJIMR-137 Retención Impuesto Sobre Ganancias de Capital (10%); 23) DJIMR-138 Ganancias de Capital a No Residentes; 24) DJIMR-217 Retenciones Artículo 8 (ISV); y, 25) DJIMR-254 Retención Venta Boletos de Lotería Electrónica, Rifas y Sorteos."
- **Gloss:** the authoritative retention-code catalog — the join key between retention moves, monthly informativas, and SAR's third-party records. Codes 118/122-134/254 have NO dedicated Ayuda in the corpus (122-134 = the ISR Art. 5 non-resident/renta-de-capital retention family; 118 = mora retention; 254 = electronic lottery). Note ABSENCE of 215/523 (tarjetas) and 136 appears here as "Impuesto Cedular ... Alquiler Habitacional (10%)" — see OQ-4 on the tarjetas-coverage question.
- **Candidate CRs:** retention-code reference data (25 rows, this EVID as LB) wired to retention tax rules; DJIMR-coverage completeness check per month (no empty-code filings; only codes with movements).
- **Topics:** fiscal-reporting, taxation

## EVID-078 14_ — modality rules: one modality, same-modality rectification (238-QUINTO/SEXTO, pp.4-5)

- **Loc:** 238-QUINTO, SEXTO (pp.4-5).
- **Verbatim:** QUINTO: DJIMR "podrán presentarse a través de Servicio Web u Oficina Virtual; no obstante, los obligados tributarios deberán implementar una sola modalidad." SEXTO: rectifications per CT periodicity; "deberán ser rectificadas haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original".
- **Gloss:** channel stickiness: pick one channel per taxpayer, rectify on the same channel. For Odoo thin-client (which exports/files via one integration) this is a configuration constraint on the filing channel, not a computation rule — but the same-modality rectification constraint belongs in the filing-engine FRs.
- **Candidate CRs:** filing-channel single-modality config + rectification channel enforcement.
- **Topics:** fiscal-reporting

## EVID-079 14_ — rectificativa consequences: SAR auto-rectifies the determinativa (238-SÉPTIMO, p.5)

- **Loc:** 238-SÉPTIMO (p.5).
- **Verbatim:** "Las Declaraciones Rectificativas de las DJIMR originales, tendrán una vinculación directa con su Declaración Jurada Determinativa, es decir, que las modificaciones incorporadas en éstas, darán como resultado declaraciones rectificativas de las Declaraciones Juradas Determinativas **de oficio por parte del Servicio de Administración de Rentas**, quedando en estado aceptada cuando el valor del impuesto a pagar sea mayor al consignado en la declaración anterior, caso contrario, quedará la declaración rectificada en estado rechazo."
- **Gloss:** informativa rectifications propagate INTO the determinativa automatically (SAR-side): accepted only when they increase tax payable, otherwise rejected. Client-side consequence (D16 ¶5 freeze kin): after a DJIMR rectification, the taxpayer's determinativa snapshot is superseded by SAR's de-oficio rectification — the Odoo side must track the extern rectification state and reconcile the frozen snapshot (import the SAR-rectified determination rather than assume the original stands).
- **Candidate CRs:** DJIMR-rectification → determinativa-supersession state import; accepted/rechazo state sync.
- **Topics:** fiscal-reporting

## EVID-080 14_ — DMR→DJIMR chain + omisas + repeal (238-NOVENO/DÉCIMO PRIMERO, considerandos, pp.2-3,5)

- **Loc:** considerandos (DEI-SG-155-2011, SAR-007-2017, D.L. 66-2015 Art. 2), 238-NOVENO, DÉCIMO PRIMERO (pp.3, 5).
- **Verbatim:** D.L. 66-2015 Art. 2: DMR "a más tardar dentro de los diez (10) días calendarios del mes siguiente en que se efectuó la retención". History: DEI-SG-155-2011 (27-jul-2011) approved the DET-MR module → "Declaración Jurada Informativa DEI-540"; SAR-007-2017 (01-jun-2017) temporarily kept CPAT-era formats. NOVENO: "Las Declaraciones Mensuales de Retenciones (DMR) que no se presentaron en el plazo establecido y que, al entrar en vigencia este acuerdo se encuentren omisas, se deben presentar a través de la Oficina Virtual mediante la DJIMR." DÉCIMO PRIMERO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo DEI-SG-155-2011".
- **Gloss:** instrument chain: DEI-540/DET (2011) → DMR (D.L. 66-2015) → **DJIMR (2024, current)**; the DMR label survives colloquially (Ayuda `71_` still titled "Generalidades DMR"). Historical DMR-period imports (go-live reconciliation, D-H3) resolve to the DMR regime; post-May-2024 months file DJIMR per código.
- **Candidate CRs:** declaration-regime dated rows (DMR pre-2024 / DJIMR post-2024-05-20); omisas-DMR migration path note.
- **Topics:** fiscal-reporting

## EVID-081 15_ — DMC creation: sujetos + all-compras scope (276-PRIMERO/SEGUNDO numeral 1, pp.2-3)

- **Loc:** 276-PRIMERO, SEGUNDO-numeral 1 (pp.2-3).
- **Verbatim:** PRIMERO: "Formular un sistema automatizado de fiscalización de compras que regule el Impuesto Sobre Ventas, creando la Declaración Jurada Informativa denominada 'Declaración Mensual de Compras del Impuesto Sobre Ventas (DMC)', generada por el módulo informático ... que forma parte del Sistema de Declaración Electrónica de Tributos (DET LIVE)." Numeral 1 SUJETOS OBLIGADOS: "todos los sujetos pasivos obligados a la presentación y/o pago de la Declaración del Impuesto Sobre Ventas, clasificados como grandes o medianos contribuyentes incluyendo los acogidos a Regímenes Especiales y demás contribuyentes que ejerzan operaciones comerciales exentas, deben informar todas las compras realizadas en el mercado interno y sus importaciones gravadas y no gravadas con el Impuesto Sobre Ventas, efectuadas en el mes".
- **Gloss:** the purchases informativa (SV F-07 purchases-annex kin): scope = grandes/medianos + special regimes + exempt operators; content = ALL purchases (taxed or not, local + imports) of the month. Grandes/medianos classification is a SAR taxpayer-segment attribute the Odoo side needs as company config.
- **Candidate CRs:** taxpayer-segment config (grande/mediano/pequeño); DMC monthly all-purchases export (local + import, gravada/exenta/ no gravada mix).
- **Topics:** fiscal-reporting

## EVID-082 15_ — DMC forma + original plazo + credit-fiscal validation purpose + 030-2012 chain (276-SEGUNDO numerales 2-4, TERCERO/CUARTO, pp.2-3)

- **Loc:** 276-SEGUNDO numerales 2-4, TERCERO, CUARTO (pp.2-3); considerandos (pp.2).
- **Verbatim:** Numeral 2 FORMA: DEI "facilitará ... el formulario incorporado en el anexo 1"; "deben separar al momento de presentar la misma, las compras que generan Crédito Fiscal de las que son incluidas en los costos y/o gastos de su contabilidad"; presentation "mediante el portal electrónico DET LIVE". Numeral 3 PLAZO (original text): "antes de la Declaración Determinativa del Impuesto Sobre Ventas dentro de los primeros diez (10) días calendarios del mes siguiente en que se efectuaron las compras internas o las importaciones"; first filing "en los primeros diez (10) días del mes de marzo de 2016". Numeral 4 SANCIONES: CT + recibo oficial de pago. TERCERO: FY2015 obligation stays under Acuerdo DEI-SG-030-2012. CUARTO: "queda sin valor y efecto el Acuerdo No. DEI-SG-030-2012" (19-mar-2012, La Gaceta 32,834, 31-may-2012 — the "Declaración Anual de Créditos del ISV", form DEI-525).
- **Gloss:** PURPOSE stated in considerandos: DMC = "insumos a la Administración Tributaria para una validación automática del crédito fiscal, costos y gastos" — SAR cross-validates the ISV credit claimed on the determinativa against supplier-side detail. The crédito-fiscal vs costos/gastos split is the core data-shape requirement. Pre-2016 history = ANNUAL credits declaration (DEI-525).
- **Candidate CRs:** DMC line model with crédito-fiscal/costo-gasto dichotomy; supplier-invoice detail (RTN, doc, base, ISV) per line; validation-report delta surface vs determinativa credit.
- **Topics:** fiscal-reporting

## EVID-083 16_ — DMC deadline 10→20 days (day-10 decongestion); later repealed (073-PRIMERO, p.2)

- **Loc:** 073-PRIMERO (p.2); considerando on day-10 saturation (p.2).
- **Verbatim:** Considerando: "el día diez (10) de cada mes se produce el vencimiento del plazo para la presentación de la Declaración del Impuesto Sobre Ventas, Declaración Mensual de Retenciones (DMR) y Declaración Mensual de Compras (DMC) ... saturación de nuestros sistemas informáticos". PRIMERO modifies numeral 3 to read: "dentro de los primeros veinte (20) días del mes siguiente en que se efectuaron las compras internas o las importaciones".
- **Gloss:** interim regime (Sep-2016 → May-2024): DMC day-20. IMPORTANT side-fact: **the ISV determinativa + DMR + DMC all fell on day 10** at 2016 — establishing the ISV monthly determinativa deadline anchor (day 10) corroborated by `43_`/`69_` Ayudas at W2b. This 20-day text was later repealed by `20_` (EVID-090). The replacement text drops the word "calendarios" — see OQ-5 (moot post-repeal).
- **Candidate CRs:** (dated deadline rows: 10d 2016-02→20d 2016-09→5d 2024-05; ISV determinativa day-10 anchor).
- **Topics:** fiscal-reporting

## EVID-084 17_ — DMC sujetos extended: Instituciones del Estado (343-PRIMERO/TERCERO, p.2)

- **Loc:** 343-PRIMERO, TERCERO (p.2); considerando citing CT Art. 30.2.b (pp.1-2).
- **Verbatim:** PRIMERO: reform numeral 1 "en el sentido de adicionar dentro de los sujetos obligados ... a las Instituciones del Estado, que realicen compras en el mercado interno y externo, sean estas gravadas o no ... indistintamente de su categoría." TERCERO: effective "una vez transcurridos dos (2) meses contados a partir de la fecha de su publicación" (published 5-ago-2019 → effective ~5-oct-2019).
- **Gloss:** public-sector entities (CT Art. 30.2.b contribuyentes) joined the DMC obligados from Oct-2019 — matters only for public-sector Odoo deployments; also a D16-style delayed-vigencia example (2-month deferred effectiveness, not immediate-on-publication).
- **Candidate CRs:** DMC-obligado dated rows (State institutions from 2019-10).
- **Topics:** fiscal-reporting

## EVID-085 18_ — Comprobante de Compras Eventuales: definition, narrow scope, 10-SMM seller gate, no crédito fiscal (279-PRIMERO/SEGUNDO a-c, pp.3)

- **Loc:** 279-PRIMERO, SEGUNDO a)-c) (p.3); statutory hooks Acuerdo 189-2014 Arts. 10.f/21.7/69 (p.2).
- **Verbatim:** a) the document is "emitido por el contribuyente adquirente y utilizado por este para respaldar los costos y gastos ... por la compras de bienes y/o prestación de servicios obtenidos de Personas Naturales Hondureñas residentes en los municipios con categoría 'D', según clasificados de la Secretaría de Derechos Humanos, Justicia, Gobernación y Descentralización." c) "se entenderá por bienes: grava, arena y material selecto y como servicios: hospedaje, alimentación, mano de obra y flete por acarreo de los bienes antes referidos." Authorization: PN sellers may sell "siempre y cuando los bienes o servicios no puedan ser adquiridos a través de un proveedor legalmente constituido en dichos municipios"; "podrán vender bienes y/o servicios por un valor no mayor a diez (10) salarios minimos promedios vigentes en el mismo periodo fiscal. Si el valor ... supera esta cantidad el proveedor debe suscribirse al Régimen de Facturación." "Este Comprobante de Compra Eventuales de Bienes y/o Servicios **no dará derecho a crédito fiscal**."
- **Gloss:** buyer-issued fiscal document (inverse of factura) authorized under 189-2014's otros-documentos clause; exhaustively enumerated goods/services; seller gate = 10 SMM promedio per fiscal year (exceed → seller must join the facturación regime); NO input-credit right — costs/gastos support only (ISR deduction evidence, not ISV credit). Municipality category "D" list is external reference data (SDGJGD classification).
- **Candidate CRs:** document type 10 emission (buyer-side) with scope guards (cat-D municipality + enumerated goods/services + no-formal-provider condition); seller annual 10-SMM cap monitor with regime-migration flag; crédito-fiscal block on type-10 lines.
- **Topics:** e-invoicing, fiscal-reporting

## EVID-086 18_ — type-10 format requisites: CAI machinery + provider-ID flexibility + huella (279-TERCERO, pp.3-4)

- **Loc:** 279-TERCERO nums. 1-9 (pp.3-4).
- **Verbatim:** Requisites: buyer RTN/name/commercial name/matriz+establecimiento address/phone/registered email; denomination; **CAI**; **fecha límite de emisión**; 16-digit correlativo NNN-NNN-NN-NNNNNNNN where the two digits = "**10 = Comprobante de Compras Eventuales**", consecutive 00000001→99999999 wrap; first three groups = "identificador del documento"; destinations — "Original: Contribuyente Adquirente ... Copia: Proveedor"; imprenta data for preimpresos (incl. Registro Fiscal de Imprentas certificate); provider block — name, **"se podrá registrar cualquiera de la información siguiente: Registro Tributario Nacional (RTN), Número de cédula de identidad, pasaporte, número de residencia para extranjeros"**, address/phone, detailed description, quantity, "Signo o denominación literal de la moneda nacional Lempira", importe literal y numeral, fecha, **"Firma y huella digital del proveedor. En caso del que el proveedor no pueda firmar debe consignar la huella digital"**; rango de documentos autorizados.
- **Gloss:** type 10 rides the FULL CAI/rango/correlativo machinery (D-H1 sequence key (establecimiento, punto de emisión, doc type) with doc-type code 10 — extends the 24_ taxonomy table at W3); provider identification is deliberately flexible (RTN OR cédula OR pasaporte OR residencia) — ID-type + ID-number pair, not RTN-mandatory; the document is paper-in-person by nature (huilla digital).
- **Candidate CRs:** l10n_latam document-type record code 10; provider-ID multi-type field on type-10 emission; CAI range/exhaustion guards apply to type 10 (shared facturación engine).
- **Topics:** e-invoicing

## EVID-087 18_ — buyer obligations: retain + enter the ISV caused; DMC registration (279-QUINTO, pp.4)

- **Loc:** 279-QUINTO (p.4); authorization/conditioning in CUARTO (p.4).
- **Verbatim:** "El contribuyente adquirente está obligado a **retener y enterar al Fisco el Impuesto Sobre Venta que cause las Compras de Bienes y/o Servicios**. La declaración y entero de este impuesto se hará en el plazo que la ley establece." Also: must "registrar las adquisiciones eventuales ... en la Declaración Jurada Informativa Mensual de Compras" — form to be provided by AT, "dentro de los primeros diez (10) días calendarios del mes siguiente que se efectuó la compra" (2016 text; superseded for DMC timing by the 5-day rule of `20_`). CUARTO: printing authorization mandatory per 189-2014; emission "podrá ser condicionado o limitada ... conforme al comportamiento tributario del Contribuyente Adquiriente".
- **Gloss:** the retention mechanism: buyer withholds the ISV caused by the occasional purchase and enters it (reverse retention on purchases — distinct from Art. 8 OTCD retentions; the RATE/base the acuerdo does not state — OQ-6). Type-10 purchases flow into the DMC as registration duty. Dated-rows discipline: the embedded "10 días" is the 2016 DMC timing, now 5 días per `20_` — cite 20_ for the deadline, 18_ for the registration duty itself.
- **Candidate CRs:** buyer ISV retention rule on type-10 purchases + entero workflow; DMC inclusion of type-10 lines; conditioning/limitation status flag on type-10 authorization.
- **Topics:** e-invoicing, fiscal-reporting, taxation

## EVID-088 19_ — tarjetas num. IX rewritten: monthly per-affiliate detail incl. devolución 8% (240-IX, p.3)

- **Loc:** 240-IX (p.3); considerandos on Resolución DEI-9382-J-2003 (pp.2-3).
- **Verbatim:** Agents must supply SAR "por cada mes calendario y **por cada sujeto pasivo de retención**: 1. Nombre, Razón o Denominación Social y Clave del Registro Tributario (RTN); 2. Valor bruto de la transacción, y fecha en que se practicó la retención; 3. **Importe de la Devolución 8%**." — "por medio del llenado de la Declaración a través del Servicio Web." Considerandos: base procedure = Resolución No. DEI-9382-J-2003, "emitida ... en fecha 23 de octubre de 2003 y publicada ... 01 de noviembre de 2003"; original contemplated informativa "dentro de los primeros diez días calendarios del mes siguiente al que se efectuó la liquidación".
- **Gloss:** per-merchant monthly detail (gross + retention date + the 8% devolución amount) — **the devolución 8% is operationally ALIVE in the 2024 declaration text** (narrows W1f OQ-1/05_ EVID-057: whatever its 2013 suspension history, SAR's current card-retention declaration carries a per-transaction devolución field). Emission date 23-oct-2003 pinned for the DEI-9382 acquisition lead (La Gaceta 01-nov-2003 — outside ENAG window; SAR-republish route).
- **Candidate CRs:** OTCD monthly export: per-RTN aggregate + transaction detail with devolución-8% column; devolución ledger feeding código 215/523 declarations.
- **Topics:** fiscal-reporting, taxation

## EVID-089 19_ — tarjetas num. X-XIII: agente-de-información duty, pago-parcial character, sanctions (240-X..XIII + SEGUNDO, pp.3-4)

- **Loc:** 240-X, XI, XII, XIII, SEGUNDO (pp.3-4).
- **Verbatim:** X: agents "deben también actuar como Agente de Información e Informar ... las operaciones que realizan con los Sujetos alcanzados por la excepción prevista en el numeral VI" — name/razón + RTN, "Importe pagado y fecha en que se efectúo la liquidación", via Servicio Web. XI: "dentro de los primeros diez (10) días calendario del mes siguiente al que se efectuó la liquidación que dio lugar a la retención, a través del Servicio Web." XII: "El importe retenido consignado en el comprobante previsto en el numeral IV ... tendrá para los responsables del tributo el carácter de **pago parcial**, tal concepto será computado en la 'Declaración Jurada de Retención de Impuesto Sobre Ventas por Tarjetas de Crédito o/y Débito' del periodo fiscal en que se efectuó la liquidación." XIII: non-presentation/non-entero → CT sanction + Boletín de Pago. SEGUNDO: rectifications "a través del Servicio Web, de conformidad a la periodicidad establecida en el Código Tributario".
- **Gloss:** three mechanics: (1) exempted-subject (numeral VI — text not in corpus) reporting duty — negative-reporting kin; (2) the retention counts as a **partial payment** for the affiliate in the liquidation period (feeds the affiliate's ISV determinativa as a credit — the código 215/523 consumer side); (3) Servicio Web channel fixed. Numerales I-VIII of DEI-9382 remain un-acquired (comprobante del numeral IV, excepción VI) — lead.
- **Candidate CRs:** excepted-merchant information report; pago-parcial credit application on affiliate ISV declarations; Service-Web channel constraint.
- **Topics:** fiscal-reporting, taxation

## EVID-090 20_ — DMC rewritten AGAIN: 5 días calendario + dual channel; CPAT-073-2016 repealed; REGISTRY GLOSS CORRECTED (237-PRIMERO..QUINTO, pp.3-4)

- **Loc:** 237-PRIMERO (rewritten ordinals PRIMERO/SEGUNDO nums. 2-4), SEGUNDO, CUARTO, QUINTO (pp.3-4).
- **Verbatim:** Rewritten procedure: "2. FORMA DE PRESENTACIÓN: I. ... se deben separar las compras que generan crédito fiscal de las compras que son incluidas en los costos y/o gastos de su contabilidad. II. La presentación de esta declaración informativa deberá realizarse a través de la Oficina Virtual o del Servicio Web." "3. PLAZO DE PRESENTACIÓN: La ... (DMC) debe presentarse dentro de los primeros **cinco (05) días calendarios** del mes siguiente al que se efectuaron las compras internas o las importaciones." "4. SANCIONES: ... serán sancionados de conformidad al Código Tributario, sin eximirlo de la obligación de presentar la misma. La sanción debe ser pagada con el Boletín de Pago..." CUARTO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo No. CPAT-SG-073-2016." QUINTO: "Quedan vigentes las demás disposiciones de los Acuerdos DEI SG-276-2015 y SAR-343-2019 que no se modifican con este acuerdo."
- **Gloss:** CURRENT DMC regime (from 20-may-2024): deadline = first 5 días calendario; channels = Oficina Virtual OR Servicio Web (no single-modality rule here, unlike DJIMR's 238-QUINTO — keep distinct); crédito-fiscal/costos split restated. Effective DMC deadline chain: 10d (2016-02) → 20d (2016-09) → **5d (2024-05, current)**. **7th title-vs-content incident:** registry gloss said "modifies retenciones procedure ordinales" — content modifies the **DMC** procedure; row amended 2026-08-20 (filename kept for provenance).
- **Candidate CRs:** DMC deadline dated rows (10d→20d→5d with vigencia dates); dual-channel filing config; sanctions engine hookup (CT + Boletín de Pago).
- **Topics:** fiscal-reporting

---

## File-level OQs

- **OQ-1 (13_ ISR Art. 28 certification):** 619 considerando quotes ISR Art. 28 requiring the Balance/GyP "certificadas por un contador hondureño titulado, o incorporado" — verify whether the Form 535 filing reproduces/replaces this certification attestation (Ayuda `67_` at W2b; synthesis question for the EEFF FR).
- **OQ-2 (13_ Reglamento Ley ISR Art. 84):** third citation of the unlocated modern Reglamento (after plantilla Art. 51, W1f). Acquisition lead stays open; no HN synthesis should cite "Reglamento Ley ISR Arts. 51/84" until acquired.
- **OQ-3 (15_ gazette number print 33,955 vs catalog 33,995):** OCR of the gazette header reads 33,955; the SAR catalog title for DEI-SG-276-2015 said 33,995. Gazette-number arithmetic (33,991 = 22-mar-2016; ~6 issues/week) favors 33,955 for 9-feb-2016 — treat catalog 33,995 as suspect [sic]; pin only if the ENAG original is ever pulled.
- **OQ-4 (14_ DJIMR catalog vs tarjetas codes):** the 25-code DJIMR list has no 215/523 (tarjetas) — card retentions appear to file under the DEI-9382-J-2003 procedure's own "DJ de Retención ISV por Tarjetas" (240-XII) outside the DJIMR system. Confirm scope split at W2b via Ayudas `41_`/`42_` (215/523) vs `40_` (217).
- **OQ-5 (16_ "20 días" without "calendario"):** the 073 replacement text says just "veinte (20) días del mes siguiente" (base text said "días calendarios"). Moot for current law (5 días calendarios explicit in 20_), but a dated-rows reconstruction of the 2016-2024 window needs a hábiles-vs-calendario ruling — default to calendario (context: decongestion of a calendario day-10 cluster); flag if ever material.
- **OQ-6 (18_ ISV retention rate/base for compras eventuales):** 279-QUINTO mandates the buyer "retener y enterar al Fisco el Impuesto Sobre Venta que cause las Compras" without stating rate/base mechanics (full 15%? on the gross?). No corpus text yet resolves it — check Ayudas (DMC/ISV family) at W2b; else acquisition question (procedural guidance).
- **OQ-7 (20_ registry mislabel):** row gloss corrected in place 2026-08-20 (7th incident; same family as 05_/94_). Filename `20_Acuerdo_SAR-237-2024_retenciones_mod.pdf` retained deliberately — renaming breaks the provenance chain; the row + this OQ are the correction of record.
