# 2026-09-05 — 정독

## 단락 1

That settles it. A second vLLM worker sits at roughly 3 to 5 GB RSS warm, and its peak during weight load and CUDA graph capture is higher than that. With 4 GB free and no swap, a TP=2 launch would put the OOM killer in play at startup, and the process it kills is not guaranteed to be the new one. The single-GPU layout stays. That also frames the remaining latency options cleanly. Anything that adds a host process is out. Everything left runs inside the existing qwen process.

**문법·구조**: 세 단어짜리 첫 문장 `That settles it.` 이 결론을 먼저 던지고, 나머지가 근거를 댄다. 두 번째 문장은 `sits at ... , and its peak ... is higher than that` 로 평상시 값과 최악값을 한 문장에 넣었는데, `that` 이 앞의 3~5 GB 를 받아 숫자를 반복하지 않는다. 세 번째 문장의 `would put` 은 가정법 조동사다. 실제로 켜 보지 않았으니 단정 대신 "켠다면 ~할 것이다"로 거리를 둔다. 뒤이은 `the process it kills is not guaranteed to be the new one` 은 관계절 안에서 목적격 관계사가 생략된 형태(the process [that] it kills)이고, `not guaranteed to be` 는 "죽는 게 새 프로세스라는 보장이 없다"는 더 나쁜 시나리오를 수동태로 차분하게 깐다. 마지막 세 문장은 리듬을 짧게 끊어 결정·기준·남는 것을 차례로 세운다. `Anything that ... is out.` 과 `Everything left runs ...` 의 any/every 대비가 배제와 잔여를 짝지어 준다.

**핵심 표현**: `put the OOM killer in play` — 잠자던 위험을 깨우는 원인을 주어로 세우는 표현. / `frames the remaining options cleanly` — 결정 하나가 남은 선택지의 틀을 잡아 준다는 뜻이다. `cleanly` 가 "군더더기 없이"를 더한다. / `Anything that adds a host process is out.` — 부류 전체를 한 문장으로 탈락시키는 구어체.

**격식 짝**: (작성)
- refined: The measured headroom rules out any option that introduces an additional host process.
- plain: With 4 GB left, anything that spins up another process is out.

<sub>출처: transcript:llm_serving 1aaa1e3c ([assistant])</sub>

---

## 단락 2

Qwen loses isolation, and this is the big one. A TP step finishes when the slowest rank finishes. Each rank now shares a GPU with a small model. A burst of mai-ui screenshots or OCR pages on either card stalls qwen's step on both. Today qwen's latency is predictable because GPU 1 is its own. After the change, qwen's p99 depends on the other two models' traffic.

**문법·구조**: 단점 목록의 첫 항목인데 문장 여섯 개가 전부 단순 현재형이다. 아직 일어나지 않은 변경의 결과를 말하면서도 미래형을 쓰지 않는 것은, 이것이 예측이 아니라 TP 의 성질에서 나오는 규칙이기 때문이다. 둘째 문장 `finishes when the slowest rank finishes` 는 같은 동사를 두 번 써서 동기화의 정의를 그대로 문장 형태로 만들었다. `on either card ... on both` 는 either/both 를 한 문장에 넣어 "어느 한쪽에서 생긴 부하가 양쪽을 멈춘다"는 비대칭을 보여 준다. 마지막 두 문장은 `Today ... / After the change ...` 로 시간 부사구를 문두에 세워 전후 대비를 만든다. `GPU 1 is its own` 의 `its own` 은 소유대명사의 독립 용법으로, "자기 것"이라는 뜻을 명사 없이 닫는다.

**핵심 표현**: `and this is the big one` — 목록의 무게를 한 항목에 몰아주는 삽입구. / `is its own` — 독점·전용을 세 단어로 말하는 법. / `depends on the other two models' traffic` — 복수 소유격(`models'`)에 주의. 두 모델의 트래픽이므로 아포스트로피가 s 뒤에 온다.

**격식 짝**: (작성)
- refined: Sharing both cards forfeits qwen's isolation, so its tail latency becomes a function of the other models' load.
- plain: Once qwen shares the cards, its slow requests are whatever mai-ui and OCR happen to be doing.

<sub>출처: transcript:llm_serving 1aaa1e3c ([assistant])</sub>

---

## 단락 3

Correlative materials microscopy pairs images of one specimen across modalities (SEM, EBSD, TEM, optical) that share little appearance and can differ in field of view (FOV) by orders of magnitude, defeating classical registration. We tested whether a scale-aware pyramidal wrapper around pretrained dense matchers (RoMa, ELoFTR, MatchAnything) could lift cross-modal registration on AmalgaMatch (187 pairs, 19 subsets). A naive tiling pyramid degrades matchers badly: because they never abstain, every tile floods robust estimation with thousands of confident matches (median error 76→1794 px). A redesigned verified coarse-to-fine wrapper recovers a small but significant gain (SR@10 0.10→0.12, p = 0.017), yet FOV ≤ 5% success stays zero. The largest lever was the backbone: cross-modal-trained MatchAnything-RoMa gave the only significant gain over zero-shot (SR@10 + 0.032, p = 0.018). Decoder-only fine-tuning cut in-distribution TEM error ~5×, but across eight seeds regressed SR@20 (0.393→0.26) by forgetting untrained modalities, which L2-SP did not fix.

**문법·구조**: 논문 초록의 전형이다. 첫 문장은 현재형으로 문제의 일반적 성질을 말하고, 둘째 문장부터 `We tested`, `gave`, `cut`, `regressed` 처럼 과거형으로 이 연구가 한 일을 보고한다. 이 시제 전환이 "배경 대 결과"의 경계다. 첫 문장의 관계절 `that share little appearance and can differ ... by orders of magnitude` 는 두 동사를 and 로 묶고, 끝의 분사구 `defeating classical registration` 이 그 결과를 한 번에 받는다. 셋째 문장의 콜론 뒤 `because they never abstain, every tile floods ...` 는 원인절을 먼저 두어 인과를 앞세운다. `yet FOV ≤ 5% success stays zero` 의 yet 은 but 보다 격식이 높고 "그럼에도"의 실망감이 스민다. 마지막 문장은 `cut ... but ... regressed ... by forgetting ..., which L2-SP did not fix` 로 긍정·부정·원인·실패한 처방을 한 문장에 눌러 담았다. `which` 가 앞 절 전체(망각 현상)를 받는 용법이다.

**핵심 표현**: `by orders of magnitude` — 몇 배가 아니라 10배·100배 단위로 다르다는 과학 문체의 정형구. / `they never abstain` — 판단 유보가 없는 모델의 위험을 한마디로. / `The largest lever was the backbone` — 여러 변인 중 효과가 가장 컸던 것을 lever 로 부르는 서술.

**격식 짝**: (작성)
- refined: The matchers' inability to abstain floods the estimator with confident yet spurious correspondences.
- plain: These models never say "not sure", so every tile dumps a pile of confident wrong matches on the solver.

<sub>출처: repo:auto_recipe_creator poc/workflow_2/docs/study/research/2026-09-03-E-yolo-and-learned-matcher-feasibility.md (프리프린트 초록 인용)</sub>
