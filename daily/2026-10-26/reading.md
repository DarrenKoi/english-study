# 2026-10-26 — 정독

## 단락 1

Lot ID search works; lot code search does not exist, because AFM rows carry no lot code field at all.

**Lot ID:** the search bar matches the typed text against the lot ID, along with filename, recipe name, date, slot and measured info. It is a case-insensitive substring match, so `t7hqr` finds every lot starting `T7HQR` (9 of the 36 mock rows for MAP608). The "결과 내 필터" box uses the same fields. This matching came through the rewrite unchanged. I confirmed this from the code and the live mock data, not by typing a lot ID into the page.

**문법·구조**: 첫 문장이 질문 두 개에 대한 결론을 세미콜론 하나로 나란히 놓는다. 이유는 because 절 하나로 끝내고 세부는 다음 단락으로 미뤘다. 본문은 모두 **현재 시제**다. 검색이 지금 이렇게 동작한다는 사실 서술이라 그렇다. 반면 "came through the rewrite unchanged" 와 "I confirmed" 만 과거형인데, 리라이트와 확인은 이미 끝난 사건이기 때문이다. `so t7hqr finds …` 의 so 는 앞 규칙(대소문자 무시·부분 일치)에서 바로 나오는 결과를 잇는다. 마지막 문장의 "from A, not by B" 는 무엇으로 확인했고 무엇으로는 안 했는지를 대비해 확인 범위를 정직하게 밝힌다.

**핵심 표현**:
- `along with` — 주된 대상(lot ID) 뒤에 부가 항목을 덧붙일 때. "A, along with B and C" 꼴이면 A 가 중심이다.
- `came through (the rewrite) unchanged` — 큰 변경을 거치고도 그대로 살아남았다. come through 는 '무사히 통과하다'.
- `not by typing …` — 실제로 해 보지 않은 검증 방법을 밝혀 두는 말.

**격식 짝**:
- refined (작성): The matching logic was carried over from the previous implementation without modification.
- plain (작성): The search works the same as before the rewrite.

<sub>출처: transcript:skewnono-v3-nuxt (AFM 검색 질문에 대한 답)</sub>

---

## 단락 2

**Lot code:** the only lot field in the AFM contract (`backend/afm/contracts.py`) is `lot_id`. There is no `lot_cd`, so there is nothing for the search to match against. Typing a lot code only hits if it happens to be a substring of the lot ID or the filename.

**Scope:** the search is client-side only. It filters whatever list `GET /api/afm/files?tool=…` returned; the backend takes no query. So a lot that isn't in that returned list can't be found, which will matter once the office adapter returns a bounded window of files.

If you want lot code search, I need to know one thing about the office AFM data: is the lot code a separate field, or derivable from the lot ID (e.g. a prefix)? If it is derivable, it is a small frontend change. If it is a separate field, it has to be added to the contract, the mock and `docs/datatables` first.

**문법·구조**: "없다 → 그래서 지금은 이렇다 → 앞으로 이게 문제다 → 진행하려면 이게 필요하다" 순서로 흐른다. `nothing for the search to match against` 는 'for + 의미상 주어 + to 부정사'에 전치사 against 가 끝에 남은 꼴이다. `whatever list … returned` 의 whatever 는 '무엇이든 돌아온 그 목록'이라 백엔드 응답을 그대로 받는다는 점을 강조한다. `which will matter once …` 는 앞 문장 전체를 받는 계속적 용법 which 에 미래 조건 once 를 붙였다. 마지막 두 문장은 **If 조건문을 쌍으로** 세워 두 경우의 작업량을 대비하고, 두 번째 쪽은 수동태 `has to be added` 로 누가 하든 해야 할 일임을 드러낸다.

**핵심 표현**:
- `only hits if it happens to be …` — 우연히 맞을 때만 검색에 걸린다.
- `which will matter once …` — 지금은 괜찮지만 조건이 바뀌면 문제가 된다고 미리 짚는다.
- `I need to know one thing: …?` — 다음 작업 전 질문을 하나로 좁힌다.

**격식 짝**:
- refined (작성): Before proceeding, I would need to confirm whether the lot code is stored as a separate field or derived from the lot ID.
- plain (작성): Quick question before I start: is the lot code its own field, or can we get it from the lot ID?

<sub>출처: transcript:skewnono-v3-nuxt (같은 답의 후반부)</sub>

---

## 단락 3

The AFM pages are now aligned to `DESIGN.md` and about 825 lines lighter (32 files, +1116 / −1941). It is pushed to `main` as `88d757b1`, and the worktree is torn down.

Lint, typecheck and the frontend tests (1845) pass. I drove all four AFM pages and the landing card in a browser (search, grouping, save dialog, point switching, image lightbox, the comparison chart, light mode) with no console errors. Pure display changes such as tooltip escaping I did not exercise by hand.

Codex and opencode each got a read-only brief in the Herdr panes you already had open: Codex on `DESIGN.md` conformance and bugs, opencode on dead code and duplication. I read the same code in parallel and reconciled the three. Codex then did a second correctness pass over the finished diff, which found three real regressions that I fixed before merging.

**문법·구조**: 첫 두 문장은 **현재형 수동태**(`are aligned`, `is pushed`, `is torn down`)로 지금 상태를 보고한다. 행위자보다 결과가 중요해서다. 둘째 단락부터 `I drove`, `I read` 처럼 과거형 능동태로 바뀌며 무엇을 했는지 서술한다. `Pure display changes … I did not exercise by hand` 는 목적어를 문두로 뺀 **도치(topicalization)**라서 '이 부분만은 직접 안 돌려 봤다'는 예외가 또렷이 선다. 셋째 단락의 콜론 뒤 `Codex on …, opencode on …` 은 반복되는 동사 got a brief 를 생략한 병렬 구조다. 마지막 `which found …` 는 계속적 관계절로 두 번째 검토의 결과를 이어 붙였고, 그 안에 다시 `that I fixed` 제한적 관계절이 들어 있다.

**핵심 표현**:
- `about 825 lines lighter` — 리팩터링 결과를 무게처럼 말한다.
- `did not exercise (X) by hand` — 수동 검증에서 뺀 부분을 밝힌다.
- `reconciled the three` — 세 리뷰 결과를 대조해 하나로 맞췄다.

**격식 짝**:
- refined (작성): The three independent reviews were reconciled into a single set of changes.
- plain (작성): I compared all three reviews and merged what they found.

<sub>출처: transcript:skewnono-v3-nuxt (AFM 페이지 리뷰·정리 완료 보고)</sub>
