# 2026-08-17 — 코칭

## 한글→영어

### 카드 1 — 보고서 한국어 윤문 요청 (내가 쓴 한글)
- 내가 쓴 한글: "docs/project_progress/04_workflow_3.md 를 중심으로 이번에 갱신한 진행보고서 한국어를 자연스럽게 윤문 (경어체 유지, 기술용어 영문 병기 유지, 표/제목 구조 유지)"   (출처: transcript:[user] auto-recipe-creator/565bfc95 — `/humanize-korean` 슬래시 명령 인자)
- 자연스러운 영어: Polish the Korean in the progress reports I just updated, with `docs/project_progress/04_workflow_3.md` as the focus. Keep the polite register, keep the English gloss next to technical terms, and leave the table and heading structure alone.
- 왜 이렇게: "윤문"은 `polish` 나 `copy-edit` 이다. `proofread` 는 오탈자 잡기라 문체를 다듬는 이 일과 다르고, `rewrite` 는 내용까지 손대도 된다는 허가로 읽혀 위험하다. "~를 중심으로"는 `centering on` 보다 `with X as the focus` 가 지시문에서 자연스럽다 — 분사구는 무엇에 걸리는지가 흐려진다. 괄호 안 제약 셋은 영어에서 괄호로 밀어 넣지 말고 명령형 세 개로 세워 대등하게 두는 편이 낫다. 요청의 절반이 사실 이 제약이기 때문이다. "경어체"는 `polite register`(격식 층위)로, "영문 병기"는 `the English gloss next to ~`(원어를 나란히 적어 둔 것)로 옮긴다. 마지막 "유지"는 앞의 둘과 성격이 달라 `keep` 을 세 번 반복하지 않고 `leave … alone`(손대지 말라)으로 바꿨다.

### 카드 2 — 상태 구분이 흐려지는 문서 (고급 한글 · 번역)
- 한글 원문: "'구현 완료'와 '실제로 실행됨'은 다른 상태이고, 진행 보고서는 그 구분을 흐리기 가장 쉬운 문서입니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: "Implemented" and "actually ran" are two different states — and a progress report is the document most likely to blur that line.
- 번역 포인트: 따옴표에 든 두 상태를 영어에서도 따옴표로 유지해야 한다. 인용부호가 "이건 용어로 취급하라"는 신호라, 없으면 `implemented` 가 그냥 형용사로 흘러간다. "다른 상태이고"의 `-고` 를 `and` 로 직역하면 두 절이 대등하게 늘어져 뒤 절의 무게가 죽는다. 대시 뒤에 `and` 를 놓으면 앞 문장을 받아 한 단계 밀어 올리는 어감이 생긴다. "가장 ~하기 쉬운 문서"는 `the easiest document to blur` 보다 `the document most likely to blur` 가 맞다 — 난이도가 아니라 **개연성**을 말하는 문장이기 때문이다. "구분을 흐리다"의 관용 짝은 `blur the line`(선을 흐리다)이라 목적어를 `distinction` 에서 `line` 으로 바꿔야 영어다워진다.

### 카드 3 — 성과가 아니라 발견 (고급 한글 · 번역)
- 한글 원문: "SEM 패널 ROI를 빈 landmark 디렉터리로만 잡아 step 6에서 매번 중단. 08-12에 원인 제거. 성과가 아니라 발견으로 서술했습니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: The correction step scoped the SEM panel ROI to an empty landmark directory, so it stalled at step 6 every time; the cause was removed on 08-12. I've written it up as a finding, not an achievement.
- 번역 포인트: 명사형으로 끊은 개조식 한국어("~ 중단.", "~ 제거.")를 영어로 그대로 옮기면 전보문이 된다. 주어와 동사를 되살려 완전한 문장으로 펴는 게 첫 작업이다. "~로만 잡아"는 범위를 한정했다는 뜻이므로 `scope A to B` 가 정확하다 — `set` 이나 `take` 로는 "그것만 대상으로 삼았다"는 한정의 뜻이 안 산다. "매번 중단"의 `stall` 은 `stop` 과 달리 **가려던 것이 멈춰 섰다**는 함의가 있어 파이프라인 사고 보고에 맞는다. 마지막 문장의 대비 `as a finding, not an achievement` 는 한국어 어순 그대로 살릴 수 있는 드문 경우다. `write up`(문서로 정리해 적다)은 `write` 보다 "보고서에 올렸다"는 절차 감각을 담는다.

