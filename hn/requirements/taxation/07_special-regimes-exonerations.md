# HN — Taxation — Special regimes, exonerations discipline & Ley Eficiencia closers

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-20 (V-HN1 validation fixes) |

## 1. Purpose

This file defines the functional requirements for cluster **T12** — the special
regimes, exonerations discipline and the Ley Eficiencia (*Ley de Eficiencia en
los Ingresos y el Gasto Público*, D. 113-2011, consolidated print Enero-2022)
closers. It owns: the **facturación statutory root** as a REFERENCE-ONLY
anchor (D. 17-2010 L-Art 57 *instituye el Régimen de Facturación* — engines
belong to the S-HN2 e-invoicing files, cited by range HN-EINV-FR-001..175);
the **Registro de Exoneraciones** lifecycle (free mandatory inscription for
exemption/special-regime beneficiaries, 1-month windows for
initial/changes/deregistration, renewal suspended, DEI may inscribe *de
oficio*; prior-authorization + resolution content; diplomatic card-operator
conventions); the **exonerations discipline** of Eficiencia E-Arts 27-29 —
*personalísimas* with any transfer provision *expresamente derogada*,
exonerated vehicles must *regularizar el pago de tributos* on enajenación to
non-exempt third parties, foreign donations exonerated *sólo cuando éstas
sean recibidas en especie* (in-kind only), the SEFIN resolution as single
sufficient document, and solvency reaching only obligations OTHER than the
requested *dispensa* (CT 211.4.b, R-H14); the **RIT** (*Régimen de
Importación Temporal*, D. 37-1984 as replaced by E-Art 30) — duty suspension
on three goods classes, per-importation guarantees for the totality of
suspended duties with the caducidad catalog, the 5-year disposal gate with
GATT Art. VII last-resort valuation, unauthorized diversion = guarantee
execution + multa 100% of the tributary debt, DEI reexport periods per
industry cycle; the **special-regime invariants** (E-Arts 31-34) —
national-market sales taxed at the regime in force at DUA acceptance, the
≤50%-national-sales cap for *empresas comerciales básicamente de
reexportación*, no-simultaneidad, and the *declaración de sacrificio fiscal*;
the **state-side rules** (E-Arts 18-19, 23) — the L25,000 solvencia gate with
3-días-hábiles *Constancia*, the sentencia-payment tax deduction with the
*prestaciones laborales* carve-out, and the CNBS-auditor certification for
claims vs the State, inapplicable to *tributaria* claims (CT 211.4.a, R-H14);
the **dead-text guards** (E-Arts 5/10 VOID per RI-0763-2021 — R-H3/R-H4 —
never FRs); the **registry-gloss meta discipline** (R-H8: 05_'s catalog title
was wrong — title ≠ content); and the amnistía D. 7-2026 dated-config
crossref (D-H2.6 example, no deep FRs).

It does **not** cover: the facturación regime engines — document taxonomy,
CAI/rango ledger, print contract, emission gate, SEE (HN-EINV-FR-001..175,
files `../e-invoicing/01..04_*.md` — L-Art 57 cited as anchor only);
ZOLADES/zonas y parques libres detail and the Acuerdo 462-2014 (exonerations
reglamento, Art. 20 derogated by Acuerdo 817-2018 Art. 2) + 424-2018 leads —
W3 cluster kin (`26_ OQ-2`), LEADs only; the tourism-incentives family
(D. 17-2010 L-Arts 53-55 + R-Arts 63-68; D. 314-98; D. 2-2026 RIT extension)
— unacquired, LEAD; the amnistía D. 7-2026 mechanics (dated config rows by
crossref, `06_` registry row); ISV credit/devolución (E-Arts 3-5 kin =
`06_isv.md` HN-TAX-FR-211..255); ganancias de capital (E-Art 14 =
`03_isr-rates-gains-minimum.md` HN-TAX-FR-081..104); retention engines
(E-Arts 35/52 anchors = `04_isr-withholding.md` HN-TAX-FR-121..153); CT
sanctions/procedure (T11 = `01_isr-framework.md` HN-TAX-FR-001..045); and
the sacrificio-fiscal declaration FORM/layout (AT-approved forma/medios/
plazos — S-HN3 surface; this file owns the duty + calendar entity only).

## 2. Legal Basis

