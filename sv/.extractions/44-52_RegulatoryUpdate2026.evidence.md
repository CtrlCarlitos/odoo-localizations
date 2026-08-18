# Evidence — W5.5: 2026 regulatory update (44_, 45_, 46_, 50_/51_, 52_)

Sources: `44_Reforma_CT_DTE_DL487` (D.O. 20-09-2022, OCR pageseg-6), `45_Normativa v2.0` (25-05-2026), `46_Manual Tecnológico v2.0`, `50_/51_Catálogos v1.1` (2026-07), `52_Json Schemas` (2026-08-11).
Read: 2026-08-16 (W5.5). **This wave supersedes parts of W1-W5 evidence; supersession map below.**

---

## EVID-083 D.L. 487-2022 — the complete DTE legal base (CT Arts. 119-A..119-H + reforms)

- **Loc:** 44_ Arts. 1-14 (pp.3-23).
- **Art. 119-A:** AT faculties a-i (rules, tech specs, structures, transmission, RG contents, sello rules, EVENT structures — "podrá establecer los eventos que sean necesarios" — the legal root of the 2026 new events; obligation dates; report-liberation dates) + normativa power (strict compliance, sanctionable).
- **Art. 119-B:** DTE def = generated + signed + transmitted + sealed. **119-C:** emission = generation→signature→transmission→delivery, electronic; receivers OBLIGED to demand (except fedatarios); AT ceases Art. 113/115-A authorizations for obligated taxpayers.
- **Art. 119-D:** transmission rules; seal effects (Art. 206); seal ≠ operation validation; events transmission duty; consultation media.
- **Art. 119-E (invalidation):** errors not affecting the operation → event within AT-set deadline + NEW corrected document (119-G); receiver ID data required in the event for FE/FEXE/FSEE (NIT, passport for foreigners, foreign registry for non-domiciled); CDE → donor ID. **FE/FEX affected-operation adjustments** (not total rescission) also via invalidation+reissue. **After the invalidation window expires, CCF and CR "podrán modificarse o ajustarse... mediante notas de débito o de crédito electrónicas" within Ley IVA Arts. 62-63 deadlines — NC/ND as the post-window adjustment path (NEW vs W5 reading).**
- **Art. 119-F (contingency):** delivery per 119-C; event with detail of untransmitted docs; transmit ALL detailed docs within AT deadline (incl. ones tied to invalidation); compliance exempts from 239-A g)/h).
- **Art. 119-G (per-type requirements):** CCFE = CT 114.a.3,4,6-10 minus sucursales + códigoGeneración + númeroControl + fecha/hora + total + forma de pago. **FE: receiver name+NIT required when total ≥ 3 SALARIOS MÍNIMOS MENSUALES (supersedes the $200 threshold — SMM-indexed now!)**; foreigner: passport; non-domiciled: foreign registry no. FEXE = FE minus I/VII + export tax separation. NRE = 114 subset + NR data. **NC/ND = CCFE requirements minus payment, MUST reference the prior CCF/CR number+date.** CLE = CCFE minus 7/9/VI + related-doc codes + net values + débito of the period. CRE = CT 112 IV subset. DCLE = CT 112 b,d,e,f,g + liquidation dates + responsible delegate. FSEE = CT 119 a,b,c,e,f + FE subset. CDE = códigoGeneración + númeroControl + donatario incl. **número de resolución de calificación de sujeto excluido** + donor ID + amounts/description/values + date/time. **DTEs do NOT need Art. 115-A correlative authorization** (códigoGeneración identifies them; also lifts Ley ISR 29-A.15.c and Ley IVA 65-A inc.3 restrictions for DTEs).
- **Art. 119-H:** free AT solution (Sistema de Facturación).
- **Art. 2 (CT 141 reform):** books — **10 días hábiles** backlog (was 15 calendar); record DTEs by Código de Generación (+ NC/ND/CCF/CR/export facturas individualized); consumer docs: CG initial/final + numeroControl range; **contingency/unsealed DTEs recordable without seal**.
- **Art. 3 (CT 147):** DTE conservation from GENERATION date, emitter's responsibility; AT not a storage service; RGs conserved in original format/medium.
- **Art. 4 (CT 173):** audit access to electronic data + the systems that generate/receive DTEs (own or third-party); IT-expert auditors; confidentiality duty. **Art. 5-8 (CT 175/179/180/181):** fedatarios verify physical factura emission AND electronic RG delivery; acta process; recidivism → cierre (257).
- **Art. 9 (CT 199):** untransmitted DTEs presumed income; RGs delivered without matching DTE → same presumption; apocryphal/fake-cert docs → nonexistent operations.
- **Art. 10 (CT 206):** deductions need DTE + seal; RG deductibility tied to non-invalidated DTE; **evidential hierarchy: AT copy > taxpayer copy > RG**.
- **Art. 11 (CT 239-A):** special DTE sanctions: a) omit emit/deliver or value mismatch **50% per doc (min 2 SMM)**; b) 119-G non-compliance **30% (min 2 SMM)**; c) transmission without structure/format/sello rules **30%**; d) **omit transmission 100% (min 9 SMM)**; e) omit RG delivery 30%; f) non-compliant RG 30%; g) omit event transmission **9 SMM**; h) late event **9 SMM**; i) non-compliant event structure **9 SMM**; j) breach of AT e-document normativa **9 SMM**.
- **Transitorias:** obligation dates per AT program; physical stock: inform + present for destruction within **15 días hábiles** of becoming obligated; Art. 113/115 systems coexistence only where AT allows (superseded/regulated by Normativa §15).
- **Topics:** e-invoicing, taxation

