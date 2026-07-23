# 2026-07-24 — 정독

## 단락 1

Connect the Hardware page's BM/PM tab to the office OpenSearch indices `fab_inform_notes` (work that happened) and `tool_maintenance_plan` (work that is scheduled), widening the table rows to carry the fields engineers read. The tab already has a per-tab provider pair under `hardware/providers/bm_pm/`. A new tracked `_shared.py` holds the value logic both providers must agree on (BM/PM classification, timestamp format, note merging, summary cards); `mock.py` and `office_example.py` each build rows from their own source and pass them through it. The dispatcher, route, contract, and Vue component are untouched — `BmPmTables.vue` renders whatever `columns` the normalizer declares. Row timestamps render as `%Y-%m-%d %H:%M` everywhere. `front-dev-home/app/utils/bmPmMarkers.ts` matches `job_starts` against the trend charts' x-axis values; a different format places markers nowhere instead of failing. The dispatcher swaps the modules by name, so drift surfaces as blank cells, not an error. Never create `providers/bm_pm/office.py`. It is gitignored, and creating it is what switches the tab to office data.

**문법·구조**: 두 인덱스에 붙인 괄호 설명 `(work that happened)` 와 `(work that is scheduled)` 가 이 단락에서 가장 배울 만한 대목입니다. 과거 단순시제 대 수동 현재시제 — 시제 하나로 "이미 일어난 일"과 "잡혀 있는 일"을 갈라 놓아, 두 인덱스의 존재 이유를 형용사 없이 설명합니다. 뒤이은 `widening the table rows to carry …` 는 분사구문이라 주절과 주어가 같고, 접속사 없이 "그러면서 동시에"를 붙입니다. `the fields engineers read` 는 관계대명사가 생략된 접촉절.

`the value logic both providers must agree on` 도 같은 생략형인데, 전치사 `on` 이 문장 끝에 남는 형태입니다. 문어에서 `on which both providers must agree` 로 바꿔 쓸 수는 있지만 기술 문서에서는 지금 형태가 표준. 세미콜론은 두 독립절이 같은 사실의 앞뒤를 이룰 때 쓰였고, 마침표로 끊으면 "공유 파일이 있다"와 "각자 통과시킨다"의 연결이 느슨해집니다.

`renders whatever columns the normalizer declares` 의 `whatever` 는 자유관계사 — "무엇이든 그것을"이라 목적어와 접속사를 한 단어가 겸합니다. 이게 여기서는 설계 주장이기도 합니다. 컴포넌트가 열 목록을 모른다는 사실 자체를 문법으로 보여 주니까요.

경고 문장 셋의 구성이 특히 실용적입니다. `a different format places markers nowhere instead of failing` — 실패 대신 조용히 엉뚱한 곳에 놓인다는 것, 즉 **증상이 없다는 게 증상**이라는 경고를 `instead of` 하나로 압축했습니다. `drift surfaces as blank cells, not an error` 도 같은 틀(`as X, not Y`). 마지막 `creating it is what switches the tab` 은 유사분열문으로, "만들지 마라"의 근거를 등식처럼 못 박습니다.

**핵심 표현**: `pass them through it` — 값을 공유 로직에 통과시킨다는 뜻으로, 파이프라인 설명의 기본 동사구. `drift surfaces as blank cells` 에서 `surface as` 는 "겉으로 ~의 모습으로 드러나다"라 증상 서술에 딱 맞습니다. `untouched` 는 한 단어로 "이번 변경에서 건드리지 않음"을 선언하는 설계 문서 상용어.

**격식 짝**:

- refined: `The dispatcher, route, contract, and Vue component are untouched.` / plain: `We're not touching the dispatcher, the route, the contract, or the Vue side.`
- refined: `A different format places markers nowhere instead of failing.` / plain: `If the format's off, the markers just don't show up — nothing errors out.`

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-23-bm-pm-office-adapter.md</sub>

---

## 단락 2

Words appear in a design for one reason: to make it easier to understand, and therefore easier to use. They are design material, not decoration. Bring the same intentionality to copy that you would bring to spacing and color. Before writing anything, ask what the design needs to say, and how it can best be said to help the person navigate the experience. Write from the end user's side of the screen. Name things by what people control and recognize, never by how the system is built. A person manages notifications, not webhook config. Describe what something does in plain terms rather than selling it. Being specific is always better than being clever.

**문법·구조**: 첫 문장의 콜론이 `one reason` 을 받아 그 이유를 to부정사로 펼칩니다. 그리고 `easier to understand, and therefore easier to use` — 같은 비교급 틀을 두 번 쓰면서 사이에 `therefore` 를 끼워, 두 이점이 병렬이 아니라 **인과**임을 밝힙니다. 이해가 먼저고 사용은 그 결과라는 순서가 문장 형태에 그대로 담겼습니다.

