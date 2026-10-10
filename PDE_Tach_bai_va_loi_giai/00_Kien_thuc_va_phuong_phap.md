# Kiến thức và phương pháp dùng trong lời giải

## Chương 1 — Hướng dẫn chi tiết

**Mục tiêu.** Xác định cấp và dạng của phương trình trước khi chọn cách giải. Ở mục này, từ “bậc” trong đề được hiểu theo nghĩa cấp đạo hàm của phương trình.

**Bước 1 — Liệt kê đạo hàm và đếm cấp.** Với $\partial^{i+j}u/\partial x^i\partial y^j$, cấp là $i+j$. Vì vậy $u_x$ cấp 1, $u_{xy}$ cấp 2, $u_{txx}$ cấp 3. Hạng $u$, $e^u$, $\log u$ không chứa đạo hàm, được xem là cấp 0. $(u_y)^2$ là bình phương của một đạo hàm cấp 1, không phải đạo hàm cấp 2. Lấy giá trị lớn nhất trong các cấp vừa liệt kê.

**Bước 2 — Viết rõ phần chứa đạo hàm cấp cao nhất.** Gọi cấp đó là $m$. Tạm xem từng đạo hàm cấp $m$ như một ẩn đại số độc lập. Nếu chúng bị bình phương, nhân với nhau hoặc nằm trong hàm mũ/lượng giác, biểu thức đã cho hoàn toàn phi tuyến. Nếu chúng chỉ xuất hiện tuyến tính, chuyển sang bước 3. Khi khai triển $(f(u))_x$, phải dùng $(f(u))_x=f'(u)u_x$ trước khi phân loại.

**Bước 3 — Xét hệ số và các hạng cấp thấp.** Nếu mọi hạng chứa $u$ và đạo hàm đều tuyến tính, hệ số chỉ phụ thuộc biến độc lập, phương trình tuyến tính. Nếu chỉ phần cấp $m$ tuyến tính, hệ số của phần đó phụ thuộc biến độc lập, còn phần cấp thấp phi tuyến, phương trình nửa tuyến tính. Nếu hệ số phần cấp $m$ phụ thuộc $u$ hoặc đạo hàm cấp thấp, phương trình tựa tuyến tính. Khi ghi kết luận, chỉ rõ hạng nào quyết định phân loại.

**Bước 4 — Xét thuần nhất khi phương trình tuyến tính.** Gom toàn bộ hạng chứa ẩn về một vế, viết $Lu=f(x,y)$. Nếu $f\equiv0$, phương trình thuần nhất; nếu không, không thuần nhất. Ví dụ $u_{xy}=u$ phải viết $u_{xy}-u=0$, nên là thuần nhất.

**Bước 5 — Kiểm tra miền và yêu cầu đề.** $\log u$ đòi hỏi $u>0$ đối với nghiệm thực. Một phép biến đổi như lấy log có thể cho phương trình tương đương trên một miền, nhưng cần phân biệt dạng biểu thức in trong đề và dạng đã biến đổi. Nếu đề chỉ hỏi cấp, dừng sau bước 1 và giải thích đạo hàm quyết định cấp.

---

**Mục tiêu.** Đưa phương trình về ODE bằng cách giữ cố định các biến không được lấy đạo hàm, hoặc đặt một đạo hàm/hợp thức trung gian.

**Bước 1 — Chọn biến và tham số.** Với $u_x=f(x,y)$, cố định $y$ và tích phân theo $x$. Khi đó “hằng số” tích phân có thể khác nhau ở mỗi $y$, nên phải viết $C(y)$. Với ba biến, tích phân theo $x$ cho một hàm $C(y,z)$.

**Bước 2 — Tích phân đúng số lần.** Chẳng hạn $u_{xx}=f$ cho $u_x=\int f\,dx+A(y)$, rồi $u=\int(\int f\,dx)dx+xA(y)+B(y)$. Với đạo hàm hỗn hợp, có thể đặt $v=u_x$ hoặc $v=yu_y+2u$ nếu PDE chứa đúng $v_x$. Mỗi lần tích phân phải giữ hàm tùy ý theo các biến còn lại.

**Bước 3 — Giải ODE tuyến tính nếu còn hạng chứa ẩn.** Với $u_x+P(x)u=Q(x,y)$, đặt $M(x)=e^{\int P(x)dx}$. Do $M'=PM$, quy tắc đạo hàm tích cho

$$
(Mu)_x=M(u_x+Pu)=MQ,\qquad
u=M^{-1}\left[\int MQ\,dx+C(y)\right].
$$

Ghi rõ $P$, $M$ và cách tính tích phân trong từng bài. Với ODE cấp 2 có hệ số hằng theo biến đang tích phân, thử $e^{\lambda x}$ và giải phương trình đặc trưng; nghiệm kép cần thêm $xe^{\lambda x}$.

**Bước 4 — Xét trường hợp suy biến trước khi chia.** Chia cho $x$, $y$ hoặc $u$ chỉ hợp lệ ở nơi chúng khác 0. Trên đường bị loại, dùng phương trình gốc để tìm ràng buộc. Nếu cần nghiệm trơn qua đường đó, xét giới hạn và đạo hàm của công thức vừa tìm.

**Bước 5 — Dùng dữ liệu và kiểm tra.** Thế điều kiện đầu/biên để xác định các hàm tùy ý, rồi lấy đạo hàm của nghiệm và thay lại phương trình. Nêu rõ miền và độ trơn cần thiết. Nếu chỉ tìm nghiệm dạng mũ, đó là một họ nghiệm thử; không tự gọi là toàn bộ nghiệm tổng quát.

---

**Mục tiêu.** Tìm nghiệm dạng mũ cho PDE tuyến tính có hệ số hằng, theo dạng thử mà đề yêu cầu.

**Bước 1 — Đặt đủ các biến trong số mũ.** Hai biến dùng $u=e^{rx+sy}$; ba biến dùng $u=e^{rx+sy+tz}$. Các tham số $r,s,t$ cần được xác định, không phải biến độc lập.

**Bước 2 — Tính các đạo hàm.** Ta có $u_x=ru$, $u_y=su$, $u_{xx}=r^2u$, $u_{xy}=rsu$, $u_{xyz}=rst\,u$. Mỗi lần lấy đạo hàm tương ứng với nhân thêm tham số của biến ấy.

**Bước 3 — Thế và giải phương trình đại số.** Vì hàm mũ không bằng 0, chia PDE cho $u$ để thu được điều kiện theo tham số. Giải hoặc tham số hóa điều kiện này. Phân biệt tham số thực và phức khi phương trình đại số không có nghiệm thực khác 0.

**Bước 4 — Kiểm tra và hiểu phạm vi kết quả.** Thế một bộ tham số cụ thể để kiểm tra. Với phương trình tuyến tính thuần nhất, tổng hữu hạn các nghiệm cũng là nghiệm. Họ nghiệm mũ chưa nhất thiết mô tả toàn bộ nghiệm; nếu muốn nghiệm tổng quát phải dùng thêm đặc trưng hoặc phương pháp phù hợp.

---

**Mục tiêu.** Với $A(x,y)u_x+B(x,y)u_y+C(x,y)u=R(x,y)$, tìm các đường mà trên đó PDE trở thành một ODE. Dùng chữ $R$ cho vế phải để không nhầm với hàm tùy ý $F$.

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

**Bước 6 — Kiểm tra kết quả.** Tính $u_x,u_y$ bằng quy tắc dây chuyền, thay vào $Au_x+Bu_y+Cu$ và kiểm tra bằng $R$. Sau đó thế lại điều kiện đầu/biên. Nêu rõ nếu chỉ có nghiệm cục bộ, nghiệm từng miền hoặc không có nghiệm trong lớp trơn yêu cầu.

**Chi tiết bước tích phân ODE.** Sau khi tìm bất biến $\rho$, viết $U'+P(s,\rho)U=Q(s,\rho)$. Chọn $M=\exp(\int_{s_0}^{s}P(r,\rho)dr)$; tính $M'=PM$, nên $MU'+M'U=MQ$. Tích phân từ $s_0$: $M(s)U(s)-U(s_0)=\int_{s_0}^sM(r)Q(r)dr$. Hằng số $U(s_0)$ phụ thuộc $\rho$; thay dữ liệu để tìm nó rồi mới đổi về tọa độ gốc.

---

**Mục tiêu.** Với $u_t+a(x,t,u)u_x=b(x,t,u)$, đặc trưng phụ thuộc cả giá trị nghiệm nên phải giải đồng thời đường đi và ẩn.

