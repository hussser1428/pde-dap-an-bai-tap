from pathlib import Path
p=Path(__file__).parent/'loi_giai_3a.tex'
s=p.read_text(encoding='utf-8')
a=s.index('(ii) Với $a=2,\\alpha=3,F=1,f=g=h=0$')
b=s.index('%ID BT_3_1_3_10',a)
s=s[:a]+r'''(ii) Với $a=2,\alpha=3,F=1,f=g=h=0$, chọn nghiệm riêng $-x^2/8$, vì $\partial_{tt}(-x^2/8)-4\partial_{xx}(-x^2/8)=1$. Viết $u=-x^2/8+F_1(x+2t)+G_1(x-2t)$. Dữ liệu đầu buộc $F_1(s)=G_1(s)=s^2/16$ khi $s>0$ (bỏ hai hằng triệt tiêu). Tại $t=3x$, $-x^2/8+49x^2/16+G_1(-5x)=0$, nên $G_1(s)=-47s^2/400$ khi $s<0$. Do đó
\[u=\begin{cases}t^2/2,&t\le x/2,\\-x^2/8+(x+2t)^2/16-47(x-2t)^2/400,&x/2<t<3x.\end{cases}\]
Giá trị và đạo hàm cấp 1 ghép tại $t=x/2$, nhưng đạo hàm cấp 2 không ghép. Đây là nghiệm yếu liên tục khả vi và cổ điển từng miền; không có nghiệm $C^2$ trên toàn miền với các dữ kiện này.
''' +s[b:]
p.write_text(s,encoding='utf-8')
