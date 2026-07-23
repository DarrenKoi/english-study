# 2026-07-24 — 새 표현

## "close the loop on X"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (c5738483)
- 맥락: 열어 두었던 확인 사항이 마침내 검증돼 끝났다고 알릴 때. 메일·스탠드업 구어 양쪽에서 씁니다.
- 한국어: (미결로 남았던 건을) 매듭짓다, 확인해서 닫다.
- 설명: 시작만 해 놓고 결과 확인이 안 된 일을 "고리를 닫는다"고 표현합니다. 단순히 끝냈다는 finish 와 달리 **확인·회신이 돌아와 순환이 완성됐다**는 뉘앙스가 핵심. 사람에게 쓰면(`close the loop with 사람`) "그쪽에 결과를 알려 주다"가 됩니다.
- 예문: Your office test closes the loop on the gateway connection — that was the one thing we could never verify from home.
- 유사어: tie off a loose end (남은 실밥을 묶다, 더 구어), confirm end-to-end (기술·중립), bring X to closure (격식·문어)
- 반의어: leave it open-ended / let it dangle

## "with room to spare"

- 레지스터: conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (f604dd4e)
- 맥락: 한계선에 아슬아슬한 게 아니라 여유 있게 통과했다고 말할 때. 성능·레이아웃·마감 어디에나.
- 한국어: 여유 있게, 아직 남는 채로.
- 설명: `spare` 는 "남아도는"이라는 뜻이라, 공간·시간·예산이 다 쓰이지 않고 남았음을 뒤에서 덧붙입니다. 문장 끝에 붙이는 부사구라 어순 고민이 없고, 앞에는 보통 수치가 옵니다(`at 1920px`, `in 40 seconds`).
- 예문: The composer fits at 1920px with room to spare, so the earlier clipping report was wrong.
- 유사어: comfortably (한 단어로 대체 가능), with margin to spare (여유폭을 더 강조), and then some (구어, "그러고도 남는다")
- 반의어: by a hair / just barely

## "line up with"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (f604dd4e)
- 맥락: 내가 찾은 사실이 상대가 말한 내용과 어긋나지 않음을 확인해 줄 때. 회의 구어에서 특히 자주.
- 한국어: ~와 들어맞다, 부합하다.
- 설명: 물건을 줄 맞춰 세운다는 그림에서 왔습니다. `match` 가 값의 일치라면 이쪽은 **서로 다른 두 근거가 같은 방향을 가리킨다**는 정합성 쪽. 상대의 말을 받을 때 쓰면 "당신 말이 맞았다"를 부드럽게 전합니다.
- 예문: The comps turned out to be an export of the existing code, which lines up with your clarification that this was a consistency pass.
- 유사어: square with (더 구어, 반박 뉘앙스 섞임), be consistent with (격식·문어), tally with (영국식 문어)
- 반의어: be at odds with / contradict

## "get burned (by X)"

- 레지스터: casual, conversational
- 출처: transcript:[assistant] skewnono_v3_nuxt (e5bd7677)
- 맥락: 과거에 그 문제로 실제 피해를 본 적이 있어 이번엔 조심한다고 말할 때. 격식 문서에는 쓰지 않습니다.
- 한국어: (그 일로) 한 번 데다, 호되게 당하다.
- 설명: 손을 덴 경험이 다음 행동을 바꾼다는 은유라, 뒤에 보통 예방책이 따라옵니다. 수동태(`got burned`)가 기본형이고, 원인은 `by` 로 답니다. 격식을 올리려면 `was bitten by` 보다 `has already suffered from` 쪽.
- 예문: This tree already got burned by concurrency once today, so I'll stage explicit paths only — never `git add -A`.
- 유사어: get bitten by (거의 동일, 살짝 더 가벼움), learn it the hard way (교훈에 초점), have been there before (완곡)
- 반의어: come away unscathed

## "textbook X"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (e5bd7677)
- 맥락: 교과서에 실릴 만큼 전형적인 사례라고 한마디로 분류할 때. 리뷰 코멘트에서 특히 편합니다.
- 한국어: 교과서적인 ~, 전형적인 ~.
- 설명: 명사 앞에 붙이는 한정어라 `a textbook example of` 를 통째로 쓰지 않아도 됩니다(`textbook duplication`, `textbook off-by-one`). 칭찬이 아니라 **"딱 그 유형"이라는 진단**으로 쓰일 때가 많고, 그래서 뒤에 `But …` 이 이어지는 일이 잦습니다.
- 예문: Two pages differing by six lines is textbook duplication — but here every sibling pair looks the same, so it's the house pattern.
- 유사어: a classic case of (구어, 살짝 체념 섞임), a canonical example of (격식·기술 문서), by the book (절차를 지켰다는 뜻이라 의미가 다름 — 혼동 주의)
- 반의어: an edge case / atypical

## "drag in (a dependency)"