**Bước 1 — Gắn nhãn điểm xuất phát.** Gọi $\xi$ là tọa độ ở $t=0$, đặt $X(0;\xi)=\xi$, $U(0;\xi)=f(\xi)$. Dọc đường, $U(t;\xi)=u(X(t;\xi),t)$.

**Bước 2 — Lập và giải hệ.** Quy tắc dây chuyền cho

$$
X'=a(X,t,U),\qquad U'=b(X,t,U).
$$

Nếu ODE của $U$ giải được trước, thế kết quả vào $X'$ rồi tích phân từ 0 đến $t$, giữ đúng điều kiện $X(0)=\xi$. Chẳng hạn $U'=\lambda U$ cho $U=e^{\lambda t}f(\xi)$. Nếu chia cho $U$ hoặc $U+1$, xét riêng các nghiệm hằng bị loại.

**Bước 3 — Khử nhãn $\xi$.** Giải $x=X(t;\xi)$ để tìm $\xi=\xi(x,t)$ rồi thay vào $u=U(t;\xi)$. Khi không khử được bằng công thức đơn giản, ghi nghiệm tham số và phương trình xác định $\xi$.

**Bước 4 — Tìm miền còn nghiệm cổ điển.** Tính $X_\xi$. Khi $X_\xi\ne0$, có thể khử nhãn cục bộ. Vì $u_x=U_\xi/X_\xi$, mẫu số tiến về 0 có thể gây đạo hàm vô hạn. Với $u_t+a(u)u_x=0$, ta có $X=\xi+a(f(\xi))t$, $X_\xi=1+a'(f(\xi))f'(\xi)t$. Tìm thời điểm dương đầu tiên mẫu này bằng 0.

**Bước 5 — Nếu dữ liệu có bước nhảy.** Viết $F'(u)=a(u)$ để có dạng bảo toàn $u_t+(F(u))_x=0$. Đặc trưng hội tụ dẫn đến sốc, tách xa dẫn đến quạt giãn; dùng Rankine–Hugoniot và điều kiện entropy như phần kiến thức về sốc. Giá trị ở chỗ đặc trưng giao nhau không được chọn tùy ý.

**Bước 6 — Thử lại.** Kiểm tra phương trình trong vùng trơn, dữ liệu ở $t=0$, miền khả nghịch và mọi đường ghép. Với dữ liệu chỉ trên một đoạn, giữ điều kiện nhãn $\xi$ nằm trong đoạn đó.

---

**Mục tiêu.** Giải PDE cấp 1 phi tuyến $F(x,y,u,p,q)=0$, với $p=u_x,q=u_y$. Chọn $s$ để gắn nhãn đường dữ liệu, $\tau$ là tham số chạy dọc đặc trưng; hai tham số này có vai trò khác nhau.

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

**Bước 7 — Kiểm tra từng nhánh và miền.** Tính $p,q$ của công thức cuối, thế vào PDE và dữ liệu. Phân biệt một nghiệm đã tìm được, các nhánh không đặc trưng cục bộ và toàn bộ nghiệm toàn cục. Giữ điều kiện của nhãn dữ liệu nếu đề chỉ cho $0\le s\le1$; kiểm tra gốc, điểm căn bằng 0 và đường làm mẫu số bằng 0.

**Chi tiết tích phân và khử sau khi lập hệ.** Trong lúc tích phân theo $\tau$, nhãn $s$ và các gradient ban đầu $p_0(s),q_0(s)$ được giữ cố định. Với $p'=cp$, viết $p=p_0e^{c\tau}$; nếu $X'=dp$ thì $X=x_0+dp_0(e^{c\tau}-1)/c$ khi $c\ne0$, hoặc $X=x_0+dp_0\tau$ khi $c=0$. Với $Y'+cY=R(\tau)$, nhân $e^{c\tau}$ cho $(e^{c\tau}Y)'=e^{c\tau}R$, rồi dùng $Y(0)$ để xác định hằng số. Khử từ hai phương trình $x=X(s,\tau),y=Y(s,\tau)$; ghi rõ tổ hợp nào loại $\tau$ hoặc $s$. Nếu chỉ cho nghiệm tham số, vẫn phải có các tích phân đã tính và điều kiện Jacobian để khử cục bộ.

---

**Mục tiêu.** Với dữ liệu gián đoạn hoặc khi đặc trưng giao nhau, tìm nghiệm yếu thỏa entropy của luật bảo toàn $u_t+(F(u))_x=0$.

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

**Bước 7 — Kiểm tra.** Trong mỗi vùng trơn, thay vào PDE. Trên mỗi sốc, kiểm tra Rankine–Hugoniot và entropy; ở mép quạt, kiểm tra liên tục. Đối chiếu dữ liệu khi $t\downarrow0$, sự liên tục của vị trí sóng qua thời điểm gặp và khối lượng nếu dữ liệu có giá hữu hạn. Nhân PDE với một hàm của $u$ chỉ giữ tương đương cho nghiệm trơn; không tự áp luật đã nhân để tính cùng đường sốc.

**Chi tiết tích phân đường sốc nằm trong quạt.** Nếu $s'=s/(2t)$ và $s(t_*)=x_*>0$, chia cho $s$ rồi tích phân từ $t_*$ đến $t$: $\log(s/x_*)=\frac12\log(t/t_*)$, nên $s=x_*\sqrt{t/t_*}$. Nếu quạt có tâm $x_0$, thay $s$ bằng $s-x_0$ trước khi tách biến. Khi trạng thái sát sốc thay đổi tại lần gặp tiếp theo, lập ODE mới và lấy vị trí tại lần gặp làm dữ liệu; không giữ hằng số của giai đoạn trước.

---

**Mục tiêu của bài.** Đưa $au_{xx}+bu_{xy}+cu_{yy}=0$ với $\Delta=b^2-4ac>0$ về phương trình có thể tích phân. Ở đây hệ số hỗn hợp là $b$, không phải $2b$.

**Bước 1 — Tìm hướng đặc trưng.** Thử tọa độ $\xi=y-mx$. Hệ số của $v_{\xi\xi}$ sau đổi biến là $am^2-bm+c$. Giải $am^2-bm+c=0$; nếu $a\ne0$, $\Delta>0$ cho hai nghiệm thực phân biệt $m_1,m_2$. Nếu $a=0$, xét trực tiếp vì khi đó $b\ne0$.

**Bước 2 — Đổi biến và kiểm tra Jacobian.** Đặt $\xi=y-m_1x$, $\eta=y-m_2x$, $u=v(\xi,\eta)$. Jacobian là $m_2-m_1\ne0$. Viết $\partial_x=-m_1\partial_\xi-m_2\partial_\eta$, $\partial_y=\partial_\xi+\partial_\eta$, rồi áp dụng hai lần để tính $u_{xx},u_{xy},u_{yy}$.

**Bước 3 — Thế toàn bộ đạo hàm vào PDE.** Hai hệ số thuần bằng 0 theo phương trình của $m_i$. Hệ số hỗn hợp khác 0, nên chia được để có $v_{\xi\eta}=0$. Với đổi biến không tuyến tính trong bài khác, phải giữ cả các hạng đạo hàm cấp 1 phát sinh.

**Bước 4 — Tích phân hai lần.** $\partial_\eta(v_\xi)=0$ cho $v_\xi=A(\xi)$; tích phân theo $\xi$ cho $v=F(\xi)+G(\eta)$. Đổi về $x,y$ và thế lại PDE để kiểm tra. Các hàm $F,G$ cần đủ trơn, thường $C^2$.

---

**Mục tiêu.** Chứng minh tính chồng chất của các nghiệm phương trình tuyến tính thuần nhất.

**Bước 1 — Viết toán tử.** Gọi $L$ là biểu thức lấy đạo hàm và nhân hệ số của PDE. Chẳng hạn $L=a\partial_x+b\partial_t$. Tuyến tính nghĩa là $L(c_1u_1+c_2u_2)=c_1Lu_1+c_2Lu_2$ với $c_1,c_2$ hằng.

**Bước 2 — Tính đạo hàm của tổng.** Dùng $(c_1u_1+c_2u_2)_x=c_1(u_1)_x+c_2(u_2)_x$ và tương tự theo các biến khác, rồi nhóm thành $c_1Lu_1+c_2Lu_2$. Không cho các hệ số $c_i$ phụ thuộc vị trí, vì khi đó có thêm đạo hàm của hệ số.

