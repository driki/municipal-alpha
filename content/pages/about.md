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

AI agents change the math. What used to require a team of 50 people filing FOIA requests and parsing PDFs can now be done by one person with an automated pipeline. We built that pipeline. It runs daily, autonomously. The same architecture extends to every public record type in the country.

## Why This Matters Now

Bond yields set the price of money. In a high-rate environment, municipal credit quality is the highest-stakes bet in fixed income. The cost of being wrong about a municipal credit position goes up when replacement capital is expensive.

Municipal governments under fiscal stress show it in AP data first -- delayed vendor payments, vendor concentration shifts, spending velocity drops. We see these patterns daily, from the actual source documents, months before they surface in bond ratings or credit downgrades.

When rates are high, we're a credit signal. When rates are low, we're an equity signal -- vendor payment anomalies predict government contractor revenue. Either way, someone needs what we see.

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

This platform's understanding of a jurisdiction improves every time a new document is ingested, a new entity is resolved, a new parcel is screened, or a new relationship is mapped. The graph gets denser, and denser graphs produce better intelligence. After 2-3 years, the platform doesn't just have data -- it has a knowledge graph of how US local government works, who owns what, who pays whom, and how infrastructure, money, and people flow through the system.

- Assessor data for tower lease screening simultaneously produces solar/wind/utility lease leads, property tax delinquency signals, municipal fiscal health indicators, and the parcel-level foundation for probate property matching. One FOIA request, five products.
- Resolving "Waste Management of Maine" to ticker WM in AP data simultaneously improves entity resolution for insurance rate filings, permit data, and contract tracking. One resolution, four graph improvements.
- Adding a new municipality to the pipeline adds documents to alt data, parcels to infrastructure screening, jurisdiction coverage to insurance territory mapping, and a new court for probate monitoring. One onboarding, multiple revenue streams activated.

The cost of acquiring a jurisdiction is paid once. The revenue is collected from every vertical that uses it.

## The Moat

- **Compounding knowledge graph.** Every jurisdiction scraped, every FOIA response received, every document classified, every entity resolved adds nodes and edges to a proprietary graph that no competitor has. The data is public in theory. In practice, acquiring and structuring it across thousands of jurisdictions takes years.
- **Agent sophistication is cumulative.** Every edge case -- a quirky CMS, a state-specific FOIA statute, an unusual assessor format, a complex chain of title -- becomes embedded knowledge in the agent workflows. A competitor starting from scratch has to rediscover every one of these. There are hundreds.
- **The work is unglamorous.** Parsing 15 assessor data formats, navigating 50 state FOIA statutes, building connectors for 6 CMS platforms, tracing mineral title chains through 100-year-old deeds. This is exactly the kind of messy, real-world infrastructure that well-funded competitors find unappealing. That ugliness is the moat.
- **Learned FOIA/FOAA intelligence.** The platform files public records requests autonomously, adapted to each state's statute (FOIA, FOIL, OPRA, Right-to-Know). Over hundreds of requests, the system has learned which contact roles respond, which email formats get through, which request language produces data vs. denials, and how long to wait before following up. It tracks every interaction, scores outcomes, and evolves its approach. A competitor can read the statute, but they can't replicate what we've learned from the responses.

## The Team

Built and operated by Matt MacDonald. One person, one automated pipeline, running daily.
