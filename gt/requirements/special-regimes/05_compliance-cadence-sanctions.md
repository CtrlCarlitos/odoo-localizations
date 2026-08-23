# GT — Special regimes — Compliance cadence + sanctions, both chains (ZF + maquila): the SR5 synthesis file

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | special-regimes |
| Status  | draft |
| Authors | GT synthesis wave S-GT6/S-GT7 |
| Updated | 2026-08-22 |

## 1. Purpose

This file is the GT special-regimes wave's COMPLIANCE-CADENCE + SANCTIONS
synthesis (cluster SR5) — one calendar-and-sanction spine covering BOTH
chains: the maquila chain (D-29-89 arts. 33-43 bis + AG 533-89 arts. 23-23
quater, 30 C/30 D, 33) and the ZF chain (D-65-89 arts. 36 bis, 43-51 + AG
242-90 arts. 34-34 quater + AG 296-94 arts. 9-12). Its hallmark is the
**GOQ-99 deadline discipline**: every deadline is transcribed EXACTLY per
instrument and días (days) are NEVER normalized with días hábiles (business
days) — the maquila monthly cuenta-corriente declaración jurada (sworn
declaration) runs "dentro de los primeros veinte (20) días de cada mes"
(PLAIN days, art. 33 b) while the coeficiente de transformación
(transformation coefficient) report of the SAME article runs "durante los
primeros veinte (20) días hábiles de cada mes" (art. 33 h) — two different
prints, two different rules. On that spine the file fixes: the compliance
calendar both chains as dated deadline rows (monthly cuenta-corriente DJ,
electronic, riding the trailing 3-month IGSS planilla electrónica via
SEADEX/Ventanilla Única — planilla lifecycle consumed by exact id from
payroll/07; monthly coeficiente to SAT / to the SAT Departamento de Control
de Entes Exentos; the annual labor-compliance DJ ante Notario + Boleta
Estadística within the first 40 días of each year per R80 — file 04's dated
pair consumed by id; the annual full nómina to MinTrabajo/IGT (+ MINECO per
the ZF reglamento) within the first 2 months; the ZF quarterly Boleta
Estadística ≤15 días post-quarter); the sanctions model (100% multa on
diverted goods + solidary liability enajenante + adquiriente in BOTH chains;
descargo 45 días post-export-declaration + US$100.00/late-declaration multa
at the FX of the day; refunds ≤30 días; the guarantees menu; the 5-year
machinery transfer lock from póliza acceptance); the art. 43 bis IGSS-driven
suspension ladder as a STATE MACHINE (2/4/6 meses tiers keyed to payroll/07
compliance states; calendar-year doubling at the highest tier; definitive
suspension on doubled-within-2-years or 3× any inciso; the art. 23 quater
apercibimiento prerequisite + SAT registry disable/enable + MINECO's
sanction registry); ZF revocation causales + one-time apercibimiento + the
15-day hearing; the fondo late-payment ladder (50% multa + daily
resarcitorios at the highest active bank rate — rate external, GOQ-10 kin —
+ 10-días-hábiles cure + juicio económico-coactivo + the 6-month
verification cycle); the art. 50 Bis defraudación aduanera special case
(D-6-2021); the regime-law vs CT sanction-track disambiguation; and the
platform-name negative anchor (GOQ-140 — SEADEX/Ventanilla Única/el Sistema
cited as printed, never as current module names).

It does **not** cover: the benefit windows and window-row model the
sanctions act on — `01_zf-exemption-schedules.md` (GT-SPR-FR-001..033,
consumed by exact id) and `03_maquila-benefit-shape.md`
(GT-SPR-FR-061..094, consumed by exact id); the ZF chain instruments and
authority-resolution rows — `02_zf-chain-regime.md` (GT-SPR-FR-034..060);
the maquila reglamento chain, the R80 dated pair itself, el Sistema's
record architecture and the customs-operation rows —
`04_maquila-reglamento-chain.md` (GT-SPR-FR-095..133, consumed by exact id);
the ZF↔maquila cross-regime bridges (revocation-driven exclusions, D-65-89
flows, the textiles→ZF valve) — `06_cross-regime-bridges.md` (SR6 —
path-only); and surfaces owned by other waves, consumed here by
exact id or pointer only: GT-PAY-FR-170..177
(`gt/requirements/payroll/07_igss-contributions.md` — the planilla
electrónica lifecycle, registro patronal filing unit, late
acceptance-with-mora, solvencia dynamics and due dates this file's calendar
and ladder ride; GT-PAY-FR-018 of payroll/01 as ≥3-worker planilla-mode
kin), GT-TAX-FR-214/216/217 (taxation/06 CT sanction track — disambiguation
row only) with GT-TAX-FR-232 prescription kin, and the fiscal-reporting
constancia surfaces GT-FIN-FR-052/054/055/065/066/068/069
(`gt/requirements/fiscal-reporting/02_retenciones-web.md` — pointer-only).

## 2. Legal Basis

