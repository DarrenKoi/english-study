# 2026-08-20 — 코칭

## 한글→영어

### 카드 1 — 기다렸다가 이어서 (내가 쓴 한글)
- 내가 쓴 한글: "기다렸다가 설명 업데이트하고 humanize까지 돌려줘"   (출처: transcript:[user] skewnono_v3_nuxt/6b1b45b4)
- 자연스러운 영어: Wait for them to come back, then update the descriptions and run humanize on top.
- 왜 이렇게: "기다렸다가"는 wait and 가 아니라 `wait for X, then Y` 로 풀어야 순서가 산다. 여기서 기다리는 대상은 탐색 에이전트이므로 목적어 them 을 살려 준다. "~까지"는 also 로도 되지만, 앞 작업 뒤에 한 겹 더 얹는 어감은 `on top` 이 정확하다. `and also run humanize` 는 단순 나열이 되어 "그것까지" 의 맛이 빠진다.

### 카드 2 — 문제 없어 보이니 그대로 밀어 줘 (내가 쓴 한글)
- 내가 쓴 한글: "이 작업에 별 다른 문제는 없을 거라 생각하니 완료되는대로 commit and push도 해줘"   (출처: transcript:[user] skewnono_v3_nuxt/6b1b45b4)
- 자연스러운 영어: I don't expect any surprises here, so go ahead and commit and push as soon as it's done.
- 왜 이렇게: "별 다른 문제는 없을 거라 생각한다"를 `I think there will be no problem` 으로 옮기면 어색하다. 영어는 이 자리에서 예상을 부정형으로 말한다 — `I don't expect any surprises`. surprises 를 쓰면 "문제"보다 범위가 넓어 "예상 못 한 게 안 나올 것"까지 담긴다. 허가를 내주는 "~도 해줘"는 `go ahead and` 가 정확한 대응이다. "완료되는대로"는 `when it's done` 보다 `as soon as it's done` 이 즉시성을 살린다.

### 카드 3 — 노후를 만든 게 아니라 지나친 것 (고급 한글 · 번역)
- 한글 원문: "이번 변경은 그 노후를 만든 것이 아니라 세 번째로 지나친 것입니다."   (출처: transcript:[assistant] / repo:skewnono_v3_nuxt docs/opencode 리뷰 기록)
- 자연스러운 영어: This change didn't create the staleness; it's the third one to walk past it.
- 번역 포인트: "노후"를 aging 으로 옮기면 물리적 마모가 되어 문서 맥락에 안 맞는다. staleness 가 정확하다. "지나친 것"은 pass 가 아니라 `walk past` 다 — 눈앞에 있었는데 손대지 않고 갔다는 그림이 들어가야 지적의 뜻이 산다. 서수 `the third one to ...` 는 "나만 그런 게 아니다"를 조용히 담아 책임을 분산시키는 장치이고, 세미콜론이 부정과 정정을 한 호흡에 붙인다.

### 카드 4 — 막는 것은 접근이 아니라 초대 (고급 한글 · 번역)
- 한글 원문: "이 기능이 막는 것은 접근이 아니라 초대입니다."   (출처: transcript:[assistant] / repo:skewnono_v3_nuxt docs/opencode 리뷰 기록)
- 자연스러운 영어: What this feature blocks is not access but the invitation.
- 번역 포인트: `What ... is` 분열문(cleft)이 핵심이다. 한국어의 "~것은 ~이다" 강조 구문이 영어에서 그대로 대응되는 자리라, 초점이 목적어에 정확히 얹힌다. `not A but B` 는 구어에서 `not A — B` 로 대시를 쓰기도 하지만, 설계 근거를 적는 문어에서는 접속사를 살리는 편이 낫다. the invitation 에 정관사를 붙여야 앞에서 말한 그 초대(메뉴 노출)를 가리킨다.

### 카드 5 — 게이트는 답이 무엇을 드러내는가를 따른다 (고급 한글 · 번역)
- 한글 원문: "carve-out 이라는 사실이 admin 전용을 뜻하지 않습니다. gate 는 답이 무엇을 드러내는가를 따릅니다."   (출처: transcript:[assistant] / repo:skewnono_v3_nuxt docs/opencode 리뷰 기록)
- 자연스러운 영어: Being a carve-out doesn't make an endpoint admin-only. The gate follows what the answer reveals, not how the code gets it.
- 번역 포인트: "~라는 사실이 ~을 뜻하지 않는다"는 동명사 주어 `Being a carve-out` 으로 줄이면 훨씬 가볍다. mean 보다 make 가 낫다 — 규칙이 무엇을 만들어 내는지를 말하는 문장이기 때문이다. 둘째 문장은 원문에 없는 `not how the code gets it` 을 덧붙였다. 한국어는 대조항을 생략해도 읽히지만 영어는 follows X 만 두면 기준이 헐거워, 대조를 세워야 규칙으로 읽힌다.

## 영어 다듬기

