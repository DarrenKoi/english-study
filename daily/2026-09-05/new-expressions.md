# 2026-09-05 — 새 표현

## "ordered by payoff per effort"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c (qwen3.8 지연 개선안)
- 맥락: 선택지를 여러 개 늘어놓기 전에 정렬 기준을 먼저 밝힐 때. 보고서·제안서의 첫 문단에 한 구로 붙인다.
- 한국어: 들인 노력 대비 효과가 큰 순으로
- 설명: payoff 는 "돌아오는 이득", per effort 는 "노력 단위당". 둘을 붙이면 ROI 를 말하되 돈 냄새를 뺀 표현이 된다. `ordered by` 뒤에 기준을 두는 틀은 어떤 목록에도 재사용된다.
- 예문: Here are the levers, ordered by payoff per effort, all grounded in the current config.
- 유사어: cheapest wins first (구어), in order of effort (노력 순만 말하고 효과는 안 말함), ranked by ROI (사업 문서)
- 반의어: in no particular order

## "a (prompt) hint, not a cap"
- 레지스터: technical
- 출처: transcript:llm_serving 1aaa1e3c / 86c08517
- 맥락: 설정값이 "권고"인지 "상한"인지 헷갈릴 때 성격을 못 박는 한 줄. 코드 리뷰·README 의 함정 경고에 어울린다.
- 한국어: 힌트일 뿐 상한이 아니다
- 설명: cap 은 "넘을 수 없는 뚜껑". 같은 뜻으로 `Effort is a prompt phrase, not a cap.` 도 같은 대화에 나온다. `X, not Y` 대조 틀은 오해가 예상되는 지점에서 먼저 선수를 치는 용도로 쓴다.
- 예문: Remember this is a prompt hint, not a cap — a hard cap needs `thinking_token_budget`.
- 유사어: advisory, not binding (격식), a suggestion rather than a limit (평이)
- 반의어: a hard cap, a hard limit

## "silently ignored"
- 레지스터: technical
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 설정이 오류도 없이 그냥 무시되는 함정을 경고할 때. 문서의 "주의" 상자에 가장 자주 나오는 부사+분사 조합이다.
- 한국어: 아무 경고 없이 무시된다
- 설명: silently 가 핵심이다. 실패는 소리를 내야 정상인데, 조용하면 사용자가 성공으로 착각한다. 그래서 `silently` 뒤에는 ignored / dropped / truncated 같은 손실 동사가 온다.
- 예문: Without that flag the budget is silently ignored, and only a re-tokenized count reveals it.
- 유사어: swallowed (더 구어, 예외를 삼킨다), quietly dropped (같은 뜻, 조금 부드러움)
- 반의어: fails loudly, rejected with an error

## "Nothing to gain here until X is fixed"
- 레지스터: professional, conversational
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 선택지 하나를 "지금은 손댈 가치가 없다"고 접을 때. 이유가 외부 의존성(툴체인·버그)일 때 특히 잘 맞는다.
- 한국어: X 가 고쳐지기 전엔 여기서 얻을 게 없다
- 설명: 주어 없는 `Nothing to gain` 은 메모체다. `here` 로 범위를 그 항목에 묶고 `until` 로 재개 조건을 붙여, 포기가 아니라 보류라는 걸 전한다.
- 예문: Nothing to gain here until the CUDA toolchain issue is fixed.
- 유사어: this is a dead end for now (더 구어), no upside until … (약간 사업체)
- 반의어: this is where the win is

## "the single largest lever available"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 여러 개선안 중 하나를 "최대 효과"로 지목할 때. 비용이 큰 안을 추천할 때 앞에 붙이면 설득력이 산다.
- 한국어: 지금 쓸 수 있는 것 중 가장 큰 지렛대
- 설명: `single` 은 largest 를 한 번 더 조여 "단연"의 어감을 준다. lever 는 이 대화 전체에서 "돌릴 수 있는 손잡이"란 뜻으로 반복된다. `available` 을 뒤에 붙여 "현실적으로 가능한 범위 안에서"로 한정한다.
- 예문: FP8 weights is the single largest decode-speed lever available.
- 유사어: the biggest win on the table (구어), the highest-impact option (중립)
- 반의어: a marginal gain

