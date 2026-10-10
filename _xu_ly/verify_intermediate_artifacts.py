"""Check full exported solutions and updated PDF pagination for Chapters 1-3."""
from pathlib import Path
import ast,json,re
import fitz

R=Path(__file__).resolve().parent;out=R.parent/'PDE_Tach_bai_va_loi_giai'
tree=ast.parse((R/'build_markdown.py').read_text(encoding='utf-8'))
mini=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('styled','markdown')],type_ignores=[])
scope={'re':re};exec(compile(mini,'markdown_export','exec'),scope)
manifest=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
ledger={i['id']:i for i in json.loads((R/'ra_soat_buoc_trung_gian_123.json').read_text(encoding='utf-8'))}
pat=r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)'
bodies={i:t.strip() for n in (1,2,3) for i,t in re.findall(pat,(R/f'chapter{n}_detailed.tex').read_text(encoding='utf-8'),re.M|re.S)}
report={}
for n in (1,2,3):
    rows=[r for r in manifest if r['section'].startswith(str(n)+'.')]
    pages=[]
    for item in rows:
        i=item['id'];body=bodies[i]
        pdfpath=out/item['file'];md=pdfpath.with_suffix('.md').read_text(encoding='utf-8')
        tex=(out/'Nguon_loi_giai'/f'{i}.tex').read_text(encoding='utf-8')
        assert scope['markdown'](body) in md,(i,'missing Markdown content')
        assert body in tex,(i,'missing editable source content')
        with fitz.open(pdfpath) as pdf:
            assert len(pdf)==item['original_pages']+item['solution_pages'],i
            assert all(pdf[p].get_images() for p in range(item['original_pages'])),(i,'original scan')
            newtext='\n'.join(pdf[p].get_text() for p in range(item['original_pages'],len(pdf)))
            assert 'Kiến thức' in newtext and 'Lời giải' in newtext,i
            assert '\ufffd' not in newtext,i
            if ledger[i]['status']=='expanded':
                assert 'Chi tiết' in newtext,(i,'supplement missing in PDF')
        assert 'f”' not in md and 'X”' not in md,(i,'corrupted derivative prime')
        for graph in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',tex):
            assert (out/graph).exists(),(i,graph)
        pages.append(item['solution_pages'])
    report[str(n)]={'items':len(rows),'expanded':sum(ledger[v['id']]['status']=='expanded' for v in rows),
                    'solution_pages':sum(pages),'max_solution_pages':max(pages),
                    'complete_Markdown_LaTeX_PDF':'passed'}
with fitz.open(R/'master.pdf') as master:
    master_pages=len(master)
report['master_pages']=master_pages
(R/'verification_intermediate_artifacts.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
# Replace the prior chapter-three artifact report, whose pagination is obsolete.
chapter3=report['3']
(R/'verification_chapter3_artifacts.json').write_text(json.dumps(
    {**chapter3,'master_pages':master_pages,'unicode':'passed','standalone_graph_paths':'passed',
     'PDF_page_counts':'passed'},indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))

# Render representative additions for visual review.
for i in ['BT_1_3_2_3_03','BT_2_3_02','BT_3_3_3_01','BT_3_5_3_02']:
    item=next(r for r in manifest if r['id']==i)
    with fitz.open(out/item['file']) as pdf:
        for p in range(item['original_pages'],len(pdf)):
            if 'Chi tiết' in pdf[p].get_text():
                pdf[p].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(R/f'review_steps_{i}.png')
                break
