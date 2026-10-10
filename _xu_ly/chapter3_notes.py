"""Trình tự giải Chương 3, dùng chung khi xuất Markdown và LaTeX."""
import re

NOTES = {
'dalembert': r"""**Bước 1 — Nhận dạng dữ liệu và tốc độ.** Viết $u_{tt}-a^2u_{xx}=F$, $u(x,0)=f(x)$, $u_t(x,0)=g(x)$; tốc độ là $a>0$, không phải $a^2$. Với dữ liệu trơn, cần $f\in C^2$, $g\in C^1$. Nếu dữ liệu có góc hoặc bước nhảy, công thức vẫn mô tả sóng từng miền nhưng phải xác định nơi mất tính trơn.

**Bước 2 — Tìm hai sóng chạy.** Đặt $\xi=x-at$, $\eta=x+at$. Quy tắc dây chuyền cho $u_{tt}-a^2u_{xx}=-4a^2u_{\xi\eta}$, nên khi $F=0$, $u=A(\xi)+B(\eta)$. Tại $t=0$, $A+B=f$, $a(B'-A')=g$. Chọn một nguyên hàm $H'=g$ rồi lấy $A=f/2-H/(2a)$, $B=f/2+H/(2a)$; hằng số của $H$ sẽ triệt tiêu.

$$
u_0(x,t)=\frac{f(x-at)+f(x+at)}2+\frac{H(x+at)-H(x-at)}{2a}.
$$

**Bước 3 — Tính tích phân theo dữ liệu thật.** Tìm nguyên hàm trên từng khoảng, nối liên tục nếu $g$ có bước nhảy; thay hai cận $x\pm at$. Dùng công thức cộng lượng giác trước khi kết luận chu kỳ. Với dữ liệu chỉ thị, tích phân bằng độ dài giao của $[x-at,x+at]$ với đoạn hỗ trợ, nhân hệ số của $g$.

**Bước 4 — Nếu có nguồn, thêm Duhamel.** Nghiệm riêng có dữ liệu đầu bằng không là

$$
u_F(x,t)=\frac1{2a}\int_0^t\int_{x-a(t-s)}^{x+a(t-s)}F(y,s)\,dy\,ds.
$$

Tính tích phân trong trước. Nếu $F$ là đa thức hoặc một mode lượng giác, có thể đoán $u_F$ rồi giải ODE theo $t$, nhưng vẫn phải buộc $u_F(x,0)=(u_F)_t(x,0)=0$. Nghiệm cuối là $u_0+u_F$.

**Bước 5 — Kiểm tra và đọc ý nghĩa.** Đạo hàm công thức: $u_x=(f'(\xi)+f'(\eta))/2+(g(\eta)-g(\xi))/(2a)$, $u_t=a(f'(\eta)-f'(\xi))/2+(g(\eta)+g(\xi))/2$. Tại $t=0$ thu lại $f,g$; đạo hàm tiếp cho PDE. Các điểm gãy $s=b$ phát sinh đường $x\pm at=b$. Chu kỳ phải đúng cho mọi $x,t$, không chỉ sau khi một mặt sóng đi qua một điểm cố định.""",
'reflection': r"""**Bước 1 — Đọc đúng điều kiện biên.** Biên $u(0,t)=0$ dùng mở rộng lẻ; biên $u_x(0,t)=0$ dùng mở rộng chẵn. Với dữ liệu trên $x\ge0$, đặt $\widetilde f(-s)=-f(s)$ hoặc $f(s)$ tương ứng, làm tương tự cho $g$. Mở rộng lẻ là $C^2$ nếu $f(0)=f''(0)=0$, và mở rộng lẻ của $g$ là $C^1$ nếu $g(0)=0$. Mở rộng chẵn đòi $f'(0)=g'(0)=0$ cho mức trơn ấy.

**Bước 2 — Lập nguyên hàm sau khi phản xạ.** Đặt $H(s)=\int_0^s\widetilde g(r)dr$. Nếu $\widetilde g$ lẻ thì $H$ chẵn; nếu $\widetilde g$ chẵn thì $H$ lẻ. Chính nguyên hàm, chứ không phải vận tốc, xuất hiện trong

$$
u=\frac{\widetilde f(x-at)+\widetilde f(x+at)}2+\frac{H(x+at)-H(x-at)}{2a}.
$$

**Bước 3 — Tách miền trước và sau khi chạm biên.** Với $u(0,t)=h(t)$, ở $x\ge at$ dùng d'Alembert với dữ liệu gốc. Ở $0<x<at$:

$$
u=h(t-x/a)+\frac{f(x+at)-f(at-x)}2+\frac1{2a}\int_{at-x}^{at+x}g(s)ds.
$$

Với $u_x(0,t)=h(t)$, dùng nghiệm của các mở rộng chẵn rồi trừ $a\int_0^{t-x/a}h(s)ds$ trên miền $x<at$. Tính riêng đạo hàm theo $x$ của hạng này để kiểm tra biên.

**Bước 4 — Trên đoạn hữu hạn, phản xạ ở cả hai đầu.** Dirichlet ở hai đầu cho mở rộng lẻ tại $0,L$, chu kỳ không gian $2L$. Neumann ở hai đầu cho mở rộng chẵn tại $0,L$, cũng chu kỳ $2L$. Một đầu lẻ, một đầu chẵn cho $\widetilde f(s+2L)=-\widetilde f(s)$ và chu kỳ $4L$, tương tự $g$. Vì thế chu kỳ thời gian thường là $2L/a$ hoặc $4L/a$. Với Neumann hai đầu còn phải xét trung bình $g$: trung bình khác không sinh hạng tuyến tính theo $t$, nên nghiệm không tuần hoàn.

**Bước 5 — Kiểm tra góc và đường ghép.** Biên Dirichlet không thuần nhất cần $h(0)=f(0)$, $h'(0)=g(0)$, $h''(0)=a^2f''(0)$ để có nghiệm $C^2$ cho phương trình thuần nhất. So sánh hai vết trên $x=at$, gồm $u,u_x,u_t$ rồi đạo hàm cấp hai. Nếu không tương thích, nêu rõ mức trơn còn lại thay vì khẳng định nghiệm cổ điển trên toàn miền.""",
'piecewise': r"""**Bước 1 — Liệt kê các khoảng của dữ liệu.** Ghi đủ điểm đầu, điểm cuối hỗ trợ, điểm gãy và bước nhảy của $f,g$. Nếu có biên, phản xạ chẵn hoặc lẻ trước khi tích phân; trên đoạn hữu hạn tiếp tục phản xạ đến một chu kỳ hoàn chỉnh.

**Bước 2 — Tính nguyên hàm liên tục.** Lấy $H'=\widetilde g$ trên từng khoảng và chọn hằng số để hai vết của $H$ bằng nhau. Viết $[s]_p^q=\min(q,\max(p,s))$ hoặc $(s)_+=\max(s,0)$ khi cần gộp nhiều nhánh. Một nguyên hàm liên tục tránh tạo ra bước nhảy giả trong nghiệm.

**Bước 3 — Xác định sóng phải và sóng trái.** Đặt $A(s)=\widetilde f(s)/2-H(s)/(2a)$, $B(s)=\widetilde f(s)/2+H(s)/(2a)$; khi đó $u=A(x-at)+B(x+at)$. Với từng $t$ được yêu cầu, dịch đồ thị $A$ sang phải $at$ và $B$ sang trái $at$, rồi cộng tung độ. Các đường $x-at=b$ và $x+at=b$ chia mặt phẳng thành các miền có công thức đơn giản.

**Bước 4 — Xét liên tục, đạo hàm và giao của các mặt sóng.** Nếu $f$ có bước nhảy, $u$ thường có bước nhảy; nếu $f$ liên tục và $g$ bị chặn thì $u$ liên tục. Tại thời điểm cố định,

$$
u_x=\frac{\widetilde f'(x-at)+\widetilde f'(x+at)}2+\frac{\widetilde g(x+at)-\widetilde g(x-at)}{2a}.
$$

Tính giới hạn trái/phải của biểu thức này tại từng vị trí ứng viên. Có thể có triệt tiêu khi hai đường gặp nhau, nên không chỉ liệt kê đường rồi khẳng định mọi đạo hàm đều mất. Với tính $C^1$ theo cả $x,t$, còn kiểm tra $u_t$. Với $C^2$, xét tiếp các góc của $g$ và đạo hàm cấp hai của $f$.

**Bước 5 — Tính thời điểm đến, giới hạn và ngưỡng.** Sóng ở $(x,t)$ chỉ nhận dữ liệu trong $[x-at,x+at]$. Giải bất đẳng thức giao hỗ trợ để tìm thời điểm đến và đi qua. Nếu $H$ hằng ngoài đoạn hỗ trợ, dùng các giá trị hằng này để tính giới hạn khi $t\to\infty$. Nếu hỏi áp suất cực đại, viết hàm từng khoảng thời gian và so sánh cực trị, bước nhảy cùng hai giá trị một phía.""",
'fourier': r"""**Bước 1 — Tách biến và chọn bài toán trị riêng theo biên.** Đặt $u=X(x)T(t)$ trong $u_{tt}=a^2u_{xx}$, suy $X''+\lambda X=0$, $T''+a^2\lambda T=0$. Tích phân từng phần cho $\lambda\int X^2=\int (X')^2$ khi hạng biên bằng không; do đó $\lambda\ge0$. Giải cả trường hợp $\lambda=0$ trước khi xét $\lambda=k^2>0$.

**Bước 2 — Tìm hệ hàm riêng.** Trên $(0,L)$: Dirichlet hai đầu dùng $\sin(n\pi x/L)$, $n\ge1$; Neumann hai đầu dùng $1$ và $\cos(n\pi x/L)$; Dirichlet–Neumann dùng $\sin((n+1/2)\pi x/L)$, $n\ge0$; Neumann–Dirichlet dùng cos của các tần số nửa nguyên ấy. Chuẩn bình phương của mode khác không là $L/2$, của mode hằng là $L$.

**Bước 3 — Chiếu cả hai dữ liệu.** Với mode khác không đặt

$$
A_n=\frac2L\int_0^L fX_n\,dx,\quad B_n=\frac2L\int_0^L gX_n\,dx,\quad \omega_n=ak_n.
$$

Tích phân từng khoảng nếu dữ liệu chia đoạn; dùng tích phân từng phần hoặc công thức tích–tổng khi là đa thức/lượng giác. Hệ số $B_n$ là hệ số của vận tốc, nên hệ số đứng trước $\sin\omega_nt$ phải là $B_n/\omega_n$.

**Bước 4 — Ghép nghiệm và xét mode hằng.**

$$
u=\sum_n\left(A_n\cos\omega_nt+\frac{B_n}{\omega_n}\sin\omega_nt\right)X_n.
$$

Với Neumann hai đầu, thêm $A_0+B_0t$, trong đó $A_0=L^{-1}\int f$, $B_0=L^{-1}\int g$. Với tần số bị thay đổi bởi hạng $u$ hoặc cản $u_t$, giải lại ODE của từng mode; không dùng nguyên tần số $ak_n$.

**Bước 5 — Kiểm tra biên, dữ liệu và hội tụ.** Mỗi mode thỏa biên; tại $t=0$ hai chuỗi cho khai triển của $f,g$. Nếu dữ liệu không tương thích ở góc, giải theo nghĩa năng lượng hoặc từng miền và nêu đường mất tính trơn; không đạo hàm một chuỗi yếu tùy ý. Chu kỳ được suy từ tất cả mode có hệ số khác không, kể cả mode hằng; hai tần số có tỷ số vô tỷ ngăn một chu kỳ chung.""",
'forced_modes': r"""**Bước 1 — Đưa điều kiện biên về thuần nhất.** Với $u(0,t)=\mu(t)$, $u(L,t)=\nu(t)$, đặt $b=(1-x/L)\mu+(x/L)\nu$. Với Neumann hai đầu đặt $b=\mu x+(\nu-\mu)x^2/(2L)$. Với Dirichlet–Neumann đặt $b=\mu+x\nu$. Viết $u=b+w$; khi đó $w$ có biên thuần nhất, nguồn $Q=F+a^2b_{xx}-b_{tt}$ và dữ liệu $f-b(x,0)$, $g-b_t(x,0)$.

**Bước 2 — Chiếu nguồn và dữ liệu lên cùng hệ hàm riêng.** Tính $Q_n(t)=\int QX_n/\int X_n^2$, $A_n$, $B_n$. Không bỏ các dữ liệu mới phát sinh từ hàm nâng biên; chúng có thể khác không ngay khi dữ liệu gốc bằng không.

**Bước 3 — Giải ODE có nguồn cho từng mode.**

$$
y_n''+\omega_n^2y_n=Q_n(t),\qquad
y_n=A_n\cos\omega_nt+\frac{B_n}{\omega_n}\sin\omega_nt+\frac1{\omega_n}\int_0^t\sin(\omega_n(t-s))Q_n(s)ds.
$$

Với mode hằng Neumann, thay công thức bằng $y_0=A_0+B_0t+\int_0^t(t-s)Q_0(s)ds$.

**Bước 4 — Xử lý cộng hưởng trước khi chia.** Nguồn $\cos\alpha t$ có đáp ứng dữ liệu không là $(\cos\alpha t-\cos\omega t)/(\omega^2-\alpha^2)$; tại $\alpha=\omega$ lấy $t\sin\omega t/(2\omega)$. Nguồn $\sin\alpha t$ có đáp ứng $(\sin\alpha t-(\alpha/\omega)\sin\omega t)/(\omega^2-\alpha^2)$; tại cộng hưởng là $\sin\omega t/(2\omega^2)-t\cos\omega t/(2\omega)$. Không thế vào phân số $0/0$.

**Bước 5 — Cộng lại hàm nâng và kiểm tra duy nhất.** Thế $u=b+\sum y_nX_n$ vào PDE và mọi dữ liệu. Với hiệu hai nghiệm, nguồn và biên bằng không; nhân phương trình với $w_t$, tích phân từng phần để có $E'=0$, $E(0)=0$, suy $w=0$. Các góc không tương thích phải được ghi riêng.""",
'energy': r"""**Bước 1 — Chọn năng lượng theo toán tử.** Với sóng dùng $E=\frac12\int(u_t^2+a^2u_x^2)dx$. Với Klein–Gordon có thêm $u$, thêm $\frac12\int u^2dx$. Với dầm $u_{tt}=-a^2u_{xxxx}$ dùng $E=\frac12\int(u_t^2+a^2u_{xx}^2)dx$, không thay $u_{xx}$ bằng $u_x$.

**Bước 2 — Đạo hàm và tích phân từng phần.** Với $u_{tt}-a^2u_{xx}+\gamma u_t+\kappa u=F$, năng lượng có hạng $\kappa u^2$ cho

$$
E'=a^2[u_tu_x]_0^L-\gamma\int u_t^2dx+\int Fu_tdx.
$$

Với dầm, tích phân hai lần cho $E'=a^2[u_{tx}u_{xx}-u_tu_{xxx}]_0^L$. Viết riêng từng hạng biên rồi dùng điều kiện biên và đạo hàm theo thời gian của điều kiện đó để cho chúng bằng không.

**Bước 3 — Suy hệ quả.** Không cản, không nguồn thì $E$ bảo toàn. Có cản $\gamma>0$ thì $E'\le0$; nếu $E$ không có hệ số $1/2$, $E'=-2\gamma\int u_t^2\ge-2\gamma E$, suy $e^{-2\gamma t}E(0)\le E(t)\le E(0)$. Với hiệu hai nghiệm cùng dữ liệu, $E(0)=0$ nên có duy nhất.

**Bước 4 — Tách biến nếu phải tìm nghiệm cụ thể.** Sóng có cản $\gamma=1$ cho $T''+T'+a^2\lambda T=0$. Đặt $T=e^{-t/2}Y$, thu $Y''+(a^2\lambda-1/4)Y=0$, $Y(0)=A$, $Y'(0)=B+A/2$. Phân biệt dao động, nghiệm kép và hàm hyperbolic. Dầm cho $X''''=k^4X$, $T''+a^2k^4T=0$; dùng đủ bốn điều kiện biên để tìm phương trình của $kL$.

**Bước 5 — Kiểm tra hệ số và khẳng định của đề.** Năng lượng đầu chứa cả $g^2$ và các đạo hàm của $f$. Thử $f=0$, $g\ne0$ để phát hiện công thức bỏ vận tốc. Với dầm, nghiệm $k=0$ phải giải trực tiếp bằng đa thức bậc ba; nghiệm $0$ của phương trình lượng giác–hyperbolic có thể chỉ là nghiệm giả do cơ sở suy biến.""",
'multidimensional': r"""**Bước 1 — Chọn Kirchhoff (3D) hoặc Poisson (2D).** Với li độ đầu bằng không, vận tốc $\psi$, tốc độ $c$, đặt $\rho=ct$. Trong ba chiều,

$$
u(P,t)=\frac t{4\pi}\int_{S^2}\psi(P+\rho\omega)d\omega.
$$

Trong hai chiều,

$$
u(P,t)=\frac1{2\pi c}\int_{|Q-P|<ct}\frac{\psi(Q)}{\sqrt{c^2t^2-|Q-P|^2}}dQ.
$$

Với li độ $f$ khác không, thêm đạo hàm theo $t$ của chính biểu thức tương ứng khi thay $\psi$ bằng $f$. Với nguồn và dữ liệu đầu không, tích phân theo thời gian của nghiệm có vận tốc là nguồn tại từng thời điểm (Duhamel).

**Bước 2 — Tận dụng hình học và đối xứng.** Chỉ thị miền $D$ biến Kirchhoff thành $t$ nhân tỷ lệ diện tích mặt cầu nằm trong $D$. Chọn trục qua tâm miền và $P$, đặt $\mu=\cos\theta$, $d\omega=d\mu\,d\phi$. Nếu điều kiện không phụ thuộc $\phi$, tỷ lệ là $|E|/2$ với $E\subset[-1,1]$. Mỗi nửa không gian cho một bất đẳng thức tuyến tính theo $\mu$; quả cầu cho một ngưỡng chỏm. Miền hợp/rút bỏ cho tổng/hiệu nếu các phần không chồng diện tích.

**Bước 3 — Viết chính xác các khoảng hợp lệ.** Giải bất đẳng thức gốc, sau đó mới bình phương khi có căn. Chia $[-1,1]$ ở nghiệm phương trình biên, kiểm tra dấu ở trung điểm từng khoảng, loại nghiệm ngoại lai. Nếu còn góc phương vị, dùng độ dài tập $\cos\phi<v$ rồi còn một tích phân theo $\mu$. Với Poisson, tích phân theo một tọa độ cho hiệu arcsin; cắt các cận vào đĩa trước khi tính.

**Bước 4 — Tính nguồn bằng nguyên hàm thời gian.** Với quả cầu bán kính $R$ cách $P$ khoảng $r>0$, đặt

$$
K_R(r,t)=t\left[\frac{R^2-(r-ct)^2}{4rct}\right]_0^1,\quad J_R(r,t)=\int_0^tK_R(r,s)ds.
$$

Tách ba giai đoạn: cả mặt cầu nằm trong miền, giao một chỏm, không giao. Nguồn bật trên $[0,T]$ cho $J_R(r,t)-J_R(r,(t-T)_+)$. Trường hợp $r=0$ tính trực tiếp, tránh chia cho $r$.

**Bước 5 — Kiểm tra chuẩn hóa, mặt sóng và cực đại.** Nếu $\psi=1$ trên toàn không gian thì $u=t$, dùng để kiểm tra hệ số. Với dữ liệu bước nhảy, chỉ kết luận cổ điển ngoài các mặt sóng. Cực đại phải xét cả điểm chuyển nhánh và giá trị một phía; nêu rõ supremum nếu chỉ đạt theo giới hạn. Nếu dùng tích phân số, ghi tham số và cách kiểm tra hội tụ; đồ thị không tự chứng minh một cực đại toàn cục.""",
'cone_polynomial': r"""**Bước 1 — Giữ nhất quán dấu toán tử.** Đặt $q=x^2+y^2-t^2$, $\Box=\partial_{xx}+\partial_{yy}-\partial_{tt}$. Phương trình $u_{tt}-\Delta u=\Phi$ là $-\Box u=\Phi$. Dữ liệu trên nón $q=0$ gợi ý mỗi hạng của nghiệm chứa ít nhất một thừa số $q$.

**Bước 2 — Tính quy tắc đạo hàm tích.** Với $H$ thuần nhất bậc $m$, dùng Euler $xH_x+yH_y+tH_t=mH$ để có $\Box(q^jH)=q^j\Box H+2j(2m+2j+1)q^{j-1}H$. Tính trực tiếp $\Box q=6$ để kiểm tra hệ số.

**Bước 3 — Lập truy hồi hữu hạn.** Viết $u=\sum a_kq^{k+1}\Box^k\Phi$. Vì $\Phi$ bậc $d-2$, hệ số khi áp dụng $\Box$ là $C_k=2(k+1)(2d-2k-1)$. Chọn $a_0=-1/C_0$, $a_k=-a_{k-1}/C_k$ để triệt tiêu các hạng còn lại. Các đạo hàm lặp của đa thức hết sau hữu hạn bước.

**Bước 4 — Chứng minh duy nhất bằng năng lượng trên miền co.** Với hiệu $v$ của hai nghiệm, đặt $E(t)=\frac12\int_{x^2+y^2<t^2}(v_t^2+|\nabla v|^2)dxdy$ cho $t<0$. Đạo hàm cả tích phân lẫn biên chuyển động. Vết $v(r,-r)=0$ cho $v_t=v_r$ và đạo hàm tiếp tuyến góc bằng không, nên thông lượng năng lượng bằng không. Nếu nghiệm đủ trơn đến đỉnh, $E(t)\to0$ khi $t\uparrow0$; do đó $E=0$, suy $v=0$ trong nón.

**Bước 5 — Thế lại nghiệm cụ thể.** Kiểm tra cả dấu PDE và $u|_{q=0}=0$. Với đa thức nguồn cụ thể, tính $\Box\Phi$ trước: nếu bằng không thì chỉ còn hạng $a_0q\Phi$.""",
}