## "This is a judgment question, so no code."
- 레지스터: conversational, professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 질문이 구현이 아니라 판단을 묻는다는 걸 첫 줄에서 밝혀, 답의 형식을 미리 예고할 때.
- 한국어: 판단을 묻는 질문이니 코드는 안 쓴다
- 설명: `judgment question` 은 "정답이 아니라 저울질이 필요한 질문". `so no code` 처럼 동사를 뺀 후반부는 회화체 메모의 리듬이다. 답의 종류를 먼저 선언하면 읽는 쪽이 기대를 조정한다.
- 예문: This is a judgment question, so no code — here is the honest trade-off.
- 유사어: this is a call, not a calculation (구어), this comes down to judgment (평이)
- 반의어: this is a mechanical change

## "and this is the big one"
- 레지스터: conversational
- 출처: transcript:llm_serving 1aaa1e3c (TP=2 단점 목록)
- 맥락: 목록 항목 여럿 중 하나를 "이게 진짜다"라고 찍을 때. 항목 제목 뒤에 삽입구처럼 붙인다.
- 한국어: 그리고 이게 제일 큰 문제다
- 설명: 항목이 열거되면 가중치가 평평해진다. 이 한 마디가 그 평평함을 깨서 독자의 시선을 한 곳에 모은다. 격식 문서면 `the decisive drawback` 이 되지만, 회화체 보고에서는 이 쪽이 훨씬 자연스럽다.
- 예문: Qwen loses isolation, and this is the big one.
- 유사어: this is the one that matters (조금 더 차분), the deal-breaker (강함, 결정적 결격)
- 반의어: a minor point

## "Nothing else moves."
- 레지스터: technical, conversational
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 변경 범위를 열거한 뒤 "그 밖엔 전부 그대로"라고 닫을 때. 설정 변경·마이그레이션 안내에서 마지막 줄로 쓴다.
- 한국어: 나머지는 하나도 안 바뀐다
- 설명: move 를 "바뀌다·자리를 옮기다"로 쓴 것. 세 단어짜리 완전한 문장이라 독자가 변경 목록을 다 읽었다는 안도감을 준다.
- 예문: Qwen goes to both GPUs and mai-ui drops to 0.40. Nothing else moves.
- 유사어: everything else stays as is (평이), all other settings are untouched (격식)
- 반의어: this touches every env file

## "My read"
- 레지스터: conversational
- 출처: transcript:llm_serving 1aaa1e3c (소제목)
- 맥락: 장단점을 다 늘어놓은 뒤 자기 의견으로 넘어가는 소제목·첫 두 단어. 회의에서 "제 생각엔"의 짧은 버전.
- 한국어: 내 판단은 / 내가 보기엔
- 설명: read 를 명사로 써서 "읽어 낸 결과". `My take` 와 거의 같지만 read 는 상황을 "판독했다"는 느낌이 있어 근거를 댄 뒤에 더 어울린다.
- 예문: My read: if the complaint is thinking tokens, the client knobs beat TP=2 with zero risk.
- 유사어: my take (같은 뜻, 더 흔함), where I land (결론에 무게), in my assessment (격식)
- 반의어: the numbers say (개인 판단이 아니라 데이터 주장)

## "If any one of them is false, ..."
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 조건 여러 개가 모두 참이어야 하는 결정을 마무리할 때. 앞 문장 `If all three are true` 와 짝을 이룬다.
- 한국어: 셋 중 하나라도 거짓이면
- 설명: `any one` 을 띄어 쓰면 "하나라도"가 강조된다(`anyone` 은 사람). all/any 대비를 두 문장으로 나눠 놓으면 AND 조건이 눈에 보인다.
- 예문: If all three are true it is a good trade. If any one is false, keep the current layout.
- 유사어: unless all three hold (한 문장 압축, 격식), if even one fails (더 구어)
- 반의어: as long as most of them hold