Authority order (binding, per master index preamble): maquila law = **69_**
(*Decreto 29-89*, consolidated through D-19-2016); maquila reglamento =
**70_** (AG 533-89) read through **71_** (AG 253-2001) corrections. ZF law
= **67_** (D-65-89, consolidated through D-6-2021 — effective publication
day 1-Jun-2021, never +90 days, R73); ZF reglamento = **68_** (AG 242-90)
EXCEPT arts. 3/6/8/13 + tarifario → **81_** (AG 65-2022; e-provisions
14-Sep-2022 — R72); fondo reglamento = **72_** (AG 296-94). **GOQ-08 resolved — D-19-2016 =
`84_` corpus primary**: the art. 43 bis suspension ladder (`84_` art. 17),
the art. 34 trailing-planilla ¶ (`84_` art. 13), the art. 33 obligations
restatement (`84_` art. 12 — e-filing now mandatory "debe enviarse") and
the ZF art. 36 bis stack (`84_` art. 26) are primary-verified against the
consolidated prints (EVID-751/752/756); D-19-2016's transitorios ARE now
readable (arts. 28-30 ZF-side + the untitled maquila art. 18 —
EVID-753/757) and print NO transitional mechanic on the ladder or the
attach (the art. 29 transitorio only stands up IGSS complaint offices
feeding MINECO's 43 bis suspensions); the reglamento-side art. 23 quater
text is now primary from AG 3-2017 (`95_` art. 17 — EVID-777). Quotation
source: the committed evidence files
`gt/.extractions/69-71_Maquila.evidence.md` (EVID-711..745),
`gt/.extractions/67-68_72_80_81_ZF.evidence.md` (EVID-646..708) and
`gt/.extractions/84_91_94_95_MaquilaZF_D19-2016_chain.evidence.md`
(EVID-746..789) — all
FROZEN; quotes verified against them and spot-checked against the `67_`/
`68_`/`69_`/`70_` txt layers; numbers, percentages, durations, dates and
article numbers exactly as printed; OCR damage kept with [sic].

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D-29-89 art. 33 (obligations): b) "Proporcionar dentro de los primeros veinte (20) días de cada mes, la declaración jurada a la Superintendencia de Administración Tributaria…, en la que se hará constar la cuenta corriente correspondiente de mercancías bajo el régimen de esta Ley… Dicha declaración jurada deberá enviarse electrónicamente." / c) "Proporcionar la planilla electrónica de pagos de cuotas laboral y patronal al instituto Guatemalteco de Seguridad Social." / d) "Llevar registros contables y un sistema de inventario perpetuo, de las mercancías ingresadas temporalmente y la cantidad de las mismas utilizadas en las mercancías producidas." / h) "Las empresas que se dediquen a la producción y transformación de materias primas en producto terminado, deberán presentar a la Administración Tributaria, en los medios que esta determine, durante los primeros veinte (20) días hábiles de cada mes, informe sobre el coeficiente de transformación determinado para sus procesos productivos." / closing: "Las personas individuales o jurídicas, propietarios de entidades o empresas, socios o accionistas de éstas, trasladarán la totalidad de la nómina de los trabajadores anualmente al Ministerio de Trabajo y Previsión Social e Inspección General de Trabajo." (tags: ref. D-38-04 art. 18; D-19-2016 art. 12) | The maquila compliance backbone: monthly sworn declaration to SAT WITHIN THE FIRST TWENTY (20) DAYS OF EACH MONTH (plain days — NOT hábiles) stating the merchandise cuenta corriente, SENT ELECTRONICALLY; provision of the IGSS electronic planilla of employee/employer cuotas; accounting records + perpetual-inventory system for temporarily entered merchandise and its consumption; monthly transformation-coefficient report DURING THE FIRST TWENTY (20) DÍAS HÁBILES of each month; annual transfer of the FULL worker nómina to MinTrabajo and the Labor Inspectorate (IGT) | `gt/sources/69_Maquila_Ley_D29-89.pdf` | pp.12-13, art. 33 incisos b), c), d), h) + closing (EVID-725) |
| LB-002 | D-29-89 arts. 34-35: art. 34: reposición-franquicia companies "únicamente deberán cumplir con las obligaciones establecidas en los incisos d), e) y f) del artículo anterior. Todas las empresas que se beneficien con esta Ley, además de cumplir con la Ley Nacional de Aduanas, el Código Aduanero Uniforme Centroamericano y su reglamento, deberán presentar adjunto a la Declaración Jurada, de acuerdo al artículo 33, literal b) de esta Ley, la planilla electrónica de seguridad social del Instituto Guatemalteco de Seguridad Social, correspondiente a los últimos tres (3) meses previos al mes que corresponda la información de la Declaración Jurada…, las que podrán entregarse o enviarse electrónicamente a la Única para las Exportaciones del Ministerio de Economía, a través del Sistema Electrónico de Exportaciones." (tag: párrafo adicionado por D-19-2016 art. 13) / art. 35: CANT companies fulfill "los incisos a), e) y f)… Además deberán presentar fotocopia simple de la póliza de importación de maquinaria, equipo, partes, componentes y accesorios dentro del plazo de cuarenta y cinco (45) días posteriores a la fecha de la liquidación de la póliza respectiva." | Regime-dependent obligation matrix: reposición-franquicia companies owe ONLY art. 33 d), e), f) — but EVERY enterprise benefiting from the law must attach to the monthly DJ the IGSS electronic social-security planilla of the TRAILING THREE (3) MONTHS prior to the DJ's information month, deliverable electronically to the exports single window of MinEconomía through the electronic exports system (the SEADEX/Ventanilla Única join — names as printed); CANT companies owe a), e), f) plus a simple photocopy of the machinery import póliza within FORTY-FIVE (45) DAYS after the póliza's liquidation date | `gt/sources/69_Maquila_Ley_D29-89.pdf` | p.13, arts. 34 y 35 (EVID-726) |
| LB-003 | AG 533-89 arts. 30 "C" y 30 "D": 30 C: coeficiente informe "dentro de los primeros veinte (20) días hábiles de cada mes con la información correspondiente a las operaciones realizadas por las empresas en el mes inmediato anterior", via the Oficina de Regímenes de Perfeccionamiento Activo virtual platform (added AG 3-2017) / 30 "D": "…deberán presentar, al Ministerio de Trabajo, a través de la Inspección General de Trabajo, dentro del plazo de los dos (2) primeros meses de cada año y por los medios que éste ponga a su disposición, la totalidad de la nómina de los trabajadores de su empresa, correspondiente al año calendario anterior." (added AG 3-2017) | Reglamento cadence rows: the coefficient report within the FIRST TWENTY (20) DÍAS HÁBILES of each month covering the IMMEDIATELY PRECEDING MONTH's operations, filed through the virtual platform of the Oficina de Regímenes de Perfeccionamiento Activo (Office of Active-Perfectionment Regimes — name as printed); the annual FULL nómina within the FIRST TWO (2) MONTHS of each year to MinTrabajo through the IGT, by the means it provides, covering the prior calendar year | `gt/sources/70_Maquila_Reglamento_AG_533-89.pdf` | pp.15-16, arts. 30 "C" y 30 "D" (EVID-738) |
| LB-004 | AG 533-89 arts. 23 Ter y 23 quater: 23 Ter: "…deberán presentar una Declaración Jurada ante Notario…, en la que hagan constar que durante el año calendario anterior, ha cumplido con las obligaciones establecidas en las leyes laborales del país. Así mismo deben presentar la Boleta Estadística… Dichos documentos deberán ser presentados dentro de los primeros cuarenta (40) días de cada año, por los medios que éste disponga. El incumplimiento… dará lugar a la cancelación de los beneficios… conforme lo establece el Artículo 43 de la Ley." (tags: added by AG 253-2013 art. 4; reformed AG 3-2017 art. 16) / 23 quater (added AG 3-2017 art. 17 — text now primary from `95_`, EVID-777): "El Ministerio de Economía previo a aplicar las suspensiones establecidas en el artículo 43 bis de la ley, deberá cumplir con el apercibimiento establecido en el artículo 23 del reglamento. Si dentro de dicho plazo el titular de la empresa infractora no cumpliere con sus obligaciones, el Departamento de Política Industrial… emitirá dictamen para que el Ministerio de Economía suspenda los derechos establecidos en la ley y sus reformas, por los plazos indicados en dicho artículo. Una vez, la resolución se encuentre firme, el Ministerio de Economía informará al Departamento de Control de Entes Exentos de la Intendencia de Recaudación y Gestión, y a la Intendencia de Aduanas de la Superintendencia de Administración Tributaria, que haga efectiva la suspensión… a partir del día inmediato siguiente de la recepción de la resolución donde se indicará el plazo de la sanción, para que ésta lo inhabilite y finalizado el plazo respectivo se habilite en sus registros informáticos. El Ministerio de Economía debe llevar un registro de las sanciones aplicadas a efecto de cumplir lo establecido en el penúltimo párrafo del artículo 43 bis de la Ley." | The annual notarized labor-compliance DJ + statistics slip within the FIRST FORTY (40) DAYS of each year (breach → benefit cancellation per law art. 43 — the R80 current text; the AG 253-2001 original "20 días del mes de enero" is history only, file 04 FR-116's dated pair); the suspension prerequisite ladder: BEFORE applying any art. 43 bis suspension MINECO must run the art. 23 apercibimiento; once the resolution is firme MINECO informs SAT's Entes-Exentos department and the Customs Intendencia, which disable the beneficiary FROM THE DAY IMMEDIATELY AFTER receiving the resolution and RE-ENABLE it when the term ends; MINECO keeps a registry of applied sanctions to feed the art. 43 bis penultimate-paragraph (recidivism) computation | `gt/sources/70_Maquila_Reglamento_AG_533-89.pdf` | pp.10-12, arts. 23 Ter y 23 quater (EVID-736; 23 quater now primary at `95_` art. 17 — EVID-777) |
| LB-005 | D-65-89 art. 36 bis (added by art. 26, D-19-2016): "Las empresas calificadas al amparo de esta Ley, deberán cumplir con lo siguiente: a) Proporcionar a la Superintendencia de Administración Tributaria de toda la información necesaria para la determinación y seguimiento de sus rentas exentas y del monto de las operaciones realizadas. b) Proporcionar la planilla electrónica de pagos de cuotas laboral y patronal al Instituto Guatemalteco de Seguridad Social. c) Llevar registros contables y un sistema de inventario perpetuo, de las mercancías ingresadas temporalmente y la cantidad de las mismas utilizadas en las mercancías producidas. d) Proporcionar al Departamento de Política Industrial y a la Superintendencia de Administración Tributaria la información que sea necesaria para determinar las mercancías que se requieran para la producción o ensamble de los productos exportables, así como para determinar las mermas, subproductos y desechos resultantes del proceso de producción. e) Proporcionar cualquier otra información pertinente… así como permitir las inspecciones… f) Cumplir con las leyes del país, particularmente las de carácter laboral. g) Las empresas que se dediquen a la producción y transformación de materias primas en producto terminado, deberán presentar a la Administración Tributaria, en los medios que esta determine, durante los primeros veinte (20) días hábiles de cada mes, informe sobre el coeficiente de transformación determinado para sus procesos productivos. h) Utilizar las herramientas informáticas o los medios que autorice la Superintendencia de Administración Tributaria y el Instituto Guatemalteco de Seguridad Social… / Las personas individuales o jurídicas, propietarios de entidades o empresas, socios o accionistas de éstas, trasladarán la totalidad de la nómina de los trabajadores anualmente al Ministerio de Trabajo y Previsión Social e Inspección General de Trabajo." | The ZF compliance backbone (post-2016, every qualified company): SAT information for the determination and tracking of exempt rents and operation amounts; IGSS electronic planilla of employee/employer cuotas; accounting records + perpetual-inventory system for temporarily entered merchandise; mermas/subproductos/desechos information to DPI + SAT; inspection tolerance; labor-law compliance; monthly transformation-coefficient report DURING THE FIRST TWENTY (20) DÍAS HÁBILES of each month; SAT/IGSS-authorized IT tools; closing: annual transfer of the full worker nómina to MinTrabajo/IGT | `gt/sources/67_ZF_Ley_D65-89.pdf` | pp.11-12, art. 36 bis incisos a)-h) + closing (EVID-671) |
| LB-006 | AG 242-90 arts. 34, 34 bis, 34 ter: art. 34: "En el caso de cualquier incumplimiento a las obligaciones contenidas en la ley, la autoridad administrativa que conozca del mismo, deberá oír al interesado, previo emitir la resolución correspondiente, otorgándole para el efecto un plazo de 15 días." / 34 bis: "…deberán presentar a la Superintendencia de Administración Tributaria, un informe sobre el coeficiente de transformación determinado conforme a sus procesos productivos. Para el efecto, el coeficiente de transformación deberá calcularse atendiendo al consumo de cada unidad de medida de materia prima utilizada en la producción de los bienes… deberá contener la descripción del bien producido, componente utilizado para la producción del bien y la unidad de medida y proporción utilizado en este… deberá presentarse por los medios que determine la Superintendencia de Administración Tributaria, al Departamento de Control de Entes Exentos…, dentro de los primeros veinte (20) días hábiles de cada mes con la información correspondiente a las operaciones realizadas por las empresas en el mes inmediato anterior." / 34 ter: "…deberán presentar al Ministerio de Trabajo, a través de la Inspección General de Trabajo, y al Ministerio de Economía dentro del plazo de los dos (2) primeros meses de cada año y por los medios que éste ponga a su disposición, la totalidad de la nómina de los trabajadores de su empresa, correspondiente al año calendario anterior." | ZF due-process + cadence: before ANY sanction resolution for law breaches the authority must hear the interested party with a FIFTEEN (15) DAY window (plain días as printed); the coefficient report to SAT — computed per unit of measure of raw material consumed, stating the produced good, component, unit and proportion — filed WITHIN THE FIRST TWENTY (20) DÍAS HÁBILES of each month for the previous month's operations, to the Departamento de Control de Entes Exentos (Exempt-Entities Control Department); the annual full nómina WITHIN THE FIRST TWO (2) MONTHS of each year to MinTrabajo/IGT AND MINECO (the reglamento's addition to the law's addressees) | `gt/sources/68_ZF_Reglamento_AG_242-90.pdf` | p.14, arts. 34, 34 bis, 34 ter (EVID-691) |
| LB-007 | AG 242-90 art. 34 quater (adicionado AG 52-2017; reformado AG 65-2022): "Las personas individuales o jurídicas, beneficiarias de la Ley, conforme a los artículos 36 literal f) y 36 Bis literal e) de la Ley, deberán presentar de forma trimestral la Boleta Estadística en el formato elaborado por el Departamento de Política Industrial, dentro los quince (15) días de finalizado el trimestre, por los medios que éste ponga a su disposición." — administradora fields a)-v) incl. "e) Cantidad de metros cuadrados autorizados; f) Cantidad de usuarios por tipo de usuario calificado; … l) Monto total de salarios pagados; m) Monto total de inversión realizada; n) Valor de las importaciones totales; o) Valor de las exportaciones totales; p) Valor de ventas al territorio aduanero nacional; q) Valor total de Derechos Arancelarios de Importación -DAI- pagados; r) Valor total de Impuesto al Valor Agregado -IVA- pagado; s) Valor total de Impuesto Sobre la Renta -ISR- pagado; t) Consumo de energía eléctrica del último mes del trimestre reportado en kWh…" — user fields a)-w) incl. "h) Número patronal ante el Instituto Guatemalteco de Seguridad Social -IGSS-; i) Empleados totales generados por usuario; j) Salarios totales pagados por usuario; k)-m) inversión en inventarios/maquinaria/infraestructura; n) Origen del capital invertido; o)-t) importaciones/exportaciones/ventas-TAN/DAI/IVA/ISR…" — closing: "El incumplimiento de esta obligación dará lugar a la cancelación de los beneficios por el Ministerio de Economía conforme lo establecen los artículos 48 y 49 de la Ley." | The ZF quarterly statistics slip [deadline as printed: "dentro los quince (15) días" — sic, no "de"]: administrators file the a)-v) layout (authorized m², users by type, TOTAL SALARIES PAID, investment, imports/exports/TAN sales, DAI/IVA/ISR paid, energy kWh) and users the a)-w) layout (IGSS employer number, total employees, total salaries, investment classes, capital origin, trade values) WITHIN FIFTEEN (15) DAYS of quarter end; NON-FILING = CANCELLATION OF BENEFITS by MINECO per law arts. 48/49. Field lists quoted from 68_ (which prints the article WITH its tags — GOQ-137 kin; 81_ OCR drops the importaciones/exportaciones rows, unresolved) | `gt/sources/68_ZF_Reglamento_AG_242-90.pdf` | pp.14-16, art. 34 quater (EVID-692) |
| LB-008 | D-29-89 arts. 41-43: art. 41: "La enajenación a cualquier título de mercancías importadas o admitidas al amparo de esta Ley, o la utilización de las mismas para fines distintos de aquellos para los cuales fue concedido el beneficio, se sancionará con multa igual al ciento por ciento (100%) de los impuestos aplicables no pagados… En caso de incumplimiento, el enajenante y el adquiriente serán responsables solidarios del pago de los montos dejados de percibir por el Estado." / art. 42: destruction of suspended goods "que no se encuentren dentro de la zona primaria de la jurisdicción aduanera… quedarán sujetas al pago de los derechos y demás impuestos…, salvo caso fortuito o de fuerza mayor, debidamente comprobado por el Ministerio de Finanzas Públicas." / art. 43: "El Ministerio de Economía revocará de oficio la resolución de calificación…: a) Cuando la empresa no inicie la producción dentro del plazo establecido… b) Por cierre, disolución o quiebra de la empresa. c) Por el incumplimiento que resulte de las obligaciones contenidas en la resolución de calificación respectiva. No obstante…, la Dirección de Política Industrial podrá apercibir por una sola vez a la empresa infractora…" | Maquila sanctions: disposal at any title, or use-diversion, of goods imported/admitted under the law = fine of ONE HUNDRED PERCENT (100%) of the unpaid applicable taxes, with transferor (enajenante) and acquirer (adquiriente) SOLIDARILY liable for the State's uncollected amounts; destruction outside the customs primary zone makes duties fall due unless force majeure evidenced to MinFinanzas; revocation of the calificación de oficio by MINECO for no-production-start, closure/dissolution/bankruptcy, or resolution breach — with a ONE-TIME formal warning (apercibimiento) valve at DPI | `gt/sources/69_Maquila_Ley_D29-89.pdf` | p.16, arts. 41, 42, 43 (EVID-729) |
| LB-009 | D-29-89 art. 43 bis (added by art. 17, D-19-2016, 31-03-2016): "El Ministerio de Economía suspenderá los derechos establecidos en la presente Ley, y sus reformas, a las entidades y empresas que incumplan la Ley Orgánica del Instituto Guatemalteco de Seguridad Social y los reglamentos, así: a) Por dos meses, cuando: i. No inscriba a algún trabajador, como establecen los reglamentos del IGSS; ii. incumplan la legislación del IGSS; iii. Se determine que niegan certificado a los trabajadores, para asistir a clínicas, hospitales y demás servicios del IGSS. b) Por cuatro meses, cuando, teniendo cincuenta o más trabajadores, no procedan a su inscripción… c) Por seis meses, cuando no enteren las cuotas laborales, patronales o las multas correspondientes al IGSS… La suspensión se duplicará cuando, durante el período de un año, calculado del uno de enero al treinta y uno de diciembre, se reincida en por lo menos dos de los incisos anteriores. Para el cálculo de la duplicación de la suspensión se aplicará la suspensión más alta. Asimismo, se suspenderá definitivamente los derechos de esta Ley a las entidades y empresas que en un período de dos años se les haya duplicado la suspensión o en por lo menos tres veces en cualquiera de los incisos del presente artículo. La aplicación de las suspensiones temporales… no exime a la entidad o empresa para cumplir con las obligaciones… con el IGSS." | THE IGSS-driven suspension ladder (all D-19-2016): TWO MONTHS for failing to inscribe a worker, breaching IGSS legislation, or denying workers the certificate to attend IGSS clinics/hospitals/services; FOUR MONTHS when, having FIFTY OR MORE workers, the enterprise does not proceed to their inscription; SIX MONTHS for non-remittance of employee/employer cuotas or IGSS fines; the suspension DOUBLES when, within a calendar year (1 January to 31 December), the enterprise reoffends in at least TWO of the incisos — the HIGHEST tier applies for the doubling computation; DEFINITIVE suspension when the suspension was doubled within a two-year period, or the enterprise incurred at least THREE TIMES in any inciso; temporary suspension does NOT exempt IGSS obligations | `gt/sources/69_Maquila_Ley_D29-89.pdf` | pp.16-17, art. 43 bis (EVID-730) |
| LB-010 | D-29-89 arts. 27, 29, 30: art. 27 ("Constitución de garantía.*", tag: D-19-2016 art. 11): "La totalidad de los derechos arancelarios, impuestos a la importación e Impuesto al Valor Agregado, de las mercancías que ingresen al territorio aduanero nacional, se garantizarán ante el fisco mediante la constitución de una garantía por cualquiera de los medios siguientes: a) Depósito en efectivo; b) Almacenes Generales de Depósito autorizados para operar como almacenes fiscales que constituyan garantía específica para este tipo de operaciones; c) Seguro de caución; d) Garantía hipotecaria; e) Garantía combinada, entre cualquiera de las anteriores." / art. 29: "…el interesado deberá solicitarlo ante la SAT…, dentro del plazo de los cuarenta y cinco (45) días posteriores a la fecha de presentación de la Declaración de Exportación, la reexportación o del Formulario Aduanero Único Centroamericano -FAUCA-… En caso que la solicitud respectiva no se presente dentro del plazo antes señalado, el contribuyente deberá pagar a la SAT una multa equivalente en quetzales a US$100.00 al tipo de cambio del día por cada declaración de exportación, reexportación o FAUCA presentada en forma extemporánea. Una vez pagada la multa, podrá proceder con lo solicitado." (tag: D-38-04 art. 17) / art. 30: "…se reembolsarán a través de cheque librado, que extenderá la Dirección General de Aduanas o Aduanas de la República, dentro del plazo de treinta (30) días siguientes a la presentación de la solicitud…" | The guarantee law-menu (as reformed by D-19-2016): ALL duties/import taxes/IVA on entered merchandise are guaranteed to the treasury by ANY of — cash deposit; authorized general deposit warehouses operating as fiscal warehouses constituting a specific guarantee; surety insurance (seguro de caución); mortgage guarantee; combined guarantee. Guarantee release (descargo): request to SAT within FORTY-FIVE (45) DAYS after presentation of the export declaration, re-export or FAUCA; late = fine EQUAL TO US$100.00 IN QUETZALS AT THE DAY'S EXCHANGE RATE per late declaration, and only after payment may the request proceed. Cash-deposit refunds: by DGA cheque within THIRTY (30) DAYS of the solicitud | `gt/sources/69_Maquila_Ley_D29-89.pdf` | p.11 art. 27; p.12 arts. 29-30 (EVID-723) |
| LB-011 | D-29-89 arts. 39 y 40: art. 39: "Se prohíbe a las empresas…, enajenar en cualquier forma en el territorio nacional, las mercancías internadas temporalmente, salvo que se paguen los derechos arancelarios e impuestos correspondientes. Se exceptúan las donaciones que se hagan a entidades de beneficencia, las que deberán contar con la autorización previa del Ministerio de Finanzas Públicas." / art. 40: "La maquinaria, equipo, partes, componentes y accesorios que se importen al amparo de esta Ley, no podrán ser enajenados ni destinados a un fin distinto de aquel para el cual hubieren sido autorizados, salvo que se cubran los derechos arancelarios, impuestos a la importación e Impuesto al Valor Agregado -IVA-, que ocasionaron, y en los casos de la maquinaria, equipo, partes, componentes y accesorios, importados después de cinco (5) años, contados a partir de la fecha de aceptación de la póliza de importación, previa notificación a la Dirección de Política Industrial…" (tag: ref. D-38-04 art. 21) | Prohibition on disposing of temporarily entered merchandise in the national territory unless the corresponding duties/taxes are paid (charity donations excepted with prior MinFinanzas authorization); machinery/equipment/parts/components/accessories imported under the law may NOT be alienated nor put to a different purpose unless the DAI/import taxes/IVA they caused are paid AND — for alienation — five (5) YEARS have elapsed from ACCEPTANCE OF THE IMPORT PÓLIZA, with prior notification to DPI: the 5-year machinery transfer lock | `gt/sources/69_Maquila_Ley_D29-89.pdf` | p.15, arts. 39 y 40 (EVID-728) |
| LB-012 | D-65-89 arts. 46 y 47: art. 46: "La enajenación a cualquier título dentro del Territorio Aduanero Nacional de la maquinaria, equipo, partes, componentes, accesorios y mercancías admitidas al amparo del esta ley, o la utilización de las mismas para fines distintos de aquellos para los cuales fue concedido el beneficio, se sancionará con multa igual al cien por ciento (100%) de los impuestos aplicables no pagados, sin perjuicio de cualesquiera otras sanciones que indiquen las leyes aduaneras vigentes. En caso de incumplimiento el enajenante y el adquiriente serán responsables solidarios del pago de los montos dejados de percibir por el Estado." / art. 47: "Cuando las mercancías ingresen o egresen de Zonas Francas sin llenar las formalidades legales correspondientes, se sancionará al infractor con multa igual al cien por ciento (100%) de los impuestos aplicables no pagados, sin perjuicio de cualesquiera otras sanciones que indiquen las leyes aduaneras vigentes y las leyes específicas en materia civil y penal que le sean aplicables." | ZF sanctions: disposal at any title inside the national customs territory of machinery/merchandise admitted under the law, or use-diversion = fine of ONE HUNDRED PERCENT (100%) of the unpaid applicable taxes, cumulative with customs-law sanctions, transferor + acquirer SOLIDARILY liable; entry/exit of merchandise into/from zonas francas WITHOUT the corresponding legal formalities = the same 100% fine, cumulative with customs, civil and penal law | `gt/sources/67_ZF_Ley_D65-89.pdf` | p.15, arts. 46 y 47 (EVID-675) |
| LB-013 | D-65-89 arts. 48-50: art. 48 (administradoras): "El Ministerio de Economía revocará de oficio la resolución de calificación de la Entidad Administradora de Zona Franca enviando copia de la revocatoria a la Dirección General de Aduanas y Dirección General de Rentas Internas en los casos siguientes: a) Por incumplimiento de los objetivos, las obligaciones y requisitos contenidos en la resolución de autorización. b) Cuando por causa imputable a ella no se diera inicio a las operaciones en el término señalado en la resolución de calificación, o dentro del plazo establecido en la prórroga respectiva. c) Por tráfico ilícito de mercancías. d) Cuando ingresen a la Zona Franca mercancías que pongan en peligro el medio ambiente o la salud de la población. En cuanto a lo establecido en los incisos b) y d) anteriores, la Dirección de Política Industrial podrá apercibir por una sola vez a la entidad administradora…" / art. 49 (usuarios): same mechanism, causales a) incumplimiento, b) tráfico ilícito, c) peligro ambiental/salud; apercibimiento once for c) / art. 50: "En los casos descritos en el artículo 48, inciso c), y 49 inciso b), la autoridad competente incautará las mercancías, las que podrá a disposición de los tribunales [sic — pondrá a disposición] para deducir las responsabilidades correspondientes, la sanción no exime al infractor de las responsabilidades civiles y penales…" | ZF revocation: MINECO revokes de oficio (copies to Aduanas + Rentas Internas) — administrators for resolution breach, imputable failure to start operations, illicit traffic, dangerous goods; users for resolution breach, illicit traffic, dangerous goods; a ONE-TIME apercibimiento is available for the non-criminal causales (48 b)/d); 49 c)); illicit traffic additionally triggers SEIZURE with the goods placed at the disposal of the courts, civil and penal liability preserved | `gt/sources/67_ZF_Ley_D65-89.pdf` | pp.15-16, arts. 48, 49, 50 (EVID-676) |
| LB-014 | D-65-89 art. 50 Bis (adicionado por art. 4, D-6-2021, 01-06-2021): "Se considera caso especial de defraudación aduanera, obtener la calificación a que se refiere la presente Ley mediante simulación, ocultación, maniobra, ardido cualquier otra [sic — "ardid o cualquier otra"] forma de engaño al Ministerio de Economía o a la Superintendencia de Administración Tributaria." | Obtaining the ZF calificación by simulation, concealment, manoeuvre, trick [sic as printed] or any other form of deception of MINECO or SAT is a SPECIAL CASE OF CUSTOMS FRAUD (defraudación aduanera) — a criminal/customs-fraud recharacterization beyond mere revocation | `gt/sources/67_ZF_Ley_D65-89.pdf` | p.16, art. 50 Bis (EVID-677) |
| LB-015 | D-65-89 art. 51: "Cuando no se efectúe o se efectúe extemporáneamente el pago a que se refiere el inciso e) del artículo 36 de esta Ley, dará lugar a que a la Entidad Administradora correspondiente, se le imponga una multa por el equivalente al cincuenta por ciento (50%) del mismo, sin perjuicio de que sin necesidad de requerimiento alguno se le carguen intereses resarcitorios por cada día de mora, calculados aplicando la tasa de interés activa más alta del mercado bancario. / En los casos mencionados en el párrafo anterior, la Dirección General de Rentas Internas del Ministerio de Finanzas Públicas, determinará de oficio lo caído en mora. La Entidad Administradora será emplazada en audiencia para que dentro de los diez (10) días hábiles siguientes al de la notificación de la providencia respectiva, presente la liquidación omitida y haga efectivo el pago. / Vencido dicho término sin que se haya hecho efectivo el pago, la Dirección General de Rentas Internas resolverá declarando firme la determinación e iniciará juicio económico-coactivo." | Fondo (US$0.10/m² monthly levy) late payment: fine of FIFTY PERCENT (50%) of the omitted amount + DAILY restitutionary interest for each day of default at the HIGHEST ACTIVE RATE OF THE BANKING MARKET (an external market reference), charged WITHOUT prior demand; the Dirección General de Rentas Internas (DGRI) determines the default de oficio; the administrator is summoned to a hearing and has TEN (10) DÍAS HÁBILES from notification of the order to present the omitted liquidation and pay; on expiry without payment the determination becomes firme and DGRI initiates the juicio económico-coactivo (economic-coercive collection suit) | `gt/sources/67_ZF_Ley_D65-89.pdf` | pp.16-17, art. 51 (EVID-678) |
| LB-016 | AG 296-94 arts. 9-12: art. 9: "La Dirección de Política Industrial verificara cada seis (6) meses las declaraciones de las Entidades Administradoras respecto al área total ocupada, vendida o arrendada… En el caso que las Entidades Administradoras hayan declarado un área menor a la realmente ocupada…, la Dirección de Política Industrial informará a la Dirección General de Rentas Internas para que dicha dependencia realice el ajuste del pago omitido y proceda conforme lo señalado en el artículo 51 del Decreto numero 65-89…" / art. 10: non/late payment → DPI "lo pondrá en conocimiento de la Dirección General de Rentas Internas, para que dicha dependencia proceda de conformidad con lo establecido en el último párrafo del artículo anterior" / art. 11 (transitorio): pending payments at the reglamento's vigencia "estarán exonerados de las multas y recargos… siempre que se efectúen dentro de los treinta (30) días siguientes" / art. 12: vigencia DCA+1 | Fondo audit wiring: DPI verifies the administrators' area declarations EVERY SIX (6) MONTHS; under-declared area is reported to DGRI which adjusts the omitted payment and applies law art. 51 (50% multa + resarcitorios + económico-coactivo); non/late payment is likewise reported to DGRI; a one-time 30-day amnesty applied to pre-1994-vigencia arrears (historical) | `gt/sources/72_ZF_Fondo_AG_296-94.pdf` | p.3, arts. 9, 10, 11, 12 (EVID-704) |
| LB-017 | D-65-89 arts. 43 y 44: art. 43: "Se prohíbe a las entidades administradoras y a los usuarios, enajenar en cualquier forma en el territorio nacional, las mercancías que hayan ingresado a Zona Franca, exoneradas o no, afectas al pago de derechos arancelarios, Impuestos a la Importación e Impuesto al Valor Agregado (IVA)." / art. 44: "La maquinaria, equipo, partes, componentes y accesorios que ingresen al amparo de esta Ley, para ser utilizados por la entidad administradora o los Usuarios de Zona Franca, no podrán ser enajenados ni destinados a un fin distinto a aquel para el cual hubiere sido autorizados en la Resolución del Ministerio de Economía." | ZF prohibitions: administrators and users may not dispose in the national territory of merchandise that entered the zona franca (exonerated or not) and is subject to DAI/import taxes/IVA; machinery/equipment/parts/components/accessories entering under the law are locked to the purpose authorized in the MINECO resolution — NOTE: the ZF print carries NO time term (no 5-year clock) | `gt/sources/67_ZF_Ley_D65-89.pdf` | pp.14-15, arts. 43 y 44 (EVID-674) |
| LB-018 | AG 533-89 art. 33 (tags: AG 12-97; AG 3-2017): "La declaración jurada mensual de la cuenta corriente de mercancías… se presentará en el formulario que para el efecto elabore el Sistema… Junto con la declaración jurada, deberá presentarse la planilla electrónica de seguridad social del Instituto Guatemalteco de Seguridad Social correspondiente a los últimos tres (3) meses previos al mes que corresponda la información de la declaración jurada, las cuales podrán entregarse o enviarse electrónicamente a la Ventanilla Única para las Exportaciones del Ministerio de Economía, a través del Servicio Electrónico de Autorización de Exportaciones (SEADEX)." | The monthly cuenta-corriente DJ uses the form el Sistema elaborates and RIDES WITH the IGSS electronic social-security planilla of the trailing THREE (3) MONTHS, deliverable electronically to the Ventanilla Única para las Exportaciones (Single Window for Exports) of MinEconomía through the Servicio Electrónico de Autorización de Exportaciones (SEADEX — Electronic Export-Authorization Service): the filing-join row (names as printed — GOQ-140) | `gt/sources/70_Maquila_Reglamento_AG_533-89.pdf` | pp.16-18, art. 33 (EVID-739) |

