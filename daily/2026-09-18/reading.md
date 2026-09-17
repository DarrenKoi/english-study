# 2026-09-18 — 정독

> equipment-data-map 문서와 skewnono Phase 1 계획은 한국어 본문이라 인용할 영어 단락이 없다. 단락 1·2 는 transcript 의 `[assistant]` 영어, 단락 3 은 영어로 쓰인 skewnono Phase B 계획의 Goal·Architecture 를 이어 붙였다. 원문 그대로이며 목록 기호·굵은 글씨·백틱과 항목 머리 라벨(`Goal:`, `Occupancy:` 같은)만 풀어 한 단락으로 이었다.

## 단락 1

So there are three identical copies of the FTP library, and the rule is to change all of them together. If only this repo changed, a later re-copy from skewnono_v3_nuxt or flask_modules would quietly bring back the ZoneInfo import, and Windows would break again. skewnono_v3_nuxt's history shows the earlier ftp_handler fixes were ported the same way (the "vendored sizing" commits). The option you picked also said the fix would go to both other copies. That's the only reason I touched it; nothing in this repo imports from it. If you'd rather not keep it in sync, the commit there (23076eaf) is local and unpushed, so I can undo it with git revert. The catch is that AGENTS.md would then have to drop its "identical copies" claim, and re-copying the library from skewnono_v3_nuxt would no longer be safe.

**문법·구조**: "왜 다른 저장소를 건드렸느냐"는 질문에 답하는 단락이다. 첫 문장의 `So` 는 앞에서 든 증거(파일 주석, AGENTS.md)를 결론으로 묶는다. 둘째 문장은 가정법 과거다. `If only this repo changed` 의 `changed` 는 과거 사건이 아니라 "만약 이 저장소만 바뀌었다면"이라는 가정이고, 주절에 `would` 가 두 번 이어져 결과의 연쇄를 그린다. 여기서 `only` 는 `this repo` 를 꾸미는 말이지 `if only`(~이기만 하면 좋을 텐데)가 아니다. 셋째·넷째 문장은 `shows (that) …`, `said (that) …` 으로 that 을 지운 보고절이며 `said the fix would go` 는 시제 일치로 will 이 would 가 됐다. `That's the only reason I touched it; nothing in this repo imports from it.` 은 세미콜론으로 주장과 그 뒷받침을 한 호흡에 묶었다. 마지막 두 문장은 되돌릴 길을 열어 주고(`If you'd rather not …, I can …`) 곧바로 그 대가를 `The catch is that …` 으로 붙인다. `would then have to drop` 의 `then` 은 "그 경우에는"이다.

**핵심 표현**: `quietly bring back` — 고친 버그가 복사 과정에서 소리 없이 되살아난다. / `That's the only reason I touched it` — 범위를 넘은 행동을 한 줄로 해명하는 틀. / `would no longer be safe` — 지금은 안전하지만 그 선택을 하면 깨진다는 조건부 경고.

**격식 짝**: (작성)
- refined: Were the change confined to this repository, a subsequent re-vendor would silently reintroduce the defect.
- plain: If we only fix it here, the next copy from the other repo brings the bug right back.
- refined: Should you prefer not to keep the copies in sync, the commit can be reverted at no cost, though the documentation would need to be amended accordingly.
- plain: If you don't want them synced, I can just revert it. We'd have to fix the doc, though.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 2

The RCS startup and login code is gone. The script now first checks for a window whose title contains EQP_ID. If there isn't one, it prints "open the tool in RCS first" and exits before doing anything else. That check matters because when the cycle can't find the right window, it treats any other open tool window as a misclick and closes it. So if you had a different tool open, it would have been closed. The script marks the tool as not occupied by anyone else. Without that, the occupancy status stays "unknown", so a successful correction gets reported as unverified. That still sends a cube notification and waits for an engineer who isn't coming.

