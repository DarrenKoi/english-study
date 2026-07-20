# 2026-07-21 — 정독

## 단락 1

The root cause was two separate things **stacked on top of each other**. The confusing `UnicodeDecodeError` was my skeleton **masking** the real error. The old deserializer did `pickle.loads` in a **blanket** `try`, and on any failure blindly ran `raw.decode("utf-8")` — which **choked on** the binary parquet bytes at `0xb6` and hid what actually went wrong. The data is parquet, which you confirmed by installing pyarrow. `PAR1` is ASCII, which is exactly why UTF-8 decoding limped to position 61 before hitting binary, and why `pickle.loads` failed (it isn't pickle).

**문법·구조**: 근본 원인을 밝히는 사고 보고문의 전형이다. 첫 문장은 과거시제(`was`)로 결론을 못박고, 이어지는 문장들이 그 결론을 하나씩 해부한다. 눈에 띄는 장치는 **관계대명사 `which`의 계속적 용법**이다 — `…parquet, which you confirmed…`, `PAR1 is ASCII, which is exactly why…`. 콤마 뒤 `which`는 앞 절 전체를 받아 "그리고 그것은 ~"으로 자연스럽게 덧붙이는 방식으로, 한국어 "~인데, 그게 바로 …"에 해당한다. `which is exactly why A and why B`처럼 이유절 `why`를 병렬로 묶어 두 결과를 한 호흡에 설명하는 리듬도 눈여겨볼 만하다. 대시(—)는 `ran … decode()` 뒤에 결과절 `which choked on…`을 붙여, 동작과 그 파국적 결과를 한 문장 안에서 잇는다.
**핵심 표현**: `stacked on top of each other`(원인이 겹겹이 포개진 상황), `mask the real error`(진짜 오류를 가리다), `choke on … bytes`(특정 바이트에서 처리가 막히다). 세 표현이 "증상은 하나인데 원인은 여러 층"이라는 그림을 함께 그린다.
**격식 짝**: "진짜 원인이 다른 문제에 가려져 있었다"를 — refined: *The true cause was obscured by an unrelated failure layered on top of it.* / plain: *The real bug was hidden under another one.*

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (redis parquet 디버깅)</sub>

---

## 단락 2

That error text is a message from the Redis **server**, and it's precise about what happened: the server requires a password, but the client's opening `HELLO` handshake arrived **without any AUTH credentials**. redis-py only omits AUTH from `HELLO` when the password it holds is empty or `None`. So the TCP connection and your host/port are fine — you reached the server — but `REDIS_PASSWORD` is arriving **empty** at connection time.

**문법·구조**: 오류 메시지를 "누가 말한 것인지"부터 규정하고 원인을 역추적하는 진단 화법이다. 기제(mechanism)를 설명할 땐 **현재시제**를 쓴다 — `requires`, `omits`, `holds` — 일반적으로 늘 그렇게 동작한다는 뜻이다. 반면 이번 실행에서 벌어진 일은 **현재진행**(`is arriving`)으로 잡아, "원리"와 "지금 이 순간의 상태"를 시제로 구분한다. 콜론(:)은 앞의 추상적 진단(`precise about what happened`)을 뒤에서 구체화하는 다리 역할을 하고, 문두 `So`는 앞 사실들에서 결론을 끌어내는 연결어다. 마지막 문장의 `fine … but …` 대조 구조가 "연결은 됐다, 그러나 비밀번호가 비어 있다"라는 핵심을 선명하게 가른다.
**핵심 표현**: `it's precise about what happened`(오류가 무슨 일인지 정확히 말해 준다), `arrive without any credentials`(자격증명 없이 도착하다), `arriving empty at connection time`(연결 시점에 빈 값으로 들어오다).
**격식 짝**: "서버에는 닿았지만 인증정보가 비어 있다"를 — refined: *You are reaching the server successfully; the failure is that no credentials accompany the handshake.* / plain: *You're hitting the server fine — the password just shows up empty.*

<sub>출처: transcript:[assistant] skewnono_v3_nuxt (Redis AUTH 진단)</sub>
