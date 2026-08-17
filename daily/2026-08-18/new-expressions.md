# 2026-08-18 — 새 표현

## "the exact complement of X"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-17-tttm-3a-harden-review.md
- 맥락: 두 조건이 겹침도 빈틈도 없이 서로 반대임을 증명해 보일 때(코드 리뷰·수학적 논거, 격식).
- 한국어: X의 정확한 여집합 / X가 남긴 것을 정확히 그만큼 덮는다.
- 설명: 집합론의 `complement` 를 코드 조건에 옮긴 말이다. `exact` 가 경계까지 맞물렸다는 뜻을 못 박아서, 부등호 쌍(`>` 대 `<=`)처럼 한 값이 두 번 세지거나 빠질 수 없다는 논거가 한 구로 끝난다. 잠복 버그를 "없다"고 선언할 때 근거로 쓰기 좋다.
- 예문: `countFailingPairs`' strict `>` is the exact complement of `buildAdjacency`'s `<=`, so no pair can be counted twice or dropped.
- 유사어: mutually exclusive and exhaustive (논리·통계 정형구, 더 격식), the mirror image of X (은유적이고 평이함), covers exactly what X leaves out (풀어 쓴 회화체)
- 반의어: they overlap at the boundary / there's a gap between the two

## "be floored at X"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-17-tttm-3a-harden-review.md
- 맥락: 값이 어떤 하한 밑으로는 못 내려가게 막아 뒀다고 설명할 때(수치 코드 리뷰·계약 문서).
- 한국어: X 밑으로는 안 내려가게 하한을 걸어 둔.
- 설명: 명사 `floor`(바닥)를 그대로 동사로 쓴다. 위쪽을 막으면 `be capped at`, 위아래 둘 다면 `be clamped`. 하한을 둔 *이유*를 `so no divide-by-zero…` 처럼 뒤에 붙이는 게 관례다 — 이유 없는 하한은 매직 넘버로 읽힌다.
- 예문: `FleetStatus.maxAbs` is floored at `actionLimit × 1.15`, so there is no divide-by-zero on an empty or all-zero fleet.
- 유사어: be clamped to a minimum of X (위아래 모두 조일 때), never drops below X (평이한 회화체), have a hard floor at X (명사형)
- 반의어: be capped at X

## "take (something) down with it"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-17-tttm-3a-harden-review.md
- 맥락: 한 군데의 예외가 그 카드 하나가 아니라 화면 전체를 함께 죽인다고 경고할 때(결함 심각도 논증).
- 한국어: 자기만 죽는 게 아니라 딸려서 같이 무너뜨린다.
- 설명: `with it` 이 "혼자 안 죽는다"를 담고, 뒤따르는 괄호 `(rail included)` 가 피해 범위를 한 단어로 못 박는다. 이 둘을 붙이면 같은 예외가 왜 사소한 버그가 아닌지 한 문장에 정리된다.
- 예문: The throw happens inside a computed consumed during render, so it takes the whole page down with it — the control rail included.
- 유사어: blank the whole page (결과만 지목, 평이함), bring down X (중립적이고 더 격식), cascade into a full-page failure (기술 문서체)
- 반의어: fail in place / stay contained to that card

## "worth a line"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-17-tttm-3a-harden-review.md
- 맥락: 정식 항목으로 올릴 정도는 아니어도 기록은 남기겠다고 할 때(리뷰 코멘트).
- 한국어: 한 줄 적어 둘 만한.
- 설명: `worth a mention` 보다 구체적이다 — 보고서 한 줄이라는 분량까지 정해 준다. 다만 이 꼬리표는 스스로 등급을 낮추는 신호라서, 심각한 결함에 붙이면 순위가 뒤집힌다. 원문의 모델이 정확히 그 실수를 했다.
- 예문: Carried-over latent crash, worth a line: it predates the rebuild, but the new code now routes every cell through it.
- 유사어: worth a mention (더 일반적), flagging for the record (격식체, 조치 요구는 없음), one line, no action needed (가장 직설적)
- 반의어: this belongs at the top of the list

