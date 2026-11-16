HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Geist:wght@400;500&family=Geist+Mono:wght@400;500&display=block" rel="stylesheet">
<link rel="stylesheet" href="base.css"><style>%s</style></head><body>
<div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface</span><span class="r">Module %s / 10 — <b>%s</b></span></div>
%s
<script>document.fonts.ready.then(()=>{document.title='H'+document.documentElement.scrollHeight;});</script></body></html>'''
M={}
NAV='''<header style="height:76px;display:flex;align-items:center;padding:0 112px;border-bottom:1px solid var(--rule);background:var(--base);position:relative;z-index:3">
<img src="rp-left-light.svg" style="height:34px"><nav style="display:flex;align-items:center;height:76px;gap:40px;margin-left:auto;margin-right:36px;font-size:15px;font-weight:500"><a>Capabilities ▾</a><a>Work ▾</a><a>Approach</a><a>About</a><a style="color:var(--sky);box-shadow:inset 0 -2px 0 var(--sky);padding:28px 0 26px">Insights</a></nav>
<a class="btn pill">Talk to Walter <span>→</span></a></header>'''

# 01 Tabs
M['01-tabs']=('Tabs','''
.tabs{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--rule);margin-top:52px}
.tab{padding:22px 0 20px;display:flex;gap:16px;align-items:baseline;position:relative;color:var(--mute2)}
.tab .t{font-size:22px;font-weight:500}
.tab.on{color:var(--text)}
.tab.on:after{content:"";position:absolute;left:0;right:24px;bottom:-1px;height:2px;background:var(--sky)}
.tab.on:before{content:"";position:absolute;left:0;width:56px;top:0;height:2px;background:var(--yel)}
.rib{position:absolute;right:-90px;top:390px;width:820px}
''','''<section class="sec" style="min-height:900px"><img class="rib" src="rb-q1.png">
<div class="g"><div style="grid-column:1/9"><div class="lab mono">02 — Capabilities</div><div class="disp">Four faces of<br>one surface.</div></div></div>
<div class="tabs" style="position:relative;z-index:2">
<div class="tab on"><span class="mono" style="color:var(--sky)">01</span><span class="t">Strategy</span></div>
<div class="tab"><span class="mono">02</span><span class="t">Marketing</span></div>
<div class="tab"><span class="mono">03</span><span class="t">Design</span></div>
<div class="tab"><span class="mono">04</span><span class="t">Development</span></div></div>
<div class="g" style="margin-top:52px;position:relative;z-index:2"><div style="grid-column:1/6">
<div class="mono" style="color:var(--mute2);margin-bottom:14px">Face 01 / 04 — Strategy</div>
<h3 style="font-size:32px;line-height:1.15">Define the challenge before anyone draws a page.</h3>
<p style="margin-top:18px">Digital strategy and account-based planning, built around the business problem rather than the channel.</p>
<div class="rt" style="margin-top:28px">
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">A</span><span>Identify the business challenge(s)</span></div>
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">B</span><span>Prioritize by benefit to the organization and cost</span></div>
<div class="row" style="grid-template-columns:52px 1fr"><span class="mono" style="color:var(--mute2)">C</span><span>Agree an implementation plan</span></div></div>
<div style="margin-top:32px;display:flex;gap:30px;align-items:center"><a class="btn b1">Talk to Walter <i></i></a><a class="tl">Strategy in detail</a></div></div>
<div style="grid-column:9/13;align-self:end;text-align:right" class="mono"><span style="color:var(--mute2)">Fig. 02 — The surface turned to its strategy face</span></div></div></section>''')

# 02 Media + text
M['02-media-text']=('Media + text','''
.split{display:grid;grid-template-columns:1fr 1fr;min-height:760px}
.media{position:relative;overflow:hidden}
.media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:0 0}
.media .cap{position:absolute;left:112px;right:40px;bottom:28px;margin:0;color:var(--text);text-shadow:0 1px 0 rgba(0,0,0,.5)}
''','''<div class="split"><div class="media"><img src="g-1.png"><div style="position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,rgba(13,15,26,.92))"></div>
<div class="cap mono"><span>Fig. 03 — Placeholder screen capture</span><span>Replace with approved work</span></div></div>
<div class="surf" style="padding:96px 112px 96px 96px"><div class="lab mono">03 — Website development</div>
<div class="disp" style="font-size:72px">Built on HubSpot.<br>Built to last.</div>
<p style="margin-top:26px;max-width:520px">From the first brief to launch, one team carries the work through analysis, scope, design and build, so nothing is lost in a hand-off.</p>
<div class="rt" style="margin-top:30px;max-width:560px">
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Process</span><span>Briefing → analysis → scope → sitemap, wireframes, design → develop</span></div>
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Platform</span><span>HubSpot CMS themes · HubSpot–Algolia search</span></div>
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Access</span><span>WCAG 2.2 AA as the target</span></div></div>
<div style="margin-top:34px"><a class="sl">See how an engagement runs →</a></div></div></div>''')

# 03 Buttons
BT=lambda dark: f'''
<div class="tbl {'' if dark else 'lt'}">
<div class="h mono">{'Dark (default)' if dark else 'Light mode — long reads'}</div><div class="h mono">Default</div><div class="h mono">Hover</div><div class="h mono">Focus (visible)</div><div class="h mono">Disabled</div>
<div class="mono rl">Primary</div>
<div><a class="btn P">Talk to Walter <i></i></a></div><div><a class="btn P PH">Talk to Walter <i></i></a></div><div><a class="btn P F">Talk to Walter <i></i></a></div><div><a class="btn P D">Talk to Walter <i></i></a></div>
<div class="mono rl">Secondary</div>
<div><a class="btn S">See our approach</a></div><div><a class="btn S SH">See our approach</a></div><div><a class="btn S F">See our approach</a></div><div><a class="btn S D">See our approach</a></div>
<div class="mono rl">Pill (header)</div>
<div><a class="btn pill PL">Talk to Walter <span>→</span></a></div><div><a class="btn pill PL PLH">Talk to Walter <span>→</span></a></div><div><a class="btn pill PL F">Talk to Walter <span>→</span></a></div><div><a class="btn pill PL D">Talk to Walter <span>→</span></a></div>
<div class="mono rl">Icon</div>
<div><a class="ico">→</a></div><div><a class="ico IH">→</a></div><div><a class="ico F">→</a></div><div><a class="ico D">→</a></div>
<div class="mono rl">Text link</div>
<div><a class="L">Website development</a></div><div><a class="L LH">Website development</a></div><div><a class="L F">Website development</a></div><div><a class="L D">Website development</a></div>
</div>'''
M['03-buttons']=('Buttons + links','''
.tbl{display:grid;grid-template-columns:200px repeat(4,1fr);border-top:1px solid rgba(234,234,233,.4)}
.tbl>div{border-bottom:1px solid var(--rule);padding:22px 0;display:flex;align-items:center;min-height:96px}
.tbl .h{min-height:auto;padding:12px 0;color:var(--mute)}.tbl .rl{color:var(--mute)}
.P{background:var(--text);color:var(--base)}.P i{width:22px;height:2px;background:var(--base);display:block}
.PH{background:#fff;box-shadow:inset 0 -2px 0 var(--yel)}
.S{border:1px solid rgba(234,234,233,.5);color:var(--text)}.SH{background:rgba(234,234,233,.08);border-color:var(--text)}
.PL{border:1px solid rgba(234,234,233,.4);color:var(--text)}.PLH{border-color:var(--sky);color:var(--sky)}
.ico{width:52px;height:52px;border:1px solid rgba(234,234,233,.5);display:flex;align-items:center;justify-content:center;font-size:18px}
.IH{background:var(--text);color:var(--base)}
.L{color:var(--sky);border-bottom:1px solid var(--sky);padding-bottom:3px;font-weight:500;font-size:15px}.LH{border-bottom-width:2px;color:var(--text);border-color:var(--text)}
.F{outline:2px solid var(--sky);outline-offset:3px}
.D{background:#1f2337!important;color:#8C90A3!important;border-color:#2a2e44!important;box-shadow:none!important}.D i{background:#8C90A3!important}.D span{color:#8C90A3!important}
.ico.D,.L.D{background:none!important}
.lt{border-top-color:#131626}.lt>div{border-bottom-color:rgba(32,56,108,.24)}.lt .h,.lt .rl{color:#4A5068}
.lt .P{background:var(--ink);color:var(--paper)}.lt .P i{background:var(--paper)}.lt .PH{background:var(--deep);box-shadow:inset 0 -2px 0 var(--yel)}
.lt .S{border-color:var(--ink);color:var(--ink)}.lt .SH{background:rgba(19,22,38,.06)}
.lt .PL{border-color:rgba(19,22,38,.5);color:var(--ink)}.lt .PL span{color:var(--deep)}.lt .PLH{border-color:var(--deep);color:var(--deep)}
.lt .ico{border-color:var(--ink);color:var(--ink)}.lt .IH{background:var(--ink);color:var(--paper)}
.lt .L{color:var(--deep);border-color:var(--deep)}.lt .LH{color:var(--ink);border-color:var(--ink)}
.lt .F{outline-color:var(--deep)}
.lt .D{background:#DCD9D2!important;color:#575C74!important;border-color:#DCD9D2!important}.lt .D i{background:#575C74!important}.lt .D span{color:#575C74!important}
.lt .ico.D,.lt .L.D{background:none!important;border-color:#c5c2bb!important}
''','''<section class="sec" style="padding-bottom:72px"><div class="g"><div style="grid-column:1/8"><div class="lab mono">Component sheet — Actions</div><div class="disp">Buttons and links</div></div>
<div style="grid-column:9/13;align-self:end"><p class="small">Sky marks interaction on dark. Yellow is the one hot edge, shown on primary hover. Focus rings are 2px with a 3px offset.</p></div></div>
<div style="margin-top:48px">'''+BT(True)+'''</div><div class="cap mono" style="margin-top:18px"><span>Fig. 04 — Dark: text #EAEAE9 15.9:1, Sky 7.3:1, muted #8C90A3 6.0:1 on base</span></div></section>
<section class="sec light" style="padding-top:64px;padding-bottom:80px">'''+BT(False)+'''<div class="cap mono" style="margin-top:18px"><span>Fig. 05 — Light mode: Sky is not used on paper; links and focus use Deep Blue #20386C (9.9:1)</span></div></section>''')

# 04 Accordion
M['04-accordion']=('Accordion','''
.it{border-bottom:1px solid var(--rule);display:grid;grid-template-columns:64px 1fr 40px;align-items:center;padding:24px 0}
.it .t{font-size:24px;font-weight:500}
.pm{width:28px;height:28px;border:1px solid rgba(234,234,233,.5);position:relative;justify-self:end;border-radius:50%}
.pm:before,.pm:after{content:"";position:absolute;background:var(--text);left:8px;right:8px;top:13px;height:1px}
.pm.plus:after{transform:rotate(90deg)}
.open{background:var(--surf);margin:0 -28px;padding:24px 28px;box-shadow:inset 2px 0 0 var(--yel)}
.open .pm{border-color:var(--sky)}.open .pm:before{background:var(--sky)}
.body{grid-column:2/3;padding-top:16px}
''','''<section class="sec"><img src="rb-edge2.png" style="position:absolute;left:-200px;top:360px;width:800px">
<div class="g"><div style="grid-column:1/6;position:relative;z-index:2"><div class="lab mono">04 — How we engage</div><div class="disp">From brief<br>to run.</div>
<p class="small" style="margin-top:22px;max-width:380px">The same team stays on the work from the first conversation through launch and after it.</p></div>
<div style="grid-column:6/13;border-top:1px solid rgba(234,234,233,.4);position:relative;z-index:2">
<div class="it open"><span class="mono" style="color:var(--sky)">01</span><span class="t">Discover</span><span class="pm"></span>
<div class="body"><p>We start with the business challenge, not the deliverable. Together we name the problem, rank options by benefit and cost, and agree what success looks like before scope is written.</p>
<div class="rt" style="margin-top:22px">
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">You get</span><span>A written brief and an agreed scope</span></div>
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Who</span><span>Walter Lentfert with the delivery team</span></div></div>
<div style="margin-top:22px"><a class="sl">Talk to Walter about discovery →</a></div></div></div>
<div class="it"><span class="mono" style="color:var(--mute2)">02</span><span class="t">Plan</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">03</span><span class="t">Build</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">04</span><span class="t">Run</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">FAQ</span><span class="t">Do you work alongside in-house teams?</span><span class="pm plus"></span></div>
<div class="it"><span class="mono" style="color:var(--mute2)">FAQ</span><span class="t">Can you work under NDA?</span><span class="pm plus"></span></div></div></div>
<div class="cap mono" style="margin-top:28px"><span>Fig. 06 — Ribbon edge-on, bleeding off the left frame</span></div></section>''')

# 05 Carousel
SL=lambda n,img,tag,t: f'''<div class="sld"><div style="height:280px;overflow:hidden;border:1px solid var(--rule)"><img src="{img}" style="width:100%;height:100%;object-fit:cover;object-position:0 0"></div><div style="padding:22px 24px 26px"><div class="mono" style="color:var(--mute2);display:flex;justify-content:space-between"><span>{tag}</span><span>{n}</span></div><h3 style="margin-top:12px;font-size:23px;line-height:1.25">{t}</h3><a class="sl" style="display:inline-block;margin-top:18px">Read →</a></div></div>'''
M['05-carousel']=('Carousel','''
.track{display:flex;gap:24px;margin-top:48px;margin-right:-112px;overflow:hidden}
.sld{flex:0 0 440px;background:var(--surf)}
.ar{width:52px;height:52px;border:1px solid rgba(234,234,233,.5);display:flex;align-items:center;justify-content:center;font-size:18px;border-radius:50%}
.prog{height:1px;background:var(--rule);margin-top:44px;position:relative}
.prog i{position:absolute;left:0;top:-1px;height:3px;width:16.66%;background:var(--sky)}
.prog b{position:absolute;left:calc(16.66% - 18px);top:-1px;height:3px;width:18px;background:var(--yel)}
''','''<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">05 — Insights</div><div class="disp">Notes from the work</div></div>
<div style="grid-column:9/13;display:flex;align-items:center;justify-content:flex-end;gap:28px"><span class="mono" style="color:var(--mute)"><b style="color:var(--text)">01</b> / 06</span>
<div style="display:flex;gap:12px"><a class="ar" style="color:#8C90A3;border-color:#2a2e44">←</a><a class="ar" style="background:var(--text);color:var(--base);border-color:var(--text)">→</a></div></div></div>
<div class="track">'''+SL('01','g-2.png','Strategy · Article','Why one office beats a roster of vendors')+SL('02','g-3.png','Development · Guide','Planning a HubSpot CRM migration without losing history')+SL('03','g-4.png','Marketing · Article','Account-based marketing for life-sciences teams')+SL('04','g-5.png','Design · Note','What WCAG 2.2 changes for enterprise sites')+'''</div>
<div class="prog"><i></i><b></b></div>
<div class="cap mono"><span>Fig. 07 — Progress in Sky, leading edge in yellow. Images are graded placeholders.</span><span>Swipe or use arrows</span></div></section>''')

# 06 Cards
CARD=lambda n,t,d,items,rb,hov: f'''<div class="cd{' hov' if hov else ''}"><div class="ri"><img src="{rb}"></div><div style="padding:26px 28px 32px">
<span class="mono" style="color:{'var(--sky)' if hov else 'var(--mute2)'}">{n}</span><h3 style="font-size:28px;margin-top:10px">{t}</h3><p class="small" style="margin-top:10px">{d}</p>
<div class="rt" style="margin-top:20px">{''.join(f'<div class="row small" style="padding:9px 0;color:var(--text)">{i}</div>' for i in items)}</div>
<a class="{'tl' if hov else 'sl'}" style="display:inline-block;margin-top:22px">{t} →</a></div></div>'''
M['06-cards']=('Cards','''
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:52px}
.cd{background:var(--surf);border:1px solid var(--rule);position:relative}
.cd .ri{height:230px;overflow:hidden;background:var(--base);display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--rule)}
.cd .ri img{width:92%}
.cd.hov{border-color:var(--sky);transform:translateY(-8px);box-shadow:inset 0 2px 0 var(--yel),0 8px 0 rgba(0,0,0,.35)}
.cd.hov .ri img{width:104%}
.cd.hov:before{content:'';position:absolute;left:0;right:0;top:0;height:2px;background:var(--yel);z-index:2}
.callout{position:absolute;top:-38px;color:var(--sky)}
''','''<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">06 — Capabilities</div><div class="disp">Pick a starting point</div></div>
<div style="grid-column:9/13"><p class="small">Every card leads into the same team. Start with the discipline closest to your problem.</p></div></div>
<div class="cards" style="position:relative">'''+CARD('01','Strategy','Digital strategy and account-based planning.',['Business challenge definition','Prioritization by benefit and cost','Implementation planning'],'rb-q0.png',False)+CARD('02','Marketing','Campaigns and automation tuned to the persona journey.',['Inbound and outbound campaigns','Account-based marketing','HubSpot marketing automation'],'rb-q2.png',True)+CARD('04','Development','HubSpot CMS, CRM and the integrations between them.',['HubSpot CMS themes','CRM implementation and migration','Bespoke process development'],'rb-q3.png',False)+'''
<span class="callout mono" style="left:calc(33.33% + 24px)">Hover — lift 8px, Sky border, yellow hot edge, ribbon zooms</span></div>
<div class="cap mono" style="margin-top:28px"><span>Fig. 08 — Card grid, 3-up (three of four disciplines). Each card shows a different face of the strip.</span><span>Default · Hover · Default</span></div></section>''')

# 07 Bento
M['07-bento']=('Bento','''
.bento{display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:330px 300px;gap:24px;margin-top:52px}
.tile{background:var(--surf);border:1px solid var(--rule);padding:26px 28px;position:relative;overflow:hidden}
''','''<section class="sec"><div class="g"><div style="grid-column:1/9"><div class="lab mono">07 — Proof</div><div class="disp">One office, in detail.</div></div></div>
<div class="bento">
<div class="tile" style="grid-column:1/7;grid-row:1/3;background:var(--base);padding:0"><img src="rb-twist.png" style="position:absolute;width:118%;left:-6%;top:40px">
<span class="mono" style="position:absolute;left:28px;top:24px;color:var(--sky)">Fig. 09 — The twist: where disciplines meet</span>
<div style="position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,var(--base) 70%)"></div><span class="mono" style="position:absolute;left:28px;bottom:24px;color:var(--mute)">Strategy · Marketing · Design · Development</span></div>
<div class="tile" style="grid-column:7/10"><div class="mono" style="color:var(--mute)">Stat — placeholder</div>
<div class="ph" style="margin-top:22px;height:150px;display:flex;align-items:center;justify-content:center;font-family:Philosopher;font-size:72px">—</div>
<p class="small" style="margin-top:16px">[Metric pending real data. Publish only a sourced, client-approved number.]</p></div>
<div class="tile light" style="grid-column:10/13;border-color:var(--paper);background:var(--paper);color:var(--ink)"><div class="mono" style="color:var(--deep)">Direct line</div>
<div style="font-family:Philosopher;font-size:36px;line-height:1.05;margin-top:18px">Talk to Walter, not a sales queue.</div>
<p class="small" style="margin-top:12px;color:#4A5068">Founder and President. Wilmington, NC.</p>
<a style="position:absolute;left:28px;bottom:28px;color:var(--deep);border-bottom:1px solid var(--deep);padding-bottom:3px;font-weight:500;font-size:15px">Book a call →</a></div>
<div class="tile" style="grid-column:7/13"><div style="display:flex;justify-content:space-between"><span class="mono" style="color:var(--mute)">Services index</span><span class="mono" style="color:var(--mute)">Est. 2008</span></div>
<div class="rt" style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;column-gap:24px">
<div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">01</span>Digital strategy</div><div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">04</span>Marketing campaigns</div>
<div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">02</span>Account-based marketing</div><div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">05</span>CRM implementation / migration</div>
<div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">03</span>Website development</div><div class="row small" style="grid-template-columns:40px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">06</span>Bespoke process development</div></div>
<p class="small" style="margin-top:18px">Focus: life sciences, medical devices, pharma and biotech.</p></div></div></section>''')

# 08 Quote
M['08-quote']=('Quote','''
blockquote{font-family:Philosopher;font-size:46px;line-height:1.16;color:var(--text);text-indent:-.4em}
.qm{color:var(--sky)}
.ar{width:52px;height:52px;border:1px solid rgba(234,234,233,.5);display:flex;align-items:center;justify-content:center;font-size:18px;border-radius:50%}
''','''<section class="sec" style="padding-top:96px"><img src="rb-top.png" style="position:absolute;right:-470px;top:-110px;width:820px">
<div class="g" style="position:relative;z-index:2"><div style="grid-column:1/4"><div class="lab mono">08 — Client words</div><div class="mono" style="color:var(--mute2);margin-top:8px">Testimonial 01 / 02</div></div>
<div style="grid-column:4/11"><div style="width:56px;height:2px;background:var(--yel);margin-bottom:34px"></div>
<blockquote><span class="qm">“</span>Walter and team have been my go-to for all things HubSpot and web development across multiple companies. From Psomagen to 9amHealth, his custom theme builds were clean, reliable, and built with scalability in mind. His work at Kean and BLIP also showed his strength in complex integrations — he delivers not just code, but confidence.<span class="qm">”</span></blockquote>
<div class="rt" style="margin-top:48px;display:grid;grid-template-columns:1fr auto;align-items:center;padding-top:18px">
<div><div style="font-weight:500">Client testimonial</div><div class="mono" style="color:var(--mute);margin-top:6px">Shared by Walter Lentfert, June 2025 · Name and title pending approval</div></div>
<div style="display:flex;gap:12px;align-items:center"><span class="mono" style="color:var(--mute);margin-right:12px"><b style="color:var(--text)">01</b> / 02</span><a class="ar" style="color:#8C90A3;border-color:#2a2e44">←</a><a class="ar" style="background:var(--text);color:var(--base);border-color:var(--text)">→</a></div></div></div></div></section>''')

# 09 Article
M['09-article']=('Article','''
.crumb{padding:0 112px;height:46px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--rule);color:var(--mute)}
.crumb b{color:var(--text);font-weight:500}
.lead{position:relative;height:640px;overflow:hidden;border-bottom:1px solid var(--rule)}
.body p{font-size:19px;line-height:1.7;margin-bottom:24px;color:#262b40}
.body sup{color:var(--deep);font-family:'Geist Mono';font-size:11px;font-weight:500}
.pq{border-left:2px solid var(--yel);padding:4px 0 4px 28px;margin:38px 0;font-family:Philosopher;font-size:40px;line-height:1.15;color:var(--ink)}
.mn{border-top:1px solid var(--ink);padding-top:12px;font-size:13px;line-height:1.55;color:#4A5068;margin-bottom:28px}
.mn .mono{color:var(--deep);display:block;margin-bottom:6px}
.mode{display:inline-flex;border:1px solid rgba(19,22,38,.4);border-radius:999px;overflow:hidden}
.mode span{padding:8px 14px}.mode .on{background:var(--ink);color:var(--paper)}
''',NAV+'''<div class="crumb mono"><span>Home</span><span>/</span><span>Insights</span><span>/</span><b>Why one office beats a roster of vendors</b></div>
<div class="lead"><img src="rb-hero.png" style="position:absolute;right:-300px;top:-30px;width:980px">
<div style="position:absolute;left:112px;top:90px;width:760px"><div class="lab mono">Insights · Strategy</div>
<div class="disp" style="font-size:84px">Why one office beats a roster of vendors</div>
<p style="font-size:21px;margin-top:26px;max-width:640px">Strategy, marketing, design and development fail at the seams between them. A single accountable team removes the seams.</p>
<div class="mono" style="margin-top:34px;color:var(--mute);display:flex;gap:36px"><span>By <b style="color:var(--text)">Walter Lentfert</b></span><span>Reading time — placeholder</span><span>Filed — Strategy</span></div></div></div>
<section class="light" style="padding:72px 112px 96px;position:relative">
<div class="g"><div style="grid-column:1/4"><div class="mono" style="color:#4A5068;border-top:1px solid var(--ink);padding-top:12px">Contents</div><div class="mono" style="margin-top:14px;line-height:2.3;color:var(--deep)">01 The seams<br><span style="color:#575C74">02 One brief</span><br><span style="color:#575C74">03 Who answers</span></div>
<div class="mono" style="margin-top:36px;color:#4A5068">Reading mode</div><div class="mode mono" style="margin-top:10px"><span class="on">Light</span><span>Dark</span></div></div>
<div style="grid-column:4/10" class="body">
<p><span style="font-weight:500;color:var(--ink)">Most enterprise web programs</span> are split across a strategy consultant, a creative agency, a development shop and a marketing-ops contractor. Each is competent. The trouble is what happens between them.<sup>1</sup></p>
<p>Every hand-off is a translation. Intent gets compressed into a brief, the brief into a design, the design into tickets. By launch, the original business challenge is three documents away.</p>
<div class="pq">The work fails at the seams, so remove the seams.</div>
<p>One office changes the unit of accountability. The person who heard the problem is in the room when it is built, and still answers the phone after launch.<sup>2</sup></p></div>
<div style="grid-column:10/13"><div class="mn"><span class="mono">Note 1</span>Draft copy for the comp. Final article text to come from Walter.</div>
<div class="mn" style="margin-top:170px"><span class="mono">Note 2</span>Long reads switch to light mode: paper #F1EFEA, ink #131626, Deep Blue links.</div></div></div>
<div class="cap mono" style="margin-top:20px"><span>Fig. 01 — Dark header with ribbon, light-mode body for long reads</span></div></section>''')

# 10 CTA + footer
M['10-cta-footer']=('CTA + footer','''
.band{position:relative;overflow:hidden;padding:120px 112px 120px;min-height:700px;border-bottom:1px solid var(--rule)}
footer{padding:30px 112px 36px;display:flex;align-items:center;gap:40px;background:var(--base)}
footer .mono{color:var(--mute)}
''','''<div class="band"><img src="rb-hero.png" style="position:absolute;left:340px;top:-60px;width:1400px">
<div style="position:absolute;left:0;top:0;bottom:0;width:62%;background:linear-gradient(90deg,var(--base) 38%,rgba(13,15,26,.0))"></div>
<div style="position:relative;z-index:2"><div class="lab mono">10 — Start here</div>
<div class="disp" style="font-size:132px;line-height:.92">Let’s talk.</div>
<p style="font-size:21px;max-width:520px;margin-top:30px">Bring the business challenge. You will speak with Walter, the founder, not a sales queue, and leave with a clear next step.</p>
<div style="margin-top:42px;display:flex;gap:32px;align-items:center"><a class="btn b1" style="height:60px;padding:0 30px;font-size:16px">Book a call with Walter <i></i></a><a class="tl">Or send a brief by email</a></div>
<div class="mono" style="margin-top:72px;color:var(--mute);display:flex;gap:40px"><span>Wilmington, NC</span><span>English &amp; Nederlands</span><span>Since 2008</span></div></div></div>
<footer><img src="rp-left-light.svg" style="height:28px"><span class="mono">© 2026 Razor Profiles LLC</span><span class="mono">Wilmington, NC</span>
<span style="margin-left:auto;display:flex;gap:32px"><a class="mono">Privacy</a><a class="mono">Terms</a><a class="mono">Accessibility</a><a class="mono">LinkedIn</a></span></footer>''')

for k,(title,css,body) in M.items(): open(k+'.html','w').write(HEAD%(css,k[:2],title,body))
print(len(M))