## 3. Functional Requirements

### 3.1 The compliance-calendar engine and the GOQ-99 deadline discipline

- **GT-SPR-FR-134:** ANCHOR (load-bearing, GOQ-99 — this file's hallmark):
  the system shall implement the special-regimes compliance calendar for
  BOTH chains as dated deadline rows (D16: valid_from/valid_to + instrument
  provenance, never global constants), each row storing the qualifier
  EXACTLY as printed — plain días vs días hábiles are DIFFERENT rules and
  are never normalized, converted or coalesced: maquila cuenta-corriente DJ
  = "primeros veinte (20) días de cada mes" PLAIN (art. 33 b); maquila +
  ZF coeficiente = "primeros veinte (20) días hábiles de cada mes" (arts.
  33 h / 36 bis g); ZF hearing = "plazo de 15 días" PLAIN (reglamento
  art. 34); fondo cure = "diez (10) días hábiles" (art. 51); annual
  labor DJ = "primeros cuarenta (40) días de cada año" PLAIN (23 Ter).
  Rejected myth (wave set): normalizing día ↔ día-hábil.
  (LB-001; LB-003; LB-004; LB-006; LB-015; EVID-725/736/738/691/678;
  GOQ-99 → OQ-002)
- **GT-SPR-FR-135:** The system shall implement the maquila monthly
  cuenta-corriente declaración jurada as a compliance-calendar entry per
  beneficiary: provided to SAT DENTRO DE LOS PRIMEROS VEINTE (20) DÍAS DE
  CADA MES (plain días, transcribed exactly), stating the cuenta corriente
  of merchandise under the law's regime, and SENT ELECTRONICALLY
  ("Dicha declaración jurada deberá enviarse electrónicamente" — the
  electronic-channel flag is part of the duty, not an option). The
  cuenta-corriente data model itself (in/out ledger, guarantee ledger) is
  owned by GT-SPR-FR-124 of file 04 — consumed by exact id; this row owns
  only the filing cadence + filing-state record.
  (LB-001; EVID-725; cross-ref GT-SPR-FR-124)
- **GT-SPR-FR-136:** The platform side shall implement the filing JOIN:
  the monthly DJ of FR-135 rides with (presented adjunto a la Declaración
  Jurada) the planilla electrónica de seguridad social of the TRAILING
  TRES (3) MESES previos al mes que corresponda la información de la
  declaración jurada — universal for ALL enterprises benefiting from the
  law (art. 34 added paragraph, D-19-2016 art. 13), deliverable or
  sendable electronically via the Ventanilla Única para las
  Exportaciones / SEADEX (names as printed, never asserted current —
  GOQ-140). The planilla lifecycle is consumed by EXACT ID, never
  re-derived: GT-PAY-FR-170..177 of
  `gt/requirements/payroll/07_igss-contributions.md` (planilla
  electrónica lifecycle; registro patronal as filing unit; rectificación;
  late acceptance with mora; solvencia dynamics; due date), with
  GT-PAY-FR-018 (payroll/01 — the ≥3-worker planilla mode) as kin.
  (LB-002; LB-018; EVID-726/739; cross-ref GT-PAY-FR-170..177;
  GT-PAY-FR-018 kin; GOQ-140 → OQ-001)
- **GT-SPR-FR-137:** The system shall implement the maquila monthly
  coeficiente de transformación report as a compliance-calendar entry:
  enterprises dedicated to the production and transformation of raw
  materials into finished product present the report to the
  Administración Tributaria, in the means it determines, DURANTE LOS
  PRIMEROS VEINTE (20) DÍAS HÁBILES de cada mes (hábil qualifier exact —
  a DIFFERENT print from FR-135's plain días, never normalized); the
  reglamento 30 C row fixes the content window — operations of the MES
  INMEDIATO ANTERIOR — and the channel as the Oficina de Regímenes de
  Perfeccionamiento Activo virtual platform (name as printed — GOQ-140
  kin). The coeficiente computation (import quantity per export unit
  including mermas/desechos/subproductos) is owned by GT-SPR-FR-122 of
  file 04 — consumed by exact id.
  (LB-001; LB-003; EVID-725/738; cross-ref GT-SPR-FR-122)
- **GT-SPR-FR-138:** The system shall implement the annual labor-DJ +
  Boleta Estadística filing as a compliance-calendar entry: the
  declaración jurada ante Notario (labor-law compliance for the prior
  calendar year) + the Boleta Estadística are presented DENTRO DE LOS
  PRIMEROS CUARENTA (40) DÍAS DE CADA AÑO via the means MINECO provides;
  breach DARÁ LUGAR A LA CANCELACIÓN DE LOS BENEFICIOS per law art. 43
  (the cancellation workflow is FR-161's revocation surface). The
  deadline VALUE is the R80 dated-row pair owned by GT-SPR-FR-116 of file
  04 — consumed by exact id; the AG 253-2001 "20 días del mes de enero"
  original is history only and NEVER resolves as current (R80).
  (LB-004; EVID-736; cross-ref GT-SPR-FR-116; R80)
- **GT-SPR-FR-139:** The system shall implement the maquila annual
  full-nómina filing as a compliance-calendar entry: the persons owning
  the entities/enterprises and their socios o accionistas trasladan the
  TOTALITY of the worker nómina annually to the Ministerio de Trabajo y
  Previsión Social and the Inspección General de Trabajo; reglamento
  30 D fixes the deadline — DENTRO DEL PLAZO DE LOS DOS (2) PRIMEROS
  MESES DE CADA AÑO, prior calendar year, via the means MinTrabajo
  provides. The payroll-side dataset is consumed from GT-PAY-FR-170..177
  by id (never re-derived). (LB-001; LB-003; EVID-725/738; cross-ref
  GT-PAY-FR-170..177)
- **GT-SPR-FR-140:** The system shall carry the maquila
  obligation-by-regime matrix as shared dated config (valid from the
  D-19-2016/AG-3-2017 layers): reposición-franquicia companies owe ONLY
  art. 33 incisos d), e), f) (plus the universal customs-law compliance
  and the FR-136 trailing-planilla attach); CANT companies owe incisos
  a), e), f) plus the simple photocopy of the machinery import póliza
  within CUARENTA Y CINCO (45) DÍAS POSTERIORES a la fecha de la
  liquidación de la póliza; all other calificadas owe the full art. 33
  set. (LB-002; EVID-726)

