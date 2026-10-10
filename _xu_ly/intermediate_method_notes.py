"""Intermediate algebra used by the chapter-specific knowledge sections."""

CH1={
'linear_char':r'''

**Chi tiết bước tích phân ODE.** Sau khi tìm bất biến $\rho$, viết $U'+P(s,\rho)U=Q(s,\rho)$. Chọn $M=\exp(\int_{s_0}^{s}P(r,\rho)dr)$; tính $M'=PM$, nên $MU'+M'U=MQ$. Tích phân từ $s_0$: $M(s)U(s)-U(s_0)=\int_{s_0}^sM(r)Q(r)dr$. Hằng số $U(s_0)$ phụ thuộc $\rho$; thay dữ liệu để tìm nó rồi mới đổi về tọa độ gốc.''',
'charpit':r'''

**Chi tiết tích phân và khử sau khi lập hệ.** Trong lúc tích phân theo $\tau$, nhãn $s$ và các gradient ban đầu $p_0(s),q_0(s)$ được giữ cố định. Với $p'=cp$, viết $p=p_0e^{c\tau}$; nếu $X'=dp$ thì $X=x_0+dp_0(e^{c\tau}-1)/c$ khi $c\ne0$, hoặc $X=x_0+dp_0\tau$ khi $c=0$. Với $Y'+cY=R(\tau)$, nhân $e^{c\tau}$ cho $(e^{c\tau}Y)'=e^{c\tau}R$, rồi dùng $Y(0)$ để xác định hằng số. Khử từ hai phương trình $x=X(s,\tau),y=Y(s,\tau)$; ghi rõ tổ hợp nào loại $\tau$ hoặc $s$. Nếu chỉ cho nghiệm tham số, vẫn phải có các tích phân đã tính và điều kiện Jacobian để khử cục bộ.''',
'shock':r'''

**Chi tiết tích phân đường sốc nằm trong quạt.** Nếu $s'=s/(2t)$ và $s(t_*)=x_*>0$, chia cho $s$ rồi tích phân từ $t_*$ đến $t$: $\log(s/x_*)=\frac12\log(t/t_*)$, nên $s=x_*\sqrt{t/t_*}$. Nếu quạt có tâm $x_0$, thay $s$ bằng $s-x_0$ trước khi tách biến. Khi trạng thái sát sốc thay đổi tại lần gặp tiếp theo, lập ODE mới và lấy vị trí tại lần gặp làm dữ liệu; không giữ hằng số của giai đoạn trước.'''}

CH2={
'canonical':r'''

**Chi tiết gom hệ số sau đổi biến.** Với $Lu=Au_{xx}+2Bu_{xy}+Cu_{yy}+Du_x+Eu_y+Ku$, tính riêng

$$
\begin{aligned}
a&=A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2,\\
2b&=2[A\xi_x\eta_x+B(\xi_x\eta_y+\xi_y\eta_x)+C\xi_y\eta_y],\\
c&=A\eta_x^2+2B\eta_x\eta_y+C\eta_y^2,\\
d&=A\xi_{xx}+2B\xi_{xy}+C\xi_{yy}+D\xi_x+E\xi_y,\\
e&=A\eta_{xx}+2B\eta_{xy}+C\eta_{yy}+D\eta_x+E\eta_y.
\end{aligned}
$$

Khi đó $Lu=av_{\xi\xi}+2bv_{\xi\eta}+cv_{\eta\eta}+dv_\xi+ev_\eta+Kv$. Trong lời giải từng ý, thế các số hoặc hàm hệ số vào từng dòng trước khi rút gọn. Với ba biến, tính $TM$ trước, rồi lấy tích vô hướng mỗi hàng của $TM$ với mỗi hàng của $T$ để có $TMT^T$.'''}

CH3={
'fourier':r'''

**Chi tiết tính tích phân hệ số.** Với $k=n\pi/L$, hai nguyên hàm thường dùng là

$$
\int x\sin kx\,dx=-x\cos kx/k+\sin kx/k^2,\qquad
\int x\cos kx\,dx=x\sin kx/k+\cos kx/k^2.
$$

Với đa thức $P$, ghi cả hai lần tích phân:

$$
\int_0^L P\sin kx\,dx
=\left[-P\cos kx/k\right]_0^L+
\left[P'\sin kx/k^2\right]_0^L-
\frac1{k^2}\int_0^L P''\sin kx\,dx.
$$

Chỉ bỏ hạng biên sau khi thế $0,L$ và điều kiện thực sự của $P$. Nếu dữ liệu chia đoạn, áp dụng công thức trên từng đoạn, rồi cộng các hạng tại điểm chia. Cuối cùng nhân nghịch đảo chuẩn của hàm riêng; nếu hệ số là của vận tốc, chia thêm tần số khi ghép nghiệm. Với mẫu số bằng $0$ trong tích–tổng, quay lại tích phân gốc để tính riêng.''',
'energy':r'''

**Chi tiết phép triệt tiêu tích phân.** Đạo hàm động năng cho $\int u_tu_{tt}$; dùng PDE thay $u_{tt}$. Với sóng, $\int u_tu_{xx}=[u_tu_x]-\int u_{tx}u_x$, và tích phân cuối triệt tiêu đạo hàm thế năng $\int u_xu_{xt}$. Với dầm,

$$
\int u_tu_{xxxx}=[u_tu_{xxx}-u_{tx}u_{xx}]+\int u_{txx}u_{xx}.
$$

Tích phân cuối triệt tiêu đạo hàm $\frac12\int u_{xx}^2$ sau khi nhân hệ số và giữ đúng dấu PDE. Viết hạng biên trước, sau đó mới dùng điều kiện của từng đầu.''',
'forced_modes':r'''

**Chi tiết xác nhận tích phân nguồn.** Với $D(t)=\omega^{-1}\int_0^t\sin(\omega(t-s))Q(s)ds$, lần đạo hàm đầu cho $D'=\int_0^t\cos(\omega(t-s))Q(s)ds$, vì $\sin0=0$. Lần sau cho $D''=Q(t)-\omega\int_0^t\sin(\omega(t-s))Q(s)ds=Q-\omega^2D$. Do $D(0)=D'(0)=0$, tích phân này thêm đúng nguồn mà giữ nguyên hai dữ liệu đầu.'''}
