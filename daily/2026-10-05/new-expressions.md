# 2026-10-05 — 새 표현

> 오늘 배치는 repo 문서 17건과 transcript 15건이다. transcript 가운데 여섯은 `/clear`·`/model` 같은 명령만 찍힌 빈 세션이고 둘은 이 학습 파이프라인의 실행 기록이라 재료에서 뺐다. repo 문서는 pm_notes 의 문서 정리 기록·과거 설계와 skewnono 의 사무실 요청서·질문서로 거의 전부 한국어. 영어 산문은 pm_notes 의 `ai-terms-html-reader` 구현 계획 하나뿐이라 거기서 둘을 골랐다. 나머지는 skewnono 세션 셋에서 나왔다. recipe-status 페이지 캐시를 "되는가, 할 만한가"로 검토한 답과 사무실 요청서를 쓴 뒤의 보고, AFM 시계열 비교 페이지를 다시 만든 세션의 진행 메모와 마무리 보고, "커밋할 것이 없다"는 짧은 답. `leave-office` 스킬 문서에서도 하나 골랐다. 불릿으로 나뉜 원문은 앞의 도입 문장과 이어 붙여 예문으로 삼았고 긴 임시 경로는 파일명만 남겼다. 노트에 이미 있어서 뺀 것: `an open loop`, `a job that has been rotting`, `where my head was`, `fold in`, `a launchpad, not a diary`, `Specific beats complete.`, `exercise (a code path)`, `Reads cleanly in light mode.`, `line up with`, `fall through to`, `the culprit`, `dominate`, `spell out`, `progressive enhancement`.

## "before I give the verdict"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 조사 중간에 "결론은 조금 뒤에 내겠다"고 알릴 때(진행 보고, 구어와 문어 사이).
- 한국어: 결론을 내기 전에
- 설명: `verdict` 는 원래 배심원의 평결이고 일상에서는 "따져 본 끝에 내리는 판정"으로 쓴다. `opinion` 보다 조사하고 내린 결론이라는 무게가 있다. 바로 다음 메시지가 `Verdict: feasible, and worth it` 으로 시작해 이 예고와 짝을 이룬다.
- 예문: Still reading — I've traced the page's requests and the scheduler; two last checks (default fab scope on open, and whether we already write to Redis) before I give the verdict.
- 유사어: before I make a call (구어, 결정 쪽), before I draw a conclusion (격식), before I weigh in (의견을 보태는 정도)
- 반의어: jump to a conclusion (따져 보지 않고 단정하다)

## "That leaves X to pre-compute."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 경우를 하나씩 지우고 남은 일을 짚을 때(설계 설명·회의).
- 한국어: 그러면 남는 건 X 뿐이다
- 설명: `That leaves + 명사 (+ to부정사)`. `That` 은 앞 문장 전체를 받는다. 날짜도 디바이스도 변수가 아니니 미리 계산할 것은 장비 종류와 fab 조합뿐이라는 소거법의 마지막 줄이다. 결론을 `So we only need to …` 로 풀지 않고 "남은 것"을 목적어로 내민다.
- 예문: That leaves tool type × fab selection to pre-compute.
- 유사어: So all that's left is X (구어), What remains is X (격식), We're down to X (구어, 후보가 줄었다)

## "well under an hour"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 수치가 기준보다 넉넉히 작아야 한다고 말할 때(요구사항·설계 문서).
- 한국어: 한 시간보다 한참 짧은
- 설명: `well` 이 `under`, `over`, `above`, `below`, `before`, `after` 앞에서 "상당히"로 쓰인다. `under an hour` 는 59분도 되지만 `well under an hour` 는 여유가 넉넉해야 한다는 말. 숫자를 못 박지 않고 여유 폭만 요구할 때 편하다.
- 예문: An hourly job needs a lock lifetime well under an hour and its own minute slot.
- 유사어: comfortably under (여유를 강조), far below (차이가 크다), a fraction of (몇 분의 일 수준)
- 반의어: just under (아슬아슬하게 아래), well over (훌쩍 넘는)

