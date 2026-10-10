from pathlib import Path
import re
r=Path(__file__).parent
def blocks(s):return {m[1]:m[2].strip() for m in re.finditer(r'^%ID (\S+)\s*\n(.*?)(?=^%ID |\Z)',s,re.M|re.S)}
extra=blocks((r/'chi_tiet_dau.tex').read_text(encoding='utf-8'))
p=r/'loi_giai_1.tex';old=blocks(p.read_text(encoding='utf-8'));old.update(extra)
p.write_text('\n'.join('%ID '+k+'\n'+v+'\n' for k,v in old.items()),encoding='utf-8')
