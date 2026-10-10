import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
root=Path(__file__).resolve().parent
out=root/'graphs' if root.name=='_xu_ly' else root.parent/'Do_thi';out.mkdir(exist_ok=True)
clip=np.clip
sgn=np.sign
def indicator(x,a,b):
    x=np.asarray(x)
    return ((x>=a)&(x<=b)).astype(float)
def tri(x):return np.maximum(1-np.abs(x),0)
def extension(x,fun,L=None,left='odd',right='odd'):
    if L is None:
        return fun(np.abs(x))*(sgn(x) if left=='odd' else 1)
    k=np.floor(x/L).astype(int); r=x-k*L
    z=np.where(k%2==0,r,L-r)
    if left==right=='odd': factor=np.where(k%2==0,1,-1)
    elif left==right=='even':factor=np.ones_like(x)
    elif left=='even':factor=np.where((k%4==0)|(k%4==3),1,-1)
    else:factor=np.where((k%4==0)|(k%4==1),1,-1)
    return fun(z)*factor
# Exact primitives; constants cancel in D'Alembert.
cfg={
1:(2,lambda z:0*z,lambda z:.5*(clip(z,-1,0)**2-1),r'0',r'H(s)=\tfrac12(\operatorname{clip}(s,-1,0)^2-1)',[.5,1,2],(-5,5)),
2:(2,tri,lambda z:clip(z-1,0,1),r'(1-|s|)_+',r'H(s)=\operatorname{clip}(s-1,0,1)',[.25,.5,1],(-4,4)),
3:(3,lambda z:indicator(z,-1,1),lambda z:.5*(clip(z,1,2)**2-1),r'\chi_{[-1,1]}(s)',r'H(s)=\tfrac12(\operatorname{clip}(s,1,2)^2-1)',[1/6,1/3,2/3],(-4,5)),
4:(2,lambda z:indicator(z,-2,-1),lambda z:.5*clip(z,0,1)**2,r'\chi_{[-2,-1]}(s)',r'H(s)=\tfrac12\operatorname{clip}(s,0,1)^2',[.25,.5,1],(-5,4)),
5:(4,lambda z:10*indicator(z,-1,1),lambda z:clip(z+1,0,2),r'10\chi_{[-1,1]}(s)',r'H(s)=\operatorname{clip}(s+1,0,2)',[.25,.5,1],(-7,7)),
6:(3,lambda z:sgn(z)*np.abs(z)*(np.abs(z)-1)*indicator(np.abs(z),0,1),lambda z:6*np.abs(z),r'\operatorname{sgn}(s)|s|(|s|-1)\chi_{[0,1]}(|s|)',r'H(s)=6|s|',[1/6,1/3,2/3],(0,4)),
7:(1,lambda z:0*z,lambda z:sgn(z)*(.5*clip(np.abs(z),0,1)**2-clip(np.abs(z),0,1)),r'0',r'H(s)=\operatorname{sgn}(s)(m^2/2-m),\quad m=\min(|s|,1)',[.5,1,2],(0,4)),
8:(3,lambda z:np.abs(z)*(2-np.abs(z))*indicator(np.abs(z),0,2),lambda z:6*z,r'|s|(2-|s|)\chi_{[0,2]}(|s|)',r'H(s)=6s',[1/6,1/3,2/3],(0,5)),
9:(1,lambda z:0*z,lambda z:clip(np.abs(z),0,2)**2-2*clip(np.abs(z),0,2),r'0',r'H(s)=m^2-2m,\quad m=\min(|s|,2)',[.5,1,2],(0,5)),
10:(1,lambda z:0*z,lambda z:sgn(z)*(2*clip(np.abs(z),0,2)-.5*clip(np.abs(z),0,2)**2),r'0',r'H(s)=\operatorname{sgn}(s)(2m-m^2/2),\quad m=\min(|s|,2)',[1,2,3],(0,6)),
11:(1,lambda z:0*z,lambda z:sgn(z)*clip(np.abs(z)-1,0,1),r'0',r'H(s)=\operatorname{sgn}(s)\operatorname{clip}(|s|-1,0,1)',[.5,1,2],(0,5)),
12:(2,lambda z:0*z,lambda z:sgn(z)*clip(np.abs(z)-1,0,1),r'0',r'H(s)=\operatorname{sgn}(s)\operatorname{clip}(|s|-1,0,1)',[.25,.5,1],(0,5)),
13:(2,lambda z:0*z,lambda z:.5*(clip(np.abs(z),1,2)**2-1),r'0',r'H(s)=\tfrac12(\operatorname{clip}(|s|,1,2)^2-1)',[.125,.25,.5],(0,5)),
14:(3,lambda z:0*z,lambda z:sgn(z)*.5*(clip(np.abs(z),2,3)**2-4),r'0',r'H(s)=\tfrac12\operatorname{sgn}(s)(\operatorname{clip}(|s|,2,3)^2-4)',[.25,.5,1],(0,7)),
15:(1,lambda z:0*z,lambda z:1-np.abs(np.mod(z,2)-1),r'0',r'H(s)=1-|\operatorname{mod}(s,2)-1|',[.25,.5,1],(0,1)),
16:(2,lambda z:np.pi-np.abs(np.mod(z,2*np.pi)-np.pi),lambda z:0*z,r'\pi-|\operatorname{mod}(s,2\pi)-\pi|',r'H(s)=0',[np.pi/8,np.pi/4,np.pi/2],(0,np.pi)),
17:(2,lambda z:extension(z,lambda q:1-q,1,'even','odd'),lambda z:0*z,r'\bar f\text{ chẵn tại }0\text{, lẻ tại }1\text{, chu kỳ }4',r'H(s)=0',[.25,.5,1],(0,1)),
18:(2,lambda z:np.where(np.mod(z,1)==0,0,extension(z,lambda q:-np.ones_like(q),1)),lambda z:1-np.abs(np.mod(z,2)-1),r'\widetilde f=-1\text{ trên }(0,1),\text{ thác triển lẻ chu kỳ }2',r'H(s)=1-|\operatorname{mod}(s,2)-1|',[.25,.5,.75],(0,1)),
19:(2,lambda z:0*z,lambda z:primitive_triangle(z,np.pi),r'0',r'H(s)=k\pi^2/2+J(r),\ r=s-k\pi,\ k=\lfloor s/\pi\rfloor;\ J(r)=r^2/2\ (k\text{ chẵn}),\ \pi r-r^2/2\ (k\text{ lẻ})',[np.pi/4,np.pi/2,3*np.pi/4],(0,np.pi)),
20:(2,lambda z:0*z,lambda z:primitive_tent_odd(z,np.pi),r'0',r'H(s)=J(r),\ r=\operatorname{mod}(s,2\pi);\ J(r)=J(2\pi-r)\ (r>\pi),\ J(r)=r^2/2\ (r\le\pi/2),\ \pi r-r^2/2-\pi^2/4\ (\pi/2<r\le\pi)',[np.pi/8,np.pi/4,3*np.pi/8],(0,np.pi)),
21:(1,lambda z:0*z,lambda z:1-np.abs(np.mod(z,4)-2),r'0',r'H(s)=1-|\operatorname{mod}(s,4)-2|',[.5,1,2],(0,1)),
22:(1,lambda z:extension(z,lambda q:np.where(q<.25,4*q,np.where(q<.5,2-4*q,0)),1),lambda z:0*z,r'\widetilde f\text{ là thác triển lẻ chu kỳ }2\text{ của tam giác trong đề}',r'H(s)=0',[0,.25,.5,1],(0,1)),
}
def primitive_triangle(z,L):
    k=np.floor(z/L).astype(int);r=z-k*L
    return k*L*L/2+np.where(k%2==0,r*r/2,L*r-r*r/2)
