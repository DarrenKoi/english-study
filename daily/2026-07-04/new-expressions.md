# 2026-07-04 — 새 표현

오늘 배치는 auto_recipe_creator 의 zoom-ladder / PM-dropdown 디버깅 세션과 코드리뷰·문서 정리
트랜스크립트가 중심. 디버깅 결론·리뷰 판정·회고에서 쓰는 표현이 많이 나왔다.

## "a dead end"
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator (zoom-ladder 세션) — "The wheel ladder becomes a dead end for mag, so we pivot to driving the PM dropdown."
- 맥락: 어떤 접근이 더 가봐야 성과가 없는 "막다른 길"임을 선언하고 방향 전환을 정당화할 때(회의·구어 모두)
- 한국어: 막다른 길, 더 가봐야 소용없는 접근
- 설명: 물리적 막다른 골목에서 온 비유. `hit a dead end`(막다른 길에 부딪히다), `a dead end for X`(X에 관해서는 막다른 길) 형태로 쓴다. 방향 전환(pivot)과 짝으로 자주 등장.
- 예문: The wheel approach turned out to be a dead end on this tool, so we pivoted to the PM-button dropdown.
- 유사어: hit a wall (부딪힌 순간을 강조; dead end 는 길 자체가 끝났다는 판정), a blind alley (같은 뜻, 약간 문어), the X axis is exhausted (기수집 — 더 격식, 개선 여지 소진)
- 반의어: a promising avenue (가능성 있는 경로)

## "hold off (on X)"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator — "You said 'commit', so I held off on the push — just say the word."
- 맥락: 할 수는 있지만 신호가 올 때까지 일부러 미루고 있다고 말할 때(동료 간 협업 구어)
- 한국어: (지시가 있을 때까지) 보류하다, 미뤄 두다
- 설명: `postpone`/`defer` 의 구어체. "안 한다"가 아니라 "기다리는 중"이라는 뉘앙스가 핵심. `hold off on + 명사/동명사`.
- 예문: I held off on the push until you confirmed the commit message.
- 유사어: put (it) on hold (좀 더 격식·중립), defer (문어·격식 — deferred deliberately 로 기수집), sit on it (구어, 다소 소극적 뉘앙스)
- 반의어: go ahead with (바로 진행하다)

## "slot into (the same lifecycle)"
- 레지스터: technical, professional
- 출처: transcript:auto_recipe_creator — "A wheel-down probe slots into the exact same lifecycle, no restructuring needed."
- 맥락: 새 기능이 기존 구조를 고치지 않고 제자리에 딱 끼워진다고 설계 근거를 댈 때(설계 리뷰·문어)
- 한국어: (기존 구조의) 빈자리에 딱 들어맞다
- 설명: slot(홈, 슬롯)에서 온 동사. 구조 변경 없이 자연스럽게 편입된다는 뉘앙스라 "저비용 변경" 논거로 강력하다. `slot into place` 도 흔함.
- 예문: The new probe slots into the same lifecycle as the reposition preview, so no restructuring is needed.
- 유사어: fit neatly into (중립), drop into (더 구어, 마찰 없음 강조), plug into (인터페이스 결합 뉘앙스)
- 반의어: require restructuring / bolt on (기수집 — 억지로 덧붙이다)

## "quietly expensive"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (CLAUDE.md 감사) — "CLAUDE.md currency bugs are quietly expensive: they misdirect work, not just confuse."
- 맥락: 눈에 띄는 장애는 아니지만 몰래 비용을 누적시키는 문제를 지적할 때(문서·리뷰, 격식)
- 한국어: 티 안 나게 비싼, 소리 없이 비용을 누적시키는
- 설명: `quietly + 형용사` 패턴(quietly broken, quietly wrong). 시끄럽게 터지는 장애(loud failure)와 대비해, 경고 없이 잘못된 방향으로 일을 유도하는 비용을 부각한다.
- 예문: Stale docs are quietly expensive — they misdirect future work instead of failing loudly.
- 유사어: silently costly (거의 동의), insidious (더 강한 부정, "은밀히 해로운"), a hidden cost (명사형)
- 반의어: fail loudly / a loud failure (요란하게 드러나는 실패)

