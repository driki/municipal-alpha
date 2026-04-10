Title: Municipal Alt Data
Slug: solutions/alt-data
Sortorder: 31
Summary: Pre-earnings municipal signals. Vendor payments and building permits resolved to 118 public company tickers from 2,300+ municipalities. Updated daily.

## You see the revenue before quarterly reports

When Grainger ships to Geneva, Illinois, it shows up in their check register weeks before it shows up in quarterly earnings. When a town council votes to authorize a $5M infrastructure bond, that's a forward-looking signal that no earnings model captures. The documents have always been public. They were just scattered across 19,500 town hall websites, and nobody was reading them all.

I built a system that reads them all, every day, across 2,300+ municipalities, and resolves vendor names to 118 public company tickers. You see the vendor payment before it becomes an earnings surprise.

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

- **2,300+ municipalities** monitored daily across 50 states
- **118 public tickers** resolved from municipal vendor names
- **320,000+ documents** ingested and classified
- **61,000+ classified signals** with investment priority scoring
- **Daily pipeline** with same-day classification and entity resolution
- **Golden-set validated** classifier, retrained weekly

See our [full methodology](/methodology/) for coverage details, known gaps, and data freshness.

## The Scale of What's Unread

US municipalities spend $3.9 trillion annually (Census of Governments). Almost none of that spending data is structured or available to financial markets. The big data vendors cover federal contracts and large-city budgets. I cover the 19,500 small and mid-sized municipalities where the same vendor payments happen, just on worse websites.

At current coverage of 2,300+ municipalities, I've resolved 118 public company tickers from municipal vendor names. At national scale, that grows to 500+ tickers across every sector that touches local government. Building permits alone total roughly 1.5 million per year nationally (Census Bureau), each one a precursor to contractor revenue 3-6 months before earnings.

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

Pilot programs scoped to your ticker universe, with custom coverage and historical backfill available.

**[Book a 15-minute data review](https://calendar.app.google/s6wDVSaJuqCkwcmg9)** -- tell me which tickers or sectors you're watching and I'll show you what I can see before it hits your current sources.

Or email [matt@municipalalpha.com](mailto:matt@municipalalpha.com?subject=Alt%20data%20inquiry%20%28via%20landing%20page%29) -- I'll send a coverage report within one business day.
