"""Minh họa nghiệm và đặc trưng Chương 2 trên miền hợp lệ."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r=Path(__file__).resolve().parent
out=r/'graphs' if r.name=='_xu_ly' else r.parent/'Do_thi'
out.mkdir(exist_ok=True)
P=lambda x,y:x**3*(1+y)/18+x**4/108
def u3(x,y):
    s=y-x;t=5*x+3*y
    return P(x,y)-s/8-P(-3*s/8,5*s/8)+np.exp(t/8)-P(t/8,t/8)
def F4(s):
    return sum(np.sin((-1/3)**j*s/2) for j in range(1,61))+3*s/4-9*s*s/320
def u4c(x,y):
    s=x-5*y;t=x+3*y
    return x*x/30+F4(s)+t-t*t/30-F4(t)
F4e=lambda s:s/4+(np.cos(s)-1)/8-(np.exp(s)-1)/64
def u4e(x,y):
    s=x-5*y;t=x+3*y
    return x*np.exp(t)/24+F4e(s)+t-t*np.exp(t)/24-F4e(t)
u5=lambda x,y:(x+y)*np.exp(-(5*x-3*y)/8)
u8=lambda x,y:np.exp(x)/4+x*(x+2*y)/4+(x+2*y)/2
u9=lambda x,y:np.exp(x)+np.exp(2*x/5)
cases={
3:[('Nghiem (c)',u3)],4:[('Nghiem (c)',u4c),('Nghiem (e)',u4e)],
5:[('Nghiem 1, C=3',u5),('Nghiem 2, C=3',lambda x,y:u5(x,y)+(5*x-3*y)**2)],
6:[('Nghiem duy nhat',lambda x,y:np.exp(x)-np.cos(5*x+y))],
7:[('Nghiem duy nhat',lambda x,y:np.exp(x)+x*(y+3*x)**2/9+np.sin(y+3*x))],
8:[('Nghiem 1',u8),('Nghiem 2',lambda x,y:u8(x,y)+(x+2*y)**2)],
9:[('Nghiem 1, C=1',u9),('Nghiem 2, C=1',lambda x,y:u9(x,y)+x+5*y)],
10:[('Nghiem duy nhat',lambda x,y:np.cos(x-2*y)+2*(1-np.exp(y/2))*np.sin(x-2*y))],
11:[('Nghiem trong mien duy nhat',lambda x,y:x+1-np.sqrt(x*x+2*y*y/3))],
14:[('Nghiem duy nhat',lambda x,y:x+2*y+np.exp(-x))],
15:[('Nghiem 1, b=0',lambda x,y:x),('Nghiem 2, b=0',lambda x,y:x+y*np.sin(x))],
17:[('Nghiem, y>0',lambda x,y:(x+y-np.arctan(y)-np.log(2))*np.log(1+y*y)+np.log(2)**2)]}
slopes={3:[1,-5/3],4:[1/5,-1/3],5:[-1,5/3],6:[-5],7:[-3],8:[-.5],9:[-.2],10:[.5]}
def generate():
    for n,functions in cases.items():
        if n==11:
            th,rad=np.meshgrid(np.linspace(.03,np.pi-.03,70),np.linspace(np.sqrt(3),np.sqrt(12),60))
            x=rad*np.cos(th)/np.sqrt(3);y=rad*np.sin(th)/np.sqrt(2)
        else:
            xs=np.linspace(.08,1.45,65) if n==15 else np.linspace(-1,1,65)
            ys=np.linspace(.05,1.5,65) if n in (15,17) else np.linspace(-1,1,65)
            x,y=np.meshgrid(xs,ys)
        count=len(functions)+int(n!=17)
        fig=plt.figure(figsize=(6*count,4.7),layout='constrained')
        for j,(title,fun) in enumerate(functions,1):
            ax=fig.add_subplot(1,count,j,projection='3d');ax.plot_surface(x,y,fun(x,y),cmap='viridis',alpha=.92)
            ax.set(xlabel='x',ylabel='y',zlabel='u',title=title)
        if n!=17:
            ax=fig.add_subplot(1,count,count);t=np.linspace(-3,3,400)
            if n in slopes:
                for k,m in enumerate(slopes[n]):
                    for offset in np.linspace(-2,2,7):ax.plot(t,m*t+offset,color=['tab:blue','tab:orange'][k],lw=.8)
                if n==4:
                    x0=.4;y0=.35;ax.plot([x0-5*y0,x0,x0+3*y0,x0-5*y0],[0,y0,0,0],color='red',lw=2,label='Tam giac phu thuoc')
                    ax.legend()
                ax.set(xlim=(-2,2),ylim=(-2,2))
            elif n==11:
                angles=np.linspace(0,np.pi,300)
                for rad0 in np.linspace(np.sqrt(3),np.sqrt(12),6):ax.plot(rad0*np.cos(angles)/np.sqrt(3),rad0*np.sin(angles)/np.sqrt(2),'tab:blue',lw=.8)
                for angle in np.linspace(.2,np.pi-.2,9):
                    rr=np.linspace(np.sqrt(3),np.sqrt(12),100);ax.plot(rr*np.cos(angle)/np.sqrt(3),rr*np.sin(angle)/np.sqrt(2),'tab:orange',lw=.8)
                ax.set(xlim=(-2.1,2.1),ylim=(0,2.6))
            elif n==14:
                for s in np.linspace(-1,4,9):ax.plot(t,s-np.exp(-t),'tab:blue',lw=.8)
                ax.set(xlim=(-2,2),ylim=(-2,2))
            elif n==15:
                tt=np.linspace(.06,1.5,300)
                for s in np.linspace(.08,1,9):ax.plot(tt,s/np.sin(tt),'tab:blue',lw=.8)
                ax.set(xlim=(0,np.pi/2),ylim=(0,3))
            ax.set(xlabel='x',ylabel='y',title='Cac duong dac trung');ax.grid(alpha=.2)
        fig.suptitle(f'BT 2.3.{n}');fig.savefig(out/f'BT_2_3_{n:02}.png',dpi=140);plt.close(fig)
    print('Chapter 2 graphs:',len(cases))

if __name__=='__main__':generate()
