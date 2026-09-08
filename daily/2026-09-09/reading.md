# 2026-09-09 — 정독

## 단락 1

Multi-Token Prediction is speculative decoding using a small extra head that ships inside the Qwen3.8 checkpoint. Normal decoding produces one token per forward pass, and each pass reads all ~48 GiB of weights from HBM, so single-stream speed is bound by memory bandwidth, not compute. With MTP the cheap head guesses the next few tokens, and the big model verifies them all in one pass. Accepted guesses are free tokens. Output is mathematically identical to plain decoding, so quality is not a concern. The only thing you buy is speed: roughly 1.5 to 2x per stream when the draft is accepted often, which it is for this model.

**문법·구조**: 전부 현재시제다. 기법의 작동 방식은 특정 시점의 사건이 아니라 항상 참인 성질이라
현재형으로 쓴다 — 여기서 과거형이 하나라도 섞이면 "그때 그랬다"는 사건 서술로 읽혀 설명이 무너진다.
연결은 `so` 세 번이 지탱한다. 매번 **측정 사실 → 그로부터 따라오는 결론** 순서라, 독자가 근거를
먼저 받고 판단을 나중에 받는다(`each pass reads … so speed is bound by …`). 마지막 문장의
`which it is` 가 이 단락에서 가장 배울 만한 자리다. 앞의 `when the draft is accepted often` 이라는
조건절을 받아 `which it is (accepted often)` 로 되받으면서, 조건을 걸어 놓고 그 조건이 실제로
충족된다고 곧바로 확인해 준다. 조건절의 안전장치는 유지하되 실무적으로는 단정하는 이중 효과다.
네 번째 문장 `Accepted guesses are free tokens.` 는 앞뒤와 길이 대비가 극단적이다. 30단어짜리
문장 사이에 4단어를 놓아 요약 지점을 시각적으로 만든다.

**핵심 표현**: `ships inside the checkpoint` — 소프트웨어가 무언가에 "실려 함께 온다"는 뜻의
`ship`. 별도 설치가 필요 없다는 사실을 동사 하나로 끝낸다. / `is bound by memory bandwidth,
not compute` — `bound by` 는 "무엇이 한계를 정하는가"를 지목하는 성능 분석의 정형구이고,
`A, not B` 대구가 흔한 오해(연산이 병목일 것이다)를 미리 잘라낸다. / `quality is not a concern` —
"품질은 좋다"가 아니라 "품질은 **따질 항목이 아니다**"라고 말해, 검토 목록에서 항목 하나를 지운다.

**격식 짝**: 이득을 좁혀 못 박기 — refined: *The sole benefit is decode latency; output distributions
are unchanged.* / plain: *All you get out of it is speed — the answers come out the same.*

<sub>출처: transcript:llm-serving 5565b9d0 (MTP 검토)</sub>

---

## 단락 2

Almost certainly not. A virtualenv changes which Python runs and which packages it sees. It cannot change whether `/project/…/models/Qwen3.8-27B` exists, and `os.path.isdir` gives the same answer under any interpreter. Two indirect ways it could matter. **Different interpreters for the two runs.** `start_all.py` launches `serve_vlm.py` with `sys.executable`, the same Python that ran `start_all.py`. If you start it with `.venv/bin/python` but ran the diagnostic with a plain `python`, the runs are not comparable. On some cloud images `python` is a wrapper that runs inside a sandbox with a different filesystem view. Rare, but that would produce exactly this symptom.

**문법·구조**: 첫 문장이 문장이 아니다. `Almost certainly not.` — 동사도 주어도 없이 부사구만으로
답한다. 질문이 yes/no 였기 때문에 가능한 생략이고, 확신의 정도(`almost certainly`)를 앞세워
"아니다"보다 정직하게 들린다. 그다음 조동사 배치가 이 단락의 뼈대다. `changes`(직설법 현재,
사실) → `cannot change`(논리적 불가능) → `could matter`(가능성) → `would produce`(가정법
귀결). 즉 **확실한 것에서 시작해 점점 약한 양태로 내려간다.** 독자는 어디까지가 사실이고 어디부터
추측인지를 조동사만 보고 구분한다. 조건문 `If you start it with X but ran the diagnostic with Y` 는
시제가 섞여 있다 — 앞은 현재(습관적으로 그렇게 시작한다면), 뒤는 과거(그때 그렇게 실행했다면).
문법 실수처럼 보이지만 두 사건이 실제로 서로 다른 시간에 있어서 이게 맞다. 마지막 `Rare, but that
would produce exactly this symptom.` 도 앞이 잘려 있다 — 형용사 하나로 문장을 열어 가능성을
낮게 평가한 뒤 `but` 으로 뒤집는다.

