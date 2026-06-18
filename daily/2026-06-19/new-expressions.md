# 2026-06-19 — 새 표현

오늘 배치는 `wiki_for_office` 아키텍처 개요(격식 문어체)와 "하루 종일 돌려도 OOM 안 나나?"를
진단한 트랜스크립트(회화+기술)가 핵심 원천이었습니다.

---

## "derived and disposable"
- 레지스터: technical, professional
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: 설계 문서에서 *정본 데이터 vs 파생 데이터*를 구분할 때 (격식). 검색 인덱스·캐시처럼 언제든 다시 만들 수 있는 것을 "버려도 되는" 것으로 규정.
- 한국어: 원본에서 파생된 것이라 버려도(지웠다 다시 만들어도) 되는.
- 설명: canonical(정본)과 대비되는 짝. derived(파생) + disposable(폐기 가능)을 묶어 "이건 진실의 원천이 아니다, 인덱스일 뿐"이라고 못 박는 설계 어휘. 뒤에 흔히 `rebuildable`(재생성 가능)이 따라온다.
- 예문: Canonical knowledge is human-curated Markdown; all search structures are derived and disposable.
- 유사어: regenerable (재생성 가능, 거의 동의어), throwaway (회화체, 더 가벼움), ephemeral (격식; "수명이 짧은"에 가까움)
- 반의어: canonical / authoritative (정본의·권위 있는), source of truth (진실의 원천)

## "the trust boundary is X, not Y"
- 레지스터: technical, professional
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: 보안 설계를 설명할 때(격식 문서). "신뢰 경계가 어디냐"를 한 문장으로 못 박는 정의형.
- 한국어: 신뢰 경계는 (개별 장비 한 대가 아니라) 회사 네트워크 전체다.
- 설명: `trust boundary`는 보안에서 "이 선 안쪽은 믿고, 바깥은 안 믿는다"의 그 선. `X, not Y` 구문으로 흔한 오해(=장비 단위)를 먼저 부정하고 진짜 기준을 세운다. 결정문·ADR 단골 문형.
- 예문: The trust boundary is the company network, not one machine: data may flow to internal services but never to public ones.
- 유사어: the line we draw is ... (회화체), the security perimeter (거의 동의어, 더 기술적)
- 반의어: (마땅한 대체 표현 없음)

## "a thin capture client"
- 레지스터: technical
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: 아키텍처에서 *역할이 가벼운 클라이언트*를 가리킬 때. 무거운 처리는 서버가, 단말은 최소한만.
- 한국어: 기능을 최소화한 얇은(가벼운) 클라이언트.
- 설명: `thin client`(↔ `thick/fat client`)는 "로직 거의 없이 캡처·전송만 하는 단말". 형용사 `thin`이 "책임을 얇게 줄였다"는 설계 의도를 한 단어로 전달한다.
- 예문: Each user runs a thin capture client on their own PC that captures the screen and sends images over an authenticated channel.
- 유사어: lightweight client (거의 동의어, 덜 전문적), dumb terminal (구식·다소 비하)
- 반의어: thick client / fat client (로직을 단말이 떠안는 무거운 클라이언트)

## "X is metadata only"
- 레지스터: technical, professional
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: "이 필드는 *표시만* 하고 강제(enforcement)는 안 한다"고 범위를 좁힐 때(격식).
- 한국어: X는 메타데이터일 뿐이다(기록만 하고 실제로 강제하지는 않는다).
- 설명: 기능을 의도적으로 줄였음을 밝히는 scope-limiting 표현. `only`가 "그 이상은 안 한다"를 강조. v1에서 권한(ACL)을 강제하지 않는다는 결정을 한 줄로 표현.
- 예문: Personal-first: `visibility` is metadata only; there is no ACL enforcement in v1.
- 유사어: advisory only (권고일 뿐 강제 아님), for display purposes only (표시 전용)
- 반의어: enforced / hard-enforced (실제로 강제되는)

