"""Assemble a complete record from the official exported viewer and reviewed Doc.
No DCF is estimated here; all financial outputs are read from the sheet snapshot.
"""
from pathlib import Path
import copy
import datetime as dt
import html
import json
import math
import re

P=Path(__file__).resolve().parent
C=P/'candidate'
s=json.loads((C/'ADBE-snapshot.json').read_text())
v=s['values']
rec=json.loads((C/'ADBE-generated.json').read_text())
old=json.loads((P/'adbe-old.json').read_text())
research_old=json.loads((P/'adbe-research-old.json').read_text())
sid=s['sheet_id']
sheet='https://docs.google.com/spreadsheets/d/'+sid+'/edit'
gids={x['properties']['title']:x['properties']['sheetId'] for x in s['metadata']['sheets']}
now=dt.datetime.now(dt.timezone.utc).isoformat()

def cell(tab, addr):
    m=re.fullmatch(r'([A-Z]+)([0-9]+)',addr)
    j=0
    for ch in m[1]:j=j*26+ord(ch)-64
    i=int(m[2])-1
    return v[tab][i][j-1] if len(v[tab])>i and len(v[tab][i])>=j else None

def esc(x):return html.escape(str(x))
def num(x):
    if isinstance(x,(int,float)):
        if 0<abs(x)<1:return f'{x*100:.2f}%'
        return f'{x:,.2f}'
    return esc(x)

def table(rows):
    rows=[r for r in rows if any(x!='' for x in r)]
    n=max(map(len,rows),default=0)
    return '<div class="table-scroll"><table><tbody>'+''.join('<tr>'+''.join('<td>'+num(row[j] if j<len(row) else '')+'</td>' for j in range(n))+'</tr>' for row in rows)+'</tbody></table></div>'

def link(tab):return sheet+'?gid='+str(gids[tab])
def section(tab,rows=None):
    text='<h3>'+esc(tab)+'</h3><p><a href="'+link(tab)+'">Ver fórmulas en la hoja vigente</a></p>'
    return text+table(rows if rows is not None else v[tab])

base=cell('Valuation output','B35')
price=cell('Input sheet','D1')
mos=cell('Resumen de Valoración','G4')
pm=base*(1-mos)
expected=cell('Escenarios e historias','H10')
values={'base':base,'conservador':cell('Valuation output','B86'),
        'optimista':cell('Valuation output','B137'),'disrupcion':cell('Valuation output','B190')}
assert math.isclose(base,392.9600099404326,abs_tol=1e-7)
assert rec['baseMOS']=='dcfBase', 'El visor debe reconocer el MOS Base al abrir el XLSX'
assert math.isclose(rec['precioMOS'],pm,abs_tol=1e-6)
assert all(r['preflight']==0 and r['formulas']==0 for r in json.loads((C/'gates.json').read_text()).values())
assert json.loads((C/'ADBE-browser.json').read_text())['errors']==[]

rec.update({'ticker':'ADBE','hojaGoogle':sheet,'nombreActivo':'Adobe Inc.','currency':'USD','market':'NASDAQ',
    'fecha':'Análisis 15-oct-2026 · estados financieros al 28-ago-2026',
    'precio':price,'precioAnalisis':price,'precioReferenciaFecha':'2026-10-15',
    'precioReferenciaFuente':'Cierre fijo del análisis15-oct-2026; no cotización en vivo',
    'baseMOS':'dcfBase','precioMOS':pm,'precioMOSMax':pm,
    'precioMOSHoy':{k:pm for k in ('conservador','base','optimista')},'savedAt':now})
rec['posicion']=old.get('posicion')
stories=[]
for idx,(letter,key) in enumerate([('A','base'),('B','conservador'),('C','disrupcion'),('D','optimista')],5):
    r=v['Escenarios e historias'][idx-1]
    stories.append({'id':letter,'nombre':r[0],'probabilidad':r[1],'crecimiento':r[2],
        'margen':r[3],'salesToCapital':r[4],'salesToCapital2':r[5],'roicTerminal':r[6],
        'valor':r[7],'terminalGrowth':r[9],'estado':r[10],'central':key=='base'})
rec['valorEsperado']={'fecha':'2026-10-15','valor':expected,'valorCentral':base,'dcfBase':base,
    'metodo':'DCF Base principal; promedio de cuatro historias complementario',
    'escenariosUnificados':True,'historiaCentralId':'A','rango':{'min':min(values.values()),'max':max(values.values())},'historias':stories}
rec['escenariosDCF']={'version':3,'fuente':'Valuation output y Escenarios e historias',
    'principal':'valorEsperado.dcfBase','central':'A','fecha':'2026-10-15','valores':values}
