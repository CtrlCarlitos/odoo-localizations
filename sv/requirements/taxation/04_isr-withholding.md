# SV — Taxation — ISR withholding: payroll retention tables & CT retention matrix

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for El Salvador's ISR
withholding layer: the salaried retention regime (*retención a asalariados*,
retention on salaries) — retention as the collection method whose sum is the
tax for salaried persons at or below US$9,100.00, the US$1,600.00 fixed
deduction embedded in the retention quota (Art. 29.7), the retention BASE
definition (gross − non-taxable remunerations − employee social-security and
pension contributions, per D.E. 10-2025 Art. 1 d)) and the Art. 33
US$800.00 × 2 personal deductions (medical incl. parents/spouse/children
under 25/domestic employees, and schooling) with the Reglamento Art. 39
dependent-child proof; the PERIODIC retention tables (monthly, *quincenal*
(fortnightly), *semanal* (weekly)) and the June/December *recálculo*
(recalculation) tables as verbatim dated data in the
`withholding_tables.csv` sidecar, with the bracket engine, the semi-annual
true-up engine (cumulative gravadas → table − prior retentions → zero
floor), its exclusions and last-employer responsibility; special periods via
*regla de tres* (rule-of-three proportion) and extraordinary remuneration
aggregation (*aguinaldo* (statutory year-end bonus), vacations, bonuses);
the multi-employer split (progressive table on the highest-paying job + flat
10% on the rest) and the voluntary retention increase; the aguinaldo
exemption vintages (standing 2-SMM rule of Art. 4.16 with floor deduction,
2014-2018 full-exemption and 2021-2024 fixed-cap transitories); the
non-payroll ISR retention matrix of the Código Tributario (Tax Code, CT)
— honorarios 10%, leases, intangibles 10%/5%, capital-yield/dividend
advances 10% (kept DISTINCT from Art. 72's 5% distributions), courts,
non-resident 20% definitive with reduced rates, tax-haven 25%, financial
institution deposits and raffles/prizes — to the extent these configure
Odoo payment flows; and the part-time/hourly service classification
(half-times, class-hours, medical-hours = *servicio permanente*, permanent
service → tables, not 10%).

It does **not** cover: the ANNUAL Art. 37 progressive table and its two
vintages (`03_isr-rates-gains.md` §3.1/§4 — SV-TAX-FR-074..076 own it; this
file's recálculo tables DERIVE from it and cite it, never restate the annual
table outside the `isr_brackets.csv` sidecar which both files share); the
filing-duty and remittance calendar (`01_isr-framework.md` §3.5 —
SV-TAX-FR-026..033; the ten-*días hábiles* remittance is SV-TAX-FR-032);
deductibility of payroll costs (`02_isr-deductions.md` SV-TAX-FR-040 — the
payroll-deductibility gate whose "retentions effected & entered" side is
satisfied by THIS file's retention data); the 5% distributions regime
(`05_isr-distributions.md` §3, to be written — dividend withholding track);
social-security contribution rates, contract law and SMM figures (later
payroll wave; the 2-SMM aguinaldo floor references the SMM *concept*, fed
by the salarios-mínimos source, and encodes no SMM value); or sanctions
(CT Arts. 226-247 zone). Those files reference this one for the base and
threshold FRs (SV-TAX-FR-104, SV-TAX-FR-106) that the payroll wave
consumes.

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated
Ley ISR, current article text incl. reform stamps through Jan-2026) with
reform decrees for changed articles > 03_ (historical consolidation through
D.L. 233-2012; supplies analysis via EVID ids). Retention tables: **53_**
(D.E. 10-2025, operative; effective 2025-05-08 per MH dating, D.O. pin
pending = SOQ-03) > 10_ (D.E. 75/25-1992, historical dated data only — R19).
Reglamento: 04_ = D.E. 101-1992 as consolidated with reforms D.E. 8-1993 /
39-1993 / **117-2001** (self-documented repeal map — R17); only survivor
articles are cited. CT matrix: 05_ (EVID-062/063). Every Ley article below
was re-verified in the 54_ consolidation text during this task (54_-verify
rule; page anchors are 54_ pagination from the extraction txt `=== PAGE n
===` markers).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 29 num. 7 | Salaried fixed deduction: natural persons whose renta comes exclusively from salaries with annual amount ≤ US$9,100.00 are not obliged to present liquidation and have the right to a FIXED DEDUCTION of US$1,600.00 NOT subject to comprobación (voucher substantiation); the fixed deduction and the social-security contributions are INCLUDED in the retention quota; salaried persons with rents above US$9,100.00 get the Arts. 32/33 deductions, subject to comprobación (stamps (2)(14)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 29.7 p.20 (EVID-096; verified 54_ txt) |
| LB-002 | Ley ISR, Art. 33 | Personal deductions for domiciled natural persons with diverse rents (Art. 29.7 expressly excepted): maximum US$800.00 PER CONCEPT per ejercicio: a) paid in-country for hospital services, medicines and professional services (physicians, anesthetists, surgeons, radiologists, psychologists, ophthalmologists, laboratory workers, physiotherapists, dentists) for the contributor, parents, spouse, children under 25 and domestic employees — professional domiciled and legally authorized; relatives/spouse not themselves contributors; Salvadoran government officials abroad exempt from the domicile requirement; only uninsured amounts; orthopedic devices; medicines with medical prescription; b) colegiatura or escolaridad (tuition/schooling) of children under 25 who are not contributors, at State-authorized teaching centers, any education level; same cap for self-financed studies; salaried persons whose renta exceeds US$9,100.00 entitled; substantiation: no document annexed to the declaration but records kept SIX years (stamps (1)(8)(17)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 33 pp.36-37 (EVID-096; verified 54_ txt) |
| LB-003 | Ley ISR, Arts. 38-39 | Salaried thresholds: domiciled natural persons with rents exclusively from salaries who were subject to retention are NOT obliged to declare, EXCEPT rents above US$60,000.00 annual, no retention effected, or retentions not consonant with the Art. 37 table (then declare or request refund); tax of non-obliged persons = SUM of retentions per CT Art. 155 in relation to the retention tables; salaried without fixed-deduction benefits may voluntarily declare for refund; at DGII request ISSS, SSF and AFP are obliged to exchange information for retention-payment control; Art. 39: domiciled or not with diverse incomes incl. salaries not exceeding the Art. 38 limit present the liquidation | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 38-39 pp.38-39 (EVID-096; verified 54_ txt) |
| LB-004 | Ley ISR, Art. 4 num. 16 | Aguinaldo: income received by workers (Código de Trabajo and Ley sobre Compensación Adicional en Efectivo) up to TWO SMM (monthly minimum wages) of the commerce-and-services sector is NOT subject to ISR retention; aguinaldos exceeding that amount are subject to retention and payment of the tax DEDUCTING the two SMM (floor deducted from the excess — stamp (23) = D.L. 458-2019 wording) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 4.16 p.7 (EVID-165; verified 54_ txt) |
| LB-005 | Ley ISR, Arts. 60, 64-65 | Retention-mechanics survivors: in-kind retained rents calculated in cash at market value at the payment moment (Art. 60); "servicio permanente" = service regulated by labor law remunerated as salaries, sueldos, sobresueldos, horas extras, primas, comisiones, gratificaciones, aguinaldos and any other compensation for personal services, indefinite or fixed term, full-time, half-time or part-time, WITH subordination or dependency (Art. 64, stamp (9)); retention tables revised periodically by the Executive through decree incorporated into the Reglamento, portions in consonance with Art. 37 (Art. 65); AGENT duties per the tables decree: a) apply the tables, b) subtract the rentas no gravadas from total period remunerations, c) effect the June and December recálculo; SUBJECT duties: 1) inform each employer of multiple employments and amounts, 2) designate which rent gets the table retention when rents are equal, 3) demand the CT Art. 145 retention constancia from the prior employer for the new one; breach sanctioned with two SMM (Art. 65 zone, stamp (19); remittance deadline Art. 62 = `01_isr-framework.md` LB-027; Art. 63 repealed (12)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 60, 64-65 pp.42-44 (EVID-104; verified 54_ txt) |
| LB-006 | D.E. 10-2025 (tablas de retención), considerandos + Art. 1 a) | Tables issued under Ley ISR Art. 65 authority tracking Art. 37 rates (D.L. 293-2025 exempt base $6,600.00 annual = $550.00 monthly); base structured on NET monthly renta after deducting cotizaciones previsionales, remuneraciones no gravadas and the legal social-security/education/health deductions of Arts. 29.7 and 33; MONTHLY table: I $0.01–$550.00 sin retención; II $550.01–$895.24 10% s/ exceso de $550.00 + $17.67; III $895.25–$2,038.10 20% s/ $895.24 + $60.00; IV $2,038.11 en adelante 30% s/ $2,038.10 + $288.57 | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | considerandos pp.1-2; Art. 1 a) p.2 (EVID-153/154) |
| LB-007 | D.E. 10-2025, Art. 1 b)/c) | QUINCENAL table: $0.01–$275.00 sin retención; $275.01–$447.62 10% s/ $275.00 + $8.83; $447.63–$1,019.05 20% s/ $447.62 + $30.00; $1,019.06 en adelante 30% s/ $1,019.05 + $144.28. SEMANAL table: $0.01–$137.50 sin retención; $137.51–$223.81 10% s/ $137.50 + $4.42; $223.82–$509.52 20% s/ $223.81 + $15.00; $509.53 en adelante 30% s/ $509.52 + $72.14. Quincenal = exact half, semanal = exact quarter of the monthly bands (NOT /4.33) | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 b)/c) p.3 (EVID-155) |
| LB-008 | D.E. 10-2025, Art. 1 d) | Retention base: only the remuneraciones gravadas (taxable remunerations) of the respective period are considered, determined by deducting from the TOTAL period remunerations: the remuneraciones no gravadas (non-taxable remunerations) and the cotizaciones laborales a la Seguridad Social (employee social-security contributions); the cotizaciones previsionales to the AFPs and public pension institutes are comprised within the no-gravadas concept; the tables do NOT embed the social-security cotización laboral, which must be subtracted before computing the retention | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 d) p.3 (EVID-156) |
| LB-009 | D.E. 10-2025, Art. 1 e) | Tramo II non-embedding: the values in Tramo II ONLY of the a)/b)/c) tables do NOT contain the US$1,600.00 deduction of Ley Art. 29.7 first inciso available to salaried natural persons whose annual amount is ≤ US$9,100.00; therefore, to apply the retention, the deduction must be considered in the corresponding calculation (no proration factor stated — SOQ-02/OQ-001) | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 e) p.4 (EVID-157) |
| LB-010 | D.E. 10-2025, Art. 1 f) | June/December recálculo: JUNE table (Jan-Jun cumulative): $0.01–$3,300.00; $3,300.01–$5,371.44 10% s/ $3,300.00 + $106.20; $5,371.45–$12,228.60 20% s/ $5,371.44 + $360.00; $12,228.61 en adelante 30% s/ $12,228.60 + $1,731.42. DECEMBER table (full-year): $0.01–$6,600.00; $6,600.01–$10,742.86 10% s/ $6,600.00 + $212.12; $10,742.87–$24,457.14 20% s/ $10,742.86 + $720.00; $24,457.15 en adelante 30% s/ $24,457.14 + $3,462.86. From the table result subtract the sum of retentions effected in the prior monthly periods (Jan-May / Jan-Nov); the POSITIVE difference is the June/December retention; negative → retain nothing. Excluded from the recálculo: remunerations subject to retención definitiva and remunerations subject to the 10% of Art. 1 h). Employer change: the LAST patrono is responsible for the recálculo and retention; the worker obtains the CT Art. 145 constancia from the prior employer within 15 días hábiles of retirement; Tramo II $1,600 applies in the recálculo (persons ≤ $9,100/yr); persons > $9,100 apply Art. 33 deductions (medical/schooling) | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 f) + tables pp.4-5 (EVID-158) |
| LB-011 | D.E. 10-2025, Art. 1 g) | Special periods: the MONTHLY table applies, computing the equivalent monthly salary by regla de tres simple (simple rule of three), likewise the monthly retention portion, and by the same method the retention for the period; extraordinary remunerations (aguinaldos, vacaciones, bonificaciones, premios, gratificaciones): same method; no associable period → treated as monthly; if computed independently → no retention, then summed with the salary and the monthly table applied; same payment date → the amount is applied against the total; different dates → against the LAST remuneration paid in the monthly period | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 g) p.6 (EVID-159) |
| LB-012 | D.E. 10-2025, Art. 1 h) | Multi-employer: two or more patronos → the table applies to the HIGHEST-paying job; the other remunerations bear flat 10% on the sums paid or credited; if the aggregate of all remunerations is below the exemption threshold → no retention; the worker informs each employer of the multiple jobs and respective amounts (in January, or within 15 días hábiles of any change); equal rents → the worker designates which gets the table; employer change in-year → prior employer issues the CT Art. 145 retention constancia within 15 días hábiles for the June/December recálculo. Voluntary increase: the worker may request DGII (formulario, copy to the retention agent) a HIGHER retention or the inclusion of other rents in the monthly calculation | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 h) pp.6-7 (EVID-160) |
| LB-013 | D.E. 10-2025, Art. 1 i), Arts. 2-4 | Mismatch duty: if ejercicio retentions do not match the Art. 37 liquidation, declare/pay per Arts. 37 & 48 or request refund; in any case subjects with rents > US$60,000.00 MUST file; online-only filing for withheld domiciled natural persons via MH website aplicativos (Art. 2 — informational; consumed by `01_isr-framework.md` FR-029/FR-031); repeals D.E. 95-2015 (18-XII-2015, D.O. 236 T.409 22-XII-2015) (Art. 3); vigencia 8 days after D.O. publication → 2025-05-08 per MH dating, D.O. pin pending (SOQ-03/OQ-002) | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 i), Arts. 2-4 pp.7-8 (EVID-161) |
| LB-014 | Reglamento ISR (D.E. 101-1992 consolidado), Art. 59 | Part-time = servicio permanente: within the Art. 64 concept the remunerations agreed not only full-time but ALSO part-time are comprised — medios tiempos (half-times), horas clase (class-hours), horas médicos (medical-hours) and similar are "partial" (retention-mechanics survivor; interaction with the Ley Art. 64 subordination qualifier = OQ-004) | `sv/sources/04_Reglamento_ISR.pdf` | Art. 59 p.14 (EVID-144) |
| LB-015 | Reglamento ISR, Art. 39 | Dependent-child deduction proof (implements Ley Art. 33 b): the child must not have turned 25; proof for studying children (professional/technological studies) = age/civil-status evidence plus the school certificate of enrollment and normal attendance ATTACHED TO THE RETURN (carried pointer from the deductions-file review — uncited there; belongs to this personal-deductions track) | `sv/sources/04_Reglamento_ISR.pdf` | Art. 39 p.13 (EVID-143) |
| LB-016 | Código Tributario, Arts. 154-155 | Retention agents: agent concept; retention effected at payment or acreditamiento (crediting), whichever occurs first; permanent services → the retention tables (payroll track); CT 155 inc. 2's general "aguinaldo exempt from ISR retention" statement YIELDS to Ley Art. 4.16 specifics (lex specialis, later in time — R22; read as within the 2-SMM floor) | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 154-155 pp.83-86 zone (EVID-062/063; R22) |
| LB-017 | Código Tributario, Arts. 156, 156-A, 156-B, 157 | CT retention matrix (fees/leases/intangibles/capital/courts): services rendered by independent natural persons → 10% regardless of amount, ADVANCES included; seasonal agricultural harvest labor EXCLUDED; leases to natural persons → 10% (Art. 156); intangibles → 10% natural persons / 5% entidades (Art. 156-A); capital yields and dividend ADVANCES → 10%, excepted: dividends already taxed as such and labor indemnities within ISR limits (Art. 156-B — DISTINCT from Ley Art. 72's 5% definitive distributions regime, `05_isr-distributions.md` §3); courts → 10% on interest in ejecutivo judgments (Art. 157) | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 156-157 pp.86-88 zone (EVID-063) |
| LB-018 | Código Tributario, Arts. 158, 158-A | Non-residents: 20% DEFINITIVE on rents from abroad (services used in-country, intangibles, capital yields); REDUCED rates: 5% international transport, 5% reinsurers, 10% qualified foreign financing (20% related-party financing), 5% film/TV rights; zona franca / ISL-exempt payers excepted; subjects of tax-haven jurisdictions → 25% (Art. 158-A) | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 158-158-A pp.88-90 zone (EVID-063) |
| LB-019 | Código Tributario, Arts. 159, 160, 145 | Financial institutions: retentions on deposit rents (interest, prizes, utilities) = DEFINITIVE payment (Art. 159 — mechanic cross-referenced by `03_isr-rates-gains.md` FR-091, which owns the small-depositor carve-out); raffles and prizes organized by natural or juridical persons → retention per the article (Art. 160); retention constancia (Art. 145): the prior employer issues the certificate within 15 días hábiles of the worker's retirement, as cross-cited by 53_ Art. 1 f)/h) for employer changes and recálculo intake | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 159-160, 145 pp.83-90 zone (EVID-063; EVID-158/160) |
| LB-020 | Tablas de Retención ISR, D.E. 75-1991 + D.E. 25-1992 — **HISTORICAL** | 1992 colones-era retention tables (literals a)-c) substituted by D.E. 25-1992, D.O. 34 T.314 20-II-1992, effective 1-III-1992; dual ¢/$ print at fixed 8.75 parity; monthly/quincenal/semanal, FIVE rows each with two 10% rows and anomalous row-3 offsets); base gross-vs-net unstated; subjects = domiciled natural persons with permanent-service remunerations; ≤ ¢50,000/yr salaried: tax = sum of retentions; repealed D.E. 36-1989; later repealed by the D.E. 95-2015 chain (derogation date unpinned — OQ-005). HISTORICAL LB per R19: dated data only, never applied to current periods; USD rows transcribed in `isr_brackets.csv` as vintage de_25_1992 | `sv/sources/10_Tablas_Retencion_ISR.pdf` | tables a)-c) pp.1-2; Arts. 1-4 + REFORMAS pp.1-3 (EVID-148..152) |
| LB-021 | Ley ISR (consolidada), tail "DISPOSICIONES RELACIONADAS" | Aguinaldo transitories overriding the standing 2-SMM rule by year: D.L. 877-2014, 177-2015, 540-2016, 831-2017, 160-2018 (2014-2018: aguinaldo retention fully exempted for the year); D.L. 229-2021 (D.O. 233 T.433 7-XII-2021) "hasta un límite de $1,100"; D.L. 596-2022 (D.O. 231 T.437) "$1,500"; D.L. 900-2023 (D.O. 225 T.441) "$1,500.00"; D.L. 159-2024 (D.O. 227 T.445 27-XI-2024) "$1,500.00"; no transitory listed after 159-2024 → 2025+ standing 2-SMM rule assumed (SOQ-05/OQ-003) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | DISPOSICIONES RELACIONADAS pp.61-63 (EVID-167) |

