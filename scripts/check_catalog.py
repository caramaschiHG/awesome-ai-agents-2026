#!/usr/bin/env python3
"""Validate structural and basic data-integrity rules for the README catalog."""

from __future__ import annotations

import html
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXTERNAL_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


def split_table_row(line: str) -> list[str]:
    """Split a Markdown table row, respecting escaped pipes and inline code."""
    text = line.strip()
    if not text.startswith("|"):
        return []

    cells: list[str] = []
    current: list[str] = []
    code_ticks = 0
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            current.extend((char, text[index + 1]))
            index += 2
            continue
        if char == "`":
            end = index + 1
            while end < len(text) and text[end] == "`":
                end += 1
            tick_count = end - index
            if code_ticks == 0:
                code_ticks = tick_count
            elif code_ticks == tick_count:
                code_ticks = 0
            current.extend(text[index:end])
            index = end
            continue
        if char == "|" and code_ticks == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1

    cells.append("".join(current).strip())
    if text.startswith("|") and cells and cells[0] == "":
        cells.pop(0)
    if text.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def is_delimiter_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def read_tables(lines: list[str]) -> tuple[list[tuple[int, list[str]]], list[str]]:
    """Return table data rows and any row-width errors, with 1-based line numbers."""
    rows: list[tuple[int, list[str]]] = []
    errors: list[str] = []
    index = 0
    while index < len(lines) - 1:
        header = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        if not header or not is_delimiter_row(separator):
            index += 1
            continue

        expected = len(header)
        index += 2
        while index < len(lines):
            cells = split_table_row(lines[index])
            if not cells:
                break
            rows.append((index + 1, cells))
            if len(cells) != expected:
                errors.append(
                    f"Line {index + 1}: table row has {len(cells)} cells; expected {expected}."
                )
            index += 1
    return rows, errors


def heading_slug(title: str) -> str:
    """Approximate GitHub's heading slug rules for this plain-text README."""
    title = re.sub(r"`([^`]*)`", r"\1", html.unescape(title)).lower()
    kept: list[str] = []
    for char in title:
        if char.isalnum() or char in "-_" or char.isspace():
            kept.append(char)
    # GitHub replaces each whitespace character with a hyphen (no collapsing),
    # so "Lightweight / Minimalist" slugs to "lightweight--minimalist".
    return re.sub(r"\s", "-", "".join(kept))


def heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    used: defaultdict[str, int] = defaultdict(int)
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = heading_slug(match.group(1).rstrip("# "))
        occurrence = used[base]
        used[base] += 1
        anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return anchors


def broken_anchors(text: str) -> list[str]:
    anchors = heading_anchors(text)
    errors: list[str] = []
    patterns = (
        re.compile(r"\]\(#([^)]+)\)"),
        re.compile(r"href=[\"']#([^\"']+)[\"']"),
    )
    for pattern in patterns:
        for match in pattern.finditer(text):
            fragment = unquote(match.group(1))
            if fragment not in anchors:
                line_number = text.count("\n", 0, match.start()) + 1
                errors.append(f"Line {line_number}: unresolved in-file anchor '#{fragment}'.")
    return errors


def local_link_errors(text: str, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    targets = [match.group(1).strip().split()[0].strip("<>") for match in MARKDOWN_LINK_RE.finditer(text)]
    targets.extend(match.group(1).strip() for match in re.finditer(r"(?:href|src)=[\"']([^\"']+)[\"']", text))
    root = root.resolve()
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path or target.startswith("//"):
            continue
        path = unquote(parsed.path)
        if path.startswith("/"):
            continue
        resolved = (ROOT / path).resolve()
        if not resolved.is_relative_to(root):
            errors.append(f"Local link escapes repository: {target}")
        elif not resolved.exists():
            errors.append(f"Local link target does not exist: {target}")
    return errors


def normalize_url(url: str) -> str:
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/") or "/"
    return f"{parsed.scheme.lower()}://{parsed.netloc.lower()}{path}?{parsed.query}".rstrip("?")


def resources_from_readme(text: str, rows: list[tuple[int, list[str]]]) -> list[tuple[int, str, str]]:
    resources: list[tuple[int, str, str]] = []
    for line_number, cells in rows:
        if not cells:
            continue
        match = EXTERNAL_LINK_RE.search(cells[0])
        if match:
            resources.append((line_number, match.group(1).strip(), match.group(2)))

    # Non-table catalog items are written as top-level linked bullets. Ignore the TOC
    # and linked citations embedded in prose (which do not start with a link).
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if line_number <= 50 or not stripped.startswith("- ["):
            continue
        match = EXTERNAL_LINK_RE.search(stripped)
        if match:
            resources.append((line_number, match.group(1).strip(), match.group(2)))
    return resources


def validate_catalog(root: Path = ROOT) -> tuple[list[str], int]:
    readme_path = root / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    rows, table_errors = read_tables(lines)
    errors.extend(table_errors)
    errors.extend(broken_anchors(text))

    # Resolve relative Markdown links and HTML image/link paths from the repository root.
    errors.extend(local_link_errors(text, root))
    resources = resources_from_readme(text, rows)

    seen: dict[tuple[str, str], int] = {}
    for line_number, label, url in resources:
        key = (label.casefold(), normalize_url(url))
        if key in seen:
            errors.append(
                f"Line {line_number}: duplicate catalog entry '{label}' (first listed on line {seen[key]})."
            )
        else:
            seen[key] = line_number

    count = len(seen)
    if count < 300:
        errors.append(f"Catalog has {count} unique linked resources; the README claims 300+. ")
    if not re.search(r"\b300\+", text):
        errors.append("README should state the verified 300+ resource threshold.")
    if re.search(r"(?<!\d)340\+", text):
        errors.append("README still contains the unverified 340+ resource claim.")
    return errors, count


def main() -> int:
    errors, count = validate_catalog()
    if errors:
        print("Catalog integrity check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Catalog integrity check passed: {count} unique linked resources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
