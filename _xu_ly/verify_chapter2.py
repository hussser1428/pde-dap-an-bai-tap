"""Đối chiếu số độc lập: PDE gốc, dữ liệu, phép đổi biến và công thức Hessian."""
from pathlib import Path
import json,re
import numpy as np
from scipy.integrate import quad
import fitz
from chapter2_graphs import u3,u4c,u4e,u5,u8,u9

r=Path(__file__).resolve().parent;out=r.parent/'PDE_Tach_bai_va_loi_giai'
def derivatives(fun,point,h=2e-4):
    p=np.asarray(point,float);n=len(p);u=fun(*p);g=np.zeros(n);H=np.zeros((n,n))
    for i in range(n):
        a=np.eye(n)[i]*h;g[i]=(fun(*(p+a))-fun(*(p-a)))/(2*h)
        H[i,i]=(fun(*(p+a))-2*u+fun(*(p-a)))/h**2
        for j in range(i):
            b=np.eye(n)[j]*h
            H[i,j]=H[j,i]=(fun(*(p+a+b))-fun(*(p+a-b))-fun(*(p-a+b))+fun(*(p-a-b)))/(4*h*h)
    return u,g,H
ops={
3:lambda x,y,u,g,H:3*H[0,0]-2*H[0,1]-5*H[1,1]-x-x*y,
4:lambda x,y,u,g,H:15*H[0,0]-2*H[0,1]-H[1,1],
5:lambda x,y,u,g,H:3*H[0,0]+2*H[0,1]-5*H[1,1]+3*g[0]+5*g[1],
6:lambda x,y,u,g,H:H[0,0]-10*H[0,1]+25*H[1,1]-np.exp(x),
7:lambda x,y,u,g,H:H[0,0]-6*H[0,1]+9*H[1,1]-np.exp(x),
8:lambda x,y,u,g,H:4*H[0,0]-4*H[0,1]+H[1,1]-np.exp(x),
9:lambda x,y,u,g,H:25*H[0,0]-10*H[0,1]+H[1,1]-10*g[0]+2*g[1]-15*np.exp(x),
10:lambda x,y,u,g,H:8*H[0,0]+8*H[0,1]+2*H[1,1]-2*g[0]-g[1],
11:lambda x,y,u,g,H:2*x*y*H[0,0]+(2*y*y-3*x*x)*H[0,1]-3*x*y*H[1,1],
14:lambda x,y,u,g,H:np.exp(2*x)*H[0,0]+2*np.exp(x)*H[0,1]+H[1,1]+np.exp(2*x)*g[0]-np.exp(2*x),
15:lambda x,y,u,g,H:np.tan(x)**2*H[0,0]-2*y*np.tan(x)*H[0,1]+y*y*H[1,1]+np.tan(x)**3*g[0]+2*y*g[1]-np.tan(x)**3,
16:lambda x,y,u,g,H:H[0,0]-2*np.sin(x)*H[0,1]+(2-np.cos(x)**2)*H[1,1]-np.cos(x)*g[1],
17:lambda x,y,u,g,H:y*y*H[0,0]-2*y*y*H[0,1]+(y*y+1)*H[1,1]-y*g[0]-(1-y*y)/y*g[1],
18:lambda x,y,u,g,H:H[0,0]+2*x*x*H[0,1]+(x**4+1)*H[1,1]+2*x*g[1]+u}
funcs={3:[u3],4:[u4c,u4e],5:[u5,lambda x,y:u5(x,y)+(5*x-3*y)**2],
6:[lambda x,y:np.exp(x)-np.cos(5*x+y)],7:[lambda x,y:np.exp(x)+x*(y+3*x)**2/9+np.sin(y+3*x)],
8:[u8,lambda x,y:u8(x,y)+(x+2*y)**2],9:[u9,lambda x,y:u9(x,y)+x+5*y],
10:[lambda x,y:np.cos(x-2*y)+2*(1-np.exp(y/2))*np.sin(x-2*y)],
11:[lambda x,y:x+1-np.sqrt(x*x+2*y*y/3)],14:[lambda x,y:x+2*y+np.exp(-x)],
15:[lambda x,y:x+.7*np.sin(x),lambda x,y:x+.7*np.sin(x)+y*np.sin(x)],
16:[lambda x,y:x*(y-np.cos(x))],
17:[lambda x,y:(x+y-np.arctan(y)-np.log(2))*np.log(1+y*y)+np.log(2)**2],
18:[lambda x,y:np.cos(y-x**3/3)]}
errors={}
for n,functions in funcs.items():
    for j,fun in enumerate(functions):
        err=0
        for x,y in [(.2,.4),(.45,.7),(.7,1.1)]:
            residual=ops[n](x,y,*derivatives(fun,(x,y)))
            if n==4:residual-=1 if j==0 else np.exp(x+3*y)
            err=max(err,abs(residual))
        assert err<4e-4,(n,j,err);errors[f'BT{n}_{j+1}']=float(err)

