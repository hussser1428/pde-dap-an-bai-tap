"""Kiến thức theo từng dạng bài Chương 2; dùng chung cho Markdown và LaTeX."""
import re

NOTES = {
'coordinates': r'''**Mục tiêu.** Tính đạo hàm khi đổi tọa độ rồi thay vào PDE. Đổi tọa độ của điểm và đổi biểu thức của hàm là hai việc cần làm cùng nhau: đặt $q=q(x)$ và $v(q)=u(x(q))$.

**Bước 1 — Kiểm tra phép đổi biến.** Tính $J=\det(\partial q/\partial x)$. Chỉ dùng các công thức trên miền $J\ne0$ và chọn một nhánh liên tục cho các góc. Tọa độ cực/trụ loại trục $r=0$; tọa độ cầu còn loại $\sin\theta=0$. Đây là suy biến của tọa độ, chưa phải kết luận rằng hàm $u$ không tồn tại ở đó.

**Bước 2 — Tính đạo hàm cấp một bằng quy tắc dây chuyền.** Nếu $b_{ik}=\partial q_k/\partial x_i$, thì

$$
u_{x_i}=\sum_k b_{ik}v_{q_k},\qquad D_i=\sum_k b_{ik}\partial_{q_k}.
$$

Với $q=Ax$, $b_{ik}=a_{ki}$ là hằng số. Với tọa độ cong, lấy nghịch đảo ma trận $\partial x/\partial q$ để tìm $b_{ik}$.

**Bước 3 — Lấy đạo hàm cấp hai cả hàm lẫn hệ số.** Áp dụng đạo hàm tích cho từng hạng:

$$
u_{x_ix_j}=\sum_{k,l}b_{ik}b_{jl}v_{q_kq_l}
+\sum_{k,l}b_{ik}(\partial_{q_k}b_{jl})v_{q_l}.
$$

Hạng thứ hai chỉ mất đi khi phép đổi biến tuyến tính. Ví dụ $\partial_x=\cos\theta\,\partial_r-(\sin\theta/r)\partial_\theta$ thì lần đạo hàm tiếp theo phải tác động lên cả $\cos\theta$ và $\sin\theta/r$.

**Bước 4 — Thu gọn toán tử.** Gom hệ số của từng $v_{q_kq_l}$ và $v_{q_k}$ trước khi cộng. Với Laplace, lấy tổng các đạo hàm $u_{x_ix_i}$. Trong hệ trực giao có hệ số độ dài $h_1,h_2,h_3$, có thể đối chiếu bằng

$$
\Delta u=\frac1{h_1h_2h_3}\sum_{k=1}^3
\partial_{q_k}\left(\frac{h_1h_2h_3}{h_k^2}v_{q_k}\right).
$$

**Bước 5 — Kiểm tra bằng hàm đơn giản.** Thử $u=1$, $u=x_i$ và $u=x_1^2+x_2^2+x_3^2$. Công thức Laplace phải lần lượt cho $0$, $0$, $6$. Với Hessian biểu diễn trong cơ sở trực chuẩn, đổi lại cơ sở Descartes bằng $H_x=E H_q E^T$, không nhầm Hessian với ma trận chỉ gồm các đạo hàm $v_{q_kq_l}$.''',
'canonical': r'''**Mục tiêu.** Phân loại và đưa phương trình tuyến tính cấp hai về dạng chính tắc, có giữ đầy đủ các hạng cấp thấp.

**Bước 1 — Chuẩn hóa hệ số.** Viết

$$
A u_{xx}+2B u_{xy}+C u_{yy}+D u_x+E u_y+K u=f.
$$

Hệ số $B$ bằng một nửa hệ số in trước $u_{xy}$. Tính $\delta=B^2-AC$: dương là hyperbolic, âm là elliptic, bằng $0$ là parabolic nếu phần cấp hai còn khác $0$. Phải xét theo từng miền khi hệ số thay đổi hoặc suy biến.

**Bước 2 — Chọn biến mới.** Với hyperbolic, giải $A(dy)^2-2Bdxdy+C(dx)^2=0$ để tìm hai bất biến $\xi,\eta$ của hai họ đặc trưng. Với parabolic, chỉ có một họ: lấy bất biến $s$ và một biến $z$ độc lập. Với elliptic, không có hai họ đặc trưng thực; hoàn thành bình phương của phần chính để loại hạng hỗn hợp rồi cân bằng hai hệ số dương. Mọi trường hợp đều kiểm tra Jacobian khác $0$.

**Bước 3 — Viết công thức thay đạo hàm.** Nếu $u(x,y)=v(\xi,\eta)$ thì

$$
\begin{aligned}
u_x&=\xi_xv_\xi+\eta_xv_\eta,\\
u_{xx}&=\xi_x^2v_{\xi\xi}+2\xi_x\eta_xv_{\xi\eta}
+\eta_x^2v_{\eta\eta}+\xi_{xx}v_\xi+\eta_{xx}v_\eta.
\end{aligned}
$$

Làm tương tự cho $u_{xy},u_{yy}$. Có thể dùng toán tử $\partial_x,\partial_y$ để rút ngắn, nhưng phải nêu các đạo hàm của hệ số nếu đổi biến phi tuyến.

**Bước 4 — Gom hệ số và chia hợp lệ.** Hệ số mới của $v_{\xi\xi}$ là $A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2$; hệ số của $v_{\xi\eta}$ là $2[A\xi_x\eta_x+B(\xi_x\eta_y+\xi_y\eta_x)+C\xi_y\eta_y]$. Hệ số mới của $v_\xi$ là $A\xi_{xx}+2B\xi_{xy}+C\xi_{yy}+D\xi_x+E\xi_y$. Chỉ chia cho hệ số khác $0$ trên miền đang xét.

**Bước 5 — Với ba biến.** Lập ma trận đối xứng $M$ của phần cấp hai; hệ số hỗn hợp được chia đôi. Dùng hoàn thành bình phương để tìm số hướng dương, âm và bằng $0$. Nếu $\xi=T x$, ma trận mới là $TMT^T$. Cho rõ ma trận $T$ và kiểm tra nó khả nghịch; chỉ ghi dấu của dạng toàn phương chưa đủ để thực hiện phép đổi biến.''',
'hyperbolic': r'''**Mục tiêu.** Giải phương trình hyperbolic sau khi đã tìm hai tọa độ đặc trưng độc lập.

**Bước 1 — Phân loại, tìm đặc trưng và thay đạo hàm.** Làm đủ các bước của phép đưa về chính tắc. Viết cả phép đổi ngược để biểu diễn vế phải $\widetilde f(\xi,\eta)=f(x(\xi,\eta),y(\xi,\eta))$.

**Bước 2 — Tích phân phương trình chính tắc.** Với $v_{\xi\eta}=g$, giữ biến kia cố định khi tích phân:

$$
v=F(\xi)+G(\eta)+\int_{\xi_0}^{\xi}\int_{\eta_0}^{\eta}g(a,b)\,db\,da.
$$

Nếu tìm được một nghiệm riêng $P(x,y)$ dễ hơn, viết $u=P+F(\xi)+G(\eta)$. Với $v_{\xi\eta}+\alpha v_\eta=0$, đặt $w=v_\eta$, giải $w_\xi+\alpha w=0$ rồi tích phân theo $\eta$; thu được $v=F(\xi)+e^{-\alpha\xi}G(\eta)$.

**Bước 3 — Đổi cả dữ liệu.** Thế tọa độ đường dữ liệu vào $\xi,\eta$, dùng quy tắc dây chuyền cho đạo hàm được cho. Trên đường không đặc trưng, hai dữ liệu thường xác định hai hàm $F,G$. Trên đường đặc trưng, có biến không thay đổi, nên dữ liệu chỉ xác định giá trị hoặc đạo hàm của một hàm tại một điểm; phải tìm điều kiện tương thích và nêu phần tùy ý còn lại.

**Bước 4 — Lập đẳng thức hình bình hành.** Với $v=F(\xi)+G(\eta)$, bốn đỉnh theo hai họ đặc trưng thỏa $v_{11}+v_{22}=v_{12}+v_{21}$. Nếu có số hạng mũ, trước hết nhân trọng số để được tổng hai hàm một biến. Với vế phải $g$, hiệu bốn đỉnh bằng tích phân kép của $g$ trên hình chữ nhật trong tọa độ mới.

**Bước 5 — Xác định miền được dữ liệu quyết định.** Hai đặc trưng đi qua điểm đang xét phải gặp đoạn dữ liệu phù hợp. Với phương trình sóng $v_{tt}=v_{zz}$ trên $z>0$, dữ liệu lúc $t=0$ xác định duy nhất miền $z>t$; ở $0<z<t$, cần thêm dữ liệu biên $z=0$. Với đặc trưng cong, dùng miền trong các tọa độ mới rồi đổi lại.

**Bước 6 — Kiểm tra.** Thế nghiệm vào cả PDE và từng điều kiện. Nếu đề yêu cầu hai nghiệm, chỉ rõ hai lựa chọn khác nhau cho hàm tùy ý và chứng minh phần chênh lệch thỏa phương trình thuần nhất, đồng thời triệt tiêu trên đường dữ liệu.''',
'parabolic': r'''**Mục tiêu.** Tận dụng phần cấp hai có dạng bình phương một đạo hàm theo hướng để giảm PDE thành ODE có tham số.

**Bước 1 — Nhận ra hướng đạo hàm.** Nếu $D=a\partial_x+b\partial_y$ có hệ số hằng, $D^2u=a^2u_{xx}+2ab u_{xy}+b^2u_{yy}$. Với hệ số biến thiên phải dùng

$$
D^2u=a^2u_{xx}+2ab u_{xy}+b^2u_{yy}+(Da)u_x+(Db)u_y.
$$

So sánh cả hạng cấp một trước khi kết luận PDE bằng $D^2u+\lambda Du+\mu u=f$.

**Bước 2 — Tìm bất biến $s$ và biến tiến $z$.** Giải $Ds=0$, chọn $Dz=k\ne0$. Kiểm tra $J=\partial(s,z)/\partial(x,y)\ne0$. Khi $k$ hằng, $D=k\partial_z$; PDE trở thành ODE theo $z$, trong đó $s$ là tham số. Nếu còn $v_s$, phải giữ lại, chỉ các trường hợp nó triệt tiêu mới giải trực tiếp như ODE.

**Bước 3 — Giải ODE.** Với $v_{zz}=g(s,z)$, tích phân hai lần cho $v=zF(s)+G(s)+\int_{z_0}^z(z-t)g(s,t)dt$. Với $a v_{zz}+b v_z+c v=g$, giải đa thức $a\lambda^2+b\lambda+c=0$, giữ hai hàm tùy ý theo $s$. Nghiệm kép có thêm hệ số $z$; có thể tìm nghiệm riêng dạng mũ hoặc đa thức.

**Bước 4 — Dùng dữ liệu đúng biến.** Tính $u_x=s_xv_s+z_xv_z$ và $u_y=s_yv_s+z_yv_z$. Nếu dữ liệu ở $s=0$, chỉ biết $F(0),G(0)$ hoặc đạo hàm của chúng; không suy ra toàn bộ các hàm. So sánh hệ số của $e^z$, $z$, $z^2$ để tìm các hằng số tương thích.

**Bước 5 — Kiểm tra tính duy nhất và nghiệm cụ thể.** Khi đường dữ liệu gặp tất cả đặc trưng một cách độc lập, giải hệ cho $F,G$. Khi đường dữ liệu là một đặc trưng, mô tả các hàm còn tùy ý và đưa hai lựa chọn rõ ràng. Cuối cùng thế lại phương trình gốc, không chỉ ODE mới.''',
'elliptic_series': r'''**Mục tiêu.** Đưa phương trình elliptic về dạng đơn giản, rồi tìm nghiệm giải tích từ dữ liệu Cauchy mà bài yêu cầu.

**Bước 1 — Loại hạng hỗn hợp và hạng cấp một do đổi biến.** Tính $\delta<0$, chọn $\xi,\eta$ thực có Jacobian khác $0$. Thay đầy đủ đạo hàm cấp hai; các đạo hàm của tọa độ có thể triệt tiêu với hạng cấp một trong đề. Kết quả thường là $v_{\xi\xi}+v_{\eta\eta}+c v=0$.

**Bước 2 — Chuyển dữ liệu sang đường tọa độ mới.** Nếu đường dữ liệu trở thành $\xi=0$, đặt $v(0,\eta)=f(\eta)$ và tính $v_\xi(0,\eta)=g(\eta)$ từ đạo hàm được cho. Nếu đường là $\eta=\eta_0$, đổi vai trò hai biến. Không lấy nguyên dữ liệu đạo hàm cũ làm dữ liệu mới khi hệ số dây chuyền khác $1$.

**Bước 3 — Khai triển và lập truy hồi.** Viết

$$
v(\xi,\eta)=\sum_{n=0}^{\infty}\frac{\xi^n}{n!}a_n(\eta),\qquad
a_0=f,\quad a_1=g,\quad a_{n+2}=-a_n''-c a_n.
$$

Tính từng $a_2,a_3,\ldots$. Nếu các hệ số sau một bậc đều bằng $0$, chuỗi kết thúc và cho một đa thức chính xác. Nếu không, cần xét hội tụ trong miền dữ liệu giải tích; chuỗi hình thức chưa tự là nghiệm.

**Bước 4 — Đổi ngược và kiểm tra.** Thế $\xi(x,y),\eta(x,y)$ vào nghiệm. Tính đạo hàm hoặc dùng toán tử đã được chứng minh tương đương để kiểm tra PDE, đồng thời kiểm tra từng dữ liệu gốc. Kết luận duy nhất trong lớp nghiệm giải tích trên miền liên thông mà phép đổi biến hợp lệ; dữ liệu Cauchy elliptic nói chung có thể không ổn định, nên không suy ra tồn tại cho dữ liệu tùy ý chỉ từ cách lập chuỗi.''',
}

