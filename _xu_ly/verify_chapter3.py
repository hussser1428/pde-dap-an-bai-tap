"""Kiểm tra độc lập: dữ liệu gốc, quadrature, biên, PDE và trị riêng."""
from pathlib import Path
import json,re
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from wave_graphs import cfg,extension
from chapter3_graphs import half_cases,full_cases,beam_roots,beam_mode
r=Path(__file__).resolve().parent
checks={}
def close(a,b,tol=1e-8):assert np.max(np.abs(np.asarray(a)-b))<tol,(a,b)
def d2(fun,x,t,h=3e-4):
    u=fun(x,t)
    return (fun(x+h,t)-2*u+fun(x-h,t))/h**2,(fun(x,t+h)-2*u+fun(x,t-h))/h**2

# Actual initial velocities, separate from the primitive implementations.
vel={
1:lambda s:s*((s>-1)&(s<0)),2:lambda s:((s>1)&(s<2))*1.,
3:lambda s:s*((s>1)&(s<2)),4:lambda s:s*((s>0)&(s<1)),5:lambda s:((s>-1)&(s<1))*1.,
6:lambda s:6*np.sign(s),7:lambda s:(abs(s)-1)*(abs(s)<1),8:lambda s:6+0*s,
9:lambda s:np.sign(s)*(2*abs(s)-2)*(abs(s)<2),10:lambda s:(2-abs(s))*(abs(s)<2),
11:lambda s:((abs(s)>1)&(abs(s)<2))*1.,12:lambda s:((abs(s)>1)&(abs(s)<2))*1.,
13:lambda s:s*((abs(s)>1)&(abs(s)<2)),14:lambda s:abs(s)*((abs(s)>2)&(abs(s)<3)),
15:lambda s:extension(np.array(s),lambda x:np.ones_like(x),1),16:lambda s:0*s,
17:lambda s:0*s,18:lambda s:extension(np.array(s),lambda x:np.ones_like(x),1),
19:lambda s:extension(np.array(s),lambda x:x,np.pi,'even','even'),
20:lambda s:extension(np.array(s),lambda x:np.minimum(x,np.pi-x),np.pi),
21:lambda s:extension(np.array(s),lambda x:np.ones_like(x),1,'odd','even'),22:lambda s:0*s,
}
def solution(n):
    a,f,H,*_=cfg[n]
    return lambda x,t:(f(x-a*t)+f(x+a*t))/2+(H(x+a*t)-H(x-a*t))/(2*a)+(1 if n==18 else 0)+(x if n==19 else 0)

primitive_error=0.
for n in range(1,23):
    a,f,H,*_=cfg[n]
    for lo,hi in [(-4.37,3.91),(-.73,.47),(.37,1.79)]:
        points=[p for p in np.concatenate((np.arange(-10,11)/4,np.arange(-4,5)*np.pi/2)) if lo<p<hi]
        integral=quad(lambda s:float(vel[n](s)),lo,hi,points=sorted(set(points)),epsabs=1e-9,limit=300)[0]
        err=abs(float(H(np.array(hi))-H(np.array(lo)))-integral);primitive_error=max(err,primitive_error)
        assert err<2e-7,(n,err)
    # At non-break points check velocity and displacement from t=0.
    for x in (.137,.413,.873):
        u=solution(n);h=1e-6
        close((u(x,h)-u(x,-h))/(2*h),vel[n](x),2e-6)
        close(u(x,0),f(np.array(x))+(1 if n==18 else 0)+(x if n==19 else 0))
checks['22_primitives_vs_original_velocity_integrals']=primitive_error

# Correct Neumann reflection in Bài 11, and comparison with integral of even data.
for t in (.35,1.3,2.7):
    u=solution(11);h=1e-5
    close((u(h,t)-u(-h,t))/(2*h),0,1e-8)
close(solution(11)(.4,3),1)
checks['Neumann_Bai_11_boundary_and_tail']='passed'
for t in (.125,.5,1):
    close(solution(18)(0,t),1)
    close(solution(18)(1,t),1)
f_example=lambda s:s*(s+1)*((-1<s)&(s<0))
u_example=lambda x:.5*(f_example(x-.5)+f_example(x+.5))
h=1e-6
close((u_example(-.5)-u_example(-.5-h))/h,.5,2e-6)
close((u_example(-.5+h)-u_example(-.5))/h,-.5,2e-6)
checks['meeting_wavefronts_boundary_values_and_one_sided_derivatives']='passed'

