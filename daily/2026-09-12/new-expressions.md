# 2026-09-12 — 새 표현

## "An untested path is where the two adapters quietly diverge."
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/recipe-tat/02-equipment-endpoints-400-tests.md
- 맥락: 테스트 없는 경로를 짚으며 왜 막아야 하는지 적을 때. 티켓·리뷰 코멘트의 문어체.
- 한국어: 테스트 안 된 경로가 바로 두 어댑터가 소리 없이 갈라지는 자리다.
- 설명: 핵심은 `quietly` 다. 오류는 안 나고 결과만 달라진다는 뜻이 이 한 단어에 들어 있다. `A is where B happens` 는 물리적 장소가 아니라 "위험이 터지는 지점"을 가리키는 관용 구문이다.
- 예문: The office adapter has no test for empty ranges, and an untested path is exactly where the mock and the real data quietly diverge.
- 유사어: silently drift apart (거의 같은 뜻, 조금 더 구어), fall out of sync (중립), diverge without anyone noticing (풀어 쓴 문어)
- 반의어: stay in lockstep, fail loudly

## "a failure mode a NamedTuple deletes at the type level"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/05-backend-shape-cleanups.md
- 맥락: 리팩터링 근거를 쓸 때. "조심하자"가 아니라 "구조로 없앤다"는 주장이라 설계 문서·리뷰에 잘 맞는다.
- 한국어: NamedTuple 이 타입 수준에서 아예 지워 버리는 실패 유형
- 설명: `delete` 의 목적어가 코드가 아니라 "실패 유형"이라서 인상이 강하다. 버그를 고치는 게 아니라 버그가 생길 여지를 없앤다. 관계절 앞 목적격 `that` 이 빠진 형태(`a failure mode (that) a NamedTuple deletes`)도 눈여겨볼 만하다.
- 예문: Swapping two positional fields is a failure mode a NamedTuple deletes at the type level.
- 유사어: rule out by construction (격식), make impossible to express (설계 글), a bug class the compiler catches (구어)
- 반의어: rely on convention, a hand-maintained invariant

## "judgement calls bundled by theme"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/tickets/dedup-refactors/05-backend-shape-cleanups.md
- 맥락: 리뷰 지적 여러 개를 티켓 하나로 묶으면서 성격을 먼저 밝히는 머리말. 문어.
- 한국어: 정답이 정해지지 않은 판단 문제들을 주제별로 묶었다.
- 설명: `judgement call` 은 규칙 위반이 아니라 재량으로 정할 문제다. 이렇게 밝혀 두면 받는 쪽이 반론해도 된다는 신호가 된다. `bundled by theme` 는 `that are bundled` 가 줄어든 과거분사 후치 수식이다. 철자는 영국식 judgement, 미국식 judgment.
- 예문: These three are judgement calls bundled by theme, not bugs, so feel free to push back on any of them.
- 유사어: grouped by topic (중립), style-level suggestions (가벼움), discretionary items (격식)
- 반의어: hard requirements, clear-cut defects

## "compares like with like"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (assistant, code-review 결과)
- 맥락: 비교하는 두 값의 조건이 같다고 확인해 줄 때. 통계·리뷰·일상 대화 어디든.
- 한국어: 같은 종류끼리 비교한다.
- 설명: 여기서 `like` 는 명사 "같은 것"이다. 공정한 비교를 뜻하는 고정 관용이고, 엉뚱한 비교를 뜻하는 `comparing apples to oranges` 의 반대편에 선다. 원문은 중복 id 를 제거한 목록끼리 길이를 비교하니 문제없다는 확인이었다.
- 예문: Both numbers exclude the warm-up requests, so the benchmark compares like with like.
- 유사어: an apples-to-apples comparison (미국 구어), a fair comparison (중립), on an equal footing (격식)
- 반의어: comparing apples to oranges

## "My recommendation is to leave it as is."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (assistant)
- 맥락: 리뷰에서 지적이 나왔지만 바꾸지 말자고 권할 때. 결론부터 말하는 보고.
- 한국어: 지금 그대로 두기를 권한다.
- 설명: `as is` 는 "현 상태 그대로"로, `as it is` 가 줄어든 꼴이다. 중고 거래의 `sold as is`(있는 그대로 판매)와 같은 뜻이다. `My recommendation is to V` 는 `I recommend V-ing` 보다 결론이 문장 앞에 더 또렷이 선다.
- 예문: The warning is harmless, so my recommendation is to leave it as is until the next dependency bump.
- 유사어: leave it alone (구어), keep it the way it is (중립), no change is warranted (격식)
- 반의어: rework it, revert it

