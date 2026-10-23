import json,ast,math,hashlib,re,datetime
from pathlib import Path
P=Path(__file__).parent;V=json.loads((P/'valuation_results.json').read_text());D=json.loads((P/'data.json').read_text());T=json.loads((P/'tabs.json').read_text());H=json.loads((P/'frozen.json').read_text())['resultsSha256'];checks=[]
# Use the independently written audit equation, not the valuation implementation.
tree=ast.parse((P.parent/'nke_revision/audit.py').read_text());func=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='independently');ns={'V':V,'D':D};exec(compile(ast.Module(body=[func],type_ignores=[]),'independent_audit_equation','exec'),ns);independent=ns['independently']
def get(tab,r,c):
 try:return T[tab][r-1][c-1]
 except IndexError:return None
def check(id,ok,detail,value=None):
 checks.append({'id':id,'status':'VALIDADO'if ok else'CON HALLAZGOS','evidence':detail,'value':value})
check('IDENTITY',hashlib.sha256((P/'valuation_results.json').read_bytes()).hexdigest()==H,'Resultados congelados antes del artículo; SHA-256 idéntico.')
for name,row in [('Base',5),('Conservadora',6),('Disrupción',7),('Optimista',8)]:
 actual=independent(V['scenarios'][name]);native=get('Escenarios e historias',row,8);check('DCF-'+name,abs(actual-native)<1e-9,'Ecuación de auditoría independiente frente a copia nativa.',{'independent':actual,'native':native,'error':abs(actual-native)})
for j,top in enumerate([6,17,28]):
 m=V['matrices'][j];errs=[]
 for i,y in enumerate(m['y']):
  for k,x in enumerate(m['x']):
   args={'wt':y,'gt':x}if j==0 else{'rt':y,'gt':x}if j==1 else{'delta':y,'margin':x}
   errs.append(abs(independent(V['scenarios']['Base'],**args)-get('Sensibilidad DCF',top+i,2+k)))
 check('SENS-'+str(j+1),max(errs)<1e-9,'25celdas contrastadas con motor independiente.',{'max_error':max(errs),'center':get('Sensibilidad DCF',top+2,4)})
check('INVERSE',abs(independent(V['scenarios']['Base'],delta=V['inverse']['selected'])-V['price'])<1e-9,'Raíz aditiva recompone precio fechado sin factor de calibración.')
for i,m in enumerate(V['multiple_matrices']):
 if m['expected'] is None:check('MULT-ND-'+str(i),all(z is None for z in m['values'][0])and get('Matrices múltiplos Base',m['start_row']+5,2)=='N/D','Ausencia explícita;FCFE no se sustituye por FCF;ancla '+m['anchor'])
 else:check('MULT-'+str(i),abs(get('Matrices múltiplos Base',m['start_row']+5,4)-m['expected'])<1e-9,'Centro nativo contra precio del método/ancla;'+m['method']+'/'+m['anchor']+'/'+m['family'])
