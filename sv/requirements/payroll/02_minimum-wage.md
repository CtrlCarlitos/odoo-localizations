# SV — Payroll — Minimum wage: salario mínimo chassis, dated SMM tables and piece-rate tariffs

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador *salario mínimo* (minimum wage, SMM) layer:
the Código de Trabajo (Labor Code, CT) chassis of Arts. 144-148 — every
worker's entitlement, the 8-hour-*jornada* (workday) reference for time-based
SMM with the 5-8-hour full-SMM window and the <5-hour proportional rule
(complete-the-week exception), the per-*jornada* floor guarantee for piece
work, and the *de pleno derecho* (as a matter of full legal right — automatic)
substitution of inferior wage stipulations — plus the Art. 159 triennial
review cadence; the DATED tariff tables of Decreto 11-2025 (16_, effective
2025-06-01, repealing D.E. 9/10-2021): four time-based sectors
(*agrícola* / *industria* / *comercio y servicios* / *maquila textil y
confección*) with three-decimal daily/hourly prints preserved verbatim, the
Art. 3 *unidad de obra* (unit of work) piece rates for caña (sugarcane) and
café (coffee) collection with their *rendimiento* (output) caps, and the
Art. 6 *descanso semanal* (weekly rest) prestación table per CT Art. 90
inciso 3º — all as the `smm_2025.csv` sidecar; the monthly-pays-regardless-
of-month-length rule; *trabajadores a domicilio* (home workers) sector
routing; the CT-benefits base rule of 16_ Art. 7 (max of sector daily SMM and
actual salary); and the SMM-indexed anchor interfaces every other file
consumes — the pinned aguinaldo exempt floor (2× *comercio y servicios*),
the unpinned FE-receptor and 25-SMM sector selections, and the 4×SMM
indemnización cap feed.

