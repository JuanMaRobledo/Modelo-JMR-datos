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
# Evidencia vigente después de la autorización explícita. Lo anterior queda
# como regresión del mantenimiento fiscal, no como valoración vigente.
AUTH=ROOT/'AUTORIZACION_EVIDENCIA'
def auth(n):return json.loads((AUTH/('xrx-autorizacion-'+n+'.json')).read_text())
new=auth('salidas')
core={'structuredContent':{'sheets':sum([auth('integridad-'+str(i))['structuredContent']['sheets']for i in range(9)],[])}}
for title,sc in [('Input sheet',(8,4)),('Input sheet · C',(12,8)),('Input sheet · O',(2.1,2.1))]:
    assert tuple(cell(core,title,r,2)['userEnteredValue']['numberValue']for r in [31,32])==sc
assert num(new,'Valuation output',33,2)==-10.935767379800657
assert abs(num(new,'Valuation output',9,3)-109.212)<1e-9
nr=auth('75-corridas');assert len(nr)==25
proof=auth('antes-sellos')['proof'];count=0
for n in nr:
    for family,start in [('A',6),('B',14),('C',37)]:
        r,c=start+n['i'],2+n['j']
        actual=cell(proof,'Sensibilidades DCF',r,c)
        assert 'formulaValue' not in actual['userEnteredValue']
        assert abs(actual['effectiveValue']['numberValue']-n[family]['value'])<1e-10
        count+=1
assert count==75
for f in ['A','B','C']:assert nr[12][f]['value']==num(new,'Valuation output',33,2)
roots=auth('inversos-tres')['results']+[auth('inverso-wacc')]
for r in roots:assert abs(r['difference'])<5e-9
for i,r in enumerate(roots):assert num(proof,'Sensibilidades DCF',22+i,2)==r['root']
gates=auth('sellos-y-gates')['gates']
for row in [2,3]:assert cell(gates,'Control de revisión',row,2)['effectiveValue']['stringValue']=='VIGENTE'
assert cell(gates,'Resumen de valoraciones',17,2)['effectiveValue']['stringValue'].startswith('N/M')
integrity=auth('integridad-resumen')
assert integrity['celdasInspeccionadas']==148302
assert integrity['fiscalB23']==3 and integrity['inputsSC']==6
assert not integrity['cambiosNoAutorizados'] and not integrity['comentariosFormatoValidacionesCambiados']
assert integrity['formulasCalculoDamodaranModificadas']==0
assert v['salidasBrutasGinsuDiagnostico']['base']==num(new,'Valuation output',33,2)
print(json.dumps({'regresionesFiscalesAntecedentes':9,'EBITDAConciliados':11,'corridasMatricesVigentes':75,'centrosDiferencia':0,'inversosVigentes':4,'inputsSC':6,'MOS':'N/M','sellos':'VIGENTE','stressAisladosAntecedentes':14,'stressConjuntosAntecedentes':3,'celdasMotorInspeccionadas':148302,'formulasCalculoDamodaranModificadas':0,'estado':'CANDIDATO','r6':'PENDIENTE INDEPENDIENTE'},ensure_ascii=False))
