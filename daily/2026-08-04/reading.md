# 2026-08-04 — 정독

## 단락 1

The preinstall trap has a precise mechanism: `pip install -r requirements.txt` is **not** an upgrade command. It resolves each named requirement and leaves an already-installed package alone whenever its version satisfies the specifier. So a preinstalled package is upgraded only if a specifier *you wrote down* excludes it — and a package you never named at all is **invisible to the whole operation**. numpy was in that third category, which is why every prior deploy "succeeded" while the image's numpy 1 sat there untouched. The corollary is counter-intuitive for a requirements file: declare transitive dependencies whose version matters. Normally you don't list what pandas pulls in. But pip can only enforce constraints that exist, and on a host where the baseline is someone else's image, "pandas will bring a good numpy" is an assumption with no mechanism behind it.

**문법·구조**: 콜론이 "이제 그 mechanism 을 서술한다"를 예고하고, 곧바로 `is not an upgrade command` 라는 **부정 정의**로 문단을 연다 — 무엇인지보다 무엇이 아닌지를 먼저 못 박는 배치다. 이어지는 세 문장은 전부 현재시제이며, 사건 보고가 아니라 **도구의 항구적 규칙**을 적기 때문이다. `whenever its version satisfies` 의 whenever 가 if 대신 쓰인 것도 같은 이유로, 한 번의 조건이 아니라 매번 그렇다는 뜻이다. 셋째 문장은 `only if` 로 필요조건을 걸고, 목적격 관계사가 생략된 `a specifier you wrote down` 으로 "네가 직접 적어 둔"을 끼워 넣은 뒤, 대시 뒤에서 세 번째 범주(아예 이름조차 없는 패키지)를 추가한다. 넷째 문장의 `which is why` 는 앞 절 전체를 받는 비제한적 관계절이고, `while … sat there untouched` 는 동시 상황을 그린다. 뒷부분은 `Normally you don't …` → `But …` 양보-반전 한 쌍으로 조언의 예외성을 드러내고, 마지막은 인용문을 그대로 주어 자리에 앉힌 계사문으로 닫는다.

**핵심 표현**:
- `the corollary is counter-intuitive` — 앞 논증에서 따라 나오지만 상식과 어긋나는 결론을 예고.
- `an assumption with no mechanism behind it` — 강제 장치 없는 기대를 가정으로 격하.
- `invisible to the whole operation` — 검사 대상에조차 오르지 못한다는 강한 부정.

**격식 짝**:
- refined: pip can only enforce constraints that exist. ↔ plain: pip can't check something you never wrote down. (작성)
- refined: A package you never named at all is invisible to the whole operation. ↔ plain: If it's not in the file, pip doesn't even see it. (작성)

<sub>출처: transcript:skewnono-v3-nuxt/910b1dcc</sub>

---

## 단락 2

One root cause behind both symptoms: the `<img>` element makes the cold-path request itself, before the server has the file cached. **The filename** — a pending or broken `<img>` paints its `alt`, and `alt` here is the image filename. The existing spinner is a *centred* overlay, so it never covered the text laid out from the top-left of a 400px box. **The 502** — `/api/msr-image` runs the tool-FTP fetch *inside* the GET on a cache miss, and the cloud ingress kills it. Your instinct was right, with one correction worth knowing: I tested it in-browser, and Chrome logs a failed `fetch()` identically to a failed `<img>`. So the obvious cleanup — rewrite to fetch + blob URL — would not have cleaned the console. The error can only go away by not making a request that fails.

**문법·구조**: 첫 문장에 동사가 없다. `One root cause behind both symptoms:` 라는 명사구를 콜론으로 던져 결론을 맨 앞에 놓는 보고문 관습이며, 뒤이어 굵은 소제목 두 개(`The filename` / `The 502`)도 같은 방식으로 문장 안에 박혀 있다 — 목록을 만들지 않고도 두 증상을 갈라 놓는다. `the text laid out from the top-left` 의 laid out 은 which was 가 빠진 **과거분사 후치수식**이고, 앞의 `so` 절과 묶여 "가운데 스피너가 왼쪽 위 글자를 못 덮었다"는 인과를 만든다. 여섯째 문장 `would not have cleaned` 는 **가정법 과거완료**로, 하지 않은 대안을 반사실로 평가한다 — 실제로 해 보지 않았음을 문법이 알려 주므로 따로 변명할 필요가 없다. 마지막 문장의 `by not making` 은 동명사 부정이며, not 이 -ing 바로 앞에 온다는 규칙이 그대로 보인다.

**핵심 표현**:
- `with one correction worth knowing` — 상대가 옳았다고 인정한 뒤 한 가지만 바로잡는 완충구.
- `the obvious cleanup would not have cleaned the console` — 그럴듯한 대안을 미리 기각.
- `can only go away by not making a request that fails` — 해법을 "무엇을 하지 않기"로 정의.

**격식 짝**:
- refined: The error can only go away by not making a request that fails. ↔ plain: The only way to kill it is to stop asking for something that isn't ready yet. (작성)
- refined: Your instinct was right, with one correction worth knowing. ↔ plain: You had it right — just one thing to add. (작성)

<sub>출처: transcript:skewnono-v3-nuxt/4eb3da27</sub>

---

## 단락 3

`numpy._core` is the *private* module tree that numpy **2.x** introduced (numpy 1.x only had `numpy.core`). Pickled arrays store the fully-qualified module path of their reconstructor, so a pickle written under numpy 2 says `numpy._core.multiarray._reconstruct`. Loading it where only numpy 1 exists raises exactly your `ModuleNotFoundError`. The asymmetry matters: numpy 2 still ships a `numpy.core` compatibility shim, so numpy-1 pickles load fine under numpy 2 — but not the reverse. So the fix direction is always "upgrade the reader", never "downgrade the writer".

**문법·구조**: 첫 문장은 `X is the … tree that numpy 2.x introduced` 라는 관계절 정의문이고, 괄호 안에 반대편 사실(1.x 에는 `numpy.core` 만 있었다)을 붙여 대조를 끝낸다. 둘째·셋째 문장은 `so` 로 인과를 잇는데, 셋째의 주어 `Loading it where only numpy 1 exists` 는 동명사 덩어리이며 그 안에 장소 부사절이 통째로 들어가 있다 — 조건을 별도 if 절로 떼지 않고 주어에 말아 넣은 형태다. `exactly your ModuleNotFoundError` 의 소유격은 "네가 본 바로 그 에러"를 가리켜, 일반론이 아니라 이 신고 건임을 못 박는다. 넷째 문장은 콜론 뒤에 근거를 깔고 대시로 `but not the reverse` 라는 생략구를 붙인다(생략된 것은 numpy-2 pickles do not load under numpy 1). 마지막은 always/never 대구에 인용부호를 씌워 지침을 표어처럼 굳힌다.

**핵심 표현**:
- `the asymmetry matters` — 방향이 한쪽으로만 성립한다는 사실이 결론을 좌우할 때의 신호 문장.
- `but not the reverse` — 반대 방향은 성립하지 않는다를 세 단어로.
- `the fix direction is always X, never Y` — 개별 사례가 아니라 원칙을 남기는 마무리.

**격식 짝**:
- refined: The fix direction is always "upgrade the reader", never "downgrade the writer". ↔ plain: Always bump the side that reads it; never hold back the side that writes it. (작성)

<sub>출처: transcript:skewnono-v3-nuxt/910b1dcc</sub>
