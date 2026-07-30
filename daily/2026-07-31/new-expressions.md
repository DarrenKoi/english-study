# 2026-07-31 — 오늘의 표현

## "right there and wrong here"

- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md
- 맥락: 같은 규칙이 A 상황에서는 옳지만 B 상황에서는 틀리다고 설계 근거를 적을 때(격식 있는 문어체)
- 한국어: 거기서는 맞고 여기서는 틀리다
- 설명: `there` 와 `here` 를 마주 세워 "규칙이 잘못된 게 아니라 적용 범위가 잘못됐다"를 한 마디로 정리한다. 남의 코드를 고칠 때 상대를 깎아내리지 않으면서 예외를 요구하는 표현이라 리뷰·설계 문서에서 쓸모가 크다.
- 예문: The adapter raises on an unknown vendor, which is right there and wrong here — this screen exists to surface the tools we have not onboarded.
- 유사어: appropriate in one place but not the other (더 밋밋한 설명조), the same rule cuts the wrong way here (구어에 가깝고 비유적)
- 반의어: correct in both cases

## "in flight"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (43fc3fea)
- 맥락: 자리를 비웠다 돌아온 사람에게 "지금 진행 중인 일"을 항목으로 보고할 때(업무 구어·짧은 상태 보고)
- 한국어: 진행 중인 (일)
- 설명: 항공 용어에서 온 표현으로 착수했지만 아직 안 끝난 상태를 가리킨다. `in progress` 보다 짧고 상태 보고 목록의 라벨로 잘 붙는다. 코드 쪽에서는 `in-flight request`(응답 대기 중인 요청)처럼 하이픈 형용사로도 자주 쓴다.
- 예문: In flight: a tool-roster view for unconnected equipment — the design is settled but nothing is implemented yet.
- 유사어: in progress (가장 중립적), under way (조금 더 격식), on my plate (내가 떠안고 있다는 뉘앙스, 구어)
- 반의어: landed, wrapped up

## "through sheer inertia"

- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt (systematic-debugging 스킬 문서)
- 맥락: 세 번째 수정도 실패한 뒤 "이 방식을 왜 아직 붙들고 있나"를 되물을 때(회고·설계 재검토)
- 한국어: 순전히 관성으로
- 설명: `inertia` 는 물리의 관성이고, `sheer` 가 붙으면 "다른 이유는 하나도 없이 그저"가 된다. 판단이 아니라 습관으로 유지돼 온 결정을 지적할 때 쓴다. 사람을 탓하지 않고 상황을 탓하는 어감이라 팀 회고에서 안전하다.
- 예문: Three failed fixes in a row is the moment to ask whether we are sticking with this pattern through sheer inertia.
- 유사어: out of habit (일상적·가벼움), because that is how it has always been done (풀어 쓴 구어), by default rather than by decision (격식)
- 반의어: by deliberate choice

## "no \"while I'm here\" improvements"

- 레지스터: technical, casual
- 출처: transcript:skewnono_v3_nuxt (systematic-debugging 스킬 문서)
- 맥락: 버그 수정 커밋에 곁다리 리팩터링을 섞지 말라고 못 박을 때(코드 리뷰·커밋 규칙)
- 한국어: "온 김에" 손보는 개선은 금지
- 설명: `while I'm here` 를 통째로 따옴표에 넣어 명사처럼 쓰는 용법이다. 개발자가 파일을 열었다가 무심코 덧붙이는 정리 작업을 한 단어로 지목한다. 인용부호가 "우리 모두 아는 그 변명"이라는 농담기를 실어 준다.
- 예문: One change at a time — address the root cause, and no "while I'm here" improvements.
- 유사어: no drive-by refactoring (같은 뜻의 개발 은어), keep the diff focused (중립적·격식), resist scope creep (관리 용어)
- 반의어: bundle the cleanup in

## "two things jump out"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (b6e687d1)
- 맥락: 자료를 훑고 나서 가장 먼저 눈에 걸린 것부터 짚고 들어갈 때(구두 보고·리뷰 서두)
- 한국어: 두 가지가 대뜸 눈에 띈다
- 설명: `jump out (at me)` 는 찾으려 애쓰지 않았는데 저절로 튀어나와 보였다는 뜻이다. 뒤에 `at me` 를 붙이면 더 개인적이고, 생략하면 객관적으로 들린다. 발견의 강도가 `I noticed` 보다 세다.
- 예문: Two things jump out that I want to flag before writing anything: the keying does not match the contract, and the parameter counts have no source at all.
- 유사어: stand out (더 중립적), catch my eye (시각적·가벼움), leap off the page (문서를 읽을 때 쓰는 강조형)
- 반의어: go unnoticed, blend in

