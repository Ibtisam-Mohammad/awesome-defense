#!/usr/bin/env python3
"""Audit README resources for curation risks and repository metadata."""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone

try:
    from datetime import UTC
except ImportError:
    UTC = timezone.utc
from pathlib import Path


SOURCE_HOSTS = {
    "github.com",
    "gitlab.com",
    "gitlab.kitware.com",
    "gitlab.orekit.org",
    "codeberg.org",
    "sourceforge.net",
}
DATA_HOSTS = {
    "arxiv.org",
    "zenodo.org",
    "celestrak.org",
    "firms.modaps.eosdis.nasa.gov",
    "damage.conflict-ecology.org",
    "fpv.ifi.uzh.ch",
    "oballinger.github.io",
    "projects.asl.ethz.ch",
}
EXEMPT_ENTRY_SECTIONS = {"Contents", "Related Topics To Watch"}
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}
TYPE_TAGS = {
    "OSS",
    "Source-available",
    "HW",
    "Dataset",
    "Paper",
    "Standard",
    "Index",
}
USER_AGENT = "awesome-defense-resource-audit"
GITLAB_HOSTS = {"gitlab.com", "gitlab.kitware.com", "gitlab.orekit.org"}
GITHUB_NON_REPO_PATHS = {
    "about",
    "collections",
    "events",
    "explore",
    "features",
    "issues",
    "login",
    "marketplace",
    "notifications",
    "pricing",
    "pulls",
    "search",
    "settings",
    "sponsors",
    "topics",
    "trending",
}
CODEBERG_NON_REPO_PATHS = {
    "explore",
    "issues",
    "notifications",
    "pulls",
    "repo",
    "user",
}


@dataclass(frozen=True)
class Entry:
    line_no: int
    section: str
    name: str
    url: str
    description: str
    tags: tuple[str, ...]


@dataclass(frozen=True)
class GithubTarget:
    owner: str
    repo: str | None
    path: str

    @property
    def key(self) -> str:
        return self.owner if self.repo is None else f"{self.owner}/{self.repo}"

    @property
    def clone_url(self) -> str | None:
        if self.repo is None:
            return None
        return f"https://github.com/{self.owner}/{self.repo}.git"


@dataclass(frozen=True)
class SourceTarget:
    host: str
    kind: str
    key: str
    check_url: str
    clone_url: str | None = None
    path: str = ""

    @property
    def check_method(self) -> str:
        return "git" if self.clone_url else "http"


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def parse_entries(readme: Path) -> list[Entry]:
    entries: list[Entry] = []
    section = ""
    pattern = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)\s+-\s+(.+)$")

    for line_no, line in enumerate(readme.read_text(encoding="utf-8").splitlines(), start=1):
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)
            continue
        match = pattern.match(line)
        if not match or section in EXEMPT_ENTRY_SECTIONS:
            continue
        name, url, description = match.groups()
        tags = tuple(re.findall(r"`([^`]+)`", description))
        entries.append(Entry(line_no, section, name, url, description, tags))
    return entries


def plain_description(description: str) -> str:
    return re.sub(r"\s*`[^`]+`", "", description).strip()


