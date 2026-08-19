# SV — Special regimes — ZF/DPA exemption schedules: D15 ladders, dividend window, exception goods

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes) |
| Updated | 2026-08-19 |

## 1. Purpose

This file is the wave's canonical D15 deliverable: the per-beneficiary dated
exemption-window rows of the Ley de Zonas Francas Industriales y de
Comercialización (12_) — the *usuario* ISR phase-down ladders (100% → 60% →
40%) and municipal tails (100% → 90% → 75% indefinite), the shorter DPA
titular tracks, the flat *desarrollista*/*administrador* windows with their
ITBIR exemption and 54-C grandfathering, the extension events (ampliación,
100%-investment-increase, 17-B/19-C strategic sectors) — each row keyed by the
Task-1 beneficiary profile (regime × role × location track metro/fuera ×
*acuerdo* D.O. date) and resolved as-of the fiscal year with
snapshot-on-write; the percentage-of-rate computation limited to the
*actividad autorizada* (authorized activity); the 12-*ejercicio* dividend
window with its exemption-suppresses-retention implication; the
exception-goods inverting gate (paid-IVA/DM-a-pago evidence on admission);
the DPA capital-goods 5-year free-transfer rule; the per-*acuerdo*
no-necessary-goods tariff nomenclature with its retroactive-acceptance
modification procedure; the Quincena-25 certificado consumption (by id) with
the declaration-duty-survives-exemption guard; and the comercializador
municipal proration.

It does **not** cover: the LSI exemption shapes and local-market caps
(`03_lsi-regime.md`); the customs clocks (`04_customs-clocks.md`); the
TAN/IVA routing of regime sales, the non-national-component duty base and
the full comercializador transfer-tax treatment (`05_tan-iva-interface.md`
— this file owns only the incentive-exclusion/municipal-proration side);
DUCA/teledespacho declarations (`06_customs-declarations.md`); obligations,
DGA-facing reporting and SMM-priced sanctions (`07_obligations-reporting-
sanctions.md`); FOVIAL/COTRANS (`08_fovial-cotrans.md`). It consumes Task
1's beneficiary-profile and benefit-state model by FR id (SV-SPE-FR-003,
FR-015, FR-016, FR-022) and never restates it.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF/DPA = **12_**
(D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998; consolidated
through reform (8) D.L. 318-2013; content title "Ley de Zonas Francas
Industriales y de Comercialización"). Pointer LBs of this file: the Ley ISR
Art. 72 interplay = **54_** (consolidated print; full authority owned by
`taxation/05_isr-distributions.md` LB-001 — cited here at pointer depth);
the Quincena-25 declaration surfaces = **67_** (Guía de Orientación
Quincena-25, Anexos 7/8 — computation authority owned by
`taxation/01_isr-framework.md` SV-TAX-FR-174, never restated here); the
declaration-duty kin = **14_** (LSI Art. 14, explicit text — the ZF-side
12_ print is corpus-silent on the declaration duty; the guard below is
anchored on the LSI twin expressly, as the S7 plan directs).

**SOQ-30 verification note (rides EVERY regime LB in this file):** the 12_
consolidation ends at D.L. 318-2013 (and 14_ at its 2007 print) —
post-cutoff reforms are unverified until official routes recover (SOQ-22
kin); article text is cited **as printed**. Verbatim text below is copied
from the W13 evidence files (EVID-253/254/255/256/257) and, where the
evidence abbreviates, from the extraction txt
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt` (citable per standing S3
ruling 25; page pointers = txt PAGE markers). D15 discipline: every
percentage, year-count, threshold and window in this file is a dated config
row with instrument provenance — never a global constant.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 17 d): "EXENCIÓN TOTAL DEL IMPUESTO SOBRE LA RENTA, SOBRE LA ACTIVIDAD AUTORIZADA: 1. POR UN PLAZO DE QUINCE (15) AÑOS, CONTADOS A PARTIR DE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO EMITIDO POR EL MINISTERIO DE ECONOMÍA, SI SE UBICA EN EL ÁREA METROPOLITANA. VENCIDO EL PLAZO CONCEDIDO, EL USUARIO TENDRÁ DERECHO A UNA EXENCIÓN PARCIAL DE LA SIGUIENTE MANERA: UN SESENTA POR CIENTO DE EXENCIÓN (60%) DE LA TASA DEL IMPUESTO SOBRE LA RENTA, APLICABLE DURANTE LOS DIEZ (10) AÑOS SIGUIENTES AL VENCIMIENTO DEL PLAZO ORIGINAL… UN CUARENTA POR CIENTO DE EXENCIÓN (40%) DE LA TASA DEL IMPUESTO SOBRE LA RENTA, APLICABLE DURANTE LOS DIEZ (10) AÑOS SIGUIENTES DE VENCIDO EL PLAZO ANTERIOR. 2. POR UN PLAZO DE VEINTE (20) AÑOS… SI SE UBICA FUERA DEL ÁREA METROPOLITANA. VENCIDO… UN SESENTA POR CIENTO DE EXENCIÓN (60%)… DURANTE LOS QUINCE (15) AÑOS SIGUIENTES… UN CUARENTA POR CIENTO (40%)… DURANTE LOS DIEZ (10) AÑOS SIGUIENTES…". Dividend window (in d), same in Art. 11 a)/Art. 19 d)): "A PARTIR DEL DÉCIMO TERCER EJERCICIO FISCAL, CONTADO DESDE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO DE CALIFICACIÓN EMITIDO POR EL MINISTERIO DE ECONOMÍA, LAS UTILIDADES O DIVIDENDOS DISTRIBUIDOS, PROVENIENTES DE LA ACTIVIDAD FAVORECIDA, SERÁN GRAVADOS CON EL IMPUESTO SOBRE LA RENTA. DURANTE LOS DOCE EJERCICIOS FISCALES, CONTADO DESDE LA PUBLICACIÓN… LA EXENCIÓN EN EL CASO DE LAS SOCIEDADES SE APLICARÁ, TANTO A LA SOCIEDAD USUARIA, COMO A LOS SOCIOS O ACCIONISTAS INDIVIDUALMENTE CONSIDERADOS, RESPECTO A LAS UTILIDADES O DIVIDENDOS PROVENIENTES DE LA ACTIVIDAD FAVORECIDA. EN CASO QUE UNO O MÁS SOCIOS SEAN PERSONAS JURÍDICAS, ESTE DERECHO SERÁ EXCLUSIVO DE ÉSTAS. ESTE BENEFICIO NO PODRÁ TRASLADARSE SUCESIVAMENTE A SUS SOCIOS." | Total ISR exemption ON THE AUTHORIZED ACTIVITY: 1. for a term of fifteen (15) years counted from the D.O. publication of the MINEC acuerdo, if located in the metropolitan area; upon expiry a PARTIAL exemption follows: 60% of the ISR RATE for the ten (10) following years, then 40% for the ten (10) years after that; 2. for twenty (20) years outside the metropolitan area, then 60% for the fifteen (15) following years, then 40% for the ten (10) years after. Dividend window (ditto in Arts. 11/19): from the THIRTEENTH fiscal ejercicio counted from the D.O. publication of the qualification acuerdo, distributed utilidades or dividends from the favored activity are TAXED with ISR; during the TWELVE fiscal ejercicios from that publication the exemption applies both to the user society AND to the partners or shareholders individually considered; where one or more partners are legal persons the right is EXCLUSIVE of those and may NOT be transferred successively to their own partners | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17 d) pp.14-15 (EVID-254; txt PAGE 14-15; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 17 e): "EXENCIÓN TOTAL DE LOS IMPUESTOS MUNICIPALES: 1. POR UN PLAZO DE QUINCE (15) AÑOS, A PARTIR DE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO… SI SE UBICA EN EL ÁREA METROPOLITANA. VENCIDO EL PLAZO CONCEDIDO… UN NOVENTA POR CIENTO DE EXENCIÓN (90%) DE LOS IMPUESTOS MUNICIPALES APLICABLES, DURANTE LOS DIEZ (10) AÑOS SIGUIENTES AL VENCIMIENTO DEL PLAZO ORIGINAL… UN SETENTA Y CINCO POR CIENTO DE EXENCIÓN (75%) DE LOS IMPUESTOS MUNICIPALES APLICABLES, EN ADELANTE. 2. POR UN PLAZO DE VEINTE (20) AÑOS… FUERA DEL ÁREA METROPOLITANA. VENCIDO… UN NOVENTA POR CIENTO… DURANTE LOS QUINCE (15) AÑOS SIGUIENTES… UN SETENTA Y CINCO POR CIENTO… EN ADELANTE. LOS CONCEJOS MUNICIPALES… PODRÁN OTORGAR BENEFICIOS ADICIONALES A LOS ESTABLECIDOS EN LA PRESENTE LEY." Investment-increase extension (after f)): "VENCIDO EL PLAZO DE LAS EXENCIONES TOTALES, LOS USUARIOS TENDRÁN DERECHO A UN PLAZO ADICIONAL DE CINCO (5) AÑOS, SI SE COMPRUEBA QUE DURANTE LOS ÚLTIMOS CINCO (5) AÑOS DE LA EXENCIÓN TOTAL, HAN AUMENTADO SU INVERSIÓN EN UN 100% CON RELACIÓN A SU INVERSIÓN INICIAL. ESTE INCREMENTO EN LA INVERSIÓN DEBERÁ REALIZARSE EN LA COMPRA DE TERRENOS, EN LA CONSTRUCCIÓN DE EDIFICACIONES Y EN LA ADQUISICIÓN DE MAQUINARIA Y EQUIPO, VINCULADAS A LA ACTIVIDAD AUTORIZADA." | Total municipal-tax exemption: 1. for fifteen (15) years from the D.O. publication of the acuerdo in the metropolitan area; upon expiry 90% of the applicable municipal taxes for the ten (10) following years, then 75% ONWARD (indefinite tail); 2. twenty (20) years outside, then 90% for the fifteen (15) following years, then 75% onward. Municipal councils may grant ADDITIONAL benefits beyond the law's. Extension: after the total-exemption term, usuarios get FIVE (5) additional years if during the last five years of total exemption they INCREASED their investment by 100% relative to their initial investment — in land purchase, building construction and machinery/equipment acquisition linked to the authorized activity | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17 e) + final ext. inciso pp.15-16 (EVID-254; txt PAGE 15-16; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 17 (nomenclature + modification incisos): "EL MINISTERIO DE ECONOMÍA DEBERÁ INCORPORAR EN EL ACUERDO QUE EMITA CON OCASIÓN DE LA AUTORIZACIÓN DE UN USUARIO, EL DETALLE DE AQUELLOS BIENES QUE NO SE CONSIDEREN NECESARIOS PARA LA EJECUCIÓN DE LA ACTIVIDAD AUTORIZADA, CON SU RESPECTIVA NOMENCLATURA ARANCELARIA, DE FORMA PARTICULAR O GENERAL, UTILIZANDO SECCIONES, CAPÍTULOS, PARTIDAS O SUBPARTIDAS, SEGÚN CORRESPONDA. EL USUARIO PODRÁ SOLICITAR AL MINISTERIO DE ECONOMÍA MODIFICACIONES AL DETALLE DE BIENES RELACIONADOS EN EL INCISO ANTERIOR, EXPRESANDO LA CAUSA QUE LO MOTIVA. EL MINISTERIO EMITIRÁ EL ACUERDO RESPECTIVO, DENTRO DEL PLAZO DE VEINTE (20) DÍAS HÁBILES, PREVIA OPINIÓN DEL MINISTERIO DE HACIENDA, EL QUE DEBERÁ RENDIRLA EN EL PLAZO DE QUINCE (15) DÍAS HÁBILES… UNA VEZ PRESENTADA LA SOLICITUD DE MODIFICACIÓN…, EL TITULAR PODRÁ IMPORTAR BAJO EL RÉGIMEN LOS BIENES CUYA MODIFICACIÓN HA SOLICITADO, CON SUSPENSIÓN EN EL PAGO DE LOS DERECHOS E IMPUESTOS DURANTE EL PERÍODO EN QUE SE PROCESE LA SOLICITUD; SI LA RESOLUCIÓN FUERE ACEPTADA, SE RETROTRAERÁ A LA FECHA DEL REGISTRO DE LA RESPECTIVA DECLARACIÓN DE MERCANCÍAS; SI FUERE DENEGADA EN TODO O EN PARTE, EL USUARIO DEBERÁ PAGAR INMEDIATAMENTE LOS DERECHOS E IMPUESTOS CORRESPONDIENTES A LOS BIENES CUYA MODIFICACIÓN FUERE DENEGADA. LA DIRECCIÓN GENERAL DE ADUANAS IMPLEMENTARÁ LOS MEDIOS ELECTRÓNICOS QUE GARANTICEN LA OPERATIVIDAD MECANIZADA DE LA APLICACIÓN DEL DETALLE… AL MOMENTO DEL TELEDESPACHO…" | MINEC must incorporate into the usuario authorization acuerdo the detail of goods NOT considered necessary for the authorized activity, with their tariff nomenclature, particular or general, using SECTIONS, CHAPTERS, HEADINGS or SUBHEADINGS as corresponds. The usuario may request modifications expressing the cause; MINEC issues the acuerdo within twenty (20) días hábiles, prior MH opinion rendered within fifteen (15) días hábiles. Once the modification request is filed the holder may import the requested goods under the regime with SUSPENSION of duties and taxes while the request processes; if the resolution is ACCEPTED it RETROACTS (retrotrae) to the registration date of the respective goods declaration (DM); if DENIED in whole or part, the usuario must pay the corresponding duties and taxes IMMEDIATELY for the denied goods. The DGA implements electronic means for the mechanized application of the detail at teledespacho time | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17 pp.16-17 (EVID-254; txt PAGE 16-17; SOQ-30 print) |
| LB-004 | Ley de Zonas Francas, Art. 17 (final exception-goods paragraph): "SE EXCEPTÚAN DE LOS BENEFICIOS CONTENIDOS EN LOS LITERALES a), b) Y c) DEL PRESENTE ARTÍCULO, LA ADQUISICIÓN DE LOS BIENES Y SERVICIOS SIGUIENTES: ALIMENTACIÓN Y BEBIDAS, EXCEPTO AGUA ENVASADA; PRODUCTOS QUE CONTENGAN TABACO, BEBIDAS ALCOHÓLICAS, ARRENDAMIENTO DE VIVIENDA, MUEBLES Y ENSERES DEL HOGAR, ARTÍCULOS SUNTUARIOS O DE LUJO, VEHÍCULOS PARA TRANSPORTE DE PERSONAS DE FORMA INDIVIDUAL O COLECTIVA Y MERCANCÍAS, SERVICIOS DE HOTELES, EN CUYO CASO, SU INGRESO A LAS ZONAS FRANCAS ESTARÁ SUPEDITADO A LA PRESENTACIÓN DE LA DECLARACIÓN DE MERCANCÍAS DEFINITIVA A PAGO, SI SE TRATA DE MERCANCÍAS EXTRANJERAS O LA PRESENTACIÓN DE LOS COMPROBANTES DE CRÉDITO FISCAL O FACTURA DE CONSUMIDOR FINAL, SI SE TRATARE DE COMPRAS DE DICHOS BIENES EN EL MERCADO LOCAL, EN LOS CUALES CONSTE QUE SE HA PAGADO EL IMPUESTO CORRESPONDIENTE; SALVO QUE LA ACTIVIDAD BENEFICIADA REQUIERA DE DICHOS BIENES O SERVICIOS PARA LA PRODUCCIÓN, ENSAMBLE O MAQUILA, MANUFACTURA, PROCESAMIENTO, TRANSFORMACIÓN O COMERCIALIZACIÓN, EN CUYO CASO DEBERÁ HACERSE DEL CONOCIMIENTO DEL MINISTERIO DE ECONOMÍA AL MOMENTO DE SOLICITAR LA AUTORIZACIÓN NECESARIA PARA OPERAR, DEBIENDO DICHO MINISTERIO CONSIGNARLO EN EL RESPECTIVO ACUERDO QUE EMITA AL USUARIO." | Excluded from the benefits of Art. 17 a), b) and c): food and beverages except bottled water; tobacco products; alcoholic beverages; housing rental; home furniture and furnishings; sumptuary or luxury articles; vehicles for individual or collective person transport and goods; hotel services — their ENTRY into the free zones is CONDITIONED on presenting the definitive-payment goods declaration (DM definitiva a pago) for foreign goods, or the Comprobante de Crédito Fiscal (tax-credit document, CCF) or Factura de Consumidor Final (final-consumer invoice, FCF) for local purchases, evidencing that the corresponding TAX HAS BEEN PAID; UNLESS the benefited activity requires those goods or services for production, assembly or maquila, manufacture, processing, transformation or commercialization — in which case it must be made known to MINEC when requesting the operating authorization, MINEC recording it in the respective acuerdo | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17 final ¶ p.17 (EVID-254; txt PAGE 17; SOQ-30 print) |
| LB-005 | Ley de Zonas Francas, Art. 11 (desarrollista): "a) EXENCIÓN TOTAL DEL IMPUESTO SOBRE LA RENTA: 1) POR EL PERÍODO DE DIEZ (10) AÑOS CONTADOS DESDE EL EJERCICIO QUE INICIE SUS OPERACIONES POR LA ACTIVIDAD DEDICADA A ZONAS FRANCAS, SI SE UBICA EN EL ÁREA METROPOLITANA; 2)… QUINCE (15) AÑOS… FUERA DEL ÁREA METROPOLITANA. A PARTIR DEL DÉCIMO TERCER EJERCICIO FISCAL, CONTADO DESDE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO DE CALIFICACIÓN…, LAS UTILIDADES O DIVIDENDOS DISTRIBUIDOS… SERÁN GRAVADOS… DURANTE LOS DOCE EJERCICIOS FISCALES… LA EXENCIÓN… TANTO A LA SOCIEDAD PROPIETARIA DE LA ZONA FRANCA, COMO A LOS SOCIOS O ACCIONISTAS INDIVIDUALMENTE CONSIDERADOS… EN CASO QUE UNO O MÁS SOCIOS SEAN PERSONAS JURÍDICAS, ESTE DERECHO SERÁ EXCLUSIVO DE ÉSTAS… b) EXENCIÓN TOTAL DE LOS IMPUESTOS MUNICIPALES: [10 años metro / 15 años fuera, mismo ancla de inicio de operaciones]… c) EXENCIÓN TOTAL DEL IMPUESTO SOBRE TRANSFERENCIA DE BIENES RAÍCES, POR LA ADQUISICIÓN DE AQUELLOS BIENES RAÍCES A SER UTILIZADOS EN LA ACTIVIDAD INCENTIVADA." Ampliation extension: "LOS DESARROLLISTAS TENDRÁN DERECHO A UN PLAZO ADICIONAL DE CINCO AÑOS PARA LAS EXENCIONES RELATIVAS AL PAGO DEL IMPUESTO SOBRE LA RENTA E IMPUESTOS MUNICIPALES, SIEMPRE QUE DURANTE EL PERÍODO DE LA EXENCIÓN TOTAL HAYAN INVERTIDO EN UNA AMPLIACIÓN DE LA ZONA FRANCA QUE CUMPLA CON LAS CARACTERÍSTICAS SIGUIENTES: I. QUE LA SUPERFICIE TOTAL DE LA AMPLIACIÓN SE ENCUENTRE UBICADA EN UN RADIO NO MAYOR A CINCO KILÓMETROS MEDIDO DESDE EL LINDERO DEL ÁREA PREVIAMENTE AUTORIZADA…; II. QUE LA SUPERFICIE DE LA AMPLIACIÓN SEA COMO MÍNIMO DE OCHO MANZANAS; III. QUE CUMPLA CON LOS REQUISITOS MÍNIMOS DE INFRAESTRUCTURA ESTABLECIDOS EN EL ARTÍCULO 10…" | Desarrollista rights: a) total ISR exemption for ten (10) years counted from the ejercicio in which operations for the free-zone activity START (metro) / fifteen (15) years (fuera) — NOTE the ladder anchor is OPERATIONS START, while the dividend window (12 ejercicios exempt, 13th taxed; PJ-socio exclusivity) counts from the D.O. PUBLICATION of the qualification acuerdo — two distinct anchors; b) total municipal-tax exemption 10y/15y on the same operations-start anchor; c) total real-estate transfer-tax (ITBIR) exemption on acquisitions of real estate to be used in the incentivated activity. +5-year ISR+municipal extension for an ampliation of the zone invested during the total-exemption period: entire ampliation surface within a five-kilometer radius of the previously authorized area's boundary, minimum surface EIGHT MANZANAS, meeting Art. 10's minimum-infrastructure requirements | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 11 pp.12-13 (EVID-253; txt PAGE 12-13; SOQ-30 print) |
| LB-006 | Ley de Zonas Francas, Art. 13: "LOS ADMINISTRADORES DE ZONA FRANCA DEBERÁN PROPORCIONAR O PROVEER DIRECTAMENTE A LAS EMPRESAS QUE EN ELLA OPEREN LAS FACILIDADES PARA EL SUMINISTRO DE AGUA, ENERGÍA ELÉCTRICA Y TREN DE ASEO, COORDINAR EL MANTENIMIENTO DE TODOS LOS SERVICIOS COMUNES…" (administrador role/duties frame; the former administrador-benefit articles 14 and 15 read "DEROGADO POR D.L. No. 318/2013"). Art. 54-C: "LOS DESARROLLISTAS Y ADMINISTRADORES DE ZONAS FRANCAS QUE SE ENCUENTREN OPERANDO AL MOMENTO DE LA ENTRADA EN VIGENCIA DEL PRESENTE DECRETO, CONTINUARÁN CON LAS EXENCIONES TOTALES HASTA EL 31 DE DICIEMBRE DE 2015 O HASTA EL VENCIMIENTO DEL PLAZO ESTABLECIDO EN SU RESPECTIVO ACUERDO, SI FUERE POSTERIOR A DICHA FECHA. VENCIDO DICHO PLAZO, TANTO DESARROLLISTAS COMO ADMINISTRADORES, Y SUS SOCIOS O ACCIONISTAS EN EL CASO, DE UTILIDADES O DIVIDENDOS DISTRIBUIDOS, GOZARÁN DE CINCO AÑOS ADICIONALES EN LAS MISMAS CONDICIONES Y ALCANCES ESTABLECIDOS EN LOS LITERALES a) Y b) DEL ARTÍCULO 11 DE ESTA LEY. EN EL CASO QUE LA MISMA PERSONA REALICE LAS FUNCIONES DE DESARROLLISTA Y ADMINISTRADOR DE ZONAS FRANCAS, ÉSTE GOZARÁ DE AMBOS BENEFICIOS. LOS DESARROLLISTAS Y ADMINISTRADORES… TENDRÁN DERECHO A UN PLAZO DE EXENCIÓN ADICIONAL DE CINCO AÑOS, SIEMPRE QUE… HAYAN INVERTIDO EN UNA AMPLIACIÓN… QUE CUMPLA CON LAS CARACTERÍSTICAS ESTABLECIDAS EN EL INCISO ÚLTIMO DEL ARTÍCULO 11…" | Administrators must provide/coordinate water, energy, waste-collection and common-services facilities (Art. 13 role frame); the pre-2013 administrador benefit articles are DEROGATED (Arts. 14/15, D.L. 318-2013). Art. 54-C (transitory): desarrollistas and administrators operating at the decree's entry into force CONTINUE total exemptions until 31-December-2015 or until the expiry of their respective acuerdo's term if LATER; after that term both roles — and their partners/shareholders for distributed utilidades or dividends — enjoy FIVE ADDITIONAL YEARS under the same conditions and scope of Art. 11 a) and b); a person performing BOTH roles enjoys BOTH benefits; they also get the +5-year extension for an Art. 11-final qualifying ampliation | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 13 p.13 + Arts. 14/15 (derogated) p.13 + Art. 54-C p.43 (EVID-253; txt PAGE 13, 43; SOQ-30 print) |
| LB-007 | Ley de Zonas Francas, Art. 19 d): "EXENCIÓN TOTAL DEL IMPUESTO SOBRE LA RENTA, SOBRE LA ACTIVIDAD AUTORIZADA: 1) POR UN PLAZO DE DIEZ (10) AÑOS, CONTADOS A PARTIR DE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO EMITIDO POR EL ÓRGANO EJECUTIVO EN EL RAMO DE ECONOMÍA, SI SE UBICA EN EL ÁREA METROPOLITANA. VENCIDO EL PLAZO… UN SESENTA POR CIENTO DE EXENCIÓN (60%) DE LA TASA DEL IMPUESTO SOBRE LA RENTA, APLICABLE DURANTE LOS CINCO (5) AÑOS SIGUIENTES… UN CUARENTA POR CIENTO DE EXENCIÓN (40%)… DURANTE LOS DIEZ (10) AÑOS SIGUIENTES… 2) POR UN PLAZO DE QUINCE (15) AÑOS… FUERA DEL ÁREA METROPOLITANA. VENCIDO… UN SESENTA POR CIENTO… APLICABLE DURANTE LOS DIEZ (10) AÑOS SIGUIENTES… UN CUARENTA POR CIENTO… DURANTE LOS DIEZ (10) AÑOS SIGUIENTES…" (same dividend-window paragraph as Art. 17 d): 12 ejercicios exempt from D.O. publication, 13th taxed, sociedad + socios, PJ-socios exclusivity — "LA SOCIEDAD TITULAR" wording) | DPA-titular total ISR exemption ON THE AUTHORIZED ACTIVITY: 1) ten (10) years from the D.O. publication of the acuerdo (metro), then 60% of the ISR rate for the five (5) following years, then 40% for the ten (10) years after; 2) fifteen (15) years (fuera), then 60% for the ten (10) following years, then 40% for the ten (10) years after — with the same 12-ejercicio dividend window and PJ-socios exclusivity as Art. 17 d) (here naming the TITULAR society) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19 d) pp.21-22 (EVID-256; txt PAGE 21-22; SOQ-30 print) |
| LB-008 | Ley de Zonas Francas, Art. 19 e): "EXENCIÓN TOTAL DE LOS IMPUESTOS MUNICIPALES: 1) POR UN PLAZO DE DIEZ (10) AÑOS, A PARTIR DE LA PUBLICACIÓN EN EL DIARIO OFICIAL DEL ACUERDO… SI SE UBICA EN EL ÁREA METROPOLITANA. VENCIDO… UN NOVENTA POR CIENTO DE EXENCIÓN (90%) DE LOS IMPUESTOS MUNICIPALES, APLICABLE DURANTE LOS PRIMEROS CINCO (5) AÑOS SIGUIENTES… UN SETENTA Y CINCO POR CIENTO DE EXENCIÓN (75%)… EN ADELANTE. 2) POR UN PLAZO DE QUINCE (15) AÑOS… FUERA… UN NOVENTA POR CIENTO… DURANTE LOS DIEZ (10) AÑOS SIGUIENTES… UN SETENTA Y CINCO POR CIENTO… EN ADELANTE. LOS CONCEJOS MUNICIPALES… PODRÁN OTORGAR BENEFICIOS ADICIONALES…" | DPA-titular total municipal-tax exemption: 1) ten (10) years from the D.O. publication (metro), then 90% for the first five (5) following years, then 75% ONWARD (indefinite tail); 2) fifteen (15) years (fuera), then 90% for the ten (10) following years, then 75% onward; municipal councils may grant additional benefits | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19 e) pp.22-23 (EVID-256; txt PAGE 22-23; SOQ-30 print) |
| LB-009 | Ley de Zonas Francas, Art. 19 (DPA nomenclature + modification + exception goods, final incisos): "EL MINISTERIO DE ECONOMÍA DEBERÁ INCORPORAR EN EL ACUERDO QUE EMITA CON OCASIÓN DE LA AUTORIZACIÓN DE UN DPA, EL DETALLE DE AQUELLOS BIENES QUE NO SE CONSIDEREN NECESARIOS… CON SU RESPECTIVA NOMENCLATURA ARANCELARIA… SECCIONES, CAPÍTULOS, PARTIDAS O SUBPARTIDAS…" (modification inciso: same 20-días-hábiles MINEC acuerdo / 15-días-hábiles MH opinion / import under suspension / "SI LA RESOLUCIÓN FUERE ACEPTADA, SE RETROTRAERÁ A LA FECHA DEL REGISTRO DE LA RESPECTIVA DECLARACIÓN DE MERCANCÍAS; SI FUERE DENEGADA EN TODO O EN PARTE, EL TITULAR DEBERÁ PAGAR INMEDIATAMENTE…"). Final ¶: "SE EXCEPTÚAN DE LOS BENEFICIOS CONTENIDOS EN LOS LITERALES a), b) Y c)… LA ADQUISICIÓN DE LOS BIENES Y SERVICIOS SIGUIENTES: ALIMENTACIÓN Y BEBIDAS, EXCEPTO AGUA ENVASADA;… SERVICIOS DE HOTELES, EN CUYO CASO, SU INGRESO AL DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO ESTARÁ SUPEDITADO A LA PRESENTACIÓN DE LA DECLARACIÓN DE MERCANCÍAS DEFINITIVAS AL PAGO… O… COMPROBANTES DE CRÉDITO FISCAL O FACTURA DE CONSUMIDOR FINAL… EN LOS CUALES CONSTE QUE SE HA PAGADO EL IMPUESTO CORRESPONDIENTE; SALVO QUE LA ACTIVIDAD BENEFICIADA REQUIERA DE DICHOS BIENES O SERVICIOS… DEBIENDO EL MINISTERIO DE ECONOMÍA CONSIGNARLO EN EL RESPECTIVO ACUERDO QUE OTORGUE AL DPA." Also (Art. 19, DPA facilitation): "PARA LA IMPORTACIÓN DE BIENES QUE GOCEN DE EXENCIÓN… LAS EMPRESAS CALIFICADAS COMO DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO NO NECESITARÁN TRAMITAR PREVIAMENTE LA APROBACIÓN DE LA ORDEN DE PEDIDO, NI LA SOLICITUD Y ORDEN DE FRANQUICIA ADUANERA DE IMPORTACIÓN, POR LO QUE LA OPERACIÓN SE AUTORIZARÁ CON LA SOLA PRESENTACIÓN… DE LA DECLARACIÓN DE MERCANCÍAS RESPECTIVA." | DPA mirror of Art. 17: MINEC incorporates the no-necessary-goods tariff detail (sections/chapters/headings/subheadings) into the DPA acuerdo; same modification procedure (20/15 días hábiles; suspension during processing; acceptance retroacts to the DM registration date; denial in whole or part ⇒ the TITULAR pays immediately); same exception-goods list and paid-tax evidence gate for entry into the DPA, with the same activity-required carve-out recorded in the acuerdo. Exempt DPA imports need no prior orden de pedido or franquicia order: the operation is authorized by the mere presentation of the respective DM | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19 final incisos pp.23-24 (EVID-256; txt PAGE 23-24; SOQ-30 print) |
| LB-010 | Ley de Zonas Francas, Art. 17-B: "LOS TITULARES DE EMPRESAS DEDICADAS A LA FABRICACIÓN DE MICROPROCESADORES; CIRCUITOS INTEGRADOS; PARTES DE VEHÍCULOS TERRESTRES, AÉREOS Y MARÍTIMOS; PIEZAS O EQUIPOS DE COMPUTADORA Y DISPOSITIVOS MÉDICOS; EQUIPOS PARA LA GENERACIÓN DE ENERGÍA, QUE SE INSTALEN EN UNA ZONA FRANCA, TENDRÁN DERECHO A UN PLAZO ADICIONAL DE CINCO AÑOS DE LA EXENCIÓN TOTAL DEL PAGO DEL IMPUESTO SOBRE LA RENTA E IMPUESTOS MUNICIPALES. AQUELLOS TITULARES… CUYA ACTIVIDAD INDUSTRIAL HAYA SIDO DECLARADA COMO ESTRATÉGICA, MEDIANTE ACUERDO EMITIDO POR EL ÓRGANO EJECUTIVO EN EL RAMO DE ECONOMÍA… TENDRÁN DERECHO A UN PLAZO DE DIEZ AÑOS ADICIONAL AL DE LA EXENCIÓN TOTAL…" (evidence gloss: estratégica declaration per Art. 2 b) = ≥US$10,000,000 new investment) | ZF-titular enterprises fabricating microprocessors; integrated circuits; land, air and sea vehicle parts; computer pieces or equipment and medical devices; energy-generation equipment installed in a free zone get FIVE additional years of the TOTAL ISR and municipal-tax exemption; those whose industrial activity is DECLARED STRATEGIC by MINEC acuerdo get TEN additional years (Art. 2 b) gloss: ≥US$10,000,000 new investment) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17-B p.19 (EVID-255; txt PAGE 19; SOQ-30 print) |
| LB-011 | Ley de Zonas Francas, Art. 19-C: "LOS TITULARES DE EMPRESAS DEDICADAS A LA FABRICACIÓN DE MICROPROCESADORES; CIRCUITOS INTEGRADOS; PARTES DE VEHÍCULOS TERRESTRES, AÉREOS Y MARÍTIMOS; PIEZAS O EQUIPOS DE COMPUTADORA Y DISPOSITIVOS MÉDICOS; EQUIPOS PARA LA GENERACIÓN DE ENERGÍA QUE SE INSTALEN EN UN DPA, TENDRÁN DERECHO A UN PLAZO ADICIONAL DE CINCO AÑOS DE LA EXENCIÓN TOTAL DEL PAGO DEL IMPUESTO SOBRE LA RENTA E IMPUESTOS MUNICIPALES. AQUELLOS TITULARES… DECLARADA COMO ESTRATÉGICA… TENDRÁN DERECHO A UN PLAZO DE DIEZ AÑOS ADICIONAL DEL DE LA EXENCIÓN TOTAL…" | DPA mirror of Art. 17-B: same six strategic sectors installed in a DPA get FIVE additional years of total ISR + municipal exemption; declared-strategic (MINEC acuerdo, Art. 2 b) ≥US$10,000,000 kin) get TEN additional years | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19-C p.26 (EVID-255; txt PAGE 26; SOQ-30 print) |
| LB-012 | Ley de Zonas Francas, Art. 20: "LA MAQUINARIA O EQUIPO QUE TENGA MÁS DE CINCO AÑOS DE HABERSE INTRODUCIDO CON FRANQUICIA O CON LIBERACIÓN DE GRAVÁMENES POR LOS BENEFICIARIOS DE LA LEY, PODRÁ SER TRANSFERIDA SIN EL PAGO DE LOS GRAVÁMENES CORRESPONDIENTES. PARA TALES EFECTOS, EL BENEFICIARIO DEBERÁ PRESENTAR A LA ADUANA CORRESPONDIENTE, LA DECLARACIÓN DE MERCANCÍAS DEL RÉGIMEN DE IMPORTACIÓN DEFINITIVA, ANEXANDO LA DECLARACIÓN DE MERCANCÍAS CON QUE LOS BIENES FUERON INTRODUCIDOS INICIALMENTE. DE NO COMPROBARSE LO ANTERIOR, PROCEDERÁ EL PAGO DE DERECHOS E IMPUESTOS EN EL CASO DE INTRODUCIRSE AL TERRITORIO ADUANERO NACIONAL." | Machinery or equipment held MORE THAN FIVE YEARS since its introduction under franchise or release of levies by the law's beneficiaries may be TRANSFERRED WITHOUT PAYMENT of the corresponding levies; for such effects the beneficiary presents to the respective customs office the definitive-import regime DM, annexing the DM with which the goods were INITIALLY introduced; absent such proof, duties and taxes are payable if the goods enter the national customs territory (article sits in the DPA chapter but textually covers "LOS BENEFICIARIOS DE LA LEY") | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 20 p.26 (EVID-256; txt PAGE 26; SOQ-30 print) |
| LB-013 | Ley de Zonas Francas, Art. 25 (final incisos): "AQUELLAS OPERACIONES QUE REALICEN LOS BENEFICIARIOS DE LA PRESENTE LEY, FUERA DE LOS ALCANCES AUTORIZADOS EN EL RESPECTIVO ACUERDO, CAUSARÁN LOS DERECHOS E IMPUESTOS A LA IMPORTACIÓN, EL IMPUESTO SOBRE LA RENTA, LOS IMPUESTOS MUNICIPALES Y EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS. LAS OPERACIONES DE TRANSFERENCIA DE DOMINIO AL TERRITORIO ADUANERO NACIONAL DE BIENES REALIZADAS POR UN COMERCIALIZADOR, CAUSARÁN EL IMPUESTO A LA TRANSFERENCIA… Y NO LES SERÁ APLICABLE LOS INCENTIVOS ESTABLECIDOS EN EL Art. 17 LITERALES d) Y e) Y Art. 19 LITERALES d) Y e)… LOS IMPUESTOS MUNICIPALES SE PAGARÁN EN LA PROPORCIÓN QUE RESULTE DE DIVIDIR SUS VENTAS AL MERCADO LOCAL SOBRE SUS VENTAS TOTALES, EN RELACIÓN A SU ACTIVO." | Operations by beneficiaries OUTSIDE the scope authorized in their respective acuerdo cause import duties and taxes, ISR, municipal taxes and IVA (the out-of-scope guard). Transfers of dominion of goods into the national customs territory by a COMERCIALIZADOR (marketer) cause the transfer tax and the Art. 17 d)/e) and Art. 19 d)/e) incentives DO NOT apply to them; municipal taxes are paid in the proportion resulting from dividing LOCAL-market sales over TOTAL sales, in relation to the company's assets | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 25 final incisos p.30 (EVID-257; txt PAGE 30; SOQ-30 print) |
| LB-014 | Ley de Zonas Francas, Art. 16 (inciso segundo): "EL ACUERDO QUE CONCEDA LA AUTORIZACIÓN AL RÉGIMEN DE UN USUARIO, DEBERÁ CONTENER COMO MÍNIMO: EL NOMBRE DEL TITULAR, LA DETERMINACIÓN DEL ESTABLECIMIENTO EN QUE SE UBICARÁ LA EMPRESA CON SU RESPECTIVA EXTENSIÓN SUPERFICIAL; LA ACTIVIDAD PRODUCTIVA Y EL MERCADO QUE SE AUTORIZA; MONTO DE INVERSIÓN INICIAL EN ACTIVOS FIJOS Y PLAZO PARA CUMPLIRLO Y/O NÚMERO DE PUESTOS DE TRABAJO PERMANENTES CON LOS QUE OPERARÁ; EN SU CASO, LA CALIFICACIÓN DE ACTIVIDAD INDUSTRIAL ESTRATÉGICA; LOS DERECHOS Y OBLIGACIONES QUE SE LE CONCEDEN…" (the DPA acuerdo mirrors this per Art. 18 final: "EL ACUERDO… DEBERÁ COMPRENDER, EN LO APLICABLE, LOS REQUISITOS DETERMINADOS EN EL ARTÍCULO 16, INCISO SEGUNDO") | The usuario authorization acuerdo must contain at minimum: holder name; the establishment and its surface extension; the PRODUCTIVE ACTIVITY AND MARKET authorized; initial fixed-asset investment amount and term and/or permanent-job count; where applicable the STRATEGIC industrial-activity qualification; and the rights and obligations granted — the acuerdo-recorded fields this file's rows and extension flags resolve against (DPA acuerdos mirror Art. 16 per Art. 18 final) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 16 p.14 + Art. 18 final p.21 (EVID-254; txt PAGE 14, 21; SOQ-30 print) |
| LB-015 | Ley ISR (consolidated), Art. 72 (pointer depth — full LB owned by `taxation/05_isr-distributions.md` LB-001): domiciled subjects that pay or credit *utilidades* to their socios/accionistas/… shall retain FIVE PERCENT (5%), definitive, whether the recipient is domiciled or not | The Art. 72 5% definitive dividend retention — the taxation-side counterpart the 12-ejercicio exemption window suppresses (expressly, per the 12_ socio-level exemption) and the 13th-ejercicio crossing re-activates; consumed by id from `taxation/05` (SV-TAX-FR-132/144/145/146), never re-derived here | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 72 p.45 (EVID-103; via taxation/05 LB-001) |
| LB-016 | Guía de Orientación Quincena Veinticinco (67_), Anexo 7: ZF/DPA/LSI checkbox "Marque si es usuario de Zona Franca, DPA o Usuario regulado en la Ley de Servicios Internacionales" (Renta-2026 screen); Anexo 8: "Versión 20 — Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial… modifica nombre en el formulario… la que tendrá como anexo el Certificado de Crédito Tributario" (pointer LB: computation/issuance authority = `taxation/01_isr-framework.md` SV-TAX-FR-174, whose LB-033/035 carry 66_ Art. 6 + 67_ in full — never restated here) | The special-regime declaration surface pointers: the renta-en-línea ZF/DPA/LSI checkbox routes certificado seekers, and F-11 v20 is the special-regime-subject ISR declaration carrying the Certificado de Crédito Tributario as anexo (print not yet acquired — pointer only, zero mechanics invented here) | `sv/sources/67_Guia_Orientacion_Quincena25.pdf` | Anexos 7/8 pp.2-13 (EVID-238; via taxation/01 LB-035) |
| LB-017 | Ley de Servicios Internacionales, Art. 14 (kin authority, explicit text; the ZF-side 12_ print is corpus-silent on the point): the desarrollista ISR exemption "NO LIBERA… DE LA OBLIGACIÓN DE PRESENTAR LA RESPECTIVA DECLARACIÓN TRIBUTARIA EN CADA EJERCICIO" | The special-regime exemption does NOT release the beneficiary from the obligation to present the respective tax declaration in each ejercicio (LSI twin text; applied here as the declaration-duty-survives-exemption guard for ZF/DPA rows, with the F-11 v20 surface as pointer) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 14 (EVID-259..262 range pp.8-15; kin — SOQ-30 print) |

## 3. Functional Requirements

### 3.1 The exemption-row chassis — D15 spine (12_ Arts. 16/17/19/25)

- **SV-SPE-FR-023:** The system shall model every ZF/DPA tax benefit as a
  per-beneficiary dated exemption row on
  `l10n_sv_special_regime.exemption_row`, keyed by the Task-1 profile
  (regime · role · activity admission · location track metro/fuera ·
  *acuerdo* D.O. date — SV-SPE-FR-003/FR-022 consumed by id), each row
  carrying tax kind (isr · municipal · itbir), benefit level (total ·
  partial), the printed percentage, `valid_from`/`valid_to` (null
  `valid_to` = indefinite tail), its anchor kind (acuerdo D.O. date ·
  operations-start ejercicio · statutory date) and instrument provenance —
  never a global constant; the resolution anchor for percentages is the
  FISCAL YEAR and the resolved percentage is snapshotted on the year's
  determination; the benefit-state field (SV-SPE-FR-015) gates resolution —
  *suspendida* yields a 0% effective percentage for the suspension span
  while the ladder dates remain UNCHANGED (the suspension period does not
  interrupt the total-benefit term, SV-SPE-FR-016), *revocada* /
  *perdida_inactividad* end the row set — and the out-of-scope guard
  applies: operations outside the scope authorized in the respective
  acuerdo cause import duties, ISR, municipal taxes and IVA (per-operation
  exclusion flag on the row set).
  (LB-014; LB-001; LB-013; EVID-254/257)
- **SV-SPE-FR-024:** The system shall generate, for a ZF *usuario*, the ISR
  ladder rows as printed — metro: 100% for 15 years from the acuerdo D.O.
  date, then 60% OF THE RATE for the 10 following years, then 40% for the
  10 years after; fuera: 100% for 20 years, then 60% for the 15 following
  years, then 40% for the 10 years after — one row per contiguous window
  (valid_from/valid_to per fiscal-year boundary), values as printed with
  12_ provenance.
  (LB-001; EVID-254)
- **SV-SPE-FR-025:** The system shall generate, for a ZF *usuario*, the
  municipal-tax ladder rows as printed — metro: 100% for 15 years, then 90%
  for the 10 following years, then 75% INDEFINITE (`valid_to` null, ending
  only on benefit-state end or regime exit); fuera: 100% for 20 years, then
  90% for the 15 following years, then 75% indefinite — and shall expose
  the municipal-council ADDITIONAL-benefits surface as empty config slots
  with NO defaults (discretionary per concejo; OQ-6).
  (LB-002; EVID-254)
- **SV-SPE-FR-026:** The system shall implement the usuario
  investment-increase extension as an extension event that lengthens the
  total-exemption windows by 5 years when, during the LAST five years of
  the total-exemption term, the beneficiary increased its investment by
  100% relative to its INITIAL investment, the increase realized in land
  purchase, building construction and machinery/equipment acquisition
  LINKED to the authorized activity (predicate fields on the event; proof
  reference; row-set regeneration from the event's effective date).
  (LB-002 final inciso; EVID-254)
- **SV-SPE-FR-027:** The system shall generate, for a DPA titular, the ISR
  ladder rows as printed — metro: 100% for 10 years from the acuerdo D.O.
  date, then 60% OF THE RATE for the 5 following years, then 40% for the 10
  years after; fuera: 100% for 15 years, then 60% for the 10 following
  years, then 40% for the 10 years after — the 10/15y DPA tracks are
  DISTINCT from the usuario 15/20y tracks (regime-distinctness invariant:
  never unified, metro/fuera selected via SV-SPE-FR-022 by id).
  (LB-007; EVID-256)
- **SV-SPE-FR-028:** The system shall generate, for a DPA titular, the
  municipal-tax ladder rows as printed — metro: 100% for 10 years, then 90%
  for the 5 following years, then 75% INDEFINITE; fuera: 100% for 15 years,
  then 90% for the 10 following years, then 75% indefinite — with the same
  additional-municipal-benefit config slots as FR-025 (no defaults).
  (LB-008; EVID-256)

### 3.2 Desarrollista / administrador tracks (12_ Arts. 11/13; 54-C)

- **SV-SPE-FR-029:** The system shall generate, for a ZF *desarrollista*,
  the FLAT benefit rows — ISR total exemption 10 years (metro) / 15 years
  (fuera) counted from the EJERCICIO IN WHICH OPERATIONS FOR THE FREE-ZONE
  ACTIVITY START (a distinct anchor from the usuario/DPA D.O.-date ladder:
  preserve both), municipal total exemption on the same operations-start
  anchor, and total ITBIR exemption on acquisitions of real estate to be
  used in the incentivated activity — no phase-down tail follows these
  tracks.
  (LB-005; EVID-253)
- **SV-SPE-FR-030:** The system shall implement the
  desarrollista/administrador AMPLIATION extension (+5 years on ISR and
  municipal rows) as an extension event whose predicate requires an
  ampliation of the zona franca invested DURING the total-exemption period
  with: the entire ampliation surface within a 5-kilometer radius of the
  previously authorized area's boundary; minimum surface of 8 manzanas; and
  compliance with Art. 10's minimum-infrastructure requirements — available
  to desarrollistas (Art. 11 final) and to 54-C grandfathered
  desarrollistas/administradores (54-C final paragraph).
  (LB-005 final; LB-006; EVID-253)
- **SV-SPE-FR-031:** The system shall implement the 54-C grandfathering as
  dated rows for pre-2013 desarrollistas AND administradores: total
  exemptions continue until 31-December-2015 OR the expiry of the
  respective acuerdo's term if later (per-beneficiary statutory end date);
  after that term both roles — and their socios/accionistas for distributed
  utilidades/dividends — get 5 ADDITIONAL years under the same conditions
  and scope of Art. 11 a)/b); a beneficiary holding BOTH roles gets BOTH
  benefit sets; and the system shall NOT ship any NEW-administrador benefit
  rows — the former administrador benefit articles (Arts. 14/15) are
  DEROGATED in the current print, so post-2013 administrador profiles carry
  duty-only rows (OQ-4).
  (LB-006; EVID-253)

### 3.3 Strategic-sector extensions (12_ Arts. 17-B/19-C)

- **SV-SPE-FR-032:** The system shall implement the Art. 17-B ZF extension
  flags as extension events lengthening the TOTAL ISR and municipal windows:
  +5 years for titular enterprises of the six strategic sectors installed in
  a zona franca (microprocessors; integrated circuits; land/air/sea vehicle
  parts; computer pieces or equipment and medical devices; energy-generation
  equipment — sector list as printed, a dated config row); +10 years when
  the industrial activity is DECLARED STRATEGIC by MINEC acuerdo (Art. 2 b)
  gloss: ≥US$10,000,000 new investment — value from the evidence gloss,
  cited as such).
  (LB-010; EVID-255)
- **SV-SPE-FR-033:** The system shall implement the Art. 19-C DPA extension
  flags with the same two tiers as FR-032 (+5 years for the six strategic
  sectors installed in a DPA; +10 years when declared strategic), as
  extension events on the DPA row set — DPA and usuario extension events
  are recorded on their own row sets and never cross-applied.
  (LB-011; EVID-255)

### 3.4 Percentage-of-rate computation — actividad autorizada only (12_ Arts. 17 d)/19 d))

- **SV-SPE-FR-034:** The system shall apply the exemption percentage ONLY
  to income from the *actividad autorizada* — the exemption rows carry
  "SOBRE LA ACTIVIDAD AUTORIZADA" semantics with the partial percentages
  being percentages OF THE ISR RATE (un sesenta por ciento DE LA TASA) —
  requiring segregated accounting between the benefited activity and local
  activity: the activity classification and mixed-cost apportionment
  machinery is CONSUMED BY ID from `taxation/02_isr-deductions.md`
  (SV-TAX-FR-035/036 — gravadas/no-gravadas activity link and allocator;
  Reglamento ISR Art. 32 gravada/no-gravable kin noted through that file's
  OQ-001), never re-derived here; the resolution anchor is the fiscal year
  and the resolved percentage + segregated bases are snapshotted on the
  year's determination.
  (LB-001; LB-007; EVID-254/256)

### 3.5 Dividend window (12_ Arts. 11/17 d)/19 d); Ley ISR Art. 72)

- **SV-SPE-FR-035:** The system shall compute, per benefited society, the
  dividend window from the D.O. PUBLICATION of the qualification acuerdo
  (its own anchor, independent of the desarrollista operations-start
  ladder anchor): during the FIRST 12 fiscal ejercicios, utilidades or
  dividends from the favored activity are EXEMPT both at the society and at
  the socio level — which EXPRESSLY SUPPRESSES the Ley ISR Art. 72 5%
  retention during the window (the exemption-suppresses-retention
  implication per the EVID-253 doubt resolution, encoded through the
  express-exemption carve-out of SV-TAX-FR-146 and the suppression of
  SV-TAX-FR-132, both consumed by id from `taxation/05_isr-distributions.md`;
  OQ-1 records the explicitness note); from the 13TH ejercicio onward,
  distributions from the favored activity are TAXED and the SV-TAX-FR-132
  5% retention fires with the SV-TAX-FR-144/145 earnings-register and
  pool bookkeeping applied by id; and the PJ-socios exclusivity rule shall
  be enforced per socio: where one or more socios are personas jurídicas,
  the exemption right is EXCLUSIVE of those socios and may NOT be
  transferred successively to their own socios (per-socio eligibility flag
  on the window).
  (LB-001; LB-005; LB-007; LB-015; EVID-253/254/256)

### 3.6 Exception goods — the inverting gate (12_ Arts. 17/19 final)

- **SV-SPE-FR-036:** The system shall implement the exception-goods config
  (identical list for ZF Art. 17 final and DPA Art. 19 final) with its
  INVERTING gate: the eight categories as printed — food and beverages
  except bottled water; tobacco-containing products; alcoholic beverages;
  housing rental; home furniture and furnishings; sumptuary or luxury
  articles; vehicles for individual/collective person transport and goods;
  hotel services — are EXCLUDED from the libre-internación benefits, and
  their admission into the zona franca or DPA is conditioned on evidence of
  PAID tax: a *declaración de mercancías definitiva a pago*
  (definitive-payment DM) for foreign goods, or a *comprobante de crédito
  fiscal* (CCF) or *factura de consumidor final* (FCF) for local purchases
  evidencing the tax paid — the evidence documents being the e-invoicing
  doc types consumed by id (SV-EINV-FR-001: 03 CCFE / 01 FE) and the DM
  record surface owned by `06_customs-declarations.md` — UNLESS the
  benefited activity requires those goods or services for the
  production/assembly/maquila/manufacture/processing/transformation/
  commercialization chain AND the requirement is recorded in the respective
  *acuerdo* (per-acuerdo activity-required flag consumed from the Art. 16
  acuerdo record of FR-023); an admission without the paid-tax evidence and
  without the acuerdo flag is BLOCKED with a pending-evidence state.
  (LB-004; LB-009; EVID-254/256)

### 3.7 Capital-goods 5-year free transfer (12_ Art. 20)

- **SV-SPE-FR-037:** The system shall track, per capital asset introduced
  under franquicia or liberation of levies, the asset-level
  franquicia-entry date (DGA introduction date, D15 anchor) and a computed
  transfer-eligibility flag that turns true after MORE than five years
  since entry; a transfer without payment of the gravámenes shall require,
  and record, the presentation to customs of the DM of the definitive-
  import regime TOGETHER WITH the ORIGINAL DM under which the goods were
  initially introduced (annex requirement — both references stored on the
  transfer record); absent that proof, the system marks duties and taxes
  payable on the goods' entry into the national customs territory (scope
  note: the article sits in the DPA chapter but textually covers the law's
  beneficiaries).
  (LB-012; EVID-256)

### 3.8 No-necessary-goods tariff detail + modification procedure (12_ Arts. 17/19)

- **SV-SPE-FR-038:** The system shall carry the no-necessary-goods tariff
  detail as dated config rows per *acuerdo* (both ZF and DPA), each row at
  the nomenclature granularity printed — secciones · capítulos · partidas ·
  subpartidas, particular or general — and shall implement the modification
  procedure as a state machine: request expressing its cause; MINEC acuerdo
  due within 20 *días hábiles* with the MH opinion due within 15 *días
  hábiles* (días-hábiles arithmetic consumed from SV-FREP-FR-202..204 by
  id); while the request processes, the requested goods import UNDER
  SUSPENSION of duties and taxes; on ACCEPTANCE the resolution RETROACTS
  (retrotrae) to the registration date of the respective DM (retro-date
  stamped on the row); on DENIAL in whole or part, an IMMEDIATE-payment
  obligation is flagged for the denied goods' duties and taxes; the DGA's
  mechanized teledespacho application of the detail is an informational
  note only (transmission surface owned by `06_customs-declarations.md`).
  (LB-003; LB-009; EVID-254/256)

### 3.9 Quincena-25 certificado consumption + declaration guard (SV-TAX-FR-174 by id; 14_ Art. 14 kin)

- **SV-SPE-FR-039:** The system shall record the FY-2026 Quincena-25
  certificado entitlement for ZF/DPA companies ONLY through the route of
  SV-TAX-FR-174 (`certificado_zf_dpa_lsi` on `l10n_sv.isr.quincena.credit`)
  consumed by id — this file contributes ONLY the regime-profile link (a
  company whose regime profile is zona franca/DPA — or LSI per
  `03_lsi-regime.md` — selects that route when the credit exceeds its
  FY-2026 ISR); NO credit computation, remanent logic, issuance or
  negotiability semantics is restated here (all owned by SV-TAX-FR-174);
  the entitlement surfaces on the special-regime declaration as pointer
  only (LB-016; F-11 v20 — OQ-2).
  (LB-016; EVID-238 via taxation/01 LB-035; cross-ref SV-TAX-FR-174)
- **SV-SPE-FR-040:** The system shall enforce the
  declaration-duty-survives-exemption guard: active exemption rows NEVER
  suppress or satisfy ISR filing duties — the beneficiary remains obliged
  to present the respective tax declaration in each ejercicio (LSI Art. 14
  explicit kin; the ZF-side 12_ print is corpus-silent, the guard is
  anchored on the twin text and on the F-11 v20 special-regime declaration
  whose existence the Quincena-25 surfaces evidence); no F-11 v20 layout
  mechanics are invented here (print not acquired — pointer OQ-2,
  SAS-statute discipline).
  (LB-017; LB-016; EVID-262/238)

### 3.10 Comercializador incentive exclusion + municipal proration (12_ Art. 25 final)

- **SV-SPE-FR-041:** The system shall apply, to transfers of dominion of
  goods into the national customs territory (TAN) by a *comercializador*,
  the incentive-exclusion and proration rules: those operations CAUSE the
  transfer tax and the Art. 17 d)/e) and Art. 19 d)/e) incentives are
  INAPPLICABLE to them (per-operation ISR/municipal exclusion flag —
  TAN-sale income never enters the exemption-row computation), and
  municipal taxes are paid in the PROPORTION local-market sales ÷ total
  sales in relation to the company's assets (proration ratio computed per
  ejercicio from the sales and asset ledgers, stored as a dated computed
  row); the transfer-tax routing, duty base and market-price machinery of
  TAN sales are owned by `05_tan-iva-interface.md` (by id, not restated).
  (LB-013; EVID-257)

## 4. Data Model

Layer semantics: all entities are Odoo-native config/ledger rows on the
Task-1 regime profile — every entity lives in the client (wave default
`odoo`; see §5). Percentages, year-counts and windows are code-text values
as printed (SOQ-30 watch), stored as dated rows with instrument provenance,
never constants. CSV sidecar evaluated per plan: the ladder SEEDS are few
(usuario/DPA/desarrollista metro/fuera shapes ≈ 10 template rows, extension
predicates 6) — §4 config rows suffice and NO sidecar ships (default none;
judgment noted in the task report).

**Exemption rows (l10n_sv_special_regime.exemption_row):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.exemption_row | profile · tax_kind | m2o · select | T1 profile key (SV-SPE-FR-003) ; isr · municipal · itbir | FR-023..031 |
| l10n_sv_special_regime.exemption_row | benefit_level · percentage | select · percent | total (100) · partial (60 · 40 · 90 · 75) — values as printed | FR-024/025/027/028 |
| l10n_sv_special_regime.exemption_row | valid_from · valid_to | date · date-null | fiscal-year-aligned windows; valid_to null = indefinite tail (75% municipal; ends on benefit-state end/regime exit) | FR-023..028 |
| l10n_sv_special_regime.exemption_row | anchor_kind · anchor_date | select · date | acuerdo_do_date · operations_start_ejercicio (desarrollista) · statutory_date (54-C end 2015-12-31/acuerdo expiry) | FR-023, FR-029, FR-031 |
| l10n_sv_special_regime.exemption_row | extension_flag | select | none · ampliation_5y · investment_increase_5y · strategic_sector_5y · estrategica_10y · grandfather_54c_5y | FR-026, FR-030..033 |
| l10n_sv_special_regime.exemption_row | suspension_effect | computed | suspendida span ⇒ effective_percentage = 0, dates unchanged (clock keeps running — SV-SPE-FR-015/016 by id) | FR-023 |
| l10n_sv_special_regime.exemption_row | resolved_percentage · resolved_fiscal_year · snapshot_on | percent · year · datetime | snapshot-on-write at the year's determination (D15/D16) | FR-023, FR-034 |
| l10n_sv_special_regime.exemption_row | provenance | char | 12_ article as printed (SOQ-30) | FR-023..033 |

**Extension events (l10n_sv_special_regime.extension_event):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.extension_event | kind | select | ampliation_5y (≥8 manzanas · 5-km radius · Art. 10 infrastructure) · investment_increase_5y (100% over initial, last 5 total-exemption years, land/buildings/machinery) · strategic_sector_5y (six-sector list) · estrategica_10y (MINEC declaration; Art. 2 b) ≥US$10,000,000 gloss) · grandfather_54c_5y | FR-026, FR-030..033 |
| l10n_sv_special_regime.extension_event | predicate_values · proof_ref | config · char | sector list row · manzanas/radius/infrastructure flags · investment base+increase measurement (bookings against T1 requisito log) · acuerdo refs | FR-026, FR-030..032 |
| l10n_sv_special_regime.extension_event | effective_date · added_years · regenerates | date · int · boolean | row-set regeneration flag (windows recomputed from the extension) | FR-026, FR-030..033 |

**Dividend window (l10n_sv_special_regime.dividend_window):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.dividend_window | sociedad · window_anchor | m2o · date | D.O. publication of the qualification acuerdo (own anchor, distinct from desarrollista operations-start) | FR-035 |
| l10n_sv_special_regime.dividend_window | exempt_ejercicios · taxed_from | int · year | 12 ejercicios exempt; 13th onward taxed (Ley ISR Art. 72 5% via SV-TAX-FR-132 by id) | FR-035 |
| l10n_sv_special_regime.dividend_window.socio | socio · pj_exclusive · eligible | m2o · boolean | PJ-socio exclusivity: right exclusive of the PJ socio, NOT successively transferable to its own socios | FR-035 |
| l10n_sv_special_regime.dividend_window | retention_suppression | computed | window-open ⇒ SV-TAX-FR-132 suppression flag consumed by taxation/05 (SV-TAX-FR-146 express carve-out) | FR-035 |

**Exception goods (l10n_sv_special_regime.exception_good):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.exception_good | category | select | alimentacion_bebidas (excepto agua envasada) · tabaco · bebidas_alcoholicas · arrendamiento_vivienda · muebles_enseres_hogar · suntuarios_lujo · vehiculos · servicios_hoteles | FR-036 |
| l10n_sv_special_regime.exception_good | activity_required | boolean | per-acuerdo flag (MINEC-recorded requirement for the benefited activity) | FR-036 |
| l10n_sv_special_regime.exception_good | evidence_kind · evidence_ref | select · m2o/char | dm_definitiva_a_pago (DM ref — 06 by id) · ccf/fcf paid-tax document (SV-EINV-FR-001 doc types by id) | FR-036 |
| l10n_sv_special_regime.exception_good | admission_state | select | pending_evidence · admitted · blocked | FR-036 |

**Tariff detail + modification (l10n_sv_special_regime.tariff_detail):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.tariff_detail | acuerdo · level · code | m2o · select · char | seccion · capitulo · partida · subpartida (particular or general, as printed) | FR-038 |
| l10n_sv_special_regime.tariff_detail | modification_state | select | none · requested (import under suspension) · accepted (retro_date = DM registration date) · denied (pay_immediately flag, total/partial) | FR-038 |
| l10n_sv_special_regime.tariff_detail | clocks | date fields | MINEC acuerdo ≤20 días hábiles · MH opinion ≤15 días hábiles (SV-FREP-FR-202..204 by id) | FR-038 |

**Capital-asset franquicia flags (account.asset extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset | sv_spe_franquicia_entry_date · sv_spe_transfer_eligible | date · computed | >5 years since entry ⇒ eligible | FR-037 |
| account.asset | sv_spe_transfer_dm_refs | char×2 | DM importación definitiva + ORIGINAL entry DM (annex requirement) | FR-037 |

**Municipal proration (l10n_sv_special_regime.municipal_proration):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.municipal_proration | fiscal_year · local_sales · total_sales · activo | year · monetary | ratio = local sales ÷ total sales in relation to activo, per Art. 25 final | FR-041 |
| l10n_sv_special_regime.municipal_proration | ratio · provenance | computed · char | dated computed row per ejercicio (comercializadores; TAN-sale income excluded from incentive rows) | FR-041 |

## 5. Odoo Mapping

Layer semantics for this wave: the exemption schedules are Odoo-native
dated config/ledger rows (no DTE generation or transmission is introduced —
the exception-goods gate READS e-invoicing documents as evidence, it does
not generate them) — every FR maps `odoo`; no SaaS rows (no
architecture-split surface per `shared/docs/saas-thin-client-architecture.md`
D2). Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-023 | odoo | l10n_sv_special_regime.exemption_row | all | THE D15 spine row; key = T1 profile (FR-003/022 by id); anchor = fiscal year; suspension ⇒ 0% effective, dates unchanged (FR-015/016 by id); out-of-scope guard per Art. 25 |
| FR-024 | odoo | l10n_sv_special_regime.exemption_row | tax_kind isr, usuario template | 100% 15/20y → 60% 10/15y → 40% 10y as printed; valid_from = acuerdo D.O. date |
| FR-025 | odoo | l10n_sv_special_regime.exemption_row | tax_kind municipal, usuario template | 100% → 90% 10/15y → 75% null valid_to (indefinite tail); concejo additional-benefit slots = NO defaults (OQ-6) |
| FR-026 | odoo | l10n_sv_special_regime.extension_event | kind investment_increase_5y | +5y on total windows; predicate = 100% over initial investment in last 5 total-exemption years (land/buildings/machinery, activity-linked) |
| FR-027 | odoo | l10n_sv_special_regime.exemption_row | tax_kind isr, DPA template | 100% 10/15y → 60% 5/10y → 40% 10y; usuario 15/20y vs DPA 10/15y never unified |
| FR-028 | odoo | l10n_sv_special_regime.exemption_row | tax_kind municipal, DPA template | 100% 10/15y → 90% 5/10y → 75% indefinite tail |
| FR-029 | odoo | l10n_sv_special_regime.exemption_row | desarrollista flat rows | ISR+municipal anchor = OPERATIONS-START ejercicio (≠ usuario/DPA D.O. anchor); ITBIR row on real-estate acquisitions |
| FR-030 | odoo | l10n_sv_special_regime.extension_event | kind ampliation_5y | ≥8 manzanas · 5-km radius · Art. 10 infrastructure; desarrollista + 54-C rows |
| FR-031 | odoo | l10n_sv_special_regime.exemption_row | grandfather_54c rows | end = 2015-12-31 or later acuerdo expiry; +5y under Art. 11 a)/b) scope; both-roles ⇒ both sets; NO new-administrador rows (Arts. 14/15 derogated — OQ-4) |
| FR-032 | odoo | l10n_sv_special_regime.extension_event | kinds strategic_sector_5y / estrategica_10y (ZF) | six-sector list as printed; ≥US$10M = Art. 2 b) evidence-gloss value |
| FR-033 | odoo | l10n_sv_special_regime.extension_event | kinds strategic_sector_5y / estrategica_10y (DPA) | 19-C mirror; events never cross-applied between row sets |
| FR-034 | odoo | exemption_row + account.move.line | resolved_percentage + activity link | actividad-autorizada-only semantics; segregation via SV-TAX-FR-035/036 by id (Reglamento Art. 32 kin through 02's OQ-001); snapshot at year determination |
| FR-035 | odoo | l10n_sv_special_regime.dividend_window(+.socio) | window_anchor/exempt 12/13th/PJ flag | suppression of SV-TAX-FR-132 during window via SV-TAX-FR-146 carve-out — all by id; OQ-1 explicitness note |
| FR-036 | odoo | l10n_sv_special_regime.exception_good | category/activity_required/evidence | inverting gate: DM-a-pago or CCF/FCF paid-tax evidence (SV-EINV-FR-001 by id) unless acuerdo-flagged; ZF+DPA same list |
| FR-037 | odoo | account.asset | sv_spe_franquicia_entry_date/transfer_eligible/DM refs | >5-year rule; DM definitiva + ORIGINAL DM annex; else duties payable on TAN entry |
| FR-038 | odoo | l10n_sv_special_regime.tariff_detail | level/code/modification_state/clocks | secciones/capítulos/partidas/subpartidas per acuerdo; 20/15 días hábiles via SV-FREP-FR-202..204 by id; retrotraer to DM registration; denial ⇒ immediate payment |
| FR-039 | odoo | l10n_sv.isr.quincena.credit (link) | route certificado_zf_dpa_lsi | SV-TAX-FR-174 by id — NOTHING restated; this file only supplies the regime-profile discriminator |
| FR-040 | odoo | l10n_sv.isr.filing.duty (guard flag) | exemption-active never clears duty | LSI Art. 14 kin; F-11 v20 pointer only (OQ-2 — no layout mechanics invented) |
| FR-041 | odoo | l10n_sv_special_regime.municipal_proration | ratio fields | comercializador TAN sales: incentives inapplicable (exclusion flag) + local/total-over-activo proration; TAN routing owned by 05 by id |

Version-regime notes (D12/D15/D16/D18/D19): all ladders, percentages,
year-counts, extension predicates and windows are code-text values cited as
printed under the SOQ-30 watch (§2) and live as dated rows keyed by the
per-beneficiary anchor (acuerdo D.O. date; desarrollista operations-start
ejercicio; 54-C statutory end); percentages resolve as-of the fiscal year
with snapshot-on-write. Mid-year go-live (D18): a migrating ZF/DPA company
ingests its ladder computation as `is_historical` rows with
original-period semantics (tiered ingestion; no re-derivation) — the
suspension-clock invariant (dates unchanged) is preserved on imported
rows. No hard gates beyond the statutory state machine (D16 no-override:
regime validity is never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a metro ZF usuario with acuerdo D.O. date 2020-03-02,
  when its exemption rows are generated, then the ISR ladder resolves to
  100% (ejercicios 2020-2034), 60% of the rate (2035-2044) and 40%
  (2045-2054), each window a dated row snapshotted at the year's
  determination (FR-024, FR-023).
- **AC-002:** Given the same usuario distributing favored-activity
  utilidades in ejercicio 2032 (the 13th from the 2020 D.O. publication),
  when the distribution is recorded, then the SV-TAX-FR-132 5% retention
  fires with the SV-TAX-FR-144/145 register/pool semantics applied by id —
  while the same distribution in 2031 (12th ejercicio) carries the
  express suppression and no retention (FR-035).
- **AC-003:** Given a ZF usuario whose acuerdo does NOT record an
  activity-required flag for alcoholic beverages, when a local purchase of
  beverages arrives with an FCF showing no paid tax, then the
  exception-goods admission is blocked in pending_evidence (no
  libre-internación benefit applied) until DM-a-pago or paid-tax CCF/FCF
  evidence is attached (FR-036).
- **AC-004:** Given a ZF company with a FY-2026 Quincena-25 credit
  exceeding its ISR, when the credit route resolves, then the entitlement
  is recorded ONLY via the SV-TAX-FR-174 route `certificado_zf_dpa_lsi`
  and no certificado computation is re-derived in this file (FR-039).
- **AC-005:** Given a usuario under suspensión (jobs requisito breach) for
  a span inside its 100% window, when the span is stamped, then the
  effective percentage is 0 for the suspension span with the ladder dates
  UNCHANGED (the clock keeps running) and the rows resume their printed
  percentages after cure (FR-023; SV-SPE-FR-015/016 by id).
- **AC-006:** Given a fuera DPA titular with acuerdo D.O. date 2018-07-15,
  when its rows are generated, then the ISR ladder is 100% (2018-2032),
  60% (2033-2042), 40% (2043-2052) and the municipal ladder 100% → 90% →
  75% indefinite — never the usuario 15/20y shapes (FR-027, FR-028).
- **AC-007:** Given a metro usuario in the microprocessor sector whose
  17-B extension event is recorded, when the row set regenerates, then the
  total ISR and municipal windows lengthen by 5 years from the extension's
  effective date (FR-032).
- **AC-008:** Given a DPA machinery asset with franquicia-entry date
  2019-05-10 transferred on 2026-02-01 with the DM importación definitiva
  and the original entry DM annexed, then the transfer records as
  gravámenes-free (entry >5 years); the same transfer without the original
  DM is flagged duties-payable on TAN entry (FR-037).
- **AC-009:** Given a comercializador with ejercicio sales local
  US$300,000 / total US$1,200,000, when the municipal proration computes,
  then the Art. 25-final ratio row (0.25 against the activo relation) is
  stored and the TAN-sale income is excluded from the Art. 17 d)/e)
  incentive computation (FR-041).
- **AC-010:** Given a usuario with both favored-activity income and local
  activity income in a 60% window, when the year's determination closes,
  then the 60%-of-rate exemption snapshot applies ONLY to the
  actividad-autorizada base, the local-activity income remaining fully
  taxed (segregation consumed from SV-TAX-FR-035/036 by id) (FR-034).
- **AC-011:** Given a no-necessary-goods modification request for a
  subpartida still processing at import time, when the goods import under
  suspension and the resolution is DENIED in part, then an
  immediate-payment obligation is flagged for the denied goods' duties and
  taxes, while an accepted resolution stamps the retro date of the DM
  registration on the row (FR-038).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | Dividend-interaction explicitness (EVID-253 doubt resolution, encoded): the 12-ejercicio exemption EXPRESSLY suppresses the Ley ISR Art. 72 5% retention on favored-activity distributions — the 12_ text exempts sociedad AND socios individually, satisfying SV-TAX-FR-146's express-carve-out; the corpus never states "no retención" verbatim for ZF. Encoded as suppression-by-express-exemption; fiscalización criteria review watch. | no | Takumi S7 (fiscalización watch) | open |
| OQ-2 | F-11 v20 acquisition watch: "Versión 20 — Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial" + Certificado anexo (67_ Anexo 8) — print NOT acquired; FR-039/FR-040 carry pointer-only surfaces with zero invented mechanics (kin of taxation/01 OQ-007 and payroll/08 OQ-004; acquisition candidate ≥71). | no | Takumi S7 (sources watch) | open |
| OQ-3 | SOQ-30 carried: the 12_ consolidation ends at D.L. 318-2013 — post-cutoff reforms unverified until official routes recover; every LB in this file cites as printed; a post-2013 reform may move ladders, percentages, extension tiers or the 54-C grandfathering — re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-4 | Administrador benefit authority: the pre-2013 administrador benefit articles (12_ Arts. 14/15) read DEROGADO (D.L. 318-2013) — the current print grants administrador ISR/municipal benefits ONLY through the 54-C grandfathering; FR-031 ships no new-administrador rows. Whether a post-2013 reform restored a general administrador benefit is unverified (SOQ-30 kin). | no | Takumi S7 (sources watch) | open |
| OQ-5 | Transitoria scope decision: this file encodes 54-C (per task scope); the sibling transitorias 54-D/54-E (pre-existing usuarios/DPA qualifying via jobs/investment proof, taking the Art. 17 numeral-2 shapes) and 54-F (hard stop of benefits at 31-dic-2015 for non-qualifiers) are recorded at evidence depth only — historical beneficiaries are ingested per D18 as `is_historical` rows with their original-period shapes; encode as FRs only if a migrating pre-2013 beneficiary requires them. | no | Takumi S7 (config watch) | open |
| OQ-6 | Concejos-municipales additional benefits (Arts. 11/17/19 final paragraphs): municipal councils MAY grant benefits beyond the law's — discretionary, instrument-less in corpus; FR-025/FR-028 expose empty config slots with NO defaults; a granted benefit lands as new dated rows with municipal-instrument provenance. | no | Takumi S7 (config watch) | open |