### 3.2 ZF compliance cadence (law art. 36 bis; reglamento arts. 34 bis-34 quater)

- **GT-SPR-FR-141:** The system shall implement the ZF compliance
  backbone for every qualified company as compliance-monitor states keyed
  to the art. 36 bis incisos: (a) SAT information for the determination
  and seguimiento of exempt rents and operation amounts; (b) the IGSS
  planilla electrónica of cuotas laboral y patronal — planilla lifecycle
  consumed by exact id from GT-PAY-FR-170 (never re-derived); (c)
  registros contables + a sistema de inventario perpetuo of temporarily
  entered merchandise and its consumption — the accounting-surface
  invariants and condition-gate semantics are consumed by exact id from
  GT-SPR-FR-076 of file 03 (which owns the inventario perpetuo gates);
  GUARD (printed asymmetry): the ZF print states record-keeping as a
  compliance DUTY, not as a window-sustaining condition — no ZF article
  conditions the art. 21/22 ISR windows on perpetual inventory, and no
  such gate shall be invented here; (d) mermas/subproductos/desechos
  information to DPI + SAT; (e) inspection tolerance + any pertinent
  information; (f) labor-law compliance; (h) the SAT/IGSS-authorized
  informatic tools.
  (LB-005; EVID-671; cross-ref GT-PAY-FR-170; GT-SPR-FR-076)
- **GT-SPR-FR-142:** The system shall implement the ZF monthly
  coeficiente de transformación report as a compliance-calendar entry
  with its reglamento 34 bis content schema: DENTRO DE LOS PRIMEROS
  VEINTE (20) DÍAS HÁBILES de cada mes (hábil qualifier exact), covering
  the MES INMEDIATO ANTERIOR, filed via the means SAT determines TO THE
  DEPARTAMENTO DE CONTROL DE ENTES EXENTOS (SAT Exempt-Entities Control
  Department — the ZF destination, distinct from the maquila's
  Administración Tributaria surface); the report computes the coefficient
  per unit of measure of materia prima consumed and states, per produced
  good, the descripción del bien producido, the componente utilized, and
  the unidad de medida y proporción utilized. The coefficient definition
  is consumed from GT-SPR-FR-122 by id.
  (LB-005; LB-006; EVID-671/691; cross-ref GT-SPR-FR-122)
- **GT-SPR-FR-143:** The system shall implement the ZF annual full-nómina
  filing as a compliance-calendar entry: DENTRO DEL PLAZO DE LOS DOS (2)
  PRIMEROS MESES DE CADA AÑO, prior calendar year, to the Ministerio de
  Trabajo through the Inspección General de Trabajo AND — the ZF
  reglamento's addition to the law's addressees — AL MINISTERIO DE
  ECONOMÍA, via the means provided. Payroll dataset consumed from
  GT-PAY-FR-170..177 by id. (LB-006; EVID-691; cross-ref
  GT-PAY-FR-170..177)
