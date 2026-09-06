# 2026-09-07 — 코칭

## 한글→영어

### 카드 1 — 야간 재기동이 낭비인지 묻기   (내가 쓴 한글)
- 내가 쓴 한글: "scheduler에 touch restart.txt로 서버 재부팅을 새벽에 하고 있는데, 매일 하는게 낭비인 것 같은데, 더 좋은 방법 없을까?"   (출처: transcript:[user] skewnono_v3_nuxt)
- 자연스러운 영어: The scheduler restarts the server every night by touching `restart.txt`. Doing that daily feels wasteful — is there a better way?
- 왜 이렇게: 한국어는 "~는데"로 세 마디를 한 문장에 이었지만 영어에서 그대로 이으면(`..., and I think..., so is there...`) 늘어진다. 사실 진술과 의견을 마침표로 끊는 편이 낫다. `touch` 는 파일을 건드려 mtime 만 갱신하는 그 명령이라 번역하지 말고 `by touching restart.txt` 로 수단을 나타내는 by + -ing 에 넣는다. "낭비인 것 같은데"는 `I think it is a waste` 보다 `feels wasteful` 이 자연스럽다 — 근거를 다 대지 않고 감으로 말한다는 신호가 그대로 담긴다. 마지막은 부정 의문(`Isn't there a better way?`)으로 옮기지 않는다. 한국어 "없을까?"는 순한 질문이지만 영어 부정 의문은 "당연히 있을 텐데 왜 안 했냐"로 들린다.

### 카드 2 — 야간 reload 를 옹호하기   (고급 한글 · 번역)
- 한글 원문: "00:05 reload 는 낭비가 아니라 하루 경계에서 프로세스 lru_cache 를 비우는 가장 싼 정합성 장치입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: The 00:05 reload is not waste; it is the cheapest consistency mechanism you have for clearing each process's `lru_cache` at the day boundary.
- 번역 포인트: "A가 아니라 B" 를 `not A but B` 로 직역하면 문어체로 굳는다. 세미콜론으로 끊고 `it is` 로 다시 세우면 반박의 리듬이 산다. "장치"는 device 로 옮기면 물건이 떠오르니 여기서는 `mechanism`. `you have` 를 끼워 넣은 것이 관건인데, 이게 없으면 "세상에서 제일 싸다"는 과한 주장이 되고, 넣으면 "네가 쓸 수 있는 선택지 중에서"로 범위가 좁혀진다. "하루 경계"는 `the day boundary` 가 그대로 통한다(`day rollover` 도 가능).

### 카드 3 — 손댈 곳이 여기가 아니라고 짚기   (고급 한글 · 번역)
- 한글 원문: "워커 4개가 요청 1000개마다 이미 재생성되므로, 하루 한 번의 touch 는 이 시스템에서 가장 드문 재기동 원인입니다. 작은 쪽을 최적화하는 중입니다."   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: The four workers already recycle every 1,000 requests, so a once-a-day touch is the rarest cause of a restart in this system. This is the smaller of the two levers.
- 번역 포인트: uWSGI 워커가 `max-requests` 로 갈리는 것은 영어로 `recycle` 이다 — `regenerate` 나 `re-create` 는 다른 그림을 그린다. "하루 한 번의"는 `a once-a-day touch` 처럼 하이픈으로 묶어 형용사로 만든다. 마지막 문장이 어렵다. 한국어는 주어 없이 지적할 수 있지만 영어는 주어를 세워야 하고, `You are optimizing the smaller half` 로 세우면 손가락질이 된다. 사물을 주어로 돌려 `This is the smaller of the two levers` 로 쓰면 사람 대신 대상이 평가받는다.

