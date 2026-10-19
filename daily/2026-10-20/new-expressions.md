# 2026-10-20 — 새 표현

오늘 배치는 문서 5건과 대화 4건이다. 문서는 레시피 일괄 복사 설계 검토 묶음인데, 영어로 쓰인 건 Codex 에게 보낸 검토 요청서(`codex-r1-prompt.md`) 하나뿐이다. 나머지 검토서·종합·사무실 확인 요청은 한국어라 표현 원료가 되지 못했다. 요청서는 짧은 명령문과 명사구로 "무엇을, 어떤 기준으로, 얼마나 짧게" 답할지를 못 박는 글이라 리뷰 요청을 영어로 쓸 때 그대로 빌려 쓸 만하다. 대화 쪽 영어는 성과 리뷰 초안을 설명한 어시스턴트 답변에서 왔다. `Keep it tight.`, `be level with`, `precedent`, `I took this to mean …` 는 이미 노트에 있어 건너뛰었다.

## "Read-only; do not edit files."
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 리뷰·조사를 맡기면서 권한 범위를 맨 앞에 못 박을 때(작업 지시서·문어)
- 한국어: 읽기만 하고 파일은 고치지 마세요.
- 설명: 형용사 `Read-only` 하나로 성격을 선언하고, 세미콜론 뒤 명령문으로 구체 행동을 금지한다. "선언 + 금지"를 한 줄에 붙여 오해의 여지를 없앤다. 사람에게 보내는 메일이라면 `Please treat this as read-only` 정도로 누그러뜨린다.
- 예문: Read-only; do not edit files — just leave your notes in the review doc.
- 유사어: look but don't touch (구어, 가벼운 농담조), no changes, please (짧고 공손), for review only (문서 머리에 다는 표식)
- 반의어: feel free to edit (수정 허용)

## "New constraints from the user (not yet in handoff.md)"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 기존 문서에 아직 반영되지 않은 새 조건을 따로 묶어 알릴 때(소제목·문어)
- 한국어: 사용자가 새로 준 제약(아직 handoff.md 에 없음)
- 설명: 괄호 속 `not yet in X` 가 "문서가 틀린 게 아니라 아직 못 따라왔다"는 시점 정보를 준다. 읽는 쪽은 문서와 이 목록이 충돌할 때 이 목록이 이긴다는 걸 바로 안다.
- 예문: Here are two new constraints from the customer, not yet in the spec.
- 유사어: pending update to X (문서 갱신 예정이라는 뉘앙스), as of today (시점 강조), not reflected in X yet (조금 더 길고 공식적)
- 반의어: already captured in X (이미 반영됨)

## "at once, reliably"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 요구 사항의 핵심 두 축(동시성·신뢰성)을 문장 끝에 쉼표로 덧붙여 강조할 때(설계 문서)
- 한국어: 한꺼번에, 그리고 확실하게
- 설명: 부사 두 개를 쉼표로 이어 문장 끝에 둔다. 뒤에 붙은 `reliably` 가 덧붙인 생각처럼 보여서 오히려 더 강하게 들린다. "빠르기만 하면 안 되고 실패 없이"라는 요구가 단어 하나로 전달된다.
- 예문: The goal is to push the same recipe to ten tools at once, reliably.
- 유사어: in one go, without failures (구어), concurrently and dependably (딱딱한 문어), in parallel, safely (기술 문서)
- 반의어: one at a time (하나씩)

## "Either is allowed."
- 레지스터: professional, conversational
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 선택지 두 개를 나열한 뒤 어느 쪽도 막혀 있지 않다고 짧게 확인해 줄 때(지시서·회의)
- 한국어: 둘 다 가능합니다.
- 설명: `Either` 가 단수 취급이라 `is` 를 쓴다. `Both are allowed` 는 "둘을 같이 해도 된다"로 읽힐 수 있지만 `Either` 는 "둘 중 아무거나 하나"라서 선택의 문제임이 분명하다.
- 예문: You can use a separate app or scale up the current host; either is allowed.
- 유사어: Either works. (구어), Both options are on the table. (회의체), You're free to pick one. (공손)
- 반의어: Neither is acceptable. (둘 다 불가)

## "Hard requirement: X must not affect Y."
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 협상 불가능한 조건을 다른 조건과 구분해 맨 앞에 박을 때(요구 사항 문서·격식)
- 한국어: 절대 조건: X 는 Y 에 영향을 주면 안 된다.
- 설명: `Hard requirement:` 라는 콜론 머리말이 "이건 트레이드오프 대상이 아니다"를 선언한다. 뒤의 `must not` 은 금지의 가장 강한 조동사다. `should not` 으로 쓰면 권고로 약해진다.
- 예문: Hard requirement: the new batch job must not affect the running production service.
- 유사어: non-negotiable (가장 강함, 구어에서도 씀), a must-have (제품 회의), a blocking condition (기술 문서)
- 반의어: nice to have (있으면 좋은 것)

