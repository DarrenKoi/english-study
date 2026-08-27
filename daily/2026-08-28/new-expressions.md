# 2026-08-28 — 새 표현

## "it now states the opposite of the code"
- 레지스터: technical, professional
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 코드가 바뀌었는데 문서가 안 따라와서 둘이 정반대를 말하고 있다고 리뷰에서 지적할 때(격식·문어)
- 한국어: 이제 그 문서가 코드와 정반대를 말하고 있다
- 설명: `state` 는 문서·규격이 주어일 때 쓰는 동사로, `say` 보다 한 단계 격식이 높고 "공식적으로 적혀 있다"는 무게를 준다. `the opposite of` 는 "다르다"가 아니라 "반대다"까지 밀어붙여 방치할 수 없는 등급임을 표시한다. 부사 `now` 가 앞의 변경을 원인으로 지목해, 문서를 고칠 책임이 이 diff 에 있음을 문장 안에서 정한다.
- 예문: CLAUDE.md defers per-feature specifics to MIGRATION.md, and it now states the opposite of the code.
- 유사어: contradicts the implementation (중립·건조), is at odds with what the code does (조금 완곡), the doc and the code disagree (구어)
- 반의어: the doc still tracks the code

## "was left contradicting it"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 한 문서만 고치고 짝이 되는 다른 문서를 빠뜨린 누락을 지적할 때(리뷰·문어)
- 한국어: (고쳐지지 않은 채) 모순 상태로 남겨졌다
- 설명: 수동태 `was left` + 현재분사 `contradicting` 이 결합해 "누가 일부러 그런 게 아니라 손이 안 닿아 그 상태로 남았다"를 그린다. 능동으로 `you forgot to update it` 이라 하면 사람을 겨누지만, 이 형태는 파일을 주어로 두어 지적이 인신공격이 되지 않는다. 리뷰 코멘트에서 자주 쓰는 완충 장치다.
- 예문: `recipe_idp.txt` was rewritten but this doc was left contradicting it.
- 유사어: was left out of sync (더 평이), went un-updated (짧고 건조), fell out of step with (비유적)
- 반의어: was brought in line

## "re-hand-rolls what X already owns"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 이미 있는 헬퍼가 담당하는 로직을 새 코드가 손으로 다시 짰다고 지적할 때(코드 리뷰)
- 한국어: X 가 이미 맡고 있는 것을 다시 손으로 짜고 있다
- 설명: `own` 이 소유가 아니라 **책임 소재**를 뜻하는 용법이 핵심이다 — "이 규칙의 주인은 저 함수다"라고 선언하면 중복 제거의 방향(어느 쪽을 남길지)까지 한 단어로 정해진다. 접두사 `re-` 가 "이미 있는데 또"를 얹어 지적의 날을 세운다.
- 예문: `align_point_of` re-hand-rolls the basename extraction that `image_variants` already owns.
- 유사어: duplicates logic that belongs to X (중립·설명적), reinvents X's job (구어)
- 반의어: delegates to the existing helper

## "the entry now dangles inside the prose paragraph"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: diff 가 헤더 한 줄을 지워서 그 아래 항목이 소속을 잃고 엉뚱한 곳에 붙어 버린 서식 파손을 지적할 때
- 한국어: 그 항목이 이제 산문 문단 안에 고아처럼 매달려 있다
- 설명: `dangle` 은 문법 용어 `dangling modifier` 와 같은 그림 — 붙을 곳을 잃고 허공에 걸린 상태. 코드·문서 구조 얘기에 쓰면 "문법적으로는 멀쩡한데 소속이 틀렸다"는 미묘한 결함을 한 단어로 전한다. `inside` 가 "밖으로 튀어나온" 게 아니라 "엉뚱한 것 안에 들어갔다"를 정확히 짚는다.
- 예문: The diff consumed the second `Raises:` header, so the `LookupError:` entry now dangles inside the `eqp_id` prose paragraph.
- 유사어: is orphaned (더 격식·건조), hangs off nothing (구어), lost its section
- 반의어: sits under its own heading

