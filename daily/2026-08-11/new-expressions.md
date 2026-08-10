# 2026-08-11 — 새 표현

## "turn a cap into a stampede"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 보호 장치가 오히려 사고를 키운다고 설계 문서·리뷰에서 지적할 때(격식 있는 문어체)
- 한국어: 상한선이 도리어 폭주를 일으키다
- 설명: `cap`(상한)과 `stampede`(가축 떼가 우르르 몰리는 것)를 맞붙여, 부하를 묶으려던 장치가 걸리는 순간 무제한 경로를 여는 역설을 한 마디로 그린다. `turn A into B` 는 의도와 결과가 뒤집혔을 때 쓰기 좋은 틀이다.
- 예문: Releasing the whole panel at the exact moment the tool is saturated is what turns a cap into a stampede.
- 유사어: backfire (그냥 역효과가 났다는 중립적 서술), defeat its own purpose (목적을 스스로 무너뜨린다 — 더 격식), open the floodgates (막았던 것이 한꺼번에 터진다)
- 반의어: hold the line (상한이 제 역할을 해 부하를 붙잡아 두다)

## "wait out (a refusal)"
- 레지스터: technical, conversational
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 지금 실패한 것을 포기하지 않고 상황이 풀릴 때까지 버틸 때(구어·문어 둘 다)
- 한국어: (지나갈 때까지) 버티며 기다리다
- 설명: `out` 이 "끝날 때까지"를 뜻해서 단순한 `wait for` 와 다르다. 태풍·파업·거절처럼 **저절로 해소되는** 상태에 붙고, 회복될 리 없는 대상에는 안 쓴다.
- 예문: A refused POST is waited out rather than surfaced, because the slot frees up as soon as the job ahead of it finishes.
- 유사어: sit it out (더 구어적 — 아예 참여하지 않고 지나 보낸다), ride it out (풍파를 견뎌 낸다는 뉘앙스), hold off (내가 자발적으로 미룬다)
- 반의어: give up on it / bail out (기다리지 않고 포기하다)

## "slower and no lighter"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 어떤 대안이 비용만 늘고 이득은 0이라고 잘라 말할 때(설계 근거·코드 주석)
- 한국어: 더 느리기만 하고 가벼워지지도 않는
- 설명: `no + 비교급`은 "조금도 더 ~하지 않다"라는 강한 부정이라 `not lighter` 보다 단호하다. 여기서는 나쁜 쪽(slower)과 좋아지지 않은 쪽(no lighter)을 한 줄에 붙여, 그 대안이 어느 축으로도 못 이긴다는 걸 보인다.
- 예문: Without that re-read the waiters would simply take turns visiting the tool, which is slower and no lighter.
- 유사어: strictly worse (모든 축에서 열등 — 더 딱딱함), all cost and no benefit (비용만 있고 이득 없음 — 회의에서 쓰기 좋음)
- 반의어: a clear win on both counts (두 축 모두 이득)

## "park a thread on that key forever"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 자원이 풀리지 않고 영구히 묶이는 최악의 실패를 테스트 근거로 적을 때(코드 주석·격식)
- 한국어: 스레드를 그 키에 영구히 붙들어 두다
- 설명: `park` 는 차를 대듯 "쓰지도 않으면서 자리만 차지하게 둔다"는 그림이라 `block` 보다 낭비의 뉘앙스가 짙다. 사람에게도 쓴다 — `park the decision until Friday`.
- 예문: One tool error must not park a worker thread on that key forever.
- 유사어: tie up (자원을 묶다 — 가장 흔함), pin down (움직이지 못하게 고정), hold hostage (인질로 잡다 — 과장된 구어)
- 반의어: release it back to the pool (자원을 풀어 되돌려 주다)

