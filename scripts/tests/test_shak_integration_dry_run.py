import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
REV="SHAK-20261029-A12-R2"
DIR=ROOT/"evidencia/captura-completa-candidata-20261031"/REV
MOD=ROOT/"scripts/integrar_matrices_nativas.py"
METHODS=("EV/EBITDA","EV/FCFF","P/E","P/FCFE","P/OCF","P/V","P/BV")
spec=importlib.util.spec_from_file_location("integrador_nativo",MOD)
native=importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)

def load(path):
    return json.loads(Path(path).read_text())

def make_candidate(v,snapshot):
    data=snapshot["data"]["sens_mult"]
    result=copy.deepcopy(v)
    matrices=[]
    for i,method in enumerate(METHODS):
        start=76+10*i
        def at(row,col):
            values=data[row-1]
            return values[col-1] if col<=len(values) else ""
        state=at(start+8,9)
        assert state in ("OK","N/D"), (method,state)
        item={"metodo":method,"escenario":"base","ancla":"JMR",
              "origen":f"'Sensibilidad por múltiplo'!A{start}:I{start+8}",
              "estado":state,
              "fundamentalFY3":[at(start+2,c) for c in range(2,7)],
              "multiploElegido":[at(row,1) for row in range(start+3,start+8)],
              "matriz":[[at(row,col) for col in range(2,7)]
                        for row in range(start+3,start+8)] if state=="OK" else None,
              "centro":at(start+5,4) if state=="OK" else None,
              "vp3Original":at(start+8,7)}
        matrices.append(item)
    result["sensibilidadMultiples"]={**(v.get("sensibilidadMultiples") or {}),
        "contrato":"base-native-five-priority-v1",
        "revisionId":v["revisionId"],"sourceSheetId":v["sheet_id"],
        "resultadosSha256":snapshot["data_sha256"],
        "estadoPublicacion":"CANDIDATO_NO_PUBLICADO",
        "controlesTecnicosAprobados":False,
        "matrices":matrices}
    return result

class ShakDryRun(unittest.TestCase):
    def test_integrator_does_not_modify_original_record(self):
        snap=load(DIR/"resultados_hoja.json")
        formulas=load(DIR/"formulas.json")
        original=load(DIR/"registro_antes.json")
        active=load(ROOT/"valoraciones"/(REV+".json"))
        before=copy.deepcopy(original)
        body=json.dumps(snap["data"],ensure_ascii=False,sort_keys=True,default=str)
        self.assertEqual(hashlib.sha256(body.encode()).hexdigest(),snap["data_sha256"])
        candidate=make_candidate(original,snap)
        out=native.integrate(original,candidate,snap,formulas)
        self.assertEqual(original,before)
        self.assertEqual(out["estado"],"EN_REVISION")
        self.assertEqual(out["valorPrincipal"],before["valorPrincipal"])
        self.assertEqual(out["precioMOS"],before["precioMOS"])
        self.assertEqual(out["escenariosDCF"],before["escenariosDCF"])
        self.assertEqual(out["descuentoMultiples"],before["descuentoMultiples"])
        self.assertEqual(out["revisionId"],before["revisionId"])
        self.assertEqual(out["sheet_id"],before["sheet_id"])
        self.assertEqual(out["sensibilidadMultiples"]["estadoPublicacion"],"INTEGRADO_EN_REVISION")
        self.assertEqual([m["estado"] for m in out["sensibilidadMultiples"]["matrices"]],
                         ["OK","N/A","OK","N/A","OK","OK","OK"])
        for m in out["sensibilidadMultiples"]["matrices"]:
            if m["estado"]=="N/A":
                self.assertEqual(m["estadoFuente"],"N/D")
                self.assertIsNone(m["matriz"])
                self.assertIn("peso cero",m["motivo"])
            else:
                self.assertEqual(len(m["matriz"]),5)
                self.assertTrue(all(len(r)==5 for r in m["matriz"]))
        self.assertFalse(out["sensibilidadMultiples"]["certificado"])
        self.assertEqual(out["auditoriaEconomica"],before["auditoriaEconomica"])
        if active.get("sensibilidadMultiples",{}).get("matrices"):
            self.assertEqual(active,out,"El registro integrado difiere de la ejecución Python verificada")
        else:
            self.assertEqual(active,original,"No se debe alterar el expediente antes de integrar")

if __name__=="__main__":
    unittest.main()
