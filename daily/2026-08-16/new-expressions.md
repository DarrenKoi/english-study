# 2026-08-16 — 새 표현

## "X says nothing about Y"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 상대가 내민 근거가 결론까지 못 미친다고 지적할 때(문서·리뷰·토론, 격식). 근거 자체는 인정하되 범위가 좁다고 자르는 방식이라 인신공격이 안 된다.
- 한국어: 그건 Y에 대해서는 아무 말도 하지 않는다 / 그 근거로는 Y를 못 덮는다.
- 설명: 주어를 사람이 아니라 *증거*로 두는 게 요령이다. "너는 틀렸다"가 아니라 "이 문장이 저기까지는 못 간다"가 되어, 반박이 사실 문제로 남는다.
- 예문: Showing that no adapter assigns the field says nothing about whether a raw payload passes it through.
- 유사어: that only shows … (더 평이한 회화체), it doesn't follow that … (논리 비약을 직접 지목, 더 강함), that's orthogonal to Y (쟁점이 아예 다른 축이라고 밀어낼 때)
- 반의어: that settles it / that closes the question

## "unfalsifiable from here"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 지금 있는 환경으로는 참·거짓을 가릴 방법이 없다고 밝힐 때(설계 토론·버그 진단, 격식).
- 한국어: 여기서는 반증할 수단이 없다.
- 설명: `un- + falsifi(y) + -able` 로 만든 과학철학 어휘가 그대로 엔지니어링에 넘어왔다. 뒤에 `from home` · `without office data` 처럼 *어디서* 가 붙어야 주장이 정확해진다. "모른다"보다 강하다 — 확인 경로 자체가 막혀 있다는 뜻이다.
- 예문: Your own constraints make this unfalsifiable from home, since the office databases are unreachable.
- 유사어: there's no way to check this from here (평이한 회화체), we can't test that claim without X (조건을 앞세워 부드럽게)
- 반의어: home-checkable / verifiable by construction

## "Cost of being wrong: …"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 판단을 밀어붙이기 전에 오판의 대가부터 적을 때(설계 문서·리뷰 코멘트, 격식). 콜론 뒤에 시나리오를 그대로 이어 쓴다.
- 한국어: 틀렸을 때 치르는 값은 —
- 설명: 확률을 다투는 대신 결과의 크기를 재는 프레임이다. 확률이 낮아도 대가가 크면 안전한 쪽을 고르자는 논증으로 이어진다.
- 예문: Cost of being wrong: a later cleanup deletes the branch, and a live badge silently disappears from a page no test covers.
- 유사어: the downside if this is wrong is … (더 평이함), what happens if we're wrong (회화체 질문형), the blast radius (실패 파급 범위, 더 구어적 은유)
- 반의어: the upside if this holds

## "Even granting (that) X, …"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 상대 주장을 일단 통째로 인정해 준 뒤 그래도 남는 문제를 짚을 때(토론·리뷰, 격식).
- 한국어: X를 인정한다 쳐도 —
- 설명: `grant` 는 "양보해 인정하다"이고, 동명사구 `even granting …` 은 양보절 `even if we accept that …` 을 한 단어로 줄인 문어체다. 앞의 논쟁을 다시 열지 않고 논점을 한 칸 옮기게 해준다.
- 예문: Even granting that the exempt branch is dead, the parameter-row markup still renders for violations.
- 유사어: even if X holds (평이·중립), granted, X — but … (문두 삽입, 회화에서도 자연스러움), assuming for the sake of argument that X (가장 격식 있고 무거움)
- 반의어: that premise doesn't hold

## "drop an objection"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 반론을 제기했다가 근거를 보고 스스로 거두는 자리(토론 기록·회의). 짧게 `Objection 1 — dropped.` 로 쓰면 회의록 문법이 된다.
- 한국어: 반론을 철회하다.
- 설명: `withdraw` 보다 가볍고 담백하다. 진 게 아니라 그 갈래를 닫는다는 어감이라, 자기 반론을 스스로 접을 때 체면 소모가 적다.
- 예문: Objection 1 — dropped; explicit key-literal construction closes the data path.
- 유사어: withdraw an objection (더 격식·법정투), I'll take that back (회화체, 사과에 가까움), stand corrected (틀렸음을 인정하는 관용구)
- 반의어: press the point / stand by the objection

## "stage X's eventual deletion"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 지금 지우지는 않되 나중에 지울 수 있게 판을 깔아 두는 리팩터링을 설명할 때(설계 문서, 격식).
- 한국어: 나중의 삭제를 미리 준비해 두다.
- 설명: 여기서 `stage` 는 git 의 staging 이 아니라 연극의 "무대에 올릴 준비를 하다"에서 온 뜻이다. `eventual` 이 "언젠가는 반드시, 다만 지금은 아님"을 담아 준다.
- 예문: The new module lets the card import from one place, staging the old file's eventual deletion without touching it today.
- 유사어: pave the way for (더 일반적·비유적), set up the removal (평이한 회화체), make X deletable (결과만 말하는 담백한 형태)
- 반의어: entrench / cement the old path

