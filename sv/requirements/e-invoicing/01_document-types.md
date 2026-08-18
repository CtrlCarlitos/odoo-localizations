# SV — E-Invoicing — Document types & per-type structures

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave 1 |
| Updated | 2026-08-17 |

## 1. Purpose

This file defines the functional requirements for the 11 El Salvadorian
*documento tributario electrónico* (DTE, electronic tax document) types: legal
identity and purpose of each type, authoritative JSON structure versions under
Normativa de Cumplimiento DTE v2.0, per-type receptor rules and thresholds,
per-type structural constraints (item caps, related-document rules,
contingency eligibility), the v2.0 new/removed fields, and the per-type tax
treatment hooks that decide document behavior (FE IVA-inclusive vs CCFE
net-plus-IVA pricing). It covers what each generated DTE must contain and how
the types map onto Odoo.

It does **not** cover: the transmission connector and API lifecycle
(`02_transmission.md`, cluster A2), the four event types in detail
(`03_events.md`, clusters A3–A5), signing and certificates (`04_signing.md`,
A6), Representación Gráfica / QR / delivery (`05_delivery.md`, A7), the
document state machine and correction windows (`06_state-machine.md`, A8),
catalog governance beyond per-type usage (A9), general tax computation rules
(A10, `taxation/`), onboarding/authorization (A11), or the client↔SaaS private
protocol contract (A12, `07_api-contract.md`). Those files reference this one
for per-type structure.

## 2. Legal Basis

Authority order (binding, per master evidence index): 44_/45_/46_/50_/51_/52_
(2026) > 18_/19_ (2025) > 40_/41_/25_ (2022). Where a conflict was
arbitrated, the resolution id (R1–R16) from the master index is noted.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D.L. 487-2022 (reforma al Código Tributario, régimen DTE), Art. 119-G | Art. 119-G: content requirements per DTE type; FE receptor identification ≥ 3 salarios mínimos mensuales; lifts Art. 115-A correlative authorization | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-G (EVID-083) |
| LB-002 | D.L. 487-2022, Art. 119-E | Art. 119-E: invalidation and post-window CCF/CR adjustment via NC/ND | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-E (EVID-083) |
| LB-003 | Normativa de Cumplimiento DTE v2.0, Anexo II (estructuras) | DTE Compliance Regulation v2.0, Annex II (unified per-type field table, N° 1–175) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo II pp. 48–80 (via DG45 §1) |
| LB-004 | Normativa v2.0, Anexo IV (validaciones DTE) | Annex IV (per-field validation rules) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo IV pp. 102–122 (via DG45 §3.1) |
| LB-005 | Normativa v2.0, Anexo I (especificaciones técnicas) | Annex I (codigoGeneración/numeroControl formats, ECMA-404, Archivo DTE) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I pp. 36–47 (via DG45 §4) |
| LB-006 | Esquemas JSON DTE/Eventos, 11-ago-2026 | Official JSON Schemas (version matrix: fe v2, ccf/nr/nc/nd v4, cr/cl/dcl/fse/cd v2, fex v3) | `sv/sources/52_Json_Schemas_DTE_Eventos_2026-08-11.zip` | schema files (EVID-087) |
| LB-007 | Código Tributario, Arts. 107–115 (sistema de documentos) | Tax Code Arts. 107–115: legal semantics of CCF, Factura, NR, NC/ND, CR, liquidaciones, formal requirements | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 107–115 pp. 39–50 (EVID-060) |
| LB-008 | Ley de Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios (Ley IVA), Art. 57 | IVA Law Art. 57: IVA must appear in the CCF separate from the price | `sv/sources/01_Ley_IVA.pdf` | Art. 57 p. 27 (EVID-048; arbitration R1) |
| LB-009 | Ley IVA, Arts. 62–63 | IVA Law Arts. 62–63: débito/crédito adjustments, 3-month windows | `sv/sources/01_Ley_IVA.pdf` | Arts. 62–63 pp. 27–29 (EVID-054) |
| LB-010 | Ley IVA, Arts. 28–32 | IVA Law Arts. 28–32: *sujetos excluidos* (excluded taxpayers); their invoices carry no IVA surcharge | `sv/sources/01_Ley_IVA.pdf` | Arts. 28–32 pp. 15–16 (EVID-055) |
| LB-011 | Código Tributario, Arts. 112 y 162-A | Tax Code Art. 112 (retention/liquidation documents) and Art. 162-A (2% card perception → DCLE) | `sv/sources/05_Codigo_Tributario.pdf` | Arts. 112, 162-A (EVID-060/062) |
| LB-012 | Código Tributario, Art. 114 | Tax Code Art. 114: CCF/factura formal requirements; factura prices include IVA; ≥ C100,000 (≈ $11,428.57) responsible parties | `sv/sources/05_Codigo_Tributario.pdf` | Art. 114 (EVID-060) |
| LB-013 | Normativa v2.0, Anexos III y V (eventos) | Annexes III/V (event structures and validations; contingency-allowed type lists) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo III pp. 81–101, Anexo V pp. 123–135 (via DG45 §2, §3.2–3.3; R2) |
| LB-014 | Normativa de Cumplimiento DTE v1.2 (17-nov-2025), §§3–7 | DTE Regulation v1.2: generation rules, numeroControl, rounding/holgura (mid authority; yields to 45_ where they overlap) | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §§3–7 pp. 7–12 (EVID-070) |
| LB-015 | Manual de Estructuras y Catálogos (2022) | Structures & Catalogs Manual: 2022 worked per-type structures and fill rules (historical; used only where 45_/52_ are silent, flagged per MOQ-08) | `sv/sources/40_manual_estructuras_catalogo.md` | Anexos 3–12, §V (EVID-005–014, 016–035) |
| LB-016 | Catálogos de Facturación Electrónica v1.1 (jul-2026) | e-Invoicing Catalogs v1.1 (CAT-001..033; machine-readable sidecars) | `sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx` | catalog sheets (EVID-086) |

