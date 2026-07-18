# 2026-07-18 — 오늘의 표현

오늘 배치는 RAG 챗 설계 스펙, AFM 컨트롤 시리즈 스펙/플랜, 시니어 코드리뷰
transcript 였습니다. 새 표현 15개 중 핵심 7개:

- **carry forward** — 앞 단계의 발견·결정을 다음 설계로 "이월"해 반영하다. "findings this design must carry forward."
- **go stale** — 기본값·목록이 시간이 지나 낡아 못 쓰게 되다. "free tiers that go stale."
- **a curated subset** — 실수로 빠뜨린 게 아니라 기준을 갖고 엄선한 일부. "We port a curated subset."
- **tightly-scoped** — 딱 필요한 범위만 건드린(리뷰 최고 칭찬 중 하나). "a tightly-scoped, well-tested decoupling."
- **remove only noise** — 지워도 정보 손실이 없다는 삭제 정당화. 짝: "silencing the warning hides nothing."
- **(conventions that) bit us** — 한 번 당해 본 함정·규칙. 경고형은 "this will bite you later."
- **keep the diff frozen** — 머지 전 diff 를 더 건드리지 않고 동결하다. "Defer if you want to keep the diff frozen."

### 오늘의 정독
`reading.md` 단락 2 — 시니어 리뷰어의 문체: "Backward compatibility holds." 처럼
두세 단어 헤드라인으로 결론을 먼저 선언하고 근거를 뒤에 대는 구조를 정독하세요.

> 처리 항목 18개 / 미뤄진 항목 0개

---

## 2차 실행 (수동 파이프라인) — 추가 표현

재수집 배치(egress guard 설계 + Skewvoir 드릴다운 영문 플랜 + YouTube 세션)에서 16개를 더 골랐고, 이번엔 트랜스크립트가 들어와 **coaching.md 가 생성됐습니다**. 핵심 6개:

- **fail open / fail closed** — 설정 누락 시 허용/차단 어느 쪽으로 실패하는가. "The default fails open."
- **a residual gap** — 대책 후에도 남는 빈틈을 명시적으로 수용. "accepts one residual gap."
- **land (a change) / in-flight** — 변경을 머지해 안착시키다 / 아직 진행 중인. "Land the in-flight work first."
- **the done bar** — 완료 판정 기준선. "excluded from the Phase-1 done bar."
- **hard-won (lessons)** — 시행착오 끝에 얻은. "bakes in the hard-won lessons."
- **chime in / preach to the choir** — 대화에 한마디 보태다 / 이미 동의하는 청중에게 설득하다(강연 구어 짝).

### 오늘의 정독 (추가)
`reading.md` 단락 4 — egress guard 문제 서술: 일반 현재 → If 조건절 → 콜론 압축("a *missing* config silently produces an *external* call") → 대시 해법으로 이어지는 문제 정의문의 정석 흐름.

### 오늘의 코칭
- 한글→영어: "내용이 적은 편인데, 구조상 어쩔 수 없는건가?" → "The outputs look a bit thin — is that inherent to how the pipeline works?" (inherent to 가 핵심) — 카드 1.
- 영어 다듬기: "make sentences gramatically correct and full sentences" → "rewrite it into complete, grammatical sentences" (두 구문 충돌을 한 동사로 통일) — 카드 2.
- 전체 10장은 `coaching.md` 참조 (한글→영어 7 + 영어 다듬기 3).

> 처리 항목 8개 / 미뤄진 항목 0개 (2차 실행분: 문서 4건 + 트랜스크립트 4건 기준)
