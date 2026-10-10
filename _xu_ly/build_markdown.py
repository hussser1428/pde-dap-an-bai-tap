from pathlib import Path
import re,json,html
import fitz
from PIL import Image
from method_notes import NOTES,key
from chapter1_notes import NOTES as CH1_NOTES, note_for
from chapter2_notes import NOTES as CH2_NOTES, note_for as note_for_ch2
from chapter3_notes import NOTES as CH3_NOTES, note_for as note_for_ch3
from chapter4_notes import NOTES as CH4_NOTES, note_for as note_for_ch4
r=Path(__file__).resolve().parent;root=r.parent;out=root/'PDE_Tach_bai_va_loi_giai'
inv=json.loads((r/'inventory.json').read_text(encoding='utf-8'))
manifest={i['id']:i for i in json.loads((out/'manifest.json').read_text(encoding='utf-8'))}
solutions={}
for p in sorted(r.glob('loi_giai*.tex')):
    for m in re.finditer(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',p.read_text(encoding='utf-8'),re.M|re.S):
        assert m[1] not in solutions,m[1];solutions[m[1]]=m[2].strip()
src=fitz.open(root/'pde bài tập.pdf')
images=out/'Hinh_de_goc';images.mkdir(exist_ok=True)
label={'VD':'Ví dụ','BT':'Bài tập thực hành','NC':'Bài nâng cao'}
def styled(tex,command,mark):
    # A heading can contain math with nested braces, e.g. e^{x+3y}.
    prefix='\\'+command+'{'
    while prefix in tex:
        start=tex.index(prefix);pos=start+len(prefix);begin=pos;depth=1
        while pos<len(tex) and depth:
            if tex[pos]=='{' and (pos==0 or tex[pos-1]!='\\'):depth+=1
            if tex[pos]=='}' and (pos==0 or tex[pos-1]!='\\'):depth-=1
            pos+=1
        if depth:break
        tex=tex[:start]+mark+tex[begin:pos-1]+mark+tex[pos:]
    return tex
def markdown(tex):
    tex=re.sub(r'\\begin\{center\}.*?\\end\{center\}','',tex,flags=re.S)
    tex=re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}','',tex)
    tex=tex.replace(r'\[','\n$$\n').replace(r'\]','\n$$\n')
    for env in ('align*','gather*'):
        mathenv='aligned' if env=='align*' else 'gathered'
        tex=tex.replace(r'\begin{'+env+'}', '\n$$\n'+r'\begin{'+mathenv+'}')
        tex=tex.replace(r'\end{'+env+'}',r'\end{'+mathenv+'}'+'\n$$\n')
    for command,mark in [('textbf','**'),('emph','*'),('textit','*')]:
        tex=styled(tex,command,mark)
    # TeX quotation marks belong to prose; doubled primes in math are derivatives.
    parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^$]*?\$)',tex)
    tex=''.join(p if j%2 else p.replace('``','“').replace("''",'”')
                for j,p in enumerate(parts))
    # Expand inline subquestions into readable paragraphs without touching displayed cases.
    chunks=tex.split('$$')
    for j in range(0,len(chunks),2):
        chunks[j]=re.sub(r'(?m)^\s*(\((?:[a-h]|i{1,3}|iv|v|vi{1,3}|ix)\))(?=\s)',r'\n\n**Ý \1.** ',chunks[j])
    tex='$$'.join(chunks)
    return re.sub(r'\n{3,}','\n\n',tex).strip()
