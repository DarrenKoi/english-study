# 2026-08-17 — 새 표현

## "(an argument) proves too much"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 상대 논거를 규칙으로 세우면 상대가 지키려던 것까지 무너진다고 지적할 때(설계 토론·리뷰, 격식).
- 한국어: 그 논증은 지나치게 증명한다 / 그 논리대로면 당신 쪽도 같이 무너진다.
- 설명: 논리학에서 온 정형구다. 전제를 부정하지 않고 **일관되게 적용만 해서** 결론을 자멸시킨다. `if X is the rule, it doesn't justify A; it annihilates B` 처럼 뒤에 "그 규칙을 끝까지 밀면 어디까지 죽는가"를 한 문장 붙여야 완성된다. 인신공격 없이 상대 원칙을 되돌려 주는 가장 정중한 형태다.
- 예문: The "unfalsifiable fixture" argument proves too much: if "no ground truth ⇒ defer" is the sequencing rule, it annihilates the license for all Phase 1 work.
- 유사어: that reasoning cuts both ways (더 평이한 회화체, 양날이라는 은유), by that logic we'd also have to … (구체 사례로 밀어붙이는 회화형), it's self-defeating (결과만 지목, 과정은 생략)
- 반의어: the principle applies narrowly here / that objection is contained

## "the weakest link in your own case"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 상대 주장 여러 개 중 어느 하나를 콕 집어 "이건 빼는 게 낫다"고 알려줄 때(토론·리뷰, 격식이되 직설적).
- 한국어: 그건 당신 논거 중에서 제일 약한 고리다.
- 설명: `your own` 이 핵심이다. 남의 약점이 아니라 **상대가 자기 편으로 데려온 근거**를 가리키므로, 공격이 아니라 정비 조언으로 읽힌다. 판정을 먼저 주고(`you're right about A, wrong to bundle B`) 그다음에 이 문장을 붙이면 승복과 반박이 한 문단에 공존한다.
- 예문: You're right about A-1, wrong to bundle A-2 into the rejection — and your reason (1) is the weakest link in your own case.
- 유사어: that's the part I'd drop (훨씬 평이한 회화체), your strongest point isn't this one (에둘러 같은 말), this argument is doing the least work for you (일하는 양의 은유, 부드러움)
- 반의어: that's the load-bearing part of your argument

## "quietly substitute A for B"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 논의 도중 쟁점이 슬며시 바뀐 것을 잡아낼 때(토론·코드리뷰 코멘트, 격식).
- 한국어: 슬쩍 A를 B 자리에 바꿔치기했다.
- 설명: `substitute A for B` 는 "B 대신 A를 넣다"라는 뜻이라 순서가 한국어 직관과 반대다 — 새로 들어오는 쪽이 앞에 온다. 부사 `quietly` 가 "고의가 아닐 수도 있지만 아무튼 표는 안 났다"는 완충 역할을 해서, 비난이 아니라 기록으로 남는다.
- 예문: You quietly substituted "ready when real data arrives" for the steelman's actual claim — motivation, not readiness.
- 유사어: you've shifted the goalposts (더 구어적이고 비난 강도가 높음), that's a different claim from the one on the table (완전히 중립적), this reframes the question (가장 부드러움)
- 반의어: you answered the claim as stated

## "the steelman (of an argument)"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 반박 전에 상대 주장을 **가장 강한 형태로** 복원해 두고 그것을 상대할 때(토론·설계 논쟁, 격식).
- 한국어: 상대 주장의 최강 버전 / 강철 인형.
- 설명: 허수아비 논증 `strawman` 의 반대말로 만들어진 신조어다. 동사로도 쓴다(`let me steelman your position`). 명사로 쓸 때 `the steelman's actual claim` 처럼 소유격을 붙이면 "내가 세워 준 최강 버전이 실제로 말한 것"이라는 뜻이 되어, 논점 이탈을 지적하는 데 딱 맞는다.
- 예문: The steelman's actual claim was never readiness — it was that without a screen, nobody has a reason to go ask.
- 유사어: the strongest version of your point (풀어 쓴 평이체), taking your argument at its best (동명사형, 회화체)
- 반의어: a strawman (약하게 왜곡한 허수아비 버전)