## "Sending a key while the server has none does no harm."
- 레지스터: conversational, technical
- 출처: transcript:llm-serving (assistant)
- 맥락: 롤아웃 순서를 짜면서 이 단계는 먼저 해도 안전하다고 안심시킬 때.
- 한국어: 서버에 키가 없을 때 키를 보내는 건 아무 해가 없다.
- 설명: `do harm` 은 "해를 끼치다"이고 부정형은 `do no harm` 이다. 동명사구가 주어라 동사는 `does`. `none` 이 `no key` 를 대신 받아 반복을 피했다. 비슷한 `It doesn't hurt to V` 는 "해 봐서 손해 볼 건 없다"는 권유 쪽으로 기운다.
- 예문: Adding the header early does no harm, because the old server simply ignores it.
- 유사어: is harmless (중립), it doesn't hurt to V (구어, 권유), is a no-op (기술)
- 반의어: breaks things, does more harm than good

## "My earlier table was partly wrong for this route."
- 레지스터: professional, conversational
- 출처: transcript:llm-serving (assistant)
- 맥락: 새 사실이 드러나 앞서 한 내 설명을 스스로 고칠 때. 변명 없는 자기 정정.
- 한국어: 앞서 드린 표가 이 경로에는 일부 맞지 않았다.
- 설명: `partly` 로 틀린 범위를 좁히고 `for this route` 로 적용 범위를 한정했다. 전부 철회가 아니라 부분 수정이라는 게 한 문장에 드러난다. 원문은 `This also means …` 로 앞 사실에서 결론을 끌어낸다.
- 예문: I missed the login gate, which means my earlier advice was partly wrong for the code-server route.
- 유사어: I need to correct what I said earlier (정중), scratch part of that (구어), that needs a correction (격식)
- 반의어: that still holds, the diagnosis stands

## "Pick a quiet time."
- 레지스터: conversational, professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 재시작·배포 체크리스트의 준비 항목. 사용자가 적은 시간대를 고르라는 짧은 지시.
- 한국어: 한가한 시간대를 골라라.
- 설명: `quiet` 이 소리가 아니라 트래픽·업무량이 적다는 뜻이다. 명령문 한 줄로 끊고 이유는 바로 뒤 문장에 붙이는 게 체크리스트 문체다. 원문도 `Step 5 restarts all models …` 로 이유를 이었다.
- 예문: Pick a quiet time for the migration — the dashboard is down for about ten minutes.
- 유사어: schedule it off-peak (기술·중립), do it after hours (구어), during a maintenance window (운영·격식)
- 반의어: at peak hours, in the middle of the workday

## "The other way round, …"
- 레지스터: conversational, professional
- 출처: transcript:llm-serving (assistant)
- 맥락: 순서를 뒤집으면 무슨 일이 생기는지 대비해 보여줄 때.
- 한국어: 반대로 하면(순서가 거꾸로면) …
- 설명: 영국식 `the other way round`, 미국식 `the other way around`. 문두 부사구로 두면 "반대 경우에는"이 된다. `vice versa` 는 두 항을 맞바꿀 때만 쓰고, 이쪽은 순서·방향을 뒤집는 상황 전반에 쓴다.
- 예문: Restart Flask first and the models second; the other way round, every call fails with a 401 for a minute.
- 유사어: the other way around (미국식), conversely (문어·격식), if you flip the order (구어)
- 반의어: in this order, as planned

## "That way nobody gets locked out."
- 레지스터: conversational, technical
- 출처: transcript:llm-serving (assistant)
- 맥락: 단계 순서의 이유를 한 줄로 닫을 때. `That way` 가 앞 조치의 효과를 받는다.
- 한국어: 그러면 아무도 접근이 막히지 않는다.
- 설명: `get locked out` 은 원래 열쇠 없이 문밖에 갇힌다는 말인데, 계정·서비스 접근이 막히는 상황까지 넓게 쓴다. `get + 과거분사` 수동은 "그런 일을 당한다"는 느낌이 `be` 수동보다 세다.
- 예문: Hand out the new key before you enable auth. That way nobody gets locked out on Monday morning.
- 유사어: lose access (중립), be shut out (문어), can't get in (구어)
- 반의어: let someone in, keep access

## "Without this, every other improvement is guesswork."
- 레지스터: professional
- 출처: transcript:pm-notes (assistant)
- 맥락: 우선순위를 주장하면서 이것부터 해야 하는 이유를 댈 때. 설계·전략 문서.
- 한국어: 이게 없으면 다른 개선은 전부 짐작에 불과하다.
- 설명: `guesswork` 는 불가산 명사라 관사 없이 `is guesswork`. `every other` 뒤에는 단수 명사가 온다. 원문은 eval 을 먼저 만들라는 주장의 근거로 이 문장을 썼다.
- 예문: Set up evals before tuning prompts; without them, every other improvement is guesswork.
- 유사어: shooting in the dark (구어), unverified (격식), a hunch (구어·개인적)
- 반의어: backed by numbers, measurable

