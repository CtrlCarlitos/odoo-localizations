# GT — Taxation — Reform-chain provenance & dated-instrument discipline

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the **provenance layer** of the Guatemala taxation wave as
machine-actionable requirements (cluster TX7 — the D16 instantiation for
taxation): the per-instrument **consolidation-cutoff register** as dated rows
for every taxation instrument in the corpus (23_ D-27-92, 24_ AG 5-2013, 25_
Código Tributario D-6-91, 26_ LAT D-10-2012, 28_ AG 213-2013, 47_ SAT digest,
74_ D-10-2025, 78_ D-20-2006, 79_ AG 425-2006); the **currency-qualifier
rule** (every citation the system emits carries its consolidation cutoff);
the **citation guards** (IVA statutory layer never cited alone; ISR = LAT
D-10-2012, never Dto. 26-92; form numbers cite 48_/RetWeb, never 78_/79_);
the binding **myths list enforced as validation rules** on requirement data
("resolución 2-2010", "Art. 3-'A'", "ISR = Dto. 26-92", "ISR anual =
SAT-1371", "LAT ≤2013", "2236", "propinas", CT art. 120 ¶); the
**D-10-2025 delta register** (derogation of IVA Art. 8-"A" added by D-31-2024
art. 13; LAE Art. 16 final ¶; vigencia = publication day 4-Nov-2025) with
its OCR defect ledger (GOQ-62); the "Mayo 8 de 1992" unlabelled-string rule
(GOQ-63); and the **GOQ-68 in-corpus finding** on the AG 125-2022
FEL-transition texts (24_ art. 29 ¶6 checked against the corpus copy —
negative, recorded in FR-258).

It does **not** cover: the substantive tax rules those instruments contain
(rate, exemptions, retention matrix, ISR brackets — files
[01_iva-core.md](01_iva-core.md) GT-TAX-FR-001..045,
[02_iva-pequeno.md](02_iva-pequeno.md) 046..068,
[03_iva-retenciones.md](03_iva-retenciones.md) 069..110,
[04_isr-trabajo.md](04_isr-trabajo.md) 111..146,
[05_isr-lucrativas-capital.md](05_isr-lucrativas-capital.md) 147..193,
[06_ct-procedures.md](06_ct-procedures.md) 194..235 — those files apply the
qualifiers and guards this file defines to every dated row they emit); the
FEL catalog governance sidecars (kin pattern:
[../catalogs/01_governance.md](../catalogs/01_governance.md)); the
dated-validity strings of declaration forms (F-wave, sourced from 48_); or
the FEL document-type layer (S-GT1 e-invoicing files, which cite 29-"A" and
CT 98"A" as live law and inherit this file's currency rules). This file is
the governance sibling of the taxation set, exactly as
`catalogs/01_governance.md` is for the FEL catalogs.

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): IVA statutory
layer = D-27-92 consolidated **through D-10-2012 ONLY — never cited alone**;
IVA reglamento = "AG 5-2013, reformado por AG 222-2019"; IVA retenciones =
D-20-2006 arts. 1-14 + AG 425-2006 Título II; ISR = LAT D-10-2012
consolidated through Dto. 46-2022 (28_ develops; 47_ = self-disclaimed
digest; 26_ > 28_ > 47_, law wins every delta); CT = "D-6-91, consolidated
through D-37-2016" + CC annotations to 03-12-2019. All quotes below were
verified against the committed evidence extracts and the source text layer
(`gt/.extractions/*.pdf.txt`), never memory.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley del IVA, Decreto Número 27-92 (texto consolidado ≤ D-10-2012): "LEY DEL IMPUESTO AL VALOR AGREGADO / DECRETO NÚMERO 27-92" / "DADO EN EL PALACIO DEL ORGANISMO LEGISLATIVO, A LOS NUEVE DIAS DEL MES DE ABRIL DE MIL NOVECIENTOS NOVENTA Y DOS." / "PALACIO NACIONAL: Guatemala, siete de mayo de mil novecientos noventa y dos. / PUBLIQUESE Y CUMPLASE / SERRANO ELIAS" / última línea sin rótulo: "Mayo 8 de 1992." / transitorio Art. 8: "entrará en vigencia el primero de julio del año en curso" / nota de pie más reciente (p.51): "ARTÍCULO 181. (Del Decreto Número 10-2012 del Congreso de la República). Vigencia. … entrará en vigencia ocho (8) días después de la fecha de publicación en el Diario Oficial…" | IVA law D-27-92 identity: given 9-Apr-1992, promulgated 7-May-1992, unlabelled trailing string "Mayo 8 de 1992" (GOQ-63 — never cited as publication date), original vigencia 1-Jul-1992; consolidation cut-off = D-10-2012 | `gt/sources/23_Ley_IVA_27-92.pdf` | p.1 title block; transitorios pp. 49–51 (EVID-161) |
| LB-002 | D-27-92 (texto ≤ D-10-2012), inventario lettered/bis impreso: "ARTICULO 10. bis* Derogado." / "ARTICULO 14 "A". Base del débito fiscal." / "ARTICULO 23 "A". *Procedimiento general para solicitar la devolución…" / "ARTICULO 24 "A". *Cambio de régimen." / "ARTICULO 24 "B". *Contadores públicos y auditores." / "ARTICULO 52 "A". * Facturas especiales por cuenta del productor…" / "ARTICULO 57 "A". * Obligación de los Registros Públicos." / "ARTICULO 57 "B". * Declaración por el vendedor de vehículos." / "ARTICULO 57 "C". * Obligación de pago del comprador del vehículo." / "ARTICULO 57 "D". * Obligación de presentación electrónica del detalle…" — AUSENTES (grep-verificado): Arts. 3-"A", 7-"A", 8-"A", 25 bis, 29-"A" | The exact lettered/bis inventory of the corpus copy: 10 bis (prints only "Derogado"), 14-"A", 23-"A", 24-"A"/"B", 52-"A", 57-"A"–"D" — and the five absences that delimit what this copy can never support (the FEL article 29-"A", the D-31-2024 8-"A", the Ley 25 bis adder) | `gt/sources/23_Ley_IVA_27-92.pdf` | article headers throughout; txt-verified 2026-08-20 (EVID-161) |
| LB-003 | D-27-92 (texto ≤ D-10-2012), cola de transitorios con vigencias por reforma: D-44-2000: "…entrará en vigencia el uno de julio del año dos mil…" / D-20-2006 (transitorio): "Los artículos 38, 51, 52, 53, 58, 59, 60 y 62 del presente Decreto empezarán a regir ocho (8) días después de su publicación en el Diario Oficial, y el articulado restante empezará a regir el 1 de agosto del año 2006." / D-4-2012 art. 72: "…serán inscritos de oficio… al Régimen de Pequeño Contribuyente establecido en la presente Ley." / D-4-2012 art. 77: "entrara en vigencia ocho días después de su publicación en el Diario Oficial." / D-10-2012 art. 181: urgencia nacional, un solo debate, "ocho (8) días después de la fecha de publicación…" (inicios programados 1-ene-2013 para Libro I ISR) | The 23_ transitorios tail: every incorporated reform decree's own vigencia rule printed verbatim — the regime-cutover anchors for the 2006 and 2012–2013 transitions (8-day defaults; the D-20-2006 split rule; de-oficio pequeño migration) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 42–51 Título VI + transitorios (EVID-179) |
| LB-004 | Reglamento de la Ley del IVA: "ACUERDO GUBERNATIVO No. 5-2013 / Guatemala, 4 de enero de 2013" / "ARTÍCULO 63. Derogatoria. Se deroga el Acuerdo Gubernativo No. 424-2006 de fecha 26 de julio de 2006." / "ARTÍCULO 64. Vigencia. El presente Acuerdo Gubernativo empezará a regir al día siguiente de su publicación en el Diario de Centro América." / despacho "(E-021-2013)-8-enero" / cola de reformas = exactamente AG 222-2019: "*Adicionado la literal j) por el Artículo 1, del Acuerdo Gubernativo Número 222-2019." (Arts. 2 j, 25 bis, 26 bis–quinquies, 28 bis, 36 bis/ter, 29 ¶4, 36) + nota CC: "*Declarada inconstitucional la frase 'así como las universidades autorizadas para funcionar en el país'… de fecha 12 de enero de 2015." (Art. 12) | IVA reglamento identity: AG 5-2013 dated 4-Jan-2013, dispatched 8-Jan-2013, effective 9-Jan-2013 (computed per Art. 64 next-day rule); reform tail = exactly ONE instrument, AG 222-2019 (the FEL cluster), plus the CC 12-Jan-2015 note on Art. 12; replaces AG 424-2006 | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.1 header; reform footnotes at Arts. 2–36 ter; pp. 25–26 signature block (EVID-180) |
| LB-005 | Reglamento (AG 5-2013, reformado por AG 222-2019), Art. 28 bis: "A partir del 1 de julio de 2021, el Régimen FEL será el único medio que la Administración Tributaria autorizará para la emisión de documentos tributarios, a las personas que se inscriban por primera vez para realizar una actividad económica." / Art. 29 ¶4 (con nota "*Reformado el cuarto párrafo por el Artículo 8, del Acuerdo Gubernativo Número 222-2019"): "Los documentos que se autoricen en medios distintos del Régimen FEL tendrán seis meses como plazo máximo de vigencia contados a partir de la fecha de la resolución de autorización." / Art. 29 ¶6 (sexto párrafo, tal como imprime esta copia): "Se exceptúan las facturas electrónicas y el resguardo de copias de facturas emitidas en papel y que luego se convierten en registros electrónicos, los cuales tendrán las características establecidas en este reglamento y en los Acuerdos de Directorio de SAT correspondientes." | The reglamento FEL cluster: FEL-only for first-time registrants from 1-Jul-2021; non-FEL authorizations capped at 6 months — printed at Art. 29 **¶4** in this copy; the sixth paragraph prints the electronic-invoice exception, NOT any AG 125-2022 text (GOQ-68 in-corpus check, this file, 2026-08-20: zero occurrences of "125-2022" or any 2022 stamp in 24_) | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p.12 Arts. 28 bis y 29 (EVID-181; GOQ-68 check on txt lines 181–193) |
| LB-006 | Decreto 10-2025, encabezado del diario: "MARTES 4 de NOVIEMBRE de 2025 No. 40 Tomo CCCXXVII! [sic]" / título: "REFORMAS A LA LEY DE ALIMENTACIÓN ESCOLAR, DECRETO NÚMERO 168-2017 [sic — los artículos posteriores imprimen 16-2017] Y ALA [sic] LEY DEL IMPUESTO AL VALOR AGREGADO, DECRETO NÚMERO 27-92…" / "Artículo 4. Vigencia. El presente Decreto fue declarado de urgencia nacional con el voto favorable de las dos terceras partes del número total de diputados… aprobado;en [sic] un solo debate y entrará en vigencia el día de su publicación en el Diario Oficial." / "EMITIDO EN EL PALACIO DEL ORGANISMO LEGISLATIVO… EL VEINTIUNO DE OCTUBRE DE DOS MIL VEINTICINCO." / firma garbled: "Anebolla Maris Qiracos Méndez. / Ministro de Fdacación [sic]" | D-10-2025 identity: emitido 21-Oct-2025, sanción 30-Oct-2025, published DCA 4-Nov-2025 No. 40; **vigencia = publication day** (urgencia nacional, single debate, no vacatio legis); OCR noise throughout — Tomo, title, signature all carry [sic] defects (defect ledger, GOQ-62) | `gt/sources/74_Ley_IVA_EScolar_Reformas_D10-2025.pdf` | p.1 gazette header + title; p.2 date blocks (EVID-187) |
| LB-007 | D-10-2025, Artículo 1: "Se deroga e! [sic] artículo 8 "A" de la Ley del Impuesto al Valor Agregado, Decreto Número 27-92, adicionado por el artículo 13 de ia [sic] Ley para la Integración: [sic] del Sector Productivo Primario y Agropecuario, Decreto Número 31-2024, ambos del Congreso de la República de Guatemala, o [sic]" | D-10-2025 Art. 1 derogates IVA Art. 8-"A" (the MINEDUC alimentación-escolar retention scheme article added by D-31-2024 art. 13) — no "3-'A'" text exists anywhere in the decree (rejected myth, R19; OCR 8/3 residue → GOQ-13) | `gt/sources/74_Ley_IVA_EScolar_Reformas_D10-2025.pdf` | p.2 Art. 1; pp. 1–2 considerandos II/III/V (EVID-188) |
| LB-008 | D-10-2025, Artículo 2: "Se deroga el párrafo final del artículo 16 de la Ley de Alimentación Escolar, Decreto Número 16-2017, adicionado por el artículo 18 de la Ley para la integración del Sector Productiva [sic] Primario y Agropecuario, Decreto Número 31-2024…" / Artículo 3: "…el cual queda asi [sic]: '6. Asociación para el Desarrollo Integral de Nororiente (ADIN) 3.50»' [sic — cifra truncada tal como imprime]" | Art. 2 derogates the LAE D-16-2017 Art. 16 final ¶ (added D-31-2024 art. 18) — the companion repeal unwinding the D-31-2024 alimentación-escolar package; Art. 3 is an unrelated 2025-budget line amendment (ADIN "3.50»" [sic] — OCR-truncated figure, not citable per GOQ-62) | `gt/sources/74_Ley_IVA_EScolar_Reformas_D10-2025.pdf` | p.2 Arts. 2 y 3 (EVID-189, EVID-190) |
| LB-009 | Ley de Actualización Tributaria, "DECRETO NÚMERO 10-2012" / "EMITIDO… EL DIECISÉIS DE FEBRERO DE DOS MIL DOCE." / "PALACIO NACIONAL: GUATEMALA, UNO DE MARZO DEL AÑO DOS MIL DOCE / PUBLÍQUESE Y CUMPLASE / PEREZ MOLINA" / sellos marginales: "*Reformado el primer párrafo, por el Artículo 4, del Decreto Del Congreso Número 4-2019 el 08-05-2019" / "*Reformado el numeral 14, por el Artículo 9, del Decreto Del Congreso Número 40-2022 el 30-08-2022" / "*Adicionado por el Artículo 13, del Decreto Del Congreso Número 46-2022 el 27-09-2022" (art. 53 Bis) — inventario completo de sellos: 14-2013, 19-2013, 4-2019, 2-2020, 40-2022, 46-2022 + sentencias CC | LAT D-10-2012 identity: emitted 16-Feb-2012, sanctioned 1-Mar-2012; consolidated through Dto. 46-2022 (27-09-2022) — the "≤2013" prior assumption is REFUTED (R24); for ISR Libro I the operative instruments are 19-2013 (bulk), 14-2013 (art. 70 núm. 7 only), 2-2020, 46-2022; post-27-09-2022 state unverified from this copy | `gt/sources/26_LAT_10-2012.pdf` | p.1 title block; p.64 promulgation; marginal stamps (61 stamp lines txt-verified) (EVID-216) |
| LB-010 | Reglamento del Libro I de la LAT: "ACUERDO GUBERNATIVO NÚMERO 213-2013 / Guatemala, 8 de mayo de 2013" / "REGLAMENTO DEL LIBRO I DE LA LEY DE ACTUALIZACIÓN TRIBUTARIA, DECRETO NÚMERO 10-2012…" / sellos: "*Reformado el tercer párrafo por el Artículo 1, del Acuerdo Gubernativo Número 167-2014 el 06-06-2014" (art. 7); art. 25 reformado + arts. 25"A"/25"B" adicionados por AG 167-2014 / "ARTICULO 91. Vigencia. El presente Acuerdo Gubernativo empezará a regir el día de su publicación en el Diario de Centro América." | ISR reglamento identity: AG 213-2013 (8-May-2013) consolidated with **AG 167-2014 only** (06-06-2014); no DCA date printed — the vigencia rule is publication-day but the date itself is undateable from the corpus | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p.1 header; pp. 39–40 signature/vigencia blocks; marginal stamps (EVID-236) |
| LB-011 | Digest SAT: "Unidad de Orientación Legal y Derechos del Contribuyente / Departamento de Consultas / Intendencia de Asuntos Jurídicos" / "Derivado de las consultas recurrentes entre los meses de diciembre 2023 a enero 2024… se presenta el siguiente documento informativo" / "Este material solo puede ser utilizado con fines ilustrativos y no sustituye la consulta de leyes y reglamentos correspondientes." | 47_ identity: undated, unsigned SAT orientation digest (no number, no signature, no publication date; consultas Dec-2023–Jan-2024; filename 2025); self-disclaimed as illustrative — authority order 26_ > 28_ > 47_, never cited as law | `gt/sources/47_SAT_Patronos_Retencion_ISR_2025.pdf` | p.1 header + PRESENTACIÓN (EVID-242) |
| LB-012 | Código Tributario, Decreto 6-91 (texto consolidado): anotaciones inline — muestra del censo (135 anotaciones): "47-91 el 01-06-1991" / "20-2006 el 06-07-2006" / "4-2012 el 25-02-2012" / "19-2013 el 21-12-2013" / "37-2016 el 31-08-2016" / última anotación de cualquier tipo: "*Sin Lugar la acción de Inconstitucionalidad en contra del Artículo 30 "C"… por el Expediente Número 3267-2018 el 03-12-2019" | CT authority table: legislative consolidation runs through D-37-2016 (31-08-2016); latest integrated event of any kind = CC ruling 03-12-2019; no FEL-era CT reform integrated in this copy — post-D37-2016 state unknown from the corpus | `gt/sources/25_Codigo_Tributario_6-91.pdf` | inline annotations throughout (no tail block exists) (EVID-192) |
| LB-013 | Decreto 20-2006: "DECRETO NÚMERO 20-2006" / "EMITIDO… EL SEIS DE JUNIO DE DOS MIL SEIS." / "PALACIO NACIONAL: Guatemala, veinte de junio del año dos mil seis. PUBLÍQUESE Y CUMPLASE" / "ARTICULO 76. Vigencia. Los artículos 38, 51, 52, 5 3 [sic], 58, 59, 60 y 62 del presente Decreto empezarán a regir ocho (8) días después de su publicación en el Diario Oficial, y el articulado restante empezará a regir el 1 de agosto del año 2006." — texto consolidado ≥2015 (notas de reforma D-4-2012 arts. 2 ¶4/12/13/20/21 del 25-02-2012 + CC expedientes 2836-2012 y 2240-2014) | D-20-2006 identity: given 6-Jun-2006, sanctioned 20-Jun-2006, DCA date not printed (GOQ-69); **split vigencia**: the eight named articles rule DCA+8d (undateable), ALL other articles — including the entire retention regime arts. 1-14 — rule the fixed date 1-Aug-2006; this print is a consolidated ≥2015 text, not the 2006 first print | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | p.1 title block; p.44 dates + Art. 76 (EVID-246) |
| LB-014 | D-20-2006, Artículo 68: "Se deroga el artículo 1 del Decreto Número 03-04… Se deroga el artículo 2 5 [sic] del Decreto Número 03-04 del Congreso de la República… Se derogan todas las disposiciones legales que se opongan a lo establecido en esta ley." / Artículo 74: "Dentro del plazo máximo de treinta (30) días contados a partir del día siguiente de la publicación de la presente ley, el Organismo Ejecutivo deberá emitir el reglamento que desarrolle lo establecido en los capítulos I, II y III del presente decreto; el reglamento de la Ley del Impuesto al Valor Agregado." / Artículo 75: "La Administración Tributaria dispondrá de seis meses, a partir de la fecha en que entren en vigencia los capítulos I, II, III de la p resente [sic] ley, para el efecto de implementar en forma programada y progresiva los procesos, procedimientos, comunicaciones y sistemas…" | D-20-2006 lineage: Art. 68 repeals the eight CT-reform articles of D.03-04 (arts. 1/3/12/14/19/21/23/25 — touching CT arts. 30/40/98/101/112/142/153/165) + catch-all; Art. 74 mandates the reglamento within 30 días of publication (fulfilled by AG 425-2006, 26-Jul-2006); Art. 75 gives SAT a 6-month progressive-implementation window from 1-Aug-2006 | `gt/sources/78_Fortalecimiento_D20-2006.pdf` | pp. 41–44 Arts. 68, 74–76 (EVID-256) |
| LB-015 | Reglamento AG 425-2006: "ACUERDO GUBERNATIVO No. 425-2006 / Guatemala, 26 de julio de 2006." / "ARTICULO 39… El presente Reglamento empezará a regir el uno de agosto de dos mil seis y deberá publicarse en el Diario de Centro América." / Art. 32 (imprentas) tal como imprime esta copia consolidada: "…la vigencia máxima que tendrán los documentos que se autoricen en medios distintos al Régimen de Facturación Electrónica en Línea -FEL-, de acuerdo con el sexto párrafo del artículo 29 del Reglamento de la Ley del Impuesto al Valor Agregado." con nota: "*Reformado por el Artículo 25, del Acuerdo Gubernativo Número 125-2022, vigente a partir del 25 de noviembre del 2022, (seis meses después de su publicación.)" | AG 425-2006 identity: issued 26-Jul-2006 (within the Art. 74 30-day window), rige 1-Aug-2006 same day as the law's chapters I–III, DCA date not printed (GOQ-69 kin); the consolidated print carries exactly one reform stamp — AG 125-2022 on art. 32 (vigente 25-Nov-2022), whose text cites "el sexto párrafo del artículo 29 del Reglamento" for the 6-month/FEL rule — the GOQ-68 hook | `gt/sources/79_Fortalecimiento_Reglamento_AG_425-2006.pdf` | p.1 header; p.16 Arts. 37–39; p.14 art. 32 + nota (EVID-260; art. 32 text txt lines 461–476) |
| LB-016 | Política de gestión de cambios regulatorios (permanente), D15/D16: filas fechadas valid_from/to + procedencia; los cambios agregan filas; nunca se reemplaza en el lugar; snapshot-on-write | Regulatory change-management standing policy, D15/D16: dated rule rows (valid_from/to + provenance); changes add rows; snapshot-on-write; no in-place replacement — the cross-country mechanics this file instantiates for GT taxation instruments | `shared/docs/regulatory-change-management.md` | D15–D16 (master-index shared canon) |

## 3. Functional Requirements

### 3.1 The per-instrument consolidation-cutoff register

- **GT-TAX-FR-236:** The system shall maintain a machine-readable
  **consolidation-cutoff register** with one dated provenance row per
  taxation instrument in the corpus — 23_ D-27-92, 24_ AG 5-2013, 25_ CT
  D-6-91, 26_ LAT D-10-2012, 28_ AG 213-2013, 47_ SAT digest, 74_ D-10-2025,
  78_ D-20-2006, 79_ AG 425-2006 — each row carrying: instrument id, date
  fields (given/sanctioned/published/effective, null where the corpus prints
  none), the consolidation cutoff, the exact reform tail (stamp list), the
  vigencia rule, and known print defects. This register governs every dated
  row emitted by files 01–06 of this wave (the currency qualifiers, guards
  and validation rules below are its read-side contract). (LB-016; EVID-161,
  EVID-180, EVID-192, EVID-216, EVID-236, EVID-242, EVID-246, EVID-260,
  EVID-187)
- **GT-TAX-FR-237:** The 23_ register row shall record: D-27-92 given
  9-Apr-1992, promulgated 7-May-1992, original vigencia 1-Jul-1992
  (transitory Art. 8), consolidation cut-off **≤ D-10-2012** (latest
  incorporated instrument; Dec-2012 publication era), GFACE-era Art. 18
  (electronic credit documentation recognized only via SAT-authorized GFACE
  — pre-FEL vintage), and the unlabelled trailing string "Mayo 8 de 1992"
  stored as an UNLABELLED string, never as a publication date (FR-257,
  GOQ-63). (LB-001; EVID-161)
- **GT-TAX-FR-238:** The register shall carry the 23_ lettered/bis article
  inventory as validation data — present: exactly 10 bis (prints only
  "Derogado"), 14-"A", 23-"A", 24-"A", 24-"B", 52-"A", 57-"A", 57-"B",
  57-"C", 57-"D"; ABSENT (grep-verified): Arts. 3-"A", 7-"A", 8-"A", 25 bis,
  29-"A" — and any requirement, citation or configuration asserting one of
  the absent articles as sourced from 23_ shall fail validation: the FEL
  article 29-"A" (added D-4-2019 art. 6), the Ley 25 bis adder (instrument
  unidentified) and the 8-"A" (added D-31-2024 art. 13, derogated D-10-2025)
  all lie beyond this copy (GOQ-01). (LB-002; EVID-161; R22; GOQ-01 → OQ-005)
- **GT-TAX-FR-239:** The register shall carry the 23_ transitorios-tail
  per-reform vigencia strings as regime-cutover anchors: the D-20-2006 split
  rule (eight named articles DCA+8d; remaining articulado fixed 1-Aug-2006),
  D-4-2012 art. 77 and D-10-2012 art. 181 (8 days after publication, with
  the scheduled 1-Jan-2013 ISR Libro I start), and the D-4-2012 art. 72
  de-oficio pequeño-migration rule. (LB-003; EVID-179)
- **GT-TAX-FR-240:** The 24_ register row shall record: AG 5-2013 dated
  4-Jan-2013, dispatched 8-Jan-2013 (stamp "(E-021-2013)-8-enero"),
  effective 9-Jan-2013 (computed per Art. 64 next-day rule); reform tail =
  **exactly AG 222-2019** (Arts. 2 j, 25 bis, 26 bis–quinquies, 28 bis, 36
  bis/ter, 29 ¶4, 36) plus the CC 12-Jan-2015 unconstitutionality note on
  Art. 12; Art. 63 derogates AG 424-2006. No other reform stamp exists in
  this copy — in particular zero AG 125-2022 content (FR-258). (LB-004;
  EVID-180)
- **GT-TAX-FR-241:** The 26_ register row shall record: LAT D-10-2012
  emitted 16-Feb-2012, sanctioned 1-Mar-2012, consolidated **through Dto.
  46-2022 (27-09-2022)** with the exact stamp inventory 14-2013, 19-2013,
  4-2019, 2-2020, 40-2022, 46-2022 + CC sentencias; the prior "LAT ≤2013"
  assumption is REFUTED (R24) and shall never appear in requirement data; the
  residual window (post-27-09-2022 reform state unverified from this copy)
  is a standing caveat on every LAT-derived row (owned by files 04/05).
  (LB-009; EVID-216; R24)
- **GT-TAX-FR-242:** The 28_ register row shall record: AG 213-2013
  (8-May-2013) consolidated with **AG 167-2014 only** (reform stamps
  06-06-2014: art. 7 ¶3, art. 25, arts. 25-"A"/25-"B"); no DCA date printed —
  the Art. 91 vigencia rule is publication-day but the date is undateable
  from the corpus, so the row carries effective = null with the rule string,
  never an invented date. (LB-010; EVID-236)
- **GT-TAX-FR-243:** The 47_ register row shall record: undated, unsigned
  SAT orientation digest (Unit of Legal Orientation/Consultas; no
  instrument number, no signature, no publication date; consultas
  Dec-2023–Jan-2024; filename dated 2025; terminus post quem Jan-2024),
  self-disclaimed "solo… con fines ilustrativos"; the ISR authority order
  **26_ > 28_ > 47_ (law wins every delta)** is register data — 47_ is
  citable only for current-practice signals, never as authority for any
  rate, threshold, deadline or article text. (LB-011; EVID-242)
- **GT-TAX-FR-244:** The 25_ register row shall record: CT D-6-91
  legislative consolidation **through D-37-2016 (31-08-2016)**, latest
  integrated event of any kind = CC ruling **03-12-2019** (Exp. 3267-2018,
  art. 30"C"); no FEL-era CT reform integrated; every CT citation emitted by
  the system carries the qualifier "D-6-91, consolidated through D-37-2016;
  CC annotations through 03-12-2019" (cross-ref file 06 for the
  void-provision guards: art. 120 suspension ¶ → cite 98"A"; art. 120"A";
  art. 94.19 — R21). (LB-012; EVID-192; R21)
