# 2026-07-29 — 정독

## 단락 1

Renaming would cost you the thing the stand-in exists for. That exact line runs unchanged at home and at the office. Give the home stand-in a different name and it has to become a fallback import or an env branch — which breaks the cross-phase principle in CLAUDE.md ("configuration changes only, no code changes"), and worse, means the import path you exercise at home is no longer the one that runs at the office. The stand-in's whole payoff is that it verifies the import, the signature, the column dtypes, and the FTP-download-before-parse ordering **through the real code path**. A differently-named stand-in verifies a path production never takes.

**문법·구조**: 첫 문장은 `cost + 사람 + 사물`의 4형식이고, 그 사물 자리에 `the thing (that) the stand-in exists for` 가 통째로 들어갔다. 관계대명사가 빠진 접촉절이라 전치사 `for` 만 끝에 남는다 — 한국어 감각으로는 허전하지만 영어에서는 이게 가장 자연스러운 자리다. 셋째 문장의 `Give ... and it has to ...` 는 명령문을 조건절로 쓴 형태로, `If you give ...` 보다 짧고 도발적이다. 이어지는 대시 뒤 `which` 는 단어 하나가 아니라 앞 절 전체를 받으며, `breaks ... and worse, means ...` 로 동사 두 개가 같은 주어를 나눠 쓴다. `and worse` 한 마디로 두 결과에 경중을 매기는 게 이 문장의 설계다. 넷째 문장은 `verifies` 하나에 명사구 넷을 매달아 길이를 버티고, 마지막 문장 `a path production never takes` 에서 다시 접촉절로 돌아와 짧게 끊는다. 긴 문장 뒤에 짧은 단정을 놓아 문단이 닫히는 리듬.

**핵심 표현**: `cost you the thing X exists for` — 이름만 바꾸는 사소한 변경이 왜 손해인지 한 줄로 요약한다. `the whole payoff is that ...` — 이 물건의 값어치는 오직 이것 하나라고 범위를 좁힌다. `a path production never takes` — 테스트가 실제로는 안 지나가는 길을 검증하게 된다는 지적.

**격식 짝**: (작성)
- refined: Renaming would cost you the thing the stand-in exists for.
- plain: Rename it and you lose the whole reason it's there.
- refined: A differently-named stand-in verifies a path production never takes.
- plain: If you rename it, you're testing something the office never runs.

<sub>출처: transcript:[assistant] skewnono_v3_nuxt</sub>

---

## 단락 2

Convert the 11 Markdown documents in `ai-dt/ai-terms-and-technologies/` into a polished, fully offline HTML learning portal that opens directly from `html/index.html`. A standard-library Python builder parses the repository's current Markdown subset into semantic HTML, rewrites collection links, and generates one checked-in page per source document. Shared CSS provides the editorial, responsive, theme-aware visual system; a small shared JavaScript file adds filtering, mobile navigation, progress, theme persistence, and active-table-of-contents behavior without fetching content. All reading functions must work from `file://` without a server, CDN, package install, or network request. Preserve all 11 source Markdown files without modifying their content. Escape source HTML before applying the supported Markdown transformations. JavaScript is **progressive enhancement**: article content and basic navigation remain usable when it is disabled. Stage and commit only the files named in each task; preserve unrelated working-tree changes.

**문법·구조**: 목표는 동사원형 `Convert` 로 열고, 구조 설명은 `parses / rewrites / generates` 현재시제 3인칭으로 이어진다. 아직 짜지도 않은 코드를 이미 그렇게 동작하는 것처럼 쓰는 게 설계 문서의 관례다. 세미콜론은 CSS 절과 JS 절을 대등하게 묶는다 — `and` 로 이었으면 앞이 뒤의 원인처럼 읽혔을 자리. 넷째 문장은 전치사 `without` 하나에 명사 넷(`a server, CDN, package install, or network request`)을 매달아 금지 조건을 한 번에 처리한다. 뒤 네 문장에서는 서법이 갈린다: 지켜야 할 성질은 `must work`, 사람이 할 일은 `Preserve / Escape / Stage and commit` 명령형. 같은 목록 안에서도 "무엇이 참이어야 하는가"와 "네가 무엇을 하라"를 이렇게 나눠 쓴다. 콜론 뒤 `article content ... remain usable when it is disabled` 는 앞에 던진 용어를 곧바로 풀이하는 자리이고, `it` 은 JavaScript 를 받으며 수동태로 행위자를 지운다.

**핵심 표현**: `work from file:// without a server` — 서버·설치 없이 파일만 더블클릭해도 돌아간다는 요구. `progressive enhancement` — 없으면 기본형, 있으면 더 나은 층. `preserve unrelated working-tree changes` — 내 작업과 무관한 변경분은 건드리지 말라는 협업 규칙.

**격식 짝**: (작성)
- refined: Preserve all 11 source Markdown files without modifying their content.
- plain: Don't touch the 11 source files.
- refined: Stage and commit only the files named in each task.
- plain: Only add the files the task lists — nothing else.

<sub>출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md</sub>

---

## 단락 3

There is one real hazard, and it isn't pull: `git clean -xdf`. The `-x` flag deletes ignored files, so at the office that would remove `office_utils/` (if it sits at the repo root there rather than in site-packages) and every `providers/office.py` — the exact files git is otherwise protecting. CLAUDE.md already bans whole-tree `checkout`/`restore`/`stash` for a related reason, but `clean -xdf` isn't on that list. Want me to add `git clean -xdf` to the banned-commands list in CLAUDE.md and note it in the `.gitignore` comment? That's the gap this question actually exposes — one line each, and it guards the file you were worried about against the one operation that can genuinely destroy it.

**문법·구조**: `There is one real hazard, and it isn't pull:` 는 답을 콜론 뒤로 미루면서 그 전에 오답 하나를 먼저 치운다. 상대가 걱정하던 게 `pull` 이었으니, 부정이 곧 반박이다. 둘째 문장은 조건을 괄호 안 `if` 절로 밀어 넣어 주절의 흐름을 끊지 않고, 대시 뒤 `the exact files git is otherwise protecting` 을 동격으로 얹는다. `otherwise` 는 "그 명령만 아니면"이라는 조건을 한 단어로 압축한 말. 셋째 문장의 `already bans ..., but ... isn't on that list` 는 현재완료 대신 `already` + 현재형으로 "이미 그래 왔다"를 처리하면서 빠진 항목을 대비시킨다. 넷째 문장 `Want me to ...?` 는 `Do you` 를 통째로 생략한 구어체 제안이라, 문서 톤이 계속 딱딱했더라도 마지막에 사람 목소리를 되돌린다. 끝 문장의 `guard A against B` 는 전치사가 `from` 이 아니라 `against` 라는 점을 함께 외워 두면 좋다.

**핵심 표현**: `there is one real hazard, and it isn't X` — 여럿처럼 보이던 위험을 하나로 좁히면서 오해를 동시에 정정한다. `Want me to ...?` — 결론을 내리지 않고 결정권을 넘기는 가벼운 제안. `guard A against B` — A를 B로부터 지키다.

**격식 짝**: (작성)
- refined: Shall I add it to the banned-commands list?
- plain: Want me to add it?
- refined: the exact files git is otherwise protecting
- plain: the very files git was keeping safe

<sub>출처: transcript:[assistant] skewnono_v3_nuxt</sub>
