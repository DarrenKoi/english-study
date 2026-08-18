# 2026-08-19 — 코칭

## 한글→영어

### 카드 1 — 시연영상을 어떻게 찍을지 상담   (내가 쓴 한글)
- 내가 쓴 한글: "@poc/workflow_3/monitor/align_fail_monitor.py 구동 하는 방식을 시연영상으로 만들어달라고 하는데, 어떻게 하는게 좋을까"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: I've been asked to record a demo video showing how `align_fail_monitor.py` runs. What's the best way to go about it?
- 왜 이렇게: "만들어달라고 하는데"의 주어는 남이고 부담은 나에게 있다 — `I've been asked to`(수동태) 가 이 구도를 그대로 옮긴다. 능동으로 `Someone asked me to` 라고 하면 그 사람이 누구인지가 궁금해져 초점이 흐려진다. "어떻게 하는게 좋을까"는 `How should I do it?` 보다 `What's the best way to go about it?` 가 상담을 청하는 어조에 가깝다 — `go about` 은 방법 전반을 묻는 구동사다.

### 카드 2 — 스크립트 요청 + 되짚기   (내가 쓴 한글)
- 내가 쓴 한글: "프레임 → mp4 조립 스크립트 만들어줘. 실제 align fail 발생했을 때 녹화하는게 더 확실하지 않으려나?"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Go ahead and write the frames-to-mp4 assembler. Though — wouldn't recording an actual align fail be more convincing?
- 왜 이렇게: "~않으려나?"는 확신 없이 던지는 되짚기다. 영어에서는 부정 의문문 `wouldn't ... ?` 가 정확히 그 자리에 온다 — `isn't it better?` 는 이미 답을 정해 둔 어조라 더 세다. 문두 `Though —` 는 앞 지시를 취소하지 않으면서 딴지를 붙이는 회화 장치다. "확실하다"는 여기서 정확성이 아니라 설득력이므로 `certain` 이 아니라 `convincing`.

### 카드 3 — 결과 확인 후 문제 보고   (내가 쓴 한글)
- 내가 쓴 한글: "warning은 뜨지 않았어. 영상 확인했는데, 장비 화면만 보이고 터미널에서 어떤게 나오는 지는 안보이네?"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: No warning came up. I watched the video — it only shows the tool window, and none of the terminal output is in it.
- 왜 이렇게: "안 보이네?"의 물음표는 질문이 아니라 발견의 억양이다. 영어로 `?` 를 붙이면 진짜 질문이 되어버리므로 평서문으로 두고 대신 `none of ...` 로 놀라움을 실었다. "확인했는데"의 `-는데`는 대조가 아니라 도입이라 `but` 이 아니라 대시(—)가 맞다. `warning은 뜨지 않았어` → `No warning came up` 처럼 부정을 명사 앞으로 당기면 짧고 자연스럽다.

### 카드 4 — 다른 형식으로도 보고 싶다   (내가 쓴 한글)
- 내가 쓴 한글: "@docs/project_progress/Align_Tuning_Agent.bento.html 이거를 pptx로도 확인하고 싶어. 배경은 하얀색으로."   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: I'd like to see this as a `.pptx` as well — white background, please.
- 왜 이렇게: "~도"는 `also` 를 어디에 놓을지 헷갈리는 자리인데, 목적어 뒤 `as well` 이 가장 안전하다. "확인하고 싶어"를 `check` 로 옮기면 검사·점검처럼 들린다 — 여기서는 눈으로 보고 싶다는 뜻이라 `see`. 마지막 조건은 완전한 문장을 만들지 않고 `white background, please` 로 던지는 편이 실제 업무 요청에 가깝다.

