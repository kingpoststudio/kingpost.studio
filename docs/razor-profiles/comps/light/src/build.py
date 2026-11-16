FONT='<link href="https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Geist:wght@400;500&family=Geist+Mono:wght@400;500&display=block" rel="stylesheet">'
TAIL='<script>document.fonts.ready.then(()=>{document.title="H"+document.documentElement.scrollHeight;});</script></body></html>'
BASE='''
*{box-sizing:border-box;margin:0;padding:0}
:root{--paper:#F1EFEA;--paper2:#E7E4DD;--card:#FAF9F6;--ink:#131626;--mute:#474D63;--mute2:#596075;--deep:#20386C;--yel:#D6DF27;--rule:rgba(19,22,38,.14);--rule2:rgba(19,22,38,.4);
--base:#0D0F1A;--surf:#131626;--text:#EAEAE9;--dmute:#A3A6B4;--dmute2:#8C90A3;--sky:#28ABE2;--drule:rgba(234,234,233,.14)}
html,body{width:1600px;background:var(--paper);color:var(--ink);font-family:Geist,sans-serif;-webkit-font-smoothing:antialiased}body{overflow:hidden}a{color:inherit;text-decoration:none}
.mono{font-family:'Geist Mono',monospace;text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:500}
.spec{height:52px;display:flex;align-items:center;padding:0 112px;border-bottom:1px solid var(--rule2);color:var(--mute);background:var(--paper)}.spec b{color:var(--ink);font-weight:500}.spec .r{margin-left:auto}
.sec{position:relative;padding:96px 112px 104px;overflow:hidden}
.g{display:grid;grid-template-columns:repeat(12,1fr);column-gap:24px;position:relative}
.lab{color:var(--deep);display:flex;gap:14px;align-items:center;margin-bottom:26px}.lab:before{content:"";width:28px;height:1px;background:var(--deep)}
.disp{font-family:Philosopher;font-weight:400;font-size:76px;line-height:.98;letter-spacing:-.01em}
h3{font-family:Geist;font-weight:500;font-size:26px;letter-spacing:-.01em}
p{font-size:17px;line-height:1.6;color:#262B40}.small{font-size:14px;line-height:1.55;color:var(--mute)}
.cap{color:var(--mute2);margin-top:14px;display:flex;justify-content:space-between}
.btn{display:inline-flex;align-items:center;gap:12px;font-weight:500;font-size:15px;height:52px;padding:0 26px}
.b1{background:var(--ink);color:var(--paper)}.b1 i{width:22px;height:2px;background:var(--paper);display:block}
.b2{border:1px solid var(--rule2);color:var(--ink)}
.dl{color:var(--deep);border-bottom:1px solid var(--deep);padding-bottom:3px;font-weight:500;font-size:15px}
.tl{color:var(--ink);border-bottom:2px solid var(--yel);padding-bottom:4px;font-weight:500;font-size:15px}
.row{display:grid;align-items:baseline;border-bottom:1px solid var(--rule);padding:12px 0}.rt{border-top:1px solid var(--rule2)}
header{height:84px;display:flex;align-items:center;padding:0 112px;gap:44px;position:relative;z-index:3}
header img{height:30px}header nav{display:flex;gap:32px;font-size:15px}header .cta{margin-left:auto;height:44px}
/* dark band */
.dark{background:var(--base);color:var(--text)}.dark p{color:rgba(234,234,233,.86)}.dark .small{color:var(--dmute)}
.dark .lab{color:var(--sky)}.dark .lab:before{background:var(--sky)}.dark .cap{color:var(--dmute2)}.dark .rt{border-color:rgba(234,234,233,.4)}.dark .row{border-color:var(--drule)}
.dark .b1{background:var(--text);color:var(--base)}.dark .b1 i{background:var(--base)}.dark .b2{border-color:rgba(234,234,233,.5);color:var(--text)}.dark .spec{background:var(--base);color:var(--dmute);border-color:rgba(234,234,233,.4)}.dark .spec b{color:var(--text)}
.dark .dl{color:var(--sky);border-color:var(--sky)}
'''
def head(extra): return f'<!doctype html><html><head><meta charset="utf-8">{FONT}<style>{BASE}{extra}</style></head>'

