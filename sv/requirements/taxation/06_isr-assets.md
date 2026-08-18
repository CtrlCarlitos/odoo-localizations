# SV — Taxation — ISR fixed assets: depreciation, software amortization & the depreciation register

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for El Salvador's ISR fixed-asset
regime — the Art. 30 *depreciación* (depreciation) deduction and the Art. 30-A
software *amortización* (amortization): the deduction of the acquisition or
fabrication cost of goods exploited by the taxpayer for computable-renta
generation, with goods consumed or exhausted within twelve months of use
deducting their TOTAL cost in the *ejercicio* (fiscal period) of greater use as
declared by the taxpayer; the >12-month annual *cuota* (quota) computed as a
fixed and constant percentage over the value subject to depreciation with the
category LEGAL MAXIMA — *edificaciones* (buildings) 5%, *maquinaria*
(machinery) 20%, *vehículos* (vehicles) 25%, *otros bienes muebles* (other
movable goods) 50% — as defaults, adoptable lower, and immutable without DGII
authorization; the depreciable-value caps (imported machinery that enjoyed IVA
exemption at import capped at the DGII-registered import value; used machinery
and movable goods capped at the new-good price adjusted by years of life —
1 year 80% / 2 years 60% / 3 years 40% / 4 years and more 20% — prices subject
to *fiscalización* (tax audit)); the *maquinaria* classification definition
(Reglamento Art. 35); the timing mechanics (part-year proportional quota for
goods not spanning a complete ejercicio; the D.L. 192-2018 seasonal-activity
*interpretación auténtica* (authentic interpretation) granting the FULL annual
quota to seasonal activities — *cafetalero/cañero* (coffee-grower/
sugar-cane-grower) as open-list exemplars — implemented as a per-company /
per-asset configuration flag; capitalization of depreciation into the cost of
goods under production, construction, manufacture, extraction or
*lotificación* (land parcelling), deducted only when the built goods are
sold); the governance blocks (no revaluation; owner-only plus in-use
requirement with the *usufructuario* (usufructuary) rule; land and inventory
never depreciable with the land/building value-separation duty; mixed
gravadas/no-gravadas use prorated per the Art. 28 final-inciso allocator owned
by `02_isr-deductions.md`; no catch-up of missed or deficient quotas;
full-redeemption stop); the evidence rules (*documentos de pago idóneos*
(suitable payment documents); real-estate transfer tax never part of
acquisition cost); the Art. 30-A software mirror (25% maximum, used-software
caps, own-produced double-deduction ban, CT Arts. 156-A/158 retention
reservation); and the Reglamento Art. 84 MANDATORY per-asset depreciation
register with its verbatim minimum field list — *especificación del bien,
valor a depreciar, fecha en que comienza a usarse, período de vida útil,
mejoras, adiciones, cuota de depreciación, saldo por depreciar, retiro,
enajenación* (asset specification, depreciable value, in-use start date,
useful-life period, improvements, additions, depreciation quota, balance to
depreciate, retirement, disposal) — plus the data the asset's nature demands,
implemented as the ISR field set and per-asset history on the asset model.
This file also owns the accumulated-admitted-depreciation ledger and the
retirement/disposal register events that feed the capital-gain interface of
`03_isr-rates-gains.md` (SV-TAX-FR-080/081/083: per-transaction result,
*costo básico* = cost − accumulated admitted depreciation, holding-period
counting — cited by id, never restated here).

