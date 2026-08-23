# SV — Taxation — Foreign-agents special levy (96_ Chapter V): the 30% impuesto on mandante-financed transactions to Agentes Extranjeros — the dated rate row (valid_from 2025-06-07), the RAEX-gated in-kind hecho generador, retention at source by the two-limb Agentes de Retención Especial (SSF institutions general / NPO-qualified catch-all), DGT enteros within the 10 first días hábiles, the 15-días-hábiles electronic reports, the domestic-donation monthly self-entero, the Art. 14 informe to DGII, CT 246/247/241 sanction routing, CT supletorio and the ISR/IVA track separation (Ley de Agentes Extranjeros, D.L. 308-2025, Arts. 10-17 + 25 + considerando IV)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (W20 fold-in, in review) |
| Authors | Takumi W20 + controller |
| Updated | 2026-08-23 |

## 1. Purpose

This file defines the functional requirements for the **Chapter V special
levy** of El Salvador's *Ley de Agentes Extranjeros* (D.L. N° 308-2025,
D.O. N° 100 T.447, 30-may-2025): the **30% impuesto sobre transacciones**
— every financial transaction effected by a foreign mandante in favor of
its Agentes Extranjeros obligates the payment of the tax (Art. 10 hecho
generador), at **30% per covered transaction** (Art. 11: transacción
financiera, desembolso, transferencia, *importación en especies o bienes
materiales de cualquier tipo* — a hecho generador ONLY *cuando así lo
determine el Registro de Agentes Extranjeros* — *o cualquier otro*
concepto, all *provenientes de fondos del mandante extranjero*), carried
as a DATED rate row (valid_from **2025-06-07**, provenance 96_ Art. 11 +
Art. 25); collection **by retención at source** (Art. 12) effected at
the moment the mandante transfers or places funds at disposal *por
cualquier modalidad, en las cuentas que tales instituciones o entidades
administren o gestionen*; the **TWO-LIMB Agentes de Retención Especial**
scope (Art. 13): limb A = SSF-supervised financial-system institutions
(general — retain on all covered transactions), limb B = any other
entity, mechanism or person intervening in the reception/canalization/
transfer of funds *desde el exterior a favor de organizaciones sin
fines de lucro* — the NPO qualifier rides limb B, never limb A; the
**entero** of the FULL retained sum (*sin deducción alguna*) to
the Dirección General de Tesorería within the **ten first días hábiles**
of the following month; the retained agents' **electronic report**
within the **fifteen first días hábiles**; the **monthly 30%
self-entero on DOMESTIC donations** (gross, within the ten días hábiles
after the monthly close); the **Art. 14 retention-subject agents' own
informe** to the DGII (NIT + names + amounts + donations + enteros,
fifteen first días hábiles); the **sanction routing** of Art. 15 (CT
Arts. 246/247/241 — the CT catalog 05_-encoded by pointer, the
sanction-base/reincidencia/deuda architecture consumed by id from
`16_ct-procedures.md`); the **CT supletorio** and the law's Art. 5
exclusion application of Art. 17; the **ISR no-prejudice** awareness
row (considerando IV → Ley ISR Art. 3 num. 4); the **RAEX
subject-identification interface** (`special-regimes/01` by id — the
MIGOB freeze/prohibitions informational only); and the
**track-separation invariant** — this levy's retention/entero/report
engine is a THIRD track, never merged with the ISR retention tables
(`taxation/04`) nor the IVA retention matrix (`taxation/13`).

It does **not** cover: the RAEX registro machinery itself — inscription
duties, the 90-day transitory, exclusion calificación procedure,
labelled-propaganda/anonymous-funding prohibitions and the MIGOB multas
(`special-regimes/01_regime-framework.md` SV-SPE-FR-201, by id — this
file only READS the registration-state field); the CT sanction article
values (Arts. 246/247/241 — 05_-encoded catalog, by pointer) and the
sanction-BASE computation, reincidencia windows and deuda-tributaria
architecture (`taxation/16_ct-procedures.md` SV-TAX-FR-380..382, by
id); the ISR retention tables (CT 154-160 —
`taxation/04_isr-withholding.md` SV-TAX-FR-121..131, by id) and the IVA
retention matrix (CT 161/162/162-A/162-B —
`taxation/13_iva-retentions.md`, its SV-TAX-FR-319 separation invariant
extended here — separation statement only, never merged matrices); the
días-hábiles computation engine (`fiscal-reporting/08_filing-calendar.md`
SV-FREP-FR-202..204, by id — all levy deadlines COMPUTE on it, none
re-derived); the AT-provided forms of Arts. 13/14 and any MH Art. 16
instrument (acuerdos/instructivos/circulares/resoluciones/guías) —
authority-side; this file ships NO form/format defaults (OQ-2, the
Art. 16 delegation being the statutory root of the acquisition watch);
the fiscal declaration surface (no F-form/declaration instrument for
the levy exists in the corpus — OQ-4 pointer to a future
fiscal-reporting wave); and the non-fiscal surfaces of 96_ (Chapters
I-IV and VI: transparency, registro, propaganda, MIGOB procedure —
`special-regimes/01` territory by id).

## 2. Legal Basis

