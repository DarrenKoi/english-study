# 2026-07-02 — 정독

## 단락 1

The downloader isn't "disconnected" — it was never written. Only `office_align_fail_alarm.py` and `office_rich_notify.py` exist in the repo; there is no `office_success_downloader.py` anywhere, and nothing exports `make_success_downloader()`. So `DOWNLOADER_AVAILABLE=False` is expected. Crucially, the downloader is irrelevant to your double-click idea — it only fetches consensus S-images, a bonus template source. The align point itself comes from the rcp align-key template matched against the live fail frame, which needs no downloader at all.

**문법·구조**: 진단을 *반박(reframe)*으로 여는 전형적 패턴이다. `isn't "disconnected" — it was never written` 은 상대의 프레임("연결이 끊겼다")을 부정하고 대시(—) 뒤에서 더 정확한 프레임("애초에 없다")으로 갈아끼운다. 세미콜론(`;`)은 밀접한 두 절("파일 두 개만 있다" / "그 파일은 없다")을 마침표보다 긴밀히 잇는다. `there is no ... anywhere` 는 부정+`anywhere`로 "어디에도 없다"를 강조. 마지막 `which needs no downloader at all` 은 비제한적 관계절로 앞 명제에 근거를 덧붙이며, 문장 전체의 결론(다운로더는 무관)을 못 박는다. 시제도 눈여겨보라: 사실 상태는 현재(`isn't`, `exist`, `comes`), 과거의 부재는 과거·수동(`was never written`).

**핵심 표현**: `it was never written`(연결이 끊긴 게 아니라 *처음부터 없다* — 원인 오진을 바로잡는 말), `irrelevant to your idea`(네 아이디어와 무관하다 — 논점 분리), `a bonus template source`(있으면 좋지만 필수는 아닌 부가 자원).

**격식 짝**: refined ↔ plain
- refined: *The downloader is irrelevant to this approach; the align point is derived independently.* (작성)
- plain: *The downloader has nothing to do with it — the align point comes from somewhere else.* (작성)

<sub>출처: transcript:[assistant] 3ca4387a…</sub>

---

## 단락 2

The coordinate mapping you worried about is now a single, well-defined hop. The align point is computed by matching the rcp template against the captured fail frame itself, so it's already in live-frame pixels — there's no msr-to-live registration step. The only transform left is frame-pixel to screen-absolute, which `image_point_to_screen()` does via the window's rect-to-image ratio, handling DPI. Because matching and the click target live in the same full-window screenshot, no panel-ROI offset or landmark calibration is needed. That's why this works at the office today without the uncalibrated monitor path.

**문법·구조**: 첫 문장 `The coordinate mapping you worried about` 은 관계대명사(that/which)가 생략된 접촉 관계절 — 구어·기술 문체에서 흔하다. `so it's already in live-frame pixels` 의 `so` 는 앞 사실에서 결론을 끌어내는 연결어. `which ... does via ...` 는 비제한 관계절로 도구(함수)가 *어떻게* 변환하는지를 곁들인다. `Because ..., no ... is needed` 는 원인절을 앞세워 "그래서 X가 불필요"라는 부정 결론을 강조하는 배열. 마지막 `That's why ...` 는 전체를 하나의 인과로 마무리한다 — *현상 → 이유*로 단락을 닫는 좋은 습관이다.

**핵심 표현**: `a single, well-defined hop`(여러 단계가 아니라 잘 정의된 *한 번의* 도약), `there's no ... registration step`(정합 단계가 아예 없다), `that's why this works ... today`("그래서 지금 당장 된다" — 실용적 결론).

**격식 짝**: refined ↔ plain
- refined: *No registration step is required, since detection and the target share one coordinate space.* (작성)
- plain: *You don't need to line anything up — they're in the same coordinate space already.* (작성)

<sub>출처: transcript:[assistant] 3ca4387a…</sub>