## "a large share of"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 전체 중 큰 몫을 차지한다고 추정할 때(분석 보고, 중립).
- 한국어: ~의 큰 몫
- 설명: `share` 는 "몫". `most of` 라고 단정하기엔 근거가 모자라고 `some of` 는 약할 때 고른다. 앞의 `may` 와 합쳐져 "재 보지는 않았지만 꽤 클 것"이라는 수위가 된다.
- 예문: It may be a large share of the 10 seconds.
- 유사어: a big chunk of (구어), a significant portion of (격식), the bulk of (대부분, 더 강함)
- 반의어: a sliver of (아주 작은 조각), a negligible part of (무시할 만한 부분)

## "One design choice to confirm before you send it"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (사무실 요청서 보고)
- 맥락: 결과물을 넘기면서 상대가 확인할 결정 하나를 먼저 꺼낼 때(작업 보고·메일).
- 한국어: 보내기 전에 확인할 설계 결정이 하나 있다
- 설명: 동사 없이 명사구만 세우고 콜론 뒤에 내용을 푼다. `There is one design choice for you to confirm` 에서 앞을 덜어 낸 꼴이고 `to confirm` 은 `choice` 를 꾸미는 to부정사다. 콜론 뒤의 `ready-made` 는 "다 만들어져 바로 쓰는"이라는 형용사로, 재료 쪽인 `pre-aggregated` 와 맞선다.
- 예문: One design choice to confirm before you send it: the letter asks for a pre-aggregated table, not ready-made page results.
- 유사어: One thing to flag before you send it (구어에 가까움), One decision needs your sign-off first (격식), Heads-up on one choice I made (구어)

## "blocked on you sending the letter"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (leave-office 요약)
- 맥락: 일이 무엇을 기다리느라 멈춰 있는지 적을 때(인수인계·이슈 트래커).
- 한국어: 네가 편지를 보내야 풀리는
- 설명: `blocked on X` 는 "X 가 되어야 진행된다". `on` 뒤에 `you sending the letter` 처럼 의미상 주어가 붙은 동명사가 왔다. 격식 문어는 소유격 `your sending` 이지만 실무 글에서는 목적격 `you` 가 흔하다.
- 예문: Two are new today — the recipe-status cube (blocked on you sending the letter and the office reply) and the office log check on where the 10 seconds goes; nothing was closed.
- 유사어: waiting on you to send the letter (구어), pending your sending the letter (격식), held up until the letter goes out (풀어 쓴 말)
- 반의어: unblocked (풀렸다), good to go (바로 진행해도 된다)

## "distill this session into"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (leave-office 스킬 문서)
- 맥락: 긴 내용에서 알맹이만 뽑아 정리하라고 지시할 때(문서·지침).
- 한국어: 이 세션을 ~로 추려 내다
- 설명: `distill` 은 원래 "증류하다". `distill A into B` 는 A 를 졸여 B 만 남긴다는 그림이다. `summarize` 가 길이를 줄이는 일이라면 `distill` 은 걸러 내는 일에 가깝다. 뒤에 `and persist it` 가 붙어 "추리고 남긴다" 두 동작이 한 문장에 들어 있다.
- 예문: Distill this session into the work that is still open and persist it so the next session can continue without re-reading everything.
- 유사어: boil this session down to (구어), condense … into (중립), reduce … to its essentials (격식)
- 반의어: pad out (불필요하게 늘리다), write up in full (빠짐없이 다 적다)

