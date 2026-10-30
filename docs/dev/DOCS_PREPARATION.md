# Main documentation preparation record

## Current control

- Mode: autodoc/onepass, selected by the project request on 2026-10-30.
- Scope: the complete single-page HTML Tetris description; one documentation pass covering all requested capability increments.
- Approval basis: the user's OK accepts the proposed interaction choices and delivery direction. The user's subsequent k approves the published PROJECT at proposal commit 2f195000fcc605d1543c86975b35e4ab45ccca92; ARCHITECTURE through TASKS checkpoints are preapproved by autodoc mode.
- Tracking: enabled for preparation and implementation by the retained root AGENTS.md policy. The sdd-docs-main milestone and DOCS-001 through DOCS-009 issues were created from the running package definitions, with exact body and milestone associations read back before repository writes.
- Publication: each owned commit is pushed and exactly read back before further work. No implementation range is selected.
- Next boundary: DOCS-008 completion is the autodoc stop. DOCS-009 package QC, documentation integration, milestone closure and implementation are not started; await explicit advance direction.
- Source package: installed SDD Manager 0.15.4.

## Scope and decisions

The user's original project description supplies complete target scope. [PROJECT](PROJECT.md) owns the approved product brief. Required increments are classic baseline, modern rules, dynamic ghost, penetrator, session-only settings, URL/cookies, session leaderboard, and manual JSON/SQLite persistence. Delivery increments are distinct from documentation passes.

Confirmed by the user's OK in response to the proposed table:

- Dynamic ghost hides if any projected cell is above the midline.
- Full-interval grounding timer resets only after lifting off the ground; pause freezes it.
- Penetrator activation spends a bonus immediately; hold is disabled until it locks. No overlapping lock is valid.
- Penetrator projection and hard drop share the lowest valid landing below the piece, ignoring intervening occupied cells.
- Settings apply immediately and recalculate projections/timing.
- Invalid URL/cookie values fall through; invalid restore files are rejected atomically.
- Record game-over results only; restart does not record abandoned games.
- Native JavaScript, Canvas board, HTML controls, optional CDN-loaded SQLite; HTTP(S) supports cookie persistence, while direct-file cookies need separate verification.

These are confirmed product choices; precise downstream contracts are defined in SPEC and its focused children without expanding them. Cross-scope concerns are penetrator/hold/landing, pause/lock timing, and configuration/file restore atomicity. Reconsider a confirmed choice only for new conflicting evidence or human steering.

## Decisions and document evidence

| Task | Evidence and decision state |
| --- | --- |
| DOCS-001 | All four root guidance files retained byte for byte against initial commit 6698c445a0f7efad9741118b8db6e6342bddd5eb; none copied. Standard task template instantiated with only DOCS-001 checked. Initialization was completed in 4b0bc6188d21d06f1badc64d86e2952ca14aad00. Later HANDOFF checkpoints supersede that initial snapshot. |
| DOCS-002 | PROJECT proposal SHA-256 ab0afe7c90e52c2e62d0507251c3c3907273fc122ba7f05262abbb96ace69a9c. User-confirmed choices are incorporated without treating that confirmation as unseen document approval. Checked against the full supplied scope, decision table, product-document boundaries, Markdown spacing and local links. First approval supplied by the user's k after the published-brief approval request; approved bytes unchanged. Acceptance/checklist commit fba272dfaaa19950711af9b168c4b219ecffdb4f was published/read back and issue #2 completed closure verified. |
| DOCS-003 | docs/dev/ARCHITECTURE.md SHA-256 3ba925931c90f81d61aa8e6e2db8762121043fe1b08bb03d105afb85e7b02a9f. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-004 | docs/dev/DECOMPOSITION.md SHA-256 ddaedaae7b46c67ad816a39ffbd4bb96e6b6e82319984f7bf3d711fc10075716. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-005 | docs/dev/SPEC.md SHA-256 cb186d90f8b85e4fde436f4e4eb4b77916989c8b33ce27efa18bfb695496ed5f; docs/dev/spec/gameplay.md SHA-256 dec241fc423d3cf473ed5122f1a90ce956fd8305ebb410fe1962698dc023c7bb; docs/dev/spec/configuration.md SHA-256 58027940b2ffc65862cbddbab22109bcd1c2f83aef591a78d691f7d9fc78fac4; docs/dev/spec/files-and-results.md SHA-256 ba44b5792a80c99af1c32eb3c1d0e6922ec78fa2554ba2b9a827077a19ede12a; docs/dev/SPEC-REVIEW-REPORT.md SHA-256 8d42eb805cf3060ae7b33f23441e751973ae6dbb32b112a9218c46b188e83101. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-006 | docs/dev/PLAN.md SHA-256 714a02dea59174ac2eff2e29f90b5a8e2cd7ee7c803dd20d6de61905cb70e0a4; docs/dev/PLAN-REVIEW-REPORT.md SHA-256 228f21a42f029c44ee65dd067a0c904917f1141b13d280b7f277b45152be24f4. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-007 | docs/dev/layout.md SHA-256 4d5a8dc871d1de0b0a7f3e4bcfa083211fb7eb6335822b778009150c15dc67d3; docs/dev/PLAN.md SHA-256 aebb6facf566297757e9da04ed8eb8aef61066da379b85d9a83ef4bbc0e192d2; docs/dev/PLAN-REVIEW-REPORT.md SHA-256 3f6feaecf066d9dd7ede4402ef503fa8087d7cb864cf6665f0478dfee0e1dfbf; AGENTS.md SHA-256 9fff55ada31f4ec46cbe821994e501808b1b54f9b200638f0843081b9edc1a41; docs/dev/policies/BROWSER_DEV_POLICY.md SHA-256 e00e33ed8911ceda92087392cb70bb451ad2e5cf6bd44b69511169d4141e7918; docs/dev/policies/WINDOWS_SHELL_POLICY.md SHA-256 da77f5ff14447abbd8419404917bd5b947ba7bf68c71b4feb72314cc4ea8b4d7; docs/dev/policies/playwright.md SHA-256 2648decb40d219204c735ac7a2e219cb40279ae4a399e00fdf6cced449df3c52; docs/dev/policies/vite-worker-loading.md SHA-256 63ce20b1c366d566b8cba223c3fa49421aa3b77c25d7f0456b0b6b4a3208d0dc. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-008 | docs/dev/TASKS.md SHA-256 5abe29059cadd9be5da24c5d009d0b368724f13526ffb0537a12326ece02cda3; docs/dev/TASKS-REVIEW-REPORT.md SHA-256 2dbc204728ab94d6bb5e4d745450565c53eca49fd16f7a7e2de09676c872fa51; docs/dev/HANDOFF.md SHA-256 5aa4fefafe3486e929174dca33609237b8835a537e50947f999d8e6ae21ba17b. Accepted under the user-selected autodoc preapproval. Scoped authoring review passed; required adjacent review report accompanies SPEC, PLAN and TASKS. Completion/checklist is atomic; publish/read back and close/read back the existing issue before dependent work. |
| DOCS-009 | Not started; autodoc stops before package QC. |

