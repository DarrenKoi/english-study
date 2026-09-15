# 2026-09-16 — 정독

> repo 문서는 영어 인용이 한국어 문장 사이에 끼어 있어 단락으로 떼어 읽기 어렵다. 그래서 세 단락 모두 transcript 의 `[assistant]` 영어에서 골랐다. 원문 그대로이며, 불릿과 굵은 글씨만 풀어 한 단락으로 이었다.

## 단락 1

My opinion of the doc: the research itself is solid. Sources are pinned to versions, the token math is right, and it correctly refuses to let Qwen touch coordinates, OCR, or Outcome rules. Its weakness is that it hedges in every section but never commits to the one thing a reader needs: where Qwen would actually change an outcome. Three gaps, now fixed in the file: Value is in the tail, not the happy path. The CV loop already handles "unique key found, OK clicked" deterministically. Qwen only matters for Episodes that currently end in `escalated_*`, `engineer_review`, Guard `unknown`, or unexpected popups. I added this to §1 and marked the two §3.1 table rows where Qwen adds nothing as control cases only.

**문법·구조**: 남의 문서를 평가하는 단락이라 칭찬 → 약점 → 수정 내역 순서로 흐른다. 첫 문장의 재귀대명사 `itself` 는 "연구 자체는"이라고 칭찬 범위를 좁혀, 뒤에 올 비판이 연구가 아니라 서술 방식을 겨눈다는 걸 미리 알린다. 둘째 문장은 세 항목을 나열하는데 수동태(`are pinned`), be + 형용사(`is right`), 능동태(`refuses to let Qwen touch`) 로 형태가 다 다르다. `let + 목적어 + 동사원형` 도 여기 있다. 셋째 문장 `Its weakness is that …` 은 명사절을 보어로 세운 틀이고, 콜론 뒤 `where Qwen would actually change an outcome` 은 간접의문 명사절이다. `would` 는 아직 시험 전이라 가정으로 말한 것이다. `Three gaps, now fixed in the file:` 은 동사 없이 명사 + 과거분사 후치수식으로 목록을 연다. 시제도 갈린다. 문서와 시스템의 상태는 현재형(`handles`, `matters`)으로, 자기가 한 수정은 과거형(`added`, `marked`)으로 적었다. 마지막 문장은 `mark A as B` 사이에 `where Qwen adds nothing` 관계부사절이 끼어 A 가 길어진 경우다.

**핵심 표현**: `the research itself is solid` — 칭찬할 대상을 좁혀 비판과 섞이지 않게 한다. / `hedges in every section but never commits to` — 단서만 달고 결론을 피하는 글을 한 줄로 요약. / `mark A as control cases only` — 평가에서 비교 기준으로만 쓸 항목을 표시.

**격식 짝**: (작성)
- refined: While the research is rigorous, the document stops short of stating where the model would materially change an outcome.
- plain: The research is good, but it never says where Qwen would actually make a difference.

<sub>출처: transcript:auto-recipe-creator (Qwen 조사 문서 검토 의견)</sub>

---

## 단락 2

Stop sending a visible-but-ambiguous key to search-around. In `key_visibility_gate`, keep `low` as the only path to fallback. Route `adjust` without `distinctive` to `engineer_review` instead of `fallback_search`. That matches the engine's own contract that `distinctive` is advisory, and it reuses the isolation tier that is already wired to `settings.reregister_second_ratio_threshold`. Search-around exists for "nothing in view". A score of 0.533 is not nothing in view, and panning away from a key you can see is the worst of the three outcomes. This is a one-line change plus two test edits in `test_correction.py`. No env switch, git revert is the rollback.

