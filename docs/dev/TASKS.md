# Implementation tasks

Derived from [SPEC](SPEC.md), [PLAN](PLAN.md), [layout](layout.md) and their adjacent conformance reviews. These are intended executable work units; every product checkbox is initially unchecked. Preparation completion does not select implementation or activate any phase.

## Execution obligations

Each task owns its implementation, meaningful checks, necessary user/developer documentation and fixes within the listed bounded outcome. Use pytest as the runner, with the actual embedded JavaScript exercised through shared Node VM fixtures and Playwright's Python API for actual-browser paths. Establish exact dependency pins and a working minimal harness with the first task; provision and exercise isolated matching Chromium headless shell and Firefox before the first dependent browser task. Follow the local browser/Playwright policies, preserve existing ignore rules and exclude generated runtime/test/dist paths. Do not add runtime application files to simplify the harness.

Tasks execute in phase/milestone order. A task's explicit predecessor references are necessary, not substitutes for phase activation, upstream review or publication gates. Each phase's first task additionally depends on its predecessor's completed/closed milestones, verified default integration and published release; phase 1 instead depends on accepted, package-reviewed and published-integrated preparation. Each phase requires eligible hosted projection before implementation. Each task commits its verified result, evidence and initial checkbox together, then pushes/readbacks before closure/progression.

No milestone has four delivery tasks, so each milestone's last delivery task folds whole-capability code review, relevant tests/regressions, blocker repair, the milestone report and HANDOFF into that same completion commit. It depends on all earlier tasks in its milestone. Dedicated phase-review tasks remain separate and count toward requested execution ranges. Their report is verification/integration readiness, not a claim of future merge or release publication. After a complete phase, the coordinator performs verified explicit main integration and the authorized release commit/tag/publication; those results gate the next phase. No phase is complete merely because its boxes are checked.

## Phase 1 — Classic baseline

