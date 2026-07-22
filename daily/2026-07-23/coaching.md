# 2026-07-23 — 코칭

## 한글→영어

### 카드 1 — 초회 조회와 폴링 주기 (내가 쓴 한글)

- 내가 쓴 한글: "맞아. 초회 10분(긴 시간이 의미가 없음) 으로 하고 이후 1분으로 조회 (매 10~20초마다 요청). 누적되는 정보는 자연스럽게 제거하면서 신규 정보만 계속해서 화면에 뿌려주기."   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "Right. Make the first fetch a 10-minute window — anything longer isn't useful — then poll a 1-minute window every 10–20 seconds. Old events should age out on their own, and only the new ones keep landing on screen."
- 왜 이렇게: "초회"는 `the first fetch` 나 `the initial load`. "긴 시간이 의미가 없음"처럼 주어가 빠진 한국어는 영어로 옮길 때 주어를 세워야 하는데, 여기서는 `anything longer` 를 주어로 삼으면 원문의 무주어 감각이 그대로 살아납니다. "자연스럽게 제거"는 `remove automatically` 보다 **`age out`** 이 정확합니다 — 시간이 지나 스스로 밀려난다는 뜻이라, 누가 지우는 게 아니라는 원문의 뉘앙스가 들어 있습니다. "뿌려주다"는 `spray` 같은 직역을 피하고 `land on screen` 이나 `show up`.

### 카드 2 — 팬아웃을 짚는 질문 (내가 쓴 한글)

- 내가 쓴 한글: "15초 고정으로 하고, 탭 복귀 시 5분으로 재조회 괜찮아. 사용자마다 각자 요청하는 개념을 너는 생각 중이야?"   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "Let's fix it at 15 seconds, and re-fetching a 5-minute window when the tab comes back is fine. One thing though — are you assuming each viewer polls the API on their own?"
- 왜 이렇게: "고정으로 하다"는 `fix it at 15 seconds` / `keep it fixed at`. "탭 복귀 시"는 `when the tab comes back` 이 가장 짧고, 격식을 올리면 `on tab focus`. 마지막 문장이 이 카드의 핵심입니다. "~하는 개념을 생각 중이야?"를 직역하면(`Are you thinking about the concept that...`) 뜻이 뭉개집니다. 실제로 묻는 건 **상대 설계의 숨은 전제**라서 `Are you assuming ...?` 가 맞습니다. 앞에 `One thing though —` 를 붙이면 동의(앞 두 항목)와 반문(뒤)이 부드럽게 갈립니다.

### 카드 3 — Redis 제안 (내가 쓴 한글)

- 내가 쓴 한글: "그러면 redis에 정보를 저장하고 넘겨주는게 api 요청 낭비를 방지하는 법이 아닐까?"   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "Then wouldn't caching it in Redis and serving from there keep us from burning API calls?"
- 왜 이렇게: 한국어의 "~아닐까?"와 영어의 `Wouldn't ...?` 는 기능이 정확히 같습니다 — 확신을 낮춰 제안을 얹는 자리. 그래서 부정 의문문을 그대로 살리는 게 옳습니다(`Isn't it better to...`는 조금 더 단정적). "낭비를 방지하다"는 `prevent waste` 보다 `keep us from burning API calls` 가 개발 맥락에서 훨씬 흔합니다. burn 은 한정된 예산을 태워 없앤다는 그림이라 "요청 낭비"의 뉘앙스와 맞습니다. "저장하고 넘겨주다"는 두 동사를 그대로 옮기지 말고 `cache ... and serve from there` 로 묶습니다.

### 카드 4 — API 예산과 쓰기 권한 (내가 쓴 한글)

