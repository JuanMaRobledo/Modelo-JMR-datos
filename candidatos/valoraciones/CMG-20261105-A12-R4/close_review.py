"""Final JMR-only diagnostics; never writes original Damodaran cells."""
import json, copy
from pathlib import Path
from model import RAW, calculate, derive
P=Path(__file__).parent
d=derive(); b=calculate(); cells={}
def put(a,v): cells[a]=v
put('C2','CMG R4 · cierre y reservas cuantificadas')
put('C3','Diagnósticos auxiliares. No reemplazan el núcleo IA ni certifican publicación.')
values={5:('Pasivo lease inicial Sep25',4980.117),6:('Altas ROU LTM: proxy de nuevas obligaciones',d['lease_add']),7:('Interés estimado LTM',d['lease_interest_proxy']),8:('Pagos lease LTM',d['lease_cash']),10:('Pasivo observado Sep26',d['lease']),13:('ROU inicial Sep25',4385.099),14:('Altas ROU LTM',d['lease_add']),15:('Bajas ROU LTM',6.127+4.609-1.542),16:('Amortización ROU estimada',d['rou_da_proxy']),18:('ROU observado Sep26',RAW['rou'])}
for r,(label,value) in values.items():put(f'C{r}',label);put(f'D{r}',value)
for r,label,f in [(9,'Pasivo reconstruido antes de residual','=D5+D6+D7-D8'),(11,'Residual pasivo: sin clasificación probada','=D10-D9'),(12,'Residual / pasivo final','=D11/D10'),(17,'ROU reconstruido antes de residual','=D13+D14-D15-D16'),(19,'Residual ROU: sin clasificación probada','=D18-D17'),(20,'Residual / ROU final','=D19/D18')]:put(f'C{r}',label);put(f'D{r}',f)
put('F6','Altas ROU no equivalen necesariamente a altas de pasivo: pagos anticipados/incentivos y revisiones pueden diferir.')
put('F11','No se imputa el residual a FX, modificaciones o interés para forzar cierre; falta desglose primario.')
put('F19','Renta fija y amortización son proxies. Un residual pequeño no demuestra precisión de sus componentes.')
put('C23','ROIC marginal implícito en transición año10→11');put('D23','=Base!N28*Base!D9/Base!N30')
transition=[]
start=b['rows'][9]['nopat']*.04/b['rows'][9]['reinvestment']
for top,years in [(26,5),(42,10)]:
 put(f'C{top}',f'Convergencia gradual de retorno marginal hacia14% en {years} años')
 put(f'C{top+1}','Duración');put(f'D{top+1}',years)
 for j in range(5,15):
  L=chr(64+j);n=j-4
  put(f'{L}{top+2}',n)
  put(f'{L}{top+3}',f'=Base!N28*(1+Base!D9)^{L}{top+2}')
  # n=1 uses the explicit year10 implied marginal return; n=years reaches 14%.
  put(f'{L}{top+4}',f'=$D$23+(Base!D8-$D$23)*MIN(({L}{top+2}-1)/($D${top+1}-1),1)')
  put(f'{L}{top+5}',f'={L}{top+3}*Base!D9/{L}{top+4}')
  put(f'{L}{top+6}',f'=IF({L}{top+2}<=$D${top+1},({L}{top+3}-{L}{top+5})/(1+Base!D13)^{L}{top+2},0)')
 for rr,label in [(3,'NOPAT'),(4,'ROIC marginal'),(5,'Reinversión'),(6,'VP FCFF dentro transición')]:put(f'C{top+rr}',label)
 put(f'C{top+8}','Terminal al año10 con transición')
 put(f'D{top+8}',f'=SUM(E{top+6}:N{top+6})+Base!N28*(1+Base!D9)^($D${top+1}+1)*(1-Base!D9/Base!D8)/(Base!D13-Base!D9)/(1+Base!D13)^$D${top+1}')
 put(f'C{top+9}','Valor por acción');put(f'D{top+9}',f'=(Base!D43-Base!D45+D{top+8}*Base!N33+Base!D46+Base!D47-Base!D48-Base!D49)/Base!D50')
 nt=b['rows'][9]['nopat'];tv=0;flows=[]
 for n in range(1,years+1):
  nt*=1.04;roic=start+(.14-start)*(n-1)/(years-1);reinv=nt*.04/roic
  tv+=(nt-reinv)/(1+d['wacc_terminal'])**n
  flows.append({'year':10+n,'nopat':nt,'roic':roic,'reinvestment':reinv,'fcff':nt-reinv})
 tv+=nt*1.04*(1-.04/.14)/(d['wacc_terminal']-.04)/(1+d['wacc_terminal'])**years
 value=(b['enterprise']-b['pv_terminal']+tv*b['rows'][9]['discount']+d['cash_total']+RAW['long_investments']-d['lease']-d['option_value'])/d['shares_total']
 transition.append({'years':years,'start_roic':start,'value':value,'rows':flows})
put('C59','Interpretación');put('D59','La transición evita el salto inmediato de reinversión; mantener14% después sigue siendo una hipótesis de ventaja persistente.')
put('C61','OCF económico normalizado');put('D61','NI económico + depreciación física + ROU − ΔNWC; NWC/ventas = −4,5%. SBC permanece como costo, sin añadir de nuevo.')
put('C62','Límite');put('D62','No equivale a CFO GAAP: excluye movimientos fiscales transitorios y usa depreciación ROU estimada. Múltiplos sin anclas finales.')
res={'lease_liability_residual':d['lease']-(4980.117+d['lease_add']+d['lease_interest_proxy']-d['lease_cash']), 'rou_residual':RAW['rou']-(4385.099+d['lease_add']-(6.127+4.609-1.542)-d['rou_da_proxy']), 'transition':transition, 'native_checks_pending':True}
(P/'closure_spec.json').write_text(json.dumps(cells,ensure_ascii=False,indent=2))
(P/'closure_results.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
if (P/'workbook_spec.json').exists():
 spec=json.loads((P/'workbook_spec.json').read_text())
 spec['sheets']['Cierre JMR']=cells
 spec['headers']['Cierre JMR']=[26,42]
 spec['columns']['Cierre JMR']=['C',48,'D',25,'E:N',15]
 (P/'workbook_spec.json').write_text(json.dumps(spec,ensure_ascii=False))
print(json.dumps({'liability_residual':res['lease_liability_residual'],'rou_residual':res['rou_residual'],'transition_values':[{k:x[k] for k in ['years','start_roic','value']} for x in transition]},indent=2))
