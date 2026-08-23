# HANDOVER — Honduras Session State & Continuation Guide

**For the next HN controller session.** Written 2026-08-20 after W1 (taxation
core), updated through round-4/D-H2/D-H3 + the merge, W2 fiscal-reporting, W3
facturación, W4 payroll, synthesis prep (master index + OQ registers),
S-HN1..S-HN4 synthesis waves + their merges, the V-HN1 VALIDATION WAVE
(merged to main 2026-08-20, thirteenth §4.6 run at `960df34`, root record
`f2eccbc`), V-HN1b (in-corpus reads 95_/96_/93_/94_/97_ + acquisition wave),
the W5 acquisition-reads wave + W5b D. 59-2023 fetch (nineteenth §4.6 run at
`cd01045`, root record `5c7185b`), the W5c 109_ evidence pass (MERGED
to main 2026-08-20 — twentieth §4.6 run at `9d1aac4`, root record `36df87c`),
the W6 R-H75-chain wave (MERGED — twenty-first §4.6 run at `24391b6`, root
record `8513e49`), the W7 residual-chain decode (MERGED 2026-08-21 —
twenty-fourth §4.6 run at `d4b2a49`, root record `380f044`), the W8
acquisition wave (MERGED 2026-08-21 — twenty-fifth §4.6 run: 2 commits
rewritten (`2012b6a..2006f04`), zero conflicts, remote ref delete +
re-push, root record `1308644`; main carries HN through EVID-481, corpus
128 files), the W9 residual-queue acquisition wave (MERGED 2026-08-21 —
twenty-eighth §4.6 run at `64183e4`, root record `e777566`; main carries HN
through EVID-565, corpus 147 files), the W10 sharpened-residual-queue
closers (MERGED to main 2026-08-21 — twenty-ninth §4.6 run at `9e600db`,
root record `67ba60d`; TWELVE files `149_`..`160_` + EVID-566..643 + rulings
R-H87..R-H90 — the 506-vs-509 instruments COMPLETE [FR-382 still blocked on
the legal reading = owner decision], the TP gate + safe-harbour-NEGATIVE,
the CbCR regime, the OTCD chain complete, the QUINCENCAL CETF informativa,
the REAP domésticos lane, and THE PROMEDIO FAMILY 5-of-6 years [2022-2025
printed/anchored, FY caps unblocked]; COVERAGE 159 rows = 157 cited + 2 N/A,
gates PASS [1099/532/574/331]), the W11 amnistía + negatives wave (MERGED to
main 2026-08-22 — thirty-first §4.6 run at `20d10fd`, root record `4b51c74`;
FIVE files `161_`..`165_` + EVID-644..664; the IHSS amnistía both
generations + the negatives sweep + the W5 lost-file recovery; COVERAGE 164
rows = 162 cited + 2 N/A, gates PASS [1099/535/574/332]), the R-H91 ruling
session (MERGED same-day — thirty-third §4.6 run at `ba98ac7`, root record
`49feee5`; the 506-vs-509 boundary ruled CONSUCOOP-gated, OQ-009 resolved,
no corpus change), and **the W12 GLIN re-grep wave (2026-08-22, on-branch
— TWO files `166_`/`167_` + EVID-665..680: the Código de Comercio = D.
73-1950 ACQUIRED [attribution corrected from "D. 4-1950" — the 12th
lead-attribution fix; Art. 143 = the 541 anchor now instrument-backed] +
the CT D. 189-1959 ORIGINAL print [THE CT promulgation pin: G 16,827-16,834
15→23-jul-1959 → vigencia 15-jul-1959; the original Art. 120 cap = 8 MESES
— the 25/15 caps arrive with D. 150-2008; the 8+3 feriado list = 1959
original, the 1960 pair reformed mechanics only]; corpus 166 files;
COVERAGE 166 rows = 164 cited + 2 N/A, gates PASS [1099/536/574/333])**.
Next = the residual watch queue
(TOP: the 2026 JD ceiling act watch via the Sección-A certificaciones
route — W11 scan + W12 tick both clean through G 37,226/21-ago-2026;
D. 96-2012 watch [gazetted 20-jul-2012 pinned]; CbCR restatement
comunicado watch [negative as of 2026-08-22]; "Acuerdo 799" TEXT + D.
247-89 watch [D. 247-89 now ALSO the payroll/08 OQ-008 cap-window key];
SEE docs; DGS SMM 2027 promedio print early-2027; S-HN5 DEFERRED).
Read this fully before acting; it is the authoritative HN cross-session
memory (conversation context does not survive). Update it at every session
boundary.

**Bootstrap prompt for a fresh session:** `Read hn/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/hn-research`, branch `hn-research`. **Merges to
  date: 2026-08-19 (W1) and 2026-08-20 (W2; W3 at `c1f9fa8`; W4 at `d5a2f4b`;
   **W5+W5b at `cd01045` w/ root record `5c7185b` — nineteenth §4.6 run,
   3 commits rewritten (`51be444..6f37179`→`d9d8317..cd01045`), zero
   conflicts — merged 2026-08-20; main carries HN through EVID-384, the W5
   requirements, and 109_ (D. 59-2023 — evidence pass DONE on-branch as
   W5c, EVID-385..391 — merged same day, twentieth §4.6 run at `9d1aac4`,
   root record `36df87c`)**;
  synthesis prep at `e106b1f`; S-HN1+S-HN2 at `6d1cfc3` w/ root record
  `b98dae1` — ninth §4.6 run; S-HN3 + R-H66 adoption at `00caef9` w/ root
  record `503ab9c` — tenth §4.6 run, zero conflicts, remote ref delete +
  re-push; **S-HN4 at `d05f2c1` w/ root record `7a40433` — eleventh §4.6
  run, 2 commits rewritten (`087e94f`→`3ee60c0`, `9890bda`→`d05f2c1`),
  zero conflicts, remote ref delete + re-push**). Rebase-then-merge per
  root HANDOVER §4.6, owner-executed.
  The cross-country canon D15-D19 was adopted at the W1 merge — HN's
  D-H2/D-H3 are country instantiations of D16/D18 (see
  `shared/docs/regulatory-change-management.md`,
  `shared/docs/go-live-readiness.md`). **Country work model (binding):** every
  country works in its own branch+worktree; `main` = integration; merge at
  milestones by owner decision. NEVER touch `sv/`, `gt/`, or root
  `HANDOVER.md` from this branch; `hn/` + specs are ours.
- **Mission:** bootstrap the Honduras Odoo localization per
  `docs/superpowers/specs/2026-08-18-hn-source-research-design.md`
  (e-invoicing IN scope; acquire+register; evidence waves authorized by the
  phase-extension note in that spec). Procedure:
  `shared/docs/requirements-extraction-procedure.md`.

## 2. Read order for a new session

1. THIS file
2. `hn/EXTRACTION_PLAN.md` — wave log (W1a-W1f taxation + W2a/W2b fiscal
   reporting + W3 facturación + W4 payroll + synthesis prep + **S-HN1/S-HN2/
   S-HN3/S-HN4 synthesis DRAFT-COMPLETE**), reading order, risks,
   **Decisions (D-H1/D-H2/D-H3 binding; D-H2/D-H3 = D16/D18
   instantiations)**
3. **`hn/.extractions/00_MASTER_INDEX.md` — THE synthesis lookup (built
   2026-08-19): authority orders per topic, 18 EV file keys, 43 clusters
   (T1-T12/F1-F11/E1-E8/P1-P12) with Governing EVIDs/LB/crossrefs, R-H1..65
   resolved-contradictions ledger, OQ registers C1-C4 (~227 open), S-wave
   plan. READ BEFORE ANY SYNTHESIS WORK.**
4. **`hn/requirements/taxation/00_index.md` + `hn/requirements/e-invoicing/
    00_index.md` + `hn/requirements/fiscal-reporting/00_index.md` +
    `hn/requirements/payroll/00_index.md` — S-HN1/S-HN2/S-HN3/S-HN4
    deliverable indexes (248 + 155 + 362 + 313 FRs, wave rulings; R-H66
    adopted 2026-08-20). READ BEFORE THE VALIDATION WAVE (COVERAGE.md
    consumes all four; payroll cites taxation/04 plantilla +
    fiscal-reporting/02 código-111 interfaces and owns the SMM-promedio
    rows).**
5. `hn/RESEARCH.md` — research dossier: sites, fetch recipes (§6), hint
   layer w/ corpus verification (§7), open leads (§5, incl. W2+W3+W4
   harvests)
6. `hn/sources/README.md` — registry, **164 files (01-165, 103
   reserved-unused)**, full provenance + mislabel-correction notes (**11
   incidents to date** — the W9 SAR-240-2024 fetch was md5-identical to
   corpus `19_`, discarded unregistered, ledger unchanged; W10: the ihss.hn
   `AJ-RIESGOS-PROFESIONALES` filename caught at page-1 as a juramentación
   memo — discarded unregistered, ledger unchanged; W11: the ihss.hn
   "Reglamento-Incapacidad-para-reformas" upload = a content-identical
   re-render of `88_` [40/40 pages same text, different md5] — discarded
   unregistered, ledger unchanged)
