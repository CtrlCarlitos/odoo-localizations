# GT Source Research — Design

**Date:** 2026-08-18
**Status:** Approved in session (design presented 2026-08-18; this file records it) — pending spec review
**Branch:** `gt-research` (worktree `.worktrees/gt-research`); merges to `main` at milestone by owner decision

## Purpose

Deep research to build the Guatemala source corpus from scratch: discover,
triage (relevant / current / useful / official), and acquire the official
documents that GT requirements extraction will read — the work that, for El
Salvador, happened organically before and alongside extraction (SV `sources/`
01–73). GT has no prior work (no hint layer), so this research also produces
the written research record SV never had.

Output feeds `gt/EXTRACTION_PLAN.md` (Stage 0 of
`shared/docs/requirements-extraction-procedure.md`): source inventory,
decomposition, reading order, topic map, risks.

## Decisions (product owner, 2026-08-18)

| # | Decision | Choice | Rationale |
|---|----------|--------|-----------|
| D-GT1 | Topic scope | Full SV mirror: e-invoicing (FEL), taxation, payroll, fiscal-reporting, chart-of-accounts, commercial-legal, special-regimes, catalogs | One research pass across all official sites now; avoids a second sweep later |
| D-GT2 | Deliverable mode | Acquire as we go | SV precedent: documents land in `gt/sources/` with registry rows as they are triaged; ambiguous items are flagged for owner decision, never guessed |
| D-GT3 | Source policy | Strict official-only | Mirrors (law firms, news, universities) never registered; recorded as acquisition leads when the official copy cannot be found (SV precedent: rejected law-firm PDF mirrors) |
| D-GT4 | Prior work | None — blank slate | No tuky-workspace-style hint layer exists for GT |
| D-GT5 | FEL integration model | Provider-mediated | Unlike SV (direct SaaS↔MH), GT FEL operates through SAT-authorized **certificadores**; SAT owns the XML standard and validates. Product will support multiple providers; **TotalDoc = default provider** |
| D-GT6 | Partner tier | Provider docs register under `partner-technical` provenance | Provider technical documentation (TotalDoc et al.) lives in `gt/sources/providers/<provider>/`, LB-citable only for provider-interface requirements, clearly marked non-government. Public docs only for now; partner-portal access is a later follow-up |
| D-GT7 | Workspace | `.worktrees/gt-research` on branch `gt-research` | Isolates the live SV session on `main`. `main` receives exactly one infrastructural commit (`.gitignore` line for `.worktrees/`, commit f6f5415). Same convention as the HN session |
| D-GT8 | Odoo journal/document-type model | Use `l10n_latam_invoice_document`: **one journal with multiple document types** (FEL FACE/FACC/FPEQ/NC/ND/RD… via `l10n_latam_document_type`), NOT one journal per document type | Product owner decision 2026-08-18. GT requirements Odoo Mapping sections must encode this; evaluation at synthesis whether to promote to a shared cross-country pattern (SV DTE model is a separate surface) |
| D-GT9 | Establishment/point-of-emission mapping | FEL DTEs identify the emission point (NIT + **código de establecimiento** per sucursal; dispositivo/point-of-emission fields where the schema carries them, e.g. cash registers). Odoo Mapping MUST cover **sucursales (branches), warehouses/bodegas, and cash registers/POS** → establishment/dispositivo codes on every DTE-emitting surface | Product owner decision 2026-08-18. Confirm exact schema field names (`Establecimiento`/`DispositivoID`-kin) in the XSD/Reglas evidence pass before finalizing the mapping |

## Research method

### Official domains (coverage map lives in `gt/SOURCE_RESEARCH.md`)

- `sat.gob.gt` / `portal.sat.gob.gt` — SAT: FEL normative + technical, forms, manuals, calendars, laws
- `cat.desa.sat.gob.gt` — FEL XSD schemas + JSON catalogs (official host, reachable)
- `github.com/notificacioneselectfel/Catalogo-FEL` — XSD/catalogs channel maintained by SAT Gerencia de Informática; linked from SAT's own technical-docs page (ratification: see Open Questions)
- `dca.gob.gt` / `legal.dca.gob.gt` — Diario de Centro América (official gazette; `diario.gob.gt` is dead)
- `igssgt.org` — IGSS social security
- `mintrabajo.gob.gt` — labor ministry (salario mínimo, labor regs)
- `mineconomia.gob.gt` — economy ministry (zonas francas / special regimes)
- `irtra.org.gt`, `intecap.edu.gt` — patronal contributions
- `congreso.gob.gt` — has NO online law library (verified W1); laws come from SAT/DCA instead
- `totaldoc.com` (+ related hosts) — partner tier, default FEL certificador

### Triage rubric (per candidate)

1. **Relevant?** — does it govern/define something in the 8-topic scope?
2. **Current?** — supersession/reform chain noted; superseded items kept only as historical LB (SV discipline)
3. **Useful?** — law / manual / form / catalog / schema — which corpus role?
4. **Official?** — `.gob.gt` or ratified official channel; else lead/flag

Verdicts: **ACQUIRE** / **FLAG** (owner decision) / **REJECT** (+reason) /
**LEAD** (non-official copy of an official doc still being hunted).

### Acquisition discipline (SV lessons baked in)

- Registry rows with provenance URL for every file; SV-style `NN_Name.ext`
  numbering from `01_`
- Verify every download by reading page 1 — labels and filenames lie
  (SV: factura.gob.sv ID shuffle; SAT W1: a resolution link labeled 639-2020
  pointing at a 639-**2011** PDF)
- Supersession discipline: capture delta/effective date/reform chain before
  synthesis trusts a source; mark superseded files in the registry
- Never guess dates/versions/decrees — "not shown" is a recorded finding

