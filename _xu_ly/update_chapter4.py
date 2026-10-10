"""Đồng bộ 50 lời giải Chương 4, giữ bản sao nguồn trước khi cập nhật."""
from pathlib import Path
import json,re,shutil

R=Path(__file__).resolve().parent
pat=re.compile(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',re.M|re.S)
def blocks(path):
    if not path.exists(): return {}
    pairs=[(m[1],m[2].strip()) for m in pat.finditer(path.read_text(encoding='utf-8'))]
    assert len(dict(pairs))==len(pairs),path
    return dict(pairs)
def save(path,items):
    path.write_text('\n\n'.join('%ID '+k+'\n'+v for k,v in items.items())+'\n',encoding='utf-8')

backup=R/'backup_truoc_chi_tiet_chuong4'
backup.mkdir(exist_ok=True)
for name in ('prepare_tex.py','refresh_pdf.py','build_markdown.py'):
    if not (backup/name).exists(): shutil.copy2(R/name,backup/name)
new={}
for n in range(1,7):
    found=blocks(R/f'chapter4_part{n}.tex')
    assert not (set(new)&set(found))
    new.update(found)
inventory=json.loads((R/'inventory.json').read_text(encoding='utf-8'))
chapter={i['id'] for i in inventory if i['section'].startswith('4.')}
assert set(new)==chapter,(chapter-set(new),set(new)-chapter)
save(R/'chapter4_detailed.tex',new)
existing=set()
for path in sorted(R.glob('loi_giai*.tex')):
    old=blocks(path); existing.update(old)
    changed=set(old)&chapter
    if changed:
        if not (backup/path.name).exists(): shutil.copy2(path,backup/path.name)
        old.update({k:new[k] for k in changed}); save(path,old)
missing={k:v for k,v in new.items() if k not in existing}
path=R/'loi_giai_4_examples.tex'
old=blocks(path); old.update(missing); save(path,old)
print('Chapter 4:',len(chapter),'detailed solutions;',len(missing),'scanned examples transcribed.')
