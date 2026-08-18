# Evidence — 41_manual_eventos_invalidacion.md

Source: `sv/sources/41_manual_eventos_invalidacion.md` (v1.1, 05/2022)
Read: 2026-08-16 (W1). Full document (432 md lines).
Citation form: section + markdown line numbers.

---

## EVID-036 Events are not DTEs; testing prerequisites

- **Loc:** §1 (md 69-75). Verbatim: "si bien... estas deben ser transmitidas en formato Json, estos no se consideran un Documento Tributario Electrónico (DTE)"; "deberá realizar el proceso de pruebas para cada uno de los eventos... Las pruebas de dichos eventos serán consideradas al momento de realizar las verificaciones para el otorgamiento de la resolución".
- **Gloss:** events (invalidation/contingency) are signed JSON messages, legally distinct from DTEs. Each event type must pass its own transmission tests during onboarding, independent of how many DTE types are requested.
- **Topics:** e-invoicing

## EVID-037 Invalidation event — semantics and state effect

- **Loc:** §2 (md 81-98). Justified reasons (md 85-92): client-ID error, product/service error, date error, price error (F and FEX only), goods return, total rescission. Verbatim: "este evento no elimina ni borra del sistema el DTE, solo se coloca el estado 'INVALIDADO'" — public consultation shows the INVALIDADO status; the document never disappears from DGII's DB. Event itself is structure-validated; rejection returns errors for correction (md 121-123). Seal on the invalidation event is what flips the DTE to INVALIDADO (md 123).
- **Topics:** e-invoicing

## EVID-038 Invalidation deadlines — RESOLVED OQ from pilot

