HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Geist:wght@400;500&family=Geist+Mono:wght@400;500&display=block" rel="stylesheet">
<link rel="stylesheet" href="base.css"><style>%s</style></head><body>'''
TAIL='<script>document.fonts.ready.then(()=>{document.title="H"+document.documentElement.scrollHeight;});</script></body></html>'
IM=[('01-ecomm-product-page','Reagent kit product page on laptop','Ecommerce · Capabilities hero, ecommerce case study'),
('02-packaging-shoot','Kit boxes, vials and tube rack, catalog shoot','Product content · Media + text, catalog/ecomm page'),
('03-bench-ordering','Gloved hands ordering on a tablet at the bench','B2B buyer moment · 4:5 card'),
('04-device-hero','Handheld device on black, one key light','Med-device launch · Full-bleed hero'),
('05-strategy-session','Team, backs turned, reviewing a site on a wall screen','Strategy / Approach · Media + text'),
('06-mobile-checkout','Gloved hand, mobile checkout (screen soft)','Mobile ecomm · 4:5 card, bento tile'),
('07-launch-booth','Dark booth, launch visual, attendees turned away','Launches & events · Case-study band'),
('08-crm-dashboard','CRM funnel dashboard on a monitor (labels soft)','Data & CRM / HubSpot · Bento, Development tab'),
('09-hq-night','Curved glass HQ at night','Enterprise scale · About, section break'),
('10-content-production','Camera shooting a benchtop instrument','Content production · Design / Approach'),
('11-kit-card','Open reagent kit, blue-capped vials','Packaging / catalog · 4:5 card'),
('12-packaging-proofs','Hands reviewing carton dielines and proofs','Packaging design · 4:5 card, Design tab')]
css='''.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px 24px;padding:0 112px 72px}
.t{position:relative;background:var(--surf);overflow:hidden}.t img{display:block;width:100%%;height:100%%;object-fit:cover}
.w{grid-column:span 2;aspect-ratio:16/9}.p{aspect-ratio:4/5}
.n{position:absolute;left:10px;top:10px;background:rgba(13,15,26,.85);padding:4px 8px;color:var(--text)}
.l{margin-top:12px;font-size:15px;color:var(--text)}.s{margin-top:6px;color:var(--mute);font-size:10.5px;letter-spacing:.1em}'''.replace('%%','%')
h=HEAD%css+'<div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface</span><span class="r">Imagery — <b>Life-science agency set (generated, graded)</b></span></div>'
h+='<section style="padding:72px 112px 44px"><div class="lab mono">Imagery — Life sciences</div><div class="disp" style="font-size:64px">The work, not just the lab</div><p class="small" style="margin-top:18px;max-width:820px">Twelve generated frames showing the agency at work for life-science brands: storefronts, catalog shoots, packaging, launches, CRM and strategy. All graded to B. Screens are kept generic or soft, with no brands or logos. These are concept images to brief a shoot or stock search, not finished photography.</p></section><div class="grid">'
order=['01','04','02','03','11','05','07','06','12','08','09','10']
d={i[0][:2]:i for i in IM}
for k in order:
    f,t,s=d[k]; cls='p' if k in('03','06','11','12') else 'w'
    h+=f'<div style="grid-column:{"span 2" if cls=="w" else "span 1"}"><div class="t {cls}" style="grid-column:auto"><img src="../{f}.png"><span class="n mono">{k}</span></div><div class="l">{t}</div><div class="s mono">{s}</div></div>'
h+='</div><div class="cap mono" style="padding:0 112px 48px;margin:0"><span>Generated with Grok Imagine · graded with grade.py at 55%</span><span>16:9 at 1280×720 · 4:5 at 864×1080</span></div>'+TAIL
open('sheet.html','w').write(h)

css2='''header{height:84px;display:flex;align-items:center;padding:0 112px;gap:44px;position:absolute;left:0;right:0;top:52px;z-index:3}
header img{height:30px}header nav{display:flex;gap:32px;font-size:15px;color:var(--text)}header .cta{margin-left:auto}
.hero{position:relative;height:820px;overflow:hidden}
.hero .ph{position:absolute;right:0;top:0;bottom:0;width:72%;border:0}.hero .ph img{width:100%;height:100%;object-fit:cover;object-position:62% 50%}
.hero .ov{position:absolute;inset:0;background:linear-gradient(90deg,var(--base) 30%,rgba(13,15,26,.85) 44%,rgba(13,15,26,0) 64%)}
.hero .tx{position:absolute;left:112px;top:220px;width:640px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:52px;position:relative}
.cd{background:var(--surf);border:1px solid var(--rule);position:relative}
.cd .ri{aspect-ratio:4/5;max-height:420px;width:100%;overflow:hidden;border-bottom:1px solid var(--rule)}.cd .ri img{width:100%;height:100%;object-fit:cover}
.cd.hov{border-color:var(--sky);transform:translateY(-8px);box-shadow:0 8px 0 rgba(0,0,0,.35)}
.cd.hov:before{content:'';position:absolute;left:0;right:0;top:0;height:2px;background:var(--yel);z-index:2}
.callout{position:absolute;top:-38px;color:var(--sky)}
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:300px 300px;gap:24px;margin-top:52px}
.bt{background:var(--surf);border:1px solid var(--rule);position:relative;overflow:hidden;padding:30px}
.bt.img{padding:0}.bt.img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.bt .cap2{position:absolute;left:24px;right:24px;bottom:20px;color:var(--text)}'''
c=HEAD%css2+'<div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface</span><span class="r">Imagery in context — <b>Hero · Cards · Bento (life sciences)</b></span></div>'
c+='''<div class="hero"><div class="ph"><img src="../01-ecomm-product-page.png"></div><div class="ov"></div>
<header style="top:0"><img src="rp-left-light.svg"><nav><span>Capabilities</span><span>Work</span><span>Approach</span><span>About</span><span>Insights</span></nav><a class="btn b1 cta" style="height:44px">Talk to Walter <i></i></a></header>
<div class="tx"><div class="mono" style="color:var(--mute)">Home / Capabilities / <span style="color:var(--text)">Ecommerce</span></div>
<div class="lab mono" style="margin-top:40px">Ecommerce for life sciences</div>
<div class="disp" style="font-size:80px">Your catalog,<br>sold online.</div>
<p style="margin-top:26px;max-width:520px">Product pages, spec tables, kit configurators and B2B checkout for reagent, lab-supply and device brands, with strategy, design, development and CRM handled by one team.</p>
<div style="display:flex;gap:16px;margin-top:36px"><a class="btn b1">Talk to Walter <i></i></a><a class="btn b2">See how we build stores</a></div></div>
<div class="cap mono" style="position:absolute;left:112px;right:112px;bottom:28px;margin:0"><span>Fig. 01 — Image 01, product page on laptop (generated, UI generic)</span><span>Capabilities / Ecommerce hero</span></div></div>
<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">06 — Cards</div><div class="disp">From bench to checkout</div></div>
<div style="grid-column:9/13"><p class="small">Each card shows a different part of the job: the product content, the buyer's moment, the mobile order.</p></div></div><div class="cards">'''
cards=[('11-kit-card','01','Product content','Catalog and packaging photography that sells a kit before the spec sheet does.','sl',''),
('03-bench-ordering','02','B2B ecommerce','Reorder flows, account pricing and spec-led search for buyers at the bench.','tl',' hov'),
('06-mobile-checkout','03','Mobile checkout','Consumables ordered in a few taps, wired into your ERP and CRM.','sl','')]
for f,n,t,dsc,lk,hv in cards:
    col='var(--sky)' if hv else 'var(--mute2)'
    c+=f'<div class="cd{hv}"><div class="ri"><img src="../{f}.png"></div><div style="padding:26px 28px 32px"><span class="mono" style="color:{col}">{n}</span><h3 style="font-size:28px;margin-top:10px">{t}</h3><p class="small" style="margin-top:10px">{dsc}</p><a class="{lk}" style="display:inline-block;margin-top:20px">{t} →</a></div></div>'
