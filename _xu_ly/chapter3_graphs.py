"""Đồ thị từ nghiệm chính xác của Chương 3; không ghi đè nguồn lời giải."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
r=Path(__file__).resolve().parent
out=r/'graphs' if r.name=='_xu_ly' else r.parent/'Do_thi'
out.mkdir(exist_ok=True)

def triangle_H(s):
    return np.where(s<=-1,0,np.where(s<=0,(s+1)**2/2,np.where(s<1,1-(1-s)**2/2,1)))

def full_cases():
    return [
        lambda x,t:np.cos(x)*np.cos(3*t)+np.sin(2*x)*np.sin(6*t)/6,
        lambda x,t:np.sin(3*x)*np.cos(15*t)+x*t,
        lambda x,t:x*x+4*t*t+np.cos(x)*np.sin(2*t)/2,
        lambda x,t:(np.exp(-abs(x-6*t))+np.exp(-abs(x+6*t)))/2+t/2+np.cos(2*x)*np.sin(12*t)/24,
        lambda x,t:np.sin(x)*np.cos(t)-.5-.5*np.cos(2*x)*np.cos(2*t)+.75*np.sin(x)*np.sin(t)-np.sin(3*x)*np.sin(3*t)/12,
        lambda x,t:1+(triangle_H(x+7*t)-triangle_H(x-7*t))/14,
    ]

def half_cases():
    def H(s):return np.clip(abs(s)-1,0,1)-np.clip(abs(s)-3,0,1)
    return [
        lambda x,t:np.sin(x)*np.cos(2*t)+np.where(x>=2*t,np.cos(2*x)*np.sin(4*t)/4,np.sin(2*x)*np.cos(4*t)/4),
        lambda x,t:np.maximum(t-x/3,0)/(1+np.maximum(t-x/3,0)),
        lambda x,t:((x+t)*abs(x+t)+(x-t)*abs(x-t))/2+np.sin(x)*np.sin(t),
        lambda x,t:np.sin(x)*np.sin(5*t)/5-np.sin(3*x)*np.sin(15*t)/45,
        lambda x,t:np.where(x>=2*t,(np.cos(x)-np.sin(x))*np.cos(2*t),np.cos(x)*(np.cos(2*t)-np.sin(2*t))),
        lambda x,t:(H(x+t)-H(x-t))/2,
    ]

def forced_cases():
    def f(s):return np.maximum(s,0)-np.maximum(s-1,0)-np.maximum(s-2,0)+np.maximum(s-3,0)
    return [
        lambda x,t:np.exp(-x)*np.cosh(2*t)+np.sin(2*x)*np.sin(4*t)/4+x*(1-np.cos(t)),
        lambda x,t:(np.arctan(x+3*t)-np.arctan(x-3*t))/6+np.exp(x)*(np.cosh(3*t)-1)/9+t-np.sin(t),
        lambda x,t:x*x+16*t*t+np.sin(x)*np.sin(4*t)/4+x*t*t/2+t**3/6,
        lambda x,t:np.exp(x)*np.sinh(7*t)/7+x*t**3/6,
        lambda x,t:x+np.cos(x)*np.sin(t)+(np.sin(x)*t*np.sin(t)+np.cos(x)*(np.sin(t)-t*np.cos(t)))/2,
        lambda x,t:(f(x-2*t)+f(x+2*t))/2+(triangle_H(x+2*t)-triangle_H(x-2*t))/4-np.exp(x)*(np.cosh(2*t)-1)/4,
    ]

def panels(ident,functions,span,times,speeds):
    x=np.linspace(*span,1201)
    fig,axes=plt.subplots(2,3,figsize=(13,7))
    for n,(ax,fun) in enumerate(zip(axes.flat,functions),1):
        for t in times:ax.plot(x,fun(x,t),label=f't={t:g}')
        ax.set_title(f'({n})');ax.set_xlabel('x');ax.set_ylabel('u(x,t)');ax.grid(alpha=.2);ax.legend(fontsize=7)
    fig.suptitle(ident+' - Lat cat tu nghiem chinh xac');fig.tight_layout();fig.savefig(out/(ident+'.png'),dpi=180);plt.close(fig)
    fig,axes=plt.subplots(2,3,figsize=(13,7))
    xx,tt=np.meshgrid(x[::3],np.linspace(0,max(times),180))
    for n,(ax,fun,a) in enumerate(zip(axes.flat,functions,speeds),1):
        ax.pcolormesh(xx,tt,fun(xx,tt),shading='auto',cmap='coolwarm')
        for b in (-1,0,1):
            ts=np.linspace(0,max(times),150)
            ax.plot(b+a*ts,ts,'k--',lw=.5);ax.plot(b-a*ts,ts,'k--',lw=.5)
        if span[0]==0:
            for start in (.25,.75):
                ts=np.linspace(start,max(times),100)
                ax.plot(a*(ts-start),ts,'w:',lw=.9)
        ax.set_xlim(span);ax.set_title(f'({n}), a={a}');ax.set_xlabel('x');ax.set_ylabel('t')
    fig.suptitle('Hai ho dac trung x +/- a*t = hang; net dut la cac duong mau')
    fig.tight_layout();fig.savefig(out/(ident+'_characteristics.png'),dpi=180);plt.close(fig)

def beam_roots():
    # Brackets exclude zero and avoid poles of tan.
    return brentq(lambda b:np.cosh(b)*np.sin(b)-np.sinh(b)*np.cos(b),3.8,4.1),brentq(lambda b:np.sinh(b)*np.cos(b)+np.cosh(b)*np.sin(b),2.2,2.5)

def beam_mode(x,b,kind):
    if kind in (0,1):
        sigma=1/np.tanh(b) if kind==0 else np.tanh(b)
        return np.cosh(b*x)-np.cos(b*x)-sigma*(np.sinh(b*x)-np.sin(b*x))
    if kind==2:return np.sin(b*x)
    if kind==3:return np.sin(b*x)
    return np.cos(b*x)

def generate():
    panels('BT_3_1_3_02',full_cases(),(-5,5),[0,.25,.6,1],[3,5,2,6,1,7])
    panels('BT_3_1_3_05',forced_cases(),(-4,4),[0,.15,.35,.65],[2,3,4,7,1,2])
    panels('BT_3_1_3_08',half_cases(),(0,6),[0,.25,.75,1.5],[2,3,1,5,2,1])
    fig,ax=plt.subplots(figsize=(9,4));ts=np.linspace(0,4,1500)
    p=np.where(ts<14/5,0,np.where(ts<=16/5,5+(5*ts-14)/10,.2))
    ax.plot(ts,p,label='u(15,t)');ax.axhline(8,color='red',ls='--',label='Nguong 8');ax.legend();ax.set_xlabel('t');ax.set_ylabel('Ap suat');ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(out/'BT_3_1_3_03.png',dpi=180);plt.close(fig)
    x=np.linspace(0,1,600);fig,axes=plt.subplots(1,3,figsize=(12,3.5))
    for ax,kind in zip(axes,range(3)):
        k=np.pi/2 if kind<2 else np.pi
        X=np.sin(k*x) if kind==0 else np.cos(k*x)
        w=np.sqrt(k*k-.25)
        for t in (0,.5,1,2):ax.plot(x,X*np.exp(-t/2)*(np.cos(w*t)+np.sin(w*t)/(2*w)),label=f't={t:g}')
        ax.set_title(['(a) D-N','(b) N-D','(c) N-N'][kind]);ax.legend(fontsize=7);ax.grid(alpha=.2);ax.set_xlabel('x')
    fig.suptitle('Song co can: a=L=1, f la mode dau duong, g=0');fig.tight_layout();fig.savefig(out/'BT_3_5_3_01.png',dpi=180);plt.close(fig)
    ba,bb=beam_roots();bs=[ba,bb,np.pi,np.pi/2,np.pi]
    fig,axes=plt.subplots(2,3,figsize=(12,7))
    for kind,(ax,b) in enumerate(zip(axes.flat,bs)):
        X=beam_mode(x,b,kind)
        for t in (0,.04,.08,.16):ax.plot(x,X*np.cos(b*b*t),label=f't={t:g}')
        ax.set_title(f'({chr(97+kind)}) beta={b:.6f}');ax.legend(fontsize=7);ax.grid(alpha=.2);ax.set_xlabel('x')
    axes.flat[-1].axis('off');fig.suptitle('Dam: a=L=1, f=mode dau duong, g=0; tan beta = +/- tanh beta o (a),(b)')
    fig.tight_layout();fig.savefig(out/'BT_3_5_3_02.png',dpi=180);plt.close(fig)
    print('9 exact chapter 3 figures generated')

if __name__=='__main__':generate()