7. Evidence files in `hn/.extractions/*.evidence.md` (committed), W12 newest
   first: `166_Codigo_Comercio_D73-1950.evidence.md` (665..672 — Art. 143 =
   the 541 anchor VERBATIM-verified; Art. 13-VI + D. 158-1954 cooperative
   carve-out; the Apéndice identity + transitory Art. 1º 1940-survival;
   full-file OCR sidecars in `.extractions/` for both) +
   `167_Codigo_Trabajo_D189-1959_original.evidence.md` (673..680 — THE CT
   promulgation pin G 16,827-16,834 → vigencia 15-jul-1959; the original
   Art. 120 cap = 8 MESES; preaviso ladder whole-life; 95.13
   sindicalizados-only; the 8+3 feriado list = 1959 original; Art. 874
   derogation genealogy); W11: `163-165_Amnistia_IHSS_2025-2026.evidence.md` (651..664 — the LIVE
   chain); `161-162_IHSS_amnistia_DL112-2016.evidence.md` (644..650 — the
   2016 pair); **the W5 lost-file recovery:
   `106+107+108_bono-reglamento-pacto-comisiones.evidence.md` RECONSTRUCTED
   at its W5 range 373..384** (the committed file had been an md5-duplicate
   of the 105_ pass since W5 — caught by the W11 corpus-global EVID sweep;
   rebuilt from surviving OCR sidecars + 600dpi re-passes, cross-anchored to
   payroll/02's LB-018 verbatims); W10: `149_Decreto_92-2015_Contribucion_Social.evidence.md` (566..577 — R-H87); `150_DEI-SG-004-2016_TP_umbral.evidence.md` (578..586 — R-H88);
   `151_SAR-653-2023_CbCR.evidence.md` (587..596); `152-154_OTCD_CETF_
   prorroga.evidence.md` (597..611 — R-H89); `155_006-JD-2008_domesticos_
   REAP.evidence.md` (612..621); `156-158_DGS_tablas_SMM_promedio.
   evidence.md` (622..633 — R-H90); `159-160_SAR_descargos_promedio_
   anchors.evidence.md` (634..643 — R-H90); W9: `130_Decreto_278-2013_Ordenamiento.evidence.md` (482..491 — R-H86);
   `131-132_Ordenamiento_reglamento_interp.evidence.md` (492..499);
   `133-134_SAR-236-256-2024.evidence.md` (500..506 — the DMC re-seed);
   `135-139_LSP_contribuciones.evidence.md` (507..523);
   `140-142_TP_precios_transferencia.evidence.md` (524..535);
   `143-144_turismo_SAR-383.evidence.md` (536..543);
   `145_Reglamento_Gral_IHSS_003-JD-2005.evidence.md` (544..553 — the
   base-composition resolver);
   `146-148_IHSS_ancestors_G33879.evidence.md` (554..565); older: `01_`
   (ISR, EVID-001..015), `02_` (ISV, 016..026), `03_` (CT, 027..038),
   `04-21-22_` (D.17-2010 family, 039..053), `07-12+11_` (tables+plantilla,
   054..056), `05+23+79+80_` (taxation closers, 057..071),
   `13-20_fiscal-procedures.evidence.md` (W2a, 072..090),
   `29+30+46-49+68+74+75_ISR-annual.evidence.md` (091..110),
   `31-42+71_retenciones.evidence.md` (111..129),
   `43-45+69+70+72+73_ISV.evidence.md` (136..150),
   `50-55_selectivo.evidence.md` (151..158),
   `56-62_contribuciones.evidence.md` (163..173),
   `63-67_informativas.evidence.md` (175..185),
   `24-26+76-78_facturacion.evidence.md` (W3, 186..214),
   `82-84+90-92+101+102+104_salario-minimo-13-14.evidence.md` (W4a, 215..240),
   `81+87+88_IHSS.evidence.md` (W4b, 250..274),
   `27+28_RAP-fondo.evidence.md` (W4c, 275..289),
    `85+86_codigo-trabajo.evidence.md` (W4d, 295..333),
   `109_Decreto_59-2023_Adulto_Mayor.evidence.md` (W5c, **385..391**);
   `110-113_aguinaldo-chain.evidence.md` (W6, **392..404**);
   `114_Decreto_135-94_Compensacion_Social.evidence.md` (W6, **405..414**);
   `115-118_taxation-ancestors.evidence.md` (W6, **415..428**);
   `119_Congreso_Inventarios_de_Leyes.evidence.md` (W7, **429..433** — the
   official congreso law inventory: the 102_ OQ-2 decoder).
    **EVID numbering is
    corpus-global, next = 681. OQs are per-file/per-doc at evidence-file end.**

## 3. State: corpus (research phase COMPLETE)

**166 registered files, every one page-1 verified (01-167; gap 103
reserved-unused; **166_/167_ acquired 2026-08-22 W12 = the GLIN re-grep wave:
166_ the Código de Comercio D. 73-1950 print [GLIN HN0505195001.PDF —
official consolidated edition post-May-1959, + the 1940-Libro-III Comercio
Marítimo APÉNDICE, truncated at CdC-APX-Art. 1038; Dado 16-feb-1950,
Ejecútese 17-feb-1950, vigor +20d after publication concludes — gazette pin
open; ATTRIBUTION CORRECTED from "D. 4-1950" — 12th lead-attribution fix];
167_ the CT D. 189-1959 ORIGINAL print [GLIN HN1905195901.PDF — complete
with promulgation tail: G 16,827-16,834 of 15→23-jul-1959 → vigencia
15-jul-1959; the genealogical baseline for 86_]**; 161-165 acquired 2026-08-22 W11 = the amnistía wave: 161_
the Reglamento Especial Amnistía/Depuración CI print 11-nov-2016 [ihss.hn
Wayback]; 162_ D.L. 112-2016 G 34,170 [ENAG]; 163_ D.L. 44-2025 G 36,861
[ENAG]; 164_ D.L. 78-2026 G 37,166 [ENAG]; 165_ Res. SOJD-IHSS-016-2026-XIII
certified G 37,189 [ENAG — located by the W11 full-text scan]; 149-160
acquired 2026-08-21 W10 = the sharpened-residual closers: 149_ D. 92-2015 G
33,883 [ENAG]; 150_ Acuerdo DEI-SG-004-2016 G 34,018 [ENAG 49-issue SUMARIO
batch-scan]; 151_ SAR-653-2023 CbCR G 36,489 [SAR catalog]; 152_ D. 7-2017
G 34,284 [SAR catalog]; 153_ SAR-239-2024 CETF informativa [SAR catalog];
154_ SAR-283-2024 prorroga [SAR catalog]; 155_ Acuerdo 006-JD-2008 REAP
domésticos G 31,681 [ihss.hn Wayback]; 156_/157_/158_ the DGS promedio
prints 2022/2023/2024 [trabajo.gob.hn uploads via Wayback CDX]; 159_
SAR-43-2026 G 37,077 [ENAG — the SAR slug login-walls]; 160_ SAR-125-2024
G 36,499 [ENAG]; 130-148
acquired 2026-08-21 W9 = the residual-queue wave:
130_ D. 278-2013 G 33,316; 131_ Acuerdo 462-2014 G 33,484; 132_ D. 74-2014
G 33,617; 133_ SAR-236-2024 G 36,538; 134_ SAR-256-2024 G 36,580; 135_
D. 105-2011 LSP texto actualizado; 136_ Acuerdo 1775-2011; 137_ D.
131-2018; 138_ D. 53-2015; 139_ D. 128-2020; 140_ D. 232-2011 TP; 141_
Acuerdo 027-2015; 142_ D. 62-2019 (G 35,077 — pin corrected); 143_
Acuerdo 618-A-2017; 144_ SAR-383-2024; 145_ Acuerdo 003-JD-2005 Reglamento
General IHSS "última versión"; 146_ the 1971 Reglamento de Aplicación;
147_ the G 30,735 gazette original of 003-JD-2005; 148_ G 33,879 IHSS/RAP
extract; 120-129 acquired 2026-08-21 W8 = the post-W6 queue:**
120_ Ley RAP ORIGINAL G 33,222 [rap.hn Wayback]; 121_ D. 51-2003 LET G 30,059;
122_ Acuerdo 0948-2003 LET-reglamento [gazette 28-jun-2003, No. unpinned];
123_ D. 52-2004 G 30,437; 124_ D. 314-98 G 28,847; 125_ D. 135-2006 G 31,168;
126_ D. 68-2017 G 34,419 [CURRENT turismo statute, derogates 314-98];
127_ Acuerdo 005-2017 G 34,282 [selectivo reglamento, text-native];
128_ D. 99-93 [FX-repatriation]; 129_ D. 74-95 TEXT [G 27,655 May-1995]**; **119_ acquired 2026-08-21 W7 = the official congreso
"Inventarios de Leyes" thematic inventory (text-native; Sub Sección 6.1
Derecho Laboral pp.274-283) — the residual-chain DECODER, EVID-429..433,
R-H81/R-H82; 110-118 acquired 2026-08-20 W6 via the Wayback of the old
official congreso.gob.hn/leyesdehonduras/ library and evidenced EVID-392..428
— the R-H75 chain `110_` D. 179-97 / `111_` D. 178-86 / `112_` D. 2-87 /
`113_` the D. 112-1982 ORIGINAL gazette print G 23,848 / `114_` D. 135-94
(14th origin) / `115_` D. 58-1982 selectivo 203 origin / `116_` D. 131-98
(Art. 43 = the 4% turística/código-259 origin) / `117_` D. 110-93 (Art. 9
intereses = código-115 core) / `118_` D. 54-96 (FIRST Ley Equidad
Tributaria)**); 105-108 acquired 2026-08-20 and W5-evidenced (EVID-362..384)
— **105_ = D. 112-1982 THE aguinaldo law (R-H74, P2 unblocked; recovered via
Wayback of the official STSS upload, correcting the round-5 "routes
exhausted" claim); 106_ = TWO extracts — D. 43-97 (G 28,271 29-may-1997) +
Reglamento STSS-154-2000 bono (gazette 6-nov-2000; 11th title incident,
R-H77); 107_ = D. 150-2008 CT-120 reform + annual pact; 108_ = Acuerdo 345
Comisiones SMM (G 25,680)**; **109_ = D. 59-2023 Adulto Mayor intermediate
reform (G 36,460 14-feb-2024, via ENAG) — EVIDENCED W5c (EVID-385..391,
R-H78/R-H79): "reformar por adición Arts. 3 y 30" — the L30,000 credit
SURVIVES unchanged (tercera list reprinted summarized 1)-14) with gazette
ellipses); cuarta edad = 80+ DEFINED; new cuarta catalogue 1)-13) banked for
S-HN5; edition's other decrees = D. 63-2023 military promotions / D. 5-2024
MUNICIPAL amnistía (expired window, "31-jun" [sic]) / D. 6-2024 migration;
title-completeness noted, NOT a 12th mislabel; a duplicate D. 103 upload was
discarded md5-identical to 104_). Structure:
- **Laws/consolidations:** ISR D.L. 25 (`01_`, hasta SAR-07-2025), ISV
  D.L. 24 (`02_`, hasta D.L. 59-2022), CT D. 170-2016 (`03_`, hasta
  D. 180-2020), D. 17-2010 + Reglamento 1121-2010 + D.28-2019 interp
  (`04_/21_/22_`), Ley Eficiencia D. 113-2011 (`05_`)
- **ISR tables FY2022-2026** (`12/10/09/08/07_`) + **plantilla 2026**
  (`11_` XLSX = the withholding computation contract)
- **Fiscal reporting:** DJIMR SAR-238-2024 (`14_`), DMC chain
  (`15/16/17/20_`), tarjetas mods (`19_`), compras eventuales (`18_`),
  EEFF SAR-619-2024 (`13_`), 42 per-código Ayudas/Generalidades (`29-75_`)
- **Facturación:** Acuerdo 481-2017 consolidado (`24_`) + 189-2014 hist
  (`25_`) + 817-2018 (`26_`) + workflow helps (`76-78_`)
