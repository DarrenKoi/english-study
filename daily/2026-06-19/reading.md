# 2026-06-19 — 정독 단락

---

## 단락 1

An internal, single-user-first **LLM wiki** for a semiconductor-memory manufacturing context. Users drop in screenshots/files/text; the system extracts, organizes, links, retrieves, and (later) drafts reports. Canonical knowledge is human-curated Markdown; all search structures are derived and disposable. If the wiki adds work for the user, it has failed.

**문법·구조**:
- 첫 문장은 동사가 없는 **명사구 정의문**(headline 스타일). 제품 소개·README에서 "이게 뭐냐"를 한 호흡에 던질 때 자주 쓴다. `single-user-first`처럼 `명사-명사-first` 하이픈 합성형용사로 "무엇을 우선하는 설계인지"를 압축.
- 두 번째 문장의 동사 나열 `extracts, organizes, links, retrieves, and (later) drafts` — **현재시제 3인칭 단수**로 시스템의 *항상적 능력*을 기술한다(특정 시점의 동작이 아니라 정의). 괄호 `(later)`는 "지금은 아니고 나중에"라는 로드맵 단서를 문장 흐름을 끊지 않고 끼워 넣은 장치.
- 세 번째 문장은 세미콜론(`;`)으로 **대조 두 절을 한 문장에** 묶었다: 앞절(정본은 사람이 큐레이션한 Markdown) ↔ 뒷절(검색 구조는 파생·폐기 가능). 세미콜론은 "이 둘은 한 쌍의 대비"라는 신호.
- 마지막 문장 `If ..., it has failed.`는 **조건절 + 현재완료**로 목표를 *실패 조건*으로 뒤집어 정의하는 단정형(06-18에도 등장한 이 저자의 시그니처 문형). 현재완료 `has failed`가 "그 순간 이미 실패로 확정"이라는 단호함을 준다.

**핵심 표현**:
- `drop in (screenshots/files/text)` — 격식 없이 "툭 던져 넣다". 입력의 저마찰성을 강조(회화체이지만 제품 카피에 자주).
- `human-curated` — "사람이 직접 선별·정리한". `curated`는 단순 저장이 아니라 *판단이 들어간 정리*를 뜻한다.
- `derived and disposable` — 파생물이라 버려도 되는(↔ canonical). 오늘 표현 카드 참고.

**격식 짝**:
- refined: *Canonical knowledge is human-curated Markdown; all derived search structures are disposable and rebuildable.*
- plain: *The real knowledge lives in Markdown that people write and clean up themselves. The search stuff is just built on top of that — you can wipe it and rebuild it anytime.*

<sub>출처: repo:wiki_for_office (architecture/overview.md, "What this is")</sub>

---

## 단락 2

These decisions came out of a brainstorming session followed by three rounds of adversarial review (Codex): round 1 surfaced external/scope risks (auth, the DRM boundary, home-testability); round 2 caught self-inflicted invariant violations (provenance, prompt-injection, id-as-identity); round 3 caught second-order contradictions introduced by the round-2 fixes (interface drift, the approval-gate-vs-automation tradeoff, citation locators). The design converged where further scrutiny needs implementation code to verify.

**문법·구조**:
- 전체가 **과거시제 서사** — 끝난 검토 과정을 시간 순으로 보고. `came out of`(~에서 나왔다), `surfaced`(드러냈다), `caught`(잡아냈다)로 능동·구체적인 동사를 골라 "무엇이 무엇을 했다"를 또렷이 한다.
- `a brainstorming session **followed by** three rounds ...` — 과거분사 `followed by`가 "그 다음에 ~이 이어졌다"를 *추가 절 없이* 압축. `which was followed by`에서 `which was`를 생략한 형태.
- **콜론(`:`) 뒤 round 1/2/3 병렬 구조**가 핵심. 세 절이 `round N + 동사 + 목적어(괄호로 구체 예시)`로 *완벽히 평행*해서, 검토가 단계마다 *다른 층위의 문제*를 잡았음을 형태만으로 보여준다 — 1차(외부·범위) → 2차(자초한 불변식 위반) → 3차(2차 수정이 *새로 만든* 모순).
- `second-order contradictions introduced by the round-2 fixes` — "수정이 *또* 모순을 낳았다"는 2차 효과를, 과거분사 `introduced by`로 군더더기 없이 수식. 이게 단락의 지적 핵심.
- 마지막 문장 `converged where further scrutiny needs implementation code to verify` — `where`는 장소가 아니라 **"~한 지점/조건에서"**라는 추상적 용법. "더 따져봤자 코드 없이는 검증 못 하는 지점까지 와서 멈췄다" = 설계가 *책상 위에서 갈 수 있는 끝*에 도달했다는 뜻.

