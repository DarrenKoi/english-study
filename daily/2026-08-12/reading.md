# 2026-08-12 — 정독

## 단락 1

Break the system into smaller units that each have one clear purpose, communicate through well-defined interfaces, and can be understood and tested independently. For each unit, you should be able to answer: what does it do, how do you use it, and what does it depend on? Can someone understand what a unit does without reading its internals? Can you change the internals without breaking consumers? If not, the boundaries need work. Smaller, well-bounded units are also easier for you to work with — you reason better about code you can hold in context at once, and your edits are more reliable when files are focused. When a file grows large, that's often a signal that it's doing too much.

**문법·구조**: 첫 문장은 관계절 `that each have … , communicate … , and can be …` 안에 동사 세 개를 나란히 물린 병렬이다. 주어가 `units` 하나뿐이라 `have/communicate/can be` 를 모두 그 하나가 받는다. 사이에 낀 `each` 는 주어를 다시 쓰지 않고 "단위마다"를 넣는 자리이며, 이 자리에서는 부사처럼 동작한다.
둘째 문장은 콜론 뒤에 의문사절 셋을 병렬로 늘어놨다. `what does it do` 는 간접의문문이면 `what it does` 여야 하지만, 여기서는 직접의문을 그대로 인용해 체크리스트 항목처럼 읽히게 했다. 문어에서 일부러 쓰는 파격이다.
그다음 두 문장은 조동사 의문문 `Can someone …? Can you …?` 로 리듬을 바꾼다. 앞이 서술이었으므로 질문 두 개가 독자를 자기 코드로 끌어들이고, `If not, the boundaries need work.` 라는 다섯 단어짜리 조각이 그 답을 받아 낸다. `if not` 은 앞의 두 질문을 통째로 받는 생략 표현이라 `if the answer is no` 를 줄인 것이다.
마지막 두 문장은 비교급 `easier … to work with` 와 `more reliable` 로 근거를 대고, `When a file grows large, that's often a signal that …` 로 판정 기준을 남긴다. `often` 이 없으면 규칙이 되고, 있으면 경험칙이 된다 — 지침 문서가 단정을 피하는 흔한 장치다.

**핵심 표현**:
- `well-bounded` — 경계가 잘 그어진. `well-` 접두 형용사는 명사 앞에서 하이픈을 유지한다(`a well-bounded unit`).
- `hold in context at once` — 쪼개지 않고 한 번에 머릿속에 담다. 사람과 모델 양쪽에 같은 논리로 쓴다.
- `the boundaries need work` — 경계가 아직 손볼 상태다. `need work` 는 "미완성"을 나무라지 않고 말하는 완충 표현이라 리뷰에 쓰기 좋다.

**격식 짝**:

| refined (설계 지침·문서) | plain (동료에게 구어) |
| --- | --- |
| If not, the boundaries need work. | If you can't, the split isn't right yet. |
| When a file grows large, that's often a signal that it's doing too much. | Big file usually means it's doing too much. |

<sub>출처: transcript:[user] auto-recipe-creator d5dd7c25 (superpowers brainstorming 스킬 문서)</sub>

---

## 단락 2

`[vite:vue] the service was stopped: write EPIPE` is not a Vue compile error. It's esbuild's message for "I tried to write a file into the esbuild child process's stdin pipe, and that child is dead." Two independent causes are both present on this machine. ( … ) `nuxt.config.ts` sets no `buildDir`, so both the dev server and `npm run build` write to the same `node_modules/.cache/nuxt/.nuxt`. They fight: the build rewrites the tree while the dev server's watcher regenerates it, and when one side tears down its esbuild service the other's pending pipe write dies as `EPIPE`.

**문법·구조**: 진단문의 전형적인 시작이 `is not …` 이다. 상대가 이미 갖고 있는 오해를 먼저 지우고 나서 자기 설명을 얹는 순서라, `It's esbuild's message for …` 가 부정 뒤의 빈자리를 곧바로 채운다.
그 `message for` 뒤에 큰따옴표로 **1인칭 문장을 통째로** 넣은 것이 이 단락의 중심 기교다. 에러 코드를 프로세스가 하는 말로 번역해 버려서, 기계 용어를 몰라도 상황이 그려진다. 인용 안은 `I tried to …, and that child is dead` 로 과거(시도) → 현재(결과)의 시제 전환이 그대로 살아 있다.
`They fight:` 는 주어와 동사 둘뿐인 짧은 문장이고 콜론으로 근거를 매단다. 앞뒤 문장이 모두 길어서 이 두 단어가 박자를 끊는다. 그 뒤는 `while` 로 동시 진행을, `when` 으로 시점을 잡아 두 절을 겹쳐 놓았고, 마지막 `dies as EPIPE` 의 `as` 는 "~라는 모습으로 죽는다"를 뜻해 원인과 관측된 증상을 한 전치사로 잇는다.
`sets no buildDir` 처럼 `no` 를 목적어에 붙여 부정하는 형태도 눈여겨볼 만하다. `does not set a buildDir` 보다 짧고, 없음 자체가 원인이라는 어감이 강해진다.