- **Payroll (W4-complete):** IHSS D. 48-2024 (`81_`, rates OCR'd) + Ley
  IHSS (`87_`, OCR'd — native layer junk) + incapacidad (`88_`); RAP fondo
  D. 47-2024 (`27_`) + D. 40-2026 (`28_`); salario mínimo bienios 2023
  (`83/84_`), 2024-2025 (`82_`), **2026-2027 CURRENT (`90_` OCR'd + `91_`
  tabla + `92_` bono + `101_` 2022/2023 vintages + `104_` D.103 machinery +
  `102_` 14th-month reglamento)**; CT D. 189-1959 (`86_`, vintage through
  D.278-2013) + **85_ = D.93-2021 PENAL-side derogations only (9th mislabel
  — NOT CT, no CT gap ever existed)**
- Misc: amnistía D. 7-2026 (`06_`), ISR reforms (`79/80_`), Adulto Mayor
  family (`95/96_`), 22-A chain (`80/93_`), selectivo IPC chain
  (`98/99/100_`), ISR-reglamento ancestor 464-1990 (`94_`), D.194-2002
  original (`97_`). LJT still unapproved (Sep-2025 newest SAR post).

## 4. Key findings (do not re-derive)

- **E-invoicing reality:** NO national XML/DTE regime. Paper regime
  (CAI/rango/vigencia, Arts. 59-61) administered digitally + a statutory
  **Sistema de Emisión Electrónica (SEE) with per-document CAEE** (Arts.
  50-58, gradual mandatory incorporation per SEFIN calendarización) —
  technical docs NOT public (lead 1). D. 17-2010 L-Art 57 = regime's
  statutory birth.
- **Document taxonomy (Arts. 5-8)**: Comprobantes Fiscales (Factura,
  Prevalorada, Ticket, Recibo Honorarios, Boleta Compra, Constancia
  Donación) / Documentos Complementarios (NC, ND, Guías Remisión,
  Comprobantes Retención) / Otros. 16-digit correlativo =
  establecimiento(3, matriz=000)+punto de emisión(3)+tipo doc(2)+consecutive(8,
  wraps 99999999).
- **Withholding:** asalariados = annualize→deduct→table→÷months (plantilla);
  composite L257,493.16 sole-source gate; 12.5% services; 1% compras
  anticipo (retainer >L15M); OTCD cards 10%-of-tax/15% fallback; non-resident
  gross table 25/10 (current = `01_` Art. 5).
- **Rates:** ISR PJ 25%, PN 15/20/25 IPC-indexed annually; 22-A gross-minimum
  (≤L1B excluded, 1%/0.5% sectors); ISV 15%/18%/0; mora 3%/mo cap 36%;
  prescription 4/5/7y; multas = income-range × SMM-promedio fractions +
  ISR-late 5→25%/month escalator.
- **W2 fiscal reporting (do not re-derive):** Form 535 EEFF-prior gate from
  FY2024 (SAR-619-2024); DJIMR = monthly informativa PER retention código
  (25-code catalog), 10 días calendario, rectificativa auto-rectifies the
  determinativa; DMC = form 527, deadline **5 días calendario
  (SAR-237-2024)**; tarjetas 523 (SW informativa) + 215 (OVI determinativa,
  base = 10% of ISV − devolución 8%) file OUTSIDE the DJIMR catalog;
  compras eventuales = doc type 10 buyer-issued (rate unpinned — OQ);
  TP pequeños excluded ≤USD 1M; AS = 5% RNG>L1M (PJ-only), ATN = minimum tax
  over L3M exemption, both D.51-2003 (un-acquired — TOP lead);
  contribuciones: 504 1% / 502 1% / 503 0.5% monthly, 506 3.6% / 509 15%+0.5%
  floor / 511 15% / 107 10% annual; selectivo 203 = separate D.58-1982 tax;
  259 = 4% turística retention.
- **W2 conflicts (open OQs — never resolve silently):** GC non-resident
  retention 2% (46_) vs 4% (05_ Art. 14); ZOLITUR Art. 4 vs Art. 25; DMC
  manuals "8 días" vs gazette 5 (5d = record); 506-vs-509 cooperative
  boundary; 39_ ≡ 37_ (both código 135).
- **W3 facturación (do not re-derive):** D-H1 FR cluster evidence-complete.
  16-digit correlativo grammar + wrap rule; type codes 01/03(Ticket machine
  prefix 09)/04/05/06/07/08/10(Prevalorada)/11/12, **02 unassigned**;
  **code-10 collision: DEI-279-2015 "10 = Compras Eventuales" (introduced
  the 16-digit grammar) vs 481-2017 "10 = Prevalorada" — OQ-2, never
  implement 10 as both**; 189-2014 = 14-digit grammar → dual historical
  parser; CAI ledger contract (Arts. 59-63): per punto × doc type, ONE active
  rango, renewal T-2mo, vigencia ≤1y, consumo starts at Activada; emission
  gate = momento-de-emisión earliest-of (Art. 14) + vigencia/fecha límite;
  two-layer print contract; L50 consolidation (imprenta only); L10,000 ID
  threshold (SEFIN-modifiable, dated row); boleta compra 5%-of-opex +
  per-provider caps, no crédito; NC/ND origin triple; guía 12-motivo + SAR
  copy; retención comprobante at hecho generador (patronos exempt unless
  requested, EVID-200); no-utilizados 12 causes/10 días hábiles; topologies
  centralizado/regional/sucursal; SEE/CAEE = medium of autoimpresor, docs
  unpublished (lead 1); helps' Base-Legal sections defective — cite the
  reglamento.
- **W4 payroll (do not re-derive):** IHSS matrix = **IVM 3.5% employer /
  2.5% worker / 0.5% State (81_ Art. 1) + EM 5%/2.5%/0.5% (87_ Art. 55-A) ⇒
  worker 5.0%, employer 8.5%**; TWO regime ceilings (2024: 11,336.32 IVM /
  11,109.30 EM; 2025: both 11,903.13 — coincidence, not merger); post-2025 =
  JD per actuarial study (dated rows); "porcentajes sobre los techos" =
  drafting ambiguity, coherent reading min(salario, techo) per 55-B;
  **contribution BASE (13th/14th/OT inclusion?) delegated to unacquired
  Reglamento General — config flag, TOP lead**; riesgos profesionales rate
  not in corpus; incapacidad: NO cuarentena — days 1-3 employer salary,
  4-365 IHSS 66% + mandatory employer complement (RIT 71/73). RAP side:
  **STACKED fondo 4% + RAP 1.5% employer (=5.5%) + worker 1.5% retention
  above IVM techo, ≤15 días entero; base "salario ordinario" undefined in
  law (OQ); ceiling 3× top-SMM (instrument unnamed, OQ); fondo coexists-
  with-offset vs CT cesantía (despido injusto: compute, deduct saldo, pay
  excess; other causes: fondo 100% prima + 35%/75% complement floors, CT
  Art. 120 lit. f); vigencia 28-may-2024, no retro**. Ley RAP = doubly
  load-bearing (truncated transcription). SMM: bienio 2026-2027 % 6/6/7/7
  (2026) · 6/6/7/7.5 (2027), full tables pinned; 2027 IPC-escalator
  de-oficio + Jan-Apr-2026 retroactivity; **promedio ONLY in DGS companion
  tables (2026: L14,917.20 → 10×SMM cap L149,172; NOT the table mean — never
  recompute); 2025 (L13,985.16) + 2027 promedios NOT in corpus = OQ +
  DGS-print lead**; 14th month (102_): June, 30-jun year-gate 100%-else-
  proportional, average-of-ordinary-salaries base, small-employer SMM-average
  variant, proportional on exit; bono educativo ≤2×SMM, ≤15-worker
  exemption, non-salary. CT: **NO aguinaldo in the CT — D. 135-94 special
  law (TOP lead; subsumes D. 112)**; vacaciones Arts. 345-356 (10/12/15/20
  días laborables at 1/2/3/4+y; 6-month ordinary average ÷ days worked; no
  360 divisor CT-side); preaviso 24h/1w/2w/1m/2m; cesantía 10d/20d/1mo/yr +
  fraction, cap 25 months (15 for micro ≤10), ≥15y vol-quit 35% / death 75%,
  last-6-month average base; jornada diurna 8h/44h-worked paid-48, nocturna
  6h/36h +25%, OT ×1.25/×1.50/×1.75, ≤12h/day, OT ≤4×/week, planillas book
  OT separately; maternity 4+6w at 180-day average + top-up, nursing
  2×30min, unauthorized firing = 60 days + 10 weeks + 2× rests; **NO general
  final-pay deadline in CT (negative — LB elsewhere)**; extra finds: Art.
  95.12-13+60-A mandatory union/non-union/coop deductions; Art. 104 sickness
  half-pay schedule; 11 paid feriados (8 fixed + 3 Semana Santa, R-H70) ÷6 average + collision rule; Art. 368
  pay-frequency caps; "salario completo" (ord+OT) indemnity base; Libro de
  Salarios (Art. 380). **85_ = 9th mislabel: D.93-2021 derogates PENAL
  (D.130-2017, 31 arts) + CPP + Lavado — ZERO CT articles; penal numbers
  collide with LIVE CT payroll articles — guard table EVID-333.**
- **S-HN1/S-HN2/S-HN3 synthesis (2026-08-20, do not re-derive):** taxation 7
  files (HN-TAX-FR-001..281, 248 FRs/54 OQs) + e-invoicing 4 files
  (HN-EINV-FR-001..175, 155 FRs/26 OQs) + fiscal-reporting 11 files
  (HN-FREP-FR-001..393, 362 FRs/154 LBs/188 ACs/169 OQs +
  `djimr_retention_codes.csv` 25 codes), controller-verified 11/11 + 11/11.
  Rulings made at synthesis: 10-SMM caps = EXCESS-ONLY never cliff (plantilla
  IF semantics, `01_ OQ-4` resolved); FY2026 promedio cap = L149,172.00
  (R-H47 applied); DAR superseded by DJIMR (R-H31 applied); bad-debt cap =
  10%-of-closing-AR (evidence over brief); L30k@60 senior tier attributed to
  D. 199-2006 per plantilla citation — row activation-blocked until acquired.
  **R-H66 (territoriality: worldwide pre-2017 / territorial 2017+,
  dated rows) ADOPTED by product owner 2026-08-20 — encoded in
  taxation/01 FR-004, OQ-001 resolved; rows stay reversible if a contrary
  instrument lands.** S-HN3
  specifics: S-HN1/S-HN2 rates consumed by id throughout; F9 IPC chain
  (98_/99_/100_) = the ONE direct-cite exception (no evidence pass,
  page-1-verified at synthesis, values controller-re-verified vs raw txt —
  cigarettes 539.00/571.34/600.99 chain + per-liter tablas as dated rows);
  only yes-blocking wave OQ = 506-vs-509 boundary (`60_ OQ-1`); open
  conflicts carried (GC 2%-vs-4%, ZOLITUR Art.4-vs-25, 138 duality, 541/542
  drifts, 535 balance-only-vs-+GyP, 509 Mar-30-vs-3-meses, D.117-2021
  identity). New top acquisition LEAD from synthesis: Reglamento Ley ISR
  ("Acuerdo N°799", 5× cited corpus-wide). SEE sub-cluster = config-gapped
  placeholders (e-invoicing/04 FR-166..169), rest of E-wave evidence-complete.
- **S-HN4 payroll synthesis (2026-08-20, do not re-derive):** 10 files +
  `smm_tables.csv` (HN-PAYR-FR-001..398, 313 FRs/146 LBs/163 ACs/73 OQs),
  subagent-dispatched with pre-allocated ranges, controller-verified 10/10
  structural + strict verbatim bank-check (5 one-word LB defects found+fixed:
  correspondientes/se refieren/establecer/recibe/crédritos). P1 OWNS the
  SMM dated rows + DGS promedio rows (R-H47 — the sole feed of taxation/04
  FR-134; print_status discipline: printed/derived_gap/reconstruction_
  blocked, never a derived amount in an amount cell; 2026 promedio
  L14,917.20 + maquila 12,930.07 verified in-CSV). P2 aguinaldo =
  config-gapped placeholders (the wave's ONLY yes-blocking OQ — D. 135-94 +
  Acuerdo 201-96 unacquired). IHSS matrix/ceilings/min-base per R-H49/50/51
  encoded; base composition = config flag (LI Art. 100). RAP stack
  R-H55/56/58 encoded with three-bases-never-share. CT family encoded with
  the R-H57 mislabel guard (EVID-333) in file 10. Evidence-over-brief
  corrections kept: feriado collision = two-holidays-one-day (paid even on
  Sunday); Art. 349 ¶2 proportional leg = employer-imputable-cause only;
  cesantía fraction = Art. 120 lit. c; Art. 104 rule-4 no half-salary
  qualifier; Art. 21-A proportionality sentence ends mid-print.

- **W5 acquisition-reads wave (2026-08-20, do not re-derive):** **R-H74 —
  D. 112-1982 (105_, EVID-362..372) IS the 13th-month statutory home**:
  entitlement = permanents + jubilados/pensionados; gate = 31-dic
  12-continuous-months same-employer else proportional (CT-347 class always
  proportional); December default + pacto (Art. 11); base = ordinary-salary
  average with the SMM-average variant (Art. 12); exit proration ALL classes
  + anticipo netting (Art. 13); vigencia 01-nov-1982 (secondary pin via 89_);
  séptimo día transitory from 10-ene-1983. The W4d "D. 135-94 (Ley del
  Aguinaldo) + Acuerdo 201-96" framing was a CONFLATION/unsourced
  attribution (**R-H75 — voided;** the real chain from 105_'s footnotes:
  D. 178-86 G 25,077 17-nov-1986 [100%-or-proportion + CBII floor + 30-day
  base + obra ÷-days + convention/custom permanents] / D. 2-87 G 25,155
  18-feb-1987 [printed date "30-feb-1987" impossible] / D. 36-90 G 26,131
  11-may-1990 [caña/destajo + incapacidad temporal] / **D. 179-97 G 28,441
  17-dic-1997 — reform content UNKNOWN = new top lead**, rows reversible).
  payroll/02 P2 rewritten (FR-052..054 + FR-088..093; OQ-001 resolved).
  Séptimo día chapter → payroll/06 FR-248/249 (ordinary-jornada valuation,
  OT excluded; fixed-part rule for mixed; destajo zona-SMM floor; four
  deemed-inclusion classes Art. 6; no-full-week-no-right Art. 7; rest-day =
  CT-340 + séptimo additive Art. 8). **R-H76** — 106_ = D. 43-97 (G 28,271,
  29-may-1997, masthead-confirmed; 21-A ≡ 104_ print, R-H43 double-pinned;
  modality loan scoped to PROPORTIONALITY only; SMM Arts. 20/35 gazette
  originals) + Reglamento STSS-154-2000 (5-oct-2000 → gazette 6-nov-2000,
  number illegible ≈29,32x = the title's "29320", **11th title-class
  incident R-H77**): payroll/02 OQ-004 RESOLVED + FR-094..096 (calendar-year
  100% gate 01-01→31-12 same employer; post-exit claim; mid-year-entry
  FORWARD proration; 2×SMM gate EXCLUDES OT/primas/bonificaciones/
  gratificaciones; family allocation — cohabiting→mother, separated→
  custodian, new-family right, orphan guardian, ONE bono per worker).
  107_ D. 150-2008 (EVID-380..382): original ≡ 86_ fn.19 zero drift; R-H58
  anchors upgraded (payroll/08 LB-007/008 + FR-305's three carve-out
  predicates incl. "otro sistema donde el patrono sea aportante" = the
  RAP/fondo bridge; payroll/05); lineage lead D. 247-89 (15-dic-1989).
  108_ Acuerdo 345 (EVID-383/384; 6-oct-1988, G 25,680, own vigencia
  unpinned): payroll/01 LB-022 + FR-041 (commissions TEMPORARY tripartita,
  Director General de Salarios presides; fijación published ONCE + 20-day
  fatal window; **fijación vigencia = +15 days after publication — DEFAULT
  displaced by the fijaciones' own clauses, R-H62 kin**). Payroll totals
  326 FRs/158 LBs/170 ACs/81 OQ rows; COVERAGE 107 rows = 105 cited + 2 N/A.
- **W5c 109_ evidence pass (2026-08-20, do not re-derive):** **R-H78 —
  D. 59-2023 = "Reformar por adición los artículos 3 y 30" of D. 199-2006;
  the L30,000 credit (Art. 30.14) SURVIVES unchanged**: the tercera-edad
  list is reprinted SUMMARIZED 1)-14) with GAZETTE-print ellipses
  (dual-OCR-pass-confirmed — PSM 6 sidecar + independent PSM 4 column pass
  agree on every load-bearing token), numeral 14 carried forward; the
  reprint corpus-confirms the 2007 numbering (credit = 14). FR-067 =
  10-ago-2007 WHOLE-LIFE row, no mid-life cutover; taxation/02 OQ-009(a)
  RESOLVED (LB-017; FR-067 caveats rewritten; 3 stale cells fixed; index
  248/**113**/140/56). Vigencia = publication day → **14-feb-2024**.
  **R-H79 — cuarta edad = "ochenta (80) años o más" DEFINED** (reformed
  Art. 3 glossary) → resolves 96_ OQ-2: the D.45-2025 utility tiers'
  (19-ene-2026) cuarta predicate = 80+; cuarta ⊂ tercera (60+); DNI-alone
  accreditation (D59-Art. 2.2). NEW cuarta-edad discount catalogue 1)-13)
  full text (medicamentos 40%, recreación 60%, salud 30%,
  pasaje/restaurantes/funerarias 35%, consultas 30/35%, lodging 35%
  Mon-Fri/25% Sat-Sun) = S-HN5 commercial-legal bank (parked per deferral).
  Reformed BENEFICIARIOS age-bounds the jubilado leg ("que cumplan con la
  edad" vs 2007 "sin importar su edad" — narrowing-vs-slip readings BOTH
  open, `109_` OQ-1 → OQ-009(b) with a 14-feb-2024 cutover; only the
  <60-jubilado edge is affected — flag-only under the plantilla gate either
  way). Edition's other decrees (EVID-391): D. 63-2023 military promotions;
  **D. 5-2024 MUNICIPAL tax amnistía** (window 14-feb-2024→"31-jun-2024"
  [sic → 30-jun, `109_` OQ-3, kin of D. 2-87's "30-feb"]; mora ≤1-dic-2023;
  plans ≤1y; optional ≤20% principal discount per Corporación; EXPIRED —
  amnistía-family kin of 06_); D. 6-2024 migration-amnesty extension to
  31-dic-2024. Residual: the gazette ellipses point at the STILL-DAMAGED
  2007 print → clean/consolidation D. 199-2006 lead STANDS (109_ OQ-2).
  COVERAGE regen: 108 rows = 106 cited + 2 N/A; 1094/495/573/323; gates
  PASS. Rulings R-H1..R-H79.
- **V-HN1b in-corpus reads (2026-08-20, do not re-derive):** `95_`+`96_`
  (EVID-337..348): **FR-067 PINNED + ACTIVATED** — L30k@60 = D. 199-2006
  **Art. 30 num. 14** (own-law "crédito adicional", NOT an ISR amendment),
  valid_from **10-ago-2007**; 96_ (D. 45-2025) does NOT touch deductions;
  carries = taxation/02 OQ-009 (**D. 59-2023 G 14-feb-2024 intermediate
  reform UNACQUIRED = new top lead**; beneficiarios = 60+ OR any-age
  jubilado vs plantilla 60-turn gate; stacking = plantilla-only practice,
  no statutory bridge; créditos-vs-deducción mechanics). `93_` (EVID-350/351):
  **R-H72** — 22-A FR-082 regime 0 (FY2017 = original D. 278-2013 Art. 9
  rules per D. 31-2019 authentic interp: L10M trigger, 1.5%/0.75% floors;
  gazette = G 34,932, catalog "34,934" in error). `97_` (EVID-355/356):
  **R-H73** — original Art. 14 conditioned the 65+/L350k exemption on 5
  consecutive Art. 22-b periods; D. 59-2020 deleted it (FR-068 history
  rows). Coverage after V-HN1b: 107 rows = 101 cited + 6 N/A; LBs 483.
- **W7 residual-chain decode (2026-08-21, do not re-derive):** the four
  1990-1995 TEXTS (D. 36-90 / D. 54-95 / D. 74-95 / D. 247-89) are
  UNACQUIRED — routes exhausted: congreso CDX FULL-DOMAIN (beyond
  leyesdehonduras: a SECOND library `leyes nacionales/` (~35 era files), a
  `Codigos/` folder, a GLIN archive with date-coded `HN<DDMMYYYY><NN>` names
  (1978-2003) — no matches), TSC biblioteca (live 2026-redesign catalog +
  Wayback CDX 12,148 PDFs), STSS/trabajo CDX (2,411 PDFs; the biblioteca
  `ley de decimo tercer mes.pdf` + `reglamento del decimo cuarto.pdf` =
  md5-IDENTICAL to 105_/102_, discarded), SAR wp-search. But the chain
  DECODED via **`119_` = the official congreso "Inventarios de Leyes"**
  (Wayback of `congreso.gob.hn/decretos/`, 559 pp., TEXT-NATIVE — no OCR
  needed; Sub Sección 6.1 "Mapeo… Derecho Laboral" pp.274-283, laws since
  1877). **R-H81:** the W4-era 102_ OQ-2 "two conflicting D. 54-95 cites"
  = **TWO decrees** — Art.-34 interp footnote prints **D. 74-95** (dado
  25-abr-1995, G 27,655 18-may-1995; the W4 extraction's "54-95" was an OCR
  misread — fixed in EVID-238/LB-002 with dual-dpi 300/600 proof) and the
  Art.-1 tacit-reform footnote's **D. 54-95** = the 14th-month extension "A
  TODOS LOS JUBILADOS Y PENSIONADOS EN GENERAL" (dado 28-mar-1995, gazette
  **G 27,639 28-abr-1995** — the book's "28,639" = digit-swap; monotonicity
  27,587@23-feb (Acuerdo 02-95's OWN new pin) < 27,639 < 27,655 arbitrates).
  payroll/02: FR-057 re-attributed to D. 74-95; **FR-097** = the dated
  beneficiary row (+jubilados from 28-abr-1995, pension-side flag, mirror of
  FR-052) in the gap range 097-100; LB-025; AC-022; **OQ-002 RESOLVED**;
  OQ-012 unchanged (D. 54-95 content pinned = extension-only, does NOT
  recite D. 135-94 vigencia). **R-H82:** D. 36-90 = **G 26,131 del
  11-MAY-1990** (the inventory's "11de Abril" = its own slip — publication
  cannot precede the 2-may-1990 Dado; payroll/06 LB-014/FR-248-249) and
  **D. 247-89 = G 26,028 del 6-ene-1990** (CT-120 "ampliación de auxilio de
  cesantía"; effect already integrated in 86_'s pre-2008 Art. 120, so its
  text is genealogical — but it is the ONE chain member whose content is
  quote-nowhere = the live residual; payroll/08 LB-007). Bonus pins: D.
  178-86/D. 2-87 corroborated ≡ 111_/112_; RIT ancestor = Acuerdo 166-JD-76
  + Art.-8 reform 003-82JD (both G 25,013 30-ago-1986); D. 215-92 =
  Judicial-branch 13th-month authorization; D. 40-89 = Dec-1989 SMM-table
  reform. **Caution class (119_ OQ-2): the inventory's gazette digits slip**
  ("25,655" for 27,655; "Decreto No. 12" for 112; garbled Acuerdo-345 pin) —
  it is a discovery/cross-check source, never the gazette record;
  monotonicity + instrument prints are the records. Totals after W7: payroll
  327/164/171/83; rulings R-H1..R-H82; next EVID 434; COVERAGE 118 rows =
  116 cited + 2 N/A, gates PASS.
- **W8 acquisition wave (2026-08-21, do not re-derive):** TEN files
  registered `120_`..`129_`: **120_ = Ley RAP D.L. 107-2013 ORIGINAL**
  (G 33,222 6-sep-2013, Wayback of rap.hn's own dead pdf/leyrap1.pdf; the
  site's "reglamento" PDFs = contest rules, discarded at page-1);
  **121_ = D. 51-2003 LET** (G 30,059 10-abr-2003; Dado 3-abr, Ejecútese
  8-abr Maduro; vigencia split +30d ISV-15 legs / +180d Cap. IX);
  **122_ = Acuerdo 0948-2003** (the LET reglamento, gazette 28-jun-2003,
  No. not printed on extract); **123_ = D. 52-2004** (LET-Art.-49 interp,
  G 30,437 9-jul-2004); **124_/125_/126_ = the turismo family**
  (314-98 G 28,847 23-abr-1999; 135-2006 cruise class G 31,168; **68-2017
  Ley de Fomento G 34,419 17-ago-2017 = CURRENT, DEROGATES 314-98**);
  **127_ = Acuerdo 005-2017** (selectivo/production-consumption reglamento,
  G 34,282 6-mar-2017, TEXT-NATIVE); **128_ = D. 99-93** (FX-repatriation,
  gazette 9-jul-1993, leyesdehonduras Wayback); **129_ = D. 74-95 TEXT**
  (G 27,655 May-1995 — found in the W6 leyesdir.cdx the W7 hunt never
  re-grepped; W7's "routes exhausted" corrected; Dado abril-1995
  600dpi-converged, Ejecútese 15-may Reina). Rulings: **R-H83 —
  "Acuerdo N°799" = the ISR reglamento of 1970** (G 19,972 13-ene-1970,
  deroga the 1955 reglamento; Art. 33 reformed by Acuerdo 6-B G 21,505
  4-feb-1975; 31_'s "799-1963" = manual slip; lineage 2106-1952→498-1954→
  787-1955→799-1970; TEXT unacquired — 119_ entry 324, EVID-479);
  **R-H84 — ATN = LET Cap. II Arts. 5-16** (1% Art. 7; PJ-comerciantes
  Art. 5; L3M EXCESS-ONLY Art. 14.1; ATN-as-ISR-credit Art. 15; declaration
  rides ISR-annual; FREP/07 OQ-010 RESOLVED — the 74_ "Capítulo II" and
  corpus "Art. 7" citations never conflicted); **AS SURPRISE — Art. 22 =
  "temporal"… "hasta el año 2005"** → the CURRENT FY2014+ AS needs its
  re-establisher (first candidate D. 278-2013, unacquired — refined lead,
  shared with the devolución-8% Arts. 20-21 residual); **R-H85 — the Ley
  RAP delta**: original Art. 42 = "empresas con 10+ empleados" +
  FOSOVI-unregistered; original Art. 43 = "El Patrono aportante" 1.5+1.5=3%
  on FULL salario mensual ordinario, ≤15 días entero, Consejo-Directivo
  rate power — NO IVM-excess/ceiling (both = 2024 inserts; credits ¶ =
  appropriation of the Arts. 40-41 block); original Art. 61's D. 167-91
  exception deleted by the reform; 47_'s ellipsis = the original's exact
  end → transcription COMPLETE (payroll/05 OQ-003/OQ-006 RESOLVED;
  FR-216 + AC-019 dated rows across the 2013→2024 boundary).
  Other pins: LET Art. 18 = the ISV-tarjetas retention-agent origin
  (FREP/04 OQ-003 Art.-18 leg); Art. 28 = Registro Fiscal de Imprentas
  (+180d vigencia — EINV lineage); Art. 44 = the cooperative-mercantile
  origin (506/509-boundary bookend); Art. 49 = OPD/ONG/OPDF rule;
  derogations (Art. 56) do NOT include D. 54-96 (negative); **D. 68-2017
  Art. 21 = the tasa-turística cobrar-retener-enterar ≤10-primeros-días
  procedure** (creation/rate stays D. 131-98 Art. 43 — untouched,
  grep-verified negative; adjudicates the días-drift: días del mes, not
  hábiles/calendario-explicit); 127_ Art. 19 = import formula
  ISV=(CIF+DAI+ISC+IPC)t (rates cuadro image-only; Arts. 18/20-vs-19 ISC
  contradiction = OQ); 128_ = the código-115 FX-deposits exclusion
  mechanism (FY-capped, criminal-origin-denied). Totals after W8: payroll
  328/165/172/83, taxation 249/114/140/56, FREP 363/160/189/170; rulings
  R-H1..R-H85; next EVID = 482; COVERAGE 128 rows = 126 cited + 2 N/A,
  gates PASS (1097/511/574/326).
- **W9 residual-queue acquisition wave (2026-08-21, do not re-derive):**
  NINETEEN files `130_`..`148_`, EVID-482..565 (84; 8 dispatched with 4
  shape-(b) re-dispatches; brief A controller-executed after triple
  failure). **R-H86 — D. 278-2013 CAPÍTULO V Art. 15 "Restablecimiento de
  la Aportación Solidaria" = the AS FY2014+ RE-ESTABLISHER** (re-reads LET
  Art. 22 wholesale: 5% on the EXCESS of RNG > L1M, PJ except
  export/tourism, sobretasa del ISR, non-deductible, ISR calendar; FREP/07
  FR-255/256 + LB-018). **130_'s other legs:** Art. 9 = the 22-A ORIGINAL
  (regime 0 extended to FY2014-17 — taxation/03 FR-082/LB-019; five 0.75%
  sectors = the ORIGINAL list; exclusion b) keeps <L10M inside the ATN;
  losses → D. 96-2012 dado 20-jun-2012 NEW pin); Art. 20 = the
  devolución-8% SIX-MONTH SELF-EXPIRING suspension (01-ene-2014→30-jun-2014
  outer bound; `41_ OQ-3` resolved as temporal — NOT a repeal; Art. 21's
  OTCD retention was 50% at 2013 → D. 7-2017 → SAR-240 chain); Arts.
  1-2/5/22-27/49 = the exonerations RESET (24+17-numeral survival
  catalogues; 12-year default cap; DGCFIA registration; Adulto Mayor #13/#11
  alive; derogations incl. D. 194-2002 Art. 48 + CT Art. 464 — a
  payroll-staleness check on 86_); Arts. 16-19+Anexo I = the CURRENT
  15/18 ISV statutory home + the canasta DESCRIPTION-PREVAILS NOTA +
  Simplificado 31-ene; vigencia EXPLICIT 01-ene-2014 (Art. 51 — not
  publication-day). **SAR-256-2024 = the DMC due-day bomb** (SEGUNDO/TERCERO:
  may/jun/jul-2024 at 20 días transitional, from aug-2024 **8 días
  calendario CURRENT** — FREP/03 FR-091/092/OQ-004 re-seeded, R-H18's
  manuals-stale reading SUPERSEDED (they cited the plazo as rewritten);
  OVI monopoly operative 28-jun-2024; SAR-236 owns the 535 approval +
  deroga the whole e-filing ancestry incl. SAR-007-2017 — FREP/01
  OQ-008/009 resolved). **LSP statutes:** the CETF (códigos 501/524) =
  LSP's own contribución, tarifa L2.00/millar (a/b/d/e/f) / L1.50 (c) /
  tramos (g); reglamento exemptions L120k/L20k + enteros 20th/5th;
  telefonía Art. 13 1% transitorio; comidas Art. 23 permanente per
  31-2018 (now in corpus via the texto actualizado); the 506-vs-509
  boundary NARROWED (53-2015 relieves ISR/ATN/AS only; no derogation
  anywhere) — **D. 92-2015 (G 33,883 14-nov-2015) = the closer lead**.
  **TP triple:** law+reglamento+interp text-in (vinculación criteria Arts.
  11-13; the 545 ancestor Arts. 29-32 with the threshold DELEGATION — the
  ≤USD-1M pequeño gate's true instrument = **DEI-SG-004-2016, still
  unacquired**; 62-2019's gazette = G 35,077 19-oct-2019 — the catalog's
  "34,224" was the CT's own edition, registry corrected). **THE Reglamento
  General IHSS triple (the W4b TOP lead RESOLVED):** `145_` Acuerdo
  003-JD-2005 "última versión" (institutional retypeset, duplicate-Art.-193
  defect) + `147_` the GAZETTE ORIGINAL (G 30,735 29-jun-2005; full Art.
  1-194; the "188-vs-143" count premise was a regex artifact) + `146_` the
  1971 Reglamento de Aplicación ancestor (≡ Acuerdo 101-JD-71 inference)
  + `148_` G 33,879 interventora extract (RAP-patrimony initiative).
  **Art. 135 = the contribution-BASE resolver — payroll/03 OQ-005
  RESOLVED, FR-115 rewritten:** cotizable salary = fixed/ordinary + primas
  + sobresueldos + BONIFICACIONES HABITUALES + OT/horas extras + trabajo
  suplementario + REST-DAY value + %ventas + commissions + profit
  participation; OUT = ocasional-y-por-mera-liberalidad primas/bonos/
  gratificaciones; in-kind ≤30%; the AGUINALDO stays OUT per D. 117-2021
  (89_); the 14th = config flag (new OQ-010). Art. 134 = minimum base =
  category SMM (FR-137); Art. 136 + 151 = the ceiling/review powers; Arts.
  43/67 = subsidio 66% + patrono complement (RIT kin); **Arts. 88-97 = the
  RP chapter (0.2% new-entrant entry on nominal-at-techo, five classes,
  January siniestralidad filing, ≥1-year stability — OQ-006 narrowed,
  class cuadros still absent)**; Art. 144 = EMPLOYER 10-day payment (new
  FR-136; vs the State's 15-day rhythm); Art. 161 = 10%-monthly multa
  class. Recipe added: ihss.hn Wayback CDX (`url=ihss.hn*&filter=mimetype:
  application/pdf`) — 246 PDFs incl. the whole reglamento family.
  Verification: EVID structural 84/84 contiguous + 3-gram bank-check with
  LOWs adjudicated; COVERAGE 147 rows = 145 cited + 2 N/A, gates PASS
  (1099/523/574/327). Totals: payroll 330/170/172/84, taxation
  249/118/140/56, FREP 363/164/189/170; rulings R-H1..R-H86; next EVID =
  566.

- **W10 sharpened-residual closers (2026-08-21, do not re-derive):** TWELVE
  files `149_`..`160_`, EVID-566..643 (78; 7 dispatched, 3 shape-(b)
  re-dispatches — all delivered). **R-H87 — D. 92-2015 (G 33,883
  14-nov-2015; Dado 8-sep-2015, Ejecútese 22-sep-2015) reforms D. 53-2015
  Arts. 3/4/7 ONLY** (grep-negative on LSP/44-A — the 506 side untouched,
  no derogation anywhere): (i) the reservas/fondos/donaciones tail in the
  509 excedente-bruto base = REFORM TEXT (text-native — resolves the
  138_-OQ-8-class "reform insert vs OCR loss"; the 59_ manual quotes the
  post-reform state); decree-Art.-2's "deducibles de los excedentes brutos"
  interp vs the reformed definition = staged α/β tension (exclude-once
  encoded, FREP/11 OQ-022 flag — never double-subtract); (ii) reformed
  Art. 7 = the 509 sanction chassis (formal fault 1-or-2 SMM-promedio by
  capital-en-giro ≤/>L200,000; material 3%/mo cap 36%) with a **THIRD
  promedio resolution semantics: "vigente en la fecha en que se origina el
  incumplimiento"** (hecho-generador time — never conflate with the FY-cap
  family or the CT-131 emission-time family); (iii) **the 506-vs-509
  boundary instruments are COMPLETE — the reformed D53-Art.-3 sentence is
  unqualified ("Las Cooperativas están exentas… a partir del Ejercicio
  Fiscal 2014") but so was the original, and every OTHER operative article
  of both decrees is CONSUCOOP-gated → readings A (all coops) vs B
  (CONSUCOOP) both textually open, B with more witnesses — FREP/11
  FR-382's selector gate STAYS BLOCKED pending OWNER RULING** (60-day
  omisos window 15-nov-2015→13-ene-2016; pre-FY2014 liberation
  CONSUCOOP-gated, HISTORICAL). **R-H88 — Acuerdo DEI-SG-004-2016 (G
  34,018 27-abr-2016; acuerdo dated 08-ene-2016)**: exercises the
  Reglamento-PT-Art.-30.4 delegation — **pequeños with related-party ops >
  USD 1,000,000 acumulado file the DJIAPT** ("1,000.000,00" as printed;
  "paridad cambiaria" with NO rate date — the 31-dic/BCH = 63_-manual
  elaboration, OQ-009 carries); TERCERO = filing notifies the Art.-8
  method; CUARTO = the Ayuda Manual is an integral part (63_'s authority);
  **NEGATIVE RULING: NO safe-harbour content (grep-verified) — with
  027-2015-Art.-38 = OECD incorporation + OECD §4.93-4.95 external, NO
  safe-harbour regime exists in HN TP law (FREP/10 OQ-005/OQ-006
  RESOLVED)**. **SAR-653-2023 (G 36,489 19-mar-2024; date line 29-dic-2023
  = catalog-slip)**: the CbCR/Informe País por País — OECD Defs. 1-13
  (**Def.-3 threshold: prior-FY consolidated revenues < EUR 750M `o`
  L19,000M words-only, never derive**); SEGUNDO Num.I Honduran-UPE duty
  LIVE / **Num.II local filing SUSPENDED from the outset by the
  TRANSITORIO until a Director-Ejecutivo comunicado** (encode suspended —
  the restatement comunicado = top lead; FREP/10 OQ-024); Num.3 surrogate
  exemption (5 conditions); Num.4 UPE-jurisdiction umbral (Jan-2015 FX, NO
  exchange condition printed); TERCERO 31-dic digital notification; QUINTO
  FY-close+12m XML; first reportable FY2025 — `63_ OQ-6` resolved.
  **R-H89 — D. 7-2017 (G 34,284 8-mar-2017)**: ISV-Art.-8 ¶6 = **10%
  automatic** (displacing 278-2013-Art.-21's 50% AND the CT-211-2
  12%-autónoma interim) + **the 15% no-discrimination fallback: "sobre el
  monto total cuando no exista discriminación del Impuesto causado"** —
  trigger = no-discrimination (NOT afiliado status), base = the transaction
  TOTAL (at 15% ISV the fallback exceeds the embedded tax — not tax-capped
  on its face, flagged); Art. 3 DEROGATED 278-2013-Art.-21; chain complete
  50% → 10%/15% (8-mar-2017) → SAR-240-2024; zero drift vs 05_'s
  consolidation — **FREP/04 OQ-003 RESOLVED, FR-147 toggle statute-dated**.
  **SAR-239-2024** = the QUINCENCAL CETF retenciones/percepciones
  informativa (banks; replaces DEI-SG-110-2012; rides the SAR-236 chassis;
  D. 194-2002-Art.-45 authority) — a new cadence class in FREP/01's
  due-day engine; **SAR-283-2024** = the 30-jun→4-jul-2024 pagos-a-cuenta
  prorroga (HISTORICAL one-off). **Acuerdo 006-JD-2008 REAP** (G 31,681
  9-ago-2008): the domésticos health-only lane — annual prepaid
  cotización, JD-delegated rates (Art. 18, values unacquired — payroll/03
  OQ-011), hospital EXCEPT maternity + incapacidad subsidies EXCLUDED (the
  payroll/04 engine does NOT run for REAP workers), optional IVM bridge,
  substitute-inscription free till year-end — FR-126 segment gate. **R-H90
  — THE PROMEDIO FAMILY: `156_`/`157_`/`158_` the DGS prints (2022
  L11,278.75/375.96/46.99 [fixer unfootnoted = lead]; 2023
  L12,377.73/412.59/51.57 [jornada triple-pass 600dpi-closed;
  TWO-PRINT-validated vs SAR-125-2024's SETRASS-411-2023 recital — the
  fixer power attaches to SETRASS/DGS oficios as a family]; 2024
  L13,156.53/438.55/54.82 [native-layer corroborated]) + `159_/160_` the
  CT-131 descargo anchors (2025 L13,985.16 via SAR-43-2026 G 37,077
  `printed_anchor` — DGS 2025 print never existed in uploads/2025; 2023
  L12,377.73 via SAR-125-2024)** — smm_tables.csv rows flipped; the FY2022-
  FY2025 10×SMM caps unblocked (112,787.50 / 123,777.30 / 131,565.30 /
  139,851.60); **THREE promedio resolution semantics separated, never
  conflated: FY-cap (taxation/04 FR-134) / emission-time umbral
  (CT-131: SAR-125-2024 used 2023's in Feb-2024, SAR-43-2026 used 2025's
  in Feb-2026 — bienio March publications demonstrated twice, D-H2) /
  hecho-generador-time sanctions (R-H87)**; 2027 = the only gap (early
  2027 watch); Oficio SETRASS-DGS-014-2025 = the 2025 fixer lead; Oficio
  SETRASS-DGS-014-2025-kin lead class. **D. 96-2012 UNACQUIRED — routes
  exhausted W10** (SAR catalog live re-crawl 506 slugs, TSC/congreso/STSS
  saved CDXs, DEI sitioleyes = 2007-era snapshots, engines unusable);
  refined pin = gazetted **20-jul-2012** per 80_'s recital; content
  partially pinned via 01_/29_/30_ (1% anticipo 2-loss-years + L100M;
  3%-CIF imports). Verification: EVID structural 78/78 + bank-check LOWs
  adjudicated (cross-file gloss quotes, 153_ layer spacing, table-OCR
  garble); COVERAGE 159 rows = 157 cited + 2 N/A, gates PASS
  (1099/532/574/331). Totals: payroll 330/172/172/85, taxation
  249/120/140/56, FREP 363/169/189/174; rulings R-H1..R-H90; next EVID =
  644.

- **W11 amnistía + negatives wave (2026-08-22, do not re-derive):** FIVE
  files `161_`..`165_`, EVID-644..664, controller-executed (no dispatch
  needed). **THE IHSS AMNISTÍA FAMILY BOTH GENERATIONS:** the 2016 HISTORICAL
  pair (D.L. 112-2016 G 34,170 26-oct-2016 [recargos/multas/intereses on
  un-entered aportes; capital always payable; 12-month window; health-access
  restoration] + its Reglamento Especial, CI print 11-nov-2016 [window
  26-oct-2016→25-oct-2017 PRINTED; flat-12% convenio interest + prima/plazo
  table ≤L200k 20%/12m · L200k-1M 20%/18m · >L1M 15%/24m; default = 1 cuota
  + 31d mora → débito claw-back; FSA-01; PN lane = Afiliación Progresiva
  (REAP cross-link); Art. 6 ¶3 = the RTN-unificación/número-único-patronal
  origin]) + **the LIVE 2025-2026 chain** (located by the W11 ENAG full-text
  scan dic-2025→ago-2026): D.L. 44-2025 (G 36,861 11-jun-2025 — the
  seven-amnistía package: municipal/IHSS/ENEE/vehicular/HONDUTEL/SANAA; IHSS
  Art. 2 scope "recargos y multas" as printed, 10-month window superseded
  mid-flight) → D.L. 78-2026 (G 37,166 12-jun-2026 the AMPLIACIÓN: **Art. 1
  = the CURRENT SAR general amnistía, window 12-jun→12-oct-2026, obligations
  ≤31-dic-2025, principal survives — and it DEROGATES D. 7-2026 Art. 7
  (06_) same-day**; Art. 2 = the IHSS re-grant, scope restored to
  recargos/multas/intereses, window → 12-oct-2026) → Res.
  SOJD-IHSS-016-2026-XIII (JD 25-jun-2026; Comité Acta CR-02-2026 [6-vs-16-
  jun print variance = OQ-1]; certified G 37,189 9-jul-2026 = the REFORMED
  REGLAMENTO: convenio gate principal > L15,000; **economics table 0% ≤12m
  / 12% longer, prima mínima 10/15/25% sin- and 20/30/35%
  con-refinanciamiento incl. demand-process tiers**; hardship exceptions
  120m ≥5% / 96m ≥10% with financials/ISR evidence; **terminal 12-oct-2026 +
  6-month processing tail (→~12-abr-2027, received-in-time only)**; Art. 24
  continuity + judicial (LI-Art.-65) + Ministerio-Público enforcement).
  Fold-ins: payroll/03 LB-021/022 + OQ-012; taxation/07 LB-013 + the LB-010
  Art.-7-derogation annotation. **W11 NEGATIVES (dated 2026-08-22, all
  scan/check-verified): NO 2026 JD ceiling act dic-2025→ago-2026 (218 ENAG
  issues, full-text — payroll/03 AC-006's blocking config gap = the LIVE
  state, 2026 payroll periods run on it) · the CbCR TRANSITORIO restatement
  comunicado NOT published (FREP/10 OQ-024 suspended row stands) · Oficio
  SETRASS-DGS-014-2025 + DGS 2025 print not published · ihss.hn full-domain
  CDX (8,000 URLs) negative for RP cuadros/JD ceiling resoluciones/REAP
  JD-rates · D. 96-2012 re-grep negative. PUBLICATION-ROUTE DATUM: IHSS JD
  acts = Sección-A CERTIFICACIÓN blocks (G 37,130/37,188/37,189/37,206
  observed) — the future techo/rate-act watch route.**
- **THE W5 LOST-FILE RECOVERY (W11, do not re-derive):** the committed
  `106+107+108_*.evidence.md` was an md5-IDENTICAL duplicate of the 105_
  pass since the W5 commit — the real EVID-373..384 bank never landed in
  git (a shape-(b) subagent anomaly UNDETECTED at W5 verification). Caught
  by the W11 corpus-global EVID structural sweep; RECONSTRUCTED
  controller-side (the 106_/107_ OCR sidecars had survived; 600dpi
  multi-pass on the damaged reglamento spans; cross-anchored to the W5
  LB-018 verbatims that survived in payroll/02). One own-reconstruction
  error caught+fixed at 600dpi (Art. 10's "extremo que deberá constar" ≠
  "excepto"); Art. 19's prescription span stays NEVER-ENCODED per the W5
  adjudication. **CONVENTION ADOPTED: run the corpus-global EVID sweep
  (duplicates + contiguity across ALL evidence files) at EVERY wave's
  verification.**

- **W12 GLIN re-grep wave (2026-08-22, do not re-derive):** TWO files,
  EVID-665..680, controller-executed, NO new ruling (deltas are dated-row
  history, both texts coexist at different dates). **The acquisition
  route:** the W8-recipe lesson ("when a hunt fails, re-grep EVERY saved
  CDX enumeration") executed against the SAVED W7 full-domain congreso CDX
  — the `PDF/CODIGOS/HN<DDMMYYYY><NN>.PDF` GLIN names are GAZETTE-DATE
  -CODED; HN0505195001 = the Código de Comercio print, HN1905195901 = the
  CT original. **166_ = Código de Comercio, DECRETO No. 73 de 1950** (NOT
  "D. 4-1950" — 12th lead-attribution fix; Dado 16-feb-1950, Ejecútese
  17-feb-1950; official consolidated print post-May-1959 [the Apéndice
  footnote cites CT-189-1959 as "actualmente"]; main sequence Libros I-VI
  to Art. ~1,683 + disposiciones 1º-21 + APÉNDICE = the 1940 code's Libro
  III Comercio Marítimo [kept vigente per transitory Art. 1º until a
  Código de la Navegación; TRUNCATED at CdC-APX-Art. 1038]; the º-glyph
  OCR trap decoded: "Artículo 1º" OCRs as "19/1%/lo./10."). **Art. 143
  VERBATIM = the FREP/10 LB-008 541 dividend-proportionality anchor — now
  instrument-backed** (Art. 144 = the socio credit right). Art. 13 catalogs
  the cooperativa as mercantile type VI with fn(1) = the **D. 158-1954**
  special-law carve-out — R-H91 CONTEXT only (corroborates the
  statute-mediated cooperative posture; does NOT reopen the ruling).
  **167_ = the CT D. 189-1959 ORIGINAL print, complete**: **THE CT
  PROMULGATION PIN — G 16,827-16,834 of 15→23-jul-1959 → vigencia
  15-JUL-1959** (Art. 875 publication-day trigger; Dado 19-may-1959,
  Ejecútese 10-jun-1959). **THE HEADLINE DELTA: original Art. 120 lit. d)
  caps cesantía at 8 MESES** — the 25/15 caps arrive with D. 150-2008
  (fn.19); no lit. g) originally; original lit. f) "valor actual" (vs
  current "valor actuarial"); the 1990-2008 window after D. 247-89's
  "ampliación" = payroll/08 OQ-008 (cap UNPINNED, prescription-muted).
  Original preaviso ladder ≡ current → whole-life rows (24h/1w/2w/1m/2m +
  the 1-day/week job-search licencia + Art. 118's worker-½/patrono-full
  omission asymmetry). Original 95.13 coop/cajas deductions =
  "trabajadores sindicalizados" ONLY (the non-union 60-A lane is wholly
  post-1973); 95.16 = the February annual wages report + Libro de Salarios
  authorization. **The 8+3 feriado list = VERBATIM the 1959 original — the
  D.L. 116-1960 + D.L. 275-1960 pair (per 86_-fn.31, confirmed by the
  print's own Anexo pointers) reformed MECHANICS only** (÷6 average interp
  + collision rule); list vintage 1959 whole-life; the 1960 texts =
  Anexo-class leads. Art. 874 = the full pre-1959 derogation genealogy
  (feriados: D.L. 96-1949 → D.L. 7-1958 → CT; contratación 224-1956;
  sindicales 101-1955). Fold-ins: payroll/08 +LB-015 +OQ-008 + FR-302
  dated-row note; payroll/06 OQ-002 refinement; payroll/10 LB-005/LB-015
  annotations; FREP/10 LB-008 annotation. Totals: payroll 330/175/172/87;
  rulings R-H1..R-H91 (unchanged); next EVID = 681. Verification: EVID
  sweep 654/zero-dup (654 = W11's 638 + 16) + bank-check adjudicated
  (13/13 load-bearing tokens in-bank; LOWs = OCR-noise/º classes) +
  COVERAGE regen 166 rows = 164 cited + 2 N/A, gates PASS (1099/536/574/333).

- **Decisions:** **D-H1** (binding, EXTRACTION_PLAN): one journal per company
  via `l10n_latam_invoice_document`; sequence key = (establecimiento→
  `stock.warehouse`, punto de emisión→child emission point, doc type→
  `l10n_latam.document.type`); emission point NOT on journal;
  user↔emission-point matrix = operational FR only. **D-H2** (2026-08-20,
  binding): temporal validity — dated rows resolved by HECHO-GENERADOR/
  period date; payroll key = (payslip period, worker attributes,
  birthday-year rules); HARD BLOCK emission outside CAI vigencia; historical
  = flagged read-only imports; payroll corrections recompute with
  ORIGINAL-period rows; filed periods write-protected; regime cutovers =
  dated config rows. **D-H3** (2026-08-20, binding): go-live ingestion =
  current-FY fiscal-document detail (read-only, original CAI numbers/dates) +
  prior-years aggregates; reconcile vs PREVIOUS system's SAR filings;
  payroll = monthly aggregates per contract (hire-date depth fondo/cesantía/
  vacaciones, FY-start depth ISR/13th/14th); stock/banks = opening balances.

## 5. Gotchas & verified lessons

- **Wrong-domain sites:** congresonacional.gob.hn / stss.gob.hn / upap.gob.hn
  / cpmcp.hn / enag.hn = NXDOMAIN. Real: `congresonacional.hn` (no law
  library), `www.trabajo.gob.hn` (STSS WordPress), **`enag.gob.hn` = Gaceta
  Digital 2015-2026** (recipe: `/index.php/gaceta-digital/<year>/<mes>` →
  `/index.php/gaceta-digital/<id>/download`). TSC biblioteca fully crawled.
- **SAR downloads:** resolve fresh wpdmdl from `/download/<slug>/` page
  (tokens rotate); some slugs dead. **SAR REST search endpoint works
  (wp-json/wp/v2/search) but only indexes posts/pages — validated empty for
  aguinaldo/séptimo día while returning hits for salario; absence of results
  ≠ absence on site (catalog crawl is the real check).**
- **OCR (proven recipes):** scanned gazettes OK at default PSM 6; TABLES
  need `gs -r400 pnggray` + `tesseract --psm 4` (proven on tabla acuerdos +
  91_/92_ rama columns); mojibake text layers (81_ rates, 90_ full, 87_
  font-mangled) re-covered by PSM 6 at 400dpi — sidecar `.OCR.txt` files
  live in hn/.extractions/ and are the AUTHORITATIVE text for those pages.
  102_'s run-on damage is legible as-is.
- `11_` plantilla formulas read fine via openpyxl (not protected).
- IHSS site needs full browser UA. Bing/DDG useless for .hn; navigate
  catalogs directly.
- **Registry glosses and catalog TITLES can mislead — 11 incidents to date**
  (the 11th, W5: 106_'s title "Gaceta 29320" names only the SECOND of its
  two gazette extracts — D. 43-97 is from G 28,271; content as claimed)
  (29_/09_/15_ SV; 05_, 94_, 101_-server-filename, 20_, 52_, **85_** HN —
  85_ was believed "CT derogations" for two sessions before W4d read it:
  Penal-only. Title ≠ content; the end-to-end read is the authority. Numeric
  article collisions across codes (Penal vs CT) make "derogates Art. N"
  claims worthless until the code is named in the text.)
- **Manuals can be stale vs gazettes (W2b):** the gazette text is the
  record; flag manual conflicts as OQs. Same class: 101_ p.4 caption
  misprints the 2023 table as "AÑO 2022"; 102_ p.1 prints D. 135-94 "de
  fecha 12 de Octubre de 1991 [sic]" (print error for 1994).

## 6. Next actions (ordered)

1. **V-HN1 validation wave: COMPLETE 2026-08-20 (see EXTRACTION_PLAN wave
   log for the full adjudication).** Deliverables: `hn/requirements/
   COVERAGE.md` (generated by committed `hn/scripts/build_coverage.py`;
   103 rows = 98 cited + 5 N/A; script gates all pass) + four adversarial
   reviewers' findings adjudicated (R-H67..R-H70 in master index; `89_`
   evidence pass EVID-334..336 with the 10th gloss incident — Art. 2
   aguinaldo interp, payroll/02 FR-087 + OQ-007 conflict vs ISR 10.h
   carried; 95_/96_ in-corpus-unread status fix; whole-base/cliff/feriados
   evidence fixes; EINV FR-085/086 + FREP FR-076 + PAYR FR-087 additions).
   All four topic indexes → approved. DONE same session (W5 wave): the
   105_-108_ evidence passes EVID-362..384 — **P2 aguinaldo UNBLOCKED**
   (R-H74/R-H75), bono reglamento encoded (R-H76, payroll/02 OQ-004
   resolved), séptimo día statutory layer, D. 150-2008 + Acuerdo 345
   anchored; COVERAGE regenerated (108 rows = 105 cited + 3 N/A) — plus the
   **D. 59-2023 FETCH (G 36,460 14-feb-2024 via ENAG, registered `109_`) —
   evidence pass DONE as the W5c wave (this session, on-branch): EVID-385..391,
   R-H78 (L30,000 credit SURVIVES — OQ-009(a) resolved, FR-067 whole-life) +
   R-H79 (cuarta edad = 80+, 96_ OQ-2 resolved) + edition decrees identified
   (D. 5-2024 municipal amnistía = expired kin of 06_); COVERAGE regen
    (108 rows = 106 cited + 2 N/A, gates PASS). W6 (same day): acquisition +
    evidence pass DONE + MERGED (twenty-first §4.6 run at `24391b6`, root
    record `8513e49`). W7 (2026-08-21): residual chain DECODED via `119_`
    (R-H81/R-H82; OQ-002 resolved; see §4 W7 block) — NEXT = the post-W6
    queue (§6.2).**
 2. **Acquisition queue (W8-amended; RESEARCH §5 + master-index
     C-registers + synthesis OQs):** ~~Ley RAP D.L. 107-2013~~ **ACQUIRED W8
     as `120_`** (R-H85) · ~~D. 51-2003 + 0948-2003 + 52-2004~~ **ACQUIRED
     W8 as `121_`/`122_`/`123_`** (R-H84) · ~~D. 314-98 watch~~ **CLOSED W8**
     (`124_` + derogation by `126_`; tasa-259 procedure = 126_-Art. 21;
     creation stays 131-98-Art. 43) · ~~post-1995 selectivo procedure~~
     **`127_` Acuerdo 005-2017 ACQUIRED** (203-canasta current-state residual
     stays open) · ~~D. 99-93~~ **ACQUIRED as `128_`** · ~~D. 74-95 text~~
     **ACQUIRED as `129_`** (D. 54-95/36-90 content-pinned, texts LOW
     priority; D. 247-89 = the live residual, watch for any pre-2015 gazette
     archive or labeled mirror) → TOP = **Reglamento General IHSS**
     (contribution-base config-flag resolver; 119_ IHSS-block negative = one
     more route exhausted — next: IHSS institutional archive / pre-2015
     JD-instrument gazette crawl) + **"Acuerdo 799" TEXT** (identity pinned
     R-H83 = G 19,972 13-ene-1970; 1970 gazette, pre-ENAG) +
     **D. 278-2013** (ONE instrument, THREE questions: the AS FY2014+
     re-establishment; the devolución-8% suspension Arts. 20-21; the
     Ordenamiento frame) +
     ~~**D. 199-2006 original**~~ (ACQUIRED as `95_` + evidenced V-HN1b —
     FR-067 pinned 10-ago-2007; residual = the 109_ wording check) +
     Ley Equidad Tributaria
    D. 51-2003 (AS/ATN + tarjetas Art. 18) + Acuerdo SAR-236-2024 + DGS SMM
    companion prints (2022-2025 + 2027 when exists) + ~~D. 58-1982 + D. 131-98~~
    (BOTH ACQUIRED W6 as `115_`/`116_` — evidenced EVID-415..424) +
    TP family (D. 232-2011 + 027-2015 + DEI-SG-004-2016) + contribuciones
     statutes + ~~Código de Comercio~~ (CLOSED W12 as `166_` — D. 73-1950) + DEI-9382-J-2003 I-VIII + W3
     adds (462-2014, 424-2018, post-2017 compras-eventuales instrument if any)
     + riesgos-profesionales reglamento + **D. 74-95 / D. 54-95 texts
     (content already pinned — priority LOW, completeness only)**. S-HN3
     sharpened the LSP statutes
     queue: D. 105-2011 + Acuerdo 1775-2011 + D. 31-2018 (LSP portion) +
     D. 53-2015/D. 92-2015 + D. 131-2018 (the 506-vs-509 boundary = the only
     yes-blocking S-HN3 OQ); also Acuerdo 034/99 (542 threshold) and the
     SAR-236-2024 DÉCIMO OCTAVO print. Most SAR-catalog fetchable (recipe §6).
   3. **R-H66 territoriality ruling: RESOLVED — adopted by product owner
      2026-08-20 (worldwide pre-2017 / territorial 2017+; taxation/01
      FR-004 dated rows; master-index Section B row 66; rows reversible).
  4. **Merge to main at milestone:** owner decision; rebase-then-merge; never
     force-push (root HANDOVER country model). Branch head after S-HN1/S-HN2
     commit = the synthesis-wave base; future waves branch from here.

Session state at stop (2026-08-22, W12 GLIN re-grep wave — committed on
`hn-research`, NOT yet merged; owner decision pending): evidence COMPLETE
through **EVID-680** (654 EVIDs on disk, zero collisions); corpus **166
files** (01-167, gap 103); main carries HN through R-H91 (corpus 164 files
at the merge; the W11 + R-H91 merges both landed 2026-08-22). **W12
on-branch: (1) ACQUISITION — 2 files `166_`/`167_` from the GLIN archive of
the old congreso.gob.hn (Wayback `id_`; surfaced by re-grepping the SAVED W7
full-domain CDX for comercio/codigos — keep the saved enumerations forever);
(2) EVIDENCE — EVID-665..680 controller-executed + full OCR sidecars
(166_/167_); no new ruling; (3) FOLD-INS — payroll/08 +LB-015 +OQ-008 +
FR-302 note, payroll/06 OQ-002 refined, payroll/10 LB-005/LB-015
annotations, FREP/10 LB-008 annotation, payroll/00_index wave-noted (totals
330/175/172/87), master index +EV166/167 + Section-C W12 delta, RESEARCH
§5 item-4 strike + §6 W12 recipes, EXTRACTION_PLAN wave log, sources/README
registry; (4) verification — EVID sweep + bank-check adjudicated + COVERAGE
regen 166 rows = 164 cited + 2 N/A, gates PASS (1099/536/574/333).** Watch
ticks this session: ENAG ago-2026 listing — no issue newer than the W11
scan's 20260821-37226 (JD-ceiling watch clean; CbCR comunicado negative as
of the W11 same-day check — not re-checked). Next = the residual watch queue
(TOP: the 2026 JD ceiling act watch via the Sección-A certificaciones
route [2026 payroll = blocking config gap AC-006 until it lands]; D.
96-2012 watch; CbCR restatement comunicado watch; "Acuerdo 799" TEXT + D.
247-89 watch [now also the OQ-008 cap-window key]; ~~Código de Comercio~~
CLOSED W12; SEE docs; DGS SMM 2027 promedio print early-2027; S-HN5
DEFERRED).

