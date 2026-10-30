# Single-page HTML Tetris

A keyboard Tetris game delivered as one HTML page with embedded application code. See the release candidate and verified delivery scope below.

See the [project brief](docs/dev/PROJECT.md), [preparation tasks](docs/dev/DOCS_TASKS.md) and [current handoff](docs/dev/HANDOFF.md).

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

## Development checks

Developer tools are separate from the downloaded page. Install the exact tools into a project-local directory with `python -m pip install --target .devdeps -r requirements-dev.txt`, then run `python tools/check.py -q`. Node.js runs isolated tests against JavaScript extracted from the actual HTML; it is not needed by players. Browser setup is documented when its execution path is verified.

Browser checks use project-local managed Chromium shell revision 1248 (156.0.8078.4) and Firefox revision 1555 (157.0), matching Playwright 1.64.1. This execution reused compatible dedicated cached assets by copying them into .browser-runtime, not personal browser profiles. `tools/browser_probe.py` verifies two isolated rendering/input cycles per browser. On this Linux host Firefox default content processes failed with `/proc/self/uid_map: EPERM`; the process-local `MOZ_DISABLE_CONTENT_SANDBOX=1` override passed for trusted local tests. The untracked .test-artifacts/provisioning.json records whether the current environment needs that override. Re-evaluate on another host; no OS security policy is changed.

## Release candidate

Version 0.5.0. All six live game settings with explicit session-only lifetime and independent panel toggles.

Run `python tools/package.py` to create dist/0.5.0/tetris-v0.5.0.html and its checksum. Download/open the HTML directly for play; no Node.js, Python, package installation or local server is required for players. Static HTTP(S) hosting supports cookie persistence when that capability is delivered.

Controls: Left/Right move; Down soft-drops; Up/X rotate clockwise; Z turns counterclockwise; Escape pauses/resumes. Use the two labeled buttons to start/restart or pause/start. Space hard-drops; C or Shift holds once per piece. P spends one available penetrator bonus; four-line clears award a bonus up to three, and hold is disabled while penetrator is active. The settings panel controls ghost mode, hard drop, preview, both locking policies and hold. Settings reset on reload in this session-only release.
