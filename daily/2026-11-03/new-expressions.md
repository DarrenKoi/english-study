# 2026-11-03 — 새 표현

## "display-only"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (skewvoir 품질 지표 작업 지시)
- 맥락: 화면에 보여 주기만 하고 판정·계산에는 쓰지 않는 값이라고 선을 그을 때(설계 문서·작업 지시)
- 한국어: 표시 전용의, 보여 주기만 하는
- 설명: 하이픈으로 묶은 복합 형용사라 명사 앞에 바로 붙습니다(display-only axes). 뒤에 "they must not feed X" 같은 금지 문장을 붙여 경계를 구체화하는 경우가 많습니다.
- 예문: These axes are display-only: they must not feed the anomaly verdict or any warning colour.
- 유사어: informational only (조금 더 평이), read-only (편집 불가라는 뜻이라 범위가 다름), for reference only (문서·표에서)
- 반의어: load-bearing (판단을 실제로 떠받치는), part of the judgement path

## "lets the engineer look; it must not decide for them"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (작업 지시 "Why" 절)
- 맥락: 도구는 근거를 보여 줄 뿐 결정은 사람이 한다는 설계 원칙을 한 문장으로 밝힐 때(문어)
- 한국어: 엔지니어가 볼 수 있게 할 뿐, 대신 판단해서는 안 된다
- 설명: 세미콜론 앞뒤로 "허용/금지"를 대구로 놓았습니다. `decide for someone` 은 "남 대신 결정하다"라는 뜻이고, 짧은 동사 look 과 대비되어 도구의 역할이 작게 그려집니다.
- 예문: The overlay lets the engineer look; it must not decide for them.
- 유사어: inform, not judge (압축형), surface the evidence and leave the call to the user (풀어 쓴 판)
- 반의어: make the call automatically

## "the first question is "did X, or did Y?""
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (작업 지시 "Why" 절)
- 맥락: 이상이 생겼을 때 실무자가 맨 먼저 묻는 질문을 그대로 인용해 기능의 필요를 설득할 때
- 한국어: 맨 먼저 드는 질문은 "X 인가, Y 인가?" 이다
- 설명: 질문을 직접 인용문으로 넣어 독자를 현장에 세웁니다. 두 갈래 의문문(did A or did B)이 진단의 분기점을 그대로 보여 줍니다.
- 예문: When a CD value moves, the first question is "did the measurement itself degrade, or did the wafer change?"
- 유사어: the obvious thing to ask is (회화), the first thing to rule out is (진단 중심)

## "manufactured by the generator"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Hard constraints)
- 맥락: mock 데이터에서 보이는 상관관계가 실제가 아니라 생성기가 만든 것이라고 경고할 때
- 한국어: 생성기가 지어낸(인위적으로 만든)
- 설명: manufacture 는 원래 "공장에서 만들다"입니다. 데이터 맥락에서는 "실재하지 않는데 만들어 낸"이라는 부정적 어감이 붙습니다(a manufactured crisis).
- 예문: Any score-to-CD relation you see at home is manufactured by the generator, not found in the data.
- 유사어: an artefact of the generator (격식, 통계 글에 흔함), baked in by the mock (회화), synthetic (중립)
- 반의어: observed in real data

## "rest on"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Other constraints — "they rest on mock-invented nominals")
- 맥락: 어떤 값·주장이 무엇을 근거로 서 있는지, 그 근거가 약하다고 짚을 때
- 한국어: ~에 근거하다, ~을 바탕으로 서 있다
- 설명: 수동적인 "based on" 보다 기반 위에 얹혀 있다는 그림이 선명합니다. 근거가 무너지면 위의 것도 무너진다는 함의가 있어 "왜 쓰지 말아야 하나"를 설명하기 좋습니다.
- 예문: Do not show the drift status anywhere new; it rests on nominals the mock invented.
- 유사어: be based on (평이), hinge on (한 가지 조건에 달림), be grounded in (격식·긍정적)

## "If, and only if,"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Scope 3번 슬라이스)
- 맥락: 조건이 맞을 때만, 그리고 맞을 때는 반드시 하라는 엄격한 조건을 걸 때(지시문·명세)
- 한국어: ~인 경우에만, 그리고 오직 그 경우에
- 설명: 수학의 iff 를 문장으로 쓴 것입니다. 쉼표로 "and only if" 를 끼워 넣어 "그 외에는 하지 말라"를 강조합니다. 지시문에서는 보통 뒤에 "If it has no such mechanism, skip this" 처럼 반대 경우를 따로 적습니다.
- 예문: If, and only if, the chart already supports an extra lane, add the score as an optional series.
- 유사어: only when (평이), provided that (격식, 강도 약함), on the condition that (계약서 투)

