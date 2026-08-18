# Evidence — W5 DTE stack (18_, 22_, 19_, 26_, 27_, 06_)

Sources: `18_Normativa_Cumplimiento_DTE.pdf` (OCR; **v1.2, 17-NOV-2025 — newest source**), `22_Manual_Tecnologico` (2022-era), `19_Manual_Funcional` (**v1.2, 09-OCT-2025**), `26_Consola`, `27_Certificado`, `06_Guia` (v8.0 09/2021).
Read: 2026-08-16 (W5). 18_ main body + targeted anexos; 22_ full; others targeted.
**Authority order established: 18_ Normativa (Nov 2025) > 19_ Funcional (Oct 2025) > 40_/41_/22_/25_ manuals (2022).**

---

## EVID-069 CRITICAL — CT Arts. 119-A..119-H missing from our CT copy

- **Loc:** 18_ cites CT 119-A (normative power, definitions a-i), 119-C (emission modalities), 119-D (sello effects), 119-E (invalidation), 119-F (contingency), 119-G (structures), 119-H (gratuidad/web system); also 239-A (new sanction article), 206 incisos.
- **Finding:** our `05_Codigo_Tributario.pdf` Art. 119 = sujetos-excluidos data; NO 119-A+ articles → our CT copy predates the DTE reform (likely a 2022+ reform; DTE sistema legal base).
- **ACTION:** obtain updated Código Tributario (or the reform decree) — required LB for e-invoicing requirements. Recorded as source gap in plan.
- **Topics:** e-invoicing (process)

## EVID-070 18_ Normativa — operative definitions & generation rules

- **Loc:** §3-7 (pp.7-12). DTE def (seal = UUID v4 + alphanumeric suffix; Art. 206 CT effect). **Archivo DTE** = plain JSON + signature + seal (what must be delivered to receptor). Documento Electrónico Apócrifo (post-seal alteration → criminal). numeroControl: 4 sections, **3rd = branch(4)+POS(4) alphanumerics, 4th = 1..9999999999999909(15), resets each fiscal year or on exhaustion** — assigned AUTOMATICALLY by emitter system (resolves W4 OQ-3: no AT range assignment for electronic; AT validates uniqueness/year). Redondeo 8-dec body / 2-dec resumen (9th/3rd ≥5 up); **holgura ±0.01 computed from ITEM decimals, not internal system decimals** (resumen must derive from rounded item values — an Odoo computation-order requirement).
- **Topics:** e-invoicing

## EVID-071 18_ — transmission modalities & platforms (Cuadro 1)

- **Loc:** §6, 9, 9.1 (pp.10-14). Regla general: transmit BEFORE delivery (uno-a-uno or lote). Contingencia = diferida: generate→sign→deliver→(restore)→event→batch≤72h del sello del evento. **Cuadro 1 contingency types: "CCFE, FE, FEXE, NRE, NDE y FSEE" — 6 types, NCE(05) ABSENT** (vs CAT-023 v1.2 = 7 incl. NC; vs 18_ Anexo IV field-7 validation listing NCE as allowed contingency type — **internal contradiction in 18_ itself**). Two platforms: Sistema de Transmisión (API) / Sistema de Facturación (MH free web app, Art. 119-H; its users may use preprinted docs during contingency + are exempt from physical-destruction rule).
- **Topics:** e-invoicing
- **Doubt:** NCE-in-contingency: Cuadro 1 says no, Anexo IV says yes. CAT-023 update needed from MH; until then treat NCE-contingency as PROHIBITED (Cuadro 1 stricter + newer than CAT-023 v1.2).

## EVID-072 18_ — sello rules, states, correction windows

