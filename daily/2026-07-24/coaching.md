# 2026-07-24 — 코칭

> 오늘 배치에는 직접 쓴 한국어 문장이 없어(스펙 문서의 한국어는 `repo:` 라 코칭 대상 밖) 한글→영어 섹션은 비웠습니다. 대신 영어로 지시·보고한 문장이 아홉 건 있어 그쪽을 촘촘히 다뤘습니다.

## 영어 다듬기

### 카드 1 — 야간 작업 지시문

- 내가 쓴 영어: "start work at 2:10am. Review the code what we have done yesterday (2026-07-23). Remove dead & unnecessary code conservatively. Refactor the code if neccessary (use the skill simplify). list up the code what you have changed in docs/issue folder. If other session is working on, wait until it is finished."   (출처: transcript:[user] skewnono_v3_nuxt, `/goal`)
- 정정:
  - `the code what we have done` → **`the code we wrote`** 또는 `what we did`. `what` 은 선행사를 이미 품은 관계대명사라 앞에 명사를 둘 수 없습니다. 명사 뒤에는 `that`(생략 가능), 명사가 없을 때만 `what`. 같은 오류가 `the code what you have changed` 에서 반복됩니다.
  - `neccessary` → **`necessary`** (c 하나, s 하나).
  - `list up` → **`list`**. up 을 붙이는 건 한국식 영어이고, 영어에서는 그냥 `list` 이거나 `write up a list of`.
  - `If other session is working on` → **`If another session is working in this tree`**. 셋을 손봐야 합니다. ① 셋 이상 중 "다른 하나"는 `another`. ② `other session` 은 관사 없이 쓸 수 없는 단수 가산명사. ③ `working on` 의 `on` 은 목적어를 요구하는데 비어 있습니다 — 목적어를 안 쓸 거면 `on` 을 빼세요.
- 더 나은 표현: "Start at 02:10. Review what we changed yesterday (2026-07-23) and remove dead code conservatively; refactor only where it clearly helps (use the simplify skill). Write up everything you touched under `docs/issues/`. If another session is already working in this tree, wait until it finishes."
- 왜: 지시문은 동사로 시작하는 명령형을 끝까지 유지해야 읽는 쪽이 항목을 놓치지 않습니다. `Refactor the code if necessary` 는 조건이 느슨해 "고칠 데가 보이면 다 고쳐라"로도 읽히는데, `only where it clearly helps` 로 좁히면 보수적으로 하라는 앞 문장과 결이 맞습니다. `use the skill simplify` 는 어순이 뒤집혔습니다 — 영어는 수식어가 앞에 오니 `the simplify skill`.

### 카드 2 — tool 이미지 경로 설명 (오타·수일치)

- 내가 쓴 영어: "each image contain relavent condition (cond.txt). you can get this in the same image_dir."   (출처: transcript:[user] skewnono_v3_nuxt, msr_file 이미지 요청)
- 정정:
  - `each image contain` → **`each image has`**. `each + 단수명사`는 단수 취급이라 동사에 -s 가 붙습니다. 그리고 파일이 따로 있는 관계라면 contain(안에 품다)보다 `has`(딸려 있다)나 `comes with` 가 정확합니다.
  - `relavent` → **`relevant`**.
  - `condition` → **`its measurement condition`**. 여기서는 특정 이미지에 딸린 것이라 한정사가 필요합니다.
- 더 나은 표현: "Each image comes with its own measurement condition in a `cond.txt` sidecar, which sits in the same image directory."
- 왜: `comes with` 는 "본체에 딸려 오는 부속"이라는 관계를 한 번에 전합니다. 그리고 `sidecar` 는 본 파일 옆에 붙는 메타데이터 파일을 부르는 업계 표준어라, 이 단어 하나로 상대가 구조를 즉시 그립니다 — 실제로 설계 문서에도 `cond.txt 사이드카` 로 그대로 실렸습니다.

### 카드 3 — tool 접속 설명 (접속사·생략)