Session state at stop (2026-08-22, R-H91 ruling session — committed on
`hn-research`, MERGED to main same-day): **NO corpus change**
(164 files, EVID-664, next EVID 665 — unchanged from the W11 merge). The
session's only work = the 506-vs-509 OWNER RULING folded in: **R-H91
(2026-08-22) — Reading B, CONSUCOOP-gated**: CONSUCOOP-recognized
cooperativas → 509; non-recognized → 506. Fold-ins: FREP/11 FR-382
rewritten + AC-011 + config/mapping rows + **OQ-009 RESOLVED** (the last
unqualified yes-blocking OQ; rows REVERSIBLE — legal reading, not statute;
watch class: SAR resoluciones/DJT opinions assigning non-CONSUCOOP coops);
FREP 00_index wave-noted + blocking-OQ note annotated; master index +R-H91
ledger row + C2 `60_ OQ-1` resolved + Section-C ruling-session delta +
queue strike; EXTRACTION_PLAN wave-log entry; this HANDOVER. Verification:
COVERAGE regen 164 rows = 162 cited + 2 N/A, gates PASS
(1099/535/574/332 — counts unchanged, status flip only). Rulings
R-H1..R-H91; totals unchanged (payroll 330/174/172/86, taxation
249/121/140/56, FREP 363/169/189/174). **Next = the residual watch queue
unchanged (TOP: the 2026 JD ceiling act watch via the Sección-A
certificaciones route [2026 payroll = blocking config gap AC-006 until it
lands]; D. 96-2012 watch; CbCR restatement comunicado watch; "Acuerdo 799"
TEXT + D. 247-89 watch; Código de Comercio (CLOSED W12); SEE docs; DGS SMM 2027
promedio print early-2027; S-HN5 DEFERRED).** [R-H91 MERGED to main
2026-08-22 — thirty-third §4.6 run: 1 commit rewritten
(`052329c`→`ba98ac7`), zero conflicts, remote ref delete + re-push,
root record `49feee5`; main carries HN through R-H91 — corpus/EVID
unchanged at 164 files / EVID-664.]