# Corrected half-line case (v): initial velocity zero, actual boundary h.
u=half_cases()[4]
for x in (.23,.61,2.1):
    close(u(x,0),np.cos(x)-np.sin(x))
    close((u(x,1e-6)-u(x,-1e-6))/2e-6,0,1e-7)
for t in (.13,.8,1.6):close(u(0,t),np.cos(2*t)-np.sin(2*t))
for x,t in ((2,.3),(.2,.8),(3,.7),(.4,1.3)):
    xx,tt=d2(u,x,t);close(tt,4*xx,2e-6)
checks['half_line_case_v_initial_data_boundary_PDE']='passed'

# Forced solutions: residuals checked against source, using independent finite differences.
cases=[
(lambda x,t:x*t**3/6,1,lambda x,t:x*t),
(lambda x,t:np.exp(-x)*np.cosh(2*t)+np.sin(2*x)*np.sin(4*t)/4+x*(1-np.cos(t)),2,lambda x,t:x*np.cos(t)),
(lambda x,t:(np.arctan(x+3*t)-np.arctan(x-3*t))/6+np.exp(x)*(np.cosh(3*t)-1)/9+t-np.sin(t),3,lambda x,t:np.exp(x)+np.sin(t)),
(lambda x,t:x*x+16*t*t+np.sin(x)*np.sin(4*t)/4+x*t*t/2+t**3/6,4,lambda x,t:x+t),
(lambda x,t:x+np.cos(x)*np.sin(t)+(np.sin(x)*t*np.sin(t)+np.cos(x)*(np.sin(t)-t*np.cos(t)))/2,1,lambda x,t:np.sin(x+t)),
]
errs=[]
for fun,a,source in cases:
    for x,t in ((.23,.17),(.61,.41),(-.4,.29)):
        xx,tt=d2(fun,x,t);err=abs(tt-a*a*xx-source(x,t));errs.append(err);assert err<3e-5,(a,x,t,err)
checks['forced_PDE_max_residual']=max(errs)

# Non-resonant and resonant responses; verify zero data and source separately.
for source in ('sin','cos'):
    for w,alpha in [(2.3,.7),(2.3,2.3)]:
        if source=='cos':fun=(lambda t:t*np.sin(w*t)/(2*w)) if w==alpha else (lambda t:(np.cos(alpha*t)-np.cos(w*t))/(w*w-alpha*alpha))
        else:fun=(lambda t:np.sin(w*t)/(2*w*w)-t*np.cos(w*t)/(2*w)) if w==alpha else (lambda t:(np.sin(alpha*t)-(alpha/w)*np.sin(w*t))/(w*w-alpha*alpha))
        close(fun(0),0);close((fun(1e-6)-fun(-1e-6))/2e-6,0,1e-8)
        for t in (.17,.51):
            h=1e-4;tt=(fun(t+h)-2*fun(t)+fun(t-h))/h**2
            close(tt+w*w*fun(t),np.sin(alpha*t) if source=='sin' else np.cos(alpha*t),5e-7)
checks['resonance_and_zero_data']='passed'

# Fourier integrals computed from original functions on their actual intervals.
for n in range(1,11):
    close(2/np.pi*quad(lambda x:np.sin(np.pi*x)*np.sin(n*x),0,np.pi)[0],2*(-1)**n*n*np.sin(np.pi**2)/(np.pi*(np.pi**2-n*n)))
    close(2*quad(lambda x:x*(1-x)*np.sin(n*np.pi*x),0,1)[0],4*(1-(-1)**n)/(n**3*np.pi**3))
    close(2/np.pi*(quad(lambda x:x*np.sin(n*x),0,np.pi/2)[0]+quad(lambda x:(np.pi-x)*np.sin(n*x),np.pi/2,np.pi)[0]),4*np.sin(n*np.pi/2)/(np.pi*n*n))
    k=n-.5
    close(2/np.pi*quad(lambda x:x*np.sin(k*x),0,np.pi)[0],2*(-1)**(n-1)/(np.pi*k*k))
    close(2/np.pi*quad(lambda x:(np.pi-x)*np.cos(k*x),0,np.pi)[0],2/(np.pi*k*k))
checks['50_Fourier_coefficients_vs_quadrature']='passed'