- **Loc:** §2.3 (md 129-136). Table: CCFE/NCE/NDE/NRE/CRE/CLE/DCLE/FSEE/CDE → **1 day** after seal (until 23:59:59 of next day); FE/FEXE → **3 months** (same-date boundary 23:59:59). Verbatim: "No se otorgará sello de recepción al evento de invalidación transmitido fuera de los plazos establecidos, por lo que the DTE aún conservará su validez original" — late events are simply refused; the DTE stays valid.
- **Candidate CR:** deadline enforcement per DTE type; calendar-day semantics (not 24h rolling).
- **Topics:** e-invoicing
- **Resolves:** pilot OQ-4 (deadlines confirmed from source; hint layer's table was correct).

## EVID-039 Invalidation replacement rules (types 1/3 vs 2)

- **Loc:** §2.1/2.4 + Anexo 2 (md 111-149, 403-411). Tipo 1 (error in DTE info) or 3 (other): replacement document must ALREADY be transmitted+sealed before the event (exceptions: NC and CL always use Null). Tipo 2 (rescind): Null replacement, single reference. Worked examples (md 143-149). Also §2.5 field 22 (documento.codigoGeneracionR): 36-char replacement code, "Requerido por Tipo de Operación" (md 189).
- **Topics:** e-invoicing

## EVID-040 Invalidation event structure (v2, 36 fields)

- **Loc:** §2.5 (md 151-213). Sections: Identificación (version=`2`, ambiente, codigoGeneracion UUID v4 for the EVENT itself, fecAnula/horAnula); Emisor (nit, nombre, tipoEstablecimiento CAT-009, **nomEstablecimiento required**, codEstableMH Null in transition, telefono, correo); Documento a invalidar (tipoDte, codigoGeneracion of target, **selloRecibido 40 chars of target**, numeroControl, fecEmi, montoIva — only for CCF/F/FEX else Null, codigoGeneracionR, receptor tipoDoc/numDoc/nombre/telefono/correo); Motivo (tipoAnulacion CAT-024, motivoAnulacion ≤200 describing the erroneous fields, **nombreResponsable + tipDocResponsable + numDocResponsable (who invalidates)**, **nombreSolicita + tipDocSolicita + numDocSolicita (who requests — receiver's data, or emitter's again if self-requested)**, md 200-207).
- **Candidate CR:** invalidation payload model incl. responsible/requester parties (CAT-022 IDs) and target-doc quad (codigoGeneracion + sello + numeroControl + fecha).
- **Topics:** e-invoicing

## EVID-041 Contingency model — deferred reception

- **Loc:** §3-3.1 (md 215-231). Force-majeure definition (md 280-285): emitter-connection failure, ISP failure, power failure, MH unavailability — each "siempre que no impida generar el documento electrónico y entregar la representación gráfica". **Trigger detection (md 287): no response after 5 seconds** or failed response processing → apply the retry policy from the "Guía de Integración Tecnológica" (separate doc, not in sources) → then operate in contingency. Deferred model (md 225-227): deliver to receiver WITHOUT seal, marked "modelo diferido/transmitido en contingencia"; after restoration: send event, then batch, then each doc gets its seal.
- **Candidate CR:** contingency mode: 5s timeout + retry policy → local generation with deferred flags → post-restoration two-step transmission.
- **Topics:** e-invoicing
- **OQ:** the "Política de reintentos"/"Guía de Integración Tecnológica" is cited but NOT in sv/sources — retrieve from MH (numbering gap candidate; may correspond to missing 21/23/24/28).

## EVID-042 Contingency timing rules

- **Loc:** §3.4 Momento 2-3 (md 294-322). Event: within **24h** of contingency end, listing 1-5000 codigoGeneracions. Rejected event: fix and retransmit within **24h** of rejection. Batch: within **72h** of the EVENT's seal, containing only documents declared in the event (normal-transmission docs may NOT join the batch, md 311). Batch processed doc-by-doc; each gets its own seal. Non-compliance: justify in writing to DGII and request extension (md 320). AT may revoke authorization for non-compliance (md 322).
- **Candidate CR:** 24h/24h/72h clocks; batch restricted to declared docs.
- **Topics:** e-invoicing

## EVID-043 Contingency-eligible DTE types — CONTRADICTION

- **Loc:** §3.3 (md 252-259): FE, CCFE, NRE, NCE, NDE, FEXE (6 types). BUT §3.5 field 17 (md 358): "'01-F', '03-CCF', '05-NC', '06-ND', '04-NR', '11-FEX' y '14-FSE'" (7 types — includes FSE/FSEE). And per-doc structures: FSEE §V.10 says contingency allowed (md 1606-1607); CRE/CLE/DCLE/CDE forbid it (confirmed). CAT-023 Tipo de Documento en Contingencia is the authority (check sidecar). Likely 7 (§3.3 list misses FSE).
- **Topics:** e-invoicing
- **Doubt:** resolve via CAT-023 + 22_Manual_Tecnologico.

## EVID-044 Contingency event structure (25 fields)

- **Loc:** §3.5 (md 324-378). Sections: Identificación (version, ambiente, codigoGeneracion for the event, fechaTransmision + hTransmision); Emisor (nit, nomb, **nombrC = responsible person + tipDoc/numDoc**, tipoEstablecimiento "requerido para los POS", codEstablecimiento optional, codPuntoVenta "001" during transition, telefono ≤50, correo); Detalle (noItem 1-5000, tipoDoc per item, codigoGeneracion per item); Motivo (fInicio/fFin/hInicio/hFin — **start AND end datetimes of the contingency**, tipoContingencia CAT-005, motivoContingencia required iff type 5, ≤500 per field spec though prose says 1000 — minor conflict md 371).
- **Candidate CR:** contingency event payload + period tracking (inicio/fin) + doc list.
- **Topics:** e-invoicing

## EVID-045 Minimum transmission tests for events

- **Loc:** Anexo 1 (md 394-399): 5 successful invalidation events + 5 successful contingency events required during onboarding. Plus (crossref 40_ manual Anexo 1, EVID-015) DTE-type tests. Test environment (00) usable again when implementing AT-mandated updates (md 159).
- **Topics:** e-invoicing

## Open questions from this pass

1. **OQ:** Retry policy ("Guía de Integración Tecnológica") missing from sources — retrieve (EVID-041).
2. **OQ:** Contingency types 6 vs 7 (FSE in/out) — CAT-023 + 22_ manual arbitrate (EVID-043).
3. **OQ:** motivoContingencia max length 500 (field spec) vs 1000 (prose) — schema arbitrates (EVID-044).

## Topic tag summary

e-invoicing: EVID-036..045
