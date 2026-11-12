"""Verifica evidencia capturada del motor nativo; no calcula un DCF alternativo."""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
E = ROOT / 'CIERRE_ECONOMICO_EVIDENCIA'
def read(name): return json.loads((E / name).read_text())
def cell(result, title, row, col):
    for sheet in result['structuredContent']['sheets']:
        if sheet['properties']['title'] != title: continue
        for block in sheet.get('data', []):
            i=row-1-block.get('startRow',0); j=col-1-block.get('startColumn',0)
            if i<0 or j<0:continue
            rows=block.get('rowData',[])
            if i<len(rows) and j<len(rows[i].get('values',[])):
                c=rows[i]['values'][j]
                if c.get('effectiveValue',{}).get('errorValue'): raise AssertionError(c)
                return c
    raise KeyError((title,row,col))
def num(*args): return cell(*args)['effectiveValue']['numberValue']

tests=read('fiscal_final_tests.json')
assert len(tests)==3
for t in tests:
    assert t['maxError']==0 and len(t['actual'])==3
    assert t['historicalETR']==-0.06402164111812443
    assert t['actual']==t['expected']

m=read('m-ebitda-after.json')
for c in range(2,13):
    assert num(m,'M · Income Statement',27,c)==num(m,'Income Statement',28,c)
assert num(m,'M · Income Statement',27,12)==-250

official=read('official_after_fiscal.json')
for name in ['Input sheet','Input sheet · C','Input sheet · O']:
    assert num(official,name,23,2)==.25
assert num(official,'Income Statement',29,12)==tests[0]['historicalETR']
assert num(official,'Valuation output',33,2)==-7.461576807613708

runs=read('official_tax_75.json'); assert len(runs)==25
for r in runs:
    for family in ['A','B','C']: assert math.isfinite(r[family]['value'])
for f in ['A','B','C']:assert runs[12][f]['value']==num(official,'Valuation output',33,2)
static=read('matrix-static-proof.json'); count=0
for s in static['structuredContent']['sheets']:
    for b in s['data']:
        for r in b['rowData']:
            for c in r['values']:
                assert 'formulaValue' not in c['userEnteredValue']
                assert isinstance(c['userEnteredValue']['numberValue'],(int,float));count+=1
assert count==75

roots=read('inverse_raw_fixed.json')['result']
roots += [read('inverse_raw_three.json')['result'][1]]
assert len(roots)==4
for r in roots: assert r['bracketed'] and abs(r['difference'])<.000004

integrity=read('integridad-mantenimiento.json')
assert not integrity['Damodaran_calculation_formula_changes']
assert not integrity['comments_formats_validation_changes']
assert integrity['cells_examined']==148302

stress=read('economic_stress_runs.json');joint=read('joint_cases.json')
assert len(stress)==14 and len(joint)==3
assert joint[0]['common'][0]>0 and joint[1]['common'][0]>2.9
assert all(s['commonConditional'][0]==0 for s in stress)
sc=read('sc_only.json')
assert abs(num(sc,'Valuation output',24,2)-2367.260085555595)<1e-9
assert abs(num(sc,'Valuation output',9,3)-109.212)<1e-9

v=json.loads((ROOT/'valoracion.json').read_text())
a=json.loads((ROOT/'analisis.json').read_text())
assert v['revisionId']==a['revisionId']=='XRX-FLOYD-20261112-R1'
assert v['estado']=='CANDIDATO' and v['valorPrincipal'] is None and v['precioMOS'] is None
assert a['html']==a['articleHtml']+a['calculationHtml']
assert a['articleHtml'].count('<h3>')==14 and a['calculationHtml'].count('<h3>')==12
print(json.dumps({'regresionesFiscales':9,'EBITDAConciliados':11,'corridasMatrices':75,'centrosDiferencia':0,'inversosValidos':4,'stressAislados':14,'stressConjuntos':3,'celdasMotorInspeccionadas':148302,'formulasCalculoDamodaranModificadas':0,'estado':'CANDIDATO','r6':'PENDIENTE INDEPENDIENTE'},ensure_ascii=False))
