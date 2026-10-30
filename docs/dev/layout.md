# Repository layout

## Single application source

Root index.html is the sole application source and runtime artifact. It contains embedded CSS, geometry/constants, pure rules, active-play clock/controller, presentation, settings/session results, validators/codecs and browser/file adapters in the logical order below. These are named in-file sections, not separately deployed JavaScript/CSS assets. This map describes intended implementation locations; preparation does not create the application or tools.

| Logical components | Physical owner | Verification owner |
| --- | --- | --- |
| Shapes/colors/kick tables, board rules, piece source, landing and reducer | index.html: definitions and rules sections | tests/test_rules.py through common embedded-source extraction/Node VM fixture |
| Clock, lifecycle and ordered commands | index.html: clock/controller sections | tests/test_rules.py; tests/test_browser.py |
| Canvas, information, keyboard, optional panels/help | index.html: embedded CSS/HTML and view/input sections | tests/test_browser.py, including screenshots/Canvas and geometric assertions |
| Six setting definitions, session results and canonical export validator | index.html: shared data/validation sections | tests/test_persistence.py; browser integration |
| URL/cookie/history and file coordination | index.html: browser adapters/controller effects | tests/test_persistence.py with injected adapters; tests/test_browser.py |
| JSON Schema/codec and SQLite loader/codec | index.html: schema and file-format sections | tests/test_persistence.py; controlled CDN failure/round-trip browser fixtures |
| Extracted schema for consumers | schema/session.schema.json | tests/test_artifact.py verifies exact embedded/extracted schema equality |
| Release generation/version/checksums | tools/package.py and embedded version metadata in index.html | tests/test_artifact.py validates the actual generated HTML/manifest |

## Development and release paths

| Path | Ownership and constraints |
| --- | --- |
| tests/conftest.py | Shared source extraction, isolated JS execution, controlled HTTP server and Playwright fixtures; no second copy of production rules |
| tests/test_rules.py | Deterministic rule/clock cases, driven by pytest with JavaScript evaluated from the actual HTML in a Node VM |
| tests/test_persistence.py | Domain/source/file validators and codec cases, injected adapters and real SQLite parity as appropriate |
| tests/test_browser.py | Playwright Python API via pytest; actual source/packaged HTML and isolated Chromium/Firefox contexts |
| tests/test_artifact.py | Single-file packaging, external-dependency boundary, version, schema and checksum checks |
| tests/fixtures/ | Small valid/invalid board/session fixtures, including corrupt import cases; no credentials or personal data |
| requirements-dev.txt | Exact compatible pytest/Playwright/developer dependency pins, established at implementation; no application runtime dependency |
| tools/package.py | Standard-library packaging where practical; emits owned release artifacts without copying tests or credentials |
| dist/<version>/ | Generated tetris-v<version>.html, checksums and final-release schema; ignored, reproducible release outputs |
| .browser-runtime/ and .test-artifacts/ | Owned isolated binaries/profiles/downloads and screenshots/traces; ignored and never application assets |
| README.md and RELEASE-NOTES.md | Accurate usage, controls/settings/formats, tested setup commands, version and current complete release message |
| docs/dev/ | Canonical design/specification/planning, active preparation and scoped reviews; product tasks in TASKS.md |
| docs/dev/policies/ | Byte-identical copied project policies from SDD Manager 0.15.4; root AGENTS links these existing files |
| docs/dev/reports/phases/<phase>/ | Milestone <phase>.<milestone>.md and PHASE-REPORT.md, emitted only during implementation |
| docs/dev/reports/IMPLEMENTATION-REPORT.md | Final implementation result and unresolved/deferred finding aggregation |
| docs/ai-logs/ | Manual historical provenance scaffold; no automated transcript writing |

Before first test/tool execution, preserve existing ignore rules and exclude generated dist, runtime/cache and test artifacts. Runtime packages remain outside source/artifacts and use one absolute project-owned browser path consistently. Use actual pinned tools; do not put an unverified command into root guidance. Windows shell constraints apply on Windows hosts only. The Vite worker policy is retained as generic existing guidance; Vite/workers are not selected architecture.

## Dependency and navigation rules

All production component ownership resolves to a named section in index.html; tests import/extract that source rather than maintaining a parallel game. Only optional pinned CDN sql.js JavaScript is externally loaded at runtime. The generated release HTML must be identical to the verified application source except explicitly verified packaging/version handling. JSON Schema is embedded for runtime validation and separately extracted for consumers, not fetched by the app.

All developer tools are separate from downloadable page execution. Do not create an application src tree, server or worker solely to fit testing convenience. [PLAN](PLAN.md) owns increment boundaries and [DECOMPOSITION](DECOMPOSITION.md) owns interfaces. Root AGENTS owns current navigation; update commands only after actual verification.
