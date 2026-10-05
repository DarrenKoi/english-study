# 2026-10-06 — 오늘의 표현

- **layered on top of a shared mechanism** — 아래 공용 장치를 고치지 않고 위에 덧댔다는 지적. 뒤에 `that should have been changed instead` 가 붙어 "고쳤어야 할 것은 아래쪽"이 된다.
- **say it is fine where it is** — 검토를 맡기면서 "안 옮겨도 되면 그렇다고 해 달라"고 열어 두는 출구. `where it is` 는 지금 놓인 자리.
- **without the user's say-so** — 허락 없이는. `say-so` 는 "그렇게 하라는 말 한마디"이고 문서에서는 `approval`.
- **visible from the hunk alone** — diff 조각만 보고도 드러나는. `from X alone` 이 검토 범위를 묶는다.
- **dead code the diff leaves behind** — 변경이 남기고 간 죽은 코드. `that` 을 뺀 관계절이고 주어가 diff 라 사람을 탓하지 않는다.
- **parse every document before rendering any output** — `every` 와 `any` 의 대비. 하나라도 틀리면 아무것도 쓰지 않는다.
- **If nothing qualifies, output exactly `(none)`.** — 해당 사항이 없을 때의 답까지 정해 주는 한 줄. `qualify` 는 "기준을 충족하다".

### 오늘의 정독
서브에이전트에게 준 ALTITUDE 리뷰 지시문 여덟 문장. `Block identity is reconstructed in the frontend` 는 수동, `The backend knows the block` 은 능동으로 써서 "다시 짜 맞추는 쪽"과 "이미 아는 쪽"을 태로 갈랐다. `Should the contract carry … instead?` 뒤에는 `Weigh against:` 로 반대 근거까지 스스로 붙인다. 줄인 관계절이 줄줄이 나오는 `/code-review low` 규칙과 명령문·현재형·`must` 가 차례로 바뀌는 구현 계획 머리말도 `reading.md` 에 있다.

### 오늘의 코칭
- 한글→영어: "~하지 않았었나?" → `Didn't we recently put together …?`. / "SQLite는 탈락시키자" → `Let's drop SQLite.` / "3개월치만" → `only the last three months of data`.
- 영어 다듬기: `Don't ask to me` → `Don't ask me`. / `more deep analysis` → `deeper analysis`. / `write down … into a md file` → `write up the results … as a Markdown file`. 카드 17장은 `coaching.md`.

> 처리 항목 30개 / 미뤄진 항목 163개
