# Gameplay contracts

Coordinates use a 10-column by 20-row board, zero-based x left to right and y top to bottom. Row 10 is the first lower-half row. A fixed cell contains a regular type/color or a locked white penetrator cell; zero means empty. The landing service and reducer own the following behavior.

## Classic game G1

Use seven four-cell tetrominoes I, J, L, O, S, T and Z. Spawn orientation 0 centered by its bounding matrix at y=0; use a 4 by 4 matrix for I, a 2 by 2 matrix for O and 3 by 3 for the others. Spawn occupied coordinates relative to the matrix origin are: I (0,1),(1,1),(2,1),(3,1); J (0,0),(0,1),(1,1),(2,1); L (2,0),(0,1),(1,1),(2,1); O (0,0),(1,0),(0,1),(1,1); S (1,0),(2,0),(0,1),(1,1); T (1,0),(0,1),(1,1),(2,1); Z (0,0),(1,0),(1,1),(2,1). Spawn x is floor((10 - matrix size)/2). Rotation uses the matrix center (I center between cells); O rotation leaves its occupied cells unchanged. All occupied spawn/movement cells must be within the visible board; no hidden spawn rows are required. A blocked spawn ends the game.

Baseline piece selection is an independent uniformly selected type per spawn. Modern G2 replaces this with the seven-bag. Start resets board, score to 0, lines to 0, level to 1, piece source, hold and bonuses. Retain settings, panel visibility and the session leaderboard. Idle, running, paused and game-over are distinct states. Movement only acts while running. Restart discards an unfinished game without a completed result. Spawn failure after a lock/hold ends the game once. No lock or game-over event can be consumed twice.

Left/Right move one column; Down attempts one-row soft drop; Up or X rotates clockwise; Z rotates counterclockwise. Space performs hard drop when delivered/enabled; C or Shift holds when delivered/enabled; P activates penetrator when delivered; Escape toggles pause. Start/Restart and Pause/Start also support the root U1 semantics. Disable held-key repeat for rotation, hard drop, hold, activation and pause; allow browser key repeat for horizontal movement and soft drop. Ignore gameplay shortcuts in form controls. Help lists these bindings and disabled capability state.

A normal placement may not overlap fixed cells. Baseline rotation tries only the unchanged origin, rejecting collision. A successful soft-drop row earns 1 point; gravity earns none. A lock adds cells, clears every full row simultaneously, compacts remaining rows downward and inserts empty rows at the top. For 1/2/3/4 cleared rows award 100/300/500/800 times the level before that clear. Total lines increase by cleared rows; level is 1 + floor(lines/10). Gravity interval is max(80, floor(1000 * 0.8^(level-1))) milliseconds. The accumulator processes elapsed active time without granting extra soft-drop points; a level change changes future intervals without resetting an active grounding deadline. Scores remain non-negative safe integers, saturating at Number.MAX_SAFE_INTEGER if necessary. No spin/combo/back-to-back scoring is required.

Baseline locks on a failed gravity or soft-drop attempt. In any lock, reject invalid/overlapping placement before fixed-board mutation. Render distinguishable regular colors with no pure white regular piece; use white exclusively for active/locked penetrator cells among piece colors. Pause freezes gravity and grounding time and suppresses gameplay inputs. Losing page visibility pauses a running game; returning does not resume it automatically.

## Modern rules G2

Shuffle one of each type into a bag using injected uniform randomness; consume the whole bag before replenishing. The next preview shows the next source draw, not the held piece. Holding an empty slot stores the active type and draws the queued type; swapping with a nonempty slot does not consume a source draw. Each held/spawned piece starts in orientation 0 at the spawn origin. Hold is allowed once per active-piece turn; locking a piece enables hold for the next piece. A blocked hold spawn causes game over. Holding cannot transfer penetrator status. Disabling hold retains its slot; reenabling does not bypass the once-per-turn limit.

For clockwise/counterclockwise rotation try the orientation transition's ordered offsets, accepting the first legal destination; failed rotation changes neither pose nor timer. Every row below starts with (0,0). The remaining offsets use x positive right and y positive UP; convert to board coordinates by subtracting y. Orientations are 0, R, 2, L. These are the game's specified kick tables, shared by transit and normal movement as applicable.