## EVID-084 Normativa v2.0 (May-2026) — new event regime

- **Loc:** 45_ §4, §9 Cuadro 5, §13.3-13.4, §15.
- **FOUR events now:** Invalidación, Contingencia, **Retorno**, **Operaciones Especiales**.
- **Evento de Retorno** (fe-eret): reports return of goods sold/purchased & service diminution/refund. Cases: receiver/third-party returns under FE/FEXE/FSEE docs; hidden-defect service refunds; **envase/empaque deposit recovery; reimportación of exported goods; export value diminution (loss/damage)**. Deadline: **3 months from seal of the related doc**; transmission: normal-previa OR **normal-diferida up to 1 day after generation/delivery** (a NEW differential-transmission mode for events!); contingency-diferida ≤24h event / ≤72h docs after contingency-event seal (Cuadro 5). Effects: FE → sale+débito decrease; FEXE → export + **remanente de crédito fiscal** decrease; FSEE → purchase decrease. **No crédito fiscal generated for the receptor; retorno is NOT a discount; cannot exceed the original; not adjustable by event/doc; doesn't invalidate origin even at 100% value; itself invalidable.**
- **Evento de Operaciones Especiales** (fe-eop): (1) **Factura de Venta Simplificada (FVS) reporting — FVS is ALIVE as a physical regime subject to monthly EOP reporting (10 primeros días hábiles of next month)** — RESOLVES W4/W5 simplificada OQ: not an electronic DTE, but DTE emitters authorized for FVS keep using it + report via EOP; (2) Comprobantes de Control Interno (CT Art. 113 special systems authorized post-Normativa). Coexistence rule: FVS + AT-authorized Art.-113 systems may coexist WITH DTE emission iff EOP transmitted; pre-Normativa Art.-115 systems may NOT (tiquetes dead since 01-Jan-2025, §15 restates).
- **CAT-002 v1.1 includes codes 17 (Evento Operaciones Especiales) and 18 (Evento Retorno)** — DTE and event types unified in one catalog.
- **Transmission ordering rule (§9.2):** affecting/adjusting/invalidating docs transmit AFTER the affected; applies uno-a-uno and lote; **a DTE may only be affected by another DTE/event if already transmitted** — an Odoo queue-ordering constraint.
- **Topics:** e-invoicing

## EVID-085 Manual Tecnológico v2.0 deltas

- **Loc:** 46_ (35 pp). Same API surface as 22_ (auth, recepciondte, recepcionlote, consultadte, consultadtelote, contingencia, anulardte — verified identical URLs). **Token validity now "configurable" in the AT platform, guidance = authenticate once per 24h** (softens the fixed 24h/48h rule of 22_). Password policy: 13-25 chars, letters+numbers+special (confirms RQ-era data). (New endpoints for retorno/eop not in the 25-May version read — either in later revision or handled by same event endpoints; schema 52_ (Aug-2026) defines payloads → check schemas for endpoint hints at synthesis.)
- **Topics:** e-invoicing