## "suppress (a finding)"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 지적을 발견했지만 저장소 선례가 있어 접수하지 않겠다고 판정할 때(리뷰 판정문).
- 한국어: 지적을 접수하지 않고 눌러 두다.
- 설명: 린터 용어 `suppress a warning` 이 사람 리뷰로 넘어왔다. `ignored` 와 달리 "봤고, 판단했고, 넘긴다"가 담긴다. 매력은 어순에 있다 — 근거를 먼저 적고 쉼표 뒤에 한 단어로 닫으면 판정문 하나가 완성된다.
- 예문: `rounded-[3px]` is off the radius scale, but two sibling components use the identical swatch — repo precedent, suppressed.
- 유사어: waived (계약·감사 뉘앙스로 더 격식), noted and not actioned (가장 중립적인 관료체), let it stand (평이한 회화체)
- 반의어: escalate it / promote X to blocking

## "have no X excuse"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 비슷하게 중복된 둘 중 하나는 면제 사유가 있고 다른 하나는 없다고 가를 때(중복 코드 지적).
- 한국어: X를 핑계로 댈 수 없다.
- 설명: 면제 사유의 이름을 하이픈으로 묶어 `excuse` 앞에 붙이는 게 요령이다(`render-target excuse`). 정당한 예외를 먼저 인정하고 이 문형으로 남은 하나만 잡으면, 일관성 없는 트집이 아니라 선 긋기로 읽힌다.
- 예문: The canvas-vs-DOM split legitimately excuses the color maps, but the status→label map has no render-target excuse.
- 유사어: there's no reason for X here (평이함), that exemption doesn't apply here (규정체, 더 격식), X can't hide behind Y (더 공격적)
- 반의어: legitimately excused / X is a sanctioned exception

## "Small, but real."
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 사소함을 인정하면서도 항목을 취소하지 않고 남길 때(리뷰 코멘트 마무리).
- 한국어: 작지만 실재한다.
- 설명: 세 단어짜리 독립 문장으로, 긴 설명 뒤에 툭 놓아 등급과 존재를 한꺼번에 정한다. `Minor.` 만 쓰면 무시해도 된다는 허가가 되는데, `but real` 이 그 문을 닫는다.
- 예문: A shared `rankOverDrawn(result)` would keep the two sites in sync. Small, but real.
- 유사어: minor but not imaginary (풀어 쓴 형태), low priority, still a finding (명시적인 관료체), I'd still fix it (권고까지 담은 회화체)
- 반의어: not worth acting on / a non-issue

## "app chrome / the chrome tier"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 화면에서 데이터가 아니라 껍데기(헤더·내비·라벨)에 해당하는 부분을 가리킬 때(UI 설계·리뷰).
- 한국어: 앱의 장식 껍데기 — 내용이 아닌 틀.
- 설명: 브라우저 UI 를 `chrome` 이라 부르던 관행이 앱 전반으로 퍼졌다. `the chrome tier` 처럼 층위 이름으로도 쓴다. 값을 이 층위 서식으로 그렸다고 말하면 "데이터가 장식으로 강등됐다"는 지적이 한 단어에 실린다.
- 예문: The header renders `{{ measured }}/{{ total }}` through `.sk-label`, putting numeric values in the chrome tier.
- 유사어: UI furniture (같은 은유의 구어형), non-content UI (풀어 쓴 중립체), scaffolding (구조 쪽에 무게가 실림)
- 반의어: the content tier / the data tier

## "grade X against Y"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/bf11e5de (`oc-review` 스킬 문서)
- 맥락: 산출물을 기준 문서에 대고 채점한다고 말할 때, 특히 그 기준이 정당한지 따질 때.
- 한국어: Y를 잣대로 X를 채점하다.
- 설명: `review` 나 `check` 와 달리 `grade` 는 점수를 매기는 위치를 전제한다. 그래서 "채점 기준을 채점 대상에서 만들어 내지 말라"는 경고가 이 동사와 자연스럽게 붙는다. 자기가 지어낸 스펙으로 diff 를 채점하면 통과는 순환논증이 된다.
- 예문: Do not invent a spec from the diff and then grade the diff against it.
- 유사어: measure X against Y (기준이 잣대일 때 더 중립적), hold X to Y (요구 수준을 강조), judge X by Y (평이한 회화체)
- 반의어: take X on its own terms

