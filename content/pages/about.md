Title: About
Slug: about
Sortorder: 4

## Two Precedents

**The business model:** The Echo Nest built a structured understanding of music from fragmented public sources -- audio fingerprints, blogs, reviews, social signals, listening data. No single source was complete. But by ingesting everything, structuring it, and building intelligence on top, they created the canonical understanding of music that Spotify, Pandora, and the rest of the streaming industry built on. They didn't sell music. They sold structured understanding of music. Multiple revenue streams on one underlying data asset. Started with a small team at MIT Media Lab, grew to ~50 people at acquisition. Acquired by Spotify for ~$100M in 2014 because the data asset was irreplaceable and would take years to rebuild.

**The technical architecture:** Google acquired Metaweb in 2010 to get Freebase, a collaborative knowledge base that structured the messy open web into entities and relationships. That acquisition became the Google Knowledge Graph, shifting search from keywords to real-world things -- people, places, companies, and how they connect. The technical insight was that structured relationships between entities are more valuable than the raw documents that contain them.

We are building the same thing for US public records. The Echo Nest's business model, built on a knowledge graph architecture.

## The Same Problem, Different Domain

US public records have the same problem music had. 19,500 municipalities, 3,100 counties, 50 state agencies, and thousands of special-purpose courts and commissions, each publishing in its own format, on its own website, behind its own filing system. Insurance rate filings that predict earnings. Probate inventories that reveal asset transfers. Mineral deeds that identify tradeable royalty positions. Municipal check registers that signal government contractor revenue. Assessor records that map infrastructure lease holders.

All of it is public by law. None of it is structured into entities and relationships. No one aggregates it because the acquisition cost has always been too high -- too many jurisdictions, too many formats, too much human labor.

The big data vendors cover New York and Chicago. Nobody is systematically reading Gorham, Maine or Franklin, New Hampshire. But small and mid-sized municipalities issue the same building permits, the same check registers, the same assessor records as large cities -- just on worse websites, with less standardization, behind more obscure FOIA statutes. That's where the gap is widest and the signal is least picked-over. Building permits alone tell you which contractors are winning work, which developers are active in a geography, and where infrastructure spending is accelerating -- months before it shows up in earnings.

The system is good at finding things because it has spent a year learning the system it operates in. Which CMS platforms hide documents behind JavaScript. Which FOIA statutes require which language. Which assessor offices respond to email and which require certified mail. Which board names mean "check registers" in which towns. None of this was designed upfront. It was learned through contact with 1,800+ jurisdictions, thousands of FOIA interactions, and hundreds of dead ends that each taught the system something. Every interaction produces a recipe. The recipes accumulate.

## Why This Matters Now

Bond yields set the price of money. In a high-rate environment, municipal credit quality is the highest-stakes bet in fixed income. The cost of being wrong about a municipal credit position goes up when replacement capital is expensive.

Municipal governments under fiscal stress show it in AP data first -- delayed vendor payments, vendor concentration shifts, spending velocity drops. We see these patterns daily, from the actual source documents, months before they surface in bond ratings or credit downgrades.

When rates are high, we're a credit signal. When rates are low, we're an equity signal -- vendor payment anomalies predict government contractor revenue. Either way, someone needs what we see.

## The Scale of the Opportunity

The numbers behind the coverage gap:

| What exists nationally | Volume | What's structured today |
|---|---|---|
| US municipalities | 19,500 | We monitor 1,800+ daily |
| Building permits issued annually | ~1.5 million (Census Bureau) | 43,000+ structured in our pipeline |
| Annual municipal government spending | $3.9 trillion (Census of Governments) | Vendor payments from 1,800+ towns, 100+ resolved tickers |
| Municipal bond market | $4 trillion (SIFMA) | Credit signals from source spending documents |
| FCC-registered tower structures | 130,000+ | 3,800+ screened with parcel cross-reference |
| Municipal infrastructure investment gap | $2.6 trillion (ASCE) | Deferred maintenance signals from spending patterns |

