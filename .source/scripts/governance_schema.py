#!/usr/bin/env python3
"""Strict non-authorizing PLAN-080 configuration and host map validation."""
from __future__ import annotations

import re
from pathlib import PureWindowsPath

PHASES = ("DISCOVER", "SPECIFY_PLAN", "IMPLEMENT", "VERIFY", "HANDOFF_REVIEW")
STATUSES = ("PENDING", "IN_PROGRESS", "READY", "NEEDS_REVIEW", "BLOCKED", "COMPLETE", "INVALIDATED")
OPERATIONS = ("read", "plan", "implement", "verify", "handoff")
WORKFLOW_PATHS = {
    "events": ".agents/state/workflow-events.jsonl",
    "state": ".agents/state/workflow-state.json",
    "lock": ".agents/state/workflow.lock",
}
GOV_LIMITS = {
    "max_selected_paths": 48, "max_host_map_documents": 64,
    "max_candidate_files": 128, "max_agents_files": 32,
    "max_reference_depth": 1, "max_agents_bytes": 131072,
    "max_host_map_bytes": 65536, "max_output_bytes": 262144,
}
WF_LIMITS = {"max_events": 4096, "max_event_bytes": 16384,
             "max_state_bytes": 262144, "max_evidence_refs": 128}
SECRET = (".pem", ".key", ".p12", ".pfx", ".jks", ".keystore")
DENIED = {".git", ".env", ".handoffs", "node_modules", ".venv", "venv",
          ".agents/state", "s2c"}


def safe_path(value: str, suffixes: tuple[str, ...] = (".md", ".json"), prefix: bool = False) -> str:
    if not isinstance(value, str) or not value or len(value) > 512:
        raise ValueError("POLICY_UNSAFE_PATH")
    if ("\\" in value or "\x00" in value or value.startswith("/")
            or PureWindowsPath(value).drive):
        raise ValueError("POLICY_UNSAFE_PATH")
    val = value[:-1] if prefix and value.endswith("/") else value
    if not val or any(p in ("", ".", "..") or ":" in p for p in val.split("/")):
        raise ValueError("POLICY_UNSAFE_PATH")
    parts = [p.casefold() for p in val.split("/")]
    if any(p in DENIED or p.startswith(".env.") or p.endswith(SECRET) for p in parts):
        raise ValueError("POLICY_UNSAFE_PATH")
    if val.casefold().startswith((".agents/state/", ".agents/.handoffs/",
                                   ".agents/skills/", ".git/", "s2c/")):
        raise ValueError("POLICY_UNSAFE_PATH")
    if prefix:
        if not value.endswith("/"):
            raise ValueError("POLICY_UNSAFE_PATH")
    elif suffixes and not val.casefold().endswith(suffixes):
        raise ValueError("POLICY_UNSAFE_PATH")
    return value


def _exact(obj, fields, reason):
    if not isinstance(obj, dict) or set(obj) != set(fields):
        raise ValueError(reason)


def _limits(obj, expected):
    _exact(obj, expected, "CONFIG_INVALID_LIMITS")
    for key, upper in expected.items():
        n = obj[key]
        if type(n) is not int or not 1 <= n <= upper:
            raise ValueError("CONFIG_INVALID_LIMITS")