- 내가 쓴 한글: "사내 알람 api를 너무 많이 요청할 수는 없어. 쓰기 권한 있어. 필요하면 별도 스케쥴러 (skewnono가 아닌 다른 서버)에서 redis에 write를 하고, skewnono에서는 read만 해서 제공하는 방법도 가능해."   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "We can't hammer the internal alarm API. And yes, we do have write access. If it helps, a separate scheduler — a different server, not SKEWNONO — could write to Redis, and SKEWNONO would only read from it and serve."
- 왜 이렇게: "너무 많이 요청하다"를 한 단어로 줄이면 **`hammer`** 입니다(격식 있게는 `we have a limited call budget for that API`). "쓰기 권한 있어"는 앞의 제약과 대비되는 좋은 소식이라, `we do have` 로 do 강조를 넣으면 그 반전이 들립니다 — 한국어에서 억양으로 처리하는 몫을 영어는 do 가 가져갑니다. "~하는 방법도 가능해"를 `it is also possible to...` 로 옮기면 전형적인 번역투입니다. 조동사 `could` 하나가 "가능하다"를 이미 다 담습니다.

### 카드 5 — 데몬 상주 루프 (내가 쓴 한글)

- 내가 쓴 한글: "wsgi 서버로 구동되는 flask에 deamon으로 상주 루프를 함께 돌려도 문제가 없어?"   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "Is it safe to run a long-lived loop as a daemon thread inside a Flask app that's served by uWSGI?"
- 왜 이렇게: "문제가 없어?"를 `Is there any problem with ...?` 로 옮기면 문법은 맞아도 어색합니다. 위험을 묻는 자리에서 원어민은 `Is it safe to ...?` 또는 `Is that a problem?` 을 씁니다. "상주 루프"는 `resident loop` 가 아니라 `a long-lived loop` / `a background loop`. "wsgi 서버로 구동되는"은 관계절 `that's served by uWSGI` 로 뒤에 붙이거나 분사구 `running under uWSGI` 로 줄입니다 — 영어는 이런 수식을 명사 뒤로 보내는 쪽이 읽기 편합니다. (철자: deamon → **daemon**)

### 카드 6 — 스케줄러 환경 답변 (내가 쓴 한글)

- 내가 쓴 한글: "cron 방식이야. 다른 flask에서 apscheduler로 돌리고 있거든."   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "It's cron-based — we already run those jobs with APScheduler in another Flask app."
- 왜 이렇게: "~거든"은 앞말의 근거를 슬쩍 덧붙이는 어미라, 영어에서는 대시(—)나 `since` 로 이어 붙이면 같은 결이 납니다. `because` 로 받으면 인과를 정면으로 주장하게 되어 원문보다 무거워집니다. "다른 flask에서"는 `in another Flask` 가 아니라 `in another Flask app` — Flask 는 프레임워크 이름이라 app 을 붙여야 인스턴스를 가리킵니다.

### 카드 7 — 관측자의 안정성 (고급 한글 · 번역)

- 한글 원문: "관측하는 쪽이 관측당하는 쪽보다 더 안정적이어야 합니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "The thing doing the watching has to be more reliable than the thing being watched."
- 번역 포인트: 한국어가 능동("관측하는")과 피동("관측당하는")의 대구로 뜻을 세웠으니, 영어도 대구를 유지해야 합니다 — 현재분사 `doing the watching` 과 과거분사 `being watched` 가 그 자리입니다. 한쪽만 명사로 바꾸면(`the monitor` vs `the thing being watched`) 균형이 깨집니다. 격식을 올리려면 `The observer must be more available than the observed.` 처럼 명사화할 수 있지만, 설계 문서에서는 풀어 쓴 쪽이 오히려 잘 읽힙니다.

### 카드 8 — 침묵의 검증 (고급 한글 · 번역)

