import json
import math
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
REV="MELI-20261028-A3"
DIR=ROOT/"evidencia/descuentos-candidatos-20261031"
METHODS=("EV/EBITDA","EV/FCFF","P/E","P/FCFE","P/OCF")
SCENARIOS=(("conservador",10),("base",19),("optimista",28))

def read(p):
    return json.loads(Path(p).read_text())

def near(a,b):
    return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isclose(a,b,rel_tol=1e-8,abs_tol=1e-6)

class DiscountEvidence(unittest.TestCase):
    def test_source_formula_and_cash_flow_consistency(self):
        n=read(DIR/(REV+"-UNFORMATTED_VALUE.json"))
        f=read(DIR/(REV+"-FORMULA.json"))
        old=read(DIR/(REV+"-registro_antes.json"))
        active=read(ROOT/"valoraciones"/(REV+".json"))
        self.assertEqual(n["sourceSheetId"],old["sheet_id"])
        self.assertEqual(f["revisionId"],old["revisionId"])
        self.assertEqual(old["valorPrincipal"],active["valorPrincipal"])
        self.assertEqual(old["precioMOS"],active["precioMOS"])
        # El registro MELI no contiene escenariosDCF; la comparación integral
        # de todos los campos ajenos a descuentoMultiples se hace abajo.
        self.assertEqual(old["metodos"],active["metodos"])
        ignored={"descuentoMultiples","sensibilidadMultiples"}
        self.assertEqual({k:v for k,v in old.items() if k not in ignored},
                         {k:v for k,v in active.items() if k not in ignored})
        rows=n["values"]
        fr=f["values"]
        self.assertTrue(near(rows[37][3],old["valorPrincipal"]))
        self.assertTrue(near(rows[37][1],old["descuentoMultiples"]["pesoDcf"]))
        self.assertTrue(near(rows[38][1],old["descuentoMultiples"]["pesoMultiplos"]))
        for idx,key in ((37,"dcfHoy"),(38,"multiplesHoy"),(39,"ponderadoHoy")):
            for col,name in ((2,"conservador"),(3,"base"),(4,"optimista")):
                self.assertTrue(near(rows[idx][col],old["descuentoMultiples"][key][name]))
        for name,start in SCENARIOS:
            for i,method in enumerate(METHODS):
                row,formula=rows[start+i],fr[start+i]
                self.assertEqual(row[0],method)
                self.assertTrue(all(isinstance(row[j],(int,float)) for j in range(3,10)))
                self.assertTrue(all(isinstance(formula[j],str) and formula[j].startswith("=") for j in range(3,10)))
                if i in (1,3):
                    self.assertLess(row[5],0)
                    self.assertLess(row[8],0)
                    self.assertEqual(row[1],0)
                if active["descuentoMultiples"].get("integracionNativa"):
                    record=active["descuentoMultiples"]["metodos"][i][name]
                    self.assertEqual(record["fy"],row[3:6])
                    self.assertEqual(record["vp"],row[6:9])
                    self.assertTrue(near(record["consolidado"],row[9]))
        if active["descuentoMultiples"].get("integracionNativa"):
            self.assertEqual(active["estado"],"EN_REVISION")
            self.assertFalse(active["descuentoMultiples"]["integracionNativa"]["certificadoEconomico"])
            self.assertEqual(len(active["descuentoMultiples"]["metodos"]),5)

if __name__=="__main__":
    unittest.main()