texts=[];rows=[]
for item in sorted(inv,key=lambda i:tuple(i['start'])):
    id=item['id'];meta=manifest[id];folder=out/Path(meta['file']).parent
    text=f'# {label[item["kind"]]} {item["number"]} — Mục {item["section"]}\n\n'
    text+=f'**Mã:** `{id}` · **Trang sách:** {item["start"][0]-1}–{item["end"][0]-1}\n\n'
    text+=f'[← Mục lục](../MUC_LUC.md) · [Bản PDF của bài]({id}.pdf)\n\n'
    text+='## Đề bài'+(' và phần trình bày có sẵn trong sách' if item['kind']=='VD' else '')+'\n\n'
    k=0
    for p in range(item['start'][0],item['end'][0]+1):
        a=item['start'][1] if p==item['start'][0] else 85
        b=item['end'][1] if p==item['end'][0] else 1268
        if b-a<12:continue
        clip=fitz.Rect(52,(a-5)/1.6,552,(b-7)/1.6)
        if clip.height<4:continue
        k+=1;name=f'{id}_{k:02}.png';target=images/name
        if not target.exists():
            pix=src[p-1].get_pixmap(matrix=fitz.Matrix(160/72,160/72),clip=clip)
            Image.frombytes('RGB',[pix.width,pix.height],pix.samples).save(target,optimize=True)
        text+=f'![Đề gốc, trang sách {p-1}](../Hinh_de_goc/{name})\n\n'
    if id!='BT_5_2_3_02':
        note=note_for(item) if item['section'].startswith('1.') else note_for_ch2(item) if item['section'].startswith('2.') else note_for_ch3(item) if item['section'].startswith('3.') else note_for_ch4(item) if item['section'].startswith('4.') else NOTES[key(item)]
        text+='## Kiến thức và trình tự giải\n\n'+note+'\n\n'
    if id in solutions:
        body=markdown(solutions[id])
        text+='## Lời giải áp dụng cho bài\n\n'+body+'\n\n'
    else:
        text+='## Lời giải trong tài liệu\n\nLời giải/đáp án có sẵn được giữ đầy đủ trong ảnh phía trên. Phần kiến thức vừa nêu giải thích trình tự phương pháp để đối chiếu từng phép biến đổi của ví dụ.\n\n'
    graph=out/'Do_thi'/(id+'.png')
    if graph.exists():text+=f'## Đồ thị minh họa\n\n![Đồ thị của {id}](../Do_thi/{id}.png)\n\n'
    characteristics=out/'Do_thi'/(id+'_characteristics.png')
    if characteristics.exists():text+=f'![Hai họ đặc trưng và miền truyền sóng của {id}](../Do_thi/{id}_characteristics.png)\n\n'
    if id in ('BT_3_6_3_02','BT_3_6_3_03'):text+='![Minh họa nón và xuyến với bộ tham số ghi trên đồ thị](../Do_thi/cone_torus.png)\n\n'
    if id in solutions and item['kind']!='VD' and not re.search('không có đề|không có nội dung',solutions[id]):
        text+='## Đối chiếu kết quả\n\n'
        text+='Khi sử dụng kết quả, kiểm tra đồng thời phương trình, dữ liệu ban đầu/biên và miền được nêu trong lời giải. Các điều kiện về tính trơn, nghiệm thực, tồn tại hoặc duy nhất là một phần của kết luận; không bỏ chúng khi ghi đáp án.\n'
    target=folder/(id+'.md');target.write_text(text,encoding='utf-8')
    relative=target.relative_to(out).as_posix();rows.append((item,meta,relative))
    combined=text.replace('../Hinh_de_goc/','PDE_Tach_bai_va_loi_giai/Hinh_de_goc/').replace('../Do_thi/','PDE_Tach_bai_va_loi_giai/Do_thi/')
    combined=combined.replace('[← Mục lục](../MUC_LUC.md)',f'[File riêng](PDE_Tach_bai_va_loi_giai/{relative})')
    combined=combined.replace(f'({id}.pdf)',f'(PDE_Tach_bai_va_loi_giai/{meta["file"]})')
    texts.append(combined)
    if len(rows)%60==0:print('MARKDOWN',len(rows),flush=True)
index='# Mục lục ví dụ và bài tập PDE\n\n**336 mục:** 99 ví dụ, 233 bài thực hành, 4 bài nâng cao. Mỗi bài có một file **Markdown** đọc trực tiếp trong IDE và một file PDF. Các ý nhỏ giữ chung trong bài.\n\nMở một file `.md`, sau đó dùng **Markdown Preview** (trong VS Code: `Ctrl+Shift+V`) để xem ảnh và công thức. Công thức dùng `$...$` và `$$...$$`; đề gốc giữ bằng ảnh để không sai ký hiệu do nhận dạng scan.\n\n[Kiến thức chung](00_Kien_thuc_va_phuong_phap.md) · [Hướng dẫn](HUONG_DAN.md) · [PDF lời giải bổ sung](00_Tat_ca_loi_giai_bo_sung.pdf)\n\n'
chapter=None
review_file=r/'ra_soat_buoc_trung_gian_123.json'
if review_file.exists():
    review=json.loads(review_file.read_text(encoding='utf-8'))
    expanded=sum(i['status']=='expanded' for i in review)
    index+=f'**Bổ sung phép tính trung gian Chương 1–3:** đã rà {len(review)} mục và mở rộng {expanded} lời giải, gồm tích phân từng phần, khử tham số, gom hệ số đổi biến, nhân ma trận, thông lượng Green và định thức dầm. Phần kiến thức chung cũng được bổ sung cách thực hiện các phép tính này. Các dấu đạo hàm kép và cấp bốn được giữ đúng trong Markdown.\n\n'
