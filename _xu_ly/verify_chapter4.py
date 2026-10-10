"""Kiểm tra số độc lập các phép tính Chương 4 trên đúng dữ liệu gốc."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import erfc

R=Path(__file__).resolve().parent
errors={};counts={}
def check(group,actual,expected,tol=2e-9):
    err=float(abs(actual-expected))
    assert err<tol,(group,actual,expected,err)
    errors[group]=max(errors.get(group,0.),err)
    counts[group]=counts.get(group,0)+1

def roots(fun):
    grid=np.linspace(1e-5,18,18001)
    found=[]
    for x,y in zip(grid[:-1],grid[1:]):
        if fun(x)*fun(y)<0:
            k=brentq(fun,x,y)
            if not found or abs(k-found[-1])>1e-6:found.append(k)
    return found[:5]

# Orthogonality projections use the original functions, not the displayed coefficients.
for n in range(1,13):
    k=n*np.pi;s=(-1)**n
    check('Dirichlet_polynomial',2*quad(lambda x:x*(1-x)*np.sin(k*x),0,1)[0],
          4*(1-s)/k**3)
    check('Dirichlet_nonmode_sine',2/np.pi*quad(lambda x:np.sin(np.pi*x)*np.sin(n*x),0,np.pi)[0],
          2*s*n*np.sin(np.pi**2)/(np.pi*(np.pi**2-n*n)))
    check('Neumann_sine',2/np.pi*quad(lambda x:np.sin(x)*np.cos(n*x),0,np.pi)[0],
          4/(np.pi*(1-n*n)) if n%2==0 else 0)
    check('Neumann_sine3',2/np.pi*quad(lambda x:np.sin(3*x)*np.cos(n*x),0,np.pi)[0],
          12/(np.pi*(9-n*n)) if n%2==0 else 0)
    check('Discontinuous_sine',2/np.pi*quad(lambda x:np.sin(n*x),0,np.pi/2)[0],
          2*(1-np.cos(n*np.pi/2))/(np.pi*n))
    k=n*np.pi/2
    check('Lifted_polynomial',quad(lambda x:(x*x-2*x-2)*np.sin(k*x),0,2)[0],
          -2*(1-s)*(1/k+1/k**3))
    check('Triangular_source',quad(lambda x:x*np.sin(k*x),0,1)[0]+quad(lambda x:(2-x)*np.sin(k*x),1,2)[0],
          2*np.sin(k)/k**2)
    check('Periodic_projection',2*quad(lambda x:(1+2*np.cos(2*np.pi*x)-2*np.sin(3*np.pi*x))*np.cos(2*n*np.pi*x),0,1)[0],
          2*(n==1)-24/(np.pi*(9-4*n*n)))

# Robin eigenfunctions, endpoint equations, norms and source coefficients.
for bc in ('RD','NR','RR','RN'):
    L=1. if bc!='RN' else np.pi
    characteristic={'RD':lambda k:k*np.cos(k*L)+np.sin(k*L),
                    'NR':lambda k:k*np.sin(k*L)-np.cos(k*L),
                    'RR':lambda k:(1-k*k)*np.sin(k*L)+2*k*np.cos(k*L),
                    'RN':lambda k:k*np.sin(k*L)-np.cos(k*L)}[bc]
    for k in roots(characteristic):
        mixed=bc in ('RD','RR','RN')
        X=lambda x:np.cos(k*x)+(np.sin(k*x)/k if mixed else 0)
        Xp=lambda x:-k*np.sin(k*x)+(np.cos(k*x) if mixed else 0)
        check('Robin_left_'+bc,X(0)-Xp(0) if mixed else Xp(0),0)
        check('Robin_right_'+bc, X(L) if bc=='RD' else X(L)+Xp(L) if bc in ('NR','RR') else Xp(L),0)
        N=L/2+np.sin(2*k*L)/(4*k)
        if mixed:N=L/2*(1+1/k**2)+np.sin(2*k*L)/(4*k)*(1-1/k**2)+np.sin(k*L)**2/k**2
        check('Robin_norm_'+bc,quad(lambda x:X(x)**2,0,L)[0],N)
        if L==1:
            A=np.sin(k)*(k*k-2*np.pi**2)/(k*(k*k-4*np.pi**2))
            B=(1-np.cos(k))*(k*k-2*np.pi**2)/(k*(k*k-4*np.pi**2))
            check('Robin_source_'+bc,quad(lambda x:np.cos(np.pi*x)**2*X(x),0,1)[0]/N,
                  (A+(B/k if mixed else 0))/N)
        else:
            def D(z):return (1-np.cos(np.pi*z))/z
            def E(z):return np.sin(np.pi*z)/z
            J=np.sin(np.pi*k)/k+(1-np.cos(np.pi*k))/k**2+D(.5+k)+D(.5-k)+(E(.5-k)-E(.5+k))/k
            check('Robin_example_coefficient',quad(lambda x:(1+2*np.sin(x/2))*X(x),0,L)[0],J)

# Explicit counterexample to monotone energy for the nonself-adjoint boundary.
def derivative_f(y):
    return 1-3*((1-y)**10-10*y*(1-y)**9)+10*y**9*(y-1)+y**10
integral=quad(lambda y:derivative_f(y)**2,0,1)[0]
assert derivative_f(0)==-2 and derivative_f(1)==2 and integral<2
check('Boundary_counterexample_pnorm',quad(lambda y:((1-y)**10-10*y*(1-y)**9)**2,0,1)[0],10/399)
errors['Boundary_counterexample_energy_growth']=0.
counts['Boundary_counterexample_energy_growth']=1

# Weighted Fourier coefficients: exponential times polynomial, from original quadrature.
for h in (-2.,-.5,0.,.5,2.):
    for n in range(1,9):
        k=n*np.pi;D=h*h+k*k;E=(-1)**n*np.exp(h)
        C=4*k*((1-h)-(1+h)*E)/D**2-16*k*h*h*(1-E)/D**3
        check('Drift_weighted_polynomial',2*quad(lambda x:np.exp(h*x)*x*(1-x)*np.sin(k*x),0,1)[0],C)
for n in range(1,9):
    k=n*np.pi;s=(-1)**n
    check('Drift_constant',2/np.pi*quad(lambda x:np.exp(-x/2)*np.sin(n*x),0,np.pi)[0],
          2*n*(1-s*np.exp(-np.pi/2))/(np.pi*(n*n+.25)))
    check('Drift_xexp',2*quad(lambda x:x*np.exp(x)*np.sin(k*x),0,1)[0],
          -2*k*s*np.e/(1+k*k)-4*k*(1-s*np.e)/(1+k*k)**2)
    b=np.sqrt(15)/2;D=(np.exp(-.5)+np.cos(b))/np.sin(b)
    check('Log_coordinate_coeff',2*quad(lambda z:(np.exp(z/2)+np.cos(b*z)-D*np.sin(b*z))*np.sin(k*z),0,1)[0],
          2*k*((1-s*np.exp(.5))/(k*k+.25)+(1+s*np.exp(-.5))/(k*k-15/4)))
for n in range(8):
    k=n+.5;s=(-1)**n
    check('Mixed_polynomial_initial',2/np.pi*quad(lambda x:(1+np.pi*np.pi*x/2)*np.sin(k*x),0,np.pi)[0],
          2/(np.pi*k)+np.pi*s/k**2)
    S=2*s/(np.pi*(1-k*k));Rmode=2*s/(np.pi*k*k);C=S+Rmode*(-1+1/np.pi);d=1-k*k
    check('Mixed_source_sine',2/np.pi*quad(lambda x:np.sin(x)*np.sin(k*x),0,np.pi)[0],S)
    for t in (.1,.7,2.):
        T=Rmode*(np.expm1(d*t)-d*t)/d**2+C*np.expm1(d*t)/d
        check('Mixed_linear_time_source',quad(lambda v:np.exp(d*(t-v))*(Rmode*v+C),0,t)[0],T,2e-8)

def g(z,K,t):return np.exp(-z*z/(4*K*t))/np.sqrt(4*np.pi*K*t)
for K in (.5,1.,2.):
    for t in (.05,.3,1.):
        for x in (0.,.4,1.7):
            first=.5*np.exp(K*t-x)*erfc((2*K*t-x)/np.sqrt(4*K*t))
            second=.5*np.exp(K*t+x)*erfc((2*K*t+x)/np.sqrt(4*K*t))
            for sign in (-1,1):
                check('Halfline_image_erfc',
                    quad(lambda y:(g(x-y,K,t)+sign*g(x+y,K,t))*np.exp(-y),0,np.inf)[0],
                    first+sign*second)
            check('Gaussian_square_completion',
                  quad(lambda y:g(x-y,K,t)*np.exp(-y*y+y),-np.inf,np.inf)[0],
                  np.exp(.25-(x-.5)**2/(1+4*K*t))/np.sqrt(1+4*K*t))

# Actual PDE residuals for explicit solutions, including log coordinates and Green potential.
def residual(fun,x,t,K,source=0.,drift=0.,reaction=0.):
    h=2e-4
    val=fun(x,t)
    ut=(fun(x,t+h)-fun(x,t-h))/(2*h)
    ux=(fun(x+h,t)-fun(x-h,t))/(2*h)
    uxx=(fun(x+h,t)-2*val+fun(x-h,t))/h**2
    return ut-K*uxx-drift*ux-reaction*val-source
for x,t in ((.2,.3),(.7,.8),(1.3,1.2)):
    fun=lambda x,t:np.exp(-2*t)*np.sin(x)
    check('PDE_coefficient_K2',residual(fun,x,t,2),0,3e-6)
    fun=lambda x,t:np.exp(.25-(x-.5)**2/(1+8*t))/np.sqrt(1+8*t)
    check('PDE_Gaussian',residual(fun,x,t,2),0,3e-6)
    fun=lambda x,t:(1-np.exp(-t))/2+(np.exp(-t)-np.exp(-8*np.pi**2*t))/(2*(8*np.pi**2-1))*np.cos(2*np.pi*x)
    check('PDE_Neumann_forced_example',residual(fun,x,t,2,np.exp(-t)*np.cos(np.pi*x)**2),0,3e-6)
    y=.6
    G=lambda x,t:np.exp(-(x-y)**2/(4*t)+t*(x+y)/2+t**3/12)/np.sqrt(4*np.pi*t)
    check('PDE_linear_potential_Green',residual(G,x,t,1,reaction=x),0,5e-6)
    check('Linear_potential_mass',quad(lambda z:np.exp(-(x-z)**2/(4*t)+t*(x+z)/2+t**3/12)/np.sqrt(4*np.pi*t),-np.inf,np.inf)[0],
          np.exp(x*t+t**3/3),2e-8)

# Fourier transport PDEs independently differentiate the printed transform.
for case in ('i','iii','iv'):
    def W(xi,t):
        if case=='i':return np.exp(-t-xi*xi*(1-np.exp(-2*t))/2-(np.exp(-t)*xi)**2/2)
        if case=='iii':return np.exp(-t-xi**4*(1-np.exp(-4*t))/4-(np.exp(-t)*xi)**2/2)
        return np.exp(t-xi*xi*(np.exp(2*t)-1)/2-(np.exp(t)*xi)**2/2)
    for xi,t in ((.3,.2),(1.1,.5),(-.8,.7)):
        h=1e-5
        wt=(W(xi,t+h)-W(xi,t-h))/(2*h);wx=(W(xi+h,t)-W(xi-h,t))/(2*h)
        err=wt+xi*wx+(1+(xi**4 if case=='iii' else xi*xi))*W(xi,t) if case!='iv' else wt-xi*wx-(1-xi*xi)*W(xi,t)
        check('Fourier_transport_'+case,err,0,3e-8)

# Laplace resolvent of the finite-interval third-order problem.
K=1.3;p=2.;L=1.
def Sp(x):return sum((p/K)**m*x**(3*m+2)/math.factorial(3*m+2) for m in range(18))
f=lambda x:x*(1-x)
C=quad(lambda y:Sp(L-y)*f(y),0,L)[0]/(K*Sp(L))
def U(x):return C*Sp(x)-quad(lambda y:Sp(x-y)*f(y),0,x)[0]/K
check('KdV_resolvent_left_value',U(0),0)
check('KdV_resolvent_right_value',U(L),0)
for x in (.2,.5,.8):
    h=2e-4
    third=(U(x+2*h)-2*U(x+h)+2*U(x-h)-U(x-2*h))/(2*h**3)
    check('KdV_resolvent_PDE',p*U(x)-f(x)-K*third,0,2e-5)

# Green positivity and semigroup, finite independently normalized modal sums.
L=1.;K=1.;n=np.arange(1,101,dtype=float)
def GD(x,y,t):return 2*np.sum(np.exp(-n*n*np.pi*np.pi*t)*np.sin(n*np.pi*x)*np.sin(n*np.pi*y))
for x,y,s,t in ((.2,.6,.1,.3),(.7,.4,.2,.15)):
    assert GD(x,y,t)>0
    check('Green_semigroup',quad(lambda z:GD(x,z,s)*GD(z,y,t),0,1)[0],GD(x,y,s+t))
for t in (.02,.1,.3):
    mass=quad(lambda y:GD(.5,y,t),0,1)[0]
    assert 0<mass<1
    mnext=quad(lambda y:GD(.5,y,t+.1),0,1)[0]
    assert mnext<mass

report={'chapter_items':50,'detailed_examples':15,'detailed_exercises':35,
        'numerical_checks':sum(counts.values()),'checks_by_topic':counts,'maximum_errors':errors,
        'nonmonotone_boundary_energy_derivative':float(2-integral)}
(R/'verification_chapter4.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