## "concede plainly"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 상대가 옳을 때 조건이나 변명을 달지 말고 인정하라고 규정할 때(리뷰 지침·회고, 격식).
- 한국어: 군더더기 없이 순순히 인정하라.
- 설명: `concede` 는 논쟁에서 한 점을 내주는 것이라 `admit`(잘못 시인)보다 대등하고 덜 굴욕적이다. 부사 `plainly` 가 "인정하되 곧바로 단서를 붙이는" 흔한 습관을 차단한다. 실제 문서에서는 뒤에 `No hedging.` 한 마디를 붙여 못을 박는다.
- 예문: Concede plainly when the model is right, especially where it caught something you wrote yourself.
- 유사어: own it (짧고 구어적, 책임까지 포함), that's a fair hit (스포츠 은유, 가벼운 회화체), I'll grant you that (한 점만 내줄 때)
- 반의어: hedge / concede with a caveat

## "a clean bill of health"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 검사에서 아무것도 안 나왔다는 판정을 가리킬 때. 특히 "검사가 실패한 것"과 "이상이 없는 것"을 구별해야 할 때(리뷰·운영 보고, 중간 격식).
- 한국어: 이상 없음 판정 / 건강 진단서.
- 설명: 항구에서 선박 검역 증명서를 뜻하던 말이 그대로 굳었다. 관사 `a` 를 붙여 통째로 쓴다. 실무에서 값어치가 큰 쓰임은 부정형이다 — 빈 결과를 이상 없음으로 **읽지 말라**고 경고할 때 이 표현이 그 오독에 이름을 붙여 준다.
- 예문: Never present an empty axis as a clean bill of health — the script exits non-zero on empty output precisely so that cannot happen quietly.
- 유사어: all clear (짧고 구어적), nothing came back (검사 결과에 한정된 평이체), signed off (승인 절차까지 끝났을 때)
- 반의어: findings outstanding / flagged for follow-up

## "pre-digest (something) into a summary"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 원자료를 대신 씹어서 넘기면 검토의 값어치가 사라진다고 금지할 때(위임 규칙·리뷰 지침, 격식).
- 한국어: 미리 소화해서 요약본으로 넘기다.
- 설명: `digest`(소화하다)에 `pre-` 를 붙여 "받는 쪽이 씹을 것을 남기지 않았다"는 뜻을 만든다. 부정 명령형(`do not pre-digest … — give it the command`)으로 쓸 때 가장 자연스럽다. 요약이 나쁘다는 말이 아니라, 요약하는 순간 내 가정이 함께 실린다는 지적이다.
- 예문: Do not pre-digest the diff into a summary and send that — give the model the diff command and let it look.
- 유사어: hand over the raw input, not your reading of it (풀어 쓴 격식체), don't editorialize (한 단어로 끝내는 회화체)
- 반의어: give it the command / let it look for itself

## "defensible, but unasked"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-3a-layout-review.md
- 맥락: 스펙 대비 리뷰에서 "틀리진 않았지만 요청 밖"인 구현을 분류할 때(리뷰 리포트, 격식).
- 한국어: 변호는 되지만 아무도 요청하지 않은 것.
- 설명: 두 판정을 한 호흡에 붙여 **품질 시비와 범위 시비를 분리**한다. `defensible` 은 "우기면 근거는 댈 수 있다"는 중간 톤이라 칭찬도 비난도 아니고, `unasked` 가 실제 지적을 담는다. scope creep 항목을 적을 때 이 짝이 가장 자주 쓰인다.
- 예문: Showing each tool's consensus residual in the dropdown is a defensible generalization, but unasked.
- 유사어: reasonable, just out of scope (완전한 평이체), nobody ordered this (구어적, 살짝 날 선 표현), gold-plating (요청 밖 과잉 구현을 한 단어로)
- 반의어: explicitly requested / in the spec as written

## "only nominally kept"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-cd-limit-review.md
- 맥락: 규칙이 형식상으로만 살아 있고 실제 동작에서는 무력해졌다고 지적할 때(스펙 리뷰·감사, 격식).
- 한국어: 이름만 지켜지고 있다 / 명목상으로만 유지된다.
- 설명: `nominal` 은 "명목상의"라는 뜻이고 `only` 가 그 앞이 아니라 **동사 바로 앞**에 놓여야 "지켜지긴 하는데 껍데기만"이라는 초점이 산다. 뒤에 반드시 실효값을 숫자로 붙여야 주장이 검증 가능해진다 — `the slider still stops at 0.2 nm, but effective tolerance is …` 처럼.
- 예문: R5's ceiling is only nominally kept: the slider still stops at 0.2 nm, but the effective tolerance at a 68 nm cell is already 0.227 nm.
- 유사어: honored in form, not in behaviour (더 격식 있고 대비가 선명함), it's there on paper (구어적), technically still true (가장 가벼운 비꼼)
- 반의어: enforced in behaviour / actually binding

