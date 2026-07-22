# 2026-07-23 — 새 표현

## "a hypothesis, not a verdict"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 도구·지표가 내놓은 결과를 그대로 믿지 말자고 할 때. 코드 리뷰나 회고에서 쓰는 단정형 경구.
- 한국어: 가설이지 판결이 아니다.
- 설명: `A, not B` 대구로 "참고할 근거일 뿐 결론은 아니다"를 한 마디에 담습니다. hypothesis(검증 대상)와 verdict(확정된 판단)의 격차가 논지 전부라, 다른 짝으로 바꿔 쓰기 좋습니다 — a signal, not a proof / a starting point, not an answer.
- 예문: Treat the linter's dead-code report as a hypothesis, not a verdict — every deletion still needs a repo-wide grep.
- 유사어: take it with a grain of salt (구어, 훨씬 가벼움), indicative rather than conclusive (격식·문어), a lead, not a conclusion (수사 은유)
- 반의어: settled / beyond dispute

## "the odd one out"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 여럿 중 하나만 규칙에서 벗어나 있다고 짚을 때. 회의·리뷰 구어에서 흔합니다.
- 한국어: 혼자만 튀는 것, 나머지와 결이 다른 하나.
- 설명: 원래는 "짝이 안 맞는 하나"라는 뜻의 관용구. 명사를 끼워 변주할 수 있어서 `the odd name out`(이름만 튀는 것), `the odd file out` 처럼 무엇이 어긋났는지까지 지정합니다.
- 예문: The tab files all follow `<tab>/mock.py`, so the one at the root is the odd name out.
- 유사어: the exception (중립·격식), out of step with the rest (행동·관행이 어긋날 때), doesn't fit the pattern (평이)
- 반의어: in keeping with the rest / consistent with the others

## "at a resting point"

- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 남의 진행 중인 작업을 건드려야 할 때, 언제 손대면 되는지 묻는 자리.
- 한국어: 작업이 일단락된 지점, 손 떼도 되는 상태.
- 설명: 끝났다(finished)가 아니라 **지금 멈춰도 깨지지 않는 상태**를 가리킵니다. 그래서 남의 브랜치·작업 트리를 존중하며 타이밍을 물을 때 딱 맞습니다.
- 예문: Want me to commit mine now, or wait until your sharpness work is at a resting point?
- 유사어: at a good stopping point (거의 같은 뜻, 더 구어), once the dust settles (상황이 어수선할 때), when you're between passes
- 반의어: mid-flight / in the middle of a change

## "more ceremony than the change warranted"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 절차를 일부러 건너뛴 이유를 설명할 때. 프로세스 논의에서 방어적이지 않게 쓰는 말.
- 한국어: 변경 규모에 비해 절차가 과했다.
- 설명: ceremony 는 여기서 "형식 절차"(스펙 문서·승인·회의)를 뜻하는 업계 용어입니다. `warrant`(~할 만하다)와 붙여 "그 정도 일에 그만한 절차는 필요 없었다"를 판단으로 제시합니다.
- 예문: I skipped the spec doc — for a twenty-line change it felt like more ceremony than the change warranted.
- 유사어: overkill for this (구어), disproportionate to the change (격식), process for process's sake (비판조)
- 반의어: worth the ceremony / this one earns a full spec

## "fail spuriously"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 테스트가 진짜 버그 없이 붉어질 때. flaky 와는 원인이 다릅니다.
- 한국어: (실제 결함 없이) 헛되이 실패하다.
- 설명: spurious 는 "겉보기만 그럴싸한, 근거 없는"이라는 뜻. flaky(무작위로 오락가락)와 달리 **원인이 분명한데 그 원인이 코드가 아닌 경우** — 환경, 시점, 잘못 쓴 단정 — 에 씁니다.
- 예문: Those assertions would fail spuriously at the office the moment you wire the first tab.
- 유사어: a false positive (결과 관점), go red for the wrong reason (구어), flaky (원인이 무작위일 때만)
- 반의어: fail for a real reason / catch a genuine regression

## "a commitment, not a preview"

- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-22-provider-presence-detection-design.md
- 맥락: 되돌리기 쉬워 보이는 행동이 실은 상태를 바꾼다고 경고할 때. 설계 문서의 Risks 절에 어울립니다.
- 한국어: 한번 하면 되돌릴 수 없는 결정이지, 미리보기가 아니다.
- 설명: 파일 하나 복사하는 사소한 동작이 곧 기능을 켜는 스위치가 되는 구조를 한 줄로 요약합니다. "가볍게 눌러 보면 안 되는 버튼"이라는 경고를 명사 대구로 압축한 형태.
- 예문: The `cp` is a commitment, not a preview — copying a stub to read it would register the feature as ready and 500 the page.
- 유사어: a one-way door (Amazon 계열 용어, 회의에서 흔함), there's no dry run here (구어), binding (법률 뉘앙스의 격식)
- 반의어: a dry run / reversible, a two-way door

## "encode a state that expires"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 테스트나 문서가 "지금 이 순간"을 사실로 굳혀 버린 잘못을 짚을 때.
- 한국어: 유효기간이 있는 상태를 (코드에) 박아 넣다.
- 설명: encode 는 "값을 코드 안에 박아 넣다". 여기에 `a state that expires` 를 붙여, 오늘은 참이지만 내일이면 거짓이 될 사실을 단정으로 써 둔 결함을 가리킵니다. 마이그레이션 중인 코드베이스에서 반복되는 실패 유형이라 이름을 붙여 둘 가치가 있습니다.
- 예문: The suite went red not because the code broke but because those tests encoded a state that expires.
- 유사어: hardcode a moment in time (평이), assert today's truth (설명적), a point-in-time assumption (격식)
- 반의어: hold at every stage / stay true as the migration progresses

## "prior art"

- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/specs/2026-07-22-provider-presence-detection-design.md
- 맥락: 새 제안이 사실은 기존 방식의 일반화라고 밝힐 때. 설계 문서의 소제목으로 자주 씁니다.
- 한국어: 선례, 이미 같은 걸 하고 있는 기존 사례.
- 설명: 특허 용어("선행 기술")에서 왔지만 소프트웨어 설계 문서에서 굳어졌습니다. `Prior art in this repo` 라는 절을 두면 "새 패턴을 들여온다"는 저항을 "이미 두 군데서 하던 걸 묶는다"로 바꿔 놓습니다.
- 예문: Two existing mechanisms already do exactly this, so the section is titled prior art rather than design.
- 유사어: precedent (더 일반적·격식), we already do this in X (평이·구어), an established pattern here
- 반의어: a new pattern / greenfield

## "heads up —"

- 레지스터: casual, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 상대가 모를 만한 사실을 지나가듯 알릴 때. 슬랙·구두 보고의 문두.
- 한국어: 미리 알려 두자면, 참고로.
- 설명: 요청도 사과도 아닌 **정보 전달** 표지입니다. 뒤에 대시나 콤마를 붙여 바로 사실을 잇습니다. 격식 있는 메일에서는 `For your awareness` 나 `Just so you know` 로 갈아탑니다.
- 예문: Heads up — `git status` shows changes I didn't make, so you're editing that file in parallel.
- 유사어: just so you know (거의 동의어, 조금 더 부드러움), FYI (문어·약식), for your awareness (격식)
- 반의어: (해당 없음 — 정보 표지라 반대 개념이 없습니다)

## "hinge on"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 여러 안 중 무엇을 고를지가 단 하나의 사실에 달렸다고 정리할 때.
- 한국어: ~에 달려 있다, ~가 갈림길이다.
- 설명: 경첩(hinge)의 은유라 "문 전체가 이 작은 축 하나로 여닫힌다"는 그림이 남습니다. depend on 보다 **결정적**이라는 뉘앙스가 강해, 논의를 한 질문으로 좁힐 때 씁니다.
- 예문: That makes several designs viable, and the choice between them hinges on one thing.
- 유사어: come down to (구어, 매우 흔함), turn on (문어·격식: the case turns on intent), depend on (중립·약함)
- 반의어: be independent of / hold either way