for item,meta,path in rows:
    ch=item['section'].split('.')[0]
    if ch!=chapter:
        chapter=ch;index+=f'\n## Chương {ch}\n\n| Bài | Mở Markdown | Trang sách |\n|---|---|---|\n'
        if ch=='1':
            index=index.replace('## Chương 1\n\n| Bài', '## Chương 1\n\nCả 93 mục đã có phần kiến thức theo từng bước và lời giải bằng chữ. Lời giải trình bày phép biến đổi cụ thể, cách dùng dữ liệu, kiểm tra nghiệm và các trường hợp đặc biệt. Bản PDF và nguồn LaTeX đã được cập nhật cùng nội dung.\n\n| Bài')
        if ch=='2':
            index=index.replace('## Chương 2\n\n| Bài', '## Chương 2\n\nCả 27 mục (9 ví dụ, 18 bài tập) đã có kiến thức và lời giải chi tiết: đổi tọa độ, tính đạo hàm, phân loại, dạng chính tắc, dùng dữ liệu, kiểm tra và miền duy nhất. Markdown, PDF và nguồn LaTeX đã đồng bộ; các sai dấu hoặc ký hiệu không rõ trong đề được ghi riêng.\n\n| Bài')
    if ch=='3' and item['id']=='VD_3_1_2_01':
        index=index.replace('## Chương 3\n\n| Bài', '## Chương 3\n\nCả 85 mục (23 ví dụ, 62 bài tập) đã có kiến thức và lời giải theo từng bước: d’Alembert, phản xạ, sóng chia đoạn, Fourier, nguồn và cộng hưởng, năng lượng, phương trình dầm, Kirchhoff–Poisson. Mỗi bài có phép tính riêng, kiểm tra dữ liệu và mức trơn; các sai công thức được ghi rõ. Markdown, PDF và LaTeX đã đồng bộ.\n\n| Bài')
    if ch=='4' and item['id']=='VD_4_1_2_01':
        index=index.replace('## Chương 4\n\n| Bài', '## Chương 4\n\nCả 50 mục (15 ví dụ, 35 bài tập) đã có kiến thức từng bước và lời giải chi tiết, gồm tính hệ số Fourier, chuẩn hàm riêng Robin, khử biên, tích phân Duhamel, rào so sánh, nhân Gauss, Fourier bậc ba/bốn và kiểm tra dữ liệu. Phép tính sơ cấp được thực hiện đến kết quả; chuỗi và tích phân không sơ cấp được giải thích cách lập và kiểm tra. Các lỗi đề hoặc điều kiện còn thiếu được ghi rõ. Markdown, PDF và LaTeX đã đồng bộ.\n\n| Bài')
    index+=f'| `{item["id"]}` | [{label[item["kind"]]} {item["number"]} · Mục {item["section"]}]({path}) | {item["start"][0]-1}–{item["end"][0]-1} |\n'
(out/'MUC_LUC.md').write_text(index,encoding='utf-8')
rootindex=index.replace('](0','](PDE_Tach_bai_va_loi_giai/0').replace('](HUONG_DAN.md)','](PDE_Tach_bai_va_loi_giai/HUONG_DAN.md)')
for _,_,p in rows:rootindex=rootindex.replace(']('+p+')','](PDE_Tach_bai_va_loi_giai/'+p+')')
(root/'MUC_LUC_PDE.md').write_text(rootindex,encoding='utf-8')
(root/'loi_giai_tong_hop.md').write_text('# Đề và lời giải PDE — bản Markdown tổng hợp\n\n[Mục lục và từng file riêng](MUC_LUC_PDE.md)\n\nBản này gồm toàn bộ 336 mục đã tách. Với các ví dụ đã giải trong sách, lời giải gốc được giữ bằng ảnh. Với bài cần bổ sung, có phương pháp, công thức và phân tích điều kiện.\n\n---\n\n'+'\n\n---\n\n'.join(texts),encoding='utf-8')
(out/'00_Kien_thuc_va_phuong_phap.md').write_text('# Kiến thức và phương pháp dùng trong lời giải\n\n## Chương 1 — Hướng dẫn chi tiết\n\n'+'\n\n---\n\n'.join(CH1_NOTES.values())+'\n\n## Chương 2 — Hướng dẫn chi tiết\n\n'+'\n\n---\n\n'.join(CH2_NOTES.values())+'\n\n## Chương 3 — Hướng dẫn chi tiết\n\n'+'\n\n---\n\n'.join(CH3_NOTES.values())+'\n\n## Chương 4 — Hướng dẫn chi tiết\n\n'+'\n\n---\n\n'.join(CH4_NOTES.values())+'\n\n## Các phương pháp ở chương sau\n\n'+'\n\n---\n\n'.join(v for k,v in NOTES.items() if k not in ('classification','direct','linear_char','quasi_char','charpit','shock','heat','maximum_heat','heat_whole')),encoding='utf-8')
guide=out/'HUONG_DAN.md';old=guide.read_text(encoding='utf-8')
old=old.replace('Mở **Muc_luc.html** để tìm và mở từng bài.','Mở **MUC_LUC.md** để đọc ngay trong IDE; mỗi bài có file Markdown gồm đề gốc, phương pháp, lời giải và đồ thị nếu có. Dùng Markdown Preview để hiển thị công thức. **Muc_luc.html** vẫn là mục lục dùng trong trình duyệt.')
guide.write_text(old,encoding='utf-8')
ht=out/'Muc_luc.html';s=ht.read_text(encoding='utf-8')
for item,meta,path in rows:
    mdlink=f'<a href="{path}">Markdown</a> · '
    if mdlink not in s:s=s.replace(f'<a href="{meta["file"]}">',mdlink+f'<a href="{meta["file"]}">')
ht.write_text(s,encoding='utf-8')
(r/'markdown_manifest.json').write_text(json.dumps([p for _,_,p in rows],ensure_ascii=False,indent=2),encoding='utf-8')
print('COMPLETE MD',len(rows),'typed solutions',len(solutions),flush=True)
