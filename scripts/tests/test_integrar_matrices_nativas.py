import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('integration',Path(__file__).parents[1]/'integrar_matrices_nativas.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def fixture():
    v={'ticker':'TEST','revisionId':'TEST-R1','sheet_id':'S','estado':'EN_REVISION','metodo_valoracion':'A','version_metodo':'A-1.2','valorPrincipal':123.4}
    data={key:[] for key in mod.REQUIRED};data['sens_mult']=[['']*9 for _ in range(230)]
    mats=[];rows=[{'values':[{} for _ in range(9)]} for _ in range(69)]
    for i,name in enumerate(mod.METHODS):
        start=76+10*i
        def put(r,c,val,formula=False):
            data['sens_mult'][r-1][c-1]=val
            rows[r-76]['values'][c-1]={'effectiveValue':{('stringValue' if isinstance(val,str) else 'numberValue'):val},'userEnteredValue':({'formulaValue':'=1+9'} if formula else {'stringValue':str(val)})}
        put(start,1,'BASE · '+name+' · ancla JMR')
        for j in range(5):put(start+2,j+2,j+1);put(start+3+j,1,j+1)
        for r in range(start+3,start+8):
            for c in range(2,7):put(r,c,10,True)
        for c,val in [(7,10),(8,10),(9,'OK')]:put(start+8,c,val)
        mats.append({'metodo':name,'origen':f"'Sensibilidad por múltiplo'!A{start}:I{start+8}",'estado':'OK','escenario':'base','ancla':'JMR','fundamentalFY3':[1,2,3,4,5],'multiploElegido':[1,2,3,4,5],'matriz':[[10]*5 for _ in range(5)],'centro':10,'vp3Original':10})
    digest=hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True,default=str).encode()).hexdigest()
    photo={'revision_id':'TEST-R1','sheet_id':'S','data':data,'data_sha256':digest}
    cand=copy.deepcopy(v);cand['sensibilidadMultiples']={'contrato':'base-native-five-priority-v1','estadoPublicacion':'CANDIDATO_NO_PUBLICADO','revisionId':'TEST-R1','sourceSheetId':'S','resultadosSha256':digest,'matrices':mats}
    cells={'spreadsheetId':'S','sheets':[{'properties':{'title':'Sensibilidad por múltiplo'},'data':[{'startRow':75,'rowData':rows}]}]}
    return v,cand,photo,cells

