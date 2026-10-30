# Configuration contracts

The configuration service owns these definitions. UI, query, cookies and both file formats share them; values are case-sensitive and no truthy/falsy coercion is accepted.

## Setting domains C1

| Key / query name | In-memory and file domain | URL/cookie spelling | Default |
| --- | --- | --- | --- |
| ghost | hide, dynamic, show | Same strings | show |
| hardDrop | Boolean | on, off | true |
| nextPreview | Boolean | on, off | true |
| hardDropLock | general, immediate | Same strings | general |
| lockPolicy | failed, interval | Same strings | interval |
| hold | Boolean | on, off | true |

All six must occur exactly once in a file settings object/table. Unknown keys or wrong types are invalid for complete imports. In the session-only increment, page initialization always uses defaults and setting changes affect only that page session; it reads/writes neither cookies nor query for game settings. Reload resets them. It does not save the leaderboard implicitly in any increment.

User changes update the active configuration without restarting or recording a game. Disabled hard drop ignores Space. Disabled preview hides the preview without consuming or changing its queue. Disabled hold preserves the slot and turn limit; active penetrator still disallows it regardless of hold=true. Ghost mode changes redraw the existing shared projection.

Switching interval to failed clears the current deadline; it does not itself lock. A later failed-down action, including the terminal hard-drop attempt, locks. Switching failed to interval starts a full interval if grounded at the change time, or starts it at later grounding. An unchanged interval policy preserves the current deadline. Changing hardDropLock affects the next hard-drop command only; choosing immediate does not retroactively lock. Restoring all six settings uses this same atomic settings update and timing rules, not six sequential partial updates.

## URL and cookie persistence C2

On HTTP(S) load, for each key choose a valid explicit URL parameter first, otherwise a valid cookie named tetris_<key>, otherwise its default. The first occurrence of a duplicate query key is the explicit candidate. Empty values, wrong case and unknown spellings are invalid. Invalid URL/cookie entries fall through independently and may produce a source-specific warning, without rejecting valid values for other settings. Unknown query parameters are unrelated and retained.

Write every valid explicit URL value into its cookie even if equal to the default. For an omitted or invalid parameter, do not replace a saved cookie with the default. No startup query rewriting is required. A user change writes only the changed key's cookie and sets one matching URL parameter using history replacement, without reload or a new history entry. Preserve unrelated parameters and the fragment. A valid restore writes all six keys and sets all six parameters, including default-valued ones. Never serialize transient panel visibility or leaderboard into cookies/query.

Cookie values use the table's spellings; URL encode names/values safely. Use Path=/, SameSite=Lax, Max-Age=31536000, and Secure on HTTPS. Verify selected values can be read back where cookie persistence is claimed. Cookie rejection/history failures produce an explicit warning and preserve the usable session setting. Under file: URLs, apply valid query values if available and permit in-session changes; unavailable cookie/history persistence must not crash play, JSON or SQLite file actions. Do not claim durable direct-file cookies without environment-specific verification.

## Acceptance details

Check all six domains against shared parsing/serialization, independent mixed-source precedence, explicit defaults, omission retention, invalid first duplicates, unrelated query/hash retention, cookie denial and history exceptions. Check immediate settings changes both in midair and grounded, with remaining interval timing, active penetrator and used hold. Restore validation failure must not reach any settings/timing/browser-write path.
