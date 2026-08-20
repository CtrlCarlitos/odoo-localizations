# HN — Fiscal reporting — DJIMR/DMR per-código retention declarations

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' retention
declaration system — cluster F2 of the master index: the *Declaración Jurada
Informativa Mensual de Retenciones* (DJIMR, monthly informative affidavit of
retentions, SAR-238-2024), which superseded the *Declaración Mensual de
Retenciones* (DMR) of D.L. 66-2015/DEI-SG-155-2011 — same obligation, dated
regime rows per R-H31. It owns: (a) the monthly **per-código** informativa
obligation (one DJIMR per retention tax code per month; 25-code catalog seeded
into the `djimr_retention_codes.csv` sidecar, EV13:EVID-077) with its
10-días-calendario cadence and the two-step *informativa → SER determinativa*
filing pair; (b) the DJIMR-specific **rectificativa de-oficio propagation**
(informativa rectifications auto-rectify the determinativa; aceptada only when
tax increases, else rechazo) and the filed-period freeze it implies; (c) the
per-código **casilla/line contracts** — 111 asalariados (casillas
2/43/44/45/46 mapping of the plantilla export), 112 honorarios (dual CAI
pairs + State-transaction fields), 113 dividendos (shareholder census
1111-1121 + country annex), 115 intereses (instrument fields, RTN-o-DNI),
116 ISV sector público (15/18 base split), 135 compras 1% (L15M-gate card),
136 cedular alquiler, 138 GC no-residente (non-resident ID triplet, eventual
cadence, dual deadline), 217 ISV Art. 8 (GRACO/5-activity gate) — plus the
generic card for codes without a dedicated Ayuda (118/122-134/137/254);
(d) the channel matrix per código with the one-modality rule, vector-fiscal
alta / *Nueva Declaración Eventual* on-ramps, the Servicio Web plantilla
export pipeline and the print-faithful 2dp DMR-validation surface; (e)
third-party attribution (the *información de terceros* ledger) and the
retention-voucher CAI linkage.

