# 2026-09-22 — 새 표현

> repo 문서 6건(equipment-data-map 통합 아키텍처·성능 제안·wiki-generator·저장소 목적·세션 저널, auto_recipe_creator align 보정 개선안)은 본문이 한국어다. 거기서는 한국어 문장에 그대로 박힌 `append-only` 하나만 골랐다. 나머지 25개는 transcript 의 어시스턴트 영어에서 나왔다(auto-recipe-creator 16, skewnono 9). 노트에 이미 있는 `the tempting fix`, `fail loudly`, `momentum is cheapest there`, `tee up a concrete restart`, `a job at risk of being forgotten`, `dive straight in`, `Keep it scannable.`, `reach for`, `not retroactive`, `go stale`, `the behaviour is unchanged, only the label is broader` 는 뺐다. back-to-office·browser-verify·agent-browser·journal 스킬 본문은 앞선 날에 다룬 글이라 건너뛰었다.

## "has zero consumers"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 파싱은 되는데 읽어 가는 코드가 하나도 없는 필드를 조사 보고나 리뷰에서 짚을 때(기술 채팅·문서)
- 한국어: 쓰는 곳이 하나도 없다
- 설명: 원문은 `` `cond.scope` is parsed (`CondInfo.scope`, `is_om`/`is_sem`) and has zero consumers in the correction path — grep finds it only in `verify_success_gather.py` and debug scripts. `` `consumer` 는 값을 읽어 가는 쪽 코드다. `nobody uses it` 보다 기술적이고 `zero` 로 개수를 박아 grep 으로 확인했다는 인상까지 준다. 뒤에 붙은 `in the correction path` 가 범위를 좁힌다. 다른 곳에서는 쓰일지 몰라도 이 경로에서는 아무도 안 읽는다는 말.
- 예문: The `retry_limit` option is still parsed from the config, but it has zero consumers since the scheduler rewrite.
- 유사어: is unused (평이), nothing reads it (구어), is dead code (더 단정적, 지울 대상으로 봄)
- 반의어: is load-bearing (많은 코드가 기대고 있다)

## "was being thrown away"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 이미 파싱·계산해 둔 값을 쓰지 않고 흘려 버리고 있었다고 짚을 때(버그 조사·리뷰 구어)
- 한국어: (멀쩡한 값이) 버려지고 있었다
- 설명: 원문은 `` It's sitting in the `cond` local variable inside `load_template` and was being thrown away. `` 앞 절의 현재진행 `It's sitting in …` 은 값이 지금도 변수 안에 멀뚱히 앉아 있는 그림을 그린다. 뒤 절 `was being thrown away` 는 과거진행 수동태로 "지금껏 계속 버려져 왔다". 누가 버렸는지는 중요하지 않고 값의 처지가 초점이라 수동태가 어울린다.
- 예문: The parser already computes a line number for each error, but it was being thrown away before the message reached the user.
- 유사어: be discarded (격식), go unused (중립, 버린다는 능동성이 없다), get dropped on the floor (구어, 흘려버리다)
- 반의어: be put to use

## "worse than the gap"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 쉬워 보이는 수정안이 원래 빈틈보다 더 위험하다고 설계 판단을 밝힐 때(리뷰·설계 근거)
- 한국어: (그렇게 메우는 편이) 빈틈을 그냥 두는 것보다 나쁘다
- 설명: 원문은 `` The tempting fix — let cond override `key_type` — is worse than the gap. `` `the tempting fix` 는 노트에 이미 있으니 비교 대상 `the gap` 을 보자. 고칠 대상을 `the problem` 이 아니라 `the gap`(빠진 부분)이라 불러 크기를 "아쉬운 정도"로 낮춰 두고 수정안이 그보다도 나쁘다고 비교한다. 대시 사이에는 수정안을 명령문 꼴로 짧게 끼워 넣었다.
- 예문: A retry here would hide real outages, and a retry that hides outages is worse than the gap it closes.
- 유사어: the cure is worse than the disease (관용구), do more harm than good (평이), make things worse (구어)
- 반의어: a strict improvement

## "flip one without the other"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 짝으로 맞아야 하는 두 값을 한쪽만 바꾸면 어긋난다고 경고할 때(코드 리뷰)
- 한국어: 하나만 바꾸고 다른 하나는 그대로 두다
- 설명: 원문은 `` Flipping one without the other gives you a template labeled `sem` filed under `"OM"`, which fails silently instead of loudly. `` `flip` 은 스위치나 값을 뒤집는 동작. 동명사 `Flipping …` 을 주어로 세우고 `gives you` 로 결과를 붙였다. 결과가 버그인데 "준다"고 하는 건 구어의 반어적 쓰임이다. `one … the other` 는 둘 중 하나와 나머지 하나를 가리키는 짝이라 셋 이상이면 `the others` 로 바뀐다.
- 예문: The client and the server both hard-code the feature flag, and flipping one without the other breaks every request.
- 유사어: change A but not B (평이), update them out of step (격식), leave one behind (구어)
- 반의어: change both in lockstep

## "labeled X, filed under Y"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 이름표와 실제 분류 위치가 어긋난 데이터를 서류함에 빗대 설명할 때(버그 설명)
- 한국어: 이름표는 X 인데 Y 칸에 꽂혀 있다
- 설명: 위와 같은 문장의 `` a template labeled `sem` filed under `"OM"` `` 이다. 과거분사 둘이 `template` 을 뒤에서 꾸민다(`a template (that is) labeled … and filed under …`). `file under` 는 서류를 어느 폴더에 꽂아 두는 동작이라 dict 의 키를 서류함에 빗댔다. 사람끼리도 `I'd file that under "nice to have"`(그건 "있으면 좋은 것"으로 치겠다)처럼 자주 쓴다.
- 예문: The bug report was labeled urgent but filed under the wrong team, so nobody picked it up for a week.
- 유사어: tagged X but stored as Y (평이), misfiled (한 단어), in the wrong bucket (구어)
- 반의어: filed where it belongs

