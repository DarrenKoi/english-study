# 2026-08-31 — 신규 표현

## "contract drift"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 코드 리뷰에서 한쪽만 바뀌어 양쪽 계약이 서서히 어긋난 상태를 짚을 때(기술·격식)
- 한국어: 계약 표류 — 백엔드는 필드를 지웠는데 프론트 타입은 그대로 남은 상태
- 설명: drift 는 배가 조류에 조금씩 밀려 항로를 벗어나는 그림이다. 한 번에 깨지는 breakage 와 달리 아무 신호 없이 벌어지는 불일치를 가리키고, JSON 경계처럼 타입 검사가 닿지 않는 자리에서 특히 잘 생긴다.
- 예문: Contract drift — the backend half of three payloads was deleted, the frontend types weren't.
- 유사어: schema mismatch (정적이고 더 좁다), out of sync (평이한 회화체)
- 반의어: the two halves stay in lockstep

## "this comment now lies"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 코드가 바뀌어 주석이 사실과 달라졌을 때, 삭제·수정을 요구하며(리뷰 코멘트)
- 한국어: 이 주석은 이제 거짓말을 한다
- 설명: 주석을 주어로 세우고 사람에게 쓰는 동사 lie 를 붙였다. is outdated 가 상태 서술이라면 이쪽은 능동적 해악 — 읽는 사람을 속인다 — 이라는 판정이라 훨씬 세게 들린다.
- 예문: This comment now lies: "The backend still ships `defaults.focus_n`" was the documented reason to leave the contract alone, and the same change-series removed it.
- 유사어: is stale (중립), no longer holds (격식)
- 반의어: the comment still holds

## "leaving it invites someone to restore the field"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 틀린 코드·주석을 지우지 않고 두면 뒷사람이 그걸 근거로 되돌릴 위험을 경고할 때
- 한국어: 그대로 두면 누군가 그 필드를 되살리게 만든다
- 설명: invite 는 "초대하다"에서 "(원치 않는 일을) 자초하다"로 확장된다. 방치의 비용을 미래 인물의 구체적 행동으로 그려 보여서, 지우자는 요구가 취향이 아니라 예방책이 된다.
- 예문: Rewrite or delete; leaving it invites someone to "restore" the field.
- 유사어: is a trap for the next reader, sets the next person up to fail
- 반의어: deleting it forecloses that mistake

## "not swap-safe"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 겉보기에 같은 두 함수를 갈아 끼워도 되는지 한 줄로 가를 때(코드 리뷰)
- 한국어: 그대로 바꿔치기하면 안 되는
- 설명: swap 에 -safe 를 붙여 즉석에서 만든 합성어다. 같은 리팩터링 안에서 "여기까지는 바꿔도 되고 여기부터는 동작이 바뀐다"를 구분해 주며, 뒤에 근거를 콜론으로 이어 붙이는 형태로 쓴다.
- 예문: Not swap-safe: its inputs are KST-aware, so the existing `.replace("+00:00","Z")` is a no-op and `iso_z` would silently convert to UTC.
- 유사어: a behaviour change in disguise, not a like-for-like replacement
- 반의어: a safe swap, a drop-in replacement

## "the first assignment is dead"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 값을 넣었다가 아래에서 무조건 덮어쓰는 코드를 지적할 때
- 한국어: 앞의 대입은 죽은 코드다
- 설명: dead 는 실행은 되지만 결과가 아무 데도 쓰이지 않는 상태를 뜻한다. dead code / dead store 로 굳어진 용법이라 별도 설명 없이 리뷰에서 통한다.
- 예문: `trace["result_count"] = len(rows)` is unconditionally overwritten four lines later; the first assignment is dead.
- 유사어: a dead store, has no observable effect
- 반의어: is load-bearing