### 카드 5 — 산출물과 함께 커밋 요청   (내가 쓴 한글)
- 내가 쓴 한글: "생성 스크립트도 같이 커밋해줘"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Commit the generator scripts alongside it.
- 왜 이렇게: "같이"는 `together` 가 아니라 `alongside`(나란히) 나 `along with` 다. `together` 는 두 대상이 하나로 묶인다는 뜻이라 파일 두 개를 같은 커밋에 넣는 상황과 어긋난다. "생성 스크립트"는 `creation script` 가 아니라 `generator script` — 무언가를 만들어내는 프로그램에 붙는 관용 명칭이다.

### 카드 6 — 파일 위치 이동 지시   (내가 쓴 한글)
- 내가 쓴 한글: "@docs/project_progress/ 로 옮겨줘"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Move it under `docs/project_progress/`.
- 왜 이렇게: 디렉터리 안으로 넣을 때 영어는 `to` 보다 `under` 나 `into` 를 쓴다 — `under` 는 트리 구조를 전제해 "그 아래로"라는 위치 감각까지 담는다. `move A to B` 는 B 가 새 이름·새 경로 전체일 때 자연스럽다.

### 카드 7 — 보고서 슬라이드 요구사항 서술   (내가 쓴 한글)
- 내가 쓴 한글: "이 과제에 대핸 경과 보고서 제출이 필요함. Head Message (정량적 효과와 예상 종료 일자). 기존 문제점과 과제를 통해 해결하고자 하는 목표. 우리가 진행해온 추진 전략 / 그로 인한 기대 효과 등이 들어가 있어야해."   (출처: transcript:[user] auto_recipe_creator, 슬래시 명령 인자)
- 자연스러운 영어: I need to submit a progress report on this project. It should open with a head message carrying the quantified impact and the expected completion date, then cover the problem we started from and what the project set out to fix, the strategy we've pursued, and the payoff we expect from it.
- 왜 이렇게: 한국어 개조식(명사로 끊어 나열)을 영어로 그대로 옮기면 조각 문장만 남는다. `It should open with ..., then cover A, B, and C` 처럼 뼈대 동사 둘을 세우고 항목을 그 아래 매다는 편이 읽힌다. "해결하고자 하는 목표"는 `the goal we want to solve`(목표를 푼다는 비문)가 아니라 `what the project set out to fix` — `set out to` 가 "애초에 하려던 바"를 담는다. "그로 인한 기대 효과"는 `expected effect` 보다 `the payoff we expect` 가 보고서 어휘로 살아 있다.

### 카드 8 — 문서 반영 후 커밋   (내가 쓴 한글)
- 내가 쓴 한글: "CLAUDE.md에 추가하고 커밋 푸쉬 해줘"   (출처: transcript:[user] auto_recipe_creator)
- 자연스러운 영어: Add it to `CLAUDE.md`, then commit and push.
- 왜 이렇게: 한국어의 `-고`는 순서와 나열을 다 덮지만 영어는 갈라진다. 여기서는 순서가 있으므로 `and` 대신 `, then` 이 정확하다. `commit and push` 는 두 명령을 붙여 쓰는 굳은 짝이라 이건 `and` 로 둔다.

### 카드 9 — replay 촬영이 왜 조작이 아닌가   (고급 한글 · 번역)
- 한글 원문: "정상 가동 중인 장비에 replay 를 쏘면 `run_correction` 이 align fail 화면이 아닌 것을 매칭하게 되어, 그 컷은 증명이 아니라 반증 자료가 됩니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: Fire a replay at a tool that's running normally and `run_correction` will match against something that isn't an align-fail screen — that take stops being evidence and becomes evidence against you.
- 번역 포인트: "쏘면 ~ 됩니다"의 조건절을 `If you fire ...` 로 옮겨도 되지만, 명령형 + `and` 로 잇는 영어 관용(`Do X and Y will happen`)이 인과를 훨씬 빠르게 전달한다. "증명이 아니라 반증 자료"는 `proof / counter-proof` 로 대칭을 맞추기 쉬운데, 영어에서 그 쌍은 논리학 냄새가 난다. `evidence` 를 한 번 더 반복해 `evidence → evidence against you` 로 굴리면 같은 대구가 일상 어휘로 성립한다. "컷"은 영상 용어 `take` 나 `shot` 으로.

