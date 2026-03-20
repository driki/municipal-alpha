Title: The Company That Shows Up in 123 Towns
Slug: research/company-footprint
Sortorder: 21

*Analysis based on entity resolution across 1,800+ municipalities. Data current as of March 2026.*

## Municipal Government Revenue Is Hiding in Plain Sight

Every municipality in America pays vendors. Phone companies, waste haulers, equipment suppliers, software providers, utilities. These payments are recorded in public documents -- check registers, budgets, RFPs, contracts, meeting minutes. The documents are public. The vendors are often publicly traded. And nobody is connecting the dots at scale.

We are. Our pipeline resolves vendor names to public company tickers across 1,800+ municipalities. The result is a dataset that shows which companies have the deepest municipal government footprint in America, sourced from the actual payment records.

## The Scale

The dataset is growing as the pipeline expands coverage.

| Month | Entity Sightings | Unique Tickers | Municipalities |
|---|---|---|---|
| February 2026 | 932 | 53 | 49 |
| March 2026 | 93,083 | 116 | 441 |

That's a 100x increase in a single month as we onboarded new municipalities and backfilled their document archives. Every new town brings its own vendor relationships, and every vendor relationship that maps to a public company enriches the dataset. At current trajectory, the pipeline will process 1M+ entity sightings within the next quarter.

The database is young. The compounding is fast.

## The Top 15

| Company | Ticker | Municipalities | Sightings | Doc Types |
|---|---|---|---|---|
| American Tower | AMT | 123 | 207 | 10 |
| AT&T | T | 118 | 1,985 | 15 |
| Crown Castle | CCI | 116 | 384 | 11 |
| Verizon | VZ | 113 | 6,183 | 16 |
| Waste Management | WM | 101 | 2,007 | 15 |
| Comcast | CMCSA | 97 | 3,397 | 16 |
| T-Mobile | TMUS | 89 | 1,314 | 14 |
| Tyler Technologies | TYL | 88 | 1,163 | 14 |
| Charter Communications | CHTR | 75 | 1,731 | 14 |
| Algonquin Power | AQN | 72 | 2,070 | 16 |
| Ferguson Enterprises | FERG | 71 | 795 | 12 |
| Amazon | AMZN | 69 | 2,932 | 10 |
| Eversource Energy | ES | 67 | 2,628 | 15 |
| Core & Main | CNM | 66 | 935 | 12 |
| Badger Meter | BMI | 63 | 282 | 13 |

Verizon appears in 113 municipalities with 6,183 individual sightings -- check register payments, RFP mentions, contract references, budget line items. That's recurring government revenue from the actual source documents.

And this is from 1,800 municipalities. The United States has 19,500.

## What the Breadth Tells You

The companies at the top of this list aren't surprising. Of course municipalities pay AT&T and Waste Management. But the data gets interesting in the details:

**Telecom is the deepest municipal vertical.** The top three non-tower companies by municipal footprint are AT&T (118 towns), Verizon (113), and Comcast (97). Municipal telecom spending is operationally recurring, budget-resistant, and growing (broadband mandates, public safety networks, IoT infrastructure). This is not discretionary spend.

**Tyler Technologies is in 88 towns.** TYL provides municipal software -- tax collection, court management, utility billing, permitting. Eighty-eight towns means 88 recurring SaaS contracts, visible in check registers as monthly or annual payments. When a municipality adopts Tyler, they rarely switch. This is municipal lock-in, measurable from public documents.

**Water infrastructure companies have national reach.** Core & Main (66 towns), Badger Meter (63), Mueller Water (56), Xylem (57), American Water Works (61). These aren't household names, but they're embedded in municipal water operations across the country. Every water main break, every meter replacement, every treatment upgrade flows through these companies.

**Amazon is a municipal vendor.** Sixty-nine towns, 2,932 sightings. Municipalities buy office supplies, server equipment, cleaning supplies, and maintenance items through Amazon. It's a line item in check registers that most analysts don't think about, but it's measurable, it's recurring, and it's growing.

## The Entity Resolution Problem

The hard part isn't finding the data. It's resolving the entities.

"WASTE MGMT" in one town's check register is the same company as "Waste Management of Maine" in another and "WM" in a third. "CORE & MAIN LP" matches "Core and Main" matches "HD SUPPLY WATERWORKS" (their former name). Our pipeline handles this across every municipality, resolving variant names to canonical entities and tickers.

This is why nobody else has this dataset. The documents are public. The entity resolution at scale is the hard part. And it gets better with every municipality we add -- every new name variant we resolve improves resolution for every other town.

## What You Can Do With This

One check register from one town is a curiosity. Entity-resolved vendor payment data across 1,800 municipalities is an alternative dataset that tracks public company government revenue from the source documents, in near-real-time, before it shows up in quarterly earnings.

The applications are straightforward:

- **Revenue signal.** If a company's municipal payment volume is growing quarter over quarter across dozens of jurisdictions, that's a revenue signal.
- **Market share.** If Tyler Technologies is in 88 towns and a competitor is in 12, that's a market share signal.
- **Geographic exposure.** If a company's municipal revenue is concentrated in one state, that's a concentration risk signal.
- **Contract lifecycle.** RFPs show new opportunities. Check registers show active payments. The absence of payments after years of presence shows a lost contract.

We see all of these. Across every municipality in the pipeline. Every day.

Interested in entity-resolved municipal vendor data? [Get in touch](/contact/).
