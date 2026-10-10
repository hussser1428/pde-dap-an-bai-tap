import json, re
from pathlib import Path
root = Path(__file__).resolve().parent
pages = [json.loads(f.read_text(encoding='utf-8-sig')) for f in sorted((root/'ocr').glob('*.json'))]
out=[]
for o in pages:
    for l in o['lines']:
        x=min(w['x'] for w in l['words']); y=min(w['y'] for w in l['words'])
        if 80<y<1270 and x<170 and re.match(r'^(?:[0-9lIl]+\.|[IVX]+\.)', l['text']):
            out.append(f"{o['page']:03} y={y:04.0f} x={x:03.0f} {l['text']}")
(root/'moc.txt').write_text('\n'.join(out),encoding='utf-8')
(root/'ocr_tat_ca.txt').write_text('\n'.join(f"\n=== PDF {o['page']} / sach {o['page']-1} ===\n"+'\n'.join(l['text'] for l in o['lines']) for o in pages),encoding='utf-8')
print('\n'.join(out))
