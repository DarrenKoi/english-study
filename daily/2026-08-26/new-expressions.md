# 2026-08-26 — 새 표현

## "self-consistent"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 설계·문서·코드가 서로 모순 없이 맞물려 있다고 리뷰 서두에서 인정할 때(코드 리뷰·설계 평가, 격식)
- 한국어: 자기 안에서 앞뒤가 맞는, 내적으로 일관된
- 설명: "옳다"가 아니라 "스스로 모순이 없다"는 판정이다. 리뷰어가 본격적인 지적 앞에 이 한 마디를 두면, 뒤에 나오는 finding 들이 설계 자체를 부정하는 게 아니라 세부를 다듬는 것임이 미리 정해진다. `consistent with X`(외부 기준과 일치)와 달리 비교 대상이 자기 자신이다.
- 예문: The design intent is self-consistent: the diff updates DESIGN.md in the same commit and applies the chip-role litmus test correctly.
- 유사어: internally consistent (같은 뜻, 조금 더 풀어 쓴 형태), coherent (논리 전체가 하나로 읽힌다는 뉘앙스)
- 반의어: internally contradictory / at odds with itself

## "an opportune moment to (do X)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 이번 변경이 원래 목적은 아니지만, 어차피 손댄 김에 해 두기 좋은 시점이라고 권할 때(리뷰 코멘트, 격식)
- 한국어: 마침 ~하기 좋은 때
- 설명: 리뷰에서 "이건 네 잘못이 아니지만"을 앞세운 뒤 개선을 권하는 완곡한 틀. `opportune` 은 "기회가 맞아떨어진"이라 `good time` 보다 격식이 높고, 지금 안 하면 다음에 또 diff 를 열어야 한다는 비용 감각이 담긴다.
- 예문: Not newly authored; noting because the diff touched every one of these lines — an opportune moment to tokenize.
- 유사어: while you're in there (구어, "들어간 김에"), a natural point to (설계 흐름상 자연스러운 지점)
- 반의어: out of scope for this change

## "Reasonable, but invented."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 구현자가 스스로 정한 값·제한이 합리적이긴 하나 요청에는 없었다고 스펙 리뷰에서 짚을 때(격식)
- 한국어: 타당하긴 한데, 지어낸 것이다.
- 설명: 두 단어짜리 판정문. 앞의 `Reasonable` 이 품질 시비를 접고, 뒤의 `invented` 가 출처 시비만 남긴다. `invented` 는 "요청문에 근거가 없다"를 꼬집는 단어라 `added` 보다 날이 서 있다. 노트의 `defensible, but unasked` 와 같은 골격인데, 이쪽은 값을 *창작*했다는 점을 강조한다.
- 예문: The scroll cap (`max-h-[9.5rem]`) is reasonable, but invented — nobody asked for it.
- 유사어: defensible, but unasked (기존 노트; 요청 여부에 초점), sensible but unrequested (더 부드러움)
- 반의어: specified / called for by the request

## "partially undercut (a requirement)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 어떤 추가 장치가 원래 요구사항의 취지를 일부 깎아먹는다고 지적할 때(스펙 리뷰, 격식)
- 한국어: (요구사항을) 부분적으로 훼손하다·깎아내리다
- 설명: `violate` 는 규칙을 어기는 것이고 `undercut` 은 밑을 파서 힘을 빼는 것이다. 요구사항을 정면으로 어기진 않았지만 그 목적(데이터에 폭을 더 준다)을 약화시킨다는 미묘한 지적에 정확히 맞는다. `partially` 가 붙어 정도를 한정한다.
- 예문: The scroll cap partially undercuts req 4 — with 60+ tools the strip itself consumes vertical space the request wanted given to the data.
- 유사어: work against (더 평이함), erode (서서히 깎는 뉘앙스), cut against the grain of (관용적)
- 반의어: reinforce / serve (the requirement)

## "the rule's substance holds"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 규칙의 자구는 못 지켰지만 그 규칙이 막으려던 일은 실제로 막혀 있다고 변호할 때(리뷰 응답·설계 논의, 격식)
- 한국어: 규칙의 본뜻은 지켜진다
- 설명: 자구(letter)와 취지(substance/spirit)를 가르는 리뷰의 기본 화법. `holds` 는 "여전히 성립한다"는 뜻의 자동사로, 정리·불변식·약속이 유지될 때 두루 쓴다. 앞에 `Mitigating:` 을 세우고 근거를 댄 뒤 이 구로 닫으면 반박이 아니라 정상 참작으로 읽힌다.
- 예문: An unscoped results pane is nearly unreachable in practice, so the rule's substance (no zeroed card masquerading as a verdict) holds.
- 유사어: the spirit of the rule is met (더 흔한 관용구), the intent survives (구어에 가까움)
- 반의어: honors the letter but not the spirit