## "stop after any slice that turns out larger than a modest addition"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Scope)
- 맥락: 작업 범위가 예상보다 커지면 멈추고 보고하라는 안전장치를 걸 때
- 한국어: 생각보다 커지는 슬라이스가 있으면 거기서 멈춰라
- 설명: `turn out + 형용사 비교급` 은 "해 보니 ~로 드러나다". 미리 알 수 없는 크기를 조건으로 삼는 표현이라 위임 지시에 잘 맞습니다. modest 는 "적당한, 크지 않은".
- 예문: Stop after any slice that turns out larger than a modest addition, and tell me what you found.
- 유사어: if it grows beyond a small change, pause (평이), if the scope balloons, stop (회화)

## "exactly what is interesting"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Scope 1번 — 실패 행 처리)
- 맥락: 버리기 쉬운 데이터가 오히려 핵심이라고 뒤집어 말할 때
- 한국어: 바로 그게 흥미로운(봐야 할) 부분이다
- 설명: exactly 가 "다른 게 아니라 바로 그것"을 강조합니다. 앞에 "a failed measurement's score" 처럼 버려질 법한 대상을 주어로 두면 반전 효과가 납니다.
- 예문: A failed measurement's score is exactly what is interesting, so do not drop those rows without saying so.
- 유사어: precisely the point (격식), the whole point (회화), the part worth looking at (평이)

## "decide and state whether"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Scope 1번)
- 맥락: 판단을 위임하되 그 판단을 반드시 밝히라고 요구할 때(작업 지시·리뷰 요청)
- 한국어: ~할지 정하고, 정한 것을 밝혀라
- 설명: 동사 두 개가 whether 절 하나를 같이 받습니다. "알아서 해"와 "말없이 하지 마"를 한 번에 담습니다.
- 예문: Decide and state whether failed rows are included in the median.
- 유사어: make the call and say which way you went (회화), choose, and document the choice (격식)

## "every ambiguity and how you resolved it"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Report back)
- 맥락: 보고서에 애매했던 점과 그 처리 방식을 빠짐없이 적어 달라고 요청할 때
- 한국어: 애매했던 점 전부와, 각각을 어떻게 정리했는지
- 설명: 명사구 + 간접의문문(how you resolved it)을 and 로 나란히 놓은 보고 항목 형식입니다. resolve an ambiguity 는 "모호함을 해소하다"의 정석 collocation.
- 예문: In your report, list every ambiguity and how you resolved it.
- 유사어: any judgement calls you made (회화), open questions and the assumptions you settled on (격식)

## "what you could not verify without a browser"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 466cd9af subagent (Report back)
- 맥락: 검증 범위의 한계를 미리 보고하게 할 때
- 한국어: 브라우저 없이는 확인하지 못한 것
- 설명: could not 과거형이 "해 보려 했지만 못 했다"를 전제합니다. 테스트 통과와 실제 동작 확인을 구분하는 보고에 자주 씁니다.
- 예문: Also list what you could not verify without a browser, so I know what to click through.
- 유사어: what is still unverified (평이), what remains untested in the real app (격식)
- 반의어: browser-verified

## "insufficient for"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고 첫 문장)
- 맥락: 검토 결과를 한 문장 판정으로 먼저 내놓을 때(보고서 서두)
- 한국어: ~에 충분하지 않다, ~을 채우기에 모자라다
- 설명: not enough 의 격식형입니다. 보고 첫 줄에 결론을 놓는 bottom-line-up-front 구조로 쓰였습니다.
- 예문: The two tables are insufficient for the existing non-rule screens.
- 유사어: not enough for (평이), fall short of (격식, 기준 미달), won't cover (회화)
- 반의어: sufficient for, enough to cover

## "Step counts cannot replace measurement counts."
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고)
- 맥락: 비슷해 보이는 두 지표를 바꿔 쓰지 말라고 못 박을 때
- 한국어: step 수로 측정 건수를 대신할 수 없다
- 설명: 주어와 목적어가 같은 꼴(X counts)이라 대비가 또렷합니다. 요청서에서는 "**step 수로 측정 건수를 대신하지 마십시오.**"로 옮겨졌습니다.
- 예문: Step counts cannot replace measurement counts; they measure different things.
- 유사어: X is no substitute for Y (격식), you can't use X in place of Y (회화), X is not a proxy for Y (분석 글)