Session state at stop (2026-08-22, W11 amnistía + negatives wave — committed
on `hn-research`, NOT yet merged; owner decision pending): evidence COMPLETE
through **EVID-664** (638 EVIDs on disk, zero collisions); corpus **164
files** (01-165, gap 103); main carries HN through EVID-643 (the W10 merge).
**W11 on-branch: (1) ACQUISITION — 5 files `161_`..`165_` (161_ ihss.hn
Wayback; 162_/163_/164_/165_ ENAG gazette full issues; 165_ located by the
W11 ENAG FULL-TEXT SCAN dic-2025→ago-2026, 218 issues, grep-all-pages — the
method now in RESEARCH §6); one discard unregistered (the 88_ re-render);
(2) EVIDENCE — EVID-644..664 controller-executed + **THE W5 LOST-FILE
RECOVERY** (the committed 106+107+108 file was an md5-duplicate of the 105_
pass; EVID-373..384 reconstructed from surviving OCR sidecars + 600dpi
re-passes); no new ruling (no contradiction resolved); (3) FOLD-INS —
payroll/03 LB-021/LB-022 + OQ-012, taxation/07 LB-013 + LB-010 annotation,
both topic indexes wave-noted + counts, master index +EV161..165 + Section-C
W11 delta, RESEARCH/EXTRACTION_PLAN updated; (4) verification — EVID
structural 638/zero-dup (the new every-wave convention) + 3-gram bank-check
with LOWs adjudicated (600dpi corrections applied) + COVERAGE regen 164 rows
= 162 cited + 2 N/A, gates PASS (1099/535/574/332). Totals: payroll
330/174/172/86, taxation 249/121/140/56, rulings R-H1..R-H90, next EVID =
665.** Next = the residual watch queue (TOP: the **2026 JD ceiling act
watch** via the Sección-A certificaciones route [an actuarial techo act may
land any month — until then 2026 payroll = blocking config gap, AC-006];
D. 96-2012 watch [20-jul-2012 gazette pin]; CbCR restatement comunicado
watch; RP class cuadros + JD ceiling resoluciones + REAP JD-rates = routes
exhausted, watch class; "Acuerdo 799" TEXT + D. 247-89 watch; Código de
Comercio; SEE docs; DGS SMM 2027 promedio print early-2027; **the 506-vs-509
legal reading = OWNER DECISION**; S-HN5 DEFERRED).

