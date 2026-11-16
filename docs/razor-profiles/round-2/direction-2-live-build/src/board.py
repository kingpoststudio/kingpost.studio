from common import *
sys.path.insert(0,'/workspace/razor-profiles/round-2/shared'); from contrast import cr
import re
css='''html,body{width:1600px}
.bb{padding:60px 72px 80px}
.top{display:flex;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:28px}
.top h1{font-size:104px}
.sec{margin-top:52px}
.sh{display:flex;align-items:baseline;gap:20px;margin-bottom:20px}
.sh h2{font-weight:800;font-size:30px;letter-spacing:-.02em;white-space:nowrap}
.sh span{font-size:14px;color:var(--mut)}
.g{display:grid;gap:16px}
.card{background:var(--g1);border:1px solid var(--line);border-radius:6px;padding:24px;position:relative}
.cap{font-family:ChivoMono;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin-bottom:14px}
.sw{height:190px;border-radius:6px;padding:16px;display:flex;flex-direction:column;justify-content:flex-end}
.sw b{font-weight:800;font-size:20px;display:block;letter-spacing:-.01em}
.sw .hx{font-family:ChivoMono;font-size:14px}
.roles{margin-top:10px;font-size:13px;line-height:1.45;color:var(--mut)}
.roles b{color:var(--txt)}
.bar{display:flex;height:60px;margin-top:20px;border-radius:6px;overflow:hidden;border:1px solid var(--line)}
.bar div{display:flex;align-items:flex-end;padding:8px 10px;font-family:ChivoMono;font-size:11px}
.spec td{padding:9px 14px 9px 0;border-bottom:1px solid var(--line);font-size:14px}
.spec td:first-child{color:var(--mut);width:140px;font-family:ChivoMono;font-size:12px;text-transform:uppercase}
.st{display:flex;flex-direction:column;align-items:center;gap:10px;font-family:ChivoMono;font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.06em}
'''
def sw(name,hx,fg,role,pairs,border=False):
    c=' · '.join(f'{lab} {cr(a,b):.1f}:1' for lab,a,b in pairs)
    return f'<div><div class="sw" style="background:{hx};color:{fg};{"box-shadow:inset 0 0 0 1px #3A4034" if border else ""}"><b>{name}</b><span class="hx">{hx}</span></div><div class="roles"><b>{role}</b><br>{c}</div></div>'
pal=''.join([
 sw('Graphite','#121410','#EEEEE6','Background',[('Signal on it','#EEEEE6','#121410'),('Fog','#A3A898','#121410')],True),
 sw('Panel','#1B1E18','#EEEEE6','Surface, cards, console',[('Signal','#EEEEE6','#1B1E18'),('Fog','#A3A898','#1B1E18')],True),
 sw('Raised','#262A22','#EEEEE6','Hover, active row, inputs',[('Signal','#EEEEE6','#262A22')],True),
 sw('Rule','#33382E','#EEEEE6','1 px borders, dividers',[('Decorative only','#33382E','#121410')],True),
 sw('Signal','#EEEEE6','#121410','Text, mark body, light mode bg',[('On Graphite','#EEEEE6','#121410')]),
 sw('Fog','#A3A898','#121410','Secondary text, mono labels',[('On Graphite','#A3A898','#121410')]),
 sw('Hi-Vis','#D6DF27','#121410','Primary CTA, done state, the live band',[('Graphite on it','#121410','#D6DF27'),('On Graphite','#D6DF27','#121410')]),
 sw('Run Sky','#5CC6F0','#121410','In-progress state, links',[('On Graphite','#5CC6F0','#121410'),('On Panel','#5CC6F0','#1B1E18')]),
])
bar=[('#121410','Graphite 58%',58,'#EEEEE6'),('#1B1E18','Panel 18%',18,'#EEEEE6'),('#262A22','Raised 4%',4,'#EEEEE6'),('#EEEEE6','Signal 11%',11,'#121410'),('#A3A898','Fog 3%',3,'#121410'),('#D6DF27','Hi-Vis 5%',5,'#121410'),('#5CC6F0','Sky 1%',1,'#121410')]
barh=''.join(f'<div style="flex:{p};background:{c};color:{f}">{t if p>=5 else ""}</div>' for c,t,p,f in bar)
orig=open('/workspace/razor-profiles/logo/rp-left-light.svg').read().split('?>',1)[-1]
orig=re.sub(r'<svg ','<svg height="52" ',orig,count=1)
def frame(lit,label):
    c=dict(top='#3E4437',bottom='#3E4437',lobe='#3E4437',cut=0.5)
    for k in lit: c[k]='#D6DF27'
    return f'<div class="st">{symbol(size=96,**c)}{label}</div>'
