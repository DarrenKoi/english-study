# 2026-10-02 — 정독

> 세 단락 모두 배치 원문(어시스턴트 답변)이다. 단락 1은 "갑자기 NameResolutionError 가 난다, 왜냐"는 질문에 코드가 아니라 네트워크 문제라고 판정하고 근거를 대는 대목이다(첫 문단에 "Why the code isn't the cause" 목록 세 항목을 이어 붙였다). 단락 2는 차트 호버 버그를 Before / Now 로 나눠 보고한 글, 단락 3은 새 분석을 제안하면서 붙인 주의 사항 목록. 단락 2와 3은 목록 기호와 굵은 표시만 뗐다.

## 단락 1

This is a network/DNS problem on the machine running Flask, not a bug in the code. `NameResolutionError … getaddrinfo failed` means the OS couldn't turn `skewnono-db1-os.osp01.skhynix.com` into an IP address. It never reached OpenSearch, so no connection or login was attempted. Nothing in `ops_store/`, `backend/_logging/`, `backend/_runtime/` or `index.py` has changed since 2026-09-20. The hostname isn't in the code. `ops_store/base.py:79` reads it from `OPENSEARCH_HOST` in your `backend/.env`. The `[opensearch-log]` line comes from a startup check (`backend/_logging/opensearch_handler.py:478`) that only runs when the process detects it's at the office and `OPENSEARCH_PASSWORD` is set. So site detection said "office", and the network then couldn't find the host.

**문법·구조**: 첫 문장은 `A, not B` 로 판정부터 내린다. `the machine running Flask` 는 현재분사가 뒤에서 명사를 꾸미는 꼴로 `the machine that is running Flask` 를 줄였다. 둘째 문장은 `means (that)` 뒤에 과거 `couldn't` 를 썼다. 에러 메시지의 뜻은 늘 같으니 `means` 는 현재, 실제로 실패한 일은 이미 일어났으니 과거. 셋째 문장은 `never reached` 로 "거기까지 가지도 못했다"를 말하고 `so` 뒤를 수동태 `no connection or login was attempted` 로 받았다. 누가 시도했는지가 아니라 시도 자체가 없었다는 게 요점이라 `no + 명사` 를 주어로 세웠다. 넷째 문장은 현재완료에 `since + 날짜` 를 붙여 "그날부터 지금까지 바뀐 게 없다"를 못 박는다. 동사에 부정어가 없는 까닭은 주어가 이미 `Nothing` 이어서. 그다음 세 문장은 코드가 어떻게 동작하는지를 말하므로 모두 단순현재다(`isn't`, `reads`, `comes from`, `only runs`). `a startup check … that only runs when …` 에서는 관계절 안에 `when` 절이 다시 들어 있고 그 안에서 조건 둘이 `and` 로 묶였다. 마지막 문장은 `So` 로 추론을 닫으면서 시제를 과거로 되돌린다. 오늘 실제로 벌어진 일을 순서대로 재구성하는 문장이라서다.

**핵심 표현**: `not a bug in the code` — 책임 소재를 첫 문장에서 가른다. / `turn A into B` — "A 를 B 로 바꾸다". DNS 조회를 전문 용어 없이 풀어 쓴 말. / `no connection or login was attempted` — "시도조차 없었다"를 수동태로.

**격식 짝**: (작성)
- refined: The failure occurred during name resolution, before any connection was established; the application code is therefore not implicated.
- plain: It couldn't even look up the server's address, so the code isn't the problem.

<sub>출처: transcript:skewnono_v3_nuxt (OpenSearch 이름 해석 오류 진단)</sub>

---

## 단락 2

Before: on these charts the "nearest point" was chosen almost only by height, so it could jump to a point several columns away. Skewvoir's Time-Series 장비 axis had this: hovering in one tool's column named a tool 150px away, which I reproduced on the old code. Codex found a gap in my first fix: the distance was measured from the column's centre instead of the pointer, so a dot 41px away could be missed near a column edge. I fixed that, and Codex confirmed it with real ECharts conversions. Now: hovers pick the dot geometrically nearest the pointer, on both sides of a column edge. The time-axis charts (like the Fab 추세선) are unchanged. The calculation is now a small pure function with node tests, including Codex's exact case. The tests fail if the fix is removed.

