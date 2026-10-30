# Delivery plan

## Strategy

Deliver eight useful browser-game increments, each preserving its predecessor. [SPEC](SPEC.md) owns complete behavior and [SPEC review](SPEC-REVIEW-REPORT.md) establishes current design conformance. Release v0.1.0 is playable classic Tetris rather than infrastructure or the complete target. Independent enhancements stay in later phases. Versions v0.2.0 through v0.7.0 add capabilities; v1.0.0 covers the full requested scope.

Every phase depends on its predecessor's verified integration and release. Milestones execute in listed order. Milestone exits require whole-capability code review, applicable checks, blocker repair, a committed milestone report and HANDOFF. TASKS folds these into the final delivery task unless the standard standalone-review threshold applies. Each phase ends with one dedicated review milestone containing exactly one code-review/testing/report task. It starts only after all delivery milestones complete and their enabled hosted closures are verified.

## Phase and milestone map

### Phase 1 — Classic baseline

Outcome: release v0.1.0, covering G1, U1 and D1 baseline.

| Milestone | Outcome and exit |
| --- | --- |
| 1.1 — Classic rules | G1 bounds, spawn coordinates, four-cell shapes, legal move/rotate and collision rejection; G1 failed-attempt locking, simultaneous clears, score/level progression and game-over once; G1 injected random/clock seams, start/pause/resume/restart and stale-generation protection; integrated capability review/check/report before closure |
| 1.2 — Playable interface | U1 board/info placement, visible information and Canvas occupied cells; G1/U1 keyboard-only moves, exact button order/labels, focus handling and pause; A1/A9 actual HTML gameplay, Canvas, pause/restart, game over and responsive required panels; integrated capability review/check/report before closure |
| 1.3 — Baseline distribution | D1 one embedded-code HTML, v0.1.0 metadata, direct-file/static hosting instructions and checksums; A1/A9 packaged-file execution, no runtime toolchain and explicit browser evidence limits; integrated capability review/check/report before closure |
| 1.4 — Phase review | One cross-milestone code review/testing/report task; verify A1 and A9 for classic play; modern controls, settings, leaderboard and files remain deferred. |

Phase exit: A1 and A9 for classic play; modern controls, settings, leaderboard and files remain deferred. Publish release v0.1.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 2 — Modern rules

Outcome: release v0.2.0, covering G2 plus always-show ghost from G3.

| Milestone | Outcome and exit |
| --- | --- |
| 2.1 — Piece source and hold | G2 deterministic bag permutations, preview order and queue retention; G2 empty/swap hold, spawn reset, blocked hold game over and turn limits; integrated capability review/check/report before closure |
| 2.2 — Kicks and landing | G2 all transition tables, first-valid offset and unchanged failure; G2 normal contiguous landing and visible ghost projection; G2 Space dispatch, drop distance scoring and ghost/drop parity; integrated capability review/check/report before closure |
| 2.3 — Grounded timing and distribution | G2 retained grounding deadline, lift reset, pause, stale timers and terminal-drop policy; A2 integrated rules/default interval timing, v0.2.0 artifact and baseline regression evidence; integrated capability review/check/report before closure |
| 2.4 — Phase review | One cross-milestone code review/testing/report task; verify A2 and prior baseline regressions; configurable settings/dynamic ghost/penetrator remain deferred. |

Phase exit: A2 and prior baseline regressions; configurable settings/dynamic ghost/penetrator remain deferred. Publish release v0.2.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 3 — Conditional ghost

Outcome: release v0.3.0, covering G3 dynamic visibility.

| Milestone | Outcome and exit |
| --- | --- |
| 3.1 — Dynamic ghost delivery | G3 every projected cell below row 10, straddling hidden and automatic redraw; use dynamic as this release mode; A3 upper/lower/straddling fixtures, pose/board recalculation and v0.3.0 artifact; integrated capability review/check/report before closure |
| 3.2 — Phase review | One cross-milestone code review/testing/report task; verify A3 and ghost/drop parity; no configuration UI or new persistence. |

Phase exit: A3 and ghost/drop parity; no configuration UI or new persistence. Publish release v0.3.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 4 — Penetrator mode

