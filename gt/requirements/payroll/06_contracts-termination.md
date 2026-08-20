# GT — Payroll — Contracts, termination and indemnización: taxonomy, despido, preaviso, finiquito

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Guatemala Código de Trabajo (Labor Code, CT, Decreto
1441) contract and termination layer: the individual-employment-contract
concept of Art. 18 and the three-class taxonomy of Art. 25 — *por tiempo
indefinido* (indefinite), *a plazo fijo* (fixed-term) and *para obra
determinada* (specific work) — under the Art. 26 INDEFINITE PRESUMPTION
(every contract is presumed indefinite absent licit express proof or
stipulation; plazo fijo / obra determinada are EXCEPTION classes valid only
for accidental or temporal services, and they convert to indefinite in
permanent-activity enterprises whose cause subsists at term expiry); the
*substitución del patrono* (employer substitution) rule of Art. 23 with its
six-month joint-liability window; the two-month *período de prueba*
(probation) of Art. 81 with its simulation ban; the *despido con justa
causa* (justified-dismissal) registry of Art. 77 — including the absence
cause f): two complete consecutive *días laborales* (working days) or six
*medios días laborales* (half working days) in one calendar month — the
Art. 78 written-cause communication duty, the judicial proof gate and the
*salarios caídos* (lapsed salaries) award of up to twelve months as a
SEPARATE damages line; the *despido indirecto* (indirect dismissal) trigger
of Art. 79 a) — non-payment of the complete salary at the agreed time and
place opens the FULL Art. 82 indemnización — and the Art. 80 abandonment
rule (worker quitting without justa causa owes *preaviso*); THE termination
money scale of Art. 82: *indemnización por tiempo servido* (severance for
time served) = ONE MONTH OF SALARY PER YEAR of continuous service, prorated
under a year, with NO maximum cap, computed on the average of the LAST SIX
MONTHS of *salario completo* (ordinary + extraordinary, Art. 93), with the
IGSS-pension actuarial offsets and the 50% rule for retirement without IGSS
protection; the WORKER-side *preaviso* (advance notice) scale of Art. 83 —
one week / ten days / two weeks / one month by tenure band — payable in
money ONLY with employer consent; the Art. 84 early-termination damages
floor for plazo fijo / obra contracts (one day of salary per month worked,
payable at cessation); the Art. 85 death-of-worker indemnización (one month
per year capped at 15 months for ≥20-worker firms / 10 months below, in
monthly installments, IGSS-offset) and the *fuerza mayor* (force majeure)
band of two days' to four months' salary; the Art. 87 end-of-contract
certificate (*finiquito* seed) with its mandatory data set; and the R33/R37
NEGATIVE invariants — NO *auxilio de cesantía*, NO doubled indemnización,
NO employer-side preaviso.

