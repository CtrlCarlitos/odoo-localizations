# SV — Taxation — ISR distributions: 5% utilities withholding & earnings register

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for El Salvador's ISR
distributions and deemed-distributions regime — Capítulo III of the Ley ISR
(*Impuesto sobre la Renta a la Distribución de Utilidades*, income tax on
the distribution of profits): the Art. 72 FIVE PERCENT definitive retention
(*retención*) on *utilidades* (profits/utilities) paid or credited by
domiciled subjects to their *socios, accionistas, asociados,
fideicomisarios, partícipes, inversionistas o beneficiarios* (partners,
shareholders, associates, trustees, participants, investors or
beneficiaries), domiciled or not, with the BROAD Art. 72 *utilidades*
definition (gravadas + exentas + no sujetas rents − costs, expenses,
deductions − the ISR of Arts. 37/41) and the payment/credit event catalog
(cash, *títulos valores* (securities), in-kind, debt compensation, loss
application, accounting operations generating availability — dividends,
*participaciones sociales, excedentes, resultados, reserva legal,
ganancias o rendimientos* alike); the no-declaration-when-retained /
separate-declaration-plus-5%-when-not duality; the Art. 73
permanent-establishment track to non-domiciliaries (self-declaration per
Art. 53 inc. 2 when unretained); the Art. 74 capital-reduction retention on
the capitalized/reinvested-earnings portion with profits-first tracing; the
Art. 74-A deemed-distribution loans (partners and related subjects,
preferential-regime/*paraíso fiscal* (tax haven) entities, foreign head
office) with the five no-retention exceptions and the default override
(arrears over six installments or quota term over one year → total
consideration = *renta gravable* (taxable income) + interest
non-deductible); the Art. 74-B no-retention cases with the
autonomous-institutions-subject override and the DGII exemption-proof duty;
the Art. 74-C *Registro de Control de Utilidades* (earnings control
register) — implemented here as the per-shareholder earnings-register data
model with taxed/untaxed profit pools, capitalization/reinvestment events
and capital-reduction tracing; the Art. 25 society-loans-are-dividends rule
feeding both Art. 72 and Art. 74-A; the exempt-society distribution
flow-through (Reglamento Art. 18) and the Reglamento Art. 19 society-income
determination ordering; the reserva-legal distribution interaction with the
society-level 25% separate liquidation (`02_isr-deductions.md`
SV-TAX-FR-063); and the FIREWALL against the CT Art. 156-B 10%
capital-yield/dividend-ADVANCE track (`04_isr-withholding.md`
SV-TAX-FR-124) plus the CT Art. 158-A carve-out pointer (scope = OQ-001).

It does **not** cover: the CT non-payroll retention matrix, the payroll
retention tables and retention mechanics generally
(`04_isr-withholding.md` — its SV-TAX-FR-124 owns the CT 156-B 10%
capital-yield/dividend-advance track kept DISTINCT from this file's Art. 72
5% regime per the firewall FR-136; its SV-TAX-FR-127 owns the CT 158-A 25%
tax-haven retention; its SV-TAX-FR-131 owns the Art. 60 in-kind
market-valuation mechanic consumed here); the Art. 37/41 rates and the
final-withheld exclusion from computation bases (`03_isr-rates-gains.md` —
SV-TAX-FR-074/077 supply the ISR subtracted in the utilidades definition;
SV-TAX-FR-076 is the exclusion interface for retained distributions);
deductions, non-deductibles and the reserva-legal constitution/reduction
register and 25% separate liquidation (`02_isr-deductions.md`
SV-TAX-FR-062/063 — cross-referenced by id, not restated); the filing-duty
and remittance calendar (`01_isr-framework.md` SV-TAX-FR-029/032 — the
ten-*días hábiles* remittance consumed by FR-149); or the CT sanctions
regime (Arts. 226-247 zone — cited informationally via CT 242 b)/c)1)
only). The fiscal-reporting wave consumes this file's earnings-register
entity (`l10n_sv.isr.earnings.register` / `l10n_sv.isr.earnings.event`, §4)
for the CT Art. 123 annual retention report and CT Art. 124
shareholder/dividend list (FR-149).

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated
Ley ISR, current article text incl. reform stamps through Jan-2026) with
reform decrees for changed articles > 03_ (historical consolidation through
D.L. 233-2012; supplies analysis via EVID ids). Reglamento: 04_ = D.E.
101-1992 as consolidated with reforms D.E. 8-1993 / 39-1993 / **117-2001**
(self-documented repeal map — R17); only survivor articles are cited
(Arts. 18-19 carry no repeal marker; Art. 21 DEROGADO (3)). CT: 05_
evidence bank (EVID-063 retention-matrix pointer zone, EVID-064
information returns, EVID-065 sanctions). Every Ley article below was
re-verified in the 54_ consolidation text during this task (54_-verify
rule; page anchors are 54_ pagination from the extraction txt `=== PAGE n
===` markers; stamp keys from the 54_ reform tail): Art. 25 p.14 (txt
lines 743-755), Arts. 72-73 p.45 → Art. 73 closing p.46 (lines 2488-2531),
Art. 74 p.46 (2535-2541), Art. 74-A pp.46-47 (2545-2593), Art. 74-B p.47
(2597-2619), Art. 74-C p.47 (2623-2632). EVID-166 had already verified
Arts. 72-74-C textually unchanged since the 03_ consolidation (no
post-2012 reform touches the 5% regime); Art. 25 bears stamps (8)(10) =
historical reforms, re-read this task.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 72 | Domiciled subjects that pay or credit utilidades to their socios, accionistas, asociados, fideicomisarios, partícipes, inversionistas o beneficiarios shall retain FIVE PERCENT (5%) of such sums; the retention is DEFINITIVE payment of the recipient's ISR, whether domiciled or not; if the retentions were not effected, the recipient declares SEPARATELY from other rents obtained in the ejercicio and pays 5%. Utilidades = remainder of the SUM of rentas gravadas, exentas y no sujetas perceived or accrued in the ejercicio MINUS costs, expenses, deductions and the ISR of Arts. 37 and 41. Paid or credited = when REALLY PERCEIVED by the recipient: cash money, títulos valores, in-kind (en especie), debt compensation, application to losses, or accounting operations generating availability — regardless of denomination: dividends, participaciones sociales, excedentes, resultados, RESERVA LEGAL, ganancias o rendimientos. By its special character this retention PREVAILS over any contrary norm, EXCEPT CT Art. 158-A (stamps (2)(5)(12)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 72 p.45 (EVID-103; verified 54_ txt) |
| LB-002 | Ley ISR, Arts. 73, 53 inc. 2 | Representatives of casas matrices, filiales, sucursales, agencias and other PERMANENT ESTABLISHMENTS that pay or credit utilidades to subjects NOT domiciled in El Salvador shall retain 5% per the preceding article; if the retentions are not effected per this chapter, the non-domiciled subjects adjust to Art. 53 inc. 2 (self-declaration within the legal term) (stamps (12)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 73 pp.45-46; Art. 53 p.40 zone (EVID-103/104) |
| LB-003 | Ley ISR, Art. 74 | Domiciled subjects shall retain 5% on sums paid or credited in CAPITAL OR PATRIMONY REDUCTIONS, in the part corresponding to CAPITALIZATIONS OR REINVESTMENTS OF UTILIDADES; for these effects, the amounts paid or credited by the reduction are considered to correspond to PREVIOUSLY CAPITALIZED UTILITIES UNTIL THEIR CUANTÍA IS EXHAUSTED (profits-first ordering) (stamps (12)(19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 74 p.46 (EVID-103; verified 54_ txt) |
| LB-004 | Ley ISR, Art. 74-A | Domiciled personas jurídicas and entes sin personalidad jurídica shall retain 5% on money or in-kind goods delivered as PRÉSTAMOS, MUTUOS, ANTICIPOS OR ANY OTHER FORM OF FINANCING to: a) their socios, accionistas, asociados, partícipes, fideicomisarios o beneficiarios and subjects RELATED to them per Art. 25 inciso final; b) subjects in low- or no-tax foreign jurisdictions / paraísos fiscales; c) their foreign head office or foreign related establishments. NO retention (and no Art. 25-inciso-final imputation) when: 1) interest contracted at market price or higher; 2) contract between financial institutions regulated by the SSF; 3) contract between public or private entities HABITUALLY dedicated to granting credits; 4) contract between the subjects of 2 and 3; 5) borrower is the State, municipality, institución autónoma, funds or fideicomisos constituted by these, or a corporación/fundación de derecho o utilidad pública. OVERRIDE for case 1: if the borrower falls into arrears (mora) in the payment of MORE THAN SIX CUOTAS (installments) or the term for paying the agreed cuota(s) exceeds ONE YEAR, the TOTAL contracted consideration is renta gravable for the borrower and the accrued interest is NOT deductible as cost or expense for ISR (stamp (19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 74-A pp.46-47 (EVID-103; verified 54_ txt) |
| LB-005 | Ley ISR, Art. 74-B | No retention and no tax under this chapter when: a) the utilidades were already subject to the chapter's retention and remittance in PRIOR distributions; b) utilidades are capitalized in NOMINATIVE SHARES or participaciones sociales of the very society paying them; c) utilidades are REINVESTED by entes sin personalidad jurídica; d) the recipient is the State and its dependencies, municipalities or another ente de derecho público, federaciones y asociaciones cooperativas, and corporaciones o fundaciones de utilidad pública excluded per Art. 6. OFFICIAL AUTONOMOUS INSTITUTIONS (including CEL) ARE SUBJECT to the tax notwithstanding exemption laws. The exemption must be PROVEN by the sujeto pasivo before DGII (stamp (19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 74-B p.47 (EVID-103; verified 54_ txt) |
| LB-006 | Ley ISR, Art. 74-C | Subjects must keep a REGISTRO DE CONTROL DE LAS UTILIDADES per ejercicio containing: the determination of their amount, those paid or credited, their capitalization or reinvestment, and the capital or patrimony reductions — identifying the values per each socio, accionista, asociado, partícipe, fideicomisario o beneficiario — consistent with the accounting (guardará correspondencia con la contabilidad); DGII shall issue the corresponding administrative norms considering the nature of the operations register; breach sanctioned per CT Art. 242 letras b) y c) numeral 1) (stamp (19)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 74-C p.47 (EVID-103; verified 54_ txt; CT 242 via EVID-065) |
| LB-007 | Ley ISR, Art. 25 | The socio or accionista, when determining renta obtenida, shall also include the utilidades REALLY PERCEIVED. Loans the society grants to accionistas or socios, or to their relatives within the FOURTH degree of consanguinity or SECOND of affinity, are considered DISTRIBUTED DIVIDENDS, unless the lending society (printed "prestataria" [sic — read prestamista, lender]) is a bank (stamp (8)). Loans to accionistas or socios, their SPOUSE or said relatives are considered RENTA GRAVABLE, unless the lending society is a bank or another public/private entity habitually dedicated to granting credits (stamp (10) — the inciso final whose related-subject circle Art. 74-A a) consumes) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 25 p.14 (EVID-103; verified 54_ txt lines 743-755) |
| LB-008 | Reglamento ISR (D.E. 101-1992 consolidado), Arts. 18, 19 | Art. 18: where a society is exempted from the tax as such entity by law or legislature-approved contract, the utilidades it distributes are GRAVABLE to the socio in the part derived from non-taxable income — UNLESS the exemption text expressly exempts the partners for profits of the favored activity (inciso added by reform (2)). Art. 19: societies determine their income BEFORE making any profit distribution and AFTER excluding legal-reserve minimums, non-taxable income and other legally-excluded income (survivors; Art. 21 DEROGADO (3)) | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 18-19 p.8 (EVID-136; verified 04_ txt lines 265-276) |
| LB-009 | Código Tributario, Art. 158-A — **POINTER / OQ-SCOPE** | Tax-haven track: subjects of low- or no-tax jurisdictions / paraísos fiscales bear the CT 25% definitive retention (owned by `04_isr-withholding.md` SV-TAX-FR-127); Art. 72's prevalence clause expressly yields to "LO REGULADO EN EL ARTÍCULO 158-A DEL CÓDIGO TRIBUTARIO". The 05_ evidence bank holds only the retention-matrix summary of 158-A — the precise carve-out SCOPE (which 158-A rules displace the 5% and when) is NOT collected: OQ-001; full CT 158-A text must be read from the CT zone before encoding overrides | `sv/sources/05_Codigo_Tributario.pdf` | Art. 158-A pp.88-90 zone (EVID-063 pointer; scope = OQ-001) |
| LB-010 | Código Tributario, Arts. 123, 124 | Annual ISR-retention information return (by January: name, NIT, base and tax per retained subject) and the dividends/shareholder-list information return (by January) — the reporting surfaces that consume this file's earnings-register entity and 5%-retention data; layouts owned by the fiscal-reporting wave | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 123-124 (EVID-064) |
| LB-011 | Ley ISR, Art. 31 (via `02_isr-deductions.md` LB-011) | Reserva-legal interaction: reduction of previously-deducted reserva legal (by capitalization, application to losses, distribution or any circumstance) = renta gravada liquidated SEPARATELY at 25%, with a per-ejercicio constitution/deduction register — the society-level track owned by `02_isr-deductions.md` SV-TAX-FR-063; Art. 72 lists RESERVA LEGAL among the utilidades denominations, so the paid/credited event ALSO enters this file's 5% regime | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 31 pp.32-35 (EVID-099); Art. 72 p.45 (EVID-103) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): no T6-specific dead tracks exist in the corpus — the
pago mínimo regime (void, R21) and the D.L. 969-2024 foreign tracks (dead,
R18) do not reach the distributions chapter; CT Art. 156-B's 10% exceptions
text ("dividends already taxed as such") governs only the 04-file advance
track, never this file's 5% regime; and Art. 25's first inciso prints
"SOCIEDAD PRESTATARIA" [sic] where the lender is meant — transcribed as
printed, read per LB-007.

## 3. Functional Requirements

### 3.1 Art. 72: the 5% definitive retention on utilidades

- **SV-TAX-FR-132:** The system shall compute and effect the 5% retention
  on every payment or credit of utilidades by a DOMICILED subject (the
  retention agent) to its socios, accionistas, asociados,
  fideicomisarios, partícipes, inversionistas or beneficiarios, whatever
  the recipient's domicile; the retention constitutes PAGO DEFINITIVO
  (definitive payment) of the recipient's ISR on those sums — the retained
  utility shall be flagged *retención definitiva* and thereby EXCLUDED
  from the recipient's ISR computation bases per
  `03_isr-rates-gains.md` SV-TAX-FR-076, and the recipient shall owe NO
  declaration for retained amounts. (LB-001; EVID-103)
- **SV-TAX-FR-133:** The system shall determine the *utilidades* base of
  Art. 72 per ejercicio as the REMAINDER of: the SUM of the subject's
  rentas gravadas, exentas y no sujetas (taxable, exempt and
  non-subject rents) perceived or accrued in the ejercicio, MINUS costs,
  expenses and deductions, MINUS the ISR regulated in Arts. 37 and 41
  (the entity's own income tax, consumed from
  `03_isr-rates-gains.md` SV-TAX-FR-074/077 — cited, not restated); the
  resulting utilidades amount feeds the per-shareholder determination
  rows of the earnings register (SV-TAX-FR-144).
  (LB-001; LB-008; EVID-103/136)
- **SV-TAX-FR-134:** The system shall treat utilidades as PAID OR
  CREDITED — triggering the 5% retention — when REALLY PERCEIVED by the
  recipient through any of the Art. 72 events: cash money; *títulos
  valores* (securities); in-kind (*en especie*, valued at market value
  at the payment moment per the Art. 60 mechanic owned by
  `04_isr-withholding.md` SV-TAX-FR-131); *compensación de deudas* (debt
  compensation); *aplicación a pérdidas* (application to losses); or
  accounting operations generating availability — DENOMINATION-AGNOSTIC:
  dividendos, participaciones sociales, excedentes, resultados, RESERVA
  LEGAL, ganancias o rendimientos all enter the same 5% track; each event
  shall be recorded as an earnings-register event line
  (SV-TAX-FR-145). (LB-001; EVID-103)
- **SV-TAX-FR-135:** The system shall support the NO-RETENTION path of
  Art. 72 inciso 2: when utilidades were not subject to the respective
  retentions, the system shall flag the recipient's obligation to
  DECLARE those utilidades SEPARATELY from the other rents obtained in
  the ejercicio and pay the 5% on them (never through the Art. 37
  progressive table or Art. 41 rate — a separate 5% computation track
  per `03_isr-rates-gains.md` SV-TAX-FR-101's slot discipline).
  (LB-001; EVID-103)
- **SV-TAX-FR-136:** The system shall enforce the special-character
  PREVALENCE of the Art. 72 retention over any contrary norm EXCEPT CT
  Art. 158-A (whose 25% tax-haven track is owned by
  `04_isr-withholding.md` SV-TAX-FR-127 and displaces the 5% for
  tax-haven recipients — carve-out scope = OQ-001), and shall assert the
  FIREWALL against the CT 156-B 10% capital-yield/dividend-ADVANCE track
  of `04_isr-withholding.md` SV-TAX-FR-124: a distribution event enters
  EXACTLY ONE track — the Art. 72 5% regime or the 156-B 10% advance
  regime — and no 156-B retention line may consume or shadow the 5%
  regime's base, nor vice versa. (LB-001; LB-009; EVID-103/063)

### 3.2 Art. 73: permanent establishments

- **SV-TAX-FR-137:** The system shall apply the 5% retention when
  representatives of casas matrices, filiales, sucursales, agencias and
  other permanent establishments pay or credit utilidades to subjects NOT
  domiciled in El Salvador; where the retention was not effected per the
  chapter, the system shall flag the non-domiciled recipient's Art. 53
  inciso 2 duty (self-declaration within the legal term) instead of
  computing a retention. (LB-002; EVID-103/104)

### 3.3 Art. 74: capital reductions

- **SV-TAX-FR-138:** The system shall compute the 5% retention on sums
  paid or credited in capital or patrimony REDUCTIONS only on the portion
  corresponding to capitalizations or reinvestments of utilidades,
  applying the statutory PROFITS-FIRST tracing: amounts paid or credited
  by the reduction correspond to previously capitalized utilidades UNTIL
  their cuantía is exhausted (traced from the shareholder's capitalized
  pool in the earnings register, SV-TAX-FR-145), the remainder being
  non-taxable capital corpus. (LB-003; LB-006; EVID-103)

### 3.4 Art. 74-A: deemed-distribution loans

- **SV-TAX-FR-139:** The system shall compute the 5% retention on sums of
  money or in-kind goods delivered by domiciled personas jurídicas or
  entes sin personalidad jurídica as *préstamos, mutuos, anticipos o
  cualquier otra forma de financiamiento* (loans, mutual loans, advances
  or any other form of financing) to: (a) their socios, accionistas,
  asociados, partícipes, fideicomisarios or beneficiarios and the
  subjects related to them per the Art. 25 inciso final circle (spouse
  and relatives within the fourth degree of consanguinity or second of
  affinity — SV-TAX-FR-142); (b) subjects constituted, located or
  domiciled in low- or no-tax foreign jurisdictions or *paraísos
  fiscales*; (c) their foreign head office, or foreign branch, agency or
  other establishment related to it. (LB-004; EVID-103)
- **SV-TAX-FR-140:** The system shall suppress the SV-TAX-FR-139
  retention (and the Art. 25-inciso-final imputation) when the financing
  is granted under any of the five Art. 74-A exceptions: 1) interest
  contracted at market price or HIGHER; 2) contract between financial
  institutions regulated by the Superintendencia del Sistema Financiero;
  3) contract between public or private entities habitually dedicated to
  the granting of credits; 4) contract between the subjects of 2 and 3;
  5) the borrower is the State, a municipality, an *institución
  autónoma* (autonomous institution), funds or fideicomisos constituted
  by these, or a *corporación o fundación de derecho o utilidad pública*
  (public-law or public-utility corporation or foundation).
  (LB-004; EVID-103)
- **SV-TAX-FR-141:** The system shall implement the Art. 74-A override
  of exception 1: when a borrower enjoying the market-rate exception
  falls into arrears (*mora*) in the payment of MORE THAN SIX *cuotas*
  (installments), or the term agreed for paying the agreed cuota(s)
  exceeds ONE YEAR, the system shall (a) treat the TOTAL of the
  contracted consideration as *renta gravable* for the borrower (deemed
  distribution — routed to the 5% regime of SV-TAX-FR-139 on the loan
  record; reading nuance recorded as OQ-003), and (b) flag all accrued
  interest as NON-deductible as cost or expense for ISR determination
  purposes (interface to the non-deductible classifier of
  `02_isr-deductions.md`). (LB-004; EVID-103)

### 3.5 Art. 25: society loans to shareholders and family

- **SV-TAX-FR-142:** The system shall classify loans granted by a
  society to its accionistas or socios, to their *cónyuge* (spouse) or to
  their relatives within the fourth degree of consanguinity or second of
  affinity as DEEMED DISTRIBUTED DIVIDENDS / *renta gravable* — routed to
  the Art. 72 5% track (via SV-TAX-FR-139's Art. 74-A machinery) —
  EXCEPT when the lending society is a bank or another public or private
  entity habitually dedicated to the granting of credits; it shall
  maintain the Art. 25 inciso final related-subject circle (spouse +
  4th/2nd relatives of each socio/accionista) as partner-relation data
  consumed by SV-TAX-FR-139, and shall include really-perceived
  utilidades in the partner's *renta obtenida* view — where the 5% was
  retained, through the definitive-withheld exclusion interface of
  `03_isr-rates-gains.md` SV-TAX-FR-076; where not, through the
  separate 5% declaration of SV-TAX-FR-135 (never the ordinary table).
  (LB-007; LB-004; EVID-103)

### 3.6 Art. 74-B: no-retention cases

- **SV-TAX-FR-143:** The system shall suppress the chapter's retention
  and tax ONLY in the Art. 74-B cases, each grounded in a register trace
  or recipient classification: a) utilidades already subject to the
  chapter's retention and remittance in PRIOR distributions (traced from
  the shareholder's already-taxed pool — SV-TAX-FR-145); b) capitalization
  of utilidades in NOMINATIVE shares or *participaciones sociales* of
  the very society paying them; c) reinvestment of utilidades by *entes
  sin personalidad jurídica* (entities without legal personality); d)
  the recipient is the State and its dependencies, municipalities or
  another *ente de derecho público*, the *federaciones y asociaciones
  cooperativas*, or *corporaciones o fundaciones de utilidad pública*
  excluded per Art. 6; and it shall NOT exempt — however explicit the
  recipient's own exemption law — the official AUTONOMOUS institutions
  (including the Comisión Ejecutiva Hidroeléctrica del Río Lempa, CEL),
  which are SUBJECT to the tax notwithstanding any exemption; every
  claimed exemption shall require a DGII-proof reference on file (the
  *sujeto pasivo* must prove it before DGII). (LB-005; EVID-103)

### 3.7 Art. 74-C: the Registro de Control de Utilidades (earnings register)

- **SV-TAX-FR-144:** The system shall keep, per ejercicio, a *Registro de
  Control de Utilidades* (earnings control register) per each socio,
  accionista, asociado, partícipe, fideicomisario or beneficiario —
  implemented as the `l10n_sv.isr.earnings.register` entity (§4) —
  containing: the DETERMINATION of the utilidades amount (per
  SV-TAX-FR-133), those PAID OR CREDITED (per SV-TAX-FR-134, with the
  retention applied), their CAPITALIZATION OR REINVESTMENT (per
  SV-TAX-FR-143 b/c), and the CAPITAL OR PATRIMONY REDUCTIONS (per
  SV-TAX-FR-138), the register keeping *correspondencia con la
  contabilidad* (consistency with the accounting — enforced by a tie-out
  check against the equity/distribution accounts); the DGII
  administrative norms for the register format are pending and tracked as
  OQ-002; breach is sanctioned per CT Art. 242 letras b) y c) numeral 1)
  (informational flag — the CT sanctions regime governs collection).
  (LB-006; EVID-103/065)
- **SV-TAX-FR-145:** The system shall maintain, inside the earnings
  register, per-shareholder PROFIT POOLS distinguishing: the ALREADY-TAXED
  pool (utilidades on which the chapter's 5% was retained and remitted —
  distributable later without retention per Art. 74-B a), with trace to
  the prior retention events); the NOT-YET-TAXED pool (distributable with
  the 5% retention); and the CAPITALIZED/REINVESTED pool (per
  SV-TAX-FR-143 b/c events, consumed by the profits-first tracing of
  SV-TAX-FR-138 on capital reductions); every distribution event shall
  record its pool designation and its pool effect (taxed draw / untaxed
  draw / untaxed-to-capitalized / capitalized draw), and pool
  consumption ordering for ordinary distributions is a taxpayer
  designation the law does not fix (working assumption: designation
  required, defaulting to the untaxed pool — retention applies unless a
  taxed-pool trace is produced, mirroring the 74-B proof-to-DGII spirit;
  recorded as OQ-004). (LB-001; LB-003; LB-005; LB-006; EVID-103)

### 3.8 Flow-through, determination ordering and interactions

- **SV-TAX-FR-146:** The system shall implement the exempt-society
  distribution flow-through (Reglamento Art. 18): where a society is
  exempted from the tax as such entity by law or by contract approved by
  the Legislature, the utilidades it distributes are GRAVABLE to the
  socio — and enter this file's 5% regime — in the part derived from the
  society's NON-TAXABLE income (the untaxed-origin portion, traced on
  the distribution event), UNLESS the text of the exempting disposition
  EXPRESSLY exempts the partners for profits of the favored activity, in
  which case no part is retained. (LB-008; EVID-136)
- **SV-TAX-FR-147:** The system shall determine society income BEFORE any
  profit distribution and AFTER excluding the legal-reserve minimums,
  the non-taxable income and the other legally-excluded income
  (Reglamento Art. 19) — the determination ordering that feeds the
  SV-TAX-FR-133 utilidades base and keeps the register consistent with
  the society's liquidation. (LB-008; EVID-136)
- **SV-TAX-FR-148:** The system shall co-apply the reserva-legal dual
  track when previously-deducted *reserva legal* (legal reserve) is
  distributed or reduced: (a) the society-level 25% separate liquidation
  on the previously-deducted cuantía, owned by
  `02_isr-deductions.md` SV-TAX-FR-063 (cross-referenced, not
  restated); and (b) this file's 5% retention on the paid/credited event
  (RESERVA LEGAL being an Art. 72 denomination — SV-TAX-FR-134), each
  track computed isolated from the other. (LB-011; LB-001; EVID-099/103;
  02-file SV-TAX-FR-063)
- **SV-TAX-FR-149:** The system shall route the 5% retention to the
  retention-remittance calendar of `01_isr-framework.md` SV-TAX-FR-032
  (ten *días hábiles*, business days, following the period of the
  retention) and shall expose the earnings register and the 5%-retention
  data as the consumption surface for the fiscal-reporting wave's CT
  Art. 123 annual ISR-retention return and CT Art. 124
  dividends/shareholder-list return (layouts owned by that wave —
  forward reference). (LB-010; LB-006; EVID-064/103; 01-file
  SV-TAX-FR-032)

## 4. Data Model

No dated legal tables belong to this file (the single 5% rate is a stable
parameter — no vintages; EVID-166 + this task's 54_ re-read), so no CSV
sidecar is produced; the artifacts of this file are the earnings-register
entities below. **Interface entity for the fiscal-reporting wave:**
`l10n_sv.isr.earnings.register` (the per-ejercicio, per-shareholder
*Registro de Control de Utilidades* aggregate) plus its event ledger
`l10n_sv.isr.earnings.event` (every determination, distribution,
capitalization, reinvestment, reduction and deemed-distribution line).
Layer semantics: this file introduces Odoo-side computation/bookkeeping
data only (wave default `odoo`; see §5).

**Earnings register — the Art. 74-C Registro de Control de Utilidades:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.earnings.register (new) | company_id, ejercicio, partner_id, partner_role | m2o/date/select | partner_role: socio · accionista · asociado · partícipe · fideicomisario · inversionista · beneficiario | FR-144 |
| l10n_sv.isr.earnings.register | utilidades_determined | monetary | the per-ejercicio determination share: Σ gravadas+exentas+no sujetas − costs/gastos/deducciones − ISR Arts. 37/41 (03-file FR-074/077 feed) | FR-133, FR-144 |
| l10n_sv.isr.earnings.register | pool_taxed_balance, pool_untaxed_balance, pool_capitalized_balance | monetary (computed from events) | already-retained (74-B a trace) · not-yet-retained (5% applies) · capitalized/reinvested (74-B b/c; consumed by Art. 74 profits-first) | FR-138, FR-143, FR-145 |
| l10n_sv.isr.earnings.register | accounting_consistent | boolean + check | "guardará correspondencia con la contabilidad": tie-out vs equity/distribution accounts; inconsistency blocks ejercicio close | FR-144 |

**Event ledger:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.earnings.event (new) | register_id, event_date, amount | m2o/date/monetary | every Art. 72-74-B event touching a shareholder's pools | FR-134, FR-144 |
| l10n_sv.isr.earnings.event | event_type | select | determination · paid_credited_cash · paid_credited_titulos · paid_credited_inkind · debt_compensation · loss_application · accounting_operation · capitalization_nominative · reinvestment_entes · capital_reduction · deemed_dividend_loan · exempt_flowthrough · reserva_legal_distribution | FR-134, FR-138..FR-143, FR-146, FR-148 |
| l10n_sv.isr.earnings.event | pool_effect | select | taxed_draw · untaxed_draw · untaxed_to_capitalized · capitalized_draw (Art. 74 profits-first) · new_determination | FR-138, FR-145 |
| l10n_sv.isr.earnings.event | retention_base, retention_amount, retained, definitive | monetary/boolean | retention = 5% × base on untaxed draws, capital-reduction capitalized portions and deemed-dividend loans; definitive → excluded from recipient bases (03-file FR-076) | FR-132, FR-135, FR-138, FR-139 |
| l10n_sv.isr.earnings.event | no_retention_ground, exemption_proof_ref | select/char | ground: 74b_a_prior_taxed · 74b_b_capitalization · 74b_c_reinvestment · 74b_d_recipient · pe_unretained_53_2; proof ref mandatory for 74-B claims (DGII proof duty) | FR-137, FR-143 |
| l10n_sv.isr.earnings.event (capital reductions) | reduction_amount, capitalized_portion, corpus_portion | monetary (computed) | profits-first exhaustion of pool_capitalized_balance; remainder = corpus | FR-138 |
| l10n_sv.isr.earnings.event (flow-through) | untaxed_origin_portion, partners_expressly_exempt | monetary/boolean | Reglamento Art. 18: 5% only on the untaxed-origin part unless the exemption text expressly covers partners | FR-146 |

**Partner classification, loans and retention posting:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner | isr_74b_recipient_class | select | state_dependencies · municipality · public_law_entity · coop_federation · art6_public_utility (no retention) · autonomous_official_institution (RETAINED — incl. CEL) · other | FR-143 |
| res.partner | isr_art25_related_circle_ids | m2m | spouse + relatives 4th consanguinity / 2nd affinity of socios/accionistas (Art. 25 inciso final circle) | FR-139, FR-142 |
| res.company | isr_exempt_society, exemption_covers_partners | boolean | exempt by law/Legislature contract; partners covered only if text expressly exempts them (04_ Art. 18) | FR-146 |
| account.move / loan record | isr_74a_loan + interest_rate, market_rate_evidence, counterparty_class, quota_term, mora_cuotas | boolean + fields | 74-A tracking: market-or-better test; SSF-regulated / habitual-credit / inter-institutional / State-borrower exceptions; mora >6 cuotas or quota-term >1y | FR-139, FR-140, FR-141 |
| account.move.line (interest) | isr_interest_nondeductible | boolean | set on the FR-141 collapse; blocks ISR deduction (02-file non-deductible classifier kin) | FR-141 |
| account.move.line / account.payment | isr_retention_rule (extension of the 04-file catalog) | select + values | distributions_5 · deemed_dividend_loan_5 · capital_reduction_5 — extends 04's catalog; capital_yields_advances_10 NEVER set on these lines (firewall) | FR-132, FR-136, FR-138, FR-139 |
| account.move.line / account.payment | isr_retention_definitive (04-file model) | boolean | true on the 5% tracks (pago definitivo) → excluded from every recipient ISR base | FR-132 |
| l10n_sv.isr.rate.parameter (03-file model) | distributions_5 | rate | the single 5% parameter; stable text — no vintage rows | FR-132..FR-139 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living in
the LGPL client. No SaaS rows are introduced in this file: none of these FRs
touch DTE generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are stable
across Odoo 17/18/19/20; version-specific behavior is recorded per row where
a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-132 | odoo | l10n_sv.isr.earnings.event + account.move.line | retained, definitive | 5% at payment/credit; definitive flag feeds 03-file FR-076 exclusion; recipient no-declaration when retained |
| FR-133 | odoo | l10n_sv.isr.earnings.register | utilidades_determined | Base = Σ gravadas+exentas+no sujetas − costs − ISR 37/41 (03-file FR-074/077 consumption interface); per-ejercicio per-shareholder rows |
| FR-134 | odoo | l10n_sv.isr.earnings.event | event_type catalog | Real-perception trigger; in-kind valued via 04-file FR-131 (Art. 60) market-value mechanic; reserva legal included as denomination |
| FR-135 | odoo | l10n_sv.isr.earnings.event + filing flag | retained = false | Separate 5% declaration flag on the recipient; never routes to Art. 37 table / Art. 41 rate (03-file FR-101 slot discipline) |
| FR-136 | odoo | retention-rule guard | isr_retention_rule check | Prevalence asserted except CT 158-A (04-file FR-127 displaces for tax-haven recipients — scope OQ-001); mutual exclusion with 04-file FR-124's capital_yields_advances_10 (firewall) |
| FR-137 | odoo | l10n_sv.isr.earnings.event (PE payer) | pe branch flag | 5% for non-domiciled recipients of PE distributions; unretained → Art. 53 inc. 2 self-declaration flag |
| FR-138 | odoo | l10n_sv.isr.earnings.event | capitalized_portion, corpus_portion | Profits-first exhaustion of pool_capitalized_balance; 5% only on the capitalized-earnings portion |
| FR-139 | odoo | account.move / loan + res.partner | isr_74a_loan, related-circle m2m | Money or in-kind financing to partners+circle / paraíso entities / foreign head office; 5% at delivery |
| FR-140 | odoo | account.move / loan | exception validator | Five exceptions: market-or-better interest (evidence field), SSF-regulated institutions, habitual credit entities, inter-institutional, State/municipality/autónoma/funds/corporación-beneficiaries |
| FR-141 | odoo | loan + account.move.line | mora tracking, isr_interest_nondeductible | Mora >6 cuotas or quota-term >1y → total consideration renta gravable (5% regime per FR-139; nuance OQ-003) + interest deduction blocked |
| FR-142 | odoo | res.partner + loan classification | Art. 25 circle | Society loans to socios/spouse/4th-2nd relatives = deemed dividends unless lender is bank/habitual-credit entity; feeds FR-139(a) |
| FR-143 | odoo | res.partner + l10n_sv.isr.earnings.event | no_retention_ground, exemption_proof_ref | 74-B a-d with register traces; autonomous official institutions NEVER exempt (incl. CEL); DGII proof ref required |
| FR-144 | odoo | l10n_sv.isr.earnings.register | all | THE Art. 74-C register entity (fiscal-reporting-wave interface); accounting tie-out check; DGII format norms pending (OQ-002); CT 242 b)/c)1) sanction informational |
| FR-145 | odoo | l10n_sv.isr.earnings.register / .event | pools + pool_effect | Taxed/untaxed/capitalized pools; designation default = untaxed pool unless taxed trace produced (OQ-004) |
| FR-146 | odoo | res.company + l10n_sv.isr.earnings.event | flow-through fields | Exempt society: 5% on untaxed-origin part; express-partner-exemption carve-out |
| FR-147 | odoo | computation ordering | — | Income determined before distributions, after reserva-legal minimums and exclusions; feeds FR-133 |
| FR-148 | odoo | l10n_sv.isr.earnings.event + separate track | reserva_legal_distribution | Dual track: 25% society separate liquidation (02-file FR-063, cross-ref) + 5% shareholder retention; isolated computations |
| FR-149 | odoo | retention remittance + report surface | CT 123/124 exposure | 01-file FR-032 ten-días-hábiles calendar; register/retention data exposed for the fiscal-reporting wave (layouts there) |

Version-regime notes (D12): no dated vintages exist in this file — the 5%
rate and the Arts. 72-74-C structure are textually stable in the 54_
consolidation (EVID-166 delta verification + this task's 54_ re-read of
Arts. 25, 72, 73, 74, 74-A, 74-B, 74-C); the only temporal gates are the
CT 158-A carve-out scope (OQ-001) and the pending DGII register norms
(OQ-002), both configuration-time dependencies rather than period
vintages.

## 6. Acceptance Criteria

- **AC-001:** Given a domiciled society with rentas gravadas of $120,000
  (≤ $150,000 → 25% rate per `03_isr-rates-gains.md` FR-077), no
  exentas/no sujetas rents and costs/expenses/deductions of $60,000
  (renta imponible $60,000 → ISR Art. 41 at 25% = $15,000, consumed from
  the 03-file rate FRs), then utilidades = 120,000 − 60,000 − 15,000 =
  $45,000, and a distribution to Partner A (60%) and Partner B (40%)
  retains 5% × 27,000 = $1,350.00 and 5% × 18,000 = $900.00
  respectively, both definitive and excluded from the recipients' ISR
  bases (FR-132, FR-133).
- **AC-002:** Given the same society with rentas gravadas of $250,000 and
  deductions of $150,000 (renta imponible $100,000 → 30% rate per
  FR-077, ISR = $30,000), then utilidades = 250,000 − 150,000 − 30,000 =
  $70,000 and a full distribution retains 5% × 70,000 = $3,500.00
  (FR-133).
- **AC-003:** Given an in-kind distribution of equipment with a
  payment-moment market value of $10,000, then the retention = 5% ×
  10,000 = $500.00 computed on the cash-equivalent value (FR-134;
  04-file FR-131 valuation mechanic).
- **AC-004:** Given a $8,000 credit of utilidades applied against a
  partner's receivable (compensación de deudas), then the retention = 5%
  × 8,000 = $400.00 posted at the compensation event (FR-134).
- **AC-005:** Given a $50,000 dividend on which no retention was
  effected, then the recipient's flag requires a SEPARATE declaration
  with 5% × 50,000 = $2,500.00, and the amount never enters the Art. 37
  progressive table (FR-135).
- **AC-006:** Given an entity paying a CT 156-B capital-yield advance of
  $3,000 and an Art. 72 dividend of $10,000, then the advance retains
  10% × 3,000 = $300.00 on the 04-file FR-124 track and the dividend
  retains 5% × 10,000 = $500.00 on this file's track — the two lines
  carry different retention rules and neither base shadows the other
  (FR-136).
- **AC-007:** Given a permanent establishment paying $12,000 of utilidades
  to a non-domiciled subject, then the retention = 5% × 12,000 =
  $600.00; given the same payment unretained, then the event flags the
  recipient's Art. 53 inc. 2 self-declaration instead of a retention
  (FR-137).
- **AC-008:** Given a partner whose capital is reduced by $30,000 and
  whose capitalized-earnings pool holds $18,000 from prior
  capitalizations, then the retention = 5% × 18,000 = $900.00 and the
  remaining $12,000 passes as corpus with no retention (profits-first
  tracing) (FR-138, FR-145).
- **AC-009:** Given a $20,000 society loan to a shareholder at
  below-market interest, then the delivery retains 5% × 20,000 =
  $1,000.00 (no exception applies) (FR-139, FR-140).
- **AC-010:** Given a $20,000 loan to a partner at market interest with
  $4,000 contracted interest (exception 1 → no retention at delivery)
  and the partner later in arrears on more than six cuotas, then the
  collapse treats the total contracted consideration $24,000 as renta
  gravable (deemed distribution; 5% regime re-engaged per FR-141 →
  $1,200.00) and flags the accrued interest as non-deductible
  (FR-141; reading nuance OQ-003).
- **AC-011:** Given a $50,000 financing granted to a State borrower
  (exception 5), then no 5% retention is computed at delivery
  (FR-140).
- **AC-012:** Given a $5,000 loan by a non-bank, non-habitual-credit
  society to a shareholder's spouse, then the loan is a deemed dividend
  and retains 5% × 5,000 = $250.00 through the Art. 25/74-A track; given
  the lender is a habitual-credit entity, then no deemed dividend and no
  retention (FR-142).
- **AC-013:** Given a $40,000 capitalization of utilidades in nominative
  shares of the same society, then no retention is computed and the
  register records an untaxed-to-capitalized event raising the
  shareholder's capitalized pool by $40,000 for later Art. 74 tracing
  (FR-143, FR-145, FR-138).
- **AC-014:** Given a $10,000 distribution to a municipality, then no
  retention applies with the 74-B d) ground and a DGII-proof reference
  recorded; given the same distribution to an official autonomous
  institution (exempt by its own law), then the retention = 5% × 10,000
  = $500.00 — the autonomous-institution override asserts (FR-143).
- **AC-015:** Given an exempt society distributing $30,000 of which
  $12,000 traces to non-taxable income origin, then the partner-side
  retention = 5% × 12,000 = $600.00 on the untaxed-origin portion; given
  the exemption text expressly exempts partners, then no retention
  (FR-146).
- **AC-016:** Given a $10,000 distribution of previously-deducted reserva
  legal, then the society posts the 25% separate liquidation 25% ×
  10,000 = $2,500.00 (02-file FR-063 track) AND the shareholder
  retention 5% × 10,000 = $500.00 (this file's track), the two
  computations isolated from each other (FR-148).
- **AC-017:** Given a $10,000 distribution designated from the
  shareholder's already-taxed pool with trace to prior retention events,
  then no retention is computed with ground 74-B a); given the same
  amount designated from the untaxed pool (the default), then the
  retention = 5% × 10,000 = $500.00 (FR-145, FR-143).
- **AC-018:** Given a $10,000 distribution to a subject of a tax-haven
  jurisdiction, then the Art. 72 5% yields to the CT 158-A track: the
  04-file FR-127 rule computes 25% × 10,000 = $2,500.00 and this file's
  5% is displaced (prevalence exception; scope OQ-001) (FR-136).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | CT 158-A carve-out scope: Art. 72's prevalence expressly yields to CT Art. 158-A, but the 05_ evidence bank holds only the retention-matrix summary (EVID-063: tax-haven subjects → 25%). Which 158-A rules displace the 5% (only the 25% haven rate? the ZF/ISL payer exceptions? reduced rates?), for which recipient classifications and payer classes, is NOT collected — per wave instruction the scope is an OQ, not an FR; read the full CT 158-A text from the 05_ CT zone before encoding the FR-136 override beyond the 25% case. | no | Takumi S2 (CT zone pass) | open |
| OQ-002 | DGII administrative norms for the Registro de Control de Utilidades (Art. 74-C empowers DGII to issue them "considering the nature of the operations register"): no resolution/norm appears in the corpus — register layout, filing and format unknown; `l10n_sv.isr.earnings.register`/`.event` (§4) encode the statutory minimum fields; conform when DGII publishes. | no | Takumi S2 (sources registry) | open |
| OQ-003 | Art. 74-A override mechanics: when the market-rate exception collapses (mora > 6 cuotas or quota-term > 1 year), the law makes the TOTAL contracted consideration renta gravable for the borrower and the interest non-deductible — FR-141 re-engages the 5% regime on the total (principal + contracted interest). Two readings to confirm with DGII practice: (a) 5% on the total as a single deemed distribution (FR-141/AC-010 as written), vs (b) renta-gravable inclusion at the recipient with the retention only on the loan principal. Also: is the >6-cuota mora counted consecutively or cumulatively, and does "plazo de la o las cuotas > 1 año" measure single-installment terms or the overall grace period? | no | Takumi S2 | open |
| OQ-004 | Pool-consumption ordering for ORDINARY distributions: the law fixes profits-first only for capital reductions (Art. 74); for ordinary distributions Art. 74-B a) merely excepts prior-taxed profits. FR-145 working assumption: designation required, defaulting to the untaxed pool (retention applies unless a taxed-pool trace is produced — mirroring the 74-B proof-to-DGII spirit). Confirm no DGII criterion mandates taxed-first consumption before encoding. | no | Takumi S2 | open |
| OQ-005 | Art. 25 inciso overlap: inciso 1 (stamp (8)) deems loans to socios/accionistas or their 4th-2nd relatives "dividendos distribuidos" with a bank-only exception (printed "sociedad prestataria" [sic]); inciso 2 (stamp (10), the "inciso final" consumed by Art. 74-A) deems loans to socios/accionistas, spouse and relatives "renta gravable" with a bank-or-habitual-credit exception. FR-142 applies the broader inciso-2 exception set uniformly through the 74-A machinery; confirm the narrower inciso-1 set is not intended to survive separately for the dividend characterization. | no | Takumi S2 | open |
| OQ-006 | Electronic reporting surface kin of 04-file OQ-007 (MOQ-10): how the 5% distributions retention surfaces in electronic reporting (CT Art. 123 annual retention report; CT Art. 124 dividend/shareholder list; reteRenta DTE field is FSEE-only per DG45 §3.1 N°147) — layouts and channels owned by the fiscal-reporting wave, which consumes `l10n_sv.isr.earnings.register`/`.event` per FR-149. | no | Takumi S2 (fiscal-reporting wave) | open |
| OQ-007 | Exemption-proof artifact (Art. 74-B final inciso: exemptions "comprobada por el sujeto pasivo ante la DGII"): which document class satisfies the proof on file (DGII resolution, exoneración certificate, other) — the register stores a free reference (`exemption_proof_ref`); define the accepted document types when DGII guidance is obtained. | no | Takumi S2 | open |
