# 2026-10-24 — 정독

## 단락 1

I set `provider.plan` to `"max"` in `/Users/daeyoung/.pi/agent/claude-bridge.json`. The existing `startupNoticeShown` value is still there. A backup of the old file is next to it as `claude-bridge.json.bak`. The startup notice is a one-time message. It doesn't fill in the setting itself. The file only had `startupNoticeShown`, which records that you've seen the notice. I added the key with a JSON read-modify-write instead of rewriting the file, so nothing else in it was changed. You'll probably need to restart pi before the bridge picks up the new setting and unlocks the 1M context in Opus.

**문법·구조**: 짧은 평서문을 쌓아 올린 보고다. 앞 세 문장은 "한 일 → 남아 있는 것 → 백업"으로 상대가 걱정할 순서를 미리 막는다. 시제는 한 일은 과거(`I set`, `I added`), 지금 상태는 현재(`is still there`, `doesn't fill in`)로 나뉜다. `which records that you've seen the notice` 는 계속적 용법 관계절로 그 값의 역할을 덧붙인다. `instead of rewriting` 은 동명사로 하지 않은 방법을 대비시키고, `so nothing else … was changed` 의 `so` 는 결과다. 마지막 문장의 `probably` 와 `before` 절은 확인 안 된 다음 단계를 단정하지 않고 조건으로 건다.

**핵심 표현**:
- `is still there` — 바꾸지 않은 값이 남아 있다는 안심 문장. 수정 보고에서 "다른 건 안 건드렸다"를 구체로 말한다.
- `It doesn't fill in the setting itself.` — `itself` 가 "알림이 알아서 해 주는 건 아니다"라는 오해를 정확히 끊는다.
- `picks up the new setting` — 프로세스가 새 설정을 읽어 들이다. 재시작이 필요한 이유를 말할 때 쓴다.

**격식 짝** (작성):
- refined: The configuration change will take effect only after the bridge process has been restarted.
- plain: You'll need to restart pi before it picks up the change.

<sub>출처: transcript:skewnono_v3_nuxt 9306a6b3 (본문 + Insight 를 이어 붙임)</sub>

---

## 단락 2

The tabs come from `FeatureTabs.vue`, so the list is a little different from what you named. TTTM is commented out of the nav while its design is reworked, so I left it out. I also made two changes from what I proposed earlier. `docs/afm/feature-summary.md` is linked from 9 places, so I left it where it is and linked to it from the table. Moving it would have broken those links. I didn't create blank files for the other tabs. Each row says 작성 예정 until its doc is written. Without the update rule in the README, an index like this stops matching the app without anyone noticing.

**문법·구조**: `A, so B` 구문이 세 번 나온다. 근거를 먼저 대고 결정을 뒤에 두는 순서라 결정이 변명이 아니라 결과로 읽힌다. `while its design is reworked` 는 진행 중인 일을 현재 수동으로 말한다(누가 하는지는 중요하지 않음). `Moving it would have broken those links` 는 동명사 주어 + 과거 가정으로, 하지 않은 일의 결과를 들어 결정을 정당화한다. `until its doc is written` 에서 미래 내용인데 현재 수동을 쓰는 건 시간 부사절 규칙이다. 마지막 문장은 `Without …` 이 조건절 역할을 해서 if 없이 가정을 만든다.

**핵심 표현**:
- `a little different from what you named` — 상대 목록을 부드럽게 정정.
- `is commented out of the nav` — 코드에서 주석 처리해 메뉴에서 뺐다. `comment out` 의 수동 + `of` 로 "어디에서 빠졌나"를 붙였다.
- `stops matching the app without anyone noticing` — 문서가 조용히 낡는 위험.

**격식 짝** (작성):
- refined: Relocating the file would have invalidated nine existing references, so it remains in place.
- plain: Moving it would've broken nine links, so I left it alone.

<sub>출처: transcript:skewnono_v3_nuxt 3df93f7f (불릿 항목을 문장으로 이어 붙이고 마지막 문장은 Insight 를 줄여 옮김)</sub>

---

## 단락 3

Gotchas seen so far: `wait --text` times out at 25 s with no partial output, so wait on a string the mock is guaranteed to emit, not on one branch of it; a fresh profile has no persisted chart theme, so ECharts may render with a different theme than your own browser shows — compare structure, not colour, unless the theme is what you are checking. Identity works with no cookie step because the dev server's default `LASTUSER` is admin. Default to the Chrome extension for "does this look and behave right?"; reach for Playwright when the check needs a controlled browser rather than mine. If the extension reports "Browser extension is not connected", switching to Playwright is a fine answer — just say which one is being used.

**문법·구조**: 첫 문장은 콜론 뒤에 세미콜론으로 함정 두 개를 나열한다. 각 함정은 "사실, so 대처법" 구조고 대처법은 명령문(`wait on …`, `compare structure …`)이다. `a string the mock is guaranteed to emit` 은 목적격 관계대명사가 생략된 관계절, `not on one branch of it` 은 앞의 `on a string` 과 평행을 이룬다. `unless the theme is what you are checking` 은 예외 조건이자 `what` 명사절이다. `Default to X; reach for Y when …` 은 기본값과 예외를 세미콜론 하나로 짝짓는 지침 문체다. 마지막 `is a fine answer — just say …` 는 허용 뒤에 조건 하나를 대시로 붙인다.

**핵심 표현**:
- `Gotchas seen so far:` — "지금까지 밟아 본 함정". 경험으로 쌓은 주의사항 목록의 머리말.
- `compare structure, not colour` — `X, not Y` 로 무엇을 볼지 좁힌다.
- `Default to X; reach for Y when …` — 도구 선택 지침의 기본 틀.

**격식 짝** (작성):
- refined: The Chrome extension is the default choice; Playwright should be used when the check requires a controlled browser instance.
- plain: Use the Chrome extension by default, and grab Playwright when you need a clean browser.

<sub>출처: repo:skewnono_v3_nuxt .claude/skills/browser-verify (transcript:skewnono-s1 cf64f1f6 에 실린 스킬 본문, 표와 중간 문장 일부를 덜어냄)</sub>
