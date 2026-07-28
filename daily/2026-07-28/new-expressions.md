# 2026-07-28 — 새 표현

## "off the table"
- 레지스터: conversational, professional
- 출처: transcript: flask-modules (Redis 락 디버깅)
- 맥락: 어떤 선택지·가능성이 논의 대상에서 완전히 빠졌음을 알릴 때(회의·구어 양쪽)
- 한국어: (선택지에서) 완전히 배제된
- 설명: 협상 테이블 은유. "Manual dispatch is off the table entirely"처럼 원인 후보를 하나씩 지워가는 진단 대화에서 특히 자연스럽다. 반대로 아직 살아 있는 선택지는 on the table.
- 예문: With every job set to `manual_dispatch: False`, manual dispatch is off the table entirely.
- 유사어: ruled out (검증을 거쳐 배제한 뉘앙스), not an option (더 평이함)
- 반의어: on the table (아직 검토 대상인)

## "a footgun"
- 레지스터: casual, technical
- 출처: transcript: flask-modules
- 맥락: 정상 기능이지만 쓰는 사람이 제 발등을 찍기 쉬운 설계를 가리킬 때(개발자 속어)
- 한국어: 제 발등 찍기 좋은 기능·설계
- 설명: "발에 쏘는 총"이라는 조어. 버그가 아니라 *합법적인* 기능인데 오용이 너무 쉬울 때 쓴다. "they make `FLUSHDB` a footgun" — 번호 DB를 쓰면 엉뚱한 DB를 통째로 지우기 쉬워진다는 맥락.
- 예문: Numbered Redis databases aren't a security boundary, and they make `FLUSHDB` a footgun.
- 유사어: a sharp edge (더 중립적·문어에도 무난), a trap (일반어)
- 반의어: safe-by-default (기본값이 곧 안전한 설계)

## "worth chasing"
- 레지스터: conversational
- 출처: transcript: flask-modules
- 맥락: 조사할 가치가 있는 단서와 무시해도 되는 신호를 가를 때(디버깅 구어)
- 한국어: 파고들 가치가 있는
- 설명: chase(추적하다)를 써서 "이건 쫓아가 볼 단서다"라는 어감. "Only two patterns are bugs worth chasing"처럼 노이즈 속에서 진짜 문제를 골라낼 때 쓴다.
- 예문: Genuine contention still produces `lock held` rows — only two patterns are bugs worth chasing.
- 유사어: worth digging into (더 깊이 파는 어감), worth pursuing (격식 한 단계 위)
- 반의어: not worth the trouble (수고 대비 무가치)

## "stagger"
- 레지스터: technical, professional
- 출처: transcript: flask-modules
- 맥락: 동시에 몰리는 작업·일정의 시작 시각을 서로 어긋나게 배치할 때(스케줄링·운영)
- 한국어: 시차를 두어 엇갈리게 배치하다
- 설명: 출근 시차제(staggered hours)에도 쓰는 동사. cron 잡 8개가 정각에 몰리지 않게 "stagger the `minute=` values"라고 하면 "분 값을 서로 다르게 벌려라"는 뜻이 된다.
- 예문: If you see gaps with no rows, stagger the `minute=` values rather than raising the pool.
- 유사어: spread out (일반어), offset (기준점에서 어긋냄), space out (간격 띄우기)
- 반의어: coincide (같은 순간에 겹치다)

## "age out (of something)"
- 레지스터: technical
- 출처: transcript: flask-modules
- 맥락: 보존 기간·용량 한도에 밀려 오래된 데이터가 자연히 빠져나갈 때(문어·구어 모두)
- 한국어: 오래되어 (목록·보존 구간에서) 밀려나다
- 설명: 사람이 나이 제한으로 자격을 잃는 데서 온 표현을 데이터에 적용한 것. "it ages out of the 500-record list" — 지우는 주체 없이 시간이 해결한다는 어감이 핵심.
- 예문: The split history is cosmetic, and it ages out of the 500-record list on its own.
- 유사어: roll off (롤링 윈도에서 떨어져 나감), expire (TTL 만료·더 즉각적)
- 반의어: be retained (보존되다)

