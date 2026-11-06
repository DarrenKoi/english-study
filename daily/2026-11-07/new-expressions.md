# 2026-11-07 — 새 표현

오늘 repo 문서(auto_recipe_creator 의 HF GUI VLM 조사 보고서)는 한국어로 쓰여 있습니다. 그래서 표현은 영어로 된 세 곳에서 골랐습니다. ARC 세션에서 어시스턴트가 낸 MAI-UI 교체 조사 결론, skewnono 서브에이전트에게 준 AFM 기능 지시서와 e-beam 페이지 조사 지시서, 그리고 지시서에 딸려 온 `tdd` 스킬 본문입니다. 결론을 먼저 말하고 근거의 한계를 밝히는 문장, 범위를 좁게 긋는 지시 문장이 많습니다.

## "a straight swap can at best tie"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator 59bde568 (MAI-UI 교체 조사 결론)
- 맥락: 교체 제안을 말릴 때, 기대 이득의 상한을 짚는 설명(회의·보고)
- 한국어: 그대로 바꿔 끼워 봐야 기껏해야 동점이다
- 설명: 원문은 `MAI-UI-8B already hits 100% on our internal benches, so a straight swap can at best tie.` 입니다. `straight swap` 은 다른 조정 없이 A를 B로 맞바꾸는 일이고 `at best` 는 "가장 잘 풀려도"입니다. 이미 만점이니 위로 갈 곳이 없다는 논리를 네 단어로 압축했습니다. `tie` 를 자동사로 써서 "비기다"가 됩니다.
- 예문: The current parser already passes every fixture, so a straight swap to the new library can at best tie.
- 유사어: the upside is capped (격식, 상한을 강조), there's nothing to gain (평이), it can only break even (손익 비유)
- 반의어: there's plenty of headroom

## "It is a long shot."
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator 59bde568 (Muse-Glimmer 통합안 평가)
- 맥락: 후보를 목록에 남기되 기대는 낮다고 선을 그을 때(회의·구어, 보고서 한 줄 평)
- 한국어: 가능성이 낮은 시도다, 밑져야 본전 수준이다
- 설명: 원래 사격·경마에서 "먼 거리 사격 = 맞힐 확률 낮음"이 어원입니다. 원문은 벤치 점수가 반복 crop 10회에 기대고 vLLM 0.28 이 필요하다고 이유를 다 댄 뒤 이 짧은 문장으로 판정을 닫습니다. 근거를 먼저, 판정은 짧게 두는 배치가 설득력을 줍니다.
- 예문: Merging all three roles into Muse-Glimmer would be ideal, but it is a long shot.
- 유사어: unlikely to pan out (조금 더 서술적), a Hail Mary (최후의 도박, 캐주얼), an outside chance (명사구, 격식 중립)
- 반의어: a safe bet, a sure thing

## "the only merge worth testing"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator 59bde568 (Merging roles 항목)
- 맥락: 여러 대안 중 시험할 가치가 있는 것을 하나로 좁힐 때(설계 검토·보고)
- 한국어: 시험해 볼 만한 유일한 통합안
- 설명: `worth + -ing` 가 명사 뒤에서 꾸미는 형태입니다(`the only merge (that is) worth testing`). 관계절을 줄여 짧게 만들었습니다. `the only` 가 나머지 안을 모두 기각한다는 뜻을 함께 싣습니다.
- 예문: Grounding into Qwen3.8 is the only merge worth testing, because we already serve that model.
- 유사어: the one option worth pursuing (조금 더 격식), the only one I'd bother trying (구어)
- 반의어: not worth the effort

## "scores are the authors' own; none were reproduced"
- 레지스터: professional, technical
- 출처: transcript:auto-recipe-creator 59bde568 (후보 표 머리말)
- 맥락: 남이 낸 수치를 인용하면서 검증하지 않았다고 밝힐 때(보고서 각주·조사 결과)
- 한국어: 점수는 저자 자체 보고값이며 재현한 것은 없다
- 설명: `the authors' own` 은 소유대명사처럼 쓰는 `one's own` 으로, "저자들이 직접 잰 것"을 강조합니다. 세미콜론 뒤 `none were reproduced` 는 수동태라 재현 주체(우리)를 지우고 사실만 남깁니다. 조사 보고서에서 신뢰 범위를 밝히는 정석 문장입니다.
- 예문: All latency figures below are the vendor's own; none were reproduced on our server.
- 유사어: self-reported figures (형용사형, 간결), as reported by the authors (각주 문체), we haven't verified these numbers (구어)
- 반의어: independently reproduced