**문법·구조**: 변경 내용을 "무엇을 했나 → 왜 필요한가 → 안 했으면 어떻게 됐나" 순서로 푼다. 현재형 문장들(`checks`, `prints`, `exits`, `treats`, `closes`)은 코드의 상시 동작을 말하는 시제다. 그 사이에 `So if you had a different tool open, it would have been closed` 가 끼어든다. 조건절은 `have + 목적어 + 보어`(도구를 열어 둔 상태)의 과거형이고 주절은 `would have been closed` 로, 실제로는 일어나지 않은 과거의 사고를 그린다. 엄밀한 가정법 과거완료라면 `had had` 가 와야 하지만 회화체에서는 이렇게 줄여 쓴다. `a window whose title contains EQP_ID` 의 `whose` 는 사물에도 쓰는 소유격 관계사다. `Without that, …` 은 if 절을 전치사구 하나로 줄인 조건 표현이고, `gets reported as unverified` 의 get 수동태는 "원치 않게 그렇게 돼 버린다"는 어감을 보탠다.

**핵심 표현**: `That check matters because …` — 사소해 보이는 검사의 이유를 여는 틀. / `treats A as B` — 시스템이 A 를 B 로 간주한다. / `waits for an engineer who isn't coming` — 오지 않을 사람을 기다린다.

**격식 짝**: (작성)
- refined: In the absence of this flag, the occupancy status remains undetermined, and a successful correction is consequently reported as unverified.
- plain: Without it, the status stays "unknown", so even a good run shows up as unverified.
- refined: Had another tool window been open, the cycle would have closed it as a presumed misclick.
- plain: If you'd had a different tool open, it would've just closed it.

<sub>출처: transcript:[assistant] auto-recipe-creator</sub>

---

## 단락 3

Recipe-search family serves fab-tagged rows with owning-fab detail routing, and live-alarm merges N fac feeds — completing multi-fab support per docs/superpowers/specs/2026-08-07-multi-fab-phase-b-design.md. Catalog rows become (recipe_name, fab_name) pairs end-to-end (contract → mock/office providers → frontend table). Detail screens stay single-fab but receive the owning fab via a fab_name query param while the URL path segment keeps the multi-fab selection. Ranking rows in recipe-tat/fail-issue gain contributing fab_names so their detail links stop assuming fabs[0]. Live-alarm maps selected fabs to distinct fac_ids, refreshes each, merges the boards, and stamps each event with its fab at read time.

**문법·구조**: 구현 계획의 목표·구조 요약이라 전부 현재형이다. 아직 만들지 않은 시스템인데도 will 을 쓰지 않고 "완성된 뒤의 상태"를 사실처럼 적는 것이 설계 문서의 관례다. 동사 선택이 눈에 띈다. `become`, `stay`, `keep`, `gain` 은 모두 상태 변화를 말하는 동사로, 바뀌는 것(`become`, `gain`)과 그대로인 것(`stay`, `keep`)이 짝을 이뤄 독자가 변경 범위를 바로 가른다. `stay single-fab but receive …` 의 `but` 은 "유지하되 이것만 추가"를 잇고, `while` 은 시간이 아니라 대조다. 첫 문장은 관사 없이 `Recipe-search family serves …` 로 시작하는 메모체고, 대시 뒤 분사구 `completing …` 이 앞 절 전체의 결과를 덧붙인다. 마지막 문장은 주어 하나에 동사 넷(`maps, refreshes, merges, and stamps`)을 병렬로 걸어 처리 순서를 그대로 나열했다. `per` 는 "~에 따라"를 뜻하는 문서체 전치사다.

**핵심 표현**: `end-to-end` — 계약부터 화면까지 전 구간. / `stop assuming fabs[0]` — 코드가 깔고 있던 전제를 걷어 낸다. / `stamps each event with its fab at read time` — 저장할 때가 아니라 읽을 때 꼬리표를 붙인다.

**격식 짝**: (작성)
- refined: Detail views remain scoped to a single fab; the owning fab is conveyed as a query parameter, whereas the path segment preserves the full selection.
- plain: The detail page still shows one fab. We pass that fab in the query and leave the path alone.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-07-multi-fab-phase-b.md</sub>
