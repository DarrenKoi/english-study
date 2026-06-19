# Handoff — 2026-06-19 persistent doc ledger + review fixes

Code-review of the pulled pipeline rework (`3ffb2a0..bde0728`), then fixes for
the findings. Supersedes decision #3 of the
[2026-06-18 journal](2026-06-18-pipeline-rework.md): the dedup ledger is now
**persistent across days**, not date-scoped. Not yet committed (working tree).

## Findings & fixes
1. **[High] Unchanged docs re-processed every day for the whole `recent_days`
   window.** The old SHA model processed each change once; the new
   `docs_today = {date, keys}` ledger reset every day, so every doc in the 7-day
   mtime window was re-fed to the LLM nightly until it aged out — duplicate
   digests + wasted tokens. **Fix:** replaced `docs_today` with a persistent
   `docs_seen` map (`"project/relpath" → "project/relpath:mtime:size"`).
   A doc is skipped until its content changes (key changes); promoted **only by
   `finalize`** so an LLM failure + retry still re-collects. Bounded to one
   entry per path (not per version).
2. **[Medium] Dead `repos`/`repo_queue` machinery.** `collect` always emitted
   empty `repos`/`repo_queue`; `finalize` and `config.DEFAULT_STATE` carried
   them with misleading comments. **Fix:** removed from `collect` manifest,
   `finalize`, and `DEFAULT_STATE` (now `{transcripts, docs_seen, last_run}`).
3. **[Low] Spool archive clobber.** Same-name note processed twice in one day
   overwrote the prior `spool/done/<date>-<name>` archive. **Fix:** `finalize`
   now suffixes `-2`, `-3`… on collision.
4. **[Low] Stale prompt example.** `new-expressions.md` template showed
   `출처: repo:wiki_for_office`; provenance is now `repo:<project> <relpath>`.
   **Fix:** updated the example.

## State migration
`state/progress.json` migrated in place: dropped `repos`/`repo_queue`/`docs_today`,
converted the 17 `docs_today.keys` → `docs_seen` (`key.rsplit(":", 2)[0]` → key).
Existing `transcripts`/`last_run` kept.

## Verified
- Full suite: **33 passing** (`PYTHONPATH=scripts uv run python -m pytest -q`).
- Tests updated: `test_new_day_refeeds_window` → `test_new_day_skips_unchanged_doc`
  (+ `test_new_day_picks_up_edited_doc`); finalize repo_queue tests replaced with
  `docs_seen` promotion + no-clobber archive tests; config tests reschema'd.

## Key files
- `scripts/pipeline/collect.py` — `docs_seen` read, `docs` manifest as path→key map
- `scripts/pipeline/finalize.py` — `docs_seen` promotion, collision-safe archive
- `scripts/pipeline/config.py` — `DEFAULT_STATE`
- `prompts/process.md`, `state/progress.json`
- Tests: `tests/test_collect.py`, `tests/test_finalize.py`, `tests/test_config.py`

## Not done
- `docs/superpowers/plans/2026-06-14-english-study-pipeline.md` still shows the
  original SHA/`repo_queue` design with full code listings — left as a
  point-in-time plan; this journal + the 2026-06-18 one record the supersession.