## "removal is type-only, no behaviour change"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 한국어: 지워도 타입만 사라질 뿐 동작은 그대로다
- 맥락: 삭제를 제안하면서 안전하다는 근거를 함께 대야 할 때(리뷰·PR 설명)
- 설명: 삭제 제안에 반드시 따라붙어야 할 두 마디를 압축한 형태다. 앞에 Verified by grep 처럼 확인 방법을 붙이면 리뷰어가 같은 절차로 재확인할 수 있다.
- 예문: Verified by grep: no runtime reads of any of these, so removal is type-only, no behaviour change.
- 유사어: a no-op at runtime
- 반의어: BEHAVIOUR-CHANGE — leave it

## "Tail for a follow-up"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-30-cleanup-self-audit-simplify.md
- 맥락: 리뷰에서 이번 범위 밖 잔여 항목을 잊지 않게 따로 떼어 둘 때(목록 머리·격식)
- 한국어: 나머지는 후속 작업으로
- 설명: tail 은 목록의 꼬리, 곧 중요도가 낮아 뒤로 밀린 잔여분이다. "이번엔 안 한다"는 선언과 "잊지는 않았다"는 약속을 한 마디로 동시에 한다.
- 예문: Tail for a follow-up (untouched files): the `sem_list`, `storage` and `meas_hist` mocks still hand-roll about eight more.
- 유사어: parking-lot items, out of scope for this pass
- 반의어: in scope for this change

## "Clean point:"
- 레지스터: professional, technical
- 출처: repo:auto_recipe_creator docs/opencode/2026-08-30-retire-legacy-poc-design-review.md
- 맥락: 지적 목록 끝에 "여기는 확인했고 문제없었다"를 남길 때(코드·설계 리뷰)
- 한국어: 확인 결과 문제없던 지점
- 설명: 지적만 늘어놓으면 리뷰가 어디까지 실제로 검토됐는지 알 수 없다. 문제를 못 찾은 지점을 따로 적어 검토 범위 자체를 증명하는 리뷰 관례다.
- 예문: Clean point: repository inspection found no Python runtime imports into the retired packages, supporting the no-port claim.
- 유사어: Nothing to flag here, checked and clean
- 반의어: Findings, ordered by value

## "what actually pins them apart"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 둘을 합칠 수 있냐는 질문에 답하기 전, 분리의 근거부터 확인하겠다고 말할 때(실무 대화)
- 한국어: 무엇이 둘을 실제로 갈라놓고 있는지
- 설명: pin 은 핀으로 꽂아 고정한다는 뜻이다. pin apart 는 사전에 오른 숙어가 아니라 pin down 을 비틀어 만든 표현인데, "둘 사이에 박혀 붙지 못하게 하는 것"이라는 그림이 바로 전달된다.
- 예문: Let me check what actually pins them apart before answering.
- 유사어: what keeps them separate, what the real difference is
- 반의어: what they already share

## "duplication documented in prose rather than removed"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 같은 코드가 두 곳에 있는데 주석으로만 그 사실을 적어 둔 상태를 비판할 때
- 한국어: 중복을 없애지 않고 글로 적어만 둔 것
- 설명: A rather than B 로 "했어야 할 일(제거)" 자리에 "실제로 한 일(기술)"을 끼워 넣어 대비시킨다. 주석이 많다는 사실 자체를 중복의 증거로 뒤집는 논법이라 반박하기 어렵다.
- 예문: `PmPlanningView.vue` carries eight comments saying "same as TttmView" — duplication documented in prose rather than removed.
- 유사어: a comment where a refactor belonged
- 반의어: the duplication was collapsed into one place

## "a feature nobody finds"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 새 설정을 기본 꺼짐으로 둘지 정할 때, 꺼진 기본값의 위험을 한 문장으로 경고(제품 논의)
- 한국어: 아무도 발견하지 못하는 기능
- 설명: 있어도 발견되지 않으면 없는 것과 같다는 UX 논거다. 관계절 nobody finds 를 명사 뒤에 붙여 설명이 아니라 판정으로 만든 점이 이 문장의 힘이다.
- 예문: A preference UI that starts empty is a feature nobody finds.
- 유사어: dead on arrival for discoverability
- 반의어: a feature that announces itself

