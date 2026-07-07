# 2026-07-08 — 새 표현

오늘 배치는 auto_recipe_creator의 ensemble 통합·검증 작업 transcript가 중심입니다.
코드 리뷰 보고서·태스크 지시문에서 나온, 검증·보고에 바로 쓸 수 있는 표현들입니다.

## "a clean lift-and-shift"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator subagent (Task 1 리팩터 보고)
- 맥락: 리팩터링 보고에서 "로직 변경 없이 코드를 그대로 들어 옮기기만 했다"고 안심시킬 때(문어·보고)
- 한국어: 그대로 들어 옮긴 (로직 무변경) 이식
- 설명: 원래 클라우드 마이그레이션 용어(재설계 없이 서버를 통째로 옮기기)인데, 코드 추출·리팩터에도 씁니다. "clean"이 붙어 "부수 변경이 전혀 섞이지 않았다"는 뉘앙스가 강해집니다.
- 예문: The extraction is a clean lift-and-shift with no logic changes.
- 유사어: a verbatim move (한 단계 더 문자 그대로), a mechanical refactor (판단 없이 기계적으로)
- 반의어: a rewrite / a redesign (동작·구조를 바꾸는 재작성)

## "Do not trust the report — verify by reading the actual code"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator subagent (검증자 지시문)
- 맥락: 검증자·리뷰어에게 "보고서를 믿지 말고 원본을 직접 확인하라"고 지시할 때(지시문·격식)
- 한국어: 보고를 믿지 말고 실제 코드를 읽어 검증하라
- 설명: `verify by -ing`(~함으로써 검증하라) 구조가 핵심입니다. "the actual code"의 actual은 "주장 말고 실물"을 대비시키는 단어입니다.
- 예문: Do NOT trust the implementer's report — verify by reading the actual code.
- 유사어: take nothing on faith (아무것도 믿고 넘기지 마라, 관용구), verify independently (독립적으로 검증하라, 더 중립적)
- 반의어: take it at face value (액면 그대로 믿다)

## "a hard blocker"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator subagent (마이그레이션 리스크 맵)
- 맥락: 리뷰·리스크 보고에서 "이건 우회 불가, 고치기 전엔 진행 불가"라고 심각도를 못 박을 때
- 한국어: (우회 불가능한) 결정적 차단 요인
- 설명: blocker 앞의 hard가 "soft(경고 수준)"와 대비됩니다. 마이그레이션 리스크 맵에서 "The entire adjust→primary path dies on migration. **Hard blocker.**"처럼 한 단어 문장으로 던지면 심각도가 극적으로 전달됩니다.
- 예문: The orb gate at line 124 kills the adjust path entirely — that's a hard blocker for the migration.
- 유사어: a showstopper (더 구어적·극적), a merge blocker (병합 한정), must-fix (형용사적)
- 반의어: a nice-to-have (없어도 되는 개선), cosmetic (표면적인)

## "(a code path) silently goes dead"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator subagent (마이그레이션 리스크 맵)
- 맥락: 에러 없이 분기 하나가 조용히 작동을 멈추는 회귀를 경고할 때(리뷰·문어)
- 한국어: (코드 경로가) 소리 없이 죽다/무력화되다
- 설명: `go dead`는 전화선·회로가 "먹통이 되다"에서 온 표현. crash와 달리 아무 신호 없이 기능만 사라지는 것이라 silently와 잘 붙습니다. "a behavior change, not a crash"와 짝으로 쓰면 완벽합니다.
- 예문: If the ensemble leaves those fields at defaults, the not_distinctive status branch silently goes dead — a behavior change, not a crash.
- 유사어: become a no-op (호출은 되지만 아무 일도 안 함), be silently disabled (수동태·더 직설)
- 반의어: fail loudly / crash hard (요란하게 실패하다)

