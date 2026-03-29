Title: Data Stories
Slug: data-stories
Sortorder: 2
Summary: Structured datasets and cross-municipal patterns from live pipeline data across 2,100+ municipalities. Updated daily.

We read municipal documents -- agendas, minutes, check registers, permits, budgets, ordinances -- across 2,100+ municipalities. The pipeline classifies every document, resolves vendor names to public company tickers, and tracks policy contagion across jurisdictions. Here's what comes out.

## The Datasets

Five structured data products, each built from different source documents, each updated daily.

### Entity-Resolved Vendor Payments

Vendor names from check registers and AP warrants resolved to public company tickers across 200+ municipalities. Payment amounts, dates, and document context included. One check register is a curiosity. Entity-resolved payments across hundreds of jurisdictions is a revenue signal.

**Source documents:** Check registers, AP warrants, budget line items, RFP awards
**Output fields:** municipality, state, vendor_raw, vendor_resolved, ticker, amount_usd, doc_type, date, signal_priority
**Coverage:** 200+ municipalities, 100+ resolved tickers, tens of thousands of entity sightings
[Download sample CSV](/sample-data/signals-sample.csv)

---

### Contagion and Policy Signals

Cross-municipal event tracking for regulatory waves, infrastructure mandates, and spending cascades. The pipeline detects when the same policy topic (PFAS remediation, lead pipe replacement, ADU mandates) appears across multiple jurisdictions and maps the contagion chain -- which town moved first, how fast it spread, what supply chain tickers are affected.

**Source documents:** Meeting agendas, minutes, ordinances, compliance reports, public hearing notices
**Output fields:** municipality, state, event_type, contagion_chain, date, risk_category, supply_chain_tickers
**Coverage:** 2,100+ municipalities, 23+ contagion patterns tracked, 50 states
[Download sample CSV](/sample-data/infrastructure-risk-sample.csv)

---

### Tower and Infrastructure Lease Prospects

Cell tower sites cross-referenced across assessor records, FCC antenna structure registrations, FAA obstruction data, and municipal check registers. Parcel-level records with owner identification, tenant type, and confidence scoring. Built for infrastructure aggregators and tower companies doing site acquisition.

**Source documents:** Assessor/property records, FCC ASR filings, FAA OE data, municipal check registers, GIS parcels
**Output fields:** municipality, state, lat/lon, structure_height, fcc_asr_id, tenant_type, owner_type, data_sources, confidence_score
**Coverage:** 4,700+ sites screened across covered municipalities
[Download sample CSV](/sample-data/tower-prospects-sample.csv)

---

### Building Permits and Contractor Signals

Structured permit records from 400+ municipalities resolved to public company tickers where applicable. Permit type, value, contractor, and address. Leading indicator for construction activity and government contractor revenue.

**Source documents:** Municipal permit portals, planning board approvals, building department records
**Output fields:** municipality, state, vendor_name, ticker, doc_type, document_date, context_snippet
**Coverage:** 400+ municipalities, 43,000+ structured permit records
[Download sample CSV](/sample-data/contractor-signals-sample.csv)

---

### Credit Quality Indicators

Budget trends, fund balances, debt service patterns, and fiscal stress signals structured from municipal financial documents. The source documents that ratings agencies eventually read, structured daily instead of annually.

**Source documents:** Annual budgets, financial reports, capital improvement plans, debt schedules, audit reports
**Output fields:** municipality, doc_type, priority, summary, monetary_amounts, detected_at
**Coverage:** 2,100+ municipalities
[Download sample CSV](/sample-data/credit-sample.csv)

---

Every dataset is documented in our [methodology](/methodology/), including coverage maps, freshness guarantees, and known gaps. If you need data from a jurisdiction we don't cover yet, we can usually onboard a new municipality in days.

## Data Stories

These stories are built entirely from the datasets above. Each one demonstrates a pattern that's only visible when you monitor 2,100+ municipalities at once.

- [PFAS Is Spreading Through Municipal Agendas Faster Than Groundwater](/research/pfas-contagion/) -- 120 events across 72 municipalities in 23 states. The remediation wave is visible in town council agendas months before EPA enforcement actions. *Built from: contagion signals, entity-resolved vendor payments*
- [The Company That Shows Up in 123 Towns](/research/company-footprint/) -- Entity resolution across 2,100+ municipalities reveals which public companies have the deepest municipal government footprint. Verizon: 6,183 sightings. Tyler Technologies: 88 towns. *Built from: entity-resolved vendor payments*
- [The Housing Density Wave Is Rewriting Municipal Zoning in Real Time](/research/housing-density-wave/) -- 399 events across 130+ municipalities in 27 states. ADU mandates, density increases, and short-term rental regulation are one wave, moving through regions at different speeds. *Built from: contagion signals, building permits*
- [Lead Pipes Are a $50B Problem Hiding in Municipal Agendas](/research/lead-pipes/) -- 77 events across 39 municipalities in 13 states. The EPA's Lead and Copper Rule is creating a predictable cascade of municipal spending. *Built from: contagion signals, entity-resolved vendor payments*
- [The Pickleball Boom Is Now a Line Item in Municipal Budgets](/research/pickleball-wave/) -- 29 signals across 14 municipalities in 9 states. From federal grants to tennis court conversions, a consumer trend becoming municipal capex. *Built from: contagion signals, credit quality indicators*
- [Data Centers Are Now a Zoning Fight in 20 States](/research/data-center-zoning/) -- 58 signals across 30 jurisdictions in 20 states. Moratoriums, tax breaks, and electricity caps are hitting municipal agendas faster than the power grid can keep up. *Built from: contagion signals, state legislature tracking, federal solicitations*

## Town Profiles

What the pipeline sees in a single municipality -- document volume, signal classification, entity resolution, infrastructure data, and vendor landscape. Each profile is auto-generated from continuous monitoring.

- [Falmouth, Maine](/profiles/falmouth-me/) -- 689 documents, 18 boards, 45 tickers, 8 tower sites. Coastal New England town with active development, climate, and infrastructure lease signals.
- [Geneva, Illinois](/profiles/geneva-il/) -- 1,338 documents, 45 boards, 50 tickers, 257 check registers. The alt data story: entity resolution maps vendor payments to public company revenue across 1,700+ sightings.
- [Pocatello, Idaho](/profiles/pocatello-id/) -- 2,244 documents, 39 boards, 98 HIGH signals, 38 tower sites. The town nobody's watching, producing more high-priority signals than cities ten times its profile.

---

## What should we investigate next?

The pipeline monitors 2,100+ municipalities in real time. If there's a trend, policy wave, or spending pattern you'd like us to dig into, we'll build the data story. [Tell us what you're curious about](mailto:matt@municipalalpha.com?subject=Data%20story%20request).
