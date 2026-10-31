#!/usr/bin/env python3
"""Restore reproducible N2 from pinned native evidence; never estimate missing cells."""
import hashlib
import json
import re
from html import escape
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def table(rows, heading):
    populated=[row for row in rows if any(c not in ('',None) for c in row)]
    count=max((len(row) for row in populated),default=0)
    def cell(x):
        return 'N/D' if x is None or x=='' else str(x)
    return '<h4>'+escape(heading)+'</h4><div class="table-scroll"><table><tbody>'+''.join('<tr>'+''.join('<td>'+escape(cell(row[i] if i<len(row) else ''))+'</td>' for i in range(count))+'</tr>' for row in populated)+'</tbody></table></div>'

def build(a,v,snapshot,formula,current):
    d=snapshot['data']
    assert snapshot['revision_id']==a['revisionId']==v['revisionId']
    assert snapshot['sheet_id']==v['sheet_id']
    digest=hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,default=str).encode()).hexdigest()
    assert digest==snapshot['data_sha256']
    # Only transport differences in trailing empty cells are allowed.
    def normalize(rows):
        return [[row[i] if i<len(row) and row[i] is not None else '' for i in range(13)] for row in rows]
    assert normalize(current['values'])==normalize(d['valuation_base'])
    ticker=a['ticker'];prefix='jmr-'+ticker.lower()+'-n2-repro-'
    headings=['Identidad, fuentes y unidades','Estados históricos y LTM','Ratios y economía del negocio','Puente contable a económico','Supuestos por historia','Costo de capital','Cuatro proyecciones anuales','Terminal y puente al patrimonio','Escenarios, probabilidades y ciclos','Múltiplos y descuentos','Sensibilidades','Fórmulas nativas, conciliación y límites']
    blocks=[]
    sheet='https://docs.google.com/spreadsheets/d/'+v['sheet_id']+'/edit'
    sources=v.get('fuentes_supuestos',[])
    if isinstance(sources,dict):sources=list(sources.values())
    links=' · '.join('<a href="'+escape(x,quote=True)+'">Fuente '+str(i+1)+'</a>' for i,x in enumerate(sources) if isinstance(x,str) and x.startswith('https://'))
    unit='Millones USD y USD por acción. Históricos AFYA conservan conversiones originales y requieren comprobar homogeneidad de FX.' if ticker=='AFYA' else 'Millones USD y USD por acción. EBIT económico ajustado no equivale al EBIT GAAP.'
    blocks.append('<p>'+escape(ticker+' · '+a['revisionId']+' · '+unit)+'</p><p><a href="'+sheet+'">Hoja oficial</a> · '+links+'</p><p>Fotografía de rangos '+escape(snapshot['captured_at'])+'; SHA256 de datos: <code>'+digest+'</code>. DCF Base contrastado nuevamente el 31-oct-2026: celdas no vacías idénticas. Las fórmulas Base se guardan en una captura independiente.</p>')
    blocks.append(''.join(table(d[k],title) for k,title in [('is','Income Statement'),('bs','Balance Sheet'),('cf','Cash Flow Statement')]))
    blocks.append('<p>Se conserva la definición del denominador de cada ratio. Los retornos contables y marginales no son intercambiables; las cifras vacías son N/D.</p>'+table(d['trailing'],'Trailing Valuation')+table(d['fm'],'Financials Multiples · filas capturadas'))
    adjustments=[[k,json.dumps(val,ensure_ascii=False) if isinstance(val,(list,dict)) else val] for k,val in (v.get('revisionSupuestos') or {}).items()]
    blocks.append(table(adjustments,'Tratamientos y parámetros efectivos del registro')+table(d['rd'],'R&D converter')+table(d['options'],'Option value')+'<p>Las convenciones del registro se presentan para reproducción; no implican aprobación de SBC, alquileres, fiscalidad o activos no operativos. Evitar doble cómputo entre ajustes de EBIT, reinversión y puente al patrimonio.</p>')
    blocks.append(table(d['stories'],'Escenarios e historias · A4:N13')+''.join(table(d[k],title) for k,title in [('growth_base','Crecimiento Base'),('growth_cons','Crecimiento Conservador'),('growth_disr','Crecimiento Disrupción'),('growth_opt','Crecimiento Optimista')]))
    blocks.append(table(d['wacc'],'Cost of capital worksheet · A12:E94')+table(d['wacc_regions'],'Exposición regional · G21:K33')+'<p>El costo del patrimonio descuenta precios de acciones; el WACC descuenta FCFF. Las tasas, unidades y referencias temporales no deben intercambiarse.</p>')
    blocks.append(''.join(table(d[k],title) for k,title in [('valuation_base','Base · A3:M42'),('valuation_cons','Conservadora · A53:M93'),('valuation_opt','Optimista · A104:M144'),('valuation_disr','Disrupción · A157:M197')] ))
    blocks.append(table(d['valuation_base'][15:],'Valor terminal, valor operativo, deuda, caja, minoritarios, opciones y acciones · Base')+'<p>La suma de VP operativos se lleva al patrimonio con las partidas del puente nativo. No se vuelve a sumar caja ni a restar deuda ya reconocida. El valor por acción se conserva sin recálculo externo.</p>')
    blocks.append(table(d['stories'],'Probabilidades y promedio condicionado nativo')+'<p>Disrupción permanece separada del promedio ordinario. Las probabilidades describen las historias registradas; no se cambian por sentimiento bursátil. <a href="#jmr-n1-chapter-5">Ver diagnóstico y transmisión de ciclos en Nivel 1</a>.</p>')
    discounts=v.get('descuentoMultiples') or {}
    methodrows=[]
    for method in discounts.get('metodos',[]):
        for scenario in ['conservador','base','optimista']:
            item=method.get(scenario)
            methodrows.append([method['nombre'],scenario]+([None]*7 if item is None else item['fy']+item['vp']+[item['consolidado']]))
    blocks.append('<p>Columnas: método, escenario, FY+1, FY+2, FY+3, VP1, VP2, VP3 y consolidado hoy. Importación nativa con fecha 31-oct-2026; precios secundarios y anclas pendientes de auditoría económica.</p>'+table(methodrows,'Descuento de múltiplos · cinco métodos')+table(d['multiples_ps'],'P/V · complementario')+table(d['multiples_pbv'],'P/BV · complementario'))
    sens=table(d['sens_dcf'],'Sensibilidad DCF · rango nativo A1:H36')
    for m in v.get('sensibilidadMultiples',{}).get('matrices',[]):
        sens+=table([['Múltiplo / fundamental FY+3']+m.get('fundamentalFY3',[])]+[[y]+row for y,row in zip(m.get('multiploElegido',[]),m.get('matriz') or [])],m['metodo']+' · Base · '+m['estado'])
    blocks.append(sens+'<p>Centros por múltiplo contrastados con VP3 del descuento de esta revisión. No se sustituye una sensibilidad de WACC por otra de ROIC o margen. Las matrices no demuestran que las anclas sean económicamente apropiadas.</p>')
    frows=[]
    for i,row in enumerate(formula['values'],3):
        for j,value in enumerate(row):
            if isinstance(value,str) and value.startswith('='):
                frows.append([chr(65+j)+str(i),value])
    blocks.append(table(frows,'Fórmulas efectivamente leídas · Valuation output A3:M42')+'<p>El archivo de evidencia conserva rangos, valores y fórmulas. Esta reproducción no ejecuta auditoría económica. Reservas del registro: '+escape(' · '.join(v.get('salvedades',[])))+'</p><p>Las proyecciones y estados proceden de la fotografía identificada; la comprobación nueva se limita al DCF Base y a los descuentos. No se certifica de nuevo cada histórico o cada escenario por repetir sus tablas.</p>')
    assert len(blocks)==12
    html='<div data-jmr-n2-reproducible="20261031"><h2>Nivel 2 · datos, fórmulas y conciliaciones</h2><nav aria-label="Índice del Nivel 2"><ol>'+''.join('<li><a href="#'+prefix+str(i)+'">'+str(i)+'. '+h+'</a></li>' for i,h in enumerate(headings,1))+'</ol></nav>'
    html+=''.join('<section id="'+prefix+str(i)+'"><h3>'+str(i)+'. '+title+'</h3>'+body+'</section>' for i,(title,body) in enumerate(zip(headings,blocks),1))+'</div>'
    old=a.get('calculationHtml','')
    if 'data-jmr-n2-reproducible=' in old:
        marker=old.find('<details data-soporte-complementario=')
        old=old[marker:] if marker>=0 else ''
    else:
        old=re.sub(r'^<section><h2>Soporte cuantitativo pendiente de importación</h2>[\s\S]*?</section>', '', old)
        old=re.sub(r'<section data-descuentos-nativos="20261031">[\s\S]*?</section>', '', old)
        old='<details data-soporte-complementario="20261031"><summary>Notas y tablas complementarias conservadas</summary>'+old.replace('<h2','<h4').replace('</h2>','</h4>')+'</details>'
    html+=old
    a['calculationHtml']=html
    a['html']=a['articleHtml']+html
    a['nivel2Reproduccion20261031']={'apartados':12,'fuenteSha256':digest,'revisionId':a['revisionId'],'baseActualContrastada':True,'historicosReauditados':False,'auditoriaEconomicaEjecutada':False}
    return a

if __name__=='__main__':
    for ticker in ['AFYA','DUOL']:
        p=next((ROOT/'analisis').glob(ticker+'-*'));a=json.loads(p.read_text())
        v=json.loads((ROOT/'valoraciones'/(a['revisionId']+'.json')).read_text())
        snapshot=json.loads((ROOT/'evidencia/integracion-nativa-20261030'/a['revisionId']/'resultados_hoja.json').read_text())
        directory=ROOT/'evidencia/descuentos-20261031'
        formula=json.loads((directory/(a['revisionId']+'-DCF-FORMULA.json')).read_text())
        current=json.loads((directory/(a['revisionId']+'-DCF-UNFORMATTED_VALUE.json')).read_text())
        result=build(a,v,snapshot,formula,current)
        p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(ticker,'12 apartados N2 con estados, cuatro proyecciones, fórmulas y evidencia')