## "nothing ruff/eslint would catch"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 리뷰를 닫으면서 "여기서 찾은 것들은 자동 도구로는 안 잡히는 종류"라고 리뷰의 가치를 규정할 때
- 한국어: 린터가 잡아 줄 만한 건 하나도 없다
- 설명: 도구 이름을 그대로 넣어 "사람 리뷰가 필요한 층"을 정의하는 관용적 마무리. 가정법 `would catch` 가 "돌려 보면 잡혔을 것"이라는 반사실을 담아, 지금 발견한 것들이 그 그물 밖이라는 뜻이 된다. 리뷰 결과 요약의 마지막 줄에 두면 CI 통과와 리뷰 통과가 다른 일임을 상기시킨다.
- 예문: No other baseline smells found; nothing ruff/eslint would catch.
- 유사어: nothing a linter flags (짧음), invisible to CI (비유적·강함), not a tooling problem
- 반의어: the linter would have caught this

## "the implementation has no such fallback"
- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 주석·docstring 이 있다고 주장하는 동작이 코드에는 실제로 없다고 반증할 때(격식)
- 한국어: 구현에는 그런 폴백이 없다
- 설명: `no such X` 는 "그런 X 라는 것 자체가 존재하지 않는다"로, `doesn't have a fallback` 보다 단호하다. 앞에서 인용한 주장을 `such` 로 되받아 가리키므로 무엇을 부정하는지가 명확해진다. 바로 뒤에 실제 동작(`it raises SourceUnavailable`)을 붙이는 게 이 표현의 정석 사용법이다.
- 예문: The docstring promises a derived-pair fallback, but the implementation has no such fallback — it raises `SourceUnavailable`.
- 유사어: there is no fallback in the code (평이), that path does not exist (건조)
- 반의어: the fallback is still wired in

## "the diff additionally invents X"
- 레지스터: professional, technical
- 출처: repo:skewnono_v3_nuxt docs/opencode/2026-08-22-align-image-404-review.md
- 맥락: 스펙이 요구하지 않은 기능이 변경분에 슬쩍 들어왔다고 지적할 때(리뷰·격식)
- 한국어: 이 변경이 (요청에 없던) X 를 추가로 지어냈다
- 설명: `invent` 가 "발명"의 긍정 뉘앙스가 아니라 **근거 없이 만들어 냈다**는 비판으로 쓰인다. `additionally` 를 동사 앞에 두어 "요구된 것은 했고, *그 위에* 더 했다"는 순서를 만들면 지적이 전면 부정으로 읽히지 않는다.
- 예문: The spec asks only for folder-listed names; the diff additionally invents `-U`/`-L` split discovery.
- 유사어: goes beyond what was asked (완곡), tacks on an unrequested feature (구어)
- 반의어: implements exactly what the spec asks

## "the code says so out loud"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 내 주장에 대한 증거가 이미 코드 안에 명시적으로 적혀 있다고 밝힐 때(설계 논증·문어)
- 한국어: 코드가 그렇다고 대놓고 말하고 있다
- 설명: 코드를 화자로 삼는 의인화가 논증을 강하게 만든다 — 내 해석이 아니라 코드가 스스로 자백했다는 구도. `out loud` 가 "추론해서 알아낸 게 아니라 소리 내어 말한다"를 얹어, 뒤에 나올 인용(주석·플래그 이름·구분선)의 무게를 미리 올린다. 콜론을 붙여 목록을 잇는 게 전형적인 사용법이다.
- 예문: So the group labels are already lying, and the code says so out loud: `separated: true` was added to 채팅 because it doesn't belong with its neighbours.
- 유사어: the code admits as much (조금 완곡), it's written right there in the source (구어)
- 반의어: that's an inference, not something the code states