## "take something on trust"
- 레지스터: professional, conversational
- 출처: transcript: flask-modules
- 맥락: 남의 보고·리뷰 결과를 검증 없이 믿는 것을 거부할 때(엔지니어링 문화)
- 한국어: 검증 없이 믿다
- 설명: "Let me verify that first finding against the actually-installed redis-py rather than take it on trust" — 리뷰 에이전트의 지적조차 소스로 확인하겠다는 태도 표명. rather than과 짝을 이루는 경우가 많다.
- 예문: Let me verify that finding against the installed source rather than take it on trust.
- 유사어: take at face value (액면 그대로 믿다), take someone's word for it (구어)
- 반의어: verify firsthand (직접 확인하다)

## "carry something over (to)"
- 레지스터: conversational, professional
- 출처: transcript: flask-modules
- 맥락: 한 환경에서 만든 것을 다른 환경·다음 기간으로 옮겨 갈 때(구어)
- 한국어: (다른 곳으로) 그대로 가져가다, 이월하다
- 설명: 집 sandbox에서 만든 수정을 사무실 코드로 옮기는 흐름 전체가 이 동사로 굴러간다 — "so you can carry them over", "What you're carrying to the office". 회계의 이월(carryover)과 같은 뿌리.
- 예문: Let me implement the three changes here so you can carry them over to your office copy.
- 유사어: port (코드 이식·기술어), transplant (수술 은유·더 강함)
- 반의어: leave behind (두고 가다)

## "unlearn"
- 레지스터: conversational, professional
- 출처: transcript: flask-modules
- 맥락: 몸에 밴 잘못된 습관·직관을 의식적으로 버려야 할 때
- 한국어: (잘못 익힌 것을) 도로 배워서 버리다
- 설명: learn에 un-을 붙인 조어지만 표준 어휘다. "The trap to unlearn: never set `lock_ttl` below your job's runtime" — 단순히 "하지 마라"가 아니라 "그렇게 배워 온 직관 자체를 지워라"는 강한 교정.
- 예문: The trap to unlearn: never set `lock_ttl` below your job's runtime hoping to dodge skips.
- 유사어: break the habit (습관 차원), shed (a belief) (문어)
- 반의어: internalize (몸에 익히다)

## "over-specified"
- 레지스터: technical
- 출처: transcript: flask-modules
- 맥락: 테스트·계약이 실제로 의존하지 않는 사실까지 못박아 둔 것을 비판할 때(문어·리뷰)
- 한국어: 필요 이상으로 세부를 못박은
- 설명: "over-specified assertions — pinning a fact the code doesn't depend on". `datetime64[ns]`처럼 코드가 의존하지 않는 해상도를 단언하면 pandas 업그레이드만으로 깨진다. 스펙 과잉이 취약성을 만든다는 진단어.
- 예문: Two of these were over-specified assertions rather than real defects — pinning a fact the code doesn't depend on.
- 유사어: brittle (깨지기 쉬운·결과 쪽 표현), overly strict (일반어)
- 반의어: under-specified (덜 정해져 모호한)

## "self-resolving"
- 레지스터: technical, professional
- 출처: transcript: flask-modules
- 맥락: 배포 후 생기는 일시적 부작용이 개입 없이 사라진다고 안심시킬 때
- 한국어: 저절로 해소되는
- 설명: "Two one-time effects, both self-resolving" — 락 키 변경으로 생기는 짧은 창과 대시보드 이력 분리가 각각 TTL 만료와 age-out으로 알아서 정리된다는 맥락. 마이그레이션 안내문에서 유용하다.
- 예문: Both effects are one-time and self-resolving — stale locks expire within `lock_ttl` on their own.
- 유사어: self-healing (시스템이 능동 복구하는 어감), transient (일시적·원인 서술)
- 반의어: requiring manual cleanup (손으로 치워야 하는)

## "size X off Y"
- 레지스터: technical, conversational
- 출처: transcript: flask-modules
- 맥락: 설정값의 크기를 어떤 기준량에서 유도해 정할 때(구어형 기술 표현)
- 한국어: Y를 기준으로 X의 크기를 정하다
- 설명: "Size `lock_ttl` off the **trigger interval** instead" — off가 "~로부터"의 파생 관계를 나타낸다. base X on Y의 구어·압축형으로, 튜닝 가이드에서 빈번하다.
- 예문: You don't need to know your job runtimes anymore — size `lock_ttl` off the trigger interval instead.
- 유사어: base X on Y (표준형), derive X from Y (격식 한 단계 위)

