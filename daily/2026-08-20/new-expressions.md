# 2026-08-20 — 새 표현

## "a documented breach"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-19-rcs-recovery-review.md
- 맥락: 코드 리뷰에서 "취향 차이가 아니라 우리가 문서로 정해 둔 규칙을 어긴 것"이라고 등급을 매길 때(격식·문어).
- 한국어: 문서화된 규칙 위반
- 설명: breach 는 violation 보다 무겁고 계약·규범을 어긴 느낌을 준다. 앞에 documented 를 붙이면 "내 주관이 아니라 저기 적혀 있다"는 근거까지 한 단어로 실린다. 리뷰어가 지적을 HARD 등급으로 올릴 때 쓰는 상투구.
- 예문: I'm filing this as a documented breach rather than a preference: AGENTS.md says docs must change with safety behavior.
- 유사어: a violation of the stated convention (더 평이함), a rule we wrote down and then broke (회화적·자조적)
- 반의어: a judgement call (규칙이 없어 판단에 맡기는 사안)

## "adds false confidence"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-19-lab-cloud-hide-review.md
- 맥락: 통과는 하지만 아무것도 증명하지 못하는 테스트·검증을 지적할 때(코드 리뷰·문어).
- 한국어: 헛된 안심을 준다
- 설명: "쓸모없다"가 아니라 "없느니만 못하다"를 담는다. 있으면 사람이 검증됐다고 믿어 버리기 때문에 해가 된다는 뜻이라, 삭제를 권하는 근거로 강하다.
- 예문: `assert value in (True, False)` passes for any boolean, so the line adds false confidence rather than coverage.
- 유사어: gives a false sense of safety (더 일상적), is vacuous (수학·논리 냄새, 더 차가움)
- 반의어: actually pins the behavior

## "harmless but unrequested"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-19-rcs-recovery-review.md
- 맥락: 스펙에 없던 기능이 들어왔지만 되돌릴 것까지는 없다고 판정할 때(리뷰 결론·문어).
- 한국어: 해롭진 않지만 요청한 적은 없다
- 설명: 두 형용사를 but 으로 묶어 판정을 한 줄로 끝낸다. 앞말이 지적의 날을 미리 깎아 두므로 상대가 방어에 들어가지 않는다.
- 예문: The new window-timeout knob is harmless but unrequested, so I'll note it rather than ask for a revert.
- 유사어: benign scope creep (범위 이탈이라는 이름을 명시), nice to have, but not in the spec (회화적)
- 반의어: squarely in scope

## "the doc of record contradicts the code"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-19-lab-cloud-hide-review.md
- 맥락: 문서와 구현이 어긋났을 때, 어느 쪽이 권위 있는 기준인지까지 함께 밝히며 지적할 때(문어·격식).
- 한국어: 공식 기준 문서가 코드와 어긋난다
- 설명: of record 는 "여러 사본 중 이것이 정본"이라는 법률·행정 어감이다. 그냥 the docs are out of date 라고 하면 누구 책임인지 흐려지지만, 이렇게 쓰면 "이 문서를 믿고 일하는 사람이 속는다"까지 들어간다.
- 예문: The route's docstring justifies itself well, but the doc of record contradicts the code, and readers trust the doc.
- 유사어: the authoritative doc now misstates the feature (더 길고 명시적), the docs are out of date (평이·중립)
- 반의어: docs and code agree

## "at worst"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-19-lab-cloud-hide-review.md
- 맥락: 남아 있는 위험의 상한을 스스로 먼저 밝혀 트레이드오프를 정당화할 때(설계 근거·구어 모두).
- 한국어: 최악의 경우라야
- 설명: 문장 중간에 끼워 "이보다 나빠질 수는 없다"는 경계를 긋는다. 결함을 숨기지 않으면서 동시에 크기를 재는 말이라, 리뷰에서 방어할 때 신뢰를 산다.
- 예문: It defaults to false while the fetch is pending, which at worst shows a BETA row for a moment to a production user.
- 유사어: in the worst case (더 격식·중립), the downside is capped at (더 분석적)
- 반의어: at best

## "the safer of the two defaults"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-19-lab-cloud-hide-review.md
- 맥락: 어느 쪽으로 두어도 실패가 가능할 때, 실패의 방향을 골랐다고 설명할 때(설계 문서·문어).
- 한국어: 둘 중 덜 위험한 기본값
- 설명: 비교급 + of the two 는 "안전한 선택지가 아예 없다"를 전제로 깔기 때문에, 완벽하지 않은 결정을 정직하게 옹호한다. safe 라고 단정했다면 반례 하나에 무너진다.
- 예문: Defaulting to false is not safe, it is the safer of the two defaults, and I picked which way to fail.
- 유사어: the lesser evil (더 구어·감정적), the cheaper failure direction (더 공학적)
- 반의어: a strictly correct default

## "through a side door"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt (transcript 인용 맥락과 같은 설계 근거 문단)
- 맥락: 정문에서 막은 것이 다른 경로로 되살아나는 상황을 경고할 때(설계 토론·구어에 가까운 비유).
- 한국어: 뒷문으로
- 설명: 규칙을 정면으로 어기지 않으면서 결과만 되돌려 놓는 변경을 가리킨다. 비난 대신 그림을 주기 때문에 반박보다 재설계를 부른다.
- 예문: An intro page advertising those screens would have re-opened the invitation through a side door.
- 유사어: by the back door (거의 같음, 영국 영어에서 더 흔함), around the gate (더 기술적)
- 반의어: through the front door

