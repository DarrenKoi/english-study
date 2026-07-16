<sub>2026-07-17 · 정독</sub>

## 단락 1

Sort numbers numerically, booleans by false/true, and text with numeric-aware locale comparison. SEQ sorts by the underlying SEQ value even though the cell displays SEQ/Last_SEQ. Equal values retain source order for stable, predictable results. Sorting must not break the selected row. The table keeps each displayed row's source index, highlights selection against that source index, and emits the source index on click so the right-side image content continues to show the clicked parameter.

**문법·구조**: 첫 문장은 **명령형 병렬**입니다 — `Sort A ~ly, B by ~, and C with ~` 세 목적어가 각기 다른 방식 부사구를 달고 하나의 동사 `Sort` 를 공유합니다. 세 번째 항목만 `and` 로 묶어 목록을 닫는 것이 영어 리스트의 기본 리듬입니다. 둘째 문장의 `even though the cell displays ...` 는 **양보 부사절**로 "표시는 A/B 인데도 정렬 기준은 A 다"라는 예상 밖 사실을 대비시킵니다(대조에는 `although/even though`, 결과에는 `so`). 넷째 문장 `must not break` 는 **금지 규범**(요구사항 문서의 당위 조동사 `must`). 마지막 문장은 `keeps ... , highlights ... , and emits ...` 로 **현재시제 3인칭 동사 병렬**을 이어 표(table)를 주어로 한 동작 규약을 나열하고, 끝의 `so ... continues to show` 는 **목적/결과절**로 "그렇게 해서 클릭한 행이 계속 보인다"는 의도를 잇습니다. 명세는 이렇게 **현재시제 + 병렬 동사**로 "시스템이 늘 이렇게 동작한다"는 항구적 규칙을 진술합니다.

**핵심 표현**: `retain source order`(동순위는 원래 순서를 유지 — 안정 정렬의 정의) · `even though`(표시와 기준이 다름을 대비) · `emit ... on click`(클릭 시 값을 내보내다, 이벤트 용어).

**격식 짝**: "정렬해도 선택한 행이 어긋나면 안 된다"를
- refined: *Sorting must not disturb the selected row; selection is tracked by source index.* (작성)
- plain: *Sorting shouldn't mess up which row you picked — it remembers the row by its original spot.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-recipe-detail-header-and-parameter-sorting-design.md</sub>

---

## 단락 2

ECharts binds a theme at init time; swapping themes requires dispose + re-init on the same DOM node. The host div and its download button persist across this (same node), so ensureChart()'s mountDownloadButton() no-ops and the button's click closure reads the freshly-assigned chart. Containers may be inside a v-if and toggle on/off. When the previous element unmounts, dispose the instance bound to it and drop its detached button; when a fresh element mounts, init against the new node.

**문법·구조**: 첫 문장은 **세미콜론(;)** 으로 밀접한 두 독립절을 잇습니다 — 앞은 사실("테마는 초기화 때 고정된다"), 뒤는 그로 인한 필요("바꾸려면 폐기 후 재초기화"). 세미콜론은 마침표보다 두 생각의 **인과·긴밀함**을 드러냅니다. 둘째 문장의 `persist across this ... , so A no-ops and B reads ...` 는 **원인→결과(`so`) + 결과 내부 병렬(`and`)** 의 이중 구조. `freshly-assigned` 는 **부사+과거분사 복합형용사**(갓 할당된)로, 하이픈으로 묶어 명사 `chart` 를 앞에서 수식합니다. 마지막 문장은 `When ... , 명령형; when ... , 명령형` 의 **대칭 조건절**로 "이럴 땐 이렇게, 저럴 땐 저렇게"를 나란히 놓아 두 수명주기 분기를 대비시킵니다 — 앞뒤 `When` 절의 구조를 똑같이 맞춘 **평행 구문(parallelism)** 이 읽기 리듬을 만듭니다.

**핵심 표현**: `bind ... at init time`(초기화 시점에 묶다/고정하다) · `persist across (a re-init)`(재초기화를 거쳐도 남아 있다) · `no-op`(아무 일도 하지 않고 넘어가다, 동사처럼 쓰임) · `toggle on/off`(켰다 껐다 하다).

**격식 짝**: "테마를 바꾸려면 같은 노드에서 폐기 후 다시 초기화해야 한다"를
- refined: *Switching themes requires disposing and re-initializing the instance on the same DOM node.* (작성)
- plain: *To change themes you've got to throw the chart away and set it up again on the same element.* (작성)

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-16-chart-image-download-and-tat-colors.md</sub>