## EVID-086 Catalogs v1.1 (2026) restructure

- **Loc:** 50_/51_ + regenerated sidecars (33 CSVs).
- **Changes vs v1.2 (2022):** CAT-002 = "Tipo de Documento / Evento" (+17/18). **CAT-008 = DISTRITO (new catalog, ~75 district codes — El Salvador's district-level admin)** — no longer "eliminado". **CAT-013 Municipio RESTRUCTURED to 44-municipio model** (2023 reorganization; codes 13/14/15 = Ahuachapán Norte/Centro/Sur etc.) — RESOLVES the municipal-drift risk. **CAT-023 = Operaciones Especiales (02 FVS, 97 Comprobantes de Control Interno)** — replaced contingency-type list (contingency-eligible DTE types now governed by Normativa text/Anexo IV validations, not a catalog). CAT-024 renamed "Motivo del evento" (same 1/2/3 values). **CAT-033 Tipo de Régimen NEW** (EX-1/EX-2/EX-3/TA-1 customs regimes — FEXE régimen field now uses this?). CAT-021 renamed "Documentos Asociados". CAT-019 actividad: 775→? (verify count in _INDEX). **Old sidecars (v1.2) replaced; supersession noted in _INDEX.md.**
- **Topics:** catalogs, e-invoicing

## EVID-087 JSON Schemas 2026-08-11 — version matrix + new events

- **Loc:** 52_ zip (extracted scratch `schemas_2026/`). Current versions: **fe-f v2, fe-ccf v4, fe-nr v4, fe-nc v4, fe-nd v4, fe-cr v2, fe-cl v2, fe-dcl v2, fe-fex v3, fe-fse v2, fe-cd v2, contingencia v4, invalidacion v3, fe-eop v1, fe-eret v1.** Old `schemas/` (2022: fc v1, ccf v3, nr/nc/nd v3, cr/cl/dcl/fex/fse/cd v1, contingencia v3, anulacion v2) fully superseded — field-level mapping must use v2 matrix. Note: old "anulacion" renamed "invalidacion" in schema files.
- **Topics:** e-invoicing

## Supersession map (W1-W5 → W5.5)

| W-evidence | Status |
|---|---|
| EVID-038 invalidation deadlines (1d/3mo table) | SUPERSEDED by EVID-083 (119-E: AT sets deadlines; Normativa Cuadro 2 in 18_ v1.2 — verify against 45_ v2.0 Cuadro at synthesis) |
| EVID-017 FE $200 receptor-name threshold | **SUPERSEDED: now ≥ 3 SMM (119-G VII)** |
| EVID-043/071 contingency-type list (6-vs-7 NCE) | Verify against 45_ v2.0 Anexo IV; CAT-023 no longer governs it |
| EVID-046 CAT-023=7-types incl FSE | OBSOLETE — CAT-023 is now Operaciones Especiales |
| EVID-025 $11,428.57 responsible parties | Still valid (CT 114 a.2 unchanged by D.L. 487) |
| Retry 8s/2x (EVID-079) | Still valid (46_ v2.0 keeps policy) |
| Item caps 2000/500 (EVID-078) | Verify in 45_ v2.0 Anexo II at synthesis |
| 24h same-code rejection fix (EVID-072) | Verify in 45_ v2.0 §10 at synthesis |

## Open questions

1. **OQ:** Retorno/EOP endpoints in Manual Tecnológico — not found in the 25-May v2.0 read; check whether a later revision or the schemas define service paths before synthesis.
2. **OQ:** 45_ v2.0 Anexos II-IV not fully read (137pp OCR) — full structure/validation re-read is part of S1 synthesis prep (the authoritative per-field tables now live there, replacing 40_ manual as primary).
3. **OQ:** FVS (Factura de Venta Simplificada) — physical doc for DTE emitters + EOP monthly reporting: does Odoo need an FVS print flow or is FE always used? Business decision for synthesis (SMM threshold vs $12 CT rule).

## Topic tag summary

e-invoicing: EVID-083..087 · catalogs: EVID-086 · taxation: EVID-083
