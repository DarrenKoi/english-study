# 2026-08-18 — 코칭

## 한글→영어

오늘 배치에는 내가 한국어로 쓴 문장이 없다 — user 메시지가 전부 영어였다. 그래서 이 절은
어시스턴트 쪽 고급 한국어를 영어로 옮기는 번역 정독 카드로만 채운다. 대신 아래
`영어 다듬기` 를 여섯 장으로 늘렸다.

### 카드 1 — 남의 세션 변경을 커밋에서 빼겠다는 통보 (고급 한글 · 번역)
- 한글 원문: "`poc/workflow_3/align/` 쪽 11개 파일은 제가 건드리지 않은 변경입니다 — 병렬 세션의 진행 중 작업으로 보입니다. 저장소 규약대로 제 파일만 pathspec으로 커밋하겠습니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: The 11 files under `poc/workflow_3/align/` are changes I never touched — they look like work in progress from a parallel session. Per the repo's convention I'll commit only my own files, by explicit pathspec.
- 번역 포인트: "제가 건드리지 않은 변경"은 관계절로 펴는 게 정답이다(`changes I never touched`). `untouched changes` 로 압축하면 "아무도 손대지 않은" 이 되어 주체가 사라지고, 이 문장의 요점은 바로 그 주체다. "~로 보입니다"의 짝은 `they look like` 이며 `it seems that` 보다 짧고 관찰의 어감이 산다. "진행 중 작업"은 `work in progress` 로 굳어진 표현이라 `ongoing work` 보다 이쪽이 개발 맥락에 맞는다. "저장소 규약대로"는 `according to` 대신 `per` 하나로 줄이는 게 커밋·리뷰 문체다. 마지막 "제 파일만 pathspec으로"는 부사구를 쉼표로 떼어 `by explicit pathspec` 으로 뒤에 붙였다 — 방법을 문장 끝에 놓으면 앞의 `only my own files` 라는 범위 선언이 흐려지지 않는다.

### 카드 2 — 제외 사유를 두 겹으로 대는 문장 (고급 한글 · 번역)
- 한글 원문: "제 작업이 아니라 다른 세션이 편집 중인 파일들이고, 테스트가 통과하는 상태인지 확인되지 않아 제외했습니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: I left them out on two counts: they aren't mine — another session is mid-edit on them — and I have no confirmation that they're in a passing state.
- 번역 포인트: 한국어는 이유 두 개를 `-고` 로 이어 붙이고 결론을 맨 뒤에 두지만, 영어는 결론을 먼저 세우고 이유를 콜론 뒤에 펼치는 편이 읽힌다. `on two counts`(두 가지 이유로)를 앞세우면 이유가 몇 개인지 미리 알려 주므로 독자가 문장 길이를 예측할 수 있다. "편집 중인"의 짝은 `mid-edit`(하이픈 한 단어)이며, `is editing` 으로 두면 지금 이 순간이라는 함의가 약해진다. "확인되지 않아"를 수동태 `it is not confirmed` 로 옮기면 누가 확인해야 하는지가 지워지므로, `I have no confirmation` 으로 주체를 되살렸다 — 판단의 책임을 내가 진다는 뜻이 이 보고의 핵심이다. "통과하는 상태"는 `in a passing state` 로 옮기면 테스트 용어로 정확하고, `whether the tests pass` 보다 상태 명사가 짧다.

### 카드 3 — 상태 용어를 오해하지 않게 풀어 주는 설명 (고급 한글 · 번역)
- 한글 원문: "`idle`은 죽은 게 아니라 마지막 턴을 끝내고 대기 중이라는 뜻이라, 컨텍스트를 그대로 유지한 채 이어서 지시할 수 있습니다."   (출처: transcript:[assistant] skewnono-v3-nuxt/421d3f75)
- 자연스러운 영어: `idle` doesn't mean dead — it means the session finished its last turn and is waiting, so it still holds its full context and you can pick up right where you left off.
- 번역 포인트: "A가 아니라 B라는 뜻이다"는 `mean` 을 두 번 쓰는 게 영어답다(`doesn't mean dead — it means …`). `not dead but waiting` 으로 줄이면 정의문이 아니라 형용사 대비가 되어, 용어를 설명하는 문장이라는 성격이 사라진다. "~라, ~할 수 있습니다"의 인과는 `so` 로 잇되 그 앞에 `it still holds its full context` 를 끼워 근거를 하나 더 세웠다 — 한국어의 "컨텍스트를 그대로 유지한 채"라는 부대상황을 영어에서 부사구로 끌고 가면(`while keeping its context`) 문장이 무거워진다. "이어서 지시할 수 있습니다"의 관용 짝은 `pick up right where you left off` 다. 직역 `you can continue giving instructions` 는 문법은 맞지만 회화에서 거의 안 쓴다.