## "grounded in (the literature)"
- 레지스터: professional
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: 설계·주장이 *선행 연구·근거에 뿌리내렸다*고 밝힐 때(격식 문어). 논문·제안서 단골.
- 한국어: ~(문헌/근거)에 단단히 기반을 둔.
- 설명: `grounded in`은 "막연한 직관이 아니라 ~에 근거를 둔다"는 신뢰 부여 표현. 뒤에 literature(선행연구), evidence, data 등이 온다. 수동태로 자주 쓴다.
- 예문: The wiki layer is specified in `llm-wiki-layer.md`, grounded in the LLM-Wiki and Retrieval-as-Reasoning literature.
- 유사어: rooted in (거의 동의어), informed by (좀 더 느슨; "~을 참고한"), based on (가장 평이)
- 반의어: ungrounded / speculative (근거 없는·추측에 불과한)

## "deferred deliberately"
- 레지스터: professional
- 출처: repo:wiki_for_office (architecture/overview.md)
- 맥락: 로드맵에서 *일부러 뒤로 미뤘다*고 밝힐 때(격식). "빠뜨린 게 아니라 의도한 결정"임을 강조.
- 한국어: 의도적으로 (뒤로) 미뤘다.
- 설명: `deliberately`가 "실수·누락이 아니라 판단"임을 못 박는 핵심. 스코프 결정문에서 "왜 지금 안 하나"를 방어할 때 유용. 이어 그 이유(가장 가치 낮고 검증 어려움)를 댄다.
- 예문: Report drafting and the automated quality loop were deferred deliberately: both are the least valuable and least testable to build first.
- 유사어: intentionally postponed (동의어, 더 평이), out of scope by design (설계상 범위 밖)
- 반의어: overlooked / dropped by accident (실수로 빠뜨린)

## "edge-triggered"
- 레지스터: technical
- 출처: transcript (auto_recipe_creator — 장기 실행 모니터 분석)
- 맥락: 비싼 작업이 *매 주기마다*가 아니라 *상태가 바뀌는 순간*에만 돈다고 설명할 때(엔지니어 구어·기술).
- 한국어: 엣지 트리거 방식의(상태 변화의 '순간'에만 발동하는).
- 설명: 전자공학의 edge-triggered(↔ level-triggered)에서 온 비유. 폴링 루프가 매번 일하는 게 아니라 "새 이벤트가 *처음 나타날 때만*" 무거운 일을 한다 → 24시간 안전의 핵심 근거로 제시.
- 예문: The expensive work is edge-triggered: it only runs when a new align-fail appears, not on every 10-second poll.
- 유사어: fires only on a state change (풀어 쓴 설명), event-driven (더 넓은 개념)
- 반의어: level-triggered / polled every cycle (매 주기 발동)

## "grow without bound"
- 레지스터: technical
- 출처: transcript (auto_recipe_creator — 리소스 누수 분석)
- 맥락: 메모리·디스크가 *상한 없이* 계속 커진다고 경고할 때(기술). 누수·무한 증가 진단의 표준어.
- 한국어: 상한 없이(한없이) 계속 늘어나다.
- 설명: `without bound` = "경계(상한)가 없는". 자원 누수 분석의 핵심 표현으로, "bounded(상한 있음)면 안전, unbounded면 위험"의 대비가 깔려 있다. 비슷하게 `grow indefinitely`도 쓴다.
- 예문: The only thing that grows without bound is the filesystem: every failure writes a new folder and nothing ever deletes them.
- 유사어: grow indefinitely (동의어), grow unbounded (형용사형), accumulate without limit
- 반의어: bounded / capped (상한이 걸린), self-limiting (스스로 멈추는)

## "the most likely to bite you"
- 레지스터: conversational
- 출처: transcript (auto_recipe_creator — 위험 요인 순위 매김)
- 맥락: 여러 위험 중 *실제로 사고 날 확률이 제일 높은 것*을 콕 집을 때(동료에게 구어로 경고).
- 한국어: 실제로 발목 잡을(탈 날) 가능성이 가장 높은 것.
- 설명: `bite (someone)`는 "(방치한 문제가 나중에) 물어뜯다 → 탈이 나다"는 구어 비유. 격식 문서라면 `the most likely failure mode`로 바꾼다. 회화에서 위험 우선순위를 솔직히 말할 때 자연스럽다.
- 예문: Disk space is the one most likely to bite you: nothing ever prunes those capture folders.
- 유사어: come back to bite you (나중에 부메랑이 되다), the biggest gotcha (구어; 숨은 함정), the real risk (중립)
- 반의어: negligible / nothing to worry about (무시해도 되는)