## "measured, not guessed"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 결정 근거가 추정이 아니라 실측이라는 걸 강조할 때. 메모리·기록의 목적을 설명하는 자리에 잘 붙는다.
- 한국어: 재서 정했지 짐작이 아니다
- 설명: 과거분사 두 개를 `not` 으로 맞세운 최소 구성. 앞에 `so the gate is` 를 붙이면 "기준이 실측으로 잠겼다"는 뜻이 된다. 같은 대화에 `Both gates are now recorded with the measured numbers` 가 이어진다.
- 예문: Recording the number so the gate is measured, not guessed.
- 유사어: evidence-based (격식·추상), grounded in numbers (중립)
- 반의어: a ballpark figure, back-of-the-envelope

## "put X in play"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 어떤 행동이 잠자던 위험 요소를 "작동 가능 상태"로 만든다고 경고할 때.
- 한국어: X 를 개입시키다, X 가 끼어들게 만들다
- 설명: 스포츠에서 공이 살아 있는 상태가 in play. `put ... in play` 는 그 상태를 만드는 원인을 주어로 세운다. 여기서는 TP=2 기동이 OOM killer 를 깨운다는 뜻이다.
- 예문: With 4 GB free and no swap, a TP=2 launch would put the OOM killer in play at startup.
- 유사어: trigger (직접적), invite (위험을 불러들인다는 어감), bring X into the picture (중립)
- 반의어: keep X out of the picture

## "Anything that adds X is out."
- 레지스터: conversational
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 제약 하나가 확정된 뒤 그 제약에 걸리는 선택지 전체를 한 문장으로 제외할 때.
- 한국어: X 를 늘리는 건 전부 제외
- 설명: `is out` 은 "탈락"의 구어체. 주어를 `anything that ...` 로 세워 개별 항목이 아니라 부류 전체를 자른다. 뒤에 `Everything left runs inside ...` 처럼 남는 것을 이어 주면 구조가 완성된다.
- 예문: Anything that adds a host process is out. Everything left runs inside the existing qwen process.
- 유사어: is off the table (같은 뜻, 조금 더 격식), doesn't qualify (중립)
- 반의어: is still on the table

## "so it isn't re-asked next session"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 결정을 기록하는 이유를 밝힐 때. 문서화의 목적이 "다시 묻지 않게"임을 짧게 말한다.
- 한국어: 다음 세션에서 다시 묻지 않도록
- 설명: `re-ask` 는 사전보다 실무에서 먼저 굳은 단어다. 수동태 `isn't re-asked` 로 누가 묻는지를 지워 절차 자체를 주어로 삼는다.
- 예문: Recording that so it isn't re-asked next session.
- 유사어: so we don't relitigate it (더 강함, 논쟁을 재개하지 않도록), to avoid asking twice (평이)
- 반의어: left open for next time

## "Reading "X" as: ..."
- 레지스터: professional
- 출처: transcript:llm_serving 86c08517
- 맥락: 모호한 지시를 자기 해석으로 바꿔 선언한 뒤 실행할 때. 되묻는 대신 해석을 밝히고 진행하는 방식이다.
- 한국어: "X" 를 이렇게 이해하고 진행합니다
- 설명: 주어 없는 현재분사 도입부는 작업 로그 문체다. 인용부호 안에 원래 단어를 두고 `as:` 뒤에 자기 해석을 풀어 쓰면, 나중에 해석이 틀렸을 때 어디서 갈렸는지 바로 찾을 수 있다.
- 예문: Reading "amend" as: the real-path fallback was a workaround, and the pod restart fixed the cause, so the tree goes back to placeholders.
- 유사어: I take "X" to mean ... (완전한 문장), interpreting "X" as ... (같은 구조, 조금 더 격식)
- 반의어: taking "X" literally

