import json,math
from pathlib import Path
from model import RAW,SCENARIOS,SOURCES,derive,calculate
P=Path(__file__).parent
spec={};formats={};headers={};cols={};R={}
def put(sn,a,v): spec.setdefault(sn,{})[a]=v
def c(n):
 r=''
 while n:n,z=divmod(n-1,26);r=chr(65+z)+r
 return r
sn='Datos y ajustes';put(sn,'C2','CMG R4 · insumos y recast de arrendamientos')
put(sn,'C3','USD millones; acciones en millones. Datos publicados y proxies diferenciados.')
for j,x in enumerate(['Concepto','Valor','Estado','Fuente y período'],3):put(sn,f'{c(j)}4',x)
for i,(k,v) in enumerate(RAW.items(),5):
 R[k]=f"'{sn}'!D{i}";put(sn,f'C{i}',k);put(sn,f'D{i}',v)
 state='Dato publicado'
 source=SOURCES['Q3']+' · 30-sep-2026'
 if k.endswith('_fy') or k.endswith('_fy_prior') or k in ['lease_rate','fixed_rent_fy','new_capex_per_unit','maintenance_capex_2026','newbuild_capex_2026','total_capex_2026']:source=SOURCES['FY25']+' · FY2025 / guía 2026'
 if k in ['new_capex_per_unit','new_lease_capital_per_unit']:state='Juicio / proxy, no costo individual publicado'
 if k in ['price']:source=SOURCES['price']+' · cierre 04-nov-2026'
 if k in ['treasury']:source=SOURCES['Rf']+' · 04-nov-2026'
 if k in ['us_default','erp_treasury']:source=SOURCES['ERP']+' · 01-nov-2026'
 if k in ['beta_unlevered','vol']:source=SOURCES['beta']+' · enero 2026, sector; volatilidad proxy'
 if k in ['tax','kd']:state='Juicio';source='25% tasa marginal; Kd=6% supuesto, rango5,5–6,5%'
 put(sn,f'E{i}',state);put(sn,f'F{i}',source)
row=max(int(v.split('D')[-1]) for v in R.values())+4
def der(k,f,label=None,state='Cálculo'):
 global row
 R[k]=f"'{sn}'!D{row}";put(sn,f'C{row}',label or k);put(sn,f'D{row}',f);put(sn,f'E{row}',state);row+=1
for k in ['revenue','ebit','tax','pretax','da','capex','cfo','sbc','lease_add','lease_cash']:
 name='tax_ltm' if k=='tax' else k
 der(name,f'={R[k+"_fy"]}+{R[k+"_9m"]}-{R[k+"_9m_prior"]}')