## "pre-existing logic carried into (a new UI)"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-25-hardware-tool-strip-review.md
- 맥락: 결함이 이번 변경이 만든 게 아니라 옛 로직이 새 화면으로 옮겨 오면서 드러난 것이라고 책임 소재를 정리할 때(리뷰 결론, 격식)
- 한국어: 새 UI 로 그대로 실려 들어온 기존 로직
- 설명: `carried into` 는 물건이 옮겨지듯 로직이 이사했다는 그림이다. "고칠 가치는 있다"와 "이 변경이 만든 결함은 아니다"를 한 문장에 담을 수 있어, 리뷰 판정문에서 `worth fixing but wasn't introduced by` 와 짝을 이룬다.
- 예문: The one real defect is pre-existing logic carried into a UI that no longer shows the disambiguating context, so it's worth fixing but wasn't introduced by this change's intent.
- 유사어: inherited from the old rail (상속 비유), surfaced by this change (이 변경이 *드러냈다*는 데 초점)
- 반의어: newly introduced (by this change)

## "X was only a label."
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 이름·설정값이 실제 동작과 무관했음을 밝혀 요청의 전제를 바로잡을 때(작업 보고 첫 문장, 구어~중간 격식)
- 한국어: X 는 이름표에 불과했다.
- 설명: "1주 윈도라고 써 있지만 실제로는 최근 10회를 보고 있었다"처럼, 사용자가 믿던 것이 표기뿐이었다는 발견을 여는 문장이다. 굵게 쳐서 보고서 첫 줄에 두면 이어지는 설명(그래서 lookback 만 늘려선 소용없다)이 자연히 따라온다.
- 예문: The old "1주 윈도우" was only a label — the office adapters capped at the ten most recent runs per tool, so widening the lookback alone would not have gathered more evidence.
- 유사어: in name only (관용구), nominal (격식 형용사)
- 반의어: load-bearing (실제로 동작을 떠받치는)

## "refused, not clamped"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 범위 밖 입력을 조용히 경계값으로 맞추지 않고 오류로 돌려보낸다는 API 정책을 한 줄로 못 박을 때(변경 요약, 기술)
- 한국어: (범위 밖 값은) 거부하지, 경계값으로 자르지 않는다
- 설명: `clamp` 는 값을 min/max 안으로 눌러 넣는 처리다. 두 동사를 `not` 으로 대비시키면 "왜 400 이 나오는가"를 설명하지 않아도 설계 의도가 전달된다. 명사 뒤 콤마 대비(`A, not B`)는 짧은 정책 선언에 잘 맞는다.
- 예문: Out-of-range values are refused with 400, not clamped.
- 유사어: rejected outright (더 강한 어조), fail fast (일반 원칙명)
- 반의어: silently clamped / coerced into range

## "move together"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 4a1eae66
- 맥락: 따로 놀던 두 설정값을 하나의 축으로 묶어 같이 변하게 했다고 설명할 때(변경 요약, 기술)
- 한국어: 함께 움직이다, 연동되다
- 설명: 한쪽만 바꾸면 효과가 없던 두 값(lookback 일수와 tool 당 run 상한)을 한 매개변수에서 파생시켰다는 뜻이다. `are coupled` 보다 그림이 쉽고, `now` 를 붙이면 "전에는 아니었다"가 따라온다.
- 예문: Lookback and run cap now move together — `window_days(weeks)` plus `runs_per_tool(weeks) = 10×weeks`.
- 유사어: are coupled (격식·기술), scale together (비례 관계를 강조)
- 반의어: drift apart / are tuned independently

## "bounded by X, not by Y"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a101dd54
- 맥락: 어떤 수치의 상한이 어디서 오는지 밝혀 "여기는 고칠 문제가 없다"고 판단할 때(설계 판단, 기술)
- 한국어: 상한을 정하는 건 X 이지 Y 가 아니다
- 설명: 같은 `ImgThumb` 이라도 열 개수가 사용자의 선택으로 정해지는 곳과 장비군(HV-SEM 4장)으로 정해지는 곳은 다르다는 논증이다. `bounded by` 는 수학의 유계 개념이라 "누가 그 수를 제한하는가"를 정확히 가리킨다.
- 예문: The column count is however many recipes the user chose to compare — bounded by the user, not by the tool family.
- 유사어: capped by (상한을 강조), driven by (원인을 강조)
- 반의어: unbounded