## "judge's call"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-msr-image-followups-two-axis-review.md
- 맥락: 규칙만으로는 안 갈리니 결정권자가 정하라고 넘길 때(리뷰 코멘트·회의)
- 한국어: 판단하는 사람 재량입니다
- 설명: 스포츠 심판 은유. 자기 의견은 이미 말했고 **결론은 상대 몫**이라고 물러나는 표현이라, 지적을 남기면서도 강요하지 않는 리뷰 어투를 만든다. 관사 없이 `judge's call` 로 툭 끊어 쓰는 게 자연스럽다.
- 예문: Two occurrences of a one-liner — extraction is borderline; judge's call.
- 유사어: your call (더 구어·직접적), a matter of taste (취향 문제라 더 가볍게), at the reviewer's discretion (가장 격식 있는 문어체)
- 반의어: non-negotiable (재량의 여지가 없다)

## "borderline"
- 레지스터: professional, conversational
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-msr-image-followups-two-axis-review.md
- 맥락: 기준선 바로 위/아래라 어느 쪽으로도 볼 수 있다고 유보할 때
- 한국어: 애매한 경계선상의
- 설명: 형용사로도 부사처럼도 쓴다(`borderline rude`). 단정을 피하면서도 "무시할 정도는 아니다"를 함께 담아, 약한 지적을 정직하게 남기는 자리에 잘 맞는다.
- 예문: A shared helper would carry both, but with only two call sites the extraction is borderline.
- 유사어: marginal (계량적 — 수치가 기준에 겨우 닿음), arguable (논쟁의 여지가 있다), a gray area (영역 자체가 모호할 때)
- 반의어: clear-cut (딱 갈린다)

## "left stale"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-oc-skills-two-axis-review.md
- 맥락: 문서·표·캐시가 갱신 없이 방치돼 사실과 어긋났다고 지적할 때(리뷰 헤드라인)
- 한국어: 갱신 안 된 채 방치된
- 설명: `leave + 목적어 + 형용사`("~한 상태로 두다") 구문이라, 누가 안 고쳤다는 **부작위**를 겨눈다. `is stale`(그냥 낡았다)보다 책임 소재가 분명해 리뷰 지적문에서 자주 골라 쓴다.
- 예문: The "Project skills" table was left stale — the diff adds three skill directories and touches neither CLAUDE.md nor AGENTS.md.
- 유사어: out of date (가장 평이함), never updated (사실 서술로 더 직접적), has drifted (조금씩 어긋났다는 과정 강조)
- 반의어: kept current (계속 최신으로 유지되다)

## "reference, not restate"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-oc-skills-two-axis-review.md
- 맥락: 같은 근거가 여러 문서에 복사돼 있을 때 단일 출처로 모으라고 처방할 때(격식)
- 한국어: (다시 쓰지 말고) 가리키기만 해라
- 설명: 동사 둘을 `A, not B` 로 맞세워 처방을 한 호흡에 담는다. 리뷰에서 문제 진단과 해법을 따로 쓰지 않고 붙여 버리는 압축 어법이라, 짧은 코멘트에 특히 잘 맞는다.
- 예문: `models.md` is the designated home; the skills should reference, not restate.
- 유사어: link out to it instead (더 평이·구어), point to the single source of truth (SSOT 어휘를 쓰는 격식체), defer to X (X 에 판단을 맡기다)
- 반의어: duplicate the rationale in each file (근거를 파일마다 복제하다)

## "the tree it claims to list"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-oc-skills-two-axis-review.md
- 맥락: 문서가 스스로 내건 약속을 지키지 못한다고 짚을 때(리뷰·감사 보고)
- 한국어: 자기가 나열한다고 주장하는 그 트리
- 설명: `claim to + 동사원형`이 "실제로는 아닌데 그렇다고 내세운다"는 의심을 얹는다. 관계절 안에 그 의심을 넣으면 별도 문장 없이 "약속 ↔ 현실"의 어긋남이 드러난다.
- 예문: The documented index no longer matches the tree it claims to list.
- 유사어: what it purports to cover (더 격식·법률투), what it advertises (더 구어적·비꼼)
- 반의어: an index that actually matches the tree (약속과 현실이 일치하는)

