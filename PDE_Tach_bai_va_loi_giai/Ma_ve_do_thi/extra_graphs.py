from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
r=Path(__file__).resolve().parent
g=r/'graphs';g.mkdir(exist_ok=True)
def angular(v):return 2*np.pi-2*np.arccos(np.clip(v,-1,1))
def cone_u(t,rad,R=1,alpha=1,c=1):
    if t<=0:return 0.
    rho=c*t
    if rad==0:return t*(1-alpha/np.sqrt(1+alpha*alpha))/2 if rho<R else 0.
    def fun(mu):
        den=2*rad*rho*np.sqrt(max(1-mu*mu,1e-30))
        B=(R*R-rad*rad-rho*rho)/den
        C=(rho*rho*mu*mu/alpha**2-rad*rad-rho*rho*(1-mu*mu))/den
        return angular(min(B,C))
    return t*quad(fun,0,1,epsabs=1e-7,limit=150)[0]/(4*np.pi)
def torus_u(t,rad,R=2,a=.5,c=1):
    if t<=0:return 0.
    rho=c*t
    if rad==0:
        h=(rho*rho+R*R-a*a)/(2*R*rho)
        return t*np.sqrt(max(0,1-h*h))
    lim=min(1,a/rho)
    def fun(mu):
        h=np.sqrt(max(0,a*a-rho*rho*mu*mu))
        den=2*rad*rho*np.sqrt(max(1-mu*mu,1e-30))
        q=rad*rad+rho*rho*(1-mu*mu)
        return angular(((R+h)**2-q)/den)-angular(((R-h)**2-q)/den)
    return t*quad(fun,-lim,lim,epsabs=1e-7,limit=150)[0]/(4*np.pi)
def maximum(fun,upper,steps=240):
    # Numerical search, refine every sampled local maximum, increase steps to verify convergence.
    ts=np.linspace(0,upper,steps+1);us=np.array([fun(t) for t in ts]);candidates=[(us.max(),ts[us.argmax()])]
    for i in range(1,len(ts)-1):
        if us[i]>=us[i-1] and us[i]>=us[i+1] and us[i]>0:
            z=minimize_scalar(lambda t:-fun(t),bounds=(ts[i-1],ts[i+1]),method='bounded',options={'xatol':1e-8})
            candidates.append((-z.fun,z.x))
    return max(candidates)
def psi(x,y,case):
    if case=='a':return 2*(y>2+2*np.abs(x)).astype(float)-(y<np.minimum(2-2*np.abs(x),0)).astype(float)+((y>np.maximum(2-2*np.abs(x),0))&(y<2+2*np.abs(x))).astype(float)
    return ((np.abs(x)>1)&(np.abs(y)<1)).astype(float)-((np.abs(x)<1)&(np.abs(y)>1)).astype(float)
def wave2(x,y,t,case,nv=40,ntheta=160):
    # r=ct*sqrt(1-v^2) removes the square-root singularity in Poisson's kernel.
    nodes,weights=np.polynomial.legendre.leggauss(nv);nodes=(nodes+1)/2;weights=weights/2
    theta=2*np.pi*(np.arange(ntheta)+.5)/ntheta
    total=np.zeros_like(x)
    for v,w in zip(nodes,weights):
        rho=2*t*np.sqrt(1-v*v)
        for ang in theta:total+=w*psi(x+rho*np.cos(ang),y+rho*np.sin(ang),case)/ntheta
    return t*total
def generate():
    x,y=np.meshgrid(np.linspace(-7,7,85),np.linspace(-4,9,85))
    fig,axs=plt.subplots(2,3,figsize=(13,7),layout='constrained')
    for row,case in enumerate(['a','b']):
        for ax,t in zip(axs[row],[.5,1.5,3]):
            u=wave2(x,y,t,case)
            cs=ax.contourf(x,y,u,25,cmap='coolwarm');fig.colorbar(cs,ax=ax)
            ax.set(title=f'Case ({case}), t={t}',xlabel='x',ylabel='y')
    fig.suptitle('BT 3.6.3.7: numerical Poisson integral (c=2)')
    fig.savefig(g/'BT_3_6_3_07.png',dpi=155);plt.close(fig)
    # Explicit chapter 2 solutions, with two valid solutions for nonunique data.
    x,y=np.meshgrid(np.linspace(-1,1,75),np.linspace(-1,1,75))
    funcs={
    3:lambda x,y:(lambda xi,eta,P:P(x,y)-xi/8-P(-3*xi/8,5*xi/8)+np.exp(eta/8)-P(eta/8,eta/8))(y-x,5*x+3*y,lambda x,y:x**3*(1+y)/18+x**4/108),
    5:lambda x,y:(x+y)*np.exp(-(5*x-3*y)/8),
    6:lambda x,y:np.exp(x)-np.cos(5*x+y),
    7:lambda x,y:np.exp(x)+x*(y+3*x)**2/9+np.sin(y+3*x),
    8:lambda x,y:np.exp(x)/4+x*(x+2*y)/4+(x+2*y)/2,
    9:lambda x,y:np.exp(x)+np.exp(2*x/5),
    10:lambda x,y:np.cos(x-2*y)+2*(1-np.exp(y/2))*np.sin(x-2*y),
    14:lambda x,y:x+2*y+np.exp(-x),
    15:lambda x,y:x,
    16:lambda x,y:x*(y-np.cos(x)),
    17:lambda x,y:(x+y-np.arctan(y)-np.log(2))*np.log(1+y*y)+np.log(2)**2,
    18:lambda x,y:np.cos(y-x**3/3)}
    for n,fun in funcs.items():
        fig=plt.figure(figsize=(8,5));ax=fig.add_subplot(projection='3d')
        ax.plot_surface(x,y,fun(x,y),cmap='viridis',alpha=.9)
        ax.set(xlabel='x',ylabel='y',zlabel='u',title=f'BT 2.3.{n}: an explicit solution')
        fig.savefig(g/f'BT_2_3_{n:02}.png',dpi=140);plt.close(fig)
    fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
    ts=np.linspace(0,4,180)
    axs[0].plot(ts,[cone_u(t,.6) for t in ts]);axs[0].set(title='Cone: R=1, alpha=1, r=0.6',xlabel='t',ylabel='u')
    axs[1].plot(ts,[torus_u(t,.6) for t in ts]);axs[1].set(title='Torus: R=2, a=0.5, r=0.6',xlabel='t',ylabel='u')
    fig.savefig(g/'cone_torus.png',dpi=150);plt.close(fig)
if __name__=='__main__':generate()