## "Questions I want your independent view on"
- 레지스터: professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 다른 검토자의 의견에 끌려가지 말고 따로 판단해 달라고 부탁할 때(리뷰 요청·격식)
- 한국어: 독립적인 의견을 듣고 싶은 질문들
- 설명: `a view on X` 의 전치사 `on` 이 관계절 끝에 남은 형태다(`questions on which I want your view`). `independent` 가 "앞선 결론을 보지 말고"라는 조건을 담는다. 교차 검토를 요청할 때 편향을 막는 표현이다.
- 예문: These are the questions I want your independent view on before we compare notes.
- 유사어: your fresh take on (구어), a second opinion on (흔함), your unbiased read on (조금 캐주얼)
- 반의어: just confirm what we've decided (동의 확인만 요청)

## "Give the decisive reason"
- 레지스터: professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 근거를 늘어놓지 말고 결론을 가른 이유 하나만 대라고 할 때(리뷰 요청·문어)
- 한국어: 결정적인 이유를 대라
- 설명: `decisive` 는 "판가름을 내는"이다. 여러 이유 중 그것 하나만으로 선택이 바뀌는 이유를 요구한다. 답변자가 장단점 표를 길게 쓰는 걸 미리 막는다.
- 예문: Pick one option and give the decisive reason in a single sentence.
- 유사어: the deciding factor (명사구로 자주 씀), what tips the balance (구어·비유), the clincher (캐주얼)
- 반의어: a minor consideration (부차적 고려)

## "what must be true of X for Y to work"
- 레지스터: technical, professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 방안이 성립하는 전제 조건을 묻거나 적을 때(설계 검토·문어)
- 한국어: Y 가 성립하려면 X 가 어떤 조건을 만족해야 하는가
- 설명: `be true of X` 는 "X 에 대해 참이다"로 성질을 묻는 틀이다. `for Y to work` 는 `for + 의미상 주어 + to부정사` 로 목적·조건을 붙인다. "가정 목록"을 질문 하나로 끌어낸다.
- 예문: List what must be true of the network for the remote worker to work.
- 유사어: the preconditions for (명사형, 격식), what it takes for X to (구어), the assumptions behind (전제를 따질 때)

## "What breaks if …?"
- 레지스터: technical, conversational
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 가정이 어긋났을 때 무엇이 깨지는지 실패 모드를 물을 때(설계 회의·리뷰)
- 한국어: …라면 무엇이 깨지나?
- 설명: 주어 자리에 `What` 을 두고 자동사 `break` 를 쓴다. "문제가 생기는가?"(yes/no)가 아니라 "무엇이"를 물어서 답이 구체적인 실패 목록이 된다.
- 예문: What breaks if the FTP server doesn't support directory rename?
- 유사어: What goes wrong if …? (구어), What's the failure mode if …? (기술 문서), What's the fallout if …? (영향 범위까지 포함)

## "where the ceiling is"
- 레지스터: technical, conversational
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 처리량·동시성의 상한이 어디서 걸리는지 물을 때(성능 논의)
- 한국어: 상한이 어디에 걸리는지
- 설명: `ceiling` 은 비유적으로 "더 올라갈 수 없는 한계"다. 뒤에 `(A vs B)` 를 붙여 병목 후보를 함께 제시하면 질문이 날카로워진다. `bottleneck` 이 막히는 지점을 말한다면 `ceiling` 은 도달 가능한 최대치를 말한다.
- 예문: Tell me where the ceiling is: the server's session limit or our CPU.
- 유사어: the upper bound (수학적·격식), the limiting factor (원인 쪽), hit the wall (구어, 동사구)
- 반의어: the floor (하한)

## "acceptable, or propose cheaper that is still trustworthy"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 현재 방식을 승인할지, 아니면 같은 신뢰도의 더 싼 대안을 낼지 양자택일로 물을 때(리뷰 요청)
- 한국어: 이대로 괜찮은가, 아니면 여전히 믿을 만하면서 더 싼 방법을 제안하라
- 설명: 형용사 하나(`acceptable`)로 첫 선택지를 닫고, 두 번째는 명령문으로 연다. `cheaper` 뒤에 명사(`an option`)가 생략된 압축체라 메모·프롬프트에서만 자연스럽다. 정식 문서라면 `propose a cheaper option that is still trustworthy` 로 쓴다.
- 예문: Is a full re-download acceptable, or can you propose a cheaper check that is still trustworthy?
- 유사어: good enough as is, or … (구어), justified, or is there a leaner alternative (격식)

