# 2026-07-02 — 새 표현

배치의 영어는 대부분 transcript(assistant 해설·subagent 버그 리뷰)에 있었습니다. repo 문서는 한국어 위주라 표현·정독 소스로만 다뤘습니다.

## "hand-wavy"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] (Hermes 평가 세션)
- 맥락: 근거·수치 없이 두루뭉술하게 넘어가는 설명을 경계할 때(엔지니어링 구어~준격식). 흔히 "not hand-wavy"로 "근거에 단단히 붙였다"를 강조.
- 한국어: 두루뭉술한, 대충 얼버무리는
- 설명: 구체 근거 없이 손짓(hand-waving)으로 때우는 느낌의 설명. 형용사로 주장·분석을 깎아내릴 때 씀.
- 예문: I pulled the specifics from the primary sources so the evaluation is grounded, not hand-wavy.
- 유사어: vague (그냥 모호), wishy-washy (애매·우유부단, 더 구어), airy (근거가 희박한)
- 반의어: rigorous, well-grounded, concrete

## "the crux (of something)"
- 레지스터: professional
- 출처: transcript:[assistant]
- 맥락: 여러 논점 중 *가장 결정적인 쟁점*을 콕 집을 때(회의·문서, 준격식).
- 한국어: 핵심, 관건, 요체
- 설명: 문제 전체가 걸려 있는 결정적 지점. "the crux of the matter/problem/concern" 꼴로 자주 쓴다.
- 예문: The crux of your concern is whether the msr align point survives the jump into live-SEM coordinates.
- 유사어: the heart of the matter, the key issue, the nub (구어)
- 반의어: a side issue, a minor detail

## "flag, don't block"
- 레지스터: professional, technical
- 출처: transcript:[assistant] (subagent 코드 리뷰)
- 맥락: 리뷰·QA에서 불확실한 지적의 *대응 강도*를 정할 때 — 진행을 막지 말고 표시만 남겨 사람이 판단하게(엔지니어링 구어~준격식).
- 한국어: 막지 말고 표시만 해둬라
- 설명: block = 병합·진행 차단, flag = 경고 표시. 확신이 약한 발견은 flag만.
- 예문: This finding is more speculative than the others — flag, don't block.
- 유사어: raise it as non-blocking, warn but allow
- 반의어: block / gate / hard-fail

## "a testbed"
- 레지스터: technical
- 출처: transcript:[assistant]
- 맥락: 어떤 기법이 효과 있는지 *시험해 볼 수 있는 장(場)*을 가리킬 때(엔지니어링).
- 한국어: 실험대, 검증 무대
- 설명: 특정 레버(변경)의 효과를 격리해 측정하는 부분·환경. "the natural testbed for X"처럼 씀.
- 예문: The rcp-only arm becomes the natural testbed for the edge_ncc lever, since consensus can't help there.
- 유사어: a proving ground, a sandbox (더 격리·놀이터 뉘앙스)
- 반의어: production (실서비스 경로)

## "a no-op"
- 레지스터: technical, casual
- 출처: transcript:[assistant] (subagent 리뷰)
- 맥락: 실행돼도 실질 효과가 없는 동작을 짚을 때(엔지니어링 은어; no-operation).
- 한국어: 아무 동작도 안 하는 것, 공회전
- 설명: 코드가 돌긴 하는데 순 효과가 0인 경로. 성능 낭비·의도 미충족의 신호.
- 예문: If the cursor already sits on the center, the glide is a no-op — 24 identical writes with zero net motion.
- 유사어: does nothing, a dead code path
- 반의어: a side effect, an effective operation

## "a rehash"
- 레지스터: conversational
- 출처: transcript:[assistant]
- 맥락: 새것처럼 보이지만 *이미 한 것을 되풀이*했음을 지적할 때(구어).
- 한국어: 재탕, 우려먹기
- 설명: 실질은 이전 작업의 재포장. 동사로도 쓴다(rehash the same idea).
- 예문: I'll tell you whether this experiment is genuinely new or just a rehash of what we already ran.
- 유사어: a retread, warmed-over (형용사), old wine in a new bottle (관용)
- 반의어: a fresh take, genuinely novel

## "a wart"
- 레지스터: technical, casual
- 출처: transcript:[assistant]
- 맥락: 치명적이진 않지만 *알고도 감수하는 작은 설계 흠*을 솔직히 표시할 때(엔지니어링 구어). 흔히 "documented wart".
- 한국어: (알려진) 흠, 옥에 티
- 설명: 완벽히 못 없애 문서에 남겨두는 자잘한 결함. 정직하게 드러낸다는 뉘앙스.
- 예문: One documented wart: the two arms use different templates, so the lift is only comparable within an arm.
- 유사어: a rough edge, a known limitation, a blemish

## "self-evidencing / self-evident"
- 레지스터: professional
- 출처: transcript:[assistant]
- 맥락: *산출물이 스스로 증거가 되도록* 만들 때, 또는 별도 설명이 필요 없는 사실을 말할 때(엔지니어링·격식).
- 한국어: 그 자체로 증거가 되는; 자명한
- 설명: self-evidencing = 결과물만 봐도 뭐가 일어났는지 드러나게 함; self-evident = 자명한.
- 예문: Drawing the marker at the known point makes the artifact self-evidencing, regardless of how the cursor renders.
- 유사어: self-explanatory, speaks for itself
- 반의어: needs corroboration, opaque

## "defeat the purpose (of)"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] (subagent 리뷰)
- 맥락: 어떤 조치가 *원래 목적을 되레 무너뜨릴* 때(구어~준격식). "the very purpose"로 강조.
- 한국어: 취지를 무색하게 하다, 본래 목적을 망치다
- 설명: 문제를 풀려던 장치가 바로 그 문제를 다시 일으키는 역설.
- 예문: Falling back to a single jump defeats the very purpose of the glide it was meant to fix.
- 유사어: be counterproductive, backfire, undercut the goal
- 반의어: serve the purpose, achieve the intent
