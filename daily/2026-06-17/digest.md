# 오늘의 표현 — 2026-06-17

오늘 배치는 전부 프로젝트 docs(영문 섞인 한글 기술문서)였습니다. 다른 글에서도 통하는 영어 표현 위주로 골랐어요.

1. **single source of truth** — 모두가 참조하는 단 하나의 정본 기준. (약어 SSOT)
2. **the bridge between X and Y** — 분리된 두 세계를 잇는 다리. "spec layer is the bridge between home and office."
3. **document what it actually returns, not what feels canonical** — 정석처럼 보이는 게 아니라 *실제 동작* 을 문서화하라.
4. **conservative default** — 안전한 쪽을 기본값으로. "주긴 쉬워도 뺏긴 어렵다."
5. **bus-factor 1** — 핵심 지식이 한 사람에게만 묶인 위험("그 사람 빠지면 멈춘다").
6. **worst-case** — 평균이 아니라 최악값을 합격 기준으로.
7. **overfit / rank-deficient** — 데이터가 적어 모델이 우연 패턴까지 외워버림.

> 처리 항목 13개 / 미뤄진 항목 1171개

---

# 오늘의 표현 (2차) — `repo:auto_recipe_creator`

두 번째 배치는 스킬 문서·세션 저널·연간 로드맵이었습니다. 자연스러운 구어/실무 표현 위주로 골랐어요.

1. **anchor on (the first idea)** — 처음 떠오른 가설에 고착되다. 가설은 3~5개 먼저 늘어놓고 시작.
2. **stress-test a plan** — 계획을 까다로운 시나리오로 두드려 약점을 찾다.
3. **call it out / surface it** — 모순·문제를 짚어 말하다 / 수면 위로 드러내다.
4. **be opinionated** — 미적대지 말고 소신 있게 하나로 정하라 (칭찬조).
5. **load-bearing** — 빠지면 전체가 무너지는 핵심. 반대는 `lean`(군더더기 없는) 안전망.
6. **fail-safe** — 불확실하면 위험한 추측 대신 안전한 거부로 떨어지는 설계.
7. **measure first, fix second** — (성능) 추측으로 손대기 전에 먼저 재라.

> 처리 항목 12개 / 미뤄진 항목 0개 (이 배치의 48개 문서 전부 검토; 나머지는 코드·경로·고유어라 학습 표현 없음)

---

# 오늘의 표현 (3차 발굴) — 스킬 문서 관용구·설계 어휘

같은 배치를 다시 훑어 1·2차에서 놓친 표현만 골랐어요. 구어 관용구가 알짜입니다.

1. **outrun your headlights** — 이해도 못 한 채 분수에 넘게 앞서 나가다(밤 운전 비유).
2. **earning its keep** — 제 밥값을 하다 / 존재 가치를 증명하다.
3. **a strong read, not a menu** — 선택지 나열 말고 소신 있는 견해 하나를 강하게 밀어라.
4. **re-litigate (a decision)** — 끝난 결정을 자꾸 다시 끄집어내 따지다.
5. **deep module / shallow module** — 작은 인터페이스에 큰 구현(깊음=good) vs 껍데기(얕음).
6. **never refactor while RED; get to GREEN first** — 실패 중엔 손대지 말고 통과부터.
7. **backstop / safety net** — 앞이 다 실패해도 받쳐주는 최후 안전장치.

> 처리 항목 16개 / 미뤄진 항목 0개 (배치 48개 문서 3차 재검토; 나머지는 코드·경로·도메인 고유어)

---

# 오늘의 표현 (4차 · 대화형 `/study`) — `repo:auto_recipe_creator` 셋업 문서

VLM 서빙·셋업 문서(깔끔한 영어)에서 *맥락까지* 챙긴 표현들. 이번엔 **정독 단락**과 **웹 정독**도 함께.

1. **keep the GPU busy across incoming requests** — 요청이 들어와도 GPU를 놀리지 않다. `keep X busy`.
2. **the model is not truly ready until both pass** — 둘 다 통과해야 비로소 준비 완료. `not ... until` 강조.
3. **a conservative / cold-start value** — 데이터 모이기 전 보수적 기본값(나중에 캘리브레이션).
4. **pixel scores to OpenCV, vibe-reading to the VLM** — 정량 판단은 고전 CV, 분위기 파악은 VLM. (도메인 경험칙)
5. **treat its verdict as an opinion, not a measurement** — 미검증 모델 판정은 '측정'이 아니라 '의견'으로 취급.
6. **stale metaphor / the images clash** — (웹 정독) 진부한 비유 / 이미지가 서로 어긋난다.
7. **I was wondering if you'd have time to ...** — (웹 정독) 가장 공손한 회화체 요청 틀.

### 오늘의 정독
- **단락**: `reading.md` — "prefix caching is useful **because** ... **while** only the image changes" (이유+대조를 한 문장에).
- **웹**: `reading-web.md` — Orwell 의 명료한 글쓰기 단락(refined) + 코드 리뷰 정중히 부탁하기(plain).

> 처리 항목 41개(샘플 정독) / 미뤄진 항목 1276개 · 대화형 실행(웹 검색 포함)