Dead text — never implementable as current law (recorded here as LB notes,
not FRs, per wave constraints): CT Art. 155 inciso 2's blanket "aguinaldo
exempt from ISR retention" statement — yields to Ley Art. 4.16 (2-SMM floor;
floor DEDUCTED from the excess since D.L. 458-2019 — R22; LB-016/LB-004);
the 10_ colones-era tables and their unstated gross base — historical dated
data only (R19; LB-020); the 2014-2018 full-exemption and 2021-2024
fixed-cap aguinaldo vintages — dated data for their years only (LB-021).

## 3. Functional Requirements

### 3.1 Salaried regime: retention as payment, base and personal deductions

- **SV-TAX-FR-102:** The system shall implement the salaried retention
  regime (*retención a asalariados*) as the ISR collection method for
  domiciled natural persons whose rents come exclusively from salaries,
  sueldos and other permanent-service remunerations: the periodic
  retention computed under this section is the employee's ISR, and for
  persons not obliged to declare the tax equals the SUM of the retentions
  effected (per CT Art. 155 in relation to the tables), with the
  retention/remittance data satisfying the "effected and entered"
  (*realizado y enterado*) condition of the payroll-deductibility gate
  `02_isr-deductions.md` SV-TAX-FR-040. (LB-003; LB-005; LB-016;
  EVID-096/104/063)