## "The handoff admits X is unresolved."
- 레지스터: professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 문서가 스스로 인정한 빈틈을 짚으며 그 부분을 다뤄 달라고 할 때(검토·문어)
- 한국어: 인수인계 문서도 X 가 해결되지 않았다고 인정한다.
- 설명: 사물 주어(`The handoff`)에 사람 동사 `admits` 를 붙였다. 문서가 "솔직하게 시인했다"는 뉘앙스라 비난 없이 빈틈을 가리킨다. `says` 보다 "약점"이라는 색이 분명하다.
- 예문: The design doc admits the race condition is unresolved, so start there.
- 유사어: concedes (더 격식), acknowledges (중립·공손), leaves X open (비난 없이 사실만)
- 반의어: claims X is solved (해결됐다고 주장)

## "the best achievable mitigation"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 완전한 해결이 불가능함을 전제하고 현실적 최선책을 요구할 때(위험 관리·격식)
- 한국어: 달성 가능한 최선의 완화책
- 설명: `mitigation` 자체가 "줄이기, 없애기 아님"을 뜻하는데 `achievable` 이 한 번 더 "현실 제약 안에서"를 박는다. 뒤의 `without a lock` 같은 제약 조건과 짝을 이뤄 쓰인다.
- 예문: Propose the best achievable mitigation without a lock.
- 유사어: the best we can do under the constraints (구어), a pragmatic safeguard (격식), damage control (사후 대응 뉘앙스, 구어)
- 반의어: a complete fix (완전한 해결)

## "state the residual risk plainly"
- 레지스터: professional
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 대책 뒤에 남는 위험을 돌려 말하지 말고 문장으로 적으라고 할 때(위험 분석·격식)
- 한국어: 남는 위험을 있는 그대로 적어라
- 설명: `residual` 은 "대책 후에도 남는"이다. `plainly` 가 "완곡어법·면책성 수식어 없이"를 요구한다. 위험 문서에서 독자가 가장 원하는 건 남은 위험이 무엇인지 한 문장으로 아는 것이다.
- 예문: After the mitigation, state the residual risk plainly so the operators know what to watch.
- 유사어: spell out what's left (구어), be upfront about the remaining risk (조금 부드러움), call out the leftover risk (기술 문서)
- 반의어: gloss over the risk (위험을 얼버무리다)

## "wrong, contradictory, over-engineered, or missing"
- 레지스터: professional, technical
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 리뷰어에게 찾아야 할 결함의 종류를 네 갈래로 나눠 줄 때(리뷰 요청)
- 한국어: 틀렸거나, 서로 모순되거나, 과하게 설계됐거나, 빠진 것
- 설명: 형용사 넷을 병렬로 둔다. 사실 오류 → 내부 모순 → 과잉 → 누락 순이라 "있어서 문제"와 "없어서 문제"를 다 덮는다. 리뷰 기준을 이렇게 쪼개 주면 답이 칭찬 위주로 흐르지 않는다.
- 예문: Flag anything in the spec that is wrong, contradictory, over-engineered, or missing.
- 유사어: errors, inconsistencies, overkill, or gaps (명사형), what's off, what clashes, what's too much, what's not there (구어)

## "No restating the handoff."
- 레지스터: professional, conversational
- 출처: repo:bulk_recipe_copy docs/design/codex-r1-prompt.md
- 맥락: 이미 아는 내용을 요약하지 말고 새 판단만 달라고 할 때(지시서·짧은 메모)
- 한국어: 인수인계 문서 내용을 되풀이하지 마세요.
- 설명: `No + 동명사` 는 표지판 문체(`No smoking`)의 금지다. 명령문(`Don't restate`)보다 짧고 규칙처럼 들린다. 지시서 끝에 몰아 두면 "형식 규칙"으로 읽힌다.
- 예문: Numbered findings only. No restating the original proposal.
- 유사어: Skip the recap. (구어), Don't summarize the doc back to me. (구어, 조금 길다), Assume I've read it. (부드러움)
- 반의어: Start with a summary. (요약부터)

## "from your boss's point of view"
- 레지스터: professional, conversational
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 문서 구성을 읽을 사람 입장에 맞췄다고 설명할 때(보고·구어/문어 공통)
- 한국어: 상사 입장에서 보면
- 설명: 소유격 `boss's` 를 꼭 붙인다. `from the boss point of view` 는 비문이다(코칭 카드 참고). 글의 구성 원칙을 독자 기준으로 설명하는 첫 문장에 잘 붙는다.
- 예문: From your boss's point of view, impact matters more than the tech stack.
- 유사어: through your manager's eyes (조금 문학적), from a reviewer's perspective (격식), as your boss would see it (구어)

