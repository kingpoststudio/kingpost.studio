import sys; sys.path.insert(0,'/workspace/razor-profiles/round-2/shared')
from mark import symbol, lockup
CSS='''
@font-face{font-family:Chivo;src:url(fonts/Chivo-VariableFont_wght.ttf);font-weight:100 900}
@font-face{font-family:Chivo;src:url(fonts/Chivo-Italic-VariableFont_wght.ttf);font-weight:100 900;font-style:italic}
@font-face{font-family:ChivoMono;src:url(fonts/ChivoMono-VariableFont_wght.ttf);font-weight:100 900}
:root{--g0:#121410;--g1:#1B1E18;--g2:#262A22;--line:#33382E;--txt:#EEEEE6;--mut:#A3A898;--hv:#D6DF27;--sky:#5CC6F0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1440px;background:var(--g0);color:var(--txt);font-family:Chivo,sans-serif;-webkit-font-smoothing:antialiased;font-size:17px;line-height:1.55}
a{color:inherit;text-decoration:none}
.mono{font-family:ChivoMono,monospace;font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-weight:500}
.d{font-family:Chivo;font-weight:800;letter-spacing:-.035em;line-height:.95}
.hv{color:var(--hv)}
.k{display:flex;align-items:center;gap:10px;color:var(--mut)}
.k:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--hv);box-shadow:0 0 0 4px rgba(214,223,39,.18)}
.btn{display:inline-flex;align-items:center;gap:14px;height:54px;padding:0 24px;font-weight:700;font-size:16px;border-radius:4px}
.btn.p{background:var(--hv);color:var(--g0)}
.btn.s{box-shadow:inset 0 0 0 1px #5A6150;color:var(--txt)}
.btn kbd{font-family:ChivoMono;font-size:11px;padding:3px 6px;border-radius:3px;background:rgba(18,20,16,.14);font-weight:600}
.btn.s kbd{background:var(--g2);color:var(--mut)}
.tl{color:var(--sky);border-bottom:1px solid var(--sky);padding-bottom:2px;font-weight:600}
header.top{height:76px;display:flex;align-items:center;padding:0 64px;border-bottom:1px solid var(--line)}
header.top nav{display:flex;align-items:center;height:76px;gap:30px;margin-left:56px;font-size:15px;font-weight:500;color:#CFD1C6}
header.top nav a{height:76px;display:flex;align-items:center}
header.top nav a.on{color:var(--txt);box-shadow:inset 0 -2px 0 var(--hv)}
header.top .rt{margin-left:auto;display:flex;align-items:center;gap:20px}
.crumb{height:46px;display:flex;align-items:center;padding:0 64px;border-bottom:1px solid var(--line);gap:10px;color:var(--mut)}
.crumb b{color:var(--txt);font-weight:500}
.panel{background:var(--g1);border:1px solid var(--line);border-radius:6px}
h2.d{font-size:72px}
h3{font-weight:700;font-size:24px;letter-spacing:-.015em;line-height:1.15}
.lead{font-size:20px;line-height:1.5;color:#D3D5CA}
.mut{color:var(--mut)}
.ok{color:var(--hv)}.run{color:var(--sky)}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%}
'''
NAV=['How we build','Services ▾','Work','Industries ▾','HubSpot','About']
MK=dict(top='#EEEEE6',bottom='#EEEEE6',lobe='#D6DF27',cut=0)
def header(active='How we build'):
    n=''.join(f'<a class="{"on" if x==active else ""}">{x}</a>' for x in NAV)
    return f'<header class="top">{lockup(height=32,word="#EEEEE6",**MK)}<nav>{n}</nav><div class="rt"><span class="mono k">Booking intro calls</span><a class="btn p" style="height:44px;font-size:15px;padding:0 18px">Talk to Walter →</a></div></header>'
def page(body,css=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{css}</style></head><body>{body}</body></html>'
