"""Kiến thức chi tiết cho Chương 1, dùng chung khi tạo Markdown và PDF."""

NOTES = {
'classification': r'''**Mục tiêu.** Xác định cấp và dạng của phương trình trước khi chọn cách giải. Ở mục này, từ “bậc” trong đề được hiểu theo nghĩa cấp đạo hàm của phương trình.

**Bước 1 — Liệt kê đạo hàm và đếm cấp.** Với $\partial^{i+j}u/\partial x^i\partial y^j$, cấp là $i+j$. Vì vậy $u_x$ cấp 1, $u_{xy}$ cấp 2, $u_{txx}$ cấp 3. Hạng $u$, $e^u$, $\log u$ không chứa đạo hàm, được xem là cấp 0. $(u_y)^2$ là bình phương của một đạo hàm cấp 1, không phải đạo hàm cấp 2. Lấy giá trị lớn nhất trong các cấp vừa liệt kê.

**Bước 2 — Viết rõ phần chứa đạo hàm cấp cao nhất.** Gọi cấp đó là $m$. Tạm xem từng đạo hàm cấp $m$ như một ẩn đại số độc lập. Nếu chúng bị bình phương, nhân với nhau hoặc nằm trong hàm mũ/lượng giác, biểu thức đã cho hoàn toàn phi tuyến. Nếu chúng chỉ xuất hiện tuyến tính, chuyển sang bước 3. Khi khai triển $(f(u))_x$, phải dùng $(f(u))_x=f'(u)u_x$ trước khi phân loại.

**Bước 3 — Xét hệ số và các hạng cấp thấp.** Nếu mọi hạng chứa $u$ và đạo hàm đều tuyến tính, hệ số chỉ phụ thuộc biến độc lập, phương trình tuyến tính. Nếu chỉ phần cấp $m$ tuyến tính, hệ số của phần đó phụ thuộc biến độc lập, còn phần cấp thấp phi tuyến, phương trình nửa tuyến tính. Nếu hệ số phần cấp $m$ phụ thuộc $u$ hoặc đạo hàm cấp thấp, phương trình tựa tuyến tính. Khi ghi kết luận, chỉ rõ hạng nào quyết định phân loại.

**Bước 4 — Xét thuần nhất khi phương trình tuyến tính.** Gom toàn bộ hạng chứa ẩn về một vế, viết $Lu=f(x,y)$. Nếu $f\equiv0$, phương trình thuần nhất; nếu không, không thuần nhất. Ví dụ $u_{xy}=u$ phải viết $u_{xy}-u=0$, nên là thuần nhất.

**Bước 5 — Kiểm tra miền và yêu cầu đề.** $\log u$ đòi hỏi $u>0$ đối với nghiệm thực. Một phép biến đổi như lấy log có thể cho phương trình tương đương trên một miền, nhưng cần phân biệt dạng biểu thức in trong đề và dạng đã biến đổi. Nếu đề chỉ hỏi cấp, dừng sau bước 1 và giải thích đạo hàm quyết định cấp.''',
'direct': r'''**Mục tiêu.** Đưa phương trình về ODE bằng cách giữ cố định các biến không được lấy đạo hàm, hoặc đặt một đạo hàm/hợp thức trung gian.

**Bước 1 — Chọn biến và tham số.** Với $u_x=f(x,y)$, cố định $y$ và tích phân theo $x$. Khi đó “hằng số” tích phân có thể khác nhau ở mỗi $y$, nên phải viết $C(y)$. Với ba biến, tích phân theo $x$ cho một hàm $C(y,z)$.

**Bước 2 — Tích phân đúng số lần.** Chẳng hạn $u_{xx}=f$ cho $u_x=\int f\,dx+A(y)$, rồi $u=\int(\int f\,dx)dx+xA(y)+B(y)$. Với đạo hàm hỗn hợp, có thể đặt $v=u_x$ hoặc $v=yu_y+2u$ nếu PDE chứa đúng $v_x$. Mỗi lần tích phân phải giữ hàm tùy ý theo các biến còn lại.

**Bước 3 — Giải ODE tuyến tính nếu còn hạng chứa ẩn.** Với $u_x+P(x)u=Q(x,y)$, đặt $M(x)=e^{\int P(x)dx}$. Do $M'=PM$, quy tắc đạo hàm tích cho

$$
(Mu)_x=M(u_x+Pu)=MQ,\qquad
u=M^{-1}\left[\int MQ\,dx+C(y)\right].
$$

Ghi rõ $P$, $M$ và cách tính tích phân trong từng bài. Với ODE cấp 2 có hệ số hằng theo biến đang tích phân, thử $e^{\lambda x}$ và giải phương trình đặc trưng; nghiệm kép cần thêm $xe^{\lambda x}$.

**Bước 4 — Xét trường hợp suy biến trước khi chia.** Chia cho $x$, $y$ hoặc $u$ chỉ hợp lệ ở nơi chúng khác 0. Trên đường bị loại, dùng phương trình gốc để tìm ràng buộc. Nếu cần nghiệm trơn qua đường đó, xét giới hạn và đạo hàm của công thức vừa tìm.

**Bước 5 — Dùng dữ liệu và kiểm tra.** Thế điều kiện đầu/biên để xác định các hàm tùy ý, rồi lấy đạo hàm của nghiệm và thay lại phương trình. Nêu rõ miền và độ trơn cần thiết. Nếu chỉ tìm nghiệm dạng mũ, đó là một họ nghiệm thử; không tự gọi là toàn bộ nghiệm tổng quát.''',
'exponential': r'''**Mục tiêu.** Tìm nghiệm dạng mũ cho PDE tuyến tính có hệ số hằng, theo dạng thử mà đề yêu cầu.

**Bước 1 — Đặt đủ các biến trong số mũ.** Hai biến dùng $u=e^{rx+sy}$; ba biến dùng $u=e^{rx+sy+tz}$. Các tham số $r,s,t$ cần được xác định, không phải biến độc lập.

**Bước 2 — Tính các đạo hàm.** Ta có $u_x=ru$, $u_y=su$, $u_{xx}=r^2u$, $u_{xy}=rsu$, $u_{xyz}=rst\,u$. Mỗi lần lấy đạo hàm tương ứng với nhân thêm tham số của biến ấy.

**Bước 3 — Thế và giải phương trình đại số.** Vì hàm mũ không bằng 0, chia PDE cho $u$ để thu được điều kiện theo tham số. Giải hoặc tham số hóa điều kiện này. Phân biệt tham số thực và phức khi phương trình đại số không có nghiệm thực khác 0.

**Bước 4 — Kiểm tra và hiểu phạm vi kết quả.** Thế một bộ tham số cụ thể để kiểm tra. Với phương trình tuyến tính thuần nhất, tổng hữu hạn các nghiệm cũng là nghiệm. Họ nghiệm mũ chưa nhất thiết mô tả toàn bộ nghiệm; nếu muốn nghiệm tổng quát phải dùng thêm đặc trưng hoặc phương pháp phù hợp.''',
'linear_char': r'''**Mục tiêu.** Với $A(x,y)u_x+B(x,y)u_y+C(x,y)u=R(x,y)$, tìm các đường mà trên đó PDE trở thành một ODE. Dùng chữ $R$ cho vế phải để không nhầm với hàm tùy ý $F$.

**Bước 1 — Đọc các hệ số và lập hệ đặc trưng.** Đặt $U(s)=u(X(s),Y(s))$. Quy tắc dây chuyền cho $U'=u_xX'+u_yY'$. Chọn $X'=A$, $Y'=B$, khi đó

$$
X'=A(X,Y),\qquad Y'=B(X,Y),\qquad U'+C(X,Y)U=R(X,Y).
$$

Nếu $A\ne0$, có thể dùng $x$ làm tham số: $dy/dx=B/A$, $du/dx+(C/A)u=R/A$. Nếu $A=0$, chọn biến khác hoặc giữ hệ theo $s$; không chia cho hệ số bằng 0.

**Bước 2 — Tìm bất biến để phân biệt các đặc trưng.** Tích phân hai phương trình đầu để tìm $\rho(X,Y)$ không đổi. Kiểm tra $A\rho_x+B\rho_y=0$. Hệ số hằng cho $\rho=Bx-Ay$. Ví dụ $X'=X,Y'=-Y$ cho $(XY)'=0$; $X'=-Y,Y'=X$ cho $(X^2+Y^2)'=0$. Khi đặc trưng là vòng kín, cần kiểm tra nghiệm sau một vòng trở về cùng giá trị.

**Bước 3 — Giải ODE của ẩn trên từng đường.** Đặt $M(s)=\exp(\int C(X(s),Y(s))ds)$. Nhân phương trình của $U$ với $M$:

$$
(MU)'=MR,\qquad
U(s)=M(s)^{-1}\left[K+\int M(s)R(X(s),Y(s))ds\right].
$$

$K$ hằng trên một đường, nhưng thay đổi giữa các đường, nên viết $K=F(\rho)$. Nếu tìm được nghiệm riêng $u_p$, có thể giải phương trình thuần nhất cho $u-u_p$ để giảm tính toán. Nếu đổi biến $(\rho,z)$, phải tính Jacobian và dùng quy tắc dây chuyền để thấy PDE chỉ còn đạo hàm theo $z$.

**Bước 4 — Thế dữ liệu và tìm hàm tùy ý.** Với đường dữ liệu $(x_0(r),y_0(r))$, $u=h(r)$, thế vào nghiệm tổng quát để thu được $F(\rho_0(r))=H(r)$, trong đó $\rho_0=\rho(x_0,y_0)$. Nếu $\rho_0$ khả nghịch, đặt $r=\rho_0^{-1}(z)$ rồi viết $F(z)=H(\rho_0^{-1}(z))$. Nếu hai giá trị $r_1,r_2$ có cùng $\rho_0$, phải có $H(r_1)=H(r_2)$. Nếu đường dữ liệu chính là đặc trưng, dữ liệu phải thỏa ODE trên đường đó và thường không xác định hết $F$.

**Bước 5 — Xác định miền tồn tại và duy nhất.** Điều kiện không đặc trưng là $x_0'B-y_0'A\ne0$ trên đường dữ liệu. Nó cho khả nghịch cục bộ dưới giả thiết trơn thích hợp; không tự cho duy nhất trên cả mặt phẳng. Chỉ những đặc trưng gặp dữ liệu mới được xác định. Tại gốc, trục hoặc đường hệ số suy biến, kiểm tra riêng và ghép các biểu thức đủ trơn.

**Bước 6 — Kiểm tra kết quả.** Tính $u_x,u_y$ bằng quy tắc dây chuyền, thay vào $Au_x+Bu_y+Cu$ và kiểm tra bằng $R$. Sau đó thế lại điều kiện đầu/biên. Nêu rõ nếu chỉ có nghiệm cục bộ, nghiệm từng miền hoặc không có nghiệm trong lớp trơn yêu cầu.''',
'quasi_char': r'''**Mục tiêu.** Với $u_t+a(x,t,u)u_x=b(x,t,u)$, đặc trưng phụ thuộc cả giá trị nghiệm nên phải giải đồng thời đường đi và ẩn.

**Bước 1 — Gắn nhãn điểm xuất phát.** Gọi $\xi$ là tọa độ ở $t=0$, đặt $X(0;\xi)=\xi$, $U(0;\xi)=f(\xi)$. Dọc đường, $U(t;\xi)=u(X(t;\xi),t)$.

**Bước 2 — Lập và giải hệ.** Quy tắc dây chuyền cho

$$
X'=a(X,t,U),\qquad U'=b(X,t,U).
$$

Nếu ODE của $U$ giải được trước, thế kết quả vào $X'$ rồi tích phân từ 0 đến $t$, giữ đúng điều kiện $X(0)=\xi$. Chẳng hạn $U'=\lambda U$ cho $U=e^{\lambda t}f(\xi)$. Nếu chia cho $U$ hoặc $U+1$, xét riêng các nghiệm hằng bị loại.

**Bước 3 — Khử nhãn $\xi$.** Giải $x=X(t;\xi)$ để tìm $\xi=\xi(x,t)$ rồi thay vào $u=U(t;\xi)$. Khi không khử được bằng công thức đơn giản, ghi nghiệm tham số và phương trình xác định $\xi$.

**Bước 4 — Tìm miền còn nghiệm cổ điển.** Tính $X_\xi$. Khi $X_\xi\ne0$, có thể khử nhãn cục bộ. Vì $u_x=U_\xi/X_\xi$, mẫu số tiến về 0 có thể gây đạo hàm vô hạn. Với $u_t+a(u)u_x=0$, ta có $X=\xi+a(f(\xi))t$, $X_\xi=1+a'(f(\xi))f'(\xi)t$. Tìm thời điểm dương đầu tiên mẫu này bằng 0.

**Bước 5 — Nếu dữ liệu có bước nhảy.** Viết $F'(u)=a(u)$ để có dạng bảo toàn $u_t+(F(u))_x=0$. Đặc trưng hội tụ dẫn đến sốc, tách xa dẫn đến quạt giãn; dùng Rankine–Hugoniot và điều kiện entropy như phần kiến thức về sốc. Giá trị ở chỗ đặc trưng giao nhau không được chọn tùy ý.

**Bước 6 — Thử lại.** Kiểm tra phương trình trong vùng trơn, dữ liệu ở $t=0$, miền khả nghịch và mọi đường ghép. Với dữ liệu chỉ trên một đoạn, giữ điều kiện nhãn $\xi$ nằm trong đoạn đó.''',
'charpit': r'''**Mục tiêu.** Giải PDE cấp 1 phi tuyến $F(x,y,u,p,q)=0$, với $p=u_x,q=u_y$. Chọn $s$ để gắn nhãn đường dữ liệu, $\tau$ là tham số chạy dọc đặc trưng; hai tham số này có vai trò khác nhau.

**Bước 1 — Viết đúng $F$ và tham số hóa dữ liệu.** Chuyển PDE về một vế, giữ mọi hệ số chứa $x,y,u$. Viết $X(s,0)=x_0(s)$, $Y(s,0)=y_0(s)$, $U(s,0)=h(s)$. Đạo hàm điều kiện theo $s$ cho

$$
p_0x_0'(s)+q_0y_0'(s)=h'(s),\qquad
F(x_0,y_0,h,p_0,q_0)=0.
$$

Giải hai phương trình này tìm tất cả nhánh thực $(p_0,q_0)$. Trên $y=0$, $p_0=h'$; trên $x=0$, $q_0=h'$; trên $y=x$, $p_0+q_0=h'$. Điều kiện dưới căn phải không âm. Các nhánh khác nhau có thể cho các nghiệm khác nhau cùng dữ liệu.

**Bước 2 — Kiểm tra không đặc trưng.** Tính $J_0=x_0'F_q-y_0'F_p$ ở dữ liệu của từng nhánh. Khi $J_0\ne0$ và các hàm đủ trơn, phép chuyển từ $(s,\tau)$ sang $(x,y)$ khả nghịch cục bộ. Khi $J_0=0$, cần xét riêng; không kết luận ngay vô nghiệm hoặc duy nhất.

**Bước 3 — Tính các đạo hàm riêng của $F$ rồi lập hệ Charpit.** Khi tính $F_x,F_y,F_u,F_p,F_q$, tạm coi năm đối số độc lập. Hệ là

$$
\begin{aligned}
X_\tau&=F_p,&Y_\tau&=F_q,&U_\tau&=pF_p+qF_q,\\
p_\tau&=-F_x-pF_u,&q_\tau&=-F_y-qF_u.
\end{aligned}
$$

Trong bài cụ thể phải thay các đạo hàm của $F$ vào hệ. Ví dụ $F=pq-1$ cho $X_\tau=q,Y_\tau=p,U_\tau=2,p_\tau=q_\tau=0$.

**Bước 4 — Tích phân hệ với điều kiện ban đầu.** Tìm phương trình giải được trước: $p'=0$, $q'=0$, hoặc tổ hợp như $(X-p)'=0$. Thế chúng vào phương trình còn lại. Nếu hệ tuyến tính $Z'=MZ$, dùng $Z=e^{\tau M}Z_0$; để tính cụ thể, tìm các tổ hợp tách hệ hoặc quan hệ $M^2, M^3$ giúp rút gọn chuỗi mũ. Ghi các phép tích phân và hằng số được dữ liệu xác định.

**Bước 5 — Khử tham số hoặc trình bày nghiệm tham số đã giải.** Từ $X(s,\tau),Y(s,\tau)$ tìm $s,\tau$ theo $x,y$ rồi thay vào $U$. Nếu giữ dạng tham số, phải có công thức $X,Y,U$ đã tích phân và miền $\det\partial(X,Y)/\partial(s,\tau)\ne0$; chỉ ghi hệ ODE chưa phải lời giải hoàn tất.

**Bước 6 — Dùng phép đổi ẩn khi thuận lợi.** Gần dữ liệu $u>0$, $p^2+q^2=u$ đổi $v=2\sqrt u$ cho $|\nabla v|^2=1$; $p^2+q^2=u^2$ đổi $v=\log u$ cũng cho eikonal. Phải tính $v_x,v_y$ để chứng minh phép đổi, đổi cả dữ liệu và giữ điều kiện dấu. Với dữ liệu hằng trên vòng tròn, đạo hàm tiếp tuyến bằng 0 nên gradient pháp tuyến có hai lựa chọn dấu.

**Bước 7 — Kiểm tra từng nhánh và miền.** Tính $p,q$ của công thức cuối, thế vào PDE và dữ liệu. Phân biệt một nghiệm đã tìm được, các nhánh không đặc trưng cục bộ và toàn bộ nghiệm toàn cục. Giữ điều kiện của nhãn dữ liệu nếu đề chỉ cho $0\le s\le1$; kiểm tra gốc, điểm căn bằng 0 và đường làm mẫu số bằng 0.''',
'shock': r'''**Mục tiêu.** Với dữ liệu gián đoạn hoặc khi đặc trưng giao nhau, tìm nghiệm yếu thỏa entropy của luật bảo toàn $u_t+(F(u))_x=0$.

**Bước 1 — Xác định thông lượng và đặc trưng.** Nếu PDE là $u_t+a(u)u_x=0$, tích phân $F'=a$. Trong vùng trơn, $u=u_0(\xi)$ và $x=\xi+F'(u_0(\xi))t$. Tính riêng tốc độ cho mỗi đoạn dữ liệu. Burgers dùng $F=u^2/2$; $u_t+u^2u_x=0$ dùng $F=u^3/3$.

**Bước 2 — Nhận diện sóng tại mỗi bước nhảy.** Gọi $u_L,u_R$ là giá trị trái, phải. So sánh $F'(u_L)$ và $F'(u_R)$. Với $F$ lồi trên khoảng trạng thái, $u_L>u_R$ tạo sốc, $u_L<u_R$ tạo quạt giãn; với $F$ lõm, thứ tự trạng thái đảo lại. Nếu độ lồi đổi dấu, phải xét thêm cấu trúc entropy, không dùng quy tắc lồi trên toàn khoảng.

**Bước 3 — Tính đường sốc từ bảo toàn.** Với $x=s(t)$,

$$
s'(t)=\frac{F(u_L)-F(u_R)}{u_L-u_R}.
$$

Nếu hai trạng thái hằng, tốc độ $\sigma$ hằng, nên $s=x_0+\sigma t$. Kiểm tra entropy bằng $F'(u_R)<\sigma<F'(u_L)$ đối với sốc nén có hai trạng thái phân biệt trong các bài này. Giá trị ngay trên đường sốc không ảnh hưởng nghiệm yếu.

**Bước 4 — Tính quạt giãn.** Từ $(x_0,0)$, đặt $z=(x-x_0)/t$, $u=V(z)$. Thế PDE cho $(F'(V)-z)V'=0$. Trong nhánh biến thiên, $F'(V)=z$, nên giải phương trình này tìm $V$. Mép quạt là $x=x_0+F'(u_L)t$ và $x=x_0+F'(u_R)t$, theo thứ tự tốc độ tăng; ghép liên tục với hai trạng thái ngoài. Chọn căn đúng dấu theo khoảng giá trị của dữ liệu.

**Bước 5 — Tìm mọi thời điểm tương tác.** Giải phương trình giao của hai sốc, sốc với mép quạt, hoặc quạt với quạt. Trước thời điểm gặp, ghép các sóng riêng. Sau khi gặp, tính lại hai trạng thái sát đường sốc. Nếu một phía nằm trong quạt, trạng thái đó phụ thuộc $s(t)$ và $t$, nên Rankine–Hugoniot trở thành ODE mới. Dùng $s(t_*)=x_*$ để tìm hằng số, rồi tiếp tục tìm lần tương tác sau.

**Bước 6 — Viết nghiệm theo từng khoảng thời gian.** Với mỗi khoảng, ghi rõ các miền $x$, thứ tự đường phân cách và công thức của $u$. Trên nửa trục, kiểm tra chiều truyền từ biên vào miền và thế điều kiện biên. Với dữ liệu trơn từng đoạn, tính $\partial x/\partial\xi$ để tìm thời điểm đầu tiên mất nghiệm cổ điển.

**Bước 7 — Kiểm tra.** Trong mỗi vùng trơn, thay vào PDE. Trên mỗi sốc, kiểm tra Rankine–Hugoniot và entropy; ở mép quạt, kiểm tra liên tục. Đối chiếu dữ liệu khi $t\downarrow0$, sự liên tục của vị trí sóng qua thời điểm gặp và khối lượng nếu dữ liệu có giá hữu hạn. Nhân PDE với một hàm của $u$ chỉ giữ tương đương cho nghiệm trơn; không tự áp luật đã nhân để tính cùng đường sốc.'''
}

