# 2026-07-27 — 정독

## 단락 1

Short answer: in-memory is safe here, and it is not inherently riskier than disk. The fear that "async mixes one host's data into another host's buffer" comes from shared mutable state, not from memory itself. Cross-host contamination happens only if concurrent units share a destination or a stateful resource. Note that disk has the exact same risk: if two hosts write to a path keyed by filename only, they clobber each other — that is cross-host mixing, just on disk. The repo's `recipe_log_collector` avoids it with a `uuid4` folder + per-IP subdir. Correctness comes from isolating the destination per host (unique buffer or unique path) and not sharing a connection — not from the storage medium. asyncio never moves data between coroutines on its own; each task has its own stack.

**문법·구조**: 이 단락은 **남의 걱정을 반박하지 않고 자리만 옮기는 법**을 보여 줍니다. "안전하다"고 우기는 대신, 걱정의 원인을 다른 데로 재배치해 결론을 뒤집습니다.

두 번째 문장의 `The fear that "…" comes from shared mutable state` 를 보세요. 여기 `that` 은 관계대명사가 아니라 **동격의 that** 입니다. `the fear` 가 무엇인지를 절 하나로 통째로 설명해 주고, 진짜 동사는 한참 뒤 `comes` 예요. 관계절이라면 `the fear that came from …` 처럼 that 이 주어 노릇을 하겠지만, 여기서는 `that` 이 문장 성분이 아니라 그냥 접속사입니다. 상대의 말을 인용부호에 담아 주어 안에 집어넣은 덕에, 반박 없이 그 걱정을 문장이 떠안고 시작합니다.

세 번째 문장의 `happens only if` 는 어순이 전부입니다. `only` 를 `if` 앞에 세우면 그 조건이 **필요조건**이 됩니다 — 그 경우가 아니면 절대 안 일어난다는 뜻. `happens if only` 로 뒤집으면 뜻이 무너지니 붙여 외우세요.

네 번째 문장의 `a path keyed by filename only` 는 `which is keyed by …` 에서 `which is` 를 지운 과거분사 후치수식입니다. 그리고 대시 뒤 `that is cross-host mixing, just on disk` 가 결정타예요. `just` 하나가 "다를 게 없다, 무대만 바뀌었다"를 담습니다. 디스크가 더 안전하다는 통념을 여기서 한 단어로 무너뜨립니다.

여섯 번째 문장은 두 번째 문장의 `comes from A, not from B` 를 그대로 다시 씁니다. 걱정을 받아 낸 문형으로 결론까지 닫는 수미상관이고, 이번엔 `not from` 앞에 대시를 세워 대비를 한 번 더 벌려 놨습니다. `of` 나 `from` 을 두 번 반복해 쓴 것도 의도예요. `not the storage medium` 이라고만 줄이면 무엇과 무엇이 맞붙는지 흐려집니다.

마지막 문장의 세미콜론은 근거를 붙이는 자리이고, `on its own`(저절로, 스스로)이 조용히 일합니다. "asyncio 가 데이터를 안 옮긴다"가 아니라 **"시키지 않으면 옮기지 않는다"** — 즉 옮기는 건 언제나 사람이 짠 공유 상태라는 뜻이 됩니다.

**핵심 표현**: `comes from A, not from B itself` 는 오해를 교정하는 자리의 기본형입니다. `clobber each other` 는 두 쪽이 서로 덮어써 망가뜨리는 상황에 쓰는 현장어. `Short answer:` 는 긴 설명 앞에 결론을 먼저 던지는 라벨이라, 질문을 받아 쓰는 문서에서 그대로 베껴 쓸 만합니다.

**격식 짝**:

- refined: `Correctness comes from isolating the destination per host, not from the storage medium.` / plain: `What keeps it correct is giving each host its own place to write — not whether it's RAM or disk.`
- refined: `Cross-host contamination happens only if concurrent units share a destination.` / plain: `Two hosts only step on each other when they're writing to the same thing.`

<sub>출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md</sub>

---

## 단락 2

Each host is one short FTP session that is almost all socket I/O, and Python releases the GIL during socket I/O — so blocking `ftplib` in a bounded thread pool fans out hundreds of hosts concurrently with zero extra packages. No `aioftp` to `pip install` into an Airflow venv, no `PythonVirtualenvOperator`, no version drift between your laptop and the worker. Around 200 simultaneous connections blow past the worker's open-file limit and the equipment's connection caps; some downloads then silently fail. `max_concurrency` caps how many run at once. One dead or black-holed host can't abort or stall the rest: tight timeouts bound each host, and failures are collected, not raised.

**문법·구조**: 설계 근거를 적는 단락의 표본입니다. 무엇을 만들었는지가 아니라 **왜 그 모양인지**만 말하고, 세 가지 이유가 각각 다른 문장 구조를 타고 옵니다.

첫 문장은 근거 두 개를 등위로 붙인 뒤 대시로 결론을 끌어냅니다. `Each host is one short FTP session that is almost all socket I/O`(근거 1) `and Python releases the GIL during socket I/O`(근거 2) `— so …`(결론). 대시 뒤에 `so` 를 두는 배치가 편합니다. 접속사만 쓰면 문장이 길게 늘어지는데, 대시가 시각적으로 한 번 끊어 주니 근거와 결론의 경계가 눈에 보여요. `almost all socket I/O` 의 `almost` 는 `all` 앞에 붙습니다 — `all almost` 는 성립하지 않습니다.

