"""Independent checks of the newly exposed intermediate calculations."""
from pathlib import Path
import ast,json,re
import numpy as np
from scipy.integrate import quad

R=Path(__file__).resolve().parent
report={}
def derivatives(fun,x,y,h=1e-4):
    z=fun(x,y)
    return z,(fun(x+h,y)-fun(x-h,y))/(2*h),(fun(x,y+h)-fun(x,y-h))/(2*h),\
        (fun(x+h,y)-2*z+fun(x-h,y))/h**2,\
        (fun(x+h,y+h)-fun(x+h,y-h)-fun(x-h,y+h)+fun(x-h,y-h))/(4*h*h),\
        (fun(x,y+h)-2*z+fun(x,y-h))/h**2

# All six original PDEs, including the +x u_y of (f).
def coeff(n,x,y):
    s=np.sin(x);c=np.cos(x)
    return [(1,2,5,x,0,-1),(1,4*x,s*s+16*x*x,s,0,-1),
        (1,s,s*s+4*x*x,x,-1,0),(9*s*s+16*x*x,4*x,1,1,0,-1),
        (1,-s,s*s,y,-x,0),(1,s,-c*c-3,0,x,0)][n]
def coords(n,x,y):
    if n==0:return x,y-2*x
    if n==1:return -np.cos(x),y-2*x*x
    if n==2:return x*x,y+np.cos(x)
    if n==3:
        a=lambda t:9*np.sin(t)**2+16*t*t
        return quad(lambda t:3*np.sin(t)/a(t),.5,x)[0],y-quad(lambda t:4*t/a(t),.5,x)[0]
    if n==4:return x,y-np.cos(x)
    return y+np.cos(x)-2*x,y+np.cos(x)+2*x
def v(s,z):return np.sin(s)+s*z*z+np.cos(z)
def transformed(n,x,y):
    s,z=coords(n,x,y);si=np.sin(x);co=np.cos(x)
    val=v(s,z);vs=np.cos(s)+z*z;vz=2*s*z-np.sin(z)
    vss=-np.sin(s);vsz=2*z;vzz=2*s-np.cos(z)
    if n==0:return vss+vzz+x*vs-2*x*vz-val
    if n==1:return si*si*(vss+vzz)+(co+si*si)*vs+(-4-4*x*si)*vz-val
    if n==2:return 4*x*x*(vss+vzz)+(2+2*x*x)*vs+(-co-x*si-1)*vz
    if n==3:
        a=9*si*si+16*x*x;ap=18*si*co+32*x
        return 9*si*si/a*(vss+vzz)+(3*co-3*si*ap/a+3*si/a)*vs+(-4+4*x*ap/a-4*x/a)*vz-val
    if n==4:return vss+y*vs+(co+y*si-x)*vz
    return -16*vsz+(x-co)*(vs+vz)
errors=[]
for n in range(6):
    err=0
    for x,y in [(.3,.4),(.7,-.3),(1.1,.6)]:
        u,ux,uy,uxx,uxy,uyy=derivatives(lambda xx,yy:v(*coords(n,xx,yy)),x,y)
        A,B,C,D,E,K=coeff(n,x,y)
        err=max(err,abs(A*uxx+2*B*uxy+C*uyy+D*ux+E*uy+K*u-transformed(n,x,y)))
    assert err<2e-4,(n,err)
    errors.append(float(err))
report['six_canonical_substitutions']=errors

# Integrations by parts, independently compared with quadrature.
errs=[]
for n in range(1,16):
    k=n*np.pi
    errs.append(abs(quad(lambda x:x*(1-x)*np.sin(k*x),0,1)[0]-2*(1-(-1)**n)/k**3))
    kn=(n-.5)*np.pi
    errs.append(abs(quad(lambda x:(1-x)*np.cos(kn*x),0,1)[0]-1/kn**2))
    errs.append(abs(quad(lambda x:x*x*np.sin(n*x),0,np.pi)[0]-
                    (-np.pi**2*(-1)**n/n+2*((-1)**n-1)/n**3)))
    for p in [.5,1.5,2.5]:
        ell=np.log(2);kn=n*np.pi/ell
        errs.append(abs(quad(lambda z:np.exp(p*z)*np.sin(kn*z),0,ell)[0]-
                        kn*(1-(-1)**n*np.exp(p*ell))/(p*p+kn*kn)))
