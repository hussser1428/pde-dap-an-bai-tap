from pathlib import Path
import json,re,io,html,csv,shutil,zipfile
import fitz
root=Path(__file__).resolve().parent.parent
r=root/'_xu_ly';out=root/'PDE_Tach_bai_va_loi_giai';out.mkdir(exist_ok=True)
src=fitz.open(root/'pde bài tập.pdf');sol=fitz.open(r/'master.pdf')
inv=json.loads((r/'inventory.json').read_text(encoding='utf-8'))
solutions=json.loads((r/'solutions.json').read_text(encoding='utf-8'))
font='C:/Windows/Fonts/arial.ttf'
starts={}
for p in sol:
    m=re.search(r'^(?:VD|BT|NC)_[\w]+',p.get_text(),re.M)
    if m: starts[m[0]]=p.number
assert len(starts)==len(solutions),(len(starts),len(solutions))
ends={k:next((v for v in sorted(starts.values()) if v>p),len(sol)) for k,p in starts.items()}
chapters={'1':'01_Phuong_trinh_cap_1','2':'02_Phuong_trinh_cap_2','3':'03_Phuong_trinh_song','4':'04_Phuong_trinh_nhiet','5':'05_Phuong_trinh_Laplace','6':'06_Chuoi_Fourier'}
names={'VD':'Ví dụ','BT':'Bài tập thực hành','NC':'Bài nâng cao'}
def add_original(doc,p,a,b,title):
    if b-a<12:return
    clip=fitz.Rect(52,max(0,(a-5)/1.6),552,min(src[p-1].rect.height,(b-7)/1.6))
    if clip.height<4:return
    pix=src[p-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=clip)
    page=doc.new_page(width=595.276,height=841.89)
    page.insert_font(fontname='vn',fontfile=font)
    page.insert_text((30,27),title,fontname='vn',fontsize=11)
    page.insert_text((30,44),f'Đề/lời giải gốc · Trang sách {p-1} (trang PDF {p})',fontname='vn',fontsize=9,color=(.35,.35,.35))
    scale=min(1.05,535/clip.width,755/clip.height)
    w,h=clip.width*scale,clip.height*scale
    page.insert_image(fitz.Rect((595-w)/2,63,(595+w)/2,63+h),stream=pix.tobytes('jpg',jpg_quality=94))
    page.insert_text((30,823),'Trích từ “Phương trình đạo hàm riêng: Ví dụ và Bài tập” · Giữ nguyên bản in',fontname='vn',fontsize=8,color=(.4,.4,.4))
rows=[]
for i in sorted(inv,key=lambda i:tuple(i['start'])):
    id=i['id'];ch=i['section'].split('.')[0];folder=out/chapters[ch];folder.mkdir(exist_ok=True)
    title=f"{names[i['kind']]} {i['number']} — Mục {i['section']}"
    doc=fitz.open()
    for p in range(i['start'][0],i['end'][0]+1):
        a=i['start'][1] if p==i['start'][0] else 85
        b=i['end'][1] if p==i['end'][0] else 1268
        add_original(doc,p,a,b,title)
    original_n=len(doc)
    if id in starts:doc.insert_pdf(sol,from_page=starts[id],to_page=ends[id]-1)
    assert len(doc)>0,id
    doc.set_metadata({'title':title,'subject':id+'; đề gốc và lời giải','author':'Trích đề từ sách; lời giải bổ sung do trợ lý biên soạn'})
    file=folder/(id+'.pdf');doc.save(file,garbage=4,deflate=True);doc.close()
    status='Có lời giải bổ sung' if id in starts else 'Có đáp án/lời giải trong bản gốc'
    if id=='BT_5_2_3_02':status='Mục đánh số trống — đã ghi chú'
    rows.append({**i,'title':title,'file':file.relative_to(out).as_posix(),'original_pages':original_n,'solution_pages':ends[id]-starts[id] if id in starts else 0,'status':status})
    if len(rows)%50==0:print('BUILT',len(rows),flush=True)