## 3. Functional Requirements

### 3.1 Shared structure (all or most DTE types)

- **SV-EINV-FR-001:** The system shall support generation of the 11 DTE types with their CAT-002 v1.1 codes: 01 *factura electrónica* (FE, electronic consumer invoice), 03 *comprobante de crédito fiscal electrónico* (CCFE, electronic tax-credit document), 04 *nota de remisión electrónica* (NRE, electronic remission note), 05 *nota de crédito electrónica* (NCE, electronic credit note), 06 *nota de débito electrónica* (NDE, electronic debit note), 07 *comprobante de retención electrónico* (CRE, electronic retention document), 08 *comprobante de liquidación electrónico* (CLE, electronic liquidation document), 09 *documento contable de liquidación electrónico* (DCLE, electronic accounting liquidation document), 11 *factura electrónica de exportación* (FEXE, electronic export invoice), 14 *factura electrónica de sujeto excluido* (FSEE, electronic excluded-subject invoice), 15 *comprobante de donación electrónico* (CDE, electronic donation receipt). (LB-003; LB-016; EVID-086)
- **SV-EINV-FR-002:** The system shall stamp each generated DTE with its authoritative JSON `version` value per the v2.0 matrix: FE=2, CRE=2, CLE=2, DCLE=2, FSEE=2, CDE=2, FEXE=3, CCFE=4, NRE=4, NCE=4, NDE=4. (LB-004 Anexo IV N°1; LB-006; DG45 §1.0; R7)
- **SV-EINV-FR-003:** The system shall generate `codigoGeneracion` as a UUID v4, 36 characters including 4 hyphens, digits and UPPERCASE letters only, unique per document, and shall use it as the document file name base. (LB-005 p.36; LB-004 N°4)
- **SV-EINV-FR-004:** The system shall generate `numeroControl` in the 31-character form `DTE-{tipoDte:2}-{estab/PV:8}-{consecutivo:15}`, where section 3 positions 1–4 are one of "M"/"B"/"S"/"P" followed by 3 digits and positions 5–8 are "P" followed by 3 digits; the consecutive is emitter-assigned (no AT correlative authorization — Art. 115-A is lifted for DTEs), unique within the calendar year, and shall reset at the start of each fiscal year (01-January). (LB-004 N°5; LB-005 pp.36–37; LB-001; EVID-070; R8)
- **SV-EINV-FR-005:** Generated JSON shall follow the unified Anexo II structure (Secciones 1–12, fields N°1–175), emitting only the fields whose Documento column includes the given type, and setting fields to `null` where the Anexo II condition (Requerido / Requerido por tipo de operación / Opcional) requires null for the operation. (LB-003)
- **SV-EINV-FR-006:** The system shall round body fields to 8 decimals (9th decimal ≥ 5 rounds up) and resumen fields to 2 decimals (3rd decimal ≥ 5 rounds up); resumen totals shall be computed from the rounded item values; every computed resumen field shall be accepted within a *holgura* (tolerance) of +$0.01. (LB-014 §3–7; LB-004 resumen rules; EVID-070, EVID-013)
- **SV-EINV-FR-007:** The system shall emit `tipoMoneda` = "USD" for every DTE type. (LB-004 N°12)
- **SV-EINV-FR-008:** The system shall enforce the emission-date windows: `fecEmi` may precede transmission and, in exceptional cases, be up to 5 days after transmission without crossing into the next tax period; `horEmi` accepts a 30-minute holgura when emission falls on the last day of a month. (LB-004 N°10–11)
- **SV-EINV-FR-009:** The system shall emit `identificacion.fusiones` (N°13, applies to NCE, NDE, CRE, CLE) as null when no merger applies, or as a NIT of 9 or 14 digits that exists in the AT's list of merged contributors (*lista de contribuyentes fusionados*, per Art. 69 inc. 1 LST). (LB-003 N°13; LB-004 N°13; DG45 §1.3)
- **SV-EINV-FR-010:** The system shall carry a CAT-008 *distrito* (district) code in the emitter address (N°28) and, where the type includes a receptor address, the receptor address (N°49), each corresponding to the declared CAT-012 departamento / CAT-013 municipio pair. (LB-003 N°28/49; DG45 §1.3)
- **SV-EINV-FR-011:** The system shall emit *domicilioFiscal* (fiscal domicile, CAT-032) in receptor N°53 for CDE and CLE, and in `ventaTercero` N°71 for FE, CCFE, NRE, NCE, NDE and FEXE; code 1 "Domiciliado" requires the third party to hold a NIT registered in IVA. (LB-003 N°53/71; LB-004 N°69–73; DG45 §1.3)
- **SV-EINV-FR-012:** The system shall enforce the structural limits per document: cuerpo maximum 2000 items (CRE and CLE: 500); documentos relacionados maximum 50 documents totaling at most 2000 items; otrosDocumentos 1–10 entries (FEXE: 1–20); apéndice 1–10 entries. (LB-004 N°74 + DG45 §1.5; R10; DCLE cap → OQ-005)
- **SV-EINV-FR-013:** The system shall restrict contingency-mode generation (*modelo facturación* 2 / *tipo transmisión* 2, with CAT-005 tipoContingencia and motivoContingencia) to types 01, 03, 04, 05, 06, 07, 11 and 14 (plus Evento de Retorno 18); CLE, DCLE and CDE shall be generated only with normal prior-transmission mode, their tipoContingencia/motivoContingencia being null. (LB-013 Anexo III Secc.4 / Anexo V N°35 / Anexo IV N°6–9; DG45 §3.3; R2)
- **SV-EINV-FR-014:** The system shall enforce the documentos-relacionados rules: the section is mandatory for NCE and NDE; all related documents within one DTE must be of the same type; only active documents bearing the *sello de recepción* (reception seal) may be referenced (never invalidated or rejected ones); a given document number may be referenced only once per referencing DTE; emitter/receptor roles must correspond to the referenced document. (LB-004 N°14–17; EVID-008)
- **SV-EINV-FR-015:** The system shall enforce the per-type related-document codes and timing: NCE/NDE → 03-CCF or 07-CR, within at most 3 months; FE/CCFE → 04-NR (same period or at most 3 days after) and 09-DCL (same period); FE/CCFE relating an NR must do so within the same period or at most 3 days; FEXE → 04-NR (same period or at most 3 days); NRE → 01-FE, 03-CCFE or 11-FEXE. (LB-004 N°14–17; R13; LB-007 Art.109)
- **SV-EINV-FR-016:** The system shall emit `resumen.observaciones` (N°168, max 3000 characters) for FE, CCFE, NRE, NCE, NDE, CRE, CLE, FEXE and FSEE when provided. (LB-003 N°168; DG45 §1.3)
- **SV-EINV-FR-017:** The system shall enforce the per-type CAT-015 *tributo* (tax/tribute code) restrictions: FE excludes codes 20 (IVA 13%) and C3 (export 0%); FEXE admits only C3 (null allowed with tipoItem 4); CLE admits only Sección-1 codes (20, C3, 59, 71, D1, C8, D5); NRE relating FE/CCFE admits 20, 59, 71, D1, C8, D5, D4; NRE relating FEXE admits only C3. (LB-004 N°96; DG45 §3.1; CAT-015 sidecar)
- **SV-EINV-FR-018:** The system shall emit non-taxable *cargos/abonos* (charges/credits not affecting the tax base) as body items with the fixed fill pattern: cantidad = 1, unidadMedida = 99, all sale-type fields $0.00, signed amount only in the charge/credit field, consolidated in the resumen total (NCE/NDE via item field N°98 `noGravado`). (LB-015 Anexo 4; LB-003 N°98; EVID-006; verify vs schemas per MOQ-08)