## "comes close to 100%"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator 59bde568 (Next step)
- 맥락: 기준치에 "거의" 닿으면 다음 결정을 내리겠다는 조건을 걸 때(계획·회의)
- 한국어: 100%에 근접하다
- 설명: 원문은 `If Qwen comes close to 100%, we can retire the MAI-UI instance.` 입니다. `come close to` 는 정확히 닿지 않아도 충분하다는 여유를 남깁니다. 기준을 딱 잘라 `reaches 100%` 라고 하면 조건이 훨씬 빡빡해집니다.
- 예문: If the single-call mode comes close to the two-call accuracy, we can drop the fine stage.
- 유사어: gets within a point or two of (수치 구체), approaches (격식), is almost at (구어)
- 반의어: falls well short of

## "guesses unreadable text into something plausible"
- 레지스터: technical, professional
- 출처: transcript:auto-recipe-creator 59bde568 (OCR into Qwen: drop it)
- 맥락: 범용 모델이 OCR 에서 못 읽은 글자를 지어내는 위험을 설명할 때(설계 근거)
- 한국어: 읽을 수 없는 글자를 그럴듯한 무언가로 짐작해 채워 넣는다
- 설명: `guess` 는 보통 목적어 하나로 끝나는데 여기서는 `guess A into B` 로 써서 "짐작으로 A를 B로 바꿔 버린다"는 결과 구문을 만들었습니다(`talk him into it` 과 같은 틀). 따옴표로 "guesses" 를 감싸 모델이 의도적으로 추측한다는 의인화를 살짝 경계하는 점도 눈여겨볼 만합니다.
- 예문: A general VLM guesses a smudged tool ID into something plausible, and the confirm gate then approves the wrong row.
- 유사어: hallucinates a plausible reading (기술 용어), fills in the blanks (평이), confabulates (학술적)
- 반의어: reports it as unreadable

## "spend their token budget on reasoning instead of answering"
- 레지스터: technical
- 출처: transcript:auto-recipe-creator 59bde568 (thinking off 선행 작업)
- 맥락: thinking 모드를 끄지 않으면 짧은 호출이 낭비된다고 설명할 때(기술 문서·리뷰)
- 한국어: 토큰 예산을 답하는 데가 아니라 추론하는 데 써 버린다
- 설명: `spend A on B` 는 "B에 A를 쓰다"로 돈·시간·노력에 두루 씁니다. 토큰을 돈처럼 다루는 비유가 자연스럽게 맞아떨어집니다. `instead of + -ing` 로 원래 써야 할 곳을 바로 대비합니다.
- 예문: Without `enable_thinking=false`, short grounding calls spend their token budget on reasoning instead of answering.
- 유사어: burn through the token budget (구어, 소진 강조), exhaust the output limit before emitting coordinates (구체적 기술)
- 반의어: go straight to the answer

## "is the figure that says whether the tool is getting slower"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature A, Why)
- 맥락: 새 지표를 왜 넣는지 한 문장으로 정당화할 때(설계 근거·요구사항)
- 한국어: 장비가 느려지는지를 말해 주는 수치다
- 설명: 수치가 "말한다(says)"는 의인화로 지표의 쓸모를 정의합니다. `whether ... is getting slower` 는 진행형이라 추세(점점 느려지는가)를 묻습니다. 앞 문장 `cannot be compared on total duration` 이 문제를 깔고 이 문장이 해답 지표를 내놓는 구조입니다.
- 예문: Seconds per point, not total duration, is the figure that says whether the tool is getting slower.
- 유사어: the metric that tells you (구어), the measure that indicates (격식), the number to watch (간결)

