# 2026-08-09 — 코칭

## 영어 다듬기

### 카드 1 — 선택된 항목의 색을 통일해 달라고 하기
- 내가 쓴 영어: "when you select multi-fabs in the left side bar, make their color the same. now they are different"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `multi-fabs` → `multiple fabs`. `multi-` 는 접두사라 뒤에 명사가 붙어 복합어를 만들 때만 살아 있습니다(`multi-fab selection`, `multi-select`). 홀로 떨어져 "여러 개의"라는 형용사로 복수형을 취하지는 못하므로 `multi-fabs` 는 비문입니다. `left side bar` 는 한 단어 `sidebar` 이고, `now` 로 시작하는 뒷문장은 앞 문장과 대비되므로 `right now` 나 `at the moment` 로 시점을 분명히 하는 게 자연스럽습니다.
- 더 나은 표현: When multiple fabs are selected in the left sidebar, they should all render in the same color — right now the non-routed ones look faded.
- 왜: 명령형 `make their color the same` 은 지시로는 통하지만 현상 보고와 요구가 두 문장으로 흩어집니다. `they should all render in …` 로 기대 상태를 먼저 못 박고 대시 뒤에 실제 상태를 붙이면, 상대가 무엇을 비교해야 하는지가 한 문장에 들어옵니다. `look faded` 처럼 증상을 좁혀 주면 원인(투명도)까지 곧바로 좁혀집니다 — `different` 만으로는 색상·굵기·배경 중 무엇인지 알 수 없습니다.

### 카드 2 — 드롭다운에 다중 선택을 넣어 달라고 하기
- 내가 쓴 영어: "Also in the landing page we can select fab via (팹 선택) In the dropdown, we should enable checkbox that enable to select multi fabs."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: 세 곳입니다. ① `in the landing page` → `on the landing page`. 웹 페이지는 평면으로 취급해 `on` 을 씁니다(`on this page`, `on the home screen`). ② `enable to select` — `enable` 은 `enable + 목적어 + to 부정사` 형태만 취하므로 목적어 없이 `enable to V` 는 성립하지 않습니다. `let you select` 나 `enable multi-select` 로 바꿉니다. ③ `enable checkbox` → `add checkboxes`. 가산명사 단수에는 관사가 필요하고, 여기서는 항목마다 하나씩이므로 복수가 맞습니다.
- 더 나은 표현: The landing page has a 팹 선택 dropdown too — let's add checkboxes there so you can pick more than one fab.
- 왜: `we should enable …` 을 `let's add …` 로 바꾸면 같은 요청이 제안으로 읽혀 부드럽습니다. `that enable to select multi fabs` 처럼 관계절로 기능을 설명하기보다 `so you can pick more than one` 으로 목적절을 쓰면 문장이 짧아지고 오류 여지도 사라집니다. `multiple` 과 `more than one` 은 뜻이 같은데, 회화에서는 후자가 더 흔합니다.

### 카드 3 — 존재하지 않는 값이 선택돼 있다고 신고하기
- 내가 쓴 영어: "in the landing page, fab 선택, M16 is pre-selected, which is not existant in fab names. check this bug"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: `existant` 는 없는 철자입니다. 형용사는 `existent` 이지만 실제로는 거의 늘 부정형 `non-existent` 로만 쓰이고, 이 문맥의 자연스러운 표현은 `there's no such fab name` 입니다. `in the landing page` → `on the landing page` (카드 2와 같은 규칙).
- 더 나은 표현: On the landing page, the 팹 선택 dropdown comes up with M16 pre-selected, but there's no such fab name — can you track down where it's coming from?
- 왜: `comes up with … pre-selected` 는 "페이지를 열면 그 상태로 시작한다"는 재현 조건까지 담습니다. `check this bug` 는 명령형이라 짧지만, 여기서 원하는 건 확인이 아니라 출처 추적이므로 `track down where it's coming from` 이 요청을 정확히 옮깁니다. 버그 보고에서는 `which is not …` 같은 관계절보다 `but` 으로 기대와 현실을 대비시키는 편이 읽기 쉽습니다.

### 카드 4 — 포트를 비워 달라고 하기
- 내가 쓴 영어: "turn off 3000, 5050 ports. I will run it by myself"   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `3000, 5050 ports` → `ports 3000 and 5050`. 번호는 명사 뒤에 오고(`port 3000`, `line 42`, `chapter 7`), 앞에 나열하면 수량으로 읽힙니다. ② `turn off ports` 는 어색합니다 — 포트는 켜고 끄는 장치가 아니라 프로세스가 점유하는 자리이므로 `free up` 이나 `kill whatever's listening on` 을 씁니다. ③ `by myself` 는 "혼자 힘으로, 도움 없이"라는 뜻이라 여기서는 과합니다. "내가 직접"은 재귀 강조 `myself` 만으로 충분합니다.
- 더 나은 표현: Free up ports 3000 and 5050 — I'll start the servers myself.
- 왜: `it` 이 무엇을 가리키는지 불분명했습니다(포트 둘? 서버 둘?). 목적어를 `the servers` 로 밝히면 그 모호함이 사라집니다. `Free up` 은 "비워 두라"까지 뜻해서 상대가 재시작을 시도하지 않게 막고, 대시로 이유를 붙이면 지시가 통보가 아니라 역할 분담이 됩니다.

### 카드 5 — 요소를 카드 안으로 옮겨 달라고 하기
- 내가 쓴 영어: "in fdc 분석 of the skewnono/analysis page, the top component (파라미터 매트릭스, 개별 그래프) should be placed in the component that has colored background."   (출처: transcript:[user] skewnono_v3_nuxt)
- 정정: ① `colored background` 앞에 관사가 빠졌습니다 — `background` 는 가산명사라 단수에는 `a` 가 필요합니다(`a colored background`). ② `in fdc 분석 of the … page` 의 이중 전치사 대신 큰 것부터 좁혀 갑니다: `On the skewnono/analysis page, in the FDC 분석 tab, …`. ③ 앞에서 `component` 를 두 번 쓰는데 서로 다른 대상이라 헷갈립니다.
- 더 나은 표현: On the skewnono/analysis page, in the FDC 분석 tab, the tab strip (파라미터 매트릭스 / 개별 그래프) should sit inside a tinted card like the blocks below it.
- 왜: `the component that has a colored background` 는 어느 컴포넌트인지 특정하지 못합니다. `a tinted card like the blocks below it` 처럼 이미 화면에 있는 사례를 가리키면 지시가 한 번에 확정됩니다. `be placed in` 은 수동태라 행위자를 찾게 만드는데, `sit inside` 는 배치의 결과 상태를 그려서 UI 요구에 더 잘 맞습니다.