### 3.2 FE — Factura Electrónica (01)

- **SV-EINV-FR-019:** FE shall be the B2C consumer document with IVA-INCLUSIVE prices: `precioUnitario` and `ventaGravada` include IVA; `ventaGravada` = (precioUnitario × cantidad) − descuento; IVA shall not be added on top of totals; `ivaItem` is informative and computed as (ventasGravadas / 1.13) × 13%. (LB-008 + LB-012 via R1; LB-004 N°96; EVID-018)
- **SV-EINV-FR-020:** FE shall require receptor identification (nombre + tipoDocumento/numDocumento) when the monto total de la operación is ≥ 3 *salarios mínimos mensuales* (SMM, monthly minimum wages) per Art. 119-G VII; below that threshold the identification fields may be null. The 2022-era $200 figure is superseded and shall not be used. (LB-001; R3; DG45 §1.5 N°38/39/42; threshold amount → OQ-007)
- **SV-EINV-FR-021:** FE receptor identification shall use CAT-022 types: 13 DUI (natural persons not registered in IVA), 36 NIT, 02 carnet de residente, 37 otro; foreigners identified per Art. 119-G VII with passport (03) and non-domiciled foreign parties with their foreign registry number. (LB-001; LB-003 N°38/39; EVID-017 carried)
- **SV-EINV-FR-022:** FE resumen shall compute subTotalVentas = totalNoSuj + totalExenta + totalGravada; subTotal = sumatoria − global discounts; montoTotalOperacion = subTotal + non-informative tributo values; totalPagar = montoTotalOperacion ± retentions/noGravado, floored at $0.00. (LB-015 §V.1a; LB-004 resumen; EVID-019)

### 3.3 CCFE — Comprobante de Crédito Fiscal Electrónico (03)

- **SV-EINV-FR-023:** CCFE shall require the full contributor receptor profile: NIT (9 or 14 digits, no dashes) held by a taxpayer with active NRC, nombre, actividad económica (CAT-019), address (departamento + municipio + complemento) and correo electrónico. (LB-004 N°38–45; LB-003 N°40; EVID-022)
- **SV-EINV-FR-024:** CCFE shall use NET prices with IVA added separately: `precioUnitario` excludes IVA; subTotalVentas = sum of operations without taxes; IVA débito (code 20) is computed and added on top (Ley IVA Art. 57 requires IVA separate from price in the CCF). (LB-008 via R1; EVID-023 arbitration note)
- **SV-EINV-FR-025:** The system shall block CCFE for operations that Ley IVA Arts. 65/65-A document with *factura* (non-deductible purchases): those operations shall be documented with FE instead. (LB-007 Art.107; EVID-060)

### 3.4 NRE — Nota de Remisión Electrónica (04)