def validate_config(name: str, cfg: dict) -> None:
    try:
        if not isinstance(cfg, dict) or type(cfg.get("schema_version")) is not int or cfg["schema_version"] != 1:
            raise ValueError("CONFIG_INVALID_SCHEMA")
        if name == "workflow":
            _exact(cfg, ("schema_version", "phases", "statuses", "paths", "limits"),
                   "CONFIG_UNSUPPORTED_FIELD")
            if cfg["phases"] != list(PHASES) or cfg["statuses"] != list(STATUSES):
                raise ValueError("CONFIG_INVALID_WORKFLOW_PROTOCOL")
            if cfg["paths"] != WORKFLOW_PATHS:
                raise ValueError("CONFIG_INVALID_WORKFLOW_PATHS")
            _limits(cfg["limits"], WF_LIMITS)
        elif name == "governance":
            _exact(cfg, ("schema_version", "host_policy_map", "categories",
                         "candidate_name_hints", "mandatory_global_files", "limits"),
                   "CONFIG_UNSUPPORTED_FIELD")
            if cfg["host_policy_map"] != ".agents/policy-map.json":
                raise ValueError("CONFIG_INVALID_POLICY_MAP_PATH")
            categories = cfg["categories"]
            if not isinstance(categories, list) or not 1 <= len(categories) <= 32:
                raise ValueError("CONFIG_INVALID_CATEGORIES")
            ids = []
            for cat in categories:
                _exact(cat, ("id", "keywords"), "CONFIG_INVALID_CATEGORIES")
                if not isinstance(cat["id"], str) or not re.fullmatch(r"[a-z][a-z_]{0,31}", cat["id"]):
                    raise ValueError("CONFIG_INVALID_CATEGORIES")
                ids.append(cat["id"])
                words = cat["keywords"]
                if (not isinstance(words, list) or not 1 <= len(words) <= 32
                        or len(words) != len(set(words))
                        or any(not isinstance(w, str) or not re.fullmatch(r"[a-z][a-z0-9 -]{1,59}", w) for w in words)):
                    raise ValueError("CONFIG_INVALID_CATEGORIES")
            if len(ids) != len(set(ids)):
                raise ValueError("CONFIG_INVALID_CATEGORIES")
            hints = cfg["candidate_name_hints"]
            if not isinstance(hints, dict) or not set(hints).issubset(ids):
                raise ValueError("CONFIG_INVALID_HINTS")
            for values in hints.values():
                if (not isinstance(values, list) or len(values) > 16
                        or len(values) != len(set(values))
                        or any(not isinstance(x, str) or
                               not re.fullmatch(r"[a-z0-9][a-z0-9_.-]*\.md", x) for x in values)):
                    raise ValueError("CONFIG_INVALID_HINTS")
            global_files = cfg["mandatory_global_files"]
            if (not isinstance(global_files, list) or len(global_files) > 16
                    or len(global_files) != len(set(global_files))):
                raise ValueError("CONFIG_INVALID_PATHS")
            for path in global_files:
                safe_path(path)
            _limits(cfg["limits"], GOV_LIMITS)
        else:
            raise ValueError("CONFIG_UNSUPPORTED_SECTION")
    except (ValueError, TypeError) as error:
        raise RuntimeError(str(error)) from error


def validate_host_map(value: object, allowed_categories: set[str], max_docs: int) -> list[dict]:
    """Read-only metadata; never grant authorization or self-approve work."""
    try:
        _exact(value, ("schema_version", "documents"), "POLICY_MAP_MALFORMED")
        if type(value["schema_version"]) is not int or value["schema_version"] != 1:
            raise ValueError("POLICY_MAP_MALFORMED")
        docs = value["documents"]
        if not isinstance(docs, list) or len(docs) > max_docs:
            raise ValueError("POLICY_MAP_MALFORMED")
        out = []
        for doc in docs:
            _exact(doc, ("category", "path", "canonical", "required_for",
                         "applies_to_prefixes", "reason"), "POLICY_MAP_MALFORMED")
            if not isinstance(doc["category"], str) or doc["category"] not in allowed_categories:
                raise ValueError("POLICY_MAP_MALFORMED")
            safe_path(doc["path"])
            if type(doc["canonical"]) is not bool:
                raise ValueError("POLICY_MAP_MALFORMED")
            operations = doc["required_for"]
            if (not isinstance(operations, list) or len(operations) != len(set(operations))
                    or not set(operations).issubset(OPERATIONS)):
                raise ValueError("POLICY_MAP_MALFORMED")
            prefixes = doc["applies_to_prefixes"]
            if (not isinstance(prefixes, list) or len(prefixes) > 16
                    or len(prefixes) != len(set(prefixes))):
                raise ValueError("POLICY_MAP_MALFORMED")
            for prefix in prefixes:
                safe_path(prefix, prefix=True)
            reason = doc["reason"]
            if (not isinstance(reason, str) or len(reason) > 160
                    or any(ord(ch) < 32 or ord(ch) == 127 for ch in reason)):
                raise ValueError("POLICY_MAP_MALFORMED")
            out.append(dict(doc))
        return out
    except (ValueError, TypeError, KeyError) as error:
        raise ValueError("POLICY_MAP_MALFORMED") from error
