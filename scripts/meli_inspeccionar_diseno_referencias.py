#!/usr/bin/env python3
import fitz, pathlib, json
from PIL import Image,ImageDraw,ImageFont
root=pathlib.Path(__file__).resolve().parents[1]
files={
'R8':'jmr-v2/informes/MELI/MELI-V2-LTM20260930-R8_INFORME_FUNDAMENTAL.pdf',
'NVDA-R6':'jmr-v2/informes/NVDA/NVDA-V2-FY26Q2FY27-R6_INFORME_FUNDAMENTAL.pdf'
}
out=root/'jmr-v2/qa/referencias-diseno-r8-nvda'
out.mkdir(exist_ok=True,parents=True)
for label,filename in files.items():
 doc=fitz.open(root/filename)
 overview=[]
 for i,p in enumerate(doc):
  if i in [0,1,2,3,4,5,6,8,10,15,20,25,30,35]:
   overview.append({'page':i+1,'preview_text':p.get_text()[:1400],'page_size':[p.rect.width,p.rect.height],
          'images':len(p.get_image_info()),'word_count':len(p.get_text().split())})
 for i in list(range(min(6,len(doc)))):
  pix=doc[i].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False)
  pix.save(out/f'{label}-pagina-{i+1:02}.png')
 # 9-page contact sheet
 sel=list(range(min(9,len(doc))))
 thumbs=[]
 for idx in sel:
  page=doc[idx]; pix=page.get_pixmap(matrix=fitz.Matrix(.38,.38),alpha=False)
  im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
  im.thumbnail((300,440))
  tile=Image.new('RGB',(325,485),'#edf1f3')
  tile.paste(im,((325-im.width)//2,5))
  ImageDraw.Draw(tile).text((12,456),f'{label} - Pagina {idx+1}',fill='#1c344a')
  thumbs.append(tile)
 board=Image.new('RGB',(325*3,485*3),'white')
 for j,im in enumerate(thumbs):board.paste(im,((j%3)*325,(j//3)*485))
 board.save(out/f'{label}-mosaico-primeras-9.jpg',quality=85)
 (out/f'{label}-estructura.json').write_text(json.dumps({'pages':len(doc),'overview':overview},ensure_ascii=False,indent=2))
 print('REF_EXAMINADA',label,'pages',len(doc),'cover_text',repr(doc[0].get_text()[:800]))
 doc.close()
