# HN — Fiscal reporting — Transfer pricing 545 (DJIAPT) + annual informativas 541 socios · 542 alquileres · 543 municipalidades

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F10 of the W2
evidence (EV63: EVID-176..183): the four annual informative declarations
that are not retention or determination engines. It owns: (a) **código
545** — the *Declaración Jurada Informativa Anual sobre Precios de
Transferencia* (DJIAPT, annual sworn informative declaration on transfer
pricing): the obligation trigger matrix (*medianos/grandes* always when
related-party operations exist; *pequeños* only above USD 1,000,000
accumulated at 31-dic BCH parity; special-benefit-regime and *paraíso
fiscal* counterpart triggers), the Apr-30 / next-business-day /
special-period +3 months calendar with the YYYYMM annual period key, the
Sección A operation-line contract (56 operation types, relación 1-19,
naturaleza 1-4, counterparty identification, TP método), the 10
type-driven conditional detail annexes with the comparability field group
(*rango intercuartil* + ajustes 1-3) and the 33-code reference-rate
catalog, Sección B (resultado ±, **Ajuste PT with auto-migration into the
ISR annual DJ base** — the write-back contract consumed by
[07_isr-annual-102-103.md](07_isr-annual-102-103.md) FR-230 by id), grupo
económico / CbCR block per SAR-653-2023, the Sección C Estudio-PT author
registry, and the USD 10,000 sanction constants; (b) **código 541** — the
*Declaración Informativa Anual de Socios y Participación de Utilidades*
(shareholders and distributed-profits inform, ISR Art. 47, end of
February); (c) **código 542** — the DJ Informativa de Contratos de
Alquileres (rental-contracts inform, lessee-side lines, Acuerdo 034/99
Sexto L120,000 trigger); and (d) **código 543** — the *Informativa de
Municipalidades* (municipalities as filers reporting L600,000+
licensees).