## "because it would otherwise be wrong"
- 레지스터: professional
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 범위 밖의 수정을 하고 "안 고치면 틀린 내용이 남아서"라고 이유를 댈 때(보고).
- 한국어: 그대로 두면 틀린 내용이 되므로
- 설명: `otherwise` 가 "고치지 않았다면"이라는 가정을 한 단어로 받고, 그래서 `would` 가 온다. `if I hadn't rewritten it` 을 쓰지 않아도 가정법이 선다. 앞 절 `The breakpoints didn't change, but` 으로 "원래는 손댈 이유가 없었다"를 먼저 인정한 점도 볼 만하다.
- 예문: The breakpoints didn't change, but I rewrote one §Grid & Container sentence about this page because it would otherwise be wrong (it said "4/8").
- 유사어: since leaving it would make it wrong (풀어 쓴 말), or it'd be out of date (구어), lest it become inaccurate (아주 격식)

## "caught five bugs, all fixed before the commit"
- 레지스터: professional, technical
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 검증 단계에서 무엇을 잡았고 어떻게 처리했는지 한 줄로 보고할 때.
- 한국어: 버그 다섯 개를 잡았고 전부 커밋 전에 고쳤다
- 설명: 주어가 사람이 아니라 `The browser pass`(브라우저 점검 한 차례)다. `catch` 는 "놓치지 않고 잡아내다". 쉼표 뒤 `all fixed before the commit` 은 `all of which were fixed` 를 줄인 꼴로 처리 결과를 덧붙이는 자리다. 원문은 이 뒤에 콜론을 찍고 다섯 개를 나열한다.
- 예문: The browser pass caught five bugs, all fixed before the commit.
- 유사어: turned up five bugs (찾다 보니 나왔다), surfaced five bugs (드러났다, 문어), flagged five issues (표시해 올렸다)
- 반의어: missed (놓쳤다), slipped through (빠져나갔다)

## "reflects the remote as it is now"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (commit and push 답)
- 맥락: 방금 확인한 값이 최신 상태 기준임을 밝힐 때(상태 보고).
- 한국어: 지금 이 순간의 원격 상태 그대로다
- 설명: `as it is now` 는 "지금 있는 그대로". `the current remote` 보다 "예전에 받아 둔 정보가 아니라 방금 본 것"이라는 점이 산다. 앞 절 `I fetched before comparing` 이 근거이고 `so that reflects …` 가 결론. `that` 은 앞 문단의 판정을 받는다.
- 예문: I fetched before comparing, so that reflects the remote as it is now.
- 유사어: is up to date with the remote (흔한 말), matches the remote's current state (격식), is current as of just now (구어)
- 반의어: is based on a stale fetch (오래된 정보 기준이다)

## "If you expected changes here, they are not in this working tree"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (commit and push 답)
- 맥락: 상대의 기대와 실제가 다를 때 탓하지 않고 찾아볼 곳을 알려 줄 때(지원·보고).
- 한국어: 여기 변경이 있을 줄 아셨다면 이 작업 트리에는 없습니다
- 설명: `If you expected …` 는 가정법이 아니라 "혹시 그렇게 생각하셨다면"이라는 열린 조건이다. 그래서 주절이 현재형 `are not`. 대시 뒤에서 있을 만한 곳 두 군데를 대어 "없습니다"로 끝내지 않고 다음 수를 건넨다. `sitting in another checkout` 의 `sit` 은 "그냥 놓여 있다".
- 예문: If you expected changes here, they are not in this working tree — they may be unsaved in an editor or sitting in another checkout.
- 유사어: If you were expecting changes, I can't see any here (구어), Should you have anticipated changes, none are present here (격식)

## "remains legible without zooming"
- 레지스터: professional, technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 좁은 화면에서도 글이 읽혀야 한다는 검증 기준을 적을 때(계획서·QA 체크리스트).
- 한국어: 확대하지 않아도 읽힌다
- 설명: `legible` 은 글자가 물리적으로 판독된다는 뜻이고 `readable` 은 글이 술술 읽힌다는 쪽까지 넓다. `remain + 형용사` 는 조건이 바뀌어도 그 상태가 유지된다는 말이라 검증 항목에 잘 맞는다. 원문은 `Verify at 360px width:` 아래의 불릿이다.
- 예문: Verify at 360px width: body text remains legible without zooming.
- 유사어: stays readable (구어, 더 넓은 뜻), can be read at default zoom (풀어 쓴 말)
- 반의어: illegible (판독 불가), too small to read (너무 작아 못 읽는)

