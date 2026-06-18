import json
import os
import time
from datetime import date
from pathlib import Path

from pipeline import config, gitutil, transcripts, spool, batch

DEFAULT_DOC_DIRS = ["doc", "docs", "shared_docs"]
DEFAULT_DOC_EXTS = [".md", ".txt"]
DEFAULT_RECENT_DAYS = 7
# 문서 탐색 중 들어가지 않을 디렉터리(빌드 산출물·벤더·VCS 내부).
PRUNE_DIRS = {"node_modules", ".git", ".venv", "venv", "__pycache__",
              "dist", "build", ".next", ".nuxt", ".output", "done"}

def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))

def _iter_projects(base: Path, exclude: set[str]):
    """~/Codes 바로 아래의 프로젝트 디렉터리들(제외·hidden 제외)을 정렬 순서로 돈다.
    git pull 루프와 문서 탐색이 같은 규칙을 쓰도록 한 곳에 모았다."""
    if not base.exists():
        return
    for project in sorted(p for p in base.iterdir() if p.is_dir()):
        if project.name in exclude or project.name.startswith("."):
            continue
        yield project

def _doc_key(project: str, relpath: str, mtime: float, size: int) -> str:
    """문서의 동일성 키: 경로 + 수정시각 + 크기. 파일을 고치면(=mtime/크기 변동) 키가 달라져
    같은 날이라도 재수집된다. stat 만으로 판정하므로 변경 없는 파일은 읽지 않는다."""
    return f"{project}/{relpath}:{mtime}:{size}"

def _iter_doc_roots(project: Path, doc_dirs: set[str]):
    """project 아래를 훑으며 이름이 doc_dirs 인 디렉터리를 깊이 제한 없이 찾는다.
    node_modules·.git·hidden 등은 들어가지 않는다(가지치기)."""
    for dirpath, dirnames, _ in os.walk(project):
        dirnames[:] = [d for d in dirnames
                       if d not in PRUNE_DIRS and not d.startswith(".")]
        for d in dirnames:
            if d in doc_dirs:
                yield Path(dirpath) / d

def discover_doc_files(base: Path, cfg: dict, now: float | None = None) -> list[dict]:
    """~/Codes 아래 각 프로젝트의 doc/docs/shared_docs 폴더에서, 최근
    recent_days 안에 수정된 .md/.txt 파일을 최신순으로 모은다(stat 만, 내용은 안 읽음)."""
    now = time.time() if now is None else now
    doc_dirs = set(cfg.get("doc_dirs", DEFAULT_DOC_DIRS))
    exts = {e.lower() for e in cfg.get("doc_exts", DEFAULT_DOC_EXTS)}
    cutoff = now - cfg.get("recent_days", DEFAULT_RECENT_DAYS) * 86400
    exclude = set(cfg.get("exclude_projects", []))

    found: dict[Path, dict] = {}   # 절대경로 기준 dedup(중첩 doc 폴더 대비)
    for project in _iter_projects(base, exclude):
        for docroot in _iter_doc_roots(project, doc_dirs):
            for dirpath, dirnames, filenames in os.walk(docroot):
                dirnames[:] = [d for d in dirnames
                               if d not in PRUNE_DIRS and not d.startswith(".")]
                for name in filenames:
                    f = Path(dirpath) / name
                    if f.suffix.lower() not in exts:
                        continue
                    try:
                        st = f.stat()
                    except OSError:
                        continue
                    if st.st_mtime < cutoff:
                        continue
                    ap = f.resolve()
                    if ap in found:
                        continue
                    found[ap] = {"mtime": st.st_mtime, "size": st.st_size,
                                 "project": project.name,
                                 "relpath": f.relative_to(project).as_posix(), "path": f}
    return sorted(found.values(), key=lambda d: d["mtime"], reverse=True)

def collect(root: Path | None = None, today: str | None = None) -> dict:
    root = Path(root) if root else config.root()
    today = today or date.today().isoformat()
    cfg = config.load_config(root / "config" / "sources.json")
    state = config.load_state(root / "state" / "progress.json")

    units: list[dict] = []

    # 1) spool 노트(사용자가 직접 적은 학습 질문) — 최우선
    for note in spool.pending_notes(root):
        rel = note.relative_to(root).as_posix()
        units.append({"kind": "spool", "id": note.name,
                      "provenance": f"spool:{rel}", "text": note.read_text(encoding="utf-8"),
                      "advance": {"note": rel}})

    # 2) 문서 폴더 — ~/Codes 전 프로젝트의 doc/docs/shared_docs 에서 최근 수정 파일을
    #    매 실행마다 다시 훑는다(상태 추적 없이 윈도 기반). 파일 1개 = 단위 1개.
    #    같은 날 이미 처리(=finalize)한 문서는 오늘 원장(state["docs_today"])에 있어 건너뛴다.
    #    원장은 finalize 가 성공 시에만 전진시키므로, LLM 실패 후 재실행은 그 문서를 다시 집는다.
    dt = state.get("docs_today") or {}
    already = set(dt.get("keys", [])) if dt.get("date") == today else set()
    base = _expand(cfg["base_path"])
    exclude = set(cfg.get("exclude_projects", []))
    for project in _iter_projects(base, exclude):
        if (project / ".git").exists():
            gitutil.pull(project)   # 최신 docs 반영(베스트에포트, 충돌 시 조용히 건너뜀)
    char_budget = cfg.get("char_budget", 200000)
    doc_chars, unread = 0, 0
    for d in discover_doc_files(base, cfg):
        key = _doc_key(d["project"], d["relpath"], d["mtime"], d["size"])
        if key in already:
            continue
        if doc_chars >= char_budget:
            unread += 1          # 예산을 이미 채움 → 읽지 않고 미룬다(다음 실행에서 재시도)
            continue
        text = d["path"].read_text(encoding="utf-8", errors="replace")
        units.append({"kind": "doc", "id": f"{d['project']}/{d['relpath']}",
                      "provenance": f"repo:{d['project']} {d['relpath']}",
                      "text": text, "advance": {"doc_key": key}})
        doc_chars += len(text)

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
    batch_text, consumed = batch.build_batch(units, char_budget, today)

    # 매니페스트(소비 단위만 상태 전진 대상). 이번 실행에서 배치에 들어간 문서 키는 "docs" 에
    # 적어 finalize 가 성공 시 오늘 원장으로 승격시킨다(예산에 밀려 빠진 문서는 기록 안 함).
    manifest = {"repos": {}, "repo_queue": {}, "transcripts": {}, "spool": [], "docs": [],
                "deferred": (len(units) - len(consumed)) + unread}
    for u in consumed:
        adv = u.get("advance")
        if u["kind"] == "transcript":
            manifest["transcripts"][adv["transcript"]] = adv["offset"]
        elif u["kind"] == "spool":
            manifest["spool"].append(adv["note"])
        elif u["kind"] == "doc":
            manifest["docs"].append(adv["doc_key"])
    manifest["docs"].sort()

    (root / "state").mkdir(parents=True, exist_ok=True)
    batch_path = root / "state" / f"batch-{today}.md"
    batch_path.write_text(batch_text, encoding="utf-8")
    (root / "state" / f"consumed-{today}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"item_count": len(consumed), "deferred": manifest["deferred"],
            "batch_path": str(batch_path), "today": today}

if __name__ == "__main__":
    print(collect())
