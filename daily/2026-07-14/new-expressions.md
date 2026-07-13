# 2026-07-14 — 새 표현

오늘 배치: skewnono_v3_nuxt 하드웨어 MDC 시계열/BM·PM 오버레이 구현 플랜(영어 설계 문서),
auto_recipe_creator 의 subagent-driven TDD 세션(구현·리뷰 서브에이전트 17건).
SDD 리뷰 어휘 다수는 이전에 이미 수집되어(hit the same wall, de-risk, worst-first 등),
설계 문서와 운영 지침에서 신규 15개를 골랐습니다.

## "stay confined to (the provider layer)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-13-hardware-mdc-timeseries-and-bmpm-overlay.md
- 맥락: 변경·영향 범위가 특정 계층 밖으로 번지지 않음을 보증할 때(설계 문서·리뷰, 격식 문어)
- 한국어: ~안에 국한되어 머무르다, 밖으로 번지지 않다
- 설명: confine(가두다)의 수동 그림. "stays confined to X"는 "X 층만 바꾸면 되고 나머지는 안전하다"는 설계 보증의 정석 문구입니다. blast radius 를 좁혔다는 주장과 짝을 이룹니다.
- 예문: Because the response contract is frozen, the office provider swap stays confined to the provider layer.
- 유사어: be limited to (중립), be contained within (격식), not leak beyond (구어·비유)
- 반의어: spill over into / leak into (밖으로 번지다)

## "land inside (the chart range)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt 같은 plan ("so markers land inside chart ranges"); transcript:auto_recipe_creator agent-a60f7… ("A real recipe lands a match")
- 맥락: 값·마커·결과가 최종적으로 어디에 '떨어지는지' 말할 때(차트 범위·조인 결과·커밋 반영, 문어·구어)
- 한국어: (결과가) ~안에 떨어지다, 안착하다
- 설명: 비행기 착륙의 그림 — 계산·이동의 끝점이 어디냐를 생생하게 전합니다. "markers land inside chart ranges"(마커가 범위 안에 온다), "lands a match"(매치에 안착한다), 변경이 반영됐다는 "the change landed"까지 개발 어휘 전반에서 씁니다.
- 예문: After re-anchoring the mock, every BM/PM marker lands inside the visible chart range.
- 유사어: fall within (격식), end up in (구어), wind up in (더 구어)
- 반의어: fall outside (the range) (범위 밖으로 벗어나다)

## "hang off (a fixed anchor)"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt 같은 plan Task 6 ("BM/PM dates hang off a fixed `NOW`")
- 맥락: 값들이 기준점 하나에 '매달려' 파생됨을 말할 때(코드 구조 설명, 구어에 가까운 문어)
- 한국어: ~에 매달려 있다, ~를 기준으로 파생되다
- 설명: 옷걸이에 걸린 그림 — 모든 날짜가 고정 앵커 하나에서 상대적으로 계산된다는 뜻입니다. 구조물이 어디에 붙어 있는지 말하는 "X hangs off Y"는 API 설계에서도 흔합니다("all endpoints hang off /api/v1").
- 예문: Every mock date hangs off a fixed anchor, so moving the anchor shifts the whole timeline at once.
- 유사어: be anchored to (중립), be keyed off (of) (기술), derive from (격식)

## "(ship it) behind a toggle, default ON"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt 같은 plan ("behind one page-level toggle (default ON)"); transcript:auto_recipe_creator 8909999c… ("code parked behind TBANK_HEATMAP=0", "ships notify-only behind the double gate")
- 맥락: 기능을 스위치 뒤에 두고 배포한다고 말할 때(기능 플래그 문화, 문어·구어)
- 한국어: 토글(스위치) 뒤에 넣어 내보내다 — 기본값 명시와 함께
- 설명: behind 전치사 하나로 "스위치로 켜고 끌 수 있게 감쌌다"는 배포 전략이 전달됩니다. behind a feature flag / gated behind X / parked behind X=0 모두 같은 계열이고, "(default ON/OFF)"를 괄호로 못 박는 것까지가 관용입니다.
- 예문: We shipped the overlay behind a page-level toggle, default ON, so anyone can turn it off per session.
- 유사어: behind a feature flag (표준), gated behind X (문어), opt-in / opt-out (기본값 관점)
- 반의어: hard-wired on (끌 수 없게 박아 넣은)