assert max(errs)<1e-12,max(errs)
report['intermediate_fourier_integrals_max_error']=max(errs)

# Green edge contributions against an independent area integral.
green=[]
for a,x,t in [(1,.3,.7),(2,-.2,1.1),(3,.7,.4)]:
    u=lambda y,T:y*y*T*T+T**3
    area=quad(lambda T:quad(lambda y:2*y*y+6*T-2*a*a*T*T,x-a*(t-T),x+a*(t-T))[0],0,t)[0]
    left=a*(u(x,t)-u(x-a*t,0));right=a*(u(x,t)-u(x+a*t,0))
    green.append(abs(area-left-right))
assert max(green)<1e-12,green
report['green_flux_max_error']=max(green)
for b in [.2,1.3,3.8,5.2]:
    C,S,c,s=np.cosh(b),np.sinh(b),np.cos(b),np.sin(b)
    assert abs(np.linalg.det([[C-c,S-s],[S+s,C-c]])-2*(1-C*c))<1e-10
report['beam_determinant']='passed'

# Newly expanded final Cauchy formulas and torus quadratic roots.
explicit=[
 (lambda x,y:-np.exp(x+y)+np.exp(4*x)*(y-2*x)**2+np.exp(2*x+y),
  lambda s:(0,s),lambda s:s*s),
 (lambda x,y:-np.exp(x+y)+(3+2*x-y)*np.exp(4*(x+y)/3)/3,
  lambda s:(s,-s),lambda s:s),
 (lambda x,y:-np.exp(x+y)+(y-2*x)**2*np.exp(8*x-2*y)/4+np.exp(3*x+y/2),
  lambda s:(s,4*s),lambda s:s*s)]
for fun,curve,data in explicit:
    for s in [-.2,0,.2]:
        assert abs(fun(*curve(s))-data(s))<1e-12
    for x,y in [(.1,.2),(-.1,.3)]:
        u,ux,uy,*_=derivatives(fun,x,y)
        assert abs(ux+2*uy-4*u-np.exp(x+y))<1e-5
for rho,z,torus_radius,a in [(2.3,.4,2.5,.8),(2.1,-.5,2.5,.8),(2.4,0,2.5,.8)]:
    A=rho*rho+torus_radius**2+z*z-a*a
    disc=4*rho*rho*(z*z+torus_radius**2)-A*A
    assert disc>0
    for sign in [-1,1]:
        mu=(-A*z+sign*torus_radius*np.sqrt(disc))/(2*rho*(z*z+torus_radius**2))
        assert abs((A+2*z*rho*mu)**2-4*torus_radius**2*rho*rho*(1-mu*mu))<1e-10
report['expanded_cauchy_formulas_and_torus_roots']='passed'

# Preserve second/fourth derivatives while converting prose quotation marks.
tree=ast.parse((R/'build_markdown.py').read_text(encoding='utf-8'))
mini=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('styled','markdown')],type_ignores=[])
scope={'re':re};exec(compile(mini,'markdown_regression','exec'),scope)
sample=chr(96)*2+r"""Nghiệm'' có $f''(x)$ và \[X''''=\lambda X,\quad \int X''Y''.\]"""
rendered=scope['markdown'](sample)
assert '“Nghiệm”' in rendered
assert "$f''(x)$" in rendered and "X''''" in rendered and "X''Y''" in rendered,rendered
report['markdown_derivative_primes']='passed'
ledger=json.loads((R/'ra_soat_buoc_trung_gian_123.json').read_text(encoding='utf-8'))
assert len(ledger)==205 and len({v['id'] for v in ledger})==205
report['reviewed_items']=len(ledger)
report['expanded_items']=sum(v['status']=='expanded' for v in ledger)
for n in (1,2,3):
    text=(R/f'chapter{n}_detailed.tex').read_text(encoding='utf-8')
    assert not any(ord(c)<32 and c not in '\r\n\t' for c in text)
(R/'verification_intermediate_steps.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
