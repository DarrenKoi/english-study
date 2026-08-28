# 2026-08-29 — 새 표현

오늘 원료는 opencode 토론 기록 두 건(search-around 재설계, workflow_4 엔진 대 runner)과
oc-discuss 스킬 본문, 그리고 chat/RAG 연동 세션의 영어 보고입니다. 토론문 특유의
판정어(misattribution, theatre)와 실패 모드 명명(converge confidently wrong, silent drift)이
많이 나왔습니다.

## "risk-now vs. risk-never"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-workflow4-engine-vs-runner-debate.md
- 맥락: 안정된 코드를 지금 건드리는 실재 위험과, 안 건드리면 영영 발생하지 않는 가상 비용을 맞세워 반대할 때(설계 토론·문어)
- 한국어: 지금의 위험 대 영원히 없는 위험
- 설명: `A vs. B` 꼴로 명사화한 판정어. 하이픈으로 `risk-now`/`risk-never` 를 한 단어처럼 묶어, 시제가 다른 두 위험을 저울 양쪽에 올린다. 뒤에 설명 없이 이 구절 하나로 결론을 찍는 용법이 강력하다.
- 예문: Freezing the demo-only engine costs zero production risk, while grafting routes onto the live loop is real risk now — it's risk-now vs. risk-never.
- 유사어: paying a real cost today for a hypothetical benefit (풀어쓴 문어형), borrowing trouble (구어; 사서 고생)
- 반의어: a free option (지금 아무 비용 없이 열어 두는 선택)

## "battle-tested"
- 레지스터: technical, professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-workflow4-engine-vs-runner-debate.md
- 맥락: 오래 운영되며 실전의 회귀·사고를 견뎌 신뢰가 쌓인 코드·도구를 가리킬 때(긍정)
- 한국어: 실전에서 단련된
- 설명: 군사 은유. `tested` 만으로는 "테스트를 돌렸다"지만 `battle-` 이 붙으면 "실제 사고를 겪고 살아남았다"가 된다. 그래서 이런 코드를 건드리는 제안은 자동으로 부담이 커진다.
- 예문: That's the engine reimplemented as an imperative jump loop inside the most battle-tested function in the repo.
- 유사어: proven in production (격식·중립), tried and true (구어), mature (완곡)
- 반의어: unproven / greenfield

## "a misattribution"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-workflow4-engine-vs-runner-debate.md
- 맥락: 상대 논거가 "그 속성은 그 대상의 것이 아니다"로 무너질 때, 오류의 종류에 이름을 붙여 지적(토론·문어)
- 한국어: 잘못된 귀속, 남의 것을 그 대상 탓/덕으로 돌림
- 설명: 단순히 wrong 이라 하지 않고 *어떤 종류로* 틀렸는지 명명하는 토론 기술. teardown 이 runner 소유가 아니라 cycle.py 소유이므로 "두 번째 엔진도 teardown 을 복제해야 한다"는 전제가 통째로 무너진다는 식이다.
- 예문: Teardown lives in cycle.py, not in the runner, so "a second engine must replicate teardown" is a misattribution.
- 유사어: that credit belongs elsewhere (풀어쓴 회화), misplaced (형용사형; 완곡)

## "by definition, not evidence"
- 레지스터: professional
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-workflow4-engine-vs-runner-debate.md
- 맥락: 당연히 그럴 수밖에 없는 사실(신규 패키지의 소비자 0)을 근거로 쓰는 논증을 자를 때(토론·문어)
- 한국어: 정의상 그런 것이지 증거가 아니다
- 설명: `X, not Y` 대구로 상대 근거의 지위를 강등시킨다. 정의에서 따라 나오는 사실은 아무것도 입증하지 못한다는 논리학 상식을 넉 단어로 압축했다.
- 예문: Zero consumers at t=0 of a deliberately untracked package is the starting state by definition, not evidence.
- 유사어: that's true by construction (기술 문어; 뉘앙스 거의 동일), that proves nothing (직설·구어)

