# SV — E-Invoicing — Onboarding & authorization

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft (W30 synthesis wave, in review) |
| Authors | Takumi synthesis wave 30 |
| Updated | 2026-08-24 |

## 1. Purpose

This file defines the functional requirements for cluster A11
(onboarding/authorization): the emitter-side onboarding and authorization
regime of the Sistema de Transmisión — the 7-step onboarding flow from
test-environment admission to first authorized emission, the acreditamiento
test windows and the minimum-test regime per DTE type and per event
(counters, the starred-mandatory gate, test-environment reuse), the
authorization program (early-adopter solicitud and DGII Resolución, the AT
implementation program's groups and obligation dates, early adoption, the
all-types-all-establishments discipline, report-liberation dates), and the
physical-stock cut-over (inform + present for anulación/destrucción within
15 días hábiles, correlative-range reporting, and the no-coexistence
invariant).

It does **not** cover: per-type document structures
(`01_document-types.md`), the MH connector, environment separation and
transmission credentials (`02_transmission.md` — FR-054/FR-057 consumed by
id), event semantics and deadlines, the event-type registry and the
coexistence rule itself (`03_events.md` — FR-087/FR-129 consumed by id),
the certificate vault and the acreditamiento portal lifecycle
(`04_signing_delivery.md` — FR-136..138 consumed by id), catalog governance
(`../catalogs/05_governance.md` — SV-CAT-FR-006 consumed by id), or the
private client↔SaaS protocol (`06_api-protocol.md`). The días-hábiles
engine is owned by `../fiscal-reporting/08_filing-calendar.md`
(SV-FREP-FR-202..204) and consumed by id. Those files reference this one
for the onboarding/authorization regime.

## 2. Legal Basis

