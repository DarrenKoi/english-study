# 2026-10-28 — 정독

## 단락 1

`DeleteSpec.files` are DELE'd, then `dirs` RMD'd — files first, so a directory emptied by the same spec can go too. There is no recursive delete: RMD refuses a non-empty directory, and walking a tree would lean on LIST/MLSD parsing that differs per server, for a destructive operation. A path already gone is a success, so a retried run is harmless.

That needs the 550 settled again: after a refused DELE/RMD the path counts as gone only if `SIZE` answers 550 (not a file) **and** `CWD` answers 550 (not a directory). Either check finding something re-raises the original refusal — which is how a non-empty directory, a directory named as a file, and a file named as a directory all stay failures. A probe refused with anything but 550 (502 "SIZE not implemented", 530, …) proves nothing about the path, so it keeps the failure too. The known ceiling: a server that refuses SIZE on an existing file with 550 makes that file read as gone.

**문법·구조**: 첫 문장은 FTP 명령어를 동사로 바꿔 쓴다. `are DELE'd, then dirs RMD'd` 에서 뒤 절은 `are` 를 생략했다. 같은 수동 구조가 반복되면 영어는 두 번째 be 동사를 떨군다. 대시 뒤 `files first, so …` 는 순서를 정한 이유를 덧붙이는 자리다. `can go too` 의 go 는 '없어지다'라는 구어 뜻이다. 둘째 문장은 콜론으로 '없다 → 왜 없는가'를 잇고 이유 두 개를 and 로 묶는다. 끝의 `for a destructive operation` 은 일부러 문장 맨 뒤로 뺐다. 그래서 '삭제라서 더 위험하다'는 무게가 마지막에 실린다. 둘째 단락의 `Either check finding something` 은 동명사구 주어인데, 의미상 주어(Either check)가 앞에 붙은 형태다. `— which is how …` 는 앞 문장 전체를 받는 관계절로, 규칙 하나가 세 가지 경우를 어떻게 함께 막는지 풀어 준다. 마지막 `The known ceiling:` 은 동사 없는 제목형 도입이다. 설계의 한계를 숨기지 않고 따로 이름 붙여 적는 습관이 보인다. `makes that file read as gone` 은 make + O + 동사원형 사역 구조이고 read as 는 '~로 읽히다'.

**핵심 표현**:
- `a retried run is harmless` — 재실행해도 해가 없다. 멱등성을 결과로 풀어 쓴 말.
- `proves nothing about (the path)` — 그 신호는 근거가 못 된다고 선을 긋는다.
- `makes (that file) read as gone` — 실제로는 있는데 없는 것으로 읽히게 만든다. 오판의 경로를 짚을 때.

**격식 짝**:
- refined (작성): Because a path that no longer exists is treated as successfully deleted, repeating the operation has no adverse effect.
- plain (작성): If it's already gone, we count that as done, so running it again won't hurt anything.

<sub>출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/ftp_fleet_downloader.md ("`delete` is DELE + RMD of empty dirs, and idempotent" 절의 두 단락)</sub>

---

## 단락 2

One equipment FTP server. Modeled as exactly one `HostSpec`. All files pulled from a host in a run travel over **one** FTP connection, opened once and reused for the directory listing and every file fetch, then closed. One host = one spec = one connection. Pulling many files from a host needs no separate function — they are listed on that host's single spec and fetched sequentially.

Deployment for a firewalled client that cannot reach the equipment servers. The client POSTs specs over HTTP to a Flask proxy on a firewall-free host; the proxy does the real FTP and returns file bytes. Both paths are in use.

