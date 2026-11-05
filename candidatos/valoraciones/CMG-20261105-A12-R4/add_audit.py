import json
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'workbook_spec.json').read_text());R=s['raw_refs'];cells={}
def p(a,v):cells[a]=v
p('C2','CMG R4 · reinversión, ROIC y duración de ventaja')
p('C3','Diagnósticos JMR separados del libro original. Proxies identificados; no auditoría F5.')
labels={5:'CAPEX LTM',6:'D&A LTM',7:'Adiciones ROU LTM',8:'Depreciación ROU proxy LTM',9:'Reinversión antes de NWC',10:'Crecimiento ventas observado LTM',11:'NWC normalizado / ventas (juicio)',12:'Reinversión normalizada indicativa',13:'Aumento ventas financiado año2',14:'S/C indicativo con lag1',15:'S/C elegido Base1–5',16:'Reinversión año1 elegida',17:'Diferencia inversión elegida vs LTM proxy',19:'CAPEX por apertura proxy',20:'PV lease por apertura proxy',21:'Capital por apertura proxy',22:'Ventas maduras por restaurante',23:'ROIC unitario a margen Base',24:'ROIC marginal perpetuo elegido',25:'ROIC si capital/local =3,50M',26:'ROIC si capital/local =4,00M',28:'Reinversión año10',29:'Reinversión estable año11',30:'Cambio reinversión terminal',31:'FCFF año10',32:'FCFF año11',33:'Cambio FCFF terminal',35:'ROIC año10 sobre capital inicial',36:'ROIC año10 sobre capital promedio'}
for row,label in labels.items():p('C'+str(row),label)
forms={5:'='+R['capex'],6:'='+R['da'],7:'='+R['lease_add'],8:'='+R['rou_da_proxy'],9:'=D5-D6+D7-D8',10:'='+R['revenue']+'-G8',12:'=D9+D10*D11',13:'=Base!F23-Base!E23',14:'=D13/D12',15:'=Base!D6',16:'=Base!E30',17:'=D16/D12-1',19:'='+R['new_capex_per_unit'],20:'='+R['new_lease_capital_per_unit'],21:'=D19+D20',22:'='+R['new_unit_sales'],23:'=D22*Base!D5*(1-'+R['tax']+')/D21',24:'=Base!D8',25:'=D22*Base!D5*(1-'+R['tax']+')/3.5',26:'=D22*Base!D5*(1-'+R['tax']+')/4',28:'=Base!N30',29:'=Base!O30',30:'=D29/D28-1',31:'=Base!N31',32:'=Base!O31',33:'=D32/D31-1',35:'=Base!N38',36:'=Base!N37'}
p('D11',-.045)
for row,f in forms.items():p('D'+str(row),f)
p('F5','Ventas FY2024');p('G5',11313.853);p('F6','Ventas9M2025');p('G6',8942.090);p('F7','Ventas9M2024');p('G7',8468.543);p('F8','Ventas LTM Sep25');p('G8','=G5+G6-G7');p('H5','SEC Q3 2025 y FY2024; USD M')
p('F9','ROU incluyen aperturas, renovaciones y revisiones. No son solo inversión en restaurantes nuevos.')
p('F14','Compara inversión LTM proxy con ventas año2: calibración hacia1,5×, no RONIC observado.')
p('F20','PV1,40M es juicio. Pasivo medio por local actual ≈1,31M; no costo marginal certificado.')
p('F24','14% implica retornos superiores al WACC estable. La alternativa de erosión finita es material.')
for n,(start,years) in enumerate([(.14,5),(.14,10),(.20,5),(.20,10)]):
 top=41+n*16;p(f'C{top}',f'ROIC inicial {start:.0%} → WACC en {years} años')
 p(f'C{top+1}','ROIC inicial');p(f'D{top+1}',start);p(f'C{top+2}','Años de erosión');p(f'D{top+2}',years)
 for j in range(5,15):
  L=chr(64+j);prev=chr(63+j);t=j-4
  p(f'{L}{top+3}',t)
  p(f'{L}{top+4}',f'=Base!N28*(1+Base!D9)^{L}{top+3}')
  p(f'{L}{top+5}',f'=$D${top+1}+(Base!D13-$D${top+1})*MIN({L}{top+3}/$D${top+2},1)')
  p(f'{L}{top+6}',f'={L}{top+4}*Base!D9/{L}{top+5}')
  p(f'{L}{top+7}',f'=({L}{top+4}-{L}{top+6})/(1+Base!D13)^{L}{top+3}')
  p(f'{L}{top+8}',f'=IF({L}{top+3}<=$D${top+2},{L}{top+7},0)')
 p(f'C{top+4}','NOPAT');p(f'C{top+5}','ROIC marginal');p(f'C{top+6}','Reinversión');p(f'C{top+7}','VP FCFF después año10');p(f'C{top+8}','VP dentro del fade')
 p(f'C{top+10}','Nuevo terminal al año10');p(f'D{top+10}',f'=SUM(E{top+8}:N{top+8})+Base!N28*(1+Base!D9)^($D${top+2}+1)*(1-Base!D9/Base!D13)/(Base!D13-Base!D9)/(1+Base!D13)^$D${top+2}')
 p(f'C{top+11}','Valor por acción con fade');p(f'D{top+11}',f'=(Base!D43-Base!D45+D{top+10}*Base!N33+Base!D46+Base!D47-Base!D48-Base!D49)/Base!D50')
 p(f'C{top+12}','Cambio frente a Base');p(f'D{top+12}',f'=D{top+11}/Base!D52-1')
s['sheets']['Auditoria JMR']=cells;s['headers']['Auditoria JMR']=[44,60,76,92];s['columns']['Auditoria JMR']=['C',42,'D',18,'E:N',15,'F',28]
(P/'workbook_spec.json').write_text(json.dumps(s,ensure_ascii=False));print(len(cells))
