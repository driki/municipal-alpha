#!/usr/bin/env python3
"""
Collect page-level analytics from GoatCounter and score content for
the citizen engagement feedback loop.

Reads GoatCounter stats via API, groups by town and content type,
identifies high-engagement topics, and writes a priority file that
the content generation pipeline reads to decide what to produce next.

Usage:
    python tools/collect_analytics.py                # last 7 days
    python tools/collect_analytics.py --days 30      # last 30 days
    python tools/collect_analytics.py --output json   # machine-readable output

Requires:
    GOATCOUNTER_API_TOKEN env var (create at stats.municipalalpha.com)
    or --token flag

Output:
    data/content-priorities.json  -- ranked list of towns and topics
    stdout                        -- human-readable summary
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode


GOATCOUNTER_HOST = "stats.municipalalpha.com"
OUTPUT_FILE = Path(__file__).parent.parent / "data" / "content-priorities.json"


def fetch_stats(token, days):
    """Fetch page-level stats from GoatCounter API."""
    start = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    end = datetime.utcnow().strftime("%Y-%m-%d")

    params = urlencode({
        "start": start,
        "end": end,
        "limit": 500,
    })

    url = f"https://{GOATCOUNTER_HOST}/api/v0/stats/total?{params}"
    req = Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")

    try:
        with urlopen(req) as resp:
            return json.loads(resp.read())
    except URLError as e:
        print(f"Error fetching GoatCounter stats: {e}", file=sys.stderr)
        return []


def classify_page(path):
    """Classify a URL path into content type, town, and topic."""

    # Town weekly digest: /towns/falmouth-me/2026-03-21/
    m = re.match(r"^/towns/([a-z-]+)/(\d{4}-\d{2}-\d{2})/?$", path)
    if m:
        return {
            "type": "town_digest",
            "town": m.group(1),
            "week": m.group(2),
        }

    # Town hub: /towns/falmouth-me/
    m = re.match(r"^/towns/([a-z-]+)/?$", path)
    if m:
        return {
            "type": "town_hub",
            "town": m.group(1),
        }

    # Data story: /research/pfas-contagion/
    m = re.match(r"^/research/([a-z0-9-]+)/?$", path)
    if m:
        return {
            "type": "data_story",
            "topic": m.group(1),
        }

    # Town profile: /profiles/falmouth-me/
    m = re.match(r"^/profiles/([a-z-]+)/?$", path)
    if m:
        return {
            "type": "town_profile",
            "town": m.group(1),
        }

    # Landing page: /solutions/tower-leads/
    m = re.match(r"^/solutions/([a-z-]+)/?$", path)
    if m:
        return {
            "type": "landing_page",
            "product": m.group(1),
        }

    # Core pages
    if path in ("/", "/data-stories/", "/how-it-works/", "/about/",
                 "/methodology/", "/contact/"):
        return {
            "type": "core_page",
            "page": path.strip("/") or "home",
        }

    return None


def score_content(stats):
    """
    Group stats by content type and town, produce engagement scores.

    Returns a dict with:
    - town_scores: {town_slug: {views, digests_viewed, score}}
    - topic_scores: {topic_slug: {views, score}}
    - page_type_breakdown: {type: total_views}
    - top_pages: [(path, views)]
    """
    town_views = defaultdict(int)
    town_digests = defaultdict(set)
    topic_views = defaultdict(int)
    type_views = defaultdict(int)
    page_list = []

    for entry in stats:
        path = entry.get("path", entry.get("name", ""))
        views = entry.get("count", entry.get("total", 0))
        if not path or not views:
            continue

        page_list.append((path, views))
        info = classify_page(path)
        if not info:
            type_views["other"] += views
            continue

        type_views[info["type"]] += views

        if info["type"] in ("town_digest", "town_hub", "town_profile"):
            town = info.get("town", "")
            town_views[town] += views
            if info["type"] == "town_digest":
                town_digests[town].add(info.get("week", ""))

        if info["type"] == "data_story":
            topic_views[info.get("topic", "")] += views

    # Score towns: views + diversity bonus (more weeks viewed = stickier)
    town_scores = {}
    for town, views in town_views.items():
        digest_count = len(town_digests[town])
        # Score: raw views + 20% bonus per unique week viewed (retention signal)
        score = views * (1 + 0.2 * digest_count)
        town_scores[town] = {
            "views": views,
            "digests_viewed": digest_count,
            "score": round(score, 1),
        }

    # Score topics by views
    topic_scores = {
        topic: {"views": views, "score": views}
        for topic, views in topic_views.items()
    }

    # Sort everything by score
    town_scores = dict(sorted(town_scores.items(),
                               key=lambda x: x[1]["score"], reverse=True))
    topic_scores = dict(sorted(topic_scores.items(),
                                key=lambda x: x[1]["score"], reverse=True))
    page_list.sort(key=lambda x: x[1], reverse=True)

    return {
        "town_scores": town_scores,
        "topic_scores": topic_scores,
        "page_type_breakdown": dict(type_views),
        "top_pages": page_list[:20],
    }


def generate_priorities(scores):
    """
    Turn engagement scores into content generation priorities.

    Output format consumed by the content generation pipeline.
    """
    priorities = {
        "generated": datetime.utcnow().isoformat() + "Z",
        "towns": [],
        "topics": [],
        "recommendations": [],
    }

    # Rank towns by engagement score
    for town, data in scores["town_scores"].items():
        priority = "high" if data["score"] > 50 else "medium" if data["score"] > 10 else "low"
        priorities["towns"].append({
            "slug": town,
            "priority": priority,
            "views": data["views"],
            "retention": data["digests_viewed"],
            "score": data["score"],
        })

    # Rank topics
    for topic, data in scores["topic_scores"].items():
        priorities["topics"].append({
            "slug": topic,
            "views": data["views"],
            "score": data["score"],
        })

    # Generate recommendations
    type_breakdown = scores.get("page_type_breakdown", {})
    town_digest_views = type_breakdown.get("town_digest", 0)
    data_story_views = type_breakdown.get("data_story", 0)
    landing_views = type_breakdown.get("landing_page", 0)

    if town_digest_views > data_story_views:
        priorities["recommendations"].append(
            "Town digests are outperforming data stories. Consider increasing digest frequency for top towns."
        )
    if landing_views > 0 and landing_views < town_digest_views * 0.05:
        priorities["recommendations"].append(
            "Landing pages are getting very low traffic relative to digests. Review CTA placement in digest footers."
        )

    # Flag towns with views but no digest content
    # (would need to cross-reference with actual content inventory)

    return priorities


def print_summary(scores, priorities):
    """Print human-readable summary to stdout."""
    print("=" * 60)
    print("CONTENT ENGAGEMENT SUMMARY")
    print("=" * 60)

    print("\n## Page Type Breakdown")
    for ptype, views in sorted(scores["page_type_breakdown"].items(),
                                key=lambda x: x[1], reverse=True):
        print(f"  {ptype:20s} {views:>6d} views")

    print("\n## Town Rankings")
    for town_data in priorities["towns"]:
        print(f"  [{town_data['priority']:6s}] {town_data['slug']:20s} "
              f"{town_data['views']:>5d} views, "
              f"{town_data['retention']} weeks viewed, "
              f"score {town_data['score']}")

    print("\n## Topic Rankings")
    for topic_data in priorities["topics"]:
        print(f"  {topic_data['slug']:30s} {topic_data['views']:>5d} views")

    print("\n## Top Pages")
    for path, views in scores["top_pages"][:10]:
        print(f"  {views:>5d}  {path}")

    if priorities["recommendations"]:
        print("\n## Recommendations")
        for rec in priorities["recommendations"]:
            print(f"  - {rec}")

    print()


def main():
    parser = argparse.ArgumentParser(description="Collect analytics for content feedback loop")
    parser.add_argument("--days", type=int, default=7, help="Days of data to fetch (default: 7)")
    parser.add_argument("--token", help="GoatCounter API token (or set GOATCOUNTER_API_TOKEN env var)")
    parser.add_argument("--output", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--dry-run", action="store_true", help="Use sample data instead of live API")
    args = parser.parse_args()

    token = args.token or os.environ.get("GOATCOUNTER_API_TOKEN", "")

    if args.dry_run:
        # Sample data for testing the scoring pipeline
        stats = [
            {"path": "/", "count": 120},
            {"path": "/towns/falmouth-me/", "count": 45},
            {"path": "/towns/falmouth-me/2026-03-21/", "count": 38},
            {"path": "/towns/falmouth-me/2026-03-14/", "count": 22},
            {"path": "/towns/falmouth-me/2026-03-07/", "count": 15},
            {"path": "/towns/geneva-il/", "count": 32},
            {"path": "/towns/geneva-il/2026-03-21/", "count": 28},
            {"path": "/towns/geneva-il/2026-03-14/", "count": 18},
            {"path": "/towns/pocatello-id/", "count": 20},
            {"path": "/towns/pocatello-id/2026-03-21/", "count": 25},
            {"path": "/towns/pocatello-id/2026-03-14/", "count": 12},
            {"path": "/research/pfas-contagion/", "count": 85},
            {"path": "/research/company-footprint/", "count": 62},
            {"path": "/research/housing-density-wave/", "count": 41},
            {"path": "/research/lead-pipes/", "count": 33},
            {"path": "/research/pickleball-wave/", "count": 55},
            {"path": "/data-stories/", "count": 48},
            {"path": "/how-it-works/", "count": 35},
            {"path": "/about/", "count": 28},
            {"path": "/methodology/", "count": 18},
            {"path": "/contact/", "count": 22},
            {"path": "/solutions/alt-data/", "count": 15},
            {"path": "/solutions/tower-leads/", "count": 12},
            {"path": "/profiles/falmouth-me/", "count": 19},
            {"path": "/profiles/geneva-il/", "count": 14},
            {"path": "/profiles/pocatello-id/", "count": 11},
        ]
    elif not token:
        print("Error: No GoatCounter API token. Set GOATCOUNTER_API_TOKEN or use --token.",
              file=sys.stderr)
        print("Use --dry-run to test with sample data.", file=sys.stderr)
        sys.exit(1)
    else:
        stats = fetch_stats(token, args.days)

    scores = score_content(stats)
    priorities = generate_priorities(scores)

    # Write priorities file
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(priorities, f, indent=2)

    if args.output == "json":
        print(json.dumps(priorities, indent=2))
    else:
        print_summary(scores, priorities)
        print(f"Priorities written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
