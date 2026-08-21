# 2026-08-22 — 정독

## 단락 1

The rebuttal is right that the byte route exists but wrong that this settles it: that route has no server-side cache. Its docstring says "FTP to memory to response"; `fetch_recipe_image` calls `_fetch_raw` and returns — nothing is stored. The only cache is the browser's `Cache-Control: immutable` header. Concrete failure: hot 9006 alarm, three engineers open the modal in an hour, each from their own browser. Engineer 1 pays the FTP fetch; engineers 2 and 3 each pay it again in full, straight to the tool that is failing alignments. `single_flight` doesn't help — it dedups only concurrent requests, not sequential cold viewers. This is exactly the herd the falsifiers warned about, arriving politely in single file. So design point 6 is not reuse — it is a new write-through cache inside `fetch_recipe_image`, which is precisely where the shared-prefix decision and the Airflow TTL actually attach. The rebuttal's "no new byte route" is true; "bytes homeless" was fixed by the wrong argument — the cost moved, it didn't vanish.

**문법·구조**: 첫 문장이 이 단락 전체의 설계다. `is right that … but wrong that …` 은 하나의 형용사 자리에 that절 두 개를 병렬로 매단 형태로, **인정과 반박을 한 문장 안에서 끝낸다**. 우리말로는 "맞긴 한데"로 두 문장이 될 것을 영어는 접속사 `but` 하나로 붙여 버린다. 논쟁문에서 가장 자주 쓰이는 뼈대이니 통째로 외워 둘 만하다. 뒤의 콜론은 "그 이유는 이것"을 예고하는데, 콜론 뒤가 완전한 문장이어도 대문자로 시작하지 않는 게 영국·미국 공통 관행이다.

시제가 셋 섞여 있는데 각각 역할이 다르다. `has no server-side cache`, `calls`, `returns` 는 **코드의 항구적 성질**이라 현재시제다. `Concrete failure:` 뒤로는 `three engineers open the modal`, `Engineer 1 pays`, `engineers 2 and 3 each pay it again` 처럼 **미래의 시나리오인데도 현재시제**를 쓴다. 가정법 `would open`, `would pay` 를 피한 것이 요령인데, 아직 일어나지 않은 일을 현재로 적으면 "일어날 수도 있다"가 아니라 "이렇게 돌아간다"로 읽힌다. 반박당하지 않으려는 문장은 대개 이렇게 쓴다.

`Concrete failure: hot 9006 alarm, three engineers open the modal in an hour, each from their own browser.` 는 동사 없이 명사구만 나열한 **전보체(telegraphic style)** 다. 조건을 빠르게 세팅하고 본론으로 넘어갈 때 쓰며, 뒤따르는 두 문장이 완전한 문장이라 대비가 생긴다. `each from their own browser` 의 `their` 는 성별 미상의 단수를 받는 현대 표준 용법이다.

세미콜론이 두 번 나오는데 쓰임이 다르다. 첫 번째(`says "FTP to memory to response"; fetch_recipe_image calls…`)는 **같은 근거의 두 조각**을 잇고, 마지막(`is true; "bytes homeless" was fixed…`)은 **인정과 반전**을 잇는다. 마침표로 끊으면 두 문장이 무관해 보이고 쉼표로 이으면 문법 오류가 되는 자리라, 세미콜론만이 답인 경우다.

**핵심 표현**: `settles it` — "이걸로 결론이 난다". 논쟁의 종결을 가리키는 동사이며, 부정형 `that doesn't settle it` 이 훨씬 자주 쓰인다. / `pay it again in full` — 비용을 은유가 아니라 회계처럼 다룬다. `in full` 이 "일부라도 아끼는 게 아니라 전액"을 못 박는다. / `attach` (자동사) — 정책·비용이 "어느 지점에 들러붙는가". 목적어 없이 `where the decision actually attaches` 로 쓰면 "실제로 결정이 걸리는 자리"가 된다.

**격식 짝**:
- refined: The rebuttal is right that the route exists but wrong that this settles it. / plain: True, the route's already there — but that's not the point.
- refined: It dedups only concurrent requests, not sequential cold viewers. / plain: It only helps when they click at the same time, not one after another.

<sub>출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-21-live-alarm-align-image-discuss.md (Round 2)</sub>

---

## 단락 2

`git worktree remove` only deletes tracked files. Anything gitignored — `node_modules/`, `.nuxt/` — survives as an empty-looking husk, which is why these two directories outlived both their worktree registration and their branches. The husk is invisible to every git command: `git worktree list` didn't show them and `git worktree prune` had nothing to do, because git's `.git/worktrees` admin area was already clean. Only `ls` on the parent directory finds them. The reflog is the reliable landing record here. `git branch --merged` couldn't help — the branches were already deleted — but `merge work/simplify: Fast-forward` entries prove the work reached `main` before teardown.

**문법·구조**: 조사 보고문의 표본이다. 첫 문장이 **일반 규칙**(현재시제), 그다음부터 **이번 사례**(과거시제)로 내려온다. `didn't show`, `had nothing to do`, `was already clean`, `couldn't help`, `were already deleted` 가 전부 과거인 것은 특정 시점에 실제로 실행해 본 결과이기 때문이다. 규칙은 현재, 관찰은 과거 — 이 층을 섞지 않는 것이 기술 보고에서 신뢰를 만든다.

`which is why …` 는 앞 절 전체를 받는 비제한 관계절이다. 앞 명사(`husk`)가 아니라 **"살아남는다는 사실"** 을 받고 있어서, 관찰에서 설명으로 넘어가는 다리 역할을 한다. 우리말 "그래서 ~인 것이다"에 해당하지만 문장을 끊지 않고 이어 붙인다는 점이 다르다.

