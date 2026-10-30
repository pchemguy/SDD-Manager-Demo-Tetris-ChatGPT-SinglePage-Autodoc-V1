# ARCHITECTURE

## System context

The [project brief](PROJECT.md) defines a keyboard Tetris game delivered as one HTML page. A browser provides rendering, input, monotonic timing, URL/history, cookies and manual file selection/download. There is no application backend or remote leaderboard. The application owns session state; cookie configuration and user-selected export files are separate persistence surfaces.

## Major blocks and dependencies

| Block | Responsibility | Dependencies |
| --- | --- | --- |
| Game rules | Board, piece state, legal transitions, scoring, landing, hold and penetrator bonuses | Plain values; injected randomness only |
| Application controller | Lifecycle, active-play clock, ordered commands, settings application and end-of-game events | Game rules; settings and session stores |
| Presentation | Canvas board, information, panels, settings, help and leaderboard | Read-only controller snapshots; commands back to controller |
| Persistence boundary | URL/cookie resolution, complete import validation, format encoding and downloads | Canonical settings and result validators; browser adapters; optional sql.js |

The controller is the only coordinator of state changes. Rendering cannot mutate gameplay. The rules never read DOM, cookies, URLs, files or wall-clock time. The persistence boundary returns validated replacement values rather than editing gameplay while parsing a file. Shared immutable definitions and validators carry settings knowledge once across all consumers.

## Single-file organization

Embed application CSS and JavaScript in named sections of the HTML. Use a single closed application scope containing cohesive functions or objects for the blocks above. Avoid separate runtime application modules, workers, fetched templates, fonts or image assets. Canvas draws the board, active piece and ghost; standard HTML supplies labeled controls and status. Embedded data tables own tetromino geometry and wall kicks.

A framework would add state/rendering machinery without a matching requirement; Canvas and native HTML cover the selected display and controls. Single-file delivery constrains packaging, not logical ownership: pure rules and validators remain callable through an opt-in test seam without a second implementation.

## Timing and command coordination

The controller converts monotonic elapsed active-play time into gravity and grounding events. Pause and hidden-page suspension stop that clock; browser scheduling delay is not an extra game clock. Commands are serialized and update the snapshot before rendering. A piece-generation identity prevents queued input, delayed callbacks or stale landing data from affecting a replacement piece.

Normal and penetrator projections use the same landing service consumed by ghost and hard drop. Penetrator movement permits overlap in transit but maintains the existence of a valid landing at or below its accepted position. Locking is a guarded rule transition: invalid overlap cannot enter the fixed board. This keeps unusual movement from creating an impossible final state.

## State ownership and persistence

Game state holds board, active/held/queued pieces, score, lines, level, bonus count and phase. Session state holds the top ten results, configuration and panel visibility. Panel visibility is not one of the six persisted game settings. Restart replaces gameplay state, retaining settings, panel visibility and session leaderboard.

The configuration service defines names, value domains and defaults once. URL and cookie adapters resolve values independently. The import coordinator reads and validates a temporary complete candidate, then applies one replacement through the controller and browser persistence adapters. It snapshots live state before commit; parse/validation failures have no side effects. Asynchronous file/library work cannot overwrite a newer restore or consume a stale export snapshot.

JSON and SQLite codecs share the canonical result/settings validation. sql.js runs only when SQLite is requested; core play and JSON remain usable if the library is unavailable. Use a pinned CDN release of its single-file JavaScript build with the database runtime embedded, so no separate binary asset is required. The [upstream single-file usage documentation](https://github.com/sql-js/sql.js#usage), checked on 2026-10-30, supports this integration direction. Pin and verify the actual CDN artifact during implementation rather than claiming a network/browser check here.

## Invariants and verification seams

- Only a valid non-overlapping piece can lock; line clearing and bonus awards occur once per lock.
- Ghost and hard drop consume one landing result for the same piece, board and mode.
- Gameplay settings have one canonical domain across UI, query, cookies, JSON and SQLite.
- Validation completes before import affects session state or browser persistence.
- The board's center is independent of optional-panel visibility; the information panel has no hide action.
- A failed external capability produces a user-visible error without disabling ordinary gameplay.

Inject clock deltas, random values, completion IDs/timestamps and storage adapters for deterministic checks. Browser checks use the delivered HTML itself. Exact observable contracts belong to SPEC; [DECOMPOSITION](DECOMPOSITION.md) refines ownership and collaborators.
