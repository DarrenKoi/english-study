# 2026-10-29 — 정독

## 단락 1

The company firewall blocks all external LLM APIs (OpenAI, Anthropic, Google, etc.). Only internally hosted open-source models behind an OpenAI-compatible API are available. Trainees cannot use vendor cloud consoles. So for each source, judge how much of it survives when you strip out the vendor's own product: concepts and exercise design transfer; labs tied to a vendor cloud do not.

Use **primary sources only** — the provider's own course page, syllabus, official GitHub repo, exam guide/skills outline, LICENSE file. Not blog summaries or listicles. Follow each claim to the page that owns it. My own knowledge of what exists may be stale, so verify each candidate still exists and note what is current; also look for things launched in 2025–2026 that I don't list.

**문법·구조**: 첫 단락은 짧은 현재형 사실 셋(blocks / are available / cannot use)으로 제약을 깐 뒤 So 로 지시를 꺼낸다. 이유를 먼저 쌓고 명령을 나중에 두니 지시가 자의적으로 들리지 않는다. 콜론 뒤는 세미콜론으로 대비 한 쌍을 만든다. `concepts and exercise design transfer; labs … do not` 에서 do not 뒤에는 transfer 가 생략됐다. 앞 절과 동사가 같으면 영어는 조동사만 남긴다. `tied to a vendor cloud` 는 labs 를 뒤에서 꾸미는 과거분사구(that are tied to)다. 둘째 단락은 명령문 `Use …` 로 열고 대시 뒤에서 primary source 가 무엇인지 목록으로 풀어 준다. 이어지는 `Not blog summaries or listicles.` 는 동사 없는 조각문이다. 허용 목록 바로 뒤에 금지 목록을 붙여 경계를 또렷하게 만든다. 마지막 문장에서는 지시자가 `My own knowledge … may be stale` 로 자기 한계를 먼저 인정한다. 그래서 '검증하라'는 요구가 불신이 아니라 협업으로 읽힌다. `things launched in 2025–2026 that I don't list` 는 과거분사 후치 수식과 관계절이 겹친 형태다.

**핵심 표현**:
- `how much of it survives when you strip out (X)` — 조건을 걷어 낸 뒤 남는 가치를 묻는 평가 기준.
- `Follow each claim to the page that owns it.` — 원출처까지 거슬러 가라. own 은 '책임지고 관리하다'.
- `My own knowledge … may be stale` — 지시자가 자기 정보가 낡았을 수 있다고 인정하는 열린 태도.

**격식 짝**:
- refined (작성): Each claim should be traced to its authoritative primary source rather than to secondary summaries.
- plain (작성): Don't trust the blog posts. Go check the actual course page yourself.

<sub>출처: transcript:pm-notes subagent a730d3ef ("Hard constraint" · "What to investigate" 두 절 첫머리)</sub>

---

## 단락 2

**Defect:** the Distribution panel shows a standard deviation taken from the backend's per-parameter summary, while verdicts and the other panels compute σ in the client. Two numbers called σ for the same parameter of the same measurement can differ. **Do:** first establish the facts — which panels show which σ, whether the backend value is a population or sample standard deviation, and over which rows. Then make the screen consistent with the smallest change: every σ shown for the active parameter of one measurement comes from the same client computation the verdicts use. Where a backend summary value must still be shown, label it so it cannot be read as the same quantity. Do NOT change the backend, the contract, or the providers.

