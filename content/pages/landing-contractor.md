Title: Government Contractor Signals
Slug: solutions/contractor-signals
Sortorder: 33
Summary: Pre-earnings municipal signals. Vendor payments and building permits mapped to 118 public company tickers. Primary-source revenue signals for government contractor coverage.

## You see the revenue before quarterly reports

Analysts model municipal revenue top-down from budget allocations and macro spending trends. I read it bottom-up from the actual payment records, 2,300+ municipalities, every day.

When a municipality pays AECOM for engineering services, that transaction appears in the check register weeks before it appears in quarterly revenue. When building permits spike in a county, the contractors winning that work show up in permit data 3-6 months before earnings.

## What the Data Looks Like

| Field | Example |
|---|---|
| Municipality | Falmouth, ME |
| Document type | check_register |
| Vendor (raw) | AECOM TECHNICAL SERVICES |
| Vendor (resolved) | AECOM |
| Ticker | ACM |
| Amount | $127,500.00 |
| Date | 2026-02-28 |
| Category | Engineering / Professional services |
| Signal priority | HIGH |

## Two Signal Layers

**Check registers and AP data** -- Who's getting paid now. Direct vendor payments from municipal governments, entity-resolved to public tickers with payment amounts, dates, and categories. The clearest revenue signal: if a town is paying a company, that's revenue.

**Building permits** -- Who's about to get paid. 43,000+ structured permit records showing which contractors are winning work, where construction is accelerating, and how local activity maps to public company revenue. Permits lead earnings by 3-6 months.

The combination surfaces revenue acceleration and deceleration signals that top-down models miss.

## Tickers We Track

100+ public companies resolved from municipal vendor names, including:

- **Construction materials:** Vulcan Materials (VMC), Martin Marietta (MLM), Summit Materials (SUM)
- **Engineering:** AECOM (ACM), Tetra Tech (TTEK), Arcadis
- **Municipal IT:** Tyler Technologies (TYL), CentralSquare
- **Water/utilities:** Xylem (XYL), Mueller Water (MWA), Essential Utilities (WTRG)
- **Waste:** Waste Management (WM), Casella Waste (CWST), Clean Harbors (CLH)
- **Industrial/MRO:** Grainger (GWW), Fastenal (FAST)

## The Scale of What's Unstructured

US municipalities spend $3.9 trillion annually. That spending flows through check registers and vendor payment records that exist as public documents in 19,500 jurisdictions. The big data vendors cover federal contracts (USASpending, GovWin) and large-city procurement. Nobody aggregates the local-level vendor payments where most government contractors actually do their work.

At current coverage, we've resolved 100+ public company tickers from 2,100+ municipalities. At national scale, every company that sells to local government, from Grainger and Fastenal to AECOM and Waste Management, gets bottom-up revenue tracking from the source transaction records. Nationally, municipalities issue roughly 1.5 million building permits per year, each one a forward-looking signal on contractor revenue that earnings models don't capture.

## Why Nobody Else Has This

Vendor payment records and check registers live inside municipal CMS platforms at URLs that nothing links to. In our testing, roughly 99% of the documents we ingest have no public navigation path. You can't Google for a town's check register and find it, because the CMS stored it without ever surfacing it in a menu or sitemap. AI agents face the same problem. The documents are public, the URLs exist, but no web crawler or AI tool will ever discover them without understanding how each CMS platform stores data internally. That's what our connectors do.

## Who This Is For

- **Fundamental L/S equity analysts** covering industrials, infrastructure, or govtech
- **Quantitative funds** looking for non-consensus revenue signals from primary sources
- **Sector specialists** tracking government contractor exposure at the transaction level

## Sample Data

**[Download sample contractor signals (CSV)](/sample-data/contractor-signals-sample.csv)** -- 50 entity-resolved signals showing vendor names, tickers, document types, and context.

## Delivery & Integration

- **Format:** Structured feeds via CSV, JSON, or API
- **Cadence:** Daily updates, same-day classification and entity resolution
- **Backfill:** Full historical data for covered municipalities
- **Filtering:** By ticker, sector, geography, or document type

## What This Looks Like in Practice

An equity analyst covering Waste Management (WM) could receive a weekly signal:

> WM appeared in 14 municipal check registers this week across 8 states. Total payments: $287K. New market entry: Geneva IL (first payment, $12,400). Competitive displacement: Falmouth ME stopped paying WM, started paying Casella (CWST) in March.

That's primary-source revenue intelligence from the payment records themselves. No surveys, no credit card panels, no web scraping proxies.

For more on how this works, read our **[Infrastructure Equity Signals one-pager (PDF)](/case-studies/infrastructure-equity-signals.pdf)** -- real examples from the current pipeline.

## Get Started

Pilot programs scoped to your ticker coverage, with broader universes and historical backfill available.

**[Book a 15-minute data review](https://calendar.app.google/s6wDVSaJuqCkwcmg9)** -- tell us which tickers or sectors you cover and we'll show you what we see.

Or email [matt@municipalalpha.com](mailto:matt@municipalalpha.com?subject=Contractor%20signals%20inquiry%20%28via%20landing%20page%29) -- we'll send a coverage report within one business day.
