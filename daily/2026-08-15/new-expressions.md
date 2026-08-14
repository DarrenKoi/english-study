# 2026-08-15 — 새 표현

## "root and branch"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/80f800fe
- 맥락: 흔적까지 남김없이 제거했다고 선언할 때(구어~격식 양쪽. 원래 정치 개혁 구호)
- 한국어: 뿌리째, 가지까지 — 완전히
- 설명: 부사구로 문장 끝에 붙는다. "지웠다"에 강도를 얹는 관용구라 `deleted`, `removed` 같은 동사 뒤가 자리다. 부분 삭제와 대비될 때만 값이 있어서, 흔적이 남았을 가능성이 있으면 쓰지 않는다.
- 예문: OpenWiki is gone, root and branch.
- 유사어: completely (밋밋하고 안전), lock, stock and barrel (같은 계열 관용구지만 "일습 전부" 쪽), for good (완전히 + 영구히)
- 반의어: partially removed

## "a conflict minefield"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 병합·리베이스가 충돌 지뢰밭이 될 뻔했다고 회고할 때(개발자 간 구어~문어)
- 한국어: 충돌 지뢰밭
- 설명: `rather than` 과 짝지어 "안전했다 vs 지뢰밭이었다"의 대비로 굴린다. 지뢰는 밟기 전엔 안 보인다는 함의라, 예측 못 한 충돌이 줄줄이 터지는 상황에 맞다.
- 예문: That's why the rebase was safe rather than a conflict minefield.
- 유사어: a can of worms (열면 곤란해지는 쪽 강조), a mess (범용·구어), painful merge (밋밋)
- 반의어: a clean rebase

## "first writer wins"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/77cbf038
- 맥락: 여러 설정 소스가 겹칠 때 우선순위 규칙을 한 줄로 못 박을 때(코드 리뷰·설계 문서)
- 한국어: 먼저 쓴 쪽이 이긴다
- 설명: 주어 없이 통째로 명사절처럼 던지는 규칙 표현. `setdefault` 처럼 "이미 값이 있으면 건드리지 않는" 의미론을 설명할 때 정확히 들어맞는다. 반대 규칙은 `last writer wins` 로, 두 개가 한 쌍으로 통용된다.
- 예문: Both use setdefault, so first writer wins — the entry point beats your file.
- 유사어: earliest binding takes precedence (격식), the first assignment sticks
- 반의어: last writer wins

## "grouped by concern rather than as one mixed blob"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 커밋을 관심사별로 쪼갰다고 밝힐 때(PR 설명·작업 보고)
- 한국어: 한 덩어리로 뭉뚱그리지 않고 관심사별로 묶어서
- 설명: `blob` 은 형태 없는 덩어리라 "정리 안 된 뭉치"를 낮잡아 부르는 말이다. `by concern` 은 separation of concerns 에서 온 표현이라 커밋·모듈·파일 어디에나 붙는다.
- 예문: Four commits landed, grouped by concern rather than as one mixed blob.
- 유사어: one logical change per commit (규범적·격식), atomic commits
- 반의어: a single catch-all commit

## "it looked worse than it was"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 놀랄 만한 상황을 보고하되 실제로는 심각하지 않았다고 먼저 안심시킬 때(구어에 가까운 보고)
- 한국어: 보기보다는 별일 아니었다
- 설명: 과거형 두 개를 붙여 "겉보기 vs 실제"를 대비시킨다. 상대가 로그나 경고를 이미 봤을 때 첫 문장으로 놓으면 톤이 잡힌다. 현재 상황이면 `it looks worse than it is`.
- 예문: Worth knowing what happened, because it looked worse than it was.
- 유사어: it's less alarming than it sounds, nothing was actually broken
- 반의어: it was worse than it looked

## "this cuts against you"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/77cbf038
- 맥락: 방금 칭찬한 설계가 하필 오늘의 상황에는 불리하게 작용한다고 짚을 때(설계 논의)
- 한국어: 이번엔 그게 당신에게 불리하게 작용한다
- 설명: `cut against` 은 "~에 반대 방향으로 작용하다". 장점을 설명한 직후 `Note this cuts against you today` 처럼 뒤집는 자리에 놓여, 균형 잡힌 조언처럼 읽히게 만든다.
- 예문: Note this cuts against you today: that default pins `CORRECTION_DRY_RUN=0`.
- 유사어: works against you here, is a liability in this case (격식)
- 반의어: this works in your favor

## "silently neuter a production run"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/77cbf038
- 맥락: 남아 있던 설정 하나가 실제 운영 실행을 무력화하는 사고를 경고할 때(설계 근거·문서)
- 한국어: 운영 실행을 조용히 거세해 버리다
- 설명: `neuter` 는 "기능을 잃게 만들다"라는 강한 어휘라 경고문에서만 쓴다. `silently` 와 붙어 "오류도 안 나고 그냥 아무 일도 안 하게 된다"는 최악의 실패 방식을 가리킨다.
- 예문: A stale `CORRECTION_DRY_RUN=1` left in someone's scratch file must not silently neuter a production run.
- 유사어: quietly disable, render it a no-op (중립적·기술적), defang (같은 계열의 비유)
- 반의어: fail loudly

