# 2026-06-28 — 코칭

## 한글→영어

### 카드 1 — "너무 오래 걸려, 빠르게 못 하나?"   (내가 쓴 한글)
- 내가 쓴 한글: "golden_reregister_report_cond 작업 시간이 너무 오래 걸려. 빠르게 할 수 없나?"   (출처: transcript:[user])
- 자연스러운 영어: `golden_reregister_report_cond takes far too long to run. Is there any way to speed it up?`
- 왜 이렇게: "작업 시간이 오래 걸려"는 영어로 주어를 *스크립트 자체*로 잡아 `X takes too long (to run)`이 가장 자연스럽습니다("the work time is long" 식 직역은 어색). "빠르게 할 수 없나?"는 `Can't we make it faster?`도 되지만, 해결책을 묻는 부드러운 관용은 `Is there any way to speed it up?` — `speed up`이 "속도를 높이다"의 정석 동사입니다.

### 카드 2 — "wheel을 더 많이 움직여 결과를 봐줘"   (내가 쓴 한글)
- 내가 쓴 한글: "wheel 한 두 번으로는 배율이 거의 무의미하게 바뀌기 때문에 더 많이 움직이고 결과를 봐줘."   (출처: transcript:[user])
- 자연스러운 영어: `One or two wheel notches barely change the magnification, so scroll a lot more and let's see what happens.`
- 왜 이렇게: "한 두 번"은 마우스휠 맥락이라 `one or two notches`(휠 한 칸 = notch)가 정확합니다. "거의 무의미하게 바뀐다"는 `barely change`(거의 안 바뀐다) 한 단어로 압축 — `change meaninglessly`는 콩글리시입니다. "결과를 봐줘"는 명령형보다 `let's see what happens`(같이 결과를 보자)가 협업 톤으로 자연스럽고, 더 직접적으로는 `and report back what you see`.

### 카드 3 — "그 장비가 fab-out 됐어"   (내가 쓴 한글)
- 내가 쓴 한글: "auto로 바꿔줘. wheel 동작이 안 되던 장비가 fab-out 되었어."   (출처: transcript:[user])
- 자연스러운 영어: `Switch it to auto. The tool where the wheel didn't work has been decommissioned (fabbed out).`
- 왜 이렇게: 반도체 현장어 "fab-out"(장비가 팹에서 빠짐/폐기)은 사내에서 통하지만, 격식 문서엔 `decommissioned`(가동 중단·퇴역) 또는 `taken out of the fab`가 더 명확합니다. "~던 장비"는 관계절 `the tool where the wheel didn't work`로 — 장소가 아니라 *그 장비에서*라는 뜻이라 `where`가 맞습니다. 현재완료 `has been decommissioned`로 "이미 빠진 상태"를 표현.

### 카드 4 — "절차를 정리해줘"   (내가 쓴 한글)
- 내가 쓴 한글: "오피스에서 consensus eval 먼저 돌리는 절차 정리해줘."   (출처: transcript:[user])
- 자연스러운 영어: `Write up the steps for running the consensus eval first, at the office.`
- 왜 이렇게: "절차를 정리해줘"는 `organize the procedure`보다 `write up the steps`(단계별로 문서화해줘)가 개발 협업에서 훨씬 자연스럽습니다. `write up`은 "정리해 적다"의 관용 동사구. "먼저 돌리는"은 동명사 `running … first`로 명사화해 `the steps for -ing` 패턴에 끼웁니다.

### 카드 5 — "위치를 아직 잘 못 찾고 있어"   (내가 쓴 한글)
- 내가 쓴 한글: "PM dropdown 버튼 위치와 dropdown 위치를 아직 잘 못 찾고 있어."   (출처: transcript:[user])
- 자연스러운 영어: `It's still not reliably locating the PM dropdown button or the dropdown itself.`
- 왜 이렇게: "위치를 못 찾다"는 `can't find the location`보다 동사 `locate`(위치를 알아내다) 하나로 깔끔합니다. "아직 잘 못 찾고 있어"의 "잘"은 *안정적으로 못 한다*는 뜻이라 `not reliably locating`이 핵심 뉘앙스를 살립니다(가끔은 되지만 못 믿는다는 함의). 진행 상태이므로 현재진행형.

### 카드 6 — "지금 ~로 세팅되어 있나?"   (내가 쓴 한글)
- 내가 쓴 한글: "지금 mouse wheel로 zoom in/out 하는 걸 우선으로 하도록 세팅되어 있나?"   (출처: transcript:[user])
- 자연스러운 영어: `Is it currently set to prefer the mouse wheel for zooming in and out?`
- 왜 이렇게: "~를 우선으로 하도록"은 `to prefer X`(X를 우선시하다) 동사 하나로 자연스럽습니다("set to do X first"보다 의도가 분명). "세팅되어 있나?"는 수동태 `Is it set to …?`가 정석이고, "지금"은 `currently`로 현재 상태임을 강조합니다.

### 카드 7 — 고급 한글 번역 정독: "끄면 실전과 어긋난다"   (고급 한글 · 번역)
- 한글 원문: "clean-vs-raw A/B에서 CLEAN이 production-faithful로 확정됐고, 이게 report가 소비할 rank-1의 기준선입니다. 끄면 report 숫자가 실전과 어긋납니다."   (출처: transcript:[assistant])
- 자연스러운 영어: `The clean-vs-raw A/B established CLEAN as the production-faithful default, and that is the baseline for the rank-1 numbers the report consumes. Turn it off and the report's figures drift away from reality.`
- 번역 포인트: "~로 확정됐다"는 `establish X as Y`(X를 Y로 확립하다) 능동 구문이 깔끔합니다. "실전과 어긋난다"는 직역(`differ from reality`)보다 `drift away from reality`가 "기준에서 서서히 벗어난다"는 뉘앙스를 살립니다. 조건을 `If you turn it off, …` 대신 **명령형+and**(`Turn it off and …`)로 쓰면 "그러면 ~된다"는 인과가 구어적으로 강해집니다.

