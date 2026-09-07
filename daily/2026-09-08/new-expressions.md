# 2026-09-08 — 새 표현

오늘 재료는 트랜스크립트 10개뿐이다. repo 문서도 spool 노트도 없어서, 영어는 전부
에이전트 보고문과 내가 에이전트에게 던진 영어 지시문에서 나왔다.

## "where git does not reach"
- 레지스터: professional
- 출처: transcript:auto_recipe_creator ff8357d4 (VLM 서비스 변경 점검)
- 맥락: 확인해야 할 일이 코드 밖·다른 기계에 있다고 선을 그을 때(보고·격식)
- 한국어: git 이 닿지 않는 곳
- 설명: 관계부사 `where` 로 장소를 수식하는데, 그 장소가 물리적 사무실 PC 이면서 동시에
  "버전관리 밖"이라는 뜻을 겹쳐 담는다. `not in the repo` 라고 쓰면 사실만 남지만
  `where git does not reach` 는 "그래서 내가 여기서 확인해 줄 수 없다"까지 함께 전달한다.
- 예문: The remaining checks are all on the office PC, where git does not reach.
- 유사어: outside version control (중립·건조), off the repo (구어), beyond what I can verify from here (더 길고 조심스러움)
- 반의어: tracked in git

## "which is expected, not a regression"
- 레지스터: professional, technical
- 출처: transcript:auto_recipe_creator ff8357d4
- 맥락: 실패가 뜨는 게 정상이라고 미리 못 박을 때(리뷰·인수인계)
- 한국어: 그건 예상된 것이지 퇴행이 아니다
- 설명: 앞 절 전체를 받는 계속적 용법 `which` 뒤에 `A, not B` 대구를 붙였다. 실패를 숨기지
  않으면서 "고칠 것 없음"으로 분류하는 판정구다. `regression` 은 "전에 되던 게 안 된다"는
  좁은 뜻이라, 이 단어를 골라야 "원래부터 안 되던 것"과 갈린다.
- 예문: It will report those as failures, which is expected, not a regression.
- 유사어: that's by design (더 단정적), known and harmless (심각도까지 붙임), a false positive (원인이 검사 쪽일 때만)
- 반의어: that's a genuine regression

## "Each needs its situation to occur."
- 레지스터: conversational, professional
- 출처: transcript:auto_recipe_creator ff8357d4
- 맥락: 왜 아직 검증 못 했는지 변명 없이 설명할 때(진행 보고·구어에 가까운 격식)
- 한국어: 각각은 그 상황이 실제로 일어나야 확인된다
- 설명: `need + 목적어 + to부정사` 로 "상황이 발생하는 것"을 필요조건 자리에 놓는다. 주어를
  사람이 아니라 `each`(그 항목들)로 두면 게으름이 아니라 성질 때문이라는 그림이 된다.
  테스트 못 한 항목을 나열한 뒤 마지막에 붙이는 문장.
- 예문: OK button, occupied popup and the abort button are still unexercised — each needs its situation to occur.
- 유사어: can only be checked when it actually happens (풀어쓴 회화체), not reproducible on demand (더 기술적)
- 반의어: I can trigger it whenever I want

## "still unexercised"
- 레지스터: technical
- 출처: transcript:auto_recipe_creator ff8357d4
- 맥락: 코드 경로가 한 번도 실행되지 않았다고 적을 때(테스트 현황·격식)
- 한국어: 아직 한 번도 실행되지 않은
- 설명: `exercise` 는 테스트 문맥에서 "코드를 실제로 돌려 본다"는 뜻이고, `un-` + 과거분사로
  그 부정을 만든다. `untested` 는 "테스트를 안 썼다"로도 읽히지만 `unexercised` 는
  "테스트는 있는데 그 경로를 아직 안 밟았다"까지 정확히 가른다.
- 예문: Four branches are still unexercised on mai-ui regardless of the service change.
- 유사어: never hit in practice (구어), has no coverage (지표 이야기로 옮겨감), dead in the current profile (더 강함)
- 반의어: covered / exercised by the suite

## "Undo: set that key back to `false`."
- 레지스터: conversational, technical
- 출처: transcript:llm_serving 4a62ec10 (auto-update 설정 변경)
- 맥락: 설정을 바꿔 준 직후 되돌리는 법을 한 줄로 남길 때(도구·안내문)
- 한국어: 되돌리려면: 그 키를 다시 `false` 로 두세요
- 설명: `Undo:` 를 라벨처럼 앞에 세우고 명령문을 붙이는 관례. `If you want to revert this,
  you can ...` 같은 긴 조건절을 라벨 한 단어로 압축한다. 변경 보고 끝에 붙이면 상대가
  결정을 되물릴 여지를 명시적으로 남기는 효과가 있다.