der('lease',f'={R["lease_current"]}+{R["lease_long"]}')
der('cash_total',f'={R["cash"]}+{R["short_investments"]}')
der('rf',f'={R["treasury"]}-{R["us_default"]}')
der('erp',f'={R["erp_treasury"]}+{R["us_default"]}')
der('shares_total',f'={R["shares"]}+{R["rsu"]}+{R["psu"]}')
der('occupancy',f'={R["occupancy_fy"]}+{R["occupancy_9m"]}-{R["occupancy_9m_prior"]}')
der('fixed_rent_proxy',f'={R["fixed_rent_fy"]}*{R["occupancy"]}/{R["occupancy_fy"]}',state='Proxy: renta fija escala con ocupación')
der('lease_interest_proxy',f'=({R["lease"]}+4980.117)/2*{R["lease_rate"]}',state='Proxy: media Sep25/Sep26, tasa FY25')
der('rou_da_proxy',f'={R["fixed_rent_proxy"]}-{R["lease_interest_proxy"]}',state='Proxy: renta fija menos interés')
der('ebit_adjusted',f'={R["ebit"]}+{R["lease_interest_proxy"]}')
der('capital',f'={R["equity"]}+{R["lease"]}-{R["cash_total"]}-{R["long_investments"]}')
der('capital_fy',f'={R["equity_fy"]}+{R["lease_fy"]}-350.545-698.591-197.123')
der('debt_weight',f'={R["lease"]}/({R["lease"]}+{R["shares_total"]}*{R["price"]})')
der('beta',f'={R["beta_unlevered"]}*(1+(1-{R["tax"]})*{R["lease"]}/({R["shares_total"]}*{R["price"]}))')
der('ke',f'={R["rf"]}+{R["beta"]}*{R["erp"]}')
der('wacc',f'={R["ke"]}*(1-{R["debt_weight"]})+{R["kd"]}*(1-{R["tax"]})*{R["debt_weight"]}')
der('wacc_terminal',f'={R["rf"]}+0.045')
der('auvk',f'={R["revenue"]}/(({R["units"]}+{R["units_prior"]})/2)',state='Proxy media de unidades de dos cierres')
der('d1',f'=(LN({R["price"]}/{R["strike"]})+({R["rf"]}+0.5*{R["vol"]}^2)*{R["maturity"]})/({R["vol"]}*SQRT({R["maturity"]}))')
der('d2',f'={R["d1"]}-{R["vol"]}*SQRT({R["maturity"]})')
der('option_value',f'={R["options"]}*({R["price"]}*NORM.S.DIST({R["d1"]},TRUE)-{R["strike"]}*EXP(-{R["rf"]}*{R["maturity"]})*NORM.S.DIST({R["d2"]},TRUE))',state='Black-Scholes; volatilidad sectorial proxy')
der('roic_average_proxy',f'={R["ebit_adjusted"]}*(1-{R["tax"]})/AVERAGE({R["capital"]},3221.838+4980.117-698.743-722.531-347.694)',state='ROIC LTM sobre media Sep25/Sep26; ajuste interés lease estimado')
der('unit_capital_proxy',f'={R["new_capex_per_unit"]}+{R["new_lease_capital_per_unit"]}')
der('unit_roic_proxy',f'={R["new_unit_sales"]}*Base!D5*(1-{R["tax"]})/{R["unit_capital_proxy"]}',state='Juicio: retorno maduro; no RONIC observado')
der('net_reinvestment_before_nwc',f'={R["capex"]}-{R["da"]}+{R["lease_add"]}-{R["rou_da_proxy"]}',state='Diagnóstico; nuevas leases incluyen renovaciones')
put(sn,f'C{row+1}','S/C 1,5× es juicio: inversión implícita se contrasta en Base, no dato publicado.')
put(sn,f'C{row+2}','Caja restringida excluida; inversiones largas a valor contable como proxy; SBC sigue en EBIT.')
headers[sn]=[4];cols[sn]=['C',38,'D',18,'E',35,'F',110]