## "lumped together"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator subagent (eval 러너 버그 헌트)
- 맥락: 구분해야 할 것들이 한 덩어리로 뭉뚱그려져 진단이 안 될 때(구어·리뷰)
- 한국어: (구분 없이) 한데 뭉뚱그려진
- 설명: lump는 "덩어리". 카운터·범주가 원인별로 분리되지 않아 "어느 쪽 탓인지 알 수 없다"는 불만과 함께 자주 나옵니다.
- 예문: It's unclear which function failed — both are lumped together under one match_failed counter.
- 유사어: conflated (격식·개념 혼동 뉘앙스), merged indistinguishably (문어)
- 반의어: broken out (per-arm) (항목별로 분리 집계된)

## "no dangling reference"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator subagent (코드리뷰 fix I4 지시문)
- 맥락: 리스트를 잘라내는 수정에서 "선택된 객체가 잘려나간 밖을 가리키는 일은 없다"고 안전성을 증명할 때
- 한국어: 허공을 가리키는 참조 없음
- 설명: dangle은 "매달려 대롱거리다". dangling reference/pointer는 대상이 사라진 뒤에도 남아 있는 참조를 가리키는 고전 용어인데, 여기서는 "trim 후에도 best_cand가 pool 안에 남는다"는 불변식 증명에 쓰였습니다.
- 예문: best_cand is always within candidates[:top_n], so it remains a member of the trimmed pool — no dangling reference.
- 유사어: no stale pointer (메모리 뉘앙스가 더 강함), still a member of the pool (풀어 쓴 표현)

## "I now have a complete picture"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator subagent (조사 진행 보고)
- 맥락: 조사·탐색을 마치고 "이제 전모를 파악했으니 결론으로 간다"고 전환을 알릴 때(진행 보고·구어)
- 한국어: 이제 전체 그림이 파악됐다
- 설명: 증거 수집 단계에서 판단 단계로 넘어가는 신호탄 문장. "I have everything I need" 보다 "부분들이 하나의 그림으로 맞춰졌다"는 뉘앙스가 있습니다.
- 예문: I now have a complete picture — let me compile the migration risk map.
- 유사어: I have everything I need (필요조건 충족 뉘앙스), the picture is clear now (상태 서술)
- 반의어: I'm still missing pieces (아직 퍼즐 조각이 빠져 있다)

## "safe to leave as-is"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator subagent (마이그레이션 리스크 맵)
- 맥락: 리뷰에서 "이 항목은 손대지 않아도 된다"고 범위에서 제외할 때
- 한국어: 그대로 둬도 안전한
- 설명: as-is(현재 상태 그대로)에 leave(놔두다)와 safe(안전 판단)가 결합. 리스크 맵에서 "must-fix" 목록과 대비되는 반대편 목록의 제목으로 쓰기 좋습니다.
- 예문: Relative comparisons like the OM-vs-SEM race are safe to leave as-is.
- 유사어: can stay untouched (구어), requires no change (격식·건조)
- 반의어: must-fix (반드시 고쳐야 하는)

## "correct by design"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator subagent (eval 러너 버그 헌트)
- 맥락: 의심스러워 보이던 코드가 "설계 전제 덕분에 원래 옳다"고 결론지을 때(리뷰·문어)
- 한국어: 설계상 옳은 (우연히 맞는 게 아니라)
- 설명: `X by design` 패턴("의도된 것이다")의 대표형. "both images come from the same tool at matching pixel scales — this is the core assumption. So this is correct by design."처럼 전제를 먼저 깔고 결론으로 씁니다. 비슷한 자리에서 correct-by-intent(의도상 옳음)도 나왔습니다.
- 예문: The offset convention matches the validated eval, so this is correct by design, not a bug.
- 유사어: intended behavior (더 평이), safe by construction (구조적으로 보장됨)
- 반의어: accidentally correct (지금은 우연히 맞을 뿐인)