- **GT-SPR-FR-144:** The system shall implement the ZF quarterly Boleta
  Estadística as a compliance-calendar entry + dataset record: presented
  DE FORMA TRIMESTRAL in the format elaborated by the Departamento de
  Política Industrial "dentro los quince (15) días de finalizado el
  trimestre" [deadline transcribed as printed — sic, no "de"], via the
  means MINECO provides, on two layouts — administradora fields a)-v)
  (authorized m², users by calificado type, TOTAL SALARIES PAID,
  investment, imports/exports/TAN sales, DAI/IVA/ISR paid, energy kWh)
  and user fields a)-w) (IGSS número patronal, total employees, total
  salaries, investment classes, capital origin, trade values) — the
  payroll-fed fields consumed from GT-PAY-FR-170..177 by id. QUOTING
  RULE (GOQ-137 kin): the field lists are quoted from `68_`, which
  prints the article WITH its tags (adicionado AG 52-2017; reformado AG
  65-2022); `81_`'s OCR drops the importaciones/exportaciones rows — the
  discrepancy is recorded, never silently resolved.
  (LB-007; EVID-692; cross-ref GT-PAY-FR-170..177; GOQ-137 kin)

### 3.3 Filing-state ingestion and platform joins (saas)

- **GT-SPR-FR-145:** The platform side shall ingest the filing states of
  every compliance-calendar duty of this file — monthly DJ (el Sistema
  form), trailing-3-month planilla attachment, coeficiente reports,
  annual DJ + boleta, annual nóminas, quarterly boleta, fondo
  declaration/payment receipts — from the printed channels (el Sistema /
  SEADEX / Ventanilla Única / MINECO- or SAT-provided electronic means /
  the Oficina de Regímenes de Perfeccionamiento Activo virtual platform)
  into the odoo-side compliance monitors as filed/pending/late states
  with evidence refs. Platform names are recorded AS PRINTED in their
  instrument layers; NO current SAT module-name assertion (post-2023
  DUCA/FEL world outside corpus). (LB-002; LB-003; LB-004; LB-006;
  LB-007; LB-018; EVID-726/736/738/691/692/739; GOQ-140 → OQ-001)
- **GT-SPR-FR-146:** The system shall carry the fiscal-reporting
  constancia surfaces as POINTER-ONLY rows: the supplier-side
  constancia-report and constancia-state semantics (report of constancias
  received filed with the IVA declaration; constancia document class,
  emission flow and state machine) are consumed by exact id from
  `gt/requirements/fiscal-reporting/02_retenciones-web.md` — GT-FIN-FR-052
  (cross-constancia guard), GT-FIN-FR-054 (constancia document date),
  GT-FIN-FR-055 (delivery obligation), GT-FIN-FR-065 (emission flow),
  GT-FIN-FR-066 (state machine), GT-FIN-FR-068 (IVA constancia
  semantics), GT-FIN-FR-069 (document class) — never re-derived here;
  the maquila-side delivery duty (Constancias de Adquisición de Insumos
  per local purchase, supplier invoice annotation with the calificación
  resolution number/date) is owned by file 03's art. 12 bis g) valve
  (GT-SPR-FR-085) and reglamento 30 B provenance — path-only here.
  (LB-003; EVID-738; cross-ref GT-FIN-FR-052/054/055/065/066/068/069;
  GT-SPR-FR-085)

### 3.4 The 100%-multa sanction core: diversion, solidarity, destruction (both chains)

- **GT-SPR-FR-147:** ANCHOR (load-bearing): the system shall implement
  the diversion sanction for BOTH chains as a sanction record computing a
  multa equal to the CIEN POR CIENTO (100%) of the impuestos aplicables
  no pagados (unpaid applicable taxes) on the diverted goods, with
  SOLIDARY LIABILITY of the enajenante (transferor) and adquiriente
  (acquirer) for the State's uncollected amounts: (maquila, art. 41)
  enajenación a cualquier título of merchandise imported/admitted under
  the law, or utilization for purposes distinct from those for which the
  benefit was granted; (ZF, art. 46) enajenación a cualquier título
  within the Territorio Aduanero Nacional of machinery/equipment/parts/
  components/accessories and merchandise admitted under the law, or
  use-diversion — "sin perjuicio" of any other sanctions the customs
  laws indicate. The sanction state lands on the beneficiary record and
  the affected asset/cuenta-corriente lines; the benefit windows it may
  eventually unwind are owned by GT-SPR-FR-001..033 (ZF) and
  GT-SPR-FR-061..094 (maquila) — consumed by exact id, never
  re-derived. (LB-008; LB-012; EVID-729/675; cross-ref
  GT-SPR-FR-001..033, GT-SPR-FR-061..094)
- **GT-SPR-FR-148:** The system shall implement the ZF art. 47 sanction
  as a separate sanction record: merchandise INGRESANDO O EGRESANDO de
  zonas francas SIN LLENAR LAS FORMALIDADES LEGALES correspondientes =
  multa equal to the CIEN POR CIENTO (100%) of unpaid applicable taxes,
  cumulative with customs, civil and penal law — a formalities predicate
  distinct from FR-147's diversion predicate (both may attach to the same
  movement; the records are separate). (LB-012; EVID-675)
- **GT-SPR-FR-149:** The system shall implement the maquila art. 42
  liability trigger: destruction of suspended merchandise OUTSIDE the
  zona primaria of the customs jurisdiction makes the derechos y demás
  impuestos fall due on the goods, UNLESS caso fortuito o fuerza mayor
  duly evidenced (comprobado) to the Ministerio de Finanzas Públicas —
  an evidence-gated liability row on the cuenta-corriente line linking
  to the guarantee ledger of GT-SPR-FR-124 (by id).
  (LB-008; EVID-729; cross-ref GT-SPR-FR-124)
- **GT-SPR-FR-150:** The system shall carry the multa tiers of this file
  as shared dated config (D16 rows with instrument provenance, never
  constants): 100% of unpaid applicable taxes — maquila art. 41 / ZF
  arts. 46-47; 50% of the omitted fondo payment — ZF art. 51; US$100.00
  per late export/reexport/FAUCA declaration at the day's exchange rate
  — maquila art. 29. The FX anchor of the US$100 row is its OWN rule
  ("tipo de cambio del día"), never unified with the fondo prior-day or
  tarifario Banguat anchors (GOQ-139 kin discipline, consumed from
  GT-SPR-FR-028 by id). (LB-008; LB-010; LB-012; LB-015; EVID-723/729/
  675/678; cross-ref GT-SPR-FR-028)

### 3.5 Descargo, refunds and the guarantees menu (maquila law arts. 27-30)

- **GT-SPR-FR-151:** The system shall implement the descargo
  (guarantee-release) workflow: the request is filed ante la SAT DENTRO
  DEL PLAZO DE LOS CUARENTA Y CINCO (45) DÍAS POSTERIORES a la fecha de
  presentación of the Declaración de Exportación, la reexportación or
  the FAUCA; if not filed within that window, the contribuyente pays SAT
  a multa EQUIVALENTE EN QUETZALES A US$100.00 AL TIPO DE CAMBIO DEL DÍA
  POR CADA DECLARACIÓN presented extemporáneously — and only UNA VEZ
  PAGADA LA MULTA may the request proceed (the workflow gates on the
  multa-paid flag, never skips it). Pairs with the finiquito lifecycle
  owned by GT-SPR-FR-131 of file 04 (consumed by exact id).
  (LB-010; EVID-723; cross-ref GT-SPR-FR-131)
- **GT-SPR-FR-152:** The system shall track the deposit-refund row:
  cash-deposit reembolsos are paid through a cheque librado by the
  Dirección General de Aduanas (or Aduanas de la República) DENTRO DEL
  PLAZO DE TREINTA (30) DÍAS SIGUIENTES a la presentación de la
  solicitud — pairing with the devolución refund processing owned by
  GT-SPR-FR-129 of file 04 (consumed by exact id).
  (LB-010; EVID-723; cross-ref GT-SPR-FR-129)
- **GT-SPR-FR-153:** The system shall implement the guarantees menu as
  the guarantee-type enum on the guarantee ledger (texto D-19-2016
  art. 11): a) Depósito en efectivo (cash deposit); b) Almacenes
  Generales de Depósito autorizados to operate as almacenes fiscales
  constituting a garantía específica; c) Seguro de caución (surety
  insurance); d) Garantía hipotecaria (mortgage guarantee); e) Garantía
  combinada among any of the foregoing — the law-menu layer over the
  ledger model owned by GT-SPR-FR-124 (file 04, by id) and the law-side
  SAT-authorized track of GT-SPR-FR-071 (file 03, by id); the menu rows
  ride shared dated config valid from the D-19-2016 layer.
  (LB-010; EVID-723; cross-ref GT-SPR-FR-071, GT-SPR-FR-124)

### 3.6 Prohibitions and the machinery transfer locks

- **GT-SPR-FR-154:** The system shall implement the maquila prohibitions
  + 5-year machinery transfer lock: (art. 39) NO enajenación in any form
  in the territorio nacional of merchandise internada temporalmente,
  SALVO payment of the corresponding derechos arancelarios e impuestos —
  with donaciones a entidades de beneficencia excepted when carrying
  PREVIA autorización del Ministerio de Finanzas Públicas; (art. 40)
  machinery/equipment/parts/components/accessories imported under the
  law may NOT be enajenados nor destinados a un fin distinto from the
  authorized one SALVO the DAI/import taxes/IVA they occasioned are
  covered AND, for alienation, CINCO (5) AÑOS counted DESDE LA FECHA DE
  ACEPTACIÓN DE LA PÓLIZA DE IMPORTACIÓN have elapsed, with PREVIA
  notificación a la Dirección de Política Industrial — the lock gate on
  every transfer transaction, keyed to the póliza-acceptance dates on
  the capital-goods registry owned by GT-SPR-FR-132 of file 04 (by id);
  breaches wire to FR-147's 100% multa.
  (LB-011; EVID-728; cross-ref GT-SPR-FR-132, FR-147)
- **GT-SPR-FR-155:** GUARD (cross-chain disambiguation): the system
  shall enforce the ZF purpose-lock WITHOUT any time term: ZF art. 43
  prohibits enajenación in the territorio nacional of merchandise that
  ingresó a Zona Franca (exonerada or not) afecta to DAI/import
  taxes/IVA, and art. 44 locks machinery/equipment/parts/components/
  accessories to the purpose authorized in the MINECO Resolución — the
  ZF print carries NO 5-year clock, and the maquila art. 40 lock shall
  NEVER be imported into the ZF chain: ZF release runs on the
  authorized-purpose test (+ duties where applicable) only; breaches
  wire to FR-147/148. (LB-017; EVID-674)

### 3.7 The art. 43 bis IGSS-driven suspension ladder — state machine

- **GT-SPR-FR-156:** ANCHOR (load-bearing): the system shall implement
  the art. 43 bis suspension ladder as a STATE MACHINE on the
  beneficiary, keyed to IGSS compliance states consumed by EXACT ID from
  GT-PAY-FR-170..177 (planilla lifecycle, registro patronal, late
  acceptance-with-mora, due dates) and GT-PAY-FR-018 (kin — the
  ≥3-worker planilla mode): tier DOS (2) MESES when (i) some worker is
  not inscribed per IGSS reglamentos, (ii) IGSS legislation is
  breached, or (iii) the enterprise is determined to deny workers the
  certificate to attend clínicas, hospitales y demás servicios del
  IGSS; tier CUATRO (4) MESES when, having CINCUENTA O MÁS
  TRABAJADORES, the enterprise does not proceed to their inscription;
  tier SEIS (6) MESES for non-remittance of the cuotas laborales,
  patronales o las multas correspondientes al IGSS. Each tier's driver
  records its inciso, its payroll-side evidence link and its start/end
  dates; tier constants ride shared dated config (FR-160).
  (LB-009; EVID-730; cross-ref GT-PAY-FR-170..177; GT-PAY-FR-018 kin)
- **GT-SPR-FR-157:** The system shall implement the doubling rule: the
  suspension SE DUPLICARÁ when, DURANTE EL PERÍODO DE UN AÑO calculated
  DEL UNO DE ENERO AL TREINTA Y UNO DE DICIEMBRE (calendar-year window,
  printed explicitly), the enterprise REINCIDE in POR LO MENOS DOS de
  los incisos anteriores; for the doubling computation LA SUSPENSIÓN
  MÁS ALTA applies (the highest tier among the recidivist incisos
  determines the doubled duration). Recidivism counters key on the
  MINECO sanction registry of FR-162 (by id).
  (LB-009; EVID-730; cross-ref FR-162)
