# 2026-09-01 — 코칭

## 한글→영어

### 카드 1 — 한 번에 가자   (내가 쓴 한글)
- 내가 쓴 한글: "한번에 가자. align_fail_monitor는 그 이후에 모양을 볼게. (문제 있을 시에 기능을 on/off 하면 되잖아)"   (출처: transcript:[user] auto-recipe-creator aeec243f)
- 자연스러운 영어: Let's do it all in one pass. I'll look at how `align_fail_monitor` shapes up afterwards — if anything goes wrong we can just toggle the feature off.
- 왜 이렇게: "한 번에 가자"를 `let's go at once` 로 옮기면 "즉시 출발하자"가 되어 뜻이 어긋난다. 여기서 뜻하는 건 작업을 쪼개지 않는다는 것이라 `in one pass`(한 번의 훑기로) 또는 `in one go` 를 쓴다. "모양을 볼게"의 '모양'은 형태가 아니라 결과의 인상이므로 `shapes up`(어떻게 되어 가는지) 이 맞는다. 괄호 속 근거는 영어에서 대시 뒤로 빼면 자연스럽고, 한국어의 "~하면 되잖아"는 상대를 설득하는 어미라 `we can just ~` 의 `just` 가 그 가벼움을 받아 준다.

### 카드 2 — 기본값을 on 으로   (내가 쓴 한글)
- 내가 쓴 한글: "일단 align fail monitor에서는 지금 거의 모든 기능들이 구현되어 있기 때문에 기본적으로 on으로 하면 돼."   (출처: transcript:[user] auto-recipe-creator aeec243f)
- 자연스러운 영어: For now, default `align_fail_monitor` to on — nearly everything in it is already implemented.
- 왜 이렇게: "일단"은 `first of all` 이 아니라 `for now`(잠정적으로) 다. 한국어는 이유(`~때문에`)를 앞에 두지만 영어 지시문은 결정을 먼저 말하고 근거를 뒤로 보낸다. `default X to on` 처럼 `default` 를 동사로 쓰면 "기본적으로 on으로 하면 돼"가 다섯 단어로 줄어든다. "기능들이"의 복수 `-들` 은 영어로 옮길 때 `nearly everything` 같은 단수 총칭이 더 자연스럽다.

### 카드 3 — 더 테스트가 필요한 경우   (내가 쓴 한글)
- 내가 쓴 한글: "남의 접근 요청을 승낙하거나, 상대가 조작 중일 때 판단과 같은 경우는 우리가 좀 더 테스트를 해봐야 할 것 같아."   (출처: transcript:[user] auto-recipe-creator aeec243f)
- 자연스러운 영어: The cases I'd want more testing on are approving someone else's access request, and deciding what to do while the other side is mid-operation.
- 왜 이렇게: "~와 같은 경우는"을 `cases like ~ are` 로 직역하면 주어가 무거워진다. `The cases I'd want more testing on are A and B` 처럼 관계절로 주어를 만들고 콜론 없이 바로 나열하는 편이 읽힌다. "판단"은 명사지만 영어에서는 `deciding what to do` 로 동명사구를 쓰는 쪽이 자연스럽다 — 무엇에 대한 판단인지가 드러나기 때문이다. "상대가 조작 중일 때"의 '조작 중'은 `mid-operation` 한 단어로 붙는다.

### 카드 4 — 선택권은 백엔드가   (내가 쓴 한글)
- 내가 쓴 한글: "그냥 쉽게 가도 된다. model 선택권은 backend (_rag)가 가져감. system prompt도 backend에서 처리. skewnono에 관련된 기능만 유저가 사용해야 함."   (출처: transcript:[user] skewnono-v3-nuxt cec320af)
- 자연스러운 영어: Take the simple route. Model choice belongs to the backend (`_rag`), and the system prompt is handled there too — the user should only see the skewnono-specific features.
- 왜 이렇게: "쉽게 가도 된다"는 허가가 아니라 지시에 가까워서 `you can go easy` 보다 명령형 `take the simple route` 가 의도에 맞는다. "선택권을 가져감"은 소유 이전이라 `belongs to`(귀속된다) 로 옮기면 명사 `ownership` 을 안 꺼내고도 통한다. 개조식 세 조각은 영어에서 그대로 끊으면 메모처럼 읽히니 `and`·대시로 한 문장에 묶는다. "유저가 사용해야 함"의 실제 뜻은 노출 범위 제한이라 `use` 보다 `see` 가 정확하다.