- 내가 쓴 영어: "As you know the ip address, you can get the images easily since all tools for hitachi. the id is 'hitachi' and password is 'hid'. This is the convension in my company and all know it so it is not confidential."   (출처: transcript:[user] skewnono_v3_nuxt, msr_file 이미지 요청)
- 정정:
  - `As you know the ip address, …` → **`Since you already know the IP address, …`**. 문두 `As` 는 "~하듯이/~할 때"로도 읽혀 이유절이 흐려집니다. 이유임을 확실히 하려면 `Since`. (덧붙여 `As you know,` 는 통째로 "아시다시피"라는 다른 관용구라 더 헷갈립니다.)
  - `since all tools for hitachi` → **`since all the tools are Hitachi machines`**. 동사가 빠졌고, 제조사는 고유명사라 대문자.
  - `the id is 'hitachi' and password is 'hid'` → `the ID is hitachi and **the** password is hid`. 두 번째 명사에도 관사가 필요하고, ID 는 대문자로 씁니다.
  - `convension` → **`convention`**. `all know it` → **`everyone knows it`** (`all` 은 단독 주어로 잘 안 씁니다).
- 더 나은 표현: "Since you already know the IP, fetching the images is straightforward — every tool here is a Hitachi machine, and they all use the same credentials (`hitachi` / `hid`). That's a company-wide convention everyone is aware of, so it isn't confidential."
- 왜: 자격 증명을 공유할 때는 **왜 공유해도 되는지**가 문장의 핵심이라, 그 부분을 마지막 독립 문장으로 떼어 놓는 편이 안전합니다. `a company-wide convention everyone is aware of` 처럼 형용사 하나(`company-wide`)로 범위를 못 박으면 "우리 회사에서는"을 절로 풀어 쓸 필요가 없습니다.

### 카드 4 — 사무실 테스트 결과 보고

- 내가 쓴 영어: "I have just tested in the office, and they are working well in chat mode. the connection with api is no problem."   (출처: transcript:[user] skewnono_v3_nuxt, c5738483)
- 정정:
  - `I have just tested in the office` → **`I just tested it at the office`**. 타동사 test 는 목적어가 필요하고, 근무지로서의 사무실은 `at the office`(`in the office` 는 건물 안이라는 물리적 위치).
  - `they are working well` → **`it works`**. 앞에 복수 선행사가 없어 `they` 가 붕 뜹니다.
  - `the connection with api is no problem` → **`there's no problem with the API connection`**. `X is no problem` 은 "그건 어렵지 않아요"라는 수락 표현이라 뜻이 어긋납니다. 상태를 보고할 때는 `there's no problem with X` 또는 `X is working fine`.
- 더 나은 표현: "I just tested it at the office — chat works, and the API connection is solid."
- 왜: `solid` 는 "끊기지 않고 안정적"을 한 단어로 담아 엔지니어 사이 보고에서 아주 흔합니다. 그리고 `have just tested` 대신 단순과거 `just tested` 를 쓰면 "방금 끝났다"가 더 자연스럽게 들립니다 — 미국식 구어에서는 just 와 단순과거의 결합이 표준입니다.

### 카드 5 — 작업 중단 선언

- 내가 쓴 영어: "good. we stop working on chat now, since we have confirmed the connection."   (출처: transcript:[user] skewnono_v3_nuxt, c5738483)
- 정정: `we stop` → **`let's stop`** 또는 `we'll stop`. 단순현재는 습관이나 확정 일정을 나타내서, 지금 내리는 결정에는 맞지 않습니다.
- 더 나은 표현: "Good — let's put chat on hold now that the connection is confirmed."
- 왜: `now that` 은 `since` 와 뜻이 같지만 **"이제 ~가 됐으니"**라는 시점 전환을 담아, 조건이 방금 충족된 상황에 딱 맞습니다. `put X on hold` 는 폐기가 아니라 보류라 재개 여지를 남기고요 — 실제 의도도 그쪽이었습니다.

### 카드 6 — 설정 확인 질문