## "it's wearing the default layout as a costume"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 어떤 모듈이 공용 틀에 속한 척하지만 실은 자기 것을 다 따로 갖고 있다고 비유로 지적할 때(구어체 논증)
- 한국어: 기본 레이아웃을 의상처럼 걸치고 있을 뿐이다
- 설명: `wear X as a costume` 은 "그것이 되었다"가 아니라 "그것처럼 보이려 입었다"는 뜻이라, 겉모습과 실체의 괴리를 한 번에 그린다. 앞에 근거(자체 셸·자체 랜딩·opt-out 플래그)를 나열한 뒤 이 문장으로 닫으면 목록이 결론으로 승격된다. 격식 문서에서도 통하지만 어조는 확실히 구어 쪽이다.
- 예문: It already opts out of the app shell with its own landing and its own workspace — it's wearing the default layout as a costume.
- 유사어: it only nominally uses the shared layout (격식·건조), it's shoehorned into the default layout (문제의 방향이 반대)
- 반의어: it fits the shared layout natively

## "It's a deletion, not an addition."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 큰 리팩터링을 제안하면서 "일이 늘어나는 게 아니라 줄어든다"고 저항을 미리 꺾을 때(설득·문어)
- 한국어: 이건 추가가 아니라 삭제다
- 설명: `A, not B` 대비를 명사 두 개로만 세운 최소 문장이라 힘이 실린다. 리팩터링 제안이 거절당하는 이유는 대개 "지금 할 일이 늘어난다"인데, 이 한 문장이 그 전제를 뒤집는다. 바로 앞에 "여섯 군데에 등록해야 한다" 같은 현재 비용을 두면 대비가 살아난다.
- 예문: Right now a new page must be registered in six places — collapsing them into one table is a deletion, not an addition.
- 유사어: this removes code rather than adding it (설명적), it's subtraction (짧고 비유적)
- 반의어: that's net-new work

## "one consequence fell out of the move"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 584bd187
- 맥락: 의도한 변경은 아니지만 그 변경에서 자연히 따라 나온 부수 효과를 보고할 때(변경 보고·격식)
- 한국어: 이번 이동에서 결과 하나가 자연히 따라 나왔다
- 설명: `fall out of` 는 "굴러 떨어져 나오다" — 내가 설계한 게 아니라 구조상 필연적으로 딸려 나왔다는 뉘앙스. `side effect` 가 부정적으로 들리는 자리에서 중립적으로 같은 사실을 전할 수 있다. 보고문에서 이 문장 뒤에는 그 결과를 어떻게 처리했는지가 반드시 따라온다.
- 예문: One consequence fell out of the move: the picker used to inherit the analysis bar's lock, and at the top of the page that lock no longer made sense.
- 유사어: a knock-on effect of the move (더 격식), this came out of the change (평이), it followed from the move
- 반의어: that had to be engineered separately

## "at the top of the page that would read as broken"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 584bd187
- 맥락: 기술적으로는 정상인 동작이 새 위치에서는 사용자 눈에 고장으로 보인다고 설명할 때(UI 설계 논증)
- 한국어: 페이지 맨 위에서는 그게 고장 난 것처럼 읽힌다
- 설명: `read as` 는 "실제로 그렇다"가 아니라 "그렇게 해석된다"를 뜻해, 동작의 정오와 인상을 분리한다. UI 얘기에서 `look` 대신 `read` 를 쓰면 "보기에"가 아니라 "의미가 그렇게 전달된다"는 층까지 가리킨다. 가정법 `would` 가 "고치지 않았다면"이라는 반사실을 유지해 준다.
- 예문: The picker greyed out until a recipe was picked; at the top of the page that would read as broken.
- 유사어: users would take it for a bug (평이), it would come across as an error (중립)
- 반의어: it reads as intentional

