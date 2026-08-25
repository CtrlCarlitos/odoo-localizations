# W0-TK: tk Phoenix Stack Extension Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give `takumid`/`tk` a second worktree stack type — `phoenix` (digest-pinned app image + Postgres behind the same isolated-network/Caddy topology as the Odoo stack) — so the SV implementation program can run its Elixir SaaS and MH simulator under the same Takumi reproducibility discipline as Odoo.

**Architecture:** Additive extension of the existing create/destroy/ports/list flow: a `Stack` discriminator on the create request routes `PrepareCreate`/`Create` to a stack-specific app-container starter; container naming and `List` move from the hardcoded `-odoo` name suffix to a `takumi.role` label; `Destroy`/`Ports` resolve container names by stack. Odoo behavior is byte-for-byte unchanged (same defaults, same names, same labels plus the new role label).

**Tech Stack:** Go (existing cobra CLI + Docker SDK client), Docker, existing test approach (table-driven unit tests + `tests/fixtures` scripts).

**Spec:** `odoo-localizations` canon repo, `docs/superpowers/specs/2026-08-24-sv-implementation-program-design.md` §4 (Takumi extension decision) + `takumi-dream/HANDOVER-ODOO-DEVELOPMENT-INFRASTRUCTURE-V3.md` (daemon conventions: digest pinning, idempotent retry, Prepare/Create split, adversarial-review comment style).

**Executes in:** `~/projects/CtrlCarlitos/takumi-dream` (branch off `main`; PR into the owner's cross-platform testing flow — do NOT merge past the owner's review).

## Global Constraints

- Repo conventions: every exported symbol gets a doc comment; non-obvious decisions cite the governing spec/handover section in a comment (match `worktrees.go` style).
- Images pinned by digest, never floating tags: new `defaultPhoenixImage` follows the `defaultOdooImage` comment discipline (pull → `docker inspect --format '{{index .RepoDigests 0}}'`).
- Same-owner retry must stay idempotent end-to-end (container-create name-conflict and network already-connected conflicts tolerated) — the M7/R2-L5 contract.
- No breaking changes to the existing Odoo path: `CreateRequest` without `Stack` behaves exactly as today; `List`/`Ports`/`Destroy` for Odoo worktrees return the same values as before (Ports gains only the role-agnostic rename of the `odoo` field — see Task 5 for the compatibility decision).
- `go vet ./...` and `go test ./...` green before every commit.

---

### Task 1: API types — `Stack` + `AppImage` + role response field

**Files:**
- Modify: `takumi-local-platform/internal/api/types.go`
- Test: `takumi-local-platform/internal/api/types_test.go` (create)

**Interfaces:**
- Produces: `CreateRequest.Stack string` (JSON `stack`; empty = `"odoo"`), `CreateRequest.AppImage string` (JSON `app_image`), `WorktreeInfo.Stack string` (JSON `stack`). Consumed by Tasks 2-6.

- [ ] **Step 1: Write the failing test**

```go
package api

import (
	"encoding/json"
	"strings"
	"testing"
)

func TestCreateRequestStackRoundTrip(t *testing.T) {
	var req CreateRequest
	in := `{"customer":"sv","worktree":"main","stack":"phoenix","app_image":"hexpm/elixir:1.18-otp-27@sha256:abc"}`
	if err := json.NewDecoder(strings.NewReader(in)).Decode(&req); err != nil {
		t.Fatal(err)
	}
	if req.Stack != "phoenix" || req.AppImage != "hexpm/elixir:1.18-otp-27@sha256:abc" {
		t.Fatalf("got stack=%q app_image=%q", req.Stack, req.AppImage)
	}
	out, err := json.Marshal(req)
	if err != nil {
		t.Fatal(err)
	}
	if !strings.Contains(string(out), `"stack":"phoenix"`) {
		t.Fatalf("missing stack in %s", out)
	}
}

func TestWorktreeInfoStackField(t *testing.T) {
	var info WorktreeInfo
	if err := json.Unmarshal([]byte(`{"customer":"sv","worktree":"main","url":"https://x","status":"up","stack":"phoenix"}`), &info); err != nil {
		t.Fatal(err)
	}
	if info.Stack != "phoenix" {
		t.Fatalf("got %q", info.Stack)
	}
}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd takumi-local-platform && go test ./internal/api/ -run Stack -v`
Expected: FAIL (compile error: unknown field Stack).