from intermediate_method_notes import CH1 as _INTERMEDIATE
for _group,_details in _INTERMEDIATE.items():
    NOTES[_group]+=_details

def key(item):
    section = item['section']
    if item['id'] == 'VD_1_3_1_2_01':
        return 'superposition'
    if section == '1.2.3' and item['number'] == 3:
        return 'exponential'
    if section == '1.2.3' and item['number'] == 4:
        return 'canonical'
    if section == '1.2.2.1' or section == '1.2.3' and item['number'] <= 2:
        return 'classification'
    if section.startswith('1.2'):
        return 'direct'
    if section.startswith('1.3'):
        return 'linear_char'
    if section == '1.4.2' and item['number'] == 3 or section == '1.4.3':
        return 'shock'
    if section.startswith('1.4'):
        return 'quasi_char'
    if section.startswith('1.5'):
        return 'charpit'
    return 'shock'

NOTES['canonical'] = r'''**Mục tiêu của bài.** Đưa $au_{xx}+bu_{xy}+cu_{yy}=0$ với $\Delta=b^2-4ac>0$ về phương trình có thể tích phân. Ở đây hệ số hỗn hợp là $b$, không phải $2b$.

**Bước 1 — Tìm hướng đặc trưng.** Thử tọa độ $\xi=y-mx$. Hệ số của $v_{\xi\xi}$ sau đổi biến là $am^2-bm+c$. Giải $am^2-bm+c=0$; nếu $a\ne0$, $\Delta>0$ cho hai nghiệm thực phân biệt $m_1,m_2$. Nếu $a=0$, xét trực tiếp vì khi đó $b\ne0$.

**Bước 2 — Đổi biến và kiểm tra Jacobian.** Đặt $\xi=y-m_1x$, $\eta=y-m_2x$, $u=v(\xi,\eta)$. Jacobian là $m_2-m_1\ne0$. Viết $\partial_x=-m_1\partial_\xi-m_2\partial_\eta$, $\partial_y=\partial_\xi+\partial_\eta$, rồi áp dụng hai lần để tính $u_{xx},u_{xy},u_{yy}$.

**Bước 3 — Thế toàn bộ đạo hàm vào PDE.** Hai hệ số thuần bằng 0 theo phương trình của $m_i$. Hệ số hỗn hợp khác 0, nên chia được để có $v_{\xi\eta}=0$. Với đổi biến không tuyến tính trong bài khác, phải giữ cả các hạng đạo hàm cấp 1 phát sinh.

**Bước 4 — Tích phân hai lần.** $\partial_\eta(v_\xi)=0$ cho $v_\xi=A(\xi)$; tích phân theo $\xi$ cho $v=F(\xi)+G(\eta)$. Đổi về $x,y$ và thế lại PDE để kiểm tra. Các hàm $F,G$ cần đủ trơn, thường $C^2$.'''