## "deliberately mirror (the already-validated X)"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator subagent (eval 러너 버그 헌트 지시문)
- 맥락: 새 코드가 검증된 기존 코드를 "일부러 그대로 본떴다"고 밝혀, 리뷰 관점을 '차이점 찾기'로 좁힐 때
- 한국어: (검증된 기존 것을) 의도적으로 그대로 본뜨다
- 설명: mirror가 동사로 "거울처럼 똑같이 하다". deliberately가 붙으면 "우연한 유사가 아니라 설계 원칙"임을 선언합니다. already-validated(이미 검증된)라는 복합 수식어와 세트로 외워둘 만합니다.
- 예문: This runner deliberately mirrors the already-validated proposer_recall_ab.py — your highest-value check is where it diverges.
- 유사어: be modeled on (본떠 만들다), follow X to the letter (한 글자까지 따르다)
- 반의어: diverge from (기준에서 갈라지다)

## "Keep it tight."
- 레지스터: conversational, casual
- 출처: transcript:auto_recipe_creator subagent (보고 형식 지시)
- 맥락: 보고·발표를 "군더더기 없이 짧게" 하라고 지시할 때(구어·명령형)
- 한국어: 간결하게 해라, 늘어지지 마라
- 설명: tight는 "빈틈 없이 조여진". 보고 형식 요구 끝에 한 문장으로 붙이면 "Be concise"보다 훨씬 자연스러운 구어체가 됩니다.
- 예문: Report status, the two edits, and the three test results. Keep it tight.
- 유사어: keep it brief (중립), no fluff (군더더기 금지, 더 캐주얼)
- 반의어: pad it out (분량을 불리다)

## "Ask if genuinely blocked."
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator subagent (태스크 지시문)
- 맥락: 위임할 때 "사소한 건 알아서 하고, 정말 막혔을 때만 물어라"라고 질문 기준을 정할 때
- 한국어: 정말로 막혔을 때만 물어봐라
- 설명: genuinely가 핵심 — "그냥 애매한 정도"와 "진짜 진행 불가"를 가르는 문턱을 한 단어로 세웁니다. 위임 지시문의 표준 마무리 문장.
- 예문: If anything is unclear, use your judgment; ask if genuinely blocked.
- 유사어: escalate only when stuck (격식·프로세스 뉘앙스), don't ask, decide (더 강한 위임)
- 반의어: check in at every step (매 단계 확인받다)

## "only real, nameable issues"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator subagent (버그 헌트 지시문)
- 맥락: 리뷰어에게 "느낌·짐작 말고, 이름 붙여 설명 가능한 결함만 보고하라"고 기준을 줄 때
- 한국어: 실재하고 구체적으로 지목 가능한 문제만
- 설명: nameable(이름 붙일 수 있는)이 묘미 — "vague concern(막연한 불안)"의 반대로, 파일·줄·시나리오를 특정할 수 있는 결함만 받겠다는 뜻입니다. "If none, return []"과 세트로 빈손 보고도 정상 결과로 인정합니다.
- 예문: Output up to six findings — only real, nameable issues; if none, return an empty list.
- 유사어: concrete, actionable findings (조치 가능한 발견), no speculative flags (추측성 지적 금지)
- 반의어: vague concerns / hunches (막연한 불안·감)

## "the whole point of X is to Y"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator subagent (removed-behavior 감사)
- 맥락: "그게 버그가 아니라 바로 그것이 존재 이유"라고 오해를 뒤집을 때(구어)
- 한국어: X의 존재 이유 자체가 Y다
- 설명: point(요지·목적)에 whole이 붙어 "부수 효과가 아니라 그 자체가 목적"임을 강조합니다. 리뷰에서 의도된 변화를 버그로 오인한 지적을 반박할 때 특히 유용합니다.
- 예문: The whole point of that runner is to measure the new decision under the new thresholds, so the changed meaning is intended there, not a bug.
- 유사어: that's precisely what it's for (격식 한 단계 위), by definition (정의상)
- 반의어: an unintended side effect (의도치 않은 부수 효과)