from intermediate_method_notes import CH3 as _INTERMEDIATE
for _group,_details in _INTERMEDIATE.items():
    NOTES[_group]+=_details

def group_for(item):
    ident=item['id']; sec=item['section'].split('.')[1]; n=int(ident.rsplit('_',1)[1])
    if sec=='1':
        return 'energy' if ident=='BT_3_1_3_01' else 'reflection' if n>=6 and ident.startswith('BT_') or ident in ('VD_3_1_2_04','VD_3_1_2_05') else 'dalembert'
    if sec=='2': return 'reflection' if '_LT_' in ident else 'piecewise'
    if sec=='3': return 'fourier'
    if sec=='4': return 'forced_modes'
    if sec=='5': return 'energy'
    return 'cone_polynomial' if ident=='BT_3_6_3_09' else 'multidimensional'

def note_for(item):
    group=group_for(item); text=NOTES[group]
    if group=='piecewise': text+='\n\n'+NOTES['reflection'] if item['id'].startswith('VD_3_2_2_0') and int(item['id'][-2:])>=3 or item['id'].startswith('BT_3_2_3_') and int(item['id'][-2:])>=6 else ''
    if group=='energy' and item['section'].startswith('3.5'):
        text+='\n\n'+NOTES['fourier']
    return text

def latex_note(item):
    text=re.sub(r'\*\*([^*]+)\*\*',lambda m:r'\textbf{'+m[1]+'}',note_for(item))
    return ''.join(part if n%2==0 else '\n'+r'\['+part+r'\]'+'\n' for n,part in enumerate(text.split('$$')))
