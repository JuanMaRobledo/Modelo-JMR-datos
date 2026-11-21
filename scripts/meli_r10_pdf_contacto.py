#!/usr/bin/env python3
"""Inspección visual del PDF de MELI R10: 52 páginas en mosaicos y 3 vistas a resolución de lectura."""
from PIL import Image,ImageOps,ImageDraw,ImageFont
import fitz, pathlib, hashlib
root=pathlib.Path(__file__).resolve().parents[1]
pdf=root/'jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.pdf'
dest=root/'jmr-v2/qa/MELI-R10-ED2'
dest.mkdir(parents=True,exist_ok=True)
for stale in dest.glob("*.jpg"):
    stale.unlink()
doc=fitz.open(pdf)
assert doc.page_count>=23
page_count=doc.page_count
try:font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',19)
except OSError:font=ImageFont.load_default()
def thumb(page,no,size=(245,350)):
    pix=page.get_pixmap(matrix=fitz.Matrix(.45,.45),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im.thumbnail((size[0]-14,size[1]-30))
    tile=Image.new('RGB',size,'#f1f5f7')
    tile.paste(im,((size[0]-im.width)//2,4))
    d=ImageDraw.Draw(tile)
    d.text((12,size[1]-26),f'Pág. {no+1}',fill='#1c344a',font=font)
    return tile
for start in range(0,page_count,26):
    batch=list(range(start,min(start+26,page_count)))
    cols=5;rows=(len(batch)+cols-1)//cols;size=(245,350)
    board=Image.new('RGB',(cols*size[0],rows*size[1]),'white')
    for slot,no in enumerate(batch):
        board.paste(thumb(doc[no],no,size),((slot%cols)*size[0],(slot//cols)*size[1]))
    out=dest/f'contacto-paginas-{start+1:02d}-{batch[-1]+1:02d}.jpg'
    board.save(out,format='JPEG',quality=83,optimize=True)
    print('MOSAICO_QA',out.relative_to(root),out.stat().st_size)
for no in [0,22,42,43,51]:
    if no>=page_count:continue
    pix=doc[no].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    out=dest/f'pagina-{no+1:02d}.jpg'
    im.save(out,format='JPEG',quality=80,optimize=True)
    print('PAGINA_QA',out.relative_to(root),out.stat().st_size)
doc.close()