c+='''<span class="callout mono" style="left:calc(33.33% + 8px)">Hover — lift 8px, Sky border, yellow hot edge</span></div></section>
<section class="sec surf" style="padding-top:80px"><div class="lab mono">07 — Bento</div><div class="disp">Launch, measure, sell again</div>
<div class="bento"><div class="bt img" style="grid-column:1/3;grid-row:1/3"><img src="../07-launch-booth.png" style="object-position:70% 50%"><div style="position:absolute;inset:auto 0 0 0;height:120px;background:linear-gradient(transparent,rgba(13,15,26,.92))"></div><div class="cap2 mono" style="display:flex;justify-content:space-between"><span>Launches &amp; events</span><span>Image 07</span></div></div>
<div class="bt img" style="grid-column:3/5;grid-row:1/2"><img src="../08-crm-dashboard.png" style="object-position:70% 40%"><div style="position:absolute;inset:auto 0 0 0;height:100px;background:linear-gradient(transparent,rgba(13,15,26,.92))"></div><div class="cap2 mono" style="display:flex;justify-content:space-between"><span>Data &amp; CRM</span><span>Image 08</span></div></div>
<div class="bt ph" style="grid-column:3/4;grid-row:2/3;display:flex;flex-direction:column;justify-content:space-between;background:transparent"><span class="mono">Stat — placeholder</span><div><div class="disp" style="font-size:56px;color:var(--sky)">— —</div><p class="small" style="margin-top:8px;color:var(--sky)">Approved client result goes here. No number until there's a source.</p></div></div>
<div class="bt" style="grid-column:4/5;grid-row:2/3;background:var(--base)"><span class="mono" style="color:var(--mute2)">What we run</span><div class="rt" style="margin-top:18px">
<div class="row small" style="padding:9px 0;color:var(--text)">Product launches</div><div class="row small" style="padding:9px 0;color:var(--text)">HubSpot CRM and automation</div><div class="row small" style="padding:9px 0;color:var(--text)">Catalog and ecommerce</div><div class="row small" style="padding:9px 0;color:var(--text)">Packaging and product content</div></div></div></div>
<div class="cap mono" style="margin-top:28px"><span>Fig. 07 — Bento with images 07 and 08; stat tile is a labelled placeholder</span><span>Home / Proof</span></div></section>'''+TAIL
open('context.html','w').write(c)