## "however many"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 개수를 아직 모르는 항을 그대로 두고 계산을 말할 때(구어, 가벼운 보고).
- 한국어: 몇 개가 되든 그만큼
- 설명: `however many + 명사` 는 "개수가 얼마든". 곱셈의 마지막 항이 미정이라는 사실을 숨기지 않고 그대로 적었다. 격식 글이라면 `N fab scopes` 나 `the number of fab scopes` 로 쓴다.
- 예문: OpenSearch load: the warm job runs about 9 endpoints × 2 tool types × however many fab scopes, every hour.
- 유사어: an unknown number of (격식), whatever number of (구어), N (문서에서 변수로)

## "Tell me which it is"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 두 갈래 중 어느 쪽인지 알려 달라고 할 때(구어, 동료 사이).
- 한국어: 어느 쪽인지 알려 줘
- 설명: 간접의문문이라 `which is it` 가 아니라 `which it is` 어순이다. `, plus the refresh minute` 로 필요한 것 하나를 더 얹고 `and I'll build the matching version` 으로 약속을 붙였다. "명령문 + and + I'll" 은 "~해 주면 ~하겠다"는 조건 틀.
- 예문: Tell me which it is, plus the refresh minute, and I'll build the matching version.
- 유사어: Let me know which one applies (조금 격식), Which one is it? (직접 묻기), Point me to the right one (구어)

## "are my picks"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (사무실 요청서 보고)
- 맥락: 근거가 깊지 않은 내 선택임을 밝히고 바꿔도 된다고 열어 둘 때(구어, 보고).
- 한국어: 내가 고른 값이다
- 설명: `pick` 은 명사로 "고른 것". `my decision` 보다 가볍고 "정답이라서가 아니라 내가 골랐다"는 뜻이 실린다. 세미콜론 뒤의 `change them … if you want different values` 가 그 짝이다.
- 예문: The 45-day window and 3-hour expiry are my picks; change them in the letter if you want different values.
- 유사어: are my defaults (기본값으로 잡았다), are what I went with (구어), are my proposed values (격식)
- 반의어: are fixed requirements (바꿀 수 없는 요구 사항이다)

## "start to finish"
- 레지스터: conversational
- 출처: transcript:skewnono-afm-trend ([user] 작업 지시)
- 맥락: 중간에 끊지 말고 끝까지 다 하라고 맡길 때(구어 지시).
- 한국어: 처음부터 끝까지
- 설명: `from start to finish` 에서 `from` 을 뗀 꼴로 쉼표 사이에 끼워 넣는 부사구. 관사가 없다. 이 지시문은 대시 앞뒤 두 토막이고 예문은 앞 토막이다. 뒤 토막은 아래 `make reasonable calls yourself` 에 있다.
- 예문: Read `AFM_TREND_BRIEF.md` and do everything it says, start to finish, without asking me questions.
- 유사어: from beginning to end (중립), end to end (기술 문맥, 전 구간), all the way through (구어)
- 반의어: partway (중간까지만), piecemeal (조금씩 나눠서)

## "make reasonable calls yourself"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-afm-trend ([user] 작업 지시)
- 맥락: 사소한 판단은 묻지 말고 알아서 정하라고 위임할 때(구어 지시, 업무 메모).
- 한국어: 적당한 판단은 네가 알아서 내려라
- 설명: `call` 은 심판의 판정에서 온 "그 자리에서 내리는 결정"이고 `make a call` 로 쓴다. 뒤에 `and record them` 을 붙여 결정은 맡기되 기록은 남기게 했다. 마무리 보고도 `Calls I made where the brief or spec was unclear` 라는 제목으로 이 지시를 받았다.
- 예문: Make reasonable calls yourself and record them in the report file it names.
- 유사어: use your judgment (가장 흔한 말), decide as you see fit (격식), wing it (캐주얼, 준비 없이 즉흥으로)
- 반의어: check with me first (먼저 물어봐라), escalate (위로 올려라)