Authority order (binding, per master index W20-A / cluster L1): the
special levy is **96_ = D.L. N° 308, Ley de Agentes Extranjeros** (Salón
de Honor del M. de Relaciones Exteriores 20-may-2025; Casa Presidencial
29-may-2025; D.O. N° 100 T.447, 30-may-2025, issue pp. 3-18 — 16 pp /
25 arts + CAPS) — a CURRENT LAW single print (no consolidation layer);
**post-print reform watch rides every LB row below** (corpus cadance:
re-verify at implementation). Chapter V (*Régimen Fiscal y Obligaciones
Tributarias*, Arts. 10-17) is the fiscal surface; Art. 25 vigencia:
"ocho días después de su publicación" → 30-may-2025 + 8 = **7-jun-2025**
(instrument-computed; EVID-396) — the dated rate row's `valid_from`.
**Quote discipline (96_, per the EV header):** the D.O. body was
scanned → the txt is forced OCR (tesseract spa PSM 4); unambiguous
intra-word artifacts are normalized, ambiguous readings kept as OCR'd
with [sic], no wording altered. The Art. 13 entero sentence's
EVID-397 reading "sin dedcción" is an unambiguous OCR artifact
(EVID-397 Doubts: "[sic OCR] = sin deducción"; W20-A carries the
same variant reading), normalized in the extraction txt (line 355);
quotes below carry the normalized txt form per the verbatim-sweep
norm, the variant reading noted at LB-004. **V1 citation rule:** every LB row below
cites 96_ with the EVID id (EVID-396/397,
`95_96_97_SpecialIncentives.evidence.md`) and the txt PAGE/line anchors
of `96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30_pp3-18.pdf.txt`
(verified this task). **D15 (binding):** the 30% rate is a DATED row —
valid_from 2025-06-07, provenance 96_ Art. 11 (rate) + Art. 25
(vigencia arithmetic); corrections use ORIGINAL-period parameters; the
article text is implemented AS PRINTED.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Agentes Extranjeros (D.L. 308-2025), Art. 10 | "Las transacciones financieras realizadas por los mandantes extranjeros a favor de sus agentes extranjeros, genera la obligación del pago del impuesto establecido en esta Ley." | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 10 (EVID-397; verified 96_ txt PAGE 9, lines 297-301) |
| LB-002 | Ley de Agentes Extranjeros, Art. 11 | "Por cada transacción financiera, desembolso, transferencia, importación en especies o bienes materiales de cualquier tipo, o cualquier otro, y que sean provenientes de fondos del mandante extranjero, ya sea a través de donaciones, pagos u otros conceptos, a favor de sus Agentes Extranjeros en el país, se aplicará un impuesto del 30%." … "En el caso de las importaciones en especie o bienes materiales de cualquier tipo, estas constituyen hecho generador cuando así lo determine el Registro de Agentes Extranjeros." … "El impuesto gravado a que se refiere este artículo será destinado por el Ministerio de Hacienda para fines de interés público, general o social." | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 11 (EVID-397; verified 96_ txt PAGE 9-10, lines 303-321) |
| LB-003 | Ley de Agentes Extranjeros, Art. 12 | "El impuesto a que se refiere el artículo que antecede será percibido mediante una retención, la cual será efectuada directamente por las instituciones del Sistema Financiero, así como por cualquier otra entidad, mecanismo, persona natural o jurídica que intervenga en la recepción, canalización o transferencia de fondos desde el exterior a favor de organizaciones sin fines de lucro, independientemente de que se encuentren o no sujetas a la supervisión de la Superintendencia del Sistema Financiero." … "La retención deberá efectuarse al momento en que, por medio de dichas entidades o mecanismos, los mandantes extranjeros realicen las respectivas transferencias de dinero o los pongan a disposición de sus agentes, por cualquier modalidad, en las cuentas que tales instituciones o entidades administren o gestionen." | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 12 (EVID-397; verified 96_ txt PAGE 10, lines 323-335) |
| LB-004 | Ley de Agentes Extranjeros, Art. 13 (designation + entero + report blocks) | "Para efectos de lo dispuesto en los artículos precedentes, se designan como responsables en carácter de Agentes de Retención Especial de dicho impuesto, a las instituciones y entidades sujetas bajo supervisión de la Superintendencia del Sistema Financiero, así como a aquellas personas naturales o jurídicas, entidades o mecanismos que, aun sin estar sujetas a dicha supervisión, intervengan en la recepción, canalización o transferencia de fondos provenientes del extranjero a favor de organizaciones sin fines de lucro, Los agentes de retención deberán enterar a la Administración Tributaria las cantidades retenidas, conforme a las reglas y plazos establecidos en este artículo." … "Las sumas que retengan los Agentes de Retención Especial deberán enterarlas sin deducción alguna, a la Dirección General de Tesorería, en cualquiera de las oficinas que esta institución tenga en el país y en los bancos autorizados por el Ministerio de Hacienda, mediante los formularios que para tal efecto disponga la Administración Tributaria, dentro de los diez primeros días hábiles del mes siguiente al periodo tributario en que se hicieron las retenciones." … "Además, los citados Agentes de Retención tienen la obligación de remitir dentro de los quince primeros días hábiles del mes siguiente al período tributario en el cual se efectuaron las retenciones, un informe por medios electrónicos de los Agentes Extranjeros a quiénes se les efectuaron las mismas, bajo las especificaciones técnicas y en los formularios que la Administración Tributaria proporcione." — EVID-397/W20-A carry the OCR variant "sin dedcción" [sic OCR]; the txt (line 355) prints the normalized "sin deducción" (EV-header PSM-4 discipline), quoted here | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 13 first/second blocks (EVID-397; verified 96_ txt PAGE 10-11, lines 339-365; normalization at txt line 355) |
| LB-005 | Ley de Agentes Extranjeros, Art. 13 (donations ¶) | "Respecto de las donaciones que les pudieran ser efectuadas a los Agentes Extranjeros dentro del territorio nacional, éstos últimos estarán obligados a enterar el 30%.en concepto del impuesto instituido, en la presente Ley, en atención de las sumas que reciban en tales conceptos. Los enteros se determinarán por períodos mensuales, respecto de las donaciones brutas recibidas, los que deberán verificarse a más tardar dentro de los diez días hábiles que sigan al del cierre del período mensual en que se recibieron, mediante formularios que proporcionará la Administración Tributaria." | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 13 donations ¶ (EVID-397; verified 96_ txt PAGE 11, lines 367-373) |
| LB-006 | Ley de Agentes Extranjeros, Art. 14 | "Los Agentes Extranjeros que hubieren sido sujetos de retenciones del mencionado impuesto o que hubieren efectuado enteros relacionados a las donaciones recibidas en el territorio nacional, tienen la obligación de remitir dentro de los quince primeros días hábiles del mes siguiente al período tributario en el cual se efectuaron las retenciones y/o realizaron los enteros, un informe por medios electrónicos, con las especificaciones técnicas y en los formularios que la Administración Tributaria establezca. Dicho informe deberá contener el Número de Identificación Tributaria y nombre del Agente Extranjero sujeto de retención, los mismos datos respecto de los Agentes de Retención Especial, así como los montos sujetos a retención y las retenciones que le hubieren efectuado; de igual. manera fespecto del monto de las donaciones que le hubieren realizado en el país y de los respectivos enteros por este último concepto. Este informe deberá ser presentado a la Dirección General de Impuestos Internos del Ministerio de Hacienda." — txt OCR "de igual. manera fespecto" = "de igual manera respecto" (intra-word artifacts, EV-header normalization) | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 14 (EVID-397; verified 96_ txt PAGE 12, lines 380-395) |
| LB-007 | Ley de Agentes Extranjeros, Art. 15 | "Las' conductas que constituyan incumplimientos con relación a la obligación de retener y enterar por parte de los Agentes de Retención Especial, reguladas en el-presente capítulo, serán sancionadas por la Administración Tributaria, con base en lo estipulado en el artículo 246 del Código Tributario." … "Los incumplimientos de los Agentes Extranjeros relativos a la obligación de enterar el impuesto sobre donaciones recibidas en el territorio nacional, deberán ser sancionadas por la misma Administración, con base a lo regulado en el artículo 247 del Código Tributario." … "Por su parte, el incumplimiento a las obligaciones de informar establecidas en este artículo, serán sancionadas por la Administración Tributaria, en lo que le resulte aplicable, por lo dispuesto en el artículo 241 del Código Tributario." — txt OCR artifacts "Las'" / "el-presente" kept as printed (= "Las" / "el presente"); the third ¶'s "en este artículo" reads on the chapter's reporting obligations (Arts. 13/14) — quoted as printed | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 15 (EVID-397; verified 96_ txt PAGE 12-13, lines 397-416) |
| LB-008 | Ley de Agentes Extranjeros, Art. 16 | "Se faculta al Ministerio de Hacienda, para que por sí'o a través de la Dirección General de Impuestos Internos y la Dirección General de Tesorería, para que dentro de sus respectivas competencias, en caso de ser necesario, pueda emitir los acuerdos, instructivos, circulares, resoluciones, guías o cualquier otro acto o instrumento administrativo, que sea necesario e indispensables, con la finalidad de evacuar consultas, o aclarar aspectos relacionados con la aplicación de lo dispuesto en el presente capítulo." — the doubled "para que" and "necesario e indispensables" are as printed; txt OCR artifacts "sí'o" kept as printed (= "sí o"); "con_.la" normalized to "con la" per EV header | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 16 (EVID-397; verified 96_ txt PAGE 13, lines 418-426) |
| LB-009 | Ley de Agentes Extranjeros, Art. 17 | "Con el objeto de darle cumplimiento a lo regulado en el presente capítulo, se aplicarán, con carácter supletorio; las disposiciones contenidas en el Código Tributario." … "Se aplicarán-de igual forma, en el presente capítulo, las exclusiones que se establezcan de conformidad con lo dispuesto en esta Ley." — txt punctuation artifacts "supletorio;" / "aplicarán-de" kept as printed | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 17 (EVID-397; verified 96_ txt PAGE 13, lines 428-435) |
| LB-010 | Ley de Agentes Extranjeros, Art. 25 + considerando IV | Art. 25: "El presente decreto entrará en vigencia ocho días después de su publicación en el Diario Oficial." Considerando IV (closing): "…es oportuno, por una parte, llevar un registro al respecto, con la finalidad de promover la transparencia en el funcionamiento de estas y, por otra parte, regular impositivamente las operaciones financieras que reciben a través de transferencias de recursos, en sus distintas modalidades, con el propósito de financiar'o no sus actividades particulares en el territorio nacional, a fin de que con ello, contribuyan tributariamente de una forma razonable y general, como lo hacen otros sujetos, en similares circunstancias, sin perjuicio de lo dispuesto en el artículo 3, numeral 4, de la Ley de Impuesto Sobre la Renta." — txt prints "da Renta" for "de la Renta"; the intra-word period in "transferencias.de recursos" dropped and the stray quote in 'lo "dispuesto' removed (unambiguous PSM-4 normalizations per EV header); "financiar'o" kept as printed; vigencia arithmetic: D.O. 30-may-2025 + 8 días = **7-jun-2025** | `sv/sources/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30.pdf` | Art. 25 (EVID-396; verified 96_ txt PAGE 16, line 538) + considerando IV (EVID-396/397; verified 96_ txt PAGE 2, lines 39-49) |

