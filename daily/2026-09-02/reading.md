# 2026-09-02 — 정독

## 단락 1

`SKEWNONO_CHAT_ANSWER_TIMEOUT` default **180 → 240** seconds. The cap stays 360. `wsgi.ini` and `docs/deployment.md` are **deliberately untouched**: both are written against the cap, not the default. The invariant they encode is `cap 360 + 5s grace = 365 < harakiri 380`, and a 240s default lands at 245 — **nowhere near that chain**. That separation is why this was a 4-file change instead of a 6-file one with an infra restart.

**문법·구조**: 첫 문장은 동사 없는 명사구로 열린다 — 화살표 `180 → 240 seconds`가 "무엇이 바뀌었는가"만 압축해서 보여준다. 세 번째 문장의 `are deliberately untouched`는 현재형 수동태다. 능동으로 "we didn't touch them"이라 썼다면 그냥 안 건드렸다는 사실만 남았을 텐데, 수동태 뒤에 `deliberately`를 붙이면 "실수로 빠뜨린 게 아니라 의도적으로 놔뒀다"는 판단이 문장에 박힌다. 콜론 뒤에서 그 이유를 한 겹 더 풀어 준다(`both are written against the cap, not the default`) — `not the default`의 대비가 핵심이다. 네 번째 문장은 등호 표기(`cap 360 + 5s grace = 365 < harakiri 380`)를 문장 속에 그대로 끌어와 수식처럼 쓰고, 대시 뒤에 `nowhere near that chain`이라는 관용구로 안전 여유를 강조한다. 마지막 문장은 `That separation is why X was Y instead of Z` 구조다 — 원인(that separation)을 주어로, 결과(4-file 대 6-file 변경)를 술어로 놓아 "왜 이 정도 규모로 끝났는지"를 한 문장에 담는다.

**핵심 표현**:
- `are deliberately untouched` — 의도를 담은 수동태. 실수로 빠뜨린 게 아니라 일부러 안 건드렸다는 뜻을 분명히 한다.
- `nowhere near that chain` — 위험 지점과 한참 떨어져 있다는 안전 여유 표현.
- `That separation is why X was Y instead of Z` — 설계 결정이 실제 변경 규모를 어떻게 줄였는지 인과로 설명하는 틀.

**격식 짝**:
- refined: *The default and the ceiling are governed by separate documents, which is precisely why this change was contained to four files.* (작성)
- plain: *We keep the default and the max number in different places, so bumping one didn't drag the other six files into it.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt 5a311ce2 — 채팅 응답 타임아웃 값 변경 커밋 요약</sub>

---

## 단락 2

This folder was the visible half of a **seam that closed**. The 2026-08-02 design put retrieval inside `chat` (`knowledge/providers/office.py` querying an index built from `rag_sources/`), so the repo needed a staging directory. The 2026-08-31 rewrite moved the whole answer boundary into `_rag` — one `agent_query` call answers a turn — and the staging directory became an orphan the deletion commit missed. **The tell was** a doc that documents deleted code: `HANDOFF.md` §3 keyed on `chat/knowledge/contracts.py`, and its own header already said §3–5 were superseded. A doc that annotates itself as stale is a doc whose subject has **moved out from under it**.

**문법·구조**: 첫 문장 `This folder was the visible half of a seam that closed`가 단락 전체의 틀을 잡는 은유다. `the visible half of X`는 "보이지 않는 절반(설계 결정)이 먼저 있었고, 이 폴더는 그 결과물일 뿐"이라는 위계를 세운다. 두 번째 문장은 과거시제 서술(`put`, `needed`)로 그 시절의 설계를 사실로 진술하고, 괄호 안에 구체적 파일 경로를 인용해 근거를 덧붙인다. 세 번째 문장은 대시 두 개로 삽입구(`one agent_query call answers a turn`)를 끼워 넣고 `and`로 결과절을 잇는다 — "설계가 바뀌었다"와 "그래서 폴더가 고아가 됐다"를 한 문장 안에 인과로 묶는다. 네 번째 문장은 콜론 뒤에 구체적 증거(파일명, 절 번호)를 나열해 "the tell"이 추상적 인상이 아니라 실제로 짚을 수 있는 것임을 보여준다. 마지막 문장 `A doc that annotates itself as stale is a doc whose subject has moved out from under it`는 같은 명사 `a doc`을 주어와 보어에 반복 배치하는 대구 구조로, 관계절 두 개(`that annotates...`, `whose subject...`)가 겹으로 걸려 격언처럼 마무리한다.

