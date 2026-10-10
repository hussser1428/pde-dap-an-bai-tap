"""Cập nhật nguồn lời giải Chương 1 từ bản diễn giải đã đối chiếu ảnh đề."""
from pathlib import Path
import re
import json
import shutil

ROOT = Path(__file__).resolve().parent
BLOCK = re.compile(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)', re.M | re.S)

def read_blocks(path):
    text = path.read_text(encoding='utf-8')
    pairs = [(m[1], m[2].strip()) for m in BLOCK.finditer(text)]
    assert len(dict(pairs)) == len(pairs), path
    return dict(pairs)

def write_blocks(path, blocks):
    path.write_text('\n\n'.join('%ID '+ident+'\n'+body for ident,body in blocks.items())+'\n', encoding='utf-8')

overrides = read_blocks(ROOT/'chapter1_detailed.tex')
inventory = json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
chapter = {i['id'] for i in inventory if i['section'].startswith('1.')}
assert set(overrides) <= chapter
backup = ROOT/'backup_truoc_chi_tiet_chuong1'
backup.mkdir(exist_ok=True)
existing = set()
for path in sorted(ROOT.glob('loi_giai*.tex')):
    blocks = read_blocks(path)
    existing.update(blocks)
    updates = {ident: overrides[ident] for ident in blocks if ident in overrides}
    if updates:
        saved = backup/path.name
        if not saved.exists():
            shutil.copy2(path,saved)
        blocks.update(updates)
        write_blocks(path,blocks)
missing = {ident:body for ident,body in overrides.items() if ident not in existing}
path = ROOT/'loi_giai_1.tex'
blocks = read_blocks(path)
blocks.update(missing)
write_blocks(path,blocks)
# Keep the earlier update entry point from restoring short versions.
path = ROOT/'chi_tiet_dau.tex'
blocks = read_blocks(path)
saved = backup/path.name
if not saved.exists():
    shutil.copy2(path,saved)
blocks.update({ident:overrides[ident] for ident in blocks if ident in overrides})
write_blocks(path,blocks)
all_ids = {ident for path in ROOT.glob('loi_giai*.tex') for ident in read_blocks(path)}
assert chapter <= all_ids, chapter-all_ids
print(f'Chapter 1: {len(chapter)} typed solutions; {len(overrides)} rewritten; {len(missing)} added from scanned examples.')
