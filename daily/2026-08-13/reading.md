# 2026-08-13 — 정독

## 단락 1

Use the final `change_events[-1]` only, require a matching cursor result for that exact rank, and return `None` when Stage 2a was truncated before it. Read the final current frame to obtain its dimensions. Define the close area as the rightmost/topmost 10%, with minimum size 64x48 pixels. Require `change.change_bbox` to intersect this region. Build an absolute-difference mask from the previous/current frames, crop it to the intersection, and use `cv2.HoughLinesP`. A partial X candidate exists only when the detected line set contains at least one positive-slope and one negative-slope diagonal with absolute angle between 20 and 70 degrees and endpoints within 24 pixels of one another. This accepts a lower-half X/V-like pair but rejects the fixture's fixed close-button X because that X exists in both frames and disappears from the frame difference.

**문법·구조**: 앞 다섯 문장은 전부 주어 없는 **명령형**입니다. 명세서에서 "당신이 이렇게 구현하라"를 사람 이름 없이 지시하는 기본 형태예요. 셋째 문장의 `with minimum size 64x48 pixels` 처럼 `with + 명사구`를 붙이면 조건을 절로 늘리지 않고 붙일 수 있습니다. 여섯째 문장에서 시제가 명령형에서 현재형 `exists`로 바뀌는데, 이 지점부터는 지시가 아니라 **판정 규칙의 정의**라서 그렇습니다. 명령형이 계속됐다면 "만들어라"로 읽혀 규칙이 흐려집니다. 마지막 문장의 `This accepts A but rejects B because …`는 하나의 주어(This)가 상반된 두 결과를 동시에 책임지는 구조라, 규칙이 어디까지 통하는지를 한 문장으로 보여줍니다.

**핵심 표현**: `require X to intersect this region` — 명세에서 조건을 요구할 때 `must`보다 `require`가 주어를 지우기 쉬워 자주 쓰입니다. `endpoints within 24 pixels of one another` — `of one another`가 "서로 간에"를 담당하고, `each other`보다 문어체입니다. `return None when Stage 2a was truncated before it` — `when`이 시간이 아니라 조건을 뜻하는 명세 관용입니다.

**격식 짝**: (작성)
- refined: A partial candidate is recognized only when both diagonal orientations are present.
- plain: We only call it a match if we see both diagonals.

<sub>출처: repo:auto_recipe_creator poc/workflow_3/docs/superpowers/plans/2026-08-12-probable-close-click-evidence.md</sub>

---

## 단락 2

A static UI glyph is the worst kind of distractor for per-frame VLM detection: it's present in every frame, so a model that locks onto it produces a confident, perfectly consistent, and completely wrong cursor track — indistinguishable from success in the artifacts. Its position makes it worse. Sitting between the Full Size button and the live SEM box means its ROI overlaps a region that genuinely changes, so `changed_in_window_px` can cross 1500 and manufacture false clicks — worse than the zero clicks you have now. The discriminator is free and needs no VLM: a real cursor moves; the palm icon never does. If the "cursor" is reported at the same pixel across hundreds of frames, it isn't a cursor.

**문법·구조**: 첫 문장은 **콜론으로 근거를 여는** 형태입니다. 콜론 앞이 주장, 뒤가 이유 — 접속사 `because`를 쓰지 않고도 인과가 서고, 뒤에 이어지는 `so` 절까지 한 호흡에 들어갑니다. `a model that locks onto it` 은 관계절로 주어를 좁힌 것이라, "모든 모델"이 아니라 "그 아이콘에 물린 모델"만 문제라는 범위 제한이 됩니다. 둘째 문장 `Its position makes it worse.` 는 다섯 단어짜리 짧은 문장인데, 앞뒤가 긴 문장이라 여기서 리듬이 한 번 끊깁니다. 셋째 문장은 동명사구 `Sitting between …` 를 통째로 주어 자리에 앉혔습니다. 넷째 문장의 세미콜론은 `a real cursor moves` 와 `the palm icon never does` 를 대칭으로 붙들며, `does` 는 `moves` 를 받는 대동사입니다. 마지막 문장은 `If …, it isn't a cursor.` — 조건절이 앞에 오고 결론이 단문으로 떨어져 판정 규칙처럼 읽힙니다.

**핵심 표현**: `the worst kind of distractor` — 최상급으로 위험도를 먼저 못 박고 근거를 뒤에 답니다. `lock onto` — 탐지기가 엉뚱한 대상에 고정될 때. `manufacture false clicks` — `manufacture`가 "없던 것을 만들어낸다"는 부정적 함의로 쓰입니다.

**격식 짝**: (작성)
- refined: A fixed graphic present in every frame yields a track that is consistent yet entirely spurious.
- plain: If it's in every frame, the model will just keep pointing at it and look right while being wrong.

<sub>출처: transcript:[assistant] auto_recipe_creator b0cef303</sub>

---

## 단락 3

Voiding those frames alone was quietly biased. Since the fallback happens specifically when the pointer is at the window edge, discarding them deletes edge-region operations preferentially — a systematic hole in the timeline, worse than random loss. So the decoy regions are now painted over in neutral gray and the frame is re-asked once. With nowhere to fall back to, the model either finds the real cursor or says none. Recovered events are marked `cursor_source="vlm_masked"`; if the retry still lands on a decoy, the void stands. Masking only on retry rather than on the first pass is the deliberate part. Blanking them up front would be cheaper, but a real cursor genuinely does travel over the Full Size button, and pre-masking would erase those true positives to kill a false one.

**문법·구조**: 셋째 문장의 `are painted over` 와 `is re-asked` 는 **수동태**인데, 여기서는 회피가 아니라 선택입니다. 행위자가 "나"라는 게 자명해서 굳이 `I now paint over …`라고 쓰면 초점이 조치가 아니라 사람으로 옮겨갑니다. 넷째 문장의 `With nowhere to fall back to` 는 `with + 명사 + to부정사`로 상황을 앞세우는 압축 구문이에요. 다섯째 문장의 세미콜론은 조치와 예외를 한 문장 안에 붙여 "예외까지가 규칙"임을 보입니다. 여섯째 문장은 동명사구 `Masking only on retry rather than on the first pass` 가 통째 주어이고, `rather than` 이 두 선택지를 같은 문법 형태로 나란히 세웁니다. 마지막 문장의 `does travel` 은 **강조 do** — "정말로 지나간다"로 앞의 반론을 미리 인정하는 장치입니다.

**핵심 표현**: `quietly biased` — 편향이 있는데 티가 안 난다는 뜻을 부사 하나로. `the void stands` — 판정이 그대로 유지된다는 뜻의 `stand`. `to kill a false one` — 목적의 to부정사가 문장 끝에서 대가를 밝힙니다.

**격식 짝**: (작성)
- refined: Pre-masking would eliminate true positives in order to suppress a single false one.
- plain: Blanking it out early would throw away good hits just to stop one bad one.

<sub>출처: transcript:[assistant] auto_recipe_creator b0cef303</sub>