- 한글 원문: "모니터링 화면에서 '조용하다'는 신호는 그 자체로 검증돼야 합니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "On a monitoring screen, silence is a claim that has to be verified, not a signal you can take at face value."
- 번역 포인트: "그 자체로 검증돼야 한다"를 `must be verified in itself` 로 직역하면 무슨 말인지 흐려집니다. 원문의 논지는 "조용함은 사실이 아니라 **주장**"이라는 것이므로, `silence is a claim` 으로 은유를 먼저 세우고 관계절로 검증 요구를 답니다. 뒤에 `not a signal you can take at face value`(액면 그대로 받아들일 신호가 아니다)를 붙여 대비를 만들면, 한국어의 "그 자체로"가 겨냥한 반대편이 드러납니다.

### 카드 9 — 자초한 문제 (고급 한글 · 번역)

- 한글 원문: "하지만 그건 스스로 만든 문제를 분산 락으로 푸는 것입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt 745b34a7)
- 자연스러운 영어: "But that's reaching for a distributed lock to solve a problem you created yourself."
- 번역 포인트: "~푸는 것입니다"라는 형식명사 종결은 영어에서 동명사구가 받습니다. 다만 `solving` 을 그대로 쓰면 사실 진술이 되어 날이 무뎌집니다. **`reach for`** 는 "굳이 그것까지 꺼내 든다"는 과잉의 뉘앙스를 담고 있어, 원문의 비판적 어조를 살립니다. "스스로 만든"은 `self-inflicted`(격식·강함)와 `you created yourself`(구어·부드러움) 중 상대를 탓하지 않으려면 후자.

## 영어 다듬기

### 카드 1 — 죽은 코드 정리 요청

- 내가 쓴 영어: "can you remove dead code and files in @back_dev_home/ebeam/hitachi/hardware/providers/? office_example.py is seen in hardware folder. and give me the office_example for fdc. I depicted the doc's mapping of fdc in os."   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `I depicted the doc's mapping` — depict 은 그림이나 글로 **묘사하다**라는 뜻이라, 문서에 적어 두었다는 의미가 되지 않습니다. `I've written up` / `I've documented` 로. 그리고 `in hardware folder` 는 관사 누락 — 특정 폴더이므로 `in the hardware folder`.
- 더 나은 표현: "Could you clean up the dead code and unused files under `.../hardware/providers/`? I see an `office_example.py` sitting in the hardware folder itself. Also, could you write the `office_example` for FDC? I've documented the FDC mapping in `docs/`."
- 왜: `remove dead code` 도 통하지만 `clean up` 이 삭제와 정돈을 함께 가리켜 실제 요청 범위에 더 맞습니다. `X is seen in Y` 는 수동태라 본 사람이 지워지는데, 여기서는 본인이 발견한 것이므로 `I see X sitting in Y` 가 자연스럽고 sitting 이 "제자리가 아닌 곳에 놓여 있다"는 뉘앙스까지 얹어 줍니다.

### 카드 2 — 파일 이름 판단

- 내가 쓴 영어: "provide/bsm/mock.py is consistent given other tabs"   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `consistent given other tabs` — given 은 "~를 감안하면"이라 비교 대상을 받지 못합니다. 일관성의 상대는 전치사 with 로 연결합니다: `consistent with the other tabs`. (오타: provide → providers)
- 더 나은 표현: "`providers/bsm/mock.py` is consistent with the other tabs — leave that one as is."
- 왜: 원문은 판단만 있고 지시가 없어 상대가 의도를 추론해야 합니다. 대시로 결론 한 마디(`leave that one as is`)를 붙이면 근거와 지시가 한 문장에 들어갑니다. 짧은 지시일수록 이 구조가 효율적입니다.

### 카드 3 — .env 처리 질문

- 내가 쓴 영어: "perhaps should I set the uncommented the office in .env file? I want you to move up those that can be now set as \"office\""   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `should I set the uncommented the office` — 동사가 둘(set/uncomment) 겹치고 목적어가 없습니다. `Should I uncomment the office lines in `.env`?` 로 하나만 남깁니다. `that can be now set` — now 같은 시점 부사는 조동사와 be 사이가 아니라 `can now be set` 순서입니다.
- 더 나은 표현: "Should I go ahead and uncomment the office lines in `.env`? And could you promote the ones that can now be switched to `office`?"
- 왜: `move up` 은 물리적으로 위로 올린다는 뜻이라 등급 상향에는 잘 쓰이지 않습니다. 상태를 한 단계 올리는 것은 **`promote`** 가 정확한 동사입니다(promote a feature to office). `go ahead and ~` 는 "그냥 ~해버릴까?"에 해당하는 구어로, 허락을 구하는 질문을 가볍게 만듭니다.