Separation and boundary notes (per W20-A): the CT articles routed by
Art. 15 (246/247/241) are **05_-encoded catalog rows consumed by
pointer** — never restated here; the sanction-BASE computation,
reincidencia windows and deuda-tributaria architecture are
`taxation/16` rows consumed **by id** (SV-TAX-FR-380..382); the RAEX
registration/exclusion machinery is `special-regimes/01` (SV-SPE-FR-201,
by id); the ISR retention tables (taxation/04) and the IVA retention
matrix (taxation/13) are NEVER merged with this levy's engine (FR-416).
The post-print reform watch (current law, single print) rides every LB
row above.

## 3. Functional Requirements

### 3.1 The impuesto — hecho generador, rate and breadth (Arts. 10-11)

- **SV-TAX-FR-405:** The system shall implement the Chapter V levy
  establishment: the hecho generador is "las transacciones financieras
  realizadas por los mandantes extranjeros a favor de sus agentes
  extranjeros" (Art. 10) — every financial transaction effected by a
  foreign mandante in favor of its Agentes Extranjeros obligates the
  payment of the impuesto; the rate is EL TREINTA POR CIENTO (30%) per
  each covered transaction (Art. 11), carried as ONE dated config row
  `l10n_sv.special_levy.rate` — valid_from **2025-06-07**, rate 0.30,
  provenance "96_ D.L. 308-2025 Art. 11 (rate) + Art. 25 (vigencia:
  ocho días después de publicación; D.O. 30-may-2025 → 7-jun-2025)" —
  NEVER a hardcoded constant (D15: the dated row governs; corrections
  use original-period parameters); the retention base is the FULL
  amount of each transacción financiera/desembolso/transferencia
  (or in-kind value per FR-406) proveniente de fondos del mandante
  extranjero — the law prints NO floor and NO base deduction; the
  destination clause (Art. 11 final ¶: MH destines the proceeds "para
  fines de interés público, general o social") is recorded as
  informational metadata only.
  (LB-001; LB-002; LB-010; EVID-397/396)
- **SV-TAX-FR-406:** The system shall implement the taxable-event
  breadth EXACTLY as printed: (a) the enumerated concepts —
  *transacción financiera, desembolso, transferencia, importación en
  especies o bienes materiales de cualquier tipo* — plus the
  **"o cualquier otro"** catch-all concepto (kept as printed, an
  open-text concept class, not an enumerated closure); (b) the
  provenance qualifier — all covered concepts must be "provenientes de
  fondos del mandante extranjero, ya sea a través de donaciones, pagos
  u otros conceptos" (mandante-funded origin, any channel); and (c) the
  IN-KIND GATE: "las importaciones en especie o bienes materiales de
  cualquier tipo" constitute hecho generador ONLY "cuando así lo
  determine el Registro de Agentes Extranjeros" — an in-kind import
  triggers the levy ONLY when a RAEX determination row exists for it
  (`l10n_sv.special_levy.in_kind.determination` config, RAEX-side
  provenance); NO default enumeration and NO auto-trigger ship (the
  determination mechanics are unknown — OQ-3; value discipline: nothing
  invented).
  (LB-002; EVID-397)

### 3.2 Collection — retention at source and the two-limb agents (Arts. 12-13)

- **SV-TAX-FR-407:** The system shall implement collection as
  RETENCIÓN at source: the impuesto "será percibido mediante una
  retención" effected directly by the Art. 12 institutions and
  entities, at the MOMENT "en que, por medio de dichas entidades o
  mecanismos, los mandantes extranjeros realicen las respectivas
  transferencias de dinero o los pongan a disposición de sus agentes,
  por cualquier modalidad, en las cuentas que tales instituciones o
  entidades administren o gestionen" — the retention moment is the
  transfer-or-availability event on the administered accounts, ANY
  modality; the retention documentation surface is the AT-provided
  formularios ("mediante los formularios que para tal efecto disponga
  la Administración Tributaria", Arts. 13/14) — a config-gap shipping
  NO document/format defaults (OQ-2); the retained amount posts to the
  levy retention ledger of FR-416 (own track).
  (LB-003; LB-004; EVID-397)
- **SV-TAX-FR-408:** The system shall implement the TWO-LIMB Agentes
  de Retención Especial scope: **LIMB A (general)** = "las instituciones
  y entidades sujetas bajo supervisión de la Superintendencia del
  Sistema Financiero" — they retain on ALL covered transactions (NO
  NPO qualifier limits limb A); **LIMB B (catch-all)** = "aquellas
  personas naturales o jurídicas, entidades o mecanismos que, aun sin
  estar sujetas a dicha supervisión, intervengan en la recepción,
  canalización o transferencia de fondos provenientes del extranjero a
  favor de organizaciones sin fines de lucro" — they retain ONLY on
  exterior funds destined to organizaciones sin fines de lucro; the NPO
  qualifier ("desde el exterior a favor de organizaciones sin fines de
  lucro") rides LIMB B and NEVER limb A; Art. 12's "independientemente
  de que se encuentren o no sujetas a la supervisión de la
  Superintendencia del Sistema Financiero" clause is limb-B supervision
  irrelevance (an SSF-supervised entity that also intervenes stays
  limb A — general), never an NPO-scope waiver on limb A. Each
  intervening entity carries an agent-limb classification
  (`ssf_general` · `npo_catchall`) resolving its retention scope.
  (LB-004; LB-003; EVID-397)

### 3.3 Enteros and reports (Art. 13)

- **SV-TAX-FR-409:** The system shall implement the entero: "Las sumas
  que retengan los Agentes de Retención Especial deberán enterarlas
  sin deducción alguna" (the FULL retained sum, nothing netted;
  EVID-397's variant "sin dedcción" [sic OCR] normalized per txt
  line 355), "a la Dirección General de
  Tesorería, en cualquiera de las oficinas que esta institución tenga
  en el país y en los bancos autorizados por el Ministerio de Hacienda,
  mediante los formularios que para tal efecto disponga la
  Administración Tributaria" (OQ-2 — no form defaults), "dentro de los
  diez primeros días hábiles del mes siguiente al periodo tributario
  en que se hicieron las retenciones" — the entero register carries
  period, full amount and a due-window computed on the SHARED
  días-hábiles engine (SV-FREP-FR-202..204, by id — asueto-aware,
  never calendar-day arithmetic).
  (LB-004; EVID-397; FREP 08-file SV-FREP-FR-202..204 by id)
- **SV-TAX-FR-410:** The system shall implement the retained agents'
  electronic report: the Agentes de Retención "tienen la obligación de
  remitir dentro de los quince primeros días hábiles del mes siguiente
  al período tributario en el cual se efectuaron las retenciones, un
  informe por medios electrónicos de los Agentes Extranjeros a quiénes
  se les efectuaron las mismas, bajo las especificaciones técnicas y
  en los formularios que la Administración Tributaria proporcione" —
  a report register (period · retained-upon Agentes Extranjeros rows ·
  due-window = the first fifteen días hábiles of the following month,
  engine-computed per SV-FREP-FR-202..204 by id); the specifications
  and formats are AT-provided — NO defaults ship (OQ-2).
  (LB-004; EVID-397; FREP 08-file SV-FREP-FR-202..204 by id)

### 3.4 The Agentes Extranjeros' own obligations (Art. 13 donations ¶ + Art. 14)

- **SV-TAX-FR-411:** The system shall implement the monthly
  domestic-donation self-entero: for "las donaciones que les pudieran
  ser efectuadas a los Agentes Extranjeros dentro del territorio
  nacional", the Agentes Extranjeros THEMSELVES "estarán obligados a
  enterar el 30%.en concepto del impuesto instituido, en la presente
  Ley, en atención de las sumas que reciban en tales conceptos" — the
  enteros "se determinarán por períodos mensuales, respecto de las
  donaciones brutas recibidas" (GROSS donations received, no
  deduction), verified "a más tardar dentro de los diez días hábiles
  que sigan al del cierre del período mensual en que se recibieron" — a
  FOLLOWING-LAPSO window (the ten días hábiles after the monthly
  close), distinct from FR-409's first-ten-of-month window — computed
  on the shared días-hábiles engine (SV-FREP-FR-202..204 by id),
  "mediante formularios que proporcionará la Administración
  Tributaria" (OQ-2); a monthly aggregate register per Agente
  Extranjero (month · gross received · 30% computed · due date).
  (LB-005; EVID-397; FREP 08-file SV-FREP-FR-202..204 by id)