It does **not** own: the OVI/SW filing chassis — alta, pendiente,
borrador, juramento, acuse/QR, estado registry and rectificativa
mechanics (fiscal-reporting file 01, cluster F1 — on disk; consumed by id;
consumed by path/cluster id throughout); the ISR annual DJ's TP ± line
placement and base increase
([07_isr-annual-102-103.md](07_isr-annual-102-103.md) HN-FREP-FR-230 —
the consumer of this file's write-back, never re-derived here); the 535
EEFF report and its related-party balance-sheet panels (file 06, cluster
F6 — parallel disclosure surface, consumed by id); the statutory
*vinculación* frame — the 1963 ISR Art. 3 economic-relatedness rules and
the Art. 47 shareholder dataset
([../taxation/01_isr-framework.md](../taxation/01_isr-framework.md)
HN-TAX-FR-006 / FR-022, consumed by id); the dividend and cedular-alquiler
retention engines and the DJIMR export contract
([../taxation/04_isr-withholding.md](../taxation/04_isr-withholding.md),
[02_djimr-retention-declarations.md](02_djimr-retention-declarations.md)
FR-062 — the 542↔136 linkage stays flag-only); CT sanctions and procedure
(taxation T11 zone — sanction *constants* live here, sanction *mechanics*
do not); and the substantive TP law content — D. 232-2011, Acuerdo
027-2015, DEI-SG-004-2016 and SAR-653-2023 are **unacquired leads**:
every law-side semantic they would pin is config-gapped, never guessed
(63_ OQ-6).

## 2. Legal Basis

Authority order (binding, per master evidence index): the per-código
Ayudas are primary for declaration mechanics; the TP family (D. 232-2011
+ Acuerdo 027-2015 + DEI-SG-004-2016 + SAR-653-2023) is NOT in the
corpus — cited through the Ayuda `63_` with LEAD flags. ISR Art. 47 is
carried by `64_` and verified verbatim against the consolidated law
`01_`. D-H1/D-H2 (dated rows) and D-H2.5 (filed-period freeze) bind
throughout.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ayuda 545 (63_), Marco Normativo + Usuarios + Umbrales + Sanciones: marco — "Ley de Regulación sobre Precios de Transferencia Decreto 232-2011 \| Enero 2014 \| Artículo 17 y 20"; "Reglamento de la Ley de Regulación sobre Precios de Transferencia Acuerdo 027-2015 \| Septiembre 2015 \| Artículo 30 y 31"; "Acuerdo DEI-SG-004 \| Abril 2016 \| Título primero"; "Directrices de la OCDE … 2010, 2017 y 2022". Usuarios: "Personas naturales o jurídicas categorizados como medianos o grandes contribuyentes que realicen operaciones comerciales o financieras con partes relacionadas o vinculadas"; "…con aquellas amparadas en regímenes especiales que gocen de beneficios fiscales según Decreto No 117-2021…"; "…con aquellas residentes en países catalogados como paraíso fiscal…"; "…catalogados como pequeños contribuyentes que realicen operaciones… con parte relacionadas locales y/o domiciliadas en el exterior, dentro de un mismo periodo fiscal por un monto acumulado superior a un millón de dólares de los Estados Unidos de America (USD 1,000,000.00) o su equivalente en Lempiras… vigente al 31 de diciembre del ejercicio que se informa,… según lo establece el Acuerdo DEI-SG-004-2016 en su Acuerda Primero". Sanciones: "La aportación de datos falsos o manifiestamente incompletos o inexactos… conlleva a la infracción establecida en el Art. 18 numeral 1) del Decreto 232-2011, sancionado con una multa de diez mil dólares de los Estados Unidos de América (USD10,000.00) en conformidad al Art. 19, numeral 1" (+ Estudio/DJ incoherence same fine p.71; fictitious foreign IDs) | 545 Ayuda: the normative frame (CT Art. 113; TP law D. 232-2011 Arts. 17/20; Reglamento 027-2015 Arts. 30-31; DEI-SG-004-2016; OECD 2010/2017/2022); filer matrix — median/large taxpayers with related-party operations always; any filer with special-benefit-regime (D. 117-2021 — identity question, OQ) or tax-haven-resident counterparts; small taxpayers only above USD 1,000,000 accumulated per FY at the 31-dic BCH parity (DEI-SG-004-2016 Acuerda Primero); USD 10,000 fine for false/incomplete/inexact data, Estudio-vs-DJ incoherence and fake foreign IDs (D. 232-2011 Arts. 18.1/19.1) | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-pp.2-8, 71 (EV63:EVID-176) |
| LB-002 | Ayuda 545 (63_), f. Plazo + búsqueda + recomendación: "El artículo 31 del Reglamento de la Ley de Regulación sobre Precios de Transferencia establece que el plazo para presentar la Declaración Jurada Informativa Anual sobre Precios de Transferencia para los obligados tributarios con período fiscal que coincida con año civil calendario es el 30 de abril o siguiente día hábil de cada año. Para los obligados tributarios con período fiscal especial debe ser a más tardar dentro de los 3 meses siguientes al cierre del período fiscal"; alta "en la casilla 'Año desde' deberá ingresar el período 2025… 'Añadir obligación'"; búsqueda "en la casilla 'Período' deberá seleccionar 202501" | 545 deadline: Apr-30 or next business day (calendar FY); special fiscal periods → within 3 months after close; the ANNUAL form is keyed by a six-digit period code YYYYMM ("202501" = FY2025 January-tag, OVI convention) | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-pp.5, 9-12, 78-80 (EV63:EVID-177) |
| LB-003 | Ayuda 545 (63_), 4./4.1 Elaboración: "está conformado por tres secciones: • Sección A-Información General de las Operaciones Relacionadas • Sección B-Información Específica del Declarante • Sección C-Información de Precios de Transferencia"; 56 códigos de operación ("1 Venta de bienes producidos… 9 Ingresos por licencias, patentes… 11 Financiamiento recibido… 24 Documentos y cuentas por cobrar… 44 Pago de dividendos o retiro de utilidades… 53 Venta de Divisas / 54 Compra de Divisas / 55 Fideicomisos / 56 Adquisición de Instrumentos Financieros"); detalle-key mapping (p.18): Tangibles 1,2,20,21,26,27,45,46 · Intangibles 9,22,34,47 · Servicios/Comisiones 3-8,10,28-33,35,51,52 · Financiamiento 11,36 · Intereses 12,37 · Cuentas Corrientes Mercantiles 24,49 · Otros 25,50 · Divisas 53,54 · Fideicomiso 55 · Instrumentos Financieros 56; casillas comunes: Tipo de Operación, Código del país, Identificación Tributaria ("identificación tributaria extranjero… números, letras, y signos"; "Cuando se consigne país Honduras… el número RTN… 14 dígitos"), Nombre o razón social, Actividad económica, Tipo de relación, Naturaleza, Moneda, Monto; Naturaleza: "1. Ingresos… códigos 1-10, 13-22, 25, 37,51, y 53 / 2. Egresos… 12, 26-35, 38-43,45-47, 50, 52, y 54 / 3. Activos… 24,36 y 56 / 4. Pasivos… 11 y 49"; relación 17 códigos ("1 Declarante es matriz o tiene el 50% o más de la propiedad de la contraparte; 2 Declarante es filia[l]…"), criteria per "Arts. 11, 12 y 13 del Acuerdo 027-2017" [sic — 027-2015 elsewhere, OQ] | 545 Sección A contract: three-section form; per-operation line = tipo (1-56) × counterparty (country / tax-ID free-format foreign, RTN 14-digit when Honduras / name / activity) × relación (1-19) × naturaleza (1-4 by op code) × moneda × monto; ten detail blocks keyed on operation type; relación criteria sourced in Reglamento Arts. 11-13 (the "027-2017" print = misdate/typo conflict) | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-pp.13-24 (EV63:EVID-178) |
| LB-004 | Ayuda 545 (63_), 4.1.11 detail annexes: comparability — "Parte Analizada… Análisis Global o Segmentado… Indicador de Rentabilidad… Resultado de operación Positivo y Negativo… como porcentaje con dos (2) posiciones decimales" ("no es necesario expresarlo con signo negativo"); "Ajuste de Comparabilidad 1, 2 y 3:… a) Ajuste de capital circulante; b) Ajuste de Diferencias Contables; y c) Ajuste de Riesgo País"; "Rango Intercuartil (primer, segundo y tercer cuartil)" "establecido en el artículo 26 del Acuerdo No 027-2015, considerando el rango ínter cuartil y la mediana"; intereses (12/37): "Monto del Financiamiento… el saldo inicial es al 01 de enero… con dos (2) posiciones decimales"; catálogo de tasas referenciales 33 códigos: "1 Euribor 1 Mes… 30 Pibor (Paris Interbank Offered Rate) / 31 Prime USA / 32 Short Term Prime Rate, Yen / 33 Otras"; "Adición spread / Resta spread… si el spread sea variable… el promedio anual"; "Garantía:… 'Sí'… especificar [texto libre]"; financiamiento: "Tipo de Tasa de Interés… fija o variable… Porcentaje de tasa… (códigos 2 o 3…)"; cuentas corrientes mercantiles (24/49) = ledger completo saldo inicial→movimientos→saldo final | The 10 annex schemas (tangibles; servicios/comisiones; intangibles; financiamiento; intereses; cta-cpta mercantiles; otros ingresos/egresos; divisas; fideicomisos; instrumentos financieros): every analytical annex carries the OECD-style comparability set + interquartile range pre/post adjustment (mediana per 027-2015 Art. 26) + ajustes 1-3; the 33-item Euribor/Pibor/Prime reference-rate catalog is fixed data; the cta-cta block is a full current-account movement ledger anchored at 01-enero | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-pp.24-61 (EV63:EVID-179) |
| LB-005 | Ayuda 545 (63_), 4.2 Sección B + 4.3 Sección C: resultado "calculado a partir de los estados financieros globales" (Art. 19.1 sanction note); Ajuste PT: "Ajuste de precios de transferencia a los Ingresos / a las Deducciones… en lempiras… Dicha diferencia se debe llevar también a las casillas de Ajuste de Precios de Transferencia de la Declaración del Impuesto Sobre la Renta, aumentando la base imponible… Cuando se omitan los valores de ajuste de precios de transferencia en las casillas de la Declaración del Impuesto Sobre la Renta, el valor migrará automáticamente a las casillas correspondientes aumentando la base imponible"; "Reorganización empresarial… transferido funciones, activos y/o riesgos a una entidad relacionada"; Grupo Económico: "Indique 'Sí' si… no está clasificado como un 'Grupo Multinacional Excluido'"; local → "'Grupo Económico. Nombre de la casa matriz' y… 'RTN casa matriz',… obligatorio"; multinacional → "'Pertenece a un Grupo Multinacional obligado a presentar Reporte País por País'… 'Entidad Informante del Reporte País por País' y… 'País de la Entidad Informante'" — "de acuerdo con los criterios establecidos en el Numeral I y II del Acuerda Segundo del Acuerdo SAR-653-2023"; "Número de empleados… no admite letras, caracteres o decimales"; Sección C: "¿La Declaración Jurada Informativa Anual Sobre Precios de Transferencia, fue elaborada con el Estudio de Precios de Transferencia?" → "Nombre de consultora o especialista… País de origen… 'Número de Identificador Tributario o Mercantil Extranjero'… país 'HN-Honduras'… casilla 'RTN Consultar'… RTN válido"; Resumen = RTN, nombre, período + totales (transacciones, monto) | 545 Secciones B/C: the ONLY annual informative that writes back into a determinativa — the TP adjustment (ingresos/deducciones) must be mirrored in the ISR DJ adjustment casillas and migrates automatically into empty DJ casillas increasing the taxable base; business-reorganization disclosure; grupo-económico profile (local: matriz RTN; multinational: country + foreign ID + CbCR flags per SAR-653-2023 Acuerda Segundo I-II — instrument unacquired, LEAD); Estudio-PT author registry; resumen totals per operation line | `hn/sources/63_Ayuda_precios_transf_545.pdf` | 63-pp.62-79 (EV63:EVID-180) |
| LB-006 | Ayudas 63_/64_/65_/66_ (shared chassis): "Única modalidad para la presentación a través de la Oficina Virtual (OVI)." grounded on "acuerdo SAR 236-2024, Primero…/Segundo…"; alta (63_): "en la casilla 'Impuestos' deberá seleccionar la opción '545 - Declaración Informe P.T.'; en la casilla 'Año desde' deberá ingresar el período 2025… 'Añadir obligación'"; juramento "Jura la exactitud y veracidad de la presente declaración"; acuse "se genera el PDF del acuse… muestra el código único de este y su respectivo QR"; estados "Original OT. Aprobada OT" / "Rectificativa OT Aprobada OT" con histórico; Excel "descargar detalle en formato Excel"; rectificativa per CT Art. 117 loading the original editable (63_ "en modo editable"; 64_ edits "socio por uno"); 63_ adds "Copiar datos… con información del período anterior" | The four forms ride ONE OVI chassis: self-enrollment per código+Año, pendiente→realizar→presentar→acuse(QR)→rectificativa lifecycle, per-CT-117 rectification reloading the original editable, historical original/rectificativa registry, Excel detail export; 545 adds copy-previous-year data. Chassis CONTRACT owned by fiscal-reporting file 01 (F1) and consumed by id | `hn/sources/63_Ayuda_precios_transf_545.pdf` + `hn/sources/64_Ayuda_socios_utilidades_541.pdf` + `hn/sources/65_Ayuda_alquileres_542.pdf` + `hn/sources/66_Ayuda_municipalidades_543.pdf` | 63-pp.5-13; 64-pp.5-15; 65-pp.5-16; 66-pp.4-16 (EV63:EVID-175) |
| LB-007 | Ley ISR (D.L. 25-1963, texto consolidado SAR-07-2025), Art. 47: "Las empresas de negocios de cualquier clase que estén establecidas o se establezcan en el futuro, así como las Instituciones de Crédito, las Capitalizadoras y Compañías de Seguros que funcionen en el país, y que distribuyan dividendos entre sus accionistas, estarán en la obligación de suministrar a la Administración Tributaria, antes del último día del mes de febrero de cada año, un informe que contenga el nombre de sus accionistas, de acuerdo con su registro, el número de acciones de que sean poseedores cada uno de ellos, el valor nominal de cada acción, el porcentaje de dividendos distribuidos por acción en los semestres anteriores a su informe y el monto total en efectivo pagado o a pagar a cada accionista." (quote carried by 64_ p.4, verified VERBATIM = 01_ Art. 47 pp.29-30; 64_ also cites CT Arts. 62.1, 63.2/63.6 as base legal — content not separately extracted, anchor only) | ISR Art. 47: every business (plus credit institutions, capitalization and insurance companies) distributing dividends must supply the Administration, before the last day of February, a shareholder report: name, number of shares, nominal value per share, per-semester dividend percentage per share and total cash paid or payable per shareholder | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` (carried via `hn/sources/64_Ayuda_socios_utilidades_541.pdf`) | 01_ Art. 47 pp.29-30; 64-pp.4-6 (EV63:EVID-181) |
| LB-008 | Ayuda 541 (64_), Elaboración + Recomendaciones: per-socio card "1. RTN:… del socio al cual se le otorgan dividendos o participaciones en utilidades… 2. Participación social en lempiras:… el monto de capital social aportado y pagado por el socio, considerar… Artículo No.143 del Código de Comercio: 'La distribución de las utilidades se hará en proporción al importe exhibido de las acciones.' 3. Participación en %: Valor porcentual del aporte de capital social… con relación al total… registrado en libros. 4. Nacionalidad: País de origen del socio. 5. Importe de participación utilidades: Monto de utilidades distribuidas y que gozara el socio para el período que se informa." — "se debe registrar socio por socio"; plazo Rec. 1: "a más tardar el ultimo día del mes de febrero del año siguiente al período que informa"; Rec. 6: "los datos relacionados con el capital social aportados por los socios… deben coincidir con los montos reflejados a nivel de escritura pública y balance general aprobado por la asamblea de accionistas" | 541 form: five per-socio fields (RTN; paid-in capital HNL per Código de Comercio Art. 143 proportionality; capital %; nationality; distributed profits) entered socio by socio; deadline per the Recomendación = last day of February of the following year (statute says "antes del último día" — 1-day drift conflict); capital data must reconcile with the escritura pública and the assembly-approved balance sheet | `hn/sources/64_Ayuda_socios_utilidades_541.pdf` | 64-pp.4-6, 10-12, 20 (EV63:EVID-181) |
| LB-009 | Ayuda 542 (65_), Generalidades + Elaboración + Recomendaciones: channel anchor "Acuerdo No. SAR-236-2024 Ordinal Décimo Tercero — Se establecen las siguientes Declaraciones Juradas Informativas con sus respectivos códigos… 29) 542-Declaracion Jurada Informativa Contratos de Alquileres"; scope "Acuerdo No. 034/99 Ordinal Sexto — La Declaración Contratos de Alquileres, será proporcionáda por todos los contribuyentes que declaren ingresos por éste concepto mayores a Lps. 120,00[0].00 y deberá comprender la información respecto de terceros que les arrienden locales comerciales o habitacionales."; plazo cuerpo: "La declaración deberá presentarse dentro de los tres meses siguientes al cierre del ejercicio fiscal" vs Rec. 1: "tiene como plazo máximo de presentación al 30 de marzo del año siguiente al cierre del ejercicio fiscal"; form: "clic en la opción '+ Añadir contrato de alquiler'. En este apartado, se deberán completar los datos del contrato de alquiler 1, tales como el RTN, el domicilio del local, el valor de alquiler anual y el plazo de alquiler (en meses)" con nota "1 Los datos corresponden al arrendatario (inquilino)."; contador "la cantidad de contratos de alquiler que se han ingresado" | 542: lessor-side annual inform whose data subjects are the LESSEES — per-contract line = arrendatario RTN + premises address + annual rent + term in months; filing trigger = declarant's rental income > L120,000 (034/99 Sexto; figure OCR-broken — LEAD); deadline 3 months post-close vs "30 de marzo" (drift conflict); contract-count summary | `hn/sources/65_Ayuda_alquileres_542.pdf` | 65-pp.1, 4-7, 10, 17 (EV63:EVID-182) |
| LB-010 | Ayuda 543 (66_), Generalidades + Elaboración: "Es una obligación tributaria mediante la cual las municipalidades deben presentar información a la administración tributaria sobre los contribuyentes municipales cuyos ingresos o volumen de ventas superen los seiscientos mil lempiras (L.600,000.00) anuales. Esta declaración, identificada como 543 -Informativa de Municipalidades, debe presentarse dentro de los tres meses siguientes al cierre del ejercicio fiscal. El incumplimiento… conlleva la aplicación de sanciones establecidas en el Código Tributario, conforme a los artículos 177, 178, 180 y 181 del Decreto 2[2]-97, según lo dispuesto en el Acuerdo 034/99."; per-contribuyente card: RTN; Apellidos y nombre/razón social (auto-llenado); Nombre comercial; "Numero de permiso de operación…"; "Fecha de operación o Vigencia:… fecha de operación o vigencia del tributo a declarar"; Departamento/Municipio/Barrio, colonia o aldea; Teléfono fijo/móvil; "Ingresos declarados: La sumatoria total de ingresos declarados"; "Número de impuesto:… 1 Impuesto Vecinal / 2 Impuesto sobre industrias, comercio y servicios / 3 Impuesto por Extracción o explotación de recursos"; período ejemplo "202501" | 543: MUNICIPALITIES are the filers (public-sector third-party reporting entity) reporting each municipal licensee with annual income/sales > L600,000; per-contribuyente card incl. license number, operation/vigencia date, geography, phones, declared income, municipal tax type (3-row catalog); deadline = 3 months post close (no explicit day); sanctions anchored in "Decreto 22-97" Arts. 177/178/180/181 via Acuerdo 034/99 (instrument identity OCR-broken, unacquired) | `hn/sources/66_Ayuda_municipalidades_543.pdf` | 66-pp.4-6, 10-13, 16-17 (EV63:EVID-183) |
| LB-011 | Código Tributario (D. 170-2016 act. D. 180-2020), Arts. 62.1, 63.2 y 63.6 — as cited by the 541 Ayuda base-legal block (64_ p.6): information-duty anchors for the socios/utilidades inform; article texts not separately extracted in the W2 evidence — carried as citation anchors only, never as content | CT information-duty anchors cited for código 541 (no content extraction — semantics owned by the taxation CT/T11 zone; cited here only as the Ayuda's own base-legal chain) | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | as cited by 64-§I.6 p.6 (EV63:EVID-181) |
| LB-012 | D. 117-2021 (89_), Art. 1 — interpretación auténtica del numeral 1) del Art. 113 CT: la disposición "no está incluyendo a los regímenes especiales que gozan de beneficios fiscales dentro de las operaciones que determinan las obligaciones tributarias relacionadas con los precios de transferencia, ya que la intención del legislador se orienta a que tales obligaciones aplican únicamente para las personas naturales o jurídicas domiciliadas o residentes en Honduras, que estén relacionadas, vinculadas o asociadas con empresas acogidas a regímenes especiales y no a estas últimas." (vigencia = publicación, 14-feb-2022) | Authentic interpretation of CT Art. 113.1 (EVID-334, V-HN1 evidence pass): the special-regime beneficiaries themselves are NOT inside the TP-determination operations — TP obligations apply only to Honduran-domiciled/resident persons RELATED to special-regime enterprises; confirms the 545 filer-side trigger of FR-326(c) and resolves the `63_ OQ-4` D. 117-2021 identity question (the Ayuda cites the interp as the phrase's carrier) | `hn/sources/89_Decreto_117-2021_interp_Art113_CT.pdf` | Art. 1 pp.1-2 (EV89:EVID-334; vigencia EVID-336) |
| LB-013 | **THE TP TRIPLE ACQUIRED W9** — D. 232-2011 (`140_`, G 32,691 10-dic-2011, vigencia 1-ene-2014 [Art. 22 year OCR-damaged, 3-witness coherence; `140_` OQ-2]) + Acuerdo 027-2015 (`141_`, G 33,837 18-sep-2015, 40 arts XI títulos; Presidencia refrendo quirk) + D. 62-2019 (`142_`, G 35,077 19-oct-2019 — catalog "34,224" corrected, EV142:EVID-534): law = related-party definition Art. 3.3 a-f (situations) + >50% grado; arm's-length duty Art. 5; DEI adjustment faculty Art. 6; comparability+aggregation Art. 7; METHOD CATALOG Art. 8-9 (mejor método + five OECD + a sixth alternative; intercuartil/mediana mechanics); Art. 10 export-commodity quote method + modulación (re-read by D. 62-2019 after the reglamento's Art. 23.1 had hardened it); Arts. 11-16 recalificación/APAs ≤5 ejercicios/doble imposición; Arts. 17-20 documentation duty + THE SANCTION TABLE (US$10,000 / 15% / 30%-or-US$20,000 / US$5,000) + electronic systems; reglamento = THE VINCULACIÓN CRITERIA Arts. 11-13 (8 supuestos incl. kinship, exclusivity agents, financial dependence; participation = >50% capital OR capacity to influence; unidad de decisión) + Arts. 29-32 THE 545 ANCESTOR (filer matrix, **threshold DELEGATION num. 4 → DEI-SG-004-2016**, deadlines Apr-30/+3m, FY2014 transition 18-dic-2015; estudio on-request per CT Art. 48, NOT filed) + Art. 26 eight-step intercuartil + Art. 38 OECD incorporation clause + Art. 39 custodian (Depto. Fiscalización Internacional y PT) | The law-side semantics OQ-006 waited for: methods/criteria/sanctions/deadlines all statute-pinned; the ≤USD 1M pequeño gate's true instrument = DEI-SG-004-2016 (still unacquired — the ONE remaining TP lead) | `hn/sources/140_Gaceta_32691_Decreto_232-2011_Precios_Transferencia.pdf` + `hn/sources/141_Gaceta_33837_Acuerdo_027-2015_Regl_Precios_Transferencia.pdf` + `hn/sources/142_Decreto_62-2019_interp_Art10_232-2011.pdf` | EV140:EVID-524..529; EV141:EVID-530..533; EV142:EVID-534/535 |
| LB-014 | **THE TP GATE INSTRUMENT ACQUIRED W10** — Acuerdo **DEI-SG-004-2016** (`150_`, G 34,018 27-abr-2016; acuerdo dated 08-ene-2016, Ministra Guzmán Bonilla; vigencia = publication day → 27-abr-2016, QUINTO): exercises Reglamento-Art.-30-num.-4's delegation — **ACUERDA PRIMERO: pequeños contribuyentes with local and/or foreign related-party operations accumulating > USD 1,000,000 (print: "1,000.000,00") or Lempira equivalent "de acuerdo a la paridad cambiaria" (NO rate/date printed — the 31-dic/BCH specificity is the 63_ manual's elaboration; OQ-009 carries the feed decision) file the DJIAPT**; SEGUNDO = Art. 31 deadlines apply; TERCERO = filing notifies the Art. 8 method; CUARTO = the Ayuda Manual is an integral part (DEI may modify format/content — the 63_ manual's own authority); QUINTO vigencia. **NEGATIVE (grep-verified): NO safe-harbour/operational-simplification content anywhere in the acuerdo** — OQ-005 resolved flag-only | FR-326(b)/FR-327's threshold row now statute-anchored directly (was Ayuda-only) | `hn/sources/150_Gaceta_34018_Acuerdo_DEI-SG-004-2016_PT_umbral.pdf` | EV150:EVID-578..586 |
| LB-015 | **THE CbCR REGIME ACQUIRED W10** — Acuerdo **SAR-653-2023** (`151_`, G 36,489 Sección A 19-mar-2024; acuerdo date printed 29-dic-2023, catalog "18-dic" = slip): the OECD-aligned **Informe País por País** — PRIMERO Defs. 1-13 (Grupo anchored to Ley-232-2011-Art. 3.3; Grupo Multinacional two-limb test; **Def.-3 Grupo Multinacional Excluido = prior-FY consolidated revenues < EUR 750M `o` L19,000M (words-only lempira leg, no FX anchor — OQ-022; never derive)**; Entidad Informante/Matriz Última/Matriz Subrogada; Omisión Sistemática); SEGUNDO duties: Num. I Honduran-resident UPE files (LIVE) / Num. II constituent-entity local filing (i + ii.a-c triggers + one-filer designation) **SUSPENDED FROM THE OUTSET by the TRANSITORIO until a Director-Ejecutivo comunicado restates it — encode suspended, never operative (OQ-021)** / Num. 3 surrogate exemption (5 conditions a-e) / Num. 4 UPE-jurisdiction-threshold no-obligation (≤ EUR-750M-equivalent national currency at Jan-2015 FX; NO express exchange-agreement condition printed); TERCERO notification by 31-dic of the reportable FY (digital to Director Ejecutivo); QUINTO presentation = FY-close+12m, XML; NOVENO first reportable FY = 2025 (test year FY2024); sanctions + use-limits chapters | New FREP cluster (the 545's CbCR sibling): CbCR duty rows pre-allocated for the next synthesis pass (this file's FR range is closed at FR-360 — append-only extension to be allocated then); `63_ OQ-6` "Numeral I y II del Acuerda Segundo" citation now text-pinned | `hn/sources/151_Gaceta_36489_Acuerdo_SAR-653-2023_CbCR.pdf` | EV151:EVID-587..596 |

## 3. Functional Requirements

### 3.1 Código 545 — obligation, calendar, chassis, sanctions

- **HN-FREP-FR-326:** The system shall compute the 545 filing-obligation
  trigger matrix per filer and fiscal year: (a) *medianos* and *grandes
  contribuyentes* (mid-size and large taxpayers) — obliged whenever any
  commercial or financial operations with related parties exist; (b)
  *pequeños contribuyentes* (small taxpayers) — obliged only when
  operations with local and/or foreign related parties accumulate, within
  one fiscal year, more than USD 1,000,000 (FR-327); (c) any filer
  segment — obliged when operations exist with counterparts *amparadas en
  regímenes especiales que gocen de beneficios fiscales* (special-regime
  benefit holders — identity RESOLVED V-HN1: the Ayuda's "según Decreto No
  117-2021" = corpus `89_`, whose Art. 1 interprets CT Art. 113.1's own
  clause; per that interpretation the TP obligation reaches only the
  DOMICILED/RESIDENT related parties of special-regime enterprises, never
  the regime entities themselves by virtue of their own regime status —
  OQ-004 resolved) or with residents of *países catalogados como paraíso
  fiscal* (tax-haven-listed countries — catalog = dated config, source
  instrument unacquired). (LB-001; LB-012; EV63:EVID-176; EV89:EVID-334)
- **HN-FREP-FR-327:** The system shall store the pequeño-segment threshold
  as a DATED parameter row — USD 1,000,000 accumulated per fiscal year,
  with the lempira equivalent resolved at the BCH exchange rate *vigente
  al 31 de diciembre del ejercicio que se informa* (in force on Dec-31 of
  the declared FY — snapshot-on-write, D-H2) — and shall EXCLUDE pequeños
  at or below USD 1,000,000 accumulated ("igual o inferior" per the
  manual; the instrument's own print reads "monto acumulado superior a un
  millón de Dólares... o su equivalente en Lempiras de acuerdo a la
  paridad cambiaria" — **W10: instrument ACQUIRED as `150_`, statute
  anchor upgraded; the 31-dic/BCH rate-day is the 63_ manual's
  elaboration, the acuerdo itself names no rate date — OQ-009's feed
  decision unchanged, valid_from 27-abr-2016**).
  (LB-001; LB-014; EV63:EVID-176; EV150:EVID-580)
- **HN-FREP-FR-328:** The system shall schedule 545 with the window row
  due April-30 of the year following the declared FY, shifting to the
  next business day when April-30 falls non-hábil ("el 30 de abril o
  siguiente día hábil"), and shall extend to at most 3 months after the
  close of an AT-authorized special fiscal period (special-period close
  date consumed from taxation/01 HN-TAX-FR-016 by id); annual records
  shall be keyed by the OVI period code YYYYMM with month-tag "01"
  (FY2025 → "202501"), as DATED per-FY rows (D-H2), never a rolling
  computation. (LB-002; EV63:EVID-177)
- **HN-FREP-FR-329:** The system shall ride all four forms of this file
  (541/542/543/545) on the shared OVI chassis owned by fiscal-reporting
  file 01 (cluster F1) consumed BY ID — alta de obligación (545 selection
  "545 - Declaración Informe P.T." + "Año desde" + "Añadir obligación"),
  pendiente→borrador→juramento→presentación lifecycle, acuse PDF with
  código único + QR, "Original OT. Aprobada OT" / "Rectificativa OT
  Aprobada OT" states with histórico, per-CT-Art.-117 rectificativa
  reloading the original editable, Excel detail export — and shall
  provide the 545-specific chassis features evidenced: copy-previous-year
  data into the new period's draft, and the resumen totals (RTN, nombre,
  período, total transacciones, total monto). No chassis mechanic is
  re-derived in this file. (LB-006; EV63:EVID-175/180)
- **HN-FREP-FR-330:** The system shall carry the D. 232-2011 sanction
  constants as DATED data for validation messaging (collection mechanics
  = CT/T11 zone, not here): USD 10,000 for (a) false or manifestly
  incomplete/inexact data (Art. 18.1 / Art. 19.1), (b) Estudio-vs-DJ
  incoherence ("aportar datos inexactos o incompletos", 63_ p.71), and
  (c) fictitious foreign tax identifications.
  (LB-001; EV63:EVID-176)

### 3.2 Código 545 Sección A — the operation-line contract

- **HN-FREP-FR-331:** The system shall implement 545 as a three-section
  form — *Sección A-Información General de las Operaciones Relacionadas*
  (related-party operations), *Sección B-Información Específica del
  Declarante* (declarant-specific), *Sección C-Información de Precios de
  Transferencia* (TP-study information) — with Sección A populated by
  per-operation lines (FR-332..339). (LB-003; EV63:EVID-178)
- **HN-FREP-FR-332:** The system shall carry the 56-row operation-type
  catalog as reference data (seed sidecar `tp_operation_types.csv` at
  implementation; labels only partially evidenced — codes 1, 9, 11, 24,
  44 and 53-56 verbatim, remaining labels pending re-extraction from
  `63_` pp.15-17 — never invented), and shall key every Sección A line
  by this catalog. (LB-003; EV63:EVID-178)
- **HN-FREP-FR-333:** The system shall validate counterparty
  identification per line: when the declared country is Honduras, the tax
  identification shall be an RTN of exactly 14 digits; for foreign
  counterparts the identification shall be free-format "números, letras,
  y signos" (numbers, letters and signs) with no HN-format enforcement;
  nombre o razón social and Actividad económica (free text, ISIC A-L
  examples printed) are recorded per line.
  (LB-003; EV63:EVID-178)
- **HN-FREP-FR-334:** The system shall carry the *tipo de relación*
  (relatedness type) catalog with the printed 17 code descriptions
  (e.g. code 1 "Declarante es matriz o tiene el 50% o más de la
  propiedad de la contraparte" — declarant is parent or holds ≥ 50%
  ownership of the counterpart), shall key lines by codes 1-19 with code
  18 absent from the evidenced table (table runs 17 → 19 — VERIFY,
  OQ-001), and shall record — without encoding — that the underlying
  vinculación criteria live in Reglamento Arts. 11-13 (Acuerdo
  027-2015; criteria table image-only, OQ-007; the 1963 statutory frame
  consumed from taxation/01 HN-TAX-FR-006 by id).
  (LB-003; EV63:EVID-178)
- **HN-FREP-FR-335:** The system shall derive the *naturaleza* (nature)
  classification from the operation type per the printed map — 1
  Ingresos (codes 1-10, 13-22, 25, 37, 51, 53), 2 Egresos (12, 26-35,
  38-43, 45-47, 50, 52, 54), 3 Activos (24, 36, 56), 4 Pasivos (11, 49)
  — with the evidenced map covering 52 of 56 codes (23, 44, 48, 55
  unlisted — VERIFY, OQ-008). (LB-003; EV63:EVID-178)
- **HN-FREP-FR-336:** The system shall record every operation amount
  (*monto*) in lempiras converted at the BCH exchange rate of the
  transaction date (per-transaction parity), as a discipline DISTINCT
  from the USD-1M threshold's 31-dic parity (FR-327) — the two rate
  dates are deliberately different and shall never share a resolved
  value (D-H2 snapshot-on-write both). (LB-003; EV63:EVID-178/176)
- **HN-FREP-FR-337:** The system shall record the TP *método* per line
  from the OECD-five + Art. 10 D. 232-2011 + alternative-methods
  taxonomy printed in the Ayuda (exact value list partially
  screenshot-only — config-gapped with FR-343), mandatory for the
  operative ranges per the Ayuda's instructions; method SEMANTICS (which
  method fits which operation) are law-side content owned by the
  unacquired D. 232-2011/027-2015 family — never derived here.
  (LB-003; EV63:EVID-178)
- **HN-FREP-FR-338:** The system shall drive the conditional detail
  blocks from the operation type per the printed mapping — Detalle de
  Tangibles (1, 2, 20, 21, 26, 27, 45, 46); Intangibles (9, 22, 34,
  47); Servicios o Comisiones (3-8, 10, 28-33, 35, 51, 52);
  Financiamiento recibido u otorgado (11, 36); Intereses (12, 37);
  Cuentas Corrientes Mercantiles (24, 49); Otros Ingresos y Otros
  Egresos (25, 50); Divisas (53, 54); Fideicomiso (55); Instrumentos
  Financieros (56) — exactly ten annex schemas, instantiated only when
  an informed operation type requires them.
  (LB-003; EV63:EVID-178)

### 3.3 Código 545 — the ten detail annexes

- **HN-FREP-FR-339:** The system shall provide the comparability field
  group as a template reused across the analytical annexes — *Parte
  Analizada* (tested party), *Análisis Global o Segmentado*, *Indicador
  de Rentabilidad* (profitability indicator), *Resultado de operación*
  Positivo y Negativo as a percentage with two decimals (losses go in
  the negative casilla, "no es necesario expresarlo con signo negativo"
  — no minus sign stored), and *Rango Intercuartil* reported as primer,
  segundo y tercer cuartil (pre- and post-adjustment), "considerando el
  rango ínter cuartil y la mediana" per Acuerdo 027-2015 Art. 26 (lead
  instrument). (LB-004; EV63:EVID-179)
- **HN-FREP-FR-340:** The system shall record the three *Ajustes de
  Comparabilidad* per analysis — 1 *Ajuste de capital circulante*
  (working capital), 2 *Ajuste de Diferencias Contables* (accounting
  differences), 3 *Ajuste de Riesgo País* (country risk) — plus the
  "otros ajustes" capacity evidenced, feeding FR-339's post-adjustment
  interquartile range. (LB-004; EV63:EVID-179)
- **HN-FREP-FR-341:** The system shall carry the 33-row reference-rate
  catalog as fixed reference data (seed sidecar `tp_reference_rates.csv`
  at implementation; endpoints evidenced verbatim — 1 "Euribor 1
  Mes" … 30 "Pibor (Paris Interbank Offered Rate)", 31 "Prime USA",
  32 "Short Term Prime Rate, Yen", 33 "Otras"; interior rows 2-29
  pending re-extraction — never invented), and shall implement the
  interests-annex mechanics: *Tipo de Tasa de Interés* fija o variable,
  *Porcentaje de tasa* (2 decimals), *Adición spread / Resta spread*
  (variable spread → annual average, "el promedio anual"), *Monto del
  Financiamiento* with the opening balance "al 01 de enero", intereses
  percibidos/pagados (2 decimals), comisiones u otros cargos, and
  *Garantía* Sí → free-text specification.
  (LB-004; EV63:EVID-179)
- **HN-FREP-FR-342:** The system shall implement the *Cuentas Corrientes
  Mercantiles* annex (op types 24/49) as a related-party current-account
  movement ledger: saldo inicial (01-enero) → débitos/créditos in
  money, in kind and other → saldo final, reconcilable with the
  related-party balance-sheet panels of the 535 EEFF report (file 06,
  cluster F6 — consumed by id, no re-derivation).
  (LB-004; EV63:EVID-179)
- **HN-FREP-FR-343:** The system shall treat every screenshot-only
  dropdown catalog as CONFIG-GAPPED reference data — tipo de servicio
  1-13, criterio de cálculo del precio/comisión/regalía, tipo de
  comparable, indicadores de rentabilidad, periodicidad de pago de
  intereses, tipo de documento de respaldo, tipo/tipo de fideicomiso,
  tipo de instrumento financiero, modalidad de la operación — loading
  each only from an extracted value list and never from guesswork
  (OQ-003). (LB-004; EV63:EVID-179)

### 3.4 Código 545 Secciones B/C — declarant analysis, Ajuste PT write-back, group profile

- **HN-FREP-FR-344:** The system shall record the Sección B *Resultado
  Positivo / Resultado Negativo* — computed "a partir de los estados
  financieros globales" (from the global financial statements) applying
  the profitability indicators, as a percentage with two decimals, with
  the Art. 19.1 sanction note (incoherence with the Estudio = FR-330
  fine) surfaced on the record. (LB-005; EV63:EVID-180)
- **HN-FREP-FR-345:** The system shall implement the *Ajuste de precios
  de transferencia* (transfer-pricing adjustment) pair — ajuste a los
  Ingresos and a las Deducciones, in lempiras — and the WRITE-BACK
  contract into the ISR annual DJ: the difference "se debe llevar
  también a las casillas de Ajuste de Precios de Transferencia de la
  Declaración del Impuesto Sobre la Renta, aumentando la base
  imponible", and "cuando se omitan los valores… el valor migrará
  automáticamente a las casillas correspondientes aumentando la base
  imponible" — i.e. the adjustment feeds the ISR DJ TP casillas
  (consumer: [07_isr-annual-102-103.md](07_isr-annual-102-103.md)
  HN-FREP-FR-230, signed ± line placement owned there), and the
  migration rule fires only into EMPTY DJ casillas: manually entered DJ
  values are never overwritten, and an already-FILED DJ is frozen
  (D-H2.5) — changes reach it only through the chassis rectificativa
  path (file 01 by id). This file owns the adjustment amounts and the
  migration trigger; the DJ lines and base increase are consumed by id.
  (LB-005; EV63:EVID-180)
- **HN-FREP-FR-346:** The system shall record the *Reorganización
  empresarial* (business reorganization) disclosure flag — whether the
  declarant "transferido funciones, activos y/o riesgos a una entidad
  relacionada" (transferred functions, assets and/or risks to a related
  entity). (LB-005; EV63:EVID-180)
- **HN-FREP-FR-347:** The system shall implement the *Grupo Económico*
  (economic group) profile block: first the exclusion screen ("Indique
  'Sí' si… no está clasificado como un 'Grupo Multinacional Excluido'");
  LOCAL group → "Nombre de la casa matriz" + "RTN casa matriz"
  (obligatory, 14-digit); MULTINATIONAL → país de la casa matriz +
  foreign tax identification of the parent, plus the CbCR flags
  "Pertenece a un Grupo Multinacional obligado a presentar Reporte País
  por País", "Entidad Informante del Reporte País por País" and "País de
  la Entidad Informante", gated "de acuerdo con los criterios
  establecidos en el Numeral I y II del Acuerda Segundo del Acuerdo
  SAR-653-2023" (country-by-country reporting — instrument unacquired,
  criteria = DATED config row, LEAD); the block also carries the
  declarant profile fields "Número de empleados" (integer only — "no
  admite letras, caracteres o decimales") and sitio-web URL.
  (LB-005; EV63:EVID-180)
- **HN-FREP-FR-348:** The system shall implement Sección C's Estudio-PT
  registry: the question "¿La Declaración Jurada Informativa Anual Sobre
  Precios de Transferencia, fue elaborada con el Estudio de Precios de
  Transferencia?"; when Sí → *Nombre de consultora o especialista*,
  *País de origen*, *Número de Identificador Tributario o Mercantil
  Extranjero* (free-format foreign ID), and when the país is
  "HN-Honduras" an RTN validated through the "RTN Consultar" casilla
  (valid 14-digit RTN). (LB-005; EV63:EVID-180)

### 3.5 Código 541 — socios y participación de utilidades

- **HN-FREP-FR-349:** The system shall generate the 541 obligation for
  every ISR Art. 47 subject — "empresas de negocios de cualquier clase"
  (businesses of any kind) established or to be established in the
  country, plus *Instituciones de Crédito, Capitalizadoras y Compañías
  de Seguros* (credit institutions, capitalization and insurance
  companies) — that distribute dividends among shareholders, sourcing
  the shareholder dataset (name, shares, nominal value, per-semester
  dividend %, total paid per shareholder) from taxation/01
  HN-TAX-FR-022 BY ID with no re-derivation; whether a no-distribution
  year still obliges is config-open (OQ-014).
  (LB-007; LB-011; EV63:EVID-181)
- **HN-FREP-FR-350:** The system shall schedule 541 as a DATED annual
  window row at the end of February of the year following the declared
  FY — defaulting to the operative last-day reading ("a más tardar el
  ultimo día del mes de febrero": Feb-28, Feb-29 in leap years) while
  recording the statute's "antes del último día" drift (Feb-27/28 —
  CONFLICT never resolved silently, OQ-012; leap-year handling per FY
  row, D-H2). (LB-007; LB-008; EV63:EVID-181)
- **HN-FREP-FR-351:** The system shall implement the per-socio card with
  exactly the five evidenced fields — 1 RTN del socio; 2 *Participación
  social en lempiras* (paid-in capital per Código de Comercio Art. 143
  proportionality); 3 *Participación en %* vs total registered capital;
  4 *Nacionalidad* (país de origen); 5 *Importe de participación
  utilidades* (distributed profits for the period) — entered "socio por
  socio" (shareholder by shareholder, bulk per-socio registration), and
  shall NOT invent the Art. 47 statutory fields absent from the card
  (número de acciones, valor nominal, porcentaje de dividendos por
  acción por semestre, monto total en efectivo) nor a foreign-tax-ID
  field beyond Nacionalidad — that gap is CONFIG (OQ-011, live card may
  differ). (LB-008; EV63:EVID-181)
- **HN-FREP-FR-352:** The system shall enforce the 541 consistency
  checks: (a) per-socio capital amounts "deben coincidir con los montos
  reflejados a nivel de escritura pública y balance general aprobado
  por la asamblea de accionistas" (must match the public deed and the
  assembly-approved balance sheet — reconciliation against registered
  capital data); and (b) per-socio *utilidades distribuidas* reconcile
  with the in-year dividend distributions recorded through the retention
  pipeline (código 113 export owned by
  [02_djimr-retention-declarations.md](02_djimr-retention-declarations.md)
  — consumed by id, linkage validation only).
  (LB-008; EV63:EVID-181)

### 3.6 Código 542 — contratos de alquileres

- **HN-FREP-FR-353:** The system shall implement the 542 per-contract
  record — via the "+ Añadir contrato de alquiler" add-record pattern —
  with the four evidenced fields: arrendatario RTN, *domicilio del
  local* (premises address), *valor de alquiler anual* (annual rent) and
  *plazo de alquiler (en meses)* (term in months), noting the printed
  footnote "Los datos corresponden al arrendatario (inquilino)" (the
  data refer to the LESSEE — the declarant is the lessor), plus the
  contract-count summary ("la cantidad de contratos de alquiler que se
  han ingresado"); no contract dates, lessor-side field or per-month
  amount are described in the source and none shall be invented
  (OQ-018). (LB-009; EV63:EVID-182)
- **HN-FREP-FR-354:** The system shall store the 542 filing trigger as
  a DATED parameter row — the declarant's own rental income for the
  concept exceeding L120,000.00 (Acuerdo 034/99 Sexto; the figure is
  OCR-broken in the only corpus carrier — "Lps. 120,00[0].00" — LEAD
  against the original instrument, OQ-015) — and shall scope the inform
  to contracts with "terceros que les arrienden locales comerciales o
  habitacionales" (third parties renting them commercial or residential
  premises). (LB-009; EV63:EVID-182)
- **HN-FREP-FR-355:** The system shall schedule 542 as a DATED annual
  window row defaulting to the operative Mar-30 of the year following
  the close ("tiene como plazo máximo de presentación al 30 de marzo"),
  while recording the cuerpo's "dentro de los tres meses siguientes al
  cierre" reading (≈ Mar-31) as an open CONFLICT — both dated data,
  never resolved silently (OQ-016). (LB-009; EV63:EVID-182)
- **HN-FREP-FR-356:** The system shall expose the 542↔código-136
  relationship as a FLAG-ONLY cross-check surface — lessee RTNs and
  contract rents may be flagged against the declarant's rental-income
  ledger feeding the cedular-alquiler retention (engine
  HN-TAX-FR-177..181, DJIMR-136 export
  [02_djimr-retention-declarations.md](02_djimr-retention-declarations.md)
  FR-062 — consumed by id) — with NO derivations in either direction:
  the source states no connection (unverified, OQ-017) and the 542
  registry must never feed or validate the 10% cedular retention until
  an instrument says so. (LB-009; EV63:EVID-182)

### 3.7 Código 543 — informativa de municipalidades

- **HN-FREP-FR-357:** The system shall model 543 with the MUNICIPALITY
  as the filing entity (a public-sector third-party filer profile — the
  reporting corporation, not the taxpayer) reporting every
  *contribuyente municipal* (municipal licensee) whose "ingresos o
  volumen de ventas" exceed the DATED threshold L600,000.00 per year
  (Acuerdo 034/99 anchor; threshold = dated row, D-H2).
  (LB-010; EV63:EVID-183)
- **HN-FREP-FR-358:** The system shall implement the per-contribuyente
  card: RTN; apellidos y nombre/razón social (auto-filled by the
  system); nombre comercial; *Número de permiso de operación*
  (municipal operating license); *Fecha de operación o Vigencia* (of
  the tax being declared — semantics unclear, OQ-022); Departamento /
  Municipio / Barrio, colonia o aldea; teléfono fijo and móvil;
  *Ingresos declarados* (sum of declared income); and *Número de
  impuesto* from the 3-row municipal tax catalog — 1 *Impuesto Vecinal*,
  2 *Impuesto sobre industrias, comercio y servicios*, 3 *Impuesto por
  Extracción o explotación de recursos*. (LB-010; EV63:EVID-183)
- **HN-FREP-FR-359:** The system shall schedule 543 as a DATED annual
  window row of three months following the municipality's fiscal close,
  with NO explicit day encoded beyond the config default Mar-31
  (calendar-year close assumed; the print gives only "dentro de los
  tres meses siguientes al cierre del ejercicio fiscal" — CONFIG,
  OQ-023). (LB-010; EV63:EVID-183)
- **HN-FREP-FR-360:** The system shall carry the 543 non-compliance
  sanctions display as CONFIG-GAPPED: the Ayuda anchors sanctions in
  "los artículos 177, 178, 180 y 181 del Decreto 2[2]-97" (OCR-broken
  identity — pre-170-2016 municipal-era Código Tributario?, unacquired)
  "según lo dispuesto en el Acuerdo 034/99" — no sanction mechanics
  implemented from this anchor (identity LEAD, OQ-020); current
  sanctions procedure = taxation T11 zone by id.
  (LB-010; EV63:EVID-183)
## 4. Data Model

Machine-readable sidecars to be seeded at implementation (NOT written in
this wave — one-file rule): `tp_operation_types.csv` (56 rows; labels
partially evidenced, FR-332) and `tp_reference_rates.csv` (33 rows;
endpoints evidenced, FR-341). CSV discipline per the wave default:
comma-separated, header row, LF endings, print-faithful values, empty
open fields; catalog rows load only from extraction — never guesswork
(FR-343).

**Código 545 DJIAPT:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.tp.declaration (new) | código · fiscal_year · period_key · special_period · state · total_transactions · total_amount | select(545)/year/char(6 "YYYYMM")/boolean/select/integer/monetary | state per file-01 chassis; period_key "202501" convention; resumen totals | FR-328, FR-329 |
| l10n_hn.tp.operation.line (new) | declaration_id · tipo_operacion · pais · identificacion_tributaria · nombre · actividad · tipo_relacion · naturaleza · moneda · monto_hnl · fx_rate · fx_date · metodo | m2o/int/catalog/char/char/char/select(1-19)/select(1-4)/char/monetary/rate/date/select | tipo = 56-row catalog (sidecar); relación 1-19 (18 = gap, OQ-001); naturaleza derived (FR-335); monto converted at per-transaction BCH rate, snapshot-on-write | FR-331..FR-338 |
| l10n_hn.tp.detail.* (new, 10 blocks) | block_key(tangibles · intangibles · servicios · financiamiento · intereses · ctas_mercantiles · otros · divisas · fideicomisos · instrumentos) · typed fields + comparability group (parte_analizada · alcance · indicador · resultado_pos_pct · resultado_neg_pct · ajuste_1/2/3 · intercuartil_q1/q2/q3 pre/post) | select/monetary | instantiated by FR-338 driver; ctas_mercantiles = ledger (saldo_inicial_01_01 → débito/credito dinero/especie/otros → saldo_final); intereses = rate/spread/garantía fields | FR-338..FR-343 |
| l10n_hn.tp.rate.catalog (new) | code (1-33) · name | int/char | seeded from sidecar; evidenced endpoints 1 Euribor 1 Mes, 30 Pibor, 31 Prime USA, 32 STPR Yen, 33 Otras | FR-341 |
| l10n_hn.tp.declaration | resultado_pos_pct · resultado_neg_pct · ajuste_pt_ingresos · ajuste_pt_deducciones · reorganizacion_flag · migrated_to_isr_dj | monetary/monetary/boolean/m2o | Ajuste PT pair + write-back trace (consumer file 07 FR-230) | FR-344..FR-346 |
| l10n_hn.tp.group.profile (new) | exclusion_screen · group_kind(local · multinacional) · matriz_nombre · matriz_rtn · matriz_pais · matriz_tax_id · cbcr_obligated · cbcr_entidad_informante · cbcr_pais_entidad · empleados · sitio_web | boolean/select/char/rtn/catalog/char/boolean/char/catalog/int/url | CbCR criteria = DATED config row per SAR-653-2023 Acuerda Segundo I-II (lead); empleados integer-only | FR-347 |
| l10n_hn.tp.estudio (new) | elaborado_con_estudio · consultora_nombre · pais · identificador_extranjero · rtn | boolean/char/catalog/char/rtn | país "HN-Honduras" → RTN validated | FR-348 |

**Códigos 541/542/543:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.informative.541 (new) | fiscal_year · socio line: rtn · participacion_hnl · participacion_pct · nacionalidad · importe_utilidades | year/rtn/monetary/percent/catalog/monetary | the five evidenced fields only (gap = OQ-011); dataset source taxation/01 FR-022 | FR-349..FR-352 |
| l10n_hn.informative.542 (new) | fiscal_year · contrato line: arrendatario_rtn · domicilio_local · alquiler_anual · plazo_meses | year/rtn/char/monetary/integer | lessee-side; contract-count summary computed | FR-353..FR-356 |
| l10n_hn.informative.543 (new) | fiscal_year · filing municipality (res.partner, public-sector filer profile) · contribuyente line: rtn · nombre(auto) · nombre_comercial · permiso_operacion · fecha_operacion_vigencia · departamento · municipio · barrio · tel_fijo · tel_movil · ingresos_declarados · numero_impuesto | year/m2o/rtn/char/char/char/date/catalog/catalog/catalog/char/char/monetary/select(1-3) | tax catalog: 1 vecinal · 2 industrias/comercio/servicios · 3 extracción/explotación | FR-357..FR-360 |

**Dated parameter rows (l10n_hn.fiscal.parameter):**

| Parameter | Value | valid_from basis | Reference |
|-----------|-------|------------------|-----------|
| tp_pequeno_threshold_usd | USD 1,000,000 (BCH parity @ 31-dic of declared FY) | DEI-SG-004-2016 Acuerda Primero (lead) | FR-327 |
| tp_multa_usd | USD 10,000 | D. 232-2011 Arts. 18.1/19.1 (lead) | FR-330 |
| alquiler_inform_trigger | L120,000.00 (OCR-marked) | Acuerdo 034/99 Sexto (lead) | FR-354 |
| municipal_inform_threshold | L600,000.00 | Acuerdo 034/99 (via 66_) | FR-357 |
| deadline rows 541/542/543 | Feb-28/29 (drift-flagged) · Mar-30 (drift-flagged) · close+3m (day config-gapped) | per-FY dated rows, D-H2 | FR-350/355/359 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = data model, engines and export
payloads living in the LGPL client. No SaaS rows: none of these FRs
touch the thin-client/SaaS split (no DTE-like transmission surface;
OVI/SW chassis export contract = file 01). Model names stable across
Odoo 17/18/19/20; no version-specific behavior exists in these sources.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-326, FR-327 | odoo | l10n_hn.fiscal.parameter + obligation generator | trigger matrix + threshold row | D-H2: threshold lempira value snapshot at 31-dic BCH rate per declared FY; D. 117-2021 identity RESOLVED (OQ-004; interp narrows scope to related parties); paraíso catalog = config-gapped (unacquired) |
| FR-328 | odoo | l10n_hn.fiscal.calendar config | 545 window row + period_key | Apr-30/next-hábil; special-FY +3m consumes taxation/01 FR-016; YYYYMM "01" month-tag |
| FR-329 | n/a (chassis = file 01) | — | — | OVI/SW state machine owned by fiscal-reporting file 01 (F1) by id; this file emits the payload + 545 extras (copy-previous-year, resumen totals) |
| FR-330 | odoo | l10n_hn.fiscal.parameter | sanction constant | USD 10,000 messaging only; collection = CT/T11 |
| FR-331..FR-338 | odoo | l10n_hn.tp.declaration + l10n_hn.tp.operation.line | Sección A engine | Catalog seeds from sidecars; naturaleza derived; FX dual-rate discipline (transaction vs 31-dic); método config-gapped values (OQ-003) |
| FR-339..FR-343 | odoo | l10n_hn.tp.detail.* + l10n_hn.tp.rate.catalog | annex blocks | 10 schemas keyed by FR-338 driver; screenshot-only dropdowns = config gaps; cta-cta ledger reconcilable with file 06 panels by id |
| FR-344..FR-348 | odoo | l10n_hn.tp.declaration + group.profile + estudio | Sección B/C | CbCR criteria dated row (SAR-653-2023 lead); write-back trace flag |
| FR-345 | odoo | l10n_hn.tp.declaration → annual DJ link | ajuste pair + migration trigger | Consumer = file 07 HN-FREP-FR-230 by id; D-H2.5: empty-casillas-only migration, filed DJ frozen, rectificativa path only |
| FR-349..FR-352 | odoo | l10n_hn.informative.541 | per-socio lines | Dataset from taxation/01 FR-022 by id; 113 reconciliation consumed from file 02 by id |
| FR-353..FR-356 | odoo | l10n_hn.informative.542 | per-contract lines | Trigger row OCR-marked (OQ-015); 136 linkage flag-only (file 02 FR-062 by id) |
| FR-357..FR-360 | odoo | l10n_hn.informative.543 + res.partner filer profile | municipal filer + card | Municipality as reporting entity; sanctions display config-gapped (OQ-020) |

Version-regime notes (D12): no instrument in this cluster defines a
version adaptation window; the dated rows above (thresholds, deadlines,
sanction constant, CbCR criteria) each carry their own valid_from basis
and resolve as-of the declared FY (D15/D16 anchor-date +
snapshot-on-write). D18/D19 do not apply: no mid-year go-live or
GL-routing surfaces exist for informative declarations.

## 6. Acceptance Criteria

- **AC-001:** Given a mediano contribuyente with one related-party
  operation of any size, then the 545 obligation is generated; given a
  pequeño with accumulated related-party operations of USD 800,000,
  then no obligation; given a pequeño at USD 1,200,000, then obliged;
  given any filer with an operation against a tax-haven-resident
  counterpart, then obliged regardless of size (FR-326).
- **AC-002:** Given FY2025 with the 31-dic-2025 BCH rate at 25.00, then
  the pequeño threshold resolves to L25,000,000 (snapshot stored); given
  an operation dated 15-mar-2025, then its monto converts at the
  15-mar-2025 rate, never at the 31-dic rate (FR-327, FR-336).
- **AC-003:** Given FY2025 (calendar), then the 545 window row closes
  2026-04-30, shifting to the next business day if non-hábil, and the
  record keys on period "202501"; given a special period closing
  30-sep-2026, then the window closes 2026-12-30 (FR-328).
- **AC-004:** Given a 545 line flagged as false data at validation,
  then the USD 10,000 sanction constant (D. 232-2011 Arts. 18.1/19.1)
  is surfaced in messaging with no collection mechanics (FR-330).
- **AC-005:** Given Sección A lines of tipo 2, 7, 12, 55 and 56, then
  the instantiated detail blocks are exactly Tangibles, Servicios o
  Comisiones, Intereses, Fideicomiso and Instrumentos Financieros
  (FR-338).
- **AC-006:** Given lines of tipo 24, 11, 53 and 54, then naturaleza
  resolves to Activos, Pasivos, Ingresos and Egresos respectively; given
  tipo 44, then naturaleza is flagged unverified rather than guessed
  (FR-335, OQ-008).
- **AC-007:** Given a counterparty with país Honduras and identification
  "0801", then validation fails (14-digit RTN required); given país
  exterior with identification "US-EIN-12-3456789", then the free-format
  value is accepted (FR-333).
- **AC-008:** Given a variable-rate financing line referencing rate code
  31 with a variable spread, then the system requests the annual-average
  spread ("el promedio anual") and stores the spread sign as adición or
  resta (FR-341).
- **AC-009:** Given an analytical annex, then the comparability group
  captures parte analizada, alcance, indicador, resultado as % with 2
  decimals (losses in the negative casilla, no sign stored) and the
  interquartile range pre- and post-adjustment with the mediana rule per
  Acuerdo 027-2015 Art. 26 (FR-339, FR-340).
- **AC-010:** Given a 545 with Ajuste PT a los Ingresos L150,000 and an
  ISR DJ whose TP casillas are empty, then the value migrates into the
  DJ TP lines (consumer file 07 FR-230) increasing the base; given the
  DJ TP casillas manually filled, then no overwrite occurs; given an
  already-filed DJ, then the record is frozen and only the rectificativa
  path (file 01) can change it (FR-345).
- **AC-011:** Given a multinational declarant, then the grupo económico
  block requires país + tax ID of the casa matriz and the CbCR flags per
  the SAR-653-2023 Acuerda Segundo I-II dated config row; given a local
  group, then matriz RTN (14 digits) is required; given empleados
  "125.5", then input is rejected (integer only) (FR-347).
- **AC-012:** Given an FY2025 541 for a company that distributed
  dividends, then the window row closes 2026-02-28 (last-day default,
  drift flagged) and per-socio lines carry exactly the five fields;
  given a socio whose capital mismatches the escritura-approved amount,
  then the consistency check flags the line (FR-350..FR-352).
- **AC-013:** Given a lessor with rental income L150,000 and three
  lease contracts, then 542 is obliged with three lessee-side contract
  lines (RTN, domicilio, alquiler anual, plazo meses) and the
  contract-count summary reads 3; given rental income L100,000, then no
  obligation (FR-353, FR-354).
- **AC-014:** Given an FY2025 542, then the window row closes 2026-03-30
  (operative default) with the "tres meses" (≈ Mar-31) reading carried
  as an open conflict flag (FR-355).
- **AC-015:** Given a municipality reporting a licensee with declared
  income L750,000, then the contribuyente line is included with tax type
  per the 3-row catalog; given a licensee at L500,000, then excluded;
  given the sanctions display, then it renders config-gapped (no D.22-97
  mechanics) (FR-357, FR-358, FR-360).
- **AC-016:** Given an FY2025 543 for a calendar-year municipality, then
  the window row closes 2026-03-31 as the config default with the
  no-explicit-day gap flagged (FR-359).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Relación catalog skips code 18 (origin `63_ OQ-1`, VERIFY): the printed table runs 17 → 19 (63_ pp.20-22) — OCR loss, print defect or genuine catalog gap? Live OVI list needed before freezing the 1-19 key domain (FR-334). | no | Takumi S-HN3 | open |
| OQ-002 | "Acuerdo 027-2017" vs 027-2015 (origin `63_ OQ-2`, CONFLICT): 63_ p.20 cites "Arts. 11, 12 y 13 del Acuerdo 027-2017" while the marco normativo and all other cites say 027-2015 — typo or a 2017 reform instrument? Never resolve silently. | no | acquisition queue | open |
| OQ-003 | Screenshot-only dropdown catalogs (origin `63_ OQ-3`, VERIFY): tipo de servicio 1-13, criterios de cálculo, tipo de comparable, indicadores de rentabilidad, periodicidad, tipo de documento, fideicomiso/instrumento types, modalidad — unobtainable from this source; each stays config-gapped (FR-343). | no | Takumi S-HN3 | open |
| OQ-004 | "Decreto No 117-2021" benefits regime (origin `63_ OQ-4`, CONFLICT) → **RESOLVED V-HN1 (2026-08-20):** corpus `89_` D. 117-2021 IS the cited instrument — its Art. 1 interprets CT Art. 113.1's own clause "y aquellas amparadas en regímenes especiales que gocen de beneficios fiscales", and the Ayuda's "según Decreto No 117-2021" attributes that quoted phrase to the interp that reprints it (no separate benefits law exists). Effect encoded in FR-326(c) via LB-012/EVID-334: TP obligation reaches only the domiciled/resident RELATED parties of special-regime enterprises, never the regime entities themselves. | no | — | resolved |
| OQ-005 | Safe Harbour scope (origin `63_ OQ-5`) → **RESOLVED W10 (negative finding):** all three cited legs now in corpus — 027-2015 Art. 38 = OECD-Directrices incorporation clause (EV141:EVID-533), OECD §4.93-4.95 = the Guidelines' own text (external reference), and **DEI-SG-004-2016 (`150_`, EV150:EVID-578..586) contains NO safe-harbour/operational-simplification content whatsoever** (grep-verified: PRIMERO..QUINTO = threshold/deadlines/method-notification/manual-integration/vigencia only). No safe-harbour regime exists in HN TP law — flag-only forever unless a NEW instrument creates one. | no | — | resolved (W10) |
| OQ-006 | TP family acquisition → **RESOLVED W10**: the W9 triple (`140_`/`141_`/`142_`, LB-013) + the two W10 remainders — **DEI-SG-004-2016 ACQUIRED as `150_`** (LB-014: the USD-1M pequeño gate's own instrument, threshold statute-pinned; the 63_ manual's integral-part authority) + **SAR-653-2023 ACQUIRED as `151_`** (LB-015: the CbCR regime, OECD glossary + duties + notification + thresholds; `63_ OQ-6` resolved). Family complete; no TP acquisition leads left except the per-OQ items below. | no | — | resolved (W10) |
| OQ-007 | Vinculación criteria → **RESOLVED W9** (EV141:EVID-531): Reglamento Arts. 11-13 now text-pinned (8 supuestos; participation = >50% capital OR capacity to influence; unidad de decisión a-d) — FR-334's criteria table can be encoded at synthesis. | no | — | resolved (W9) |
| OQ-008 | Naturaleza map coverage (file-local, VERIFY): the evidenced map covers 52 of 56 codes — 23, 44, 48 and 55 (fideicomisos!) are unlisted (63_ p.22); verify vs live form before freezing FR-335's derivation. | no | Takumi S-HN3 | open |
| OQ-009 | BCH rate feed semantics (file-local, CONFIG): which published BCH rate/series governs the per-transaction conversion (FR-336) and the 31-dic threshold parity (FR-327) — feed source and rate type unpinned; encode as dated config with an explicit BCH-source decision. | no | Takumi S-HN3 | open |
| OQ-010 | 545 print edition drift (file-local, VERIFY; kin `67_ OQ-5`): 63_ is the per-FY "PERÍODO 202501" edition — whether a FY2026 edition changes casillas/catalogs is unknown; re-verify catalogs at each FY edition. | no | Takumi S-HN3 | open |
| OQ-011 | 541 fields vs Art. 47 (origin `64_ OQ-1`, CONFIG): the card's five fields do not cover número de acciones / valor nominal / porcentaje de dividendos por acción per semestre, and no foreign-tax-ID field beyond Nacionalidad — more fields in the live card, or statutory content intentionally dropped? | no | Takumi S-HN3 | open |
| OQ-012 | 541 deadline drift (origin `64_ OQ-2`, CONFLICT): statute "antes del último día del mes de febrero" (Feb-27/28) vs Recomendación "a más tardar el ultimo día" (Feb-28/29) — which does OVI enforce? FR-350 defaults last-day with the conflict flagged. | no | Takumi S-HN3 | open |
| OQ-013 | 541 sample values (origin `64_ OQ-3`, VERIFY): screenshots carry no OCR'd sample values (64_ pp.11-12) — casilla labels beyond the five enumerated fields unverifiable from this source. | no | Takumi S-HN3 | open |
| OQ-014 | 541 obligation in no-distribution years (file-local, CONFIG): Art. 47 conditions the inform on businesses "que distribuyan dividendos" — whether a zero-distribution year still files (nil report) is unpinned; config flag until SAR practice/OVI behavior confirms. | no | Takumi S-HN3 | open |
| OQ-015 | 542 threshold OCR-broken (origin `65_ OQ-1`, LEAD): "Lps. 120,00[0].00" read as L120,000.00 — confirm against the Acuerdo 034/99 Sexto original (not in corpus); FR-354 stores the row OCR-marked. | no | acquisition queue | open |
| OQ-016 | 542 deadline drift (origin `65_ OQ-2`, CONFLICT): §1.3 "dentro de los tres meses siguientes al cierre" (≈ Mar-31) vs Recomendación 1 "30 de marzo" — both dated data; FR-355 encodes Mar-30 operative pending instrument, never silent resolution. | no | Takumi S-HN3 | open |
| OQ-017 | 542 ↔ cedular-136 linkage (origin `65_ OQ-3`, VERIFY): the Ayuda states no connection to the cedular-alquiler regime (`31_`/DJIMR-136) — FR-356 stays flag-only; whether the 542 registry feeds or validates the 10% cedular retention (or any monthly-rent threshold) is unverified. | no | Takumi S-HN3 | open |
| OQ-018 | 542 registry-record semantics (origin `65_ OQ-4`, VERIFY): no contract dates (only plazo en meses), no lessor-side field, no per-month amount — confirm the live form matches the four described fields before freezing FR-353. | no | Takumi S-HN3 | open |
| OQ-019 | Acuerdo 034/99 + SAR-236-2024 Décimo Tercero catalog (origin `65_ OQ-5`, LEAD): the base instrument for BOTH 542 and 543 (its Sexto + the informativa-catalog list — items 30 and "31)" truncated/blank in the 65_ print, p.4); acquiring it pins the threshold, the 543 anchor and the catalog tail. | no | acquisition queue | open |
| OQ-020 | 543 sanctions anchor identity (origin `66_ OQ-1`, LEAD): "artículos 177, 178, 180 y 181 del Decreto 2[2]-97" — OCR-broken number read as 22-97 (pre-2016 municipal-era Código Tributario?); instrument not in corpus; FR-360 renders config-gapped. | no | acquisition queue | open |
| OQ-021 | 543 rectificativa text unreliable (origin `66_ OQ-2`, VERIFY): 66_ p.16 mistakenly says "formulario del Informe de Estado de Situación Financiera" (535 chassis bleed) — do not cite that passage; rectificativa behavior = file-01 chassis contract only. | no | Takumi S-HN3 | open |
| OQ-022 | 543 field semantics (origin `66_ OQ-3`, CONFIG): "Numero de permiso de operación" (municipal license number?), "Fecha de operación o Vigencia" (of license or tax?), "Ingresos declarados" (to the municipality? period basis?) — definitions not given; fields carried as evidenced. | no | Takumi S-HN3 | open |
| OQ-023 | 543 plazo day (origin `66_ OQ-4`, CONFIG): "tres meses siguientes al cierre" with no explicit day (cf. 65_'s "30 de marzo") — Mar-31 assumed for calendar-year municipalities as config default (FR-359), unconfirmed. | no | Takumi S-HN3 | open |
| OQ-024 | CbCR TRANSITORIO suspension + restatement lead (W10, file-local, from `151_` OQ-6): SEGUNDO-Num.II (constituent-entity local filing) is suspended in its entirety from the outset until the Director Ejecutivo restates it by comunicado general — the only live presentation duty is Num.I (Honduran-resident UPE). Encode the Num.II row as SUSPENDED-until-restated (LB-015); the restatement comunicado = TOP acquisition lead for this cluster. Also: SAR-653-2023's date line prints 29-dic-2023 (catalog "18-dic-2023" = slip — adjudicated to the print). | no | acquisition queue | open (new W10) |
| OQ-025 | CbCR lempira threshold + Num.4 architecture (W10, file-local, from `151_` OQ-7/OQ-4): Def.-3's lempira leg prints "19 mil millones de lempiras" in WORDS with no digits, no FX rate and no methodology (the dual EUR-o-L threshold is disjunctive as printed) — never derive the lempira figure; contrast SEGUNDO-Num.4's own Jan-2015 FX mechanic. Num.4 attaches NO express exchange-agreement condition to the UPE-jurisdiction-umbral no-obligation rule (encoded as printed, no inference). | no | controller (next synthesis) | open (new W10) |
| OQ-024 | SAR-236-2024 ordinal structure (origin `66_ OQ-5`, VERIFY): 66_ cites "Acuerdo 236-2024 sección séptima / sección octava" while other Ayudas cite ordinals (PRIMERO/TERCERO/DÉCIMO OCTAVO) — verify the instrument's actual ordinal structure (kin `32_ OQ-2`, instrument unacquired standalone). | no | acquisition queue | open |