## "cannot distinguish A from B"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고 — "B cannot distinguish empty from failed.")
- 맥락: 데이터 구조가 서로 다른 두 상태를 같은 모양으로 만들어 버린다고 지적할 때
- 한국어: A 와 B 를 구별하지 못한다
- 설명: 표(table)를 주어로 둔 무생물 주어 문장입니다. `distinguish A from B` 와 `tell A and B apart` 가 짝입니다. 여기서 empty·failed 는 형용사를 명사처럼 쓴 상태 이름입니다.
- 예문: Table B alone cannot distinguish an empty recipe from a failed extraction.
- 유사어: can't tell A and B apart (회화), conflates A and B (격식, 섞어 버린다는 비판)
- 반의어: keeps A and B separate

## "underspecified"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고 — "Recipe identity/selection is underspecified.")
- 맥락: 명세가 틀리진 않았지만 정할 것을 다 정하지 않았다고 지적할 때(리뷰·명세)
- 한국어: 명세가 덜 된, 정의가 모자란
- 설명: under- 는 "기준보다 덜". 틀렸다(wrong)가 아니라 "빈칸이 남았다"는 지적이라 리뷰에서 부드럽게 쓰입니다.
- 예문: The join key is underspecified: the spec never says whether the tool family is part of it.
- 유사어: not pinned down (회화), loosely defined (평이), ambiguous (모호함 자체에 초점)
- 반의어: fully specified, overspecified (너무 구체적이라 유연성이 없는)

## "Snapshots only preserve future collection."
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고)
- 맥락: 스냅샷 기능이 과거를 되살려 주지 않는다는 한계를 짧게 경고할 때
- 한국어: 스냅샷은 앞으로 모이는 것만 남긴다
- 설명: only 가 동사 앞에서 범위를 좁힙니다. "켠 날 이후만"이라는 함정을 다섯 단어로 압축했습니다.
- 예문: Snapshots only preserve future collection, so there will be no trend from before the launch.
- 유사어: history starts the day you turn it on (회화), it does not backfill (기술 용어)
- 반의어: backfill historical data

## "X and Y were not verified."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 0028e27e (Codex 검토 보고 마지막 줄 — "Office coverage and live behavior were not verified.")
- 맥락: 보고를 마치며 확인하지 않은 범위를 수동태로 담담히 밝힐 때
- 한국어: X 와 Y 는 확인하지 않았다
- 설명: 수동태라 "누가"가 빠지고 "무엇이 확인 안 됐나"만 남습니다. 바로 앞 "No files changed." 와 함께 보고서의 정직한 꼬리말 역할을 합니다.
- 예문: No files changed. Office coverage and live behavior were not verified.
- 유사어: I didn't check X or Y (회화), X and Y remain unconfirmed (격식)

## "the logical AND of two independent questions"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 0028e27e (skewnono CLAUDE.md — "Which adapter answers is the logical AND of two independent questions")
- 맥락: 결과가 두 조건을 모두 만족할 때만 정해진다는 것을 논리 연산자로 비유할 때
- 한국어: 서로 독립된 두 질문의 논리곱(AND)
- 설명: AND 를 대문자로 써서 일상어 and 가 아니라 논리 연산임을 표시합니다. 주어가 간접의문문(Which adapter answers)인 점도 눈여겨볼 만합니다.
- 예문: Whether the office adapter runs is the logical AND of two independent questions: are we at the office, and is the adapter written?
- 유사어: depends on both X and Y (평이), requires X and Y to hold (격식)
- 반의어: either condition is enough (OR)

## "stays the same across phases"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 0028e27e (skewnono CLAUDE.md — "Frontend code stays the same across phases.")
- 맥락: 환경·단계가 바뀌어도 그대로인 부분을 짚을 때
- 한국어: 단계가 바뀌어도 그대로다
- 설명: `stay + 형용사`(stay the same, stay identical)가 변화 없음을 말합니다. across 는 "여러 단계에 걸쳐".
- 예문: Frontend code stays the same across phases; only the API target changes.
- 유사어: is identical across (격식), doesn't change between (회화)
- 반의어: varies by phase, branches on phase
