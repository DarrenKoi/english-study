# 2026-09-12 — 정독

## 단락 1

**Agent = Model + Harness.** The harness is all the code around the model: the loop, tools, context handling, permissions, checks, state and tracing. The model supplies the intelligence; the harness turns it into work you can trust. The model is the part you can't change, so most quality differences come from the harness. LangChain went from outside the top 30 to the top 5 on Terminal Bench 2.0 by changing only its harness, with the same model.

**문법·구조**: 첫 문장은 등식 하나로 주제를 던진다. 둘째 문장의 **콜론(:)** 뒤에는 앞의 `all the code around the model` 이 구체적으로 무엇인지 늘어놓는다. 콜론은 "즉 다음과 같다"를 기호 하나로 처리한다.

셋째 문장은 **세미콜론(;)** 으로 두 절을 저울처럼 맞세웠다. `The model supplies …; the harness turns …` 는 주어·동사·목적어 틀이 같아서 역할 분담이 한눈에 대비된다. `and` 로 이으면 이 긴장감이 풀린다.

관계대명사 생략이 두 번 나온다. `work (that) you can trust`, `the part (that) you can't change`. 목적격이라 빼도 되고 구어·기술 글에서는 빼는 쪽이 더 흔하다.

마지막 문장은 근거 사례다. `went from X to Y` 로 변화의 폭을 보여주고 `by changing only its harness` 로 수단을 댄다. 끝의 `with the same model` 은 쉼표로 떼어 덧붙였는데, 이 짧은 구가 "변수는 하네스 하나"라는 통제 조건을 못박아 주장 전체를 받친다.

**핵심 표현**
- **turn A into B** — A 를 B 로 바꿔 놓다. 원료와 결과물을 대비할 때 쓴다: 지능이라는 원료가 믿을 수 있는 작업이 된다.
- **the part you can't change** — 통제 밖 변수를 명사구 하나로 가리킨다. 뒤에 `so …` 가 붙으면 "그러니 바꿀 수 있는 쪽에 힘을 써라"가 된다.
- **went from outside the top 30 to the top 5** — 순위 변화를 `from … to …` 로 보여준다. `outside the top 30` 처럼 범위 밖을 가리키는 표현이 요긴하다.

**격식 짝**
- refined: *Because the model itself is fixed, variation in output quality is largely attributable to the surrounding harness.* (작성)
- plain: *You can't change the model, so the harness is where the wins are.* (작성)
- refined: *The model provides the capability; the harness renders that capability dependable.* (작성)
- plain: *The model's the brains. The harness is what makes it reliable.* (작성)

<sub>출처: transcript:-Users-daeyoung-Codes-pm-notes (assistant)</sub>

---

## 단락 2

**My recommendation is to leave it as is.** Picking only what you choose is the behavior you asked for, and new tools are rare. The count still shows that a tool isn't picked. The fix would be to bring back a separate "all tools" value just for 전체 선택. That means two kinds of saved selection again, which is what this change removed. If new tools do join fabs often enough that people might miss them, say so and I'll add that back. I haven't changed any code.

**문법·구조**: 리뷰 결과를 받고 결정을 권하는 단락이다. **결론을 첫 문장에** 두고 근거 → 대안 → 대안의 비용 → 재검토 조건 → 현재 상태 순으로 간다. 영어 업무 글의 표준 흐름이다.

둘째 문장의 주어는 동명사구 `Picking only what you choose` 다. 행동 자체를 주어로 세웠고 그 안에 명사절 `what you choose` 가 들었다.

넷째 문장의 `The fix would be to …` 에서 **would** 가 중요하다. 하지 않기로 한 선택지를 가정으로 제시하는 법이다. `The fix is to …` 라고 쓰면 당장 고치자는 말로 읽힌다.

다섯째 문장 끝 `, which is what this change removed` 의 `which` 는 앞 절 전체("저장 형태가 다시 두 가지가 된다")를 받는다. 쉼표 뒤 계속적 용법이라 정보를 덧붙이는 느낌이다.

여섯째 문장의 `do join` 은 **강조의 do** 다. "혹시 정말로 자주 추가된다면"이라는 가능성을 부각한다. `often enough that …` 은 정도 + 결과 구문이고, 명령문 `say so` 에 `and I'll …` 을 이어 조건부 약속을 만들었다. 마지막 `I haven't changed any code.` 는 현재완료로 지금 상태를 보고하며 닫는다.

**핵심 표현**
- **leave it as is** — 현 상태 그대로 두다. 권고의 결론으로 딱 맞는다.
- **bring back X** — 없앤 것을 되살리다. `restore` 보다 구어적이다.
- **which is what this change removed** — "그게 바로 이번 변경이 없앤 것"이라며 대안을 받아치는 계속적 관계절.

**격식 짝**
- refined: *I recommend retaining the current behavior.* (작성)
- plain: *I'd just leave it.* (작성)
- refined: *Should new tools be added frequently enough to go unnoticed, let me know and I will reinstate the option.* (작성)
- plain: *If this ever bites people, tell me and I'll put it back.* (작성)

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt (assistant)</sub>

---

## 단락 3

Why Flask restarts before the models: a Flask that has the key sends `Bearer <key>` to vLLM. A vLLM started without `--api-key` ignores that header, so the order is safe. The other way round, a vLLM with the key gets calls from a Flask with no key, and every call returns 401 until Flask restarts. Why clients get the key in step 4: sending a key while the server has none does no harm, because the proxy removes it and re-injects its own. That way nobody gets locked out when step 5 turns auth on.

**문법·구조**: `Why Flask restarts …:` 는 **간접의문문을 제목처럼** 쓴 꼴이다. 직접 의문문이면 `Why does Flask restart …?` 인데 여기서는 도치 없이 평서 어순을 쓰고 콜론으로 답을 붙였다. 체크리스트·FAQ 해설에 자주 나오는 형태다.

같은 명사 `a vLLM`, `a Flask` 를 꾸미는 방식이 세 가지로 갈린다. 관계절 `a Flask that has the key`, 과거분사 축약 `A vLLM started without --api-key`, 전치사구 `a vLLM with the key`. 뜻은 비슷하지만 뒤로 갈수록 짧고 가볍다. 한 단락에서 섞어 쓰면 문장이 단조롭지 않다.

`until Flask restarts` 는 미래 일인데도 **현재형**을 쓴다. 시간·조건 부사절의 규칙이다. `while the server has none` 의 `none` 은 `no key` 를 대신 받아 반복을 피한다. `re-injects its own` 의 `its own` 도 `its own key` 에서 명사를 뺐다.

마지막 `That way …` 는 앞 조치의 효과를 한 번에 받아 단락을 닫는다.

**핵심 표현**
- **the other way round** — 순서를 뒤집은 경우를 대비할 때 문두에 둔다.
- **does no harm** — 먼저 해도 손해 볼 게 없다는 안전 보증.
- **get locked out** — 접근이 막히다. 롤아웃 순서의 목적을 한 동사로 요약한다.

**격식 짝**
- refined: *Were the order reversed, every request would be rejected with a 401 until Flask was restarted.* (작성)
- plain: *Flip the order and everything 401s until Flask comes back up.* (작성)
- refined: *Distributing the key in advance is harmless, as the proxy strips and replaces it.* (작성)
- plain: *Handing out the key early doesn't hurt — the proxy swaps it anyway.* (작성)

<sub>출처: transcript:-Users-daeyoung-Codes-llm-serving (assistant)</sub>
