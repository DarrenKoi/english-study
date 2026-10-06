# 2026-10-07 — 새 표현

> 오늘 배치는 repo 문서 10건과 transcript 14건이다. repo 문서는 모두 skewnono_v3_nuxt 의 AFM 적재 명세·질문서·페이지 가치 조사·Vue 학습 노트인데 본문이 한국어여서 표현 재료가 나오지 않았다. transcript 여섯은 `/clear` 만 찍힌 빈 세션. 영어는 네 군데서 나왔다. `office.py` 를 만들어도 되느냐는 질문에 어시스턴트가 영어로 답한 글, `/api/msr-image` 의 404 를 두고 주고받은 두 차례 답, 작업 중간에 찍힌 한 줄짜리 영어 진행 보고, 그리고 세션에 딸려 온 스킬 문서 둘(`browser-verify`, `leave-office`). 스킬 문서와 `/code-review low` 지시문은 앞선 배치에서 대부분 골랐으므로 남은 것만 집었다. 노트에 이미 있어서 뺀 것: `one-for-one`, `hijack the tab`, `is guaranteed to emit`, `compare structure, not colour`, `pick by situation`, `reach for (a tool)`, `is a fine answer`, `not retroactive`, `rather than assuming`, `Gotchas seen so far:`, `an open loop`, `a job that has been rotting`, `Specific beats complete.`, `a launchpad, not a diary`, `at a glance`, `where my head was`, `exercise (a code path)`, `eyeball it`, `tear down`.

## "it has never run against the real Redis and MinIO"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 코드는 준비됐지만 실제 환경에서 돌려 본 적이 없다고 미리 밝힐 때(인수인계·배포 전 안내, 구어와 문어 모두).
- 한국어: 실제 Redis·MinIO 를 상대로는 한 번도 돌려 본 적이 없다
- 설명: `run against X` 는 X 를 상대로 실행한다는 뜻. 테스트(`run the tests against staging`)나 쿼리(`run it against the prod DB`)에 붙는다. 현재완료 `has never run` 은 "지금까지 한 번도"이고 `the real` 이 바로 뒤 문장의 `a fake hash and a fake object store` 와 짝을 이룬다.
- 예문: Yes, the template is ready to copy, but it has never run against the real Redis and MinIO, so do the read-only smoke run first.
- 유사어: hasn't been tested against real data (평이), is untested in production (격식, 보고서), has only run against fakes (반대쪽에서 말하기)
- 반의어: battle-tested (실전에서 검증된), proven in production (운영에서 입증된)

## "do the read-only smoke run first"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 본 작업에 앞서 "켜지기는 하는지"만 가볍게 확인하라고 권할 때(배포 절차 안내).
- 한국어: 읽기 전용 스모크 실행부터 먼저 하세요
- 설명: `smoke test` 는 전원을 넣어 연기가 나는지만 보던 하드웨어 검사에서 온 말. 여기서는 `smoke run` 으로 써서 "시험"보다 "한 번 돌려 봄"에 무게를 뒀다. `read-only` 가 앞에 붙어 "아무것도 쓰지 않으니 안심하고 돌려도 된다"는 뜻까지 담는다. `first` 는 문장 끝에 둔다.
- 예문: Before you copy the adapter into place, do the read-only smoke run first. (작성)
- 유사어: do a dry run (실제 반영 없이 돌려 보기), do a quick sanity check (구어, 더 가벼움), run a preflight check (격식)
- 반의어: go straight to production (바로 운영에 올리다)

## "The `cp` is the switch"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 어떤 동작 하나가 곧 전환 스위치임을 짚어 줄 때(동료에게 구조를 설명하는 말투).
- 한국어: 그 복사가 곧 스위치다
- 설명: `A is the switch` 는 은유를 그대로 서술어에 놓은 문장. 콜론 뒤의 `once office.py exists, the office process serves real AFM data instead of the mock` 가 그 뜻을 푼다. `once` 는 "~하는 순간부터". 한국어 답변에도 같은 말이 나온다("이 복사가 곧 AFM 을 사무실 데이터로 전환하는 스위치입니다").
- 예문: The `cp` is the switch: once `office.py` exists, the office process serves real AFM data instead of the mock.
- 유사어: Copying the file is what turns it on (풀어 쓴 평이체), The copy itself is the cutover (배포 용어 `cutover`)

