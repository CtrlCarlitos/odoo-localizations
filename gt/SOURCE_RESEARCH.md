# GT — Source Research Log (Stage 0 precursor)

Deep research for the Guatemala source corpus. This log records every candidate
document found, the triage verdict, and the site coverage map — the research
record that feeds `gt/EXTRACTION_PLAN.md` (Stage 0).

**Session**: started 2026-08-18, branch `gt-research`, worktree `.worktrees/gt-research`.

## Policy (decided with product owner 2026-08-18)

- **Topic scope**: full SV mirror — e-invoicing (FEL), taxation, payroll,
  fiscal-reporting, chart-of-accounts, commercial-legal, special-regimes,
  catalogs.
- **Source policy**: official-only, strict. Official GT government sites only;
  mirrors (law firms, news, universities) are never registered — recorded as
  acquisition leads when the official copy cannot be found.
  **Exception — partner tier**: FEL operates through SAT-authorized third-party
  installers; provider technical documentation (TotalDoc = default provider,
  https://www.totaldoc.com/) registers under a `partner-technical` provenance
  tier, LB-citable only for provider-interface requirements, clearly marked
  non-government. Public docs only (no partner-portal access yet).
- **Acquisition**: acquire-as-we-go into `gt/sources/` (SV-style `NN_Name.ext`
  numbering from `01_`) + registry rows in `gt/sources/README.md`. Ambiguous
  items get FLAGGED for owner decision, never guessed.
- **Triage rubric per candidate**: relevant → current (supersession chain) →
  useful (law / manual / form / catalog / schema) → official? Verdicts:
  ACQUIRE / FLAG / REJECT(+reason).

## Official domains (coverage map)

| Domain | Covers | Sweep status |
|--------|--------|--------------|
| sat.gob.gt (+ FEL subsites/portals) | Tax authority: FEL normative + technical, forms, manuals, calendars, catalogs | pending |
| congreso.gob.gt | Law library: codes + laws + reforms | pending |
| diario.gob.gt | Diario de Centro América (official gazette) | pending |
| igssgt.org | Social security (IGSS) | pending |
| mintrabajo.gob.gt | Labor ministry: salary minimums, labor regs | pending |
| mineconomia.gob.gt | Economy ministry: zonas francas / special regimes | pending |
| irtra.org.gt | IRTRA (patronal recreation institute) | pending |
| intecap.edu.gt | INTECAP (technical training, patronal contribution) | pending |
| totaldoc.com (partner tier) | Default FEL installer — public integration docs | pending |

## Verdicts legend

- **ACQUIRED** — downloaded to `gt/sources/NN_...`, registry row added, verified
  by reading page 1 (labels lie — SV lesson).
- **FLAG** — needs owner decision (unofficial mirror, ambiguous version,
  superseded-vs-historical call, blocked URL).
- **REJECT** — with reason (superseded with no historical value, out of scope,
  duplicate).
- **LEAD** — non-official copy of an official document we still need; official
  copy still hunted.

## Wave log

### W1 — e-invoicing core (SAT FEL technical + legal + provider layer)

- dispatched: 3 research agents (A: SAT FEL technical artifacts; B: FEL legal
  basis + regimes + timeline; C: provider layer — SAT installers registry +
  TotalDoc public docs). Research-only: return candidate lists, no downloads.

(candidate tables appended below as sweeps return)

## Candidates

## Open questions / blockers
