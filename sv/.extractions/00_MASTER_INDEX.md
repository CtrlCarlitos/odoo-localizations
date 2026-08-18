# MASTER EVIDENCE INDEX — El Salvador DTE localization (S1 synthesis lookup)

Built: 2026-08-17. Inputs (read-only, no source PDFs re-read): the eight evidence/digest files + `shared/docs/saas-thin-client-architecture.md`.
**Authority order (binding):** 44_/45_/46_/50_/51_/52_ (2026) > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). Where the supersession map in EV44 marks a W-item SUPERSEDED, the current-authority finding governs; old EVID ids are kept as history.

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

- Clusters: 12 (A1-A12). Governing EVID totals per cluster: A1=5, A2=4, A3=3, A4=3, A5=3, A6=4, A7=2, A8=3, A9=2, A10=13, A11=8, A12=4 (+6 D-items). DG45 digest governs structure/validation in A1-A8, A10.
- Resolved contradictions: 16 (R1-R16; R16 flagged [?]).
- Open questions: 8 (MOQ-01/03/04/05/06/07/10/11); 19 struck/resolved (15 evidence-pass + 4 in the 2026-08-17 schema pass: MOQ-02/08/09/12).
- Evidence corpus indexed: EVID-001..087 across 7 evidence files + DG45 + ARCH.
