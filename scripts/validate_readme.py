#!/usr/bin/env python3
"""Validate README structure, links, tags, and duplicate cross-listings."""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import difflib
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


EXEMPT_ENTRY_SECTIONS = {"Contents", "Related Topics To Watch"}
TOC_EXEMPT_HEADINGS = {"Scope", "Contents", "Legend", "License"}
GITHUB_HOSTS = {"github.com", "www.github.com"}

# Keep this list tiny and limited to redirects confirmed during README curation.
KNOWN_GITHUB_REPO_ALIASES = {
    ("webodm", "webodm"): ("opendronemap", "webodm"),
}
KNOWN_GITHUB_REPO_DISPLAYS = {
    ("opendronemap", "webodm"): ("OpenDroneMap", "WebODM"),
}


@dataclass(frozen=True)
class Entry:
    line_no: int
    section: str
    name: str
    url: str
    description: str
    tags: tuple[str, ...]


def slugify(text: str) -> str:
    """Approximate GitHub's generated heading anchors for this README."""
    text = text.strip().lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.replace("&", "")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def load_tags(path: Path) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        raise ValueError(f"{path} must contain a non-empty JSON object")
    return set(data)


def collect_anchors(markdown: str) -> set[str]:
    counts: Counter[str] = Counter()
    anchors: set[str] = set()
    for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*#*$", markdown, re.MULTILINE):
        base = slugify(match.group(2))
        count = counts[base]
        counts[base] += 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def collect_markdown_links(markdown: str) -> list[str]:
    return [
        match.group(1)
        for match in re.finditer(
            r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", markdown
        )
    ]


def collect_entries(markdown: str) -> tuple[list[Entry], list[str]]:
    entries: list[Entry] = []
    errors: list[str] = []
    section = ""

    entry_pattern = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)\s+-\s+(.+)$")

    for line_no, line in enumerate(markdown.splitlines(), start=1):
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)
            continue

        if not line.startswith("- [") or section in EXEMPT_ENTRY_SECTIONS:
            continue

        match = entry_pattern.match(line)
        if not match:
            errors.append(
                f"line {line_no}: resource entries must use '- [Name](URL) - Description. `Tag`'"
            )
            continue

        name, url, description = match.groups()
        tags = tuple(re.findall(r"`([^`]+)`", description))
        plain_description = re.sub(r"\s*`[^`]+`", "", description).strip()

        if not tags:
            errors.append(f"line {line_no}: resource entry has no metadata tags")
        if plain_description and not plain_description.endswith((".", ")")):
            errors.append(f"line {line_no}: description should end with a period")

        entries.append(
            Entry(
                line_no=line_no,
                section=section,
                name=name,
                url=url,
                description=description,
                tags=tags,
            )
        )

    return entries, errors


def validate_local_links(markdown: str, readme_path: Path) -> list[str]:
    anchors = collect_anchors(markdown)
    errors: list[str] = []

    for link in collect_markdown_links(markdown):
        if link.startswith("#"):
            target = urllib.parse.unquote(link[1:])
            if target not in anchors:
                errors.append(f"missing anchor: {link}")
        elif link.startswith(("http://", "https://", "mailto:")):
            continue
        else:
            path_part = link.split("#", 1)[0]
            target = (readme_path.parent / path_part).resolve()
            if path_part and not target.exists():
                errors.append(f"missing local file: {link}")

    return errors


def validate_contents(markdown: str) -> list[str]:
    headings: list[tuple[str, str]] = []
    for match in re.finditer(r"^##\s+(.+?)\s*$", markdown, re.MULTILINE):
        title = match.group(1)
        if title not in TOC_EXEMPT_HEADINGS:
            headings.append((title, f"#{slugify(title)}"))

    contents_match = re.search(
        r"^## Contents\s*\n(?P<body>.*?)(?=^##\s+)",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    if not contents_match:
        return ["missing Contents section"]

    toc_links = re.findall(
        r"^- \[[^\]]+\]\((#[^)]+)\)",
        contents_match.group("body"),
        re.MULTILINE,
    )
    expected_links = [anchor for _title, anchor in headings]

    if toc_links == expected_links:
        return []

    diff = "\n".join(
        difflib.unified_diff(
            toc_links,
            expected_links,
            fromfile="README Contents",
            tofile="README headings",
            lineterm="",
        )
    )
    return [f"Contents section does not match level-2 headings:\n{diff}"]


def validate_tags(entries: list[Entry], allowed_tags: set[str]) -> list[str]:
    errors: list[str] = []
    for entry in entries:
        for tag in entry.tags:
            if tag not in allowed_tags:
                errors.append(
                    f"line {entry.line_no}: unknown tag `{tag}` on {entry.name}"
                )
        if "arxiv.org/" in entry.url and "Paper" not in entry.tags:
            errors.append(f"line {entry.line_no}: arXiv entries must use the `Paper` tag")
    return errors


def github_repo_parts(url: str) -> tuple[str, str] | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme.casefold() not in {"http", "https"}:
        return None
    if parsed.netloc.casefold() not in GITHUB_HOSTS:
        return None

    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) != 2:
        return None

    owner = urllib.parse.unquote(parts[0])
    repo = re.sub(
        r"\.git\Z",
        "",
        urllib.parse.unquote(parts[1]),
        flags=re.IGNORECASE,
    )
    if not owner or not repo:
        return None
    return owner, repo