HCSS='''.hero{position:relative;height:1000px;overflow:hidden}
.hero .rib{position:absolute;left:560px;top:-10px;width:1180px}
.hero .tx{position:relative;z-index:2;padding:76px 112px 0;width:860px}
.strip{position:absolute;left:112px;right:112px;bottom:0;display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--rule2);z-index:2}
.strip>div{padding:26px 28px 40px 0;border-right:1px solid var(--rule);margin-right:24px}.strip>div:last-child{border-right:0}
.strip h4{font-family:Geist;font-weight:500;font-size:20px;margin-top:10px}
.strip .on{position:relative}.strip .on:before{content:'';position:absolute;left:0;top:-1px;width:64px;height:2px;background:var(--yel)}
.dark .strip{border-color:rgba(234,234,233,.4)}.dark .strip>div{border-color:var(--drule)}
'''
def hero(mode):
    dk=mode=='dark'
    logo='rp-left-light.svg' if dk else 'rp-left-dark.svg'
    rib='rbd-hero.png' if dk else 'rbl-hero.png'
    m2='var(--dmute)' if dk else 'var(--mute)'
    caps=[('01','Strategy','Positioning, digital strategy and account-based planning.'),('02','Marketing','Launches, campaigns and HubSpot automation.'),('03','Design','Brand, packaging, product content and UX.'),('04','Development','Websites, ecommerce, CRM and integrations.')]
    s=f'''<body class="{'dark' if dk else ''}"><div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface · {'Dark' if dk else 'Light'} mode</span><span class="r">Capabilities — <b>Hero</b></span></div>
<div class="hero"><img class="rib" src="{rib}">
<header><img src="{logo}"><nav><span>Capabilities</span><span>Work</span><span>Approach</span><span>About</span><span>Insights</span></nav><a class="btn b1 cta">Talk to Walter <i></i></a></header>
<div class="tx"><div class="mono" style="color:{m2}">Home / <span style="color:{'var(--text)' if dk else 'var(--ink)'}">Capabilities</span></div>
<div class="lab mono" style="margin-top:44px">For life-science companies</div>
<div class="disp" style="font-size:88px;line-height:.96">One team for<br>life-science brands.</div>
<p style="margin-top:28px;max-width:610px;font-size:19px">Strategy, marketing, design and development under one roof for pharma, biotech, med-device, CRO and lab-supply companies. Enterprise-ready process, and a founder who picks up the phone.</p>
<div style="display:flex;gap:16px;margin-top:38px;align-items:center"><a class="btn b1">Talk to Walter <i></i></a><a class="btn b2">See selected work</a></div></div>
<div class="strip">'''
    for i,(n,t,d) in enumerate(caps):
        s+=f'<div class="{"on" if i==0 else ""}"><span class="mono" style="color:{"var(--sky)" if dk else "var(--deep)"}">{n}</span><h4>{t}</h4><p class="small" style="margin-top:8px">{d}</p></div>'
    s+='</div></div>'+TAIL
    return head(HCSS)+s
open('hero-light.html','w').write(hero('light')); open('hero-dark.html','w').write(hero('dark'))