## "no more informative than none"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a101dd54
- 맥락: 라벨·표시가 있어도 구별이 안 되면 없는 것과 같다고 설계 선택을 정당화할 때(기술 설명, 중간 격식)
- 한국어: 없는 것보다 나을 게 없다
- 설명: 비교급 `no more ~ than` 은 "~와 다를 바 없다"는 부정이다. 두 셀이 똑같이 `U` 라고 적혀 있으면 정보량이 0 이라는 논리를 한 구로 끝낸다. 왜 리스트 인식형 함수(`imageVariantLabels`)를 써야 했는지의 근거가 이 한 줄에 있다.
- 예문: The per-name form returns "U" for both — two cells reading `U` are no more informative than none.
- 유사어: adds nothing (평이), is indistinguishable from having no label (풀어쓰기)
- 반의어: disambiguating

## "blocked at the payload, not the UI"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a101dd54
- 맥락: 어떤 기능이 화면이 아니라 데이터 계약 때문에 막혀 있다고 병목의 층을 짚을 때(옵션 비교, 기술)
- 한국어: 막힌 곳은 UI 가 아니라 페이로드다
- 설명: 사용자가 "버튼만 달면 되지 않나"라고 생각하기 쉬운 기능에 대해, 진짜 병목은 백엔드 계약(slot→파일명 하나)이라 비용이 다르다고 설명하는 구다. `at the X` 로 층을 지목하는 화법은 `blocked` 외에 `decided`, `enforced` 와도 잘 붙는다.
- 예문: The variant selector is blocked at the payload, not the UI — `images[slot]` is a slot→single filename map, so it structurally cannot carry the other three files.
- 유사어: the bottleneck is the contract (풀어쓰기), a backend change in disguise (구어)
- 반의어: a purely cosmetic change

## "the more expensive half"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a101dd54
- 맥락: 두 선택지 중 안 고른 쪽이 왜 비싼지 덧붙일 때(옵션 정리 말미, 구어~중간 격식)
- 한국어: (둘 중) 비용이 더 큰 쪽
- 설명: 선택지가 두 개일 때 `the other option` 대신 `half` 로 부르면 "둘이 한 짝"임이 드러나고, `more expensive` 가 안 고른 이유를 함께 준다. 결론 뒤에 한 줄로 붙이는 마무리 구.
- 예문: That's a backend contract change (mock + `office_example.py`), which is why it's the more expensive half.
- 유사어: the costlier route (격식), the heavier lift (구어 관용구)
- 반의어: the cheap half / the quick win

## "the fix is narrower than it might sound"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 문제 설명이 거창하게 들리지만 실제 수정 범위는 작다고 상대를 안심시키며 시작할 때(진단 보고 서두, 구어)
- 한국어: 고칠 범위는 들리는 것보다 좁다
- 설명: `narrower` 를 변경 범위에 쓰는 것이 핵심이다. `might sound` 는 "당신이 그렇게 들었을 수도 있다"를 가정법으로 부드럽게 인정한다. 코드가 이미 대부분을 모델링하고 있을 때 이 문장으로 열면, 뒤의 긴 분석이 "큰일"이 아니라 "정확한 한 줄"을 찾는 과정으로 읽힌다.
- 예문: The code already models most of this, so the fix is narrower than it might sound.
- 유사어: smaller than it looks (평이), a surgical change (결과를 강조)
- 반의어: bigger than it looks / a wider blast radius

## "would happily claim"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 검사가 허술해 잘못된 입력도 거리낌 없이 받아들인다고 코드를 의인화해 경고할 때(버그 설명, 구어)
- 한국어: 아무렇지 않게 (자기 것이라) 주장할 것이다
- 설명: `happily` 는 여기서 반어다 — 코드는 기뻐하지 않지만, 막을 장치가 없어 "기꺼이" 잘못된 매칭을 한다는 그림이다. `claim` 은 셀이 recipe 를 자기 소관으로 가져간다는 도메인 은유. 가정법 `would` 가 "지금은 안 일어나지만 데이터만 바뀌면 바로"를 담는다.
- 예문: A cell with no `family` and `phase_in: ['PV']` would happily claim a Pool recipe.
- 유사어: would gladly accept (같은 반어), lets X through unchallenged (더 격식)
- 반의어: rejects outright

## "the data happens to be right, so the code was never asked to be"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 불변식이 코드가 아니라 데이터의 우연한 모양에 기대고 있는 버그 부류를 이름 붙일 때(진단 통찰, 중간 격식)
- 한국어: 데이터가 우연히 맞아서, 코드는 맞을 것을 요구받은 적이 없다
- 설명: `happens to be` 가 "우연"을, 뒤의 수동태 `was never asked to be` 가 "요구 부재"를 담는다. 뒤의 `be` 는 앞의 `right` 를 생략한 채 받는다(`asked to be [right]`). 문장 전체를 따옴표로 묶어 `the classic "…" bug` 처럼 버그의 이름으로 쓰는 용법이 인상적이다.
- 예문: This is the classic "the data happens to be right, so the code was never asked to be" bug.
- 유사어: works by accident (평이), correct by coincidence, not by construction (기존 노트 `by construction` 계열)
- 반의어: enforced by the engine / an invariant