### 카드 4 — 테스트용 기본 장비

- 내가 쓴 영어: "for the test, the basic tool is \"MCD018\" or \"MCD320\" if you want. when we do test in the __main__."   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `the basic tool` — basic 은 "기초적인"이라 기본값이라는 뜻이 없습니다. 기본값은 `the default`. `when we do test in the __main__` — do test 는 강조 용법이 아니면 비문이고(`run the test`), `__main__` 앞의 the 도 불필요합니다.
- 더 나은 표현: "For the smoke test in `__main__`, use `MCD018` as the default tool — `MCD320` works too if you'd rather."
- 왜: 두 문장이 같은 것을 말하고 있어 한 문장으로 합치는 편이 읽기 쉽습니다. `if you want` 은 결정권을 상대에게 넘기는 말인데 여기서는 대안 제시라 `if you'd rather`(굳이 다른 걸 쓰고 싶으면)가 더 맞습니다.

### 카드 5 — 탭 단계별 확인

- 내가 쓴 영어: "I want to check step by step for the tabs in the hardware, if necessary, we can separate the .env.example and .env for hardware with subtask."   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `check step by step for the tabs` — check 의 목적어를 for 로 연결하지 않습니다. `check the tabs one by one` 또는 `go through the tabs one at a time`. `with subtask` 는 관사도 없고 뜻도 모호합니다 — `as a separate subtask`. 그리고 콤마로 두 문장을 이어 붙인 comma splice 라 마침표로 끊어야 합니다.
- 더 나은 표현: "I'd like to verify the hardware tabs one at a time. If that needs it, we can split `.env` and `.env.example` per tab as a separate subtask."
- 왜: `step by step` 은 정해진 절차를 순서대로 밟는다는 뜻이고, 여기서 말하려는 건 "한 번에 하나씩"이라 **`one at a time`** 이 정확합니다. 둘의 차이가 은근히 큽니다 — 전자는 순서가, 후자는 동시성 억제가 초점입니다.

### 카드 6 — 폴백 제안

- 내가 쓴 영어: "just simply let's make skewnono_hardware_provider=office and check if office.py exists or not for each subpath. if no existant, fall back to mock.py. is it easier?"   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 정정: `if no existant` — existant 는 없는 단어이고(형용사는 existent), 여기서는 절이 필요합니다: `if it isn't there` / `if it's missing`. `just simply` 는 뜻이 겹치므로 하나만 씁니다. `exists or not` 의 or not 도 간접의문문에서는 군더더기입니다.
- 더 나은 표현: "Let's just set `SKEWNONO_HARDWARE_PROVIDER=office` and have the dispatcher check whether each subpath has an `office.py`, falling back to `mock.py` when it doesn't. Wouldn't that be simpler?"
- 왜: `is it easier?` 는 "(이미 나온 안들 중) 그게 더 쉬운가?"로 들려 판단을 상대에게 완전히 넘깁니다. 자기 제안을 밀어 보는 자리에서는 `Wouldn't that be simpler?` 가 자연스럽고, 부정 의문문이라 반박 여지도 남깁니다. 마지막 조건은 분사구문(`falling back to ... when it doesn't`)으로 붙이면 조건과 결과가 한 호흡에 들어갑니다.

### 카드 7 — 라이브 알람 페이지 제안