- 예문: Undo: set that key back to `false`, or run `claude config set autoUpdates false`.
- 유사어: To revert: … (더 격식), Roll it back with … (구어·능동)
- 반의어: This change is one-way.

## "byte for byte"
- 레지스터: technical, professional
- 출처: transcript:equipment_data_map de6f3de9 (spec.md 스냅샷 검증)
- 맥락: 두 파일이 완전히 같음을 주장할 때(검증 보고·격식)
- 한국어: 한 바이트도 다르지 않게
- 설명: 전치사 `for` 로 같은 명사를 반복해 "하나씩 대응해서"라는 부사구를 만드는 틀
  (`word for word`, `line for line` 과 같은 계열). `identical` 만 쓰면 "내용이 같다"로
  느슨하게 읽히는데, `byte for byte` 는 그 판정이 기계적 비교였음까지 함께 말한다.
- 예문: Before this batch, `spec.md` matched the architecture doc byte for byte.
- 유사어: word for word (텍스트 한정), an exact copy (더 평이함), bit-for-bit identical (더 강함)
- 반의어: equivalent but reformatted

## "recommend, don't just offer"
- 레지스터: professional
- 출처: transcript:llm_serving 4a62ec10 (Claude Code Doctor 지침)
- 맥락: 선택지만 늘어놓지 말고 의견을 내라고 요구할 때(지시문·설계 근거)
- 한국어: 권해라, 선택지만 던지지 말고
- 설명: 명령문 두 개를 쉼표로 붙인 `A, don't just B` 대구. `just` 하나가 "offer 가 나쁘다"가
  아니라 "offer 에서 멈추는 게 문제다"로 뜻을 좁힌다. 회의에서 "그래서 뭘 하자는 건데?"를
  덜 무례하게 말하는 방식이기도 하다.
- 예문: Propose, then confirm, then apply — and recommend, don't just offer.
- 유사어: take a position (더 강함), tell me which one you'd pick (구어), state a preference (완곡)
- 반의어: lay out the options and let me decide

## "silently widen permission posture"
- 레지스터: professional, technical
- 출처: transcript:llm_serving 4a62ec10
- 맥락: 동의 범위를 넘어선 권한 확대를 경계할 때(보안·설계 격식)
- 한국어: 권한 태세를 소리 없이 넓히다
- 설명: `posture` 는 보안 문맥에서 "지금 어떤 자세로 서 있는가", 즉 방어·허용 수준 전체를
  가리킨다. `widen` 이 그 범위를 넓히는 동사고, `silently` 가 "당사자 모르게"를 얹는다.
  세 단어가 붙어 "정리에 동의한 사람이 권한 확대까지 동의한 것으로 취급되면 안 된다"는
  주장을 한 구로 만든다.
- 예문: A user consenting to decluttering must not silently widen their permission posture.
- 유사어: quietly expand what runs without asking (풀어쓴 형태), grant more than was asked for (평이함)
- 반의어: keep the permission surface unchanged

## "Add the fewest letters needed."
- 레지스터: professional
- 출처: transcript:equipment_data_map de6f3de9 (내가 쓴 지시문)
- 맥락: 산출물을 늘리지 말라고 상한을 걸 때(작업 지시·격식)
- 한국어: 필요한 최소 개수만 추가해라
- 설명: 최상급 `fewest` 뒤에 과거분사 `needed` 가 명사를 뒤에서 수식한다(`the fewest X
  needed` = 필요한 최소한의 X). `Don't add too many` 같은 부정 명령보다 판단 기준을 상대에게
  넘겨주면서도 방향은 분명하다. `Keep changes minimal` 과 짝으로 자주 쓴다.
- 예문: Add the fewest letters needed; extending numbering is fine.
- 유사어: keep additions to a minimum (더 평이), only add what you must (구어)
- 반의어: cover every case up front

## "the id is theirs to choose"
- 레지스터: professional, conversational
- 출처: transcript:equipment_data_map de6f3de9
- 맥락: 검색에 걸린 항목이 문제가 아닌 이유를 댈 때(리뷰 응답)
- 한국어: 그 id 는 그 사람이 정할 몫이다
- 설명: `be + 소유대명사 + to부정사` 로 "누구의 권한/책임인가"를 한 구에 담는 틀
  (`the call is yours to make`, `that's his to decide`). 검사에서 나온 한 건을 기각하면서
  규칙 자체는 살려 두는 데 쓰인다 — 예외가 아니라 애초에 대상이 아니었다는 논리.
- 예문: One hit, the engineer's own `init` step, where the id is theirs to choose.
- 유사어: that's their call (구어), left to the operator by design (격식·수동)
- 반의어: the tool assigns it

