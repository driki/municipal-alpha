# Content Redaction Rules for municipalalpha.com

These rules apply to all town profiles, data stories, and use cases published on the website. The goal: demonstrate capability and build credibility without giving away benchmarkable specifics that help competitors or reveal operational timeline.

## 1. No exact monitoring start dates

- Never write "Monitoring since: February 2026" or "Since March 2026."
- Use "Monitoring: Active, continuous" in summary tables.
- Remove specific backfill dates. Use "Week 1 (backfill)" not "Feb 24 (backfill)."
- The subtitle can say "updates weekly" but not when monitoring began.

## 2. Round counts to bands

- Use "200+" not "202." Use "1,900+" not "1,985." Use "6,100+" not "6,183."
- For counts under 100, round to nearest 10: "90+" not "98."
- For summary metrics: "680+" not "689." "1,300+" not "1,338."
- Exception: round numbers like "50 tickers" or "18 boards" are fine exact.

## 3. FOAA/records request: outcome, not mechanism

- Describe what the data enables, not how the system learns.
- OK: "The system improves its acquisition success rate over time."
- NOT OK: "Every interaction gets scored. Successful patterns propagate to similar towns."
- Never mention: reward tracking, confidence decay, archetype matching, cooling periods, email templates, scoring interactions.

## 4. Cap tables, show sample counts

- Town profiles: show top 5 entities, note "Showing 5 of 20+ resolved entities."
- Data stories: show top 10 companies, note "Showing 10 of 100+ resolved tickers."
- Board tables: note "Showing 5 of 18 monitored boards."
- Never publish complete lists of anything.

## 5. No tower owner names in profiles

- Don't name American Tower, SBA, Crown Castle, etc. in town profiles.
- Use "national tower operators" or "5 distinct operators."
- Show structure count and height range, not owner breakdown.
- Tower owner data is the product -- don't give it away.

## 6. Relative timelines in trend tables

- Use "8-10 quarters ago" or "Current quarter" not "2023-Q3" or "2026-Q1."
- Weekly tables use "Week 1, Week 2..." not calendar dates.
- This prevents competitors from determining dataset age and growth rate.

## 7. No specific investment recommendations

- Never include "recommended_action: BUY" or similar from signal data.
- Describe which companies are *present* in municipal data, not what to do about it.
- The line is: "these companies appear in municipal spending data" (OK) vs. "buy these tickers" (not OK).

## General principles

- The content should make a reader think "I need to talk to these people" not "I have enough to build this myself."
- Name real towns -- credibility requires specifics. But round the numbers.
- The data stories should reveal the *existence* of patterns, not the full dataset.
- Every page ends with a CTA to /contact/.
- Every table is explicitly labeled as a sample or subset.

---

## Town Digest Red Team Checklist

Run against every auto-generated town digest before publishing. Protects the competitive moat while maximizing the public value of the content.

### Never include in town digests:

- **Ticker symbols or company-to-ticker mappings.** The digest says "Waste Management contract renewal" not "Waste Management (WM)." Entity resolution is the product, not the content.
- **Entity sighting counts or resolution methodology.** Never say "we've identified 45 public companies in Falmouth's records."
- **Signal classification labels or scores.** No "HIGH priority signal" language. The digest just reports what happened.
- **Pipeline architecture details.** Never reference navigators, classifiers, crawl schedules, or automation. The digest should read as if a human journalist wrote it.
- **FOAA/FOIA request strategy.** If the source is a FOAA response, say "according to records obtained by Municipal Alpha" without describing the process.
- **Coverage gaps or expansion plans.** Don't say "we're adding police logs next month."
- **Specific scraping targets or CMS platform names.** Never say "scraped from CivicPlus."
- **Cross-town pattern analysis.** The digest is about one town, one week. Cross-municipal patterns belong in Data Stories.
- **Reward tracker scores, strategy weights, or pipeline telemetry.**

### Always include in town digests:

- **Source document links where available.** Link to the agenda, meeting packet, or official document on the town's own website.
- **Attribution for non-web-published data.** Records from FOAA: "according to records obtained by Municipal Alpha." Do not describe the request process.
- **Board/committee names and meeting dates.** Public information, makes the digest searchable and credible.
- **Factual, neutral tone.** AP/C-SPAN style. No editorializing, predictions, or advocacy.
- **Institutional data CTA in footer only.** One line, not woven into the narrative.
- **"Coming Up" section** with next week's meetings and deadlines.
- **Summary stats line** at the bottom (boards met, documents published, calls, permits).

### Gray areas (use judgment):

- **Vendor names in meeting context:** OK to report "Waste Management contract renewal" because it's in the public agenda. Not OK to add "which also appears in 28 other towns."
- **Dollar amounts from public documents:** OK. Budget figures, contract amounts, sale prices are the details that make the digest useful.
- **Personnel names:** OK for public officials (town manager, superintendent, chief, council members). Omit names of crime suspects unless charges are filed. Omit names of residents at public hearings unless they're in an official capacity.
- **Property addresses:** OK for permits, real estate transfers, commercial development. For police/fire calls at private residences, use street name only unless the incident is significant (structure fire, major accident).