Outcome: release v0.4.0, covering G4.

| Milestone | Outcome and exit |
| --- | --- |
| 4.1 — Penetrator gameplay | G4 four-line earn, cap three, spend once and restart reset; G4 occupancy transit, valid-future-landing invariant and overlap-safe lock; G4 P activation, white active/locked piece, bonus symbols, disabled hold and next regular piece; integrated capability review/check/report before closure |
| 4.2 — Penetrator integration and distribution | A4 lowest legal destination across occupied bands, projection/drop identity and both lock modes; A4 integrated fixtures, preserved fixed cells, bonus display and v0.4.0 artifact; integrated capability review/check/report before closure |
| 4.3 — Phase review | One cross-milestone code review/testing/report task; verify A4 and lock/hold/ghost regressions; settings and persistence remain deferred. |

Phase exit: A4 and lock/hold/ghost regressions; settings and persistence remain deferred. Publish release v0.4.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 5 — Session configuration

Outcome: release v0.5.0, covering C1.

| Milestone | Outcome and exit |
| --- | --- |
| 5.1 — Live configuration | C1 strict types/enums and a complete normalized settings object; C1 all six choices, defaults and disabled-capability display without extra gameplay actions; C1 interval-policy changes, unchanged deadlines, hardDrop/preview/hold/ghost effects and penetrator restriction; integrated capability review/check/report before closure |
| 5.2 — Session-only delivery | U1 settings/help toggles preserve board center; C1 page reload resets defaults with no persistence side effects; A5 session-only HTTP and file behavior, default show ghost and v0.5.0 artifact; integrated capability review/check/report before closure |
| 5.3 — Phase review | One cross-milestone code review/testing/report task; verify A5 and UI setting/ghost/penetrator interactions; no cookie/query reads or writes yet. |

Phase exit: A5 and UI setting/ghost/penetrator interactions; no cookie/query reads or writes yet. Publish release v0.5.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 6 — URL and cookie configuration

Outcome: release v0.6.0, covering C2.

| Milestone | Outcome and exit |
| --- | --- |
| 6.1 — Configuration persistence | C2 mixed-source precedence, invalid values, first duplicate, omitted parameter and unknown-key retention; C2 explicit-default writes, omission retention, correct attributes and unavailable-cookie warnings; C2 one changed parameter, unrelated/hash retention and history failure isolation; integrated capability review/check/report before closure |
| 6.2 — Reload delivery | A6 reload/reopen fixture matrix and file-mode graceful limits; A6 cookie/query usage, supported HTTP mode, direct-file limitations and v0.6.0 artifact; integrated capability review/check/report before closure |
| 6.3 — Phase review | One cross-milestone code review/testing/report task; verify A6 and C1 regressions; leaderboard still not persisted. |

Phase exit: A6 and C1 regressions; leaderboard still not persisted. Publish release v0.6.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 7 — Session leaderboard

Outcome: release v0.7.0, covering L1.

| Milestone | Outcome and exit |
| --- | --- |
| 7.1 — Top-ten session delivery | L1 stable IDs/UTC, tie ordering, duplicate-event exclusion, abandoned-game omission and top-ten bound; L1/U1 left-of-info panel, empty state, hide/show centering and game-over refresh; A7 restart retention, reload empty history despite saved settings, v0.7.0 artifact; integrated capability review/check/report before closure |
| 7.2 — Phase review | One cross-milestone code review/testing/report task; verify A7 plus leaderboard panel placement; no automatic or file history persistence. |

Phase exit: A7 plus leaderboard panel placement; no automatic or file history persistence. Publish release v0.7.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

### Phase 8 — Manual file persistence

Outcome: release v1.0.0, covering F1, F2 and complete intended scope.