Authority order (binding, per master evidence index): Eficiencia = `05_`
(consolidation print **Enero-2022** — vintage caveat `05_ OQ-2`: post-2017/
2022 reform chain unverified per-article) with **VOID texts Arts. 5/10**
(RI-0763-2021, 25-mar-2021; R-H3/R-H4 — dead text, never FRs); D. 17-2010
family = `04_` + `21_` (L-Arts 40-44, 57 + R-Arts 44-47; reglamento vintage
caveat `04_ OQ-2`); amnistía = `06_` (registry row; D-H2.6 dated-row rule).
Rulings applied: **R-H8** (05_ registry gloss WRONG — content = the
exonerations/RIT/state-side zone, NOT impuesto mínimo/solidario; title ≠
content), **R-H14** (E-Art 23 certification not for *tributaria* claims,
CT 211.4.a; exoneración solvency = obligations other than the requested
*dispensa*, CT 211.4.b), **R-H3/R-H4** (E-Arts 5/10 VOID). D-H2 binds:
every dated legal value (RIT windows, regime cutovers, amnistía windows)
lives in valid_from/valid_to config rows, additive-only.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D. 17-2010, L-Art 57 — **REFERENCE ONLY** | "Instituye el Régimen de Facturación" — institutes the facturación regime, creating the Registro Fiscal de Imprentas (imprentas and autoimpresores); DEI to regulate "los tipos de documentos de carácter fiscal y sus requisitos, la regulación de la factura electrónica, las personas... que deben inscribirse" — the 2010 statutory base later developed by Acuerdo 189-2014 → 481-2017; ALL regime engines are owned by the e-invoicing files (HN-EINV-FR-001..175) — this file cites the root, implements nothing | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Art 57 p.14 (EV04:EVID-052) |
| LB-002 | D. 17-2010, L-Arts 40-44 + Reglamento (Acuerdo 1121-2010), R-Arts 44-47 | Registro de Exoneraciones: free MANDATORY inscription for beneficiaries of exemptions or special regimes; 1-month windows for initial inscription, changes and deregistration; renewal SUSPENDED until updated; DEI may inscribe de oficio (L-Art 40, R-Arts 44-47); card-operator conventions for diplomatic exonerations (L-Art 41); exoneración requires PRIOR authorization + resolution with project detail and approximate purchase amount (L-Arts 42-43) | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` + `hn/sources/21_Acuerdo_1121-2010_Regl_D17-2010.pdf` | L-Arts 40-44 p.11; R-Arts 44-47 pp.10-11 (EV04:EVID-052) |
| LB-003 | Ley de Eficiencia (D. 113-2011, texto consolidado Enero-2022), E-Arts 27-29 (E-Art 28 footnote: CT D. 170-2016 Art. 211 num. 4)b) interpretation) | Exemptions/exonerations are PERSONALÍSIMAS — any provision transferring them to third parties "quedan expresamente derogadas"; exonerated vehicles must "regularizar el pago de tributos al momento de su enajenación a terceros no exentos"; foreign donations to registered private voluntary organizations are exonerated "sólo cuando éstas sean recibidas en especie" (in-kind only); SEFIN authorizes exonerations/exemptions/franchises of special laws and its resolution (beneficiary solvent) "será el documento suficiente para acreditar la exoneración... ninguna institución del Estado debe exigir la tramitación de otro documento"; SEFIN may sign conventions with financial institutions to automate/control benefits; AT collaborates with verification; interpretation: the required solvency is for obligations "distintas a la dispensa del pago de tributos solicitados" (solvency elsewhere, not for the exempted tax itself) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Arts 27-29 pp.12-13 (EV05:EVID-063; R-H14 CT 211.4.b) |
| LB-004 | Ley de Eficiencia, E-Art 30 (reformed D. 261-2011 Art. 1 + D. 170-2016 Art. 195; replaces Arts. 1/2/4 of D. 37-1984) | RIT = SUSPENSION of import duties on: a) raw materials/semi-elaborates/envases/empaques/inputs for exported goods or services (DEI sets reexport periods by industry cycle); b) machinery/equipment/molds/tools/spares/accessories used EXCLUSIVELY for export production — enajenable only after 5 YEARS from importation, with Aduanera authorization + duty payment valued at "el método del último recurso previsto en el Acuerdo Relativo a la Aplicación del Artículo VII del GATT 1994"; c) muestrarios/instructivos/patrones/modelos; vehicles excluded without prior Aduanera dictamen; unauthorized sale/transfer to the national market = infraction: guarantee execution + multa of 100% of the tributary debt; per-importation GARANTÍA to the Aduanera for the totality of suspended duties — pagaré, certificado de depósito, prenda aduanera, inmueble, fianza, póliza, cash deposit, certified check, bank guarantee, or combination — "Derecho Preferente a favor del Estado... de Ejecución Inmediata"; guarantee caducidad: a) reexport within legal term; b) nationalization or reexport; c) voluntary abandonment | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 30 pp.13-15 (EV05:EVID-064) |
| LB-005 | Ley de Eficiencia, E-Arts 31-34 (Art. 31 reformed D. 124-2013; Art. 32 derogated with D. 314-98 tourism Art. 5.1) | Special-tax-regime companies (export-incentive laws) may sell to the national market EXCEPT "empresas comerciales básicamente de reexportación" which may destine ≤50% of sales nationally; taxes due "de conformidad al régimen impositivo vigente a la fecha de aceptación de la Declaración única Aduanera (DUA)", Aduanera verifies per risk analysis; the importer is additionally subject to ISR + internal + municipal taxes; donations to the public sector per DEI reglamento (Art. 31); Art. 33 NO SIMULTANEIDAD: beneficiaries "no podrán acogerse simultáneamente a dos o más Leyes de Fomento a las Exportaciones o Regímenes Suspensivos" — RIT, Turismo, Zonas Libres, ZIP, Zonas Agrícolas, Zona Libre Turística Islas de la Bahía, Depósitos de Aduana, Depósitos Temporales, Tiendas Libres; Art. 34 DECLARACIÓN DE SACRIFICIO FISCAL: beneficiaries of exemptions/exonerations or special regimes "deben presentar la declaración de sacrificio fiscal, en la forma, medios y plazos que... apruebe la Administración Tributaria" | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Arts 31-34 pp.15-16 (EV05:EVID-065) |
| LB-006 | Ley de Eficiencia, E-Arts 18-19 | Art. 18: payments of firm judicial sentences to private parties have the corresponding taxes deducted per AT/Aduanera liquidation, "se exceptúan... las prestaciones laborales"; no sentence payment without AT solvencia certification. Art. 19 SOLVENCIA: no public institution may contract goods/services > L25,000.00 with non-solvent suppliers; Constancia de Solvencia issued within 3 días hábiles | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Arts 18-19 p.10 zone (EV05:EVID-060) |
| LB-007 | Ley de Eficiencia, E-Art 23 | Claims against the State for interest, daño emergente or lucro cesante require a certification by a CNBS-registered auditor firm that the amounts are BOOKED AND DECLARED — interpreted by CT D. 170-2016 Art. 211 num. 4)a): NOT applicable when the claim is of TRIBUTARIA/IMPONITIVA nature (R-H14) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 23 p.11 zone (EV05:EVID-060; R-H14 CT 211.4.a) |
| LB-008 | Ley de Eficiencia, E-Art 10 — **VOID / DEAD TEXT (R-H4)**; E-Art 5 — **VOID (R-H3, kin 06-file)** | Art. 10 (budget transfers with the full object-code list) DECLARED UNCONSTITUTIONAL (RI-0763-2021, 25-mar-2021) — dead rows, never feed; Art. 5 (ISV credit non-refundable / closure-consolidation to fisco) likewise VOID — its dead-text guard is owned by `06_isv.md`, recorded here for the Eficiencia dead-text map only | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 10 pp.5-7 (EV05:EVID-060); E-Art 5 p.3 (EV05:EVID-059) |
| LB-009 | Ley de Eficiencia — corpus-identity finding (R-H8) | Header: "TEXTO CONSOLIDADO... Según Decretos: 261-2011, 278-2013, 124-2013, 170-2016 y 7-2017 y Sentencia de Inconstitucionalidad... Enero, 2022"; in-line annotations: Arts. 5/10/20 "(DECLARADO INCONSTITUCIONAL)" per RI-0763-2021 of 25-mar-2021; Arts. 13/20/32/41/42 derogated. META: the source-registry gloss ("impuesto mínimo/solidario") does NOT match the content (that law contains NEITHER — those live in 22-A and the D. 51-2003 family); 4th title-vs-content mislabel — content read end-to-end is the authority, never the registry title/gloss | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | whole file; registry row + inventory (EV05:EVID-067; R-H8) |
| LB-010 | D. 7-2026 — AMNISTÍA TRIBUTARIA (La Gaceta 37,069, 13-feb-2026) — **[W11 ANNOTATION: its Art. 7 (the 4-month SAR general amnistía, 13-feb→~13-jun-2026) is DEROGATED by D.L. 78-2026 (G 37,166 12-jun-2026) and succeeded same-day by 78-2026 Art. 1 — see LB-013; the municipal/ENEE/vehicular legs were re-granted by the 44-2025/78-2026 chain, EVID-653/657]** | One-time amnesty — municipal 3-month window; ENEE arrears; vehicle regularization L10,000 pre-2010; ancillary, not a rate reform; enters ONLY as dated config rows per D-H2.6 (valid_from = instrument vigencia), crossref — no engines in this file | `hn/sources/06_Decreto_7-2026_G37069.pdf` | Gaceta 37,069 13-feb-2026 (registry row `06_`; no EVID — config crossref) |
| LB-011 | **Turismo family — ALL THREE ACQUIRED W8** (`124_` D. 314-98 G 28,847 23-abr-1999 + `125_` D. 135-2006 G 31,168 30-nov-2006 + `126_` D. 68-2017 G 34,419 17-ago-2017; EVID-460..467): D. 68-2017 Art. 5 = the CURRENT benefit stack — (1) 15-year IMPRORROGABLE exoneration ISR + ATN + AS y sus Conexos; (2) 5-year ISR-and-retentions exemption on project services/honorarios; (3) 10-year ISV-free local purchases (IHT-calified); (4) Ley de Aduanas machinery/equipment benefits; (5) 10-year DAI + ISC + aranceles import exoneration (electronic/security/modernization fees carved out); benefits PERSONALÍSIMOS; Art. 4 migration = new investments post-D. 278-2013 qualify by crediting investment + RENOUNCING the prior regime (35%-NPV re-qualification gate); Art. 6 obligations (Registro de Exonerados annual renewal; Declaración Jurada de Sacrificio Fiscal; ISV + Tasa Turística collection); Art. 25 DEROGATES D. 314-98 (+ZOLITUR-interleaved clause, 126_ OQ-3) with acquired-rights saving; Art. 23 reglamento mandate (= Acuerdo 618-A-2017, G 34,486 8-nov-2017 — unacquired lead); 125_ = the cruise-terminal class (10-yr ISR+ISV+any-tax RENEWABLE, ≥USD5M, ENP exemptions, municipal 0.25% volumen factor — HISTORICAL post-derogation, acquired-rights edge 126_ OQ-5) | The turismo cluster's statutory basis: 314-98-era rows = HISTORICAL (valid_to 17-ago-2017); the current stack = D. 68-2017 dated rows (valid_from 17-ago-2017); the ATN/AS-exoneration leg cross-confirms both Cap. II taxes live in the FY2017+ world (121_/EVID-444-449 kin); E-Art 33's no-simultaneidad catalog still governs Turismo enrollment | `hn/sources/126_Gaceta_34419_Decreto_68-2017_Ley_Fomento_Turismo.pdf` + `hn/sources/124_Gaceta_28847_Decreto_314-98_Ley_Incentivos_Turismo.pdf` + `hn/sources/125_Gaceta_31168_Decreto_135-2006_Adicion_Art5_314-98.pdf` | 68-17-Arts. 4-6 pp.2-4; Art. 25 p.9 (EV126:EVID-464..467; EV124:EVID-460..462; EV125:EVID-463) |
| LB-012 | **W9 exonerations-frame additions** — D. 278-2013 (`130_`, G 33,316 30-dic-2013, vigencia 01-ene-2014): Arts. 1-2 = the GREAT exonerations derogation + 24-numeral survival catalogue (incl. #13 Adulto Mayor D. 199-2006 Arts. 33/36; #17 LSP + D. 199-2011 fideicomiso; #18 RIT/ZOLI/LIT); Art. 5 = the ISR-side 17-numeral exceptions (jubilados #10, adulto mayor #11, gremiales #12, ZOLI/ZIP #8); Arts. 22-27 = the control frame (12-year default cap; registration before benefit; DGCFIA single window; CT-Art.-121 + 4-SMM sanction); Art. 49 derogations (D. 194-2002 Art. 48; CT Art. 464; D. 17-2010 Arts. 40/63; LIT Art. 5.1). + **Acuerdo 462-2014 ACQUIRED** (`131_`, G 33,484 21-jul-2014 — the Art.-50 reglamento): the exonerations SURVIVAL inventory operative (25 numerals), Declaración de Sacrificio Fiscal procedure, Registro de Beneficiarios; its Art. 20 valid_to 4-dic-2018 (Acuerdo 817-2018). + **Acuerdo 618-A-2017 ACQUIRED** (`143_`, G 34,486 8-nov-2017): the D. 68-2017 reglamento (LB-011's lead closed — incentive procedures, exoneration mechanics; edition carries other content first, EV143 inventory). + D. 74-2014 (`132_`): Ley-Art. 5 num. 11 authentic interp (the 65+ exoneration survives — taxation/02 LB-018) | The 2013-14 exonerations RESET now statute-complete at both law and reglamento levels: survival-catalogue rows, the 12-year cap, registration gates and the Sacrificio-Fiscal procedure are encodable as dated rows (valid_from 01-ene-2014 / reglamento 21-jul-2014); LIT Art. 5.1 derogated = the D. 68-2017 stack's clean start corroborated | `hn/sources/130_Gaceta_33316_Decreto_278-2013_Ley_Ordenamiento_Finanzas_Publicas.pdf` + `hn/sources/131_Gaceta_33484_Acuerdo_462-2014_Regl_Ley_Ordenamiento.pdf` + `hn/sources/143_Gaceta_34486_Acuerdo_618-A-2017_Regl_Ley_Fomento_Turismo.pdf` | EV130:EVID-483/484/491; EV131:EVID-492..499; EV143:EVID-536..540 |
| LB-013 | **W11 — the 2025-2026 amnistía package, SAR side** — `163_` **D.L. 44-2025** (G 36,861 mié 11-jun-2025; Dado 3-jun-2025, Ejecútese 10-jun-2025, vigencia = publication day): the seven-amnistía architecture — municipal (Art. 1: mora ≤31-dic-2024, window →30-sep-2025, ≤1-year municipal plans; the D. 5-2024 successor), IHSS (Art. 2 — payroll/03 LB-022), ENEE (Art. 3), vehicular IP-FY2024-back (Art. 4), HONDUTEL (Art. 5, incl. public-sector compensation), SANAA (Art. 6); considerando restates **CT-Art.-2.4's amnistía definition** (accessory obligations only — the principal always survives) with a digit-slip ("Decreto No.70-2016" for the CT's 170-2016, dates garbled — flagged EVID-651). `164_` **D.L. 78-2026** (G 37,166 vie 12-jun-2026; Dado 13-may-2026, Ejecútese 15-may-2026, vigencia 12-jun-2026) the AMPLIACIÓN: **Art. 1 = the CURRENT SAR general amnistía — 4-month window 12-jun-2026→12-oct-2026**, multas/recargos/intereses exonerated on obligations (formal AND material) ≤31-dic-2025, CONDITIONAL on paying the tributos pendientes per the applicable law's deadlines; **Art. 7 of D. 7-2026 (06_) DEROGATED** (same-day successor — no gap); Arts. 3-4 re-grant municipal + servicios | The SAR-side amnistía dated-config rows (D-H2.6 class, never engines): 06_-Art.-7 rows now valid_to 12-jun-2026 (derogated); 78-2026-Art.-1 rows valid 12-jun-2026→12-oct-2026 (amnestied periods cap at FY2025-and-back); the municipal/ENEE/vehicular/HONDUTEL/SANAA legs = amnistía-map inventory only (out of Odoo scope) | `hn/sources/163_Gaceta_36861_Decreto_44-2025_Amnistias.pdf` + `hn/sources/164_Gaceta_37166_Decreto_78-2026_Amnistia_ampliacion.pdf` | EV163:EVID-651/653; EV164:EVID-654/655/657 |

Dead text — never implementable as current law (notes, not FR engines):
E-Art 10 budget transfers (VOID, R-H4 — guard FR-279) and E-Art 5 ISV-credit
closure (VOID, R-H3 — guard owned by `06_isv.md`); E-Art 32 (derogated with
D. 314-98 tourism Art. 5.1); E-Arts 25/26 windows (2011 — historical); the
`05_` registry gloss itself (R-H8 — never a content source, guard FR-280).

## 3. Functional Requirements

### 3.1 Facturación statutory root (reference) & Registro de Exoneraciones lifecycle

- **HN-TAX-FR-256:** The system shall record D. 17-2010 L-Art 57 — which
  *instituye el Régimen de Facturación*, creates the Registro Fiscal de
  Imprentas and mandates the regulation of *la factura electrónica* — as the
  STATUTORY ANCHOR citation only: no facturación engine, document type,
  authorization ledger or emission gate is implemented in this file; every
  such engine is owned by the e-invoicing files (HN-EINV-FR-001..175,
  `../e-invoicing/01..04_*.md`), consumed by cross-reference.
  (LB-001; EV04:EVID-052)
- **HN-TAX-FR-257:** The system shall keep a *Registro de Exoneraciones*
  (exonerations registry) recording the FREE, MANDATORY inscription of every
  beneficiary of exemptions or special regimes, with lifecycle events —
  initial inscription, changes and deregistration — each filed within its
  1-MONTH window, and with the registry enrollment status visible on the
  beneficiary partner record. (LB-002; EV04:EVID-052)
- **HN-TAX-FR-258:** The system shall model the registry's administrative
  states: renewal SUSPENDED until updated (no renewal processing while the
  suspension stands — a dated regime row, re-enabled only by a successor
  instrument), and *de oficio* inscription (registry rows creatable by the
  administration's own motion, flagged as such with their source).
  (LB-002; EV04:EVID-052)
- **HN-TAX-FR-259:** The system shall require, on every exoneración
  enrollment, the PRIOR-AUTHORIZATION chain: an authorization request plus
  the issuing resolution reference carrying the PROJECT DETAIL and the
  APPROXIMATE PURCHASE AMOUNT (L-Arts 42-43), stored as the registry row's
  authorization/resolution snapshot (the input to the FR-264 single-document
  rule). (LB-002; EV04:EVID-052)
- **HN-TAX-FR-260:** The system shall carry the diplomatic-exonerations
  card-operator conventions field (L-Art 41): registry rows for diplomatic
  beneficiaries may reference a card-operator convention record (flag +
  reference; mechanics outside this file — OTCD surfaces = `06_isv.md`
  HN-TAX-FR-211..255 kin). (LB-002; EV04:EVID-052)

### 3.2 Exonerations discipline (Eficiencia E-Arts 27-29)

- **HN-TAX-FR-261:** The system shall enforce the *personalísimas* rule:
  exemptions/exonerations are strictly personal to the beneficiary — every
  transfer-to-third-party provision is *expresamente derogada*, so no
  exoneración flag, rate suppression or registry status shall propagate,
  assign or be lent to any third party (the exonerated flags on
  partners/products of §4 carry beneficiary identity, never a transferable
  class). (LB-003; EV05:EVID-063)
- **HN-TAX-FR-262:** The system shall implement the exonerated-asset disposal
  trigger: on ENAJENACIÓN of an exonerated VEHICLE to a non-exempt third
  party, the disposal shall *regularizar el pago de tributos* — the
  suspended/exonerated taxes are liquidated and paid AT THAT MOMENT, a
  blocking tax-regularization step on the disposal flow (valuation basis
  unpinned → §7 OQ-006 kin). (LB-003; EV05:EVID-063)
- **HN-TAX-FR-263:** The system shall validate the in-kind-only rule for
  FOREIGN DONATIONS: donations from abroad to registered private voluntary
  organizations are exonerated *sólo cuando éstas sean recibidas en especie* —
  a cash foreign donation shall NOT receive the exoneración treatment (goods-
  only validation on the donation receipt: in-kind = eligible, cash =
  excluded). (LB-003; EV05:EVID-063)
- **HN-TAX-FR-264:** The system shall implement the SEFIN single-document
  principle: the SEFIN resolution (issued on a solvent beneficiary) "será el
  documento suficiente para acreditar la exoneración" — no State institution
  may demand any other document — so the registry row's SEFIN resolution
  reference (FR-259) is the SOLE exoneración credential consumed by every
  downstream surface (invoices, customs, DUA), each recording only a
  reference to it, never a second tramitation. (LB-003; EV05:EVID-063)
- **HN-TAX-FR-265:** The system shall encode the exoneración solvency
  semantics per the CT Art. 211 num. 4)b) interpretation (R-H14): the
  beneficiary's required solvency reaches obligations OTHER than the
  *dispensa del pago de tributos solicitados* — delinquency consisting SOLELY
  of the tax being exonerated shall NOT block the exoneración (the solvencia
  test excludes the requested dispensa itself). (LB-003; EV05:EVID-063; R-H14)

### 3.3 RIT — Régimen de Importación Temporal (E-Art 30)

- **HN-TAX-FR-266:** The system shall model RIT as SUSPENSION of import
  duties on three eligible goods classes: (a) raw materials, semi-elaborates,
  *envases/empaques* and inputs for exported goods or services; (b)
  machinery, equipment, molds, tools, spares and accessories used
  EXCLUSIVELY for export production; (c) *muestrarios, instructivos,
  patrones, modelos* — each RIT import record carrying its class; VEHICLES
  are excluded without a prior Aduanera *dictamen* reference on the record.
  (LB-004; EV05:EVID-064)
- **HN-TAX-FR-267:** The system shall require, per importation, a GUARANTEE
  to the Aduanera for the TOTALITY of the suspended duties, accepting the
  statutory instrument catalog — *pagaré, certificado de depósito, prenda
  aduanera, inmueble, fianza, póliza,* cash deposit, certified check, bank
  guarantee, or combination — recording the State's *Derecho Preferente...
  de Ejecución Inmediata* as the guarantee's enforcement attribute.
  (LB-004; EV05:EVID-064)
- **HN-TAX-FR-268:** The system shall release (mark *caducada*) an RIT
  guarantee on any of the statutory caducidad events: (a) reexport within the
  legal term; (b) nationalization or reexport; (c) voluntary abandonment —
  each event closing the guarantee and the import record's suspended-duty
  exposure with it. (LB-004; EV05:EVID-064)
- **HN-TAX-FR-269:** The system shall enforce the 5-YEAR DISPOSAL GATE for
  class-(b) goods: machinery/equipment/molds/tools/spares/accessories are
  *enajenable* only AFTER 5 years from importation, with Aduanera
  authorization plus payment of the duties valued at *el método del último
  recurso previsto en el Acuerdo Relativo a la Aplicación del Artículo VII
  del GATT 1994* (disposal-eligibility date = importation + 5 years,
  snapshotted; pre-gate disposal attempts blocked). (LB-004; EV05:EVID-064)
- **HN-TAX-FR-270:** The system shall implement the diversion infraction:
  unauthorized sale or transfer of RIT goods to the NATIONAL MARKET triggers
  (a) execution of the FR-267 guarantee for the suspended duties and (b) a
  multa of 100% of the tributary debt — both recorded as infraction entries
  on the RIT import record. (LB-004; EV05:EVID-064)
- **HN-TAX-FR-271:** The system shall load the RIT reexport periods as DATED
  config rows set by the administration PER INDUSTRY CYCLE (DEI-era
  designation as printed — administration mapping is config, §7 OQ-005),
  resolving each import record's reexport deadline from the row in force at
  its importation date (D-H2; never "today"); the D. 2-2026 RIT extension is
  UNACQUIRED — window changes enter only when its rows land (LEAD, §7
  OQ-004). (LB-004; EV05:EVID-064)
- **HN-TAX-FR-282:** (W8) The system shall load the tourism-incentive
  stack as DATED regime rows (D-H2.6): (a) HISTORICAL set valid
  1999-04-23 → 2017-08-16 (D. 314-98 as amended by D. 135-2006 + D.
  17-2010 L-Arts 5/8): 10-year ISR new-projects exoneration, import
  exonerations, the cruise-terminal renewable class; (b) CURRENT set
  valid from 2017-08-17 (D. 68-2017): 15-yr ISR+ATN+AS-conexos
  improrrogable, 5-yr services-retentions exemption, 10-yr ISV local
  purchases, 10-yr import exoneration — with the migration rule (prior
  regime RENUNCIATION credited at enrollment; ≥35%-NPV improvements
  re-qualify existing operators), the personalísimo non-transferability
  guard, and the annual Registro-de-Exonerados renewal +
  Sacrificio-Fiscal DJ as enrollment-linked compliance events (LB-011;
  EV126:EVID-465/466; EV124:EVID-460..463)

### 3.4 Special-regime invariants (E-Arts 31-34)

- **HN-TAX-FR-272:** The system shall stamp the tax point of a special-regime
  company's NATIONAL-MARKET sales at the DUA ACCEPTANCE DATE: taxes are due
  *de conformidad al régimen impositivo vigente a la fecha de aceptación de
  la Declaración única Aduanera (DUA)* — regime rows resolved by that date
  (D-H2), the importer additionally flagged subject to ISR + internal +
  municipal taxes on those sales; donations to the public sector follow the
  DEI reglamento (unacquired — pointer only). (LB-005; EV05:EVID-065)
- **HN-TAX-FR-273:** The system shall monitor the reexporter cap:
  *empresas comerciales básicamente de reexportación* may destine at most 50%
  of their sales to the national market — a rolling national-vs-total sales
  ratio per regime period FLAGGING any breach above 50% (compliance monitor;
  the sanction consequence runs on the CT/T11 frame, cited not restated).
  (LB-005; EV05:EVID-065)
- **HN-TAX-FR-274:** The system shall enforce NO-SIMULTANEIDAD: a
  beneficiary *no podrá acogerse simultáneamente a dos o más Leyes de Fomento
  a las Exportaciones o Regímenes Suspensivos* — the regime-enrollment
  entity shall reject a second concurrent enrollment in the statutory catalog
  (RIT · Turismo · Zonas Libres · ZIP · Zonas Agrícolas · Zona Libre
  Turística Islas de la Bahía · Depósitos de Aduana · Depósitos Temporales ·
  Tiendas Libres), strictly one active row per beneficiary per date (D-H2
  dated enrollment; successive enrollment requires terminating the prior
  row). (LB-005; EV05:EVID-065)
- **HN-TAX-FR-275:** The system shall carry the *declaración de sacrificio
  fiscal* duty: every beneficiary of exemptions/exonerations or special
  regimes *debe presentar la declaración de sacrificio fiscal, en la forma,
  medios y plazos que... apruebe la Administración Tributaria* — a per-FY
  filing calendar entity flagging the duty for every active
  exoneración/regime row (form/layout = S-HN3 surface; plazos unpinned → §7
  OQ-006). (LB-005; EV05:EVID-065)

### 3.5 State-side rules (E-Arts 18-19, 23)

- **HN-TAX-FR-276:** The system shall implement the L25,000 solvencia gate:
  no public institution may contract goods or services for more than
  L25,000.00 with a NON-SOLVENT supplier — on sales to State-institution
  customers above L25,000, the system shall require the customer-side
  solvencia status (the *Constancia de Solvencia* being issuable within 3
  días hábiles — an SLA field, not a computation); vendor-side gate depth =
  product decision (§7 OQ-008). (LB-006; EV05:EVID-060)
- **HN-TAX-FR-277:** The system shall implement the sentencia-payment
  retention: payments of firm judicial sentences to private parties carry
  the corresponding taxes DEDUCTED per the AT/Aduanera liquidation — *se
  exceptúan... las prestaciones laborales* (labor-prestación components are
  exempt from the deduction) — and NO sentence payment shall process without
  the AT solvencia certification reference. (LB-006; EV05:EVID-060)
- **HN-TAX-FR-278:** The system shall implement the E-Art 23 claims
  certification boundary: claims against the State for interest, *daño
  emergente* or *lucro cesante* require a CNBS-registered auditor-firm
  certification that the amounts are BOOKED AND DECLARED (evidence reference
  on the claim record) — EXCEPT claims of *tributaria/impositiva* nature,
  which per CT 211.4.a (R-H14) shall NOT be gated by the certification.
  (LB-007; EV05:EVID-060; R-H14)

### 3.6 Dead-text, provenance & config-crossref guards

- **HN-TAX-FR-279:** The system shall NEVER compute or feed any E-Art 10
  budget-transfer rule: the article is VOID (RI-0763-2021; R-H4) — recorded
  as dead rows only, no engine, no config feed; same discipline for the
  E-Art 5 VOID text whose guard is owned by `06_isv.md` (dead-text map, not
  restated). (LB-008; EV05:EVID-060; R-H4)
- **HN-TAX-FR-280:** The system shall enforce the source-provenance rule
  (R-H8 meta): every statutory config row created from the Eficiencia family
  (and this file's catalogs generally) shall carry a
  `source_article_key` pointing at the ARTICLE TEXT read end-to-end — rows
  keyed only to a source-registry title or gloss shall be REJECTED at
  validation (title ≠ content; 05_'s catalog gloss named the wrong law
  entirely). (LB-009; EV05:EVID-067; R-H8)
- **HN-TAX-FR-281:** The system shall carry the amnistía D. 7-2026 as DATED
  CONFIG ROWS ONLY (D-H2.6): municipal 3-month window, ENEE arrears and
  vehicle-regularization L10,000/pre-2010 rows with valid_from 13-feb-2026 —
  crossref surface, window-scoped, never an engine of this file (expiry
  backfilled when the window instrument's successor lands).
  (LB-010; D-H2.6 dated-row rule; no EVID anchor — config-structure FR
  whose LB-010 is itself the instrument crossref: controller waiver
  granted at V-HN1, the only such row in this topic)

## 4. Data Model

No dated numeric tables of this cluster are machine-read at this wave (RIT
industry-cycle periods, sacrificio-fiscal plazos and the amnistía windows are
config rows; CSV sidecar deferred to implementation per the
`05_d17-2010-family.md` §4 discipline). Layer: Odoo-side
bookkeeping/status data only (wave default `odoo`; see §5).

**Registro de Exoneraciones + exonerations discipline:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.exoneration.registry (new) | beneficiary_partner_id, regime_benefit_class, enrolled_on, state | m2o/select/date/select | regime_benefit_class: exemption · exoneration · special_regime · diplomatic; state: active · change_pending · suspended_renewal · deregistered · de_oficio_enrolled | FR-257, FR-258 |
| l10n_hn.exoneration.registry | lifecycle_window_due, window_type | date/select | window_type: initial · change · deregistration — each due within 1 month of its triggering event | FR-257 |
| l10n_hn.exoneration.registry | authorization_ref, resolution_ref, resolution_date, project_detail, approximate_purchase_amount, card_operator_convention_ref | char/date/monetary | the L-Arts 42-43 prior-authorization chain + L-Art 41 diplomatic convention reference | FR-259, FR-260 |
| l10n_hn.exoneration.registry | sefin_resolution_ref (single credential), solvency_scope | char/select | solvency_scope = other_obligations_only (CT 211.4.b — the dispensa itself excluded from the test) | FR-264, FR-265 |
| res.partner | hn_exonerated, hn_exoneration_registry_id, hn_personalissima (non-transferable marker, always true when exonerated) | boolean/m2o | exoneración flags on the BENEFICIARY partner only — never transferable (personalísimas) | FR-261 |
| product.template / asset record | hn_exonerated_vehicle, hn_disposal_regularization_due | boolean/date | exonerated-vehicle flag; disposal trigger opens the tax-regularization blocking step | FR-262 |
| account.move (donation receipt) | hn_foreign_donation, hn_donation_in_kind, opv_registry_ref | boolean/m2o | foreign donations: in-kind = eligible; cash = excluded; registered private voluntary organization reference | FR-263 |

**RIT tracked-goods register (proposals):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.rit.import (new) | import_date, goods_class, product/tracking lot links (stock.lot), reexport_deadline | date/select/m2o/date | goods_class: a_inputs_export · b_machinery_exclusive_export · c_muestrarios; vehicles require aduanera_dictamen_ref else blocked; reexport deadline resolved from the dated industry-cycle row in force at import_date (D-H2) | FR-266, FR-271 |
| l10n_hn.rit.import | suspended_duties_total, disposal_eligible_date, disposal_authorization_ref, gatt_last_resort_valuation | monetary/date/char/monetary | disposal_eligible_date = import_date + 5 years (class b); GATT Art. VII last-resort valuation snapshot on disposal | FR-269 |
| l10n_hn.rit.import | diversion_infraction, multa_100pct_amount, guarantee_executed | boolean/monetary | unauthorized national-market diversion: guarantee execution + multa = 100% of the tributary debt | FR-270 |
| l10n_hn.rit.guarantee (new) | rit_import_id, instrument_type, coverage_amount, state, caducidad_event, preferential_immediate | m2o/select/monetary/select/boolean | instrument_type: pagaré · certificado_de_depósito · prenda_aduanera · inmueble · fianza · póliza · cash_deposit · certified_check · bank_guarantee · combination; caducidad_event: reexport_within_term · nationalization_or_reexport · voluntary_abandonment | FR-267, FR-268 |
| l10n_hn.tax.parameter (reused) | parameter, value, valid_from, valid_to, source_article_key | mixed/date/char | rit_reexport_period rows per industry cycle (administration-set, dated); amnistía D. 7-2026 window rows (crossref) | FR-271, FR-281 |

**Regime invariants + state-side:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.regime.enrollment (new) | beneficiary_partner_id, regime, valid_from, valid_to | m2o/select/date | regime catalog: RIT · Turismo · Zonas Libres · ZIP · Zonas Agrícolas · Zona Libre Turística Islas de la Bahía · Depósitos de Aduana · Depósitos Temporales · Tiendas Libres; ONE active row per beneficiary per date (no-simultaneidad constraint) | FR-274 |
| l10n_hn.sacrificio.calendar (new) | fiscal_year, due_date, filed_ref, beneficiary_scope | year/date/char | per-FY filing-duty rows for every active exoneración/regime beneficiary; due dates = AT-approved (unpinned → OQ-006); form = S-HN3 | FR-275 |
| res.partner (State-institution customer) | hn_state_institution, hn_solvency_status, constancia_sla_days, constancia_ref | boolean/select/integer/char | L25,000 gate: solvency_status: solvent · non_solvent · pending (constancia within 3 días hábiles SLA) | FR-276 |
| account.payment (sentencia) | hn_judicial_sentence_payment, tax_deduction_amount, labor_prestacion_component (excluded), at_solvencia_cert_ref | boolean/monetary/monetary/char | sentence payments: taxes deducted per AT/Aduanera liquidation; prestaciones laborales carve-out; AT solvencia precondition reference | FR-277 |
| account.move.line (claim vs State) | hn_state_claim_class, cnbs_certification_ref | select/char | claim_class: interest · daño_emergente · lucro_cesante (certification required) · tributaria (NOT required — R-H14 carve-out) | FR-278 |
| l10n_hn.tax.parameter (dead rows) | parameter, status | mixed/select | eficiencia_art_10 rows status = historical_dead (VOID R-H4); never selectable | FR-279 |
| l10n_hn.* config rows (all) | source_article_key | char | R-H8 provenance: mandatory article-text key; gloss/title-only rows rejected at validation | FR-280 |

## 5. Odoo Mapping

Layer semantics: `odoo` = computation/bookkeeping/status logic in the LGPL
client; no SaaS rows (HN's only architecture-split surface is the SEE channel
— blocked on unpublished docs, W3 E8 lead 1 — untouched by this file). Model
names stable across Odoo 17/18/19/20; vintages recorded per row.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-256 | odoo | documentation/config metadata | statutory-anchor citation | Reference row only; engines = e-invoicing files HN-EINV-FR-001..175 (crossref by range) |
| FR-257, FR-258 | odoo | l10n_hn.exoneration.registry | state, lifecycle windows | Renewal suspension = dated regime row (re-enabled by successor instrument only); de-oficio flag carries source |
| FR-259, FR-260 | odoo | l10n_hn.exoneration.registry | authorization/resolution snapshot, convention ref | Approximate purchase amount snapshotted at resolution (D15); feeds FR-264 single-credential consumption |
| FR-261, FR-262 | odoo | res.partner + product/asset flags + disposal flow | beneficiary-bound exoneración flags; disposal_regularization_due | Personalísimas: no propagation path by design, transfer attempts flag an error; exonerated-vehicle disposal blocked until tax regularization (valuation input = config, OQ-006 kin) |
| FR-263, FR-264 | odoo | account.move (donation) + l10n_hn.exoneration.registry | in-kind validation; sefin_resolution_ref | Cash foreign donations never exonerated; single credential — the e-invoicing exonerado print registers (OCE/CRE/SAG, HN-EINV-FR-100..140 zone) reference it, never duplicate (OQ-007) |
| FR-265 | odoo | registry solvency check | solvency_scope | CT 211.4.b semantics: dispensa itself excluded from the solvency test (R-H14) |
| FR-266 | odoo | l10n_hn.rit.import + stock.lot | goods_class, dictamen gate | Tracked-goods register proposal: stock tracking (lot/serial) available unchanged 17-20 |
| FR-267..FR-270 | odoo | l10n_hn.rit.guarantee + l10n_hn.rit.import | instrument catalog, caducidad, disposal gate, infraction | Coverage = totality of suspended duties (preferential-immediate execution); +5-year disposal gate with GATT last-resort valuation snapshot (D15); diversion = guarantee execution + 100% multa (sanctions frame = T11, cited) |
| FR-271 | odoo | l10n_hn.tax.parameter | rit_reexport_period rows | D-H2: resolved by importation date, never "today"; D. 2-2026 extension = LEAD (OQ-004); administration designation = config (OQ-005) |
| FR-272, FR-273 | odoo | l10n_hn.regime.enrollment + sales reporting | dua_acceptance stamp, national-sales ratio | Regime rows resolved by DUA acceptance date (D-H2); ISR/internal/municipal flags; rolling ≤50% reexporter monitor (breach flag only — consequence = CT frame) |
| FR-274 | odoo | l10n_hn.regime.enrollment | single-active constraint | SQL/ORM constraint: one active regime row per beneficiary per date; successive enrollment requires prior termination |
| FR-275 | odoo | l10n_hn.sacrificio.calendar | per-FY duty rows | Due dates = AT-approved (OQ-006); declaration form/layout = S-HN3 surface |
| FR-276, FR-277 | odoo | res.partner (State customer) + account.payment | solvencia status/constancia SLA; sentence retention fields | L25,000 gate + 3-días-hábiles constancia SLA (vendor-portal depth = OQ-008); AT/Aduanera liquidation deduction with prestaciones laborales carve-out; AT solvencia precondition |
| FR-278 | odoo | account.move.line (claims) | certification gate + carve-out | CNBS certification ref required for non-tributaria claims; tributaria claims bypass (R-H14) |
| FR-279..FR-281 | odoo | l10n_hn.tax.parameter + config-row validation | dead rows; source_article_key; amnistía window rows | E-Art 10 VOID (R-H4) historical_dead, never selectable; R-H8 provenance rule (article-text key mandatory, gloss/title-only rejected); amnistía rows valid_from 13-feb-2026, crossref only (D-H2.6) |

Version-regime notes (D-H2/D12): FR-258 (renewal suspension), FR-271 (RIT
industry-cycle periods) and FR-281 (amnistía windows) are dated-row regimes —
additive-only, resolved by the record's own date, `valid_to` backfilled only
when a successor instrument arrives; FR-274 enrollments are dated rows with
the single-active constraint evaluated per date; FR-269/FR-272 snapshots are
write-time (D15). Odoo 17/18/19/20: no version-specific behavior — custom
models/fields and stock tracking are version-stable.

## 6. Acceptance Criteria

- **AC-001:** Given a beneficiary newly granted an exemption on 05-mar-2026,
  when the registry row is created, then it is active with the 1-month window
  due 05-abr-2026 and the resolution reference, project detail and
  approximate purchase amount snapshotted (FR-257, FR-259).
- **AC-002:** Given a renewal request while the renewal-suspension row is in
  force, then renewal processing is blocked; given an
  administration-originated enrollment, then the row carries the de-oficio
  source flag (FR-258).
- **AC-003:** Given an attempt to copy or assign an exoneración flag from a
  beneficiary partner to a third party, then the operation is rejected —
  personalísimas, no transfer path exists (FR-261).
- **AC-004:** Given the enajenación of an exonerated vehicle to a non-exempt
  buyer, then the disposal cannot complete until the tax-regularization step
  liquidates the exonerated taxes at that moment (FR-262).
- **AC-005:** Given a foreign donation of goods (in-kind) to a registered
  private voluntary organization, then the exoneración applies; given the
  same donation in cash, then it is denied (FR-263).
- **AC-006:** Given a registry row with its SEFIN resolution recorded, when
  any downstream surface (invoice, DUA) consumes the exoneración, then it
  records only a reference to that single document, never a second
  tramitation (FR-264).
- **AC-007:** Given an exoneration applicant whose ONLY delinquency is the
  very tax covered by the requested dispensa, then the solvency test passes —
  the dispensa itself is excluded per CT 211.4.b (FR-265).
- **AC-008:** Given an RIT importation of class-(b) machinery with suspended
  duties of L400,000, then a guarantee covers exactly the L400,000 totality
  with a statutory instrument type and the immediate-execution attribute
  (FR-266, FR-267).
- **AC-009:** Given an RIT importation of a vehicle without an Aduanera
  dictamen reference, then RIT processing is blocked; given the dictamen
  present, then it proceeds (FR-266).
- **AC-010:** Given a class-(b) RIT import dated 10-jun-2024, then
  disposal_eligible_date = 10-jun-2029; a 2027 disposal is blocked; a 2029+
  disposal requires the Aduanera authorization + GATT valuation snapshot
  (FR-269).
- **AC-011:** Given unauthorized diversion of RIT goods with suspended duties
  L400,000 to the national market, then the infraction entries compute the
  guarantee execution for L400,000 and a multa of 100% = L400,000.00
  (FR-270).
- **AC-012:** Given reexport within the legal term, then the guarantee is
  marked caducada (reexport_within_term) and the suspended-duty exposure
  closes; likewise nationalization and voluntary abandonment (FR-268).
- **AC-013:** Given a reexporter (*empresa comercial básicamente de
  reexportación*) with national sales of 55% of total in the regime period,
  then the ≤50% monitor flags the breach (FR-273).
- **AC-014:** Given a beneficiary with an active RIT enrollment on
  01-may-2026, when a Zonas Libres enrollment is attempted with overlapping
  validity, then the constraint rejects it — admitted only after the RIT
  row's valid_to (FR-274).
- **AC-015:** Given a national-market sale by a special-regime company whose
  DUA was accepted 15-mar-2026, then the applicable regime rows are those in
  force on 15-mar-2026 (not sale/computation date), with the ISR/internal/
  municipal exposure flags asserting (FR-272).
- **AC-016:** Given FY2026 with an active exoneración beneficiary, then the
  sacrificio-fiscal calendar carries the per-FY duty row, pending until a
  filing reference lands (form/plazo config per OQ-006) (FR-275).
- **AC-017:** Given a State-institution customer contracting L30,000 >
  L25,000 with a non_solvent supplier, then the gate flags/blocks per the
  configured depth and the constancia SLA field records the 3-días-hábiles
  window (FR-276).
- **AC-018:** Given a firm-sentence payment of L100,000 where L40,000 is
  prestaciones laborales, then the tax deduction applies per the AT/Aduanera
  liquidation on the non-labor L60,000 only, with the AT solvencia
  certification required to process (FR-277).
- **AC-019:** Given a claim vs the State for lucro cesante, then the record
  demands the CNBS-auditor certification reference (booked-and-declared);
  given a tributaria-nature claim, then no certification gate applies
  (R-H14) (FR-278).
- **AC-020:** Given any computation or config feed referencing Eficiencia
  E-Art 10, then it yields nothing — historical_dead rows (VOID, R-H4); and
  given a config row keyed only to a registry title or gloss, then validation
  rejects it (R-H8) (FR-279, FR-280).
- **AC-021:** Given the amnistía D. 7-2026 rows, then they exist only as
  dated config rows valid_from 13-feb-2026 with no engine of this file
  consuming them beyond window-scoped crossref (FR-281).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Eficiencia consolidation vintage (origin `05_ OQ-2`, carried): the 05_ print is Enero-2022, reform chain footnoted only through D. 7-2017 + the 2021 sentencia annotations — post-2017/2022 reforms (if any) unverified per-article. Every FR citing E-Arts 18-19/23/27-34 carries the caveat; verify against a fresher consolidation/gazette chain before freezing config. | no | Takumi S-HN1 (acquisition queue) | open |
| OQ-002 | SEFIN devolution procedure (origin `05_ OQ-5`, carried): the SEFIN procedure for returning wrongly-retained amounts to 65+ ≤L350k exemptees (D. 59-2020 Art. 2 final para) is not in corpus — LEAD; the mandate is citable meanwhile (deduction/exemption engines = `02_isr-deductions.md` FR-066..068 kin; devolution workflow = pointer only). | no | acquisition queue | open (LEAD) |
| OQ-003 | Exonerations-reglamento leads (origin `26_ OQ-2`, W3 kin): **462-2014 ACQUIRED W9** (`131_` — LB-012: the survival inventory + Sacrificio-Fiscal procedure + Registro de Beneficiarios; its Art. 20 valid_to 4-dic-2018 per 817-2018; the Art.-28 sub-reglamento and Acuerdo 424-2018 (ITA ISV Art. 15.a) remain unacquired); the ZOLADES/zonas detail = num. 18's reglamento-side content, now partially pinned. | no | acquisition queue (narrowed: 424-2018 + Art.-28 sub-reglamento) | open (narrowed) |
| OQ-004 | RIT D. 2-2026 extension + tourism family: **W8 — the tourism family is ACQUIRED** (`124_`/`125_`/`126_`, LB-011/FR-282; current statute = D. 68-2017, 314-98 derogated 17-ago-2017 with acquired-rights saving; reglamento 618-A-2017 remains unacquired — field-level calificación workflow only). Remaining: D. 2-2026 RIT extension text (FR-271 window rows). | no | acquisition queue (narrowed: D. 2-2026 + 618-A-2017) | open (narrowed) |
| OQ-005 | Reglamento 1121-2010 vintage for R-Arts 44-47 (origin `04_ OQ-2`, kin of `05_d17-2010-family.md` OQ-001): no reglamento consolidation found; R-Arts 44-47 bear no known reform but the 2010 vintage caveat applies. Also: agency designations print DEI/Aduanera (pre-SAR) — the current-administration mapping is config keyed per instrument date, never hardcoded. | no | Takumi S-HN1 (acquisition queue) | open (kin) |
| OQ-006 | Sacrificio-fiscal declaration parameters: the AT-approved forma/medios/plazos (E-Art 34) are not in corpus — due dates, form and channel unpinned (FR-275 calendar rows ship placeholder); S-HN3 owns the declaration surface. Kin: exonerated-vehicle disposal valuation basis at FR-262 is likewise unpinned — config until an instrument lands. | no | Takumi S-HN3 + acquisition queue | open (CONFIG) |
| OQ-007 | Exonerado print-register linkage: the e-invoicing print contract carries three exonerado registers (OCE/CRE/SAG — `../e-invoicing/03_document-mechanics.md`, HN-EINV-FR-100..140 zone) whose subject classes overlap this file's Registro de Exoneraciones; confirm the mapping (which register consumes which regime_benefit_class) at S-HN2/S-HN3 integration so FR-264's single credential is referenced, never duplicated. | no | Takumi S-HN2 + S-HN3 | open |
| OQ-008 | State-side gate depth (DECIDE): the L25,000 solvencia gate (FR-276) binds State institutions as BUYERS — Odoo-side it surfaces as the customer/solvency status on public-sector sales; whether to build a procurement-side blocking gate (Odoo used by a State entity) and a vendor-portal constancia surface is a product decision, not a statutory one. | no | product owner (Takumi) | open (DECIDE) |
