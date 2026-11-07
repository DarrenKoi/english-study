# 2026-11-08 — 새 표현

오늘 배치는 skewnono 대화 네 개입니다. 메인 세션은 사무실 에이전트와 질문지·회신을 여섯 번 주고받으며 device-statistics 계열 표를 고친 기록이고, 나머지 셋은 서브에이전트 지시서(AFM 측정 항목 간 관계, skewvoir 조사)입니다. 앞 문서 부분은 한국어라 표현은 어시스턴트의 영어 보고와 지시서에서 골랐습니다. 실수를 스스로 바로잡는 문장, 추측과 사실을 가르는 문장, 범위를 좁히는 지시 문장이 많습니다.

## "you can paste the file as-is"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (질문지 작성 보고)
- 맥락: 손대지 말고 그대로 넘기면 된다고 안내할 때(업무 메신저·구어)
- 한국어: 파일을 그대로 붙여 넣으면 된다
- 설명: 원문은 `Like the earlier sheets, it has no file paths or commit hashes, so you can paste the file as-is.` 입니다. `as-is` 는 "있는 그대로, 고치지 않고"라는 부사입니다. 앞에 왜 그대로 써도 되는지(경로·해시가 없다)를 먼저 대고 `so` 로 결과를 붙였습니다. 계약서의 `sold as-is`(하자 보증 없이 현 상태로)도 같은 말입니다.
- 예문: The script has no machine-specific paths, so you can run it as-is on the office laptop.
- 유사어: use it unchanged (조금 더 격식), drop it in as is (구어, "그냥 끼워 넣어"), verbatim (문자 그대로, 텍스트 한정)
- 반의어: it needs adapting first

## "without any error"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (3차 회신 반영 보고, Most urgent 항목)
- 맥락: 버그가 조용히 틀린 결과를 낼 때, 그 위험을 강조하는 보고(글·회의)
- 한국어: 에러 하나 없이 (틀린 채로 돈다)
- 설명: 원문은 `it reads the whole index, back to 2022, without any error.` 입니다. 에러가 안 난다는 사실을 안심 요소가 아니라 경고로 썼습니다. 날짜 형식이 달라 90일 창이 통째로 사라졌는데 아무도 모르게 돌았다는 점이 이 버그의 무서운 부분이라 문장 끝에 둬서 강조합니다.
- 예문: The migration skipped half the rows without any error, which is why nobody noticed for a week.
- 유사어: silently (가장 흔한 개발자 표현, `fails silently`), with no warning (평이), quietly (구어, 약간 문학적)
- 반의어: fails loudly, throws right away

## "were measured with the window broken"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (3차 회신 반영 보고)
- 맥락: 앞서 받은 숫자를 믿을 수 없는 이유를 짚을 때(보고·글)
- 한국어: 창이 고장 난 상태에서 잰 것이다
- 설명: 원문은 `That also means the N4 numbers (57,145 → 57,179, 513 → 516 devices) were measured with the window broken.` 입니다. `with + 명사 + 과거분사` 는 부대상황 구문으로 "~가 …된 상태로"입니다. 절을 하나 더 만들지 않고(`while the window was broken`) 세 단어로 조건을 붙여 문장이 가볍습니다.
- 예문: Those benchmark numbers were taken with the cache disabled, so they overstate the latency.
- 유사어: under the broken window (조금 어색, 비권장), while the window was broken (절로 풀어쓴 평이형), were taken before the fix (구어)
- 반의어: were measured after the fix

## "That's my guess; the office didn't say."
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (4차 회신 반영, V4 해석)
- 맥락: 내 해석이 확인된 사실이 아님을 짧게 밝힐 때(보고·구어)
- 한국어: 그건 제 추측입니다. 사무실은 말하지 않았어요.
- 설명: 앞 문장에서 "raw"와 "화면"을 어떻게 읽었는지 밝힌 뒤 바로 이 문장으로 확신의 수준을 표시합니다. `didn't say` 는 목적어 없이 "명시하지 않았다"는 뜻으로 자주 씁니다. 세미콜론으로 두 짧은 절을 이어 "추측 ↔ 근거 부재"가 한 호흡에 읽힙니다.
- 예문: I assumed the timestamps are KST; that's my guess, the spec didn't say.
- 유사어: this is my interpretation, not confirmed (격식), I'm inferring this (중립), I'm reading between the lines (구어)
- 반의어: the office confirmed it

