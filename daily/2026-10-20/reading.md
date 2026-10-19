# 2026-10-20 — 정독

## 단락 1
Impact comes before features. Each project leads with the problem and what happens if nothing is done, and the build details come second. A reviewer can then see the business case first. The two strongest points are proof from outside your own work: the award is official recognition from the company, and the MI TF dependency shows another team relies on what you built. That's why both appear in the summary, the KPI cards and the 승격 reasons.

**문법·구조**: 첫 문장은 세 단어짜리 원칙문이고 나머지가 그 원칙을 풀어 준다. 두 번째 문장의 `what happens if nothing is done` 은 명사절이라 `the problem` 과 나란히 `leads with` 의 목적어가 된다. 조건절 속 `is done` 은 수동태인데, 행위자(누가 안 하든)가 중요하지 않아서 그렇다. 세 번째 문장의 `then` 은 시간 순서가 아니라 "그렇게 배치하면 결과적으로"를 뜻하는 결과 부사다. 네 번째 문장은 콜론으로 주장(`two strongest points`)을 먼저 세우고 그 뒤에 예시 둘을 `and` 로 붙인다. 마지막 `That's why …` 가 앞의 이유를 받아 "그래서 문서에 이렇게 배치했다"로 결론을 닫는다. 원칙 → 적용 → 효과 → 근거 → 배치라는 흐름이 다섯 문장 안에 다 들어 있다.

**핵심 표현**:
- `lead with X` — X 로 글·발표를 시작하다. 보고서에서 "무엇을 앞에 둘까"를 말할 때 쓴다.
- `relies on what you built` — 관계대명사 `what` 이 "당신이 만든 것"을 명사로 만든다. `relies on your tool` 보다 범위가 넓다.
- `That's why both appear in …` — 앞 문장들을 근거로 묶어 현재의 배치를 정당화하는 연결 틀.

**격식 짝**:
- refined (작성): Each section opens with the problem and the cost of inaction; implementation details follow.
- plain (작성): I start every project with the problem and what goes wrong if we do nothing, then get into how I built it.

<sub>출처: transcript:pm_notes my-task [assistant]</sub>

---

## 단락 2
Two placeholders need real numbers: how many Align Fail cases are now handled automatically per week and the hours saved, and the MI TF result. I left these blank rather than invent figures. Filling them in would make the strongest claims hard to dispute. The files stay out of git. They contain internal names and the daily-user count, so I followed your existing rule. I added one line to `.gitignore` so the HTML is excluded too. That `.gitignore` edit is the only pending change, and nothing has been committed.

**문법·구조**: 할 일 보고의 전형적인 순서다. 남은 일(`need real numbers`) → 그렇게 한 이유(`rather than invent`) → 채웠을 때의 효과(`would make`) → 다른 주제(git) → 현재 상태. 세 번째 문장은 동명사 주어 `Filling them in` 에 가정의 `would` 를 붙여 "채운다면"을 조건절 없이 표현한다. `The files stay out of git` 의 `stay` 는 상태 유지 동사라 "앞으로도 안 들어간다"까지 함축한다. 마지막 문장은 현재완료 수동 `has been committed` 로 "지금 이 순간까지 커밋된 것 없음"을 확정한다. 단순과거 `was committed` 로 쓰면 이 현재 시점 확인이 약해진다. 이 단락은 문장 대부분이 짧은데, 보고문에서 짧은 문장은 확인 항목처럼 읽힌다.

**핵심 표현**:
- `rather than invent figures` — 하지 않은 선택을 밝혀 빈칸이 의도임을 알린다.
- `stay out of git` — 저장소에 들어가지 않은 상태를 유지한다.
- `the only pending change` — 남은 변경은 이것 하나뿐이라고 범위를 닫는다.

**격식 짝**:
- refined (작성): No changes have been committed; the `.gitignore` update remains the sole pending modification.
- plain (작성): I haven't committed anything yet. The only change waiting is that one `.gitignore` line.

<sub>출처: transcript:pm_notes my-task [assistant]</sub>

---

## 단락 3
Verification: re-download + hash on every file for every target — acceptable, or propose cheaper that is still trustworthy. The handoff admits the "currently running recipe" race is unresolved. Propose the best achievable mitigation without a lock and state the residual risk plainly. Anything in handoff.md that is wrong, contradictory, over-engineered, or missing. Be specific with line references. Keep it tight: numbered findings, each with a one-line recommendation. No restating the handoff.

**문법·구조**: 완전한 문장과 조각문이 섞인 "지시서 문체"다. 첫 문장은 `주제: 현재안 — 판정 요청` 형태로 동사가 없다. 대시가 "이 안에 대해"를, 쉼표 뒤 `or propose` 가 대안 요청을 붙인다. 네 번째 줄(`Anything in handoff.md that …`)도 동사 없는 명사구인데, 앞에서 이어진 질문 목록의 7번 항목이라 "찾아서 알려 달라"가 생략됐다. 관계절 `that is wrong, …` 이 형용사 넷을 받는다. 명령문은 `Propose … and state …`, `Be specific …` 처럼 동사로 시작해 한 줄에 하나씩 요구한다. `each with a one-line recommendation` 은 독립 분사구문(`with` 구)이라 "각 항목마다"를 덧붙이는 구조다. 마지막 `No restating …` 은 금지 표지판 문형이다. 사람에게 보내는 메일이라면 조각문을 완전한 문장으로 풀어 쓰는 게 예의지만, 프롬프트·체크리스트에서는 이 압축이 오히려 명확하다.

**핵심 표현**:
- `the best achievable mitigation without a lock` — 완전한 해결이 없다는 걸 인정한 위에서 최선을 요구한다.
- `state the residual risk plainly` — 대책 뒤 남는 위험을 돌려 말하지 말 것.
- `Be specific with line references.` — 주장마다 줄 번호를 달라는 리뷰 요청의 단골 문장.

**격식 짝**:
- refined (작성): Where a complete fix is not possible, please describe the most effective mitigation available and explicitly state the risk that remains.
- plain (작성): If there's no real fix, tell me the best workaround and just say what could still go wrong.

<sub>출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md</sub>