## "There is no separate flag to flip."
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 따로 켜야 할 설정이 없다고 못 박을 때(설정·배포 설명).
- 한국어: 따로 뒤집을 플래그는 없다
- 설명: `flip a flag / a switch` 는 켜고 끄는 값을 "젖힌다"는 동사. `to flip` 은 `flag` 를 꾸미는 to 부정사이고 `separate` 가 "그것 말고 또"를 맡는다. 짧은 문장을 앞 문장 뒤에 따로 세워서 독자가 "그럼 환경변수는?" 하고 찾지 않게 한다.
- 예문: The `cp` is the switch. There is no separate flag to flip.
- 유사어: No extra config is needed (평이), Nothing else to toggle (구어), It requires no additional configuration (격식)
- 반의어: It's gated behind a feature flag (기능 플래그 뒤에 있다)

## "To back out, …"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 바꾼 것을 되돌리는 방법을 한 줄로 알려 줄 때(절차서·구두 안내).
- 한국어: 되돌리려면
- 설명: `back out` 은 들어간 길을 뒷걸음으로 나오는 그림. 변경을 물린다는 뜻으로 운영 문서에 흔하다. 문두의 `To + 동사` 는 목적을 먼저 내거는 틀이라 독자가 "이 줄은 되돌릴 때 보는 줄"임을 바로 안다. `back out of the deal` 처럼 약속에서 발을 뺀다는 뜻도 있다.
- 예문: To back out, delete `office.py` or set `SKEWNONO_AFM_PROVIDER=mock`.
- 유사어: To roll back (배포 용어, 더 격식), To undo it (평이), To revert (git 문맥)
- 반의어: To roll it out (내보내려면), To go ahead (진행하려면)

## "stays visible either way"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 두 갈래 중 어느 쪽을 택해도 결과가 같다고 안심시킬 때(구어·메신저).
- 한국어: 어느 쪽이든 그대로 보인다
- 설명: `either way` 는 앞에 나온 두 선택지(`delete office.py` 또는 환경변수 변경)를 한꺼번에 받는다. 문장 끝이나 맨 앞 어디에 두어도 된다. `stay + 형용사` 는 상태가 바뀌지 않고 유지된다는 뜻.
- 예문: The page stays visible either way and goes back to showing mock data.
- 유사어: in either case (격식), whichever you choose (선택을 강조), regardless (한 단어, 문어)

## "degrade to a null or a missing button"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (office.py 생성 가능 여부 답변)
- 맥락: 가정이 틀려도 화면이 죽지 않고 기능 일부만 빠진다고 설명할 때(위험도 설명).
- 한국어: null 이나 버튼 하나 빠지는 정도로 낮아진다
- 설명: `degrade to X` 는 "나빠져 봐야 X 까지". 노트에 있는 `degrade gracefully` 가 방식을 말한다면 이쪽은 도착점을 말한다. 앞의 `None of the four should crash the page` 와 세미콜론으로 이어 "죽지는 않는다, 대신 이렇게 된다"를 한 문장에 담았다. 여기서 `should` 는 의무가 아니라 예상.
- 예문: None of the four should crash the page; they degrade to a null or a missing button, so you can copy first and fix in `office.py` afterwards.
- 유사어: fall back to (대체 경로로 넘어가다), the worst case is (구어), fail soft (업계 은어)
- 반의어: crash the page (화면을 죽이다), fail hard (통째로 실패하다)