**문법·구조**: 용어집(glossary) 문체다. 각 정의가 `One equipment FTP server.`, `Deployment for …` 처럼 **주어·동사 없는 명사구**로 시작한다. 표제어(Host, Proxy path)가 바로 위에 있으니 'X is …' 를 반복하지 않는 것이다. `Modeled as exactly one HostSpec.` 도 앞에 It is 를 생략한 과거분사 구문이다. 셋째 문장의 `pulled from a host in a run` 은 files 를 뒤에서 꾸미는 축약 관계절(that are pulled)이다. 쉼표 뒤 `opened once and reused …, then closed` 는 connection 의 일생을 과거분사 세 개로 순서대로 보여 준다. 열고 다시 쓰고 닫는다. `One host = one spec = one connection.` 은 등호로 규칙을 공식처럼 박는다. 다음 문장은 동명사 주어 `Pulling many files …` 로 생길 법한 의문(여러 파일이면 함수가 따로 필요한가)을 먼저 꺼내고 대시 뒤에서 수동태 두 개(`are listed …, and fetched …`)로 답한다. 둘째 정의에서는 세미콜론이 client 와 proxy 의 역할을 한 문장 안에서 나눈다. 마지막 `Both paths are in use.` 는 네 단어짜리 단언이라 앞의 긴 문장들 뒤에서 더 단단하게 들린다.

**핵심 표현**:
- `travel over one FTP connection` — 데이터가 한 연결을 타고 간다. travel over 는 경로·매체를 말할 때.
- `opened once and reused …, then closed` — 자원의 수명을 과거분사 나열로 보여 주는 틀.
- `Both paths are in use.` — 둘 다 실제 운영 중이라 어느 쪽도 버릴 수 없다.

**격식 짝**:
- refined (작성): Each host is served by a single FTP connection, which is established once, reused for every operation in the run, and then closed.
- plain (작성): We open one connection per machine, do everything over it, and close it at the end.

<sub>출처: repo:skewnono_v3_nuxt ftp_handler/docs/adr/CONTEXT.md ("Host" · "Proxy path" 두 항목을 이어 인용)</sub>

---

## 단락 3

`durationRows`: the `[...(byRecipe.get(...) ?? []), d.seconds]` spread copies the array on each append, so it is quadratic per recipe. At n ≤ 20 that is under 200 element copies. I would not change it, but a plain `push` would be cleaner if the file is touched again.

`Duration.vue`: `selected` is a prop, so the row list re-renders on each click, but the work is about 20 `v-for` rows plus a handful of recipe rows. That is inherent to the highlight. The `row.entry.key === selected` compare appears three times per row, but it is a string compare and not worth hoisting.

**문법·구조**: 코드 리뷰 보고의 전형적인 3박자다. **관찰 → 규모로 따진 비용 → 판정**. 첫 단락에서 관찰은 `copies the array on each append, so it is quadratic` 이다. so 가 '그러니 이차 시간'이라는 결론을 바로 낸다. 둘째 문장 `At n ≤ 20 that is under 200 element copies.` 는 전치사구 At n ≤ 20 을 앞에 둬서 '이 규모에서는'이라는 전제를 먼저 깔고 실제 숫자로 비용을 잰다. 셋째 문장은 would 를 두 번 써서 의견임을 드러낸다. `I would not change it` 은 판단이고 `would be cleaner if …` 는 가정이라 강요가 아닌 제안이 된다. 둘째 단락은 `X, so Y, but Z` 로 인과와 양보를 한 문장에 담는다. 비용이 생기는 이유(prop 이라 다시 그림)를 인정하고 그래도 작다(20행)고 덧붙이는 흐름이다. 이어지는 `That is inherent to the highlight.` 는 짧은 지시대명사 문장으로 판정만 내린다. 마지막 문장도 `appears three times …, but it is … and not worth hoisting` 으로 '사실은 인정하되 고칠 가치는 없다'를 같은 틀로 반복한다. 비용을 먼저 숫자로 보여 주니 '문제 없음'이라는 판정이 가볍게 들리지 않는다.

**핵심 표현**:
- `I would not change it, but (X) would be cleaner if the file is touched again.` — 지금 고칠 건 아니고 다음 기회에 하라는 부드러운 제안.
- `That is inherent to (the highlight).` — 기능 자체의 대가라서 줄일 대상이 아니라는 판정.
- `not worth hoisting` — 반복 계산을 밖으로 빼 봐야 이득이 없다.

**격식 짝**:
- refined (작성): The overhead is intrinsic to the highlighting behaviour and does not warrant optimisation at this scale.
- plain (작성): It's just what highlighting costs, and with 20 rows it really doesn't matter.

<sub>출처: transcript:skewnono-v3-nuxt subagent(efficiency review) [assistant] (리뷰 보고의 두 항목을 이어 인용, 항목 기호만 뺌)</sub>