## "Every repeated mistake is a harness bug."
- 레지스터: technical, professional
- 출처: transcript:pm-notes (assistant)
- 맥락: 에이전트·자동화 운영 원칙을 격언처럼 한 줄로 말할 때.
- 한국어: 반복되는 실수는 모두 하네스의 버그다.
- 설명: 모델이나 사람 탓을 시스템 탓으로 옮기는 프레이밍이다. `Every X is a Y bug` 틀은 "그러니 구조로 고쳐라"까지 함축한다. `every` 뒤에는 단수 명사와 `is`.
- 예문: We treat every repeated mistake as a harness bug and add a check so the agent can't make it twice.
- 유사어: fix the system, not the person (격언), treat recurring errors as process defects (격식)
- 반의어: blame the model, chalk it up to bad luck

## "Checking that is what separates a safe reflow from a quietly broken page."
- 레지스터: professional
- 출처: transcript:pm-notes (assistant)
- 맥락: 결과를 가르는 결정적 한 가지를 짚을 때.
- 한국어: 안전한 줄바꿈과 소리 없이 깨진 페이지를 가르는 게 바로 그 점검이다.
- 설명: `what separates A from B` 는 A 와 B 를 구분 짓는 결정 요인이다. 동명사 주어 + `is what …` 은 주어를 강조하는 구문이고, `separate A from B` 의 전치사는 from 으로 고정이다.
- 예문: Testing the rollback before you need it is what separates a calm outage from a long night.
- 유사어: makes the difference between A and B (중립), is the dividing line between (격식), is the whole game (구어)
- 반의어: makes no difference

## "That fits what you asked for, but it's the one trade-off here."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (assistant)
- 맥락: 요청대로 구현했지만 대가가 하나 있다고 먼저 알릴 때.
- 한국어: 요청하신 방향에는 맞지만 여기서 감수할 점이 그 하나다.
- 설명: `the one X` 는 "유일한 X"를 강조한다. `the one trade-off` 라고 하면 이것 말고 손해 볼 건 없다는 말까지 된다. `fits what you asked for` 는 명사절 `what` 을 목적어로 받는다.
- 예문: New tools start unchecked. That fits the opt-in design, but it's the one trade-off here.
- 유사어: the only downside (중립), the price of this (구어), the sole compromise (격식)
- 반의어: a free win, no trade-offs at all

## "The TIFF→WebP conversion is sound."
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (assistant)
- 맥락: 진단 중에 의심 대상 하나를 배제할 때. "여기는 문제없다."
- 한국어: TIFF→WebP 변환은 제대로 되어 있다.
- 설명: 형용사 `sound` 는 "결함 없이 튼튼한"이다. `sound reasoning`, `structurally sound` 로도 쓴다. 원문은 `… is sound and is not what produces the blank tiles` 로 이어져 배제와 원인 지목을 한 문장에 담았다.
- 예문: The retry logic is sound; the blank tiles come from the grid, which never uses it.
- 유사어: works correctly (중립), holds up (구어), is well-founded (격식, 논리·근거에)
- 반의어: flawed, broken

## "That's expected, not a bug."
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt (assistant)
- 맥락: 이상해 보이는 동작이 설계대로라고 미리 알려 둘 때.
- 한국어: 그건 의도된 동작이지 버그가 아니다.
- 설명: `X, not Y` 대조 생략 구문이다. 문서에서 흔한 `This is expected behavior.` 의 구어판이고, 오해할 법한 지점에 먼저 박아 두면 문의가 줄어든다.
- 예문: At home the endpoint always returns 503 — that's expected, not a bug.
- 유사어: working as intended (격식), by design (중립), that's supposed to happen (구어)
- 반의어: a regression, unexpected behavior

## "This is exactly where the symptom lands."
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (assistant)
- 맥락: 결함이 있는 곳과 증상이 드러나는 곳이 겹친다고 설명할 때.
- 한국어: 증상이 드러나는 곳이 바로 여기다.
- 설명: `land` 는 "떨어져 닿다"라서 문제나 비용이 누구에게, 어디에 닿는지 말할 때 쓴다(`the cost lands on users`). 원문은 재시도 없는 그리드가 하필 HV-SEM 사용자가 쓰는 모드라는 점을 짚었다.
- 예문: Users on slow networks hit the timeout first, so that's exactly where the symptom lands.
- 유사어: shows up (구어), manifests (격식), where it bites (구어)
- 반의어: stays hidden

## "Only then fill in the key."
- 레지스터: professional, technical
- 출처: transcript:llm-serving (assistant) · repo:llm_serving docs/01-runtime-layout-and-capacity.md ("only then consider more aggressive runtime flags")
- 맥락: 절차의 마지막 단계를 앞 조건이 끝난 뒤에만 하라고 못박을 때.
- 한국어: 그다음에야 비로소 키를 채워라.
- 설명: 평서문 문두의 `only then` 은 도치를 부른다(`Only then did we notice …`). 명령문은 주어가 없어 도치 없이 `Only then fill in …` 으로 쓴다. 순서를 한 단어로 강조하는 장치다.
- 예문: Give every client the key first; only then turn auth on at the server.
- 유사어: not until then (강조, 약간 문어), after that and not before (구어·강조), subsequently (격식, 강조 없음)
- 반의어: right away, before anything else
