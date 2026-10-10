NOTES={
'classification':r'''**Cách xác định cấp và dạng phương trình.** Trước hết tìm cấp đạo hàm cao nhất $m$. Sau đó xem biểu thức có tuyến tính theo các đạo hàm cấp $m$ hay không, và hệ số của chúng phụ thuộc vào biến độc lập hay vào ẩn. Cuối cùng, nếu phương trình tuyến tính, gom toàn bộ hạng chứa $u$ về một vế để xét nguồn $f$ có bằng 0 hay không. Bình phương của $u_y$ vẫn là đạo hàm cấp 1; $u_{xy}$ có cấp 2.''',
'direct':r'''**Bước 1 — Chọn biến tích phân.** Nếu PDE chỉ lấy đạo hàm theo $x$, coi $y$ là tham số; “hằng số” tích phân lúc này là một hàm của $y$. Nếu có đạo hàm hỗn hợp, có thể đặt một đạo hàm trung gian để giảm cấp.

**Bước 2 — Giải ODE theo biến đã chọn.** Với $u_x+a(x)u=f(x,y)$, dùng thừa số tích phân $M(x)=e^{\int a(x)dx}$:

$$
(Mu)_x=Mf,\qquad u=M^{-1}\left[\int Mf\,dx+C(y)\right].
$$

**Bước 3 — Kiểm tra miền.** Chia cho $x$, $y$ hoặc $u$ có thể bỏ mất nghiệm trên nơi chúng bằng 0; cần xét riêng và kiểm tra kéo dài đủ trơn.''',
'linear_char':r'''**Bước 1 — Lập hệ đặc trưng.** Với $a(x,y)u_x+b(x,y)u_y+c(x,y)u=f(x,y)$, đặt

$$
\frac{dX}{ds}=a(X,Y),\qquad \frac{dY}{ds}=b(X,Y),\qquad \frac{dU}{ds}+c(X,Y)U=f(X,Y).
$$

Hệ hai phương trình đầu xác định các đường trong mặt phẳng; tìm một bất biến $\rho(X,Y)$ dọc đường đó.

**Bước 2 — Tích phân ẩn trên đặc trưng.** Phương trình của $U$ là ODE tuyến tính; nhân $e^{\int c\,ds}$ rồi tích phân. Hàm tùy ý theo $\rho$ đóng vai trò hằng số tích phân.

**Bước 3 — Dùng dữ liệu và xét duy nhất.** Thế đường dữ liệu $(X_0(r),Y_0(r))$ vào nghiệm tổng quát. Nếu nhiều điểm dữ liệu cùng nằm trên một đặc trưng, các giá trị phải tương thích. Dữ liệu chỉ quyết định nghiệm trên các đặc trưng mà nó gặp; không tự suy ra duy nhất ngoài miền ấy.''',
'quasi_char':r'''**Bước 1 — Theo dõi ẩn cùng đặc trưng.** Với $u_t+a(x,t,u)u_x=b(x,t,u)$, trên đường $x=X(t)$ đặt $U(t)=u(X(t),t)$:

$$X'=a(X,t,U),\qquad U'=b(X,t,U),\qquad X(0)=\xi,\quad U(0)=f(\xi).$$

**Bước 2 — Khử tham số.** Giải $X,U$ rồi tìm $\xi$ từ $x=X(t;\xi)$. Điều kiện $X_\xi\ne0$ cho nghiệm cổ điển cục bộ; khi các đặc trưng giao nhau, công thức cổ điển không còn xác định đơn trị.

**Bước 3 — Với dữ liệu gián đoạn.** Nếu viết được dạng bảo toàn $u_t+(F(u))_x=0$, dùng điều kiện sốc và entropy; không nối tùy ý các nhánh giao nhau.''',
'charpit':r'''**Bước 1 — Xác định đạo hàm trên đường dữ liệu.** Đặt $p=u_x,q=u_y$, PDE $F(x,y,u,p,q)=0$. Với $u(x_0(s),y_0(s))=h(s)$, ta cần đồng thời

$$p_0x_0'(s)+q_0y_0'(s)=h'(s),\qquad F(x_0,y_0,h,p_0,q_0)=0.$$

Hai phương trình này có thể cho nhiều nhánh $(p_0,q_0)$ hoặc không có nhánh thực.

**Bước 2 — Tích phân hệ Charpit.** Trên mỗi nhánh dùng

$$
\begin{aligned}
X'&=F_p,&Y'&=F_q,&U'&=pF_p+qF_q,\\
p'&=-F_x-pF_u,&q'&=-F_y-qF_u.
\end{aligned}
$$

**Bước 3 — Chuyển thành nghiệm.** Từ $X(s,\tau),Y(s,\tau),U(s,\tau)$, khử $(s,\tau)$ ở nơi $\det\partial(X,Y)/\partial(s,\tau)\ne0$. Nếu dùng phép đổi như $\log u$ hoặc $\sqrt u$, phải giữ điều kiện dấu. Cuối cùng tính $u_x,u_y$ và thế lại vào $F=0$ cùng dữ liệu.''',
'shock':r'''**Bước 1 — Vận tốc đặc trưng.** Viết PDE dưới dạng $u_t+(F(u))_x=0$. Trong vùng trơn, $u$ không đổi dọc $x=\xi+F'(u_0(\xi))t$.

**Bước 2 — Sốc hay quạt giãn.** Với thông lượng lồi, bước nhảy $u_L>u_R$ tạo sốc; $u_L<u_R$ tạo quạt. Với thông lượng lõm, thứ tự đảo lại. Nếu thông lượng đổi độ lồi trên khoảng trạng thái, phải xét riêng điều kiện entropy.

Tốc độ sốc tại $x=s(t)$ được tính bởi

$$s'(t)=\frac{F(u_L)-F(u_R)}{u_L-u_R}.$$

Trong quạt tự đồng dạng từ $(x_0,0)$, giải $F'(u)=(x-x_0)/t$ và ghép với hai trạng thái ngoài quạt.

**Bước 3 — Ghép sau tương tác.** Tìm thời điểm sốc gặp sốc hoặc mép quạt bằng cách giải phương trình giao. Sau khi gặp, tính lại trạng thái hai phía và phương trình tốc độ; điều kiện liên tục của $s(t)$ xác định hằng số tích phân. Không nhân luật bảo toàn bởi một hàm của $u$ rồi coi nghiệm sốc của hai luật là tương đương.''',
'canonical':r'''**Bước 1 — Phần chính.** Với $Au_{xx}+2Bu_{xy}+Cu_{yy}$, tính $\delta=B^2-AC$: dương là hyperbolic, bằng 0 là parabolic, âm là elliptic tại điểm đang xét.

**Bước 2 — Chọn tọa độ và dùng quy tắc dây chuyền.** Đặt $u(x,y)=v(\xi(x,y),\eta(x,y))$ với Jacobian khác 0. Đặc biệt,

$$
u_{xx}=v_{\xi\xi}\xi_x^2+2v_{\xi\eta}\xi_x\eta_x+v_{\eta\eta}\eta_x^2+v_\xi\xi_{xx}+v_\eta\eta_{xx}.
$$

Tính tương tự $u_{xy},u_{yy}$; phải giữ các hạng cấp 1 phát sinh khi phép đổi biến không tuyến tính. Dạng chính tắc chỉ hợp lệ trên miền Jacobian không triệt tiêu.

**Bước 3 — Giải phương trình đã đổi và áp dữ liệu.** Với $v_{\xi\eta}=h$, tích phân hai lần cho $v=F(\xi)+G(\eta)+\iint h$. Với phương trình chỉ theo một tọa độ, coi tọa độ kia là tham số. Dữ liệu đặt trên đặc trưng có thể không xác định hết các hàm tùy ý.''',
'wave':r'''**Bước 1 — Hai họ đặc trưng.** Với $u_{tt}=a^2u_{xx}$, chúng là $x-at=\text{hằng}$ và $x+at=\text{hằng}$. Viết $u=A(x-at)+B(x+at)$, rồi dùng $u(x,0)=f(x)$, $u_t(x,0)=g(x)$:

$$A+B=f,\qquad -aA'+aB'=g.$$

**Bước 2 — Công thức nghiệm.** Tích phân hai đẳng thức cho d’Alembert:

$$u(x,t)=\frac{f(x-at)+f(x+at)}2+\frac1{2a}\int_{x-at}^{x+at}g(s)ds.$$

Nếu có nguồn $H(x,t)$, cộng phần Duhamel

$$\frac1{2a}\int_0^t\int_{x-a(t-s)}^{x+a(t-s)}H(y,s)\,dy\,ds.$$

**Bước 3 — Biên và tính trơn.** Biên Dirichlet 0 dùng thác triển lẻ; Neumann 0 dùng thác triển chẵn. Biên khác 0 phải cộng sóng từ biên hoặc dùng hàm khử biên. Kiểm tra các đường $x\pm at$ đi qua điểm gãy của dữ liệu; công thức nghiệm yếu có thể đúng dù nghiệm không $C^2$ qua mặt sóng.''',
'wave_series':r'''**Bước 1 — Bài trị riêng không gian.** Đặt $u=X(x)T(t)$, được $-X''=\lambda X$, $T''+a^2\lambda T=0$. Các điều kiện biên xác định cơ sở $X_n$; Dirichlet hai đầu cho $X_n=\sin(n\pi x/L)$, còn biên hỗn hợp có thể cho tần số nửa nguyên.

**Bước 2 — Khai triển dữ liệu.** Với $N_n=\int_0^LX_n^2$, đặt $f_n=N_n^{-1}\int fX_n$, $g_n=N_n^{-1}\int gX_n$, $\omega_n=a\sqrt{\lambda_n}$.

$$u=\sum_n\left[f_n\cos\omega_nt+\frac{g_n}{\omega_n}\sin\omega_nt+\int_0^t\frac{\sin\omega_n(t-s)}{\omega_n}H_n(s)ds\right]X_n.$$

Mode $\omega_n=0$, nếu có, được hiểu bằng giới hạn $\sin\omega_nt/\omega_n=t$. Với biên không thuần nhất, khử biên trước khi tính hệ số nguồn. Nếu có lực cản hoặc phản ứng, giải ODE của từng mode theo hệ số thực tế của bài, không dùng nguyên công thức dao động điều hòa.''',
'wave_nd':r'''**Bước 1 — Chọn công thức theo số chiều.** Trong ba chiều, với li độ đầu bằng 0, công thức Kirchhoff là

$$u(P,t)=\frac{t}{4\pi}\int_{S^2}\psi(P+at\omega)\,d\omega.$$

Với vận tốc là hàm chỉ thị của một miền, tích phân này bằng $t$ nhân tỷ lệ diện tích mặt cầu nằm trong miền. Trong hai chiều dùng Poisson:

$$u(P,t)=\frac1{2\pi a}\int_{|Q-P|<at}\frac{\psi(Q)}{\sqrt{a^2t^2-|Q-P|^2}}\,dQ.$$

**Bước 2 — Dùng hình học hoặc đối xứng.** Chỏm cầu, tọa độ cực và đối xứng quay giúp giảm tích phân mặt thành độ dài khoảng hoặc tích phân một chiều. Phải kiểm tra bất đẳng thức gốc sau khi bình phương.

**Bước 3 — Nguồn và cực trị.** Nguồn được tích phân theo thời gian bằng Duhamel. Tìm cực trị trong từng nhánh trơn rồi xét thêm các thời điểm chuyển nhánh; dữ liệu gián đoạn đôi khi chỉ cho supremum theo giới hạn một phía.''',
'heat':r'''**Bước 1 — Tách biến hoặc khử biên.** Với $u_t=Ku_{xx}+H$ và biên thuần nhất, bài không gian là $-X''=\lambda X$. Nếu biên khác 0, chọn $b$ thỏa biên và đặt $w=u-b$, nguồn mới là $H+Kb_{xx}-b_t$.

**Bước 2 — Tính hệ số và giải từng mode.** Đặt $N_n=\int X_n^2$, $f_n=\int fX_n/N_n$, $H_n=\int HX_n/N_n$. Mỗi hệ số thời gian thỏa

$$T_n'+K\lambda_nT_n=H_n(t),\qquad T_n(0)=f_n.$$

Nhân $e^{K\lambda_nt}$ và tích phân:

$$T_n(t)=f_ne^{-K\lambda_nt}+\int_0^te^{-K\lambda_n(t-s)}H_n(s)ds.$$

**Bước 3 — Xét thời gian dài và tính tương thích.** Các mode $\lambda_n>0$ giảm; Neumann/tuần hoàn có mode hằng phải tính riêng. Nếu có $Au_x+Bu$, đổi $u=e^{-Ax/(2K)}v$ để đưa về $v_t=Kv_{xx}+(B-A^2/(4K))v$. Phải đổi cả biên lẫn dữ liệu đầu, và kiểm tra các góc tại $t=0$.''',
'maximum_heat':r'''**Bước 1 — Lập hàm so sánh.** Muốn chứng minh $u\le v$, xét $w=u-v$. Kiểm tra $w\le0$ trên biên parabol và $w_t-Kw_{xx}\le0$ trong miền (có thêm các hệ số nếu PDE của bài có chúng).

**Bước 2 — Loại cực đại dương.** Tại cực đại trong không gian–thời gian, $w_x=0,w_{xx}\le0$ và dấu $w_t$ phù hợp nên bất đẳng thức nghiêm không thể xảy ra. Với bất đẳng thức không nghiêm, dùng $w-\varepsilon e^{\gamma t}$ rồi cho $\varepsilon\downarrow0$. Neumann/Robin cần dùng dấu đạo hàm pháp tuyến; biên có nguồn không tự cho cùng cận của dữ liệu đầu.

**Bước 3 — Cực tiểu và điều kiện áp dụng.** Áp dụng tương tự cho $-w$. Phương trình có nguồn khác 0 phải kiểm tra hàm trên/dưới thực sự là nghiệm trên/dưới; không dùng nguyên lý của phương trình thuần nhất mà bỏ nguồn.''',
'heat_whole':r'''**Bước 1 — Nhân cơ bản.** Trên toàn trục, với $K>0$,

$$G_K(x,t)=\frac1{\sqrt{4\pi Kt}}e^{-x^2/(4Kt)},\qquad u(x,t)=\int_{\mathbb R}G_K(x-y,t)f(y)dy.$$

**Bước 2 — Nửa trục hoặc nguồn.** Dirichlet 0 dùng $G_K(x-y,t)-G_K(x+y,t)$ trên $y>0$; Neumann 0 dùng tổng hai nhân. Nguồn cho tích phân Duhamel $\int_0^tG_K(\cdot,t-s)*H(\cdot,s)ds$.

**Bước 3 — Tính tích phân hoặc đổi biến.** Dữ liệu Gaussian dùng hoàn thành bình phương; hàm chỉ thị cho erf/erfc. Với hệ số biến đổi, tìm phép đổi thời gian và không gian trước. Các phương trình đạo hàm cấp ba/bốn trong mục này dùng nhân Fourier riêng, không phải nhân Gauss. Trên nửa trục, thiếu biên tại 0 thường mất tính duy nhất.''',
'laplace_series':r'''**Bước 1 — Tách biên và chọn cơ sở.** Với hình chữ nhật, tách một bài có một cạnh dữ liệu khác 0 rồi chồng chất. Các cạnh đối diện Dirichlet 0 chọn sine, Neumann 0 chọn cosine; sau tách biến $-X''=\lambda X$, phần còn lại thỏa $Y''-\lambda Y=F_n$.

**Bước 2 — Giải phương trình theo tọa độ còn lại.** Khi $F_n=0$, dùng sinh/cosh thay vì sine/cosine dao động. Khi có nguồn, dùng nghiệm riêng hoặc Green của ODE. Hệ số được tính từ tích phân trực giao, ví dụ $f_n=2L^{-1}\int_0^Lf(x)\sin(n\pi x/L)dx$.

**Bước 3 — Kiểm tra tồn tại và duy nhất.** Với $\Delta u=F$, biên Neumann phải có $\int_{\partial\Omega}\partial_\nu u=\int_\Omega F$. Hiệu hai nghiệm cùng dữ liệu là điều hòa; tích phân Green xác định nó bằng 0 hoặc bằng hằng tùy biên. Các giá trị trái nhau ở góc không thể cho nghiệm liên tục trên toàn miền đóng.''',
'laplace_polar':r'''**Bước 1 — Viết toán tử theo tọa độ cực.**

$$\Delta u=u_{rr}+\frac1r u_r+\frac1{r^2}u_{\theta\theta}.$$

Với mode $\cos n\theta,\sin n\theta$, phương trình xuyên tâm thuần nhất có hai nghiệm $r^n,r^{-n}$; mode 0 có $1,\log r$. Trên đĩa chứa tâm, tính chính quy loại $r^{-n}$ và $\log r$; trên vành khuyên giữ cả hai.

**Bước 2 — Dùng dữ liệu.** Khai triển Fourier dữ liệu trên đường tròn để tìm hệ số; mỗi mode trên đĩa nhân $(r/R)^n$. Trên hình quạt, điều kiện ở hai cạnh góc xác định tần số $n\pi/\alpha$. Với Neumann, $\partial_\nu=\partial_r$ trên cung ngoài, còn trên cạnh góc là $\pm r^{-1}\partial_\theta$.

**Bước 3 — Nguồn và tương thích.** Tách một nghiệm riêng của $\Delta P=F$, rồi giải bài điều hòa cho $u-P$. Tổng thông lượng ngoài phải bằng tích phân nguồn đối với Neumann; mode hằng thể hiện đúng điều kiện này.''',
'harmonic':r'''**Các công cụ dùng trong chứng minh.** Với hai hàm đủ trơn,

$$\Delta(uv)=u\Delta v+v\Delta u+2\nabla u\cdot\nabla v.$$

Với hàm xuyên tâm $u=f(r)$ trong $\mathbb R^n$,

$$\Delta u=f''(r)+\frac{n-1}{r}f'(r).$$

Tính giá trị trung bình và công thức Poisson cho phép suy cận nội của đạo hàm. Khi dùng liên thông, tính trơn tại tâm hoặc tăng trưởng ở vô cực, phải nêu giả thiết tương ứng; bỏ một giả thiết có thể làm kết luận sai.''',
'maximum_laplace':r'''**Bước 1 — Xác nhận điều hòa và miền.** Kiểm tra $\Delta u=0$ và tính liên tục trên miền đóng nếu muốn áp dụng nguyên lý cực đại đến biên; một cực nằm trên biên có thể làm hỏng giả thiết.

**Bước 2 — Dùng cực đại hoặc giá trị trung bình.** Hàm điều hòa không hằng trên miền liên thông không đạt cực đại/cực tiểu trong miền. Trên đĩa, giá trị tâm là trung bình dữ liệu trên đường tròn. Với dữ liệu không âm, nhân Poisson dương còn cho tính dương trong miền.

**Bước 3 — Tính các giá trị biên và xét ngoại lệ.** Cực đại yếu cho cận không nghiêm; muốn dấu nghiêm phải dùng nguyên lý mạnh và loại nghiệm hằng. Với Robin, dùng $\int|\nabla w|^2=\int_{\partial\Omega}w\partial_\nu w$ cho hiệu hai nghiệm.''',
'spectral':r'''**Bước 1 — Chọn bài trị riêng đúng biên.** Giải $-L\phi=\lambda\phi$. Nếu có trôi $Au_x$, phép đổi ẩn mũ đưa về toán tử tự liên hợp nhưng đồng thời đổi điều kiện Neumann thành Robin; cần giữ sự thay đổi này.

**Bước 2 — Trực giao và hệ số.** Nếu toán tử tự liên hợp với trọng số $\sigma$, hệ số của $q$ là $q_n=\int q\phi_n\sigma/\int\phi_n^2\sigma$. Trong hình chữ nhật, hàm riêng thường là tích hai hàm một chiều và trị riêng là tổng hai trị riêng.

**Bước 3 — Giải mode của bài PDE.** Nhiệt cho $T_n'+\lambda_nT_n=H_n$; Poisson cho $-\lambda_nT_n=H_n$ sau khử biên; sóng cho $T_n''+\lambda_nT_n=H_n$. Mode 0, phổ liên tục và dữ liệu đầu dư phải xét riêng, không áp công thức chia cho $\lambda_n$ một cách máy móc.''',
'fourier':r'''**Bước 1 — Chốt quy ước.** Trên $[-L,L]$, dùng $f=a_0+\sum_{n\ge1}(a_n\cos(n\pi x/L)+b_n\sin(n\pi x/L))$, với

$$a_0=\frac1{2L}\int_{-L}^Lf,\quad a_n=\frac1L\int_{-L}^Lf\cos\frac{n\pi x}{L},\quad b_n=\frac1L\int_{-L}^Lf\sin\frac{n\pi x}{L}.$$

**Bước 2 — Tính hệ số.** Hàm chẵn chỉ có cosine, hàm lẻ chỉ có sine. Hàm phân đoạn phải chia tích phân tại điểm đổi biểu thức. Dùng tích thành tổng, tích phân từng phần hoặc chuỗi hình học/log để tính hệ số.

**Bước 3 — Hội tụ và giá trị ở mép.** Với dữ liệu trơn từng khúc, chuỗi về giá trị hàm tại điểm liên tục, về trung bình hai giới hạn tại điểm nhảy. Khai triển sine/cosine trên $[0,L]$ tương ứng thác triển lẻ/chẵn; giá trị ở đầu mút phải xét theo thác triển, không mặc nhiên bằng dữ liệu ban đầu. Hệ số suy đủ nhanh cho hội tụ đều bằng tiêu chuẩn Weierstrass.'''
}
def key(item):
    s=item['section'];ch=s.split('.')[0]
    if s=='1.2.3' and item['number']==4:return 'canonical'
    if s=='1.2.2.1' or s=='1.2.3' and item['number']<=2:return 'classification'
    if s.startswith('1.2'):return 'direct'
    if s.startswith('1.3'):return 'linear_char'
    if s.startswith('1.4'):return 'quasi_char'
    if s.startswith('1.5'):return 'charpit'
    if ch=='1':return 'shock'
    if ch=='2':return 'canonical'
    if s.startswith('3.1') or s.startswith('3.2'):return 'wave'
    if s.startswith('3.6'):return 'wave_nd'
    if ch=='3':return 'wave_series'
    if s.startswith('4.2'):return 'maximum_heat'
    if s.startswith('4.6'):return 'heat_whole'
    if ch=='4':return 'heat'
    if s.startswith('5.1'):return 'laplace_series'
    if s.startswith('5.2') or s.startswith('5.3'):return 'laplace_polar'
    if s.startswith('5.4'):return 'harmonic'
    if s.startswith('5.5'):return 'maximum_laplace'
    if ch=='5':return 'spectral'
    return 'fourier'
