import sys; sys.path.insert(0,'/workspace/razor-profiles/round-2/shared')
from mark import symbol, lockup
CSS='''
@font-face{font-family:Bricolage;src:url(fonts/BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf);font-weight:200 800;font-stretch:75% 100%}
@font-face{font-family:Instrument;src:url(fonts/InstrumentSans-VariableFont_wdth,wght.ttf);font-weight:400 700;font-stretch:75% 100%}
@font-face{font-family:Instrument;src:url(fonts/InstrumentSans-Italic-VariableFont_wdth,wght.ttf);font-style:italic;font-weight:400 700}
:root{--white:#F7F9FC;--frost:#E4EBF4;--ink:#0E1A33;--navy:#003271;--sky:#28ABE2;--yel:#D6DF27;--slate:#4A5872;--line:#C9D4E3;--cut:28px}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1440px;background:var(--white);color:var(--ink);font-family:Instrument,sans-serif;-webkit-font-smoothing:antialiased;font-size:17px;line-height:1.55}
a{color:inherit;text-decoration:none}
.d{font-family:Bricolage;font-stretch:78%;font-weight:700;letter-spacing:-.025em;line-height:.94;font-variation-settings:"opsz" 96}
.eyebrow{font-family:Bricolage;font-weight:600;font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-stretch:90%;display:flex;align-items:center;gap:12px;color:var(--navy)}
.eyebrow:before{content:"";width:14px;height:14px;background:var(--sky);clip-path:polygon(0 0,55% 0,100% 45%,100% 100%,0 100%)}
.wrap{padding:0 96px}
.cut{clip-path:polygon(0 0,calc(100% - var(--cut)) 0,100% var(--cut),100% 100%,0 100%)}
.btn{display:inline-flex;align-items:center;gap:14px;height:56px;padding:0 30px 0 26px;font-weight:600;font-size:16px;clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,0 100%)}
.btn.p{background:var(--navy);color:#fff}
.btn.y{background:var(--yel);color:var(--ink)}
.btn.s{background:transparent;color:var(--navy);box-shadow:inset 0 0 0 2px var(--navy);clip-path:none}
.btn .ar{font-family:Bricolage;font-size:20px;line-height:1}
.tl{font-weight:600;color:var(--navy);border-bottom:2px solid var(--sky);padding-bottom:2px}
header.top{height:84px;display:flex;align-items:center;padding:0 96px;background:var(--white);border-bottom:1px solid var(--line)}
header.top nav{display:flex;align-items:center;height:84px;gap:34px;margin-left:auto;margin-right:36px;font-weight:500;font-size:15px}
header.top nav a{height:84px;display:flex;align-items:center}header.top nav a.on{color:var(--navy);box-shadow:inset 0 -3px 0 var(--sky)}
.crumb{height:52px;display:flex;align-items:center;padding:0 96px;font-size:13px;color:var(--slate);border-bottom:1px solid var(--line);gap:10px}
.crumb b{color:var(--ink);font-weight:600}.crumb .r{margin-left:auto;display:flex;gap:22px}
.crumb .r span:before{content:"";display:inline-block;width:7px;height:7px;background:var(--sky);margin-right:8px;vertical-align:1px}
h2.d{font-size:76px}
h3{font-family:Bricolage;font-stretch:85%;font-weight:650;font-size:28px;letter-spacing:-.015em;line-height:1.05}
.lead{font-size:20px;line-height:1.5;color:#26324d}
.mut{color:var(--slate)}
.chip{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;padding:6px 12px 6px 10px;background:var(--frost);color:var(--navy)}
.chip i{width:9px;height:9px;display:block;clip-path:polygon(0 0,55% 0,100% 45%,100% 100%,0 100%)}
.ph{border:2px dashed #8EA0BD;color:var(--slate);display:flex;align-items:center;justify-content:center;text-align:center;font-size:13px;font-weight:600;letter-spacing:.04em}
'''
NAV=['Services ▾','Industries ▾','HubSpot','Work','About','Insights']
def header(active='Services ▾'):
    n=''.join(f'<a class="{"on" if x==active else ""}">{x}</a>' for x in NAV)
    return f'<header class="top">{lockup(height=34)}<nav>{n}</nav><a class="btn p" style="height:46px;font-size:15px;padding:0 22px 0 20px">Talk to Walter <span class="ar">→</span></a></header>'
def page(body,css='',title='',w=1440):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{CSS}{css}</style></head><body>{body}</body></html>'
