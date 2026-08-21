# HN — Fiscal reporting — Selectivo declarations: códigos 203/211/210/205/204/259 + the IPC value chain

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file owns the DECLARATION surfaces of master-index cluster F9 — the six
monthly SAR OVI *declaraciones juradas* (sworn declarations) of the
selective-consumption family: **código 203** general *Impuesto Selectivo al
Consumo* (D. 58-1982 — a separate 1982 statute), **211** cigarettes, **210**
*aguas gaseosas* (soft drinks), **205** *alcoholes y licores nacionales*
(domestic alcohols and liquors) and **204** *cerveza* (beer — the last four
being D. 17-2010 *impuesto de producción y consumo* declarations), and **259**
the *Tasa por Servicios Turísticos* (tourist-services rate, D. 131-98 Art. 43
— a 4% retention, grouped here only by SAR's shared OVI form chassis). It also
owns the **current-value home** for the selectivo IPC-adjustment *Acuerdos*
172-2022 → 014-2023 → 218-2024 (sources `98_/99_/100_`, cited DIRECT — no
evidence pass exists for them; page-1-verified by this synthesis on
2026-08-20): the dated per-millar/per-liter rows that
`taxation/05_d17-2010-family.md` deliberately stores only as placeholder
slots (its OQ-004 names this file the values' home). Values are recorded AS
PRINTED, never re-derived (R-H10-kin discipline).

It does **not** cover: selectivo law-side bases, 2010 base tables, the IPC
mechanism-as-law and the vehicle/slots/DUA-seal families —
`taxation/05_d17-2010-family.md` BY ID (HN-TAX-FR-188..207); the OVI/SW
filing chassis and declaration lifecycle (login→borrador→juramento→acuse,
dual channel, estado pills, D-H2.5 freeze) — fiscal-reporting file 01
(cluster F1), consumed by id; the ISV 18% stacking computation —
`taxation/06_isv.md` (its OQ-004 = `02_ OQ-4`, cross-check hint resolved
here); DJIMR/DMR retention export surfaces (F2); retention-voucher and
fiscal-document surfaces (e-invoicing wave, W3 E6); and CT
sanctions/procedure (T11 file).

## 2. Legal Basis

Authority order (binding, per master evidence index): the per-código SAR
Ayudas (`50_-55_`) are the field/flow authority for each declaration surface;
the IPC-chain *Acuerdos* `98_/99_/100_` are DIRECT sources for the current
values (no evidence pass — page-1-verified 2026-08-20, OQ-013); D. 17-2010
law-side values = `taxation/05` by id, never restated; manuals are STALE vs
gazettes where they conflict (R-H18 family; `54_ OQ-1`); all deadlines are
print-vintage DATED DATA — días **calendario** unless the instrument says
**hábiles** (per-instrument encoding, `04_ OQ-3` discipline).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ayuda DJ **Impuesto Selectivo al Consumo (código 203)**: "DECLARACIÓN JURADA DE IMPUESTO SELECTIVO AL CONSUMO (CÓDIGO 203)"; "(creado mediante Decreto No 58-1982 y sus reformas)"; sujetos: "los productores, fabricantes e importadores que se dediquen a la comercialización de las mercancías sujetas a este gravamen… También son responsables las personas naturales y jurídicas que en forma eventual realice[n] producciones o importaciones"; plazo: "dentro de los primeros diez (10) días hábiles siguientes al mes a que corresponda la declaración, de acuerdo con lo establecido en el Artículo 8 del Decreto No 58-1982"; Sección A: "Base de Cálculo / Tarifa / Impuesto a pagar" | General selective-consumption-tax declaration, code 203: created by Decree 58-1982 and reforms; liable = producers, manufacturers and importers of the taxed merchandise, including eventual (one-off) producers/importers; filed within the first ten business days (días hábiles) of the following month per Art. 8 of D. 58-1982; form Section A = Base / Tariff (rate) / Tax due (ad-valorem shape) | `hn/sources/50_Ayuda_selectivo_203.pdf` | portada + Generalidades pp.4-6; Sección A p.9 (EV50:EVID-152) |
| LB-002 | **D. 58-1982 (Ley de Impuesto Selectivo al Consumo) — ACQUIRED W6 as `115_`** (La Gaceta 02-ago-1982; Dado 28-jul-1982 per print — the adjacent-decree layout makes the Dado block OQ-flagged, `115_ OQ-2`; vigencia = publication → 02-ago-1982): Art. 1 creates the tax over the non-vehicle luxury canasta by fracción arancelaria; **Art. 2 the vehicle cc-tiers 10→50% ad-valorem** ("6. De 2,501 c.c. en adelante 50%" — load-bearing, EVID-417); Art. 3 single-stage collection (imports FOB-based; national ex-fábrica + 15% utilidad estimada); Art. 5 exemptions; Art. 6 contribuyentes responsables (producers, manufacturers, importers incl. eventuales); Art. 8 monthly DJ 10 días hábiles + factura with tax stated separately; Art. 10 stock taxed at vigencia; Art. 11 ISV supletoria; Art. 13 vigencia. **1995 state (EVID-409): D. 135-94 Cap. III reformed Arts. 1/3 to a flat 20% ad-valorem over Anexo II (imports base = CIF + arancel + SAA; national ex-fábrica) + SAC-8703 vehicles 20%.** | The código-203 statutory chain now in corpus: 1982 original (canasta + cc-tier tarifa) → 1995 restructure (20% + Anexo II). BOTH states are historical config; the CURRENT-state tarifa/canasta needs the modern reform chain (the 1995 state is the last in-corpus word) — FR-304 stays config-gapped for live periods, with the two dated states loadable. D. 59-1982 (adjacent in the same gazette, 20% CIF surcharge, 1982-only) noted EVID-419. | `hn/sources/115_Gaceta_1982-08-02_Decreto_58_Selectivos_Consumo.pdf` (+ `114_` Cap. III for the 1995 state) | 58-82-Arts. 1-13 (pp.1-2); D135-Cap. III Arts. 7-8 (p.5-6) (EV115:EVID-415..EVID-419; EV114:EVID-409) |
| LB-003 | Ayuda DJ **Producción y Consumo de Cigarrillos (código 211)**: responsable "El contribuyente en su condición de productor o fabricante, según el Artículo 23 del Decreto No 17-2010"; plazo "dentro de los primeros diez (10) días hábiles del mes siguiente a aquel en que se causó el hecho generador, según el Artículo 26"; Base de Cálculo: "el impuesto específico el cual se debe calcular sobre la base de cada millar o fracción de cigarrillos y el valor base del impuesto de los cigarrillos por millar o proporcional por fracción de millar de conformidad con la cantidad de cigarrillos vendida o importada, considerando el monto del impuesto específico actual determinado de conformidad con la variación positiva de la tasa del Índice de Precios (IPC) publicado por el Banco Central de Honduras (BCH)"; "Impuesto a pagar, campo autocompletado por el sistema (será igual a la base de cálculo)" | Cigarette production-and-consumption declaration, code 211: filer = the taxpayer as producer or manufacturer (D. 17-2010 Art. 23); filed within the first ten días hábiles of the month following the taxable event (Art. 26); base = the specific tax computed per thousand or pro-rated fraction of thousand cigarettes sold or imported, at the current IPC/BCH-adjusted specific amount; Tax due is system-autocomputed and equals the base (specific-amount shape) | `hn/sources/51_Ayuda_cigarrillos_211.pdf` | portada; Generalidades pp.4/6; selección p.8; Sección A p.9 (EV50:EVID-153) |
| LB-004 | Ayuda DJ **Producción y Consumo de Aguas Gaseosas (código 210 — NOT 212, R-H20)**: portada "(CÓDIGO 210)"; responsable "productor o fabricante, según el Artículo 38 del Decreto No 17-2010"; plazo "dentro de los primeros diez (10) días calendario del mes siguiente… según el Artículo 38"; base legal: "Decreto 17-2010, Ley de Fortalecimiento… y sus reformas, **Acuerdo No.014-2023**"; Sección A: "Base de Cálculo; Debe consignar el valor resultante, después de establecer el factor determinado anualmente en la tabla de producción según los litros por lempiras" + same autocomputed-impuesto text | Soft-drinks declaration, code 210 (the printed code is 210 — registry gloss "212-family" was the 8th mislabel, R-H20): filer = producer/manufacturer (Art. 38); first ten días calendario; base legal cites Acuerdo 014-2023 of the IPC chain; base = the value resulting after applying the annually-determined factor from the production table, "liters per lempira" (per-liter specific shape; no value printed) | `hn/sources/52_Ayuda_gaseosas.pdf` | portada; pp.4-5; p.8; Sección A p.9 (EV50:EVID-154; R-H20) |
| LB-005 | Ayuda DJ **Producción de Alcoholes y Licores Nacionales (código 205)**: title says "Nacionales"; same Art. 38 responsable/plazo (días calendario) and same base legal + same "factor… litros por lempiras" Sección A text as LB-004 | Domestic alcohols and liquors declaration, code 205: producer/manufacturer filer only — importers are nowhere addressed (title "Nacionales"; OQ-007); same D. 17-2010 Art. 38 chassis, 10 días calendario, single aggregated Base field with no proof-degree breakdown (OQ-008) | `hn/sources/53_Ayuda_alcoholes_205.pdf` | portada; pp.4-6; Sección A p.9 (EV50:EVID-155) |
| LB-006 | Ayuda DJ **Producción y Consumo de Cerveza (código 204)**: same Art. 38 chassis; portada carries "Dirección Nacional de Cumplimiento Tributario / **Junio 2026**"; login form styled "SER-204"; base legal still cites "**Acuerdo No. 014-2023**" although the corpus-current chain instrument is Acuerdo 218-2024 (`54_ OQ-1`) | Beer declaration, code 204: only dated manual of the six (Junio 2026 — freshest chassis snapshot); same producer/manufacturer filer, 10 días calendario, per-liter factor base; its Acuerdo citation is stale vs Acuerdo 218-2024 or is a deliberate tabla-reference — unresolved, never guessed | `hn/sources/54_Ayuda_cerveza_204.pdf` | portada p.1; pp.4-6; Sección A p.10 (EV50:EVID-156) |
| LB-007 | Ayuda DJ **Tasa por Servicios Turísticos (código 259)**: "(Creado mediante Decreto No. 131-98)"; rate/bases: "La tasa será de cuatro por ciento (4%) sobre el precio de alojamiento diario en hoteles; del precio por el arrendamiento de vehículos para fines turísticos; y, sobre el precio de los servicios prestados por las agencias operadoras de turismos receptivo. Artículo 43 del Decreto No. 131-98"; retebedores: "Las empresas hoteleras, las arrendadoras de vehículos para fines turísticos y las operadoras de turismos receptivo serán las responsables de retener y depositar este tributo"; exemption: "Quedan exceptuados…, las pensiones, hospedajes y hoteles de uso popular, calificados por el Instituto Hondureño de Turismo (IHT)"; plazo 10 días calendario; Sección A: "Base de Cálculo… / Tarifa; 4%. / Impuesto a pagar; campo autocompletado" | Tourist-services rate declaration, code 259: created by D. 131-98 (Ley de Estímulo a la Producción, a la Competitividad y Apoyo al Desarrollo Humano — statute unacquired, LEAD); 4% on three bases — daily hotel lodging price, tourist vehicle-rental price, inbound-tour-operator service price; hotels/rental companies/inbound operators are the retention agents; IHT-certified "uso popular" lodging exempt; 10 días calendario; ad-valorem form shape (Base + fixed Tarifa 4%) | `hn/sources/55_Ayuda_turistico_259.pdf` | portada; pp.4-6; Sección A p.9; alta p.8 (EV50:EVID-157) |
| LB-008 | **Acuerdo 172-2022** (SEFIN, signed 24-feb-2022; La Gaceta 35,877, 19-mar-2022): Art. 1 ajuste 5.32% IPC (Art. 1 prints "diciembre de 2020" while the considerandos quote dic-2021 — print anomaly, OQ-013); Art. 2 cigarrillos "QUINIENTOS TREINTA Y NUEVE LE mp I RAS EXACTOS (L539.00) sobre la base de cada millar o fracción de millar de cigarrillos vendidos, importados o adquiridos"; Art. 3 tabla L/litro 2022 (gaseosas 2202.10/99 = 0.893137; cerveza 2202.91/2203.00 = 6.344923; vinos/sangría/fermentadas 2204-2206 = 7.961705; brandy/whisky/gin/vodka/licores/tequila/bebidas preparadas = 42.996291; ron 2208.40.10.00 = 26.179739; ron añejado 40/38/36° = 26.179739/24.870590/23.561559; otros y aguardiente 2208.40.90.00 = 18.710715; aguardiente 45/40/38/30° = 18.710715/15.399872/12.874272/9.239873); Art. 5 alcohol etílico L0.153938/litro; Art. 6 monthly distributor-price reporting to DGPT; Art. 7 SARAH precision codes; Art. 8 deroga Acuerdo 199-2021; Art. 9 vigencia = 2 months from the día siguiente hábil of publication | Agreement 172-2022 — the 2022 vintage of the selectivo IPC adjustment: 5.32% adjustment factor; cigarettes L539.00 per thousand; the 2022 per-liter table by SAC 2022 + código de precisión; ethyl alcohol L0.153938/L; repeals Acuerdo 199-2021 (whose own tabla is unacquired — OQ-014); effective two months after the business day following gazette publication (derived ≈ 20-may-2022, flagged) | `hn/sources/98_Acuerdo_172-2022_selectivo_IPC.pdf` | pp.1-6 direct (Arts. 1-9); **page-1-verified 2026-08-20, no evidence pass (OQ-013)** |
| LB-009 | **Acuerdo 014-2023** (SEFIN, signed 31-ene-2023; La Gaceta 36,207, 19-abr-2023): Art. 1 IPC dic-2022 "nueve punto ochenta por ciento (9.80%)" pero el ajuste "sólo se actualizará en un seis por ciento (6%), por ser el máximo permitido" (Arts. 25/34 cap); Art. 2 cigarrillos "QUINIENTOS SETENTA Y UN LEMPIRAS CON TREINTA Y CUATRO CENTAVOS (L 571.34)"; Art. 3 tabla L/litro 2023 (gaseosas 0.946726; cerveza 6.725618; vinos/fermentadas 8.439407; brandy/gin/vodka/licores/whisky/tequila 45.576068; ron 27.750524; ron añejado 40/38/36° = 27.750524/26.362825/24.975252; otros y aguardiente 19.833358; aguardiente 45/40/38/30° = 19.833358/16.323864/13.646728/9.794266); Art. 5 alcohol etílico "L 0.163174"; Art. 7 distributor-price reporting + sanction; Art. 9 deroga 172-2022; Art. 10 vigencia 2 months | Agreement 014-2023 — the 2023 vintage: IPC 9.80% capped at the 6% statutory maximum; cigarettes L571.34/millar; 2023 per-liter table; ethyl alcohol L0.163174/L; repeals 172-2022; effective two months after publication (derived ≈ 20-jun-2023, flagged) | `hn/sources/99_Acuerdo_014-2023_selectivo.pdf` | pp.1-7 direct (Arts. 1-10); **page-1-verified 2026-08-20, no evidence pass (OQ-013)** |
| LB-010 | **Acuerdo 218-2024** (SEFIN, signed 26-feb-2024; La Gaceta 36,537, 18-may-2024 — corpus-current): Art. 1 "Ajustar a cinco punto diecinueve por ciento (5.19%)… variación interanual de índice de Precios al Consumidor a diciembre del 2023"; Art. 2 cigarrillos "SEISCIENTOS LE mpi RAS CON NOVENTA Y NUEVE CENTAVOS (L. 600.99)" + per-millar tabla extending to electronic cigarettes (2402.20; 2404.11; 2404.12; 2404.19.10; 2404.19.90; **8543.40** dispositivos personales de vaporización — all 600.99); Art. 3 tabla L/litro printed at 4dp (gaseosas 0.9959; cerveza 7.0744; vinos/fermentadas 8.8774; brandy/gin/vodka/licores/whisky/tequila/bebidas preparadas 47.9414; ron 29.1907; ron añejado 40/38/36° = 29.1907/27.7311/26.2716; otros y aguardiente 20.8627; aguardiente 45/40/38/30° = 20.8627/17.1710/14.3549/10.3026; alcohol etílico 2207.x = 0.1716 — tabla-only, no separate alcohol article this vintage); Art. 5 "debe prevalecer la descripción comercial"; Art. 8 distributor-price reporting + sanction; Art. 10 deroga 014-2023; Art. 11 vigencia 2 months | Agreement 218-2024 — the current vintage: 5.19% adjustment; cigarettes L600.99/millar now expressly covering electronic cigarettes and personal vaporization devices; 2024 per-liter table (4dp print); classification precedence restated on the commercial description; repeals 014-2023; effective two months after publication (derived ≈ 19-jul-2024, flagged) | `hn/sources/100_Acuerdo_218-2024_selectivo_IPC.pdf` | pp.1-7 direct (Arts. 1-11); **page-1-verified 2026-08-20, no evidence pass (OQ-013)** |
| LB-011 | **D. 17-2010**, L-Arts 23/26 (cigarettes: filer, millar base, días hábiles), 32-33/34 (beverage per-liter table + annual IPC revision capped 6%), 38 (beverage filer + días calendario), 86 (derogation list — does NOT name D. 58-1982; items 1-6 name other instruments + item 7 generic clause) — as quoted by the Ayudas; **law-side values/2010 base tables = `taxation/05` LB-008/LB-009 BY ID (HN-TAX-FR-194..200), never restated here** | Decree 17-2010 (Ley de Fortalecimiento de los Ingresos, Equidad Social y Racionalización del Gasto Público): the per-product production-and-consumption taxes behind códigos 211/210/205/204; Art. 86's non-derogation of D. 58-1982 is the coexistence conflict of OQ-002 | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Arts 23/26 pp.8-9; 32-34 p.10; 38 p.11; 86 (page unverified — EV50:EVID-152..156/158 gloss) |
| LB-012 | **D. 131-98 — ACQUIRED W6 as `116_`** (La Gaceta 20-may-1998, No. ≈28,566 OCR-tentative; full statute = **Ley de Estímulo a la Producción, a la Competitividad y Apoyo al Desarrollo Humano**): **Art. 43 FULL original** — "…créase la TASA DE SERVICIOS TURISTICOS. La tasa será de cuatro por ciento (4%) sobre el precio de alojamiento diario en hoteles; del precio por el arrendamiento de vehículos para fines turísticos; y, sobre el precio de los servicios prestados por las agencias operadoras de turismo receptivo. Las empresas hoteleras, las arrendadoras de vehículos para fines turísticos y las operadoras de turismo receptivo serán las responsables de retener y depositar este tributo… La obligación deberá cumplirse dentro de los diez (10) días del mes siguiente en que se causó el tributo. En el caso de las operadoras de turismo receptivo… se excluirán los valores de los servicios de alojamiento diario en hoteles y arrendamiento de vehículos… que hayan prestado y sobre los cuales ya se hubiere pagado la tasa. Quedan exceptuados… las pensiones, hospodajes, [y] hoteles de uso popular… calificados así por el Instituto Hondureño de Turismo." + Art. 44: administration = "Secretaría de Estado en el Despacho de Finanzas por medio de la Dirección Ejecutiva de Ingresos" + Art. 51 (L8M budget line funded from this tasa) | The código-259 statutory ORIGINAL: 4%/three-bases/retention-agents/exemption all now gazette-pinned (55_/71_ manual quotes CONFIRMED, EV115:EVID-424). TWO drift notes (gazette = record): (i) manual prints "diez (10) días calendario" where the original reads "diez (10) días del mes siguiente" (unqualified días); (ii) manual drops the Tesorería-General deposit clause. **NEW statutory rule the manuals omit — the OPERADORA ANTI-CASCADING EXCLUSION**: the inbound-operator base EXCLUDES lodging/rental values already taxed (never tax the same value twice across retainer families). Still unpinned: base composition incl./excl. ISV (OQ-011 stands — statute silent). Later-instrument WATCH: nothing in corpus derogates Art. 43; Ley de Turismo D. 314-98 (unacquired lead) may restate — manuals 55_/71_ (2024-2026) still cite it live. | `hn/sources/116_Gaceta_1998-05-20_Decreto_131-98_tasas.pdf` | 131-98-Arts. 43-44 (p.7); Art. 51 (p.8) (EV115:EVID-424; EV115:EVID-420) |

## 3. Functional Requirements

### 3.1 Family chassis — six monthly OVI obligations (F1 consumed by id)

- **HN-FREP-FR-296:** The system shall register six independent monthly
  declaration obligations — SER-203, SER-211, SER-210, SER-205, SER-204 and
  SER-259 — each presented through SAR's OVI with the two-section form
  ("A. Determinación del Impuesto" / "B. Créditos"), on the shared
  login→Declaraciones→Filtrar→"Realizar" pipeline whose chassis FRs are owned
  by fiscal-reporting file 01 (cluster F1) and consumed BY ID here — no
  chassis rule is restated or re-derived. (LB-001; LB-003..LB-007;
  EV50:EVID-151)
- **HN-FREP-FR-297:** The system shall implement Sección B (Créditos) with
  the family-wide autocomputed, non-editable panel:
  "Pagos realizados en el período" (autocompleted only when a paid value
  exists for that impuesto and period), "Excedente del período anterior"
  (validated against the prior month's credit), "Importe a compensar" and
  "Cesiones de crédito" (usable only with SAR-authorized credits), "Total
  créditos" (autocompleted); "Los campos de esta sección no serán
  editables". (LB-001; EV50:EVID-151)
- **HN-FREP-FR-298:** The system shall carry each declaration through the
  lifecycle: "Guardar como borrador" → "Presentar" → the juramento popup
  ("Jura la exactitud y veracidad de la presente declaración") →
  confirmation → "Ver formulario y acuse" generating the acuse PDF with its
  "código único" and QR code, snapshotting the resolved vintage values onto
  the presented record (D15 snapshot-on-write; D-H2.5 filed-period freeze —
  a presented declaration's stored values never mutate silently).
  (LB-001; EV50:EVID-151)
- **HN-FREP-FR-299:** The system shall support both payment paths from the
  presented declaration: botón "Pagar" (bank list / banca en línea) or the
  *boletín de pago* paid "en línea desde su banca electrónica o mediante
  una ventanilla" with the boletín number. (LB-001; EV50:EVID-151)
- **HN-FREP-FR-300:** The system shall expose the rectificativa flow for
  every código of this family per the F1 chassis (two entry points; original
  values left / corrections right; "Rectificativa OT Aprobada OT" state in
  morado; rejection message "Esta declaración queda rechazada…") with CT
  Art. 117 limits owned by file 01 — this file only binds the six códigos to
  that surface. (LB-001; EV50:EVID-151)
- **HN-FREP-FR-301:** The system shall gate each obligation on the
  vector-fiscal *alta* (obligation registration) with the per-código channel
  deltas as printed: 203/211 instruct alta in Recomendaciones ("si… no se
  encuentra de alta la obligación… deberá ser dada de alta"); 210/259 state
  it inline ("deberá proceder a dar de alta desde la Oficina Virtual
  (OVI)" — 210 and 259); 205/204 mention no alta path — recorded as config
  (absence ≠ impossibility). (LB-001; LB-003; LB-004; LB-007;
  EV50:EVID-151)
- **HN-FREP-FR-302:** The system shall encode the family deadline matrix as
  per-instrument DATED CONFIG (hábil vs calendario, `04_ OQ-3` discipline;
  kin HN-TAX-FR-151): 203 = first 10 días **hábiles** (D. 58-1982 Art. 8);
  211 = first 10 días **hábiles** (Art. 26); 210/205/204 = first 10 días
  **calendario** (Art. 38); 259 = first 10 días **calendario** (D. 131-98
  Art. 43) — never silently normalized to one convention.
  (LB-001; LB-003..LB-007; EV50:EVID-158)

### 3.2 SER-203 — the general selectivo under D. 58-1982

- **HN-FREP-FR-303:** The system shall flag the SER-203 duty for
  "productores, fabricantes e importadores" of the merchandise subject to
  the D. 58-1982 gravamen, expressly including *eventual* (one-off)
  producers and importers — the only código of this family whose sujetos
  include importadores by name. (LB-001; EV50:EVID-152)
- **HN-FREP-FR-304:** The system shall render SER-203 in the ad-valorem
  shape "Base de Cálculo / Tarifa / Impuesto a pagar" with the Tarifa
  resolved from DATED config rows. **W6: the statutory chain is now IN
  CORPUS** — 1982 state (D. 58-1982 Arts. 1-2: non-vehicle luxury canasta +
  vehicle cc-tiers 10→50%, `115_` EVID-415..419) and 1995 state (D. 135-94
  Cap. III: flat 20% ad-valorem over Anexo II + SAC-8703 vehicles, `114_`
  EVID-409) both loadable as HISTORICAL rows; for CURRENT periods the
  determination stays config-gapped (the 1995 state is the last in-corpus
  word; the modern reform chain is unacquired — never-guess, OQ-001
  narrowed) while the obligation, calendar and form shape ship complete.
  (LB-001; LB-002; LB-011; EV50:EVID-152/158; EV115:EVID-415..419;
  EV114:EVID-409)
- **HN-FREP-FR-305:** The system shall enforce the non-aggregation
  invariant: SER-203 is a SEPARATE tax, never an aggregator — amounts
  declared under the D. 17-2010 per-product códigos (211/210/205/204) shall
  never flow into a 203 Base; the statutory coexistence of D. 58-1982 with
  the per-product regime (D. 17-2010 Art. 86 does not derogate it) is
  carried as an open CONFLICT (OQ-002), never resolved silently in either
  direction. (LB-002; LB-011; EV50:EVID-152/158)

### 3.3 SER-211 — cigarettes (per-millar specific)

- **HN-FREP-FR-306:** The system shall compute the 211 determination as a
  specific per-unit amount: Base de Cálculo = the current IPC/BCH-adjusted
  *impuesto específico* applied "sobre la base de cada millar o fracción de
  cigarrillos… por millar o proporcional por fracción de millar de
  conformidad con la cantidad de cigarrillos vendida o importada"
  (thousands, fractions pro-rated — never ceiling-rounded to the next
  millar), and "Impuesto a pagar" autocomputed equal to the Base (no Tarifa
  field). (LB-003; EV50:EVID-153)
- **HN-FREP-FR-307:** The system shall restrict the SER-211 filer role to
  the taxpayer "en su condición de productor o fabricante" (Art. 23) while
  the Base counts cigarettes "vendida o importada": the importer-side path
  (SER-211 self-declaration vs customs/DUA liquidation under another
  mechanism) is UNRESOLVED and ships as a config flag on the obligation —
  never a silent branch (OQ-005). (LB-003; EV50:EVID-153/158)
- **HN-FREP-FR-308:** The system shall set the 211 tipo de declaración to
  **Determinativa** (the p.5 form table and the p.8 numbered steps control)
  and shall flag, never encode, the p.8 "Informativa" print glitch
  (internal contradiction, likely typo — OQ-004). (LB-003;
  EV50:EVID-151/153)

### 3.4 SER-210 / SER-205 / SER-204 — the per-liter family

- **HN-FREP-FR-309:** The system shall implement SER-210 (gaseosas) on the
  D. 17-2010 Art. 38 chassis — producer/manufacturer filer, first 10 días
  calendario, per-liter specific form (Base = Impuesto, autocomputed) — and
  shall pin the obligation code to **210** everywhere (portada, form table,
  dropdown), per ruling R-H20 (registry gloss "212-family" = mislabel;
  residual SER-212 lead = OQ-014). (LB-004; EV50:EVID-154; R-H20)
- **HN-FREP-FR-310:** The system shall implement SER-205 (alcoholes y
  licores NACIONALES) as producer-only (importers unaddressed — OQ-007) and
  shall compute the single aggregated Base de Cálculo OFF-FORM from the
  product mix: liters per product-and-proof variant × the dated per-liter
  rows (ron/aguardiente by degree; law-side grid = HN-TAX-FR-198 by id),
  because the form exposes one Base with no gradación breakdown (OQ-008
  carries the unverifiable-off-form caveat). (LB-005; LB-009; LB-010;
  EV50:EVID-155)
- **HN-FREP-FR-311:** The system shall implement SER-204 (cerveza) on the
  same Art. 38 chassis, snapshotting the Junio-2026 manual as the freshest
  chassis print, and shall record — without acting on — the base-legal
  anomaly that the manual cites Acuerdo 014-2023 while the corpus-current
  instrument is Acuerdo 218-2024 (stale citation vs tabla-reference —
  OQ-009; the operative values remain the FR-313 vintage rows either way).
  (LB-006; EV50:EVID-156)
- **HN-FREP-FR-312:** The system shall interpret the manuals' base language
  — "el factor determinado anualmente en la tabla de producción según los
  litros por lempiras" — as the working hypothesis: Base = liters
  subject to the tax × the annually-determined per-liter factor published in
  the IPC-chain tablas (LB-008..LB-010); NO value is printed in any manual,
  and the exact factor semantics (per-liter amount vs an inverse
  liters-per-lempira divisor) stay OQ-flagged until reconciled against the
  `99_`/`100_` tablas at implementation (OQ-006). (LB-004; LB-005; LB-006;
  EV50:EVID-154/155/156)

### 3.5 The IPC-chain value home (direct sources 98_/99_/100_)

- **HN-FREP-FR-313:** The system shall load the selectivo current values as
  DATED vintages — one per Acuerdo (172-2022; 014-2023; 218-2024
  corpus-current) — with `valid_from` per each Acuerdo's own vigencia rule
  ("dos (2) meses contados a partir del día siguiente hábil de la fecha de
  su publicación": gazettes 19-mar-2022 / 19-abr-2023 / 18-may-2024;
  resolved effective dates ≈ 20-may-2022 / 20-jun-2023 / 19-jul-2024 are
  DERIVED-AND-FLAGGED, never asserted as printed) — transcribed exactly as
  printed (98_/99_ at 6dp, 100_ at 4dp), never re-derived, re-rounded or
  cap-computed (R-H10-kin; OQ-013/OQ-014). (LB-008; LB-009; LB-010 —
  direct, page-1-verified 2026-08-20; EV50:EVID-158)
- **HN-FREP-FR-314:** The system shall carry the cigarette per-millar rows
  as printed: L539.00 (172-2022 Art. 2), L571.34 (014-2023 Art. 2), L600.99
  (218-2024 Art. 2) "sobre la base de cada millar o fracción de millar de
  cigarrillos vendidos, importados o adquiridos"; and shall scope the
  218-2024 vintage to the enlarged per-millar tabla — tobacco cigarettes
  (2402.20), electronic cigarettes containing tobacco/reconstituted tobacco
  or nicotine or substitutes (2404.11/2404.12/2404.19.10/2404.19.90) and
  "cigarrillos electrónicos y dispositivos personales de vaporización
  eléctricos similares" (8543.40) — all at the same L600.99 (earlier
  vintages' tablas carry no 2404/8543 rows — scope difference is data, not
  interpretation). (LB-008; LB-009; LB-010 — direct; EV50:EVID-153/158)
- **HN-FREP-FR-315:** The system shall carry the beverage per-liter rows
  keyed by SAC 2022 code + código de precisión per vintage, as printed in
  each Art. 3 tabla (family anchors — full values in §4): gaseosas
  (2202.10.00.00/2202.99.90.00); cerveza sin alcohol / de malta
  (2202.91/2203.00); vinos, champagne, sangría y demás bebidas fermentadas
  (2204.x/2205.x/2206.00); brandy/coñac/vermut y aguardiente de vino
  (2205.x .00 / 2208.20); whisky/gin/vodka/licores/tequila/bebidas
  preparadas-breizzer-coolers (2208.30-.90); ron (2208.40.10 by añejado
  degree) and otros y aguardiente (2208.40.90 by degree).
  (LB-008; LB-009; LB-010 — direct; EV50:EVID-154/155/156/158)
- **HN-FREP-FR-316:** The system shall carry the alcohol-etílico per-liter
  rows with their per-vintage source articles as printed: L0.153938
  (172-2022 Art. 5), L0.163174 (014-2023 Art. 5) and L0.1716 (218-2024 —
  tabla rows 2207.10.10.00/2207.10.90.00/2207.20.00.00 only; that vintage
  has NO separate alcohol article — recorded as a source-shape difference,
  never normalized). (LB-008; LB-009; LB-010 — direct; EV50:EVID-155)
- **HN-FREP-FR-317:** The system shall apply the unspecified-proof rule:
  for production and import of ron and aguardiente "con graduación
  alcohólica no especificada en el cuadro", the tax of the "grado alcohólico
  inmediato superior" (immediately higher listed degree) applies — resolved
  against the vintage's own degree rows. (LB-008; LB-009; LB-010 — direct,
  Arts. 4/4/4)
- **HN-FREP-FR-318:** The system shall encode classification precedence PER
  VINTAGE as printed: 172-2022 Art. 4 and 014-2023 Art. 6 — "debe prevalecer
  el tipo de bebida" under the SAC general interpretation rules and HS
  amendments (aduanera communicates divergent incisos to SEFIN/AT); 218-2024
  Art. 5 — "debe prevalecer la **descripción comercial**" under the same
  SAC rules (wording drift recorded, OQ-013; both bind the customs
  classification feed only). (LB-008; LB-009; LB-010 — direct)
- **HN-FREP-FR-319:** The system shall generate the monthly
  distributor-price report duty owned by the chain Acuerdos: productores e
  importadores of cigarettes and other tobacco products, gaseosas and
  refrescantes, bebidas alcohólicas and other prepared/fermented beverages —
  plus SEFIN-authorized importers of industrial alcohol and alcohol for
  preparing beverages (014-2023/218-2024 scope) — must report to the
  Dirección General de Política Tributaria (DGPT) "los precios de venta al
  distribuidor de sus productos" monthly; non-compliance sanctioned per the
  applicable framework (014-2023 Art. 7 / 218-2024 Art. 8; 172-2022 Art. 6
  without the sanction clause — vintage scope is data).
  (LB-008; LB-009; LB-010 — direct)
- **HN-FREP-FR-320:** The system shall implement the missing-vintage
  no-default rule: a period with no IPC-chain row loaded (pre-172-2022 — the
  Acuerdo 199-2021 chain and earlier is unacquired; post-218-2024 — the next
  Acuerdo pending) blocks the specific-tax determination of códigos
  211/210/205/204 with an explicit config-gap flag — NEVER a fallback to the
  prior vintage, NEVER a 6%-cap-derived value (filling
  `taxation/05` OQ-004's "missing-year rows = config gaps, never
  cap-derived" contract). (LB-008; LB-009; LB-010 — direct;
  EV50:EVID-158)

### 3.6 SER-259 — tasa por servicios turísticos (4% retention)

- **HN-FREP-FR-321:** The system shall implement the 259 retention engine
  per D. 131-98 Art. 43 **as gazette-pinned since W6 (`116_`, OQ-010
  resolved)**: 4% on (a) the daily lodging price in hotels, (b) the price of
  vehicle rentals for tourist purposes and (c) the price of services of
  *agencias operadoras de turismos receptivo* (inbound tour operators); the
  retention agents are the hotel companies, tourist vehicle-rental companies
  and inbound operators, who retain and deposit at the Tesorería General or
  authorized agency; AND shall enforce the OPERADORA ANTI-CASCADING
  EXCLUSION — the inbound-operator base (c) EXCLUDES lodging and
  tourist-vehicle-rental values already subjected to the tasa (the same
  value never enters two retainer families' bases).
  (LB-007; LB-012; EV50:EVID-157; EV115:EVID-424)
- **HN-FREP-FR-322:** The system shall exempt from the 259 retention the
  stays at "pensiones, hospedajes y hoteles de uso popular, calificados por
  el Instituto Hondureño de Turismo (IHT)" — an IHT-certification flag on
  the lodging partner, whose qualification mechanics are config (OQ-012).
  (LB-007; EV50:EVID-157)
- **HN-FREP-FR-323:** The system shall render SER-259 in the ad-valorem
  shape — "Base de Cálculo… / Tarifa; 4%. / Impuesto a pagar; campo
  autocompletado por el sistema" — with the monthly entero inside the first
  10 días of the following month (D. 131-98 Art. 43 gazette original:
  "dentro de los diez (10) días del mes siguiente" — UNQUALIFIED días; the
  55_ manual's added word "calendario" is a gloss, recorded, gazette =
  record), and shall carry the base composition (ISV included or excluded;
  service charges in or out) as UNPINNED config on every FR-321 line
  (OQ-011 — the statute is silent). (LB-007; LB-012; EV50:EVID-157/158;
  EV115:EVID-424)

### 3.7 Cross-boundaries (consumed by id — never restated)

- **HN-FREP-FR-324:** The system shall feed the ISV 18% family base with
  the FR-313..FR-316 vintage values BY ID into `taxation/06_isv.md`
  HN-TAX-FR-224 (distributor-stage price "incluyendo el valor del impuesto
  de producción y consumo" for beer/sodas; import base CIF + arancelarios +
  selectivos of HN-TAX-FR-218..220): the exact stacking ORDER remains that
  file's OQ-004 (`02_ OQ-4`, register C1) — this file supplies values only
  and resolves no ordering. (LB-011; EV50:EVID-158)
- **HN-FREP-FR-325:** The system shall consume the selectivo LAW side BY ID
  from `taxation/05_d17-2010-family.md` — cigarettes HN-TAX-FR-194..197
  (L350/millar 2010 base + IPC mechanism), beverages HN-TAX-FR-198..200
  (2010 per-liter table + mechanism), stacking boundary HN-TAX-FR-207, its
  OQ-004 value-home contract pointing here — and the hábil/calendario
  config family HN-TAX-FR-151 from `taxation/04_isr-withholding.md`; no
  law-side base, rate or 2010 table is restated in this file.
  (LB-011; EV50:EVID-152/158)

## 4. Data Model

Value rows land in the `selectivo_rates.csv` sidecar CONTRACT defined by
`taxation/05_d17-2010-family.md` §4 (families `cigarette_millar`,
`beverage_liter`, `alcohol_etilico`; `value_home = f9_ipc_acuerdo`): this
file owns the CONTENT of those rows (the three vintages below,
print-faithful precision per vintage — 6dp/6dp/4dp — never re-rounded); the
single-file synthesis mandate means the CSV itself is seeded at
implementation from LB-008..LB-010, not written by this wave.

**IPC-chain vintage matrix (values AS PRINTED; direct sources):**

| Family (SAC anchor) | 172-2022 (G 19-mar-2022) | 014-2023 (G 19-abr-2023) | 218-2024 (G 18-may-2024, current) |
|---|---|---|---|
| Adjustment factor | 5.32% (Art. 1 prints "dic-2020" — anomaly, OQ-013) | 9.80% IPC capped at 6% (Art. 1) | 5.19% (Art. 1) |
| Cigarrillos L/millar (incl. 2404.x + 8543.40 e-cig from 218-2024) | 539.00 | 571.34 | 600.99 |
| Gaseosas 2202.10/99 L/L | 0.893137 | 0.946726 | 0.9959 |
| Cerveza 2202.91/2203.00 L/L | 6.344923 | 6.725618 | 7.0744 |
| Vinos/sangría/fermentadas 2204-2206 L/L | 7.961705 | 8.439407 | 8.8774 |
| Brandy/coñac/vermut/aguardiente-vino 2205(.00)/2208.20 L/L | 42.996291 | 45.576068 | 47.9414 |
| Whisky/gin/vodka/licores/tequila/beb. preparadas 2208.30-.90 L/L | 42.996291 | 45.576068 | 47.9414 |
| Ron 2208.40.10.00 L/L | 26.179739 | 27.750524 | 29.1907 |
| Ron añejado 40°/38°/36° L/L | 26.179739/24.870590/23.561559 | 27.750524/26.362825/24.975252 | 29.1907/27.7311/26.2716 |
| Otros y aguardiente 2208.40.90.00 L/L | 18.710715 | 19.833358 | 20.8627 |
| Aguardiente 45°/40°/38°/30° L/L | 18.710715/15.399872/12.874272/9.239873 | 19.833358/16.323864/13.646728/9.794266 | 20.8627/17.1710/14.3549/10.3026 |
| Alcohol etílico 2207.x L/L (source article) | 0.153938 (Art. 5) | 0.163174 (Art. 5) | 0.1716 (tabla-only) |

**Entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.selectivo.parameter (taxation/05 model; F9 fills the f9_ipc_acuerdo slots) | acuerdo, gazette_ref, ipc_pct, valid_from, valid_to, family, sac_code, precision_code, proof_degree, amount, unit, source_article | char/date/monetary/select | acuerdos 172-2022/014-2023/218-2024; valid_from = vigencia-rule-resolved (derived, flagged); unit: millar · litro; value_home = f9_ipc_acuerdo; never overwritten (D-H2) | FR-313..FR-317, FR-320 |
| l10n_hn.frep.selectivo.declaration (new) | código, period, state, base, tarifa, impuesto, b_pagos, b_excedente, b_compensar, b_cesiones, b_total_creditos, acuse_code, acuse_qr, boletin_no | select/date/monetary/char | código: 203 · 204 · 205 · 210 · 211 · 259; state: borrador → presentada → rectificativa/rechazada; Sección B non-editable (FR-297); tarifa empty for specific forms (impuesto = base) | FR-296..FR-300, FR-306, FR-309..FR-311, FR-323 |
| l10n_hn.frep.obligation (family instance) | código, due_day_count (10), due_day_semantics, alta_channel | select/int | semantics: hábil (203/211) · calendario (204/205/210/259); alta_channel: recomendaciones (203/211) · inline (210/259) · none-printed (205/204) | FR-301, FR-302 |
| product.template | consumption of taxation/05 fields BY ID (hn_selectivo_family, hn_proof_degree) | select/float | no new fields here — declaration layer keys rows off the law-side product grid | FR-310, FR-315..FR-317 |
| res.partner | tourist_rate_retainer, iht_uso_popular | boolean/select | retainer kinds: hotel · tourist_vehicle_rental · inbound_operator; IHT certification flag (config, OQ-012) | FR-321, FR-322 |
| account.move.line | tourist_rate_base_component, tourist_rate_retained | monetary | 259 retention lines on lodging/rental/inbound service invoices; base composition flag (OQ-011) | FR-321, FR-323 |
| l10n_hn.selectivo.price.report (new) | reporter, period, product, distributor_price, dgpt_sent_on | m2o/date/monetary | monthly DGPT distributor-price report rows (tobacco/gaseosas/alcoholic/prepared beverages + authorized industrial-alcohol importers) | FR-319 |

## 5. Odoo Mapping

Layer semantics: `odoo` for the whole family — computation, dated config and
declaration bookkeeping live in the LGPL client; SAR's OVI portal is an
external surface (this layer shapes data, calendars and ledgers for it) and
no SaaS-split surface exists in this cluster. Model names stable across
Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-296..FR-300 | odoo | l10n_hn.frep.selectivo.declaration | lifecycle fields | Chassis FRs consumed by id from fiscal-reporting file 01 (F1); D-H2.5 freeze on presented records; acuse código único + QR stored |
| FR-301, FR-302 | odoo | l10n_hn.frep.obligation | alta + due-day rows | D12 version regime: deadlines are print-vintage DATED DATA (manuals undated except 54_ Junio-2026); hábil/calendario per instrument (04_ OQ-3) |
| FR-303..FR-305 | odoo | obligation flag + declaration form shape | ad-valorem gate | D. 58-1982 rows absent → computation blocked with config gap (OQ-001); non-aggregation invariant guarded in code review tests |
| FR-306..FR-308 | odoo | account.move (producer/import moves) × l10n_hn.selectivo.parameter | per-millar compute | Fraction pro-rated (÷1000 × dated L/millar); impuesto = base autocompute; importer-path flag (OQ-005); Determinativa fixed (OQ-004 note) |
| FR-309..FR-312 | odoo | account.move × l10n_hn.selectivo.parameter | per-liter compute | 210 pinned (R-H20); 205 aggregated-off-form proof mix; factor semantics flagged (OQ-006); 014-2023-vs-218-2024 citation anomaly noted (OQ-009) |
| FR-313..FR-317 | odoo | l10n_hn.selectivo.parameter (f9 slots) | vintage rows | D15/D16: dated rows + snapshot-on-write onto declarations; values print-faithful (6dp/6dp/4dp); valid_from derived from each vigencia rule and flagged; e-cig scope rows only from 218-2024 |
| FR-318 | odoo | product classification feed | precedence rows | Per-vintage precedence text as printed (tipo de bebida → descripción comercial drift, OQ-013); customs-feed only |
| FR-319 | odoo | l10n_hn.selectivo.price.report | DGPT rows | Monthly job off producer/importer price lists; sanction exposure informational |
| FR-320 | odoo | parameter lookup | missing-vintage block | Same no-default pattern as taxation/04 FR-124; fills taxation/05 OQ-004 contract |
| FR-321..FR-323 | odoo | account.move.line retention + res.partner flags | 259 engine | 4% on three bases; IHT exemption flag; base-composition config (OQ-011); rate manual-print vintage (OQ-010) |
| FR-324 | odoo | value feed only | by-id interface | Stacking ORDER stays taxation/06 OQ-004 (02_ OQ-4) — this file asserts no order |
| FR-325 | odoo | by-id consumption | none | Law side = taxation/05 HN-TAX-FR-194..200/207 + OQ-004; calendar family = taxation/04 HN-TAX-FR-151 |

Version-regime notes (D12): the IPC vintages carry their own effective
mechanism (2-months-post-gazette vigencia) — regime changes are dated rows,
no adaptation windows; the six Ayudas are print-vintage manuals (R-H18
family: gazette text is the record where they conflict — the one in-family
instance is `54_ OQ-1`, carried OQ-009).

## 6. Acceptance Criteria

- **AC-001:** Given cigarettes taxed in January 2026, then the SER-211
  deadline row computes against the first 10 días **hábiles** of February
  2026; given gaseosas in the same month, then SER-210 computes against the
  first 10 días **calendario** — the two semantics never normalize to one
  (FR-302).
- **AC-002:** Given 2,400 cigarettes sold in a period under the 218-2024
  vintage, then Base = Impuesto = 2.4 × 600.99 = L1,442.376 (stored
  full-precision, printed 2dp) — the fraction is pro-rated, never ceiled to
  3 millares (FR-306, FR-314).
- **AC-003:** Given 10,000 L of cerveza de malta under 218-2024, then Base
  = Impuesto = 10,000 × 7.0744 = L70,744.00; given the same lot under the
  014-2023 vintage, then 10,000 × 6.725618 = L67,256.18 (FR-312, FR-315).
- **AC-004:** Given ron añejado at 37° (unlisted), then the applicable row =
  the 38° row of the selected vintage (29.1907 → 27.7311 → 26.2716 ladder
  per vintage); given aguardiente at 43°, then the 45° row (FR-317).
- **AC-005:** Given a period dated after the 014-2023 effective date and
  before 218-2024's, then cigarette rows resolve to L571.34; given a period
  after 218-2024's effective date, then L600.99 — resolved by the
  vigencia-rule valid_from rows, dates flagged derived (FR-313, FR-314).
- **AC-006:** Given a 2025 period with no post-218-2024 Acuerdo loaded, then
  the 211/210/205/204 determinations block with a missing-vintage flag —
  never 600.99 × 1.06, never the prior vintage silently (FR-320).
- **AC-007:** Given an electronic-cigarette product (SAC 2404.12) in a
  218-2024-period move, then the per-millar L600.99 applies; given the same
  product in a 172-2022-period move, then the vintage carries no such row
  and the determination flags for manual classification (FR-314).
- **AC-008:** Given an SER-203 attempt with no D. 58-1982 tarifa rows
  loaded, then the obligation and calendar render but "Impuesto a pagar"
  computes nothing and a config-gap flag surfaces (FR-304).
- **AC-009:** Given a month with 211 Base L1,442.38 filed, then the SER-203
  Base of the same taxpayer is unchanged — no per-product amount ever
  aggregates into 203 (FR-305).
- **AC-010:** Given a 205 mix of 1,000 L aguardiente 40° + 500 L ron añejado
  40° under 218-2024, then the single aggregated Base = 1,000 × 17.1710 +
  500 × 29.1907 = L31,766.35, with the mix trace stored off-form
  (FR-310, FR-315).
- **AC-011:** Given a presented January declaration whose vintage values
  were later re-seeded, then the presented record keeps its stored snapshot
  (código único + QR intact) and only future periods see the new rows
  (FR-298, FR-313).
- **AC-012:** Given a prior-month credit of L500 on SER-210, then the next
  month's Sección B shows "Excedente del período anterior" = 500
  autocomputed; an "Importe a compensar" edit without a SAR-authorized
  credit record is rejected; all Section B fields stay non-editable
  (FR-297).
- **AC-013:** Given a rectificativa initiated from Declaraciones →
  Realizadas → "Rectificar", then original values render left / corrections
  right and the state pill reads "Rectificativa OT Aprobada OT" (or the
  rechazo message on rejection) (FR-300).
- **AC-014:** Given an SER-211 selection screen, then tipo = Determinativa
  and no informativa-mode artifact exists for codes 203/204/205/210/211/259
  (FR-308).
- **AC-015:** Given hotel lodging revenue of L100,000 in a month at a
  non-exempt hotel, then the 259 retention = 4% × base-config = L4,000 on
  the base-composition flag's setting, declared with Base + Tarifa 4% and a
  first-10-días-calendario entero (FR-321, FR-323).
- **AC-016:** Given a stay at an IHT uso-popular-certified hospedaje, then
  no 259 retention line is created (FR-322).
- **AC-017:** Given a producer of gaseosas with distributor prices for the
  month, then a DGPT price-report row is generated with period, product and
  price, and the report job covers tobacco/beverage/alcohol producers and
  importers plus authorized industrial-alcohol importers per the
  014-2023/218-2024 scope (FR-319).
- **AC-018:** Given an ISV 18% computation consuming selectivo values, then
  the values come from the FR-313..316 rows by id and the system asserts no
  stacking order of its own (order = taxation/06 OQ-004) (FR-324).
- **AC-019:** Given 2,000 L of imported alcohol etílico under 218-2024,
  then the per-liter row = 0.1716 (tabla-sourced) and under 014-2023 =
  0.163174 (Art. 5-sourced) — source article recorded per row (FR-316).
- **AC-020:** Given a carga of the vintage matrix, then every stored amount
  equals its print (0.9959 not 0.995900; 6dp rows keep 6dp) and no stored
  value is a ×(1+IPC) recomputation (FR-313).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `50_ OQ-1` (carried, C2 — LEAD): what merchandise canasta remains under D. 58-1982 / SER-203? **W6 NARROWED: the statutory chain is in corpus** (`115_` 1982 canasta + cc-tier tarifa; `114_` 1995 flat-20% Anexo-II restructure — LB-002) — the remaining question is which state (if either) governs CURRENT periods: the modern reform chain after D. 135-94 is unacquired, so FR-304 keeps the live-period config gap with the two dated states loadable as history. | no (current-state only; historical states pinned) | acquisition queue (post-1995 selectivo reform chain) | open (narrowed) |
| OQ-002 | `50_ OQ-2` (carried, C2 — CONFLICT): canasta overlap — does any good fall under BOTH D. 58-1982 (203) and the D. 17-2010 per-product impuestos? Art. 86 derogates D. 58-1982 nowhere by name (items 1-6 + generic item 7) — coexistence unexplained in corpus; FR-305 encodes the invariant only, never a resolution. | no | controller (ruling) | open |
| OQ-003 | `50_ OQ-3` + `53_ OQ-3` (carried, C2 — VERIFY): five of the six manuals are undated (vintage only inferable ≥2024 via the SAR-236-2024 citation; only 54_ prints "Junio 2026") — all deadlines/rates are print-vintage DATED DATA; re-verify on any manual re-print. | no | Takumi S-HN3 | open |
| OQ-004 | `51_ OQ-1` (carried, C2 — CONFLICT): 211 p.8 instructs tipo "Informativa" while the p.5 table and same-page steps say "Determinativa" — likely typo; FR-308 fixes Determinativa and flags the glitch; confirm on the live OVI. | no | Takumi S-HN3 | open |
| OQ-005 | `51_ OQ-2` (carried, C2 — CONFIG): filer = "productor o fabricante" (Art. 23) but the base counts cigarettes "vendida o importada" — do cigarette importers file SER-211, or is the import side collected at customs/DUA under another mechanism? FR-307 ships the flag; customs importer paths open (kin OQ-007). | no | Takumi S-HN3 + acquisition queue (customs practice) | open |
| OQ-006 | `52_ OQ-2` + `54_ OQ-2` (carried, C2 — CONFIG): exact mechanics of "el factor determinado anualmente en la tabla de producción según los litros por lempiras" — FR-312's liters × dated-per-liter-factor reading is the working hypothesis; reconcile against the `99_`/`100_` tablas and SAR practice before freezing (values themselves are pinned by FR-313..316). | no | Takumi implementation | open |
| OQ-007 | `53_ OQ-1` (carried, C2 — CONFIG): importers of alcoholic beverages are entirely unaddressed (title "Nacionales"; filer = productor/fabricante) — who declares/pays for imports, under which código or customs liquidation? | no | Takumi S-HN3 + acquisition queue | open |
| OQ-008 | `53_ OQ-2` (carried, C2 — CONFIG): law bases vary by product and proof (ron/aguardiente by degrees) but the form asks a single aggregated Base with no gradación breakdown — FR-310 computes the mix off-form; confirm against live OVI behavior (pre-computed base accepted as-is?). | no | Takumi S-HN3 | open |
| OQ-009 | `54_ OQ-1` (carried, C2 — CONFLICT): the Junio-2026 cerveza manual's base legal still cites Acuerdo 014-2023 while the corpus-current instrument is Acuerdo 218-2024 — stale citation or deliberate tabla-reference; recorded, never acted on (operative values = FR-313 vintages either way); watch the next manual re-print. | no | Takumi S-HN3 (re-print watch) | open |
| OQ-010 | `55_ OQ-1` (carried, C2 — LEAD) → **RESOLVED at W6**: D. 131-98 acquired as `116_` (G 20-may-1998) — Art. 43 FULL original confirms the 4%, the three bases, the retention agents and the official long title; Art. 44 pins administration (Finanzas/DEI). Drift recorded (LB-012): manual "10 días calendario" vs gazette "10 días del mes siguiente"; manual omits the Tesorería deposit clause and the operadora anti-cascading exclusion (now encoded, FR-321). Residual watch: Ley de Turismo D. 314-98 (unacquired) may restate the tasa — manuals still cite Art. 43 live. | no | controller (W6) | resolved (D. 314-98 watch carried) |
| OQ-011 | `55_ OQ-2` (carried, C2 — CONFIG): 259 base composition unstated — is the 4% applied on the price including or excluding ISV (and service charges)? Config flag on every FR-321 line; pin from the statute or SAR guidance. | no | acquisition queue | open |
| OQ-012 | `55_ OQ-3` (carried, C2 — CONFIG): operational definitions missing — "agencias operadoras de turismos receptivo" scope and the IHT "uso popular" qualification mechanics (registry/certification?) drive FR-321(c) and FR-322 flags. | no | acquisition queue (IHT) | open |
| OQ-013 | FILE-LOCAL (no evidence pass ran on `98_/99_/100_`): cited DIRECT with page-1 verification by this synthesis on 2026-08-20 — all three PASS title-vs-content (98_ = Acuerdo 172-2022, G 35,877 19-mar-2022; 99_ = Acuerdo 014-2023, G 36,207 19-abr-2023; 100_ = Acuerdo 218-2024, G 36,537 18-may-2024). Recorded print anomalies, values never "corrected": (a) 98_ Art. 1 prints "diciembre de 2020" where its considerandos quote the dic-2021 IPC (5.32% both places); (b) 98_ p.5 OCR garble zone around the 2208.20/2208.30 rows (values cross-checked against the 99_/100_ tablas' clean structure); (c) 100_ p.1 carries the signature tail of an unrelated congressional decree (front-matter noise, not a mislabel); (d) precedence wording drift 98_/99_ "tipo de bebida" vs 100_ "descripción comercial" (FR-318 encodes per vintage). A W-kin evidence pass should confirm before implementation freeze. | no | Takumi S-HN3 (evidence backfill) | open |
| OQ-014 | FILE-LOCAL (vintage gaps + residuals): (a) pre-172-2022 vintages — Acuerdo 199-2021 (derogated by 172-2022, Art. 8) and the earlier chain are unacquired → historical periods are config gaps (FR-320); the next post-218-2024 Acuerdo is a standing watch; (b) `52_ OQ-1` residual after R-H20 fixed the gaseosas mislabel: does any separate SER-212 form exist (e.g. otras bebidas alcohólicas/preparadas per the Acuerdo titles)? Acquisition lead: SAR Ayuda list; (c) valid_from dates are derived from each Acuerdo's 2-months-post-gazette vigencia rule — pin the exact calendar resolution (día siguiente hábil determination) at implementation. | no | acquisition queue + Takumi implementation | open |