## "I've got the full picture."
- 레지스터: conversational
- 출처: transcript:skewnono-afm-trend (진행 메모)
- 맥락: 조사가 끝나 전체를 파악했다고 알릴 때(구어, 진행 보고).
- 한국어: 전체 그림이 잡혔다
- 설명: `the picture` 는 "상황". `get the picture` 는 "알아듣다"이고 `the full picture` 는 빠진 조각 없이 다 안다는 말이다. `I've got` 은 현재완료 꼴이지만 뜻은 `I have`. 읽기만 하던 메모가 이 한 줄 뒤로 "이제 쓴다"로 바뀐다.
- 예문: I've got the full picture. Starting the worktree's Flask (:5051) and Nuxt (:3100) in the background while I write the utils.
- 유사어: I have everything I need (필요한 건 다 모았다), I see how it fits together (구조를 이해했다), I'm up to speed (따라잡았다)
- 반의어: I'm still piecing it together (아직 맞춰 보는 중이다)

## "in one shot"
- 레지스터: conversational
- 출처: transcript:skewnono-afm-trend (진행 메모)
- 맥락: 여러 번 나누지 않고 한 번에 해낸다고 말할 때(구어).
- 한국어: 한 번에, 한 방에
- 설명: `shot` 은 "시도 한 번"이자 "사진 한 장"이라 스크린샷 얘기에 꼭 맞는다. 앞 절은 왜 그렇게 하는지의 이유(`The app scrolls an inner container`)이고 `so I'll …` 로 조치를 이었다.
- 예문: The app scrolls an inner container, so I'll use a tall viewport to capture the whole page in one shot.
- 유사어: in one go (영국식 구어), in a single pass (기술 문맥), all at once (중립)
- 반의어: in pieces (조각조각), over several passes (여러 차례에 걸쳐)

## "it behaves"
- 레지스터: conversational
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 조건이 맞으면 문제없이 동작한다고 말할 때(구어, 보고).
- 한국어: 제대로 동작한다, 얌전하다
- 설명: 목적어도 부사도 없이 `behave` 만 쓰면 "말을 잘 듣는다". 아이에게 `Behave!` 라고 하는 그 동사를 수식에 썼다. 반대말 `misbehave` 도 코드에 그대로 쓴다. 뒤의 `as the screenshots show` 가 근거.
- 예문: With 6 or more measurements it behaves, as the screenshots show.
- 유사어: it works as expected (중립), it holds up (버틴다), it's well-behaved (형용사형)
- 반의어: it misbehaves (오동작한다), it acts up (구어, 말썽을 부린다)

## "fires four live requests"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 화면 동작 하나가 요청 몇 개를 내보내는지 설명할 때(성능 분석).
- 한국어: 실시간 요청 네 개를 쏜다
- 설명: `fire` 는 요청이나 이벤트를 "발사한다". `send` 보다 동작 하나에 여러 개가 한꺼번에 나간다는 느낌이 있다. 주어는 동명사구 `Opening the TAT tab`. `live` 는 캐시가 아니라 매번 실제로 조회한다는 형용사다.
- 예문: Opening the TAT tab fires four live requests: `ranking`, `summary`, `daily-trend` and `devices`.
- 유사어: sends four requests (중립), kicks off four requests (구어), issues four queries (격식)

