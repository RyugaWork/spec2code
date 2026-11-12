#!/usr/bin/env python3
"""Non-autonomous five-stage workflow preflight and integrity journal (PLAN-080).

Read-only status/evaluate never create files. Mutations are restricted to three
managed .agents/state/workflow-* paths. This is NOT a test runner, approval
provider, shell interface, Git client, release signer or Spec Kit executor.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Callable

import config_loader
import governance_schema as schema
import path_guard
import policy_resolver
import scope_io

CFG = config_loader.load("workflow")
PATHS = {name: Path(value) for name, value in CFG["paths"].items()}
LIMITS = CFG["limits"]
ZERO = "0" * 64
MARKER = "spec2code-workflow-v1"
TRANSITIONS = {
    "DISCOVER": {"SPECIFY_PLAN"},
    "SPECIFY_PLAN": {"DISCOVER", "IMPLEMENT"},
    "IMPLEMENT": {"SPECIFY_PLAN", "VERIFY"},
    "VERIFY": {"IMPLEMENT", "SPECIFY_PLAN", "HANDOFF_REVIEW"},
    "HANDOFF_REVIEW": {"VERIFY"},
}


@dataclass(frozen=True)
class WorkflowRequest:
    root: Path
    task_id: str
    phase: str = "DISCOVER"
    operation: str = "status"
    session_id: str | None = None
    evidence_refs: tuple[str, ...] = ()
    reason: str = ""


def _json_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest(event: dict) -> str:
    return hashlib.sha256(_json_bytes({k: v for k, v in event.items()
                                       if k != "event_sha256"})).hexdigest()


def _input(req: WorkflowRequest) -> Path:
    root = path_guard.validate_root(req.root)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", req.task_id):
        raise RuntimeError("WF_INVALID_TASK_ID")
    if req.phase not in schema.PHASES or req.operation not in (
            "status", "evaluate", "begin", "advance", "invalidate", "reconcile", "close"):
        raise RuntimeError("WF_INVALID_ACTION")
    if not isinstance(req.reason, str) or len(req.reason) > 200 or any(
            ord(ch) < 32 or ord(ch) == 127 for ch in req.reason):
        raise RuntimeError("WF_INVALID_REASON")
    if len(req.evidence_refs) > LIMITS["max_evidence_refs"]:
        raise RuntimeError("WF_EVIDENCE_LIMIT")
    for rel in req.evidence_refs:
        if (not isinstance(rel, str) or not rel or len(rel) > 512 or
                rel.startswith("/") or "\\" in rel or ":" in rel or
                ".." in rel.split("/")):
            raise RuntimeError("WF_UNSAFE_EVIDENCE_REF")
        path_guard.check_path(root, rel)
    return root


def _read_json(root: Path, rel: Path | str, limit: int) -> dict | None:
    path = path_guard.check_path(root, rel)
    if not path.is_file():
        return None
    if path.is_symlink():
        raise RuntimeError("WF_UNOWNED_STATE")
    try:
        data = scope_io.read_bytes(root, path, max_bytes=limit)
        value = json.loads(data.decode("utf-8"))
    except (RuntimeError, OSError, ValueError, UnicodeError) as err:
        raise RuntimeError("WF_STATE_INVALID") from err
    if not isinstance(value, dict):
        raise RuntimeError("WF_STATE_INVALID")
    return value


def _session(root: Path, req: WorkflowRequest, active: bool) -> tuple[dict, str]:
    session = _read_json(root, ".agents/state/session.json", 1024 * 1024)
    if not session or not session.get("id") or not session.get("repository_binding"):
        raise RuntimeError("ACTIVE_SESSION_REQUIRED")
    path_guard.assert_scope(root, session["repository_binding"])
    if active and session.get("status") != "ACTIVE":
        raise RuntimeError("ACTIVE_SESSION_REQUIRED")
    if req.session_id and req.session_id != session["id"]:
        raise RuntimeError("WORKFLOW_SESSION_MISMATCH")
    fingerprint = hashlib.sha256(_json_bytes(session["repository_binding"])).hexdigest()
    return session, fingerprint


def _source_snapshot(root: Path) -> str:
    tracked = ("AGENTS.md", ".agents/policy-map.json", ".agents/state/context-pack.json")
    result = []
    for rel in tracked:
        path = path_guard.check_path(root, rel)
        if path.is_symlink():
            raise RuntimeError("WF_INPUT_INVALIDATED")
        if not path.is_file():
            result.append((rel, None))
            continue
        st = path.stat()
        if st.st_size > 4 * 1024 * 1024:
            raise RuntimeError("WF_INPUT_INVALIDATED")
        result.append((rel, hashlib.sha256(
            scope_io.read_bytes(root, path, max_bytes=4 * 1024 * 1024)).hexdigest()))
    return hashlib.sha256(_json_bytes({"files": result})).hexdigest()


def _events(root: Path) -> list[dict]:
    path = path_guard.check_path(root, PATHS["events"])
    if path.is_symlink():
        raise RuntimeError("EVENT_LOG_CORRUPT")
    if not path.is_file():
        return []
    raw = scope_io.read_bytes(root, path, max_bytes=LIMITS["max_events"] *
                              LIMITS["max_event_bytes"] + 1)
    if raw and not raw.endswith(b"\n"):
        raise RuntimeError("EVENT_LOG_CORRUPT")
    lines = raw.splitlines()
    if len(lines) > LIMITS["max_events"]:
        raise RuntimeError("EVENT_LOG_CORRUPT")
    events, prev = [], ZERO
    for i, line in enumerate(lines, 1):
        if not line or len(line) > LIMITS["max_event_bytes"]:
            raise RuntimeError("EVENT_LOG_CORRUPT")
        try:
            event = json.loads(line.decode("utf-8"))
        except (ValueError, UnicodeError) as err:
            raise RuntimeError("EVENT_LOG_CORRUPT") from err
        if (not isinstance(event, dict) or event.get("schema_version") != 1 or
                event.get("sequence") != i or event.get("event_id") != f"WF-{i:06d}" or
                event.get("prev_event_sha256") != prev or
                event.get("event_sha256") != _digest(event) or
                _json_bytes(event) != line):
            raise RuntimeError("EVENT_LOG_CORRUPT")
        if (event.get("phase") not in schema.PHASES or
                event.get("action") not in ("BEGIN", "ADVANCE", "INVALIDATE", "CLOSE") or
                not isinstance(event.get("session_id"), str)):
            raise RuntimeError("EVENT_LOG_CORRUPT")
        events.append(event)
        prev = event["event_sha256"]
    return events


def _replay(events: list[dict]) -> dict | None:
    if not events:
        return None
    first = events[0]
    if (first["action"] != "BEGIN" or first["phase"] != "DISCOVER" or
            first["from_status"] != "PENDING" or first["to_status"] != "IN_PROGRESS"):
        raise RuntimeError("EVENT_LOG_CORRUPT")
    task, session = first["task_id"], first["session_id"]
    phase, status = "DISCOVER", "IN_PROGRESS"
    completed, invalidated = set(), set()
    for event in events[1:]:
        if (event.get("task_id") != task or event.get("session_id") != session or
                event.get("from_status") != status or status == "COMPLETE"):
            raise RuntimeError("EVENT_LOG_CORRUPT")
        action, target, new_status = event["action"], event["phase"], event["to_status"]
        if action == "ADVANCE":
            if (target not in TRANSITIONS[phase] and
                    not (status == "INVALIDATED" and target == phase)):
                raise RuntimeError("EVENT_LOG_CORRUPT")
            if new_status != "IN_PROGRESS":
                raise RuntimeError("EVENT_LOG_CORRUPT")
            if schema.PHASES.index(target) < schema.PHASES.index(phase):
                invalidated.update(schema.PHASES[schema.PHASES.index(target) + 1:])
                completed.difference_update(invalidated)
            elif target != phase:
                completed.add(phase)
            phase, status = target, new_status
            invalidated.discard(phase)
        elif action == "INVALIDATE":
            if new_status != "INVALIDATED":
                raise RuntimeError("EVENT_LOG_CORRUPT")
            phase, status = target, new_status
            invalidated.update(schema.PHASES[schema.PHASES.index(phase):])
            completed.difference_update(invalidated)
        elif action == "CLOSE":
            if (phase != "HANDOFF_REVIEW" or target != phase or
                    new_status != "COMPLETE"):
                raise RuntimeError("EVENT_LOG_CORRUPT")
            status = new_status
            completed.add(phase)
        else:
            raise RuntimeError("EVENT_LOG_CORRUPT")
    return {"schema_version": 1, "managed_by": MARKER, "task_id": task,
            "session_id": session, "current_phase": phase, "phase_status": status,
            "phase_history": [
                {"phase": x, "status": ("COMPLETE" if x in completed else
                 "INVALIDATED" if x in invalidated else
                 status if x == phase else "PENDING")} for x in schema.PHASES],
            "last_event_sha256": events[-1]["event_sha256"],
            "last_sequence": len(events),
            "context_snapshot_sha256": events[-1]["source_snapshot"],
            "binding_fingerprint": events[-1]["binding_fingerprint"],
            "approval_state": "UNKNOWN", "release_authorized": False}


def _state(root: Path, req: WorkflowRequest):
    events = _events(root)
    state = _replay(events)
    cache = _read_json(root, PATHS["state"], LIMITS["max_state_bytes"])
    if cache and cache.get("managed_by") != MARKER:
        raise RuntimeError("WF_UNOWNED_STATE")
    if state and state["task_id"] != req.task_id:
        raise RuntimeError("WF_DIFFERENT_TASK_ACTIVE")
    return events, state, state != cache


def evaluate(req: WorkflowRequest) -> dict:
    root = _input(req)
    events, current, stale = _state(root, req)
    phase = current["current_phase"] if req.operation == "status" and current else req.phase
    blocking, review, passed = [], [], ["GT-015"]
    if stale:
        review.append("STATE_STALE")
    try:
        session, binding = _session(root, req, active=phase in ("IMPLEMENT", "VERIFY"))
        passed.append("GT-001")
    except RuntimeError as err:
        session, binding = None, None
        if phase in ("DISCOVER", "SPECIFY_PLAN") and str(err) == "ACTIVE_SESSION_REQUIRED":
            review.append("GT-006")
        else:
            blocking.append("GT-006")
    try:
        policy = policy_resolver.resolve(policy_resolver.PolicyRequest(
            root, req.task_id, "Review project governance", (),
            "implement" if phase in ("IMPLEMENT", "VERIFY", "HANDOFF_REVIEW") else "plan"))
        if policy["policy_status"] == "BLOCKED":
            blocking.append("GT-002")
        elif policy["policy_status"] == "NEEDS_REVIEW":
            review.append("GT-002")
        else:
            passed.append("GT-002")
    except (RuntimeError, OSError, ValueError):
        blocking.append("GT-002")
        policy = {"policy_status": "BLOCKED"}
    if current:
        if session and (current["session_id"] != session["id"] or
                        current["binding_fingerprint"] != binding):
            blocking.append("WORKFLOW_SESSION_MISMATCH")
        if current["context_snapshot_sha256"] != _source_snapshot(root):
            blocking.append("GT-014")
        if current["phase_status"] == "INVALIDATED":
            blocking.append("GT-014")
    if phase in ("SPECIFY_PLAN", "IMPLEMENT", "VERIFY", "HANDOFF_REVIEW"):
        review += ["GT-003", "GT-004"]
    if phase in ("IMPLEMENT", "VERIFY", "HANDOFF_REVIEW"):
        review += ["GT-007", "GT-008"]
    if phase in ("VERIFY", "HANDOFF_REVIEW"):
        review += ["GT-009", "GT-010"]
    if phase == "HANDOFF_REVIEW":
        review += ["GT-011", "GT-012", "GT-013"]
    status = "BLOCKED" if blocking else "NEEDS_REVIEW" if review else "READY"
    return {"schema_version": 1, "task_id": req.task_id, "phase": phase,
            "current_phase": current["current_phase"] if current else None,
            "phase_status": current["phase_status"] if current else "UNINITIALIZED",
            "gate_status": status, "machine_passed": sorted(set(passed)),
            "review_gates": sorted(set(review)),
            "blocking_gates": sorted(set(blocking)),
            "policy_status": policy["policy_status"], "state_stale": stale,
            "release_authorized": False, "can_grant_permissions": False}


@contextmanager
def _lock(root: Path):
    path = path_guard.check_path(root, PATHS["lock"])
    if path.exists() or path.is_symlink():
        raise RuntimeError("WORKFLOW_LOCKED")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY |
                     getattr(os, "O_NOFOLLOW", 0), 0o600)
    except FileExistsError as err:
        raise RuntimeError("WORKFLOW_LOCKED") from err
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(MARKER.encode())
        yield
    finally:
        if path.is_file():
            raw = scope_io.read_bytes(root, path, max_bytes=1024)
            if raw != MARKER.encode():
                raise RuntimeError("WORKFLOW_LOCK_CORRUPT")
            scope_io.unlink_verified(root, path, hashlib.sha256(raw).hexdigest())


def _write(root: Path, old: list[dict], record: dict) -> dict:
    path = path_guard.check_path(root, PATHS["events"])
    if len(old) >= LIMITS["max_events"]:
        raise RuntimeError("WF_EVENT_CAP")
    if not path.exists():
        scope_io.atomic_text(root, path, "")
    scope_io.append_text(root, path, _json_bytes(record).decode("utf-8") + "\n")
    verified = _events(root)
    if (len(verified) != len(old) + 1 or
            verified[-1]["event_sha256"] != record["event_sha256"]):
        raise RuntimeError("WF_JOURNAL_WRITE_UNVERIFIED")
    state = _replay(verified)
    content = json.dumps(state, sort_keys=True, indent=2) + "\n"
    if len(content.encode()) > LIMITS["max_state_bytes"]:
        raise RuntimeError("WF_STATE_TOO_LARGE")
    scope_io.atomic_text(root, PATHS["state"], content)
    return state


def transition(req: WorkflowRequest, *,
               trusted_gate_check: Callable[[str, WorkflowRequest], bool] | None = None) -> dict:
    root = _input(req)
    if req.operation not in ("begin", "advance", "invalidate", "reconcile", "close"):
        raise RuntimeError("WF_INVALID_ACTION")
    session, binding = _session(root, req, active=req.operation not in ("reconcile", "close"))
    with _lock(root):
        session, binding = _session(root, req, active=req.operation not in ("reconcile", "close"))
        prior, current, stale = _state(root, req)
        if current and (current["session_id"] != session["id"] or
                        current["binding_fingerprint"] != binding):
            raise RuntimeError("WORKFLOW_SESSION_MISMATCH")
        if req.operation == "reconcile":
            if not stale:
                return {"operation": "reconcile", "status": "READY", "reconciled": False}
            if not current:
                raise RuntimeError("WF_RECONCILE_BLOCKED")
            scope_io.atomic_text(root, PATHS["state"],
                                 json.dumps(current, sort_keys=True, indent=2) + "\n")
            return {"operation": "reconcile", "status": "READY", "reconciled": True}
        if stale:
            raise RuntimeError("STATE_STALE")
        if req.operation == "begin":
            if current:
                raise RuntimeError("WF_ALREADY_STARTED")
            action, target, to_status = "BEGIN", "DISCOVER", "IN_PROGRESS"
        elif current is None:
            raise RuntimeError("WF_NOT_STARTED")
        elif req.operation == "invalidate":
            if current["phase_status"] == "COMPLETE":
                raise RuntimeError("WF_ALREADY_CLOSED")
            action, target, to_status = "INVALIDATE", req.phase, "INVALIDATED"
        elif req.operation == "advance":
            target = req.phase
            resume = current["phase_status"] == "INVALIDATED" and target == current["current_phase"]
            backward = (target in TRANSITIONS[current["current_phase"]] and
                        schema.PHASES.index(target) < schema.PHASES.index(current["current_phase"]))
            if (target not in TRANSITIONS[current["current_phase"]] and not resume) or current["phase_status"] not in ("IN_PROGRESS", "INVALIDATED"):
                raise RuntimeError("WF_ILLEGAL_TRANSITION")
            if not backward and not resume:
                decision = evaluate(WorkflowRequest(root, req.task_id, current["current_phase"],
                                                    "evaluate", session["id"]))
                if decision["gate_status"] == "BLOCKED":
                    raise RuntimeError("WF_EXIT_GATE_BLOCKED")
                if decision["gate_status"] == "NEEDS_REVIEW":
                    if trusted_gate_check is None or not all(
                            trusted_gate_check(gate, req) for gate in decision["review_gates"]):
                        raise RuntimeError("WF_APPROVAL_REQUIRED")
            action, to_status = "ADVANCE", "IN_PROGRESS"
        else:
            if current["current_phase"] != "HANDOFF_REVIEW":
                raise RuntimeError("WF_ILLEGAL_TRANSITION")
            decision = evaluate(WorkflowRequest(root, req.task_id, "HANDOFF_REVIEW",
                                                "evaluate", session["id"]))
            if decision["gate_status"] == "BLOCKED":
                raise RuntimeError("WF_EXIT_GATE_BLOCKED")
            if decision["gate_status"] == "NEEDS_REVIEW":
                if trusted_gate_check is None or not all(
                        trusted_gate_check(gate, req) for gate in decision["review_gates"]):
                    raise RuntimeError("WF_APPROVAL_REQUIRED")
            action, target, to_status = "CLOSE", "HANDOFF_REVIEW", "COMPLETE"
        record = {"schema_version": 1, "sequence": len(prior) + 1,
                  "event_id": f"WF-{len(prior)+1:06d}", "task_id": req.task_id,
                  "session_id": session["id"], "phase": target, "action": action,
                  "from_status": current["phase_status"] if current else "PENDING",
                  "to_status": to_status,
                  "observed_at": datetime.now(timezone.utc).isoformat(),
                  "source_snapshot": _source_snapshot(root),
                  "binding_fingerprint": binding,
                  "evidence_refs": list(req.evidence_refs),
                  "reason_codes": ["INPUT_INVALIDATED" if action == "INVALIDATE" else "EXPLICIT_TRANSITION"],
                  "prev_event_sha256": prior[-1]["event_sha256"] if prior else ZERO}
        record["event_sha256"] = _digest(record)
        if len(_json_bytes(record)) > LIMITS["max_event_bytes"]:
            raise RuntimeError("WF_EVENT_TOO_LARGE")
        updated = _write(root, prior, record)
        return {"operation": req.operation, "status": "READY",
                "current_phase": updated["current_phase"],
                "phase_status": updated["phase_status"],
                "last_sequence": updated["last_sequence"],
                "release_authorized": False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    sub = parser.add_subparsers(dest="operation", required=True)
    for action in ("status", "evaluate", "begin", "advance", "invalidate", "reconcile", "close"):
        p = sub.add_parser(action)
        p.add_argument("--task-id", required=True)
        if action in ("evaluate", "invalidate"):
            p.add_argument("--phase", choices=schema.PHASES, default="DISCOVER")
        if action == "advance":
            p.add_argument("--to", choices=schema.PHASES, required=True)
        if action in ("begin", "advance", "invalidate", "reconcile", "close"):
            p.add_argument("--session-id")
        if action == "invalidate":
            p.add_argument("--reason", default="")
        if action in ("advance", "close"):
            p.add_argument("--evidence-ref", action="append", default=[])
    args = parser.parse_args(argv)
    phase = getattr(args, "to", None) or getattr(args, "phase", "DISCOVER")
    req = WorkflowRequest(Path(args.root), args.task_id, phase, args.operation,
                          getattr(args, "session_id", None),
                          tuple(getattr(args, "evidence_ref", ())),
                          getattr(args, "reason", ""))
    try:
        result = (evaluate(req) if args.operation in ("status", "evaluate")
                  else transition(req))
        print(json.dumps(result, sort_keys=True))
        status = result.get("gate_status", result.get("status"))
        return {"READY": 0, "NEEDS_REVIEW": 3, "BLOCKED": 4}.get(status, 0)
    except (OSError, RuntimeError, ValueError) as err:
        reason = str(err)
        safe = reason if re.fullmatch(r"[A-Z][A-Z0-9_]{2,79}", reason) else "WF_TECHNICAL_ERROR"
        print("WORKFLOW_GUARD_FAILED | " + safe, file=sys.stderr)
        return 3 if safe == "WF_APPROVAL_REQUIRED" else 2


if __name__ == "__main__":
    sys.exit(main())