### 카드 1 — 소개 페이지 설명 보강 요청
- 내가 쓴 영어: "give some more explanation in each page intro in the intro page. you can batch the jobs with /oc-discuss to explore the pages. If lots of Koreans are used, do not forget to use /humanize-korean:humanize skill."   (출처: transcript:[user] skewnono_v3_nuxt/6b1b45b4)
- 정정: `If lots of Koreans are used` → `If a lot of Korean text is used`. Koreans 는 셀 수 있는 명사로 "한국 사람들"이 된다. 언어를 뜻할 때는 무관사 단수 Korean 이고, 분량을 말하려면 Korean text / Korean prose 처럼 명사를 세워야 한다.
- 더 나은 표현: Flesh out the per-page blurbs on the intro page. Feel free to fan out parallel agents to read the pages first. If the result ends up mostly in Korean, run it through /humanize-korean:humanize.
- 왜: `give some more explanation in each page intro in the intro page` 는 in 이 두 번 겹쳐 위치가 흐려진다. `flesh out` 하나로 "이미 있는 짧은 글을 살 붙여 늘려라"가 정확히 전달되고, blurb 은 소개용 짧은 설명문을 가리키는 딱 맞는 단어다. `batch the jobs` 는 일감을 모아 한 번에 돌린다는 뜻이라 병렬 탐색과 어긋난다 — `fan out` 이 의도한 동작이다. 마지막 문장은 `run it through X` 로 도구를 통과시키는 관용을 쓰면 do not forget 같은 지시가 필요 없어진다.

### 카드 2 — 태그가 되살아난 것 같다
- 내가 쓴 영어: "in the activity page, I see CD-SEM as 가장 많이 쓴 기능 from many users. I thought we lifted up this tag as CD-SEM is too broad term. check it please"   (출처: transcript:[user] skewnono_v3_nuxt/eee1b8fd)
- 정정: `CD-SEM is too broad term` → `CD-SEM is too broad a term`. too/so/as + 형용사가 단수 가산명사를 수식할 때는 관사가 형용사 뒤로 간다(too broad a term, so big a change). `too broad a category` 도 같은 꼴이다.
- 더 나은 표현: On the activity page, CD-SEM is showing up as the top feature for a lot of users. I thought we'd retired that tag because it's too broad a bucket — can you check?
- 왜: `lift up` 은 물리적으로 들어 올린다는 뜻이라 "태그를 걷어냈다"가 전달되지 않는다. 이 맥락에서는 `retire`(더 이상 쓰지 않기로 하다)가 정확하고, drop/phase out 도 쓸 수 있다. `I see X from many users` 보다 `X is showing up ... for a lot of users` 가 관찰 대상이 화면임을 분명히 한다. 끝의 `check it please` 는 문법은 맞지만 명령형이라 딱딱하다. `can you check?` 한 마디면 같은 요청이 훨씬 부드럽다.

### 카드 3 — 빠진 섹션 지적
- 내가 쓴 영어: "update the intro page. we miss 실험실 intro in the page."   (출처: transcript:[user] skewnono_v3_nuxt/300f9ed8)
- 정정: `we miss 실험실 intro` → `we're missing the 실험실 intro`. miss 의 단순현재는 "그리워하다 / 놓치다(반복)"로 읽힌다. 지금 없다는 상태를 말하려면 진행형 `be missing` 을 쓰고 관사도 붙인다.
- 더 나은 표현: The intro page has no 실험실 section — it's missing entirely. Can you add it?
- 왜: 원문은 "업데이트하라"와 "빠졌다"가 따로 놀아 무엇을 고칠지가 두 번 읽어야 잡힌다. 문제를 먼저 말하고 요청을 뒤에 두면 한 번에 읽힌다. `has no X` 는 부재를 사실로 진술하고, `missing entirely` 가 "일부가 부실한 게 아니라 통째로 없다"를 못박는다.

### 카드 4 — 테이블 기본값·정렬 요청
- 내가 쓴 영어: "in device-statistics, in 디바이스 선택 table, make the default row counts 50. and make sortable based on the measurement counts for 90 days, lot_cd or Grade."   (출처: transcript:[user] skewnono_v3_nuxt/ebc0c755)
- 정정: `make the default row counts 50` → `make the default row count 50`. count 는 여기서 "한 페이지에 몇 행"이라는 하나의 설정값이므로 단수다. 그리고 `make sortable` 은 목적어가 빠졌다 — make 는 `make X sortable` 로 대상을 받아야 한다.
- 더 나은 표현: On device-statistics, in the 디바이스 선택 table: default the page size to 50, and make the 90-day measurement count, lot_cd, and Grade sortable by clicking the header.
- 왜: default 를 동사로 쓰는 `default the page size to 50` 은 개발 문맥의 관용이라 짧고 오해가 없다. row count 보다 page size 가 페이지네이션 설정임을 정확히 가리킨다. `the measurement counts for 90 days` 는 하이픈 복합형용사 `the 90-day measurement count` 로 줄면 열 이름처럼 읽혀 더 낫다. 마지막으로 `by clicking the header` 를 붙이면 어떤 UI 를 원하는지가 확정되어, 구현자가 되묻지 않아도 된다.
