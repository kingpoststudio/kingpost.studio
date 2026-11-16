HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500&family=Inter:wght@400;500&family=Geist+Mono:wght@400;500&display=block" rel="stylesheet">
<link rel="stylesheet" href="base.css"><script src="mob.js"></script><style>%s</style></head><body><div class="sheet">
<div class="spec mono"><span><b>Razor Profiles</b> · Direction A — Cross-Section</span><span class="r">Module %s / 10 — <b>%s</b></span></div>
<div class="wrap"><div class="cols"></div>
<span class="tk" style="left:40px;top:28px"></span><span class="tk" style="right:40px;top:28px"></span><span class="tk" style="left:40px;bottom:28px"></span><span class="tk" style="right:40px;bottom:28px"></span>
%s
</div></div><script>%s
document.fonts.ready.then(()=>{document.title='H'+document.documentElement.scrollHeight;});</script></body></html>'''
M={}
NAV='''<header style="height:76px;display:flex;align-items:center;border-bottom:1px solid var(--rule);margin:-72px -128px 0;padding:0 128px;background:var(--paper);position:relative">
<img src="rp-left-dark.svg" style="height:34px"><nav style="display:flex;align-items:center;height:76px;gap:40px;margin-left:auto;margin-right:40px;font-size:15px;font-weight:500"><a>Capabilities ▾</a><a>Work ▾</a><a>Approach</a><a>About</a><a style="color:var(--deep);box-shadow:inset 0 -2px 0 var(--deep);padding:28px 0 26px">Insights</a></nav>
<a class="btn b1" style="height:44px;font-size:14px;padding:0 18px"><i></i>Talk to Walter</a></header>'''

# 01 Tabs
M['01-tabs']=('Tabs','''
.tabs{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--ink);border-bottom:1px solid var(--rule);margin-top:48px}
.tab{padding:20px 0 18px;display:flex;gap:16px;align-items:baseline;border-right:1px solid var(--rule);padding-left:20px;position:relative}
.tab:first-child{padding-left:0}
.tab .t{font-family:'Inter Tight';font-size:22px;font-weight:500;color:var(--mute)}
.tab.on .t{color:var(--ink)}
.tab.on:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:3px;background:var(--ink)}
.tab.on .sq{width:8px;height:8px;background:var(--yel);outline:1px solid var(--ink);display:inline-block;margin-left:auto;margin-right:20px}
''','''
<div class="g"><div style="grid-column:1/8"><div class="lab mono">02 — Capabilities</div><h2>Four disciplines, <span>one surface.</span></h2></div>
<div style="grid-column:9/13;align-self:end"><p class="small">Select a discipline to see what it covers and how it connects to the other three.</p></div></div>
<div class="tabs" role="tablist">
<div class="tab on"><span class="mono" style="color:var(--deep)">01</span><span class="t">Strategy</span><span class="sq"></span></div>
<div class="tab"><span class="mono" style="color:var(--mute2)">02</span><span class="t">Marketing</span></div>
<div class="tab"><span class="mono" style="color:var(--mute2)">03</span><span class="t">Design</span></div>
<div class="tab"><span class="mono" style="color:var(--mute2)">04</span><span class="t">Development</span></div></div>
<div class="g" style="margin-top:48px">
<div style="grid-column:1/6">
<div class="mono" style="color:var(--mute);margin-bottom:14px">Panel 01 / 04 — Strategy</div>
<h3 style="font-size:30px;line-height:1.15">Define the challenge before anyone draws a page.</h3>
<p style="margin-top:18px">Digital strategy and account-based planning, built around the business problem rather than the channel.</p>
<div class="rule-top" style="margin-top:28px">
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">A</span><span>Identify the business challenge(s)</span></div>
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">B</span><span>Prioritize by benefit to the organization and cost</span></div>
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">C</span><span>Agree an implementation plan</span></div>
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">D</span><span>Account-based marketing strategy</span></div></div>
<div style="margin-top:30px;display:flex;gap:28px;align-items:center"><a class="btn b1"><i></i>Talk to Walter</a><a class="tl">Strategy in detail →</a></div>
</div>
<div style="grid-column:7/13"><div class="frame" style="height:470px;border-color:var(--rule)"><svg id="m" width="100%" height="470" viewBox="0 0 648 470"></svg>
<span class="mono" style="position:absolute;right:16px;top:14px;color:var(--mute)">Section B-B</span></div>
<div class="cap mono"><span>Fig. 02 — Strategy quarter of the surface</span><span>Scale 1:1</span></div></div></div>''',
"mob(document.getElementById('m'),{R:190,W:64,cx:324,cy:240,hi:[.06,.31],mark:{u:.19,off:22,t:'01 STRATEGY'}});")

# 02 Media + text
M['02-media-text']=('Media + text','''''','''
<div class="g" style="align-items:start">
<div style="grid-column:1/8"><div class="frame"><img src="d-media.png" style="width:772px"><span class="tk" style="left:-8px;top:-8px"></span><span class="tk" style="right:-8px;bottom:-8px"></span></div>
<div class="cap mono"><span>Fig. 03 — Placeholder screen capture, dithered</span><span>Replace with approved client work</span></div></div>
<div style="grid-column:9/13;padding-top:8px"><div class="lab mono">03 — Website development</div>
<h2 style="font-size:42px">Built on HubSpot, <span>engineered to last.</span></h2>
<p style="margin-top:22px">From the first brief to launch, one team carries the work through analysis, scope, design and build, so nothing is lost in a hand-off.</p>
<div class="rule-top" style="margin-top:28px">
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">Process</span><span>Briefing → current &amp; competitor analysis → scope → sitemap, wireframes, design → develop</span></div>
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">Platform</span><span>HubSpot CMS themes</span></div>
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">Search</span><span>HubSpot–Algolia search</span></div>
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">Access</span><span>WCAG 2.2 AA as the target</span></div></div>
<div style="margin-top:30px"><a class="tl">See how an engagement runs →</a></div></div></div>''','')

# 03 Buttons
M['03-buttons']=('Buttons + links','''
.tbl{display:grid;grid-template-columns:200px repeat(4,1fr);border-top:1px solid var(--ink)}
.tbl>div{border-bottom:1px solid var(--rule);padding:22px 0;display:flex;align-items:center;min-height:96px}
.tbl .h{min-height:auto;padding:12px 0;color:var(--mute)}
.focus{outline:2px solid var(--deep);outline-offset:3px}
.dis{background:#DCD9D2!important;color:#7d8191!important;border-color:#DCD9D2!important}
.dis i{background:#b9b6ae!important}
.ico{width:52px;height:52px;border:1px solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:18px}
.darkband{margin:64px -128px -96px;padding:56px 128px 64px;background:var(--ink);color:var(--paper);position:relative}
.darkband .tbl{border-top-color:rgba(241,239,234,.5)}
.darkband .tbl>div{border-bottom-color:rgba(241,239,234,.14)}
.darkband .h,.darkband .rl{color:rgba(241,239,234,.6)}
.dk1{background:var(--paper);color:var(--ink)}.dk1 i{width:8px;height:8px;background:var(--yel);display:block;outline:1px solid var(--ink)}
.dk2{border:1px solid var(--paper);color:var(--paper)}
.dk3{color:var(--sky);padding:0;height:auto}
.dkl{color:var(--sky);border-bottom:1px solid var(--sky);padding-bottom:3px;font-weight:500;font-size:15px}
.dfocus{outline:2px solid var(--sky);outline-offset:3px}
.ddis{background:#2a2e40!important;color:#7b8096!important;border-color:#2a2e40!important}
.dico{width:52px;height:52px;border:1px solid var(--paper);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--paper)}
.note{color:var(--mute);margin-top:18px}
''','''
<div class="g"><div style="grid-column:1/8"><div class="lab mono">Component sheet — Actions</div><h2>Buttons and links</h2></div>
<div style="grid-column:9/13;align-self:end"><p class="small">Every state at 1:1. Focus rings are 2px with a 3px offset and pass 3:1 against the surface.</p></div></div>
<div class="tbl" style="margin-top:44px">
<div class="h mono">On paper</div><div class="h mono">Default</div><div class="h mono">Hover</div><div class="h mono">Focus (visible)</div><div class="h mono">Disabled</div>
<div class="mono rl" style="color:var(--mute)">Primary</div>
<div><a class="btn b1"><i></i>Talk to Walter</a></div><div><a class="btn b1" style="background:var(--deep)"><i></i>Talk to Walter</a></div><div><a class="btn b1 focus"><i></i>Talk to Walter</a></div><div><a class="btn b1 dis"><i></i>Talk to Walter</a></div>
<div class="mono rl" style="color:var(--mute)">Secondary</div>
<div><a class="btn b2">See our approach</a></div><div><a class="btn b2" style="background:rgba(19,22,38,.06)">See our approach</a></div><div><a class="btn b2 focus">See our approach</a></div><div><a class="btn b2 dis">See our approach</a></div>
<div class="mono rl" style="color:var(--mute)">Tertiary</div>
<div><a class="btn b3">Read more →</a></div><div><a class="btn b3" style="text-decoration:underline;text-underline-offset:5px">Read more &nbsp;→</a></div><div><a class="btn b3 focus">Read more →</a></div><div><a class="btn b3" style="color:#8a8e9c">Read more →</a></div>
<div class="mono rl" style="color:var(--mute)">Icon</div>
<div><a class="ico">→</a></div><div><a class="ico" style="background:var(--ink);color:var(--paper)">→</a></div><div><a class="ico focus">→</a></div><div><a class="ico" style="border-color:#c5c2bb;color:#a3a6b2">→</a></div>
<div class="mono rl" style="color:var(--mute)">Text link</div>
<div><a class="tl">Website development</a></div><div><a class="tl" style="border-bottom-width:2px;color:var(--ink);border-color:var(--ink)">Website development</a></div><div><a class="tl focus">Website development</a></div><div><a class="tl" style="color:#8a8e9c;border-color:#c5c2bb">Website development</a></div>
</div>
<div class="note mono">Fig. 04 — Yellow is a marker only, never text. Disabled states are exempt from contrast minimums but never carry meaning alone.</div>
<div class="darkband"><span class="tk" style="left:40px;top:24px;filter:invert(1)"></span><span class="tk" style="right:40px;top:24px;filter:invert(1)"></span>
<div class="tbl">
<div class="h mono">On dark band</div><div class="h mono">Default</div><div class="h mono">Hover</div><div class="h mono">Focus (visible)</div><div class="h mono">Disabled</div>
<div class="mono rl">Primary</div>
<div><a class="btn dk1"><i></i>Talk to Walter</a></div><div><a class="btn dk1" style="background:#fff"><i></i>Talk to Walter</a></div><div><a class="btn dk1 dfocus"><i></i>Talk to Walter</a></div><div><a class="btn dk1 ddis"><i style="background:#555a6e;outline:none"></i>Talk to Walter</a></div>
<div class="mono rl">Secondary</div>
<div><a class="btn dk2">See our approach</a></div><div><a class="btn dk2" style="background:rgba(241,239,234,.1)">See our approach</a></div><div><a class="btn dk2 dfocus">See our approach</a></div><div><a class="btn dk2 ddis">See our approach</a></div>
<div class="mono rl">Tertiary</div>
<div><a class="btn dk3">Read more →</a></div><div><a class="btn dk3" style="text-decoration:underline;text-underline-offset:5px">Read more &nbsp;→</a></div><div><a class="btn dk3 dfocus">Read more →</a></div><div><a class="btn dk3" style="color:#5f647a">Read more →</a></div>
<div class="mono rl">Icon</div>
<div><a class="dico">→</a></div><div><a class="dico" style="background:var(--paper);color:var(--ink)">→</a></div><div><a class="dico dfocus">→</a></div><div><a class="dico" style="border-color:#3a3f54;color:#5f647a">→</a></div>
<div class="mono rl">Text link</div>
<div><a class="dkl">Website development</a></div><div><a class="dkl" style="color:var(--paper);border-color:var(--paper);border-bottom-width:2px">Website development</a></div><div><a class="dkl dfocus">Website development</a></div><div><a class="dkl" style="color:#5f647a;border-color:#3a3f54">Website development</a></div>
</div><div class="mono" style="margin-top:18px;color:rgba(241,239,234,.6)">Fig. 05 — Sky #28ABE2 appears only on dark surfaces (6.9:1 on ink).</div></div>''','')

# 04 Accordion
M['04-accordion']=('Accordion','''
.acc{border-top:1px solid var(--ink)}
.it{border-bottom:1px solid var(--rule);display:grid;grid-template-columns:64px 1fr 40px;align-items:center;padding:22px 0}
.it .t{font-family:'Inter Tight';font-size:24px;font-weight:500}
.pm{width:28px;height:28px;border:1px solid var(--ink);position:relative;justify-self:end}
.pm:before,.pm:after{content:"";position:absolute;background:var(--ink);left:7px;right:7px;top:13px;height:1px}
.pm.plus:after{transform:rotate(90deg)}
.open{background:var(--card);margin:0 -24px;padding:22px 24px;border-bottom:1px solid var(--ink)}
.open .t{color:var(--ink)}
.body{grid-column:2/3;padding-top:16px}
''','''
<div class="g">
<div style="grid-column:1/5"><div class="lab mono">04 — How we engage</div><h2 style="font-size:44px">From brief to run,<br><span>no hand-offs.</span></h2>
<p class="small" style="margin-top:20px">The same team stays on the work from the first conversation through launch and after it.</p>
<div style="margin-top:36px;position:relative"><svg id="m" width="100%" height="250" viewBox="0 0 420 250"></svg><div class="cap mono"><span>Fig. 06 — Step 01 of 04</span></div></div></div>
<div style="grid-column:6/13" class="acc">
<div class="it open"><span class="mono" style="color:var(--deep)">01</span><span class="t">Discover</span><span class="pm"></span>
<div class="body"><p>We start with the business challenge, not the deliverable. Together we name the problem, rank options by benefit and cost, and agree what success looks like before scope is written.</p>
<div class="rule-top" style="margin-top:22px">
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">You get</span><span>A written brief and an agreed scope</span></div>
<div class="row small" style="grid-template-columns:120px 1fr"><span class="mono" style="color:var(--mute2)">Who</span><span>Walter Lentfert with the delivery team</span></div></div>
<div style="margin-top:20px"><a class="tl">Talk to Walter about discovery →</a></div></div></div>
<div class="it"><span class="mono" style="color:var(--mute2)">02</span><span class="t">Plan</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">03</span><span class="t">Build</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">04</span><span class="t">Run</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">FAQ</span><span class="t">Do you work alongside in-house teams?</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">FAQ</span><span class="t">Can you work under NDA?</span><span class="pm plus"></span></div>
</div></div>''',"mob(document.getElementById('m'),{R:120,W:40,cx:205,cy:125,hi:[.06,.31],mark:{u:.19,off:16}});")

# 05 Carousel
SL=lambda n,img,tag,t: f'''<div class="sl"><div class="frame"><img src="{img}" style="width:430px"></div><div class="mono" style="color:var(--mute);margin-top:16px;display:flex;justify-content:space-between"><span>{tag}</span><span>{n}</span></div><h3 style="margin-top:10px;font-size:24px;line-height:1.2">{t}</h3><a class="tl" style="display:inline-block;margin-top:16px">Read →</a></div>'''
M['05-carousel']=('Carousel','''
.track{display:flex;gap:24px;margin-top:44px;margin-right:-128px;overflow:hidden}
.sl{flex:0 0 432px}
.arrows{display:flex;gap:12px}
.ar{width:52px;height:52px;border:1px solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:18px}
.prog{height:1px;background:var(--rule);margin-top:40px;position:relative}
.prog i{position:absolute;left:0;top:-1px;height:3px;width:16.66%;background:var(--ink)}
''','''
<div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">05 — Insights</div><h2>Notes from the work</h2></div>
<div style="grid-column:9/13;display:flex;align-items:center;justify-content:flex-end;gap:28px"><span class="mono" style="color:var(--mute)"><b style="color:var(--ink)">01</b> / 06</span>
<div class="arrows"><a class="ar" style="border-color:#c5c2bb;color:#a3a6b2">←</a><a class="ar" style="background:var(--ink);color:var(--paper)">→</a></div></div></div>
<div class="track">'''+SL('01','d-c1.png','Strategy · Article','Why one office beats a roster of vendors')+SL('02','d-c2.png','Development · Guide','Planning a HubSpot CRM migration without losing history')+SL('03','d-c3.png','Marketing · Article','Account-based marketing for life-sciences teams')+SL('04','d-c4.png','Design · Note','What WCAG 2.2 changes for enterprise sites')+'''</div>
<div class="prog"><i></i></div>
<div class="cap mono"><span>Fig. 07 — Progress rule, slide 1 of 6. Images are dithered placeholders.</span><span>Swipe or use arrows</span></div>''','')

# 06 Cards
CARD=lambda n,t,d,items,hu,hov: f'''<div class="cd{' hov' if hov else ''}"><div style="display:flex;justify-content:space-between"><span class="mono" style="color:var(--deep)">{n}</span>{'<span class="sq"></span>' if hov else ''}</div>
<svg class="cm" id="c{n}" width="100%" height="170" viewBox="0 0 384 170"></svg>
<h3 style="font-size:28px">{t}</h3><p class="small" style="margin-top:10px">{d}</p>
<div class="rule-top" style="margin-top:20px">{''.join(f'<div class="row small" style="padding:9px 0">{i}</div>' for i in items)}</div>
<a class="tl" style="display:inline-block;margin-top:22px">{t} {'&nbsp;&nbsp;→' if hov else '→'}</a></div>'''
M['06-cards']=('Cards','''
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px}
.cd{border:1px solid var(--rule);border-top:1px solid var(--ink);padding:28px 28px 32px;background:var(--paper);position:relative}
.cd.hov{background:var(--card);border-color:var(--ink);border-top:3px solid var(--ink);transform:translateY(-6px);box-shadow:0 6px 0 rgba(19,22,38,.08)}
.sq{width:10px;height:10px;background:var(--yel);outline:1px solid var(--ink)}
.callout{position:absolute;top:-36px;left:50%;color:var(--deep);display:flex;align-items:center;gap:10px}
.callout:before{content:"";width:1px;height:26px;background:var(--deep);position:absolute;left:-8px;top:10px}
''','''
<div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">06 — Capabilities</div><h2>Pick a starting point</h2></div>
<div style="grid-column:9/13"><p class="small">Every card leads into the same team. Start with the discipline closest to your problem.</p></div></div>
<div class="cards" style="position:relative">
'''+CARD('01','Strategy','Digital strategy and account-based planning.',['Business challenge definition','Prioritization by benefit and cost','Implementation planning'],[.06,.31],False)+CARD('02','Marketing','Campaigns and automation tuned to the persona journey.',['Inbound and outbound campaigns','Account-based marketing','HubSpot marketing automation'],[.31,.56],True)+CARD('04','Development','HubSpot CMS, CRM and the integrations between them.',['HubSpot CMS themes','CRM implementation and migration','Bespoke process development'],[.81,1],False)+'''
<span class="callout mono" style="left:calc(33.33% + 40px)">Hover state — lift 6px, 3px ink cap, marker</span></div>
<div class="cap mono" style="margin-top:28px"><span>Fig. 08 — Card grid, 3-up (three of four disciplines). Each figure highlights its quarter.</span><span>Default · Hover · Default</span></div>''',
"[['c01',[.06,.31]],['c02',[.31,.56]],['c04',[.81,1]]].forEach(([id,h])=>mob(document.getElementById(id),{R:118,W:38,cx:192,cy:86,hi:h,n:140,tx:-1.1}));")

# 07 Bento
M['07-bento']=('Bento','''
.bento{display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:330px 300px;gap:24px;margin-top:44px}
.tile{border:1px solid var(--rule);border-top:1px solid var(--ink);padding:26px 28px;position:relative;background:var(--paper)}
''','''
<div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">07 — Proof</div><h2>One office, <span>shown in detail.</span></h2></div></div>
<div class="bento">
<div class="tile" style="grid-column:1/7;grid-row:1/3;padding:0"><svg id="m" width="100%" height="560" viewBox="0 0 648 560"></svg>
<span class="mono" style="position:absolute;left:28px;top:24px;color:var(--deep)">Fig. 09 — The full surface</span>
<span class="mono" style="position:absolute;left:28px;bottom:24px;color:var(--mute)">Strategy · Marketing · Design · Development</span></div>
<div class="tile" style="grid-column:7/10"><div class="mono" style="color:var(--mute)">Stat — placeholder</div>
<div class="ph" style="margin-top:22px;height:150px;display:flex;align-items:center;justify-content:center;font-family:'Inter Tight';font-size:64px;font-weight:300">—</div>
<p class="small" style="margin-top:16px">[Metric pending real data. Publish only a sourced, client-approved number.]</p></div>
<div class="tile dark" style="grid-column:10/13;border-color:var(--ink);background:var(--ink)"><div class="mono" style="color:var(--sky)">Direct line</div>
<h3 style="font-size:28px;margin-top:18px;color:var(--paper);line-height:1.15">Talk to Walter, not a sales queue.</h3>
<p class="small" style="margin-top:12px">Founder and President. Wilmington, NC.</p>
<a class="dkl" style="position:absolute;left:28px;bottom:28px;color:var(--sky);border-bottom:1px solid var(--sky);padding-bottom:3px;font-weight:500;font-size:15px">Book a call →</a></div>
<div class="tile" style="grid-column:7/13"><div style="display:flex;justify-content:space-between"><span class="mono" style="color:var(--mute)">Services index</span><span class="mono" style="color:var(--mute)">Est. 2008</span></div>
<div class="rule-top" style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;column-gap:24px">
<div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">01</span>Digital strategy</div><div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">04</span>Marketing campaigns</div>
<div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">02</span>Account-based marketing</div><div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">05</span>CRM implementation / migration</div>
<div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">03</span>Website development</div><div class="row small" style="grid-template-columns:40px 1fr"><span class="mono" style="color:var(--mute2)">06</span>Bespoke process development</div></div>
<p class="small" style="margin-top:18px">Focus: life sciences, medical devices, pharma and biotech.</p></div>
</div>''',"mob(document.getElementById('m'),{R:205,W:70,cx:330,cy:285,hi:[.06,.31],mark:{u:.19,off:22,t:'01 STRATEGY'}});")

# 08 Quote
M['08-quote']=('Quote','''
blockquote{font-family:'Inter Tight';font-weight:300;font-size:40px;line-height:1.22;letter-spacing:-.018em;color:var(--ink);text-indent:-.42em}
.qm{color:var(--deep);font-weight:400}
''','''
<div class="g">
<div style="grid-column:1/4"><div class="lab mono">08 — Client words</div>
<div style="position:relative;margin-top:28px"><svg id="m" width="100%" height="200" viewBox="0 0 312 200"></svg></div>
<div class="cap mono" style="margin-top:6px"><span>Fig. 10 — Testimonial 01 / 02</span></div></div>
<div style="grid-column:5/13">
<div style="width:56px;height:4px;background:var(--yel);outline:1px solid var(--ink);margin-bottom:34px"></div>
<blockquote><span class="qm">“</span>Walter and team have been my go-to for all things HubSpot and web development across multiple companies. From Psomagen to 9amHealth, his custom theme builds were clean, reliable, and built with scalability in mind. His work at Kean and BLIP also showed his strength in complex integrations — he delivers not just code, but confidence.<span class="qm">”</span></blockquote>
<div class="rule-top" style="margin-top:44px;display:grid;grid-template-columns:1fr auto;align-items:center;padding-top:18px">
<div><div style="font-weight:500">Client testimonial</div><div class="mono" style="color:var(--mute);margin-top:6px">Shared by Walter Lentfert, June 2025 · Name and title pending approval</div></div>
<div style="display:flex;gap:12px;align-items:center"><span class="mono" style="color:var(--mute);margin-right:12px"><b style="color:var(--ink)">01</b> / 02</span><a class="ico" style="width:52px;height:52px;border:1px solid #c5c2bb;color:#a3a6b2;display:flex;align-items:center;justify-content:center">←</a><a style="width:52px;height:52px;background:var(--ink);color:var(--paper);display:flex;align-items:center;justify-content:center">→</a></div></div>
</div></div>''',"mob(document.getElementById('m'),{R:95,W:32,cx:150,cy:100,n:120});")

# 09 Article
M['09-article']=('Article','''
.crumb{margin:0 -128px;padding:0 128px;height:46px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--rule);color:var(--mute)}
.crumb b{color:var(--deep);font-weight:500}
h1{font-family:'Inter Tight';font-weight:500;font-size:64px;line-height:1.02;letter-spacing:-.025em}
.body p{font-size:18px;line-height:1.7;margin-bottom:22px;color:#262b40}
.body sup{color:var(--deep);font-family:'Geist Mono';font-size:11px;font-weight:500}
.pq{border-left:4px solid var(--yel);padding:6px 0 6px 28px;margin:36px 0;font-family:'Inter Tight';font-size:32px;font-weight:300;line-height:1.25;letter-spacing:-.015em;color:var(--ink);box-shadow:-5px 0 0 -4px var(--ink)}
.mn{border-top:1px solid var(--ink);padding-top:12px;font-size:13px;line-height:1.55;color:#3d4258;margin-bottom:28px}
.mn .mono{color:var(--deep);display:block;margin-bottom:6px}
''',NAV+'''
<div class="crumb mono"><span>Home</span><span>/</span><span>Insights</span><span>/</span><b>Why one office beats a roster of vendors</b></div>
<div class="g" style="margin-top:56px">
<div style="grid-column:1/10"><div class="lab mono">Insights · Strategy</div>
<h1>Why one office beats a roster of vendors</h1>
<p style="font-size:21px;margin-top:22px;max-width:760px">Strategy, marketing, design and development fail at the seams between them. A single accountable team removes the seams.</p></div>
<div style="grid-column:10/13;align-self:end" class="rule-top">
<div class="row small" style="grid-template-columns:90px 1fr"><span class="mono" style="color:var(--mute2)">Author</span>Walter Lentfert</div>
<div class="row small" style="grid-template-columns:90px 1fr"><span class="mono" style="color:var(--mute2)">Reading</span>[x] min — placeholder</div>
<div class="row small" style="grid-template-columns:90px 1fr"><span class="mono" style="color:var(--mute2)">Filed</span>Strategy</div></div></div>
<div style="margin-top:44px"><div class="frame" style="height:440px;overflow:hidden"><img src="d-article.png" style="width:1342px;height:440px;object-fit:cover;object-position:50% 18%"></div>
<div class="cap mono"><span>Fig. 01 — Lead image, dithered placeholder</span><span>Replace with approved imagery</span></div></div>
<div class="g" style="margin-top:56px">
<div style="grid-column:1/3" class="mono"><div style="color:var(--mute);border-top:1px solid var(--ink);padding-top:12px">Contents</div><div style="margin-top:14px;line-height:2.2;color:var(--deep)">01 The seams<br><span style="color:var(--mute)">02 One brief</span><br><span style="color:var(--mute)">03 Who answers</span></div></div>
<div style="grid-column:4/10" class="body">
<p><span style="font-family:'Inter Tight';font-weight:500;font-size:20px">Most enterprise web programs</span> are split across a strategy consultant, a creative agency, a development shop and a marketing-ops contractor. Each is competent. The trouble is what happens between them.<sup>1</sup></p>
<p>Every hand-off is a translation. Intent gets compressed into a brief, the brief into a design, the design into tickets. By launch, the original business challenge is three documents away.</p>
<div class="pq">The work fails at the seams, so remove the seams.</div>
<p>One office changes the unit of accountability. The person who heard the problem is in the room when it is built, and still answers the phone after launch.<sup>2</sup></p></div>
<div style="grid-column:10/13">
<div class="mn"><span class="mono">Note 1</span>Draft copy for the comp. Final article text to come from Walter.</div>
<div class="mn" style="margin-top:150px"><span class="mono">Note 2</span>Margin notes sit in columns 10–12 and align to their reference line.</div></div></div>''','')

# 10 CTA + footer
M['10-cta-footer']=('CTA + footer','''
.band{margin:-72px -128px 0;background:var(--ink);color:var(--paper);padding:96px 128px 104px;position:relative;overflow:hidden}
.band h2{font-size:96px;color:var(--paper);letter-spacing:-.03em}
.band .tk:before,.band .tk:after{background:var(--sky)}
.dk1{background:var(--paper);color:var(--ink)}.dk1 i{width:8px;height:8px;background:var(--yel);display:block;outline:1px solid var(--ink)}
.dkl{color:var(--sky);border-bottom:1px solid var(--sky);padding-bottom:3px;font-weight:500;font-size:15px}
footer{margin:0 -128px -96px;padding:34px 128px 42px;position:relative;z-index:2;background:var(--paper);display:flex;align-items:center;gap:40px;border-top:1px solid var(--ink)}
footer .mono{color:var(--mute)}
footer a.mono:hover{color:var(--ink)}
''','''
<div class="band"><span class="tk" style="left:40px;top:28px"></span><span class="tk" style="right:40px;top:28px"></span><span class="tk" style="left:40px;bottom:28px"></span><span class="tk" style="right:40px;bottom:28px"></span>
<svg id="m" width="760" height="560" viewBox="0 0 760 560" style="position:absolute;right:40px;top:30px"></svg>
<div class="mono" style="color:var(--sky);display:flex;gap:14px;align-items:center;margin-bottom:28px"><span style="width:28px;height:1px;background:var(--sky);display:block"></span>10 — Start here</div>
<h2>Talk to Walter.</h2>
<p style="font-size:21px;max-width:560px;margin-top:24px;color:rgba(241,239,234,.85)">Bring the business challenge. You will speak with the founder, not a sales queue, and leave with a clear next step.</p>
<div style="margin-top:40px;display:flex;gap:32px;align-items:center"><a class="btn dk1" style="height:60px;padding:0 30px;font-size:16px"><i></i>Book a call with Walter</a><a class="dkl">Or send a brief by email →</a></div>
<div class="mono" style="margin-top:64px;color:rgba(241,239,234,.55);display:flex;gap:40px"><span>Wilmington, NC</span><span>English &amp; Nederlands</span><span>Since 2008</span></div>
</div>
<footer><img src="rp-left-dark.svg" style="height:28px"><span class="mono">© 2026 Razor Profiles LLC</span><span class="mono">Wilmington, NC</span>
<span style="margin-left:auto;display:flex;gap:32px"><a class="mono">Privacy</a><a class="mono">Terms</a><a class="mono">Accessibility</a><a class="mono">LinkedIn</a></span></footer>''',
"mob(document.getElementById('m'),{R:250,W:84,cx:390,cy:280,ink:'#F1EFEA',hiCol:'#28ABE2',hi:[.06,.31],ew:.9});")

for i,(k,(title,css,body,js)) in enumerate(M.items()):
    open(k+'.html','w').write(HEAD%(css,k[:2],title,body,js))
print(list(M))
