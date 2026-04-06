Title: Municipal Alt Data
Slug: solutions/alt-data
Sortorder: 31
Summary: Vendor payments and building permits resolved to 100+ public company tickers from 2,100+ municipalities. Updated daily.

## Non-consensus signals from documents that don't exist on the internet

Municipal governments publish financial records -- check registers, budgets, capital plans, legislative votes -- to CMS platforms that search engines and AI agents can't reach. We built connectors to 15+ municipal CMS platforms and read these documents daily across 2,100+ municipalities.

When Grainger ships to Geneva, Illinois, it shows up in their check register weeks before it shows up in quarterly revenue. When a town council votes to authorize a $5M infrastructure bond, that's a forward-looking signal that no earnings model captures. We read these documents every day, for every town in the pipeline, and resolve vendor names to 100+ public company tickers.

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

Multiply this by 2,100+ municipalities and 100+ resolved tickers. That's the dataset.

## Signal Types

**Check registers and AP data** -- Direct vendor payments from municipal governments. The clearest revenue signal: if a town is paying a company, that's revenue. Entity-resolved to public tickers with payment amounts, dates, and categories.

**Building permits** -- 43,000+ structured permit records showing which contractors are winning work, where construction is accelerating, and how local activity maps to public company revenue. Permits lead earnings by 3-6 months.

**Budget and appropriation signals** -- Municipal budget approvals, amendments, and spending authorizations that predict future vendor payments. A budget line item for "water infrastructure" in March becomes a contract award in June becomes a check register payment in September.

**Contagion signals** -- Policy patterns (PFAS remediation, housing density changes, lead pipe replacement) spreading across municipalities. When Maine mandates ADU zoning and 80 towns respond, the building material suppliers who serve those towns see revenue impact. We track the pattern across jurisdictions.

## Coverage and Methodology

- **2,100+ municipalities** monitored daily across 50 states
- **100+ public tickers** resolved from municipal vendor names
- **309,000+ documents** ingested and classified
- **Daily pipeline** with same-day classification and entity resolution
- **Golden-set validated** classifier, retrained weekly

See our [full methodology](/methodology/) for coverage details, known gaps, and data freshness.

## The Scale of What's Uncovered

US municipalities spend $3.9 trillion annually (Census of Governments). Almost none of that spending data is structured or available to financial markets. The big data vendors cover federal contracts and large-city budgets. We cover the 19,500 small and mid-sized municipalities where the same vendor payments happen, just on worse websites.

At our current coverage of 2,100+ municipalities, we've resolved 100+ public company tickers from municipal vendor names. At national scale, that number grows to 500+ tickers across every sector that touches local government, from construction materials to waste management to municipal IT. Building permits alone total roughly 1.5 million per year nationally (Census Bureau), each one a leading indicator of contractor revenue 3-6 months before earnings.

The pipeline adds ~25 municipalities per week. The marginal cost of each addition is near zero.

## Why You Can't Google This

Check registers and AP warrants are the most financially valuable municipal documents, and they are almost never discoverable through search engines or AI assistants. In our testing, roughly 99% of the documents we ingest exist at CMS URLs with no public navigation link. A finance director uploads a check register to the town portal, it gets stored, and nothing ever links to it. Google can't index what it can't find. AI agents browse the same pages Google does. The documents are public record, sitting on public servers, at URLs that nothing points to. We find them because we built connectors for each municipal CMS platform, not a general-purpose crawler.

## Who This Is For

- **Quantitative hedge funds** looking for non-consensus revenue signals from public records
- **Fundamental analysts** seeking primary-source data on government contractor exposure
- **Alt data platforms** (Neudata, TenderAlpha, Eagle Alpha) looking for new datasets to list
- **Credit analysts** monitoring municipal fiscal health from spending patterns

## Sample Data

**[Download sample signals (CSV)](/sample-data/signals-sample.csv)** -- 50 redacted entity-resolved signals showing the data structure: municipality, document type, vendor, ticker, signal priority, and date.

## Delivery & Integration

- **Format:** Structured feeds via CSV, JSON, or API
- **Cadence:** Daily updates, same-day classification
- **Backfill:** Full historical data for covered municipalities
- **Filtering:** By ticker, sector, geography, document type, or signal priority

## How It Differs From Federal Contract Data

Federal procurement databases (USASpending, GovWin, Shovels) cover top-down government spending. Municipal Alpha covers bottom-up: the 19,500 local governments where the same companies do work but nobody aggregates the data. Federal contracts are competed, awarded, and publicly tracked. Municipal vendor payments happen quietly in check registers that no one reads.

The two datasets are complementary, not competitive. Federal data tells you who won the big contracts. Municipal data tells you who's winning the small ones everywhere, and whether that's accelerating or slowing.

## Get Started

Pilot programs start at **$1,000/month** for a ticker universe. Custom pricing for broader coverage and historical backfill.

**[Book a 15-minute data review](https://calendar.app.google/s6wDVSaJuqCkwcmg9)** -- tell us which tickers or sectors you're watching and we'll show you coverage live.

Or email [matt@municipalalpha.com](mailto:matt@municipalalpha.com?subject=Alt%20data%20inquiry%20%28via%20landing%20page%29) -- we'll send a coverage report within one business day.