PCSS=HCSS+'''
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:56px;position:relative}
.cd{background:var(--card);border:1px solid var(--rule);position:relative}
.cd .ri{aspect-ratio:4/5;overflow:hidden;border-bottom:1px solid var(--rule);background:var(--base)}.cd .ri img{width:100%;height:100%;object-fit:cover}
.cd.hov{border-color:var(--deep);transform:translateY(-8px);box-shadow:0 8px 0 rgba(19,22,38,.06)}
.cd.hov:before{content:'';position:absolute;left:-1px;right:-1px;top:-1px;height:3px;background:var(--yel);z-index:2}
.callout{position:absolute;top:-36px;color:var(--deep)}
.split{display:grid;grid-template-columns:7fr 5fr;background:var(--paper2)}
.split .m{position:relative;min-height:720px;overflow:hidden}.split .m img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 50%}
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:320px 320px;gap:24px;margin-top:56px}
.bt{background:var(--card);border:1px solid var(--rule);position:relative;overflow:hidden;padding:28px}
.bt.img{padding:0}.bt.img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.tagl{position:absolute;left:20px;bottom:18px;right:20px;display:flex;justify-content:space-between}
.chip{background:var(--paper);color:var(--ink);padding:5px 8px}.chipd{background:rgba(13,15,26,.86);color:var(--text);padding:5px 8px}
.ph{border:1px dashed var(--deep);background:transparent}
blockquote{font-family:Philosopher;font-size:42px;line-height:1.22;color:var(--text)}
.ar{width:52px;height:52px;border:1px solid rgba(234,234,233,.5);display:inline-flex;align-items:center;justify-content:center;border-radius:50%;font-size:18px}
.ctab{position:relative;overflow:hidden;padding:128px 112px 128px;min-height:720px;border-top:1px solid var(--rule2)}
footer{padding:30px 112px 36px;display:flex;align-items:center;gap:40px;border-top:1px solid var(--rule2)}footer .mono{color:var(--mute)}
'''
p=head(PCSS)+'<body><div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface · Light mode</span><span class="r">Capabilities page — <b>Cards · Media + text · Bento · Quote · CTA + footer</b></span></div>'
# cards
p+='''<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/10"><div class="lab mono">02 — Capabilities</div><div class="disp" style="font-size:68px">Everything a launch needs,<br>in one team</div></div>
<div style="grid-column:10/13"><p class="small">Four disciplines, one team, one plan. Each card links to the capability page; the images show the kind of work behind it.</p></div></div><div class="cards">'''
cards=[('05-strategy-session','01','Strategy','Positioning, digital strategy and account-based planning for complex buying groups.',['Business challenge definition','Account-based planning'],'dl',''),
('07-launch-booth','02','Marketing','Product launches, campaigns and HubSpot automation built around the buyer journey.',['Launch campaigns','Marketing automation'],'tl',' hov'),
('L3-proofs-white','03','Design','Brand systems, packaging, product content and UX that hold up in regulated markets.',['Packaging and labelling','Product photography'],'dl',''),
('01-ecomm-product-page','04','Development','HubSpot CMS sites, ecommerce storefronts, CRM and the integrations between them.',['Websites and ecommerce','CRM and integrations'],'dl','')]
for f,n,t,d,li,lk,hv in cards:
    p+=f'<div class="cd{hv}"><div class="ri"><img src="{f}.png" style="object-position:{"62%" if f.startswith(("05","07","01")) else "50%"} 50%"></div><div style="padding:24px 24px 30px"><span class="mono" style="color:{"var(--deep)" if hv else "var(--mute2)"}">{n}</span><h3 style="margin-top:10px">{t}</h3><p class="small" style="margin-top:10px">{d}</p><div class="rt" style="margin-top:18px">'+''.join(f'<div class="row small" style="padding:9px 0;color:var(--ink)">{x}</div>' for x in li)+f'</div><a class="{lk}" style="display:inline-block;margin-top:20px">{t} →</a></div></div>'