def canonical_github_repo(owner: str, repo: str) -> tuple[str, str]:
    key = (owner.casefold(), repo.casefold())
    return KNOWN_GITHUB_REPO_ALIASES.get(key, key)


def canonical_url_key(url: str) -> str:
    github_parts = github_repo_parts(url)
    if github_parts:
        owner, repo = canonical_github_repo(*github_parts)
        return f"https://github.com/{owner}/{repo}"
    return url


def display_url_for_key(key: str, group: list[Entry]) -> str:
    for repo_key, display_parts in KNOWN_GITHUB_REPO_DISPLAYS.items():
        if key == f"https://github.com/{repo_key[0]}/{repo_key[1]}":
            owner, repo = display_parts
            return f"https://github.com/{owner}/{repo}"

    for entry in sorted(group, key=lambda item: item.line_no):
        github_parts = github_repo_parts(entry.url)
        if github_parts and canonical_url_key(entry.url) == key:
            owner, repo = github_parts
            return f"https://github.com/{owner}/{repo}"
    return key


def duplicate_groups(entries: list[Entry]) -> dict[str, list[Entry]]:
    by_url: defaultdict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_url[canonical_url_key(entry.url)].append(entry)
    return {url: group for url, group in by_url.items() if len(group) > 1}


def normalized_name(name: str) -> str:
    return " ".join(name.casefold().split())


def duplicate_name_groups(entries: list[Entry]) -> dict[str, list[Entry]]:
    by_name: defaultdict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_name[normalized_name(entry.name)].append(entry)

    return {
        name: group
        for name, group in by_name.items()
        if len({canonical_url_key(entry.url) for entry in group}) > 1
    }


def duplicate_url_sort_key(item: tuple[str, list[Entry]]) -> tuple[int, str]:
    key, group = item
    return -len(group), display_url_for_key(key, group)


def validate_duplicates(
    entries: list[Entry],
) -> tuple[list[str], dict[str, list[Entry]], dict[str, list[Entry]]]:
    url_groups = duplicate_groups(entries)
    name_groups = duplicate_name_groups(entries)
    errors: list[str] = []
    for key, group in sorted(url_groups.items()):
        sections = Counter(entry.section for entry in group)
        for section, count in sections.items():
            if count > 1:
                lines = ", ".join(
                    str(entry.line_no)
                    for entry in group
                    if entry.section == section
                )
                errors.append(
                    "same-section duplicate URL in "
                    f"`{section}` at lines {lines}: "
                    f"{display_url_for_key(key, group)}"
                )
    for _name, group in sorted(name_groups.items()):
        lines = ", ".join(
            str(entry.line_no)
            for entry in sorted(group, key=lambda item: item.line_no)
        )
        urls = ", ".join(
            display_url_for_key(key, group)
            for key in sorted({canonical_url_key(entry.url) for entry in group})
        )
        errors.append(
            "duplicate display name "
            f"`{group[0].name}` uses different URLs at lines {lines}: {urls}"
        )
    return errors, url_groups, name_groups