def primitive_tent_odd(z,L):
    r=np.mod(z,2*L);r=np.where(r>L,2*L-r,r)
    return np.where(r<=L/2,r*r/2,L*r-r*r/2-L*L/4)
extras={
1:r'Tại $t=1$, $u_x=[g(x+2)-g(x-2)]/4$, nên không khả vi tại $x=-3,1$ (các bước nhảy tại $g(-1)$). Các điểm $x=-2,2$ chỉ mất trơn cấp 2 vì $g$ liên tục tại 0.',
2:r'Nghiệm liên tục tại mọi điểm. Các đường có thể mất trơn cấp 1 là $x\pm2t=-1,0,1$ do $f$ và $x\pm2t=1,2$ do $g$; trên mỗi giao điểm phải cộng hai hạng để kiểm tra triệt tiêu. Tại $t=1$, không có điểm mất liên tục.',
3:r'Nghiệm gián đoạn trên $x\pm3t=\pm1$ do phần $f$. Ngoài ra đạo hàm cấp 1 có thể nhảy trên $x\pm3t=1,2$ do vận tốc. Công thức tường minh trên quyết định giá trị tại các giao đường; tại $t=1$ các điểm gián đoạn là $-4,-2,2,4$.',
4:r'Gián đoạn trên $x\pm2t=-2,-1$; đạo hàm còn có thể nhảy trên $x\pm2t=0,1$. Ngoài hợp các đường này nghiệm trơn.',
5:r'Tại $x=10$, áp suất lớn nhất $5+1/4=5.25$ tại $t=11/4$. Giá trị này nhỏ hơn 6 nên tòa nhà không sập theo ngưỡng đề. Áp suất là 0 trước $9/4$, tăng từ 5 đến 5.25 trong đoạn $[9/4,11/4]$, sau đó bằng $1/4$.',
6:r'Tại $t=1/3$, trong miền $x>0$, nghiệm khả vi theo $x$ đúng ở $x\ne1,2$. Dữ liệu vận tốc 6 không tương thích Dirichlet tại góc $(0,0)$, nên không có nghiệm cổ điển toàn miền.',
7:r'Thác triển chẵn $g$ liên tục nên $u_x$ tồn tại khắp $x>0$, kể cả tại $t=1$. Các đạo hàm cấp 2 có thể mất trên các đường xuất phát từ 0,1. Giới hạn $\lim_{t\to\infty}u(1,t)=-1/2$.',
8:r'Tại $t=1/3$, nghiệm khả vi theo $x$ ở mọi $x>0$ trừ $1,3$. Khi $t\to\infty$ tại $x=1$, phần $f$ bằng 0 và $u=6t\to+\infty$.',
9:r'Tại $t=1$, không có đạo hàm theo $x$ ở $x=1,3$. Giới hạn $u(1,t)\to0$.',
10:r'Thác triển chẵn $g$ liên tục nên tại $t=1$, mọi $x>0$ đều khả vi theo $x$. $\lim_{t\to\infty}u(1/2,t)=2$.',
11:r'Đề yêu cầu thác triển chẵn nhưng biên là Dirichlet; phải dùng thác triển lẻ. Hàm $H$ ở trên là nguyên hàm của vận tốc lẻ. Nghiệm liên tục; các đường kỳ dị đạo hàm là $x\pm t=\pm1,\pm2$ trong nửa trục.',
12:r'Nghiệm liên tục, các đường kỳ dị cấp 1 là $x\pm2t=\pm1,\pm2$; chỉ giữ phần nằm trong $x>0,t>0$.',
13:r'Nghiệm liên tục; đường mất trơn cấp 1 là $x\pm2t=\pm1,\pm2$.',
14:r'Nghiệm liên tục; đường mất trơn cấp 1 là $x\pm3t=\pm2,\pm3$.',
15:r'Tách biến cho $u=\sum_{n\text{ lẻ}}4\sin(n\pi t)\sin(n\pi x)/(n^2\pi^2)$. Dữ liệu $g=1$ tại hai đầu không tương thích nên đây là nghiệm yếu; chu kỳ thời gian 2.',
16:r'Tách biến cho $u=\pi/2-(4/\pi)\sum_{n\text{ lẻ}}\cos(2nt)\cos(nx)/n^2$. Chu kỳ $\pi$. Dữ liệu $f=x$ không có đạo hàm biên 0, nên không có nghiệm cổ điển tại các góc.',
17:r'Mô hình $u_{tt}=4u_{xx}$, $u_x(0,t)=0,u(1,t)=0$, $f=1-x,g=0$. Với $k_n=(n+1/2)\pi$, nghiệm $u=\sum_{n\ge0}2\cos(2k_nt)\cos(k_nx)/k_n^2$. Chu kỳ 2; dữ liệu không tương thích đạo hàm tại đầu tự do.',
18:r'Chọn $v=1$, $w=u-1$ có biên 0, $w(x,0)=-1,w_t(x,0)=1$. Nghiệm $u=1+\sum_{n\text{ lẻ}}[-4\cos(2n\pi t)/(n\pi)+2\sin(2n\pi t)/(n^2\pi^2)]\sin(n\pi x)$. Góc dữ liệu $u(x,0)=0$ mâu thuẫn biên 1: chỉ có nghiệm yếu với mặt sóng.',
19:r'Chọn $v=x$. $w=u-x$ có biên Neumann 0, dữ liệu $w=0,w_t=x$. Nghiệm $u=x+\pi t/2-(2/\pi)\sum_{n\text{ lẻ}}\sin(2nt)\cos(nx)/n^3$. Có mode tuyến tính nên không tuần hoàn.',
20:r'Mô hình biên cố định $u_{tt}=4u_{xx}$ trên $(0,\pi)$, $f=0,u_t=g$. $u_x(0,t)=\widetilde g(2t)/2$. Do đó $\int_0^{\pi/2}|u_x(0,t)|^2dt=\frac18\int_0^\pi g^2$, suy bất đẳng thức với $T\ge\pi/2$. Với $g=\min(x,\pi-x)$, $u=\sum_{n\ge1}2\sin(n\pi/2)\sin(2nt)\sin(nx)/(\pi n^3)$.',
21:r'Mô hình $u_{tt}=u_{xx}$, $u(0,t)=0,u_x(1,t)=0$, dữ liệu $f=0,u_t=g$. Thác triển lẻ tại 0, chẵn tại 1, chu kỳ 4. Trong $0<t<1$, $u_x(0,t)=g(t)$, suy $\int_0^1g^2\le\int_0^T|u_x(0,t)|^2dt$ với $T\ge1$. Đồ thị bên dưới dùng $g=1$ theo ý (c).',
22:r'Tốc độ 1, biên cố định hai đầu, vận tốc ban đầu 0. Tại $0\le t\le1/4$, những điểm $x\in[3/4,1]$ và đầu $x=0$ vẫn cân bằng. Với $x\in(1/2,1)$, thời điểm sóng tới là $t_* =x-1/2$; nghiệm bắt đầu khác 0 ngay sau đó. Với tốc độ $c$, $t_*=(x-1/2)/c$, và vùng chưa bị tác động tới $t=1/4$ là $x\ge1/2+c/4$ nếu ngưỡng này nhỏ hơn 1; hai đầu cố định luôn cân bằng.',
}
def generate():
    for n,(a,f,H,ft,ht,times,span) in cfg.items():
        ident=f'BT_3_2_3_{n:02}'
        def sol(x,t):return (f(x-a*t)+f(x+a*t))/2+(H(x+a*t)-H(x-a*t))/(2*a)+(1 if n==18 else 0)+(x if n==19 else 0)
        xs=np.linspace(*span,1501)
        fig,axs=plt.subplots(2,len(times),figsize=(4*len(times),6),squeeze=False)
        axs[0,0].plot(xs,f(xs)/2-H(xs)/(2*a),label='A(s), song phai')
        axs[0,0].plot(xs,f(xs)/2+H(xs)/(2*a),label='B(s), song trai')
        axs[0,0].legend(fontsize=8);axs[0,0].set_title('Hai song chay ban dau')
        for ax,t in zip(axs[1],times):
            ax.plot(xs,sol(xs,t),lw=1.6);ax.axhline(0,color='gray',lw=.5);ax.set_title(f't = {t:.4g}');ax.set_xlabel('x');ax.set_ylabel('u');ax.grid(alpha=.2)
        for ax in axs[0,1:]:ax.axis('off')
        if len(times)>1:
            ts=np.linspace(0,max(times),180);xx,tt=np.meshgrid(xs[::4],ts)
            axs[0,1].axis('on');axs[0,1].pcolormesh(xx,tt,sol(xx,tt),shading='auto',cmap='coolwarm');axs[0,1].set_title('Mien truyen song');axs[0,1].set_xlabel('x');axs[0,1].set_ylabel('t')
        fig.suptitle(f'Muc 3.2.3 - Bai {n}');fig.tight_layout();fig.savefig(out/(ident+'.png'),dpi=150);plt.close(fig)
    print('22 wave figures generated; no solution sources overwritten')
if __name__=='__main__':generate()