## "add the check, not the override"
- 레지스터: professional, technical
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 값을 강제로 덮어쓰는 대신 어긋나면 경고만 내는 쪽을 골랐다고 보고할 때(변경 보고)
- 한국어: 덮어쓰기 말고 검사만 넣다
- 설명: 원문은 `` So I added the check, not the override — `templates.py`: `` `A, not B` 틀로 한 일과 일부러 안 한 일을 한 번에 말한다. 둘 다 `the` 가 붙은 이유는? 바로 앞 단락에서 거론한 그 검사, 그 override 라서다. 이어지는 `Skipped: cond-driven routing — …` 까지 읽으면 "안 한 것 + 이유"를 남기는 보고 습관이 보인다.
- 예문: I added the check, not the override, so a mismatched config now logs a warning instead of silently changing the route.
- 유사어: warn, don't rewrite (원칙을 명령형으로), flag it instead of fixing it (구어), detect rather than correct (격식)
- 반의어: force the value

## "we have no evidence X ever breaks"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 실제로 깨진 적 없는 가정을 굳이 고치지 않는 근거를 댈 때(설계 판단·리뷰 답변)
- 한국어: X 가 깨진 적이 있다는 증거가 없다
- 설명: 원문은 `` Skipped: cond-driven routing — we have no evidence the `IMAP000N` convention ever breaks. `` 접속사 `that` 이 빠진 동격 명사절이다(`evidence (that) …`). `ever` 는 "한 번이라도"라 부정 맥락에서 증거의 문턱을 가장 낮게 잡는다. 곧이어 `If that WARNING fires at the office, …` 로 증거가 생기면 무엇을 할지 조건을 걸어 두었다. YAGNI 를 말로 풀면 이런 모양.
- 예문: We have no evidence the old date format ever breaks the importer, so I'd rather not add a converter yet.
- 유사어: nothing suggests X (중립), there's no sign that X (구어), we have yet to see X (격식, "아직까지는")
- 반의어: we've seen it break before

## "in both places at once"
- 레지스터: technical, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 짝으로 묶인 두 곳을 반드시 함께 고치라고 후속 작업을 못 박을 때(리뷰·작업 메모)
- 한국어: 두 군데를 한꺼번에
- 설명: 원문은 `` If that WARNING fires at the office, move routing to `cond.scope` in **both** places at once. `` `both` 에 강세를 줘 한 곳만 고치면 앞의 `flip one without the other` 가 된다는 경고를 되살린다. `at once` 는 "즉시"도 되고 "동시에"도 되는데 여기서는 뒤쪽이다. 헷갈릴 자리라면 `at the same time` 이나 `in the same commit` 이 안전하다.
- 예문: The limit is defined in both the API and the worker, so change it in both places at once or the queue will reject valid jobs.
- 유사어: in the same commit (개발 맥락에서 가장 구체적), together (평이), in lockstep (격식·기술)
- 반의어: one at a time