### 카드 4 — 완곡하게 절차를 하나 권하는 문장 (고급 한글 · 번역)
- 한글 원문: "다만 커밋 전에 `uv run python poc/workflow_3/align/test_correction.py` 정도는 돌려 보고 넣는 편이 안전합니다."   (출처: transcript:[assistant] auto-recipe-creator/565bfc95)
- 자연스러운 영어: That said, it'd be safer to run at least `uv run python poc/workflow_3/align/test_correction.py` before you commit them.
- 번역 포인트: 문두 "다만"은 `However` 보다 `That said` 가 어울린다 — 앞말을 취소하지 않고 조건 하나만 얹는 자리이기 때문이다. "~정도는"의 짝이 `at least` 인데, 위치가 중요하다. 동사 앞(`at least run`)에 두면 "돌리기라도 하라"가 되고, 목적어 앞에 두면 "이것만이라도"가 되어 원문의 뜻과 맞는다. "~하는 편이 안전합니다"는 가정법 `it'd be safer to` 로 옮기는 게 자연스럽다. 직설 `it is safer to` 는 사실 진술이 되어 권고의 완곡함이 사라지고, `you should` 는 원문보다 세다. "돌려 보고 넣는"의 두 동작은 영어에서 하나로 줄이고 `before you commit` 이 순서를 대신 담게 했다 — 동사를 둘 다 살리면(`run it and then add them`) 절차 나열이 되어 권고의 초점이 흩어진다.

## 영어 다듬기

### 카드 1 — 없는 기능을 지목하는 요청
- 내가 쓴 영어: "for the pm-tune page, you have to be able to search recipe component, which is missing now."   (출처: transcript:[user] skewnono-v3-nuxt/bd4caa93)
- 정정: ① `search recipe component` → `search for a recipe component`. `search` 는 "장소를 뒤진다"는 뜻의 타동사라서(`search the room`) 찾는 **대상**을 목적어로 받으려면 `for` 가 필요하다. 목적어를 바로 받고 싶으면 `search` 대신 `find` 나 `look up` 을 쓴다. 그리고 `component` 는 가산명사이므로 관사 없이 홀로 못 선다. ② `which is missing now` → `which is currently missing`. `now` 는 문장 끝에서 시점을 가리키는 부사라 관계절 안의 상태를 수식하기엔 헐렁하다.
- 더 나은 표현: The pm-tune page needs to let you search for a recipe component — that's missing right now.
- 왜: `you have to be able to` 는 상대를 주어로 세운 의무문이라 "당신이 할 수 있어야 한다"로 읽힌다. 요청하려는 것은 사람의 능력이 아니라 페이지의 기능이니, 주어를 페이지로 바꾸고 `needs to let you …` 로 두면 요구 대상이 분명해진다. 관계절 `which is missing` 을 대시 뒤 독립절 `that's missing right now` 로 떼어 낸 것도 의도적이다 — 관계절은 부수 설명으로 읽히지만, 이 문장에서 "지금 없다"는 사실이 요청의 근거 전부다.

### 카드 2 — 필터 상태를 저장해 달라는 요청
- 내가 쓴 영어: "in skewvoir, we have filter in 검색 component. Can we make it remembered in localStorage? the filter setting can be customized and stored in user's localStorage for the better UX."   (출처: transcript:[user] skewnono-v3-nuxt/79582753)
- 정정: ① `we have filter` → `we have filters` 또는 `we have a filter`. 가산명사는 관사나 복수형 중 하나가 필요하다. ② `in 검색 component` → `in the 검색 component`. 앞에서 특정한 컴포넌트를 가리키므로 정관사가 붙는다. ③ `in user's localStorage` → `in the user's localStorage`. 소유격 앞에도 그 사람이 특정될 때는 정관사가 온다. ④ `for the better UX` → `for better UX`. 비교급이라도 특정 대상을 비교하지 않는 일반 진술이면 무관사다(`for better performance`, `for faster startup` 과 같은 꼴).
- 더 나은 표현: Skewvoir's 검색 component has filters — can we persist them to `localStorage`? Letting each user keep their own filter setup across visits would be better UX.
- 왜: `make it remembered` 는 문법은 서지만 어색하다. 저장을 뜻하는 동사가 이미 있다 — `persist X to storage` 가 프런트엔드 표준 어휘이고, 더 평이하게는 `remember X across reloads`. 세 번째 문장의 `can be customized and stored` 는 두 수동태를 `and` 로 이어 누가 무엇을 하는지 지운다. `Letting each user keep …` 로 동명사 주어를 세우면 행위자(사용자)와 이득(UX)이 한 문장에서 연결된다. `their own` 은 성별을 특정하지 않는 단수 대명사로 쓰는 요즘 표준 용법이다.