## "survives exactly until (someone does X)"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 지금은 멀쩡해 보이는 것이 언제 깨질지를 조건으로 못 박을 때(위험 설명, 중간 격식)
- 한국어: 정확히 누군가 X 를 하는 순간까지만 살아남는다
- 설명: `until` 앞의 `exactly` 가 이 구의 힘이다 — "언젠가"가 아니라 "바로 그 사건"에 수명이 걸려 있다. 주어를 `it`(불변식) 으로 두고 `survives` 라는 생존 동사를 쓰면 코드가 시한부라는 그림이 된다.
- 예문: The invariant lives in a comment and in the shape of hand-written seed cells, not in the engine — so it survives exactly until someone edits a rule.
- 유사어: holds only as long as (조건을 긍정으로), is one edit away from breaking (구어)
- 반의어: holds regardless of the data

## "dead outside tests"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 어떤 함수의 호출자가 테스트뿐이라 운영 경로에서는 실행되지 않는다고 지적할 때(코드 분석, 기술)
- 한국어: 테스트 밖에서는 죽은 코드다
- 설명: `dead code` 를 조건부로 쪼갠 표현이다. 완전히 죽진 않았지만(테스트는 부른다) 런타임에는 영향이 없으니, 거기를 고쳐도 아무것도 안 바뀐다는 결론이 따라온다. 세 단어로 "고칠 곳이 여기가 아니다"를 말한다.
- 예문: The frontend's `deriveFamily`/`derivePhase` are dead outside tests, so fixing the derivation there would change nothing at runtime.
- 유사어: test-only (형용사형), never reached in production (풀어쓰기)
- 반의어: live / on the hot path

## "One fork I don't want to guess on"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 분석을 마치고 구현 전에 사용자 결정이 필요한 갈림길 하나를 꺼낼 때(질문 도입, 구어)
- 한국어: 내 추측으로 정하고 싶지 않은 갈림길 하나
- 설명: `fork` 는 길이 갈라지는 지점이다. `guess on` 은 "추측으로 때우다"라는 구동사로, "묻는 게 귀찮아서가 아니라 틀리면 비싸서 묻는다"는 태도를 전한다. 뒤에 콜론을 두고 선택지를 나열하는 도입구로 쓴다.
- 예문: One fork I don't want to guess on: should PV be dropped from the payload, or only ignored in the verdict?
- 유사어: a decision I'd rather not make for you (더 공손), worth your call (기존 노트)
- 반의어: I'll just pick one

## "hence the squeeze you're seeing"
- 레지스터: conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt a101dd54
- 맥락: 원인을 설명한 직후 사용자가 겪는 증상과 연결해 마무리할 때(원인 설명 말미, 구어)
- 한국어: 그래서 지금 보시는 것처럼 비좁은 것이다
- 설명: `hence` + 명사구는 동사 없이 결과를 잇는 압축형이다(`hence the delay`, `hence the 400`). `the squeeze you're seeing` 처럼 "당신이 보고 있는 증상"을 명사로 만들면 원인 설명이 사용자 경험으로 돌아와 닫힌다. `squeeze` 는 공간이 눌린 상태를 가리키는 구어 명사.
- 예문: That's 4 columns inside a lane that already only gets half the panel — hence the squeeze you're seeing.
- 유사어: which is why it looks cramped (풀어쓰기), so that's your symptom (구어)
- 반의어: (마땅한 대체 표현 없음)

## "X decided Y, not taste"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt a8bc1b87
- 맥락: 시각적 선택이 취향이 아니라 문서화된 기준에서 나왔다고 밝힐 때(디자인 결정 설명, 중간 격식)
- 한국어: Y 를 정한 건 X 지 취향이 아니다
- 설명: 디자인 리뷰에서 "왜 이 색?"에 가장 좋은 답은 규칙을 가리키는 것이다. `not taste` 가 짧게 붙어 "논쟁할 여지가 없다"를 만든다. 주어를 사람이 아니라 기준(`the litmus test`)으로 두는 무생물 주어 구문이 격식을 올린다.
- 예문: The litmus test decided the chip colours, not taste: "narrows data" → terracotta, "picks one subject" → ink.
- 유사어: by the book, not by preference (관용), rule-driven rather than aesthetic (격식)
- 반의어: a matter of taste