| Transition | J/L/S/T/Z remaining offsets | I remaining offsets |
| --- | --- | --- |
| 0 to R | (-1,0), (-1,1), (0,-2), (-1,-2) | (-2,0), (1,0), (-2,-1), (1,2) |
| R to 0 | (1,0), (1,-1), (0,2), (1,2) | (2,0), (-1,0), (2,1), (-1,-2) |
| R to 2 | (1,0), (1,-1), (0,2), (1,2) | (-1,0), (2,0), (-1,2), (2,-1) |
| 2 to R | (-1,0), (-1,1), (0,-2), (-1,-2) | (1,0), (-2,0), (1,-2), (-2,1) |
| 2 to L | (1,0), (1,1), (0,-2), (1,-2) | (2,0), (-1,0), (2,1), (-1,-2) |
| L to 2 | (-1,0), (-1,-1), (0,2), (-1,2) | (-2,0), (1,0), (-2,-1), (1,2) |
| L to 0 | (-1,0), (-1,-1), (0,2), (-1,2) | (1,0), (-2,0), (1,-2), (-2,1) |
| 0 to L | (1,0), (1,1), (0,-2), (1,-2) | (-1,0), (2,0), (-1,2), (2,-1) |

O has no translated kick. Landing for an ordinary piece is the last legal origin reached by contiguous one-row downward movement, never passing through fixed cells. Ghost is drawn at that placement. Hard drop moves directly there and earns 2 points per downward row moved; drop distance zero earns zero points. Hard drop with the general failed-attempt policy counts its terminal blocked downward attempt and locks. With interval locking it starts or retains the grounding deadline. Immediate hard-drop policy locks on that hard-drop command in either general mode. Repeated zero-distance hard drops do not renew a deadline or earn points.

For full-interval locking, a piece becomes grounded when a one-row downward move is impossible under its movement mode. Detect this after every spawn, movement, rotation, gravity/drop or setting change. On first grounding, capture the current gravity interval as a per-piece deadline measured in active-play time. Lateral movement/rotation that stays grounded retains the same deadline; a failed downward attempt does not lock early. If the piece lifts off ground, clear that deadline; a later grounding starts a new full interval. Successful hold or lock discards all replaced-piece timers. Pause/resume retains the remaining duration. At a clock step, process already due grounding expiration before a gravity event at the same active time. Input at a time equal to an expired deadline cannot renew the old piece. A delayed callback must not apply to a newer generation.

## Ghost visibility G3

Ghost is an outline/translucent projection that does not modify the board, active pose, score or timing. Always-hide draws none. Always-show draws the shared landing whenever there is one. Dynamic mode draws it only when every occupied projected cell has y >= 10. A piece with even one projected cell at y=9 is hidden, including a piece crossing the midline. Recompute on pose, board, penetrator-mode or visibility-setting changes. An outline at the active pose is allowed when already landed.

## Penetrator G4

A simultaneous four-line clear awards one bonus after the clear, capped at three. Spending is allowed only while running with an active regular piece and at least one bonus; reject without effect when already active, paused or empty. Activation spends exactly one immediately, marks the current piece white and disables hold until lock. It does not reset the pose, source order or a retained grounding timer. Start/Restart clears bonuses. Earning/spending redraws one lightning symbol per stored bonus; zero shows none and a numeric/text empty state.

Transit may overlap fixed cells, without deleting or recoloring them, but all occupied active cells remain in board bounds. For an orientation/x, enumerate candidate origins at or below the current y within board bounds and select the greatest y with no fixed-cell overlap. This is the penetrator landing even if obstructed cells occur along the path. A transformation is accepted only if at least one such valid destination remains at or below its candidate pose. If no destination exists, reject the movement/rotation unchanged. This preserves a safe eventual lock, including while the visible active pose overlaps the stack.

Downward transit moves one row while that invariant holds. Grounding occurs at the deepest valid destination when no further downward transit preserving a valid future destination exists. This destination cannot overlap the stack. Ghost/hard drop use exactly the same deepest valid destination. Hard drop may cross multiple occupied segments; it does not clear them or award their lines. Scoring, general/immediate lock policy and pause timing follow G1/G2. Only actual full rows created by a valid lock clear normally. The ability ends at lock, so the next piece is regular and hold can become available under its normal turn rule.
