# 2026-08-02 — 코칭

## 한글→영어

오늘 배치에는 내가 한국어로 쓴 메시지도, `spool/` 노트도 없었다. 그래서 아래 두 장은
`[assistant]` 메시지가 인용한 한국어 문서 문장을 옮겨 본 번역 정독 카드다.

### 카드 1 — 남은 숙제를 밝히며 문서를 닫기   (고급 한글 · 번역)
- 한글 원문: "스케줄러 자체는 아직 없습니다."   (출처: transcript:[assistant] — 인용된 `docs/datatables/device_statistics_weekly_trend.txt`)
- 자연스러운 영어: The scheduler itself does not exist yet. / What's still missing is the scheduler itself.
- 번역 포인트: "자체는"이 대조 강조라 `itself`가 그대로 대응한다. 다만 문서를 닫는 마지막 줄이라면 `What's still missing is …` 쪽이 낫다. 영어는 문장 끝에 무게를 싣기 때문에, 빠진 것을 문미로 보내면 그게 다음 작업 항목이라는 신호가 된다. `아직`을 `still`로 옮길지 `yet`으로 옮길지는 위치가 정한다 — `not … yet`은 부정문에, `still missing`은 긍정 형태에 붙는다.

### 카드 2 — 없는 데이터를 응답에서 다루는 규칙   (고급 한글 · 번역)
- 한글 원문: "스냅샷이 없는 과거 주차는 키 자체를 응답에서 뺍니다."   (출처: transcript:[assistant] — 인용된 datatable 문서)
- 자연스러운 영어: Past weeks with no snapshot are omitted from the response entirely — the key is not returned at all.
- 번역 포인트: 한국어는 "키 자체를 뺍니다"로 능동이지만 API 규격을 적을 때 영어는 수동(`are omitted`)이 자연스럽다. 규격은 서버가 무엇을 하느냐가 아니라 응답이 어떤 모양이냐를 규정해서다. "자체를"이 여기서는 강조라 `entirely`나 `at all`로 옮긴다. `omit`을 골랐다는 점도 중요하다 — `exclude`는 걸러 냈다는 뜻이고 `omit`은 애초에 넣지 않았다는 뜻이라, "빈 값으로라도 키가 오지 않는다"는 계약을 정확히 전달한다.

## 영어 다듬기

### 카드 1 — 스케줄러 작업 지시
- 내가 쓴 영어: "flask_module is widely used in my projects of my own since it is built to use my company's system and fab tools. As we need to setup the scheduler to be attached to the flask server, benchmark the api folder where scheduler code (scheduler, extension, redis) to built the scheduler here. the main purpose of having scheduler is to remove old data of image_cache and pre-computing the device-statistics."   (출처: transcript:[user])
- 정정:
  - `my projects of my own` → `my own projects`. `of my own`은 명사 뒤에 붙어 소유를 강조하는 형태(`a room of my own`)라 `my`와 겹치면 중복이 된다.
  - `setup` → `set up`. 명사·형용사는 `setup`, 동사는 두 단어다.
  - `to built` → `to build`. `to` 뒤는 항상 원형이다.
  - `to remove old data … and pre-computing …` → `to remove … and pre-compute …`. `to` 하나가 두 동사를 이끌 때 형태를 맞춰야 한다.
  - `the main purpose of having scheduler` → `of having a scheduler`. 가산명사 단수에는 관사가 필요하다.
- 더 나은 표현: `flask_module` is used across my own projects because it's built around my company's systems and fab tools. Since the scheduler needs to attach to the Flask server, use the `api` folder — its scheduler, extension, and redis modules — as the benchmark for building one here. The scheduler exists to purge stale `image_cache` data and pre-compute device statistics.
- 왜: `widely used in my projects` 는 규모를 말하는 표현이라 개인 프로젝트에는 크다. `across my own projects` 가 "여러 곳에서 쓴다"를 과장 없이 전달한다. 목적을 말할 때 `The main purpose of having X is to …` 는 관사와 전치사가 줄줄이 붙는데, `X exists to …` 로 줄이면 같은 뜻이 절반 길이가 된다. 지시문에서는 자주 쓰이는 형태다. `old data` 는 `stale` 하나로 바꾸면 "오래됐고 이제 쓸모없다"까지 담긴다.