# Collect the theory remaining between the exercises/examples; do not copy full source.
theory=fitz.open()
for p in range(4,276):
    covered=[]
    for i in inv:
        if i['start'][0]<=p<=i['end'][0]:
            a=i['start'][1] if p==i['start'][0] else 85
            b=i['end'][1] if p==i['end'][0] else 1268
            if b>a:covered.append((max(85,a),min(1268,b)))
    cursor=85
    for a,b in sorted(covered):
        if a-cursor>50:add_original(theory,p,cursor,a,'Kiến thức và công thức tham chiếu')
        cursor=max(cursor,b)
    if 1268-cursor>50:add_original(theory,p,cursor,1268,'Kiến thức và công thức tham chiếu')
theory.save(out/'00_Ly_thuyet_trich_tu_sach.pdf',garbage=4,deflate=True);theory.close()
appendix=fitz.open()
for p in range(276,286):add_original(appendix,p,1030 if p==276 else 85,1268,'Phụ lục lời giải có sẵn trong sách')
appendix.save(out/'00_Phu_luc_loi_giai_goc.pdf',garbage=4,deflate=True);appendix.close()
editable=out/'Nguon_loi_giai';editable.mkdir(exist_ok=True)
pre=(r/'master.tex').read_text(encoding='utf-8').split('\\begin{document}')[0]
for id,body in solutions.items():
    s=pre+r'\begin{document}'+'\n'+r'\section*{'+id.replace('_',r'\_')+' — Lời giải bổ sung}\n'+body+r'\end{document}'
    s=s.replace('_xu_ly/graphs/','Do_thi/')
    (editable/(id+'.tex')).write_text(s,encoding='utf-8')
