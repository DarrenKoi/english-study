# 2026-07-21 — 수집한 표현

## "a red herring"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (redis parquet 디버깅)
- 맥락: 디버깅에서 "이건 진짜 원인이 아니라 눈길을 끄는 헛단서"라고 짚을 때(구어·기술 토론)
- 한국어: 진짜 원인에서 주의를 돌리는 가짜 단서.
- 설명: 추리소설에서 유래한 관용구. 눈에 띄는 증상(여기선 바이트 `0xb6`)이 사실 원인과 무관할 때 쓴다.
- 예문: The `0xb6` is a red herring; the real question is what `pickle.loads` actually raised.
- 유사어: a false lead (수사·추적 뉘앙스), a distraction (더 일반적), a wild goose chase (헛수고까지 함의)
- 반의어: the smoking gun (결정적 증거), the tell (결론을 드러내는 단서)

## "my money is on X"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (원인 추정)
- 맥락: 확정 전이지만 "가장 그럴 법한 쪽"을 걸듯 자신 있게 추측을 밝힐 때(구어)
- 한국어: 나는 X 쪽에 건다 — 가장 유력하다고 본다.
- 설명: 도박에서 온 표현. 단정하지 않으면서도 확신의 정도를 담아 예측할 때 쓴다.
- 예문: My money is on the first case — a formatting difference in the `.env` line, since the host and port clearly loaded.
- 유사어: I'd bet (that) … (거의 동일, 약간 더 가벼움), my best guess is …, I'd wager (격식·문어)
- 반의어: it's anyone's guess (전혀 못 짚겠다)

## "belong in / belong to"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (자격증명 위치 판단)
- 맥락: "이건 원래 여기에 있어야 마땅하다"고 올바른 위치·소관을 짚을 때(격식·구어 공용)
- 한국어: ~에 (마땅히) 있어야 한다 / ~의 소관이다.
- 설명: `belong in`은 물리적·논리적 위치("여기 들어가야 한다"), `belong to`는 소유·소속("~의 것/~의 몫")으로 갈린다. 규범적 당위를 담백하게 말할 때 유용.
- 예문: Those are real credentials, so they belong in the gitignored `.env`, not in any tracked file.
- 유사어: should live in (구어에서 자주), is the right home for, is the job of (소관을 말할 때)
- 반의어: has no business being in (있어선 안 된다)

## "prove out (end to end)"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (마이그레이션 검증 마일스톤)
- 맥락: 계획·설계가 실전에서 실제로 통함이 처음부터 끝까지 입증됐다고 회고할 때(격식)
- 한국어: (실전에서) 통함이 입증되다 / 검증되다.
- 설명: 자동사 `prove out`은 "이론이 실측으로 확인되다". `end to end`가 붙으면 부분이 아니라 전 구간이 검증됐음을 강조한다.
- 예문: That's the whole three-phase migration strategy proving out end to end: mock → office by configuration alone, no frontend changes.
- 유사어: pan out (구어, "결국 잘 풀리다"), bear out (증거가 뒷받침하다), hold up (검증을 견디다)
- 반의어: fall apart (무너지다), not pan out

## "ripple through"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (타입 변경 파급)
- 맥락: 한 곳의 변경이 여러 파일·계층으로 연쇄적으로 번질 때(설계·리팩터링)
- 한국어: (변경이) 파급되어 번지다.
- 설명: 물결(ripple)이 퍼지는 이미지. 한 결정이 왜 여러 곳을 건드리는지 설명할 때 자연스럽다.
- 예문: Version is a string, not an int — this rippled through four files, because the contract is the shared truth between mock and office.
- 유사어: propagate (더 중립·기술적), cascade (연쇄·순차 강조), fan out (여러 갈래로 퍼짐)
- 반의어: stay contained / be self-contained (한 곳에 갇히다)

## "an orphan (nothing reads it)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (미참조 픽스처)
- 맥락: 코드·데이터 자산이 아무 데서도 참조되지 않아 사실상 죽어 있음을 지적할 때(기술)
- 한국어: 아무도 참조하지 않는 고아(죽은) 자산.
- 설명: 명사 `orphan` 또는 형용사 `orphaned`로 쓴다. "고쳐도 아무 테스트가 안 깨진다"는 근거와 함께 삭제·방치를 정당화할 때 자주 등장.
- 예문: Confirmed: the fixture is an orphan (nothing reads it), so no test forces its update.
- 유사어: dead code (실행 안 되는 코드), a dangling reference (끊긴 참조), unreferenced
- 반의어: load-bearing (떠받치는, 건드리면 무너지는), actively used

## "wire up (X to Y)"
- 레지스터: technical
- 출처: transcript:[user]/[assistant] skewnono_v3_nuxt ("wire up storage page to the office db")
- 맥락: 프런트·기능을 실제 데이터 소스·백엔드에 연결해 동작하게 만들 때(기술·구어)
- 한국어: ~를 ~에 (배선하듯) 연결하다.
- 설명: 전선을 잇는 이미지에서 온 개발 은어. UI를 API·DB에 붙여 실데이터가 흐르게 하는 작업을 가리킨다.
- 예문: sem_list is now the first SKEWNONO feature wired to office Redis, rendering live on the 장비 리스트 page.
- 유사어: hook up (더 캐주얼), connect (중립), plumb through (배관 은유; 값을 계층 관통시켜 넘기다)
- 반의어: stub out (실연결 없이 가짜로 막아 두다), mock

