#!/usr/bin/env python3
import json
import re
from html import escape
from pathlib import Path
from estandarizar_nivel1 import Document

ROOT=Path(__file__).resolve().parent.parent

def add_prose(a, expansion):
    h=a['articleHtml']
    if 'data-ampliacion-editorial="20261031"' in h:
        return
    d=Document(h)
    edits=[]
    for number,paragraphs in expansion.items():
        node=next(n for n in d.nodes if n.attrs.get('id')=='jmr-n1-chapter-'+number)
        index=d.nodes.index(node)
        next_h=next((n for n in d.nodes[index+1:] if n.tag=='h2' and n.attrs.get('id','').startswith('jmr-n1-chapter-')),None)
        limit=next_h.start if next_h else len(h)
        # Remove an explicit gap only in a chapter receiving specific analysis.
        for p in d.nodes:
            if p.tag=='p' and p.attrs.get('data-editorial-gap')=='true' and node.end<=p.start<limit:
                edits.append((p.start,p.end,''))
        block='<div data-ampliacion-editorial="20261031" data-ticker="'+a['ticker']+'">'+''.join('<p>'+escape(p)+'</p>' for p in paragraphs)+'</div>'
        edits.append((node.end,node.end,block))
    for start,end,value in sorted(edits,reverse=True):
        h=h[:start]+value+h[end:]
    a['articleHtml']=h
    a['ampliacionEditorial20261031']={'capitulosAmpliados':list(map(int,expansion)), 'supuestosModificados':False,'auditoriaEconomicaEjecutada':False,'profundidad':'PENDIENTE_CONTROL_EDITORIAL'}

def native_discount_appendix(a,v):
    d=v.get('descuentoMultiples') or {}
    if not d.get('integracionNativa'):
        return
    a['descuentoMultiples']=d
    old=a.get('calculationHtml','')
    old=re.sub(r'<section data-descuentos-nativos="20261031">[\s\S]*?</section>', '', old)
    rows=[]
    for method in d['metodos']:
        for scenario in ('conservador','base','optimista'):
            source=method.get(scenario)
            cells=[method['nombre'],scenario]
            cells+=['N/D']*7 if source is None else source['fy']+source['vp']+[source['consolidado']]
            rows.append('<tr>'+''.join('<td>'+escape(str(c))+'</td>' for c in cells)+'</tr>')
    info=d['integracionNativa']
    source='https://docs.google.com/spreadsheets/d/'+v['sheet_id']+'/edit'
    block='<section data-descuentos-nativos="20261031"><h3>Descuentos nativos por método y escenario</h3>'
    block+='<p>Revisión '+escape(v['revisionId'])+' · <a href="'+source+'">Hoja oficial</a> · Descuento de múltiplos A1:M80. Se transcriben valores nativos; no se recalculan los precios. Los FY incluyen las distribuciones según la definición de la hoja. VP1, VP2 y VP3 respetan su fecha de pago. El consolidado es el criterio nativo y no equivale al centro VP3 de una matriz.</p>'
    block+='<p>Estado técnico: '+escape(info['estado'])+'. Auditoría económica independiente pendiente.</p>'
    if info['motivoPendiente']:
        block+='<p><strong>Pendiente:</strong> '+escape(info['motivoPendiente'])+'</p>'
    block+='<div class="table-scroll"><table><thead><tr>'+''.join('<th>'+x+'</th>' for x in ['Método','Escenario','FY+1','FY+2','FY+3','VP1','VP2','VP3','Consolidado hoy'])+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
    block+='<p>Fotografía SHA256: <code>'+info['capturaSha256']+'</code>. Valores y fórmulas conservados en evidencia/descuentos-20261031/. Los N/D son ausencia de resultados, sin imputación de cero ni cambio de ponderación.</p></section>'
    a['calculationHtml']=old+block

if __name__=='__main__':
    expansions=json.loads((ROOT/'scripts/ampliaciones_editoriales_20261031.json').read_text())
    catalog=json.loads((ROOT/'catalogo.json').read_text())
    for p in sorted(ROOT/path for path in catalog['analisis']):
        a=json.loads(p.read_text())
        if a.get('version_metodo')!='A-1.2':
            continue
        if a['ticker'] in expansions:
            add_prose(a,expansions[a['ticker']])
        vp=ROOT/'valoraciones'/(a['revisionId']+'.json')
        if vp.exists():
            native_discount_appendix(a,json.loads(vp.read_text()))
        a['html']=a['articleHtml']+a.get('calculationHtml','')
        p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
        if a['ticker'] in expansions:
            n=len(re.sub('<[^>]+>',' ',a['articleHtml']).split())
            print(a['ticker'],n,'palabras; ampliación económica sin modificar supuestos')