Authority order (binding, per master evidence index): 44_/45_/46_/50_/51_/52_
(2026) > 18_/19_ (2025) > 40_/41_/25_ (2022). No arbitration id applies
within this cluster's own slices (R12 governs the coexistence limb owned by
`03_events.md` FR-129). 18_/26_/27_/44_ are raster PDFs without a text
layer: their rows carry gloss-form content with §/pp. locators citing the
EVID row (the `04_signing_delivery.md` LB-008 precedent); only 40_/41_
(markdown sources) carry verbatim Spanish quotes.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D.L. 487-2022 (reforma al Código Tributario, régimen DTE), Art. 1 (CT Art. 119-A) | AT faculties a–i over the DTE regime: issue the cumplimiento normativa and technical specs, document structures, transmission rules, RG contents, sello rules and EVENT structures ("podrá establecer los eventos que sean necesarios" — the legal root of the 2026 new events), and set the OBLIGATION DATES (which taxpayers must emit DTEs by when) and the REPORT-LIBERATION DATES (lit. i); non-compliance with the normativa is sanctionable (gloss per EVID-083) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 1 p. 3 (EVID-083) |
| LB-002 | D.L. 487-2022, disposiciones transitorias | Obligation dates per the AT implementation program; upon becoming obligated, the emitter must INFORM the AT and PRESENT its physical document stock for destruction within 15 días hábiles; Art. 113/115 (legacy-authorization) systems may coexist with DTE emission only where the AT allows — regulated by Normativa §15 (gloss per EVID-083) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Transitorias (EVID-083) |
| LB-003 | Normativa de Cumplimiento DTE v1.2 (18_), §§15–16 | Tiquetes (Art.-115-equivalent documents) banned for DTE emitters from 01-Jan-2025 (FE mandatory for consumer operations — that limb owned by `03_events.md` FR-129 by id; 45_ v2.0 §15 restates the ban per EVID-084); implementation program: the AT sets taxpayer GROUPS and DATES; the emitter must implement ALL document types it is authorized for across ALL its establishments; taxpayers MAY adopt early (before their group date); report-liberation dates set per Art. 119-A lit. i (gloss per EVID-077) | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §§15–19 pp. 22–24 (EVID-077) |
| LB-004 | Normativa v1.2 (18_), §12 | Physical documents replaced by DTEs must be presented to the AT for anulación/destrucción and their CORRELATIVE RANGES reported; NO physical/DTE coexistence while emitting DTEs (exception: Sistema de Facturación users); "documentos impresos" includes PDF-emission systems lacking the official data structure (gloss per EVID-074). Cross-note: the conservation limb of §12 is owned by `04_signing_delivery.md` LB-010 — distinct slices of the same section | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §12–12.1 p. 18 (EVID-074) |
| LB-005 | Manual de Estructuras y Catálogos (40_), §I: "Paso 1: Complete los requisitos mínimos para ingresar a la plataforma (tener un sistema de facturación que genere los archivos Json de conformidad a los requisitos establecidos por el Ministerio de Hacienda)." · "Paso 2: Envío de solicitud de ingreso al ambiente para pruebas." · "Paso 3: Obtener el Certificado de Firma Electrónica y la contraseña de acceso a la API." · "Paso 4: Ejecutar las pruebas mínimas requeridas. (en esta plataforma se otorgan 2 meses para realizar las pruebas desde el ingreso a la consola de administración de facturación electrónica)" · "Paso 5: Presentar la solicitud de Autorización para ser emisor de DTE. Una vez superadas las pruebas deberá presentar solicitud para ser autorizado como emisor de DTE (solo para contribuyentes que opten por iniciar a emitir DTE previo a la fecha designada por el Ministerio de Hacienda)." · "Paso 6: DGII emitirá la Resolución de autorización. (solo para contribuyentes que opten por iniciar a emitir DTE previo a la fecha designada por el Ministerio de Hacienda)." · "Paso 7: Inicia operaciones emitiendo los tipos de DTE que se hayan autorizado." | The 7-step emitter onboarding: (1) minimum requirements — an invoicing system generating MH-conformant JSON; (2) request admission to the test environment; (3) obtain the electronic-signature certificate and the API access password; (4) execute the required minimum tests — 2 months granted from entry to the electronic-invoicing administration console; (5) present the DTE-emitter authorization request; (6) DGII issues the authorization Resolución — steps 5–6 qualified as printed: ONLY for taxpayers opting to emit DTEs BEFORE the MH-designated date (the early/voluntary limb); (7) begin operations emitting the authorized DTE types | `sv/sources/40_manual_estructuras_catalogo.md` | §I md 120–128 (EVID-001) |
| LB-006 | Manual de Consola Administrativa (26_), Sitio Emisores DTE | Console sections: Inicio (onboarding state), Detalle de Emisor (authorized doc types), Certificado, Sistema de Facturación, Solicitar Autorización (test→production), Consultas, Gestión de Usuario API (credential creation/password); minimum-tests table per doc type, starred types = mandatory before requesting additional types (gloss per EVID-081 — raster PDF; the per-type counts/starred set themselves → OQ-001) | `sv/sources/26_Manual_Consola_Administrativa.pdf` | TOC + pp. 6–9 (EVID-081) |
| LB-007 | Manual de Eventos de Invalidación y Contingencia v1.1 (41_), §1 + Anexo 1: "deberá realizar el proceso de pruebas para cada uno de los eventos por medio del Sistema de Transmisión de DTE con respuesta exitosa, es decir que se les otorgó el sello de recepción." · "Las pruebas de dichos eventos serán consideradas al momento de realizar las verificaciones para el otorgamiento de la resolución que autorizará a los contribuyentes como emisores de documentos tributarios electrónicos; cabe aclarar que las pruebas para estos eventos deberán realizarse independientemente se solicite ingresar con uno o más DTE." · Anexo 1 "Pruebas de transmisión satisfactorias mínimas para eventos de invalidación y contingencia en el Sistema Integrado DTE": "Evento de Invalidación" → 5, "Evento de Contingencia" → 5 | Each event type must pass its own transmission tests during onboarding (successful = sello de recepción granted), independent of how many DTE types are requested; the event tests are considered in the verifications for granting the authorization resolución; Anexo 1 prints the minimum successful-transmission counts: 5 invalidation events + 5 contingency events | `sv/sources/41_manual_eventos_invalidacion.md` | §1 md 69–75 + Anexo 1 md 394–399 (EVID-036/045) |
| LB-008 | Manual de Obtención de Certificado (27_) | Acreditamiento required ONCE PER ENVIRONMENT (test AND production — credentials personalized per environment); test credentials valid 2 months (Sistema de Transmisión) / 15 days (Sistema de Facturación) to complete the minimum tests; portal https://info.dtes.mh.gob.sv/ (NIT + DGII services password) → Sitio Emisores DTE (gloss per EVID-080 — raster PDF). Cross-note: same-instrument kin of `04_signing_delivery.md` LB-008; the certificate-side lifecycle is owned there by FR-136..138 by id — this row anchors the window semantics for the test regime | `sv/sources/27_Manual_Obtencion_Certificado.pdf` | pp. 5–10 (EVID-080) |