It does **not** cover: the salario / salario completo model and pay-basis
taxonomy (`01_ct-salary-model.md` — its GT-PAY-FR-005 salario-completo
integration basis, GT-PAY-FR-013 no-interest rule, GT-PAY-FR-010/FR-011
garnishment ladder, GT-PAY-FR-016 privileged credits, GT-PAY-FR-020
prescription clocks and GT-PAY-FR-022 intermediario solidarity are consumed
by id, never restated); jornada, week structure and the day-counting surface
(`02_working-time-overtime.md` — its GT-PAY-FR-040 week/day configuration
keys the Art. 77 f) absence counting); the salario mínimo chassis
(`03_minimum-wage.md`); statutory bonuses — bono 14, incentivo and the
corpus-absent December aguinaldo (`04_statutory-bonuses.md` — its
GT-PAY-FR-081 termination proration, GT-PAY-FR-082 bono-14 6/12 inclusion
feed, GT-PAY-FR-090 incentivo exclusion and GT-PAY-FR-095 aguinaldo-absence
negative FR are consumed by id); vacaciones and maternidad terminations
(`05_vacaciones-maternidad.md` — its GT-PAY-FR-106 termination proration
lands on this file's settlement surface); IGSS contribution and pension
mechanics (`07_igss-contributions.md`, by filename — the actuarial pension
data source for the Art. 82 e) offsets); IRTRA/INTECAP charges
(`08_irtra-intecap.md`); ISR/IVA interfaces (`09_isr-iva-interfaces.md` —
the exemption/deductibility feeds GT-TAX-FR-117/146/169 are consumed by id
only); or sanction values (owned by
`gt/requirements/taxation/06_ct-procedures.md` — the Art. 159 2×
domicile-work sanction is recorded here as a myth-rejection NOTE only,
never implemented).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **CT labor
LBs cite 32_ as "CT art. N (texto según edición conmemorativa 2024,
MinTrabajo)" — no "current through" date claimable** (commemorative
MinTrabajo print of indeterminate consolidation cutoff: latest printed
annotation D18-2001 with demonstrably later unannotated content —
GOQ-70/71; the qualifier carried on every CT row below IS the R44
mitigation; no dated-consolidation claim is ever made). **Rejected myths
never implemented (R33/R37):** no *auxilio de cesantía* (phrase
zero-occurrence in the whole CT), no doubled unjust-dismissal indemnización
(the only 2× anywhere = the art. 159 domicilio sanction — myth-rejection
note), and preaviso is the WORKER's obligation, never the employer's.
Evidence-elision completions (precedent of `02_working-time-overtime.md`):
the EVID-269 Art. 25 taxonomy / Art. 26 ¶¶2-3 / Art. 23, the Art. 82 d)
nullity clause, the Art. 83 final-¶ b)-extension and the Art. 87
optional-block verbatims are completed verbatim from the source txt layer
(`gt/.extractions/32_Codigo_Trabajo_D1441.pdf.txt`, spacing artifacts
normalized) — marked "(completed verbatim from the source txt layer)" in
the rows.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT arts. 25 y 26 (texto según edición conmemorativa 2024, MinTrabajo), art. 25: "a) Por tiempo indefinido, cuando no se especifica fecha para su terminación. b) A plazo fijo, cuando se especifica fecha para su terminación o cuando se ha previsto el acaecimiento de algún hecho o circunstancia como la conclusión de una obra, que forzosamente ha de poner término a la relación de trabajo…; y c) Para obra determinada, cuando se ajusta globalmente o en forma alzada el precio de los servicios…" / art. 26: "Todo contrato individual de trabajo debe tenerse por celebrado por tiempo indefinido, salvo prueba o estipulación lícita y expresa en contrario." / "Deben tenerse siempre como contratos a plazo indefinido… si al vencimiento… subsiste la causa que les dio origen" / "En consecuencia, los contratos a plazo fijo y para obra determinada tienen carácter de excepción y sólo pueden celebrarse en los casos que así lo exija la naturaleza accidental o temporal del servicio que se va a prestar o de la obra que se va a ejecutar." (¶¶2-3 completed verbatim from the source txt layer) | Art. 25: contract classes — indefinite (no termination date specified), fixed-term (date or necessarily-terminating event specified; for the event case the worker's activity itself, not the work result, is the contract object), specific-work (globally/lump-sum priced services start-to-finish, taking the result — the obra — into account); Art. 26: every contract is presumed INDEFINITE absent licit express proof or stipulation otherwise; fixed-term/specific-work contracts in permanent-or-continued-activity enterprises always count as indefinite when the cause subsists at expiry; the exception classes are valid only where the accidental or temporal nature of the service or work demands it | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Arts. 25-26 p.24 (EVID-269) |
| LB-002 | CT art. 18 (texto según edición conmemorativa 2024, MinTrabajo): "Contrato individual de trabajo, sea cual fuere su denominación, es el vínculo económico-jurídico mediante el que una persona (trabajador), queda obligada a prestar a otra (patrono), sus servicios personales o a ejecutarle una obra, personalmente, bajo la dependencia continuada y dirección inmediata o delegada de esta última, a cambio de una retribución de cualquier clase o forma." | An individual employment contract, whatever its denomination, is the economic-juridical bond by which a person (worker) is obliged to render another (employer) personal services or execute a work for him, personally, under the continued dependence and immediate or delegated direction of the latter, in exchange for retribution of any kind or form — the relationship-recognition basis regardless of the contract's label | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 18 p.23 (EVID-269) |
| LB-003 | CT art. 23 (texto según edición conmemorativa 2024, MinTrabajo): "La sustitución del patrono no afecta los contratos de trabajo existentes, en perjuicio del trabajador. El patrono sustituido queda solidariamente obligado con el nuevo patrono por las obligaciones derivadas de los contratos o de las disposiciones legales, nacidas antes de la fecha de la sustitución y hasta por el término de seis meses." (completed verbatim from the source txt layer) | Employer substitution does not prejudice existing employment contracts; the substituted employer remains solidarily (jointly and severally) liable with the new employer for obligations arising from the contracts or the law BEFORE the substitution date, for a term of SIX MONTHS — after which liability subsists only for the new employer | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 23 pp.24-25 (EVID-269) |
| LB-004 | CT art. 81 (texto según edición conmemorativa 2024, MinTrabajo): "En todo contrato por tiempo indeterminado los dos primeros meses se reputan de prueba, salvo que por mutua conveniencia las partes pacten un período de menor." / "Durante el período de prueba cualquiera de las partes puede ponerle término al contrato, por su propia voluntad, con justa causa o sin ella, sin incurrir en responsabilidad alguna." / "Se prohibe la simulación del período de prueba…" | In every indefinite contract the FIRST TWO MONTHS are deemed probation, unless the parties mutually pact a shorter period; during probation EITHER party may end the contract at will, with or without just cause, incurring NO liability whatsoever; simulation of the probation period (to evade recognition of indefinite-contract rights) is prohibited | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 81 p.49 (EVID-270) |
| LB-005 | CT art. 77 (texto según edición conmemorativa 2024, MinTrabajo): "Son causas justas que facultan al patrono para dar por terminado el contrato de trabajo, sin responsabilidad de su parte:" / f) "Cuando el trabajador deje de asistir al trabajo sin permiso del patrono o sin causa justificada, durante dos días laborales completos y consecutivos o durante seis medios días laborales en un mismo mes calendario." / h) "Cuando infrinja cualquiera de las prohibiciones del artículo 64, o del reglamento interior de trabajo debidamente aprobado, después de que el patrono lo aperciba una vez por escrito. No será necesario el apercibimiento en el caso de embriaguez cuando…" / k) "Cuando el trabajador incurra en cualquier otra falta grave…" | Art. 77: just causes empowering the employer to terminate without responsibility — f) the worker's absence from work without employer permission or justified cause during TWO COMPLETE CONSECUTIVE WORKING DAYS or SIX HALF WORKING DAYS in one calendar month; h) breach of the art. 64 prohibitions or the duly approved interior work regulation, AFTER one written warning (apercibimiento) by the employer — the warning being unnecessary for drunkenness cases as printed; k) any other grave fault by the worker (catalogue head + payroll-adjacent letters f/h/k) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 77 pp.46-47 (EVID-271) |
| LB-006 | CT art. 78 (texto según edición conmemorativa 2024, MinTrabajo): "La terminación del contrato de trabajo conforme a una o varías de las causas enumeradas en el artículo anterior, surte efectos desde que el patrono lo comunique por escrito al trabajador indicándole la causa del despido y éste cese efectivamente en sus labores, pero el trabajador goza del derecho de emplazar al patrono… con el objeto de que pruebe la justa causa… Si el patrono no prueba dicha causa, debe pagar al trabajador: a) Las indemnizaciones que según este Código le pueda corresponder; y b) A título de daños y perjuicios, los salarios que el trabajador ha dejado de percibir desde el momento del despido hasta el pago de su indemnización, hasta un máximo de doce (12) meses de salario y las costas judiciales." | Termination under an Art. 77 cause takes effect when the employer COMMUNICATES IT IN WRITING stating the dismissal cause and the worker effectively ceases work; the worker may summon the employer before the labor courts to PROVE the just cause — if the employer fails to prove it he must pay: (a) the indemnities this Code grants, and (b) as damages, the SALARIES THE WORKER STOPPED RECEIVING from dismissal until payment of the indemnización, up to a maximum of TWELVE (12) MONTHS of salary, plus judicial costs | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 78 pp.47-48 (EVID-272) |
| LB-007 | CT art. 79 a) (texto según edición conmemorativa 2024, MinTrabajo): "Cuando el patrono no le pague el salario completo que le corresponda, en la fecha y lugar convenidos o acostumbrados. Quedan a salvo las deducciones autorizadas por la ley;" | Just cause empowering the WORKER to terminate without responsibility: when the employer fails to pay the COMPLETE salary corresponding to the worker at the agreed or customary date and place — lawful deductions saved — the indirect-dismissal trigger (non-/under-/late payment opens the full Art. 82 indemnización via the Art. 82 head) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 79 a) p.48 (EVID-273) |
| LB-008 | CT art. 80 (texto según edición conmemorativa 2024, MinTrabajo): "…Si el patrono prueba… que abandonó sus labores sin justa causa, en los casos de contratos por tiempo indefinido, debe el trabajador pagarle el importe del preaviso y los daños y perjuicios… y si se trata de contratos a plazo fijo o para obra determinada, el trabajador debe satisfacer las prestaciones que indica el artículo 84." | If the employer PROVES that the worker abandoned the work without just cause: for indefinite contracts the worker must pay the employer the PREAVISO amount and the damages; for fixed-term or specific-work contracts the worker must satisfy the Art. 84 prestaciones (the worker-side mirror of the early-termination floor) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 80 p.49 (EVID-273) |
| LB-009 | CT art. 82 head, b), c) y d) (texto según edición conmemorativa 2024, MinTrabajo), head: "Si el contrato de trabajo por tiempo indeterminado concluye una vez transcurrido el período de prueba, por razón de despido injustificado del trabajador, o por alguna de las causas previstas en el artículo 79, el patrono debe pagar a éste una indemnización por tiempo servido equivalente a un mes de salario por cada año de servicio continuos y si los servicios no alcanzan a un año, en forma proporcional al plazo trabajado." / b) "Su importe debe calcularse tomando como base el promedio de los salarios devengados por el trabajador durante los últimos seis meses que tengan de vigencia el contrato o el tiempo que haya trabajado, si no se ha ajustado dicho término;" / c): continuity not interrupted "por enfermedad, vacaciones, licencias, huelga legal u otras causas análogas… suspenden y no terminan el contrato" / d) "Es nula ipso jure la cláusula del contrato que tienda a interrumpir la continuidad de los servicios prestados o por prestarse;" (d) completed verbatim from the source txt layer) | Art. 82: when an indefinite contract ends after probation by UNJUSTIFIED DISMISSAL or an Art. 79 (indirect-dismissal) cause, the employer owes severance for time served = ONE MONTH OF SALARY PER YEAR of continuous service, prorated to time worked when under a year (NO maximum anywhere in the article); b) the amount computes on the AVERAGE OF SALARIES EARNED DURING THE LAST SIX MONTHS of contract validity — or the time worked if shorter; c) continuity is NOT interrupted by illness, vacations, licenses, legal strike or other analogous suspending causes; d) any clause tending to interrupt the continuity of services rendered or to be rendered is NULL IPSO JURE | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 82 pp.49-51 (EVID-274) |
| LB-010 | CT art. 82 a) y e) (texto según edición conmemorativa 2024, MinTrabajo), a): "Su importe no puede ser objeto de compensación, venta o cesión, ni puede ser embargado, salvo en los términos del artículo 97;" / e): dismissal for "enfermedad o invalidez permanente o vejez" owes no indemnización "siempre que… quede devengando… una pensión… cuyo valor actuarial sea equivalente o mayor" — if the IGSS pension is lesser, "el patrono queda obligado únicamente a cubrirle la diferencia" / the worker retiring for those causes without IGSS protection gets "el cincuenta por ciento (50%) de la indemnización prevista en este artículo" | a) The severance amount cannot be compensated, sold or ceded, nor garnished, save in the terms of art. 97 (the inembargability/privilege interface); e) an employer dismissing for illness, permanent invalidity or old age owes NOTHING while the IGSS-protected worker draws, from cessation, a pension whose ACTUARIAL value equals or exceeds the severance — a lesser pension obliges the employer to cover only the DIFFERENCE; a worker retiring for those causes WITHOUT IGSS protection is owed FIFTY PERCENT (50%) of the Art. 82 severance (difference-completion when an IGSS pension is actuarially lesser) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 82 a)/e) pp.49-51 (EVID-274) |
| LB-011 | CT art. 83 (texto según edición conmemorativa 2024, MinTrabajo): "El trabajador que desee dar por concluido su contrato por tiempo indeterminado sin justa causa o atendiendo únicamente a su propia voluntad y una vez que haya transcurrido el período de prueba debe dar aviso previo al patrono… o en su defecto de conformidad con las siguientes reglas: a) Antes de ajustar seis meses de servicios continuos, con una semana de anticipación por lo menos; b) Después de seis meses de ser vicios [sic] continuos pero menos de un año, con diez, días [sic] de anticipación por lo menos; c) Después de un año de ser vicios [sic] continuos pero menos de cinco años, con dos semanas de anticipación por lo menos; y d) Después de cinco años de servicios continuos, con un mes de anticipación por lo menos." / "…no pueden ser compensados pagando el trabajador al patrono una cantidad igual al salario actual correspondiente a las expresadas plazos, salvo que este último lo consienta" / "Son aplicables al preaviso las reglas de los incisos c) y d) del artículo 82." / "Igualmente lo es la del inciso b) del mismo texto legal, en todos aquellos casos en que proceda calcular el importe en dinero del plazo respectivo." (final sentence completed verbatim from the source txt layer; the txt layer prints "plazas" where the evidence layer prints "plazos" — recorded, the evidence text is carried) | The WORKER who wishes to end an indefinite contract without just cause, on his own will alone, once probation has run, must give the employer ADVANCE NOTICE per the contract's express stipulation or, failing that, the scale: (a) before six months of continuous service — at least ONE WEEK; (b) six months to one year — at least TEN DAYS; (c) one to five years — at least TWO WEEKS; (d) after five years — at least ONE MONTH; the notices are NOT COMPENSABLE by paying the employer an amount equal to the current salary of the stated periods UNLESS THE EMPLOYER CONSENTS; the Art. 82 c)/d) continuity rules apply to preaviso, as does Art. 82 b) (the last-6-months average) whenever the money value of the notice period must be computed — preaviso is the worker's obligation (R37: no employer-side preaviso duty exists) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 83 p.50 (EVID-275) |
| LB-012 | CT art. 84 (texto según edición conmemorativa 2024, MinTrabajo): "En los contratos a plazo fijo y para ejecución de obra determinada, cada una de las partes puede ponerles término, sin justa causa, antes del advenimiento del plazo o de la conclusión de la obra, pagando a la otra los daños y perjuicios correspondientes…" / "Si la terminación prematura del contrato ha sido decretada por el patrono, los daños y perjuicios que éste debe de pagar al trabajador, no pueden ser inferiores a un día de salario por cada mes de trabajo continuo ejecutado, o fracción de tiempo menor, si no se ha ajustado dicho término." / "Este mínimo… debe ser satisfecho en el momento mismo de la cesación del contrato…" | In fixed-term and specific-work contracts either party may terminate without just cause before the term arrives or the work concludes, paying the other the corresponding damages (assessed by a labor inspector, or the labor courts once in litigation); when the EMPLOYER decrees the early termination, his damages to the worker CANNOT BE LESS THAN ONE DAY OF SALARY PER MONTH of continuous work executed (or the lesser fraction if a month is not completed); this minimum must be satisfied AT THE VERY MOMENT of cessation (and is deductible from greater damages later determined) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 84 pp.50-51 (EVID-276) |
| LB-013 | CT art. 85 (texto según edición conmemorativa 2024, MinTrabajo), a) muerte: "la obligación del patrono es la de cubrir a dichos dependientes el importe de un mes de salario por cada año de servicios prestados, hasta el límite máximo de quince meses, si se tratare de empresas con veinte o más trabajadores, y de diez meses si fueren empresas con menos de veinte trabajadores. Dicha indemnización deba [sic] cubrirla el patrono en mensualidades equivalentes al monto del salario…" (IGSS benefits offset up to the difference) / b) fuerza mayor/caso fortuito, insolvencia, quiebra, incapacidad o muerte del patrono: obligations "sin que en ningún caso éstas puedan ser menores del importe de dos días de salario, ni mayores de cuatro meses de salario, por cada trabajador" / "si la insolvencia o quiebra se declara culpable o fraudulenta, se deben aplicar las reglas de los artículos 82 y 84…" | a) Death of the worker: absent IGSS protection (or dependents lacking IGSS benefit rights), the employer owes the economic dependents ONE MONTH OF SALARY PER YEAR of services, capped at FIFTEEN MONTHS for enterprises with twenty or more workers and TEN MONTHS below twenty, payable in MONTHLY INSTALLMENTS equivalent to the salary the worker earned; inferior IGSS death benefits oblige the employer only to cover the difference; beneficiary quality is proven before the labor courts (herederos or concubina as printed); b) force majeure/act of God, insolvency, bankruptcy, incapacity or death of the employer terminates without worker liability, the Inspection/Tribunals graduating the despido obligations DISCRETIONARILY but never below TWO DAYS' SALARY nor above FOUR MONTHS' SALARY per worker (economic capacity and contract duration weighed); culpable or fraudulent insolvency/bankruptcy reverts to the Arts. 82/84 rules when they yield greater prestaciones | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 85 pp.51-52 (EVID-277) |
| LB-014 | CT art. 87 (texto según edición conmemorativa 2024, MinTrabajo): "A la expiración de todo contrato de trabajo, por cualquier causa que éste termine, el patrono debe dar al trabajador un documento que exprese únicamente: a) La fecha de su entrada y de su salida; b) La clase de trabajo ejecutado; y c) El salario ordinario y extraordinario devengado durante el último período del pago." / "Si el trabajador lo desea, el certificado debe determinar también: a) La manera como trabajó; y b) La causa o causas de la terminación del contrato." (optional block completed verbatim from the source txt layer) | Upon expiry of EVERY employment contract whatever the termination cause, the employer must give the worker a document stating ONLY: (a) the entry and exit dates; (b) the class of work executed; and (c) the ORDINARY AND EXTRAORDINARY salary earned during the last pay period; if the worker so wishes, the certificate must also state the manner in which he worked and the termination cause(s) — the finiquito/constancia mandatory data set | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 87 p.52 (EVID-279) |
| LB-015 | NEGATIVE FINDING, CT whole text (texto según edición conmemorativa 2024, MinTrabajo): the phrase "auxilio de cesantía" has ZERO occurrences in the text; the only doubling provision = art. 159 (trabajo a domicilio): "El patrono que infrinja esta disposición debe ser sentenciado a pagar una indemnización a cada uno de los trabajadores, equivalente al doble de los salarios que haya dejado de percibir." | No cesantía scale and no double indemnity for unjust dismissal exist anywhere in this Code; termination money = art. 82 indemnización (1 month/year, uncapped, 6-month salario-completo average, IGSS offsets) + art. 78 b) salarios caídos (≤12 months) + art. 83 preaviso (worker-side) + art. 84 plazo-fijo floor + art. 85 death/fuerza-mayor scales; the ONLY 2× multiplier in the entire Code is the art. 159 domicile-work underpayment sanction (a sanction for trabajo a domicilio — never a payroll severance rule) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Whole text (searched); art. 159 pp.77-78 (EVID-278) |