`They are design material, not decoration.` 은 이 글 전체를 관통하는 `X, not Y` 틀의 첫 등장입니다. 같은 틀이 `by what people control …, never by how the system is built`, `notifications, not webhook config` 로 세 번 더 돌아옵니다. 부정항을 뒤에 두면 마지막에 남는 잔상이 "하지 말아야 할 것"이라, 지침 문장에서 기억에 오래 붙습니다.

`the same intentionality to copy that you would bring to spacing and color` 의 `would` 를 놓치지 마세요. 실제로 그렇게 하고 있다는 서술이 아니라 "spacing 에는 당연히 그러지 않느냐"는 **가정 위의 비교**입니다. `do` 로 썼다면 사실 확인이 되어 설득력이 줄어듭니다.

명령형이 여섯 문장 연속으로 이어지는데도 단조롭지 않은 이유는 길이 조절입니다. 긴 명령문(`Before writing anything, …`) 다음에 짧은 명령문(`Write from the end user's side of the screen.`), 그다음 예시 한 문장(`A person manages notifications, not webhook config.`). 마지막은 명령형을 버리고 동명사 주어의 평서문(`Being specific is …`)으로 닫아, 지시가 아니라 원칙으로 착지합니다.

**핵심 표현**: `design material, not decoration` — 재료냐 장식이냐는 대비는 코드 리뷰에도 그대로 옮겨 씁니다(주석은 재료인가 장식인가). `write from the end user's side of the screen` 은 화면을 사이에 둔 위치로 시점을 지정하는 표현이라, `from the user's perspective` 보다 그림이 선명합니다. `specific … than clever` 는 영어권 기술 글쓰기의 오래된 경구로, 변수 이름 논쟁에서 그대로 인용됩니다.

**격식 짝**:

- refined: `Name things by what people control and recognize, never by how the system is built.` / plain: `Call it what users actually do with it, not what it's called in the code.`
- refined: `Being specific is always better than being clever.` / plain: `Just say what it does — don't try to be witty.`

<sub>출처: transcript:[user] skewnono_v3_nuxt (f604dd4e, frontend-design 스킬 본문)</sub>

---

## 단락 3

The two `live-alarm.vue` pages are 29 lines differing by 6 — textbook duplication. But every cd-sem/hv-sem page pair in this repo is that same thin shim (`fail-issue` 15/2, `hardware` 28/6, `index` 31/6, `recipe-status` 28/6). Collapsing only live-alarm would make it the lone exception among five siblings. In a codebase, *consistent* duplication is a pattern; deduplicating one instance is what actually creates the maintenance hazard. Nuxt's eslint already runs `no-unused-vars`, so dead locals and imports are pre-caught. Effort at 02:10 should go where linters are blind: unused *exports*, unreferenced files, dead props, and superseded scripts.

**문법·구조**: `29 lines differing by 6` 은 현재분사가 명사를 뒤에서 꾸미는 형태로, `29 lines that differ by 6` 을 세 단어로 줄였습니다. 수치 뒤에 분사를 다는 이 압축은 리뷰 메모에서 아주 자주 쓸 만합니다.

세 번째 문장의 `would make` 가 논지의 무게중심입니다. 아직 하지 않은 리팩터링의 결과를 가정법으로 그려 보이기 때문에, 반대 근거를 제시하면서도 상대 제안을 틀렸다고 단정하지 않습니다. 실제로 그렇게 됐다면 `made` 였겠죠.

네 번째 문장의 세미콜론은 대조를 담습니다. 앞은 일반 원칙(`consistent duplication is a pattern`), 뒤는 그 원칙에서 나오는 반직관적 결론(`deduplicating one instance is what actually creates the hazard`). 마침표로 나누면 두 주장이 그냥 나열되지만, 세미콜론은 뒤 절을 앞 절의 귀결로 묶습니다. `is what actually creates` 는 앞 단락들과 같은 유사분열문 — `actually` 가 들어가면서 "상식과 반대로"라는 뒤집기 신호가 붙습니다.

마지막 문장의 `where linters are blind` 는 장소가 아니라 **범주**를 가리키는 자유관계사입니다. 그 뒤 콜론이 그 범주의 목록을 열어 주고, `unused exports / unreferenced files / dead props / superseded scripts` 넷이 모두 형용사+명사로 리듬을 맞춥니다.

**핵심 표현**: `a thin shim` — 두 층 사이에 끼워 넣은 얇은 껍데기 코드. `sibling`(같은 층위의 형제 파일)과 짝지어 쓰면 구조 설명이 간결해집니다. `pre-caught` 는 `pre-` 를 분사에 붙여 "이미 앞 단계에서 걸러진"을 한 단어로 만든 즉석 조어인데, 기술 글에서 이런 조어는 허용 폭이 넓습니다. `where linters are blind` 는 도구의 사각지대를 가리키는 표현으로 그대로 외워 둘 만합니다.

**격식 짝**:

- refined: `Collapsing only live-alarm would make it the lone exception among five siblings.` / plain: `If we merge just live-alarm, it ends up the only odd one out of the five.`
- refined: `Effort at 02:10 should go where linters are blind.` / plain: `Spend the time on stuff the linter can't see.`

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (e5bd7677)</sub>