p+='<span class="callout mono" style="left:calc(25% + 6px)">Hover — lift 8px, Deep Blue border, yellow hot edge</span></div><div class="cap mono" style="margin-top:28px"><span>Fig. 02 — Dark photos sit as contained windows; light-ground shots (03) sit flush with paper</span><span>Default · Hover · Default · Default</span></div></section>'
# media + text
p+='''<div class="split"><div class="m"><img src="L1-kit-white.png"><div class="cap mono" style="position:absolute;left:112px;bottom:28px;right:32px;margin:0"><span>Fig. 03 — Concept image (generated) · replace with project photography</span></div></div>
<div style="padding:104px 112px 96px 72px"><div class="lab mono">03 — Selected work</div><div class="mono" style="color:var(--mute2);margin-top:-12px;margin-bottom:22px">Placeholder — approved project goes here</div>
<div class="disp" style="font-size:60px">Packaging and product content</div>
<p style="margin-top:24px">From the carton system to catalog photography and the product page, one team keeps the product looking the same in every place a buyer meets it.</p>
<div class="rt" style="margin-top:30px">
<div class="row small" style="grid-template-columns:110px 1fr;color:var(--ink)"><span class="mono" style="color:var(--mute2)">Client</span><span>Client name pending approval</span></div>
<div class="row small" style="grid-template-columns:110px 1fr;color:var(--ink)"><span class="mono" style="color:var(--mute2)">Scope</span><span>Packaging · photography · product pages</span></div>
<div class="row small" style="grid-template-columns:110px 1fr;color:var(--ink)"><span class="mono" style="color:var(--mute2)">Result</span><span>Approved outcome goes here</span></div></div>
<div style="margin-top:34px"><a class="dl">Read the case study →</a></div></div></div>'''
# bento
p+='''<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/9"><div class="lab mono">04 — Selected work</div><div class="disp" style="font-size:68px">The work, across the range</div></div>
<div style="grid-column:9/13"><p class="small">Every tile is a placeholder for an approved project. No client names or numbers until they are cleared.</p></div></div>
<div class="bento"><div class="bt img" style="grid-column:1/3;grid-row:1/3;background:var(--paper)"><img src="L2-device-white.png" style="object-position:50% 70%"><div class="tagl mono"><span class="chip">Design · Med-device launch</span><span class="chip">Placeholder</span></div></div>
<div class="bt img" style="grid-column:3/5;grid-row:1/2;background:var(--base)"><img src="10-content-production.png" style="object-position:60% 50%"><div class="tagl mono"><span class="chipd">Content production</span><span class="chipd">Placeholder</span></div></div>
<div class="bt ph" style="grid-column:3/4;grid-row:2/3;display:flex;flex-direction:column;justify-content:space-between"><span class="mono" style="color:var(--deep)">Result — placeholder</span><div><div class="disp" style="font-size:56px;color:var(--deep)">— —</div><p class="small" style="margin-top:8px;color:var(--deep)">An approved, sourced client result goes here.</p></div></div>
<div class="bt dark" style="grid-column:4/5;grid-row:2/3;background:var(--base);border-color:var(--base)"><span class="mono" style="color:var(--dmute)">Who we work with</span><div class="rt" style="margin-top:16px">'''+''.join(f'<div class="row small" style="padding:8px 0;color:var(--text)">{x}</div>' for x in ['Pharma','Biotech','Medical devices','CROs','Lab supply and reagents'])+'''</div></div></div>
<div class="cap mono" style="margin-top:28px"><span>Fig. 04 — Bento: one light-ground hero tile, one dark window, a placeholder stat, one ink tile</span><span>Capabilities / Work</span></div></section>'''
# quote dark band
p+='''<section class="sec dark" style="padding:112px 112px 120px"><img src="rb-top.png" style="position:absolute;right:-470px;top:-110px;width:820px">
<div class="g" style="position:relative;z-index:2"><div style="grid-column:1/4"><div class="lab mono">05 — Client words</div><div class="mono" style="color:var(--dmute2);margin-top:8px">Testimonial 01 / 02</div></div>
<div style="grid-column:4/11"><div style="width:56px;height:2px;background:var(--yel);margin-bottom:34px"></div>
<blockquote>“Walter and team have been my go-to for all things HubSpot and web development across multiple companies. From Psomagen to 9amHealth, his custom theme builds were clean, reliable, and built with scalability in mind. His work at Kean and BLIP also showed his strength in complex integrations — he delivers not just code, but confidence.”</blockquote>
<div class="rt" style="margin-top:48px;display:grid;grid-template-columns:1fr auto;align-items:center;padding-top:18px">
<div><div style="font-weight:500">Client testimonial</div><div class="mono" style="color:var(--dmute);margin-top:6px">Shared by Walter Lentfert, June 2025 · Name and title pending approval</div></div>
<div style="display:flex;gap:12px;align-items:center"><span class="mono" style="color:var(--dmute);margin-right:12px"><b style="color:var(--text)">01</b> / 02</span><a class="ar" style="color:#8C90A3;border-color:#2a2e44">←</a><a class="ar" style="background:var(--text);color:var(--base);border-color:var(--text)">→</a></div></div></div></div></section>'''
# cta + footer
p+='''<div class="ctab"><img src="rbl-alt.png" style="position:absolute;left:560px;top:-80px;width:1160px">
<div style="position:relative;z-index:2"><div class="lab mono">06 — Start here</div>
<div class="disp" style="font-size:132px;line-height:.92">Let’s talk.</div>
<p style="font-size:21px;max-width:520px;margin-top:30px">Bring the business challenge. You will speak with Walter, the founder, not a sales queue, and leave with a clear next step.</p>
<div style="margin-top:42px;display:flex;gap:32px;align-items:center"><a class="btn b1" style="height:60px;padding:0 30px;font-size:16px">Book a call with Walter <i></i></a><a class="tl">Or send a brief by email</a></div>
<div class="mono" style="margin-top:72px;color:var(--mute);display:flex;gap:40px"><span>Wilmington, NC</span><span>English &amp; Nederlands</span><span>Since 2008</span></div></div></div>
<footer><img src="rp-left-dark.svg" style="height:28px"><span class="mono">© 2026 Razor Profiles LLC</span><span class="mono">Wilmington, NC</span>
<span style="margin-left:auto;display:flex;gap:32px"><a class="mono">Privacy</a><a class="mono">Terms</a><a class="mono">Accessibility</a><a class="mono">LinkedIn</a></span></footer>'''+TAIL
open('page.html','w').write(p)