## "stale but harmless"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 낡은 값이 남은 걸 보고하되 고칠 필요는 없다고 등급을 매길 때(마무리 보고)
- 한국어: 낡았지만 해롭지는 않다
- 설명: 형용사 두 개를 `but` 으로 붙인 짧은 판정구. 발견을 숨기지 않으면서 우선순위를 낮추는 자리에 쓴다. 뒤에 `— say the word if you want it corrected` 같은 선택지를 붙이는 게 관례다.
- 예문: It's a provenance stamp for the wiki generator, so it's stale but harmless.
- 유사어: cosmetic (미관상 문제일 뿐), non-blocking, no functional impact (격식)
- 반의어: actively misleading

## "isolate exactly one variable"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/d5dd7c25
- 맥락: 실험을 어떻게 설계할지 권할 때(디버깅·검증 논의)
- 한국어: 변수를 딱 하나만 남기다
- 설명: 실험 설계의 기본을 그대로 개발 현장에 옮긴 말. `exactly` 가 핵심이라 빼면 힘이 빠진다. 뒤에 "그래야 나쁘게 나와도 뭘 탓할지 안다"가 따라오는 흐름이 정석이다.
- 예문: Same frames, same sidecar, new code — that isolates exactly one variable.
- 유사어: change one thing at a time (구어), a controlled comparison (격식)
- 반의어: change the input and the code at once

## "a record, not a live pointer"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/80f800fe
- 맥락: 옛 문서를 왜 안 고쳤는지 설명할 때(정리 작업 보고)
- 한국어: 살아 있는 참조가 아니라 그 시점의 기록
- 설명: `X, not Y` 대구로 판단 기준을 통째로 보여주는 형태. 날짜가 박힌 보고서는 낡아도 틀린 게 아니라는 논리라, 문서 정리에서 무엇을 남길지 가르는 잣대로 쓰인다.
- 예문: That deck describes the toolchain as it was then — a record, not a live pointer.
- 유사어: a historical snapshot, point-in-time documentation (격식)
- 반의어: a live reference that can go stale

## "in favor of"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 둘 중 하나를 버리고 다른 쪽을 택했다고 밝힐 때(격식 문어·커밋 메시지)
- 한국어: ~을 택하고 (~을 버리고)
- 설명: `discarded / dropped / deprecated A in favor of B` 형태로 굳어져 있다. 버린 쪽을 목적어로, 남긴 쪽을 `in favor of` 뒤에 두는 어순이 고정이라 뒤집으면 뜻이 반대가 된다.
- 예문: Your local duplicates were discarded in favor of the remote's versions.
- 유사어: replaced by (수동·중립), superseded by (격식), we went with B instead (회화)
- 반의어: kept A over B

## "horizontal slicing"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/5d7e71c1 (tdd 스킬)
- 맥락: 테스트를 몰아 쓰고 구현을 몰아 하는 안티패턴을 이름 붙일 때(방법론 문서)
- 한국어: 가로로 쪼개기 — 층별로 몰아서 하는 방식
- 설명: 안티패턴 이름이라 항상 부정적으로 쓴다. 대구인 `vertical slices` 가 함께 나와야 뜻이 선명해진다. 테스트뿐 아니라 "설계 전부 → 구현 전부" 같은 다른 층 분할에도 그대로 쓴다.
- 예문: Horizontal slicing — writing all tests first, then all implementation — verifies imagined behavior.
- 유사어: big-bang integration (통합 쪽 대응어), layer-by-layer development
- 반의어: vertical slices

## "tautological (test)"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/5d7e71c1 (tdd 스킬)
- 맥락: 코드와 같은 계산을 반복해 절대 실패할 수 없는 테스트를 지적할 때(코드 리뷰)
- 한국어: 동어반복적인 (테스트)
- 설명: 논리학 용어를 그대로 빌려 왔다. 판정의 근거는 "구성상 통과한다(passes by construction)"이며, 처방은 "기대값을 독립된 출처에서 가져와라"로 이어진다.
- 예문: The assertion recomputes the expected value the way the code does, so the test is tautological and can never disagree with the code.
- 유사어: a self-fulfilling assertion, testing the implementation against itself
- 반의어: an independently derived expectation