rec['descuentoMultiples']['dcfHoy']={k:values[k] for k in ('conservador','base','optimista')}
rec['crecimientoImplicito']={'version':3,'fecha':'2026-10-15','precioFecha':'2026-10-15','precio':price,
    'dcfHoy':base,'dcfFy3':rec['metodos'][0]['base'],'metodo':'DCF inverso de la hoja vigente, delta común años1–5',
    'dcfInverso':{'incrementoTasaAnual':cell('DCF inverso','B5'),'gImplicito':cell('DCF inverso','B6'),
        'gDcf':cell('DCF inverso','B4'),'precioReconstruido':cell('DCF inverso','B7'),
        'errorAbsoluto':abs(cell('DCF inverso','B7')-price),'estado':'VIGENTE'},
    'alerta':'Condición matemática del precio congelado, no pronóstico.'}
rec['lecturaDamodaran']={'fecha':'2026-10-15','dcfBase':base,'fuente':'Duración ventaja · FCFF',
    'dcfSinFoso':cell('Duración ventaja · FCFF','B5'),'dcfMoat5':cell('Duración ventaja · FCFF','B6'),
    'dcfMoat10':cell('Duración ventaja · FCFF','B7'),'esQuintoEscenario':False}
rec['zonas']['conMOS']={'min':pm,'max':pm,'base':'dcfBase'}
rec['zonas']['descripcion']='Bandas Value/Deep Value/histórica sobre promedio de escenarios; único MOS sobre DCF Base.'
multiple_rows=v['Múltiplos implícitos DCF'][4:9]
rec['multiplosImplicitosDCF']={'version':3,'fecha':'2026-10-15','horizonte':3,'noUsarComoInputDCF':True,
    'criterio':'Cada DCF frente al mismo precio de referencia, sobre métricas FY+3 propias de su escenario',
    'metodos':[{'nombre':r[0],'conservador':r[1],'base':r[4],'optimista':r[7]} for r in multiple_rows],
    'salvedades':['Equivalencias prospectivas FY+3; no ratios LTM de mercado.']}
rec['cotizacionMultiples']={'version':3,'precioMercado':price,'fechaCorte':'2026-10-15','horizonte':3,
    'esPrecioActualVerificado':False,'fuente':'Precio fijo de referencia del análisis, no precio en vivo',
    'metodos':[{'nombre':r[0],'mercado_FY3_equivalente':{'conservador':r[2],'base':r[5],'optimista':r[8]},
        'deltaMercado_vs_DCF_FY3':{'conservador':r[3],'base':r[6],'optimista':r[9]}} for r in multiple_rows]}
rec['multiplesHistoricos']={'fuente':link('Múltiplos históricos'),'estado':'Anclas secundarias documentadas; ver tabla completa en cálculos'}

def paragraphs(text):
    out=[]
    for p in re.split(r'\n\s*\n',text.strip()):
        p=p.strip()
        if not p:continue
        if re.match(r'^\d+\. ',p):out.append('<h2>'+esc(p)+'</h2>')
        else:
            p=esc(p).replace('\n',' ')
            p=re.sub(r'https://[^\s<>\)]+',lambda m:'<a href="'+m[0]+'">'+m[0]+'</a>',p)
            out.append('<p>'+p+'</p>')
    return ''.join(out)

text=(P/'adbe-doc.txt').read_text().lstrip('\ufeff').replace('\r','')
text=text.split('Enlaces directos al Nivel 2')[0]
main,technical=text.split('20. Nivel 2',1)
head,multiples=main.split('17. Múltiplos:',1)
mult,tail=multiples.split('18. Riesgos,',1)
article='<article data-jmr-version="2026-10-16-adbe-final-roic25">'+paragraphs(head)
article+='<h2>17. Múltiplos como contraste secundario</h2><details><summary>Selección y comparación de múltiplos por escenario</summary>'
article+=paragraphs('Múltiplos:'+mult)+section('Múltiplos implícitos DCF',v['Múltiplos implícitos DCF'][3:9])+'</details>'
article+=paragraphs('18. Riesgos,'+tail)
article+='<h2>Matriz del DCF Base</h2>'+table(v['Sensibilidad DCF'][6:12])
article+='<p>El centro corresponde a ΔWACC0 y g3,5%: US$392,96. <a href="'+link('Sensibilidad DCF')+'">Ver todas las matrices y fórmulas</a>.</p>'
article+='<p><a href="'+sheet+'">Hoja vigente</a> · <a href="https://docs.google.com/document/d/1q3O4-5h_a9_qarFsgr0aaVlZv1Ke93h_QDolWHbbEK0/edit">Artículo fuente revisado</a></p></article>'
calc='<article data-jmr-calculations="2026-10-16-adbe-final-roic25"><h1>ADBE · Cálculos y supuestos</h1>'+paragraphs('20. Nivel 2'+technical)
inputs=[v['Input sheet'][n-1][:2] for n in [22,24,25,27,28,29,30,31,32,33,35,36,38,47,50,69,120]]
calc+=section('Input sheet',inputs)
for tab,rows in [('Escenarios e historias',v['Escenarios e historias'][3:15]),('Sensibilidad DCF',None),
                 ('DCF inverso',v['DCF inverso'][:10]),('Duración ventaja · FCFF',v['Duración ventaja · FCFF'][:11]),
                 ('Múltiplos implícitos DCF',v['Múltiplos implícitos DCF'][:20]),('Múltiplos históricos',None)]:
    calc+=section(tab,rows)
