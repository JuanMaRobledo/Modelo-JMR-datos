"""Conciliar registros con lecturas nativas verificadas, sin alterar supuestos DCF.

Uso: python scripts/reconciliar_publicacion_20261019.py /ruta/JMR-review
Las lecturas se conservan fuera del repositorio; el manifiesto contiene referencias
y controles. Los antecedentes publicados siguen disponibles en git.
"""
import copy, datetime, hashlib, html, json, math, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
METHODS=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV']
TABS=['EVEBITDA','EVFCFF','PE','PFCFE','POCF','PV','PBV']
SCEN=['conservador','base','optimista']
STAMP=datetime.datetime.now(datetime.timezone.utc).isoformat()
VERSION='cierre-integridad-20261019-v1'
REVIEWS={
 'AAPL':'Se mantienen los cinco relativos publicados. Revisar recompras, SBC y capitalización de servicios frente a hardware; no usar el patrimonio contable como sustituto de valor económico. El corte de pares sigue siendo el documentado.',
 'ADSK':'Se mantienen los relativos de la hoja. EBITDA, utilidad y flujo requieren el mismo tratamiento de SBC, arrendamientos y deuda. Los denominadores históricos reconstruidos no equivalen a FCF reportado; no se aplica una conversión uniforme a toda la historia.',
 'ADBE':'Se conservan las anclas restituidas por decisión del usuario. EBITDA y P/E requieren normalizar SBC y contrastar crecimiento y reinversión; los otros métodos siguen visibles con su peso efectivo, sin crear una selección nueva.',
 'SHAK':'El crecimiento de locales no justifica por sí solo una prima frente a restaurantes con mayor ROIC. Se conservan los pesos vigentes, con EV/FCFF y P/FCFE excluidos; falta un ajuste de pares sustentado en margen, reinversión y arrendamientos. La brecha no se corrige forzando el múltiplo hacia el DCF.',
 'PLTR':'El histórico de hipercrecimiento y la prima de pares requieren revisar SBC, crecimiento FY+3 y margen normalizado. No extrapolar el crecimiento inmediato al régimen estable ni tratar como independientes múltiplos justificados y DCF que comparten supuestos.',
 'CELH':'Normalizar pagos y terminaciones de distribución, adquisiciones y el periodo de expansión. Los pares de bebidas difieren en margen, ROIC y crecimiento; las ponderaciones publicadas conservan salvedades mientras se verifica esa homogeneidad.',
 'PFE':'La expiración de patentes, adquisiciones y deuda exigen beneficio y flujo normalizados. Los pares propuestos carecen de ajuste documentado por crecimiento, margen y riesgo; se conserva la selección publicada como provisional.',
 'MCD':'La franquicia, el refranquiciamiento y los arrendamientos limitan la comparación de ingresos con restaurantes operados directamente. P/BV no representa bien el patrimonio afectado por recompras; no se sustituye un N/D por cero.',
 'NVO':'Revisar márgenes y crecimiento normalizados frente a presión de precios, competencia y pipeline. La comparación histórica procede de otro corte del DCF; se conservan anclas y pesos hasta contrastar pares contemporáneos.',
 'NVDA':'Revisar normalización del ciclo, márgenes y crecimiento de IA; los pares de semiconductores no deben tomarse como equivalentes por etiqueta sectorial. Las diferencias entre versiones anteriores del DCF no justifican cambiar las anclas.',
 'AMZN':'Los pares mezclan comercio, nube y publicidad. EV/EBITDA no captura por sí solo el CapEx de IA y P/E depende de la mezcla de negocios; se conserva el peso publicado con revisión por segmentos pendiente.',
 'AFYA':'El nicho de educación médica, regulación y márgenes difiere de otras educadoras brasileñas. Conservar la mediana ajustada publicada como hipótesis, y documentar fuentes y ajuste por ROIC, crecimiento y riesgo antes de recalibrar.',
 'EPAM':'Separar el riesgo estructural de IA del ciclo de contratación. Revisar margen, utilización, caja y recompras frente a consultoras comparables; no usar el DCF de una versión anterior para validar la brecha actual.',
 'MP':'Se respeta la decisión explícita de 80% DCF y 20% P/V. El P/V procede de una historia corta y sigue provisional: requiere margen neto sostenible, reinversión y riesgo. Los métodos de utilidad y flujo excluidos no se reactivan por obtener una cifra numérica.',
 'NFLX':'Se conservan 60% DCF y 40% relativos y el selector de horizonte vigente. Revisar tratamiento del contenido, reinversión y comparación con negocios de medios heterogéneos. El MOS sigue anclado al DCF Base.',
}
def finite(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def near(a,b): return finite(a) and finite(b) and abs(a-b)<=max(1e-7,abs(b)*1e-10)
def col(n):
 s=''
 while n: n,r=divmod(n-1,26);s=chr(65+r)+s
 return s
def value(l,t,a):
 e=l['sheets'].get(t,{}).get('cells',{}).get(a,{}).get('effectiveValue',{})
 return e.get('numberValue',e.get('stringValue',e.get('boolValue')))
def num(l,t,a):
 v=value(l,t,a);return v if finite(v) else None
def trio(l,t,row):return {k:num(l,t,c+str(row)) for k,c in zip(SCEN,'CDE')}
def table(l,t):
 sh=l['sheets'][t];cells=sh['cells'];rs=[int(re.search(r'\d+',a)[0]) for a in cells]
 rows=[];cols=min(sh['properties']['gridProperties']['columnCount'],17)
 for r in range(1,max(rs,default=0)+1):
  out=[]
  for c in range(1,cols+1):
   x=cells.get(col(c)+str(r),{});v=num(l,t,col(c)+str(r));e=x.get('effectiveValue',{})
   if e.get('errorValue'):raise ValueError(f'{l["ticker"]}: error de fórmula en {t}!{col(c)}{r}')
   attr=f' data-value="{v}"' if finite(v) else ''
   out.append(f'<td{attr}>'+html.escape(str(x.get('formattedValue','')))+' pilcrowTOKEN</td>')
  rows.append(f'<tr data-row="{r}">'+''.join(out)+'</tr>')
 return '<h3>'+html.escape(t)+'</h3><div class="table-wrap"><table class="jmr-table jmr-sheet"><tbody>'+''.join(rows).replace(' pilcrowTOKEN','')+'</tbody></table></div>'
def matrix_checks(l,economic=False):
 tab='Sensibilidad económica múltiplos' if economic else 'Sensibilidad por múltiplo'
 if tab not in l['sheets']:return []
 out=[]
 for si,k in enumerate(SCEN):
  for mi,m in enumerate(METHODS):
   r=(11 if economic else 6)+(si*7+mi)*10
   center=num(l,tab,'D'+str(r+5))
   original=num(l,tab,'G'+str(r+8)) if not economic else None
   formulaErrors=[]
   for rr in range(r+3,r+8):
    for c in 'BCDEF':
     if l['sheets'][tab]['cells'].get(c+str(rr),{}).get('effectiveValue',{}).get('errorValue'):formulaErrors.append(c+str(rr))
   state='ERROR' if formulaErrors else 'OK' if finite(center) and (economic or near(center,original)) else 'N/D' if center is None else 'DESCUADRE'
   out.append({'metodo':m,'escenario':k,'centro':center,'vp3Original':original,'estado':state,'formulaErrors':formulaErrors})
 return out
def counter(ledger):return {'controlesOK':sum(x['estado']=='OK' for x in ledger),'noDisponibles':sum(x['estado']=='N/D' for x in ledger),'errores':sum(x['estado'] in ('ERROR','DESCUADRE') for x in ledger),'controles':ledger}
def money(n,currency):
 if not finite(n):return 'N/D'
 s=f'{n:,.2f}'.translate(str.maketrans(',.','.,'))
 return ('COP ' if currency=='COP' else 'US$ ')+s
def block(a):
 t=a['ticker'];curr='COP' if t.startswith(('GRUPO','PF')) else 'USD';base=a['valorPrincipal'];h=a.get('valoracionHolding');dm=a.get('descuentoMultiples') or {};sel=a.get('seleccionMultiples') or {};s=a['sensibilidadMultiples'];eco=s.get('economica',{})
 rows=[]
 for m in sel.get('metodos',[]):
  ss=m.get('salida') or {};fmt=lambda n:f'{n:.2f}×' if finite(n) else 'N/D'
  rows.append('<tr>'+''.join('<td>'+html.escape(str(v))+'</td>' for v in [m['nombre'],f'{100*m.get("pesoVigente",0):.1f}%',fmt(m.get('historico')),fmt(m.get('proxySectorial')),fmt(ss.get('conservador')),fmt(ss.get('base')),fmt(ss.get('optimista')),m.get('control',''),m.get('criterio','')])+'</tr>')
 lead=f'<section data-jmr-cierre="{VERSION}" id="cierre-{t.lower()}"><h2>Valoración vigente · {t} · 19-oct-2026</h2><p><strong>Método principal: {a["metodoPrincipal"]}. Base: {money(base,curr)} por acción. MOS {a["mos"]*100:g}%: {money(a["precioMOS"],curr)}.</strong> El MOS se aplica únicamente al Base principal. Conservador, Base y Optimista se presentan separados de Disrupción.</p>'
 if h:lead+='<p>SOTP referencial: cotizadas a mercado de junio y no cotizadas a valor en libros. El DCF es opcional, sin peso y no condiciona este SOTP. Pendiente valorar económicamente las no cotizadas y actualizar el capital y la matriz al mismo corte.</p>'
 else:
  weights=' / '.join(f'{m["nombre"]} {100*m["peso"]:g}%' for m in a['metodos'] if (m.get('peso') or 0)>0)
  lead+=f'<p>Pesos vigentes: {html.escape(weights)}. Múltiplos Base hoy: {money((dm.get("multiplesHoy") or {}).get("base"),curr)}; combinado Base hoy: {money((dm.get("ponderadoHoy") or {}).get("base"),curr)}; objetivo combinado FY+3: {money((a.get("objetivoPonderado") or {}).get("base"),curr)}. Criterio de descuento: {html.escape(dm.get("criterio",""))}. Estos resultados son secundarios y no determinan el MOS.</p>'
 lead+=f'<p>Control de matrices de precio: {s["controlesOK"]}/21 conciliadas; {s["noDisponibles"]} N/D. Matrices económicas: {eco.get("controlesOK",0)} centros numéricos; {eco.get("noDisponibles",0)} N/D. N/D no se convierte en cero. La conciliación aritmética no valida por sí sola comparables o anclas.</p>'
 review=a.get('revisionPorEmpresa',{})
 lead+='<p><strong>Revisión por empresa:</strong> '+html.escape(review.get('conclusion',''))+'</p>'
 lead+='<p>'+html.escape(sel.get('advertencia',''))+'</p>'
 if rows:lead+='<details><summary>Selección y fundamento de los siete múltiplos</summary><div class="table-wrap"><table class="jmr-table"><thead><tr>'+''.join('<th>'+x+'</th>' for x in ['Método','Peso','Historia','Pares','Conservador','Base','Optimista','Control','Criterio'])+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div></details>'
 for tab in ['Sensibilidad por múltiplo','Sensibilidad económica múltiplos']:
  text=a['hojas']['valoracion'].get(tab)
  if text:lead+='<details><summary>'+tab+'</summary>'+text+'</details>'
 lead+='<p><a href="'+html.escape(a['hojaGoogle'],quote=True)+'">Abrir hoja vigente</a>. Las cifras de este bloque prevalecen sobre los antecedentes fechados que siguen.</p></section>'
 return '<!--jmr-cierre-start-->'+lead+'<!--jmr-cierre-end-->'
def prepend(text,new):
 text=re.sub(r'<!--jmr-cierre-start-->[\s\S]*?<!--jmr-cierre-end-->','',text or '')
 # Preserve earlier narrative and source evidence; label old numerical summaries.
 text=re.sub(r'<!--jmr-sync-start-->[\s\S]*?<!--jmr-sync-end-->','',text)
 text=re.sub(r'<p class="jmr-antecedente">[\s\S]*?</p>','',text)
 return new+'<p class="jmr-antecedente">Antecedentes y tesis: conservar sus fechas; las cifras vigentes figuran arriba.</p>'+text
def main(review):
 changes=[];audits=[]
 for p in sorted((ROOT/'valoraciones').glob('*.json')):
  a=json.loads(p.read_text());old=copy.deepcopy(a);t=a['ticker'];l=json.loads((review/'live'/f'{t}.json').read_text());h=a.get('valoracionHolding')
  base=h['nav']['base'] if h else num(l,'Resumen de Valoración','D32')
  oldbase=(a.get('escenariosDCF') or {}).get('base') or (a.get('valorEsperado') or {}).get('valorCentral')
  if not h and not near(base,oldbase):raise ValueError(f'{t}: cambió el DCF principal: requiere auditar supuestos')
  if not finite(base):raise ValueError(f'{t}: principal no numérico')
  a.update(metodoPrincipal='SOTP' if h else 'DCF FCFF',valorPrincipal=base,savedAt=STAMP)
  if t in ['NU','PFDAVVNDA']:a['metodoPrincipal']='Modelo financiero provisional · FCFE pendiente'
  if t=='PAGS':a['metodoPrincipal']='Modelo financiero provisional · revisión sectorial pendiente'
  if t in ['GRUPOSURA','PFGRUPSURA']:a['metodoPrincipal']='Modelo financiero provisional · SOTP pendiente'
  a['precioMOS']=base*(1-a['mos']);a['precioMOSMax']=a['precioMOS']
  # Preserve the MOS percentage and every DCF scenario; refresh source-linked outputs only.
  checks=matrix_checks(l);ec=matrix_checks(l,True);counts=counter(checks);eco=counter(ec)
  if counts['errores'] or eco['errores']:raise ValueError(f'{t}: matrices con errores')
  a['sensibilidadMultiples'].update({**counts,'version':'matrices-por-bloque-20261019','lastExport':'2026-10-19','seleccion':'Pesos y criterio de la hoja vigente; contadores por matriz, no por celda'})
  a['sensibilidadMultiples']['economica']={**eco,'version':'20261019','matrices':len(ec),'fuente':l['id'],'unidad':'Múltiplo económico en veces (×), no precio'}
  methods={x['nombre']:x for x in a.get('metodos',[])}
  if not h:
   dm=copy.deepcopy(a.get('descuentoMultiples') or {});dm.update(version=3,horizontes=[1,2,3],horizonteAnios=3,costoPatrimonio=num(l,'Descuento de múltiplos','B5'),criterio=value(l,'Descuento de múltiplos','B6'),dcfHoy=trio(l,'Descuento de múltiplos',38),multiplesHoy=trio(l,'Descuento de múltiplos',39),ponderadoHoy=trio(l,'Descuento de múltiplos',40),pesoDcf=num(l,'Descuento de múltiplos','B38'),pesoMultiplos=num(l,'Descuento de múltiplos','B39'),metodos=[])
   total=dm['pesoMultiplos'];newmethods=[]
   dcf=next(x for x in a['metodos'] if 'DCF' in x['nombre']);newmethods.append(dcf)
   for mi,(m,tab) in enumerate(zip(METHODS,TABS)):
    weight=num(l,'Resumen de Valoración','B'+str(mi+7)) if mi<5 else .2 if t=='MP' and m=='P/V' else 0
    x={'nombre':m,'peso':weight,'pesoMultiplos':weight/total if total else 0};out={'nombre':m,'peso':weight}
    for si,k in enumerate(SCEN):
     if mi<5:
      r=[11,20,29][si]+mi;fy=[num(l,'Descuento de múltiplos',c+str(r)) for c in 'DEF'];vp=[num(l,'Descuento de múltiplos',c+str(r)) for c in 'GHI'];cons=num(l,'Descuento de múltiplos','J'+str(r));check=value(l,'Descuento de múltiplos','K'+str(r))
     else:
      r=[12,23,34][si];fy=[num(l,tab,c+str(r)) for c in 'FGH'];vp=[num(l,tab,c+str(41+si)) for c in 'BCD'];cons=num(l,tab,'E'+str(41+si));check='OK' if all(finite(z) for z in vp) else 'N/D'
     x[k]={'fy':fy,'vp':vp,'consolidado':cons,'chequeo':check};out[k]=fy[2]
    dm['metodos'].append(x);newmethods.append(out)
   a['metodos']=newmethods;a['descuentoMultiples']=dm
   a['objetivoPonderado']=trio(l,'Descuento de múltiplos',50);a['valorPresentePonderado']=dm['ponderadoHoy']
   dm['vp3']={k:sum(x['peso']*x[k]['vp'][2] for x in dm['metodos'] if x['peso']>0)/total if total and all(finite(x[k]['vp'][2]) for x in dm['metodos'] if x['peso']>0) else None for k in SCEN}
   dm['consolidado']={k:{'fy':[sum(x['peso']*x[k]['fy'][n] for x in dm['metodos'] if x['peso']>0)/total for n in range(3)] if total else [None]*3,'vp':[sum(x['peso']*x[k]['vp'][n] for x in dm['metodos'] if x['peso']>0)/total for n in range(3)] if total else [None]*3,'consolidado':dm['multiplesHoy'][k]} for k in SCEN}
   dm['chequeo']={'multiplosFY3SinDescontar':trio(l,'Descuento de múltiplos',47),'multiplosVP3':trio(l,'Descuento de múltiplos',48),'resultado':{k:value(l,'Descuento de múltiplos',c+'49') for k,c in zip(SCEN,'CDE')}}
   for k in SCEN:
    computed=sum(x['peso']*x[k]['consolidado'] for x in dm['metodos'] if x['peso']>0)/total if total else None
    if total and not near(computed,dm['multiplesHoy'][k]):raise ValueError(f'{t}/{k}: consolidado no concilia {computed} vs {dm["multiplesHoy"][k]}')
    if not near(dm['dcfHoy'][k]*dm['pesoDcf']+dm['multiplesHoy'][k]*total,dm['ponderadoHoy'][k]):raise ValueError(f'{t}/{k}: combinación no concilia')
   if not near(num(l,'Resumen de Valoración','D36'),a['precioMOS']):raise ValueError(f'{t}: MOS nativo no concilia')
  selection=a.get('seleccionMultiples') or {};selection['advertencia']='Pesos leídos de la hoja vigente. Los pares y anclas conservan su corte documentado; no se presumen homogéneos ni actuales. La revisión de integridad no equivale a validación de supuestos.'
  for x in selection.get('metodos',[]):
   m=x['nombre'];actual=next((z for z in a['metodos'] if z['nombre']==m),{});x['pesoVigente']=actual.get('peso',0)
   tab=TABS[METHODS.index(m)];x['salida']={k:num(l,tab,'J'+str(r)) for k,r in zip(SCEN,[8,19,30])}
   available=all(z['estado']=='OK' for z in checks if z['metodo']==m) and len(checks)==21
   x['controlCalculo']='OK' if available else 'N/D';x['control']='OK · advertencias económicas' if available else 'N/D'
   if h:x['control']='N/D';x['pesoVigente']=0;x['rol']='No elegible · SOTP'
  if t=='MP':
   selection['advertencia']+=' Excepción aprobada: 80% DCF / 20% P/V; P/V sigue siendo un ancla histórica provisional, no una conclusión económica.'
   for x in a.get('multiplesAdicionales',{}).get('metodos',[]):x['peso']=.2 if x['nombre']=='P/V' else 0
  selection['integridadVersion']=VERSION;a['seleccionMultiples']=selection
  dossier=review/'dossiers'/f'{t}.json';d=json.loads(dossier.read_text()) if dossier.exists() else {};decision=d.get('decision',{})
  conclusion=REVIEWS.get(t) or 'Se conciliaron los siete métodos y sus horizontes con la hoja vigente. Se conservan las anclas y pesos publicados, con sus criterios por método. Falta evidencia contemporánea y homogénea de comparables antes de recalibrarlos; el expediente anterior conserva su fecha y no valida automáticamente las cifras vigentes.'
  if t in ['NU','PFDAVVNDA','PAGS']:conclusion='El motor consolidado vigente no se identifica como FCFE validado sólo por ser una financiera. Falta conciliar capital regulatorio y flujo distribuible al accionista por negocio; se conserva la cifra publicada como provisional y los múltiplos como contraste secundario.'
  if h:conclusion='SOTP principal conciliado. Cotizadas a junio, no cotizadas a libro y recompra proforma: referencia híbrida, con valoración económica de no cotizadas pendiente. El DCF opcional no bloquea el SOTP.'
  if t in ['GRUPOSURA','PFGRUPSURA']:conclusion='La hoja aún presenta un modelo consolidado financiero. Falta SOTP atribuible por participaciones; no se reclasifica este resultado como SOTP ni se da por validado.'
  a['revisionPorEmpresa']={'fecha':'2026-10-19','alcance':'Integridad nativa y revisión de evidencia existente; sin alterar supuestos DCF ni forzar múltiplos para aproximarlos al DCF','conclusion':conclusion,'fuentesExpediente':decision.get('fuentes',[]),'expediente':f'JuanMaRobledo/JMR-valuation/reference/multiplos_v3/{t}_decision_resultado.json' if d else None,'pendientesEconomicos':True,'estado':'CONCILIADO_CON_SALVEDADES'}
  for tab in l['sheets']:
   if tab not in ['Input sheet'] and tab in a['hojas']['valoracion'] or tab in ['Resumen de Valoración','Descuento de múltiplos','Sensibilidad por múltiplo','Sensibilidad económica múltiplos']:
    a['hojas']['valoracion'][tab]=table(l,tab)
  a['controlPublicacion']={'version':VERSION,'fecha':STAMP,'fuenteHoja':l['id'],'dcfPrincipalSinCambios':True,'mosConciliado':True,'matricesPrecio':counts['controlesOK'],'matricesPrecioND':counts['noDisponibles'],'matricesEconomicas':eco['controlesOK'],'matricesEconomicasND':eco['noDisponibles'],'comparablesValidados':False,'verificacionVisual':'PENDIENTE'}
  newblock=block(a);a['analisisFundamental']=prepend(a.get('analisisFundamental',''),newblock)
  for group in a['hojas'].values():
   for name,text in list(group.items()):
    if ('Tesis' in name or name=='Informe de valoración') and isinstance(text,str):group[name]=prepend(text,newblock)
  p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
  for q in (ROOT/'analisis').glob(t+'-research-*.json'):
   j=json.loads(q.read_text());linked=j.get('linkedValuation') or {};linkedid=re.search(r'/d/([\w-]+)',linked.get('hojaGoogle',''))
   if linkedid and linkedid[1]!=l['id']:raise ValueError(f'{t}: análisis vinculado a otra hoja')
   for key in ['metodoPrincipal','valorPrincipal','valoracionHolding','descuentoMultiples','metodos','objetivoPonderado','valorPresentePonderado','precioMOS','baseMOS','sensibilidadMultiples','seleccionMultiples','controlPublicacion','revisionPorEmpresa']:
    if key in a:j[key]=copy.deepcopy(a[key])
   j['linkedValuation']=copy.deepcopy(a);j['updatedAt']=STAMP
   for key in ['html','articleHtml','valuationHtml']:j[key]=prepend(j.get(key,''),newblock)
   j['calculationHtml']=prepend(j.get('calculationHtml',''),newblock)
   j.setdefault('valuationSync',{}).update(updatedAt=STAMP,base=base,threshold=a['precioMOS'],baseMOS=a['baseMOS'],scope='Conciliación nativa de siete múltiplos, MOS y contadores por matriz',sourcePath=str(p.relative_to(ROOT)),sourceSavedAt=STAMP)
   q.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
  audits.append({'ticker':t,'path':str(p.relative_to(ROOT)),'metodoPrincipal':a['metodoPrincipal'],'base':base,'MOS':a['precioMOS'],'pesoTotal':sum(x.get('peso',0) for x in a['metodos']),'matricesOK':counts['controlesOK'],'matricesND':counts['noDisponibles'],'economicasOK':eco['controlesOK'],'economicasND':eco['noDisponibles'],'estado':'CONCILIADO_CON_SALVEDADES','antesSHA256':hashlib.sha256(json.dumps(old,sort_keys=True).encode()).hexdigest()})
  changes.append(t)
 (ROOT/'auditorias/cierre-valoraciones-2026-10-19.json').write_text(json.dumps({'version':VERSION,'fecha':STAMP,'empresas':len(audits),'supuestosDCFCambiados':False,'pendientes':['Comparables contemporáneos y homogéneos por empresa','Valor económico de no cotizadas de Grupo Argos','SOTP de Grupo Sura ordinaria y PF','Integración sectorial del publicador Colombia'],'entradas':audits},ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'empresas':len(changes),'matricesOK':sum(x['matricesOK'] for x in audits),'matricesND':sum(x['matricesND'] for x in audits)},ensure_ascii=False))
if __name__=='__main__':main(Path(sys.argv[1]))