## "predates the diff"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-oc-skills-two-axis-review.md
- 맥락: 지금 리뷰 중인 변경의 책임이 아니라 원래 있던 문제라고 선을 그을 때
- 한국어: 이 변경 이전부터 있던 문제다
- 설명: `pre-` + `date` 로 "~보다 시간상 앞선다"를 한 단어에 담아 `existed before` 보다 짧다. 지적은 남기되 작성자를 탓하지 않는 완충 장치로 리뷰에서 자주 쓴다.
- 예문: The coverage gap predates the diff — widen the glob or record the exclusion in CLAUDE.md.
- 유사어: pre-existing (형용사형으로 명사 앞에 붙일 때), not introduced here (가장 평이한 부정 서술), inherited (물려받은 것이라는 뉘앙스)
- 반의어: introduced by this change (이번 변경이 만들어 낸)

## "the criterion as written is unmet"
- 레지스터: professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-msr-image-followups-two-axis-review.md
- 맥락: 의도는 이해하지만 **문서에 적힌 문구 그대로**를 기준으로 삼겠다고 못박을 때(격식)
- 한국어: 문서에 적힌 대로의 기준은 충족되지 않았다
- 설명: `as written` 이 명사 뒤에 붙어 "해석이 아니라 문면 그대로"를 한정한다. 뒤의 `unmet` 은 수동태를 피한 형용사 술어라 담백하다 — `has not been met` 보다 단정적이다.
- 예문: Disclosed openly, but the criterion as written is unmet.
- 유사어: falls short of the stated bar (기준선 은유), does not satisfy the acceptance criterion (가장 격식), technically not met (`technically` 로 조금 물러섬)
- 반의어: satisfied to the letter (문면 그대로 충족됐다)

## "the premises check out"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-10-msr-image-followups-two-axis-review.md
- 맥락: 결론을 말하기 전에 전제부터 실제로 확인했다고 밝힐 때(검증 보고 첫 줄)
- 한국어: 전제가 사실로 확인됐다
- 설명: `check out` 은 자동사로 "조사해 보니 맞더라"는 뜻이라, 주어가 사람이 아니라 **주장·수치**다. 검증 결과를 먼저 통과시킨 뒤 지적으로 넘어가는 리뷰 구조를 만드는 관용 표현이다.
- 예문: Verification complete — the premises check out, and the settled judgments are respected.
- 유사어: holds up under scrutiny (뜯어봐도 무너지지 않는다 — 더 격식), is borne out by the code (코드가 뒷받침한다)
- 반의어: the premise doesn't hold (전제가 성립하지 않는다)

## "to buy that last factor"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-08-10-msr-image-tool-load.md
- 맥락: 남은 작은 이득 하나를 얻으려고 큰 복잡도를 치를 값어치가 없다고 기각할 때
- 한국어: 그 마지막 한 배수를 얻자고
- 설명: `buy` 를 돈이 아니라 **복잡도를 지불해 성능을 산다**는 은유로 쓴다. `to + 동사원형` 목적 부정사가 문장 끝에 오면서 "이 비용은 저 이득을 위한 것"이라는 저울이 바로 보인다.
- 예문: A Redis lease would add TTLs, polling and failure modes to buy that last factor.
- 유사어: for that last few percent (더 평이한 수치 표현), at that price (그 대가를 치르고서), not worth the candle (관용적·문어)
- 반의어: comes for free (아무 비용 없이 딸려 온다)

## "That's rationalization."
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (TDD 스킬 문서)
- 맥락: 상대(또는 자신)가 그럴듯한 핑계로 원칙을 비껴가려 할 때 짧게 끊는 말
- 한국어: 그건 합리화입니다
- 설명: `rationalization` 은 "논리적 사고"가 아니라 **사후 정당화**를 뜻하는 부정어다. `rational`(이성적)과 뿌리는 같아도 의미가 반대쪽이라 한국인 학습자가 자주 헷갈리는 쌍이다.
- 예문: Thinking "skip TDD just this once"? Stop. That's rationalization.
- 유사어: that's a cop-out (구어·더 세다), you're talking yourself into it (스스로를 설득하고 있다), special pleading (논증 오류 용어)
- 반의어: that's a legitimate exception (그건 정당한 예외다)