It does **not** cover: retention **rates and computation engines** — consumed
by id from `../taxation/04_isr-withholding.md` (HN-TAX-FR-121..153: plantilla,
12.5% services, 1% compras; FR-135 composite sole-source gate; FR-150/151
entero anchor; **FR-153 = the per-código record data shape whose export
contract this file owns**), `../taxation/03_isr-rates-gains-minimum.md`
(HN-TAX-FR-095..104: GC/non-resident; FR-099 4% buyer retention),
`../taxation/05_d17-2010-family.md` (HN-TAX-FR-170..181: dividends, cédula
alquiler) and `../taxation/06_isv.md` (HN-TAX-FR-223 ISV rate matrix feeding
the 116/217 15/18 split) — never restated here; the generic OVI/SW **filing
lifecycle chassis** (login→alta→pendiente→borrador→juramento→acuse/QR,
Boletín, buzón, SW two-stage validation machinery) — file 01 of this wave
(cluster F1, HN-FREP-FR-001..040 pre-allocated, parallel write), consumed by
id; the **tarjetas** declarations 215/523 and the devolución 8% (outside the
catalog, R-H16) — file 04; the DMC form 527 (file 03) and the ISV
determinativa 201/RS 202 (file 05); the *comprobante de retención*
**emission mechanics** (type 05, CAI/rango machinery) —
`../e-invoicing/03_document-mechanics.md` HN-EINV-FR-139/140, consumed by id
(this file stores the voucher's identifiers as data); and sanctions
computation (CT frame — hook only).

## 2. Legal Basis

Authority order (binding, per master evidence index): SAR-236-2024 (OVI/SW
channel chassis — file 01's instrument), **SAR-238-2024 (DJIMR, current)** >
D.L. 66-2015 Art. 2 + DEI-SG-155-2011 (DMR era, repealed) > per-código
Ayudas (`31_-40_` here) > `71_` Generalidades DMR (compilation — cite **per
row only, never §4**, R-H27). All Ayudas are undated prints citing
SAR-236/238-2024 in-text ⇒ post-May-2024 vintage, read 2026-08-19: rates,
channels and deadlines are DATED DATA, never asserted current beyond the
print. D-H2 dated rows and the D-H2.5 filed-period freeze bind throughout.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo SAR-238-2024, PRIMERO/SEGUNDO/TERCERO | PRIMERO: automated system so retention agents inform the AT of the detail of retentions effected on third parties "mediante la 'Declaración Jurada Informativa Mensual de Retenciones (DJIMR)', que proporcionará la determinación de la obligación de presentar y pagar el tributo en la Declaración Jurada Determinativa de los impuestos retenidos"; SEGUNDO: deadline "dentro del plazo de los primeros diez (10) días calendarios del mes siguiente al que se efectuó la retención"; TERCERO: one DJIMR "por cada código de impuesto de retención", which in turn feeds the agent's own determinativa "y la de terceros" | System + monthly deadline + per-código informativa feeding the determinativa and third-party records | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-PRIMERO..TERCERO pp.3-4 (EV13:EVID-076) |
| LB-002 | SAR-238-2024, CUARTO | "Las retenciones que se informen en cada una de las DJIMR, serán conforme a los siguientes Códigos de Impuestos: 1) DJIMR-111 Retención en la Fuente Asalariados; 2) DJIMR-112 Retención por Servicios, Honorarios, y otros (Art. 50); 3) DJIMR-113 Retención por Dividendos o Utilidades Distribuidas (Art. 25); 4) DJIMR-115 … Intereses y Rendimientos Financieros (Art. 9); 5) DJIMR-116 … (Sólo Sector Público); 6) DJIMR-118 … Contribuyentes en Mora; 7)…19) DJIMR-122…134 (Art. 5 ISR family); 20) DJIMR-135 Retención Anticipo ISR o ATN (1%); 21) DJIMR-136 … Cedular sobre Alquiler Habitacional (10%); 22) DJIMR-137 … Ganancias de Capital (10%); 23) DJIMR-138 Ganancias de Capital a No Residentes; 24) DJIMR-217 Retenciones Artículo 8 (ISV); y, 25) DJIMR-254 Retención Venta Boletos de Lotería Electrónica, Rifas y Sorteos" | The authoritative 25-code retention catalog — join key between retention moves, monthly informativas and SAR third-party records (no 215/523: tarjetas file outside, R-H16) | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-CUARTO pp.3-4 (EV13:EVID-077) |
| LB-003 | SAR-238-2024, QUINTO/SEXTO | QUINTO: DJIMR "podrán presentarse a través de Servicio Web u Oficina Virtual; no obstante, los obligados tributarios deberán implementar una sola modalidad"; SEXTO: rectifications per CT periodicity, "deberán ser rectificadas haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original" | One-modality channel rule + same-modality rectification | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-QUINTO/SEXTO pp.4-5 (EV13:EVID-078) |
| LB-004 | SAR-238-2024, SÉPTIMO | "Las Declaraciones Rectificativas de las DJIMR originales, tendrán una vinculación directa con su Declaración Jurada Determinativa … darán como resultado declaraciones rectificativas de las Declaraciones Juradas Determinativas de oficio por parte del Servicio de Administración de Rentas, quedando en estado aceptada cuando el valor del impuesto a pagar sea mayor al consignado en la declaración anterior, caso contrario, quedará la declaración rectificada en estado rechazo" | Informativa rectifications propagate into the determinativa automatically (SAR de oficio); accepted only if tax payable increases, otherwise rejected | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-SÉPTIMO p.5 (EV13:EVID-079) |
| LB-005 | SAR-238-2024, NOVENO/DÉCIMO PRIMERO + considerandos | D.L. 66-2015 Art. 2: DMR "a más tardar dentro de los diez (10) días calendarios del mes siguiente en que se efectuó la retención"; history DEI-SG-155-2011 (DET-MR module → "Declaración Jurada Informativa DEI-540") → SAR-007-2017; NOVENO: omisas DMR "se deben presentar a través de la Oficina Virtual mediante la DJIMR"; DÉCIMO PRIMERO: "Dejar sin valor y efecto las disposiciones contenidas en el Acuerdo No. DEI-SG-155-2011" | DMR→DJIMR instrument chain; omisas-DMR migration path; DEI-SG-155-2011 repealed (R-H31) | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | considerandos pp.2-3; 238-NOVENO/DÉCIMO PRIMERO pp.3, 5 (EV13:EVID-080) |
| LB-006 | Ayuda 136 (31_), §2.2/§2.2.2/§2.3 — shared chassis (identical in 32_-40_) | "Una vez presentada la Declaración Informativa, debe realizar la Declaración Determinativa (SER) del código de impuesto y del mismo período de la Declaración Informativa"; Section A autocompletes "Base de Cálculo / Tarifa / Impuesto a pagar"; Section B: "'Pagos realizados para el período', será autocompletado por el sistema… 'Excedente del período anterior'… 'Importe a compensar' y 'Cesiones de crédito', se utilizará solo cuando se tengan créditos autorizados por el Servicio de Administración de Rentas (SAR). … Los campos de esta sección no serán editables"; "Rectificada la Declaración Original Informativa [debido al autocompletado,] la Declaración Original Determinativa también será rectificada"; rechazo: "Esta declaración queda rechazada. Debe ponerse en contacto con la Administración Tributaria"; states "Original OT, Aprobada OT" → "Rectificada OT, Aprobada OT"; extemporaneous filings auto-generate a multa payable via the Pagar/Boletín pair | The two-step informativa→SER contract, Section A autocompletion, read-only SAR credits, rectification mirror, rechazo terminal state, late-filing multa | `hn/sources/31_Ayuda_cedular_alquiler.pdf` | 31-§2.2 pp.9-18; §2.3 pp.19-23 (EV31:EVID-111) |
| LB-007 | Ayuda 136 (31_), §I + §2.2/§2.4 | Rate anchor: "impuesto cedular de Renta del diez por ciento (10%) sobre el precio del arriendo o alquiler de viviendas… (Artículo 9 Reglamento… Acuerdo No. 1121-2010)"; plazo: retentions "deberán liquidarse en una declaración jurada y enterarse al Fisco en forma mensual, a más tardar dentro de los diez (10) días calendario del mes siguiente… (Según el Artículo 35 de Ley de Eficiencia… Decreto No.113-2011)"; forms: "136 / Determinativa / Única modalidad… la Oficina Virtual (OVI)" + "DJIMR136 / Informativa / Única modalidad… OVI"; informativa card: RTN, "CAI… longitud máxima de 37 caracteres", "Numero de Documento Establecimiento / Punto de emisión / tipo documento / correlativo", "Fecha de emisión", "Importe base mensual retención" | 136 surfaces: 10% rate print, OVI-only both steps, provider-factura card (no retention-voucher fields) | `hn/sources/31_Ayuda_cedular_alquiler.pdf` | 31-§I pp.4-6; §2.2 pp.9-10; §2.4 pp.23-25 (EV31:EVID-112) |
| LB-008 | Ayuda 111 (32_), §2.2 casillas + §I.4/§I.7 | "2-RTN, debe ingresar el Registro Tributario Nacional (RTN) del asalariado al cuál efectuaron la retención. 44-Importe base mensual retención, incorporar el monto total por el cual se generó la retención. Casilla 46-Retenido, consigna el importe total retenido al asalariado"; opcionales: "43-Ingresos brutos proyectados anuales…; 45-Deducciones mensuales… según al Artículo 13 de la Ley del Impuesto Sobre la Renta"; forms: "DJIMR 111 / Informativa / Podría presentar en OVI y Servicio Web (SW)" + "111 / Determinativa / Única modalidad… OVI", footnote quoting 236-2024 DÉCIMO OCTAVO single-modality; plazo Art. 35 D.113-2011 10 días | The 111 line contract (casillas 2/43/44/45/46) — NO computation restated (plantilla = the computation contract, taxation/04) | `hn/sources/32_Ayuda_retencion_asalariados_111.pdf` | 32-§2.2 p.11; §I.4-§I.7 pp.5-6 (EV31:EVID-113) |
| LB-009 | Ayuda 111 (32_), §2.1C-§2.2.1 — SW plantilla pipeline (kin 34/35/36/37/42_) | Plantilla download per impuesto/periodo; "el formato de celda debe ser texto en cada fila llenada"; "la versión de las plantillas puede cambiar, según lo considere la Administración Tributaria… debe asegurarse de que sea la última versión"; upload → "número de la orden de trabajo… puede ser recibida con o sin errores… 'Generar Informe'… descargar en formato PDF… hasta que la orden de trabajo sea recibida sin errores"; "deberá validar en oficina virtual si la declaración ha sido presentada, caso contrario verificar en el buzón electrónico el informe de errores"; "recuerde que siempre se realizan dos validaciones" | SW bulk channel: versioned text-cell plantillas, two-stage validation (portal OT + OVI/buzón), error-report loop | `hn/sources/32_Ayuda_retencion_asalariados_111.pdf` | 32-§2.1C..2.2.1 pp.9-16 (EV31:EVID-114) |
| LB-010 | Ayuda 112 (33_), §I.4-5 + §2.2 | Art. 50 restated: PJs "deberán retener y enterar al Fisco el doce punto cinco por ciento (12.5%) del monto de los pagos o créditos que efectúen por concepto de honorarios profesionales, dietas, comisiones, gratificaciones, bonificaciones y remuneraciones por servicios técnicos"; card: RTN, "CAI… del que brindo el servicio"; "Número de Documento Fiscal (Establecimiento / Punto de emisión / tipo documento / correlativo)"; "Fecha de emisión"; "Fecha del documento de retención: fecha en la cual el agente retenedor emitió el comprobante de retención"; second "CAI… para el agente de retención"; "Importe base mensual de retención"; "Código de la institución del estado… según Secretaría de Finanzas"; "Código F01… solo aplica… con el estado"; forms: "DMR-112 / Informativa / Única modalidad… la Oficina Virtual" + "SER-112 / Determinativa / Única modalidad… Oficina Virtual"; vector-fiscal alta recommendation | 112 line contract: dual CAI/document/date pairs (provider factura + retention voucher) + State-transaction fields; OVI-only | `hn/sources/33_Ayuda_ret_serv_honorarios_112.pdf` | 33-§I.4-5 pp.5-6; §2.2 pp.11-12 (EV31:EVID-115) |
| LB-011 | Ayuda 113 (34_), §I.3 + §2.2 + §2.1B + Anexo 1 | Art. 25 restated (10% dividend gravamen, sociedad mercantil as agent, excluded from the Art. 22 progressive scale, capitalización exenta, >100-day related receivables = deemed dividends); casillas: "1111-Tipo… (Accionista/Socio); 1112-Cantidad acciones…; 1113-Valor nominal acciones…; 1114-Parte social, indicar el porcentaje del capital social…; 1115-Porcentaje participación… (el porcentaje debe ir números enteros, sin el signo de %); 1116-Distribución… (SÍ/NO); 1117-Monto distribuido…; 1118-Monto por pagar…; 1119-Socio nacional… (SÍ/NO); 1120-País origen… Tomar como referencia el Anexo 1; 1121-Cambio socio… (SÍ/NO)"; forms: "DMR-113 / Informativa / Podría presentar en OVI y Servicio Web (SW)" + "SER-113 / Determinativa / Única modalidad… OVI"; Alta: "'Alta de Obligaciones'… '+Añadir Obligación'… 'Se ha agregado una obligación'" | 113 shareholder-census line contract + country annex (stale entries YU/TP/ZZ/AN) + Alta-de-Obligación flow | `hn/sources/34_Ayuda_ret_dividendos_113.pdf` | 34-§I.3 pp.4-5; §2.2 pp.15-16; §2.1B pp.9-11; Anexo 1 pp.48-54 (EV31:EVID-116) |
| LB-012 | Ayuda 115 (35_), §I.4/§I.8 + §2.2 | D. 110-93 Art. 9 restated: interest incomes from enumerated instruments "estarán gravadas con una tarifa del diez por ciento (10%) calculada sobre el total de dichas rentas"; Art. 10: retained by the paying/crediting PJ or institution "al momento de efectuarse cualesquiera de estas dos operaciones", entero within 10 días calendario of the following month; casillas: "2-RTN… o Documento Nacional de Identificación del retenido (proveedor). 36-Instrumento… títulos valores, operaciones bursátiles, depósitos (en cuentas de ahorros en Bancos), y préstamo. 37-Tipo de identificación del instrumento financiero… 38-Tipo de moneda… 44-Importe base mensual retención"; forms: "DMR-115 / Informativa / Podría presentar en OVI y Servicio Web (SW)" + "SER-115 / Determinativa / Única modalidad… OVI" | 115 line contract: instrument-typed financial-interest retention; payment-or-credit trigger; RTN-o-DNI flexibility | `hn/sources/35_Ayuda_ret_intereses_115.pdf` | 35-§I.4 p.5; §I.8 pp.6-7; §2.2 pp.11-12 (EV31:EVID-117) |
| LB-013 | Ayuda 116 (36_) §I.7/§2.1 + Generalidades (71_) §3 | 36_: "Considerar la Normativa aplicada: Artículo 100, Decreto Legislativo 182-2020"; casillas: "2-RTN… del retenido (proveedor). 7-CAI… 37 caracteres… 71-Nº documento (establecimiento / punto de emisión / tipo documento / correlativo)… 9-Fecha de emisión… 30-Fecha del documento de retención… 341-CAI retención… 342-Nº documento retención… 4646-Retenido: agregar el importe total retenido. Importe base 15%… Importe base 18%…"; forms: "DJIMR-116 / Informativa / Podría presentar en OVI y Servicio Web (SW)" + "116 / Determinativa / Única modalidad… OVI"; 71_ row: "Decreto 5-2001 / Acuerdo No. SAR-238-2024 / Decreto No. 62-2023 Art.137 / 116 / … / NA" + bullet: "En todas las compras de bienes y servicios del Estado, el valor del pago del Impuesto Sobre Ventas será retenido en cada Orden de Pago o documento equivalente. Dicho valor deberá ser enterado en la Tesorería General de la República. Se exceptúan… las compras exoneradas del pago de dicho impuesto por ley o cuando el valor de la compra de igual al precio de la importación y ya se hubiere cancelado el impuesto correspondiente" | 116 line contract: State buyers retain the ISV itself per Orden de Pago, 15/18 base split, TGR entero, exemption guards; base-legal conflict open (36_ OQ-1) | `hn/sources/36_Ayuda_ret_ISV_sector_publico_116.pdf` + `hn/sources/71_Generalidades_DMR.pdf` | 36-§I.7 p.6; §2.1 pp.11-12; 71-§3 p.3 (EV31:EVID-118) |
| LB-014 | Ayuda 135 (37_), §I.1 + §2.2 + §2.2.3 | Sujetos: "Personas Jurídicas o Comeriante [sic] Individuales, con ventas mayores a quince millones de Lempiras anuales (L.15,000,000.00), se designaron como Agentes de Retención del uno por ciento (1%)… de sus proveedores de bienes y servicios que no estén sujetos al sistema de pagos a cuenta… (Acuerdo DEI-217-2010)"; casillas: "2-RNT [sic]… 7-CAI… 71-N° documento… 9-Fecha de emisión… 30-Fecha del documento de retención… 341-CAI Retención… 342-Número de Documento de retención (Establecimiento - Punto de emisión - tipo documento - correlativo)… 32-Código de la institución del estado… 44-Importe base mensual retención: acreditar el importe base mensual sujeto a retención"; determinativa: "Base de cálculo: que será la consignada en la declaración informativa. Tarifa: corresponde al porcentaje de retención realizado"; forms: "135 / Informativa / Modalidad… Oficina Virtual (OVI) y Servicio Web (SW)" + "135 / Determinativa / Única modalidad… OVI" | 135 line contract: L15M retainer gate, full retention-voucher pair, Tarifa = the percentage performed | `hn/sources/37_Ayuda_ret_anticipo_135.pdf` | 37-§I.1 p.4; §2.2 pp.12-13; §2.2.3 p.24 (EV31:EVID-119) |
| LB-015 | Ayuda 138 (38_), §I.4-5 + §I.8 + §2.1/§2.1.2 | D. 273-2013 Art. 13 → Ley de Eficiencia Art. 14: "Cuando las enajenaciones de bienes inmuebles o derechos y valores sean realizadas por un no residente, el adquiriente debe retener el cuatro por ciento (4%) del valor de la transmisión de dominio a cuenta de este impuesto. Dicho valor debe ser enterado dentro de los diez (10) días calendario siguiente a la transacción"; plazo dual-anchor: monthly rule "(Según el Artículo 35 de Ley De Eficiencia… y Acuerdo No. SAR-238-2024)"; card: "RTN: Campo no obligatorio… Pasaporte o Identificación CA: Consignar el documento oficial de viaje según el país de residencia fiscal… Número identificador tributario o mercantil… País de residencia… deberá completar al menos las casillas denominadas 'Pasaporte o identificación CA' o 'Número Identificador tributario o mercantil'"; "La presentación de estas Declaraciones tiene como característica el no ser recurrentes… 'Nueva Declaración Eventual'"; forms both OVI ("DMR-138 / SER-138") | 138 line contract: 4% buyer retention, non-resident ID triplet with at-least-one rule, eventual cadence, dual deadline | `hn/sources/38_Ayuda_ret_gc_no_residente_138.pdf` | 38-§I.4-5 p.5; §I.8 p.6; §2.1 p.7; §2.1.2 pp.12-13 (EV31:EVID-120) |
| LB-016 | Ayuda 135 duplicate (39_), §I.4/§2.2/§2.4 | Same código 135, Art. 19 D.17-2010; sujetos verbatim-identical to 37_ incl. "(Acuerdo DEI-217-2010)"; forms: "135 / Informativa / Única modalidad para la presentación a través de la Oficina Virtual (OVI); 135 / Determinativa / Única modalidad… OVI" — conflicts with 37_'s OVI+SW; 10 unnumbered card fields; base-field gloss corrupted ("acreditar el importe total retenido") | The duplicate 135 print (OVI-only variant) — R-H21: 37_ canonical, channel conflict open (39_ OQ-1) | `hn/sources/39_Ayuda_ret_1pct_D17-2010.pdf` | 39-§I.4 p.5; §2.2 p.10; §2.4 p.28 (EV31:EVID-121) |
| LB-017 | Ayuda 217 (40_), §I.4-5 + §2.2 + §2.2.2 | "El Artículo Primero, Acuerdo DEI-215-2010, Designa a la totalidad de los sujetos pasivos que tengan la categoría de Grandes Contribuyentes, como Agentes de Retención del Impuesto Sobre Ventas causado en la prestación de servicios que le brinden las personas naturales y jurídicas dedicadas a las siguientes actividades: a) Transporte de carga por cualquier vía. b) Servicios de limpieza, aseo y fumigación. c) Servicios de Impresión o serigrafía. d) Servicios de Investigación y seguridad. e) Alquiler de locales comerciales, maquinaria o equipo"; card: RNT [sic], nombre auto, CAI, N° documento, fecha emisión, "Fecha del documento de retención", "CAI Retención", "Número de Documento de retención", "Importe base 15%… Importe base 18 %…", "Código de la Institución del Estado… Código F01…"; determinativa autocompletes "Retenido al 15% / Retenido al 18% / Impuesto a pagar"; forms: "217 / Informativa/Determinativa / Única modalidad… OVI" | 217 line contract: GRACO designation + 5-activity whitelist, 15/18 base buckets, voucher pair; rate semantics unpinned (40_ OQ-1) | `hn/sources/40_Ayuda_ret_ISV_art8_217.pdf` | 40-§I.4-5 p.5; §2.2 pp.9-10; §2.2.2 p.16 (EV31:EVID-122) |
| LB-018 | Generalidades DMR (71_), §3 tables + bullets (per-row only, R-H27) | ISR table rows: 111 "Art. 22 y 28, Ley ISR / NA"; 112 "Artículo 50, Ley ISR / 12.5%"; 113 "Artículo 25, Ley ISR / 10%"; 115 "Artículo 9, Decreto No. 110-93 / 10%"; 116 "Decreto 5-2001 / Acuerdo No. SAR-238-2024 / Decreto No. 62-2023 Art.137 / NA"; 118 "Artículo 299, Ley Presupuesto General de la República (se modifica cada año según dicha Ley) / Contribuyentes en Mora/Instituciones del Estado / N/A"; 135 "Art. 19, Decreto 17-2010 / Acuerdo DEI-SG-217-2010 / 1%"; 136 "Art. 5, Decreto 17-2010 / Artículo 13, Acuerdo 1121-2010 / 10%"; 137 "Acuerdo DEI-SG-27-2011 / Retención Impuesto Sobre Ganancias de Capital (10%) / 10%"; 138 "Artículo 7, Decreto 17-2010 y sus reformas / 4%"; 112 exception: "Se exceptúan… los pagos efectuados bajo contratos de trabajo celebrados dentro del período fiscal y cuyos honorarios como única fuente de ingresos no excedan la base exenta según la Tabla Progresiva de artículo 22 de la Ley de ISR"; 135 gloss: "deberán retener a sus proveedores que no estén sujetos al sistema de pago a cuenta el uno por ciento (1%) en concepto de anticipo del Impuesto Sobre La Renta o el Activo Total Neto, el que sea mayor" | The consolidated per-código rate/base-legal sheet: 112 sole-source exception (tabla-relative), 135 greater-of character, 115 exclusions, family anchors not printed in the Ayudas | `hn/sources/71_Generalidades_DMR.pdf` | 71-§3 pp.3-8 (EV31:EVID-125) |
| LB-019 | Ayudas 31/33/34/35/37/38/39/40 (mixed), alta + eventual sections | "Deberá acceder al botón 'Alta de Obligaciones'… seleccionar el impuesto y el periodo que dará alta a la obligación… '+Añadir Obligación'… 'Se ha agregado una obligación'"; "Esta opción se realizará en los casos que la obligación sea eventual; aplica para la presentación de ambas declaraciones Informativa/Determinativa… 'Nueva Declaración Eventual'… mostrará una pantalla con las diferentes declaraciones y sus códigos respectivos"; SW caveat: eventual "esta solo permitirá su ingreso mediante tarjeta" | Vector-fiscal alta + one-off eventual on-ramps (eventual = card-entry only) | `hn/sources/34_Ayuda_ret_dividendos_113.pdf` (+ 31/33/35/37/38/39/40 same sections) | 34-§2.1B pp.9-11; 31-§2.4 pp.23-25; 38-§2.1 p.7 (EV31:EVID-126) |
| LB-020 | All Ayudas §I.4/§I.5 form tables — channel matrix + 236-2024 quotes | Matrix (informativa/determinativa): 136 OVI-only/OVI; 111 OVI+SW/OVI; 112 OVI-only/OVI; 113 OVI+SW/OVI; 115 OVI+SW/OVI; 116 OVI+SW/OVI; 135 OVI+SW/OVI (37_) but OVI-only/OVI (39_); 138 OVI/OVI; 217 OVI/OVI; 523 SW-only (no determinativa); 215 OVI-only (no informativa). DÉCIMO OCTAVO: "podrán ser presentadas por Servicio Web u Oficina Virtual; no obstante, se deberá implementar el uso continuo de una sola modalidad"; DÉCIMO NOVENO: rectify "haciendo uso de la misma modalidad mediante la cual fue presentada la declaración original… Exceptuando las Declaraciones Juradas que fueron presentadas previo a la entrada en vigor del presente acuerdo" | Per-código channel reference data; determinativa always OVI; single modality; pre-236-2024 rectification exception | `hn/sources/31_Ayuda_cedular_alquiler.pdf` … `hn/sources/40_Ayuda_ret_ISV_art8_217.pdf` (per-doc form tables) | 31 p.5; 32 p.5; 33 p.5; 34 p.6; 35 p.5; 36 p.5; 37 p.5; 38 p.5; 39 p.5; 40 p.5 (EV31:EVID-127) |
| LB-021 | Generalidades DMR (71_), intro + §6-7 | DMR "es un formulario informativo aprobado mediante Acuerdo DEI-SG-155-2011 publicado el 27 de julio del 2011… en el cual se deben informar las retenciones efectuadas a terceros… preparada para obtener la información a detalle de terceros y se desprende de la obligación de presentar y pagar el tributo retenido"; "La no presentación de la Declaración Mensual de Retenciones (DMR) en la forma y plazo establecido, dará lugar a la sanción según el Artículo 160 del Código Tributario" | DMR/DJIMR identity + third-party-information purpose + CT Art. 160 sanction hook on non-filing | `hn/sources/71_Generalidades_DMR.pdf` | 71-intro p.2; §6-7 p.9 (EV31:EVID-129) |

## 3. Functional Requirements

### 3.1 The DJIMR system: obligation, cadence, two-step, propagation

- **HN-FREP-FR-041:** The system shall generate, per calendar month, one
  DJIMR informativa **per retention código with movements** (never an
  empty-code filing), each aggregating that month's retention records of the
  código, and shall generate a DJIMR only for códigos present in the 25-code
  catalog (FR-049); for código 111 the monthly row set shall cover all 12
  months of the fiscal year including zero-retention months (plantilla
  declare-12-months note, consumed from HN-TAX-FR-133).
  (LB-001; LB-002; EV13:EVID-076/077)
- **HN-FREP-FR-042:** The system shall anchor every DJIMR informativa and
  its SER determinativa to the deadline of the first 10 días CALENDARIO of
  the month following the month in which the retention was practiced —
  consumed as the dated entero anchor of HN-TAX-FR-150 with the
  per-instrument hábil/calendario semantics of HN-TAX-FR-151 (all DJIMR
  códigos = calendario; the only deviation in this family is 138's
  transaction-based leg, FR-063); the fiscal-calendar engine itself is file
  01's, consumed by id. (LB-001; LB-014; EV13:EVID-076; EV31:EVID-119)
- **HN-FREP-FR-043:** The system shall enforce the two-step filing order per
  código+period: the SER determinativa (same código, same period) is
  generatable only after the informativa is presented, with Section A
  autocompleted from the informativa per the per-código variant map —
  Base/Tarifa/Impuesto a pagar (generic codes), Base de cálculo + Impuesto
  only with NO Tarifa (111 and 116), Tarifa = the percentage of retention
  performed (135), Retenido al 15% / Retenido al 18% / Impuesto a pagar
  (217) — and shall never allow manual override of autocompleted Section A
  values. (LB-006; LB-014; LB-017; EV31:EVID-111/119/122)
- **HN-FREP-FR-044:** The system shall render determinativa Section B
  (Créditos) read-only: "Pagos realizados para el período" autocompleted by
  the system, "Excedente del período anterior" carried forward, and "Importe
  a compensar" / "Cesiones de crédito" usable only with SAR-authorized
  credits (an authorization reference required to unlock those two fields).
  (LB-006; EV31:EVID-111)
- **HN-FREP-FR-045:** The system shall maintain the third-party attribution
  ledger: every DJIMR line shall carry the retained party's identity (RTN or
  the per-código ID flexibility of FR-059/063), base and retained amount,
  exposed as a retenido-side query surface (per-third-party, per-period
  retained totals) feeding the retained parties' credit/consulta surfaces —
  the *información de terceros* purpose of the DJIMR system.
  (LB-001; LB-021; EV13:EVID-076; EV31:EVID-129)
- **HN-FREP-FR-046:** The system shall encode the retention-declaration
  regime as DATED rows per R-H31: regime `dmr` for periods before the
  SAR-238-2024 vigencia (La Gaceta 36,538, 20-may-2024) and regime `djimr`
  from 2024-05-20 onward, with DEI-SG-155-2011 (DET-MR/DEI-540) recorded as
  repealed and SAR-007-2017 as the interim format keeper; omisas DMR periods
  shall be fileable through the DJIMR via OVI (migration path), and
  historical DMR-period imports shall resolve to the `dmr` regime row
  (D-H2/D-H3); the "NNN DMR" labels surviving in the live OVI UI
  (tarjeta/eventual texts and form-table mixes) are cosmetic and shall map
  to the same obligation object. (LB-005; EV13:EVID-080; R-H31;
  EV31:EVID-111)
- **HN-FREP-FR-047:** The system shall implement the DJIMR-specific
  rectification propagation: a rectificativa of an original informativa has
  direct linkage to its determinativa — the modifications result in
  rectificativas of the Declaraciones Juradas Determinativas **de oficio by
  SAR**, with the rectified determinativa state = aceptada when the tax
  payable exceeds the previously declared value, else estado rechazo; the
  client-side mirror (rectifying the informativa auto-rectifies the
  determinativa) shall be recorded on the declaration chain.
  (LB-004; LB-006; EV13:EVID-079; EV31:EVID-111)
- **HN-FREP-FR-048:** The system shall reconcile filed determinativa
  snapshots against SAR's de-oficio rectifications (FR-047): after a DJIMR
  rectification the original determinativa snapshot is superseded — the
  system shall import/accept the SAR-rectified determination rather than
  assume the original stands, shall surface the aceptada/rechazo outcome,
  and shall never locally overwrite a filed-period value (D-H2.5 kin; the
  freeze itself = FR-071). (LB-004; LB-006; EV13:EVID-079; EV31:EVID-111)

### 3.2 Catalog, channels and on-ramps

- **HN-FREP-FR-049:** The system shall seed the retention-code catalog from
  the `djimr_retention_codes.csv` sidecar (25 rows, transcribed exactly from
  238-CUARTO with 71_ per-row rate/base-legal metadata and the Ayudas'
  channel data) and wire each código to the corresponding retention tax
  code/engine of the taxation wave; the catalog is the join key between
  retention moves, monthly informativas and third-party records, and rows
  shall never be removed — codes may only be added by a new SAR instrument
  (dated rows). (LB-002; LB-018; EV13:EVID-077; EV31:EVID-125)
- **HN-FREP-FR-050:** The system shall carry the per-código channel matrix
  as DATED operational reference data: informativa channels 111/113/115/116
  = OVI+SW; 112/136/138/217 = OVI-only; 135 = UNRESOLVED (37_ OVI+SW vs 39_
  OVI-only — conflict open, R-H21, OQ-018); the determinativa channel is OVI
  for every código (invariant); the one-modality rule (single channel per
  taxpayer for the informativa family) shall be enforced on repeated
  filings. (LB-003; LB-016; LB-020; EV13:EVID-078; EV31:EVID-121/127)
- **HN-FREP-FR-051:** The system shall route rectifications through the
  same modality as the original declaration, with a pre-vigencia exception
  flag: declarations presented before SAR-236-2024's entry into force are
  exempt from the same-modality requirement (236-2024 DÉCIMO NOVENO as
  quoted in the Ayudas). (LB-003; LB-020; EV13:EVID-078; EV31:EVID-127)
- **HN-FREP-FR-052:** The system shall condition the per-código monthly
  filing calendar on the company's vector-fiscal registration state
  (obligations not *dadas de alta* never appear as pending) and shall offer
  the *Nueva Declaración Eventual* one-off path (card-entry only, covering
  both informativa and determinativa) for unregistered códigos and sporadic
  retention events — the mandatory route for 138's transaction-triggered
  filings (FR-063) and one-off 113 distributions — plus an alta-state
  reconciliation surface. (LB-019; EV31:EVID-126)
- **HN-FREP-FR-053:** For códigos with the Servicio Web channel, the system
  shall export the informativa to the SAR plantilla per the casilla
  contracts of §3.3: text-formatted cells on every filled row, latest-
  version plantilla fetch (versions change at AT discretion), orden-de-
  trabajo acceptance loop with error-report (PDF) ingestion until "sin
  errores", and the second OVI-side/buzón validation check — consuming the
  generic SW two-stage machinery of file 01 by id, owning here only the
  per-código field mapping. (LB-009; EV31:EVID-114)

### 3.3 Per-código line contracts (casillas)

- **HN-FREP-FR-054:** The system shall export código 111 lines per employee
  per month with casillas 2 (asalariado RTN), 44 (importe base mensual
  retención) and 46 (retenido) mandatory and casillas 43 (ingresos brutos
  proyectados anuales) and 45 (deducciones mensuales per Art. 13) optional,
  consuming the per-employee record shape of HN-TAX-FR-153(a) (plantilla DMR
  sheet: RTN/ID, name, base ÷ months, tax ÷ months, concepto "salarios") —
  the 1:1 mapping plantilla↔casillas is carried as OQ-001 (`32_ OQ-1`);
  no computation is restated here (NA alícuota per 71_; engines =
  taxation/04 by id). (LB-008; LB-018; EV31:EVID-113/125)
- **HN-FREP-FR-055:** The system shall emit DJIMR-111 upload values
  print-faithful at 2 decimals for the DMR/SW validation surface (default
  per carried origin `07_ OQ-1`, via taxation/04 OQ-006): retention records
  store full precision but values are rounded 2dp at the export surface and
  the validation never re-derives band values.
  (LB-008; LB-009; EV31:EVID-113/114)
- **HN-FREP-FR-056:** The system shall export código 112 lines with the
  dual document pair — provider factura CAI + Número de Documento Fiscal
  (establecimiento/punto de emisión/tipo documento/correlativo) + fecha de
  emisión, AND the retention voucher's own CAI + fecha del documento de
  retención — plus importe base mensual de retención, and for State
  transactions the código de la institución del estado (SEFIN
  classification) and Código F01 fields; the 12.5% engine, concept tags
  and sole-source exception gate are consumed by id (HN-TAX-FR-137..141 +
  FR-135/138; current-year exception amount unpinned, OQ-004); the
  informativa is OVI-only per the print (anomaly flagged, OQ-005).
  (LB-010; EV31:EVID-115)
- **HN-FREP-FR-057:** The system shall export código 113 lines as a
  per-shareholder census on distribution events: casillas 1111 (tipo:
  Accionista/Socio), 1112 (cantidad de acciones), 1113 (valor nominal
  acciones), 1114 (parte social — porcentaje del capital social) and 1115
  (porcentaje participación — enteros, sin el signo de %) carried as
  DISTINCT as-printed fields (intended distinction undefined, OQ-006),
  1116 distribución SÍ/NO, 1117 monto distribuido, 1118 monto por pagar,
  1119 socio nacional SÍ/NO, 1120 país origen (FR-058), 1121 cambio socio
  SÍ/NO; the dividend retention engine is consumed by id from
  HN-TAX-FR-170..176, and an Alta de la Obligación may be required before
  the first filing (FR-052). (LB-011; LB-019; EV31:EVID-116/126)
- **HN-FREP-FR-058:** For casilla 1120 the system shall use the SAR Anexo
  1 country-code list AS PRINTED — it is the validation list — including
  the stale entries YU (Yugoslavia), TP (East Timor), ZZ (campo por
  actualizar) and AN (Netherlands Antilles), each flagged
  `stale_vs_iso_3166_1`; codes shall never be silently normalized to ISO
  3166-1 (DECIDE open, OQ-008). (LB-011; EV31:EVID-116)
- **HN-FREP-FR-059:** The system shall export código 115 lines with
  casilla 2 accepting RTN **or** DNI for the retenido (ID-type + number
  pair), and the instrument fields 36 (instrumento: títulos valores,
  operaciones bursátiles, depósitos, préstamo), 37 (tipo de identificación
  del instrumento financiero), 38 (tipo de moneda) and 44 (importe base
  mensual); the payment-or-credit trigger date shall be captured on the
  retention record (earliest-of); the exclusion set (banks → Art. 22
  regime, D. 99-93 FX deposits, D. 110-93 Art. 12 monto) is carried as
  config-gapped flags (FR-073). (LB-012; LB-018; EV31:EVID-117/125)
- **HN-FREP-FR-060:** The system shall export código 116 lines for
  public-sector purchases with the provider document pair (2 RTN, 7 CAI ≤37
  chars, 71 Nº documento 4-segment, 9 fecha de emisión), the
  retention-voucher pair (30 fecha del documento de retención, 341 CAI
  retención, 342 Nº documento retención), the ISV-rate-split bases Importe
  base 15% / Importe base 18% (rate matrix consumed by id from
  HN-TAX-FR-223) and casilla 4646 Retenido; the retention = the ISV itself
  (100%-of-tax, R-H33) withheld per Orden de Pago, with the guards:
  law-exonerated purchases and import-priced purchases where the ISV was
  already paid are excluded; entero routing carries the TGR-vs-banks
  conflict flag (FR-070, OQ-012). (LB-013; EV31:EVID-118; R-H33)
- **HN-FREP-FR-061:** The system shall export código 135 lines with the
  full voucher pair (7 CAI, 71 N° documento, 9 fecha emisión, 30 fecha
  documento retención, 341 CAI retención, 342 Nº documento retención), the
  32 código de la institución del estado and casilla 44 importe base
  mensual; the retention base DEFAULTS TO THE PURCHASE AMOUNT (71_'s
  gross-sales gloss reads as the retainer's L15M-gate test pasted as base —
  CONFLICT open, OQ-022, never silently resolved); the 1% engine, L15M
  gate, supplier exemptions (incl. the D. 28-2019 waste-collector
  carve-out — absent from the Ayuda, sourced from the taxation wave's
  exemption catalog HN-TAX-FR-145/146, OQ-014) and the greater-of
  ISR/ATN anticipo tagging are consumed by id from HN-TAX-FR-142..148.
  (LB-014; LB-018; EV31:EVID-119/125)
- **HN-FREP-FR-062:** The system shall export código 136 lines with the
  provider-factura card only — RTN, CAI (≤37 caracteres), Numero de
  Documento (establecimiento/punto de emisión/tipo documento/correlativo),
  fecha de emisión, importe base mensual retención — with NO
  retention-voucher fields (the retention cites the landlord's factura);
  both steps are OVI-only; the cédular engine, L15,000/month threshold and
  m² proration are consumed by id from HN-TAX-FR-177..181 (threshold not
  restated in the Ayuda — OQ-002; determinativa Tarifa value unpinned —
  OQ-003). (LB-007; EV31:EVID-112)
- **HN-FREP-FR-063:** The system shall export código 138 lines with the
  non-resident ID triplet — RTN (optional; Honduran resident abroad),
  pasaporte o identificación CA, número identificador tributario o
  mercantil — validated at-least-one-of (pasaporte/CA OR foreign tax ID),
  plus país de residencia and importe base mensual; the filing cadence is
  transaction-triggered (eventual) with the periodic path available when
  the obligation is alta'd; the system shall compute and track BOTH
  deadline models — transaction + 10 días calendario (Eficiencia Art. 14
  per D. 273-2013 Art. 13) and month-end + 10 días calendario
  (SAR-238-2024) — alerting at the earlier (conservative operational
  default) while the conflict stays open for SAR ruling (OQ-016); the 4%
  engine is consumed by id from HN-TAX-FR-099 (the 46_ 2% print is never
  encoded — R-H26). (LB-015; EV31:EVID-120; R-H26)
- **HN-FREP-FR-064:** The system shall export código 217 lines with the
  15%/18% base buckets (Importe base 15% / Importe base 18%, per the ISV
  rate matrix consumed by id from HN-TAX-FR-223), the retention-voucher
  pair and fecha del documento de retención, and the State-transaction
  fields (institución code + F01); the retention applies only when the
  company is a gran contribuyente (GRACO designation, Acuerdo DEI-215-2010)
  AND the provider is dedicated to one of the five enumerated activities
  (transporte de carga por cualquier vía; limpieza/aseo/fumigación;
  impresión o serigrafía; investigación y seguridad; alquiler de locales
  comerciales, maquinaria o equipo); rate semantics (%-of-tax vs
  %-of-base) stay unpinned (OQ-020) — the determinativa surfaces Retenido
  al 15%/18% as autocompleted data, never as a locally restated rate.
  (LB-017; EV31:EVID-122)

### 3.4 Voucher linkage, catalog breadth and data quality

- **HN-FREP-FR-065:** The system shall link every retention record whose
  per-código card requires it to its *comprobante de retención* (retention
  voucher) — storing the voucher's own CAI, document number (4-segment) and
  emission date (112/116/135/217 cards) — and shall block the DJIMR line
  when the voucher reference is missing; the voucher's EMISSION mechanics
  (type 05, CAI/rango machinery, OTCD and patronos variants) are consumed
  by id from HN-EINV-FR-139/140 and never re-derived here.
  (LB-010; LB-013; LB-014; LB-017; EV31:EVID-115/118/119/122)
- **HN-FREP-FR-066:** The system shall validate provider-document
  references on every card that cites a supplier factura (112/115/116/135/
  136/217): CAI ≤ 37 characters, document number as the 4-segment
  establecimiento/punto de emisión/tipo documento/correlativo, and fecha de
  emisión present — the same fiscal-document line-key discipline the DMC
  consumes (file 03 by id).
  (LB-007; LB-010; LB-013; LB-014; EV31:EVID-112/115/118/119)
- **HN-FREP-FR-067:** For catalog codes without a dedicated Ayuda in the
  corpus (118 mora; 122-134 Art. 5 family; 137 premios; 254 electronic
  lottery), the system shall file the generic card contract of the shared
  chassis (retenido identity + base + retained, auto-name) with rate and
  base semantics as CONFIG-GATED catalog data: 122-134 rates resolve by id
  from the taxation Art. 5 engines (HN-TAX-FR-101/102 — which Tarifa the
  OVI expects for non-real-estate filings adjacent to 138 stays open,
  OQ-015); 118's anchor is PGR Art. 299 (moves annually — dated rows per
  budget law); 137 = DEI-SG-27-2011 premios GC 10%; 254 = 5% per the 71_
  gloss. (LB-002; LB-018; EV13:EVID-077; EV31:EVID-125)

### 3.5 Lifecycle surfaces: states, sanctions, freeze

- **HN-FREP-FR-068:** The system shall track the declaration state chain
  per código+period — Original OT → Aprobada OT → Rectificada OT (the OVI
  purple-font marker recorded as metadata) — with rechazo as a terminal
  state requiring contact with the Administración Tributaria before any
  further action on that declaration, and shall synchronize imported states
  (acuse/consulta) with local records. (LB-006; EV31:EVID-111)
- **HN-FREP-FR-069:** The system shall attach to every extemporaneous DJIMR
  filing the auto-generated multa (payable through the same Pagar/Boletín
  pair, consumed from file 01 by id) and shall record the CT Art. 160
  non-filing sanction hook for missed monthly per-código deadlines — the
  sanction computation itself is owned by the CT/taxation frame by id.
  (LB-006; LB-021; EV31:EVID-111/129)
- **HN-FREP-FR-070:** The system shall route determinativa payments through
  the default bank/Boletín channel (file 01 by id) with a per-código
  routing exception flag: código 116's entero is directed to the Tesorería
  General de la República per the 71_ gloss while the 36_ UI shows the
  standard bank Pagar/Boletín flow — CONFLICT recorded, never silently
  resolved (OQ-012); the tarjetas BCH-only routing (código 215) is file
  04's by id. (LB-013; LB-006; EV31:EVID-118/111)
- **HN-FREP-FR-071:** The system shall freeze retention moves for any
  código+month whose DJIMR informativa has been filed (D-H2.5 filed-period
  protection): posting, editing or canceling retention records in the filed
  período is blocked, and corrections route exclusively through the
  rectificativa flow — which triggers the FR-047 de-oficio propagation and
  the FR-048 snapshot reconciliation.
  (LB-004; LB-006; EV13:EVID-079; EV31:EVID-111)
- **HN-FREP-FR-072:** The system shall treat every catalog rate, channel
  and deadline value as DATED DATA pinned to its print (Ayudas undated,
  post-May-2024 vintage, read 2026-08-19; 71_ rows all cite SAR-238-2024):
  values carry their source anchor and are never asserted current beyond
  the print; where the taxation wave owns the engine, the CSV rate column
  is informational metadata and the engine id governs computation.
  (LB-018; LB-020; EV31:EVID-125/127)
- **HN-FREP-FR-073:** The system shall carry the 115 exclusion set —
  bank-paid interest under the Art. 22 regime, D. 99-93 foreign-currency
  deposits, and the D. 110-93 Art. 12 monto exclusion — as CONFIG-GAPPED
  engine flags sourced from 71_ (not from the Ayuda, which omits them): no
  excluded-interest reporting mechanism exists in the OVI casillas
  (config gap, OQ-009); the flags activate only when D. 110-93/D. 99-93 are
  acquired. (LB-012; LB-018; EV31:EVID-117/125)
- **HN-FREP-FR-074:** The system shall record código 116's base legal as an
  ANNUAL-MOVING, unresolved triple anchor: D.L. 182-2020 Art. 100 (36_)
  vs D. 5-2001 + D. 62-2023 Art. 137 (71_) — none of the three instruments
  in corpus, all recorded as divergent metadata (OQ-011); implementation
  requires pinning the current budget year's article, and the retention
  mechanics stand on R-H33 (100%-of-tax per Orden de Pago) regardless of
  which anchor governs. (LB-013; LB-018; EV31:EVID-118/125)
- **HN-FREP-FR-075:** The system shall enforce the catalog scope guard:
  tarjetas codes 215/523 (R-H16 — determinativa/informativa of the DEI-9382
  -J-2003/SAR-240-2024 procedure, file 04 by id) and the 524/501
  financial-transactions contribution codes that 71_'s sheet also lists
  NEVER generate DJIMR rows or enter this catalog (`71_ OQ-4` cross-cite);
  retention moves tagged with those codes route to their own declaration
  families. (LB-018; EV31:EVID-125; EV31:EVID-124; R-H16)

## 4. Data Model

Machine-readable sidecar next to this file: `djimr_retention_codes.csv` —
the 25-code retention catalog (one row per código, EV13:EVID-077 as printed,
enriched with 71_ per-row rate/base-legal metadata and the Ayudas' channel
matrix). It carries no FRs of its own. CSV discipline: comma-separated,
header row, LF endings; fields containing commas are double-quoted;
`regime_valid_from` = 2024-05-20 for every row (the SAR-238-2024 catalog
vintage — pre-2024 DMR months resolve to the `dmr` regime row of FR-046,
not to catalog rows); `rate_pct` EMPTY where no print pins a value (122-134
family — resolve from taxation/03 by id at implementation; never guess);
`informativa_channel` carries `ovi` / `ovi+sw` / `unresolved_37vs39` (135);
`filing_mode` = `periodic` except 138 = `eventual+periodic` (dual deadline
per FR-063); `notes` carries the per-row OQ markers and R-rulings
(R-H16/R-H21/R-H26/R-H33/R-H31). Layer semantics: Odoo-side
reference/export data only (wave default `odoo`; see §5).

**Declaration objects and catalog:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.djimr.declaration (new) | código_id, period, decl_type, regime, channel, state, acuse_code, acuse_qr, parent_id, supersedes_state | m2o/char/date/select | decl_type: informativa · determinativa (SER); regime: dmr (pre-2024-05) · djimr; state: borrador · presentada · original_ot · aprobada_ot · rectificada_ot · aceptada · rechazo; supersedes_state from SAR de-oficio import | FR-041, FR-043, FR-046..FR-048, FR-068 |
| l10n_hn.djimr.line (new) | declaration_id, retenido_partner_id, id_type/id_number, base, retained, casilla payload (JSON), provider_cai, provider_doc_number, provider_doc_date, voucher_cai, voucher_doc_number, voucher_date | m2o/monetary/json/char | casilla payload per §3.3 contracts (111: 2/43/44/45/46; 113: 1111-1121; 115: 36/37/38; 116: bases 15/18 + 4646; 135: full voucher pair; 138: ID triplet); third-party attribution fields | FR-045, FR-054..FR-066 |
| l10n_hn.retention.code (new) | codigo, name_es, name_en, family, rate_pct, base_semantics, filer, deadline_rule, informativa_channel, determinativa_channel, filing_mode, base_legal_es, evid_anchor, regime_valid_from | char/select | seeded from `djimr_retention_codes.csv`; rate informational where taxation owns the engine (FR-072); add-only (dated rows) | FR-049, FR-067, FR-072, FR-075 |
| l10n_hn.djimr.credit (on determinativa) | pagos_periodo (RO), excedente_anterior (RO), importe_compensar, cesiones_credito + sar_authorization_ref | monetary/char | Section B read-only block; compensar/cesiones locked without SAR authorization reference | FR-044 |
| l10n_hn.country.code.sar (new) | code, name, stale_vs_iso_3166_1 | char/boolean | Anexo 1 as printed (YU/TP/ZZ/AN flagged) | FR-058 |
| res.partner (extension) | hn_nonresident_passport_ca, hn_nonresident_tax_id, hn_fiscal_residence_country, hn_id_type (rtn · dni · passport_ca · foreign_tax_id) | char/select | non-resident ID triplet + 115 RTN-o-DNI pair | FR-059, FR-063 |
| l10n_hn.fiscal.vector (file 01 kin, consumed) | obligation código × alta state | boolean/date | gates the per-código pending calendar; eventual path for unregistered codes | FR-052 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = declaration generation, export,
validation-state and ledger logic living in the LGPL client. No SaaS rows:
no thin-client/SaaS split surface exists for these FRs (HND has no XML/DTE
transmission regime; the SW channel is a file upload the client prepares).
Generic OVI/SW chassis machinery (acuse/Boletín/buzón/SW two-stage engine,
fiscal-calendar rows) = file 01 by id; models stable across Odoo
17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-041 | odoo | l10n_hn.djimr.declaration + retention records | monthly generator | Per-código-with-movements; 111 emits 12 monthly rows (HN-TAX-FR-133 note); D-H2: period-resolved |
| FR-042 | odoo | l10n_hn.fiscal.calendar (file 01 engine) | due-date rows | Consumes HN-TAX-FR-150/151; all DJIMR códigos = días calendario; 138 dual rows (FR-063) |
| FR-043, FR-044 | odoo | l10n_hn.djimr.declaration (determinativa) | Section A/B | Autocomplete variant map per código; Section B RO + SAR-authorization unlock |
| FR-045 | odoo | l10n_hn.djimr.line + retenido query surface | third-party ledger | información de terceros; feeds consulta/credit surfaces by id |
| FR-046 | odoo | l10n_hn.djimr.declaration.regime | dated rows | D-H2/D-H3: DMR pre-2024-05 / DJIMR post; omisas migration path; R-H31 |
| FR-047, FR-048 | odoo | declaration chain (parent/supersedes) | propagation | De-oficio aceptada/rechazo; SAR-rectified determination import; D-H2.5 reconciliation |
| FR-049 | odoo | l10n_hn.retention.code | CSV seeding | Add-only catalog; join key to retention tax codes |
| FR-050, FR-051 | odoo | l10n_hn.retention.code channel fields + filing config | channel matrix | 135 = unresolved flag (OQ-018); determinativa=OVI invariant; same-modality + pre-236 exception |
| FR-052 | odoo | l10n_hn.fiscal.vector gate + eventual wizard | alta/eventual | Card-entry-only eventual path; 138/113 primary consumers |
| FR-053 | odoo | export mapper (per código) + OT state machine | SW plantilla | Text-cell formatting; latest-version fetch; two-stage validation loop (file 01 machinery by id) |
| FR-054, FR-055 | odoo | l10n_hn.djimr.line (111 payload) | casillas 2/43/44/45/46 | Consumes HN-TAX-FR-153(a); print-faithful 2dp at export (`07_ OQ-1` default) |
| FR-056 | odoo | djimr.line (112 payload) + partner/move refs | dual CAI pair | voucher refs via FR-065; institución/F01 for State transactions |
| FR-057, FR-058 | odoo | djimr.line (113 payload) + l10n_hn.country.code.sar | census + annex | 1114/1115 distinct as printed (OQ-006); annex as printed, stale flags (OQ-008) |
| FR-059 | odoo | djimr.line (115 payload) + res.partner hn_id_type | instrument fields | RTN-o-DNI; earliest-of trigger capture; exclusions config-gapped (FR-073) |
| FR-060 | odoo | djimr.line (116 payload) | bases 15/18 + 4646 | ISV split consumed from HN-TAX-FR-223; TGR flag (FR-070); R-H33 |
| FR-061 | odoo | djimr.line (135 payload) | voucher pair | Base default = purchase amount (OQ-022 conflict marker); exemptions from HN-TAX-FR-145/146 |
| FR-062 | odoo | djimr.line (136 payload) | provider-factura card | OVI-only; engine from HN-TAX-FR-177..181 |
| FR-063 | odoo | djimr.line (138 payload) + partner triplet | eventual + dual deadline | Both deadline models tracked; alert at earlier (flagged default, OQ-016); R-H26 guard |
| FR-064 | odoo | djimr.line (217 payload) + activity whitelist | buckets 15/18 | GRACO gate + 5 activities; rate semantics marker (OQ-020) |
| FR-065, FR-066 | odoo | retention record ↔ voucher refs + provider doc key | linkage/block | Emission mechanics = HN-EINV-FR-139/140 by id; CAI ≤37ch + 4-segment key |
| FR-067 | odoo | l10n_hn.retention.code config gates | generic card | 118/122-134/137/254; PGR Art. 299 annual rows; rates by id or config gap |
| FR-068 | odoo | declaration state chain | states | rechazo terminal; OVI state sync |
| FR-069 | odoo | declaration + account.payment (multa) | late-filing | CT Art. 160 hook; computation = CT frame by id |
| FR-070 | odoo | payment routing flag | TGR exception | Conflict recorded (OQ-012); tarjetas BCH = file 04 |
| FR-071 | odoo | retention record período freeze | D-H2.5 block | Filed código+month immutable; corrections via rectificativa only |
| FR-072..FR-075 | odoo | l10n_hn.retention.code metadata + scope guard | dated data / guards | 116 annual anchor (OQ-011); 115 exclusions (OQ-009); 215/523/524/501 excluded (R-H16, `71_ OQ-4`) |

Version-regime notes (D12): FR-046 records the DMR→DJIMR regime boundary
(SAR-238-2024, G 36,538 20-may-2024 — immediate-on-publication vigencia);
FR-072 records the Ayuda print vintage (post-May-2024, read 2026-08-19);
FR-074 records 116's annual budget-law anchor cycle; FR-053 records the
plantilla version cycle (no fixed dates — always-latest rule).

## 6. Acceptance Criteria

- **AC-001:** Given January 2026 with retention movements in códigos 111,
  112 and 135 only, then exactly three DJIMR informativas are generated
  (111/112/135), none for any other código, and the 111 set contains one
  row per employee per month for all 12 months of the FY including
  zero-retention months (FR-041).
- **AC-002:** Given retentions practiced in January 2026, then the
  informativa + determinativa deadline resolves to 2026-02-10 (first 10
  días calendario of the following month); given a 138 transaction on
  15-ene-2026, then BOTH deadlines are tracked (transaction+10d = 25-ene;
  month-end+10d = 10-feb) with the alert firing at 25-ene and the conflict
  flag surfaced (FR-042, FR-063).
- **AC-003:** Given an informativa for código 112 period 2026-01 in state
  presentada, then the SER-112 determinativa for the same código+period is
  generatable with Section A autocompleted (Base/Tarifa 12.5%/Impuesto);
  given no informativa presented, then determinativa generation is blocked
  (FR-043).
- **AC-004:** Given a 135 determinativa, then Tarifa = the percentage
  actually retained (1%), Base = the informativa-consigned base; given a
  111 or 116 determinativa, then no Tarifa field is emitted; given a 217
  determinativa, then Retenido al 15% and Retenido al 18% surface as
  autocompleted values (FR-043).
- **AC-005:** Given a determinativa in Section B, then pagos/excedente are
  read-only system values and importe a compensar/cesiones remain locked
  until a SAR authorization reference is supplied (FR-044).
- **AC-006:** Given a DJIMR rectificativa whose tax payable exceeds the
  original, then the linked determinativa is superseded with state
  aceptada and the imported SAR-rectified determination replaces the frozen
  snapshot; given a rectificativa lowering the tax, then the determinativa
  state = rechazo with the contact-AT workflow surfaced (FR-047, FR-048,
  FR-068).
- **AC-007:** Given a May-2024 retention month, then the declaration
  resolves to regime `djimr`; given April-2024, then regime `dmr`; given an
  omisa DMR month (e.g. 2023-11), then the migration path files it through
  DJIMR via OVI and the record keeps the `dmr` period regime (FR-046).
- **AC-008:** Given a retention move tagged código 112, then the DJIMR-112
  line carries 12.5% as catalog metadata while the retained amount is
  computed by the taxation engine id (HN-TAX-FR-137); given a move tagged
  215, 523, 524 or 501, then no DJIMR row is generated (scope guard)
  (FR-049, FR-075).
- **AC-009:** Given the channel matrix, then 111/113/115/116 informativas
  accept OVI or SW, 112/136/138/217 informativas are OVI-only, every
  determinativa is OVI, and the 135 informativa channel row reads
  UNRESOLVED with both prints cited (FR-050).
- **AC-010:** Given a first 111 informativa filed via SW, then a subsequent
  OVI attempt for the same family warns/blocks (one modality) and the
  rectification UI routes to SW; given a declaration filed pre-May-2024,
  then the same-modality constraint is waived (FR-050, FR-051).
- **AC-011:** Given a filed DJIMR-111 for 2026-01, then posting an
  additional January 111 retention move is blocked; the correction flows
  only through a rectificativa, which triggers the de-oficio propagation
  (FR-071, FR-047).
- **AC-012:** Given a 112 line for a State transaction, then both document
  pairs are present (provider CAI/doc/date + voucher CAI/date) plus
  institución code and F01; given a missing voucher reference, then the
  line is blocked from the informativa (FR-056, FR-065).
- **AC-013:** Given a distribution to a shareholder holding 1,000 of
  10,000 shares (L50,000 nominal capital), then the 113 census row carries
  1112 = 1000, 1113 = 50.00 and 1114/1115 as separate as-printed
  percentage fields; given a foreign shareholder, then 1120 accepts the
  SAR-annex code including a stale entry, flagged but never ISO-normalized
  (FR-057, FR-058).
- **AC-014:** Given a 115 line for a retenido natural person without RTN,
  then casilla 2 accepts the DNI (ID-type pair) and the instrument fields
  36/37/38 are captured; given a bank-paymaster exclusion flag unset for
  D. 110-93 acquisition, then the exclusion stays config-gapped, not
  computed (FR-059, FR-073).
- **AC-015:** Given a State purchase of a 15%-rated good (base L10,000)
  and an 18%-rated service (base L10,000), then the 116 line carries
  Importe base 15% = 10,000 and Importe base 18% = 10,000 with Retenido =
  the ISV itself (1,500 + 1,800) and the TGR routing flag surfaced
  (FR-060, FR-070).
- **AC-016:** Given a 138 retention on a non-resident with no RTN and a
  passport, then the ID triplet validates (at-least-one satisfied) and the
  filing is generated through the eventual path; given neither passport/CA
  nor foreign tax ID, then the line is blocked (FR-063, FR-052).
- **AC-017:** Given a 111 export built from full-precision retention
  records (base 1,234.567), then the uploaded plantilla value reads 1,234.57
  (2dp print-faithful) and no band value is re-derived (FR-055).
- **AC-018:** Given an extemporaneous DJIMR filing, then the multa payment
  attachment is generated on the Pagar/Boletín pair and the CT Art. 160
  hook is recorded for the missed per-código deadline (FR-069).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | 111 plantilla↔casillas mapping (origin `32_ OQ-1`, VERIFY): the Ayuda restates no computation; verify at implementation that the plantilla DMR-sheet export columns map 1:1 to casillas 2/43/44/45/46 (numbering source = 32_ §2.2). | no | Takumi S-HN3 | open |
| OQ-002 | 136 L15,000 anchor (origin `31_ OQ-1`, VERIFY): the monthly-per-property threshold + m² proration are not restated in the Ayuda and no OVI validation hint exists; confirm whether OVI enforces the threshold or it rests on the taxpayer (anchor = HN-TAX-FR-177/178). | no | Takumi S-HN3 | open |
| OQ-003 | 136 determinativa Tarifa (origin `31_ OQ-2`, CONFIG): Tarifa appears in Section A but its value (presumably 10%) is nowhere printed for 136. | no | Takumi S-HN3 | open |
| OQ-004 | 112 sole-source exception amount (origin `33_ OQ-1`, CONFIG; kin `01_ OQ-6`): 71_ restates the exception tabla-relative ("base exenta según la Tabla Progresiva del artículo 22") with no lempira amount — consume the composite gate of HN-TAX-FR-135 (FY2025 L257,493.16; FY2026 ≈ L268,324.32 unpinned). | no | Takumi S-HN3 (consumes S-HN1) | open |
| OQ-005 | 112 OVI-only anomaly (origin `33_ OQ-2`, VERIFY): 112 lacks the SW plantilla path while 111/113/115/116/135(37_) have it — highest-volume retention, possibly a stale manual; verify vs live OVI/SW or the SAR-236-2024 ordinal (kin `32_ OQ-2`, file 01). | no | Takumi S-HN3 | open |
| OQ-006 | Casilla 1114 vs 1115 semantics (origin `34_ OQ-1`, CONFIG): "Parte social" (% del capital social) vs "Porcentaje participación" overlap; intended distinction undefined — needs SAR field gloss or a filled sample; carried distinct as printed (FR-057). | no | Takumi S-HN3 | open |
| OQ-007 | 34_ print artifact (origin `34_ OQ-2`, VERIFY): determinativa filter text "Retención por impuesto a la venta" (p.29) is chassis text recycled from the 116 manual — never cite as 113 content. Recorded to prevent mis-citation. | no | — | open (guard note) |
| OQ-008 | Country codes stale (origin `34_ OQ-3`, DECIDE): Anexo 1 carries YU/TP/ZZ/AN — SAR-accepted validation list vs ISO 3166-1. Default = annex as printed with stale flags (FR-058); product decision whether to offer ISO aliases. | no | product owner + Takumi S-HN3 | open |
| OQ-009 | 115 exclusions (origin `35_ OQ-1`, LEAD): the three exclusions (banks→Art. 22; D. 99-93 FX deposits; D. 110-93 Art. 12 monto) appear only in 71_; no OVI casilla encodes excluded-interest reporting — acquire D. 110-93 (+D. 99-93) and pin the mechanism (FR-073 config gate). | no | acquisition queue | open |
| OQ-010 | 115 casilla 2 RTN o DNI (origin `35_ OQ-2`, CONFIG): DNI format and OVI validation unpinned — ID-type pair encoded (FR-059), format rules pending. | no | Takumi S-HN3 | open |
| OQ-011 | 116 base-legal moving target (origin `36_ OQ-1`, CONFLICT): D.L. 182-2020 Art. 100 (36_) vs D. 5-2001 + D. 62-2023 Art. 137 (71_) — successive annual budget-law re-enactments, none acquired; pin the current year's article before shipping public-sector 116 (FR-074). | no | acquisition queue + Takumi S-HN3 | open |
| OQ-012 | 116 routing (origin `36_ OQ-2`, CONFIG/CONFLICT): 71_ directs entero to the Tesorería General de la República while the 36_ UI shows the standard bank Pagar/Boletín; also confirm the 100%-of-tax reading (R-H33 partial) from the budget-law article once acquired. | no | Takumi S-HN3 | open |
| OQ-013 | 116 casilla print defects (origin `36_ OQ-3`, VERIFY): "4646-Retenido" odd numbering and a duplicated 32-gloss — encode numbering as printed; never cite the second 32 gloss. | no | — | open (guard note) |
| OQ-014 | 135 exemption family (origin `37_ OQ-2`, VERIFY): the D. 17-2010 Art. 19 exemption family (incl. the D. 28-2019 waste-collector interp, R-H7) is absent from the Ayuda and from any card field — keep exemption logic sourced from the taxation wave's catalog (HN-TAX-FR-145/146, `04_`/`21_`/`22_`), never from the Ayudas. | no | Takumi S-HN3 (consumes S-HN1) | open |
| OQ-015 | 138 Tarifa for non-real-estate (origin `38_ OQ-1`, CONFIG): the Art. 5 non-resident gross-rate table is not reproduced in the Ayuda; what Tarifa OVI expects for a 138 filing on non-real-estate gains (vs the 122-134 codes covering them) is unpinned — rates by id from HN-TAX-FR-101/102, config-gated. | no | Takumi S-HN3 | open |
| OQ-016 | 138 deadline duality (origin `38_ OQ-2`, CONFLICT): Eficiencia Art. 14 says enter within 10 días calendario following THE TRANSACTION; the same page restates the monthly rule (Art. 35 + SAR-238-2024). FR-063 models BOTH (alert at the earlier, flagged); flag for SAR ruling — never resolve silently. | no | controller + SAR ruling | open |
| OQ-017 | 138 print defects (origin `38_ OQ-3`, VERIFY): "Decreto No.11-2011" [sic — 113-2011] and an ellipsed D. 273-2013 quote — the full Art. 14 text must come from the Eficiencia consolidation (`05_`, taxation wave), not this Ayuda. | no | — | open (guard note) |
| OQ-018 | 135 channel conflict (origin `39_ OQ-1`, CONFLICT; `37_ OQ-1` = same single issue): 37_ says informativa OVI+SW (and documents the SW pipeline + Alta flow); 39_ says OVI-only. Treat 37_ as canonical for content (R-H21); channel row = UNRESOLVED until the SAR-236-2024 ordinal pins the list (acquisition lead `32_ OQ-2`, file 01) or a live OVI/SW check. | no | Takumi S-HN3 + acquisition queue | open |
| OQ-019 | Duplicate 135 manual (origin `39_ OQ-2`, VERIFY): reason for two prints (audience/vintage/SW-rollout timing) unknown — dedupe the registry only after OQ-018 resolves; both retained for provenance. | no | registry keeper | open |
| OQ-020 | 217 rate semantics (origin `40_ OQ-1`, CONFIG): whether the retention is 15/18% OF THE TAX (Art. 8's facultad text suggests %-of-tax: "retenciones total o parcialmente sobre el Impuesto causado") or of the gross base is nowhere stated — needs DEI-SG-215-2010 text (lead) or a SAR ruling; FR-064 stores buckets only. | no | acquisition queue + Takumi S-HN3 | open |
| OQ-021 | 217 citation form (origin `40_ OQ-2`, VERIFY): "Acuerdo DEI-215-2010" (40_/71_ header) vs "Acuerdo DEI-SG-215-2010" (71_ table row; same for 217-2010) — use the DEI-SG- full form in the acquisition queue, note the short form. | no | acquisition queue | open |
| OQ-022 | 135 base gloss (origin `71_ OQ-2`, CONFLICT): 71_'s "base imponible debe ser las ventas brutas menos las devoluciones descuentos y rebajas" reads like the retainer's sales test pasted as the retention base; default = base is the PURCHASE amount, gate = net gross sales (FR-061); confirm vs Art. 19 text (`04_`, taxation wave). | no | controller + Takumi S-HN3 | open |
| OQ-023 | 71_ base-legal divergences (origin `71_ OQ-3`, CONFLICT; R-H27 discipline): 116 (D.5-2001+D.62-2023 vs 36_'s D.L. 182-2020 Art. 100 → OQ-011), 138 (Art. 7 D.17-2010 vs 38_'s D.273-2013→Eficiencia-14), 136 (Art. 5 D.17-2010+Regl. 1121-2010 Art. 13 vs 31_'s Regl. Art. 9) — 71_ = SAR-current compilation cited per row; divergences = acquisition priorities, never resolved law. | no | acquisition queue | open |
| OQ-024 | Catalog breadth beyond retentions (origin `71_ OQ-4`, VERIFY): 71_'s sheet also carries 254 (already in the DJIMR catalog) and 524/501 (financial-transactions contribution, SAR-239-2024 family) — cross-cite EV31:EVID-125 for those families; no re-derivation here (FR-075 guard). | no | sibling files (contribuciones wave) | open |