Dead print / myth notes — never implementable (LB notes, not FRs): the
art. 159 2× sanction belongs to the trabajo-a-domicilio regime and is a
judicially-sentenced sanction, not a severance multiplier — recorded as the
R33 myth-rejection note proving the doubling rejection (LB-015). The art. 83
print defects ("diez, días", "ser vicios" for servicios) and the
"plazos/plazas" evidence-vs-txt variance are carried as [sic]/notes, never
corrected into law text (§7 note 3). Edition vintage (R44/GOQ-70/71): the
32_ source is the MinTrabajo commemorative 2024 print with an
indeterminate consolidation cutoff — cited only with the edition qualifier,
never as a dated consolidation.

Version regime (D12): NO dated data is owned by this file — every value
cited here (2 months, 2 días/6 medios días, 12 months, 6 months, 1
month/year, 50%, 6-month solidarity window, 1 week/10 days/2 weeks/1
month, 1 day/month, 15/10 months, 2 días/4 months) is STATIC law (CT
arts. 23, 25-26, 77-85, 87). The only dated inputs consumed externally are
the company headcount snapshot (art. 85 cap selection — as-of-event-date
configuration data) and the IGSS actuarial pension values (file 07, by
filename).

## 3. Functional Requirements

### 3.1 Contract taxonomy, substitution and probation (CT Arts. 18, 23, 25-26, 81)