- [x] Phase 1 — Classic baseline
    - [x] Milestone 1.1 — Classic rules
        - [x] T-001 — Implement board geometry and legal piece transitions
            Verified: `python tools/check.py -q` - 1 passed in 0.36s. Observed RED: valid empty-board T placement returned false; geometry implementation makes collision/bounds/translation scenarios pass. Pinned local pytest and source-extraction Node VM harness verified.
            Scope: index.html rule definitions; tests/test_rules.py. Depends on: accepted/reviewed preparation and eligible phase-1 activation.
            Contract/evidence: G1 bounds, spawn coordinates, four-cell shapes, legal move/rotate and collision rejection. Include relevant checks, fixes and changed usage documentation.
            Establish the pinned pytest/source-extraction harness and developer instructions as part of verifying these rules; do not install an application runtime dependency.
        - [x] T-002 — Implement gravity locking line clearing and scoring
            Verified: `python tools/check.py -q` - 2 passed in 0.59s. Observed RED for missing game scoring result; four-line clear, prior-level scoring, gravity failed-down lock and once-only blocked-spawn game over now pass.
            Scope: index.html reducer/clock; tests/test_rules.py. Depends on: T-001.
            Contract/evidence: G1 failed-attempt locking, simultaneous clears, score/level progression and game-over once. Include relevant checks, fixes and changed usage documentation.
        - [x] T-003 — Verify baseline game lifecycle invariants
            Verified: `python tools/check.py -q` - 3 passed in 0.66s. Observed RED: a paused clock advanced five rows; pause/resume now freezes elapsed time and restart resets score lines level and pose.
            Scope: index.html rule integration; tests/test_rules.py. Depends on: T-002.
            Contract/evidence: G1 injected random/clock seams, start/pause/resume/restart and stale-generation protection. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 1.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/1/1.1.md and HANDOFF with this task's initial completion.
    - [x] Milestone 1.2 — Playable interface
        - [x] T-004 — Build the centered board and information view
            Verified: `python tools/check.py -q` - 5 passed in 3.59s. Observed RED in both real browsers because the board was absent; centered Canvas and information now render with opaque pixels, correct initial statistics and exact two gameplay buttons. Chromium shell and Firefox local-environment override passed representative provisioning cycles.
            Scope: index.html embedded CSS/Canvas/HTML; tests/test_browser.py. Depends on: T-003.
            Contract/evidence: U1 board/info placement, visible information and Canvas occupied cells. Include relevant checks, fixes and changed usage documentation.
        - [x] T-005 — Connect keyboard and the two gameplay buttons
            Verified: `python tools/check.py -q` - 7 passed in 4.42s. Observed RED: Start left pages idle. Actual mouse/keyboard dispatch, movement, pause freeze, resume and restart now pass. Corrected the test to inspect status text content independently of CSS uppercase presentation; its behavioral state assertions remain intact.
            Scope: index.html controller/input/help; tests/test_browser.py. Depends on: T-004.
            Contract/evidence: G1/U1 keyboard-only moves, exact button order/labels, focus handling and pause. Include relevant checks, fixes and changed usage documentation.
        - [x] T-006 — Exercise playable classic scenarios in Chromium and Firefox
            Verified: `python tools/check.py -q` - 15 passed in 8.07s. Real Chromium/Firefox keyboard, lifecycle, game-over, opaque Canvas and 360/768/1440 centering scenarios pass. Screenshot review found clipped gameplay buttons; added failing bounds checks and fixed intrinsic grid minimums, preserving exact labels.
            Scope: tests/test_browser.py; project test configuration; index.html fixes. Depends on: T-005.
            Contract/evidence: A1/A9 actual HTML gameplay, Canvas, pause/restart, game over and responsive required panels. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 1.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/1/1.2.md and HANDOFF with this task's initial completion.
    - [x] Milestone 1.3 — Baseline distribution
        - [x] T-007 — Prepare single-file release packaging and instructions
            Verified: `python tools/check.py -q` - 16 passed in 7.46s. Observed RED for missing deployable artifact; reproducible packaging now emits an exact-source standalone HTML plus SHA256SUMS. Added candidate installation/control instructions, versioned notes and readable embedded CSS/section organization.
            Scope: tools/package.py; README.md; RELEASE-NOTES.md; index.html version. Depends on: T-006.
            Contract/evidence: D1 one embedded-code HTML, v0.1.0 metadata, direct-file/static hosting instructions and checksums. Include relevant checks, fixes and changed usage documentation.
        - [x] T-008 — Verify the deployable baseline artifact
            Verified: `python tools/check.py -q` - 18 passed in 11.01s. The actual packaged file runs from file:// in both managed browsers, starts/pauses with real controls and renders opaque Canvas without a server or developer runtime. Exact source bytes/checksum and scoped artifact structure pass.
            Scope: tests/test_artifact.py; tools/package.py; README.md. Depends on: T-007.
            Contract/evidence: A1/A9 packaged-file execution, no runtime toolchain and explicit browser evidence limits. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 1.3 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/1/1.3.md and HANDOFF with this task's initial completion.
    - [x] Milestone 1.4 — Phase review
        - [x] T-009 — Review test and report phase 1
            Verified: `python tools/check.py -q` - 18 passed in 8.43s. Full classic phase acceptance passes: 18 rule, real-browser, responsive and direct-file artifact tests. Reviewed all three milestone reports and their corrected findings; task persistence audit and explicit default integration/release publication follow this phase result.
            Depends on: all delivery tasks in phase 1, completion/closure of milestones 1.1, 1.2, 1.3, and their committed review evidence.
            Scope: cross-milestone code review, A1 and A9 for classic play; modern controls, settings, leaderboard and files remain deferred. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/1/PHASE-REPORT.md, HANDOFF, release v0.1.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 2 — Modern rules

- [ ] Phase 2 — Modern rules
    - [ ] Milestone 2.1 — Piece source and hold
        - [ ] T-010 — Add seven-bag source and next preview
            Scope: index.html piece source and preview; tests/test_rules.py. Depends on: T-009.
            Contract/evidence: G2 deterministic bag permutations, preview order and queue retention. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-011 — Add hold and once-per-turn lifecycle
            Scope: index.html reducer/input/hold view; tests/test_rules.py; tests/test_browser.py. Depends on: T-010.
            Contract/evidence: G2 empty/swap hold, spawn reset, blocked hold game over and turn limits. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 2.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/2/2.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 2.2 — Kicks and landing
        - [ ] T-012 — Add orientation-specific wall kicks
            Scope: index.html rotation tables/rules; tests/test_rules.py. Depends on: T-011.
            Contract/evidence: G2 all transition tables, first-valid offset and unchanged failure. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-013 — Share landing between ghost and drop commands
            Scope: index.html landing/view; tests/test_rules.py; tests/test_browser.py. Depends on: T-012.
            Contract/evidence: G2 normal contiguous landing and visible ghost projection. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-014 — Add keyboard hard drop and scoring
            Scope: index.html input/reducer; tests/test_rules.py; tests/test_browser.py. Depends on: T-013.
            Contract/evidence: G2 Space dispatch, drop distance scoring and ghost/drop parity. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 2.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/2/2.2.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 2.3 — Grounded timing and distribution
        - [ ] T-015 — Implement full-interval and immediate-drop timing policies
            Scope: index.html active-play clock/reducer; tests/test_rules.py. Depends on: T-014.
            Contract/evidence: G2 retained grounding deadline, lift reset, pause, stale timers and terminal-drop policy. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-016 — Package and verify the modern-rule release
            Scope: tools/package.py; tests/test_browser.py; README.md; RELEASE-NOTES.md; index.html version. Depends on: T-015.
            Contract/evidence: A2 integrated rules/default interval timing, v0.2.0 artifact and baseline regression evidence. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 2.3 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/2/2.3.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 2.4 — Phase review
        - [ ] T-017 — Review test and report phase 2
            Depends on: all delivery tasks in phase 2, completion/closure of milestones 2.1, 2.2, 2.3, and their committed review evidence.
            Scope: cross-milestone code review, A2 and prior baseline regressions; configurable settings/dynamic ghost/penetrator remain deferred. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/2/PHASE-REPORT.md, HANDOFF, release v0.2.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 3 — Conditional ghost

