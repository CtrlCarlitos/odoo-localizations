# GT — E-Invoicing — Validation rules (Reglas y Validaciones v2.0)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL
business-validation universe of the *Reglas y Validaciones* (validation
rulebook) v2.0: the validation pipeline (XSD conformance first, then
business rules) and the three-column severity model; emission-date windows
(5-day back-dating, same-calendar-month future dating, affiliation-change
lookback) as the D16 dated-instrument implementation; emitter NIT/Mini-RTU
eligibility checks (marcas, CAIS trait, FEPE clasificación); establishment
active-in-RTU and classification gates; receptor identification rules (CUI,
EXT, exact-string CF with the Q2,500 cap); line-level arithmetic; the
*frases* (statutory phrase/scenario annotations) matrix and the tipo-4
exemption catalog; every rate and validation constant as decree-bound dated
rows (IVA, IDP, ITH, ITP, TDP, IFB, MUN, IDB, TAB, CEM, IBN, TAP, FESP/FEPE
retentions, régimen primario/pecuario/agropecuario payments); and the totals
and complement arithmetic (Gran Total, NCRE/CAIS origin caps, complemento
matrix, exportaciones/INCOTERM, retention and reference complements).

It does **not** cover: the DTE type taxonomy and per-type behavior hooks
(`01_document-types.md`, cluster E1), the XSD schema set and channel drift
(`02_dte-schema.md`, cluster E2 — XSD conformance as a generation gate is
GT-EINV-FR-068 there), the anulación window/blockers and contingencia models
(`06_anulacion-contingencia.md`, cluster E6), the certificador API, mini-RTU
transport and runtime mensajes delivery
(`05_certificador-interface.md` §establishment, clusters E5/E7), the mandate
chronology (`04_mandate-onboarding.md`, cluster E4), the graphic
representation (`07_display-representation.md`, cluster E8), or the statutory
authority behind each rate (taxation waves — this file records rate values as
Reglas-printed dated rows, not as law citations). Those files reference this
one for the validation-rule universe.

## 2. Legal Basis

