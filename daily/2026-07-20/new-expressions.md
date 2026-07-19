# 2026-07-20 — 새 표현

## "do the heavy lifting"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 81e82c59
- 맥락: 시스템·설계에서 힘든 일 대부분을 어떤 요소가 대신 해주고 있다고 말할 때(구어·리뷰)
- 한국어: 궂은일을 도맡다, 무거운 몫을 감당하다
- 설명: 원래 "무거운 짐을 드는 일"인데, 코드 리뷰에선 "이 세 가지 설계 결정이 유지보수성의 대부분을 책임진다"처럼 공로가 어디에 있는지 짚을 때 씁니다. 배치에선 "three design decisions are doing the heavy lifting"으로 등장했습니다.
- 예문: The contract tests are doing the heavy lifting here — the docs just describe what they already enforce.
- 유사어: carry the load (부담을 진다는 중립 표현), do the real work (더 직설적)
- 반의어: be along for the ride (묻어가다)

## "a sharp edge"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 81e82c59
- 맥락: 편리한 기능에 숨은, 베일 수 있는 위험 지점 하나를 경고할 때(리뷰·구어)
- 한국어: 날카로운 모서리, 다치기 쉬운 지점
- 설명: 도구가 대체로 안전하지만 특정 사용법에서 사고가 나는 지점을 "모서리"에 비유합니다. 배치에선 rglob 자동 등록의 부작용을 "The rglob auto-discovery has one sharp edge"라고 했습니다. 복수형 "sharp edges"는 API의 거친 부분 전반을 가리킵니다.
- 예문: The auto-discovery is convenient, but it has one sharp edge: any stray routes.py goes live silently.
- 유사어: a footgun (스스로 쏘기 쉬운 기능, 더 캐주얼), a gotcha (예상 밖 함정), a pitfall (일반적·중립)
- 반의어: guardrails (안전장치)

## "sweep in"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 66803736
- 맥락: 커밋·작업 범위에 의도치 않은 파일이 휩쓸려 들어갔을 때(git 문맥)
- 한국어: (의도 없이) 휩쓸어 담다
- 설명: 빗자루로 쓸어 담듯 무관한 것까지 같이 들어간 상황. 배치에선 "my git commit swept in 11 unrelated pre-staged files"처럼 수동 실수의 표준 표현으로 반복해 나왔습니다.
- 예문: A bare git commit swept in four files I had explicitly meant to exclude.
- 유사어: get caught up in (말려들다), drag in (끌고 들어오다)
- 반의어: scope the commit to (커밋 범위를 ~로 한정하다)

## "maintenance hygiene"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 81e82c59
- 맥락: 구조 결함은 아니지만 꾸준히 챙겨야 할 정리·청소성 작업을 분류할 때(리뷰·격식)
- 한국어: 유지보수 위생, 코드 청결 관리
- 설명: hygiene(위생)을 빌려 "심각한 문제는 아니고 평소 습관으로 관리할 일"이라는 등급을 매깁니다. 배치에선 "None of these are structural flaws — they're maintenance hygiene"으로 결함의 심각도를 낮춰 정리했습니다.
- 예문: Deleting the orphaned pycache folders is maintenance hygiene, not a structural fix.
- 유사어: housekeeping (일상 정리, 더 구어적), code health (코드 건강 전반)
- 반의어: a structural flaw (구조적 결함)

## "come for free"
- 레지스터: technical, conversational
- 출처: transcript:skewnono_v3_nuxt 7112bc25
- 맥락: 별도 노력 없이 기존 구조 덕에 공짜로 얻어진 효과를 설명할 때(구어·기술)
- 한국어: 공짜로 따라오다, 덤으로 얻어지다
- 설명: 좋은 추상화의 배당금을 표현하는 관용구. 배치에선 "placement consistency came for free from component reuse" — 컴포넌트를 재사용한 덕에 배치 일관성이 저절로 확보됐다는 뜻입니다.
- 예문: Because all three tabs render the same nav component, the consistent header came for free.
- 유사어: fall out of (구조에서 자연히 도출되다), get X for free (동일 구문의 타동형)
- 반의어: come at a cost (대가가 따르다)

