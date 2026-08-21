# SV — Taxation — CT procedures: the Reglamento de Aplicación del Código Tributario cross-tax layer — definitions and clocks (caducidad vs prescripción), representation and domicilio fiscal, registration and agent designation, declarations and the amendment classification gate, payments and extinction modes, compensación, refunds, sanctions and deuda tributaria, books and records, fiscalización bundles, and the print-era document/dictamen heritage (D.E. N° 117-2001 Arts. 1-146)

| Field   | Value |
|-------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (W17 fold-in wave, in review) |
| Authors | Takumi synthesis wave 17 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the CROSS-TAX procedural
layer of El Salvador's *Reglamento de Aplicación del Código Tributario*
(D.E. N° 117, 11-dic-2001; the CT application reglamento): the operative
definition set of Art. 2 — *caducidad* (administrative limitation clock,
self-materializing by the *simple transcurso del tiempo*) vs
*prescripción* (taxpayer limitation, pleaded; the DGII declares it) as
limitation-tracking vocabulary on fiscal-period records, the
*ejercicio comercial* calendar-year constant, and the *Administración
Tributaria* = Ministerio de Hacienda-through-Direcciones-Generales
identity; the representation and *domicilio fiscal* stack (representante
legal credential set vs gestión-scoped *apoderado*, address types with
change-effective semantics and fallback notification places);
registration mechanics (inscripción, the NRC card as contribuyente
proof, corporate-event notice checklists, the AT's registry of
retention/perception agents); the declaration state model (forms never
excuse filing, the receiver's no-modification/must-receive rules, the
modification taxonomy and the FORMAL-DEFECT vs PAYMENT-AFFECTING
amendment classification gate anchored on CT 103); payments and the
extinction-mode enum (pago · compensación · confusión · prescripción —
no condonación); the compensación gate (efectivo-paid, firmes/líquidos/
exigibles, CT 76 imputation order) and the Art. 23 IMPRESCRIPTIBILIDAD
invariant for un-entered retentions; refunds (the 120-day resolution
clock, the asalariado excess-retention devolución with its
enteros-verification precondition, and the Art. 133 two-year caducidad
for the agent's erroneous-retention refund claims — the agent-side twin
of Art. 23); the sanction-base and *deuda tributaria* architecture
(payable-portion-only sanction base, reincidencia windows, per-ejercicio
granularity, midnight birth of principal, indivisibility); the books and
records regime (bound-and-foliated books, the 2-month/15-day backlog
limits, the separate-registration invariant feeding the prorrata
engine, the computerized-systems documentation retention duty); the
fiscalización awareness layer (notification mechanics, the
audit-response export bundle including the *catálogo de cuentas y
manual de aplicación*, the consulta no-toll rule); and the print-era
historical block (imprenta/AT-correlative chain, Comprobante de
Liquidación and Factura de Exportación, máquinas registradoras with the
¢4,970.00 dated [sic] colones gate, the dictamen block, the
transitorios substantive-vs-procedural split and Art. 146's AT
normative power as the citation-rule root for F-forms/catalogs/DGII
resoluciones).