### 카드 10 — 정합이 어긋난 로그는 없느니만 못하다   (고급 한글 · 번역)
- 한글 원문: "시각이 어긋난 로그를 붙이면 없느니만 못해서 조용히 넘어가지 않게 했습니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: A log panel whose timestamps don't line up is worse than none at all, so I made the failure say why instead of passing over it in silence.
- 번역 포인트: "없느니만 못하다"는 `worse than nothing` 이 정확한 대응이고, `at all` 을 붙이면 강조까지 옮겨진다. "조용히 넘어가지 않게 했습니다"의 사동을 그대로 `made it not pass silently` 로 옮기면 어색하다 — 무엇을 하게 만들었는지(`say why`)를 긍정으로 세우고 부정은 뒤로 밀면 영어답다. "시각이 어긋난"은 `wrong time` 이 아니라 `don't line up` — 두 계열이 서로 안 맞는다는 뜻이라 정렬 동사를 쓴다.

### 카드 11 — 파일 계보를 왜 지키나   (고급 한글 · 번역)
- 한글 원문: "`git mv` 를 쓴 덕분에 diff 가 `1 file changed, 0 insertions(+), 0 deletions(-)` 로 잡혔습니다. … 이 파일은 앞으로도 갱신할 문서라 계보가 이어지는 편이 낫습니다."   (출처: transcript:[assistant] auto_recipe_creator)
- 자연스러운 영어: Using `git mv` is why the diff came out as `1 file changed, 0 insertions(+), 0 deletions(-)`. This document will keep being revised, so it's worth keeping its history unbroken.
- 번역 포인트: "덕분에"를 `thanks to` 로 옮기면 감사 표현으로 기울어 기술 설명에 뜬다. `Using X is why Y` 구문이 원인을 주어 자리에 앉혀 담담하게 만든다. "계보"는 사람 계보의 `lineage` 대신 파일 이력의 `history` 가 자연스럽고, "이어지는 편이 낫다"는 `unbroken`(끊기지 않은) 한 단어로 압축된다. "잡혔습니다"처럼 결과가 드러난 것은 `came out as`.

## 영어 다듬기

### 카드 1 — 레이아웃 변경 요청
- 내가 쓴 영어: "In pm-tuinng and tttm page, I think 비교 대상 / 비교 범위 component should be in the top (rather than placed like sidebar). After you select the info about tool models and recipe / parameter, you will be able to see data in the other components."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `In pm-tuinng and tttm page` → `On the pm-tune and TTTM pages` (오타 `tuinng`; 페이지 위에 얹힌 요소는 `in` 이 아니라 `on`; 대상이 둘이므로 복수 `pages`). `should be in the top` → `should be at the top` (`in the top` 은 "상위권 안에", 위치는 `at`). `placed like sidebar` → `docked as a sidebar` (관사 누락; `like` 는 비유라 실제 사이드바를 가리키려면 `as`).
- 더 나은 표현: On the pm-tune and TTTM pages, the 비교 대상 / 비교 범위 controls belong at the top of the page rather than docked in a left rail. Once a tool model and a recipe/parameter are selected, the downstream components should render their data.
- 왜: `I think ... should be` 는 두 겹 완화라 요청이 흐려진다 — `belong at the top` 은 한 마디로 위치를 규정하면서도 명령조가 아니다. `you will be able to see` 의 `you` 는 나인지 사용자인지 모호하니, 주어를 화면 요소로 바꿔 `the components should render` 로 두면 사양서 문장이 된다. `After you select` → `Once ... are selected` 로 바꾸면 조건(게이트)이라는 성격이 드러난다.