## "When fab doesn't settle it"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (3차 회신 반영, S2/S3)
- 맥락: 1차 기준으로 결정이 안 날 때 쓰는 보조 규칙을 적을 때(설계 글·계약 주석)
- 한국어: fab 으로 결정이 안 나면
- 설명: 원문은 `When fab doesn't settle it, the adapter takes the newest document; that rule is written in the contract's docstring.` 입니다. `settle` 은 논쟁·문제를 "결판내다, 매듭짓다"라는 뜻이고 여기서 `it` 은 "어느 파라미터 세트를 고를지"라는 문제 자체입니다. 질문지에도 `the 7 cases that fab alone doesn't settle` 로 나옵니다. tie-break 규칙을 설명할 때 바로 쓰기 좋습니다.
- 예문: If the timestamp doesn't settle it, fall back to the lowest document ID.
- 유사어: break the tie (동점 깨기, 구어·기술), decide it (평이), resolve the ambiguity (격식)
- 반의어: leaves it open

## "That one is a counting artifact"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (fab_name 전환 중 테스트 실패 설명)
- 맥락: 테스트·지표가 어긋난 원인이 실제 버그가 아니라 세는 방식 때문일 때(코드 리뷰·구어)
- 한국어: 그건 세는 방식에서 생긴 착시다
- 설명: `artifact` 는 측정·처리 과정이 만든 가짜 신호입니다(이미지의 압축 artifact 와 같은 말). 원문은 바로 이어 `a lot spans several fab_names` 로 원인을 대고 테스트가 distinct `lot_cd` 를 세야 한다고 고칩니다. 실패를 보고 "버그 아님"을 먼저 선언하고 근거를 붙이는 흐름입니다.
- 예문: The spike on Monday is a reporting artifact; the dashboard double-counts retries.
- 유사어: a side effect of how we count (평이), a measurement artifact (격식), not a real regression (구어, 결론만)
- 반의어: a real regression, a genuine bug

## "My helper landed between `_lot_bridge` and its cache decorator."
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (3차 회신 반영 중)
- 맥락: 내가 넣은 코드가 엉뚱한 위치에 들어간 실수를 스스로 알릴 때(작업 중 진행 보고)
- 한국어: 제가 넣은 헬퍼가 `_lot_bridge` 와 그 캐시 데코레이터 사이에 끼어 들어갔습니다
- 설명: `land` 는 "도착하다, 떨어지다"에서 나와 코드가 어떤 자리에 들어갔다는 뜻으로 씁니다. 의도치 않은 결과라는 뉘앙스가 있어 `I put it` 보다 담담합니다. 뒤에 `Fixing the order:` 를 붙여 실수 보고와 조치를 한 줄로 끝냅니다.
- 예문: The new import landed inside the `if TYPE_CHECKING` block, so it fails at runtime.
- 유사어: ended up (구어, "결국 ~에 가 있었다"), got inserted (수동, 중립), slipped in between (실수 뉘앙스 강조)
- 반의어: (마땅한 반의 표현 없음)

## "This corrects how I recorded S3 last round."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (4차 회신 반영, T3/T4)
- 맥락: 지난번 내 기록이 틀렸음을 담백하게 인정할 때(보고·글)
- 한국어: 지난 회차에 S3 를 기록한 방식을 이것으로 바로잡습니다
- 설명: 주어를 `I was wrong` 대신 `This`(이번 변경)로 세워 사과보다 수정 사실에 초점을 둡니다. `how I recorded` 는 명사절이라 "무엇을 틀렸는지"를 정확히 짚습니다. `last round` 는 질문지를 회차로 주고받는 맥락에 맞는 말입니다.
- 예문: This corrects how I described the retry policy in yesterday's update.
- 유사어: this supersedes my earlier note (격식), I got S3 wrong last time; this fixes it (구어, 직접 인정), correction to the previous round (제목형)
- 반의어: this confirms what I recorded

## "Because `fab_name` is finer than `fac_id`"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (fab_name 전환 보고)
- 맥락: 키·분류 단위의 세밀함을 비교해 하나를 빼는 이유를 댈 때(설계 글)
- 한국어: `fab_name` 이 `fac_id` 보다 더 잘게 나뉘므로
- 설명: 원문은 `Because fab_name is finer than fac_id, adding fac_id wouldn't separate anything further.` 입니다. `fine` 은 "가는, 촘촘한"이라 `finer` 는 단위가 더 세분된다는 뜻입니다(`fine-grained`, `finer granularity`). 뒤 절의 `wouldn't separate anything further` 는 가정법으로 "넣어 봐야 더 가르는 게 없다"를 말합니다.
- 예문: Because the hourly bucket is finer than the shift, grouping by shift adds nothing.
- 유사어: more granular (격식), more fine-grained (기술 글에서 흔함), more specific (평이)
- 반의어: coarser than