## "best-known defaults"
- 레지스터: professional
- 출처: transcript:equipment_data_map de6f3de9
- 맥락: 지금 아는 최선의 값이지만 확정은 아니라고 표시할 때(미결 사항 보고)
- 한국어: 현재 아는 한 가장 정확한 기본값(확정 아님)
- 설명: 하이픈으로 `best-known` 을 한 덩어리 형용사로 묶었다. "가장 잘 알려진"이 아니라
  "우리가 아는 것 중 최선"이라는 뜻이고, 뒤에 `confirm them before …` 이 붙어야 완성된다.
  값을 비워 두지도 않고 사실로 단정하지도 않는 중간 지점을 만드는 장치.
- 예문: Letter 14 states the four skill discovery roots as best-known defaults; confirm them before the installer is built.
- 유사어: a working assumption (더 임시적), our current understanding (격식·완곡), placeholder values (확신이 더 낮음)
- 반의어: confirmed values

## "cost context but never get used"
- 레지스터: professional, technical
- 출처: transcript:llm_serving 4a62ec10
- 맥락: 유지 비용만 있고 쓰임이 없는 것을 정리 대상으로 지목할 때(감사·구어에 가까운 격식)
- 한국어: 컨텍스트만 잡아먹고 정작 쓰이지는 않는
- 설명: `cost` 를 타동사로 써서 목적어에 자원(`context`)을 바로 놓는다 — `cost me an hour`
  와 같은 용법이다. 뒤에 `but never get used` 를 붙여 비용과 효용을 한 문장 안에서 맞세우면,
  삭제 근거가 따로 필요 없어진다.
- 예문: Find extensions that cost context but never get used.
- 유사어: pure overhead (더 단정적), earn their keep (반대편 표현), dead weight (구어·평가적)
- 반의어: pays for itself

## "an injectable test seam"
- 레지스터: technical
- 출처: transcript:equipment_data_map de6f3de9
- 맥락: 테스트를 위해 구현을 갈아끼울 지점을 요구할 때(설계 지시·격식)
- 한국어: 테스트에서 갈아끼울 수 있는 이음매
- 설명: `seam` 은 옷의 솔기에서 온 말로, "여기서 갈라 다른 것을 끼울 수 있는 경계"를 뜻한다.
  `injectable` 이 그 경계로 대체 구현을 주입할 수 있음을 못 박는다. `mock` 은 끼워 넣는
  물건이고 `seam` 은 끼울 자리라, 설계를 요구할 때는 자리 쪽 단어를 써야 말이 맞는다.
- 예문: OS keystore lookup has no explicit supported backend or test seam.
- 유사어: a seam for injection (같은 뜻·어순만 다름), a swappable backend (구현 쪽에서 본 표현), a hook point (더 느슨함)
- 반의어: hard-wired to the real implementation

## "bounded status output"
- 레지스터: technical
- 출처: transcript:equipment_data_map de6f3de9
- 맥락: 출력 항목이 허용 목록으로 묶여 있음을 규정할 때(계약 명세·격식)
- 한국어: 항목이 미리 정해진 범위로 묶인 상태 출력
- 설명: 여기서 `bounded` 는 "양이 적다"가 아니라 "무엇이 나올 수 있는지 목록이 닫혀 있다"는
  뜻이다. 그래서 뒤에 무엇이 새어 나가면 안 되는지가 따라붙는다. 크기 상한을 말하는
  `bounded memory` 와 같은 단어지만 묶는 대상이 다르다.
- 예문: Make `status` expose the report's existence and hash as bounded status output.
- 유사어: a fixed allowlist of fields (더 구체적), a closed output contract (격식)
- 반의어: free-form output / whatever the model decides to print

## "invisible to git tooling"
- 레지스터: technical
- 출처: transcript:skewnono_v3_nuxt 23a9b296 (worktree 정리)
- 맥락: 왜 표준 명령으로는 안 잡히는지 설명할 때(진단 보고)
- 한국어: git 도구로는 아예 보이지 않는
- 설명: `invisible to X` 는 "X 의 관점에서는 존재하지 않는다"는 뜻이고, 뒤에 대안 관측 방법이
  따라와야 실용적인 문장이 된다. 여기서는 `has to be found by looking at the filesystem`
  이 그 짝이다. 버그가 아니라 도구의 관할 밖이라는 판정이라 비난의 색이 없다.
- 예문: An orphan like this is invisible to git tooling and has to be found by looking at the filesystem.
- 유사어: outside the tool's view (더 평이), not something the command knows about (구어)
- 반의어: shows up in `git worktree list`