### 카드 2 — 선행 작업 대기 지시
- 내가 쓴 영어: "Wait until the agent finished the job in the first pane (check with herdr skill). After job done in the first pane. Start the job."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `Wait until the agent finished` → `Wait until the agent has finished` (미래의 완료 시점을 가리키는 `until` 절은 과거형이 아니라 현재완료/현재형). `After job done in the first pane.` → 마침표로 끊긴 조각 문장이라 절이 아니다.
- 더 나은 표현: Hold off until the agent in the first pane is done — check its status with the herdr skill — and start only then.
- 왜: `Hold off` 는 "일부러 착수를 미룬다"는 뜻이라 단순한 `wait` 보다 지시가 분명하다. 조각으로 흩어진 세 문장을 대시로 삽입구를 만들어 한 문장에 담으면 "확인은 곁가지, 조건은 하나"라는 구조가 드러난다. 끝의 `only then` 이 "그 전에는 안 된다"를 명시해 중복 문장이 필요 없어진다.

### 카드 3 — 502 버그 신고
- 내가 쓴 영어: "when I try to access recipe 열어보기 that are in the tables in recipe-status, I got 502 BAD gate way. The recipes I tried to get them are available in recipe-search/recipe-detail."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `when I try ... I got` → `when I try ... I get` (조건절이 현재면 주절도 현재; 재현되는 증상은 현재형). `502 BAD gate way` → `a 502 Bad Gateway` (한 단어 `Gateway`, 관사 필요). `The recipes I tried to get them` → `The recipes I tried to open` (관계절 안에 목적어 `them` 을 또 쓰는 이중 목적어 오류 — 한국어의 "그것들을"이 그대로 넘어온 자리다).
- 더 나은 표현: Opening a recipe from the recipe-status tables returns a 502 Bad Gateway, even though the same recipes load fine from recipe-search and recipe-detail. Could you check what's failing on the recipe-status side (Recipe TAT, align fail, meas fail)?
- 왜: 버그 신고는 `when I try to ..., I get ...` 보다 동작을 주어로 세운 `Opening X returns Y` 가 짧고 재현 조건이 또렷하다. 두 번째 문장은 `even though` 로 붙여 "같은 레시피인데 한쪽만 죽는다"는 대조를 한 문장에 담았다 — 이 대조가 사실상 진단의 절반이다. `what's going on` 도 통하지만 `what's failing` 이 무엇을 봐 달라는지 좁혀 준다.

### 카드 4 — 설계 선택 승인
- 내가 쓴 영어: "yes. explicit empty state is the way to go."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `explicit empty state` → `an explicit empty state` (셀 수 있는 단수 명사에 관사 필요).
- 더 나은 표현: Yes — go with an explicit empty state.
- 왜: `X is the way to go` 는 자연스러운 관용구지만 평가에 머문다. 상대가 결정을 기다리는 상황에서는 `go with X` 로 지시까지 얹는 편이 한 번에 끝난다. 문두 `Yes —` 처럼 대시로 이으면 승인과 지시가 한 호흡이 된다.

### 카드 5 — 파일 위치 묻기
- 내가 쓴 영어: "where is bento.html?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Where did the `.bento.html` end up?
- 왜: 문법 오류는 없다. 다만 `Where is X?` 는 상대가 당연히 알 거라는 전제가 없는 중립 질문이고, `Where did X end up?` 는 "네가 방금 만들었는데 어디에 놓였냐"는 맥락을 담는다. `end up` 이 과정 끝의 착지점을 가리켜, 직전 작업의 결과를 묻는 자리에 딱 맞는다.

### 카드 6 — 섹션 갱신 지시
- 내가 쓴 영어: "update things worth flagging"   (출처: transcript:[user] skewnono_v3_nuxt)
- 더 나은 표현: Redo the "Things worth flagging" section — I think you left things out.
- 왜: 오류는 없지만 `update` 는 "추가로 손봐라"에서 "처음부터 다시 써라"까지 폭이 넓어, 받는 쪽이 어느 쪽인지 고르게 된다. `Redo` 로 범위를 못박고 이유(`you left things out`)를 한 절 붙이면 왕복이 한 번 줄어든다. 문서 안 소제목을 가리킬 때는 따옴표로 묶어 그 제목 자체임을 표시한다.
