# 2026-10-03 — 정독

> 세 단락 모두 배치 원문이고 auto_recipe_creator 세션에서 돌아온 리뷰 보고서다. 단락 1은 Codex 가 "검출된 클릭 직후의 화면 변화는 버리자"는 설계에 반대하는 대목(Q2 전문). 단락 2는 Codex 코드 리뷰의 결함 보고 한 건으로, 맨 앞의 파일 위치와 `[P2]` 표시만 뗐다. 단락 3은 `/simplify` altitude 보고서에서 판정 둘째 문장, "Current form", "Concrete cost" 를 이어 붙였다. 절대 경로, 주석을 인용한 한국어 괄호, 오피스 패키지 규칙 한 문장은 뺐다.

## 단락 1

Hypothesis: a detected dropdown-open followed by a missed option selection within 1.5s loses the selection. grouping.py:179-206 explicitly supports open then select as a sequence. The transitive chain can suppress indefinitely while changes keep arriving, and closeness in time does not prove that the earlier action caused the change. Typing already has an explicit ownership mechanism (type_detect.py:311-315). The safer rule is to merge nearby observations for presentation but never delete one because an earlier action exists.

**문법·구조**: 첫 단어 `Hypothesis:` 가 이 단락의 검증 수준을 미리 알린다. 첫 문장은 주어가 길다. `a detected dropdown-open followed by a missed option selection within 1.5s` 까지가 전부 주어이고 동사는 `loses` 하나뿐. `detected`, `followed`, `missed` 는 모두 과거분사로 명사를 꾸민다. 시제는 끝까지 단순현재인데, 일어난 사건이 아니라 규칙이 어떻게 동작하는지를 말하기 때문이다. `can suppress indefinitely` 의 `can` 은 "그럴 수 있다"는 가능성. `while changes keep arriving` 은 "변화가 계속 들어오는 한"으로 `keep + -ing` 가 반복을 나타낸다. `and` 뒤 절은 무생물 `closeness in time` 을 주어로 세우고 `does not prove that …` 을 붙였다. that 절 안만 과거 `caused` 인 이유는 원인 행위가 먼저 일어난 일이라서. 마지막 문장 `The safer rule is to merge … but never delete …` 는 `be + to부정사` 보어에 동사 둘을 `but` 으로 묶었다. `one` 은 `an observation` 을 받는다. `never delete one because …` 는 "~라는 이유로 지우지는 마라"로, 부정이 `because` 절까지 덮는다. 비교급 `safer` 를 골라 상대 설계를 틀렸다고 하지 않고 더 안전한 쪽을 내놓았다.

**핵심 표현**: `explicitly supports open then select as a sequence` — 동사 원형 둘을 명사처럼 써서 조작 순서에 이름을 붙였다. / `closeness in time does not prove …` — 시간상 가깝다는 것과 원인이라는 것을 가른다. / `merge … for presentation` — 보여 줄 때만 묶고 데이터는 남긴다는 구분.

**격식 짝**: (작성)
- refined: Temporal proximity alone does not establish that the earlier action caused the change; nearby observations should therefore be merged for display, never discarded.
- plain: Just because it happened right after a click doesn't mean the click caused it, so group them and don't throw any away.

<sub>출처: transcript:auto_recipe_creator (Codex 설계 리뷰 Q2)</sub>

---

## 단락 2

A negative time gap is also merged, which inverts the observation interval. The call site does not guarantee time order. frame_reduce.py:50 sorts by filename lexically, and monitor/recording.py:234 stores the sequence number as `:04d`. Once a recording holds more than 9,999 frames, `10000` sorts before `1000`. Reproduced with the real collection and merge functions: `[500.0, 500.05, 50.0, 50.05]` merged into one observation with start 500.0 and end 50.05. Fix: sort by numeric sequence/time at the shared frame-collection point, and require `0 <= gap <= limit` in the merge condition. Add a test at the sequence-digit boundary.