def note_for(item):
    value = NOTES[key(item)]
    if item['id'] == 'BT_1_2_3_05':
        value += r'''

**Bổ sung cho ý tổng bình phương đạo hàm.** Với nghiệm thực, $u_x^2+u_y^2=0$ buộc từng đạo hàm bằng 0, nên $u$ hằng trên mỗi thành phần liên thông. Nếu vế phải là $k<0$, vô nghiệm thực; nếu $k>0$, đây là eikonal $|\nabla u|^2=k$. Nghiệm affine $u=ax+by+c$ cần $a^2+b^2=k$, nhưng chỉ là một họ. Muốn dựng nghiệm cục bộ từ dữ liệu trên đường $\gamma(s)$, chọn gradient ban đầu $P(s)$ thỏa $|P|^2=k$, $P\cdot\gamma'=h'$. Đặc trưng cho $X=\gamma(s)+2\tau P(s)$, $U=h(s)+2k\tau$; chỉ khử được tham số nơi Jacobian khác 0. Cách này được áp dụng riêng ở ý (d).'''
    return value

NOTES['superposition'] = r'''**Mục tiêu.** Chứng minh tính chồng chất của các nghiệm phương trình tuyến tính thuần nhất.

**Bước 1 — Viết toán tử.** Gọi $L$ là biểu thức lấy đạo hàm và nhân hệ số của PDE. Chẳng hạn $L=a\partial_x+b\partial_t$. Tuyến tính nghĩa là $L(c_1u_1+c_2u_2)=c_1Lu_1+c_2Lu_2$ với $c_1,c_2$ hằng.

**Bước 2 — Tính đạo hàm của tổng.** Dùng $(c_1u_1+c_2u_2)_x=c_1(u_1)_x+c_2(u_2)_x$ và tương tự theo các biến khác, rồi nhóm thành $c_1Lu_1+c_2Lu_2$. Không cho các hệ số $c_i$ phụ thuộc vị trí, vì khi đó có thêm đạo hàm của hệ số.

**Bước 3 — Thế giả thiết nghiệm.** Nếu $Lu_i=0$, tổng có $L=0$ nên cũng là nghiệm. Nếu các nghiệm có cùng dữ liệu biên, phải kiểm tra riêng dữ liệu của tổng; tính chồng chất của PDE chưa tự giữ nguyên dữ liệu.

**Bước 4 — Mở rộng cho phương trình có nguồn.** Nếu $Lu_i=f$, hiệu $u_1-u_2$ thỏa thuần nhất, nhưng tổng có nguồn $2f$. Để giải $Lu=f$, dùng một nghiệm riêng $u_p$ cộng mọi nghiệm thuần nhất $u_h$.'''

def latex_note(item):
    import re
    value = note_for(item)
    value = re.sub(r'\*\*([^*]+)\*\*', lambda m: r'\textbf{' + m[1] + '}', value)
    chunks = value.split('$$')
    return ''.join(chunk if n % 2 == 0 else '\\[' + chunk + '\\]' for n, chunk in enumerate(chunks))
