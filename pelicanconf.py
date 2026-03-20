AUTHOR = "Municipal Alpha"
SITENAME = "Municipal Alpha"
SITEURL = ""
SITESUBTITLE = "Public Record Intelligence"

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

# Static paths
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

# Clean URLs
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

# Landing page is custom index.html template at root
# Article listing (if any) goes to /blog/
INDEX_SAVE_AS = "index.html"
DIRECT_TEMPLATES = ["index"]