# Actual data of each problem, tested independently from the source PDE.
data=[]
def close(a,b):
    err=float(abs(a-b));assert err<5e-6,(a,b,err);data.append(err)
for t in [-.4,0,.3,.7]:
    close(u3(t,t),np.exp(t));close(u3(3*t,-5*t),t+1)
    close(u4c(3*t,t),np.sin(t));close(u4c(t,0),t)
    close(u4e(t,0),t);close(derivatives(u4e,(t,0))[1][1],np.sin(t)+1)
    for fun in funcs[5]:
        close(fun(3*t,5*t),8*t);close(derivatives(fun,(3*t,5*t))[1][1],3*t+1)
    for fun in funcs[8]:
        close(fun(2*t,-t),np.exp(2*t)/4);close(derivatives(fun,(2*t,-t))[1][1],t+1)
    for fun in funcs[9]:close(fun(t,-t/5),np.exp(t)+np.exp(2*t/5))
    f=funcs[6][0];close(f(t,0),np.exp(t)-np.cos(5*t));close(derivatives(f,(t,0))[1][1],np.sin(5*t))
    f=funcs[7][0];close(f(t,0),np.exp(t)+np.sin(3*t)+t**3);close(f(0,t),1+np.sin(t))
    f=funcs[10][0];close(f(t,0),np.cos(t));close(derivatives(f,(t,0))[1][1],np.sin(t))
    f=funcs[14][0];close(f(0,t),2*t+1);close(derivatives(f,(0,t))[1][0],0)
    f=funcs[16][0];close(f(0,t),0);close(derivatives(f,(0,t))[1][0],t-1)
    f=funcs[17][0];close(f(t,1),(t+1-np.pi/4)*np.log(2));close(derivatives(f,(t,1))[1][1],t+1-np.pi/4-np.log(2)/2)
    f=funcs[18][0];close(f(0,t),np.cos(t));close(derivatives(f,(0,t))[1][0],0)
for t in [.1,.4,1.2]:
    for fun in funcs[15]:close(fun(t,0),t+.7*np.sin(t))
for theta in [.3,1.2,2.7]:
    close(funcs[11][0](np.cos(theta),np.sqrt(3/2)*np.sin(theta)),np.cos(theta))
for t in [1,1.4,2]:close(funcs[11][0](t,0),1)