class IntegrationTests(unittest.TestCase):
    def test_valid_keeps_value_and_inputs(self):
        args=fixture();before=copy.deepcopy(args);r=mod.integrate(*args)
        self.assertEqual(args,before);self.assertEqual(r['valorPrincipal'],123.4)
        self.assertEqual(r['estado'],'EN_REVISION');self.assertFalse(r['sensibilidadMultiples']['certificado'])
        self.assertEqual(r['sensibilidadMultiples']['estadoPublicacion'],'INTEGRADO_EN_REVISION')
    def test_financial_change_rejected(self):
        a=list(fixture());a[1]['valorPrincipal']=999
        with self.assertRaisesRegex(ValueError,'campos ajenos'):mod.integrate(*a)
    def test_hash_and_partial_snapshot_rejected(self):
        for change in [lambda a:a[2]['data']['fm'].append([999]),lambda a:a[2]['data'].pop('input')]:
            a=list(fixture());change(a)
            with self.assertRaises(ValueError):mod.integrate(*a)
    def test_false_source_and_axes_rejected(self):
        for change in [lambda m:m.update(origen='otro'),lambda m:m['fundamentalFY3'].__setitem__(0,99),lambda m:m['matriz'][0].__setitem__(0,99)]:
            a=list(fixture());change(a[1]['sensibilidadMultiples']['matrices'][0])
            with self.assertRaises(ValueError):mod.integrate(*a)
    def test_hardcoded_and_stale_values_rejected(self):
        for change in [lambda c:c['userEnteredValue'].pop('formulaValue'),lambda c:c['effectiveValue'].update(numberValue=11)]:
            a=list(fixture());change(a[3]['sheets'][0]['data'][0]['rowData'][3]['values'][1])
            with self.assertRaises(ValueError):mod.integrate(*a)
    def test_existing_or_bank_rejected(self):
        for change in [lambda v:v.update(ticker='NU'),lambda v:v.update(sensibilidadMultiples={'matrices':[{}]}),lambda v:v.update(estado='APROBADA')]:
            a=list(fixture());change(a[0])
            with self.assertRaises(ValueError):mod.integrate(*a)
    def test_negative_flow_na_requires_evidence(self):
        val={'descuentoMultiples':{'metodos':[{'nombre':'EV/FCFF','peso':0,
            'estado':'N/A: flujo negativo','base':{'fy':[-1,-2,-3],'vp':[-1,-2,-2.5]}}]}}
        self.assertTrue(mod.negative_flow_na(val,'EV/FCFF'))
        self.assertFalse(mod.negative_flow_na(val,'P/E'))
        for change in [lambda x:x.update(peso=.1),lambda x:x.update(estado='PENDIENTE'),
                       lambda x:x['base']['fy'].__setitem__(2,3),
                       lambda x:x['base']['vp'].__setitem__(2,3),
                       lambda x:x['base'].pop('fy')]:
            a=copy.deepcopy(val)
            change(a['descuentoMultiples']['metodos'][0])
            self.assertFalse(mod.negative_flow_na(a,'EV/FCFF'))

    def test_integrate_documented_na_keeps_sheet_nd(self):
        official,candidate,photo,cells=fixture()
        choice={'nombre':'EV/FCFF','peso':0,'estado':'N/A: flujo negativo',
                'base':{'fy':[-2,-3,-4],'vp':[-1.5,-2.3,-3]}}
        official['descuentoMultiples']={'metodos':[choice]}
        candidate['descuentoMultiples']=copy.deepcopy(official['descuentoMultiples'])
        m=candidate['sensibilidadMultiples']['matrices'][1]
        m.update(estado='N/D',matriz=None,centro=None,vp3Original=-3)
        start=86
        rows=cells['sheets'][0]['data'][0]['rowData']
        def set_cell(row,col,val):
            photo['data']['sens_mult'][row-1][col-1]=val
            cell=rows[row-76]['values'][col-1]
            cell['effectiveValue']={('stringValue' if isinstance(val,str) else 'numberValue'):val}
        for row in range(start+3,start+8):
            for col in range(2,7):set_cell(row,col,'N/D')
        set_cell(start+8,7,-3)
        set_cell(start+8,8,-3)
        set_cell(start+8,9,'N/D')
        digest=hashlib.sha256(json.dumps(photo['data'],ensure_ascii=False,sort_keys=True,default=str).encode()).hexdigest()
        photo['data_sha256']=digest
        candidate['sensibilidadMultiples']['resultadosSha256']=digest
        out=mod.integrate(official,candidate,photo,cells)
        rel=out['sensibilidadMultiples']['matrices'][1]
        self.assertEqual(rel['estado'],'N/A')
        self.assertEqual(rel['estadoFuente'],'N/D')
        self.assertIsNone(rel['matriz'])
        self.assertEqual(out['valorPrincipal'],official['valorPrincipal'])
        self.assertEqual(candidate['sensibilidadMultiples']['matrices'][1]['estado'],'N/D')
        invalid=copy.deepcopy(official)
        invalid['descuentoMultiples']['metodos'][0]['base']['fy'][2]=2
        invalid_candidate=copy.deepcopy(candidate)
        invalid_candidate['descuentoMultiples']=copy.deepcopy(invalid['descuentoMultiples'])
        with self.assertRaisesRegex(ValueError,'justificación'):
            mod.integrate(invalid,invalid_candidate,photo,cells)

    def test_missing_method_rejected(self):
        a=list(fixture());a[1]['sensibilidadMultiples']['matrices'].pop()
        with self.assertRaises(ValueError):mod.integrate(*a)

if __name__=='__main__':unittest.main()