### 카드 5 — import 대신 파일 존재로 판정   (고급 한글 · 번역)
- 한글 원문: "판정을 import 이 아니라 파일 존재로 한 것이 이 설계의 핵심 트레이드오프입니다. import 로 판정하면 정확하지만 부팅 때 faiss·torch 를 끌어와 앱이 죽을 수 있고, 그건 '채팅이 안 됨'이 아니라 '사이트 전체가 안 뜸'입니다."   (출처: transcript:[assistant] skewnono-v3-nuxt cec320af)
- 자연스러운 영어: Deciding on file presence rather than on a successful import is the central trade-off in this design. Importing would be the accurate test, but it drags `faiss` and `torch` in at boot and can take the app down with it — and that isn't "chat is broken", that's "the whole site won't come up".
- 번역 포인트: "판정"은 문맥마다 다른 단어가 붙는다. 여기서는 두 갈래 중 하나를 고르는 일이라 `deciding on X` 가 맞고, `judgment` 는 사람이 내리는 평가라 어긋난다. "끌어와"는 원치 않는데 딸려 온다는 뜻이라 `pull in` 보다 `drag in` 이 어감을 살린다. 마지막 대비는 한국어가 인용부호로 처리했는데, 영어도 같은 장치를 그대로 쓰되 `that isn't A, that's B` 로 주어를 반복해야 대구가 선다 — `not A but B` 로 줄이면 두 인용 사이의 낙차가 사라진다.

### 카드 6 — 이름이 거짓말을 시작한다   (고급 한글 · 번역)
- 한글 원문: "컨트롤이 둘이 되면서 게이트 이름이 거짓말을 하기 시작합니다."   (출처: transcript:[assistant] skewnono-v3-nuxt cec320af)
- 자연스러운 영어: The moment there are two controls, the gate's name starts to lie.
- 번역 포인트: "~되면서"는 시간과 인과를 함께 담은 어미라 `as` 로도 되지만, `the moment ~` 를 쓰면 "그 순간부터"라는 경계선이 살아난다. "거짓말을 하기 시작합니다"를 `begins to tell a lie` 로 늘이면 은유가 무거워진다 — 영어에서 이름·주석·지표가 주어일 때 `lie` 는 자동사로 그냥 쓴다(`the name lies`). 짧게 두는 게 원문의 촌철 효과를 옮기는 길이다.

### 카드 7 — 하면 안 되는 단순화   (고급 한글 · 번역)
- 한글 원문: "비밀값을 상수 블록으로 옮기는 건 하면 안 되는 단순화입니다."   (출처: transcript:[assistant] auto-recipe-creator aeec243f)
- 자연스러운 영어: Moving secrets into the constants block is the one simplification you don't get to make.
- 번역 포인트: "하면 안 되는"을 `a simplification you must not make` 로 옮기면 규정집 말투가 된다. `you don't get to ~` 는 "그럴 자격이 없다"는 뜻이라 금지를 부드럽게, 그러나 더 단호하게 전한다. `the one X` 의 `one` 도 번역에 없는 장치인데, 앞에서 여러 단순화를 권한 흐름에 예외를 하나 세우는 자리라 붙여야 문맥이 맞는다.

## 영어 다듬기

### 카드 8 — 설정 파일이 너무 많다
- 내가 쓴 영어: "we have so many things to control via workflow_3_config.py and config_loader.py and .env .etc. can't we make it simpler? why not making multiple folders based on the purpose of the tests?"   (출처: transcript:[user] auto-recipe-creator aeec243f)
- 정정: `why not making` → `why not make`. `why not` 뒤에는 동사원형이 온다(`Why not try it?`). 동명사를 쓰려면 `how about making` 으로 바꿔야 한다. `.etc` → `etc.` — 점은 뒤에 하나만 찍는 축약 표기다.
- 더 나은 표현: There's too much to control across `workflow_3_config.py`, `config_loader.py`, and `.env`. Can we make this simpler — say, splitting the tests into folders by purpose?
- 왜: `so many things` 은 감탄에 가깝고 `too much` 가 불만을 정확히 담는다. `via A and B and C` 처럼 `and` 를 반복하면 나열이 지루해지니 `across` + 콤마 목록으로 바꾼다. 두 질문을 따로 던지는 대신 `— say, ...` 로 제안을 붙이면 "불평 + 대안"이 한 호흡에 들어간다.

