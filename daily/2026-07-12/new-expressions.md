# 2026-07-12 — 새 표현

오늘 배치: auto_recipe_creator — recording_filter 설계 대화(브레인스토밍→스펙→플랜)와
consensus 파이프라인 구현·리뷰 서브에이전트 transcript 16건. 설계 대화의 구어 표현과
코드 리뷰의 평가 어휘가 풍부한 날 — 13개를 골랐습니다.

## "park (a plan/task)"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 686f8e5b… ("For now it's parked exactly where you asked.")
- 맥락: 작업·아이디어를 버리는 게 아니라 잠시 보류해 뒀다고 말할 때(회의·채팅, 구어)
- 한국어: (하던 일·계획을) 잠시 세워 두다, 보류하다
- 설명: 차를 주차하듯 일을 안전한 자리에 세워 두는 비유. shelve보다 가볍고 "곧 다시 꺼낸다"는 뉘앙스가 강합니다. 회의에서 옆길 주제를 미룰 때의 "Let's park that for now"도 같은 용법.
- 예문: For now the plan is parked exactly where you asked — say the word when you want to execute it.
- 유사어: shelve (더 장기 보류·살짝 격식), put (something) on hold (중립), table (미국 회의어로 '보류' — 영국에선 정반대로 '안건에 올리다'이니 주의)
- 반의어: pick it back up (다시 집어 들다)

## "reach for (a tool)"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 686f8e5b… ("But before you reach for it, you should know that workflow_3 already filters during capture")
- 맥락: 상대가 어떤 도구·해결책을 쓰려 할 때 "그걸 꺼내 들기 전에"라고 한 박자 말리는 조언(리뷰·상담, 구어)
- 한국어: (도구·해결책에) 손을 뻗다, 꺼내 들다
- 설명: 물리적으로 손을 뻗는 그림이 그대로 은유가 된 표현. "before you reach for X"는 "X부터 쓰기 전에 이것부터 확인하라"는 조언의 정형구입니다.
- 예문: Before you reach for the post-hoc filter, check whether the recorder already drops duplicate frames.
- 유사어: turn to (기대다·의지하다), grab (더 캐주얼), resort to (격식 — 마지못해 최후 수단으로)
- 반의어: hold off on (쓰기를 미루다)

## "worth a look"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator 686f8e5b… ("A few spots worth a look:")
- 맥락: 상대에게 검토 포인트를 가볍게 추천할 때(리뷰 요청·핸드오프, 구어~중간 격식)
- 한국어: 한 번 볼 가치가 있는
- 설명: worth + 명사의 최소 형태. "A few spots worth a look"처럼 명사 뒤에 붙여 관계절(that are worth a look)을 통째로 줄이는 것이 요령입니다.
- 예문: The spec is committed — a few spots are worth a look before you approve it.
- 유사어: worth checking out (구어), worth double-checking (재확인 뉘앙스), merits attention (격식)
- 반의어: safe to skip (건너뛰어도 되는)

## "say so"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator 686f8e5b… ("If you'd rather keep the workflow_2 files as thin wrappers, say so.")
- 맥락: "생각이 다르면 그렇게 말해 달라"고 의견 표명을 청할 때(협업 채팅, 구어)
- 한국어: 그렇게 말하다, (다르면) 말씀해 주세요
- 설명: so가 앞 문장 전체를 받는 대용어. "If you disagree, say so."처럼 조건문과 짝을 이뤄 두 단어로 끝내는 간결함이 묘미입니다.
- 예문: If you'd rather keep the old files as thin wrappers, just say so.
- 유사어: let me know (더 부드러움), speak up (침묵을 깨고 말하다), flag it (업무 어투)

## "fold in (now rather than later)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator 686f8e5b… ("that's a small change to fold in now rather than later")
- 맥락: 진행 중인 작업 범위에 작은 변경을 함께 섞어 넣자고 제안할 때(계획 논의, 문어·구어)
- 한국어: (진행 중인 작업에) 함께 접어 넣다, 묶어서 처리하다
- 설명: 요리에서 반죽에 재료를 '접어 넣듯' 살살 섞는 동작이 어원. 별도 작업으로 떼지 않고 지금 배치에 자연스럽게 포함시킨다는 그림이며, "now rather than later"와 자주 짝을 이룹니다.
- 예문: If you want the client switched too, that's a small change to fold in now rather than later.
- 유사어: roll into (묶어 넣다), incorporate (격식), bundle with (같이 묶다)
- 반의어: split out (따로 떼어내다) / defer (뒤로 미루다)

## "watertight"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator subagents/agent-a73d1793… (Task 6 동시성 리뷰: "The code is safe, just not watertight under a very specific race.")
- 맥락: 논증·설계·코드에 빈틈이 전혀 없음(또는 있음)을 평가할 때(리뷰·보고, 문어)
- 한국어: 물샐틈없는, 빈틈없는
- 설명: 배에 물이 새지 않는다는 뜻에서 온 형용사. "safe, just not watertight"처럼 부분 부정과 결합하면 "안전하긴 한데 완벽하진 않다"는 정밀한 심각도 평가가 됩니다.
- 예문: The locking is safe in practice, just not watertight under a very specific race.
- 유사어: airtight (논증·알리바이에 더 흔함), bulletproof (구어), ironclad (계약·보증에 격식)
- 반의어: leaky (새는), full of holes (허점투성이)