**문법·구조**: 결함 보고의 전형인 **Defect → Do** 2단 구조다. Defect 첫 문장은 while 로 두 쪽을 맞세운다. 백엔드 값을 보여 주는 쪽과 클라이언트에서 계산하는 쪽. `taken from …` 은 standard deviation 을 꾸미는 과거분사구다. 둘째 문장 `Two numbers called σ … can differ.` 에서 called σ 도 같은 후치 수식인데, '이름은 같은데 값은 다르다'는 문제의 핵심을 이 한 구가 담는다. Do 쪽은 순서 부사 `first … Then …` 로 '사실 확인 → 최소 수정' 단계를 못 박는다. 대시 뒤에는 확인할 질문 세 개를 which / whether / over which 로 병렬해 간접의문문 목록을 만든다. 콜론 뒤 `every σ shown … comes from the same client computation the verdicts use` 는 목표 상태를 현재형으로 적는다. 바라는 결과를 이미 참인 사실처럼 쓰는 사양서 문체다. 마지막 두 문장은 예외(Where … must still be shown)와 금지(Do NOT)로 범위를 닫는다. 대문자 NOT 은 이 지시에서 가장 어기기 쉬운 선이 어디인지 보여 준다.

**핵심 표현**:
- `Two numbers called σ … can differ.` — 이름만 같고 값이 다른 문제를 한 문장으로 요약.
- `make the screen consistent with the smallest change` — 일관성을 최소 수정으로 맞추라는 범위 지시.
- `label it so it cannot be read as the same quantity` — 값은 두되 오독을 막으라.

**격식 짝**:
- refined (작성): Any backend-derived figure that remains on screen should be labelled distinctly so that it is not mistaken for the client-computed value.
- plain (작성): If you still have to show the backend number, call it something else so nobody thinks it's the same σ.

<sub>출처: transcript:skewnono-v3-nuxt subagent a676af14 ("A — one σ definition per screen" 절, 괄호 속 파일 경로는 생략하고 인용)</sub>

---

## 단락 3

One dead host never aborts its siblings, and inside a host one bad file (or directory, for `mkdir` / `delete`) never aborts the rest. Failures are collected into the report, never raised. Callers gate on `failure_ratio` (e.g. `> 0.2`, or zero successes) — tools go offline routinely.

Cross-host contamination comes from **shared mutable state**, not from memory: each host gets its own connection used sequentially in its own thread, and each file lands in a fresh local `BytesIO`. Disk has the same risk (two hosts writing the same filename clobber each other); correctness comes from isolating the destination per host, not from the medium.

**문법·구조**: 첫 문장은 never 를 두 번 써서 같은 원칙을 두 규모(호스트끼리, 호스트 안 파일끼리)에 반복 적용한다. `Failures are collected into the report, never raised.` 는 수동태 과거분사 두 개를 쉼표로 맞세워 'A 이지 B 가 아니다'를 동사 하나로 처리한다. 셋째 문장 대시 뒤 `tools go offline routinely` 는 정책의 이유다. routinely 하나로 '실패는 예외가 아니라 일상'이라는 전제를 깐다. 둘째 단락은 **X comes from A, not from B** 틀을 처음과 끝에 두 번 쓴다(not from memory / not from the medium). 같은 틀이 앞뒤를 감싸서 주장이 하나로 닫힌다. 콜론 뒤에는 each … its own 을 반복해 격리가 어떻게 이뤄지는지 보여 준다. `used sequentially in its own thread` 는 connection 을 꾸미는 과거분사구다. 괄호 속 `two hosts writing the same filename clobber each other` 에서 writing … 은 hosts 를 꾸미는 현재분사구이고 동사는 clobber 다. 주어가 길어도 동사를 찾으면 문장이 풀린다.

**핵심 표현**:
- `Failures are collected into the report, never raised.` — 예외를 던지지 않고 모아서 보고한다는 설계 원칙.
- `X comes from A, not from B` — 원인을 바로잡을 때 쓰는 대비 틀.
- `correctness comes from isolating the destination per host` — 정확성의 근거를 '격리'라는 행위로 짚는다.

**격식 짝**:
- refined (작성): The risk of cross-host contamination arises from shared mutable state rather than from the storage medium itself.
- plain (작성): The danger isn't memory versus disk. It's two hosts touching the same thing.

<sub>출처: repo:bulk_recipe_copy ftp_handler/docs/adr/ftp_fleet_downloader.md ("Failure isolation is the normal case" · "In-memory, not disk" 절)</sub>