**핵심 표현**:
- `the visible half of a seam that closed` — 구조적 변화가 남긴 흔적을 은유로 짚는 표현.
- `became an orphan (the deletion commit missed)` — 정리 과정에서 빠뜨려 남겨진 대상을 가리키는 표준적 비유.
- `moved out from under it` — 발밑의 땅이 옮겨가듯, 어떤 것의 근거·맥락이 사라졌다는 뜻.

**격식 짝**:
- refined: *This directory persisted only because it documented an architecture that had already been superseded.* (작성)
- plain: *This folder just never got cleaned up after the redesign moved on.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt 70009579 — 죽은 `rag_sources` 폴더 삭제 근거</sub>

---

## 단락 3

**The thing making this a non-decision** is that `@timestamp` isn't a *string* to OpenSearch, it's an instant — the offset you write is discarded after parsing. You're choosing the encoding of a value nothing downstream ever reads back in that encoding. That's the definition of **a change with cost and no effect**. The place a timezone choice *does* matter is where a wall clock is genuinely part of the meaning: `_kst_now()` for the health endpoint, and the `time_zone` on aggregations that decide which calendar day a turn belongs to. Both already say Asia/Seoul. **My recommendation: leave it.** If reading raw docs is the actual pain, set `dateFormat:tz: Asia/Seoul` in Dashboards' Advanced Settings — that fixes the display for every index at once, including the activity one.

**문법·구조**: 첫 문장은 `The thing making this X is that Y`라는 의사분열문(pseudo-cleft)이다. 주어 자리에 원인 전체를 명사절로 앉혀 강조하고, 이탤릭 `*string*`으로 "겉보기엔 문자열 같지만 실제로는 아니다"를 시각적으로 대비시킨다. 두 번째 문장은 목적어 자리에 관계절 표지 없이 명사구(`a value nothing downstream ever reads back`)를 바로 붙인다 — `that/which`를 넣으면 오히려 늘어진다. 세 번째 문장은 앞 두 문장 전체를 `That`으로 받아 한 단어로 요약하는 결론문이다. 네 번째 문장 `The place X does matter is where Y`는 첫 문장과 짝을 이루는 두 번째 의사분열문으로, "안 중요한 곳"과 "중요한 곳"을 같은 문형으로 나란히 세워 대비를 준다 — 조동사 강조형 `does`가 이탤릭으로 다시 강조된다. `My recommendation: leave it.`는 콜론 뒤에 동사원형 두 단어만 남긴 초압축 명령문이다. 긴 논증 끝에 오는 결론이라 길게 쓸 필요가 없다. 마지막 문장은 `If X, Y — that fixes Z` 조건문 뒤에 대시로 효과를 덧붙이는 구조다.

**핵심 표현**:
- `The thing making this X is that Y` — 원인을 강조해서 앞세우는 의사분열 구문.
- `a value nothing downstream ever reads back` — 관계대명사 없이 명사를 바로 수식하는 압축 표현.
- `My recommendation: leave it.` — 대안을 다 검토한 뒤 최소한의 말로 내리는 결론 형식.

**격식 짝**:
- refined: *My recommendation is to retain the current implementation without modification.* (작성)
- plain: *Yeah, I'd just leave it as is.* (작성)

<sub>출처: transcript:skewnono-v3-nuxt 4feef4b1 — 채팅 로그 타임존 저장 방식 검토</sub>
