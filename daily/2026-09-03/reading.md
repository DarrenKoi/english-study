# 2026-09-03 — 정독

## 단락 1

When I *don't* reach for a browser: anything a `curl -b "LASTUSER=…" localhost:3000/api/...` answers. Payload shape, a provider swap, a computed number — those are faster and more precise through the API or pytest, and a browser check there is theater. I reach for it when the thing I changed only exists in a browser. Chart state never shows up in a unit test. Downloads are the same: only a real click proves the blob actually lands. Rough rule: if the bug could be described without mentioning pixels, events, or the URL bar, it isn't a browser job.

**문법·구조**: 첫 문장은 주어부터 나오지 않는다. `When I don't ...:` 라는 부사절을 앞세우고 콜론 뒤에 답을 던지는 구성이라, 리스트 항목처럼 읽히면서도 문장이다. 뒤이어 `Payload shape, a provider swap, a computed number —` 세 명사구를 나열하고 대시로 받아 `those are ...` 로 되받는데, 이 재수용(resumptive) 구조 덕에 주어가 길어져도 문장이 무겁지 않다. 시제는 전부 현재형이다 — 한 번의 사건이 아니라 늘 지키는 습관·규칙을 말하기 때문이다. 마지막 문장의 `if ... , it isn't ...` 는 가정법이 아닌 단순 현재 조건절인데, 규칙을 시간에 매이지 않는 진리처럼 세우려는 선택이다. `only exists in a browser` 의 only 가 동사 앞이 아니라 exists 앞에 붙은 위치도 눈여겨볼 만하다 — 존재 자체를 한정한다.

**핵심 표현**: `a browser check there is theater` — 절차만 갖추고 실질이 없다는 신랄한 판정. `there` 하나로 "다른 데선 아니고 바로 그 경우엔"을 표현한다. / `only a real click proves the blob actually lands` — 증명의 최소 조건을 말하는 틀. prove 뒤에 that 을 생략해 속도를 냈다. / `it isn't a browser job` — 능력이 아니라 담당 범위를 자르는 판정.

**격식 짝**: (작성)
- refined: A browser check adds no evidence where the API already answers the question.
- plain: If curl already tells you, opening a browser is just for show.

<sub>출처: transcript:skewnono_v3_nuxt df4b4762 ([assistant])</sub>

---

## 단락 2

The label and the exclusion are now two predicates on purpose. `paramRole` is the raw Mother_Para flag, so every non-mother row says `son`. `ridesOnMother` is the narrower "son inside a region that actually has a mother", and that is still what cap inheritance and the son toggle key on. Keeping them apart means the toggle's numbers did not move at all with this change. One caveat to be aware of: a row can now read `son` while its note has no exclusion mark. The behaviour is unchanged, only the label is broader, and the docstrings say so.

**문법·구조**: `on purpose` 를 문장 끝에 두어 "둘로 나뉘어 있다"는 사실보다 "일부러 그랬다"는 판단에 무게를 실었다 — 위치가 곧 강조다. 두 술어를 소개할 때 `A is X, so ...` / `B is the narrower "...", and that is still what ... key on` 으로 구조를 일부러 어긋나게 짰다. 병렬을 맞추면 대칭으로 읽히는데, 여기서는 둘이 대등하지 않고 하나가 더 좁다는 걸 형태로도 보여 준다. `what ... key on` 은 관계절 안에서 전치사가 뒤에 남는 형태(preposition stranding)로, 격식체의 `on which ...` 보다 훨씬 자연스럽다. 네 번째 문장의 `did not move at all` 은 완료형이 아닌 단순 과거인데, 변경 시점이라는 한 사건에 못박기 때문이다. 마지막 문장은 부정→긍정→근거 순서다: 안 바뀐 것을 먼저 말하고, 바뀐 범위를 좁혀 주고, `and the docstrings say so` 로 확인 경로까지 넘긴다.

**핵심 표현**: `two predicates on purpose` — 합칠 수 있었으나 안 합쳤다는 설계 선언. / `the narrower "..."` — 정관사 + 비교급으로 두 개념 중 좁은 쪽을 지목하는 경제적인 방법. / `and the docstrings say so` — 주장 뒤에 검증 위치를 붙여 말을 사실로 바꾸는 마무리.

**격식 짝**: (작성)
- refined: The two predicates are kept distinct deliberately, so the toggle's semantics are untouched.
- plain: We left them as two separate checks on purpose — the toggle works exactly like before.

<sub>출처: transcript:skewnono_v3_nuxt ad54ba15 ([assistant])</sub>