## "use the one that section already has in hand"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature A, What)
- 맥락: 새로 가져오지 말고 이미 확보한 값을 쓰라고 지시할 때(작업 지시·리뷰)
- 한국어: 그 섹션이 이미 손에 쥐고 있는 것을 써라
- 설명: `have ... in hand` 는 "이미 확보해 둔"입니다. 컴포넌트를 사람처럼 "손에 쥔" 주체로 그려서 범위를 직관적으로 보여 줍니다. 바로 뒤 `do not fetch anything new` 가 같은 뜻을 금지문으로 한 번 더 박습니다.
- 예문: Don't call the detail API again; use the point list the page already has in hand.
- 유사어: already has on hand (거의 같음, 재고 뉘앙스), already loaded (기술적), already available (중립)
- 반의어: fetch it fresh

## "Rename that existing card so it says what it is"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature B, 1)
- 맥락: 이름이 실제 내용과 어긋날 때 이름을 내용에 맞추자고 할 때(UI 리뷰·회의)
- 한국어: 그 카드 이름을 바꿔 실제로 무엇인지 드러나게 하라
- 설명: `so (that) it says what it is` 는 목적절입니다. `say what it is` 는 "자기가 뭔지 스스로 밝힌다"는 짧고 단단한 구입니다. 단일 포인트 높이맵이 "웨이퍼 히트맵"이라는 이름을 달고 있어 오해를 부른다는 문제를 정면으로 고칩니다.
- 예문: The card shows one point's height map, so rename it so it says what it is.
- 유사어: give it an accurate name (평이), name it for what it shows (조금 문어), make the title match the content (설명적)
- 반의어: a misleading label

## "stay inside what it allows"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature A, What)
- 맥락: 기존 결정 문서가 허용한 범위 밖으로 나가지 말라고 할 때(작업 지시)
- 한국어: 그 문서가 허용하는 범위 안에 머물러라
- 설명: `what it allows` 는 명사절이고 `stay inside` 가 공간 비유로 경계를 만듭니다. 바로 뒤 `in particular do not present this as utilisation` 처럼 구체 금지 사항을 덧붙이는 흐름이 자연스럽습니다.
- 예문: Read the recommendation doc first and stay inside what it allows; anything beyond that needs a new decision.
- 유사어: stay within its scope (격식), don't go beyond what it permits (풀어쓰기), keep to what was agreed (회의체)
- 반의어: overstep, go beyond the brief

## "rejected as needing more data"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature A, OEE 금지)
- 맥락: 과거에 기각된 안과 그 이유를 괄호 하나로 남길 때(설계 문서·지시서)
- 한국어: 데이터가 더 필요하다는 이유로 기각됨
- 설명: `rejected as + -ing` 는 "~라는 이유로/~로 판정되어 기각된"입니다. 분사구문이라 주어와 be 동사가 빠졌고 괄호 속 메모에 딱 맞는 길이입니다. 같은 틀로 `dismissed as too costly`, `flagged as risky` 를 만들 수 있습니다.
- 예문: Uptime and OEE are out of scope (rejected as needing more data than the logs carry).
- 유사어: turned down for lack of data (평이), set aside pending more data (보류 뉘앙스, 격식)
- 반의어: approved, adopted

## "rather than a hand-built SVG if one fits"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Feature B, 2)
- 맥락: 기존 부품을 우선 쓰되 맞지 않을 때만 새로 만들라고 할 때(작업 지시·리뷰)
- 한국어: 맞는 게 있으면 손으로 짠 SVG 대신 그걸 써라
- 설명: `if one fits` 의 `one` 은 앞에 나온 `an existing chart/heat component` 를 받는 대명사입니다. `fit` 을 자동사로 써서 "용도에 맞다"는 뜻이 됩니다. 조건을 짧게 달아 강제가 아닌 우선순위로 만듭니다.
- 예문: Reuse an existing heatmap component rather than a hand-built SVG if one fits.
- 유사어: where possible (더 일반적), if there's a suitable one (풀어쓰기), when it does the job (구어)
- 반의어: build from scratch