## "I left these blank rather than invent figures."
- 레지스터: professional
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 모르는 수치를 지어내지 않고 빈칸으로 남긴 이유를 밝힐 때(보고서 초안 전달)
- 한국어: 수치를 지어내는 대신 비워 두었습니다.
- 설명: `rather than + 동사원형` 으로 "하지 않은 쪽"을 명시한다. 빈칸이 실수가 아니라 의도된 선택임을 한 문장으로 알린다. `invent figures` 는 "숫자를 만들어내다"의 직설 표현이다.
- 예문: I left the cost line blank rather than invent a figure; please fill in the real number.
- 유사어: rather than guess (부드러움), instead of making up numbers (구어), pending confirmation (격식, 표 안에서)

## "would make the strongest claims hard to dispute"
- 레지스터: professional
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 근거 보강이 주장에 어떤 힘을 주는지 설명할 때(설득·평가 문서)
- 한국어: 가장 강한 주장들을 반박하기 어렵게 만든다
- 설명: `make + 목적어 + 형용사 + to부정사` 구조다. `hard to dispute` 가 "반박 불가"보다 한 단계 겸손해 과장처럼 들리지 않는다. 숫자를 채워 달라고 부탁하는 문장 뒤에 붙이면 동기가 된다.
- 예문: Adding the before-and-after numbers would make your strongest claims hard to dispute.
- 유사어: airtight (강함), hard to argue with (구어), well-substantiated (격식)
- 반의어: easy to poke holes in (구어, 허점이 많은)

## "Impact comes before features."
- 레지스터: professional
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 성과 보고·제안서의 서술 순서 원칙을 한 줄로 말할 때(보고서 작성 조언)
- 한국어: 기능보다 효과가 먼저다.
- 설명: `come before` 가 순서(배치)와 우선순위를 동시에 말한다. 세 단어짜리 원칙문이라 소제목이나 피드백 첫 줄로 좋다.
- 예문: In a promotion review, impact comes before features.
- 유사어: lead with the outcome (구어), outcomes over outputs (경영 문구), put the why before the what (설명적)
- 반의어: features first (기능 나열부터)

## "proof from outside your own work"
- 레지스터: professional
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 자기 주장이 아니라 제3자(수상·타 팀 의존)가 보증하는 근거임을 강조할 때(평가·추천)
- 한국어: 내 일 바깥에서 온 증거
- 설명: `from outside` 가 "자기 평가가 아님"을 뜻한다. 같은 단락의 `official recognition`, `another team relies on what you built` 가 그 예시다. 승격 심사에서 가장 무게가 실리는 근거 유형을 짚는 말이다.
- 예문: The award and the other team's dependence are proof from outside your own work.
- 유사어: third-party validation (격식), external evidence (중립), others vouching for it (구어)
- 반의어: self-assessment (자기 평가)

## "you went from building things to planning projects and training people"
- 레지스터: professional, conversational
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 한 해 동안 역할이 어떻게 넓어졌는지 성장 서사로 한 문장에 담을 때(성과 리뷰)
- 한국어: 만드는 사람에서 과제를 기획하고 사람을 가르치는 사람으로 넘어갔다
- 설명: `go from A to B` 가 변화의 방향을 보여준다. B 자리에 동명사 둘(`planning`, `training`)을 병렬로 두어 확장된 범위를 나열한다. 승격 사유의 "이미 상위 레벨 일을 하고 있다"로 이어지는 문장이다.
- 예문: This year I went from building tools to planning projects and training other engineers.
- 유사어: grew from X into Y (성장 강조), moved beyond X to Y (격식), stepped up from X to Y (구어)

## "it prints cleanly and works in dark mode"
- 레지스터: technical, conversational
- 출처: transcript:pm_notes my-task [assistant]
- 맥락: 산출물(HTML 등)의 실사용 품질을 짧게 보장할 때(작업 보고)
- 한국어: 인쇄해도 깔끔하고 다크 모드에서도 잘 보인다
- 설명: `print` 를 자동사로 써서 "문서가 (깔끔하게) 인쇄된다"를 표현한다. `read well`, `sell well` 처럼 사물 주어 + 자동사 + 부사 패턴이다.
- 예문: The report is one self-contained file; it prints cleanly and works in dark mode.
- 유사어: is print-friendly (형용사형), looks right on paper (구어), renders correctly in print (기술 문서)

## "To review X instead, pass it as the target"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt subagent [assistant]
- 맥락: 지금 요청으로는 할 일이 없을 때 원하는 결과를 얻는 다른 사용법을 안내할 때(도구 출력·문서)
- 한국어: 대신 X 를 검토하려면 그걸 대상으로 넘기세요
- 설명: `To + 동사` 로 목적을 앞에 두고 명령문으로 방법을 준다. `instead` 가 "지금 요청과 다른 경로"임을 알린다. 빈 결과를 돌려줄 때 사용자가 다음 행동을 바로 알게 한다.
- 예문: To review the latest commit instead, pass it as the target, e.g. `/code-review HEAD~1`.
- 유사어: If you meant X, run … (구어), Alternatively, specify X as … (격식)
