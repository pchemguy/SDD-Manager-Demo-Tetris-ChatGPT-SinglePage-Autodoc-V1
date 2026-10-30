# Main documentation preparation record

## Current control

- Mode: autodoc/onepass, selected by the project request on 2026-10-30.
- Scope: the complete single-page HTML Tetris description; one documentation pass covering all requested capability increments.
- Approval basis: the user's OK accepts the proposed interaction choices and delivery direction. The user's subsequent k approves the published PROJECT at proposal commit 2f195000fcc605d1543c86975b35e4ab45ccca92; ARCHITECTURE through TASKS checkpoints are preapproved by autodoc mode.
- Tracking: enabled for preparation and implementation by the retained root AGENTS.md policy. The sdd-docs-main milestone and DOCS-001 through DOCS-009 issues were created from the running package definitions, with exact body and milestone associations read back before repository writes.
- Publication: each owned commit is pushed and exactly read back before further work. No implementation range is selected.
- Next boundary: PROJECT approved; prepare the remaining preapproved documents and stop after DOCS-008 before package QC, integration or implementation.
- Source package: installed SDD Manager 0.15.4.

## Scope and decisions

The user's original project description supplies complete target scope. [PROJECT](PROJECT.md) owns the proposed product brief. Required increments are classic baseline, modern rules, dynamic ghost, penetrator, session-only settings, URL/cookies, session leaderboard, and manual JSON/SQLite persistence. Delivery increments are distinct from documentation passes.

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
| DOCS-002 | PROJECT proposal SHA-256 ab0afe7c90e52c2e62d0507251c3c3907273fc122ba7f05262abbb96ace69a9c. User-confirmed choices are incorporated without treating that confirmation as unseen document approval. Checked against the full supplied scope, decision table, product-document boundaries, Markdown spacing and local links. First approval supplied by the user's k after the published-brief approval request; approved bytes unchanged. DOCS-002 completes with this acceptance record and checklist; issue #2 closure follows publication. |
| DOCS-003 | docs/dev/ARCHITECTURE.md SHA-256 3ba925931c90f81d61aa8e6e2db8762121043fe1b08bb03d105afb85e7b02a9f. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-004 | docs/dev/DECOMPOSITION.md SHA-256 ddaedaae7b46c67ad816a39ffbd4bb96e6b6e82319984f7bf3d711fc10075716. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-005 | docs/dev/SPEC.md SHA-256 cb186d90f8b85e4fde436f4e4eb4b77916989c8b33ce27efa18bfb695496ed5f; docs/dev/spec/gameplay.md SHA-256 dec241fc423d3cf473ed5122f1a90ce956fd8305ebb410fe1962698dc023c7bb; docs/dev/spec/configuration.md SHA-256 58027940b2ffc65862cbddbab22109bcd1c2f83aef591a78d691f7d9fc78fac4; docs/dev/spec/files-and-results.md SHA-256 ba44b5792a80c99af1c32eb3c1d0e6922ec78fa2554ba2b9a827077a19ede12a; docs/dev/SPEC-REVIEW-REPORT.md SHA-256 8d42eb805cf3060ae7b33f23441e751973ae6dbb32b112a9218c46b188e83101. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-006 | Not started; preapproved under autodoc, subject to technical QC. |
| DOCS-007 | Not started; preapproved under autodoc, subject to technical QC. |
| DOCS-008 | Not started; preapproved under autodoc, subject to technical QC. |
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

Initialization commit 4b0bc6188d21d06f1badc64d86e2952ca14aad00 was published and exactly read back; issue #1 evidence and completed closure were read back. PROJECT proposal publication was exactly read back. Acceptance fba272dfaaa19950711af9b168c4b219ecffdb4f was published/read back and issue #2 closed/read back before dependent design. No package QC or implementation is authorized. Each completed document retains its actual content identity below; the current commit's later hosted closure is pending until read back. Each completed document retains its actual content identity below; the current commit's later hosted closure is pending until read back. Each completed document retains its actual content identity below; the current commit's later hosted closure is pending until read back.
