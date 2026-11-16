from common import *
sys.path.insert(0,'/workspace/razor-profiles/round-2/shared'); from contrast import cr
W=1600
css='''html,body{width:1600px}
.bb{padding:64px 80px 80px}
.top{display:flex;align-items:flex-end;justify-content:space-between;border-bottom:3px solid var(--ink);padding-bottom:26px}
.top h1{font-size:92px}
.sec{margin-top:56px}
.sh{display:flex;align-items:baseline;gap:18px;margin-bottom:22px}
.sh h2{white-space:nowrap;font-family:Bricolage;font-stretch:85%;font-weight:700;font-size:30px;letter-spacing:-.01em}
.sh span{font-size:14px;color:var(--slate)}
.g{display:grid;gap:20px}
.card{background:#fff;border:1px solid var(--line);padding:26px;position:relative}
.cap{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--slate);margin-bottom:14px;font-family:Bricolage;font-stretch:90%}
.sw{height:200px;padding:18px;display:flex;flex-direction:column;justify-content:flex-end;font-size:13px;line-height:1.4}
.sw b{font-family:Bricolage;font-stretch:85%;font-size:21px;font-weight:700;display:block}
.sw .hx{font-weight:600;font-size:15px;letter-spacing:.02em}
.roles{margin-top:12px;font-size:13px;line-height:1.45;color:var(--slate)}
.bar{display:flex;height:64px;margin-top:22px}
.bar div{display:flex;align-items:flex-end;padding:8px 10px;font-size:12px;font-weight:600}
.spec td{padding:10px 14px 10px 0;border-bottom:1px solid var(--line);font-size:14px;vertical-align:baseline}
.spec td:first-child{color:var(--slate);width:150px;font-weight:600}
'''
def sw(name,hx,fg,role,pairs):
    c=' · '.join(f'{lab} {cr(a,b):.1f}:1' for lab,a,b in pairs)
    return f'<div><div class="sw cut" style="background:{hx};color:{fg};{"box-shadow:inset 0 0 0 1px var(--line)" if hx in ("#F7F9FC","#E4EBF4") else ""}"><b>{name}</b><span class="hx">{hx}</span></div><div class="roles"><b style="color:var(--ink)">{role}</b><br>{c}</div></div>'
