# 2026-09-29 — 정독

> 세 단락 모두 배치 원문 그대로다. 단락 1은 사무실 LLM 에게 보내는 조사 브리프의 머리말로, 형제 문서와 역할을 나누고 전제 조건을 거는 구성이 교과서적이다. 단락 2는 OM align 진단에서 128 px 라는 숫자 하나로 "같은 키의 중복이냐, 옆에 있는 닮은꼴이냐"를 가려내는 추론. 단락 3은 번호 목록 두 항목에서 번호와 굵은 소제목만 뗐다. 배포 전에 왜 빈 셀을 쓰면 안 되는지 인과를 끝까지 따라간다.

## 단락 1

This brief is for an LLM running **at the office**, next to the real data. Its sibling, `hardware_field_usage.md`, asks whether each field *exists* in the shape the code reads. This one asks what the data *behaves* like: cadence, ranges, noise, what the unexplained tokens mean, and which differences between tools are real signal. Home cannot see any of this. The FDC and SCE panels were built on a mock, so several of their display choices are guesses. Run `hardware_field_usage.md` first. If the schema is wrong, these statistics are meaningless.

**문법·구조**: 첫 문장의 `running at the office` 는 `an LLM` 을 뒤에서 꾸미는 현재분사구(= that is running)이고 쉼표 뒤 `next to the real data` 가 위치를 덧붙인다. 둘째·셋째 문장은 `Its sibling … asks whether …` / `This one asks what …` 로 주어와 동사를 맞춰 대구를 만들었다. `whether`(있느냐 없느냐)와 `what … like`(어떻게 행동하느냐)를 기울임꼴 `exists` ↔ `behaves` 로 대비한 게 이 단락의 뼈대다. 셋째 문장 콜론 뒤 목록은 명사(`cadence, ranges, noise`)에서 명사절(`what the unexplained tokens mean`, `which differences … are real signal`)로 길어진다. 넷째 문장 `Home cannot see any of this.` 는 짧다. 앞의 긴 목록을 한 번에 받아 제약을 못 박는 문장이라 짧아야 힘이 산다. 다섯째 문장은 수동태 `were built on a mock` 으로 만든 주체보다 "무엇 위에 지어졌나"에 초점을 두고 `so` 로 결론(`are guesses`)을 잇는다. 끝의 두 문장은 명령문 → 조건문 순서. 먼저 지시하고 이유를 뒤에 붙였다.

**핵심 표현**: `Its sibling, X, asks …; this one asks …` — 관련 문서 둘의 역할을 한 쌍으로 가른다. / `Home cannot see any of this.` — 앞 목록 전체를 `any of this` 로 받아 한계를 선언. / `If the schema is wrong, these statistics are meaningless.` — 선행 조건을 어기면 결과가 무의미해진다는 경고.

**격식 짝**: (작성)
- refined: Its companion document verifies that each field exists in the expected shape; this one characterizes how the data behaves.
- plain: The other brief checks the fields are there. This one checks what the data actually looks like.

<sub>출처: repo:skewnono_v3_nuxt docs/datatables/hitachi/hardware_fdc_sce_characterization.md</sub>

---

## 단락 2

Now the 2nd is a genuinely different spot, but 128 px is still close. One constraint pins the key size: the matcher only scores positions where the whole template fits inside the frame. With the key centered at y=64, the template can't be taller than about 128 px. An OM key is also 10–20% of the frame, so it's probably ~100–130 px wide. That makes a 128 px offset (dx −127, dy −12) **about one key width to the left**: an adjacent copy of the same pattern, not an overlapping duplicate. That's hypothesis 2, a repeating OM array. The matcher is working correctly: inside the white box, the key and its neighbor really look the same (0.83 vs 0.82).

