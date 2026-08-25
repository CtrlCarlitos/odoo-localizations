# SV Corpus Digest — implementation-scoping view

**Generated 2026-08-24 from the corpus at `75ecedd`** (1,747 FRs, post-W30,
COVERAGE 93/8/2/24 of 127 gate green). Mechanical census (grep-derived; FR
totals reconcile exactly with the per-topic indexes). This file is the scoping
input for the implementation design session / build-plan waves — NOT a
requirements artifact: nothing here overrides the corpus, GO_LIVE_READINESS,
or the topic indexes. Regenerate the greps if the corpus moves (W-wave or
watch-triggered amendments) before relying on the numbers.

## 1. Shape

| Topic | FRs | OQs (open/res) | Build flavor |
|---|---|---|---|
| e-invoicing (+protocols, catalogs) | 237 (EINV 179 + PROT 40 + CAT 18) | 51 (38/13) | DTE emission/transmission/contingency/onboarding — external API stack |
| taxation | 421 | 91 (81/10) | ISR + IVA engines, CT procedures, retentions, declarations |
| fiscal-reporting | 214 | 52 (50/2) | F-07/F-14 casilla engine + annexes + días-hábiles engine (FR-202..204) |
| payroll | 147 | 42 (39/3) | SS/ISSS/SMM/aguinaldo/indemnización clocks; consumes FREP+TAX heavily |
| commercial-legal | 248 | 35 | society/SAS/acciones/AML awareness — mostly partner/company config + invariants |
| special-regimes | 204 | 60 (48/12) | ZF/LSI/customs/DUCA/FOVIAL-COTRANS; D15 per-acuerdo ladders |
| chart-of-accounts | 276 | ~6 open | NIIF-PYMES policies, deferred-tax adoption — the accounting capstone |
| **Total** | **1,747** | ~337 total | |

**Model surface:** ~161 distinct `l10n_sv.*` entities. Heaviest:
`f07.casilla.value` (34 refs), ISR earnings event/register (35), F-07/F-14
annex rows (~45), IVA retention/reintegro/period-determination (~34), payroll
aguinaldo/SS/indemnización (~30).

**Data shipped as dated rows:** 33 catalog CSVs (1,586 rows — CAT-019
actividad-económica 776, CAT-008 distrito 264, CAT-020 país 250) + 5
parameter CSVs (F-14 codes 50, ISR brackets 24, withholding 21, SMM 19, SS
15). Catalog versions are **not monotonic** — dated catalog rows per
CAT-FR-007..010.

## 2. Dependency graph (by-id consumes → build order)

```
e-invoicing  → (leaf: 1 FREP ref)              [wave 1 + catalogs]
frep         → TAX 32, EINV 11, PAY 3          [wave 2, with taxation]
taxation     → FREP 37, SPE 16, EINV 14, PAY 3 [wave 2 core]
payroll      → FREP 26, TAX 22                 [wave 3]
spe          → TAX 14, EINV 7, FREP 5          [wave 4]
coa          → TAX 17, CML 9, PAY 5, EINV 4    [wave 5 — top consumer, closes the corpus]
cml          → mostly leaf; payroll interface = FR-247/248 (SAS accionista)
```

The dense triangle is **taxation ↔ fiscal-reporting ↔ payroll** (they consume
each other's engines by id — the días-hábiles engine, SMM feed, retention
registers). Nothing consumes COA except via pointer → COA last. This matches
the wave order the corpus itself was built in.

## 3. Risk areas (ranked)

1. **DTE transmission stack** (biggest single surface): JWS RS512 signing,
   anulación/contingencia/eventos, 26 invalidación deadline classes,
   onboarding state machine + per-DTE minimum tests (counts = config, no
   defaults). Four WATCH limbs: F-11 v19/v20 prints, Retorno/OpEsp endpoints
   (MOQ-05, schema-absent — gates FR-062/090), cert renewal procedure
   (OQ-006), AML reglamento (2026-10-17).
2. **Casilla engine** (F-07/F-14): 34-ref `casilla.value` model, annex
   upload/validation flows, HN-kin dead-print guard for pago-mínimo
   casillas. Casilla honesty rules are verbatim-anchored.
3. **D15 as-of machinery** (payroll corrections, ZF/LSI ladders,
   aguinaldo-cap vintages): per-acuerdo dated rows, original-period
   corrections, no retro-transmission — the highest-design-discipline
   component in the corpus.
4. **IVA credit/pro-rata/reintegro + ISR engines**: 421 taxation FRs incl.
   verbatim retention matrices and the CT procedures state model.
5. **Config-gaps (owner decisions, no defaults by canon)**: ~102 hits
   corpus-wide (spe 34, cml 30, taxation 24, coa 14) — Economía commission
   rates, SMM-mayor-cuantía sector, AT program groups/dates, test-count
   rows, RAEX reglamento.

## 4. Invariants that will bite if missed (§5 canon condensed)

pago mínimo **void** (sent. 18-2012); CT-311 maternity gate void;
24h-over-5-días law-wins pair (OQ-tracked); D13/D14
one-journal-many-doctypes + establecimientos/caja first-class; verbatim
rounding + posting tiers; config-gaps ship **no defaults**; CC↔CAT
auto-translation banned; never-implement list is short and load-bearing.

## 5. Amendment surface (what can still change the corpus)

F-11 v19/v20 + F-14 v17 manual (MH landing watch) · DTE stack re-version
(factura.gob.sv, pinned recipe in sv/HANDOVER §6) · AML reglamento
≤2026-10-17 (uif unblocked post-W30 sweep) · aguinaldo-cap decree
Nov/Dec-2026 (gated on the D.O. feed stall clearing) · SOQ-46 negative
watch (cvpcpa + D.O.). All watch-class: none blocks starting
implementation. WATCH/CONFIG-GAP pointers with cadences live in
`GO_LIVE_READINESS.md` §5.2/§5.3 — that file stays the gate authority.

## 6. Census reproduction (worktree, corpus at rest)

```
rg -oN "SV-[A-Z]+-FR-[0-9]{3}" sv/requirements --no-filename | sort -u | wc -l
# per-topic: same, scoped per dir (reconciles with 00_index totals)
rg -oN "l10n_sv\.[a-zA-Z_.0-9]+" sv/requirements --no-filename \
  | sed 's/[0-9]\+$//' | sort -u | wc -l        # entity census (161)
# cross-topic consumption: per-dir unique FR ids minus own prefix,
#   counted by foreign prefix (see §2 numbers)
wc -l sv/requirements/*/*.csv                    # data volumes
```
