# Results and file contracts

## Session results L1

A completed game is a game-over transition, including blocked spawning after a hold. Insert one record for that game generation with a new stable ID, the final non-negative integer score and the UTC completion timestamp. Pause, restart and page close do not complete a result. New-game result IDs must not collide with restored records; generate a new ID if needed. Retain at most ten ranked records. Order by score descending, timestamp ascending, then ID by ASCII lexical order. Preserve IDs and timestamps exactly across ranking and file round trips. Render rank/score/time clearly; empty history is a valid visible state.

A record has exactly id, score and timestamp. ID is 1 to 128 ASCII characters matching ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$. Score is an integer from 0 through 9007199254740991. Timestamp is canonical UTC YYYY-MM-DDTHH:mm:ss.sssZ, a real calendar instant accepted without normalization and identical to its parsed instant's ISO serialization. Reject impossible dates, local/offset times, leap-second spellings, omitted milliseconds and noncanonical forms. Duplicate IDs are invalid even if all other fields match. Equal scores/timestamps with distinct IDs are valid.

Reload starts with an empty leaderboard even when settings persist. Restore replaces history; a subsequent completed game is ranked with the restored records. Export and restore do not record a new game or alter the current board/score, and restoring settings follows C1.

## Manual files F1

Save captures one immutable snapshot of current top ten plus all six settings, offers JSON or SQLite, and downloads exactly one selected-format file. Default selection is JSON; format selection is not a seventh game setting. Suggested names are tetris-session.json and tetris-session.sqlite. Cancel or an encoding/download failure shows an appropriate status without changing live results/settings. Restore uses one file picker accepting either format; detect SQLite by its SQLite format 3 header and otherwise attempt UTF-8 JSON, rather than trusting an extension. Permit one UTF-8 BOM for JSON. Limit input to 2 MiB and reject malformed UTF-8, excessive nesting beyond 32 and duplicate object member names. These limits cover the intended ten-result format without accepting arbitrarily large data.

JSON root has exactly formatVersion, results and settings. formatVersion is integer 1. results is an array of zero through ten complete records; input array order may vary, and canonical ranking is applied after complete validation. settings has exactly the six C1 keys and their in-memory types/values. Additional root/record/setting properties, missing properties, non-finite/non-integer scores, unknown versions and invalid semantic fields are errors. Supply a JSON Schema Draft 2020-12 describing this complete structure, with no additional properties, bounds/enums and timestamp shape/date-time format. Embed its authoritative data in the page; distribute an identical extracted schema with release documentation. Runtime validation must enforce calendar/UTC round-trip semantics and unique IDs in addition to schema structure, and check every array entry before any truncation or commit.

Restore reads/parses/validates in a temporary candidate, including all settings and all records. Before validation succeeds it must not mutate results, configuration, timers, cookies or URL. After success replace results and apply configuration as a single controller operation, then update all settings cookies/parameters under C2. Keep the running game's board, source, score and bonuses. Browser persistence capability errors after successful validation are reported under C2; do not misreport them as invalid input. Validation failures identify the problem clearly and leave all live surfaces exactly as before. File selection/read cancellation has no effects. If a newer restore starts, discard an older unfinished read before it can commit. JSON actions require no CDN library.

## SQLite format F2

Create a regular SQLite database with PRAGMA user_version=1 and application_id=1414812243 (hexadecimal 0x54545253). These header metadata fields identify the version and format; reject unsupported or missing values. Use exactly these two user tables and columns:

```sql
CREATE TABLE high_scores (
    id TEXT NOT NULL PRIMARY KEY,
    score INTEGER NOT NULL CHECK (score >= 0 AND score <= 9007199254740991),
    timestamp TEXT NOT NULL
);
CREATE TABLE settings (
    key TEXT NOT NULL PRIMARY KEY,
    value TEXT NOT NULL
);
```

settings contains exactly one row for each C1 key, using its URL/cookie spelling as TEXT, including on/off Boolean encodings. high_scores contains zero to ten rows; serialize canonical result values without regenerating IDs/timestamps. Export inserts bound parameters, not interpolated user text, and completes its temporary database before downloading. No persistent browser database or worker is required.

Before accepting import, inspect SQLite header, integrity, version/application metadata, actual table/column definitions and every row's SQL storage type/value. Require TEXT IDs/timestamps/keys/values and INTEGER scores in the safe range. Require the two actual user tables with exactly their columns in stated order and declared types, non-null declarations and primary keys; reject views, triggers and unexpected user schema objects. Internal SQLite bookkeeping objects may be ignored only when they cannot supply user records. Do not run SQL supplied by the file; use fixed read-only queries and schema inspection, with trusted_schema disabled/query_only enabled before querying content. Bound size, row counts and duplicates independently of claimed SQL constraints. Then convert to the canonical export model and run the same complete semantic validation as JSON. An apparently well-formed SQLite file with an invalid timestamp or setting is still invalid.

Close temporary statements/databases on success and failure. Lazy-load the pinned single-file sql.js library only for SQLite actions, with a 20-second load/init timeout and explicit retry after failure. A missing/unavailable CDN or runtime does not change current state or prevent JSON actions. Record actual loaded artifact/version and verification in the release evidence.

## Failure and parity acceptance

Exercise zero/ten results, unsorted valid input, score zero/maximum, stable IDs, tie ordering and timestamp boundaries. Both formats must round-trip to identical canonical records/settings. Reject eleven rows, duplicate result IDs/setting rows, missing/unknown keys, wrong Boolean spellings/types, invalid calendar dates, unsafe integers, malformed JSON, wrong versions, corrupt/truncated SQLite, schema/type mismatches and wrong application metadata. For each rejection compare results, settings, cookies and URL before/after and confirm no mutation. Test CDN failure, cancelled selection, read failure and competing restores separately from invalid-content rejection.
