# Agent instructions

## Specification-driven development

This project uses the SDD Manager plugin for specification-driven development. If not already in the context, load `PLUGIN.md` from installed location or from `.agents/plugins/sdd-manager/PLUGIN.md` and the coordinator skill entry it references. If neither source is available, report the missing plugin before dependent workflow work.

**Follow the applicable SDD Manager workflows, including human checkpoints, Git publication and integration, and the tracking policy below.**

## Initialization

Execute the [skill and plugin discovery protocol](SKILL_DISCOVERY_PROTOCOL.md).

## Windows shell

On **Windows execution hosts only**, follow [WINDOWS_SHELL_POLICY.md](docs/dev/policies/WINDOWS_SHELL_POLICY.md): CMD syntax, unavailable PowerShell/pwsh, temporary files for script text and shell operations, and the documented tool probe/recovery. This repository policy is independent of the plugin.

## Browser development

When developing or testing browser-based applications or browser extensions, follow [BROWSER_DEV_POLICY.md](docs/dev/policies/BROWSER_DEV_POLICY.md). Prioritize Chromium and include Firefox by default; project documents may specify other choices. Use dedicated, isolated environments.

## Environment diagnostics

When Playwright is selected, follow [Playwright environment guidance](docs/dev/policies/playwright.md) before dependent setup and execution, and when provisioning or browser runtime blocks required checks.

When a Vite-served module worker fails to start, especially from a linked Windows checkout or with an HTML entry response, follow [Vite worker-loading diagnostics](docs/dev/policies/vite-worker-loading.md). Diagnose the loading stage before applying a workaround; this guidance does not apply to every SQLite or worker failure.

## Workflow continuity

For continuation, read `docs/dev/HANDOFF.md` and use `sdd-manage`'s continuity subworkflow to reconstruct later work from current development records and Git. The handoff describes a checkpoint, not necessarily the branch tip. At startup, inspect unfinished workflow branches against their recorded parents and request the continuation branch unless already selected. Preserve the recovered scope, approvals and stopping boundary.

## Human checkpoints

Present each necessary new development document with concise substantive analysis and pause for acceptance before dependent work. Honor the user's requested implementation range and stop when it is complete.

The user may explicitly preapprove future checkpoints at any time. Retain the scope and conditions of that decision, including after interruption; do not repeat a covered approval request. Preapproval does not waive QC, resolve blockers or expand the authorized implementation range.

## Commits and publication

Keep each task's verified result, required evidence and completion checkbox in the same commit. Push every owned commit and verify remote containment before further work or another commit, unless the user explicitly directs local-only or deferred publication.

Use SDD Manager's integration procedure at the authorized complete boundary.

## GitHub tracking

Enable and maintain GitHub tracking for documentation preparation and implementation **by default**. The user may disable tracking, select local-only work or choose another supported backend. Preserve an established choice through interruptions and access failures; copying this template does not reset it.

Follow `sdd-manage`'s preparation and phase-activation workflows for required tracking readiness and lifecycle updates. Reconcile uncertain effects before retrying and report unmet prerequisites before dependent work.

## Project guidance

Maintain project-specific navigation and validated setup/check commands here as they become established. Do not invent commands, paths, requirements or completion claims.

## Application and development navigation

The application delivery target is one root index.html with embedded application code. See [PROJECT](docs/dev/PROJECT.md), [ARCHITECTURE](docs/dev/ARCHITECTURE.md), [DECOMPOSITION](docs/dev/DECOMPOSITION.md), [SPEC](docs/dev/SPEC.md), [PLAN](docs/dev/PLAN.md) and [layout](docs/dev/layout.md). Preparation progress remains in docs/dev/DOCS_TASKS.md and its control/evidence in docs/dev/DOCS_PREPARATION.md. Once created, docs/dev/TASKS.md owns executable product work.

The selected development verification runner is pytest with Playwright's Python API; pure JavaScript rules can be exercised through an isolated Node VM driven by pytest. These are development facilities, not application runtime requirements. Exact dependency pins and working setup/check commands must be established and documented during implementation. No browser installation is required for document-only preparation. Preserve Chromium headless-shell and Firefox coverage under the policies above; unavailable native/full-browser evidence is reported separately.
