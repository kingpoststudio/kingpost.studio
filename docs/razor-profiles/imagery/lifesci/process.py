import sys,glob,os
sys.path.insert(0,'..')
from PIL import Image,ImageFilter
import numpy as np
src=open('../grade.py').read().split('for f in sorted')[0]; exec(src)
for f in sorted(glob.glob('raw/*.jpg')):
    n=os.path.basename(f)[:-4]; im=Image.open(f).convert('RGB')
    if n.startswith('07'):  # garbled launch headline -> soft
        box=(830,160,1140,216); im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(5)),box[:2])
    if n.startswith('08'):  # garbled dashboard labels/numbers -> soft
        box=(606,120,1150,470); im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(1.6)),box[:2])
    if im.width<im.height:  # 3:4 -> 4:5
        h=int(im.width*5/4); t=(im.height-h)//2; im=im.crop((0,t,im.width,t+h))
    g=grade(im)
    out=Image.blend(im,g,0.55)
    a=np.maximum(np.asarray(out).astype(int),[13,15,26]).astype('uint8')
    Image.fromarray(a).save(n+'.png'); print(n,out.size)
