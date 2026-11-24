# 2026-11-25 — 새 표현

오늘 배치는 pm_notes 에서 UpNote 앱을 다루는 스킬을 만들고 시험한 대화 한 건입니다. 질문도 답도 영어라서 표현은 모두 어시스턴트의 보고문에서 골랐어요. 시험 결과를 알리고, 못 한 것을 못 했다고 밝히고, 틀린 계획을 바로잡는 문장이 많습니다. 내가 쓴 영어 문장은 `coaching.md` 에서 따로 다듬었습니다.

## "come from sources I can't vouch for"
- 레지스터: professional, conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (스킬 검색 결과 보고)
- 맥락: 출처를 믿을 근거가 없다고 선을 그을 때(추천을 거절하는 보고, 동료 사이 중립 격식)
- 한국어: 내가 보증할 수 없는 출처에서 나왔다.
- 설명: `vouch for + 사람/물건` 은 "내 이름을 걸고 괜찮다고 말해 주다"입니다. 부정으로 쓰면 "나쁘다"가 아니라 "내가 확인해 준 적이 없다"여서 단정하지 않고 거리를 둡니다. 전치사 `for` 가 꼭 붙어요.
- 예문: I haven't used that library myself, so I can't vouch for it.
- 유사어: I can't verify these sources (사실 확인 쪽, 격식), I don't know who's behind them (구어), of unknown provenance (문어, 딱딱함)
- 반의어: from a trusted publisher, I can vouch for it

## "well below the bar for a skill worth trusting"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (스킬 검색 결과 보고)
- 맥락: 기준에 한참 못 미친다고 평가할 때(리뷰·채용·도구 선정, 글과 말 모두)
- 한국어: 믿을 만한 스킬의 기준에 한참 못 미친다.
- 설명: `the bar` 는 높이뛰기 가로대에서 온 "합격선"입니다. `below the bar`, `clear the bar`, `raise the bar` 로 묶어 외우면 좋아요. `well` 은 `below` 를 세게 해 주는 부사이고, `worth trusting` 은 `worth + -ing` 로 명사 뒤에서 꾸밉니다.
- 예문: Two stars and no commits in three years is well below the bar for a dependency worth adding.
- 유사어: falls far short of the standard (격식), doesn't make the cut (구어), nowhere near good enough (가장 구어)
- 반의어: clears the bar, meets the standard

## "A broader search … turned up nothing relevant"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (스킬 검색 결과 보고)
- 맥락: 찾아봤지만 쓸 만한 것이 안 나왔다고 보고할 때(조사 결과, 중립 격식)
- 한국어: 범위를 넓혀 찾아봐도 관련 있는 것은 나오지 않았다.
- 설명: `turn up` 은 "찾다 보니 나오다"입니다. 주어가 사람이 아니라 `search` 여서 검색이 결과를 내놓는 그림이 돼요. 같은 대화 뒤쪽에 `It also turned up several community MCP servers` 처럼 긍정으로도 나옵니다. `nothing relevant` 처럼 `-thing` 뒤에는 형용사가 뒤에 붙습니다.
- 예문: A quick search of the issue tracker turned up nothing relevant, so I opened a new ticket.
- 유사어: found nothing relevant (평이), came up empty (구어), yielded no relevant results (격식·논문)
- 반의어: turned up several hits

## "editing existing notes still means driving the app's UI"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (Codex 조사 요약)
- 맥락: API 가 없어 화면을 직접 조작해야 한다고 설명할 때(자동화·테스트 문서)
- 한국어: 기존 노트를 고치려면 여전히 앱 화면을 직접 조작해야 한다.
- 설명: `A means B` 는 "A 를 하려면 B 가 따라온다"입니다. `mean` 뒤에 동명사가 오면 "뜻하다"가 아니라 "~을 수반하다"예요(`mean to do` 는 "~할 작정이다"). `drive the UI` 는 사람이 아닌 프로그램이 클릭과 입력으로 화면을 모는 것으로, 테스트 자동화에서 굳은 말입니다.
- 예문: Without an API, exporting the report still means driving the web UI with a script.
- 유사어: requires automating the UI (격식), has to go through the screen (구어), relies on GUI automation (기술 문서)
- 반의어: can be done through the API