## "Nothing to commit or push"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`commit and push all` 에 대한 답)
- 맥락: 시킨 일을 할 것이 없을 때 결과부터 한마디로 답하는 자리(작업 보고).
- 한국어: 커밋할 것도 push 할 것도 없습니다
- 설명: `There is` 를 뺀 명사구 한 덩이로 답을 열고 콜론 뒤에 근거 셋을 댄다. 그중 `main has no commits ahead of origin/main` 의 `ahead of` 는 git 이 쓰는 말 그대로("원격보다 앞선 커밋"). 반대는 `behind`. 마지막의 `leftover worktrees` 는 "치우지 않고 남은".
- 예문: Nothing to commit or push: the working tree is clean, `main` has no commits ahead of `origin/main`, and there are no leftover worktrees.
- 유사어: Everything is already pushed (평이), You're all caught up (구어), The branch is up to date with the remote (git 문구)
- 반의어: You have unpushed commits (push 안 한 커밋이 있다)

## "Both halves are on purpose."
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 질문이 두 가지를 한꺼번에 물었을 때 "둘 다 의도한 것"이라고 먼저 답하는 자리(구어).
- 한국어: 두 부분 다 일부러 그렇게 한 겁니다
- 설명: 질문은 `anonymous` 와 404 를 한 문장에 묶어 `is that on purpose?` 라고 물었다. 답은 그것을 `both halves` 로 쪼개 받고 질문의 `on purpose` 를 그대로 돌려준다. 묻는 쪽 낱말을 되받으면 답이 질문에 정확히 붙는다. 이어지는 두 소제목은 같은 뜻을 `by design`, `a deliberate mapping` 으로 바꿔 쓴다.
- 예문: Both halves are on purpose.
- 유사어: Both are intentional (중립), Both are by design (설계를 강조), Neither is a bug (부정으로 뒤집기)
- 반의어: Neither was intended (둘 다 의도한 게 아니다), That's a bug (그건 버그다)

## "depends on a number I can't see from here"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 판단에 필요한 자료가 내 손에 없다고 밝히며 답의 한계를 그을 때(진단·리뷰).
- 한국어: 여기서는 볼 수 없는 숫자에 달려 있다
- 설명: 주어가 `Whether the 404s are harmless` 라는 명사절. "무해한지는 ~에 달렸다"를 그대로 옮긴 꼴이다. `a number I can't see from here` 는 관계대명사를 뺀 관계절이고 `from here` 는 "코드만 읽는 내 자리에서는". 모른다는 말을 "모른다" 대신 "무엇이 있으면 안다"로 한다.
- 예문: Whether the 404s are *harmless* depends on a number I can't see from here.
- 유사어: I can't tell without the logs (평이), That hinges on data I don't have (격식), It comes down to how many there are (구어)

## "one bucket for every cookie-less visitor, not one person"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 로그의 한 이름이 사람 하나가 아니라 묶음임을 바로잡을 때(로그 해석).
- 한국어: 쿠키 없는 방문자 전부를 담는 통 하나이지 사람 한 명이 아니다
- 설명: `bucket` 은 분류해 담는 통. 통계·로그에서 "한 묶음"을 가리킨다. `A, not B` 로 오해할 만한 읽기를 바로 옆에서 지운다. `-less` 를 붙인 `cookie-less` 는 즉석에서 만든 형용사인데 뜻이 바로 통한다(`password-less`, `server-less`).
- 예문: It is one bucket for every cookie-less visitor, not one person.
- 유사어: a catch-all id (무엇이든 받아 주는 id), a shared label (공용 이름표), an umbrella name (우산 이름)

## "It is not a missing route and not an outage."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 걱정할 만한 두 가지 가능성을 한 문장으로 지워 줄 때(장애 여부 설명).
- 한국어: 라우트가 없는 것도 아니고 장애도 아닙니다
- 설명: `not A and not B` 로 `not` 을 두 번 쓴다. `neither A nor B` 보다 구어에 가깝고 두 부정이 따로따로 또렷하다. 앞 문장(`a 404 means the tool was reachable and refused that one path`)이 "무엇인지"를 말했으니 이 문장은 "무엇이 아닌지"를 맡는다. `outage` 는 서비스가 통째로 내려간 상태.
- 예문: So a 404 means the tool was reachable and refused that one path. It is not a missing route and not an outage.
- 유사어: It's neither a routing bug nor downtime (격식), Nothing is down (구어)