### 카드 4 — 대안이 왜 더 나쁜지   (고급 한글 · 번역)
- 한글 원문: "재기동 시점이 메모리에 좌우돼 '하루 경계' 보장이 사라짐 (= 캐시 staleness 복귀)"   (출처: transcript:[assistant] skewnono_v3_nuxt)
- 자연스러운 영어: Restart timing would then hinge on memory, and you lose the day-boundary guarantee — which puts the cache staleness right back.
- 번역 포인트: "~에 좌우되다"는 `depend on` 도 되지만 `hinge on` 이 "그 하나에 전부 매달린다"는 취약함까지 담아 대안을 깎는 문맥에 맞는다. 가정된 대안을 말하고 있으니 `would` 가 필요하다 — 현재형으로 쓰면 지금 그렇다는 뜻이 된다. "보장이 사라짐"은 무생물 주어(`the guarantee disappears`)보다 `you lose the guarantee` 가 영어답다. 잃는 주체를 세우면 손실이 체감된다. 표에 적힌 축약형 `(= ...)` 은 영어 산문에서는 `which puts ... right back` 처럼 관계절로 푸는 편이 자연스럽다.

## 영어 다듬기

### 카드 1 — Codex 에게 감사 결과 넘기기
- 내가 쓴 영어: "ask about these audit list to codex (using herdr skill to open a tab). can we implement the audit result"   (출처: transcript:[user] llm_serving)
- 정정: ① `ask about X to Y` 는 비문이다. ask 는 사람을 바로 목적어로 받는다 — `ask Codex about X`. ② `these audit list` 는 수 불일치. `this audit list` 또는 `these audit items`. ③ `using herdr skill` → `using the herdr skill` (특정 스킬 하나를 가리키므로 the). ④ `the audit result` → `the audit results` (항목 16개라 복수).
- 더 나은 표현: Take this audit list to Codex — open a tab with the herdr skill. Can we act on what it finds?
- 왜: `Take X to Y` 는 "가져가서 물어봐"를 한 동사로 끝낸다. `implement the audit result` 는 "감사 결과를 구현한다"라 어색하다 — 구현하는 것은 결과가 아니라 권고 사항이니 `act on the findings` 나 `apply the recommendations` 로 쓴다. 명령이 둘이면 두 번째는 대시로 붙여 부연으로 낮추는 편이 읽기 좋다.

### 카드 2 — 진행 지시 + 도구 사용 요청
- 내가 쓴 영어: "let's go. if you think it is important to check. ask for the help to the codex via herdr skill. also actively use /simplify and /code-review:code-review"   (출처: transcript:[user] llm_serving)
- 정정: ① `if you think it is important to check.` 는 종속절만 있고 주절이 없다. 마침표 대신 쉼표로 다음 문장에 붙여야 한다. ② `ask for the help to the codex` — `ask Y for help` 가 맞는 틀이고 `the` 도 뺀다: `ask Codex for help`. ③ `via herdr skill` → `via the herdr skill`.
- 더 나은 표현: Go ahead. If you think something needs a second look, ask Codex for help through the herdr skill, and lean on /simplify and /code-review as you go.
- 왜: `let's go` 는 같이 출발하자는 뜻이라 상대에게 맡길 때는 `Go ahead` 가 맞다. `it is important to check` 는 무엇을 확인하는지가 빈다 — `something needs a second look` 이 대상과 정도를 함께 준다. `actively use` 는 문법은 맞지만 딱딱하다. `lean on` 이 "적극적으로 기대어 써라"를 한 구로 담고, `as you go` 가 "끝나고 한 번"이 아니라 "하는 내내"라는 빈도를 정해 준다.

### 카드 3 — 커밋 승인
- 내가 쓴 영어: "good. commit and push"   (출처: transcript:[user] llm_serving)
- 더 나은 표현: Looks good — go ahead and commit and push.
- 왜: 문법 오류는 없다. 다만 `good.` 만 있으면 무엇이 좋은지가 없어 통보처럼 들린다. `Looks good` 은 "내가 보고 판단했다"를 한 단어 더로 담아, 승인 행위가 드러난다. `go ahead and` 는 뜻을 더하지 않고 명령의 각을 깎는 완충구다(구어에서 아주 흔하다). 격식을 올린다면 `The changes look good; please commit and push.`