Authority order (binding, per master evidence index): **Reglas y
Validaciones v2.0 (19/12/2024, vigencia abril 2025)** governs ALL validation
behavior over every 2018-vintage manual/caso; the cover footer "Versión
1.7.10 1 de 132 Febrero 2025" is a stale stamp from the previous 132-page
build and is never cited as content version (R1; the committed source file
name retains that stale string — the artifact is the 146-page v2.0 printing,
late folios "de 146 Abril 2025"). Binding rulings for this file: R1
(citation form), R7 (Reglas v2.0 supersedes 2018 bounds, e.g. frase tipo-4
escenarios 1–12 → 1–35+36), R15 (editorial drift — key on rule content and
codes, never section/row numbers; GOQ-45), R16 (CF cap applies to the
11-type list incl. FACP), R17 (CodigoProducto carries BOTH the CGP*LBS and
GAL* families per the Reglas, over the GH XSD's GAL-only enum), GOQ-50
(all rate values are decree-bound dated rows). Section numbers below are
findability locators only — the binding rule identity is its content and
codes (R15/GOQ-45). The extracted text twin
`gt/.extractions/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf.txt` is
the direct-consultation copy of the same artifact.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025), portada: título "VERSIÓN 2.0" + pie "Versión 1.7.10 1 de 132 Febrero 2025"; folios tardíos "134 de 146 Abril 2025"; historial fila "2.0 19/12/2024 Se agregan los tipos de DTE: … FEPE / FARP / FCRP / FPEC / FCPC … FECHA ENTRADA DE VIGENCIA Abril 2025" (sin fila 1.7.10 en el historial) | Version forensics: the artifact is the v2.0 printing (19/12/2024, effective April 2025); "1.7.10/Febrero 2025" exists only as a stale cover footer — cite "Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025)" only | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | p. 1; pp. 129–146; historial p. 146 (EVID-111, EVID-112, EVID-113; cadena EVID-114) |
| LB-002 | Reglas v2.0, §1.4 (tabla de roles): "El Certificador las aplica en su sistema, previo a certificar el documento … La SAT las aplica al momento de recibir el DTE … Rechaza. Si el documento no cumple con todas las validaciones, el Certificador lo rechaza y avisa al Emisor … Informa … dicha clasificación puede variar"; regla 2.1: "Una casilla no cumple con lo establecido en el esquema principal del DTE (XSD) o en los esquemas de los complementos (cuando aplique) … Error. El XML enviado no cumple con el esquema del XSD." (columnas CERTIFICADOR SI / SAT1 "Rechaza (ERC)") | Validation actors and pipeline: XSD conformance is validation #1 (SAT1 rejects with ERC); the Certificador applies rules pre-certification and rejects; SAT primary rules reject or inform, secondary rules inform; SAT classification is explicitly mutable | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §1.4 pp. 18–19; regla 2.1 p. 20 (EVID-117, EVID-118) |
| LB-003 | Reglas v2.0, reglas 2.2.1.1–4 + "Aclaración sobre la validación 2.2.1.1 (fecha futura)": 1: "El día, mes y año de la casilla “Fecha y hora de emisión” tiene una antigüedad mayor a cinco días … y el tipo de DTE es diferente de “CIVA” y “CAIS”. (Se cuenta a partir del siguiente día de la emisión)"; 2: "… es posterior al último día del mes de la “Fecha y hora de certificación”"; 3/4 (ISR/IVA): "Se realizó cambió a la afiliación … y se emite DTE con fecha del mes anterior (5 días calendario), deberá mostrar la afiliación con la que contaba anteriormente …"; Aclaración: "La validación permite que se facture con fecha futura, pero siempre dentro del mismo mes calendario" | Emission-date windows: ≤5 days back-dating counted from the day after emission (CIVA/CAIS exempt); future dates only within the same calendar month as certification; 5-day affiliation-change lookback must show the OLD affiliation (ISR and IVA rules both) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.2.1 pp. 20–21 + ejemplos trabajados (EVID-119) |
| LB-004 | Reglas v2.0, reglas 2.2.2.1–10: 3: "… un NIT que no está afiliado al IVA … y el tipo de DTE es distinto de: “CIVA”, “FESP”, “RECI”, “RDON”"; 6 (CAIS): "El NIT Emisor no tiene vigente la característica especial: “DECRETO 29-89”" ("La SAT comparte con cada Certificador de DTE, la característica especial de sus acreditados"); ClasificacionEmisor 3: "El tipo de DTE es FEPE y su única clasificación registrada en la casilla “productorClasificacion” del minirtu es productor (1672)"; MARCAS: "1 Marca de domicilio no localizado … 2 Marca de Omiso … 1 = Omiso en IVA" ("Esta información es provista a través del Mini RTU") | Emitter NIT eligibility via Mini-RTU: IVA-affiliation requirement with the CIVA/FESP/RECI/RDON exceptions; CAIS requires the "DECRETO 29-89" special trait; FEPE barred when the sole registered clasificación is productor (1672); MARCAS are non-blocking flags supplied through the Mini RTU | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.2.2 pp. 22–23 (EVID-120) |
| LB-005 | Reglas v2.0, reglas 2.2.3.1–2 + tablas: 1: "El establecimiento no aparece activo en la SAT para ese NIT en esa fecha de emisión"; tabla de clasificación: "Exento Constitucional 1703 → Centros educativos privados 1704* [CIVA] SI [CAIS] NO [RECI] SI [FESP] NO"; "Beneficio Fiscal Temporal 2204 → Maquila Decreto 29-89 … 2224* NO SI NO NO"; "Persona jurídica … 887 → Universidades autorizadas 963 SI NO SI SI; Universidades Autorizadas Privadas 1084 …; Confederación Deportiva 964 …"; "Entidad del Estado 886 → Centros Educativos Públicos 899 …; Comité Olímpico Guatemalteco 965 …; IGSS 966 …"; nota 6: FESP sin afiliación al IVA debe corresponder a esta tabla; con afiliación, se permite la emisión; tabla regímenes: "3696 1696 Régimen Primario SI SI NO NO SI / 3694 885 … / 3695 1696 Régimen Pecuario NO NO SI SI SI / 3689 885 …" (última columna = Factura Especifica) | Establishment gates: active-in-RTU at emission date; classification tables gate CIVA/CAIS/RECI/FESP emission (1703→1704, 2204→2224, 887→963/1084/964, 886→899/965/966); régimen primario/pecuario establishment pairs 3696/1696 and 3694/885 (primario), 3695/1696 and 3689/885 (pecuario), all FEPE-capable | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.2.3 pp. 24–26 + tablas (EVID-121) |
| LB-006 | Reglas v2.0, reglas 2.2.4.1–12 + Aclaraciones: 8 (EXT): "• Tener una longitud entre 3 y 18 caracteres • Puede contener letras de la A a la Z (mayúsculas) y dígitos (0-9) • Puede contener caracteres especiales (&, %, -, /, #, =) • No debe contener espacios"; 11: "El contenido de la casilla “ID del receptor” es igual a CF (Consumidor Final), el contenido de la casilla “Tipo de DTE” es: “FACT, FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE, FACP”, y el contenido de la casilla “Gran total” es igual o superior a Q. 2,500.00"; 12: "El tipo de DTE es FEPE y el ID Receptor es un NIT de organización empresa"; Aclaración: "no permiten que un DTE contenga textos que sean diferentes de CF. Por ejemplo, son incorrectos estos valores: C/F, C.F. o Consumidor Final"; "Al momento de validar el CUI y este ser correcto en la representación gráfica se deberá de consignar el nombre devuelto por el servicio del Renap" | Receptor rules: EXT charset (3–18 chars, A–Z, 0–9, & % - / # =, no spaces); CF is an exact string with the Q2,500 cap on the 11-type list incl. FACP; FEPE receptor must be a natural person; CUI validated against RENAP with the returned name consigned | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.2.4 pp. 27–28 (EVID-122) |
| LB-007 | Reglas v2.0, §§2.2.5–2.2.7 y 2.3.x: 2.2.5 (Exp): "Se incluye la casilla “Exportación” y el contenido … incluye uno de los textos: “NABN”, “RDON” “RECI”, “FESP”, “CIVA”, “CAIS”"; "… el “Tipo de DTE” es distinto de “NDEB”, “NCRE”; y no se incluye el complemento “Exportaciones”"; 2.2.7.1: NCRE/NDEB/CIVA/CAIS deben llevar la moneda del documento referencia; 2.2.7.2: CF + moneda distinta de GTQ + monto convertido ≥ Q2,500 → rechaza; 2.3.1: espectáculos públicos ⇒ máximo 1 ítem; CIVA ⇒ máximo 2 ítems; 2.3.5.1: "El contenido de esta casilla es diferente al resultado de (Casilla “Cantidad”) multiplicado por (casilla “PrecioUnitario”)"; 2.3.6.1: Descuento ≤ Precio; 2.3.7: OtrosDescuento ≤ Precio − Descuento; 2.3.8: "B" obligatorio para FACA, FCCA, FACP, FAAE, FCAE (y NEV, FEPE); "S" obligatorio para espectáculos y RANT; exportación + Servicio ⇒ sin INCOTERM | Destination/export flag rules, currency matching, item caps, line arithmetic (Precio = Cantidad × PrecioUnitario), discount bounds and per-type Bien/Servicio constraints | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§2.2.5–2.2.7, 2.3.1–2.3.8 pp. 28–33 (EVID-123, EVID-124, EVID-125) |
| LB-008 | Reglas v2.0, reglas 2.3.2.1–5 + "Catálogo de productos": 3: "Se envía un código de producto y el tipo de DTE es diferente de FACT, FCAM, NCRE, NDEB"; 5: "Se envía el código de producto GALDIESEL y el código de unidad gravable para el impuesto IDP es diferente de 4"; catálogo: "1 CGP10LBS Subsidio cilindro 10 libras 08.00 / 2 CGP20LBS … 16.00 / 3 CGP25LBS … 20.00 / 4 CGP35LBS … 28.00 / 5 CGP100LBS Cilindro de gas envasado propano de 100 lbs 0.00. *Sujeta a la vigencia de leyes y reglamentos para el efecto" | CodigoProducto: only on FACT/FCAM/NCRE/NDEB; both CGP*LBS subsidy codes and GALDIESEL (IDP unidad gravable 4) exist; subsidy per-unit values Q8/16/20/28/0.00 explicitly law-dependent | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.3.2 pp. 31–32 + catálogo (EVID-126) |
| LB-009 | Reglas v2.0, §2.4.1 matriz Impuestos × Tipo DTE (filas por código) y §2.4.3 casillas A–D: "A Monto gravable SI NO SI NO SI SI NO SI SI NO NO NO / B Código de unidad gravable: SI ×12 / C Cantidad de unidades gravables NO SI NO SI NO NO NO SI SI SI SI SI / D Monto del impuesto SI ×12" (NDEB/NCRE excluyen Tasa Municipal y Tarifa Portuaria; tipos régimen primario/pecuario y FEPE: ningún impuesto) | Tax-capability matrix: which of the 12 taxes each of the 26 types may carry; per-tax Impuesto casilla usage (MontoGravable / CodigoUnidadGravable / CantidadUnidadesGravables / MontoImpuesto presence) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.4.1 pp. 34–36; §2.4.3 p. 36 (EVID-127) |
| LB-010 | Reglas v2.0, §2.6 matriz de frases: leyenda "0 No requerido (la frase no es requerida) / 1 Requerido (La frase siempre debe estar presente) / 2 Opcional (La frase puede o no estar presente)"; nota: "Los tipos de frase 1, 2, 3, 6 y 7 se pueden obtener automáticamente del Registro Tributario Unificado (RTU), con base a la obligación de cada afiliación del impuesto que tenga el emisor" (24 columnas de tipos DTE; CIVA/CAIS excluidas) | Frases matrix: 12 frase tipos × 24 DTE-type columns with 0/1/2 semantics; tipos 1, 2, 3, 6 and 7 are auto-derivable from the emitter's RTU obligations | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.6 pp. 41–42 (EVID-130) |
| LB-011 | Reglas v2.0, §2.6.1 reglas 1–36: 6/7: exportación ⇒ frase tipo 4 (Exento o no afecto) presente, escenario "1"; 7A: NDEB/NCRE sin Exp ⇒ escenario "22"; 8: FACT/FCAM/FESP sin Exp con ítems sin IVA ⇒ tipo 4 requerido; 9: FACT/FCAM escenario ∈ {2,3,6,7,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32}; 9A: FESP escenario ∈ {2, 11}; 10: RDON ⇒ esc. 4; 11: RECI ⇒ esc. ∈ {2,5,6,8,16,20,33}; 12–16B: compuertas tipo 8 (personería); 26: CIVA prohibido incluir frases; 27: escenario 36 ⇒ solo FACT/FCAM; 28: mismo tipo+escenario solo una vez (excepto RANT); 29–36: escenarios régimen ligados a Exp, ClasificacionEmisor='Intermediario' (clasificación 1674) y "la forma de cálculo … registrada en RTU" ("Régimen Pecuario Exportador y forma de pago del impuesto del 2% sobre las ventas brutas", "Régimen Primario Exportador … el 2% sobre las ventas brutas", "Régimen Pecuario y forma de pago del impuesto es el 10% sobre las utilidades") | Frase scenario validation cluster: export/NC-ND special cases, per-type escenario lists, tipo-8 personería gates, uniqueness, CIVA frase ban, and régimen escenario ↔ RTU forma-de-cálculo linkage | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.6.1 pp. 43–46 (EVID-131) |
| LB-012 | Reglas v2.0, §2.6.8 catálogo frase tipo 4 (Exento o no afecto al IVA), escenarios 1–35 (34 ausente [sic]): "1 Exportaciones. Cuando el vendedor exporta bienes o servicios. FACT FCAM — Exenta del IVA (art. 7 num. 2 Ley del IVA)"; "15 Venta al menudeo en mercados … no excedan de cien quetzales (Q. 100.00) por cada transacción … (art. 7 num. 11)"; "22 Las notas de débito y crédito no deben incluir IVA cuando el documento origen … tampoco lo incluye"; "26 Boletos aéreos para beneficiarios del Dec. 31-2022 … (art. 4 Dec. 31-2022)"; escenario 36 citado en 2.6.1.27 | Tipo-4 exemption catalog: escenarios 1–35 printed (34 absent) with per-row legal-basis legend text; escenario 36 cited in rule text; supersedes the 2018 casos bound of 1–12 (R7) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.6.8 pp. 50–53 (EVID-132; escenario 36 vía EVID-131) |
| LB-013 | Reglas v2.0, §§2.6.5–2.6.16 + "Aclaración valor apoyo social": tipo 1 esc. 1–3 ("Sujeto a pagos trimestrales ISR" / "Sujeto a retención definitiva ISR" / "Sujeto a pago directo ISR (XXXX - dd/mm/aaaa)"); tipo 6: "forma de pago del impuesto es el 5% sobre las ventas brutas" / "el 5% sobre las utilidades — … no retener"; tipo 7: "No retener, XXXX" ("El número de resolución se debe incorporar en el XML del DTE en la casilla correspondiente"); tipo 9 esc. 1: "Decreto XX-2022 [sic] … gas licuado envasado en cilindros portátiles … por un valor XXXXX"; esc. 2/3 "Decreto 42-2022 … apoyo social temporal"; esc. 4 "Impuesto de Salida Vía Aérea … (art. 4 Dec. 31-2022)"; esc. 5/6/7 "Decreto 45-2022 … / y sus Reformas / Decreto 05-2023"; Aclaración: "Para establecer el valor del apoyo social se deberá multiplicar el Descuento Especial según el producto consignado por la cantidad …"; tipo 10: "Régimen Primario Productos y Comercializador … 1.5% sobre las ventas brutas" / "Régimen Primario Exportador … 2% sobre las ventas brutas"; tipo 11 (pecuario): 1.5% ventas brutas / 10% utilidades / 2% exportador | Frase scenario details and embedded rates: regime payment rates (agropecuario 5%; primario 1.5%/2%; pecuario 1.5%/10%/2%), tipo-9 fuel-subsidy arithmetic, resolución number/date fields, and the "Decreto XX-2022" placeholder defect (GOQ-46) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§2.6.5–2.6.16 pp. 47–58 + Aclaración (EVID-133) |
| LB-014 | Reglas v2.0, §2.7: catálogo "1 Tasa 12.00% IVA 12% 12 / 2 Tasa 0 (Cero) IVA 0% 0"; 2.7.1.2: "… casilla “Precio” menos las casillas … “descuento” [sic "frato"] y “otros descuentos” y el resultado de ellas dividido entre el factor 1.12; cuando la casilla “Código de la Unidad Gravable” es igual a 1"; 2.7.1.3: unidad 2 ⇒ sin división; 2.7.2.2: "(Se incluye la casilla de “Exportación”) y (El contenido de la casilla es diferente de 2)"; 2.7.3.1: "Cantidad de Unidades Gravables no debe estar presente para el IVA"; 2.7.4.1: IVA = MontoGravable × %; Aclaraciones: "1. El IVA siempre debe estar incluido en el precio (casillas “Precio Unitario” y “Precio”), excepto … exentas o no afectas … 2. En el caso de notas de débito y crédito … se deben registrar dentro de los dos meses siguientes a la fecha de emisión de la factura afectada … no tendrá derecho al reconocimiento del crédito fiscal según lo indica el artículo 17" | IVA computation: 12%/0% unidades gravables, price-inclusive model, base = (Precio − Descuento − OtrosDescuento)/1.12 for unidad 1, export ⇒ unidad 2, no CantidadUnidadesGravables for IVA; NC/ND two-month fiscal-credit rule (Ley IVA art. 17) as informative advice | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.7 pp. 59–61 + ejemplos (EVID-134) |
| LB-015 | Reglas v2.0, §2.8: catálogo de 13 tasas específicas: "1 Gasolina superior … Q4.70 / 2 Gasolina regular … Q4.60 / 3 Gasolina de aviación … Q4.70 / 4 Diésel … Q1.30 / 5 Gas Oil … Q1.30 / 6 Kerosina (DPK), (Avjet, turbo fuel) Q0.50 / 7 Nafta Q0.50 / 8 Fuel Oil (Bunker C) Q0.00 / 9 Gas licuado de petróleo a granel Q0.50 / 10 Gas licuado petróleo carburación Q0.50 / 11 Petróleo crudo usado como combustible Q0.00 / 12 Otros combustibles derivados del petróleo Q0.00 / 13 Asfaltos Q0.00"; 2.8.4.2 (no-GTQ): "El valor de la Tasa específica en Q … dividido entre el tipo de cambio del Banco de Guatemala en la fecha de emisión del DTE y el resultado multiplicarlo por la casilla “Cantidad de Unidades Gravables”"; Aclaración: "… En caso no existiera tipo de cambio oficial … se deberá de utilizar el último tipo de cambio registrado. Cuando la moneda sea USD se deberá utilizar la tasa de referencia publicada por el Banco de Guatemala y cuando sea diferente se deberá tomar el tipo de cambio de venta" | IDP (impuesto al petróleo): 13 per-unit Q rates (no MontoGravable); Banguat FX rules — emission-date rate, last-published fallback, USD = tasa de referencia, other currencies = tipo de cambio de venta | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.8 pp. 62–65 (EVID-135) |
| LB-016 | Reglas v2.0, §§2.9–2.13: Turismo Hospedaje: "1 Tasa Hospedaje 10% Hospedaje 10.00% 10 / 2 Tasa Hospedaje Exento … 0%" (fn. 7: la Tarjeta de Turismo US$5.00 → Migración US$10.00, "No se incluye en ningún DTE"); Turismo Pasajes: "1 Salida del país por vía aérea Aérea USD30.00 / 2 … marítima Marítima USD10.00 / 3 … aérea exento según Decreto 31-2022 Aérea exenta Dec. 31-2022 0.00"; regla 2.10.2.2: "El contenido de la casilla es igual a 3 y no incluye la frase tipo 9 codigo 4"; "tipo de cambio del Banco de Guatemala del día anterior de la fecha de emisión" (fn. 8: "Literal C, Art. 21, del Decreto número 1701"); Timbre de Prensa: "1 Timbre de prensa cinco (5) por millar Timbre de prensa 0.50%"; Bomberos: "1 Impuesto por seguro contra incendios Bomberos 2.00%"; Tasa Municipal: código "DDMMCCC — DD: Código de departamento (2 dígitos) MM: Código de municipio (2 dígitos) CCC: Código de concepto (3 dígitos)"; "El valor de la tasa municipal MUN es variable, se acepta el monto ingresado" | ITH 10%; ITP USD30 aérea/USD10 marítima with day-before Banguat reference rate and the unidad-3 (exenta Dec. 31-2022) frase tipo 9 esc. 4 gate; TDP 0.50% (cinco por millar); IFB 2%; MUN variable amount with structured DDMMCCC unit code | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§2.9–2.13 pp. 66–79 (EVID-136) |
| LB-017 | Reglas v2.0, §§2.14–2.18: Bebidas Alcohólicas: "1 Cervezas … 2203.00.00 — 6.00% / 2 Vinos … 2204 — 7.50% / 3 Vino espumoso … 7.50% / 4 Vino “vermouth” … 7.50% / 5 Sidras … 7.50% / 6 Bebidas alcohólicas destiladas … 2208 — 8.50% / 7 Bebidas alcohólicas mezcladas … 7.50% / 8 Otras bebidas fermentadas … 7.50%" ("se debe consignar el precio sugerido al consumidor por cada unidad gravable"); Tabaco: "1 Impuesto sobre el precio de venta en fábrica por paquete de 10 cajetillas de 20 cigarrillos … 100.00% / 2 … precio de venta sugerido al consumidor … 75.00%"; Cemento: "1 Bolsa de 42.5 kilogramos — Q1.50"; Bebidas No Alcohólicas: "1 Bebidas gaseosas y jarabes Q0.18 / 2 Bebidas isotónicas o deportivas Q0.12 / 3 Jugos y néctares Q0.10 / 4 Bebidas de yogur Q0.10 / 5 Agua natural envasada … hasta cuatro litros … Q0.08" (exceptuada la de más de cuatro litros); Tarifa Portuaria: "1 Tarifa portuaria — $0.05" (no-USD: Banguat "del día anterior de la fecha de emisión") | IDB 6/7.5/8.5% on the suggested consumer price; TAB 100%/75%; CEM Q1.50 per 42.5 kg bag; IBN Q0.18/0.12/0.10/0.08 (water >4 liters excepted); TAP USD0.05 with day-before Banguat conversion | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§2.14–2.18 pp. 80–94 (EVID-137) |
| LB-018 | Reglas v2.0, §2.19: 2.19.1.1: "… la casilla “Precio” menos las casillas “Descuento” y “Otros Descuentos”, más la sumatoria de las casillas “MontoImpuesto” de los impuestos que sean sumables al DTE (excepto el IVA por estar ya incluido)"; 2.19.2.1: "Gran Total … sumatoria de las casillas “Total”"; 2.19.1.2/2.19.2.4: "… “total”/“Gran total” … es igual o superior a Q. 2,500.00, … “ID Receptor” es igual a CF … “FACT, FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE”" (10 tipos, sin FACP); 2.19.2.2/3: NCRE (y CAIS Gran Total) no pueden exceder los totales registrados del documento origen cuando "Régimen antiguo" está ausente | Totals arithmetic: Total = Σ(Precio − Descuento − OtrosDescuento) + Σ addable MontoImpuesto (IVA already inside price); Gran Total = Σ Total; CF Q2,500 ceiling (10-type list here vs 11 incl. FACP at 2.2.4.11/2.2.5.6 — GOQ-47); NCRE/CAIS origin caps | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.19 pp. 95–96 (EVID-138) |
| LB-019 | Reglas v2.0, §3.1 catálogo de complementos: leyenda "0 No corresponde (el complemento no debe estar presente) / 1 No requerido (el complemento puede estar lleno o vacío) / 2 Requerido (el complemento siempre debe estar lleno)"; filas (extracto): "1 Exportación: 1 [FACT/FCAM/FACA/FCCA/FAPE/FCPE/FAAE/FCAE + los cuatro tipos régimen]"; "2 Retenciones de factura especial: 2 for FESP"; "3 Abonos de factura cambiaria: 2 for FCAM/FCCA/FCPE/FCAE/FCRP/FCPC"; "4 Referencias de Nota de crédito y débito: 2 for NCRE/NDEB"; "7 Referencias de constancias: 2 CIVA/CAIS"; "11 Traslado de mercancías: 2 NEV"; "12 Exportación provisional: 2 FACP"; "14 Retenciones de factura especifica: 2 FEPE" (numeración salta el 13 [sic]) | Complement applicability catalog: the 14 × 26 matrix with 0/1/2 semantics; required complements per type; numbering unstable (13 skipped, TOC labels drift) — key on complement names | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §3.1 pp. 97–98 (EVID-139) |
| LB-020 | Reglas v2.0, §§3.2–3.4.4: campos del complemento (extracto): "Lugar de expedición No Texto, 150 / Nombre consignatario Si Texto, 70 / … Código consignatario No Texto, 17 / … INCOTERM Si* Solo cuando sea B en el campo B/S / Número del DTE provisional No Texto, 32 / … Número de DUCA procedente No Texto, 50"; tabla INCOTERMS: "EXW … FCA … FAS … FOB … CFR … CIF … CPT … CIP … DDP … DAP … DPU Entregada en el lugar de la descarga … ZZZ Otros"; 3.4.1: UUID del DTE provisional debe coincidir con el registro SAT ("El contenido de la casilla pertenece a un DTE diferente de FACP" → rechaza; "no coincide con UUID vigente" → "La factura provisional se encuentra anulada"); moneda/receptor deben coincidir con el FACP origen | Exportaciones complement: consignatario blocks + INCOTERM (goods only, incl. DPU — DTA removed) + provisional-DTE back-references with UUID/currency/receiver consistency | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§3.2–3.4.4 pp. 99–102 (EVID-140) |
| LB-021 | Reglas v2.0, §§3.5–3.14: 3.5.1.1: "“ISR a Retener” … sumatoria de las casillas “Monto Gravable por 5%. Según Decreto 10-2012"; 3.5.2.1: IVA a Retener = "Total Monto Impuesto" del IVA; 3.5.3.1: TotalMenosRetenciones = "Sumatoria de las casillas “Monto Gravable” … menos … “ISR a Retener”"; §3.7 fn. 10: "Referencia a un único DTE: Cada Nota de Crédito o de Débito solo puede hacer referencia a un único DTE"; 3.7.1.2: origen debe ser "FACT", "FCAM"; 3.7.1.3 (papel): Código Tipo ∈ "1", "2", "7", "8", "9", "30", "32", "37", "38", "53", "57", "60", "62", "63", "66", "67", "68", "69", "72"; 3.7.1.6: "Se deja sin efecto la presente validación, para permitir la aplicación de Notas de Crédito o de Débito, a través de un certificador distinto al certificador del DTE original"; §3.10: constancias referencian FACT/FCAM/FESP; MontoIVAExento ≤ total IVA del origen (tolerancia ±2 decimales); constancia vigente bloquea otra; 3.8.2.1: "MontoCobroIVA … multiplicar el valor de la casilla “BaseImponible” por el 12%"; §3.16.1 (ICT): "El contenido de la casilla es diferente a la multiplicación de la casilla Gran Total por 1.5%; o la casilla TotalMenosRetenciones es diferente de la resta Gran Total menos RetencionICT" | Retention and reference complement arithmetic: FESP ISR 5% (Dec 10-2012) + IVA = TotalMontoImpuesto; NC/ND single-origin with FACT/FCAM (FEL) or legacy paper Código-Tipo origins; cross-certificador NC/ND allowed; constancia reference caps; cobro-ajena IVA 12%; FEPE ICT 1.5% of Gran Total | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§3.5–3.14 pp. 103–121 (EVID-141) |
| LB-022 | Reglas v2.0, anexos 5.1–5.2: depuración: "a) Eliminar los espacios en blanco … b) … eliminar todos los puntos … d) Eliminar los guiones (altos o bajos) en la anteúltima posición. e) Si el dígito de la derecha es una letra k minúscula, reemplazarla por una K mayúscula. f) Si el contenido resultante … es “C/F” o “CONSUMIDOR FINAL”, reemplazarlo por “CF” en mayúsculas"; 5.1.3: "El NIT tiene un tamaño de 2 dígitos hasta 12 dígitos … El dígito verificador (D) se encuentra en el extremo derecho"; 5.1.4 (CUI): "El CUI puede tener 2 longitudes diferentes, de 12 o 13 dígitos … El dígito verificador es siempre el quinto dígito contando de derecha a izquierda … Las últimas 4 posiciones de la derecha (CCCC) NUNCA se toman en cuenta … multiplicando cada uno de los 7 u 8 dígitos … el resultado se multiplica por 10. Al resultado final se le aplica la función “mod” con el parámetro “11”"; 5.2.1: "Tolerancia absoluta máxima: una centésima (de cualquier moneda …)"; 5.2.2: totales verticales idéntica tolerancia | NIT/CUI canonicalization and check-digit algorithms (NIT coefficient table not printed — GOQ-49) and the ±0.01 absolute tolerance for every arithmetic validation | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | Anexos 5.1–5.2 pp. 132–134 (EVID-145) |
| LB-023 | Decisiones compartidas D15/D16: filas valid_from/valid_to por parámetro legal; resolución as-of la fecha de anclaje del dominio; congelamiento al escribir; sin transmisión con fecha pasada fuera de ventana; clase histórica no transmisible | Shared decisions D15 (anchor-date pattern) and D16 (dated rule rows, no past-dated transmission, historical = non-transmittable class) — the regime this file instantiates for emission dates and rate constants | `shared/docs/regulatory-change-management.md` | D15–D16 (canon compartido del master index; D-GT10 = instanciación GT) |

## 3. Functional Requirements

### 3.1 Validation pipeline, severity model & citation discipline

- **GT-EINV-FR-071:** The validation pipeline shall run in fixed order: XSD
  conformance first (rule 2.1 — a single non-conformant casilla rejects the
  XML with "Error. El XML enviado no cumple con el esquema del XSD", SAT1
  "Rechaza (ERC)"), and business rules (Reglas §2.2+) only afterwards, over
  XSD-conformant documents. The generation-side twin of this gate is
  GT-EINV-FR-068 in `02_dte-schema.md`; this file owns the validation-order
  semantics. (LB-002; EVID-117)
- **GT-EINV-FR-072:** The system shall implement the three-column severity
  model — Certificador rechaza (pre-certification), SAT primaria (rechaza o
  informa), SAT secundaria (informa) — and shall key every error-mapping
  entry on rule content + returned message text, never on a fixed
  Reject/Inform classification, because SAT explicitly reserves the right to
  reclassify between primaria and secundaria ("dicha clasificación puede
  variar"); a reclassification shall change no product code. (LB-002;
  EVID-118)
- **GT-EINV-FR-073:** Every validation rule, matrix row and catalog value
  shall be identified by its content and codes (DTE codes, frase
  tipo/escenario, impuesto/unidad codes, complement names) — never by Reglas
  section or table row numbers, which are editorially unstable (duplicate
  21-type table pp.15–17; the five v2.0 types numbered 22–26 in one matrix
  and 23–27 in another; complemento 13 skipped; two §3.16). Section numbers
  appear in this file as findability locators only → OQ-002 (GOQ-45).
  (LB-001; LB-009; LB-019; EVID-116, EVID-127, EVID-128, EVID-139; R15)
- **GT-EINV-FR-074:** The rulebook vintage shall be stored as dated rows:
  the implemented rule set = Reglas y Validaciones v2.0 (19/12/2024,
  *FECHA ENTRADA DE VIGENCIA Abril 2025*, valid_from 2025-04); the strings
  "1.7.10" and "Febrero 2025" are artifact metadata (stale cover footer)
  and shall never appear as a content-version citation; whether a real
  1.7.10 interim printing circulated is open → OQ-001 (GOQ-44). A future
  Reglas revision appends a dated row (D16), never overwrites. (LB-001;
  EVID-111, EVID-112, EVID-113, EVID-114; R1)
- **GT-EINV-FR-075:** Validation shall be dual per the thin-client contract
  (D2): the Odoo client mirrors the shared pre-validation rules (date
  windows, canonicalization, arithmetic, caps, matrix gates) for early UX
  rejection, and the SaaS core is the authoritative validator that compiles
  the DTE and owns the certificador-facing result; the two sides implement
  the identical rule set from the same shared rule/matrix data (§4), and any
  rule not mirrorable client-side (registry lookups) is SaaS-only and is
  marked so in §5. (LB-002; EVID-118)
- **GT-EINV-FR-076:** Every amount-arithmetic validation (line, tax, total,
  complement) shall compare with an absolute tolerance of one centesimal
  (±0.01) of the invoice currency, both horizontally (per item) and
  vertically (totals), per annex 5.2; intermediate values may carry 4+
  decimals before 2-decimal rounding. (LB-022; EVID-145)

### 3.2 Emission dates (D16 dated-instrument regime)

- **GT-EINV-FR-077:** The *Fecha y hora de emisión* (emission date/time)
  shall not be older than five days with respect to the *Fecha y hora de
  certificación* (certification date/time), counted from the day after the
  emission date (worked example: emission 23/12, certification 29/12 = day 6
  → reject); CIVA and CAIS are exempt from this window (retroactive
  constancias). (LB-003; EVID-119)
- **GT-EINV-FR-078:** The emission date shall not be later than the last day
  of the certification month: future dating is allowed only within the same
  calendar month (worked example: emission 01/11, certification 31/10 →
  reject). (LB-003; EVID-119)
- **GT-EINV-FR-079:** When the emitter's ISR or IVA affiliation changed and
  a DTE is emitted with a date in the previous month within the 5-calendar
  -day back-window, the DTE shall carry the OLD affiliation; past the
  permitted days, emission with the old affiliation shall not be allowed.
  Both the ISR rule and the IVA rule apply. (LB-003; EVID-119)
- **GT-EINV-FR-080:** The emission-date regime shall implement the D16
  dated-instrument mechanics: affiliation/regime parameters are resolved
  as-of the emission anchor date and snapshotted on the record at write time
  (D15); no transmission with a past date outside the 5-day window is
  permitted (hard no-override emission block); documents dated beyond the
  window are the historical, non-transmittable class and are never sent to
  certification. (LB-003; LB-023; EVID-119; D15/D16/D-GT10)
### 3.3 Emitter NIT / Mini-RTU eligibility

- **GT-EINV-FR-081:** The emitter NIT shall be validated against the
  Mini-RTU: existence/active registration and IVA affiliation consistent
  with the DTE type, with the printed exceptions — CIVA, FESP, RECI and RDON
  are emittable by NITs not affiliated to IVA. (LB-004; EVID-120)
- **GT-EINV-FR-082:** Mini-RTU MARCAS (1 domicilio no localizado; 2 omiso
  en IVA) shall be surfaced as non-blocking warnings on the emission surface
  — they never block generation. (LB-004; EVID-120)
- **GT-EINV-FR-083:** CAIS emission shall require the emitter to hold the
  special trait "DECRETO 29-89" (shared by SAT to certificadores per
  emitter); absence → reject. (LB-004; EVID-120)
- **GT-EINV-FR-084:** FEPE shall be barred when the emitter's only
  registered clasificación in the Mini-RTU casilla productorClasificacion is
  productor (1672) — "El tipo de documento no aplica para la clasificación
  de productor". (LB-004; EVID-120)
- **GT-EINV-FR-085:** The receptor NIT shall be validated against the Mini
  RTU for existence in SAT (annex 5.1.1), after depuración canonicalization
  (FR-094). (LB-022; EVID-145)
- **GT-EINV-FR-086:** NIT structural validation shall accept 2–12 digits
  with the check digit at the extreme right (K allowed after
  canonicalization), per annex 5.1.3. The check-digit algorithm is described
  (weights ×10 then mod 11) but the NIT coefficient table is NOT printed in
  the Reglas → OQ-006 (GOQ-49): the system shall NOT implement guessed
  mod-11 coefficients; until the official coefficient list is obtained, the
  product performs structural checks only and defers check-digit
  verification to the certificador/SAT validation chain. (LB-022; EVID-145)

### 3.4 Establishment gates

- **GT-EINV-FR-087:** The *código de establecimiento* (establishment code)
  shall reference an establishment active in SAT's registry for that NIT at
  the emission date — "El establecimiento no aparece activo en la SAT para
  ese NIT en esa fecha de emisión" → reject. (LB-005; EVID-121)
- **GT-EINV-FR-088:** CIVA/CAIS/RECI/FESP emission shall be gated by the RTU
  classification tables (stored as the §4 matrix, keyed on codes): Exento
  Constitucional 1703 → Centros educativos privados 1704 (CIVA SI / CAIS NO
  / RECI SI / FESP NO); Beneficio Fiscal Temporal 2204 → Maquila Decreto
  29-89 2224 (CAIS); Persona jurídica 887 → Universidades autorizadas 963 /
  Universidades Autorizadas Privadas 1084 / Confederación Deportiva 964
  (CIVA/RECI/FESP mix); Entidad del Estado 886 → Centros Educativos Públicos
  899 / Comité Olímpico Guatemalteco 965 / IGSS 966. (LB-005; EVID-121)
- **GT-EINV-FR-089:** FESP establishment matching shall follow the printed
  footnote: an emitter WITHOUT IVA affiliation may emit FESP only from an
  establishment matching the classification table; an emitter WITH IVA
  affiliation may emit FESP regardless of the table. (LB-005; EVID-121)
- **GT-EINV-FR-090:** Régimen primario/pecuario establishment eligibility
  shall use the Nube/código pairs (matrix data): primario 3696/1696 and
  3694/885; pecuario 3695/1696 and 3689/885 — each pair gates its régimen's
  factura/cambiaria columns, and all four pairs are FEPE-capable (last
  matrix column SI). (LB-005; EVID-121)
- **GT-EINV-FR-091:** The runtime result of the establishment gates shall be
  reported through the mensajes vocabulary — FEL_RCP305 (not in SAT
  registry), FEL_RCP306 (not active on emission date), FEL_RCP460
  (classification incompatible with DTE type), FEL_RCP485 (RANT activity
  mismatch), FEL_RCP497 (regime mismatch) — delivered through the
  certificador interface contract
  ([05_certificador-interface.md](05_certificador-interface.md) §establishment;
  mensajes sidecar per GT-CAT-FR-013). (LB-005; EVID-121; EVID-029 via
  master-index cluster E7)

### 3.5 Receptor identification

- **GT-EINV-FR-092:** The *ID del receptor* (receiver ID) shall take the
  forms NIT (RTU-validated), CUI (RENAP-validated), EXT or the literal CF;
  EXT shall be 3–18 characters, uppercase A–Z and digits 0–9, the special
  characters &, %, -, /, #, = only, and no spaces. (LB-006; EVID-122)
- **GT-EINV-FR-093:** CUI validation shall accept 12 or 13 digits with the
  check digit always the fifth digit from the right, the last four
  positions never counted in the check, weights ×10 then mod 11, and a
  departamento/municipio sanity table (variable — new municipios may extend
  it); RENAP web-service validation returns the name that the graphic
  representation must consign, and a deceased status only informs (never
  rejects). (LB-006; LB-022; EVID-122, EVID-145)
- **GT-EINV-FR-094:** The system shall canonicalize receiver IDs per annex
  5.1 depuración before any comparison: strip spaces; strip points; strip
  hyphens in the penultimate position; upcase a trailing k; and replace
  "C/F" or "CONSUMIDOR FINAL" with the exact literal "CF" — a receptor ID
  containing anything other than the exact string CF in the CF slot is
  invalid (C/F, C.F. and Consumidor Final are the printed incorrect
  examples). (LB-006; LB-022; EVID-122, EVID-145)
- **GT-EINV-FR-095:** A CF-receptor DTE of any of the 11 types — FACT,
  FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE, FACP — shall be
  rejected when its Gran Total equals or exceeds Q2,500.00, in GTQ or
  converted at the Banguat emission-date rate for foreign-currency
  documents; the 11-type list incl. FACP is the conservative product rule
  (R16) because the totals-section twin lists only 10 types → OQ-004
  (GOQ-47). Cross-refs: the per-type hooks GT-EINV-FR-036/037 in
  `01_document-types.md`. (LB-006; LB-007; LB-018; EVID-122, EVID-124,
  EVID-138; R16)
- **GT-EINV-FR-096:** FEPE shall accept only natural-person receptores: a
  receptor ID that resolves to an organización/empresa NIT → reject
  (cross-ref GT-EINV-FR-037 in `01_document-types.md`). (LB-006; EVID-122)

### 3.6 Lines, currency & product codes

- **GT-EINV-FR-097:** Each line's *Precio* shall equal Cantidad ×
  PrecioUnitario (within ±0.01). (LB-007; EVID-125)
- **GT-EINV-FR-098:** Discount bounds shall hold per line: Descuento ≤
  Precio; OtrosDescuento ≤ Precio − Descuento (discounts never exceed
  Precio). (LB-007; EVID-125)
- **GT-EINV-FR-099:** The Bien/Servicio flag shall be constrained per type:
  "B" mandatory for FACA, FCCA, FACP, FAAE, FCAE (and NEV, FEPE); "S"
  mandatory for espectáculos and RANT documents; an export line flagged
  Servicio carries no INCOTERM. (LB-007; LB-020; EVID-125, EVID-140)
- **GT-EINV-FR-100:** Item-count caps shall hold: espectáculos-públicos
  documents maximum 1 item; CIVA maximum 2 items (bienes y servicios).
  (LB-007; EVID-125)
- **GT-EINV-FR-101:** Currency rules: NCRE/NDEB/CIVA/CAIS shall carry the
  same Moneda as the referenced origin document; a CF-receptor document in
  foreign currency whose converted total reaches Q2,500.00 (Banguat
  emission-date rate) → reject (same cap as FR-095). (LB-007; EVID-124,
  EVID-125)
- **GT-EINV-FR-102:** *CodigoProducto* shall be accepted only on FACT,
  FCAM, NCRE and NDEB, and shall carry BOTH code families per the Reglas
  catalog (R17 — the GH XSD's GAL-only pattern is drift, never implemented
  alone): CGP10LBS/CGP20LBS/CGP25LBS/CGP35LBS/CGP100LBS subsidy codes with
  per-unit values Q8.00/16.00/20.00/28.00/0.00 (dated rows — "Sujeta a la
  vigencia de leyes y reglamentos"), and GALDIESEL which requires the IDP
  unidad gravable code 4. (LB-008; EVID-126; R17)
### 3.7 Frases engine

- **GT-EINV-FR-103:** Frase applicability shall follow the 12-tipo ×
  24-DTE-column matrix with 0/1/2 semantics (0 = not required, 1 =
  required, 2 = optional), stored as shared matrix data (§4; frases sidecar
  per GT-CAT-FR-009/010) and keyed on codes. CIVA/CAIS are outside the
  matrix columns. (LB-010; EVID-130)
- **GT-EINV-FR-104:** Frase tipos 1, 2, 3, 6 and 7 shall be auto-derived
  from the emitter's RTU obligation data ("se pueden obtener automáticamente
  del Registro Tributario Unificado (RTU)"), not hand-picked by the user;
  the derived frase + escenario is proposed at emission and may not
  contradict the registered obligation. (LB-010; EVID-130)
- **GT-EINV-FR-105:** The tipo-4 exemption catalog shall cover escenarios
  1–35 as printed (escenario 34 absent — gap [sic]) plus escenario 36 cited
  in the FACT/FCAM-only rule; the 2018 casos bound of escenarios 1–12 is
  superseded (R7) and treating >12 as error is forbidden. Each escenario
  carries its verbatim legal-legend text (e.g. esc. 1 exportaciones art. 7
  num. 2 Ley del IVA; esc. 15 menudeo Q100 threshold; esc. 22 NC/ND
  origin-without-IVA). (LB-011; LB-012; EVID-131, EVID-132; R7)
- **GT-EINV-FR-106:** Tipo-4 escenario selection shall enforce the printed
  gates: export documents (FACT/FCAM/FACP/NDEB/NCRE with Exp) require tipo 4
  escenario 1; NDEB/NCRE without Exp require escenario 22; FACT/FCAM/FESP
  without Exp whose items carry no IVA require tipo 4 present; FACT/FCAM
  admit the enumerated escenario list {2,3,6,7,9–19,21,23–32}; FESP admits
  {2, 11}; RDON requires 4; RECI admits {2,5,6,8,16,20,33}; escenario 36 is
  FACT/FCAM-only; escenario 21/23 gate FACT/FCAM/NCRE/NDEB and 24
  additionally RECI (condominios 1050); the same tipo+escenario pair may
  appear only once per DTE (RANT excepted); CIVA shall carry no frase at
  all. (LB-011; LB-012; EVID-131, EVID-132)
- **GT-EINV-FR-107:** Tipo-8 (ISR exenciones) scenarios shall be gated by
  type, affiliation and personería: esc. 1 universidades
  (FACT/FCAM/RECI/RDON + General + personería 740); esc. 2 centros educativos
  privados (RECI); esc. 3 iglesias (RECI/RDON + General + 735/736); esc. 4
  entes no lucrativos; esc. 5 cooperativas (+710); esc. 6/7/9/10/11
  FACT/FCAM/NCRE/NDEB + General; esc. 8 with personería 715/716.
  (LB-011; EVID-131)
- **GT-EINV-FR-108:** Tipo-9 (apoyo social) amounts shall compute per the
  Aclaración: escenario 1 value = Descuento Especial del producto ×
  cantidad (gas-propano cylinders); escenario 2 = gallons × per-gallon
  descuento (gasolina regular/diésel); escenario 3 total = Gran Total + the
  quetzal value of the apoyo social; the escenario-1 legend still cites the
  editorial placeholder "Decreto XX-2022" [sic] → OQ-003 (GOQ-46) — the
  legend text is stored verbatim until the governing decreto (45-2022 /
  05-2023) is confirmed. (LB-013; EVID-133)
- **GT-EINV-FR-109:** Régimen frases 10/11/12 (and their escenarios under
  the 2.6.1 rules 29–36) shall be validated against the RTU-registered
  forma de cálculo: Régimen Primario Productos y Comercializador = 1.5%
  sobre las ventas brutas; Régimen Primario Exportador = 2% sobre las
  ventas brutas; Régimen Pecuario = 1.5% ventas brutas / 10% sobre las
  utilidades; Régimen Pecuario Exportador = 2% sobre las ventas brutas;
  escenario selection is additionally gated by the Exp flag and
  ClasificacionEmisor = 'Intermediario' (clasificación 1674). (LB-011;
  LB-013; EVID-131, EVID-133)
- **GT-EINV-FR-110:** Frase tipos 1 (escenario 3) and 7 shall carry the
  resolution number (and date where the catalog flags it) in the DTE's
  NumeroResolucion/FechaResolucion casillas — "El número de resolución se
  debe incorporar en el XML del DTE en la casilla correspondiente".
  (LB-013; EVID-133)

### 3.8 Tax computation & rate constants (dated rows)

- **GT-EINV-FR-111:** IVA shall use unidades gravables 1 (12.00%) and 2
  (0%), always price-inclusive: MontoGravable = (Precio − Descuento −
  OtrosDescuento) / 1.12 when the unidad is 1; no division when the unidad
  is 2; MontoImpuesto = MontoGravable × rate; CantidadUnidadesGravables
  shall NOT be present for IVA; an export document (Exp) shall use unidad 2.
  Worked example: Precio 560.00 → MontoGravable 500.00, IVA 60.00, total
  560.00 (no IVA added on top). (LB-014; EVID-134)
- **GT-EINV-FR-112:** Simplified-regime types (FPEQ, FCAP, FACA, FCCA, FAPE,
  FCPE, FAAE, FCAE, FARP, FCRP, FPEC, FCPC, FEPE and the no-tax family per
  the capability matrix) shall carry NO IVA node — the document simply
  states no IVA ("IVA N/A" columns in the worked examples). (LB-009;
  LB-014; EVID-127, EVID-134)
- **GT-EINV-FR-113:** NC/ND emission more than two months after the
  affected invoice shall produce an informative (non-blocking) advisory: the
  Reglas state the two-month registration window of Ley IVA art. 17 and only
  the fiscal-credit recognition is lost — there is no hard emission ban.
  (LB-014; EVID-134)
- **GT-EINV-FR-114:** IDP shall compute per-unit with the 13 specific rates
  as dated rows (§4): gasolina superior Q4.70, gasolina regular Q4.60,
  gasolina de aviación Q4.70, diésel Q1.30, gas oil Q1.30, kerosina/DPK
  Q0.50, nafta Q0.50, fuel oil Q0.00, GLP granel Q0.50, GLP carburación
  Q0.50, petróleo crudo combustible Q0.00, otros derivados Q0.00, asfaltos
  Q0.00 — MontoImpuesto = rate × CantidadUnidadesGravables with NO
  MontoGravable; non-GTQ documents convert the Q rate at the Banguat
  emission-date exchange rate (USD = tasa de referencia; other currencies =
  tipo de cambio de venta; fallback = last published rate). (LB-015;
  EVID-135)
- **GT-EINV-FR-115:** ITH (*impuesto al turismo hospedaje*, lodging tourism
  tax) shall compute 10% over the monto gravable (the exento unidad exists
  for exempt lodging); the former Tarjeta de Turismo (US$5 → US$10, moved
  to Migración) is included in NO DTE. (LB-016; EVID-136)
- **GT-EINV-FR-116:** ITP (*impuesto al turismo pasajes*, exit-ticket
  tourism tax) shall compute USD30.00 per aerial exit ticket and USD10.00
  per maritime exit ticket, converted at the Banguat reference rate of the
  day BEFORE the emission date; unidad 3 (aérea exenta per Decreto 31-2022)
  requires frase tipo 9 escenario 4 on the document. Worked example: 2
  boletos × USD30 × Q7.50 = Q450.00. (LB-016; EVID-136)
- **GT-EINV-FR-117:** TDP (*timbre de prensa*, press stamp duty) shall
  compute 0.50% ("cinco (5) por millar") over the monto gravable.
  (LB-016; EVID-136)
- **GT-EINV-FR-118:** IFB (*impuesto por seguro contra incendios*, fire
  insurance tax — Bomberos) shall compute 2.00% over the monto gravable.
  (LB-016; EVID-136)
- **GT-EINV-FR-119:** MUN (*tasa municipal*, municipal rate) shall accept a
  variable free amount with the structured 7-digit unit code DDMMCCC (DD
  departamento, MM municipio, CCC concepto — certificador-assigned or 000).
  (LB-016; EVID-136)
- **GT-EINV-FR-120:** IDB (*impuesto sobre bebidas alcohólicas*, alcoholic
  beverages tax) shall compute 6.00% (cervezas), 7.50% (vinos, espumosos,
  vermouth, sidras, mezcladas, otras fermentadas) or 8.50% (destiladas) over
  the suggested consumer price per unidad gravable — a separate base from
  the line price. (LB-017; EVID-137)
- **GT-EINV-FR-121:** TAB (*impuesto al tabaco*, tobacco tax) shall compute
  100.00% over the factory sale price (paquete de 10 cajetillas de 20
  cigarrillos) or 75.00% over the suggested consumer price, per its two
  unidades. (LB-017; EVID-137)
- **GT-EINV-FR-122:** CEM (*impuesto al cemento*, cement tax) shall compute
  Q1.50 per 42.5-kilogram bag (CantidadUnidadesGravables × rate, with the
  standard FX clauses for non-GTQ documents). (LB-017; EVID-137)
- **GT-EINV-FR-123:** IBN (*impuesto sobre bebidas no alcohólicas*,
  non-alcoholic beverages tax) shall compute per unit: Q0.18 gaseosas y
  jarabes; Q0.12 isotónicas o deportivas; Q0.10 jugos y néctares; Q0.10
  bebidas de yogur; Q0.08 agua natural envasada hasta cuatro litros
  (natural water over four liters excepted). (LB-017; EVID-137)
- **GT-EINV-FR-124:** TAP (*tarifa portuaria*, port tariff) shall compute
  USD0.05 per unit, converted for non-USD documents at the Banguat rate of
  the day before the emission date. (LB-017; EVID-137)
- **GT-EINV-FR-125:** The tax-capability matrix (26 types × 12 taxes, §4
  data keyed on codes) shall gate which Impuesto nodes each type may carry:
  NDEB/NCRE exclude Tasa Municipal and Tarifa Portuaria (all other taxes
  allowed); NABN/RDON/RECI carry none; FESP and CIVA carry IVA only; the
  agropecuario, electrónico, régimen primario/pecuario and FEPE types carry
  none; per-tax casilla presence (MontoGravable / CodigoUnidadGravable /
  CantidadUnidadesGravables / MontoImpuesto) follows the A–D usage matrix.
  (LB-009; EVID-127)
- **GT-EINV-FR-126:** FESP retention arithmetic shall hold: ISR a Retener =
  Σ MontoGravable × 5% (Decreto 10-2012, as modified by Decreto 4-2019 per
  the changelog); IVA a Retener = the document's TotalMontoImpuesto of IVA;
  TotalMenosRetenciones = Σ MontoGravable − ISR a Retener (±0.01).
  (LB-021; EVID-141)
- **GT-EINV-FR-127:** FEPE ICT retention arithmetic shall hold: RetencionICT
  = Gran Total × 1.5%; TotalMenosRetenciones = Gran Total − RetencionICT
  (±0.01); the "ICT" expansion is unprinted → OQ-008 (GOQ-24; statutory
  hook Decreto 31-2024 art. 4 pending acquisition — GOQ-13 kin).
  (LB-021; EVID-141)
- **GT-EINV-FR-128:** The agropecuario payment family (frase tipo 6) shall
  carry the RTU-registered form: 5% sobre las ventas brutas (with retention)
  or 5% sobre las utilidades ("no retener") — the frase legend text differs
  per form and the printed legend must match the registered election.
  (LB-013; EVID-133)
- **GT-EINV-FR-129:** Régimen payment rates (frases tipo 10/11) shall
  compute: primario 1.5% sobre las ventas brutas (Productos y
  Comercializador) or 2% sobre las ventas brutas (Exportador); pecuario
  1.5% sobre las ventas brutas, 10% sobre las utilidades, or 2% sobre las
  ventas brutas (Exportador) — each tied to the RTU forma de cálculo
  (FR-109). (LB-013; EVID-133)
- **GT-EINV-FR-130:** Every rate and validation constant in this section
  shall be stored as a decree-bound DATED ROW (impuesto/parameter, value,
  unit/base, valid_from = 2024-12-19 — the Reglas v2.0 row date — plus
  provenance), because the printed values are "Sujeta a la vigencia de
  leyes y reglamentos": a decree reform appends a row (D16), never
  overwrites, and the resolved value is snapshotted on the document at
  write time (D15) → watchlist OQ-007 (GOQ-50). (LB-008; LB-015; LB-017;
  LB-023; EVID-126, EVID-135, EVID-137)
- **GT-EINV-FR-131:** Until GOQ-20 is answered (per-item Impuesto cap: GH
  XSD caps at 2, CD allows 20), pre-validation shall NOT hard-code 3-tax
  single-line emission as valid: the conservative per-line tax-count cap of
  GT-EINV-FR-050 (`02_dte-schema.md`) stays in force and multi-tax lines
  are split. (LB-009; EVID-127; GOQ-20 via `02_dte-schema.md` OQ-003)
### 3.9 Totals & complement arithmetic

- **GT-EINV-FR-132:** Document totals shall compute: per line Total =
  (Precio − Descuento − OtrosDescuento) + the MontoImpuesto of the taxes
  that are sumable to the DTE (IVA excluded — already inside the price);
  Gran Total = Σ Total (all with ±0.01 tolerance). (LB-018; EVID-138)
- **GT-EINV-FR-133:** NCRE totals (Total and Gran Total) shall not exceed
  the registered totals of the origin document, and the CAIS Gran Total
  shall not exceed the origin's, in both cases only when the origin is NOT
  a "Régimen antiguo" (legacy paper) document — caps are enforced against
  FEL origins; paper origins are identified by the Código-Tipo list (FR-137,
  GOQ-48). (LB-018; LB-021; EVID-138, EVID-141)
- **GT-EINV-FR-134:** Complement applicability shall follow the 14 × 26
  catalog matrix with 0/1/2 semantics (0 = must not be present, 1 = may be
  filled or empty, 2 = must be filled), keyed on complement NAMES (the
  printed numbering skips 13 and the TOC labels drift — FR-073): required —
  FESP → Retenciones de factura especial; FEPE → Retenciones de factura
  específica; NCRE/NDEB → Referencias de nota de crédito y débito; CIVA/CAIS
  → Referencias de constancias; NEV → Traslado de mercancías; FACP →
  Exportación provisional; cambiaria types → Abonos de factura cambiaria.
  Canonical name/URI values remain GOQ-21 (GT-EINV-FR-050 context in
  `02_dte-schema.md`). (LB-019; EVID-139)
- **GT-EINV-FR-135:** The Exportaciones complement shall be required on
  non-NC/ND export documents (Exp flag) and shall carry the consignatario
  blocks with INCOTERM required only for goods lines ("Solo cuando sea B en
  el campo B/S"), the INCOTERM table including DPU (DTA removed), the
  provisional-DTE reference fields and the DUCA number; NC/ND mirror the
  origin's Exp flag; NABN/RDON/RECI/FESP/CIVA/CAIS can never export.
  (LB-007; LB-020; EVID-124, EVID-140)
- **GT-EINV-FR-136:** FACP finalization references shall validate: the
  referenced UUID must exist in SAT's record, belong to a FACP, be vigente
  (an annulled provisional → "La factura provisional se encuentra anulada"),
  and match the new document's currency and receptor. (LB-020; EVID-140)
- **GT-EINV-FR-137:** Each NCRE/NDEB shall reference exactly ONE origin DTE
  ("Cada Nota de Crédito o de Débito solo puede hacer referencia a un único
  DTE"); the origin shall be a FEL FACT/FCAM or a legacy paper document
  whose Código-Tipo is in the printed list {1, 2, 7, 8, 9, 30, 32, 37, 38,
  53, 57, 60, 62, 63, 66, 67, 68, 69, 72} (interpretation of the list →
  OQ-005, GOQ-48); cross-certificador NC/ND is allowed — the
  same-certificador restriction is explicitly "sin efecto" (supersession
  since Reglas v1.6). (LB-021; EVID-141)
- **GT-EINV-FR-138:** Referencias de constancias (CIVA/CAIS) shall
  reference origins FACT/FCAM/FESP; MontoIVAExento shall not exceed the
  origin's total IVA (±2-decimals tolerance); while a vigente CIVA/CAIS
  exists for an origin authorization number, another shall not be emitted.
  (LB-021; EVID-141)
- **GT-EINV-FR-139:** The Cobros por cuenta ajena (third-party collections)
  complement shall compute MontoCobroIVA = BaseImponible × 12% (±0.01).
  (LB-021; EVID-141)

## 4. Data Model

Machine-readable twins: the frases/unidades/mensajes sidecars live in
[../catalogs/_INDEX.md](../catalogs/_INDEX.md) (CAT-FRS / CAT-UGR / CAT-MSG;
GT-CAT-FR-009..015); the matrices below are seed registry data both sides
derive their validators from. **All rate rows are decree-bound dated rows
(GOQ-50): valid_from = 2024-12-19 (Reglas v2.0 row date; vigencia abril
2025); reforms append rows, never overwrite (D16).**

**Table 1 — Rate & validation constants (dated rows; values as printed by
Reglas v2.0):**

| Parameter | Value | Unit / base | valid_from | Reference |
|-----------|-------|-------------|------------|-----------|
| IVA | 12% / 0% | price-inclusive; base = (Precio − Desc − OtrosDesc)/1.12; export ⇒ unidad 2 | 2024-12-19 | FR-111; LB-014 |
| IDP (13 unidades) | Q4.70 / Q4.60 / Q4.70 / Q1.30 / Q1.30 / Q0.50 / Q0.50 / Q0.00 / Q0.50 / Q0.50 / Q0.00 / Q0.00 / Q0.00 | per gallon; no MontoGravable; Banguat emission-date FX | 2024-12-19 | FR-114; LB-015 |
| ITH | 10% (+ exento unidad) | on monto gravable | 2024-12-19 | FR-115; LB-016 |
| ITP | USD30.00 aérea / USD10.00 marítima / 0 exenta (unidad 3, Dec 31-2022) | per ticket; day-before Banguat reference rate; unidad 3 ⇒ frase 9-esc.4 | 2024-12-19 | FR-116; LB-016 |
| TDP | 0.50% | cinco por millar on monto gravable | 2024-12-19 | FR-117; LB-016 |
| IFB | 2.00% | on monto gravable | 2024-12-19 | FR-118; LB-016 |
| MUN | variable (free amount) | unit code DDMMCCC | 2024-12-19 | FR-119; LB-016 |
| IDB | 6.00% / 7.50% / 8.50% | on suggested consumer price per unidad | 2024-12-19 | FR-120; LB-017 |
| TAB | 100.00% / 75.00% | factory price / suggested consumer price | 2024-12-19 | FR-121; LB-017 |
| CEM | Q1.50 | per 42.5 kg bag | 2024-12-19 | FR-122; LB-017 |
| IBN | Q0.18 / Q0.12 / Q0.10 / Q0.08 | per unit (gaseosas / isotónicas / jugos-yógur / agua ≤4L) | 2024-12-19 | FR-123; LB-017 |
| TAP | USD0.05 | per unit; day-before Banguat | 2024-12-19 | FR-124; LB-017 |
| FESP ISR retención | 5% | Σ MontoGravable (Dec 10-2012, mod. Dec 4-2019); IVA ret. = TotalMontoImpuesto | 2024-12-19 | FR-126; LB-021 |
| FEPE ICT retención | 1.5% of Gran Total | Dec 31-2024 art. 4 (expansion GOQ-24) | 2024-12-19 | FR-127; LB-021 |
| Agropecuario (frase 6) | 5% ventas brutas / 5% utilidades | RTU forma de pago | 2024-12-19 | FR-128; LB-013 |
| Primario (frase 10) | 1.5% ventas brutas / 2% exportador | RTU forma de cálculo | 2024-12-19 | FR-129; LB-013 |
| Pecuario (frase 11) | 1.5% ventas brutas / 10% utilidades / 2% exportador | RTU forma de cálculo | 2024-12-19 | FR-129; LB-013 |
| Gas-subsidy per-unit values | Q8.00 / 16.00 / 20.00 / 28.00 / 0.00 (CGP10/20/25/35/100LBS) | per cylinder; "Sujeta a la vigencia de leyes y reglamentos" | 2024-12-19 | FR-102/108; LB-008 |
| CF receptor cap | Q2,500.00 Gran Total (GTQ or FX-converted) | 11 types incl. FACP (R16; GOQ-47) | 2024-12-19 | FR-095; LB-006 |
| Emission windows | 5 días back (from day after emission; CIVA/CAIS exempt) / same-calendar-month future / 5-day affiliation lookback | — | 2024-12-19 | FR-077..079; LB-003 |
| Arithmetic tolerance | ±0.01 absolute | any currency, horizontal + vertical | 2024-12-19 | FR-076; LB-022 |
**Table 2 — Frases matrix summary (12 tipos × 24 DTE columns; 0/1/2 — full
grid in the sidecar; key applicability from EVID-130):**

| Tipo | Name / meaning | RTU-auto | Key applicability |
|------|----------------|----------|-------------------|
| 1 | ISR retención status | yes | required(1) FACT/FCAM/NCRE/NDEB |
| 2 | Agente retención IVA | yes | optional(2) FACT/FCAM/NCRE/NDEB |
| 3 | No crédito fiscal | yes | required(1) FPEQ/FCAP/FACA/FCCA/FAPE/FCPE/FAAE/FCAE/FARP/FCRP/FPEC/FCPC |
| 4 | Exento / no afecto al IVA | no | optional FACT/FCAM/RDON/RECI/FESP; required NCRE/NDEB; escenarios 1–35 (+36 cited) |
| 5 | FESP | no | required(1) FESP |
| 6 | Agropecuario 5% | yes | required(1) FACA/FCCA |
| 7 | Régimen electrónico | yes | required(1) FAPE/FCPE/FAAE/FCAE |
| 8 | ISR exenciones | no | optional(2) FACT/FCAM/RDON/RECI/NCRE/NDEB (personería gates) |
| 9 | Apoyo social / textos NEV-RANT-FACP | no | optional FACT/FCAM/FPEQ/FCAP/NCRE/NDEB + FACA/FCCA(2); required(1) NEV/RANT; FACP esc. 11 |
| 10 | Régimen Primario | no | required(1) FARP/FCRP |
| 11 | Régimen Pecuario | no | required(1) FPEC/FCPC |
| 12 | FEPE | no | required(1) FEPE |

**Table 3 — Complemento matrix summary (14 × 26; 0 = forbidden, 1 =
optional/may be filled, 2 = required; keyed on names, numbering unstable):**

| Complement | Applicability (2 = required) |
|------------|------------------------------|
| Exportación | 1 for FACT/FCAM/FACA/FCCA/FAPE/FCPE/FAAE/FCAE + FARP/FCRP/FPEC/FCPC (requiredness driven by the Exp rules, FR-135) |
| Retenciones de factura especial | 2 FESP |
| Abonos de factura cambiaria | 2 FCAM/FCCA/FCPE/FCAE/FCRP/FCPC |
| Referencias de nota de crédito y débito | 2 NCRE/NDEB |
| Cobros por cuenta ajena | 1 FACT/FCAM |
| Espectáculos públicos | 1 FACT/FCAM/FPEQ/FCAP/FAPE/FCPE |
| Referencias de constancias | 2 CIVA/CAIS |
| Medios de pago | 1 FACT/FCAM/FPEQ/FCAP/FACA/FCCA/FAPE/FCPE/FAAE/FCAE |
| Decreto 31-2022 (boletos aéreos) | 1 same set as Medios de pago |
| LEPP (Ley Electoral y de Partidos Políticos) | 1 RDON |
| Traslado de mercancías | 2 NEV |
| Exportación provisional | 2 FACP |
| Retenciones de factura específica | 2 FEPE |

**Table 4 — Establishment classification gates (matrix seed; codes, not row
numbers):**

| RTU classification | Sub-classifications (code) | CIVA | CAIS | RECI | FESP |
|--------------------|---------------------------|------|------|------|------|
| Exento Constitucional (1703) | Centros educativos privados (1704) | SI | NO | SI | NO |
| Beneficio Fiscal Temporal (2204) | Maquila Decreto 29-89 (2224) | NO | SI | NO | NO |
| Persona jurídica (887) | Universidades autorizadas (963) / Universidades Autorizadas Privadas (1084) / Confederación Deportiva (964) | SI | NO | SI (964: NO) | SI (964: NO) |
| Entidad del Estado (886) | Centros Educativos Públicos (899) / Comité Olímpico Guatemalteco (965) / IGSS (966) | per matrix | per matrix | per matrix | per matrix |

Régimen establishment pairs (all FEPE-capable): 3696/1696, 3694/885
(primario); 3695/1696, 3689/885 (pecuario).

## 5. Odoo Mapping

Layer semantics (per the D2 dual-validation contract): `odoo` = client-side
pre-validation surface (shared rules mirrored for early UX rejection) or
data capture; `saas` = authoritative validation / registry-fed rules the
client cannot mirror; `shared` = contract items both sides implement
identically from the §4 data (authoritative resolution stays SaaS-side).
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required. Version-regime note (D12): every rule in this file is
keyed to the Reglas v2.0 vintage (19/12/2024, vigencia abril 2025) and its
dated rows (§4 Table 1); a rulebook revision = new dated rows + adaptation
window, never in-place edits. Applicability note (D15/D16): all
dated-parameter FRs (rates, caps, windows) resolve as-of the emission date,
snapshot the resolved value on the record, and carry valid_from/valid_to
rows; historical records are the non-transmittable class (FR-080).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-071 | saas | — | — | Pipeline order enforced at compilation; odoo inherits GT-EINV-FR-068's local generation gate |
| FR-072 | saas | — | — | Error-mapping registry SaaS-side; reclassification-tolerant keys (content + message text) |
| FR-073 | shared | — | — | Contract item: both sides key rules/matrices on codes; locator metadata never an identity |
| FR-074 | saas | — | — | Rulebook-vintage dated rows in the SaaS registry; surfaced read-only in odoo |
| FR-075 | shared | — | — | The dual-validation contract itself; mirror set derived from the same §4 data |
| FR-076 | shared | account.move, account.move.line | amount fields | Tolerance constant shared; odoo pre-check mirrors ±0.01 |
| FR-077 | shared | account.move | invoice_date | Mirrored client-side early UX; authoritative SaaS; CIVA/CAIS exemption flag on doc type |
| FR-078 | shared | account.move | invoice_date | Same-month-future check mirrored |
| FR-079 | shared | res.partner, account.move | regime fields, invoice_date | Old-affiliation snapshot during lookback |
| FR-080 | shared | account.move | invoice_date, regime snapshot fields | D15/D16: anchor-date resolution + snapshot-on-write; historical class non-transmittable |
| FR-081 | saas | res.company | vat, afiliacion | Mini-RTU lookup SaaS-side (certificador feed); odoo caches company afiliación for UX |
| FR-082 | odoo | res.partner / res.company | marca flags | Non-blocking warnings surfaced at emission; data SaaS-fed |
| FR-083 | saas | res.company | special traits | "DECRETO 29-89" trait from mini-RTU feed |
| FR-084 | saas | res.company | clasificación | productorClasificacion (1672) gate |
| FR-085 | saas | res.partner | vat | Mini-RTU existence check after FR-094 canonicalization |
| FR-086 | shared | res.partner | vat | Structural checks both sides; check-digit deferred (GOQ-49) — no mod-11 guesses shipped |
| FR-087 | saas | account.move | establishment code | Active-at-emission-date lookup vs registry feed |
| FR-088 | shared | establishment classification registry | matrix rows | §4 Table 4 seed data both sides; codes not row numbers |
| FR-089 | saas | res.company | afiliacion + establishment | Footnote-6 logic SaaS-side |
| FR-090 | shared | establishment pair registry | matrix rows | Régimen pair data |
| FR-091 | saas | — | — | Mensajes mapping via GT-CAT-FR-013; delivery contract = 05_certificador-interface.md §establishment |
| FR-092 | shared | res.partner | l10n_latam_identification_type_id, vat | EXT charset + form rules mirrored |
| FR-093 | shared | res.partner | vat (CUI) | CUI algorithm shared; RENAP name consignment on report |
| FR-094 | shared | res.partner | vat | Depuración canonicalization both sides (single shared helper) |
| FR-095 | shared | account.move | amount_total, doc type | Q2,500 CF cap mirrored; FX conversion needs the rate feed (SaaS-supplied) |
| FR-096 | shared | res.partner | company_type | Natural-person gate mirrored |
| FR-097 | shared | account.move.line | price_unit, quantity, price_total | Line arithmetic mirror |
| FR-098 | shared | account.move.line | discount fields | Bounds mirror |
| FR-099 | shared | product.template / move.line | tipo B/S flag | Per-type defaults from doc type |
| FR-100 | shared | account.move | line count | UX caps mirrored |
| FR-101 | shared | account.move | currency_id | Origin-currency match + FX cap mirror |
| FR-102 | shared | product.product | code (CGP*/GAL*) | Both families per R17; GALDIESEL⇒IDP unidad 4 validation |
| FR-103 | shared | account.move | frase_ids | Matrix from sidecar GT-CAT-FR-009/010 |
| FR-104 | saas | res.company | RTU obligations | Auto-derivation SaaS-side (RTU feed); proposal surfaced in odoo |
| FR-105 | shared | frase escenario catalog | rows | 1–35 + 36; sidecar carries legend texts |
| FR-106 | shared | account.move | frase_ids | Escenario gates mirrored |
| FR-107 | shared | res.partner, account.move | personería | Tipo-8 gates mirrored |
| FR-108 | shared | account.move.line | subsidy fields | Apoyo-social arithmetic mirror; "XX-2022" legend verbatim (GOQ-46) |
| FR-109 | saas | res.company | RTU forma de cálculo | RTU-linked escenario validation SaaS-side |
| FR-110 | shared | account.move | NumeroResolucion/FechaResolucion | Resolution capture in odoo; validated SaaS |
| FR-111 | shared | account.tax | price_include=True, amount | Price-inclusive IVA both sides must agree; /1.12 formula shared |
| FR-112 | shared | l10n_latam.document.type | tax availability | No-IVA doc types seeded without IVA taxes |
| FR-113 | odoo | account.move | reversal wizard | Informative advisory surfaced at UX; SaaS stamps informative flag |
| FR-114 | saas | account.tax (IDP) | per-unit rates | Banguat feed SaaS-side; rates as dated rows §4 |
| FR-115 | shared | account.tax (ITH) | amount=10 | — |
| FR-116 | saas | account.tax (ITP) | USD per-unit | Day-before Banguat rate SaaS-fed; frase 9-esc.4 gate shared |
| FR-117 | shared | account.tax (TDP) | amount=0.5 | — |
| FR-118 | shared | account.tax (IFB) | amount=2 | — |
| FR-119 | shared | account.tax (MUN) | free amount + DDMMCCC code | — |
| FR-120 | shared | account.move.line | suggested consumer price base | Separate base field needed (IDB) |
| FR-121 | shared | account.move.line | factory/suggested price bases | TAB two bases |
| FR-122 | saas | account.tax (CEM) | Q1.50/bag | FX clause SaaS-fed |
| FR-123 | saas | account.tax (IBN) | per-unit Q | FX clause SaaS-fed |
| FR-124 | saas | account.tax (TAP) | USD0.05 | Day-before Banguat |
| FR-125 | shared | l10n_latam.document.type × account.tax | matrix rows | Tax-capability matrix seed |
| FR-126 | shared | account.move (FESP) | retention fields | ISR 5% + IVA arithmetic mirror |
| FR-127 | shared | account.move (FEPE) | RetencionICT fields | 1.5% arithmetic mirror; label pending GOQ-24 |
| FR-128 | shared | account.move | frase tipo 6 | Legend text per registered form |
| FR-129 | shared | account.move | frases 10/11 | Rates tied to RTU election (FR-109) |
| FR-130 | saas | rate registry | dated rows | valid_from/valid_to + provenance; snapshot-on-write |
| FR-131 | shared | account.move.line | tax_ids count | Conservative cap until GOQ-20; mirrors GT-EINV-FR-050 |
| FR-132 | shared | account.move | amount fields | Totals arithmetic mirror |
| FR-133 | saas | account.move (NCRE/CAIS) | ref origin totals | Origin-registry lookup SaaS-side; Régimen antiguo detection |
| FR-134 | shared | account.move | complement wrappers | Matrix from §4 Table 3; names keyed (GOQ-21 values pending) |
| FR-135 | shared | account.move (export) | complemento fields, incoterm | INCOTERM incl. DPU list shared |
| FR-136 | saas | account.move (FACP→FACT) | ref UUID | SAT-record lookup SaaS-side |
| FR-137 | saas | account.move (NC/ND) | ref_document_ids | Single-origin + origin-type gate SaaS-side (registry); odoo enforces single-ref UX |
| FR-138 | saas | account.move (CIVA/CAIS) | ref constancia fields | Origin totals + vigente-constancia registry check |
| FR-139 | shared | account.move | cobro ajeno fields | 12% arithmetic mirror |
## 6. Acceptance Criteria

- **AC-001:** Given a DTE whose XML fails XSD conformance, when validated,
  then no business rule is evaluated and the ERC reject path returns
  "El XML enviado no cumple con el esquema del XSD" (FR-071).
- **AC-002:** Given SAT reclassifies a rule from primaria-rechaza to
  secundaria-informa, when the change lands, then no product code changes —
  the error-mapping entry (keyed on rule content + message text) simply
  reports the new severity (FR-072/073).
- **AC-003:** Given emission 23/12 and certification 29/12 (6 days, counted
  from the day after emission), when a FACT is submitted, then it is
  rejected; given the same dates on a CIVA, then it passes the 5-day rule
  (FR-077).
- **AC-004:** Given emission 01/11 with certification 31/10, when
  validated, then the document is rejected (future date outside the
  certification month); given emission 30/10 with certification 31/10, then
  it passes (FR-078).
- **AC-005:** Given an affiliation change effective this month and a DTE
  dated 3 days before the change (previous month), when emitted, then the
  DTE carries the OLD affiliation; given a date beyond the 5-day window,
  then the old affiliation is refused (FR-079).
- **AC-006:** Given a partner NIT input with spaces, points, a penultimate
  hyphen and a trailing k, when canonicalized, then all are stripped/upcased
  per depuración; given a receptor value "C.F.", when validated, then it is
  rejected — only the exact literal "CF" passes (FR-094).
- **AC-007:** Given a CF-receptor FACT with Gran Total Q2,499.99, when
  validated, then it passes; given Q2,500.00 (or a USD total whose
  emission-date conversion reaches Q2,500.00), then it is rejected; given
  the same on FACP, then it is rejected (11-type conservative list, R16)
  (FR-095, FR-101).
- **AC-008:** Given a line with Precio 560.00, Descuento 0, unidad
  gravable 1, when computed, then MontoGravable = 500.00, IVA = 60.00 and
  the total adds no further IVA (price-inclusive model) (FR-111, FR-132).
- **AC-009:** Given 10 gallons of gasolina superior on a GTQ FACT, when IDP
  is computed, then MontoImpuesto = 10 × Q4.70 = Q47.00 and no MontoGravable
  is present (FR-114).
- **AC-010:** Given 2 aerial exit tickets with the day-before Banguat
  reference rate Q7.50, when ITP is computed, then 2 × USD30.00 × 7.50 =
  Q450.00; given unidad 3 without frase tipo 9 escenario 4, then the
  document is rejected (FR-116).
- **AC-011:** Given a FESP with Σ MontoGravable Q40,000.00 and document IVA
  Q3,200.00, when the retention complement is computed, then ISR a Retener
  = Q2,000.00, IVA a Retener = Q3,200.00 and TotalMenosRetenciones =
  Q38,000.00 (FR-126).
- **AC-012:** Given a FEPE with Gran Total Q10,000.00, when the ICT
  retention is computed, then RetencionICT = Q150.00 and
  TotalMenosRetenciones = Q9,850.00 (FR-127).
- **AC-013:** Given an export FACT carrying Exp without frase tipo 4
  escenario 1, when validated, then it is rejected; given an NCRE without
  Exp whose tipo-4 escenario is not 22, then it is rejected (FR-106).
- **AC-014:** Given a declared IVA of 2,142.87 against a computed
  17,857.142857 × 12% = 2,142.86, when compared, then it passes (within the
  printed min/max band 2,142.85–2,142.87, ±0.01) (FR-076).
- **AC-015:** Given any NIT, when the validation module runs, then no mod-11
  check-digit verdict is produced (structural checks only) until the
  official coefficient table is obtained — GOQ-49 (FR-086).
- **AC-016:** Given an establishment inactive at the emission date, when
  the DTE is validated, then it is rejected and the surfaced runtime
  mensaje is FEL_RCP306 (FR-087, FR-091).
- **AC-017:** Given an NCRE referencing two origin DTEs, then it is
  rejected; given an NCRE referencing a FACT certified by a different
  certificador, then it is allowed (single-origin + cross-certificador
  rules) (FR-137).
- **AC-018:** Given the rate registry, when inspected, then every row of §4
  Table 1 carries valid_from 2024-12-19 with provenance, and a decree
  reform appends a new row without mutating history (FR-130).
- **AC-019:** Given a CodigoProducto CGP100LBS on an FPEQ, when validated,
  then it is rejected (product codes only on FACT/FCAM/NCRE/NDEB); given
  GALDIESEL with an IDP unidad gravable ≠ 4 on a FACT, then it is rejected
  (FR-102).
- **AC-020:** Given a FESP without the Retenciones de factura especial
  complement, when validated, then it is rejected; given the complement
  registry, when keyed, then lookups are by complement name — never by the
  printed catalog row number (13 skipped) (FR-134).

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.1);
question text verbatim from the register where printed. This file OWNS
GOQ-44, GOQ-45, GOQ-46, GOQ-47, GOQ-48, GOQ-49, GOQ-50 and GOQ-24. Kin ids
referenced inline only: GOQ-20 (per-item Impuesto cap, owned by
`02_dte-schema.md`), GOQ-21 (complement name/URI values, owned by
`02_dte-schema.md`), GOQ-13 (Decreto 31-2024 acquisition, owned by
`01_document-types.md`), GOQ-02 (channel umbrella, catalogs-owned).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-44 (owned): "Reglas “v1.7.10 1 de 132 Febrero 2025” cover footer: did a real 1.7.10 interim printing exist (affects citation hygiene only)?" | no | GT synthesis wave S-GT1 | open |
| OQ-002 | GOQ-45 (owned, guard): "Reglas editorial drift: changelog's “2.2.5 Tipo Receptor” section absent (body = DestinodelaVenta); ch.3 numbering unstable; 2.2.2 prórrogas numeral drift — key on content/codes, never section or row numbers." Guards FR-073 and every matrix seed in §4. | no | GT synthesis wave S-GT1 | open (standing guard) |
| OQ-003 | GOQ-46 (owned): "Frase tipo 9 escenario 1 cites “Decreto XX-2022” [sic] placeholder — which decreto governs gas-propano subsidio texts (45-2022? 05-2023?)." Blocks the final legend text of FR-108; verbatim placeholder shipped meanwhile. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT) | open |
| OQ-004 | GOQ-47 (owned): "CF Q2,500 DTE list: 11 types (incl. FACP, rules 2.2.4.11/2.2.5.6) vs 10 (2.19.1.2/2.19.2.4) — which authoritative for FACP-CF? Conservative: 11 (R16)." | no | GT synthesis wave S-GT1 → W6 partner ask (SAT) | open |
| OQ-005 | GOQ-48 (owned): "“Régimen antiguo” paper Código-Tipo list (1,2,7,8,9,30,32,37,38,53,57,60,62,63,66,67,68,69,72) needs the SAT resolution-type catalog to interpret." Affects FR-133/137 paper-origin detection. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT) | open |
| OQ-006 | GOQ-49 (owned): "NIT check-digit coefficient table not printed (algorithm described, coefficients omitted) — obtain before implementing mod-11." Blocks only the check-digit component of FR-086; structural checks + certificador delegation ship meanwhile — NEVER implement coefficient guesses. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT/RTU reglamento) | open |
| OQ-007 | GOQ-50 (owned): "Rate rows (IDP Q4.70…, IBN, CEM, TAP, regime %) are decree-bound dated values (“Sujeta a la vigencia de leyes y reglamentos”) — D-GT10 watchlist, never constants." Governs FR-130 and §4 Table 1; taxation waves cross-check the statutory layer. | no | GT synthesis wave S-GT1 (watchlist) | open (standing watch) |
| OQ-008 | GOQ-24 (owned): "“ICT” (RetencionesFacturaEspecifica, FEPE) expansion + legal basis — verify vs D-31-2024 art. 4 (GOQ-13 kin)." Blocks only the user-facing label of FR-127; the 1.5% arithmetic is fully printed. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT; D-31-2024 acquisition) | open |