두 번째 문장에는 동사가 없습니다. `No X, no Y, no Z` 로 명사구만 세 개 늘어놓은 형태예요. 문법적으로 불완전한데도 읽히는 건 앞 문장의 `with zero extra packages` 를 풀어 쓴 동격이기 때문입니다. 이런 무동사 나열은 **앞 문장이 그 자리를 이미 만들어 놨을 때만** 성립하니, 단독으로 쓰면 그냥 비문이 됩니다. `No aioftp to pip install into …` 의 `to` 부정사도 눈여겨보세요. "설치할 aioftp 가 없다"라는 뜻이고, 명사 뒤 to 부정사가 "~할" 로 앞을 꾸미는 자리입니다.

세 번째 문장의 세미콜론은 인과입니다. 한도를 넘긴다(원인) → 조용히 실패한다(결과). 여기에 `then` 이 붙어 시간 순서까지 잡아 주는데, `and` 로 이었다면 두 사실이 나란히 놓이기만 하고 이 순서가 안 보입니다.

마지막 문장의 콜론 뒤에는 근거가 두 개 옵니다. 그중 `failures are collected, not raised` 는 수동태 대구인데, `raise` 가 파이썬의 예외 발생 동사이면서 일반 영어 동사이기도 해서 한 단어로 두 층위를 동시에 말합니다. 능동으로 `we collect failures instead of raising them` 이라고 써도 되지만, 그러면 주어가 사람으로 바뀌어 **시스템의 성질**이라는 느낌이 옅어집니다.

**핵심 표현**: `fan out hundreds of hosts with zero extra packages` — `fan out` 은 하나에서 여럿으로 갈라져 동시에 나가는 그림이고, `with zero extra packages` 는 대가가 없음을 수치로 못 박는 꼬리표입니다. `version drift between your laptop and the worker` 는 두 환경이 서서히 어긋나는 상태를 한 명사로 부른 말. `bound each host` 의 `bound` 는 동사 "한계를 지우다"이며, `bind`(묶다)의 과거형과 철자가 겹치니 문맥으로 갈라 읽어야 합니다.

**격식 짝**:

- refined: `Failures are collected, not raised.` / plain: `We gather up what went wrong instead of blowing up on the first one.`
- refined: `One dead or black-holed host cannot abort or stall the rest.` / plain: `One tool being down doesn't drag everything else down with it.`

<sub>출처: repo:flask_modules ftp_handler/docs/adr/ftp_fleet_downloader.md</sub>

---

## 단락 3

A ruler means "measure a length" — that isn't what the page does. It picks a magnification and a pixel count. `scan-search` is a scan frame with a magnifier inside it, which is the page's question exactly: what magnification fits the pattern inside the field of view? And "scan" is the right verb for a SEM. I rendered the candidates at nav size against the icons already in the header before choosing, which is what ruled the others out. The one real risk was a second magnifier in the header. It isn't a problem in practice: `search` always appears inside a labelled pill, never bare in the icon-only cluster.

**문법·구조**: 선택의 근거를 대는 단락입니다. 고른 것을 칭찬하지 않고 **탈락시킨 이유**로 설득하는 구조라, 리뷰어에게 판단 과정을 넘겨줍니다.

첫 문장의 `that isn't what the page does` 는 유사분열문(pseudo-cleft)의 부정형입니다. `the page doesn't do that` 이라고 써도 뜻은 같지만, `what the page does`(이 페이지가 하는 일)를 하나의 명사 덩어리로 만들어 `that` 과 맞세우면 대조가 훨씬 또렷합니다. 바로 다음 문장 `It picks a magnification and a pixel count` 가 그 빈자리를 채우니, 두 문장이 짝으로 읽힙니다.

세 번째 문장의 `, which is the page's question exactly` 는 **앞 절 전체를 받는 비제한적 관계절**입니다. 선행사가 명사 하나가 아니라 "돋보기가 들어간 스캔 프레임"이라는 상황 전체예요. 쉼표 없이 붙이면 `it` 만 받는 제한적 관계절로 읽혀 뜻이 좁아집니다. 문장 끝의 `exactly` 는 부사가 문미로 밀려난 자리인데, 이렇게 두면 앞 명사구 전체에 강세가 얹힙니다.

`And "scan" is the right verb for a SEM.` 은 문두 And 입니다. 학교 문법에서는 말리지만 기술 글에서는 흔하고, 여기서는 **근거 하나를 일부러 따로 떼어** 무게를 주려고 썼습니다. 앞 문장에 `and` 로 이어 붙였다면 이 문장은 부록처럼 묻혔을 겁니다.

다섯 번째 문장의 `, which is what ruled the others out` 은 관계절 안에 유사분열문이 또 들어간 이중 구조입니다. `which`(내가 나란히 렌더링해 본 것) + `is what …`(바로 그것이 나머지를 탈락시킨 이유). 절차를 말하고 그 절차가 곧 근거였다고 한 번에 닫는 방식이라, 결론과 방법론을 따로 쓸 필요가 없어집니다.

마지막 문장의 `never bare in the icon-only cluster` 에서는 `it appears` 가 생략됐습니다. 앞의 `always appears inside a labelled pill` 과 대구를 이루면서 반복되는 동사만 지운 형태이고, 형용사 `bare` 가 그대로 남아 부사처럼 읽힙니다.

**핵심 표현**: `that isn't what X does` 는 후보를 탈락시키는 가장 짧은 문형입니다. `in practice`(이론상은 몰라도 실제로는)는 위험을 인정한 뒤 무해함을 주장하는 자리에 쓰고, 앞에 `The one real risk was …` 를 세워 두면 정직하게 들립니다.

**격식 짝**:

- refined: `A ruler denotes linear measurement, which is not what this page performs.` / plain: `A ruler says "measure a length" — that's not what the page does.`
- refined: `The risk of a duplicate magnifier does not materialize in practice.` / plain: `In practice the second magnifier just isn't a problem.`

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (fe1dc34e)</sub>
