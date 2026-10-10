"""Apply reviewed intermediate calculations; keep an item-by-item audit."""
from pathlib import Path
import re,json

R=Path(__file__).resolve().parent
PAT=re.compile(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',re.M|re.S)
def blocks(path):
    pairs=[(m[1],m[2].strip()) for m in PAT.finditer(path.read_text(encoding='utf-8'))]
    assert len(pairs)==len(dict(pairs)),path
    return dict(pairs)
def write(path,b):
    path.write_text('\n\n'.join('%ID '+i+'\n'+t for i,t in b.items())+'\n',encoding='utf-8')

original={i:t for p in (R/'backup_truoc_bo_sung_buoc_trung_gian_123').glob('loi_giai*.tex') for i,t in blocks(p).items()}
inventory=json.loads((R/'inventory.json').read_text(encoding='utf-8'))
add={}
for n in (1,2,3):
    add.update(blocks(R/f'bo_sung_buoc_chuong{n}.tex'))
def extra(i,t):
    add[i]=add.get(i,'')+'\n\n'+t.strip()

# Explicit expansion for each constant linear transformation. These rows are
# problem-specific coefficients, rather than a restatement of a general method.
linear={
'BT_2_3_03':(-1,1,5,3,3,-1,-5),
'BT_2_3_04':(1,-5,1,3,15,-1,-1),
'BT_2_3_05':(1,1,5,-3,3,1,-5),
'BT_2_3_06':(5,1,1,0,1,-5,25),
'BT_2_3_08':(1,2,1,0,4,-2,1),
'BT_2_3_09':(1,5,1,0,25,-5,1),
'BT_2_3_10':(1,-2,1,0,8,4,2),
}
for i,(a,b,c,d,A,B,C) in linear.items():
    name=('s','z') if i in ('BT_2_3_06','BT_2_3_08','BT_2_3_09','BT_2_3_10') else (r'\xi',r'\eta')
    s,z=name
    def terms(items):
        result=''
        for val,label in items:
            if val==0:continue
            sign='-' if val<0 else '+' if result else ''
            result+=sign+(str(abs(val)) if abs(val)!=1 else '')+label
        return result or '0'
    xx=terms([(a*a,'v_{'+s+s+'}'),(2*a*c,'v_{'+s+z+'}'),(c*c,'v_{'+z+z+'}')])
    xy=terms([(a*b,'v_{'+s+s+'}'),(a*d+b*c,'v_{'+s+z+'}'),(c*d,'v_{'+z+z+'}')])
    yy=terms([(b*b,'v_{'+s+s+'}'),(2*b*d,'v_{'+s+z+'}'),(d*d,'v_{'+z+z+'}')])
    coeff=[(A*a*a,2*B*a*b,C*b*b),(2*A*a*c,2*B*(a*d+b*c),2*C*b*d),(A*c*c,2*B*c*d,C*d*d)]
    sums=[terms([(v,'') for v in row])+'='+str(sum(row)) for row in coeff]
    # terms treats 1 specially for labels; numbers need their own formatting.
    sums=[''.join(('+' if j and v>=0 else '')+str(v) for j,v in enumerate(row))+'='+str(sum(row)) for row in coeff]
    extra(i,r'\textbf{Chi tiết thế ba đạo hàm cấp hai.} Với tọa độ đã chọn,'+'\n'+
          r'\[u_{xx}='+xx+r',\quad u_{xy}='+xy+r',\quad u_{yy}='+yy+r'.\]'+'\n'+
          r'Nhân lần lượt với $'+str(A)+'$,$'+str(2*B)+'$,$'+str(C)+'$, hệ số theo thứ tự $v_{'+s+s+'},v_{'+s+z+'},v_{'+z+z+'}$ là\n'+
          r'\['+r',\qquad '.join(sums)+r'.\]')

const_integral=r'''\textbf{Chi tiết tích phân của dữ liệu hằng.} Với $k_n=n\pi/L$,
\[\int_0^L\sin k_nx\,dx=\left[-\frac{\cos k_nx}{k_n}\right]_0^L=\frac{1-(-1)^n}{k_n}.\]
Nhân $2/L$ cho hệ số của hằng $1$ là $2(1-(-1)^n)/(n\pi)$; hằng $-1$ đổi dấu. Khi chiếu vận tốc, còn chia $\omega_n$ trong hệ số $\sin\omega_nt$; khi chiếu li độ, hệ số $\cos\omega_nt$ giữ nguyên.'''
for i in ['BT_3_2_3_15','BT_3_2_3_18','VD_3_5_2_01']:
    extra(i,const_integral)
xcos=r'''\textbf{Chi tiết hệ số cos của dữ liệu $x$.} Trên $(0,\pi)$, trung bình là $A_0=\pi^{-1}\int_0^\pi x\,dx=\pi/2$. Với $n\ge1$,
\[\int_0^\pi x\cos nx\,dx=\left[\frac{x\sin nx}{n}\right]_0^\pi-\frac1n\int_0^\pi\sin nx\,dx
=\frac{(-1)^n-1}{n^2}.\]
Nhân $2/\pi$ cho $2((-1)^n-1)/(\pi n^2)$. Nếu dữ liệu này là li độ thì giữ hệ số với $\cos2nt$; nếu là vận tốc thì chia $2n$ và nhân $\sin2nt$. Vì $n$ lẻ có $(-1)^n-1=-2$, hệ số lần lượt là $-4/(\pi n^2)$ và $-2/(\pi n^3)$.'''
for i in ['BT_3_2_3_16','BT_3_2_3_19']:
    extra(i,xcos)
extra('BT_3_2_3_17',r'''\textbf{Chi tiết chiếu li độ lên hệ cos nửa nguyên.} $k_n=(n+1/2)\pi$, $\cos k_n=0$, chuẩn $\int_0^1\cos^2k_nx\,dx=1/2$. Tích phân từng phần:
\[\int_0^1(1-x)\cos k_nx\,dx=\left[\frac{(1-x)\sin k_nx}{k_n}\right]_0^1+\frac1{k_n}\int_0^1\sin k_nx\,dx
=\frac{1-\cos k_n}{k_n^2}=\frac1{k_n^2}.\]
Chia chuẩn $1/2$ cho hệ số $2/k_n^2$; vận tốc đầu bằng $0$ nên không có phần sine theo thời gian.''')
triangle=r'''\textbf{Chi tiết hệ số của tam giác.} Với $f(x)=\min(x,\pi-x)$, chia tại $b=\pi/2$. Đổi $y=\pi-x$ ở nửa sau cho
\[\int_0^\pi f(x)\sin nx\,dx=(1+(-1)^{n+1})\int_0^b x\sin nx\,dx.\]
Tích phân cuối bằng $[-x\cos nx/n+\sin nx/n^2]_0^b=-b\cos(nb)/n+\sin(nb)/n^2$. Nếu $n$ chẵn, hệ số trước tích phân bằng $0$; nếu $n$ lẻ, $\cos(nb)=0$. Nhân $2/\pi$ được $4\sin(n\pi/2)/(\pi n^2)$.'''
for i in ['BT_3_2_3_20','BT_3_5_3_03']:
    extra(i,triangle)

energy=r'''\textbf{Chi tiết tích phân từng phần trong đạo hàm năng lượng.} Đặt $E=\frac12\int_0^L(u_t^2+a^2u_x^2+\kappa u^2)dx$. Với $u_{tt}-a^2u_{xx}+\gamma u_t+\kappa u=F$,
\[\begin{aligned}
E'&=\int_0^L(u_tu_{tt}+a^2u_xu_{xt}+\kappa uu_t)dx\\
&=\int_0^Lu_t(a^2u_{xx}-\gamma u_t-\kappa u+F)dx
+a^2\int_0^Lu_xu_{xt}dx+\kappa\int_0^Luu_tdx\\
&=a^2[u_tu_x]_0^L-a^2\int_0^Lu_{tx}u_xdx
+a^2\int_0^Lu_xu_{xt}dx-\gamma\int_0^Lu_t^2dx+\int_0^LFu_tdx\\
&=a^2[u_tu_x]_0^L-\gamma\int_0^Lu_t^2dx+\int_0^LFu_tdx.
\end{aligned}\]
Hai hạng $\kappa uu_t$ triệt tiêu ngay khi thế PDE; hai tích phân $u_xu_{xt}$ triệt tiêu sau tích phân từng phần. Với biên Dirichlet thuần nhất, đạo hàm vết theo $t$ cho $u_t=0$; với biên Neumann thuần nhất, $u_x=0$. Nếu định nghĩa năng lượng không có $1/2$, nhân cả đẳng thức đạo hàm với $2$.'''
for i in ['BT_3_1_3_01','VD_3_4_2_02','BT_3_4_3_03','VD_3_5_2_01','BT_3_5_3_01','BT_3_5_3_04','BT_3_5_3_06']:
    text=energy
    if i=='BT_3_1_3_01':
        text=text.replace(r'\int_0^L',r'\int_{-R}^R').replace(r'[u_tu_x]_0^L',r'[u_tu_x]_{-R}^R')
        text=text[:text.index('Với biên Dirichlet')]+r"Chọn $R$ lớn hơn miền hỗ trợ trên khoảng thời gian xét, nên $u_t=u_x=0$ ở $x=\pm R$. Với $I=2E$, nhân đẳng thức đạo hàm với $2$ để có $I'=0$."
    extra(i,text)

orthog=r'''\textbf{Chi tiết trực giao và dấu trị riêng.} Nhân $-X''=\lambda X$ bởi $X$, tích phân:
\[\lambda\int_0^LX^2dx=-[X'X]_0^L+\int_0^L(X')^2dx=\int_0^L(X')^2dx.\]
Hạng biên hết vì mỗi đầu có $X=0$ hoặc $X'=0$. Nếu $\lambda=0$, $\int(X')^2=0$ cho $X$ hằng; khi có một đầu Dirichlet, hằng đó bằng $0$. Với hai trị riêng,
\[(\lambda_m-\lambda_n)\int_0^LX_mX_n\,dx
=\int_0^L(-X_m''X_n+X_n''X_m)dx
=[-X_m'X_n+X_n'X_m]_0^L=0.\]
Nếu $\lambda_m\ne\lambda_n$, chia hiệu trị riêng cho tích vô hướng bằng $0$.'''
for i in ['VD_3_3_2_03','BT_3_3_3_05','BT_3_5_3_01']:
    extra(i,orthog)
extra('BT_3_5_3_02',r"""\textbf{Chi tiết tích phân chứng minh trực giao dầm.} Tích phân từng phần hai lần:
\[\int_0^L(X_m''''X_n-X_n''''X_m)dx=
[X_m'''X_n-X_m''X_n'-X_n'''X_m+X_n''X_m']_0^L.\]
Hai tích phân còn lại là $\int X_m''X_n''$ và $\int X_n''X_m''$, triệt tiêu khi trừ. Tại đầu ngàm $X=X'=0$, đầu tựa $X=X''=0$, đầu trượt $X'=X'''=0$, mỗi tích biên mất một thừa số. Thay phương trình hàm riêng cho $(\lambda_m-\lambda_n)\int X_mX_n=0$, rồi chia hiệu trị riêng.""")
beam_energy=r'''\textbf{Chi tiết hai lần tích phân từng phần của dầm.}
\[\int_0^L u_tu_{xxxx}dx
=[u_tu_{xxx}]_0^L-\int_0^Lu_{tx}u_{xxx}dx
=[u_tu_{xxx}-u_{tx}u_{xx}]_0^L+\int_0^Lu_{txx}u_{xx}dx.\]
Thế $u_{tt}=-a^2u_{xxxx}$ vào đạo hàm động năng. Tích phân cuối cùng triệt tiêu với đạo hàm $\frac{a^2}{2}\int u_{xx}^2$, còn $E'=a^2[u_{tx}u_{xx}-u_tu_{xxx}]_0^L$.'''
extra('BT_3_5_3_02',beam_energy)
damping=r'''\textbf{Chi tiết đổi ẩn trong ODE có cản.} Với $T=e^{-t/2}Y$,
\[T'=e^{-t/2}(Y'-Y/2),\quad T''=e^{-t/2}(Y''-Y'+Y/4).\]
Do đó $T''+T'+\Omega^2T=e^{-t/2}[Y''+(\Omega^2-1/4)Y]$. Dữ liệu $T(0)=A,T'(0)=B$ trở thành $Y(0)=A,Y'(0)=B+A/2$. Nếu $\Omega=0$, giải trực tiếp $T''+T'=0$: đặt $Z=T'$, $Z=Be^{-t}$, rồi $T=A+B(1-e^{-t})$.'''
for i in ['VD_3_5_2_01','BT_3_5_3_01','BT_3_5_3_04']:
    extra(i,damping)
duhamel=r'''\textbf{Chi tiết đạo hàm đáp ứng mode nguồn.} Đặt $D_n(t)=\omega_n^{-1}\int_0^t\sin(\omega_n(t-s))Q_n(s)ds$. Vì $\sin0=0$,
\[D_n'=\int_0^t\cos(\omega_n(t-s))Q_n(s)ds,\quad
D_n''=Q_n(t)-\omega_n\int_0^t\sin(\omega_n(t-s))Q_n(s)ds=Q_n-\omega_n^2D_n.\]
Tại $0$, $D_n=D_n'=0$. Vì thế tích phân vừa cho đúng nguồn, vừa giữ nguyên cả hai dữ liệu ban đầu của các hạng thuần nhất. Với mode hằng, $D_0=\int_0^t(t-s)Q_0(s)ds$, $D_0'=\int_0^tQ_0(s)ds$, $D_0''=Q_0(t)$, không chia cho $\omega_0=0$.'''
for i in ['VD_3_4_2_02','BT_3_4_3_03']:
    extra(i,duhamel)

extra('BT_3_6_3_06',r'''\textbf{Chi tiết các hàm dùng trong biểu thức tường minh.} Với tốc độ $1$, bán kính $1$, $d>0,t>0$,
\[K_1(d,t)=t\left[\frac{1-(d-t)^2}{4dt}\right]_0^1.\]
Với $r>0$, đặt $b=|1-r|$, $q=[t]_b^{r+1}$ và $A(s)=((1-r^2)s+rs^2-s^3/3)/(4r)$:
\[J_1(r,t)=\tfrac12\min(t,(1-r)_+)^2+A(q)-A(b).\]
Tại tâm, $K_1(0,t)=t$ khi $t<1$, bằng $0$ khi $t>1$, $J_1(0,t)=\min(t,1)^2/2$; tại $t=0$, $K_1=J_1=0$. Khi đổi $\tau=t-s$, $s$ chạy $0$ đến $\min(t,T)$ nên $\tau$ chạy ngược từ $t$ đến $(t-T)_+$:
\[\int_0^{\min(t,T)}K_1(r,t-s)ds=\int_{(t-T)_+}^{t}K_1(r,\tau)d\tau=J_1(r,t)-J_1(r,(t-T)_+).\]''')

ledger=[]
for n in (1,2,3):
    chapter=[it for it in inventory if it['section'].startswith(str(n)+'.')]
    source=R/f'chapter{n}_detailed.tex'
    current=blocks(source)
    for it in chapter:
        i=it['id']
        base=original[i]
        if i in add:
            # Each supplement stays inside the solution, alongside its final
            # formula; it is not hidden in a separate knowledge-only file.
            current[i]=base+'\n\n'+add[i].strip()
        elif i not in current:
            current[i]=base
        ledger.append({'id':i,'chapter':n,'status':'expanded' if i in add else 'reviewed',
                       'reason':'Bổ sung phép tính trung gian cụ thể.' if i in add else
                       'Đã có phép tính trực tiếp hoặc lập luận ngắn đầy đủ; không cần kéo dài thao tác sơ cấp.'})
    assert set(current)=={it['id'] for it in chapter},source
    write(source,current)
(R/'ra_soat_buoc_trung_gian_123.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
for n in (1,2,3):
    print(n,sum(x['chapter']==n for x in ledger),sum(x['chapter']==n and x['status']=='expanded' for x in ledger))