- **SV-TAX-FR-412:** The system shall implement the retention-subject
  agents' own electronic informe: the Agentes Extranjeros "que
  hubieren sido sujetos de retenciones del mencionado impuesto o que
  hubieren efectuado enteros relacionados a las donaciones recibidas
  en el territorio nacional" must remit "dentro de los quince primeros
  días hábiles del mes siguiente al período tributario en el cual se
  efectuaron las retenciones y/o realizaron los enteros, un informe
  por medios electrónicos, con las especificaciones técnicas y en los
  formularios que la Administración Tributaria establezca" (OQ-2),
  containing: "el Número de Identificación Tributaria y nombre del
  Agente Extranjero sujeto de retención", "los mismos datos respecto
  de los Agentes de Retención Especial", "los montos sujetos a
  retención y las retenciones que le hubieren efectuado" and, "de
  igual manera respecto del monto de las donaciones que le hubieren
  realizado en el país y de los respectivos enteros por este último
  concepto" — presented "a la Dirección General de Impuestos Internos
  del Ministerio de Hacienda" (DGII, not DGT); due-window engine-
  computed (SV-FREP-FR-202..204 by id).
  (LB-006; EVID-397; FREP 08-file SV-FREP-FR-202..204 by id)

### 3.5 Sanctions, supletorio and interfaces (Arts. 15-17 + considerando IV)

