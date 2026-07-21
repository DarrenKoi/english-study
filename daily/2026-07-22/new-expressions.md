# 2026-07-22 — 새 표현

## "Good catch"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 상대가 내가 놓친 문제를 짚어줬을 때 먼저 인정하고 시작하는 리액션(회의·리뷰·채팅 어디서나)
- 한국어: "좋은 지적이에요", "그거 잘 잡으셨네요"
- 설명: 지적을 받아들이는 가장 짧고 기분 좋은 방법. 이 뒤에 바로 본론("— the cloud absolutely needs considering")을 이어붙이는 흐름이 전형적이다. 리뷰 코멘트 답글에서도 자주 쓴다.
- 예문: Good catch — the cloud absolutely needs considering, because production silently showing fake data would be a real incident.
- 유사어: Nice catch (같은 뜻, 조금 더 캐주얼), Fair point (지적 수용이지만 "잡아냈다"는 뉘앙스는 약함), You're right to flag this (격식 한 단계 위)

## "On it"
- 레지스터: conversational, casual
- 출처: transcript:skewnono_v3_nuxt 92aad678
- 맥락: 지시를 받자마자 "바로 착수합니다"라고 답할 때(채팅·구어, 두 단어로 끝)
- 한국어: "바로 할게요", "지금 합니다"
- 설명: "I'm on it"의 축약. 뒤에 착수 내용을 대시로 이어 "On it — rename skew, then commit"처럼 쓰면 응답과 작업 계획이 한 줄에 담긴다.
- 예문: On it — I'll rename skew too, then commit.
- 유사어: Will do (수락의 뉘앙스가 더 강함), Right away (격식 조금 위), I'll get right on it (완전한 문장 버전)

## "Mystery solved"
- 레지스터: conversational
- 출처: transcript:skewnono_v3_nuxt 92aad678
- 맥락: 한참 헤매던 이상 현상의 원인을 마침내 찾았을 때 결과 보고의 첫 마디로(구어·채팅)
- 한국어: "수수께끼 풀렸습니다", "원인 찾았어요"
- 설명: 디버깅 서사에서 전환점을 알리는 관용구. 뒤에 대시로 원인을 붙인다: "Mystery solved — those changes are a concurrent, unrelated edit."
- 예문: Mystery solved — those limit changes came from a concurrent edit in another session, not from my rename.
- 유사어: That explains it (원인을 듣고 납득할 때), Found it (더 짧고 밋밋), Case closed (수사 종결 느낌, 장난기 있음)

## "a false alarm"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 문제라고 의심했던 것이 조사해 보니 문제가 아니었을 때(리뷰·디버깅 보고)
- 한국어: 오탐, 헛경보
- 설명: 화재경보 오작동에서 온 표현. 리뷰에서 "my one suspected defect is a false alarm"처럼 자기 의심을 스스로 철회할 때 정직하고 깔끔하게 들린다.
- 예문: I verified the cache path directly — my suspected immortal-cache defect is a false alarm.
- 유사어: a false positive (탐지 도구·테스트 문맥의 기술어), a non-issue (문제 자체가 아님), a red herring (진짜 원인에서 주의를 돌린 단서)
- 반의어: a real find / a genuine defect

## "(something) takes care of itself"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 별도 조치 없이 저절로 해결되는 부분임을 안심시킬 때(구어·설명)
- 한국어: 알아서 해결된다, 신경 쓸 필요 없다
- 설명: 설계 설명의 마무리에 자주 온다 — 사람이 챙길 일과 시스템이 알아서 하는 일을 갈라 줄 때. "register just your office PC's hostname — the cloud takes care of itself."
- 예문: Register just your office PC's hostname — the cloud takes care of itself.
- 유사어: sorts itself out (영국식 색채, 같은 뜻), is handled automatically (격식·문어), no action needed on X (보고서식)

## "a deliberate act"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 위험한 동작이 실수로는 일어날 수 없고 의도적으로만 가능하게 설계했음을 강조할 때(설계 근거·문어)
- 한국어: 의도적인 행위(실수가 아니라)
- 설명: 안전 설계를 설명하는 열쇠말. "that stays a deliberate act"는 "기본값으로는 안 일어나고, 하려면 명시적으로 해야 한다"는 뜻을 한 구로 전달한다.
- 예문: When you do want office data from home, that stays a deliberate act: set the one feature's env var explicitly.
- 유사어: an explicit opt-in (기본 꺼짐+명시적 선택), a conscious decision (판단의 뉘앙스), intentional (형용사 한 단어)
- 반의어: an accident / a silent default

## "flagged, not broken"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 리뷰에서 "지적은 해 두지만 고장은 아니다"라고 심각도를 명확히 구분할 때(문어·리뷰 보고)
- 한국어: 표시만 해 둔 것이지 고장난 게 아님
- 설명: "X, not Y" 대구로 판정의 수위를 압축한다. 발견 사항을 나열할 때 독자가 "그래서 고쳐야 하나?"를 되묻지 않게 해 준다. flag는 "문제 가능성을 표시하다"라는 리뷰 동사.
- 예문: The scope-creep items are coordinated end-to-end and documented — flagged, not broken.
- 유사어: noted, not blocking (머지 관점의 수위 표현), cosmetic only (겉모습 문제일 뿐), worth knowing (조치 불요 정보)

