# 2026-08-07 — 새 표현

## "survive injected faults"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-06-loop-failure-path-hardening.md
- 맥락: 설계 문서에서 목표를 한 줄로 못 박을 때(격식 있는 문어체). 장애를 "기다리는" 게 아니라 "일부러 주입해서" 견디는지 본다는 뜻이 핵심.
- 한국어: 일부러 집어넣은 결함을 견디고 살아남다
- 설명: `injected`가 "인위적으로 넣은"을 뜻해서, 우연히 생긴 장애(observed failure)와 명확히 구분된다. 카오스 테스트·fault injection 문맥의 표준 표현.
- 예문: The goal is to make the real-time loop survive injected faults, so teardown always completes even when a step throws.
- 유사어: withstand simulated failures (더 중립적), hold up under fault injection (구어에 가까움), be resilient to induced errors (가장 격식)
- 반의어: fall over on the first error

## "a refinement chain, not a vote"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator VLM 두 단계 검토
- 맥락: 두 모델·두 검사가 "서로 검증한다"는 통념을 반박할 때. 코드 리뷰나 설계 논쟁에서 상대의 전제를 정확히 되짚는 자리.
- 한국어: 서로 표를 던지는 게 아니라 앞 결과를 다듬기만 하는 사슬
- 설명: `A, not B` 대조 구문으로 오해를 한 문장에 정정한다. 뒷 단계가 앞 단계의 출력에만 의존하면 독립성이 없다는 논지를 압축한 말.
- 예문: The two models never independently agree — it's a refinement chain, not a vote, because the second one only sees a crop derived from the first.
- 유사어: a pipeline, not a cross-check (더 평이), sequential rather than independent (격식·중립)
- 반의어: an independent cross-check

## "silently downgraded to X"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator 스코어러 버그 설명
- 맥락: 버그가 오류를 내지 않고 결과의 등급만 슬쩍 낮출 때. 로그를 봐도 안 보이는 종류의 결함을 지적하는 자리.
- 한국어: 오류 없이 조용히 한 등급 낮게 처리되다
- 설명: `silently`가 "예외도 로그도 없이"를 담당한다. 측정 도구 자체가 신호를 잃는 상황을 가리켜, 그냥 wrong 보다 훨씬 무섭다는 뉘앙스.
- 예문: The exact case the bench exists to measure was silently downgraded to "couldn't tell."
- 유사어: quietly reclassified as (거의 동의), swallowed as a lesser error (구어)
- 반의어: surfaced as a hard failure

## "so this can't quietly revert"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator 회귀 테스트 추가 설명
- 맥락: 테스트를 왜 넣었는지 한 줄로 정당화할 때. 코드 리뷰 대화에서 자주 쓰인다.
- 한국어: 이게 슬그머니 원래대로 돌아가지 못하게
- 설명: `revert`의 주어가 사람이 아니라 상태라는 점이 재미있다. 누가 되돌린 게 아니라 조건이 바뀌며 저절로 무력화되는 상황까지 포함한다.
- 예문: The test asserts the crop stays under three rows, so this can't quietly revert to the old behavior.
- 유사어: so the fix can't erode (비유적), to pin the behavior down (더 평이)
- 반의어: leave it to convention

## "the weak link"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 단계별 실패 분석
- 맥락: 여러 단계 중 어디가 문제인지 지목할 때. 회의 구어와 보고서 양쪽에서 통한다.
- 한국어: 가장 약한 고리, 병목이 되는 지점
- 설명: chain 은유의 관용구라 `weakest link`도 되지만, 후보가 둘일 때는 `the weak link`가 더 자연스럽다.
- 예문: If the coarse stage refuses to ground, the coarse model is the weak link and the fine model never gets a chance.
- 유사어: the bottleneck (성능 쪽), the failure point (더 중립), where it breaks down (구어)
- 반의어: the reliable leg

## "deliberate friction"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 커서 벤치 opt-in 설명
- 맥락: 일부러 불편하게 만든 설계를 변호할 때. 안전장치를 설명하는 문어체.
- 한국어: 의도적으로 넣은 마찰(번거로움)
- 설명: friction 은 UX에서 보통 나쁜 것이지만 `deliberate`가 붙으면 미덕이 된다. "실수로는 못 켜게" 라는 뜻을 두 단어로 전달.
- 예문: The cursor arm stays behind an explicit env flag — that's deliberate friction, since it's the only part that moves the physical mouse.
- 유사어: an intentional speed bump (구어·비유), a guard rail (보호 뉘앙스가 더 큼)
- 반의어: a frictionless default

