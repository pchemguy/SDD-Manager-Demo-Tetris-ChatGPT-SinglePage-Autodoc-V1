# Main documentation preparation record

## Current control

- Mode: autodoc/onepass, selected by the project request on 2026-10-30.
- Scope: the complete single-page HTML Tetris description; one documentation pass covering all requested capability increments.
- Approval basis: the user's OK accepts the proposed interaction choices and delivery direction. It does not accept an unseen project brief. PROJECT approval remains pending; ARCHITECTURE through TASKS checkpoints are preapproved by autodoc mode.
- Tracking: enabled for preparation and implementation by the retained root AGENTS.md policy. The sdd-docs-main milestone and DOCS-001 through DOCS-009 issues were created from the running package definitions, with exact body and milestone associations read back before repository writes.
- Publication: each owned commit is pushed and exactly read back before further work. No implementation range is selected.
- Next boundary: publish PROJECT for first approval; then prepare the remaining preapproved documents and stop after DOCS-008 before package QC, integration or implementation.
- Source package: installed SDD Manager 0.15.4.

## Scope and decisions

The user's original project description supplies complete target scope. PROJECT.md will own the proposed product brief once created. Required increments are classic baseline, modern rules, dynamic ghost, penetrator, session-only settings, URL/cookies, session leaderboard, and manual JSON/SQLite persistence. Delivery increments are distinct from documentation passes.

Confirmed by the user's OK in response to the proposed table:

- Dynamic ghost hides if any projected cell is above the midline.
- Full-interval grounding timer resets only after lifting off the ground; pause freezes it.
- Penetrator activation spends a bonus immediately; hold is disabled until it locks. No overlapping lock is valid.
- Penetrator projection and hard drop share the lowest valid landing below the piece, ignoring intervening occupied cells.
- Settings apply immediately and recalculate projections/timing.
- Invalid URL/cookie values fall through; invalid restore files are rejected atomically.
- Record game-over results only; restart does not record abandoned games.
- Native JavaScript, Canvas board, HTML controls, optional CDN-loaded SQLite; HTTP(S) supports cookie persistence, while direct-file cookies need separate verification.

These are confirmed product choices; precise downstream contracts remain to be specified without expanding them. Cross-scope concerns are penetrator/hold/landing, pause/lock timing, and configuration/file restore atomicity. Reconsider a confirmed choice only for new conflicting evidence or human steering.

## Decisions and document evidence

| Task | Evidence and decision state |
| --- | --- |
| DOCS-001 | All four root guidance files retained byte for byte against initial commit 6698c445a0f7efad9741118b8db6e6342bddd5eb; none copied. Standard task template instantiated with only DOCS-001 checked. HANDOFF records initialization and the pending brief. |
| DOCS-002 | Not yet proposed; first PROJECT approval remains active. |
| DOCS-003 through DOCS-008 | Not started; subsequent document checkpoints preapproved by autodoc mode, subject to technical QC. |
| DOCS-009 | Not started; autodoc stops before package QC. |

## Initialization

- Git repository: pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1; default branch main; clean initial state at 6698c445a0f7efad9741118b8db6e6342bddd5eb.
- Retained files: AI_DISCLOSURE.md, SDD-MANAGER.md, AGENTS.md and SKILL_DISCOVERY_PROTOCOL.md. All initially existed, so initialization adds no mixed-presence pause.
- Repository discovery: no standalone or bundled skills/plugins. Installed SDD Manager supplies the running procedure. Repository browser-policy links to absent bundled plugin assets need project-specific reconciliation before browser work; they do not establish that those assets are installed.
- Manual provenance: default enabled. Byte-identical two-file scaffold seeded on design-docs/ai-logs; seed 699998d5a2ad3f50a807e4748a723d58fae34246; forward correction b9f752a767954b75b054077697cc9df4397e7875 restores the original ignore rules. Explicit two-parent default merge 805cc3aad27443c40ee4121557723c4f2bac8393 verified and published before design-docs/main creation. No transcript recorded.
- Credential exclusion: original ignore entries retained and *.tkn added; gh.tkn verified ignored and untracked. Credential content is excluded from project records.
- Copied scaffold CRLF endings retained byte for byte; whitespace verification uses cr-at-eol.
- Reset: none.

## Pending transitions

Initialization publication and DOCS-001 evidence/closure require readback after this record's commit. PROJECT remains awaiting proposal and approval. Recover actual Git and hosted state before replaying operations.