from intermediate_method_notes import CH2 as _INTERMEDIATE
for _group,_details in _INTERMEDIATE.items():
    NOTES[_group]+=_details

def note_for(item):
    ident=item['id'];n=int(ident.rsplit('_',1)[1])
    if ident.startswith('VD_'):
        group='coordinates' if n in (1,5) else 'canonical' if n in (2,3,4) else 'parabolic' if n==7 else 'hyperbolic'
    else:
        group='coordinates' if n==1 else 'canonical' if n==2 else 'hyperbolic' if n in (3,4,5,11,12,13) else 'elliptic_series' if n in (16,17,18) else 'parabolic'
    base=NOTES[group]
    if ident=='BT_2_3_02':
        base+='\n\n'+r'**Lưu ý riêng của bài.** Các đường $\sin x=0$ hoặc $x=0$ có thể đổi loại hoặc làm phép đổi biến mất khả nghịch. Phân loại tại các đường ấy riêng; dạng chính tắc elliptic chỉ viết trên từng miền mở không chứa chúng.'
    if ident in ('VD_2_2_09','BT_2_3_11'):
        base+='\n\n'+r'**Biến đổi riêng của bài.** Dùng tọa độ cực (hoặc cực sau khi co giãn trục). Khi thu được $r v_{r\theta}-v_\theta=0$, đặt $w=v/r$ thì $w_{r\theta}=0$. Vì vậy $v=rF(\theta)+G(r)$; phải chia nghiệm cho $r$ trước khi lập đẳng thức bốn đỉnh.'
    return base

def latex_note(item):
    text=note_for(item)
    text=re.sub(r'\*\*([^*]+)\*\*',lambda m:r'\textbf{'+m[1]+'}',text)
    chunks=text.split('$$')
    return ''.join(part if n%2==0 else '\n'+r'\['+part+r'\]'+'\n' for n,part in enumerate(chunks))