## "so the mock's numbers stay the same"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (2차 회신 반영, R8)
- 맥락: 시드 고정 mock 을 고칠 때 다른 값이 흔들리지 않음을 보장할 때(PR 설명·보고)
- 한국어: 그래서 mock 숫자는 그대로다
- 설명: 원문은 `It makes the same number of random draws as before, so the mock's numbers stay the same.` 입니다. 난수를 뽑는 횟수가 같아야 시드 고정 난수열이 밀리지 않는다는 핵심을 한 문장에 담았습니다. `stay the same` 은 `remain unchanged` 의 구어형입니다.
- 예문: The new field reuses the existing draw, so every other generated value stays the same.
- 유사어: remain unchanged (격식), don't shift (구어), are unaffected (중립)
- 반의어: shift, drift

## "random variation in the long tail"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (5차 회신 반영, W2)
- 맥락: 시뮬레이션 값이 목표와 어긋난 이유가 분포 꼬리의 우연임을 설명할 때(보고)
- 한국어: 긴 꼬리 쪽의 무작위 변동
- 설명: 원문은 `VeritySEM is low because of random variation in the long tail; the generator itself averages close to the target.` 입니다. `long tail` 은 드물지만 큰 값이 길게 늘어진 분포 꼬리입니다. 세미콜론 뒤 `the generator itself` 로 "개별 실행은 흔들려도 생성기 자체는 맞다"를 구분해 줍니다.
- 예문: The p99 jumped because of a few outliers in the long tail, not a general slowdown.
- 유사어: sampling noise (기술, 짧음), luck of the draw (구어), outliers (원인을 개별 값으로 지목)
- 반의어: a systematic bias

## "Saving this to memory so it sticks for later sessions"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (fab_name 규칙 메모리 저장)
- 맥락: 결정을 기록해 다음에도 유지되게 하겠다고 알릴 때(구어·작업 보고)
- 한국어: 다음 세션에도 남도록 메모리에 저장합니다
- 설명: `stick` 은 "들러붙다"에서 나와 "(기억·결정이) 남다, 정착하다"는 뜻입니다. `so (that) it sticks` 는 목적의 `so` 절이고 `that` 을 생략한 구어형입니다. `the name stuck`(그 이름이 굳어졌다)처럼도 씁니다.
- 예문: I'll add it to the README so the convention sticks for new hires.
- 유사어: so it carries over (다음으로 넘어감 강조), so it persists (기술·격식), so we don't lose it (구어)
- 반의어: so it gets forgotten, it won't stick

## "Expected failure (old assumption)."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt e6aa6018 (2차 회신 반영 중)
- 맥락: 테스트가 빨갛게 떴지만 의도된 결과임을 바로 알릴 때(작업 로그·구어)
- 한국어: 예상한 실패입니다(옛 가정 때문)
- 설명: 동사 없는 명사구 보고입니다. 괄호 속 `old assumption` 이 "테스트가 옛 사실을 아직 믿고 있다"는 원인을 두 단어로 줍니다. 이어 `Updating the tests to the new facts.` 로 조치를 붙입니다. 진행 로그는 이렇게 짧게 끊어 써도 자연스럽습니다.
- 예문: Expected failure: the test still asserts the old 15% skip rate.
- 유사어: red as expected (TDD 구어), the test is out of date (원인 강조), that one's supposed to fail (회화)
- 반의어: an unexpected failure, a surprise regression

## "Clearly separate facts from your own inferences."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 a282d5 (skewvoir 조사 지시)
- 맥락: 조사·보고를 맡기며 사실과 추론을 구분해 달라고 할 때(지시서·격식)
- 한국어: 사실과 본인의 추론을 분명히 구분하세요
- 설명: `separate A from B` 는 "A를 B와 떼어 놓다"입니다. `inference` 는 근거로부터 끌어낸 추론이라 `opinion`(의견)이나 `guess`(추측)보다 무게 있는 단어입니다. `your own` 을 넣어 "원문이 말한 것"과 "네가 덧붙인 것"의 경계를 강조합니다.
- 예문: In the incident write-up, clearly separate what the logs show from your own inferences.
- 유사어: distinguish fact from interpretation (격식), flag what you're guessing (구어), mark anything unverified (실무)
- 반의어: blend speculation into the findings