- **Loc:** §10-10.2 (pp.14-16). Sello prerequisites (5 rules: structure/format/signature/deadlines/validations per Anexos IV-V). **Rejected docs: correct within 24h of rejection notice, retransmit with SAME codigoGeneración; after the window → NEW codigoGeneración** (supersedes 41_'s implied flow). States: Transmitido (sub: Ajustado — adjusted by later doc; Observado — AT observations not affecting validity), Rechazado (presumed income per CT 199; no deductions), Invalidado (no tax validity; readable version void). Books: record by GENERATION date w/ codigoGeneración incl. untransmitted; declare in generation period. Deductions require seal (119-D + 206). Seal ≠ operation validation (119-D inc.3).
- **Candidate CRs:** state machine (transmitted/observed/adjusted/rejected/invalidated); same-code retry then new-code; generation-date bookkeeping.
- **Topics:** e-invoicing

## EVID-073 18_ — entrega & representación gráfica

- **Loc:** §11-11.3 (pp.16-17). Delivery = **Archivo DTE + versión interpretada legible (Representación Gráfica)**, electronic, both modalities; contingency docs without seal must show CAT-004 code 2. **Receiver OBLIGED to demand DTE with seal** (119-C inc.6). RG: no probative value, generated simultaneously, delivered per operation, **QR mandatory** (params per 22_: `https://admin.factura.gob.sv/consultaPublica?ambiente=&codGen=&fechaEmi=`). Versión Legible A/B/C/D categories binding. Fedatario not obliged to demand.
- **Topics:** e-invoicing

## EVID-074 18_ — conservation & physical-document destruction

- **Loc:** §12-12.1 (p.18). Electronic conservation per CT 147 (10y), exact structure/format preserved, incl. untransmitted. **Physical documents replaced by DTE must be presented to AT for anulación/destrucción + correlative ranges reported. NO coexistence**: no physical docs while emitting DTE (exception: Sistema de Facturación users). "Documentos impresos" includes PDF-emission systems lacking the official data structure.
- **Candidate CR:** migration flow: destroy authorized physical stock on DTE adoption.
- **Topics:** e-invoicing

## EVID-075 18_ — NEW invalidation taxonomy (Cuadro 2)

- **Loc:** §13.1.1 (p.19). Replaces/refines CAT-024 usage:
  | # | Base legal | Doc types | Case | Deadline |
  |---|---|---|---|---|
  | 1 | 119-E inc.1 lit.a | ALL | **Errores that don't affect the underlying operation** (data-entry: date, name, description) | 1 day |
  | 2 | 119-A inc.1 lit.g | CCFE, NRE, NCE, NDE, CLE, CRE, DCLE, FSEE, CDE | **Total rescission** (e.g., goods return) | 1 day |
  | 3 | 119-E inc.2 | **FE & FEXE only** | Rescission **or operation-affecting adjustments** (price reduction, product change) | 3 months |
- **Gloss:** the FE/FEX 3-month window is for rescission/adjustment; ALL OTHER docs 1-day. Type semantics now tied to the business effect (error vs rescission vs adjustment), not "1/2/3 otros". Supersedes 41_ §2.3's simpler table (which matched it partially) — 41_ lacks the error/rescission/adjustment distinction for non-FE docs.
- **Topics:** e-invoicing

## EVID-076 18_ — contingency effects & web-system fallback

- **Loc:** §13.1.2-13.4 (pp.19-22). Retry policy exhaustion pre-condition (per 22_ Manual Tecnológico — resolves 41_'s dangling "Guía de Integración" reference: it's 22_ §3.3). Declarations reflect contingency ops only once sealed; sanctions 239-A a)/d) for untransmitted. **Sistema de Facturación users: may use pre-authorized physical docs during contingency** (transmission-platform users may not).
- **Topics:** e-invoicing

## EVID-077 18_ — coexistence, implementation program, change-management

- **Loc:** §15-19 (pp.22-24). **Tiquetes (doc equivalents) banned from 01-JAN-2025 for DTE emitters → FE mandatory for consumer ops** (resolves CT-Art.-115-ticket question: registradora tickets dead for DTE emitters). Implementation program: AT sets groups/dates; emitter must implement ALL doc types it's authorized for across ALL establishments; may adopt early. Report-liberation dates per 119-A lit.i. **Normativa change deadlines (Cuadro 4): structural "Versiones" → 10 primeros días hábiles of the 3rd month after communication; minor "Modificaciones" → 10 primeros días hábiles of the next month; non-structural → immediate.** No seal for non-compliant-after-deadline docs.
- **Candidate CRs:** tiquete→FE migration; normativa version-adaptation SLA (module maintenance requirement).
- **Topics:** e-invoicing

## EVID-078 18_ Anexos — structure deltas vs 40_ manual

- **Loc:** Anexo II pass + change log (pp.2, 49-50, 84-85). **FEXE new Sección 7 "COMPRA POR CUENTA DE TERCEROS"** (fields 72 numDoc / 73 nombre, ≤20 / ≤250 chars — purchase-by-third-party, distinct from ventaTercero). Item limits confirmed: body max 2000 (most) / **500 for CRE, DCL, CL** (2024 modification of campo 21). Invalidación event structure = 50 fields (matches 41_ §2.5 v2 numbering + sello note). Anexo IV validations: numeroControl resets 01-Jan, unique within year; modelo diferido (field 6 list incl. **NCE**) only with transmission type 2; UUID uppercase-only validated. Anexo IV/V are the machine-checkable validation rules (per-field, per-DTE) — full detail for Takumi ACs.
- **Topics:** e-invoicing

## EVID-079 22_ Manual Tecnológico — firmador & APIs