def render_duplicate_report(entries: list[Entry], readme_path: Path) -> str:
    url_groups = duplicate_groups(entries)
    name_groups = duplicate_name_groups(entries)
    total_entries = len(entries)
    unique_literal_urls = len({entry.url for entry in entries})
    unique_canonical_urls = len(
        {canonical_url_key(entry.url) for entry in entries}
    )

    lines = [
        "# Duplicate URL Report",
        "",
        f"Built from `{readme_path.as_posix()}` by `scripts/validate_readme.py`.",
        "",
        "Cross-section duplicates are allowed when one resource is genuinely useful in more than one category. Use this report during review to decide whether a repeated URL is intentional or should become a single canonical entry.",
        "",
        "GitHub repository-root URLs are normalized without network calls for scheme, host, owner/repo case, trailing slashes, and `.git` suffixes; locally confirmed repository redirects may also be grouped.",
        "",
        "## Summary",
        "",
        f"- Resource entries: {total_entries}",
        f"- Unique literal resource URLs: {unique_literal_urls}",
        f"- Unique canonical resource URLs: {unique_canonical_urls}",
        f"- Duplicate URL groups: {len(url_groups)}",
        f"- Duplicate display-name groups with different URLs: {len(name_groups)}",
        "",
        "## Duplicate URLs",
        "",
    ]

    if not url_groups:
        lines.append("No duplicate URL groups.")
        lines.append("")

    for key, group in sorted(url_groups.items(), key=duplicate_url_sort_key):
        lines.append(f"### `{display_url_for_key(key, group)}`")
        lines.append("")
        variants = sorted({entry.url for entry in group})
        if len(variants) > 1:
            lines.append(
                "Canonical-equivalent variants: "
                + ", ".join(f"`{url}`" for url in variants)
            )
            lines.append("")
        for entry in sorted(group, key=lambda item: (item.section, item.line_no)):
            lines.append(
                f"- `{entry.section}` line {entry.line_no}: {entry.name}"
            )
        lines.append("")

    lines.extend(["## Duplicate Display Names", ""])
    if not name_groups:
        lines.append("No duplicate display names with different URLs.")
        lines.append("")

    for _name, group in sorted(
        name_groups.items(),
        key=lambda item: (item[0], item[1][0].line_no),
    ):
        lines.append(f"### `{group[0].name}`")
        lines.append("")
        for entry in sorted(group, key=lambda item: (item.section, item.line_no)):
            lines.append(
                f"- `{entry.section}` line {entry.line_no}: {entry.url}"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def check_duplicate_report(report_path: Path, expected: str) -> list[str]:
    if not report_path.exists():
        return [f"duplicate report is missing: {report_path}"]
    actual = report_path.read_text(encoding="utf-8")
    if actual == expected:
        return []
    diff = "\n".join(
        difflib.unified_diff(
            actual.splitlines(),
            expected.splitlines(),
            fromfile=str(report_path),
            tofile=f"{report_path} (expected)",
            lineterm="",
        )
    )
    return [f"duplicate report is out of date:\n{diff}"]


def external_urls(markdown: str) -> list[str]:
    return sorted(
        {
            link
            for link in collect_markdown_links(markdown)
            if link.startswith(("http://", "https://"))
        }
    )


def open_url(url: str, timeout: int, method: str) -> tuple[int | None, str | None]:
    headers = {
        "User-Agent": "Mozilla/5.0 awesome-defense link-check",
        "Accept": "text/html,application/xhtml+xml,application/xml,application/pdf;q=0.9,*/*;q=0.8",
    }
    request = urllib.request.Request(url, headers=headers, method=method)
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            status = getattr(response, "status", None) or response.getcode()
            if method != "HEAD":
                response.read(1)
            if 200 <= status < 400:
                return status, None
            return status, f"HTTP {status}"
    except urllib.error.HTTPError as exc:
        return exc.code, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report any URL failure compactly.
        return None, f"{type(exc).__name__}: {str(exc)[:160]}"


def check_one_url(url: str, timeout: int) -> tuple[str, int | None, str | None]:
    status, error = open_url(url, timeout, "GET")
    if error and status in {403, 405, 429, 500, 502, 503, 504}:
        head_status, head_error = open_url(url, timeout, "HEAD")
        if not head_error:
            return url, head_status, None
    return url, status, error


def validate_external_links(markdown: str, workers: int, timeout: int) -> list[str]:
    urls = external_urls(markdown)
    failures: list[str] = []
    start = time.time()

    print(f"Checking {len(urls)} unique external URLs...")
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        checks = [executor.submit(check_one_url, url, timeout) for url in urls]
        for index, check in enumerate(futures.as_completed(checks), start=1):
            url, _status, error = check.result()
            if error:
                failures.append(f"{error}: {url}")
            if index % 100 == 0 or index == len(checks):
                print(f"Checked {index}/{len(checks)}")

    print(f"External link check finished in {time.time() - start:.1f}s")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", nargs="?", default="README.md", type=Path)
    parser.add_argument("--tags", default=Path("data/tags.json"), type=Path)
    parser.add_argument("--check-external", action="store_true")
    parser.add_argument("--workers", default=24, type=int)
    parser.add_argument("--timeout", default=25, type=int)
    parser.add_argument("--write-duplicate-report", type=Path)
    parser.add_argument("--check-duplicate-report", type=Path)
    args = parser.parse_args()

    readme_path = args.readme
    markdown = readme_path.read_text(encoding="utf-8")
    allowed_tags = load_tags(args.tags)

    entries, entry_errors = collect_entries(markdown)
    errors = []
    errors.extend(validate_local_links(markdown, readme_path))
    errors.extend(validate_contents(markdown))
    errors.extend(entry_errors)
    errors.extend(validate_tags(entries, allowed_tags))
    duplicate_errors, url_groups, name_groups = validate_duplicates(entries)
    errors.extend(duplicate_errors)

    report = render_duplicate_report(entries, readme_path)
    if args.write_duplicate_report:
        args.write_duplicate_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_duplicate_report.write_text(report, encoding="utf-8")
    if args.check_duplicate_report:
        errors.extend(check_duplicate_report(args.check_duplicate_report, report))

    if args.check_external:
        errors.extend(validate_external_links(markdown, args.workers, args.timeout))

    print(f"Resource entries: {len(entries)}")
    print(f"Unique literal resource URLs: {len({entry.url for entry in entries})}")
    print(
        "Unique canonical resource URLs: "
        f"{len({canonical_url_key(entry.url) for entry in entries})}"
    )
    print(f"Duplicate URL groups: {len(url_groups)}")
    print(f"Duplicate display-name groups with different URLs: {len(name_groups)}")

    if errors:
        print("\nValidation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("README validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
