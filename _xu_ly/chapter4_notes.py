"""Kiến thức từng bước Chương 4, dùng chung cho Markdown và LaTeX."""
import re

NOTES = {
'fourier': r"""**Bước 1 — Đọc hệ số và điều kiện biên.** Viết phương trình dưới dạng $u_t=Ku_{xx}$, $K>0$. Nếu đề ký hiệu tốc độ $a$ và viết $u_t=a^2u_{xx}$ thì thay $K=a^2$; không nhầm $a$ với $K$. Kiểm tra điều kiện đầu $f$ có khớp giá trị biên tại $t=0$ hay không. Sự không tương thích tại góc không ngăn nghiệm trơn với $t>0$, nhưng ngăn tính liên tục đến góc khi biên Dirichlet khác vết của $f$.

**Bước 2 — Tách biến và giải bài toán không gian.** Thế $u=XT$ vào PDE, chia cho $KXT$ để có $X''/X=T'/(KT)=-\lambda$. Do đó $X''+\lambda X=0$, $T'+K\lambda T=0$. Với $\lambda=k^2>0$, $X=A\cos kx+B\sin kx$; thay từng điều kiện biên để tìm $k$. Hai biên Dirichlet cho $X_n=\sin(n\pi x/L)$, $n\ge1$; hai biên Neumann cho $1$ và $\cos(n\pi x/L)$; biên Dirichlet–Neumann cho sine, biên Neumann–Dirichlet cho cosine, với $k_n=(n+1/2)\pi/L$, $n\ge0$. Trường hợp $\lambda=0$ phải giải riêng $X=A+Bx$; chỉ giữ mode hằng nếu biên cho phép.

**Bước 3 — Tính hệ số, không chỉ ghi tích phân.** Đặt $N_n=\int_0^L X_n^2dx$, $c_n=N_n^{-1}\int_0^L fX_n\,dx$. Với các mode sine/cosine chuẩn, $N_n=L/2$; mode hằng có $N_0=L$. Nếu $f$ là đa thức, tích phân từng phần đến hết; nếu $f$ chia đoạn, tách đúng cận; nếu $f$ lượng giác, dùng tích–tổng. Chẳng hạn với $k=n\pi/L$, $f(0)=f(L)=0$,

$$
\int_0^Lf\sin kx\,dx=\frac1k\int_0^Lf'\cos kx\,dx
=-\frac1{k^2}\int_0^Lf''\sin kx\,dx.
$$

Các hạng biên phải được tính trước khi bỏ. Khi tích–tổng tạo mẫu $k-m=0$, tính trực tiếp tích phân ở tần số đó.

**Bước 4 — Giải ODE và ghép nghiệm.** Nhân $T_n'+K\lambda_nT_n=0$ với $e^{K\lambda_nt}$, được $(e^{K\lambda_nt}T_n)'=0$. Vì $T_n(0)=c_n$,

$$
u(x,t)=\sum_n c_ne^{-K\lambda_nt}X_n(x).
$$

Thêm $c_0=L^{-1}\int_0^Lf$ cho Neumann hai đầu. Kiểm tra từng mode: $X_n''=-\lambda_nX_n$, nên đạo hàm theo $t$ và $K$ lần đạo hàm theo $x$ cấp hai bằng nhau.

**Bước 5 — Kiểm tra dữ liệu, hội tụ và thời gian dài.** Với $t\ge\varepsilon>0$, thừa số $e^{-K\lambda_nt}$ cho phép lấy đạo hàm chuỗi. Với dữ liệu có bước nhảy, giới hạn ban đầu tại bước nhảy là trung bình hai vết. Nếu $f\in L^1$, $|c_n|\le2\|f\|_1/L$ cho hệ chuẩn, nên tổng các mode dương tiến về không đều theo $x$. Neumann giữ trung bình; Dirichlet và biên hỗn hợp có giới hạn không. Một nghiệm giảm theo hàm mũ và khác không không thể tuần hoàn theo thời gian.""",
'energy': r"""**Bước 1 — Chọn đúng đại lượng.** Năng lượng bình phương là $I(t)=\frac12\int_0^Lu^2dx$. Để chứng minh duy nhất, áp dụng cho hiệu $w$ của hai nghiệm cùng dữ kiện; $w$ có dữ liệu đầu bằng không và biên thuần nhất. Tổng nhiệt $E=\int_0^Lu\,dx$ là đại lượng khác, dùng khi đề hỏi bảo toàn hoặc suy giảm tổng nhiệt.

**Bước 2 — Đạo hàm và tích phân từng phần.** Với $u_t=Ku_{xx}$,

$$
I'=\int_0^Luu_t\,dx
=K[uu_x]_0^L-K\int_0^Lu_x^2dx.
$$

Thay biên tại $L$ rồi trừ giá trị tại $0$. Dirichlet/Neumann thuần nhất làm hạng biên bằng không. Robin $u_x(0)=u(0)$ đóng góp $-u(0)^2$; Robin $u_x(L)=-u(L)$ đóng góp $-u(L)^2$. Biên tuần hoàn triệt tiêu hai đầu. Một điều kiện ghép khác phải được kiểm tra trực tiếp, vì hạng biên có thể dương.

**Bước 3 — Suy duy nhất và tính dương của trị riêng.** Nếu $I'\le0$ và $I(0)=0$ thì $0\le I(t)\le0$, nên $w=0$. Với $X''+\lambda X=0$, nhân với $X$ rồi tích phân:

$$
\lambda\int_0^LX^2dx=\int_0^L(X')^2dx-[XX']_0^L.
$$

Nếu vế phải không âm thì $\lambda\ge0$. Khi bằng không, buộc từng số hạng không âm bằng không và kiểm tra biên để quyết định có mode hằng hay chỉ nghiệm tầm thường.

**Bước 4 — Chứng minh trực giao.** Nhân hai phương trình riêng lần lượt với $X_m,X_n$, trừ rồi tích phân:

$$
(\lambda_n-\lambda_m)\int_0^LX_nX_mdx
=[X_nX_m'-X_n'X_m]_0^L.
$$

Biên tự liên hợp làm vế phải bằng không; $\lambda_n\ne\lambda_m$ suy trực giao. Với biên không tự liên hợp hoặc đạo hàm bậc ba, không tự động dùng công thức chiếu trực giao.

**Bước 5 — Khi có hạng phản ứng hoặc bậc đạo hàm khác.** Với Dirichlet và $u_t=Ku_{xx}+Au_x+Bu$, hạng $A\int uu_x=A[u^2]_0^L/2=0$, nên $I'=-K\int u_x^2+2BI\le2BI$; $e^{-2Bt}I$ không tăng, vẫn suy duy nhất. Với $u_t=Ku_{xxx}$, tích phân hai lần cho $I'=K[uu_{xx}-u_x^2/2]_0^L$. Với tổng nhiệt trong bài Neumann có $-ru$, $E'=K[u_x]_0^L-rE$; giải ODE này trước khi kết luận.""",
'maximum': r"""**Bước 1 — Viết toán tử và biên parabol.** Đặt $P=\partial_t-a(x,t)\partial_{xx}-b(x,t)\partial_x-c(x,t)$ với $a\ge0$, $c\le0$. Biên parabol gồm mặt $t=0$ và các biên không gian; mặt $t=T$ vẫn thuộc miền được ước lượng. Với phương trình nhiệt, $a=K>0$, $b=c=0$.

**Bước 2 — Loại cực đại dương bằng dấu đạo hàm.** Tại cực đại dương nội miền, $w_x=0$, $w_{xx}\le0$, $w_t=0$; nếu cực đại trên mặt thời gian trên thì đạo hàm một phía cho $w_t\ge0$. Suy $Pw\ge0$, mâu thuẫn $Pw<0$. Với $Pw\le0$, xét $w_\varepsilon=w-\varepsilon e^{\gamma t}$, $\gamma>0$: $Pw_\varepsilon=Pw-\varepsilon(\gamma-c)e^{\gamma t}<0$. Chứng minh $w_\varepsilon\le0$ rồi cho $\varepsilon\downarrow0$.

**Bước 3 — So sánh hai hàm bằng hiệu.** Để chứng minh $v\le u\le V$, kiểm tra $Pv\le Pu\le PV$ và thứ tự của dữ liệu đầu, biên. Áp dụng bước 2 cho $v-u$ và $u-V$. Nếu có nguồn dương, hằng số không nhất thiết là nghiệm trên, nên phải tính $PV-Pu$; không dùng cực đại của dữ liệu để chặn một bài có nguồn mà chưa kiểm tra.

**Bước 4 — Xử lý Neumann, Robin và tuần hoàn.** Neumann thuần nhất có thể phản xạ chẵn qua đầu mút; điểm biên trở thành điểm trong. Robin viết theo pháp tuyến ngoài $\partial_\nu u+\sigma u=0$, $\sigma\ge0$. Tại cực đại dương không hằng, bổ đề Hopf cho $\partial_\nu u>0$, trái với $\partial_\nu u=-\sigma u\le0$. Với Robin phải thêm mức $0$ vào cận hằng nếu dữ liệu mang một dấu. Biên tuần hoàn ghép hai đầu thành đường tròn; không còn biên không gian.

**Bước 5 — Miền vô hạn và nguồn bị chặn.** Trên toàn trục/nửa trục, cần nghiệm bị chặn trên mỗi dải thời gian (hoặc điều kiện tăng trưởng đủ dùng). Dùng rào $\varepsilon((x-x_0)^2+2Kt)$ trên đoạn lớn, áp dụng cực đại trên miền hữu hạn rồi cho $\varepsilon\downarrow0$; cách này loại ảnh hưởng từ vô cực. Nếu $|Pu|\le N$ và $|u|\le M$ trên biên parabol, đặt $V=M+Nt$. Vì $PV=N-cV\ge N$, suy $|u|\le M+Nt\le M+NT$. $M$ ở đây là cận của $|u|$, không phải cực đại có dấu.""",
'green': r"""**Bước 1 — Tìm cơ sở và chuẩn.** Giải $-X_n''=\lambda_nX_n$ với đúng biên thuần nhất. Đặt $N_n=\int_0^LX_n^2dx$; các hàm riêng ở biên Robin không có chuẩn mặc định $L/2$. Từ $c_n=N_n^{-1}\int fX_n$ trong chuỗi nghiệm, đổi thứ tự tổng–tích phân với $t>0$ để nhận ra

$$
G(x,y,t)=\sum_n\frac{X_n(x)X_n(y)}{N_n}e^{-K\lambda_nt},\qquad
u(x,t)=\int_0^LG(x,y,t)f(y)dy.
$$

**Bước 2 — Tính chuẩn Robin đến biểu thức sơ cấp.** Nếu $X=\cos kx+\sin kx/k$, dùng

$$
N=\frac L2(1+k^{-2})+\frac{\sin(2kL)}{4k}(1-k^{-2})+\frac{\sin^2(kL)}{k^2}.
$$

Nếu $X=\cos kx$, $N=L/2+\sin(2kL)/(4k)$. Hai biên tuần hoàn có mode hằng $1/L$ trong $G$ và cặp sine/cosine tần số $2n\pi/L$.

**Bước 3 — Kiểm tra PDE, biên và đối xứng.** Đạo hàm $e^{-K\lambda_nt}X_n(x)$ cho $G_t=KG_{xx}$; đạo hàm theo $y$ tương tự. Biên được kiểm tra trên từng $X_n$. Mỗi tích $X_n(x)X_n(y)$ đối xứng; hội tụ đều của chuỗi đạo hàm trên $t\ge\varepsilon$ biện minh các thao tác. Dữ liệu delta ban đầu hiểu qua $\int Gf\to f$ trong miền hoặc trong $L^2$, không bằng cách thế $t=0$ trực tiếp vào một chuỗi không hội tụ.

**Bước 4 — Chứng minh dương và khối lượng.** Nguyên lý cực đại cho $\int Gf\ge0$ với $f\ge0$, suy $G\ge0$ bằng cách lấy $f$ tập trung gần một điểm. Kết hợp tính nửa nhóm và nguyên lý mạnh để suy $G>0$ trong miền. $m(x,t)=\int G(x,y,t)dy$ là nghiệm có dữ liệu đầu $1$. Neumann/tuần hoàn giữ $m=1$; Dirichlet hoặc Robin hấp thụ cho $0<m<1$.

**Bước 5 — Nửa nhóm và thời gian dài.** Trực giao cho $\int G(x,z,s)G(z,y,t)dz=G(x,y,s+t)$. Với $H(t)=\max_xm(x,t)$ ở Dirichlet, $m(x,t+s)\le H(t)m(x,s)$, nên $H(t+s)\le H(t)H(s)<H(t)$. Để chứng minh $H(t)\to1$ lúc đầu, giữ một $x_0$ trong miền, dùng $m(x_0,t)\to1$ và $m(x_0,t)\le H(t)\le1$.""",
'forced': r"""**Bước 1 — Khử điều kiện biên không thuần nhất.** Viết $u=b+w$ với $b$ thỏa đúng biên. Dirichlet hai đầu: $b=\mu+(\nu-\mu)x/L$. Neumann hai đầu: $b=\mu x+(\nu-\mu)x^2/(2L)$. Neumann–Dirichlet: $b=\nu+\mu(x-L)$; Dirichlet–Neumann: $b=\mu+x\nu$. Robin trái–Dirichlet phải: $b=\mu+d+dx$, $d=(\nu-\mu)/(L+1)$. Neumann trái–Robin phải: $b=\nu-\mu(L+1)+\mu x$. Hai Robin: $b=\mu+d+dx$, $d=(\nu-\mu)/(L+2)$.

**Bước 2 — Tính lại nguồn và dữ liệu đầu.** Từ $u_t=Ku_{xx}+F$ suy $w_t=Kw_{xx}+Q$, $Q=F+Kb_{xx}-b_t$, $w(x,0)=f(x)-b(x,0)$. Tính $b_t,b_{xx}$ trước khi chiếu; với hàm nâng bậc hai Neumann, $Kb_{xx}$ không bằng không. Nếu dùng trạng thái dừng $P$, giải $KP''+F=0$ và đúng biên rồi đặt $w=u-P$.

**Bước 3 — Chiếu và giải ODE bằng nhân tử.** Với $N_n=\int X_n^2$, đặt $d_n=N_n^{-1}\int(f-b_0)X_n$, $Q_n(t)=N_n^{-1}\int QX_n$. Phương trình mode là $T_n'+K\lambda_nT_n=Q_n$. Nhân với $e^{K\lambda_nt}$, tích phân từ $0$ đến $t$, rồi chia:

$$
T_n=d_ne^{-K\lambda_nt}+\int_0^te^{-K\lambda_n(t-s)}Q_n(s)ds,\qquad
u=b+\sum_nT_nX_n.
$$

Đây cũng là công thức Green $u=b+\int G(f-b_0)+\int_0^t\int GQ$ cho biên đã được khử.

**Bước 4 — Thực hiện tích phân thời gian.** Với $Q_n(s)=C_ne^{-\rho s}$, đặt $d=K\lambda_n$:

$$
\int_0^te^{-d(t-s)}C_ne^{-\rho s}ds
=C_ne^{-dt}\int_0^te^{(d-\rho)s}ds
=C_n\frac{e^{-\rho t}-e^{-dt}}{d-\rho}.
$$

Nếu $d=\rho$, kết quả là $C_nte^{-dt}$. Với nguồn hằng, kết quả $C_n(1-e^{-dt})/d$ khi $d>0$; mode $d=0$ phải dùng $\int_0^tQ_0(s)ds$. Nguồn đa thức thời gian tích phân từng phần hoặc giải ODE với nghiệm riêng đa thức.

**Bước 5 — Kiểm tra và tìm giới hạn.** Mỗi mode đúng PDE, biên; $T_n(0)=d_n$ trả lại dữ liệu đầu sau khi cộng $b_0$. Tách mode hằng Neumann: $\frac d{dt}\int u=K(\nu-\mu)+\int F$. Trạng thái dừng chỉ tồn tại nếu tổng nguồn và thông lượng cân bằng. Với các mode dương, kiểm tra hội tụ đủ để lấy giới hạn đều; không bỏ một mode bằng không hoặc mode tăng.""",
'drift': r"""**Bước 1 — Loại đạo hàm cấp một bằng tính đạo hàm đầy đủ.** Với $u_t=Ku_{xx}+Au_x+Bu$, đặt $u=e^{-hx}v$, $h=A/(2K)$. Khi đó

$$
u_t=e^{-hx}v_t,\quad u_x=e^{-hx}(v_x-hv),\quad
u_{xx}=e^{-hx}(v_{xx}-2hv_x+h^2v).
$$

Thay vào PDE, hệ số $v_x$ là $A-2Kh=0$, hệ số $v$ là $Kh^2-Ah+B=B-A^2/(4K)$. Vì thế $v_t=Kv_{xx}+Cv$, $C=B-A^2/(4K)$; có thể tiếp tục đặt $v=e^{Ct}z$ để $z_t=Kz_{xx}$.

**Bước 2 — Đổi dữ liệu và biên cùng phép đổi ẩn.** $v(x,0)=e^{hx}f(x)$. Dirichlet thuần nhất giữ nguyên; Neumann biến thành $v_x-hv=0$, nên không giữ nguyên một cơ sở cosine nếu $A\ne0$. Với Dirichlet:

$$
u=e^{-hx}\sum_{n\ge1}\left(\frac2L\int_0^Le^{hy}f(y)\sin\frac{n\pi y}Ldy\right)
e^{[C-K(n\pi/L)^2]t}\sin\frac{n\pi x}L.
$$

**Bước 3 — Tính hệ số mũ–đa thức.** Dùng nguyên hàm

$$
\int e^{hy}\sin ky\,dy
=\frac{e^{hy}(h\sin ky-k\cos ky)}{h^2+k^2}.
$$

Với $y e^{hy}$ hoặc $y(1-y)e^{hy}$, lấy đạo hàm theo $h$ của tích phân đã tính trên cận cố định; trình bày đạo hàm để tìm hệ số thực. Cách này tránh để lại một tích phân sơ cấp chưa thực hiện.

**Bước 4 — Hệ số không gian biến thiên.** Với $x^2u_{xx}$ trên $x>0$, đặt $z=\ln x$: nếu $U(z,t)=u(e^z,t)$ thì $u_x=U_z/x$, $x^2u_{xx}=U_{zz}-U_z$. Đổi miền và biên sang biến $z$ rồi dùng bước 1. Biên không thuần nhất nên tìm trạng thái dừng trước khi khai triển.

**Bước 5 — Duy nhất và ổn định.** Với hiệu nghiệm Dirichlet, $I'=-K\int w_x^2+2BI\le2BI$ suy $w=0$ khi $I(0)=0$. Giới hạn phụ thuộc các số $C-K\lambda_n$ có hệ số khác không: âm thì giảm, bằng không thì tồn tại mode dừng, dương thì tăng. Phải kiểm tra tính thống nhất giữa miền PDE và vị trí biên trước khi dùng công thức.""",
'whole': r"""**Bước 1 — Chọn nhân nhiệt theo miền và hệ số.** Trên $\mathbb R$, $g_K(z,t)=(4\pi Kt)^{-1/2}e^{-z^2/(4Kt)}$, $u=g_K*f$. Trên nửa trục, thác triển lẻ cho Dirichlet $0$, chẵn cho Neumann $0$; sau đổi $y\mapsto-y$ ở nửa âm:

$$
H_D(x,y,t)=g_K(x-y,t)-g_K(x+y,t),\qquad
H_N(x,y,t)=g_K(x-y,t)+g_K(x+y,t).
$$

Kiểm tra $H_D(0,y,t)=0$, $\partial_xH_N(0,y,t)=0$. Nửa trục phải có một điều kiện biên; dữ liệu đầu một mình không xác định duy nhất.

**Bước 2 — Tính các tích phân không gian.** Mode $\sin ky,\cos ky$ biến thành $e^{-Kk^2t}\sin kx,e^{-Kk^2t}\cos kx$. Với Gauss $e^{-\alpha(y-m)^2}$, $\alpha>0$, hoàn thành bình phương:

$$
-\frac{(x-y)^2}{4Kt}-\alpha(y-m)^2
=-\frac{1+4\alpha Kt}{4Kt}\left(y-\frac{x+4\alpha Ktm}{1+4\alpha Kt}\right)^2
-\frac{\alpha(x-m)^2}{1+4\alpha Kt}.
$$

Đổi biến để $\int_{\mathbb R}e^{-z^2}dz=\sqrt\pi$, suy $(g_K*f)(x)=e^{-\alpha(x-m)^2/(1+4\alpha Kt)}/\sqrt{1+4\alpha Kt}$. Với dữ liệu chỉ thị đoạn, cận hữu hạn tạo $\operatorname{erf}$; với $e^{-y}$ trên nửa trục, cận $0,\infty$ tạo $\operatorname{erfc}$, trong đó $\operatorname{erf}z=2\int_0^ze^{-r^2}dr/\sqrt\pi$, $\operatorname{erfc}z=1-\operatorname{erf}z$.

**Bước 3 — Thêm nguồn và biên.** Nguồn cho $u=g_K*f+\int_0^tg_K(\cdot,t-s)*F(\cdot,s)\,ds$, hoặc thay $g_K$ bằng $H_D,H_N$. Biên Dirichlet $\mu(t)$ trên nửa trục thêm

$$
\int_0^t\frac{x\,e^{-x^2/[4K(t-s)]}}{\sqrt{4\pi K}(t-s)^{3/2}}\mu(s)ds.
$$

Nguồn một mode giảm cùng tốc độ khuếch tán cho tích phân thời gian hằng sau khi gom mũ, nên xuất hiện $te^{-Kk^2t}$.

**Bước 4 — Đổi biến khi hệ số phụ thuộc thời gian hoặc có vận chuyển.** Với $u_t=a(t)u_{xx}+b(t)u_x+c(t)u$, đặt $A=\int_0^ta$, $B=\int_0^tb$, $C=\int_0^tc$, $u=e^Cv(x+B,A)$. Tính $u_t=e^C(cv+bv_z+av_\tau)$, $u_x=e^Cv_z$, $u_{xx}=e^Cv_{zz}$, suy $v_\tau=v_{zz}$. Dấu dịch là $x+B$, không phải $x-B$. Với hạng $xu_x$, dùng $z=e^{\pm t}x$ và chọn đồng hồ $\tau'(t)=e^{\pm2t}$.

**Bước 5 — Nhiều chiều và kiểm tra.** Nhân $n$ chiều là tích các nhân một chiều. Dữ liệu dạng tích tách được tích phân không gian bằng Fubini; nguồn dạng tích vẫn phải tích phân theo một thời gian chung $s$. Kiểm tra PDE bằng đạo hàm Duhamel: đạo hàm cận trên trả lại $F(x,t)$, phần còn lại bằng $K\Delta u$. Nhân Gauss là xấp xỉ đơn vị, nên trả lại dữ liệu tại điểm liên tục; dữ liệu nhảy không cho nghiệm liên tục đến mọi điểm lúc đầu.""",
'higher': r"""**Bước 1 — Phân biệt đạo hàm cấp hai, ba và bốn.** Quy ước $\widehat f(\xi)=\int e^{-i\xi x}f(x)dx$, biến đổi ngược có hệ số $1/(2\pi)$. Khi đó $\widehat{f^{(m)}}=(i\xi)^m\widehat f$, $\widehat{xf}=i\partial_\xi\widehat f$, $\widehat{xf_x}=-\widehat f-\xi\partial_\xi\widehat f$.

**Bước 2 — Giải phương trình của biến đổi.** $u_t=u_{xx}$ cho $\widehat u=e^{-t\xi^2}\widehat f$. $u_t=u_{xxx}$ cho $\widehat u=e^{-it\xi^3}\widehat f$. $u_t=-u_{xxxx}$ cho $\widehat u=e^{-t\xi^4}\widehat f$. Với $xu_x$, giải PDE cấp một theo $\xi$ bằng đường đặc trưng, gồm cả hệ số biên độ $-\widehat u$.

**Bước 3 — Biến đổi ngược và ý nghĩa tích phân.** Nhân bậc ba là $A_t(x)=(3t)^{-1/3}\operatorname{Ai}(-x/(3t)^{1/3})$, tích phân dao động. Nhân bậc bốn là $B_t(x)=(2\pi)^{-1}\int e^{i\xi x-t\xi^4}d\xi$, hội tụ tuyệt đối theo $\xi$ và có thể đổi dấu. Không áp dụng tính dương của Gauss hay nguyên lý cực đại cấp hai cho hai nhân này.

**Bước 4 — Miền hữu hạn cần kiểm tra biên và toán tử liên hợp.** Với $u_t=Ku_{xxx}$, $u(0)=u_x(0)=u(L)=0$, năng lượng cho $I'=-K u_x(L)^2/2$. Toán tử liên hợp là $-KD^3$ với $Y(0)=Y(L)=Y'(L)=0$. Đây không phải bài Sturm–Liouville tự liên hợp cấp hai; không suy mọi trị riêng đều thực và không tự dùng hệ số $\int fX/\int X^2$. Có thể giải bằng biến đổi Laplace theo thời gian và nghiệm cơ bản của ODE bậc ba, tránh khẳng định cơ sở chưa chứng minh.

**Bước 5 — Nêu lớp dữ liệu đủ cho công thức.** Với bậc ba trên toàn trục, công thức Fourier hợp lệ trước hết cho dữ liệu Schwartz hoặc $L^2$ theo nghĩa biến đổi Fourier. Dữ liệu liên tục bị chặn là phân phối tempered; phép nhân $e^{-it\xi^3}\widehat f$ vẫn hợp lệ vì các đạo hàm của thừa số tăng đa thức, nên xác định nghiệm trong $\mathcal S\prime$. Tuy nhiên điều đó không bảo đảm tích phân Airy hội tụ tuyệt đối hay nghiệm tự động là hàm cổ điển. Ghi đúng ý nghĩa của công thức theo lớp dữ liệu."""
}

def group_for(item):
    ident=item['id']; sec=item['section'].split('.')[1]
    if sec=='1':
        return 'energy' if ident in ('VD_4_1_2_03','BT_4_1_3_02','BT_4_1_3_05') else 'fourier'
    if sec=='2': return 'maximum'
    if sec=='3': return 'green'
    if sec=='4': return 'forced'
    if sec=='5':
        return 'higher' if ident=='VD_4_5_2_02' else 'energy' if ident=='BT_4_5_3_05' else 'drift'
    return 'higher' if ident=='BT_4_6_3_04' else 'whole'

def note_for(item):
    group=group_for(item)
    return NOTES[group]

def latex_note(item):
    text=re.sub(r'\*\*([^*]+)\*\*',lambda m:r'\textbf{'+m[1]+'}',note_for(item))
    return ''.join(part if n%2==0 else '\n'+r'\['+part+r'\]'+'\n' for n,part in enumerate(text.split('$$')))