- [ ] **Step 3: Minimal implementation**

In `types.go`, extend `CreateRequest` and `WorktreeInfo`:

```go
// Stack selects the worktree's application stack: "" or "odoo" (default)
// keeps today's exact behavior; "phoenix" runs a digest-pinned
// Elixir/Phoenix app container beside the shared Postgres container,
// same network topology (W0-TK spec §Architecture).
Stack string `json:"stack"`    // optional; "" = "odoo"
// AppImage is the digest-pinned application image for non-odoo stacks.
// Required when Stack = "phoenix"; ignored otherwise.
AppImage string `json:"app_image"`
```

```go
type WorktreeInfo struct {
	Customer string `json:"customer"`
	Worktree string `json:"worktree"`
	URL      string `json:"url"`
	Status   string `json:"status"`
	// Stack echoes the worktree's stack ("odoo" or "phoenix"); set by
	// the daemon from the role label, never trusted from the request.
	Stack string `json:"stack"`
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `go test ./internal/api/ -v`
Expected: PASS (all api tests).

- [ ] **Step 5: Commit**

```bash
git add internal/api/types.go internal/api/types_test.go
git commit -m "api: stack + app_image create fields, stack on worktree info"
```

### Task 2: Stack resolution — pure functions (normalize, names, roles)

**Files:**
- Create: `takumi-local-platform/internal/daemon/stacks.go`
- Create: `takumi-local-platform/internal/daemon/stacks_test.go`

**Interfaces:**
- Consumes: `api.CreateRequest.{Stack,AppImage}` (Task 1).
- Produces: `normalizeStack(req api.CreateRequest) (api.CreateRequest, error)`; `phoenixContainerName(customer, worktree string) string`; constants `roleLabel = "takumi.role"`, `RoleOdoo = "odoo"`, `RolePhoenix = "phoenix"`. (`startPhoenix` lands in Task 3 with the helpers it needs.)

- [ ] **Step 1: Write the failing test** — the five-function test file from the draft below, matching the repo's table-test style (`worktrees_test.go` pattern):

```go
package daemon

import (
	"testing"

	"github.com/CtrlCarlitos/takumi/internal/api"
)

func TestNormalizeStack(t *testing.T) {
	tests := []struct {
		name    string
		req     api.CreateRequest
		want    string
		wantErr bool
	}{
		{name: "empty defaults to odoo", req: api.CreateRequest{Customer: "sv", Worktree: "w"}, want: RoleOdoo},
		{name: "explicit odoo", req: api.CreateRequest{Stack: "odoo"}, want: RoleOdoo},
		{name: "phoenix with digest image", req: api.CreateRequest{Stack: "phoenix", AppImage: "hexpm/elixir:1.18-otp-27@sha256:abc"}, want: RolePhoenix},
		{name: "phoenix without app_image errors", req: api.CreateRequest{Stack: "phoenix"}, wantErr: true},
		{name: "phoenix with floating tag errors", req: api.CreateRequest{Stack: "phoenix", AppImage: "hexpm/elixir:1.18-otp-27"}, wantErr: true},
		{name: "unknown stack errors", req: api.CreateRequest{Stack: "rails"}, wantErr: true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			out, err := normalizeStack(tt.req)
			if tt.wantErr {
				if err == nil {
					t.Fatalf("normalizeStack(%+v) = nil error, want error", tt.req)
				}
				return
			}
			if err != nil {
				t.Fatalf("normalizeStack(%+v) unexpected error: %v", tt.req, err)
			}
			if out.Stack != tt.want {
				t.Errorf("stack = %q, want %q", out.Stack, tt.want)
			}
		})
	}
}