## "breathing room"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 2df41210
- 맥락: 레이아웃·일정·예산에 여유 공간을 준다고 말할 때(구어)
- 한국어: 숨 쉴 틈, 여유 공간
- 설명: UI에선 요소 사이 여백, 일정에선 버퍼를 뜻합니다. 배치에선 모달을 넓히며 "gives the 2-column field grid real breathing room"이라고 썼습니다. give A breathing room 꼴로 자주 씁니다.
- 예문: Widening the modal to 768px gives the field grid some breathing room.
- 유사어: elbow room (움직일 여지, 더 구어적), headroom (상한까지 남은 여유 — 수치 문맥)
- 반의어: cramped (비좁은)

## "hand-wave"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt b7df6a67
- 맥락: 근거 없이 얼버무리며 넘어가는 설명을 비판하거나 차단할 때(리뷰·구어)
- 한국어: 손사래로 얼버무리다, 두루뭉술 넘어가다
- 설명: 손을 흔들며 "대충 그렇게 됩니다" 하고 넘어가는 모습에서 온 동사. 배치에선 검증 자료를 미리 줘서 "so it can't hand-wave" — 상대가 얼버무릴 수 없게 만들었다는 용법이 나왔습니다. 명사형 hand-waving도 흔합니다.
- 예문: I gave the reviewer the verified data-availability facts so it can't hand-wave the hard parts.
- 유사어: gloss over (대충 넘기다), paper over (덮어 감추다 — 은폐 뉘앙스)
- 반의어: ground (a claim) in evidence (근거에 정박시키다)

## "rule of thumb"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt e77685e7
- 맥락: 정밀하진 않지만 실무에서 통하는 경험칙을 제시할 때(구어)
- 한국어: 경험칙, 어림 법칙
- 설명: 엄지 폭으로 대충 재던 관행에서 온 말. 배치에선 "Rule of thumb: consider /compact when you're past ~75–80% used"처럼 문두에 콜론으로 던지는 패턴이 전형적입니다.
- 예문: Rule of thumb: compact the session once you're past eighty percent of the context window.
- 유사어: a good heuristic (격식·기술 문맥), a ballpark guide (대략의 기준)
- 반의어: a hard rule (예외 없는 규칙)

## "eyeball it"
- 레지스터: casual, conversational
- 출처: transcript:skewnono_v3_nuxt 2df41210
- 맥락: 계측 없이 눈대중으로 확인하자고 할 때(동료 간·캐주얼)
- 한국어: 눈대중으로 보다
- 설명: eyeball(안구)을 동사로 써서 "직접 눈으로 대충 확인하다". 배치에선 모달 폭을 조정한 뒤 "Want to eyeball it first, or is 3xl the target?"이라고 물었습니다. 정밀 검증(measure, verify)과 대비되는 가벼운 확인입니다.
- 예문: Want to eyeball it in the browser first, or should I just commit the wider modal?
- 유사어: give it a once-over (한번 훑어보다), sanity-check (최소한의 타당성 확인 — 좀 더 기술적)
- 반의어: measure it precisely (정밀 측정하다)

## "muscle memory carries over"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt ec3ce099
- 맥락: 도구를 바꿔도 몸에 밴 습관이 그대로 통한다고 안심시킬 때(구어)
- 한국어: 손에 익은 감각이 그대로 이어지다
- 설명: muscle memory는 의식하지 않고 손이 기억하는 조작 습관. carry over는 "이월되다". 배치에선 tmux에서 Herdr로 갈아타도 같은 Ctrl-a 프리픽스라 "your muscle memory carries over directly"라고 했습니다.
- 예문: Since both tools use Ctrl-a as the prefix, your muscle memory carries over directly.
- 유사어: transfer (기술이 전이되다 — 중립), translate to (다른 환경에서도 통하다)
- 반의어: start from scratch (처음부터 다시 익히다)