- [ ] Phase 3 — Conditional ghost
    - [ ] Milestone 3.1 — Dynamic ghost delivery
        - [ ] T-018 — Integrate midline-based ghost visibility
            Scope: index.html ghost predicate/view; tests/test_rules.py; tests/test_browser.py. Depends on: T-017.
            Contract/evidence: G3 every projected cell below row 10, straddling hidden and automatic redraw; use dynamic as this release mode. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-019 — Document package and verify conditional ghost
            Scope: README.md; RELEASE-NOTES.md; tools/package.py; tests/test_browser.py; index.html version. Depends on: T-018.
            Contract/evidence: A3 upper/lower/straddling fixtures, pose/board recalculation and v0.3.0 artifact. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 3.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/3/3.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 3.2 — Phase review
        - [ ] T-020 — Review test and report phase 3
            Depends on: all delivery tasks in phase 3, completion/closure of milestones 3.1, and their committed review evidence.
            Scope: cross-milestone code review, A3 and ghost/drop parity; no configuration UI or new persistence. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/3/PHASE-REPORT.md, HANDOFF, release v0.3.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 4 — Penetrator mode

- [ ] Phase 4 — Penetrator mode
    - [ ] Milestone 4.1 — Penetrator gameplay
        - [ ] T-021 — Add bonus accounting and activation state
            Scope: index.html reducer; tests/test_rules.py. Depends on: T-020.
            Contract/evidence: G4 four-line earn, cap three, spend once and restart reset. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-022 — Implement safe penetrator transit and landing
            Scope: index.html board/landing/rotation; tests/test_rules.py. Depends on: T-021.
            Contract/evidence: G4 occupancy transit, valid-future-landing invariant and overlap-safe lock. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-023 — Connect penetrator hotkey hold restriction and visuals
            Scope: index.html input/view/info; tests/test_browser.py; tests/test_rules.py. Depends on: T-022.
            Contract/evidence: G4 P activation, white active/locked piece, bonus symbols, disabled hold and next regular piece. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 4.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/4/4.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 4.2 — Penetrator integration and distribution
        - [ ] T-024 — Unify penetrator ghost drop and grounding behavior
            Scope: index.html landing/clock; tests/test_rules.py; tests/test_browser.py. Depends on: T-023.
            Contract/evidence: A4 lowest legal destination across occupied bands, projection/drop identity and both lock modes. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-025 — Package and verify penetrator delivery
            Scope: README.md; RELEASE-NOTES.md; tools/package.py; tests/test_browser.py; index.html version. Depends on: T-024.
            Contract/evidence: A4 integrated fixtures, preserved fixed cells, bonus display and v0.4.0 artifact. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 4.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/4/4.2.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 4.3 — Phase review
        - [ ] T-026 — Review test and report phase 4
            Depends on: all delivery tasks in phase 4, completion/closure of milestones 4.1, 4.2, and their committed review evidence.
            Scope: cross-milestone code review, A4 and lock/hold/ghost regressions; settings and persistence remain deferred. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/4/PHASE-REPORT.md, HANDOFF, release v0.4.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 5 — Session configuration