## "a gray zone (of the spec)"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator agent-a7026… ("this is in a gray zone of the spec rather than a clear violation")
- 맥락: 규정 위반도 준수도 아닌 애매 지대를 판정할 때(리뷰·규정 논의)
- 한국어: 회색 지대, 애매한 경계 영역
- 설명: 흑백 사이의 회색 — 스펙이 명시적으로 다루지 않아 위반이라 부르기도, 준수라 부르기도 어려운 영역입니다. "in a gray zone of X rather than a clear violation" 구조로 판정의 결을 섬세하게 만듭니다. a gray area 가 더 일반적인 형태.
- 예문: Valid JSON of the wrong shape sits in a gray zone of the spec — neither a parse failure nor a compliant payload.
- 유사어: a gray area (더 흔한 일반형), borderline (형용사적), ambiguous territory (서술형)
- 반의어: a clear violation / clear-cut (명백한 위반 / 명백한)

## "negligible (the risk is negligible)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator agent-a2d32… ("In practice the file is always machine-written by the driver, so the risk is negligible.")
- 맥락: 리스크·차이가 무시해도 될 만큼 작다고 판정할 때(리뷰·보고, 격식)
- 한국어: 무시해도 될 정도의, 미미한
- 설명: neglect(방치하다)에서 온 형용사 — "신경 쓰지 않아도 되는 크기"라는 판정어입니다. 리뷰에서 Minor 를 수용할 때의 근거 문장("the risk is negligible")으로 거의 고정적으로 쓰입니다.
- 예문: The file is always machine-written, so the risk of a malformed payload is negligible.
- 유사어: vanishingly small (수사적 강조), immaterial (재무·법 격식), trivial (좀 더 구어)
- 반의어: material / non-trivial (유의미한)

## "vacuous (a vacuous test)"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator 리뷰 지시문 다수 ("Tests assert the claimed values and aren't vacuous", "a test that asserts nothing")
- 맥락: 형식만 갖추고 실질 검증이 없는 테스트·주장을 깎아내릴 때(코드리뷰, 문어)
- 한국어: 공허한, 알맹이 없는 — 아무것도 검증하지 않는
- 설명: vacuum(진공)과 같은 뿌리로 '속이 빈'. 테스트 리뷰의 핵심 질문 "이 테스트가 vacuous 하지 않은가?"는 "구현을 지워도 통과하는(asserts nothing) 테스트 아닌가"라는 뜻입니다. 반대 판정은 non-vacuous / substantive.
- 예문: The sort test is not vacuous — it pins the exact index order instead of just checking the length.
- 유사어: toothless (구어·비유), trivially passing (기술 서술), asserts nothing (풀어쓴 형태)
- 반의어: substantive / non-vacuous (실질 검증이 있는)

## "adjudicate (carried findings)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator agent-a60f7… ("Adjudicate the 4 carried Minors explicitly (acceptable vs must-fix)")
- 맥락: 쌓인 쟁점 하나하나에 수용/기각의 공식 판정을 내릴 때(최종 리뷰·심사, 격식)
- 한국어: (쟁점을) 심판하다, 판정을 내리다
- 설명: 법정 용어를 리뷰로 가져온 동사 — 단순 의견(comment)이 아니라 accept/reject 를 '판결'하는 행위입니다. 앞 단계에서 이월된(carried) 미결 항목을 최종 처리할 때 정확히 맞는 단어입니다.
- 예문: The final reviewer adjudicated all four carried minors explicitly, marking each acceptable or must-fix.
- 유사어: rule on (판정하다, 준격식), settle (매듭짓다), triage (우선순위 분류 — 판정보다 앞 단계)
- 반의어: leave (an issue) open (미결로 남기다)

## "trace the data, don't just pattern-match"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator agent-a60f7… ("Trace the data, don't just pattern-match."); 같은 리뷰의 "verified end-to-end, not pattern-matched"
- 맥락: 표면 유사성으로 넘겨짚지 말고 실제 흐름을 따라가라고 지시할 때(리뷰·디버깅 지침)
- 한국어: 데이터를 끝까지 따라가라 — 눈에 익은 모양만 보고 판단하지 말고
- 설명: pattern-match 가 동사로 쓰이면 "본 적 있는 모양과 비슷하니 맞겠지"라는 얕은 판단을 가리키는 개발자 은어가 됩니다. trace(추적)와 대비시켜 검증의 깊이를 요구하는 명령문입니다.
- 예문: Trace one real recipe through both drivers — don't just pattern-match on the key format.
- 유사어: verify end-to-end (검증 관점), follow the data flow (중립), eyeball it (반대 방향 — '대충 훑다', 구어)
- 반의어: go by surface similarity (표면 유사성으로 판단하다)

## "bite-sized (tasks)"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 8909999c… (writing-plans 지침: "Give them the whole plan as bite-sized tasks")
- 맥락: 일·자료를 한입 크기로 잘게 쪼갰다고 말할 때(계획·교육 자료, 구어부터 문어까지)
- 한국어: 한입 크기의, 잘게 쪼갠
- 설명: 한 입에 먹을 수 있는 크기라는 음식 비유가 그대로 업무 단위로 온 형용사입니다. bite-sized tasks/chunks/lessons 처럼 부담 없이 소화 가능한 단위임을 강조합니다. 격식 문서에서는 fine-grained 가 대응어.
- 예문: The plan hands the engineer bite-sized tasks, each with its own test cycle and commit.
- 유사어: fine-grained (격식·기술), digestible (같은 소화 비유), small and self-contained (서술형)
- 반의어: monolithic (통짜의)

