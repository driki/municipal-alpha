Title: Methodology
Slug: methodology
Sortorder: 5

## Coverage

We monitor 1,800+ municipalities across 50 states. The United States has 19,500 municipalities. Our coverage is concentrated in New England, the Midwest, and the Mountain West, expanding weekly through automated onboarding.

**What we cover well today:**

- Municipal meeting documents (agendas, minutes, packets) from 1,800+ municipalities
- Check registers and accounts payable data from 200+ municipalities
- Building permits from 400+ municipalities (43,000+ structured records)
- Tower and infrastructure lease data from assessor records (3,800+ sites screened)
- FOAA/FOIA response data from 100+ jurisdictions with active records requests

**Known gaps:**

- County-level data (recorder, probate, assessor) is early stage -- we have depth in Maine and New Hampshire, limited coverage elsewhere
- Western and Southern states are underrepresented relative to New England and Midwest
- Insurance rate filings and mineral rights data are in pilot phase, not production coverage
- Real-time check register feeds exist for a minority of covered municipalities -- most are periodic via records requests

We are transparent about where our coverage is strong and where it is thin. If you need data from a specific jurisdiction, ask -- we can often onboard a new municipality in days.

## Data Freshness

The pipeline runs daily at 10 PM ET. Every covered municipality is crawled, new documents are classified, and entities are resolved against the knowledge graph.

- **Document ingestion:** Daily for web-published documents. Varies for FOAA/FOIA responses (depends on jurisdiction response times, typically 5-10 business days)
- **Signal classification:** Same-day. Documents ingested in the evening crawl are classified and available by morning
- **Entity resolution:** Same-day. New vendor names are matched against the ticker database during classification
- **Tower/infrastructure data:** Weekly census. FCC and FAA cross-referencing runs on a weekly cycle

## Source Types

| Source | Method | Typical Latency |
|---|---|---|
| Municipal agendas and minutes | Automated web scraping (CivicPlus, Granicus, BoardDocs, custom) | Same-day |
| Check registers / AP data | FOAA/FOIA records requests + web scraping where available | 5-30 days (records request) or same-day (web) |
| Building permits | Web scraping + records requests | Same-day to 30 days |
| Assessor records | Records requests + GIS portal scraping | 5-30 days |
| FCC/FAA tower data | Federal database cross-reference | Weekly |
| Insurance rate filings | State DOI portal scraping | Same-day (pilot) |

## Classification

Documents are classified by an LLM-based classifier into document types (agenda, minutes, check_register, permit, ordinance, etc.) and assigned a financial priority score (HIGH, MEDIUM, LOW, NONE). The classifier is validated against a golden set of manually labeled documents and retrained weekly.

**What "HIGH priority" means:** The document contains information that maps directly to a public company ticker, infrastructure asset, or fiscal health indicator. Examples: a check register payment to a Grainger subsidiary, a tower lease renewal on a planning board agenda, a budget amendment showing a revenue shortfall.

**What the classifier does not do:** It does not make investment recommendations, predict price movements, or assign sentiment. It structures facts from public documents and resolves entities. The signal is the structured data itself.

## Entity Resolution

Vendor names in municipal documents are messy. "Waste Management of Maine," "WM," "Waste Mgmt," and "WASTE MANAGEMENT INC" are the same company (ticker: WM). Our entity resolution system maps these variations to canonical company names and public tickers.

Current resolution covers 100+ public company tickers across 1,800+ municipalities. Resolution accuracy varies by entity -- large, frequently-appearing companies (AT&T, Verizon, Waste Management) resolve at high accuracy. Smaller or regional companies may not resolve on first appearance and are queued for manual review.

## Methodology for Data Stories

Each data story (PFAS, housing density, company footprint, lead pipes) is built from classified signals in the pipeline, not from desk research or news aggregation. The counts, geographic breakdowns, and entity sightings are drawn directly from the knowledge graph.

When we say "120+ PFAS events across 72 municipalities," that means 120+ documents classified as PFAS-related by the pipeline, sourced from 72 distinct municipal websites. The events are verifiable -- every signal traces back to a specific document URL on a specific municipality's website.

## What We Don't Do

- We don't scrape paywalled or subscription-only data sources
- We don't use social media, news, or web traffic data
- We don't make investment recommendations or predictions
- We don't sell data that isn't derived from public records
- We don't access non-public government systems -- everything we structure is published by governments for public consumption or obtained through formal records requests

## Questions About Our Data

If you want to understand our coverage for a specific jurisdiction, entity, or data type, reach out. We'll tell you exactly what we have and what we don't.

**Email:** [matt@municipalalpha.com](mailto:matt@municipalalpha.com)
