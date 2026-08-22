# HN — Fiscal reporting — OTCD tarjetas: códigos 215/523 + devolución 8%

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN3 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Honduras OTCD
(*operadoras/administradoras/concesionarios de tarjetas de crédito o débito* —
card issuers, operators and concessionaires) fiscal-reporting surfaces of
master-index cluster **W2-F4**: the two-declaration tarjetas regime — código
**215** (*Declaración Jurada Determinativa* de la retención ISV por tarjetas,
OVI-only, single Base de Cálculo = 10% of the ISV caused on affiliates' taxed
card transactions MINUS the *devolución* 8% (refund) of the ISV effectively
paid) and código **523** (per-transaction *informativa* (informational
declaration), Servicio Web-only, casillas 2/461/4611/462/466) — both filed by
the SAME OTCD agent within the first 10 días calendario of the following
month; the R-H16 catalog boundary (both codes sit OUTSIDE the 25-code DJIMR
catalog — never modeled as DJIMR códigos); the SAR-240-2024 numerales IX-XIII
rewrite (per-merchant monthly detail INCLUDING the *Importe de la Devolución
8%* field — the 8% refund is operationally ALIVE per R-H22 — plus the
excepted-subject *agente de información* reporting duty and the *pago parcial*
(partial payment) character of the retention for affiliates); the
devolución-8% declaration-side surface (suspension history and when-it-applies
instruments unacquired — LEAD `41_ OQ-3`); the BCH-only payment channel
(dated operational data); and the 523-before-215 ordering guidance.

It does **not** cover: the retention computation itself — the 10%-of-tax
retention, the 15% no-discrimination fallback, the monthly banking entero and
the devolución-8% right/computation are owned by
[taxation/06_isv.md](../taxation/06_isv.md) and consumed here BY ID
(HN-TAX-FR-248/249/250/255); the DJIMR/DMR per-código engine and its catalog
(S-HN3 file 02, cluster F2 — boundary only here, guard complementing
HN-FREP-FR-049); the OVI/SW filing chassis,
plantilla pipeline and fiscal calendar (S-HN3 file 01, cluster F1 — consumed
as scope note); the affiliate's ISV determinativa 201 and its OTCD-credit
casillas (S-HN3 file 05 = HN-FREP-FR-175 feed c — this file supplies the
per-affiliate aggregate feed; mechanics VERIFY, OQ-006); the retention comprobante document
contract (e-invoicing E6, [../e-invoicing/03_document-mechanics.md]
(../e-invoicing/03_document-mechanics.md)); and CT sanctions/procedure
(taxation/01, T11 frame — hookup flag only).

## 2. Legal Basis

