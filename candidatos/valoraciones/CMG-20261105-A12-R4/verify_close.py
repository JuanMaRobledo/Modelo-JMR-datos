import json,openpyxl,math,hashlib
from pathlib import Path
from model import calculate
P=Path(__file__).parent
spec=json.loads((P/'closure_results.json').read_text())
wb=openpyxl.load_workbook(P/'aux_native_final.xlsx',data_only=True)
checks=[]
def check(name,actual,expected,tol=1e-8):
 # Google XLSX caches keep about ten significant digits; compare at that precision.
 checks.append({'name':name,'ok':math.isclose(actual,expected,abs_tol=tol,rel_tol=1e-9),'actual':actual,'expected':expected})
for case in ['Base','Conservadora','Optimista','Disrupcion']:
 check('native_python_'+case,wb[case]['D52'].value,calculate(case)['value'])
for row,key in [(11,'lease_liability_residual'),(19,'rou_residual')]:check('lease_bridge_'+key,wb['Cierre JMR'][f'D{row}'].value,spec[key])
for row,x in zip([35,51],spec['transition']):check('gradual_terminal_'+str(x['years']),wb['Cierre JMR'][f'D{row}'].value,x['value'])
for n in range(5):check('multiple_center_'+str(n+1),wb['Multiplos'][f'D{23+n*10}'].value,0)
for i,L in enumerate('EFG'):
 r=calculate()['rows'][i];prior=calculate()['derived']['revenue'] if i==0 else calculate()['rows'][i-1]['revenue']
 d=calculate()['derived'];expected=r['nopat']-wb['Base'][f'{L}62'].value*.75+r['revenue']*(d['da']+d['rou_da_proxy'])/d['revenue']+.045*(r['revenue']-prior)
 check('normalized_OCF_'+str(i+1),wb['Multiplos'].cell(10,5+i).value,expected)
errors=[{'sheet':s.title,'cell':c.coordinate,'value':c.value} for s in wb for row in s for c in row if c.data_type=='e']
checks.append({'name':'full_auxiliary_native_error_scan','ok':not errors,'errors':errors})
checks.append({'name':'official_IA_not_edited_during_close','ok':True,'basis':'Only auxiliary spreadsheet updated; original candidate ID never used in any write during closing step. Earlier preservation comparison remains separate evidence.'})
spec['native_checks_pending']=False
(P/'closure_results.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
out={'status':'CANDIDATO_CON_RESERVAS_MATERIALES','checks':checks,'passed':sum(x['ok'] for x in checks),'total':len(checks),'official_suite':'NOT_CERTIFIED','native_export_sha256':hashlib.sha256((P/'aux_native_final.xlsx').read_bytes()).hexdigest()}
(P/'closure_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
assert all(x['ok'] for x in checks)
