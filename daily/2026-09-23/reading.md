# 2026-09-23 — 정독

> repo 문서 3건은 본문이 한국어라 인용할 영어 단락이 없고 세 단락 모두 equipment-data-map 세션의 `[assistant]` 영어 원문이다. 굵은 소제목은 풀어서 본문에 이었고 중간에 뺀 문장은 `…` 로 표시. 단락 1은 요청을 실행하기 전에 반대 의견을 내는 글, 단락 2는 버그의 원인을 설명하는 포스트모템, 단락 3은 설정값의 종류를 나눠 주는 설명문이다. 세 글 모두 짧은 문장과 긴 문장을 번갈아 쓰면서 콜론과 대시로 "주장 → 근거"를 잇는 모습을 눈여겨보자.

## 단락 1

This one I want to push back on before touching anything, because it reverses the one rule the whole safety design hangs on. `index.md:94-111` says the agent accepts *no* equipment facts — not in its prompt, not in a file it reads. The reason isn't ceremony: an IP, root path or account name that reaches the agent sits in its transcript forever, in whatever the tool logs, and the `rollout.json` → plan-hash → approval chain only proves anything if the agent had no way to author those values. That's also why `engineer.toml` (the one file the agent reads) holds no equipment facts, and why `init` is TTY-only. "Let the LLM ask me for the IP and fill it in" is precisely the flow the spec forbids. … So my recommendation is: keep `init` in your hands, and let the redo land. If you still want the agent to drive it, that is a design change, not a convenience: it means deleting the no-equipment-facts rule from `index.md`, the "operator commands stay human" invariant, the TTY check, and the scenario in letter 10 that fails when a skill runs `init`. I'll do it if you confirm, but I'd be removing the guarantee that no agent transcript ever contains an equipment address.

**문법·구조**: 첫 문장은 목적어 `This one` 을 문두로 끌어낸 도치. 평서 어순 `I want to push back on this one` 보다 "이것만은"이라는 대비가 앞에 선다. `the one rule the whole safety design hangs on` 은 관계대명사가 빠진 접촉절이고 전치사 `on` 이 절 끝에 남았다. 셋째 문장이 이 단락의 심장인데 `The reason isn't ceremony:` 로 오해를 먼저 걷어낸 뒤 콜론 뒤에 긴 이유가 온다. 주어가 `an IP, root path or account name that reaches the agent` 로 길고 술어 둘(`sits … forever`, `only proves anything if …`)이 `and` 로 이어지며 `only … if` 가 조건을 뒤로 던지는 구조. 넷째 문장의 `That's also why …, and why …` 는 같은 원인에서 나온 결과 둘을 `why` 절 두 개로 묶은 병렬이다. 다섯째 문장은 상대의 말을 따옴표로 그대로 주어 삼았는데, 인용을 주어로 세우면 반박이 사람이 아니라 문장을 향한다. 후반부 `If you still want …, that is …: it means deleting A, B, C, and D` 는 조건절 → 판정 → 콜론 → 동명사 목록의 순서로, 판정을 먼저 주고 대가를 나열하는 방식. 마지막 문장의 `I'll do it if you confirm, but I'd be removing …` 은 단순 미래와 가정법 진행(`would be removing`)을 맞세워 "하겠다"와 "그 순간 무엇을 잃는지"를 한 문장에 담았다.

**핵심 표현**: `push back on X before touching anything` — 실행 전에 이의를 내겠다는 예고. / `The reason isn't ceremony:` — 규칙이 형식이 아니라 실질임을 콜론으로 이어 설명. / `a design change, not a convenience` — 요청의 등급을 다시 매기는 `A, not B`.

**격식 짝**: (작성)
- refined: I would like to raise an objection before making any changes, as this request reverses the single rule on which the entire safety design depends.
- plain: Before I touch anything, I want to push back on this one. It flips the one rule everything else leans on.
- refined: Should you still wish the agent to perform this step, please note that it constitutes a design change rather than a convenience.
- plain: If you still want the agent doing it, that's a design change, not a convenience.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 2

What was wrong: `ftp_handler/proxy/flask_proxy.py:136` checked `token is not None`. A blank `FTP_PROXY_TOKEN=` in `.env` becomes `""` in the environment (not `None`), so the server switched auth *on* with an empty token and 401'd every header-less request — while the client (`proxy_downloader.py:147`, `... or None`) correctly sent no header. The two sides disagreed on what "" means; the fake proxy runs in the same process as the check, so letter 03's transport check hit it immediately. Fix: one line — `os.getenv("FTP_PROXY_TOKEN") or None` on the server too. … This is the classic "is it set?" vs "is it non-empty?" split. `os.getenv` returns `None` only when the variable is absent; a dotenv loader that writes every `KEY=` line makes "absent" almost impossible in practice, so any server check must use `or None` (or `if token:`). The client author knew; the server author didn't, and nothing tested the pair together with an empty value.

