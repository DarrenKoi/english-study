# 2026-07-18 — 새 표현

오늘 배치는 skewnono 설계 문서(RAG 챗 기반, AFM 컨트롤 시리즈)와 코드리뷰 transcript 가
중심이었습니다. 설계·리뷰 영어에서 15개 표현을 골랐습니다.

## "carry forward"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md
- 맥락: 이전 단계(리뷰·회의)에서 나온 결정·발견을 다음 단계로 "가지고 간다"고 할 때(문어·격식)
- 한국어: (앞 단계의 결과를) 이월하다, 계속 반영해 가져가다
- 설명: 회계 용어(이월)에서 온 표현. 설계 문서에서 "이 발견들은 잊지 말고 이번 설계에 반영해야 한다"를 한 단어로 처리합니다.
- 예문: A retrospective review added three operational findings that this design must carry forward.
- 유사어: retain (그냥 유지, 이동 뉘앙스 없음), propagate (기술적·자동 전파 뉘앙스), inherit (아래 단계가 물려받는 쪽 시점)
- 반의어: drop / leave behind (다음 단계로 안 가져가고 버리다)

## "go stale"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md
- 맥락: 데이터·설정·문서가 시간이 지나 낡아 못 쓰게 됨을 말할 때(구어·기술 문서 모두)
- 한국어: (기본값·목록·캐시가) 낡아버리다, 유효하지 않게 되다
- 설명: stale(빵이 눅눅해진)에서 온 은유. become outdated 보다 짧고 생생하며, "관리 안 하면 자연히 썩는다"는 뉘앙스가 있습니다.
- 예문: The default `CHAT_MODELS` entries are free OpenRouter tiers that go stale.
- 유사어: become outdated (중립·격식), rot (더 강한 구어, bit rot), age poorly (완곡)
- 반의어: stay fresh / stay current (계속 유효하다)

## "make (the transition) mechanical"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md
- 맥락: 문서·절차를 잘 만들어 나중 작업이 "판단 없이 따라만 하면 되는" 수준이 되게 할 때(문어)
- 한국어: (작업을) 기계적으로 따라 할 수 있게 만들다
- 설명: mechanical 은 여기서 "지루한"이 아니라 "판단이 필요 없는 = 리스크가 낮은"이라는 칭찬입니다. 마이그레이션 문서의 목표를 한 문장으로 요약하는 관용 패턴.
- 예문: `MIGRATION.md` will make the office transition mechanical.
- 유사어: make it turnkey (더 제품스러운 뉘앙스), reduce it to a checklist (구체적), make it a paint-by-numbers exercise (구어·비유)
- 반의어: leave it to judgment (판단에 맡기다)

## "a curated subset"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-afm-points-table-design.md
- 맥락: 전체를 다 옮기지 않고 "가치 있는 것만 골라낸 일부"를 이식·제공한다고 할 때(문어)
- 한국어: 선별한 부분집합, 엄선한 일부
- 설명: curate(큐레이션하다)는 "기준을 갖고 골랐다"는 뉘앙스. 단순 subset/part 와 달리 "빠진 것은 실수가 아니라 의도"임을 알립니다.
- 예문: We port a curated subset of the legacy component rather than all 768 lines.
- 유사어: a handpicked subset (더 구어), a distilled version (추려서 압축한), a trimmed-down port (기능 축소 강조)
- 반의어: a wholesale port / a 1:1 copy (통째 이식)

## "feature parity"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-afm-histogram-controls-design.md
- 맥락: 신구 시스템·경쟁 제품과 "기능이 대등한 상태"를 목표로 말할 때(기술 기획 표준 용어)
- 한국어: 기능 동등성 (기존 제품과 같은 기능 수준)
- 설명: parity 는 "동등함". reach/achieve feature parity with X 형태로 마이그레이션 프로젝트의 완료 조건을 정의할 때 늘 나옵니다.
- 예문: C4 is the final sub-project of the AFM feature-parity effort.
- 유사어: on par with (형용사구, 더 일반적), functional equivalence (더 격식·계약서 느낌)
- 반의어: a feature gap (기능 격차)

