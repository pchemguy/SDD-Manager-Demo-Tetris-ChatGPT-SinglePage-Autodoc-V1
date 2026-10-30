# Single-page HTML Tetris

A browser Tetris project intended for delivery as one HTML file with embedded application HTML, CSS and JavaScript. Development is in preparation; no playable release is available yet.

See the [project brief](docs/dev/PROJECT.md), [preparation tasks](docs/dev/DOCS_TASKS.md) and [current handoff](docs/dev/HANDOFF.md).

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

## Development checks

Developer tools are separate from the downloaded page. Install the exact tools into a project-local directory with `python -m pip install --target .devdeps -r requirements-dev.txt`, then run `python tools/check.py -q`. Node.js runs isolated tests against JavaScript extracted from the actual HTML; it is not needed by players. Browser setup is documented when its execution path is verified.

Browser checks use project-local managed Chromium shell revision 1248 (156.0.8078.4) and Firefox revision 1555 (157.0), matching Playwright 1.64.1. This execution reused compatible dedicated cached assets by copying them into .browser-runtime, not personal browser profiles. `tools/browser_probe.py` verifies two isolated rendering/input cycles per browser. On this Linux host Firefox default content processes failed with `/proc/self/uid_map: EPERM`; the process-local `MOZ_DISABLE_CONTENT_SANDBOX=1` override passed for trusted local tests. The untracked .test-artifacts/provisioning.json records whether the current environment needs that override. Re-evaluate on another host; no OS security policy is changed.