### 카드 8 — 고급 한글 번역 정독: "모순이 풀린다"   (고급 한글 · 번역)
- 한글 원문: "모순이 풀립니다: 버튼은 VLM coarse→fine으로 위치를 *학습*하는데, 드롭다운은 사람이 박은 *고정 비율*로 추정합니다. 같은 화면에서 한쪽은 적응형, 한쪽은 고정값."   (출처: transcript:[assistant])
- 자연스러운 영어: `That resolves the contradiction: the button learns its position via VLM coarse-to-fine, whereas the dropdown is estimated from a hard-coded ratio. On the same screen, one side is adaptive and the other is fixed.`
- 번역 포인트: "모순이 풀린다"는 `the contradiction resolves` 또는 `that resolves the contradiction`(앞 발견이 모순을 해소한다). 대조는 `whereas`(반면에 — 격식 대비 접속사)가 `but`보다 두 절을 나란히 견주는 데 적합합니다. "사람이 박은 고정 비율"의 "박은"은 `hard-coded`(코드에 박힌)로 딱 떨어집니다.

### 카드 9 — 고급 한글 번역 정독: "검증이 버그를 잡았다"   (고급 한글 · 번역)
- 한글 원문: "검증이 실제로 버그를 잡았습니다 — 검증 안 했으면 놓칠 뻔했습니다."   (출처: transcript:[assistant])
- 자연스러운 영어: `The verification actually caught a bug — I would have missed it if I hadn't checked.`
- 번역 포인트: "버그를 잡다"는 `catch a bug`가 관용. "놓칠 뻔했다"는 가정법 과거완료 `would have missed it if I hadn't checked`로 "안 했더라면 놓쳤을 것"을 표현합니다 — 한국어 "~뻔했다"의 반사실(counterfactual)을 영어는 if절 시제로 드러냅니다.

## 영어 다듬기

### 카드 1 — "나중에 다시 볼게"
- 내가 쓴 영어: "I see. I leave this topic and come visit later on."   (출처: transcript:[user])
- 정정: `I leave` → `I'll leave` (지금 정해서 *앞으로* 떠난다는 의사결정이므로 미래 `will`); `come visit` → `come back to it` (영어에서 추상적 주제로 "방문하다"는 어색 — 주제엔 `come back to`).
- 더 나은 표현: `Got it. I'll set this topic aside and come back to it later.`
- 왜: `set aside`(잠시 제쳐두다)가 "지금은 그만두고 나중에"의 뉘앙스를 정확히 담습니다. "later on"도 틀린 건 아니지만 `later` 하나로 충분하고, 주제를 다시 다루는 건 `come back to it`이 자연스럽습니다.

### 카드 2 — "~에서 어떤 결론이었지?"
- 내가 쓴 영어: "what was our conclusion from the test golden_consensus_eval_cond.py?"   (출처: transcript:[user])
- 정정: 문법 오류는 없습니다.
- 더 나은 표현: `What conclusion did we reach from testing golden_consensus_eval_cond.py?`
- 왜: `our conclusion from the test`도 통하지만, `reach a conclusion`(결론에 도달하다)이 더 관용적인 연어입니다. "the test ~.py"는 `testing ~.py`(동명사)로 바꾸면 "그 스크립트를 테스트한 것에서"라는 행위가 또렷해집니다.

### 카드 3 — "사무실 상황을 고려하면"
- 내가 쓴 영어: "research on PixelRAG and see if we can apply this method to the side_project under the current circumstance in the office of mine."   (출처: transcript:[user])
- 정정: `research on PixelRAG` → `research PixelRAG` (research가 타동사라 on 불필요); `the office of mine` → `my office` (`of mine`는 명사 뒤 소유 강조용이라 어색).
- 더 나은 표현: `Research PixelRAG and see whether we can apply it to the side project, given my current office constraints.`
- 왜: "현재 상황을 고려하면"은 `under the current circumstance`(단수도 어색)보다 `given my current office constraints`(현 사무실 제약을 감안하면)가 무엇이 제약인지까지 함축해 훨씬 구체적입니다. `whether`가 `if`보다 간접의문문에 격식 있게 맞습니다.

### 카드 4 — "확인이 필요해"
- 내가 쓴 영어: "I need to understand the existing VLM plumbing and the failure-handling/escalation path so a plan can reuse them."   (출처: transcript:[user])
- 정정: 문법 오류는 없습니다 — 잘 쓴 문장입니다.
- 더 나은 표현: `I need to map the existing VLM plumbing and the failure-handling / escalation path so that a future plan can build on them.`
- 왜: 이미 훌륭하지만 한 단계 위로: `understand`(이해하다)보다 `map`(구조를 지도처럼 파악하다)이 "재사용할 수 있게 구조를 훑겠다"는 의도에 더 맞습니다. `reuse`도 좋지만 `build on`(~을 토대로 쌓다)이 "기존 것을 확장한다"는 뉘앙스를 더 살립니다. `plumbing`(내부 배관=하부 연결 구조)은 아주 자연스러운 비유 표현이니 계속 쓰세요.