- **SV-TAX-FR-103:** The system shall grant the US$1,600.00 fixed
  deduction of Ley Art. 29.7 to salaried natural persons whose annual
  renta is ≤ US$9,100.00 — NOT subject to *comprobación*
  (voucher substantiation) — recognizing that the law embeds the fixed
  deduction and the social-security contributions in the retention quota:
  in the June/December recálculo tables the embedding is structural
  (boundaries shifted, SV-TAX-FR-110/111), while in the periodic
  monthly/quincenal/semanal tables ONLY Tramo II values exclude it and the
  deduction must be applied in the calculation per D.E. 10-2025 Art. 1 e)
  (proration working assumption and ordering per OQ-001/SOQ-02);
  salaried persons above US$9,100.00 receive the Art. 33 deductions
  instead (SV-TAX-FR-105). (LB-001; LB-009; LB-010; EVID-096/157/158)
- **SV-TAX-FR-104:** The system shall compute the retention BASE per
  D.E. 10-2025 Art. 1 d) for every periodic, recálculo and special-period
  computation: base = total remunerations of the period MINUS the
  *remuneraciones no gravadas* (non-taxable remunerations, including the
  *cotizaciones previsionales* — pension contributions to AFPs and public
  pension institutes, which the decree comprises within the no-gravadas
  concept) MINUS the *cotizaciones laborales a la Seguridad Social*
  (employee social-security contributions, ISSS); EMPLOYER-side
  contributions shall never be netted; the base shall be computed BEFORE
  the table lookup (Tramo II fixed-deduction ordering per OQ-001), and
  only *remuneraciones gravadas* (taxable remunerations) of the
  respective period may enter any table application. (LB-008; EVID-156)
