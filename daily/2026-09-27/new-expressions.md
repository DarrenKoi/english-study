# 2026-09-27 — 새 표현

> 오늘 배치는 transcript 10건이고 repo 문서와 spool 노트는 없었다. 표현 22개는 모두 `[assistant]` 영어에서 골랐다. 출처 세션은 auto-recipe-creator 의 점유 판독·SEM 이동 모드 감지 디버깅, equipment-data-map 의 연구·스펙 개정·home/office 분리·ftp_handler 리뷰 반영. `half right`, `that settles it`, `worth a look` 은 노트에 거의 같은 표현이 있어서 뺐다.

## "fix at the root"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 증상만 덮지 않고 원인 지점을 고치겠다고 작업 방향을 밝힐 때(버그 보고 답변·커밋 설명, 격식 중간).
- 한국어: 근본 원인에서 고치다
- 설명: `at the root` 는 "뿌리에서"라는 부사구. `fix` 뒤에 붙으면 땜질이 아니라 원인을 고친다는 말이 된다. 원문은 `trace how … versus …, then fix at the root` 로 "추적 먼저, 수정은 그다음"이라는 순서까지 한 문장에 담았다. 같은 세션의 `Reusing the shared function is the root-cause fix` 처럼 형용사형 `root-cause fix` 로도 쓴다.
- 예문: I'll trace how the row point gets located here versus the office-verified tool-select path, then fix at the root.
- 유사어: address the root cause (격식), get to the bottom of it (원인 규명에 방점, 구어), fix it properly (평이)
- 반의어: patch over the symptom / a band-aid fix (증상만 덮는 땜질)

## "change the question rather than pad the answer"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 모델이나 도구가 어떤 종류의 답을 잘 못 낼 때 보정값을 덧대지 말고 묻는 방식을 바꾸자는 설계 원칙을 말할 때(설계 글·리뷰).
- 한국어: 답에 여유분을 덧대지 말고 질문을 바꿔라
- 설명: `pad` 는 "완충재를 덧대다"로, 코드에서 bbox 에 픽셀을 더하는 padding 과 겹친다. `rather than` 앞뒤에 동사원형 `change` / `pad` 를 맞춘 병렬 구조다. mai-ui 가 열 폭 추정에 약하자 "폭 대신 헤더 중심점만 묻자"로 질문을 바꾼 맥락에서 나왔다.
- 예문: When a model is unreliable at one kind of answer, change the question rather than pad the answer.
- 유사어: reframe the problem (격식), ask it something it's good at (구어), play to the tool's strengths (관용)
- 반의어: pile on correction factors (보정값만 계속 쌓다)

## "Two gates on the same fact are not twice as safe."
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 같은 사실을 두 번 검사하면 더 안전하다는 직관을 반박할 때(설계 리뷰, 격식 중간).
- 한국어: 같은 사실에 관문을 둘 둔다고 두 배로 안전해지지는 않는다.
- 설명: `twice as + 형용사` 는 배수 비교. 원문은 바로 뒤에 이유를 붙인다. `When the weaker reader sits downstream of the stronger one, its disagreements are almost all its own noise.` 약한 판독기가 강한 판독기 뒤에 있으면 둘이 어긋날 때 틀린 쪽은 거의 늘 약한 쪽이다. 그래서 두 번째 관문은 거짓 unknown 만 늘린다.
- 예문: Two gates on the same fact are not twice as safe.
- 유사어: More checks aren't always safer. (평이), A redundant check only adds noise. (구체적)
- 반의어: defense in depth (서로 독립인 층이 겹쳐 실제로 안전이 커지는 경우)

## "a deliberate trade"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 설계의 허점을 질문받았을 때 알고 고른 절충이라고 밝히면서 약점도 같이 인정할 때(질문 답변·설계 설명).
- 한국어: 의도한 절충
- 설명: 여기서 `trade` 는 `trade-off` 의 준말 격. 원문 `That is a deliberate trade, but it has a weak point.` 은 "일부러 그랬다"로 방어하고 곧바로 `but` 으로 약점을 인정한다. 방어만 하면 고집으로, 약점만 말하면 실수로 들린다. 한 문장에 둘을 담아 균형을 잡았다.
- 예문: That is a deliberate trade, but it has a weak point.
- 유사어: a conscious trade-off (격식), a calculated compromise (문어), I did that on purpose, but … (구어)
- 반의어: an oversight (미처 못 본 실수)