## "out from under"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator subagents/agent-a73d1793… ("the second gather's cleanup can delete `.events_new` out from under the first gather's rename")
- 맥락: 누군가/무언가가 한창 쓰고 있는 것을 그 밑에서 빼내 버리는 상황(동시성 버그 설명, 기술 구어)
- 한국어: (쓰고 있는 것을) 발밑에서 빼내 버리다
- 설명: 관용구 "pull the rug out from under someone"(딛고 선 양탄자를 확 빼다)에서 온 그림. 동시성 리뷰에서 "다른 스레드가 사용 중인 파일·자원을 지워버린다"를 한 구로 생생하게 전달합니다.
- 예문: The second cleanup can delete the staging directory out from under the first thread's rename.
- 유사어: behind its back (등 뒤에서 — 의인화), mid-operation (작업 도중에 — 중립 서술)

## "a maintenance liability"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator subagents/agent-a76967829… (Task 5 리뷰: "This is not a bug today but is a maintenance liability")
- 맥락: 지금은 동작하지만 앞으로 관리 부담이 될 코드를 지적할 때(코드 리뷰, 격식)
- 한국어: 관리상의 부채, 갖고 있으면 손해가 되는 짐
- 설명: liability는 자산(asset)의 반대 — 소유 자체가 부담이 되는 것. "not a bug today but a maintenance liability"는 결함의 심각도를 '버그'와 '빚'으로 정확히 구분해 매기는 리뷰 정형구입니다.
- 예문: The duplicated loop is not a bug today, but it is a maintenance liability.
- 유사어: technical debt (더 넓은 관용어), a foot-gun (구어 — 제 발등 찍는 도구), a time bomb (과장 구어)
- 반의어: an asset (자산)

## "design debt"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator subagents/agent-a73d1793… ("This is a design debt rather than a bug, but worth noting")
- 맥락: 버그는 아니지만 설계 차원에서 미뤄 둔 빚임을 구분해 말할 때(리뷰·설계 논의, 문어)
- 한국어: 설계 부채
- 설명: technical debt의 하위 개념 — 구현 실수가 아니라 설계 결정 차원에서 진 빚. "X rather than a bug"의 프레임으로 심각도 범주를 바로잡는 데 쓰입니다.
- 예문: Reading settings from the environment at call time is design debt rather than a bug, but worth noting.
- 유사어: technical debt (상위어), a known limitation (알려진 한계)
- 반의어: a deliberate design choice (의도된 설계 결정)

## "divergence-prone"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator subagents/agent-a76967829… ("the loop body itself is duplicated and divergence-prone")
- 맥락: 복붙된 코드가 앞으로 서로 어긋나기 쉽다고 경고할 때(리뷰, 기술 문어)
- 한국어: (복제본끼리) 어긋나기 쉬운
- 설명: 접미사 -prone(~하기 쉬운)은 명사에 붙여 즉석 형용사를 만드는 생산적 패턴입니다: error-prone, crash-prone, injury-prone. "duplicated and divergence-prone"은 "중복이라 갈라지기 쉽다"를 두 단어로 압축합니다.
- 예문: The two helpers share an identical loop body, which makes them divergence-prone.
- 유사어: liable to drift (어긋나기 쉬운), error-prone (같은 -prone 패턴), fragile (더 일반적)
- 반의어: robust (튼튼한) / -proof 계열 (crash-proof 등)

## "post-hoc"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator 686f8e5b… ("Standalone post-hoc filter — poc/workflow_2/filter_frames_by_change.py")
- 맥락: 일이 끝난 뒤 사후에 하는 처리·분석을 가리킬 때(기술 문어, 라틴어 차용)
- 한국어: 사후의, 일이 끝난 뒤에 하는
- 설명: 라틴어 "이 이후에". 통계에서는 post-hoc analysis(사후 분석), 여기서는 녹화가 끝난 뒤 돌리는 필터. 실시간 처리(inline / at capture time)와 짝지어 대비하면 뜻이 선명해집니다.
- 예문: The recorder filters inline at capture time, so a post-hoc pass over the saved frames may be redundant.
- 유사어: after-the-fact (일상어), retrospective (격식), offline (배치 처리 뉘앙스)
- 반의어: inline / at capture time (실시간의), upfront (선제적인)

## "in the first place"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator 686f8e5b… ("the 'unnecessary' idle/duplicate frames are largely never written to disk in the first place")
- 맥락: "애초에 그 문제가 생기지도 않는다"고 전제 자체를 무를 때(설명·반박, 구어)
- 한국어: 애초에, 처음부터
- 설명: 부정문과 결합하면 "발생 후 처리"가 아니라 "발생 자체가 없음"을 강조합니다. 의문문에서는 "Why did you do it in the first place?"(애초에 왜 했어?)의 뉘앙스.
- 예문: The idle frames are never written to disk in the first place, so there's nothing to clean up afterward.
- 유사어: to begin with (문두·문미 모두 가능), at all (부정 강조)
- 반의어: after the fact (사후에)

## "are you fine (doing X)?"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator 686f8e5b… ("or are you fine running the workflow_2 bench tool manually on the saved folders?")
- 맥락: 상대가 현 상태를 받아들일 수 있는지 가볍게 확인할 때(옵션 제시 질문, 구어)
- 한국어: ~하는 걸로 괜찮으세요?
- 설명: be fine + -ing는 "~하는 것으로 만족하는가"를 묻는 가장 가벼운 형태. "Do you want A, or are you fine (doing) B?"처럼 선택지 끝에 붙이면 강요 없이 결정을 넘길 수 있습니다.
- 예문: Do you want it wired into the loop, or are you fine running the bench tool manually?
- 유사어: are you OK with -ing (동급 구어), does it work for you if … (일정·조건 확인), would you rather … (선호 묻기)
