# 2026-09-06 — 오늘의 표현

- **it does not get a fresh one** — 새로 붙는 컴포넌트가 자기 몫의 예산을 따로 받는 게 아니라 기존 예산을 나눠 쓴다고 못박는 말. 앞에 `borrows from that same budget` 을 깔고 대시 뒤에 붙이면 흔한 오해가 한 문장에 닫힌다.
- **at the ... cliff** — 임계값을 넘으면 완만히 나빠지는 게 아니라 뚝 떨어진다. `limit` 은 선만 그리고 `cliff` 는 넘었을 때 무슨 일이 나는지까지 그린다.
- **mid-request** — 요청을 처리하는 도중에. `mid-` 는 하이픈 하나로 부사구를 만든다(mid-flight, mid-migration).
- **if X changes materially** — 사정이 실질적으로 달라지면. `materially` 가 "사소한 변동으로 결정을 다시 뒤집지는 말라" 는 방어선을 같이 친다.
- **do not "optimize" X back up** — 되돌릴 게 뻔한 설정에 미리 못을 박는 말. 따옴표가 "본인은 최적화라 믿겠지만 아니다" 를 비꼬지 않고 전달한다.
- **best treated as X, not a mandatory part of Y** — 쓰되 필수 구성에서는 빼자는 권고. `we recommend` 없이 권고를 담는 수동태 정형구다.
- **field report** — 논문 수치가 아니라 실제로 굴려 본 사람의 후기. "없다" 를 근거로 "그래서 직접 재야 한다" 로 넘어가는 논증의 축.

### 오늘의 정독
`reading.md` 단락 1 — FTP 프록시의 메모리 예산을 설명하는 ADR 의 Context 절이다. 다섯 문장이 전부 현재시제인 이유와, 분사구문(`failing ... and disrupting ...`)으로 인과 사슬을 한 사건처럼 묶는 방식을 짚었다. 단락 2는 같은 문서의 Consequences 절인데 조동사와 세미콜론이 문장을 끌고 가는 대비가 보인다.

### 오늘의 코칭
- 한글→영어: "flask proxy와 동시에 이 구성이 가능한가?" 의 핵심어는 `at the same time` 이 아니라 **`coexist`** 다 — "둘 다 살아 있을 수 있나" 를 담는다. (카드 4)
- 한글→영어: "폐기." 한 마디는 격식에 따라 `decommission`(절차대로) / `retire`(중립) / `drop`(구어) 셋으로 갈린다. (카드 10)
- 영어 다듬기: "can we scan to fix to meet pylance format rule?" → **"Can we sweep the codebase and fix whatever Pylance flags?"** — 정적 분석의 지적을 받는 동사는 `flag` 다. (카드 6)
- 영어 다듬기: `explain about X` 는 비표준 — explain 은 타동사라 목적어를 바로 받는다. (카드 5)

전체는 `coaching.md`.

> 처리 항목 28개 / 미뤄진 항목 925개