## "premature coupling"
- 레지스터: technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-workflow4-engine-vs-runner-debate.md
- 맥락: 아직 필요하지 않은 의존을 미리 만들어 두는 설계를 기각할 때(설계 리뷰·문어)
- 한국어: 시기상조의 결합
- 설명: `premature optimization` 의 자매 표현. "언젠가 쓸지 모르니 지금 연결해 두자"는 제안에, 결합 자체가 비용임을 상기시키는 한 단어 판정이다.
- 예문: Making the engine emit the runner's StepResult shape is premature coupling — two viewers, one per scope, is coherent.
- 유사어: premature abstraction (추상화를 미리 만드는 쪽), speculative generality (리팩터링 냄새 이름)
- 반의어: loose coupling

## "converge confidently wrong"
- 레지스터: technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-search-around-zoomout-grid-debate.md
- 맥락: 알고리즘이 시끄럽게 실패하는 대신 확신에 찬 오답으로 안착하는, 가장 위험한 실패 모드를 말할 때(기술 문어)
- 한국어: 확신을 갖고 틀린 값에 수렴하다
- 설명: `doesn't just get noisy — it converges confidently wrong` 구조가 핵심. 잡음(noisy)은 눈에 보이지만, 주기 구조에서 한 주기 어긋난 상관값은 높은 신뢰도로 나오므로 오류 신호 자체가 없다. 부사 `confidently` 가 `wrong` 을 꾸며 모순 어법처럼 읽히는 것이 의도다.
- 예문: On periodic gratings, phase correlation doesn't just get noisy — it converges confidently wrong, with no error signal at all.
- 유사어: fail silently (조용한 실패; 확신의 뉘앙스는 없음), answer confidently but wrongly (회화형)
- 반의어: fail loudly

## "dead reckoning"
- 레지스터: technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-search-around-zoomout-grid-debate.md
- 맥락: 외부 피드백 없이 명령값 누적만으로 현재 위치를 추정하는 방식을 비판적으로 이름 붙일 때(항법 용어 차용)
- 한국어: 추측 항법 — 계기 없이 속도·방향 누적으로만 위치를 셈하는 것
- 설명: 배·비행기 항법에서 온 용어. `dead-reckoning with zero feedback` 처럼 쓰면 "체인이 길어질수록 오차가 무한히 쌓인다"는 비판이 용어 하나에 담긴다.
- 예문: Chaining 30 double-clicks with no stage readback is dead reckoning with zero feedback — origin return is an untested assumption.
- 유사어: open-loop control (제어공학 용어), flying blind (구어; 계기 없이 감으로)
- 반의어: closed-loop control (측정 피드백으로 보정)

## "scrape the floor"
- 레지스터: technical, conversational
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-search-around-zoomout-grid-debate.md
- 맥락: 값이 하한선을 간신히 턱걸이해 여유(margin)가 전혀 없음을 말할 때(구어적 은유, 기술 토론에서도 자연스러움)
- 한국어: 바닥을 긁다시피 간신히 하한을 넘다
- 설명: 원문은 `scale 0.67, scraping the MIN_CONFIRM_SCALE=0.6 floor`. 통과는 했지만 최악 조건에서 바로 떨어질 값이라는 경고가 `scraping` 한 단어에 실린다.
- 예문: The nearest rung restores scale 0.67, scraping the 0.6 confirm floor with no margin for a smaller frame.
- 유사어: barely clear the bar (턱걸이 통과), cut it close (아슬아슬하다; 더 구어)
- 반의어: with plenty of headroom

## "bound the damage"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-28-search-around-zoomout-grid-debate.md
- 맥락: 실패를 없애지는 못해도 피해의 상한은 묶여 있다고 방어할 때(설계 근거·문어)
- 한국어: 피해에 상한을 두다
- 설명: bound 를 동사로 쓰는 수학·공학 어법. "이 설계는 시간이 5-10배 든다"는 반론에 "abort 래치와 알림 경로가 damage 를 bound 한다"로 받으면, 위험을 부정하지 않으면서 수용 가능함을 논증한다.
- 예문: The abort latch plus the exhausted-to-notification path bounds the damage of a runaway search.
- 유사어: cap the downside (손실 상한; 금융 어감), limit the blast radius (기술 은유)
- 반의어: an unbounded failure mode

