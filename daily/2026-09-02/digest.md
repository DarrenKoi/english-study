# 2026-09-02 — 오늘의 표현

1. **readiness** — `mode`(환경이 사무실인가)와 별개로 "이 기능이 실제로 준비됐는가"만 따로 판정하는 축. 두 질문을 하나의 스위치로 뭉치면 설명 못 하는 실패가 생긴다.
2. **X is the norm** — 예외처럼 보이는 값이 실은 표준이라고 선을 그어, 예외 취급하려던 가정을 뒤집을 때.
3. **discharged** — 리뷰 판정 같은 의무가 커밋으로 완전히 이행돼 더 이상 남지 않았다는 뜻. 빚을 갚아 없앤다는 격식 있는 동사를 빌려 왔다.
4. **a change with cost and no effect** — `cost`와 `effect`를 대구로 놓아 "든 비용은 있는데 얻는 게 없다"는 판정을 한 문장에 압축.
5. **cascades across (four files)** — 값 하나의 변경이 여러 파일로 순차적으로 번져 나가는 모습. `across`가 퍼지는 범위를 한 단어로 명시한다.
6. **co-location** — 두 시스템을 별도 서비스로 쪼개지 않고 한 프로세스 안에 같이 두는 배치. 저자가 직접 만든 한국어 "동거"와 나란히 병기됐다.
7. **it's spent** — 물리적으로는 남아 있지만 목적을 다해 더 쓸모없어진 것을 가리키는 판정. 화살·총알이 다 쓴 상태를 뜻하던 말이다.

전체 20개는 [new-expressions.md](new-expressions.md).

### 오늘의 정독
단락 1은 타임아웃 값 변경을 요약한 실제 커밋 메시지 — 의도적 수동태(`are deliberately untouched`)와 `That separation is why X was Y instead of Z` 구조가 어떻게 설계 결정을 압축하는지 본다. 단락 2는 죽은 폴더를 삭제하며 남긴 진단 — `the tell was`라는 은유 하나로 여러 근거를 정리하는 법을 보여준다. [reading.md](reading.md)

### 오늘의 코칭
- 한글→영어: "장비 hold 해제와 루프 재시도는 별개 문제다"는 `are two separate problems`처럼 짧고 단호하게 옮긴다. 사내 공지문 "~할 수 있게 되었습니다"는 과정을 드러내지 않고 `now serves`라는 단순 현재형이면 충분하다.
- 영어 다듬기: `some takes too long` → `some take`(복수 주어-동사 일치). 타임스탬프 표현은 `stored with UTC time with zero`가 아니라 `stored in UTC with a zero offset`.

전체 15장은 [coaching.md](coaching.md).

> 처리 항목 33개 / 미뤄진 항목 856개