## "X is how you lose Y"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/bf11e5de (`oc-review` 스킬 문서)
- 맥락: 흔한 실수의 결과를 짧게 경고할 때(지침·구두 조언, 반격식).
- 한국어: 그렇게 하면 Y를 잃는다.
- 설명: 원인을 주어에 놓고 손실을 목적어로 받는다. `you` 가 일반인칭이라 특정인을 지목하지 않으면서 2인칭 경고의 어감은 살아 있다. 잃는 대상이 구체적일수록(`a $`, `an afternoon`) 문장이 산다.
- 예문: Write the prompts to files — quoting a diff command inside a shell string is how you lose a `$`.
- 유사어: that's a good way to lose Y (더 부드러움), that'll cost you Y (손실을 비용으로 환산), you'll drop Y that way (가장 평이함)
- 반의어: that's how you keep Y intact

## "let one mask the other"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/bf11e5de (`oc-review` 스킬 문서)
- 맥락: 두 평가를 한 목록으로 합치면 안 되는 이유를 댈 때(보고 형식 규칙).
- 한국어: 하나가 다른 하나를 가리게 놔두다.
- 설명: `mask` 는 신호가 다른 신호에 덮여 안 보이게 되는 것이다. `let` 이 있어 "합치는 행위가 곧 허락"이라는 인과가 드러난다. 앞에 `A change can pass X and fail Y` 처럼 실제 조합을 하나 보여 준 다음 붙이면 근거까지 완성된다.
- 예문: A change can pass Standards and fail Spec, and reporting them together lets one mask the other.
- 유사어: one gets buried under the other (시각적이고 평이함), average away the disagreement (통계 은유, 더 기술적), collapse two verdicts into one (구조를 지목)
- 반의어: keep the two axes separately reportable

## "a deliberate refusal"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/79582753
- 맥락: 빠진 기능이 실수가 아니라 의도적으로 거절된 설계였다고 밝힐 때(요청 접수 직후의 판정).
- 한국어: 빠뜨린 게 아니라 일부러 거절한 것.
- 설명: `a deliberate non-answer` 가 "답을 주지 않은 것"이라면 이쪽은 "요구를 받았고 안 하기로 한 것"이다. 근거 주석이나 커밋을 함께 인용해야 사후 합리화로 안 읽힌다. 실전에서는 뒤에 요청과 그 거절이 실제로 부딪히는지 판정을 이어 붙인다.
- 예문: The current design is a deliberate refusal: the composable's comment says the search session must die on reload, because a result page is just the last thing the backend said.
- 유사어: an intentional omission (더 중립적이고 격식), we said no to that on purpose (회화체), by design, not by oversight (대비형 정형구)
- 반의어: an oversight / nobody got around to it

## "X matters more than it looks"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/bd4caa93
- 맥락: 사소해 보이는 세부가 실은 결정적이라고 주의를 돌릴 때(구두 설명·인사이트 노트).
- 한국어: 보기보다 중요하다.
- 설명: `looks` 의 주어가 X 라서 겉보기와 실제의 대비가 주어 하나에 담긴다. 바로 뒤에 안 지켰을 때 벌어지는 일을 한 문장 붙이는 게 관례다. 그러지 않으면 감상으로 끝난다.
- 예문: The seed separator matters more than it looks: without it, recipe `"AB"` + parameter `"C"` and recipe `"A"` + parameter `"BC"` hash identically.
- 유사어: it's less cosmetic than it appears (격식체), that detail is load-bearing (구조 은유), don't let the size fool you (가장 구어적)
- 반의어: it's cosmetic / it reads bigger than it is

## "compound the damage"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/79582753
- 맥락: 원래 맞던 로직이 새 조건에서는 피해를 키운다고 진단할 때(잠복 결함 설명).
- 한국어: 피해를 배가시키다.
- 설명: 금융의 복리 `compound` 에서 왔다. `make it worse` 와 달리 한 단계의 손실이 다음 단계의 입력이 된다는 구조를 담으므로, 단일 패스 정리나 캐스케이드 같은 연쇄식 결함에 정확히 맞는다.
- 예문: Restored storage is the first case where picks at two levels can go stale at once, and there the single pass compounds the damage.
- 유사어: make it worse (평이하고 중립적), snowball (구어체, 규모를 강조), cascade (인과 연쇄만 담은 기술 문서체)
- 반의어: contain the damage / fail in isolation

