# System specification

## Scope and contract ownership

Deliver the [PROJECT](PROJECT.md) game as one HTML file with embedded application markup, styling and JavaScript. [ARCHITECTURE](ARCHITECTURE.md) owns the block model and [DECOMPOSITION](DECOMPOSITION.md) the component boundaries. The controller coordinates pure rules, active-play timing, views and persistence. This specification defines the complete target; PLAN determines which contracts apply to each useful release.

| Contract | Canonical owner | Responsible components |
| --- | --- | --- |
| G1: classic game, scoring, lifecycle and keyboard commands | [Gameplay](spec/gameplay.md#classic-game-g1) | Rules, clock, controller and views |
| G2: modern pieces, hold, kicks, drop and locking | [Gameplay](spec/gameplay.md#modern-rules-g2) | Piece source, reducer, landing service and clock |
| G3: conditional ghost | [Gameplay](spec/gameplay.md#ghost-visibility-g3) | Landing service and view |
| G4: penetrator capability | [Gameplay](spec/gameplay.md#penetrator-g4) | Reducer, board, landing service and view |
| C1: six session settings and live application | [Configuration](spec/configuration.md#setting-domains-c1) | Configuration service and controller |
| C2: URL and cookie persistence | [Configuration](spec/configuration.md#url-and-cookie-persistence-c2) | Configuration service and browser adapter |
| L1: completed-game records and ranking | [Files and results](spec/files-and-results.md#session-results-l1) | Session results and controller |
| F1/F2: validated JSON/SQLite manual persistence | [Files and results](spec/files-and-results.md#manual-files-f1) | Codecs, validator and import coordinator |
| U1: layout, controls and accessible status | This root | HTML input/view and Canvas view |
| D1: artifact and error isolation | This root | Controller, file coordinator and packaging |

## Layout and controls U1

Final panel order is leaderboard, game information and controls, board, settings, controls/help. The board is anchored at the viewport's horizontal center; optional panels do not participate in that centering calculation. Place the information panel immediately left of the board and settings immediately right; leaderboard and help occupy the next outer positions. No panel obscures the board or information. Keep the board and information visible; they have no hide controls.

For constrained widths, compact panel dimensions and board cells while retaining readable controls. Preserve the panel order and board centering; permit horizontal scrolling of outer optional panel regions without moving the board/information pair. Do not wrap panels to different positions or let optional panels obscure required panels. Review at widths 360, 768 and 1440 CSS pixels with optional-panel combinations. Settings/help start visible; leaderboard starts visible when delivered. Panel visibility is session UI state, not a game setting or file field.

The information panel shows score, lines, level and lifecycle state. Modern delivery adds held and next pieces; penetrator delivery adds one lightning symbol per available bonus, up to three. Setting-controlled previews disappear when disabled. Above the two bottom gameplay buttons place separate labeled toggles for the three optional panels once their capabilities exist. Start/Restart is left and Pause/Start right; retain these exact labels. The right button pauses a running game, resumes a paused game or starts an idle game; after game over it starts a fresh game. The left button always starts a fresh game. Both operate without a pointer. All movement, rotation, soft/hard drop, hold and penetrator activation require keyboard input; there are no clickable equivalents.

Settings use labeled native controls. Save and Restore are a single pair at the bottom of settings; format selection may use a labeled native select. Hiding settings hides those controls together. File selection cancellation is a no-op. Keyboard focus remains visible. Gameplay shortcuts do not intercept typing/select operations while a form control is focused. A focused button retains ordinary Enter/Space activation. While the game surface has focus, handled arrows and Space do not scroll the page. Status, errors and leaderboard entries use text content rather than HTML insertion; announce meaningful lifecycle/errors through an accessible status region. Do not announce every gravity tick.

## Delivery and failure isolation D1

The release HTML contains all application code and assets; the optional pinned CDN JavaScript SQLite library is the only runtime dependency. No build step, Node installation or server process is required to play a downloaded page. HTTP(S) static hosting is the supported cookie mode. Document direct-file persistence limitations accurately. JSON play/import/export remains functional when SQLite loading fails. A SQLite load has a bounded timeout, a clear retryable error and no live-state changes.

Treat settings, query, cookies and uploaded content as data. Validation/parse errors identify the affected source or field and preserve valid session state. Cookie/history API failures produce a clear persistence warning while the selected in-session value remains usable; do not claim that unavailable browser persistence succeeded. An invalid restore has no settings, result, cookie or URL effects. No automatic result upload/storage, account or remote leaderboard exists.

## Objective acceptance

| Acceptance | Required evidence |
| --- | --- |
| A1: playable baseline | Start, keyboard move/rotate/drop, clear lines, score/level, pause/resume, game over and restart through the delivered HTML; no other clickable gameplay controls |
| A2: modern rules | Seven-piece bag permutation; hold once per lock; preview order; kick success/failure; ghost/drop parity; grounded timing across pause, kicks and hard drop |
| A3: ghost boundary | Projected cells entirely above, entirely below and straddling row 10; toggles and board changes recompute visibility |
| A4: penetrator safety | Transit overlap preserves fixed cells; valid deepest landing agrees with ghost/drop; invalid transformations rejected; no overlapping locks; bonus cap/earn/spend and hold restriction verified |
| A5: session configuration | All six controls, defaults, immediate effects and page-reload reset in the session-only release |
| A6: automatic persistence | All per-setting URL/cookie/default combinations, explicit default cookie writes, omitted parameters, invalid source values, unrelated query/hash preservation and reload |
| A7: session leaderboard | Terminal results recorded once; abandoned games omitted; top ten/ties/IDs/UTC preserved; reload empties results |
| A8: manual persistence | Both round trips preserve exact values/IDs/timestamps; malformed version/schema/types/duplicates/timestamps/settings/database content leave all four live surfaces unchanged |
| A9: presentation/artifact | Panel toggles preserve board centering; required panels stay usable at stated widths; hidden settings hide Save/Restore; delivered file has embedded application code and runs without a local toolchain |

Each phase checks only delivered contracts and prior regressions. Chromium and Firefox browser checks are intended; execution evidence, unavailable checks and remaining unverified behavior must be distinguished in release reports. These criteria describe required outcomes, not claims that checks have run.
