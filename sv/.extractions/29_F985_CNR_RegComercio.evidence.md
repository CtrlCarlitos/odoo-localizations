# Evidence — 29_ (MISLABELED FILE: actual content = F985/F-975 CNR Registro de Comercio upload manual)

Source: `sv/sources/29_Modificacion_Anexos_F07_F14.pdf` — **WRONG-LABEL INCIDENT (tuky import)**: registry title says "Modificación de Anexos F07/F14" but the file's actual content is the **F985 V1 CNR (Centro Nacional de Registro) Registro de Comercio upload manual** (10 pp). The real annex-modification resolution for F-07/F-14 is NOT in the corpus (see OQ-1).
Read: 2026-08-18 (W8).
Citation form: page of the file (file pagination = printed page).

## EVID-172 CNR Registro de Comercio semi-annual report (F985 v1) — wrong-document record + CT 121 evidence

- **Loc:** whole file; header p.1, structure pp.1-2, load procedure pp.3-10.
- **Verbatim:** p.1: "Manual de Usuario para Carga de Archivos en Informe Centro Nacional de Registro, Registro de Comercio F985 V1 ... en base al Art. 121 literal a, numeral 2 del Código Tributario, el Centro Nacional de Registro cumpla con la obligación de informar de forma semestral el detalle de Sociedades y Comerciantes cuya constitución, transformación, fusión, disolución, o liquidación, se haya registrado, durante el semestre período informado." Structure: 9 CSV columns (A NIT/DUI 9-14; B name 100; C calidad 1=Representante Legal 2=Socio/Accionista; D NIT rep/socios 14; E name; F tipo de trámite 1 CONSTITUCIÓN 2 TRANSFORMACIÓN 3 FUSIÓN 4 DISOLUCIÓN 5 LIQUIDACIÓN 6 MATRÍCULA DE EMPRESA Y ESTABLECIMIENTO; G fecha constitución dd/mm/aaaa; H fecha inscripción/matrícula; I semestre MMYYYY-style 022022). CSV semicolon-delimited, text cells, no headers.
- **Gloss:** this is the CNR's OWN third-party information filing (CT Art. 121 a)2 — the registry reporting society events to DGII), not a taxpayer obligation: OUT OF SCOPE for the Odoo thin client / fiscal-reporting FRs. Value: (1) documents the CT 121 third-party report regime mechanics (CSV upload via MH portal "Declaraciones e Informes en Línea", F985 icon, semi-annual, confirmation checkbox + PRESENTAR); (2) the MH 2026 calendar (30_) names this same duty "Informe Semestral sobre la Constitución, Transformación, Fusión, Disolución o Liquidación de Sociedades (F-975)" while the manual titles itself F985 — MH's own numbering is inconsistent (OQ-3 in the F-14 evidence file).
- **Candidate CRs:** none for fiscal-reporting (third-party report, CNR-side). CT 121 anchor available if the commercial-legal wave needs the registry-information regime.
- **Topics:** fiscal-reporting (registry note only), commercial-legal (pointer).
- **Doubts/xref:** registry row must be retitled; the intended "Modificación de Anexos F07 F14" document remains unacquired (OQ-1).

## Open questions (29_)

- OQ-1: The registry's intended document — the DGII resolution(s) modifying F-07/F-14 annexes (the legal authority behind annex-set versions v13→v14 / v15→v16 / v16→v17, incl. the 2026 Quincena-25 annex change) — is NOT in the corpus; only the upload manuals (34_/35_) exist. Acquire from MH/D.O. if annex-version legal basis is needed (numbering continues from 61).
- OQ-2: (housekeeping) sources/README registry row for 29_ retitled to actual content; retained as CT-121 reference.
