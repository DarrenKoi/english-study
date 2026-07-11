# 2026-07-12 — 정독

## 단락 1

`RecordingSession` does *not* save every screenshot. It samples fast (`poll_sec=0.3s`) but only **writes** a frame when the content actually changed vs. the last saved frame (`_frame_changed`, `recording.py:61`), plus one heartbeat frame every 5s as "nothing happened here" evidence. So the "unnecessary" idle/duplicate frames are largely never written to disk in the first place. Look at `_to_diff_gray` (`recording.py:52`) and `_frame_changed` (`recording.py:61`). The cycle just stops the session and takes the frame list — it runs **no** post-filter (`cycle.py:504`).

**문법·구조**: 첫 문장의 does *not* save는 조동사 do로 부정을 강조하는 장치 — 상대의 예상("전부 저장하겠지")을 정면으로 뒤집을 때 씁니다. 둘째 문장은 samples fast ↔ only writes의 대조 병렬이고, 끝의 plus는 접속사처럼 항목을 하나 더 얹습니다(as "nothing happened here" evidence는 "~라는 증거로"의 as+명사구). 셋째 문장 are largely never written은 수동태에 largely(대체로)와 never를 겹쳐 "거의 예외 없이 아예 안 쓰인다"를 만듭니다. 마지막 대시(—)는 앞 문장의 함의를 한 번 더 못 박는 재진술입니다.
**핵심 표현**: in the first place (애초에 — 부정문과 결합해 "생길 일 자체가 없다"), a heartbeat frame ("살아 있음" 신호의 은유), a post-filter (사후 필터 — post-hoc과 같은 계열).
**격식 짝**: (작성) refined: "Redundant frames are never persisted at capture time." ↔ plain: "The junk frames never get written in the first place."

<sub>출처: transcript:auto_recipe_creator 686f8e5b… (recording_filter 설계 대화)</sub>

---

## 단락 2

This window is extremely narrow (nanoseconds on a local filesystem) but is a genuine correctness gap — the `_IN_FLIGHT` dedup was designed to be the guard, but the guard is bypassed because the thread just finished. The result in the worst case is a failed swap (caught by the `except` block in `gather_success_images` and returned as `error:swap:...`), leaving the cache empty and causing the caller to proceed without consensus (falls back to rcp, which is safe).

The practical impact is low (this scenario requires `wait_for_gather` to be called immediately after a gather completes, which is unlikely in the alarm-driven loop), and the fallback is safe (rcp). The code is **safe**, just not watertight under a very specific race. No change is strictly required, but if hardening is desired: remove the dead-entry pruning at line 135 — leave the completed (not-alive) thread reference in `thread` so that `join` is a no-op (joining a finished thread returns immediately) and the re-fire branch is never reached. This is the simplest fix and eliminates the window entirely.

**문법·구조**: 코드 리뷰 판정문의 전형입니다. was designed to be / is bypassed / is never reached — 행위자를 지운 수동태 연쇄로 "누가"가 아니라 메커니즘 자체에 초점을 둡니다. leaving the cache empty and causing the caller to proceed는 결과를 이어붙이는 분사구문(= and it leaves … and causes …). if hardening is desired는 you를 숨긴 격식 수동 조건문으로, 제안을 강요 없이 내미는 어법. so that `join` is a no-op은 목적·결과의 so that절이고, 문장마다 붙는 괄호는 주장 옆에 근거·예외를 즉석 병기하는 리뷰 특유의 습관입니다.
**핵심 표현**: watertight ("safe, just not watertight"의 부분 부정 — 안전하지만 완벽하진 않다), out from under (이 리뷰 앞부분의 "delete X out from under Y" — 쓰는 중인 것을 발밑에서 빼내다), a no-op (아무 일도 하지 않는 연산).
**격식 짝**: (작성) refined: "No change is strictly required." ↔ plain: "You don't have to touch it." / refined: "if hardening is desired" ↔ plain: "if you want to harden it"

<sub>출처: transcript:auto_recipe_creator subagents/agent-a73d1793… (Task 6 동시성 리뷰)</sub>

---

## 단락 3

The implementation is correct and well-scoped. The `n_images == 0` gate change and TTL guard are both clean. The `_events_new`/`_events_old` swap is a genuine improvement over a plain `rmtree(events_dir)` because it minimizes the absence window to a single `rename`. The most actionable finding is **Issue 1**: the `except` block in the swap sequence does not clean up `.events_new`/`.events_old`, leaving them behind on a mid-swap crash if the next call happens to be TTL-fresh. That is the only path worth patching before the office deploy. **Issue 2** is a refactoring opportunity (delegate `count_staged_events` body to `_count_events`) with no runtime impact today.

**문법·구조**: 총평(Assessment)의 모범 구조 — ① 평가 형용사 병렬(correct and well-scoped)로 결론부터, ② a genuine improvement over X because …로 비교 대상과 근거를 한 문장에, ③ leaving them behind …의 분사구문으로 결함의 여파를 잇고, ④ happens to be(마침 ~인 경우)로 발생 조건의 우연성을 표시합니다. worth patching은 worth+동명사, with no runtime impact today는 with+명사구를 문장 꼬리에 달아 범위를 한정하는 기법입니다.
**핵심 표현**: the most actionable finding (지금 당장 손댈 수 있는 발견), worth patching before the office deploy (배포 전에 고칠 가치가 있는), a refactoring opportunity (문제가 아니라 '기회'로 재프레임).
**격식 짝**: (작성) refined: "That is the only path worth patching before the office deploy." ↔ plain: "That's the one thing I'd fix before it goes to the office."

<sub>출처: transcript:auto_recipe_creator subagents/agent-a76967829… (Task 5 품질 리뷰 총평)</sub>