## "still pay the 10 seconds"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 최적화를 했는데도 비용이 그대로 드는 경우를 짚을 때(성능 논의).
- 한국어: 여전히 10초를 치른다
- 설명: 시간과 지연을 돈처럼 `pay` 한다. `pay the cost`, `pay the latency` 와 같은 계열이다. 주어가 사람이 아니라 `most opens`(대부분의 열기)인 점도 영어답다. 앞의 `barely helps` 는 "거의 도움이 안 된다"는 준부정.
- 예문: A plain "cache on first request" layer barely helps a low-traffic internal page: with a 1-hour lifetime, most opens are the first of that hour and still pay the 10 seconds.
- 유사어: still take the full 10 seconds (중립), still eat the 10 seconds (구어), still incur the delay (격식)
- 반의어: get it for free (비용 없이 얻는다), hit the cache (캐시에 맞는다)

## "keeps it off the 00:05 reload"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (recipe-status 캐시 검토)
- 맥락: 작업 시간이 다른 작업과 겹치지 않게 한다고 설명할 때(스케줄 설계).
- 한국어: 00:05 재적재 시간대와 겹치지 않게 한다
- 설명: `keep A off B` 는 "A 가 B 위에 올라가지 않게 하다". 시간표에서 두 작업이 포개지지 않는다는 그림이다. 주어가 동명사구 `Restricting it to working hours` 라 "근무 시간으로 제한하면 ~된다"로 읽는다.
- 예문: Restricting it to working hours keeps it off the 00:05 reload and the quiet-window jobs.
- 유사어: keeps it clear of (피하게 한다), avoids colliding with (충돌을 피한다), steers it away from (멀리 돌린다)
- 반의어: lands on top of (정확히 겹친다), collides with (충돌한다)

## "at the finest grain"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (사무실 요청서 보고)
- 맥락: 집계 단위를 가장 잘게 잡는다고 말할 때(데이터 설계).
- 한국어: 가장 잘게 쪼갠 단위로
- 설명: `grain` 은 데이터 한 행이 나타내는 단위. `fine`(잘다)의 최상급 `finest` 를 붙였다. 콜론 뒤 `one row per day × fab × tool × recipe × lot` 이 그 단위의 정의다. 반대쪽 형용사는 `coarse`.
- 예문: Instead the letter asks for counts and sums at the finest grain: one row per day × fab × tool × recipe × lot.
- 유사어: at the lowest level of detail (풀어 쓴 말), at row-level granularity (격식), as granular as possible (구어)
- 반의어: at a coarse grain (굵은 단위로), rolled up (합쳐 올린)

## "cap the split count"
- 레지스터: technical
- 출처: transcript:skewnono-afm-trend (진행 메모)
- 맥락: 값에 상한을 걸겠다고 할 때(구현 메모).
- 한국어: 눈금 수에 상한을 건다
- 설명: `cap` 을 동사로 써서 "뚜껑을 씌우다", 곧 상한을 둔다는 말. `limit` 과 뜻은 같지만 위쪽만 막는다는 점이 분명하다. 세미콜론으로 증상(`labels overlap`)과 조치(`I'll cap`)를 이었다.
- 예문: Mileage axis labels overlap at 112px height; I'll cap the split count.
- 유사어: limit (중립), put a ceiling on (풀어 쓴 말), clamp (위아래를 다 막을 때)
- 반의어: lift the cap (상한을 푼다), leave it unbounded (제한 없이 둔다)

## "drops out of"
- 레지스터: technical
- 출처: transcript:skewnono-afm-trend (진행 메모)
- 맥락: 조건에 안 맞는 항목이 목록·차트에서 빠진다고 설명할 때.
- 한국어: ~에서 빠진다
- 설명: `drop out of` 는 스스로 떨어져 나간다는 자동사구. 누가 지운 것이 아니라 조건 때문에 저절로 빠진다. 사람이 주어면 "중퇴하다"가 된다. 예문의 `02` 는 화면의 둘째 카드 번호다.
- 예문: BSOX group works: the no-data file (TT032O0·02) shows its Summary stats with n "–" and drops out of 02 (stability says 5건).
- 유사어: is excluded from (수동, 격식), falls out of (비슷한 구어), is left out of (빠져 있다)
- 반의어: shows up in (나타난다), is included in (포함된다)

