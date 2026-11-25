# 2026-11-26 — 정독

세 단락 모두 대화에 실려 온 llm-council 스킬 문서에서 그대로 옮겼습니다. 단락 1은 도구가 왜 있는지와 언제 쓸 만한지, 단락 2는 그 절차의 약한 고리, 단락 3은 익명 심사를 그렇게 짠 까닭을 말합니다. 절차를 설명하면서 단계마다 이유를 붙이는 글이라, 설계 문서를 쓸 때 본으로 삼기 좋아요.

## 단락 1

One model asked once gives one answer, and that answer leans toward however the question was framed. The council counters this: five advisors with deliberately opposed thinking styles answer independently, reviewers judge the answers without knowing who wrote them, and a chairman with no stake in the conversation turns it all into a single recommendation that shows how divided the council was.

A session is nine subagents: about five minutes and, in Claude Code, roughly 600k tokens (mostly per-agent overhead). That is worth it for questions where being wrong is expensive and reasonable people could disagree: a pricing or positioning call, a pivot, an architecture choice that is hard to reverse, "what is weak about this plan/copy/design".

It adds nothing to a question with one right answer, a creation task ("write me a tweet"), or a choice with no real stakes. If asked to council one of those, just answer it and say in a line why the council was skipped.

**문법·구조**: 첫 문장의 주어는 `One model asked once` 입니다. `asked once` 는 과거분사가 뒤에서 꾸미는 꼴로 `that is asked once` 를 줄였어요. `one` 이 세 번(`One model`, `once`, `one answer`) 되풀이되며 "하나뿐"이라는 문제를 박아 둡니다. `however the question was framed` 의 `however` 는 "어떤 식으로든"이라는 관계부사이고, 절 전체가 `toward` 의 목적어입니다. 둘째 문장은 콜론 뒤에 절 셋을 나란히 놓았습니다. 주어가 `five advisors`, `reviewers`, `a chairman` 으로 바뀌고 동사는 모두 현재형이에요. 절차를 순서대로 말하면서도 `first`, `then` 같은 연결어를 하나도 쓰지 않았습니다. 마지막 절의 `that shows how divided the council was` 만 과거(`was`)인 까닭은 권고가 나올 때는 토론이 이미 끝났기 때문입니다. 둘째 단락의 `That is worth it for …` 에서 `That` 은 앞 문장의 비용 전체를 받고, 콜론 뒤 예시 넷은 명사구 셋에 인용문 하나를 섞었습니다. 셋째 단락은 같은 틀을 뒤집어 `It adds nothing to A, B, or C` 로 쓰지 말아야 할 경우를 댑니다. `If asked to council one of those` 는 `If (you are) asked` 에서 주어와 be 동사가 빠진 꼴이고, `council` 을 동사로 돌려 썼습니다.

**핵심 표현**: `counters this` 는 "이 문제에 맞선다". 앞 문장 전체를 `this` 한 낱말로 받아 문제와 해법을 붙였습니다. `with no stake in` 은 "걸린 이해관계가 없는"이고 셋째 단락의 `no real stakes`(잃을 것이 없는)와 같은 낱말의 두 쓰임이에요. `worth it for` 는 "~에는 그 값을 한다"로, 비용을 먼저 숫자로 밝힌 뒤에 쓰여서 설득력이 생깁니다.

**격식 짝** (작성):
- refined: A single query yields a single answer, and that answer is biased by the way the question is posed.
- plain: Ask once and you get one answer, and it leans whichever way you asked.
- refined: The process is justified only where an error would be costly and informed opinion is divided.
- plain: It's only worth doing when getting it wrong would hurt and smart people would argue about it.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/d43a02f6 (llm-council 스킬 문서, 도입부)</sub>

---

## 단락 2

The brief is the council's single point of failure. Every participant except the Outsider reads it, so an omitted option or a baked-in assumption is one the whole council shares, and five advisors will agree on it as confidently as one. Keep it neutral, do not steer, leave out any opinion you voiced earlier in the conversation, and if you narrowed the options or assumed a constraint the user did not state, say so in the brief.

If the question is too vague to brief ("council this: my business"), ask one clarifying question, then proceed.