## "the same class of bug as X"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 새 버그가 예전에 겪은 버그와 원인 구조가 같다고 묶어 말할 때(디버깅 대화·포스트모템).
- 한국어: X 와 같은 부류의 버그
- 설명: `class` 는 "부류". 사례 하나(instance)가 아니라 같은 원인에서 나오는 버그 묶음을 가리킨다. 원문은 관사와 주어를 뺀 조각문 `Same class of bug as …` 로 시작해 콜론 뒤에 공통 원인을 붙인다. 노트에 있는 `a known class of problem` 이 "알려진 유형"이라면 이쪽은 두 버그를 나란히 놓는 비교다.
- 예문: Same class of bug as the demo's "wrong Close" lesson: a generic label locator on the whole tool window finds any OK.
- 유사어: the same failure mode as (격식·공학), a cousin of that bug (구어, 닮았지만 똑같진 않음), history repeating itself (구어)
- 반의어: a one-off (한 번뿐인 별개 사고)

## "in order of likelihood"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 가능한 원인 여러 개를 확률 높은 순으로 늘어놓을 때(진단 보고·장애 분석).
- 한국어: 가능성이 높은 순서대로
- 설명: `in order of + 명사` 는 정렬 기준을 밝히는 틀이다(`in order of importance`, `in order of priority`). 원문은 `Three reasons that happens, in order of likelihood:` 로 개수와 정렬 기준을 먼저 알린 뒤 목록을 연다. 읽는 사람은 첫 항목부터 확인하면 된다는 걸 바로 안다.
- 예문: There are three reasons that happens, in order of likelihood.
- 유사어: from most to least likely (평이), in descending order of probability (문어), starting with the usual suspect (구어)
- 반의어: in no particular order (순서에 의미 없음)

## "The fix is a stronger anchor, not a longer prompt."
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 모델이 대상을 못 찾을 때 프롬프트를 늘리자는 제안에 "입력의 기준점을 바꾸자"로 방향을 돌릴 때(LLM·VLM 설계 대화).
- 한국어: 필요한 건 더 긴 프롬프트가 아니라 더 확실한 기준점이다.
- 설명: `The fix is A, not B.` 는 해결책을 대비로 못 박는 틀이다. 비교급 `stronger` / `longer` 가 운율을 맞춘다. `anchor` 는 위치를 잡을 때 기준으로 삼는 확실한 대상으로, 여기서는 이미 검증된 SEM box 다.
- 예문: It is coarse-to-fine already, but the fix is a stronger anchor, not a longer prompt.
- 유사어: More words won't help; a better reference point will. (평이), Better input beats better instructions. (격언풍)
- 반의어: just tweak the prompt (문구만 손보기)

## "turn the problem from X into Y"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 상대가 준 정보 덕에 문제의 성격이 바뀌어 쉬워졌다고 공을 돌릴 때(협업 대화·회고).
- 한국어: 문제를 X 에서 Y 로 바꿔 놓다
- 설명: `turn A into B` 는 "A 를 B 로 바꾸다"이고 `from` 을 넣으면 출발점이 두드러진다. 원문은 `A better prompt alone would not have fixed it` 로 가정법 과거완료를 써서 "프롬프트만으론 안 됐을 것"이라 말한 뒤 사용자의 버튼 목록이 열쇠였다고 인정한다.
- 예문: A better prompt alone would not have fixed it, but your button list did, because it turned the problem from "find a tiny icon" into "find a text button and count".
- 유사어: reframe the problem as (격식), change the whole picture (구어), make it a different problem (평이)
- 반의어: leave the problem as hard as it was

## "X are worth more than Y"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 양보다 확실성이 중요하다는 판단을 숫자 대비로 짧게 말할 때(설계 판단 설명).
- 한국어: X 가 Y 보다 값지다
- 설명: `worth more than` 은 값어치 비교다. 원문은 `two confirmed` / `thirteen guessed` 로 숫자와 분사 형용사를 짝지어 대비를 날카롭게 했다. 속담 `A bird in the hand is worth two in the bush.` 와 같은 틀이다.
- 예문: Two confirmed text anchors are worth more than thirteen guessed icons.
- 유사어: quality over quantity (관용), A bird in the hand is worth two in the bush. (속담), One solid X beats ten shaky Ys. (구어)
- 반의어: the more, the better (많을수록 좋다)

## "Fair question."
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 상대가 내 결정의 허점을 찌르는 질문을 했을 때 그 지적이 정당하다고 먼저 인정할 때(채팅·회의, 구어).
- 한국어: 물을 만한 질문이에요.
- 설명: `Good question` 이 질문을 칭찬한다면 `Fair question` 은 "그렇게 따질 만하다"고 인정하는 쪽이다. 원문은 이어서 자기 판단이 지나쳤다고 털어놓는다. 방어하기 전에 인정부터 하는 짧은 쿠션 말이다.
- 예문: Fair question. The two earlier icon attempts failed on a full-window capture and on a strip cut to the box height.
- 유사어: Fair point. (질문이 아니라 주장을 받을 때), That's a reasonable question. (격식), You got me there. (구어, 허를 찔렸을 때)

