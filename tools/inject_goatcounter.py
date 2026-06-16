#!/usr/bin/env python3
"""
Inject the GoatCounter loader <script> into the unlinked standalone pages under
content/extra/ as they sit in output/.

WHY: every page under content/extra/ is a standalone HTML file copied verbatim by
`copy-static-html`, bypassing the Pelican base template (theme/.../base.html) that
carries the GoatCounter loader. So these buyer/prospect/discussion/dispatch pages
"run dark" — no pageview is recorded, and any on-page `window.goatcounter.count(...)`
depth-event JS they contain silently no-ops because `window.goatcounter` is never
defined (the guard `if (window.goatcounter && window.goatcounter.count)` fails).
We send these pages to specific recipients and want to see the hits; without the
loader we are blind to whether anyone opened them.

This is the GoatCounter sibling of inject_noindex.py and uses the identical
content/extra-derived page set, so adding the loader can never touch a public
Pelican page (towns/, solutions/, research/, ...) — those have no content/extra
source and already inherit the loader from base.html. New buyer pages added to
copy-static-html are covered automatically.

The injected snippet is byte-identical to the loader in base.html so the two
sources never drift in endpoint/behavior.

Runs AFTER `copy-static-html` (wired into the Makefile html/publish targets), so
it regenerates on every build/deploy and never drifts. Stdlib-only — same behavior
on macOS (local) and ubuntu-latest (CI).

SCOPE: only output/<dir>/**.html files that have a corresponding
content/extra/<dir>/ source.

Idempotent: skips any page that already carries the GoatCounter loader (matched by
the data-goatcounter attribute — the loader's distinguishing mark, NOT the
window.goatcounter.count() depth-event call, which is not the loader).

Usage:
    python3 tools/inject_goatcounter.py            # inject into output/, report count
    python3 tools/inject_goatcounter.py --check     # report what WOULD change, write nothing
"""

import re
import sys
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
EXTRA_DIR = BASEDIR / "content" / "extra"
OUTPUT_DIR = BASEDIR / "output"

# Byte-identical to the loader in theme/municipal-alpha/templates/base.html.
LOADER_TAG = (
    '<script data-goatcounter="https://stats.municipalalpha.com/count"\n'
    '            async src="//stats.municipalalpha.com/count.js"></script>'
)

# First <head ...> opening tag, case-insensitive.
HEAD_OPEN_RE = re.compile(r"<head\b[^>]*>", re.IGNORECASE)
# The loader's distinguishing mark — the data-goatcounter attribute. Matching this
# (not a bare "goatcounter" string) means a page that only has the
# window.goatcounter.count() depth-event call is correctly treated as loader-less.
LOADER_RE = re.compile(r"""data-goatcounter\s*=""", re.IGNORECASE)


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
    """Return a status: 'injected', 'skipped-has-loader', 'skipped-no-head'."""
    text = html_path.read_text(encoding="utf-8")
    if LOADER_RE.search(text):
        return "skipped-has-loader"
    m = HEAD_OPEN_RE.search(text)
    if not m:
        return "skipped-no-head"
    new_text = text[: m.end()] + "\n" + LOADER_TAG + text[m.end():]
    if write:
        html_path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    counts = {"injected": 0, "skipped-has-loader": 0, "skipped-no-head": 0}
    skipped_no_head = []
    for html_path in extra_output_pages():
        status = inject(html_path, write=not check_only)
        counts[status] += 1
        if status == "skipped-no-head":
            skipped_no_head.append(html_path.relative_to(OUTPUT_DIR))

    verb = "would inject" if check_only else "injected"
    print(
        f"[goatcounter] {verb} loader into {counts['injected']} unlinked extra "
        f"page(s); {counts['skipped-has-loader']} already had the loader; "
        f"{counts['skipped-no-head']} had no <head>."
    )
    for p in skipped_no_head:
        print(f"[goatcounter]   WARNING no <head>, left untracked: {p}")
    # Build step: never fail the build over this. A missing <head> is surfaced
    # as a WARNING above (Commandment VII — diagnostic reports status, exits 0).
    return 0


if __name__ == "__main__":
    sys.exit(main())
