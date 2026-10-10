"""Bổ sung các phép suy dẫn riêng, giữ biểu thức hình học đã kiểm tra từ scan."""
from pathlib import Path
import re
r=Path(__file__).resolve().parent
source=r/'backup_truoc_chi_tiet_chuong3'/'loi_giai_3c.tex'
if not source.exists():source=r/'loi_giai_3c.tex'
old=dict((m[1],m[2].strip()) for m in re.finditer(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',source.read_text(encoding='utf-8'),re.M|re.S))
prefix={
1:r'''\textbf{Bước 1. Quy các miền về cầu, nửa không gian và lớp.} Với vận tốc chỉ thị, Kirchhoff bằng $t$ nhân tỷ lệ diện tích mặt cầu. Các quả cầu bị bỏ ở (a),(b),(c) nằm trong miền lớn và đôi cầu ở (a) không chồng thể tích, nên được lấy hiệu các chỉ thị. Các quả cầu ở (d) rời nhau, nên cộng ba đóng góp. Đặt $\mu$ hướng về tâm cầu; điều kiện $r^2+c^2t^2-2rct\mu<R^2$ cho ngưỡng chỏm.

\textbf{Bước 2. Tính các khoảng cách đúng điểm quan sát.} (a) $P=(0,100,0)$ cách tâm lớn $100$, cách hai tâm $(\pm1,0,0)$ cùng $\sqrt{10001}$. (b) $P_z=100$, cầu bị bỏ có tâm $z=-2$, cách $102$; nửa không gian $z<0$ cho $\mu<-100/(2t)$, tỷ lệ $(1-50/t)_+/2$. (c) lớp $0<z<4$ cho $-100/(3t)<\mu<-96/(3t)$, còn cầu tâm $z=2$ cách $98$. (d) khoảng cách là $98$ tới $(0,2,0)$ và $\sqrt{10004}$ tới hai tâm $(\pm2,0,0)$. (e) hiệu hai góc phần tư là $(\operatorname{sgn}x+\operatorname{sgn}y)/2$; mỗi tọa độ của hướng cầu đều phân bố đều trên $[-1,1]$.

\textbf{Bước 3. Thay tỷ lệ diện tích vào Kirchhoff.}''',
2:r'''\textbf{Bước 1. Tham số hóa mặt cầu và giữ dấu của nón.} Tốc độ ký hiệu $c$, $\rho=ct$. Trên trục $z$, điểm cầu có chiều cao $z+\rho\mu$, bán kính trụ $\rho\sqrt{1-\mu^2}$. Miền $D$ là giao của $z'>\alpha r'$ với quả cầu $|Q|<R$; điều kiện $z'>0$ không được bỏ khi bình phương. Tích phân phương vị cho $2\pi$, nên $u=t|E|/2$.

\textbf{Bước 2. Giải từng ngưỡng; ở mặt phẳng $z=0$ khử góc phương vị.} Nhờ đối xứng chỉ cần $P=(r,0,0)$. Đặt $\omega=(\sqrt{1-\mu^2}\cos\phi,\sqrt{1-\mu^2}\sin\phi,\mu)$. Nón đòi $\mu>0$ và $r'^2<\rho^2\mu^2/\alpha^2$; cầu đòi $r'^2+\rho^2\mu^2<R^2$. Viết $r'^2=r^2+\rho^2(1-\mu^2)+2r\rho\sqrt{1-\mu^2}\cos\phi$, được hai cận trên cho $\cos\phi$. Độ dài góc đúng là $A(\min(B,C))$, không nhân hai tỷ lệ chỏm độc lập.

\textbf{Bước 3. Công thức tính $u$ và cực trị.}''',
3:r'''\textbf{Bước 1. Đưa điều kiện xuyến về một biến góc.} Trên trục $z$, bán kính trụ của điểm cầu là $\rho\sqrt{1-\mu^2}$, chiều cao $z+\rho\mu$. Thay vào $(r'-R)^2+z'^2<a^2$, khai triển để được tập $E$ dưới đây. Bình phương phương trình biên có thể sinh nghiệm ngoại lai, nên chia các khoảng và kiểm tra bất đẳng thức gốc.

\textbf{Bước 2. Ở mặt phẳng $z=0$, tính góc phương vị.} Chọn $P=(r,0,0)$, đặt $h=\sqrt{a^2-\rho^2\mu^2}$. Điều kiện xuyến tương đương $R-h<r'<R+h$, với $|\rho\mu|<a$. Vì $R>a$, cận dưới dương nên có thể bình phương hai vế. Thay $r'^2=r^2+\rho^2(1-\mu^2)+2r\rho\sqrt{1-\mu^2}\cos\phi$ cho $C_-<\cos\phi<C_+$. Độ dài góc là hiệu $A(C_+)-A(C_-)$.

\textbf{Bước 3. Tích phân một chiều và cực trị.}''',
4:r'''\textbf{Bước 1. Kiểm tra hai dữ liệu trước khi dùng công thức in.} Tại $t=0$, công thức $\psi+t\varphi$ trong sách cho li độ $\psi$ và vận tốc $\varphi$, đảo với dữ liệu đã ghi. Vì thế cần đổi lại $\varphi+t\psi$. Đặt $I(t)=\int_0^t(t-s)g(s)ds$, ta có $I(0)=I'(0)=0$, $I''=g$.

\textbf{Bước 2. Trường hợp điều hòa.} Mọi Laplace của $f,\varphi,\psi$ đều bằng không, nên nghiệm không có đóng góp $c^2\Delta u$; chỉ cần giải ODE thời gian tại mỗi điểm. Trường hợp $k$-điều hòa dùng chuỗi Taylor chẵn/lẻ theo thời gian và chuỗi Duhamel, nhưng kết thúc vì $\Delta^k$ của từng dữ liệu bằng không.

\textbf{Bước 3. Nghiệm sửa đúng và chuỗi hữu hạn.}''',
5:r'''\textbf{Bước 1. Duhamel của nguồn cầu không đổi theo thời gian.} Li độ/vận tốc đầu bằng không, tốc độ $1$. Tại mỗi thời điểm nguồn $s$, vận tốc xung là $\chi_{B_1}$, nên đóng góp ở thời gian trễ $\tau=t-s$ là $K_1(r,\tau)$. Tích phân $s$ cho $u=J_1(r,t)$.

\textbf{Bước 2. Tính nguyên hàm ở từng giai đoạn.} Với cầu bán kính $R$, nếu $r<R$, trước $R-r$ có $K_R(s)=s$; nếu $r\ge R$, trước $r-R$ có $K_R=0$. Trong $|R-r|<s<R+r$, $K_R=(R^2-(r-s)^2)/(4r)$ là đa thức bậc hai. Sau $R+r$ đóng góp xung bằng không, nên $J_R$ giữ hằng số. Tích phân ba nhánh cho công thức dưới đây.

\textbf{Bước 3. Nghiệm và trạng thái dừng.}''',
6:r'''\textbf{Bước 1. Chồng nghiệm vận tốc và nguồn.} Hai cầu vận tốc có dấu trái nhau cho $K_1(d_+,t)-K_1(d_-,t)$. Nguồn chỉ bật khi $0<s<T$, nên phần nguồn là $\int_0^{\min(t,T)}K_1(r,t-s)ds$. Đổi $\tau=t-s$ cho hiệu hai nguyên hàm $J$.

\textbf{Bước 2. Dùng đối xứng và thời gian yêu cầu.} Ở $x=0$, khoảng cách tới hai tâm $(\pm2,0,0)$ bằng nhau, nên phần vận tốc triệt tiêu hoàn toàn; câu (a) chỉ còn nguồn với $T=1$. Câu (b) giữ hai khoảng cách khác nhau và thay $t=r$ vào biểu thức, không thay $d_\pm$ bằng $r$.

\textbf{Bước 3. Công thức áp dụng.}''',
7:r'''\textbf{Bước 1. Tích phân Poisson theo tung độ trước.} Với $c=2$, tại hoành độ $X$, đĩa ảnh hưởng có tung độ $P_y\pm h(X)$. Một dải $l<Y<v$ góp nguyên hàm $\arcsin((Y-P_y)/h)$, sau khi cắt hai cận vào $[-1,1]$. Các miền trong đề có cận tung độ tường minh theo $|X|$, nên chỉ còn một tích phân theo $X$.

\textbf{Bước 2. Hai đối xứng cần dùng.} Câu (a): trước $2t<98/\sqrt5$, cả đĩa quanh $(0,100)$ nằm trong miền $D_1$, vận tốc bằng $2$, nên $u=2t$. Câu (b): $\psi(Y,X)=-\psi(X,Y)$ và điểm quan sát $(100,100)$ bất biến khi đổi tọa độ. Đĩa và nhân Poisson cũng bất biến, nên tích phân đổi thành đối của chính nó: $u(100,100,t)=0$ với mọi $t$. Công thức tích phân dưới đây áp dụng cả cho các điểm khác khi vẽ đồ thị, nhưng tại điểm của câu (b) kết quả rút gọn là $0$.

\textbf{Bước 3. Tính các dải và dựng đồ thị.}''',
8:r'''\textbf{Bước 1. Hạ về hai bài một chiều có nguồn.} Vì $F=\chi_{[0,1]}(x)+\chi_{[0,1]}(y)$, đặt $u=U(x,t)+U(y,t)$. Mỗi $U$ có dữ liệu không, giải $U_{tt}-U_{xx}=\chi_{[0,1]}$.

\textbf{Bước 2. Tích phân hai lần hàm chỉ thị.} $H(s)=s_+-(s-1)_+$ là nguyên hàm liên tục của chỉ thị, và $Q(s)=(s_+^2-(s-1)_+^2)/2$ thỏa $Q''=\chi_{(0,1)}$. Duhamel cho $U=\frac12\int_0^t[H(x+\tau)-H(x-\tau)]d\tau=\frac12[Q(x+t)+Q(x-t)-2Q(x)]$. Khai triển $Q$ cho công thức dưới đây.

\textbf{Bước 3. Nghiệm và kiểm tra.}''',
9:r'''\textbf{Bước 1. Đạo hàm tích và Euler.} $q=x^2+y^2-t^2$, $\Box=\Delta-\partial_{tt}$, nên $\Box q=6$. Với $H$ thuần nhất bậc $m$, hạng đạo hàm chéo bằng $4j q^{j-1}(xH_x+yH_y+tH_t)=4jm q^{j-1}H$. Cộng $\Box q^j=2j(2j+1)q^{j-1}$ cho công thức tích dưới đây.

\textbf{Bước 2. Lập hệ số thay vì chép dấu in.} Đặt $u=\sum a_kq^{k+1}\Box^k\Phi$. Hệ số hạng hạ bậc là $C_k=2(k+1)(2d-2k-1)$. Vì PDE là $-\Box u=\Phi$, cần $a_0=-1/C_0$; các hạng sau triệt tiêu khi $a_k=-a_{k-1}/C_k$. Suy biểu thức giai thừa kép, có dấu âm phía ngoài và số mũ $q^{k+1}$, không phải $q^{2k+2}$.

\textbf{Bước 3. Công thức đúng, chứng minh duy nhất và nguồn cụ thể.}''',
}
suffix={
1:r'Ở (a),(c),(d), sau khi mặt cầu ra ngoài toàn bộ các miền bị chặn, đóng góp bằng $0$; ở (b),(e), miền vận tốc không bị chặn nên không suy như vậy. Tại các điểm dữ liệu liên tục, đạo hàm đầu đúng bằng chỉ thị; chuẩn hóa $\psi=1$ cho $u=t$. Các mặt tiếp xúc với biên miền là nơi cần xét vết một phía.',
2:r'Với $r>0$, công thức tích phân và bài toán cực trị một biến là biểu diễn chính xác theo tham số; các con số do mã tích phân/tối ưu trả về là xấp xỉ. Mã chia lưới thời gian, tinh chỉnh từng cực đại và cho phép tăng độ phân giải để kiểm tra hội tụ, nên không dùng một lần tối ưu cục bộ làm bằng chứng cực đại toàn cục. Ở $r=0$ công thức supremum nêu trên là tường minh, suy bằng lấy $t\uparrow R/c$. Điều kiện nón strict và biên cầu phải được giữ khi xét đạt cực đại.',
3:r'Ở $r=0$, $U^2$ là một đa thức bậc hai theo $\rho^2$ với hệ số đầu âm. Đạo hàm bằng $0$ tại $\rho^2=R^2+a^2$, nằm giữa $(R-a)^2,(R+a)^2$, nên đây là cực đại toàn cục $a/c$. Ở $r>0$, biểu thức tích phân và cực trị một biến là chính xác theo tham số; kết quả từ mã là xấp xỉ, cần tăng cả độ chính xác tích phân và số khoảng thời gian để kiểm tra ổn định.',
4:r'Để kiểm tra chuỗi ở (b), đạo hàm hai lần hạng li độ chuyển $t^{2j}/(2j)!$ thành $t^{2j-2}/(2j-2)!$; Laplace hạng trước sinh cùng $\Delta^j\varphi$. Tương tự cho vận tốc và tích phân nguồn. Chỉ hạng nguồn $j=0$ sinh $fg$, các hạng cuối mất vì $\Delta^k=0$. Tại $0$ chỉ hai hạng $j=0$ có thể cho li độ/vận tốc, nên đúng $\varphi,\psi$.',
5:r'Với $R=1$, trạng thái dừng là $(3-r^2)/6$ bên trong và $1/(3r)$ bên ngoài. Công thức Laplace hướng tâm $v_{rr}+2v_r/r$ cho $-1$ bên trong và $0$ bên ngoài; giá trị cùng đạo hàm nối tại $r=1$, nên không sinh nguồn mặt cầu. Hai dữ liệu đầu của $J$ bằng $0$ vì $J(0)=0$ và $J_t=K$, $K(r,0)=0$.',
6:r'Tại $t=0$, cả $J$ và $K$ bằng $0$; đạo hàm của phần $K$ cho đúng hiệu hai chỉ thị cầu và phần $J$ có vận tốc đầu không. Với $t=r=0$, kết quả là $0$ và dùng nhánh tâm của $J$ để tránh chia $r$. Các min/max của $K,J$ nêu trong phần kiến thức và Ví dụ 3.6.2.5 làm biểu thức câu (b) hoàn toàn tường minh.',
7:r'Với vận tốc hằng $1$, tích phân hai chiều của nhân bằng $2\pi ct$, cho $u=t$, kiểm tra hệ số $1/(4\pi)$ khi $c=2$. Đồ thị bề mặt dùng tích phân số, phải đọc tham số lưới trong mã; đường $x=y$ của câu (b) luôn bằng $0$ theo đối xứng, là một kiểm tra độc lập cho đồ thị.',
8:r'Từ $U=\frac12(Q(x+t)+Q(x-t)-2Q(x))$, có $U_{tt}-U_{xx}=Q\,'''+"''"+r'(x)=\chi_{(0,1)}(x)$. Tại $t=0$ các hạng triệt tiêu và $U_t=0$. Vì tổng không có đạo hàm chéo giữa $x,y$, PDE hai chiều có đúng hai nguồn. Công thức đúng theo nghĩa phân phối cả tại các đường cận chạm $0,1$.',
9:r'Đạo hàm biên chuyển động trong năng lượng ở (ii) có tốc độ bán kính $-1$, nên hạng biên mang dấu âm. Vết $u(r,-r)=0$ cho $u_r-u_t=0$; thế vào thông lượng triệt tiêu bình phương. Với $\Phi=xyt$, tính trực tiếp $u=-[x^3yt+xy^3t-xyt^3]/18$: $u_{tt}=xyt/3$, $u_{xx}=-xyt/3$, $u_{yy}=-xyt/3$, suy hiệu bằng $xyt$. Hệ số $-1/18$ và dấu đã được kiểm tra độc lập.',
}
parts=[]
for n in range(1,10):
    ident=f'BT_3_6_3_{n:02}'; body=old[ident]
    parts.append('%ID '+ident+'\n'+prefix[n]+'\n\n'+body+'\n\n'+r'\textbf{Bước 4. Đối chiếu và kết luận.} '+suffix[n].replace(r"v\,'",r"v'").replace(r"Q\,''",r"Q''"))
(r/'chapter3_space.tex').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('9 multidimensional-wave derivations')