These records all exist as public documents. The acquisition cost has been too high for anyone to aggregate them, too many jurisdictions, too many CMS platforms, too many state-specific FOIA statutes. AI agents change the unit economics. Six CMS connectors cover roughly 80% of US municipal websites, and the marginal cost of adding a municipality to the pipeline is near zero once the connector exists.

We add ~25 municipalities per week. The pipeline infrastructure scales past 5,000. Every new municipality activated produces data for every revenue vertical simultaneously, the cost is paid once and the revenue compounds across verticals.

## Revenue Verticals

Applications built on the knowledge graph, not separate businesses.

| Vertical | Data Source | Buyer | Status |
|---|---|---|---|
| Infrastructure lease intelligence | Municipal assessor records + FCC/FAA | Tower REITs, aggregators, solar/wind developers | Pilot live |
| Municipal alternative data | Municipal AP, permits, agendas | Hedge funds, permit aggregators | Signal validated |
| Insurance rate filing intelligence | State DOI filing portals | Hedge funds, insurers, research | Ready to build |
| Mineral rights intelligence | County recorder deeds + state O&G commissions | Mineral aggregators, energy PE | Ready to build |
| Probate & estate intelligence | County probate courts | Wealth mgmt, RE investors, PE | Ready to build |

## The Compounding Effect

![Diagram showing one jurisdiction at top funneling into multiple revenue verticals below]({static}/images/compounding-effect.png)

Two things compound in this system, and the second one is less obvious. The data compounds: more jurisdictions, more documents, more cross-references, more history. But the operational intelligence also compounds. Every FOIA interaction teaches the system something about that jurisdiction. Every failed crawl produces a recipe for the next attempt. Every edge case solved becomes available to every future jurisdiction. The system does not just get bigger. It gets better at locating things.

- One FOIA request to a municipal assessor produces tower lease leads, solar lease leads, property tax signals, AND feeds alt data scoring. Five products from one acquisition.
- One entity resolution ("Waste Management of Maine" resolves to ticker WM) simultaneously improves insurance rate filing data, permit tracking, and contract award detection.
- One new jurisdiction activates documents for alt data, parcels for infrastructure screening, jurisdiction coverage for insurance territory mapping, and a new court for probate monitoring. And it onboards faster than the last one, because the recipe library is larger.
- One dead end: the FCC tower registration database missed a $50K/year tower lease in rural Maine. That dead end produced a recipe combining ULS licenses, FAA filings, trail databases, and elevation data. That recipe now applies to every rural tower search, not just the one that produced it.

The cost of acquiring a jurisdiction is paid once. The revenue is collected from every vertical that uses it. And the recipe learned from acquiring it makes the next acquisition cheaper.

## The Moat

The mess is why nobody starts. The recipes are why nobody catches up.

- **Recipes compound faster than data.** The data asset grows linearly with jurisdictions covered. The recipe library grows combinatorially, because a recipe learned in one context often applies in others. The recipe for extracting tower data from unorganized territories came from combining five techniques each learned in a different jurisdiction. A competitor would need to hit those same dead ends to develop the same recipe.
- **Time is the ingredient you cannot buy.** The system knows which FOIA language works in Maine vs New Hampshire, which assessor offices send Vision caidump format vs custom exports, which CMS platforms require JavaScript rendering, which board names correspond to financial data in which towns. This is not infrastructure. It is accumulated operational intelligence. It took a year of daily interactions to learn. A well-funded competitor starting today starts with zero recipes.
- **The work is unglamorous.** Nobody wants to parse 15 assessor data formats, navigate 50 state FOIA statutes, build connectors for 6 CMS platforms, or trace mineral title chains through 100-year-old deeds. This is exactly the kind of messy, real-world work that well-funded competitors find unappealing. That is fine. We like it here.
- **Cross-domain recipes transfer.** A FOIA playbook developed for Maine municipal assessors applies to Maine school districts and special districts too, same statute, same language. A CMS connector built for one CivicPlus municipality works for hundreds. Every new domain entered activates recipes already in the library.

## The Team

Built and operated by Matt MacDonald. One person, one automated pipeline, running daily.