- [ ] Phase 5 — Session configuration
    - [ ] Milestone 5.1 — Live configuration
        - [ ] T-027 — Define the six canonical setting domains and defaults
            Scope: index.html config service; tests/test_persistence.py. Depends on: T-026.
            Contract/evidence: C1 strict types/enums and a complete normalized settings object. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-028 — Build the six labeled settings controls
            Scope: index.html settings HTML/view; tests/test_browser.py. Depends on: T-027.
            Contract/evidence: C1 all six choices, defaults and disabled-capability display without extra gameplay actions. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-029 — Apply settings through one live controller update
            Scope: index.html controller/clock/view; tests/test_rules.py; tests/test_browser.py. Depends on: T-028.
            Contract/evidence: C1 interval-policy changes, unchanged deadlines, hardDrop/preview/hold/ghost effects and penetrator restriction. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 5.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/5/5.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 5.2 — Session-only delivery
        - [ ] T-030 — Integrate panel visibility and reload isolation
            Scope: index.html panel controls; tests/test_browser.py. Depends on: T-029.
            Contract/evidence: U1 settings/help toggles preserve board center; C1 page reload resets defaults with no persistence side effects. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-031 — Package and verify session-only settings
            Scope: README.md; RELEASE-NOTES.md; tools/package.py; tests/test_browser.py; index.html version. Depends on: T-030.
            Contract/evidence: A5 session-only HTTP and file behavior, default show ghost and v0.5.0 artifact. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 5.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/5/5.2.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 5.3 — Phase review
        - [ ] T-032 — Review test and report phase 5
            Depends on: all delivery tasks in phase 5, completion/closure of milestones 5.1, 5.2, and their committed review evidence.
            Scope: cross-milestone code review, A5 and UI setting/ghost/penetrator interactions; no cookie/query reads or writes yet. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/5/PHASE-REPORT.md, HANDOFF, release v0.5.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 6 — URL and cookie configuration

- [ ] Phase 6 — URL and cookie configuration
    - [ ] Milestone 6.1 — Configuration persistence
        - [ ] T-033 — Resolve independent URL cookie and default sources
            Scope: index.html browser/config adapters; tests/test_persistence.py. Depends on: T-032.
            Contract/evidence: C2 mixed-source precedence, invalid values, first duplicate, omitted parameter and unknown-key retention. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-034 — Write explicit URL values and changed cookies
            Scope: index.html cookie adapter; tests/test_persistence.py; tests/test_browser.py. Depends on: T-033.
            Contract/evidence: C2 explicit-default writes, omission retention, correct attributes and unavailable-cookie warnings. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-035 — Update queries on setting changes without reload
            Scope: index.html history adapter; tests/test_persistence.py; tests/test_browser.py. Depends on: T-034.
            Contract/evidence: C2 one changed parameter, unrelated/hash retention and history failure isolation. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 6.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/6/6.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 6.2 — Reload delivery
        - [ ] T-036 — Verify reload and browser-failure integration
            Scope: tests/test_browser.py; tests/test_persistence.py; index.html fixes. Depends on: T-035.
            Contract/evidence: A6 reload/reopen fixture matrix and file-mode graceful limits. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-037 — Package and document automatic settings persistence
            Scope: README.md; RELEASE-NOTES.md; tools/package.py; index.html version. Depends on: T-036.
            Contract/evidence: A6 cookie/query usage, supported HTTP mode, direct-file limitations and v0.6.0 artifact. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 6.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/6/6.2.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 6.3 — Phase review
        - [ ] T-038 — Review test and report phase 6
            Depends on: all delivery tasks in phase 6, completion/closure of milestones 6.1, 6.2, and their committed review evidence.
            Scope: cross-milestone code review, A6 and C1 regressions; leaderboard still not persisted. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/6/PHASE-REPORT.md, HANDOFF, release v0.6.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 7 — Session leaderboard

- [ ] Phase 7 — Session leaderboard
    - [ ] Milestone 7.1 — Top-ten session delivery
        - [ ] T-039 — Collect and rank completed game records
            Scope: index.html session-results/controller; tests/test_persistence.py. Depends on: T-038.
            Contract/evidence: L1 stable IDs/UTC, tie ordering, duplicate-event exclusion, abandoned-game omission and top-ten bound. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-040 — Present the leaderboard and visibility toggle
            Scope: index.html leaderboard/info layout; tests/test_browser.py. Depends on: T-039.
            Contract/evidence: L1/U1 left-of-info panel, empty state, hide/show centering and game-over refresh. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-041 — Verify session lifetime and package leaderboard release
            Scope: README.md; RELEASE-NOTES.md; tests/test_browser.py; tools/package.py; index.html version. Depends on: T-040.
            Contract/evidence: A7 restart retention, reload empty history despite saved settings, v0.7.0 artifact. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 7.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/7/7.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 7.2 — Phase review
        - [ ] T-042 — Review test and report phase 7
            Depends on: all delivery tasks in phase 7, completion/closure of milestones 7.1, and their committed review evidence.
            Scope: cross-milestone code review, A7 plus leaderboard panel placement; no automatic or file history persistence. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/7/PHASE-REPORT.md, HANDOFF, release v0.7.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.