def host(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


def github_target(url: str) -> GithubTarget | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        return None
    if parts[0] == "orgs" and len(parts) >= 2:
        return GithubTarget(owner=parts[1], repo=None, path="/".join(parts[2:]))
    if parts[0] in GITHUB_NON_REPO_PATHS:
        return None
    owner = parts[0]
    repo = parts[1].removesuffix(".git") if len(parts) >= 2 else None
    path = "/".join(parts[2:])
    return GithubTarget(owner=owner, repo=repo, path=path)


def github_source_target(url: str) -> SourceTarget | None:
    target = github_target(url)
    if target is None:
        return None
    if target.repo is None:
        return SourceTarget(
            host="github.com",
            kind="github-owner",
            key=target.key,
            check_url=f"https://github.com/{target.owner}",
            path=target.path,
        )
    return SourceTarget(
        host="github.com",
        kind="github-repo",
        key=target.key,
        check_url=f"https://github.com/{target.owner}/{target.repo}",
        clone_url=target.clone_url,
        path=target.path,
    )


def gitlab_source_target(url: str) -> SourceTarget | None:
    parsed = urllib.parse.urlparse(url)
    target_host = parsed.netloc.lower()
    if target_host not in GITLAB_HOSTS:
        return None
    parts = [part.removesuffix(".git") for part in parsed.path.split("/") if part]
    if not parts:
        return None
    if "-" in parts:
        marker_index = parts.index("-")
        repo_parts = parts[:marker_index]
        path = "/".join(parts[marker_index + 1 :])
    else:
        repo_parts = parts
        path = ""
    if not repo_parts:
        return None
    if len(repo_parts) == 1:
        owner = repo_parts[0]
        return SourceTarget(
            host=target_host,
            kind="gitlab-group",
            key=f"{target_host}/{owner}",
            check_url=f"https://{target_host}/{owner}",
            path=path,
        )

    repo_path = "/".join(repo_parts)
    return SourceTarget(
        host=target_host,
        kind="gitlab-repo",
        key=f"{target_host}/{repo_path}",
        check_url=f"https://{target_host}/{repo_path}",
        clone_url=f"https://{target_host}/{repo_path}.git",
        path=path,
    )


def sourceforge_source_target(url: str) -> SourceTarget | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "sourceforge.net":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 2 and parts[0] in {"projects", "p"}:
        project = parts[1]
        return SourceTarget(
            host="sourceforge.net",
            kind="sourceforge-project",
            key=f"sourceforge.net/projects/{project}",
            check_url=f"https://sourceforge.net/projects/{project}/",
            path="/".join(parts[2:]),
        )
    return None


def codeberg_source_target(url: str) -> SourceTarget | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "codeberg.org":
        return None
    parts = [part.removesuffix(".git") for part in parsed.path.split("/") if part]
    if not parts or parts[0] in CODEBERG_NON_REPO_PATHS:
        return None
    if len(parts) == 1:
        owner = parts[0]
        return SourceTarget(
            host="codeberg.org",
            kind="codeberg-owner",
            key=f"codeberg.org/{owner}",
            check_url=f"https://codeberg.org/{owner}",
        )

    owner, repo = parts[:2]
    return SourceTarget(
        host="codeberg.org",
        kind="codeberg-repo",
        key=f"codeberg.org/{owner}/{repo}",
        check_url=f"https://codeberg.org/{owner}/{repo}",
        clone_url=f"https://codeberg.org/{owner}/{repo}.git",
        path="/".join(parts[2:]),
    )


def source_target(url: str) -> SourceTarget | None:
    parsed = urllib.parse.urlparse(url)
    target_host = parsed.netloc.lower()
    if target_host == "github.com":
        return github_source_target(url)
    if target_host in GITLAB_HOSTS:
        return gitlab_source_target(url)
    if target_host == "sourceforge.net":
        return sourceforge_source_target(url)
    if target_host == "codeberg.org":
        return codeberg_source_target(url)
    return None


def load_cache(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_cache(path: Path, data: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def is_cache_fresh(record: dict, max_age_days: int) -> bool:
    checked_at = record.get("checked_at")
    if not checked_at:
        return False
    try:
        checked = datetime.fromisoformat(checked_at)
    except ValueError:
        return False
    return (datetime.now(UTC) - checked).days <= max_age_days


def is_source_cache_fresh(target: SourceTarget, record: dict, max_age_days: int) -> bool:
    return record.get("kind") == target.kind and is_cache_fresh(record, max_age_days)


def git_remote_check(target: SourceTarget, timeout: int) -> tuple[str, dict]:
    if target.clone_url is None:
        raise ValueError(f"{target.key} does not have a clone URL")
    command = ["git", "ls-remote", "--symref", target.clone_url, "HEAD"]
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            env=env,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return target.key, {
            "checked_at": now_iso(),
            "kind": target.kind,
            "host": target.host,
            "check": target.check_method,
            "ok": False,
            "default_branch": None,
            "error": f"timeout after {timeout}s",
        }

    default_branch = None
    for line in completed.stdout.splitlines():
        match = re.match(r"ref:\s+refs/heads/([^\s]+)\s+HEAD$", line)
        if match:
            default_branch = match.group(1)
            break

    return target.key, {
        "checked_at": now_iso(),
        "kind": target.kind,
        "host": target.host,
        "check": target.check_method,
        "ok": completed.returncode == 0,
        "default_branch": default_branch,
        "error": None if completed.returncode == 0 else (completed.stderr.strip() or "git ls-remote failed")[:400],
    }


def http_status_check(url: str, timeout: int) -> tuple[int | None, str | None]:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "User-Agent": USER_AGENT,
    }
    last_error = None
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, None
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:300]
            last_error = body or exc.reason
            if method == "HEAD" and exc.code in {403, 405}:
                continue
            return exc.code, last_error
        except Exception as exc:  # noqa: BLE001 - compact audit error.
            last_error = f"{type(exc).__name__}: {str(exc)[:300]}"
            if method == "HEAD":
                continue
            return None, last_error
    return None, last_error


def http_source_check(target: SourceTarget, timeout: int) -> tuple[str, dict]:
    status, error = http_status_check(target.check_url, timeout)
    return target.key, {
        "checked_at": now_iso(),
        "kind": target.kind,
        "host": target.host,
        "check": target.check_method,
        "ok": status is not None and 200 <= status < 400,
        "status": status,
        "error": error,
    }


def can_fallback_to_project_page(record: dict) -> bool:
    error = record.get("error") or ""
    return any(
        marker in error.lower()
        for marker in (
            "timeout after",
            "operation timed out",
            "connection timed out",
            "failed to connect",
            "network is unreachable",
        )
    )


def source_check(target: SourceTarget, timeout: int) -> tuple[str, dict]:
    if target.clone_url:
        key, record = git_remote_check(target, timeout)
        if (
            not record.get("ok")
            and target.kind in {"gitlab-repo", "codeberg-repo"}
            and can_fallback_to_project_page(record)
        ):
            status, error = http_status_check(target.check_url, timeout)
            if status is not None and 200 <= status < 400:
                record.update(
                    {
                        "check": "git+http-fallback",
                        "git_error": record.get("error"),
                        "ok": True,
                        "status": status,
                        "error": None,
                    }
                )
            else:
                record["status"] = status
                record["http_error"] = error
        return key, record
    return http_source_check(target, timeout)


def refresh_source_cache(
    targets: list[SourceTarget],
    cache: dict[str, dict],
    max_age_days: int,
    workers: int,
    timeout: int,
) -> dict[str, dict]:
    stale = [
        target
        for target in targets
        if not is_source_cache_fresh(target, cache.get(target.key, {}), max_age_days)
    ]
    if not stale:
        return cache

    print(f"Checking {len(stale)} source targets...")
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        checks = [executor.submit(source_check, target, timeout) for target in stale]
        for index, future in enumerate(futures.as_completed(checks), start=1):
            key, record = future.result()
            cache[key] = record
            if index % 50 == 0 or index == len(checks):
                print(f"Checked {index}/{len(stale)} source targets")
    return cache


def github_api_request(path: str, token: str | None, timeout: int) -> tuple[int | None, dict | None, str | None]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8")), None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:300]
        return exc.code, None, body
    except Exception as exc:  # noqa: BLE001 - compact audit error.
        return None, None, f"{type(exc).__name__}: {str(exc)[:300]}"


def refresh_api_cache(
    targets: list[GithubTarget],
    cache: dict[str, dict],
    token: str | None,
    allow_unauthenticated: bool,
    max_age_days: int,
    timeout: int,
) -> dict[str, dict]:
    if not token and not allow_unauthenticated:
        return cache

    repo_targets = [target for target in targets if target.repo is not None]
    stale = [
        target
        for target in repo_targets
        if not is_cache_fresh(cache.get(target.key, {}), max_age_days)
    ]
    if not stale:
        return cache

    print(f"Checking {len(stale)} GitHub repos with REST API...")
    for index, target in enumerate(stale, start=1):
        status, data, error = github_api_request(f"/repos/{target.owner}/{target.repo}", token, timeout)
        if data:
            cache[target.key] = {
                "checked_at": now_iso(),
                "ok": True,
                "status": status,
                "name": data.get("full_name"),
                "description": data.get("description"),
                "archived": data.get("archived"),
                "disabled": data.get("disabled"),
                "fork": data.get("fork"),
                "stars": data.get("stargazers_count"),
                "forks": data.get("forks_count"),
                "open_issues": data.get("open_issues_count"),
                "license": (data.get("license") or {}).get("spdx_id"),
                "default_branch": data.get("default_branch"),
                "pushed_at": data.get("pushed_at"),
                "updated_at": data.get("updated_at"),
                "topics": data.get("topics", []),
                "homepage": data.get("homepage"),
            }
        else:
            cache[target.key] = {
                "checked_at": now_iso(),
                "ok": False,
                "status": status,
                "error": error,
            }
        if index % 25 == 0 or index == len(stale):
            print(f"Checked {index}/{len(stale)} GitHub API records")
        if status == 403 and not token:
            print("Unauthenticated GitHub API rate limit hit; stopping API checks.")
            break
        time.sleep(0.05)
    return cache


def is_source_like(entry: Entry) -> bool:
    return host(entry.url) in SOURCE_HOSTS


def issue(
    issues: list[dict],
    entry: Entry,
    severity: str,
    kind: str,
    detail: str,
    suggestion: str,
) -> None:
    issues.append(
        {
            "line": entry.line_no,
            "section": entry.section,
            "name": entry.name,
            "url": entry.url,
            "severity": severity,
            "kind": kind,
            "detail": detail,
            "suggestion": suggestion,
        }
    )


def analyze_entries(
    entries: list[Entry],
    source_cache: dict[str, dict],
    api_cache: dict[str, dict],
    stale_years: int,
) -> tuple[list[dict], list[dict]]:
    issues: list[dict] = []
    suggestions: list[dict] = []

    for entry in entries:
        tags = set(entry.tags)
        target = github_target(entry.url)
        source = source_target(entry.url)
        entry_host = host(entry.url)

        if tags == {"Dual-use"}:
            issue(
                issues,
                entry,
                "high",
                "type-tag-missing",
                "Entry is tagged only as Dual-use, which does not identify resource type.",
                "Add a concrete type tag such as OSS, HW, Dataset, Standard, Paper, or Index, or remove the entry.",
            )

        if "OSS" in tags and not is_source_like(entry):
            issue(
                issues,
                entry,
                "medium",
                "oss-tag-on-non-source-url",
                f"`OSS` tag appears on a non-source host: {entry_host}.",
                "Link to the source repository directly or remove the OSS tag.",
            )

        if entry_host not in SOURCE_HOSTS | DATA_HOSTS and not (TYPE_TAGS & tags):
            issue(
                issues,
                entry,
                "medium",
                "external-url-needs-type-review",
                f"External host `{entry_host}` is not a known source or data host.",
                "Confirm this is a reusable technical project page, not context/news/marketing.",
            )

        if entry_host in SOURCE_HOSTS and source is None:
            issue(
                issues,
                entry,
                "high",
                "github-url-unparsed" if entry_host == "github.com" else "source-url-unparsed",
                f"Source URL on `{entry_host}` could not be parsed as a supported owner, repository, project, or path.",
                "Fix the URL, point to the canonical project/repository page, or remove the entry.",
            )

        if target and target.repo is None and "Index" not in tags:
            issue(
                issues,
                entry,
                "low",
                "github-organization-entry",
                "Entry links to a GitHub organization or user rather than a specific repository.",
                "Use the `Index` tag for intentional source hubs or replace with a specific repository.",
            )

        if source:
            source_record = source_cache.get(source.key)
            if (
                source_record
                and source_record.get("kind") == source.kind
                and not source_record.get("ok")
            ):
                check_name = "git ls-remote" if source.clone_url else "HTTP status check"
                issue_kind = "github-remote-failed" if source.kind == "github-repo" else "source-check-failed"
                issue(
                    issues,
                    entry,
                    "high",
                    issue_kind,
                    source_record.get("error") or f"{check_name} failed.",
                    "Fix the URL, replace with the current project or repository, or remove the entry.",
                )

            if source.path and source.kind not in {"github-repo"}:
                issue(
                    issues,
                    entry,
                    "low",
                    "source-deep-link",
                    "Entry points to a path inside a source host project.",
                    "Prefer the repository or project URL unless the path is the reusable resource being indexed.",
                )

        if target and target.repo:
            if target.path:
                issue(
                    issues,
                    entry,
                    "low",
                    "github-deep-link",
                    "Entry points to a path inside a repository.",
                    "Prefer the repository URL unless the path is the reusable resource being indexed.",
                )

            api_record = api_cache.get(target.key)
            if api_record and api_record.get("ok"):
                if api_record.get("archived") and "Archive" not in tags:
                    issue(
                        issues,
                        entry,
                        "medium",
                        "archived-repo-missing-archive-tag",
                        "GitHub marks this repository as archived.",
                        "Add `Archive` or replace with an active successor.",
                    )

                license_id = api_record.get("license")
                if "OSS" in tags and license_id in {None, "NOASSERTION"}:
                    issue(
                        issues,
                        entry,
                        "medium",
                        "oss-license-unverified",
                        "GitHub API did not expose a repository license.",
                        "Confirm the project has an open-source license, remove `OSS`, or remove the entry.",
                    )

                pushed_at = api_record.get("pushed_at")
                age_years = None
                if pushed_at and "Archive" not in tags:
                    pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
                    age_years = (datetime.now(UTC) - pushed).days / 365.25
                    if age_years >= stale_years:
                        issue(
                            issues,
                            entry,
                            "medium",
                            "stale-repo-without-archive-tag",
                            f"Last pushed {age_years:.1f} years ago.",
                            "Confirm the project is still useful; add `Archive` or remove if superseded.",
                        )

                if api_record.get("fork") and "Archive" not in tags and "Fork" not in tags:
                    issue(
                        issues,
                        entry,
                        "low",
                        "github-fork-entry",
                        "GitHub marks this repository as a fork.",
                        "Prefer the upstream repository unless the fork has unique curated value.",
                    )

                stars = api_record.get("stars")
                if (
                    stars is not None
                    and stars < 5
                    and license_id in {None, "NOASSERTION"}
                    and (age_years is None or age_years >= 2)
                    and "Archive" not in tags
                ):
                    issue(
                        issues,
                        entry,
                        "low",
                        "low-reuse-heuristic",
                        "Repository has low adoption signals and no API-visible license.",
                        "Review manually for spam, toy status, or weak reusable value.",
                    )

                description = api_record.get("description")
                if description:
                    suggestions.append(
                        {
                            "line": entry.line_no,
                            "section": entry.section,
                            "name": entry.name,
                            "url": entry.url,
                            "current": plain_description(entry.description),
                            "github_description": description.strip(),
                            "suggested_entry": f"- [{entry.name}]({entry.url}) - {description.strip().rstrip('.')}. "
                            + " ".join(f"`{tag}`" for tag in entry.tags),
                        }
                    )

    return issues, suggestions


def unique_source_targets(entries: list[Entry]) -> list[SourceTarget]:
    targets = {}
    for entry in entries:
        target = source_target(entry.url)
        if target:
            targets[target.key] = target
    return sorted(targets.values(), key=lambda item: (item.host, item.kind, item.key.lower()))


def source_coverage(
    entries: list[Entry],
    source_cache: dict[str, dict],
    max_age_days: int,
) -> list[dict]:
    buckets: dict[tuple[str, str], dict] = defaultdict(
        lambda: {
            "entries": 0,
            "target_keys": set(),
            "checked": 0,
            "ok": 0,
            "failed": 0,
            "unchecked": 0,
        }
    )
    targets = {target.key: target for target in unique_source_targets(entries)}

    for entry in entries:
        entry_host = host(entry.url)
        if entry_host not in SOURCE_HOSTS:
            continue
        target = source_target(entry.url)
        kind = target.kind if target else "unparsed"
        bucket = buckets[(entry_host, kind)]
        bucket["entries"] += 1
        if target:
            bucket["target_keys"].add(target.key)

    for target in targets.values():
        bucket = buckets[(target.host, target.kind)]
        record = source_cache.get(target.key, {})
        if is_source_cache_fresh(target, record, max_age_days):
            bucket["checked"] += 1
            if record.get("ok"):
                bucket["ok"] += 1
            else:
                bucket["failed"] += 1
        else:
            bucket["unchecked"] += 1

    rows = []
    for (entry_host, kind), bucket in buckets.items():
        rows.append(
            {
                "host": entry_host,
                "kind": kind,
                "entries": bucket["entries"],
                "targets": len(bucket["target_keys"]),
                "checked": bucket["checked"],
                "ok": bucket["ok"],
                "failed": bucket["failed"],
                "unchecked": bucket["unchecked"],
            }
        )
    return sorted(rows, key=lambda item: (item["host"], item["kind"]))


def render_report(
    entries: list[Entry],
    issues: list[dict],
    suggestions: list[dict],
    source_cache: dict[str, dict],
    api_cache: dict[str, dict],
    max_age_days: int,
    token_available: bool,
) -> str:
    severity_counts = Counter(issue["severity"] for issue in issues)
    kind_counts = Counter(issue["kind"] for issue in issues)
    host_counts = Counter(host(entry.url) for entry in entries)
    source_targets = unique_source_targets(entries)
    coverage_rows = source_coverage(entries, source_cache, max_age_days)
    active_source_records = sum(row["checked"] for row in coverage_rows)
    active_github_repo_keys = {
        target.key for target in unique_github_targets(entries) if target.repo is not None
    }
    active_api_records = sum(1 for key in active_github_repo_keys if key in api_cache)

    lines = [
        "# Resource Audit",
        "",
        "Maintainer curation report produced by `scripts/audit_resources.py`.",
        "",
        "This report is a curation review queue, not an automatic removal list. It combines deterministic checks with metadata-derived review prompts.",
        "",
        "## Summary",
        "",
        f"- Resource entries: {len(entries)}",
        f"- Unique URLs: {len({entry.url for entry in entries})}",
        f"- Hosts: {len(host_counts)}",
        f"- Source targets parsed: {len(source_targets)}",
        f"- Current source check records for active targets: {active_source_records}/{len(source_targets)}",
        f"- GitHub API metadata records cached for active repo targets: {active_api_records}",
        f"- GitHub token available for this run: {'yes' if token_available else 'no'}",
        f"- Open audit issues: {len(issues)}",
        "",
    ]

    if severity_counts:
        lines.extend(["## Issues By Severity", ""])
        for severity, count in sorted(severity_counts.items(), key=lambda item: SEVERITY_ORDER.get(item[0], 99)):
            lines.append(f"- `{severity}`: {count}")
        lines.append("")

    if kind_counts:
        lines.extend(["## Issues By Type", ""])
        for kind, count in kind_counts.most_common():
            lines.append(f"- `{kind}`: {count}")
        lines.append("")

    lines.extend(["## Host Distribution", ""])
    for entry_host, count in host_counts.most_common():
        lines.append(f"- `{entry_host}`: {count}")
    lines.append("")

    if coverage_rows:
        lines.extend(
            [
                "## Source Check Coverage",
                "",
                "| Host | Type | Entries | Targets | Current checks | OK | Failed | Unchecked |",
                "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in coverage_rows:
            lines.append(
                f"| `{row['host']}` | `{row['kind']}` | {row['entries']} | {row['targets']} | "
                f"{row['checked']} | {row['ok']} | {row['failed']} | {row['unchecked']} |"
            )
        lines.append("")

    if issues:
        lines.extend(["## Audit Queue", ""])
        for item in sorted(issues, key=lambda value: (SEVERITY_ORDER.get(value["severity"], 99), value["line"])):
            lines.append(
                f"- `{item['severity']}` `{item['kind']}` [README.md:{item['line']}](../README.md#L{item['line']}) "
                f"`{item['section']}` / {item['name']}: {item['detail']} "
                f"Suggested action: {item['suggestion']}"
            )
        lines.append("")

    if suggestions:
        lines.extend(
            [
                "## GitHub Description Suggestions",
                "",
                "These are raw GitHub repository descriptions. Use them as grounding, not as automatic replacements.",
                "",
            ]
        )
        for item in sorted(suggestions, key=lambda value: value["line"]):
            lines.append(f"### [README.md:{item['line']}](../README.md#L{item['line']}) {item['name']}")
            lines.append("")
            lines.append(f"- Current: {item['current']}")
            lines.append(f"- GitHub: {item['github_description']}")
            lines.append("")
            lines.append("```md")
            lines.append(item["suggested_entry"])
            lines.append("```")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def unique_github_targets(entries: list[Entry]) -> list[GithubTarget]:
    targets = {}
    for entry in entries:
        target = github_target(entry.url)
        if target:
            targets[target.key] = target
    return sorted(targets.values(), key=lambda item: item.key.lower())


def print_source_coverage(rows: list[dict]) -> None:
    if not rows:
        return
    print("Source coverage:")
    for row in rows:
        if row["targets"]:
            print(
                f"  {row['host']} / {row['kind']}: "
                f"{row['checked']}/{row['targets']} current checks "
                f"({row['entries']} entries, {row['failed']} failed)"
            )
        else:
            print(f"  {row['host']} / {row['kind']}: {row['entries']} entries")


def failing_issue_count(issues: list[dict], severity: str) -> int:
    threshold = SEVERITY_ORDER[severity]
    return sum(1 for item in issues if SEVERITY_ORDER.get(item["severity"], 99) <= threshold)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", nargs="?", default=Path("README.md"), type=Path)
    parser.add_argument("--cache-dir", default=Path("data/audit"), type=Path)
    parser.add_argument("--write-report", default=Path("docs/resource-audit.md"), type=Path)
    parser.add_argument("--check-git", action="store_true")
    parser.add_argument("--github-api", action="store_true")
    parser.add_argument("--allow-unauthenticated-api", action="store_true")
    parser.add_argument("--max-age-days", default=7, type=int)
    parser.add_argument("--stale-years", default=3, type=int)
    parser.add_argument("--workers", default=24, type=int)
    parser.add_argument("--timeout", default=20, type=int)
    parser.add_argument(
        "--fail-on-severity",
        choices=tuple(SEVERITY_ORDER),
        help="Exit non-zero if any audit issue is at this severity or higher.",
    )
    args = parser.parse_args()

    entries = parse_entries(args.readme)
    source_targets = unique_source_targets(entries)
    github_targets = unique_github_targets(entries)

    source_cache_path = args.cache_dir / "github-remotes.json"
    api_cache_path = args.cache_dir / "github-api.json"
    source_cache = load_cache(source_cache_path)
    api_cache = load_cache(api_cache_path)

    if args.check_git:
        source_cache = refresh_source_cache(
            targets=source_targets,
            cache=source_cache,
            max_age_days=args.max_age_days,
            workers=args.workers,
            timeout=args.timeout,
        )
        write_cache(source_cache_path, source_cache)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if args.github_api:
        api_cache = refresh_api_cache(
            targets=github_targets,
            cache=api_cache,
            token=token,
            allow_unauthenticated=args.allow_unauthenticated_api,
            max_age_days=args.max_age_days,
            timeout=args.timeout,
        )
        write_cache(api_cache_path, api_cache)

    issues, suggestions = analyze_entries(entries, source_cache, api_cache, args.stale_years)
    report = render_report(
        entries=entries,
        issues=issues,
        suggestions=suggestions,
        source_cache=source_cache,
        api_cache=api_cache,
        max_age_days=args.max_age_days,
        token_available=bool(token),
    )
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(report, encoding="utf-8")

    coverage_rows = source_coverage(entries, source_cache, args.max_age_days)
    print(f"Resource entries: {len(entries)}")
    print(f"Source targets: {len(source_targets)}")
    print(f"GitHub targets: {len(github_targets)}")
    print_source_coverage(coverage_rows)
    print(f"Audit issues: {len(issues)}")
    print(f"Wrote {args.write_report}")
    if args.fail_on_severity:
        failing_count = failing_issue_count(issues, args.fail_on_severity)
        if failing_count:
            print(
                f"Failing because {failing_count} audit issues are "
                f"{args.fail_on_severity} severity or higher."
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