- 내가 쓴 영어: "here we have automated align fail handling system, which is activated when align fail alarm code happens in the alarm system (using api). I want to exempt this alarm (tell you the align fail occurs) and apply in this skewnono application. ... I can send api every 10 or 20 seconds to get the info and tell the info to the users who are in the page."   (출처: transcript:[user] skewnono_v3_nuxt 745b34a7)
- 정정: 네 군데입니다. ① `we have automated ... system` — 셀 수 있는 단수 명사에 관사 누락(`an automated align-fail handling system`). ② `I want to exempt this alarm` — **exempt 는 "면제하다"라 정반대 뜻**이 됩니다. 의도한 "빼내 오다"는 `tap into` 또는 `pull this alarm out`. ③ `apply in this application` — apply 는 대상을 to 로 받습니다(`apply it to SKEWNONO`). ④ `send api` — API 는 보내는 게 아니라 호출하는 것(`call the API`), 그리고 `users who are in the page` 는 `on the page`(면 위 = on).
- 더 나은 표현: "We already have an automated align-fail handler here: it kicks in when an align-fail alarm code shows up in the alarm system, which it reads over an API. I'd like to tap into that same alarm and surface it in SKEWNONO — a page that continuously broadcasts align failures and measurement failures by alarm code. I could call the API every 10–20 seconds and push what comes back to whoever has the page open. Does that sound reasonable, and what would you build it with?"
- 왜: 원문은 사실 나열이 길어 정작 요구가 묻힙니다. **이미 있는 것 → 하고 싶은 것 → 방법 → 질문** 순으로 끊으면 상대가 답할 지점이 분명해집니다. `kick in`(자동으로 발동하다), `tap into`(기존 흐름에서 빼 쓰다), `surface`(사용자에게 드러내다)는 이런 요청에서 계속 재활용할 동사 셋입니다. 마지막의 `what specs can we use?` 도 spec 이 "사양서"를 뜻해 오해를 부르니, 묻고 싶은 게 기술 선택이라면 `what would you build it with?` 가 정확합니다.

### 카드 8 — 디바이스 칩 스크롤 요청

- 내가 쓴 영어: "in Align Fail and MEas Fail page, in the 디바이스 선택 component, sometimes you need more space to display device code. can you make it scrollable? currently notation at the end with like +number. but can't see them."   (출처: transcript:[user] skewnono_v3_nuxt 6ead3117)
- 정정: `currently notation at the end with like +number. but can't see them.` — 동사가 없는 조각 문장 둘입니다. `Right now the overflow collapses into a +N counter, and I can't see what's hidden.` 로 주어와 동사를 세웁니다. `in ... page` 는 페이지가 둘이니 복수이고 전치사도 on 입니다: `on the Align Fail and Meas Fail pages`.
- 더 나은 표현: "On the Align Fail and Meas Fail pages, the 디바이스 선택 component sometimes runs out of room for the device codes. Right now the overflow collapses into a `+N` counter and there's no way to see what's hidden — could you make the strip scrollable instead?"
- 왜: `you need more space` 의 you 는 막연한 일반 주어라 누구에게 공간이 부족한지 흐려집니다. 주체를 컴포넌트로 옮겨 `runs out of room` 으로 쓰면 문제 자체를 가리키게 됩니다. 요청은 증상 설명 뒤 맨 끝에 두는 편이 설득력이 큽니다 — 근거가 먼저 서기 때문입니다.

### 카드 9 — 남은 일 확인

- 내가 쓴 영어: "something to commit and push?"   (출처: transcript:[user] skewnono_v3_nuxt d4c08a6a)
- 더 나은 표현: "Anything left to commit and push?"
- 왜: 문법 오류는 없습니다 — 주어와 동사를 생략한 구어체 축약이라 그대로도 통합니다. 다만 이런 확인 질문에서는 something 보다 **anything** 이 맞습니다. something 은 있을 것이라 기대할 때, anything 은 있는지 없는지를 물을 때 씁니다. `left` 한 단어를 넣으면 "아직 남은 게 있냐"는 뜻이 분명해집니다.