## Phase 8 — Manual file persistence

- [ ] Phase 8 — Manual file persistence
    - [ ] Milestone 8.1 — Validated JSON transfer
        - [ ] T-043 — Define the export schema and complete canonical validator
            Scope: index.html embedded schema/validator; tests/test_persistence.py; schema/session.schema.json. Depends on: T-042.
            Contract/evidence: F1/L1/C1 complete content, bounds, duplicate keys/IDs, safe score, timestamps and version. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-044 — Add JSON snapshot downloads and Save controls
            Scope: index.html JSON codec/settings file controls; tests/test_browser.py; tests/test_persistence.py. Depends on: T-043.
            Contract/evidence: F1 one JSON snapshot file, correct current top ten/settings, hidden-settings button containment. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-045 — Restore JSON through staged atomic replacement
            Scope: index.html file coordinator/controller; tests/test_persistence.py; tests/test_browser.py. Depends on: T-044.
            Contract/evidence: F1 invalid content unchanged across all surfaces; valid replacement, cookies/query, cancellation and stale-read protection. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 8.1 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/8/8.1.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 8.2 — SQLite transfer
        - [ ] T-046 — Integrate a pinned lazy single-file sql.js runtime
            Scope: index.html dependency loader; tests/test_persistence.py; README.md. Depends on: T-045.
            Contract/evidence: F2 one CDN JavaScript dependency, bounded load/init, retry and JSON/game isolation. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-047 — Export the versioned SQLite format
            Scope: index.html SQLite encoder; tests/test_persistence.py. Depends on: T-046.
            Contract/evidence: F2 exact high_scores/settings tables, metadata, bound writes and stable values. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-048 — Validate and restore SQLite through the common candidate path
            Scope: index.html SQLite reader/validator; tests/test_persistence.py; tests/test_browser.py. Depends on: T-047.
            Contract/evidence: F2 integrity/schema/storage types/all rows/version, complete validation and cleanup before one common commit. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 8.2 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/8/8.2.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 8.3 — Interoperability and distribution
        - [ ] T-049 — Verify cross-format parity and restore failure isolation
            Scope: tests/test_persistence.py; tests/test_browser.py; index.html fixes. Depends on: T-048.
            Contract/evidence: A8 JSON-to-SQLite and reverse, invalid-field matrix, runtime failures and unchanged results/settings/cookies/query. Include relevant checks, fixes and changed usage documentation.
        - [ ] T-050 — Package the complete single-page release and schema
            Scope: tools/package.py; schema/session.schema.json; README.md; RELEASE-NOTES.md; index.html version. Depends on: T-049.
            Contract/evidence: A9 v1.0.0 HTML, embedded/extracted-schema equality, checksum/install instructions and full-scope artifact checks. Include relevant checks, fixes and changed usage documentation.
            Milestone exit: depends on all 8.3 delivery tasks; whole-capability code review, focused/regression checks, blocker repair, committed report docs/dev/reports/phases/8/8.3.md and HANDOFF with this task's initial completion.
    - [ ] Milestone 8.4 — Phase review
        - [ ] T-051 — Review test and report phase 8
            Depends on: all delivery tasks in phase 8, completion/closure of milestones 8.1, 8.2, 8.3, and their committed review evidence.
            Scope: cross-milestone code review, A8 and full A1-A9 regression/packaging; JSON/SQLite parity and all six settings. Review actual source/packaged HTML, applicable rule/adapter/browser cases and milestone findings; repair blockers and retain excluded/unavailable checks accurately.
            Evidence: docs/dev/reports/phases/8/PHASE-REPORT.md, HANDOFF, release v1.0.0 readiness/source/artifact identity and TODO disposition. Do not claim integration or provider publication before readback.
            Final result: also produce docs/dev/reports/IMPLEMENTATION-REPORT.md aggregating full-scope results and every unresolved/deferred finding, provenance, options and owner.

## Coverage and stopping boundaries

G1/U1/D1 baseline belongs to phase 1; G2 to phase 2; dynamic G3 to phase 3; G4 to phase 4; C1 to phase 5; C2 to phase 6; L1 to phase 7; F1/F2/final D1 to phase 8. Every task points to its contract group and expected evidence, with exact behavior in SPEC rather than duplicated task definitions. One current TASKS list owns all product IDs.

Milestone boundaries permit a requested pause with their reports; partial phases remain unmerged. A next-N or phase request authorizes only that range. Full-project implementation is not selected by this document. Version changes, packaged HTML/schema, use instructions and release evidence remain necessary at the planned delivery boundaries.
