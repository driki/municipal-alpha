#!/usr/bin/env python3
"""
Inject <meta name="robots" content="noindex"> into the unlinked standalone
pages under content/extra/ as they sit in output/.

WHY: every page under content/extra/ is an unlinked, directly-shared page
(prospect/buyer discussion pages, dispatches, decks, overviews). None of them
are in sitemap.xml and none are linked from the public site — they are sent to
specific recipients via tracked links, not meant to be found via organic search.
Without an explicit noindex they are protected only by obscurity: one forwarded
or leaked URL away from Google discovering and indexing a buyer's prospect page,
which could then surface "DESRI"/"Connell"/"Ready.net" pages in search results
(a confidentiality break — Commandment II, guard the trust).

noindex (NOT a robots.txt Disallow) is the correct control here: a Disallow
blocks crawling, which means Google never sees the noindex and can still index
the bare URL if it discovers it via a link. Allow-crawl + noindex is Google's
prescribed way to guarantee a page never appears in search.

Runs AFTER `copy-static-html` (wired into the Makefile html/publish targets), so
it regenerates on every build/deploy and never drifts. Stdlib-only — no extra
dependency in the GitHub Actions build, same behavior on macOS (local) and
ubuntu-latest (CI), unlike a cross-platform sed injection.

SCOPE: only output/<dir>/index.html files that have a corresponding
content/extra/<dir>/ source. It can never touch a public Pelican page (towns/,
solutions/, research/, profiles/, ...) because those have no content/extra
source. New buyer pages added to copy-static-html are covered automatically.

Idempotent: skips any page that already carries a name="robots" meta (respects
an explicit directive a page author may have set).

Usage:
    python3 tools/inject_noindex.py            # inject into output/, report count
    python3 tools/inject_noindex.py --check     # report what WOULD change, write nothing
"""

import re
import sys
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
EXTRA_DIR = BASEDIR / "content" / "extra"
OUTPUT_DIR = BASEDIR / "output"

NOINDEX_TAG = '<meta name="robots" content="noindex">'

# First <head ...> opening tag, case-insensitive.
HEAD_OPEN_RE = re.compile(r"<head\b[^>]*>", re.IGNORECASE)
# Any existing robots meta — if present, leave the page alone.
ROBOTS_META_RE = re.compile(r"""<meta\s+[^>]*name\s*=\s*['"]robots['"]""", re.IGNORECASE)


def extra_output_pages():
    """Yield output/*.html paths that derive from a content/extra/<dir> source.

    Mirrors how copy-static-html populates output/: each content/extra/<dir>
    contributes output/<dir>/**.html. We only ever return paths that both
    (a) have an extra source and (b) actually exist in output/ (i.e. were
    copied this build), so the set is exactly the unlinked standalone pages.
    """
    if not EXTRA_DIR.is_dir() or not OUTPUT_DIR.is_dir():
        return
    for src in sorted(EXTRA_DIR.iterdir()):
        if not src.is_dir():
            continue  # skip robots.txt, CNAME, favicons, etc.
        out_dir = OUTPUT_DIR / src.name
        if not out_dir.is_dir():
            continue  # this extra dir wasn't copied into output this build
        for html_path in sorted(out_dir.rglob("*.html")):
            yield html_path


def inject(html_path: Path, write: bool) -> str:
    """Return a status: 'injected', 'skipped-has-robots', 'skipped-no-head'."""
    text = html_path.read_text(encoding="utf-8")
    if ROBOTS_META_RE.search(text):
        return "skipped-has-robots"
    m = HEAD_OPEN_RE.search(text)
    if not m:
        return "skipped-no-head"
    new_text = text[: m.end()] + "\n" + NOINDEX_TAG + text[m.end():]
    if write:
        html_path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    counts = {"injected": 0, "skipped-has-robots": 0, "skipped-no-head": 0}
    skipped_no_head = []
    for html_path in extra_output_pages():
        status = inject(html_path, write=not check_only)
        counts[status] += 1
        if status == "skipped-no-head":
            skipped_no_head.append(html_path.relative_to(OUTPUT_DIR))

    verb = "would inject" if check_only else "injected"
    print(
        f"[noindex] {verb} into {counts['injected']} unlinked extra page(s); "
        f"{counts['skipped-has-robots']} already had a robots meta; "
        f"{counts['skipped-no-head']} had no <head>."
    )
    for p in skipped_no_head:
        print(f"[noindex]   WARNING no <head>, left unprotected: {p}")
    # Build step: never fail the build over this. A missing <head> is surfaced
    # as a WARNING above (Commandment VII — diagnostic reports status, exits 0).
    return 0


if __name__ == "__main__":
    sys.exit(main())