**핵심 표현**: `the runs are not comparable` — 두 실행 결과를 나란히 놓고 비교할 자격이 없다.
결과가 다르다고 말하기 전에 *비교 자체가 성립하는지*를 먼저 따지는 순서가 진단의 기본이다. /
`a different filesystem view` — 파일이 있고 없고가 아니라 "보는 창이 다르다". 컨테이너·샌드박스
문제를 설명할 때 가장 짧은 표현이다. / `exactly this symptom` — `exactly` 가 없으면 "비슷한 증상"이
되고, 있으면 "지금 네가 보는 그 증상 자체"가 된다. 가설을 후보로 승격시키는 단어다.

**격식 짝**: 가능성은 인정하되 낮게 두기 — refined: *This is uncommon, but it would account for the
observed behaviour precisely.* / plain: *Rare, but that would do it.*

<sub>출처: transcript:llm-serving b0fb3a9d (모델 경로 진단)</sub>

---

## 단락 3

The stated concern is not reproducible in source. No reachable Phase 3 Linux path can import or call `proxy_downloader`. Both selection sites are pure `platform.system() == "Windows"` branches with no env override, no fallback, and no proxy code inside `direct_downloader`. But the concern cannot be closed from here, and the reason is a real defect: the deployment chain ships a gitignored file it cannot validate, and the one mechanism built to catch a bad copy — `STALE office.py` — is structurally dead on the cloud. `msr_image` additionally emits no transport evidence at all.

**문법·구조**: 감사 보고서의 결론 단락이고, 형태가 정확히 **판정 → 근거 → 반전 → 잔여**다.
1~3문장은 전부 부정문인데 부정하는 층위가 다르다. `is not reproducible`(현상 부정) →
`No … path can`(존재 부정) → `with no override, no fallback, and no proxy code`(전치사구
안의 삼중 부정). 마지막 삼중 반복은 세 갈래 도피로를 하나씩 막는 소리라, 셋을 `and` 로 묶어
한 호흡에 읽히게 한 게 의도다. 4문장의 `But` 이 방향을 튼다. 접속사를 문두에 세우는 건 격식체에서
피하라고 배우지만 보고서 결론에서는 오히려 표준이다 — 앞 세 문장이 안심시켰으니 여기서 시선을
확 돌려야 하기 때문이다. 콜론 뒤는 `defect` 의 내용을 푸는 동격이고, 그 안에서 `ships a
gitignored file it cannot validate` 는 관계대명사 `that` 을 생략한 목적격 관계절이다.
마지막 문장의 `additionally` 는 문중에 놓였다. 문두 `Additionally,` 보다 덜 무겁고, 앞 문장과
같은 무게의 항목이 아니라 **덧붙이는 한 가지**임을 위치로 표시한다.

**핵심 표현**: `not reproducible in source` — "코드를 읽어서는 재현되지 않는다". 어디까지
확인했는지를 범위와 함께 밝히는 정직한 판정어다. / `the concern cannot be closed from here` —
티켓을 닫는다는 `close` 에 `from here` 를 달아, 결론이 아니라 *내 위치의 한계*임을 말한다. /
`structurally dead` — 꺼져 있는 게 아니라 구조상 절대 켜질 수 없는. 방어 장치를 평가하는 말로
`disabled`(누군가 껐다)보다 훨씬 무겁다.

**격식 짝**: 확인 못 한 부분을 밝히기 — refined: *This cannot be established from the repository
alone; direct observation of the host is required.* / plain: *I can't settle that from here — someone
has to look at the box.*

<sub>출처: transcript:skewnono-v3-nuxt 6702b593 (FTP transport 감사)</sub>
