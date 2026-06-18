# Handoff — 2026-06-18 pipeline rework

Session covering schedule change, doc auto-discovery, idiom example sentences,
same-day dedup, and a code review with fixes. All work is committed and pushed
to `origin/main` (clean tree). Commits referenced by SHA — read those for diffs.

## What changed (commits, newest first)
- `d08fec9` fix(collect): code-review fixes — ledger-on-success, stat-key, dedup loop, dead-code removal
- `e62542a` feat(collect): per-day dedup ledger (later reworked by d08fec9)
- `4033b4b` study: digest 2026-06-18 (verification-run output, kept as today's real digest)
- `a55540f` feat: 00:01 schedule, ~/Codes doc auto-discovery (7d window), idiom example sentences

## Decisions & rationale (not obvious from diffs)
1. **launchd 23:00 → 00:01** so each run lands inside its own date.
   Plist updated in repo *and* copied to `~/Library/LaunchAgents/` + reloaded
   (`bootout`/`bootstrap`). The installed copy is separate from the repo file —
   if you edit `scripts/com.daeyoung.english-study.plist`, re-copy + reload.
2. **collect rewritten**: hardcoded repo+git-diff → recursive discovery of
   `doc`/`docs`/`shared_docs` folders across all of `~/Codes`, `.md`/`.txt`
   modified within `recent_days` (now **7**, was 14), newest-first.
   `english-study` excluded; git repos get best-effort `git pull --ff-only`.
   Config: `config/sources.json` (`doc_dirs`, `doc_exts`, `recent_days`,
   `exclude_projects`). The old `repo_queue` resume machinery was removed from
   `collect` (window model is self-healing); `finalize`/state keys kept for
   spool+transcripts.
3. **Same-day dedup (review finding #1)**: dedup ledger now lives in
   `state/progress.json` as `docs_today = {date, keys}`, promoted **only by
   finalize** (success path). `collect` reads it, resets on a new day. This
   fixed a regression where an LLM failure + same-day retry permanently skipped
   that run's docs. Ledger key = `path:mtime:size` (stat-only) → unchanged docs
   skip without being read; a newest-first char-budget cap stops reading once
   the batch is full.
4. **Idiom example sentences**: `prompts/process.md` now requires a full example
   sentence on every `notes/by-register/*.md` entry and on the `예문` field.
   Verified in the live run's output.

## Verified
- Full suite: **32 passing** (`PYTHONPATH=scripts python3 -m pytest -q`).
- Live `collect → claude -p` ran end-to-end (finalize skipped); produced
  `daily/2026-06-18/` + updated `notes/`. Both features confirmed in output.
- Live discovery: 33 docs in the 7-day window across auto_recipe_creator /
  wiki_for_office / flask_modules / llm_chatbot.

## Open / next-session candidates
- **Today (2026-06-18) is "unprotected"**: the dedup ledger only activates after
  a real `finalize`. The committed `daily/2026-06-18/` digest stands; tonight's
  00:01 run is the first to write `docs_today` into `progress.json`. A manual
  full pipeline run today *could* append a duplicate section to the existing
  digest. Tonight's nightly run is clean.
- **Backfill not done**: existing pre-2026-06-18 `notes/by-register/*.md`
  entries still lack example sentences (only new entries get them). User was
  offered a backfill; deferred.
- **Possible follow-up**: `deferred` count no longer includes budget-unread docs
  precisely vs. discovered total — informational only, low priority.

## Key files
- `scripts/pipeline/collect.py` — discovery, dedup read, budget cap
- `scripts/pipeline/finalize.py` — ledger promotion (`docs_today`)
- `scripts/pipeline/gitutil.py` — trimmed to `_git` + `pull`
- `config/sources.json`, `prompts/process.md`, `CLAUDE.md`
- Tests: `tests/test_collect.py`, `tests/test_gitutil.py`

## Suggested skills for the next agent
- `tdd` — repo is test-first; add a failing test before changing `collect`/`finalize`.
- `code-review` — run before merge on any further pipeline changes.
- `study` — interactive supervised pipeline run with web search.
