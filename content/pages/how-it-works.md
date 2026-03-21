Title: How It Works
Slug: how-it-works
Sortorder: 3

## A Knowledge Graph of US Public Records

This is not five separate products stitched together. It is a knowledge graph -- entities, types, properties, and the relationships between them, continuously growing as new documents are ingested. Every municipality we add, every document we parse, every entity we resolve adds nodes and edges to the graph. Different data types from different jurisdictions connect into a unified picture because the graph connects them.

Google built its Knowledge Graph by acquiring Metaweb, the company behind Freebase, turning the messy open web from strings into things. We are doing the same thing for US public records. 19,500 municipalities publishing in their own formats, their own portals, their own filing systems. We resolve that into a single graph of entities and relationships: which town paid which vendor, which parcel has which lease, which estate disclosed which assets.

## How a Parcel Connects Everything

![Diagram showing a single parcel connected to five data sources: Assessor Records, FCC Registry, FAA Database, Check Register, and Planning Board]({static}/images/intelligence-layer.png)

A single parcel in Falmouth, Maine appears in:

- **Assessor data** -- tower lease, landowner identity, property valuation
- **FCC registry** -- tower tenant (American Tower, Crown Castle, etc.)
- **FAA filing database** -- construction permit, tower height, coordinates
- **Municipal check register** -- lease payment to landowner, amount, frequency
- **Planning board agenda** -- zoning variance, public hearing, conditions

Each source adds nodes and edges to that parcel's place in the graph. None is complete alone. Together, they produce a lead that no single-source competitor can match.

## How an Entity Connects Everything

An entity like American Tower appears in assessor records across 50 states, FCC registrations nationwide, FAA filings, municipal RFPs, insurance rate filings (tower liability coverage), and county recorder mineral lease assignments. Each appearance enriches the entity's node in the graph, connecting it to new jurisdictions, new document types, new relationships.

Resolving "Waste Management of Maine" to ticker WM in AP data simultaneously improves entity resolution for insurance rate filings, permit data, and contract tracking. One resolution, four graph improvements.

## How a Jurisdiction Connects Everything

A single jurisdiction like Cumberland County, Maine produces assessor data (tower + solar + utility leases), probate filings (estate property transfers), recorder data (mineral rights, if applicable), municipal spending (AP + permits), and insurance territory data. All from one county.

Every new jurisdiction added to the pipeline activates data for every active vertical simultaneously. The graph gets denser, and denser graphs produce better intelligence.

## Why 19,500 Municipalities

The big data vendors cover New York and Chicago. We cover the 19,500 small and mid-sized municipalities that issue the same building permits, check registers, and assessor records, just on worse websites, behind more obscure FOIA statutes. AI agents make that possible. Our pipeline runs daily, autonomously.

Nobody else reads Gorham, Maine. Or Pocatello, Idaho. Or the thousands of other towns where the finance director posts a check register to a CivicPlus portal and nobody outside city hall ever looks at it. Those check registers contain the same vendor payment data that Bloomberg terminals show for federal contracts, just at the local level, where 19,500 jurisdictions spend a combined $3.9 trillion annually on payroll, infrastructure, services, and procurement.

The coverage gap is the product. US municipalities collectively issue roughly 1.5 million building permits per year, process billions in vendor payments, publish thousands of planning board decisions, and file hundreds of thousands of public records annually. Almost none of it is structured. The few vendors that touch municipal data focus on the largest cities or aggregate at the state level, missing the transaction-level detail where the signal lives.

We're not building a better way to read New York City's budget. We're building the first way to read Gorham's check register, and Pocatello's building permits, and Geneva's vendor payments, at the same time, every day, automatically.

**Where we are today:**

- **1,800+** municipalities monitored daily, all 50 states
- **292,000+** documents ingested and classified
- **43,000+** building permits structured
- **100+** public company tickers resolved from municipal vendor names
- Adding ~25 new municipalities per week, with infrastructure built to scale past 5,000

**Where this goes:**

- **19,500** US municipalities issuing these same records
- **~1.5M** building permits issued nationally per year (Census Bureau)
- **$3.9T** in annual municipal government spending (Census of Governments)
- **$4T** municipal bond market
- **130,000+** FCC-registered tower structures

The marginal cost of adding a municipality to the pipeline is near zero once the CMS connector exists, and six connector platforms cover roughly 80% of US municipal websites. The graph gets denser with every town added, and denser graphs produce better intelligence.

## The AI Agent Architecture

Every product on this platform shares the same core capability: AI agents that discover data sources, file records requests, navigate government portals, parse unfamiliar document formats, extract structured data, and resolve entities into the knowledge graph. The agents are general-purpose. What changes per vertical is the detection patterns, the data sources, and the buyer. The infrastructure is built once.

| Agent Capability | Verticals It Serves |
|---|---|
| FOIA/FOIL/OPRA filing (state-adapted) | All verticals |
| Government portal discovery + scraping | All verticals |
| Document classification (LLM-based) | Alt data, insurance, probate |
| Entity resolution (vendor/company names) | Alt data, insurance |
| Parcel screening + owner resolution | Tower leases, mineral rights |
| Chain-of-title tracing | Mineral rights, probate |
| Format auto-detection + parsing | All verticals |
| Lead scoring + qualification | Tower leases, mineral rights, probate |
| Cross-reference with federal databases | Tower (FCC/FAA), mineral (BLM), insurance (NAIC) |

## Automated Public Records Requests

Most valuable government data isn't on a website. Assessor records, detailed check registers, and permit databases usually require a formal public records request -- FOIA at the federal level, but every state has its own statute with its own rules, deadlines, contact roles, and fee structures. Maine calls it FOAA. New Hampshire calls it Right-to-Know. New York calls it FOIL.

The platform files these requests autonomously, adapted to each state's statute. But the real advantage isn't the filing -- it's the learning. Over hundreds of requests, the system tracks which contact roles respond (town clerks vs. assessors vs. finance directors), which email formats get through, which request language produces usable data vs. form-letter denials, optimal cooling periods between follow-ups, and which towns respond to the first request vs. the third. Every interaction is scored. Successful patterns propagate to similar jurisdictions automatically. Failed approaches get deprioritized.

A competitor can read the statute. They can't replicate what we've learned from the responses.

## Building Permits as a Signal Source

Building permits are one of the most underrated public data sources. Every commercial construction project, infrastructure upgrade, and development phase starts with a permit. The data tells you which contractors are winning work, which developers are active in a geography, where infrastructure spending is accelerating, and how local construction activity maps to public company revenue -- months before any of it shows up in earnings or analyst reports.

Small and mid-sized municipalities issue the same permits as large cities, just on worse websites with less standardization. That's where the coverage gap is widest. We structure 16,000+ permit records and growing, resolved to entities and tickers where possible.

## The Pipeline

![Diagram showing the self-improving pipeline cycle: Crawl, Classify, Score, Improve, Learn]({static}/images/pipeline-loop-v2.png)

The system runs daily, autonomously. It crawls municipal portals, classifies documents, resolves entities to public company tickers, scores signals, and delivers qualified leads. Self-healing automation detects when a municipality changes its website and adapts. A reward-based learning system tracks which automated actions succeed and evolves strategy over time. When a fix works for one town, the system propagates it to similar towns with decaying confidence by similarity.

The pipeline doesn't just collect data. It files records requests, processes responses, follows up on non-responses, onboards new jurisdictions, retrains its own classifiers, and evaluates the business value of every action it takes. Every day it runs, it gets better at running.
