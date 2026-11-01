#!/usr/bin/env python3
"""Structural sanity checks for the comparison page.

Catches the two failure modes that actually bit during authoring: unbalanced
tags after a hand edit, and a table row that gained or lost a cell when a
configuration column was added.

Usage:
    python3 scripts/validate_html.py index.html [--expect-stale STRING ...]

Exits non-zero if anything fails.
"""

from __future__ import annotations

import argparse
import re
import sys

TAGS = ("section", "article", "table", "div", "tr", "td", "th")


def check_balance(html: str) -> list[str]:
    problems = []
    for tag in TAGS:
        opened = len(re.findall(rf"<{tag}[ >]", html))
        closed = len(re.findall(rf"</{tag}>", html))
        if opened != closed:
            problems.append(f"tag <{tag}>: {opened} opened, {closed} closed")
    return problems


def check_tables(html: str) -> list[str]:
    """Each table's rows should agree on cell count.

    A colspan row legitimately has fewer cells, so a table is only flagged when
    it has more than two distinct counts, or two that differ without a colspan
    present.
    """
    problems = []
    for i, table in enumerate(re.findall(r"<table.*?</table>", html, re.S), 1):
        rows = re.findall(r"<tr.*?</tr>", table, re.S)
        counts = {len(re.findall(r"<t[dh][ >]", r)) for r in rows}
        has_colspan = "colspan" in table
        if len(counts) > 2 or (len(counts) == 2 and not has_colspan):
            problems.append(
                f"table {i}: inconsistent cell counts {sorted(counts)} "
                f"across {len(rows)} rows"
            )
    return problems


def check_document(html: str) -> list[str]:
    problems = []
    if not html.lstrip().startswith("<!DOCTYPE html>"):
        problems.append("document does not begin with <!DOCTYPE html>")
    for once in ("<title>", "<body>", "<head>"):
        if html.count(once) != 1:
            problems.append(f"expected exactly one {once}, found {html.count(once)}")
    if "prefers-color-scheme: dark" not in html:
        problems.append("no dark-mode block found")
    if not re.search(r"body\s*\{[^}]*background", html):
        problems.append("body has no explicit background (artifact will borrow host ground)")
    return problems


def check_stale(html: str, needles: list[str]) -> list[str]:
    return [f"stale string present: {n!r} ({html.count(n)}x)" for n in needles if n in html]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument(
        "--expect-stale",
        nargs="*",
        default=[],
        metavar="STRING",
        help="strings that must NOT appear, e.g. superseded prices",
    )
    args = ap.parse_args()

    with open(args.path, encoding="utf-8") as fh:
        html = fh.read()

    problems: list[str] = []
    problems += check_document(html)
    problems += check_balance(html)
    problems += check_tables(html)
    problems += check_stale(html, args.expect_stale)

    print(f"{args.path}: {len(html):,} bytes, {html.count(chr(10)) + 1:,} lines")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