- **SV-TAX-FR-105:** The system shall support the Art. 33 personal
  deductions — a maximum of US$800.00 per ejercicio PER CONCEPT (two
  concepts, medical + education): (a) medical: hospital services,
  medicines and professional services of physicians, anesthetists,
  surgeons, radiologists, psychologists,
  ophthalmologists, laboratory workers, physiotherapists and dentists
  paid in-country for the contributor, parents, spouse, children under
  25 and domestic employees (professional domiciled and legally
  authorized; relatives/spouse not themselves contributors; only amounts
  not compensated by insurance or other indemnity; orthopedic devices;
  medicines only with medical prescription); (b) education: *colegiatura o
  escolaridad* (tuition/schooling) of children under 25 who are not
  contributors at State-authorized centers, any level, plus the same cap
  for the contributor's self-financed studies; available to salaried
  persons whose renta exceeds US$9,100.00 (with the Art. 32 deductions)
  and to diverse-income persons; the system shall require NO document
  annexed to a declaration but enforce the SIX-year record-retention
  flag; and for the schooling concept it shall apply the Reglamento
  Art. 39 proof rule — the child must not have turned 25 and studying
  children require age/civil-status evidence plus the school certificate
  of enrollment and normal attendance attached to the return.
  (LB-002; LB-015; EVID-096/143)
- **SV-TAX-FR-106:** The system shall expose the salaried-regime
  thresholds as dated parameters driving retention-mode selection and
  year-end flags: (a) US$9,100.00 annual renta — at or below: fixed
  deduction mode (SV-TAX-FR-103) with no liquidation duty; above:
  Art. 33 deductions mode (SV-TAX-FR-105); (b) US$60,000.00 annual
  rents — mandatory-declaration flag consumed by
  `01_isr-framework.md` SV-TAX-FR-029; (c) retention-vs-Art. 37
  mismatch and no-retention cases — declare-or-refund flag consumed by
  SV-TAX-FR-029 (mismatch duty per D.E. 10-2025 Art. 1 i)). (LB-003;
  LB-013; EVID-096/161)
- **SV-TAX-FR-107:** The system shall record (informational,
  awareness-level) that ISSS, the Superintendencia del Sistema Financiero
  (SSF) and the AFPs are obliged to exchange information with DGII for
  control of retention payments by retention agents — no Odoo computation
  derives from this duty; it justifies retaining employee/pension
  contribution identifiers on the payroll data model. (LB-003; EVID-096)

### 3.2 Retention tables as dated legal data

- **SV-TAX-FR-108:** The system shall load the periodic retention tables
  (monthly, quincenal, semanal) and the June/December recálculo tables as
  DATED legal data selected by the payment period's date (D7/D12
  version regime), seeded from the `withholding_tables.csv` sidecar
  transcribed EXACTLY as printed in D.E. 10-2025: printed-digit
  anomalies are carried in the note column with [sic] flags and NEVER
  silently corrected (SOQ-03 fidelity rule — June 5,371.44 / 12,228.60 /
  cuota 106.20 / 1,731.42; semanal IV 509.53; quincenal IV 1,019.06);
  the retention-decree chain shall be recorded as vintage metadata —
  D.E. 25-1992 (historical, `isr_brackets.csv` vintage de_25_1992) →
  D.E. 95-2015 (repealed by D.E. 10-2025 Art. 3; its table values are
  NOT in the corpus — OQ-005) → D.E. 10-2025 OPERATIVE, valid_from
  2025-05-08 per MH dating with the publishing D.O. issue pending
  (SOQ-03/OQ-002); the annual Art. 37 table vintages consumed by the
  recálculo derivation remain `03_isr-rates-gains.md` SV-TAX-FR-074
  property (both vintages also seeded in `isr_brackets.csv`).
  (LB-006; LB-007; LB-010; LB-013; LB-020; EVID-153..161; R19; R20)
- **SV-TAX-FR-109:** The system shall compute every periodic retention
  by the bracket engine on the SV-TAX-FR-104 base: locate the table row
  (frequency-appropriate vintage) whose DESDE/HASTA interval contains
  the base, apply the row's percentage over the excess of the base above
  the row's SOBRE EL EXCESO DE anchor, and add the row's *cuota fija*
  (fixed quota); Tramo I bases retain nothing (*SIN RETENCIÓN*).
  (LB-006; LB-007; EVID-154/155)

### 3.3 June/December recálculo engine

- **SV-TAX-FR-110:** The system shall compute the JUNE recalculation:
  accumulate the employee's remuneraciones gravadas January-through-June
  (net of the SV-TAX-FR-104 components), apply the June recálculo table
  to the cumulative base, subtract the sum of the retentions effected in
  the prior monthly periods January-through-May, and retain the POSITIVE
  difference; a negative difference retains nothing (floor at zero).
  (LB-010; EVID-158)
- **SV-TAX-FR-111:** The system shall compute the DECEMBER
  recalculation: accumulate the remuneraciones gravadas of the whole
  ejercicio (January-through-December), apply the December recálculo
  table, subtract the sum of the retentions effected January-through-
  November, and retain the positive difference (zero floor); the
  December table equals the Art. 37 annual table of
  `03_isr-rates-gains.md` SV-TAX-FR-074 shifted by +US$1,600.00 on the
  Tramo II/III boundaries with identical cuotas fijas (structural
  embedding of the Art. 29.7 deduction — cited, not restated).
  (LB-010; EVID-158)
- **SV-TAX-FR-112:** The system shall EXCLUDE from both recálculo
  accumulations: (a) remunerations that were subject to *retención
  definitiva* (definitive withholding), and (b) remunerations subject to
  the flat 10% multi-employer retention of SV-TAX-FR-117 (Art. 1 h)
  amounts. (LB-010; EVID-158)
- **SV-TAX-FR-113:** The system shall assign the June/December
  recálculo responsibility to the LAST *patrono o empleador* (employer)
  when the worker changed employers in-year, ingesting the CT Art. 145
  *constancia de retención* (retention certificate) that the prior
  employer must issue within 15 días hábiles of the worker's
  retirement — prior-employer retention data enters the recálculo only
  through that constancia. (LB-010; LB-012; LB-019; EVID-158/160)
- **SV-TAX-FR-114:** The system shall select the deduction mode inside
  the recálculo per the annual projection: workers with annual renta ≤
  US$9,100.00 get the Tramo II US$1,600 fixed deduction (embedded in
  the shifted recálculo tables); workers above US$9,100.00 instead
  apply the Art. 33 deductions (medical/schooling, SV-TAX-FR-105) in
  the recálculo. (LB-010; EVID-158)

### 3.4 Special periods and extraordinary remunerations

- **SV-TAX-FR-115:** The system shall compute retentions for daily or
  special pay periods through the *regla de tres simple* (simple
  rule-of-three) monthly equivalence: derive the equivalent monthly
  salary, compute the corresponding monthly retention, and derive the
  period's retention by the same proportional method (the MONTHLY table
  is always the vehicle; no flat day-rate shortcut). (LB-011; EVID-159)
- **SV-TAX-FR-116:** The system shall aggregate EXTRAORDINARY
  remunerations — *aguinaldos* (statutory year-end bonuses),
  *vacaciones* (vacation pay), *bonificaciones, premios,
  gratificaciones* (bonuses, prizes, gratuities) — into the retention
  computation by the D.E. 10-2025 Art. 1 g) rules: same regla-de-tres
  method; no associable period → treated as monthly; an extraordinary
  remuneration computed independently (no retention arose) is SUMMED
  with the salary and the monthly table applied; when paid on the same
  date as the salary, the amount is aggregated into the total for the
  table application, and when payment dates differ, into the LAST
  remuneration paid within the monthly period. (LB-011; EVID-159)

### 3.5 Multi-employer cases

- **SV-TAX-FR-117:** The system shall compute multi-employer retention
  splits: the progressive table (SV-TAX-FR-109) applies ONLY to the
  HIGHEST-paying employment; every other employment bears a flat 10%
  retention on the sums paid or credited (amounts excluded from the
  recálculo per SV-TAX-FR-112); where the aggregate of all
  remunerations falls below the exemption threshold (Tramo I), NO
  retention is effected by any employer. (LB-012; EVID-160)