### 카드 4 — 손댄 범위를 한정해 보고 (고급 한글 · 번역)
- 한글 원문: "00/01/03은 이번에 새로 쓴 문단만 같은 패턴으로 손봤습니다 — 7월에 검토받은 기존 문장은 그대로 뒀습니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: For 00/01/03 I applied the same patterns only to the paragraphs written this round; the July prose that had already been reviewed was left untouched.
- 번역 포인트: 한국어 주제 표지 "00/01/03은"을 영어 주어로 올리면 문서가 무언가를 한 것처럼 읽힌다. `For 00/01/03` 로 전치사구를 앞에 두고 주어는 행위자 `I` 로 세워야 맞는다. "만"의 위치가 핵심인데, `only applied` 로 앞당기면 "적용만 했다"가 되므로 `only to the paragraphs` 로 한정 대상 바로 앞에 붙인다. "7월에 검토받은"은 이번 작업보다 먼저 끝난 일이라 과거완료 `had already been reviewed` 가 필요하다 — 단순 과거로 두면 두 사건의 선후가 사라진다. "그대로 뒀습니다"는 `left untouched` 가 관용이고, 여기서 수동태는 행위자를 숨기려는 게 아니라 **기존 문장**에 초점을 붙들어 두려는 선택이다.

## 영어 다듬기

### 카드 1 — 진척 보고서를 갱신해 달라는 지시
- 내가 쓴 영어: "we have to write the report what we have done so far. what's the achievements and the bottlebecks in the docs/project_progress/ update based on the latest tasks done."   (출처: transcript:[user] auto-recipe-creator/565bfc95)
- 정정: ① `the report what we have done` → `a report on what we have done`. 관계사 `what` 은 선행사를 가질 수 없다(`what` = `the thing which`). 명사 `report` 뒤에 내용을 붙이려면 전치사 `on`/`about` 이 있어야 한다. ② `what's the achievements` → `what are the achievements`. 주어가 복수다. ③ `bottlebecks` → `bottlenecks`(병목).
- 더 나은 표현: We need to write up where the project actually stands. Update the reports under `docs/project_progress/` from the latest work — what we've achieved, and where we're still stuck.
- 왜: 한 덩어리로 이어진 요청을 목적(무엇을 원하는가)과 지시(무엇을 해라)로 끊었다. `write the report` 의 정관사는 상대가 어느 보고서인지 이미 안다는 전제인데, 실제로는 폴더째 갱신하는 일이라 `write up where the project stands`(현황을 정리하다)가 요청의 실체에 가깝다. `achievements and bottlenecks` 는 보고서 목차어라 딱딱하니, 구어 지시에서는 `what we've achieved / where we're still stuck` 처럼 절로 풀면 훨씬 자연스럽다. `based on the latest tasks done` 의 `done` 은 뒤에 붙은 과거분사가 무엇을 꾸미는지 흐릿하다 — `from the latest work` 로 줄이면 뜻이 그대로 남는다.

### 카드 2 — 파이프라인 논리 점검 요청
- 내가 쓴 영어: "check if the code and logic are well set for downloading consensus -> extracting align point from consensus images and apply that to the live SEM Box in the remote monitor."   (출처: transcript:[user] auto-recipe-creator/03453890)
- 정정: ① `and apply that` → `and applying it`. 앞의 `downloading`, `extracting` 과 병렬이므로 동명사여야 한다. 전치사 `for` 의 목적어 세 개가 형태를 맞춰야 문장이 성립한다. ② `extracting align point` → `extracting the align point`(가산명사에 관사).
- 더 나은 표현: Audit the whole path end to end — downloading the consensus, extracting the align point from the consensus images, and applying it to the live SEM box on the remote monitor. I want to know whether the logic holds up at every step.
- 왜: `check if … are well set` 은 뜻은 통하지만 `well set` 이 영어에서 잘 안 쓰이는 결합이다. 점검을 부탁하는 자리에서는 `audit`(훑어 검증하다)이나 `does the logic hold up`(논리가 버티는가)이 관용이다. 화살표로 이어 붙인 단계는 영어에서 대시 + 동명사 목록으로 펴면 그대로 읽히고, `end to end` 한 마디가 "중간만 보지 말고 전 구간"이라는 요구를 담는다. 위치 전치사도 갈린다 — 화면 안이 아니라 원격 모니터 **위에 떠 있는** 창이므로 `in the remote monitor` 가 아니라 `on the remote monitor` 다.

### 카드 3 — 걱정하는 실패 시나리오 설명
- 내가 쓴 영어: "Since the consensus image size and the live SEM Box size are different, there has to be rescale process involved. I am worried that even if you get the right align point, it might screw up in the live SEM box due to mis-scaling."   (출처: transcript:[user] auto-recipe-creator/03453890)
- 정정: `there has to be rescale process` → `there has to be a rescale step`. `process` 는 가산명사라 관사 없이 단수로 쓸 수 없다.
- 더 나은 표현: Because the consensus image and the live SEM box aren't the same size, a rescale has to happen somewhere. My worry is that even with the right align point, mis-scaling could land the click in the wrong place.
- 왜: 원문도 충분히 통하지만 세 군데가 한 단계 올라간다. ① `the consensus image size and the live SEM Box size are different` 는 `size` 를 두 번 끌고 다닌다. `the two aren't the same size` 로 묶으면 짧고 강해진다. ② `it might screw up` 의 `it` 이 무엇을 가리키는지 모호하다 — 좌표인지 클릭인지 절차 전체인지. `mis-scaling could land the click in the wrong place` 처럼 원인과 결과를 각각 주어·목적어로 세우면 걱정의 내용이 그대로 검증 가능한 명제가 된다. ③ `I am worried that …` 도 맞지만, `My worry is that …` 은 걱정을 명사로 앉혀 뒤 문장에서 그것 하나만 반박·해소하기 쉽게 만든다.