## "Be dense and factual"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 a282d5 (skewvoir 조사 지시)
- 맥락: 보고서를 군더더기 없이 정보 위주로 써 달라고 요청할 때(지시서)
- 한국어: 빽빽하고 사실 위주로 쓰세요
- 설명: 원문은 `Be dense and factual; quote short load-bearing snippets only.` 입니다. `dense` 는 사람에게 쓰면 "둔하다"는 욕이지만 글에 쓰면 "밀도 높다"는 칭찬입니다. 이 차이를 기억해 두면 좋습니다. 형용사 두 개로 문체 요구를 끝내는 간결한 명령문입니다.
- 예문: Keep the summary dense and factual; skip the background we already know.
- 유사어: be concise and concrete (격식), no fluff (구어), stick to the facts (평이)
- 반의어: be verbose, pad it out

## "cannot be asked"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 ad6032 (AFM 측정 항목 간 관계 지시)
- 맥락: 지금 화면·도구로는 어떤 질문 자체를 던질 수 없다며 기능의 필요를 설명할 때(기획 글)
- 한국어: (그런 질문은) 던질 수조차 없다
- 설명: 원문은 `Today every chart on the screen looks at one column at a time, so "do left and right move together or is there an asymmetry?" and "does this value drift as the tip accumulates mileage?" cannot be asked.` 입니다. 사용자가 품을 질문 두 개를 따옴표로 직접 주어 자리에 세우고 수동태로 닫았습니다. "기능이 없다"보다 "이 질문을 못 한다"가 필요를 더 생생하게 보여 줍니다.
- 예문: With only daily totals in the report, "which hour did the spike start?" cannot be asked.
- 유사어: there's no way to answer (평이), is out of reach (중립), the screen can't tell you (구어)
- 반의어: can be answered at a glance

## "nothing new needs fetching"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 ad6032 (AFM 측정 항목 간 관계 지시)
- 맥락: 기능 범위가 프론트에서 끝나고 새 데이터 요청이 필요 없음을 밝힐 때(지시서·설계)
- 한국어: 새로 가져올 것이 없다
- 설명: 원문은 `The data is already loaded for the group; nothing new needs fetching.` 입니다. `need + -ing` 는 수동 의미입니다(`needs fetching` = `needs to be fetched`). 영국식 느낌이 조금 있고 짧아서 지시서에 잘 맞습니다. 앞 절이 사실, 뒤 절이 그 귀결이라 세미콜론이 자연스럽습니다.
- 예문: The page already holds every row it needs; nothing new needs fetching.
- 유사어: no extra requests are required (격식), no new API calls (기술 구어), it's all on the client already (구어)
- 반의어: needs a new endpoint

## "an observed relation in a hand-picked group"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 ad6032 (AFM 관계 지시, Wording 항목)
- 맥락: 통계 결과를 인과·일반 결론처럼 읽히지 않게 선을 그을 때(분석 보고·UI 문구 지침)
- 한국어: 손으로 고른 묶음에서 관찰된 관계
- 설명: 원문은 `Wording: this is an observed relation in a hand-picked group.` 이고 바로 `No "correlated therefore", no regression line presented as a model, no pass/fail.` 이 이어집니다. `observed` 는 "본 것이지 증명한 것이 아니다", `hand-picked` 는 "무작위 표본이 아니다"를 각각 담아 두 단어로 일반화를 막습니다.
- 예문: Treat the trend as an observed relation in a hand-picked set of lots, not as a rule.
- 유사어: a correlation in this sample only (격식), what we saw in these runs (구어), an anecdotal pattern (약간 깎아내리는 뉘앙스)
- 반의어: a causal effect, a general finding

## "beyond what falls out for free"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt 466cd9af 서브에이전트 ad6032 (AFM 관계 지시, Out of scope)
- 맥락: 다른 작업의 부산물로 저절로 생기는 것 외에는 손대지 말라고 범위를 그을 때(지시서)
- 한국어: 저절로 따라 나오는 것 이상으로는 (하지 마라)
- 설명: 원문은 `export changes beyond what falls out for free.` 입니다. `fall out` 은 "결과로 자연히 생겨나다", `for free` 는 "추가 노력 없이"입니다. 개발자들이 `this falls out of the design`(설계에서 저절로 나온다)처럼 자주 씁니다.
- 예문: Don't build a CSV export; take whatever falls out for free from the table component.
- 유사어: comes for free (구어), is a by-product (중립), happens as a side effect (기술)
- 반의어: needs dedicated work