### 카드 9 — 기본 모델 지정
- 내가 쓴 영어: "in chat, let's set the default model to be 'GaiA-Small-Latest'. Since you're taking care of the front-end. do you need to be matching with the _rag folder?"   (출처: transcript:[user] skewnono-v3-nuxt cec320af)
- 정정: `Since you're taking care of the front-end.` 은 종속절만 있고 주절이 없는 조각 문장이다. 뒤 문장에 붙여 `Since you're handling the front end, do you ...` 로 이어야 한다. `do you need to be matching with` → `do you need to match`. 상태 유지가 아니라 단순 조건이라 진행형이 어색하고, `match` 는 타동사라 `with` 가 필요 없다.
- 더 나은 표현: In chat, let's make `GaiA-Small-Latest` the default model. Since you're handling the front end, does that need to line up with the `_rag` folder?
- 왜: `set X to be Y` 의 `to be` 는 군더더기고, `make X the default` 가 한 단계 자연스럽다. 주어를 `you` 에서 `that` 으로 바꾸면 "네가 맞춰야 하나"가 아니라 "그 값이 맞아야 하나"가 되어 실제 질문에 가깝다. `line up with` 은 두 설정이 서로 어긋나면 안 된다는 뜻을 `match` 보다 잘 전한다.

### 카드 10 — 배치도 색상 버그 신고
- 내가 쓴 영어: "There is an weird part in the 장비 그룹 배치도 ... When I check more than two parameters from 분석 조건. the 장비 그룹 배치도 display them under 2D charts and they are dispersed in the chart and the color is not reflect the groups.. Some of tools are blue and all other are red."   (출처: transcript:[user] skewnono-v3-nuxt dc332be2)
- 정정: `an weird` → `a weird`(자음 소리 `w` 앞에서는 `a`). `When I check ... 분석 조건.` 뒤의 마침표는 종속절을 끊어 조각으로 만든다 — 쉼표로 바꿔 주절과 이어야 한다. `display` → `displays`(주어가 단수). `the color is not reflect` → `the colors don't reflect`(`reflect` 가 본동사라 `is` 가 들어가면 안 된다). `Some of tools` → `Some of the tools`(`some of` 뒤에는 한정사가 필요). `all other are` → `all the others are`(대명사로 쓸 때는 `others`).
- 더 나은 표현: Something looks wrong with the 장비 그룹 배치도 on pm-planning and tttm. When I select more than two parameters under 분석 조건, the chart scatters the tools and the colors don't seem to track the grouping — some tools are blue, the rest are red. Judging by where the dots sit, there should be more than two colors. Could you dig into this?
- 왜: `There is a weird part in X` 는 "X 안에 이상한 부분이 있다"는 물리적 그림이라 어색하다. 증상 신고는 `Something looks wrong with X` 로 여는 게 관용적이다. `and ... and ... and` 로 이은 세 증상은 세미콜론·대시로 갈라야 각각이 보인다. `reflect` 대신 `track`(따라 움직이다) 을 쓰면 "색이 그룹을 따라가야 하는데 안 따라간다"는 기대까지 담긴다. 명령형 `debug this issue please` 는 `Could you dig into this?` 로 바꾸면 같은 요청이 훨씬 자연스럽다.

### 카드 11 — 범례가 필요하다
- 내가 쓴 영어: "We have to mention the meaning of red and blue in 장비 그룹 배치도 in order to prevent misunderstanding."   (출처: transcript:[user] skewnono-v3-nuxt dc332be2)
- 정정: (문법 오류 없음)
- 더 나은 표현: We should spell out what red and blue mean on the 장비 그룹 배치도, so it can't be misread.
- 왜: `mention` 은 지나가듯 언급하는 것이라 범례를 붙이자는 요구에는 약하다. `spell out`(빠짐없이 명시하다) 이 의도한 강도다. `the meaning of red and blue` 같은 `of` 명사구는 영어에서 `what red and blue mean` 이라는 절로 푸는 쪽이 가볍다. `in order to prevent misunderstanding` 은 격식이 과한 목적절이라, 수동형 `so it can't be misread` 로 줄이면 "오해할 여지 자체를 없앤다"는 뜻이 더 강해진다.