- **GT-SPR-FR-158:** The system shall implement the definitive
  suspension rule: rights are suspended DEFINITIVELY for entities whose
  suspension was DOUBLED within a PERÍODO DE DOS AÑOS, or which incur
  EN POR LO MENOS TRES VECES in CUALQUIERA de los incisos — the
  definitive state is terminal on the beneficiary record (it feeds the
  cross-regime exclusion surfaces of file 06, path-only) and is never
  auto-lifted. (LB-009; EVID-730)
- **GT-SPR-FR-159:** The system shall record suspension as a
  RIGHTS-STATE overlay, never a window re-anchor: a suspension
  suspends "los derechos establecidos en la presente Ley" of the
  beneficiary for its term; the underlying per-beneficiary windows
  (GT-SPR-FR-001..033 / 061..094, by id) are NOT re-anchored, extended,
  paused or shortened by any printed rule — no suspension-driven window
  mechanic shall be invented (printed silence recorded). Temporary
  suspensions do NOT exempt the entity from complying with its IGSS
  obligations ("no exime… para cumplir con las obligaciones… con el
  IGSS" — payroll obligations continue through the suspension).
  (LB-009; EVID-730; cross-ref GT-SPR-FR-001..033, GT-SPR-FR-061..094)
- **GT-SPR-FR-160:** The system shall carry the ladder configuration as
  shared dated data (D16): tiers 2/4/6 meses; the ≥50-trabajadores
  threshold for the 4-month tier; the calendar-year recidivism window
  (1-Jan–31-Dec, ≥2 incisos, highest tier); the 2-year doubled /
  3×-any-inciso definitive triggers — all with instrument provenance
  D-19-2016 art. 17 (added 31-03-2016; now primary from `84_`,
  consolidated-print-consistent — EVID-752/730). GOQ-08 RESOLVED: no
  pre-2016 ladder exists in print, and D-19-2016's own transitorios
  (readable at `84_` arts. 28-30 + the untitled art. 18 — EVID-753/757)
  print no ladder-specific transitional mechanic (art. 29 only orders
  the IGSS complaint offices + e-service feeding the suspensions); no
  transitional mechanic shall be modeled.
  (LB-009; EVID-730/752/753/757; GOQ-08 resolved → OQ-005)

### 3.8 Maquila enforcement ladder: revocation, the 23 quater prerequisite, SAT registry

- **GT-SPR-FR-161:** The system shall implement the maquila revocation
  causales of law art. 43 as lifecycle states: (a) production not
  initiated within the plazo of the calificación resolution (or its
  prórroga); (b) cierre, disolución o quiebra of the enterprise; (c)
  breach of the obligations contained in the calificación resolution —
  with the DPI valve: "la Dirección de Política Industrial podrá
  apercibir POR UNA SOLA VEZ a la empresa infractora" (a one-time
  formal warning before revocation, at DPI's option). Consumed by exact
  id, never re-derived: the apercibimiento record (30 días hábiles
  cure) = GT-SPR-FR-114 of file 04; the labor-ruling fast-track (5+5
  días) = GT-SPR-FR-115 of file 04; the R80-linked cancellation of
  FR-138 wires here as a causal-c) breach. Revocation consequences on
  requalification bars are cross-regime — `06_cross-regime-bridges.md`,
  path-only. (LB-004; LB-008; EVID-729/736; cross-ref GT-SPR-FR-114,
  GT-SPR-FR-115, GT-SPR-FR-116)
- **GT-SPR-FR-162:** The system shall implement the reglamento 23
  quater enforcement wiring around the FR-156 ladder: PREVIOUS to any
  art. 43 bis suspension MINECO must run the art. 23 apercibimiento
  (consumed from GT-SPR-FR-114 by id — the prerequisite gate on the
  suspension state machine); on failure within that plazo, the
  Departamento de Política Industrial issues dictamen for MINECO to
  suspend; once the resolution is FIRME, MINECO informs the
  Departamento de Control de Entes Exentos de la Intendencia de
  Recaudación y Gestión and the Intendencia de Aduanas de la SAT, which
  make the suspension effective (disable the beneficiary) A PARTIR DEL
  DÍA INMEDIATO SIGUIENTE de receiving the resolution — which states
  the sanction term — and RE-HABILITAN the beneficiary in their
  registros informáticos when the term ends (a disable/enable state
  ingested and mirrored, never emulated); and MINECO leads a REGISTRO
  DE LAS SANCIONES APLICADAS to satisfy the art. 43 bis
  penultimate-paragraph computation — the system's sanction ledger
  mirrors that registry and feeds FR-157/FR-158.
  (LB-004; EVID-736/777; cross-ref GT-SPR-FR-114, FR-157, FR-158)

### 3.9 ZF revocation, the 15-day hearing, boleta-breach cancellation

- **GT-SPR-FR-163:** The system shall implement the ZF revocation
  causales as lifecycle states: administradoras (art. 48) — incumplimiento
  of the objectives/obligations/requisitos of the authorization
  resolution; failure to start operations within the resolution term (or
  prórroga) for causes imputable to it; TRÁFICO ILÍCITO de mercancías;
  entry of merchandise endangering the environment or the population's
  health; usuarios (art. 49) — resolution breach; tráfico ilícito;
  dangerous goods; revocation is DE OFICIO by MINECO with copies to
  Aduanas and Rentas Internas; the ONE-TIME apercibimiento valve is
  available only for the non-criminal causales (48 b)/d); 49 c));
  tráfico ilícito cases additionally trigger INCAUTACIÓN (seizure) with
  the goods placed at the disposal of the courts [printed "podrá a
  disposición" — sic], civil and penal responsibilities preserved.
  (LB-013; EVID-676)
- **GT-SPR-FR-164:** The system shall implement the ZF hearing gate as
  a precondition on EVERY sanction resolution of the ZF chain: for any
  incumplimiento of the law's obligations, the administrative authority
  must OÍR AL INTERESADO before issuing the corresponding resolution,
  granting UN PLAZO DE 15 DÍAS (plain días, transcribed exactly — GOQ-99
  kin; a DIFFERENT print from the fondo's 10 días hábiles cure). No ZF
  sanction workflow (revocation FR-163, cancellation FR-165, fondo
  referral FR-168) may close without a completed hearing record.
  (LB-006; EVID-691; GOQ-99 → OQ-002)
- **GT-SPR-FR-165:** The system shall implement the boleta-breach
  cancellation wire: incumplimiento of the art. 34 quater filing duty
  (FR-144) DARÁ LUGAR A LA CANCELACIÓN DE LOS BENEFICIOS by MINECO
  CONFORME LO ESTABLECEN LOS ARTÍCULOS 48 Y 49 DE LA LEY — i.e. the
  calendar breach of FR-144 feeds FR-163's causales through the FR-164
  hearing gate; the cancellation state lands on the benefit rows owned
  by GT-SPR-FR-001..033 (by id, never re-derived).
  (LB-007; EVID-692; cross-ref FR-144, FR-163, FR-164,
  GT-SPR-FR-001..033)

### 3.10 Fondo enforcement ladder (ZF art. 51 + AG 296-94 arts. 9-10)

- **GT-SPR-FR-166:** The system shall implement the fondo late-payment
  sanction on top of the fondo liability engine owned by
  GT-SPR-FR-022..025 of file 01 (consumed by exact id): non-payment or
  late payment of the art. 36 e) levy imposes a multa of the equivalent
  CINCUENTA POR CIENTO (50%) of the same (the omitted payment) + daily
  INTERESES RESARCITORIOS for each day of mora at the TASA DE INTERÉS
  ACTIVA MÁS ALTA DEL MERCADO BANCARIO — the rate is an EXTERNAL market
  reference with no fixed index named in the instrument (GOQ-10 kin:
  mora-rate externals are never hardcoded; the row stores a
  rate-source-external flag and consumes an externally supplied value).
  The resarcitorios are charged SIN NECESIDAD DE REQUERIMIENTO ALGUNO
  (no prior demand needed — accrual starts at default).
  (LB-015; EVID-678; cross-ref GT-SPR-FR-022..025; GOQ-10 → OQ-003)
- **GT-SPR-FR-167:** The system shall implement the fondo enforcement
  sequence: the Dirección General de Rentas Internas DETERMINA DE OFICIO
  lo caído en mora; the Entidad Administradora is EMPLAZADA EN
  AUDIENCIA to, DENTRO DE LOS DIEZ (10) DÍAS HÁBILES SIGUIENTES al de la
  notificación de la providencia respectiva, present the omitted
  liquidation and make the payment effective (the cure window — hábil
  qualifier exact, a DIFFERENT print from FR-164's plain-días hearing);
  on expiry without payment, DGRI resolves declaring the determination
  FIRME and initiates the JUICIO ECONÓMICO-COACTIVO — the state machine
  segment: default → de-oficio determination → hearing/10-días-hábiles
  cure → firme → coactivo. (LB-015; EVID-678)
- **GT-SPR-FR-168:** The system shall implement the fondo verification
  cycle: the Dirección de Política Industrial verifies the
  administradoras' declarations every SEIS (6) MESES against the total
  area ocupada, vendida o arrendada; where a MENOR area than the real
  one was declared, DPI informs DGRI which adjusts the omitted payment
  and proceeds per law art. 51 (wiring into FR-166/FR-167); non/late
  payment is likewise put before DGRI; payment-receipt copies evidence
  the declaration/payment duties (AG 296-94 arts. 9-10). The 1994
  one-time 30-day amnesty transitorio is recorded as history only.
  (LB-016; EVID-704; cross-ref FR-166, FR-167)

### 3.11 Defraudación aduanera (art. 50 Bis) and track disambiguation + platform-name negative

- **GT-SPR-FR-169:** The system shall implement the art. 50 Bis fraud
  flag (added by D-6-2021 art. 4, effective 1-Jun-2021 — publication
  day, R73): obtaining the ZF calificación MEDIANTE SIMULACIÓN,
  OCULTACIÓN, MANIOPRA, ARDID O CUALQUIER OTRA FORMA DE ENGAÑO
  ["ardido cualquier otra" — sic as printed] to MINECO or SAT is a CASO
  ESPECIAL DE DEFRAUDACIÓN ADUANERA — a compliance flag on the
  beneficiary pairing with the art. 5 Bis h) exclusion surface (file 02
  territory, path-only); the sanction mechanics of defraudación
  aduanera live in the criminal/customs-fraud regime OUTSIDE this
  corpus and are NEVER invented here.
  (LB-014; EVID-677; cross-ref R73)
- **GT-SPR-FR-170:** DISAMBIGUATION ANCHOR (regime-law vs CT sanction
  tracks): the sanctions of this file are REGIME-LAW sanctions — multas
  on unpaid taxes computed by the regime laws, benefit suspension /
  revocation / cancellation, fondo enforcement — applicable "sin
  perjuicio de cualesquiera otras sanciones" of customs, civil, penal
  and Código Tributario law; the CT sanction surfaces (Art. 94 multa
  table, cierre temporal, commutation) are owned by taxation/06 and
  consumed by exact id only: GT-TAX-FR-214 (multa table), GT-TAX-FR-216
  (cierre temporal 10-20 days), GT-TAX-FR-217 (commutation), with
  GT-TAX-FR-232 (prescription-anchored retention) as kin — NEVER merged
  into, re-derived from, or double-counted with the regime-law records
  of this file (a regime sanction row records its track = regime-law;
  CT-track exposure is a separate pointer).
  (LB-008; LB-012; EVID-729/675; cross-ref GT-TAX-FR-214/216/217;
  GT-TAX-FR-232 kin)
- **GT-SPR-FR-171:** NEGATIVE ANCHOR (GOQ-140 — owned by this file's
  integration): the platform names printed in the instruments — el
  Sistema (Sistema Integrado de Operación de los Regímenes de
  Perfeccionamiento Activo), SEADEX (Servicio Electrónico de
  Autorización de Exportaciones), la Ventanilla Única para las
  Exportaciones, the Oficina de Regímenes de Perfeccionamiento Activo,
  the MINECO/SAT/MinTrabajo-provided electronic means — are cited ONLY
  as printed in their instrument layers; the system shall NEVER assert
  a current SAT module name for any of them (the post-2023 DUCA/FEL
  world is outside the corpus). Integration mappings resolve channel
  labels from the printed-name rows until an external source lands.
  (LB-002; LB-003; LB-004; LB-018; EVID-726/736/738/739; GOQ-140 →
  OQ-001)

## 4. Data Model

Layer semantics: the compliance-calendar monitors, sanction/suspension
state machines and guarantee-ledger rows live in the Odoo client; the
deadline rows, multa tiers and ladder configuration are shared dated
config both sides honor identically; SEADEX/planilla joins and
filing-state ingestion are SaaS-side surfaces (with payroll/07 fin-side
pointers). The system records compliance states and sanctions — it never
emulates MINECO, SAT, Aduanas, el Sistema or the IGSS. No printed data
table in this file warrants a CSV sidecar (the deadline-row and tier sets
are small seed-row sets; the wave index may consolidate them later).

**Compliance calendar (l10n_gt_regimes.compliance_calendar / .filing_state):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_regimes.compliance_calendar | chain · duty · period_type | select pair | maquila · zf; duties: cc_dj_monthly · coeficiente_monthly · annual_labor_dj_boleta · annual_nomina · quarterly_boleta · cant_poliza_copy · fondo_cycle; monthly · quarterly · annual · per-event | FR-134, FR-135, FR-137..139, FR-140, FR-142..144 |
| l10n_gt_regimes.compliance_calendar | deadline_rule | structured | day-count + qualifier EXACT as printed: días (plain) vs días hábiles — two enumerations, never coerced (GOQ-99); anchor: month-start / quarter-end / year-start / event-date | FR-134 |
| l10n_gt_regimes.compliance_calendar | valid_from · valid_to · instrument | date pair + provenance | D16 rows: art. 33 (D-19-2016 layer) · 30 C/30 D (AG 3-2017) · 23 Ter (AG 3-2017 restatement — R80 pair via FR-116) · 34 bis/ter/quater (AG 52-2017/AG 65-2022) | FR-134..144 |
| l10n_gt_regimes.filing_state | duty · period · state · channel · evidence | composite | states: pending · filed · late; channels as printed (el Sistema · SEADEX · Ventanilla Única · medios MINECO/SAT/MinTrabajo — GOQ-140 rows); evidence refs (form id, planilla ids, receipt) | FR-135, FR-145 |
| l10n_gt_regimes.cc_dj_attachment | dj_filing · planilla_ids (trailing 3 months) · channel | m2m + select | the art. 34/33-reglamento join; planilla records consumed from payroll/07 by id | FR-136 |
| l10n_gt_regimes.boleta | quarter · layout (administradora a)-v) / usuario a)-w)) · dataset | date + select + json | m², users by type, salarios pagados, investments, imports/exports/TAN, DAI/IVA/ISR paid, IGSS número patronal, employees, energy kWh — field lists quoted from 68_ (GOQ-137 kin) | FR-144 |