## "X beats Y (Turn count beats token price.)"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 8909999c… ("Turn count beats token price.")
- 맥락: 두 요인 중 무엇이 더 지배적인지 한 문장 격언으로 못 박을 때(가이드라인·의사결정 문서의 헤드라인)
- 한국어: X가 Y를 이긴다 — X가 더 결정적이다
- 설명: 관사 없는 명사구 둘을 beats 로 잇는 격언 구문 — "Done beats perfect", "Clarity beats cleverness"처럼 우선순위 규칙을 제목화하는 영어 특유의 압축입니다. 이 한 줄을 헤드라인으로 놓고 뒤에 근거를 푸는 배치까지가 용법입니다.
- 예문: Turn count beats token price — a cheap model that takes three times the turns costs more overall.
- 유사어: X trumps Y (같은 구조, 약간 더 격식), X matters more than Y (풀어쓴 중립형), X wins over Y (구어)

## "trust X over Y"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator 8909999c… ("trust the ledger and git log over your own recollection")
- 맥락: 두 정보원이 충돌할 때 어느 쪽을 우선할지 정할 때(운영 지침·디버깅 원칙)
- 한국어: Y보다 X를 믿어라
- 설명: over 하나로 비교 대상이 붙는 간결한 우선순위 구문입니다. prefer X over Y 와 같은 골격인데 동사가 trust 가 되면 "기억보다 기록"류의 신뢰 서열을 정하는 문장이 됩니다.
- 예문: After a context reset, trust the ledger and the git log over your own recollection.
- 유사어: prefer X to/over Y (선호), take X over Y (구어), X is authoritative (X가 정본이다, 격식)

## "shelve (shelved)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 8909999c… ("Phase 2 (E-frame confirmation) — shelved.")
- 맥락: 계획을 폐기하는 건 아니고 무기한 보류로 치워 둘 때(프로젝트 관리, 문어·구어)
- 한국어: (계획을) 선반에 올려두다 — 무기한 보류하다
- 설명: 책을 선반에 꽂아 두는 그림 — 버린 것(rejected)과 달리 언제든 꺼낼 수 있게 치워 둔 상태입니다. park 보다 기간이 길고 재개 기약이 약한 뉘앙스이며, 수동태 한 단어 "shelved."를 상태 라벨처럼도 씁니다.
- 예문: Phase 2 is shelved for now — nothing blocks it, but nothing justifies it yet either.
- 유사어: park (더 단기 보류), put on ice (구어), table (미국 회의 용법 — 보류)
- 반의어: revive / dust off (다시 꺼내다)

## "fix forward"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt 같은 plan Task 10 ("No code changes expected; fix-forward anything found")
- 맥락: 롤백 대신 결함을 발견 즉시 다음 커밋으로 고치며 전진하는 전략을 말할 때(배포·운영)
- 한국어: 되돌리지 않고 전진 수정하다
- 설명: roll back(이전 상태로 복귀)의 반대 전략으로 굳은 운영 용어입니다. 검증 단계에서 나오는 잔손질을 "그 자리에서 고쳐 흡수한다"는 지시로, 하이픈을 붙여 동사처럼(fix-forward) 쓰기도 합니다.
- 예문: If the browser checklist turns anything up, we fix forward in the same task instead of reverting.
- 유사어: roll forward (배포 문맥), hotfix (긴급 수정 — 명사 뉘앙스), patch it in place (서술형)
- 반의어: roll back / revert (되돌리다)

## "right-size (task right-sizing)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 8909999c… (writing-plans 지침 "Task Right-Sizing" — "A task is the smallest unit that carries its own test cycle")
- 맥락: 너무 크지도 작지도 않게 단위 크기를 맞출 때(업무 분할·클라우드 비용 최적화, 격식)
- 한국어: 딱 맞는 크기로 조정하다
- 설명: downsize/upsize 에서 파생한 비즈니스 동사 — 방향이 아니라 '적정'이 목적입니다. 클라우드 비용(right-size the instances), 작업 분할(task right-sizing) 등 크기 결정 전반에 쓰고, 동명사형이 표제어처럼 굳었습니다.
- 예문: Right-size each task so a reviewer could reject one without blocking its neighbors.
- 유사어: scope appropriately (서술형), calibrate the granularity (격식), cut to size (비유)
- 반의어: over-scope / under-scope (너무 크게 / 너무 작게 잡다)
