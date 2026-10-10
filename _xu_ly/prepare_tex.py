from pathlib import Path
import re,json
from chapter1_notes import latex_note
from chapter2_notes import latex_note as latex_note_ch2
from chapter3_notes import latex_note as latex_note_ch3
from chapter4_notes import latex_note as latex_note_ch4
r=Path(__file__).resolve().parent
inv=json.loads((r/'inventory.json').read_text(encoding='utf-8'))
solutions={}
for p in sorted(r.glob('loi_giai*.tex')):
    for m in re.finditer(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',p.read_text(encoding='utf-8'),re.M|re.S):
        assert m[1] not in solutions,m[1]
        solutions[m[1]]=m[2].strip()
assert all(i['id'] in solutions for i in inv if i['kind']!='VD')
pre=r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec,amsmath,amssymb,graphicx}
\usepackage[margin=18mm]{geometry}
\setmainfont{Times New Roman}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\allowdisplaybreaks
\sloppy
\emergencystretch=2em
\begin{document}
'''
parts=[]
for i in inv:
    id=i['id']
    if id not in solutions:continue
    extra=r/'graphs'/(id+'.png')
    if extra.exists() and 'includegraphics' not in solutions[id]:
        solutions[id]+='\n'+r'\begin{center}\includegraphics[width=.97\linewidth,height=11cm,keepaspectratio]{_xu_ly/graphs/'+id+r'.png}\end{center}'+'\n'+r'\textit{Đồ thị minh họa; với nghiệm số, xem phương pháp và tham số trong mã Python kèm theo.}'
    characteristics=r/'graphs'/(id+'_characteristics.png')
    if characteristics.exists():
        solutions[id]+='\n'+r'\begin{center}\includegraphics[width=.97\linewidth,height=11cm,keepaspectratio]{_xu_ly/graphs/'+id+r'_characteristics.png}\end{center}'
    if id in ('BT_3_6_3_02','BT_3_6_3_03'):
        solutions[id]+='\n'+r'\begin{center}\includegraphics[width=.97\linewidth]{_xu_ly/graphs/cone_torus.png}\end{center}'
    title={'VD':'Ví dụ','BT':'Bài tập','NC':'Bài nâng cao'}[i['kind']]
    note = latex_note(i) if i['section'].startswith('1.') else latex_note_ch2(i) if i['section'].startswith('2.') else latex_note_ch3(i) if i['section'].startswith('3.') else latex_note_ch4(i) if i['section'].startswith('4.') else None
    knowledge = '\n'+r'\subsection*{Kiến thức và trình tự giải}'+'\n'+note+'\n'+r'\subsection*{Lời giải áp dụng cho bài}'+'\n' if note else r'\textit{Áp dụng kiến thức và phương pháp trong tài liệu gốc.}\par'+'\n'
    parts.append(r'\clearpage\noindent\texttt{\detokenize{'+id+r'}}\par'+ '\n'+r'\section*{Lời giải bổ sung — '+title+' '+str(i['number'])+' · Mục '+i['section']+'}\n'+knowledge+solutions[id]+'\n')
(r/'master.tex').write_text(pre+'\n'.join(parts)+r'\end{document}',encoding='utf-8')
(r/'solutions.json').write_text(json.dumps(solutions,ensure_ascii=False,indent=2),encoding='utf-8')
print('SOLUTION ITEMS',len(parts))