## "404 blames the file, 503 blames the tool or network"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 상태 코드 두 개가 각각 무엇을 원인으로 가리키는지 대비해 설명할 때(설계 근거).
- 한국어: 404 는 파일 탓, 503 은 장비나 네트워크 탓
- 설명: 숫자가 주어 자리에 앉아 `blame` 을 한다. 무생물 주어에 사람 동사를 주는 의인화인데, 같은 동사를 되풀이한 두 절을 쉼표로만 이어서 대비가 선다. 앞의 `The 404/503 split is what makes the log readable` 은 `what` 절로 "바로 그것이 ~하게 한다"를 강조한 꼴.
- 예문: The 404/503 split is what makes the log readable: 404 blames the file, 503 blames the tool or network.
- 유사어: 404 points at the file (같은 그림, 약한 어감), 404 means the file is the problem (평이)

## "would also land as 404"
- 레지스터: technical, conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 다른 원인도 같은 결과로 떨어진다는 한계를 덧붙일 때(로그 해석의 주의점).
- 한국어: 그것도 404 로 떨어진다
- 설명: `land as X` 는 여러 갈래가 흘러가다 X 라는 칸에 내려앉는다는 그림. `would` 는 "그런 일이 생긴다면"이라는 가정을 싣는다. 문장 끝의 `not only a truly missing file` 이 "진짜 없는 파일만 그런 게 아니다"를 붙인다.
- 예문: `ftplib.error_perm` covers every 5xx FTP reply, so a permission refusal on the file would also land as 404, not only a truly missing file.
- 유사어: would also show up as 404 (눈에 보이는 쪽), would also map to 404 (대응 관계를 강조), would end up as 404 (구어)

## "which points to a stale `office.py` copy"
- 레지스터: professional, technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 증상을 보고 가장 그럴듯한 원인을 지목할 때(진단 보고, 문어).
- 한국어: 그렇다면 묵은 `office.py` 사본이 원인으로 보인다
- 설명: `point to X` 는 증거가 X 쪽을 가리킨다는 말. 단정(`is caused by`)보다 한 발 물러나 있다. 쉼표 뒤의 `which` 는 낱말 하나가 아니라 앞 절 전체(버그가 돌아왔다는 사실)를 받는다. `stale` 은 한때 맞았으나 갱신되지 않은 것.
- 예문: The cond-sidecar directory bug from 2026-08-10 is back, which points to a stale `office.py` copy.
- 유사어: which suggests (더 조심스러움), which indicates (격식), which smells like (구어, 감으로 짚을 때)
- 반의어: which rules out (그 가능성을 지운다)

## "That field doesn't narrow it down"
- 레지스터: conversational, professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`error_name is Not Found.` 에 대한 답)
- 맥락: 상대가 준 단서가 후보를 줄여 주지 못한다고 말할 때(디버깅 대화).
- 한국어: 그 필드로는 범위가 좁혀지지 않는다
- 설명: `narrow it down` 은 후보를 줄여 나간다는 구동사. 대명사 `it` 은 가운데에 끼운다. 주어를 `That field` 로 잡아서 상대의 답이 틀렸다는 말이 되지 않는다. 쓸모가 없는 쪽은 필드다. 콜론 뒤에 `is just the HTTP status phrase, not the reason` 으로 이유를 바로 댄다.
- 예문: That field doesn't narrow it down: `error_name` is just the HTTP status phrase, not the reason.
- 유사어: That doesn't tell us much (구어), That doesn't help distinguish them (격식), That's not conclusive (보고서)
- 반의어: That settles it (그걸로 결론이 난다), That pins it down (그걸로 딱 짚인다)