**문법·구조**: 포스트모템의 전형적 순서다. 무엇이 틀렸나(과거) → 왜 그렇게 됐나(현재, 일반 사실) → 고침(명사구) → 교훈(현재). 첫 문장은 과거 단순 `checked` 로 사건을 적는다. 둘째 문장은 현재 시제 `becomes` 로 환경 변수의 일반 규칙을 말한 뒤 `so` 로 결과(`switched … on`, `401'd`)를 잇는다. 상태 코드를 동사로 만든 `401'd` 는 채팅·리뷰에서만 통하는 구어다. 대시 뒤의 `while the client … correctly sent no header` 는 대조의 `while`. `The two sides disagreed on what "" means` 는 두 프로그램을 사람처럼 세워 책임을 나눈다. `Fix: one line —` 처럼 콜론과 대시로 문장 없이 정보를 붙이는 방식도 보고문 관용. 교훈 단락의 `returns None only when …` 은 `only` 가 조건을 좁힌다. 마지막 문장은 세미콜론으로 `The client author knew; the server author didn't` 를 맞세운 뒤 `and nothing tested the pair together` 로 진짜 원인(시험 부재)을 밝힌다. 사람 둘을 대비시키면서도 이름을 부르지 않는 점이 비난 없는 포스트모템의 문체다.

**핵심 표현**: `The two sides disagreed on what "" means` — 짝 코드의 해석 불일치를 한 줄로. / `the classic "is it set?" vs "is it non-empty?" split` — 흔한 버그 유형에 이름 붙이기. / `nothing tested the pair together` — 각각은 맞았는데 조합을 시험한 적이 없었다는 원인 진술.

**격식 짝**: (작성)
- refined: The client and the server interpreted an empty string differently, and no test exercised the two together with that value.
- plain: The two sides read "" differently, and nothing ever tested them side by side with an empty value.

<sub>출처: transcript:[assistant] equipment-data-map</sub>

---

## 단락 3

Those three budgets are the "no budget, no run" ones — the CLI refuses without them. When any is hit the run ends *normally* with partial coverage recorded; it's a ceiling, not a failure. … Two kinds of limits hide under "budgets". `max_download_files` / `max_total_bytes` / `max_elapsed_seconds` are *stop* limits — reach one and the run finishes with partial coverage. `requests_per_second` / `max_connections` are *pace* limits — they never end a run, they just keep the tool from noticing you. `max_file_bytes` is neither: it's a reporting threshold, and the spec deliberately says it never rejects a file.

**문법·구조**: 설정 항목을 분류해 주는 설명문이라 시제는 전부 현재. 첫 문장은 인용부호로 만든 별칭 `the "no budget, no run" ones` 가 명사 노릇을 하고 대시 뒤에 그 뜻을 푼다. 둘째 문장의 `When any is hit` 은 수동태로 행위자를 지웠는데 누가 한도를 치느냐는 중요하지 않고 "닿으면"만 중요해서다. `it's a ceiling, not a failure` 가 `A, not B` 로 오해를 막는다. 셋째 문장 `Two kinds of limits hide under "budgets"` 는 한도가 스스로 "숨어 있다"고 말하는 의인화로 분류의 문을 여는 장치. 이어지는 두 문장은 완전히 같은 뼈대다. 항목 나열 → `are *stop* limits` / `are *pace* limits` → 대시 → 풀이. 대시 뒤의 `reach one and the run finishes` 는 명령문 + `and` 로 조건을 만드는 구어 문법이고 둘째 대시 뒤는 `they never end a run, they just …` 로 부정과 긍정을 쉼표 하나로 맞세웠다. 마지막 문장 `is neither:` 가 두 분류 모두 아니라고 못 박고 콜론 뒤에 세 번째 성격을 준다. `deliberately` 한 단어가 "실수가 아니라 설계"임을 알리는 셈.

**핵심 표현**: `it's a ceiling, not a failure` — 한도 도달이 정상 종료임을 알리는 대비. / `Two kinds of limits hide under X` — 한 이름 아래 다른 성격이 섞여 있음을 열어 주는 문장. / `keep the tool from noticing you` — 속도 제한의 목적을 비유로.

**격식 짝**: (작성)
- refined: Reaching any of these limits terminates the run normally, with the partial coverage recorded; the limit is an upper bound rather than an error condition.
- plain: Hit any of them and the run just stops and writes down how far it got. It's a ceiling, not a failure.

<sub>출처: transcript:[assistant] equipment-data-map</sub>