## "Delete means delete."
- 레지스터: casual, professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (TDD 스킬 문서)
- 맥락: 지시를 절충해서 해석할 여지를 아예 닫아 버릴 때(규칙 문서·구두 지시)
- 한국어: 지우라면 지우는 겁니다
- 설명: `X means X` 동어반복은 논리적으로는 공허하지만, 영어에서는 "달리 읽지 말라"는 강조 장치로 굳어졌다(`no means no`). 규칙 문서에서 예외를 미리 봉쇄할 때 쓴다.
- 예문: Don't keep it as reference, don't adapt it while writing tests — delete means delete.
- 유사어: no wiggle room (해석의 여지 없음), I mean it literally (문자 그대로다), full stop / period (문장 끝에 붙여 논의 종료)
- 반의어: use your judgment (재량껏 하라)

## "a job at risk of being forgotten"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-auto-recipe-creator (back-to-office 스킬 문서)
- 맥락: 오래 방치된 항목을 보고서·인수인계에서 골라 짚을 때(격식 있는 문어)
- 한국어: 잊힐 위험에 놓인 일감
- 설명: `at risk of + 동명사`가 명사 뒤에 바로 붙어 관계절 하나를 아낀다. 수동 동명사(`being forgotten`)라 **누가 잊는지 지목하지 않고** 위험만 말하므로, 상대를 탓하지 않고 경고할 수 있다.
- 예문: Call out anything whose date is several days old — that's a job at risk of being forgotten.
- 유사어: in danger of slipping through the cracks (관용구 — 조직의 틈으로 빠지는 그림), likely to go stale (문서·데이터에 더 잘 맞음)
- 반의어: actively tracked (계속 추적되고 있는)

## "glad it landed cleanly"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 칭찬을 받고 짧게 받아넘길 때(동료 사이 구어, 슬랙·스탠드업)
- 한국어: 깔끔하게 들어가서 다행이네요
- 설명: 앞의 `I'm` 을 생략한 축약 응답이라 구어답다. `land` 는 배포·머지된 변경이 "착지했다"는 개발자 은유이고, `cleanly` 는 충돌·회귀·수정 없이라는 뜻이다.
- 예문: Thanks — glad it landed cleanly.
- 유사어: happy it worked out (더 일반적·비기술), glad that went smoothly (배포 밖 상황에도 씀)
- 반의어: sorry that one bounced (되돌려져서 미안하다)

## "a file outlives the caveat text next to it"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 내보낸 산출물이 화면보다 오래 남으니 더 보수적으로 만들어야 한다고 설득할 때
- 한국어: 파일은 옆에 붙은 단서 문구보다 오래 남는다
- 설명: `outlive`(~보다 오래 살아남다)를 무생물에 붙여, 다운로드된 CSV 가 맥락과 분리되는 문제를 한 문장으로 압축했다. 설계 판단의 근거를 적을 때 그대로 옮겨 쓸 수 있는 틀이다.
- 예문: Recomputing the signals unconditionally would have produced a file that asserts more than the screen does, and a file outlives the caveat text next to it.
- 유사어: the export travels without its context (맥락 없이 돌아다닌다 — 더 설명적), screenshots lie later (구어적 경구)
- 반의어: the caveat travels with the data (단서가 데이터에 붙어 함께 간다)

## "assert more than the screen does"
- 레지스터: technical, professional
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 내보내기·API 응답이 UI 보다 강한 주장을 담으면 안 된다고 규칙을 세울 때
- 한국어: 화면이 말하는 것보다 더 단정해 버리다
- 설명: `assert` 를 "코드가 검사한다"가 아니라 **"산출물이 주장한다"**는 뜻으로 쓴 자리. `more than the screen does` 처럼 대동사 `does` 로 반복을 피하는 비교 구문이 영어답다.
- 예문: The CSV honors that same gate, because recomputing the badges would produce a file that asserts more than the screen does.
- 유사어: claim more confidence than we have (확신을 과장하다), overstate what the data supports (데이터가 뒷받침하는 것 이상을 말하다)
- 반의어: mirror exactly what the UI shows (화면과 정확히 같은 것만 담다)

