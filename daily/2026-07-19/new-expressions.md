# 2026-07-19 — 새 표현

## "a second-opinion review"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-skewvoir-wafer-map-enhancement.md
- 맥락: 다른 리뷰어(또는 다른 도구)에게 한 번 더 검토를 받았다고 말할 때(문어·격식)
- 한국어: 2차 소견 검토, 별도 검토자의 재검토
- 설명: 의사에게 받는 second opinion(2차 소견)을 코드 리뷰에 옮긴 말. "제3자의 눈으로 다시 봤다"는 뉘앙스가 한 단어에 담긴다.
- 예문: A second-opinion review surfaced 8 issues; verified against source, these were reconciled as follows.
- 유사어: an independent review (더 중립적·격식), a fresh pair of eyes (회화체, "새로운 시각")
- 반의어: a self-review (자가 검토)

## "override X where they conflict"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-skewvoir-wafer-map-enhancement.md
- 맥락: 문서 두 버전이 충돌할 때 우선순위를 선언하는 문장(스펙·계약서 문체)
- 한국어: 충돌하는 부분에서는 X를 무효화한다/우선한다
- 설명: `where`가 "~하는 곳에서는/~하는 한"이라는 조건 관계절로 쓰였다. 전체를 갈아엎는 게 아니라 충돌 지점만 새 버전이 이긴다는 정밀한 한정.
- 예문: The revisions below override the original tasks where they conflict.
- 유사어: take precedence over (더 격식), supersede (전면 대체 뉘앙스가 강함)
- 반의어: defer to (~에 양보하다)

## "slip through"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-skewvoir-wafer-map-enhancement.md
- 맥락: 잘못된 값·버그가 검증망을 "빠져나가" 통과해버리는 상황(구어에도 문어에도 흔함)
- 한국어: (검사를) 빠져나가다, 새어 들어오다
- 설명: slip(미끄러지다) + through(뚫고). 방어 코드 이야기에서 "이제 이런 값은 못 빠져나간다"를 부정문으로 자주 쓴다.
- 예문: `resolveColorRange` guards with `Number.isFinite`, so an empty input no longer slips through.
- 유사어: sneak past (더 의인화된 구어), get through the cracks / fall through the cracks (누락되다)
- 반의어: get caught (걸리다)

## "behavior-preserving"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-skewvoir-wafer-map-enhancement.md
- 맥락: 리팩터링·이름 변경이 동작을 바꾸지 않음을 못 박을 때(커밋 메시지·플랜 문서)
- 한국어: 동작을 보존하는 (변경)
- 설명: 명사 앞에 붙는 복합 형용사(hyphenated compound). "-preserving"은 order-preserving, type-preserving처럼 생산적으로 조합된다.
- 예문: This is a behavior-preserving rename of the two view modes — no new features.
- 유사어: no-op refactor (구어·속어에 가까움), semantically identical (더 격식)
- 반의어: behavior-changing (동작이 달라지는)

## "answer a low-value question"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-activity-fab-page-usage-design.md
- 맥락: 기존 기능을 없애자고 설득할 때, 기능이 아니라 "그 기능이 답하는 질문"의 가치를 깎는 화법(문어)
- 한국어: 별 가치 없는 질문에 답하다
- 설명: 대시보드·차트를 "질문에 대한 답"으로 프레이밍하는 관용적 사고법. 이어지는 "tells us little about …"(~에 대해 알려주는 게 거의 없다)와 짝으로 쓰면 제거 근거가 완성된다.
- 예문: This card answers a low-value question — model popularity mirrors fleet size and tells us little about how the application is actually used.
- 유사어: adds little insight (완곡), the wrong question to ask (더 단정적)
- 반의어: answer the more valuable question

## "reality overtook the plan"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (플랜 회고 리뷰)
- 맥락: 계획이 낡기 전에 구현이 먼저 앞질러 가버린 상황을 회고할 때
- 한국어: 현실이 계획을 앞질렀다
- 설명: overtake는 "추월하다". 사건(events), 현실(reality)이 주어가 되어 문서·계획을 추월했다고 하면 "계획이 틀렸다"보다 부드럽고 정확하다.
- 예문: Here's where reality overtook the plan: the plain-bubble UI was replaced wholesale before the plan was even reviewed.
- 유사어: events outpaced the plan, the plan fell behind reality (시점 반전)
- 반의어: the plan held up (계획이 그대로 유효했다)

## "the plan's biggest miss"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (플랜 회고 리뷰)
- 맥락: 회고에서 가장 뼈아픈 누락 하나를 지목할 때(구어에 가깝지만 문서에도 씀)
- 한국어: 이 계획의 최대 실책/누락
- 설명: miss가 명사로 "빗나감, 놓친 것". a near miss(아슬아슬한 순간), a big miss(큰 실책)처럼 스포츠 어감이 배어 있어 비난보다 담백하다.
- 예문: Retry duplication was the plan's biggest miss — the test asserted one failure but never exercised the retry path.
- 유사어: the biggest oversight (더 격식), the biggest blind spot (구조적 맹점 뉘앙스)
- 반의어: the plan's biggest win