- **SV-EINV-FR-026:** NRE shall be the goods-transfer document requiring receptor `bienTitular` from CAT-025 (*título a que se remiten los bienes*, title under which goods are transferred) and full receptor identification. (LB-007 Art.109; LB-004 receptor rules; EVID-028)
- **SV-EINV-FR-027:** NRE shall relate only active, sealed documents of types 01-FE, 03-CCFE or 11-FEXE (the sale documents it accompanies or precedes), with the related CCF/F issued within 3 days after the period of NR emission referencing the NR. (LB-004 N°14–17; LB-007 Art.109)

### 3.5 NCE — Nota de Crédito Electrónica (05)

- **SV-EINV-FR-028:** NCE shall adjust only prior 03-CCF or 07-CR documents, with the documentos-relacionados section mandatory (1–50, same type, active and sealed), within the Ley IVA Art. 62–63 windows (at most 3 months); after an invalidation window expires, CCF and CR shall remain adjustable via NCE/NDE. (LB-004 N°14–17; LB-009; LB-002; R13)
- **SV-EINV-FR-029:** NCE shall identify its receptor via tipoDocumento/numDocumento (CAT-022); `receptor.nit` (N°40) shall not be emitted for NCE (field eliminated in v2.0). (LB-003 §1.4)
- **SV-EINV-FR-030:** NCE shall emit the v2.0 item-level adjustment fields N°98 `noGravado`, N°99 `ivaPerci`, N°100 `iva13`, N°101 `ivaRete` and the summary totals N°143 totalIvaPercibido, N°144 codigoRetencionMH, N°145 totalIvaRetenido, N°146 totalIva13, N°151 totalNoGravado, N°153 totalPagar; and shall NOT emit the eliminated fields N°130–132 (global discounts), N°134 (descuento percentage), N°139 (subTotal), N°141–142 (ivaPercibido/ivaRetenido). (LB-003 §1.3–1.4; DG45 §1.3)
- **SV-EINV-FR-031:** NCE/NDE adjusting a 07-CRE shall set ventaNoSuj/ventaExenta/ventaGravada to $0.00 per item with cantidad = 1, and the sum of adjustments shall not exceed "Total de operaciones − descuento global" of the related CCFE (code 03) nor "Total monto sujeto a retención" of the related CRE (code 07). (LB-004 cuerpo rules; DG45 §3.1)
- **SV-EINV-FR-032:** NCE/NDE resumen shall compute totalPagar = montoTotalOperacion + totalIvaPercibido − totalIvaRetenido ± cargos/abonos, floored at $0.00 when abonos exceed the monto. (LB-004 resumen rules)

### 3.6 NDE — Nota de Débito Electrónica (06)

- **SV-EINV-FR-033:** NDE shall adjust only prior 03-CCF, 05-NCE, 06-NDE or 07-CR documents, with the same mandatory-related-documents, sealing and 3-month window rules as NCE, and shall inherit FR-029–FR-032 structure rules. (LB-004 N°14–17; LB-007 Art.110; R13)

### 3.7 CRE — Comprobante de Retención Electrónico (07)

- **SV-EINV-FR-034:** CRE shall be the IVA-retention document with emisor = *agente de retención* (retention agent) and receptor = *sujeto de retención* (withheld subject); emisor NRC may be null when the retention agent has no active NRC; NCE/NDE adjusting a CR shall validate against non-IVA-registered retention agents. (LB-007 Art.112; LB-004 emisor rules; EVID-027)
- **SV-EINV-FR-035:** CRE items shall each carry the related-document quad (N°78–81 tipoDocRelacionado/tipoGeneracion/numeroDocRelacionado/fechaGeneracion, required) with at most 500 items and no mixing of document types within one CRE; `codigoRetencionMH` shall use CAT-006 (22 = Retención IVA 1%, C4 = 13%, C9 = otras); `ivaRetenido` = montoSujetoRet × legal rate; `montoSujetoRet` shall be computed as (TotalGravadas − descuento global) when relating a CCFE and as (TotalGravadas − descuento global) / 1.13 when relating an FE. (LB-004 N°78–81, N°103–105, N°74; EVID-027; DG45 §3.1)
- **SV-EINV-FR-036:** CRE shall emit `resumen.iva13` (N°157) as informative IVA 13% calculated on the monto sujeto a retención, without effect on total IVA retenido (CT Art. 162 inc. 7°). (LB-003 N°157; DG45 §1.3)

### 3.8 CLE — Comprobante de Liquidación Electrónico (08)

- **SV-EINV-FR-037:** CLE shall be the period liquidation of third-party-account sales with emisor = *comisionista* (commission agent) and receptor = *mandante* (principal); each cuerpo item shall represent exactly one liquidated document (F, CCF, FEX, NC or ND may mix within one CLE); values shall be net of IVA; documents invalidated/annulled within the period shall be entered as negative values (a document active-then-invalidated within the same period ⇒ two items with opposite signs); each sealed document may appear in a CLE only once (twice only for the positive+negative same-period case). (LB-007 Art.108; LB-004 cuerpo rules; EVID-031)
- **SV-EINV-FR-038:** CLE shall copy receptor `domicilioFiscal` (N°53) from the FE v2 / CCFE-NCE-NDE v4 / FEXE v3 document being liquidated; `receptor.nit` (N°40) shall not be emitted for CLE. (LB-004 N°53; LB-003 §1.4)
- **SV-EINV-FR-039:** CLE shall report FEX values separately in `exportaciones` (N°93), as negative values when the informed FEX has been invalidated or annulled. (LB-003 N°93; DG45 §1.5)

