import copy, hashlib, importlib.util, json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[2]
REV="MELI-20261028-A3"
D=ROOT/"evidencia/captura-completa-candidata-20261031"/REV
spec=importlib.util.spec_from_file_location("native",ROOT/"scripts/integrar_matrices_nativas.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
METHODS=('EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV')
def read(p):return json.loads(Path(p).read_text())
def candidate(before,snapshot):
 r=copy.deepcopy(before);rows=snapshot['data']['sens_mult']
 def get(row,col):
  x=rows[row-1]
  return x[col-1] if col<=len(x) else ''
 mat=[]
 for i,name in enumerate(METHODS):
  start=76+i*10;state=get(start+8,9)
  mat.append({'metodo':name,'escenario':'base','ancla':'JMR','estado':state,
    'origen':f"'Sensibilidad por múltiplo'!A{start}:I{start+8}",
    'fundamentalFY3':[get(start+2,c) for c in range(2,7)],
    'multiploElegido':[get(rr,1) for rr in range(start+3,start+8)],
    'matriz':[[get(rr,c) for c in range(2,7)] for rr in range(start+3,start+8)] if state=='OK' else None,
    'centro':get(start+5,4) if state=='OK' else None,'vp3Original':get(start+8,7)})
 r['sensibilidadMultiples']={**(before.get('sensibilidadMultiples') or {}),
    'contrato':'base-native-five-priority-v1','revisionId':before['revisionId'],
    'sourceSheetId':before['sheet_id'],'resultadosSha256':snapshot['data_sha256'],
    'estadoPublicacion':'CANDIDATO_NO_PUBLICADO',
    'controlesTecnicosAprobados':False,'matrices':mat}
 return r
class DryRun(unittest.TestCase):
 def test_snapshot_hash_and_full_formula_reconciliation(self):
  before=read(D/'registro_antes_matrices.json')
  snapshot=read(D/'resultados_hoja.json');formulas=read(D/'formulas.json')
  body=json.dumps(snapshot['data'],ensure_ascii=False,sort_keys=True,default=str)
  self.assertEqual(hashlib.sha256(body.encode()).hexdigest(),snapshot['data_sha256'])
  original=copy.deepcopy(before)
  result=mod.integrate(before,candidate(before,snapshot),snapshot,formulas)
  self.assertEqual(before,original)
  self.assertEqual(result['estado'],'EN_REVISION')
  self.assertEqual(result['valorPrincipal'],before['valorPrincipal'])
  self.assertEqual(result['precioMOS'],before['precioMOS'])
  self.assertEqual(result['descuentoMultiples'],before['descuentoMultiples'])
  self.assertEqual(result['metodos'],before['metodos'])
  self.assertEqual([m['estado'] for m in result['sensibilidadMultiples']['matrices']],
                   ['OK','N/A','OK','N/A','OK','OK','OK'])
  self.assertFalse(result['sensibilidadMultiples']['certificado'])
  active=read(ROOT/'valoraciones'/(REV+'.json'))
  if active.get('sensibilidadMultiples',{}).get('matrices'):
   self.assertEqual(active,result)
  else:
   self.assertEqual(active,before)
if __name__=='__main__':unittest.main()
