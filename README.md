# Single-page HTML Tetris

A keyboard Tetris game delivered as one HTML page with embedded application code. See the release candidate and verified delivery scope below.

See the [project brief](docs/dev/PROJECT.md), [preparation tasks](docs/dev/DOCS_TASKS.md) and [current handoff](docs/dev/HANDOFF.md).

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

## Development checks

Developer tools are separate from the downloaded page. Install the exact tools into a project-local directory with `python -m pip install --target .devdeps -r requirements-dev.txt`, then run `python tools/provision.py` followed by `python tools/check.py -q`. Node.js runs isolated tests against JavaScript extracted from the actual HTML; it is not needed by players. Provisioning uses only dedicated managed browsers and records rendering/input preflight evidence. Node.js 22 or newer is required for developer rule tests.

Browser checks use project-local managed Chromium shell revision 1248 (156.0.8078.4) and Firefox revision 1555 (157.0), matching Playwright 1.64.1. This execution reused compatible dedicated cached assets by copying them into .browser-runtime, not personal browser profiles. `tools/browser_probe.py` verifies two isolated rendering/input cycles per browser. On this Linux host Firefox default content processes failed with `/proc/self/uid_map: EPERM`; the process-local `MOZ_DISABLE_CONTENT_SANDBOX=1` override passed for trusted local tests. The untracked .test-artifacts/provisioning.json records whether the current environment needs that override. Re-evaluate on another host; no OS security policy is changed.

## Current release

Version 1.0.0. Validated versioned JSON/SQLite save and restore of session results and all six settings; complete-file validation precedes effects.

Run `python tools/package.py` to create dist/1.0.0/tetris.html and its checksum. Download/open the HTML directly for play; no Node.js, Python, package installation or local server is required for players. Static HTTP(S) hosting supports cookie persistence when that capability is delivered.

Controls: Left/Right move; Down soft-drops; Up/X rotate clockwise; Z turns counterclockwise; Escape pauses/resumes. Use the two labeled buttons to start/restart or pause/start. Space hard-drops; C or Shift holds once per piece. P spends one available penetrator bonus; four-line clears award a bonus up to three, and hold is disabled while penetrator is active. The settings panel controls ghost mode, hard drop, preview, both locking policies and hold. URL names are ghost, hardDrop, nextPreview, hardDropLock, lockPolicy and hold. Boolean URL/cookie spellings are on/off. Priority is valid URL, cookie, default; unsupported direct-file cookies are reported rather than promised. Game-over results persist only in the current page session; restart does not record an unfinished game. Save/Restore at the bottom of settings manually transfer JSON or SQLite. SQLite lazily loads the pinned single-file sql.js CDN library; JSON and play remain usable offline without it. Invalid restores leave results/settings/cookies/query unchanged. The supplied JSON Schema describes format version 1.

## Manual save and restore

Use Save at the bottom of Settings to download JSON or SQLite. Restore accepts either format by its content, replaces the current session top ten, and applies all six settings to the page, cookies and URL. Cancel leaves the session unchanged. Invalid or unsupported files show an error without changing these values. Results otherwise last only until the page reloads; restarting an unfinished game does not record it.

The [JSON Schema](schema/session.schema.json) describes version 1. Runtime validation additionally checks real calendar dates, exact safe integers, unique result IDs and duplicate JSON members. Both formats preserve each ID, score and canonical UTC completion timestamp. SQLite contains high_scores(id, score, timestamp) and settings(key, value), with six uniquely keyed setting rows, user_version=1 and application_id=1414812243. There is a 2 MiB import limit.

SQLite alone loads sql.js 1.15.0 from the pinned jsDelivr single-file build. Its integrity is verified with SHA-384; no separate WASM or worker download is needed. The first SQLite action needs network access. JSON and gameplay work without this dependency. Upstream [sql.js](https://github.com/sql-js/sql.js) is MIT licensed; SQLite is public domain. Automated browser integration uses the exact fetched library bytes with integrity/CORS checks; Python sqlite3 independently checks downloaded databases.

Developer setup installs managed browser assets if absent, probes two fresh contexts per engine, and verifies the pinned SQL asset. This host reused compatible managed browser assets; a clean browser download and native Windows execution were not exercised here. The Firefox override described above is limited to child processes and diagnosed namespace failures.

Stable latest downloads: [game HTML](https://github.com/pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1/releases/latest/download/tetris.html), [JSON Schema](https://github.com/pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1/releases/latest/download/session.schema.json), [checksums](https://github.com/pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1/releases/latest/download/SHA256SUMS). Version identity remains in the tag and embedded page metadata.

Published release: [v1.0.0](https://github.com/pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1/releases/tag/v1.0.0).