## "over-correct"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 실패를 피하려다 반대쪽으로 너무 나간 내 판단을 인정할 때(회고·사과, 격식 중간).
- 한국어: 지나치게 바로잡다, 반대로 너무 가다
- 설명: 운전하다 핸들을 너무 꺾는 데서 나온 말이다. `by + -ing` 로 무엇을 지나치게 했는지 밝힌다. 두 번 실패하고 나서 아예 다시 시도하지 않은 게 과잉 교정이었다는 고백이다.
- 예문: I over-corrected by never retrying once the strip covered the full column.
- 유사어: overshoot (목표를 지나치다), swing too far the other way (구어), overcompensate (심리·격식)
- 반의어: not go far enough (덜 바로잡다)

## "silently revert to X"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 코드가 오류 없이 조용히 더 약한 동작으로 되돌아가는 함정을 경고할 때(코드 리뷰·설계 문서).
- 한국어: 소리 없이 X 로 되돌아가다
- 설명: 개발 영어에서 `silently` 는 "에러나 경고 없이"라는 뜻으로 자주 붙는다(`silently fails`, `silently drops`). 진행형 `is silently reverting` 은 그 출력을 읽는 순간마다 벌어진다는 느낌을 준다. 노트의 `can't quietly revert` 는 git 되돌리기라 뜻이 다르다.
- 예문: Any consumer that reads the coarse output is silently reverting to the weaker stage.
- 유사어: quietly fall back to (평이), regress without warning (격식), undo the fix behind your back (구어)
- 반의어: fail loudly (눈에 띄게 실패하다)

## "building ahead of the data"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 결과가 아직 안 나온 단계에 기대어 다음 작업을 미리 만들려는 걸 말릴 때(계획 논의).
- 한국어: 데이터보다 앞서 만들기
- 설명: `ahead of` 는 "~보다 앞서". 원문 `Starting them now would be building ahead of the data.` 는 `would be` 로 "지금 시작하면 그렇게 된다"고 가정해 부드럽게 말린다. `get ahead of oneself`(김칫국부터 마시다)와 결이 같다.
- 예문: Steps 3–5 all depend on the step 2 results, so starting them now would be building ahead of the data.
- 유사어: getting ahead of ourselves (구어), premature (격식), putting the cart before the horse (관용)
- 반의어: let the data lead (데이터가 나온 뒤 따라가기)

## "It works, but only while …"
- 레지스터: professional
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 지금 방식이 돌아가긴 하지만 사람의 기억 같은 약한 전제에 기대고 있다고 조건을 달 때(설계 비판).
- 한국어: 되긴 하는데, ~하는 동안에만이다
- 설명: `only while` 이 "그 조건이 유지되는 동안만"으로 유효 범위를 좁힌다. 원문 `That works, but only while both sides remember a list of files.` 은 칭찬처럼 시작해 조건절로 약점을 드러낸다. 이어지는 `The weak spot is …` 로 어디가 깨질지 짚는 흐름까지 한 세트다.
- 예문: That works, but only while both sides remember a list of files.
- 유사어: It holds as long as … (평이), It works, provided that … (격식), It works until someone forgets … (구어)
- 반의어: It works by construction. (전제 없이 구조상 성립)

## "Not quite."
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상대 이해가 거의 맞지만 핵심 하나가 다를 때 부드럽게 정정하며 말문을 열 때(채팅·회의).
- 한국어: 꼭 그렇진 않아요.
- 설명: `No` 보다 훨씬 부드럽다. 원문은 바로 다음 문장에서 어디가 다른지 짚는다. `Not quite.` 만 던지고 멈추면 퉁명스러우니 한 문장 설명을 꼭 붙인다.
- 예문: Not quite. With what I just wrote, the office agent still writes inside the parser folder.
- 유사어: Close, but … (구어), Almost. (구어), That's not entirely accurate. (격식)
- 반의어: Exactly. / Spot on.

## "has stopped mattering"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 상황이 바뀌어 한때 중요하던 할 일이 의미를 잃었다고 알릴 때(진행 상황 공유).
- 한국어: 더는 중요하지 않게 됐다
- 설명: `stop + -ing` 는 "~하기를 멈추다". 현재완료 `has stopped` 가 "이미 그렇게 됐다"를 보여 주고 `probably` 가 단정을 누그러뜨린다. 원문은 `106 files were measured through the proxy, so SIZE is working.` 으로 근거를 댄다.
- 예문: One side note: the proxy redeploy has probably stopped mattering.
- 유사어: is now moot (격식), is no longer relevant (평이), is off the table (구어, 선택지에서 빠짐)
- 반의어: still matters / has become critical

