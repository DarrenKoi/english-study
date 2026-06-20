# 정독 — 2026-06-18

오늘은 배치에 양질의 영어 단락이 풍부해, 모두 **원문 인용**으로 골랐습니다. 설계문서 영어의 두 가지 전형 — (1) 무엇인지 *단정적으로 정의*하는 단락, (2) 어떻게 만들어졌는지 *과거 시제로 서술*하는 단락 — 을 짝지어 봅니다.

---

## 단락 1

An internal, single-user-first **LLM wiki** for a semiconductor-memory manufacturing context. Users drop in screenshots/files/text; the system extracts, organizes, links, retrieves, and (later) drafts reports. Canonical knowledge is human-curated Markdown; all search structures are derived and disposable. If the wiki adds work for the user, it has failed.

**문법·구조**
- **명사구 한 방으로 정의**: 첫 문장엔 동사가 없습니다(`An internal … LLM wiki for …`). 설계문서·제품소개에서 "이건 X다"를 압축할 때 흔한 *headline noun phrase* — 형용사를 앞에 쌓아(`internal, single-user-first`) 한 줄로 정체성을 못 박습니다.
- **세미콜론(`;`)의 역할**: `Users drop in …; the system extracts …` — 마침표보다 가깝고 쉼표보다 먼, *대등한 두 절*을 잇습니다. 한국어 "사용자는 ~하고, 시스템은 ~한다"의 대구를 영어에서 세미콜론으로 살린 것.
- **현재시제 = 변하지 않는 사실/사양**: `extracts, organizes, links, retrieves` 모두 단순현재. 매뉴얼·사양서는 "지금 일어나는 일"이 아니라 "항상 그러함"을 말하므로 현재시제가 기본값입니다.
- **수동+형용사로 속성 규정**: `is human-curated`, `are derived and disposable` — 행위자보다 *성질*에 초점. "누가 만들었나"가 아니라 "사람이 큐레이션한 것 / 파생이고 버려도 되는 것"임을 규정.
- **마지막 문장의 현재완료 단정**: `If … it has failed.` → ["If the wiki adds work…"](new-expressions.md) 참고. 목표를 *반대 상황으로* 정의하는 닫는 문장.

**핵심 표현**
- **drop in (screenshots/files)** — "툭 던져 넣다"(저마찰 입력). 구어적이라 사용자 행동 묘사에 잘 맞음.
- **human-curated** — "사람이 직접 선별·관리한". `auto-generated` 의 반대 축.
- **derived and disposable** — "파생이라 언제든 버리고 다시 만드는". canonical(정본) ↔ derived(파생)의 대조 축.

**격식 짝** — "이 데이터는 언제든 다시 만들면 된다"
- refined (문어): *All search structures are **derived and disposable**, rebuildable from the canonical store at any time.* (작성)
- plain (회화): *Don't worry about the index — **we can just rebuild it** from the source whenever.* (작성)

<sub>출처: repo:wiki_for_office (docs/architecture/overview.md, "What this is")</sub>

---

## 단락 2

These decisions came out of a brainstorming session followed by three rounds of adversarial review (Codex): round 1 surfaced external/scope risks (auth, the DRM boundary, home-testability); round 2 caught self-inflicted invariant violations (provenance, prompt-injection, id-as-identity); round 3 caught second-order contradictions introduced by the round-2 fixes (interface drift, the approval-gate-vs-automation tradeoff, citation locators). The design converged where further scrutiny needs implementation code to verify.

**문법·구조**
- **과거시제 = 끝난 과정의 서술**: `came out of`, `surfaced`, `caught`. 단락 1(사양·현재)과 정반대로, "어떻게 만들어졌나"는 *완료된 사건*이라 과거시제. 같은 문서 안에서도 **설명하는 대상에 따라 시제가 갈린다**는 게 핵심.
- **`followed by` (과거분사 후치수식)**: `a session followed by three rounds …` = "~에 뒤이은". `which was followed by` 를 줄인 형태로, 절차의 순서를 명사구 안에 압축.
- **콜론+세미콜론으로 목록 구조화**: 콜론(`:`) 뒤에 `round 1 …; round 2 …; round 3 …` 세 절을 세미콜론으로 병렬. 각 절 안에 다시 괄호로 예시를 묶어 *3단 계층*(전체 → 라운드 → 예시)을 문장부호만으로 만듭니다.
- **수동·분사로 인과 압축**: `contradictions introduced by the round-2 fixes` — "round-2 수정이 만들어낸 모순". 관계절(`that were introduced`) 대신 과거분사 후치로 군더더기 제거.
- **`where` 의 추상적 용법**: `converged where further scrutiny needs …` 의 `where` 는 장소가 아니라 *지점/상황*("~한 지점에서"). 추상 명사 뒤 `where` 는 격식 영어의 단골.

**핵심 표현**
- **surface (a risk) / catch (a violation)** — "리스크를 드러내다 / 위반을 잡아내다". 리뷰 서술의 동사 쌍.
- **self-inflicted** — "자초한, 스스로 만든"(self-inflicted invariant violations = 우리가 정한 불변식을 우리가 어긴 것).
- **second-order (contradictions)** — "이차적인"(어떤 수정이 *부수적으로* 낳은). first-order(직접) ↔ second-order(파생).

**격식 짝** — "그 수정 때문에 새 문제가 생겼다"
- refined (문어): *Round 3 caught **second-order contradictions introduced by** the round-2 fixes.* (원문)
- plain (회화): *Turns out fixing round 2 **broke a few other things** — that's what round 3 picked up.* (작성)

<sub>출처: repo:wiki_for_office (docs/architecture/overview.md, "How this was developed")</sub>