### 카드 4 — 남은 세션을 정리해 달라는 요청
- 내가 쓴 영어: "close sessions remain"   (출처: transcript:[user] skewnono-v3-nuxt/1cbe5d61)
- 정정: 문장이 아니라 세 단어의 나열이라 두 가지로 갈린다 — 명령문 "close sessions"(세션을 닫아라)에 `remain` 이 붙은 것인지, "닫힌 세션이 남아 있다"는 서술인지. 동사와 목적어의 관계를 드러내려면 관계절이 필요하다: **Close the sessions that are still open.**
- 더 나은 표현: Shut down whatever sessions are still hanging around — and tell me first if any of them is holding unsaved work.
- 왜: 짧은 지시는 좋지만 **한 단어라도 두 갈래로 읽히면 짧은 게 손해**다. `whatever sessions are still hanging around` 는 개수를 모른 채 "남은 것 전부"를 가리키는 구어 관용이고, `hang around` 가 "끝났는데도 안 사라지고 있다"는 뉘앙스를 담아 상황에 딱 맞는다. 뒤에 붙인 조건 한 줄이 실제로 이 요청에서 가장 중요한 부분이었다 — 닫기 전에 무엇을 확인해야 하는지를 지시에 함께 실으면 되묻는 왕복이 사라진다.

### 카드 5 — 죽은 서버 프로세스 재시작 지시
- 내가 쓴 영어: "kill the stale flask parent and restart it"   (출처: transcript:[user] skewnono-v3-nuxt/1cbe5d61)
- 더 나은 표현: Kill the stale Flask parent process and bring the server back up.
- 왜: 문법 오류는 없다. 다만 `restart it` 의 `it` 이 방금 죽인 부모 프로세스를 가리키게 되어, 문자 그대로 읽으면 "죽인 그것을 다시 살려라"가 된다. 실제로 원한 건 부모 프로세스가 아니라 **서버**를 다시 띄우는 것이므로 목적어를 갈아 주는 편이 정확하다. `bring X back up` 은 서버·서비스를 다시 올릴 때 쓰는 구동사로, `restart` 보다 "죽었다가 다시 선다"는 그림이 선명하다. `flask` 는 프레임워크 이름이니 대문자 `Flask` 로 쓴다.

### 카드 6 — 목업 스타일을 페이지에 적용
- 내가 쓴 영어: "apply 3a style into the tttm page"   (출처: transcript:[user] skewnono-v3-nuxt/deda1b39)
- 정정: `apply … into` → `apply … to`. `apply A to B` 가 고정된 짝이다. `into` 는 안으로 들어가는 이동을 그리므로 "규칙·양식을 대상에 적용한다"는 뜻과 맞지 않는다.
- 더 나은 표현: Apply the 3a layout to the TTTM page.
- 왜: 관사 `the` 를 붙이면 "우리가 아는 그 3a"가 되어 목업의 특정 안을 가리킨다. 무관사 `3a style` 은 일반적인 양식을 말하는 것처럼 읽힌다. 또 실제로 바꾼 것이 색이 아니라 배치였으므로 `style` 보다 `layout` 이 요청을 정확히 담는다 — 실제 작업 로그에도 "apply 3a는 repaint가 아니라 layout 작업"이라는 판단이 남아 있다.

### 카드 7 — 지적받은 위험을 처리하자는 동의
- 내가 쓴 영어: "yes. we have to deal with those possible risks"   (출처: transcript:[user] auto-recipe-creator/03453890)
- 더 나은 표현: Yes — let's handle both. Start with the `OVERSAMPLE` one, since that's the failure no gate can catch.
- 왜: 오류는 없다. `possible risks` 의 `possible` 은 잉여다 — risk 자체가 이미 "일어날 수도 있는 일"이라 형용사가 뜻을 더하지 않는다. `we have to` 는 외부에서 지워진 의무처럼 들리는데, 방금 스스로 결정한 자리에서는 `let's` 가 맞는 어조다. 개수(`both`)와 순서(`start with`)를 한 줄 붙이면 승인이 곧 작업 지시가 되어 되묻는 왕복이 준다.