### 카드 12 — 스크립트 폴더 정리
- 내가 쓴 영어: "can we prune the py files based on the purposes in @scripts/ ? make subfolders and organize the files. you can remove the old files that no more needed."   (출처: transcript:[user] skewnono-v3-nuxt fdbfe0cc)
- 정정: `the old files that no more needed` → `the old files that are no longer needed`. 관계절에도 동사가 필요하고, `no more` 는 수량·시간의 종료(`no more coffee`)에 쓰며 상태의 종료는 `no longer` 다.
- 더 나은 표현: Can we reorganize the Python files in `@scripts/` by purpose — subfolders, one per job? Feel free to delete anything that's no longer needed.
- 왜: `prune` 은 잘라내기만 뜻하는데 실제 요청은 재배치가 주라서 `reorganize ... by purpose` 가 맞는다. `make subfolders and organize the files` 는 같은 말을 두 번 하므로 대시 뒤 `subfolders, one per job` 한 조각이면 충분하다. `you can remove` 는 능력을 말하는 것처럼 읽히니 허가를 뜻하는 `feel free to delete` 로 바꾼다.

### 카드 13 — 언더스코어 폴더 통합 제안
- 내가 쓴 영어: "don't we need to refactor the folders (starting with '_') in back_dev_home to be gathered into a single folder? the folders are used for managing the web app. so we can put them together."   (출처: transcript:[user] skewnono-v3-nuxt f2d1927f)
- 정정: `to refactor the folders ... to be gathered into` 는 to부정사가 둘 겹쳐 주체가 흐려진다. `refactor the folders ... and gather them into a single folder` 로 등위 접속하거나, `pull the folders ... into a single folder` 로 합친다.
- 더 나은 표현: Shouldn't we pull the `_`-prefixed folders in `back_dev_home` into one folder? They're all app plumbing, so they belong together.
- 왜: `don't we need to ~` 는 필요를 묻는 말이라 제안치고는 무겁다. `shouldn't we ~` 가 "그러는 게 낫지 않나"라는 제안에 맞는다. `(starting with "_")` 삽입구는 ``_``-prefixed 라는 형용사로 앞당기면 문장이 끊기지 않는다. `used for managing the web app` 은 길어서, 이 판에서 통하는 명사 `plumbing`(배관 = 기능이 아닌 기반 코드) 한 단어로 대체된다. 마지막 `so we can put them together` 는 가능성을 말하는데, 근거를 대는 자리라 `they belong together`(한데 있는 게 맞다) 가 논지에 맞는다.

### 카드 14 — 포트 정리
- 내가 쓴 영어: "clean the ports 5050, 3000"   (출처: transcript:[user] skewnono-v3-nuxt 81fe0f54)
- 정정: (문법 오류 없음 — 명령형 메모라 관사 생략도 허용된다)
- 더 나은 표현: Free up ports 5050 and 3000 — kill whatever's listening.
- 왜: 포트에는 `clean`(더러운 것을 닦다) 을 쓰지 않는다. 굳어진 짝은 `free up a port` 이고, `clear port 5050` 도 통한다. 목록을 쉼표로만 끊으면 명령의 끝이 어디인지 모호하니 마지막 항목 앞에 `and` 를 넣는다. `kill whatever's listening` 을 덧붙이면 "프로세스를 죽여도 된다"는 허가까지 전해져서 되묻는 왕복이 줄어든다.

### 카드 15 — 폴더 삭제 확인
- 내가 쓴 영어: "I see. In ebeam folder, we have cdsem and skew folders. can they be deleted?"   (출처: transcript:[user] skewnono-v3-nuxt f2d1927f)
- 정정: `In ebeam folder` → `In the ebeam folder`. 특정 폴더를 가리키므로 관사가 필요하다. 관사를 피하려면 경로 표기 ``Under `ebeam/` `` 를 쓴다.
- 더 나은 표현: Got it. Under `ebeam/` there are still `cdsem/` and `skew/` — are those safe to delete?
- 왜: `I see` 는 이해했다는 신호로 맞지만 조금 딱딱해서, 대화의 방향을 바꿀 때는 `Got it` 이 자연스럽다. `we have` 는 소유를 말하는데 여기서는 존재 확인이라 `there are` 가 정확하고, `still` 을 넣으면 "아직 남아 있다"는 의심이 드러나 질문의 의도가 앞선다. `can they be deleted` 는 기술적 가능성을 묻지만 실제로 궁금한 건 안전성이라, `are those safe to delete` 가 답을 정확히 겨눈다.