- **SV-TAX-FR-118:** The system shall support the worker's
  multi-employer information duties: informing each employer of the
  existence of more than one employment and the respective amounts — in
  January, or within 15 días hábiles of any change — and designating
  which employment's rent receives the table retention when the rents
  of different employments are of EQUAL amount (breach carries a
  two-SMM sanction per the Ley Art. 65 zone — informational flag, CT
  sanctions regime governs collection). (LB-005; LB-012; EVID-104/160)
- **SV-TAX-FR-119:** The system shall support a voluntary retention
  increase elected by the worker: a HIGHER retention amount or the
  inclusion of other rents in the monthly calculation, requested to
  DGII via its formulario with copy to the retention agent, recorded as
  a dated worker-level override on the retention computation (no
  system-initiated variation without the DGII form on file).
  (LB-012; EVID-160)

### 3.6 Aguinaldo exemption vintages

- **SV-TAX-FR-120:** The system shall compute the aguinaldo retention
  under the Art. 4.16 STANDING rule with vintage selection by payment
  year: exemption up to TWO SMM (salario mínimo mensual) of the
  commerce-and-services sector — the SMM figure is a dated parameter
  fed by the salarios-mínimos source (16_), concept-referenced here
  with NO SMM value encoded in this file; aguinaldos exceeding the
  exempt amount are retained upon DEDUCTING the two-SMM floor from the
  excess (D.L. 458-2019 wording, stamp (23)); vintage rows as dated
  data: 2014-2018 (D.L. 877-2014/177-2015/540-2016/831-2017/160-2018)
  = FULL exemption; 2021 (D.L. 229-2021) = cap US$1,100.00; 2022-2024
  (D.L. 596-2022/900-2023/159-2024) = cap US$1,500.00; 2025+ = the
  standing 2-SMM rule (assumption re-verified by the payroll wave per
  SOQ-05/OQ-003); CT 155 inc. 2's blanket-exemption reading never
  applies (R22). (LB-004; LB-016; LB-021; EVID-165/167/063; R22)

### 3.7 CT non-payroll retention matrix

- **SV-TAX-FR-121:** The system shall effect ISR retentions at the
  moment of payment or *acreditamiento* (crediting to account),
  whichever occurs first (CT Art. 154 agent concept), and shall apply
  the 10% retention to fees for services rendered by independent
  natural persons (*honorarios*) REGARDLESS of amount, including
  ADVANCES, EXCLUDING seasonal agricultural harvest labor (*labores
  agrícolas de cosecha estacional*). (LB-016; LB-017; EVID-063)
- **SV-TAX-FR-122:** The system shall apply the 10% retention to lease
  rents (*arrendamientos*) paid or credited to natural persons.
  (LB-017; EVID-063)
- **SV-TAX-FR-123:** The system shall apply the intangibles retention
  split by lessor type: 10% when the holder is a natural person, 5%
  when an entity (*entidades*), on rents for the use or exploitation of
  intangibles. (LB-017; EVID-063)
- **SV-TAX-FR-124:** The system shall apply the 10% retention to
  capital yields and dividend ADVANCES (CT Art. 156-B), excepting
  dividends already taxed as such and labor indemnities within ISR
  limits, and shall keep this 10% track DISTINCT from the Art. 72 5%
  definitive distributions regime owned by
  `05_isr-distributions.md` §3 (dividend withholding track — to be
  written): no 156-B retention line may consume or shadow the 5%
  regime's base and vice versa. (LB-017; EVID-063)
- **SV-TAX-FR-125:** The system shall apply the 10% retention to
  interest awarded in *juicios ejecutivos* (enforcement judgments) —
  courts as retention agents on judgment interest. (LB-017; EVID-063)
- **SV-TAX-FR-126:** The system shall apply the 20% DEFINITIVE
  retention to non-resident subjects on Salvadoran-source rents from
  abroad (services used in-country, intangibles, capital yields), with
  the REDUCED rates as dated parameters: 5% international transport,
  5% reinsurers, 10% qualified foreign financing, 20% related-party
  financing, 5% film/TV rights; payers exempted by zona franca / ISL
  legislation are excepted from the retention duty. (LB-018; EVID-063)
- **SV-TAX-FR-127:** The system shall apply the 25% retention to
  subjects domiciled or incorporated in tax-haven jurisdictions
  (CT Art. 158-A), keyed to the CT's related-subject /
  preferential-regime classification (consumed from the CT partner
  classification; no separate haven list is invented here).
  (LB-018; EVID-063)
- **SV-TAX-FR-128:** The system shall apply the financial-institutions
  retention on deposit rents (interest, prizes, utilities) as
  DEFINITIVE payment (CT Art. 159), consuming the small-depositor
  carve-out owned by `03_isr-rates-gains.md` SV-TAX-FR-091 (domiciled
  natural person, holder, average monthly balance below US$25,000.00 →
  renta no gravable, no retention). (LB-019; EVID-063)
- **SV-TAX-FR-129:** The system shall apply the raffles-and-prizes
  retention (CT Art. 160) to raffle and prize payments flowing through
  Odoo payment/disbursement documents, as a definitive retention keyed
  to the payment's prize nature. (LB-019; EVID-063)

### 3.8 Part-time and hourly service classification

- **SV-TAX-FR-130:** The system shall classify part-time and hourly
  service remunerations — *medios tiempos* (half-times), *horas clase*
  (class-hours), *horas médicos* (medical-hours) and similar — as
  *servicio permanente* (permanent service) under the Reglamento
  Art. 59 extension, routing them to the progressive retention tables
  (SV-TAX-FR-109) and NEVER to the 10% honorarios retention of
  SV-TAX-FR-121; the Ley Art. 64 definition (indefinite or fixed term,
  full/half/part-time, WITH subordination or dependency) governs, and
  the boundary question for arrangements lacking subordination is
  recorded as OQ-004. (LB-005; LB-014; EVID-104/144)
- **SV-TAX-FR-131:** The system shall compute retentions on in-kind
  remunerations at the market value of the goods or services at the
  moment of payment (cash-equivalent base per Ley Art. 60), feeding
  that value through the SV-TAX-FR-104 base and the applicable table or
  matrix rule. (LB-005; EVID-104)

## 4. Data Model

Machine-readable sidecars live next to this markdown file:
`withholding_tables.csv` (the operative D.E. 10-2025 periodic + recálculo
tables, verbatim) and `isr_brackets.csv` (the two Art. 37 ANNUAL vintages —
shared with `03_isr-rates-gains.md` §4 — PLUS the 10_/D.E. 25-1992
retention tables as historical vintage de_25_1992, USD rows as printed).
CSV discipline: comma-separated, header row, LF endings; amounts as printed
(thousands separators preserved inside quoted fields — loaders strip
them); empty to_amount = EN ADELANTE (open-ended); rate_pct 0 encodes
SIN RETENCIÓN/EXENTO as printed; the withholding_tables.csv note column
carries [sic] flags and vintage labels per row, while isr_brackets.csv
(brief-exact columns vintage…scope) carries vintage labels in its
vintage/scope columns with the 1992 print anomalies (row-3 offsets ≠
lower bounds, quincenal IV/V overlap at $952.34, semanal V DESDE
$476.12 vs IV HASTA $476.11) transcribed as printed and documented in
OQ-006; column names (from_amount/to_amount/rate_pct/
over_excess_of/fixed_quota) match 03's §4 table headers in story
(Desde/Hasta/% a aplicar/Sobre el exceso de/Más cuota fija de), with the
1992 vintage's FIVE-tramo structure (two 10% rows, anomalous row-3 offsets)
reconciled here as printed — it never conflicts with 03's four-tramo Art.
37 vintages because the vintage key separates them. Note:
`isr_brackets.csv` leaves `valid_from` BLANK for the dl_957_2011
vintage — the D.L. 957-2011 publication/effective date is not pinned in
the corpus and is not invented; the chain gap is covered by OQ-005. Layer semantics: this
file introduces Odoo-side computation/bookkeeping data only (wave default
`odoo`; see §5).