## "Note IDs come back after all"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (Codex 조사 요약)
- 맥락: 앞에서 안 된다고 했던 것이 알고 보니 된다고 뒤집을 때(구어·보고 제목)
- 한국어: 알고 보니 노트 ID 가 돌아온다.
- 설명: 문장 끝 `after all` 은 "예상과 달리 결국"입니다. 바로 앞 보고에서 "아무것도 돌아오지 않는다"고 했기 때문에 이 한마디로 그 말을 고칩니다. 문장 앞 `After all,` 은 "어쨌든 ~이니까"로 이유를 대는 말이라 뜻이 달라요.
- 예문: The old endpoint is still up after all, so we don't need to migrate this week.
- 유사어: as it turns out (조금 더 서술적), contrary to what I said earlier (격식, 정정임을 밝힘), turns out (구어, 주어 생략)

## "which I'm assuming UpNote picks up as a tag"
- 레지스터: conversational, technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (테스트 노트 안내)
- 맥락: 확인하지 않은 가정을 가정이라고 밝히며 말할 때(시험 보고, 구어)
- 한국어: UpNote 가 태그로 알아챌 것이라고 내가 가정하고 있는 것.
- 설명: 관계절 안에 `I'm assuming` 을 끼운 꼴입니다. `which UpNote picks up as a tag` 라고 단정하지 않고 가정임을 드러내요. `pick up A as B` 는 프로그램이 A 를 B 로 인식해 받아들인다는 뜻입니다. 이 가정은 나중에 틀린 것으로 밝혀졌습니다.
- 예문: The file starts with a shebang line, which I'm assuming the installer picks up as a sign that it's executable.
- 유사어: which I expect UpNote to treat as a tag (조금 격식), which should register as a tag (추측을 `should` 로), which is presumably parsed as a tag (기술 문서)

## "a typo would silently create a stray one"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (시험 결과 정리)
- 맥락: 경고 없이 엉뚱한 것이 생기는 위험을 알릴 때(설계 메모·리뷰)
- 한국어: 오타 하나로 아무 경고 없이 엉뚱한 노트북이 생긴다.
- 설명: `stray` 는 제자리를 벗어나 떠도는 것(길 잃은 개가 `a stray dog`)입니다. `silently` 는 오류나 알림 없이 일어난다는 뜻으로 버그 설명에 자주 붙어요. `would` 는 실제로 일어난 일이 아니라 "그런 일이 생기면"이라는 가정입니다. `one` 은 앞의 `notebook` 을 받습니다.
- 예문: The config loader accepts unknown keys, so a typo would silently create a stray setting that nothing reads.
- 유사어: would create an unwanted one without warning (풀어 쓴 말), would quietly leave an orphan behind (기술 구어), could inadvertently create a duplicate (격식)

## "My tag plan was wrong, and it has left the test notes scattered"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (시험 결과 정리)
- 맥락: 자기 실수와 그 뒤처리 부담을 한 문장으로 인정할 때(사후 보고)
- 한국어: 내 태그 계획이 틀렸고, 그 탓에 테스트 노트가 흩어져 있다.
- 설명: `leave + 목적어 + 형용사/분사` 는 "그 결과 ~한 상태로 남겨 두다"입니다. 앞절은 과거(`was wrong`), 뒷절은 현재완료(`has left`)라서 잘못은 지난 일이고 결과는 지금도 남아 있다는 구분이 시제에 실려요. 변명 없이 `was wrong` 으로 끊는 점도 볼 만합니다.
- 예문: My estimate was wrong, and it has left the team short by two days.
- 유사어: I got the tagging wrong, so the test notes are all over the place (구어), the tagging approach failed, leaving the notes dispersed (격식)

## "That settles both questions"
- 레지스터: conversational, professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (시험 결과 정리)
- 맥락: 상대의 답으로 열려 있던 물음이 다 풀렸다고 받을 때(회의·채팅)
- 한국어: 그걸로 두 가지 물음이 다 정리됐다.
- 설명: `settle` 은 흔들리던 것이 가라앉는 그림이라 논쟁, 의문, 계산에 다 씁니다. `That` 은 방금 들은 답 전체를 받아요. 굳은 말 `That settles it.` 에서 `it` 자리에 구체적인 대상을 넣은 꼴입니다.
- 예문: The benchmark came back twice as fast, which settles the question of whether the rewrite was worth it.
- 유사어: That answers both questions (평이), That clears up both points (모호함이 걷혔다는 쪽), Both points are now resolved (격식)
- 반의어: That leaves both questions open