Historical stop state (W10, superseded above): evidence COMPLETE through
**EVID-643**; corpus **159 files** (01-160, gap 103); W9 merged to main
(twenty-eighth §4.6 run at `64183e4`, root record `e777566`; main carries
HN through EVID-565, 147 files). **W10 on-branch on `hn-research` (this
session): (1) ACQUISITION — 12 files `149_`..`160_` (SAR catalog 151-154
fresh-wpdmdl; ENAG gazette 149/150/159/160 — 150_ located via the 49-issue
April/May-2016 SUMARIO batch-scan, 159_ because the SAR slug login-walls;
trabajo.gob.hn uploads Wayback 156-158 — the DGS promedio prints; ihss.hn
Wayback 155_ REAP; the ihss.hn AJ-RIESGOS-PROFESIONALES catch discarded
unregistered); (2) EVIDENCE — EVID-566..643 in 7 files (7 dispatched, 3
shape-(b) re-dispatches successful); rulings **R-H87** (D. 92-2015: tail =
reform text, boundary instruments COMPLETE — reading A-vs-B open),
**R-H88** (DEI-SG-004-2016 = the TP gate; safe harbour NEGATIVE),
**R-H89** (D. 7-2017 = the OTCD middle instrument), **R-H90** (the
promedio family + three resolution semantics); (3) FOLD-INS — FREP/10
OQ-005/OQ-006 RESOLVED + LB-014/015 + FR-326/327 re-anchored + OQ-024/025
new, FREP/11 LB-013 + OQ-008 narrowed + OQ-009 instruments-complete +
FR-378 statute-anchored + OQ-022, FREP/04 OQ-003 RESOLVED + LB-014 +
FR-147, FREP/01 LB-022 (quincenal CETF cadence + prorroga HISTORICAL),
taxation/06 LB-020 + FR-249, taxation/01 LB-025 + FR-037, payroll/01
LB-023 + FR-024/025 rewritten + smm_tables.csv promedio rows flipped
(printed ×3 + printed_anchor 2025), payroll/03 LB-020 + FR-126 REAP gate +
OQ-011; three topic indexes wave-noted + counts; master index +EV149..160
+ R-H87..R-H90 + Section-C W10 delta; RESEARCH/EXTRACTION_PLAN updated;
(4) verification — structural 78/78 contiguous + bank-check LOWs
adjudicated (incl. the 157_ jornada 600dpi triple-pass close) + COVERAGE
regen 159 rows = 157 cited + 2 N/A, gates PASS (1099/532/574/331).**
Next = the residual queue (TOP: D. 96-2012 watch [routes exhausted W10;
gazetted 20-jul-2012 pinned via 80_'s recital]; the CbCR TRANSITORIO
restatement comunicado; Oficio SETRASS-DGS-014-2025 [the 2025 promedio
fixer] + the DGS 2025 print watch; RP class cuadros + JD ceiling
resoluciones 2003-2024; the REAP JD-rates family; then "Acuerdo 799" TEXT
(1970) + D. 247-89 text watch; Código de Comercio; SEE docs; DGS SMM 2027
promedio print expected early-2027; **the 506-vs-509 legal reading =
OWNER DECISION**; S-HN5 stays DEFERRED). [W10 MERGED to main 2026-08-21 —
twenty-ninth §4.6 run: 1 commit rewritten (`bef10b2`→`9e600db`), zero
conflicts, remote ref delete + re-push, root record `67ba60d`; main carries
HN through EVID-643, corpus 159 files.]

Historical stop state (W9, superseded above): evidence COMPLETE through
**EVID-565**; corpus **147 files** (01-148, gap 103); W8 merged to main
(twenty-fifth §4.6 run, root record `1308644`; main carries HN through
EVID-481, 128 files). **W9 committed on `hn-research` at `71223da` +
pushed**: (1) ACQUISITION — 19 files `130_`..`148_` (the SAR-catalog
family 130-144 via fresh-wpdmdl fetches — SAR-240-2024 duplicate discarded
md5-identical to `19_`; the IHSS reglamento triple 145-148 via the ihss.hn
Wayback CDX recipe); (2) EVIDENCE — EVID-482..565 in 9 files (8
dispatched; 4 shape-(b) re-dispatches; brief A controller-executed after
triple failure); ruling **R-H86** (AS re-establisher = D. 278-2013 Art.
15); (3) FOLD-INS — payroll/03 OQ-005 RESOLVED (FR-115 rewrite +
LB-015..019 + FR-136/137 + OQ-006 narrowed + OQ-010 new), taxation/03
regime-0 FY2014-17 + 273→278 correction, taxation/02 65+ continuity,
taxation/06 the 15/18+canasta home, taxation/07 exonerations frame,
FREP/07 AS anchored, FREP/03 the DMC 8-day re-seed (R-H18 superseded),
FREP/01 OVI chassis + OQ-006/008/009, FREP/10 TP triple, FREP/11
LSP/CETF statutes; master index +EV130..148 + R-H86 + Section-C W9 delta;
RESEARCH/EXTRACTION_PLAN updated; (4) verification — structural 84/84 +
bank-check adjudicated + COVERAGE regen 147 rows = 145 cited + 2 N/A,
gates PASS (1099/523/574/327). [W9 MERGED to main 2026-08-21 —
twenty-eighth §4.6 run: 2 commits rewritten
(`71223da..43b7733`→`fa57aa1..64183e4`), zero conflicts, remote ref
delete + re-push, root record `e777566`; main carries HN through
EVID-565, corpus 147 files.]

Historical stop state (W7, superseded above): evidence COMPLETE through
**EVID-433**; corpus 118 files; W6 merged to main
(twenty-first §4.6 run at `24391b6`, root record `8513e49`; main carries HN
through EVID-428). **W7 committed on `hn-research` (this session, not yet
merged — owner decision pending)**: (1) TEXT HUNT — routes A-D exhausted for
the four 1990-1995 texts (congreso CDX FULL-domain: second library `leyes
nacionales/`, `Codigos/`, GLIN date-coded archive — negative; TSC live
2026-redesign + CDX 12k PDFs — negative; STSS/trabajo CDX 2,411 PDFs — two
fetches md5-identical to 102_/105_, discarded; SAR wp-search empty);
(2) DECODE — `119_` = the official congreso "Inventarios de Leyes"
(text-native, 559 pp., Wayback of congreso.gob.hn/decretos/) registered +
evidenced EVID-429..433; **R-H81** — 102_/payroll OQ-2 = TWO decrees: interp
= **D. 74-95** (G 27,655 18-may-1995; W4 footnote read "54-95" was an OCR
misread — EVID-238/LB-002 fixed, dual-dpi 300/600 proof) and extension =
**D. 54-95** (jubilados/pensionados, G 27,639 28-abr-1995; book's "28,639" =
digit-swap; monotonicity chain 27,587 < 27,639 < 27,655 arbitrates; Acuerdo
02-95 itself = G 27,587 23-feb-1995 NEW pin); **R-H82** — D. 36-90 = G 26,131
**11-may-1990** (inventory's "11-abril" = slip — publication cannot precede
the 2-may Dado) + D. 247-89 = G 26,028 6-ene-1990 (text = the ONE live
residual, genealogical); RIT ancestor identified (166-JD-76 + 003-82JD,
G 25,013 30-ago-1986); (3) SYNTHESIS — payroll/02 FR-057 re-attributed +
**FR-097** (dated 14m beneficiary row, gap range 097-100) + LB-025 + AC-022
+ 14m.config dated rows + **OQ-002 RESOLVED** (OQ-012 annotated, unchanged);
payroll/06 LB-014 + FR-248/249 gazette-pinned; payroll/08 LB-007 lineage
pinned; master index +EV119 + R-H81/R-H82 + registers; (4) verification —
bank-check 23/23 Spanish legs vs the text layer + 5/5 glyph probes vs
600dpi; structural payroll/02 47/25/22/13 = index; (5) totals — payroll
**327/164/171/83**, FREP 363/157/189/169, rulings R-H1..R-H82, next EVID =
434; COVERAGE regenerated **118 rows = 116 cited + 2 N/A, gates PASS
(1095/503/574/325)**. **Next = the post-W6
queue (TOP: Acuerdo 799 Reglamento Ley ISR, Reglamento General IHSS,
Ley RAP D.L. 107-2013, D. 51-2003; then D. 314-98 watch, post-1995 selectivo
chain, D. 99-93, 95_ clean-consolidation lead (109_ OQ-2), D. 247-89 text
watch); S-HN5 stays DEFERRED. [W7 MERGED to main 2026-08-21 — twenty-fourth
§4.6 run: 2 commits rewritten (`18aea5c..f0b0e92`→`c0d4049..d4b2a49`),
zero conflicts, remote ref delete + re-push, root record `380f044`; main
carries HN through EVID-433, corpus 118 files.]**

## 7. Conventions (mirroring SV)

- Evidence: verbatim Spanish + gloss; candidate CRs + topic tags; doubts →
  OQs, never guesses. Per-file OQ numbering; corpus-global EVID (next=644).
  W2b + W4 + S-HN1/S-HN2 ran subagent-dispatched with pre-allocated EVID/FR
  ranges per family — proven pattern for large batches; controller verifies
  ranges + spot-checks verbatims afterward (done for W4: ranges + 8
  source-level spot-checks incl. all OCR-derived quotes; done for
  S-HN1/S-HN2: 11/11 structural verification + 5/5 verbatim spot-checks —
   script pattern in session log, keep re-using; done for S-HN3: 11/11
   structural (adapted script `/tmp/opencode/verify_hn_s3.py` pattern) +
   5/5 verbatim spot-checks + IPC-chain value re-verification + CSV 25-code
   match vs EVID-077; done for S-HN4: 10/10 structural
   (`/tmp/opencode/hn/s4/verify_hn_s4.py`, same pattern) + STRICT FULL
   verbatim bank-check — every quote-pair-bounded Spanish span ≥40 chars in
   every file vs the evidence bank, split on ellipses, guillemet-edge
   stripping: 372 spans PASS, 5 real one-word LB defects found+fixed, ~45
   residual checker flags adjudicated as artifacts (English spans, OCR-
   bracket resolutions, «» nesting, table reformat). The strict bank-check
   (`/tmp/opencode/hn/s4/spotcheck5.py` pattern) SUPERSEDES 5-sample
   spot-checks for future waves. NOTE: subagent empty-return anomalies now
   TWO shapes —
   (a) empty-return with file-on-disk (W2b/W4, twice), (b) empty-return with
   file ABSENT (S-HN3: 4 of 11 dispatches failed to deliver; simple re-
   dispatch succeeded all 4). S-HN4: 10/10 dispatches delivered (zero
   anomalies). ALWAYS verify disk state, never trust the
   return alone; re-dispatch is the fix for shape (b).
- `.gitignore`: `hn/.extractions/*` ignored EXCEPT `*.evidence.md` +
  `00_MASTER_INDEX.md` (**created 2026-08-19 — committed; update it at every
  wave/milestone that adds EVIDs, rulings, or resolves OQs**).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from `119` (103 reserved-unused);
  page-1 verify everything. **11 title/gloss incidents to date** (the 11th =
  106_: title "Gaceta 29320" names only the second of its two extracts) —
  title-vs-content discipline on EVERY acquisition AND every evidence read.
- **Manuals can be stale vs gazettes (W2b):** gazette text is the record.
- **OCR sidecars:** for any file with an `.OCR.txt` in `.extractions/`, the
  OCR sidecar (not the native-layer txt) is authoritative for the damaged
  passages (81_, 87_, 90_, 91_, 92_ as of W4; 106_, 107_ as of W5; 109_ as
  of W5c — its critical passages additionally re-verified with an
  independent PSM 4 column-aware pass; the dual-pass agreement is what
  proved the Art. 30 ellipses are gazette print, not OCR loss — reuse this
  dual-pass pattern whenever "ellipsis vs OCR-truncation" is load-bearing;
  110..118 as of W6 — `gs -r300 pnggray` + `tesseract --psm 6`; 119_ needs NO
  sidecar (text-native — `gs -sDEVICE=txtwrite` is the authoritative layer);
  155_ as of W10 (300dpi/psm6, two-column de-interleave); **156_/157_/158_
  as of W10 = the DGS TABLE prints (400dpi PSM 4 sidecars; tables need the
  psm4 column-aware pass per the proven recipe; the 157_ jornada cell =
  the W10 triple-pass case: sidecar noise "4127.59" vs PSM6 "412.59" vs
  600dpi-PSM4 "417.59" adjudicated by PSM6 + ÷30 arithmetic + hora
  coherence — reuse multi-pass + arithmetic coherence when a single table
  glyph is load-bearing);**
  and the
  W6 triple-pass (300/400/600dpi) on 113_'s Art. 18 is the R-H80 basis —
  reuse multi-dpi convergence when a single glyph is load-bearing and no
  image-input is available in-session).