**핵심 표현**:
- `tear down (a service)` — 띄워 둔 것을 정리해 내리다. 반대는 `spin up`.
- `pending write` — 아직 끝나지 않은 채 걸려 있는 쓰기.
- `dies as EPIPE` — EPIPE 라는 형태로 죽는다. 원인 대신 증상의 이름을 결과 자리에 놓는다.

**격식 짝**:

| refined (장애 보고서) | plain (동료에게 구어) |
| --- | --- |
| The two processes write to the same build directory and tear down each other's esbuild service. | Dev server and build are fighting over the same cache dir. |
| The file is innocent; the helper process is being killed mid-build. | Nothing's wrong with the file — the helper just got killed. |

<sub>출처: transcript:[assistant] skewnono-v3-nuxt e4cdbee9 (npm run build EPIPE 진단, 두 대목을 잇대 인용)</sub>

---

## 단락 3

The core decision was storing the suffix, not the index. Your framing — "this suffix info varies based on the recipe and parameters" — is exactly why an index would have been a silent bug: on a point rendering `U T M L`, index 2 is `M`; on a point missing its `-T` shot it's `L`. So the memory holds `"M"` and re-resolves it against each point's own filenames, falling back to the first image when that suffix isn't there. ( … ) Each host previously had `ref(0)` plus a reset watcher — three copies of a rule that had already drifted. Replacing them with a writable computed means "reset on point change" and "restore on point change" are no longer two competing code paths; the getter simply re-derives from the current filenames. There is no reset left to get wrong.

**문법·구조**: 둘째 문장이 이 단락의 무게중심이다. 주어(`Your framing`)와 동사(`is`) 사이에 em-dash 로 사용자 발언을 통째로 끼워 넣어, 상대가 한 말을 근거로 되돌려준다. `is exactly why …` 는 "당신 말이 바로 그 이유다"라는 틀이라, 결정을 내 판단이 아니라 상대의 관찰에서 끌어낸 것으로 만든다.
콜론 뒤는 세미콜론으로 두 사례를 나란히 붙였다. `on a point rendering U T M L` 의 `rendering` 은 명사를 뒤에서 꾸미는 현재분사로, `on a point that renders …` 를 줄인 형태다. 뒤 절에서는 `index 2 is` 를 반복하지 않고 `it's L` 로 받아 대비가 선명해진다.
`would have been a silent bug` 는 실제로 일어나지 않은 과거를 말하는 가정법 과거완료다. 채택하지 않은 설계를 논할 때 사실 서술과 섞이지 않게 해 주는 시제이며, 뒤의 `had already drifted`(그 시점에 이미 어긋나 있었다)와 함께 시간 층이 둘로 갈린다.
마지막 문장 `There is no reset left to get wrong.` 은 `left`(남아 있는)와 `to get wrong`(틀릴 여지가 있는)이 앞뒤로 `reset` 을 감싼다. "고쳤다"가 아니라 "틀릴 대상 자체가 사라졌다"로 끝내는 마무리다.

**핵심 표현**:
- `drift` — 복사본들이 시간이 지나며 서로 어긋나다. `three copies of a rule that had already drifted`.
- `two competing code paths` — 같은 상황을 서로 다르게 처리하려고 다투는 두 경로.
- `no X left to get wrong` — 틀릴 X 자체가 남아 있지 않다. 리팩터링 결과를 한 줄로 닫는 상투구.

**격식 짝**:

| refined (PR 설명) | plain (구어) |
| --- | --- |
| Remembering the index would have been a silent bug. | If we'd stored the index, it'd break and nobody would notice. |
| There is no reset left to get wrong. | There's nothing left to reset, so nothing left to break. |

<sub>출처: transcript:[assistant] skewnono-v3-nuxt d5b1f8a7 (variant 기억 기능, 두 대목을 잇대 인용)</sub>
