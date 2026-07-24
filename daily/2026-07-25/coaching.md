# 2026-07-25 — 코칭

> 오늘 배치에는 직접 쓴 한국어가 한 문장도 없었습니다(`repo:` 배포 문서의 한국어는 코칭 대상 밖, 어시스턴트 발화도 전부 영어). 그래서 한글→영어 섹션은 비우고, 영어로 지시한 두 건을 다뤘습니다.

## 영어 다듬기

### 카드 1 — `/goal` 로 건 작업 조건

- 내가 쓴 영어: "run the skill /back-to-office and finish the jobs that we haven't done yet."   (출처: transcript:[user] skewnono_v3_nuxt, `/goal` 인자)
- 정정: (문법 오류 없음 — 관계절 `that we haven't done yet` 도 시제·어순 모두 정확합니다.)
- 더 나은 표현: "Run the `/back-to-office` skill, then finish whichever carried-over jobs are actually doable from this machine. If a job needs the office network, write down what's blocking it and move on."
- 왜: 두 가지가 문장을 한 단계 올립니다.

  먼저 어순입니다. `run the skill /back-to-office` 는 한국어 "스킬 /back-to-office 를 실행해"의 순서를 그대로 옮긴 형태예요. 영어는 수식어가 앞에 붙으니 `run the /back-to-office skill` 이 자연스럽습니다. `use the skill simplify` → `use the simplify skill` 도 같은 교정이라, 이 패턴 하나만 익혀 두면 앞으로 반복해서 씁니다.

  더 중요한 건 `the jobs that we haven't done yet` 의 범위입니다. 문법은 맞지만 이 말은 **끝나지 않은 전부**를 가리켜서, 사무실 네트워크가 있어야만 되는 일까지 포함합니다. 실제로 그 때문에 Stop 훅이 아홉 번 연속으로 "아직 안 끝났다"를 반복했고, 회사망에 경로가 없다는 사실이 네 번이나 다시 측정됐습니다. 조건을 거는 문장에서는 **달성 가능한 범위를 문장 안에 넣어야** 합니다 — `whichever … are actually doable from this machine` 처럼요. `whichever` 는 "그중 ~한 것은 무엇이든"이라 조건과 대상을 한 단어로 묶어 주고, 뒤의 `If a job needs …, write down what's blocking it and move on` 은 못 하는 경우의 출구를 미리 열어 둡니다.

  참고로 `haven't done yet` 대신 `haven't gotten to yet`(아직 손대지 못한) 이나 `are still open`(아직 열려 있는) 을 쓰면 "안 했다"의 책망하는 느낌이 옅어집니다. 남은 일을 가리키는 실무 표준어는 `open` 이나 `outstanding` 입니다.

### 카드 2 — 리뷰 범위 지정

- 내가 쓴 영어: "changes since 88a5aee — wafer die-grid offset + mock map_offset coherence" / "review changes since 88a5aee (wafer-geometry map_offset coherence, Tasks 5-6 + offset call-site wiring)"   (출처: transcript:[user] skewnono_v3_nuxt, `/simplify`·`/code-review` 인자)
- 정정: (문법 오류 없음 — 둘 다 명령형과 명사구를 의도대로 쓴 라벨입니다.)
- 더 나은 표현: "Review everything that landed since 88a5aee — the wafer die-grid offset, the mock's `map_offset` coherence, and the offset wiring at the call sites."
- 왜: 지금 형태는 커밋 제목처럼 압축된 라벨이라 그 자체로 문제가 없습니다. 다만 문장으로 풀면 두 가지를 얻습니다.

  `changes since 88a5aee` 를 `everything that landed since 88a5aee` 로 바꾸면 `land` 가 일합니다. 이 동사는 "머지되어 실제로 들어갔다"는 뜻이라, 작업 중인 변경과 이미 반영된 변경을 갈라 줍니다. `What landed this week?` 는 스탠드업에서 그대로 쓰는 문장입니다.

  그리고 `+` 로 이어 붙인 항목은 `A, B, and C` 로 푸는 편이 낫습니다. 기호는 세 항목이 같은 층위인지 아닌지를 못 보여 주는데, 실제로 이 셋 중 마지막(`offset call-site wiring`)은 앞 둘의 결과라 성격이 다릅니다. 영어에서 열거의 마지막 앞에 오는 `and` 는 "여기서 목록이 끝난다"는 신호라, 읽는 쪽이 범위를 정확히 닫을 수 있습니다.

  소유격도 하나 챙겨 두세요. `mock map_offset coherence` 는 명사 셋이 붙어 있어 무엇이 무엇에 속하는지 모호합니다. `the mock's map_offset` 으로 아포스트로피를 넣으면 "목이 내보내는 map_offset"이 분명해집니다 — 실제로 설계 문서도 `the emitted map_offset and the generated stage_coordinate` 처럼 소유·수식 관계를 매번 드러냅니다.
