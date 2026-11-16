from common import *
css='''
.hero{display:grid;grid-template-columns:1fr 600px;gap:56px;padding:72px 64px 0;height:800px;position:relative}
.hero h1{font-size:140px;margin:34px 0 34px}
.hero .lead{width:620px}
.ctas{display:flex;gap:16px;margin-top:40px}
.con{align-self:start;overflow:hidden}
.con .hd{display:flex;align-items:center;gap:14px;padding:16px 20px;border-bottom:1px solid var(--line)}
.con .hd .ring{margin-left:auto}
.stg{display:grid;grid-template-columns:28px 1fr auto;gap:12px;padding:11px 20px;border-bottom:1px solid var(--line);align-items:start}
.stg b{font-weight:700;font-size:16px;display:block}
.stg p{font-size:13px;color:var(--mut);line-height:1.45;margin-top:2px}
.stg .t{font-family:ChivoMono;font-size:12px;color:var(--mut);white-space:nowrap;padding-top:3px}
.stg .ic{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;margin-top:1px}
.stg.done .ic{background:var(--hv);color:var(--g0)}
.stg.now{background:#20241C}
.stg.now .ic{box-shadow:inset 0 0 0 2px var(--sky)}
.stg.now .ic:after{content:"";width:8px;height:8px;border-radius:50%;background:var(--sky)}
.stg.todo .ic{box-shadow:inset 0 0 0 1.5px #5A6150}
.stg.todo b{color:var(--mut)}
.bar{height:6px;background:var(--g2);border-radius:3px;margin-top:10px;overflow:hidden}
.bar i{display:block;height:100%;width:75%;background:var(--sky)}
.chk{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line)}
.chk div{padding:12px 20px;border-right:1px solid var(--line)}
.chk div:last-child{border:0}
.chk b{display:block;font-size:20px;font-weight:800;margin-top:4px}
.foot{padding:10px 20px;color:#7E8475}
.tick{position:absolute;left:0;right:0;bottom:0;height:92px;border-top:1px solid var(--line);display:grid;grid-template-columns:repeat(4,1fr)}
.tick div{padding:20px 0 0 64px;border-right:1px solid var(--line)}
.tick div+div{padding-left:28px}
.tick b{display:block;font-size:17px;font-weight:700;margin-top:4px;color:var(--txt);text-transform:none;letter-spacing:0;font-family:Chivo}
'''
st=[('done','01','Brief','A 45-minute call with Walter. Goals, audience, constraints.','Mon 09:30'),
('done','02','Spec','Sitemap and scope drafted by AI, cut and signed off by a strategist.','Tue 16:10'),
('done','03','Design','Three layout directions generated, one chosen and refined by a designer.','Thu 11:45'),
('now','04','Build','HubSpot CMS theme, 18 of 24 modules merged. Engineer reviews every line.','running'),
('todo','05','QA','WCAG 2.2 AA, forms, redirects, CRM sync.','next')]
rows=''.join(f'<div class="stg {s}"><span class="ic">{"✓" if s=="done" else ""}</span><div><b>{n} · {t}</b><p>{p}</p>{"<div class=bar><i></i></div>" if s=="now" else ""}</div><span class="t {"run" if tm=="running" else ""}">{tm}</span></div>' for s,n,t,p,tm in st)
body=header()+'''<div class="crumb mono"><span>Home</span><span>/</span><b>How we build</b><span style="margin-left:auto">Wilmington, NC · since 2008 · EN / NL</span></div>
<section class="hero"><div>
<div class="mono k">AI-first digital agency · HubSpot · CRM · E-commerce</div>
<h1 class="d">Brief in.<br><span class="hv">Build live.</span></h1>
<p class="lead">One conversation with Walter becomes a working website, CRM or store, shipped in short loops you can watch. AI drafts at every step. A named person checks and signs off every step.</p>
<div class="ctas"><a class="btn p">Start a build with Walter <span>→</span></a><a class="btn s">Read a build log</a></div>
</div>
<div class="con panel"><div class="hd"><span class="mono" style="color:var(--txt)">Build 0142</span><span class="mono mut">Website redesign · HubSpot CMS</span><span class="ring">'''+symbol(size=34,**MK)+'''</span></div>
'''+rows+'''<div class="chk mono"><div class="mut">Human sign-offs<b class="ok">3 / 3</b></div><div class="mut">Accessibility<b>AA target</b></div><div class="mut">Status<b class="run">On plan</b></div></div>
<div class="foot mono">Illustrative build log · not client data</div></div>
<div class="tick mono"><div class="mut">Accuracy<b>Every AI output signed by a person</b></div><div class="mut">Speed<b>Short loops, visible every day</b></div><div class="mut">Taste<b>Senior designers make the call</b></div><div class="mut">Delight<b>Details people notice, then use</b></div></div>
</section>'''
open('hero.html','w').write(page(body,css))