## "and nothing errored"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 실패했는데 에러가 하나도 안 났다는 점을 짚을 때(버그 보고).
- 한국어: 그런데 에러는 하나도 안 났다
- 설명: `error` 를 동사로 쓴 개발자 구어. 문장 끝에 `, and nothing errored` 를 덧붙여 "그래서 찾기 어려웠다"는 말을 대신한다. 격식 글에서는 `no error was raised`. `the tag I'd used` 의 `I'd` 는 `I had` 다.
- 예문: The 01 chart didn't render at all: Nuxt names the file `<AfmTrendChart>`, not the tag I'd used, and nothing errored.
- 유사어: it failed silently (가장 흔한 말), no error was raised (격식), without a peep (구어)
- 반의어: it threw (예외를 던졌다), it failed loudly (요란하게 실패했다)

## "pulls μ far enough to put every point outside the limits"
- 레지스터: technical
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 이상치 하나가 통계량을 끌고 가서 생기는 부작용을 설명할 때(분석 보고).
- 한국어: μ 를 끌고 가서 모든 점이 한계 밖에 놓인다
- 설명: `부사 + enough to부정사` 로 "…할 만큼 ~하게". 주어 `one big excursion`(크게 벗어난 값 하나)이 평균을 `pull` 한다는 그림이다. 앞 절의 `while` 은 시간이 아니라 대조(`μ is a plain mean while σ is outlier-resistant`).
- 예문: The spec's μ is a plain mean while σ is outlier-resistant, so in a very small group one big excursion pulls μ far enough to put every point outside the limits.
- 유사어: skews the mean so much that … (so … that 구문), drags the average off (구어), distorts the mean (격식)

## "is covered only by a unit test, not seen in the browser"
- 레지스터: technical, professional
- 출처: transcript:skewnono-afm-trend (시계열 비교 마무리 보고)
- 맥락: 검증 수준이 경로마다 다르다는 걸 밝힐 때(마무리 보고).
- 한국어: 단위 테스트로만 덮였고 브라우저에서 본 것은 아니다
- 설명: `covered by` 는 테스트가 그 경로를 지난다는 말. `only` 를 `by` 앞에 두어 "그것뿐"을 찍고 `, not seen in the browser` 로 빠진 쪽을 덧붙였다. 앞 절 `No group I could build contains a STOPPED block` 이 왜 못 봤는지의 이유다.
- 예문: No group I could build contains a STOPPED block, so the "블록 STOPPED" path is covered only by a unit test, not seen in the browser.
- 유사어: is unit-tested but not verified in the browser (풀어 쓴 말), has test coverage only (짧게), is untested end to end (전 구간으로는 미검증)
- 반의어: verified end to end (전 구간 확인), confirmed in the browser (브라우저에서 확인)

## "checked-in"
- 레지스터: technical
- 출처: repo:pm_notes docs/superpowers/plans/2026-07-28-ai-terms-html-reader.md
- 맥락: 생성물을 저장소에 커밋해 둔다는 점을 형용사로 밝힐 때(설계·계획 문서).
- 한국어: 저장소에 커밋해 둔
- 설명: `check in` 은 버전 관리에 넣는다는 동사구이고 하이픈을 넣으면 명사 앞 형용사가 된다. 빌드할 때마다 만들고 버리는 산출물과 달리 생성물도 저장소에 둔다는 결정이 이 한 단어에 들어 있다. 예문은 동사 셋(`parses`, `rewrites`, `generates`)을 나란히 놓은 문장이다.
- 예문: A standard-library Python builder parses the repository's current Markdown subset into semantic HTML, rewrites collection links, and generates one checked-in page per source document.
- 유사어: committed (가장 흔한 말), version-controlled (격식), tracked (git 용어)
- 반의어: generated at build time (빌드 때 생성되는), git-ignored (저장소에서 제외한)
