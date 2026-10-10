"""Thay lời giải Chương 2 sau khi đối chiếu bản scan, giữ bản sao nguồn cũ."""
from pathlib import Path
import json,re,shutil

r=Path(__file__).resolve().parent
pattern=re.compile(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',re.M|re.S)
def blocks(path):
    if not path.exists():return {}
    pairs=[(m[1],m[2].strip()) for m in pattern.finditer(path.read_text(encoding='utf-8'))]
    assert len(dict(pairs))==len(pairs),path
    return dict(pairs)
def save(path,items):
    path.write_text('\n\n'.join('%ID '+k+'\n'+v for k,v in items.items())+'\n',encoding='utf-8')
new=blocks(r/'chapter3_detailed.tex')
chapter={i['id'] for i in json.loads((r/'inventory.json').read_text(encoding='utf-8')) if i['section'].startswith('3.')}
assert set(new)==chapter,(chapter-set(new),set(new)-chapter)
backup=r/'backup_truoc_chi_tiet_chuong3';backup.mkdir(exist_ok=True)
existing=set()
for path in sorted(r.glob('loi_giai*.tex')):
    old=blocks(path);existing.update(old)
    changed=set(old)&chapter
    if changed:
        if not (backup/path.name).exists():shutil.copy2(path,backup/path.name)
        old.update({k:new[k] for k in changed});save(path,old)
missing={k:v for k,v in new.items() if k not in existing}
path=r/'loi_giai_3_examples.tex';old=blocks(path);old.update(missing);save(path,old)
print('Chapter 3:',len(chapter),'detailed solutions;',len(missing),'scanned examples transcribed.')