**문법·구조**: 첫 문장은 은유 하나로 된 짧은 단언이고 둘째 문장이 그 까닭을 풉니다. `so` 가 원인과 결과를 잇고, 이어지는 `and` 가 결과를 하나 더 붙여요. `is one the whole council shares` 에서 `one` 은 앞의 `option` 과 `assumption` 을 받는 대명사이고, 뒤에 목적격 관계대명사가 빠졌습니다. `as confidently as one` 의 `one` 은 다른 것으로 "조언자 한 명"입니다. 같은 낱말이 한 문장에서 두 가지를 가리키니 읽을 때 갈라 봐야 해요. `will agree` 의 `will` 은 미래가 아니라 "으레 그렇게 된다"는 습성을 말합니다. 셋째 문장은 명령문 넷을 쉼표로 늘어놓았습니다. 앞의 셋은 짧고 마지막 하나만 `if` 절을 앞세워 길어요. 이 `if` 절의 동사 `narrowed`, `assumed` 가 과거인 것은 브리프를 쓰기 전에 이미 한 일이기 때문이고, `did not state` 도 같은 때를 가리킵니다. `too vague to brief` 는 `too … to` 구문에 `brief` 를 동사("브리프로 만들다")로 쓴 꼴입니다.

**핵심 표현**: `single point of failure` 는 시스템 용어를 문서에 빌려 쓴 것으로, "여기가 틀리면 전부 틀린다"를 엔지니어에게 한 번에 전합니다. `do not steer` 는 목적어 없이 "방향을 틀지 마라", 곧 결론을 유도하지 말라는 뜻이에요. `say so` 의 `so` 는 앞 절 내용 전체를 받아 "그랬다고 밝혀라"가 됩니다.

**격식 짝** (작성):
- refined: Any assumption embedded in the brief propagates to every participant.
- plain: If the brief gets something wrong, everyone gets it wrong.
- refined: Should you have narrowed the options yourself, disclose that in the brief.
- plain: If you cut the list down yourself, say so.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/d43a02f6 (llm-council 스킬 문서, 질문 틀 잡기)</sub>

---

## 단락 3

This round is what makes the council more than "ask five times". Reviewers see the answers without the advisor names, so they judge the argument rather than defer to a role. Shuffle the answers into numbered files and record the mapping: […]

Three reviewers, not five: every reviewer is the same model with the same instructions, so they tend to agree on which answer is strongest and weakest. Their value is the third question, where each finds different gaps. Give each reviewer a different reading order so no answer benefits from always being read first.

**문법·구조**: 첫 문장 `This round is what makes A more than B` 는 `what` 절을 보어로 둔 강조 구문입니다. "이 단계가 A 를 B 이상으로 만든다"를 평서문보다 힘주어 말해요. 둘째 문장의 `judge … rather than defer` 는 동사 원형 둘을 맞춘 병렬입니다. 둘째 단락은 `Three reviewers, not five:` 처럼 동사 없는 명사구로 열고 콜론 뒤에 까닭을 댑니다. 결정을 먼저 던지고 근거를 붙이는 순서예요. `tend to agree on which answer is strongest and weakest` 에서 `which` 절은 전치사 `on` 의 목적어인 간접의문문입니다. `the third question, where each finds different gaps` 의 `where` 는 장소가 아니라 "그 질문에서는"이라는 뜻으로 추상명사를 받았어요. 마지막 문장 `so no answer benefits from always being read first` 는 목적절인데 `that` 이 빠졌고, `being read` 는 전치사 뒤 수동 동명사입니다. 부사 `always` 가 동명사 앞에 놓인 자리도 눈여겨볼 만합니다. 가운데 `[…]` 자리에는 원문의 셸 명령과 번호 표기 설명이 있어 뺐습니다.

**핵심 표현**: `more than "ask five times"` 는 따옴표로 값싼 대안에 이름을 붙여 놓고 그것과 다르다고 말하는 수법입니다. `defer to` 는 권위에 판단을 넘기는 것. `benefits from` 은 흔히 좋은 뜻이지만 여기서는 "부당하게 덕을 본다"로 쓰여 공정성을 말합니다.

**격식 짝** (작성):
- refined: Anonymization ensures that each response is assessed on its merits rather than on its author's standing.
- plain: Hide the names so people rate what was said, not who said it.
- refined: The reading order is varied so that no response gains an advantage from its position.
- plain: Mix up the order so nobody wins just by going first.

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/d43a02f6 (llm-council 스킬 문서, 상호 검토)</sub>
