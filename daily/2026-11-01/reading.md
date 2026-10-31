# 2026-11-01 — 정독

## 단락 1

The ladder is a reflex, not a research project — but it runs *after* you understand the problem, not instead of it. Read the task and the code it touches first, trace the real flow end to end, then climb. Two rungs work → take the higher one and move on. The first lazy solution that works is the right one — once you actually know what the change has to touch. **Bug fix = root cause, not symptom.** A report names a symptom. Before you edit, grep every caller of the function you're about to touch. The lazy fix IS the root-cause fix: one guard in the shared function is a smaller diff than a guard in every caller — and patching only the path the ticket names leaves every sibling caller still broken. Fix it once, where all callers route through.

**문법·구조**: 첫 문장은 `A, not B` 대비를 두 번 쓴다(`a reflex, not a research project` / `after …, not instead of it`). 대시(—) 뒤 `but` 으로 앞 주장에 단서를 다는 흐름이다. 둘째 문장은 명령문 세 개(`Read … trace … then climb`)를 순서대로 나열해 절차를 보여 준다. 일반 원칙은 현재형으로만 서술되는데, 지침서 영어의 기본값이다. `once you actually know …` 의 `once` 는 "일단 ~하고 나면"이라는 조건 접속사로 앞 주장의 적용 시점을 좁힌다. 후반부는 `A report names a symptom.` 같은 짧은 단언으로 리듬을 끊은 다음, 콜론 뒤 긴 문장에서 이유를 편다. `leaves every sibling caller still broken` 은 `leave + 목적어 + 형용사` 5형식이라 "~를 ~한 상태로 남겨 둔다"가 된다. 마지막 `where all callers route through` 는 관계부사 where 절로 "고칠 장소"를 지목한다.

**핵심 표현**:
- `take the higher one and move on` — 둘 다 되면 더 좋은 쪽을 고르고 미련 없이 넘어가라. 결정을 오래 끌지 말자는 구어 지침.
- `the path the ticket names` — 목적격 관계대명사(that)가 빠진 `명사 + 주어 + 동사` 꼴. "티켓이 지목한 경로".
- `sibling caller` — 같은 함수를 부르는 다른 호출부. 형제처럼 나란히 있는 것을 `sibling` 으로 부른다.

**격식 짝** (작성):
- refined: "Address the defect at its source rather than at each point where it manifests." ↔ plain: "Fix it once, where all the callers go through."
- refined: "Comprehension must precede any attempt to minimise the change." ↔ plain: "Understand the problem first, then keep the change small."

<sub>출처: transcript:bulk-recipe-copy 87a47375 (Ponytail 스킬 지침 "The ladder")</sub>

---

## 단락 2

Lazy code without its check is unfinished. Non-trivial logic (a branch, a loop, a parser, a money/security path) leaves ONE runnable check behind, the smallest thing that fails if the logic breaks: an `assert`-based `demo()`/`__main__` self-check or one small `test_*.py`. No frameworks, no fixtures, no per-function suites unless asked. Trivial one-liners need no test, YAGNI applies to tests too.

**문법·구조**: 네 문장뿐이지만 정의 → 요구 → 제한 → 예외 순서가 또렷하다. 둘째 문장의 `leaves … behind` 는 구동사 `leave behind`(남겨 두다) 사이에 목적어가 끼어든 형태다. 그 뒤 쉼표로 이어지는 `the smallest thing that fails if the logic breaks` 는 앞 명사구를 다시 풀어 주는 동격이고, 그 안의 `that` 관계절과 `if` 조건절이 겹쳐 "로직이 깨지면 실패하는 가장 작은 것"이라는 정의를 만든다. 셋째 문장은 동사 없이 `No X, no Y, no Z unless asked.` 로 끝나는 명사구 나열이다. 금지 목록을 빠르게 읽히게 하는 지침체 문법이다. `unless asked` 는 `unless (you are) asked` 에서 주어와 be동사가 생략된 꼴.

**핵심 표현**:
- `leave one runnable check behind` — 실행 가능한 확인 하나를 남겨 두다. 작업 뒤에 흔적을 남긴다는 그림.
- `unless asked` — 요청이 없는 한. 짧은 예외 조항으로 지침 끝에 자주 붙는다.
- `YAGNI applies to tests too` — 원칙을 다른 영역까지 넓히는 `X applies to Y too` 틀.

**격식 짝** (작성):
- refined: "Any non-trivial logic should be accompanied by at least one executable check." ↔ plain: "If the logic isn't trivial, leave one test behind."

<sub>출처: transcript:bulk-recipe-copy 87a47375 (Ponytail 스킬 지침 "When NOT to be lazy")</sub>

---

## 단락 3

The favicon is copied, `DESIGN.md` is back in sync with SKEWNONO, and both are pushed to `main` as `d24825e`. The SPA build passes, the favicon files are in the output, and the icon links render in `index.html`. The SVG is linked as a plain file. SKEWNONO inlines it in the page only because its URL changes on every click, and this app has no page navigation. Left out on purpose: the three slogan images in the Corporate section. One is SK hynix's official "We Do Technology" logo artwork, and this repo is public. `DESIGN.md` points to the originals in SKEWNONO (`docs/design/slogan/`) instead. If you're fine publishing them, it's one small commit to add them.

**문법·구조**: 완료 보고의 정석 구조다. 첫 두 문장은 `A, B, and C` 3항 병렬로 "무엇이 끝났는지"를 몰아서 말한다. 끝난 상태를 `is copied`·`are pushed` 처럼 **수동태 현재형**으로 써서 행위자(나)보다 결과에 초점을 둔다. 다음은 `only because` 로 원본이 다르게 한 이유를 좁혀 설명한다. "이유가 이것뿐이니 여기선 해당되지 않는다"는 논리가 `only` 한 단어에 실린다. `Left out on purpose:` 는 주어·동사를 생략한 표제형 문장이고, 콜론 뒤에 대상을 두어 눈에 띄게 한다. 마지막 문장은 `If you're fine -ing` 조건절로 결정을 상대에게 넘기면서 비용(`one small commit`)을 함께 알려 준다.

**핵심 표현**:
- `back in sync with` — 어긋났던 사본을 원본과 다시 맞췄다.
- `Left out on purpose` — 의도적으로 뺐다. 빠진 게 실수가 아님을 먼저 밝힌다.
- `points to … instead` — 사본을 두지 않고 원본을 가리키게 했다.

**격식 짝** (작성):
- refined: "The slogan images have been intentionally omitted; the documentation references the originals instead." ↔ plain: "I left the slogan images out on purpose. The doc just points to the originals."
- refined: "Should you be comfortable publishing them, adding them requires only a single commit." ↔ plain: "If you're fine publishing them, it's one small commit."

<sub>출처: transcript:bulk-recipe-copy 87a47375 ([assistant] 파비콘·DESIGN.md 동기화 완료 보고)</sub>