## "to the same effect"
- 레지스터: professional
- 출처: transcript:llm_serving 86c08517
- 맥락: 원래 하려던 방법이 막혀 다른 수단을 썼지만 결과는 같다고 보고할 때.
- 한국어: 같은 결과가 나도록
- 설명: effect 는 "효과·결과". 수단이 달라도 결과가 동일하다는 걸 이 한 구가 보장한다. `with the same result` 보다 격식이 한 단계 높고, 법·계약 문장에도 자주 나온다.
- 예문: A plain `git checkout` was blocked, so the revert was done with in-place edits to the same effect.
- 유사어: with the same outcome (평이), achieving the same end (격식)
- 반의어: with a subtly different result

## "per your standing preference"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 이미 정해 둔 사용자 규칙을 따랐다고 짧게 밝힐 때. 매번 확인하지 않는 이유를 한 구로 댄다.
- 한국어: 평소 정해 두신 대로
- 설명: standing 은 "상시 유효한"(standing order, standing rule). `per` 는 "~에 따라"의 격식 전치사. 두 단어가 합쳐져 "일회성 지시가 아니라 늘 적용되는 원칙"임을 전한다.
- 예문: Not committed, per your standing preference.
- 유사어: as usual (구어, 원칙이란 뉘앙스 없음), in line with your default (중립)
- 반의어: on your one-off instruction

## "Go direct, not through the proxy"
- 레지스터: technical
- 출처: transcript:llm_serving 86c08517
- 맥락: 네트워크 경로를 고를 때 중간 계층을 건너뛰라고 지시하는 짧은 명령문.
- 한국어: 프록시 말고 직접 붙어라
- 설명: `go direct` 는 부사 direct 를 쓴 관용 표현(directly 도 되지만 짧은 쪽이 명령문에 맞다). `not through ...` 로 제외할 경로를 뒤에 달아 두 경로를 한 줄에 대비한다.
- 예문: Go direct, not through the Flask proxy, for xhigh: the proxy buffers fully with a 300s read timeout.
- 유사어: hit the port directly (구어), bypass the proxy (중립)
- 반의어: route it through the proxy

## "X does not remove the need for Y"
- 레지스터: professional
- 출처: repo:llm_serving docs/01-runtime-layout-and-capacity.md
- 맥락: 큰 자원 하나가 다른 자원의 필요성을 없애 주지 않는다는 흔한 오해를 바로잡을 때.
- 한국어: X 가 있다고 Y 가 필요 없어지는 건 아니다
- 설명: `remove the need for` 는 "필요를 없애다"의 정형구. 부정문으로 쓰면 "여전히 필요하다"를 우회적으로, 그러나 단호하게 말한다. 문서 절의 첫 문장으로 두면 뒤에 오는 목록의 존재 이유가 된다.
- 예문: Large GPU VRAM does not remove the need for host RAM.
- 유사어: does not make Y unnecessary (평이), Y is still required regardless (직설)
- 반의어: renders Y unnecessary

## "not truly ready until both pass"
- 레지스터: professional
- 출처: repo:llm_serving docs/02-model-bringup-and-special-settings.md
- 맥락: 검증 기준 두 개를 세운 뒤 "둘 다 통과해야 완료"라고 못 박는 마무리 문장.
- 한국어: 둘 다 통과하기 전엔 진짜 준비된 게 아니다
- 설명: truly 가 "형식상 ready" 와 "실제 ready" 를 가른다. `until both pass` 는 조건을 숫자로 못 박아 한쪽만 확인하고 넘어가는 습관을 막는다.
- 예문: The model is not truly ready until both pass.
- 유사어: only counts as ready when ... (평이), ready in name only (반대쪽을 지적할 때)
- 반의어: good enough once health responds

