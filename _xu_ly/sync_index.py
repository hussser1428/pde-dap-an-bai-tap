from pathlib import Path
import json,csv,re,html
r=Path(__file__).parent.parent/'PDE_Tach_bai_va_loi_giai'
rows=json.loads((r/'manifest.json').read_text(encoding='utf-8'))
with (r/'Muc_luc.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Mã','Mục','Bài','Trang sách từ','Trang sách đến','Lời giải thêm (trang)','Tình trạng','Markdown','PDF'])
    for i in rows:w.writerow([i['id'],i['section'],i['number'],i['start'][0]-1,i['end'][0]-1,i['solution_pages'],i['status'],Path(i['file']).with_suffix('.md').as_posix(),i['file']])
p=r/'Muc_luc.html';s=p.read_text(encoding='utf-8')
s=s.replace('Mỗi bài đánh số chính là một PDF;','Mỗi bài đánh số chính có một file Markdown và một PDF;')
s=s.replace('href="00_Ly_thuyet_trich_tu_sach.pdf"','href="00_Kien_thuc_va_phuong_phap.md"')
by_id={row['id']:row for row in rows}
def update_row(match):
    fragment=match[0]
    ident=re.search(r'<td>((?:VD|BT|NC)_[^<]+)</td>',fragment)
    if ident and ident[1] in by_id:
        fragment=re.sub(r'<td>[^<]*</td></tr>$', '<td>'+html.escape(by_id[ident[1]]['status'])+'</td></tr>',fragment)
    return fragment
s=re.sub(r'<tr>.*?</tr>',update_row,s,flags=re.S)
p.write_text(s,encoding='utf-8')
print('CSV/index synchronized')