## "a quick win"
- 레지스터: conversational, professional
- 출처: repo:skewnono_v3_nuxt docs/handoff/handoff-2026-07-16-skewvoir-drilldowns-plan-amendment.md
- 맥락: 노력 대비 효과가 빨리 나오는 작은 작업을 먼저 하자고 제안할 때(회의·구어, 문서에도 무난)
- 한국어: 손쉬운 성과, 빨리 따먹을 수 있는 열매
- 설명: 우선순위 논의의 단골 표현. "제대로 된 큰 작업 전에 이것부터 하면 바로 티가 난다"는 제안에 씁니다.
- 예문: If the user wants the quick win first, Task 3b requires Task 3's `setFocusedMsr`.
- 유사어: low-hanging fruit (거의 동의어, 약간 진부), an easy win (같은 뜻), a cheap fix (수정 작업에 한정)
- 반의어: a long slog (오래 걸리는 고된 작업)

## "tightly-scoped"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (code review)
- 맥락: 변경·작업이 "딱 필요한 범위만 건드렸다"고 칭찬·평가할 때(리뷰·문어)
- 한국어: 범위를 좁고 엄격하게 한정한
- 설명: scope 를 동사로 쓴 수동 분사형. 리뷰에서 a tightly-scoped change 는 "부수 효과 걱정이 적다"는 최고급 칭찬 중 하나입니다.
- 예문: The change is a tightly-scoped, well-tested decoupling with consistent contracts across all five commits.
- 유사어: narrowly-scoped (중립), surgical (더 비유적·강함), minimal (범위보단 크기 강조)
- 반의어: sprawling / scope-creepy (범위가 번져버린)

## "a clean, minimal cut"
- 레지스터: professional, conversational
- 출처: transcript:auto-recipe-creator (code review)
- 맥락: 리뷰 총평 첫 줄에서 "군더더기 없이 딱 필요한 만큼만 잘라낸 변경"이라고 평할 때
- 한국어: 깔끔하고 최소한으로 잘라낸 변경
- 설명: cut 은 여기서 외과 수술의 절개처럼 "잘라낸 방식"을 뜻합니다. 명사 하나로 변경의 품질(clean)과 크기(minimal)를 동시에 평가합니다.
- 예문: Clean, minimal cut — the change does exactly what the spec asked.
- 유사어: a surgical change (같은 은유), a focused diff (diff 관점), no-frills (부가 기능 없음 강조)
- 반의어: a sprawling change (여기저기 번진 변경)

## "remove only noise"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (code review)
- 맥락: 경고·로그·코드를 지워도 "잃는 정보가 없다"고 안전함을 논증할 때(리뷰·문어)
- 한국어: (지운 것이) 소음만 없앨 뿐 정보 손실이 없다
- 설명: signal vs noise 은유. 같은 리뷰의 "silencing the warning hides nothing"(경고를 꺼도 숨겨지는 건 없다)과 짝으로, 삭제 변경을 정당화하는 결정타 문장입니다.
- 예문: Removing the load-time warning removes only noise.
- 유사어: hides nothing (같은 논증의 다른 축), is informationally lossless (더 딱딱한 격식), pure cleanup (구어)
- 반의어: swallow a real signal (진짜 신호를 삼켜버리다)

## "rise above (Minor)"
- 레지스터: professional
- 출처: transcript:auto-recipe-creator (code review)
- 맥락: 이슈들의 심각도가 어떤 등급을 "넘지 않는다"고 총평할 때(리뷰·문어)
- 한국어: (심각도가) ~등급 위로 올라가지 않다
- 설명: rise above 는 물리적 상승 은유를 심각도 사다리에 적용한 것. none rise above Minor 한 문장이면 "전부 사소함"을 등급 체계 안에서 정확히 말할 수 있습니다.
- 예문: None of the carryover items rise above Minor on the whole-branch view.
- 유사어: none exceed (더 중립), all fall below (반대 방향에서 서술), nothing blocking (결론만 말하는 구어)
- 반의어: escalate to (Critical) (등급이 올라가다)