- 레지스터: technical
- 출처: repo:skewnono_v3_nuxt docs/superpowers/plans/2026-07-23-msr-image-tool-fetch.md
- 맥락: import 한 줄이 원치 않는 무거운 의존성까지 끌고 들어온다고 경고할 때. 주석·설계 문서에서.
- 한국어: (딸려서) 함께 끌고 들어오다.
- 설명: 끌고 온다는 물리적 어감이 있어 **의도치 않음**을 드러냅니다. 중립적인 `pull in` 과 달리 대개 부정문·경고문에 놓입니다(`must NOT drag in …`). 전이 의존성(transitive dependency) 이야기를 일상어로 옮길 때 쓰기 좋습니다.
- 예문: Importing this package must not drag in office-only dependencies, so the provider module is imported lazily.
- 유사어: pull in (중립), bring along (구어), transitively import (격식·정확)
- 반의어: keep the import surface lean

## "next in line"

- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (c5738483)
- 맥락: 여러 후보 중 다음 차례가 무엇인지 짚을 때. 우선순위 논의의 마무리 문장으로.
- 한국어: 다음 차례인, 대기 순서상 그다음.
- 설명: 줄 서 있는 그림이라 **이미 순서가 정해져 있다**는 함의가 붙습니다. 아직 정해지지 않았다면 `a candidate for next` 가 정확합니다. 사람에게 쓰면 승계·승진 뉘앙스(`next in line for the role`).
- 예문: You recently wrote the datatable docs, which suggested the BM/PM feature was next in line.
- 유사어: up next (구어·짧음), on deck (미국 야구 은유, 캐주얼), the next candidate (중립·격식)
- 반의어: at the back of the queue

## "signposting"

- 레지스터: professional
- 출처: transcript:[user] skewnono_v3_nuxt (f604dd4e, frontend-design 스킬 본문)
- 맥락: UI 문구·문서 제목이 길잡이 역할을 한다고 설명할 때. 디자인·기술 글쓰기 담론의 용어.
- 한국어: 길 안내 표지 노릇, 이정표 역할.
- 설명: 도로 표지판(signpost)의 동명사형으로, 낱개 표지가 아니라 **표지를 세우는 행위·체계 전체**를 가리킵니다. 글쓰기 강의에서는 "독자가 지금 어디쯤인지 알려 주는 장치"라는 뜻으로도 씁니다.
- 예문: The vocabulary of an interface is the signposting for someone navigating the product, so the same action keeps the same name everywhere.
- 유사어: wayfinding (공간·UX 용어), navigational cues (중립·설명적), orientation for the reader (글쓰기 맥락)

## "sometimes less is more"

- 레지스터: conversational
- 출처: transcript:[user] skewnono_v3_nuxt (f604dd4e, frontend-design 스킬 본문)
- 맥락: 더 넣자는 제안을 부드럽게 눌러 절제를 권할 때. 디자인·코드 리뷰 어디서나 통합니다.
- 한국어: 덜어 내는 편이 나을 때가 있다.
- 설명: 건축가 미스 반데어로에의 경구가 일상어로 굳은 것. `sometimes` 를 앞에 달면 원칙 선언이 아니라 이번 건에 대한 제안이 되어 훨씬 덜 강압적입니다. 뒤에는 보통 무엇을 뺄지 구체안이 따라옵니다.
- 예문: Sometimes less is more — extra animation is exactly what makes a page feel machine-generated.
- 유사어: restraint pays off (더 격식), keep it minimal (직설·중립), cut one thing before you leave the house (은유적 조언)
- 반의어: go maximalist / more is more

## "build to a quality floor"

- 레지스터: professional, technical
- 출처: transcript:[user] skewnono_v3_nuxt (f604dd4e, frontend-design 스킬 본문)
- 맥락: 자랑할 항목이 아니라 당연히 지켜야 할 최저선을 정할 때. 기준 합의 문장으로.
- 한국어: 최저 품질선을 지켜 만들다.
- 설명: `floor`(바닥)는 밑으로 내려갈 수 없는 하한, `ceiling`(천장)은 상한. 접근성·반응형처럼 **못 지키면 결함이지만 지켜도 칭찬거리는 아닌** 항목을 묶어 부를 때 씁니다. 원문의 `without announcing it` 이 그 성격을 잘 짚습니다.
- 예문: Build to a quality floor without announcing it: responsive down to mobile, visible keyboard focus, reduced motion respected.
- 유사어: table stakes (구어, "기본 입장료"), a baseline (중립), a minimum bar (구어·중립)
- 반의어: a stretch goal / a ceiling

## "cancel each other out"

- 레지스터: technical
- 출처: transcript:[user] skewnono_v3_nuxt (f604dd4e, frontend-design 스킬 본문)
- 맥락: 두 규칙이 서로를 무효화해 결과적으로 아무 효과가 없을 때. CSS·설정·플래그 디버깅에서.
- 한국어: 서로 상쇄되어 무효가 되다.
- 설명: 수학의 상쇄에서 왔고, 주어는 늘 복수입니다. 한쪽이 다른 쪽을 이기는 `override` 와 달리 **양쪽 다 의도대로 안 먹힌** 상태를 가리킵니다. `out` 을 빼고 `cancel each other` 라고만 해도 통하지만, 구어에서는 out 을 붙이는 쪽이 자연스럽습니다.
- 예문: It's easy to write CSS selectors that cancel each other out, especially for the padding between sections.
- 유사어: override one another (한쪽이 이김 — 뉘앙스 다름), negate each other (격식), fight each other (구어·비유)
- 반의어: compose cleanly / stack

