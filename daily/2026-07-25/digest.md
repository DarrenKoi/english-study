# 2026-07-25 — 오늘의 표현

- **have a shelf life** — 유통기한이 있다. 지금 맞는 주석·측정치도 언젠가 상한다고 완곡하게 경고할 때. `tied to ~` 를 붙이면 수명이 무엇에 묶였는지까지 담깁니다.
- **a false green** — 가짜 통과. 실패해야 마땅한데 초록불이 뜬 테스트. 결과가 흔들리는 flaky 와 달리 일관되게 틀린 답을 준다는 점에서 더 나쁩니다.
- **nothing announces it** — 아무것도 알려 주지 않는다. `no warning is printed` 같은 수동태보다 짧고 세서, 최악의 실패를 규정하는 `because` 절에 잘 붙습니다.
- **what breaks the tie** — 승부를 가르는 것은. 두 후보를 이미 늘어놓은 뒤 결정적 근거 하나만 문장 앞으로 끌어올리는 유사분열문.
- **under-powered (a test)** — 검출력이 부족한. 통계 어휘를 빌려 "전제가 틀린 게 아니라 표본이 약하다"를 가릅니다. 테스트를 고치라는 뜻이지 설계를 뒤집으라는 뜻이 아닙니다.
- **promote X to blocking** — 경고를 차단 수준으로 승격하다. `advisory` ↔ `blocking` 한 쌍이면 CI·배포 게이트의 심각도 설계를 영어로 그대로 말할 수 있습니다.
- **at your expense** — 당신 비용을 축내면서. 중단 선언에 붙이면 게을러서가 아니라 상대를 아껴서 멈춘다는 뜻이 됩니다. `at the expense of X`(X를 희생해서)와 구분하세요.

→ 전체 16개는 [new-expressions.md](new-expressions.md)

### 오늘의 정독

배포 설계 문서의 "이건 실현 가능성 배포다" 단락을 골랐습니다. `A bundle that boots … is a success` / `A bundle that refuses to start is the only real failure` 로 관계절 두 개를 대구로 세워, 성공의 정의만으로 나머지 검사의 심각도를 전부 결정해 버리는 구조입니다. `the only` 하나가 나머지를 advisory 로 밀어내는 대목을 눈여겨보세요.

→ [reading.md](reading.md) (단락 3개 — 나머지 둘은 대시로 감싼 비제한적 관계절, 그리고 "못 한다"를 변명처럼 들리지 않게 쓰는 수동태·부정 주어)

### 오늘의 코칭

- **영어 다듬기 카드 1** — `run the skill /back-to-office` 는 어순이 뒤집혔습니다(`the /back-to-office skill`). 더 중요한 건 `the jobs that we haven't done yet` 이 사무실 네트워크가 필요한 일까지 포함해, 달성 불가능한 조건이 되어 훅이 아홉 번 반복됐다는 점.
- **영어 다듬기 카드 2** — `changes since 88a5aee` 를 `everything that landed since 88a5aee` 로. `land` 는 "머지되어 실제로 들어갔다"라 작업 중인 변경과 갈라 줍니다.

→ [coaching.md](coaching.md)

> 처리 항목 18개 / 미뤄진 항목 0개 (문서 7건 + 트랜스크립트 11건. 이 중 트랜스크립트 10건은 `/clear` 뿐이라 추출 대상이 없었고, 한국어로 쓴 문장이 배치 전체에 없어 한글→영어 카드는 만들지 않았습니다.)