body=f'''<div class="bb">
<div class="top"><div><div class="mono k">Razor Profiles · Round 2 · Direction 2</div><h1 class="d" style="margin-top:16px">Live Build</h1></div>
<p style="width:640px;font-size:17px;color:#D3D5CA">An AI-first agency that works in the open. The site borrows the grammar of a build pipeline (stages, checks, sign-offs, timestamps) so speed and accuracy are shown, not claimed. The mark becomes a status ring: one band lights up for the stage you are in.</p></div>

<div class="sec"><div class="sh"><h2>The mark: same ring, now a status light</h2><span>Real silhouette and Philosopher wordmark paths from the live SVG. The gradient raster goes; the ring becomes one solid colour with one live band in Hi-Vis.</span></div>
<div class="g" style="grid-template-columns:1fr 1fr">
<div class="card"><div class="cap">Original 2024 (light version, gradient raster in a vector clip)</div><div style="height:140px;display:flex;align-items:center;gap:40px"><img src="/workspace/razor-profiles/logo/rp-logo.png" style="height:112px">{orig}</div></div>
<div class="card"><div class="cap">Evolution: true vector, one colour, the lobe is the live band</div><div style="height:140px;display:flex;align-items:center;gap:40px">{symbol(size=112,**MK)}{lockup(height=52,word="#EEEEE6",**MK)}</div></div></div>
<div class="g" style="grid-template-columns:1.5fr 1fr;margin-top:16px">
<div class="card"><div class="cap">Status states (motion: the light travels band to band, then rests on the lobe)</div><div style="display:flex;justify-content:space-around;padding:10px 0 4px">{frame(["top"],"01 Strategy")}{frame(["lobe"],"02 Build")}{frame(["bottom"],"03 Run")}{frame(["top","lobe","bottom"],"Live / done")}</div>
<p style="font-size:13px;color:var(--mut);margin-top:14px">In motion only: hairline 0.5/32 seams appear between bands. The resting logo is always the lobe-lit version.</p></div>
<div class="card"><div class="cap">Clearspace: X on every side, X = half the ring height</div><div style="height:200px;display:flex;align-items:center;justify-content:center"><div style="position:relative;padding:30px 36px;outline:1px dashed #6B7260;background:repeating-linear-gradient(45deg,rgba(214,223,39,.08) 0 6px,transparent 6px 12px)"><div style="background:var(--g0);outline:1px solid var(--line)">{lockup(height=60,word="#EEEEE6",**MK)}</div><span class="mono" style="position:absolute;left:6px;top:6px;font-size:10px" >X</span></div></div></div></div>
<div class="g" style="grid-template-columns:1fr 1fr 1fr 1.25fr;margin-top:16px">
<div class="card" style="background:#EEEEE6;border-color:#EEEEE6"><div class="cap" style="color:#4B5044">Light mode (long reads)</div><div style="height:100px;display:flex;align-items:center">{lockup(height=38,word="#121410",top="#121410",bottom="#121410",lobe="#A9B200",cut=0)}</div><p style="font-size:12px;color:#4B5044">Lobe darkens to #A9B200 on light so it holds 3:1 as a graphic.</p></div>
<div class="card" style="background:var(--hv);border-color:var(--hv)"><div class="cap" style="color:#121410">On Hi-Vis: one colour</div><div style="height:100px;display:flex;align-items:center">{lockup(height=38,word="#121410",mode="mono",top="#121410",cut=0)}</div></div>
<div class="card"><div class="cap">One colour, reversed</div><div style="height:100px;display:flex;align-items:center">{lockup(height=38,word="#EEEEE6",mode="mono",top="#EEEEE6",cut=0)}</div></div>
<div class="card"><div class="cap">Small sizes</div><div style="display:flex;align-items:flex-end;gap:30px;height:110px">
<div class="st">{symbol(size=64,**MK)}64</div><div class="st">{symbol(size=32,**MK)}32</div><div class="st">{symbol(size=20,**MK)}20</div><div class="st">{symbol(size=16,mode="mono",top="#EEEEE6",cut=0)}16 mono</div>
<div class="st"><div style="width:44px;height:44px;border-radius:9px;background:var(--hv);display:flex;align-items:center;justify-content:center">{symbol(size=30,mode="mono",top="#121410",cut=0)}</div>app</div></div></div></div></div>

<div class="sec"><div class="sh"><h2>Colour</h2><span>Dark-first, graphite rather than navy. Hi-Vis is the brand’s Urgent Yellow, promoted to the CTA and every “done” state.</span></div>
<div class="g" style="grid-template-columns:repeat(8,1fr)">{pal}</div>
<div class="bar">{barh}</div>
<p style="font-size:13px;color:var(--mut);margin-top:8px">Usage ratio on a typical page. Status colour has meaning: Hi-Vis = done / act, Run Sky = in progress. Never decorative glows, never gradients.</p></div>

<div class="sec"><div class="sh"><h2>Type</h2><span>One family, two voices: Chivo (Omnibus-Type, OFL) for display and body, Chivo Mono for data, labels and the build log.</span></div>
<div class="g" style="grid-template-columns:1.3fr 1fr">
<div class="card"><div class="cap">Display · Chivo 800 · −3.5% · leading 0.95</div>
<div class="d" style="font-size:120px">Brief in.</div><div class="d hv" style="font-size:72px;margin-top:6px">Build live.</div>
<div style="font-weight:700;font-size:24px;margin-top:18px;letter-spacing:-.015em">H3 · Chivo 700 — CRM implementation &amp; migration</div>
<div class="mono" style="margin-top:16px;color:var(--mut)">Chivo Mono 500 · 12 px · caps +6% · Build 0142 · ✓ signed off · Tue 16:10</div></div>
<div class="card"><div class="cap">Body · Chivo 400 / 700</div>
<p class="lead">Lead 20/30. One conversation with Walter becomes a working website, CRM or store.</p>
<p style="margin-top:14px;color:#D3D5CA">Body 17/26. AI drafts at every step. A named person checks and signs off every step, so you get speed without losing accuracy.</p>
<table class="spec" style="margin-top:18px;border-collapse:collapse;width:100%"><tr><td>H1</td><td>Chivo 800 · 140/133</td></tr><tr><td>H2</td><td>Chivo 800 · 72/68</td></tr><tr><td>H3</td><td>Chivo 700 · 24/28</td></tr><tr><td>Body</td><td>Chivo 400 · 17/26</td></tr><tr><td>Data</td><td>Chivo Mono 500 · 12–14</td></tr></table></div></div></div>

<div class="sec"><div class="sh"><h2>UI grammar</h2><span>4 px radii, 1 px rules, status dots. Every module can show a state.</span></div>
<div class="g" style="grid-template-columns:1.3fr 1fr">
<div class="card" style="display:flex;gap:16px;align-items:center;flex-wrap:wrap"><a class="btn p">Start a build with Walter →</a><a class="btn s">Read a build log</a><a class="tl">See the case</a>
<span class="mono" style="display:flex;gap:18px;width:100%;margin-top:8px"><span><i class="dot" style="background:var(--hv)"></i> Done</span><span><i class="dot" style="background:var(--sky)"></i> Running</span><span><i class="dot" style="box-shadow:inset 0 0 0 1.5px #5A6150"></i> Queued</span><span class="mut">✓ Human sign-off</span></span></div>
<div class="card"><div style="display:flex;align-items:center;gap:12px;background:var(--g0);border:1px solid #5A6150;border-radius:4px;padding:14px 16px"><span class="hv" style="font-family:ChivoMono">›</span><span style="color:var(--mut)">Tell Walter what you’re building…</span><span class="mono" style="margin-left:auto;background:var(--g2);padding:3px 6px;border-radius:3px">Enter</span></div>
<div style="height:6px;background:var(--g2);border-radius:3px;margin-top:20px"><i style="display:block;height:6px;width:62%;background:var(--sky);border-radius:3px"></i></div><div class="mono mut" style="margin-top:8px">Progress bar · Run Sky</div></div></div></div>
</div>'''
open('brand-board.html','w').write(page(body,css))