**Bước 3 — Thế giả thiết nghiệm.** Nếu $Lu_i=0$, tổng có $L=0$ nên cũng là nghiệm. Nếu các nghiệm có cùng dữ liệu biên, phải kiểm tra riêng dữ liệu của tổng; tính chồng chất của PDE chưa tự giữ nguyên dữ liệu.

**Bước 4 — Mở rộng cho phương trình có nguồn.** Nếu $Lu_i=f$, hiệu $u_1-u_2$ thỏa thuần nhất, nhưng tổng có nguồn $2f$. Để giải $Lu=f$, dùng một nghiệm riêng $u_p$ cộng mọi nghiệm thuần nhất $u_h$.

## Chương 2 — Hướng dẫn chi tiết

**Mục tiêu.** Tính đạo hàm khi đổi tọa độ rồi thay vào PDE. Đổi tọa độ của điểm và đổi biểu thức của hàm là hai việc cần làm cùng nhau: đặt $q=q(x)$ và $v(q)=u(x(q))$.

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

**Bước 5 — Kiểm tra bằng hàm đơn giản.** Thử $u=1$, $u=x_i$ và $u=x_1^2+x_2^2+x_3^2$. Công thức Laplace phải lần lượt cho $0$, $0$, $6$. Với Hessian biểu diễn trong cơ sở trực chuẩn, đổi lại cơ sở Descartes bằng $H_x=E H_q E^T$, không nhầm Hessian với ma trận chỉ gồm các đạo hàm $v_{q_kq_l}$.

---

**Mục tiêu.** Phân loại và đưa phương trình tuyến tính cấp hai về dạng chính tắc, có giữ đầy đủ các hạng cấp thấp.

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

**Bước 5 — Với ba biến.** Lập ma trận đối xứng $M$ của phần cấp hai; hệ số hỗn hợp được chia đôi. Dùng hoàn thành bình phương để tìm số hướng dương, âm và bằng $0$. Nếu $\xi=T x$, ma trận mới là $TMT^T$. Cho rõ ma trận $T$ và kiểm tra nó khả nghịch; chỉ ghi dấu của dạng toàn phương chưa đủ để thực hiện phép đổi biến.

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

Khi đó $Lu=av_{\xi\xi}+2bv_{\xi\eta}+cv_{\eta\eta}+dv_\xi+ev_\eta+Kv$. Trong lời giải từng ý, thế các số hoặc hàm hệ số vào từng dòng trước khi rút gọn. Với ba biến, tính $TM$ trước, rồi lấy tích vô hướng mỗi hàng của $TM$ với mỗi hàng của $T$ để có $TMT^T$.

---

**Mục tiêu.** Giải phương trình hyperbolic sau khi đã tìm hai tọa độ đặc trưng độc lập.

**Bước 1 — Phân loại, tìm đặc trưng và thay đạo hàm.** Làm đủ các bước của phép đưa về chính tắc. Viết cả phép đổi ngược để biểu diễn vế phải $\widetilde f(\xi,\eta)=f(x(\xi,\eta),y(\xi,\eta))$.

**Bước 2 — Tích phân phương trình chính tắc.** Với $v_{\xi\eta}=g$, giữ biến kia cố định khi tích phân:

$$
v=F(\xi)+G(\eta)+\int_{\xi_0}^{\xi}\int_{\eta_0}^{\eta}g(a,b)\,db\,da.
$$

Nếu tìm được một nghiệm riêng $P(x,y)$ dễ hơn, viết $u=P+F(\xi)+G(\eta)$. Với $v_{\xi\eta}+\alpha v_\eta=0$, đặt $w=v_\eta$, giải $w_\xi+\alpha w=0$ rồi tích phân theo $\eta$; thu được $v=F(\xi)+e^{-\alpha\xi}G(\eta)$.

**Bước 3 — Đổi cả dữ liệu.** Thế tọa độ đường dữ liệu vào $\xi,\eta$, dùng quy tắc dây chuyền cho đạo hàm được cho. Trên đường không đặc trưng, hai dữ liệu thường xác định hai hàm $F,G$. Trên đường đặc trưng, có biến không thay đổi, nên dữ liệu chỉ xác định giá trị hoặc đạo hàm của một hàm tại một điểm; phải tìm điều kiện tương thích và nêu phần tùy ý còn lại.

**Bước 4 — Lập đẳng thức hình bình hành.** Với $v=F(\xi)+G(\eta)$, bốn đỉnh theo hai họ đặc trưng thỏa $v_{11}+v_{22}=v_{12}+v_{21}$. Nếu có số hạng mũ, trước hết nhân trọng số để được tổng hai hàm một biến. Với vế phải $g$, hiệu bốn đỉnh bằng tích phân kép của $g$ trên hình chữ nhật trong tọa độ mới.

**Bước 5 — Xác định miền được dữ liệu quyết định.** Hai đặc trưng đi qua điểm đang xét phải gặp đoạn dữ liệu phù hợp. Với phương trình sóng $v_{tt}=v_{zz}$ trên $z>0$, dữ liệu lúc $t=0$ xác định duy nhất miền $z>t$; ở $0<z<t$, cần thêm dữ liệu biên $z=0$. Với đặc trưng cong, dùng miền trong các tọa độ mới rồi đổi lại.

**Bước 6 — Kiểm tra.** Thế nghiệm vào cả PDE và từng điều kiện. Nếu đề yêu cầu hai nghiệm, chỉ rõ hai lựa chọn khác nhau cho hàm tùy ý và chứng minh phần chênh lệch thỏa phương trình thuần nhất, đồng thời triệt tiêu trên đường dữ liệu.

---

**Mục tiêu.** Tận dụng phần cấp hai có dạng bình phương một đạo hàm theo hướng để giảm PDE thành ODE có tham số.

**Bước 1 — Nhận ra hướng đạo hàm.** Nếu $D=a\partial_x+b\partial_y$ có hệ số hằng, $D^2u=a^2u_{xx}+2ab u_{xy}+b^2u_{yy}$. Với hệ số biến thiên phải dùng

$$
D^2u=a^2u_{xx}+2ab u_{xy}+b^2u_{yy}+(Da)u_x+(Db)u_y.
$$

So sánh cả hạng cấp một trước khi kết luận PDE bằng $D^2u+\lambda Du+\mu u=f$.

**Bước 2 — Tìm bất biến $s$ và biến tiến $z$.** Giải $Ds=0$, chọn $Dz=k\ne0$. Kiểm tra $J=\partial(s,z)/\partial(x,y)\ne0$. Khi $k$ hằng, $D=k\partial_z$; PDE trở thành ODE theo $z$, trong đó $s$ là tham số. Nếu còn $v_s$, phải giữ lại, chỉ các trường hợp nó triệt tiêu mới giải trực tiếp như ODE.

**Bước 3 — Giải ODE.** Với $v_{zz}=g(s,z)$, tích phân hai lần cho $v=zF(s)+G(s)+\int_{z_0}^z(z-t)g(s,t)dt$. Với $a v_{zz}+b v_z+c v=g$, giải đa thức $a\lambda^2+b\lambda+c=0$, giữ hai hàm tùy ý theo $s$. Nghiệm kép có thêm hệ số $z$; có thể tìm nghiệm riêng dạng mũ hoặc đa thức.

**Bước 4 — Dùng dữ liệu đúng biến.** Tính $u_x=s_xv_s+z_xv_z$ và $u_y=s_yv_s+z_yv_z$. Nếu dữ liệu ở $s=0$, chỉ biết $F(0),G(0)$ hoặc đạo hàm của chúng; không suy ra toàn bộ các hàm. So sánh hệ số của $e^z$, $z$, $z^2$ để tìm các hằng số tương thích.

**Bước 5 — Kiểm tra tính duy nhất và nghiệm cụ thể.** Khi đường dữ liệu gặp tất cả đặc trưng một cách độc lập, giải hệ cho $F,G$. Khi đường dữ liệu là một đặc trưng, mô tả các hàm còn tùy ý và đưa hai lựa chọn rõ ràng. Cuối cùng thế lại phương trình gốc, không chỉ ODE mới.

---

**Mục tiêu.** Đưa phương trình elliptic về dạng đơn giản, rồi tìm nghiệm giải tích từ dữ liệu Cauchy mà bài yêu cầu.

**Bước 1 — Loại hạng hỗn hợp và hạng cấp một do đổi biến.** Tính $\delta<0$, chọn $\xi,\eta$ thực có Jacobian khác $0$. Thay đầy đủ đạo hàm cấp hai; các đạo hàm của tọa độ có thể triệt tiêu với hạng cấp một trong đề. Kết quả thường là $v_{\xi\xi}+v_{\eta\eta}+c v=0$.