## "take effect"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/77cbf038
- 맥락: 변경이 실제로 발효되는 시점을 못 박을 때(운영 안내·배포 공지)
- 한국어: 발효되다, 실제로 적용되다
- 설명: 무생물 주어를 그대로 쓰는 게 자연스럽다(`The deletion only takes effect …`). 조건절 `once it's pushed` 를 붙여 "아직은 아니다"를 함께 전달하는 게 이 표현의 실제 쓰임이다. 구어에서는 `it took` 만으로도 통한다.
- 예문: The deletion only takes effect once it's pushed — until then tonight's run still fires.
- 유사어: come into force (법령·격식), go live (배포 구어), kick in (완전 구어)
- 반의어: be ignored

## "patch-equivalent"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 해시는 다른데 변경 내용은 같은 커밋을 가리킬 때(git 진단)
- 한국어: 패치(변경 내용)가 동일한
- 설명: `identical` 이 아니라 `equivalent` 인 게 핵심이다 — 메타데이터는 다르고 diff 만 같다는 뜻. 하이픈 형용사라 명사 앞뒤 어디든 붙는다.
- 예문: `git cherry` confirms the two duplicate-titled local commits are patch-equivalent to the remote pair.
- 유사어: functionally identical (더 넓은 범위), the same change under a different hash (풀어쓴 형태)
- 반의어: near-identical but divergent

## "worth chasing"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/d5dd7c25
- 맥락: 지금 주제는 아니지만 따로 파볼 값은 있다고 표시할 때(디버깅 대화)
- 한국어: 따로 쫓아볼 만한
- 설명: `worth -ing` 틀에 `chase` 를 넣어 "추적할 가치"를 나타낸다. 버그·단서에 붙고, 이미 원인이 밝혀진 것에는 안 쓴다. 보통 `a separate bug worth chasing` 처럼 `separate` 와 붙어 범위를 잘라낸다.
- 예문: A meaningful slice of `vlm` means the join is dropping frames, which is a separate bug worth chasing.
- 유사어: worth digging into, deserves its own investigation (격식)
- 반의어: not worth the detour

## "characterization tests"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-flask-modules/e7a381ab
- 맥락: 남의 코드·벤더 사본의 현재 동작을 그대로 못 박는 테스트를 부를 때(테스트 설계 논의)
- 한국어: 특성화 테스트 — 현재 동작을 있는 그대로 기록하는 테스트
- 설명: "이렇게 동작해야 한다"가 아니라 "지금 이렇게 동작한다"를 남기는 테스트다. 그래서 목적어가 `records what it already does` 처럼 현재형 서술이 된다. 레거시·벤더 코드에 손댈 때의 표준 용어.
- 예문: The file calls itself characterization tests — it records what the vendored copy already does, so a future re-vendor can't silently change behavior.
- 유사어: golden master tests, regression guard (범위가 더 넓음)
- 반의어: specification tests

## "a discoverability decision, not a security one"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/49618803
- 맥락: 링크를 숨겨 둔 이유가 보안이 아니라 노출 정책임을 구분할 때(리뷰·설계 설명)
- 한국어: 보안이 아니라 발견 가능성에 대한 결정
- 설명: `an X decision, not a Y one` 틀이 통째로 재사용된다(`one` 이 `decision` 을 받는다). 뒤에 "그래서 이 변경은 전자만 건드리고 후자는 약화시키지 않는다"가 따라오면 설득이 완성된다.
- 예문: That's a discoverability decision, not a security one — this change touches the former without weakening the latter.
- 유사어: a UX call, not a policy one; a matter of exposure rather than access control (격식)
- 반의어: a hard security boundary

## "pop in late"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/49618803
- 맥락: 데이터가 늦게 도착해 UI 요소가 뒤늦게 튀어나오는 현상을 말할 때(프런트엔드 구어)
- 한국어: 뒤늦게 툭 튀어나오다
- 설명: `flash in` (잠깐 보였다 사라짐)과 짝으로 쓰여 두 방향의 깜빡임을 한 문장에 담는다. 원인 절(`Those render before … resolves`)이 앞에 오고 증상이 뒤에 오는 배치가 자연스럽다.
- 예문: Those render before `/activity/me` resolves, so an admin-conditional nav item would flash in or pop in late for every user.
- 유사어: appear with a delay (중립), layout shift (측정 가능한 현상 쪽)
- 반의어: settle before first paint

## "at zero equipment risk"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator/77cbf038
- 맥락: 얻는 것과 감수하는 위험을 한 문장에서 맞세울 때(운영 설정 제안)
- 한국어: 장비 위험은 전혀 없이
- 설명: `at zero X` 는 `at no cost` 계열의 전치사구로, 문장 끝에 붙여 대가를 0으로 못 박는다. 앞에 `gives you the maximum evidence` 같은 이득이 와야 대비가 산다.
- 예문: `CORRECTION=1` plus `CORRECTION_DRY_RUN=1` gives you the maximum evidence per alarm at zero equipment risk.
- 유사어: with no downside, without touching the hardware (구체적)
- 반의어: at the cost of a real click
