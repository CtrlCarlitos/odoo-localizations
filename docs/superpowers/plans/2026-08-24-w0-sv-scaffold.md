# W0-SV: SV Implementation Wave 0 — Monorepo Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap `CtrlCarlitos/sv-implementation` (the private monorepo holding the LGPL-bound Odoo client, the proprietary Elixir SaaS, the MH simulator, the protocol mirror, and CI) with a trivial-but-real protocol round-trip green in CI — the exit gate of Wave 0.

**Architecture:** Per the approved spec: `client/odoo/` (Odoo 19.0 addon skeletons run under Takumi worktrees), `saas/elixir/` (Phoenix umbrella, `core` + `sv` apps run under the new tk phoenix stack), `sim/mh/` (schema-harness Elixir app), `protocol/` (pinned mirror of the canon-repo protocol spec), `ci/` (workflows + guards). Every test cites FR ids; every image is digest-pinned; the LGPL boundary is CI-enforced from day one.

**Tech Stack:** Odoo 19.0 (digest-pinned), Elixir/Phoenix (hexpm image, digest-pinned), PostgreSQL 17 (tk's pinned image), GitHub Actions, `ex_json_schema`, `jwcrypto`.

**Spec:** `odoo-localizations` canon repo `docs/superpowers/specs/2026-08-24-sv-implementation-program-design.md` (authoritative — §1 topology, §2 Wave-0 row, §3 protocol, §4 engineering details). Dependency: **W0-TK merged** (`2026-08-24-w0-tk-phoenix-stack.md`) — Tasks 3+ need the phoenix stack.

**Executes in:** `~/projects/CtrlCarlitos/sv-implementation` (new repo; created by Task 1). The canon repo (`odoo-localizations/.worktrees/sv`) holds this plan and the wave bookkeeping (Task 9).

## Global Constraints

- **LGPL boundary:** nothing under `client/` may reference `saas/`, `sim/`, or `protocol/` internals; client deps = Odoo + public PyPI only. CI-enforced (Task 7).
- **FR traceability:** every test file cites the FR ids it verifies as `# FR: SV-XXX-FR-nnn` comments; the lint resolves them against the vendored corpus FR-id list (Task 6). No test without a citable FR or a `# INFRA:` tag (scaffold-only tests).
- **Digest pinning:** all images pinned `name@sha256:...`; pins live in `pinned-images.env` at the repo root with the pull+inspect recipe in comments.
- **Value discipline (D15/D19 canon):** no default values for config-gap classes anywhere in scaffold code.
- **Commits:** short imperative, no emojis; push after each task.
- The protocol spec is **authored in the canon repo**; `protocol/` here is a mirror updated only by `scripts/sync-protocol.sh` (Task 5).

---

### Task 1: Repo + directory skeleton + license markers

**Files:**
- Create: repo `CtrlCarlitos/sv-implementation` (private), `README.md`, `.gitignore`, `pinned-images.env`, `client/odoo/.gitkeep`, `saas/elixir/.gitkeep`, `sim/mh/.gitkeep`, `protocol/README.md`, `ci/README.md`, `scripts/` dir, `client/COPYING.LESSER` (LGPL-3 text), `saas/HEADER.md` + `sim/HEADER.md` (proprietary notices).

**Interfaces:**
- Produces: the repo URL + root layout every later task builds inside.

- [ ] **Step 1: Create the repo**

```bash
cd ~/projects/CtrlCarlitos
gh repo create CtrlCarlitos/sv-implementation --private --confirm 2>/dev/null || gh repo create sv-implementation --private
mkdir -p sv-implementation && cd sv-implementation && git init -b main
```

- [ ] **Step 2: Layout + markers**

```
client/COPYING.LESSER     # https://www.gnu.org/licenses/lgpl-3.0.txt verbatim
client/README.md          # "LGPL-3 boundary. Publishable via subtree split. See canon spec §1."
saas/HEADER.md            # "Proprietary. CtrlCarlitos. Never distributed. See D2/D5."
sim/HEADER.md             # same class of notice
protocol/README.md        # "Mirror only — authoritative spec lives in odoo-localizations (canon). sync: scripts/sync-protocol.sh"
ci/README.md              # one line per workflow (filled Task 7)
pinned-images.env         # KEY=name@sha256:... lines, pull+inspect recipe in comment header
.gitignore                # elixir (_build, deps, *.ez), python (__pycache__), .env, /priv/static unless assets
```

- [ ] **Step 3: README (root)** — 10 lines max: what this repo is, canon pointer, "all environments via Takumi (tk)" pointer, CI badge placeholder.
- [ ] **Step 4: Commit + push**

```bash
git add -A && git commit -m "scaffold: monorepo skeleton with license boundaries" && git remote add origin git@github.com:CtrlCarlitos/sv-implementation.git && git push -u origin main
```

### Task 2: Odoo 19 pin + `l10n_sv` skeleton (installable, one INFRA test)

**Files:**
- Create: `client/odoo/l10n_sv/__init__.py`, `__manifest__.py`, `models/__init__.py`, `tests/__init__.py`, `tests/test_scaffold.py`

**Interfaces:**
- Produces: installable `l10n_sv` on Odoo 19.0; the `ODOO_19_IMAGE` pin in `pinned-images.env`; the `tk` worktree pattern all Odoo tasks reuse.

- [ ] **Step 1: Pin Odoo 19**

```bash
docker pull odoo:19
docker inspect --format '{{index .RepoDigests 0}}' odoo:19
# append to pinned-images.env: ODOO_19_IMAGE=<output>
```

- [ ] **Step 2: Module skeleton** — manifest (name `l10n_sv`, deps `['l10n_latam_invoice_document']` per D13, license `LGPL-3`, version `19.0.1.0.0`); empty `models/__init__.py`; test:

```python
from odoo.tests import TransactionCase

# INFRA: Wave-0 scaffold — module installability (spec §2 Wave 0)
class TestScaffold(TransactionCase):
    def test_module_installed(self):
        module = self.env['ir.module.module'].search([('name', '=', 'l10n_sv')], limit=1)
        self.assertTrue(module)
        self.assertEqual(module.state, 'installed')
```

- [ ] **Step 3: Run under tk**

```bash
export WORKSPACE_ROOT=~/projects/CtrlCarlitos/sv-implementation-customers  # tk resolves customers under this root
mkdir -p $WORKSPACE_ROOT/customers/sv-impl/main/client/odoo
cp -r client/odoo/l10n_sv $WORKSPACE_ROOT/customers/sv-impl/main/client/odoo/
# (Task 4 replaces this copy dance with a git worktree of sv-implementation itself as the customer repo)
tk create sv-impl main --image "$(grep ODOO_19_IMAGE pinned-images.env | cut -d= -f2)"
# then in the Odoo URL: install l10n_sv; assert no WARNING/ERROR in container logs
```

- [ ] **Step 4: Commit** — `git commit -m "l10n_sv: Odoo 19 skeleton (installable, INFRA test)"`

### Task 3: `l10n_sv_edi` skeleton + vault/signer interfaces (stubbed)

**Files:**
- Create: `client/odoo/l10n_sv_edi/{__init__.py,__manifest__.py,requirements.txt}`, `client/odoo/l10n_sv_edi/services/{__init__.py,vault.py,signer.py}`, `client/odoo/l10n_sv_edi/tests/test_signer_stub.py`

**Interfaces:**
- Produces: `l10n_sv_edi.services.vault.CertVault` (`load(env: str) -> CertPair | None` — stub returns None) and `l10n_sv_edi.services.signer.sign(cert: CertPair, payload: bytes) -> str` (stub: raises `NotImplementedError("Wave 1")`). Wave 1 replaces bodies; signatures are the Wave-1 contract.

- [ ] **Step 1: Failing test** — `# INFRA:` scaffold test: import both symbols, assert vault stub returns None and signer raises NotImplementedError("Wave 1").
- [ ] **Step 2: Verify it fails** (module not found → after Task 2's `tk` env is up, run via `tk exec sv-impl main -- odoo-bin ... --test-enable -i l10n_sv_edi` or a plain `python -c` import check inside the container — follow whichever the Task-2 worktree made natural).
- [ ] **Step 3: Implement stubs** (manifest deps `['l10n_sv']`, license LGPL-3; `requirements.txt`: `jwcrypto>=1.5`).
- [ ] **Step 4: Verify pass; commit** — `git commit -m "l10n_sv_edi: vault+signer Wave-1 interfaces, stubbed"`

### Task 4: Elixir umbrella `saas/elixir` (core + sv) under the tk phoenix stack

**Files:**
- Create: `saas/elixir/` mix umbrella (`apps/core`, `apps/sv`), `.formatter.exs`, `mix.exs`
- Modify: `pinned-images.env` (`PHOENIX_IMAGE`)

**Interfaces:**
- Produces: `core` app with `CoreWeb.Endpoint` `/healthz` → `200 {"status":"ok"}`; `sv` app router `POST /v1/sv/dte/prepare` and `POST /v1/sv/dte/:id/signed` returning the §3 envelope; `GET /v1/sv/state`. Run command env contract: `DATABASE_URL`, `PHX_HOST`, `PORT=4000` (the tk phoenix stack provides all three).

- [ ] **Step 1: Scaffold the umbrella inside the container** (no host Elixir — everything via the pinned image):

```bash
IMG="$(grep PHOENIX_IMAGE pinned-images.env | cut -d= -f2)"
docker run --rm -v "$PWD/saas/elixir:/work" -w /work "$IMG" sh -c \
  "mix new core --sup && mix new sv --sup" # then move both under apps/, create root mix.exs umbrella
```

- [ ] **Step 2: Healthz** — TDD in-container: write `test/core_web/controllers/health_controller_test.exs` asserting `conn |> get("/healthz") |> json_response(200, %{"status" => "ok"})`; implement router+controller; `mix test` green.
- [ ] **Step 3: Protocol envelope stubs + dev auth plug** — fixture creds first (spec §4: dev-mode fixture creds committed): `apps/sv/priv/dev_creds.json` = `{"api_key": "dev-wave0-key", "company_nit": "06142206171022"}` (a syntactically-valid dummy NIT, not a real one); `SvWeb.Plugs.Auth` reads it (dev only), rejects missing/wrong `Authorization: Bearer` with 401 `{"error": "entitlement", "detail": "invalid key"}`. Then `SvWeb.DTEController`:

```elixir
# Wave-0 stub: shapes only. Real generation = Wave 1 (SaaS IP per D2).
# FR: SV-PROT-FR-001 (protocol contract surfaces)
def prepare(conn, params) do
  json(conn, %{
    dte_id: Ecto.UUID.generate(),
    canon_json: params,
    mh_schema_valid: true,
    warnings: [],
    plan: %{sign_payload: "WAVE1-STUB"},
    entitlement: %{status: "active", expiry: nil, grace: false},
    protocol_version: "sv/0.1.0"
  })
end

def signed(conn, %{"id" => id}) do
  json(conn, %{
    dte_id: id, estado: "SIMULADO",
    sello: nil, codigo_generacion: nil, mh_response: nil,
    entitlement: %{status: "active", expiry: nil, grace: false},
    protocol_version: "sv/0.1.0"
  })
end
```

with the contract test asserting every §3 envelope key on both endpoints (`# FR: SV-PROT-FR-001`).
- [ ] **Step 4: Run under tk phoenix stack** (requires W0-TK merged). The customer-repo recipe (tk resolves worktrees under `$WORKSPACE_ROOT/customers/<customer>/`):

```bash
export WORKSPACE_ROOT=~/tk-workspace   # separate from source checkouts, per tk's model
mkdir -p "$WORKSPACE_ROOT/customers/sv-saas" && cd "$WORKSPACE_ROOT/customers/sv-saas"
git -C ~/projects/CtrlCarlitos/sv-implementation worktree add main main
cd "$WORKSPACE_ROOT"
tk create sv-saas main --stack phoenix --app-image "$(grep PHOENIX_IMAGE pinned-images.env | cut -d= -f2)"
# healthz via https://sv-saas-main.localhost/healthz; record this exact recipe in saas/elixir/README.md
```

- [ ] **Step 5: Commit** — `git commit -m "saas: phoenix umbrella (core healthz + sv protocol-envelope stubs)"`

### Task 5: Protocol v0.1 authored (canon) + mirror + sync script

**Files:**
- Create (canon repo): `sv/protocol/sv-protocol.md` (v0.1.0 — §3 endpoints verbatim, envelope tables, error taxonomy, semver header + changelog)
- Create (monorepo): `scripts/sync-protocol.sh`, `protocol/sv-protocol.md` (mirror)

**Interfaces:**
- Produces: `protocol/VERSION` file (`sv/0.1.0`) consumed by the `sv` app's `protocol_version` field (replace the hardcoded string with a compile-time read — `elixir: File.read!("../../protocol/VERSION")` in config, path relative to umbrella root at build time).

- [ ] **Step 1: Write the protocol doc in the canon repo** (from spec §3; every response field tabulated; error taxonomy `validation|regulator|system|entitlement` with semantics).
- [ ] **Step 2: sync script**

```bash
#!/usr/bin/env bash
# Copies the authoritative protocol spec from the canon repo into this
# mirror. Run whenever the canon version bumps. Fails if VERSION regressed.
set -euo pipefail
CANON="${CANON_ROOT:?~/projects/CtrlCarlitos/odoo-localizations}"
SRC="$CANON/sv/protocol/sv-protocol.md"
[ -f "$SRC" ] || { echo "missing $SRC"; exit 1; }
cp "$SRC" protocol/sv-protocol.md
grep -oP 'Version: sv/\K[0-9.]+' protocol/sv-protocol.md > protocol/VERSION
git add protocol/ && echo "mirrored $(cat protocol/VERSION)"
```

- [ ] **Step 3: Wire `protocol_version`** to the VERSION file; contract test updated to assert equality with `protocol/VERSION`.
- [ ] **Step 4: Commit both repos** (canon: protocol v0.1 spec + push sv-research; monorepo: mirror + script).

### Task 6: `sim/mh` skeleton — schema harness green

**Files:**
- Create: `sim/mh/` (mix app in the same umbrella workspace as `saas/elixir` — sibling directory, shared deps per spec §4), `sim/mh/priv/schemas/` + `sim/mh/priv/schemas/MANIFEST.sha256`, `sim/mh/lib/sim_mh/schema_bank.ex`, `sim/mh/test/sim_mh/schema_bank_test.exs`

**Interfaces:**
- Produces: `SimMh.SchemaBank.load!()/validate!(doc_path, doc)` — loads the 15 DTE/event schemas, validates a document against one; consumed by Wave 1's full simulator.

- [ ] **Step 1: Vendor the schemas** — from the canon's `52_` zip (byte-pinned `schemas/` per registry): extract to `sim/mh/priv/schemas/fe-v1.json` etc. (all 15), then `sha256sum` each into `MANIFEST.sha256`; a test asserts every file still matches the manifest (`# INFRA:` + `# FR: SV-EINV-FR-054` for env-separation files where relevant — cite only schema-anchored FRs you can see in the corpus).
- [ ] **Step 2: Failing tests** — generate the minimal FE fixture deterministically from the schema (no hand-authoring): a small mix task `mix sim_mh.gen_fixture fe > test/fixtures/fe_minimal.json` that walks `fe-v1.json`'s `required` tree, emitting each required scalar with a type-derived placeholder (`string` → `"X"`, numbers → `0`, enums → first value) — the generator is ~40 lines and doubles as Wave-1 test tooling. Tests: `SchemaBank.validate!("fe", read_fixture())` returns `:ok`; `validate!("fe", %{})` raises naming the first missing required property.
- [ ] **Step 3: Implement** — `ex_json_schema` dep; `load!` parses all schemas at boot into a `%{binary => schema}` map keyed by short type (`fe`, `nc`, …, `evento_*`).
- [ ] **Step 4: `mix test` green (in-container); commit** — `git commit -m "sim/mh: schema bank + manifest-pinned 52_ schema set"`

### Task 7: CI — workflows + guards

**Files:**
- Create: `.github/workflows/elixir.yml`, `.github/workflows/odoo.yml`, `ci/fr_ids.txt` (vendored), `ci/lint_fr_traceability.py`, `ci/lint_lgpl_boundary.sh`

**Interfaces:**
- Produces: CI that (a) runs `mix test` for saas+sim on setup-beam with a postgres service; (b) builds the Odoo image (from `ODOO_19_IMAGE` pin) with both addons and runs their tests; (c) runs both lints.

- [ ] **Step 1: FR-traceability lint** — vendored `fr_ids.txt` generated from the canon (`rg -oN "SV-[A-Z]+-FR-[0-9]{3}" sv/requirements --no-filename | sort -u > ci/fr_ids.txt`); the Python lint: every `# FR:` citation in `**/tests/**` (py + exs) must resolve; every test file must contain ≥1 `# FR:` or `# INFRA:` marker.
- [ ] **Step 2: LGPL guard** — `ci/lint_lgpl_boundary.sh`: fail if any file under `client/` matches `saas/|sim/|../` in imports/requires/mounts (grep patterns per spec §1).
- [ ] **Step 3: Workflows** — elixir.yml (ubuntu-latest, `elixir: 1.18.4-otp-27`, services: postgres:17, `mix test` in `saas/elixir` + `sim/mh`); odoo.yml (docker build from pinned base + addons, `odoo-bin -i l10n_sv,l10n_sv_edi --test-enable --stop-after-init`, log-hygiene grep for WARNING/ERROR).
- [ ] **Step 4: Push + verify a green run on GitHub; fix what it catches; commit.**

### Task 8: Wave-0 exit-gate verification (local, under tk)

- [ ] Trivial round-trip on the tk phoenix stack: `POST /v1/sv/dte/prepare` (curl from host against the worktree URL) → envelope with all §3 keys + `protocol_version == protocol/VERSION`; `POST /v1/sv/dte/<id>/signed` → `estado: SIMULADO`. Record the transcript in `docs/wave0-transcript.md`.
- [ ] Odoo worktree: both modules installed, tests green, logs clean.
- [ ] CI green on main. **This is the Wave 0 exit gate (spec §2).**

### Task 9: Canon bookkeeping

- [ ] In the canon repo (`.worktrees/sv`): `sv/HANDOVER.md` gains the "Implementation program" section — W0 close record: monorepo SHA, tk merged SHA (from W0-TK), gate status, protocol v0.1 location. Commit + push sv-research. Merge to main = owner decision (§4.6 protocol).