- 내가 쓴 영어: "have you set the chat models that can be used in office?"   (출처: transcript:[user] skewnono_v3_nuxt, 7ba6bfc1)
- 정정: `in office` → **`at the office`**. 관사 없는 `in office` 는 "재임 중인"(the president in office)이라는 전혀 다른 뜻입니다.
- 더 나은 표현: "Have you configured the chat models we'll use at the office?"
- 왜: `set` 은 값 하나를 지정할 때, `configure` 는 목록·옵션을 갖춰 놓을 때 씁니다. `that can be used` 를 `we'll use` 로 줄이면 수동태 관계절이 사라져 다섯 단어가 두 단어가 됩니다 — 가능성이 아니라 계획을 묻는 것이므로 뜻도 더 정확해집니다.

### 카드 7 — 파일 수정 요청

- 내가 쓴 영어: "Can you make chat/provider/office_example.py updated? where I can put my api key used in my office? and how can I add model list that is used in my office?"   (출처: transcript:[user] skewnono_v3_nuxt, c5738483)
- 정정:
  - `make X updated` → **`update X`**. `make + 목적어 + 과거분사`는 사역이라 "남을 시켜 ~되게 하다"로 어색해집니다. 동사 하나로 충분합니다.
  - `where I can put …?` → **`Where do I put …?`**. 직접 의문문은 조동사가 주어 앞으로 나갑니다. `Could you tell me where I can put …` 처럼 간접의문문으로 감쌀 때만 원래 어순.
  - `add model list` → **`add a model`** / `add models to the list`. 가산명사 단수 앞에는 관사.
- 더 나은 표현: "Could you update `chat/providers/office_example.py`? Where should I put the API key I use at the office, and how do I add the models we run there?"
- 왜: 질문 두 개를 `and` 로 한 문장에 묶으면 답하는 쪽이 둘 다 답해야 한다는 게 분명해집니다. `should I` 는 `can I` 보다 "권장 위치가 어디냐"에 가깝고, 설정 파일 질문에서는 대개 그쪽을 묻고 있죠.

### 카드 8 — UI 변경 요청

- 내가 쓴 영어: "can you get rid of 라이브 알람 in the nav? only icon is enough (like chat page)"   (출처: transcript:[user] skewnono_v3_nuxt, 65aade15)
- 정정:
  - `only icon is enough` → **`the icon alone is enough`** 또는 `icon-only is enough`. `only` 를 명사 앞에 놓으려면 관사가 앞서야 하고(`the only icon`), 그러면 "유일한 아이콘"이라는 딴 뜻이 됩니다.
  - `like chat page` → **`like the chat page`**.
- 더 나은 표현: "Could you drop the 라이브 알람 label from the nav? Icon-only is enough, the way the chat entry works."
- 왜: 지운 대상이 메뉴 항목 전체가 아니라 **글자**였으니 `the label` 이라고 짚어야 오해가 없습니다. `the way X works` 는 `like X` 보다 무엇을 본뜨라는 건지 분명해서, UI 요청에서 특히 쓸모 있습니다.

### 카드 9 — 짧은 지시 두 건

- 내가 쓴 영어: "untagle it and verify it" / "commit and push to the main"   (출처: transcript:[user] skewnono_v3_nuxt, f604dd4e·7ba6bfc1)
- 정정:
  - `untagle` → **`untangle`** (n 이 빠졌습니다).
  - `push to the main` → **`push to main`**. 브랜치 이름은 고유명사 취급이라 관사를 붙이지 않습니다. `the main branch` 라고 `branch` 를 밝힐 때만 the 가 붙습니다.
- 더 나은 표현: "Untangle the history, then verify it." / "Commit and push to `main`."
- 왜: `it and it` 처럼 대명사가 겹치면 각각이 뭘 가리키는지 흐려집니다. 첫 목적어만 명사로 밝히면(`the history`) 두 번째 `it` 이 자동으로 그 결과를 가리켜 문장이 깔끔해집니다.
