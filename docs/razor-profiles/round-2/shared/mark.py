"""Razor Profiles mark evolutions, built from the REAL vector geometry in logo/rp-left-light.svg:
the symbol silhouette (its clipPath) and the Philosopher wordmark paths. Nothing redrawn."""
import re, math
SRC='/workspace/razor-profiles/logo/rp-left-light.svg'
_s=open(SRC).read()
SIL=re.search(r'<clipPath id="clippath"><path class="cls-1" d="([^"]+)"',_s).group(1)
_body=re.sub(r'base64,[A-Za-z0-9+/=]+','',_s)
WORD=''.join(re.findall(r'<(?:path|polygon|rect) class="cls-2"[^>]*/>',_body)).replace('class="cls-2" ','')
C=(15.6,16.4)            # optical centre of the ring
SEAMS={'tr':-48.0,'r':9.3,'l':167.5}   # angles (deg, svg y-down) through the three original overlap cusps
def _sector(a0,a1,r=60):
    if a1<a0: a1+=360
    pts=[C]+[(C[0]+r*math.cos(math.radians(a)),C[1]+r*math.sin(math.radians(a))) for a in [a0+(a1-a0)*i/24 for i in range(25)]]
    return ' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)
def _cut(a,r=60):
    return f'{C[0]:.2f},{C[1]:.2f} {C[0]+r*math.cos(math.radians(a)):.2f},{C[1]+r*math.sin(math.radians(a)):.2f}'
_n=[0]
def symbol(mode='cut',top='#28ABE2',lobe='#D6DF27',bottom='#003271',cut=0.9,size=None,extra=''):
    """mode cut: three flat bands with razor-thin transparent cuts (Direction 1).
       mode live: one colour silhouette with one 'live' band (Direction 2). top/bottom = base colour, lobe = live colour.
       mode mono: single colour silhouette."""
    _n[0]+=1; i=f'm{_n[0]}'
    vb='-1 -1 34 34'
    wh=f'width="{size}" height="{size}"' if size else ''
    t,r,l=SEAMS['tr'],SEAMS['r'],SEAMS['l']
    cuts='' if cut<=0 else ''.join(f'<polyline points="{_cut(a)}" stroke="#000" stroke-width="{cut}" fill="none"/>' for a in (t,r,l))
    mask=f'<mask id="{i}k" maskUnits="userSpaceOnUse" x="-5" y="-5" width="45" height="45"><path d="{SIL}" fill="#fff"/>{cuts}</mask>'
    if mode=='mono':
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" {wh} {extra}><defs>{mask}</defs><g mask="url(#{i}k)"><rect x="-5" y="-5" width="45" height="45" fill="{top}"/></g></svg>'
    bands=f'<polygon points="{_sector(l,t)}" fill="{top}"/><polygon points="{_sector(t,r)}" fill="{lobe}"/><polygon points="{_sector(r,l)}" fill="{bottom}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" {wh} {extra}><defs>{mask}</defs><g mask="url(#{i}k)">{bands}</g></svg>'
def lockup(word='#101A33',height=None,**kw):
    """Horizontal lockup: evolved symbol + the original Philosopher wordmark paths (viewBox of the source file)."""
    sym=symbol(**kw)
    inner=re.sub(r'^<svg[^>]*>','',sym)[:-6]
    inner=f'<g transform="translate(-0.4 -0.4) scale(0.955)">{inner}</g>' if False else inner
    h=f'height="{height}"' if height else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 166.5 33.8" {h}><svg x="-1" y="-1" width="34" height="34" viewBox="-1 -1 34 34" overflow="visible">{inner}</svg><g fill="{word}">{WORD}</g></svg>'
if __name__=='__main__':
    open('/tmp/t.html','w').write('<body style="background:#eee">'+lockup(height=80)+symbol(size=200)+symbol(mode='live',top='#141613',bottom='#141613',lobe='#D6E12E',size=200)+'</body>')
