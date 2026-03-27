import json
from pathlib import Path

# Load metrics from data file (auto-updated weekly by VPS)
_metrics_file = Path(__file__).parent / "data" / "metrics.json"
if _metrics_file.exists():
    with open(_metrics_file) as f:
        METRICS = json.load(f)
else:
    METRICS = {
        "municipalities": "1,800+",
        "states": "50",
        "documents": "292,000+",
        "signals": "53,000+",
        "tower_sites": "3,800+",
        "permits": "43,000+",
        "tickers": "100+",
        "updated": "2026-03-20",
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
STATIC_PATHS = ["images", "extra/CNAME", "extra/sample-data", "extra/llms.txt"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/llms.txt": {"path": "llms.txt"},
    "extra/sample-data/tower-prospects-sample.csv": {"path": "sample-data/tower-prospects-sample.csv"},
    "extra/sample-data/signals-sample.csv": {"path": "sample-data/signals-sample.csv"},
    "extra/sample-data/credit-sample.csv": {"path": "sample-data/credit-sample.csv"},
    "extra/sample-data/contractor-signals-sample.csv": {"path": "sample-data/contractor-signals-sample.csv"},
    "extra/sample-data/infrastructure-risk-sample.csv": {"path": "sample-data/infrastructure-risk-sample.csv"},
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