- **GT-PAY-FR-127:** The system shall classify every employment
  relationship (recognized per the art. 18 bond — personal services under
  continued dependence and immediate/delegated direction for retribution,
  *sea cual fuere su denominación* — whatever the contract's label) into
  exactly one class of the Art. 25 taxonomy — *indefinido* (indefinite),
  *plazo fijo* (fixed-term) or *obra determinada* (specific work) — and
  shall enforce the Art. 26 INDEFINITE PRESUMPTION as a validation gate:
  every contract defaults to indefinite; a plazo fijo / obra determinada
  classification is admitted ONLY with licit EXPRESS stipulation or proof,
  backed by a recorded service nature that is accidental or temporal (the
  exception character of Art. 26 ¶3); and a plazo/obra contract in an
  enterprise of permanent-or-continued activity whose generating cause
  subsists at term expiry CONVERTS to indefinite (the conversion date
  recorded on the contract). The class routes every termination outcome of
  FR-129..FR-152: only indefinite contracts open the Art. 82 indemnización
  (FR-135); valid plazo/obra contracts route early termination to the
  Art. 84 floor (FR-146). (LB-001; LB-002; EVID-269)
- **GT-PAY-FR-128:** The system shall model *sustitución del patrono*
  (employer substitution) for payroll-liability continuity: existing
  contracts are unaffected; the SUBSTITUTED employer remains solidarily
  liable with the new employer for obligations born before the
  substitution date for a term of SIX MONTHS from that date — after the
  window, liability subsists only for the new employer. Substitution
  records carry the pair (substituted patrono, new patrono), the
  substitution date and the computed window end; the solidarity flag pair
  is the same surface as `01_ct-salary-model.md` GT-PAY-FR-022
  (intermediario solidarity — consumed by id, never re-derived).
  (LB-003; EVID-269)
- **GT-PAY-FR-129:** The system shall implement the *período de prueba*
  (probation) of Art. 81 as a termination-liability clock: for every
  indefinite contract the FIRST TWO MONTHS are deemed probation — the
  parties may mutually pact a SHORTER period (recorded), never a longer
  one; termination by either party inside the window — at will, with or
  without just cause — accrues NO termination-money liability (no Art. 82
  indemnización, no Art. 78 b) salarios caídos, no preaviso duty). The
  Art. 81 simulation ban shall be enforced as a guard: probation windows
  may not be stipulated, re-stipulated or chained with the purpose of
  evading indefinite-contract rights (a re-hire whose probation follows a
  prior probation for the same worker/services within a short horizon
  raises the guard flag; the Art. 82 d) continuity nullity of FR-138
  completes the anti-circumvention net). (LB-004; EVID-270)

### 3.2 Justa causa registry and the despido record (CT Arts. 77-78)

- **GT-PAY-FR-130:** The system shall keep an Art. 77 *justa causa*
  (just cause) registry as configuration data driving justified-dismissal
  routing: each cause row stores its letter, its evidence prerequisites
  and its validation rule — with the payroll-adjacent letters fully
  specified: f) ABSENCE THRESHOLDS — absence without permission or
  justified cause during **two complete consecutive días laborales** or
  **six medios días laborales in one calendar month**, the día-laboral
  counting keyed on the week-length/day-counting configuration of
  `02_working-time-overtime.md` GT-PAY-FR-040 (5- or 6-day semana,
  consumed by id); h) the art. 64-prohibition/reglamento-infringement
  cause requiring ONE prior WRITTEN warning (*apercibimiento*) recorded on
  the worker's file (drunkenness excepted as printed); k) the
  any-other-grave-fault catchall (judicial-gate: gravity surfaced, never
  auto-decided). A justified dismissal validated against a registry row
  pays NO Art. 82 indemnización and NO salarios caídos — subject to the
  Art. 78 proof gate of FR-131. (LB-005; EVID-271)
- **GT-PAY-FR-131:** The system shall enforce the Art. 78 form
  requirements on every Art. 77 dismissal: the termination record shall
  carry the WRITTEN communication to the worker STATING THE DISMISSAL
  CAUSE (document reference + date), and the termination takes effect
  only from that written communication plus the worker's effective
  cessation of work. The judicial proof gate shall be surfaced (never
  adjudicated): the worker's *emplazar* (summon) right to have the
  employer prove the just cause, with the prescription anchors consumed
  from `01_ct-salary-model.md` GT-PAY-FR-020 — 20 días hábiles for the
  employer's justified-dismissal right (from the cause) and 30 días
  hábiles for the worker's dismissal claim (from termination); a cause
  flagged unproven (judicial finding recorded) routes the termination to
  the FR-132 award stack. (LB-006; LB-005; EVID-272, EVID-271)
- **GT-PAY-FR-132:** The system shall compute the Art. 78 b)
  unproven-cause award stack as SEPARATE lines, never merged: (a) the
  indemnizaciones this Code grants — i.e. the Art. 82 indemnización of
  FR-135 for indefinite contracts — and (b) *salarios caídos* (lapsed
  salaries): the salaries the worker stopped receiving from the dismissal
  moment until payment of the indemnización, CAPPED at **twelve (12)
  months of salary**, plus the judicial-costs pointer (external to
  payroll). Salarios caídos compute as elapsed full months (design
  default: calendar months from effective cessation to the recorded
  indemnización payment date — §7 note 2) × the FR-136 monthly average;
  the line is a DAMAGES award, never interest (kin of
  `01_ct-salary-model.md` GT-PAY-FR-013 — the Code's only interest rule
  is the prohibition). (LB-006; EVID-272)

### 3.3 Despido indirecto and worker abandonment (CT Arts. 79-80)

- **GT-PAY-FR-133:** The system shall implement the *despido indirecto*
  (indirect dismissal) trigger of Art. 79 a): a recorded employer failure
  to pay the SALARIO COMPLETO corresponding to the worker at the agreed or
  customary date and place (non-payment, under-payment or late payment of
  the complete salary; lawful deductions saved) empowers the WORKER to
  terminate without responsibility — and such termination carries the FULL
  Art. 82 indemnización (the Art. 82 head expressly routes "las causas
  previstas en el artículo 79"). Payroll reliability is legally
  load-bearing: every missed/incomplete/late salary event shall be
  recordable as the entitlement trigger on the worker's termination
  record. (LB-007; LB-009; EVID-273, EVID-274)
- **GT-PAY-FR-134:** The system shall implement the Art. 80 abandonment
  rule as a WORKER-side liability: where the employer proves that the
  worker abandoned the work without just cause — for indefinite
  contracts,   the worker owes the employer the preaviso import (the
  FR-143/FR-144 scale and money rules) plus damages (judicially graduated
  — surfaced, not computed here); for plazo fijo / obra determinada
  contracts, the worker must satisfy the Art. 84 prestaciones (the
  FR-146 floor mirrored against the worker). No employer termination
  money arises from a proven abandonment. (LB-008; EVID-273)

### 3.4 Indemnización engine — despido injusto (CT Art. 82)

- **GT-PAY-FR-135:** The system shall compute the Art. 82 *indemnización
  por tiempo servido* (severance for time served) for INDEFINITE contracts
  (FR-127 class) concluded AFTER the probation window (FR-129) by (i)
  unjustified dismissal or (ii) an Art. 79 indirect-dismissal cause
  (FR-133) — and by nothing else — as:
  quantum = monthly_average_base (FR-136) × (years of continuous service
  + prorated fraction when service is under a year), with the
  continuous-service count running from the date the work relationship
  STARTED whatever its form. There is NO maximum cap on this quantum —
  any configured ceiling is rejected (R33 kin: caps belong to folk models
  of other jurisdictions, not this Code). (LB-009; EVID-274, EVID-278)
- **GT-PAY-FR-136:** The computation base shall be the Art. 82 b)
  average: **the promedio of the salarios devengados during the LAST SIX
  MONTHS of contract validity — or the time worked if the contract has
  not run six months** — computed on *salario completo* per CT art. 93
  (ordinary + ordinary-equivalent + extraordinary earnings), consuming
  the integration basis of `01_ct-salary-model.md` GT-PAY-FR-005 by id
  (never re-derived here): the base aggregates every ordinary-jornada and
  extraordinary-jornada earning line of the window, including overtime.
  (LB-009; EVID-274; via 01 GT-PAY-FR-005)