## "inherited, not introduced"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 이번 변경이 만든 결함이 아니라 원래 있던 것이라고 선을 그을 때(리뷰 응답·회귀 분류, 격식).
- 한국어: 물려받은 것이지 새로 들여온 게 아니다.
- 설명: 과거분사 두 개를 대비시켜 한 구로 끝낸다. 책임 회피처럼 들리지 않으려면 **뒤에 "그러니 이 변경을 막을 근거는 못 된다"는 결론**을 붙여야 한다. 같은 계열로 `carried over, not introduced` 가 있다 — 이쪽은 리뷰어가 스스로 자기 지적의 등급을 낮출 때 쓴다.
- 예문: The order bias is inherited, not introduced: the lens, the rollup, and the filter all carry the same confound.
- 유사어: pre-existing (한 단어, 가장 중립적), this change didn't cause it (완전한 평이체), that's a separate bug (쟁점 분리에 초점)
- 반의어: introduced by this change / a regression

## "discount (something) when judging X"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 겉으로 커 보이는 수치에서 자동 생성분을 빼고 봐야 한다고 지시할 때(견적·리뷰 티어 판정, 격식).
- 한국어: (판단할 때) 그건 감안해서 빼라.
- 설명: 상점의 `discount`(할인)와 어원은 같지만 여기서는 "무게를 깎아 계산하다"라는 뜻의 타동사다. 명령형으로 문단 첫머리에 놓고 뒤에 근거 한 문장(`a 400-line vendored resync is not complexity`)을 붙이는 형태가 관용이다.
- 예문: Discount generated churn: a 400-line vendored-package resync is not complexity.
- 유사어: don't count X toward Y (가장 평이함), net that out (금융 어투, 간결), take X with a grain of salt (신뢰도를 깎는 쪽이라 뜻이 살짝 다름)
- 반의어: count it in full / take the number at face value

## "the honest default"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 기본값을 정할 때 안전빵이 아니라 실측에 맞는 값을 고르라고 권할 때(운영 규칙·문서, 격식).
- 한국어: 정직한 기본값.
- 설명: `sensible default`(무난한 기본값)와 달리 `honest` 는 **과장하지 않은**이라는 뜻을 얹는다. 늘 최고 사양을 고르는 습관을 겨냥한 말이라, 뒤에 그 기본값이 측정에서 나왔다는 근거가 따라붙는다.
- 예문: `medium` is the honest default for an ordinary one-feature diff — it was measured on a tool-using review, which is why the old blanket "always heavy" rule is gone.
- 유사어: a sensible default (더 흔하고 중립적), the default that matches reality (풀어 쓴 형태), err on the side of X (반대 방향, 여유를 두는 쪽)
- 반의어: a blanket rule / always max out

## "it wants its own change"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt/deda1b39
- 맥락: 발견은 했지만 이번 커밋에 끼워 넣지 않고 별건으로 돌릴 때(작업 보고·리뷰 마무리, 중간 격식).
- 한국어: 그건 별도 작업으로 다뤄야 한다.
- 설명: 무생물 주어 + `want` 는 "필요로 한다"는 영어 특유의 관용이다(`this sentence wants a comma`). `needs` 보다 부드럽고, 작업 자체가 요구하는 것처럼 들려서 미루는 결정을 개인 취향이 아니라 성격 판단으로 만든다.
- 예문: `maximalCliques` has no pivot and measures ~155 ms per call — pre-existing and load-bearing for correctness, so I left it; it wants its own change.
- 유사어: that deserves its own PR (더 구체적, 회화체), let's not bundle that here (합치지 말자는 쪽에 초점), out of scope for this diff (가장 격식)
- 반의어: fold it into this change / it comes along with this

## "leave (something) alone"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt/1cbe5d61
- 맥락: 정리 작업 중 건드리지 말아야 할 대상을 지목할 때(구두 지시·작업 보고, 구어).
- 한국어: 그건 손대지 말고 그냥 둬라.
- 설명: `leave it` 만으로도 통하지만 `alone` 이 붙으면 "치우려는 충동을 막는" 어감이 생긴다. 조건절(`unless you're done for the day`)을 뒤에 달아 언제부터는 건드려도 되는지 함께 주는 게 실무 관용이다.
- 예문: Leave the Flask and Nuxt processes alone unless you're done developing for the day — they're your running app, not session leftovers.
- 유사어: don't touch it (가장 직설적), that one stays (짧은 선언형), hands off X (구어적이고 살짝 강함)
- 반의어: tear it down / clean it up

