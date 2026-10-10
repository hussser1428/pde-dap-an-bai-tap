"""Kiểm tra đủ nội dung 50 mục Chương 4 và bản xuất Markdown/PDF/LaTeX."""
from pathlib import Path
import ast,json,re
import fitz
from chapter4_notes import note_for,latex_note

R=Path(__file__).resolve().parent;OUT=R.parent/'PDE_Tach_bai_va_loi_giai'
pat=r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)'
bodies={i:t.strip() for i,t in re.findall(pat,(R/'chapter4_detailed.tex').read_text(encoding='utf-8'),re.M|re.S)}
rows=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
items=[r for r in rows if r['section'].startswith('4.')]
assert len(items)==50 and set(bodies)=={r['id'] for r in items}
tree=ast.parse((R/'build_markdown.py').read_text(encoding='utf-8'))
mini=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('styled','markdown')],type_ignores=[])
scope={'re':re};exec(compile(mini,'markdown_export','exec'),scope)
master_text=(R/'master.tex').read_text(encoding='utf-8')
aggregate=(OUT/'Nguon_loi_giai/Tat_ca_loi_giai.tex').read_text(encoding='utf-8')
master=fitz.open(R/'master.pdf')
starts={}
for p in master:
    match=re.search(r'^(?:VD|BT|NC)_[\w]+',p.get_text(),re.M)
    if match:starts[match[0]]=p.number
assert len(starts)==322
counts=[];graphs=0
for row in items:
    i=row['id'];body=bodies[i]
    md=(OUT/row['file']).with_suffix('.md').read_text(encoding='utf-8')
    tex=(OUT/'Nguon_loi_giai'/f'{i}.tex').read_text(encoding='utf-8')
    assert scope['markdown'](body) in md,(i,'incomplete solution in Markdown')
    assert note_for(row) in md,(i,'incomplete knowledge in Markdown')
    assert body in tex and latex_note(row) in tex,(i,'incomplete editable LaTeX')
    assert body in master_text and body in aggregate,i
    assert 'f”' not in md and 'X”' not in md and '\ufffd' not in md,i
    assert md.count('$$')%2==0,i
    with fitz.open(OUT/row['file']) as pdf:
        assert len(pdf)==row['original_pages']+row['solution_pages'],i
        assert row['solution_pages']>=1,(i,'missing supplement')
        assert all(pdf[p].get_images() for p in range(row['original_pages'])),(i,'missing original images')
        supplement='\n'.join(pdf[p].get_text() for p in range(row['original_pages'],len(pdf)))
        assert 'Kiến thức' in supplement and 'Lời giải áp dụng' in supplement,i
        assert '\ufffd' not in supplement,(i,'bad Unicode')
        end=min([p for p in starts.values() if p>starts[i]]+[len(master)])
        assert end-starts[i]==row['solution_pages'],i
        # Verify that splitting preserved every page of the compiled supplement.
        for j,p in enumerate(range(starts[i],end)):
            assert pdf[row['original_pages']+j].get_text()==master[p].get_text(),(i,j,'PDF text lost during split')
    for graph in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',tex):
        assert (OUT/graph).exists(),(i,graph)
        graphs+=1
    counts.append(row['solution_pages'])
common=(OUT/'00_Kien_thuc_va_phuong_phap.md').read_text(encoding='utf-8')
assert '## Chương 4 — Hướng dẫn chi tiết' in common
assert 'Cả 50 mục (15 ví dụ, 35 bài tập)' in (R.parent/'MUC_LUC_PDE.md').read_text(encoding='utf-8')
log=(R/'master.log').read_text(encoding='utf-8',errors='replace')
assert 'Overfull' not in log and 'Missing character' not in log
report={'chapter_items':50,'complete_Markdown_LaTeX_PDF':'passed',
        'original_scans':'preserved','solution_pages':sum(counts),
        'minimum_solution_pages':min(counts),'maximum_solution_pages':max(counts),
        'graphs':graphs,'master_solution_items':len(starts),'master_pages':len(master),
        'overfull_boxes':0,'missing_characters':0}
(R/'verification_chapter4_artifacts.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
master.close()

# Render actual solution pages and graphs for visual inspection.
for i in ('BT_4_1_3_05','BT_4_2_3_06','BT_4_4_3_01','VD_4_5_2_02','BT_4_5_3_06','BT_4_6_3_04','VD_4_4_2_01'):
    row=next(r for r in items if r['id']==i)
    with fitz.open(OUT/row['file']) as pdf:
        for p in range(row['original_pages'],len(pdf)):
            if 'Lời giải áp dụng' in pdf[p].get_text():
                pdf[p].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(R/f'review_ch4_{i}.png')
                break
        if i in ('BT_4_5_3_06','BT_4_6_3_04','VD_4_4_2_01'):
            pdf[-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(R/f'review_ch4_{i}_last.png')