### 카드 3 — 포트를 정리해 달라는 지시
- 내가 쓴 영어: "stop the port 5050, 3000"   (출처: transcript:[user] skewnono-v3-nuxt/40758a79)
- 정정: ① 포트는 멈출 수 있는 물건이 아니다. 멈추는 것은 그 포트를 붙잡고 있는 프로세스이므로 `stop whatever is running on ports 5050 and 3000` 처럼 대상을 하나 끼워야 한다. ② `the port 5050` → `port 5050`. 번호가 붙은 고유 지시에는 관사를 붙이지 않는다(`room 302`, `gate 7` 과 같은 꼴). ③ 두 개를 나열할 때는 쉼표가 아니라 `and` 로 잇고 명사를 복수로 만든다 — `ports 5050 and 3000`.
- 더 나은 표현: Kill whatever's listening on ports 5050 and 3000.
- 왜: 의도가 통했으니 이 문장이 실패한 건 아니다. 다만 `listening on` 을 넣으면 판별 기준까지 함께 전달된다 — "그 포트에서 듣고 있는 것"이 곧 `lsof -iTCP:PORT -sTCP:LISTEN` 로 확인할 대상이라, 상대가 이름으로 프로세스를 찾다가 엉뚱한 걸 죽일 여지가 줄어든다. 개발 서버를 정리할 때는 `stop` 보다 `kill` 이 흔하다. `stop` 은 서비스 관리자에게 정상 종료를 요청하는 어감이고, `kill` 은 신호를 보내 끊는 쪽이다.

### 카드 4 — 파일이 있는지 묻는 질문
- 내가 쓴 영어: "have we made office.py in provider?"   (출처: transcript:[user] skewnono-v3-nuxt/bf11e5de)
- 정정: ① `in provider` → `in the providers folder` 또는 `under providers/`. 폴더 이름이 실제로 복수형이고, 위치를 뜻하는 폴더에는 관사가 필요하다. 경로로 쓸 때는 `under providers/` 처럼 슬래시를 붙여 폴더임을 드러내는 편이 짧다. ② `made` 는 물건을 제작한다는 뜻이라 파일에는 `created` 나 `added` 가 맞는다.
- 더 나은 표현: Do we have an `office.py` under `providers/` yet?
- 왜: `have we created …?` 도 옳지만, 알고 싶은 것은 만든 이력이 아니라 지금 있는지 여부다. `Do we have X yet?` 이 그 질문을 정확히 담고, 문미 `yet` 이 "아직 안 만들었다면 그것도 답"이라는 여지를 준다 — 그래서 상대가 없다고 답하면서 이유까지 붙이기 쉬워진다. 파일명 앞의 `an` 은 특정 파일이 아니라 "그런 파일 하나"를 묻는 것이라 부정관사가 맞는다.

### 카드 5 — 설정을 추가해 달라는 지시
- 내가 쓴 영어: "setup this config in herdr config."   (출처: transcript:[user] auto-recipe-creator/687a4050)
- 정정: ① `setup` → `set up`. 붙여 쓴 `setup` 은 명사·형용사 전용이고(`the setup`, `setup costs`), 동사는 반드시 띄어 쓴다. ② `in herdr config` → `in the herdr config`. ③ 다만 이 문장의 진짜 문제는 동사 선택이다. 이미 완성된 블록을 파일에 넣어 달라는 요청이라 `set up`(처음부터 구성하다)보다 `add … to`(추가하다)가 맞는다.
- 더 나은 표현: Add this to the herdr config.
- 왜: 목적어 `this config` 가 뒤의 `herdr config` 와 같은 단어를 두 번 쓰게 만든다. 붙여 넣은 블록을 `this` 하나로 가리키면 반복이 사라지고, 무엇을 어디에 넣는지가 한눈에 남는다. 한 단계 더 격식을 얹고 싶으면 `Please add these keybindings to the herdr config.` 처럼 대상의 이름(`keybindings`)을 밝히면 된다 — 지시문에서는 목적어를 구체화하는 쪽이 언제나 안전하다.

### 카드 6 — 배경 세션이 있는지 확인
- 내가 쓴 영어: "do we have a session running in bg now?"   (출처: transcript:[user] skewnono-v3-nuxt/421d3f75)
- 정정: 문법 오류는 없다. `have + 목적어 + 현재분사` 는 정상적인 구문이고(`we have a job running`), 축약 `bg` 도 개발자 사이에서는 통한다.
- 더 나은 표현: Any background sessions running right now?
- 왜: 원문은 "우리가 하나를 가지고 있는가"를 묻지만, 실제로 알고 싶은 것은 몇 개든 있는지다. 복수 `Any background sessions` 로 열어 두면 상대가 "하나 있습니다"와 "셋 있습니다"를 같은 형식으로 답할 수 있다. `Do we have …?` 를 떼고 명사구로 시작하는 것은 구어에서 흔한 생략이라 짧고 자연스럽다. 격식을 갖춰 쓸 자리라면 `Is anything still running in the background?` 처럼 완전한 문장으로 되돌리면 된다. `bg` → `background` 로 편 것은 글로 남는 지시일 때만 신경 쓸 문제다.