def model(sn,case,offset=0,override=None,extra=True):
 s=SCENARIOS[case];put(sn,f'C{2+offset}',f'CMG R4 · {case} · auxiliar JMR')
 def p(a,v):
  import re
  aa=re.sub(r'(\d+)$',lambda m:str(int(m.group(1))+offset),a);put(sn,aa,v)
 def ref(a):
  import re
  return re.sub(r'(\d+)$',lambda m:str(int(m.group(1))+offset),a)
 def f(a,v):
  import re
  # Shift local addresses only; external references supplied later via tokens.
  if offset:v=re.sub(r'(?<![!\w\'])\$?([C-O])\$?(\d+)',lambda m:m.group(0).replace(m.group(2),str(int(m.group(2))+offset)),v)
  p(a,v)
 assumptions=[('Margen económico objetivo',s['margin']),('S/C años1–5',s['sc1']),('S/C años6–10',s['sc2']),('ROIC marginal terminal',s['roic']),('g terminal',s['g']),('Probabilidad JMR',s['weight'])]
 for r,(label,v) in enumerate(assumptions,5):p('C'+str(r),label);p('D'+str(r),v)
 for rr,k in [(12,'wacc'),(13,'wacc_terminal')]:p('C'+str(rr),k);p('D'+str(rr),'='+R[k])
 p('C14','Lag de reinversión');p('D14',1)
 p('C15','Cambio comparables (pp)');p('D15',0)
 labels={16:'Año',18:'Restaurantes propios al cierre',19:'Aperturas NETAS (juicio)',20:'Crecimiento comparable',21:'Ventas por unidad proxy',22:'Restaurantes promedio proxy',23:'Ingresos',24:'Crecimiento ingresos',25:'Margen EBIT económico',26:'EBIT económico',27:'Tasa fiscal',28:'NOPAT',29:'Sales-to-Capital marginal',30:'Reinversión',31:'FCFF',32:'WACC',33:'Factor descuento',34:'Valor presente FCFF',35:'Capital inicial',36:'Capital final',37:'ROIC capital promedio',38:'ROIC capital inicial',39:'RONIC proxy (cohorte previa)'}
 for rr,label in labels.items():p('C'+str(rr),label)
 for j in range(4,16):
  L=c(j);prev=c(j-1);nxt=c(j+1);year=j-4
  p(L+'16',year)
  if year==0:
   for rr,k in [(18,'units'),(21,'auvk'),(23,'revenue'),(26,'ebit_adjusted'),(27,'tax'),(35,'capital')]:p(L+str(rr),'='+R[k])
   p(L+'25',f'={L}26/{L}23');p(L+'28',f'={L}26*(1-{L}27)');continue
  if year<=10:
   p(L+'19',s['openings'][year-1]);p(L+'20',s['comps'][year-1])
   f(L+'18',f'={prev}18+{L}19');f(L+'21',f'={prev}21*(1+{L}20+$D$15)');f(L+'22',f'=AVERAGE({prev}18,{L}18)');f(L+'23',f'={L}21*{L}22')
  else:f(L+'23',f'={prev}23*(1+$D$9)')
  f(L+'24',f'={L}23/{prev}23-1');f(L+'25',f'=$D$25+($D$5-$D$25)*MIN({L}16/5,1)');f(L+'26',f'={L}23*{L}25');p(L+'27','='+R['tax']);f(L+'28',f'={L}26*(1-{L}27)')
  f(L+'29',f'=IF({L}16<=5,$D$6,$D$7)')
  f(L+'30',f'={L}28*$D$9/$D$8' if year==11 else f'=MAX(0,IF($D$14=0,({L}23-{prev}23)/{L}29,({nxt}23-{L}23)/{L}29))')
  f(L+'31',f'={L}28-{L}30');f(L+'32',f'=IF({L}16<=5,$D$12,$D$12+($D$13-$D$12)*MIN(({L}16-5)/5,1))')
  f(L+'33',f'=1/(1+{L}32)' if year==1 else f'={prev}33/(1+{L}32)' if year<=10 else f'={prev}33')
  f(L+'34',f'={L}31*{L}33');f(L+'35',f'={prev}35' if year==1 else f'={prev}36');f(L+'36',f'={L}35+{L}30');f(L+'37',f'={L}28/AVERAGE({L}35,{L}36)');f(L+'38',f'={L}28/{L}35')
  if year>1:f(L+'39',f'=IF({prev}30>0,({L}28-{prev}28)/{prev}30,0)')
 for rr,label in [(43,'EV operativo'),(44,'Valor terminal año10'),(45,'VP valor terminal'),(46,'Caja disponible'),(47,'Inversiones no operativas proxy'),(48,'Deuda leases reconocida (una vez)'),(49,'Valor opciones (una vez)'),(50,'Acciones + RSU/PSU esperadas'),(51,'Patrimonio ordinario'),(52,'Valor por acción provisional'),(53,'MOS35% sobre Base'),(54,'Peso terminal / EV')]:p('C'+str(rr),label)
 f('D44','=O31/($D$13-$D$9)');f('D45','=D44*N33');f('D43','=SUM(E34:N34)+D45')
 for rr,k in [(46,'cash_total'),(47,'long_investments'),(48,'lease'),(49,'option_value'),(50,'shares_total')]:p('D'+str(rr),'='+R[k])
 f('D51','=D43+D46+D47-D48-D49');f('D52','=MAX(0,D51/D50)');f('D53','=D52*0.65');f('D54','=D45/D43')
 if override:
  for a,v in override.items():p(a,v)
 if extra:
  for rr,label in [(60,'EV al fin del año'),(61,'Deuda: política constante D/EV'),(62,'Intereses del período'),(63,'Nueva financiación neta'),(64,'FCFE compatible'),(65,'Ke compatible'),(66,'Factor descuento Ke'),(67,'VP FCFE')]:p('C'+str(rr),label)
  for j in range(14,3,-1):
   L=c(j);nxt=c(j+1);prev=c(j-1);y=j-4
   p(L+'60','=D44' if y==10 else f'=({nxt}31+{nxt}60)/(1+{nxt}32)')
   p(L+'61',f'={R["debt_weight"]}*{L}60')
   if y>0:
    p(L+'62',f'={prev}61*{R["kd"]}');p(L+'63',f'={L}61-{prev}61');p(L+'64',f'={L}31-{L}62*(1-{R["tax"]})+{L}63')
    p(L+'65',f'=({L}32-{R["debt_weight"]}*{R["kd"]}*(1-{R["tax"]}))/(1-{R["debt_weight"]})')
    p(L+'66',f'=1/(1+{L}65)' if y==1 else f'={prev}66/(1+{L}65)');p(L+'67',f'={L}64*{L}66')
  p('C69','FCFE valor por acción (identidad)');p('D69',f'=(SUM(E67:N67)+(1-{R["debt_weight"]})*D44*N66+D46+D47-D49+D61-D48)/D50')
  p('C70','Diferencia FCFE − FCFF');p('D70','=D69-D52')
  p('C72','FCFE usa D/EV constante y ajuste de financiación inicial; equivalencia algebraica, no método independiente.')
  headers[sn]=[16];cols[sn]=['C',38,'D:O',15]
 return f"'{sn}'!D{52+offset}"