**문법·구조**: 증상, 원인, 문턱, 재현, 수정, 테스트 순으로 일곱 문장이 흐른다. 버그 리포트의 표준 순서다. 첫 문장은 수동태 `is also merged` 로 무엇이 잘못 처리되는지를 주어에 세웠고, `, which inverts …` 의 `which` 는 앞 절 전체를 받아 결과를 붙인다. 둘째부터 넷째 문장은 코드의 성질을 말하므로 단순현재(`does not guarantee`, `sorts`, `stores`, `holds`). `Once a recording holds more than 9,999 frames` 의 `Once` 는 "일단 ~하면"이라 버그가 드러나는 문턱을 표시한다. 그 뒤 `sorts before` 는 `sort` 를 자동사로 썼다. 다섯째 문장은 `Reproduced with …:` 로 시작해 주어와 be 동사(`This was`)를 생략했다. 보고서에서 흔한 생략. 콜론 뒤 `merged` 는 과거 시제 자동사로, 실제로 한 번 돌려 본 결과라 과거다. `Fix:` 뒤는 명령문 셋(`sort`, `require`, `Add`)이 이어지고 `at the shared frame-collection point` 가 어디서 고칠지를 못 박는다. 호출부마다 고치지 말고 공통 지점 한 곳에서 고치라는 말.

**핵심 표현**: `The call site does not guarantee time order.` — 전제가 성립하지 않는다는 것을 한 문장으로. / `sorts by filename lexically` — 숫자가 아니라 글자로 정렬한다. / `Add a test at the sequence-digit boundary.` — 9,999 와 10,000 사이, 자릿수가 바뀌는 경계를 테스트 위치로 지정한다.

**격식 짝**: (작성)
- refined: Because frame filenames are ordered lexically and the sequence number is zero-padded to four digits, the ordering breaks once a recording exceeds 9,999 frames.
- plain: The files are sorted as text and the counter only has four digits, so frame 10000 ends up ahead of frame 1000.

<sub>출처: transcript:auto_recipe_creator (Codex 코드 리뷰 1차, 확정 결함 2)</sub>

---

## 단락 3

The optional-arg fix is the right mechanism, but it is half-applied. `manual_open_recipe.py:240-243` passes one call's inputs through two channels: `eqp_id` by argument, target by `os.environ["MANUAL_CLICK_TARGET"] = "file_manager"`. The comment on line 240 describes a forced argument, which is what a parameter is. The env write outlives the call. Any same-process caller that later runs `manual_click_button.main()` with a changed `TARGET` constant silently gets `file_manager`, because env beats the constant. That is the same "env silently overrides" class of bug this diff just fixed for `eqp_id`.

**문법·구조**: 첫 문장은 `is the right mechanism, but` 으로 옳은 점을 먼저 인정하고 한계를 뒤에 둔다. 둘째 문장의 콜론 뒤 `eqp_id by argument, target by …` 는 동사 없이 `by + 무관사 명사` 로 수단만 나란히 놓았다(`by email`, `by hand` 와 같은 틀). 셋째 문장 `, which is what a parameter is` 는 계속적 용법의 `which` 가 `a forced argument` 를 받고 그 안에 `what` 절이 들어 있다. "강제로 넘기는 인자, 그게 바로 매개변수"라는 말로 주석이 스스로 답을 말하고 있다고 꼬집는다. 넷째 문장은 다섯 단어뿐. 긴 문장 사이에 짧은 문장을 끼워 핵심(`outlives the call`)을 세웠다. 다섯째 문장은 주어가 길다. `Any same-process caller that later runs … with a changed TARGET constant` 까지가 주어이고 동사는 `gets`, 그 앞의 부사 `silently` 가 "오류 없이 조용히"를 맡는다. `because env beats the constant` 가 이유. 마지막 문장은 `class of bug (that) this diff just fixed` 로 관계사를 생략했고 `just fixed` 만 과거다. 나머지는 코드의 성질이라 현재, 이것만 방금 한 일이라서다.

**핵심 표현**: `passes one call's inputs through two channels` — 한 호출의 입력이 두 길로 간다는 문제 정의. / `The env write outlives the call.` — 쓴 값이 호출보다 오래 남는다. / `silently gets` — 예외 없이 엉뚱한 값을 받는다. (`X beats Y`, `the same class of bug` 는 노트에 이미 있다.)

**격식 짝**: (작성)
- refined: Writing to the environment has an effect that persists beyond the call, so a later caller in the same process may be silently redirected.
- plain: The env var sticks around after the call, so the next caller can end up with the wrong target without noticing.

<sub>출처: transcript:auto_recipe_creator (simplify 리뷰, altitude 보고서)</sub>