- **Loc:** §2-5 (pp.5-32). Firmador options: Java Spring Boot source / Docker (SSL & non-SSL) / Windows service; local only. Sign endpoint `http://localhost:8113/firmardocumento/` POST {nit, activo, passwordPri, dteJson} → JWS RS512 body (status/body). **Auth: POST /seguridad/auth (test: apitest.dtes.mh.gob.sv)** form-urlencoded user+pwd → Bearer JWT + roles; **token 24h prod / 48h test** (run once daily or per model); error codes 100-111. **Recepción uno-a-uno: POST /fesv/recepciondte** (ambiente, idEnvio, version, tipoDte, documento=signed, codigoGeneracion) → estado PROCESADO/RECHAZADO + selloRecibido + clasificaMsg/codigoMsg + **observaciones[]** (non-blocking field warnings, e.g. calc observations — 'RECIBIDO CON OBSERVACIONES' codigoMsg 002). **Lote: POST /fesv/recepcionlote** (idEnvio UUID-v4 uppercase, nitEmisor, documentos[≤100]) → codigoLote; **consulta lote GET /fesv/recepcion/consultadtelote/{codigoLote}** → per-DTE results; **consulta DTE POST /fesv/recepcion/consultadte** (nitEmisor, tdte, codigoGeneracion). **Eventos: POST /fesv/contingencia, POST /fesv/anulardte**. QR URL (EVID-073). Retry policy: **8s timeout** → status query → resend, **max 2 retries** → contingency (41_ says 5s — 22_ is the technological authority; conflict logged). Holgura de transmisión: docs accepted 1 day after fecEmi EXCEPT period-end: +30 min only. Batch windows: test 300 lots 08:00-17:00; prod 400 lots 22:00-05:00 (cyclic invoicing); contingency batches 24/7.
- **Candidate CRs:** full Odoo connector spec (endpoints, auth caching, retry, states, obs handling).
- **Topics:** e-invoicing

## EVID-080 27_ Certificado — acreditamiento flow

- **Loc:** pp.5-10. Acreditamiento required once per environment (test AND prod — credentials personalized per env). Test credentials valid **2 months** (Sistema de Transmisión) / **15 days** (Sistema de Facturación) to complete minimum tests. Login via https://info.dtes.mh.gob.sv/ with NIT + DGII services password → Sitio Emisores DTE. Steps: info verification (RUC data) → certificate generation → API user management.
- **Topics:** e-invoicing

## EVID-081 26_ Consola — Sitio Emisores DTE overview

- **Loc:** TOC + pp.6-9. Consola sections: Inicio (onboarding state), Detalle de Emisor (authorized doc types), Certificado, Sistema de Facturación, **Solicitar Autorización** (test→prod), Consultas, **Gestión de Usuario API** (credential creation/password). Minimum-tests table per doc type (starred = mandatory before requesting additional types).
- **Topics:** e-invoicing

## EVID-082 19_ Funcional v1.2 (Oct-2025) + 06_ Guía — scope notes

- **Loc:** TOCs + section reads. 19_: 11 DTE structure section descriptions (matches 40_ + 18_ Anexo II), event sections, CAT-024 3-option list still shown (1 error / 2 rescind / 3 otro) — **older taxonomy coexists with 18_ Cuadro 2**; authority: 18_. 06_ (v8.0 2021): oldest overview — reception model, signer responsibility, contingency momios (5s-era), firmador install. Both retained as LB for concepts superseded by 18_/19_ where dated.
- **Topics:** e-invoicing

## Open questions from this pass

1. **OQ (blocking):** Updated Código Tributario with Arts. 119-A..119-H + 239-A + 206 incisos — REQUIRED source (EVID-069). Retrieve reform (likely D.L. circa 2022-2023, "Ley de Facturación Electrónica"/CT reform).
2. **OQ:** NCE in contingency: 18_ Cuadro 1 (no) vs 18_ Anexo IV (yes) vs CAT-023 v1.2 (yes). Need CAT-023 current version / MH clarification. Default: prohibited.
3. **OQ:** CAT-024 vs 18_ Cuadro 2 taxonomy mapping (does CAT-024 still have "3 Otro"? 19_ shows it; 18_ redefines semantics) — check catalogs v1.3+.
4. **OQ (resolved):** retry policy = 22_ §3.3 (8s/2 retries) not "Guía de Integración" (dangling ref in 41_ explained).
5. **OQ (resolved):** W4 OQ-2 (simplificada electrónica): 18_ §15 — tiquetes banned for DTE emitters since 01-Jan-2025; Factura Simplificada (≤$12 CT Art. 107 inc.4) physical regime continues for non-DTE emitters only. No electronic simplificada type.

## Topic tag summary

e-invoicing: EVID-069..082