for case in SCENARIOS:model(case,case)

# All 5x5 sensitivities use the same formula builder. Native Sheets has no Excel What-if tables.
sn='Sensibilidades';put(sn,'C2','CMG R4 · sensibilidades del auxiliar JMR')
put(sn,'C3','Centros = Base. g máximo4,6% <= Rf4,68%. WACC mueve curva completa.')
families=[('WACC × g',[-.01,-.005,0,.005,.01],[-.01,-.005,0,.003,.006]),('ROIC terminal × g',[-.04,-.02,0,.02,.04],[-.01,-.005,0,.003,.006]),('Comparables × margen',[-.01,-.005,0,.005,.01],[-.02,-.01,0,.01,.02]),('S/C 1–5 × S/C 6–10',[-.3,-.15,0,.15,.3],[-.3,-.15,0,.15,.3])]
idx=0
for fi,(name,xs,ys) in enumerate(families):
 top=5+fi*10;put(sn,f'C{top}',name)
 for j,y in enumerate(ys,5):put(sn,f'{c(j)}{top+1}',y+(.04 if fi<2 else .185 if fi==2 else 1.4))
 for i,x in enumerate(xs,top+2):
  put(sn,f'D{i}',x+(derive()['wacc'] if fi==0 else .14 if fi==1 else 0 if fi==2 else 1.5))
  for j,y in enumerate(ys,5):
   off=idx*78;over={}
   if fi==0:over={'D12':f'={R["wacc"]}+{x}','D13':f'={R["wacc_terminal"]}+{x}','D9':.04+y}
   if fi==1:over={'D8':.14+x,'D9':.04+y}
   if fi==2:over={'D15':x,'D5':.185+y}
   if fi==3:over={'D6':1.5+x,'D7':1.4+y}
   output=model('Motor JMR','Base',off,over,extra=False);put(sn,f'{c(j)}{i}','='+output);idx+=1
 put(sn,f'C{top+8}','Centro − Base');put(sn,f'D{top+8}',f'=G{top+4}-Base!D52')
headers[sn]=[6,16,26,36];cols[sn]=['C',38,'D:I',16]

sn='Resumen';put(sn,'C2','Chipotle · nueva revisión A-1.2 R4')
put(sn,'C3','CANDIDATO. Recast y valor auxiliar provisionales; no publicable por discrepancias de plantilla.')
for j,v in enumerate(['Historia','Valor / acción','MOS35%','Probabilidad JMR'],3):put(sn,f'{c(j)}5',v)
for i,case in enumerate(SCENARIOS,6):
 put(sn,f'C{i}',case);put(sn,f'D{i}',f"='{case}'!D52");put(sn,f'E{i}',f"='{case}'!D53" if case=='Base' else 'No aplica');put(sn,f'F{i}',f"='{case}'!D10")
put(sn,'C11','Promedio C/B/O condicionado');put(sn,'D11','=(D6*F6+D7*F7+D8*F8)/(F6+F7+F8)')
put(sn,'C13','Referencia de mercado 04-nov-2026');put(sn,'D13','='+R['price'])
put(sn,'C14','Potencial (valor − precio) / precio');put(sn,'D14','=D6/D13-1')
put(sn,'C16','Base anterior publicado');put(sn,'D16',25.246494601933065)
put(sn,'C17','Cambio vs anterior');put(sn,'D17','=D6/D16-1')
put(sn,'C19','Principal reserva económica');put(sn,'D19','S/C marginal y persistencia del ROIC14% son juicios, no observaciones por cohorte.')
put(sn,'C21','Principal bloqueo técnico');put(sn,'D21','Plantilla IA difiere del original; no sobrescribir fórmulas ni certificar integridad original.')
put(sn,'C23','Equivalencia contable FCFE / FCFF');put(sn,'D23','=Base!D70')
headers[sn]=[5];cols[sn]=['C',40,'D',24,'E:F',20]

