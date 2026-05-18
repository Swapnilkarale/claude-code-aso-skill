# Branch Protection & Branching Strategy

This repository follows a strict **three-tier branching strategy**. Working
branches always flow into `dev`, and `dev` is the **only** branch allowed to
merge into `main`. The GitHub Actions workflows in this repo enforce parts of
this automatically; the remaining enforcement is done via GitHub branch
protection rules (configured once in the repository settings).

```
working branch  ── PR ──►  dev  ── PR ──►  main  ── release.yml ──►  GitHub Release
   (feature-*,                                     │
    fix-*, docs-*,                                 │
    refactor-*, chore-*)                           └── wiki-sync.yml ──► Wiki
```

## Working branches

Naming convention (enforced by `auto-pr-dev.yml`):

| Prefix       | Used for                       | Auto labels             |
|--------------|--------------------------------|-------------------------|
| `feature-*`  | New features / enhancements    | `feature`, `enhancement`|
| `fix-*`      | Bug fixes                      | `bug`, `fix`            |
| `docs-*`     | Documentation only             | `documentation`         |
| `refactor-*` | Refactors (no behavior change) | `refactoring`           |
| `chore-*`    | Maintenance, CI, tooling       | `chore`                 |

When linked to an issue, use `{prefix}-{issue-number}-{slug}`
(e.g. `feature-42-trending-keywords`). The `branch-lifecycle.yml` workflow
creates these branches automatically when an issue is labelled `ready`.

## Workflow map

| Workflow                  | Trigger                                          | Purpose                                |
|---------------------------|--------------------------------------------------|----------------------------------------|
| `auto-pr-dev.yml`         | Push to `feature-*`/`fix-*`/`docs-*`/`refactor-*`/`chore-*` | Auto-create PR into `dev`             |
| `auto-pr-main.yml`        | Manual (`workflow_dispatch`)                     | Create release PR from `dev` to `main` |
| `branch-lifecycle.yml`    | Issue labelled `ready`, PR sync/close            | Create branch / rebase / delete       |
| `python-quality.yml`      | PR + push to `dev`/`main` (python paths)         | Ruff lint/format + syntax matrix      |
| `security.yml`            | PR + push to `dev`/`main` + weekly cron          | CodeQL, TruffleHog, dependency audit  |
| `claude-code-review.yml`  | PR to `dev`/`main`                               | Size labels + AI review on dev PRs    |
| `claude-main-check.yml`   | PR to `main`                                     | Enforce `dev`-only source + final AI gate |
| `claude.yml`              | `@claude` mention                                | On-demand assistant                    |
| `wiki-sync.yml`           | Push to `main` (docs paths)                      | Mirror docs to GitHub Wiki             |
| `release.yml`             | Push to `main`                                   | Build skill ZIP + tag + GitHub Release |
| `labels.yml`              | Push to `main`/`dev` touching label manifest     | Sync `.github/labels.yml`              |

## Required branch protection rules

Configure these once in **Settings → Branches** (or via `gh api`). The CI status
check names below match the workflow job names exactly.

## One-time repository settings

Before the automation can work end-to-end, two repository-level toggles must
be flipped (these cannot be set from a workflow):

1. **Settings → Actions → General → Workflow permissions**
   - Set to **"Read and write permissions"**
   - Tick **"Allow GitHub Actions to create and approve pull requests"**

   Without this, `auto-pr-dev.yml` and `auto-pr-main.yml` will fail with
   `GitHub Actions is not permitted to create or approve pull requests`,
   even though the workflows themselves declare `pull-requests: write`.

2. **Settings → Actions → General → Fork pull request workflows from outside
   collaborators** — set to **"Require approval for first-time contributors"**
   (default is fine). Workflows that need a write token (auto-rebase,
   auto-PR) intentionally skip fork branches in `branch-lifecycle.yml`, so
   this is mainly belt-and-braces.

### `main` (protected, release branch)

- Require a pull request before merging
  - Required approvals: **1**
  - Dismiss stale approvals when new commits are pushed
  - Require review from Code Owners
- Require status checks to pass before merging
  - Require branches to be up to date before merging: **enabled**
  - Required status checks:
    - `Quality Summary`              (from `python-quality.yml`)
    - `Security Summary`             (from `security.yml`)
    - `Enforce dev to main rule`     (from `claude-main-check.yml`)
    - `Claude Release Validation`    (from `claude-main-check.yml`)