## "an operational interpretation, not a claim that ..."
- 레지스터: professional
- 출처: repo:llm_serving docs/02-model-bringup-and-special-settings.md
- 맥락: 표에 적은 역할 배정이 공식 스펙이 아니라 운영 경험에서 나온 배치임을 밝힐 때. 과장 책임을 피하는 문서 어법이다.
- 한국어: 운영상의 해석이지, ~라는 주장이 아니다
- 설명: interpretation 과 claim 을 맞세워 "우리가 이렇게 쓴다"와 "원래 그렇게 정해져 있다"를 구분한다. `not a claim that` 뒤에는 완전한 절이 온다.
- 예문: This is an operational interpretation, not a claim that the model cards guarantee those exact roles.
- 유사어: a working assumption (평이), a practical reading rather than a specification (풀어쓰기)
- 반의어: a documented guarantee

## "an always-call-everything pipeline"
- 레지스터: technical
- 출처: repo:llm_serving docs/04-operations-integration-and-benchmarking.md
- 맥락: 안전하다고 모든 모델을 매번 다 부르는 설계를 비판적으로 이름 붙일 때.
- 한국어: 매번 전부 다 호출하는 파이프라인
- 설명: 구 전체를 하이픈으로 묶어 형용사로 만드는 영어 특유의 조어법. 이름을 붙이면 나쁜 설계가 하나의 "종류"가 되어 피하기 쉬워진다.
- 예문: Keeping sidecars off at first avoids building an always-call-everything pipeline.
- 유사어: a kitchen-sink pipeline (구어, "다 때려 넣은"), calling every model on every request (풀어쓰기)
- 반의어: a gated cascade, escalate-only-on-failure

## "the weak spot"
- 레지스터: conversational, professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (Ultralytics 문서 인용)
- 맥락: 전체적으로는 괜찮은 도구·모델의 취약한 한 지점을 지목할 때. 문서의 Limitations 절 문장이다.
- 한국어: 약점, 취약한 곳
- 설명: `weakness` 보다 구체적인 "자리"를 가리킨다. 주어를 대상으로 두고 `is the weak spot` 으로 닫는 문장은 한 줄 요약으로 강하다.
- 예문: Rare categories are the weak spot.
- 유사어: the Achilles' heel (더 극적), where it falls down (구어)
- 반의어: the strong suit

## "they never abstain"
- 레지스터: technical
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (프리프린트 초록 인용)
- 맥락: 모델·분류기가 "모르겠다"를 출력하지 못하는 성질을 지적할 때. 학술·기술 문장에서 fail-closed 논의와 붙어 다닌다.
- 한국어: 기권을 모른다, 항상 답을 내놓는다
- 설명: abstain 은 투표에서 기권하듯 "판단을 유보하다". 이 성질이 있으면 자신감 있는 오답이 쏟아진다. 초록에서는 `because they never abstain, every tile floods robust estimation with thousands of confident matches` 로 인과를 잇는다.
- 예문: A naive tiling pyramid degrades matchers badly, because they never abstain.
- 유사어: cannot say "I don't know" (평이), always produces an answer (중립)
- 반의어: degrade to unknown, fail closed

## "This applies even if you ..."
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (Ultralytics 라이선스 FAQ 인용)
- 맥락: 규칙에 예외가 없음을 예상 가능한 반론을 미리 열거하며 못 박을 때. 라이선스·정책 문서의 어법이다.
- 한국어: 다음 경우에도 마찬가지로 적용된다
- 설명: `even if` 뒤에 독자가 "나는 해당 안 되겠지" 하고 떠올릴 조건들을 일부러 나열한다. 빠져나갈 구멍을 하나씩 닫는 글쓰기다.
- 예문: This applies even if you train your own model from scratch or use YOLO only internally.
- 유사어: regardless of whether you ... (격식), no exceptions for ... (직설)
- 반의어: unless you ...