### 3.9 DCLE — Documento Contable de Liquidación Electrónico (09)

- **SV-EINV-FR-040:** DCLE shall be the card-acquirer settlement document (2% IVA perception, CT Art. 162-A) with emisor = *agente perceptor* (perceiving agent, card issuer) and receptor = *afiliado* (merchant affiliate); its cuerpo shall be a single settlement record (not item-per-document) containing periodoLiquidacionFechaInicio/Fin (fin ≥ inicio), codigoLiquidacion, cantidadDocumentos, valorOperaciones, valoresSinPercepcion + descripcionSinPercepcion, subTotal = valorOperaciones − no sujetos a percepción, montoSujetoPercepcion, ivaPercibido = 2% of the net subject amount, comision + porcentajeComision + ivaComision = comisión × 13%, and valorLiquidoPagar = valorOperaciones − comisión − ivaPercibido − ivaComision. (LB-011 Art.112/162-A; LB-004 N°106–122; EVID-032)
- **SV-EINV-FR-041:** DCLE shall be the only type emitting Sección 10 EXTENSIÓN (N°169–171, responsible-delegate identification required per Art. 119-G); the emitter/receptor MH establishment codes (codEstablecimiento/codPuntoVenta MH) and emisor tipoEstablecimiento shall not be emitted for DCLE. (LB-003 N°169–171 + §1.4; LB-001)

### 3.10 FEXE — Factura Electrónica de Exportación (11)

- **SV-EINV-FR-042:** FEXE (version 3) shall be the export invoice with emisor = *exportador* and a foreign receptor (no NIT/NRC): nombre, tipoDocumento/numDocumento (CAT-022, leading zeros preserved), descActividad (free text), codPais + nombrePais (CAT-020 destination), complemento (foreign address) and tipoPersona (CAT-029). (LB-003; EVID-033; DG45 §1.2)
- **SV-EINV-FR-043:** FEXE *tipo de exportación* shall use CAT-011 codes 1 (goods) or 2 (services) only — codes 3 and 4 are forbidden; `recintoFiscal` (CAT-027), `regimen` (CAT-028) and `tipoRegimen` (CAT-033, new) shall be required when exportación = 1 and null when = 2. (LB-004 emisor N°28–31/36; DG45 §1.3)
- **SV-EINV-FR-044:** FEXE shall emit Sección 7 COMPRA POR CUENTA DE TERCEROS (N°72 `compraTercero.numDocumento`, N°73 `compraTercero.nombre`); when N°72 is filled, the receptor must be listed by the AT as *operador logístico* (logistics operator). (LB-003 §1.3; LB-004 N°72)
- **SV-EINV-FR-045:** FEXE totals shall compute the gravadas (afectas) base as Total gravadas − descuento global + seguro + flete; tributos shall be C3 (IVA exportaciones 0%) only, mandatory even at $0.00; INCOTERMS (CAT-031) shall be required when exportación = 1; `resumen.totalNoOnerosa` (N°152) shall report non-onerous transfers of goods (art. 77 LST). (LB-004 N°93–96, N°152; DG45 §1.3, §1.5)
- **SV-EINV-FR-046:** FOVIAL (D1) and COTRANS (C8) tributes in FEXE shall require prior AT authorization (*solicitud/autorización*). (LB-004 N°96; DG45 §3.1)
- **SV-EINV-FR-047:** FEXE may relate documents in Sección 2 (new in v2.0), admitting 04-NR with the same-period-or-3-days rule. (LB-003 §1.3; LB-004 N°14–17)

### 3.11 FSEE — Factura Electrónica de Sujeto Excluido (14)

- **SV-EINV-FR-048:** FSEE shall be the document for operations involving *sujetos excluidos* (excluded taxpayers, Ley IVA Arts. 28–32): amounts shall be stated WITHOUT any IVA surcharge (Art. 32); the receptor (sujeto excluido) shall be identified via tipoDocumento/numDocumento (CAT-022; DUI for natural persons); emisor NRC is optional. (LB-010; LB-003; EVID-034)
- **SV-EINV-FR-049:** FSEE items shall use tipoItem codes 1–3 only (no tax-as-item code 4) with a single compras/sales amount field (no gravadas/exentas/noSujetas split); `resumen.ivaRetenido` (N°142, eliminated for FSEE) shall not be emitted; `reteRenta` (N°147, FSEE-only) shall be emitted and totalPagar = subTotal − reteRenta. (LB-003 §1.3–1.4; LB-004 resumen; DG45 §1.3)

### 3.12 CDE — Comprobante de Donación Electrónico (15)

- **SV-EINV-FR-050:** CDE shall be the donation receipt issued by the *donatario* (donation recipient, emitter), who shall attach the resolución de calificación como sujeto excluido (CAT-021 doc code 1, mandatory); the receptor is the *donante* (donor) with codDomiciliado (CAT-032: 1 Domiciliado / 2 No Domiciliado) and codPais (CAT-020, nationality/domicile); the receptor address shall not be required when not domiciled. (LB-001; LB-004 N°58–68; EVID-035)
- **SV-EINV-FR-051:** CDE items shall state tipoDonacion (CAT-026: 1 efectivo, 2 bien, 3 servicio) with valor donado = (valorUnitario × cantidad) − depreciación; cantidad = 1 for cash donations; depreciation allowed for used goods. (LB-004 cuerpo; EVID-012/035)
- **SV-EINV-FR-052:** CDE payment data shall be emitted only for tipoDonación = 1 (cash): forma de pago (CAT-017) null for bien/servicio donations, with montoPago = totalDonación. (LB-004 resumen; DG45 §3.1)