## "stand as written"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 전에 적어 둔 목록·계획이 그 뒤로 바뀐 게 없어 그대로 유효하다고 알릴 때(업무 재개·상태 보고)
- 한국어: 적힌 그대로 유효하다
- 설명: 원문은 `Carryover is 2 days old (2026-09-19) — nothing shipped since, so the office list stands as written.` `stand` 는 "(결정·기록이) 유효하게 남아 있다"는 자동사(`The offer still stands`). 노트에 있는 `stand as reported` 가 보고된 결과를 두고 하는 말이라면 이쪽은 적어 둔 계획을 가리킨다. `as written` 은 `as it was written` 을 줄인 꼴이다.
- 예문: Nobody raised objections at the review, so the migration plan stands as written.
- 유사어: still holds (구어), remains valid (격식), is still good to go (구어, 실행 준비까지 됐다)
- 반의어: needs revising

## "nothing shipped since"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 마지막 기록 이후 배포·반영된 것이 없다고 짧게 상태를 전할 때(스탠드업·채팅)
- 한국어: 그 뒤로 나간 게 없다
- 설명: 같은 문장의 앞부분이다. 문장 끝에 홀로 선 부사 `since` 가 "그때 이후로"(`since then`)를 대신한다. 완전한 문장이라면 `nothing has shipped since` 처럼 현재완료가 맞는데 원문은 대시 뒤 메모체라 조동사를 떨어뜨렸다. `ship` 은 자동사로 "(기능이) 출시되다, 반영되다".
- 예문: The last release went out on Monday and nothing has shipped since, so the bug has to be in that build.
- 유사어: nothing has gone out since (구어), no changes have been deployed since then (격식), it's been quiet since (구어)
- 반의어: a lot has landed since

## "do it or drop it"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 오래 미뤄 둔 사소한 일을 이번에 끝내든 목록에서 빼든 정하자고 할 때(업무 정리 구어)
- 한국어: 하든지, 아니면 버리든지
- 설명: 원문은 `Two at risk: the VLM checklist is a 30-second confirmation that's been carried three weeks — do it or drop it.` 두운(d–d)을 맞춘 명령문 둘을 `or` 로 이어 선택지를 둘로 좁힌다. "계속 미루기"라는 세 번째 길을 막는 말이라 목록 정리에 제격이다. `that's been carried three weeks` 는 현재완료 수동태 + 기간으로 "3주째 이월되고 있다".
- 예문: That ticket has been in the backlog since March, so this sprint we either do it or drop it.
- 유사어: make a call on it (평이), fish or cut bait (미국 관용구), commit to it or cut it (구어)
- 반의어: keep kicking it down the road

## "a standing watch item"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 일정을 잡을 수 없고 사건이 생기길 기다려야 하는 일을 할 일 목록과 떼어 둘 때(업무 관리)
- 한국어: 상시로 지켜볼 항목
- 설명: 원문은 `Ticket 18 can't be *scheduled*, it waits on a real alarm, so it will keep aging; consider moving it out of "do first" into a standing watch item.` 형용사 `standing` 은 "상시의, 늘 유효한"(`a standing order`, `a standing meeting`). `watch item` 은 처리 대상이 아니라 관찰 대상이라는 구분이다. `move it out of A into B` 로 목록 사이를 옮기는 동작을 그렸다.
- 예문: We can't fix the flaky payment test on a schedule, so let's make it a standing watch item and dig in whenever it fails.
- 유사어: something to keep an eye on (구어), an ongoing watch (격식), a tripwire (기술, 걸리면 알림이 오는 것)
- 반의어: an action item (당장 할 일)

## "keep aging"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 처리할 수 없는 조건 탓에 목록의 항목이 계속 묵어 간다고 말할 때(백로그 점검)
- 한국어: (항목이) 계속 묵어 간다
- 설명: 같은 문장의 `so it will keep aging`. 동사 `age` 는 "나이 들다"인데 백로그·재고·계정처럼 오래될수록 나빠지는 대상에 두루 쓴다(`aging inventory`, `ticket aging`). `keep + -ing` 는 멈추지 않고 이어짐. 원문의 `can't be scheduled, it waits …` 는 쉼표로 두 문장을 이은 구어체(comma splice)라 글에서는 세미콜론이나 `because` 로 잇는 편이 낫다.
- 예문: If nobody owns these alerts, they'll just keep aging in the queue until someone mutes them.
- 유사어: pile up (구어, 쌓이다), sit untouched (평이), go stale (노트에 있음, 정보가 낡다)
- 반의어: get cleared

