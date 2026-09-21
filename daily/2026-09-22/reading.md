# 2026-09-22 — 정독

> repo 문서 6건은 본문이 한국어라 인용할 영어 단락이 없고 세 단락 모두 transcript 의 `[assistant]` 영어 원문이다. 굵은 글씨와 불릿 기호를 풀어 한 단락으로 이었고 긴 파일 경로와 괄호 속 임계값 목록은 `…` 로 줄였다. 단락 1 마지막 문장 뒤에 붙은 코드 블록 머리말(`` — `templates.py`: ``)은 떼고 마침표로 닫았다. 단락 1은 버그의 원인과 수정 범위를 설명하는 글, 단락 2는 "이 버튼은 왜 있나"에 답하는 글, 단락 3은 아침에 일을 이어받으며 쓰는 상태 보고. 같은 날 같은 사람의 영어가 목적에 따라 얼마나 짧아지고 길어지는지 견줘 읽어 보자.

## 단락 1

`cond.scope` is parsed (`CondInfo.scope`, `is_om`/`is_sem`) and has zero consumers in the correction path — grep finds it only in `verify_success_gather.py` and debug scripts. It's sitting in the `cond` local variable inside `load_template` and was being thrown away. That matters because `key_type` drives two things: the `templates` dict key `route_template` matches `read_mode()` against, and the `is_sem_template` branch at `matching/engine.py:977` (OM = MIND⊕sel RRF, SEM = ECC alone). The tempting fix — let cond override `key_type` — is worse than the gap. `key_type` is set inside `load_template`, but the `"OM"`/`"SEM"` dict key `route_template` looks up is set independently in `build_templates_from_assets`. Flipping one without the other gives you a template labeled `sem` filed under `"OM"`, which fails silently instead of loudly. So I added the check, not the override.

**문법·구조**: 첫 문장은 한 주어에 수동 `is parsed` 와 능동 `has zero consumers` 를 `and` 로 물렸다. "파싱은 되는데 쓰이지는 않는다"는 대조가 동사 두 개로 끝난다. 대시 뒤에 붙은 건 grep 결과라는 근거. 둘째 문장은 한 문장 안에서 시제가 바뀐다. 값은 지금도 변수에 있으니 현재진행 `It's sitting`, 버려지는 일은 이번 수정 전까지 이어진 일이라 과거진행 수동 `was being thrown away`. 셋째 문장의 `That matters because …` 는 앞의 사실이 왜 중요한지로 넘어가는 다리다. 가장 까다로운 곳은 콜론 뒤 첫 항목 `the templates dict key route_template matches read_mode() against` 이다. 관계대명사가 빠지고 전치사 `against` 가 절 끝에 홀로 남았다. 풀면 `the dict key (that) route_template matches read_mode() against`, 곧 "route_template 이 read_mode() 결과를 대조하는 그 키". 한국어 화자는 `against which …` 로 앞에 끌어오기 쉬운데 기술 문서에서도 전치사를 뒤에 남기는 쪽이 더 흔하다. 다섯째 문장의 `the dict key route_template looks up` 은 어떨까? 같은 접촉절이고 이번에는 `looks up` 의 목적어가 앞의 `dict key` 다. 여섯째 문장은 동명사 주어 `Flipping one without the other` 에 과거분사 둘(`labeled`, `filed under`)이 이어지고 비제한 `, which …` 가 앞 상황 전체를 받는다. 마지막 문장은 `So` 로 결론을 내리며 `A, not B` 로 한 일과 안 한 일을 가른다.

**핵심 표현**: `That matters because …` — 방금 말한 사실이 왜 문제인지 이어 갈 때. / `set independently in …` — 같은 값을 두 곳이 따로 정한다는 사실을 한 단어(`independently`)로 드러낸다. / `fails silently instead of loudly` — 에러 없이 틀린 결과만 내는 실패를 부사 대조로 말한다.

**격식 짝**: (작성)
- refined: The field is parsed but never consumed in the correction path; in effect, it has been discarded.
- plain: We parse it, but nothing in the correction path ever reads it. It just gets thrown away.
- refined: Changing one of these without the other would produce a template whose label and dictionary key disagree, and the failure would go unnoticed.
- plain: Change one and not the other, and the template ends up under the wrong key with nothing to tell you.

<sub>출처: transcript:[assistant] auto-recipe-creator</sub>

---

## 단락 2

The gallery is not "images only". It is a review queue of measurement sites, one card per measured or failed site row. Every site gets a card whether or not the tool saved an image for it. A site with no image file still renders as a card showing an image-off icon and the text 이미지 없음, because the evidence row (failure, residual, vendor score) must stay visible even when there is nothing to look at. So 이미지 있음 hides those placeholder cards. The filter in `…/views/Gallery.vue:258` drops any entry whose `hasImage` is false. Image-less sites are real in the data: in the mock, every 20th step is an "empty" row with no image names, and at the office a failed or unmeasured site often has no image file at all. The queue even counts them separately as `withImage` / `withoutImage`.