## 3. Functional Requirements

### 3.1 Onboarding workflow & per-type test regime

- **SV-EINV-FR-165:** The system shall track the emitter's DTE onboarding as a per-environment state machine/checklist mirroring the 7-step flow (LB-005): (1) minimum requirements — invoicing system generating MH-conformant JSON; (2) test-environment admission request; (3) obtain the signing certificate and API access password; (4) execute the required minimum tests; (5) present the DTE-emitter authorization request; (6) DGII issues the authorization Resolución; (7) begin operations emitting the authorized DTE types. Steps 5–6 carry the printed early-adopter qualification — "(solo para contribuyentes que opten por iniciar a emitir DTE previo a la fecha designada por el Ministerio de Hacienda)" — so the resolución flow is the pre-designation-date/voluntary limb; after the designation date the entry route is the AT obligation program (FR-172). The certificate/credential steps (3) consume `04_signing_delivery.md` FR-136..138 and `02_transmission.md` FR-054/057 by id — nothing of the vault, portal or credential-storage contract is restated here. (LB-005; cross-ref 04 FR-136..138, 02 FR-054/057)
- **SV-EINV-FR-166:** The system shall track minimum-test completion per DTE type: a passed-tests counter per (environment, DTE type) evaluated against its required-count row, bound to the test window in which the tests must complete — test credentials valid 2 months (Sistema de Transmisión) or 15 days (Sistema de Facturación) per environment (LB-008; the deadline-tracking surface itself is `04_signing_delivery.md` FR-138 by id). The per-type required counts (26_ consola table — not corpus-extracted) are CONFIG ROWS with no product defaults → OQ-001. (LB-006; LB-008; OQ-001)
- **SV-EINV-FR-167:** The system shall enforce the starred-mandatory gate of the consola minimum-tests table: a request for ADDITIONAL document types is offerable only after the starred doc types' minimum-test counts have passed; which types are starred is part of the OQ-001 config rows (no defaults). (LB-006; OQ-001)

### 3.2 Event-test regime

