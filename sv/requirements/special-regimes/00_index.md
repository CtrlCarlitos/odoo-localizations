# SV — Special regimes (zonas francas / aduanas / servicios internacionales / FOVIAL-COTRANS) wave-prep index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | evidence pass COMPLETE (W13, 2026-08-19); S7 prep DONE (SR1-SR8 clusters + SOQ-30..45 in master index, 2026-08-19) — synthesis IN PROGRESS |
| Authors | Controller (wave-prep stub; W13 evidence; S7 prep) |
| Updated | 2026-08-19 |

**S7 synthesis lookup:** master index
[§S7-A clusters SR1-SR8 + §S7 SOQ register](../../.extractions/00_MASTER_INDEX.md)
(`sv/.extractions/00_MASTER_INDEX.md`); special-regimes authority order in
its header. Planned files: `01_regime-framework.md` (SR1) ·
`02_zf-exemption-schedules.md` (SR2) · `03_lsi-regime.md` (SR3) ·
`04_customs-clocks.md` (SR4) · `05_tan-iva-interface.md` (SR5) ·
`06_customs-declarations.md` (SR6) · `07_obligations-reporting-sanctions.md`
(SR7) · `08_fovial-cotrans.md` (SR8). Prefix: **SV-SPE-FR** (wave-sequential
from 001).

This is a **wave-prep anchor stub, explicitly NOT a requirements file**:
it carries no FRs, no LBs and no ACs of its own. It exists to hold the
input inventory and the cross-wave discoveries that the future
special-regimes synthesis wave will consume, so they are not lost
between waves. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Input inventory (per HANDOVER §8.5b)

Acquired sources earmarked for the wave (all currently `pending-S2+`
in [../COVERAGE.md](../COVERAGE.md)):

- [12_Ley_Zonas_Francas.pdf](../../sources/12_Ley_Zonas_Francas.pdf) — Ley de Zonas Francas Industriales y de Comercialización, D.L. 405 (consolidated through D.L. 318-2013; **READ W13** — EVID-251..258 in `sv/.extractions/12_Ley_Zonas_Francas.evidence.md`; already kin-cited by `../fiscal-reporting/02_f07-annexes-sales.md` for the Anexo 2 export ZF tasa-0 bucket and `03` for the ZF/DPA tipo-11 purchases — its Art. 25 is that 0%-IVA authority).
- [13_Ley_Organica_Aduanas.pdf](../../sources/13_Ley_Organica_Aduanas.pdf) — Ley Orgánica de la DGA, D. 903 (through D.L. 121-2012; **READ W13** — EVID-268: institutional frame; ZF/DPA/parques inside the servicio aduanero).
- [14_Ley_Servicios_Internacionales.pdf](../../sources/14_Ley_Servicios_Internacionales.pdf) — Ley de Servicios Internacionales, D.L. 431 (2007; **READ W13** — EVID-259..264: indefinite ISR exemptions; 1.5%/1% local-service retentions; 24-month admisión temporal).
- [17b_Reglamento_Servicios_Internacionales.pdf](../../sources/17b_Reglamento_Servicios_Internacionales.pdf) — its Reglamento, D. 131 (2008; **READ W13** — EVID-265..267: **Art. 22 local-market caps 50/40/30%**; DGA inventory-report contract; semestral auditor dictamen).
- [42_Comunicado_Exportaciones_Panama.docx](../../sources/42_Comunicado_Exportaciones_Panama.docx) — exports comunicado (Panamá; **READ W13** — EVID-273: DUCA-F SIECA transmission from 03-mar-2025).
- [43_DUCA_Instructivo_COMIECO.pdf](../../sources/43_DUCA_Instructivo_COMIECO.pdf) — DUCA instructivo (COMIECO Res. 409-2018; **READ W13** — EVID-272: 62-field contract; DUCA-F 30 días hábiles).
- [31_Guia_FOVIAL_COTRANS.pdf](../../sources/31_Guia_FOVIAL_COTRANS.pdf) — FOVIAL guide DG-002/2001 (the only corpus anchor for the casilla-525 credit pointers left open by `../fiscal-reporting/01_f07-declaration.md` OQ-003 and `05` OQ-003; **READ W13** — EVID-274: $0.20/galón outside IVA base; **COTRANS not covered — instrument still absent, MOQ-04 half-open**; underlying laws absent).
- [74_Ley_Simplificacion_Aduanera_D529.pdf](../../sources/74_Ley_Simplificacion_Aduanera_D529.pdf) — **ACQUIRED+READ W13** (uif.gob.sv; EVID-269..271 in `sv/.extractions/13_42_43_74_Aduanas.evidence.md`): teledespacho chassis; presumed flete/seguro 1.25/1.50/10% FOB; $18 inspection tasa; 5-year caducidad/records.
- **D.L. 598-2020** (Ley Especial y Transitoria sobre la Modalidad de Pago del ISR aplicable a pequeños contribuyentes, turismo, energía eléctrica, servicios de TV/internet/telefonía) + the **EVID-167 tail laws** (D.L. 95-2024 inmobiliarios en altura; 201-2025 Aeropuerto Internacional del Pacífico; 308-2025 Ley de Agentes Extranjeros; 386-2025 biogás Acelhuate; 411-2025 energía eléctrica universal access) — special-payment/incentive regimes named in the 54_ related-laws tail; **acquisition candidates**, not yet in corpus (see `sv/.extractions/54_Ley_ISR_consolidada_DO79_T447.evidence.md` EVID-167).
- **Cross-cutting acquisition gaps surfaced by W13** (file OQs): Reglamento General Ley ZF (Art. 51); **LESIA** (Ley Especial para Sancionar Infracciones Aduaneras — cited by 12_/74_); DUCA user manual (mandatory fields); Ley Fondo de Conservación Vial D.L. 208-2000 + COTRANS instrument (31_ OQ-1/2); current-consolidation hunts for 12_/13_/14_/17b_/74_ (all end 2012-2013).

## Binding decisions for the synthesis wave

- **D15 as-of doctrine (§5 ruling 42, decided 2026-08-19)** — this wave is its
  canonical consumer: ZF/LSI/DPA exemption schedules are per-beneficiary dated
  rows (acuerdo D.O. date + location track + 60/40 phase-down ladders or
  LSI indefinite-until-cessation rows, never global constants); the $18 tasa /
  presumed flete-seguro / cap percentages / SMM-sanction values are dated
  config rows with instrument provenance.

## W11 discoveries feeding the wave (by-id pointers)

- **ZF/DPA/LSI Certificado de Crédito Tributario** — D.L. 499 (Quincena-25) Art. 6: FY-2026 private-sector voluntary payers under special regimes (ZF/DPA/LSI) take the 100% ISR credit as a negotiable Certificado de Crédito Tributario, auto-generated at the FY-2026 filing. This wave is the **consumer of `../taxation/01_isr-framework.md` SV-TAX-FR-174** (route `certificado_zf_dpa_lsi` — cited by id, never restated); evidence `sv/.extractions/66-70_Quincena25.evidence.md` (EVID-237).
- **F-11 v20 "Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial" + Certificado de Crédito Tributario anexo** — per 67_ (Guía de Orientación Quincena-25) Anexo 8: a dedicated F-11 version v20 exists for special-regime subjects, carrying the certificado anexo. Print not yet acquired (numbering ≥71 watch; `../taxation/01_isr-framework.md` OQ-007; kin `../payroll/08_isr-interfaces.md` OQ-004).