## "it earns its own bar"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt 584bd187
- 맥락: 어떤 요소에 전용 자리를 주기로 한 판단을 "자격을 얻었다"로 정당화할 때(설계 논증·문어)
- 한국어: 그건 자기 몫의 바를 가질 자격이 있다
- 설명: `earn` 이 화면 공간을 **공짜로 주는 게 아니라 값을 치르고 얻는 것**으로 규정한다. 이 한 동사 덕에 "눈에 띄게 키우자"가 취향 문제에서 기준 문제로 옮겨 간다. 바로 앞에 "다른 것들과 종류가 다른 질문에 답한다" 같은 자격 근거가 오는 게 정석이다.
- 예문: 튜닝할 장비 answers a different kind of question from the three bars below it, so it earns its own bar.
- 유사어: it warrants a dedicated row (격식), it deserves its own slot (평이)
- 반의어: it doesn't warrant a row of its own

## "this is already costing you"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 미래의 위험이 아니라 이미 지불 중인 비용임을 상대에게 각인시킬 때(설득·구어에 가까운 업무 대화)
- 한국어: 이건 이미 대가를 치르고 있다
- 설명: 현재진행형 + `already` 가 "언젠가 문제가 된다"를 "지금 새고 있다"로 시제를 당긴다. 목적어 `you` 를 직접 붙여 비용의 귀속처를 상대로 지정하는 게 설득의 핵심 — 추상적 기술 부채가 상대의 청구서가 된다. 뒤에는 반드시 구체적 증거(중복 트리, 스텁 파일 수)가 와야 감상으로 끝나지 않는다.
- 예문: This is already costing you: `pages/ebeam/` carries parallel cd-sem and hv-sem trees, and two more families are stubbed with an index each.
- 유사어: you're already paying for this (같은 뜻, 더 직접적), it's already a drag on you (구어)
- 반의어: it hasn't bitten you yet

## "that's past what one row holds"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 항목 수가 한 줄·한 화면의 수용 한계를 이미 넘었다고 수치로 판정할 때(설계 논증)
- 한국어: 그건 한 줄이 담을 수 있는 양을 넘는다
- 설명: `past` 를 전치사로 써서 "넘어섰다"를 동사 없이 처리하는 압축형. `what one row holds` 라는 관계절이 한계를 사람 취향이 아니라 **그릇의 용량**으로 객관화한다. 앞에 개수를 세어 두면 이 문장이 결론 역할을 한다.
- 예문: Pull the standalone apps out and E-Beam still has nine tab-worthy pages — that's past what one row holds.
- 유사어: more than one row can take (평이), beyond what fits (짧음)
- 반의어: comfortably within one row

## "the compiler catches none of it"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 여러 곳에 수동으로 등록해야 하는 구조의 위험을 "빠뜨려도 빌드가 안 깨진다"로 규정할 때
- 한국어: 컴파일러가 그중 하나도 잡아 주지 않는다
- 설명: `catch` 의 목적어를 `none of it` 으로 두어 부정을 문장 끝에 배치하는 영어식 강조. "실수하면 조용히 틀린다"는 최악의 실패 양상을 여섯 단어로 전한다. 앞 절에 "여섯 군데에 등록해야 한다"가 오면 원인과 결과가 한 문장에 담긴다.
- 예문: A new page must be registered in six places and the compiler catches none of it.
- 유사어: none of it is type-checked (건조), nothing fails the build (같은 뜻, 도구 중립)
- 반의어: the build breaks if you forget one

## "worth deciding deliberately rather than discovering later"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 지금 결론을 내라고 강요하지 않으면서도 방치의 대가를 알릴 때(권고·문어)
- 한국어: 나중에 발견하는 것보다 지금 의식적으로 정해 두는 편이 낫다
- 설명: `decide` 와 `discover` 를 대비시켜 **선택**과 **사고**를 가르는 문장이다. 두 동명사가 `rather than` 으로 묶여 있어 명령이 아니라 비교가 되고, `worth` 로 시작해 주어를 생략했으므로 지목당하는 사람이 없다. 지적을 남기되 갈등을 만들지 않는 마무리 문장으로 쓴다.
- 예문: Device statistics is quietly drifting toward standalone — worth deciding deliberately rather than discovering later.
- 유사어: better settled now than stumbled on later (구어), make it a choice, not an accident (더 강함)
- 반의어: we can cross that bridge when we come to it