## "clobber"
- 레지스터: technical, casual
- 출처: transcript:skewnono_v3_nuxt 7112bc25
- 맥락: 동시 작업·덮어쓰기로 남의 데이터를 짓뭉갤 위험을 말할 때(개발자 은어)
- 한국어: 짓밟아 덮어쓰다, 뭉개다
- 설명: 원래 "두들겨 패다"라는 속어인데, 개발에선 파일·변수·커밋을 의도치 않게 덮어써 망가뜨리는 걸 뜻합니다. 배치에선 경쟁하는 git 세션을 두고 "the racing commits could just as easily have clobbered something"이라고 경고했습니다.
- 예문: Pause the other session while you work here — a racing commit could clobber your staged files.
- 유사어: overwrite (중립·정확), stomp on (밟아 뭉개다 — 비슷한 은어)
- 반의어: preserve (온전히 보존하다)

## "churn"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt 2df41210
- 맥락: 의미 있는 개선 없이 코드만 휘젓는 변경을 깎아내릴 때(리뷰·격식)
- 한국어: 공회전성 변경, 헛도는 뒤척임
- 설명: 우유를 휘젓듯(churn) 요란하지만 남는 게 없는 변경. 배치에선 변수명 일괄 변경을 거부하며 "Renaming those would be churn without meaning"이라고 했습니다. diff churn, code churn 꼴로도 씁니다.
- 예문: Renaming the runtime identifiers would be churn without meaning — they describe the feature, not the widget.
- 유사어: busywork (바쁘기만 한 일), noise (diff 소음)
- 반의어: a substantive change (실질적 변경)

## "starve"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 92aa3491
- 맥락: 한 요소가 자원(공간·CPU·예산)을 독차지해 다른 쪽을 말려 죽일 때(기술)
- 한국어: (자원을) 굶기다, 말려 죽이다
- 설명: 스케줄링의 starvation에서 온 동사인데 레이아웃에도 그대로 씁니다. 배치에선 "a child with intrinsic height can starve a flex-1 sibling down to its min-height floor" — 웨이퍼 맵이 공간을 다 먹어 차트가 최소 높이까지 쪼그라든 상황입니다.
- 예문: The fixed-height wafer map starves its flex sibling down to the 144px floor on short viewports.
- 유사어: crowd out (밀어내다), monopolize (독점하다 — 격식)
- 반의어: leave room for (여지를 남기다)

## "butt against"
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 92aa3491
- 맥락: 요소가 여백 없이 가장자리에 딱 붙어 부딪히는 모양을 말할 때(UI 리뷰·구어)
- 한국어: (여백 없이) 맞닿다, 들이받다
- 설명: butt는 머리로 들이받는 동작. UI에선 콘텐츠가 카드 모서리에 여백 없이 붙은 상태를 그립니다. 배치에선 차트 여백을 넓히며 "instead of butting against them(카드 모서리)"이라고 썼습니다. butt up against 꼴도 흔합니다.
- 예문: With the wider inset, the scatter points no longer butt against the card's right edge.
- 유사어: press up against (밀착하다), be flush with (면이 맞닿다 — 중립·의도된 정렬)
- 반의어: have margin from (여백을 두다)

## "worth your call"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt b7df6a67
- 맥락: 결정권이 상대에게 있는 사안 하나를 짚어 넘길 때(협업·구어)
- 한국어: 당신이 정할 만한 문제
- 설명: call은 "판정·결정"(make the call). "one thing worth your call"은 "이건 내 선에서 정하지 않고 당신 판단을 받을 가치가 있다"는 공손한 에스컬레이션입니다. 배치에선 플랜 분리 여부를 사용자에게 넘기며 썼습니다.
- 예문: One thing worth your call: keep the gated tasks inside this plan, or split them into a follow-up doc?
- 유사어: your call (더 짧고 구어적), up to you (완전 캐주얼), at your discretion (격식)
- 반의어: I'll make the call (내가 정하겠다)
