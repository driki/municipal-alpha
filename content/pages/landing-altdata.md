Title: Municipal Alt Data
Slug: solutions/alt-data
Sortorder: 31

## Government contractor revenue from the source documents

Municipal check registers, vendor payments, and building permits are the source records that earnings eventually reflect. We structure them daily across 1,800+ municipalities and resolve vendor names to 100+ public company tickers.

When Grainger ships to Geneva, Illinois, it shows up in their check register weeks before it shows up in quarterly revenue. We read the check register. Every day. For every town in the pipeline.

## What the Data Looks Like

| Field | Example |
|---|---|
| Municipality | Geneva, IL |
| Document type | check_register |
| Vendor (raw) | W W GRAINGER INC |
| Vendor (resolved) | Grainger |
| Ticker | GRI |
| Amount | $4,287.50 |
| Date | 2026-02-14 |
| Category | MRO / Industrial supply |
| Signal priority | HIGH |

Multiply this by 1,800+ municipalities and 100+ resolved tickers. That's the dataset.

## Signal Types

**Check registers and AP data** -- Direct vendor payments from municipal governments. The clearest revenue signal: if a town is paying a company, that's revenue. Entity-resolved to public tickers with payment amounts, dates, and categories.

**Building permits** -- 43,000+ structured permit records showing which contractors are winning work, where construction is accelerating, and how local activity maps to public company revenue. Permits lead earnings by 3-6 months.

**Budget and appropriation signals** -- Municipal budget approvals, amendments, and spending authorizations that predict future vendor payments. A budget line item for "water infrastructure" in March becomes a contract award in June becomes a check register payment in September.

**Contagion signals** -- Policy patterns (PFAS remediation, housing density changes, lead pipe replacement) spreading across municipalities. When Maine mandates ADU zoning and 80 towns respond, the building material suppliers who serve those towns see revenue impact. We track the pattern across jurisdictions.

## Coverage and Methodology

- **1,800+ municipalities** monitored daily across 50 states
- **100+ public tickers** resolved from municipal vendor names
- **292,000+ documents** ingested and classified
- **Daily pipeline** with same-day classification and entity resolution
- **Golden-set validated** classifier, retrained weekly

See our [full methodology](/methodology/) for coverage details, known gaps, and data freshness.

## Who This Is For

- **Quantitative hedge funds** looking for non-consensus revenue signals from public records
- **Fundamental analysts** seeking primary-source data on government contractor exposure
- **Alt data platforms** (Neudata, TenderAlpha, Eagle Alpha) looking for new datasets to list
- **Credit analysts** monitoring municipal fiscal health from spending patterns

## Sample Data

**[Download sample signals (CSV)](/sample-data/signals-sample.csv)** -- 50 redacted entity-resolved signals showing the data structure: municipality, document type, vendor, ticker, signal priority, and date.

## Get Started

Alt data is delivered as structured feeds (CSV, JSON, or API), updated daily. Historical backfill available for covered municipalities.

**Email:** [matt@municipalalpha.com](mailto:matt@municipalalpha.com) -- tell us which tickers or sectors you're watching and we'll send a coverage report.