## "declined to answer"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator `nodet` 정의
- 맥락: 모델·시스템이 틀린 게 아니라 아예 응답을 거부한 경우를 구분할 때.
- 한국어: (틀린 게 아니라) 답하기를 거부했다
- 설명: 사람에게 쓰는 동사를 모델에 그대로 써서 "실수(mistake)"와 "거부(refusal)"를 가른다. 이 구분이 곧 후속 조치를 가른다.
- 예문: Nothing was clicked and nothing was scored wrong — the model simply declined to answer.
- 유사어: returned nothing (평이), abstained (통계·투표 은유), refused to ground (도메인 한정)
- 반의어: answered confidently but wrongly

## "that's the oracle failing, not the models"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator 벤치 결과 해석 주의사항
- 맥락: 측정 결과가 나쁠 때 "측정 대상"이 아니라 "측정 도구"를 의심하라고 미리 경고하는 자리.
- 한국어: 그건 모델이 아니라 채점 기준(정답 판정기)이 실패한 것이다
- 설명: oracle 은 테스트에서 "정답이 무엇인지 알려주는 장치"를 뜻하는 용어다. `X, not Y` 대조로 책임 소재를 옮긴다.
- 예문: If a button is icon-only, every combo scores unreadable — that's the oracle failing, not the models.
- 유사어: a measurement artifact (더 격식), my scoring code giving up (구어·자기지시)
- 반의어: a genuine capability gap

## "my change was cosmetic"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 크롭 패딩 수정 회고
- 맥락: 자기 수정이 겉만 바뀌고 실제 동작은 그대로였다고 인정할 때. 자기비판을 짧고 담담하게 하는 어조.
- 한국어: 내 수정은 겉치레였다(실효가 없었다)
- 설명: cosmetic 은 "화장품의"에서 온 말이라 "표면만 손댄"의 은유가 살아 있다. 숫자만 바꾸고 하한선(floor)에 막혀 무효였던 상황에 딱 맞는다.
- 예문: Lowering the ratio changed nothing — my first attempt at this was cosmetic, and I caught it before shipping.
- 유사어: a no-op in practice (기술적), it didn't move the needle (구어 관용구)
- 반의어: a substantive change

## "one feature reading as two"
- 레지스터: technical, professional
- 출처: transcript:skewnono_v3_nuxt 로그 feature slug 버그
- 맥락: 데이터가 잘못 분류돼 하나가 둘로 쪼개져 보이는 현상을 요약할 때. 버그 리포트의 결론 문장.
- 한국어: 한 기능이 둘로 갈려 기록되는 것
- 설명: `read as`는 "~로 읽힌다/보인다"라는 수동적 관찰 동사다. 시스템이 그렇게 보고한다는 뜻이지 실제로 둘이라는 뜻이 아니다.
- 예문: The API path fell through to the fallback and was filed as `cdsem` — one feature reading as two.
- 유사어: a split identity in the logs (설명적), double-counted under two slugs (더 구체적)
- 반의어: consolidated under one slug

## "nothing backfills them"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 배포 운영 노트
- 맥락: 버그를 고쳐도 과거 데이터는 그대로라고 미리 알려줄 때. 운영 공지의 정형구.
- 한국어: 과거 데이터를 소급해 채워 넣는 장치는 없다
- 설명: backfill 은 데이터 파이프라인 용어로 "지난 구간을 다시 계산해 채우기"다. `nothing`을 주어로 세워 "아무도 안 한다"를 단정적으로 전달.
- 예문: Rows already in the index keep the old value; nothing backfills them, so a window spanning the deploy will show both.
- 유사어: historical rows are left as-is (평이), no retroactive migration (격식)
- 반의어: a one-off backfill job reindexes the history

## "the schema of record"
- 레지스터: professional, technical
- 출처: transcript:skewnono_v3_nuxt mag-pixel 문서 갱신
- 맥락: 같은 사실이 여러 곳에 있을 때 어디가 기준인지 못 박는 자리. 설계 문서·리뷰 코멘트.
- 한국어: 기준이 되는 스키마(정본)
- 설명: `system of record`(정본 시스템)에서 파생된 표현. `of record`가 "공식적으로 인정된"을 뜻하는 후치 수식어다.
- 예문: The mag-pixel feature is frontend-only, with `cdsem_mag_pixel_table.txt` as the schema of record.
- 유사어: the single source of truth (더 흔함), the authoritative definition (격식)
- 반의어: a derived copy