## "this raises the stakes on X rather than lowering them"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 새 정보가 기존 권고를 약화시키는 게 아니라 오히려 더 중요하게 만든다고 정정할 때(격식)
- 한국어: 이건 X 의 판돈을 낮추는 게 아니라 오히려 올린다
- 설명: 상대가 "그럼 그 단계는 안 해도 되겠네"로 읽을 가능성을 문장 안에서 선제적으로 닫는 구조다. `rather than lowering them` 이 없으면 절반만 전달된다 — 예상되는 오독을 명시적으로 부정하는 게 이 표현의 값이다. 대명사 `them` 이 `stakes` 를 받아 반복을 피한다.
- 예문: Adding a second grouping level raises the stakes on the single-table refactor rather than lowering them.
- 유사어: it makes step 3 more urgent, not less (평이), the cost of skipping it just went up
- 반의어: that takes the pressure off

## "It's growing, not bifurcating."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: "우리도 커지니까 따로 떼자"는 주장에 기준을 들이대 반박할 때(설계 심사)
- 한국어: 그건 커지는 것이지 갈라지는 게 아니다
- 설명: 현재진행형 두 개를 `not` 으로 맞세워 규모와 종류를 구분한다. 앞서 세운 판정 기준(어휘를 공유하는가·기존 셸에 맞는가)을 통과했음을 전제로 하므로, 이 문장 하나가 그 기준의 판결문 역할을 한다. 기준 없이 쓰면 그냥 취향 싸움이 된다.
- 예문: Recipe search shares the vocabulary and fits the page shell — it's growing, not bifurcating.
- 유사어: that's scale, not a split (더 짧음), size isn't a reason to fork
- 반의어: it has outgrown the shared shell

## "one word means one thing across both tables"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f9b54b3d
- 맥락: UI 용어를 통일한 이유를 한 줄로 밝힐 때(변경 보고·문어)
- 한국어: 한 단어가 두 표에서 같은 뜻 하나만 갖게 된다
- 설명: `one … one …` 반복이 규칙을 슬로건처럼 만든다. 왜 굳이 기존 표의 단어를 재사용했는지를 설명하는 자리에 두면, 선택이 게으름이 아니라 원칙이 된다. `across` 가 범위를 지정해 "이 표 안에서만"이 아님을 못 박는다.
- 예문: The sub-labels reuse the words the fleet table already uses, so one word means one thing across both tables.
- 유사어: the vocabulary stays consistent (건조), no term does double duty (조금 비유적)
- 반의어: the same word means two different things here

## "a PASS only proves the script ran"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt f9b54b3d
- 맥락: 검증 스크립트를 실패시켜 보지 않은 채 통과를 믿으면 안 된다고 경고할 때(테스트·검증 논의)
- 한국어: PASS 는 스크립트가 돌았다는 것만 증명한다
- 설명: 부사 `only` 가 증명의 범위를 잘라 내는 게 문장의 전부다 — 초록불이 무엇을 보장하고 무엇을 보장하지 않는지 경계를 긋는다. 앞에 `without that negative control` 을 붙이면 조건까지 완성된다. 자기 테스트를 스스로 의심하는 어휘라 리뷰에서 신뢰를 얻는다.
- 예문: Without that negative control, a PASS only proves the script ran, not that it measured anything.
- 유사어: a green check isn't evidence (구어), the assertion was never exercised (기술적)
- 반의어: the oracle was proven able to fail

## "zsh globbing is eating my `--include` flags"
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 86fb71e7
- 맥락: 명령이 예상대로 안 먹힐 때 원인을 짧게 대며 방법을 바꾸겠다고 알릴 때(작업 중 혼잣말투)
- 한국어: zsh 의 글로빙이 `--include` 플래그를 먹어 버리고 있다
- 설명: `eat` 이 셸·파서가 인자를 삼켜 없앤다는 뜻으로 굳어진 개발 구어다. 현재진행형이라 "지금 이 순간 벌어지는 일"로 읽혀 실황 보고에 어울린다. 뒤에 해결책(`so I'm quoting them`)을 대시나 `so` 로 바로 붙이는 게 짝이다.
- 예문: Still mapping the existing gallery — zsh globbing is eating my `--include` flags, so I'm quoting them.
- 유사어: the shell is swallowing the flags (같은 뜻), glob expansion mangles the args (더 격식)
- 반의어: quoting gets them through intact