pal=''.join([
 sw('Cut White','#F7F9FC','#0E1A33','Background',[('Ink on it','#0E1A33','#F7F9FC'),('Slate','#4A5872','#F7F9FC')]),
 sw('Frost','#E4EBF4','#0E1A33','Surface, cards, chips',[('Ink','#0E1A33','#E4EBF4'),('Slate','#4A5872','#E4EBF4')]),
 sw('Ink Navy','#0E1A33','#F7F9FC','Text, dark sections',[('White','#F7F9FC','#0E1A33')]),
 sw('Mark Navy','#003271','#fff','Primary CTA, colour fields, links',[('White on it','#FFFFFF','#003271'),('On white','#003271','#F7F9FC')]),
 sw('Sky','#28ABE2','#0E1A33','Fields, mark, decoration only on light',[('Ink on it','#0E1A33','#28ABE2'),('On white','#28ABE2','#F7F9FC')]),
 sw('Edge Yellow','#D6DF27','#0E1A33','CTA on navy, one highlight per screen',[('Ink on it','#0E1A33','#D6DF27'),('On navy','#D6DF27','#003271')]),
 sw('Slate','#4A5872','#fff','Secondary text, captions',[('On white','#4A5872','#F7F9FC')]),
])
bar=[('#F7F9FC','Cut White 50%',50,'#0E1A33'),('#E4EBF4','Frost 14%',14,'#0E1A33'),('#003271','Mark Navy 16%',16,'#fff'),('#28ABE2','Sky 9%',9,'#0E1A33'),('#0E1A33','Ink 7%',7,'#fff'),('#4A5872','Slate 2%',2,'#fff'),('#D6DF27','Yellow 2%',2,'#0E1A33')]
barh=''.join(f'<div style="flex:{p};background:{c};color:{f};{"box-shadow:inset 0 0 0 1px var(--line)" if c=="#F7F9FC" else ""}">{t if p>5 else ""}</div>' for c,t,p,f in bar)
orig=open('/workspace/razor-profiles/logo/rp-left-dark.svg').read().split('?>',1)[-1]
import re
orig=re.sub(r'<svg ','<svg height="56" ',orig,count=1)
body=f'''<div class="bb">
<div class="top"><div><div class="eyebrow">Razor Profiles · Round 2 · Direction 1</div><h1 class="d" style="margin-top:14px">Clean Cut</h1></div>
<p style="width:620px;font-size:17px;color:#26324d">The mark’s three swooshes become three flat bands separated by razor-thin cuts. Accuracy, speed and delight are the bands; taste is the cut, what we leave out. A bright, flat, cut-paper system: big colour planes, one chamfered corner, no gradients, no mono labels.</p></div>

<div class="sec"><div class="sh"><h2>The mark: an evolution, not a replacement</h2><span>Same silhouette and the same Philosopher wordmark paths from the live SVG. What changes: the raster gradient becomes three flat vector bands, cut at the three original overlap points.</span></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<div class="card"><div class="cap">Original (2024, gradient raster inside a vector clip)</div><div style="height:150px;display:flex;align-items:center;gap:40px"><img src="/workspace/razor-profiles/logo/rp-logo.png" style="height:120px">{orig}</div></div>
<div class="card"><div class="cap">Evolution: true vector, three flat bands, three razor cuts</div><div style="height:150px;display:flex;align-items:center;gap:40px">{symbol(size=120)}{lockup(height=56)}</div></div>
</div>
<div class="g" style="grid-template-columns:1.35fr 1fr 1fr;margin-top:20px">
<div class="card"><div class="cap">Clearspace: X on every side, where X = half the symbol height</div>
<div style="height:220px;display:flex;align-items:center;justify-content:center"><div style="position:relative;padding:34px 40px;outline:1.5px dashed var(--sky)"><div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(40,171,226,.13) 0 6px,transparent 6px 12px)"></div><div style="position:relative;background:var(--white);outline:1px solid var(--line)">{lockup(height=68)}</div>
<span style="position:absolute;left:4px;top:8px;font-size:11px;font-weight:700;color:var(--navy)">X</span><span style="position:absolute;right:12px;bottom:8px;font-size:11px;font-weight:700;color:var(--navy)">X</span></div></div>
<p style="font-size:13px;color:var(--slate)">Cuts are fixed angles through the original cusps (−48°, 9°, 167°) and scale with the mark: 0.9/32 of symbol height.</p></div>
<div class="card" style="background:var(--navy);border-color:var(--navy)"><div class="cap" style="color:#BFD0EA">On Mark Navy: bottom band turns Cut White</div><div style="height:220px;display:flex;align-items:center;justify-content:center">{lockup(height=46,word="#F7F9FC",bottom="#F7F9FC")}</div></div>
<div class="card" style="background:var(--sky);border-color:var(--sky)"><div class="cap" style="color:var(--ink)">On Sky: one-colour Ink, cuts kept</div><div style="height:220px;display:flex;align-items:center;justify-content:center">{lockup(height=46,word="#0E1A33",mode="mono",top="#0E1A33")}</div></div>
</div>
<div class="g" style="grid-template-columns:1fr 1fr 1.2fr;margin-top:20px">
<div class="card" style="background:var(--ink);border-color:var(--ink)"><div class="cap" style="color:#9fb0cc">Dark / one-colour reversed</div><div style="height:110px;display:flex;align-items:center;gap:30px">{lockup(height=40,word="#F7F9FC",bottom="#F7F9FC")}</div><div style="display:flex;align-items:center;gap:30px">{lockup(height=26,word="#F7F9FC",mode="mono",top="#F7F9FC")}</div></div>
<div class="card"><div class="cap">One-colour positive</div><div style="height:110px;display:flex;align-items:center">{lockup(height=40,mode="mono",top="#0E1A33")}</div><div>{lockup(height=26,mode="mono",top="#003271",word="#003271")}</div></div>
<div class="card"><div class="cap">Small sizes: cuts drop below 24 px</div><div style="display:flex;align-items:flex-end;gap:34px;height:150px">
<div style="text-align:center;font-size:12px;color:var(--slate)">{symbol(size=96)}<br>96</div><div style="text-align:center;font-size:12px;color:var(--slate)">{symbol(size=48)}<br>48</div><div style="text-align:center;font-size:12px;color:var(--slate)">{symbol(size=32,cut=1.4)}<br>32</div><div style="text-align:center;font-size:12px;color:var(--slate)">{symbol(size=24,cut=0)}<br>24</div><div style="text-align:center;font-size:12px;color:var(--slate)">{symbol(size=16,cut=0)}<br>16 favicon</div>
<div style="text-align:center;font-size:12px;color:var(--slate)"><div style="width:48px;height:48px;background:var(--navy);display:flex;align-items:center;justify-content:center;border-radius:10px">{symbol(size=34,bottom="#F7F9FC")}</div>app</div></div></div>
</div></div>

<div class="sec"><div class="sh"><h2>Colour</h2><span>Paired with WCAG 2.2 contrast ratios. Sky (2.5:1) and Yellow never carry text or controls on light backgrounds.</span></div>
<div class="g" style="grid-template-columns:repeat(7,1fr)">{pal}</div>
<div class="bar">{barh}</div>
<p style="font-size:13px;color:var(--slate);margin-top:8px">Usage ratio across a typical page. Colour arrives as whole planes (a Sky section, a Navy CTA band), never as gradients or tints. Yellow is the one hot spot per screen.</p></div>

<div class="sec"><div class="sh"><h2>Type</h2><span>Both Google Fonts (OFL), self-hosted. No mono: labels are Bricolage caps.</span></div>
<div class="g" style="grid-template-columns:1.25fr 1fr">
<div class="card"><div class="cap">Display — Bricolage Grotesque 700, width 78, opsz 96, −2.5%</div>
<div class="d" style="font-size:112px">Cut to fit.</div><div class="d" style="font-size:76px;margin-top:10px;color:var(--navy)">Precise by design.</div>
<div style="font-family:Bricolage;font-stretch:85%;font-weight:650;font-size:28px;margin-top:16px">H3 · Website development on HubSpot CMS</div>
<div class="eyebrow" style="margin-top:18px">Label · Bricolage 600 · 13 px · caps +12%</div></div>
<div class="card"><div class="cap">Body — Instrument Sans 400/600</div>
<p class="lead">Lead 20/30. We plan, design and build enterprise websites, CRM and e-commerce with AI in every step.</p>
<p style="margin-top:16px">Body 17/26. From the first brief to launch, one team carries the work through analysis, scope, design and build, so nothing is lost in a hand-off. Walter stays your point of contact the whole way.</p>
<table class="spec" style="margin-top:20px;border-collapse:collapse;width:100%">
<tr><td>H1</td><td>Bricolage 700 · 120/113 · w78</td></tr><tr><td>H2</td><td>Bricolage 700 · 76/72 · w78</td></tr><tr><td>H3</td><td>Bricolage 650 · 28/30 · w85</td></tr><tr><td>Body / small</td><td>Instrument Sans 400 · 17/26 · 14/21</td></tr><tr><td>Buttons</td><td>Instrument Sans 600 · 16</td></tr></table></div></div></div>

<div class="sec"><div class="sh"><h2>Shape &amp; UI</h2><span>The one motif: a single 45° chamfer on the top-right corner, taken from the mark’s top-right cut. Never rounded, never on more than one corner.</span></div>
<div class="g" style="grid-template-columns:1.4fr 1fr">
<div class="card" style="display:flex;gap:22px;align-items:center;flex-wrap:wrap"><a class="btn p">Talk to Walter <span class="ar">→</span></a><a class="btn s">See how we build</a><a class="tl">Read the case</a><span class="chip"><i style="background:var(--sky)"></i>HubSpot CMS</span>
<div style="background:var(--navy);padding:20px;display:flex;gap:20px;align-items:center;width:100%"><a class="btn y">Book 30 minutes with Walter <span class="ar">→</span></a><span style="color:#fff;font-weight:600;border-bottom:2px solid var(--yel)">Or email the team</span></div></div>
<div class="card" style="display:flex;gap:18px;align-items:flex-end"><div class="cut" style="--cut:40px;width:150px;height:150px;background:var(--sky)"></div><div class="cut" style="--cut:28px;width:120px;height:120px;background:var(--navy)"></div><div class="cut" style="--cut:14px;width:70px;height:70px;background:var(--yel)"></div><p style="font-size:13px;color:var(--slate)">Chamfer: 28 px on cards, 14 px on buttons, 40 px on full-bleed planes.</p></div>
</div></div>
</div>'''
open('brand-board.html','w').write(page(body,css))