## "the longer it sits, the more work stacks on an unproven base"
- 레지스터: professional
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 검증 안 된 코드를 서둘러 확인해야 하는 이유를 쌓이는 비용으로 설득할 때(우선순위 제안)
- 한국어: 오래 둘수록 검증 안 된 토대 위에 일이 더 쌓인다
- 설명: 원문은 `` …, and `a89a852` is unverified on real equipment — the longer it sits, the more work stacks on an unproven base. `` `the + 비교급 …, the + 비교급 …` 은 "~할수록 더 ~하다". 두 절 모두 주어와 동사를 온전히 갖춰 리듬이 산다. `sit` 은 "(손대지 않은 채) 놓여 있다", `stack on` 은 "위에 쌓이다". `unproven base` 는 확인 안 된 토대 위에 집을 올리는 건축 비유다.
- 예문: Let's review the schema change today; the longer it sits, the more work stacks on an unproven base.
- 유사어: we're building on sand (관용 비유), every day we wait adds risk (평이), the cost of delay compounds (격식)
- 반의어: verify it before we build on it

## "bring home (the numbers)"
- 레지스터: conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 현장·사무실에서 돌려 보고 결과를 챙겨 오라고 할 때(업무 지시 구어)
- 한국어: (결과를) 챙겨서 가져오다
- 설명: 원문은 `` Next action, verbatim from the carryover: `git pull` → `a89a852`, run `manual_align_correction.py` with the DFT placed (a) at a corner of the first frame, (b) ~1 FOV away. Bring home: `` 사무실에서 실행하고 집으로 로그를 들고 오는 사용자의 작업 방식을 그대로 옮긴 말이다. 콜론 뒤 목록으로 챙길 것을 나열했다. 관용구 `bring home` 은 "(요점을) 절실히 깨닫게 하다"(`bring home the point`)나 "생활비를 벌다"(`bring home the bacon`)로도 쓰이니 목적어로 뜻을 가린다.
- 예문: When you run the test at the plant, bring home the full log and the two screenshots, not just the pass/fail line.
- 유사어: bring back (평이), report back with (업무 격식), grab (구어, "챙겨 와")
- 반의어: leave behind

## "if it misbehaves"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] auto-recipe-creator
- 맥락: 새 기능이 이상하게 굴 때 끄는 방법(롤백)을 미리 안내할 때(배포 노트)
- 한국어: 이상하게 굴면, 기대와 다르게 동작하면
- 설명: 원문은 `` Rollbacks if it misbehaves: wasted hint moves → `ALIGN_FAIL_PARTIAL_HINT_MOVES=0`; wrong auto-OK after search → `ALIGN_FAIL_SEARCH_CONTINUE=0`. `` `misbehave` 는 원래 아이가 말을 안 듣는다는 동사인데 코드·기계에도 쓴다. `fail` 과 달리 멈추지는 않고 엉뚱한 일을 한다는 어감이다. 원문처럼 "증상 → 끄는 스위치"를 짝지어 두면 읽는 사람이 곧바로 대응한다.
- 예문: The new cache is behind a flag, so if it misbehaves in production you can turn it off without a deploy.
- 유사어: acts up (구어), goes wrong (평이), behaves unexpectedly (격식)
- 반의어: behaves as expected

## "trace it end to end"
- 레지스터: technical, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 기능이 입력부터 화면까지 어떻게 흐르는지 코드를 따라가 확인했다고 보고할 때(조사 보고)
- 한국어: 처음부터 끝까지 따라가 보다
- 설명: 원문은 `Traced it end to end. Here is what the button does and why it exists.` 주어 `I` 를 떨어뜨린 보고체다. `end to end` 는 부사로 쓸 때 하이픈이 없고 명사 앞 형용사로 쓸 때 하이픈을 넣는다(`an end-to-end test`). 뒤 문장 `Here is what … and why it exists` 가 결론을 예고하는 다리 노릇을 한다.
- 예문: I traced the request end to end, and the timeout comes from the proxy, not the database.
- 유사어: follow it all the way through (구어), walk the code path (기술), trace it from input to output (평이)
- 반의어: spot-check (일부만 확인하다)

