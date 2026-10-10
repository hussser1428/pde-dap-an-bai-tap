from PIL import Image, ImageDraw
from pathlib import Path
import sys
root=Path(__file__).resolve().parent
nums=[int(x) for x in sys.argv[1:]]
for i in range(0,len(nums),2):
    group=nums[i:i+2]
    sheet=Image.new('RGB',(1906,1380),'#ddd')
    draw=ImageDraw.Draw(sheet)
    for j,n in enumerate(group):
        im=Image.open(root/'pages'/f'{n+1:03}.png').convert('RGB')
        draw.text((j*953+20,8),f'TRANG SACH {n} / PDF {n+1}',fill='black')
        sheet.paste(im,(j*953,30))
    path=root/('sheet_'+'_'.join(map(str,group))+'.png')
    sheet.save(path)
    print(path.name)