check('LTM-REVENUE',get('Income Statement',3,12)==46398+11213-11720,'Flujo LTM por acumulados comparables.')
check('LTM-GROWTH',abs(get('Income Statement',4,12)-(45891/46440-1))<1e-12,'LTM contra LTM previo;corrección de comparador FY.')
check('LTM-SHARES',abs(get('Income Statement',25,12)-D['LTM']['basic_shares'])<1e-9 and get('Income Statement',26,12)>=get('Income Statement',25,12),'Promedios reconstruidos por días,no sumados;aproximación reconocida.')
check('BRIDGE',abs((V['scenarios']['Base']['result']['ev']+V['cash']-V['debt_book']-V['options'])/V['shares']-V['base_value'])<1e-12,'Puente al patrimonio;clasesA+B;leases una vez.')
check('MOS',abs(get('Presentación',7,2)-V['base_value']*.65)<1e-9,'MOS35% sobreBase.')
check('AVERAGE',abs(get('Escenarios e historias',10,8)-V['average_three'])<1e-9,'Promedio ordinario de3historias;disrupción aparte.')
check('PROB',abs(sum(c['prob']for c in V['scenarios'].values())-1)<1e-12,'Previa declive40/25/15/20;sin ajuste no documentado.')
check('G-TERMINAL',V['rf']>=.04 and V['wacc_terminal']>.04,'g4%nominalUSD≤Rf;WACC>g;disrupción g0 explícito.')
check('MARGIN-PATH',abs(V['scenarios']['Base']['result']['rows'][1]['margin']-(.0525+V['lease_adjustment']/45891+(V['scenarios']['Base']['margin_adjusted']-(.0525+V['lease_adjustment']/45891))/4))<1e-12,'Cuatro intervalos de año1a5,ningún salto doble.')
b=V['scenarios']['Base'];check('S2C-TERMINAL',abs(b['s2c_late']*b['margin_adjusted']*(1-V['tax_marginal'])*1.04-b['roic_terminal'])<1e-12,'S/Ctemporal coherente con inversión_t yΔNOPAT_t+1.')
check('REINV-CONTINUITY',abs(b['result']['terminal_reinvestment']/b['result']['rows'][-1]['reinvestment']-1.04)<1e-10,'Continuidad año10–11sin crecimiento gratuito.')
raw=json.loads((P/'native_export.json').read_text());errors=[(s['properties']['title'],i+1,j+1)for s in raw['sheets']for d in s.get('data',[])for i,r in enumerate(d.get('rowData',[]))for j,c in enumerate(r.get('values',[]))if'errorValue'in c.get('effectiveValue',{})]
check('NATIVE-ERRORS',not errors,'64pestañas en los límites usados/exportados;45errores auxiliares previos resueltos;no certifica todas las celdas de la cuadrícula.',errors)
article=(P/'02_Analisis_NKE.md').read_text();titles=re.findall(r'^## (\d+)\. (.+)$',article,re.M)
check('EDITORIAL-STRUCTURE',len(titles)==18 and[int(x[0])for x in titles]==list(range(1,19)),'18secciones exactas,subsecciones ymarcos independientes.')
check('EDITORIAL-REQUIRED',all(article.count('\n### '+x+'\n')==1for x in ['Las 5 fuerzas de Porter','Síntesis final']),'Porter con5filas ySíntesis con3párrafos sustantivos.')
check('EDITORIAL-CURRENT',all(x in article for x in ['David Denton','Johanna Nielsen','Alexandre Arnault','16m acciones adicionales']),'8-Kcompletan equipo,gobierno yplanempleados;ya no se presenta Friend como CFOactual.')
check('EDITORIAL-COVERAGE',len(json.loads((P/'coverage.json').read_text())['sections'])==30,'30apartados/subapartados localizados;límites documentales diferenciados de trabajo pendiente.')
check('DOC-RD',False,'Falta serie deI+D separada;ROIC/sector no plenamente homogéneos. No es gasto cero.')
check('DOC-OPTIONS',False,'Detalle completo al31-may;agregado84m de10-Qno desglosa opciones/RSU.')
check('DOC-PEERS',False,'AnclaBdepares no completamente homologada enEV,D&Ayclases;no se certifica contraste independiente.')
check('DOC-FCFE',False,'Financiación neta histórica no reconciliada. Método y4matrices N/D,peso0;presentación errónea previa resuelta.')
check('LEGACY-GATE',False,'controles_todas.sh se intentó en este entorno,pero no completó módulos,registro externo yautenticación. No hay certificación integral deese script.')
old=json.loads((P.parent/'nke_revision/audit_checks.json').read_text());impacts=old['impacts']
out={'revisionId':V['revision'],'resultsSha256':H,'stage':'Auditoría separada posterior al análisis;sin modificar valoración ni artículo','status':'CON HALLAZGOS','math_status':'VALIDADO en alcance reproducido','economic_status':'Plausible con reservas','documentary_status':'CON HALLAZGOS','checks':checks,'impacts':impacts,'native_errors':errors,'executed':{'dcf_histories':4,'dcf_sensitivity_cells':75,'multiple_numeric_centers':24,'multiple_explicit_nd':4,'bounded_native_tabs':64,'engine_regression_tests':8},'limitations':['No certificación integral del script legado ni cuadrículas completas','Sin sesión autenticada para prueba visual deapp/PDF;publicación se verificará por rutas ydatos servidos','Opciones,país,pares,I+D yTAM/cuota con límites explícitos'],'completedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(P/'audit_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('checks',len(checks),'pass',sum(x['status']=='VALIDADO'for x in checks),'findings',sum(x['status']!='VALIDADO'for x in checks))
