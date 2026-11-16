from common import *
import os
os.makedirs('modules',exist_ok=True)
MCSS='''.spec{height:44px;display:flex;align-items:center;padding:0 64px;border-bottom:1px solid var(--line);color:var(--mut)}
.spec .r{margin-left:auto;color:var(--txt)}
.m{padding:84px 64px 92px;position:relative}
.g12{display:grid;grid-template-columns:repeat(12,1fr);column-gap:24px}
.hd{display:grid;grid-template-columns:repeat(12,1fr);column-gap:24px;align-items:end;margin-bottom:56px}
'''
def mod(n,name,body,css=''):
    spec=f'<div class="spec mono">Razor Profiles · Direction 2 — Live Build<span class="r">Module {n:02d} / 10 — {name}</span></div>'
    slug=f'{n:02d}-'+name.lower().replace(' + ','-').replace(' ','-').replace('’','')
    open(f'modules/{slug}.html','w').write(page(spec+body,MCSS+css).replace('url(fonts/','url(../fonts/').replace('src="img/','src="../img/'))
    return slug
def H(k,h,p=''):
    return f'<div class="hd"><div style="grid-column:1/8"><div class="mono k">{k}</div><h2 class="d" style="margin-top:22px">{h}</h2></div><p class="lead" style="grid-column:8/13">{p}</p></div>'