## "slip back in"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 막아 둔 것이 몰래 다시 끼어들지 못하게 하는 장치를 설명할 때(코드 설명).
- 한국어: 슬그머니 다시 들어오다
- 설명: `slip` 은 "미끄러지듯 몰래 움직이다", `back in` 은 "다시 안으로". `so … can't …` 로 장치의 목적을 문장 끝에 둔다. 노트의 `slip past (a check)` 가 검사를 빠져나가는 쪽이라면 이쪽은 없앤 것이 되돌아오는 쪽이다.
- 예문: If the model adds `### Inferred` or any other `###` section anyway, it counts as `llm_failed`, so guesses can't slip back in.
- 유사어: creep back in (서서히, 구어), sneak back in (몰래, 구어), reappear unnoticed (격식)
- 반의어: stay out (계속 배제되다)

## "go the other way"
- 레지스터: conversational
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 경계 사례의 판정 결과를 보여 주고 반대로 처리할 게 있으면 알려 달라고 할 때(검토 요청).
- 한국어: 반대쪽으로 판정되다
- 설명: `go` 가 "(판정·결과가) 어느 쪽으로 나다". `The vote could go either way.` 의 그 `go`. 원문은 제외·유지 표를 보인 뒤 이 한 문장으로 최종 판단을 사용자에게 넘긴다. 노트의 `the other way round`(순서가 거꾸로)와는 다르다.
- 예문: Tell me if any of those should go the other way.
- 유사어: be flipped (구어), be classified differently (격식), belong on the other list (평이)
- 반의어: stay as they are

## "the dangerous direction"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 오판 두 방향 가운데 어느 쪽이 더 위험한지 따져 판정 규칙을 한쪽으로 기울일 때(안전 설계).
- 한국어: 위험한 쪽의 오류
- 설명: 오류를 방향으로 보는 틀. 빈 칸을 사용 중으로 잘못 보면 교정을 건너뛸 뿐이지만 사용 중인 칸을 빈 칸으로 보면 남의 세션을 클릭하게 된다. 원문은 괄호 `(a click into a view-only session)` 로 피해를 구체적으로 적었다. 노트의 `the dangerous kind of wrong` 이 오류의 종류를 말한다면 이쪽은 두 방향 중 한쪽을 고른다.
- 예문: It does not filter by name shape, because a false free is the dangerous direction.
- 유사어: the costlier error (격식), fail safe toward X (공학), err on the side of caution (관용)
- 반의어: a safe failure (틀려도 해가 없는 쪽)

## "fight the prompt"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 프롬프트 문구를 계속 고쳐 모델을 설득하는 대신 코드 쪽에서 보정하겠다고 방향을 틀 때(LLM 작업 대화).
- 한국어: 프롬프트와 씨름하다
- 설명: `fight` 가 "씨름하다". `rather than + 동사원형` 으로 버리는 선택지를 앞에 둔다. `again` 에는 이미 몇 번 씨름했다는 피로감이 묻어 있다.
- 예문: Rather than fight the prompt again, I'll add an origin shift, default one button up per your observation.
- 유사어: wrestle with the prompt (구어), keep tweaking the wording (평이), prompt-engineer our way out (구어, 살짝 비꼼)
- 반의어: work around it in code (코드로 우회하다)

## "break on refactors"
- 레지스터: technical
- 출처: transcript:[assistant] equipment-data-map
- 맥락: 구현 세부를 그대로 흉내 낸 테스트 대역이 리팩터링 때마다 깨진다고 경고할 때(테스트 설계).
- 한국어: 리팩터링할 때마다 깨지다
- 설명: `break on X` 는 "X 가 일어날 때 깨지다". 원문 `Doubles that mirror an implementation detail break on refactors` 는 관계절 `that mirror …` 가 주어를 꾸미고 동사 `break` 가 한참 뒤에 온다. 주어가 길어도 동사 수 일치(`Doubles … break`)를 놓치지 않는다.
- 예문: Doubles that mirror an implementation detail break on refactors; a no-op `close()` is the smaller contract.
- 유사어: are brittle (평이), couple tests to the implementation (격식·공학), fall over whenever the code moves (구어)
- 반의어: survive refactors / test behavior, not implementation

## "a contract with the screen, not a description"
- 레지스터: technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 프롬프트 속 이름 하나가 설명이 아니라 모델이 그대로 따르는 약속이라서 틀리면 틀린 결과가 확신 있게 나온다고 짚을 때(LLM 설계 글).
- 한국어: 설명이 아니라 화면과 맺은 계약
- 설명: `A, not B` 대비로 이름의 성격을 다시 정의한다. 원문은 `so the wrong name yields a confidently wrong crop` 으로 결과까지 잇는다. 동사 `yield` 는 "(결과를) 낳다"로 글에서 쓰는 격식어다.
- 예문: Column names in prompts are contracts with the screen, not descriptions, so the wrong name yields a confidently wrong crop.
- 유사어: The prompt is a spec, not a hint. (구어), Treat labels as an interface. (격식)
- 반의어: a loose description (대충 적은 설명)