## "latch onto"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (workflow_4 리뷰 세션)
- 맥락: 한 번 잡은 대상(폴더·가설·값)을 놓지 않고 계속 물고 있을 때 — 종종 잘못 잡은 것에(기술·구어)
- 한국어: 물고 늘어지다, 한 번 잡은 것에 들러붙다
- 설명: 걸쇠(latch)가 찰칵 걸리면 저절로 풀리지 않는다는 은유. 미러의 첫 폴링이 runner 의 mkdir 보다 빨라 *직전 run 폴더*에 영구히 붙어 버린 경쟁 조건을 이 동사 하나가 정확히 그린다.
- 예문: If its first poll beat the runner's mkdir, the mirror latched onto the previous run's folder forever.
- 유사어: lock onto (조준·추적 어감), fixate on (사람의 집착 쪽)
- 반의어: let go of

## "decorative"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (workflow_4 리뷰 세션)
- 맥락: 존재하지만 동작에 아무 영향이 없는 코드·표를 판정할 때(리뷰; cosmetic 보다 "장식품"이라는 조롱기가 조금 더 있다)
- 한국어: 장식일 뿐인, 동작과 무관한
- 설명: 원문은 `the per-class table was decorative and wrong` — 장식일 뿐인데 심지어 내용도 틀렸다는 이중 판정. 뒤에 `and wrong` 을 붙이는 순간 "지워야 한다"가 자동으로 따라온다.
- 예문: Since the runner aborts on any failure, the per-class routing table was decorative — and wrong.
- 유사어: cosmetic (동작 무관 수정), a no-op in practice (실질 무동작)
- 반의어: load-bearing

## "a torn read"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (workflow_4 리뷰 세션)
- 맥락: 쓰다 만 파일을 다른 쪽이 읽어 반쪽짜리 데이터를 보는 동시성 현상(기술 용어)
- 한국어: 찢어진 읽기 — 절반만 쓰인 상태를 읽어 버리는 것
- 설명: `torn`(찢긴) 이 절반은 새 데이터, 절반은 옛 데이터인 상태를 그린다. 3.6 MB HTML 을 매초 새로고침하는 브라우저 앞에서 비원자적으로 덮어쓰면 나는 현상이고, 처방은 임시 파일 + `os.replace` 원자 교체다.
- 예문: A non-atomic 3.6 MB rewrite under a one-second browser refresh risks a torn read; tmp plus os.replace closes it.
- 유사어: a half-written file (풀어쓴 형태), a dirty read (DB 용어; 커밋 전 데이터를 읽음)
- 반의어: an atomic write

## "a bound that never fires"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/3cc218db (chat/RAG ack 세션)
- 맥락: 조건상 절대 발동할 수 없는 한도·가드는 없는 것과 같다고 지적할 때(기술 문어)
- 한국어: 결코 발동하지 않는 상한
- 설명: fire 는 트리거·가드가 "발동한다"는 관용 동사. 호출당 타임아웃이 턴 전체의 wall-clock 보다 길면 논리적으로 먼저 잘릴 수 없으므로, 존재하되 무의미한 한도가 된다. 설정값 리뷰에서 그대로 쓸 수 있는 판정문.
- 예문: A per-call timeout longer than the turn's wall-clock is a bound that never fires.
- 유사어: a guard in name only (이름뿐인 가드), dead code (도달 불가 코드; 더 넓은 말)
- 반의어: an enforced limit

## "collapse to (one character)"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/b08be631 (chat/RAG 연동 세션)
- 맥락: 커 보이던 문제가 아주 작은 해법 하나로 줄어들었음을 보고할 때(보고·구어)
- 한국어: (문제가) ~하나로 접히다/수렴하다
- 설명: 원문은 `The whole problem collapsed to one character: a leading _`. 콜론 뒤에 그 "한 글자"를 바로 보여 주는 구성이 극적 효과를 만든다. 해법의 크기를 극단적으로 줄여 말해 설계의 우아함을 자랑하는 문형.
- 예문: The whole "foreign git repo inside this tree" problem collapsed to one character: a leading underscore.
- 유사어: boil down to (요지는 ~다), reduce to (중립·문어)
- 반의어: balloon into (걷잡을 수 없이 커지다)

