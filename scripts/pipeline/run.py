import subprocess
from pathlib import Path

from pipeline import config, tokenlog
from pipeline.collect import collect
from pipeline.finalize import finalize

def _invoke_claude(prompt: str, root: Path) -> str:
    # 무인 실행: 도구를 파일 계열로만 제한한다. 배치에 섞일 수 있는
    # 프롬프트 인젝션이 Bash·네트워크로 번지지 못하게 막는 방어선.
    # (git push 는 LLM 이 아니라 finalize 의 Python 이 수행)
    res = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json",
         "--allowedTools", "Read,Edit,Write,Glob"],
        cwd=str(root), capture_output=True, text=True)
    if res.returncode != 0:
        return ""
    return res.stdout

def run(root: Path | None = None) -> dict:
    root = Path(root) if root else config.root()
    info = collect(root=root)
    today = info["today"]
    if info["item_count"] == 0:
        print(f"[{today}] 처리할 새 항목 없음. 종료.")
        return {"status": "empty", "today": today}

    prompt = _build_prompt(root, info)
    out = _invoke_claude(prompt, root)
    if not out.strip():
        print(f"[{today}] LLM 호출 실패 — 상태를 전진시키지 않고 종료(다음 실행에서 재시도).")
        return {"status": "llm_failed", "today": today}
    usage = tokenlog.parse_usage(out)
    tokenlog.append_token_log(root, today, usage, info["item_count"])

    finalize(root=root, today=today)
    print(f"[{today}] 완료. 항목 {info['item_count']}개, 미뤄짐 {info['deferred']}개, "
          f"토큰 out={usage['output_tokens']}, 비용 ${usage['cost_usd']}")
    return {"status": "done", "today": today, **usage}

def _build_prompt(root: Path, info: dict) -> str:
    process_md = root / "prompts" / "process.md"
    base = process_md.read_text(encoding="utf-8") if process_md.exists() else ""
    today = info["today"]
    return (f"{base}\n\n---\n"
            f"처리할 배치 파일: {info['batch_path']}\n"
            f"오늘 날짜: {today}\n"
            f"출력 폴더 접두사: daily/{today}/\n")

if __name__ == "__main__":
    run()