**Withholding tables and engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.withholding.table (new) | decree, valid_from, valid_to, frequency, tramo, from_amount, to_amount, rate, over_excess_of, fixed_quota, note | monetary/select/date | frequency: monthly · quincenal · semanal · june_recalc · december_recalc; seeded from `withholding_tables.csv`; to_amount null = EN ADELANTE; note carries [sic] flags | FR-108, FR-109 |
| l10n_sv.isr.rate.bracket (03 file model) | vintage, tramo, desde, hasta, rate, excess_of, fixed_quota | see 03 §4 | seeded from `isr_brackets.csv` incl. historical de_25_1992 rows (scope column distinguishes annual_liquidation vs retention_monthly/quincenal/semanal) | FR-108 |
| hr.contract | isr_retention_frequency | select | monthly · quincenal · semanal (drives table selection; special periods via FR-115) | FR-109, FR-115 |
| hr.salary.rule / hr.payslip | isr_gross_remunerations, isr_no_gravadas, isr_ss_laboral (ISSS), isr_previsional (AFP/public), isr_retention_base | monetary (computed) | base = gross − no_gravadas − ss_laboral − previsional; employer contributions never netted | FR-104 |
| hr.payslip | isr_tramo, isr_rate_applied, isr_excess_base, isr_fixed_quota | select/monetary | bracket-engine trace per payslip | FR-109 |
| hr.payslip | isr_fixed_deduction_applied | monetary | Tramo II $1,600 proration (working assumption OQ-001: 1,600/12 monthly = 133.33; /24 quincenal = 66.67; /48 semanal = 33.33, matching the decree's exact half/quarter convention) | FR-103 |

**Recálculo engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.withholding.recap (new) | employee, window, cumulative_gravadas, table_tax, prior_retentions, retention_due | monetary/date | window: june (Jan-Jun, minus Jan-May retentions) · december (Jan-Dec, minus Jan-Nov); retention_due = max(0, table_tax − prior_retentions) | FR-110, FR-111 |
| l10n_sv.isr.withholding.recap | excluded_definitive, excluded_multijob_10 | monetary | retención definitiva and Art. 1 h 10% amounts excluded from accumulation | FR-112 |
| l10n_sv.isr.withholding.recap | last_employer_id, constancia_ref | m2o/char | last-employer responsibility; CT 145 constancia intake (15 días hábiles) | FR-113 |
| l10n_sv.isr.withholding.recap | deduction_mode | select | fixed_1600 (≤ $9,100) · art33 (> $9,100) | FR-114 |

**Multi-employer and aguinaldo vintages:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.employee / hr.contract | isr_multi_job_informed_on, isr_designated_table_employer | date · boolean | January or 15-días-hábiles informing; equal-rents designation | FR-118 |
| hr.employee | isr_voluntary_increase_ref | char | DGII formulario reference + copy-to-agent date | FR-119 |
| hr.contract (secondary employments) | isr_flat_10_track | boolean (computed) | non-highest-paying jobs: flat 10%, excluded from recálculo | FR-117 |
| l10n_sv.isr.aguinaldo.exemption (new) | valid_from, valid_to, mode, cap_amount | date/select/monetary | mode: full_exemption (2014-2018) · fixed_cap (2021 $1,100; 2022-2024 $1,500) · two_smm_standing (2025+); SMM value fed by the 16_ payroll-wave source — not stored here | FR-120 |

**Thresholds and non-payroll retention matrix:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.rate.parameter (03 file model) | parameter, value, valid_from, valid_to | monetary | salaried_threshold_9100 · mandatory_declaration_60000 · fixed_deduction_1600 · personal_deduction_800_x2 | FR-103, FR-105, FR-106 |
| account.move.line / account.payment | isr_retention_rule | select null | honorarios_10 · lease_natural_10 · intangibles_natural_10 · intangibles_entity_5 · capital_yields_advances_10 · courts_interest_10 · nonresident_20 · nonresident_transport_5 · nonresident_reinsurer_5 · nonresident_financing_10 · nonresident_related_financing_20 · nonresident_film_tv_5 · tax_haven_25 · deposits_159 · prizes_160 | FR-121..FR-129 |
| account.move.line / account.payment | isr_retention_definitive | boolean | true → excluded from every ISR computation base (`03_isr-rates-gains.md` SV-TAX-FR-076) and from recálculo accumulations | FR-112, FR-126, FR-128 |
| res.partner | isr_retention_profile | select (computed) | drives rule defaulting: independent_natural · lessor_natural · lessor_entity · nonresident · tax_haven · financial_institution | FR-121..FR-128 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living in
the LGPL client. No SaaS rows are introduced in this file: none of these FRs
touch DTE generation/transformation (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are stable
across Odoo 17/18/19/20; version-specific behavior is recorded per row where
a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-102 | odoo | hr.salary.rule (ISR retention) + l10n_sv.isr.withholding.run | retention posts | Satisfies 02-file SV-TAX-FR-040 gate's "effected & entered" side; remittance calendar per 01-file FR-032 (10 días hábiles) |
| FR-103 | odoo | hr.payslip | isr_fixed_deduction_applied | Version regime (D12): $1,600 embedded structurally in recálculo tables (D.E. 10-2025); periodic Tramo II non-embedded — proration working assumption /12 //24 //48 per OQ-001 (SOQ-02), MH guidance pending |
| FR-104 | odoo | hr.salary.rule / hr.payslip | base components | THE base FR (payroll-wave interface): gross − no gravadas − ISSS laboral − AFP/previsional; employer side never netted; base before lookup (ordering OQ-001) |
| FR-105 | odoo | hr.employee / l10n_sv.isr.personal.deduction | deduction lines + proof flags | $800×2; 6-year retention flag; Reglamento Art. 39 enrollment-certificate attachment for schooling (child < 25) |
| FR-106 | odoo | l10n_sv.isr.rate.parameter | thresholds | THE threshold FR (payroll-wave interface): $9,100 mode switch; $60,000 + mismatch flags consumed by 01-file FR-029 (53_ Art. 1 i) online-filing note per 01-file FR-031) |
| FR-107 | odoo | — (informational) | — | ISSS/SSF/AFP information-exchange awareness; keeps contribution identifiers on the model; no computation |
| FR-108 | odoo | l10n_sv.isr.withholding.table / l10n_sv.isr.rate.bracket | CSV seeding | Version regime (D12): retention-decree chain D.E. 25-1992 → D.E. 95-2015 (values absent from corpus, OQ-005) → D.E. 10-2025 operative valid_from 2025-05-08 (MH dating; D.O. pin pending SOQ-03/OQ-002); [sic] fidelity per SOQ-03 (note column) |
| FR-109 | odoo | hr.salary.rule (computation) | bracket engine | Frequency-keyed row lookup; marginal-over-excess + cuota fija; SIN RETENCIÓN on Tramo I |
| FR-110 | odoo | l10n_sv.isr.withholding.recap | june window | Cumulative Jan-Jun − Jan-May retentions; max(0, ·) |
| FR-111 | odoo | l10n_sv.isr.withholding.recap | december window | Cumulative ejercicio − Jan-Nov retentions; December table = Art. 37 vintage B shifted +$1,600 (03-file FR-074 interface — derivation cited, annual table not restated) |
| FR-112 | odoo | l10n_sv.isr.withholding.recap | exclusion fields | Definitive-retention and multi-employer 10% lines filtered from accumulations |
| FR-113 | odoo | l10n_sv.isr.withholding.recap + hr.employee | last_employer, constancia_ref | CT 145 constancia intake; 15 días hábiles from retirement |
| FR-114 | odoo | l10n_sv.isr.withholding.recap | deduction_mode | ≤ $9,100 fixed deduction (table-embedded); > $9,100 Art. 33 path |
| FR-115 | odoo | hr.payslip (special periods) | regla-de-tres engine | Monthly-equivalent salary → monthly retention → period proration; monthly table always the vehicle |
| FR-116 | odoo | hr.payslip line tagging | extraordinary flags | Aguinaldo/vacaciones/bonificaciones/premios/gratificaciones aggregation; same-date vs last-remuneration deduction ordering |
| FR-117 | odoo | hr.contract | isr_flat_10_track | Highest-paying = tables; rest = flat 10% (excluded from recálculo); aggregate below Tramo I → none |
| FR-118 | odoo | hr.employee | informing fields | January / 15-días-hábiles duty; equal-rents designation; two-SMM sanction flag informational (CT collects) |
| FR-119 | odoo | hr.employee | isr_voluntary_increase_ref | DGII formulario on file required before any override applies |
| FR-120 | odoo | l10n_sv.isr.aguinaldo.exemption | vintage rows | Version regime (D12): 2014-2018 full exemption; 2021 $1,100; 2022-2024 $1,500; 2025+ standing 2-SMM with floor DEDUCTED (D.L. 458-2019); SMM value from 16_ payroll-wave feed (concept only here — no value encoded); SOQ-05/OQ-003 re-verification at encoding |
| FR-121 | odoo | account.move.line / account.payment | isr_retention_rule = honorarios_10 | Retention at payment/acreditamiento (CT 154); advances included; agricultural harvest labor excluded |
| FR-122 | odoo | account.move.line / account.payment | lease_natural_10 | Lessor = natural person detection via res.partner |
| FR-123 | odoo | account.move.line / account.payment | intangibles split | 10% natural / 5% entity keyed to lessor profile |
| FR-124 | odoo | account.move.line / account.payment | capital_yields_advances_10 | Firewall against Art. 72's 5% (05_isr-distributions.md §3 — forward ref, to be written); exceptions: already-taxed dividends, ISR-limited labor indemnities |
| FR-125 | odoo | account.move.line (court judgments) | courts_interest_10 | Interest component of ejecutivo judgment payments |
| FR-126 | odoo | account.payment + res.partner | nonresident matrix | 20% definitive + reduced rates as dated parameters; ZF/ISL-exempt payer exception; definitive → excluded from bases (03-file FR-076) |
| FR-127 | odoo | res.partner | tax_haven_25 | CT related-subject/preferential-regime classification consumed; no local haven list invented |
| FR-128 | odoo | account.move.line | deposits_159 | Definitive; consumes 03-file FR-091 small-depositor carve-out (< $25,000 avg monthly balance → no retention) |
| FR-129 | odoo | account.payment | prizes_160 | Raffle/prize payments tagged at disbursement |
| FR-130 | odoo | hr.contract | classification rule | Part-time/horas clase/horas médicos → tables (Reglamento Art. 59); subordination boundary = OQ-004 (Ley Art. 64) |
| FR-131 | odoo | hr.payslip / account.move | in-kind valuation | Market value at payment moment (Ley Art. 60) as cash-equivalent base |

Version-regime notes (D12): FR-108 records the retention-decree chain with
the D.E. 10-2025 vintage dated 2025-05-08 (MH dating; publishing D.O. issue
pending — SOQ-03/OQ-002) and the D.E. 25-1992 historical vintage (effective
1992-03-01; derogation date unpinned — OQ-005). FR-111's December table
derives from the Art. 37 vintage B (D.L. 293-2025, from 2025-05-08 —
03-file FR-074 owns the annual vintages; straddle nuance = 03-file
OQ-009). FR-120 records the aguinaldo vintages (2014-2018 full exemption;
2021 US$1,100; 2022-2024 US$1,500; 2025+ standing 2-SMM — SOQ-05/OQ-003).
FR-103's $1,600, FR-105's $800, FR-106's $9,100/$60,000 are stable
unindexed amounts in the current text (same class as 03-file OQ-003).

## 6. Acceptance Criteria

- **AC-001:** Given a monthly gross remuneration of $700.00 with $21.00
  employee ISSS, $63.00 AFP and a $100.00 non-taxable remuneration item,
  then the retention base = 700.00 − 100.00 − 21.00 − 63.00 = $516.00 →
  Tramo I, SIN RETENCIÓN (FR-104, FR-109).
- **AC-002:** Given a monthly base of $900.00 (2025-05+ vintage), then the
  retention = 20% × (900.00 − 895.24) + 60.00 = $60.95 (Tramo III;
  $900.00 sits above the Tramo II ceiling of $895.24) (FR-109).
- **AC-003:** Given a quincenal base of $500.00, then the retention =
  20% × (500.00 − 447.62) + 30.00 = $40.48; given a semanal base of
  $250.00, then the retention = 20% × (250.00 − 223.81) + 15.00 =
  $20.24 (FR-109).
- **AC-004:** Given a monthly base of $650.00 for a worker projected at
  ≤ $9,100.00/yr, then the Tramo II $1,600 proration applies per the
  OQ-001 working assumption (650.00 − 133.33 = 516.67 → Tramo I,
  SIN RETENCIÓN), whereas without the deduction the base would retain
  10% × (650.00 − 550.00) + 17.67 = $27.67; the assumption flag OQ-001
  is surfaced on the payslip trace (FR-103).
- **AC-005:** Given January-May cumulative gravadas of $6,000.00 with
  prior retentions of $60.00 and a June gravada of $2,500.00, then the
  June recálculo accumulates $8,500.00, the June table yields 20% ×
  (8,500.00 − 5,371.44) + 360.00 = $985.71, and the June retention =
  max(0, 985.71 − 60.00) = $925.71 (FR-110).
- **AC-006:** Given prior retentions of $1,600.00 and a June table result
  of $1,200.00, then the difference is negative and the June retention is
  $0.00 — no refund or negative retention is posted (FR-110).
- **AC-007:** Given ejercicio gravadas of $30,000.00 and Jan-Nov
  retentions of $2,500.00, then the December recálculo applies the
  December table to $30,000.00: 30% × (30,000.00 − 24,457.14) +
  3,462.86 = $5,125.72, and the December retention = max(0, 5,125.72 −
  2,500.00) = $2,625.72 (FR-111).
- **AC-008:** Given a worker with a $5,000.00 definitive-retention
  remuneration and a $20,000.00 multi-employer 10%-retained secondary
  employment, then neither amount enters the June/December recálculo
  accumulation (FR-112).
- **AC-009:** Given a worker changing employers on 10-March, then the
  recálculo responsibility flags to the new (last) employer and the
  computation ingests the prior employer's CT 145 constancia issued
  within 15 días hábiles; absent the constancia the recap is flagged
  incomplete (FR-113).
- **AC-010:** Given employments paying $2,500.00 (A) and $1,200.00 (B)
  monthly bases, then A retains per the monthly table (30% × (2,500.00 −
  2,038.10) + 288.57 = $427.14) and B retains flat 10% × 1,200.00 =
  $120.00 excluded from any recálculo; given two employments of $300.00
  and $200.00 (aggregate below Tramo I), then neither retains (FR-117).
- **AC-011:** Given an aguinaldo of $1,800.00 paid in December 2025 with
  the 2-SMM comercio-y-servicios floor at $400.00 (payroll-wave feed),
  then the exempt floor is $800.00 and the retention base for the excess
  aggregation = 1,800.00 − 800.00 = $1,000.00; given the same aguinaldo
  paid in 2023, then the fixed-cap vintage applies (exempt up to
  $1,500.00 → base $300.00); given 2016, then full exemption (FR-120).
- **AC-012:** Given a $2,000.00 honorarios payment to an independent
  natural person (half of it an advance), then 10% × 2,000.00 = $200.00
  is retained at payment/acreditamiento including the advance portion;
  given otherwise-identical seasonal agricultural harvest labor, then no
  honorarios retention (FR-121).
- **AC-013:** Given a part-time class-hours contract (10 horas clase
  weekly) with subordination, then the remuneration routes to the
  semanal progressive table, never the 10% honorarios rule; the
  subordination-qualifier doubt is carried by OQ-004 (FR-130).
- **AC-014:** Given a payslip dated 2025-04-30 vs one dated 2025-05-30
  at the same base, then the table loader selects the D.E. 10-2025
  vintage only for the latter (valid_from 2025-05-08 per MH dating,
  SOQ-03 flag on the vintage row) and the April lookup is flagged for
  the missing D.E. 95-2015 vintage data (OQ-005) (FR-108).
- **AC-015:** Given a $10,000.00 payment to a non-resident for services
  used in-country, then the retention = 20% × 10,000.00 = $2,000.00
  definitive (excluded from the recipient's ISR bases per 03-file
  FR-076); given the same payment for qualified foreign financing, then
  10% = $1,000.00; given a related-party financing, then 20%;
  given a reinsurer premium, then 5% (FR-126).
- **AC-016:** Given an intangibles royalty of $5,000.00 to a natural
  person, then 10% = $500.00; given the same royalty to an entity, then
  5% = $250.00; given a capital-yield advance of $3,000.00 subject to
  CT 156-B, then 10% = $300.00 posted on the 156-B track with the
  Art. 72 5% firewall asserted (no double counting with
  `05_isr-distributions.md` §3) (FR-123, FR-124).
- **AC-017:** Given a worker's DGII formulario requesting a higher
  retention on file (copy to agent recorded), then the payslip applies
  the elected higher amount; absent the form reference, the override is
  rejected (FR-119).
- **AC-018:** Given a $1,000.00 in-kind salary component (goods) at a
  payment-date market value of $950.00, then the retention computes on
  the $950.00 cash-equivalent base through FR-104 (FR-131).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-02: proration of the Art. 29.7 US$1,600 fixed deduction for quincenal/semanal Tramo II calculations (D.E. 10-2025 Art. 1 e) mandates "serán consideradas en el cálculo" but states no factor) and its ORDERING vs the Art. 1 d) SS/AFP netting. Working assumption implemented by FR-103/FR-104: monthly = 1,600/12 = 133.33; quincenal = 1,600/24 = 66.67; semanal = 1,600/48 = 33.33 (matching the decree's exact half/quarter band convention — semanal bands are /4, not /4.33); ordering = d) netting first (base), then the prorated $1,600 reduction for projected-≤$9,100 Tramo II earners, then table lookup (equivalent to shifting the Tramo II window up; Tramos III/IV already embed the deduction). Check MH guidance before encoding. | no | Takumi S2 + payroll wave | open |
| OQ-002 | SOQ-03: D.E. 10-2025 provenance + fidelity: pin the publishing D.O. issue (vigencia 8 días tras publicación → 2025-05-08 assumed per MH dating) and verify the printed-digit anomalies — June 5,371.44 (exact halving 5,371.43), 12,228.60 (= 12,228.57), cuota 106.20 (= 106.06; largest deviation, deliberate-looking), cuota 1,731.42 (= 1,731.43), semanal IV DESDE 509.53 (= 509.5275), semanal III HASTA 509.52 (= 509.525), quincenal IV DESDE 1,019.06 (= 1,019.055, consistent round-up). CSV transcribes as printed with [sic] notes (01-file OQ-005 kin). | no | Takumi S2 (sources registry) | open |
| OQ-003 | SOQ-05: does a 2025/2026 aguinaldo transitory exist capping the Art. 4.16 2-SMM exemption at a fixed $? The 54_ related-laws tail lists none after D.L. 159-2024 ($1,500) → FR-120 assumes the standing 2-SMM rule for 2025+; the payroll wave re-verifies at encoding time and owns the SMM feed (16_). | no | Takumi payroll wave | open |
| OQ-004 | 04_ OQ-5 carried: Reglamento Art. 59 classifies ALL part-time remunerations (medios tiempos, horas clase, horas médicos) as servicio permanente → tables, but the reformed Ley Art. 64 adds "CON CARÁCTER DE SUBORDINACIÓN O DEPENDENCIA" — does a part-time/hourly arrangement WITHOUT subordination fall outside the tables regime (and route to the 10% honorarios rule)? FR-130 written on Art. 59 + Art. 64 combined. | no | Takumi S2 | open |
| OQ-005 | 53_ OQ-2 carried: retention-decree chain gap — no source fixes the tables between D.E. 25-1992 (effective 1992-03-01; derogation date itself unpinned) and D.E. 95-2015 (repealed by D.E. 10-2025), in particular the post-D.L. 957-2011 alignment; D.E. 95-2015's own table values are absent from the corpus. Historical dated-data completeness only: periods before 2025-05-08 cannot be computed from the corpus. | no | Takumi S2 (sources registry) | open |
| OQ-006 | 10_ OQ-1..5 carried (historical 1992 vintage): row-3 marginal offsets printed ≠ bracket lower bounds (¢2,000.00/¢1,000.00/¢500.00 vs ¢4,104.17/¢2,052.09/¢1,026.05) with discontinuities from row 2; quincenal IV/V overlap (HASTA ¢8,333.33 vs DESDE ¢8,333.01; printed $952.34 both); semanal V DESDE "¢4,1666.01" [sic — USD $476.12 confirms 4,166.01]; gross-vs-net base unstated (resolved for the CURRENT regime by 53_ d); derogation by the later chain unpinned. CSV encodes USD figures as printed; verify against D.O. Nº 34 (20-II-1992) before any historical computation. | no | Takumi S2 (sources registry) | open |
| OQ-007 | MOQ-10 kin: how do ISR retentions (payroll tables and this CT matrix) surface in electronic reporting flows? The DTE reteRenta field is FSEE-only (DG45 §3.1 N°147) and CRE covers IVA retention — the electronic channel for ISR retention reporting (CT Art. 123 annual report; 123-A counter-report) needs confirmation in the fiscal-reporting wave. | no | Takumi S2 (fiscal-reporting wave) | open |
| OQ-008 | Art. 37 vintage-straddle kin (03-file OQ-009) for WITHHOLDING: D.E. 10-2025 (2025-05-08) tracks the D.L. 293-2025 Art. 37 table — for wages earned 1-Jan–7-May-2025 the corpus holds no operative table (D.E. 95-2015 values absent, OQ-005); confirm whether MH mandated the 2015-era tables through 2025-05-07 or an immediate switch, before computing stub-period payrolls. | no | Takumi S2 | open |