Authority order (binding, per master evidence index): SAR-240-2024 (tarjetas
IX-XIII) is the operative procedure instrument; Resolución DEI-9382-J-2003 =
base procedure (lead — numerales I-VIII unacquired); `71_` Generalidades =
compilation, cite per-row only, never §4 (R-H27); Ayudas `41_`/`42_` =
per-código field/flow authority (operational, DATED prints post-May-2024,
no print date); SAR-238-2024 CUARTO = the DJIMR catalog boundary. Statutory
anchors (Ley ISV Art. 8; LET Art. 18; D. 113-2011 Arts. 3-4; D. 278-2013
Arts. 20-21; D. 7-2017; CT Art. 211) enter only as evidenced in the
EV13/EV31 base-legal lists — several unacquired (LEAD). D-H1/D-H2/D-H2.5/
D-H3 bind (dated rows, filed-period freeze, ingestion depths).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo SAR-240-2024, numerales IX-XIII y SEGUNDO (10-may-2024, La Gaceta 36,538, 20-may-2024) | IX: agents must supply SAR "por cada mes calendario y **por cada sujeto pasivo de retención**: 1. Nombre, Razón o Denominación Social y Clave del Registro Tributario (RTN); 2. Valor bruto de la transacción, y fecha en que se practicó la retención; 3. **Importe de la Devolución 8%**" — "por medio del llenado de la Declaración a través del Servicio Web." X: agents "deben también actuar como Agente de Información e Informar ... las operaciones que realizan con los Sujetos alcanzados por la excepción prevista en el numeral VI" — name/razón + RTN, "Importe pagado y fecha en que se efectúo la liquidación", via Servicio Web. XI: "dentro de los primeros diez (10) días calendario del mes siguiente al que se efectuó la liquidación que dio lugar a la retención, a través del Servicio Web." XII: "El importe retenido consignado en el comprobante previsto en el numeral IV ... tendrá para los responsables del tributo el carácter de **pago parcial**, tal concepto será computado en la 'Declaración Jurada de Retención de Impuesto Sobre Ventas por Tarjetas de Crédito o/y Débito' del periodo fiscal en que se efectuó la liquidación." XIII: non-presentation/non-entero → CT sanction + Boletín de Pago. SEGUNDO: rectifications "a través del Servicio Web, de conformidad a la periodicidad establecida en el Código Tributario" | `hn/sources/19_Acuerdo_SAR-240-2024_ISV_tarjetas_mod.pdf` | 240-IX..XIII + SEGUNDO pp.3-4 (EV13:EVID-088/089) |
| LB-002 | Resolución No. DEI-9382-J-2003 — **LEAD (unacquired; numerales I-VIII outside corpus)** | Base procedure of the whole tarjetas regime, as recited in SAR-240-2024 considerandos: "emitida ... en fecha 23 de octubre de 2003 y publicada ... 01 de noviembre de 2003"; the original contemplated an informativa "dentro de los primeros diez días calendarios del mes siguiente al que se efectuó la liquidación"; 71_ row cites it as "Resolución número DEI-9382-J-2003 (procedimiento de presentación)". Numerales I-VIII un-acquired: the numeral-IV retention comprobante and the numeral-VI exception text are known only by reference | `hn/sources/19_Acuerdo_SAR-240-2024_ISV_tarjetas_mod.pdf`; `hn/sources/71_Generalidades_DMR.pdf` | 19_ considerandos pp.2-3 (EV13:EVID-088); 71-§3 p.3 (EV31:EVID-125) |
| LB-003 | Ayuda 41_ — DJ Determinativa Retención ISV por Tarjetas Débito/Crédito, código 215 (SAR manual; undated print, post-May-2024 — DATED DATA) | Sujetos: "Se designa a los contribuyentes emisores u operadoras y concesionarios de servicios de tarjetas de crédito o débito como agentes de retención del impuesto sobre ventas causado por las transferencias de bienes o prestación de servicios gravados y realizados por los negocios afiliados, cuando reciban el pago con el uso de tarjetas de crédito de sus clientes (Articulo 8, Ley del Impuesto Sobre Ventas)". Forms: "215 \| Determinativa \| Oficina Virtual" [description cross-wired with 523 naming — `41_ OQ-1`]. Plazo: OTCD "deben enterar a través del sistema bancario la totalidad de los montos retenidos en cada mes, a más tardar dentro de los primeros diez (10) días calendario del mes siguiente en el que se practicó la retención... (Ley del Impuesto Sobre Ventas… Artículo 8)". Base casilla: "Casilla Base de Calculo: consignará el valor que resulte de la retencion del 10% del Impuesto Sobre Ventas causado en las transacciones de bienes y servicios gravados de sus afiliados menos el valor de la devolucion del 8% del importe del impuesto efectivamemte [sic] pagado". Payment: "deberá seleccionar el botón 'Boletín de pago' descargarlo e imprimirlo y realizar el pago en el Banco Central de Honduras". Base-legal list: "Ley del Impuesto Sobre Ventas… Decreto-Ley Número 24; Artículo 8. / Ley de Equidad Tributaria (Decreto 51-2003); Artículo 18. / Ley de Eficiencia… (Decreto 113-2011); Artículos 3 y 4. / Ley de Ordenamiento de las Finanzas Públicas… (Decreto 278-2013); Artículo 20 y 21. / Decreto 7-2017 Reforma el párrafo sexto del Art.8… / Acuerdo 240-2024" | `hn/sources/41_Ayuda_ret_ISV_tarjetas_215.pdf` | 41-§I.2 p.4; §I.4 p.5; §I.7-8 p.6; §2.2 p.11; p.14; rectification pp.16-19 (EV31:EVID-123) |
| LB-004 | Ayuda 42_ — DJ Informativa Retención ISV por Tarjetas (ATC), código 523 (SAR manual; undated print, post-May-2024 — DATED DATA) | Forms: "Declaración Jurada de Retención de Impuesto Sobre Ventas por Tarjetas de Crédito o/y Débito" (ATC) \| 523 \| Informativa \| Servicio Web (SW)". Pairing: "es 523 - Declaración Agencias Tarjetas de Crédito (A.T.C.)… En el Tipo de la declaración selecciona informativa, recuerde que después se debe presentar la determinativa la cual corresponde al código de Impuesto 215". Plazo: "dentro de los primeros diez (10) días calendario del mes siguiente al que se efectuó la liquidación que dio lugar a la retención, a través del Servicio Web… (Acuerdo 240-2024 numeral XI)". Casillas: "2-RTN: debe ingresar el Registro Tributario Nacional (RTN) del negocio afiliado. 461-Fecha transacción… formato texto (DD/MM/AA). 4611-Valor bruto transacción: consigne el valor de la transacción antes de Impuesto Sobre Ventas. 462-Impuesto pagado; agregar el importe total del Impuesto Sobre Ventas de la transacción ya sea que este corresponda al 15% o 18%. 466-Nº Tipo de transacción: agregue la palabra Retenido o Exento… por exento aquella transacción que no está sujeta a dicha retención". Recommendation: "Realice la presentación de la declaración informativa código 523 y posteriormente la declaración determinativa código 215". Base-legal list identical to 41_ | `hn/sources/42_Ayuda_ATC_523.pdf` | 42-§I.4-8 pp.5-6; §2.1B pp.8-9; §2.2 p.11; p.20 (EV31:EVID-124) |
| LB-005 | 71_ Generalidades DMR, tarjetas row (compilation — cite per-row only, R-H27) | "215 D / 523- I \| Retención ISV Por Tarjetas de Débito o Credito \| 15% 18%" with base legal "Artículo 8, Ley ISV / Artículo 3, Decreto 113-2011 (Devolución 8%) / Artículo 21, Decreto 278-2013 / Artículo 211, Decreto 170-2016 / Artículo 1, Decreto No.7-2017 / Resolución número DEI-9382-J-2003 (procedimiento de presentación) / Acuerdo No. SAR-240-2024"; the "15% 18%" column = the ISV rate tags of the underlying transactions, NOT a retention alícuota | `hn/sources/71_Generalidades_DMR.pdf` | 71-§3 p.3 (EV31:EVID-125) |
| LB-006 | Ley del Impuesto Sobre Ventas (D.L. 24), Art. 8 | The OTCD designation statute: card issuers/operators/concessionaires as retention agents on affiliates' taxed transactions; article text (10%-of-tax retention, no-discrimination fallback, monthly banking entero) OWNED by taxation/06 LB-009 — consumed by id here, never re-derived | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 8 (as restated 41-§I.2/§I.8, EV31:EVID-123; article text = taxation/06 LB-009 by id) |
| LB-007 | Ley de Equidad Tributaria (D. 51-2003), Art. 18 — **LEAD (unacquired)** | Cited in the 41_/42_ base-legal lists as a devolución-8%-family anchor; text not in corpus — one of the three when-it-applies instruments of `41_ OQ-3` | `hn/sources/41_Ayuda_ret_ISV_tarjetas_215.pdf` | 41-§I.7 p.6 (EV31:EVID-123); same list 42-§I p.6 (EV31:EVID-124) |
| LB-008 | Ley de Eficiencia (D. 113-2011), Arts. 3 y 4 — **LEAD as to this wave** | Cited in the 41_/42_ base-legal lists; 71_ flags "Artículo 3, Decreto 113-2011 (Devolución 8%)"; the article text (8% right of natural persons; OTCD processing/reporting; D. 278-2013 Art. 21 / D. 170-2016 / D. 7-2017 reform chain of Art. 4) is OWNED by taxation/06 LB-016/LB-017 — consumed by id here | `hn/sources/41_Ayuda_ret_ISV_tarjetas_215.pdf` | 41-§I.7 p.6 (EV31:EVID-123); 71-§3 p.3 (EV31:EVID-125) |
| LB-009 | Ley de Ordenamiento de las Finanzas Públicas (D. 278-2013), Arts. 20 y 21 — **ACQUIRED W9 as `130_` (G 33,316 30-dic-2013; vigencia 01-ene-2014)** | Art. 20 = the devolución-8% SIX-MONTH SUSPENSION, verbatim: "Dejar en suspenso por el término máximo de seis (6) meses a partir del día que entre en vigencia el presente Decreto, la aplicación del Artículo 3 de la Ley de Eficiencia «…» contentivo de la devolución del ocho por ciento (8%) «…» con el objetivo de que las [OTCD] ajusten sus sistemas «…» la discriminación del importe del Impuesto Sobre Ventas causado, incluso cuando el mismo sea igual a cero (0) [...] Si en el término citado no se cumple con el cometido se les impondrá la sanción establecida en el Artículo 179 del Código Tributario" — a SELF-EXPIRING suspension (01-ene-2014 → outer bound 30-jun-2014), not a repeal; Art. 21 = the OTCD retention-numerals rewrite with the **2013-vintage 50% retention** ("Las OTCD deben aplicar una retención del cincuenta por ciento (50%) de manera automática sobre el monto total del Impuesto Sobre Ventas que sea causado") — the pre-D. 7-2017 state of the chain now text-pinned (50% → 10%/15% via D. 7-2017 → SAR-240-2024 IX-XIII per LB-001) | the `41_ OQ-3` when-it-applies RESIDUAL narrows to the post-30-jun-2014 window (no corpus instrument re-suspends; R-H22's operationally-alive-2024 reading consistent) | `hn/sources/130_Gaceta_33316_Decreto_278-2013_Ley_Ordenamiento_Finanzas_Publicas.pdf` | D278-Arts. 20-21 (pp.9-10; EV130:EVID-488) |
| LB-010 | Decreto 7-2017 (reforma el párrafo sexto del Art. 8, Ley ISV) — **LEAD (unacquired)** | Cited in the 41_ base-legal list ("Decreto 7-2017 Reforma el párrafo sexto del Art.8…") and the 71_ row ("Artículo 1, Decreto No.7-2017"); text not in corpus — affects the Art. 8 retention paragraph, content unpinned | `hn/sources/41_Ayuda_ret_ISV_tarjetas_215.pdf` | 41-§I.7 p.6 (EV31:EVID-123); 71-§3 p.3 (EV31:EVID-125) |
| LB-011 | Código Tributario (D. 170-2016), Art. 211 — **LEAD as to content** | Cited in the 71_ tarjetas row base legal ("Artículo 211, Decreto 170-2016"); article content not extracted in this wave's evidence — agents/responsables frame owned by taxation/01 (T11) by id; cited here only as evidenced | `hn/sources/71_Generalidades_DMR.pdf` | 71-§3 p.3 (EV31:EVID-125) |
| LB-012 | Acuerdo SAR-238-2024, CUARTO (10-may-2024, La Gaceta 36,538, 20-may-2024) — the DJIMR catalog boundary | "Las retenciones que se informen en cada una de las DJIMR, serán conforme a los siguientes Códigos de Impuestos: 1) DJIMR-111 … 25) DJIMR-254" — the exhaustive 25-code catalog contains NO 215 and NO 523: both tarjetas declarations file OUTSIDE the DJIMR system (R-H16), under the DEI-9382-J-2003/SAR-240-2024 procedure | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` | 238-CUARTO pp.3-4 (EV13:EVID-077) |
| LB-013 | Acuerdo SAR-236-2024, DÉCIMO SÉPTIMO — **LEAD (unacquired; quoted fragment)** | As quoted in 42_ p.5: Servicio Web modality via "la plantilla proporcionada por el Servicio de Administración de Rentas (SAR)" — the SW plantilla channel basis for 523; full ordinal scope (channel list) un-acquired (`32_ OQ-2` kin) | `hn/sources/42_Ayuda_ATC_523.pdf` | 42-§I.4 p.5 (EV31:EVID-124) |
| LB-014 | **D. 7-2017 ACQUIRED W10** (`152_`, G 34,284 Miércoles 8-mar-2017; the OTCD chain middle instrument): Art. 1 reforms ISV Art. 8 ¶6 — **OTCD retention 50% → 10% "de manera automática"** (displacing also the CT-211-2 12%-autónoma interim); **the ¶6 num. 4 15% FALLBACK: "deben aplicar un quince por ciento (15%) de manera automática sobre el monto total cuando no exista discriminación del Impuesto causado en las transacciones" — trigger = NO-DISCRIMINATION of the ISV in the affiliate's records, base = the TRANSACTION TOTAL (monto total), not the tax** (origin of the 10%/15% contract SAR-240-2024 restates); num. 3 = the affiliate duty to register ISV caused even at zero/final-consumer sales, on pain of OTCD automatic registration; Art. 2 interp (10% "cuando exista" the discrimination); **Art. 3 DEROGATES D. 278-2013 Art. 21 (the 50% rule)**. Drift-check vs `05_` consolidation = NONE material (comma + Tarjeta(s) only; the consolidation fills the elided numerales 1/2/5/6/7 — those CRs stand on 05_/EVID-058) | FR-147's regime-state rows statute-dated (50% → 10%/15% at 8-mar-2017); the 15%-fallback trigger/base now primary-text (was manual-inferred); OQ-003 RESOLVED | `hn/sources/152_Gaceta_34284_Decreto_7-2017_reforma_Art8_LISV.pdf` | EV152:EVID-597..601 |

## 3. Functional Requirements

### 3.1 Regime identity, filer and the DJIMR catalog boundary (R-H16)

- **HN-FREP-FR-121:** The system shall model the tarjetas retention reporting
  as a TWO-declaration regime filed by the SAME agent: código 215 =
  *declaración jurada determinativa* (determinative sworn declaration,
  Oficina Virtual only) and código 523 = *declaración jurada informativa*
  (informational sworn declaration, Servicio Web only, per-transaction
  detail), per the 42_ pairing text "En el Tipo de la declaración selecciona
  informativa, recuerde que después se debe presentar la determinativa la
  cual corresponde al código de Impuesto 215". (LB-003; LB-004; LB-005;
  EV31:EVID-123/124/125)
- **HN-FREP-FR-122:** The system shall configure the filer as the OTCD
  itself — "contribuyentes emisores u operadoras y concesionarios de
  servicios de tarjetas de crédito o débito" designated retention agents per
  Art. 8 Ley ISV — and shall never generate 215/523 filings for the
  *negocios afiliados* (affiliated merchants), whose only surface is the
  credit/pago-parcial interface (FR-139/140). (LB-003; LB-006;
  EV31:EVID-123)
- **HN-FREP-FR-123:** The system shall enforce the R-H16 catalog boundary:
  the 25-code DJIMR catalog (SAR-238-2024 CUARTO) contains neither 215 nor
  523, so the DJIMR informativa→SER two-step chassis, the per-código DJIMR
  generator and any de-oficio rectification propagation are NEVER applied to
  the tarjetas codes — they file under the DEI-9382-J-2003/SAR-240-2024
  procedure as stand-alone declarations; this guard complements the
  retention-code catalog seed of file 02 (HN-FREP-FR-049 — 25 rows, join
  key, no 215/523 rows ever added outside a new SAR instrument).
  (LB-001; LB-012; EV13:EVID-077; EV31:EVID-124; R-H16)
- **HN-FREP-FR-124:** The system's internal declaration catalog shall treat
  code+tipo as authoritative for the tarjetas rows — 215/Determinativa and
  523/Informativa — and shall ignore the cross-wired form-table description
  text ("Declaración Retención de Administrados de Tarjeta de Crédito y
  Débito (ATC)" printed on the 215 row, ATC naming belonging to 523) and the
  ATC expansion drift ("Agencias…" vs "Administrados…"): no gloss is
  encoded, only code+tipo+channel. (LB-003; LB-004; EV31:EVID-123/124;
  `41_ OQ-1`)
- **HN-FREP-FR-125:** The system shall carry the procedure as DATED regime
  rows (D-H2): DEI-9382-J-2003 base procedure (published 01-nov-2003,
  original informativa within the first 10 días calendarios after the
  liquidation month) → SAR-240-2024 rewrite, `valid_from` 2024-05-20
  (publication date, La Gaceta 36,538), numerales IX-XIII operative; months
  before 2024-05-20 resolve to the pre-240 regime row for reconstruction and
  never silently to the rewritten text. (LB-001; LB-002; EV13:EVID-088)

### 3.2 Código 523 — SW-only per-transaction informativa

- **HN-FREP-FR-126:** The system shall generate, per calendar month, one 523
  informativa whose lines are the per-transaction detail of the period's
  card settlements, with the casilla contract: 2 = affiliate RTN
  (*negocio afiliado*), 461 = transaction date (text format DD/MM/AA), 4611
  = *Valor bruto transacción* (gross transaction value BEFORE ISV), 462 =
  *Impuesto pagado* (total ISV of the transaction), 466 = *Nº Tipo de
  transacción* with the literal word Retenido or Exento. (LB-004;
  EV31:EVID-124)
- **HN-FREP-FR-127:** The system shall tag every 523 line's ISV amount
  (casilla 462) with the underlying rate tier — 15% or 18% — resolved from
  the transaction's ISV computation (rate matrix owned by taxation/06,
  consumed by id), including lines where the amount arose from the
  no-discrimination fallback (taxation/06 HN-TAX-FR-249). (LB-004; LB-005;
  EV31:EVID-124/125)
- **HN-FREP-FR-128:** The system shall operationalize casilla 466 as the
  line-level retention-eligibility flag: Retenido for transactions subject
  to the 10%-of-tax retention; Exento — "por exento aquella transacción que
  no está sujeta a dicha retención" — for transactions of subjects reached
  by the DEI-9382 numeral-VI exception and other non-subject cases, with
  Exento lines also feeding the excepted-subject report of FR-142.
  (LB-004; EV31:EVID-124; EV13:EVID-089)
- **HN-FREP-FR-129:** The system shall file 523 through the Servicio Web
  channel ONLY (no OVI-card alternative exists for 523), consuming the SW
  plantilla pipeline — versioned plantilla download, text-formatted cells,
  upload, orden de trabajo, two-stage validation, buzón error loop — from
  the S-HN3 filing-chassis file (cluster F1) by scope reference (file 01;
  FR ids cross-referenced once that file exists — OQ-008). (LB-004; LB-013;
  EV31:EVID-124/127)
- **HN-FREP-FR-130:** The system shall anchor the 523 deadline to the
  liquidación: presentation "dentro de los primeros diez (10) días
  calendario del mes siguiente al que se efectuó la liquidación que dio
  lugar a la retención, a través del Servicio Web" (SAR-240-2024 numeral
  XI) — días CALENDARIO, monthly cadence. (LB-001; LB-004; EV13:EVID-089;
  EV31:EVID-124)
- **HN-FREP-FR-131:** The system shall compute, per calendar month and per
  *sujeto pasivo de retención* (each affiliate RTN), the SAR-240-2024
  numeral-IX merchant summary — (1) name/razón social + RTN, (2) *Valor
  bruto de la transacción* + retention date, (3) *Importe de la Devolución
  8%* — and shall carry the devolución amount as a first-class field of the
  tarjetas ledger (the 8% is operationally ALIVE in the 2024 text, R-H22);
  the printed 523 casillas (2/461/4611/462/466) contain NO devolución
  column, so the casilla↔plantilla mapping of the IX field stays unpinned
  and the payload keeps the amount regardless (OQ-004). (LB-001; LB-004;
  EV13:EVID-088; EV31:EVID-124; R-H22)

### 3.3 Código 215 — OVI-only determinativa

- **HN-FREP-FR-132:** The system shall generate the monthly 215
  determinativa with the single *Base de Cálculo* semantics verbatim:
  "el valor que resulte de la retencion del 10% del Impuesto Sobre Ventas
  causado en las transacciones de bienes y servicios gravados de sus
  afiliados menos el valor de la devolucion del 8% del importe del impuesto
  efectivamente pagado" — i.e. base = (0.10 × ISV caused on affiliates'
  taxed card transactions) − (devolución 8% of the ISV effectively paid),
  floored-at-zero behavior NOT asserted (no corpus evidence of a floor —
  negative bases pass through as printed and are flagged). (LB-003;
  EV31:EVID-123)
- **HN-FREP-FR-133:** The system shall consume the retention computation
  inputs BY ID from taxation/06 — the 10%-of-tax retention split
  (HN-TAX-FR-248), the 15% no-discrimination fallback (HN-TAX-FR-249), the
  monthly banking entero aggregate (HN-TAX-FR-250) and the devolución-8%
  right/suspension-history rows (HN-TAX-FR-255) — never re-deriving rates,
  bases or the 8% computation in this file; this file owns only the
  declaration aggregation and the base-formula wiring of FR-132.
  (LB-003; LB-006; LB-008; EV31:EVID-123/125)
- **HN-FREP-FR-134:** The system shall anchor the 215 deadline to the
  retention: enterero "a más tardar dentro de los primeros diez (10) días
  calendario del mes siguiente en el que se practicó la retención" (as
  restated by 41_ citing Ley ISV Art. 8) — días CALENDARIO, monthly
  cadence; where a month's retentions and liquidaciones diverge, each
  record keys on its own anchor month (FR-138). (LB-003; LB-006;
  EV31:EVID-123)
- **HN-FREP-FR-135:** The system shall file 215 through the Oficina Virtual
  channel ONLY (no Servicio Web path exists for 215; no DJIMR informativa
  pairs with it), consuming the OVI declaration lifecycle from the S-HN3
  chassis file (cluster F1) by scope reference (OQ-008). (LB-003;
  EV31:EVID-123/127)
- **HN-FREP-FR-136:** The system shall route 215 payment as a DATED
  operational row: Boletín de pago printed/downloaded and paid at the
  Banco Central de Honduras (BCH) — unique among the declaration family;
  `valid_from` = the 41_ manual print (post-May-2024, read 2026-08-20),
  with the channel re-verifiable and never assumed for other codes or
  periods (OQ-002). (LB-003; EV31:EVID-123)
- **HN-FREP-FR-137:** The system shall support rectification of both
  declarations per SAR-240-2024 SEGUNDO ("a través del Servicio Web, de
  conformidad a la periodicidad establecida en el Código Tributario") with
  the 41_ OVI side-by-side original-vs-corrected presentation and
  Rectificada-OT states, under D-H2.5 filed-period freeze: the filed
  original snapshot is never mutated, rectifications create new versions;
  NO de-oficio determinativa propagation is modeled for 215/523 (that
  mechanic is DJIMR-chassis-specific, FR-123). The channel nuance
  (SEGUNDO's SW text vs 41_'s OVI rectification walkthrough for 215) is
  carried as OQ-007. (LB-001; LB-003; EV13:EVID-089; EV31:EVID-123)

### 3.4 Pago parcial character and the affiliate credit interface

- **HN-FREP-FR-138:** The system shall stamp every OTCD retention record
  with its *liquidación* period (the settlement that gave rise to the
  retention) and its retention date, both deadlines (FR-130/134) resolving
  from those anchors, and every 523 line and 215 aggregation keying on the
  same period. (LB-001; LB-003; LB-004; EV13:EVID-088/089; EV31:EVID-124)
- **HN-FREP-FR-139:** The system shall stamp the retained amount consigned
  in the numeral-IV comprobante with *pago parcial* (partial-payment)
  character for the *responsables del tributo* (the affiliates), per
  SAR-240-2024 XII: "tendrá para los responsables del tributo el carácter
  de pago parcial, tal concepto será computado en la 'Declaración Jurada de
  Retención de Impuesto Sobre Ventas por Tarjetas de Crédito o/y Débito'
  del periodo fiscal en que se efectuó la liquidación" — the retention is
  a partial payment of the affiliate's ISV, never a definitive tax.
  (LB-001; EV13:EVID-089)
- **HN-FREP-FR-140:** The system shall produce the per-affiliate monthly
  aggregate (RTN + retained amounts + pago-parcial character + devolución-8%
  amount) as the feed for the affiliate's ISV determinativa 201 OTCD-credit
  surface, owned by S-HN3 file 05 = HN-FREP-FR-175 feed (c)
  (*Impuesto Retenido por Ventas de Crédito o Débito*; feed value
  `otcd_tarjetas`) — whether the credit enters the affiliate's 201 as a
  credit line, a separate casilla or a débito reduction is OPEN (`02_ OQ-1`,
  shared with file 05 OQ-012 and taxation/06 OQ-001; OQ-006).
  (LB-001; LB-003; EV13:EVID-089; EV31:EVID-123)
- **HN-FREP-FR-141:** The system shall carry on every retention record the
  reference to the retention comprobante of DEI-9382-J-2003 numeral IV
  (the voucher whose consigned amount carries the pago-parcial character);
  the comprobante's own document contract = e-invoicing E6
  (../e-invoicing/03_document-mechanics.md) and taxation/06 HN-TAX-FR-248
  by id — here only the reference field (numerales I-VIII unacquired,
  OQ-009). (LB-001; LB-002; EV13:EVID-089)

### 3.5 Excepted-subject information duty (SAR-240-2024 X)

- **HN-FREP-FR-142:** The system shall generate the *agente de información*
  report for operations with subjects reached by the DEI-9382 numeral-VI
  exception ("Sujetos alcanzados por la excepción prevista en el numeral
  VI"): per subject, name/*razón social* + RTN, *Importe pagado* (amount
  paid) and *fecha en que se efectúo la liquidación* (settlement date),
  presented via Servicio Web; the numeral-VI exception text is unacquired
  (LEAD, OQ-009) and its subject set is configuration, never hardcoded.
  (LB-001; LB-002; EV13:EVID-089)
- **HN-FREP-FR-143:** The system shall file the excepted-subject report on
  the same monthly cadence and channel as 523: "dentro de los primeros diez
  (10) días calendario del mes siguiente al que se efectuó la liquidación…
  a través del Servicio Web" (numeral XI), reusing the SW pipeline and
  period anchoring of FR-129/130. (LB-001; LB-004; EV13:EVID-089;
  EV31:EVID-124)

### 3.6 Filing calendar and ordering

- **HN-FREP-FR-144:** The system shall create monthly fiscal-calendar rows
  for both codes — 215 (OVI) and 523 (SW) — each due within the first 10
  días calendario of the following month, conditioned on the company's
  vector-fiscal *alta* state for the obligation (alta/eventual on-ramps =
  S-HN3 chassis file 01 by scope reference, OQ-008); both rows carry the
  SAR-240-2024 `valid_from` regime stamp of FR-125. (LB-001; LB-003;
  LB-004; EV13:EVID-088/089; EV31:EVID-123/124)
- **HN-FREP-FR-145:** The system shall surface the filing-order guidance —
  "Realice la presentación de la declaración informativa código 523 y
  posteriormente la declaración determinativa código 215" — as a SOFT
  warning when 215 is generated/filed before 523 of the same period
  (default non-blocking), because whether OVI enforces the ordering is
  unpinned; a config flag may promote the warning to a block once verified
  (OQ-005). (LB-004; EV31:EVID-124)

### 3.7 Devolución 8% declaration surface and sanctions hookup

- **HN-FREP-FR-146:** The system shall maintain the devolución-8%
  declaration-side ledger — per merchant per month the *Importe de la
  Devolución 8%* (FR-131), netted in the 215 base (FR-132) — with its
  status carried as DATED rows consumed from taxation/06 HN-TAX-FR-255:
  operationally ALIVE (R-H22; SAR-240-IX field + 215 base), suspension
  history = D. 278-2013 Art. 20 six-month suspension (~30-dic-2013) as
  history rows; this file owns no 8% computation or eligibility logic.
  (LB-001; LB-003; LB-009; EV13:EVID-088; EV31:EVID-123; R-H22)
- **HN-FREP-FR-147:** The system shall implement the 8% leg of the 215
  base formula as a DATED configuration toggle bound to the FR-146 status
  rows (periods with an alive row → netting applies; suspension-window
  periods → the leg contributes zero and the run records the regime state),
  never silently dropping the leg and never hardcoding it on — because WHEN
  the 8% applies is unpinned (D. 113-2011 Art. 3 / LET Art. 18 / D.
  278-2013 Arts. 20-21 all cited, none acquired — LEAD, OQ-003).
  **W10: OQ-003 RESOLVED — the three-instrument chain is now complete:
  D. 113-2011 Art. 3 (`05_`, corpus) + LET Art. 18 (`121_`, W8 — the
  retention-agent origin) + D. 278-2013 Arts. 20-21 (`130_`, W9 — Art. 20
  = the six-month self-expiring suspension 01-ene-2014→30-jun-2014 outer
  bound, R-H86; Art. 21 = the 50% retention)** + **D. 7-2017 (`152_`, W10
  — LB-014: Art. 1 reforms ISV Art. 8 ¶6 → 10% automatic; Art. 2 interp;
  Art. 3 DEROGATES D. 278-2013 Art. 21) + SAR-240-2024 (`19_`, IX-XIII
  restatement)**. The toggle semantics stand; the regime-state rows are
  now statute-dated: 50% (30-dic-2013→7-mar-2017, 278-2013-Art.-21) →
  10%-automatic + 15%-no-discrimination-fallback (8-mar-2017, D. 7-2017
  → SAR-240-2024 current procedure).**
  (LB-001; LB-003; LB-007; LB-008; LB-009; LB-014; EV13:EVID-088;
  EV31:EVID-123; EV121:EVID-447; EV130:EVID-490; EV152:EVID-597..601;
  R-H22/R-H86)
- **HN-FREP-FR-148:** The system shall hook non-presentation and
  non-entero of 215/523 to the CT sanction engine as a flag + Boletín de
  Pago attachment (SAR-240-2024 XIII), with the sanction computation and
  procedure owned by taxation/01 (T11 frame) by id — no sanction logic in
  this file. (LB-001; LB-011; EV13:EVID-089; EV31:EVID-125)

## 4. Data Model

Machine-readable sidecars next to this file when produced (none required at
draft — no catalogs beyond the two codes). Layer semantics: Odoo-side
computation/bookkeeping/export data only (see §5). Dated legal parameters
carry `valid_from/valid_to` rows (D15) and resolve as-of the liquidación/
retention month (D-H2); filed declarations are frozen snapshots (D-H2.5).

**Declaration regime rows (D-H2):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.tarjeta.regime (new) | valid_from, valid_to, procedure_instrument, notes | date/char | 2003-11-01 DEI-9382-J-2003 (base) → 2024-05-20 SAR-240-2024 IX-XIII (current, open) | FR-125, FR-144 |
| l10n_hn.tarjeta.payment.channel (new) | valid_from, valid_to, channel | date/select | bch_counter (Banco Central de Honduras, Boletín) — DATED operational row from the 41_ print; re-verify (OQ-002) | FR-136 |

**Declaration objects:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.tarjeta.declaration (new) | code, tipo, period, channel, state, acuse_ref, boletin_ref, rectifies_ref, regime_id | select(215/523)/select(determinativa/informativa)/date/select(ovi/sw)/char | states per F1 chassis (original/rectificada OT…); rectifies_ref chains versions under D-H2.5 freeze | FR-121, FR-124, FR-129, FR-135..FR-137 |
| l10n_hn.tarjeta.txn.line (new) | declaration_id, affiliate_rtn, affiliate_name, txn_date, gross_excl_isv, isv_amount, isv_rate_tag, flag, liquidacion_period, retention_ref | m2o/char/date/monetary/select(15/18)/select(retenido/exento) | casilla map 2/461/4611/462/466; 461 stored date + printed DD/MM/AA text; retention_ref → the FR-141 comprobante reference | FR-126..FR-128, FR-138 |
| l10n_hn.tarjeta.merchant.summary (new) | period, affiliate_rtn, affiliate_name, gross_value, retention_date, devolucion_8_amount | date/char/monetary | the SAR-240-IX triple (name+RTN / bruto+fecha / devolución 8%) — devolución column mapping OQ-004 | FR-131, FR-146 |
| l10n_hn.tarjeta.exempt.report (new) | period, rtn, name, paid_amount, liquidacion_date, channel | date/char/monetary/select(sw) | numeral-VI excepted-subject rows (agente de información duty) | FR-142, FR-143 |
| l10n_hn.tarjeta.retention.record (new) | period, affiliate_rtn, isv_caused, retained_10pct, devolucion_8_amount, pago_parcial (bool), comprobante_numeral_iv, credit_feed_state | date/char/monetary/boolean/char/select | computation inputs consumed from taxation/06 (FR-133); pago_parcial per 240-XII; credit_feed_state → affiliate 201 interface (file 05) | FR-132, FR-133, FR-139..FR-141 |
| l10n_hn.isv.devolucion8 (taxation/06-owned) | status rows | dated rows | alive (R-H22) + D. 278-2013 Art. 20 suspension history — IMPORTED read-only; drives the FR-147 toggle | FR-146, FR-147 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping/export logic
in the LGPL client. No SaaS rows: no DTE-like transmission surface exists in
the corpus (HN filing = OVI/SW web interaction; the Odoo side generates the
payloads/ledgers, transmission is operator-driven through the chassis). The
OVI/SW chassis (login, plantilla pipeline, orden de trabajo, acuse/QR,
boletín caducidad) = S-HN3 file 01 (cluster F1) — consumed by scope
reference (OQ-008); model names stable across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-121, FR-124 | odoo | l10n_hn.tarjeta.declaration + ir.ui selection config | code+tipo+channel | Catalog rows seeded 215/Determinativa/ovi and 523/Informativa/sw; description text never stored as identity (41_ OQ-1) |
| FR-122 | odoo | res.company / res.partner OTCD role | is_otcd_agent | Filer gate: emisores/operadoras/concesionarios per Art. 8 designation; affiliates never file |
| FR-123 | odoo | DJIMR generator guard (file 02 boundary) | exclusion flag | R-H16: 215/523 excluded from the 25-code catalog loop, from DJIMR completeness checks and from de-oficio propagation |
| FR-125 | odoo | l10n_hn.tarjeta.regime | dated rows | D12/D-H2: DEI-9382 (2003-11-01) → SAR-240-2024 (2024-05-20, open); pre-2024-05 months reconstruct on the base row |
| FR-126..FR-128 | odoo | l10n_hn.tarjeta.txn.line | casilla payload | Text-format DD/MM/AA export cell for 461; 15/18 tag from the ISV computation (taxation/06 by id); Retenido/Exento flag drives the exempt report too |
| FR-129, FR-135 | odoo | declaration channel fields + chassis hooks | channel=sw / channel=ovi | 523 SW-only (240-XI; SAR-236 DÉCIMO SÉPTIMO fragment); 215 OVI-only; chassis FR ids = file 01 (OQ-008) |
| FR-130, FR-134 | odoo | l10n_hn.fiscal.calendar rows | due-day rows | Both first-10-días-calendario rows; 523 anchored to liquidación month (240-XI), 215 to retention month (41_/Art. 8 restatement); hábil/calendario per-instrument discipline (04_ OQ-3 kin) — both calendario here |
| FR-131 | odoo | l10n_hn.tarjeta.merchant.summary | devolución_8_amount | 240-IX field alive (R-H22); casilla mapping open (OQ-004) — payload keeps the amount regardless |
| FR-132, FR-133 | odoo | l10n_hn.tarjeta.retention.record + python compute | base formula | Base = 0.10 × ISV causado − devolución 8% net; inputs from taxation/06 HN-TAX-FR-248/249/250/255 by id; no floor asserted (flag on negative) |
| FR-136 | odoo | l10n_hn.tarjeta.payment.channel | dated row | BCH-only Boletín route (41_ print, DATED); re-verify before go-live (OQ-002) |
| FR-137 | odoo | declaration rectification chain | rectifies_ref + side-by-side view | D-H2.5 freeze: originals immutable; CT periodicity; no de-oficio propagation (R-H16 boundary); channel nuance OQ-007 |
| FR-138..FR-141 | odoo | retention record stamps | liquidacion_period · pago_parcial · comprobante_numeral_iv · credit_feed_state | Pago-parcial per 240-XII; comprobante contract = e-invoicing E6 + taxation/06 FR-248 by id; 201 credit interface = file 05 HN-FREP-FR-175 feed c (OQ-006) |
| FR-142, FR-143 | odoo | l10n_hn.tarjeta.exempt.report | SW rows | Numeral-VI subject set = config (LEAD OQ-009); same 10-day/SW cadence as 523 |
| FR-144 | odoo | fiscal-calendar generator | two rows/month | alta-conditioned per F1 chassis (file 01 scope); regime-stamped |
| FR-145 | odoo | filing-order soft check | warning flag | Default warn-not-block (42_ OQ-2); config-promotable |
| FR-146, FR-147 | odoo | devolución ledger + config toggle | status-row join | Status rows imported from taxation/06 (HN-TAX-FR-255); suspension window → leg = 0 with regime-state record; never hardcoded on |
| FR-148 | odoo | sanction hookup flag | CT frame by id | CT Art. 160/211 zone = taxation/01 (T11); Boletín attachment only |

Version-regime notes (D12): FR-125/FR-144 record the SAR-240-2024
valid_from 2024-05-20 with no adaptation window (effectivity on
publication); FR-136 records the BCH channel row dated to the 41_ print
(operational, can change without notice); FR-146/147 record the
devolución-8% status/suspension history rows (taxation/06-owned vintage).

## 6. Acceptance Criteria

- **AC-001:** Given the monthly DJIMR completeness run for any period, then
  no 215 or 523 rows are generated and the tarjetas retentions
  appear only in the stand-alone 215/523 declarations (FR-123; R-H16).
- **AC-002:** Given an affiliate card transaction of L1,000.00 + ISV 15%
  (L150.00) settled 2026-01-15 with retention practiced, then the 523 line
  carries RTN, 461 = "15/01/26", 4611 = 1,000.00, 462 = 150.00 tagged 15%,
  466 = "Retenido" (FR-126, FR-127).
- **AC-003:** Given a transaction of a subject configured under the
  numeral-VI exception, then the 523 line flags 466 = "Exento" AND the
  excepted-subject report gains a row (RTN, importe pagado, fecha de
  liquidación) filed SW within 2026-02-10 (FR-128, FR-142, FR-143).
- **AC-004:** Given a month with ISV causado on affiliates' taxed card
  transactions of L30,000.00 and devolución 8% of the ISV effectively paid
  = L1,000.00, then the 215 Base de Cálculo = 0.10 × 30,000.00 − 1,000.00
  = L2,000.00 (FR-132).
- **AC-005:** Given retentions/liquidaciones practiced in January 2026,
  then both the 523 (SW) and 215 (OVI) calendar rows fall due 2026-02-10
  (first 10 días calendario) (FR-130, FR-134, FR-144).
- **AC-006:** Given an operator generating 215 before filing 523 of the
  same period, then a non-blocking ordering warning is raised; given the
  config flag promoted, then generation is blocked (FR-145).
- **AC-007:** Given a filed 215, then its payment artifact = Boletín de
  pago with channel row `bch_counter` (Banco Central de Honduras), and no
  other declaration of this file reuses that channel row (FR-136).
- **AC-008:** Given a retained amount of L3,000.00 consigned in the
  numeral-IV comprobante for affiliate X, then the retention record is
  stamped pago_parcial = true and X's monthly aggregate carries the L3,000
  as a partial payment of X's ISV computable in the liquidación period
  (FR-139, FR-140).
- **AC-009:** Given a merchant-month with devolución 8% = L500.00, then the
  merchant summary row reports Importe de la Devolución 8% = 500.00 and the
  215 base nets it (regime status alive — R-H22) (FR-131, FR-146).
- **AC-010:** Given a rectified 215, then the UI shows original and
  corrected values side-by-side, the state reads Rectificada OT, and the
  original filing snapshot is unchanged on disk (D-H2.5) (FR-137).
- **AC-011:** Given an affiliate card transaction with NO discriminated
  ISV, then the fallback computation (taxation/06 HN-TAX-FR-249) yields the
  ISV amount and the 523 line's 462 carries it tagged 15% (FR-127).
- **AC-012:** Given a period of 2024-04, then the regime row resolves to
  DEI-9382-J-2003 (base); given 2024-06, then to SAR-240-2024 IX-XIII
  (valid_from 2024-05-20) (FR-125).
- **AC-013:** Given a period inside the D. 278-2013 Art. 20 suspension
  window (status row suspended), then the 8% leg of the 215 base
  contributes zero and the run records the regime state; given a 2025
  period, then the netting applies (FR-147).
- **AC-014:** Given the internal declaration catalog, then the 215 row
  identity = (215, determinativa, ovi) and the 523 row = (523, informativa,
  sw), and no ATC description string is stored as identity (FR-121,
  FR-124).
- **AC-015:** Given the per-affiliate aggregate for January 2026, then the
  credit-feed record (RTN, retained, pago-parcial, devolución) is exported
  for the affiliate's 201 surface owned by file 05 — mechanics flagged OPEN
  (OQ-006), never silently applied as a débito reduction (FR-140).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `41_ OQ-1` (carried, C2) [VERIFY]: 215/523 form-table description cross-wiring — the 215 row prints the ATC (523) description; code+tipo authoritative (FR-124). Confirm against a live OVI form table. | no | Takumi S-HN3 | open |
| OQ-002 | `41_ OQ-2` (carried, C2) [CONFIG]: 215 BCH-only payment — "realizar el pago en el Banco Central de Honduras" is unique among the manuals and is DATED operational data (FR-136 dated row); verify the current payment channel before encoding beyond the row. | no | Takumi S-HN3 | open |
| OQ-003 | `41_ OQ-3` (carried, C2) [LEAD] → **RESOLVED W10: the devolución-8% instrument chain is now COMPLETE** — D. 113-2011 Art. 3 (`05_`, corpus) + LET Art. 18 (`121_`, W8 = the card-issuer retention-AGENT origin) + **D. 278-2013 Arts. 20-21 (`130_`, W9: Art. 20 = six-month self-expiring suspension, outer bound 30-jun-2014 — temporal, NOT a repeal)** + **D. 7-2017 (`152_`, W10 = LB-014: 50%→10% reform + 15% no-discrimination fallback + Art. 3 derogation of 278-2013-Art.-21)**. FR-147's dated-toggle reading CONFIRMED and statute-dated; the 8%-leg alive/suspended windows now resolvable from the instrument chain. | no | — | resolved (W10) |
| OQ-004 | `42_ OQ-1` (carried, C2) [VERIFY]: the 523 casillas (2/461/4611/462/466) lack the 240-IX "Importe de la Devolución 8%" column — either 462/466 encode it implicitly or the live plantilla (not the Ayuda) carries the column; verify vs live plantilla (FR-131 keeps the amount in the payload regardless). | no | Takumi S-HN3 | open |
| OQ-005 | `42_ OQ-2` (carried, C2) [CONFIG]: 523-before-215 ordering enforcement unpinned — the 42_ recommendation says 523 first but 41_ is standalone; whether OVI blocks 215 when 523 is unfiled is unknown (FR-145 default = warn). | no | Takumi S-HN3 | open |
| OQ-006 | `02_ OQ-1` (carried, C1) [VERIFY]: OTCD 10%-of-tax retention vs the affiliate's own débito — credit line, separate casilla, or débito reduction on the affiliate's 201? Shared with file 05 (now existing: pinned at HN-FREP-FR-175 feed c, whose OQ-012 carries the same origin) and taxation/06 OQ-001; this file supplies the aggregate feed (FR-140) and never resolves the question. | no | Takumi S-HN3 (files 04+05) | open |
| OQ-007 | File-local [VERIFY]: rectification channel for 215 — SAR-240-2024 SEGUNDO says rectifications "a través del Servicio Web", but 41_ walks an OVI rectification flow for 215 (side-by-side, Rectificativa OT) and 523 is the only SW declaration of the pair; whether 215 rectifications must route SW (or SEGUNDO addresses only the SW declarations) is unpinned (FR-137 encodes channel-follows-declaration). | no | Takumi S-HN3 | open |
| OQ-008 | File-local [CONFIG]: chassis/catalog cross-references to S-HN3 siblings — file 02 pinned (HN-FREP-FR-049 catalog seed, FR-123 guard), file 05 pinned (HN-FREP-FR-175 feed c, FR-140); file 01 (OVI/SW chassis, fiscal calendar, alta/eventual — pre-allocated HN-FREP-FR-001..040, parallel write at drafting time) remains a scope reference — re-pin its ids at wave validation without renumbering this file. | no | Takumi S-HN3 controller | open |
| OQ-009 | File-local [LEAD]: DEI-9382-J-2003 numerales I-VIII unacquired (emitted 23-oct-2003, published 01-nov-2003 — La Gaceta outside ENAG window; SAR-republish route): the numeral-IV retention-comprobante contract and the numeral-VI exception text (subject set of FR-142) remain config-gapped until acquired (LB-002). | no | acquisition queue | open |
