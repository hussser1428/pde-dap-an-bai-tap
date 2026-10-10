from pathlib import Path
import re
r=Path(__file__).parent
p=r/'loi_giai_2.tex';s=p.read_text(encoding='utf-8')
s=s.replace('một nghiệm là $u=(x+y)e^{-(5x-3y)/8}$.','hai nghiệm khác nhau là $u_1=(x+y)e^{-(5x-3y)/8}$ và $u_2=u_1+(5x-3y)^2$. Hạng cộng có giá trị và đạo hàm cần thiết bằng 0 trên đặc trưng dữ liệu.')
s=s.replace('một nghiệm là $e^x/4+x(x+2y)/4+(x+2y)/2$.','hai nghiệm là $u_1=e^x/4+x(x+2y)/4+(x+2y)/2$ và $u_2=u_1+(x+2y)^2$; hạng thêm không đổi các vết đã cho.')
s=s.replace('Thí dụ $u=e^x+e^{2x/5}$.','Hai nghiệm: $u_1=e^x+e^{2x/5}$ và $u_2=u_1+x+5y$.')
s=s.replace('Có vô số nghiệm. Công thức chỉ xét','Hai lựa chọn $G(s)=\\lambda s$ và $G(s)=\\lambda s+s^2$ cho hai nghiệm khác nhau cùng dữ liệu. Công thức chỉ xét')
p.write_text(s,encoding='utf-8')
p=r/'loi_giai_6.tex';s=p.read_text(encoding='utf-8').replace('$b_N=1$, các $b_n$ khác 0.','$b_N=1$, $b_n=0$ với $n\\ne N$.');p.write_text(s,encoding='utf-8')
p=r/'loi_giai_3_graph.tex';s=p.read_text(encoding='utf-8')
# Split the only long display reported by XeLaTeX.
s=s.replace(r';\ J(r)=J(2\pi-r)',r'.\]\[J(r)=J(2\pi-r)')
p.write_text(s,encoding='utf-8')