| Milestone | Outcome and exit |
| --- | --- |
| 8.1 — Validated JSON transfer | F1/L1/C1 complete content, bounds, duplicate keys/IDs, safe score, timestamps and version; F1 one JSON snapshot file, correct current top ten/settings, hidden-settings button containment; F1 invalid content unchanged across all surfaces; valid replacement, cookies/query, cancellation and stale-read protection; integrated capability review/check/report before closure |
| 8.2 — SQLite transfer | F2 one CDN JavaScript dependency, bounded load/init, retry and JSON/game isolation; F2 exact high_scores/settings tables, metadata, bound writes and stable values; F2 integrity/schema/storage types/all rows/version, complete validation and cleanup before one common commit; integrated capability review/check/report before closure |
| 8.3 — Interoperability and distribution | A8 JSON-to-SQLite and reverse, invalid-field matrix, runtime failures and unchanged results/settings/cookies/query; A9 v1.0.0 HTML, embedded/extracted-schema equality, checksum/install instructions and full-scope artifact checks; integrated capability review/check/report before closure |
| 8.4 — Phase review | One cross-milestone code review/testing/report task; verify A8 and full A1-A9 regression/packaging; JSON/SQLite parity and all six settings. |

Phase exit: A8 and full A1-A9 regression/packaging; JSON/SQLite parity and all six settings. Publish release v1.0.0 only after full-phase review, verified explicit integration into main and release-source/artifact checks.

## Increment boundaries and demonstrations

Phase 1 uses failed-downward locking and baseline random selection, without modern actions or empty placeholders for later settings/results/files. Its interface milestone demonstrates a complete playable game for any human feedback about readability/control response before distribution; this feedback can guide a requested amendment without inventing an extra mandatory approval. Phase 2 supplies always-show ghost and default interval locking. Phase 3 demonstrates dynamic midline visibility. Phase 4 proves penetrator safety through representative occupied-stack fixtures. Phase 5 exposes the six defaults/modes through session-only controls and preserves a real release before persistence. Phase 6 adds only configuration durability. Phase 7 adds completed-game session history. Phase 8 adds only manual transfer of the already established settings/history, with common JSON/SQLite validation.

The phase-3 dynamic mode is the delivered behavior before configuration controls; phase 5 initializes the specified configurable default ghost=show. Direct file use and HTTP hosting remain delivery paths; HTTP cookie claims start only with phase 6. Upcoming contracts do not block completion of a correct earlier increment. No phase is a promise to deliver the full later backlog.

## Verification, integration and releases

Select deterministic pure-rule/adapter checks and browser interaction checks through the actual HTML. Use pytest with Playwright's Python API and pinned compatible Chromium headless shell and Firefox builds in a dedicated environment; no other browsers are selected. Establish provisioning, repeated contexts/pages, Canvas output, interaction and cleanup before dependent execution. Use the repository browser/Playwright policies; bounded diagnostics and permitted recovery precede declaring a mode unavailable. Unavailable full-browser or native OS-window behavior is reported unverified and excluded under that policy; it does not remove deployable HTML or block feasible checks/releases. A failing feasible required check or actual game/artifact defect remains a blocker.

At each phase exit, review its delivered contracts plus relevant regressions. Validate the packaged HTML rather than only source fixtures. Use controlled HTTP contexts for cookies/query and a file context for downloaded-page smoke checks. Import checks compare results/settings/cookies/query before and after failures. Rendering checks inspect Canvas output/screenshots and panel geometry; DOM text alone cannot establish board rendering.

Delivery tasks prepare version metadata, instructions, artifacts and release notes. Phase review establishes exits and reports; complete authorized phase boundaries explicitly merge into main, verify the merged state and publish/read back. A release commit/tag on the actual default branch pins that verified source. Publish a GitHub release with the deployable HTML, checksum, installation/use instructions and corresponding notes; the final release also supplies the JSON Schema. The app remains one runtime HTML file. No signed/store package or website deployment is part of this delivery.

## Risks and decision evidence

Shared landing/clock invariants are checked before adding penetrator. Stage session-only configuration before durable effects to isolate precedence defects. Compare both codecs against one canonical validator to detect partial-restore or format drift. At phase 8 prove the pinned CDN library's actual artifact/API before relying on it; library load failure must leave JSON/play usable. Browser availability is evidence-specific, with clear limits rather than blanket compatibility claims. Reports list performed/unavailable checks, findings and remaining unverified behavior. Last-phase review also produces the final implementation report with aggregated unresolved/deferred findings and their owners/options.

Physical ownership is defined by layout after strategy acceptance. This plan does not select an implementation range or activate future-phase hosted objects.