## "a confound"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator (A/B 리뷰) — "If the ensemble call omitted `scales=COMPARE_SCALES` it would default to DEFAULT_SCALES — a confound."
- 맥락: 실험(A/B)에서 비교하려는 변수 외에 결과를 오염시키는 교란 변수를 지적할 때(통계·실험 설계, 문어)
- 한국어: 교란 변수 (실험 결과를 오염시키는 제3의 차이)
- 설명: 통계 용어 confounding variable 의 명사형 축약. 동사 `confound`(뒤섞어 혼란시키다)도 쓴다. A/B 공정성(fairness) 논의에서 "그 차이 때문에 비교가 무효"라고 못 박는 단어.
- 예문: Letting the two runners use different scale bands would be a confound — the delta would no longer isolate the new channels.
- 유사어: a confounding variable (풀어 쓴 정식 용어), a lurking variable (통계 교과서 표현), apples-to-oranges (구어 비유 — 비교 불가)
- 반의어: a controlled comparison (교란이 통제된 비교)

## "rule out"
- 레지스터: professional, conversational
- 출처: transcript:auto_recipe_creator — "I think it's here, but I can't rule out that identical-looking place 20 µm over."
- 맥락: 후보·가설을 "아닌 것으로 배제"할 때. 진단·디버깅에서 "배제 못 하면 확정도 못 한다"는 논리로 자주 씀(구어·문어 공용)
- 한국어: (가능성을) 배제하다
- 설명: 의학 진단에서 일상까지 널리 쓰는 구동사. 부정형 `can't rule out`(배제할 수 없다)이 특히 유용 — 단정을 피하면서 불확실성을 정직하게 남긴다.
- 예문: Let me re-read the committed code to rule out a real bug before assuming it's a config issue.
- 유사어: eliminate (더 격식·단정적), exclude (문어), dismiss (검토 없이 물리치는 뉘앙스라 주의)
- 반의어: confirm / rule in (의학에서 실제로 씀)

## "X is the whole story"
- 레지스터: conversational
- 출처: transcript:auto_recipe_creator — "`2nd/best=0.994` is the whole story — the score surface is flat."
- 맥락: 여러 숫자·요인 중 "사실상 이것 하나가 전부"라고 핵심을 콕 집을 때(구어, 설명 대화)
- 한국어: 이게 사실상 전부다, 핵심은 이 하나다
- 설명: 복잡해 보이는 상황을 한 요인으로 환원하는 구어 문형. 같은 대화의 "the real culprit"(진범)과 짝 — culprit 은 부정적 원인, whole story 는 중립적 설명 전부.
- 예문: The second-ratio of 0.994 is the whole story: two spots match almost identically, so the engine refuses to commit.
- 유사어: the real culprit (원인 규명 뉘앙스), that's the crux (기수집 — 더 격식), it boils down to X (환원 과정 강조)
- 반의어: only part of the picture (전체 중 일부일 뿐)

## "fight the (repo's own) convention"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator — "Gitignoring a folder literally named `docs/` also fights the repo's own convention."
- 맥락: 어떤 선택이 기존 관례와 어긋나 마찰을 일으킨다고 반대 근거를 댈 때(설계 논의·문어)
- 한국어: (기존) 관례와 싸우다 = 관례를 거스르다
- 설명: fight 를 "규칙과 싸우다"로 은유 확장. `fight the framework`, `don't fight the platform` 처럼 도구·관례를 거스르는 설계를 경고하는 관용 패턴.
- 예문: A gitignored folder named `docs/` would silently fight the repo's own convention that docs are tracked.
- 유사어: go against the grain (일반 관용구), break with convention (더 중립 — 의도적 이탈), cut against (문어)
- 반의어: follow / lean into the convention (관례에 올라타다)

## "actionable, not aspirational"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (CLAUDE.md 감사) — "I named the canonical entry files so the flow is actionable, not aspirational."
- 맥락: 문서·계획이 "바로 실행 가능한 수준"인지 "희망사항 수준"인지 대비할 때(문서 품질 평가, 격식)
- 한국어: (희망사항이 아니라) 바로 실행 가능한
- 설명: 두 형용사의 두운(a-)까지 맞춘 대구 표현. aspirational 은 "지향점일 뿐 실체가 없는"이라는 완곡한 비판으로, 기획 문서 리뷰에서 자주 쓰인다.
- 예문: Name the exact entry files in the doc so the workflow is actionable, not aspirational.
- 유사어: concrete vs vague (평이한 대비), executable (기계적 뉘앙스), copy-paste ready (명령어에 한정)
- 반의어: aspirational / hand-wavy (기수집)