**Sanctions + state machines (l10n_gt_regimes.sanction / .suspension / .ladder_config):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_regimes.sanction | track · type | select pair | track: regime_law (this file — FR-170 disambiguation; CT track = taxation/06 pointer); types: multa_100_diversion · multa_100_informal_entry_exit · multa_50_fondo · multa_usd100_descargo · destruction_liability · revocation · cancellation · suspension · definitive_suspension · fraude_flag | FR-147..149, FR-151, FR-156..158, FR-161, FR-163, FR-165..169 |
| l10n_gt_regimes.sanction | basis_amount · solidary_parties · unpaid_taxes_basis | monetary + m2m | 100%/50% tiers from shared config; enajenante + adquiriente solidary rows (both chains) | FR-147, FR-148, FR-150 |
| l10n_gt_regimes.suspension | beneficiary · tier_months (2/4/6) · driver_inciso (a.i/a.ii/a.iii/b/c) · start · end · payroll_evidence | composite | drivers keyed to GT-PAY-FR-170..177 states by id; ≥50-trabajadores threshold for tier b | FR-156 |
| l10n_gt_regimes.suspension | doubled (calendar-year ≥2 incisos, highest tier) · definitive (2-yr doubled / 3× any inciso) · rights_state overlay | booleans + linkage | never a window re-anchor (FR-159); feeds file-06 exclusion pointers | FR-157, FR-158, FR-159 |
| l10n_gt_regimes.ladder_config | tier_rows · thresholds · recidivism_windows | dated config | 2/4/6 meses · 50 trabajadores · 1-enero–31-diciembre · 2 años · 3× — provenance D-19-2016 art. 17 (31-03-2016; primary `84_`); GOQ-08 resolved: no transitional mechanics printed | FR-160 |
| l10n_gt_regimes.sanction_registry | applied_sanctions ledger | one2many | mirrors MINECO's 23 quater registro de sanciones — feeds doubling/definitive computation | FR-157, FR-158, FR-162 |
| l10n_gt_regimes.sat_registry_state | disabled_from (day after resolution receipt) · reEnable_at term end | dates | disable/enable ingested + mirrored, never emulated | FR-162 |
| l10n_gt_regimes.apercibimiento linkage | one_time_valve · hearing_15_dias (ZF, plain) · cure_10_habiles (fondo) | composite | maquila apercibimiento = file-04 FR-114 by id; ZF hearing gate on every ZF sanction; fondo cure inside FR-167 sequence | FR-161, FR-164, FR-167 |

**Descargo, refunds, guarantees, locks, fondo enforcement (l10n_gt_regimes.*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_regimes.descargo | declaration_ref (export/reexport/FAUCA) · deadline (+45 días) · multa (US$100.00 @ FX-of-day, per declaration) · multa_paid_flag | composite | once paid, the request proceeds (workflow gate) | FR-151 |
| l10n_gt_regimes.refund_row | request_date · due (request + 30 días) · instrument (DGA cheque) | dates | pairs file-04 FR-129/131 by id | FR-152 |
| l10n_gt_regimes.guarantee | type_enum a)-e) | select | efectivo · almacén fiscal · seguro de caución · hipotecaria · combinada (menu valid from D-19-2016 layer) | FR-153 |
| l10n_gt_regimes.transfer_lock | asset (capital-goods registry link) · poliza_acceptance_date · unlock_date (+5 años) · duties_paid · dpi_notified | composite | maquila art. 40 lock; GUARD: no ZF counterpart row (no time term printed) | FR-154, FR-155 |
| l10n_gt_regimes.fondo_enforcement | default_event · multa_50 · resarcitorios_accrual (external rate — GOQ-10 kin) · determination (de oficio) · cure_deadline (10 días hábiles) · firme · coactivo · verification_cycle (6 meses) | state machine | pairs the fondo engine GT-SPR-FR-022..025 (file 01) by id | FR-166, FR-167, FR-168 |
| l10n_gt_regimes.hearing | sanction_ref · granted_plazo (15 días plain) · completed | composite | ZF precondition on every sanction resolution | FR-164 |

**Dated config (l10n_gt_regimes.dated_value — D16 instrument + valid_from/valid_to + provenance):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_regimes.dated_value | key | char | maquila_cc_dj_deadline (20 días plain) · maquila_coeficiente_deadline (20 días hábiles) · zf_coeficiente_deadline (20 días hábiles → Entes Exentos) · annual_labor_dj (R80 pair via FR-116) · annual_nomina_2_months (both chains; ZF + MINECO) · zf_boleta_quarterly (15 días post-quarter) · zf_hearing_15_dias · fondo_cure_10_habiles · descargo_45_dias + usd100_fx_of_day · multa_tiers (100% / 50%) · ladder_config (2/4/6, 50, 1-yr, 2-yr, 3×) · garantia_menu a)-e) · transfer_lock_5_years | FR-134..171 |
| l10n_gt_regimes.dated_value | qualifier | enum | dias · dias_habiles — stored per row exactly as printed; no conversion helpers between them (GOQ-99) | FR-134 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2; wave defaults): `odoo` = the
compliance-calendar monitors, sanction/suspension state machines and
guarantee-ledger rows in the LGPL client; `shared` = deadline rows, multa
tiers and ladder configuration as dated config both sides honor
identically; `saas` = SEADEX/planilla joins and filing-state ingestion
(with payroll/07 fin-side pointers). Model names are stable across Odoo
17/18/19/20; no version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-134 | shared | compliance_calendar deadline_rule | qualifier enum | GOQ-99 hallmark: días vs días hábiles never normalized; D16 provenance rows |
| FR-135 | odoo | compliance_calendar + filing_state | cc_dj_monthly | 20 días PLAIN + electronic flag; ledger itself = GT-SPR-FR-124 by id |
| FR-136 | saas | cc_dj_attachment ingestion | DJ + trailing 3-month planilla | SEADEX/Ventanilla Única as printed (GOQ-140); GT-PAY-FR-170..177 by id |
| FR-137 | odoo | compliance_calendar | coeficiente_monthly (maquila) | 20 días HÁBILES; prior-month ops; computation = GT-SPR-FR-122 by id |
| FR-138 | odoo | compliance_calendar | annual_labor_dj_boleta | Value = R80 pair from GT-SPR-FR-116 by id; breach wires to FR-161 |
| FR-139 | odoo | compliance_calendar | annual_nomina (maquila) | First 2 months (30 D); GT-PAY-FR-170..177 by id |
| FR-140 | shared | obligation matrix config | reposición d/e/f · CANT a/e/f + 45-días | Valid from D-19-2016/AG-3-2017 layers |
| FR-141 | odoo | compliance monitors (ZF backbone) | 36 bis a)-h states | IGSS planilla = GT-PAY-FR-170 by id; inventario perpetuo = GT-SPR-FR-076 by id (guard: no ZF window gate) |
| FR-142 | odoo | compliance_calendar + coeficiente schema | zf_coeficiente_monthly | 20 días hábiles → Departamento de Control de Entes Exentos |
| FR-143 | odoo | compliance_calendar | annual_nomina (ZF) | First 2 months; MinTrabajo/IGT + MINECO |
| FR-144 | odoo | boleta record + calendar | quarterly layouts a)-v)/a)-w) | "dentro los quince (15) días" [sic]; fields from 68_ (GOQ-137 kin); payroll-fed fields by id |
| FR-145 | saas | filing_state ingestion | all duties | Channels as printed; state lands odoo-side |
| FR-146 | shared | pointer rows | constancia surfaces | GT-FIN-FR-052/054/055/065/066/068/069 by id; delivery duty = GT-SPR-FR-085 |
| FR-147 | odoo | sanction (multa_100_diversion) | both chains | Solidary enajenante+adquiriente; windows 001..033/061..094 by id |
| FR-148 | odoo | sanction (multa_100_informal) | art. 47 | Separate predicate from FR-147 |
| FR-149 | odoo | destruction_liability | art. 42 | Force-majeure evidence gate (MinFin) |
| FR-150 | shared | dated_value multa_tiers | 100% · 50% · US$100 FX-of-day | FX anchors never unified (GOQ-139 kin; GT-SPR-FR-028 by id) |
| FR-151 | odoo | descargo workflow | +45 días · US$100 gate | Pairs GT-SPR-FR-131 by id |
| FR-152 | odoo | refund_row | ≤30 días DGA cheque | Pairs GT-SPR-FR-129 by id |
| FR-153 | odoo | guarantee.type_enum | menu a)-e) | Ledger = GT-SPR-FR-124; law-side track = GT-SPR-FR-071 (both by id) |
| FR-154 | odoo | transfer_lock (maquila) | +5 años from póliza acceptance | Registry link GT-SPR-FR-132 by id; wires to FR-147 |
| FR-155 | shared | transfer_lock guard | no ZF time term | ZF = authorized-purpose test only; maquila 5-year never imported |
| FR-156 | odoo | suspension state machine | tiers 2/4/6 | Drivers from GT-PAY-FR-170..177 by id; GT-PAY-FR-018 kin |
| FR-157 | odoo | suspension doubling | calendar-year ≥2 incisos | Highest tier applies; counters from FR-162 registry |
| FR-158 | odoo | definitive suspension | 2-yr doubled / 3× any | Terminal; feeds file-06 pointers |
| FR-159 | odoo | rights_state overlay | never window re-anchor | Windows 001..033/061..094 by id; IGSS duties continue |
| FR-160 | shared | ladder_config | 2/4/6 · 50 · 1-yr · 2-yr · 3× | Provenance D-19-2016 art. 17 (primary `84_`); GOQ-08 resolved — no transitionals printed |
| FR-161 | odoo | revocation causales (maquila) | art. 43 a)-c) | Apercibimiento = GT-SPR-FR-114 by id; 5+5 = FR-115 by id |
| FR-162 | odoo | 23 quater wiring + sanction_registry + sat_registry_state | prerequisite + disable/enable | Apercibimiento prerequisite from FR-114 by id; disable from day after receipt |
| FR-163 | odoo | revocation causales (ZF) | arts. 48/49/50 | One-time apercibimiento for non-criminal causales; seizure flag |
| FR-164 | odoo | hearing gate (ZF) | 15 días plain | Precondition on every ZF sanction (GOQ-99 kin) |
| FR-165 | odoo | cancellation wire | boleta breach → arts. 48/49 | FR-144 → FR-163 via FR-164; windows by id |
| FR-166 | odoo | fondo_enforcement sanction | 50% + resarcitorios | Rate EXTERNAL (GOQ-10 kin); accrual without prior demand; engine = GT-SPR-FR-022..025 by id |
| FR-167 | odoo | fondo sequence | 10 días hábiles cure → firme → coactivo | De-oficio determination; hábil qualifier exact |
| FR-168 | odoo | fondo verification cycle | every 6 meses | Under-declaration → DGRI adjustment + art. 51; 1994 amnesty = history |
| FR-169 | odoo | fraude flag (50 Bis) | D-6-2021 art. 4 | Effective 1-Jun-2021 (R73); mechanics outside corpus — never invented |
| FR-170 | shared | sanction.track disambiguation | regime_law vs CT | GT-TAX-FR-214/216/217 by id; GT-TAX-FR-232 kin; never merged |
| FR-171 | shared | platform-name negative rows | GOQ-140 owned | Printed names only; no current module-name assertion |