# Three-variable canonical forms, using matrices read from original coefficients.
Ms=[np.array([[1,1,1],[1,2,0],[1,0,3]]),np.array([[1,2,6],[2,4,3],[6,3,9]]),np.array([[3,-1,1],[-1,2,2],[1,2,3]])]
Ts=[np.array([[1,0,0],[-1,1,0],[-2,1,1]]),
np.array([[1,0,0],[0,1/np.sqrt(3),-1/(3*np.sqrt(3))],[-2/np.sqrt(3),0,1/(3*np.sqrt(3))]]),
np.array([[1/np.sqrt(3),0,0],[np.sqrt(3/5)/3,np.sqrt(3/5),0],[-4*np.sqrt(5/3)/5,-7*np.sqrt(5/3)/5,np.sqrt(5/3)]])]
for n,(M,T) in enumerate(zip(Ms,Ts)):
    assert np.max(abs(T@M@T.T-np.diag([1,1,1 if n==0 else -1])))<1e-12

# Complete spherical/toroidal Hessian: pull back a known Cartesian polynomial.
def poly(x,y,z):return x*x+2*y*y+3*z*z+x*y+x*z+y*z+.1*x**3
coordinate_errors=[]
for R in [0,2.5]:
    for rad,theta,phi in [(.4,.5,.7),(.7,1.2,2),(.9,2.4,-.6)]:
        s=np.sin(theta);c=np.cos(theta);p=np.cos(phi);q=np.sin(phi);rho=R+rad*s
        def forward(r0,t0,f0):return ((R+r0*np.sin(t0))*np.cos(f0),(R+r0*np.sin(t0))*np.sin(f0),r0*np.cos(t0))
        def v(r0,t0,f0):return poly(*forward(r0,t0,f0))
        _,g,H=derivatives(v,(rad,theta,phi))
        K=np.array([[H[0,0],H[0,1]/rad-g[1]/rad**2,H[0,2]/rho-s*g[2]/rho**2],
        [H[0,1]/rad-g[1]/rad**2,H[1,1]/rad**2+g[0]/rad,H[1,2]/(rad*rho)-c*g[2]/rho**2],
        [H[0,2]/rho-s*g[2]/rho**2,H[1,2]/(rad*rho)-c*g[2]/rho**2,H[2,2]/rho**2+s*g[0]/rho+c*g[1]/(rad*rho)]])
        E=np.array([[s*p,c*p,-q],[s*q,c*q,p],[c,-s,0]])
        x,y,z=forward(rad,theta,phi);expected=np.array([[2+.6*x,1,1],[1,4,1],[1,1,6]])
        err=float(np.max(abs(E@K@E.T-expected)));assert err<8e-5,(R,err);coordinate_errors.append(err)

# Variable-coefficient (i.d) uses +u_x in the original, not +x u_x.
for x,y in [(.3,.4),(1.2,-.2),(2.4,.7)]:
    a=9*np.sin(x)**2+16*x*x;ap=18*np.sin(x)*np.cos(x)+32*x
    h=3*np.sin(x)/a;k=-4*x/a
    hp=3*np.cos(x)/a-3*np.sin(x)*ap/a**2;kp=-4/a+4*x*ap/a**2
    M=np.array([[a,4*x],[4*x,1]]);T=np.array([[h,0],[k,1]])
    assert np.max(abs(T@M@T.T-np.eye(2)*9*np.sin(x)**2/a))<1e-12
    assert abs((a*hp+h)-(3*np.cos(x)-3*np.sin(x)*ap/a+3*np.sin(x)/a))<1e-12
    assert abs((a*kp+k)-(-4+4*x*ap/a-4*x/a))<1e-12

# Example 8: independent arbitrary F,G and all three reconstructed-data formulas.
F=lambda s:np.sin(s)+s*s;G=lambda s:np.cos(s)+s
v8=lambda x,y:F(x-y)+np.exp(-(x-y))*G(x-2*y)
for x,y in [(.2,.4),(-.3,.5),(.6,-.2)]:
    u,g,H=derivatives(v8,(x,y));close(2*H[0,0]+3*H[0,1]+H[1,1]+g[0]+g[1],0)
    u0=lambda t:F(t)+np.exp(-t)*G(t)
    u0p=lambda t:np.cos(t)+2*t+np.exp(-t)*(-np.sin(t)+1-G(t))
    u1=lambda t:-(np.cos(t)+2*t)+np.exp(-t)*G(t)-2*np.exp(-t)*(-np.sin(t)+1)
    a=x-y;b=x-2*y
    close(v8(x,y),u0(a)-np.exp(-a)*quad(lambda t:np.exp(t)*(u0p(t)+u1(t)),a,b)[0])

