# SV — Special regimes (zonas francas / aduanas / servicios internacionales / FOVIAL-COTRANS) wave-prep index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | pre-wave (no requirement files yet) |
| Authors | Controller (wave-prep stub) |
| Updated | 2026-08-18 |

This is a **wave-prep anchor stub, explicitly NOT a requirements file**:
it carries no FRs, no LBs and no ACs of its own. It exists to hold the
input inventory and the cross-wave discoveries that the future
special-regimes synthesis wave will consume, so they are not lost
between waves. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Input inventory (per HANDOVER §8.5b)

Acquired sources earmarked for the wave (all currently `pending-S2+`
in [../COVERAGE.md](../COVERAGE.md)):

- [12_Ley_Zonas_Francas.pdf](../../sources/12_Ley_Zonas_Francas.pdf) — Ley de Zonas Francas y Recintos Comerciales (ZF; already kin-cited by `../fiscal-reporting/02_f07-annexes-sales.md` for the Anexo 2 export ZF tasa-0 bucket and `03` for the ZF/DPA tipo-11 purchases).
- [13_Ley_Organica_Aduanas.pdf](../../sources/13_Ley_Organica_Aduanas.pdf) — Ley Orgánica de Aduanas (customs/export regime; DUCA kin).
- [14_Ley_Servicios_Internacionales.pdf](../../sources/14_Ley_Servicios_Internacionales.pdf) — Ley de Servicios Internacionales (LSI).
- [17b_Reglamento_Servicios_Internacionales.pdf](../../sources/17b_Reglamento_Servicios_Internacionales.pdf) — its Reglamento.
- [42_Comunicado_Exportaciones_Panama.docx](../../sources/42_Comunicado_Exportaciones_Panama.docx) — exports comunicado (Panamá).
- [43_DUCA_Instructivo_COMIECO.pdf](../../sources/43_DUCA_Instructivo_COMIECO.pdf) — DUCA instructivo (COMIECO).
- [31_Guia_FOVIAL_COTRANS.pdf](../../sources/31_Guia_FOVIAL_COTRANS.pdf) — FOVIAL/COTRANS guide (the only corpus anchor for the casilla-525 credit pointers left open by `../fiscal-reporting/01_f07-declaration.md` OQ-003 and `05` OQ-003; the underlying laws are absent — MOQ-04).
- **D.L. 598-2020** (Ley Especial y Transitoria sobre la Modalidad de Pago del ISR aplicable a pequeños contribuyentes, turismo, energía eléctrica, servicios de TV/internet/telefonía) + the **EVID-167 tail laws** (D.L. 95-2024 inmobiliarios en altura; 201-2025 Aeropuerto Internacional del Pacífico; 308-2025 Ley de Agentes Extranjeros; 386-2025 biogás Acelhuate; 411-2025 energía eléctrica universal access) — special-payment/incentive regimes named in the 54_ related-laws tail; **acquisition candidates**, not yet in corpus (see `sv/.extractions/54_Ley_ISR_consolidada_DO79_T447.evidence.md` EVID-167).

## W11 discoveries feeding the wave (by-id pointers)

- **ZF/DPA/LSI Certificado de Crédito Tributario** — D.L. 499 (Quincena-25) Art. 6: FY-2026 private-sector voluntary payers under special regimes (ZF/DPA/LSI) take the 100% ISR credit as a negotiable Certificado de Crédito Tributario, auto-generated at the FY-2026 filing. This wave is the **consumer of `../taxation/01_isr-framework.md` SV-TAX-FR-174** (route `certificado_zf_dpa_lsi` — cited by id, never restated); evidence `sv/.extractions/66-70_Quincena25.evidence.md` (EVID-237).
- **F-11 v20 "Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial" + Certificado de Crédito Tributario anexo** — per 67_ (Guía de Orientación Quincena-25) Anexo 8: a dedicated F-11 version v20 exists for special-regime subjects, carrying the certificado anexo. Print not yet acquired (numbering ≥71 watch; `../taxation/01_isr-framework.md` OQ-007; kin `../payroll/08_isr-interfaces.md` OQ-004).