**문법·구조**: 상대의 전제("이미지만 보여 주는 화면")를 부정문으로 먼저 꺾고 곧바로 `It is a review queue …` 로 올바른 정의를 세운다. 쉼표 뒤 `one card per measured or failed site row` 는 동사 없는 동격 명사구로 queue 의 구성을 풀어 준다. 셋째 문장의 `whether or not` 은 "~했든 안 했든"이라는 양보. `whether the tool saved an image for it or not` 처럼 `or not` 을 뒤로 보내도 된다. 가장 긴 넷째 문장을 뜯어 보자. `renders as a card` 의 `render` 는 "그려지다"는 자동사이고 현재분사 `showing …` 이 카드를 뒤에서 꾸민다. `because` 절의 `must` 는 규칙이 아니라 설계 요구다. `even when` 은 실제로 일어나는 경우를 걸 때 쓰고 가정이라면 `even if`. `nothing to look at` 에서는 to부정사가 `nothing` 을 꾸미며 전치사 `at` 을 끝에 남겼다. 두 문단을 잇는 건 다섯째 문장의 `So`. 앞에서 깐 사실(이미지 없는 카드가 있다)에서 버튼의 존재 이유를 끌어내니 설명이 억지스럽지 않다. 사물에도 소유격 `whose` 를 쓴다는 점은 `whose hasImage is false` 가 보여 준다. `every 20th step` 은 `every + 서수` 로 "20번째마다". 마지막 문장의 `even` 은 증거를 하나 더 얹는 점층이다.

**핵심 표현**: `whether or not` — 조건과 상관없이 늘 그렇다고 말할 때. / `stay visible even when there is nothing to look at` — 볼 것이 없어도 자리는 남긴다는 설계 원칙. / `one card per …` — `per` 로 대응 관계를 짧게 박는다.

**격식 짝**: (작성)
- refined: Every site is represented by a card, regardless of whether an image was captured for it.
- plain: Each site gets a card, image or no image.
- refined: Sites without images genuinely occur in the data, both in the mock and on site.
- plain: Sites with no image really do show up, in the mock and at the office.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>

---

## 단락 3

Tree is clean and everything from Friday is pushed (`a89a852`). Carryover is 2 days old (2026-09-19) — nothing shipped since, so the office list stands as written. Two at risk: the VLM checklist is a 30-second confirmation that's been carried three weeks — do it or drop it. Ticket 18 can't be *scheduled*, it waits on a real alarm, so it will keep aging; consider moving it out of "do first" into a standing watch item. It's the newest code, the only job whose blockers (…) clear directly from its output, and `a89a852` is unverified on real equipment — the longer it sits, the more work stacks on an unproven base. Want me to open `partial_hint.py` and the `_search_around` path in `correction.py` so the log lines are easy to map back, or are you starting on a different job?

**문법·구조**: 상태 보고라 관사와 be 동사가 곧잘 빠진다. `Tree is clean` 은 `The tree`, `Carryover is 2 days old` 는 `The carryover`, `Two at risk:` 는 `Two are at risk:` 를 줄인 헤드라인체다. 채팅에서는 자연스럽지만 메일이나 문서라면 관사를 살리자. `everything from Friday is pushed` 는 동작이 아니라 끝난 상태를 말하는 `be + 과거분사` 다. `that's been carried three weeks` 는 현재완료 수동에 기간을 붙였고 `for` 가 빠졌다. 넷째 문장의 이탤릭 `*scheduled*` 는 무엇을 강조할까? 날을 잡아 할 수는 없고 기다려야 한다는 대비다. 이 문장의 `can't be scheduled, it waits …` 는 쉼표로 두 문장을 붙인 comma splice 라 글에서는 세미콜론이 맞다. `consider moving` 도 챙겨 두자. `consider + -ing` 이지 `to` 부정사가 아니다. 다섯째 문장의 `It` 은 원문에서 바로 위 제목 `Recommendation: corner-key recovery run` 을 받는다. `whose blockers … clear` 의 `clear` 는 "(장애물이) 걷히다"는 자동사. 마지막의 `the longer …, the more …` 로 미룰수록 쌓이는 비용을 보여 주고 나서, 질문으로 결정을 상대에게 넘긴다. `Want me to …?` 는 `Do you want me to …?` 의 구어 축약이다. `so the log lines are easy to map back` 에서 쉼표 없는 `so` 는 목적("~하도록")을 나타낸다.

**핵심 표현**: `stands as written` — 적어 둔 목록이 지금도 유효하다. / `do it or drop it` — 미루기라는 세 번째 길을 막는 양자택일. / `Want me to …, or are you …?` — 제안과 다른 선택지를 한 질문에 담아 결정권을 넘긴다.

**격식 짝**: (작성)
- refined: The carryover dates from 19 September and nothing has shipped since, so the list remains valid as written.
- plain: The list is two days old and nothing's changed, so it still holds.
- refined: Shall I open `partial_hint.py` and the search path in `correction.py`, or would you prefer to start on another job?
- plain: Want me to pull up `partial_hint.py`, or are you doing something else first?

<sub>출처: transcript:[assistant] auto-recipe-creator</sub>