## "reproduce the bug in miniature"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (eb7129d4)
- 맥락: 실패 테스트가 실제 장애를 작게 재현했다고 설명할 때(디버깅 보고·격식)
- 한국어: 그 버그를 축소판으로 재현하다
- 설명: `in miniature` 는 "규모만 줄인 같은 것"을 뜻하는 부사구다. 테스트가 단순한 흉내가 아니라 구조가 같은 축소 모형임을 주장할 때 정확하다. 미술·건축에서 온 말이라 문어체 색이 있다.
- 예문: The two failing tests reproduce your bug in miniature: the message names only one source even though the registry was consulted and declined.
- 유사어: a scaled-down version of the same failure (풀어 쓴 설명), a minimal repro (개발 은어, 격식 낮음)
- 반의어: an unrelated failure

## "what stands between A and B"

- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md
- 맥락: 사소해 보이는 장치가 사실 유일한 방어선임을 설득할 때(설계 근거·격식)
- 한국어: A 와 B 사이를 막고 선 유일한 것
- 설명: 물리적으로 "사이에 서 있다"는 그림을 그려, 제거하면 곧장 나쁜 결과가 온다는 인과를 압축한다. `X is the only thing that prevents Y` 보다 짧고 강하다. 방어 로직·폴백·경고를 지킬 때 특히 잘 맞는다.
- 예문: This bucket is what stands between a new tool type and silent invisibility on the one screen meant to surface it.
- 유사어: the only safeguard against (더 사무적), all that keeps X from Y (구어에 가까움)
- 반의어: a redundant guard

## "that is the point, not an optimization"

- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md
- 맥락: 성능 튜닝으로 오해받기 쉬운 설정이 사실 기능의 핵심임을 못 박을 때(주석·설계 문서)
- 한국어: 그게 요점이지 최적화가 아니다
- 설명: `X, not Y` 대비 구문으로 오해 한 가지를 미리 차단한다. 뒷사람이 "성능 때문이니 지워도 되겠지"라며 되돌리는 일을 막는 주석의 정석이다. 무엇이 아닌지를 먼저 말해 무엇인지를 또렷하게 만든다.
- 예문: `immediate: false` is the point, not an optimization — navigating to the page must never touch the company-wide roster.
- 유사어: this is load-bearing, not decoration (비유적·구어), deliberate rather than incidental (격식)
- 반의어: a nice-to-have

## "tell a genuine new arrival from a long-abandoned entry"

- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md
- 맥락: 어떤 값이 두 경우를 구별하는 근거가 되는지 설명할 때(데이터 계약 문서·격식)
- 한국어: 진짜 신규 반입분과 오래 방치된 항목을 구별하다
- 설명: `tell A from B` 는 "A 와 B 를 구별하다"라는 고정 구문으로 `distinguish` 의 일상 버전이다. `tell` 뒤에 목적어가 길어져도 `from` 이 짝을 잡아 주므로 긴 명사구 두 개를 나란히 놓을 수 있다. `tell the difference between A and B` 로도 같은 뜻이 되지만 이쪽이 더 짧다.
- 예문: The column is imprecise for old tools and trustworthy for recent ones, which is what makes it usable for telling a genuine new arrival from a long-abandoned roster entry.
- 유사어: distinguish A from B (격식·문어), tell the difference between A and B (가장 평이함), separate the signal from the noise (비유적)
- 반의어: conflate A with B, lump them together

## "found late if ever"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (b6e687d1)
- 맥락: 조용히 잘못된 결과를 내는 버그의 위험을 한 줄로 요약할 때(코드 리뷰·격식 낮은 문어)
- 한국어: 늦게 발견되거나 아예 발견되지 않는
- 설명: `if ever` 는 "그런 일이 있기라도 하다면"이라는 조건 축약으로, 앞의 부사를 최악 쪽으로 한 번 더 민다. 예외도 안 나고 로그도 안 남는 버그를 묘사할 때 `wrong order, no exception, found late if ever` 처럼 세 조각을 나열하면 리듬이 산다.
- 예문: A first-match scan sorts the step into the wrong slot with no exception raised — wrong order, found late if ever.
- 유사어: caught late, if at all (거의 같은 뜻, 더 평이함), fails silently (원인 쪽에 초점)
- 반의어: caught immediately, fails loudly

## "get flagged rather than absorbed"

- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (b6e687d1)
- 맥락: 예상과 다른 데이터를 조용히 삼키지 말고 드러내도록 만들었다고 설명할 때(진단 도구·검증 설계)
- 한국어: 조용히 흡수되지 않고 표시되게 하다
- 설명: `absorb` 가 여기서는 "티 없이 받아들여 없던 일로 만들다"는 부정적 의미다. `flag` 와 짝지어 "드러내기 vs 삼키기"의 대비를 만든다. 검증 로직의 설계 의도를 한 문장으로 설명할 때 반복해서 쓸 수 있는 틀이다.
- 예문: Fab coverage is checked against the confirmed split, so contents contradicting the key name get flagged rather than absorbed.
- 유사어: surfaced rather than swallowed (더 구어적), raise instead of skipping silently (코드 설명조)
- 반의어: silently tolerated, papered over