## 4. Data Model

The MH JSON structure itself lives SaaS-side only (architecture decision D2:
private minimal protocol between Odoo and SaaS; the SaaS compiles it into the
MH schema). This section documents the semantic fields both sides and the
SaaS team must agree on. Machine-readable catalog sidecars live in
[../catalogs/](../catalogs/) (33 CSVs, v1.1 2026-07).

**DTE type registry** (seed data; per-type caps and modes):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_latam.document.type | code | char(2) | 01, 03, 04, 05, 06, 07, 08, 09, 11, 14, 15 | CAT-002 `CAT-002_tipo-documento-evento.csv`; FR-001 |
| l10n_latam.document.type | json_version | integer | 2 (01,07,08,09,14,15) · 3 (11) · 4 (03,04,05,06) | FR-002; DG45 §1.0 |
| l10n_latam.document.type | max_body_items | integer | 2000 general · 500 (07 CRE, 08 CLE) · 1 (09 DCLE single record) | FR-012, FR-035, FR-040 |
| l10n_latam.document.type | contingency_allowed | boolean | true: 01,03,04,05,06,07,11,14 · false: 08,09,15 | FR-013; DG45 §3.3 |
| l10n_latam.document.type | related_doc_codes | char list | 05→03,07 · 06→03,05,06,07 · 01/03→04,08,09 · 11→04 · 04→01,03,11 | FR-015 |

**Key shared structural fields** (v2.0 additions marked NEW):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (DTE) | codigoGeneracion | char(36) | UUID v4 uppercase | FR-003 |
| account.move (DTE) | numeroControl | char(31) | DTE-TT-EEEEEEEE-CCCCCCCCCCCCCCC | FR-004 |
| account.move (DTE) | fecEmi / horEmi | date / time | windows per FR-008 | FR-008 |
| account.move (DTE) | fusiones (NEW) | char(14) null | NIT 9/14 digits, AT merged list | FR-009 |
| res.partner | distrito (NEW) | many2one CAT-008 | 263 district codes | FR-010 |
| res.partner / sale | domicilioFiscal (NEW) | select CAT-032 | 1 Domiciliado / 2 No Domiciliado | FR-011 |
| account.move.line | noGravado / ivaPerci / iva13 / ivaRete (NEW, NCE/NDE) | monetary | — | FR-030 |
| account.move (DTE) | tributoSujetoIVA (NEW, N°84) | char CAT-015 §2 | codes A8, 57, 90, A6 with tipoItem 4 mechanics | FR-018 note; OQ-002 (key spelling) |
| account.move (DTE) | resumen.observaciones (NEW, N°168) | text(3000) | 9 types | FR-016 |
| account.move (FEXE) | compraTercero numDoc/nombre (N°72/73) | char / char(250) | receptor must be AT-listed operador logístico | FR-044 |
| account.move (CRE) | codigoRetencionMH | select CAT-006 | 22 (1%) · C4 (13%) · C9 (otras) | FR-035 |
| account.move (CDE) | tipoDonacion | select CAT-026 | 1 efectivo · 2 bien · 3 servicio | FR-051 |

**Field-count deltas per type** (approximate, OCR-tallied [?]): FE ~102,
CCFE ~100, NRE ~83, NCE ~87, NDE ~88, CRE ~58, CLE ~70, DCLE 64, FEXE ~96,
FSEE ~66, CDE ~61 (incl. sello N°175) — see DG45 §1.2; authoritative
enumeration = 45_ Anexo II + 52_ schemas.

## 5. Odoo Mapping

