import json
from pathlib import Path

# Load metrics from data file (auto-updated weekly by VPS)
_metrics_file = Path(__file__).parent / "data" / "metrics.json"
if _metrics_file.exists():
    with open(_metrics_file) as f:
        METRICS = json.load(f)
else:
    METRICS = {
        "municipalities": "2,100+",
        "states": "50",
        "documents": "309,000+",
        "signals": "57,000+",
        "tower_sites": "4,700+",
        "permits": "43,000+",
        "tickers": "100+",
        "updated": "2026-03-29",
    }

AUTHOR = "Municipal Alpha"
SITENAME = "Municipal Alpha"
SITEURL = ""
SITESUBTITLE = "A Knowledge Graph of US Public Records"

PATH = "content"
THEME = "theme/municipal-alpha"

TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# No blog feed until we have articles
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pages config
PAGE_ORDER_BY = "sortorder"
DISPLAY_PAGES_ON_MENU = True

# No blogroll or social links yet
LINKS = ()
SOCIAL = ()

DEFAULT_PAGINATION = False

# Markdown extensions -- toc adds heading IDs for anchor links
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {"permalink": False},
        "markdown.extensions.tables": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

# Static paths
STATIC_PATHS = ["images", "extra/CNAME", "extra/sample-data", "extra/case-studies", "extra/llms.txt"]
# Prevent Pelican from treating HTML in extra/ as content
READERS = {"html": None}
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/llms.txt": {"path": "llms.txt"},
    "extra/sample-data/tower-prospects-sample.csv": {"path": "sample-data/tower-prospects-sample.csv"},
    "extra/sample-data/signals-sample.csv": {"path": "sample-data/signals-sample.csv"},
    "extra/sample-data/credit-sample.csv": {"path": "sample-data/credit-sample.csv"},
    "extra/sample-data/contractor-signals-sample.csv": {"path": "sample-data/contractor-signals-sample.csv"},
    "extra/sample-data/infrastructure-risk-sample.csv": {"path": "sample-data/infrastructure-risk-sample.csv"},
    "extra/sample-data/connell-redev-sample-2026-03-27.pdf": {"path": "sample-data/connell-redev-sample-2026-03-27.pdf"},
    "extra/sample-data/simon-redev-sample-2026-03-27.pdf": {"path": "sample-data/simon-redev-sample-2026-03-27.pdf"},
    "extra/sample-data/sw-cole-infrastructure-sample-2026-03-27.pdf": {"path": "sample-data/sw-cole-infrastructure-sample-2026-03-27.pdf"},
    "extra/sample-data/desri-energy-sample-2026-03-28.pdf": {"path": "sample-data/desri-energy-sample-2026-03-28.pdf"},
    "extra/sample-data/amt-combined-alert-2026-03-28.html": {"path": "sample-data/amt-combined-alert-2026-03-28.html"},
    "extra/case-studies/amherst-nh-procurement-chain.pdf": {"path": "case-studies/amherst-nh-procurement-chain.pdf"},
    "extra/case-studies/infrastructure-equity-signals.pdf": {"path": "case-studies/infrastructure-equity-signals.pdf"},
    "extra/case-studies/muni-credit-early-warning.pdf": {"path": "case-studies/muni-credit-early-warning.pdf"},
}

# Clean URLs
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

# Landing page is custom index.html template at root
# Article listing (if any) goes to /blog/
INDEX_SAVE_AS = "index.html"
DIRECT_TEMPLATES = ["index"]