**문법·구조**: `Before:` 와 `Now:` 두 라벨이 시제를 가른다. 앞쪽은 과거(`was chosen`, `had`, `found`, `was measured`), 뒤쪽은 현재(`pick`, `are unchanged`, `is`). 과거 구간의 수동태 `was chosen`, `was measured` 는 누가 골랐는지보다 무엇을 기준으로 삼았는지가 중요해서 썼다. `could jump`, `could be missed` 의 `could` 는 "늘 그랬다"가 아니라 "그럴 수 있었다"다. 조건이 맞을 때만 드러나는 버그였다는 뜻을 조동사 하나가 맡는 셈. 콜론은 세 번 나오는데 쓰임이 다 같다. 앞에서 요약하고 뒤에서 풀어 준다(`had this: …`, `a gap in my first fix: …`). `hovering in one tool's column named a tool 150px away` 는 동명사구가 주어다. `, which I reproduced on the old code` 의 `which` 는 앞 절 전체를 받는다. `from the column's centre instead of the pointer` 에서 `instead of` 뒤에 생략된 말은 `from`. `the dot geometrically nearest the pointer` 의 `nearest` 는 전치사처럼 목적어를 바로 받는다(`nearest to` 도 된다). 마지막 문장은 단순현재 조건문으로, 한 번 있었던 일이 아니라 이 테스트의 성질을 말한다.

**핵심 표현**: `found a gap in my first fix` — 리뷰어가 찾은 빈틈을 숨기지 않고 보고에 넣는다. / `on both sides of a column edge` — 경계 양쪽에서 다 맞다는 범위 표시. / `The tests fail if the fix is removed.` — 테스트가 진짜로 지키고 있다는 증거를 한 문장으로.

**격식 짝**: (작성)
- refined: The initial fix measured distance from the centre of the column rather than from the pointer, and could therefore overlook a point close to a column boundary.
- plain: My first fix measured from the middle of the column, so it could miss a dot right next to the edge.

<sub>출처: transcript:skewnono_v3_nuxt (하드웨어 탭 리셋·카테고리 축 수정 보고)</sub>

---

## 단락 3

Things to keep in mind with these: They show differences in correction settings, not proven measurement skew. The MDC schema doc says the same. With only 4–6 tools, the median includes your own tool. Nothing should auto-flag a tool as bad. Office data is collected once a day, so the exact time of a change isn't known. #2 and #5 can only give the day. #3 can't be labelled as an X/Y anisotropy, because what the 0°/90° suffixes physically mean isn't confirmed.

**문법·구조**: 사건이 아니라 데이터의 성질과 한계를 말하는 글이라 시제는 전부 단순현재. 둘째 문장(원문 첫 항목)은 `A, not B` 로 이 분석이 보여 주는 것과 보여 주지 못하는 것을 가른다. `proven` 은 형용사로 쓰인 과거분사. `says the same` 의 `the same` 은 뒤에 `thing` 이 생략된 대명사 용법이다. `With only 4–6 tools,` 는 `with` 구가 이유를 맡아 `Because there are only …` 보다 짧다. `Nothing should auto-flag …` 는 부정어를 주어로 세운 금지다. `must not` 만큼 세지 않은, 설계 원칙을 말하는 어조. `is collected once a day, so … isn't known` 은 수동태 둘이 이어진다. 누가 수집하는지, 누가 모르는지는 말할 필요가 없어서. `can only give the day` 의 `can only` 는 능력의 한계를 말한다. 구조상 가장 볼 만한 것은 마지막 문장. `because` 절의 주어가 명사절 `what the 0°/90° suffixes physically mean` 이다. 절 안의 동사는 복수 주어에 맞춰 `mean` 이고 절 전체는 단수로 받아 `isn't confirmed` 다.

**핵심 표현**: `not proven measurement skew` — "증명된 건 아니다"를 `proven` 한 단어로 걸어 둔다. / `Nothing should auto-flag a tool as bad.` — 자동 판정을 금하는 설계 원칙. `flag A as B` 는 "A 를 B 라고 표시하다". / `can only give the day` — 줄 수 있는 것의 한계를 담담하게.

**격식 짝**: (작성)
- refined: Because the data are collected once daily, the precise time of a change cannot be determined; only the date can be reported.
- plain: We only get one reading a day, so we can tell you the day it changed, not the time.

<sub>출처: transcript:skewnono_v3_nuxt (MDC 추가 분석 제안)</sub>