# Example 9 and the sign defect in Example 6.
for x,y in [(.2,.4),(-.3,.7),(.6,1.2)]:
    fun=lambda x,y:x*x+y*y+2*y-3
    u,g,H=derivatives(fun,(x,y));close(x*y*H[0,0]+(y*y-x*x)*H[0,1]-x*y*H[1,1],0)
close((.5*1**2),.5) # f=1 yields the printed F=y^2/2; LF=1.
Fprint=lambda x,y:quad(lambda t:quad(lambda s:1,2*t+x-2*y,t+x-y)[0],0,y)[0]
u,g,H=derivatives(Fprint,(.3,.7));close(2*H[0,0]+3*H[0,1]+H[1,1],1)

# Wave coordinate transformation and boundary control with compatible data.
k=np.pi/18;Phi=lambda z:np.sin(k*z)
for x,t in [(1,.2),(2,.7),(3,1.3)]:
    f=lambda x,t:np.sin(k*x**3/3)*np.cos(k*t)
    u,g,H=derivatives(f,(x,t));res=x*H[0,0]-x**5*H[1,1]-2*g[0]
    assert abs(res)<1e-4,(x,t,res)
for tau in np.linspace(0,9,19):close(-.5*(Phi(18-tau)-Phi(tau)),0)
for z in np.linspace(0,9,19):close(np.sin(k*z)*np.cos(k*9),0)

# Characteristic Cauchy compatibility in BT13, including two different solutions.
Phi13=lambda z:np.sin(z);lam=.3
for j in [0,1]:
    f=lambda x,y:np.sin((np.arctan(x)+y)/2)+lam*(np.arctan(x)-y)+j*(np.arctan(x)-y)**2
    for x,y in [(.2,.4),(-.3,.5),(.6,-.2)]:
        u,g,H=derivatives(f,(x,y));res=(1+x*x)**2*H[0,0]-H[1,1]+2*x*(1+x*x)*g[0]
        assert abs(res)<1e-5,res
    for x in [-.4,.3,.8]:
        z=np.arctan(x);close(f(x,z),Phi13(z));close(derivatives(f,(x,z))[1][1],.5*np.cos(z)-lam)

rows=[i for i in json.loads((out/'manifest.json').read_text(encoding='utf-8')) if i['section'].startswith('2.')]
assert len(rows)==27
for row in rows:
    md=(out/row['file']).with_suffix('.md');s=md.read_text(encoding='utf-8')
    assert '## Kiến thức và trình tự giải' in s and '## Lời giải áp dụng cho bài' in s,row['id']
    assert 'Bước 1' in s and s.count('$$')%2==0,row['id']
    assert not any(ord(c)<32 and c not in '\n\t\r' for c in s)
    tex=out/'Nguon_loi_giai'/(row['id']+'.tex');assert tex.exists()
    pdf=fitz.open(out/row['file']);assert len(pdf)==row['original_pages']+row['solution_pages']
    assert row['solution_pages']>=1 and row['id'] in pdf[row['original_pages']].get_text();pdf.close()
report={'chapter2_items':len(rows),'pde_residuals':errors,'data_checks':len(data),'max_data_error':max(data),
'three_dimensional_canonical_forms':'passed','spherical_and_toroidal_hessians':coordinate_errors,
'variable_coefficient_canonical_form':'passed','characteristic_compatibility':'passed','wave_boundary_control':'passed',
'example6_sign_discrepancy':'confirmed against printed PDE','artifacts':'27 Markdown/PDF/LaTeX sets passed'}
(r/'verification_chapter2.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