func TestPhoenixContainerName(t *testing.T) {
	if got := phoenixContainerName("sv", "main"); got != "sv-main-phoenix" {
		t.Errorf("phoenixContainerName = %q, want %q", got, "sv-main-phoenix")
	}
}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd takumi-local-platform && go test ./internal/daemon/ -run "NormalizeStack|PhoenixContainer" -v`
Expected: FAIL (compile error: undefined symbols).

- [ ] **Step 3: Implement `stacks.go`**

```go
package daemon

import (
	"fmt"
	"strings"

	"github.com/CtrlCarlitos/takumi/internal/api"
)

// Stack role labels generalize container identity beyond the original
// -odoo name suffix: every managed app container carries its stack role,
// and List/Destroy/Ports key off labels instead of name shapes (W0-TK
// spec §Architecture). Odoo containers additionally keep the legacy
// "-odoo" suffix so external scripts see no change.
const (
	roleLabel   = "takumi.role"
	RoleOdoo    = "odoo"
	RolePhoenix = "phoenix"
)

// normalizeStack validates and defaults the stack discriminator. Rules:
// empty = odoo (back-compat contract, Global Constraints); phoenix
// requires an app_image pinned by digest — the same drift-risk refusal
// defaultOdooImage's comment documents for floating tags.
func normalizeStack(req api.CreateRequest) (api.CreateRequest, error) {
	switch req.Stack {
	case "":
		req.Stack = RoleOdoo
	case RoleOdoo, RolePhoenix:
	default:
		return req, fmt.Errorf("unknown stack %q (want odoo|phoenix)", req.Stack)
	}
	if req.Stack == RolePhoenix {
		if req.AppImage == "" {
			return req, fmt.Errorf("stack phoenix requires app_image")
		}
		if !strings.Contains(req.AppImage, "@sha256:") {
			return req, fmt.Errorf("app_image must be digest-pinned (name@sha256:...), got %q", req.AppImage)
		}
	}
	return req, nil
}