## "a 21,000-character note goes through uncut"
- 레지스터: technical, conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (긴 노트 시험)
- 맥락: 데이터가 잘리지 않고 끝까지 전달된다고 확인할 때(시험 보고)
- 한국어: 21,000자짜리 노트가 잘리지 않고 그대로 넘어간다.
- 설명: `go through` 는 요청, 결제, 메시지가 막히지 않고 통과한다는 뜻입니다. 뒤에 형용사 `uncut` 을 붙여 "어떤 상태로" 통과했는지 말해요. 숫자와 단위를 하이픈으로 묶어 명사 앞에 두면 단위는 단수(`21,000-character`)입니다.
- 예문: The payment went through, but the receipt email arrived with the last line cut off.
- 유사어: arrives complete (평이, 같은 대화에 나옴), is delivered in full (격식), makes it across intact (구어)
- 반의어: gets cut off, is truncated

## "The skill works as it stands"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (백업 설정 보류)
- 맥락: 더 손대지 않은 지금 상태로도 된다고 말할 때(검토 의견, 글과 말)
- 한국어: 스킬은 지금 상태 그대로 동작한다.
- 설명: `as it stands` 는 "현재 있는 그대로"입니다. 뒤에 "더 고칠 수는 있지만"이 숨어 있어서, 아쉬운 점을 말하기 전후에 자주 놓아요. 주어가 복수면 `as they stand`, 상황 전체를 가리키면 `as things stand` 입니다.
- 예문: The proposal is fine as it stands, though a cost table would make it easier to approve.
- 유사어: as is (짧은 구어·계약 문구), in its current form (격식), the way it is now (가장 평이)
- 반의어: once it's been reworked

## "Both come down to the same thing"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (시험 불가 사유)
- 맥락: 여러 문제의 원인이 하나라고 묶을 때(구어·설명)
- 한국어: 둘 다 따지고 보면 같은 문제다.
- 설명: `come down to` 는 가지를 쳐 내고 남는 알맹이를 가리킵니다. 뒤에 콜론을 찍고 그 한 가지를 바로 말해 주면(`: someone has to unlock the Mac once`) 듣는 사람이 기다리지 않아요. `It all comes down to …` 로도 많이 씁니다.
- 예문: The slow build and the flaky tests both come down to the same thing: the CI machine is out of memory.
- 유사어: both boil down to (구어, 졸여 낸다는 그림), both stem from the same cause (격식), it's the same root cause (기술 보고)

## "test reading and editing in one go"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (시험 불가 사유)
- 맥락: 여러 일을 한 번에 몰아서 하겠다고 할 때(구어, 영국식에 가까움)
- 한국어: 읽기와 고치기를 한 번에 시험하다.
- 설명: `in one go` 는 중간에 끊지 않고 한 차례에 끝낸다는 뜻입니다. 미국식으로는 `in one shot`, `all at once` 가 더 흔해요. `at once` 는 "즉시"로도 읽히므로 "한꺼번에"를 분명히 하려면 `all at once` 나 `in one go` 를 씁니다.
- 예문: Once the server is back, I'll run the migration and the smoke tests in one go.
- 유사어: all at once (평이), in a single pass (기술 문서), in one sitting (앉은 자리에서, 읽기·쓰기에)
- 반의어: one at a time, in stages

## "leave the test notes in place"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (집에서 이어 할 일)
- 맥락: 치우지 말고 그대로 두라고 부탁할 때(작업 지시, 중립 격식)
- 한국어: 테스트 노트를 그 자리에 그대로 두다.
- 설명: `in place` 는 "제자리에"입니다. `leave A in place` 는 건드리지 말라는 뜻이고, `edit in place` 는 새로 만들지 않고 그 자리에서 고친다는 뜻이에요. 같은 대화에 `retyping it in place` 도 나옵니다. `Until then` 으로 기한을 붙여 언제까지인지 밝혔습니다.
- 예문: Please leave the old config in place until the new one has run for a full day.
- 유사어: leave them as they are (평이), don't touch them yet (구어), keep them untouched for now (조금 격식)
- 반의어: clear them out, remove them

## "The copy can be up to an hour old"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (읽기 시험 보고)
- 맥락: 캐시나 백업이 얼마나 뒤처질 수 있는지 한계를 알릴 때(운영 문서)
- 한국어: 사본은 길게는 한 시간 전 것일 수 있다.
- 설명: `up to + 수량` 은 상한이고 `숫자 + old` 는 나이입니다. 사람 나이를 말하는 꼴을 데이터에 그대로 써서 "얼마나 묵었나"를 나타내요. `can be` 는 늘 그렇다는 것이 아니라 그럴 때가 있다는 가능성입니다.
- 예문: The dashboard reads from a cache, so the numbers can be up to five minutes old.
- 유사어: may lag by as much as an hour (지연 쪽에서 본 말), is at most an hour stale (기술 구어), is refreshed hourly (갱신 주기로 바꿔 말함)
- 반의어: is always current, is live