- **SV-EINV-FR-168:** The system shall track per-event minimum tests with the counts printed in 41_ Anexo 1: Evento de Invalidación → 5 and Evento de Contingencia → 5 successful transmission tests each (LB-007 verbatim table). The 2026 event types Retorno and Operaciones Especiales have no evidenced test minimums (41_ v1.1 predates them) — their required-count rows are config-gated on OQ-002, no defaults minted. (LB-007; OQ-002; event-type identities per `03_events.md` FR-087 by id)
- **SV-EINV-FR-169:** Event tests count toward the authorization: per LB-007, "Las pruebas de dichos eventos serán consideradas al momento de realizar las verificaciones para el otorgamiento de la resolución" — and the per-event tests "deberán realizarse independientemente se solicite ingresar con uno o más DTE": the event-test counters are requirements of their own, independent of how many DTE types are requested, and the readiness surface shall never mark the checklist complete with an incomplete event-test row. (LB-007)
- **SV-EINV-FR-170:** The test environment shall remain reusable after authorization for AT-mandated updates: "Podrán utilizar ambiente destino "00", cuando se implementen actualizaciones indicadas por la Administración Tributaria, con el propósito de garantizar el correcto funcionamiento de dichos cambios." (41_ §2.5 ambiente field). The product shall re-open the test checklist/counter surface when an AT-mandated change lands, aligned with the catalog adaptation deadlines owned by SV-CAT-FR-006 by id (Cuadro 4 SLA — deadline values live there). (LB-007; cross-ref `../catalogs/05_governance.md` SV-CAT-FR-006)

### 3.3 Authorization program & the AT implementation mandate