## "So the earlier reading stands"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`error_name is Not Found.` 에 대한 답)
- 맥락: 새 정보를 검토한 뒤에도 앞서 내린 해석이 유효하다고 정리할 때(분석 보고).
- 한국어: 그러니 앞의 해석은 그대로다
- 설명: `stand` 는 "서 있다"에서 "여전히 유효하다"로 넓어진 자동사(`the offer stands`, `the record still stands`). `reading` 은 읽는 행위가 아니라 "해석". 내 주장이 맞았다고 말하는 문장인데 주어가 `I` 가 아니라 `the reading` 이어서 우기는 느낌이 없다.
- 예문: So the earlier reading stands: on `/api/msr-image` a 404 can only come from the tool's FTP refusing the file with a 550.
- 유사어: So what I said before still holds (평이), My earlier conclusion is unchanged (격식), Same answer as before (구어)
- 반의어: That changes things (그러면 얘기가 달라진다), I take that back (그 말은 취소한다)

## "To tell A from B, the useful columns are …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`error_name is Not Found.` 에 대한 답)
- 맥락: 두 가지 가능성을 가르려면 무엇을 봐야 하는지 안내할 때(진단 절차).
- 한국어: A 와 B 를 가려내려면 볼 만한 열은 …
- 설명: `tell A from B` 는 "A 와 B 를 구별하다". `tell` 이 "말하다"가 아니라 "알아보다"로 쓰인다(`I can't tell them apart`). 원문은 A 와 B 자리에 따옴표 친 상황 이름을 넣었다. 문두 목적구 뒤에 주절이 `the useful columns are:` 로 와서 목록을 연다.
- 예문: To tell "old purged images" from "something is broken", the useful columns are how many there are and how clustered they are. (작성)
- 유사어: To distinguish A from B (격식), To figure out which it is (구어), To separate A from B (분리의 그림)

## "a handful across old MSRs is normal"
- 레지스터: conversational
- 출처: transcript:skewnono-v3-nuxt [assistant] (`error_name is Not Found.` 에 대한 답)
- 맥락: 적은 수로 흩어져 있으면 정상이라고 기준을 줄 때(로그 판독 요령).
- 한국어: 오래된 MSR 여기저기에 몇 건 있는 정도면 정상
- 설명: `a handful` 은 한 줌, 곧 "몇 개 안 되는". 뒤에 `of 404s` 가 생략됐다. `across` 가 "여러 곳에 걸쳐 흩어져"를 맡아서 소제목의 `how clustered`(얼마나 몰려 있나)와 맞선다. 단수 취급해서 동사는 `is`. 세미콜론 뒤의 `every image of one MSR or one tool is not` 은 `normal` 을 생략한 대구.
- 예문: A handful across old MSRs is normal; every image of one MSR or one tool is not.
- 유사어: a few scattered ones (평이), the odd 404 here and there (구어), sporadic failures (격식)
- 반의어: a flood of them (쏟아지듯 많은), every single request (요청마다 전부)

## "the log alone can't answer this"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`error_name is Not Found.` 에 대한 답)
- 맥락: 주어진 자료만으로는 결론을 낼 수 없다고 선을 그을 때(분석의 한계 고지).
- 한국어: 로그만으로는 답이 나오지 않는다
- 설명: 명사 뒤의 `alone` 은 "~만으로는". 같은 답에 `from the status code alone` 도 나온다. 어제 고른 `visible from the hunk alone` 과 같은 쓰임. 주어가 `the log` 여서 "내가 모른다"가 아니라 "이 자료가 답을 못 준다"가 되고 다음 문장 `In that case, open one of the failing images …` 가 대안을 댄다.
- 예문: If the rows don't carry the query string, the log alone can't answer this.
- 유사어: the log isn't enough on its own (평이), you can't tell from the log by itself (구어), the log is inconclusive (격식)