- **GT-TAX-FR-245:** The 78_ register row shall record: D-20-2006 given
  6-Jun-2006, sanctioned 20-Jun-2006, DCA date not printed; **split
  vigencia**: arts. 38/51/52/53/58/59/60/62 rule DCA+8d (undateable from the
  corpus — GOQ-69), ALL other articles — including the entire retention
  regime arts. 1-14 — rule the fixed date **1-Aug-2006** (verbatim, no
  computation); this print is a consolidated ≥2015 text (inline D-4-2012
  reform notes arts. 2 ¶4/12/13/20/21, all 25-02-2012, + CC exps. 2836-2012
  and 2240-2014), not the pristine 2006 print. (LB-013; EVID-246)
- **GT-TAX-FR-246:** The 79_ register row shall record: AG 425-2006 issued
  26-Jul-2006 (fulfilling D-20-2006 art. 74's 30-day reglamento mandate),
  rige 1-Aug-2006 (Art. 39) same day as the law's chapters I–III, DCA date
  not printed; reform stamp = **AG 125-2022 on art. 32 only** ("vigente a
  partir del 25 de noviembre del 2022, (seis meses después de su
  publicación.)"), FEL-transition content; retention articles show no
  reform notes. (LB-015; EVID-260)
- **GT-TAX-FR-247:** The register shall carry the D-20-2006 lineage rows:
  the Art. 68 repeal map of D.03-04 (its arts. 1/3/12/14/19/21/23/25, which
  had touched CT arts. 30/40/98/101/112/142/153/165, derogated with a
  catch-all clause); the Art. 74 reglamento mandate (30 días from
  publication — fulfilled by AG 425-2006); and the Art. 75 SAT
  6-month progressive-implementation window counted from 1-Aug-2006.
  (LB-014; EVID-256)

### 3.2 Currency qualifiers & citation guards

- **GT-TAX-FR-248:** Every citation of a taxation instrument emitted by the
  system (requirement data, seeded configuration, generated documentation,
  diagnostic strings) shall carry its consolidation cutoff as resolved from
  the register — e.g. "D-27-92 (texto ≤ D-10-2012)", "AG 5-2013, reformado
  por AG 222-2019", "D-6-91, consolidated through D-37-2016", "LAT D-10-2012
  (texto ≤ D-46-2022 del 27-09-2022)", "D-20-2006 (texto consolidado
  ≥2015; régimen de retenciones vigente 1-ago-2006)", "AG 425-2006 (rige
  1-ago-2006; art. 32 reformado por AG 125-2022, vigente 25-11-2022)" — a
  bare instrument citation with no cutoff is a validation failure.
  (LB-016; FR-236; EVID-161, EVID-180, EVID-192, EVID-216, EVID-246,
  EVID-260)
- **GT-TAX-FR-249:** The IVA statutory layer shall NEVER be cited alone:
  every current-law row derived from 23_ carries the qualifier "D-27-92
  (texto ≤ D-10-2012), reformado por… (≥ D-4-2019 / D-31-2024 / D-10-2025)";
  the post-2018 consolidated text is missing from the corpus and its
  acquisition is pending (GOQ-01). (LB-001; EVID-161; R22; GOQ-01 → OQ-005)
- **GT-TAX-FR-250:** ISR citations shall resolve only to the LAT: ISR law =
  **D-10-2012 Libro I (vigente 1-ene-2013)**; Dto. 26-92 and its reforms
  were derogated by LAT art. 180.1 effective with the Libro I start
  (1-Jan-2013) and shall never be cited as current ISR law; reglamento =
  AG 213-2013 (reformado por AG 167-2014); digest 47_ never as authority
  (FR-243); the "propinas" addition in 47_'s art. 68 num. 1 quotation is an
  unverified digest addendum — the 26_ consolidated list governs (R25).
  (LB-009; LB-010; LB-011; EVID-216, EVID-236, EVID-242; R25)
- **GT-TAX-FR-251:** Form-number citations shall cite the form catalog
  (48_/RetWeb) only — the retention instruments 78_/79_ print no form
  numbers (both say only "el formulario que para el efecto proporcione la
  Administración Tributaria"); the R46 mapping is binding validation data:
  ISR retenciones = SAT-1331; ISR anual lucrativas = SAT-1411; relación de
  dependencia anual = SAT-1431; ISR Capital Mensual = SAT-1321; ISR No
  Residentes Pago Directo (mensual) = SAT-1371 — the string "SAT-1371" as
  ISR-anual identity is a rejected myth. (LB-013; LB-015; EVID-246, EVID-260,
  EVID-265 note; R46)
- **GT-TAX-FR-252:** The myths list shall be enforced as machine-actionable
  validation rules on requirement data (kin to the catalogs governance
  corrections-log pattern): the strings "resolución 2-2010" (rejected basis
  for the IVA-retention regime — it rests solely on D-20-2006 Capítulo I +
  AG 425-2006 Título II, grep-verified absence, R23), "Art. 3-'A'" (never
  existed; the D-10-2025 derogation names 8-"A", R19), "ISR = Dto. 26-92"
  (superseded, FR-250), "ISR anual = SAT-1371" (R46), "LAT ≤2013" /
  "consolidated through Dto. 14-2013" (refuted, R24), "2236" as a current
  form identifier (legacy, rejected), "propinas" as part of the art. 68
  num. 1 list (R25), and any CT art. 120 final-¶ citation as live law
  (void per CC Exp. 680-2013 — cite 98"A".2, R21) shall not appear as
  authority data anywhere in the seeded requirements, and their detection at
  CI time blocks the build. (LB-002; LB-007; LB-009; LB-012; EVID-161,
  EVID-188, EVID-216; R19, R21, R23, R24, R25, R46)

### 3.3 D-10-2025 delta register & OCR defect ledger

- **GT-TAX-FR-253:** The register shall carry the D-10-2025 identity row:
  emitido 21-Oct-2025, sanción 30-Oct-2025, published DCA 4-Nov-2025 No. 40
  (Tomo "CCCXXVII!" [sic]), **vigencia = publication day 4-Nov-2025**
  (urgencia nacional, single debate, Art. 4; no transitory articles, no
  vacatio legis — every operative article effective 4-Nov-2025).
  (LB-006; EVID-187)
- **GT-TAX-FR-254:** The D-10-2025 delta register shall contain exactly
  four rows, each effective 4-Nov-2025: Art. 1 **DEROGA** D-27-92 Art.
  8-"A" (added by D-31-2024 art. 13 — the MINEDUC alimentación-escolar
  retention scheme; recorded as printed, never as "3-'A'", R19/GOQ-13);
  Art. 2 **DEROGA** the LAE D-16-2017 Art. 16 final ¶ (added D-31-2024
  art. 18); Art. 3 REFORMA a D-36-2024 budget line (ADIN "3.50»" [sic] —
  OCR-truncated, not citable, FR-256); Art. 4 VIGENCIA. Completeness
  guard: nothing else in D-10-2025 touches D-27-92 — the decree shall never
  be over-read as a broader IVA reform. (LB-007; LB-008; EVID-188,
  EVID-189, EVID-190)
- **GT-TAX-FR-255:** The 74_ defect ledger shall record every printed defect
  verbatim with [sic] and never normalize it: the title misprint
  "168-2017" [sic] (contradicted by Art. 2's own "16-2017"), Tomo
  "CCCXXVII!" [sic], the garbled signature block ("Anebolla Maris Qiracos
  Méndez… Ministro de Fdacación" [sic]), the OCR intrusions in Art. 1
  ("e! [sic]", "ia [sic]", ": [sic]", "o [sic]") and the truncated Art. 3
  figure "3.50»" [sic]; identity nonetheless unambiguous (decree number +
  both target laws + coherent dates). (LB-006; LB-007; LB-008; EVID-187,
  EVID-188, EVID-190)
- **GT-TAX-FR-256:** OCR-noise values from 74_ shall not be citable until
  clean-copy verification (GOQ-62): the Tomo string, the title "168-2017"
  reading, the signature block and the "3.50»" budget figure are defect-
  ledger data only — dates and article numbers are citable (internally
  consistent), the defective strings are not. (LB-006; LB-008; EVID-187,
  EVID-190; GOQ-62 → OQ-001)
- **GT-TAX-FR-257:** The unlabelled string "Mayo 8 de 1992." (final line of
  23_) shall be stored as an unlabelled trailing string of the instrument
  row — plausibly the original DCA publication date but printed without any
  label; it shall never be cited, computed from, or seeded as a publication
  date without external confirmation (GOQ-63; the 23_ row's published field
  = null). (LB-001; EVID-161; GOQ-63 → OQ-002)

### 3.4 GOQ-68 — FEL-transition reglamento currency (in-corpus check recorded)

- **GT-TAX-FR-258:** The register shall record the GOQ-68 in-corpus finding
  (checked 2026-08-20 against `24_Reglamento_IVA_AG_5-2013.pdf.txt`):
  24_ art. 29 prints six paragraphs; the **sixth paragraph (sexto párrafo)
  does NOT print any AG 125-2022 FEL-transition text** — it prints the
  electronic-invoice exception ("Se exceptúan las facturas electrónicas y el
  resguardo de copias…") — and the copy contains ZERO occurrences of
  "125-2022" or any 2022 stamp (sole art. 29 reform note: AG 222-2019 art. 8
  on ¶4). Consequence recorded as data: 79_ art. 32 (as reformed by
  AG 125-2022, vigente 25-Nov-2022) grounds its 6-month non-FEL
  authorization rule on "el sexto párrafo del artículo 29 del Reglamento" —
  but the in-corpus 24_ prints that rule at **¶4**; the ¶6 citation
  therefore implies a post-2022 reglamento text not held in corpus, and the
  **AG 125-2022 acquisition need stands** (already queued,
  DOWNLOAD_QUEUE rev 7). (LB-005; LB-015; EVID-181, EVID-260; GOQ-68 →
  OQ-003)
- **GT-TAX-FR-259:** FEL-transition citations shall resolve as follows
  until GOQ-68's acquisition leg closes: the 6-month non-FEL sunset cites
  reglamento Art. 29 **¶4** (AG 222-2019 art. 8) as printed in-corpus; the
  FEL-only rule for first-time registrants cites Art. 28 bis (AG 222-2019,
  from 1-Jul-2021); the AG 125-2022 reform of 79_ art. 32 (art. 25 of the
  AG, vigente 25-Nov-2022, "seis meses después de su publicación") is
  citable only through its reform stamp as printed in 79_ — the AG 125-2022
  body text itself is not citable from this corpus. (LB-005; LB-015;
  EVID-181, EVID-260; GOQ-68 → OQ-003)

### 3.5 Register mechanics & validation gate

- **GT-TAX-FR-260:** Citation validation against this register (cutoff
  presence per FR-248, never-alone per FR-249, ISR authority per FR-250,
  form-number authority per FR-251, myths per FR-252, delta completeness
  per FR-254, defect/OCR guards per   FR-255/256, unlabelled-string rule per
  FR-257) shall run as a **CI gate on the requirements data** in the SaaS
  build pipeline (kin to the catalogs governance corrections-log pattern):
  a violation blocks the build with a diagnostic naming the FR and the
  offending row — never a warning. (LB-016; LB-001; LB-007; LB-009; LB-013;
  EVID-161, EVID-188, EVID-216, EVID-246; FR-236..257)
- **GT-TAX-FR-261:** When a new instrument print or consolidation arrives
  in `gt/sources/` (e.g. the post-2018 consolidated IVA text GOQ-01, the
  D-31-2024 full text GOQ-13, or AG 125-2022 GOQ-68), the pipeline shall
  capture its delta, dates and reform tail in the register BEFORE any
  synthesis requirement is written against it; register rows are appended
  (D16) — a newer consolidation adds a row and closes the old one's window,
  never replacing the earlier print's provenance in place. (LB-016; LB-001;
  LB-004; LB-015; EVID-161, EVID-181, EVID-260; GOQ-68 → OQ-003,
  GOQ-01 → OQ-005, GOQ-13 → OQ-006)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance; snapshot-on-write; register rows are append-only (FR-261).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.legal.instrument.provenance | instrument_id | char | 23_ D-27-92 · 24_ AG 5-2013 · 25_ D-6-91 · 26_ LAT D-10-2012 · 28_ AG 213-2013 · 47_ digest · 74_ D-10-2025 · 78_ D-20-2006 · 79_ AG 425-2006 | FR-236 |
| l10n_gt.legal.instrument.provenance | given / sanctioned / published / effective | date / date / date / date | null where the corpus prints none (23_ published = null — GOQ-63; 28_ published/effective = null; 78_/79_ published = null — GOQ-69); 74_ effective = 2025-11-04 | FR-237, FR-242, FR-245, FR-246, FR-253, FR-257 |
| l10n_gt.legal.instrument.provenance | consolidation_cutoff | char | 23_ "≤ D-10-2012" · 24_ "AG 222-2019" · 25_ "D-37-2016 (31-08-2016) + CC 03-12-2019" · 26_ "D-46-2022 (27-09-2022)" · 28_ "AG 167-2014 (06-06-2014)" · 47_ "terminus post quem Jan-2024" · 78_ "≥2015 print" · 79_ "AG 125-2022 stamp on art. 32" | FR-237..246 |
| l10n_gt.legal.instrument.provenance | reform_tail | char | exact stamp lists (24_: "exactly AG 222-2019 — Arts. 2 j, 25 bis, 26 bis-quinquies, 28 bis, 36 bis/ter, 29 ¶4, 36 + CC 12-01-2015 note Art. 12"; 26_: "14-2013, 19-2013, 4-2019, 2-2020, 40-2022, 46-2022 + CC"; 78_: "D-4-2012 arts. 2 ¶4/12/13/20/21 + CC 2836-2012/2240-2014") | FR-240, FR-241, FR-245 |
| l10n_gt.legal.instrument.provenance | vigencia_rule | char | fixed date (23_ 1-Jul-1992; 78_ arts. 1-14 / 79_ 1-Aug-2006) · DCA+8d (78_ arts. 38/51/52/53/58/59/60/62 — undateable, GOQ-69) · publication day (74_ Art. 4; 28_ Art. 91) · next day after publication (24_ Art. 64, computed 9-Jan-2013) · "seis meses después de su publicación" (AG 125-2022 stamp) | FR-237, FR-239, FR-240, FR-242, FR-245, FR-246, FR-253 |
| l10n_gt.legal.instrument.provenance | unlabelled_strings | json | {"23_": "Mayo 8 de 1992."} — stored, never a date field (GOQ-63) | FR-257 |
| l10n_gt.legal.article.inventory | instrument / articles_lettered_bis / articles_absent | char / json / json | 23_: present = [10 bis "Derogado", 14"A", 23"A", 24"A", 24"B", 52"A", 57"A", 57"B", 57"C", 57"D"]; absent = [3-"A", 7-"A", 8-"A", 25 bis, 29-"A"] | FR-238 |
| l10n_gt.legal.delta | instrument / article / target_instrument / target_article / operation / effective | char / char / char / char / selection derogación-reforma-vigencia / date | 74_ D-10-2025: Art. 1 → D-27-92 Art. 8-"A" (D-31-2024 art. 13) DEROGACIÓN 2025-11-04; Art. 2 → LAE D-16-2017 Art. 16 final ¶ (D-31-2024 art. 18) DEROGACIÓN 2025-11-04; Art. 3 → D-36-2024 art. 132 REFORMA 2025-11-04; Art. 4 VIGENCIA 2025-11-04 | FR-254 |
| l10n_gt.legal.defect.ledger | instrument / location / defect_text | char / char / char | 74_: Tomo "CCCXXVII!" [sic]; title "168-2017" [sic]; "Anebolla Maris Qiracos Méndez… Ministro de Fdacación" [sic]; Art. 1 "e!/ia/:/o" [sic]; Art. 3 "3.50»" [sic] — verbatim [sic], never normalized; non-citable until clean copy (GOQ-62) | FR-255, FR-256 |
| l10n_gt.legal.validation.rule | rule_key / forbidden_string / correction | char / char / char | myths: "resolución 2-2010" → D-20-2006 Cap. I + AG 425-2006 Tít. II; "Art. 3-'A'" → 8-"A" (D-31-2024 art. 13, derogated D-10-2025); "ISR = Dto. 26-92" → LAT D-10-2012; "ISR anual = SAT-1371" → SAT-1411/1431 per R46; "LAT ≤2013" → through D-46-2022; "2236" → rejected legacy id; "propinas" (art. 68 num. 1) → 26_ list governs; CT art. 120 ¶ → 98"A".2 (CC 680-2013) | FR-252 |
| l10n_gt.legal.citation.qualifier | instrument_id / qualifier_string | char / char | emitted with every citation (FR-248 catalog of exact strings) | FR-248 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `shared` = the provenance
register and its qualifier/guard contract — data both sides must honor
identically (this register governs every dated row any module emits);
`saas` = the CI validation gate on requirements data living in the build
pipeline (kin to the catalogs governance pattern). Per the wave plan the
register is `shared`; citation validation is `saas`. Model names stable
across Odoo 17/18/19/20; no version-specific behavior required by this
file — the register is consumed as config data by both sides.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-236 | shared | l10n_gt.legal.instrument.provenance (new) | all register fields | Append-only register (D16); governs dated-row emission files 01–06 |
| FR-237 | shared | — (register data §4) | 23_ row | Unlabelled string kept out of date fields (FR-257) |
| FR-238 | shared | l10n_gt.legal.article.inventory | 23_ lettered/bis + absences | Absent-article assertions from 23_ fail validation |
| FR-239 | shared | — (register data §4) | 23_ transitorios vigencia strings | Regime-cutover anchors (2006 split; 2012–2013 transitions) |
| FR-240 | shared | — (register data §4) | 24_ row | Tail "exactly AG 222-2019" is copy property; no AG 125-2022 content |
| FR-241 | shared | — (register data §4) | 26_ row | "LAT ≤2013" refuted (R24); residual post-46-2022 caveat owned by files 04/05 |
| FR-242 | shared | — (register data §4) | 28_ row | published/effective = null + rule string; never an invented date |
| FR-243 | shared | — (register data §4) | 47_ row + authority order | 26_ > 28_ > 47_; digest never authority |
| FR-244 | shared | — (register data §4) | 25_ row | Qualifier on every CT citation; void-text guards owned by file 06 |
| FR-245 | shared | — (register data §4) | 78_ row | Split vigencia; retention regime fixed 1-Aug-2006; ≥2015 print caveat |
| FR-246 | shared | — (register data §4) | 79_ row | AG 125-2022 stamp on art. 32 only |
| FR-247 | shared | — (register data §4) | D-20-2006 lineage rows | D.03-04 repeal map; art. 74 mandate; art. 75 SAT window |
| FR-248 | shared | protocol/config envelope | cutoff qualifier on emitted citations | Both sides emit the same qualifier strings; bare citations rejected |
| FR-249 | shared | — | 23_-never-alone guard | Pairs with GOQ-01 acquisition (post-2018 text) |
| FR-250 | shared | — | ISR authority guard | LAT-only; 26-92 superseded 1-Jan-2013; "propinas" R25 guard |
| FR-251 | shared | — | form-number authority guard | R46 mapping binding; 48_/RetWeb owns forms |
| FR-252 | shared | — (validation data §4) | myths rule set | Detected at CI (FR-260); kin to catalogs corrections log |
| FR-253 | shared | — (register data §4) | 74_ identity row | Vigencia = publication day 4-Nov-2025 |
| FR-254 | shared | l10n_gt.legal.delta | D-10-2025 rows | Completeness guard against over-reading the decree |
| FR-255 | shared | l10n_gt.legal.defect.ledger | 74_ defects | Verbatim [sic]; never normalized |
| FR-256 | shared | — | OCR non-citable list | GOQ-62; clean-copy verification precondition |
| FR-257 | shared | — | unlabelled-string rule | GOQ-63; published = null on the 23_ row |
| FR-258 | shared | — (register data §4) | GOQ-68 finding row | Negative ¶6 check + AG 125-2022 acquisition flag |
| FR-259 | shared | — | FEL-transition citation routing | 29 ¶4 (AG 222-2019) as printed; AG 125-2022 via 79_ stamp only |
| FR-260 | saas | — (CI pipeline) | validation gate on requirements data | Blocks build on violation; kin to catalogs governance pattern |
| FR-261 | shared | — (ops procedure) | register maintenance | Capture-before-synthesis; append-only (D16); GOQ-01/13/68 arrivals |

## 6. Acceptance Criteria

- **AC-001:** Given the register, when read, then it contains one row per
  corpus instrument with exactly these cutoffs: 23_ ≤ D-10-2012; 24_ AG
  222-2019; 25_ D-37-2016 + CC 03-12-2019; 26_ D-46-2022 (27-09-2022); 28_
  AG 167-2014 (06-06-2014); 47_ terminus post quem Jan-2024; 74_ effective
  4-Nov-2025; 78_ ≥2015 print with retention regime 1-Aug-2006; 79_ AG
  125-2022 stamp on art. 32. (FR-236..246)
- **AC-002:** Given the 23_ article inventory, when compared against the
  source, then the lettered/bis set is exactly {10 bis "Derogado", 14-"A",
  23-"A", 24-"A", 24-"B", 52-"A", 57-"A".."D"} and the absent set is
  exactly {3-"A", 7-"A", 8-"A", 25 bis, 29-"A"}; a requirement citing 29-"A"
  or 25 bis to 23_ fails validation. (FR-238)
- **AC-003:** Given any citation the system emits, when inspected, then it
  carries a register cutoff qualifier (e.g. "D-27-92 (texto ≤ D-10-2012)")
  and a bare citation is a CI failure. (FR-248, FR-260)
- **AC-004:** Given a current-law IVA row citing D-27-92 without the
  "reformado por… (≥ D-4-2019 / D-31-2024 / D-10-2025)" leg, when the CI
  gate runs, then the build fails naming FR-249. (FR-249, FR-260)
- **AC-005:** Given seeded requirement data containing any myth string
  ("resolución 2-2010", "Art. 3-'A'", "ISR = Dto. 26-92", "ISR anual =
  SAT-1371", "LAT ≤2013", "2236", "propinas" as art. 68 num. 1 content, or
  a CT art. 120 ¶ citation as live law), when validated, then each is
  rejected with its correction (D-20-2006+AG 425-2006 / 8-"A" / LAT
  D-10-2012 / SAT-1411-1431 per R46 / through D-46-2022 / rejected legacy /
  26_ governs / 98"A".2). (FR-252, FR-260)
- **AC-006:** Given an ISR requirement citing Dto. 26-92 as current law
  (post-1-Jan-2013), or a form-number citation resolving to 78_/79_ or to
  SAT-1371 as the annual ISR form, when validated, then it fails (LAT art.
  180.1 derogation; R46 mapping). (FR-250, FR-251)
- **AC-007:** Given the D-10-2025 delta register, when read, then it holds
  exactly four rows all effective 2025-11-04 — Art. 1 derogating D-27-92
  Art. 8-"A" (added D-31-2024 art. 13), Art. 2 derogating the LAE Art. 16
  final ¶, Art. 3 the budget REFORMA, Art. 4 vigencia — and no row names any
  "3-'A'". (FR-253, FR-254)
- **AC-008:** Given the 74_ defect ledger, when reviewed, then the title
  "168-2017", Tomo "CCCXXVII!", the signature garbles and "3.50»" appear
  verbatim with [sic], none is normalized, and none is citable as data
  until a clean DCA copy verifies it (GOQ-62). (FR-255, FR-256)
- **AC-009:** Given the 23_ instrument row, when inspected, then its
  published-date field is null, the string "Mayo 8 de 1992." is stored as
  unlabelled_strings data, and no computation or citation derives a
  publication date from it (GOQ-63). (FR-257)
- **AC-010:** Given the GOQ-68 finding row, when reviewed, then it records:
  24_ art. 29 sixth paragraph prints the electronic-invoice exception (not
  AG 125-2022 text); zero "125-2022" occurrences in 24_; the in-corpus
  6-month rule lives at ¶4 (AG 222-2019); and the AG 125-2022 acquisition
  flag is set. (FR-258, FR-259)
- **AC-011:** Given a new instrument arriving in `gt/sources/`, when
  registered, then its delta and dates are captured before synthesis writes
  against it and the earlier print's provenance row remains intact
  (append-only). (FR-261)
- **AC-012:** Given the Odoo Mapping table, when checked, then every FR row
  carries a Layer value: register/qualifier/guard data = `shared`, the CI
  validation gate = `saas`. (FR-236..261)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text verbatim from the register. Owned: GOQ-62/63/68/69; kin:
GOQ-01/13 (already S-GT1/S-GT2-cited). All rows trace-pending, not
blockers; the GOQ-68 in-corpus leg is resolved in this file (FR-258) —
master-index annotation is the controller's.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-62 (owned): "74_ OCR noise: Tomo "CCCXXVII!" [sic], title "168-2017" [sic], signature garbles, "3.50»" — verify vs clean DCA before quoting." Affects FR-256 (defect strings non-citable until verified). | no | GT synthesis wave S-GT2 → acquisition queue (clean DCA 4-Nov-2025 No. 40 copy) | open |
| OQ-002 | GOQ-63 (owned): "23_ ends with unlabelled "Mayo 8 de 1992." — plausibly the DCA date but unlabeled; do not cite as publication date." Affects FR-257 (published = null on the 23_ row). | no | GT synthesis wave S-GT2 → external confirmation (DCA archive Jun-1992) | open |
| OQ-003 | GOQ-68 (owned): "AG 125-2022 + "sexto párrafo del artículo 29 del Reglamento IVA" FEL-transition texts: 79_ art. 32 cites both; AG 125-2022 not in corpus — check 24_ art. 29 ¶6 in-corpus at synthesis; acquire AG 125-2022 if needed." **In-corpus check done in this file (FR-258, 2026-08-20): NEGATIVE — 24_ art. 29 ¶6 prints the electronic-invoice exception; no AG 125-2022 text anywhere in 24_; acquisition need confirmed (DOWNLOAD_QUEUE rev 7).** Acquisition leg remains open. | no | GT synthesis wave S-GT2 → acquisition queue (AG 125-2022 full text) | open (in-corpus leg resolved 2026-08-20) |
| OQ-004 | GOQ-69 (owned): "78_/79_ print no DCA dates: the retention chapters are fixed-date (1-ago-2006) but arts. 38/51/52/53/58/59/60/62 = DCA+8d, undateable." Affects FR-245/FR-246 (published = null; DCA+8d articles carry rule strings, not dates). | no | GT synthesis wave S-GT2 → acquisition queue (DCA Jul-2006 dates) | open |
| OQ-005 | GOQ-01 (kin, register lists TX1/TX2/TX3 freeze): "Post-2018 consolidated Ley IVA 27-92 text: Art. 29-'A' body, Ley 25 bis adder (electronic 100% refund), art. 54 B/BIS nomenclature, post-2012 exemption families (peaje/turismo/canasta), Q150,000 currency." Affects FR-238 (absent-articles), FR-249 (never-alone qualifier). | no | GT synthesis wave S-GT2 → acquisition queue (DCA Edición Legal / accountant) | open |
| OQ-006 | GOQ-13 (kin): "D-31-2024 full text acquisition (added IVA 8-'A'; LAE changes; the 5 new DTE types FEPE/FARP/FCRP/FPEC/FCPC; ICT definition) + clean-DCA verification of D-10-2025's "8 'A'" reading (OCR 8/3 residue)." Affects FR-254 (delta row recorded as printed — "3-'A'" never existed). | no | GT synthesis wave S-GT2 → acquisition queue (shared with S-GT1) | open |