## "documented failure mode"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-15-lot-outlier-merge-duplication-discuss.md
- 맥락: 이 저장소가 예전에 겪고 문서로 남겨둔 고장 유형을 근거로 삼을 때(코드 리뷰·ADR, 격식).
- 한국어: 문서로 남아 있는(이미 알려진) 고장 양식.
- 설명: `failure mode` 는 "어떤 식으로 망가지는가"라는 유형 이름이고, 앞의 `documented` 가 "내 인상이 아니라 기록"이라는 무게를 얹는다. 팀 규칙을 근거로 들 때 가장 반박하기 어려운 형태다.
- 예문: In a repo whose documented failure mode is exactly "a guard added to one copy never reaches its sibling," recording only the dead half misses the point.
- 유사어: a known failure pattern (덜 격식), this is how it breaks here (회화체로 풀어쓴 형태)
- 반의어: an unprecedented failure

## "the contract working"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/91c6854e — HTTP 에러 진단
- 맥락: 에러처럼 보이는 응답이 사실은 규약대로 동작한 결과라고 뒤집을 때(장애 분석 보고, 준격식).
- 한국어: 이건 버그가 아니라 계약(규약)이 제대로 작동한 것이다.
- 설명: `the 400 is the contract working` 처럼 계사문으로 쓴다. 에러 코드를 고장이 아니라 *합의된 응답*으로 재분류하는 한 줄이라, 잘못된 수정 작업을 미리 막는다.
- 예문: The catalog already says the slug must be `cdsem` or `hvsem`, so the 400 is the contract working.
- 유사어: working as designed / by design (더 짧고 건조함), that's expected behavior (가장 평이한 회화체), not a defect (분류만 부정)
- 반의어: a genuine defect / a real regression

## "extrapolate from X"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/91c6854e — HTTP 에러 진단
- 맥락: 있는 사례를 근거로 없는 것까지 미루어 짐작한 행동을 설명할 때(원인 분석, 준격식). 대개 그 추측이 빗나갔다는 함의를 달고 온다.
- 한국어: X에서 미루어 넘겨짚다.
- 설명: 수학의 외삽(外揷)에서 온 말이라 "가진 데이터 바깥으로 선을 늘였다"는 그림이 그대로 산다. 사람의 추측을 두고 쓰면 비난보다 진단에 가깝게 들린다.
- 예문: These are token callers extrapolating from the catalog — `/storage` exists, so they tried `/storage/wafer`.
- 유사어: guess by analogy (평이함), assume X follows the same shape (구조를 콕 집어 말할 때), read too much into X (넘겨짚음을 더 비판적으로)
- 반의어: stay within what's documented

## "one level up"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 같은 원칙이 한 층 위 단위에서 다시 적용된다고 짧게 붙일 때(ADR·설계 노트, 준격식).
- 한국어: 한 단계 위에서(더 큰 단위로).
- 설명: 문장 끝에 대시로 붙여 앞말을 재분류하는 꼬리표로 자주 쓴다. 새 개념을 만들지 않고 이미 세운 원칙의 적용 범위만 옮기므로, 설명이 짧아진다.
- 예문: A whole-batch transport failure marks every host in it failed — per-host isolation one level up.
- 유사어: at a coarser granularity (더 격식·정밀), the same idea, but for batches (회화체로 풀어씀)
- 반의어: one level down / per item

## "deploy in either order"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 두 쪽을 각각 배포해도 순서에 상관없이 안전하다고 보장할 때(운영 문서, 격식).
- 한국어: 어느 쪽을 먼저 올려도 된다.
- 설명: `either order` 는 "두 순서 중 아무거나"를 두 단어로 담는다. 배포 문서에서 이 한 줄이 있느냐 없느냐가 새벽에 순서를 맞춰 올려야 하느냐를 가른다.
- 예문: An entry arriving without a credential falls back to the proxy's environment — that fallback is what lets the two halves deploy in either order.
- 유사어: order-independent (형용사 한 단어, 더 건조함), no deploy ordering required (배포 문서 관용구), backward compatible (구버전과의 호환에 초점)
- 반의어: must be deployed in lockstep / server first, then client

## "memory-bounded"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 입력이 아무리 커져도 메모리 사용량이 일정 이하로 묶인다고 못 박을 때(성능 설계, 격식).
- 한국어: 메모리 사용이 상한에 묶인.
- 설명: `-bounded` 접미형은 무엇이 한계를 정하는지를 앞에 붙여 계속 확장된다 — `I/O-bound`, `CPU-bound`, `memory-bounded`. 뒤에 `regardless of fleet size` 처럼 *무엇과 무관한지* 를 붙여야 주장이 완성된다.
- 예문: Each file is handed to you the moment it downloads, then dropped, so the stream stays memory-bounded regardless of fleet size.
- 유사어: constant-memory (수학적으로 더 강한 주장), RAM stays flat (회화체·구체적)
- 반의어: unbounded / peak RAM grows with input

## "Correctness comes from A — not from B"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md
- 맥락: 흔한 오해를 바로잡으며 진짜 원인을 지정할 때(ADR 결론 문장, 격식).
- 한국어: 정확성은 A에서 나오지 B에서 나오는 게 아니다.
- 설명: `A, not B` 대구를 문장 전체 골격으로 쓴 형태다. B 자리에 상대가 믿고 있던 것을 놓아야 힘이 산다 — 부정이 반론의 자리를 대신한다.
- 예문: Correctness comes from isolating the destination per host and not sharing a connection — not from the storage medium.
- 유사어: what makes this safe is A, not B (평이한 강조구문), the deciding factor is A (담백한 단언)
- 반의어: both A and B are required