## "below the fold"

- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (f604dd4e)
- 맥락: 스크롤해야 보이는 위치라 사실상 안 보인다고 지적할 때. 웹 UI 리뷰의 표준 용어.
- 한국어: 첫 화면 아래로 밀려난, 스크롤해야 보이는.
- 설명: 접힌 신문의 아래쪽 절반이라 가판대에서 안 보인다는 데서 왔습니다. `off-screen`(아예 화면 밖)과 달리 **스크롤하면 있긴 있다**는 점이 다릅니다. 중요한 요소가 여기 있으면 그 자체로 결함 보고가 됩니다.
- 예문: The chat panel is a proper card now, but the composer is still below the fold.
- 유사어: out of view without scrolling (풀어쓴 중립형), off-screen (더 강함 — 아예 안 보임), buried (구어·비유)
- 반의어: above the fold

## "fence (something) off"

- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (e5bd7677)
- 맥락: 남이 작업 중인 영역을 이번 범위에서 일부러 빼겠다고 선언할 때. 협업 조율 문장으로.
- 한국어: 울타리를 쳐 손대지 않다, 범위 밖으로 격리하다.
- 설명: 물리적 울타리 은유라 **경계가 명시적**이라는 어감이 있습니다. 단순히 안 한다는 `skip` 과 달리 "이유가 있어 접근 금지로 표시해 뒀다"에 가깝습니다. 대상이 대명사면 `fence it off` 로 사이에 넣습니다.
- 예문: `msr_image/` is fenced off from this review — another session still owns it and will keep changing it.
- 유사어: cordon off (사고 현장 어감, 더 강함), wall off (영구 격리 뉘앙스), keep out of scope (중립·문어)
- 반의어: bring it into scope

## "a cold read"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (e5bd7677)
- 맥락: 사전 준비 없이 처음 훑어보는 상태를 가리킬 때. 준비의 가치를 강조하는 대비 문장에서.
- 한국어: 아무 배경 없이 처음 읽어 보는 것.
- 설명: 배우가 대본을 미리 안 보고 읽는 오디션 용어에서 왔습니다. `evidence, not a cold read` 처럼 **대비 항으로** 놓을 때 가장 잘 삽니다. 사람의 심리를 즉석에서 읽는다는 점술 용어 `cold reading` 과는 다른 갈래라 문맥으로 구분됩니다.
- 예문: Let me capture the prep findings now, so 02:10 starts from evidence rather than a cold read.
- 유사어: going in blind (구어), a first pass with no context (풀어쓴 중립형), sight-reading (음악 은유)
- 반의어: an informed read / a briefed start

## "bespoke"

- 레지스터: professional
- 출처: transcript:[assistant] skewnono_v3_nuxt (f604dd4e)
- 맥락: 공용 부품을 두고 그 자리에만 따로 만든 것을 지적할 때. 코드 리뷰에서는 대개 비판입니다.
- 한국어: 그 건에만 맞춰 따로 지은, 주문 제작한.
- 설명: 원래 맞춤 양복(bespoke suit)의 고급스러운 칭찬어인데, 소프트웨어에서는 뜻이 뒤집혀 **"공용 컴포넌트를 안 쓰고 혼자 만든"**이라는 부정 평가로 굳었습니다. 이 반전을 모르면 칭찬으로 오독하기 쉽습니다.
- 예문: Live-alarm had grown a bespoke `FeedStatusBar` doing the same three jobs the shared MetaBar already does.
- 유사어: hand-rolled (구어, 같은 비판 어감), one-off (일회성에 초점), custom-built (중립)
- 반의어: off-the-shelf / shared

## "a stale lock"

- 레지스터: technical
- 출처: transcript:[assistant] skewnono_v3_nuxt (f604dd4e)
- 맥락: 잠금이 걸려 있을 때 그냥 지워도 되는지 판단하는 대목에서. 프로세스·파일 잠금 디버깅.
- 한국어: 주인이 죽고 남은 잠금, 유효하지 않은 잠금.
- 설명: `stale` 은 "김빠진·오래돼 못 쓰는". 잠금을 만든 프로세스가 이미 죽었는데 파일만 남은 상태를 가리키고, 이때만 삭제가 안전합니다. 살아 있는 프로세스가 쥐고 있으면 반대로 `genuinely held` 라고 표현합니다.
- 예문: A live Chrome genuinely holds that profile — it isn't a stale lock, so I'll drive my own browser instead.
- 유사어: an orphaned lock (주인 없는), a leftover lockfile (구체·구어), a dangling lock (중립)
- 반의어: a live lock holder / a genuinely held lock