S=[]
# 01 Build log timeline
ev=[('Day 1','Brief','Walter','45-minute call. Business challenge, audience, constraints, budget.','AI transcribes and structures the brief','Walter agrees the brief with you','done'),
('Day 2','Spec','Strategist','Current &amp; competitor analysis, sitemap, scope.','AI drafts the sitemap and audits competitors','Strategist cuts it to what matters; you sign','done'),
('Day 4','Design','Designer','Wireframes, then design from a tested module library.','AI generates layout and copy options','Designer chooses, edits and owns the result','done'),
('Week 2','Build','Engineer','HubSpot CMS theme, CRM and commerce integrations.','AI writes and tests code alongside engineers','Engineer reviews every line before merge','run'),
('Week 3','QA &amp; launch','Team','WCAG 2.2 AA, forms, redirects, CRM sync, analytics.','AI runs accessibility and regression checks','Walter walks you through launch','todo')]
rows=''.join(f'''<div class="ev {s}"><div class="when mono">{w}</div><div class="node"><i></i></div><div class="what"><div style="display:flex;align-items:baseline;gap:14px"><h3>{t}</h3><span class="mono mut">Owner · {o}</span><span class="mono st">{ {"done":"✓ Signed off","run":"● Running","todo":"○ Queued"}[s]}</span></div><p>{d}</p>
<div class="lanes"><div><span class="mono">AI</span>{a}</div><div><span class="mono">Human</span>{h}</div></div></div></div>''' for w,t,o,d,a,h,s in ev)
S.append(mod(1,'Build log',f'''<section class="m">{H("How we build","Every step logged.<br><span class=hv>Every step signed.</span>","AI makes us fast. People make us right. Here is what a typical HubSpot website build looks like, step by step.")}
<div class="log">{rows}</div><p class="mono mut" style="margin-top:20px">Typical timeline for a mid-size website build · actual plans set in the written scope</p></section>''','''
.log{border-top:1px solid var(--line)}
.ev{display:grid;grid-template-columns:120px 48px 1fr;border-bottom:1px solid var(--line)}
.when{padding-top:30px;color:var(--mut)}
.node{position:relative}.node:before{content:"";position:absolute;left:23px;top:0;bottom:0;width:1px;background:var(--line)}
.node i{position:absolute;left:16px;top:30px;width:15px;height:15px;border-radius:50%;background:var(--g0);box-shadow:inset 0 0 0 1.5px #5A6150}
.ev.done .node i{background:var(--hv);box-shadow:none}.ev.run .node i{box-shadow:inset 0 0 0 2px var(--sky);background:radial-gradient(var(--sky) 0 3px,transparent 3.5px)}
.what{padding:24px 0 24px}
.what p{color:#D3D5CA;margin-top:6px;font-size:16px}
.st{margin-left:auto}.done .st{color:var(--hv)}.run .st{color:var(--sky)}.todo .st{color:var(--mut)}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.lanes div{background:var(--g1);border:1px solid var(--line);border-radius:4px;padding:12px 14px;font-size:14px;display:flex;gap:14px;align-items:baseline}
.lanes span{color:var(--mut);width:52px;flex:none}
.run .what{}
.ev.run{background:linear-gradient(90deg,transparent 0 168px,#171A14 168px)}
.todo h3{color:var(--mut)}'''))
# 02 Services index
sv=[('website-development','Website development','HubSpot CMS themes and modules, HubSpot + Algolia search, WCAG 2.2 AA.','HubSpot CMS',True),
('crm','CRM implementation &amp; migration','Move to HubSpot without losing a contact, a deal or a workflow.','Integrations',False),
('e-commerce','E-commerce &amp; integrations','Storefronts, checkouts and the back-end systems they talk to.','Commerce',False),
('strategy','Digital strategy &amp; ABM','Identify the challenge, prioritise by benefit and cost, plan it.','ABM',False),
('campaigns','Marketing campaigns','Inbound and outbound programmes, automated in HubSpot.','Automation',False),
('bespoke','Bespoke process development','When the off-the-shelf workflow doesn’t fit, we build the one that does.','Custom',False)]
li=''.join(f'<div class="sv {"on" if o else ""}"><span class="mono path">/services/{p}</span><h3>{t}</h3><p>{d}</p><span class="tag mono">{g}</span><span class="go">{"→" if o else "↗"}</span></div>' for p,t,d,g,o in sv)
S.append(mod(2,'Services index',f'''<section class="m">{H("Services","Six services.<br><span class=hv>One build team.</span>","Strategy, marketing, design and development under one roof, so you never manage a hand-off between shops.")}
<div class="svl">{li}</div>
<div class="prev panel"><img src="img/desk.jpg"><div class="pv"><span class="mono k">Preview · Website development</span><b>From briefing to a live HubSpot theme, with one team carrying the work end to end.</b><a class="btn p" style="height:44px;font-size:14px">Explore website development →</a></div></div></section>''','''
.svl{border-top:1px solid var(--line);width:62%}
.sv{display:grid;grid-template-columns:230px 1fr 120px 40px;grid-template-rows:auto auto;column-gap:24px;padding:20px 16px;border-bottom:1px solid var(--line);align-items:baseline}
.sv .path{grid-row:1/3;color:var(--mut);font-size:11.5px;padding-top:6px}
.sv h3{font-size:26px}.sv p{grid-column:2;color:var(--mut);font-size:15px;margin-top:4px}
.sv .tag{grid-row:1/3;grid-column:3;justify-self:start;background:var(--g2);padding:4px 8px;border-radius:3px;font-size:11px;color:#CFD1C6}
.sv .go{grid-row:1/3;grid-column:4;font-size:22px;color:var(--mut);justify-self:end}
.sv.on{background:var(--g1);box-shadow:inset 3px 0 0 var(--hv)}.sv.on .path{color:var(--hv)}.sv.on .go{color:var(--hv)}
.prev{position:absolute;right:64px;top:310px;width:470px;overflow:hidden}
.prev img{width:100%;height:270px;object-fit:cover;display:block}
.pv{padding:22px;display:flex;flex-direction:column;gap:14px}.pv b{font-size:20px;line-height:1.3}.pv .btn{align-self:flex-start}'''))
# 03 Case study build report
S.append(mod(3,'Case study',f'''<section class="m"><div class="rep panel">
<div class="rh"><div><span class="mono k">Build report · Kean</span><h2 class="d" style="font-size:68px;margin-top:18px">Deep backend systems,<br><span class="hv">wired into HubSpot.</span></h2></div>
<div class="rs mono"><div><span>Client</span>Kean</div><div><span>Scope</span>Backend systems · integrations</div><div><span>Platform</span>HubSpot CMS + custom</div><div><span>Status</span><b class="ok">✓ Live</b></div></div></div>
<div class="rb"><div class="col"><div class="mono" style="background:#2A2E22;color:var(--hv);padding:6px 10px;border-radius:3px;display:inline-block;margin-bottom:22px">Sample case copy · real details from Walter before publishing</div><div class="mono mut lab">Problem</div><p>Marketing ran on one system, operations on several others. Data moved by export and hope.</p>
<div class="mono mut lab" style="margin-top:28px">What we built</div><ul><li><i>✓</i>Integration layer between HubSpot and back-office systems</li><li><i>✓</i>CRM objects mapped to how the business actually works</li><li><i>✓</i>Automated QA on every sync</li></ul></div>
<div class="col"><div class="mono mut lab">Results</div><div class="mt"><div><b>—</b><span>Hours of manual export removed / month</span></div><div><b>—</b><span>Records synced without loss</span></div><div><b>—</b><span>Weeks, brief to live</span></div></div><p class="mono" style="color:#7E8475;margin-top:12px">Metric slots stay empty until Kean approves real numbers</p>
<blockquote>“…deep backend systems work at Kean, Walter consistently brings creative solutions, technical excellence, and a collaborative spirit.”<cite class="mono">Client testimonial · June 2025 · attribution pending approval</cite></blockquote></div></div>
<div class="rf"><span class="mono mut">Checks</span><span class="mono ok">✓ Scope signed</span><span class="mono ok">✓ Code reviewed</span><span class="mono ok">✓ Data reconciled</span><span class="mono ok">✓ Client sign-off</span><a class="btn p" style="margin-left:auto;height:44px;font-size:14px">Read the full report →</a></div></div></section>''','''
.rep{overflow:hidden}
.rh{display:grid;grid-template-columns:1fr 420px;gap:40px;padding:40px 40px 36px;border-bottom:1px solid var(--line)}
.rs div{display:grid;grid-template-columns:110px 1fr;padding:10px 0;border-bottom:1px solid var(--line);color:var(--txt)}
.rs span{color:var(--mut)}
.rb{display:grid;grid-template-columns:1fr 1.2fr}
.col{padding:36px 40px}.col+.col{border-left:1px solid var(--line)}
.lab{margin-bottom:12px}.col p{color:#D3D5CA}
.col ul{list-style:none}.col li{padding:10px 0;border-bottom:1px solid var(--line);display:flex;gap:12px}.col li i{font-style:normal;color:var(--hv)}
.mt{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.mt div{background:var(--g0);border:1px dashed #4A5042;border-radius:4px;padding:18px}
.mt b{font-size:56px;font-weight:800;line-height:1;display:block;color:var(--mut)}.mt span{font-size:13px;color:var(--mut);display:block;margin-top:10px}
blockquote{margin-top:24px;font-size:20px;line-height:1.4;border-left:3px solid var(--hv);padding-left:20px;font-weight:500}
cite{display:block;font-style:normal;color:var(--mut);margin-top:12px}
.rf{display:flex;gap:26px;align-items:center;padding:18px 40px;border-top:1px solid var(--line);background:#171A14}'''))
# 04 Bento
S.append(mod(4,'Bento',f'''<section class="m">{H("What we optimise for","Accuracy. Speed.<br><span class=hv>Taste. Delight.</span>","Four promises, each with a mechanism behind it rather than an adjective.")}
<div class="bento">
<div class="b a panel"><span class="mono k">Accuracy</span><h3>Every AI output has a human owner.</h3><div class="diff"><div class="mono mut">Review · homepage hero copy</div><p class="del">− “We leverage cutting-edge AI to unlock synergies.”</p><p class="add">+ “Brief in. Build live.”</p><span class="mono mut">edited by a person · approved by you</span></div><div class="sig">{"".join(f'<div><span class="mono">{x}</span><b>{y}</b><i class="mono ok">✓ signed</i></div>' for x,y in [("Spec","Strategist"),("Design","Designer"),("Code","Engineer"),("Launch","Walter")])}</div></div>
<div class="b s panel"><span class="mono k">Speed</span><h3>Short loops you can see.</h3><div class="spark">{"".join(f'<i style="height:{h}%"></i>' for h in [30,45,38,60,52,70,64,82,76,90])}</div><p class="mono mut">Daily build updates · illustrative</p></div>
<div class="b w panel"><div><span class="mono k">Talk to Walter</span><h3 style="font-size:30px;margin-top:14px">One point of contact,<br>brief to launch.</h3><a class="btn p" style="margin-top:22px;height:46px;font-size:14px">Book 30 minutes →</a></div><div class="ring">{symbol(size=200,**MK)}</div></div>
<div class="b t panel"><span class="mono k">Taste</span><h3>Senior designers make the call.</h3><div class="opts"><div></div><div></div><div class="pick"><span class="mono">chosen</span></div><div></div></div><p class="mono mut">AI proposes options · a designer picks one and refines it</p></div>
<div class="b dl"><span class="mono k" style="color:var(--g0)">Delight</span><h3 style="color:var(--g0);font-size:34px">Details people notice, then use.</h3><p style="color:#2A2E22;font-size:15px">Micro-interactions, fast pages and forms that don’t fight you. Built to WCAG 2.2 AA so delight includes everyone.</p></div>
</div></section>''','''
.bento{display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:280px;gap:16px}
.b{padding:28px;display:flex;flex-direction:column;gap:14px;overflow:hidden;position:relative}
.b h3{font-size:26px}
.a{grid-column:1/6;grid-row:span 2}.s{grid-column:6/9}.w{grid-column:9/13;grid-row:span 2;flex-direction:column;justify-content:space-between}.t{grid-column:6/9}.dl{grid-column:1/13;grid-row:auto;height:200px;background:var(--hv);border-radius:6px;display:grid;grid-template-columns:160px 1fr 1fr;align-items:center;gap:30px}
.diff{background:var(--g0);border:1px solid var(--line);border-radius:4px;padding:16px 18px;margin-top:10px;display:flex;flex-direction:column;gap:8px}.diff p{font-family:ChivoMono;font-size:14px}.del{color:#8A8F80;text-decoration:line-through}.add{color:var(--hv)}
.sig{margin-top:auto;border-top:1px solid var(--line)}
.sig div{display:grid;grid-template-columns:100px 1fr auto;padding:16px 0;border-bottom:1px solid var(--line);align-items:center}.sig span{color:var(--mut)}
.spark{display:flex;align-items:flex-end;gap:8px;height:110px;margin-top:auto}.spark i{flex:1;background:var(--g2);border-radius:2px}.spark i:last-child{background:var(--sky)}
.w .ring{align-self:flex-end}
.opts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:auto;height:80px}.opts div{background:var(--g2);border-radius:3px}.opts .pick{background:transparent;box-shadow:inset 0 0 0 2px var(--hv);display:flex;align-items:flex-end;padding:6px}.opts .pick span{color:var(--hv);font-size:10px}
.dl .k:before{background:var(--g0);box-shadow:none}'''))
# 05 Media + text
S.append(mod(5,'Media + text','''<section class="m"><div class="g12" style="align-items:center">
<div style="grid-column:1/8;position:relative"><div class="panel" style="overflow:hidden;padding:0"><img src="img/whiteboard.jpg" style="width:100%;height:600px;object-fit:cover;display:block;filter:contrast(1.05)"></div>
<div class="note panel"><span class="mono k">Day 1 · 10:15</span><b>Sitemap agreed on the whiteboard. Spec draft in your inbox by tomorrow.</b></div></div>
<div style="grid-column:9/13"><div class="mono k">Website development</div><h2 class="d" style="font-size:60px;margin-top:22px">It starts on a whiteboard,<br><span class="hv">not in a template.</span></h2>
<p class="lead" style="margin-top:22px;font-size:18px">From the first brief to launch, one team carries the work through analysis, scope, design and build, so nothing is lost in a hand-off.</p>
<div class="steps mono"><div><span>01</span>Briefing</div><div><span>02</span>Current &amp; competitor analysis</div><div><span>03</span>Define project scope</div><div><span>04</span>Sitemap · wireframes · design</div><div><span>05</span>Develop on HubSpot CMS</div></div>
<div style="display:flex;gap:16px;margin-top:30px"><a class="btn p">Start a brief →</a><a class="btn s">See our work</a></div>
<p class="mono" style="color:#7E8475;margin-top:18px">Photo: generated placeholder · replace with a real session</p></div></div></section>''','''
.note{position:absolute;right:-36px;bottom:-30px;width:340px;padding:20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 20px 40px rgba(0,0,0,.4)}
.note b{font-size:17px;line-height:1.35}
.steps{margin-top:26px;border-top:1px solid var(--line)}
.steps div{padding:12px 0;border-bottom:1px solid var(--line);display:flex;gap:16px;color:var(--txt);text-transform:none;font-size:13px;letter-spacing:.02em}
.steps span{color:var(--hv)}'''))
# 06 Talk to Walter
days=[('Mon','16'),('Tue','17'),('Wed','18'),('Thu','19'),('Fri','20')]
slots=['09:30','11:00','14:00','15:30']
cal=''.join(f'<div class="day"><span class="mono mut">{d} Nov {n}</span>'+''.join(f'<a class="sl {"pick" if (d,s)==("Tue","11:00") else ""} {"x" if (d,s) in [("Mon","09:30"),("Wed","14:00"),("Thu","11:00"),("Fri","15:30")] else ""}">{s}</a>' for s in slots)+'</div>' for d,n in days)
S.append(mod(6,'Talk to Walter',f'''<section class="m"><div class="g12">
<div style="grid-column:1/6"><div class="mono k">Your point of contact</div><h2 class="d" style="margin-top:22px;font-size:62px">Talk to Walter.<br><span class="hv">Not a sales queue.</span></h2>
<p class="lead" style="margin-top:22px;font-size:18px">Walter Lentfert founded Razor Profiles in 2008. 30+ years in strategy, marketing, sales and execution, from commercial operations at GE Healthcare to leading HubSpot implementation work in the US. He scopes every build himself and stays on it until launch.</p>
<div class="wf mono"><div><span>Based</span>Wilmington, NC</div><div><span>Languages</span>English · Nederlands</div><div><span>Since</span>2008</div><div><span>Email</span>walter.lentfert@razorprofiles.com</div></div></div>
<div style="grid-column:7/13;align-self:start" class="bk panel"><div class="bh"><div class="ph mono">Portrait<br>to be shot</div><div><b style="font-size:20px">30 minutes with Walter</b><div class="mono mut" style="margin-top:4px">Video call · bring the business challenge</div></div></div>
<div class="cal">{cal}</div>
<div class="bf"><div><span class="mono mut">Selected</span><div style="font-weight:700;margin-top:2px">Tue Nov 17 · 11:00 ET</div></div><a class="btn p" style="margin-left:auto">Confirm call →</a></div>
<p class="mono" style="color:#7E8475;padding:0 24px 18px">Calendar slots illustrative · connects to Walter’s HubSpot meetings link</p></div></div></section>''','''
.wf{margin-top:30px;border-top:1px solid var(--line)}.wf div{display:grid;grid-template-columns:130px 1fr;padding:12px 0;border-bottom:1px solid var(--line);color:var(--txt);text-transform:none;font-size:13px}.wf span{color:var(--mut);text-transform:uppercase}
.bk{overflow:hidden}
.bh{display:flex;gap:18px;align-items:center;padding:24px;border-bottom:1px solid var(--line)}
.ph{width:76px;height:76px;border-radius:50%;border:1px dashed #6B7260;display:flex;align-items:center;justify-content:center;text-align:center;font-size:9px;color:var(--mut);line-height:1.3}
.cal{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;padding:24px}
.day{display:flex;flex-direction:column;gap:8px}.day>span{margin-bottom:4px}
.sl{display:flex;justify-content:center;padding:12px 0;border-radius:4px;box-shadow:inset 0 0 0 1px #4A5042;font-family:ChivoMono;font-size:14px}
.sl.x{color:#5A6150;box-shadow:none;background:var(--g0);text-decoration:line-through}
.sl.pick{background:var(--hv);color:var(--g0);box-shadow:none;font-weight:700}
.bf{display:flex;align-items:center;padding:20px 24px;border-top:1px solid var(--line);background:#171A14}'''))
# 07 Testimonials
S.append(mod(7,'Testimonials','''<section class="m">'''+H("What clients say","Not just code.<br><span class=hv>Confidence.</span>","Two client quotes on file from June 2025, with five more expected. Names and titles appear once approved.")+'''
<div class="qs"><div class="q panel"><div class="qt mono"><span class="ok">✓ Verified client</span><span class="mut">9amHealth · Psomagen · Blip · Kean</span></div>
<p>“I’ve had the opportunity to work with Walter and his team across several companies, and each time, his ability to deliver sharp, strategic, and high-performing digital work has made a real impact.”</p>
<div class="who"><i></i><div><b>Name &amp; title pending approval</b><span class="mono mut">Seamless HubSpot theme development · complex e-commerce integration</span></div></div></div>
<div class="q panel"><div class="qt mono"><span class="ok">✓ Verified client</span><span class="mut">Psomagen · 9amHealth · Kean · Blip</span></div>
<p>“Walter and team have been my go-to for all things HubSpot and web development across multiple companies. From Psomagen to 9amHealth, his custom theme builds were clean, reliable, and built with scalability in mind. […] He delivers not just code, but confidence.”</p>
<div class="who"><i></i><div><b>Name &amp; title pending approval</b><span class="mono mut">Custom HubSpot themes · complex integrations</span></div></div></div></div>
<div class="nav"><span class="mono mut">02 / 07</span><div class="pg"><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i><i></i></div><a class="btn s" style="margin-left:auto;width:54px;justify-content:center;padding:0">←</a><a class="btn p" style="width:54px;justify-content:center;padding:0">→</a></div></section>''','''
.qs{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.q{padding:32px;display:flex;flex-direction:column;gap:24px}
.qt{display:flex;justify-content:space-between}
.q p{font-size:25px;line-height:1.35;font-weight:500;letter-spacing:-.01em}
.who{display:flex;gap:14px;align-items:center;margin-top:auto;padding-top:22px;border-top:1px solid var(--line)}.who i{width:44px;height:44px;border-radius:50%;border:1px dashed #6B7260}.who b{display:block}
.nav{display:flex;align-items:center;gap:20px;margin-top:24px}.pg{display:flex;gap:6px}.pg i{width:28px;height:4px;background:var(--g2);border-radius:2px}.pg i.on{background:var(--hv)}'''))
# 08 Engagement
S.append(mod(8,'Engagement models',f'''<section class="m">{H("Ways to work with us","Sprint, Build<br><span class=hv>or Run.</span>","Every engagement starts with a 30-minute call with Walter and a written scope within 48 hours.")}
<div class="tbl panel"><div class="tr th"><div></div><div><span class="mono k">Sprint</span><b>Fix one thing, fast</b></div><div class="hi"><span class="mono k" style="color:var(--g0)">Build</span><b>Site, CRM or store, end to end</b><span class="flag mono">Recommended</span></div><div><span class="mono k">Run</span><b>An extension of your team</b></div></div>
{"".join(f'<div class="tr"><div class="mono mut">{a}</div><div>{b}</div><div class="hi">{c}</div><div>{d}</div></div>' for a,b,c,d in [("Typical length","2–4 weeks","Project, scoped per brief","Monthly"),("Budget","Fixed fee","From $5k","Retainer"),("Strategy &amp; ABM","Plan only","✓","✓ quarterly roadmap"),("Design &amp; build","One module or audit","✓ full site / CRM / store","✓ continuous"),("AI-accelerated QA","✓","✓","✓"),("WCAG 2.2 AA","✓","✓","✓"),("Walter as contact","✓","✓","✓"),("White-label for agencies","—","✓","✓")])}
<div class="tr tf"><div></div><div><a class="btn s" style="height:46px;font-size:14px">Scope a sprint</a></div><div class="hi"><a class="btn" style="height:46px;font-size:14px;background:var(--g0);color:var(--hv)">Start a build with Walter →</a></div><div><a class="btn s" style="height:46px;font-size:14px">Plan a retainer</a></div></div></div>
<p class="mono" style="color:#7E8475;margin-top:16px">“From $5k” = budget floor on Razor’s HubSpot Solutions Directory listing · confirm before publishing</p></section>''','''
.tbl{overflow:hidden}
.tr{display:grid;grid-template-columns:260px 1fr 1fr 1fr;border-bottom:1px solid var(--line)}
.tr>div{padding:16px 24px;font-size:16px}
.tr .hi{background:rgba(214,223,39,.07);box-shadow:inset 1px 0 0 rgba(214,223,39,.4),inset -1px 0 0 rgba(214,223,39,.4)}
.th>div{padding:26px 24px}.th b{display:block;font-size:22px;margin-top:10px;letter-spacing:-.01em}
.th .hi{background:var(--hv);color:var(--g0);position:relative}.th .hi .k:before{background:var(--g0);box-shadow:none}
.flag{position:absolute;right:20px;top:24px;background:var(--g0);color:var(--hv);padding:3px 8px;border-radius:3px;font-size:10px}
.tf{border:0}.tf>div{padding:24px}'''))
# 09 Insights carousel
arts=[('Process','How we use AI without losing accuracy','Where models draft, where people decide, and why every deliverable has a named owner.','8 min'),
('CRM','Planning a HubSpot CRM migration without losing history','Mapping objects, owners and workflows before a single record moves.','11 min'),
('Strategy','Why one team beats a roster of vendors','The hidden cost of hand-offs between strategy, design and development shops.','6 min'),
('E-commerce','Wiring commerce into the CRM','What changes when orders, customers and campaigns live in one system.','9 min')]
cards=''.join(f'<div class="ac panel"><div class="th2"><span class="mono">{c}</span><div class="pat p{i}"></div></div><div class="ab"><span class="mono mut">{c} · {t2} read</span><h3>{t}</h3><p>{d}</p><a class="tl">Read →</a></div></div>' for i,(c,t,d,t2) in enumerate(arts))
S.append(mod(9,'Insights carousel',f'''<section class="m" style="overflow:hidden">{H("Insights","Notes from<br><span class=hv>the build.</span>","Proposed launch articles. Each one documents how we actually work, not thought-leadership filler.")}
<div class="car">{cards}</div><div style="display:flex;align-items:center;gap:20px;margin-top:28px"><div style="flex:1;height:2px;background:var(--g2)"><i style="display:block;width:38%;height:2px;background:var(--hv)"></i></div><a class="btn s" style="width:54px;justify-content:center;padding:0">←</a><a class="btn p" style="width:54px;justify-content:center;padding:0">→</a></div></section>''','''
.car{display:flex;gap:16px;width:1700px}
.ac{width:410px;flex:none;overflow:hidden}
.th2{height:200px;position:relative;border-bottom:1px solid var(--line);overflow:hidden}
.th2 .mono{position:absolute;left:18px;top:16px;z-index:2;background:var(--g0);padding:3px 8px;border-radius:3px}
.pat{position:absolute;inset:0}
.p0{background:repeating-linear-gradient(90deg,#262A22 0 1px,transparent 1px 28px),repeating-linear-gradient(0deg,#262A22 0 1px,transparent 1px 28px);}
.p0:after{content:"";position:absolute;left:40%;top:30%;width:120px;height:60px;background:var(--hv)}
.p1{background:linear-gradient(#1B1E18,#1B1E18) padding-box;}
.p1:before{content:"";position:absolute;inset:40px 30px;background:repeating-linear-gradient(0deg,#33382E 0 10px,transparent 10px 22px)}
.p1:after{content:"";position:absolute;left:30px;right:190px;top:84px;height:10px;background:var(--sky)}
.p2{background:radial-gradient(circle at 70% 60%,transparent 0 60px,#33382E 61px 62px,transparent 63px),radial-gradient(circle at 70% 60%,var(--hv) 0 10px,transparent 11px)}
.p3{background:repeating-linear-gradient(135deg,#262A22 0 14px,#1B1E18 14px 28px)}
.p3:after{content:"";position:absolute;right:40px;bottom:30px;width:80px;height:80px;border-radius:50%;background:var(--hv)}
.ab{padding:22px;display:flex;flex-direction:column;gap:10px}.ab p{color:var(--mut);font-size:15px}.ab .tl{align-self:flex-start;margin-top:6px}'''))
# 10 CTA + footer
S.append(mod(10,'CTA + footer',f'''<section class="cta"><div class="ring">{symbol(size=520,**MK)}</div><div style="position:relative;width:860px">
<div class="mono k">Start a build</div><h2 class="d" style="font-size:118px;margin-top:24px">What are we<br><span class="hv">building?</span></h2>
<div class="pr"><span class="hv" style="font-family:ChivoMono;font-size:22px">›</span><span class="ty">We need our product catalogue searchable on HubSpot by Q2</span><i class="cur"></i><a class="btn p" style="margin-left:auto;height:48px">Send to Walter →</a></div>
<p class="mono mut" style="margin-top:14px">Goes straight to Walter’s inbox · or email walter.lentfert@razorprofiles.com</p></div></section>
<footer><div class="fr">{lockup(height=30,word="#EEEEE6",**MK)}<nav><a>How we build</a><a>Services</a><a>Work</a><a>Industries</a><a>HubSpot</a><a>Partnerships</a><a>About</a><a>Contact</a></nav></div>
<div class="fr2 mono"><span>© 2008–2026 Razor Profiles LLC</span><span>Wilmington, NC</span><span>EN / NL</span><span style="margin-left:auto">Privacy</span><span>Terms</span><span><i class="dot" style="background:var(--hv)"></i> WCAG 2.2 AA</span></div></footer>''','''
.cta{padding:110px 64px 120px;position:relative;overflow:hidden;border-bottom:1px solid var(--line)}
.cta .ring{position:absolute;right:40px;top:70px;opacity:1}
.pr{display:flex;align-items:center;gap:14px;margin-top:44px;background:var(--g1);border:1px solid #5A6150;border-radius:6px;padding:10px 10px 10px 22px}
.ty{font-size:19px}.cur{width:2px;height:24px;background:var(--hv)}
footer{padding:40px 64px 32px}
.fr{display:flex;align-items:center}.fr nav{margin-left:auto;display:flex;gap:28px;font-size:15px;color:#CFD1C6}
.fr2{display:flex;gap:24px;color:var(--mut);margin-top:32px;padding-top:20px;border-top:1px solid var(--line)}'''))
print(' '.join(f'modules/{s}.html' for s in S))