**핵심 표현**:
- `surface (a risk)` / `catch (a violation)` — 위험을 *드러내다* / 위반을 *잡아내다*. 리뷰·QA 서사의 동사 짝.
- `self-inflicted` — "자초한(스스로 만든)". 외부 탓이 아니라 우리 설계가 만든 문제라고 솔직히 인정하는 형용사.
- `second-order (contradictions/effects)` — "2차적인(=어떤 조치가 *간접적으로* 낳은)". 1차 수정의 부작용을 가리키는 사고·설계 어휘.

**격식 짝**:
- refined: *Round 2's fixes introduced second-order contradictions, which round 3 then had to resolve.*
- plain: *The round-2 fixes ended up causing new problems of their own, and round 3 had to clean those up.*

<sub>출처: repo:wiki_for_office (architecture/overview.md, "How this was developed")</sub>

---

## 단락 3

The script itself is well-built for 24/7 running — no RAM leak in the code I can see. The expensive work (window capture, pywinauto enumeration, popup threads, PIL images) is edge-triggered: it only runs when a new align-fail appears, not on every 10-second poll. The only thing that grows without bound is the filesystem: every align-fail writes a new timestamped folder, and nothing ever deletes them. So it's safe to run all day from a memory standpoint — but watch disk usage, and verify the real fetcher closes its connections.

**문법·구조**:
- **기술 진단을 회화 톤으로** 푼 단락. `— no RAM leak in the code I can see`처럼 대시(`—`)로 핵심 결론을 덧붙이고, `I can see`(내가 본 한에서)로 *정직한 한정*을 단다. 단정과 겸손을 동시에.
- `is edge-triggered: it only runs when ..., not on every ... poll` — 콜론으로 *용어를 정의*하고, `not on ...`으로 **흔한 오해를 즉시 부정**해 정확도를 높이는 패턴(`X, not Y`).
- `The only thing that grows without bound is ...` — `The only thing that ...` 강조 구문으로 "딱 하나, 이것만 위험"이라고 범위를 좁힌다. 뒤이어 콜론으로 *왜 그런지*(폴더는 쌓이고 지우는 코드는 없음)를 댄다.
- 마지막 문장은 `So ... — but ...` 구조로 **결론 + 단서**를 한 문장에: `safe ... from a memory standpoint`(메모리 관점에선 OK)로 적용 범위를 못 박고, `but watch ...`로 다른 위험(디스크)을 경고. 명령형 `watch / verify`로 행동 권고를 짧게 끝낸다.

**핵심 표현**:
- `edge-triggered` — 상태 변화의 순간에만 발동(↔ 매 주기 폴링). 오늘 표현 카드 참고.
- `grow without bound` — 상한 없이 한없이 커지다(자원 누수 진단어).
- `from a memory standpoint` — 메모리 관점에 한정해서 (보면). 결론의 적용 범위를 좁히는 한정구.

**격식 짝**:
- refined: *From a memory standpoint the loop is safe for continuous operation; the outstanding risks are unbounded disk growth and the unaudited connection handling in the production fetcher.*
- plain: *Memory-wise it's fine to leave running all day — just keep an eye on disk space, and double-check that the real fetcher isn't leaving connections open.*

<sub>출처: transcript (auto_recipe_creator, "하루 종일 돌려도 OOM 안 나나?" 진단)</sub>