Version-regime note (D12/D15/D16): this file is a dated-instrument regime
— every deadline row, multa tier, ladder constant and menu row resolves
as-of the domain anchor date and carries instrument provenance (maquila
law arts. 33-43 bis through the D-19-2016 layer (primary `84_` — GOQ-08
resolved); AG 533-89 arts. 23-33
through the AG-3-2017-current print; ZF law through D-6-2021 effective
1-Jun-2021; AG 242-90 arts. 34-34 quater through the AG 52-2017/AG
65-2022 tags; AG 296-94). The GOQ-99 qualifier discipline is version
load-bearing: the plain-días and días-hábiles prints coexist within the
same articles and the same chain (art. 33 b vs 33 h; art. 34 hearing vs
art. 51 cure) — the qualifier is stored per row exactly as printed with
no conversion helper. Hard gates in this file: the FR-151 multa-paid gate
on descargo, the FR-164 hearing precondition on ZF sanctions, the FR-162
apercibimiento prerequisite on suspensions, the FR-154/155 transfer
locks, and the FR-138 annual-DJ breach wire to cancellation.

## 6. Acceptance Criteria

- **AC-001:** Given the compliance-calendar configuration, when inspected,
  then the maquila cuenta-corriente DJ row prints "primeros veinte (20)
  días" with qualifier días (plain) + the electronic-filing flag, the
  maquila and ZF coeficiente rows print "primeros veinte (20) días
  hábiles" with qualifier días hábiles, and no code path converts one
  qualifier into the other (GOQ-99). (FR-134, FR-135, FR-137, FR-142)
- **AC-002:** Given a maquila DJ filing for information month M, when
  assembled, then it carries the trailing 3-month IGSS planilla
  attachment (months M-3..M-1) with planilla records resolving through
  GT-PAY-FR-170..177 by id, and the channel row prints SEADEX/Ventanilla
  Única as printed — never a current module name (GOQ-140).
  (FR-136, FR-145, FR-171)
- **AC-003:** Given the annual labor-DJ deadline for a current-period
  filing, when resolved, then it returns the first-40-días + Boleta
  Estadística row via GT-SPR-FR-116 by id; and given the filing is
  recorded 41 días into the year, then the breach wires to the FR-161
  cancellation surface. (FR-138, FR-161)
- **AC-004:** Given a ZF quarter ending on date Q, when the boleta
  calendar resolves, then the deadline is Q + 15 días with the dataset
  validating the administradora a)-v) or usuario a)-w) layout (salaries,
  IGSS patronal number, DAI/IVA/ISR paid present); and given the boleta
  is never filed, then a cancellation case opens against FR-163 causales
  through the FR-164 hearing gate, citing law arts. 48/49.
  (FR-144, FR-163, FR-164, FR-165)
- **AC-005:** Given a diverted-goods event (enajenación or use-diversion)
  in either chain, when the sanction computes, then the multa equals
  100% of the unpaid applicable taxes with enajenante and adquiriente
  both recorded as solidary parties; and given a ZF entry/exit missing
  formalities, then a separate art. 47 sanction record opens alongside
  any art. 46 record. (FR-147, FR-148, FR-150)
- **AC-006:** Given an export declaration presented on date D with its
  descargo requested on D + 46 días, then the workflow demands the
  US$100.00-per-declaration multa at the day's FX before proceeding;
  and given the multa pays, then the request proceeds. Given a cash
  deposit refund request, then the due date is request + 30 días by DGA
  cheque. (FR-151, FR-152)
- **AC-007:** Given a beneficiary inscribing none of its 60 workers,
  then a 4-month suspension tier opens (≥50 threshold) AFTER the
  art. 23 apercibimiento prerequisite completes (23 quater); given a
  non-remittance of cuotas, then the tier is 6 months; and given
  reoffence in two incisos within 1-Jan–31-Dec, then the doubled
  duration equals 2× the HIGHEST tier. (FR-156, FR-157, FR-162)
- **AC-008:** Given a beneficiary whose suspension was doubled within a
  2-year period (or a third incursion in any inciso), then the
  definitive-suspension state is terminal; and given any suspension, then
  the underlying windows (GT-SPR-FR-001..033/061..094) remain
  un-re-anchored while the IGSS obligations continue.
  (FR-158, FR-159)
- **AC-009:** Given a firme suspension resolution received by SAT on date
  R, then the registry-state row disables the beneficiary from R + 1 day
  and re-enables at term end; and the sanction registry feeding the
  doubling/definitive computations mirrors MINECO's 23 quater ledger.
  (FR-162)
- **AC-010:** Given an maquila-benefit machinery transfer attempted 4
  years after póliza acceptance, then it is blocked (5-year lock; duties
  + DPI notification required after year 5); and given the same attempt
  on a ZF asset, then the gate runs ONLY on the authorized-purpose test —
  no 5-year term applies (cross-chain guard). (FR-154, FR-155)
- **AC-011:** Given a fondo payment missed at the first-5-días deadline,
  then the enforcement segment opens: 50% multa + daily resarcitorios
  accruing from default at an externally supplied highest-active-bank
  rate (rate-source-external flag; never a hardcoded constant — GOQ-10
  kin), a 10-días-hábiles cure window from notification, and on expiry a
  firme determination + juicio económico-coactivo state; and given the
  6-month verification finds under-declared m², then the DGRI adjustment
  wires into the same segment. (FR-166, FR-167, FR-168)
- **AC-012:** Given a ZF qualification obtained by deception, then the
  art. 50 Bis defraudación-aduanera flag sets on the beneficiary (no
  invented sanction mechanics; art. 5 Bis h) exclusion consumed as a
  file-06 pointer); and given any sanction record of this file, then its
  track reads regime_law with CT-track exposure only as a taxation/06
  pointer (GT-TAX-FR-214/216/217 by id — never merged).
  (FR-169, FR-170)
- **AC-013:** Given the obligation matrix, when a reposición-franquista
  company's calendar resolves, then only duties d)/e)/f) (+ the universal
  trailing-planilla attach) appear; and given a CANT company, then the
  45-day machinery-póliza-copy duty also appears. (FR-140)
- **AC-014:** Given the ZF compliance backbone of a qualified company,
  then the inventario-perpetuo duty surfaces as a compliance monitor
  whose invariants resolve through GT-SPR-FR-076 by id, with NO
  ZF-window-sustaining gate (printed asymmetry guard); and the annual
  nómina row addresses MinTrabajo/IGT + MINECO within the first 2 months.
  (FR-141, FR-143)
- **AC-015:** Given any ZF sanction workflow, when it attempts to close
  without a completed 15-días hearing record, then it is blocked; and
  given the maquila apercibimiento valve, then it is available exactly
  once per infringing enterprise (por una sola vez).
  (FR-161, FR-164)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
this file OWNS GOQ-140 (platform-name currency — "SR5 integration" per
the register) and carries kin rows for GOQ-99 (deadline qualifiers),
GOQ-04 (IGSS externals via the planilla consumption), GOQ-10 (mora-rate
external — fondo resarcitorios) and GOQ-08 (RESOLVED — D-19-2016 =
`84_` primary: the 43 bis ladder, the art. 34 attach ¶ and the 36 bis
stack primary-verified, the transitorios readable with no ladder
mechanic, and the reglamento-side 23 quater text now primary from `95_`).
No gaps beyond the 140-GOQ register were treated as open questions; the
68_-vs-81_ boleta field-list drift is recorded as a GOQ-137 kin quoting
rule (FR-144), not a new question; genuinely new gaps would be
report-only to the controller (none found).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-140 (owned): "Platform-name currency: 'el Sistema' / Oficina de Regímenes de Perfeccionamiento Activo / SEADEX / Ventanilla Única / Plataforma DPI — current SAT module names (post-2023 DUCA/FEL world) outside corpus." FR-136/145/171 (and the GOQ-140 kin rows on FR-137/164) record names only as printed (1989-2017 instrument layers); no integration mapping may assert current module names until an external source lands. | no | GT synthesis wave S-GT6/S-GT7 → W6 partner ask | open |
| OQ-002 | GOQ-99 (kin): deadline qualifiers transcribed exactly per instrument — the plain-días prints (cuenta-corriente DJ first 20 días; ZF hearing 15 días; annual DJ first 40 días) are never normalized with the días-hábiles prints (coeficiente first 20 días hábiles; fondo cure 10 días hábiles; apercibimiento 30 días hábiles). Statutory qualifier semantics (what a plain "día" excludes) need the LAT/CT qualifier evidence owned by taxation/04 §7 — consumed as resolved there, never re-derived. | no | GT synthesis wave S-GT6/S-GT7 (consumes taxation/04 §7 resolution by pointer) | open |
| OQ-003 | GOQ-10 kin (mora external): the fondo resarcitorios rate = "la tasa de interés activa más alta del mercado bancario" — an external market reference with no fixed index named in the instrument; FR-166 stores a rate-source-external flag and consumes an externally supplied value. Acquiring the current rate source (SIP/Banguat/MinFin practice) closes the configuration input; the IGSS planilla due-date/mora externals of the FR-136 consumption remain GOQ-04 kin (payroll/07 §7 rows). | no | GT synthesis wave S-GT6/S-GT7 → W6 partner ask | open |
| OQ-004 | GOQ-04 (kin): the suspension-ladder drivers and the trailing-3-month planilla ride IGSS cuota rates, bases, topes and planilla deadlines that are ALL external (JD reglamentos, Acuerdo 1118 family / 1421); this file consumes GT-PAY-FR-170..177 by exact id and asserts no IGSS value. | no | GT synthesis wave S-GT6/S-GT7 (payroll/07 §7 owns the IGSS half) | open |
| OQ-005 | GOQ-08 (kin, transitional-clause dependency): RESOLVED — D-19-2016 = `84_` corpus primary (EVID-746..758): the art. 43 bis ladder (art. 17) and the art. 34 trailing-planilla ¶ (art. 13) are primary-verified (EVID-751/752), and the transitorios are readable (arts. 28-30 + the untitled art. 18 — EVID-753/757): no transitional mechanic on the ladder/attach is printed (FR-160 keeps the no-modeling guard); the reglamento-side 23 quater text is now primary from AG 3-2017 (`95_` art. 17 — EVID-777). No residual dependency for this file. | no | GT synthesis wave S-GT6/S-GT7 (closed by the 84_/95_ acquisition) | resolved |
