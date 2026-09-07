# 2026-09-08 — 정독

## 단락 1

`git worktree remove` deletes the checkout and the registration, but it will refuse or leave behind a directory containing **untracked** files. Per the project's worktree-tooling note, frontend worktrees need `nuxi prepare` + a `node_modules` symlink — those generate untracked build artifacts, which is exactly what survived the removal here. The tell that this was an *orphan* and not an active worktree: its `.git` was missing entirely. A live linked worktree has `.git` as a *file* containing `gitdir: /path/to/main/.git/worktrees/<name>`, not a directory. `git worktree prune` only cleans git's **administrative** records under `.git/worktrees/` — it never touches disk contents outside them. So an orphan like this is invisible to git tooling and has to be found by looking at the filesystem.

**문법·구조**: 진단문의 표준 배치다. 1문장은 `deletes A and B, but it will refuse or leave behind C`
로 도구가 하는 일과 안 하는 일을 한 문장 안에 대비시킨다. `will` 이 미래가 아니라 습성을 뜻하는
용법인 게 핵심 — "그럴 것이다"가 아니라 "원래 그렇게 동작한다"다. 2문장 끝의 `which is exactly
what survived the removal here` 는 앞 절 전체를 받는 계속적 `which` 인데, `exactly` 를 넣어
일반 설명을 이 사건의 원인으로 못 박는다. 3문장은 콜론 뒤에 증거를 놓는 무동사 구조라 판정과
근거가 시각적으로 갈린다. 4문장의 `has `.git` as a file …, not a directory` 는 `as` 로 자격을
지정하고 `not` 으로 오해를 잘라내는 짝이고, 마지막 `So …` 는 앞 세 사실에서 결론을 뽑는 유일한
접속사다 — 접속사를 아껴 마지막 한 번만 쓴 덕에 그 문장이 결론으로 읽힌다.

**핵심 표현**: `refuse or leave behind` — 명령이 실패하거나 절반만 하고 물러난다는 두 결과를
한 동사구에 묶었다. `invisible to git tooling` — "도구가 못 잡는다"를 버그가 아니라 관할 문제로
표현하고, 바로 뒤에 대안 관측법(`has to be found by looking at the filesystem`)을 붙여야 문장이
완성된다. `never touches` — 부정 부사를 동사 앞에 세워 "이 명령은 그 일을 애초에 안 한다"는
설계상 경계를 단호하게 긋는다.

**격식 짝**: (작성)
- refined: `git worktree prune` only reconciles git's administrative records; disk contents outside them are never touched.
- plain: `prune` just tidies up git's own bookkeeping — it won't delete anything on disk.

<sub>출처: transcript:skewnono_v3_nuxt 23a9b296 (worktree 정리)</sub>

---

## 단락 2

Code side is clean. The remaining checks are all on the office PC, where git does not reach. Git-tracked code needs nothing. Every VLM default in `poc/workflow_3` already resolves to a live slug. Grounding is `mai-ui` for all six per-purpose services, OCR is `paddleocr-vl-1.5`, `service_fallback_order` is `("mai-ui",)` alone, and the client registry lists only the three served proxy slugs plus two direct-gateway LLMs. The word `ui_venus` survives only in module names, artifact filenames and comments. Removed slugs appear in no reachable code path.

**문법·구조**: 세 단어짜리 판정문(`Code side is clean.`)으로 열고 갈수록 문장이 길어지는 구조라,
바쁜 사람은 첫 줄만 읽고 끝낼 수 있다. 시제가 전부 현재인 게 눈여겨볼 점 — 점검 결과는 과거의
행위가 아니라 지금 코드의 상태이므로 현재형이 맞는다. `already resolves` 의 `already` 는
"당신이 걱정한 그 일은 이미 되어 있다"로 질문에 직접 답하는 부사고, 없으면 그냥 사실 서술이 된다.
5문장은 `A is X, B is Y, C is Z, and D lists …` 로 네 항목을 같은 틀에 얹어 나열하는데, 마지막에만
`and` 를 놓아 목록이 끝났음을 표시한다. 마지막 두 문장은 부정을 서로 다른 방식으로 만든다 —
`survives only in …` 은 살아남은 범위를 좁혀서, `appear in no reachable code path` 는 명사 앞
`no` 로 — 같은 "없다"를 두 번 반복하지 않으려는 선택이다.

**핵심 표현**: `where git does not reach` — 확인이 코드 밖 기계에서만 가능하다고 선을 긋는다.
`resolves to a live slug` — 설정값이 실제로 존재하는 대상으로 풀린다는 뜻이고, `live` 가
"등록만 되어 있는" 것과 "지금 떠 있는" 것을 가른다. `appear in no reachable code path` —
"코드에 남아는 있지만 실행되지 않는다"를 문자열 검색 결과와 구분해 말하는 방식.

**격식 짝**: (작성)
- refined: Every VLM default already resolves to a live slug; no removed identifier appears in a reachable code path.
- plain: All the VLM defaults point at something that's actually running, and none of the old names are in code that runs.

<sub>출처: transcript:auto_recipe_creator ff8357d4 (VLM 서비스 변경 점검)</sub>

---

## 단락 3

The review turned up four things worth fixing, and only one of them is urgent. The keystore lookup has no injectable test seam, so every test either talks to the real credential store or skips silently — that is the one I would fix first. The four discovery roots are best-known defaults rather than confirmed values; I have marked them as such and left a gate in the letter so nobody builds the installer on top of a guess. Status now prints the report's hash as bounded output, which keeps the agent from inventing fields nobody asked for. I added the fewest letters needed, since a document that costs context but never gets used is worse than no document at all. The rollout id stays out of it — that one is the engineer's to choose, and the tooling should not silently widen what it decides on their behalf.

**문법·구조**: 오늘 표현들을 하나의 보고 단락으로 엮은 모범 단락이다. 1문장의
`and only one of them is urgent` 는 발견 개수와 우선순위를 한 번에 줘서 읽는 사람이 분량을
가늠하게 한다. 2문장은 `so` 로 원인→결과를 잇고 대시 뒤에 판단(`that is the one I would fix
first`)을 붙이는데, 가정법 `would` 가 "내 의견이지 당신의 결정을 대신하지 않는다"는 여지를 남긴다.
3문장의 `rather than` 은 A 를 긍정하면서 B 를 부정하는 대비 접속사고, 세미콜론 뒤에서 그 판단에
따라 무엇을 했는지로 넘어간다. 4문장의 `which keeps X from -ing` 는 앞 절 전체를 주어 삼아
효과를 서술하는 틀 — `keep A from B` 가 "막는다"를 `prevent` 보다 부드럽게 만든다. 마지막
문장의 `on their behalf` 는 소유격 대신 써서 "그 사람 몫의 결정"이라는 앞 구절과 맞물린다.

**핵심 표현**: `best-known defaults rather than confirmed values` — 값을 비워 두지도 확정하지도
않는 중간 지점. `bounded output` — 출력에 나올 수 있는 항목의 목록이 닫혀 있다는 뜻. `worse than
no document at all` — 비교급 뒤에 `at all` 을 붙여 "아예 없는 것"을 기준선으로 세운다.

**격식 짝**: (작성)
- refined: I have marked those values as provisional and gated the installer on human confirmation.
- plain: I flagged those as guesses and put a stop sign there so nobody builds on them.

<sub>출처: 모범 단락(작성) — 오늘 표현을 엮음</sub>