## "Landed today on main"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Shared context)
- 맥락: 방금 병합된 변경을 알리고 건드리지 말라고 할 때(개발팀 구어·작업 지시)
- 한국어: 오늘 main 에 들어간(병합된)
- 설명: 변경이 브랜치에 "착륙한다(land)"는 비유는 개발자 사이에서 merge 보다 더 흔히 쓰입니다. 원문은 `Landed today on main, do not change their behaviour:` 로 주어를 빼고 분사로 시작해 머리말처럼 씁니다.
- 예문: The baseline fix landed on main this morning, so rebase before you start.
- 유사어: was merged into main (중립·격식), went in (구어), shipped (배포까지 포함한 뉘앙스)
- 반의어: was reverted, is still in review

## "do not treat any pattern seen at home as real"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (Shared context, mock)
- 맥락: 가짜 데이터에서 본 경향을 실제로 오해하지 말라고 경고할 때(작업 지시·분석 보고)
- 한국어: 집(mock 환경)에서 본 패턴을 진짜로 여기지 마라
- 설명: `treat A as B` 는 "A를 B로 취급하다"입니다. `seen at home` 은 과거분사구가 뒤에서 pattern 을 꾸밉니다. 앞 문장 `The mock's values are fabricated` 가 사실을, 이 문장이 행동 규칙을 맡는 2단 구성입니다.
- 예문: The mock's values are fabricated, so do not treat any trend you see in it as real.
- 유사어: don't read anything into (구어), don't draw conclusions from (중립), treat as illustrative only (격식)
- 반의어: take it at face value

## "survives refactors because it doesn't care about internal structure"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent aee64395 (tdd 스킬 본문)
- 맥락: 좋은 테스트의 조건을 설명할 때(테스트 원칙·코드 리뷰)
- 한국어: 내부 구조에 관심이 없기 때문에 리팩터링을 거쳐도 살아남는다
- 설명: 테스트를 생물처럼 `survive` 하는 주체로 씁니다. `doesn't care about` 은 구어 같지만 기술 글에서도 "의존하지 않는다"를 생생하게 전합니다. 반대 상황은 같은 글의 `the test breaks when you refactor but behavior hasn't changed` 입니다.
- 예문: A test that calls only the public function survives refactors because it doesn't care about internal structure.
- 유사어: is robust to refactoring (격식), doesn't break when you restructure the code (평이), is decoupled from implementation (기술 용어)
- 반의어: is brittle, breaks on every refactor

## "Which pages are thin (a table over raw data) versus analytic?"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a92bd579 (e-beam 페이지 조사, Key questions)
- 맥락: 기능의 깊이를 평가하는 축을 세울 때(제품 검토·조사 질문)
- 한국어: 어떤 페이지가 얇고(원자료 위에 표 하나) 어떤 페이지가 분석적인가?
- 설명: `thin` 은 "내용이 빈약한"입니다. 괄호로 정의를 즉석에서 붙여(`a table over raw data`) 모호함을 없앴습니다. `A versus B` 는 두 범주를 맞세워 분류 기준을 만듭니다. `over` 는 "원자료 위에 얹은"이라는 층위 비유입니다.
- 예문: Most of our dashboards are thin, a table over raw data, rather than analytic.
- 유사어: bare-bones (구어), shallow (조금 부정적), a data dump (비판적, 구어)
- 반의어: analytic, insight-driven

## "requires a maintainability case before adding cross-page links"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent a92bd579 (Constraints)
- 맥락: 변경 전에 정당화 논거를 먼저 내라고 요구할 때(설계 검토·조직 규칙)
- 한국어: 페이지 간 링크를 넣기 전에 유지보수성 논거를 요구한다
- 설명: `case` 는 "주장을 뒷받침하는 논거"입니다. `make a case for X` 가 기본형이고 여기서는 명사로 `a maintainability case` 처럼 앞에 관점을 붙였습니다. `a business case`, `a security case` 로 바꿔 쓰기 좋습니다.
- 예문: The owner requires a maintainability case before we add another shared filter.
- 유사어: a justification (평이), a business case (경영 문맥), make the argument for (구어)
- 반의어: add it without justification
