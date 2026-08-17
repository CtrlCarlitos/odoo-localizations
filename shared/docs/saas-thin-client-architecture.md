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
