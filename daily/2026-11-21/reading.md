# 2026-11-21 — 정독

대화 본문이 한국어라서 영어 단락은 세션에 실린 스킬 문서에서 골랐습니다. 셋 다 에이전트에게 주는 지시문입니다. 명령문이 이어지는데도 딱딱하지 않은 까닭은 문장마다 이유나 조건이 붙어 있어서예요. 명령과 근거가 어떤 순서로 놓이는지 따라가 봅니다.

## 단락 1

With a `thread` field on the request, the API keeps the conversation for a short time, so each later request sends only the new messages. In long multi-turn loops (agent tool loops, long chats) that means smaller requests and lower time to first token, at the same price. Threads are best-effort: keep your own copy of the conversation and replay it when the API can't continue the thread; the SDK thread helper (`client.beta.messages.thread(...)`) does this for you. **Threads can't be combined with compaction**, most context editing, Message Batches or token counting; to compact, start a new thread from a summary you write. Message threads are not ZDR eligible. Using this feature does not affect your use of other ZDR eligible features.

**문법·구조**: 단락 전체가 현재시제입니다. 기능이 늘 그렇게 동작한다는 사실을 말하기 때문이에요. 첫 문장은 `With + 명사구` 로 조건을 열고(`If you add a thread field` 를 줄인 꼴) `so` 로 결과를 잇습니다. 둘째 문장의 `that` 은 앞 문장 전체를 받고, `that means A and B, at the same price` 에서 쉼표 뒤 전치사구가 "게다가 값은 그대로"라는 덤을 붙입니다. 셋째 문장은 콜론이 핵심입니다. `Threads are best-effort` 라는 성격 규정이 먼저 오고 콜론 뒤에 그래서 해야 할 일(`keep … and replay …`)이 명령문으로 옵니다. 세미콜론 뒤는 다시 평서문으로 돌아가 "그 일은 헬퍼가 해 준다"고 안심시켜요. 넷째 문장은 수동태 `can't be combined with` 를 썼는데, 누가 결합하느냐보다 결합이 안 된다는 제약이 주제라서 그렇습니다. 세미콜론 뒤 `to compact, start …` 는 목적의 to 부정사를 문두에 둔 명령문이고, `a summary you write` 는 목적격 관계대명사가 빠진 관계절입니다. 마지막 문장은 동명사구 `Using this feature` 가 주어입니다.

**핵심 표현**: `best-effort` 는 "되도록 하지만 보장은 안 한다"는 형용사입니다. 그래서 바로 뒤에 `keep your own copy` 가 따라옵니다. `time to first token` 은 첫 글자가 나오기까지 걸리는 시간으로, 통째로 한 명사처럼 씁니다. `eligible` 은 "자격이 되는"인데 `ZDR eligible` 처럼 앞에 조건 이름을 붙여 "그 제도의 적용 대상"이라는 뜻을 만듭니다.

**격식 짝** (작성):
- refined: Threads are provided on a best-effort basis; clients should retain a local copy of the conversation and resubmit it if the thread cannot be resumed.
- plain: Threads might not always be there, so keep your own copy and send it again if one disappears.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Message Threads")</sub>

---

## 단락 2

Enumerate the model slugs you can pass to a subagent in this session (Cursor `Task`, Claude Code `Agent`, OpenCode `task`, Codex `spawn_agent`). That is the dependable source. If your harness also has a command that lists the user's models, prefer it for completeness (for example `opencode models` or `pi --list-models`). If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid even though they are not detected slugs.

**문법·구조**: 명령문, 짧은 평서문, 조건문 둘, 금지문, 예외 순으로 놓였습니다. 절차를 쓸 때 본받을 만한 뼈대예요. 기본 행동 → 그것을 믿는 이유 → 더 나은 수단이 있을 때 → 아무것도 안 될 때 → 절대 하지 말 것 → 예외. 관계절이 네 번 나오는데 셋은 관계대명사가 빠졌습니다(`slugs [that] you can pass`, `slugs [that] they have access to`, `a real slug [that] you have not confirmed is available`). 마지막 것이 까다롭습니다. `you have not confirmed (that) it is available` 에서 `it` 이 선행사로 빠져나간 꼴이라 `confirmed is` 가 붙어 보입니다. 틀린 문장이 아니고 "삽입절이 낀 관계절"이에요. 시제도 볼 만합니다. `have not confirmed` 는 현재완료로, 쓰는 시점까지 확인을 마쳤느냐를 묻습니다. `even though` 는 사실을 인정하면서 양보하는 접속사라서, 가정인 `even if` 와 다릅니다.

**핵심 표현**: `prefer it for completeness` 는 "빠짐없이 얻으려면 그쪽을 택하라"입니다. `for + 추상명사` 로 목적을 짧게 말해요(`for safety`, `for clarity`). `have access to` 는 "쓸 권한이 있다"이고 전치사가 문장 끝에 남습니다. `Never write …` 는 `Do not` 보다 센 금지인데 대문자로 소리치지 않고도 충분히 단호합니다.

**격식 짝** (작성):
- refined: Do not record any identifier whose availability has not been verified.
- plain: Don't write down a slug unless you've checked it actually works.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (setup-pstack 스킬 "1. Detect available models")</sub>

---

## 단락 3

**Confirm migration scope before editing:** When a user asks to migrate code to a newer Claude model without naming a specific file, directory, or file list, **ask which scope to apply first** - the entire working directory, a specific subdirectory, or a specific set of files. Do not start editing until the user confirms. Imperative phrasings like "migrate my codebase", "move my project to X", "upgrade to Sonnet 4.6", or bare "migrate to Opus 4.8" are **still ambiguous** - they tell you what to do but not where, so ask. Proceed without asking only when the prompt names an exact file, a specific directory, or an explicit file list ("migrate `app.py`", "migrate everything under `services/`", "update `a.py` and `b.py`").

**문법·구조**: 규칙 하나를 네 문장으로 쌓았습니다. 조건과 행동, 금지, 흔한 오해 반박, 예외 순이에요. 첫 문장은 `When … without naming …` 으로 조건을 길게 깐 뒤 주절이 명령문 `ask which scope to apply first` 로 떨어집니다. `without + 동명사` 가 "~하지 않은 채"를 맡고, `which scope to apply` 는 의문사 + to 부정사로 `which scope you should apply` 를 줄였습니다. 둘째 문장의 `not … until` 은 "확인할 때까지 하지 마라", 뒤집으면 "확인한 뒤에야 하라"입니다. 셋째 문장은 주어가 깁니다. `Imperative phrasings like A, B, C, or bare D` 전체가 주어이고 동사는 `are` 예요. `bare` 는 "아무 수식 없이 그것만 달랑"이라는 형용사입니다. 대시 뒤에서 이유를 대고 `so ask` 로 닫습니다. 넷째 문장은 `only when` 이 문장 가운데 있어서 도치가 일어나지 않습니다. `Only when …` 을 문두로 빼면 `Only when the prompt names a file should you proceed` 처럼 조동사가 앞으로 나와요.

**핵심 표현**: `still ambiguous` 의 `still` 은 "명령형이라 분명해 보여도 여전히"라는 양보를 한 단어로 처리합니다. `what to do but not where` 는 반복되는 부분을 지운 대구입니다. `names an exact file` 의 `name` 은 동사로 "콕 집어 말하다"예요.

**격식 짝** (작성):
- refined: Do not begin editing until the user has confirmed the scope of the migration.
- plain: Hold off on any edits until they tell you which files they mean.

<sub>출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/444fbcbd (claude-api 스킬 "Common Pitfalls")</sub>
