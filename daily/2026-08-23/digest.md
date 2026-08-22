# 2026-08-23 — 오늘의 표현

리뷰에서 지적을 받아치고 안 고친 것을 스스로 밝히는 말이 오늘의 축이다. oc-review 기록
두 편이 통째로 영어 산문이라, 배치 전체가 "이 지적은 왜 유효한가/왜 무효인가" 로 채워졌다.

- **Existing drift elsewhere doesn't authorize a new instance.** — 다른 데 이미 어긋난 게 있다고 해서 하나 더 만들 권한이 생기진 않는다. 선례를 `authorize`(허가)라는 법률 어휘로 받아 놓고, 그건 허가가 아니라 부채라고 뒤집는다.
- **it's preservation, not invention** — 새로 만든 게 아니라 있던 걸 보존한 것. 상대가 씌운 "지어냈다" 프레임을 반대말 한 단어로 되돌리는, 두 명사짜리 반박.
- **the docstring describes the old bug as the new behavior** — docstring 이 옛 버그를 새 동작이라고 설명하고 있다. "문서가 낡았다" 를 `describe A as B` 로 바꾸면, 버그가 사양으로 승격돼 다음 사람이 복원할 위험까지 함께 지목된다.
- **the fix is at the right altitude** — 수정이 알맞은 추상 층위에 있다. `altitude` 는 고도 은유라, 호출부 땜질(too low)과 과잉 추상(too high)을 한 단어로 가른다.
- **two sites I deliberately left alone** — 일부러 손대지 않은 두 곳. `deliberately` 하나가 누락과 판단을 가른다 — 빼면 그냥 빠뜨린 것으로 읽힌다.
- **I want evidence before making that trade.** — 그 맞바꿈은 근거를 보고 하겠다. 거절이 아니라 조건부 동의라, 상대가 근거를 가져오면 진행된다는 문이 열려 있다.
- **fetch a file it never checked existed** — 존재 확인을 한 적 없는 파일을 가져오게 시켰다. `never` 가 "이름을 잘못 만들었다" 를 "검증 단계가 통째로 없었다" 로 재정의한다.

전체 16개는 `new-expressions.md`.

### 오늘의 정독

단락 1은 칭찬과 지적을 문장 **형태**로 갈라 놓는다 — 세미콜론으로 네 항목을 매단 긴 칭찬
문장 뒤에 `MIGRATION.md not updated.` 라는 동사 없는 조각이 뚝 떨어진다. 리듬이 바뀌는
자리가 곧 태도가 바뀌는 자리다. → `reading.md`

### 오늘의 코칭

- **한글→영어**: "결과는 나오는데 너무 오래걸린다" 는 한 문장에 다 담지 말고 `a search does come back with results — it just takes far too long.` 으로 끊는다. 강조의 `does` 가 "안 되는 게 아니라" 를 한 단어로 실어 준다.
- **한글→영어**: "무조건 이득인가?" 는 `always a win` 이고, 뒤에 `or are there cases where it isn't` 를 붙여야 상대가 "네" 로 뭉개고 넘어가지 못한다.
- **영어 다듬기**: `re-start where it stops` 는 뜻이 반대다(처음부터 다시). 이어받기는 `resume from where it left off` 가 정착된 관용구이고, `binary check` 는 `checksum` 이라고 해야 통한다.
- **영어 다듬기**: `in the production mode` → `in production`. 환경을 가리킬 때는 무관사 관용구이고, `mode` 는 앱의 동작 모드일 때만 쓴다.

→ `coaching.md`

> 처리 항목 14개 / 미뤄진 항목 1313개