- **SV-TAX-FR-413:** The system shall implement sanction ROUTING and
  the supletorio frame: (a) Agentes de Retención Especial breaches of
  the retener/enterar obligations → CT Art. 246; (b) Agentes
  Extranjeros breaches of the donation-entero obligation → CT Art.
  247; (c) breaches of the chapter's reporting obligations → CT Art.
  241 — the CT articles themselves are 05_-encoded (catalog consumed
  BY POINTER, never restated) and the sanction-BASE computation,
  reincidencia windows and deuda-tributaria architecture are consumed
  BY ID from `taxation/16` (SV-TAX-FR-380..382); (d) CT supletorio per
  Art. 17 ("se aplicarán, con carácter supletorio; las disposiciones
  contenidas en el Código Tributario") — 16's
  declaration-state/payments/prescription vocabulary consumed by id,
  never restated here; (e) the law's Art. 5 exclusion determinations
  (RAEX calificación "por periodos anuales, renovables
  automáticamente, o por cada proyecto en particular") apply to the
  chapter per Art. 17's final clause ("Se aplicarán-de igual forma…
  las exclusiones que se establezcan de conformidad con lo dispuesto
  en esta Ley") — carried as config slots on the levy subject
  (exclusion state + period), NO defaults (RAEX-side determination
  practice; OQ-1 kin).
  (LB-007; LB-009; EVID-397/396; TAX 16-file SV-TAX-FR-380..382 by id)
- **SV-TAX-FR-414:** The system shall implement the
  subject-identification interface consuming `special-regimes/01` BY
  ID: the levy's subject resolution (who is an Agente Extranjero for
  Chapter V purposes) reads the RAEX registration state carried by
  SV-SPE-FR-201 (`sv_raex_state` · `sv_raex_date`: unregistered ·
  registered · excluded) — the field is OWNED by spe/01 and never
  duplicated here; the MIGOB-side freeze/prohibitions (the
  unregistered total activity/asset freeze; suspension/cancelación of
  personería jurídica) are INFORMATIONAL ONLY — no tax machinery is
  duplicated and no levy computation keys on MIGOB sanction state
  (the levy keys on the covered-transaction facts plus the
  registration/exclusion state read by id).
  (LB-009; EVID-396 pointer; SPE 01-file SV-SPE-FR-201 by id)
- **SV-TAX-FR-415:** The system shall carry the ISR no-prejudice row
  (awareness-level; layer: shared): the levy applies "sin perjuicio de
  lo dispuesto en el artículo 3, numeral 4, de la Ley de Impuesto
  Sobre la Renta" (considerando IV) — the levy and the ISR obligations
  are INDEPENDENT: levy postings neither create, replace nor alter ISR
  bases, retentions or renta determinations (the Ley ISR Art. 3 num. 4
  renta concept and its D.L. 969-2024 foreign-source exclusion are
  54_/taxation territory, by id — never restated here); no levy
  amount ever flows into an ISR computation surface.
  (LB-010; EVID-396/397)
- **SV-TAX-FR-416:** The system shall keep this levy's
  retention/entero/report engine a STRICTLY SEPARATE THIRD TRACK:
  never merged with the ISR retention tables
  (`taxation/04_isr-withholding.md` SV-TAX-FR-121..131, by id) nor
  with the IVA retention matrix (`taxation/13_iva-retentions.md` —
  its SV-TAX-FR-319 ISR/IVA separation invariant EXTENDED here to a
  three-track invariant): one operation may carry a levy 30%
  retention AND an ISR retention AND an IVA retention as SEPARATE tax
  lines, each under its own engine, entero windows and reporting
  surfaces — never a merged line, never a cross-posted ledger
  (Chapter V read as a whole, LB-001..LB-009).
  (LB-001; LB-002; LB-003; LB-004; LB-005; LB-006; LB-007; LB-008;
  LB-009; EVID-397; TAX 04-file SV-TAX-FR-121..131 by id; TAX 13-file
  SV-TAX-FR-319 by id)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the 30% rate enters as ONE dated config
row with the post-print reform watch (§2) riding it. Layer semantics:
classification/timing/subject computation living in the LGPL client
(wave default `odoo`; see §5) — nothing here touches DTE generation.
**All due-dates/windows (FR-409/410/411/412) COMPUTE on the shared
días-hábiles engine consumed by id (SV-FREP-FR-202..204,
`fiscal-reporting/08_filing-calendar.md`) — no local calendar
arithmetic.** Interface entity for the wave's index and future
fiscal-reporting consumers: the dated rate row + the retention event
ledger + the entero/report/donation/informe registers below.

**Dated rate row (D15):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.special_levy.rate (new) | code, valid_from, rate, provenance | char / date / decimal / char | ONE row: `foreign_agents_30pct` · 2025-06-07 · 0.30 · "96_ D.L. 308-2025 Art. 11 + Art. 25" (vigencia arithmetic D.O. 30-may-2025 + 8 días); corrections use original-period parameters | FR-405 |

**Retention events (move-line surface):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (SV extension) | l10n_sv_special_levy_base, l10n_sv_special_levy_amount | monetary / monetary (computed) | levy base (full transaction amount from mandante funds) + 30% computed (rate row as-of the retention period, D15) | FR-405, FR-407 |
| account.move.line (SV extension) | l10n_sv_special_levy_agent_limb | select | `ssf_general` · `npo_catchall` — the intervening entity's limb (scope gate) | FR-408 |
| account.move.line (SV extension) | l10n_sv_special_levy_raex_determination_id | m2o | link to the in-kind determination row; empty = monetary transaction (no gate) | FR-406 |
| l10n_sv.special_levy.in_kind.determination (new, config) | partner, period, scope, provenance, state | m2o / char / char / char / select | RAEX "cuando así lo determine" rows — RAEX-side provenance REQUIRED, no default enumeration (OQ-3) | FR-406 |
| l10n_sv.special_levy.exclusion (new, config) | partner, basis, valid_from, valid_to, provenance | m2o / char / date / date / char | Art. 5 exclusion calificación applied to the chapter per Art. 17 final clause (annual-renewable or per-project); RAEX-side provenance, NO defaults (OQ-1 kin) | FR-413 |
| res.partner (SV extension) | l10n_sv_special_levy_agent_limb | select | `ssf_general` · `npo_catchall` · none — the entity's retention-agent limb classification (RAEX state itself is spe/01's field, consumed by id — NOT duplicated) | FR-408, FR-414 |

