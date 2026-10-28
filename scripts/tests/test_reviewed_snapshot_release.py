"""Publication regression: copied real release, no network or external writes."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('release_check', ROOT/'scripts/verificar_cierre_multiplos.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class ReviewedSnapshotRelease(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record=json.loads((ROOT/'archivo/NFLX-antes-NFLX-20261028-R1/valoracion-20261025.json').read_text())
        cls.analysis=json.loads((ROOT/'archivo/NFLX-antes-NFLX-20261028-R1/analisis-20261025.json').read_text())
        cls.evidence=json.loads((ROOT/cls.record['cierreMultiplos']['evidencePath']).read_text())
        cls.audit=(ROOT/'archivo/NFLX-antes-NFLX-20261028-R1/auditoria-20261025.md').read_text()

    def test_real_release_replays_63_prices_and_discounts(self):
        result=check.verify_snapshot_release(self.record,self.analysis,self.evidence,self.audit)
        self.assertEqual(result['pricesAndDiscountsReplayed'],63)
        self.assertEqual(result['criterion'],'Promedio 1-3 años')

    def test_changed_discounted_result_fails(self):
        record=copy.deepcopy(self.record)
        record['descuentoMultiples']['metodos'][0]['base']['vp'][1]+=1
        with self.assertRaises(AssertionError):
            check.verify_snapshot_release(record,self.analysis,self.evidence,self.audit)

    def test_changed_source_hash_fails(self):
        evidence={**self.evidence,'sourceSha256':'0'*64}
        with self.assertRaises(AssertionError):
            check.verify_snapshot_release(self.record,self.analysis,evidence,self.audit)

    def test_different_analysis_revision_fails(self):
        analysis={**self.analysis,'revisionId':'OTHER-REVISION'}
        with self.assertRaises(AssertionError):
            check.verify_snapshot_release(self.record,analysis,self.evidence,self.audit)


if __name__ == '__main__':
    unittest.main()