## Initialization

- Git repository: pchemguy/SDD-Manager-Demo-Tetris-ChatGPT-SinglePage-Autodoc-V1; default branch main; clean initial state at 6698c445a0f7efad9741118b8db6e6342bddd5eb.
- Retained files: AI_DISCLOSURE.md, SDD-MANAGER.md, AGENTS.md and SKILL_DISCOVERY_PROTOCOL.md. All initially existed, so initialization adds no mixed-presence pause.
- Repository discovery: no standalone or bundled skills/plugins. Installed SDD Manager supplies the running procedure. At DOCS-007, repository policy links are reconciled to byte-identical local policy copies; this does not install a plugin or browser.
- Manual provenance: default enabled. Byte-identical two-file scaffold seeded on design-docs/ai-logs; seed 699998d5a2ad3f50a807e4748a723d58fae34246; forward correction b9f752a767954b75b054077697cc9df4397e7875 restores the original ignore rules. Explicit two-parent default merge 805cc3aad27443c40ee4121557723c4f2bac8393 verified and published before design-docs/main creation. No transcript recorded.
- Credential exclusion: original ignore entries retained and *.tkn added; gh.tkn verified ignored and untracked. Credential content is excluded from project records.
- Copied scaffold CRLF endings retained byte for byte; whitespace verification uses cr-at-eol.
- Reset: none.

## Pending transitions

DOCS-001 through DOCS-007 commits were each published and exactly read back; corresponding issue completed closures were read back before dependent work. DOCS-008 TASKS and its scoped conformance report have passed the derivation checks; its completion commit publication and issue #8 evidence/closure require readback after this snapshot. Keep DOCS-009 unchecked, issue #9 and sdd-docs-main open. Do not run package QC or integrate documentation under the current autodoc stop.

## Final pass boundary

Full requested scope is represented in PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC with three contract children, PLAN, layout and TASKS. Scoped SPEC, combined PLAN/layout and TASKS reports record current review identities and outcomes. Eight implementation phases/releases contain 17 delivery milestones, 43 delivery tasks and eight dedicated phase reviews (51 product tasks total), all unchecked. This is a document-pass result, not whole-package readiness or delivered functionality.

Additional design precision chosen within the accepted scope includes safe eventual penetrator landing, duplicate-query first-value handling, strict canonical UTC/ID/score validation, versioned SQLite metadata and a single-file SQL runtime. These resolve executable boundary details; the original user-confirmed decisions remain active. No product code, dependencies, browsers, release artifacts or GitHub releases were created. Next eligible workflow is explicit DOCS-009 package QC, followed by verified documentation integration and its checkpoint; implementation additionally needs an authorized range.
