Title: Solutions
Slug: solutions
Sortorder: 1

<style>
.sol-hero {
    max-width: 640px;
    margin-bottom: 48px;
}
.sol-hero h2 {
    font-family: 'Newsreader', serif;
    font-size: 28px;
    font-weight: 500;
    color: #0C0C0C;
    margin-bottom: 16px;
    margin-top: 0;
}
.sol-hero p {
    font-size: 17px;
    color: #555;
    line-height: 1.7;
    margin-bottom: 24px;
}

.sol-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
    margin-bottom: 56px;
}

.sol-card {
    border: 1px solid #E8E4DF;
    border-radius: 6px;
    overflow: hidden;
    background: #fff;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    transition: border-color 0.15s, box-shadow 0.15s;
}
.sol-card:hover {
    border-color: #E8512D;
    box-shadow: 0 2px 16px rgba(232, 81, 45, 0.1);
}

.sol-card-img {
    width: 100%;
    height: 160px;
    object-fit: cover;
}

.sol-card-body {
    padding: 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.sol-card-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #E8512D;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}

.sol-card h3 {
    font-family: 'Newsreader', serif;
    font-size: 20px;
    font-weight: 500;
    color: #0C0C0C;
    margin: 0 0 8px;
    line-height: 1.3;
}

.sol-card-hook {
    font-size: 14px;
    color: #555;
    line-height: 1.6;
    margin-bottom: 16px;
    flex: 1;
}

.sol-card-proof {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #888;
    border-top: 1px solid #E8E4DF;
    padding-top: 12px;
    margin-top: auto;
}
.sol-card-proof strong {
    color: #0C0C0C;
    font-weight: 600;
}

.sol-mid-cta {
    background: #0C0C0C;
    color: #F7F4F0;
    border-radius: 6px;
    padding: 40px 48px;
    margin: 8px 0 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
    flex-wrap: wrap;
}
.sol-mid-cta h3 {
    font-family: 'Newsreader', serif;
    font-size: 22px;
    font-weight: 500;
    margin: 0 0 8px;
    color: #F7F4F0;
}
.sol-mid-cta p {
    font-size: 14px;
    color: #aaa;
    margin: 0;
    line-height: 1.5;
}
.sol-mid-cta .cta-button {
    flex-shrink: 0;
}

.sol-proof-section {
    background: #F7F4F0;
    border-radius: 6px;
    padding: 40px 48px;
    margin-bottom: 56px;
    text-align: center;
}
.sol-proof-quote {
    font-family: 'Newsreader', serif;
    font-size: 20px;
    font-style: italic;
    color: #0C0C0C;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto 12px;
}
.sol-proof-attr {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.sol-bottom-cta {
    text-align: center;
    padding: 24px 0 8px;
}
.sol-bottom-cta h3 {
    font-family: 'Newsreader', serif;
    font-size: 24px;
    font-weight: 500;
    color: #0C0C0C;
    margin-bottom: 12px;
}
.sol-bottom-cta p {
    font-size: 15px;
    color: #555;
    margin-bottom: 24px;
    line-height: 1.6;
}
.sol-bottom-cta .sol-or {
    display: block;
    margin: 16px 0;
    font-size: 13px;
    color: #888;
}
.sol-bottom-cta a.sol-email {
    color: #E8512D;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
}
.sol-bottom-cta a.sol-email:hover {
    text-decoration: underline;
}

@media (max-width: 640px) {
    .sol-grid { grid-template-columns: 1fr; }
    .sol-mid-cta { padding: 28px 24px; flex-direction: column; text-align: center; }
    .sol-proof-section { padding: 28px 24px; }
    .sol-proof-quote { font-size: 18px; }
}
</style>

<div class="sol-hero">
<h2>You see the thing before it becomes a thing</h2>
<p>Every day, 19,500 town halls publish documents that predict market events weeks or months before they happen. Vendor payments before earnings. Planning votes before permits. Budget approvals before RFPs. I built a system that reads them all.</p>
<a href="https://calendar.app.google/s6wDVSaJuqCkwcmg9" class="cta-button">Book a 15-Minute Data Review</a>
</div>

<div class="sol-grid">

<a href="/solutions/alt-data/" class="sol-card">
<img src="/images/story-company-footprint.png" alt="Municipal Alt Data" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Quant &amp; Fundamental</div>
<h3>Municipal Alt Data</h3>
<div class="sol-card-hook">Pre-earnings municipal signals. Vendor payments and building permits resolved to public company tickers. You see the revenue before quarterly reports.</div>
<div class="sol-card-proof"><strong>128</strong> tickers tracked &middot; <strong>319K</strong> signal-ticker pairs measured</div>
</div>
</a>

<a href="/solutions/tower-leads/" class="sol-card">
<img src="/images/story-data-center-zoning.png" alt="Tower & Infrastructure Leads" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Infrastructure &amp; REITs</div>
<h3>Tower &amp; Infrastructure Leads</h3>
<div class="sol-card-hook">Pre-listing lease intelligence. Qualified tower prospects with parcel data and owner ID. You contact the landowner before anyone else knows the lease exists.</div>
<div class="sol-card-proof"><strong>7,700+</strong> tower sites screened &middot; <strong>23-month</strong> avg competitive window</div>
</div>
</a>

<a href="/solutions/credit-intelligence/" class="sol-card">
<img src="/images/story-lead-pipes.png" alt="Municipal Credit Intelligence" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Fixed Income</div>
<h3>Municipal Credit Intelligence</h3>
<div class="sol-card-hook">Pre-downgrade fiscal intelligence. Leading indicators of stress from source spending documents. You see the fiscal distress before the rating agency does.</div>
<div class="sol-card-proof"><strong>8.7x</strong> separation ratio &middot; distressed vs stable municipalities</div>
</div>
</a>

<a href="/solutions/contractor-signals/" class="sol-card">
<img src="/images/story-housing-wave.png" alt="Government Contractor Signals" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Equity Research</div>
<h3>Government Contractor Signals</h3>
<div class="sol-card-hook">Pre-earnings municipal signals. Vendor payments and permits mapped to public tickers. Bottom-up revenue signals that top-down models miss.</div>
<div class="sol-card-proof"><strong>43K</strong> permits tracked &middot; <strong>2,500+</strong> municipalities</div>
</div>
</a>

<a href="/solutions/energy-development/" class="sol-card">
<img src="/images/story-renewable-energy.png" alt="Renewable Energy Siting" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Project Origination</div>
<h3>Renewable Energy Siting</h3>
<div class="sol-card-hook">Pre-RFP project intelligence. Zoning decisions, planning approvals, and environmental permits. You know about the project before the RFP is written.</div>
<div class="sol-card-proof"><strong>20K+</strong> HIGH-priority signals &middot; <strong>50</strong> states covered</div>
</div>
</a>

<a href="/solutions/infrastructure-risk/" class="sol-card">
<img src="/images/story-pfas.png" alt="Municipal Infrastructure Risk" class="sol-card-img">
<div class="sol-card-body">
<div class="sol-card-tag">Insurance &amp; Risk</div>
<h3>Infrastructure Risk Intelligence</h3>
<div class="sol-card-hook">Pre-event risk intelligence. PFAS contamination, lead pipe replacement, deferred maintenance, consent decree tracking. You see the risk before the claim.</div>
<div class="sol-card-proof"><strong>459</strong> contagion topics tracked across municipalities</div>
</div>
</a>

</div>

<div class="sol-mid-cta">
<div>
<h3>Not sure which fits?</h3>
<p>Tell me what you're working on. I'll show you what I can see before it hits your current sources.</p>
</div>
<a href="https://calendar.app.google/s6wDVSaJuqCkwcmg9" class="cta-button">Book a 15-Minute Call</a>
</div>

<div class="sol-proof-section">
<div class="sol-proof-quote">"No one's doing anything related to this in any way, shape, or form that I am aware of."</div>
<div class="sol-proof-attr">Financial Advisor, Wealth Management</div>
</div>

<div class="sol-bottom-cta">
<h3>366,000 documents. 2,500 municipalities. Updated every night.</h3>
<p>The same precursor intelligence powers every product above. The question is how your industry uses the timing advantage.</p>
<a href="https://calendar.app.google/s6wDVSaJuqCkwcmg9" class="cta-button">Book a Data Review</a>
<span class="sol-or">or</span>
<a href="mailto:matt@municipalalpha.com?subject=Solutions%20inquiry" class="sol-email">matt@municipalalpha.com</a>
</div>
