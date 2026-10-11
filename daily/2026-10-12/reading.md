# 2026-10-12 — 정독

> 세 단락 모두 배치 원문이다. 단락 1은 e-beam 페이지 현황 노트 3장의 Inferences 세 항목과 Gaps 첫 항목을 이어 붙였고 항목 머리의 `(inference)` 표지만 뺐다. 단락 2는 skewnono 세션에서 어시스턴트가 낡은 인용을 지운 뒤 낸 보고의 앞부분이다. 원문에서 목록으로 나뉜 세 건 가운데 첫 건만 문장으로 이어 옮겼다. 단락 3은 히트맵 라벨 수정 보고이고 변경 두 가지를 적은 목록은 뺐으며 끝 문장은 같은 답의 Insight 에서 왔다. 1은 관찰에서 원인을 끌어내고 자기 조사의 한계를 적는 글, 2는 "대부분은 이랬고 세 건은 달랐다"로 변경을 요약하는 글, 3은 고친 것과 확인 못 한 것을 갈라 적는 글이다.

## 단락 1

The thin pages are thin **because** their office source is a current snapshot with no history (sem_list roster, storage collector, idp_ver current version), **not because** analysis was skipped; adding trend to them needs new collection, which the owner **has so far declined** for storage. Export is uneven within one page family: on H/W 관리 only two of seven panels export, and the three pages a shift engineer **would most want to hand over from** (라이브 알람, 측정 이력, TTTM) have no export at all. Because most pages keep filters in memory or localStorage rather than the URL, a finding on those pages cannot be shared as a link. Only recipe detail, recipe search, H/W 관리 and Recipe 현황's tab can. The matrix cells marked N are "not found by the grep patterns used", **not proofs of absence**; a control case was run for exports and `route.query`, but not for every column.

**문법·구조**: 첫 문장의 뼈대는 `A is B because X, not because Y` 다. 독자가 떠올릴 법한 오해(분석을 빼먹었다)를 `not because` 로 먼저 치우고 진짜 원인을 남긴다. 세미콜론 뒤 `adding trend to them needs new collection` 은 동명사구가 주어이고 `which` 는 바로 앞 명사 `new collection` 을 받는 계속적 용법이다. `has so far declined` 는 현재완료에 `so far` 를 끼워 "지금까지는"이라는 여지를 둔다. 둘째 문장은 콜론 앞에서 주장(`uneven`)을 하고 콜론 뒤에서 숫자 둘로 증명한다. `the three pages (that) a shift engineer would most want to hand over from` 은 전치사 `from` 이 문장 끝에 남은 관계절이다. `would` 는 실제 조사한 사실이 아니라 글쓴이의 짐작이라는 표시다. 셋째 문장은 `Because …` 종속절을 앞세워 원인에서 결과로 흐르고 넷째 문장 `Only … can.` 은 동사구 `be shared as a link` 를 통째로 생략했다. 긴 문장 뒤에 세 단어짜리 술부가 와서 예외가 또렷해진다. 마지막 문장은 수동태 둘(`are … not found`, `was run`)로 조사 행위를 적는다. 누가 했는지보다 무엇을 했고 안 했는지가 중요한 자리여서 수동이 맞다.

**핵심 표현**: `not because analysis was skipped` — 원인 하나를 명시적으로 배제하는 틀. / `Export is uneven within one page family` — "들쭉날쭉하다"를 `uneven` 한 단어로. / `not proofs of absence` — "못 찾았다"와 "없다"를 가르는 조사 보고의 단골 단서.

**격식 짝**: (작성)
- refined: The absence of trend views on these pages reflects a limitation of the data source rather than an omission in the analysis.
- plain: Those pages don't have trends because the data has no history, not because someone forgot to build them.
- refined: A finding on such a page cannot be shared as a link, since its filters are not held in the URL.
- plain: You can't send someone a link to what you found there. The filters aren't in the URL.

<sub>출처: repo:skewnono_v3_nuxt docs/research/2026-10-09-analysis-service-directions-notes/ebeam_pages_current_state.md</sub>

---

## 단락 2

The stale citations are gone: pushed as `1f4254dc`, 20 files, worktree torn down. No path to a deleted doc remains in tracked files; ruff, markdown lint and eslint on the touched files pass, and I did not run pytest or the frontend tests **since** the changes are comments and docs only. Most edits just drop the pointer, or the sentence **that existed only to carry it**. Three **went further than** a deletion. `backend/ebeam/fail_issue/MIGRATION.md` pointed at the deleted spec's §9.2 for how to tune `FAIL_INDEX_CEIL` / `FAIL_INDEX_FLOOR` at the office. I inlined three of its four checks in condensed form **rather than lose them**. The fourth, the mixed-fab bias check, is left out. The count grew from the 17 I reported earlier because the search also caught `measHistQuery.ts` (citing a spec that was already missing) and two tracked tickets under `.scratch/sk-bad-sweep/`.