## "Half yes, half no."
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/3cc218db (chat/RAG 데이터 분담 논의)
- 맥락: 복합 질문에 "절반은 맞고 절반은 아니다"로 답을 여는 첫 문장(회화·보고 서두)
- 한국어: 반은 예, 반은 아니오
- 설명: 두 갈래 답을 예고하는 신호탄. 바로 뒤에 `Yes to X — ... No to Y — ...` 로 각 절반을 전개해야 완성된다. 뭉뚱그린 `it depends` 보다 훨씬 정보량이 많다.
- 예문: Half yes, half no — yes to the office owning the testing, no to the RAG repo owning structured data access.
- 유사어: yes and no (더 흔한 형태), it's a mixed bag (평가가 갈릴 때)
- 반의어: an unqualified yes (조건 없는 동의)

## "worth your confirmation when convenient"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/0002648a (mag_pixel 정리 세션)
- 맥락: 급하지 않은 확인 요청을 보고 말미에 정중하게 덧붙일 때(문어)
- 한국어: 편하실 때 확인해 주실 만한 것
- 설명: `worth + 명사` 로 요청의 무게를 낮추고 `when convenient` 로 마감 압박을 없앤다. "지금 답 안 주셔도 되지만 언젠가는 정리돼야 한다"는 뉘앙스를 한 줄에 담는 보고 마무리 상투구.
- 예문: One thing worth your confirmation when convenient: whether the reference width is exactly 135 mm or a calibrated figure.
- 유사어: when you get a chance (구어), no rush, but… (더 캐주얼)
- 반의어: this needs your sign-off before we ship

## "(be) theatre"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (oc-discuss 스킬 본문 인용)
- 맥락: 형식만 갖추고 실질이 없는 절차를 신랄하게 잘라 말할 때(문어·평가)
- 한국어: 연극(시늉)일 뿐이다
- 설명: `security theater` 계열의 은유. 약한 반론에만 답하는 토론은 절차를 다 거쳤어도 검증이 아니라 공연이라는 판정. 명사 하나를 보어로 세워 `X is theatre.` 로 끝내는 것이 어법의 전부라 더 세다.
- 예문: A debate where you answer only the weak objections is theatre.
- 유사어: a box-ticking exercise (요식 행위), going through the motions (시늉만 내기)
- 반의어: a substantive review

## "silent drift"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (oc-discuss 스킬 본문 인용)
- 맥락: 아무 오류 신호 없이 상태·문맥이 조금씩 어긋나 가는 실패를 이름 붙일 때(기술 문어)
- 한국어: 소리 없는 표류
- 설명: 세션 id 를 잃은 채 새 세션이 열리면 겉으로는 성공처럼 보이면서 대화 문맥만 통째로 어긋난다 — 그 실패 모드의 이름. `the silent drift this skill exists to prevent` 처럼 방어 장치의 존재 이유를 설명하는 자리에 잘 붙는다.
- 예문: An empty session id would start a fresh session while appearing to succeed — precisely the silent drift this check exists to prevent.
- 유사어: quiet divergence (명사형 대안), skew (어긋남; 통계 어감)
- 반의어: a loud failure / a hard error

## "restate rather than advance"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/116ed130 (oc-discuss 스킬 본문 인용)
- 맥락: 논의가 새 근거 없이 같은 말만 반복되는 시점을 짚어 종료를 선언할 때(문어)
- 한국어: 진전 없이 되풀이만 하다
- 설명: `A rather than B` 로 두 동사를 맞세워 "말은 오가지만 위치가 안 바뀐다"를 진단한다. 토론 종료 조건을 감정 없이 기술하는 데 알맞다.
- 예문: Stop when the exchange converges — when the model drops its objections, or both sides restate rather than advance.
- 유사어: go in circles (구어), talk past each other (서로 딴 얘기만 하다)
- 반의어: move the discussion forward
