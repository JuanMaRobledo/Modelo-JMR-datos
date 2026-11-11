"""Regresión: una valoración CANDIDATO no está sustituida hasta publicarse."""
from __future__ import annotations
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "registro_revisiones.py"
spec = importlib.util.spec_from_file_location("registro_revisiones_for_test", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class RegistroCandidatosTest(unittest.TestCase):
    def test_candidato_no_publicado_no_es_sustituida(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"valoraciones").mkdir()
            (root/"candidatos"/"valoraciones").mkdir(parents=True)
            (root/"catalogo.json").write_text(json.dumps({"valoraciones":[]}),encoding="utf-8")
            old={"ticker":"CELH","revisionId":"CELH-20261028-A1","estado":"EN_REVISION"}
            new={"ticker":"CELH","revisionId":"CELH-REBOOT-3T26-R1",
                 "estado":"CANDIDATO","publicationStatus":"CANDIDATO"}
            (root/"valoraciones"/"CELH-20261028-A1.json").write_text(json.dumps(old),encoding="utf-8")
            (root/"valoraciones"/"CELH-REBOOT-3T26-R1.json").write_text(json.dumps(new),encoding="utf-8")
            previous=mod.ROOT
            try:
                mod.ROOT=root
                vigentes, revisiones=mod.recolectar()
                self.assertIn("CELH-20261028-A1",revisiones)
                self.assertNotIn("CELH-REBOOT-3T26-R1",revisiones)
                self.assertEqual(vigentes,{})
                new["estado"]="EN_REVISION"
                new["publicationStatus"]="EN_REVISION"
                (root/"valoraciones"/"CELH-REBOOT-3T26-R1.json").write_text(json.dumps(new),encoding="utf-8")
                _, revisiones=mod.recolectar()
                self.assertIn("CELH-REBOOT-3T26-R1",revisiones)
            finally:
                mod.ROOT=previous

if __name__=="__main__":
    unittest.main()