## "Notwithstanding any other provision of this License"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (AGPL-3.0 §13 인용)
- 맥락: 계약·라이선스에서 "다른 조항이 뭐라 하든 이 조항이 우선한다"고 여는 정형구. 읽을 줄 알면 되고 쓸 일은 드물다.
- 한국어: 이 라이선스의 다른 어떤 조항에도 불구하고
- 설명: notwithstanding 은 "~에도 불구하고"의 법률체 전치사(= despite). 뒤에 오는 문장이 예외·우선 규정임을 알리는 신호라, 이 단어가 보이면 그 조항을 따로 읽어야 한다.
- 예문: Notwithstanding any other provision of this License, if you modify the Program, your modified version must offer all users interacting with it remotely an opportunity to receive the Corresponding Source.
- 유사어: despite anything else in this agreement (평이한 법률체), overriding the rest of the licence (풀어쓰기)
- 반의어: subject to the other provisions (다른 조항에 종속된다)

## "a small but significant gain"
- 레지스터: professional
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (프리프린트 초록 인용)
- 맥락: 효과 크기는 작아도 통계적으로 유의하다고 보고할 때. 논문 초록의 정형구이며 p 값이 바로 뒤에 따라온다.
- 한국어: 작지만 유의한 향상
- 설명: small 과 significant 가 모순처럼 보이지만 significant 는 "통계적으로 우연이 아니다"란 전문 의미다. 기술 보고서에서 이 구를 쓰면 독자는 "실용적 가치는 따로 판단하라"는 신호로 읽는다.
- 예문: A redesigned coarse-to-fine wrapper recovers a small but significant gain (SR@10 0.10→0.12, p = 0.017).
- 유사어: a modest but reliable improvement (비통계 문맥), statistically significant yet practically minor (풀어쓰기)
- 반의어: a large but noisy gain

## "X clears the precondition"
- 레지스터: professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 사전 조건 여러 개 중 하나가 확인됐다고 알릴 때. 남은 조건을 `One gate is left` 로 이어 붙인다.
- 한국어: X 로 그 전제 조건은 통과됐다
- 설명: clear 를 "장애물을 넘다"의 타동사로 쓴 것(clear a hurdle). 조건을 관문(gate)에 비유하는 이 대화의 어휘 체계와 맞물린다.
- 예문: NVLink clears the interconnect precondition, so TP=2 is now a real option. One gate is left: host RAM.
- 유사어: satisfies the requirement (격식), ticks that box (구어)
- 반의어: fails the precondition

## "the wall the whole repo is built around"
- 레지스터: conversational, professional
- 출처: transcript:llm_serving 1aaa1e3c
- 맥락: 프로젝트 전체의 설계를 규정한 핵심 제약 하나를 가리킬 때.
- 한국어: 이 저장소 전체가 그 벽을 피해서 지어졌다
- 설명: wall 은 넘을 수 없는 한계. `built around` 는 "그것을 중심에 두고 짓다"와 "그것을 피해서 짓다"의 두 뜻이 겹쳐 제약이 설계의 중심이었음을 한 구에 담는다. 관계절에서 전치사 around 가 뒤에 남는 구어적 구조다.
- 예문: The host has 16 GB and no swap. This is the wall the whole repo is built around.
- 유사어: the constraint that shaped every decision (풀어쓰기·격식), the hard limit behind all of this (평이)
- 반의어: a soft limit we can negotiate

## "you cannot put the target into words"
- 레지스터: conversational
- 출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (YOLOE 문서 인용)
- 맥락: 텍스트 프롬프트가 아니라 예시 이미지가 필요한 이유를 설명할 때. 기술 문서지만 관용구라 일상 대화에도 그대로 쓴다.
- 한국어: 찾는 대상을 말로 표현할 수 없다
- 설명: `put X into words` 는 "말로 옮기다"의 관용구. 감정에도 쓰지만(I can't put it into words) 여기서는 분류 라벨을 붙일 수 없는 대상을 가리킨다.
- 예문: Use visual prompts when you cannot put the target into words: a specific part, logo, or defect.
- 유사어: hard to name (짧음), defies description (격식·과장)
- 반의어: easy to label