## "have no business doing X"
- 레지스터: conversational, professional
- 출처: transcript: flask-modules
- 맥락: 어떤 주체가 그 일을 할 자격·소관이 아예 없다고 단언할 때(설계 원칙 표명)
- 한국어: ~할 자격·소관이 전혀 없다
- 설명: "A generic lock primitive has no business naming the caller's work" — 범용 락이 호출자의 작업 이름을 짓는 건 월권이라는 책임 분리 선언. 사람에게 쓰면 힐난이 되지만 모듈·계층에 쓰면 깔끔한 설계 언어가 된다.
- 예문: A generic lock primitive has no business naming the caller's work.
- 유사어: it's not X's place to (사람 쪽에 자연스러움), out of scope for (중립·격식)
- 반의어: it's X's job to (마땅히 X의 몫이다)

## "a bet on X / stop betting"
- 레지스터: conversational, technical
- 출처: transcript: flask-modules
- 맥락: 설정값이 미래의 불확실한 값을 찍어 맞히는 도박이 되어 버렸음을 지적할 때
- 한국어: X에 거는 도박 / 도박을 그만두다
- 설명: "the current design forces `lock_ttl` to be a bet on that runtime... The fix is to stop betting." 낮게 걸면 침묵 동시 실행, 높게 걸면 orphan 폭주 — 양쪽 다 지는 도박이니 구조로 판을 없애라는 논법. 은유 하나로 설계 결함을 요약한다.
- 예문: The current design forces `lock_ttl` to be a bet on runtime — the fix is to stop betting and renew the TTL while the job runs.
- 유사어: a gamble on (일반어), guesswork (찍기·불확실성 강조)
- 반의어: a guarantee (보장)

## "the only arbiter"
- 레지스터: professional
- 출처: transcript: flask-modules
- 맥락: 여러 주체가 다툴 때 최종 판정 권한이 어디에 있는지 지목할 때(문어·격식)
- 한국어: 유일한 판정자
- 설명: arbiter는 중재·판정하는 주체. "Redis is the only arbiter" — 워커들이 서로의 상태를 볼 수 없으니 락의 승패는 Redis만 가른다는 뜻. 분산 시스템 설명에서 "single source of truth"의 판정 버전.
- 예문: On workers 2–4 the dispatch can't see the scheduler's in-flight jobs; Redis is the only arbiter.
- 유사어: the final authority (더 일반적), the tie-breaker (동점 상황 한정)

## "turn up (something)"
- 레지스터: conversational
- 출처: transcript: flask-modules
- 맥락: 조사·검색이 뜻밖의 것을 발견해 낼 때(구어)
- 한국어: (조사가) ~을 캐내다, 찾아내다
- 설명: "Checking the other `fn.__name__` sites turned up a live bug" — 주어가 사람이 아니라 *조사 행위*인 게 포인트. 자동사로 쓰면 "검색에 안 나온다"(nothing turned up)가 된다.
- 예문: Checking the other call sites turned up a live bug beyond the lock key.
- 유사어: uncover (격식 한 단계 위), surface (떠오르게 하다·타동)
- 반의어: come up empty (아무것도 못 찾다)

## "provision (v.)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-27-opensearch-logging-activity.md
- 맥락: 인프라 자원(인덱스·계정·서버)을 미리 만들어 준비할 때(문어·운영)
- 한국어: (인프라를) 사전 구축하다
- 설명: 명사 provision(공급)에서 온 동사로, 클라우드·운영 문서의 표준어. "A one-time script provisions local and production aliases" — create보다 "쓸 수 있게 갖춰 둔다"는 준비의 어감이 강하다.
- 예문: A one-time script under `ops_index_mgmt/` provisions local and production aliases on the same company cluster.
- 유사어: set up (일반어), stand up (a cluster) (구어·운영 속어)
- 반의어: decommission (해체하다)