# Beam boundary conditions directly on analytic derivative formulas.
ba,bb=beam_roots();roots=[ba,bb]
for kind,b in enumerate(roots):
    sigma=1/np.tanh(b) if kind==0 else np.tanh(b)
    def X(x):return np.cosh(b*x)-np.cos(b*x)-sigma*(np.sinh(b*x)-np.sin(b*x))
    def Xp(x):return b*(np.sinh(b*x)+np.sin(b*x)-sigma*(np.cosh(b*x)-np.cos(b*x)))
    def Xpp(x):return b*b*(np.cosh(b*x)+np.cos(b*x)-sigma*(np.sinh(b*x)+np.sin(b*x)))
    def Xppp(x):return b**3*(np.sinh(b*x)-np.sin(b*x)-sigma*(np.cosh(b*x)+np.cos(b*x)))
    close(X(0),0);close(Xp(0),0)
    if kind==0:close(X(1),0,1e-9);close(Xpp(1),0,1e-8)
    else:close(Xp(1),0,1e-8);close(Xppp(1),0,1e-8)
    # Integral Rayleigh identity for the actual BC, verifies no missing sign.
    close(quad(lambda x:Xpp(x)**2,0,1)[0],b**4*quad(lambda x:X(x)**2,0,1)[0],2e-7)
checks['beam_corrected_roots_and_four_boundary_conditions']=roots

# Mixed reflection period checked on an explicit example, not a sine series.
f=lambda s:extension(np.array(s),lambda x:((x>.25)&(x<1/3)).astype(float),1,'odd','even')
for s in (.29,.7,1.71,2.3,3.2):close(f(s+2),-f(s));close(f(s+4),f(s))
assert f(.29)!=f(2.29)
checks['mixed_boundary_antiperiod_2_period_4']='passed'

# Multidimensional normalization, sphere cap and source primitive from radial PDE.
def K(r,t,R=1,c=1):
    if t<=0:return 0.
    if r==0:return t*(c*t<R)
    return t*np.clip((R*R-(r-c*t)**2)/(4*r*c*t),0,1)
def J(r,t,R=1,c=1):
    if r==0:return .5*min(t,R/c)**2
    b=abs(R-r)/c;q=np.clip(t,b,(R+r)/c)
    A=lambda s:((R*R-r*r)*s+r*c*s*s-c*c*s**3/3)/(4*r*c)
    return .5*min(t,max(R-r,0)/c)**2+A(q)-A(b)
for R,c in ((1,1),(2,2)):
    for r0 in (.31,.89,1.43,2.2):
        for t in (.2,.71,1.3,3.9):
            pts=sorted(set(p for p in (abs(R-r0)/c,(R+r0)/c) if 0<p<t))
            close(J(r0,t,R,c),quad(lambda s:K(r0,s,R,c),0,t,points=pts)[0])
    for r0 in (.3,.7,1.4,2.3):
        expected=R**3/(3*c*c*r0) if r0>=R else (3*R*R-r0*r0)/(6*c*c)
        close(J(r0,10,R,c),expected)
checks['radial_source_primitive_vs_Duhamel_integral']='passed'
poly=lambda x,y,t:-(x*x+y*y-t*t)*x*y*t/18
h=2e-4
for x,y,t in ((.1,.2,-.7),(.3,-.1,-.9)):
    base=poly(x,y,t)
    dd=lambda dim:(poly(x+h*(dim==0),y+h*(dim==1),t+h*(dim==2))-2*base+poly(x-h*(dim==0),y-h*(dim==1),t-h*(dim==2)))/h**2
    close(dd(2)-dd(0)-dd(1),x*y*t,1e-7)
    close(poly(x,y,-np.sqrt(x*x+y*y)),0)
checks['cone_polynomial_sign_source_trace']='passed'

# 85 item coverage and meaningful section headings, including all 23 examples.
inv=json.loads((r/'inventory.json').read_text(encoding='utf-8'))
ids={i['id'] for i in inv if i['section'].startswith('3.')}
sol=json.loads((r/'solutions.json').read_text(encoding='utf-8'))
assert len(ids)==85 and all(i in sol for i in ids)
assert all('bước 1' in sol[i].lower() and 'bước 2' in sol[i].lower() for i in ids)
checks['coverage']={'total':85,'examples':sum(i.startswith('VD_') for i in ids),'exercises':sum(i.startswith('BT_') for i in ids)}
(r/'verification_chapter3.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=True,indent=2))
