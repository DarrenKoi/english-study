# 2026-09-16 — 오늘의 표현

- **Value is in the tail, not the happy path.** — 새 모델이 쓸모를 내는 자리는 잘 도는 기본 경로가 아니라 드문 예외 상황이다.
- **hedges in every section but never commits to X** — 단서만 달고 결론은 끝내 내지 않는 문서를 한 줄로 비평하는 틀. ↔ take a clear stance.
- **not a hard enforcement layer** — 지침은 방향만 잡을 뿐 막아 주지는 못한다. *CLAUDE.md instructions shape Claude's behavior but are not a hard enforcement layer.*
- **Before committing to X, validate that …** — `commit to` 뒤엔 동명사. 되돌리기 어려운 결정 앞에서 전제부터 확인하라는 권고.
- **X is cleared** — 의심하던 원인을 배제할 때. *Scale is cleared: base 1.02 means …* ≈ ruled out.
- **X by nature** — 설계 결과(`by construction`)가 아니라 대상 본래의 성질. *OM keys are periodic by nature.*
- **git revert is the rollback** — 되돌릴 장치를 따로 만들 필요가 없다는 안심 한 줄.

### 오늘의 정독
Qwen 조사 문서 검토 의견 단락 — `the research itself is solid` 로 칭찬 범위를 먼저 좁히고 `Its weakness is that it hedges … but never commits to …` 한 문장에 약점을 몰았다. align gate 권고(명령문 세 개 + 비용·롤백)와 잘못 알던 전제를 인정하는 답변(`No, I did not.` → `which is why …`)은 `reading.md` 에 함께 있다.

### 오늘의 코칭
- 한글→영어: "우리의 상황 H200 GPU1장으로 … 몇개의 요청을 처리할 수 있지?" → `In our setup, with a single H200, how many concurrent requests can qwen3.8 handle?` ("상황"은 `setup`, "1장"은 `a single`) / "preempt 하지 실패하지는 않습니다" → `preempts on its own rather than failing`.
- 영어 다듬기: `how long it does take` → `how long it takes` (간접의문은 평서 어순) / `make sure that in windows, you should use proxy` → `Make sure Windows always goes through the proxy` (`make sure` 절에는 `should` 를 넣지 않는다) / `entire remove is not proper` → `deleting the whole folder won't work`.
- 전체 한글→영어 4장, 영어 다듬기 17장은 `coaching.md`. 붙여 넣은 콘솔 로그와 파이프라인 프롬프트는 뺐다.

> 처리 항목 22개 / 미뤄진 항목 623개