## "(conventions that) bit us"
- 레지스터: conversational, casual
- 출처: repo:skewnono_v3_nuxt docs/handoff/handoff-2026-07-16-skewvoir-drilldowns-plan-amendment.md
- 맥락: 과거에 실수로 "당해 본" 규칙·함정을 후임에게 경고할 때(구어, 인수인계 문서의 살아있는 제목)
- 한국어: 우리가 물렸던(한 번 당했던) 규칙들
- 설명: bite 는 함정이 "무는" 은유. "This will bite you later"(나중에 이게 발목 잡는다)처럼 미래 경고형으로도 자주 씁니다. 격식 문서라면 caused issues 로 순화.
- 예문: Conventions that bit us: run the Markdown linter after every doc edit.
- 유사어: burned us (거의 동의어, 더 강함), tripped us up (걸려 넘어짐, 순함), came back to haunt us (뒤늦게 대가를 치름)
- 반의어: saved us (우리를 구해준 규칙)

## "well-behaved (data)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-afm-histogram-controls-design.md
- 맥락: 이상치·극단값 없이 가정대로 움직이는 데이터·입력을 말할 때(기술·통계)
- 한국어: 얌전한(이상치 없는·가정을 지키는) 데이터
- 설명: 아이 행동 표현을 데이터에 의인화한 기술 관용구. 수학에서도 well-behaved function 이 표준 용어입니다.
- 예문: Auto mode picks Sturges for well-behaved data and Freedman-Diaconis when outliers exceed 5%.
- 유사어: clean (더 일반적), outlier-free (구체적), degenerate 의 반대 개념으로 non-degenerate
- 반의어: pathological / degenerate (병적인·퇴화한 입력)

## "keep the diff frozen"
- 레지스터: technical, conversational
- 출처: transcript:auto-recipe-creator (code review)
- 맥락: 머지 직전, 추가 수정 없이 현재 변경분을 그대로 유지하자고 할 때(리뷰·구어)
- 한국어: (머지 전) diff 를 더 건드리지 않고 동결해 두다
- 설명: freeze 는 code freeze 처럼 "변경 금지" 은유. 리뷰어가 사소한 개선을 제안하면서도 "지금 diff 를 얼려두고 싶으면 미뤄도 된다"고 출구를 열어 줄 때 씁니다.
- 예문: Defer the log tweak if you want to keep the diff frozen.
- 유사어: leave the diff as-is (평이), lock the change down (더 강함), no further churn (churn 관점)
- 반의어: reopen the change (변경을 다시 열다)

## "text-first and image-selective"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-17-chat-agentic-rag-foundation-design.md
- 맥락: 처리 순서·우선순위 정책을 "X-first, Y-선택적" 복합 형용사로 압축할 때(설계 문서)
- 한국어: 텍스트를 우선하고 이미지는 선별적으로 쓰는
- 설명: X-first (mobile-first, API-first)와 X-selective 를 조합한 정책 명명 패턴. 형용사 두 개로 4단계 파이프라인 전체의 철학을 요약합니다. citation-first(출처 우선)도 같은 문서에 등장.
- 예문: The retrieval flow is text-first and image-selective: search text, then open only the pages the agent judges relevant.
- 유사어: prioritize text over images (풀어 쓴 평이체), text-centric (우선순위보단 중심성)
- 반의어: image-heavy (이미지 위주의)

## "stay close to (the data they describe)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-recipe-status-inline-summaries-design.md
- 맥락: UI·문서 요소를 관련 대상 "가까이에 붙여 두는" 배치 원칙을 말할 때(설계 문어)
- 한국어: (요약이) 그것이 설명하는 데이터 곁에 머물게 하다
- 설명: 물리적 거리 은유로 정보 설계 원칙(연관 정보 근접 배치)을 표현. 코드에서도 "keep the comment close to the code it explains" 같은 변형이 흔합니다.
- 예문: Move the summary values into the table headers so they stay close to the ranked data they describe.
- 유사어: colocate with (더 기술적), sit next to (평이·구어)
- 반의어: float free of (맥락에서 떨어져 겉돌다)
