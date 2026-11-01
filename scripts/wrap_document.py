#!/usr/bin/env python3
"""Wrap an HTML fragment as a complete standalone document.

Some artifact hosts accept a fragment and add the document skeleton themselves;
others require a complete document. This converts the former to the latter by
splitting at the end of the last <style> block: everything up to and including
it becomes the head, everything after becomes the body.

Idempotent: a file that already starts with <!DOCTYPE html> is left alone.

Usage:
    python3 scripts/wrap_document.py page.html            # in place
    python3 scripts/wrap_document.py page.html out.html   # to a new file
"""

from __future__ import annotations

import sys

SKELETON = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{head}
</head>
<body>
{body}
</body>
</html>
"""


def wrap(html: str) -> str:
    if html.lstrip().startswith("<!DOCTYPE"):
        return html
    marker = "</style>"
    if marker not in html:
        raise SystemExit("no </style> found; cannot tell head from body")
    cut = html.rindex(marker) + len(marker)
    return SKELETON.format(head=html[:cut].strip(), body=html[cut:].strip())


def main() -> int:
    if not 2 <= len(sys.argv) <= 3:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) == 3 else src

    with open(src, encoding="utf-8") as fh:
        original = fh.read()

    result = wrap(original)
    if result is original:
        print(f"{src}: already a complete document, unchanged")
        return 0

    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(result)
    print(f"{dst}: wrapped, {len(result):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