# Multiples are secondary scenarios, anchored to fundamentals and dated industry comparators.
sn='Multiplos';put(sn,'C2','CMG R4 · múltiplos secundarios y anclas FY+1/+2/+3')
put(sn,'C3','Juicios de salida limitados por fundamentales. Sin equiparar percentiles sectoriales con CMG.')
methods=[('EV/EBITDA',17.49,'enterprise'),('EV/FCFF',22.,'enterprise'),('P/E',23.,'equity'),('P/FCFE',24.,'equity'),('P/OCF',18.,'equity')]
for j,v in enumerate(['Método','Múltiplo elegido','Fundamental +1','Fundamental +2','Fundamental +3','VP +1','VP +2','VP +3'],3):put(sn,f'{c(j)}5',v)
for i,(name,m,typ) in enumerate(methods,6):
 put(sn,f'C{i}',name);put(sn,f'D{i}',m)
 for j,y in enumerate([1,2,3],5):
  L=c(y+4)
  if name=='EV/EBITDA':f=f'=Base!{L}26+Base!{L}23*({R["da"]}+{R["rou_da_proxy"]})/{R["revenue"]}'
  elif name=='EV/FCFF':f=f'=Base!{L}31'
  elif name=='P/E':f=f'=Base!{L}28-Base!{L}62*(1-{R["tax"]})'
  elif name=='P/FCFE':f=f'=Base!{L}64'
  else:f=f'=Base!{L}28-Base!{L}62*(1-{R["tax"]})+Base!{L}23*({R["da"]}+{R["rou_da_proxy"]})/{R["revenue"]}+.045*(Base!{L}23-'+(R["revenue"] if y==1 else f'Base!{c(y+3)}23')+')'
  put(sn,f'{c(j)}{i}',f)
  bridge=f'+Base!D46+Base!D47-Base!D48-Base!D49' if typ=='enterprise' else '-Base!D49'
  discount=f'Base!{L}33' if typ=='enterprise' else f'Base!{L}66'
  put(sn,f'{c(j+3)}{i}',f'=({c(j)}{i}*$D{i}{bridge})/Base!D50*{discount}')
 put(sn,f'L{i}','Sector17,49× EBITDA positivo enero2026; demás anclas son juicios JMR pendientes de cierre normativo.' if name=='EV/EBITDA' else 'JUICIO; aún requiere ancla histórica homogénea y límite fundamental JMR antes de promoción.')
for n,(name,m,typ) in enumerate(methods):
 top=15+n*10;put(sn,f'C{top}',name+' · múltiplo × fundamental FY+3')
 for j,k in enumerate([.8,.9,1,1.1,1.2],5):put(sn,f'{c(j)}{top+1}',f'=$G${6+n}*{k}')
 for i,k in enumerate([.8,.9,1,1.1,1.2],top+2):
  put(sn,f'D{i}',f'=$D${6+n}*{k}')
  for j in range(5,10):
   bridge='+Base!D46+Base!D47-Base!D48-Base!D49' if typ=='enterprise' else '-Base!D49';discount='Base!G33' if typ=='enterprise' else 'Base!G66'
   put(sn,f'{c(j)}{i}',f'=(${"D"}{i}*{c(j)}${top+1}{bridge})/Base!D50*{discount}')
 put(sn,f'C{top+8}','Centro − VP3 propio');put(sn,f'D{top+8}',f'=G{top+4}-J{6+n}')
headers[sn]=[5,16,26,36,46,56];cols[sn]=['C',38,'D:K',18,'L',90]

put('Motor JMR','A1','Auxiliar generado: mismas fórmulas JMR para todas las combinaciones; no es hoja Damodaran.')
spec={'Resumen':spec.pop('Resumen'),**spec}
(P/'workbook_spec.json').write_text(json.dumps({'sheets':spec,'headers':headers,'columns':cols,'raw_refs':R},ensure_ascii=False))
print(len(spec),'sheets',sum(len(x) for x in spec.values()),'cells')
