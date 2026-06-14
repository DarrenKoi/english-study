import json
import os
from datetime import date
from pathlib import Path

from pipeline import config, gitutil, transcripts, requests_inbox, batch

def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))

def collect(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()
    cfg = config.load_config(root / "config" / "sources.json")
    state = config.load_state(root / "state" / "progress.json")

    units: list[dict] = []
    repo_heads: dict[str, str] = {}

    # 1) 요청(주문서) — 최우선
    for req in requests_inbox.pending_requests(root):
        rel = req.relative_to(root).as_posix()
        units.append({"kind": "request", "id": req.name,
                      "provenance": f"request:{rel}", "text": req.read_text(encoding="utf-8"),
                      "advance": {"request": rel}})

    # 2) repo 별 증분 마크다운 (repo 1개 = 단위 1개, all-or-nothing)
    base = _expand(cfg["base_path"])
    for r in cfg["repos"]:
        repo_path = base / r["name"]
        if not repo_path.exists():
            continue
        gitutil.pull(repo_path)
        since = state["repos"].get(r["name"])
        files = gitutil.changed_md_files(repo_path, since, r["globs"])
        repo_heads[r["name"]] = gitutil.head_sha(repo_path)
        if not files:
            continue
        body = []
        for f in files:
            body.append(f"### {f}\n\n{(repo_path / f).read_text(encoding='utf-8', errors='replace')}")
        units.append({"kind": "repo", "id": r["name"],
                      "provenance": f"repo:{r['name']} ({','.join(r['globs'])})",
                      "text": "\n\n".join(body),
                      "advance": {"repo": r["name"], "sha": repo_heads[r["name"]]}})

    # 3) 트랜스크립트 — 파일 1개 = 단위 1개
    tx_dir = _expand(cfg["transcripts_dir"])
    recs, new_offsets = transcripts.new_messages(tx_dir, state["transcripts"])
    by_file: dict[str, list[str]] = {}
    for rec in recs:
        by_file.setdefault(rec["file"], []).append(f"[{rec['role']}] {rec['text']}")
    for fname, texts in by_file.items():
        units.append({"kind": "transcript", "id": fname,
                      "provenance": f"transcript:{fname}", "text": "\n\n".join(texts),
                      "advance": {"transcript": fname, "offset": new_offsets[fname]}})

    # 예산 내 조립
    batch_text, consumed = batch.build_batch(units, cfg.get("char_budget", 200000), today)

    # 매니페스트(소비 단위만 상태 전진 대상)
    manifest = {"repos": {}, "transcripts": {}, "requests": [], "deferred": len(units) - len(consumed)}
    for u in consumed:
        adv = u["advance"]
        if u["kind"] == "repo":
            manifest["repos"][adv["repo"]] = adv["sha"]
        elif u["kind"] == "transcript":
            manifest["transcripts"][adv["transcript"]] = adv["offset"]
        elif u["kind"] == "request":
            manifest["requests"].append(adv["request"])

    (root / "state").mkdir(parents=True, exist_ok=True)
    batch_path = root / "state" / f"batch-{today}.md"
    batch_path.write_text(batch_text, encoding="utf-8")
    (root / "state" / f"consumed-{today}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"item_count": len(consumed), "deferred": manifest["deferred"],
            "batch_path": str(batch_path), "today": today}

if __name__ == "__main__":
    print(collect())