**Bước 2 — Chuyển dữ liệu sang đường tọa độ mới.** Nếu đường dữ liệu trở thành $\xi=0$, đặt $v(0,\eta)=f(\eta)$ và tính $v_\xi(0,\eta)=g(\eta)$ từ đạo hàm được cho. Nếu đường là $\eta=\eta_0$, đổi vai trò hai biến. Không lấy nguyên dữ liệu đạo hàm cũ làm dữ liệu mới khi hệ số dây chuyền khác $1$.

**Bước 3 — Khai triển và lập truy hồi.** Viết

$$
v(\xi,\eta)=\sum_{n=0}^{\infty}\frac{\xi^n}{n!}a_n(\eta),\qquad
a_0=f,\quad a_1=g,\quad a_{n+2}=-a_n''-c a_n.
$$

Tính từng $a_2,a_3,\ldots$. Nếu các hệ số sau một bậc đều bằng $0$, chuỗi kết thúc và cho một đa thức chính xác. Nếu không, cần xét hội tụ trong miền dữ liệu giải tích; chuỗi hình thức chưa tự là nghiệm.

**Bước 4 — Đổi ngược và kiểm tra.** Thế $\xi(x,y),\eta(x,y)$ vào nghiệm. Tính đạo hàm hoặc dùng toán tử đã được chứng minh tương đương để kiểm tra PDE, đồng thời kiểm tra từng dữ liệu gốc. Kết luận duy nhất trong lớp nghiệm giải tích trên miền liên thông mà phép đổi biến hợp lệ; dữ liệu Cauchy elliptic nói chung có thể không ổn định, nên không suy ra tồn tại cho dữ liệu tùy ý chỉ từ cách lập chuỗi.

## Chương 3 — Hướng dẫn chi tiết

**Bước 1 — Nhận dạng dữ liệu và tốc độ.** Viết $u_{tt}-a^2u_{xx}=F$, $u(x,0)=f(x)$, $u_t(x,0)=g(x)$; tốc độ là $a>0$, không phải $a^2$. Với dữ liệu trơn, cần $f\in C^2$, $g\in C^1$. Nếu dữ liệu có góc hoặc bước nhảy, công thức vẫn mô tả sóng từng miền nhưng phải xác định nơi mất tính trơn.

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

**Bước 5 — Kiểm tra và đọc ý nghĩa.** Đạo hàm công thức: $u_x=(f'(\xi)+f'(\eta))/2+(g(\eta)-g(\xi))/(2a)$, $u_t=a(f'(\eta)-f'(\xi))/2+(g(\eta)+g(\xi))/2$. Tại $t=0$ thu lại $f,g$; đạo hàm tiếp cho PDE. Các điểm gãy $s=b$ phát sinh đường $x\pm at=b$. Chu kỳ phải đúng cho mọi $x,t$, không chỉ sau khi một mặt sóng đi qua một điểm cố định.

---

**Bước 1 — Đọc đúng điều kiện biên.** Biên $u(0,t)=0$ dùng mở rộng lẻ; biên $u_x(0,t)=0$ dùng mở rộng chẵn. Với dữ liệu trên $x\ge0$, đặt $\widetilde f(-s)=-f(s)$ hoặc $f(s)$ tương ứng, làm tương tự cho $g$. Mở rộng lẻ là $C^2$ nếu $f(0)=f''(0)=0$, và mở rộng lẻ của $g$ là $C^1$ nếu $g(0)=0$. Mở rộng chẵn đòi $f'(0)=g'(0)=0$ cho mức trơn ấy.

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

**Bước 5 — Kiểm tra góc và đường ghép.** Biên Dirichlet không thuần nhất cần $h(0)=f(0)$, $h'(0)=g(0)$, $h''(0)=a^2f''(0)$ để có nghiệm $C^2$ cho phương trình thuần nhất. So sánh hai vết trên $x=at$, gồm $u,u_x,u_t$ rồi đạo hàm cấp hai. Nếu không tương thích, nêu rõ mức trơn còn lại thay vì khẳng định nghiệm cổ điển trên toàn miền.

---

**Bước 1 — Liệt kê các khoảng của dữ liệu.** Ghi đủ điểm đầu, điểm cuối hỗ trợ, điểm gãy và bước nhảy của $f,g$. Nếu có biên, phản xạ chẵn hoặc lẻ trước khi tích phân; trên đoạn hữu hạn tiếp tục phản xạ đến một chu kỳ hoàn chỉnh.

**Bước 2 — Tính nguyên hàm liên tục.** Lấy $H'=\widetilde g$ trên từng khoảng và chọn hằng số để hai vết của $H$ bằng nhau. Viết $[s]_p^q=\min(q,\max(p,s))$ hoặc $(s)_+=\max(s,0)$ khi cần gộp nhiều nhánh. Một nguyên hàm liên tục tránh tạo ra bước nhảy giả trong nghiệm.

**Bước 3 — Xác định sóng phải và sóng trái.** Đặt $A(s)=\widetilde f(s)/2-H(s)/(2a)$, $B(s)=\widetilde f(s)/2+H(s)/(2a)$; khi đó $u=A(x-at)+B(x+at)$. Với từng $t$ được yêu cầu, dịch đồ thị $A$ sang phải $at$ và $B$ sang trái $at$, rồi cộng tung độ. Các đường $x-at=b$ và $x+at=b$ chia mặt phẳng thành các miền có công thức đơn giản.

**Bước 4 — Xét liên tục, đạo hàm và giao của các mặt sóng.** Nếu $f$ có bước nhảy, $u$ thường có bước nhảy; nếu $f$ liên tục và $g$ bị chặn thì $u$ liên tục. Tại thời điểm cố định,

$$
u_x=\frac{\widetilde f'(x-at)+\widetilde f'(x+at)}2+\frac{\widetilde g(x+at)-\widetilde g(x-at)}{2a}.
$$

Tính giới hạn trái/phải của biểu thức này tại từng vị trí ứng viên. Có thể có triệt tiêu khi hai đường gặp nhau, nên không chỉ liệt kê đường rồi khẳng định mọi đạo hàm đều mất. Với tính $C^1$ theo cả $x,t$, còn kiểm tra $u_t$. Với $C^2$, xét tiếp các góc của $g$ và đạo hàm cấp hai của $f$.

**Bước 5 — Tính thời điểm đến, giới hạn và ngưỡng.** Sóng ở $(x,t)$ chỉ nhận dữ liệu trong $[x-at,x+at]$. Giải bất đẳng thức giao hỗ trợ để tìm thời điểm đến và đi qua. Nếu $H$ hằng ngoài đoạn hỗ trợ, dùng các giá trị hằng này để tính giới hạn khi $t\to\infty$. Nếu hỏi áp suất cực đại, viết hàm từng khoảng thời gian và so sánh cực trị, bước nhảy cùng hai giá trị một phía.

---

