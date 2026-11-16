import csv
rows=[r for r in csv.reader(open('../photos.tsv'),delimiter='\t')]
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Geist:wght@400;500&family=Geist+Mono:wght@400;500&display=block" rel="stylesheet">
<link rel="stylesheet" href="base.css"><style>%s</style></head><body>'''
TAIL='<script>document.fonts.ready.then(()=>{document.title="H"+document.documentElement.scrollHeight;});</script></body></html>'
fam={'a':('A','Architecture & surfaces','Curved facades, stairwells and glass under one hard light. Continuity and enterprise scale — the Möbius, built.'),
'b':('B','Life-sciences craft','Instruments and glassware isolated on black. The client world, shot as precision rather than as a stock lab.'),
'c':('C','People at work, turned away','Hands, backs, silhouettes at the work. Warmth and a personal team without staged smiles or eye contact.'),
'd':('D','Material macro','Satin, folded paper, sculpted metal. Texture for section breaks and backgrounds; the closest cousin of the ribbon.')}
css='''.fam{padding:56px 112px 64px;border-top:1px solid var(--rule)}
.fh{display:grid;grid-template-columns:120px 420px 1fr;align-items:baseline;margin-bottom:34px;column-gap:24px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.it .pair{display:grid;grid-template-columns:1fr 1fr;gap:4px;height:300px}
.it .pair div{position:relative;overflow:hidden;background:var(--surf)}
.it img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.it .tag{position:absolute;left:8px;top:8px;background:rgba(13,15,26,.85);color:var(--text);padding:4px 7px;font-size:10px}
.it .t{margin-top:14px;font-size:14px;line-height:1.4;color:var(--text)}
.it .m{margin-top:6px;color:var(--mute);font-size:10.5px;letter-spacing:.1em}'''
h=HEAD%css+'<div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface</span><span class="r">Imagery — <b>Stock families, original → graded</b></span></div>'
h+='<section style="padding:72px 112px 40px"><div class="lab mono">Imagery — Direction B</div><div class="disp" style="font-size:64px">Four families, one light</div><p class="small" style="margin-top:18px;max-width:760px">Each pair: Pexels original (left) and the same frame graded toward B (right) — blacks lifted to #0D0F1A, cool split tone, warm hues pulled down. All 14 are free under the Pexels licence; credit is shown anyway.</p></section>'
for k,(L,name,desc) in fam.items():
  its=[r for r in rows if r[0].startswith(k)]
  h+=f'<section class="fam"><div class="fh"><span class="mono" style="color:var(--sky)">Family {L}</span><span class="disp" style="font-size:40px">{name}</span><p class="small" style="max-width:640px">{desc}</p></div><div class="grid">'
  for key,n,pid,slug,t,p in its:
    f=f'{key}-{n}'
    h+=f'<div class="it"><div class="pair"><div><img src="thumb/{f}.jpg"><span class="tag mono">Original</span></div><div><img src="thumb/{f}-graded.jpg"><span class="tag mono" style="color:var(--sky)">Graded B</span></div></div><div class="t">{t}</div><div class="m mono">{key.upper()} · {p} · Pexels {pid}</div></div>'
  h+='</div></section>'
h+='<div class="cap mono" style="padding:0 112px 48px;margin:0"><span>Source: pexels.com/photo/&lt;slug&gt;-&lt;id&gt; — see CREDITS.md</span><span>Grade: grade.py (gradient map + 20–60% chroma, warm hues ×0.2)</span></div>'+TAIL
open('sheet.html','w').write(h)

# context comp
css2='''.split{display:grid;grid-template-columns:1fr 1fr;min-height:760px}
.media{position:relative;overflow:hidden}.media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.media .cap{position:absolute;left:112px;right:40px;bottom:28px;margin:0;color:var(--text)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:52px;position:relative}
.cd{background:var(--surf);border:1px solid var(--rule);position:relative}
.cd .ri{height:300px;overflow:hidden;position:relative;border-bottom:1px solid var(--rule)}
.cd .ri img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:none}
.cd.hov{border-color:var(--sky);transform:translateY(-8px);box-shadow:0 8px 0 rgba(0,0,0,.35)}
.cd.hov .ri img{transform:scale(1.05)}
.cd.hov:before{content:'';position:absolute;left:0;right:0;top:0;height:2px;background:var(--yel);z-index:2}
.callout{position:absolute;top:-38px;color:var(--sky)}
.band{position:relative;height:560px;overflow:hidden}.band img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 45%}
.band .ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(13,15,26,.94) 0%,rgba(13,15,26,.7) 42%,rgba(13,15,26,0) 75%)}'''
c=HEAD%css2+'<div class="spec mono"><span><b>Razor Profiles</b> · Direction B — One Surface</span><span class="r">Imagery in context — <b>Modules 02 · 06 · section break</b></span></div>'
c+='''<div class="split"><div class="media"><img src="../graded/b1-lab-microscope-graded.jpg" style="object-position:50% 40%"><div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:linear-gradient(transparent,rgba(13,15,26,.92))"></div>
<div class="cap mono"><span>Fig. 03 — Family B · Pexels 32362925, graded</span><span>@ VIP / Pexels</span></div></div>
<div class="surf" style="padding:96px 112px 96px 96px"><div class="lab mono">02 — Media + text</div>
<div class="disp" style="font-size:72px">Precise work for<br>precise industries.</div>
<p style="margin-top:26px;max-width:520px">Strategy, marketing, design and development under one roof, for teams whose work has to be exact — and whose audience can tell when it isn't.</p>
<div class="rt" style="margin-top:30px;max-width:560px">
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Image</span><span>Instrument isolated on black, one hard key, cool split</span></div>
<div class="row small" style="grid-template-columns:120px 1fr;color:var(--text)"><span class="mono" style="color:var(--mute2)">Crop</span><span>Subject off-centre, falls into shadow at the frame edge</span></div></div>
<div style="margin-top:34px"><a class="sl">See how an engagement runs →</a></div></div></div>
<section class="sec"><div class="g" style="align-items:end"><div style="grid-column:1/8"><div class="lab mono">06 — Cards</div><div class="disp">Pick a starting point</div></div>
<div style="grid-column:9/13"><p class="small">Same 3-up grid, with graded photography in place of the ribbon crops. One family per card keeps the row from feeling like a mood board.</p></div></div>
<div class="cards">'''
cards=[('c3-people-writing','01','Strategy','Digital strategy and account-based planning.','Family C · Pexels 5759949','sl',''),
('a1-arch-spiral-stair','02','Marketing','Campaigns and automation tuned to the persona journey.','Family A · Pexels 3853796','tl',' hov'),
('d2-material-form','03','Design','Brand, UX and interface design built as a system.','Family D · Pexels 29636882','sl','')]
for f,n,t,dsc,src,lk,hv in cards:
  col='var(--sky)' if hv else 'var(--mute2)'
  c+=f'<div class="cd{hv}"><div class="ri"><img src="../graded/{f}-graded.jpg"></div><div style="padding:26px 28px 32px"><span class="mono" style="color:{col}">{n}</span><h3 style="font-size:28px;margin-top:10px">{t}</h3><p class="small" style="margin-top:10px">{dsc}</p><div class="mono" style="margin-top:18px;color:var(--mute2);font-size:10px">{src}</div><a class="{lk}" style="display:inline-block;margin-top:20px">{t} →</a></div></div>'
c+='''<span class="callout mono" style="left:calc(33.33% + 8px)">Hover — lift 8px, Sky border, yellow hot edge, image scales 105%</span></div></section>
<div class="band"><img src="../graded/d1-material-satin-graded.jpg"><div class="ov"></div>
<div style="position:absolute;left:112px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;max-width:640px">
<div class="lab mono">Section break — Family D</div><div class="disp" style="font-size:64px">One surface,<br>start to finish.</div>
<p style="margin-top:22px;max-width:500px">Material macro as a full-bleed band: texture carries the transition while type stays on the darkest third.</p></div>
<div class="cap mono" style="position:absolute;left:112px;right:112px;bottom:28px;margin:0"><span>Fig. 09 — Pexels 8007352, graded · Tamanna Rumee / Pexels</span><span>Overlay: #0D0F1A 94% → 0%</span></div></div>'''+TAIL
open('context.html','w').write(c)