func phoenixContainerName(customer, worktree string) string {
	return customer + "-" + worktree + "-phoenix"
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `go test ./internal/daemon/ -v`
Expected: PASS (all new + existing tests).

- [ ] **Step 5: Commit**

```bash
git add internal/daemon/stacks.go internal/daemon/stacks_test.go
git commit -m "daemon: stack discriminator, phoenix naming, role labels"
```

### Task 3: Shared app-container helpers + `startPhoenix` + Create routing

**Files:**
- Modify: `takumi-local-platform/internal/daemon/worktrees.go` (extract helpers from `startOdoo`/`startPostgres`; wire `PrepareCreate`/`Create`)
- Modify: `takumi-local-platform/internal/daemon/stacks.go` (`startPhoenix` + helpers land here)
- Test: `takumi-local-platform/internal/daemon/stacks_test.go` (routing test appended)

**Interfaces:**
- Consumes: Task 2 symbols.
- Produces (binding signatures — extract, don't reinvent; derive bodies from the existing `startOdoo`/`startPostgres` implementations and their mount/path conventions):
  - `baseLabels(customer, worktree, role string) map[string]string` — the `takumi.managed/customer/worktree` set plus `takumi.role=role`.
  - `natPortSet(ports ...int) nat.PortSet`
  - `containerWorkdir(hostSourcePath string) string` — the in-container mount target, following `startOdoo`'s `/mnt/...` convention.
  - `fileLogConfig(hostLogFile string) container.LogConfig`
  - `startAppContainer(ctx context.Context, cfg container.Config, hc container.HostConfig, name, isolatedNet string) error` — the create-or-start idempotent core both stacks share (M7/R2-L5 contract).
  - `(c *Client) startPhoenix(ctx context.Context, name, dbName, isolatedNet, image, hostname, customer, worktree, hostSourcePath, hostLogFile string) error`
  - `PreparedCreate.role string`; `PreparedCreate.odooName` renamed `appName` (internal field, no API impact).

- [ ] **Step 1: Extract helpers with zero behavior change**

Move label-map construction, PortSet building, bind-mount derivation, and the create-or-start core out of `startOdoo`/`startPostgres` into the signatures above; `startOdoo` gains `roleLabel: RoleOdoo`. The pre-existing `worktrees_test.go` is the regression net — it must pass unmodified between every extraction step.

- [ ] **Step 2: Regression check**

Run: `go test ./internal/daemon/ -v`
Expected: PASS (failures = behavior change; fix before continuing).

- [ ] **Step 3: Implement `startPhoenix`**

```go
// startPhoenix runs the worktree's Phoenix app container: the worktree
// source bind-mounted at the container workdir, mix phx.server as the
// command, DATABASE_URL pointing at the sibling Postgres container on
// the isolated network, HTTP on 4000 (Caddy routes the worktree hostname
// to it). Same idempotent-retry contract as startOdoo via the shared
// startAppContainer core.
func (c *Client) startPhoenix(ctx context.Context, name, dbName, isolatedNet, image, hostname, customer, worktree, hostSourcePath, hostLogFile string) error {
	workdir := containerWorkdir(hostSourcePath)
	cfg := container.Config{
		Image:  image,
		Labels: baseLabels(customer, worktree, RolePhoenix),
		Env: []string{
			"MIX_ENV=dev",
			"PORT=4000",
			fmt.Sprintf("DATABASE_URL=ecto://odoo:odoo@%s/odoo", dbName),
			fmt.Sprintf("PHX_HOST=%s", hostname),
		},
		Cmd:          []string{"sh", "-c", "cd " + workdir + " && mix deps.get && mix ecto.setup && exec mix phx.server"},
		ExposedPorts: natPortSet(4000),
	}
	hc := container.HostConfig{Binds: []string{hostSourcePath + ":" + workdir}}
	if hostLogFile != "" {
		hc.LogConfig = fileLogConfig(hostLogFile)
	}
	return c.startAppContainer(ctx, cfg, hc, name, isolatedNet)
}
```

- [ ] **Step 4: Wire PrepareCreate/Create**

`PrepareCreate` first line: `req, err := normalizeStack(req)` (return on error) — before the collision check, same reason the OdooImage default runs first. Set `role: req.Stack`; set `appName` = `odooContainerName(...)` for odoo, `phoenixContainerName(...)` for phoenix. `Create` pulls `[]string{req.AppImage, defaultDBImage}` for phoenix (odoo path unchanged), and calls `startOdoo` XOR `startPhoenix` before the unchanged caddy NetworkConnect block (which now uses `prep.appName`).

- [ ] **Step 5: Routing test (pure — follows the repo's table-test style)**

```go
func TestPrepareCreateRoutesPhoenix(t *testing.T) {
	c := &Client{workspaceRootHost: "/home/dev/takumi-dream"} // PrepareCreate touches Docker only for the collision check; see note
	// NOTE: if the collision check runs against the real client in this
	// environment, gate this test behind the same mechanism collision_test.go
	// uses (read it first and mirror its approach exactly).
	prep, err := c.PrepareCreate(context.Background(), api.CreateRequest{
		Customer: "sv", Worktree: "main", Stack: "phoenix",
		AppImage: "hexpm/elixir:1.18-otp-27@sha256:abc",
		SourcePath: "customers/sv/main", AddonsPath: "client/odoo",
	}, false)
	if err != nil {
		t.Fatal(err)
	}
	if prep.role != RolePhoenix || prep.appName != "sv-main-phoenix" {
		t.Fatalf("role=%q appName=%q", prep.role, prep.appName)
	}
}
```

- [ ] **Step 6: Full suite + vet + commit**

Run: `go test ./... && go vet ./...`

```bash
git add internal/daemon/
git commit -m "daemon: route create by stack; shared app-container core; odoo unchanged"
```

### Task 4: `List` off role labels; `Destroy`/`Ports` per stack

**Files:**
- Modify: `takumi-local-platform/internal/daemon/worktrees.go` (`List`, `Destroy`, `Ports`, `volumeNames`)
- Test: extend `takumi-local-platform/internal/daemon/worktrees_test.go`

**Interfaces:**
- Produces:
  - `appContainerName(role, customer, worktree string) string` (`RoleOdoo` → legacy `-odoo` suffix, `RolePhoenix` → `-phoenix`) — the single name-resolution point `Destroy`/`Ports`/log-followers call.
  - `worktreeInfoFromContainers(containers []container.Summary) []api.WorktreeInfo` — `List`'s filtering/dedupe logic extracted as a pure function (this is what makes it testable without a Docker client, matching the repo's pure-function test style).
  - `volumeNames` per stack: phoenix worktrees have one data volume (db) — signature becomes `volumeNames(role, customer, worktree string) (dbData, appData string)` with `appData == ""` for phoenix.
  - `List` uses `worktreeInfoFromContainers` + sets `Stack` from the role label; `Destroy`/`Ports` resolve names via `appContainerName`.

- [ ] **Step 1: Write the failing tests** (append to `worktrees_test.go`; table style per the file's existing patterns):

```go
func TestAppContainerName(t *testing.T) {
	if got := appContainerName(RoleOdoo, "acme", "feature-x"); got != "acme-feature-x-odoo" {
		t.Errorf("odoo name = %q", got)
	}
	if got := appContainerName(RolePhoenix, "acme", "feature-x"); got != "acme-feature-x-phoenix" {
		t.Errorf("phoenix name = %q", got)
	}
}

func TestVolumeNamesPerStack(t *testing.T) {
	dbData, appData := volumeNames(RoleOdoo, "acme", "feature-x")
	if dbData != "acme-feature-x-db-data" || appData != "acme-feature-x-odoo-data" {
		t.Errorf("odoo volumes = %q, %q", dbData, appData)
	}
	dbData, appData = volumeNames(RolePhoenix, "acme", "feature-x")
	if dbData != "acme-feature-x-db-data" || appData != "" {
		t.Errorf("phoenix volumes = %q, %q (want db only)", dbData, appData)
	}
}

func TestWorktreeInfoFromContainers(t *testing.T) {
	mk := func(name string, labels map[string]string) container.Summary {
		return container.Summary{Names: []string{"/" + name}, Labels: labels}
	}
	base := map[string]string{managedLabel: "true", customerLabel: "sv", worktreeLabel: "main"}
	got := worktreeInfoFromContainers([]container.Summary{
		mk("sv-main-odoo", maps.Merge(base, map[string]string{roleLabel: RoleOdoo})), // dedupe partner
		mk("sv-main-db", map[string]string{managedLabel: "true"}),                   // no role → skipped
		mk("sv-feat-phoenix", map[string]string{managedLabel: "true", customerLabel: "sv", worktreeLabel: "feat", roleLabel: RolePhoenix}),
	})
	if len(got) != 2 {
		t.Fatalf("len = %d, want 2 (%+v)", len(got), got)
	}
	byKey := map[string]api.WorktreeInfo{}
	for _, w := range got {
		byKey[w.Customer+"/"+w.Worktree] = w
	}
	if byKey["sv/main"].Stack != RoleOdoo || byKey["sv/feat"].Stack != RolePhoenix {
		t.Errorf("stacks = %+v", byKey)
	}
}
```

(Use plain `for` loop map-merge instead of `maps.Merge` if that helper isn't imported in the test file yet — keep imports minimal per repo style.)

- [ ] **Step 2: Run to verify failure** — `go test ./internal/daemon/ -run "AppContainerName|VolumeNames|WorktreeInfo" -v`
- [ ] **Step 3: Implement** — extract `worktreeInfoFromContainers` (replacing `List`'s inline suffix-filter loop: skip containers without a `roleLabel`, dedupe by customer/worktree, `Stack` from the label, URL/Status as today); `appContainerName` switch; `volumeNames` per stack (its existing callers in `Destroy` pass the inspected container's role from the `takumi.role` label — `ContainerInspect` returns it in `info.Config.Labels`).
- [ ] **Step 4: Full suite green** — `go test ./...`
- [ ] **Step 5: Commit** — `git commit -m "daemon: role-label list/destroy/ports, per-stack volumes"`

### Task 5: CLI — `tk create --stack phoenix --app-image`

**Files:**
- Modify: `takumi-local-platform/cmd/takumi/main.go` (`createCmd`)
- Test: follow existing CLI test pattern in `cmd/takumi/` (if none exists, assert flag registration via a `createCmd()` construction test).

**Interfaces:**
- Produces: `tk create <customer> <worktree> [--image ODOO_DIGEST] [--stack odoo|phoenix] [--app-image APP_DIGEST]` — `--stack phoenix` requires `--app-image`; `tk create` output gains the stack line for phoenix worktrees.

- [ ] **Step 1: Failing test** — `createCmd()` registers flags `stack` and `app-image`, and the request builder errors when `stack=phoenix` and `app-image` is empty.
- [ ] **Step 2: Verify failure.** Run: `go test ./cmd/takumi/ -v`
- [ ] **Step 3: Implement** — flags + request fields; `--image` keeps its odoo-only meaning (help text updated to say so).
- [ ] **Step 4: Verify pass + full suite.** `go test ./...`
- [ ] **Step 5: Commit** — `git commit -m "tk: create --stack/--app-image flags"`

### Task 6: Pin the Phoenix base image + integration verification script

**Files:**
- Modify: `takumi-local-platform/internal/daemon/stacks.go` (fill `defaultPhoenixImage` if we want a default — decision: NO default in daemon; phoenix requires `app_image`. Instead:)
- Create: `tests/fixtures/sv-phoenix/README.md` + `tests/fixtures/sv-phoenix/verify.sh`
- Modify: `takumi-dream` root README "what works" note (one line, owner-approved wording).

**Interfaces:**
- Produces: `tests/fixtures/sv-phoenix/verify.sh` — the manual cross-platform checklist script the owner runs in their Linux/Mac/Windows-WSL testing phase.

- [ ] **Step 1: Write `verify.sh`**

```bash
#!/usr/bin/env bash
# Manual cross-platform verification for the phoenix stack (W0-TK).
# Run on each platform in the owner's testing phase. Requires: tk
# installed, TAKUMID_URL set, daemon up (tk setup done), WORKSPACE_ROOT
# exported to this repo's parent checkout.
set -euo pipefail
IMG="${PHOENIX_IMAGE:?set PHOENIX_IMAGE to a digest-pinned hexpm/elixir image}"
CUSTOMER=w0tk-verify WORKTREE=phoenix
SRC="$WORKSPACE_ROOT/customers/$CUSTOMER"
mkdir -p "$SRC/$WORKTREE" && cd "$SRC" && git init -q "$WORKTREE" 2>/dev/null || true
cd "$WORKTREE" && mkdir -p addons && touch addons/.gitkeep
cd "$WORKSPACE_ROOT"
tk create "$CUSTOMER" "$WORKTREE" --stack phoenix --app-image "$IMG"
URL="https://$CUSTOMER-$WORKTREE.localhost"
echo "worktree URL: $URL (expect the app's 4000 endpoint via Caddy; a plain elixir image serving nothing yet is also a PASS for routing if curl resolves and reaches the container)"
tk ports "$CUSTOMER" "$WORKTREE"   # expect app endpoint port 4000
tk destroy "$CUSTOMER" "$WORKTREE" # expect clean 204, no warnings
echo "PASS"
```

- [ ] **Step 2: Choose + record the digest-pinned image** (runtime discovery):

```bash
docker pull hexpm/elixir:1.18.4-otp-27
docker inspect --format '{{index .RepoDigests 0}}' hexpm/elixir:1.18.4-otp-27
```

Record the full `name@sha256:...` string in the fixture README (the SV repo pins its own copy in W0-SV Task 3).

- [ ] **Step 3: Run `verify.sh` on this WSL host** (owner runs it on Mac/Windows in their phase). Fix what it catches.
- [ ] **Step 4: Commit** — `git commit -m "tests: sv-phoenix cross-platform verification fixture"`

### Task 7: Wave record

- [ ] Commit any fixes; `go vet ./... && go test ./...` green; push branch; open PR to `takumi-dream` main with the W0-TK spec link in the description. **PR merges by owner decision only** (it rides the active testing phase).
- [ ] Record the merged SHA in the canon repo's `sv/HANDOVER.md` implementation-program section (W0-SV Task 9 consumes it as the pinned tk version).