- **SV-EINV-FR-171:** The system shall record early-adopter/voluntary authorization as dated rows with instrument provenance: the solicitud (Paso 5) date and the DGII Resolución de autorización (Paso 6) reference + date, per environment, driving the test→production transition (the consola "Solicitar Autorización" step — LB-006). After the designation date the entry route is the AT obligation program (FR-172); the resolución flow remains the early/voluntary limb exactly as 40_ §I prints it. (LB-005; LB-006)
- **SV-EINV-FR-172:** The system shall model the AT implementation program as append-only dated mandate rows (D15/D16 discipline: valid_from, provenance, a change adds a row, never edits): group identifier + obligation date + instrument provenance, supporting the who-must-emit-by-when evaluation for the company. NO cohort instrument is in the corpus (the program acts under the 119-A faculties, LB-001) → the rows are config-gated, populated only when the AT publishes, watch → OQ-003. (LB-001; LB-002; LB-003; D15/D16; OQ-003)
- **SV-EINV-FR-173:** The system shall support the early-adoption path: a taxpayer not yet obligated (no mandate row, or its group's date not reached) may adopt DTE emission voluntarily before its designation date — routed through the FR-165 checklist and the FR-171 resolución flow (Normativa §15: emitters may adopt early). (LB-003)
- **SV-EINV-FR-174:** Implementation-program discipline: upon authorization or obligation, the emitter implements ALL DTE types it is authorized for across ALL its establishments (LB-003) — the onboarding surface shall expose per-(document type × establishment) readiness, not just company-level, with the numeroControl establishment/point-of-sale space consumed from `01_document-types.md` FR-004 by id and warehouses↔establecimientos per canon D14. (LB-003; cross-ref 01 FR-004; D14)
- **SV-EINV-FR-175:** The report-liberation dates (Art. 119-A lit. i — the AT faculty setting when report/book obligations are liberated for DTE emitters) shall be modeled as dated config rows with instrument provenance on the mandate registry; no corpus instrument exists → provenance-gated, rides OQ-003 (no defaults). (LB-001; LB-003; OQ-003)

### 3.4 Physical-stock cut-over

- **SV-EINV-FR-176:** Upon the obligation date, the emitter's physical-stock cut-over shall be tracked: INFORM the AT and PRESENT the physical documents replaced by DTEs for anulación/destrucción within 15 días hábiles of becoming obligated — the días-hábiles arithmetic is consumed from SV-FREP-FR-202..204 by id (never computed locally); the destruction record carries dated inform/present events and its state. (LB-002; LB-004; cross-ref `../fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202..204)
- **SV-EINV-FR-177:** The correlative ranges of the voided/destroyed physical stock shall be recorded and reported (LB-004): per destruction, one range record per document type (from–to correlative), snapshotted as reported (D15 snapshot-on-write — a correction adds a row, never edits); the range record is the emitter's evidentiary copy of the report. (LB-004; D15)
- **SV-EINV-FR-178:** The no-coexistence invariant: a DTE emitter under the Sistema de Transmisión shall have no physical emission path for the replaced document types — no physical/DTE coexistence, with "documentos impresos" understood to include PDF-emission systems lacking the official data structure (LB-004). The exception limb is consumed from `03_events.md` FR-129 by id (the FVS/Art.-113-OpEsp coexistence exception and the tiquete ban live there); the Sistema de Facturación exception is recorded as a 119-H awareness note — users of the AT's free solution sit outside the transmission-system onboarding this file governs. The cut-over sequencing (last-legacy documents, sequence-init records) rides canon D19. (LB-004; LB-002; cross-ref 03 FR-129; D19)

### 3.5 Onboarding/authorization status surface

- **SV-EINV-FR-179:** The company-level onboarding/authorization status surface shall aggregate: authorized doc types (mirroring the consola Detalle de Emisor — LB-006), checklist state (FR-165), per-type and per-event test counters (FR-166/FR-168), mandate state + obligation date (FR-172) and stock-destruction state (FR-176) — each element carrying its dated-row provenance (D15). (LB-006; D15)

## 4. Data Model

All registries below are dated-row registries (D15/D16): provenance is
mandatory on every row, and cited rows are immutable — a change adds a row.
Config-gated rows (mandate groups, per-type test counts) ship EMPTY, with
no product defaults.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.onboarding.state | company | m2o res.company | — | FR-165 |
| l10n_sv_edi.onboarding.state | environment | selection | 00 pruebas / 01 producción (CAT-001) | FR-165 |
| l10n_sv_edi.onboarding.state | step | selection | paso_1..paso_7 (40_ §I) | FR-165 |
| l10n_sv_edi.onboarding.state | state | selection | pending / done / not_applicable (steps 5–6 post-designation: program route) | FR-165, FR-171 |
| l10n_sv_edi.onboarding.state | completed_on | date | — | FR-165 |
| l10n_sv_edi.onboarding.test | company | m2o res.company | — | FR-166 |
| l10n_sv_edi.onboarding.test | scope | selection | doc_type / event_type | FR-166, FR-168 |
| l10n_sv_edi.onboarding.test | environment | selection | 00 / 01 | FR-166 |
| l10n_sv_edi.onboarding.test | doc_type | selection | CAT-002 (when scope = doc_type) | FR-166 |
| l10n_sv_edi.onboarding.test | event_type | selection | invalidación / contingencia / retorno / opEsp (03 FR-087) | FR-168 |
| l10n_sv_edi.onboarding.test | required_count | integer | CONFIG: 26_ table → OQ-001 (doc types); 41_ Anexo 1 prints 5 + 5; Retorno/OpEsp → OQ-002 | FR-166, FR-168 |
| l10n_sv_edi.onboarding.test | passed_count | integer | sealed successful transmissions | FR-166, FR-168 |
| l10n_sv_edi.onboarding.test | starred_mandatory | boolean | config (OQ-001 starred set) | FR-167 |
| l10n_sv_edi.onboarding.test | window_deadline | date | 2 months (Sistema de Transmisión) / 15 days (Sistema de Facturación); deadline surface owned by 04 FR-138 | FR-166 |
| l10n_sv_edi.mandate.group | row_kind | selection | obligation_group / report_liberation | FR-172, FR-175 |
| l10n_sv_edi.mandate.group | group | char | AT program group id (obligation rows) | FR-172 |
| l10n_sv_edi.mandate.group | obligation_date | date | — | FR-172 |
| l10n_sv_edi.mandate.group | instrument | char | provenance — CONFIG-GATED, no corpus instrument (OQ-003) | FR-172, FR-175 |
| l10n_sv_edi.mandate.group | valid_from / valid_to | date | dated-row discipline | FR-172; D15/D16 |
| l10n_sv_edi.authorization.resolution | company | m2o res.company | — | FR-171 |
| l10n_sv_edi.authorization.resolution | environment | selection | 00 / 01 | FR-171 |
| l10n_sv_edi.authorization.resolution | requested_on | date | Paso 5 solicitud | FR-171 |
| l10n_sv_edi.authorization.resolution | resolution_ref | char | DGII Resolución reference | FR-171 |
| l10n_sv_edi.authorization.resolution | resolution_date | date | Paso 6 | FR-171 |
| l10n_sv_edi.authorization.resolution | instrument | char | provenance | FR-171 |
| l10n_sv_edi.stock.destruction | company | m2o res.company | — | FR-176 |
| l10n_sv_edi.stock.destruction | mandate_row | m2o l10n_sv_edi.mandate.group | the obligation row that started the clock | FR-176 |
| l10n_sv_edi.stock.destruction | informed_on | date | inform AT | FR-176 |
| l10n_sv_edi.stock.destruction | presented_on | date | present for anulación/destrucción | FR-176 |
| l10n_sv_edi.stock.destruction | due_on | date | obligation_date + 15 días hábiles (SV-FREP-FR-202..204 by id) | FR-176 |
| l10n_sv_edi.stock.destruction | state | selection | pending / informed / presented / closed | FR-176 |
| l10n_sv_edi.stock.destruction.range | destruction_id | m2o l10n_sv_edi.stock.destruction | — | FR-177 |
| l10n_sv_edi.stock.destruction.range | doc_type | selection | CAT-002 | FR-177 |
| l10n_sv_edi.stock.destruction.range | correlative_from / correlative_to | char | the reported range (snapshot-on-write) | FR-177; D15 |
| res.company | l10n_sv_edi_onboarding_state · l10n_sv_edi_mandate_state · l10n_sv_edi_obligation_date · l10n_sv_edi_stock_state | selection / date | derived aggregates (FR-179); authorized doc types derived from the resolution rows | FR-179 |

## 5. Odoo Mapping

Layer semantics (this cluster): `odoo` = the checklist/status/config
surfaces the emitter's Odoo instance keeps; `saas` = gates that consume the
dated rows (readiness evaluation, the emission-path invariant); `shared` =
the dated-row registries both sides honor (mandate, authorization,
destruction provenance). Model names are stable across Odoo 17/18/19/20;
no version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-165 | odoo | l10n_sv_edi.onboarding.state | step, state | Checklist mirrors the manual/portal steps; cert/credential steps consume 04 FR-136..138 + 02 FR-054/057 by id |
| FR-166 | odoo | l10n_sv_edi.onboarding.test | counters, window_deadline | required_count config-gated (OQ-001); passed counters fed from sealed-transmission confirmations pushed over the private protocol |
| FR-167 | odoo | l10n_sv_edi.onboarding.test | starred_mandatory gate | Starred set = config (OQ-001); gate blocks the additional-types request action |
| FR-168 | shared | l10n_sv_edi.onboarding.test | event rows | 5 + 5 seeded from 41_ Anexo 1; Retorno/OpEsp rows await OQ-002 |
| FR-169 | saas | — | readiness evaluation | Readiness/evidence pack for the resolución request computed SaaS-side from the counters; surfaced to odoo |
| FR-170 | shared | l10n_sv_edi.onboarding.state | test-reopen | Re-open test surface on AT-mandated updates; rides SV-CAT-FR-006 deadlines by id |
| FR-171 | odoo | l10n_sv_edi.authorization.resolution | dated rows | Portal steps recorded manually; provenance mandatory |
| FR-172 | shared | l10n_sv_edi.mandate.group | dated rows | Append-only, config-gated (OQ-003); D15/D16 discipline |
| FR-173 | odoo | l10n_sv_edi.onboarding.state | route flag | Voluntary path reuses the FR-165 checklist + FR-171 rows |
| FR-174 | odoo | onboarding.state × stock.warehouse config | per (type × establishment) readiness | D14 warehouses↔establecimientos; numeroControl space per 01 FR-004 by id |
| FR-175 | shared | l10n_sv_edi.mandate.group | report_liberation rows | Provenance-gated (OQ-003); no defaults |
| FR-176 | odoo | l10n_sv_edi.stock.destruction | due_on | 15 días hábiles via SV-FREP-FR-202..204 by id; never computed locally |
| FR-177 | odoo | l10n_sv_edi.stock.destruction.range | ranges | Snapshot-on-write (D15); correction = new row |
| FR-178 | saas | — | emission-path invariant | Physical print paths for replaced types not offerable; FVS/OpEsp exception per 03 FR-129 by id; 119-H awareness note |
| FR-179 | odoo | res.company | status aggregates | Derived from the registries; dated-row provenance on each element |

## 6. Acceptance Criteria

- **AC-001:** Given an emitter in the test environment with 5 sealed invalidation-event tests and 5 sealed contingency-event tests, then the readiness surface marks the event-test requirement complete and includes the counters in the authorization-request evidence pack; given either counter below its required row (5/5), then the requirement shows incomplete and the checklist cannot complete. (FR-168, FR-169)
- **AC-002:** Given the starred doc-type set configured (OQ-001 rows) with an unmet minimum, then the request-additional-document-types action is blocked with the starred-gap explanation; given the starred minimums passed, then the action is offerable. (FR-167)
- **AC-003:** Given a mandate row whose obligation date reaches the company, then the company flips to obligated and the stock-destruction clock is computed as obligation date + 15 días hábiles via the shared días-hábiles engine (SV-FREP-FR-202..204 by id), never by local arithmetic. (FR-172, FR-176)
- **AC-004:** Given a stock destruction recorded with ranges (e.g. FE A-00000101..A-00500101), then the range records are snapshotted as reported with dated provenance and never mutate — a correction adds a new row. (FR-177)
- **AC-005:** Given a company with no mandate row (or a future group date) that completes the 7-step checklist, then the voluntary/early-adoption path records the solicitud and DGII resolución as dated provenance rows and production-environment emission is enabled for the authorized types. (FR-165, FR-171, FR-173)
- **AC-006:** Given a DTE emitter under the Sistema de Transmisión (a non-exception system), then physical print paths for the replaced document types are not offerable (no-coexistence); the block explanation cites the FVS/OpEsp exception owned by `03_events.md` FR-129 and the Sistema de Facturación (119-H) awareness note. (FR-178)

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Per-type minimum-test counts and the starred-mandatory set (26_ consola table) are not corpus-extracted — 26_ is a raster PDF and the table was not read; 40_ Anexo 1 (md 1859–1876, EVID-015 placeholder, superseded per master-index A11 History) may itself hold the per-type table. required_count/starred rows are config-gated with NO product defaults; obtain from 26_ + 40_ Anexo 1 raw text before the onboarding test surfaces ship. | no | Takumi (raw-text pass) | open |
| OQ-002 | Retorno / Operaciones Especiales test minimums: 41_ v1.1 (05/2022) prints 5 + 5 for invalidación/contingencia only; the 2026 event types postdate it and no v2.0 limb has been evidenced (MOQ-05 kin — endpoint/structure gaps of the same 2026-event vintage). No defaults minted; re-probe 45_/46_ and new manual editions. | no | Takumi (watch) | open |
| OQ-003 | AT implementation-program instruments (obligation groups/dates) and report-liberation acts (119-A lit. i) are not in the corpus: mandate rows are config-gated dated rows awaiting provenance. Watch kin MOQ-05 class; re-probe rides the D.O. / factura.gob.sv cadence. | no | Takumi (watch) | open |
| OQ-004 | 26_/27_ manuals are 2022-vintage portal flows (Sitio Emisores DTE section names, test→production steps): currency watch shared with `04_signing_delivery.md` OQ-006 kin; portal-flow drift re-probe at the regulatory-change cadence. | no | Takumi (watch) | open |