## "the scroll affordance"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (6ead3117)
- 맥락: UI 리뷰에서 "더 있다는 걸 사용자가 어떻게 아는가"를 논할 때.
- 한국어: 스크롤할 수 있음을 알려 주는 시각적 단서.
- 설명: affordance 는 대상이 스스로 "이렇게 쓰라"고 알려 주는 성질(디자인 용어). 잘린 마지막 줄·그림자·스크롤바가 전부 affordance 이고, 이 단어를 쓰면 "예뻐서"가 아니라 "발견 가능성 때문에" 그렇게 했다는 근거가 섭니다.
- 예문: `max-h-28` is deliberately not a multiple of the row height — a partially clipped last row is itself the scroll affordance.
- 유사어: a visual cue (평이), a discoverability hint (설명적), signifier (Norman 이후의 엄밀한 용법)
- 반의어: a hidden control / no visual cue

## "be level with (a branch)"

- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 로컬과 원격이 같은 커밋에 있다고 보고할 때.
- 한국어: (브랜치가) 나란하다, 앞서지도 뒤처지지도 않았다.
- 설명: `ahead / behind` 와 한 세트로 쓰는 표현. `in sync with` 보다 짧고, git 이 쓰는 up to date 보다 대화체에 가깝습니다.
- 예문: Working tree is clean and `main` is level with `origin/main` — nothing to push.
- 유사어: in sync with (가장 흔함), up to date with (git 출력의 표현), neither ahead nor behind (설명적)
- 반의어: ahead of / behind origin, diverged

## "carry (something) forward"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 지금은 못 하고 다음 자리로 넘기는 항목을 정리할 때. 회의록·인수인계 마무리 문장.
- 한국어: 다음으로 넘기다, 이월하다.
- 설명: 회계의 "이월"에서 왔지만 업무 일반에 정착했습니다. 수동형 `Two things carried forward for when you're at the office` 처럼 목록 머리에 쓰면 "버린 게 아니라 보류"라는 뜻이 분명해집니다.
- 예문: Two things carried forward for when you're at the office: the smoke test and the two verify items.
- 유사어: park (something) (구어: let's park that), defer (격식), leave on the list for later
- 반의어: close out / drop (something)

## "buy (someone) something"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 어떤 설계 결정이 대가로 얻어 준 이득을 말할 때. `cost` 와 짝지어 씁니다.
- 한국어: (그 선택이) ~를 벌어다 주다, ~를 얻게 해 주다.
- 설명: 돈이 아니라 **설계 판단**을 주어로 세우는 용법이라 처음엔 낯섭니다. `Cost: ... Buys: ...` 형태로 트레이드오프를 두 줄로 제시하면 논의가 아주 빨라집니다.
- 예문: That's the fail-fast the tab split bought you — one broken tab can't quietly serve fabricated data.
- 유사어: gain you / earn you (거의 동의어), what you get in return (평이), the payoff is (명사형)
- 반의어: cost you / at the expense of

## "the dangerous kind of wrong"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 틀린 것들 중에서도 특히 위험한 종류를 구분해 지적할 때.
- 한국어: 위험한 쪽으로 틀린 것.
- 설명: `the ... kind of X` 틀은 같은 범주 안에서 등급을 가릅니다. 여기서는 "요란하게 틀려서 바로 걸리는 오류"와 "권위 있게 읽혀서 그대로 믿게 되는 오류"를 갈라놓습니다. 뒤에 근거를 대시로 붙이는 게 정석.
- 예문: The docstring was the only thing that was wrong, which is the dangerous kind of wrong — it reads authoritative and costs nothing to believe.
- 유사어: wrong in a way that doesn't announce itself (풀어쓰기), a silent failure (기술 용어), plausible but false
- 반의어: obviously wrong / wrong in a way that fails loudly

## "walk into (a trap)"

- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (d4c08a6a)
- 맥락: 스스로 함정에 걸릴 뻔했다고 인정할 때. 회고에서 자기 판단을 낮춰 말하는 자리.
- 한국어: (함정에) 걸려들다, 빠질 뻔하다.
- 설명: `nearly walked into` 처럼 부사를 앞에 붙이면 "피했지만 아슬아슬했다"가 됩니다. 남을 탓하지 않고 위험 지점만 남기는 표현이라 팀 회고에서 안전합니다.
- 예문: The module claims those prefixes identify a family, which is the trap I nearly walked into.
- 유사어: fall for (something) (더 구어, 속았다는 뉘앙스), be caught out by (영국식), take the bait (미끼 은유)
- 반의어: catch it in time / see it coming