(editable/'Tat_ca_loi_giai.tex').write_text((r/'master.tex').read_text(encoding='utf-8').replace('_xu_ly/graphs/','Do_thi/'),encoding='utf-8')
shutil.copy2(r/'master.pdf',out/'00_Tat_ca_loi_giai_bo_sung.pdf')
graphs=out/'Do_thi';graphs.mkdir(exist_ok=True)
for f in (r/'graphs').glob('*.png'):shutil.copy2(f,graphs/f.name)
scripts=out/'Ma_ve_do_thi';scripts.mkdir(exist_ok=True)
for f in ['wave_graphs.py','extra_graphs.py']:shutil.copy2(r/f,scripts/f)
(scripts/'requirements.txt').write_text('numpy\nscipy\nmatplotlib\n',encoding='utf-8')
with (out/'Muc_luc.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['Mã','Loại','Mục','Số bài','Trang sách từ','Trang sách đến','Đề gốc (số trang)','Lời giải thêm (số trang)','Tình trạng','Đường dẫn'])
    for i in rows:w.writerow([i['id'],names[i['kind']],i['section'],i['number'],i['start'][0]-1,i['end'][0]-1,i['original_pages'],i['solution_pages'],i['status'],i['file']])
table=''.join(f'<tr><td>{html.escape(i["id"])}</td><td><a href="{html.escape(i["file"])}">{html.escape(i["title"])}</a></td><td>{i["start"][0]-1}–{i["end"][0]-1}</td><td>{html.escape(i["status"])}</td></tr>' for i in rows)
page='''<!doctype html><html lang="vi"><meta charset="utf-8"><title>Mục lục bài tập PDE</title><style>body{font:16px Arial;max-width:1200px;margin:36px auto;padding:0 20px;color:#162738}h1{font-size:28px}input{padding:12px;width:95%;margin:18px 0}table{border-collapse:collapse;width:100%}td,th{padding:11px;border-bottom:1px solid #ddd;text-align:left}a{color:#0564b7}small{color:#5e6c7b}</style><h1>Ví dụ và bài tập PDE — từng file riêng</h1><p>336 mục: 99 ví dụ, 233 bài thực hành, 4 bài nâng cao. Mỗi bài đánh số chính là một PDF; các ý nhỏ ở chung trong bài. Đề và lời giải có sẵn được giữ dưới dạng ảnh trích từ sách. Lời giải bổ sung nằm sau đề.</p><p><a href="00_Ly_thuyet_trich_tu_sach.pdf">Kiến thức và công thức</a> · <a href="00_Tat_ca_loi_giai_bo_sung.pdf">Toàn bộ lời giải bổ sung</a> · <a href="00_Phu_luc_loi_giai_goc.pdf">Phụ lục gốc</a> · <a href="HUONG_DAN.md">Hướng dẫn và lưu ý</a></p><p><small>Đề sai dấu, thiếu dữ kiện, mục trống hoặc yêu cầu không đúng được nêu rõ trong lời giải; phiên bản sửa được phân biệt với bản in.</small></p><input id="q" placeholder="Tìm mã bài, chương, mục hoặc tình trạng…" oninput="document.querySelectorAll('tbody tr').forEach(r=>r.hidden=!r.textContent.toLowerCase().includes(this.value.toLowerCase()))"><table><thead><tr><th>Mã</th><th>Mở PDF</th><th>Trang sách</th><th>Tình trạng</th></tr></thead><tbody>'''+table+'</tbody></table></html>'
(out/'Muc_luc.html').write_text(page,encoding='utf-8')
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'HUONG_DAN.md').write_text('''# Ví dụ và bài tập PDE đã tách

Mở **Muc_luc.html** để tìm và mở từng bài. Có 336 file bài riêng: 99 ví dụ, 233 bài thực hành và 4 bài nâng cao. Mỗi số bài chính là một file; các phần (a), (b), (i), (ii)… giữ chung để không mất mối liên hệ và dữ kiện chung. Ba bài lý thuyết sau mục 3.2.3 dùng mã LT. Mục 5.2.3 bài 2 chỉ có số thứ tự trong sách, không có đề; file đó ghi rõ tình trạng.

Trong mỗi PDF, phần đầu là ảnh cắt của đề và lời giải gốc nếu có; phần sau là lời giải bổ sung được soạn lại với công thức rõ nét. Số trang sách bằng số trang PDF nguồn trừ 1 vì có trang bìa. Các trang lý thuyết cần tra theo số phương trình được gom trong **00_Ly_thuyet_trich_tu_sach.pdf**. Phụ lục đáp án gốc được giữ riêng vì số mục trong phụ lục có chỗ không khớp đánh số trong thân sách.

Lời giải dùng đặc trưng/Charpit, điều kiện Rankine–Hugoniot, dạng chính tắc, d’Alembert/Kirchhoff/Poisson, tách biến Fourier, Duhamel, hàm Green, năng lượng và nguyên lý cực đại như trong sách. Đề mâu thuẫn, thiếu điều kiện, sai dấu hoặc phát biểu không đúng được phân tích và có phiên bản sửa khi xác định được; không mặc nhiên đổi đề. Khi dữ liệu thiếu thật sự, file ghi không xác định duy nhất hoặc không có nghiệm trong lớp đã yêu cầu.

**00_Tat_ca_loi_giai_bo_sung.pdf** gom các lời giải bổ sung để đọc liên tục. Thư mục **Nguon_loi_giai** chứa mã LaTeX có thể chỉnh sửa; biên dịch bằng XeLaTeX từ thư mục gốc này, ví dụ `xelatex Nguon_loi_giai/BT_4_1_3_01.tex`. Các đồ thị nằm ở **Do_thi**. Mã Python ở **Ma_ve_do_thi**, cần numpy, scipy, matplotlib; đây là minh họa và công cụ kiểm tra số. Đồ thị Poisson hai chiều dùng tích phân số nên có sai số, không thay thế biểu thức nghiệm chính xác. Bài nón và xuyến có tham số tùy ý: hàm `cone_u`, `torus_u`, `maximum` cho phép nhập tham số để tính cực đại số; tăng độ chia để kiểm tra hội tụ.

Bản PDF nguồn không bị thay đổi. Các lời giải bổ sung là bản biên soạn học tập, không phải lời giải chính thức của tác giả. Những phần giải dài được trình bày ở dạng chuỗi hội tụ hoặc tích phân xác định khi đây là dạng tự nhiên của nghiệm.
''',encoding='utf-8')
print('COMPLETE',len(rows),'items;',sum(i['solution_pages']>0 for i in rows),'supplemented',flush=True)