## "one thing to expect:"
- 레지스터: professional, conversational
- 출처: repo·transcript 공통 보고 패턴 (skewnono_v3_nuxt 활동 로그 수정 보고)
- 맥락: 수정을 보고한 뒤, 사용자가 곧 마주칠 잔여 현상을 미리 알릴 때(구두 보고·메신저).
- 한국어: 한 가지 미리 알아 두실 것은
- 설명: 사과도 변명도 아닌 예고다. 고쳤는데 왜 아직 그대로냐는 질문을 앞질러 막는 자리에 쓴다. 뒤에는 보통 기간이나 조건이 따라온다.
- 예문: One thing to expect: the fix only corrects new events, so the old label keeps showing until it drains out.
- 유사어: a heads-up on what you'll still see (더 캐주얼), please note that (사무적·딱딱함)
- 반의어: nothing further to watch for

## "a second, quieter failure"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt (활동 로그 다중 FAB 진단 보고)
- 맥락: 눈에 띈 버그 뒤에 숨어 있던, 증상이 없어 더 위험한 버그를 드러낼 때(진단 보고·문어).
- 한국어: 조용히 진행되던 두 번째 결함
- 설명: quieter 가 핵심이다. 시끄러운 버그는 신고되지만 조용한 버그는 데이터를 조용히 갉아먹는다는 대비를 형용사 하나로 만든다. 뒤에 "그래서 이쪽이 더 비쌌다"가 이어지기 좋다.
- 예문: There was a second, quieter failure in the same regex: real page opens were dropped, not just mislabeled.
- 유사어: a silent failure mode (더 표준적인 용어), the bug behind the bug (구어적)
- 반의어: a loud failure

## "fall through to (the fallback)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt (활동 로그 분류기 진단), docs/opencode 리뷰 문서
- 맥락: 조건 분기가 하나도 맞지 않아 마지막 기본 경로로 흘러가는 동작을 설명할 때(코드 설명·문어·구어 공통).
- 한국어: 어느 규칙에도 안 걸려 기본 경로로 떨어지다
- 설명: switch 문의 fall-through 에서 온 말이지만 라우팅·분류기 설명에 그대로 쓴다. "매칭 실패"보다 낫다 — 실패가 아니라 조용히 다른 값이 나왔다는 사실을 담기 때문이다.
- 예문: The comma-joined segment matched no page rule, so the path fell through to the tool-slug fallback.
- 유사어: land in the catch-all (더 구어), degrade to the default (더 격식)
- 반의어: match a specific rule

## "make the failure loud"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-19-rcs-recovery-review.md
- 맥락: 테스트나 검증을 고쳐 "틀리면 바로 티가 나게" 만들자고 제안할 때(리뷰 코멘트).
- 한국어: 깨질 때 요란하게 깨지게 만들다
- 설명: 고장을 없애자는 말이 아니라 고장을 보이게 하자는 말이다. 이 구분을 아는 리뷰어가 쓴다. 반대편에 fail silently 가 있어 대비가 선명하다.
- 예문: Asserting the step name instead of the index would make the failure loud.
- 유사어: fail fast and visibly (더 관용적인 원칙 표현), surface the breakage (더 부드러움)
- 반의어: fail silently

## "stay in agreement"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt (프론트·백엔드 계약 픽스처 설명)
- 맥락: 양쪽에서 따로 구현된 두 코드가 앞으로도 어긋나지 않게 묶어 두었다고 말할 때(문어).
- 한국어: 두 쪽이 계속 일치하도록 묶어 두다
- 설명: match 는 지금 같다는 뜻이고 stay in agreement 는 앞으로도 같으리라는 장치가 있다는 뜻이다. 공유 픽스처·계약 테스트를 설명하는 자리에 딱 맞는다.
- 예문: Three multi-FAB rows went into the shared fixture so the two halves stay in agreement.
- 유사어: keep the two sides honest (구어적·재치), stay in lockstep (더 강한 결합을 함의)
- 반의어: drift apart

## "drain out on its own"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt (활동 로그 30일 윈도 설명)
- 맥락: 이미 쌓인 잘못된 데이터가 시간이 지나면 조회 창 밖으로 밀려나 저절로 사라진다고 말할 때(구두 설명).
- 한국어: 손대지 않아도 시간이 지나면 빠져나간다
- 설명: 백필을 하지 않기로 한 결정을 설명하는 말이다. on its own 이 "우리가 아무것도 안 한다"는 부분을 명시해서, 방치가 아니라 선택임을 드러낸다.
- 예문: Rows already written keep the old label, so it will show in the 30-day window until it drains out on its own.
- 유사어: age out of the window (더 정확·기술적), wash out over time (더 구어)
- 반의어: need a backfill

## "pin (a case) in the unit tests"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt (계약 픽스처 대신 단위 테스트로 고정한 판단)
- 맥락: 공유 계약에 넣기는 어려운 예외 사례를 각 쪽 테스트에 못박아 둘 때(리뷰·커밋 메시지).
- 한국어: 그 사례를 테스트로 못박아 두다
- 설명: pin 은 "지금 동작을 고정해 앞으로 바뀌면 실패하게 한다"는 뜻으로 쓴다. cover 보다 의도가 좁고 강하다 — 커버리지가 아니라 회귀 방지가 목적이다.
- 예문: I kept the allowlist intact and pinned the multi-FAB case in each side's unit tests instead.
- 유사어: lock in with a regression test (더 길지만 오해가 없음), nail down (구어)
- 반의어: leave it unasserted