## "a blanket try/except"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (예외 처리 안티패턴)
- 맥락: 예외를 종류 안 가리고 다 잡아 진짜 원인을 가리는 코드를 비판할 때(코드 리뷰)
- 한국어: 무차별로 다 잡는 예외 처리(안티패턴).
- 설명: `blanket`은 "담요처럼 전부 덮는". 좁게 잡아야 할 예외를 뭉뚱그려 삼키면 원인이 숨는다는 맥락에서 쓴다.
- 예문: The old deserializer did `pickle.loads` in a blanket `try`, and on any failure blindly ran `raw.decode("utf-8")`.
- 유사어: a catch-all except, over-broad exception handling, swallow an exception (결과 쪽 초점)
- 반의어: a narrow/targeted except (좁게 특정 예외만 잡기)

## "choke on (something)"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (디코딩 실패)
- 맥락: 파서·함수가 특정 입력을 처리하지 못하고 턱 막혀 실패할 때(기술)
- 한국어: (특정 입력을) 처리 못 하고 턱 막히다.
- 설명: 음식이 목에 걸리는 이미지. 어떤 입력에서 코드가 막히는지를 생생하게 전달한다.
- 예문: It blindly ran `raw.decode("utf-8")` — which choked on the binary parquet bytes at `0xb6` and hid what actually went wrong.
- 유사어: barf on (더 속어), fail on, trip over (걸려 넘어지다)
- 반의어: handle gracefully (매끄럽게 처리하다), digest

## "fail loudly (with actionable messages)"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (검증 설계)
- 맥락: 오류를 조용히 넘기지 않고 원인·다음 행동까지 알려주며 요란하게 실패시키자고 할 때(설계 원칙)
- 한국어: 조용히 넘기지 말고 (조치 가능한 메시지로) 요란하게 실패시키다.
- 설명: `fail fast`와 짝을 이루는 방어적 설계 격언. 실패를 감추는 것보다 크게 드러내 빨리 고치게 하는 편이 낫다는 뜻.
- 예문: Validation fails loudly with actionable messages: a missing key tells you which env vars to check.
- 유사어: fail fast (조기 실패), surface the error (원인을 드러내다), crash hard (극단적으로)
- 반의어: fail silently (조용히 실패), swallow an exception, quietly expensive

## "point me at (something)"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (다음 작업 요청)
- 맥락: "무엇을 봐야 할지 알려주면 내가 하겠다"고 대상을 가리켜 달라 청할 때(구어·협업)
- 한국어: ~를 (콕 집어) 알려줘 / 가리켜 줘.
- 설명: 손가락으로 가리키는 이미지. 자원·파일·이슈의 위치만 주면 나머지는 맡겠다는 협업 화법.
- 예문: When you're ready to connect the next feature, point me at its Redis key(s) and I'll follow the same path.
- 유사어: send me (the link), tell me where (…is), just show me
- 반의어: figure it out myself (내가 알아서 찾다)

## "stacked on top of each other"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (근본 원인 분석)
- 맥락: 하나로 보였던 증상이 사실 별개의 원인 여럿이 겹쳐 생겼음을 밝힐 때(디버깅)
- 한국어: (원인·문제가) 겹겹이 포개져 있다.
- 설명: 얽힌 버그를 풀 때 "증상은 하나인데 원인은 층층이"라는 상황을 그린다. 각 층을 하나씩 벗겨 설명하는 서두로 좋다.
- 예문: The root cause was two separate things stacked on top of each other.
- 유사어: compounding (서로 증폭), layered, intertwined (얽힘 강조)
- 반의어: a single root cause (단일 원인)

## "the first place to check"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (분류 규칙 설명)
- 맥락: 특정 증상이 나타나면 어디부터 살펴야 하는지 진단 출발점을 일러줄 때(구어·격식)
- 한국어: 가장 먼저 확인해 볼 곳.
- 설명: 문제 진단의 우선순위를 담백하게 지목하는 표현. "If X happens, that's the first place to check" 형태로 자주 쓴다.
- 예문: If office equipment ever shows up missing from the lists, that prefix rule is the first place to check.
- 유사어: the usual suspect (흔한 범인), where I'd start, the prime suspect
- 반의어: a last resort (최후에야 볼 곳)

## "a de-dup guard"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (merge 중복 방지)
- 맥락: 조인·병합 등에서 중복 행이 유입되는 것을 막으려 미리 넣는 방어 코드를 가리킬 때(데이터 처리)
- 한국어: 중복 유입을 막는 방어 장치.
- 설명: `de-dup`은 deduplicate의 축약. left join이 오른쪽 중복 키 때문에 행을 불릴 수 있어 미리 유일화해 두는 조치를 이렇게 부른다.
- 예문: A left join still multiplies a left row if the right side has duplicate keys, so I added a de-dup guard before merging.
- 유사어: a uniqueness constraint (DB 층), collapse to one row per key (동작 서술)
- 반의어: (마땅한 대체 표현 없음)