## "the superset contract is code, not a comment"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt 86fb71e7
- 맥락: 리팩터링으로 어떤 규칙이 주석 수준에서 타입·구조 수준으로 올라갔다고 보고할 때
- 한국어: 상위집합 계약이 이제 주석이 아니라 코드다
- 설명: `X is code, not a comment` 는 "지키라고 적어 둔 것"과 "안 지키면 안 돌아가는 것"의 차이를 다섯 단어로 표현하는 관용형. 리팩터링의 가치를 줄 수가 아니라 **강제력의 층**으로 설명하므로, 라인 수가 줄지 않아도 개선임을 논증할 수 있다.
- 예문: The caller now builds the lattice and passes it in, so the superset contract is code, not a comment.
- 유사어: the invariant is enforced rather than documented (격식), the type system holds it now
- 반의어: it's still an honour-system rule

## "that fix was right, and it stopped one file short"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 과거의 개선을 인정하면서 그것이 딱 한 걸음 모자랐다고 이어서 지적할 때(비판을 부드럽게 여는 법)
- 한국어: 그 수정은 옳았고, 다만 파일 하나를 남기고 멈췄다
- 설명: 앞 절의 인정이 뒤 절의 지적을 무장 해제시킨다 — `and` 를 쓴 것이 요령으로, `but` 이면 인정이 취소되지만 `and` 는 둘 다 참으로 남긴다. `one file short` 는 거리 단위를 파일로 바꾼 표현이라 "얼마나 모자랐는지"까지 수치로 준다.
- 예문: Deriving three consumers from one array was right, and it stopped one file short — four more hand-maintained lists still exist.
- 유사어: it didn't go quite far enough (평이·완곡), it fell one step short of the fix
- 반의어: that change went all the way

## "hiding it was never the drawer's job"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 어떤 장치가 떠맡고 있던 역할이 애초에 그 장치 몫이 아니었다고 정리할 때(설계 논증)
- 한국어: 그걸 숨기는 건 애초에 그 서랍의 일이 아니었다
- 설명: `was never X's job` 이 과거 시제 + `never` 로 "지금부터 아니다"가 아니라 "처음부터 아니었다"를 말한다. 그래서 역할을 빼앗는 게 아니라 잘못 붙은 걸 떼는 일이 되고, 저항이 줄어든다. 바로 뒤에 진짜 담당자(`hiddenOnCloud already does it, per-row`)를 대는 게 필수다.
- 예문: Production hiding was never the drawer's job — `hiddenOnCloud` already does it, per row.
- 유사어: that responsibility sits elsewhere (격식·중립), that's not what the drawer is for (구어)
- 반의어: that is exactly what the drawer is there for

## "X stops being a place"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt f0e35121
- 맥락: 분류 축이 잘못 잡혔을 때, 그것을 위치가 아니라 속성(뱃지·플래그)으로 옮기자고 제안할 때
- 한국어: X 는 더 이상 장소가 아니게 된다
- 설명: 정보 구조 논의에서 **place(어디에 있는가) vs property(무엇인가)** 의 대립을 한 문장에 압축한 표현. `stops being` 이 폐지가 아니라 성격 변경임을 알려, "그럼 그 기능은 어디 가냐"는 반문을 미리 막는다. 같은 틀로 `maturity is a badge, never a place` 처럼 확장해 쓴다.
- 예문: 실험실 stops being a place: maturity becomes a badge on the row, and the pages move to the group they belong to.
- 유사어: it becomes an attribute rather than a location (설명적), stop filing by it (짧고 직접적)
- 반의어: it stays a drawer of its own
