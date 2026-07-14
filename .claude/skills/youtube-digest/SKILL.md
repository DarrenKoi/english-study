---
name: youtube-digest
description: Turn a YouTube video into a markdown digest file (metadata, summary, key contents, notable quotes, useful English expressions, and a cleaned-up full transcript) using Chrome browser automation. Use this whenever the user shares a YouTube link (youtube.com/watch, youtu.be) and wants a summary, transcript, notes, or study material from it — even if they just say "take a look at this video". Also use when the user asks to check a YouTube channel for new uploads and digest them.
---

# YouTube → Markdown Digest

Produce one markdown file per video in `youtube/<publish-date>-<slug>.md` (repo root).
The digest serves double duty: a readable summary of the video AND English study
material for this repo, so it always includes a "Useful English expressions" section.

## Step 1 — Load browser tools

Load ALL Chrome tools in ONE ToolSearch call (never one at a time):
`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_create_mcp`

Call `tabs_context_mcp` (createIfEmpty: true) first, then work in a tab from the group.

## Step 2 — Navigate and grab metadata

Batch: navigate to the watch URL (strip `&t=...` timestamps) → wait 4s → run this JS:

```js
const pr = window.ytInitialPlayerResponse; const vd = pr?.videoDetails;
const mf = pr?.microformat?.playerMicroformatRenderer;
const tracks = pr?.captions?.playerCaptionsTracklistRenderer?.captionTracks?.map((t,i) =>
  ({i, lang: t.languageCode, kind: t.kind || 'manual', name: t.name?.simpleText}));
JSON.stringify({title: vd?.title, author: vd?.author, channelId: vd?.channelId,
  videoId: vd?.videoId, lengthSeconds: vd?.lengthSeconds, viewCount: vd?.viewCount,
  publishDate: mf?.publishDate, category: mf?.category,
  description: (vd?.shortDescription||'').slice(0,1200), tracks})
```

Note whether the caption track `kind` is `asr` (auto-generated) — this determines how
aggressive the transcript cleanup in Step 5 needs to be.

Do NOT try to fetch the caption track's `baseUrl` directly (`/api/timedtext`): YouTube
gates it behind a proof-of-origin token and it returns an empty body. Use the on-page
transcript panel instead (Step 3).

## Step 3 — Open the transcript panel

```js
const sec = document.querySelector('ytd-video-description-transcript-section-renderer button');
if (sec) { sec.click(); 'ok'; } else {
  const b = [...document.querySelectorAll('button')]
    .find(x => (x.getAttribute('aria-label')||'').toLowerCase().includes('transcript'));
  b ? (b.click(), 'ok-aria') : 'no transcript button'; }
```

Wait ~3s after clicking. If neither button exists, the video has no transcript —
tell the user and stop (offer a description-only digest).

## Step 4 — Extract the segments

YouTube's current UI renders segments as `transcript-segment-view-model` elements
(the old `ytd-transcript-segment-renderer` returns 0 — don't be fooled; verify with a
screenshot if a selector finds nothing, because the panel may be visibly open anyway).
Each segment's `innerText` has 3 lines: visible timestamp, a screen-reader duplicate
("18 seconds"), then the text — so drop line 1:

```js
const segs = [...document.querySelectorAll('transcript-segment-view-model')]
  .map(el => { const l = el.innerText.split('\n').map(s=>s.trim()).filter(Boolean);
    return {t: l[0], s: l.slice(2).join(' ')}; }).filter(x => x.s);
window.__full = segs.map(x => `[${x.t}] ${x.s}`).join('\n');
JSON.stringify({count: segs.length, chars: window.__full.length,
  first: segs[0], last: segs[segs.length-1]})
```

Sanity-check that the last timestamp roughly matches the video length — if it is far
short, the panel lazy-loaded; scroll the panel and re-extract.

## Step 5 — Pull the text out in chunks

The javascript_tool result truncates around 1,000 characters. Pull the stashed string
with ONE `browser_batch` of `window.__full.substring(i*1000, (i+1)*1000)` calls —
`ceil(chars/1000)` actions. Chunks are exact cuts (often mid-word); concatenate them
with no separator.

## Step 6 — Clean the transcript

Rewrite the raw (usually ASR) transcript into grammatically correct, complete
sentences. This is an editing pass, not a paraphrase — preserve the speaker's meaning,
voice, and order. Specifically:

- Merge fragments that ASR split mid-sentence; fix punctuation and capitalization.
- Fix misrecognized words from context (e.g. "Asians are writing tons of code" →
  "Agents are writing tons of code"). Verify proper nouns (people, products) against
  the video description or a quick web search when unsure.
- Drop pure disfluencies ("um", "you know", stutters like "we we don't") but keep
  rhetorical repetition and the speaker's personality.
- Keep stage directions like [applause] [music] only where meaningful.
- Group sentences into paragraphs by topic; prefix each paragraph with the timestamp
  of its first segment, e.g. `**[2:28]** Okay, let's start. …`.
- Head the section with a note that the transcript was cleaned up from auto-generated
  captions, listing notable name corrections.

## Step 7 — Write the markdown file

Path: `youtube/<publishDate YYYY-MM-DD>-<kebab-title-slug>.md` (trim slug to ~8 words).
Use this exact structure:

```markdown
# <Title>

| | |
|---|---|
| **Channel** | <author> |
| **URL** | https://www.youtube.com/watch?v=<videoId> |
| **Published** | <YYYY-MM-DD> |
| **Length** | <M:SS> |
| **Views (at capture)** | ~<n> |
| **Speaker** | <if identifiable> |
| **Captured** | <today> (transcript: <track name>, cleaned up) |

## Summary
2–4 paragraphs. Lead with the core claim/topic, then the main arguments in order.

## Key contents by section
Timestamped bullet list: `- **M:SS – Label.** one-line gist.`

## Notable quotes
3–6 short blockquotes (cleaned wording).

## Useful English expressions from the talk
8–15 idioms/collocations actually used in the video, each with a one-line meaning
and the quoted usage. Prefer expressions a Korean engineer would find worth learning.

## Transcript (cleaned)
> Note about ASR cleanup + name corrections.
Timestamped paragraphs per Step 6.
```

Send the finished file to the user with SendUserFile (display: render). Do not commit
unless asked.

## Channel-check mode

When asked to check a channel for NEW uploads: open `<channel-url>/videos`, read the
first grid items' titles/links/age via JS on `ytd-rich-item-renderer a#video-title-link`
(fall back to parsing `ytInitialData`). Compare video IDs against
`state/youtube-seen.json` (`{"<channelId>": ["<videoId>", ...]}`); digest unseen ones
(newest first, confirm with the user if more than 2), then append their IDs to the
state file. On first run treat only the latest video as new.