- **GT-PAY-FR-137:** Component feeds into the FR-136 average, consumed
  BY ID from `04_statutory-bonuses.md`, never restated: (a) BONO 14
  enters the art. 82 average at the proportion corresponding to six
  months of services, or the time worked if shorter — accrued bono 14 ×
  min(6 months, time worked)/12 — per its GT-PAY-FR-082 inclusion feed
  (D-42-92 art. 4; EVID-348 cross-ref); (b) the INCENTIVO is EXCLUDED
  from every indemnización average — its single inclusion surface is the
  séptimo-día computation — per its GT-PAY-FR-090 non-integration nature
  rule (D-78-89 art. 2); (c) the December aguinaldo is absent from the
  corpus and NEVER invented into the base (its GT-PAY-FR-095 negative FR
  governs). (LB-009; EVID-274; via 04 GT-PAY-FR-082, GT-PAY-FR-090, GT-PAY-FR-095)
- **GT-PAY-FR-138:** The system shall enforce the Art. 82 c)/d)
  continuity rules: continuity of service is NOT interrupted by
  *enfermedad, vacaciones, licencias, huelga legal* (illness, vacations,
  licenses, legal strike) or other analogous causes that SUSPEND rather
  than terminate the contract (the suspension bridges of
  `05_vacaciones-maternidad.md` feed this); and any contract clause
  tending to interrupt the continuity of services rendered or to be
  rendered is NULL IPSO JURE — re-hire chains, entity rotations or clause
  inserts may never reset the service-years count (the anti-circumvention
  counterpart of the FR-129 simulation ban). (LB-009; EVID-274)
- **GT-PAY-FR-139:** The system shall stamp the Art. 82 a) protection on
  the indemnización line: the amount cannot be object of compensación,
  venta or cesión, nor be embargoed, save in the terms of art. 97 — the
  garnishment ladder and alimony carve-out of
  `01_ct-salary-model.md` GT-PAY-FR-010/FR-011 and the first-class
  privilege metadata of its GT-PAY-FR-016 are consumed by id as the only
  lawful deduction/attachment surfaces. (LB-010; EVID-274)
- **GT-PAY-FR-140:** The system shall implement the Art. 82 e) IGSS
  actuarial offsets: for a dismissal by cause of *enfermedad, invalidez
  permanente o vejez* (illness, permanent invalidity or old age), NO
  indemnización is owed while the worker — protected by the correlativa
  IGSS benefits — draws, from the very moment of cessation, a pension
  whose ACTUARIAL value is equivalent to or greater than the
  indemnización; where the IGSS pension is actuarially LESSER, the
  employer is obliged to cover only the DIFFERENCE. The pension type,
  amount and actuarial valuation are EXTERNAL data consumed from
  `07_igss-contributions.md` (by filename — the IGSS data source; the
  expectativa-de-vida determination is the Institute's, never computed
  here). (LB-010; EVID-274)
- **GT-PAY-FR-141:** The system shall implement the Art. 82 50% rule:
  a worker who, by permanent illness or invalidity or by old age, becomes
  unable to continue in the position and RETIRES for those causes
  (justification previously recorded) is owed **fifty percent (50%) of
  the Art. 82 indemnización** when he does NOT enjoy the correlativa
  IGSS benefits; if he enjoys them but the IGSS recognizes only a pension
  actuarially lesser than that 50% quantum, the employer covers only the
  difference to complete it; a pension superior or equal discharges the
  employer entirely. (LB-010; EVID-274)
- **GT-PAY-FR-142:** ISR treatment is a FEED consumed by id, never
  re-derived here: the indemnización por tiempo servido is fully exempt —
  `gt/requirements/taxation/04_isr-trabajo.md` GT-TAX-FR-117 (with the
  death/incapacity indemnities and social-security pensions of the same
  row) — and the employer-side deductibility interfaces are
  GT-TAX-FR-146 (indemnizaciones deduction capped at 8.33% of annual
  remunerations; retention↔deduction dependency) and GT-TAX-FR-169
  (Criterio 6-2018 planilla-gate backing for expense documentation); NO
  exemption split, retention arithmetic or deductibility computation
  lives in this file. (LB-009; EVID-274; external feed ids only)

### 3.5 Preaviso — the WORKER's notice obligation (CT Art. 83) [R37]

- **GT-PAY-FR-143:** The system shall store and apply the Art. 83
  *preaviso* (advance-notice) scale as a WORKER obligation — R37: never
  an employer duty — for a worker ending an indefinite contract without
  justa causa, on his own will alone, after probation has run: notice per
  the contract's express stipulation where one exists, otherwise the
  statutory bands — before six months of continuous service: **one week**;
  six months to under one year: **ten days**; one year to under five
  years: **two weeks**; after five years of continuous service: **one
  month** (minimum anticipation in each band). The notice is given in
  WRITING (a verbal contract's worker may give it verbally before two
  witnesses — recorded); the band reads continuous service under the
  FR-138 continuity rules (Art. 82 c)/d) apply to preaviso by express
  extension). (LB-011; EVID-275)
- **GT-PAY-FR-144:** The system shall enforce the Art. 83 money rules:
  preaviso is NOT compensable by the worker paying an amount equal to the
  current salary of the corresponding period, EXCEPT with the EMPLOYER'S
  CONSENT — a money-in-lieu line is emitted only on a recorded consent
  flag; when the money value of the notice period is computed (consented
  substitution, or the FR-134 abandonment liability), it uses the Art. 82
  b) base (the FR-136 last-6-months salario-completo average) by express
  extension; and once the worker has given notice, the employer may order
  immediate cessation — having found a substitute or for any other motive
  — WITHOUT incurring responsibility (a recorded post-notice cessation
  order closes the relation liability-free from that date; it is a
  reaction to the worker's notice, never an employer preaviso duty).
  (LB-011; LB-009; EVID-275)
- **GT-PAY-FR-145:** NEGATIVE FR (R37 citation guard): NO employer-side
  preaviso duty exists anywhere in the CT — the employer's termination
  money is exclusively the Art. 78 b) salarios caídos, the Art. 82
  indemnización, the Art. 84 floor and the Art. 85 scales; any
  employer-paid notice/severance-notice line, accrual or provision citing
  the CT is rejected as a validation error (the folk "employer preaviso"
  model of other jurisdictions fails here). (LB-011; LB-015; EVID-275, EVID-278)

### 3.6 Plazo fijo / obra early termination (CT Art. 84)

- **GT-PAY-FR-146:** The system shall compute the Art. 84
  early-termination damages floor for VALID plazo fijo / obra determinada
  contracts (FR-127 gate passed) ended by the EMPLOYER without just cause
  before the term arrives or the work concludes: damages ≥ **one día de
  salario per month of continuous work executed** — or the lesser
  fraction when a month is not completed — computed as
  daily_salary × months worked (+ fraction); the floor is satisfied AT THE
  VERY MOMENT of cessation (same-day payment line on the termination
  settlement) and is DEDUCTIBLE from the greater damages an inspector or
  the labor tribunals later determine (the ceiling is judicial —
  surfaced as a graduation record, never auto-computed). The
  daily-salary derivation is corpus-silent and ships as the §7 note 1
  design default (FR-136 average ÷ 30). Worker-side mirror: the FR-134
  abandonment liability of plazo/obra workers. (LB-012; EVID-276)

### 3.7 Death and fuerza mayor terminations (CT Art. 85)

- **GT-PAY-FR-147:** The system shall compute the Art. 85 a)
  death-of-worker indemnización: where the worker lacked IGSS protection
  at death (or the economic dependents lack IGSS benefit rights), the
  employer owes the DEPENDENTS one month of salary per year of services
  — capped at **fifteen months** for enterprises with twenty or more
  workers, **ten months** for enterprises with fewer than twenty
  (headcount = company configuration data read as of the death date —
  §7 note 5) — payable in MONTHLY INSTALLMENTS equivalent to the salary
  the worker earned (installment = the FR-136 monthly average); IGSS
  death benefits INFERIOR to the rule oblige the employer only to cover
  the difference (offset data from `07_igss-contributions.md`, by
  filename). The beneficiary census (herederos / concubina as printed)
  is judicially determined — surfaced as a gate field, never computed.
  (LB-013; EVID-277)
- **GT-PAY-FR-148:** The system shall record the Art. 85 b) *fuerza
  mayor* terminations — force majeure / act of God, insolvency, judicial
  or extrajudicial bankruptcy/liquidation of the enterprise, incapacity
  or death of the employer, when the facts produce the absolute
  impossibility of performance — as liability-band data: the Inspection
  or labor tribunals graduate the despido obligations DISCRETIONARILY
  (economic capacity of the enterprise weighed with each contract's
  duration) within the statutory band — never below **two días de
  salario** nor above **four months of salary** per worker; a CULPABLE
  or FRAUDULENT insolvency/bankruptcy declaration escalates to the
  Arts. 82/84 rules whenever they yield greater prestaciones (the
  escalation re-routes to FR-135/FR-146). The graduation value itself is
  a judicial/administrative act — surfaced, never auto-computed.
  (LB-013; EVID-277)

