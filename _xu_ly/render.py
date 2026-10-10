import fitz
from pathlib import Path
root = Path(__file__).resolve().parent
out = root / 'pages'
out.mkdir(exist_ok=True)
doc = fitz.open(root.parent / 'pde bài tập.pdf')
for i, page in enumerate(doc):
    path = out / f'{i+1:03}.png'
    if not path.exists():
        page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(path)
print(f'Rendered {len(doc)} pages', flush=True)