## "at zero new abstractions"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 기존 구조를 재사용해 추가 비용 없이 기능을 넣었다고 보고할 때
- 한국어: 새 추상화 하나 없이
- 설명: 전치사 `at` 이 "그 값·그 비용으로"라는 가격표를 붙인다(`at no extra cost` 와 같은 계열). 숫자 `zero` 를 형용사로 세워 비용이 정확히 0임을 못박는다.
- 예문: Reusing it kept both new tables at zero new abstractions.
- 유사어: without inventing a new layer (새 층을 만들지 않고), for free, structurally (구조적으로는 공짜로)
- 반의어: at the cost of one more indirection (한 겹 더 우회하는 대가로)

## "a two-line revert"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 내가 넘겨짚어 넣은 부분을 상대가 쉽게 되돌릴 수 있다고 안심시킬 때
- 한국어: 두 줄만 지우면 되돌아갑니다
- 설명: 하이픈 복합형용사(`two-line`)를 명사 앞에 붙이면 `line` 이 단수다 — `two-lines revert` 는 틀리다. 되돌리기 비용을 숫자로 못박아 결정을 가볍게 만드는 협업 어법이다.
- 예문: If you only wanted the fleet table, the matrix buttons are a two-line revert.
- 유사어: trivially reversible (더 격식), one flag away from the old behaviour (플래그 하나로 되돌아간다)
- 반의어: a one-way door (되돌릴 수 없는 결정)

## "one thing I decided rather than asked"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 확인 없이 내 판단으로 처리한 부분을 보고 끝에 스스로 밝힐 때
- 한국어: 여쭙지 않고 제가 판단한 것이 하나 있습니다
- 설명: `rather than` 뒤에 동사를 병렬로 놓아 `decided ↔ asked` 를 맞세운다. 실수를 사과하는 게 아니라 **재량의 범위를 스스로 공개**하는 어법이라, 신뢰를 쌓는 보고 마무리로 좋다.
- 예문: One thing I decided rather than asked: you said "datatable" in the singular, but that view has two tables and both lacked export.
- 유사어: I took the liberty of ~ing (더 격식·정중), I made a judgment call on X (판단이었다고 명시)
- 반의어: I left that for you to decide (그건 결정하지 않고 남겨 뒀습니다)

## "would read as"
- 레지스터: professional, technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 어떤 표기가 독자에게 잘못 읽힐 위험을 설명할 때(설계 근거·리뷰)
- 한국어: ~라고 읽히게 된다
- 설명: `read` 가 수동태 없이 자동사로 "그렇게 읽힌다"를 뜻하는 용법이라 `be read as` 로 쓰면 오히려 어색하다. 화자의 의도가 아니라 **독자의 해석**을 논거로 세우는 자리에 딱 맞는다.
- 예문: A recipe an equipment never ran gets an empty rate, not `0.00` — 0% would read as "ran it and never failed."
- 유사어: comes across as (인상을 준다 — 사람에게도 씀), invites the reading that ~ (그런 해석을 부른다 — 격식)
- 반의어: leaves no room for misreading (오독의 여지가 없다)

## "the line hugs the axis"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-skewnono-v3-nuxt/10006b9b (assistant)
- 맥락: 차트 형태를 골라야 하는 이유를 시각적으로 설명할 때(대시보드 설계)
- 한국어: 선이 축에 딱 붙어 버린다
- 설명: `hug` 는 "끌어안다"에서 나와 무생물이 곡선·해안선을 따라 밀착할 때 널리 쓴다(`the road hugs the coast`). 값이 0에 몰려 선 그래프가 무의미해지는 상황을 한 단어로 그린다.
- 예문: Align-fail days are mostly 0, so the line hugs the axis and you can't count the zero days.
- 유사어: flatlines (완전히 평평해진다 — 더 극적), sits on the baseline (기준선에 얹혀 있다)
- 반의어: the series spreads across the range (값이 범위 전체에 퍼진다)