## "a bug the merge exposed, not a reason to stop"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 리팩터링 도중 튀어나온 결함을 두고 작업을 되돌리자는 반응이 나올 때(설계 논의)
- 한국어: 합치기가 드러낸 버그지 멈출 이유는 아니다
- 설명: X, not Y 대구가 상대 결론만 정확히 겨눈다. "드러냈다(exposed)"와 "만들었다(introduced)"를 가르는 것이 이 반론의 전부다.
- 예문: That third one is the interesting part — it's a bug the merge exposed, not a reason to stop.
- 유사어: surfaced by, not caused by
- 반의어: a regression this change introduced

## "a checkbox that lies"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 컨트롤이 스스로 내건 약속을 못 지키는 UI 설계를 반박할 때
- 한국어: 거짓말하는 체크박스
- 설명: 무생물을 주어로 세우고 lie 를 붙이는 어법이다(cf. this comment now lies). 켜면 되는 줄 알았는데 옆 컨트롤이 더 필요한 체크박스는 사용자와의 약속을 어긴 셈이라는 판정.
- 예문: A checkbox that silently needed another control would be a checkbox that lies.
- 유사어: a control that doesn't do what it says
- 반의어: a control that keeps its promise

## "each X paid the same tax"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 같은 실수가 페이지·모듈마다 반복돼 왔음을 드러낼 때(사후 분석)
- 한국어: 새로 생긴 것마다 같은 비용을 치렀다
- 설명: 반복 비용을 세금에 비유해, 한 사람의 실수가 아니라 구조가 매번 청구하는 값임을 밝힌다. 뒤에 "and X was the first one to forget" 을 붙이면 이번 버그가 시간 문제였다는 결론까지 따라온다.
- 예문: Each new page paid the same tax, and `pm-planning` was the first one to forget.
- 유사어: pays a recurring cost, a guaranteed recurring tax (명사형)
- 반의어: the cost was paid once, in one place

## "makes silence the failure mode"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 기본값이 빈 값이 아니라 그럴듯한 값이라서 오류가 눈에 띄지 않는 설계를 지적할 때
- 한국어: 조용히 틀리는 것을 실패 방식으로 만든다
- 설명: 분기를 빠뜨렸을 때 화면이 비면 바로 알아채지만, 그럴듯한 값이 나오면 아무도 모른다. 이어지는 a confidently wrong one 이 그 위험을 인격화해 못 박는다.
- 예문: A fallback that means 장비 상태 makes silence the failure mode: forget a branch and you don't get a blank tab bar, you get a confidently wrong one.
- 유사어: fails silently, fails open
- 반의어: fails loudly, fails closed

## "mid-pack"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 파일 크기·성능 수치가 또래 대상과 견줘 특별히 나쁘지 않다고 판정할 때
- 한국어: 여럿 가운데 중간쯤
- 설명: 자전거·마라톤 경주에서 선두와 후미 사이 중간 집단(pack)을 가리키던 말이다. 절대 기준이 아니라 이웃과의 비교라는 점이 핵심이라, 리팩터링을 거절하는 근거로 쓰인다.
- 예문: 784 lines is mid-pack for this repo's View components, so splitting it would break consistency, not improve it.
- 유사어: middle of the pack, unremarkable for this codebase
- 반의어: an outlier

## "the odd file out"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 일관성을 근거로 "좋아 보이는 개선"을 거절할 때
- 한국어: 혼자만 튀는 파일
- 설명: the odd one out(무리에서 하나만 다른 것)의 변형이다. 그 변경이 나쁘다는 게 아니라 여기서만 다르게 만든다는 지적이라, 나중에 전체를 함께 바꾸자는 여지를 남긴다.
- 예문: Every sibling View in this repo keeps its pipeline inline, so extracting would make this one the odd file out.
- 유사어: the exception in an otherwise uniform set
- 반의어: consistent with its siblings

