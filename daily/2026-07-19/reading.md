# 2026-07-19 — 정독

## 단락 1

`git ls-files` shows all four (`mock.py`, `office.py`, `contracts.py`, `data.py`) are tracked. So when you evolve a feature, all the changes ride the same commit through GitHub. Office just does `git pull` and gets everything. There is no inherent "home status ≠ office status" — unless **both sides edit the same file independently and both push.** That's the only thing that creates a conflict.

**문법·구조**: 증거 제시(현재형 shows) → 결과 도출(So when you …) → 짧은 단문으로 리듬 전환(Office just does …) 순서의 논증 구조. 넷째 문장은 "There is no X — unless Y" 꼴로, 대시 뒤에 unless 절을 붙여 유일한 예외 조건을 도드라지게 만든다. 마지막 "That's the only thing that creates a conflict"는 that 관계절로 앞 문장 전체를 받아 못을 박는다.
**핵심 표현**: *evolve a feature*(기능을 점진적으로 발전시키다 — change보다 방향성이 있다), *ride the same commit*(한 커밋에 실려 함께 이동하다), *inherent*(구조에 내재된 — 우연이 아니라 필연이라는 뜻).
**격식 짝**: "That's the only thing that creates a conflict"(plain) ↔ "A conflict arises only when both parties modify the same file independently"(refined, 작성). 구어는 that으로 앞말을 받고, 문어는 명사 주어(a conflict)와 only when 절로 압축한다.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/8521af31 (office 어댑터 마이그레이션 설명)</sub>

---

## 단락 2

All 8 tasks shipped earlier today as commits `987fe37` → `795cd2e`, followed by three fix/redesign commits. So this is a retrospective review — the interesting part is where the plan turned out to be wrong or incomplete, since those are lessons for the next plan. The structure held up well: the TDD task ordering executed cleanly with no inter-task rework, the interfaces declared in each task's header matched what downstream tasks consumed, and the `afm`-style provider seam dropped in without friction. The "persist user message BEFORE the LLM call" constraint was the right durability call.

**문법·구조**: 첫 문장은 과거 사실(shipped) 뒤에 과거분사구 "followed by …"를 붙여 사건 순서를 한 문장에 눌러 담는다. 둘째 문장의 "where the plan turned out to be wrong"은 where 명사절로 "틀린 지점"을 통째로 주어부에 넣는 회고 문형. 셋째 문장은 콜론 뒤에 병렬 절 세 개(ordering executed / interfaces matched / seam dropped in)를 나란히 세워 "잘된 점"을 증거 목록으로 제시한다. 마지막 "the right durability call"은 call(판단)을 명사로 쓰는 압축 표현.
**핵심 표현**: *turn out to be wrong*(결과적으로 틀린 것으로 드러나다), *hold up well*(검증을 버텨내다), *the right call*(옳은 판단 — 구어지만 회고 문서에서도 흔하다).
**격식 짝**: "was the right durability call"(plain) ↔ "proved to be the correct decision for durability"(refined, 작성). 구어는 call 한 단어, 문어는 prove to be + 명사구로 푼다.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/461e0fb2 (플랜 회고 리뷰)</sub>

---

## 단락 3

The activity page carries a "SEM List 모델별 사용" card that ranks SEM equipment models by usage. This answers a low-value question — model popularity mirrors fleet size and tells us little about how the application is actually used. The more valuable question is **fab usage**: which fab the traffic comes from, and which pages are frequently activated within that fab. We do not care about individual user/engineer identity in this card.

**문법·구조**: 기능 제거를 설득하는 문제 서술의 정석. 현재형 carries/ranks로 현상을 중립 기술한 뒤, 둘째 문장에서 대시로 근거 두 개(mirrors …, tells us little …)를 병렬로 단다. 셋째 문장은 "The more valuable question is X:" 비교급 주어 + 콜론으로 대안을 세우고, 콜론 뒤 간접의문문 두 개(which fab …, which pages …)가 그 질문의 실체다. 마지막 문장은 non-goal을 단문 현재형으로 선언해 범위를 잘라낸다.
**핵심 표현**: *mirror*(동사: ~를 그대로 반영하다 — 인과가 아니라 동형이라는 지적), *tell us little about*(~에 대해 알려주는 게 거의 없다), *We do not care about X in this card*(범위 제외 선언).
**격식 짝**: "tells us little about how it's actually used"(plain에 가까운 문어) ↔ "offers limited insight into actual usage patterns"(refined, 작성). 전자는 동사 tell로 직설, 후자는 명사화(insight, patterns)로 격식을 올린다.

<sub>출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-16-activity-fab-page-usage-design.md</sub>
