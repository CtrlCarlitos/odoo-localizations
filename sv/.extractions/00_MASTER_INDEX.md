# MASTER EVIDENCE INDEX — El Salvador localization (S1 + S2 + S3 + S4 + S5-prep synthesis lookup)

Built: 2026-08-17. S1 inputs (read-only, no source PDFs re-read): the eight evidence/digest files + `shared/docs/saas-thin-client-architecture.md`. **S2/ISR extension 2026-08-17:** W6+W7 evidence files (EV03/EV04/EV10/EV53/EV54/EV56) merged into clusters T1–T8 below; rulings R17–R22; SOQ-01..07. **S3/fiscal-reporting extension 2026-08-18:** W8 evidence (EVID-172..190, files EV29/EV30/EV34/EV35/EV61-64) merged into clusters F1–F12 below; SOQ-08..14. **S4/payroll extension 2026-08-18:** W9 evidence (EVID-191..210, files EV16/EV08/EV09/EV11/EV65) merged into clusters P1–P10 below; rulings R23–R24; SOQ-15..21.
**Authority order (binding):** 44_/45_/46_/50_/51_/52_ (2026) > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). Where the supersession map in EV44 marks a W-item SUPERSEDED, the current-authority finding governs; old EVID ids are kept as history.
**ISR authority order (binding, S2):** 54_ (consolidated Ley ISR, article text current incl. stamps through Jan-2026) with reform decrees 55_ (Art. 37), 56_ (Art. 3.4 + derogations), 57_/58_ (interpretaciones auténticas) for changed articles > 03_ (historical copy, consolidated through D.L. 233-2012). Retention tables: 53_ (D.E. 10-2025, operative; **published D.O. N° 79 T.447 30-abr-2025 = gazette print 60_, effective 2025-05-08 — SOQ-03 RESOLVED 2026-08-18**) > 10_ (D.E. 75/25-1992, historical). Reglamento: 04_ = D.E. 101-1992 as reformed by D.E. 8-1993/39-1993/**117-2001** (self-documented repeal map; see R17).
**Payroll authority order (binding, S4):** pensions = 09_ (**D.L. 614, Ley Integral del Sistema de Pensiones, effective 2022-12-29 — derogates D.L. 927-1996/SAP per Art. 162; registry title is a misnomer, see R24**) over any SAP-era lore; ISSS = 08_ (D.L. 1263 law-level rates; caps in the Reglamento — absent, SOQ-15) with 09_ Art. 154 governing pensioner-health (R23); labor = 11_ (CT, Índice Legislativo edition); SMM = 16_ (Decreto 11-2025, effective 2025-06-01) over the 2021 pair. Retention/ISR interfaces owned by 53_/54_ (S2 files); F-14 column model by 35_/38_/59_ (S3 files).

**File keys (citation prefixes):**
| Key | File |
|---|---|
| EV40 | `sv/.extractions/40_manual_estructuras_catalogo.evidence.md` |
| EV41 | `sv/.extractions/41_manual_eventos_invalidacion.evidence.md` |
| EV25 | `sv/.extractions/25_Catalogos_Transmision_v1.2.xlsx.evidence.md` |
| EV01 | `sv/.extractions/01_Ley_IVA.evidence.md` |
| EV05 | `sv/.extractions/05_Codigo_Tributario.evidence.md` |
| EV18 | `sv/.extractions/18_Normativa_DTE_W5.evidence.md` |
| EV44 | `sv/.extractions/44-52_RegulatoryUpdate2026.evidence.md` |
| DG45 | `sv/.extractions/45_Anexos.digest.md` (authoritative v2.0 structure digest) |
| ARCH | `shared/docs/saas-thin-client-architecture.md` |
| EV03 | `sv/.extractions/03_Ley_ISR.evidence.md` (EVID-088..108) |
| EV04 | `sv/.extractions/04_Reglamento_ISR.evidence.md` (EVID-128..146) |
| EV10 | `sv/.extractions/10_Tablas_Retencion_ISR.evidence.md` (EVID-148..152) |
| EV53 | `sv/.extractions/53_Tablas_Retencion_ISR_DE10_2025.evidence.md` (EVID-153..161) |
| EV54 | `sv/.extractions/54_Ley_ISR_consolidada_DO79_T447.evidence.md` (EVID-162..167; covers 55_ delta) |
| EV56 | `sv/.extractions/56-58_ISR_DL969_DL192_DL345.evidence.md` (EVID-168..170) |
| EV16 | `sv/.extractions/16_Salarios_Minimos_2025.evidence.md` (EVID-191..192) |
| EV08 | `sv/.extractions/08_Ley_ISSS.evidence.md` (EVID-193..196) |
| EV09 | `sv/.extractions/09_Ley_Sistema_Pensiones.evidence.md` (EVID-197..200) |
| EV11 | `sv/.extractions/11_Codigo_Trabajo.evidence.md` (EVID-201..209) |
| EV65 | `sv/.extractions/65_F11_v18_form_visual.evidence.md` (EVID-210) |

DG45 sections cited as: §1 (Anexo II structures/versions), §2 (Anexo III events), §3.1 (Anexo IV DTE validations), §3.2 (Anexo V event validations), §3.3 (contingency-type resolution), §4 (Anexo I technical specs), §5 (OCR warnings).

---

## Section A — Topic clusters (synthesis worklist)

### A1 — Document types & per-type structures
**Covers:** the 11 DTE types — authoritative v2.0 JSON versions, section layout, per-type field deltas (new/removed), and per-field validation rules.
- **Governing EVIDs:** EVID-083 (EV44; CT 119-G per-type content requirements, D.L. 487) · EVID-087 (EV44; 52_ schema version matrix) · EVID-070 (EV18; numeroControl, generation, rounding/holgura-from-item-decimals) · EVID-078 (EV18; 18_ v1.2 Anexo II deltas — mid authority, yields to DG45) · EVID-060 (EV05; CT 107-115 document-type legal semantics) · **DG45 §1.0-1.5, §3.1** (authoritative versions: FE 2, CRE 2, CLE 2, DCLE 2, FSEE 2, CDE 2, FEXE 3, CCFE 4, NRE 4, NCE 4, NDE 4; fields 1-175; new keys fusiones/distrito/domicilioFiscal/tributoSujetoIVA[?]; removals incl. receptor.nit for NCE/NDE/CLE, Extensión DCLE-only).
- **LB:** D.L. 487-2022 Art. 119-G (44_) · Código Tributario Arts. 107-115 (05_) · Normativa v2.0 Anexo II + Anexo IV (45_, via DG45) · JSON Schemas 2026-08-11 (52_, EVID-087) · Ley IVA Art. 62 (adjustment docs, EV01:EVID-054).
- **History (superseded detail, still the worked-example base):** EVID-005-012 (EV40; Anexo 3-12 fill rules: numeroControl 31ch, cargos/abonos, CAT-015 mechanics, related docs, otros docs, discounts, payments, donación, rounding) · EVID-013 (EV40; Anexo 12 rounding/holgura) · EVID-016-035 (EV40; per-type v1/v3 structures FE→CDE). Use only where DG45/52_ are silent; verify against schemas (MOQ-08).

### A2 — Transmission & connector
**Covers:** API endpoints, auth/token lifecycle, retry policy, lote batching, transmission states/observaciones, holgura windows, ordering rule.
- **Governing EVIDs:** EVID-079 (EV18; 22_ endpoints: `/seguridad/auth`, `/fesv/recepciondte`, `/fesv/recepcionlote` ≤100 docs, `consultadtelote`, `consultadte`, `/fesv/contingencia`, `/fesv/anulardte`; obs/codigoMsg 002; batch windows; QR URL — API surface verified identical in 46_ per EVID-085) · EVID-085 (EV44; 46_ v2.0: token configurable, guidance once-per-24h; password 13-25) · EVID-084 (EV44; §9.2 ordering: affected-before-affecting, uno-a-uno and lote) · EVID-072 (EV18; states + 24h same-code rejection fix — verify vs 45_ §10, MOQ-07) · **DG45 §4** (Anexo I: ambientes 00/01, uno-a-uno/lote, NEW service-status consultation rule 3.5; §3.1 N°10 fecEmi ≤5 days after transmission, horEmi 30-min month-end holgura).
- **LB:** CT 119-D/119-F (D.L. 487, EV44:EVID-083) · Normativa v2.0 §9 + Anexo I (45_) · Manual Tecnológico v2.0 (46_, EV44:EVID-085).
- **History:** EVID-041/042 (EV41; 5s trigger, 5000-doc batches — superseded by 8s/2-retry and 1000-cap) · EVID-071 (EV18; Cuadro 1 — superseded on contingency list).

### A3 — Events — invalidación
**Covers:** invalidation taxonomy (business-effect semantics), differentiated deadlines per DTE type, event v3 structure, preconditions and replacement-doc sequencing.
- **Governing EVIDs:** EVID-083 (EV44; CT 119-E: error/rescission/adjustment paths; post-window CCF/CR adjustments via NC/ND under Ley IVA 62-63; receiver-ID data for FE/FEXE/FSEE) · EVID-075 (EV18; Cuadro 2 taxonomy) · EVID-087 (EV44; invalidacion schema v3) · **DG45 §2.1 (Secciones 1/3/6/11), §2.2 (≈33 fields + sello), §3.2 N°9 + N°43-48** — deadlines: CCFE/CRE/NCE/NDE **1 day** after seal; CLE/DCLE **10 días hábiles** of month following period; NRE/CDE/Evento retorno/Evento OpEsp **4 calendar days**; FE/FEXE/FSEE **3 months**; blocks: CCFE/CRE with active NCE/NDE → invalidate NC/ND first; FE/FEXE/FSEE with applied retorno event → invalidate event first; codigoGeneracionR only tipoInvalidación 1/3.
- **LB:** CT 119-E (D.L. 487, 44_) · Normativa v2.0 §13 + Anexo III/V (45_) · CAT-024 v1.1 "Motivo del evento" 1/2/3 (EV44:EVID-086).
- **History:** EVID-014 (EV40; Anexo 9 replacement matrix) · EVID-037-040 (EV41; v1.1 event semantics, 1d/3mo table, v2 36-field structure).

### A4 — Events — contingencia
**Covers:** contingency model (deferred), allowed DTE types, clocks (event ≤24h; docs ≤72h), event v4 structure, batch restrictions.
- **Governing EVIDs:** EVID-084 (EV44; Cuadro 5 clocks: contingency-diferida ≤24h event / ≤72h docs after event seal) · EVID-076 (EV18; retry-exhaustion precondition; sanctions 239-A g)/h); Sistema de Facturación users may use pre-authorized physical docs) · EVID-087 (EV44; contingencia schema v4) · **DG45 §3.3 + §2.1 Secciones 4-5, §3.2 N°10, N°34-36** — allowed types: **01-FE, 03-CCFE, 04-NRE, 05-NCE, 06-NDE, 07-CRE, 11-FEXE, 14-FSEE + 18-Evento retorno**; excluded CLE/DCLE/CDE; detail cap **1000 items/event** (>1000 ⇒ new event); event transmission ≤24h after contingency end.
- **LB:** CT 119-F (D.L. 487, 44_) · Normativa v2.0 §9/§13 (45_).
- **History:** EVID-041-044 (EV41; v1.1 model/structure, 500[?]/5000 caps) · EVID-071 (EV18; Cuadro 1 6-type list).

### A5 — Events — Retorno + Operaciones Especiales (new 2026)
**Covers:** the two new 2026 events — goods return/service refund (fe-eret v1) and special operations reporting incl. FVS (fe-eop v1).
- **Governing EVIDs:** EVID-084 (EV44; retorno cases incl. envase deposit, reimportación, export diminution; 3-month deadline from related doc's seal; normal-previa OR normal-diferida ≤1 day; effects per FE/FEXE/FSEE; no-discount/no-exceed/not-invalidate-origin rules; EOP = FVS monthly reporting 10 primeros días hábiles + CT-113 internal-control docs; coexistence rule) · EVID-086 (EV44; CAT-023 = Operaciones Especiales codes 02 FVS / 97 Comprobantes de Control Interno) · EVID-087 (EV44; fe-eret v1, fe-eop v1) · **DG45 §2.1** (retorno Secciones 2/6-10/12; related docs only 01/11/14 max 50; tipoEvento CAT-002 18/17; **§3.2 N°9**: 3-month transmission window; **2 years** for emitter activity codes {21001, 21008, 46482, 46484, 46491, 47721}; §3.2 N°61-88 body rules incl. value caps (ivaRetenido (VG/1.13)×1%, reteRenta 10%); OpEsp only AT-designated taxpayers).
- **LB:** Normativa v2.0 §4 + Cuadro 5 + §13.3-13.4 (45_) · CT 119-A event power (D.L. 487) · CAT-002 v1.1 codes 17/18.
- **History:** none (events did not exist pre-2026).

### A6 — Signing & certificates
**Covers:** JWS signing standard, certificate model (MH-issued simple certs), firmador, acreditamiento per environment, client-side vault decision.
- **Governing EVIDs:** EVID-083 (EV44; CT 119-B generation→signature→transmission→delivery chain) · EVID-079 (EV18; firmador `http://localhost:8113/firmardocumento/`, JWS RS512) · EVID-080 (EV18; 27_ acreditamiento per env, 2-month/15-day test windows, info.dtes.mh.gob.sv) · EVID-085 (EV44; 46_ v2.0 password policy) · **DG45 §4** (Cuadro 10: JWS over full DTE/event JSON, PKCS8 keys, RSASSA[? OCR]; cert validated on every document/event).
- **LB:** CT 119-B (D.L. 487, 44_) · Normativa v2.0 Anexo I Cuadro 10 (45_) · 27_ Certificado manual (EVID-080).
- **History:** EVID-003 (EV40; 2022 cert model, per-emitter infra, optional MH signing service).
- **Crossref:** A12/D2 — client-side signer + encrypted vault (ARCH).

### A7 — RG/QR + delivery
**Covers:** entrega = Archivo DTE + Representación Gráfica, QR content, versión legible A/B/C/D, download-site requirements, RG conservation.
- **Governing EVIDs:** EVID-073 (EV18; 18_ §11: RG no probative value, QR mandatory, URL `https://admin.factura.gob.sv/consultaPublica?ambiente=&codGen=&fechaEmi=`, receiver obliged to demand sealed DTE) · EVID-083 (EV44; CT 147 reform: RGs conserved in original format/medium; fedatarios verify RG delivery) · **DG45 §4** (QR only as entrega requirement — links to download site; NO payload/endpoint spec in Anexos; NEW Módulo de Entrega).
- **LB:** CT 119-C/119-D + Art. 3 (CT 147 reform) + Arts. 5-8 (D.L. 487, 44_) · Normativa §11 + Anexo I (45_).
- **History:** EVID-020 (EV40; A/B/C/D categories + sello-not-in-outbound-JSON — concept carried into v2.0 Anexo column structure per DG45 §4).

### A8 — State machine & correction
**Covers:** document states, rejected-doc 24h same-code correction, generation-date bookkeeping, ordering rule, evidential hierarchy.
- **Governing EVIDs:** EVID-072 (EV18; states Transmitido [Ajustado/Observado] / Rechazado / Invalidado; 24h same-codigoGeneración retry then new; generation-date books; deductions need seal) · EVID-084 (EV44; §9.2 a DTE may only be affected if already transmitted) · EVID-083 (EV44; CT 199 untransmitted = presumed income; CT 206 hierarchy AT copy > taxpayer copy > RG) · **DG45 §3.1** (holgura +$0.01 all computed resumen fields; fecEmi/horEmi windows; N°5 numeroControl year-reset/uniqueness).
- **LB:** CT 119-D, 199, 206 as reformed (D.L. 487, 44_) · Normativa v2.0 §10 + Anexo IV (45_; §10 main-body verify → MOQ-07).
- **History:** EVID-002 (EV40; seal-before-delivery reception model).

### A9 — Catalogs
**Covers:** 33 CSV sidecars (v1.1 2026), catalog restructure, versioning/adaptation SLA, dated storage.
- **Governing EVIDs:** EVID-086 (EV44; CAT-002 +17/18; CAT-008 Distrito new ~75 codes; CAT-013 → 44-municipio model; CAT-023 → Operaciones Especiales; CAT-024 renamed "Motivo del evento" same 1/2/3; CAT-033 Tipo de Régimen new; CAT-021 renamed) · EVID-077 (EV18; Cuadro 4 adaptation SLA: structural Versiones → 10 primeros días hábiles of 3rd month; minor → next month; non-structural immediate) · **DG45** (CAT-008 usage fields N°28/49; CAT-032 domicilioFiscal N°53/71; CAT-033 N°36; CAT-025 NRE; CAT-029/030/031 FEXE).
- **LB:** Catálogos FE v1.1 2026-07 (50_/51_, EV44:EVID-086) · Normativa §19 Cuadro 4 (18_).
- **History:** EVID-004 (EV40; 2022 31-catalog matrix) · EVID-046 (EV25; v1.2 — obsolete: CAT-023, CAT-008, CAT-013 all changed).

### A10 — Taxes feeding DTE
**Covers:** CAT-015 mechanics, FE inclusive vs CCFE net, retentions (IVA 1%/13%, perception 2%), FOVIAL/COTRANS, exports 0%, pro-rata, deductibility-driven doc choice.
- **Governing EVIDs:** EVID-048 (EV01; Ley IVA Art. 54 13%, Art. 57 IVA separate from price → CCFE net) · EVID-018 (EV40; FE IVA-inclusive formulas — carried) · EVID-007 (EV40; CAT-015 3 sections: per-item multi-tax, §2 tax-as-item tipoItem 4, §3 informative — verify vs v2.0 N°84 [?]) · EVID-047/049/050/051/052/053/054/055 (EV01; taxable events/points, base rules, deductibility 65/65-A, pro-rata 66, carryforward, exports 74-77 + ZF, adjustments 62-63, excluded subjects → FSEE) · EVID-062 (EV05; retention matrix: 1% ≥$100 grandes, 13% unregistered agro/finance, card 2% perception 162-A, MH prizes) · EVID-063 (EV05; ISR retentions 10%/20%/25%/5%) · **DG45 §3.1 N°96 + Resumen** (ivaItem FE = (ventasGravadas/1.13)×13%; CRE montoSujetoRet: CCFE = TotalGravadas − descGlobal, FE = (TG − dG)/1.13; tributos per type: FE excl. 20/C3, FEXE only C3, CLE §1, NRE list; NCE/NDE item taxes N°98-101 + totals N°143-146; FSEE ivaRetenido removed, reteRenta FSEE-only N°147; CRE iva13 N°157 informative; FOVIAL/COTRANS in FEXE need authorization).
- **LB:** Ley IVA Arts. 47-77 (01_) · Reglamento IVA Arts. 29-30 (02_, EV01:EVID-058) · CT Arts. 112, 154-162-B (05_) · CT 246-A FOVIAL sanctions (EV05:EVID-065).
- **History:** EVID-023 (EV40; CCFE wording defect — resolved, see R1) · EVID-032 (EV40; DCLE 2% worked example — carried).

### A11 — Onboarding/authorization
**Covers:** emitter acreditamiento, minimum tests per DTE type and per event, authorization resolution, implementation program, physical-stock destruction.
- **Governing EVIDs:** EVID-001 (EV40; 7-step onboarding — carried) · EVID-036 (EV41; events ≠ DTEs; per-event tests) · EVID-045 (EV41; 5 invalidation + 5 contingency events; test env reusable for mandated updates) · EVID-080 (EV18; per-environment credentials, 2 months/15 days) · EVID-081 (EV18; 26_ consola sections, mandatory-starred tests) · EVID-077 (EV18; AT sets groups/dates; ALL authorized types across ALL establishments; early adoption) · EVID-074 (EV18; no physical/DTE coexistence; destruction + range reporting) · EVID-083 (EV44; transitorias: physical stock informed + destroyed within 15 días hábiles; obligation dates per AT program).
- **LB:** D.L. 487 transitorias + 119-H (44_) · Normativa §15-19 (18_ v1.2; 45_ §15 restates tiquete ban per EVID-084).
- **History:** EVID-015 (EV40; Anexo 1 placeholder — never read; superseded by EVID-045/081 test regime).

### A12 — Client↔SaaS API contract (ARCH: shared/docs/saas-thin-client-architecture.md)
**Covers:** the S0.5 decision log D1-D6 — binding architecture constraints for every S1 Odoo-Mapping Layer assignment (`odoo`/`saas`/`shared`).
- **D1 (ARCH §S0.5):** Contingency & resilience — SaaS on Fly.io multi-region; NO local-fallback generation in client; customer↔SaaS partition risk accepted, framed as force majeure per CT 119-F logic (EVID-083/EV44; EVID-084 contingency clocks).
- **D2 (ARCH):** Generation/sequencing/transmission/events/state/catalogs/versioning = SaaS; signing = client-side (encrypted cert vault, Python JWS/RS512 per EVID-079 pattern; SaaS never holds private keys); wire format = PRIVATE MINIMAL PROTOCOL (not MH JSON — schema transformation = core IP, SaaS-side); dual validation (client pre-check + SaaS authoritative, all results surfaced).
- **D3 (ARCH):** Archive tiering — Tier A mandatory local mirror of every sealed Archivo DTE + RG at response time (satisfies CT 147 reform, EVID-083); Tier B paid SaaS hosting with exit export; tier-down always compliant.
- **D4 (ARCH):** Entitlement hard wall — no subscription ⇒ no generation (server-side enforcement only); subscription state (status/expiry/grace) = standing field in every protocol response → client banner FRs; read paths (Tier A mirror) exempt.
- **D5 (ARCH):** Client license LGPL-3; SaaS proprietary, never distributed; trademark reserved. (OPL-1/AGPL-3/MIT rejected — rationale in doc.)
- **D6 (ARCH):** Multi-country hybrid — one Elixir/Phoenix SaaS, shared protocol core (auth, entitlement, archive, transmission state machine, webhooks) + namespaced payloads (`"common"`, `"sv"`, future `"gt"`); per-namespace semver; client modules share plumbing.
- **LB anchors cited by ARCH:** emitter liability non-delegable (CT 119-A/119-G, EVID-083); conservation is emitter's duty (CT 147 reformed, EVID-083); per-env certs (EVID-080); short sanctionable deadlines (24h/1-day, EVID-072/083).
- **Governing EVIDs referenced:** 072, 079, 080, 083, 084.

---

## Section S2-A — Taxation (ISR) topic clusters (synthesis worklist)

Built from W6+W7 evidence (EVID-088..108, 128..146, 148..170). Cross-topic EVIDs from S1
(A10) still apply where cited. **Citation rule for synthesis: every ISR LB cites 54_ (or the
specific reform decree 55_/56_/57_/58_) as current authority; 03_/10_ citations are
historical-LB only** (EVID-166 residual-risk note: the delta pass verified only changed +
worry-list articles, so the merge re-reads 54_ article text during synthesis anyway).

### T1 — Subjects, periods & computation methods
**Covers:** hecho generador & renta-obtenida concept (categories a–d incl. catch-all), subjects (incl. sucesiones/fideicomisos/conjuntos/irregular societies), Art. 6 exclusions + utilidad-pública qualification, fiscal year, cash vs accrual per taxpayer type (irrevocable accrual election), estate/trust period splits, branch consolidation, FX conversion (CT Art. 62).
- **Governing EVIDs:** EVID-088 (EV03; categories + catch-all + D.L. 629 representación) · EVID-090 (EV03; subjects/exclusions) · EVID-091 (EV03; periods/methods; FX doubt → resolved via CT Art. 62, T8) · EVID-129 (EV04; subjects + qualification dossier) · EVID-130 (EV04; renta concept, constructive receipt) · EVID-131 (EV04; territorial source + branch consolidation).
- **LB:** 54_ Arts. 1-2, 5-6, 13, 17-24 · 04_ Arts. 2, 6-7, 9-11, 20 · CT Art. 62 (05_ raw txt, lines 840-844: foreign-currency base converts at hecho-generador-day rate; installment-sale FX deltas added; payment-date FX difference never in base — controller read 2026-08-17, closes 03_ OQ-2).
- **History:** none (03_ = same articles, older consolidation).

### T2 — Territoriality & foreign-source exclusion (D.L. 969-2024)
**Covers:** SV-source rules (goods/services/IP/securities/government), Art. 127 partial-territory apportionment, the Art. 3.4 foreign-source exclusion, the Art. 28 pro-rata carve-out for mixed subjects, dead foreign tracks (14-A 6º-8º; 16 4ºc)/5º/7º; 27 2º-4º), surviving domestic 10% deposit/securities tracks.
- **Governing EVIDs:** EVID-092 (EV03; territoriality + anti-exemption gross-up — gross-up DEAD for foreign rents per 969-2024) · EVID-164 (EV54; Art. 3.4 + carve-out + derogations as consolidated) · EVID-168 (EV56; FULL Art. 2 derogation scope + vigencia 2024-03-22) · EVID-094 (EV03; **foreign-securities/deposit paragraphs = DEAD TEXT** per EVID-164/168; domestic Art. 27 inciso 1º / Art. 16 4º a)-b) survive).
- **LB:** 54_ Arts. 3.4, 14-A, 16, 27 (current state) · 56_ Art. 2 (derogation scope) · 57_/58_ n/a here.
- **Version note (D12):** cutover 2024-03-22; periods before it keep the old foreign tracks (dated data).

### T3 — Renta neta: deductions, non-deductibles & pro-rata
**Covers:** Art. 28 necessary-cost gate + gravadas/total pro-rata (+ 969 carve-out), Art. 29 general deductions (numerals 1-11: payroll-retention gate, relatives proof, travel/viáticos, leases, insurance 50% home-office, taxes, fuel whitelist, repairs, interest rules, inventories), Art. 29-A non-deductibles (thin-cap 3:1, active-rate+4pts, 25-SMM cash ban, IVA-doc defects, retention-linked block), Art. 31-32 (reserva legal 25% separate, bad debts + evidence checklist, donations 20% cap + qualified donee, social-benefit expenses), mermas deductibility (345-2019: inherent/measurable/real-cost + regulator recognition + zero-base guard), Reglamento segregation 50/50 + P&L adjustment layer, social funds Art. 141.
- **Governing EVIDs:** EVID-097 (EV03; Art. 28 pro-rata) · EVID-098 (EV03; Art. 29 numerals) · EVID-099 (EV03; Arts. 31-32) · EVID-100 (EV03; Art. 29-A) · EVID-139 (EV04; viáticos/tools; deposit interest — Art. 29 stale vs Ley 4.5) · EVID-140 (EV04; gravable/no-gravable segregation, 50/50 common costs) · EVID-143 (EV04; bad-debt evidence + child<25 deduction proof) · EVID-146 (EV04; employer social funds) · EVID-170 (EV56; mermas + zero-base guard).
- **LB:** 54_ Arts. 28-33, 126 · 58_ Art. 1 · 04_ Arts. 28, 31-32, 37-39, 141.
- **Crossref:** A10 EVID-050 (IVA 58-SMM cash rule vs ISR 25-SMM — different taxes, do not conflate).

### T4 — Rates, brackets & special computations
**Covers:** Art. 37 progressive table (TWO vintages: 2011-957 config exempt $4,064 / 293-2025 config exempt $6,600 effective 2025-05-08 — dated data, D7/D12), Art. 41 entities 30%/25% @ $150k, non-resident natural persons 30%, foreign conjuntos 5% gross, final-withheld rents excluded from base; capital gains (12-month rule → 10% separate vs ordinary; basis = cost − admitted depreciation; improvements; banks/insurers liquidations ordinary; capital-loss 5y ledger restricted to capital gains; **no general NOL** — SOQ-04); securities/deposits 10% separate liquidation (weighted-average cost; loss netting same-period + 5y); media-tasa method status (SOQ-01); special computations: >24-month instalment deferral (habitual traders; capital gains carved out), repossession gain/loss, rent-with-promise-to-sell, POC >1y contracts, life annuities, interest presumption, insurer/fianza determination, export income valuation; reserva legal 25% separate liquidation (from EVID-099).
- **Governing EVIDs:** EVID-093 (EV03; ganancia de capital) · EVID-094 (EV03; securities 10% — domestic tracks only post-969) · EVID-095 (EV03; tariffs; **Tramos I/II superseded by EVID-163**) · EVID-106 (EV03; losses/no-NOL) · EVID-132 (EV04; instalments/repossession) · EVID-133 (EV04; habitualidad) · EVID-134 (EV04; basis/holding-period counting) · EVID-135 (EV04; media-tasa 9-step — see SOQ-01) · EVID-137 (EV04; annuities/insurers/non-compete) · EVID-138 (EV04; POC) · EVID-141 (EV04; insurers/export income) · EVID-163 (EV54; Art. 37 current table + vintages).
- **LB:** 54_ Arts. 14, 14-A, 37, 40-42, 31.1 · 55_ Art. 1 (table verbatim) · 04_ Arts. 12-19, 22-26, 33-34.

### T5 — Withholding: payroll tables + CT retention matrix
**Covers:** salaried regime (Art. 29.7 $1,600 fixed deduction embedded in retention; Art. 33 $800×2 personal deductions; Art. 38 thresholds $9,100/$60,000), D.E. 10-2025 operative tables: monthly/quincenal/semanal brackets, NET base (bruto − no gravadas − cotizaciones laborales SS/AFP), Tramo II $1,600 not embedded, June/December recálculo (cumulative + prior-retention netting + zero floor; last-employer responsibility; CT 145 constancia 15 días hábiles), special periods via regla de tres, extraordinary remunerations aggregation, multi-employer (table on highest + 10% flat rest, excluded from recalc; January/15-días information duty), voluntary increase via DGII form, online-only filing; CT matrix for non-payroll retentions (honorarios 10%, intangibles 10%/5%, capital yields 10%, non-residents 20% definitive with reduced rates, tax havens 25%, deposits Art. 159 definitive, prizes); part-time = servicio permanente (hours-based contracts → tables, not 10%); aguinaldo Art. 4.16 (2-SMM floor; excess retention DEDUCTS floor since 458-2019; 2021-2024 $-cap transitories); deposit-interest exemption interplay (Art. 4.5 < $25k avg balance vs Art. 27/CT 159 — harmonized reading: 4.5 carves out small depositors; SOQ-07 confirms).
- **Governing EVIDs:** EVID-096 (EV03; salaried regime) · EVID-104 (EV03; retention mechanics survivors) · EVID-144 (EV04; part-time) · EVID-153..161 (EV53; D.E. 10-2025 in full) · EVID-165 (EV54; aguinaldo 4.16) · EVID-167 (EV54; transitory caps + related laws) · EV05:EVID-062/063 (CT Arts. 154-160 matrix; note EVID-063's "aguinaldo exempt" = CT 155 inc.2 general statement, yields to Ley 4.16 specifics — R22).
- **LB:** 54_ Arts. 4.16, 29.7, 33, 38-39 · 53_ Art. 1 a)-i), Arts. 2-4 · CT Arts. 154-160, 145 (05_).
- **History:** EVID-148..152 (EV10; 1992 colones-era tables — dated data rows only; D.E. 75/25 → D.E. 36 chain).

### T6 — Distributions & deemed distributions (5%)
**Covers:** Art. 72 dividend withholding (5% definitive, domiciled or not; "utilidades" broad definition incl. reserva legal distribution; payment/credit events incl. in-kind/compensation/loss application), Art. 73 permanent establishments, Art. 74 capital reductions (profits-first), Art. 74-A partner/preferential-regime/head-office loans (5%; default >6 installments or >1y → full consideration gravable + interest non-deductible; exceptions), Art. 74-B no-retention cases, Art. 74-C Registro de Control de Utilidades per shareholder, Art. 25 society loans to shareholders = dividends; exempt-entity distributions flow-through (Reglamento Art. 18).
- **Governing EVIDs:** EVID-103 (EV03; full 5% regime) · EVID-136 (EV04; exempt-society distributions).
- **LB:** 54_ Arts. 25, 72-74-C · 04_ Arts. 18-19 · CT Art. 158-A carve-out + 242 b)/c)1) sanctions (05_, collect in synthesis from EVID-063/065 zone).
- **Crossref:** A10 EVID-063 (CT 156-B capital-yield advances 10% — distinct from 72's 5%; synthesis must keep the two withholding tracks apart).

### T7 — Fixed assets: depreciation, software & registers
**Covers:** Art. 30 rates (5/20/25/50% edificaciones/maquinaria/vehículos/otros), used-asset base caps (80/60/40/20%), ≤12-month assets full cost, construction-asset capitalization into cost, no revaluation, land not depreciable, mixed-use pro-rata, no catch-up, DGII authorization for % changes, IVA-exempt import machinery DGII value cap; Art. 30-A software 25% mirror; seasonal-activity full-quota rule (192-2018; cafetalero/cañero exemplars = open list → config flag); mandatory per-asset depreciation register field list (Reglamento Art. 84 survivor: specification, value, start date, useful life, improvements, additions, quota, balance, retirement, disposal); maquinaria definition (Reglamento Art. 35).
- **Governing EVIDs:** EVID-101 (EV03; Art. 30) · EVID-102 (EV03; Art. 30-A) · EVID-142 (EV04; export income + maquinaria) · EVID-145 (EV04; Art. 84 register) · EVID-169 (EV56; seasonal depreciation).
- **LB:** 54_ Arts. 30, 30-A · 57_ Art. 1 · 04_ Art. 35, 84 (+ Art. 34 consumed by T4 — `taxation/03_isr-rates-gains.md` LB-019/FR-100).
- **Crossref:** T4 capital-gain basis (= cost − accumulated admitted depreciation, EVID-093/134).

### T8 — Filing, payment & procedure routing
**Covers:** annual declaration 4-month window (Art. 48/51), Art. 92 filing-duty catalog (incl. IVA-registered persons; salaried Art. 38 exception; $60,000 mandatory threshold per 53_ Art. 1 i)), conjunto event returns (día hábil siguiente, solidarity), online-only filing for withheld persons (53_ Art. 2), Art. 105-A stale sanction (colon minimum — superseded by CT 226-247 zone per EVID-065), the massive repeal map routing procedures to CT (Ley ~70 arts; Reglamento D.E. 117-2001 map), 10-días-hábiles retention remittance + December rule (Art. 62 — likely CT-superseded, flag), FX conversion rule (CT Art. 62).
- **Governing EVIDs:** EVID-107 (EV03; declaration/payment) · EVID-108 (EV03; repeal map + final provisions) · EVID-128 (EV04; Reglamento norm identity + repeal map — R17) · EVID-161 (EV53; online filing + $60k) · EV05:EVID-065 (sanctions zone).
- **LB:** 54_ Arts. 48-53, 62, 75, 92, 105-A · 53_ Art. 1 i), Art. 2 · CT Arts. 62, 226-247 (05_).

## Section S3-A — Fiscal-reporting topic clusters (synthesis worklist)

Built from W8 evidence (EVID-172..190). **Citation rule for synthesis: the forms/manuals
ARE the primary authority for declaration mechanics** (34_ = F-07 v14 manual ENERO 2025 +
39_ form Actualizado 15-08-2025; 35_ = F-14 v16 manual OCTUBRE 2025 + 38_ form;
59_ = F-14 v17 form 2026-06-03); legal anchors (CT/Ley/Decreto) cited per the S2 order
where the forms reference them. Version regime (D12): F-07 v14 current; F-14 = v16 annex
mechanics + v17 form layout (Quincena-25 section, EVID-184) — synthesis writes FRs
against the v16 annex format with a v17 vintage row for the form-level Quincena-25 change.

### F1 — F-07 declaration engine: casilla graph & payment computation
**Covers:** the 77-row casilla arithmetic (39_/EVID-179): sales buckets 5-21 → SUMA VENTAS 105 / débitos 141-150; compras 24-33 + otros créditos 34-41 → SUMA COMPRAS 100 / CRÉDITOS 145; remanente 155 vs impuesto determinado 160; retenciones al declarante 161-166 + Art. 74-A disminución 491-493→203; excedente 167 / total 168; D.L. 764-2014 control-de-liquidez credit 520; FOVIAL credit 525; 521; retenciones por el declarante 169-172→187-190 (+modificatoria 401-405→188); reintegro exportadores 523/524; multas 192-195 + intereses 196 → TOTAL A PAGAR 198; Art. 74-A flag + declaración que modifica; USD-only.
- **Governing EVIDs:** EVID-179 (39_ + 36_ index).
- **LB:** 39_ (form arithmetic) + CT Arts. 74-A, 162, D.L. 764-2014 Art. 10.7 (anchors named on the form).
- **Crossref:** taxation A-clusters (IVA computation = Ley IVA Arts. 54-66, W3 evidence EV01/02); FOVIAL/COTRANS quantity-tax risk (31_).

### F2 — Annex upload engine: file format + validations + modificatorias
**Covers:** semicolon CSV, all-Text cells, ≤25-char filename, no headers/merged cells, 2-decimal truncation, 0.00 nils, no negatives (except anulados CT 111), DD/MM/AAAA period-consistency (anulados + compras 3-prior-period windows: CT 111 / Ley IVA 63), annex-number column on every row, per-annex structure check; modificatorias = annexes 3-12 carryover + 1-2 re-upload; casillas auto-total from annexes (no manual fill).
- **Governing EVIDs:** EVID-173 (34_ §II + notes) · EVID-178 §XVI-XXVII (34_).
- **LB:** 34_ §II/§XVI-§XVII + CT Art. 111 + Ley IVA Art. 63 (anchors printed in the manual).

### F3 — Sales annexes 1-2: row models + DTE identifier mapping + Renta pair
**Covers:** Anexo 1 per-document B2B (CCF/NC/ND; clase 1/2/4; DUI/NIT XOR period-gated; R/S Tipo-Operación/Tipo-Ingreso from Enero-2025 else 0; codes 1/2/3/4/12/13 and 1-10/12/13); Anexo 2 aggregated B2C (tipos 01/02/10/11; physical ranges DEL/AL; DTE rows grouped BY DAY with first/last código de generación; N/A resolución/serie; máquina registradora for tiquetes; gravadas locales IVA-INCLUSIVE mirroring R1/FE convention; export split dentro/fuera CA (GT/HN/SV/NI/CR) + servicios + ZF/DPA tasa 0; negatives only anulados; Aduanas cross-check awareness).
- **Governing EVIDs:** EVID-174 (34_ §III) · EVID-175 (34_ §IV).
- **DTE identifier mapping (operative everywhere):** Serie = sello de recepción (40c); Resolución = número de control (28c), pre-Nov-2022 = código de generación (32c); Número = código de generación (32c), pre-Nov-2022 = número de control; control interno blank for DTE.
- **Crossref:** e-invoicing FR-012/018 (identifier fields); taxation T4 (R/S feeds the F-11 rentas matrix; code 12 = F14/F910-consolidated, 13 = Art. 6 LISR excluidos).

### F4 — Purchase annexes 3/5/16: IVA buckets + ISR cost/gasto quartet + excluidos
**Covers:** Anexo 3 column model (internal/internación/importación × gravada/exenta buckets; crédito = 13% of gravadas J..M; total G..M with ND+/NC−; tipos 03/05/06/11/12/13; ZF/DPA tipo 11 per Ley ZF Art. 25; Tesorería pseudo-NIT 06140108140066 for foreign 12/13; Q/R/S/T ISR quartet from Feb-2024 with code 8 dedup + 9 public/non-deductible); Anexo 5 excluidos purchases (CT 119 anchor; 13% retention; post-entero crédito re-entry into casilla 128); Anexo 16 Decreto 357 (informativo, mayo-2022→fin-de-obra window).
- **Governing EVIDs:** EVID-176 (34_ §V) · EVID-177 (34_ §VII).
- **Crossref:** taxation T3 (pro-rata feeds 132-134 credits); special-regimes wave (ZF/DPA, Ley ZF Art. 25).

### F5 — Retention/perception annexes 4/6-12 + F-930 view
**Covers:** al-declarante credits (161 anticipo 2%, 162 retención 1%, 163 percepción 1%); por-declarante payables (169 percepción 1%, 170 retención 1%, 171 anticipo 2%, 172 retención 13%); Anexo 4 cuenta-de-terceros domiciliados (mandante + CCF/factura + comprobante-de-liquidación linkage, monto sin IVA for FC); CRE (07) and CL (08) document types wired via the standard DTE identifier mapping; % validation (1/2/13); F-930 v3 = the standalone monthly inform over the same ledger (document-typed summary + calidad/modalidad).
- **Governing EVIDs:** EVID-177 (34_ §VI/VIII-XIV) · EVID-189 (63_).
- **Crossref:** e-invoicing CRE/CL FRs; taxation T5 (IVA-side vs ISR-side matrices stay distinct).

### F6 — Anulados/emitidos annex + DTE event feed
**Covers:** XIX annex columns A-J (resolución/clase/preimpreso DESDE-HASTA/tipo 01-14/tipo-detalle/serie= sello 40c/DESDE-HASTA/código-generación); detail codes A (anulado) / X (extraviado) / D (DTE invalidado); Documentos EMITIDOS annex auto-derived from annexes 1/2/9/10/11/12 (only anulados uploaded); invalidation events feed from the e-invoicing module (this answers e-invoicing 02 OQ-008's F-07 side; NRE-on-origin-invalidation 02 OQ-009 unaffected).
- **Governing EVIDs:** EVID-178 (34_ §XVIII-XIX).
- **Defect ruling (S3):** §XIX col J "36 caracteres" and the inverted Sept/Oct cutover in col A are manual defects — the annexes-1-12 convention (32c; Nov-2022 cutover) is operative (see S3 OQ register).
- **Crossref:** e-invoicing 03_events FR-103/104/117 (invalidation events are the source); R8 2-year window context.

### F7 — Fuel & dated-regime annexes 13-17
**Covers:** Anexo 13 tasas diferenciadas (Decreto 321, from Mar-2022, MANUAL entry, global net-of-IVA by SUPERIOR/REGULAR/DIÉSEL; 13% ops stay in annexes 1-3); Anexo 14 precios-máximos NC detail (Ley Especial Transitoria, from Abr-2022; galones 11+8 decimals; price/valor/descuento/IVA-del-descuento sin IVA); Anexo 15 (casilla 92) + 16 (casilla 65) Decreto 357 informatives; Anexo 17 importadores (Jun-Ago 2022 closed window, informativo). All vintage-gated (D12 dated regimes; regime-validity windows as data).
- **Governing EVIDs:** EVID-178 (34_ §XX-XXIV).

### F8 — F-14 declaration & retention annex engine
**Covers:** annex columns A-W (domiciliado/país/NIT-NIF/DUI/código-ingreso; devengado vs bonificaciones vs aguinaldo exento/gravado split for payroll codes 01/60/80; SEVEN SS columns with legal caps AFP $472.93 + ISSS $30 + INPEP 7.5% + IPSFA 9.5% + CEFAFA 5% + Bienestar Magisterial 5.58% + ISSS-IVM 7.5% [dated data, payroll-wave feed]; Renta quartet S-V from Feb-2024; periodo MMYYYY); validations (retention % = legal rate per code — system rejects; aguinaldo gravado ≤ devengado; caps; 2-decimals; DUI/NIT XOR); haven 25% exactness; declaration = pure projection of the annex (no manual casillas); modificatoria = limpiar + full re-upload + prior-amount anchors (casillas 50/221/225/332/711/761); form tab architecture (Pago a Cuenta / Acreditables con-sin dependencia / Definitivas / Op. Financieras 501-529 liquidity tracks / Contribución Especial / No Domiciliados / Agentes Extranjeros 701-780); pago-mínimo remnant casilla printed but DEAD (R21 — never feed).
- **Governing EVIDs:** EVID-180 (35_ + 37_) · EVID-181 (35_) · EVID-183 (38_ + country codes 35_).
- **Crossref:** taxation T5 (rates/base FR-102..131 compute the values this annex reports; SOQ-02 proration affects rows); payroll wave (SS caps + aguinaldo/quincena splits); CT 154-160 matrix LB-017/019.

### F9 — Income-code catalog & cross-tax consolidation (F-14 apéndice + F-910)
**Covers:** income codes 01-85 with class = acreditable/definitiva/sin-retención(60)/no-gravado(70-72); 43/44/45 = distributions leg (Art. 72/74/74-A → taxation T6 earnings-register interface); 40 = haven 25%; 47 = CT 123 aggregate (NIT 14 zeros + VARIOS); F-910 v9 annual consolidation (01-vs-60 rule: retained-at-least-once → 01, never → 60; ANNUAL SS columns); F-910 = the CT 123 surface that taxation 04 OQ-007/MOQ-10 hunted (ISR side).
- **Governing EVIDs:** EVID-182 (35_ apéndice) · EVID-187 (61_).
- **Crossref:** taxation T5/T6; F3's R/S code 12 wording ("consolidados en F910").

### F10 — F-14 v17 Quincena-25 vintage + annex-format gap
**Covers:** v17 form = v16 + "INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO" (row 61, casillas 417 número-de-sujetos / 418 monto) with rows 61-104 → 62-105 renumbered; annex-level representation UNKNOWN (no v17 manual/plantilla yet — MH checked 2026-08-18); the Quincena-25 law itself not in corpus (acquisition candidate numbering ≥65); payroll wave co-dependency.
- **Governing EVIDs:** EVID-184 (59_ vs 38_ diff).

### F11 — Related informs: F-915 (distributions) + F-935 (agentes extranjeros)
**Covers:** F-915 v4 (DISTRIBUYÓ/CAPITALIZÓ + acta fecha/número; socio-quality transitions antes/durante/perdió × cantidad/utilidades/valor-contable; per-socio rows incl. no-domiciliado; CT 241 + CP 249-A juramento) — the published format behind Ley ISR Art. 74-C's inform (partially answers taxation 05 OQ-002: format exists, norms resolution still absent); F-935 v1 (RETENCIÓN vs ENTERO blocks; transfer-level rows with número-de-transacción + país-de-origen; donantes-locales track anchor OQ).
- **Governing EVIDs:** EVID-188 (62_) · EVID-190 (64_).
- **Crossref:** taxation T6 (earnings register feeds F-915); F8's agentes-extranjeros tab.

### F12 — Filing calendar & deadline engine
**Covers:** monthly core F-07/F-14/F-06/F-930/F-935/F-945 (+F-960); annual anchors F-910/F-915/F-986/F-987 (Feb), F-455 fusión dictámenes CT 134 (Mar), F-11/F-971/F-944/F-30/F-40/F-982 (Apr), auditor-fiscal appointments CT 131 (May), F-950 quarterly pattern; asuetos table feeding días-hábiles computation; due-day windows = visual calendar layer (unpinned — S3 OQ); "fechas pueden ser modificadas por la Asamblea" disclaimer → calendar as dated data.
- **Governing EVIDs:** EVID-185 (30_) · EVID-186 (30_).
- **Crossref:** e-invoicing FR-103 deadlines (same días-hábiles engine); taxation T8 (10-días-hábiles remittance); 01-file FR-032.

## Section S4-A — Payroll topic clusters (synthesis worklist)

Built from W9 evidence (EVID-191..210). **Citation rule for synthesis: labor LBs cite
11_ (CT); SS rates cite 08_ Art. 29 (ISSS) / 09_ Arts. 13-16 (SIP D.L. 614 — never
SAP-era lore); SMM values cite 16_ as dated data; ISR/retention interfaces cite the
S2 files by FR id (no re-derivation); F-14 column semantics cite the S3 files.** Cap
VALUES not in any law (ISSS base cap, AFP IBC ceiling, instituto rates) enter as
dated data from the F-14 v16 print (SOQ-11 discipline) with instrument OQs.

### P1 — Salary model: salario vs salario básico
**Covers:** CT Art. 119 salario definition (integrantes: habitual bonuses, overtime, rest/asueto-day pay, profit shares; excluded: occasional gratuities, reimbursements, prestaciones sociales), Art. 140-143 salario básico as the universal base for employer money obligations, Art. 142 seven derivation rules (hourly/period/mixed/obra/destajo/a domicilio/commission-6-month), equal pay (Art. 123), salary credits first-priority (CT 121; ISSS first-class 08_ Art. 36; SIP privileged 09_ Art. 25).
- **Governing EVIDs:** EVID-201 (EV11) · EVID-195 (EV08, credits) · EVID-198 (EV09, privileged).
- **LB:** 11_ Arts. 119-123, 140-143 · 08_ Art. 36 · 09_ Art. 25.
- **Crossref:** 09_ Art. 14 IBC (near-identical exclusion list — synthesis maps, does not duplicate).

### P2 — Salario mínimo chassis + dated tables
**Covers:** CT Arts. 144-148 (8h reference; 5-8h full SMM; <5h proportional unless completing week; piece-rate floor per jornada; de-pleno-derecho substitution of inferior wages), Art. 159 triennial review, Decreto 11-2025 tables (4 time-based sectors + piece-rate caña/café + Art. 6 descanso prestación table), rendimiento caps (2 t/jornada, tarea geometry), home-worker routing, benefit bases = max(daily SMM, actual salary) (16_ Art. 7).
- **Governing EVIDs:** EVID-191 (EV16) · EVID-192 (EV16) · EVID-208 (EV11).
- **LB:** 16_ Arts. 1-15 (D.O. 95 T.447 23-May-2025; effective 2025-06-01; repeals D.E. 9/10-2021) · 11_ Arts. 144-160.
- **Version regime (D12):** SMM rows = dated data; prior vintage (2021 pair) absent from corpus (EV16 OQ-3).

### P3 — Work time, surcharges, descanso semanal, asuetos
**Covers:** jornada limits (8/44 diurno, 7/39 nocturno, >4h-nocturna classification, peligrosas 7/39-6/36), ≥8h rest between jornadas, nocturnal +25% (Art. 168), overtime +100% of salario básico/hour with weekly-excess base rule (Art. 169 + Art. 142 final), fuerza-mayor exception, permanent-extra pacts (Art. 170), séptimo día (complete-week accrual at básico; presumed included in period salaries — decomposition; rest-day work básico+≥50%+compensatorio; no-horario 6-day rule; piece-rate prestación from 16_ Art. 6), asueto set (CT 190 static list + 191 básico + 192 2× pay + 193 exceptions + 194 coincidence) with the calendar dated-data overlay (30_; divergence → SOQ-19).
- **Governing EVIDs:** EVID-202 (EV11) · EVID-203 (EV11) · EVID-205 (EV11) · EVID-192 (EV16, piece-rate prestación).
- **LB:** 11_ Arts. 161-176, 190-195 · 16_ Arts. 5-6 · 30_ (dated asueto data, EV30 crossref).
- **Crossref:** fiscal-reporting/08 días-hábiles engine (shared asueto table).

### P4 — Vacaciones
**Covers:** 15 days + 30% surcharge (Art. 177), 200-worked-days gate (180), continuity rules (181), scheduling windows + 30-day notice (182), base derivation (183: current básico or 6-month average ÷ días laborables), lodging/food +25% each (184), pre-payment rule (185), termination proration (187), cash-compensation prohibition + fractional schemes (188-189).
- **Governing EVIDs:** EVID-204 (EV11).
- **LB:** 11_ Arts. 177-189.

### P5 — Aguinaldo (labor computation)
**Covers:** obligation + tiers 15/19/21 days by seniority (Arts. 196-198), proportional for <1 year at Dec-12 (197), base derivation (199), payment window 12-20 December (200), no disciplinary forfeiture (201), termination proration (202), justifiable-absence days count (203). ISR exento/gravado split = taxation-owned (R22 vintages in taxation/04); payroll supplies the gross prima + the floor check (2×SMM comercio y servicios = $817.60 with 16_ feed).
- **Governing EVIDs:** EVID-206 (EV11) · EVID-191 (EV16, SMM feed).
- **LB:** 11_ Arts. 196-203 · 16_ Art. 2 (comercio y servicios row).
- **Crossref:** taxation/04 aguinaldo FRs (R22/SOQ-05); fiscal-reporting/06 F-14 annex aguinaldo exento/gravado pair.

### P6 — Social-security contributions: rates, bases, caps, regime routing
**Covers:** ISSS salud 7.5% patrono / 3% trabajador (08_ Art. 29); Art. 99 public special 6.68%/2.67%; SIP 16% = 7.25% trabajador + 8.75% empleador with 9.0/6.0/1.0 destination split and the never-pass-through invariant (09_ Art. 16); IBC = ordinary-services money remuneration (vacations/commissions in; aguinaldo/viáticos/ocasionales out), SMM floor, calendar-day months, multi-job per-salary, subsidy months (09_ Art. 14); independent workers full-share (09_ Art. 15); affiliation/routing (AFP choice, 20-day default, IPSFA/IvD exclusions — 09_ Arts. 8/11); pensioner-side rates (7.80% health R23; 7% solidarity >6×PM — payroll-adjacent); CAPS as dated data (F-14 print: AFP $472.93, ISSS $30, INPEP 7.5%, IPSFA 9.5%, CEFAFA 5%, Bien. Mag. 5.58%, ISSS-IVM 7.5% — SOQ-11/16/17 instrument OQs).
- **Governing EVIDs:** EVID-193 (EV08) · EVID-194 (EV08) · EVID-197 (EV09) · EVID-200 (EV09).
- **LB:** 08_ Arts. 3, 29, 33-34, 99-100 · 09_ Arts. 8, 11, 13-16, 121, 154 · F-14 v16 print (caps as dated data).
- **Crossref:** taxation T5 (retention base nets worker-side cotizaciones per 53_ literal d); fiscal-reporting F8 (annex column model).

### P7 — SS declaration, remittance, sanctions
**Covers:** declare + pay pension cotizaciones within the FIRST 10 DÍAS HÁBILES of the following month, electronic planilla carrying BOTH the AFP declaration and the ISSS obrero-patronal planilla (09_ Art. 21); omission/inconsistency cure procedure (09_ Art. 22); ISSS late recargo 1%/month-or-fraction (08_ Art. 33); SIP sanctions (late declaration 5% ≤20d / 10% >; non-enrollment 15%; non-payment 20% + 2%/mo; underpayment 10% + 5%/mo — 09_ Arts. 143-145); employer-share no-deduction invariant + restitution (08_ Art. 33); work-accident reports ≤48h (08_ Art. 75); planilla única mechanism (09_ Art. 27); employer record duties (16_ Art. 11 planillas/asistencia/recibos; CT Art. 160 inspection).
- **Governing EVIDs:** EVID-195 (EV08) · EVID-198 (EV09) · EVID-192 (EV16).
- **LB:** 09_ Arts. 21-24, 27, 143-146 · 08_ Arts. 33, 75 · 16_ Arts. 11-13 · 11_ Art. 160.
- **Crossref:** fiscal-reporting/08 días-hábiles engine; taxation T8 (same 10-días-hábiles window family).

### P8 — Contracts, termination, indemnización, illness & maternity benefits
**Covers:** contract taxonomy (indefinido presumption + plazo validity gates Art. 25; obra with 7-day notice Art. 26; interinos Art. 27; 30-day trial Art. 28); unjustified-dismissal indemnización = 30 days básico/year + prorated fractions, min 15 days, countable salary capped at 4× daily SMM (Art. 58); fixed-term variant (59); termination constancia (60); illness subsidy 75% with seniority-tier day caps (307-308); chronic-illness stability + full ISSS subsidy (308-A/B); maternity 16 weeks @75% básico, 10 post-partum mandatory, ISSS subsidy deductible, **Art. 311 tenure gate VOID (sent. 105-2014)** (309-312); lactancia 1h/d paid (312); sepelio 60 days básico (313); vacation/aguinaldo termination proration (187/202).
- **Governing EVIDs:** EVID-207 (EV11) · EVID-209 (EV11).
- **LB:** 11_ Arts. 25-28, 55-60, 307-313 + notes block (sent. 105-2014).
- **Crossref:** P2 (4×SMM cap feed).

### P9 — Payroll ↔ ISR/reporting interfaces
**Covers:** worker SS/pension cotizaciones excluded from the ISR retention base (53_ literal d — consumes taxation/04 FRs, no re-derivation); aguinaldo exento/gravado split feed to F-14 annex (F8 columns); the 7 SS columns + Renta quartet S-V as payroll-produced values (SOQ-11: payroll owns the values, F-14 mirrors as validation params); F-910 annual consolidation feeds (61_: 01-vs-60 rule, annual SS columns); F-11 personal deductions 711-725 (SS rows 713-724, AFP voluntary 717 with the stale-label warning, deducción fija 722); voluntary pension savings ≤10% IBC deductible + 5-year withdrawal clawback (09_ Art. 138); cotizaciones/rendimientos rentas no gravadas (09_ Art. 26 ↔ Ley ISR Art. 4); rentas matrix S-wiring (65_ OQ-1, taxation-side).
- **Governing EVIDs:** EVID-199 (EV09) · EVID-210 (EV65) · EVID-198 (EV09, 10-días deadline family).
- **LB:** 09_ Arts. 21, 26, 138 · 65_ (form zones/casillas) · S2/S3 files by FR id.
- **Crossref:** taxation/04 + 01; fiscal-reporting/06 + 07.

### P10 — Quincena Veinticinco (UNBLOCKED 2026-08-18 — W11 acquisition 66_-70_)
**Covers:** the Ley Especial Quincena Veinticinco = **D.L. 499, D.O. N° 8 T.450 14-ene-2026 (effective same day), acquired as 66_** (official DGII copy via transparenciafiscal after the D.O. outage) + the full implementation package 67_ (Guía fiscal), 68_/69_ (upload instructions/manual), 70_ (plantilla). Benefit = **50% of monthly salario básico o nominal, gate ≤ $1,500, paid 15–25 Jan each year**; mandatory for public AND private from 2027; **2026 transitory: public mandatory / private VOLUNTARY with a 100% ISR tax credit** (remanent → other ISR obligations; ZF/DPA/LSI → negotiable Certificado de Crédito Tributario auto-generated at FY-2026 filing). Worker invariants: renta no gravada, NO ISR retention, NO SS/pension contributions, NOT in any benefit-calculation base, inembargable; eligibility mirrors aguinaldo/CAE per sector; termination-with-responsibility before 25-Jan → proportional right. Employer: gasto deducible (paid + original signed planilla + F-14 annex). Tercerización: FCF con valor exento + no Ley-IVA-Art.-66 pro-rata. Reporting chain: **F-14 v17 January-only annex (7-column semicolon CSV: APELLIDOS 100 / NIT 14 XOR DUI 9 / dd/mm/aaaa / SALARIO 4+2 / QUINCENA 3+2 / mmaaaa) → casillas 417/418 → F-910 NO GRAVADOS auto code 73 → renta-en-línea casilla 724 extension → F-11 v19 casilla 319 credit; ZF/DPA/LSI checkbox → F-11 v20 + certificado anexo**.
- **Governing EVIDs:** EVID-236 (EV66 law) · EVID-237 (EV66/67 fiscal) · EVID-238 (EV67/68 declaration surfaces) · EVID-239 (EV68/69/70 file format + portal).
- **Status:** evidence complete; payroll/08 + fiscal-reporting FR fold-ins = next edit wave (S6 fix-wave candidates); F-11 v19/v20 prints to acquire (≥71).
- **Crossref:** P1 (category matrix), P5 (aguinaldo gates), P9 (F-11 711-725 feeds — casilla 724 label + 319), F8/F9/F10 (F-14 annex + code 73 + January window), special-regimes (certificado).


---

## Section S5-A — Commercial-legal topic clusters (synthesis worklist)

Built from W10 evidence (EVID-211..235). **Citation rule for synthesis: mercantile-registry
and accounting LBs cite 07_ (D.L. 671, consolidated ≤ reform (29) D.L. 641-2008 — post-2008
reforms UNVERIFIED, SOQ-22); AML thresholds/clocks cite 15_ Art. 9/9-A/9-B (as reformed
(2)–(6), current) — NEVER 17_'s superseded colones/3-day values (R26); 17_ citable only
for window mechanics, no-tip-off, and red-flag catalogs; society type menu may be
incomplete without the SAS law (SOQ-23); cap/threshold values are code-text (not
instrument-dated) unless flagged.**

### C1 — Comerciante status, matrícula & Registro de Comercio
**Covers:** comerciante definitions (individual/social; presumption by publicity/establishment, Arts. 1-6); the four professional obligations (Art. 411); matrícula de empresa = registro único, permanent + ANNUAL renewal, locales/agencias/sucursales registration (412-420); constancia = sole proof of status (418); closure sanction + 30-hábiles grace (419); cancellation cases (422); Registro architecture under CNR (matrículas/documentos/balances; poderes-nombramientos-credenciales; 456-487); matrícula-precondition-to-registration (469); publication rule 3× alternate D.O.+daily, deadlines from last D.O. publication (486); ag/professional-collective exemption from L.II except 411 I/IV (Art. 20).
- **Governing EVIDs:** EVID-211 · EVID-212 · EVID-217 (all EV07).
- **LB:** 07_ Arts. 1-6, 20, 411-422, 456-487.
- **Crossref:** 29_ CNR F985/F-975 mechanics (EVID-172); e-invoicing emitter identity (A11).

### C2 — Accounting regime: books, legalization, no-alteration, retention
**Covers:** organized system per accepted standards + electronic systems EXPRESSLY legal with watchdog notice (435); castellano + USD accounts + in-country keeping (436); keeper thresholds ≥$12k individuals / all sociedades (437); book legalization by Contador Público / Auditor Externo + folios + opening razón (438); **no-blancos/raspaduras + immediate rectification-asiento regime (439)** extended to ALL statutory registers (440); **retention 10y + 5y post-liquidation; received/issued facturas + correspondence anexas to the books (451/454)**; media migration (microfilm/optical) only ≥24 months after emission, notarized copies equivalent (455); <$12k single bound book + annual balance (452); inventory/balance first Diario partida (446); labor-obligation provision (447).
- **Governing EVIDs:** EVID-213 · EVID-215 · EVID-216 (all EV07).
- **LB:** 07_ Arts. 435-455.
- **Crossref:** e-invoicing 02 §3.11 correction-accounting invariants (kin); D3 archive tiers; AML retention C10 (longest-per-object matrix = synthesis deliverable, SOQ-28).

### C3 — Annual financial statements & balance deposit
**Covers:** FY-close balance general + resultados + cambios-en-patrimonio within 3 months IMPRORROGABLE, auditor externo handoff (282-283); auditor dictamen 30d (284); junta approval → **DEPOSIT in Registro de Comercio = third-party effect, no deposit no fe** (286/441); threshold ladder: individuals ≥$12k signed propietario+contador, ≥$34k + auditor-certified, sociedades+EIRL always full set with dictamen (474); registro de balances (459); registro de Estados Financieros contents (442); valuation criteria Consejo de Vigilancia → NIC fallback (443-444) = the NIIF hook for chart-of-accounts; revaluation reserva (445); MH exception for ISR declarations (286 final).
- **Governing EVIDs:** EVID-214 (EV07).
- **LB:** 07_ Arts. 282-286, 441-445, 459, 474.
- **Crossref:** chart-of-accounts wave (32_/33_ consume the NIC anchor); fiscal-reporting F12 calendar kin.

### C4 — Society data model: types, formation, capital, reserves
**Covers:** type taxonomy personas/capitales × fijo/variable (18); escritura pública + 12-field content (21-22); **personality ONLY at inscription (25)** + inscription catalogue (24/465); estatutos deposit (23); capital = pasivo-side invariant, assets ≥ capital (29); apportations incl. non-money valuation rules (31-33); dividend ceiling = realized per-balance profit (37-38); **reserva legal: colectiva 5% → 1/6 capital (91); SRL+S.A.+EIRL 7% → 1/5 floor (123/295/616)** with restoration duty (39); 4 society books incl. capital-variable movements (40); SRL profile (Ltda. suffix, $2,000 min, participaciones $1+ multiples, 5% exhibit, voto-por-dólar, 3/4-quorum, Registro de Socios 7-field book, auditor mandatory) (101-125); S.A. profile (acciones $1+, nominativas-until-paid, no below-par, no self-acquisition/no own-share loans, share-ledger 8 fields, 15-day preferential windows, auditor monthly duties) (126-160, 289-293); cooperative special rules (19).
- **Governing EVIDs:** EVID-218 · EVID-219 · EVID-220 (all EV07).
- **LB:** 07_ Arts. 17-43, 101-160, 289-295.
- **Crossref:** SAS type = SOQ-23 acquisition; taxation/05 distributions (reserve/profit interplay).

### C5 — Society lifecycle: capital variable, fusión, liquidación, nullity, extranjeras
**Covers:** capital variable (de C.V. suffix, movement book consultable, withdrawal year-end effects, minimum disclosure) (306-314); fusión (90-day opposition window, publication of agreement+last balance, Ley de Competencia inscription checkpoint, personality until inscription) (315-321); transformación (successor continuity, unlimited-liability survival for pre-change ops, auditor valúo for personas→capital) (322-325); liquidación ("en liquidación" suffix, ≤2y, liquidator faculties incl. fiscal obligations, final balance deposited, **post-liquidation books+papers bank deposit 10y**) (326-342); revocación de disolución (342-A); nullity/irregularity (illicit object, 90-120d regularization windows, unlimited liability, **15-day escritura-presentation duty**, 4-month registro check, out-of-object reform, single-socio 3-month collapse → empresa individual) (343-357); extranjeras (registration package: statutes, domicile decision, resident representative + poder, MINEC investment-registry capital proof, balance inicial certified; sucursal domicile) (358-361).
- **Governing EVIDs:** EVID-221 · EVID-222 (all EV07).
- **LB:** 07_ Arts. 306-361.
- **Crossref:** CT solvencia at liquidation (EIRL, 620); e-invoicing emitter-name suffix propagation (A8 kin).

### C6 — Auxiliares del comercio & authority defaults
**Covers:** factores (general authority from appointment, registry inscription of powers + terminación, post-revocation validity until notice/inscription) (365-377); dependientes (bind principal; in-store collection unless caja-reserve posted; outside sale/collection = written authorization + ID or recibo/factura with firma y sello; viajeros order-taking + guarantees but no advance collection/plazos/quitas/descuentos) (378-383); agentes dependientes (plaza exclusivity default, operations book per principal, monthly documented-account remuneration) (384-391); agentes representantes/distribuidores (continuous designation, exclusive-zone commissions incl. principal's own deals, 3-month termination notice, 5-head indemnification scale, just causes, foreign-principal import bar until compliance) (392-399-B); intermediarios (own registro + diario books, no representation) (400-410).
- **Governing EVIDs:** EVID-223 (EV07).
- **LB:** 07_ Arts. 365-410.
- **Crossref:** payroll salesperson/authority profiles (11_ labor layer governs employment side).

### C7 — Empresa mercantil, establecimiento & EIRL
**Covers:** empresa = transferable bien mueble; statutory element package (establecimiento, clientela+fama, nombre+distintivos, arrendamientos, mobiliario/maquinaria, labor contracts, mercancías/créditos); debt succession on transmission; >6-month inactivity kills empresa character; transferor 2-year non-compete; local-change publication 15d (553-569); nombre comercial/distintivos/patentes DEROGATED to IP laws (570-599); EIRL (E. de R. L. suffix, auditor-certified pre-constitution inventory, free capital, formulario-based 7-field registration, capital down not below 1/4 paid, 30-day opposition on inventory publication, reserve/profit/statements/vigilancia incorporation by reference, forced-liquidation triggers, **CT-solvency-checked voluntary liquidation**) (600-622).
- **Governing EVIDs:** EVID-224 (EV07).
- **LB:** 07_ Arts. 553-622.
- **Crossref:** C5 (lifecycle); taxation (liquidation solvencia — CT link).

### C8 — Payment instruments, prescription & proof
**Covers:** títulos valores general rules (castellano; words-over-figures + lower-sum; máquina protectora precedence; inhábil-day extension; salvo buen cobro; enrichment action 1y) (623-653); pagaré (6-field content, default vista/domicilio rules) (788-792); **cheque (número+serie mandatory, 7-field form, raspaduras void; presentation 15d same-plaza / 1m national / 3m cross-border; agency 72h; protest ≤15d or bank note; caducidad cascade; 1y prescription; ≥20% refusal indemnity; special cheques: cruzado, abono-en-cuenta, certificado, viajero 2y, limitado, circular, caja/gerencia)** (793-838); mora interest pactado→legal, legal rate fixed periodically by Economía (960); solidarity of codeudores/fiadores (962); **mercantile prescription matrix 6m cta-cte rectification / 1y cheque-letra-regreso-vicios-transporte-corporate / 2y compraventa-sociedad-suministro-comisión / 5y credit contracts from LAST RECOGNITION** (995); caducidad no-suspension (996-998); proof means incl. **facturas + registros contables** (999) + legally-kept books win (1002).
- **Governing EVIDs:** EVID-225 · EVID-226 (all EV07).
- **LB:** 07_ Arts. 623-653, 788-838, 945-1012.
- **Crossref:** fiscal-reporting F12 días-hábiles engine (inhábil-day extension kin); aging/prescription clocks on ledgers.

### C9 — Sales & intermediary contracts
**Covers:** mercantile-sale scope + farm/artisan carve-out (1013); price determination + arras-to-price (1014); signed pedido binds buyer (1015); delivery defaults (1020); **defect/warranty clocks: apparent-on-examination waiver, packaged 8d, hidden 15d-from-discovery + 1y-from-delivery; functioning-warranty 30d-denounce/6m-action/3y-default-period (1019-1021)**; sample/gusto/perfection rules (1022-1024); resolution-on-installments + registry for identifiable goods (1025-1026); documents-over-goods + D/a D/P (1027-1029); **CSF/CIF/CAF, CF, LAB/FOB in-code clauses with risk-pass points (1030-1035)**; venta a plazos de bienes muebles (reserved domain, registry, 10-day intimate resolution, 3-month prescription, colones-remnant threshold) (1038-1050); estimatorio/consignment ownership-invariant (1051); permuta (1052-1054); suministro (periodic/continued, min-max, exclusivity both ways, 3-month denounce) (1055-1065); comisión (own-name/foreign-account, 8-day silence-acceptance, **no credit without authorization — else cash-demandable**, named-buyer reporting, retention + commission-withholding) (1066-1082); mandato mercantil (account+name, silence-ratification) (1083-1097).
- **Governing EVIDs:** EVID-227 (EV07).
- **LB:** 07_ Arts. 1013-1097.
- **Crossref:** e-invoicing FEX INCOTERMs (01/03); warehouse/consignment locations; SOQ-29 colones remnants.

### C10 — AML compliance (Ley D. 498 + Reglamento D. 2-2000)
**Covers:** sujetos obligados = 20 categories incl. **ANY mercantile society (Art. 2.20)** + professionals >$10k; unsupervised exempt ONLY from Oficialía (Art. 2 tail); UIF under FGR (3); threshold reporting **cash >$10,000 per client same-day or rolling-month (window = 30 continuous days back from last transaction, 17_ Art. 3 mechanics) / other financial media >$25,000; deadline 5 días hábiles from operation; insurers indemnizations too** (15_ Art. 9); suspicion reports amount-irrelevant, ≤15(+15)días-hábiles analysis then 5 días hábiles, attempts included, terrorism nexus (9-A); due diligence + **PEP enhanced identification** (9-B); KYC obligations: identify + on-whose-behalf; **retention 5y operation docs (from operation end) / 5y client ID+account+correspondence (from relation end) / ≥15y transaction registers (reconstructable)**; nominative-only, no anonymous/fictitious accounts (11-12); **8-field transaction capture incl. employee code + hour (13)**; Oficialía de Cumplimiento requirements + independence (14); electronic records/transmission valid (15-A); safe harbor (26-A) + tip-off crimes (26-B); no-tip-off rule (17_ Art. 4j); compliance-liaison 15-días-hábiles designation/change notice (17_ Art. 4g); **red-flag catalogs = configurable detection menu (structuring, velocity, activity-consistency, KYC-refusal, pattern-shift — case-creation, never auto-report)** (17_ Arts. 12-18); border $10k declaration context (4-8-A, 19-22).
- **Governing EVIDs:** EVID-228 · EVID-229 · EVID-230 · EVID-231 (EV15) · EVID-232 · EVID-233 · EVID-234 · EVID-235 (EV17).
- **LB:** 15_ Arts. 2-15-A, 19-26-B (current, post-reform (6)) · 17_ Arts. 3 (window mechanics only), 4, 11-19 (methodology only — R26).
- **Crossref:** C2 retention matrix (SOQ-28); payroll user/role kin; fiscal-reporting días-hábiles engine.

---

## Section B — Resolved contradictions ledger

| # | Contradiction | Resolution (current authority) | Authority cite |
|---|---|---|---|
| R1 | FE IVA-inclusive prices vs CCFE ventaGravada "(con inclusión de IVA)" wording + worked example showing IVA added | **FE = IVA-inclusive; CCFE = NET + IVA added.** Manual's CCF wording is a copy-paste defect from FE structure. Legal root: CCF must state IVA separate from price; factura = IVA included in price | EV40:EVID-018/023 (+arbitration note); EV01:EVID-048 (Ley IVA Art. 57; CT Art. 114 via EV05:EVID-060) |
| R2 | NCE in contingency: 18_ Cuadro 1 (no) vs 18_ Anexo IV (yes) vs CAT-023 v1.2 (7 types) | **NCE (05) ALLOWED.** Contingency types = 01, 03, 04, 05, 06, 07, 11, 14 + Evento retorno (18); CLE/DCLE/CDE excluded everywhere. All four 45_ Anexo lists unanimous | DG45 §3.3 (Anexo II N°8/9, Anexo IV N°6-9, Anexo III Secc.4, Anexo V N°35); supersedes EV18:EVID-071, EV41:EVID-043, EV25:EVID-046 |
| R3 | FE receptor name threshold: $200 (2022 manual) vs SMM-indexed (D.L. 487) | **≥ 3 SALARIOS MÍNIMOS MENSUALES** (per 119-G VII); Anexos say only "monto legalmente establecido"; $200 = 2022-era history | EV44:EVID-083 (119-G); EV44 supersession map; history EV40:EVID-017; DG45 §1.5 (N°38/39/42) |
| R4 | Contingency trigger/retry: 5s (41_) vs 8s (22_) | **8s timeout → status query → resend, max 2 retries → contingency**; policy kept in 46_ v2.0 | EV18:EVID-079; EV44:EVID-085; history EV41:EVID-041 |
| R5 | CAT-023: 7 contingency DTE types (v1.2) vs 2026 restructure | **CAT-023 = "Operaciones Especiales"** (02 FVS, 97 Comprobantes de Control Interno); contingency-eligible types now governed by Normativa Anexos, not a catalog | EV44:EVID-086; DG45 §3.3; obsolete EV25:EVID-046 |
| R6 | Invalidation taxonomy/deadlines: CAT-024 1/2/3 + 41_ table (1d/3mo) vs 18_ Cuadro 2 business-effect types | **Differentiated deadlines (45_ Anexo V):** CCFE/CRE/NCE/NDE 1 day; CLE/DCLE 10 háb. of following month; NRE/CDE/Evento retorno/Evento OpEsp 4 calendar days; FE/FEXE/FSEE 3 months. CAT-024 kept (renamed "Motivo del evento", values 1/2/3); semantics per 18_ Cuadro 2 + 119-E | DG45 §3.2 N°9, N°43-48; EV18:EVID-075; EV44:EVID-083/086; history EV41:EVID-038/039 |
| R7 | Version numbers per type: Anexo II field 1 vs Anexo IV field 1 (FEXE 2 vs 3); 2022-era versions | **Anexo IV authoritative:** FE 2, CRE 2, CLE 2, DCLE 2, FSEE 2, CDE 2, FEXE 3, CCFE 4, NRE 4, NCE 4, NDE 4; events: invalidación 3, contingencia **4** (erratum fixed 2026-08-17: schema const 4, see contingencia-schema-v4.json; original digest said 3), retorno 1, eop 1. Confirmed by 52_ schemas | DG45 §1.0 + §2 header (+§5 warning 3); EV44:EVID-087 |
| R8 | numeroControl 3rd section: numeric-only transition vs alphanumeric examples | **Alphanumeric, structured:** pos 1-4 = M/B/S/P + 3 digits; pos 5-8 = P + 3 digits; emitter-assigned; year-reset + uniqueness; NO AT correlative authorization for DTEs (115-A lifted) | EV18:EVID-070; DG45 §3.1 N°5 + §4; EV44:EVID-083 (119-G); history EV40:EVID-005/016/027 |
| R9 | Contingency event detail cap: 5000 (41_ prose) / 500 [?] vs v2.0 | **1000 items per event** (>1000 ⇒ new event); types may mix; one codigoGeneración per item | DG45 §2.1 N°34 + §2.2 + §3.2 N°34-36; history EV41:EVID-042/044 |
| R10 | Item caps 2000/500 (verify-flagged in supersession map) | **Confirmed: cuerpo max 2000; CRE y CLE 500;** related docs max 50/2000; otrosDocumentos 1-10 (FEXE 1-20); apéndice 1-10. DCLE cap not restated in v2.0 (single-record cuerpo) [?] → MOQ-12 | DG45 §1.5 + §3.1 N°74; EV18:EVID-078 |
| R11 | Retry-policy source: 41_ cites missing "Guía de Integración Tecnológica" | **= 22_ Manual Tecnológico §3.3** (the 8s/2-retry policy) | EV18:EVID-076 + OQ-4 (resolved); EV18:EVID-079 |
| R12 | Tiquetes registradora / electronic Factura Simplificada | **Tiquetes banned for DTE emitters since 01-Jan-2025; no electronic simplificada type.** FVS survives as PHYSICAL doc for authorized DTE emitters, reported monthly via Evento de Operaciones Especiales (10 primeros días hábiles); pre-Normativa Art.-115 systems cannot coexist; FVS + Art.-113 systems can (iff EOP transmitted) | EV18:EVID-082 OQ-5 + EVID-077; EV44:EVID-084; CT 107/115 (EV05:EVID-060) |
| R13 | NC/ND applicability: hint "only CCF" | **NC adjusts CCF + CR (03/07); ND adjusts CCF/NC/ND/CR (03/05/06/07);** NCE/NDE relating CCF/CR allowed ≤3 months; after invalidation-window expiry CCF and CR adjustable via NC/ND (Ley IVA 62-63 windows) | EV40:EVID-029/030; EV05:EVID-060 (CT 110); EV44:EVID-083 (119-E); DG45 §3.1 N°14-17 |
| R14 | CT copy lacked Arts. 119-A..119-H/239-A/206 (DTE legal base missing) | **Obtained & read: D.L. 487-2022 (44_)** — full DTE regime incl. events power, sello effects, sanctions 239-A a)-j) | EV18:EVID-069 (gap) → EV44:EVID-083 (resolution) |
| R15 | Token validity: fixed 24h prod / 48h test (22_) | **Configurable in AT platform; guidance = authenticate once per 24h** (softening, not conflict — design for configurable) | EV18:EVID-079 → EV44:EVID-085 |
| R16 | Transmission-vs-fecEmi windows: 22_ holgura (docs accepted 1 day after fecEmi; period-end +30 min) vs 45_ Anexo IV N°10 (fecEmi up to 5 days AFTER transmission, not crossing next period) | **45_ v2.0 governs where they overlap** [? — possibly different axes: forward-dating vs late-transmission grace]; confirm 22_-grace status in 46_ v2.0 → MOQ-07 | DG45 §3.1 N°10 vs EV18:EVID-079 [?] |
| R17 | Reglamento ISR provenance: 54_ tail lists "REGLAMENTO: D.E. 101, 21-XII-1992 + reforms 8/39-1993" vs 04_ self-documenting a D.E. 117-2001 repeal map (54_-file OQ-4) | **Same instrument chain; no conflict.** 04_ = D.E. 101-1992 consolidated, printing its own REFORMAS block (p.20): (1) D.E. 8-1993, (2) D.E. 39-1993, (3) D.E. 117-2001 — the mass-repeal reform. The 54_ tail listing is editorially partial (omits the 2001 reform). Cite 04_ for Reglamento LBs; repeal authority = D.E. 117-2001 (NOT the CT) | EV04:EVID-128 (REFORMAS block verbatim); EV54:EVID-167 (tail listing) |
| R18 | Foreign-source income: W6 EVID-094 foreign-securities/deposit paragraphs (10% regime, top-up, gross-up) vs current consolidated text | **Foreign tracks DEAD per D.L. 969-2024 (effective 2024-03-22):** Art. 3.4 excludes ALL foreign-source values from the renta concept; derogated: Art. 14-A incisos 6º-8º, Art. 16 4º c)/5º/7º (in part), Art. 27 2º-4º; Art. 28 pro-rata carve-out for mixed subjects. Domestic 10% tracks (Art. 27 1º, Art. 16 4º a)-b)) survive. EVID-092's anti-exemption gross-up equally dead for foreign rents | EV56:EVID-168 (Art. 2 full scope + vigencia); EV54:EVID-164; dead text: EV03:EVID-094 |
| R19 | Retention tables: 10_ (D.E. 75/25-1992, colones-era, gross base unstated) vs 53_ (D.E. 10-2025) | **53_ OPERATIVE** (repeals D.E. 95-2015; effective 2025-05-08 per MH dating): monthly/quincenal/semanal + June/December recálculo; base = NET (bruto − remuneraciones no gravadas − cotizaciones laborales SS y previsionales); Tramo II does NOT embed the $1,600. 10_ = historical dated data only (its OQ-4 base question is resolved for the CURRENT regime by 53_ literal d)) | EV53:EVID-153..158; history EV10:EVID-148..152 |
| R20 | Art. 37 brackets: 03_ transcription (exempt $4,064.00; Tramo II $4,064.01–$9,142.86 s/ $4,064.00 + $212.12) vs D.L. 293-2025 | **TWO dated vintages (D7/D12):** (a) 957-2011 config — vigencia ≤ 2025-05-07; (b) 293-2025 config — exempt $6,600.00; Tramo II $6,600.01–$9,142.86, 10% s/ $6,600.00 + $212.12; Tramos III/IV + all cuotas unchanged; effective 2025-05-08. Non-resident 30% inciso unchanged | EV54:EVID-163 (55_ Art. 1 verbatim + 54_ p.38 stamps (1)(19)(25)); superseded rows: EV03:EVID-095 |
| R21 | Pago mínimo (Arts. 76-81, 1%/0.6% gross minimum) | **VOID — never implement.** Sentencia 18-2012 (D.O. 216 T.401, 19-XI-2013) struck the unitary regulation; sent. 98-2014 struck Art. 77 again + connected; D.L. 762-2014 (attempted re-enactment) void per sent. 96-2014. No successor regime appears in the 54_ reform tail through Jan-2026 | EV03:EVID-105; EV54:EVID-162 |
| R22 | Aguinaldo retention: CT Art. 155 inc.2 "aguinaldo exempt from ISR retention" (EVID-063) vs Ley Art. 4.16 (2-SMM floor; excess retained, floor DEDUCTED since D.L. 458-2019) | **Ley 4.16 governs** (lex specialis, later in time): exemption up to 2 SMM comercio y servicios; excess = retention base after deducting the floor. CT 155-II read as within the floor. Vintage rows: 2014-2018 full-exemption transitories; 2021 $1,100; 2022-2024 $1,500 caps; 2025+ standing 2-SMM rule (SOQ-05 re-verifies) | EV54:EVID-165/167; EV05:EVID-063; EV53:EVID-159 xref |
| R23 | Pensioner health cotización: 08_ Art. 29 "6% de su pensión" vs 09_ Art. 154 "7.80% de su pensión mensual" (S4/W9 find) | **7.80% governs** — D.L. 614 (2022) is later in time and specifically regulates the pensioner health cotización (also extends coverage to cónyuge/conviviente). 08_'s 6% = historical text; no reform needed (08_ Art. 29 only covers active-worker splits as operative) | EV09:EVID-199 (Art. 154 verbatim); historical EV08:EVID-193 |
| R24 | 09_ registry title ("Ley del Sistema de Ahorro para Pensiones") vs content (Ley INTEGRAL del Sistema de Pensiones, D.L. 614, effective 2022-12-29, which DEROGATES D.L. 927-1996 the SAP) | **Content governs; title is a misnomer** (registry row amended 2026-08-18). Any SAP-era rate lore (e.g. 6.25%/6.75% splits) is DEAD for current periods — only D.L. 614 Art. 16's 16% (7.25/8.75) may be cited; SAP-era Normas Técnicas survive only where not contrary (09_ Art. 159) | EV09:EVID-197/200 (Arts. 16, 162, 164) |
| R25 | 15_ registry title ("Ley contra el Lavado de Activos y del Financiamiento al Terrorismo") vs document content | **Content governs: Ley Contra el Lavado de Dinero y de Activos, D. 498 (2-dic-1998, D.O. 240 T.341 23-dic-1998), consolidated through reform (6) D.L. 104-2015** — no "Financiamiento al Terrorismo" in the title; registry row amended (2026-08-18, W10). Third title-vs-content incident after 29_/09_ — standing lesson reconfirmed | EV15: header + REFORMAS block (EVID-228 context) |
| R26 | AML reglamento thresholds: 17_ Art. 3 "Quinientos Mil Colones" + 3 días hábiles vs 15_ Art. 9 (post-reform (2) D.L. 568-2013) "$10,000 efectivo / $25,000 otros medios" + 5 días hábiles | **15_ governs thresholds and clocks** (later-in-time restatement of Art. 9); 17_ (D. 2-2000) predates ALL six law reforms and is stale there — but its **window mechanics survive as the only corpus definition of the Art. 9 "término de un mes" (30 continuous days counted back from the last transaction, early-report once the multiple-operation total crosses the threshold)**, plus no-tip-off (Art. 4j), liaison notice (4g) and the red-flag catalogs (12-18). Post-reform reglamento acquisition queued (SOQ-27) | EV15:EVID-229 (Art. 9/9-A verbatim); EV17:EVID-232 (Art. 3 verbatim + supersession note) |

---

## Section C — Open questions inventory (remaining open)

| MOQ | Question | Blocking for | Record answer in |
|---|---|---|---|
| MOQ-01 | CAT-019 actividad-económica canonical source/URL (source link broken; count 775→? post-v1.1) | A9 | Catalog sidecar `_INDEX.md` + A9 FRs (origin: EV40 OQ-2/EVID-004; EV44:EVID-086 note) |
| MOQ-03 | Ley IVA Art. 28 exclusion thresholds in colones — current administered status (non-blocking; FSEE regime documented regardless) | A10 (minor) | Taxation synthesis footnote (origin: EV01 OQ-1) |
| MOQ-04 | FOVIAL/COTRANS legal basis not in sources (laws absent; only guide 31_); are they in IVA base (Art. 51.d tension)? FEXE usage requires AT authorization (DG45 §3.1 N°96) | A10 | Taxation synthesis; obtain FOVIAL/COTRANS laws (origin: EV01 OQ-2) |
| MOQ-05 | Retorno/EOP endpoint paths — absent from 46_ v2.0 (25-May) AND from Anexos (deferred to Manuales); check 52_ schemas for hints or later manual revision | A2, A5 | Connector spec (origin: EV44 OQ-1; DG45 §4 confirms absence). **Schema pass 2026-08-17: all 15 files in 52_ scanned — zero endpoint strings; absence schema-verified; externally blocked on AT** |
| MOQ-06 | FVS: does Odoo need an FVS print flow (SMM-threshold users) or is FE always used? Business decision | A5, A11 | S1 decision log (origin: EV44 OQ-3) |
| MOQ-07 | 45_ v2.0 main body §10 not verified (digest covers Anexos only): 24h same-code rejection fix + late-transmission grace (R16) | A8, A2 | State-machine FRs; re-read 45_ §10 + 46_ §transmission |
| MOQ-10 | CRE structure is IVA-retention-only; how are ISR retentions reported electronically? (reteRenta now FSEE-only N°147) | A10 | Retention FRs; CAT-006 + CT 154-160 review (EV40:EVID-027 doubt) |
| MOQ-11 | CDE async seal "24-72h after transmission" (2022) — still true in v2.0? | A1, A8 (minor) | State-machine / CDE FRs (EV40:EVID-035) |

### S2 open questions (ISR wave)

| SOQ | Question | Blocking for | Record answer in |
|---|---|---|---|
| ~~SOQ-01~~ | Capital-gain method: Reglamento Art. 17 media-tasa/1.0%-fallback (rate anchors stale: "Art. 41" pre-tier era) vs Ley Art. 42 flat 10% >12mo. — **RESOLVED** (S2 synthesis 2026-08-17): Ley Art. 42 flat 10% governs current periods and classes (54_ pp.39-40, stamp (14) = D.L. 496-2004); Art. 17 media-tasa = historical pre-2004 method. Verdict in `taxation/03_isr-rates-gains.md` §7 OQ-001 (FR-082 on Art. 42) | T4 capital-gain FRs | done — 03 §7 OQ-001 resolved |
| SOQ-02 | $1,600 (Art. 29.7) proration for quincenal/semanal Tramo II calculations (53_ literal e) mandates inclusion, gives no factor; /12 implied by recálculo shifts) + ordering vs literal d) SS netting. Define for Odoo; check MH guidance | T5 | taxation withholding FR + OQ row (origin: EV53 OQ-4) |
| ~~SOQ-03~~ | D.E. 10-2025 fidelity + provenance: pin the publishing D.O. issue (vigencia 8 días tras publicación → 2025-05-08 assumed) and verify printed-digit anomalies (June table 5,371.44 / 12,228.60 / cuota 106.20; semanal 509.53; quincenal 1,019.06). Path: fetch Apr/May-2025 D.O. volume via the `/api/v1/diarios-disponibles` recipe (PSM 6) — **RESOLVED** (2026-08-18, EVID-171 / source 60_): D.E. 10 published **D.O. N° 79 T.447 30-abr-2025** pp. 25-32 (same issue as D.L. 293/55_) → effective **2025-05-08** confirmed; ALL anomaly digits confirmed in the gazette print (not certified-copy artifacts); December table exact-consistent as contrast. CSV [sic] fidelity rows stand | T5 table-data FRs | done — 04 §7 OQ-002 + 01 §7 OQ-005 resolved; 53_-file OQ-1/OQ-3 closed |
| ~~SOQ-04~~ | General NOL (pérdida fiscal) carryforward: absent from the Ley (only capital losses 5y, Art. 14/14-A); confirm no CT/Reglamento rule adds one (targeted "pérdida fiscal" scan of 05_/04_ txt) before any NOL FR — **RESOLVED** (S2 synthesis 2026-08-17): scans of 05_/04_ negative (document/sanction senses only); NO general NOL — only capital losses per Arts. 14/14-A. Verdict in `taxation/03_isr-rates-gains.md` §7 OQ-002 (FR-086 states it) | T4 | done — 03 §7 OQ-002 resolved |
| SOQ-05 | 2025/2026 aguinaldo transitory: 54_ tail lists none after D.L. 159-2024 ($1,500) → assume standing 2-SMM rule for 2025+; payroll wave re-verifies at encoding time | T5 | payroll wave (origin: EV53 OQ-5) |
| SOQ-06 | Reglamento survivors vs CT: D.E. 117-2001 predates the CT (D.L. 230-2000? both 2000-2001 era) — whether any additional 04_ survivor articles were later repealed by CT Art. 344 ff. Non-blocking; cite survivors as printed | T1/T3/T4/T7 | taxation OQ row (origin: EV04 OQ-1) |
| SOQ-07 | Deposit interest: Art. 27 10% (CT 159 definitive) vs Art. 4.5 exemption for natural persons < $25,000 avg monthly balance. Working harmonized reading: 4.5 carves out small depositors; 27/159 apply above. Non-blocking; synthesis records as FR note | T4/T5 | taxation FR note (origin: EV03 OQ-6) |
| SOQ-08 | F-07/F-14 due-day scheduling (W8): the 2026 calendar's due-day windows are a visual (highlighted-cell) layer; the by-NIT-digit day-assignment rule has no normative anchor in the corpus. Working assumption: deadline windows = dated configuration data, unpinned values; extract the visual layer or find the schedule instrument before deadline FRs get AC-grade dates | F12 | fiscal-reporting deadline FRs (origin: EV34 OQ-1 / EV35 OQ-5 / EV30 OQ-1) |
| ~~SOQ-09~~ | F-14 v17 Quincena-25 annex representation (W8): v17 form adds casillas 417/418 but NO v17 manual/plantilla existed; the Ley Especial Quincena Veinticinco itself was not in the corpus. — **RESOLVED** (2026-08-18, W11 acquisition 66_-70_ via transparenciafiscal): law acquired as 66_ (D.L. 499, D.O. N° 8 T.450 14-ene-2026); annex representation = 7-column semicolon-delimited CSV per 69_ §1-2 + 70_ header (APELLIDOS 100 uppercase no-commas; NIT 14 XOR DUI 9 no separators; FECHA dd/mm/aaaa; SALARIO 4+2 no-thousands; QUINCENA 3+2; PERIODO mmaaaa); upload January-only, independent of the retention annex; code 73 auto-assigned at presentation (EVID-238/239). Annex-level FRs UNBLOCKED — fold at next fiscal-reporting edit | F10 | done — evidence `66-70_Quincena25.evidence.md`; FR fold-ins queued |
| SOQ-10 | F-07 §XIX defects (W8): anulados annex col J says código de generación "36 caracteres" (32 everywhere else) and col A's cutover instruction ("septiembre hacia atrás código de generación; octubre 2022 en adelante número de control") INVERTS the Nov-2022 rule used in annexes 1-12. **Ruling applied (S3):** manual transcription defects — annexes-1-12 convention operative; record as LB note, never encode the inverted cutover | F6 | fiscal-reporting LB note (origin: EV34 OQ-2) |
| SOQ-11 | SS caps as dated data (W8): F-14 annex caps printed Oct-2025 (AFP $472.93, ISSS $30.00 $-caps; INPEP 7.5% / IPSFA 9.5% / CEFAFA 5% / Bienestar Magisterial 5.58% / ISSS-IVM 7.5% %-maxima) — cap feed/cadence + ceiling bases belong to the payroll wave (16_/08_/09_); the F-14 side mirrors them as validation parameters | F8 | payroll wave (origin: EV35 OQ-3) |
| SOQ-12 | Annex-modification resolutions missing (W8): the DGII resolution(s) modifying F-07/F-14 annexes (29_'s intended content; the legal authority behind v14/v16/v17 annex sets incl. Quincena-25) are not in the corpus — manuals/forms are the only authority. Non-blocking (manuals carry full structures); acquire opportunistically | F2/F10 | sources registry (origin: EV29 OQ-1) |
| SOQ-13 | F-935 "donantes locales" entero track: normative anchor unstated in the form (CT 156 zone or a specific regime?) — chase in the CT matrix during S3 | F11 | fiscal-reporting OQ row (origin: EV61-64 OQ-3) |
| SOQ-14 | F-950 frequency/applicability (quarterly pattern Ene/Abr/Jul(+Oct?); whose obligation) — confirm for the reporting inventory | F12 | fiscal-reporting OQ row (origin: EV30 OQ-2) |
| SOQ-15 | ISSS **Reglamento de Aplicación absent** (W9): it alone fixes the high-income exclusion threshold (08_ Art. 3), the cotizable-base CAP behind the F-14 ISSS $30 print, remittance/planilla mechanics (08_ Art. 33), variable-income bases (08_ Art. 34). Acquisition candidate (≥66); until then caps = F-14 print dated data | P6, P7 | payroll FR + OQ row (origin: EV08 OQ-1/OQ-2) |
| SOQ-16 | SIP **IBC ceiling instrument absent** (W9): no base cap in D.L. 614; F-14 v16 print caps AFP $472.93 — instrument (BCR Norma Técnica?) unacquired; value enters as dated data with OQ | P6 | payroll FR + OQ row (origin: EV09 OQ-1) |
| SOQ-17 | SIP **Reglamento + Normas Técnicas + Institutos Previsionales laws absent** (W9): planilla-única spec, acreditación windows; INPEP/IPSFA/CEFAFA/Bienestar-Magisterial/ISSS-IVM rate laws (public-sector employers) — F-14 print is the only anchor | P6, P7 | payroll OQ row (origin: EV09 OQ-2/OQ-3) |
| SOQ-18 | **SMM sector selection** (W9): aguinaldo floor pinned to "comercio y servicios" (Ley 4.16); FE-receptor ≥3×SMM (e-invoicing 01 OQ-007) and the 25-SMM cash ban (taxation/02 OQ-002) name no sector — config decision + MH guidance hunt | P2, P5 | payroll + taxation OQ rows (origin: EV16 OQ-2) |
| SOQ-19 | **Asueto dual-layer** (W9): CT Art. 190 static list vs Calendario-2026 legend extras (2-Jan, Día del Padre, 5-6-Aug pattern, fin-de-año) — extra days are decree instruments absent from corpus; design = CT base + calendar dated-data overlay; visual-layer kin of SOQ-08 | P3 | payroll FR note + OQ row (origin: EV11 OQ-1) |
| SOQ-20 | SMM 2025 **three-decimal prints** (daily/hourly tariffs): both PSM reads agree; transcribe exact-as-printed ([sic] discipline, D.E. 10-2025 precedent); gazette re-verification optional when D.O. recovers | P2 | payroll CSV fidelity note (origin: EV16 OQ-1) |
| SOQ-21 | CT copy vintage: Índice Legislativo edition, stamps through (22), no as-of date — cross-checks consistent with post-2017 consolidation; re-verify stamped articles if a later CT reform lands | P1-P8 | payroll LB note (origin: EV11 OQ-3; non-blocking) |

### S5 open questions (commercial-legal wave)

| SOQ | Question | Blocking for | Record answer in |
|---|---|---|---|
| SOQ-22 | **07_ consolidation cutoff mid-2008** (reform (29) D.L. 641): post-2008 CC reforms unverified — before S5 synthesis trusts any article, check the Asamblea reform list (kin of 03_/54_ resolution); articles reformed by (29) carry USD wording, unreformed colones phrasing = textual remnant | C1-C9 trust | S5 prep acquisition/verification (origin: EV07 OQ-1) |
| SOQ-23 | **SAS law absent**: Sociedad por Acciones Simplificada exists (if at all) under separate legislation — company-type menu incomplete; acquire the SAS law (numbering ≥66) and record side-by-side vs S.A./SRL | C4 | sources registry + C4 FR note (origin: EV07 OQ-2) |
| SOQ-24 | **Quiebra block vintage** (Arts. 498-552, classic 1970 regime): verify whether modern insolvency/concursos legislation derogated it before citing beyond terminology | C5 (minor) | S5 OQ row (origin: EV07 OQ-3) |
| SOQ-25 | **Ley de Registro de Comercio + Reglamento absent** (referenced 415/420/456 for matrícula renewal epochs, fees, sanctions, registry operations) | C1 | acquisition candidate ≥66 (origin: EV07 OQ-4) |
| SOQ-26 | **Interés legal mercantil rate instrument** (Art. 960: fixed periodically by Economía) — dated config outside corpus; never hardcode | C8 | S5 FR config + OQ row (origin: EV07 OQ-6) |
| SOQ-27 | **Current AML reglamento + UIF forms absent**: 17_ = 2000 pre-reform instrument (R26); the post-D.L.-568-2013 reglamento and UIF/FGR report formularios are not in corpus | C10 | acquisition candidate ≥66 + external-interface assumption (origin: EV17 OQ-1/OQ-2; EV15 OQ-1/OQ-2) |
| SOQ-28 | **Retention matrix reconciliation** (synthesis deliverable): CC 10y books + issued/received facturas-anexas + 5y post-liquidation (07_ 451/454) vs AML 5y docs / 15y transaction registers (15_ 10-B/12) vs any DTE-specific retention in 45_/46_ — write the longest-per-object matrix in the S5 file; SaaS archive tiers (D3) must satisfy it | C2, C10, e-invoicing archive | S5 FR + OQ row |
| SOQ-29 | Colones-era remnants in unreformed CC articles ("moneda nacional" 31; "un mil colones" 1038; ¢5,000 cooperative cap 19-II) — operative currency USD; cite as historical text, flag each value-level use (10_ discipline) | C4, C9 | S5 LB notes (origin: EV07 OQ-7) |

### Struck (resolved during evidence passes — retained for audit)

- ~~40_ OQ-1~~ numeroControl alphanumeric — RESOLVED (EV18:EVID-070; DG45 §3.1 N°5) → R8.
- ~~40_ OQ-3~~ NC/ND only-for-CCF — RESOLVED (EV40:EVID-029/030; EV05:EVID-060; EV44:EVID-083) → R13.
- ~~40_ OQ-4~~ invalidation deadlines 1d/3mo — RESOLVED then superseded (EV41:EVID-038 → DG45 §3.2 N°43-48) → R6.
- ~~41_ OQ-1~~ retry-policy source missing — RESOLVED (22_ §3.3; EV18 OQ-4) → R11.
- ~~41_ OQ-2~~ contingency 6 vs 7 types — RESOLVED (DG45 §3.3: 8 + evento 18) → R2.
- ~~41_ OQ-3 (part)~~ — remains as MOQ-02.
- ~~01_ OQ-3~~ CCFE net vs gross — RESOLVED (EV01:EVID-048, Ley IVA Art. 57) → R1.
- ~~05_ OQ-1~~ C100,000 ≈ $11,428.57 conversion — RESOLVED as consistent; threshold unchanged by D.L. 487 (EV40:EVID-025; EV44 supersession map).
- ~~05_ OQ-2~~ electronic simplificada — RESOLVED (EV18 OQ-5; EV44:EVID-084 FVS+EOP) → R12.
- ~~05_ OQ-3~~ AT correlative ranges for electronic — RESOLVED (EV18:EVID-070 emitter-assigned; EV44:EVID-083 119-G lifts 115-A) → R8.
- ~~18_ OQ-1 (blocking)~~ updated CT 119-A..H — RESOLVED (44_ D.L. 487, EV44:EVID-083) → R14.
- ~~18_ OQ-2~~ NCE contingency — RESOLVED (DG45 §3.3) → R2.
- ~~18_ OQ-3~~ CAT-024 "3 Otro" survives? — RESOLVED (EV44:EVID-086: renamed "Motivo del evento", same 1/2/3) → R6.
- ~~44-52 OQ-2~~ 45_ Anexos not fully read — RESOLVED by DG45 digest (residual garbled-keys work = MOQ-08).
- ~~supersession-map verifies~~ item caps (→ DG45 §1.5, R10), invalidation deadlines (→ DG45 §3.2, R6), contingency list (→ DG45 §3.3, R2) — all verified.
- ~~MOQ-02~~ motivoContingencia length — RESOLVED (2026-08-17 schema pass): `motivo.motivoContingencia` and DTE `motivoContin` both maxLength **500** in 52_ schemas; written into 03_events FR-109.
- ~~MOQ-08~~ OCR-garbled keys — RESOLVED (2026-08-17 schema pass, all items): N°84 = `codTributo` ("Tributo sujeto a cálculo de IVA"); N°7 = `tipoOperacion`; CRE N°103 = `montoSujetoGrav`; event N°31 = `emisor.tipoItemExpor` (eret); event N°92 = `resumen.totalCompraExcluidos` (eret); DCLE cuerpo = single object (periodoLiquidacionFechaInicio/Fin, codLiquidacion, cantidadDoc, valorOperaciones, montoSinPercepcion, montoSujetoPercepcion, ivaPercibido, comision, porcentComision, ivaComision, liquidoApagar…); Cuadro 10 = JWS / CAdES label / PKCS8EncodedKeySpec / **RS512** (example header base64-decodes `{"alg":"RS512"}`; printed "RSA512" = regulator typo; 18_ twin row confirms CAdES); event apéndice scope = **Retorno + OpEsp only** (invalidación/contingencia schemas carry no apendice); NCE/NDE tributos = CAT-015 §1+3 per Anexo IV N°96 (T1/D8 nonexistent in v1.1; FE-only 20/C3 exclusion) → 01 OQ-002/003, 03 OQ-005, 04 OQ-002 resolved.
- ~~MOQ-09~~ subTotal sign — RESOLVED (2026-08-17): Anexo IV N°139 raw = "Sumatoria de operaciones" − global discounts (FE/CCFE/NRE; FSEE variant "Total de operaciones" − descuento global). Subtraction uniform; 2022 CCFE "+" = copy-paste defect → 01 OQ-004.
- ~~MOQ-12~~ DCLE item cap — RESOLVED (2026-08-17): fe-dcl-v2 `cuerpoDocumento` is a single object, no array caps → 01 OQ-005.

---

## Coverage totals

- S1 clusters: 12 (A1-A12). Governing EVID totals per cluster: A1=5, A2=4, A3=3, A4=3, A5=3, A6=4, A7=2, A8=3, A9=2, A10=13, A11=8, A12=4 (+6 D-items). DG45 digest governs structure/validation in A1-A8, A10.
- S2/ISR clusters: 8 (T1-T8), from 63 EVID entries (EVID-088..108, 128..146, 148..170; 109-127 reserved-unused) across 6 evidence files + CT crossrefs (EVID-062/063/065 + Art. 62 raw read).
- S3/fiscal-reporting clusters: 12 (F1-F12), from 19 EVID entries (EVID-172..190) across 5 evidence files (EV29/EV30/EV34/EV35/EV61-64); forms are primary authority for declaration mechanics (34_/35_ manuals + 38_/39_/59_ forms + 61_-64_ informs).
- S3/fiscal-reporting delivered: 8 files + index + CSV sidecar (SV-FREP-FR-001..208) — see `sv/requirements/fiscal-reporting/00_index.md`.
- S4/payroll clusters: 10 (P1-P10), from 20 EVID entries (EVID-191..210) across 5 evidence files (EV16/EV08/EV09/EV11/EV65); P10 (Quincena-25) BLOCKED on the D.L. 499 acquisition (D.O. route down 2026-08-18).
- S4/payroll delivered: 8 files + index + 2 CSV sidecars (SV-PAY-FR-001..137) — see `sv/requirements/payroll/00_index.md`.
- S5/commercial-legal clusters: 10 (C1-C10), from 25 EVID entries (EVID-211..235) across 3 evidence files (EV07/EV15/EV17); built W10 2026-08-18; synthesis pending (SOQ-22 verification + SOQ-23/25/27 acquisitions first).
- W11/Quincena-25 package (2026-08-18): 66_-70_ acquired via transparenciafiscal (user-supplied search; D.O. /seleccion still 500); EVID-236..239 in `66-70_Quincena25.evidence.md`; P10 UNBLOCKED, SOQ-09 RESOLVED; F-11 v19/v20 prints discovered (acquisition candidates ≥71); 5 file-level OQs (2 resolved in-file: delimiter `;`, casilla 724).
- Resolved contradictions: 26 (R1-R16 S1, R16 flagged [?]; R17-R22 ISR/S2; R23-R24 payroll/S4; R25-R26 commercial-legal/W10).
- Open questions: S1 = 8 (MOQ-01/03/04/05/06/07/10/11; 19 struck/resolved incl. the 2026-08-17 schema pass); S2 = 7 opened, 4 open (SOQ-02/05/06/07), 3 resolved (SOQ-01/04 in-wave via 03 §7; SOQ-03 2026-08-18 via EVID-171/60_); S3 = 7 opened (SOQ-08..14), 2 resolved (SOQ-09 W11; SOQ-10 carries an applied ruling); S4 = 7 opened (SOQ-15..21); S5 = 8 opened (SOQ-22..29); EV53 OQ-1/OQ-3, EV54 OQ-1/OQ-3 and EV56 set already resolved.
- Evidence corpus indexed: EVID-001..240 (S1 = 001..087 across 7 evidence files + DG45 + ARCH; S2 = ISR files 088..170; S3 = 172..190 + 171 = D.E. 10 gazette verification; S4/payroll = 191..210; S5/commercial-legal = 211..235; W11/Quincena-25 = 236..239).