## "sounds like a tautology"
- 레지스터: professional, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 이름이나 문구가 문맥상 뻔한 말을 되풀이해 무의미하게 들린다고 지적할 때(UX 문구 리뷰)
- 한국어: 동어반복처럼 들린다
- 설명: 원문은 `It filters for "sites that have an image", but on a screen titled 이미지 갤러리 it sounds like a tautology.` `tautology` 는 "동어반복, 하나 마나 한 말". 이미지 갤러리에서 "이미지 있음"처럼 문맥이 이미 참으로 만든 말을 다시 할 때 쓴다. 바로 앞 문장 `The label describes the entry, not the gallery.` 가 이유를 먼저 대 두었다. `on a screen titled …` 의 `titled` 는 과거분사로 "~라는 제목이 붙은".
- 예문: On a page called Settings, a tab named "General Settings" sounds like a tautology.
- 유사어: redundant (가장 흔함), says the same thing twice (평이), goes without saying (구어, "말할 필요도 없다")
- 반의어: informative

## "Two cheap fixes if you want one"
- 레지스터: conversational, professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 질문에 답한 뒤 원하면 해 줄 가벼운 해결책을 곁들여 제안할 때(리뷰 답변·채팅)
- 한국어: 원하시면 싸게 고칠 방법이 두 가지 있어요
- 설명: 원문은 `Two cheap fixes if you want one:` 동사 없는 명사구 머리말이다. 여기서 `cheap` 은 질이 낮다는 게 아니라 손이 덜 간다는 말. `if you want one` 으로 고칠지 말지는 상대 몫이라는 여지를 남겼고 둘 중 하나만 고르면 된다는 뜻도 `one` 에 담았다. 단락은 `Neither is applied; this was a question, not a change request.` 로 닫힌다.
- 예문: Two cheap fixes if you want one: cache the lookup, or move it out of the loop.
- 유사어: A couple of quick options, if you want to change it: (평이), Two low-effort remedies, should you wish to proceed: (격식)
- 반의어: This needs a proper redesign.

## "names the thing it removes"
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 필터·버튼 이름을 남는 것이 아니라 빼는 것으로 짓자고 제안할 때(UX 문구 설계)
- 한국어: (이름이) 빼는 대상을 가리킨다
- 설명: 원문은 `` Rename it to `이미지 없는 site 숨기기` or `이미지 없음 제외`, which names the thing it removes. `` 비제한 관계절 `, which …` 가 앞의 후보 이름을 받는다. 여기서 `name` 은 동사로 "이름으로 가리키다". `the thing it removes` 는 관계대명사가 빠진 접촉절이다. 사용자는 이 조언대로 `rename it to 이미지 없음 제외` 라고 답했다.
- 예문: "Hide archived" works better than "Show active" because it names the thing it removes.
- 유사어: says what it hides (구어), is named after what it filters out (평이), describes the exclusion explicitly (격식)
- 반의어: names what's left

## "This was a question, not a change request."
- 레지스터: professional
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 질문에 답만 하고 아무것도 바꾸지 않았다고 선을 그을 때(에이전트·동료 협업)
- 한국어: 질문이었으니 아무것도 바꾸지 않았어요
- 설명: 원문은 `Neither is applied; this was a question, not a change request. Say which one and I'll do it.` 질문과 요청을 `A, not B` 로 가른다. 과거형 `was` 는 방금 받은 메시지를 가리킨다. 이어지는 `Say which one and I'll do it.` 은 `명령문 + and + will` 조건 구문으로 "골라 주면 하겠다".
- 예문: I only read the logs and didn't restart anything; this was a question, not a change request.
- 유사어: I took this as a question, so I haven't changed anything. (평이), I've treated this as a query rather than a request for changes. (격식)

