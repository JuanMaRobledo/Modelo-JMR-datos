"""Llena la hoja de auditoría independiente (REGLAS §11) desde los archivos de la auditoría en el repositorio. No toca la hoja de valoración."""
import sys, json, csv, re
sys.path[:0]=['.','scripts']
from jmr_valuation.io.sheets_auth import get_gspread_client
AID='1YEUFaivTD62CGJq5nvOfZtLI_TZAp-BBQwRS_t4A2OY'; VAL='1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI'
D='/home/user/Modelo-JMR-datos/candidatos/valoraciones/AMZN-20261102-A12-R2/'
GH='https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/ccr-45b14ab1-3u0mt6/candidatos/valoraciones/AMZN-20261102-A12-R2/'
rep=open(D+'AUDITORIA_ECONOMICA_AMZN_R2.md').read(); ent=open(D+'FASE_4_ENTREGA.md').read()
def clean(c): return re.sub(r'\*\*|`','',c).strip()
def tabla(txt, cabecera_inicio):
    L=txt.split('\n'); i=[k for k,l in enumerate(L) if l.startswith(cabecera_inicio)][0]; rows=[]
    while i<len(L) and L[i].startswith('|'):
        if not re.match(r'^\|[-| ]+\|$',L[i]): rows.append([clean(c) for c in L[i].strip().strip('|').split('|')])
        i+=1
    return rows
hall=tabla(rep,'| ID | Severidad')
r3=tabla(rep,'| # | Celda (R3)')
ctrl=tabla(ent,'| Paso o control')
fuentes=[[l] for l in rep.split('## 18.')[1].split('**No verificado')[0].split('\n') if re.match(r'^\d+\. ',l)]
a1=json.load(open(D+'auditoria_fase4/alternativas.json')); a2=json.load(open(D+'auditoria_fase4/alternativas2.json')); r=json.load(open(D+'auditoria_fase4/resolucion_R3.json'))
base=a1['base']
pr=[['Prueba','Valor por acción (USD)','Δ vs Base R2 (%)','Archivo']]+[['Base R2 (réplica exacta)',round(base,4),0,'alternativas.json']]
for k,v in a1['alternativas'].items(): pr.append([k,round(v['ps'],4),round(v['pct'],2),'alternativas.json'])
for k,v in a2.items():
    if isinstance(v,dict): pr.append([k,round(v['ps'],4),round(v['pct'],2),'alternativas2.json'])
for k,v in r['paquetes_R3'].items(): pr.append(['R3 '+k,round(v['valor'],4),round(v['pct'],2),'resolucion_R3.json'])
b=r['beta_regresion']; pr.append(['Beta de regresión 60m (no es valor)',round(b['beta'],4),'',f"EE {b['error_estandar']:.3f}; R² {b['r2']:.2f}"])
pr.append(['Impuesto diferido total Anthropic (M USD; no es valor)',round(r['impuesto_diferido']['DTL_total']),'',"base preferentes 12.100"])
inv=list(csv.reader(open(D+'auditoria_fase4/inventario_entradas_R2.csv')))
resumen=[['Campo','Valor'],
 ['Empresa / ticker','Amazon.com, Inc. · AMZN'],['Revisión auditada','AMZN-20261102-A12-R2 (CANDIDATO; no en catálogo)'],
 ['Hoja de valoración',f'https://docs.google.com/spreadsheets/d/{VAL}/edit'],['Prompt','auditoria-economica-jmr-v1.3'],
 ['Versión de la auditoría','v2.1 · 2-nov-2026'],['Auditor','Claude Code · claude-opus-5-5 · esfuerzo high · sesión distinta de las fases 2 y 3 (ChatGPT/Codex)'],
 ['Dictamen','PENDIENTE'],['Tesis económica','Plausible con reservas'],
 ['Bloqueantes','A-01 prima de riesgo no es la del corte (+12 % a +20 %); A-02 arrendamientos contados dos veces (+6,2 % a +6,6 %)'],
 ['Valor Base R2 (oficial, sin cambios)','148,68 USD · MOS 96,64'],['R3 central propuesto (auditor, no oficial)','185,32 USD · MOS 120,46 · rango 169,0–197,8'],
 ['Precio del análisis','240,35 USD (30-oct-2026)'],['Margen terminal implícito en el precio (R3 central)','22,4 %'],
 ['Modificaciones a la valoración','Ninguna: 0 escrituras en la hoja, el JSON o el análisis por parte de la auditoría'],
 ['Nota de independencia','La adenda de fase 3 sobre Anthropic/OpenAI (2-nov-2026) se redactó en la misma sesión: requiere revisión independiente'],
 ['Informe completo (18 secciones)',GH+'AUDITORIA_ECONOMICA_AMZN_R2.md'],['Entrega fase 4',GH+'FASE_4_ENTREGA.md'],['Evidencia reproducible',GH+'auditoria_fase4'],
 ['Publicación en auditorias/narrativas','No publicada (requiere autorización expresa)']]
sh=get_gspread_client().open_by_key(AID)
tabs=[('Resumen',resumen),('Hallazgos',hall),('R3 propuesto',r3),('Pruebas',pr),('Controles',ctrl),('Inventario entradas',inv),('Fuentes',[['Fuente']]+fuentes)]
ws0=sh.sheet1
for i,(name,data) in enumerate(tabs):
    ws=ws0 if i==0 else sh.add_worksheet(title=name,rows=max(len(data)+5,20),cols=max(len(r) for r in data)+1)
    if i==0: ws.update_title(name); ws.resize(rows=max(len(data)+5,20),cols=max(len(r) for r in data)+1)
    w=max(len(r) for r in data); data=[r+['']*(w-len(r)) for r in data]
    ws.update(values=data,range_name='A1',value_input_option='RAW' if name!='Pruebas' else 'USER_ENTERED')
    ws.format('1:1',{'textFormat':{'bold':True}}); ws.freeze(rows=1)
    print(name,len(data),'filas')