Layer semantics: `saas` = generation/transformation/validation logic living in
the Elixir core (thin client never builds MH JSON); `odoo` = posting, display
or data-capture surface in the LGPL client; `shared` = private-protocol
contract items both sides must honor. Per D2, validation runs at both ends —
client pre-checks are noted but authoritative validation is SaaS-side.
Model names are stable across Odoo 17/18/19/20; no version-specific behavior
is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | saas | l10n_latam.document.type | code, name | Type registry seeded per CAT-002; per-company enablement gated by AT authorization (A11 file). l10n_latam pattern available 17–20 |
| FR-002 | saas | l10n_latam.document.type | json_version | Version stamped at generation; client never handles it |
| FR-003 | saas | — | codigoGeneracion | UUID v4 generated server-side; mirrored to client archive (D3 Tier A) |
| FR-004 | saas | — | numeroControl | Single server-side sequencer per D2 (no fleet drift); year-reset + uniqueness in one store |
| FR-005 | saas | account.move | l10n_latam_document_type_id | Schema compilation = core IP (D2); client sends private-protocol payload only |
| FR-006 | saas | account.move.line | price_unit, tax_ids | Authoritative rounding/holgura SaaS-side; odoo pre-validation mirrors the rule for early UX rejection |
| FR-007 | saas | account.move | invoice_date | Constant; surfaced for completeness |
| FR-008 | saas | account.move | invoice_date, time fields | Windows validated at generation; rejection reason surfaced to odoo |
| FR-009 | shared | res.company | fusion_nit | Emitter master data captured in odoo, carried as contract field, validated against AT list SaaS-side |
| FR-010 | shared | res.partner | distrito_id (new), state_id/city | District↔municipio correspondence needed for both client selection UI and server validation |
| FR-011 | shared | res.partner, sale.order | domicilio_fiscal | CAT-032 code a contract field; code 1 implies NIT-registered third party check |
| FR-012 | shared | account.move.line | — | Cap enforced authoritatively SaaS-side; odoo pre-check drives line-splitting UX (>2000 lines ⇒ second DTE) |
| FR-013 | saas | account.move | l10n_latam_document_type_id | Generation-mode gate server-side; odoo UI blocks contingency flow for excluded types |
| FR-014 | saas | account.move | ref_document_ids (new) | Related-doc registry contract: codigoGeneracion/numeroControl refs validated SaaS-side |
| FR-015 | saas | account.move | ref_document_ids | Timing windows (3 days / 3 months / same period) authoritative SaaS-side |
| FR-016 | shared | account.move | narration → observaciones | Free text captured in odoo, passed through protocol (max 3000) |
| FR-017 | saas | account.tax | l10n_sv_tributo_code (new) | Per-type tributo matrix = core IP; odoo tax templates carry CAT-015 codes |
| FR-018 | saas | account.move.line | charge/credit line tagging | Fill pattern applied at transformation; odoo tags lines (product-based) |
| FR-019 | shared | account.tax, product.pricelist | price_include=True for FE taxes | R1 contract: odoo computes IVA-inclusive (tax-included mode); SaaS formula must match. Both sides must agree — contract item |
| FR-020 | odoo | res.partner, account.move | name, vat, l10n_latam_identification_type_id | Threshold check surfaced at invoicing UX (partner completion); SaaS validates authoritatively. Amount configurable (OQ-007); old $200 config must NOT be seeded |
| FR-021 | odoo | res.partner | l10n_latam_identification_type_id | CAT-022 mapping on partner (native l10n_latam field, 17–20) |
| FR-022 | saas | account.move | amount fields | Resumen formulas at transformation |
| FR-023 | odoo | res.partner | vat, nrc (new), activity_code, street/email | Required-field enforcement at posting surface; SaaS re-validates |
| FR-024 | shared | account.tax | price_include=False for CCFE taxes | Mirror of FR-019: net + IVA added. Odoo tax config and SaaS formula must agree |
| FR-025 | odoo | account.fiscal.position / move type selection | document type defaults | Doc-type selection logic client-side (deductibility rules from A10 taxation file) |
| FR-026 | shared | account.move | bien_titular (CAT-025) | Contract field captured on the move |
| FR-027 | saas | account.move | ref_document_ids | Sealed/active check server-side |
| FR-028 | saas | account.move | ref_document_ids, reversal reason | Credit-note workflow in odoo (native reversals), window validation SaaS-side |
| FR-029 | saas | — | — | Structure-only rule |
| FR-030 | saas | account.move.line, account.move | noGravado/ivaPerci/iva13/ivaRete, totals | Adjustment fields part of protocol payload (shared semantics) but computed SaaS-side |
| FR-031 | saas | account.move | ref_document_ids | Exceedance checks vs original totals |
| FR-032 | saas | account.move | amount_total | totalPagar formula |
| FR-033 | saas | account.move | ref_document_ids | Inherits 029–032 |
| FR-034 | odoo | res.partner | retention_agent flag (new) | Agent/subject roles configured on partners; doc generation SaaS-side |
| FR-035 | saas | account.move.line | retention fields | Per-item quad + CAT-006 + formulas; odoo feeds retention staging lines |
| FR-036 | saas | account.move | informative iva13 | Informative only |
| FR-037 | saas | account.move | period liquidation wizard (odoo UX) | Liquidation run selected in odoo (source docs picker); aggregation SaaS-side |
| FR-038 | saas | account.move | ref_document_ids | DomicilioFiscal copied at transformation |
| FR-039 | saas | account.move | exportaciones field | FEX-negative rule |
| FR-040 | saas | account.move | settlement staging (odoo import) | Card-settlement data staged in odoo; single-record cuerpo compiled SaaS-side |
| FR-041 | saas | — | — | Extensión DCLE-only |
| FR-042 | saas | res.partner | foreign partner fields | Foreign receptor data captured in odoo partner form |
| FR-043 | shared | account.move | export type, recinto/regimen/tipoRegimen | Export parameters contract fields on the move |
| FR-044 | saas | account.move | compraTercero fields | Operador-logístico check against AT list |
| FR-045 | saas | account.move.line | insurance/freight lines | seguro/flete feed from odoo invoice lines; C3 + INCOTERMS rules SaaS-side |
| FR-046 | saas | — | — | Authorization flag from emitter profile |
| FR-047 | saas | account.move | ref_document_ids | New-for-FEXE section |
| FR-048 | odoo | res.partner | sujeto_excluido category | Partner fiscal category drives FSEE selection (A10 taxation file) |
| FR-049 | saas | account.move.line | single amount field | Structure rules |
| FR-050 | odoo | res.company | donatario_resolution (new) | Resolution stored on company; emitted with every CDE |
| FR-051 | saas | account.move.line | donation valuation | Depreciation input from odoo line |
| FR-052 | saas | account.move | payment fields | Payment block rules |

## 6. Acceptance Criteria

