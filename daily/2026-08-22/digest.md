# 2026-08-22 — 오늘의 표현

논쟁하고 물러서고 되받는 말이 오늘의 축이다. 설계를 두고 모델과 두 라운드를 붙은 기록과
디버깅·리뷰 스킬 문서가 배치의 절반을 채웠다.

- **objections, worst first** — 반론을 심각한 것부터. 동사도 관사도 없이 정렬 기준만 선언하는 표제형이라, 앞 명사만 갈아 끼워 `findings, highest severity first` 로도 쓴다.
- **split the difference** — 절충하다. 흥정에서 온 말인데 기술 논쟁에서는 대개 부정형으로 나온다 — 어느 쪽이 옳은지가 쟁점일 때 가운데를 고르면 아무도 옳지 않은 안이 남기 때문이다.
- **the cost moved, it didn't vanish** — 비용이 옮겨 갔을 뿐 사라지지 않았다. 접속사 없이 쉼표만으로 두 절을 붙여, 상대의 사실 주장은 인정하고 결론만 회수한다.
- **rely on it in anger** — 실전에서 믿고 쓰다. `in anger` 는 화와 무관하고 군사 표현 `fired in anger`(실전 발사)에서 왔다. 검증 안 된 비상 정지 장치에 딱 맞는 경고문이었다.
- **wait it out** — 끝날 때까지 그냥 버티다. 대명사가 동사와 부사 사이에 끼는 분리형이라 `wait out it` 은 틀린다.
- **self-inflicted** — 자초한. 근거를 반박하지 않고 근거의 출처를 무너뜨린다 — 우리가 만든 제약이라면 우리가 풀 수도 있다.
- **a correct refusal** — 옳은 거절. 실패로 보이는 동작이 사실은 정당한 거부일 수 있다고 유보하는 말이며, 성급한 수정을 막는다.

전체 23개는 `new-expressions.md`.

### 오늘의 정독

단락 1은 `is right that … but wrong that …` 한 문장으로 인정과 반박을 동시에 끝낸다.
아직 일어나지 않은 실패 시나리오를 가정법 대신 현재시제로 적어 "일어날 수도 있다"가 아니라
"이렇게 돌아간다"로 읽히게 만든 것이 이 단락의 기술이다. → `reading.md`

### 오늘의 코칭

- **한글→영어**: "구현이 쉬운쪽으로 선택해주세요" → `Go with whichever is easier to implement — your call.` 끝의 `your call` 두 단어가 위임을 못 박아 상대가 되묻지 않게 한다.
- **한글→영어**: "드러낸 것이지 만든 게 아닙니다" 는 `It is A, not B` 로 옮기면 동사의 힘이 죽는다. `surfaced a latent defect; it didn't create one` 처럼 동사 둘을 세미콜론으로 세운다.
- **영어 다듬기**: `In what circumstance` → `Under what circumstances`. 전치사는 `under` 이고 거의 항상 복수형이다.
- **영어 다듬기**: (i)이냐 (ii)냐를 묻는 양자택일 질문에 `yes` 로 답하면 앞 선택지를 고른 것으로 읽힌다. 고른 쪽을 이름으로 말해야 한다.

→ `coaching.md`

> 처리 항목 14개 / 미뤄진 항목 1341개