### 3.8 Finiquito certificate (CT Art. 87)

- **GT-PAY-FR-149:** The system shall generate, on expiry of EVERY
  employment contract whatever the termination cause, the Art. 87
  certificate document with the MANDATORY data set — and NOTHING else by
  default: (a) the worker's entry and exit dates; (b) the class of work
  executed; (c) the ordinary AND extraordinary salary earned during the
  last pay period — generated from the departure record and the last
  payslip; the OPTIONAL blocks (the manner in which the worker worked;
  the termination cause(s)) are emitted ONLY on a recorded worker
  request. The document is the finiquito seed; it is distinct from any
  ISR retention constancia (taxation-owned) and from the vacation record
  of `05_vacaciones-maternidad.md` GT-PAY-FR-110 (different duties,
  never merged). (LB-014; EVID-279)

### 3.9 Termination settlement assembly

- **GT-PAY-FR-150:** The system shall assemble the termination
  settlement as the single surface where every termination-driven line
  wires in BY ID, never restated: (a) the Art. 82 indemnización
  (FR-135..FR-141, with its IGSS offset state); (b) the salarios caídos
  award (FR-132); (c) the Art. 84 floor for valid plazo/obra contracts
  (FR-146); (d) the Art. 85 death scale (FR-147) or fuerza-mayor
  graduation record (FR-148); (e) the worker-side preaviso liability
  (FR-134/FR-143/FR-144 — a worker-payable, emitted only on the consent
  or proof flags); (f) the vacation termination proration of
  `05_vacaciones-maternidad.md` GT-PAY-FR-106 (mechanics owned there);
  (g) the bono 14 termination proration of `04_statutory-bonuses.md`
  GT-PAY-FR-081 (mechanics owned there); and the run emits the FR-149
  certificate, stamping the ISR exemption flag from GT-TAX-FR-117 (feed
  only). Probation-window exits (FR-129), proven justa-causa dismissals
  (FR-130/FR-131) and plazo-advenimiento/mutuo-consent terminations
  (Art. 86) pay no severance lines — only the by-id prorations and the
  certificate. (LB-006; LB-009; LB-011; LB-012; LB-013; LB-014; EVID-272,
  EVID-274, EVID-275, EVID-276, EVID-277, EVID-279)

### 3.10 NEGATIVE invariants (R33 — myth rejections)

- **GT-PAY-FR-151:** NEGATIVE FR (R33 citation guard): NO *auxilio de
  cesantía* exists — the phrase has ZERO occurrences in the CT text — and
  no cesantía concept, scale, accrual, reserve or payment line may exist
  in any GT payroll surface citing the CT; termination money is
  EXCLUSIVELY the Art. 82 indemnización + the Art. 78 b) salarios caídos
  + the Arts. 83/84/85 rules of this file. Any cesantía row imported
  from another jurisdiction's model is rejected as a validation error.
  (LB-015; EVID-278)
- **GT-PAY-FR-152:** NEGATIVE FR (R33 citation guard): NO doubled
  indemnización — no 2× (or any multiple) of the unjust-dismissal
  indemnización exists anywhere in the Code; the ONLY 2× provision in
  the entire CT is the Art. 159 trabajo-a-domicilio underpayment
  sanction ("el doble de los salarios que haya dejado de percibir"),
  recorded here as a MYTH-REJECTION NOTE only — a judicially-sentenced
  sanction of the domicilio regime, never a payroll severance rule, and
  never implemented in this file (sanction surfaces are taxation/06
  territory). Any doubling multiplier applied to an Art. 82 quantum is
  rejected. (LB-015; EVID-278)

## 4. Data Model

Layer semantics: payroll is Odoo-native for computation, registries and
documents; the statutory scales/clocks of this file (probation window,
solidarity window, absence thresholds, preaviso bands, death caps, fuerza
mayor band, negative guards) are `shared` contract items both sides must
resolve identically. No sidecar lives next to this file; the only dated
inputs consumed externally are the company headcount snapshot (FR-147) and
the IGSS actuarial pension data (FR-140/FR-147 — file 07, by filename).

**Contract taxonomy, substitution, probation:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | gt_pay_contract_class | select | indefinido · plazo_fijo · obra_determinada (art. 25) | FR-127 |
| hr.contract (plazo/obra) | gt_pay_service_nature · gt_pay_stipulation_express | select/boolean | accidental · temporal · permanente (permanente + plazo/obra → validation error, class defaults indefinite); conversion flag when cause subsists at expiry (art. 26) | FR-127 |
| hr.contract | gt_pay_substitution_pair · gt_pay_substitution_date · gt_pay_solidarity_until | m2o pair / date / date (computed) | substituted + new patrono; window end = substitution date + 6 months | FR-128 |
| hr.contract | gt_pay_probation_end · gt_pay_probation_shorter_pact | date (computed) / boolean | default = start + 2 months; mutually-pacted shorter window recorded; longer pacts rejected; simulation guard flag on re-stipulated probations | FR-129 |

**Justa causa registry and despido record:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.justa.causa (config) | letter · rule · evidence_prereqs | char / selection / json | art. 77 catalogue rows; f) = 2 días laborales completos consecutivos / 6 medios días in one calendar month (counting keyed on 02 GT-PAY-FR-040 week surface); h) = written apercibimiento prerequisite (drunkenness excepted); k) = grave fault, judicial gate | FR-130 |
| hr.employee | gt_pay_absence_counters | integer (computed) | consecutive-full-labor-day streak · half-day count per calendar month (unpermissioned/unjustified absences only) | FR-130 |
| hr.departure | gt_pay_causa_written_doc · gt_pay_causa_letter · gt_pay_written_comm_date · gt_pay_effective_cessation | char ref / m2o / date / date | art. 78 written-cause communication record; effects from communication + cessation | FR-131 |
| hr.departure | gt_pay_causa_proven · gt_pay_proof_gate | boolean / gate | judicial proof outcome (emplazar right surfaced); unproven → FR-132 stack | FR-131 |
| l10n_gt.pay.salarios.caidos (new) | from_date · to_date · months_elapsed · monthly_rate · cap_months | date / date / int / monetary / const 12 | months × FR-136 average; 12-month cap; never an interest line | FR-132 |

**Indemnización engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.indemnizacion (new) | eligibility_route | select | unjustified_dismissal · indirect_art79 (indefinite contracts, post-probation, only these) | FR-135, FR-133 |
| l10n_gt.pay.indemnizacion | years_continuous · fraction · quantum | numeric (computed) | 1 month/year + prorated fraction; NO cap field exists (config ceilings rejected) | FR-135 |
| l10n_gt.pay.indemnizacion | base_window · monthly_avg_base | selection / monetary (computed) | last 6 months of contract validity (or full shorter tenure); salario completo aggregation via 01 GT-PAY-FR-005 | FR-136 |
| l10n_gt.pay.indemnizacion | bono14_feed · incentivo_excluded | monetary / flag | bono 14 at min(6m, time)/12 via 04 GT-PAY-FR-082; incentivo out per 04 GT-PAY-FR-090; aguinaldo never invented (04 GT-PAY-FR-095) | FR-137 |
| l10n_gt.pay.indemnizacion | continuity_bridges · nullity_guard | boolean (computed) | suspension periods bridge service; continuity-interrupting clauses null ipso jure; count from relation start | FR-138 |
| hr.payslip.line (indemnización) | gt_pay_no_compensation_no_cesion · unembargable | stamped flags | art. 82 a) protection; deductions only via 01 GT-PAY-FR-010/011 ladder; privilege tag 01 GT-PAY-FR-016 | FR-139 |
| l10n_gt.pay.indemnizacion | igss_pension_type · pension_actuarial_value · offset_state | select / monetary (external, file 07) / computed | none_due (actuarial ≥ quantum) · difference_only (lesser) | FR-140 |
| l10n_gt.pay.indemnizacion | retirement_case · fifty_pct_quantum · justification_record | boolean / monetary (computed) / char ref | 50% of indemnización without IGSS protection; difference-completion with lesser IGSS pension | FR-141 |
| hr.payslip.line (indemnización) | isr_exemption_flag | stamped (external feed) | GT-TAX-FR-117 fully exempt — feed only; deductibility interfaces GT-TAX-FR-146/169 external | FR-142 |