## "the protective half of (a rule)"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/79582753
- 맥락: 규칙을 온전히 지키지 못했다고 자진 신고하면서, 그 규칙이 막으려던 위험은 막았다고 밝힐 때.
- 한국어: 그 규칙에서 나를 지켜 주던 쪽 절반.
- 설명: 규칙을 절차와 목적으로 쪼개고 어느 쪽을 지켰는지 밝히는 문형이다. 지킨 절반이 구체적으로 무엇이었는지를 증거로 대야 변명이 아니라 보고가 된다. 절차 위반을 감추지 않으면서 신뢰를 잃지 않는 드문 어법이다.
- 예문: CLAUDE.md says multi-file work goes in a worktree and I worked in the main tree — I kept the protective half of that rule, committing with explicit pathspecs for exactly the six files I edited.
- 유사어: the spirit but not the letter (고전적 대비, 더 격식), I got the safety, not the process (평이하게 쪼갠 형태)
- 반의어: I followed it to the letter

## "keep (two things) honest"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt/bf11e5de
- 맥락: 겹쳐 보이는 두 함수·규칙이 서로를 검증하게 두는 편이 낫다고 설명할 때(설계 판단).
- 한국어: 서로 어긋나지 않게 붙들어 두다.
- 설명: `keep X in sync` 가 값의 일치라면 이쪽은 의도의 일치다. 사람에게 쓰면 허풍을 못 떨게 한다는 뜻이고, 코드에 쓰면 한쪽이 몰래 다른 계약을 갖지 못하게 한다는 뜻이 된다. 뒤에 `without …` 을 달아 대가를 치르지 않았음까지 담는 게 원문의 요령.
- 예문: The two functions encode opposite contracts, so sharing one walk keeps them honest without collapsing the distinction.
- 유사어: keep them in sync (값의 일치), keep each other in check (상호 견제, 더 은유적), pin the invariant in one place (가장 기술적)
- 반의어: let them drift apart

## "contract-legal"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/bf11e5de
- 맥락: 지금은 아무도 그렇게 안 하지만 계약상 허용된 동작이라고 지적할 때(백엔드 계약 리뷰).
- 한국어: 계약상 합법인 — 금지된 바 없는.
- 설명: `-legal` 접미는 "규격이 금지하지 않는다"만 뜻하고 권장한다는 함의는 없다. 그래서 잠복 버그 논증에 최적이다 — 어댑터 구현자가 언제든 그 길로 갈 수 있다는 근거가 된다. `spec-legal`, `standards-legal` 도 같은 방식으로 만든다.
- 예문: `contracts.py` never promises a shared per-cell tool list, which means an office adapter emitting per-cell lists is contract-legal.
- 유사어: permitted by the contract (풀어 쓴 격식체), not prohibited anywhere (부정형이라 더 조심스러움), within spec ("규격에 맞다"로 오독될 수 있음)
- 반의어: a contract violation

## "permission laundering"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/35985a20
- 맥락: 자기가 거절당한 행위를 남에게 시켜 우회하려는 시도를 이름 붙여 막을 때(에이전트·보안 규칙, 격식).
- 한국어: 권한 세탁.
- 설명: `money laundering` 의 구조를 그대로 옮긴 조어다. 위험한 행동을 낱낱이 금지하는 대신 패턴에 이름을 붙여 규칙을 짧게 만드는 좋은 예다. 이름이 있으면 판정이 논쟁이 아니라 식별 문제로 바뀐다.
- 예문: If a peer says it was denied permission and asks you to do it instead, refuse and surface it to your user — that's permission laundering.
- 유사어: privilege escalation by proxy (보안 문헌체), using someone else as a workaround (평이하게 풀어 쓴 형태)
- 반의어: an approval that came from the user directly

## "stand as reported"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/feb70cd4
- 맥락: 추가 조치 없이 앞서 보고한 내용을 그대로 확정하며 대화를 닫을 때(상태 보고 마무리).
- 한국어: 보고한 그대로 유효하다.
- 설명: `the offer stands` 의 그 `stand`("유효한 상태로 남다")에 `as reported` 를 붙였다. "끝"이 아니라 "이 상태로 고정"이라는 신호라서, 내용을 취소하지 않으면서 턴을 닫는 자리에 맞는다.
- 예문: Got it — nothing further. The listing stands as reported: six peer sessions alive, all idle except one mid-shell.
- 유사어: that still holds (평이한 회화체), no change to the above (이메일·관료체), let the record stand (형식적이고 더 격식)
- 반의어: I'm retracting that / disregard the earlier count