**Bước 1 — Tách biến và chọn bài toán trị riêng theo biên.** Đặt $u=X(x)T(t)$ trong $u_{tt}=a^2u_{xx}$, suy $X''+\lambda X=0$, $T''+a^2\lambda T=0$. Tích phân từng phần cho $\lambda\int X^2=\int (X')^2$ khi hạng biên bằng không; do đó $\lambda\ge0$. Giải cả trường hợp $\lambda=0$ trước khi xét $\lambda=k^2>0$.

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

**Bước 5 — Kiểm tra biên, dữ liệu và hội tụ.** Mỗi mode thỏa biên; tại $t=0$ hai chuỗi cho khai triển của $f,g$. Nếu dữ liệu không tương thích ở góc, giải theo nghĩa năng lượng hoặc từng miền và nêu đường mất tính trơn; không đạo hàm một chuỗi yếu tùy ý. Chu kỳ được suy từ tất cả mode có hệ số khác không, kể cả mode hằng; hai tần số có tỷ số vô tỷ ngăn một chu kỳ chung.

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

Chỉ bỏ hạng biên sau khi thế $0,L$ và điều kiện thực sự của $P$. Nếu dữ liệu chia đoạn, áp dụng công thức trên từng đoạn, rồi cộng các hạng tại điểm chia. Cuối cùng nhân nghịch đảo chuẩn của hàm riêng; nếu hệ số là của vận tốc, chia thêm tần số khi ghép nghiệm. Với mẫu số bằng $0$ trong tích–tổng, quay lại tích phân gốc để tính riêng.

---

**Bước 1 — Đưa điều kiện biên về thuần nhất.** Với $u(0,t)=\mu(t)$, $u(L,t)=\nu(t)$, đặt $b=(1-x/L)\mu+(x/L)\nu$. Với Neumann hai đầu đặt $b=\mu x+(\nu-\mu)x^2/(2L)$. Với Dirichlet–Neumann đặt $b=\mu+x\nu$. Viết $u=b+w$; khi đó $w$ có biên thuần nhất, nguồn $Q=F+a^2b_{xx}-b_{tt}$ và dữ liệu $f-b(x,0)$, $g-b_t(x,0)$.

**Bước 2 — Chiếu nguồn và dữ liệu lên cùng hệ hàm riêng.** Tính $Q_n(t)=\int QX_n/\int X_n^2$, $A_n$, $B_n$. Không bỏ các dữ liệu mới phát sinh từ hàm nâng biên; chúng có thể khác không ngay khi dữ liệu gốc bằng không.

**Bước 3 — Giải ODE có nguồn cho từng mode.**

$$
y_n''+\omega_n^2y_n=Q_n(t),\qquad
y_n=A_n\cos\omega_nt+\frac{B_n}{\omega_n}\sin\omega_nt+\frac1{\omega_n}\int_0^t\sin(\omega_n(t-s))Q_n(s)ds.
$$

Với mode hằng Neumann, thay công thức bằng $y_0=A_0+B_0t+\int_0^t(t-s)Q_0(s)ds$.

**Bước 4 — Xử lý cộng hưởng trước khi chia.** Nguồn $\cos\alpha t$ có đáp ứng dữ liệu không là $(\cos\alpha t-\cos\omega t)/(\omega^2-\alpha^2)$; tại $\alpha=\omega$ lấy $t\sin\omega t/(2\omega)$. Nguồn $\sin\alpha t$ có đáp ứng $(\sin\alpha t-(\alpha/\omega)\sin\omega t)/(\omega^2-\alpha^2)$; tại cộng hưởng là $\sin\omega t/(2\omega^2)-t\cos\omega t/(2\omega)$. Không thế vào phân số $0/0$.

**Bước 5 — Cộng lại hàm nâng và kiểm tra duy nhất.** Thế $u=b+\sum y_nX_n$ vào PDE và mọi dữ liệu. Với hiệu hai nghiệm, nguồn và biên bằng không; nhân phương trình với $w_t$, tích phân từng phần để có $E'=0$, $E(0)=0$, suy $w=0$. Các góc không tương thích phải được ghi riêng.

**Chi tiết xác nhận tích phân nguồn.** Với $D(t)=\omega^{-1}\int_0^t\sin(\omega(t-s))Q(s)ds$, lần đạo hàm đầu cho $D'=\int_0^t\cos(\omega(t-s))Q(s)ds$, vì $\sin0=0$. Lần sau cho $D''=Q(t)-\omega\int_0^t\sin(\omega(t-s))Q(s)ds=Q-\omega^2D$. Do $D(0)=D'(0)=0$, tích phân này thêm đúng nguồn mà giữ nguyên hai dữ liệu đầu.

---

**Bước 1 — Chọn năng lượng theo toán tử.** Với sóng dùng $E=\frac12\int(u_t^2+a^2u_x^2)dx$. Với Klein–Gordon có thêm $u$, thêm $\frac12\int u^2dx$. Với dầm $u_{tt}=-a^2u_{xxxx}$ dùng $E=\frac12\int(u_t^2+a^2u_{xx}^2)dx$, không thay $u_{xx}$ bằng $u_x$.

**Bước 2 — Đạo hàm và tích phân từng phần.** Với $u_{tt}-a^2u_{xx}+\gamma u_t+\kappa u=F$, năng lượng có hạng $\kappa u^2$ cho

$$
E'=a^2[u_tu_x]_0^L-\gamma\int u_t^2dx+\int Fu_tdx.
$$

Với dầm, tích phân hai lần cho $E'=a^2[u_{tx}u_{xx}-u_tu_{xxx}]_0^L$. Viết riêng từng hạng biên rồi dùng điều kiện biên và đạo hàm theo thời gian của điều kiện đó để cho chúng bằng không.

**Bước 3 — Suy hệ quả.** Không cản, không nguồn thì $E$ bảo toàn. Có cản $\gamma>0$ thì $E'\le0$; nếu $E$ không có hệ số $1/2$, $E'=-2\gamma\int u_t^2\ge-2\gamma E$, suy $e^{-2\gamma t}E(0)\le E(t)\le E(0)$. Với hiệu hai nghiệm cùng dữ liệu, $E(0)=0$ nên có duy nhất.

**Bước 4 — Tách biến nếu phải tìm nghiệm cụ thể.** Sóng có cản $\gamma=1$ cho $T''+T'+a^2\lambda T=0$. Đặt $T=e^{-t/2}Y$, thu $Y''+(a^2\lambda-1/4)Y=0$, $Y(0)=A$, $Y'(0)=B+A/2$. Phân biệt dao động, nghiệm kép và hàm hyperbolic. Dầm cho $X''''=k^4X$, $T''+a^2k^4T=0$; dùng đủ bốn điều kiện biên để tìm phương trình của $kL$.

**Bước 5 — Kiểm tra hệ số và khẳng định của đề.** Năng lượng đầu chứa cả $g^2$ và các đạo hàm của $f$. Thử $f=0$, $g\ne0$ để phát hiện công thức bỏ vận tốc. Với dầm, nghiệm $k=0$ phải giải trực tiếp bằng đa thức bậc ba; nghiệm $0$ của phương trình lượng giác–hyperbolic có thể chỉ là nghiệm giả do cơ sở suy biến.

**Chi tiết phép triệt tiêu tích phân.** Đạo hàm động năng cho $\int u_tu_{tt}$; dùng PDE thay $u_{tt}$. Với sóng, $\int u_tu_{xx}=[u_tu_x]-\int u_{tx}u_x$, và tích phân cuối triệt tiêu đạo hàm thế năng $\int u_xu_{xt}$. Với dầm,

$$
\int u_tu_{xxxx}=[u_tu_{xxx}-u_{tx}u_{xx}]+\int u_{txx}u_{xx}.
$$

Tích phân cuối triệt tiêu đạo hàm $\frac12\int u_{xx}^2$ sau khi nhân hệ số và giữ đúng dấu PDE. Viết hạng biên trước, sau đó mới dùng điều kiện của từng đầu.

---

**Bước 1 — Chọn Kirchhoff (3D) hoặc Poisson (2D).** Với li độ đầu bằng không, vận tốc $\psi$, tốc độ $c$, đặt $\rho=ct$. Trong ba chiều,

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

**Bước 5 — Kiểm tra chuẩn hóa, mặt sóng và cực đại.** Nếu $\psi=1$ trên toàn không gian thì $u=t$, dùng để kiểm tra hệ số. Với dữ liệu bước nhảy, chỉ kết luận cổ điển ngoài các mặt sóng. Cực đại phải xét cả điểm chuyển nhánh và giá trị một phía; nêu rõ supremum nếu chỉ đạt theo giới hạn. Nếu dùng tích phân số, ghi tham số và cách kiểm tra hội tụ; đồ thị không tự chứng minh một cực đại toàn cục.

---

**Bước 1 — Giữ nhất quán dấu toán tử.** Đặt $q=x^2+y^2-t^2$, $\Box=\partial_{xx}+\partial_{yy}-\partial_{tt}$. Phương trình $u_{tt}-\Delta u=\Phi$ là $-\Box u=\Phi$. Dữ liệu trên nón $q=0$ gợi ý mỗi hạng của nghiệm chứa ít nhất một thừa số $q$.

**Bước 2 — Tính quy tắc đạo hàm tích.** Với $H$ thuần nhất bậc $m$, dùng Euler $xH_x+yH_y+tH_t=mH$ để có $\Box(q^jH)=q^j\Box H+2j(2m+2j+1)q^{j-1}H$. Tính trực tiếp $\Box q=6$ để kiểm tra hệ số.

**Bước 3 — Lập truy hồi hữu hạn.** Viết $u=\sum a_kq^{k+1}\Box^k\Phi$. Vì $\Phi$ bậc $d-2$, hệ số khi áp dụng $\Box$ là $C_k=2(k+1)(2d-2k-1)$. Chọn $a_0=-1/C_0$, $a_k=-a_{k-1}/C_k$ để triệt tiêu các hạng còn lại. Các đạo hàm lặp của đa thức hết sau hữu hạn bước.

**Bước 4 — Chứng minh duy nhất bằng năng lượng trên miền co.** Với hiệu $v$ của hai nghiệm, đặt $E(t)=\frac12\int_{x^2+y^2<t^2}(v_t^2+|\nabla v|^2)dxdy$ cho $t<0$. Đạo hàm cả tích phân lẫn biên chuyển động. Vết $v(r,-r)=0$ cho $v_t=v_r$ và đạo hàm tiếp tuyến góc bằng không, nên thông lượng năng lượng bằng không. Nếu nghiệm đủ trơn đến đỉnh, $E(t)\to0$ khi $t\uparrow0$; do đó $E=0$, suy $v=0$ trong nón.

**Bước 5 — Thế lại nghiệm cụ thể.** Kiểm tra cả dấu PDE và $u|_{q=0}=0$. Với đa thức nguồn cụ thể, tính $\Box\Phi$ trước: nếu bằng không thì chỉ còn hạng $a_0q\Phi$.

## Chương 4 — Hướng dẫn chi tiết

**Bước 1 — Đọc hệ số và điều kiện biên.** Viết phương trình dưới dạng $u_t=Ku_{xx}$, $K>0$. Nếu đề ký hiệu tốc độ $a$ và viết $u_t=a^2u_{xx}$ thì thay $K=a^2$; không nhầm $a$ với $K$. Kiểm tra điều kiện đầu $f$ có khớp giá trị biên tại $t=0$ hay không. Sự không tương thích tại góc không ngăn nghiệm trơn với $t>0$, nhưng ngăn tính liên tục đến góc khi biên Dirichlet khác vết của $f$.

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

**Bước 5 — Kiểm tra dữ liệu, hội tụ và thời gian dài.** Với $t\ge\varepsilon>0$, thừa số $e^{-K\lambda_nt}$ cho phép lấy đạo hàm chuỗi. Với dữ liệu có bước nhảy, giới hạn ban đầu tại bước nhảy là trung bình hai vết. Nếu $f\in L^1$, $|c_n|\le2\|f\|_1/L$ cho hệ chuẩn, nên tổng các mode dương tiến về không đều theo $x$. Neumann giữ trung bình; Dirichlet và biên hỗn hợp có giới hạn không. Một nghiệm giảm theo hàm mũ và khác không không thể tuần hoàn theo thời gian.

---

**Bước 1 — Chọn đúng đại lượng.** Năng lượng bình phương là $I(t)=\frac12\int_0^Lu^2dx$. Để chứng minh duy nhất, áp dụng cho hiệu $w$ của hai nghiệm cùng dữ kiện; $w$ có dữ liệu đầu bằng không và biên thuần nhất. Tổng nhiệt $E=\int_0^Lu\,dx$ là đại lượng khác, dùng khi đề hỏi bảo toàn hoặc suy giảm tổng nhiệt.

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

**Bước 5 — Khi có hạng phản ứng hoặc bậc đạo hàm khác.** Với Dirichlet và $u_t=Ku_{xx}+Au_x+Bu$, hạng $A\int uu_x=A[u^2]_0^L/2=0$, nên $I'=-K\int u_x^2+2BI\le2BI$; $e^{-2Bt}I$ không tăng, vẫn suy duy nhất. Với $u_t=Ku_{xxx}$, tích phân hai lần cho $I'=K[uu_{xx}-u_x^2/2]_0^L$. Với tổng nhiệt trong bài Neumann có $-ru$, $E'=K[u_x]_0^L-rE$; giải ODE này trước khi kết luận.

---

**Bước 1 — Viết toán tử và biên parabol.** Đặt $P=\partial_t-a(x,t)\partial_{xx}-b(x,t)\partial_x-c(x,t)$ với $a\ge0$, $c\le0$. Biên parabol gồm mặt $t=0$ và các biên không gian; mặt $t=T$ vẫn thuộc miền được ước lượng. Với phương trình nhiệt, $a=K>0$, $b=c=0$.

**Bước 2 — Loại cực đại dương bằng dấu đạo hàm.** Tại cực đại dương nội miền, $w_x=0$, $w_{xx}\le0$, $w_t=0$; nếu cực đại trên mặt thời gian trên thì đạo hàm một phía cho $w_t\ge0$. Suy $Pw\ge0$, mâu thuẫn $Pw<0$. Với $Pw\le0$, xét $w_\varepsilon=w-\varepsilon e^{\gamma t}$, $\gamma>0$: $Pw_\varepsilon=Pw-\varepsilon(\gamma-c)e^{\gamma t}<0$. Chứng minh $w_\varepsilon\le0$ rồi cho $\varepsilon\downarrow0$.

**Bước 3 — So sánh hai hàm bằng hiệu.** Để chứng minh $v\le u\le V$, kiểm tra $Pv\le Pu\le PV$ và thứ tự của dữ liệu đầu, biên. Áp dụng bước 2 cho $v-u$ và $u-V$. Nếu có nguồn dương, hằng số không nhất thiết là nghiệm trên, nên phải tính $PV-Pu$; không dùng cực đại của dữ liệu để chặn một bài có nguồn mà chưa kiểm tra.

**Bước 4 — Xử lý Neumann, Robin và tuần hoàn.** Neumann thuần nhất có thể phản xạ chẵn qua đầu mút; điểm biên trở thành điểm trong. Robin viết theo pháp tuyến ngoài $\partial_\nu u+\sigma u=0$, $\sigma\ge0$. Tại cực đại dương không hằng, bổ đề Hopf cho $\partial_\nu u>0$, trái với $\partial_\nu u=-\sigma u\le0$. Với Robin phải thêm mức $0$ vào cận hằng nếu dữ liệu mang một dấu. Biên tuần hoàn ghép hai đầu thành đường tròn; không còn biên không gian.

**Bước 5 — Miền vô hạn và nguồn bị chặn.** Trên toàn trục/nửa trục, cần nghiệm bị chặn trên mỗi dải thời gian (hoặc điều kiện tăng trưởng đủ dùng). Dùng rào $\varepsilon((x-x_0)^2+2Kt)$ trên đoạn lớn, áp dụng cực đại trên miền hữu hạn rồi cho $\varepsilon\downarrow0$; cách này loại ảnh hưởng từ vô cực. Nếu $|Pu|\le N$ và $|u|\le M$ trên biên parabol, đặt $V=M+Nt$. Vì $PV=N-cV\ge N$, suy $|u|\le M+Nt\le M+NT$. $M$ ở đây là cận của $|u|$, không phải cực đại có dấu.

---

**Bước 1 — Tìm cơ sở và chuẩn.** Giải $-X_n''=\lambda_nX_n$ với đúng biên thuần nhất. Đặt $N_n=\int_0^LX_n^2dx$; các hàm riêng ở biên Robin không có chuẩn mặc định $L/2$. Từ $c_n=N_n^{-1}\int fX_n$ trong chuỗi nghiệm, đổi thứ tự tổng–tích phân với $t>0$ để nhận ra

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

**Bước 5 — Nửa nhóm và thời gian dài.** Trực giao cho $\int G(x,z,s)G(z,y,t)dz=G(x,y,s+t)$. Với $H(t)=\max_xm(x,t)$ ở Dirichlet, $m(x,t+s)\le H(t)m(x,s)$, nên $H(t+s)\le H(t)H(s)<H(t)$. Để chứng minh $H(t)\to1$ lúc đầu, giữ một $x_0$ trong miền, dùng $m(x_0,t)\to1$ và $m(x_0,t)\le H(t)\le1$.

---

**Bước 1 — Khử điều kiện biên không thuần nhất.** Viết $u=b+w$ với $b$ thỏa đúng biên. Dirichlet hai đầu: $b=\mu+(\nu-\mu)x/L$. Neumann hai đầu: $b=\mu x+(\nu-\mu)x^2/(2L)$. Neumann–Dirichlet: $b=\nu+\mu(x-L)$; Dirichlet–Neumann: $b=\mu+x\nu$. Robin trái–Dirichlet phải: $b=\mu+d+dx$, $d=(\nu-\mu)/(L+1)$. Neumann trái–Robin phải: $b=\nu-\mu(L+1)+\mu x$. Hai Robin: $b=\mu+d+dx$, $d=(\nu-\mu)/(L+2)$.

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

**Bước 5 — Kiểm tra và tìm giới hạn.** Mỗi mode đúng PDE, biên; $T_n(0)=d_n$ trả lại dữ liệu đầu sau khi cộng $b_0$. Tách mode hằng Neumann: $\frac d{dt}\int u=K(\nu-\mu)+\int F$. Trạng thái dừng chỉ tồn tại nếu tổng nguồn và thông lượng cân bằng. Với các mode dương, kiểm tra hội tụ đủ để lấy giới hạn đều; không bỏ một mode bằng không hoặc mode tăng.

---

**Bước 1 — Loại đạo hàm cấp một bằng tính đạo hàm đầy đủ.** Với $u_t=Ku_{xx}+Au_x+Bu$, đặt $u=e^{-hx}v$, $h=A/(2K)$. Khi đó

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

**Bước 5 — Duy nhất và ổn định.** Với hiệu nghiệm Dirichlet, $I'=-K\int w_x^2+2BI\le2BI$ suy $w=0$ khi $I(0)=0$. Giới hạn phụ thuộc các số $C-K\lambda_n$ có hệ số khác không: âm thì giảm, bằng không thì tồn tại mode dừng, dương thì tăng. Phải kiểm tra tính thống nhất giữa miền PDE và vị trí biên trước khi dùng công thức.

---

**Bước 1 — Chọn nhân nhiệt theo miền và hệ số.** Trên $\mathbb R$, $g_K(z,t)=(4\pi Kt)^{-1/2}e^{-z^2/(4Kt)}$, $u=g_K*f$. Trên nửa trục, thác triển lẻ cho Dirichlet $0$, chẵn cho Neumann $0$; sau đổi $y\mapsto-y$ ở nửa âm:

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

**Bước 5 — Nhiều chiều và kiểm tra.** Nhân $n$ chiều là tích các nhân một chiều. Dữ liệu dạng tích tách được tích phân không gian bằng Fubini; nguồn dạng tích vẫn phải tích phân theo một thời gian chung $s$. Kiểm tra PDE bằng đạo hàm Duhamel: đạo hàm cận trên trả lại $F(x,t)$, phần còn lại bằng $K\Delta u$. Nhân Gauss là xấp xỉ đơn vị, nên trả lại dữ liệu tại điểm liên tục; dữ liệu nhảy không cho nghiệm liên tục đến mọi điểm lúc đầu.

---

**Bước 1 — Phân biệt đạo hàm cấp hai, ba và bốn.** Quy ước $\widehat f(\xi)=\int e^{-i\xi x}f(x)dx$, biến đổi ngược có hệ số $1/(2\pi)$. Khi đó $\widehat{f^{(m)}}=(i\xi)^m\widehat f$, $\widehat{xf}=i\partial_\xi\widehat f$, $\widehat{xf_x}=-\widehat f-\xi\partial_\xi\widehat f$.

**Bước 2 — Giải phương trình của biến đổi.** $u_t=u_{xx}$ cho $\widehat u=e^{-t\xi^2}\widehat f$. $u_t=u_{xxx}$ cho $\widehat u=e^{-it\xi^3}\widehat f$. $u_t=-u_{xxxx}$ cho $\widehat u=e^{-t\xi^4}\widehat f$. Với $xu_x$, giải PDE cấp một theo $\xi$ bằng đường đặc trưng, gồm cả hệ số biên độ $-\widehat u$.

**Bước 3 — Biến đổi ngược và ý nghĩa tích phân.** Nhân bậc ba là $A_t(x)=(3t)^{-1/3}\operatorname{Ai}(-x/(3t)^{1/3})$, tích phân dao động. Nhân bậc bốn là $B_t(x)=(2\pi)^{-1}\int e^{i\xi x-t\xi^4}d\xi$, hội tụ tuyệt đối theo $\xi$ và có thể đổi dấu. Không áp dụng tính dương của Gauss hay nguyên lý cực đại cấp hai cho hai nhân này.

**Bước 4 — Miền hữu hạn cần kiểm tra biên và toán tử liên hợp.** Với $u_t=Ku_{xxx}$, $u(0)=u_x(0)=u(L)=0$, năng lượng cho $I'=-K u_x(L)^2/2$. Toán tử liên hợp là $-KD^3$ với $Y(0)=Y(L)=Y'(L)=0$. Đây không phải bài Sturm–Liouville tự liên hợp cấp hai; không suy mọi trị riêng đều thực và không tự dùng hệ số $\int fX/\int X^2$. Có thể giải bằng biến đổi Laplace theo thời gian và nghiệm cơ bản của ODE bậc ba, tránh khẳng định cơ sở chưa chứng minh.

**Bước 5 — Nêu lớp dữ liệu đủ cho công thức.** Với bậc ba trên toàn trục, công thức Fourier hợp lệ trước hết cho dữ liệu Schwartz hoặc $L^2$ theo nghĩa biến đổi Fourier. Dữ liệu liên tục bị chặn là phân phối tempered; phép nhân $e^{-it\xi^3}\widehat f$ vẫn hợp lệ vì các đạo hàm của thừa số tăng đa thức, nên xác định nghiệm trong $\mathcal S\prime$. Tuy nhiên điều đó không bảo đảm tích phân Airy hội tụ tuyệt đối hay nghiệm tự động là hàm cổ điển. Ghi đúng ý nghĩa của công thức theo lớp dữ liệu.

## Các phương pháp ở chương sau

**Bước 1 — Phần chính.** Với $Au_{xx}+2Bu_{xy}+Cu_{yy}$, tính $\delta=B^2-AC$: dương là hyperbolic, bằng 0 là parabolic, âm là elliptic tại điểm đang xét.

**Bước 2 — Chọn tọa độ và dùng quy tắc dây chuyền.** Đặt $u(x,y)=v(\xi(x,y),\eta(x,y))$ với Jacobian khác 0. Đặc biệt,

$$
u_{xx}=v_{\xi\xi}\xi_x^2+2v_{\xi\eta}\xi_x\eta_x+v_{\eta\eta}\eta_x^2+v_\xi\xi_{xx}+v_\eta\eta_{xx}.
$$

Tính tương tự $u_{xy},u_{yy}$; phải giữ các hạng cấp 1 phát sinh khi phép đổi biến không tuyến tính. Dạng chính tắc chỉ hợp lệ trên miền Jacobian không triệt tiêu.

**Bước 3 — Giải phương trình đã đổi và áp dữ liệu.** Với $v_{\xi\eta}=h$, tích phân hai lần cho $v=F(\xi)+G(\eta)+\iint h$. Với phương trình chỉ theo một tọa độ, coi tọa độ kia là tham số. Dữ liệu đặt trên đặc trưng có thể không xác định hết các hàm tùy ý.

---

**Bước 1 — Hai họ đặc trưng.** Với $u_{tt}=a^2u_{xx}$, chúng là $x-at=\text{hằng}$ và $x+at=\text{hằng}$. Viết $u=A(x-at)+B(x+at)$, rồi dùng $u(x,0)=f(x)$, $u_t(x,0)=g(x)$:

$$A+B=f,\qquad -aA'+aB'=g.$$

**Bước 2 — Công thức nghiệm.** Tích phân hai đẳng thức cho d’Alembert:

$$u(x,t)=\frac{f(x-at)+f(x+at)}2+\frac1{2a}\int_{x-at}^{x+at}g(s)ds.$$

Nếu có nguồn $H(x,t)$, cộng phần Duhamel

$$\frac1{2a}\int_0^t\int_{x-a(t-s)}^{x+a(t-s)}H(y,s)\,dy\,ds.$$

**Bước 3 — Biên và tính trơn.** Biên Dirichlet 0 dùng thác triển lẻ; Neumann 0 dùng thác triển chẵn. Biên khác 0 phải cộng sóng từ biên hoặc dùng hàm khử biên. Kiểm tra các đường $x\pm at$ đi qua điểm gãy của dữ liệu; công thức nghiệm yếu có thể đúng dù nghiệm không $C^2$ qua mặt sóng.

---

**Bước 1 — Bài trị riêng không gian.** Đặt $u=X(x)T(t)$, được $-X''=\lambda X$, $T''+a^2\lambda T=0$. Các điều kiện biên xác định cơ sở $X_n$; Dirichlet hai đầu cho $X_n=\sin(n\pi x/L)$, còn biên hỗn hợp có thể cho tần số nửa nguyên.

**Bước 2 — Khai triển dữ liệu.** Với $N_n=\int_0^LX_n^2$, đặt $f_n=N_n^{-1}\int fX_n$, $g_n=N_n^{-1}\int gX_n$, $\omega_n=a\sqrt{\lambda_n}$.

$$u=\sum_n\left[f_n\cos\omega_nt+\frac{g_n}{\omega_n}\sin\omega_nt+\int_0^t\frac{\sin\omega_n(t-s)}{\omega_n}H_n(s)ds\right]X_n.$$

Mode $\omega_n=0$, nếu có, được hiểu bằng giới hạn $\sin\omega_nt/\omega_n=t$. Với biên không thuần nhất, khử biên trước khi tính hệ số nguồn. Nếu có lực cản hoặc phản ứng, giải ODE của từng mode theo hệ số thực tế của bài, không dùng nguyên công thức dao động điều hòa.

---

**Bước 1 — Chọn công thức theo số chiều.** Trong ba chiều, với li độ đầu bằng 0, công thức Kirchhoff là

$$u(P,t)=\frac{t}{4\pi}\int_{S^2}\psi(P+at\omega)\,d\omega.$$

Với vận tốc là hàm chỉ thị của một miền, tích phân này bằng $t$ nhân tỷ lệ diện tích mặt cầu nằm trong miền. Trong hai chiều dùng Poisson:

$$u(P,t)=\frac1{2\pi a}\int_{|Q-P|<at}\frac{\psi(Q)}{\sqrt{a^2t^2-|Q-P|^2}}\,dQ.$$

**Bước 2 — Dùng hình học hoặc đối xứng.** Chỏm cầu, tọa độ cực và đối xứng quay giúp giảm tích phân mặt thành độ dài khoảng hoặc tích phân một chiều. Phải kiểm tra bất đẳng thức gốc sau khi bình phương.

**Bước 3 — Nguồn và cực trị.** Nguồn được tích phân theo thời gian bằng Duhamel. Tìm cực trị trong từng nhánh trơn rồi xét thêm các thời điểm chuyển nhánh; dữ liệu gián đoạn đôi khi chỉ cho supremum theo giới hạn một phía.

---

**Bước 1 — Tách biên và chọn cơ sở.** Với hình chữ nhật, tách một bài có một cạnh dữ liệu khác 0 rồi chồng chất. Các cạnh đối diện Dirichlet 0 chọn sine, Neumann 0 chọn cosine; sau tách biến $-X''=\lambda X$, phần còn lại thỏa $Y''-\lambda Y=F_n$.

**Bước 2 — Giải phương trình theo tọa độ còn lại.** Khi $F_n=0$, dùng sinh/cosh thay vì sine/cosine dao động. Khi có nguồn, dùng nghiệm riêng hoặc Green của ODE. Hệ số được tính từ tích phân trực giao, ví dụ $f_n=2L^{-1}\int_0^Lf(x)\sin(n\pi x/L)dx$.

**Bước 3 — Kiểm tra tồn tại và duy nhất.** Với $\Delta u=F$, biên Neumann phải có $\int_{\partial\Omega}\partial_\nu u=\int_\Omega F$. Hiệu hai nghiệm cùng dữ liệu là điều hòa; tích phân Green xác định nó bằng 0 hoặc bằng hằng tùy biên. Các giá trị trái nhau ở góc không thể cho nghiệm liên tục trên toàn miền đóng.

---

**Bước 1 — Viết toán tử theo tọa độ cực.**

$$\Delta u=u_{rr}+\frac1r u_r+\frac1{r^2}u_{\theta\theta}.$$

Với mode $\cos n\theta,\sin n\theta$, phương trình xuyên tâm thuần nhất có hai nghiệm $r^n,r^{-n}$; mode 0 có $1,\log r$. Trên đĩa chứa tâm, tính chính quy loại $r^{-n}$ và $\log r$; trên vành khuyên giữ cả hai.

**Bước 2 — Dùng dữ liệu.** Khai triển Fourier dữ liệu trên đường tròn để tìm hệ số; mỗi mode trên đĩa nhân $(r/R)^n$. Trên hình quạt, điều kiện ở hai cạnh góc xác định tần số $n\pi/\alpha$. Với Neumann, $\partial_\nu=\partial_r$ trên cung ngoài, còn trên cạnh góc là $\pm r^{-1}\partial_\theta$.

**Bước 3 — Nguồn và tương thích.** Tách một nghiệm riêng của $\Delta P=F$, rồi giải bài điều hòa cho $u-P$. Tổng thông lượng ngoài phải bằng tích phân nguồn đối với Neumann; mode hằng thể hiện đúng điều kiện này.

---

**Các công cụ dùng trong chứng minh.** Với hai hàm đủ trơn,

$$\Delta(uv)=u\Delta v+v\Delta u+2\nabla u\cdot\nabla v.$$

Với hàm xuyên tâm $u=f(r)$ trong $\mathbb R^n$,

$$\Delta u=f''(r)+\frac{n-1}{r}f'(r).$$

Tính giá trị trung bình và công thức Poisson cho phép suy cận nội của đạo hàm. Khi dùng liên thông, tính trơn tại tâm hoặc tăng trưởng ở vô cực, phải nêu giả thiết tương ứng; bỏ một giả thiết có thể làm kết luận sai.

---

**Bước 1 — Xác nhận điều hòa và miền.** Kiểm tra $\Delta u=0$ và tính liên tục trên miền đóng nếu muốn áp dụng nguyên lý cực đại đến biên; một cực nằm trên biên có thể làm hỏng giả thiết.

**Bước 2 — Dùng cực đại hoặc giá trị trung bình.** Hàm điều hòa không hằng trên miền liên thông không đạt cực đại/cực tiểu trong miền. Trên đĩa, giá trị tâm là trung bình dữ liệu trên đường tròn. Với dữ liệu không âm, nhân Poisson dương còn cho tính dương trong miền.

**Bước 3 — Tính các giá trị biên và xét ngoại lệ.** Cực đại yếu cho cận không nghiêm; muốn dấu nghiêm phải dùng nguyên lý mạnh và loại nghiệm hằng. Với Robin, dùng $\int|\nabla w|^2=\int_{\partial\Omega}w\partial_\nu w$ cho hiệu hai nghiệm.

---

**Bước 1 — Chọn bài trị riêng đúng biên.** Giải $-L\phi=\lambda\phi$. Nếu có trôi $Au_x$, phép đổi ẩn mũ đưa về toán tử tự liên hợp nhưng đồng thời đổi điều kiện Neumann thành Robin; cần giữ sự thay đổi này.

**Bước 2 — Trực giao và hệ số.** Nếu toán tử tự liên hợp với trọng số $\sigma$, hệ số của $q$ là $q_n=\int q\phi_n\sigma/\int\phi_n^2\sigma$. Trong hình chữ nhật, hàm riêng thường là tích hai hàm một chiều và trị riêng là tổng hai trị riêng.

**Bước 3 — Giải mode của bài PDE.** Nhiệt cho $T_n'+\lambda_nT_n=H_n$; Poisson cho $-\lambda_nT_n=H_n$ sau khử biên; sóng cho $T_n''+\lambda_nT_n=H_n$. Mode 0, phổ liên tục và dữ liệu đầu dư phải xét riêng, không áp công thức chia cho $\lambda_n$ một cách máy móc.

---

**Bước 1 — Chốt quy ước.** Trên $[-L,L]$, dùng $f=a_0+\sum_{n\ge1}(a_n\cos(n\pi x/L)+b_n\sin(n\pi x/L))$, với

$$a_0=\frac1{2L}\int_{-L}^Lf,\quad a_n=\frac1L\int_{-L}^Lf\cos\frac{n\pi x}{L},\quad b_n=\frac1L\int_{-L}^Lf\sin\frac{n\pi x}{L}.$$

**Bước 2 — Tính hệ số.** Hàm chẵn chỉ có cosine, hàm lẻ chỉ có sine. Hàm phân đoạn phải chia tích phân tại điểm đổi biểu thức. Dùng tích thành tổng, tích phân từng phần hoặc chuỗi hình học/log để tính hệ số.

**Bước 3 — Hội tụ và giá trị ở mép.** Với dữ liệu trơn từng khúc, chuỗi về giá trị hàm tại điểm liên tục, về trung bình hai giới hạn tại điểm nhảy. Khai triển sine/cosine trên $[0,L]$ tương ứng thác triển lẻ/chẵn; giá trị ở đầu mút phải xét theo thác triển, không mặc nhiên bằng dữ liệu ban đầu. Hệ số suy đủ nhanh cho hội tụ đều bằng tiêu chuẩn Weierstrass.