calc+='</article>'
card='<section class="jmr-valuation-card"><h2>Adobe · DCF Base US$'+f'{base:.2f}'+'</h2><p>MOS35%: US$'+f'{pm:.2f}'+' · Precio de referencia15-oct-2026: US$'+f'{price:.2f}'+'</p><p>Promedio de escenarios secundario: US$'+f'{expected:.2f}'+'</p>'+table([['Escenario','DCF USD/acción']]+[[k,x] for k,x in values.items()])+'</section>'
rec['analisisFundamental']=article+calc
for tab in ['Input sheet','Option value','Cost of capital worksheet','Escenarios e historias','Sensibilidad DCF','DCF inverso','Duración ventaja · FCFF','Múltiplos implícitos DCF']:
    rec['hojas']['valoracion'][tab]=section(tab)
rec['auditoria']={'fecha':now,'estado':'ESTRUCTURA Y ENTRADAS APROBADAS; SALVEDADES ECONÓMICAS EXPLÍCITAS',
    'anterior':old.get('auditoria'),'hojaOrigen':sid,
    'preflightOficial':{'status':'CERTIFICADO','fallos':0},'formulasCriticas':{'desviaciones':0,'gatesPendientes':0},
    'run':'https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/38917900764',
    'notas':['ROIC marginal terminal25%, g3.5%, margen40%.','12.2M RSU/PSU dentro del denominador401.4M, no doble deducción.',
             'ERP geográfica y spread Kd estimados; ESPP sin cuantificación separada.','Precio de análisis fijo; cotización actual se obtiene por separado.'],
    'visual':'Visor local del código productivo; producción requiere sesión privada de usuario.'}
rec['publicacion']={'version':'ADBE-20261016-roic25-option-reviewed','fecha':now,'autorizadaPorUsuario':True,
    'metodoPrincipal':'DCF Base','baseMOS':'dcfBase','hojaGoogle':sheet}

research={k:copy.deepcopy(research_old[k]) for k in ['id','ticker','logo','remotePath']}
linked={k:copy.deepcopy(value) for k,value in rec.items() if k not in ['analisisFundamental','hojas']}
linked['sourcePath']='valoraciones/ADBE-1789572982820.json'
research.update({'title':'Adobe: valoración JMR y monetización de IA','company':'Adobe Inc.','date':'2026-10-15',
    'price':price,'priceFetchedAt':'2026-10-15T20:00:00Z','updatedAt':now,'sourceName':'ADBE_Analisis_JMR_final_ROIC25_2026-10-15',
    'sourceMarkdown':text,'html':article+calc,'articleHtml':article,'calculationHtml':calc,'valuationHtml':card,
    'linkedValuation':linked,'linkedValuationAtResearch':copy.deepcopy(linked),'news':'',
    'analysisSchema':'jmr-work-20261014-v3','valorEsperado':rec['valorEsperado'],'escenariosDCF':rec['escenariosDCF'],
    'crecimientoImplicito':rec['crecimientoImplicito'],'valuationSync':{'fecha':now,'baseMatches':True,'mosMatches':True},
    'auditoriaEspecifica':rec['auditoria'],'publicacion':rec['publicacion']})

checks={
 'MOS_BASE':math.isclose(rec['precioMOS'],base*.65,abs_tol=1e-8),
 'FOUR_SCENARIOS':len(stories)==4,
 'PROBABILITIES':math.isclose(sum(x['probabilidad'] for x in stories),1),
 'EXPECTED':math.isclose(sum(x['probabilidad']*x['valor'] for x in stories),expected,abs_tol=1e-6),
 'INVERSE':rec['crecimientoImplicito']['dcfInverso']['errorAbsoluto']<.001,
 'LINKED_BASE':research['linkedValuation']['valorEsperado']['dcfBase']==base,
 'LINKED_MOS':research['linkedValuation']['precioMOS']==pm,
 'SENSITIVITY_CENTER':math.isclose(cell('Sensibilidad DCF','D10'),base,abs_tol=1e-8),
 'ROIC25':cell('Escenarios e historias','G5')==.25,
 'G35':cell('Escenarios e historias','J5')==.035,
 'NO_OLD_BASE':not any(x in research['html'] for x in ['484,92','484.92','237,99','237.99']),
 'MAIN_ID_PRESERVED':research['id']==research_old['id'],
}
assert all(checks.values()), checks
O=P/'output';O.mkdir(exist_ok=True)
for name,obj in [('ADBE-1789572982820.json',rec),('ADBE-research-1790475622244-a6a92.json',research),('ADBE-publication-controls.json',checks)]:
    (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'base':base,'mos':pm,'expected':expected,'checks':checks,'bytes':[len(json.dumps(rec)),len(json.dumps(research))]},ensure_ascii=False))