**Preaviso (worker-side), plazo fijo floor, art. 85 scales, finiquito:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.preaviso.scale (config) | tenure_band · notice_due | selection / char | <6m = 1 week · 6m-1y = 10 días · 1-5y = 2 weeks · >5y = 1 month (art. 83; minimum anticipation) | FR-143 |
| l10n_gt.pay.preaviso (new) | notice_date · written_form · employer_consent_money · money_value | date / boolean / boolean / monetary (computed) | worker-payable line only on consent or FR-134 proof; money value on the art. 82 b) average (FR-136); post-notice cessation order field (liability-free close) | FR-143, FR-144 |
| l10n_gt.pay.plazo.fijo.damages (new) | months_worked · fraction · daily_rate · floor_quantum · paid_at_cessation | numeric / monetary (computed) / boolean | ≥ 1 día salario per month (fraction included); deductible from later judicial damages; ceiling = inspector/tribunal record | FR-146 |
| l10n_gt.pay.death.indemnizacion (new) | headcount_snapshot · cap_months · years · installment_value · igss_offset | integer (dated config) / const 15 or 10 / numeric / monetary / monetary (file 07) | 1 month/year capped 15 (≥20 workers) / 10 (<20); monthly installments = worker's monthly salary; beneficiary gate = judicial field | FR-147 |
| l10n_gt.pay.fuerza.mayor (new) | cause_type · band_floor · band_ceiling · graduation_value · escalation | selection / monetary / monetary / monetary (external record) / boolean | floor 2 días salario · ceiling 4 months salary; IGT/tribunal graduation surfaced; culpable/fraudulent insolvency → arts. 82/84 escalation | FR-148 |
| finiquito document (report/mail.template) | mandatory: entry/exit dates, work class, last-period ordinary+extraordinary salary; optional: manner, causes (worker request only) | template | generated from departure record + last payslip | FR-149 |
| hr.departure (settlement) | gt_pay_settlement_lines | one2many (by-id refs) | indemnización (FR-135..141) + salarios caídos (FR-132) + art. 84 floor (FR-146) + art. 85 (FR-147/148) + preaviso worker-payable (FR-143/144) + 05 GT-PAY-FR-106 + 04 GT-PAY-FR-081 — ids only | FR-150 |
| l10n_gt.pay.guard (negative rows) | guard ids | char | cesantia_absent · doubling_absent (art. 159 = note only) · employer_preaviso_absent — both sides' catalogs carry the guards | FR-145, FR-151, FR-152 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `shared` =
contract items (statutory scales/clocks and negative guards) both sides
must honor identically; judicial-gate workflows are SURFACED as record
fields with external outcomes, never adjudicated. Payroll-wave default
(binding): scales/clocks = `shared`; severance computation + finiquito
generation = `odoo`. Model names stable across Odoo 17/18/19/20; no
version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-127 | odoo | hr.contract | gt_pay_contract_class + service-nature gate | Indefinite presumption validation; permanent-activity conversion recorded; class routes FR-129..152 outcomes |
| FR-128 | shared | hr.contract (odoo surface) | substitution pair + 6-month window | Clock row both sides resolve (window end = substitution date + 6 months); solidarity flags = 01 GT-PAY-FR-022 surface |
| FR-129 | shared | hr.contract (odoo surface) | probation clock + simulation guard | First-2-months clock (shorter mutual pact recorded, longer rejected); in-probation exits pay no termination money |
| FR-130 | odoo | l10n_gt.pay.justa.causa + hr.employee counters | catalogue rows + absence counters | f) thresholds counted on 02 GT-PAY-FR-040 day surface; h) written apercibimiento prerequisite; k) judicial gate |
| FR-131 | odoo | hr.departure | written-causa doc + proof gate | Effects from written communication + effective cessation; prescription anchors consumed from 01 GT-PAY-FR-020 |
| FR-132 | odoo | l10n_gt.pay.salarios.caidos | months × rate, cap 12 | Separate award line; calendar-month default (§7 note 2); never interest (01 GT-PAY-FR-013 kin) |
| FR-133 | odoo | hr.departure + payslip events | indirect-dismissal trigger | Unpaid/incomplete/late salario completo → worker termination with full art. 82 route |
| FR-134 | odoo | hr.departure | abandonment proof fields | Worker owes preaviso (+ damages surfaced) or art. 84 mirror; no employer money arises |
| FR-135 | odoo | l10n_gt.pay.indemnizacion | quantum | 1 month/year prorated, NO cap; eligibility = indefinite + post-probation + unjustified/art. 79 only |
| FR-136 | odoo | l10n_gt.pay.indemnizacion | base window + monthly average | Last-6-months salario completo (or shorter tenure); aggregation via 01 GT-PAY-FR-005 |
| FR-137 | odoo | l10n_gt.pay.indemnizacion | bono14 feed / incentivo flag | Feeds by id: 04 GT-PAY-FR-082 (6/12 inclusion), 04 GT-PAY-FR-090 (exclusion), 04 GT-PAY-FR-095 (aguinaldo absent) |
| FR-138 | odoo | l10n_gt.pay.indemnizacion | continuity bridges + nullity guard | Suspensions bridge; continuity clauses null ipso jure; count from relation start |
| FR-139 | odoo | hr.payslip.line (stamped) | no-compensation/no-cession + unembargable | Deduction surfaces only via 01 GT-PAY-FR-010/011; privilege tag 01 GT-PAY-FR-016 |
| FR-140 | odoo | l10n_gt.pay.indemnizacion | IGSS offset fields | Pension/actuarial data external from file 07 (filename); none_due / difference_only states |
| FR-141 | odoo | l10n_gt.pay.indemnizacion | 50% case | Retirement without IGSS protection = 50% of quantum; difference-completion with lesser pension |
| FR-142 | odoo | hr.payslip.line (stamped, external feed) | ISR exemption flag | GT-TAX-FR-117 fully exempt — feed only; GT-TAX-FR-146/169 deductibility interfaces external |
| FR-143 | shared | l10n_gt.pay.preaviso.scale (odoo surface) | tenure bands 1w/10d/2w/1m | Worker-side scale both sides resolve; written form (verbal + 2 witnesses recorded); 82 c)/d) extension |
| FR-144 | odoo | l10n_gt.pay.preaviso | consent flag + money value | Money only with employer consent; valued on FR-136 base; post-notice cessation order closes liability-free |
| FR-145 | shared | l10n_gt.pay.guard | employer_preaviso_absent | R37 guard row in both catalogs; any employer-notice-pay line citing the CT rejected |
| FR-146 | odoo | l10n_gt.pay.plazo.fijo.damages | floor computation | 1 día salario/month + fraction, paid at cessation; ceiling = judicial record; daily-rate default §7 note 1 |
| FR-147 | shared | l10n_gt.pay.death.indemnizacion (odoo surface) | caps 15/10 + installments | Scale rows shared; headcount snapshot = dated config read at death date; IGSS offset from file 07; beneficiary gate judicial |
| FR-148 | shared | l10n_gt.pay.fuerza.mayor (odoo surface) | band [2 días, 4 months] | Band data shared; graduation value external record; culpable/fraudulent escalation → arts. 82/84 routes |
| FR-149 | odoo | report/mail.template (finiquito) | mandatory a/b/c + optional blocks | Generated from departure + last payslip; optional manner/causes on worker request only |
| FR-150 | odoo | hr.departure (settlement) | settlement lines (by-id) | Wires FR-132/135..141/143..149 + 05 GT-PAY-FR-106 + 04 GT-PAY-FR-081; emits FR-149; ISR flag via GT-TAX-FR-117 |
| FR-151 | shared | l10n_gt.pay.guard | cesantia_absent | R33 guard row in both catalogs; termination money = arts. 78 b)/82/83/84/85 exclusively |
| FR-152 | shared | l10n_gt.pay.guard | doubling_absent | R33 guard row; art. 159 2× = myth-rejection note only (sanction, taxation/06 territory); no multiplier on art. 82 |

Version-regime notes (D12): no dated values live in this file. All cited
values are STATIC law (CT arts. 23, 25-26, 77-85, 87 — edition qualifier
of §2 carried, R44/GOQ-70/71 vintage watch). The headcount snapshot
(FR-147) is company configuration data read as of the death event; the
IGSS actuarial values (FR-140/FR-141/FR-147) are external data of file 07
(by filename).

## 6. Acceptance Criteria

