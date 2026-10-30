# DECOMPOSITION

## Responsibility model

[ARCHITECTURE](ARCHITECTURE.md) defines four blocks. The components below refine their responsibilities without creating separate runtime application files. The controller coordinates them; shared definitions are immutable and do not depend on consumers.

| Component | Owns and provides | Requires | Boundary checks |
| --- | --- | --- | --- |
| Piece definitions | Shape/orientation tables, regular colors, rotation transitions and kick offsets | Plain data | Four cells per orientation; no regular white; complete transition tables |
| Board rules | Bounds, occupancy, valid placement, row compaction and spawn viability | Piece definitions | No out-of-range writes; surviving occupied cells retained after valid compaction |
| Piece source | Baseline random selection and modern seven-bag queue | Injected random function | Deterministic draws; each modern bag has seven unique types |
| Landing service | Ordinary contiguous landing and penetrator lowest valid landing; grounded eligibility | Board rules; active piece/mode | Ghost/drop parity; transit overlap distinct from lock validity |
| Game reducer | Active/held pieces, score/lines/level, bonus count, spawn/lock/game-over transitions | Board rules, piece source and landing service | Once-only lock/award/completion; rejected action leaves state unchanged |
| Active-play clock | Gravity elapsed time and per-piece grounding deadline | Monotonic deltas and game state | Pause freezes time; generation change removes stale deadlines |
| Configuration service | Six setting definitions, defaults, parsing and validated replacement | Plain data | Complete domain checks shared by all channels |
| Session results | Stable result records, top-ten ranking and whole replacement | Validated results; injected IDs and UTC timestamp source | No duplicate insertion; ranking ties deterministic; restart does not insert |
| Browser controller | Command dispatch, lifecycle, import commit and effects | Rules, clock, config, results and browser adapters | Single ordered mutation path; pending async operations cannot apply stale data |
| Canvas view | Board, active piece, ghost and previews from snapshots | Geometry/colors and derived visibility | Consistent occupied cells and bonus style; no rule mutation |
| HTML view/input | Information, optional panels, labels, buttons, settings/help and keyboard commands | Controller commands and snapshots | Keyboard focus/scroll handling; only specified clickable gameplay actions |
| URL/cookie adapter | Source resolution, cookie read/write and query replacement | Configuration service and browser APIs | Per-setting precedence; preserve unrelated query/fragment; failures visible |
| Canonical export validator | Full version, record, timestamp and setting checks | Shared configuration domains | Reject complete invalid candidates before any live-state effect |
| JSON codec | Parse/encode canonical export; schema-aligned validation | Canonical validator and embedded JSON Schema | Same acceptance as supplied schema plus semantic checks |
| SQLite codec | Read/write high_scores/settings and version metadata | Lazy sql.js; canonical validator | Validate schema/content/version; dispose statements/database on all paths |
| File coordinator | File selection, size/type detection, candidate staging and one download | Both codecs; controller import commit | Cancel is a no-op; failures do not replace live state; snapshot export stable |

## Interface direction and ownership

A game command accepts a current game state and validated configuration, producing a next state and events. Gravity and lock expiration are commands, not hidden side effects inside drawing. The controller consumes the game-over event to add one session result using injected identity/time; reducers do not access current UTC time or browser storage.

The landing service accepts board, piece geometry and movement mode. It returns either a valid landing/grounding description or no permissible destination. Ghost and hard drop consume it directly. Penetrator transformations must retain a valid eventual landing; no consumer invents another drop algorithm. Fixed-cell collision checks stay distinct from penetrator transit checks.

The clock owns elapsed active time and the deadline for the current piece only. The reducer signals transitions that ground, lift or replace a piece. Configuration updates ask the controller to recalculate current timing rather than resetting the game or giving each UI setting its own timer.

The configuration service parses individual source values and validates complete candidates. The URL/cookie adapter owns source precedence and browser effects. The file codecs never write cookies, history or session state. Every codec returns the same validated export representation to the file coordinator.

The import coordinator stages a complete candidate and resolves load errors before dispatching replacement. It commits session results/settings together, then reflects their accepted values through the UI and persistence adapter. Validation failure cannot reach that command. The game board remains owned by the reducer; restored settings affect the current game through the same settings-update path as UI changes.

## Lifetimes and failures

Page load creates one controller/session. Start/Restart creates a new game generation, clears its clock and bonuses, and retains session configuration/results. Pause retains the active piece and remaining timers. A terminal game-over event is consumed once even when a render or restart follows immediately.

Library loading is one lazy, bounded request shared by simultaneous SQLite actions. A failed load can be retried by a later explicit action and does not block JSON. A restore-selection identity protects against older reads completing after a newer selection. File parsing uses disposable temporary objects; save encodes a captured snapshot rather than a leaderboard changing mid-export.

Buttons and keyboard input dispatch commands; programmatic test calls use the same path or pure component functions. An opt-in test export exposes only the seams needed by deterministic rule/adapter tests. It is absent or inert in ordinary play. [SPEC](SPEC.md) owns exact settings, gameplay, export and rejection contracts.