It does **not** cover: the capital-gain computation itself, the
*habitualidad* gate, the capital-loss ledger and the 12-month routing
(`03_isr-rates-gains.md` §3 — its SV-TAX-FR-079..085 own them; this file only
feeds FR-080/081/083 with register data); the Art. 28 necessary-cost gate and
the gravadas/total pro-rata allocator with the D.L. 969-2024 carve-out
(`02_isr-deductions.md` SV-TAX-FR-034..037 — consumed here for mixed-use
assets, not restated); the repair-vs-improvement classifier
(`02_isr-deductions.md` SV-TAX-FR-047 — this file receives its
capitalization inflows as register *mejoras/adiciones*); the CT Arts. 156-A /
158 retentions on intangibles reserved by Art. 30-A's final clause
(`04_isr-withholding.md` SV-TAX-FR-123/126 own them); the general deduction
gate and non-deductible catalog (`02_isr-deductions.md` §3); or the
depreciation/expense ACCOUNT structure (chart-of-accounts wave — this file
owns the asset register and computation rules; account codes are that wave's
surface). The fiscal-reporting wave and Task 7's index consume this file's
register field model (§4) as the depreciation-register interface.

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated
Ley ISR, current article text incl. reform stamps through Jan-2026) with
reform decree 57_ (D.L. 192-2018, *interpretación auténtica* of Art. 30.1
inciso 2º) for the changed article > 03_ (historical consolidation through
D.L. 233-2012; supplies analysis via EVID ids). Reglamento: 04_ = D.E.
101-1992 as consolidated with reforms D.E. 8-1993 / 39-1993 / **117-2001**
(self-documented repeal map — R17); only survivor articles are cited (Art. 84
is the SOLE survivor of the books/records/inventories regime — Arts. 81-83,
85-101 derogated by reform (3); Art. 35 carries no repeal marker). Every Ley
article below was re-verified in the 54_ consolidation text during this task
(54_-verify rule; page anchors are 54_ pagination from the extraction txt
`=== PAGE n ===` markers; stamp keys from the 54_ reform tail, txt lines
3241-3328): Art. 30 begins p.27 ("Depreciación" heading, txt line 1474);
incisos 1º-2º p.27 (lines 1476-1487); inciso 3º num. 1 pp.27-29 (lines
1489-1590) with the D.L. 192-2018 authentic-interpretation block embedded
pp.27-29 (lines 1499-1582); num. 2 pp.29-30 (lines 1592-1624); num. 3 p.30
(lines 1626-1659); nums. 4-10 pp.30-31 (lines 1661-1703); Art. 30-A pp.31-32
(lines 1705-1772). Stamps borne: Art. 30 → (2) D.L. 250-1992, (7) D.L.
841-1996, (14) D.L. 496-2004; Art. 30-A → (15) D.L. 646-2005 (the decree that
ADDED the article). D.L. 192-2018 is not a numbered stamp: its text is
incorporated VERBATIM inline in the 54_ consolidation. The 54_ reform tail
(through D.L. 499-2026, 14-Jan-2026) was checked this task: no later reform
touches Arts. 30 or 30-A. Reglamento anchors re-read this task in the 04_ txt:
Art. 35 (lines 438-441, p.12), Art. 84 (lines 553-559, p.16) with the
derogated neighbors visible at lines 550-552/560-563.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 30 incisos 1º-2º | Deductible from renta obtenida: the acquisition or fabrication cost of goods exploited by the taxpayer for the generation of computable renta. Goods consumed or exhausted within a period NOT GREATER THAN TWELVE MONTHS of use or employment in renta production: their TOTAL cost is deducted in the ejercicio in which their use was GREATER, as declared by the taxpayer (stamps (7)(14)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 30 incisos 1º-2º p.27 (EVID-101 loc pp.26-28; verified 54_ txt lines 1476-1487) |
| LB-002 | Ley ISR, Art. 30 inciso 3º num. 1 + D.L. 192-2018 (interpretación auténtica, incorporated inline) | The deduction proceeds for the LOSS OF VALUE goods and installations suffer through use in the renta-gravable-producing source. Goods whose use in gravable-renta production does not span a COMPLETE ejercicio: only the part of the annual quota PROPORTIONALLY corresponding as a function of the time the good has been in use generating renta or conserving the source is deductible. INTERPRETACIÓN AUTÉNTICA (D.L. 192): in SEASONAL activities, such as those of the cafetalero and cañero sectors, the use or employment of machinery and equipment in gravable-renta production is understood as realized over the COMPLETE ejercicio, the TOTAL annual depreciation quota being deductible during the useful life of such goods and per the deductibility rules applicable to COSTO DE VENTA (cost of sales). Goods employed in the production, construction, manufacture or extraction of other goods, likewise in the lotificación of inmuebles: the annual quota (or corresponding proportion) FORMS PART OF THE COST of those goods; the taxpayer is only entitled to deduct from renta obtenida the depreciation corresponding to the goods SOLD in the respective ejercicio or period (stamps (7)(14)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` + `sv/sources/57_InterpAut_Art30_DL192_DO_2018-12-12.pdf` | 54_ Art. 30 num. 1 pp.27-29 (EVID-101; verified 54_ txt lines 1489-1590 incl. D.L. 192 block 1499-1582); 57_ Arts. 1-3 p.1-2 (EVID-169) |
| LB-003 | Ley ISR, Art. 30 inciso 3º num. 2 a)-b) | The value SUBJECT TO DEPRECIATION shall be the TOTAL COST OF THE GOOD, save: a) imported machinery that enjoyed IVA (transfer-tax) exemption at import → as MAXIMUM the value recorded by the Dirección General at the moment of import; b) used machinery or movable goods → the MAXIMUM value subject to depreciation shall be the NEW-good price at the moment of acquisition, adjusted per years of life: 1 año 80% / 2 años 60% / 3 años 40% / 4 años y más 20%. The prices of these goods are SUBJECT TO FISCALIZACIÓN (stamp (7)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 30 num. 2 pp.29-30 (EVID-101; verified 54_ txt lines 1592-1624) |
| LB-004 | Ley ISR, Art. 30 inciso 3º num. 3 | The taxpayer determines the depreciation corresponding to the ejercicio by applying a FIXED AND CONSTANT percentage over the value subject to depreciation. The MAXIMUM percentages permitted: EDIFICACIONES 5% / MAQUINARIA 20% / VEHÍCULOS 25% / OTROS BIENES MUEBLES 50%. Once a percentage is adopted for a given good, it may NOT be changed without authorization of the Dirección General de Impuestos Internos; if changed, the depreciation is NOT deductible. Outlays really made for the acquisition, creation, elaboration or construction of the goods must be demonstrated by DOCUMENTOS DE PAGO IDÓNEOS. In NO case is the real-estate transfer tax part of the acquisition cost of inmuebles for depreciation purposes (stamps (2)(7)(14)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 30 num. 3 p.30 (EVID-101; verified 54_ txt lines 1626-1659) |
| LB-005 | Ley ISR, Art. 30 inciso 3º nums. 4-10 | 4) Valuation or revaluation of goods in use is NOT applicable to this deduction. 5) Depreciation claimable ONLY over OWNED goods while in use producing gravable income; where one person holds the usufruct and another the naked ownership, the USUFRUCTUARY depreciates while the usufruct lasts. 6) Taxpayers shall keep a DETAILED depreciation register — save those not obliged by law to keep formal accounting or records; the Reglamento regulates the form of keeping it. 7) Quotas missed or under-charged in prior years may NOT be accumulated to later years' quotas. 8) NOT depreciable: merchandise or inventory existences, nor rural or urban land — EXCEPT what is built on it; for edificaciones the taxpayer shall SEPARATE in the accounting the land value and the building value. 9) Goods used at the same time in gravable and non-gravable production (or non-renta): depreciation admitted ONLY in the proportion of gravable income per Art. 28 final inciso. 10) The depreciable good is REDEEMED for tax purposes within the term resulting from the fixed percentage; NO depreciation deduction on goods already fiscally redeemed (stamp (14) on nums. 8-10) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 30 nums. 4-10 pp.30-31 (EVID-101; verified 54_ txt lines 1661-1703) |
| LB-006 | Ley ISR, Art. 30-A (added by D.L. 646-2005) | Deductible from renta obtenida via amortization: the acquisition or PRODUCTION cost of computer programs (software) used for gravable-renta production or source conservation, applying a FIXED AND CONSTANT percentage of a MAXIMUM 25% annual over the production or acquisition cost, without prejudice to: a) own-produced programs for own use — the capitalized cost is NOT deductible when the outlays composing it were deducted in a PRIOR period; b) valuation or revaluation not applicable; c) USED software — maximum amortizable value = the NEW-program price at acquisition adjusted: 1 año 80% / 2 años 60% / 3 años 40% / 4 años 20%, prices subject to fiscalización; d) part-year use → only the proportional part of the annual quota; e) only OWNED software while in use producing gravable income; f) mixed gravable/non-gravable use → only the gravable proportion per Art. 28 final inciso; g) missed amortization may NOT be accumulated to later years; h) the percentage may NOT be changed without authorization of the Administración Tributaria (Tax Administration). All without prejudice to CT Arts. 156-A and 158 (stamp (15)) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 30-A pp.31-32 (EVID-102; verified 54_ txt lines 1705-1772) |
| LB-007 | D.L. 192-2018 (interpretación auténtica del Art. 30.1 inciso 2º), Arts. 1-3 | Art. 1: "en las actividades estacionales, como las que realizan el sector cafetalero y cañero, el uso o empleo de maquinaria y equipo en la producción de la renta gravada se entiende realizado en el ejercicio de imposición completo, siendo deducible el total de la cuota de depreciación anual durante la vida útil de tales bienes y conforme a las reglas de deducibilidad aplicables al costo de venta." Art. 2: the interpretation is incorporated into the Art. 30.1 inciso-segundo text FROM ITS VIGENCIA. Art. 3: vigencia eight days after publication (D.O. N° 233 T.421, 12-XII-2018 → effective **2018-12-20**) | `sv/sources/57_InterpAut_Art30_DL192_DO_2018-12-12.pdf` | Arts. 1-3 pp.1-2 (EVID-169; incorporated verbatim in 54_ pp.27-29) |
| LB-008 | Reglamento ISR (D.E. 101-1992 consolidado), Art. 84 | "Las depreciaciones de los bienes dedicados a la producción de ingresos computables se anotarán minuciosamente y detalladamente por medio de registros pormenorizados, debiendo contener, por lo menos, la siguiente información: ESPECIFICACION DEL BIEN, VALOR A DEPRECIAR, FECHA EN QUE COMIENZA A USARSE, PERIODO DE VIDA UTIL, MEJORAS, ADICIONES, CUOTA DE DEPRECIACION, SALDO POR DEPRECIAR, RETIRO, ENAJENACION, y todos los datos que la naturaleza del bien exija." SOLE SURVIVOR of the books/records/inventories regime (Arts. 81-83, 85-101 DEROGADO (3) D.E. 117-2001) — the "reglamento" form the Ley Art. 30 num. 6 calls for; live legal basis | `sv/sources/04_Reglamento_ISR.pdf` | Art. 84 p.16 (EVID-145; verified 04_ txt lines 553-559, derogated neighbors 550-552/560+) |
| LB-009 | Reglamento ISR, Art. 35 | "Para los efectos del inciso 2º literal b) del Nº 3 del Art. 30 de la ley [sic — printed cross-ref; the definitional scope maps to the maquinaria category of the current Art. 30 num. 3 rates and the num. 2 b) used-machinery caps], se entiende por maquinaria todo aparato o conjunto de piezas que sirve para la elaboración de productos o para producir determinados efectos, tales como trituradores de piedra, excavadoras, tornos empleados en mecánica y fundición, y otros semejantes." | `sv/sources/04_Reglamento_ISR.pdf` | Art. 35 p.12 (EVID-142; verified 04_ txt lines 438-441) |
| LB-010 | Ley ISR, Art. 14 (via `03_isr-rates-gains.md` LB-006) — **POINTER** | Capital-gain basis linkage: *costo básico* for goods acquired *a título oneroso* = acquisition cost MINUS the *depreciaciones realizadas y admitidas* (depreciations effected and admitted under the law) — the accumulated-admitted-depreciation figure THIS file's register produces; consumed by `03_isr-rates-gains.md` SV-TAX-FR-080 (per-transaction result), SV-TAX-FR-081 (costo básico), SV-TAX-FR-083 (holding period) — cross-referenced by id, not restated | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 14 pp.9-10 (EVID-093; 03-file LB-006/FR-081) |
| LB-011 | Ley ISR, Art. 28 inciso final (via `02_isr-deductions.md` LB-001) — **POINTER** | Mixed-use allocator: costs/expenses bearing simultaneously on gravadas, no-gravables and non-renta activity are deductible only in the proportion rentas gravadas ÷ total — the pro-rata factor owned by `02_isr-deductions.md` SV-TAX-FR-036 (carve-out SV-TAX-FR-037), consumed by this file's mixed-use depreciation FR | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 28 p.19 zone (EVID-097; 02-file LB-001/FR-036) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): no T7-specific dead tracks exist — the *pago mínimo*
regime (void, R21) and the D.L. 969-2024 foreign tracks (dead, R18) do not
reach Arts. 30/30-A; the Reglamento Art. 17 *media-tasa* method is historical
(`03_isr-rates-gains.md` LB-010) and touches only the capital-gain COMPUTATION
this file feeds, never the register; Reglamento Arts. 81-83 and 85-101
(books/records/inventories regime around Art. 84) are DEROGADO (3) and are
cited only as the repeal-map context proving Art. 84's survivor status. The
54_ reform tail through Jan-2026 adds nothing touching this file (verified
this task).

## 3. Functional Requirements

### 3.1 Depreciation deduction: scope, base and category maxima (Art. 30)

- **SV-TAX-FR-150:** The system shall deduct, from the *renta obtenida*
  (obtained income) of each *ejercicio*, the depreciation of the acquisition
  or fabrication cost of goods exploited by the taxpayer in the generation of
  computable renta; and for goods consumed or exhausted within a period of
  twelve months or less of use in renta production, it shall deduct the
  TOTAL cost in the ejercicio in which the good's use was GREATER, taking
  that ejercicio from the taxpayer's own declaration (no depreciation
  schedule for ≤12-month goods). (LB-001; EVID-101)
- **SV-TAX-FR-151:** The system shall compute, for each asset whose use
  extends beyond twelve months, an annual depreciation quota by applying a
  FIXED AND CONSTANT percentage over the value subject to depreciation,
  seeded per category at the LEGAL MAXIMA as default rates —
  *edificaciones* 5%, *maquinaria* 20%, *vehículos* 25%, *otros bienes
  muebles* 50% — where the taxpayer may adopt a LOWER percentage but never a
  higher one; once a percentage is adopted for a good, the system shall
  refuse any change unless a DGII authorization reference is recorded on the
  asset — depreciation computed under an unauthorized change is NON-deductible
  and the system shall flag it as such. (LB-004; EVID-101)
- **SV-TAX-FR-152:** The system shall determine the VALUE SUBJECT TO
  DEPRECIATION as the total cost of the good, EXCEPT: (a) imported machinery
  that enjoyed IVA exemption at import — the depreciable value shall be
  capped at the value recorded by DGII at the moment of import (cap ground
  `import_iva_exempt_dgii` with the DGII value as evidence field); (b) used
  machinery or movable goods — the depreciable value shall be capped at the
  NEW-good price at the moment of the taxpayer's acquisition, multiplied by
  the years-of-life factor: 1 year 80%, 2 years 60%, 3 years 40%, 4 years or
  more 20% (cap ground `used_asset` with new-price and years-of-life evidence
  fields); both cap families are MAXIMA (a lower actual cost depreciable in
  full) and their price inputs are subject to *fiscalización* — the system
  shall keep the supporting values on the asset record.
  (LB-003; EVID-101)
- **SV-TAX-FR-153:** The system shall classify assets into the *maquinaria*
  20% category when they are any apparatus or set of pieces serving to
  elaborate products or to produce determined effects — *trituradores de
  piedra* (stone crushers), *excavadoras* (excavators), *tornos* (lathes)
  used in mechanics and foundry, and similar (Reglamento Art. 35 definition,
  with a classification hint on the category and the definition text exposed
  to the classifier). (LB-009; EVID-142)

### 3.2 Computation timing (Art. 30 num. 1; D.L. 192-2018)

- **SV-TAX-FR-154:** The system shall admit, for a good whose use or
  employment in gravable-renta production does not span a COMPLETE
  ejercicio, only the part of the annual quota that proportionally
  corresponds as a function of the TIME the good has been in use in the
  generation of renta or conservation of the source (part-year *pro-rata
  temporis*; day/month count convention recorded as OQ-003).
  (LB-002; EVID-101)
- **SV-TAX-FR-155:** The system shall implement the seasonal-activity rule
  of the D.L. 192-2018 *interpretación auténtica*: for assets flagged
  seasonal, the use of machinery and equipment in gravable-renta production
  is understood as realized over the COMPLETE ejercicio and the system shall
  deduct the TOTAL annual depreciation quota — no proration by season length
  — during the useful life of such goods, with the deduction posted under
  the *costo de venta* (cost of sales) deductibility rules; the seasonal
  qualification shall be an OPEN-LIST configuration flag settable per
  company and per asset (the *cafetalero/cañero* sectors are statutory
  exemplars, never a hard-coded sector list), defaulting to OFF.
  Version note (D12): interpretation effective 2018-12-20; periods before
  that date apply the ordinary part-year proration of SV-TAX-FR-154 (dated
  data). (LB-002; LB-007; EVID-169)
- **SV-TAX-FR-156:** The system shall capitalize the depreciation of goods
  employed in the production, construction, manufacture or extraction of
  other goods, and in the *lotificación* (land parcelling) of *bienes
  inmuebles* (immovable goods): the annual
  quota (or its proportion) shall form part of the COST of the goods built
  or parcelled — never deducted as a period expense — and the system shall
  grant the deduction only for the depreciation corresponding to goods SOLD
  in the respective ejercicio or period (recovery through cost of sales at
  the sale event). (LB-002; EVID-101)
- **SV-TAX-FR-157:** The system shall admit depreciation for goods used at
  the same time in gravable and non-gravable (or non-renta) production only
  in the proportion corresponding to gravable income, consuming the Art. 28
  final-inciso allocator owned by `02_isr-deductions.md` SV-TAX-FR-036 —
  including its D.L. 969-2024 carve-out (SV-TAX-FR-037: subjects flagged
  `isr_foreign_excluded_concepts` apply no factor; version cutover
  2024-03-22, dated data). (LB-005; LB-011; EVID-101; 02-file
  SV-TAX-FR-036/037)

### 3.3 Blocks, exclusions and evidence (Art. 30 nums. 3-10)

- **SV-TAX-FR-158:** The system shall NOT accumulate to the quotas of later
  years the depreciation quotas a taxpayer failed to deduct, or deducted in
  a lesser amount, in prior years (no catch-up: each ejercicio's admitted
  quota is capped at its own current quota; the deficiency is recorded on
  the asset history as non-recoverable). (LB-005; EVID-101)
- **SV-TAX-FR-159:** The system shall treat every depreciable good as
  REDEEMED for tax purposes within the term resulting from its fixed
  percentage (e.g. 5% → 20 years; 20% → 5; 25% → 4; 50% → 2), and shall
  block ANY further depreciation deduction once the good is fiscally
  redeemed — the register locks with ground `fully_redeemed`.
  (LB-005; EVID-101)
- **SV-TAX-FR-160:** The system shall admit the depreciation claim only on
  goods OWNED by the taxpayer while they are in use in the production of
  gravable income; where over a good one person holds the *usufructo*
  (usufruct) and another the *nuda propiedad* (bare ownership), the system
  shall attribute the depreciation to the USUFRUCTUARY while the usufruct
  lasts, and none to the bare owner. (LB-005; EVID-101)
- **SV-TAX-FR-161:** The system shall never depreciate *mercaderías*
  (merchandise) or inventory existences, nor rural or urban LAND — except
  what is built on it — and, for *edificaciones*, shall require the
  accounting SEPARATION of the land value from the building value,
  depreciating only the building component. (LB-005; EVID-101)
- **SV-TAX-FR-162:** The system shall not apply any valuation or
  REVALUATION of goods in use to this deduction: revaluation-driven value
  changes shall never raise the depreciable base, the annual quota or the
  register's *saldo por depreciar* (consistent with the Art. 30-A literal b)
  mirror and the CT-bookkeeping reality of the asset record).
  (LB-005; EVID-101)
- **SV-TAX-FR-163:** The system shall require, for the depreciation of
  acquisition, creation, elaboration or construction outlays, demonstration
  by *documentos de pago idóneos* (suitable payment documents — payment
  evidence references on the asset record), and shall NEVER include the
  real-estate transfer tax in the acquisition cost of inmuebles for
  depreciation purposes. (LB-004; EVID-101)

### 3.4 Software amortization (Art. 30-A)

- **SV-TAX-FR-164:** The system shall amortize the acquisition or
  production cost of computer programs (software) used in gravable-renta
  production or source conservation, applying a fixed and constant
  percentage of a MAXIMUM 25% annual (the maximum implying a 4-year span at
  full quota; a shorter schedule would need a higher percentage that the
  25% maximum does not admit — OQ-007), only for OWNED software while in
  use producing gravable income; for programs produced by the taxpayer for
  its own use, the system shall refuse the amortization of the capitalized
  cost when the outlays composing that cost were already deducted in a
  prior period (no double deduction). Software is the EXPRESS deductible
  intangible track — *derechos de llave* (goodwill), marks and similar
  intangibles stay non-deductible per `02_isr-deductions.md` SV-TAX-FR-052
  numeral 19. (LB-006; EVID-102; 02-file SV-TAX-FR-052)
- **SV-TAX-FR-165:** The system shall cap the value subject to software
  amortization, for USED programs, at the NEW-program price at the moment
  of acquisition multiplied by the years-of-life factor — 1 year 80%,
  2 years 60%, 3 years 40%, 4 years 20% — mirroring the used-machinery
  caps of SV-TAX-FR-152 (same evidence fields, cap ground
  `used_software`), the prices being subject to fiscalización.
  (LB-006; EVID-102)
- **SV-TAX-FR-166:** The system shall apply to software the Art. 30 mirror
  governance: no revaluation (literal b); part-year proportional quota when
  use does not span a complete ejercicio (literal d — same convention as
  SV-TAX-FR-154); mixed gravable/non-gravable use admitted only in the
  gravable proportion per the 02-file allocator (literal f — SV-TAX-FR-157
  kin); no accumulation of missed amortization to later years (literal g —
  SV-TAX-FR-158 kin); and no percentage change without authorization of
  the *Administración Tributaria* (literal h — same authorization-reference
  mechanic as SV-TAX-FR-151); all without prejudice to the CT Arts. 156-A
  and 158 retention tracks owned by `04_isr-withholding.md`
  SV-TAX-FR-123/126. (LB-006; EVID-102; 04-file SV-TAX-FR-123/126)

### 3.5 The Art. 84 depreciation register

- **SV-TAX-FR-167:** The system shall keep a detailed, per-asset
  depreciation register for goods dedicated to the production of computable
  income (*registros pormenorizados* — itemized records), containing AT
  LEAST the Reglamento Art. 84 fields — *ESPECIFICACIÓN DEL BIEN* (asset
  specification), *VALOR A DEPRECIAR* (value subject to depreciation, per
  SV-TAX-FR-152), *FECHA EN QUE COMIENZA A USARSE* (in-use start date),
  *PERÍODO DE VIDA ÚTIL* (useful-life period, derived from the fixed
  percentage per SV-TAX-FR-159), *MEJORAS* (improvements), *ADICIONES*
  (additions), *CUOTA DE DEPRECIACIÓN* (depreciation quota), *SALDO POR
  DEPRECIAR* (balance left to depreciate), *RETIRO* (retirement),
  *ENAJENACIÓN* (disposal) — plus every datum the nature of the specific
  asset demands (open extension fields); the register duty binds every
  taxpayer obliged to keep formal accounting or records, and is waived only
  for those exempt from that obligation by law. (LB-008; EVID-145)
- **SV-TAX-FR-168:** The system shall maintain per-asset history inside the
  register: every *mejora* and *adición* — including the capitalization
  inflows routed from `02_isr-deductions.md` (repair-classified expenses
  implying remodeling, structural extension, value increase or life
  extension per its SV-TAX-FR-047, and interest linked to non-gravable
  assets capitalized into acquisition cost per its SV-TAX-FR-049) — shall
  be recorded as a register line RAISING the asset's *valor a depreciar*
  and *saldo por depreciar*, generating its own quota at the asset's
  adopted fixed percentage without reopening prior years (mechanics
  recorded as OQ-006); and every ejercicio shall record its quota line
  (full, proportional, seasonal or capitalized) with its admitted and
  blocked amounts. (LB-008; EVID-145; 02-file SV-TAX-FR-047/049)
- **SV-TAX-FR-169:** The system shall record, as register events, every
  RETIRO (retirement — with date and value) and every ENAJENACIÓN
  (disposal — with date, transaction value and book data), closing the
  asset's depreciation and freezing its history; disposal events are the
  feed for the capital-gain routing owned by `03_isr-rates-gains.md`
  (SV-TAX-FR-079 habituality gate, SV-TAX-FR-080 per-transaction result,
  SV-TAX-FR-083 holding-period counting — cited by id, not restated), and
  retirement events shall state whether the retired good leaves any
  *saldo por depreciar*. (LB-008; LB-010; EVID-145/093; 03-file
  SV-TAX-FR-079/080/083)
- **SV-TAX-FR-170:** The system shall expose, per asset, the ACCUMULATED
  ADMITTED DEPRECIATION — the sum of the *depreciaciones realizadas y
  admitidas* (depreciations effected and admitted under the law: quota
  lines actually admitted as deductions, excluding blocked lines under
  SV-TAX-FR-151/158/159 grounds) — as the feed consumed by
  `03_isr-rates-gains.md` SV-TAX-FR-081 for *costo básico* (acquisition
  cost − accumulated admitted depreciation) and by its SV-TAX-FR-080 for
  the disposal transaction result; the register's *saldo por depreciar*
  shall tie to *valor a depreciar* − accumulated admitted depreciation,
  and the reconciliation shall be verifiable per asset per ejercicio.
  (LB-010; LB-008; EVID-093/145; 03-file SV-TAX-FR-080/081)

### 3.6 Category templates, configuration and deduction routing

- **SV-TAX-FR-171:** The system shall seed asset-category templates per
  the Art. 30 legal classes — *edificaciones*, *maquinaria* (with the
  Art. 35 classification hint per SV-TAX-FR-153), *vehículos*, *otros
  bienes muebles*, and *software* (Art. 30-A) — each defaulting to its
  legal maximum rate (5/20/25/50/25%), with the used-asset and
  used-software cap factors (80/60/40/20%) and the IVA-exempt-import
  DGII-value cap as configurable base rules, and the seasonal flag
  (SV-TAX-FR-155) settable per company and per asset (default OFF; the
  statutory exemplars cafetalero/cañero exposed only as documentation of
  the open list, never as an enumerated whitelist).
  (LB-003; LB-004; LB-006; LB-007; LB-009; EVID-101/102/169/142)
- **SV-TAX-FR-172:** The system shall route every depreciation/amortization
  line computed under this file to the ISR deduction layer
  (`02_isr-deductions.md` SV-TAX-FR-034 gate) with its routing class:
  ordinary period deduction; seasonal full quota under the *costo de venta*
  rules (SV-TAX-FR-155); capitalized into built-goods cost with
  recovery at sale (SV-TAX-FR-156); gravable-proportion share
  (SV-TAX-FR-157/166); or NON-deductible with ground — unauthorized
  percentage change, post-redemption, non-owned asset, land/inventory,
  revaluation-driven, own-produced double-deduction, or missed-quota
  catch-up (SV-TAX-FR-151/158/159/160/161/162/164) — every line traceable
  to its register quota line. (LB-001; LB-002; LB-004; LB-005; LB-006;
  EVID-101/102/169)

## 4. Data Model

No dated legal TABLE vintages belong to this file: the category maxima
(5/20/25/50%) and the used-asset cap factors (80/60/40/20%) are textually
stable in the 54_ consolidation (stamps (2)/(7)/(14) — last touching reform
D.L. 496-2004; reform tail through Jan-2026 adds nothing — verified this
task), so no CSV sidecar is produced and the parameters live on the category
and cap configuration below. The only version regime is the D.L. 192-2018
seasonal cutover (effective 2018-12-20 — a behavior flag with a dated
validity, not a table vintage). **Interface entity for the chart-of-accounts
wave and Task 7's index:** the ISR depreciation register = the Art. 84 field
set + per-asset history on `account.asset` (rows below). Layer semantics:
this file introduces Odoo-side computation/bookkeeping data only (wave
default `odoo`; see §5).

**Category templates and cap configuration:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset.category (SV extension) | isr_legal_class, isr_rate_max | select / percent | edificaciones_5 · maquinaria_20 · vehiculos_25 · otros_muebles_50 · software_25 (legal MAXIMA defaults; adoptable lower) | FR-151, FR-164, FR-171 |
| account.asset.category (SV extension) | isr_maquinaria_definition_hint | text | Reglamento Art. 35 definition exposed to the classifier (apparatus/set of pieces elaborating products or producing effects; crushers, excavators, lathes, similar) | FR-153 |
| l10n_sv.isr.used.asset.cap (new) | min_years, max_years, factor, applies_to | int (nullable max) / percent / select | 1→80% · 2→60% · 3→40% · 4+→20%; applies_to: maquinaria_bienes_muebles (Art. 30.2.b) · software (Art. 30-A c) | FR-152, FR-165 |
| res.company | isr_seasonal_activity | boolean (default false) | open-list seasonal qualification (D.L. 192-2018; exemplars cafetalero/cañero documented, never enumerated); per-asset override below | FR-155, FR-171 |
| account.asset | isr_seasonal (override) | boolean (tri-state) | unset = inherit company flag; on/off per asset | FR-155 |

**The Art. 84 register — ISR field set on the asset (verbatim minimums +
nature extras):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset (SV extension) | isr_especificacion | char/text | ESPECIFICACIÓN DEL BIEN — asset specification (distinct from the free description: the register-facing identification) | FR-167 |
| account.asset | isr_valor_a_depreciar | monetary (computed) | VALOR A DEPRECIAR — total cost capped per FR-152/165 grounds: none · import_iva_exempt_dgii · used_asset · used_software | FR-152, FR-165, FR-167 |
| account.asset | isr_base_cap_ground, isr_cap_evidence_new_price, isr_cap_evidence_years, isr_dgii_import_value | select / monetary / int | cap evidence (new-good price, years of life, DGII import-record value) — fiscalización inputs | FR-152, FR-165 |
| account.asset | isr_fecha_inicio_uso | date | FECHA EN QUE COMIENZA A USARSE — in-use start date (drives FR-154 proration and 03-file FR-083 holding) | FR-154, FR-167 |
| account.asset | isr_periodo_vida_util, isr_rate_adopted, isr_dgii_change_authorization | int (years, computed from rate) / percent / char | PERÍODO DE VIDA ÚTIL = term from the fixed percentage (5%→20y, 20%→5y, 25%→4y, 50%→2y); adopted % immutable without DGII authorization reference | FR-151, FR-159, FR-167 |
| account.asset | isr_mejoras, isr_adiciones | monetary (computed from register lines) | MEJORAS / ADICIONES — improvements and additions raising the depreciable value (inflows incl. 02-file FR-047/FR-049 capitalizations) | FR-168 |
| account.asset | isr_cuota_depreciacion | monetary (computed) | CUOTA DE DEPRECIACIÓN — current annual quota (fixed % × valor a depreciar) | FR-151, FR-167 |
| account.asset | isr_saldo_por_depreciar | monetary (computed) | SALDO POR DEPRECIAR — valor a depreciar (+ mejoras/adiciones) − accumulated admitted depreciation; 0 at redemption → lock | FR-159, FR-170 |
| account.asset | isr_retiro | date + monetary + cause | RETIRO — retirement event (date, value, cause; residual saldo stated) | FR-169 |
| account.asset | isr_enajenacion | date + monetary | ENAJENACIÓN — disposal event (date, transaction value; book data snapshot for the 03-file feed) | FR-169 |
| account.asset | isr_nature_extra_fields | open key-value | "todos los datos que la naturaleza del bien exija" — nature-demanded extras (open extension) | FR-167 |
| account.asset | isr_owner_status | select | owner · usufructuary (depreciates) · bare_owner (never) · lessee (never) | FR-160 |
| account.asset | isr_land_separation | boolean + monetary split | edificaciones on owned land: land value vs building value separated; depreciation on building component only | FR-161 |
| account.asset | isr_fully_redeemed | boolean (computed) | fiscal redemption reached → depreciation blocked (register lock) | FR-159 |
| account.asset | isr_payment_doc_refs | m2m to account.move.line / char refs | documentos de pago idóneos evidence; real-estate transfer tax excluded from cost by validation | FR-163 |
| account.asset | isr_admitted_depreciation | monetary (computed, fed to 03 file) | accumulated depreciaciones realizadas y admitidas — the costo básico feed | FR-170; 03-file FR-081 |

**Per-asset history (quota lines) and routing:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.asset.depreciation.line (new) | asset_id, ejercicio, quota_amount, proration_factor, seasonal | m2o / fiscal year / monetary / factor / boolean | one line per ejercicio per asset; factor for part-year use (FR-154) or 1.0 full-seasonal (FR-155) | FR-154, FR-155, FR-168 |
| l10n_sv.isr.asset.depreciation.line | admitted_amount, blocked_amount, block_ground | monetary / select null | unauthorized_change · post_redemption · non_owned · land_inventory · revaluation · double_deduction · catch_up | FR-151, FR-158..FR-162, FR-164, FR-172 |
| l10n_sv.isr.asset.depreciation.line | routing_class | select | period_deduction · seasonal_cost_of_sale · capitalized_built_goods · gravable_proportion · non_deductible | FR-155, FR-156, FR-157, FR-166, FR-172 |
| l10n_sv.isr.asset.depreciation.line | improvement_ref, addition_ref | m2o to capitalization source | mejoras/adiciones lines raising valor a depreciar (02-file FR-047/049 inflows) | FR-168 |
| account.asset (software) | isr_software_ownproduced, isr_prior_deducted_outlays | boolean | own-produced for own use: capitalized cost non-amortizable when components already deducted | FR-164 |
| account.move (disposal/retirement) | isr_register_close snapshot | related fields | disposal event values feeding 03-file FR-079/080/083 computations (habituality, result, holding) | FR-169 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living in
the LGPL client. No SaaS rows are introduced in this file: none of these FRs
touch DTE generation/transformation (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are stable
across Odoo 17/18/19/20 (`account.asset`/`account.asset.category` exist in
core asset accounting; the SV extension fields above ride the standard
models); version-specific behavior is recorded per row where a legal vintage
exists. The depreciation ACCOUNTS the lines post to are the chart-of-accounts
wave's surface; this file owns the register, computation and routing rules.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-150 | odoo | account.asset + computation | cost, ≤12m flag | ≤12-month goods bypass the schedule: full cost in the declared greater-use ejercicio |
| FR-151 | odoo | account.asset + account.asset.category | isr_rate_adopted, isr_rate_max | Legal maxima as category defaults; lower adoptable; change requires isr_dgii_change_authorization else non-deductible flag |
| FR-152 | odoo | account.asset | isr_base_cap_ground + evidence | Import IVA-exempt machinery → DGII import value; used goods → new price × 80/60/40/20; maxima, not floors |
| FR-153 | odoo | account.asset.category | isr_maquinaria_definition_hint | Art. 35 definition text as classifier aid; 20% category |
| FR-154 | odoo | l10n_sv.isr.asset.depreciation.line | proration_factor | Time-in-use proportional quota; day/month convention = OQ-003 |
| FR-155 | odoo | res.company + account.asset + line | isr_seasonal, seasonal flag | FULL quota, no season-length proration; costo-de-venta routing; version: effective 2018-12-20 (pre-cutover periods prorate); open list — never hard-coded sectors |
| FR-156 | odoo | l10n_sv.isr.asset.depreciation.line | routing_class = capitalized_built_goods | Quota into built/parcelled-goods cost; recovery at sale (cost of sales) |
| FR-157 | odoo | computation | consumes 02-file FR-036 factor | Gravadas/total allocator; 02-file FR-037 carve-out flag skip (969-2024, cutover 2024-03-22) |
| FR-158 | odoo | l10n_sv.isr.asset.depreciation.line | block_ground = catch_up | Missed/deficient prior quotas never accumulated; recorded non-recoverable |
| FR-159 | odoo | account.asset | isr_fully_redeemed | Redemption term from fixed % (20/5/4/2 years); register lock |
| FR-160 | odoo | account.asset | isr_owner_status | Owner-only + in-use; usufructuary depreciates; lessee/bare owner never |
| FR-161 | odoo | account.asset | isr_land_separation | Inventory/land never; land vs building split for edificaciones |
| FR-162 | odoo | computation guard | — | Revaluation values never raise base/quota/saldo (any revaluation model output ignored for ISR) |
| FR-163 | odoo | account.asset | isr_payment_doc_refs | Idóneos payment-document evidence; real-estate transfer tax rejected from cost |
| FR-164 | odoo | account.asset (software) | isr_software_ownproduced | 25% max fixed/constant (4-year span at maximum); ownership+use; no double deduction on own-produced; counterpoint to 02-file FR-052 n.19 |
| FR-165 | odoo | account.asset + l10n_sv.isr.used.asset.cap | applies_to = software | Used-software caps 80/60/40/20% of new price |
| FR-166 | odoo | computation + line | mirror flags | Art. 30-A literals b/d/f/g/h mirror the corresponding 30 rules; CT 156-A/158 reservation → 04-file FR-123/126 |
| FR-167 | odoo | account.asset (SV extension) | THE Art. 84 field set | Register = asset-model fields + history (§4); nature extras open; duty waived only for non-formal-accounting subjects |
| FR-168 | odoo | l10n_sv.isr.asset.depreciation.line | improvement_ref/addition_ref | Mejoras/adiciones raise valor a depreciar; own quota at adopted %; prior years never reopened (mechanics OQ-006) |
| FR-169 | odoo | account.asset + account.move | isr_retiro / isr_enajenacion | Register-close events; disposal feed to 03-file FR-079/080/083 (cited, not restated) |
| FR-170 | odoo | account.asset | isr_admitted_depreciation | THE costo básico feed (03-file FR-081); saldo tie-out check per asset per ejercicio |
| FR-171 | odoo | account.asset.category seeding | templates per class | Maxima defaults 5/20/25/50/25%; cap factors config; seasonal flag per company/asset (default OFF) |
| FR-172 | odoo | l10n_sv.isr.asset.depreciation.line | routing_class + block_ground | Lines routed to the 02-file FR-034 deduction gate with traceability to the register |

Version-regime notes (D12): FR-155 records the D.L. 192-2018 seasonal
cutover (effective 2018-12-20; earlier periods compute the ordinary part-year
proration — dated behavior flag). FR-157 inherits the D.L. 969-2024
allocator carve-out cutover (2024-03-22) from the 02-file FR-037. The
category maxima and used-asset cap factors carry no vintage regime: their
last reforming instruments are the 54_ stamps (2)/(7)/(14) (D.L. 250-1992 /
841-1996 / 496-2004) and Art. 30-A's adding decree (15) (D.L. 646-2005); the
54_ reform tail through Jan-2026 (D.L. 499-2026 the latest) touches neither
article — verified this task (dated data anchor: re-verify at the 54_
consolidation's next refresh).

## 6. Acceptance Criteria

- **AC-001:** Given machinery acquired for $30,000.00 in the *maquinaria*
  category (20% maximum adopted), in use in gravable production from 1-Apr
  of the current ejercicio through year-end (9 of 12 months), then the
  annual quota = 20% × 30,000.00 = $6,000.00 and the admitted depreciation
  = 6,000.00 × 9/12 = $4,500.00 (FR-151, FR-154).
- **AC-002:** Given the same machinery in use the full following ejercicio,
  then the admitted depreciation = $6,000.00; given the taxpayer had adopted
  10% instead of the 20% maximum, then the quota = 10% × 30,000.00 =
  $3,000.00 per year and no validation error is raised (lower rates
  adoptable) (FR-151).
- **AC-003:** Given used machinery acquired for $25,000.00 with 3 years of
  life and a new-good price of $50,000.00 at the acquisition moment, then
  the depreciable value is capped at 40% × 50,000.00 = $20,000.00 and the
  annual quota at the 20% category rate = $4,000.00 (FR-152).
- **AC-004:** Given imported machinery that enjoyed IVA exemption at import,
  acquired for $80,000.00 while DGII's import record values it at
  $70,000.00, then the depreciable value = $70,000.00 (DGII-value cap)
  (FR-152).
- **AC-005:** Given a coffee-processing company flagged seasonal
  (cafetalero exemplar) with milling machinery of $120,000.00 at 20% used
  only during the 4-month harvest season, then the deducted quota =
  20% × 120,000.00 = $24,000.00 — the FULL annual quota with no 4/12
  proration — routed under the costo-de-venta rules; given the same asset
  in a non-seasonal company with 6 months of use, then the admitted quota
  = 24,000.00 × 6/12 = $12,000.00 (FR-155, FR-154).
- **AC-006:** Given a good consumed within ten months of use costing
  $800.00, then no depreciation schedule is created and the $800.00 is
  deducted in the ejercicio the taxpayer declares as greater use
  (FR-150).
- **AC-007:** Given a construction crane whose annual quota is $10,000.00
  while used to build a building for sale, then the $10,000.00 enters the
  building's cost (capitalized, no period deduction) and is deducted when
  the built good is sold (FR-156).
- **AC-008:** Given an asset with annual quota $6,000.00 and an Art. 28
  allocator factor of 0.75 from `02_isr-deductions.md` FR-036, then the
  admitted depreciation = 6,000.00 × 0.75 = $4,500.00 (FR-157).
- **AC-009:** Given a quota of $6,000.00 not deducted in year 1, then year
  2 admits at most its own $6,000.00 — never $12,000.00 — and the year-1
  deficiency is recorded non-recoverable (FR-158).
- **AC-010:** Given an *edificación* of $150,000.00 at 5%, then the fiscal
  redemption term is 20 years and the year-21 deduction is blocked with
  ground `fully_redeemed` even if book value remains (FR-159).
- **AC-011:** Given a property acquired for $200,000.00 with the accounting
  separating $50,000.00 of land from $150,000.00 of building, then
  depreciation computes only on $150,000.00 at 5% = $7,500.00 per year and
  the land component never depreciates (FR-161).
- **AC-012:** Given the percentage on the $30,000.00 machinery changed from
  20% to 25% with no DGII authorization reference recorded, then the
  recomputed depreciation is flagged NON-deductible in full (FR-151).
- **AC-013:** Given software acquired for $100,000.00 (new, owned, in
  gravable use) at the 25% maximum, then the annual amortization =
  $25,000.00 over a 4-year span; given it entered use on 1-May (8 of 12
  months), then the first-year admitted amortization = 25,000.00 × 8/12 =
  $16,666.67 (FR-164, FR-166).
- **AC-014:** Given used software acquired for $18,000.00 with 2 years of
  life and a new-program price of $40,000.00, then the amortizable base is
  capped at 60% × 40,000.00 = $24,000.00 (actual cost lower → $18,000.00
  depreciable in full) and the quota at 25% = $4,500.00 per year
  (FR-165).
- **AC-015:** Given machinery of $30,000.00 at 20% with three full-year
  quotas admitted ($18,000.00) plus one 9-month part-year line ($4,500.00),
  then the accumulated admitted depreciation = $22,500.00, the register's
  *saldo por depreciar* = 30,000.00 − 22,500.00 = $7,500.00, and a disposal
  feeds `03_isr-rates-gains.md` FR-081 a *costo básico* of 30,000.00 −
  22,500.00 = $7,500.00 with the disposal event closing the register
  (FR-170, FR-169).
- **AC-016:** Given a blocked quota line (unauthorized percentage change)
  of $7,500.00 in a year, then the accumulated admitted depreciation
  EXCLUDES it and the *saldo por depreciar* tie-out reports the blocked
  amount separately (FR-170, FR-151).
- **AC-017:** Given an asset under usufruct where the taxpayer holds the
  usufruct and a related party the bare ownership, then the depreciation
  computes in the usufructuary's determination and none in the bare
  owner's; given a leased asset, then no depreciation is admitted to the
  lessee (FR-160).
- **AC-018:** Given an improvement of $12,000.00 routed from
  `02_isr-deductions.md` FR-047 (life-extension repair classification) onto
  the $150,000.00 *edificación* at 5%, then the register records a *mejora*
  line raising the depreciable value to $162,000.00 and an additional
  quota of 5% × 12,000.00 = $600.00 per year going forward, with prior
  years unchanged (FR-168).
- **AC-019:** Given a new asset record, then the register exposes ALL ten
  Art. 84 minimum fields (especificación, valor a depreciar, fecha en que
  comienza a usarse, período de vida útil, mejoras, adiciones, cuota de
  depreciación, saldo por depreciar, retiro, enajenación) plus the
  nature-extras extension, and a subject not obliged to keep formal
  accounting is exempt from the register duty (FR-167).
- **AC-020:** Given a machine retired with a residual *saldo por
  depreciar* of $3,000.00, then the retirement event records date, value
  and the residual saldo, closes the asset history and no later quota line
  is generated (FR-169, FR-159).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Reglamento Art. 84 is the lone survivor of the repealed books regime (Arts. 81-101): its interaction with the CT Arts. 139-143 books/records regime (which now governs contabilidad formal) is unverified — SOQ-06, carried as `01_isr-framework.md` OQ-004; field list cited as printed either way (EVID-145 OQ-6 origin). | no | Takumi S2 (CT zone pass) | open |
| OQ-002 | Seasonal-activity qualification: "actividades estacionales" is open text with cafetalero/cañero as exemplars only. Which further activities validly set the flag (and is evidence/DGII criterion required before claiming the full quota)? FR-155 implements the open-list config flag defaulting OFF; qualification guidance needed for onboarding. | no | Takumi S2 | open |
| OQ-003 | Part-year pro-rata convention: the law admits "la parte de la cuota anual que proporcionalmente corresponda en función del tiempo" without fixing days vs months. FR-154/AC-001 use months (9/12); confirm no DGII criterion mandates day-count (or vice versa) before encoding the factor. | no | Takumi + Odoo implementation | open |
| OQ-004 | Used-asset "AÑOS DE VIDA" measurement (FR-152/165): years of the good's life counted from what — prior-owner use years, age since fabrication/acquisition, or a declared remaining-life? And what evidence sources the "precio del bien nuevo al momento de su adquisición" (quotes subject to fiscalización)? Define accepted evidence classes for the cap fields. | no | Takumi S2 | open |
| OQ-005 | Register format norms: Art. 30 num. 6 defers the register form to the Reglamento (Art. 84 gives the minimum field list); whether DGII issued further administrative norms/resolution detailing the register's format or presentation (kin to the 05-file OQ-002 for the Art. 74-C norms) — none appears in the corpus; §4 encodes the statutory minimums, conform when published. | no | Takumi S2 (sources registry) | open |
| OQ-006 | Mejoras/adiciones mechanics: the register mandates the fields but not the computation — whether an improvement generates its own forward quota at the asset's fixed percentage (FR-168 as written), extends the useful-life period, or restarts a schedule; boundary with current-expense repairs owned by `02_isr-deductions.md` FR-047. Confirm Odoo behavior with DGII practice. | no | Takumi + Odoo implementation | open |
| OQ-007 | Software schedule span: Art. 30-A fixes only the 25% MAXIMUM (4-year span at the maximum); whether the Administración Tributaria has ever authorized a higher percentage for fast-obsolescence software (the authorization path of literal h exists but no rate above 25% is in the corpus), and whether slower schedules (longer than 4 years) are uncontested practice. FR-164 encodes 25% max with adoptable-lower. | no | Takumi S2 | open |
