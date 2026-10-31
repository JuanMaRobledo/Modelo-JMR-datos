import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
REV="SHAK-20261029-A12-R2"
SNAP=ROOT/"evidencia/captura-completa-candidata-20261031"/REV/"resultados_hoja.json"
PARTIAL=ROOT/"candidatos/hoja-multiples"/(REV+"-captura-rango.json")
OFFICIAL=ROOT/"valoraciones"/(REV+".json")
METHODS=("EV/EBITDA","EV/FCFF","P/E","P/FCFE","P/OCF","P/V","P/BV")

def near(a,b):
    return isinstance(a,(float,int)) and isinstance(b,(float,int)) and abs(a-b)<=max(1e-6,abs(b)*1e-8)

class CandidateIntegrity(unittest.TestCase):
    def test_complete_snapshot_integrity_without_publishing(self):
        s=json.loads(SNAP.read_text())
        p=json.loads(PARTIAL.read_text())
        v=json.loads(OFFICIAL.read_text())
        self.assertEqual(s["revision_id"],v["revisionId"])
        self.assertEqual(s["sheet_id"],v["sheet_id"])
        self.assertEqual(p["sourceSheetId"],s["sheet_id"])
        self.assertEqual(len(s["capture_ranges"]),30)
        self.assertEqual(s["data"]["audit_internal"],[])
        self.assertEqual(len(s["data"]),31)
        self.assertEqual(len(s["data"]["sens_mult"]),230)
        self.assertEqual(len(s["data"]["valuation_base"]),40)
        self.assertEqual(len(s["data"]["input"]),120)
        body=json.dumps(s["data"],ensure_ascii=False,sort_keys=True,default=str)
        self.assertEqual(hashlib.sha256(body.encode()).hexdigest(),s["data_sha256"],
                         "La foto no debe circular con un hash distinto al motor Python")
        rows=s["data"]["sens_mult"]
        for i,method in enumerate(METHODS):
            start=76+10*i
            capture=p["metodos"][i]
            self.assertEqual(capture["metodo"],method)
            self.assertTrue(rows[start-1][0].startswith("BASE · "+method+" ·"))
            self.assertEqual(rows[start+7][8],capture["estadoHoja"])
            if capture["estadoHoja"]=="OK":
                for rr in range(5):
                    for col in range(5):
                        self.assertTrue(near(rows[start+2+rr][col+1],capture["matriz"][rr][col]),
                                        method+" fila="+str(rr))
                self.assertTrue(near(rows[start+4][3],capture["vp3Original"]))
            else:
                self.assertEqual(capture["estadoHoja"],"N/D")
                self.assertIsNone(capture["matriz"])
        official_matrices=v.get("sensibilidadMultiples",{}).get("matrices") or []
        self.assertIn(len(official_matrices),(0,7))
        if official_matrices:
            self.assertEqual(v["sensibilidadMultiples"]["resultadosSha256"],s["data_sha256"])
            self.assertEqual(v["sensibilidadMultiples"]["estadoPublicacion"],"INTEGRADO_EN_REVISION")
            self.assertFalse(v["sensibilidadMultiples"]["certificado"])
        self.assertEqual(v["estado"],"EN_REVISION")

if __name__=="__main__":
    unittest.main()
