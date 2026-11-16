from common import *
import os
os.makedirs('modules',exist_ok=True)
MCSS='''.spec{height:48px;display:flex;align-items:center;padding:0 96px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--slate);border-bottom:1px solid var(--line);font-family:Bricolage;font-stretch:90%}
.spec .r{margin-left:auto;color:var(--ink)}
.m{padding:88px 96px 96px;position:relative}
.g12{display:grid;grid-template-columns:repeat(12,1fr);column-gap:24px}
'''
def mod(n,name,body,css='',bg='var(--white)'):
    spec=f'<div class="spec">Razor Profiles · Direction 1 — Clean Cut<span class="r">Module {n:02d} / 10 — {name}</span></div>'
    html=page(spec+body,MCSS+css).replace('<body>',f'<body style="background:{bg}">')
    slug=f'{n:02d}-'+name.lower().replace(' + ','-').replace(' ','-').replace('’','').replace("'",'')
    open(f'modules/{slug}.html','w').write(html.replace('url(fonts/','url(../fonts/').replace('src="img/','src="../img/'))
    return slug
S=[]
# 01 Services grid
S.append(mod(1,'Services grid','''<section class="m"><div class="g12" style="align-items:end">
<div style="grid-column:1/8"><div class="eyebrow">Services</div><h2 class="d" style="margin-top:20px">Six services.<br><span style="color:var(--navy)">One accountable team.</span></h2></div>
<p class="lead" style="grid-column:8/13">Strategy, marketing, design and development under one roof, so enterprise teams never manage a hand-off between shops.</p></div>
<div class="sg">
<div class="sc cut big"><span class="n">01</span><h3>Website development</h3><p>HubSpot CMS themes engineered to last, from briefing and competitor analysis to launch.</p><ul><li>HubSpot themes &amp; modules</li><li>HubSpot + Algolia search</li><li>WCAG 2.2 AA by default</li></ul><a class="tl" style="color:var(--ink);border-color:var(--ink)">Website development →</a></div>
<div class="sc cut"><span class="n">02</span><h3>CRM implementation &amp; migration</h3><p>Move to HubSpot without losing a contact, a deal or a workflow.</p><ul><li>Data mapping &amp; migration</li><li>Integration services</li></ul></div>
<div class="sc cut"><span class="n">03</span><h3>E-commerce &amp; integrations</h3><p>Storefronts, checkouts and the back-end systems they talk to.</p><ul><li>Commerce integrations</li><li>Backend systems work</li></ul></div>
<div class="sc cut"><span class="n">04</span><h3>Digital strategy &amp; ABM</h3><p>Identify the business challenge, prioritise by benefit and cost, then plan.</p><ul><li>Account-based marketing</li><li>Implementation plans</li></ul></div>
<div class="sc cut"><span class="n">05</span><h3>Marketing campaigns</h3><p>Inbound and outbound programmes, automated in HubSpot.</p><ul><li>Marketing automation</li><li>Inbound / outbound</li></ul></div>
<div class="sc cut nv" style="grid-column:span 2"><span class="n">06</span><h3>Bespoke process development</h3><p>When the off-the-shelf workflow doesn’t fit, we build the one that does.</p><a class="btn y" style="margin-top:auto;align-self:flex-start">Ask Walter about yours <span class="ar">→</span></a></div>
</div></section>''','''.sg{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:auto auto;gap:20px;margin-top:64px}
.sc{background:#fff;padding:30px 30px 34px;min-height:300px;display:flex;flex-direction:column;gap:12px;border-top:4px solid var(--navy)}
.sc .n{font-family:Bricolage;font-weight:700;font-size:15px;color:var(--slate)}
.sc p{font-size:15px;color:#33405c}
.sc ul{list-style:none;margin-top:6px;font-size:14px;font-weight:600}
.sc li{padding:7px 0;border-top:1px solid var(--line)}
.sc.big{grid-row:1/3;background:var(--sky);border-top:0;--cut:56px}
.sc.big h3{font-size:44px;margin-top:auto}.sc.big p{font-size:17px;color:var(--ink)}.sc.big .n{color:var(--ink)}.sc.big li{border-color:rgba(14,26,51,.25)}
.sc.nv{background:var(--navy);color:#fff;border-top:0}.sc.nv p,.sc.nv .n{color:#C9D6EC}
'''))
# 02 Process
steps=[('Brief','Walter','A conversation, not a form. Business challenge, audience, constraints, budget.','Transcribes, structures and drafts the brief','Walter agrees it with you'),
('Spec','You + us','Current &amp; competitor analysis, sitemap, scope. Signed off before anything is built.','Drafts the sitemap and audits competitors in hours','A strategist cuts it to what matters'),
('Design','Design','Wireframes, then design, built from a tested module library.','Generates layout and copy options','A designer chooses, edits, and owns it'),
('Build','HubSpot CMS','Themes, modules, CRM and commerce integrations.','Writes and tests code alongside engineers','An engineer reviews every line'),
('Launch','Run &amp; grow','QA, WCAG 2.2 AA, analytics, then campaigns and iteration.','Checks accessibility and regressions on every release','Walter reviews results with you')]
st=''.join(f'''<div class="st"><div class="h"><span>{i+1:02d}</span><b>{a}</b><em>{b}</em></div><p>{c}</p><div class="ai"><small>AI does</small>{d}</div><div class="hu"><small>People do</small>{e}</div></div>''' for i,(a,b,c,d,e) in enumerate(steps))
S.append(mod(2,'How we build',f'''<section class="m"><div class="g12" style="align-items:end"><div style="grid-column:1/9"><div class="eyebrow">How we build</div><h2 class="d" style="margin-top:20px">AI in every step.<br><span style="color:var(--navy)">A person signs off every step.</span></h2></div>
<p class="lead" style="grid-column:9/13">Speed comes from the machines. Accuracy and taste come from the people who decide what ships.</p></div>
<div class="ps">{st}</div>
<div class="legend"><span><i style="background:var(--sky)"></i>AI-accelerated</span><span><i style="background:var(--navy)"></i>Human decision</span><span style="margin-left:auto" class="mut">Example flow for a HubSpot website build. Sprints and retainers use the same five cuts.</span></div></section>''','''
.ps{display:grid;grid-template-columns:repeat(5,1fr);margin-top:64px;gap:14px}
.st{display:flex;flex-direction:column}
.st .h{background:var(--ink);color:#fff;padding:22px 22px 20px;clip-path:polygon(0 0,calc(100% - 22px) 0,100% 50%,calc(100% - 22px) 100%,0 100%,22px 50%);padding-left:40px;display:grid;grid-template-columns:auto 1fr;column-gap:10px}
.st:first-child .h{clip-path:polygon(0 0,calc(100% - 22px) 0,100% 50%,calc(100% - 22px) 100%,0 100%);padding-left:22px}
.st .h span{font-family:Bricolage;font-weight:700;color:var(--yel);font-size:14px;grid-row:1/3;padding-top:5px}
.st .h b{font-family:Bricolage;font-stretch:85%;font-size:24px;font-weight:700}
.st .h em{font-style:normal;font-size:13px;color:#A9B8D2}
.st p{font-size:14px;color:#33405c;padding:20px 6px 18px;min-height:112px}
.st .ai,.st .hu{font-size:14px;font-weight:600;padding:16px 18px;line-height:1.4}
.st .ai{background:var(--sky);color:var(--ink);clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,0 100%)}
.st .hu{background:var(--navy);color:#fff;margin-top:8px}
.st small{display:block;font-family:Bricolage;font-size:11px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;opacity:.8}
.legend{display:flex;gap:28px;margin-top:28px;font-size:14px;font-weight:600;align-items:center}
.legend i{display:inline-block;width:12px;height:12px;margin-right:8px;vertical-align:-1px}'''))
# 03 Tabs (Industries)
S.append(mod(3,'Tabs','''<section class="m"><div class="eyebrow">Who we build for</div><h2 class="d" style="margin-top:20px">Fluent in your industry.<br><span style="color:var(--navy)">Not limited by it.</span></h2>
<div class="tabs"><a class="on">Life sciences &amp; med device</a><a>Marketing agencies</a><a>Consumer</a><a>Non-profit</a><a>Enterprise B2B</a></div>
<div class="g12 panel"><div style="grid-column:1/6;padding-top:8px">
<h3 style="font-size:38px">Regulated, technical, and still easy to buy from.</h3>
<p class="lead" style="margin-top:18px;font-size:18px">Our founder spent years in life-science commercial operations, so we speak your buyers’ language. What we bring is the same thing every client gets: a fast, accurate HubSpot build.</p>
<div class="kv"><div><b>Indexing &amp; web search</b><span>HubSpot + Algolia for large product catalogues</span></div><div><b>Account-based marketing</b><span>For long, multi-stakeholder buying cycles</span></div><div><b>NDA-first process</b><span>Many of our clients can’t be named. That’s fine.</span></div></div>
<div style="display:flex;gap:26px;align-items:center;margin-top:34px"><a class="btn p">Talk to Walter <span class="ar">→</span></a><a class="tl">Life sciences in detail</a></div></div>
<div style="grid-column:7/13"><div class="cut" style="--cut:48px;height:520px;overflow:hidden"><img src="img/cut-acrylic.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="display:flex;justify-content:space-between;font-size:13px;color:var(--slate);margin-top:12px"><span>Tab 1 of 5. Industry pages share one template; imagery stays agency-framed, never lab stock.</span><span>Image: generated concept</span></div></div></div></section>''','''
.tabs{display:flex;margin-top:52px;border-bottom:2px solid var(--ink)}
.tabs a{padding:18px 26px;font-family:Bricolage;font-stretch:85%;font-size:20px;font-weight:650;color:var(--slate)}
.tabs a.on{background:var(--ink);color:#fff;clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,0 100%)}
.panel{margin-top:56px}
.kv{margin-top:28px;border-top:2px solid var(--ink)}
.kv div{display:grid;grid-template-columns:220px 1fr;padding:14px 0;border-bottom:1px solid var(--line);font-size:15px}
.kv span{color:var(--slate)}'''))
# 04 Media + text
S.append(mod(4,'Media + text','''<section class="m" style="padding-top:0;padding-left:0"><div class="g12" style="align-items:center;column-gap:0">
<div style="grid-column:1/8;position:relative"><div class="cut" style="--cut:64px;height:720px;overflow:hidden"><img src="img/studio-wall.jpg" style="width:100%;height:100%;object-fit:cover;object-position:60% 50%"></div>
<div class="cut" style="position:absolute;right:-40px;bottom:48px;background:var(--yel);padding:22px 26px;width:300px;--cut:18px"><b style="font-family:Bricolage;font-stretch:85%;font-size:22px">One table.</b><p style="font-size:14px">Strategy, design and engineering in the same review, every week.</p></div></div>
<div style="grid-column:9/13;padding-top:88px"><div class="eyebrow">Website development</div>
<h2 class="d" style="font-size:64px;margin-top:20px">Built on HubSpot.<br><span style="color:var(--navy)">Cut to fit.</span></h2>
<p class="lead" style="margin-top:22px;font-size:18px">From the first brief to launch, one team carries the work through analysis, scope, design and build, so nothing is lost in a hand-off.</p>
<ol class="ol"><li><span>01</span>Briefing</li><li><span>02</span>Current &amp; competitor analysis</li><li><span>03</span>Define project scope</li><li><span>04</span>Sitemap, wireframes, design</li><li><span>05</span>Develop on HubSpot CMS</li></ol>
<div style="display:flex;gap:26px;align-items:center;margin-top:32px"><a class="btn p">Start with a brief <span class="ar">→</span></a><a class="tl">See our work</a></div>
<p style="font-size:12px;color:var(--slate);margin-top:22px">Photo: generated placeholder. Replace with a real studio session.</p></div></div></section>''','''
.ol{list-style:none;margin-top:26px;border-top:2px solid var(--ink)}
.ol li{display:flex;gap:18px;padding:12px 0;border-bottom:1px solid var(--line);font-weight:600;font-size:16px}
.ol span{font-family:Bricolage;color:var(--sky);font-weight:700;width:22px;-webkit-text-stroke:.3px var(--navy);color:var(--navy)}'''))
# 05 Case study
S.append(mod(5,'Case study','''<section class="m"><div class="cs">
<div class="l cut"><div class="eyebrow" style="color:var(--yel)">Case study · E-commerce</div>
<h2 class="d" style="font-size:72px;color:#fff;margin-top:22px">Blip: commerce wired into the CRM.</h2>
<p style="color:#C9D6EC;font-size:18px;margin-top:20px">A complex e-commerce integration, so orders, customers and marketing live in one system instead of three.</p>
<div class="tags"><span>HubSpot theme</span><span>E-commerce integration</span><span>Backend systems</span></div>
<a class="btn y" style="margin-top:40px;align-self:flex-start">Read the case <span class="ar">→</span></a></div>
<div class="r"><div class="mt"><div class="metric"><b>—%</b><span>Checkout conversion</span><em>Pending client sign-off</em></div>
<div class="metric"><b>— wk</b><span>Brief to launch</span><em>Pending client sign-off</em></div>
<div class="metric"><b>—</b><span>Systems unified</span><em>Pending client sign-off</em></div></div>
<blockquote>“…complex e-commerce integration at Blip, and deep backend systems work at Kean…”<cite>Client testimonial, June 2025 · name pending approval</cite></blockquote>
<div style="font-size:12px;font-weight:700;background:var(--yel);padding:6px 10px;align-self:flex-start">Sample case copy: real problem / system / output and metrics from Walter before publishing</div><div class="spec2"><div><small>Problem</small>Commerce data lived outside marketing.</div><div><small>System</small>HubSpot CMS + commerce integration</div><div><small>Output</small>One record per customer</div></div></div>
</div></section>''','''
.cs{display:grid;grid-template-columns:1.05fr 1fr;gap:20px}
.cs .l{background:var(--navy);padding:56px;--cut:64px;min-height:640px;display:flex;flex-direction:column}
.cs .l .eyebrow:before{background:var(--yel)}
.tags{display:flex;gap:10px;margin-top:auto;flex-wrap:wrap}
.tags span{font-size:13px;font-weight:600;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.4);padding:7px 12px}
.cs .r{display:flex;flex-direction:column;gap:20px}
.mt{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.metric{background:var(--sky);padding:26px 22px;min-height:220px;display:flex;flex-direction:column;clip-path:polygon(0 0,calc(100% - 22px) 0,100% 22px,100% 100%,0 100%)}
.metric b{white-space:nowrap;font-family:Bricolage;font-stretch:78%;font-size:64px;font-weight:700;line-height:1;letter-spacing:-.03em}
.metric span{font-weight:600;margin-top:auto}.metric em{font-style:normal;font-size:12px;opacity:.8}
blockquote{background:#fff;padding:34px;font-family:Bricolage;font-stretch:85%;font-size:28px;line-height:1.2;font-weight:600;border-left:6px solid var(--yel)}
cite{display:block;font-family:Instrument;font-style:normal;font-size:13px;color:var(--slate);font-weight:500;margin-top:16px}
.spec2{display:grid;grid-template-columns:repeat(3,1fr);background:var(--frost)}
.spec2 div{padding:20px 22px;font-weight:600;font-size:15px;border-right:1px solid #fff}
.spec2 small{display:block;font-family:Bricolage;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--slate);margin-bottom:6px}'''))
# 06 Meet Walter
S.append(mod(6,'Meet Walter','''<section class="m"><div class="g12" style="align-items:stretch">
<div style="grid-column:1/6;position:relative"><div class="ph cut" style="--cut:56px;height:640px;background:var(--frost);flex-direction:column;gap:10px">'''+symbol(size=120,cut=0.9)+'''<span>Portrait of Walter Lentfert<br>to be photographed (none on file)</span></div>
<div style="position:absolute;left:0;bottom:0;background:var(--yel);padding:14px 20px;font-weight:600;font-size:14px">Founder &amp; President · since 2008</div></div>
<div style="grid-column:7/13;display:flex;flex-direction:column"><div class="eyebrow">Your point of contact</div>
<h2 class="d" style="margin-top:20px">You’ll talk to Walter.<br><span style="color:var(--navy)">Not a sales queue.</span></h2>
<p class="lead" style="margin-top:24px">Walter Lentfert founded Razor Profiles in 2008. He has spent 30+ years in strategy, marketing, sales and execution, from commercial operations at GE Healthcare to leading HubSpot implementation work in the US. He scopes every engagement himself and stays on it until launch.</p>
<div class="facts"><div><b>2008</b><span>Founded, Wilmington, NC</span></div><div><b>30+</b><span>Years in strategy &amp; marketing</span></div><div><b>EN · NL</b><span>English &amp; Nederlands</span></div><div><b>1</b><span>Point of contact, brief to launch</span></div></div>
<div style="display:flex;gap:26px;align-items:center;margin-top:auto"><a class="btn p">Book 30 minutes with Walter <span class="ar">→</span></a><a class="tl">Email Walter</a></div></div></div></section>''','''
.facts{display:grid;grid-template-columns:repeat(4,1fr);margin:36px 0 40px;border-top:2px solid var(--ink)}
.facts div{padding:18px 16px 0 0}
.facts b{font-family:Bricolage;font-stretch:78%;font-size:44px;font-weight:700;display:block;line-height:1;color:var(--navy)}
.facts span{font-size:14px;color:var(--slate);display:block;margin-top:8px}'''))
# 07 Quote
S.append(mod(7,'Testimonial','''<section style="background:var(--sky);padding:96px 96px 104px;position:relative;overflow:hidden">
<div style="position:absolute;right:-180px;top:-150px;opacity:1">'''+symbol(size=640,top='#5BC0EA',lobe='#5BC0EA',bottom='#5BC0EA')+'''</div>
<div class="g12" style="position:relative"><div style="grid-column:1/11"><div class="eyebrow" style="color:var(--ink)"><style>.eyebrow:before{background:var(--ink)}.spec{color:var(--ink);border-color:rgba(14,26,51,.25)}</style>What clients say</div>
<p class="d" style="font-size:64px;line-height:1.02;margin-top:28px;letter-spacing:-.02em">“Walter and team have been my go-to for all things HubSpot and web development across multiple companies. […] He delivers not just code, but <span style="background:var(--yel);padding:0 .1em">confidence</span>.”</p>
<div style="display:flex;gap:18px;align-items:center;margin-top:40px"><div style="width:56px;height:56px;background:var(--navy)" class="cut"></div><div><b style="font-size:17px">Client name &amp; title pending approval</b><div style="font-size:15px">Worked with Razor Profiles at Psomagen, 9amHealth, Kean and Blip</div></div>
<div style="margin-left:auto;display:flex;gap:10px"><a class="nb">←</a><a class="nb on">→</a></div></div></div></div>
<div class="dots"><i class="on"></i><i></i><i></i><span>1 / 2 real quotes on file · 5 more expected</span></div></section>''','''
.nb{width:56px;height:56px;display:flex;align-items:center;justify-content:center;font-family:Bricolage;font-size:24px;box-shadow:inset 0 0 0 2px var(--ink)}
.nb.on{background:var(--ink);color:#fff}
.dots{display:flex;gap:8px;align-items:center;margin-top:48px;position:relative}
.dots i{width:40px;height:4px;background:rgba(14,26,51,.3)}.dots i.on{background:var(--ink)}
.dots span{margin-left:16px;font-size:13px;font-weight:600}''',bg='var(--sky)'))
# 08 Engagement
S.append(mod(8,'Engagement models','''<section class="m"><div class="g12" style="align-items:end"><div style="grid-column:1/8"><div class="eyebrow">Ways to work with us</div><h2 class="d" style="margin-top:20px">Three ways in.<br><span style="color:var(--navy)">Same team either way.</span></h2></div>
<p class="lead" style="grid-column:8/13">Every engagement starts with a 30-minute call with Walter and a written scope. No surprises after that.</p></div>
<div class="eg">
<div class="ec cut"><small>Sprint</small><h3>Fix one thing, fast.</h3><p>A single module, a migration audit, an ABM plan. Fixed scope, fixed fee.</p><div class="pr"><b>2–4</b> weeks</div><ul><li>Written scope in 48 hours</li><li>One senior lead</li><li>AI-accelerated QA</li></ul><a class="btn s">Scope a sprint</a></div>
<div class="ec cut hi"><span class="flag">Recommended</span><small>Build</small><h3>A site, CRM or store, end to end.</h3><p>Strategy, design and development as one project, launched on HubSpot.</p><div class="pr"><b>From $5k</b> budget</div><ul><li>Brief → spec → design → build</li><li>WCAG 2.2 AA and QA included</li><li>Walter as your point of contact</li></ul><a class="btn y">Talk to Walter <span class="ar">→</span></a></div>
<div class="ec cut"><small>Partner</small><h3>An extension of your team.</h3><p>Monthly capacity for campaigns, CRM operations and continuous improvement.</p><div class="pr"><b>Monthly</b> retainer</div><ul><li>Reserved team hours</li><li>Quarterly roadmap with Walter</li><li>White-label for agencies</li></ul><a class="btn s">Plan a partnership</a></div></div>
<p style="font-size:13px;color:var(--slate);margin-top:20px">“From $5k” reflects the budget floor on Razor’s HubSpot Solutions Directory listing; confirm before publishing.</p></section>''','''
.eg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:60px;align-items:stretch}
.ec{background:#fff;padding:40px 36px;display:flex;flex-direction:column;gap:14px;position:relative;--cut:36px}
.ec small{font-family:Bricolage;font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--navy)}
.ec h3{font-size:34px}.ec p{font-size:15px;color:#33405c}
.ec .pr{font-size:15px;color:var(--slate);border-top:2px solid var(--ink);padding-top:16px;margin-top:6px}
.ec .pr b{font-family:Bricolage;font-stretch:78%;font-size:48px;color:var(--ink);margin-right:6px;letter-spacing:-.02em}
.ec ul{list-style:none;font-size:15px;font-weight:600;margin-bottom:18px}.ec li{padding:9px 0;border-bottom:1px solid var(--line)}
.ec li:before{content:"";display:inline-block;width:9px;height:9px;background:var(--sky);margin-right:12px;clip-path:polygon(0 0,55% 0,100% 45%,100% 100%,0 100%)}
.ec .btn{margin-top:auto;align-self:flex-start}
.ec.hi{background:var(--navy);color:#fff}.ec.hi small{color:var(--yel)}.ec.hi p,.ec.hi .pr{color:#C9D6EC}.ec.hi .pr{border-color:#fff}.ec.hi .pr b{color:#fff}.ec.hi li{border-color:rgba(255,255,255,.2)}
.flag{position:absolute;right:56px;top:40px;font-size:12px;font-weight:700;background:var(--yel);color:var(--ink);padding:4px 10px}'''))
# 09 FAQ accordion
qa=[('How do you actually use AI?','In every step, from structuring the brief and auditing competitors to generating layout options, writing code and running accessibility checks. What AI never does is decide. A named person reviews and signs off every deliverable, which is how we stay fast without getting sloppy.',True),
('Who will I work with?','Walter scopes the work and stays your point of contact. Senior strategists, designers and HubSpot engineers do the work; no juniors learning on your account.',False),
('Do you work under NDA?','Yes, routinely. Many of our clients can’t be named publicly, and our process assumes confidentiality from the first call.',False),
('Can you migrate our CRM to HubSpot?','Yes. CRM implementation and migration, with integration services for the systems around it.',False),
('Is Razor Profiles only for life sciences?','No. Life sciences and med device are a large share of our clients, alongside marketing agencies, consumer and non-profit work.',False)]
acc=''.join(f'<div class="q {"on" if o else ""}"><div class="qh"><span>{i+1:02d}</span><b>{q}</b><i>{"−" if o else "+"}</i></div>{f"<p>{a}</p>" if o else ""}</div>' for i,(q,a,o) in enumerate(qa))
S.append(mod(9,'FAQ accordion',f'''<section class="m"><div class="g12"><div style="grid-column:1/5"><div class="eyebrow">Straight answers</div><h2 class="d" style="margin-top:20px;font-size:68px">Questions enterprise teams ask first.</h2>
<p class="mut" style="margin-top:22px">Something else? Walter answers these himself.</p><a class="btn p" style="margin-top:28px">Ask Walter <span class="ar">→</span></a></div>
<div style="grid-column:6/13">{acc}</div></div></section>''','''
.q{border-top:2px solid var(--ink)}.q:last-child{border-bottom:2px solid var(--ink)}
.qh{display:grid;grid-template-columns:56px 1fr 56px;align-items:center;padding:24px 0}
.qh span{font-family:Bricolage;font-weight:700;color:var(--slate)}
.qh b{font-family:Bricolage;font-stretch:85%;font-size:28px;font-weight:650;letter-spacing:-.01em}
.qh i{font-style:normal;width:44px;height:44px;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:inset 0 0 0 2px var(--ink);justify-self:end}
.q.on{background:#fff}.q.on .qh{padding-left:16px;padding-right:16px}.q.on p{padding-left:72px}.q.on .qh i{background:var(--yel);box-shadow:none}
.q p{padding:0 56px 30px;font-size:17px;color:#33405c;max-width:780px}'''))
# 10 CTA + footer
S.append(mod(10,'CTA + footer','''<section class="cta"><div class="mk">'''+symbol(size=760,bottom='#F7F9FC')+'''</div>
<div style="position:relative;width:820px"><div class="eyebrow" style="color:var(--yel)">Let’s talk</div>
<h2 class="d" style="font-size:150px;color:#fff;margin-top:22px">Talk to<br>Walter.</h2>
<p style="color:#C9D6EC;font-size:20px;margin-top:24px;width:600px">Bring the business challenge. You’ll leave the first call with a straight answer on scope, timing and whether we’re the right fit.</p>
<div style="display:flex;gap:28px;align-items:center;margin-top:40px"><a class="btn y">Book 30 minutes <span class="ar">→</span></a><span style="color:#fff;font-weight:600;border-bottom:2px solid var(--yel)">walter.lentfert@razorprofiles.com</span></div></div></section>
<footer><div class="fr">'''+lockup(height=36,word='#F7F9FC',bottom='#F7F9FC')+'''<nav><a>Services</a><a>Industries</a><a>HubSpot</a><a>Partnerships</a><a>About</a><a>Contact</a></nav></div>
<div class="fr2"><span>© 2008–2026 Razor Profiles LLC · Wilmington, NC</span><span>English &amp; Nederlands</span><span style="margin-left:auto">Privacy</span><span>Terms</span><span>Accessibility: WCAG 2.2 AA</span></div></footer>''','''
.cta{background:var(--navy);padding:120px 96px 130px;position:relative;overflow:hidden}
.cta .eyebrow:before{background:var(--yel)}
.cta .mk{position:absolute;right:-120px;top:60px}
footer{background:var(--ink);color:#fff;padding:44px 96px 36px}
.fr{display:flex;align-items:center}.fr nav{margin-left:auto;display:flex;gap:34px;font-weight:600;font-size:15px}
.fr2{display:flex;gap:28px;font-size:13px;color:#A9B8D2;margin-top:36px;padding-top:22px;border-top:1px solid rgba(255,255,255,.15)}''',bg='var(--ink)'))
print(' '.join(f'modules/{s}.html' for s in S))
