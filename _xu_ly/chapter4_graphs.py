"""Vẽ minh họa Chương 4; chạy độc lập chỉ tạo hình, không ghi đè lời giải."""
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.special import erfc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
DEST=ROOT.parent/'Do_thi' if ROOT.name=='Ma_ve_do_thi' else ROOT/'graphs'

def robin_roots(L,count):
    return np.array([brentq(lambda k:k*np.sin(k*L)-np.cos(k*L),
        j*np.pi/L+1e-9,(j+.5)*np.pi/L-1e-9) for j in range(count)])

def dirichlet_polynomial(x,t):
    n=np.arange(1,181,2,dtype=float)
    return np.sum((8/(n**3*np.pi**3)*np.exp(-n*n*np.pi*np.pi*t))[:,None]
                  *np.sin(n[:,None]*np.pi*x),axis=0)

def panels(ident,cases):
    fig,axs=plt.subplots(1,len(cases),figsize=(6.1*len(cases),3.8),squeeze=False)
    for ax,(x,fun,initial,times,title) in zip(axs[0],cases):
        ax.plot(x,initial(x),color='black',lw=1.5,label='t = 0 (data)')
        for t in times: ax.plot(x,fun(x,t),label=f't = {t:g}')
        ax.set(xlabel='x',ylabel='u(x,t)',title=title)
        ax.grid(alpha=.25);ax.legend(fontsize=8)
    fig.tight_layout();DEST.mkdir(exist_ok=True,parents=True)
    fig.savefig(DEST/(ident+'.png'),dpi=160);plt.close(fig)

def main():
    x=np.linspace(0,1,501);y=np.linspace(0,np.pi,601)
    n=np.arange(1,301,dtype=float)
    c=2*(-1.)**n*n*np.sin(np.pi**2)/(np.pi*(np.pi**2-n*n))
    panels('VD_4_1_2_01',[
        (x,lambda z,t:.75*np.exp(-np.pi**2*t)*np.sin(np.pi*z)-.25*np.exp(-9*np.pi**2*t)*np.sin(3*np.pi*z),
         lambda z:np.sin(np.pi*z)**3,[.03,.1,.3],'Dirichlet: sin^3(pi x)'),
        (y,lambda z,t:np.sum((c*np.exp(-2*n*n*t))[:,None]*np.sin(n[:,None]*z),axis=0),
         lambda z:np.sin(np.pi*z),[.01,.1,.5],'Dirichlet: sin(pi x), L = pi')])
    m=np.arange(1,151,dtype=float)
    panels('VD_4_1_2_02',[
        (x,lambda z,t:.5+.5*np.exp(-4*np.pi**2*t)*np.cos(2*np.pi*z),
         lambda z:np.cos(np.pi*z)**2,[.01,.05,.15],'Neumann: cos^2(pi x)'),
        (y,lambda z,t:2/np.pi+np.sum((4/(np.pi*(1-4*m*m))*np.exp(-8*m*m*t))[:,None]*np.cos(2*m[:,None]*z),axis=0),
         np.sin,[.03,.2,1.],'Neumann: sin x')])
    k=robin_roots(np.pi,100)
    def X(z):return np.cos(k[:,None]*z)+np.sin(k[:,None]*z)/k[:,None]
    norm=np.pi/2*(1+1/k**2)+np.sin(2*k*np.pi)/(4*k)*(1-1/k**2)+np.sin(k*np.pi)**2/k**2
    coeff=np.array([quad(lambda z:(1+2*np.sin(z/2))*(np.cos(a*z)+np.sin(a*z)/a),0,np.pi)[0]
                    for a in k])/norm
    panels('VD_4_1_2_03',[(y,lambda z,t:np.sum((coeff*np.exp(-2*k*k*t))[:,None]*X(z),axis=0),
        lambda z:1+2*np.sin(z/2),[.1,1.,4.],'Robin left, Neumann right: K = 2')])
    panels('BT_4_1_3_01',[
        (x,dirichlet_polynomial,lambda z:z*(1-z),[.02,.1,.3],'Dirichlet: x(1-x)'),
        (y,lambda z,t:np.exp(-2*t)*np.sin(z),np.sin,[.1,.5,1.],'Dirichlet: K = 2 (a read as K)')])
    odd=np.arange(1,181,2,dtype=float)
    def constant_source(z,t):
        return np.sum((4/(np.pi*odd**3)*(1-np.exp(-odd*odd*t)))[:,None]*np.sin(odd[:,None]*z),axis=0)
    panels('VD_4_4_2_01',[
        (y,constant_source,lambda z:0*z,[.1,.5,2.],'Dirichlet: source 1; limit x(pi-x)/2'),
        (x,lambda z,t:(1-np.exp(-t))/2+(np.exp(-t)-np.exp(-8*np.pi**2*t))/(2*(8*np.pi**2-1))*np.cos(2*np.pi*z),
         lambda z:0*z,[.1,.5,2.],'Neumann: source exp(-t)cos^2(pi x)')])
    panels('BT_4_2_3_08',[(x,lambda z,t:(t+1)*z*(1-z),lambda z:z*(1-z),
        [.5,1.,2.],'Positive source: temperature exceeds initial maximum')])
    z=np.linspace(-4,4,601)
    panels('VD_4_6_2_01',[
        (z,lambda z,t:.5+.5*np.exp(-36*t)*np.cos(6*z),lambda z:np.cos(3*z)**2,
         [.02,.1,.3],'Whole line: cos^2(3x)'),
        (z,lambda z,t:np.exp(-z*z/(1+8*t))/np.sqrt(1+8*t),lambda z:np.exp(-z*z),
         [.1,.5,1.],'Whole line: Gaussian, K = 2')])
    z=np.linspace(0,5,601)
    panels('BT_4_6_3_02',[(z,lambda z,t:.5*np.exp(2*t-z)*erfc((4*t-z)/np.sqrt(8*t))
        +.5*np.exp(2*t+z)*erfc((4*t+z)/np.sqrt(8*t)),lambda z:np.exp(-z),
        [.02,.2,1.],'Half line: Neumann image, K = 2')])
    print('Chapter 4: 8 figures generated.')

if __name__=='__main__':main()
