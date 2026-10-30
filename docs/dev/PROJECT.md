# Single-page HTML Tetris

## Purpose and outcome

Provide a playable browser Tetris game for keyboard play, distributed as one well-organized HTML file. Embed all application HTML, CSS and JavaScript. External dependencies are limited to widely used JavaScript libraries from established CDNs. Ordinary gameplay is independent of the optional CDN-loaded SQLite capability.

Deliver a simple classic baseline first, followed by bounded useful increments. Publish a versioned GitHub release with notes after each completed, verified and integrated implementation phase. Intended delivery is a browser page, without an application server, separate runtime installation, Electron package or browser extension.

## Complete product scope

### Play and modern rules

Include a classic falling-tetromino game with a board, keyboard movement and rotation, gravity, soft drop, line clearing, scoring, level progression, game over, restart and pause. Extend it with hold, next-piece preview, ghost projection, 7-bag randomization, wall kicks and hard drop.

The default general locking policy waits one full gravity interval from becoming grounded. Hard drop follows that policy unless immediate hard-drop locking is selected. Movement and rotation do not restart the grounded timer unless the piece lifts off the ground. Pausing freezes the timer.

Ghost visibility supports always hidden, always shown and dynamic visibility. Dynamic mode hides the ghost when any projected cell is above the board midline, including a projection straddling the midline, and shows it when all projected cells are in the lower half.

### Penetrator capability

Clearing four lines at once earns one penetrator bonus, up to three stored bonuses. A keyboard activation spends one bonus immediately and makes the current piece a penetrator until it locks. Hold is disabled while that piece is active. The piece can pass through occupied cells without destroying them, but must lock entirely within the board without overlapping occupied cells.

Penetrator hard drop finds the lowest valid non-overlapping landing position below the current piece, ignoring intervening occupied cells. Its ghost previews the same landing. Render penetrator pieces entirely white and reserve white from regular pieces. Show one symbol per available bonus in the game information panel and update it on earning or spending a bonus.

### Configuration and automatic persistence

Provide six settings: three-mode ghost visibility; hard drop on/off; next preview on/off; hard-drop locking following the general policy or immediate; general locking on a failed downward attempt or after a full grounded gravity interval; and hold on/off.

First deliver these as session-only configuration, with no retention across page reloads. Then add per-setting URL query and cookie persistence. Resolve each setting independently from a valid explicit URL value, then a valid saved cookie, then its default. Invalid URL and cookie values fall through to the next valid source. Save explicit valid URL values to cookies even when equal to a default; an omitted parameter retains the saved cookie value. A player change updates its cookie and query parameter immediately. Settings take effect immediately, with affected projections and timing recalculated consistently.

HTTP(S) is the supported mode for cookie persistence. Direct-file opening supports gameplay and manual files, with direct-file cookie behavior requiring separate verification rather than a portability claim.

### Leaderboard and manual file persistence

Show the top ten completed-game results ranked by score, maintained only within the current session. Record game-over results; restarting abandons an unfinished game without creating a result.

At the bottom of the settings panel provide one Save and one Restore button; hiding that panel hides both. Save offers JSON or SQLite and downloads one file containing the current top ten results and all six settings. Restore accepts either format and replaces the session leaderboard and configuration, updating cookies and URL parameters.

Preserve stable result IDs, non-negative integer scores and UTC completion timestamps. JSON includes a format version, results and settings, with a supplied JSON Schema and complete validation including timestamps and setting values. SQLite includes high_scores(id, score, timestamp), settings(key, value), one uniquely keyed row for each setting and database-metadata format versioning. Validate the whole file before changing results, settings, cookies or query parameters. A failure displays a clear error and leaves them unchanged. File saving and restoring are manual.

### Layout and controls

Arrange the final panels left to right: leaderboard; game information and controls; board; settings; controls/help. Keep the board centered when optional panels are shown or hidden. Keep the board and game information panel visible. Accommodate constrained viewports without silently hiding these required panels.

In the game information panel show standard information such as score and level. Above its bottom gameplay buttons, provide individual show/hide toggles for leaderboard, settings and help. At the bottom place only two clickable gameplay action buttons: Start/Restart on the left and Pause/Start on the right. All other gameplay actions use the keyboard. Panel toggles, settings and manual file controls remain clickable as specified.

## Delivery direction

Deliver the classic baseline, modern rules, conditional ghost visibility, penetrator mode, session configuration, URL/cookie persistence, session leaderboard and JSON/SQLite persistence as successive useful releases. The exact milestone and task breakdown belongs to PLAN and TASKS. Each release preserves earlier working capabilities and includes verification evidence and any unverified behavior.

## Technical direction and boundaries

Use native JavaScript, Canvas for the board and standard HTML controls. Organize embedded code into cohesive game rules, timing, presentation and persistence responsibilities so that the single-file delivery remains testable. Use a CDN-loaded SQLite library for the optional database format. Specific library selection, test tools, file-format contracts and detailed controls belong to the subsequent design and specification.

Exclude accounts, online ranking, multiplayer, automatic leaderboard persistence and additional delivery platforms from this scope. Do not imply implementation or browser verification from this brief.
