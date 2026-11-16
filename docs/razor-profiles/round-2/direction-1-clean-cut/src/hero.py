from common import *
css='''
.hero{position:relative;height:760px;overflow:hidden;background:var(--white)}
.hero .txt{position:absolute;left:96px;top:78px;width:760px}
.hero h1{font-size:120px;margin:26px 0 30px}
.hero h1 em{font-style:normal;color:var(--navy)}
.hero h1 .k{display:inline-block;width:.42em;height:.42em;background:var(--yel);margin-left:.08em;clip-path:polygon(0 0,55% 0,100% 45%,100% 100%,0 100%)}
.hero .lead{width:650px}
.hero .ctas{display:flex;gap:28px;align-items:center;margin-top:38px}
.hero .mk{position:absolute;right:72px;top:46px}
.lab{position:absolute;font-family:Bricolage;font-stretch:85%;font-weight:650;font-size:15px;display:flex;align-items:center;gap:10px;white-space:nowrap}
.lab small{font-family:Instrument;font-weight:500;font-size:13px;color:var(--slate)}
.lab:before{content:"";width:46px;height:1.5px;background:var(--ink)}
.strip{position:absolute;left:0;right:0;bottom:0;height:116px;display:grid;grid-template-columns:repeat(4,1fr);background:var(--white);border-top:1px solid var(--line)}
.strip div{padding:24px 28px 0 96px;border-right:1px solid var(--line)}
.strip div+div{padding-left:28px}
.strip b{font-family:Bricolage;font-stretch:85%;font-size:21px;font-weight:700;display:flex;gap:10px;align-items:center}
.strip b i{width:14px;height:14px;display:block;clip-path:polygon(0 0,55% 0,100% 45%,100% 100%,0 100%)}
.strip p{font-size:14px;color:var(--slate);margin-top:6px}
'''
mk=symbol(size=580)
body=header()+'''<div class="crumb"><a>Home</a><span>/</span><b>Services</b><div class="r"><span>Since 2008</span><span>Wilmington, NC</span><span>English &amp; Nederlands</span></div></div>
<section class="hero">
<div class="mk">'''+mk+'''</div>
<div style="position:absolute;left:1268px;top:70px;width:150px;font-size:13px;line-height:1.35;color:var(--slate)"><b style="font-family:Bricolage;font-stretch:85%;font-size:15px;color:var(--ink);display:block">The cut</b>Taste is what we decide to leave out.</div>
<div style="position:absolute;left:1246px;top:118px;width:1.5px;height:56px;background:var(--ink);transform:rotate(14deg);transform-origin:top"></div>
<div class="txt">
<div class="eyebrow">AI-first digital agency · HubSpot · CRM · E-commerce</div>
<h1 class="d">Precise by design. <em>Fast by default.</em><span class="k"></span></h1>
<p class="lead">We plan, design and build enterprise websites, CRM and e-commerce with AI in every step, and a senior human on the other end of the line. That human is Walter.</p>
<div class="ctas"><a class="btn p">Talk to Walter <span class="ar">→</span></a><a class="tl">See how we build</a></div>
</div>
<div class="strip">
<div><b><i style="background:var(--navy)"></i>Accuracy</b><p>Every AI draft checked by a person who signs it.</p></div>
<div><b><i style="background:var(--sky)"></i>Speed</b><p>Spec to staging in days, not quarters.</p></div>
<div><b><i style="background:#fff;box-shadow:inset 0 0 0 2px var(--ink);outline:2px solid var(--ink);outline-offset:-2px"></i>Taste</b><p>The cut: what we decide to leave out.</p></div>
<div><b><i style="background:var(--yel)"></i>Delight</b><p>Interfaces people actually come back to.</p></div>
</div></section>'''
open('hero.html','w').write(page(body,css))
