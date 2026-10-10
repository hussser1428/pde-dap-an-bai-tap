from pathlib import Path
import json,re
import numpy as np
import fitz
from scipy.integrate import quad
root=Path(__file__).parent.parent;out=root/'PDE_Tach_bai_va_loi_giai'
rows=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
assert len(rows)==336
assert len({i['id'] for i in rows})==336
broken=[];badmath=[]
for row in rows:
    md=out/Path(row['file']).with_suffix('.md');s=md.read_text(encoding='utf-8')
    if s.count('$$')%2:badmath.append(md.name)
    if re.search(r'\\(?:textbf|emph|includegraphics|begin\{align\*)',s):badmath.append(md.name)
    plain=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
    plain=re.sub(r'\$[^$\n]*\$','',plain)
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',plain):
        if not (md.parent/link).resolve().exists():broken.append((md.name,link))
    d=fitz.open(out/row['file']);assert len(d)==row['original_pages']+row['solution_pages'],row['id']
    assert all(p.rect.width>0 and p.rect.height>0 for p in d)
    d.close()
assert not broken,broken[:5];assert not badmath,badmath
# Numerical residuals verify explicit formulas against the source PDE,
# independently of TeX generation and formatting.
def deriv(f,x,y,h=2e-4):
    u=f(x,y);ux=(f(x+h,y)-f(x-h,y))/(2*h);uy=(f(x,y+h)-f(x,y-h))/(2*h)
    xx=(f(x+h,y)-2*u+f(x-h,y))/h**2;yy=(f(x,y+h)-2*u+f(x,y-h))/h**2
    xy=(f(x+h,y+h)-f(x+h,y-h)-f(x-h,y+h)+f(x-h,y-h))/(4*h*h)
    return u,ux,uy,xx,xy,yy
P=lambda x,y:x**3*(1+y)/18+x**4/108
def f3(x,y):
    xi=y-x;eta=5*x+3*y
    return P(x,y)-xi/8-P(-3*xi/8,5*xi/8)+np.exp(eta/8)-P(eta/8,eta/8)
cases={
3:(f3,lambda x,y,u,ux,uy,xx,xy,yy:3*xx-2*xy-5*yy-(x+x*y)),
5:(lambda x,y:(x+y)*np.exp(-(5*x-3*y)/8),lambda x,y,u,ux,uy,xx,xy,yy:3*xx+2*xy-5*yy+3*ux+5*uy),
6:(lambda x,y:np.exp(x)-np.cos(5*x+y),lambda x,y,u,ux,uy,xx,xy,yy:xx-10*xy+25*yy-np.exp(x)),
7:(lambda x,y:np.exp(x)+x*(y+3*x)**2/9+np.sin(y+3*x),lambda x,y,u,ux,uy,xx,xy,yy:xx-6*xy+9*yy-np.exp(x)),
8:(lambda x,y:np.exp(x)/4+x*(x+2*y)/4+(x+2*y)/2,lambda x,y,u,ux,uy,xx,xy,yy:4*xx-4*xy+yy-np.exp(x)),
9:(lambda x,y:np.exp(x)+np.exp(2*x/5),lambda x,y,u,ux,uy,xx,xy,yy:25*xx-10*xy+yy-10*ux+2*uy-15*np.exp(x)),
10:(lambda x,y:np.cos(x-2*y)+2*(1-np.exp(y/2))*np.sin(x-2*y),lambda x,y,u,ux,uy,xx,xy,yy:8*xx+8*xy+2*yy-2*ux-uy),
14:(lambda x,y:x+2*y+np.exp(-x),lambda x,y,u,ux,uy,xx,xy,yy:np.exp(2*x)*xx+2*np.exp(x)*xy+yy+np.exp(2*x)*ux-np.exp(2*x)),
16:(lambda x,y:x*(y-np.cos(x)),lambda x,y,u,ux,uy,xx,xy,yy:xx-2*np.sin(x)*xy+(2-np.cos(x)**2)*yy-np.cos(x)*uy),
17:(lambda x,y:(x+y-np.arctan(y)-np.log(2))*np.log(1+y*y)+np.log(2)**2,lambda x,y,u,ux,uy,xx,xy,yy:y*y*xx-2*y*y*xy+(y*y+1)*yy-y*ux-(1-y*y)/y*uy),
18:(lambda x,y:np.cos(y-x**3/3),lambda x,y,u,ux,uy,xx,xy,yy:xx+2*x*x*xy+(x**4+1)*yy+2*x*uy+u)}
residuals={}
for n,(fun,op) in cases.items():
    err=max(abs(op(x,y,*deriv(fun,x,y))) for x,y in [(0.2,.4),(.6,.8),(-.3,1.1)])
    assert err<2e-4,(n,err);residuals[str(n)]=float(err)
# Fourier signs and coefficients, checked by quadrature on original data.
for n in range(1,9):
    a=2*(quad(lambda x:x*np.sin(n*np.pi*x),0,.5)[0]+quad(lambda x:(x-1)*np.sin(n*np.pi*x),.5,1)[0])
    assert abs(a+2*np.cos(n*np.pi/2)/(n*np.pi))<1e-11
    b=2*quad(lambda x:x*(1-x)*np.sin(n*np.pi*x),0,1)[0]
    assert abs(b-4*(1-(-1)**n)/(n**3*np.pi**3))<1e-11
report={'items':336,'markdown_files':336,'supplemented_items':sum(i['solution_pages']>0 for i in rows),'broken_links':broken,'bad_math_blocks':badmath,'pde_residuals':residuals,'fourier_coefficient_checks':'passed'}
(root/'_xu_ly'/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