**Entero / report / donation / informe registers:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.special_levy.entero (new) | period, amount, due_window, state, form_ref | char / monetary / date-computed / select / char | full retained sum ("sin deducción alguna"); due = first 10 días hábiles of following month (engine by id); state: pending · entered; form_ref = AT formulario (OQ-2 — empty allowed, no default) | FR-409 |
| l10n_sv.special_levy.report (new) | period, due_window, retained_upon_ids, payload, form_ref | char / date-computed / m2m / binary / char | retained agents' electronic informe of retained-upon Agentes Extranjeros; due = first 15 días hábiles of following month (engine by id); AT specifications (OQ-2) | FR-410 |
| l10n_sv.special_levy.donation.entero (new) | month, gross_received, levy_computed, due_date, form_ref | date / monetary / monetary (computed) / date-computed / char | monthly aggregate per Agente Extranjero: 30% of gross domestic donations; due = 10 días hábiles AFTER month close (engine by id); AT formulario (OQ-2) | FR-411 |
| l10n_sv.special_levy.agent.informe (new) | period, due_window, nit, name, retention_agent_data, retention_amounts, donation_amounts, entero_amounts, form_ref | char / date-computed / char / char / binary / monetary / monetary / monetary / char | the Art. 14 informe to DGII (NIT + names + amounts + donations + enteros); due = first 15 días hábiles of following month (engine by id); AT-established format (OQ-2) | FR-412 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = classification/timing/subject
computation logic living in the LGPL client. No SaaS rows are
introduced: nothing here touches DTE generation or transformation;
this file supplies the rate row, the retention event ledger, the
limb-resolution logic and the entero/report/donation/informe
registers. Model names are stable across Odoo 17/18/19/20
(`account.move`, `account.move.line`, `res.partner`); version-specific
behavior is recorded per row where a legal vintage exists. D15
doctrine (binding): the 30% rate resolves AS-OF the retention period
from the dated row (valid_from 2025-06-07); corrections use
original-period parameters; article text implemented AS PRINTED
(post-print reform watch, §2).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-405 | odoo | l10n_sv.special_levy.rate | dated 30% row | Art. 10 hecho generador + Art. 11 rate as ONE dated row (valid_from 2025-06-07, provenance Art. 11 + Art. 25); base = full transaction amount (no printed floor/deduction); destination clause informational |
| FR-406 | odoo | l10n_sv.special_levy.in_kind.determination + account.move.line | in-kind gate | Enumerated concepts + "o cualquier otro" catch-all as printed + mandante-funds provenance qualifier; in-kind import triggers ONLY with a RAEX determination row present; no default enumeration (OQ-3) |
| FR-407 | odoo | account.move.line | retention event + moment | Collection = retención at the transfer/availability moment, any modality, on administered accounts; documentation surface = AT formularios — config-gap, NO defaults (OQ-2) |
| FR-408 | odoo | res.partner + account.move.line | agent_limb | Two limbs: `ssf_general` (SSF-supervised, ALL covered transactions) · `npo_catchall` (other interveners, ONLY exterior funds to organizaciones sin fines de lucro); NPO qualifier rides limb B, never limb A; "independientemente" clause = limb-B supervision irrelevance |
| FR-409 | odoo | l10n_sv.special_levy.entero | full-sum entero | "sin deducción alguna" (EVID-397 variant "sin dedcción" [sic OCR] normalized) to DGT offices + MH-authorized banks; due = first 10 días hábiles of following month on the shared engine (SV-FREP-FR-202..204 by id); AT formulario ref (OQ-2) |
| FR-410 | odoo | l10n_sv.special_levy.report | 15-hábiles report | Retained agents' electronic informe of retained-upon Agentes Extranjeros; first 15 días hábiles of following month (engine by id); AT specifications/formats (OQ-2) |
| FR-411 | odoo | l10n_sv.special_levy.donation.entero | monthly self-entero | Agentes Extranjeros self-enter 30% of GROSS domestic donations per monthly period; due = 10 días hábiles AFTER month close (following-lapso window, engine by id); AT formulario (OQ-2) |
| FR-412 | odoo | l10n_sv.special_levy.agent.informe | DGII informe | Retention-subject agents' own electronic informe: NIT + name of sujeto + agent data + retention bases/amounts + donation amounts + enteros; first 15 días hábiles (engine by id); to DGII (not DGT); AT-established format (OQ-2) |
| FR-413 | odoo | sanction routing rows + l10n_sv.special_levy.exclusion | CT 246/247/241 routing + exclusions | Routing consumed by pointer into the 05_-encoded CT catalog; base/reincidencia/deuda by id from TAX 16 (SV-TAX-FR-380..382); CT supletorio → 16's vocabulary by id; Art. 5 exclusions = config slots, no defaults (OQ-1 kin) |
| FR-414 | odoo | res.partner (read-only interface) | RAEX state by id | Subject resolution READS spe/01's `sv_raex_state`/`sv_raex_date` (SV-SPE-FR-201 by id — never duplicated); MIGOB freeze/prohibitions informational only; no levy computation keys on MIGOB sanction state |
| FR-415 | shared | — (awareness) | ISR independence | Considerando IV: levy "sin perjuicio" of Ley ISR Art. 3 num. 4 (54_/taxation by id); levy postings never touch ISR bases/retentions — documentation-level invariant, no operative ISR surface here |
| FR-416 | odoo | tax-line separation guard | third-track invariant | Levy engine never merges with taxation/04 (SV-TAX-FR-121..131 by id) nor taxation/13 (SV-TAX-FR-319 invariant extended to three tracks); simultaneous retentions book as separate lines/ledgers |