### Execution mechanics

- Controller (this session) downloads, verifies, registers, commits
- Parallel research-only subagents sweep site/topic clusters and return
  candidate lists + assessments; they never write or download
- Findings and verdicts land in `gt/SOURCE_RESEARCH.md` (durable record —
  subagent output does not survive)
- No push until milestone; merge decision is the owner's

## Deliverables

1. `gt/sources/` — acquired corpus (+ `gt/sources/providers/` partner tier) with registry rows in `gt/sources/README.md`
2. `gt/SOURCE_RESEARCH.md` — research record: every candidate + verdict, site coverage map, open questions, blockers
3. `gt/README.md` — sources section updated as the corpus grows
4. `HANDOVER.md` — updated at milestone (GT state + rulings)
5. Optional at milestone: `gt/EXTRACTION_PLAN.md` Stage-0 skeleton (inventory, reading order, topic map, risks) for owner review

## Wave structure

| Wave | Scope | Status |
|------|-------|--------|
| W1 | E-invoicing core: SAT FEL technical artifacts + legal basis + provider layer | Sweeps returned 2026-08-18; acquisition pending |
| W2 | Taxation core laws: IVA (Dto. 27-92 + AG 5-2013), Código Tributario (Dto. 6-91), ISR/LAT (Dto. 10-2012 + AG 213-2013), retenciones/anticipos | pending |
| W3 | Payroll: Código de Trabajo, IGSS, salario mínimo, aguinaldo/bono 14, IRTRA/INTECAP | pending |
| W4 | Fiscal reporting: SAT forms/declarations, calendario fiscal | pending |
| W5 | Chart-of-accounts (Código de Comercio, PCGA/NIIF-PYMES), commercial-legal (AML, registro mercantil), special-regimes (zonas francas Dto. 65-89, ley de zona libre, etc.) | pending |
| W6 | Partner follow-ups: TotalDoc partner-portal items (API manuals, sandbox, SDK) | blocked on partner access |

## W1 structural findings that shape the corpus (2026-08-18)

- **Terminology**: GT uses **certificadores de DTE** (18 authorized; registry
  is an HTML page), not "instaladores". **TotalDoc = GRUPO CDS S.A., NIT
  107902281**, authorized 02/12/2021 → **02/12/2026 (expires ~3.5 months out —
  track renewal)**.
- **No "Anexo técnico" document exists.** The functional equivalents:
  *Reglas y validaciones* (versioned PDF chain 1.5.1 → 1.7.9 → current id
  85864), *Documento Técnico Servicios* (SAT↔certificador web-service spec),
  XSD schemas (26 files, GT_Documento-0.2.1 + complements), JSON catalogs
  (mensajes / unidades gravables / frases).
- **FEL legal chain**: Acuerdo de Directorio **13-2018** (creates FEL, in
  force 23-May-2018) → reformed by **26-2019** → **15-2020**; mandatory
  incorporation via Resoluciones SAT-DSI 243-2019 … 1240-2021 (general IVA
  regime) … 1350-2022 (pequeños contribuyentes) … 400-2023. No single
  national-mandate law verified (a "Decreto 6-2021" is UNVERIFIED — never cite
  until confirmed).
- **ISR today = Decreto 10-2012 (Ley de Actualización Tributaria) + AG
  213-2013** — SAT's own listing supersedes the old Dto. 26-92 codification.
  Ley IVA = Dto. 27-92 + Reglamento AG 5-2013. Código Tributario = Dto. 6-91.
- **Schema drift**: `GT_Documento-0.2.1.xsd` differs between cat.desa
  (52,176 B) and GitHub main (67,278 B); endoso/GLP XSDs and CatalogoFrases
  0.6.0 exist only on GitHub. Which revision production validates against is
  an open question.

## Constraints & risks

- **`portal.sat.gob.gt` blocks non-browser clients (Cloudflare 403, even with
  browser UA)**. Acquisition routes for portal-hosted PDFs: Wayback snapshots
  of official URLs (provenance noted, flagged for re-verification), or owner
  manual browser download. `cat.desa` and the GitHub repo serve directly.
- `legal.dca.gob.gt` search is a JS app — gazette retrieval needs a browser
  session or alternate routes.
- Most SAT pages print no dates — dates must come from document contents or
  wpfd Creado/Actualizado metadata (browser-only).
- Congreso has no law library; law consolidations depend on SAT/DCA hosting.

## Open questions (owner rulings pending)

1. ~~GitHub ratification~~ **RESOLVED 2026-08-18**: ratified; both GitHub
   (pinned SHA 961133c) and cat.desa acquired as `29_`/`30_`.
2. ~~Portal PDF acquisition route~~ **RESOLVED 2026-08-18**: manual browser
   downloads by owner; queue `gt/DOWNLOAD_QUEUE.md`; inbox-staged.
3. **Schema drift (cat.desa vs GitHub)** — 8 of 17 shared files differ
   (measured). Which revision do certificadores validate against in
   production? Affects which copy is corpus authority.
4. **"Decreto 6-2021"** — hypothesized e-invoicing mandate law, unverified on
   any official page. Do not cite until confirmed.

## Success criteria

- Corpus covers all 8 topics with official (or ratified) provenance and a
  registry row per file; every ACQUIRE verified by page-1 read
- Every W1–W5 candidate recorded in `gt/SOURCE_RESEARCH.md` with a verdict;
  every open question explicit (no silent picks)
- Owner-reviewable at milestone: merge or continue-waves decision

## Out of scope (this phase)

- Reading/evidence passes (Stage 2+) — extraction starts after EXTRACTION_PLAN
- Requirements files — synthesis waves come later
- Partner-portal (login) documentation — W6 follow-up when access exists