## "I only read the code; I have not seen the log rows themselves."
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt [assistant] (`/api/msr-image` 404 질문에 대한 답)
- 맥락: 답의 근거가 어디까지인지 밝혀 둘 때(분석 끝에 붙이는 단서).
- 한국어: 저는 코드만 읽었고 로그 행 자체는 보지 못했습니다
- 설명: 세미콜론이 "한 것"과 "하지 않은 것"을 나란히 세운다. 앞은 단순과거(`read`, 발음은 /red/)로 끝낸 일을, 뒤는 현재완료 부정으로 "아직도 못 본 상태"를 말한다. `themselves` 는 "로그에 대한 설명 말고 로그 그 자체"를 강조하는 재귀대명사.
- 예문: I only read the code; I have not seen the log rows themselves.
- 유사어: This is based on the code alone (근거를 주어로), I'm going off the code here (구어), I haven't verified this against the actual logs (격식)

## "passed on the numbers"
- 레지스터: conversational, technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 수치로는 통과했지만 눈으로 볼 것이 남았다고 구분해 보고할 때(진행 상황 한 줄).
- 한국어: 숫자상으로는 통과
- 설명: `on the numbers` 는 "측정값 기준으로는". 괄호 안에 그 숫자들(`640×360`, `0 console errors`)을 늘어놓고 세미콜론 뒤에 `just locating the screenshot to eyeball the layout before committing` 을 붙여 "눈으로 보는 확인은 아직"임을 알린다. 통과의 범위를 스스로 좁힌 표현.
- 예문: Browser check passed on the numbers (popup image renders 640×360 at its natural 640×360, zip link present, 0 console errors); just locating the screenshot to eyeball the layout before committing.
- 유사어: passes on paper (서류상으로는), the metrics check out (수치는 맞는다), numerically it's fine (형용사 쪽)
- 반의어: looks right to the eye (눈으로 보기에 맞다)

## "dropped out of the viewer"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt [assistant] (작업 중 진행 보고)
- 맥락: 특정 조작에서 화면이 뷰어 밖으로 빠져 버리는 버그를 한 줄로 적을 때(버그 보고).
- 한국어: 뷰어에서 튕겨 나갔다
- 설명: `drop out of X` 는 X 에서 빠져나오다(`drop out of school`). 원문은 대시 사이에 버그 한 문장을 통째로 끼웠다. 주어는 `Tab through an image type with no images` 라는 긴 덩어리인데 `Tab` 을 동사로 쓴 동명사 꼴에서 `-bing` 을 줄인 메모체다. 앞의 `fixing one gap` 이 "구멍 하나를 메우는 중"이라고 먼저 알린다.
- 예문: Arrows and keys work; fixing one gap — Tab through an image type with no images dropped out of the viewer — and re-testing the full Tab cycle.
- 유사어: kicked you back to the list (구어), exited the viewer (중립), fell out of image mode (비슷한 그림)
- 반의어: stayed in the viewer (뷰어에 남았다)

## "times out at 25 s with no partial output"
- 레지스터: technical
- 출처: transcript:skewnono-v3-nuxt (browser-verify 스킬 문서)
- 맥락: 도구가 기다리다 실패할 때 아무 단서도 남기지 않는다는 함정을 적을 때(운영 메모).
- 한국어: 25초에 타임아웃되고 중간 출력은 하나도 없다
- 설명: `time out` 은 동사(두 단어), `timeout` 은 명사(한 단어). `at 25 s` 가 시점을, `with no partial output` 이 "그때까지 얻은 것도 못 받는다"를 붙인다. 그래서 뒤 문장이 `so wait on a string the mock is guaranteed to emit` 으로 이어진다. 실패하면 단서가 없으니 확실한 것만 기다리라는 흐름.
- 예문: `wait --text` times out at 25 s with no partial output, so wait on a string the mock is guaranteed to emit, not on one branch of it.
- 유사어: gives up after 25 s and prints nothing (구어), fails silently after 25 s (조용히 실패)
- 반의어: streams output as it goes (진행하면서 출력을 흘려 준다)

