from pathlib import Path
import json,re,shutil,os,argparse
import fitz
from chapter1_notes import latex_note
from chapter2_notes import latex_note as latex_note_ch2
from chapter3_notes import latex_note as latex_note_ch3
from chapter4_notes import latex_note as latex_note_ch4
parser=argparse.ArgumentParser()
parser.add_argument('--chapter', help='Chỉ cập nhật các PDF và nguồn riêng của chương được chọn')
args=parser.parse_args()
r=Path(__file__).parent;root=r.parent;out=root/'PDE_Tach_bai_va_loi_giai'
src=fitz.open(r/'master.pdf');starts={}
for page in src:
    m=re.search(r'^(?:VD|BT|NC)_[\w]+',page.get_text(),re.M)
    if m:starts[m[0]]=page.number
sols=json.loads((r/'solutions.json').read_text(encoding='utf-8'))
assert set(starts)==set(sols)
rows=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
for row in rows:
    id=row['id']
    if args.chapter and row['section'].split('.')[0]!=args.chapter:continue
    if id not in starts:continue
    start=starts[id];end=min([n for n in starts.values() if n>start]+[len(src)])
    file=out/row['file'];old=fitz.open(file);new=fitz.open()
    new.insert_pdf(old,from_page=0,to_page=row['original_pages']-1);new.insert_pdf(src,from_page=start,to_page=end-1)
    new.set_metadata(old.metadata);old.close()
    temp=file.with_suffix('.new.pdf');new.save(temp,garbage=4,deflate=True);new.close();os.replace(temp,file)
    row['solution_pages']=end-start;row['status']='Có lời giải bổ sung'
    if id=='BT_5_2_3_02':row['status']='Mục đánh số trống — đã ghi chú'
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(r/'master.pdf',out/'00_Tat_ca_loi_giai_bo_sung.pdf')
shutil.copy2(r/'master.pdf',root/'loi_giai_tong_hop.pdf')
shutil.copy2(r/'master.tex',root/'loi_giai_tong_hop.tex')
editable=out/'Nguon_loi_giai';pre=(r/'master.tex').read_text(encoding='utf-8').split('\\begin{document}')[0]
for id,body in sols.items():
    item=next(i for i in rows if i['id']==id)
    if args.chapter and item['section'].split('.')[0]!=args.chapter:continue
    note=latex_note(item) if item['section'].startswith('1.') else latex_note_ch2(item) if item['section'].startswith('2.') else latex_note_ch3(item) if item['section'].startswith('3.') else latex_note_ch4(item) if item['section'].startswith('4.') else None
    knowledge=r'\subsection*{Kiến thức và trình tự giải}'+'\n'+note+'\n'+r'\subsection*{Lời giải áp dụng cho bài}'+'\n' if note else ''
    tex=pre+r'\begin{document}'+'\n'+r'\section*{'+id.replace('_',r'\_')+' — Lời giải bổ sung}\n'+knowledge+body+r'\end{document}'
    (editable/(id+'.tex')).write_text(tex.replace('_xu_ly/graphs/','Do_thi/'),encoding='utf-8')
(editable/'Tat_ca_loi_giai.tex').write_text((r/'master.tex').read_text(encoding='utf-8').replace('_xu_ly/graphs/','Do_thi/'),encoding='utf-8')
for p in (r/'graphs').glob('*.png'):shutil.copy2(p,out/'Do_thi'/p.name)
shutil.copy2(r/'extra_graphs.py',out/'Ma_ve_do_thi'/'extra_graphs.py')
if args.chapter=='3':
    for name in ('wave_graphs.py','chapter3_graphs.py'):
        shutil.copy2(r/name,out/'Ma_ve_do_thi'/name)
if args.chapter=='4':
    shutil.copy2(r/'chapter4_graphs.py',out/'Ma_ve_do_thi'/'chapter4_graphs.py')
print('REFRESHED',len(starts),'solutions',len(src),'pages')