## "that is the gate on X"

- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (b6e687d1)
- 맥락: 한 가지 미확인 사실이 뒤의 작업 전체를 막고 있다고 알릴 때(진행 보고·의사결정 요청)
- 한국어: 그것이 X 를 막고 있는 관문이다
- 설명: `gate` 를 명사로 써서 "이게 열려야 다음이 진행된다"는 의존 관계를 만든다. `blocker` 가 사고를 뜻한다면 `gate` 는 원래부터 통과해야 할 조건이라는 어감이라 비난기가 없다. 동사로 `X gates Y` 라고도 쓴다.
- 예문: The blob's internal structure is unverified, and it is the gate on both the parameter list and the per-count buckets.
- 유사어: a prerequisite for (사무적·격식), the blocker (사고·지연의 어감), a hard dependency (계약적)
- 반의어: a nice-to-have, orthogonal to

## "Ready when you are."

- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (43fc3fea)
- 맥락: 상대의 인사·노크에 "언제든 시작하시죠"로 짧게 답할 때(가벼운 업무 구어)
- 한국어: 준비됐습니다, 시작하실 때 말씀만 하세요
- 설명: `I am ready whenever you are ready` 를 두 번 줄인 관용구다. 주도권을 상대에게 넘기면서도 이쪽은 이미 대기 상태라는 걸 알린다. 회의 시작, 화면 공유, 페어 프로그래밍 시작 등 순간마다 그대로 쓸 수 있다.
- 예문: Ready when you are — say the word and I will pull up the failing test.
- 유사어: whenever you're ready (거의 같음, 살짝 더 부드러움), I'm all set (내 준비 상태에만 초점), at your convenience (격식 있는 문어)
- 반의어: give me a minute

## "state something untrue"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (a068254c)
- 맥락: 편의를 위한 값 단순화가 사실과 다른 주장을 하게 된다고 반대할 때(설계 근거·격식)
- 한국어: 사실이 아닌 것을 말하게 된다
- 설명: `lie` 는 의도를 함의하지만 `state something untrue` 는 화자를 탓하지 않고 결과만 지적한다. 빈 값과 없음을 같은 값으로 뭉개는 설계처럼, 코드가 사용자에게 잘못된 사실을 "말하게" 되는 상황에 정확히 맞는다.
- 예문: Collapsing an empty group to `null` would state something untrue: the file was read, and the group simply is not in it.
- 유사어: claim more than the data supports (연구·분석 문맥), misrepresent the state (사무적)
- 반의어: report exactly what happened

## "weakly grounded — revisit once it has real use"

- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-30-pending-tools.md
- 맥락: 근거가 얕은 임계값을 남기면서 그 사실을 코드에 정직하게 적어 둘 때(주석·설계 문서)
- 한국어: 근거가 약하다 — 실제로 쓰이기 시작하면 다시 보자
- 설명: 확신 수준을 스스로 낮춰 적는 표현이라 뒷사람이 그 숫자를 사실로 오해하지 않는다. `revisit once ~` 는 재검토 조건을 시점이 아니라 사건으로 걸어 두는 방식이고, 기한 없는 TODO 보다 훨씬 잘 지켜진다.
- 예문: Weakly grounded — revisit once the screen has real use; rows past the threshold are de-emphasized, never hidden.
- 유사어: a rough first cut (더 가벼움), provisional until we have data (격식), an educated guess (근거의 성격에 초점)
- 반의어: empirically established

## "rushing guarantees rework"

- 레지스터: professional, conversational
- 출처: transcript:skewnono_v3_nuxt (systematic-debugging 스킬 문서)
- 맥락: 급하니 절차를 건너뛰자는 압박에 답할 때(팀 대화·짧은 원칙 선언)
- 한국어: 서두르면 반드시 두 번 일하게 된다
- 설명: 주어를 동명사로 잡고 `guarantees` 를 써서 가능성이 아니라 필연으로 말한다. `may lead to` 였다면 협상 여지가 생기지만 `guarantees` 는 문을 닫는다. 짧은 격언형이라 회의에서 그대로 인용하기 좋다.
- 예문: We are not skipping the investigation because the release is tomorrow — rushing guarantees rework.
- 유사어: more haste, less speed (속담, 문어), we will pay for it later (구어·완곡)
- 반의어: measure twice, cut once