Version-regime notes (D12/D15): FR-405 carries the dated-row doctrine —
the 30% rate and the 2025-06-07 valid_from are config data with printed
provenance, not constants; a post-print reform of 96_ would land as a
NEW dated row (original-period parameters preserved for corrections).
The post-print reform watch (§2) rides every 96_-anchored row.

## 6. Acceptance Criteria

- **AC-001:** Given a $10,000.00 wire from a foreign mandante to a
  for-profit Agente Extranjero executed by an SSF-supervised bank
  (limb A), when the transfer posts, then the bank retains 30%
  ($3,000.00) — limb A retains on ALL covered transactions with NO NPO
  gate (FR-405, FR-408).
- **AC-002:** Given a NON-SSF money-transfer entity (limb B), when a
  $5,000.00 exterior funds transfer destined to an organización sin
  fines de lucro posts, then the entity retains 30% ($1,500.00); given
  the same entity carrying a $5,000.00 exterior transfer destined to a
  FOR-PROFIT agent, then NO retention books (the NPO qualifier gates
  limb B only) (FR-408).
- **AC-003:** Given June-2025 retentions (período tributario June),
  when the entero register resolves, then the due-window is the FIRST
  TEN DÍAS HÁBILES of July-2025 computed on the shared engine
  (asueto-aware, SV-FREP-FR-202..204 by id), the amount is the FULL
  retained sum ("sin deducción alguna" — nothing netted), and the
  venue is DGT offices/MH-authorized banks with the AT formulario
  reference required (form ships NO default — OQ-2) (FR-409).