**문법·구조**: 첫 문장은 결과를 먼저 말하고 콜론 뒤에 동사 없는 명사구 셋을 쉼표로 늘어놓은 메모 문체다. `worktree torn down` 은 `the worktree has been torn down` 에서 관사와 조동사를 뗀 꼴이다. 둘째 문장은 세미콜론으로 두 가지를 가른다. 앞은 지금의 상태(`remains`, 현재), 뒤는 한 일과 안 한 일(`pass` 현재, `did not run` 과거)이다. 안 돌린 테스트를 숨기지 않고 `since` 절로 이유를 붙였는데, `because` 보다 `since` 가 "당연히 알 만한 이유"를 가볍게 대는 말투다. 셋째·넷째 문장은 `Most … / Three …` 로 일반과 예외를 맞세운다. 예외를 설명하는 다섯째 문장부터 시제가 다시 갈린다. 지운 문서가 예전에 하던 일은 과거(`pointed at`), 내가 한 조치도 과거(`inlined`), 지금 남은 상태는 현재 수동(`is left out`)이다. `rather than lose them` 은 주절이 과거여도 동사원형을 쓴다. 마지막 문장은 `the 17 (that) I reported earlier` 로 앞선 보고와 숫자가 달라진 이유를 먼저 나서서 설명한다. `citing …` 과 괄호 속 `that was already missing` 이 발견 경위를 덧붙인다.

**핵심 표현**: `No path to a deleted doc remains in tracked files` — 부정 주어 `No … remains` 로 "하나도 안 남았다"를 단정한다. / `Three went further than a deletion` — 단순 삭제가 아닌 건을 따로 꺼내는 머리말. / `The count grew from the 17 I reported earlier because …` — 앞서 말한 숫자와 어긋나는 점을 먼저 해명한다.

**격식 짝**: (작성)
- refined: Three of its four checks were inlined in condensed form so that they would not be lost; the fourth has been omitted.
- plain: I copied three of the four checks in, shortened, so we don't lose them. I skipped the fourth.

<sub>출처: transcript:skewnono-v3-nuxt [assistant]</sub>

---

## 단락 3

Fixed and pushed (`d8f10e11`): the Chuck 온도 heatmap now shows every tool name on the y-axis, including the bottom row. The chart was in a fixed 320px box, **so once** enough tools were selected ECharts **silently dropped** labels that would overlap, starting from the bottom. Checked in the browser on CD-SEM · R3 with 14 tools selected (screenshot above): all 14 names render. I did not reproduce the missing label before the change, so the cause is **inferred from the code rather than observed**. 22px per row is tighter than the 30px the ranking charts use, because heatmap cells need no room for markers — it keeps a 19-tool fab at roughly 490px instead of 640px.

**문법·구조**: 다섯 문장이 "결과 → 원인 → 검증 → 한계 → 설계 근거" 순서다. 첫 문장과 셋째 문장은 주어 `I` 를 뗀 과거분사로 시작한다(`Fixed and pushed`, `Checked in the browser`). 커밋 메시지와 작업 보고에서 흔한 생략이다. 첫 문장의 `now shows` 는 고친 뒤의 현재 상태이고 `including the bottom row` 가 사용자가 짚은 바로 그 증상을 되받는다. 둘째 문장은 과거 시제로 원인을 설명한다. `so once enough tools were selected` 에서 `once` 는 "~하자마자, 일단 ~하면"이라는 접속사이고 `labels that would overlap` 의 `would` 는 과거 시점에서 본 가정(그리면 겹쳤을 라벨)이다. `starting from the bottom` 은 분사구로 어느 쪽부터 사라졌는지를 덧붙인다. 넷째 문장이 이 보고의 핵심이다. `I did not reproduce …, so the cause is inferred …` 로 과거 사실에서 현재 판단의 지위를 끌어낸다. 마지막 문장은 비교급 `tighter than the 30px (that) the ranking charts use` 에 관계절이 숨어 있고 대시 뒤에서 그 선택의 효과를 숫자로 보여 준다.

**핵심 표현**: `silently dropped labels that would overlap` — 에러 없이 빼 버렸다는 뜻의 `silently drop`. / `the cause is inferred from the code rather than observed` — 근거의 등급을 스스로 낮춰 적는 한 줄. / `need no room for markers` — `need no X` 는 `don't need any X` 의 문어형.

**격식 짝**: (작성)
- refined: The root cause was not reproduced prior to the change and is therefore inferred from the code rather than observed.
- plain: I never actually saw the bug happen before I fixed it, so the cause is my best guess from reading the code.

<sub>출처: transcript:skewnono-v3-nuxt [assistant]</sub>