## "gloss over"
- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt e65e5c9a
- 맥락: 불리하거나 귀찮은 사실을 얼버무리고 넘어가는 행동(주로 "하지 않았다"는 부정문으로 정직함을 강조)
- 한국어: 얼버무리고 넘어가다, 대충 덮다
- 설명: "one honest caveat I documented rather than glossed over"처럼 rather than과 짝지으면 "숨기지 않고 기록했다"는 신뢰의 문장이 된다.
- 예문: One honest caveat I documented rather than glossed over: the favorites store is not yet migrated to the factory.
- 유사어: paper over (결함을 임시로 가리다), sweep under the rug (은폐 뉘앙스 강함), brush aside (지적을 무시하다)
- 반의어: call out / surface (드러내 짚다)

## "an open loop"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 끝나지 않고 걸려 있는 일감을 가리키는 말(작업 인수인계·GTD 문화권 용어)
- 한국어: 미결 항목, 열려 있는 일
- 설명: "닫히지 않은 회로"의 은유. done list의 반대편에 있는 것들 — 진행 중·차단됨·시작 전 — 을 통칭한다. "a clean list of open loops, not a record of what got done."
- 예문: The goal is a clean list of open loops, not a record of what got done.
- 유사어: an open item (회의록 용어), unfinished business (구어적·극적), a loose end (마무리 안 된 자잘한 끝단)
- 반의어: closed out / done and dusted

## "a launchpad, not a diary"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 문서의 목적을 대비로 정의할 때 — 기록용이 아니라 다음 행동의 출발대(문어·가이드라인)
- 한국어: 일기장이 아니라 발사대
- 설명: "A, not B" 은유 대구의 좋은 견본. 문서 성격 논쟁("이거 너무 길어요")을 은유 하나로 정리한다. 인수인계 노트·회의록·README 어디에나 응용 가능.
- 예문: Keep it under 25 lines — this is a launchpad, not a diary.
- 유사어: forward-looking, not retrospective (풀어쓴 격식 버전), actionable, not archival (같은 대구 구조)

## "Specific beats complete."
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 두 미덕이 충돌할 때 우선순위를 격언 형태로 선언(가이드라인·문어)
- 한국어: 빠짐없는 것보다 구체적인 게 낫다
- 설명: "X beats Y"는 우선순위 격언의 생산적인 틀 — "Done beats perfect", "Clarity beats cleverness"처럼 무한 응용된다. 동사 하나로 비교급 문장을 대체해 단호하게 들린다.
- 예문: Specific beats complete: "next: add MAD slider min/step, AnalyzePanel.vue:120" is worth more than a paragraph.
- 유사어: X trumps Y (같은 구조, 조금 격식 위), better X than Y (평이한 버전)

## "smells like ..."
- 레지스터: conversational, technical
- 출처: transcript:skewnono_v3_nuxt 92aad678
- 맥락: 확증 전이지만 증상 패턴이 특정 원인을 가리킬 때의 조심스러운 추정(디버깅 구어)
- 한국어: ~냄새가 난다, ~같아 보인다
- 설명: "code smell"의 동사 버전. "which smells like pytest-randomly reshuffling order"처럼 쓰면 "추정 단계"임을 자연스럽게 표시하면서 다음 검증 행동(순서 고정해 보자)으로 이어진다.
- 예문: The results differ run-to-run, which smells like the test runner reshuffling execution order.
- 유사어: looks like (더 중립), points to (증거가 가리킨다 — 확신 조금 위), reeks of (냄새가 지독하다 — 강한 부정 평가)

## "a type wanting to be born"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2 (code-review 스킬의 Data Clumps 해설)
- 맥락: 같은 필드 몇 개가 늘 붙어 다니면 타입으로 묶으라는 리팩터링 신호를 의인화해 말할 때(문어·기술)
- 한국어: 태어나고 싶어 하는 타입(타입으로 묶일 때가 된 데이터 뭉치)
- 설명: Fowler의 Data Clumps 냄새를 설명하는 생생한 의인화. "the same few fields keep travelling together — a type wanting to be born." 추상 개념에 의지를 부여하는 영어 특유의 수사다.
- 예문: The same three params keep travelling together across these functions — that's a type wanting to be born.
- 유사어: begging to be extracted (추출을 애원한다 — 같은 의인화), a missing abstraction (밋밋한 격식 버전)

## "How far do you want me to go?"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 92aad678
- 맥락: 작업 범위가 예상보다 커졌을 때, 실행 전에 상대에게 범위 결정을 넘기는 질문(구어·채팅)
- 한국어: 어디까지 할까요?
- 설명: 계약(contract)까지 건드리는 큰 변경 앞에서 "Before I touch cross-phase contracts, how far do you want me to go?"처럼 쓰면 신중함과 주도권 존중을 동시에 전달한다.
- 예문: This rename touches four features and the shared contracts — how far do you want me to go?
- 유사어: What's in scope? (범위 확인의 명사형), Should I stop here or keep going? (평이한 버전), up to you (결정권 이양의 최단형)

## "a job that has been rotting"
- 레지스터: conversational, professional
- 출처: transcript:skewnono_v3_nuxt 1b71ccc2
- 맥락: 손대지 않은 채 며칠씩 방치되어 상해 가는 일감을 지적할 때(구어적 은유, 내부 문서)
- 한국어: 썩어 가는(방치된) 일감
- 설명: stale(신선하지 않은)보다 한 단계 더 나간 부패의 은유. since 날짜를 남기는 이유를 "that date is how you spot a job that has been rotting"으로 설명하면 규칙에 서사가 생긴다.
- 예문: Keep the original since date — that date is how you spot a job that has been rotting.
- 유사어: going stale (표준적·중립), languishing (격식 위 — 방치되어 시들다), gathering dust (먼지 쌓이다 — 물건·계획에)
- 반의어: actively worked / fresh