It does **not** cover: the *salario* / *salario básico* model and the
canonical earning-category matrix (`01_salary-model.md` — consumed by FR id,
never restated); jornada limits, surcharges, and the séptimo-día / descanso
semanal accrual mechanics for time-based workers
(`03_working-time-surcharges.md` — it consumes the Art. 6 prestación rates
recorded here); the vacaciones and aguinaldo computation engines
(`04_statutory-benefits.md` — the aguinaldo floor VALUE flows from this
file); social-security rates and caps (`05_social-security-contributions.md`,
`06_ss-declaration-remittance.md`); contracts, termination and the
indemnización computation (`07_contracts-termination.md` — owns the 4×SMM cap
arithmetic); or the aguinaldo ISR exento/gravado split
(`08_isr-interfaces.md`; `taxation/04_isr-withholding.md` SV-TAX-FR-120 owns
the split and consumes this file's floor by reference). Those files consume
this one for the dated SMM values and the sector-selection config.

## 2. Legal Basis

Authority order (binding, per master evidence index S4): SMM tariffs =
16_ (Decreto No. 11 — "Tarifas de Salarios Mínimos para la República de El
Salvador", Ministerio de Trabajo y Previsión Social, published Diario Oficial
No. 95, Tomo No. 447, 23-May-2025; in force 2025-06-01; repeals D.E. 9 and
10 of 07-Jul-2021) over the repealed 2021 pair; chassis = 11_ (Código de
Trabajo, Índice Legislativo edition, reform stamps (1)-(22) — SOQ-21 watch);
the salary/básico model and category matrix are consumed from
`01_salary-model.md` by FR id; the SMM-indexed ISR/e-invoicing anchors are
consumed from the S2 files by FR/OQ id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Trabajo, Art. 144: every worker — including *trabajadores a domicilio* (home workers) — is entitled to a salario mínimo that covers the needs of the household, which "se fijará periódicamente" | Every worker, home workers included, has the right to a minimum wage covering household needs; it is fixed periodically | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 144, Arts. 144-160 pp.36-38 (EVID-208) |
| LB-002 | Código de Trabajo, Art. 147: "Cuando los salarios mínimos se fijen por unidad de tiempo se referirán a la jornada ordinaria de trabajo de ocho horas diarias. Cuando la jornada de trabajo sea menor de ocho horas pero mayor de cinco, el patrono estará obligado a pagar el salario mínimo fijado; la misma obligación tendrá si, para el efecto de completar la semana laboral, la jornada fuere menor de cinco horas. En cualquier otro caso, la remuneración será proporcional al tiempo trabajado." For destajo, ajuste por obra and precio alzado: "obligatorio para el patrono asegurar el salario mínimo por jornada de trabajo" | Time-based minimum wages refer to the ordinary 8-hour workday; a jornada over five but under eight hours obliges the employer to pay the full fixed minimum wage, and the same obligation applies when a jornada under five hours serves to complete the working week; in any other case remuneration is proportional to time worked. For piecework/work-adjustment/lump-sum arrangements the employer is obliged to guarantee the minimum wage per workday | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 147, Arts. 144-160 pp.36-38 (EVID-208) |
| LB-003 | Código de Trabajo, Art. 148: the SMM "sustituyen de pleno derecho ... cualesquiera otros inferiores que se hayan estipulado"; never a negation of better acquired rights | Minimum wages substitute, as a matter of full legal right, any inferior stipulated wages; the substitution never negates better acquired rights | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 148, Arts. 144-160 pp.36-38 (EVID-208) |
| LB-004 | Código de Trabajo, Art. 159: "Los salarios mínimos fijados por decreto deberán ser revisados, por lo menos, cada tres años." | Minimum wages fixed by decree must be reviewed at least every three years | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 159, Arts. 144-160 pp.36-38 (EVID-208) |
| LB-005 | Decreto 11-2025, identity + Art. 1 + sector definitions + Arts. 14-15: "Tarifas de Salarios Mínimos para la República de El Salvador" (given 22-May-2025); considerando VI records the 2021 predecessor pair (D.E. 9 y 10, 07-Jul-2021, D.O. 129 T.432, vigentes from 1-Ago-2021); Art. 1 establishes the tariffs for the sectors "agrícola, industria, comercio, servicios, maquila textil y confección; así como para las personas trabajadoras a domicilio que laboren en estos rubros"; sector definitions: agricola includes "ganadería, pesca, recolección de cosecha de café y otras actividades agrícolas", servicios includes "servicios público o privado", industria includes "los ingenios azucareros, el beneficio de café, y otras actividades de industria y agroindustria"; Art. 14: "Deróguese los Decretos Ejecutivos No. 9 y 10" (de fecha 07 de julio de 2021); Art. 15: in force from 1-Jun-2025 | Decree 11-2025: the SMM tariff decree for the agricultural, industry, commerce/services and textile-maquila sectors plus home workers in those rubros, with sector definitions; repeals the 2021 executive-decree pair; effective 2025-06-01 | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.17 sumario + p.18 considerando VI + p.18 Art. 1 + p.21 Arts. 14-15 (EVID-191) |
| LB-006 | Decreto 11-2025, Art. 2 table [PSM-4 recovery]: "SECTOR ECONÓMICO — Salario Mensual / Salario por jornada diaria / Salario por Hora ordinaria: Agrícola $305.23 $10.035 $1.254 / Industria $408.80 $13.440 $1.680 / Comercio y servicios $408.80 $13.440 $1.680 / Maquila Textil y confección $402.32 $13.227 $1.653" (daily/hourly figures printed with THREE decimals — both PSM 4 and PSM 6 reads agree; SOQ-20); post-table inciso: "El salario mensual al que se hace referencia en el inciso anterior, se pagará indistintamente del número de días del mes que se está remunerando." | Art. 2: the four time-based sector tariffs — monthly / per-workday / per-ordinary-hour, with the daily and hourly values printed to three decimals as gazette constants (daily ≠ monthly/30: 10.035 × 30 = 301.05 ≠ 305.23 — never recomputed); the monthly salary pays regardless of the number of days of the month being remunerated | `sv/sources/16_Salarios_Minimos_2025.pdf` | pp.18-19 Art. 2 + inciso (EVID-191; SOQ-20) |
| LB-007 | Decreto 11-2025, Art. 3 (caña/café collection by unidad de obra, sistema mixto u otras estipulaciones similares — "no sujetos a horarios de trabajo"): a) "Recolección de caña — Por Tonelada $5.018 / Por arroba $2.007 [PSM-6 garble resolved by PSM-4]; Recolección de Café — Por libra $0.080"; b) fractions of tonelada/tarea: "el pago de ésta será proporcional a la unidad correspondiente"; c) "El empleador no podrá exigir un rendimiento mayor al de dos toneladas de caña o al de una extensión de terreno equivalente a una tarea en una misma jornada; la tarea deberá entenderse como el corte de seis surcos por catorce brazadas en resiembras y de seis surcos por diez brazadas en plantillas"; d) additional cortes "deberán ser remuneradas conforme a la escala fijada en el presente artículo" | Art. 3: piece-rate tariffs for sugarcane and coffee collection ($5.018/ton, $2.007/arroba (traditional weight unit; not quantified in the corpus — no invented conversion) and $0.080/lb); fractional production paid proportionally to the corresponding unit; output caps — the employer may not require more than 2 tons of cane or a tarea-equivalent land extension per jornada, the tarea being the cutting of six furrows by fourteen armspans in replantings and six by ten in new plantings; additional cuts remunerated per the article's scale | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.19 Art. 3 (EVID-192) |
| LB-008 | Decreto 11-2025, Art. 4: home workers ("personas trabajadoras a domicilio") in these rubros get the corresponding sector tariff | Home workers in the covered sectors receive the sector tariff corresponding to their rubro | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.19 Art. 4 (EVID-192) |
| LB-009 | Decreto 11-2025, Art. 6 table [PSM-4 recovery; empty under PSM 6] — descanso semanal prestación per CT Art. 90 inciso 3º: "Recolección de caña — Por cada Tarea $1.673 / Por cada Tonelada $0.836; Recolección de Café — Por cada arroba $0.335" | Art. 6: the piece-rate weekly-rest prestación table — cane $1.673 per tarea and $0.836 per ton, coffee $0.335 per arroba — implementing CT Art. 90 inciso 3º for workers not subject to work schedules | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.20 Art. 6 (EVID-192; PSM-4 recovery; SOQ-20) |
| LB-010 | Decreto 11-2025, Arts. 7-8: Art. 7: "El pago de las prestaciones que establece el Código de Trabajo ... como día de asueto, vacaciones, aguinaldo, indemnizaciones y otras, se hará con base al salario mínimo diario establecido, excepto cuando el salario estipulado sea mayor." Art. 8: irrenunciabilidad of the decree's rights | Art. 7: CT benefits (holiday, vacation, aguinaldo, indemnización and others) are paid on the established daily minimum wage unless the stipulated salary is higher; Art. 8: the decree's rights are non-waivable | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.20 Arts. 7-8 (EVID-192) |
| LB-011 | Código de Trabajo, Art. 58 (stamps (6)(8)) — interface anchor only, computation OWNED by `07_contracts-termination.md`: for the indemnización calculation "NINGUN SALARIO PODRA SER SUPERIOR A CUATRO VECES EL SALARIO MINIMO DIARIO LEGAL VIGENTE" (no salary may exceed four times the current legal daily minimum wage) | The countable salary for unjustified-dismissal indemnización is capped at 4× the current legal daily SMM — sector unnamed ("salario mínimo diario legal vigente", EVID-207 doubt; selection via this file's FR-022 config) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 58, Arts. 55-60 pp.20-21 (EVID-207) |

Version regime (D12): the SMM tariff rows are DATED data. The corpus holds
exactly one vintage — Decreto 11-2025, valid_from 2025-06-01 (published D.O.
No. 95 T.447 23-May-2025) — which repeals the 2021 pair (D.E. 9/10-2021, in
force 1-Ago-2021); the 2021 values themselves are ABSENT from the corpus and
are never invented (OQ-001 — rows would be needed only to recompute or
floor-validate periods before 2025-06-01). The CT Art. 159 triennial review
cadence means new vintages arrive on decree cadence; loaders select by
valid_from and flag lookups predating the earliest vintage.

## 3. Functional Requirements

### 3.1 SMM chassis (CT Arts. 144-148, 159)

- **SV-PAY-FR-011:** The system shall load the salario mínimo tariffs as
  DATED legal data keyed by (sector, tariff type, unit) and selected by the
  period's date, seeded from the `smm_2025.csv` sidecar transcribed EXACTLY
  as printed in Decreto 11-2025: the three-decimal daily/hourly time-based
  values ($10.035/$1.254/$13.440/$1.680/$13.227/$1.653) and the Art. 6
  prestación values ($1.673/$0.836/$0.335) are gazette constants carrying
  [sic] fidelity flags and are NEVER rounded, reformatted or recomputed from
  the monthly figures (daily ≠ monthly/30; SOQ-20); the vintage chain shall
  be recorded as metadata — Decreto 11-2025 OPERATIVE valid_from 2025-06-01
  (D.O. No. 95 T.447 23-May-2025, Art. 15), repealing D.E. 9/10-2021 (Art.
  14), whose values are absent from the corpus (pre-2025-06-01 lookups flag
  OQ-001, never guess); the CT Art. 159 triennial review cadence is recorded
  on the data model as the expected re-issue cadence. (LB-004; LB-005;
  LB-006; EVID-191/208; SOQ-20)
- **SV-PAY-FR-012:** The system shall apply the Art. 147 jornada rules to
  every time-based SMM worker: the SMM refers to the ordinary eight-hour
  jornada; a jornada of more than five and up to eight hours is paid the
  FULL daily sector SMM; a jornada under five hours is paid PROPORTIONALLY
  to the time worked (hourly tariff × hours) — EXCEPT when the short jornada
  is worked to complete the *semana laboral* (working week), in which case
  the full daily SMM is owed (kin of the Art. 143 complete-the-week day,
  SV-PAY-FR-008). (LB-002; EVID-208)
- **SV-PAY-FR-013:** The system shall guarantee the per-jornada minimum
  floor for piece workers (*destajo*, ajuste por obra, precio alzado and the
  Art. 3 collection rubros): when a jornada's production-based pay falls
  below the applicable sector DAILY SMM, the payroll shall top the day's pay
  up to that floor; the floor sector for the collection rubros is the
  agrícola row — café collection is expressly included in the agrícola
  sector definition, while caña collection reads through the "otras
  actividades agrícolas" catch-all (LB-005): a stated working reading
  folded into OQ-002. (LB-002; LB-005; LB-007; EVID-208/191/192)
- **SV-PAY-FR-014:** The system shall implement the *de pleno derecho*
  substitution of Art. 148: any contractual wage stipulation inferior to
  the applicable current-vintage SMM is automatically replaced by the SMM —
  the substitution is applied (and re-evaluated) whenever a dated tariff row
  changes, flipping the contract's floor-validation status without
  renegotiation — and shall never reduce wages or rights superior to the SMM
  (mejores derechos adquiridos); the decree's rights are non-waivable
  (*irrenunciabilidad*, 16_ Art. 8). (LB-003; LB-010; EVID-208/192)
- **SV-PAY-FR-015:** The system shall pay the MONTHLY sector SMM regardless
  of the number of days of the month being remunerated — February and July
  both pay the same monthly figure; no day-count proration of the monthly
  tariff is permitted (the proportional and per-jornada rules of FR-012/
  FR-013 operate on the daily/hourly tariffs, never by rescaling the
  monthly). (LB-006; EVID-191)

### 3.2 Piece-rate tariffs and descanso prestación (16_ Arts. 3, 6)

- **SV-PAY-FR-016:** The system shall pay caña and coffee collection
  workers on the Art. 3 unit-of-work tariffs — caña $5.018 per tonelada and
  $2.007 per arroba, café $0.080 per libra — as dated data from the sidecar,
  with FRACTIONAL production paid proportionally to the corresponding unit
  (fractions of tonelada/tarea never truncated nor rounded away); production
  pay classifies as ordinary pay (*salario integrante*) per the canonical
  matrix of `01_salary-model.md` SV-PAY-FR-004 — consumed by FR id, not
  restated. (LB-007; EVID-192)
- **SV-PAY-FR-017:** The system shall enforce the Art. 3 rendimiento caps:
  no employer requirement may demand output greater than two toneladas of
  caña OR a land extension equivalent to one *tarea* (task — the cutting of
  six *surcos* (furrows) by fourteen *brazadas* (armspans) in *resiembras*
  (replantings), six by ten in *plantillas* (new plantings)) in a single
  jornada; the cap is per-jornada, and the tarea's metric quantification is
  a configurable parameter (OQ-004). (LB-007; EVID-192)
- **SV-PAY-FR-018:** The system shall remunerate additional cortes (cuts
  beyond the ordinary rendimiento of the jornada) at the Art. 3 scale —
  every additional tonelada, arroba or libra is paid the same unit tariff,
  with the cap of FR-017 bounding what may be REQUIRED, never what may be
  paid. (LB-007; EVID-192)
- **SV-PAY-FR-019:** The system shall accrue the descanso semanal
  prestación for piece-rate collection workers on the Art. 6 table per CT
  Art. 90 inciso 3º — caña $1.673 per tarea and $0.836 per tonelada, café
  $0.335 per arroba, from the sidecar — keeping this prestación table
  DISTINCT from the Art. 3 production tariffs (the tarea prestación has no
  Art. 3 counterpart rate; the tonelada/arroba prestación values are
  separate rows, never merged with the $5.018/$2.007 production rates); the
  accrual mechanics and the séptimo-día engine consuming these rates belong
  to `03_working-time-surcharges.md`, and the prestación classifies as
  *prestación social* per `01_salary-model.md` SV-PAY-FR-004. (LB-009;
  EVID-192)

### 3.3 Routing and benefit bases (16_ Arts. 4, 7)

- **SV-PAY-FR-020:** The system shall route *trabajadores a domicilio*
  (home workers) in the covered rubros to the sector tariff corresponding to
  the work performed (time-based or piece-rate), so their floors, tariffs
  and prestación bases equal those of on-site workers of the same sector;
  their *salario básico* derivation remains the SB-R6 rule of
  `01_salary-model.md` SV-PAY-FR-006 (hourly básico = daily ÷ 8). (LB-001;
  LB-005; LB-008; EVID-191/192/208)
- **SV-PAY-FR-021:** The system shall compute every CT benefit payment —
  día de asueto (public holiday), vacaciones (vacation), aguinaldo
  (year-end bonus), indemnizaciones (severance) and other CT prestaciones —
  for SMM-level workers on the base of the applicable sector DAILY SMM,
  except when the stipulated salary is higher: benefit base =
  max(actual daily salary, sector daily SMM), with the sector daily SMM
  read from the dated sidecar rows; consumer files 03, 04 and 07 read this
  rule instead of re-deriving their bases. (LB-010; EVID-192)

### 3.4 SMM-indexed anchor interfaces (SOQ-18)

- **SV-PAY-FR-022:** The system shall expose a single SMM sector-mapping
  configuration consumed by every SMM-indexed rule in the corpus: PINNED —
  the aguinaldo ISR-exempt floor = 2× the MONTHLY SMM of the *comercio y
  servicios* sector (Ley ISR Art. 4.16 rule owned by
  `taxation/04_isr-withholding.md` SV-TAX-FR-120; from the Decreto 11-2025
  row, $408.80 valid_from 2025-06-01 → floor $817.60); UNPINNED —
  configurable sector selection with a documented default for (a) the FE
  receptor identification threshold ≥3 SMM (consumer:
  `e-invoicing/01_document-types.md` OQ-007) and (b) the 25-SMM ISR
  cash-payment ban threshold (consumer: `taxation/02_isr-deductions.md`
  OQ-002); the configuration shall name its consumers and never encode
  SMM values itself (values always read from the dated sidecar).
  (LB-006; EVID-191; SOQ-18)
- **SV-PAY-FR-023:** The system shall feed the 4×SMM indemnización cap of
  CT Art. 58 — no countable salary above four times the current legal daily
  SMM — from this file's dated DAILY tariff rows through the FR-022
  sector-mapping configuration (the article names no sector; EVID-207
  doubt); the cap ARITHMETIC is owned by `07_contracts-termination.md`
  SV-PAY-FR-106 (forward reference by file — resolved: 07's FR-106 has
  landed) — this FR supplies only the dated values and
  the selection config. (LB-011; EVID-207)

## 4. Data Model

Machine-readable sidecar lives next to this markdown file: `smm_2025.csv`
(the Decreto 11-2025 tariffs, verbatim — four time-based sectors ×
month/day/hour + the Art. 3 piece rates + the Art. 6 descanso prestación
rows). CSV discipline: comma-separated, header row, LF endings; amounts
EXACTLY as printed — the three-decimal values are preserved digit-for-digit
and NEVER rounded or recomputed (daily ≠ monthly/30; the note column carries
[sic] flags and provenance per the `withholding_tables.csv` precedent,
SOQ-20); empty valid_to = current vintage (open-ended); sector keys are
ASCII snake_case aliases of the D.O. Spanish sector names (agricola ·
industria · comercio_y_servicios · maquila_textil_y_confeccion ·
recoleccion_cana · recoleccion_cafe); loaders select rows by (sector,
tariff_type, unit) with valid_from ≤ period date, flagging lookups that
predate 2025-06-01 (OQ-001 — the 2021 vintage rows are intentionally absent
and must not be invented). Layer semantics: payroll is Odoo-native — all
entities below live in the client (wave default `odoo`; see §5).

**SMM tariff store and floors:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.smm.tariff (new) | decree, valid_from, valid_to, sector, tariff_type, unit, amount, note | date/select/monetary/char | seeded from `smm_2025.csv`; tariff_type: time_based · piece_rate · descanso_prestacion; unit: month · day · hour · tonelada · arroba · libra · tarea; note carries [sic] flags | FR-011, FR-016, FR-019 |
| hr.contract | sv_pay_smm_sector | select | agricola · industria · comercio_y_servicios · maquila_textil_y_confeccion · recoleccion_cana · recoleccion_cafe (sector definitions per LB-005; collection rubros floor to the agrícola tariff) | FR-011, FR-013, FR-020, FR-021 |
| hr.contract | sv_pay_smm_substituted | boolean (computed, dated) | de-pleno-derecho floor-validation flag: contract wage < current-vintage applicable tariff → true; re-evaluated on every dated-row change | FR-014 |
| hr.payslip | sv_pay_smm_floor_topup | monetary (computed) | Art. 147 per-jornada top-up for piece-rate days (production pay → sector daily SMM) | FR-013 |
| l10n_sv.smm.piecework.config (new) | max_toneladas_jornada, tarea_geometry | numeric / char (config) | 2 toneladas per jornada; tarea = 6 surcos × 14 brazadas (resiembras) / 6 surcos × 10 brazadas (plantillas); metric quantification configurable (OQ-004) | FR-017 |

**SMM-indexed sector mapping (SOQ-18):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.smm.sector.mapping (new) | consumer_rule, sector, pinned, default_note | select/boolean/char | aguinaldo_floor_2smm → comercio_y_servicios (pinned = true; Ley ISR Art. 4.16 via taxation/04 SV-TAX-FR-120); fe_receptor_3smm (e-invoicing/01 OQ-007) · isr_cash_ban_25smm (taxation/02 OQ-002) · indemnizacion_cap_4x (CT Art. 58, file 07) → configurable sector, pinned = false, documented default required (OQ-002) | FR-022, FR-023 |

Category-matrix cross-reference: piece-rate production pay classifies as
ordinary pay and the Art. 6 prestación as *prestación social* per the
canonical matrix of `01_salary-model.md` §4 (SV-PAY-FR-004) — consumed by FR
id; this file restates no matrix rows.

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr / hr_payroll module
family) — every FR maps `odoo`; no SaaS rows are introduced because none of
these FRs touch DTE generation/transformation (an architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`). Model names
are stable across Odoo 17/18/19/20; no version-specific behavior is required
beyond the dated-data regime below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-011 | odoo | l10n_sv.smm.tariff | CSV seeding | Version regime (D12): Decreto 11-2025 valid_from 2025-06-01 (D.O. 95 T.447 23-May-2025); 2021 pair repealed-and-absent (OQ-001); [sic] three-decimal fidelity in the note column (SOQ-20); triennial re-issue cadence (CT Art. 159) |
| FR-012 | odoo | hr.payslip (computation) | jornada proration | 5-8h → full daily SMM; <5h → hourly tariff × hours unless completing the semana laboral; hourly values read as printed (never monthly ÷ scale) |
| FR-013 | odoo | hr.payslip | sv_pay_smm_floor_topup | Per-jornada floor for destajo/obra/precio alzado + Art. 3 rubros; collection floors to the agrícola daily row |
| FR-014 | odoo | hr.contract | sv_pay_smm_substituted | Auto-substitution on dated-row change (validation flip); mejores derechos adquiridos never reduced; irrenunciabilidad (16_ Art. 8) |
| FR-015 | odoo | hr.payslip (computation) | monthly parity rule | Monthly SMM identical for 28/29/30/31-day months; no proration of the monthly figure |
| FR-016 | odoo | hr.payslip (piecework lines) | unit tariffs × production | $5.018/t · $2.007/arroba · $0.080/lb as printed; fractional units paid proportionally; category per 01-file FR-004 |
| FR-017 | odoo | l10n_sv.smm.piecework.config | rendimiento caps | 2 t or 1 tarea per jornada; tarea geometry configurable (OQ-004) |
| FR-018 | odoo | hr.payslip (piecework lines) | additional cuts | Beyond-ordinary output paid on the same Art. 3 scale; cap bounds requirements, not pay |
| FR-019 | odoo | hr.payslip (prestación line) | Art. 6 accrual | $1.673/tarea · $0.836/t · $0.335/arroba as printed; kept distinct from Art. 3 rows; séptimo-día engine in file 03 |
| FR-020 | odoo | hr.contract | sv_pay_smm_sector routing | A domicilio workers take their rubro's sector tariff; básico via 01-file SB-R6 (FR-006) |
| FR-021 | odoo | hr.salary.rule / hr.payslip | benefit-base selection | base = max(actual daily salary, sector daily SMM) for asueto/vacaciones/aguinaldo/indemnización; consumers: files 03, 04, 07 |
| FR-022 | odoo | l10n_sv.smm.sector.mapping | consumer config | Pinned: aguinaldo floor → comercio y servicios ($408.80 → $817.60, taxation/04 SV-TAX-FR-120); unpinned: FE threshold (e-invoicing/01 OQ-007), 25-SMM ban (taxation/02 OQ-002) — OQ-002 defaults |
| FR-023 | odoo | l10n_sv.smm.sector.mapping + l10n_sv.smm.tariff | 4×SMM cap feed | CT Art. 58 daily-tariff feed; arithmetic owned by 07_contracts-termination.md FR-106 (forward reference resolved — landed) |

Version-regime notes (D12): the only dated values in scope are the SMM tariff
rows (Decreto 11-2025, valid_from 2025-06-01). The repealed 2021 vintages
are absent from the corpus (OQ-001) — loaders flag pre-2025-06-01 lookups
rather than interpolating; new vintages arrive per the CT Art. 159 triennial
review cadence and append as new valid_from rows. The three-decimal prints
are transcription-fidelity constants (SOQ-20/OQ-003) and survive re-issues
only as re-printed.

## 6. Acceptance Criteria

- **AC-001:** Given an industria worker whose contract fixes a daily wage of
  US$13.00 in force at 2025-06-01, when the Decreto 11-2025 vintage becomes
  operative, then the contract's floor validation flips to substituted and
  payroll pays the sector daily tariff US$13.440 [sic, as printed] — the de
  pleno derecho substitution — while a US$15.00 contract is untouched
  (better stipulation stands) (FR-011, FR-014).
- **AC-002:** Given a comercio y servicios worker on a 6-hour jornada, then
  the day pays the FULL daily SMM US$13.440; given a 3-hour day NOT
  completing the semana laboral, then the pay is proportional — 3 ×
  US$1.680 = US$5.04; given the same 3-hour day worked to complete the
  working week, then the full US$13.440 is owed (FR-012).
- **AC-003:** Given a caña piece worker who cuts 1.5 toneladas in one
  jornada, then production pay = 1.5 × US$5.018 = US$7.527, the Art. 147
  floor tops the day up to the agrícola daily SMM US$10.035 (top-up
  US$2.508), and the employer may not REQUIRE more than 2 toneladas or one
  tarea-equivalent per jornada (FR-013, FR-016, FR-017).
- **AC-004:** Given a caña piece worker paid per tonelada with 10 toneladas
  in the week, then the Art. 6 descanso prestación = 10 × US$0.836 =
  US$8.36; given a tarea-paid worker with 6 tareas, then 6 × US$1.673 =
  US$10.038 — never mixed with the Art. 3 production rates (FR-019).
- **AC-005:** Given the CSV comercio_y_servicios month row US$408.80
  (valid_from 2025-06-01), then the aguinaldo ISR-exempt floor handed to
  `taxation/04_isr-withholding.md` SV-TAX-FR-120 is 2 × 408.80 = US$817.60,
  and no other sector row feeds that consumer (pinned mapping) (FR-022).
- **AC-006:** Given an agrícola monthly-salary worker, then February (28
  days) and July (31 days) of the same vintage both pay US$305.23 — the
  monthly tariff is never prorated by month length (FR-015).
- **AC-007:** Given a worker whose actual daily salary is US$9.00 against a
  sector daily SMM of US$10.035, then asueto, vacaciones, aguinaldo and
  indemnización bases compute on US$10.035; given an actual daily salary of
  US$15.00, then the bases compute on US$15.00 (max rule) (FR-021).
- **AC-008:** Given a trabajadora a domicilio sewing in the maquila textil y
  confección rubro, then her floors and tariffs are the maquila sector rows
  (month US$402.32 / day US$13.227 / hour US$1.653 as printed), with the
  hourly básico derived per SB-R6 (daily ÷ 8) (FR-020).
- **AC-009:** Given a payslip dated 2025-05-15 (before the earliest corpus
  vintage), then the tariff lookup flags OQ-001 and blocks floor validation
  — no 2021-pair value is invented or interpolated (FR-011).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Prior SMM vintages absent (16_ OQ-3 / D12): the repealed 2021 pair (D.E. 9/10-2021, in force 1-Ago-2021) is not in the corpus, so floor validation, substitution checks and SMM-indexed anchors cannot be computed for periods before 2025-06-01; historical rows would need the 2021 decrees (acquisition optional, source numbering ≥66) and are NEVER invented. | no | Takumi S4 (sources watch) | open |
| OQ-002 | SOQ-18 carried: which sector's SMM feeds each UNPINNED SMM-indexed rule — the FE receptor threshold ≥3 SMM (`e-invoicing/01_document-types.md` OQ-007), the 25-SMM ISR cash-payment ban (`taxation/02_isr-deductions.md` OQ-002) and the 4×SMM indemnización cap (CT Art. 58 "salario mínimo diario legal vigente", EVID-207) — plus the kin sector-selection working reading of FR-013 (the Art. 3 collection-rubros per-jornada floor maps to the agrícola row: café express in the sector definition, caña via the "otras actividades agrícolas" catch-all, LB-005)? FR-022 ships configurable selection with documented defaults; MH guidance hunt pending. | no | Takumi S4 + taxation/e-invoicing consumers | open |
| OQ-003 | SOQ-20 carried (16_ OQ-1): the three-decimal prints of the Art. 2 daily/hourly tariffs and the Art. 6 prestación table are transcribed exact-as-printed with [sic] flags (both PSM 4 and PSM 6 reads agree; daily ≠ monthly/30 confirms they are gazette constants); optional gazette re-verification when the D.O. /seleccion route recovers (kin of the SOQ-03 discipline). Not blocking. | no | Takumi S4 (sources registry) | open |
| OQ-004 | Tarea metric quantification: Art. 3 c) defines the tarea as the cut of six surcos × fourteen brazadas (resiembras) or six × ten (plantillas), and caps the required rendimiento at 2 toneladas or a tarea-equivalent extension per jornada — but the corpus never quantifies the brazada/surco metric in area terms, so the ton ↔ tarea equivalence for cap enforcement is a configurable parameter pending producer-side quantification guidance. | no | Takumi S4 (payroll config) | open |