## "worth double-checking"
- 레지스터: conversational, professional
- 출처: transcript (auto_recipe_creator — 점검 권고)
- 맥락: "이건 직접 한 번 더 확인할 값어치가 있다"고 부드럽게 권할 때(코드리뷰·구두 보고 모두).
- 한국어: 한 번 더 확인해 둘 만하다.
- 설명: `worth + -ing`(=~할 가치가 있다) 패턴의 실전형. 명령("확인해") 대신 가치를 제시해 부드럽게 권한다. 보고서엔 `warrants a second look`로 격식화.
- 예문: The real office version is swapped in at runtime, so that's the one file worth double-checking on the office machine.
- 유사어: worth a second look (동의어), worth verifying (더 격식), I'd sanity-check that (구어)
- 반의어: safe to skip / not worth the effort (확인 안 해도 되는)

## "from a (memory) standpoint"
- 레지스터: professional, conversational
- 출처: transcript (auto_recipe_creator — 결론 한정)
- 맥락: 결론을 *특정 관점에 한정*해 말할 때. "메모리 면에서는 괜찮다 (단, 디스크는 별개)"처럼 범위를 명확히.
- 한국어: ~ 관점/측면에서 (보면).
- 설명: `from a X standpoint`로 판단의 적용 범위를 좁혀, 다른 측면의 위험은 따로 있음을 암시한다. `from a X perspective`와 호환. 솔직하고 정확한 결론 진술에 유용.
- 예문: Bottom line: it's safe to run all day from a memory standpoint — but watch your disk usage.
- 유사어: from a X perspective (동의어), as far as X goes (구어; "X에 관한 한")
- 반의어: (마땅한 대체 표현 없음)

---

## 한글→영어 코칭 카드

### 카드 1 — "유니크한 위치는 두 이미지에 모두 존재하는 경우가 있고, 없다면 문제가 있는 것"
- 출처: transcript (사용자가 align_point_correction 관련해 쓴 한국어 프롬프트)
- **내가 쓴 한글**: "이미지가 아무리 달라도 유니크한 위치는 두 이미지에 모두 존재하는 경우가 있고, 없다면 그건 live SEM 이미지가 완전히 다른 위치에 있거나 문제가 있기 때문에 마우스로 이동이 필요."
- **자연스러운 영어**: "However different the two images are, a genuinely unique landmark often exists in both. When it doesn't, the live SEM view is either framed on a completely different area or is otherwise off — so a manual mouse move is needed."
- **왜 이렇게**:
  - "이미지가 아무리 달라도" → `However different the two images are, ...` — `however + 형용사 + 주어 + be`는 "아무리 ~해도"의 격식 양보절. 회화로는 `No matter how different the images are`.
  - "유니크한 위치" → 좌표가 아니라 *식별 가능한 지점*이므로 `unique location`보다 `unique landmark`(또는 `distinctive feature`)가 정확. CV 맥락에서 landmark/feature가 표준어.
  - "~인 경우가 있다" → `there are cases where ...`로 직역하기 쉽지만, `often exists`처럼 빈도 부사로 녹이면 더 영어답다.
  - "문제가 있기 때문에" → `because there is a problem`(막연)보다 `is otherwise off`(뭔가 어긋났다)가 엔지니어 구어로 자연스럽다.

### 카드 2 — "VLM이 이런 것도 가능할까 궁금한거야"
- 출처: transcript (같은 프롬프트의 마무리 질문)
- **내가 쓴 한글**: "VLM을 이용해서 from rcp와 from msr 이미지를 나란히 붙여서, 왼쪽 중심부와 유사한 부분을 오른쪽에서도 찾을 수 있는지 궁금해. VLM이 이런 것도 가능할까?"
- **자연스러운 영어**: "I'm curious whether a VLM could take the rcp and msr images side by side and locate, on the right, the region that matches the center of the left one. Is that the kind of thing a VLM can actually do?"
- **왜 이렇게**:
  - "~할 수 있는지 궁금해" → `I'm curious whether ...` / `I wonder if ...`. `whether`는 격식, `if`는 회화. 둘 다 자연스럽다.
  - "나란히 붙여서" → `side by side`(부사구) 한 단어구로 깔끔. `attach them next to each other`는 어색.
  - "이런 것도 가능할까?" → `Is that possible?`도 되지만, `Is that the kind of thing a VLM can do?`가 "이런 부류의 일"을 살려 더 자연스럽고, `actually`로 "정말로?"의 뉘앙스를 더한다.