- **AC-001:** Given any of the 11 DTE types is generated, when the JSON is compiled, then `identificacion.version` equals the FR-002 matrix value for that type (verified for all 11 against 52_ schemas).
- **AC-002:** Given a DTE generated in a new fiscal year, when numeroControl is assigned, then the consecutive restarts from the beginning and no numeroControl repeats within the same calendar year (FR-004).
- **AC-003:** Given an FE whose montoTotalOperacion ≥ 3 SMM, when receptor nombre or numDocumento is missing, then generation is blocked with a field-level error; given an FE below the threshold with receptor fields null, then generation succeeds (FR-020).
- **AC-004:** Given an FE line with cantidad 10 and precioUnitario $11.30 (IVA-inclusive), when the DTE is compiled, then ventaGravada = $113.00 and ivaItem = ($113.00/1.13) × 13% = $13.00, and totalPagar does not add IVA on top (FR-019).
- **AC-005:** Given a CCFE line with cantidad 10 and precioUnitario $100.00 (net), when the DTE is compiled, then ventaGravada = $1,000.00, IVA 20 = $130.00 added on top, montoTotalOperacion = $1,130.00 before other tributos (FR-024).
- **AC-006:** Given an invoice with 2,001 lines of a general type, when the client prepares generation, then it splits into two DTEs; given a CRE staged with 501 items, then the SaaS rejects it (FR-012, FR-035).
- **AC-007:** Given a CLE (or DCLE or CDE) submitted with tipoModelo = 2 / tipoTransmision = 2, then the SaaS rejects it; given an NCE submitted the same way, then it is accepted as contingency-eligible (FR-013).
- **AC-008:** Given an NCE generated without at least one documentoRelacionado of type 03 or 07, then pre-validation blocks generation (FR-028).
- **AC-009:** Given an NCE adjusting a CRE whose adjustments exceed the CRE's total monto sujeto a retención, then the SaaS rejects it (FR-031).
- **AC-010:** Given a CRE item relating a CCFE with TotalGravadas $1,000.00 and descuento global $100.00, then montoSujetoRet = $900.00; given the same values relating an FE, then montoSujetoRet = $900.00/1.13 = $796.46 (FR-035).
- **AC-011:** Given a DCLE with valorOperaciones $10,000.00, no sujetos a percepción $0.00, comisión $200.00, then ivaPercibido (2%) = $200.00, ivaComision = $26.00 and valorLiquidoPagar = $10,000.00 − $200.00 − $200.00 − $26.00 = $9,574.00 (FR-040).
- **AC-012:** Given an FEXE with compraTercero.numDocumento filled and a receptor not on the AT operador-logístico list, then the SaaS rejects it (FR-044).
- **AC-013:** Given an FSEE, then no IVA is added or stated and resumen contains no ivaRetenido; totalPagar = subTotal − reteRenta (FR-048, FR-049).
- **AC-014:** Given a CDE without the CAT-021 code-1 resolución document, then generation is blocked (FR-050).
- **AC-015:** Given a fusiones NIT that is not in the AT merged-contributors list, then the SaaS rejects the DTE; given fusiones = null with no merger, then it passes (FR-009).
- **AC-016:** Given a receptor distrito code that does not correspond to the declared departamento/municipio, then the SaaS rejects the DTE (FR-010).
- **AC-017:** Given a computed resumen field differing from the sum of rounded items by ≤ +$0.01, then the DTE is accepted; by more, then rejected (FR-006).
- **AC-018:** Given an NCE compiled with any of the eliminated fields N°130–132/134/139/141–142 present, then the structure is rejected as invalid v2.0 (FR-030).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | v2.0 eliminated Sección 10 EXTENSIÓN for every type except DCLE, but CT Art. 114 requires deliverer/receiver names + signatures on CCF ≥ $11,428.57. How is that legal requirement satisfied now (Representación Gráfica surface? reform? dropped)? | no | Takumi synthesis wave 1 | open |
| OQ-002 | MOQ-08: exact JSON key spellings unresolvable from OCR — DTE N°84 *tributoSujetoIVA*, DTE N°7 `tipoOperacion` vs `tipoTransmision`, CRE N°103 `montoSujetoGrav`. Verify against 52_ schemas before implementation. | no | Takumi (schema pass) | open |
| OQ-003 | MOQ-08 (part): NCE/NDE allowed CAT-015 codes in v2.0 — 2022 manual listed anomalous codes T1/D8/C5; confirm allowed set from 52_ schemas. | no | Takumi (schema pass) | open |
| OQ-004 | MOQ-09: global-discount sign in resumen.subTotal — 2022 FE formula shows subtraction, CCFE prose shows addition; never arbitrated. Confirm from 52_ schemas + 45_ worked examples. | no | Takumi (schema pass) | open |
| OQ-005 | MOQ-12: DCLE cuerpo item cap — 18_ v1.2 set 500 for CRE/DCL/CL, but 45_ digest restates only "CRE y CLE 500"; DCLE cuerpo is a single record in any case. Confirm cap inapplicable. | no | Takumi (schema pass) | open |
| OQ-006 | MOQ-11: CDE async seal "24–72h after transmission" (2022 manual) — still true under v2.0? Affects CDE delivery flow. | no | SaaS team | open |
| OQ-007 | FE receptor threshold "≥ 3 salarios mínimos mensuales" (119-G VII): which SMM figure applies (per-activity amounts change annually; CT Art. 228 selection rule?) — the threshold must ship as a configurable amount with a documented default. | no | Takumi + SaaS team | open |
| OQ-008 | Type-code discrepancy: DG45 §3.3 parentheticals list contingency-excluded types as "CLE (15), DCLE (16), CDE (17)" but CAT-002 v1.1 (from official 51_ XLSX) codes are CLE=08, DCLE=09, CDE=15 (matching 2022 structures). Requirements use CAT-002. Verify tipoDte enums in 52_ schemas. | no | Takumi (schema pass) | open |
