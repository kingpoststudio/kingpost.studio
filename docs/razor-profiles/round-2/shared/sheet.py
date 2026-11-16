"""Contact sheet: python3 sheet.py OUT.jpg TITLE BG FG png1 png2 ... (2 columns, labeled)"""
import sys
from PIL import Image, ImageDraw, ImageFont
out,title,bg,fg=sys.argv[1:5]; files=sys.argv[5:]
F='/workspace/razor-profiles/round-2/direction-1-clean-cut/src/fonts/BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf'
try:
    ft=ImageFont.truetype(F,44); fl=ImageFont.truetype(F,24)
    try: ft.set_variation_by_axes([96,85,700]); fl.set_variation_by_axes([24,90,600])
    except Exception: pass
except Exception: ft=fl=ImageFont.load_default()
CW=1100; pad=60; gap=50
ims=[Image.open(f).convert('RGB') for f in files]
th=[]
for im in ims:
    s=CW/im.width; th.append(im.resize((CW,int(im.height*s)),Image.LANCZOS))
cols=[[],[]]; hs=[0,0]
for i,t in enumerate(th):
    c=0 if hs[0]<=hs[1] else 1; cols[c].append((i,t)); hs[c]+=t.height+gap+44
W=pad*2+CW*2+gap; H=pad+110+max(hs)+pad
sh=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(sh)
d.text((pad,pad),title,font=ft,fill=fg)
for c in (0,1):
    y=pad+110; x=pad+c*(CW+gap)
    for i,t in cols[c]:
        name=files[i].rsplit('/',1)[-1].replace('.png','')
        d.text((x,y),name.upper().replace('-',' · ',1),font=fl,fill=fg); y+=40
        sh.paste(t,(x,y)); d.rectangle([x-1,y-1,x+CW,y+t.height],outline='#9AA6B8'); y+=t.height+gap
sh.save(out,quality=88); print(out,sh.size)
