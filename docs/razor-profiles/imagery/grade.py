import numpy as np, glob, os
from PIL import Image
BASE=np.array([13,15,26])/255.
def grade(im):
    a=np.asarray(im.convert('RGB')).astype(np.float32)/255.
    r,g,b=a[...,0],a[...,1],a[...,2]
    L=0.2126*r+0.7152*g+0.0722*b
    # hue (deg)
    mx=a.max(-1);mn=a.min(-1);d=mx-mn+1e-6
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))*60
    # warm = reds/oranges/yellows/magentas 300..75deg
    hh=(h+60)%360  # warm band now ~0..135
    warm=np.clip(1-np.abs(hh-67)/80,0,1)
    keep=0.6*(1-warm)+0.2*warm           # warm hues heavily desaturated, blues kept
    chroma=(a-L[...,None])*keep[...,None]
    # tone: gentle S, compress highlights so whites stay off-white
    t=np.clip(L,0,1); t=t*t*(3-2*t)*0.35+t**0.85*0.65; t=t*0.97
    # gradient map: base -> navy -> cool mid -> #EAEAE9
    stops=np.array([[0,13,15,26],[.25,36,44,68],[.55,112,122,142],[.8,184,190,198],[1,242,242,240]],np.float32)
    m=np.stack([np.interp(t,stops[:,0],stops[:,c]/255.) for c in (1,2,3)],-1)
    out=m+chroma*0.8
    # cool split: nudge highlights slightly toward Sky, shadows toward navy
    sky=np.array([40,171,226])/255.;navy=np.array([0,50,113])/255.
    out=out+ (sky-out)*(0.06*t**2)[...,None] + (navy-out)*(0.06*(1-t)**3)[...,None]
    out=BASE+(1-BASE)*np.clip(out-BASE,0,1)/(1-BASE)*(1-BASE)  # floor at base
    out=np.maximum(out,BASE)
    return Image.fromarray((np.clip(out,0,1)*255+.5).astype(np.uint8))
for f in sorted(glob.glob('original/*.jpg')):
    grade(Image.open(f)).save('graded/'+os.path.basename(f).replace('.jpg','-graded.jpg'),quality=90)
    print(f)