시간 관계를 나타내는 세 표현이 겹쳐 쓰였다. `outlived`(~보다 오래 살아남았다), `already`(두 번), `before teardown`. 특히 `outlive` 는 사람의 수명 어휘를 디렉터리에 붙인 것으로, 뒤에 목적어 두 개를 `both A and B` 로 묶어 "등록도 브랜치도 다 넘겼다"를 한 번에 처리한다.

부정 뒤의 반전을 대시로 감싼 `couldn't help — the branches were already deleted — but …` 는 **이유를 삽입절로 밀어 넣는** 방식이다. 괄호를 쓰면 곁가지로 읽히고 쉼표를 쓰면 `but` 과 충돌하는데, 대시 한 쌍이 이유를 본문 무게로 유지하면서 `couldn't help … but` 의 연결을 살린다.

`Only ls on the parent directory finds them.` 은 `Only` 를 문두에 두고도 도치하지 않았다. `Only` 가 **주어를 수식**할 때는 도치가 없고(`Only ls finds them`), 부사구를 수식할 때만 도치한다(`Only then did I find them`). 이 구분을 틀리는 사람이 많으니 두 예를 짝으로 기억하는 게 좋다.

**핵심 표현**: `an empty-looking husk` — 껍데기. `-looking` 하이픈 형용사가 "비어 보이지만 실제로 파일은 있다"는 겉과 속의 어긋남을 만든다. / `had nothing to do` — 명령이 할 일이 없었다는 뜻이지 실패했다는 뜻이 아니다. 이 구분이 진단에서 결정적일 때가 많다. / `the landing record` — 어떤 작업이 main 에 도착했는지 증명하는 기록. `land`(머지되어 안착하다)의 명사형 활용이다. / `before teardown` — 정리·철거 전에. 관사 없이 쓰는 게 관례다.

**격식 짝**:
- refined: These directories outlived both their worktree registration and their branches. / plain: The folders stuck around long after the worktree and the branch were gone.
- refined: The reflog is the reliable landing record here. / plain: The reflog's the only place that still remembers it got merged.

<sub>출처: transcript:skewnono_v3_nuxt (worktree 정리 세션)</sub>

---

## 단락 3

This is the skill. Everything else is mechanical. If you have a tight pass/fail signal for the bug — one that goes red on this bug — you will find the cause; bisection, hypothesis-testing, and instrumentation all just consume it. If you don't have one, no amount of staring at code will save you. Spend disproportionate effort here. Be aggressive. Be creative. Refuse to give up. Treat the loop as a product: once you have a loop, tighten it. A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight — a debugging superpower.

**문법·구조**: 지시문의 문법이 앞의 두 단락과 완전히 다르다. 주어가 사라지고 **명령문**이 이어진다 — `Spend`, `Be`, `Be`, `Refuse`, `Treat`, `tighten`. 명령문은 주어를 지운 만큼 문장이 짧아지고, 짧아진 문장을 연달아 놓으면 리듬이 빨라진다. 조언하는 글이 이 형태를 고르는 이유다.

조건절 두 개가 정확히 대칭으로 서 있다. `If you have … you will find the cause` / `If you don't have one, no amount of staring at code will save you.` 둘 다 **제1조건문**(if + 현재 → will)이라 "일어날 법한 일"로 다룬다. 가정법 과거(`if you had … you would find`)로 썼다면 "현실성 없는 가정"이 되어 조언의 힘이 빠진다. 조언문에서 시제를 낮춰 잡는 실수가 잦은데, 이 대칭이 좋은 본보기다.

`no amount of staring at code will save you` 는 부정 주어 구문이다. `You can't fix it by staring at code` 보다 강한 이유는, 부정이 동사가 아니라 **주어 자체**에 걸려 "얼마를 하든 소용없다"를 양의 문제로 만들기 때문이다. `no amount of X will Y` 는 통째로 쓰는 틀이다.

마지막 문장의 세미콜론은 **비교의 축**이다. 앞뒤가 `A는 거의 쓸모없다 ; B는 강력하다` 로 대칭이고, 형용사 자리(`flaky` ↔ `deterministic`)와 수치(`30-second` ↔ `2-second`)만 갈아 끼웠다. 숫자를 하이픈으로 묶어 형용사로 만들 때는 단수형을 쓴다 — `a 30-second loop` 이지 `a 30-seconds loop` 이 아니다. 그리고 대시 뒤의 `a debugging superpower` 는 동사 없이 앞 명사를 다시 부르는 동격이다.

**핵심 표현**: `goes red on this bug` — 테스트가 이 버그에서 실제로 실패한다. `go red` / `go green` 은 CI 색깔을 그대로 동사로 쓴 것이며 `turn red` 보다 개발자 어투다. / `disproportionate effort` — 비율에 안 맞게 큰 노력. 보통은 비판어지만 여기서는 **의도적 배분**을 뜻하는 칭찬 쪽으로 뒤집혔다. / `barely better than` — 겨우 나은 정도, 즉 사실상 같다. 완곡한 부정이다. / `tighten` — 루프를 더 빠르고 결정적으로 조이다. 나사를 조이는 그림에서 왔다.

**격식 짝**:
- refined: Spend disproportionate effort here. / plain: This is the part worth over-investing in.
- refined: No amount of staring at code will save you. / plain: You're not going to read your way out of this one.

<sub>출처: transcript:skewnono_v3_nuxt (diagnosing-bugs 스킬, Phase 1)</sub>