## "drop in without friction"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt (플랜 회고 리뷰)
- 맥락: 기존 구조에 새 부품이 개조 없이 매끄럽게 들어맞았다고 평가할 때
- 한국어: 마찰 없이 그대로 끼워지다
- 설명: drop in은 "툭 넣으면 그대로 작동"(cf. a drop-in replacement), without friction은 "저항·개조 비용 없이". 통합 비용이 0이었다는 회고 상찬.
- 예문: The afm-style provider seam dropped in without friction.
- 유사어: slotted right in (구어), integrated seamlessly (격식)
- 반의어: needed rework to fit (맞추려고 재작업이 필요했다)

## "stop short of (doing)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 어떤 행동 직전까지만 하고 그 선은 넘지 않았음을 알릴 때(보고·문어)
- 한국어: ~하기 직전에 멈추다, ~까지는 하지 않다
- 설명: short of가 "~에 못 미쳐"라는 뜻이라, 준비는 다 해놓고 마지막 한 발은 안 뗐다는 정확한 그림을 그린다. 권한 경계를 지켰다는 보고에 딱 맞는다.
- 예문: Since your note says "only commit when I ask," I've stopped short of committing.
- 유사어: hold off on (미루다, 시점 뉘앙스), refrain from (더 격식·금욕적)
- 반의어: go ahead with (그대로 진행하다)

## "one housekeeping note"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 본론이 끝난 뒤 소소한 정리 사항을 덧붙일 때(회의 진행·이메일 상투구)
- 한국어: 정리 차원의 참고 사항 하나
- 설명: housekeeping은 "집안 정리"에서 온 은유로, 회의 서두·말미의 자잘한 운영 공지를 가리킨다. 중요도가 낮음을 미리 표시해 듣는 부담을 줄인다.
- 예문: One housekeeping note: the memory that says the migration is unpushed is now stale and could mislead a future session.
- 유사어: a minor admin item (사무적), while we're at it (구어, "하는 김에")
- 반의어: (마땅한 반의어 없음 — 본론은 the main item 정도로 대비)

## "one heads-up before you ..."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (.env 스위치 작업)
- 맥락: 상대가 다음 행동을 하기 전에 미리 알려주는 주의 한 마디(구어·채팅)
- 한국어: ~하기 전에 미리 알려드릴 것 하나
- 설명: heads up!(고개 들어, 조심!)이 명사화된 것. give someone a heads-up 형태로도 쓴다. 경고보다 가볍고 친절한 어감.
- 예문: One heads-up before you restart: this now points sem_list at the office provider.
- 유사어: just so you know (더 캐주얼), for your awareness (사무적·이메일)
- 반의어: (마땅한 반의어 없음)

## "mirror it back"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 상대의 말을 자기 말로 되비추어 이해가 맞는지 확인할 때(적극적 경청 화법)
- 한국어: (이해한 내용을) 그대로 되짚어 말하다
- 설명: 거울(mirror)에 비추듯 상대의 설계·요구를 내 언어로 재진술하는 것. 합의 확인(alignment check)의 정석 표현.
- 예문: Let me mirror it back precisely so we're fully aligned before I touch anything.
- 유사어: play it back (구어), restate my understanding (격식)
- 반의어: talk past each other (서로 딴소리하다)

## "ride the same commit"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 여러 파일의 변경이 한 커밋에 실려 함께 이동한다고 말할 때
- 한국어: 같은 커밋에 실려 가다
- 설명: ride(올라타다)로 변경사항을 승객처럼 의인화했다. "they travel together"와 같은 결로, 원자적 변경(atomic change)을 생생하게 표현한다.
- 예문: When you evolve a feature, all the changes ride the same commit through GitHub.
- 유사어: travel together (같은 문서에서 함께 쓰임), land in one commit (착지 은유)
- 반의어: drift apart (제각각 어긋나다)

## "on your own terms"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 강요된 시점이 아니라 자신이 정한 방식·시점으로 처리한다고 할 때
- 한국어: 자기 조건대로, 자기 페이스대로
- 설명: terms는 "조건". 충돌 해소처럼 수동적으로 당하던 일을 능동적으로 통제한다는 뉘앙스 전환에 쓴다.
- 예문: The merge you were dreading becomes a readable diff you apply on your own terms.
- 유사어: at your own pace (속도에 초점), when it suits you (시점에 초점)
- 반의어: under duress (압박 속에서), on someone else's schedule

## "crystal clear"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 이제 완전히 이해됐다고 확인해줄 때(구어; 문어에서는 다소 캐주얼)
- 한국어: 수정처럼 명료한, 완전히 분명한
- 설명: crystal(수정)의 투명함에 빗댄 강조. "Now it's crystal clear"는 앞선 오해가 걷혔음을 함께 암시한다. make oneself crystal clear는 경고조가 될 수 있으니 주의.
- 예문: Now it's crystal clear — and it matches exactly what I sketched.
- 유사어: perfectly clear (중립), unambiguous (격식·문어)
- 반의어: murky (흐릿한), as clear as mud (반어적 구어)

## "caught mechanically, not by memory"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt (office 어댑터 마이그레이션)
- 맥락: 사람의 기억력이 아니라 자동화된 장치가 오류를 잡는다고 대비시킬 때
- 한국어: 기억이 아니라 기계적 장치로 잡힌다
- 설명: "X, not Y" 대구로 신뢰의 근거를 사람에서 시스템으로 옮기는 문형. mechanically는 "자동으로·규칙적으로"라는 공학적 어감.
- 예문: The contract test runs at the office, so drift is caught mechanically, not by memory.
- 유사어: enforced by tooling (도구가 강제), automated away (사라지게 자동화)
- 반의어: rely on discipline (사람의 규율에 기대다)
