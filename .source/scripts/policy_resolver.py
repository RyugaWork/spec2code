#!/usr/bin/env python3
"""Repository-local, read-only, bounded policy discovery (PLAN-080)."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path, PurePosixPath
import re
import sys

import config_loader
import governance_schema as schema
import path_guard
import scope_io

CFG = config_loader.load("governance")


@dataclass(frozen=True)
class PolicyRequest:
    root: Path
    task_id: str
    task: str
    paths: tuple[str, ...] = ()
    operation: str = "read"


def _text(root: Path, rel: str, cap: int) -> str | None:
    path = path_guard.check_path(root, rel)
    if not path.is_file() or path.is_symlink():
        return None
    try:
        return scope_io.read_bytes(root, path, max_bytes=cap).decode("utf-8")
    except (UnicodeError, OSError, ValueError):
        raise RuntimeError("POLICY_READ_FAILED:" + rel)


def _relative(root: Path, value: str) -> str:
    rel = schema.safe_path(value, suffixes=())
    path_guard.check_path(root, rel)
    return rel


def _scan_agents(root: Path, paths: tuple[str, ...]) -> list[dict]:
    candidates = {"AGENTS.md"}
    for value in paths:
        rel = PurePosixPath(_relative(root, value))
        for ancestor in list(rel.parents)[:-1]:
            if str(ancestor) != ".":
                candidates.add((ancestor / "AGENTS.md").as_posix())
        if str(rel.parent) != ".":
            candidates.add((rel.parent / "AGENTS.md").as_posix())
    if len(candidates) > CFG["limits"]["max_agents_files"]:
        raise RuntimeError("POLICY_AGENTS_LIMIT")
    files = []
    for rel in sorted(candidates):
        path = path_guard.check_path(root, rel)
        if path.is_symlink():
            raise RuntimeError("POLICY_SYMLINK_BLOCKED:" + rel)
        if path.is_file():
            if path.stat().st_size > CFG["limits"]["max_agents_bytes"]:
                raise RuntimeError("POLICY_AGENTS_TOO_LARGE:" + rel)
            files.append({"path": rel, "reason": "root" if rel == "AGENTS.md" else "nested"})
    return files


def _map(root: Path) -> list[dict]:
    rel = CFG["host_policy_map"]
    path = path_guard.check_path(root, rel)
    if path.is_symlink():
        raise RuntimeError("POLICY_SYMLINK_BLOCKED:" + rel)
    if not path.exists():
        return []
    try:
        data = json.loads(_text(root, rel, CFG["limits"]["max_host_map_bytes"]),
                          object_pairs_hook=_unique_pairs)
    except (ValueError, TypeError, UnicodeError) as err:
        raise RuntimeError("POLICY_MAP_MALFORMED") from err
    return schema.validate_host_map(data, {c["id"] for c in CFG["categories"]},
                                    CFG["limits"]["max_host_map_documents"])


def _unique_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def _categories(task: str, paths: tuple[str, ...]) -> set[str]:
    haystack = (task + " " + " ".join(paths)).casefold()
    return {cat["id"] for cat in CFG["categories"]
            if any(re.search(r"(?<![a-z0-9])" + re.escape(word.casefold()) +
                             r"(?![a-z0-9])", haystack) for word in cat["keywords"])}


def resolve(request: PolicyRequest) -> dict:
    root = path_guard.validate_root(request.root)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", request.task_id):
        raise RuntimeError("POLICY_INVALID_TASK_ID")
    if request.operation not in schema.OPERATIONS:
        raise RuntimeError("POLICY_INVALID_OPERATION")
    if not isinstance(request.task, str) or not 1 <= len(request.task) <= 2000:
        raise RuntimeError("POLICY_INVALID_TASK")
    if len(request.paths) > CFG["limits"]["max_selected_paths"]:
        raise RuntimeError("POLICY_PATH_LIMIT")
    paths = tuple(sorted({_relative(root, p) for p in request.paths}))
    agents = _scan_agents(root, paths)
    cats = _categories(request.task, paths)
    manifest = _map(root)
    selected, candidates, missing, canonical = [], [], [], {}
    for entry in manifest:
        category = entry["category"]
        if category not in cats and not entry["applies_to_prefixes"]:
            continue
        prefixes = entry["applies_to_prefixes"]
        if prefixes and not any(any(p.startswith(x) for x in prefixes) for p in paths):
            continue
        rel = entry["path"]
        required = request.operation in entry["required_for"]
        path = path_guard.check_path(root, rel)
        if path.is_symlink():
            raise RuntimeError("POLICY_SYMLINK_BLOCKED:" + rel)
        exists = path.is_file()
        doc = {"path": rel, "category": category, "required": required,
               "canonical": entry["canonical"], "reason": entry["reason"],
               "exists": exists}
        if required and not exists:
            missing.append("POLICY_REQUIRED_MISSING:" + rel)
        if exists:
            (selected if required else candidates).append(doc)
        if required and entry["canonical"]:
            canonical.setdefault(category, set()).add(rel)
    for rel in CFG["mandatory_global_files"]:
        path = path_guard.check_path(root, rel)
        if path.is_symlink():
            raise RuntimeError("POLICY_SYMLINK_BLOCKED:" + rel)
        if not path.is_file():
            missing.append("POLICY_REQUIRED_MISSING:" + rel)
        else:
            selected.append({"path": rel, "category": "governance",
                             "required": True, "canonical": False,
                             "reason": "bundled mandatory reference", "exists": True})
    conflicts = ["POLICY_CANONICAL_CONFLICT:" + cat for cat, refs in canonical.items()
                 if len(refs) > 1]
    # Hints are suggestions, never sole proof of approved business policy.
    hint_names = {name.casefold(): category for category in cats
                  for name in CFG["candidate_name_hints"].get(category, ())}
    policy_dir = path_guard.check_path(root, ".agents/.documents")
    if policy_dir.is_dir() and not policy_dir.is_symlink():
        files = sorted(p for p in policy_dir.iterdir()
                       if p.is_file() and not p.is_symlink())
        if len(files) > CFG["limits"]["max_candidate_files"]:
            raise RuntimeError("POLICY_CANDIDATE_LIMIT")
        for file in files:
            if file.name.casefold() in hint_names:
                rel = file.relative_to(root).as_posix()
                if not any(d["path"] == rel for d in selected + candidates):
                    candidates.append({"path": rel, "category": hint_names[file.name.casefold()],
                                       "required": False, "canonical": False,
                                       "reason": "filename hint; authority unverified", "exists": True})
    reasons = sorted(set(missing + conflicts))
    status = ("BLOCKED" if reasons and request.operation in ("implement", "verify", "handoff")
              else "NEEDS_REVIEW" if reasons or (cats and not selected and not candidates)
              else "READY")
    return {"schema_version": 1, "task_id": request.task_id,
            "policy_status": status, "root_agents": agents,
            "selected_categories": sorted(cats),
            "selected_documents": sorted(selected, key=lambda d: d["path"]),
            "candidate_documents": sorted(candidates, key=lambda d: d["path"]),
            "blocking_reasons": reasons if status == "BLOCKED" else [],
            "review_reasons": reasons if status != "BLOCKED" else [],
            "notes": ["Located documents are not proof of approval.",
                      "No host policy files were modified."]}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".")
    p.add_argument("--task-id", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--paths", nargs="*", default=[])
    p.add_argument("--operation", choices=schema.OPERATIONS, default="read")
    p.add_argument("--format", choices=("json", "summary"), default="summary")
    args = p.parse_args()
    try:
        result = resolve(PolicyRequest(Path(args.root), args.task_id, args.task,
                                       tuple(args.paths), args.operation))
        if args.format == "json":
            print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        else:
            print("POLICY_ROUTE | " + result["task_id"] + " | " +
                  result["policy_status"] + " | required=" +
                  str(len(result["selected_documents"])) + " | candidate=" +
                  str(len(result["candidate_documents"])))
        return {"READY": 0, "NEEDS_REVIEW": 3, "BLOCKED": 2}[result["policy_status"]]
    except (RuntimeError, OSError, ValueError) as err:
        print("POLICY_ROUTE_BLOCKED | " + str(err), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
