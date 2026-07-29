# 2026-07-30 — 정독

## 단락 1

Your report was half right, and the half that was wrong points at the real cause. The X button was genuinely missing — confirmed on all three dialogs. Nuxt UI 4 renders its close button *inside* the header slot's fallback content, and `AlignPopup` overrides that slot, so the X went with it. The close-up views are worse: they override `#content`, which wraps header, body and footer, so they rendered no chrome at all. ESC, though, was working the whole time. I reproduced the bug against the mock backend and pressed Escape on both dialogs — each closed, and click-outside worked too. So why did it feel unclosable? Look at the screenshot: there *is* an X at the top-right of the screen, and it belongs to the beta banner sitting behind the overlay. A visible-but-dead X plus no real one is a stronger "I'm trapped" signal than no X at all.

**문법·구조**: 첫 문장이 글 전체의 뼈대다. `half right … the half that was wrong` 로 같은 명사를 되받아 관계절을 걸면, 정정과 원인 제시가 한 문장에 들어간다. 시제 배치를 보면 판정은 현재·과거 단순형(`was half right`, `went with it`)이고, 재현 실험만 과거(`I reproduced`, `pressed`)로 적혀 "주장 → 증거" 순서가 시제로도 갈린다. `ESC, though, was working the whole time` 의 `was working` 진행형은 "그 시간 내내 계속"이라는 지속을 살리려는 선택이라, 단순과거 `worked` 보다 사용자의 오해를 정면으로 반박한다. 중간의 `So why did it feel unclosable?` 는 수사 의문문으로, 답을 스스로 내기 전에 독자의 질문을 대신 꺼내 흐름을 꺾는다. 마지막 문장은 `A + plus B is a stronger X than C` 라는 비교 구문 하나로 결론을 압축한다.

**핵심 표현**: `half right`(절반은 맞다 — 상대를 부정하지 않고 정정하는 자리), `replace/override … wholesale`(슬롯을 덮으면 딸린 것까지 통째 사라진다), `a visible-but-dead X`(하이픈으로 즉석 형용사를 만들어 UI 상태를 한 덩어리로 부르는 방식).

**격식 짝**: 
- refined: *The reported symptom is only partly accurate, and the inaccurate portion identifies the underlying cause.*
- plain: *You were half right — and the wrong half is what actually explains it.* (작성)

<sub>출처: transcript:skewnono_v3_nuxt c3d8d75e (assistant) · 원문 발췌를 한 단락으로 이어 붙임</sub>

---

## 단락 2

The bug was quiet: `get_align_detail` sent ENAP settings to `read_af_pr_condition` and align condition files to `read_meas_image_condition`. Both were wrong. Nothing failed, because a wrong parser still accepts the bytes and still returns something renderable — the screen filled in, 180 tests passed, and the defect existed only in the values, and only at the office. Two things I did not guess. For point numbers of three or above there is no documented optic, so `align_optics` returns `None` and the adapter leaves that condition unread with a warning naming the point; a guessed "SEM" would render OM optics under a SEM heading and read as perfectly ordinary data. The batch reader's return shape is still unverified, so the splitter accepts either an ordered sequence or a name-keyed mapping, and anything else is attached whole with its type logged — that log is what answers the question at the office.

**문법·구조**: `Nothing failed, because …` 에서 콤마 뒤 `because` 는 앞 문장 전체에 이유를 다는 자리다. 콤마 없이 붙이면 "실패하지 않은 이유"가 아니라 "실패의 조건"으로 읽힐 여지가 생긴다. 이어지는 `still accepts … and still returns …` 는 `still` 을 두 번 반복해 "틀렸는데도 멀쩡히 굴러간다"는 역설을 리듬으로 밀어붙인다. 세미콜론(`… naming the point; a guessed "SEM" would …`)은 사실과 가정을 한 호흡에 묶는 장치로, 뒤쪽은 가정법 `would` 라 실제 일어난 일이 아님이 표시된다. 마지막의 `that log is what answers the question` 은 what-분열문이다. 평범하게 `the log answers it` 이라 쓰면 밋밋한데, `what` 절로 초점을 옮겨 "다른 게 아니라 바로 그 로그"가 된다.

**핵심 표현**: `the defect existed only in the values`(동작이 아니라 값에만 결함이 있었다 — 조용한 버그를 정확히 정의), `read as perfectly ordinary data`(자동사 `read` = 남에게 …으로 읽히다), `Two things I did not guess`(추측하지 않고 남겨 둔 것을 따로 표제로 세우는 정직한 보고 형식).

**격식 짝**: 
- refined: *The return shape remains unverified, so the implementation accommodates both plausible forms and logs the type it actually receives.*
- plain: *We still don't know what it returns, so it handles both and just logs whatever shows up.* (작성)

<sub>출처: transcript:skewnono_v3_nuxt 0ff1832b (assistant) · 원문 발췌를 한 단락으로 이어 붙임</sub>

---

## 단락 3

"Unmerged" and "unlanded" are different questions. `git branch --merged` walks ancestry, so a rebased or re-applied commit reads as unmerged forever even though its content is already on main — which is why all ten branches looked alarming at first. `git cherry` compares patch-ids, a hash of the diff that ignores the SHA and the commit metadata, so it catches the rebased duplicates that ancestry misses. It still reports a false miss when context lines have shifted, which is why comparing the blobs was the real tiebreaker. Every file on those branches turned out to exist on main already, and main's copies were generally the larger, later versions. Only one branch resisted that reading: its test names have no overlap with main's, so I can't call it a clean duplicate without reading both suites properly.

**문법·구조**: 도구 이름이 주어로 서고 동사가 `walks`, `compares`, `reports`, `misses` 처럼 현재형이다. 이 현재형은 "그때 그랬다"가 아니라 "원래 그렇게 동작한다"는 일반 진실이라, 도구 설명에는 과거형보다 이쪽이 맞다. `which is why …` 가 두 번 나오는데, 앞 절 전체를 선행사로 받는 비제한적 관계절이다. 관찰(도구가 이렇게 동작한다) → 귀결(그래서 이렇게 보였다)을 매번 붙여 주니 근거와 결론이 끊기지 않는다. `a hash of the diff that ignores …` 는 동격 명사구로, 괄호나 별도 문장을 쓰지 않고 용어를 그 자리에서 정의하는 경제적인 방법이다. 마지막 문장의 `resisted that reading` 은 무생물 주어 은유 — 브랜치가 해석에 "저항한다"고 말해 예외를 부드럽게 도입한다.

**핵심 표현**: `walk ancestry`(커밋 조상 계보를 따라 훑다), `read as unmerged`(…처럼 보이다 — 상태 서술의 자동사 read), `a false miss`(있는데 없다고 나오는 오탐의 반대 — false positive 와 짝).

**격식 짝**: 
- refined: *Ancestry-based checks cannot distinguish a rebased commit from a genuinely absent one; content comparison was therefore decisive.*
- plain: *Ancestry can't tell a rebase from a missing commit, so we had to compare the files themselves.* (작성)

<sub>출처: transcript:skewnono_v3_nuxt 134c9baf (assistant) · 원문 발췌를 한 단락으로 이어 붙임</sub>