- Require conversation resolution before merging
- Require linear history
- Restrict who can push to matching branches (admins only)
- Do not allow bypassing the above settings
- Allow force pushes: **off**
- Allow deletions: **off**
- Restrict pushes that create files larger than 100 MB

### `dev` (protected, integration branch)

- Require a pull request before merging
  - Required approvals: **1**
  - Dismiss stale approvals when new commits are pushed
  - Require review from Code Owners
- Require status checks to pass before merging
  - Require branches to be up to date before merging: **enabled**
  - Required status checks:
    - `Quality Summary`        (from `python-quality.yml`)
    - `Security Summary`       (from `security.yml`)
    - `Claude Code Review`     (from `claude-code-review.yml`)
- Require conversation resolution before merging
- Require linear history
- Allow force pushes: **off**
- Allow deletions: **off**

### Working branches (`feature-*`, `fix-*`, `docs-*`, `refactor-*`, `chore-*`)

- Allow force pushes (with lease) so the auto-rebase step can keep the branch
  current with `dev`.
- No required reviews (review happens on the resulting PR to `dev`).
- Will be auto-deleted by `branch-lifecycle.yml` after the PR merges.

## One-shot setup with `gh`

The block below applies the recommended protection to `main` and `dev`. Adjust
the required check names if you rename a workflow.

```bash
# main
gh api -X PUT "repos/${OWNER}/${REPO}/branches/main/protection" \
  -H "Accept: application/vnd.github+json" \
  -f required_status_checks.strict=true \
  -F required_status_checks.contexts[]='Quality Summary' \
  -F required_status_checks.contexts[]='Security Summary' \
  -F required_status_checks.contexts[]='Enforce dev to main rule' \
  -F required_status_checks.contexts[]='Claude Release Validation' \
  -f enforce_admins=true \
  -F required_pull_request_reviews.required_approving_review_count=1 \
  -F required_pull_request_reviews.dismiss_stale_reviews=true \
  -F required_pull_request_reviews.require_code_owner_reviews=true \
  -f required_linear_history=true \
  -f allow_force_pushes=false \
  -f allow_deletions=false \
  -f restrictions=null

# dev
gh api -X PUT "repos/${OWNER}/${REPO}/branches/dev/protection" \
  -H "Accept: application/vnd.github+json" \
  -f required_status_checks.strict=true \
  -F required_status_checks.contexts[]='Quality Summary' \
  -F required_status_checks.contexts[]='Security Summary' \
  -F required_status_checks.contexts[]='Claude Code Review' \
  -f enforce_admins=false \
  -F required_pull_request_reviews.required_approving_review_count=1 \
  -F required_pull_request_reviews.dismiss_stale_reviews=true \
  -F required_pull_request_reviews.require_code_owner_reviews=true \
  -f required_linear_history=true \
  -f allow_force_pushes=false \
  -f allow_deletions=false \
  -f restrictions=null
```

## Release flow

1. Open a PR from a working branch to `dev` (auto-created on first push).
2. Quality + security + AI review run. Address feedback, get 1 approval, merge.
3. When ready to release, run **Actions → Auto-Create Release PR (dev to main)**
   and pick `patch`/`minor`/`major`.
4. The release PR is reviewed; `claude-main-check.yml` enforces that the PR
   came from `dev` and runs a minimal final gate.
5. On merge, `release.yml` reads the version from `pyproject.toml`, builds
   `app-store-optimization-<version>.zip`, tags `v<version>`, and creates the
   GitHub Release with notes from `CHANGELOG.md`.
6. `wiki-sync.yml` updates the wiki from the new `main`.

## Secrets and variables required

| Name                       | Type    | Used by                                                 |
|----------------------------|---------|---------------------------------------------------------|
| `CLAUDE_CODE_OAUTH_TOKEN`  | Secret  | `claude.yml`, `claude-code-review.yml`, `claude-main-check.yml` |
| `GITHUB_TOKEN` (built-in)  | Secret  | all workflows                                           |
| `PROJECT_VERSION`          | Var (optional) | `wiki-sync.yml` (defaults to `1.0.0`)            |