## "moot (make X moot)"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (NCC 리뷰) — "A/B presumably never produced a None NCC ... making `None` moot there but production-safe here."
- 맥락: 어떤 우려·논점이 조건 변화로 "따질 실익이 없어졌다"고 정리할 때(리뷰·법률 유래, 격식)
- 한국어: 논의할 실익이 없는, 이미 무의미해진 (논점)
- 설명: 법률 용어(moot case: 판결해도 실효 없는 사건)에서 온 형용사. `a moot point` 가 대표 꼴이고, `make X moot`(X를 무의미하게 만들다)로 동사구처럼 활용. 결함이 "있지만 안 터진다"는 inert in practice(기수집)와 비슷하되 moot 은 "논쟁 자체가 무의미"에 초점.
- 예문: The out-of-bounds candidates are filtered earlier, which makes the None-handling question moot in the A/B run.
- 유사어: inert in practice (기수집 — 결함이 실전에서 안 터짐), academic (이론상의 논쟁일 뿐), beside the point (초점 밖)
- 반의어: a live issue (여전히 유효한 쟁점)

## "office-blind / fix (it) blind"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator — "Office-blind Windows runtime"; "Three findings I deliberately did not fix blind."
- 맥락: 대상 환경을 직접 볼 수 없는 채로 작업한다고 제약을 명시할 때(원격 디버깅·협업)
- 한국어: (환경을) 못 보는 채로, 깜깜이로
- 설명: blind 를 부사처럼 붙여 "확인 수단 없이"를 표현. `fly blind`(계기 없이 비행하다)가 원형이고, `office-blind` 처럼 `X-blind` 합성어로도 만든다. "fix blind = 실물 확인 없이 고치다"는 위험 신호로 쓰인다.
- 예문: I deliberately didn't fix those three findings blind — they need the first office run's logs to calibrate.
- 유사어: fly blind (관용구 원형), sight unseen (실물 안 보고 — 구매 맥락), in the dark (정보 부재 일반)
- 반의어: with eyes on (the target) / verified against real data

## "sweep up (unrelated WIP)"
- 레지스터: technical, conversational
- 출처: transcript:auto_recipe_creator — "Let me inspect that file's diff so I don't sweep up unrelated WIP into this docs commit."
- 맥락: 커밋·변경에 의도치 않은 것까지 쓸려 들어가는 상황을 경계할 때(git 워크플로 대화)
- 한국어: (빗자루로 쓸듯) 무관한 것까지 휩쓸어 담다
- 설명: sweep(쓸다)의 비유. 커밋 범위 오염을 묘사하는 생생한 동사로, `git add -A` 의 위험을 말할 때 딱 맞는다. 수동형 `get swept up in` 은 "휘말리다"로 더 일반적.
- 예문: Stage only the files you touched, or you'll sweep up someone else's WIP into your commit.
- 유사어: drag in (끌어들이다), scoop up (퍼 담다 — 더 구어), stack on top of (기존 변경 위에 쌓이다)
- 반의어: keep the commit surgical (기수집 — 정밀하게 최소 범위로)

## "a judgment-heavy pass"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator (/batch 판단) — "This isn't a uniform migration — it's a judgment-heavy pass."
- 맥락: 기계적 일괄 처리가 아니라 건건이 판단이 필요한 작업임을 규정해, 자동화·병렬화가 부적합하다고 논증할 때(계획 수립, 격식)
- 한국어: 판단이 많이 개입되는 (일괄 아닌) 작업
- 설명: `X-heavy` 합성 패턴(compute-heavy, text-heavy)의 응용. pass 는 "한 차례 훑는 작업"이라는 소프트웨어 관용 명사. "judgment-heavy → 한 사람이 일관되게" 라는 결정 근거로 이어진다.
- 예문: It's a judgment-heavy pass over twenty files, so a single careful session beats a fan-out of isolated agents.
- 유사어: case-by-case (건별 판단), nuanced (미묘한 차이가 많은), discretionary (재량이 필요한 — 격식)
- 반의어: mechanical / a uniform migration (기계적 일괄 변경)

## "before declaring done"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator — "A too-clever exclusion filter can hide real hits, so always re-scan unfiltered before declaring done."
- 맥락: 완료 선언 전 최종 검증 절차를 규범으로 말할 때(회고·체크리스트, 문어)
- 한국어: "다 했다"고 선언하기 전에
- 설명: `declare + 형용사` 구문(declare it done/safe/dead). 완료는 사실이 아니라 *선언*이라는 뉘앙스가 있어, 선언 전 검증 의무를 자연스럽게 요구한다. 같은 문장의 `too-clever`(과하게 영리한 = 부작용을 낳는)도 함께 익혀두면 좋다.
- 예문: Re-run the full grep unfiltered before declaring the migration done.
- 유사어: before calling it done (더 구어), before signing off (승인 뉘앙스), verification before completion (절차명 느낌)
- 반의어: declare victory prematurely (성급한 완료 선언)
