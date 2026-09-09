# 2026-09-10 — 오늘의 표현

- **Three lines earn their place.** — 8줄 중 5줄을 지우고 3줄만 남길 때. "필요하다" 대신 "제 몫을 한다" 로 판정하면 근거가 선다.
- **that's expected noise, not a fault** — 빨간 줄이 뜨지만 정상인 상황을 미리 알려줄 때. X-not-Y 구조로 오해를 먼저 지운다.
- **fails in a way that looks like success** — 조용한 실패를 경고하는 정형구. 준비 프로브가 옛 인스턴스에 응답받는 상황처럼.
- **a drift trap** — 지금은 무해한 중복이 나중에 어긋날 구조. 기본값이 코드와 설정에 두 번 선언될 때 쓴다.
- **held hostage by** — 하나가 막혀 나머지 전부가 못 나갈 때. blocked 보다 부당함이 실린다.
- **decay into wrong instructions** — 낡은 docstring 은 그냥 낡는 게 아니라 틀린 지시가 된다. `decay` 가 자동 진행을 담는다.
- **Both resolve on their own.** — 자동사 `resolve` 로 행위자를 지워 "손대지 않아도 풀린다" 를 만든다.

### 오늘의 정독

단락 1은 SIGKILL 을 견디는 프로세스를 두고 `A process surviving SIGKILL isn't defying you` 로 시작한다 — 명사 뒤 현재분사로 관계절을 접고, 의인화를 세운 뒤 곧바로 부정하는 방식. 단락 3의 `ordering beats detection` 은 긴 설명을 세 단어로 봉인하는 `X beats Y` 슬로건 틀이다. → `reading.md`

### 오늘의 코칭

- 한글→영어: "채점자들은 rank-1 이런 의미를 모름. 풀어서 설명" 의 "풀어서" 는 `explain in detail` 이 아니라 `spell out in plain language` — 자세히가 아니라 전문용어를 걷어내라는 뜻.
- 한글→영어(고급): "단일 원본" 은 `single original` 이 아니라 `single source of truth`. 긍정을 뒤집어 `can never drift apart` 로 쓰면 설계가 막아 주는 실패가 드러난다.
- 영어 다듬기: `is necessary?` 는 조동사가 빠진 어순. `Is common.env still pulling its weight?` — `still` 한 단어가 질문에 시간 축을 넣는다.
- 영어 다듬기: `in the github` → `on GitHub`. 플랫폼 위는 `on`, 고유명사라 관사 없음.

→ `coaching.md`

> 처리 항목 18개 / 미뤄진 항목 0개