## "pre-armed"
- 레지스터: technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 필터·옵션이 사용자가 누르기 전부터 켜져 있는 상태를 말할 때(UI 검증 보고)
- 한국어: 미리 켜져 있는
- 설명: 원문은 `With 이상·실패 우선 pre-armed, the queue showed 2 of 22 sites.` `arm` 은 무기나 경보기를 "작동 대기 상태로 두다"는 동사이고 `pre-` 를 붙여 기본값으로 켜 있음을 말한다. `with + 명사 + 과거분사` 는 부대 상황("~가 켜진 채로"). `2 of 22 sites` 는 "22곳 중 2곳"을 짧게 쓰는 보고체다.
- 예문: With the "errors only" filter pre-armed, new users never see the full log and assume nothing is running.
- 유사어: on by default (가장 평이), preselected (UI 용어), enabled out of the box (구어)
- 반의어: opt-in (사용자가 직접 켜야 하는)

## "be live (on the dev server)"
- 레지스터: technical, conversational
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 바꾼 내용이 서버에 반영돼 지금 실제로 보인다고 확인해 줄 때(배포·검증 보고)
- 한국어: (변경이) 반영돼 돌아가고 있다
- 설명: 원문은 `The rename is live on the dev server and the toggle still filters correctly.` 형용사 `live` 는 [laɪv] 로 읽고 "실제로 돌아가는, 반영된"이다. `on the dev server` 로 반영 위치를 밝혀 운영 반영과 헷갈리지 않게 했다. 동사구 `go live` 는 "출시되다".
- 예문: The new pricing page is live on staging, so you can check it before we push it to production.
- 유사어: is up (구어, 서버가 떠 있다), is out (구어, 출시됐다), has been deployed (격식)
- 반의어: is still local only

## "Nothing left to commit."
- 레지스터: conversational, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 커밋해 달라는 요청에 이미 다 커밋돼 있다고 짧게 답할 때(개발 채팅)
- 한국어: 커밋할 게 남아 있지 않아요
- 설명: 원문은 `` Nothing left to commit. The rename was already committed as `31dc3151` and pushed when I made it; the file is clean and main matches origin/main. `` `There is nothing left to commit` 에서 `There is` 를 떨어뜨렸다. `left` 는 과거분사로 "남은", `to commit` 은 `nothing` 을 꾸미는 to부정사다. 곧바로 과거 시제로 이유를 대서 요청을 흘려들은 게 아님을 보인다.
- 예문: Nothing left to commit; the fix went in with yesterday's merge.
- 유사어: All done already. (구어), The tree is already clean. (기술 구어), There are no pending changes. (격식)
- 반의어: You have uncommitted changes.

## "be real in the data"
- 레지스터: professional, technical
- 출처: transcript:[assistant] skewnono-v3-nuxt
- 맥락: 예외처럼 보이는 경우가 실제 데이터에 있다고 근거를 댈 때(설계 설명)
- 한국어: 실제 데이터에 존재한다
- 설명: 원문은 `Image-less sites are real in the data: in the mock, every 20th step is an "empty" row with no image names, and at the office a failed or unmeasured site often has no image file at all.` 형용사 `real` 을 "실재하는"으로 쓰고 `in the data` 로 근거의 출처를 붙였다. 콜론 뒤에 mock 과 현장이라는 증거 둘을 `and` 로 나란히 세웠다. 엣지 케이스가 가상의 걱정이 아니라고 반박할 때 쓰기 좋다.
- 예문: Negative durations are real in the data, because some devices report their end time before their start time.
- 유사어: actually occur in the data (평이), show up in production (구어), are attested in the data set (격식·학술)
- 반의어: purely hypothetical

## "append-only"
- 레지스터: technical
- 출처: repo:equipment-data-map docs/journals/260921/260921_192336_architecture-doc-review-and-office-refresh.md
- 맥락: 기록 파일을 고쳐 쓰지 않고 뒤에 줄만 더하는 방식이라고 설명할 때(설계 문서)
- 한국어: 뒤에 덧붙이기만 하는(수정·삭제 없이)
- 설명: 저널의 `ledger가 append-only이고 awk 검사가 letter별 마지막 done 줄만 본다`에서 한국어 문장 안에 영어 그대로 쓰였다. 복합 형용사라 명사 앞에서는 하이픈을 넣고(`an append-only ledger`) 보어 자리에서도 그대로 쓴다(`The log is append-only.`). "마지막 줄이 이긴다"는 짝 개념 `last write wins` 가 자주 따라다닌다.
- 예문: The audit log is append-only, so a correction goes in as a new line rather than an edit to the old one.
- 유사어: write-once (더 엄격, 한 번 쓰면 끝), an immutable log (격식·기술), add-only (드물게 쓰임)
- 반의어: edited in place