## "crosses the seam"
- 레지스터: technical, professional
- 출처: transcript:[user] skewnono-v3-nuxt/d3cb6758-cf05-44b1-8363-691e01340651.jsonl
- 맥락: 두 계층 사이에 무엇이 오가고 무엇은 안 오가는지 계약으로 못 박을 때
- 한국어: 경계를 넘어 전달되다
- 설명: seam 은 두 계층이 맞닿는 봉합선이다. 넘어가는 것 하나만 열거하면 나머지는 자동으로 내부 구현이 되므로, 금지 목록을 길게 쓰는 것보다 계약이 단단해진다.
- 예문: The filesystem `image_path` is never returned — only `figure_id` crosses the seam.
- 유사어: is what the boundary carries
- 반의어: stays on this side of the boundary

## "Deliberately not done:"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/7445fdf6-3fe2-4c5f-8232-6fee5e20fe67.jsonl
- 맥락: 작업 보고 끝에 안 한 일과 그 이유를 밝힐 때(격식·소제목)
- 한국어: 일부러 하지 않은 것
- 설명: 빠뜨림과 선택을 가르는 한 마디다. Skipped 보다 강해서, 몰라서 안 한 게 아니라 재 보고 판단했다는 뜻이 분명해진다. 뒤에 측정 근거를 붙이면 완결된다.
- 예문: Deliberately not done: extracting the 150-line analysis pipeline into a composable — I measured the sibling files first.
- 유사어: Out of scope by choice, Considered and rejected
- 반의어: left undone by oversight

## "worth a glance if X"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt/d3cb6758-cf05-44b1-8363-691e01340651.jsonl
- 맥락: 확신 못 하는 사항을 동료에게 가볍게 넘길 때(구어에 가까운 실무)
- 한국어: X 하면 한 번 봐 둘 만하다
- 설명: worth a look 보다 가볍다. 조건절을 달면 "지금 당장은 아니고 문제가 생기면"이라는 시점까지 함께 지정돼, 상대의 할 일 목록을 늘리지 않는다.
- 예문: The office agent's snippet spelled `minual_figures` — I used `manual_figures`; worth a glance if figures 404 at the office.
- 유사어: keep an eye on it, flagging it just in case
- 반의어: needs checking before you ship

## "per the (pathspec) rule"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator/a6e1b17a-2c86-4a6b-8a36-47edad1117b3.jsonl
- 맥락: 어떤 판단의 근거가 합의된 규칙임을 한 마디로 밝힐 때(작업 보고·격식)
- 한국어: (그) 규칙에 따라
- 설명: per + 규칙 이름은 "그 규칙에 따라"를 두 단어로 끝내는 격식 표현이다. 행동의 근거를 취향이 아니라 합의된 규칙에 두어, 왜 안 했냐는 되물음을 미리 막는다.
- 예문: Left them alone per the pathspec rule.
- 유사어: in line with our convention, as the rule requires
- 반의어: made an exception this time

## "before anyone acts on that report"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator/a6e1b17a-2c86-4a6b-8a36-47edad1117b3.jsonl
- 맥락: 낡은 문서를 폐기하라는 대신 실행 전에 손보라고 절제해 경고할 때
- 한국어: 누가 그 보고서대로 실행에 옮기기 전에
- 설명: act on X 는 "X 를 근거로 실제로 움직이다"이다. 문서 자체를 공격하지 않고 그것이 행동으로 옮겨지는 시점만 겨누므로, 남의 작업물을 두고 하는 지적으로 안전하다.
- 예문: That audit predates today's work — worth re-scoping those three lines before anyone acts on that report.
- 유사어: before it gets actioned (영국식 사무 영어)
- 반의어: safe to act on as written