## "on your behalf"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt/1cbe5d61
- 맥락: 권한이 누구에게 있는지 못 박을 때. 특히 대신 승인·결정할 수 없다고 밝힐 때(권한 설명·정책 문서, 격식).
- 한국어: 당신을 대신하여 / 당신 몫으로.
- 설명: `for you`(당신을 위해)와 갈린다 — `on your behalf` 는 **권한을 대리한다**는 뜻이라 승인·서명·결정처럼 자격이 걸린 행위에 붙는다. 부정문에서 특히 값을 한다: 왜 못 하는지가 친절이 아니라 구조의 문제가 된다.
- 예문: The gate belongs to the receiving user, which is exactly why a peer can never approve work on your behalf.
- 유사어: in your name (법률·문서 어투, 더 격식), for you (권한 함의가 빠진 평이체), acting for X (대리인 관계를 명시)
- 반의어: in its own right / with its own authority

## "the risk prices into X"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-16-tttm-page-start-order-discuss.md
- 맥락: 어떤 위험이 특정 항목만의 문제가 아니라 시스템 전체에 이미 반영돼 있다고 반박할 때(설계 논쟁, 격식).
- 한국어: 그 위험은 이미 X 전체에 값으로 매겨져 있다.
- 설명: 금융의 `priced in`(이미 가격에 반영됨)을 자동사처럼 굴린 형태다. `prices into A or into none of it` 처럼 양자택일로 닫으면, "이것만 골라 감점할 수는 없다"는 논증이 한 문장에 완성된다. 다소 고급 표현이라 문어에서만 쓴다.
- 예문: If "someone reads mock as real drift" were a live risk, it shipped weeks ago — the risk prices into the app's whole mock architecture or into none of it.
- 유사어: that risk is already baked in (훨씬 평이하고 흔함), it applies across the board (범위만 말하는 중립형), you can't single this one out (결론만 말하는 회화체)
- 반의어: this change adds fresh exposure

## "a smell hunt wearing a different label"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt/deda1b39 (`oc-review` 스킬 본문)
- 맥락: 근거 문서 없이 돌린 검사는 이름만 그럴듯한 취향 지적이라고 잘라 말할 때(방법론 규정, 격식).
- 한국어: 이름표만 바꿔 단 냄새 찾기.
- 설명: `wearing a different label` 이 핵심 부품이다 — 앞의 명사가 무엇으로 **위장했는지**를 붙이는 만능 꼬리다(`a rewrite wearing a refactor's label`). 규정문에서 "왜 이 절차가 필요한가"를 한 구로 정당화한다.
- 예문: Name what you settled on in the report — a Standards axis run against nothing is a smell hunt wearing a different label.
- 유사어: that's taste dressed up as policy (같은 은유, 더 직설적), it's the same thing under another name (완전한 평이체)
- 반의어: grounded in a cited rule / a documented breach

## "Bottom line: …"
- 레지스터: conversational, professional
- 출처: transcript:auto-recipe-creator/03453890
- 맥락: 긴 분석 끝에 실행 가능한 결론 한 단락만 남길 때(구두 보고·이메일 마무리, 중간 격식).
- 한국어: 정리하면 결국은 —
- 설명: 회계의 손익계산서 맨 아랫줄에서 왔다. `In conclusion` 보다 훨씬 구어적이고, 앞의 분석을 요약하는 게 아니라 **행동으로 옮길 것 하나**를 고른다는 점이 다르다. 그래서 뒤에는 대개 `the one thing I'd fix …` 같은 선택 문장이 온다.
- 예문: Bottom line: the mis-scaling scenario you feared is well defended, and the one thing I'd actually fix before trusting it on office data is the fixed `OVERSAMPLE=10`.
- 유사어: net-net (금융권 구어, 더 짧음), what this means for you is … (독자 중심으로 돌린 형태), the practical upshot (격식 있는 문어)
- 반의어: to be clear, nothing is settled yet

## "no reason to wait on that"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt/1cbe5d61
- 맥락: 응답이 안 온 항목을 붙들고 있지 말고 진행하자고 판단할 때(운영 판단·상황 보고, 구어에 가까운 실무체).
- 한국어: 그걸 기다릴 이유는 없다.
- 설명: `wait for`(사람·물건을 기다리다)와 `wait on`(어떤 일이 풀리기를 기다리며 붙들려 있다)의 차이가 요점이다. 뒤에 "기다려도 결정에 쓸 근거가 늘지 않는다"는 이유를 붙이면 조급함이 아니라 판단으로 읽힌다.
- 예문: No reason to wait on that — the evidence you'd act on is already in hand, and its reply could only add what you can read off the pane faster.
- 유사어: that's not a blocker (한 단어로 끝내는 실무체), we can move without it (가장 평이함), don't hold the line for it (전화 은유, 구어적)
- 반의어: that's the gate on everything else / hold until it lands
