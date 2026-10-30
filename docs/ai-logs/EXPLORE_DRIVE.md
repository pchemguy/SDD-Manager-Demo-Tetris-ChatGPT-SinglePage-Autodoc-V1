---
url: https://chatgpt.com/c/6ae46cb0-a334-83ea-b173-f070e1885436
note: SDD Manager - docs/demo/hello_world/prompts/Single Page Autodoc.md
---

> [!IMPORTANT]
>
> **Historical exploration transcript.** This document is retained for provenance and is not authoritative for current behavior or agent instructions.

## Seed Prompt

> [!NOTE] Prompt
>
>
> Help me develop the following project using $sdd-manager in autodoc mode.
> 
> ### Project repo and credentials
> 
> GitHub repository: https://github.com/{OWNER}/{REPO}
> 
> GitHub token: {FINE_GRAINED_GH_TOKEN}
> 
> ### Versioning and releases
> 
> Manage the project's versioning, choosing an appropriate initial version and increasing it to reflect delivered changes. After each implementation phase is completed, verified and integrated, create and publish a new GitHub release with the corresponding version tag and release notes.
> 
> ### Project: Single-page HTML Tetris game
> 
> #### Playable classic baseline
> 
> Develop a single-page HTML Tetris game with a playable classic baseline and the enhancements below. Deliver one well-organized HTML file with all application HTML, CSS and JavaScript embedded. External dependencies are limited to widely used JavaScript libraries available from established CDNs.
> 
> Provide a **Game info and controls** panel showing standard game information, such as score and level. At its bottom, place only two clickable gameplay control buttons: **Start/Restart** on the left and **Pause/Start** on the right. All other gameplay actions must use the keyboard.
> 
> Treat this description as the complete target scope. Deliver the simplest sensible playable baseline first, then add capabilities through bounded phases that each provide a useful functionality increment.
> 
> #### Modern rule extensions
> 
> - Hold piece.
> - Next-piece preview.
> - Ghost piece.
> - 7-bag piece randomization.
> - Wall kicks.
> - Hard drop.
> - Full gravity interval lock delay: by default, lock after one full gravity interval from becoming grounded. Hard drop follows the same locking policy unless immediate hard-drop locking is selected.
> 
> #### Conditional ghost-piece visibility
> 
> Provide a ghost visibility mode that dynamically hides the ghost when its projected landing position is in the upper half of the board, above the midline, and shows it again when that position returns to the lower half.
> 
> #### Penetrator mode
> 
> Allow the player to turn the current falling piece into a penetrator with a hotkey, provided a penetrator bonus is available. A penetrator can pass through occupied cells without destroying them. This ability lasts until the piece locks; its final position must be entirely within the board without overlapping occupied cells.
> 
> For a penetrator, hard drop must pass through blocking cells to the lowest valid landing position. The ghost piece must preview that same position whenever it is visible.
> 
> Clearing four lines at once awards one penetrator bonus, granting one activation of the penetrator ability. Allow up to three bonuses to accumulate.
> 
> Render penetrator pieces entirely white, and do not use white for regular pieces. Show the available bonuses in the game info and controls panel using one symbol per bonus, such as a lightning bolt. Update the indicator whenever a bonus is earned or spent.
> 
> #### Session-only game configuration
> 
> Provide a settings panel with controls for:
> 
> 1. Ghost-piece visibility: always hide, hide dynamically above the board’s midline, or always show.
> 2. Hard drop: on or off.
> 3. Next-piece preview: on or off.
> 4. Hard-drop locking policy: follow the selected general locking policy, or lock immediately after hard drop.
> 5. General locking policy: lock on a failed downward movement attempt, or after one full gravity interval from becoming grounded.
> 6. Hold piece: on or off.
> 
> Use sensible defaults. Deliver session-only configuration as an intermediate increment before adding persistence. During this increment, keep settings within the current page session; do not persist them across page reloads.
> 
> #### URL GET and cookie persistence
> 
> Support cookies and URL query parameters for all settings above. Restore saved settings or apply URL-supplied settings when the page is reloaded or the game is opened again. Use sensible defaults where neither source supplies a value.
> 
> Resolve each setting independently in this order:
> 
> 1. A value explicitly supplied by its URL parameter.
> 2. A saved cookie value.
> 3. The default value.
> 
> Whenever the player changes a setting, save its selected value in the corresponding cookie and update its URL query parameter.
> 
> Save explicit URL parameter values in the corresponding cookies, including values equal to the default. When a parameter is omitted, retain its saved cookie value rather than replacing it with the default.
> 
> #### Leaderboard
> 
> Show a leaderboard panel with the 10 best completed-game results, ranked by score. Update it after each game and keep the history only for the current session.
> 
> #### File persistence
> 
> Place **Save** and **Restore** buttons at the bottom of the settings panel. Hiding the settings panel also hides these buttons.
> 
> Save offers JSON or SQLite and downloads one file containing the current top 10 results and all six game configuration settings. Restore accepts either format, replaces the leaderboard and applies the saved settings, updating their cookies and URL parameters.
> 
> Preserve each result's stable ID, non-negative integer score and UTC game-completion timestamp in both formats. JSON includes a format version, results array and settings object; provide a JSON Schema and validate the complete content before loading, including timestamps and setting values. SQLite includes `high_scores(id, score, timestamp)` and `settings(key, value)`, with one uniquely keyed row per game setting and format versioning in database metadata.
> 
> Validate the entire file before changing results, settings, cookies or URL parameters. On failure, show a clear error and leave them unchanged. Saving and restoring are manual; restored results become the session leaderboard.
> 
> #### UI layout
> 
> Arrange the panels from left to right:
> 
> | Panel | Position |
> | --- | --- |
> | Leaderboard | Left of game info and controls |
> | Game info and controls | Immediately left of the board |
> | Board | Center of the screen |
> | Settings | Immediately right of the board |
> | Controls/help | Right of settings |
> 
> Keep the board and game info and controls panels visible. In the game info and controls panel, place individual show/hide toggle buttons for the leaderboard, settings and controls/help panels above the **Start/Restart** and **Pause/Start** buttons. Keep the board centered when panels are hidden or shown.
> 
> ### Design clarification
> 
> During preparation, resolve important interactions and boundary cases, including ghost positions that straddle the midline; lock-delay timing and resets; penetrator activation, hold and locking behavior; and invalid configuration values. Surface decisions that materially affect gameplay before implementation.