It does **not** cover: the ISR retention mechanics of Arts. 91-103
(permanent services, remunerations sujetas, 10-hábiles entero,
constancia — `payroll/08_isr-interfaces.md` territory, wired by id in
this wave's T4); the IVA retention/percepción mechanics of Arts.
104-107 (non-domiciled reverse charge, import-temporal leases,
designation criteria, price reporting — developed by taxation/13's
matrix in this wave's T2; the CT retention matrix itself is
`13_iva-retentions.md` SV-TAX-FR-303..319, by id, never restated here);
the CT sanction catalog (CT 226-262, 05_-encoded — this file supplies
only the sanction-BASE and reincidencia mechanics that develop it); the
DTE emission surfaces (e-invoicing/01 by id); the F-07/F-14 builders
(`fiscal-reporting/`, by id); the prorrata/reintegro computations
themselves (`11_iva-pro-rata-remanente.md` SV-TAX-FR-269..283 and
`14_iva-exports-refunds.md`, by id); and the días-hábiles computation
engine (`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202..204,
by id — this file's clock rows resolve AS-OF their trigger event per
D15 and consume that engine, never reimplement it).

## 2. Legal Basis

Authority order (binding, per wave constraints): **Código Tributario =
05_ governs substance; 75_ develops procedure.** Where a 75_ article
restates or develops a CT article, the LB row below cites 75_ primary
for procedure with a co-cite note to the CT anchor (for this file, the
load-bearing pairs are: Art. 133/Art. 23 — the two-sided retention
limitation pair; Art. 95←CT 155 and Arts. 104-106←CT 161/162 belong to
payroll/08 and taxation/13, T2/T4 territory). Substantive matrices
already encoded in sibling files are cited BY FR ID, never restated
(the ISR track `taxation/04` and the IVA track `taxation/13` NEVER
merge — S9 constraint rides).

**Instrument identity:** D.E. N° 117 (11-dic-2001), published D.O. N°
234, Tomo 353, 11-dic-2001; **effective 19-dic-2001** per Art. 148's
eight-days-after-publication rule; 148 articles; signature block Flores
Pérez / Daboub (ad-honorem), p.85.

**R17/R30(a) role (EVID-358 audit):** this instrument IS the
04_/02_ mass-repeal authority corpus rulings R17 (index line 631) and
R30(a) (line 644) cite — Art. 147 repeals 108 articles of the ISR
Reglamento (D.E. 101-1992) and 24 of the IVA Reglamento (D.E.
83-1992). EVID-358's computed survivor sets: 04_ = Arts. 1, 2, 6, 7,
9-20, 22-35, 37-39, 59, 84, 141 (+144 spent); 02_ live survivors =
**Arts. 1-10, 16-26, 29-30, 50-51** (+52 spent) — R30(a)'s "16-30"
over-includes 27-28 (repealed), and 36/45 died earlier via reform (1)
D.E. 60-1993 (02_ corrective addendum recorded — master index + sources
README; the 04_ survivor-phrasing fold remains pending, EV75 OQ-5).

**Vintage-note rule (rides every 75_ LB row in this file, per Global
Constraints — not repeated per row):** 75_ print carries NO REFORMAS
block (EV75 OQ-1) and post-2001 repeal by CT Art. 344 ff is
print-unresolvable (OQ-8, SOQ-06-kin) — cite as printed with the watch
note. **OQ-2 bar:** the 10-year prescription (Art. 21) and 3y/5y
reincidencia windows (Art. 137) are 2001-print values — encoded ONLY as
dated config-gap rows with the pin-current-CT condition; never as
constants. **OQ-3 bar:** dictamen block (Arts. 58-72) = historical/
awareness only, never operative FRs. **OQ-4 bar:** máquinas
registradoras block (Arts. 44-55) = historical awareness; ¢4,970.00
colones gate dated [sic], never converted (D15/D16).

**Consumer map (who cites this file by id):** W17 T2 (taxation/04 then
13 — LB co-cites to 75_ Arts. 95-107); W17 T3 (fiscal-reporting/01 —
the modificatoria engine SV-FREP-FR-040 consumes FR-367's
classification gate; 06/07/08 notes); W17 T4 (payroll/08 — the
precio-de-mercado root of FR-357). Existing id consumers of anchors
re-homed here: SV-TAX-FR-174 (Quincena-25 credit/certificado,
`01_isr-framework.md`), SV-TAX-FR-269..283 (prorrata engine,
`11_iva-pro-rata-remanente.md`), SV-FREP-FR-202..204 (días-hábiles
engine, `fiscal-reporting/08_filing-calendar.md`), SV-COA-FR-022..054
(`chart-of-accounts/02_coa-structure.md`), SV-TAX-FR-303..319
(`13_iva-retentions.md`).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001), Art. 1 | "El presente Reglamento desarrolla con carácter general y obligatorio los alcances del Código Tributario, así como el desarrollo y ejecución del mismo para su correcta aplicación"; cuando se haga mención a la "Administración o Administración Tributaria" y en atención a lo que establece el artículo 21 del Código Tributario, "debe entenderse que se alude al Ministerio de Hacienda, por medio de las Direcciones Generales respectivas bajo cuya competencia se encuentran todas las actividades administrativas relacionadas con los tributos internos y su recaudación" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 1 pp.1-2 (EVID-339; verified 75_ txt lines 63-69, 73-80) |
| LB-002 | Reglamento CT, Art. 2 defs. 2.10-2.11 | 2.10 Caducidad: "El vencimiento del plazo o término que el Código otorga a la Administración Tributaria para ejercer su facultad fiscalizadora y sancionatoria; así como para el contribuyente a efecto de solicitar la devolución de tributos, accesorios, anticipos o retenciones indebidas o en exceso, la cual requiere para su materialización del simple transcurso del tiempo, no siendo necesaria la alegación ni declaración de la autoridad administrativa". 2.11 Prescripción: "imposibilita a la Administración para reclamar al deudor moroso, la obligación principal y sus accesorios… ésta requiere alegación de la parte interesada. La Dirección General de Impuestos Internos será la competente para declararla y que produzca sus efectos" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 2 pp.5-6 (EVID-339; verified 75_ txt lines 219-236) |
| LB-003 | Reglamento CT, Art. 2 defs. 2.12 y 2.16 | 2.12: "Ejercicio Comercial: El comprendido desde el uno de enero al treinta y uno de diciembre de cada año". 2.16 Precio de mercado: "El precio de venta que tengan los bienes o servicios, en negocios o establecimientos similares ubicados en el mismo sector, localidad o departamento; para efectos de establecer la similitud de los establecimientos, se tomara en consideración entre otros factores los siguientes: tamaño de los negocios, actividad o giro, nivel económico, participación en el mercado" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 2 p.6 (EVID-339; verified 75_ txt lines 237-240, 270-278) |
| LB-004 | Reglamento CT, Art. 2 def. 2.4 (métodos de interpretación y analogía) y def. 2.2 (imágenes ópticas) | Analogía: "es un procedimiento admisible como medio de integración de la ley, y no como un método de interpretación, por consiguiente mediante ella no pueden crearse tributos ni exenciones". 2.2: "Imágenes ópticas no modificables: Las representaciones gravadas y visibles de determinados documentos originales cuyo sistema de resguardo electrónico ha sido autorizado por la Administración Tributaria y que no son susceptibles de ser cambiados o alterados por ningún medio" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 2 pp.3-4 (EVID-339; verified 75_ txt lines 88-93, 142-146) |
| LB-005 | Reglamento CT, Arts. 3, 4 y 9 | Art. 4: consultas por "los sujetos pasivos, su representante o apoderado debidamente acreditados… mediante escrito dirigido a la Administración Tributaria"; "Los efectos de las respuestas emitidas por la Administración a consultas planteadas por los sujetos pasivos, son de aplicación individual, por lo que, en ningun caso dicha aplicación se extenderá ningun otro sujeto pasivo" [sic "ningun"]; "La presentación de la consulta no interrumpirá los plazos establecidos en el ordenamiento tributario para el cumplimiento de las obligaciones correspondientes"; "no podrán entablar recurso alguno contra la contestación a la consulta". Art. 3: guías de orientación divulgadas por la Administración, modificables a su criterio. Art. 9: denuncias con "mecanismos internos que garanticen la confidencialidad de la identidad de los denunciantes" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 3-4 pp.6-7, Art. 9 pp.9-10 (EVID-340; verified 75_ txt lines 341-347) |
| LB-006 | Reglamento CT, Art. 30 | Representante legal: "deberá mostrarse parte por medio de escrito dirigido a la Administración Tributaria y acreditar su personería mediante escritura de constitución, punto de acta de elección y la credencial debidamente inscrita"; apoderado: "deberán previamente designarlo mediante escrito… acreditar su personería por medio de poder en el que conste en forma clara e inequívoca la gestión que se le encomienda realizar. En el caso de persona jurídica tal designación deberá efectuarla el representante legal de la misma" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 30 p.17 (EVID-341; verified 75_ txt lines 862-870) |
| LB-007 | Reglamento CT, Arts. 28-29 + def. 2.9 | Art. 28 (cambio efectivo, CT 90.4): "el cierre definitivo de operaciones en el lugar señalado para oír notificaciones y desvinculación total de actividades del negocio… así como el consecuente abandono del mismo y traslado físico del local". Art. 29 (CT 90.5/173.r): failing señalamiento, "se considerara como tal cualesquiera de los lugares a que aluden" CT 54 a)/b) y 55 a)/b). Def. 2.9: "Dirección Procesal: Es el lugar que para efectos procesales, se ha señalado para recibir notificaciones, definido por los apoderados designados por escrito por los sujetos pasivos" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 28-29 pp.16-17; def. 2.9 p.5 (EVID-341; verified 75_ txt lines 213-217, 830-836) |
| LB-008 | Reglamento CT, Arts. 5 y 8 | Art. 5 (CT 32): la Administración "deberá mantener actualizados los registros relativos a la representación de los sujetos pasivos". Art. 8 (acceso al expediente): escrito en duplicado; el apoderado agrega "testimonio de poder o fotocopia del mismo certificada por Notario"; las personas jurídicas agregan "el testimonio de la escritura de constitución… así como el punto de acta de elección y la credencial de representación vigente debidamente inscrita"; los expedientes "en ningún caso podrán ser consultados fuera de las instalaciones" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 5, 8 p.8-9 (EVID-341; verified 75_ txt lines 384-388, 415-425) |
| LB-009 | Reglamento CT, Arts. 24-25 | Art. 24: "Los contribuyentes deberán inscribirse en la Administración Tributaria o en los lugares que ésta disponga dentro del plazo estipulado en el Código… La Administración Tributaria deberá llevar registros de los contribuyentes inscritos. Asimismo deberá llevar registros respecto de los Agentes de Retención y Percepción que designe". Art. 25: "entregará a cada contribuyente la tarjeta respectiva, en que conste su número de registro… La tarjeta, en original, acreditará la calidad de contribuyente. En el caso del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, la referida tarjeta deberá ser presentada siempre que se efectúen compras o se utilicen servicios necesarios para realizar la actividad o giro del establecimiento, negocio u oficina, a fin de exigir el Comprobante de Crédito Fiscal correspondiente" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 24-25 pp.15-16 (EVID-342; verified 75_ txt lines 770-796) |
| LB-010 | Reglamento CT, Arts. 26-27 | Art. 26 (CT 86 inc. 6): aviso de "disolución, liquidación, fusión, transformación y cualquier modificación de la sociedad" + "Certificación del Punto de Acta de Asamblea General y testimonio de la escritura en original o fotocopia certificada por Notario, debidamente inscrita en el Registro respectivo". Art. 27: cambio de datos básicos via formulario de la Administración "dentro del plazo" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 26-27 p.16 (EVID-342; verified 75_ txt lines 805-812) |
| LB-011 | Reglamento CT, Art. 31 | "Los contribuyentes deben liquidar el impuesto en los formularios que proporcionará la Administración Tributaria. La falta de tales formularios no libera de la obligación de declarar y pagar el impuesto dentro del plazo legal" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 31 p.17 (EVID-343; verified 75_ txt lines 880-884) |
| LB-012 | Reglamento CT, Art. 32 | El receptor delegado "revisará… para cerciorarse de que todos los requisitos han sido llenados… pero en ningún caso podrá modificarlas, debiendo ser los sujetos pasivos quienes hagan las correcciones"; "El delegado deberá recibir la declaración aún cuando los sujetos pasivos se negaren a corregir los errores… salvo en los casos que dichos errores conlleven la disminución del valor a pagar o aumente el saldo a favor" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 32 p.18 (EVID-343; verified 75_ txt lines 899-918) |
| LB-013 | Reglamento CT, Arts. 33-34 | Art. 33: la modificación "podrá referirse a los datos, informaciones, cálculo del impuesto, u otros elementos constitutivos de la naturaleza propia de cada impuesto". Art. 34: las declaraciones originales modificadas "por la omisión de requisitos formales o errores de la misma naturaleza, no se consideraran como presentadas incorrecta; aquellas declaraciones en las que como producto de la modificación de lugar al pago original o complementario del impuesto si se consideraran como presentadas incorrectas, de conformidad a lo establecido en el artículo 103 del Código Tributario" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 33-34 p.18 (EVID-343; verified 75_ txt lines 918-943; CT 103 co-anchor) |
| LB-014 | Reglamento CT, Art. 35 | Declaraciones electrónicas: "tomará en cuenta los datos necesarios para las transferencias electrónicas, tales como: encriptado de los procesos, firma digital o electrónica, facilidades para cambios de clave por el sujeto pasivo autorizado y recibo de verificación electrónico proporcionado por la Administración como constancia de recibido" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 35 pp.18-19 (EVID-343; verified 75_ txt lines 944-960) |
| LB-015 | Reglamento CT, Arts. 13-14 y 20 | Art. 13: la obligación sustantiva "se extingue… a) por el pago. b) Por compensación; c) Por confusión; y d) Por prescripción". Art. 14: "Cualquier persona puede pagar de la manera establecida en el artículo 72 del Código a nombre de un deudor tributario". Art. 20: la confusión "se da cuando en El Estado convergen simultáneamente la calidad de deudor y acreedor de la referida obligación" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 13-14 p.11, Art. 20 p.13 (EVID-344/345; verified 75_ txt lines 566-572, 594-596, 701-704) |
| LB-016 | Reglamento CT, Art. 15 | Autoliquidado pagadero "en las Colecturías del Servicio de Tesorería, en los Bancos del Sistema Financiero o en los lugares señalados por la Administración"; liquidación oficiosa: "dentro de los dos meses posteriores contados a partir de la fecha en que la resolución liquidatoria del impuesto quede firme"; el contribuyente completa "el mandamiento de ingreso respectivo, en forma clara, precisa, inteligible, sin borrones, tachaduras o enmendaduras, tanto el original como sus copias"; "El mandamiento de ingreso será proporcionado por la Administración Tributaria, por cada liquidación de impuesto" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 15 pp.11-12 (EVID-344; verified 75_ txt lines 602-625) |
| LB-017 | Reglamento CT, Art. 16 | Multas: "deberá efectuar el pago de la misma dentro de los treinta días siguientes a aquel en que quede firme la resolución sancionatoria"; "Los sujetos pasivos podrán autoliquidar en forma voluntaria en los formularios respectivos la multa correspondiente, aplicando la atenuante pertinente en los casos que proceda"; "La ausencia de autoliquidación voluntaria de la multa… no impide la recepción de la declaración correspondiente"; las no autoliquidadas "serán impuestas por la Administración Tributaria mediante resolución, previo seguimiento del proceso sancionatorio pertinente" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 16 p.12 (EVID-344; verified 75_ txt lines 643-660) |
| LB-018 | Reglamento CT, Art. 18 | Los intereses por mora (CT 75.b) "se regirán por lo dispuesto en el Decreto Legislativo correspondiente" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 18 p.13 (EVID-344; verified 75_ txt lines 670-674) |
| LB-019 | Reglamento CT, Art. 19 | "La Administración Tributaria compensará de oficio con conocimiento del interesado o a petición de parte, los saldos acreedores de los contribuyentes provenientes de tributos internos, con sus saldos deudores de los referidos tributos, respetando el orden de imputación de pagos establecido en el artículo 76 del Código, siempre que los pagos hubieren sido hechos en efectivo y que tanto los saldos acreedores como deudores sean firmes, líquidos y exigibles" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 19 p.13 (EVID-345; verified 75_ txt lines 689-694) |
| LB-020 | Reglamento CT, Arts. 21-22 | Art. 21: "La prescripción opera en contra del Fisco, una vez transcurridos 10 años contados a partir del día en que debió ejercerse la acción o derecho de reclamación, de acuerdo a las reglas siguientes: 1) Cuando se trate de impuesto autoliquidado por el contribuyente, a partir del día siguiente a aquel en que concluyó el término legal para pagar o el de su prórroga si la hubiere; y 2) Cuando se trate de liquidación oficiosa o de imposición de multas aisladas… a partir del día siguiente al vencimiento del plazo para el pago, establecido en el artículo 74 inciso 2º del Código". Art. 22: "opera cuando se hayan cumplido los requisitos establecidos por el Código para considerarla materializada tanto para lo principal como para lo accesorio" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 21-22 pp.14-15 (EVID-345; verified 75_ txt lines 712-745; 2001-print value — OQ-2) |
| LB-021 | Reglamento CT, Art. 23 | "La Administración Tributaria podrá exigir en cualquier tiempo, al agente de retención la obligación de enterar las cantidades retenidas y no enteradas en su oportunidad, e imponer la sanción correspondiente" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 23 p.15 (EVID-345; verified 75_ txt lines 748-751; CT 247 sanction kin by pointer, 05_ EVID-065) |
| LB-022 | Reglamento CT, Arts. 129, 130 y 132 | Art. 129: resoluciones definitivas cuando "a) No se interponga recurso de apelación dentro del término que la ley respectiva establece…; b) Se declare inadmisible el recurso de apelación; y c) Se dicte fallo que resuelve el recurso de apelación". Art. 132: "previo informe de que las sumas que se pretende devolver han ingresado al Fondo General, a petición de parte, dictará resolución ordenando se devuelva al interesado el excedente"; "dentro de los 120 días siguientes a la fecha de presentación de la solicitud por el interesado"; "En la misma forma se procederá cuando se trate de multas e intereses pagados, cuando la cuantía de lo pagado sea disminuida por resolución firme" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 129-132 pp.78-80 (EVID-355; verified 75_ txt lines 4076-4155) |
| LB-023 | Reglamento CT, Art. 131 | Asalariados: "personas naturales domiciliadas, cuyos ingresos provengan exclusivamente de salarios, en la cuantías determinadas por la Ley de Impuesto sobre la Renta; tendrán derecho a la devolución de las cantidades retenidas que resultaren en exceso después de liquidado el impuesto… sin perjuicio de la verificación que pueda hacer la Administración Tributaria, de que el agente de retención ha efectuado los enteros de las cantidades retenidas" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 131 p.79 (EVID-355; verified 75_ txt lines 4121-4130) |
| LB-024 | Reglamento CT, Art. 133 | "La caducidad para solicitar la devolución por parte del sujeto pasivo que efectuó el cobro indebido de cantidades retenidas y enteradas al fisco, operará dentro del término de dos años contados a partir de la fecha del pago indebido, sin perjuicio de la acción civil a que haya lugar por parte de los sujetos a quienes les efectuó la retención indebidamente" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 133 p.80 (EVID-355; verified 75_ txt lines 4156-4162; pairs Art. 23 — LB-021) |
| LB-025 | Reglamento CT, Art. 135 | Cláusula legal para fianzas (CT 222/225): "Un mes antes del vencimiento de esta fianza, extendida por el término de dos años contados a partir de la expedición de la autorización por parte de la Administración Tributaria, si la Institución afianzadora no ha recibido informe de la oficina correspondiente sobre el pago o pagos a cuenta de la suma afianzada, dicha institución deberá depositar en la Dirección General de Tesorería, el valor total o parcial de la suma afianzada, según el caso" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 135 pp.80-81 (EVID-355; verified 75_ txt lines 4181-4196) |
| LB-026 | Reglamento CT, Art. 136 (CT 238.b) | "Cuando se aplique la sanción establecida en el artículo 238 literal b) del Código Tributario y se hubieren hecho retenciones y entero de impuesto así como anticipos a cuenta, la referida sanción recaerá únicamente sobre la porción del impuesto a pagar, excluyendo el monto retenido y enterado y el anticipo a cuenta ingresado al Fondo General de la Nación" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 136 p.81 (EVID-356; verified 75_ txt lines 4205-4212; CT 238 developer row) |
| LB-027 | Reglamento CT, Art. 137 (CT 262) | Reincidencia requiere: "a) Sentencia o resolución firme en la que se sancione la primera infracción; b) Que se incurra nuevamente en infracción respecto de la misma obligación cuyo incumplimiento fue sancionado; y c) Que la infracción se cometa dentro del plazo de la caducidad de la facultad sancionatoria, es decir, dentro del plazo de tres años contados desde el día siguiente en que se cometió la primera infracción, si mediare liquidación del impuesto por parte del contribuyente dentro del plazo legal; o dentro del plazo de cinco años, si no se hubiere presentado la liquidación del impuesto o si se hubiere presentado extemporáneamente"; "Para la calificación de la reiteración, se estará a la concurrencia del acto o hecho tipificado como infracción" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 137 p.82 (EVID-356; verified 75_ txt lines 4214-4235; 2001-print values — OQ-2) |
| LB-028 | Reglamento CT, Arts. 138-141 | Art. 138: la deuda es "la obligación sustantiva principal liquidada por el contribuyente más las obligaciones accesorias como multas o intereses liquidados por la Administración Tributaria… habrá tantas deudas tributarias, como ejercicios impositivos diferentes con respecto a un mismo contribuyente". Art. 139: la principal existe "a partir de la media noche del último día del ejercicio o período impositivo de que se trate"; los intereses "desde el día en que se incurre en mora"; las multas de oficio "a partir del día en que la resolución mediante la cual se imponen, quede firme". Art. 141: la deuda "es única e indivisible independientemente que la cosa debida sea fraccionable, requiere para su satisfacción, el entero total de la suma debida" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 138-141 pp.82-83 (EVID-356; verified 75_ txt lines 4249-4297) |
| LB-029 | Reglamento CT, Art. 74 | Anotaciones cronológicas; los libros "se llevarán en libros empastados y foliados en forma correlativa"; "en lo que respecta a la contabilidad formal no podrá permitirse un atraso mayor de dos meses en las anotaciones, contados desde el día siguiente en que se efectuó la operación… o para el caso de los ajustes… conforme a principios de contabilidad aprobados por el Consejo de Vigilancia… o en su defecto por las Normas Internacionales de Contabilidad"; "Para efectos de los registros para el control del [IVA] no podrá permitirse un atraso mayor a quince días, conforme a lo establecido en el artículo 141 literal a) del Código" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 74 p.48 (EVID-350; verified 75_ txt lines 2476-2494; CT 141-a anchor) |
| LB-030 | Reglamento CT, Art. 76 | "deberán registrar sus operaciones en forma separada diferenciando unas y otras, también deberán registrar separadamente e identificar los costos, gastos, y créditos fiscales relacionados con cada tipo de operación o actividad, con el objeto de determinar correcta del tributo" [sic "determinar correcta"] | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 76 p.49 (EVID-350; verified 75_ txt lines 2530-2536) |
| LB-031 | Reglamento CT, Art. 77 | Contabilidad computarizada: "deberá conservar como parte integrante de la misma toda la documentación relativa al diseño del sistema, los diagramas del mismo y los programas fuente cuando proceda, así como las bases de datos, por el plazo establecido en dicho precepto legal [CT 147], los cuales pondrá a la disposición de la Administración Tributaria, así como el equipo y sus técnicos, cuando ésta lo requiera en el ejercicio de la facultad fiscalizadora" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 77 p.50 (EVID-350; verified 75_ txt lines 2545-2553) |
| LB-032 | Reglamento CT, Arts. 80-85 | Art. 80: jerarquía del contador (CT 139.2/209 + CC 437) incl. "Bachilleres en Comercio y Administración opción contador o Bachiller Técnico Vocacional Comercial opción contaduría… Número de Registro de Acreditación… Unidad de Acreditación… del Ministerio de Educación"; éstos "no pueden realizar funciones reservadas exclusivamente al contador público autorizado por el Consejo de Vigilancia". Art. 81: registro de inventarios con columnas mínimas 1)-6) (fecha; operación con referencia documental y partida — compras a proveedores, devoluciones de clientes, retiros…). Arts. 82-85: especificaciones de columnas de los libros IVA (ventas a contribuyentes, ventas a consumidores, compras) y anexo de exportaciones; las anulaciones se registran en el mes de su ocurrencia | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 80-85 pp.51-55 (EVID-350; column specs summarized, not quoted verbatim — historical templates) |
| LB-033 | Reglamento CT, Art. 109 | "Las notificaciones deberán practicarse en horas y días hábiles… se entenderá por horas hábiles las comprendidas de las seis de la mañana a las siete de la tarde de cada día"; CT 172 "otros similares" = actividades cuyo horario se prolonga tras las 19:00 y opera en días inhábiles (restaurantes, hoteles, moteles, hospedajes o casa de huéspedes, casinos y discotecas); CT 181.f "otro documento de identificación" = "carné electoral, documento único de identidad, pasaporte, licencia de conducir, tarjeta de afiliación del ISSS, carné de INPEP" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 109 p.66 (EVID-353; verified 75_ txt lines 3413-3425; esquela mechanics Arts. 111-113 by summary) |
| LB-034 | Reglamento CT, Art. 120 (CT 126.a) | Exhibición a)-i): libros de contabilidad, registros auxiliares/especiales y de control de inventarios e IVA; inventarios inicial y final; "estados financieros básicos y sus anexos… debidamente firmados"; "Balanzas o balances de comprobación mensuales y de saldos ajustados de final del ejercicio"; partidas o comprobantes contables, declaraciones de mercancía, documentos de compras y ventas, comprobantes de cheques, contratos, recibos, correspondencia comercial; "Copias originales de las declaraciones de los diferentes tributos"; "Catalogo de cuentas y manual de aplicación"; "Informe del auditor externo, cuado proceda" [sic "cuado"]; "Dictamen e informe fiscal cuando proceda"; "Todos estos documentos deberán estar arreglados en relación con cada período que comprenda el ejercicio comercial, por orden de fecha y asientos de la contabilidad" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 120 pp.70-72 (EVID-354; verified 75_ txt lines 3690-3722) |
| LB-035 | Reglamento CT, Arts. 36-38 | Art. 36: "para soportar las transferencias de bienes, prestación de servicios y exportaciones, únicamente deben emitir y entregar los documentos que establezca el Código Tributario… no será valido el uso de cualquier otro documento… La emisión y entrega de documentos que exijan otras leyes no sustituye la obligación de emitir y entregar documentos establecida en el artículo 107 del Código Tributario". Art. 37: "deberán portar las Notas de Remisión, Facturas y Comprobantes de Crédito Fiscal, según corresponda, durante el traslado, circulación o tránsito de bienes muebles y mercaderías, y exhibir tales documentos a delegados o auditores de la Administración Tributaria". Art. 38 (CT 114): inclusión de "las direcciones de todas las sucursales si las hubiere", con informe-relief volumétrico y para cambios de nombre/denominación/giro "siempre que justifique y compruebe la efectividad de dichos cambios" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 36-38 pp.19-21 (EVID-346; verified 75_ txt lines 975-1010) |
| LB-036 | Reglamento CT, Art. 39 | Documentos impresos: "deberán contener el numero de autorización otorgado por la Dirección General de Impuestos Internos"; imprentas deben "exigirles la presentación del original de la tarjeta de inscripción para efectos del IVA(NRC)"; abstenerse de reposiciones de documentos perdidos o "documentos con numeración repetida"; listado de clientes (CT 116.f) mínimo: "Nombre del cliente, NIT, NRC, tipo de documento emitido, rango impreso expresado bajo el concepto 'desde' – 'hasta'" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 39 p.21 (EVID-346; verified 75_ txt lines 1020-1040) |
| LB-037 | Reglamento CT, Arts. 41-43 | Art. 41 (CT 108): el Comprobante de Liquidación contiene 1) "Un resumen 'desde –hasta', de los números de los documentos emitidos… con el valor total del monto de las operaciones realizadas por tipos de documento… el valor consignado debe ser neto de impuesto"; 2) "El debito fiscal de las operaciones… reflejado por separado en el comprobante de liquidación"; los mandantes lo registran "en el Libro de Ventas a Contribuyentes, en el período tributario que corresponda". Art. 42: facturas de exportación "deberán identificarse bajo la denominación 'Factura de Exportación' poseer un número correlativo independiente y diferente al utilizado por las facturas que amparan operaciones locales… deberán ser preimpresas por imprenta autorizada"; "deberán registrarse en el libro de ventas a consumidores, consignando los valores de acuerdo a lo establecido en los artículos 81 y 82 del presente Reglamento" [sic cross-ref — consumer-sales book is Art. 83; print anomaly, OQ-7]. Art. 43 (CT 163): el agente de percepción "deberá emitir un Comprobante de Crédito Fiscal, en el que además de consignar el debito fiscal que genere la operación deberá de consignar en forma separada el impuesto percibido en calidad de agente"; entero con la declaración del impuesto | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 41-43 pp.21-22 (EVID-347; verified 75_ txt lines 1085-1155) |
| LB-038 | Reglamento CT, Arts. 44-50 (resumen histórico) | Art. 44: identificación de máquinas (número/marca/modelo/serie visible; CPU en redes; series propias de equipos autoensamblados); capacidad mínima de "cuatro dígitos" y "contador automático inviolable". Art. 45: tiquetes con NRC+NIT, correlativo, "Fecha y hora de la emisión", condición "gravado o exento", "Inclusión del impuesto respectivo en el precio", subtotalización y "Valor total de la operación"; "Cuando el monto total de las operaciones sean igual o superiores a ¢ 4,970.00, la maquina registradora o sistema computarizado autorizado deberá ser capaz de consignar los datos requeridos en el literal b), numeral 7) del artículo 114 del Código Tributario… y en caso de no cumplirlo deberá emitirse una factura preimpresa". Art. 46: devoluciones con sello "DEVOLUCION" y reflejo en negativo en la cinta de auditoría. Arts. 47-48: reportes X/Z conciliados con el libro de ventas a consumidores; "no estará permitido por motivo alguno, retroceder la numeración". Art. 49: "La Administración Tributaria podrá autorizar la utilización de cintas de auditoría electrónicas o bitácoras en sustitución de cintas de papel". Art. 50: solicitud de autorización con divulgación de software d)1-8 ("Licencia de uso de la aplicación… Descripción del equipo…") | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 44-50 pp.23-31 (EVID-348; verified 75_ txt lines 1230-1240, 1431; colones value dated [sic], never converted) |
| LB-039 | Reglamento CT, Arts. 58-72 (dictamen — HISTORICAL) | Art. 58: auditoría por "Licenciados en Contaduría Pública o Contadores Públicos Certificados"; Art. 61: nombramiento "a más tardar dentro de los primeros cinco meses del período anual a dictaminar", aviso a la AT "dentro del plazo de treinta días calendario"; Art. 65: dictamen con alcance — "se planificó y se examinaron las cifras mediante pruebas selectivas", separando "los incumplimientos formales de los sustantivos, subsanados y no subsanados, debiendo cuantificarse monetariamente el impacto impositivo"; Art. 66: "Los estados financieros a presentar serán los que establecen las Normas Internacionales de Contabilidad", comparativos, "expresando sus cifras en miles de colones o dólares de Estados Unidos de América según la moneda de curso legal"; Art. 67: anexos a)-n) incl. la cadena de determinación del IVA (b.3) que replantea prorrata y reintegro libro por libro | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 58-72 pp.34-47 (EVID-349; verified 75_ txt lines 1845-1878, 1975-1985; historical/awareness only — OQ-3) |
| LB-040 | Reglamento CT, Arts. 145-146 | Art. 145 (CT 280): "las normas sustantivas referentes a hechos generadores de carácter periódico e instantáneo ocurridos con anterioridad a la vigencia del citado Código se regirán por las disposiciones legales vigentes al momento de su ocurrencia y las relativas a hechos generadores ocurridos a partir de la vigencia del Código Tributario se regirán por las disposiciones legales del mismo"; "Las normas relativas a procedimientos serán aplicables a partir de la vigencia del Código Tributario para todas aquellas actuaciones, etapas y plazos que independientemente del ejercicio o período que correspondan, su trámite se inicie dentro de la vigencia del mismo…". Art. 146: "La Administración Tributaria está facultada para dictar las normas administrativas generales, dentro de lo previsto en el Código Tributario y las Leyes Tributarias respectivas para el cumplimiento de la misma y del presente reglamento" | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 145-146 p.84 (EVID-357; verified 75_ txt lines 4350-4375) |
| LB-041 | Reglamento CT, Arts. 147-148 | Art. 147: "A partir de la fecha en que entre en vigencia el presente Reglamento, quedan derogadas: a) Las disposiciones del Decreto Ejecutivo Nº 101… Reglamento de la Ley de Impuesto Sobre la Renta: Artículos 3, 4, 5, 8, 21, 36, 40… 142, 143. b) Las disposiciones del Decreto Ejecutivo Nº 83… Reglamento de la Ley de Impuesto a la Transferencia de Bienes Muebles y a la prestación de Servicios: Artículos 11, 12, 13, 14, 15, 27, 28, 31… 46, 47, 48, 49." (listas completas en EVID-358). Art. 148: "El presente Decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." D.O. N° 234, Tomo 353, 11-dic-2001 → effective 19-dic-2001 | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 147-148 pp.84-85 (EVID-358; verified 75_ txt lines 4384 ff., 4416-4445) |

Dead text and separation notes — never implementable as merged rows
(per wave constraints): the payroll retention engine of Arts. 91-103
stays `payroll/08_isr-interfaces.md` territory (this wave's T4 wires
its LB co-cites to 75_); the IVA retention/percepción mechanics of
Arts. 104-107 develop the CT 161/162 matrix that `13_iva-retentions.md`
SV-TAX-FR-303..319 owns (by id — never restated here; the ISR track
`taxation/04` and IVA track `taxation/13` NEVER merge); the CT sanction
catalog (CT 226-262) stays 05_-encoded — this file supplies only
Art. 136's base computation and Art. 137's reincidencia mechanics. The
dictamen (58-72) and máquinas-registradoras (44-55) blocks are
historical/awareness rows gated by OQ-3/OQ-4 — never operative FRs. The
vintage-note rule (§2 preamble) rides every 75_ row above.

## 3. Functional Requirements

### 3.1 Definitions & clocks vocabulary (Arts. 1-2)

- **SV-TAX-FR-354:** The system shall implement the limitation-tracking
  vocabulary as CONFIG CATEGORIES on fiscal-period and liability
  records, never as self-executing enforcement: *caducidad* — the
  administrative clock (fiscalización/sanción powers; the taxpayer's
  refund claims for "tributos, accesorios, anticipos o retenciones
  indebidas o en exceso"), materializing by the *simple transcurso del
  tiempo* with no allegation or declaration required; vs
  *prescripción* — the taxpayer-pleaded limitation that bars the
  Administración's claim, requiring "alegación de la parte interesada"
  with the Dirección General de Impuestos Internos as the authority
  that declares it. Clock state is tracked (start, running, materialized)
  but the system shall NOT auto-extinguish liability on a prescripción
  date (the declaration is DGII's, per the definition).
  (LB-002; EVID-339)
- **SV-TAX-FR-355:** The system shall anchor the *ejercicio comercial*
  (commercial/fiscal year) as the calendar-year constant — "El
  comprendido desde el uno de enero al treinta y uno de diciembre de
  cada año" — for every fiscal-period record this layer touches,
  closing the corpus-wide calendar-year assumption (now anchored at
  75_; consumed everywhere by config, never per-file redefined).
  (LB-003; EVID-339)
- **SV-TAX-FR-356:** The system shall resolve the authority identity
  "Administración Tributaria" as the Ministerio de Hacienda by means of
  its Direcciones Generales (DGII for internal taxes and their
  recaudación), recording the DGII/DGT authority-split vocabulary as a
  documentation-level authority-resolution row for venue fields on
  declarations, payments and refund surfaces (which office liquidates
  vs which office collects).
  (LB-001; EVID-339)
- **SV-TAX-FR-357:** The system shall carry the interpretation-methods
  block as a documentation-level constraint set: *analogía* is a means
  of law INTEGRATION, not interpretation, and "mediante ella no pueden
  crearse tributos ni exenciones" (no requirement may be inferred into
  existence by analogy); the *precio de mercado* factors (tamaño de los
  negocios, actividad o giro, nivel económico, participación en el
  mercado) are the root of in-specie valuation — consumed by
  payroll/08's remuneration valuation by id in this wave's T4, never
  duplicated here; and *imágenes ópticas no modificables* (optical,
  unalterable document images under an AT-authorized electronic
  safekeeping system) is the archive-tier kin of the CT 147 conservation
  regime (SOQ-28 archive tiers, by pointer).
  (LB-003; LB-004; EVID-339)

### 3.2 Representation & domicilio (Arts. 5-8, 28-30 + def. 2.9)

- **SV-TAX-FR-358:** The system shall model fiscal representation as
  two distinct credential kinds on the company/partner record: the
  REPRESENTANTE LEGAL — shown by written notice to the Administración
  and accredited by the full set *escritura de constitución, punto de
  acta de elección y la credencial debidamente inscrita* — and the
  GESTIÓN-SCOPED APODERADO — designated in writing with a *poder* in
  which the entrusted management ("la gestión que se le encomienda
  realizar") is stated "en forma clara e inequívoca" (for personas
  jurídicas the designation is made by the representante legal); the
  representation register is a maintained registry (AT keeps its own;
  the implementation keeps the credential set with dates and scope).
  (LB-006; LB-008; EVID-341)
- **SV-TAX-FR-359:** The system shall distinguish DOMICILIO/address
  types for tax procedure: the *domicilio fiscal*/notification address
  vs the *dirección procesal* — "el lugar que para efectos procesales,
  se ha señalado para recibir notificaciones, definido por los
  apoderados designados por escrito" — and shall apply the
  change-effective semantics of Art. 28: a notification address changes
  ONLY on the conjunction of definitive closure of operations at the
  place, total disengagement of the business activities, abandonment
  and *traslado físico del local* (physical relocation); where no
  address is designated, the fallback-place rule of Art. 29 (CT 54
  a)/b) y 55 a)/b) places) applies — recorded as a fallback flag, the
  fallback selection itself being AT-side.
  (LB-007; EVID-341)
- **SV-TAX-FR-360:** The system shall expose the expediente-access
  documentary set as a documentation-level checklist (awareness): the
  request in duplicate; the apoderado adding *testimonio de poder* (or
  notary-certified copy); personas jurídicas adding the *escritura de
  constitución*, the *punto de acta de elección* and the vigent
  registered credential; and expedients never consultable outside the
  facilities (AT-side constraint with no client-side surface beyond the
  checklist artifact).
  (LB-008; EVID-341; layer: shared — documentation)

### 3.3 Registration & agent designation (Arts. 24-27)

- **SV-TAX-FR-361:** The system shall model registration status:
  inscripción of contribuyentes within the Código's deadline, the AT's
  registry of inscribed contribuyentes mirrored on the partner record,
  and the NRC card data — number plus the fact that "La tarjeta, en
  original, acreditará la calidad de contribuyente" (card-in-original
  as the accreditation fact, with issuance/attribution dates).
  (LB-009; EVID-342)
- **SV-TAX-FR-362:** The system shall record the NRC-card presentation
  duty as an AWARENESS note (no print-era enforcement): for IVA
  purchases/services of the business giro the card "deberá ser
  presentada siempre… a fin de exigir el Comprobante de Crédito Fiscal
  correspondiente" — the 2001 ancestor of receiver NIT/NRC document
  fields; the DTE stack (CAT-006 receiver identification, e-invoicing
  by id) governs current behavior, which this row never overrides.
  (LB-009; EVID-342; layer: shared — awareness)
- **SV-TAX-FR-363:** The system shall implement the corporate-event
  notice checklist: an aviso obligation covering "disolución,
  liquidación, fusión, transformación y cualquier modificación de la
  sociedad", each event carrying the certified documentary attachment
  set — *Certificación del Punto de Acta de Asamblea General* and
  *testimonio de la escritura* (original or notary-certified copy,
  registered in the Registro respectivo) — with the CT 86 15-day clock
  co-anchored on 05_ (EV05:EVID-059 change-clock set, by pointer; the
  clock computation consumes the días-hábiles engine SV-FREP-FR-202..204
  only where the CT text makes it hábiles — CT 86's own term governs).
  (LB-010; EVID-342; CT 86 co-cite via 05_)
- **SV-TAX-FR-364:** The system shall carry the AT's separate registry
  of retention/perception agents as the agent-designation flag surface:
  the AT "deberá llevar registros respecto de los Agentes de Retención
  y Percepción que designe" — a partner-level designation record
  (kind: retención · percepción; designation act reference and date)
  that this wave's taxation/13 designation FRs consume BY ID
  (SV-TAX-FR-306, `13_iva-retentions.md` — never restated here); the
  designation LIST itself is administered data (config surface, no
  invented entries).
  (LB-009; EVID-342; TAX 13-file SV-TAX-FR-306 by id)

### 3.4 Declarations: the state model (Arts. 31-35)

- **SV-TAX-FR-365:** The system shall enforce the declaration-preparation
  invariant that the absence of official forms NEVER excuses the
  obligation: "La falta de tales formularios no libera de la obligación
  de declarar y pagar el impuesto dentro del plazo legal" — return
  computation and filing-deadline surfaces must never gate on form
  availability.
  (LB-011; EVID-343)
- **SV-TAX-FR-366:** The system shall implement the declaration
  reception state model: the receiving channel REVIEWS but "en ningún
  caso podrá modificarlas" — detected errors are FLAGGED, corrections
  belong to the sujeto pasivo — and the declaration MUST be received
  "aún cuando los sujetos pasivos se negaren a corregir los errores",
  EXCEPT errors that "conlleven la disminución del valor a pagar o
  aumente el saldo a favor" (payable-reducing / saldo-a-favor-increasing
  errors block acceptance until corrected). The reception state enum:
  received · received-with-flagged-errors · blocked-payable-reducing-
  error.
  (LB-012; EVID-343)
- **SV-TAX-FR-367:** The system shall implement the amendment
  CLASSIFICATION GATE (CT 103 anchor): a modification may refer to
  "los datos, informaciones, cálculo del impuesto, u otros elementos
  constitutivos de la naturaleza propia de cada impuesto" (the
  modification taxonomy); originals modified "por la omisión de
  requisitos formales o errores de la misma naturaleza" are NOT
  incorrect declarations (no incorrect-declaration state, no sanction
  surface), while modifications that give "lugar al pago original o
  complementario del impuesto" ARE incorrect declarations per CT 103.
  The classification flag (formal-defect-only vs payment-affecting)
  rides every amended return and feeds fiscal-reporting/01's
  modificatoria engine BY ID (SV-FREP-FR-040 — wired in this wave's
  T3; never restated here).
  (LB-013; EVID-343; FREP 01-file SV-FREP-FR-040 by id)
- **SV-TAX-FR-368:** The system shall carry the Art. 35 electronic-
  filing invariant set as a DOCUMENTATION LAYER for portal connectors
  (awareness — the AT's own channel guarantees, not client logic):
  "encriptado de los procesos, firma digital o electrónica, facilidades
  para cambios de clave por el sujeto pasivo autorizado y recibo de
  verificación electrónico… como constancia de recibido" — an
  authenticated-channel + electronic-receipt contract that any
  declaration-connector spec against modern DGII surfaces must satisfy
  in its current form.
  (LB-014; EVID-343; layer: shared — documentation)

### 3.5 Payments & extinction (Arts. 13-18)

- **SV-TAX-FR-369:** The system shall carry the extinction-mode enum on
  the tax-liability ledger: "a) por el pago. b) Por compensación; c)
  Por confusión; y d) Por prescripción" — with *confusión* defined as
  the State converging "simultáneamente la calidad de deudor y
  acreedor" of the obligation; the enum carries NO condonación mode
  (condonation is not a 75_-recognized extinction path; no such
  transition may be modeled).
  (LB-015; EVID-344/345)
- **SV-TAX-FR-370:** The system shall encode the payment-window rows:
  (a) any person may pay a debtor's tax ("Cualquier persona puede
  pagar… a nombre de un deudor tributario" — third-party payment
  supported with payer ≠ debtor); (b) oficio liquidations are payable
  "dentro de los dos meses posteriores contados a partir de la fecha
  en que la resolución liquidatoria del impuesto quede firme" (2-month
  window from firme — dated config row resolving as-of the firme event,
  D15); (c) autoliquidado payments at colecturías/banks/AT-designated
  places as the 2001 print's venue list (awareness — portal payments
  now; venue fields are config, never hardwired to physical places).
  (LB-016; EVID-344)
- **SV-TAX-FR-371:** The system shall model the multa payment flow:
  imposed multas pay "dentro de los treinta días siguientes a aquel en
  que quede firme la resolución sancionatoria" (30-day window from
  firme — dated row, D15); a VOLUNTARY self-assessment path exists
  ("autoliquidar en forma voluntaria… aplicando la atenuante
  pertinente en los casos que proceda") with the atenuante as a config
  input; and the absence of voluntary self-assessment "no impide la
  recepción de la declaración correspondiente" — multa state NEVER
  blocks return reception; non-self-assessed multas are imposed by
  resolución (AT-side).
  (LB-017; EVID-344)
- **SV-TAX-FR-372:** The system shall carry the *mandamiento de
  ingreso* mechanics as a payment-document contract (awareness for the
  surviving contexts): one mandamiento per liquidation, provided by the
  AT, completed "en forma clara, precisa, inteligible, sin borrones,
  tachaduras o enmendaduras, tanto el original como sus copias" — the
  ISR/ITR and IVA-retentions-to-non-domiciled contexts of the 2001
  print, surviving operationally in the import-services flow
  (`13_iva-retentions.md` SV-TAX-FR-303 and
  `15_iva-declaration-interfaces.md`, by pointer). Mora interest is governed
  by an EXTERNAL instrument ("el Decreto Legislativo correspondiente",
  CT 75-b) — config-gap: the interest rate/curve is NEVER hardcoded;
  it resolves from the external instrument's config rows.
  (LB-016; LB-018; EVID-344; TAX 13/15-files by id)

### 3.6 Compensación, prescription & imprescriptibilidad (Arts. 19-23)

- **SV-TAX-FR-373:** The system shall implement the compensación GATE:
  credits may be compensated against debits of *tributos internos* —
  oficio with the interested party's knowledge or on request — only
  when (a) the credits were PAID IN CASH ("siempre que los pagos
  hubieren sido hechos en efectivo" — credits settled in kind or by
  compensation do not qualify), (b) BOTH sides are "firmes, líquidos y
  exigibles", and (c) the CT Art. 76 imputation order is respected;
  the Quincena-25 credit/certificado carry-forward consumer is
  SV-TAX-FR-174 (`01_isr-framework.md`, by id — never restated here).
  (LB-019; EVID-345; TAX 01-file SV-TAX-FR-174 by id)
- **SV-TAX-FR-374:** The system shall encode the prescription
  dies-a-quo config rows AS DATED 2001-PRINT VALUES, gated by the OQ-2
  pin-current-CT condition (never constants, never auto-enforcement —
  see FR-354's pleaded-only semantics): prescription operates "en
  contra del Fisco, una vez transcurridos 10 años" counted (1) for
  taxpayer-self-liquidated tax, "a partir del día siguiente a aquel en
  que concluyó el término legal para pagar o el de su prórroga si la
  hubiere"; (2) for oficio liquidations and isolated multas, "a partir
  del día siguiente al vencimiento del plazo para el pago, establecido
  en el artículo 74 inciso 2º del Código"; prescription materializes
  only when the Código's requisites are met "tanto para lo principal
  como para lo accesorio" (Art. 22).
  (LB-020; EVID-345; OQ-2 gated)
- **SV-TAX-FR-375:** The system shall implement the Art. 23
  IMPRESCRIPTIBILIDAD invariant: un-entered retentions are collectible
  "EN CUALQUIER TIEMPO" — the AT may demand the agent enter retained
  and un-entered sums and impose the corresponding sanction with NO
  limitation clock ever starting; every retention-liability ledger line
  shall carry a perpetual-exposure flag that activates when the entero
  deadline lapses unmet and never time-expires. The 75%-sanction kin is
  CT 247 (05_-encoded, by pointer); the agent-side twin is Art. 133
  (FR-378).
  (LB-021; EVID-345; CT 247 by pointer)

### 3.7 Refunds (Arts. 129-135)

- **SV-TAX-FR-376:** The system shall model the refund case lifecycle:
  a resolución is DEFINITIVA in sede administrativa when (a) no
  apelación is filed within the legal term, (b) the apelación is
  declared inadmisible, or (c) the apelación fallo issues (the
  firme-trigger vocabulary for every downstream clock); a devolución
  requires the prior Fondo-General verification (the sums "han
  ingresado al Fondo General" — Tesorería informe) and resolves within
  "los 120 días siguientes a la fecha de presentación de la solicitud"
  (120-day clock from solicitud, D15); multas and intereses follow the
  same path "cuando la cuantía de lo pagado sea disminuida por
  resolución firme" (firme-reduced refunds).
  (LB-022; EVID-355)
- **SV-TAX-FR-377:** The system shall model the asalariado
  excess-retention devolución: natural persons domiciled in the country
  whose income derives EXCLUSIVELY from salaries, in the Ley ISR
  quantities, "tendrán derecho a la devolución de las cantidades
  retenidas que resultaren en exceso después de liquidado el impuesto"
  upon solicitud — with the PRECONDITION that the AT verifies "que el
  agente de retención ha efectuado los enteros de las cantidades
  retenidas" (enteros-verification gate on the agent before the
  worker's refund); the modern consumer is the renta-en-línea
  devolución surface (66_-70_ instruments, by pointer).
  (LB-023; EVID-355)
- **SV-TAX-FR-378:** The system shall implement the Art. 133
  two-year caducidad for the AGENT's erroneous-retention refund
  claims: the sujeto pasivo that made the undue collection of retained
  and entered sums may claim the devolución only "dentro del término
  de dos años contados a partir de la fecha del pago indebido" (clock
  from the pago indebido date, D15), "sin perjuicio de la acción civil
  a que haya lugar por parte de los sujetos a quienes les efectuó la
  retención indebidamente" (the affected retainee's civil action is
  preserved and tracked as an exposure note, not a managed clock) —
  the agent-side twin of FR-375's perpetual AT exposure: the AT never
  loses its claim; the agent gets exactly two years.
  (LB-024; EVID-355; pairs FR-375)
- **SV-TAX-FR-379:** The system shall carry the fianza (bond)
  clause set as an awareness config template for garantía records
  under CT 222/225: the statutory minimum clause runs the fianza "por
  el término de dos años contados a partir de la expedición de la
  autorización" with the AUTOMATIC-DEPOSIT mechanism — one month
  before expiry, absent a payment informe, the afianzadora deposits
  the total or partial suma afianzada with the Dirección General de
  Tesorería.
  (LB-025; EVID-355; layer: odoo — config template)

### 3.8 Sanctions & deuda tributaria architecture (Arts. 136-143)

- **SV-TAX-FR-380:** The system shall implement the CT 238-b sanction
  BASE computation rule: when the late-declaration sanction applies
  and retentions have been made AND entered, or anticipos a cuenta
  paid, "la referida sanción recaerá únicamente sobre la porción del
  impuesto a pagar, excluyendo el monto retenido y enterado y el
  anticipo a cuenta ingresado al Fondo General de la Nación" — the
  sanction base = payable portion only; the CT 238 percentages
  themselves are 05_-encoded (by pointer, never restated).
  (LB-026; EVID-356)
- **SV-TAX-FR-381:** The system shall encode the reincidencia windows
  AS DATED 2001-PRINT config-gap rows gated by OQ-2 (never constants):
  reincidencia requires (a) a "sentencia o resolución firme" sanctioning
  the first infraction, (b) a NEW infraction of the SAME obligation,
  and (c) commission within the sanction-caducidad window — "tres años
  contados desde el día siguiente en que se cometió la primera
  infracción" when the taxpayer liquidated within the legal term, or
  "cinco años" when the liquidation was never filed or was filed
  extemporáneamente; *reiteración* qualifies by "la concurrencia del
  acto o hecho tipificado como infracción" (concurrency of the
  typified act).
  (LB-027; EVID-356; OQ-2 gated)
- **SV-TAX-FR-382:** The system shall implement the deuda tributaria
  architecture: granularity is PER-EJERCICIO PER-CONTRIBUYENTE —
  "habrá tantas deudas tributarias, como ejercicios impositivos
  diferentes con respecto a un mismo contribuyente"; the principal is
  born "a partir de la media noche del último día del ejercicio o
  período impositivo" (midnight of period end); intereses run "desde
  el día en que se incurre en mora"; multas liquidadas de oficio from
  the day the imposing resolution "quede firme"; and the debt is
  "única e indivisible independientemente que la cosa debida sea
  fraccionable" — satisfaction requires "el entero total de la suma
  debida" (no partial-discharge state; partial payments are
  imputations, never discharges).
  (LB-028; EVID-356)

### 3.9 Books & records regime (Arts. 73-90)

- **SV-TAX-FR-383:** The system shall implement the book-form and
  backlog-limit KPIs: anotaciones in chronological order in "libros
  empastados y foliados en forma correlativa" (bound, correlatively
  foliated — an attribute of the legal-books archive surface); the
  general-books backlog limit — "no podrá permitirse un atraso mayor
  de dos meses en las anotaciones, contados desde el día siguiente en
  que se efectuó la operación" (adjustments from the day the
  contabilización circumstance arises); and the IVA-register limit —
  "no podrá permitirse un atraso mayor a quince días, conforme a lo
  establecido en el artículo 141 literal a) del Código" (CT 141-a
  anchor; CT 242 backlog sanctions are 05_-encoded, by pointer). The
  limits surface as compliance KPI monitors (dated rows; the 15-day
  IVA/2-month books monitors), not posting blockers.
  (LB-029; EVID-350)
- **SV-TAX-FR-384:** The system shall enforce the separate-registration
  invariant: operations recorded "en forma separada diferenciando unas
  y otras", with the related "costos, gastos, y créditos fiscales"
  separately registered and identified per type of operation or
  activity — the ledger-separation root that the prorrata engine
  consumes BY ID (SV-TAX-FR-269..283, `11_iva-pro-rata-remanente.md`
  — the prorrata computation is never restated here).
  (LB-030; EVID-350; TAX 11-file SV-TAX-FR-269..283 by id)
- **SV-TAX-FR-385:** The system shall carry the computerized-systems
  clause as an implementation-archive DELIVERABLE SPEC (shared layer):
  the taxpayer "deberá conservar como parte integrante de la misma
  toda la documentación relativa al diseño del sistema, los diagramas
  del mismo y los programas fuente cuando proceda, así como las bases
  de datos" for the CT 147 term, all put at the Administración's
  disposition "así como el equipo y sus técnicos, cuando ésta lo
  requiera" — the implementation must retain design documentation,
  diagrams, source where applicable and database access, and the
  deployment record must evidence the equipment-and-technicians access
  duty.
  (LB-031; EVID-350; layer: shared — deliverable spec)
- **SV-TAX-FR-386:** The system shall carry the 75_ book-column
  specifications as HISTORICAL COLUMN TEMPLATES (awareness): the IVA
  books' column specs (ventas a contribuyentes · ventas a consumidores
  · compras), the inventory-register minimum columns (fecha;
  operación with document/partida reference — compras a proveedores,
  devoluciones de clientes, retiros…) and the export annex are the
  2001 print's book architecture; the F-07 annex engines are the
  MODERN consumers (`fiscal-reporting/01..05`, SV-FREP-FR-016/023/040
  by id — column authority lives there, never here); anulaciones book
  in the month of occurrence (the anulación-booking rule).
  (LB-032; EVID-350; FREP 01-file SV-FREP-FR-016/023/040 by id)
- **SV-TAX-FR-387:** The system shall record the contador/assistant
  tier awareness set (no operative gating): the contador público's
  Consejo-de-Vigilancia authority vs the assistant tiers — "Bachilleres
  en Comercio y Administración opción contador o Bachiller Técnico
  Vocacional Comercial opción contaduría" with their Ministerio de
  Educación accreditation registry data — who "no pueden realizar
  funciones reservadas exclusivamente al contador público autorizado
  por el Consejo de Vigilancia"; recorded as book-authorization
  metadata (who keeps the books), never as a posting rule.
  (LB-032; EVID-350; layer: odoo — metadata)

### 3.10 Notifications & fiscalización — awareness (Arts. 3-4, 9, 108-128)

- **SV-TAX-FR-388:** The system shall carry the notification mechanics
  as DOCUMENTATION-LEVEL knowledge (AT-side procedure; no client
  surface beyond deadline-tracking context): hábil hours "de las seis
  de la mañana a las siete de la tarde"; the night-trade carve-outs of
  CT 172 "otros similares" (restaurantes, hoteles, moteles, hospedajes
  o casa de huéspedes, casinos y discotecas); *esquela* constructive
  service deemed complete AT fijación (Arts. 111-113); the
  edicto/72-hour appeal-clock rules (Art. 114 zone); and the
  ID-document list for CT 181.f — "carné electoral, documento único de
  identidad, pasaporte, licencia de conducir, tarjeta de afiliación
  del ISSS, carné de INPEP" — CAT-006 kin for partner-ID-type configs.
  (LB-033; EVID-353; layer: shared — documentation)
- **SV-TAX-FR-389:** The system shall implement the audit-response
  export bundle as a DELIVERABLE SPEC (shared layer): on fiscalización,
  the taxpayer must produce — period-sorted ("arreglados en relación
  con cada período que comprenda el ejercicio comercial, por orden de
  fecha y asientos de la contabilidad") — the books and registers
  (incl. IVA/inventory controls), inventarios inicial y final, the
  signed basic EEFF + anexos, the monthly balanzas/balances de
  comprobación + year-end adjusted saldos, comprobantes and supporting
  documents, COPIAS ORIGINALES of the tributos' declarations, the
  "Catalogo de cuentas y manual de aplicación" [sic print] and the
  external-auditor/dictamen informs when applicable. The catálogo de
  cuentas y manual structure is owned by the chart-of-accounts file
  (SV-COA-FR-022..054, `02_coa-structure.md`, by id — never restated
  here); this FR owns the bundle assembly and period-sorting spec.
  (LB-034; EVID-354; COA 02-file SV-COA-FR-022..054 by id)
- **SV-TAX-FR-390:** The system shall enforce the consulta no-toll and
  individuality rules as configuration-behavior invariants (awareness
  level): consulta answers' effects "son de aplicación individual" —
  "en ningun caso dicha aplicación se extenderá ningun otro sujeto
  pasivo" [sic "ningun"] — so a consulta answer configured in the
  system NEVER gates or recalculates another subject's deadline or
  determination; "La presentación de la consulta no interrumpirá los
  plazos" — filing a consulta never tolls any compliance deadline (no
  deadline-freeze on consulta state); no recurso lies against the
  contestación itself (only against acts applying its criteria); guías
  de orientación are orientation-only and freely modifiable by the AT
  (non-binding citation discipline); denuncias are confidential
  (identity reserved). AT-side mechanics (consulta processing) are out
  of scope; only the no-toll/individuality invariants bind client
  behavior.
  (LB-005; EVID-340; layer: odoo — config invariant)

### 3.11 Print-era historical block + norm hierarchy (Arts. 36-55, 58-72, 144-146)

- **SV-TAX-FR-391:** The system shall carry the document-validity
  doctrine and transit rules as AWARENESS (the doctrinal base survives
  under DTE): only Código-established documents support transfers,
  services and exports — "no será valido el uso de cualquier otro
  documento" and other laws' emission documents "no sustituye la
  obligación" of CT 107 documents; goods in transit must port NR/
  Factura/CCF "durante el traslado, circulación o tránsito" and
  exhibit them to AT delegates; and legal documents must include "las
  direcciones de todas las sucursales si las hubiere" (with the
  volume/name-change information reliefs) — the sucursal-address
  accumulation surviving conceptually in DTE emitter establishment
  data (e-invoicing surfaces, by pointer).
  (LB-035; EVID-346; layer: shared — awareness)
- **SV-TAX-FR-392:** The system shall record the imprenta/AT-correlative
  chain as SUPERSEDED for DTE emitters (citation-rule awareness):
  printed documents carried the DGII authorization number, imprentas
  verified the NRC card original and refused repositions and
  "documentos con numeración repetida", keeping the CT 116.f client
  list ("Nombre del cliente, NIT, NRC, tipo de documento emitido,
  rango impreso… 'desde' – 'hasta'"); R8 rules for DTEs (numeroControl
  with NO AT-correlative authorization — CT 115-A lifted it) and the
  Normativa DTE govern current emission; this row documents why
  pre-DTE documents carry AT authorization numbers (historical-document
  ingestion context), never a live authorization flow.
  (LB-036; EVID-346; layer: shared — citation rule)
- **SV-TAX-FR-393:** The system shall carry the third-account and
  export-factura mechanics as AWARENESS while the CAT-002 CLE/DCLE
  document types govern: comisionistas/consignatarios keep issued
  copies and emit the monthly *Comprobante de Liquidación* with the
  "desde –hasta" summary per document type (values net of tax) and the
  débito fiscal "reflejado por separado", booked by the mandante "en
  el Libro de Ventas a Contribuyentes"; the *Factura de Exportación*
  (pre-FEXE ancestor) carries "un número correlativo independiente y
  diferente" from local facturas, was "preimpresa por imprenta
  autorizada", and booked per the print's cross-ref to "los artículos
  81 y 82 del presente Reglamento" [sic — the consumer-sales book is
  Art. 83; print cross-ref anomaly, OQ-7]; the perception agent's CCF
  consigns "en forma separada el impuesto percibido en calidad de
  agente" (the ivaPercibido separate-consignment root surviving in DTE
  CCF structures).
  (LB-037; EVID-347; layer: shared — awareness)
- **SV-TAX-FR-394:** The system shall record the máquinas
  registradoras/tiquete/formulario-único block as HISTORICAL AWARENESS
  (R12: tiquetes banned since 01-ene-2025; CT 115-A + Normativa DTE
  govern): hardware identification and "contador automático
  inviolable"; tiquete content specs; X/Z reports reconciled to the
  consumer-sales book (the EOP monthly-window ancestor); cinta de
  auditoría paper→electrónica/bitácora; the colones gate — "igual o
  superiores a ¢ 4,970.00" [sic — dated colones value, NEVER converted
  or encoded] above which full receiver data or a preprinted factura
  was required; the DEVOLUCION-stamp/negative-reflection ritual; "no
  estará permitido por motivo alguno, retroceder la numeración"; the
  formulario único's system-assigned doc-type/correlativo concept (the
  DTE emission-engine ancestor); the contingency facturas stock —
  mapping conceptually to DTE contingencia flows (e-invoicing, by
  pointer); and the software-disclosure checklist (license, equipment,
  et al. — Art. 50 d)1-8) as an AT-facing implementation-doc artifact.
  (LB-038; EVID-348; layer: shared — historical)
- **SV-TAX-FR-395:** The system shall record the dictamen block (Arts.
  58-72) as a HISTORICAL BLUEPRINT only (OQ-3: the mandatory-dictamen
  regime was restructured post-2001; never operative FRs): the
  nombramiento/aviso clocks (5 months / 30 días calendario), the
  dictamen's formal-vs-substantive incumplimiento separation with
  monetary quantification, the EEFF presented per "las Normas
  Internacionales de Contabilidad" (the NIC reference is SOQ-46 kin —
  Consejo-de-Vigilancia criteria first, N-wave by pointer), and the
  anexo set's IVA determination chain (b.3) restating the prorrata and
  exporter-reintegro ledgers — a validation blueprint whose live
  computations are already encoded from the operative instruments
  (`11_iva-pro-rata-remanente.md` SV-TAX-FR-269..283 and
  `14_iva-exports-refunds.md`, by id — never restated).
  (LB-039; EVID-349; TAX 11-file SV-TAX-FR-269..283 by id; layer:
  shared — historical)
- **SV-TAX-FR-396:** The system shall carry the transitorios discipline
  and the Art. 146 authority root as a NORM-HIERARCHY citation rule
  (shared layer): substantive norms apply by hecho-generador date —
  facts before the CT's vigencia under the then-current law, facts
  after under the CT ("las normas sustantivas… ocurridos con
  anterioridad a la vigencia… se regirán por las disposiciones legales
  vigentes al momento de su ocurrencia"); procedural norms apply
  immediately to trámites initiated under the CT, pending trámites
  finishing under prior law (the two-vintage discipline every cutover
  — DTE 2023-2025 included — reuses; D15/D16 kin); old IVA
  books/stationery usable to agotamiento when properly authorized; and
  Art. 146 — the AT "está facultada para dictar las normas
  administrativas generales" within the CT and the tax laws — is the
  AUTHORITY ROOT under which the F-forms, catalogs and DGII resoluciones
  (34_/35_/50-52_ instruments) sit: every such instrument's provenance
  chain cites 75_ Art. 146.
  (LB-040; EVID-357; layer: shared — citation rule)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the 10-year prescription, 3y/5y
reincidencia, 2-month/15-day/30-day/120-day/2-year clocks enter as
dated config rows with instrument provenance (75_ + article), gated per
§2's OQ-2/OQ-3/OQ-4 bars; procedural clocks resolve AS-OF their trigger
event (firme date, pago indebido date, solicitud date, month-end) per
D15. Layer semantics: config/ledger surfaces living in the LGPL client
(`odoo`); documentation/deliverable specs shared (`shared`); see §5.

**Limitation-tracking vocabulary (FR-354/374/375/378):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.limitation.category (new) | code, kind, clock_basis, authority | char / select / char / char | kind: caducidad (self-materializing) · prescripcion (pleaded; DGII declares); clock_basis: simple_transcurso · alegacion; e.g. refund_claims · sanction_power · fiscalizacion · prescription_fisco | FR-354 |
| l10n_sv.fiscal.period (SV extension) | l10n_sv_limitation_state_ids | o2m | per-category clock instances (start = dies-a-quo; state: running · materialized; materialization NEVER auto-extinguishes liability for prescripción) | FR-354, FR-374 |
| l10n_sv.prescription.config (new, DATED) | tax_kind, dies_a_quo_rule, years, valid_from, instrument | select / select / int / date / char | autoliquidado → day_after_legal_payment_term; oficio_o_multas → day_after_ct74_2_window; years = 10 (2001 print — OQ-2 pin-current-CT gate before activation) | FR-374 |
| account.move.line (retention liability, SV extension) | l10n_sv_perpetual_exposure | boolean (stored) | activates when the entero deadline lapses unmet; never time-expires (Art. 23) | FR-375 |
| l10n_sv.refund.case (new) | kind, solicitud_date, fondo_general_verified, resolution_deadline, firme_trigger | select / date / boolean / date / select | kind: asalariado_excess · entered_excess · firme_reduced_multas_intereses · agent_erroneous_retention; resolution_deadline = solicitud + 120 días; agent_erroneous_retention additionally carries caducidad = pago_inebido_date + 2 años (Art. 133); civil_action_exposure note flag | FR-376, FR-377, FR-378 |

**Representation, domicilio & registration (FR-358/359/361/363/364):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner (SV extension) | l10n_sv_representation_ids | o2m | kind: representante_legal (escritura + punto_de_acta + credencial_inscrita) · apoderado (poder ref + gestión scope text); designation date; for PJ the designator is the representante legal | FR-358 |
| res.partner (SV extension) | l10n_sv_notification_address_kind | select | domicilio_fiscal · direccion_procesal · fallback_ct54_55 (fallback flag when none designated) | FR-359 |
| res.partner (SV extension) | l10n_sv_registered, l10n_sv_nrc_card | boolean / char | inscripción state; NRC card number + accreditation fact (card in original) + issuance date | FR-361 |
| l10n_sv.corporate.event (new) | event_kind, notice_date, attachments, deadline | select / date / m2m / date | disolucion · liquidacion · fusion · transformacion · modificacion; attachments: certificación punto de acta + testimonio escritura (original or notary-certified, registered); deadline per CT 86 (05_ co-anchor) | FR-363 |
| res.partner (SV extension) | l10n_sv_at_agent_designation_ids | o2m | kind: retencion · percepcion; designation act ref + date — consumed by SV-TAX-FR-306 (13-file) | FR-364 |

**Declaration state & payments (FR-365..372):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (declaration, SV extension) | l10n_sv_reception_state | select | received · received_with_flagged_errors · blocked_payable_reducing_error (no-modification channel invariant) | FR-366 |
| account.move (declaration, SV extension) | l10n_sv_amendment_class | select | formal_defect_only (NOT incorrect) · payment_affecting (incorrect per CT 103); taxonomy tag: datos · informaciones · calculo · otros_elementos — feeds SV-FREP-FR-040 | FR-367 |
| account.move (tax liability, SV extension) | l10n_sv_extinction_mode | select | pago · compensacion · confusion · prescripcion (NO condonacion value exists) | FR-369 |
| l10n_sv.payment.window (new, DATED) | kind, window, anchor | select / char / select | oficio_liquidation: 2 months from firme; multa: 30 days from firme; third-party-payer allowed (payer ≠ debtor) | FR-370, FR-371 |
| account.payment (SV extension) | l10n_sv_mandamiento_ref | char | mandamiento de ingreso per liquidation (clean/precise/no enmendaduras contract — document template constraint) | FR-372 |
| l10n_sv.interest.config (config-gap) | instrument_ref, curve | char | external D.L. governs mora interest (CT 75-b); NEVER hardcoded — empty until the instrument is sourced | FR-372 |

**Compensación, sanctions & deuda (FR-373/380/381/382):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.compensation.gate (new) | credit_paid_in_cash, both_sides_status, imputation_order | boolean / select / char | efectivo-paid only (in-kind/settled-by-compensation credits rejected); firmes · líquidos · exigibles on both sides; CT 76 order; mode: oficio_con_conocimiento · a_peticion_de_parte | FR-373 |
| l10n_sv.sanction.base (new) | payable_portion, retained_entered_excluded, anticipos_excluded | monetary / boolean / boolean | CT 238-b base = payable portion only; exclusions computed from entero and anticipo ledger facts (percentages 05_-encoded, by pointer) | FR-380 |
| l10n_sv.reincidencia.config (new, DATED) | first_sanction_firme, same_obligation, window_kind, years | boolean / boolean / select / int | window: 3y (timely self-liquidation) · 5y (unfiled/extemporaneous) — 2001 print, OQ-2 gate; reiteración = concurrency of the typified act | FR-381 |
| account.move (deuda ledger, SV extension) | l10n_sv_deuda_ejercicio, l10n_sv_principal_birth, l10n_sv_indivisible | m2o / datetime / boolean | per-ejercicio per-contribuyente granularity; principal born midnight of period end; indivisibility — no partial-discharge state | FR-382 |

**Books/backlog & bundles (FR-383/385/386/389):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.backlog.kpi (new, DATED) | register_kind, max_delay | select / char | iva_registers: 15 days (CT 141-a) · general_books: 2 months; monitor surface (sanctions 05_-encoded, by pointer) | FR-383 |
| l10n_sv.impl.archive (shared deliverable) | design_docs, diagrams, source_when_proceeds, databases, access_duty_evidence | binary refs / boolean | CT 147 term retention + equipment-and-technicians access duty record | FR-385 |
| l10n_sv.audit.bundle (shared deliverable) | components, period_sorted | m2m / boolean | EEFF+anexos · balanzas mensuales/saldos ajustados · comprobantes · declaraciones (copias originales) · catálogo+manual (COA 02-file by id) · auditor/dictamen informs; sorted per período/fecha/asiento | FR-389 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = configuration/ledger surfaces
living in the LGPL client; `shared` = documentation-level constraints
and deliverable specs (implementation archive, audit bundle,
historical/citation-rule awareness); no `saas` rows — nothing here
touches DTE generation or transformation (e-invoicing rows cited by
id). Model names are stable across Odoo 17/18/19/20 (`res.partner`,
`account.move`, `account.move.line`, `account.payment`); version-
specific behavior is recorded per row where a legal vintage exists.
D15 doctrine (binding): every procedural clock resolves as-of its
trigger event (firme, pago indebido, solicitud, month-end); dated legal
parameters are immutable dated rows with instrument provenance; the
vintage-note rule of §2 rides every row.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-354 | odoo | l10n_sv.limitation.category + l10n_sv.fiscal.period | limitation vocabulary | caducidad self-materializing vs prescripción pleaded (DGII declares — no auto-extinguish); config categories only |
| FR-355 | odoo | company/fiscal-period config | calendar-year constant | Jan-1..Dec-31 ejercicio comercial; corpus-wide anchor, no per-file redefinition |
| FR-356 | shared | venue config rows (documentation) | MH/Direcciones Generales identity | Authority-resolution vocabulary for liquidates-vs-collects venue fields; documentation level |
| FR-357 | shared | documentation constraints | analogía bar · precio-de-mercado factors · imágenes ópticas | Analogía never creates tributos/exenciones; precio factors consumed by payroll/08 (T4 wiring, by id); imágenes → SOQ-28 pointer |
| FR-358 | odoo | res.partner | representation_ids | Representante legal credential set vs gestión-scoped apoderado (poder scope text) |
| FR-359 | odoo | res.partner.address types | notification_address_kind | Domicilio vs dirección procesal; change-effective = closure + traslado físico conjunction; fallback flag (CT 54/55) |
| FR-360 | shared | checklist artifact | expediente-access set | Documentation-level; AT-side constraint; no client surface beyond the artifact |
| FR-361 | odoo | res.partner | registered + nrc_card | NRC card data; card-in-original accreditation fact |
| FR-362 | shared | awareness note | card-presentation duty | 2001 ancestor of receiver NIT/NRC fields; DTE stack (CAT-006) governs — never overrides |
| FR-363 | odoo | l10n_sv.corporate.event | event checklist + attachments | Disolución/liquidación/fusión/transformación/modificación; CT 86 15-day clock co-anchored on 05_ (EV05:EVID-059) |
| FR-364 | odoo | res.partner | at_agent_designation_ids | AT registry mirror; consumed by SV-TAX-FR-306 (13-file, by id); list = administered config, no invented entries |
| FR-365 | odoo | declaration-preparation guard | form-availability invariant | Forms' absence never gates computation/filing; 2001 rule, still-true invariant |
| FR-366 | odoo | account.move (declaration) | reception_state | No-modification (flag-only); must-receive-uncorrected EXCEPT payable-reducing/saldo-a-favor-increasing errors |
| FR-367 | odoo | account.move (declaration) | amendment_class | Formal-defect-only ≠ incorrect; payment-affecting = incorrect (CT 103); feeds SV-FREP-FR-040 (frep/01, wired T3) |
| FR-368 | shared | connector documentation | Art. 35 invariant set | Encryption/digital signature/key management/e-receipt — portal-connector spec layer (awareness) |
| FR-369 | odoo | account.move (liability) | extinction_mode | pago/compensación/confusión/prescripción; NO condonación value exists in the enum |
| FR-370 | odoo | l10n_sv.payment.window + account.payment | dated windows + third-party payer | Oficio 2-month from firme; multa 30-day from firme; anyone-may-pay (payer ≠ debtor); venues = config (2001 print awareness) |
| FR-371 | odoo | l10n_sv.payment.window (multa) | self-assessment + atenuante | Voluntary autoliquidación with atenuante config; never blocks return reception |
| FR-372 | odoo | account.payment + l10n_sv.interest.config (gap) | mandamiento + external interest | Mandamiento template contract (no enmendaduras); mora interest = external D.L., NEVER hardcoded (config-gap) |
| FR-373 | odoo | l10n_sv.compensation.gate | efectivo + firme/líquido/exigible + CT 76 | In-kind credits rejected; consumer: SV-TAX-FR-174 (Quincena-25, by id) |
| FR-374 | odoo | l10n_sv.prescription.config (DATED) | 10 años + dies-a-quo rules | 2001-print values; OQ-2 pin-current-CT gate before activation; never auto-enforcement |
| FR-375 | odoo | account.move.line (retention) | perpetual_exposure flag | Un-entered retentions collectible en cualquier tiempo; CT 247 75% sanction kin (05_, pointer) |
| FR-376 | odoo | l10n_sv.refund.case | firme triggers + 120-day clock | Fondo-General verification precondition; firme-reduced multas/intereses same path |
| FR-377 | odoo | l10n_sv.refund.case (asalariado) | enteros-verification gate | Salary-exclusive workers; agent's enteros verified before devolución; renta-en-línea consumer (pointer) |
| FR-378 | odoo | l10n_sv.refund.case (agent claim) | 2-year caducidad from pago indebido | Agent-side twin of FR-375; retainee civil action preserved (exposure note) |
| FR-379 | odoo | garantía config template | fianza clause set | 2-year term from authorization + automatic-deposit clause (DGT); CT 222/225 awareness |
| FR-380 | odoo | l10n_sv.sanction.base | payable-portion-only | CT 238-b developer; excludes retained-and-entered + anticipos; percentages 05_-encoded (pointer) |
| FR-381 | odoo | l10n_sv.reincidencia.config (DATED) | 3y/5y windows | Firme-first + same obligation + within caducidad; 2001 print, OQ-2 gate; reiteración = typified-act concurrency |
| FR-382 | odoo | account.move (deuda) | granularity + indivisibility | Per-ejercicio per-contribuyente; principal midnight-birth; intereses ex mora; multas ex firme; entero total required |
| FR-383 | odoo | l10n_sv.backlog.kpi (DATED) | 2-month/15-day monitors | Books vs IVA registers; CT 141-a anchor; CT 242 sanctions 05_-encoded (pointer); monitors, not blockers |
| FR-384 | odoo | ledger separation guard | per-treatment registration | Costos/gastos/créditos identified per treatment; prorrata input for SV-TAX-FR-269..283 (by id) |
| FR-385 | shared | l10n_sv.impl.archive (deliverable) | design/diagrams/source/db + access duty | CT 147 term retention; equipment-and-technicians access evidence |
| FR-386 | shared | historical column templates | IVA books/inventory/export annex | Awareness templates; F-07 annex engines are modern consumers (SV-FREP-FR-016/023/040, by id); anulación in month of occurrence |
| FR-387 | odoo | book-authorization metadata | contador/assistant tiers | CPA (Consejo de Vigilancia) vs MinEd-accredited assistant tiers; metadata, never a posting rule |
| FR-388 | shared | documentation knowledge | notification mechanics | Hábil hours 6:00-19:00; esquela-at-fijación; edicto/72h; ID list CAT-006 kin; AT-side only |
| FR-389 | shared | l10n_sv.audit.bundle (deliverable) | period-sorted export set | EEFF + declaraciones (copias originales) + catálogo+manual (SV-COA-FR-022..054 by id) + balanzas + comprobantes |
| FR-390 | odoo | config invariant | consulta no-toll/individuality | Answers individual-only ("en ningun caso… ningun otro sujeto pasivo" [sic]); no deadline toll; guías non-binding; denuncias confidential |
| FR-391 | shared | awareness (doctrine) | valid-docs/porteo/sucursal | Doctrinal base survives under DTE; sucursal accumulation → emitter data (e-invoicing pointer) |
| FR-392 | shared | citation rule | imprenta chain superseded | R8 (numeroControl, CT 115-A lifted AT-correlative); historical-document ingestion context only |
| FR-393 | shared | awareness | CL + Factura de Exportación + ivaPercibido | CAT-002 CLE/DCLE govern; Art. 42 "81 y 82" [sic] cross-ref anomaly (OQ-7); FEXE ancestor |
| FR-394 | shared | historical | máquinas registradas block | ¢4,970.00 dated [sic] colones — NEVER converted; R12 tiquete ban; contingency → DTE contingencia (pointer); software-disclosure artifact |
| FR-395 | shared | historical blueprint | dictamen block (58-72) | OQ-3 bar: never operative; NIC reference SOQ-46 kin; prorrata/reintegro live in 11_/14_ files (by id) |
| FR-396 | shared | citation rule (norm hierarchy) | transitorios + Art. 146 | Substantive-by-hecho-generador vs procedural-immediate (two-vintage discipline); Art. 146 = F-forms/catalogs/resoluciones authority root (34_/35_/50-52_) |

Version-regime note (D12/D15): FR-370/371/374/376/378/381/383 carry
dated procedural parameters (windows, dies-a-quo rules, backlog
limits) — each resolves as-of its trigger event, stores the resolved
value on the record (snapshot-on-write), and ships as a dated row with
instrument provenance (75_ + article + EVID id); the OQ-2-gated rows
(FR-374, FR-381) stay inert config until the current CT terms are
pinned. The vintage-note rule (§2) rides every row: 75_ print carries
no REFORMAS block and post-2001 repeal is print-unresolvable (OQ-1/OQ-8).

## 6. Acceptance Criteria

- **AC-001:** Given an amended return whose only modification is the
  correction of a formal defect (an omitted formal requisite), when the
  amendment posts, then the declaration does NOT enter the
  incorrect-declaration state and no sanction surface opens (FR-367);
  given the same period amended with a complementary payment of tax,
  then the declaration IS flagged incorrect per CT 103 and the flag
  feeds the modificatoria engine (FR-367; SV-FREP-FR-040 by id).
- **AC-002:** Given a return presented with an uncorrected error that
  INCREASES the payable amount, when the reception runs, then the
  return is received with the error flagged (receiver cannot modify);
  given an uncorrected error that REDUCES the payable or increases the
  saldo a favor, then the return is blocked from reception until
  corrected (FR-366).
- **AC-003:** Given a tax credit settled by payment in kind (or by a
  prior compensation), when a compensation is attempted against it,
  then the gate REJECTS the credit (only efectivo-paid credits
  qualify); given a cash-paid credit with both sides firmes, líquidos
  y exigibles, then the compensation books under the CT 76 imputation
  order (FR-373).
- **AC-004:** Given a retention-liability line whose entero deadline
  lapsed unmet 8 years ago, when any limitation sweep runs, then the
  line still carries the perpetual-exposure flag — no prescription
  clock ever applies to un-entered retentions (FR-375); the AT's claim
  is collectible en cualquier tiempo.
- **AC-005:** Given an agent that wrongly retained and entered sums on
  01-mar-2026 (pago indebido date), when the refund-claim window is
  computed, then the claim caducidad is 01-mar-2028 (2 años from the
  pago indebido, Art. 133) and the retainees' civil-action exposure
  note is preserved; given no claim by then, then the refund case
  closes as caducada while FR-375's AT-side exposure on the same sums
  remains untouched (FR-378 vs FR-375).
- **AC-006:** Given a fiscalización request, when the audit bundle
  exports, then it contains the signed EEFF + anexos, the monthly
  balanzas and year-end adjusted saldos, the comprobantes, ORIGINAL
  copies of the declarations, and the catálogo de cuentas y manual
  (structure per SV-COA-FR-022..054, by id), all sorted per período by
  date and asiento (FR-389).
- **AC-007:** Given a late declaration whose tax was $5,000 of which
  $3,500 was retained-and-entered by agents and $500 were anticipos,
  when the CT 238-b sanction base computes, then the base is the $1,000
  payable portion only (FR-380).
- **AC-008:** Given an IVA register last updated 20 days before the
  KPI sweep and a general book last updated 40 days before it, when
  the backlog monitors run, then the IVA register shows NON-COMPLIANT
  (>15 days) and the general books show COMPLIANT (≤2 months) — both
  as KPI states, never posting blockers (FR-383).
- **AC-009:** Given a consulta answer recorded in the system for
  subject A, when subject B's deadline recalculation is attempted on
  the strength of that answer, then the recalculation is refused —
  consulta effects are individual-only and filing one never tolls any
  plazo (FR-390).
- **AC-010:** Given a liquidación oficiosa that became firme on
  05-feb-2026, when the payment window resolves, then the payment is
  due by 05-apr-2026 (2 months from firme); given a multa whose
  sancionatoria resolution became firme the same day, then its window
  closes 07-mar-2026 (30 days from firme) and its non-self-assessment
  never blocks the underlying return's reception (FR-370, FR-371).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | Vintage watch (EV75 OQ-1): the 75_ print carries NO REFORMAS block and no as-of date — whether any post-2001 reform of D.E. 117-2001 itself exists is unknown from the document; corpus signals negative. The SOQ-22/30-kin verification note rides every LB citing 75_ until asamblea/D.O. routes recover. | no | Takumi W17 (sources registry) | open |
| OQ-2 | Prescription/reincidencia pin-current-CT (EV75 OQ-2): Art. 21's 10-year prescription and Art. 137's 3y/5y reincidencia windows are 2001-print values; the CT's own current prescription/caducidad terms (Arts. 82-85 and 262 zones) were never extracted. FR-374/FR-381 ship as inert dated config rows — pin the current CT text before activating them. | no | Takumi W17 + CT re-anchor pass | open |
| OQ-3 | Dictamen regime status (EV75 OQ-3): the mandatory-dictamen block (Arts. 58-72) was restructured at the CT level post-2001 (05_ carries no dictamen entry); FR-395 stays historical/awareness until the current CT text is pinned. | no | Takumi W17 (CT re-anchor pass) | open |
| OQ-4 | Art. 42 cross-ref anomaly (EV75 OQ-7, quoted in LB-037): the export-factura booking cross-ref "los artículos 81 y 82 del presente Reglamento" looks mis-pointed (the consumer-sales book is Art. 83; 81-82 = inventarios/IVA-registers intro) — print anomaly [sic]; cite-with-note, no behavior keyed to the cross-ref. | no | Takumi W17 | open |
| OQ-5 | Post-2001 repeal watch (EV75 OQ-8, SOQ-06 kin): whether any 75_ article was later repealed/amended by CT Art. 344 ff or other post-2001 instruments cannot be resolved from this print (no internal markers, no as-of date); the SOQ-06 verification note extends to every 75_-cited LB (incl. all rows in §2). | no | Takumi W17 (sources registry) | open |

Wiring note: the EV75 OQ-4/OQ-5/OQ-6 residue (máquinas-block status
post-DTE; the 04_ survivor-phrase correction; the R30(a) corrective
addendum for 02_ survivors) belongs to the corpus index/audit register,
not this file's OQ table — recorded in §2's preamble audit note for
provenance.