**문법·구조**: 권고문이다. 앞 세 문장이 모두 명령문(`Stop -ing`, `keep A as B`, `Route A to B instead of C`)이라 할 일이 행동 단위로 떨어진다. `stop sending` 은 "보내기를 그만두라"이고 `stop to send` 는 "보내려고 멈추라"라서 뜻이 다르다. `visible-but-ambiguous` 는 세 단어를 하이픈으로 묶은 복합형용사다. 넷째 문장에는 `that` 이 두 번 나오는데 역할이 다르다. `the engine's own contract that distinctive is advisory` 의 `that` 은 동격(contract 의 내용), `the isolation tier that is already wired to …` 의 `that` 은 관계대명사다. `that` 뒤가 완전한 절인지 주어가 빠진 절인지로 구분한다. 다섯째 문장은 인용구 `"nothing in view"` 로 기능을 정의하고, 여섯째 문장에서 그 인용구를 명사처럼 받아 `is not nothing in view` 로 반박한다. 같은 문장 후반은 동명사 주어 `panning away from a key you can see`(접촉 관계절 포함)를 세웠다. 마지막 두 문장은 비용(`a one-line change`)과 되돌리기(`the rollback`)로 위험이 작다는 걸 보여 주며 끝낸다.

**핵심 표현**: `keep X as the only path to Y` — 경로를 하나로 좁히는 설계 지시. / `A is not nothing in view` — 상대 규칙의 표현을 그대로 가져와 반박하는 수사. / `git revert is the rollback` — 롤백 장치가 따로 필요 없다는 안심.

**격식 짝**: (작성)
- refined: A visible but ambiguous key should be escalated for engineer review rather than trigger a search.
- plain: If you can see the key but can't tell which one it is, hand it to an engineer. Don't go searching.

<sub>출처: transcript:auto-recipe-creator (align gate 권고)</sub>

---

## 단락 3

No, I did not. My notes and the engineer guide both assume the model folder is a git copy of the hub that pulls updates. Your actual setup is a plain copy-paste of the repo folder, which is why the merge script and the git reset were the wrong answers. With that workflow the restart is just: pull in the hub, then in the qwen3 folder delete everything except `.venv`, `.env` and `equipment.toml`, paste the hub contents back in minus `.git` and `out/`, and recreate `office/progress.md` with the header line. The Python script from my last message does exactly that, so it still fits. Nothing else is needed. Let me record this so I stop assuming git in the model folders.

**문법·구조**: 잘못 알고 있던 전제를 인정하는 답변이다. 사용자의 `do you know that?` 에 `No, I did not.` 로 답했는데, 현재형 질문을 과거형 대동사 `did` 로 받아 "(지금 들을 때까지) 몰랐다"는 뜻을 만든다. 둘째 문장은 `assume` 뒤 `that` 이 생략된 명사절 안에 다시 `that pulls updates` 관계절이 들어간 이중 구조다. 셋째 문장의 `, which is why …` 는 앞 절 전체를 받아 결과를 잇는 계속적 용법이고, `were the wrong answers` 는 이미 내놓은 답을 과거형으로 평가한다. 넷째 문장은 `the restart is just:` 뒤에 명령형 동사 네 개(`pull`, `delete`, `paste`, `recreate`)를 나열해 절차를 한 문장에 담았다. `minus` 는 "~을 빼고"라는 전치사로 쓰였다. `does exactly that` 의 `that` 은 앞 절차 전체를 가리킨다. 마지막 문장 `Let me record this so I stop assuming …` 은 `stop + 동명사`에 `so (that)` 목적절을 붙여 재발 방지를 약속한다. 인정 → 원인 → 올바른 절차 → 재발 방지 순서를 그대로 빌려 쓰면 사과문이 짧고 단단해진다.

**핵심 표현**: `which is why X were the wrong answers` — 잘못의 원인을 한 절로 인정. / `does exactly that, so it still fits` — 기존 결과물이 여전히 유효하다고 확인. / `so I stop assuming X` — 같은 실수를 반복하지 않겠다는 마무리.

**격식 짝**: (작성)
- refined: I was not aware of that; my earlier recommendations rested on the assumption that each model folder was a git clone.
- plain: I didn't know that. I assumed the folders were git clones, so I gave you the wrong fix.

<sub>출처: transcript:equipment-data-map (재시작 절차 대화)</sub>