- **AC-001:** Given a contract with a written 12-month term whose recorded
  service nature is permanent, when classified, then the Art. 26 gate
  REJECTS the plazo fijo class and the contract stores indefinido — a
  later unjustified dismissal routes to the Art. 82 indemnización (FR-135);
  given the same 12-month term on an accidental service, then the plazo
  fijo class stands and early employer termination routes to the Art. 84
  floor (FR-146); given a plazo contract in a permanent-activity
  enterprise whose generating cause subsists at expiry, then the contract
  converts to indefinite at the expiry date. (FR-127)
- **AC-002:** Given a substitution of patrono recorded on 1-March, then
  the substituted and new employers are jointly flagged for obligations
  born before 1-March until 1-September (six months), and from
  2-September only the new employer remains liable. (FR-128)
- **AC-003:** Given an indefinite-contract worker exiting on probation
  day 45, then no indemnización, salarios caídos or preaviso line exists
  on the settlement; given a re-hire stipulating a fresh 2-month
  probation for the same services within months of a probation-period
  exit, then the simulation guard flags the stipulation and the service
  count does not reset (Art. 82 d) nullity). (FR-129, FR-138)
- **AC-004:** Given a 5-day-semana worker (02 GT-PAY-FR-040 configuration)
  with unpermissioned absences of 2 complete consecutive días laborales,
  then the Art. 77 f) cause row is eligible; given 5 medios días in the
  calendar month, then not yet; given the 6th medio día, then eligible;
  given an art. 64-prohibition infringement without any prior written
  apercibimiento, then the h) row is ineligible until the warning is
  recorded. (FR-130)
- **AC-005:** Given a dismissal recorded without the written
  causa-stating communication, then the termination record is invalid
  until completed and the routing treats it as unjustified (FR-132
  stack); given a written causa later flagged unproven by the recorded
  judicial outcome, then the same stack — indemnización + salarios
  caídos — computes. (FR-131, FR-132)
- **AC-006:** Given an unjustified dismissal on 1-January with a
  FR-136 monthly average of Q4,000 and the indemnización paid on
  1-September, then the salarios caídos line = 8 × Q4,000 = Q32,000; had
  payment come after 14 months, then the line is capped at 12 × Q4,000 =
  Q48,000; and no interest line ever exists on the award. (FR-132)
- **AC-007:** Given a recorded employer failure to pay the complete
  salary at the agreed date, then the worker's Art. 79 a) termination
  carries the FULL Art. 82 indemnización (indirect dismissal), identical
  to an unjustified dismissal. (FR-133)
- **AC-008:** Given 3 years 4 months of continuous service on an
  indefinite contract, unjustified-dismissed post-probation, with a
  last-6-months salario completo average of Q5,000 (overtime included;
  bono 14 feed included at min(6m, time)/12 per 04 GT-PAY-FR-082;
  incentivo lines excluded per 04 GT-PAY-FR-090), then the indemnización
  = (3 + 4/12) × Q5,000 = Q16,666.67 with no cap applied at any tenure.
  (FR-135, FR-136, FR-137)
- **AC-009:** Given a 3-month suspension (enfermedad) inside the tenure
  of AC-008, then the service-years count is unchanged (suspension
  bridges continuity); given a contract clause splitting the worker's
  tenure across two entities to interrupt continuity, then the clause is
  null ipso jure and the count runs from the relation start.
  (FR-138)
- **AC-010:** Given a dismissal for vejez with a recorded IGSS pension
  whose actuarial value ≥ the Art. 82 quantum, then the employer owes
  Q0; given an actuarially lesser pension, then only the difference is
  paid; given a worker retiring for permanent invalidity without IGSS
  protection (justification recorded), then 50% of the quantum is paid.
  (FR-140, FR-141)
- **AC-011:** Given a worker with 3 years of service quitting without
  justa causa and no notice, and the employer proving abandonment, then
  the worker owes TWO WEEKS' preaviso (the 1-5y band); given no employer
  consent to money payment, then no money-in-lieu line exists (the
  notice-period service stands); given consent, then the money value
  computes on the FR-136 average; and no employer-paid preaviso line may
  ever be generated by any route (R37). (FR-134, FR-143, FR-144, FR-145)
- **AC-012:** Given a valid plazo fijo worker (accidental service) with
  18 months worked whose employer ends the contract early without just
  cause, then the floor = 18 × daily salary (design default daily =
  FR-136 average ÷ 30, §7 note 1) paid AT cessation, and any later
  tribunal-fixed greater damages credit the floor already paid.
  (FR-146)
- **AC-013:** Given a worker dying after 12 years of service in a
  25-worker firm without IGSS protection, then the dependents' indemnización
  = 12 months (under the 15-month cap) paid in monthly installments of
  the worker's monthly salary, the beneficiary gate open for the
  judicial determination; given a 15-worker firm, then the same 12 years
  cap at 10 months; given inferior IGSS death benefits, then only the
  difference is paid. (FR-147)
- **AC-014:** Given a termination caused by caso fortuito closing the
  enterprise, then the graduation record carries the band [2 días
  salario, 4 months salario] and the externally-recorded graduation
  value; given a culpable-insolvency declaration where arts. 82/84 yield
  more, then the case re-routes to the FR-135/FR-146 computations.
  (FR-148)
- **AC-015:** Given any termination, then the generated finiquito carries
  exactly the mandatory trio — entry/exit dates, work class, last-period
  ordinary AND extraordinary salary — and includes the manner-of-work or
  termination-cause blocks ONLY when the worker-request flag is set.
  (FR-149)
- **AC-016:** Given an unjustified dismissal settlement, then the run
  wires by id the Art. 82 indemnización, the salarios caídos line, the
  vacation proration of 05 GT-PAY-FR-106 and the bono 14 proration of 04
  GT-PAY-FR-081, emits the FR-149 certificate, and stamps the
  GT-TAX-FR-117 full-exemption flag with no ISR arithmetic executed
  here. (FR-150, FR-142)
- **AC-017:** Given a rule-import attempt creating any cesantía
  accrual row, any 2× multiplier on an Art. 82 quantum, or any
  employer-side preaviso line citing the CT, when the guard registry is
  consulted, then each is rejected (cesantia_absent · doubling_absent ·
  employer_preaviso_absent), and a search of this file's LB table for a
  cesantía or doubling provision returns only the LB-015 negative
  finding with the art. 159 myth-rejection note. (FR-151, FR-152, FR-145)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C):
NONE are assigned to this file. GOQ-70/71 (R44 edition discipline) are
discharged by the qualifier on every CT LB row (§2), the same treatment
as `01_ct-salary-model.md` and `05_vacaciones-maternidad.md`. No OQ rows
are registered here and no new OQ ids are invented. Genuine gaps surfaced
during synthesis are REPORTED to the wave lead (task report) instead:

1. **Art. 84 daily-rate derivation (affects FR-146):** the floor of "un
   día de salario por cada mes" does not state how the día de salario
   derives for monthly-salaried workers; design default = FR-136
   last-6-months average ÷ 30, configurable pending an
   authority-grounded convention.
2. **Salarios caídos measurement (affects FR-132):** art. 78 b) fixes
   the window (dismissal → payment of the indemnización) and the 12-month
   cap but not the counting unit; design default = calendar months
   elapsed × the FR-136 monthly average, partial terminal month
   pro-rated.
3. **Art. 83 print defects (LB-011):** the edition prints "diez, días"
   and "ser vicios" (for servicios) — carried [sic]; and the evidence
   layer prints "plazos" where the source txt layer prints "plazas" in
   the non-compensation clause — variance recorded, the evidence text is
   carried per wave discipline (kin of the file-02 elision-completion
   precedent).
4. **Art. 82 e) actuarial data dependency (affects FR-140/FR-141):** the
   offset and 50% rules hinge on IGSS pension values and
   expectativa-de-vida actuarial determinations made by the Institute —
   the data interface is file 07's (by filename); until that file lands
   the fields are external-input placeholders, never estimated
   payroll-side.
5. **Art. 85 headcount snapshot semantics (affects FR-147):** the 15/10
   cap keys on "empresas con veinte o más trabajadores" without an
   as-of rule; design default = headcount read at the death date, and
   the beneficiary census (herederos/concubina as printed) is
   judicially determined — surfaced as a gate field only.
6. **Probation re-stipulation horizon (affects FR-129):** art. 81 bans
   simulation without defining the lookback for guard purposes; design
   default = flag any second probation for the same worker/services
   within 12 months of a prior probation's end, pending doctrine.
