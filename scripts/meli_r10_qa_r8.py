#!/usr/bin/env python3
import pathlib,fitz,json
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
src=root/'jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.pdf'
ref=root/'jmr-v2/informes/MELI/MELI-V2-LTM20260930-R8_INFORME_FUNDAMENTAL.pdf'
dest=root/'jmr-v2/qa/MELI-R10-ED4';dest.mkdir(exist_ok=True,parents=True)
for p in dest.glob('*.jpg'):p.unlink()
for p in dest.glob('*.png'):
 if p.name!='cotizacion-original-R8.png':p.unlink()
with fitz.open(src) as doc,fitz.open(ref) as original:
 for name,p in [('ED4-portada',doc[0]),('R8-portada',original[0]),('ED4-perfil',doc[1]),('R8-perfil',original[1]),('ED4-contenido',doc[3])]:
  pix=p.get_pixmap(matrix=fitz.Matrix(1.45,1.45),alpha=False)
  pix.save(dest/(name+'.png'))
 size=(245,355)
 for start in range(0,len(doc),24):
  sel=list(range(start,min(start+24,len(doc))))
  tile=Image.new('RGB',(size[0]*6,size[1]*4),'white')
  for j,index in enumerate(sel):
   pix=doc[index].get_pixmap(matrix=fitz.Matrix(.38,.38),alpha=False)
   im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
   im.thumbnail((size[0]-10,size[1]-27))
   sub=Image.new('RGB',size,'#f0f4f6')
   sub.paste(im,((size[0]-im.width)//2,2))
   ImageDraw.Draw(sub).text((9,size[1]-24),'Pág. '+str(index+1),fill='#1c344a')
   tile.paste(sub,((j%6)*size[0],(j//6)*size[1]))
  out=dest/f'paginas-{start+1:02}-{sel[-1]+1:02}.jpg'
  tile.save(out,quality=85)
 # Compare color of cover center to R8 original: identical blue by standard.
 for label,p in [('R8',original[0]),('ED4',doc[0])]:
  pix=p.get_pixmap(matrix=fitz.Matrix(.15,.15),alpha=False)
  im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
  print('COLOR_PORTADA',label,im.getpixel((im.width//2,im.height//3)))
 print('QA_OK',json.dumps({'nuevo':len(doc),'referencia':len(original),'imagenes':sum(len(x.get_image_info()) for x in doc)}))