## "which is now out of date"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (읽기 시험 보고)
- 맥락: 문서나 기록이 지금 사실과 안 맞게 됐다고 짚을 때(리뷰·보고)
- 한국어: 그것은 이제 낡은 내용이다.
- 설명: `out of date` 는 서술 자리에서는 띄어 쓰고, 명사 앞에서는 하이픈으로 묶습니다(`an out-of-date note`). 쉼표 뒤 `which` 는 앞 절 전체("노트가 아직 그렇게 말한다")를 받아요. `now` 가 "쓸 때는 맞았다"는 뜻을 살립니다.
- 예문: The README still tells you to install Node 16, which is now out of date.
- 유사어: is no longer accurate (격식), is stale (기술 구어), is outdated (한 단어, 중립)
- 반의어: is up to date, is current

## "any link you made to the old one would no longer point to it"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (요약 노트 교체 보고)
- 맥락: 교체 방식의 부작용을 미리 알릴 때(변경 안내)
- 한국어: 예전 노트로 걸어 둔 링크가 있다면 더는 그 노트를 가리키지 않는다.
- 설명: `any link you made` 는 링크가 있는지 모르는 채로 "있다면 어느 것이든"을 뜻합니다. 그래서 동사도 `would` 예요. `point to` 는 링크, 포인터, 화살표가 가리키는 대상을 말하는 기본 동사입니다. `no longer` 는 일반 동사 앞, 조동사 뒤에 놓입니다.
- 예문: If you rename the branch, any bookmark you saved to the old URL would no longer point to it.
- 유사어: would break (가장 짧음), would become a dead link (결과 쪽), would cease to resolve (격식·기술)
- 반의어: would still point to it, would keep working

## "Two ways around it while you're remote"
- 레지스터: conversational
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (잠금 상태 설명)
- 맥락: 제약을 못 없애도 돌아갈 길이 있다고 말할 때(구어·안내 제목)
- 한국어: 원격에 있는 동안 이를 피해 가는 방법 두 가지.
- 설명: `a way around + 문제` 는 문제를 없애지 않고 옆으로 돌아가는 길입니다. `a way to fix it` 과는 다른 말이에요. 동사로는 `get around`, 명사 하나로는 `a workaround` 입니다. `remote` 를 형용사로 써서 `you're remote` 라 하면 "재택·원격 근무 중"이 됩니다.
- 예문: There's no way around the approval step, but you can start the paperwork today.
- 유사어: two workarounds (명사, 기술 문서), two options in the meantime (평이), two ways to get by (구어, 임시로 버틴다는 느낌)

## "That's a security trade-off for a machine left unattended"
- 레지스터: professional
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (잠금 상태 설명)
- 맥락: 편의를 얻는 대신 치르는 값을 짚을 때(설계 검토·권고)
- 한국어: 지켜보는 사람 없이 둔 기기에는 보안을 내주는 선택이다.
- 설명: `trade-off` 는 하나를 얻으려고 다른 하나를 내주는 맞바꿈입니다. `left unattended` 는 `a machine (that is) left unattended` 가 줄어든 과거분사구로, 공항 안내 방송의 `unattended baggage` 와 같은 낱말이에요. 뒤에 `so it's your call` 이 이어져 결정은 상대에게 넘깁니다.
- 예문: Turning off two-factor login saves a few seconds, but that's a security trade-off for an account with admin rights.
- 유사어: it comes at a cost to security (격식), you're giving up some safety for convenience (풀어 쓴 구어), there's a downside (가장 가벼움)

## "so the Mac never goes idle and locks"
- 레지스터: technical
- 출처: transcript:-Users-daeyoung-Codes-pm-notes-my-task/2fb60678 (잠금 해제 설정 안내)
- 맥락: 설정이나 명령의 결과를 설명할 때(사용 안내)
- 한국어: 그래서 Mac 이 유휴 상태로 넘어가 잠기는 일이 없다.
- 설명: `go + 형용사` 는 상태가 바뀐다는 뜻입니다(`go idle`, `go quiet`, `go offline`). `never` 가 뒤의 동사 둘(`goes idle`, `locks`)에 함께 걸려 "유휴가 되고 이어서 잠기는" 흐름 전체를 부정해요. `lock` 은 여기서 목적어 없이 "잠기다"로 쓰였습니다.
- 예문: Keep the session active with a ping every minute so the connection never goes idle and drops.
- 유사어: so the Mac stays awake (평이), which prevents the idle lock from kicking in (기술 구어), so it doesn't time out (세션·연결에)
- 반의어: goes to sleep, times out