- **AC-004:** Given $8,000.00 gross domestic donations received by an
  Agente Extranjero in July-2025, when the monthly aggregate closes,
  then the self-entero owed is $2,400.00 (30% of gross), due a más
  tardar within the TEN DÍAS HÁBILES FOLLOWING 31-jul-2025
  (engine-computed) (FR-411).
- **AC-005:** Given an Agente de Retención Especial failing to retain
  or to enter, then the breach routes to CT Art. 246 (values by
  pointer into the 05_-encoded catalog; base/reincidencia per
  SV-TAX-FR-380..381 by id); given a donation-entero breach, then CT
  Art. 247; given a reporting breach (FR-410/FR-412 surfaces), then
  CT Art. 241 (FR-413).
- **AC-006:** Given one operation carrying a levy 30% retention
  (this file) AND an ISR retention (taxation/04) AND an IVA retention
  (taxation/13), when the lines book, then all three remain SEPARATE
  tax lines under their own engines and ledgers — the levy retention
  NEVER lands in the ISR or IVA retention ledgers (FR-416).
- **AC-007:** Given a container of bienes materiales imported by an
  Agente Extranjero with NO RAEX determination row, when the import
  posts, then NO hecho generador fires (no 30%); given a RAEX
  determination row present for that import, then the 30% levy
  triggers (FR-406).
- **AC-008:** Given the LB-004 verbatim quote, then it carries "sin
  deducción alguna" exactly as the extraction txt renders it (line
  355), with EVID-397's OCR-variant reading ("sin dedcción" [sic
  OCR]) recorded in the normalization note — quote fidelity preserved
  and grep-verifiable (LB-004; FR-409).
- **AC-009:** Given a partner with `sv_raex_state = registered`
  (spe/01's field, SV-SPE-FR-201 by id), when the levy subject
  resolution runs, then it READS the spe/01 field (no local
  duplicate); given $3,000.00 of levy postings on an agent's account,
  then the ISR retention bases and renta determinations are UNCHANGED
  (FR-414, FR-415).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | RAEX reglamento not acquired (transparencia.gob.sv "versión pública" seen in search per EVID-396): the registration formats/directrices AND the Art. 5 exclusion-calificación practice (annual-renewable / per-project rows consumed by FR-413) are config-gaps — acquisition candidate (next sources registry id ≥106). No defaults ship. | no | Takumi W20 (sources registry) | open |
| OQ-2 | AT-provided forms absent: Arts. 13/14 print "los formularios que para tal efecto disponga/proporcione/establezca la Administración Tributaria" (retention documentation, entero form, report/informe formats) — this file ships NO form/format defaults; Art. 16's delegation (MH/DGII/DGT acuerdos, instructivos, circulares, resoluciones, guías) is the statutory root of the acquisition watch. | no | Takumi W20 + controller | open |
| OQ-3 | RAES in-kind determination mechanics unknown: Art. 11's "cuando así lo determine el Registro de Agentes Extranjeros" has no published procedure/format for importaciones en especie — FR-406 ships config rows only, no default enumeration; resolve when a determination instrument or practice surfaces. | no | Takumi W20 | open |
| OQ-4 | Fiscal-reporting declaration surface unknown: no F-form/declaration instrument for the levy's enteros/reports/informes exists in the corpus — the FR-409..412 registers expose the data; wiring into a declaration surface belongs to a future fiscal-reporting wave (pointer only, nothing pending here blocks implementation). | no | Takumi W20 (fiscal-reporting wave) | open |

Wiring note: FR-405..416 are the ids `special-regimes/01` OQ-6's
routing pointed to (the "future taxation pass" for the Chapter V
retention engine EVID-397 recorded at evidence depth); the W20 index
task flips spe/01's FR-201/OQ-6 pointers, `spe/00_index`,
`taxation/00_index` and COVERAGE to these ids — this file itself
touches no other file.