## "Merge, don't overwrite"
- 레지스터: technical, professional
- 출처: transcript:skewnono-v3-nuxt (leave-office 스킬 문서)
- 맥락: 기존 내용을 지우지 말고 합치라는 규칙을 제목 한 줄로 걸 때(지시문 소제목).
- 한국어: 덮어쓰지 말고 합쳐라
- 설명: `Do X, don't Y` 는 명령문 둘을 쉼표로 붙인 표어 틀이다(`Show, don't tell`). 접속사 없이 붙여야 구호처럼 들린다. 바로 아래 줄이 `This is the point of the skill.` 이어서 이 제목이 스킬의 존재 이유임을 밝힌다.
- 예문: When you update the open-jobs file, merge, don't overwrite. (작성)
- 유사어: Append, don't replace (덧붙이는 쪽), Update in place (제자리에서 갱신), Preserve what's there (있는 것을 지켜라)
- 반의어: Start from a clean slate (백지에서 시작하다)

## "must keep showing up until it is actually done"
- 레지스터: professional, conversational
- 출처: transcript:skewnono-v3-nuxt (leave-office 스킬 문서)
- 맥락: 끝나지 않은 일이 목록에서 슬그머니 사라지면 안 된다고 요구할 때(도구 설계 원칙).
- 한국어: 정말 끝날 때까지 계속 목록에 떠야 한다
- 설명: `keep -ing` 는 "계속 ~하다", `show up` 은 "나타나다". `actually` 가 "끝났다고 적힌 것"과 "실제로 끝난 것"을 가른다. 주어 `A job left untouched for days` 는 `that has been` 을 줄인 분사구가 뒤에서 꾸민다. `must` 는 규칙의 세기.
- 예문: A job left untouched for days must keep showing up until it is actually done.
- 유사어: must stay on the list until it's really finished (평이), shouldn't silently fall off (부정으로 뒤집기), must persist until closed (격식)
- 반의어: quietly drop off the list (조용히 목록에서 빠지다)

## "If you're tempted to list something finished, it belongs in …"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (leave-office 스킬 문서)
- 맥락: 하고 싶어질 실수를 미리 짚고 올바른 자리를 알려 줄 때(지시문·가이드).
- 한국어: 끝난 일을 적고 싶어지면, 그건 ~에 갈 것이다
- 설명: `be tempted to` 는 "~하고 싶은 유혹을 느끼다". 금지(`Do not list finished work`) 대신 읽는 사람의 충동을 먼저 알아주는 말투다. `belong in X` 는 "X 가 제자리". `something finished` 는 `-thing` 뒤에 형용사가 오는 어순.
- 예문: If you're tempted to list something finished, it belongs in the journal/today-log, not here.
- 유사어: If you feel like adding …, put it in … instead (구어), Resist the urge to … (더 단호), Finished work goes in … (평서 규칙)

## "terse and forward-looking"
- 레지스터: professional
- 출처: transcript:skewnono-v3-nuxt (leave-office 스킬 문서)
- 맥락: 문서의 문체를 두 낱말로 주문할 때(작성 지침).
- 한국어: 짧게, 그리고 앞으로 할 일 중심으로
- 설명: `terse` 는 군말 없이 짧은. `concise` 보다 더 깎아 낸 느낌이고 때로는 퉁명스럽다는 뜻도 된다. `forward-looking` 은 지나간 일이 아니라 다음에 할 일을 본다는 뜻. 형용사 둘이 동사 `Write` 뒤에서 방식을 말한다. 뒤 문장 `this is a launchpad, not a diary` 가 같은 주문을 비유로 되풀이한다.
- 예문: Write in English, terse and forward-looking.
- 유사어: short and action-oriented (평이), brief and to the point (구어), concise and prospective (격식)
- 반의어: wordy and backward-looking (장황하고 지난 일 중심인), a blow-by-blow account (시시콜콜한 경과 기록)