## "the right move is deletion, not inversion"
- 레지스터: professional
- 출처: transcript:skewnono_v3_nuxt `MAG_GT_ASSUMED` 제거 결정
- 맥락: 플래그를 `false`로 두는 대신 아예 지우자고 설득할 때. 리팩터링 판단을 한 줄로 요약.
- 한국어: 값을 뒤집을 게 아니라 지우는 게 맞다
- 설명: 명사 두 개(deletion / inversion)를 맞세워 선택지를 대비시킨다. 뒤집기만 하면 도달 불가능한 코드가 남아 다음 사람이 "복원"하려 든다는 논거가 뒤따른다.
- 예문: If the predicate were left hardcoded to false, the badge and its tests would become unreachable code — the right move is deletion, not inversion.
- 유사어: remove it rather than neutralize it (평이), rip it out instead of flipping it (구어)
- 반의어: keep it and flip the default

## "repeats aren't padding"
- 레지스터: conversational, technical
- 출처: transcript:auto_recipe_creator 벤치 읽는 법 안내
- 맥락: 반복 측정이 왜 낭비가 아닌지 먼저 방어할 때. 상대가 "굳이 3번씩?"이라 물을 걸 예상한 선제 문장.
- 한국어: 반복 실행은 자리 채우기가 아니다
- 설명: `padding`은 분량 부풀리기를 뜻해서, "쓸데없이 늘린 것"이라는 예상 반론을 그대로 인용해 부정한다. 짧은 부정문이 그래서 힘이 있다.
- 예문: Repeats aren't padding — your symptom is intermittent, and one run per combo cannot see stability at all.
- 유사어: the extra runs earn their keep (관용적), redundancy here is load-bearing (비유)
- 반의어: that's just busywork

## "inside run-to-run noise"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator 벤치 판정선 설명
- 맥락: 두 수치의 차이가 유의미하지 않다고 말할 때. 측정 결과를 과신하지 말라고 제동을 거는 자리.
- 한국어: 실행 간 편차 범위 안에 있는(= 유의미하지 않은)
- 설명: `inside`가 "범위 안"을 공간적으로 표현한다. `within the noise`도 같은 뜻이며, 통계 용어 없이 유의성 부족을 말하는 가장 흔한 방법.
- 예문: If the margin is inside run-to-run noise, treat it as no evidence rather than proof.
- 유사어: within the margin of error (더 격식), not outside the noise floor (측정공학)
- 반의어: a gap well outside the noise

## "get swept into (someone else's commit)"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator 동시 세션 커밋 충돌 보고
- 맥락: 내 변경이 남의 커밋에 딸려 들어갔다고 알릴 때. 병렬 작업 상황의 히스토리 설명.
- 한국어: (내 수정이) 남의 커밋에 휩쓸려 들어가다
- 설명: sweep 이 "빗자루로 쓸어 담다"라서 의도치 않게 함께 담긴 뉘앙스가 산다. 비난 없이 사실만 전달하기에 좋다.
- 예문: My edits got swept into their teardown-hardening commit, so the code is in HEAD under someone else's message.
- 유사어: got bundled in with (평이), rode along on their commit (구어)
- 반의어: landed in its own commit

## "eyeball (a number)"
- 레지스터: casual, technical
- 출처: transcript:auto_recipe_creator 오버레이 이미지 안내
- 맥락: 정밀 검증 말고 눈으로 슥 확인하라고 할 때. 동료에게 하는 구어.
- 한국어: 눈대중으로 확인하다
- 설명: 명사 eyeball 이 동사로 쓰인 캐주얼 용법. 격식 문서에서는 `visually inspect`로 바꾼다.
- 예문: The overlays show the click point and the OCR strip, so you can eyeball any number that looks wrong.
- 유사어: sanity-check by eye (중간 격식), visually inspect (격식)
- 반의어: verify programmatically

## "close it by structure"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-06-loop-failure-path-hardening.md
- 맥락: 규율·주석이 아니라 구조로 결함을 막았다고 주장할 때. 커밋 메시지와 설계 문서의 어조.
- 한국어: (관행이 아니라) 구조로 막다
- 설명: `by structure`가 "코드 형태 자체가 강제한다"를 뜻해, `by convention`(관행에 기댐)의 반대편에 선다. 이 대비가 문장의 전부다.
- 예문: Three cycles now share one teardown contract, which closes by structure the drift that copied `finally` blocks used to allow.
- 유사어: make it structurally impossible (강조), enforce it in code rather than in comments (풀어쓴 형태)
- 반의어: rely on convention