**문법·구조**: 첫 문장은 `Now …, but … still …` 으로 진전을 인정하고 곧장 남은 문제를 짚는다. `still` 이 "나아졌지만 아직"의 뉘앙스를 맡는다. 둘째 문장 `One constraint pins the key size:` 의 `pin` 은 "값을 한 점에 고정하다"라는 동사고 콜론 뒤에 그 제약을 풀어 쓴다. `where the whole template fits inside the frame` 은 `positions` 를 꾸미는 관계부사절. 셋째 문장은 `With + 명사 + 과거분사`(`With the key centered at y=64`) 독립 분사구문으로 조건을 앞에 깔고 `can't be taller than` 으로 상한을 준다. 넷째 문장의 `also` 는 두 번째 근거를 덧붙이는 신호이고 `probably` 로 추정임을 밝힌다. 다섯째 문장 `That makes X Y` 는 5형식(`make + 목적어 + 보어`)이다. 앞의 두 근거가 128 px 를 "키 한 개 폭"으로 만든다는 결론의 문형. 콜론 뒤 `A, not B` 로 두 가설 중 하나를 고른다. 마지막 문장도 콜론으로 판정(`is working correctly`) 뒤에 증거를 붙였다. 콜론이 세 번 나오는데 모두 "주장 → 근거"의 순서다.

**핵심 표현**: `One constraint pins X:` — 여러 가능성 중 하나로 값을 좁히는 근거를 꺼낸다. / `That makes X about Y` — 계산 결과를 해석으로 바꿔 말하는 문형. / `an adjacent copy of the same pattern, not an overlapping duplicate` — 비슷해 보이는 두 해석을 형용사 한 쌍(adjacent ↔ overlapping)으로 가른다.

**격식 짝**: (작성)
- refined: Given the frame constraint, the 128 px offset corresponds to approximately one key width, indicating an adjacent instance of a repeating pattern rather than a duplicate detection.
- plain: 128 px is about one key wide, so it's the key next door, not the same key twice.

<sub>출처: transcript:[assistant] auto-recipe-creator</sub>

---

## 단락 3

Never write a bad cell into a side-field; leave the field out. Because the index is dynamically mapped, the first write fixes each field's type. After that, a doc carrying `""`, `"abc"` or `NaN` in a float or long field is rejected outright, and the whole FDC record is lost, `values` included. Our mirror skips unparseable cells for exactly this reason (for example, `'25,0'` reads as 25.0 and junk is omitted). Write numbers as numbers, not strings. If `temp_c` is first written as `"23.39"`, it's mapped as text for the life of that index. The average query on it then fails, so the fleet view goes empty until a rollover.

**문법·구조**: 명령문 두 개(`Never write …`, `Write numbers as numbers …`)가 단락을 두 덩어리로 나누고 각 명령 뒤에 이유가 따라온다. 첫 문장은 세미콜론으로 금지와 대안(`leave the field out`)을 한 줄에 묶었다. 둘째 문장 `Because …, the first write fixes each field's type` 에서 `fix` 는 "고치다"가 아니라 "고정하다"다. 셋째 문장은 `carrying …` 현재분사구가 `a doc` 을 꾸미고 수동태 `is rejected outright` 와 `is lost` 를 `and` 로 이었다. 끝의 `values included` 는 독립 분사구문(= with values included)으로 "values 까지 포함해서"라는 피해 범위를 덧붙인다. 넷째 문장 `for exactly this reason` 은 앞 문장 전체를 이유로 받는다. 여섯째 문장의 `for the life of that index` 는 "그 인덱스가 존재하는 한 계속"이라는 기간 표현. 마지막 문장은 `then … so … until` 로 실패가 번지는 순서와 끝나는 시점을 한 줄에 담았다. 수동태가 많은 이유는 행위자(누가 매핑하나)보다 데이터에 무슨 일이 생기는지가 초점이기 때문이다.

**핵심 표현**: `is rejected outright` — 부분 처리 없이 통째로 거부된다. / `X included` — 명사 뒤에 붙여 "X 까지 포함해서"를 짧게. / `for the life of the index` — 되돌릴 수 없는 기간을 강조한다.

**격식 짝**: (작성)
- refined: Unparseable values must be omitted rather than written, since a type conflict causes the entire document to be rejected.
- plain: If a cell doesn't parse, just skip that field. One bad value and the whole record gets thrown out.

<sub>출처: transcript:[assistant] skewnono-v3-nuxt</sub>