### 카드 2 — 설정 변경이 필요한지 되묻기
- 내가 쓴 영어: "yes. and no need to setup in uwsi.ini?"   (출처: transcript:[user])
- 정정: `setup` → `set up` (동사), `uwsi.ini` → `wsgi.ini` (오타).
- 더 나은 표현: (문어) Understood. And nothing needs to be set up in `wsgi.ini`? / (구어) Got it. So we don't need to touch `wsgi.ini`?
- 왜: `no need to …?` 는 질문으로는 형태가 덜 갖춰져 있다. `nothing needs to be …?` 로 주어를 세우면 확인 질문이 되고, 구어라면 `So we don't need to …?` 가 더 자연스럽다. `So` 로 시작하는 질문은 앞 설명에서 추론한 결론을 확인하는 자리에 잘 맞는다. 여기서 `touch` 는 "수정하다"의 가벼운 관용 표현이라 설정 파일과 특히 잘 붙는다.

### 카드 3 — 한산한 시간대를 알려 주기
- 내가 쓴 영어: "The time between 1 and 8 am is quite time so that we can do scheduled tasks without worrying about the resources."   (출처: transcript:[user])
- 정정:
  - `quite time` → `quiet time`. 철자 하나 차이지만 뜻이 완전히 다르다(`quite` = 꽤).
  - `the resources` → `resources`. 특정 자원을 가리키는 게 아니라 일반 개념이라 무관사 복수다.
  - `so that we can` 은 문법상 맞지만 여기서는 목적이 아니라 결과다. `so` 만으로 충분하다.
- 더 나은 표현: 1–8 AM is our quiet window, so scheduled jobs can run there without competing for resources.
- 왜: `quiet window` 는 운영 쪽에서 굳은 표현이라 `quiet time` 보다 정확하다 — 작업을 넣을 수 있는 *구간*이라는 뜻이 들어 있다. `do scheduled tasks` 는 어색한 결합이고, 작업은 `run` 한다. `without worrying about the resources` 는 걱정하는 주체가 사람이라 초점이 흐려지는데, `without competing for resources` 로 바꾸면 실제로 일어나는 일(자원 경합)을 가리킨다. 시간을 `1–8 AM` 로 쓰면 `The time between 1 and 8 am` 보다 한결 간결하다.

### 카드 4 — 결정 세 가지를 한 번에 승인하기
- 내가 쓴 영어: "touch data.py if needed. retention 12 weeks good but I can change later on if needed."   (출처: transcript:[user])
- 정정: `retention 12 weeks good` 에는 동사가 없다 → `12 weeks of retention is good`. 그리고 한 문장에 `if needed` 가 두 번 나온다.
- 더 나은 표현: Touch `data.py` if you need to. Twelve weeks of retention is fine for now — I may tune it later.
- 왜: 짧은 승인 메시지는 이대로도 통하지만, `if needed` 반복이 두 승인을 같은 무게로 만들어 버린다. 두 번째를 `for now` + `I may tune it later` 로 풀면 "지금은 승인, 나중에 조정 가능"이라는 다른 뜻이 살아난다. 실제로 이 구분이 설계에 반영됐다 — 나중에 바꿀 값이므로 상수가 아니라 환경 변수여야 한다는 결론이 여기서 나왔다. `change` 대신 `tune` 을 쓰면 "고치는 것"이 아니라 "조정하는 것"임이 분명해진다.

### 카드 5 — 유형이 닫혔는지 되묻기
- 내가 쓴 영어: "The bug class here is one pool serving two masters. Is that fixed?"   (출처: transcript:[user])
- 정정: 없음.
- 더 나은 표현: You framed the bug class as one pool serving two masters — is the class itself closed, or just this instance?
- 왜: 원문도 정확하고 짧다. 다만 `Is that fixed?` 의 `that` 이 무엇을 가리키는지 모호하다 — 유형인지 개별 버그인지. 두 선택지를 `or` 로 나란히 제시하면 답하는 쪽이 얼버무릴 수 없게 된다. 실제로 이 질문이 "인스턴스는 고쳤고 유형은 열려 있다"는 답을 끌어냈다. `You framed X as …` 는 상대가 쓴 표현을 되받아 논의의 출발점으로 삼는 문형으로, 리뷰에서 유용하다.