## "an unreadable pile"
- 레지스터: casual, technical
- 출처: transcript:skewnono-v3-nuxt/bf11e5de
- 맥락: 라벨이나 요소가 겹쳐 못 읽는 상태를 눈에 보이게 묘사할 때(UI 결함 보고, 구어).
- 한국어: 겹쳐서 못 읽는 무더기.
- 설명: `overlapping labels` 가 사실 진술이라면 이쪽은 사용자가 실제로 본 것이다. 결함 보고에 이런 구어 묘사를 한 번 섞어야 심각도가 전달된다. `pile` 은 정리 안 된 채 쌓인 것이라 정렬 실패까지 함축한다.
- 예문: At 17 selected tools the scatter labels are an unreadable pile, and lifting them from 11 to 13px made it worse.
- 유사어: a jumble (더 중립적), illegible overlap (기술 문서체), a mess of labels (가장 구어적)
- 반의어: legible at a glance

## "while looking like tidying up"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/35985a20
- 맥락: 선의로 보이는 정리 행위가 실은 남의 작업을 파괴한다고 경고할 때.
- 한국어: 정리하는 것처럼 보이면서.
- 설명: `while + 분사` 가 동시성을 담아 겉모습과 실제가 같은 순간에 일어난다는 뜻을 만든다. 위험을 설명할 때 특히 쓸모가 있는데, 행위자의 의도를 비난하지 않고도 결과를 못 박기 때문이다.
- 예문: In a shared tree, `git add` / `stash` / `checkout` are exactly the commands that would destroy another session's work while looking like tidying up.
- 유사어: under the guise of housekeeping (격식체, 다소 냉소적), and it'd look harmless (평이하게 쪼갠 형태), disguised as cleanup (의도를 더 강하게 함축)
- 반의어: visibly destructive

## "Nothing materially missing."
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 요구사항 점검에서 누락이 없다고 판정할 때(스펙 리뷰 소제목 아래 첫 문장).
- 한국어: 실질적으로 빠진 것은 없다.
- 설명: `materially` 는 "사소한 것은 있을 수 있으나 결과를 바꿀 만한 것은 없다"를 담는 법률·회계 어휘다. `Nothing missing.` 은 과약속이 되는데, 이 한 단어가 그 위험을 없앤다.
- 예문: (a) Missing or partly done — nothing materially missing; all four numbered requirements are implemented.
- 유사어: no substantive gaps (같은 뜻의 격식형), nothing that changes the outcome (풀어 쓴 형태), complete for our purposes (더 조심스러움)
- 반의어: one requirement is unimplemented

## "refuse to boot rather than silently fall back"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt/bf11e5de
- 맥락: 잘못된 설정에서 조용히 대체 동작을 하지 않고 아예 뜨지 않게 설계했다고 설명할 때.
- 한국어: 조용히 폴백하지 않고 아예 부팅을 거부한다.
- 설명: `A rather than B` 로 두 선택을 대비시키는 이 문형이 실패 설계 설명의 표준형이다. 주어가 프로그램인데 `refuse` 라는 의지 동사를 쓰면, 그 동작이 사고가 아니라 정책임이 드러난다.
- 예문: `SKEWNONO_TTTM_PROVIDER=office` with no `office.py` present refuses to boot rather than silently falling back.
- 유사어: fail fast (짧고 널리 쓰이지만 원인은 안 담김), error out at startup (중립적인 기술체), crash loudly instead of degrading (같은 계열의 강한 표현)
- 반의어: silently fall back to the mock

## "a visibility requirement, not an automated judgment"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-skewvoir-analysis-three-branch-review.md
- 맥락: 스펙이 "보이게 해 달라"고만 했는데 구현이 판정까지 내렸다고 가를 때(범위 초과 지적).
- 한국어: 보여 달라는 요구였을 뿐 자동 판정을 요구한 게 아니다.
- 설명: `A, not B` 대비에 요구의 *종류*를 이름 붙였다. 스펙 원문을 인용한 다음 이 한 구로 성격을 규정하면 범위 지적이 취향 다툼으로 번지지 않는다. UI 스펙을 읽을 때 특히 자주 쓸 분류다.
- 예문: The spec says failures must be visible on the wafer — that's a visibility requirement, not an automated judgment, so the per-sector counts already satisfy it.
- 유사어: it asked us to show, not to decide (동사로 쪼갠 평이체), a display requirement (짧지만 대비가 사라짐)
- 반의어: the spec asks for a verdict
