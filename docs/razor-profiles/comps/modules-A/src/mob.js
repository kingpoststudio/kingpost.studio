// Line-art Möbius (same construction as hero A). opts: R,W,cx,cy,tx,tz,hi:[u0,u1](fractions of 2π),ink,hiCol,n
function mob(svg,o){const NS='http://www.w3.org/2000/svg';o=Object.assign({R:230,W:78,tx:-1.02,tz:.38,hi:null,ink:'#131626',hiCol:'#20386C',n:180,ew:1,mark:null},o);
 const P=(u,v)=>{let x=(o.R+v*Math.cos(u/2))*Math.cos(u),y=(o.R+v*Math.cos(u/2))*Math.sin(u),z=v*Math.sin(u/2);
 let x1=x*Math.cos(o.tz)-y*Math.sin(o.tz),y1=x*Math.sin(o.tz)+y*Math.cos(o.tz);
 let y2=y1*Math.cos(o.tx)-z*Math.sin(o.tx),z2=y1*Math.sin(o.tx)+z*Math.cos(o.tx);return[o.cx+x1,o.cy+y2,z2];};
 const S=[],T=2*Math.PI;
 for(let i=0;i<o.n;i++){const u=i/o.n*T,a=P(u,-o.W),b=P(u,o.W);S.push({a,b,z:(a[2]+b[2])/2,u,k:'r'});}
 for(let i=0;i<720;i++){const u0=i/720*2*T,u1=(i+1)/720*2*T,a=P(u0,o.W),b=P(u1,o.W);S.push({a,b,z:(a[2]+b[2])/2,u:u0%T,k:'e'});}
 S.sort((p,q)=>p.z-q.z);const zs=S.map(s=>s.z),zn=Math.min(...zs),zx=Math.max(...zs);
 for(const s of S){const t=(s.z-zn)/(zx-zn),L=document.createElementNS(NS,'line');
  L.setAttribute('x1',s.a[0].toFixed(2));L.setAttribute('y1',s.a[1].toFixed(2));L.setAttribute('x2',s.b[0].toFixed(2));L.setAttribute('y2',s.b[1].toFixed(2));
  const hi=o.hi&&s.u>=o.hi[0]*T&&s.u<=o.hi[1]*T;
  if(s.k==='e'){L.setAttribute('stroke',o.ink);L.setAttribute('stroke-width',((0.8+1.6*t)*o.ew).toFixed(2));L.setAttribute('opacity',(0.35+0.65*t).toFixed(2));}
  else{L.setAttribute('stroke',hi?o.hiCol:o.ink);L.setAttribute('stroke-width',(hi?(0.9+0.9*t):(0.4+0.5*t)).toFixed(2));L.setAttribute('opacity',(hi?(0.55+0.45*t):(0.12+0.45*t)).toFixed(2));}
  L.setAttribute('stroke-linecap','round');svg.appendChild(L);}
 if(o.mark){const m=P(o.mark.u*T,o.W+o.mark.off),r=document.createElementNS(NS,'rect');r.setAttribute('x',m[0]-6);r.setAttribute('y',m[1]-6);r.setAttribute('width',12);r.setAttribute('height',12);r.setAttribute('fill','#D6DF27');r.setAttribute('stroke',o.ink);svg.appendChild(r);
  if(o.mark.t){const tx=document.createElementNS(NS,'text');tx.setAttribute('x',m[0]+16);tx.setAttribute('y',m[1]+4);tx.setAttribute('font-family','Geist Mono');tx.setAttribute('font-size','11');tx.setAttribute('letter-spacing','1.5');tx.setAttribute('fill',o.mark.c||'#20386C');tx.textContent=o.mark.t;svg.appendChild(tx);}}
}
