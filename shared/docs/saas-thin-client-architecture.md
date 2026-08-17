# Product Architecture — SaaS Core + Open-Source Thin Client

**Status: OPEN — framing note. Boundary decisions (Q1–Q8) need a dedicated
socratic session BEFORE S1 synthesis writes Odoo Mapping sections.**

## Strategic intent

The El Salvador localization (and later GT/HN) ships as:

1. **Open-source Odoo module (thin client)** — free to clone; minimal logic;
   talks to the SaaS. Cloning it is legal and welcome: without the SaaS it
   does nothing.
2. **Proprietary SaaS platform (Elixir/Phoenix)** — the actual localization
   brain: document generation, signing, transmission, validation, catalogs,
   events, version management. Access = paid subscription.

The moat is the SaaS logic, not the client code. Monetization works because
the artifact people want (working e-invoicing) only exists behind the API.
Takumi's role shifts: it builds/maintains **thin clients**, and the SaaS is a
separate (Elixir) codebase — requirements must serve BOTH.

## What this means for THIS repository

Requirements are written once but consumed twice:

- **Odoo Mapping sections** must state, per FR, WHERE the logic lives:
  `odoo` (client), `saas` (Elixir core), or `shared` (contract between them).
- The client↔SaaS **API contract** itself becomes a requirements artifact
  (it's the surface Takumi builds against and the thing users depend on).
- The version-regime problem (see
  [regulatory-change-management.md](regulatory-change-management.md))
  simplifies on one axis and worsens on another: spec upgrades deploy
  centrally in the SaaS (no client migration wave), but the API contract
  versioning now mirrors the regulator's versioning.

## Legal constraints (El Salvador facts that shape the boundary)

From our evidence passes — verify equivalents per country:

1. **The emitter is responsible, always** (CT 119-A/119-G; EVID-083).
   Delegating processing to a SaaS does not delegate legal liability. ToS
   must reflect this.
2. **Conservation is the emitter's duty** (CT 147 reformed by D.L. 487:
   AT is explicitly NOT the emitter's archive; EVID-083). If the SaaS stores
   DTEs, that's a service, not a legal discharge — the client must be able
   to hold/export the emitter's DTE archive (10 years).
3. **Contingency mode requires continued operation** when MH is
   unreachable (deferred generation + delivery + later batch). If the SaaS
   itself is unreachable, the thin client cannot invoice at all — decide:
   acceptable (SLA argument) or local-fallback required (IP argument against;
   complexity argument for SaaS-only).
4. **Signing certs are per-emitter, personalized per environment**
   (EVID-080/083). Who holds the private key — emitter (client-side firmador,
   MH's own reference pattern) or SaaS (custody + liability questions)?
5. **Deadlines are short and sanctionable** (24h rejection fix, 1-day
   invalidation, 10-hábiles declarations). SaaS uptime and queue latency are
   compliance parameters, not conveniences.

## Candidate split (TO BE DECIDED — not a decision record)

Illustrative only:

| Capability | Candidate layer | Notes |
|---|---|---|
| DTE JSON generation (all 11+ types, 4 events) | saas | Core IP: schema matrix, rounding/holgura, per-type rules |
| numeroControl / codigoGeneración | saas or shared | Sequencing state lives where? |
| Catalogs (CAT-001..033+) | saas (served) / odoo (cached subset) | Dated-version serving (see change-mgmt note) |
| Signing (JWS) | odoo-local firmador vs saas | Key custody question (Q4) |
| Transmission + retry + event ordering | saas | 8s/2-retry, affected-before-affecting (EVID-084) |
| Sello/state storage, Archivo DTE, RG/QW rendering | saas + odoo mirror | Emitter archive duty (point 2) |
| Invoice posting, taxes, accounts | odoo (native) | Odoo stays the ERP; SaaS never books |
| Entitlement/auth (API keys, subscription) | saas | The paywall |

## Monetization & IP-protection mechanics (candidates)

- Client license: Odoo-ecosystem-compatible (OPL-1 or LGPL-3 — confirm; AGPL
  pressure from Odoo community edition hosting must be analyzed).
- Trademark/branding: name + logo reserved even where code is open.
- SaaS ToS: per-company subscriptions, API keys, fair-use, audit rights,
  termination = client keeps data (export), loses service.
- Abuse signals: key sharing detection, anomaly telemetry (opt-in? legal?).
- Pricing surfaces to model in requirements: per-company, per-DTE-volume,
  per-doc-type bundles (CRE/DCLE users differ from FE-only retail).

## Open questions (socratic session agenda)

- **Q1:** Exact capability split (the table above is a strawman).
- **Q2:** API contract shape: one REST surface per country vs unified;
  versioning policy; SDK generation for Takumi.
- **Q3:** Offline/contingency posture: SaaS-only vs local fallback — legal
  risk vs IP exposure tradeoff.
- **Q4:** Signing key custody: emitter-held (local firmador container) vs
  SaaS-held (HSM, custody liability).
- **Q5:** Data residency & archive: what the client must store/export to
  satisfy CT 147 if the SaaS relationship ends.
- **Q6:** Client license choice + Odoo marketplace/hosting implications.
- **Q7:** Entitlement model & enforcement (and what a non-payer's Odoo
  degrades to).
- **Q8:** Multi-country: shared SaaS core with country packs vs per-country
  services (Elixir umbrella app?) — affects GT/HN requirements reuse.

## Immediate plan impact (adopted)

- S1 synthesis gains a **pre-step (S0.5): architecture-split session** —
  boundary must be settled before Odoo Mapping sections are written.
- Requirements template: Odoo Mapping table gains a **Layer** column
  (`odoo` / `saas` / `shared`); done in this commit.
- S1 deliverables add: `sv/requirements/e-invoicing/` files must include
  the client↔SaaS API contract FRs (transmission/state/archive/entitlement
  surfaces) alongside fiscal FRs.

---

## S0.5 DECISION LOG (in progress)

### D1 — Contingency & resilience posture (2026-08-16)

**Decision:** SaaS deployed on Fly.io multi-region (distributed sites). No
local-fallback generation in the client. Residual risk = customer↔SaaS
network partition, accepted and framed contractually (target: availability
≥ MH's own; ToS positions residual risk as force majeure per CT 119-F
logic).

**Rationale:** MH-outage contingency (the legally-recognized case) is
handled centrally by the SaaS in deferred mode. Our own outage is an
engineering problem (multi-region) not an architectural one; adding local
generation to mitigate it would leak the rules engine into the open client.

### D2 — Generation/signing split + private protocol (2026-08-16)

**Decision:**
- **Generation, sequencing, transmission, events, state, catalogs, version
  management: SaaS-side** (numeroControl sequencing stays a single
  server-side store — no fleet drift).
- **Signing: client-side** (Odoo holds the emitter's cert + private key in
  an encrypted vault model; Python JWS/RS512 signer; MH's own on-prem
  firmador pattern — SaaS never touches private keys).
- **The client↔SaaS wire format is a PRIVATE MINIMAL PROTOCOL** — it does
  not resemble the government JSON. The SaaS compiles/transforms it into
  the public MH schema (which lives only SaaS-side, with the transformation
  and validation logic = core IP).
- **Validation runs at BOTH ends**: client-side pre-validation (cheap,
  early rejection in Odoo) + SaaS-side authoritative validation; the
  round-trip must surface every validation result to the client.

**Consequences adopted:**
- The private protocol is a first-class versioned contract artifact
  (semver + changelog + deprecation windows), maintained in this repo's
  requirements; it decouples from MH's spec cadence.
- Client-side cert vault is client-side security surface we own: encrypted
  storage, per-environment (test/prod) cert handling.
- Offline posture per D1: without SaaS connectivity the client cannot
  generate — accepted.

### D3 — Archive & exit: tiered retention (2026-08-16)

**Decision:** Archive custody is a PAID TIER CHOICE, not a single posture:

- **Tier A (base):** Client is system of record — every sealed DTE (Archivo
  DTE + RG) mirrored into Odoo at response time; CT 147 duty satisfied
  locally even with zero SaaS. Exit = keep everything, lose service.
- **Tier B (paid):** SaaS-hosted archive — long-term conservation, search,
  re-download, RG re-rendering on the platform; exit export (structured
  dump) included while account is in good standing.
- Tier-down (B→A or cancel) always leaves the emitter compliant via the
  local mirror; ToS makes clear SaaS hosting is a convenience on top of the
  emitter's own duty.

**Rationale (user):** monetization opportunity — "we get paid more if we do
more" — while keeping every customer's legal baseline satisfied by Tier A
(mirroring is not optional on the client side; hosting is).

### D4 — Entitlement enforcement (2026-08-16)

**Decision:** Hard wall — no valid subscription, no DTE generation (SaaS
refuses private-protocol calls; client cannot invoice electronically).
Mitigation is aggressive pre-cutoff UX, not soft degradation:

- Escalating reminders via email AND Odoo interface (banner states:
  warning → urgent → final) driven by SaaS-reported subscription state in
  every protocol response.
- Grace/dunning windows configurable per ToS; the client renders them but
  enforcement is server-side only (never trust the client).
- Read paths (local mirrored archive) keep working offline of entitlement —
  they are the emitter's own data (per D3 Tier A).

**Consequence:** private protocol responses must carry subscription/entitlement
state (status, expiry, grace flags) as a standing field — client banner FRs
derive from it.
