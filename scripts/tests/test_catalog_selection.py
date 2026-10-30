"""Active-release selection regression tests, isolated and offline."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('gate', Path(__file__).resolve().parents[1]/'verificar_cierre_multiplos.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class CatalogSelection(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.vp = 'valoraciones/NKE-new.json'
        self.ap = 'analisis/NKE-new.json'
        self.record = {'ticker': 'NKE', 'revisionId': 'NEW'}
        self.analysis = {**self.record, 'linkedValuation': {'sourcePath': self.vp, 'revisionId': 'NEW'}}
        self.catalog = {'valoraciones': [self.vp], 'analisis': [self.ap]}
        self.write('valoraciones/NKE-old.json', {'ticker': 'NKE', 'revisionId': 'OLD'})
        self.write('analisis/NKE-old.json', {'ticker': 'NKE', 'revisionId': 'OLD'})
        self.write(self.vp, self.record)
        self.write(self.ap, self.analysis)
        self.write('catalogo.json', self.catalog)

    def write(self, path, data):
        p = self.root/path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data))

    def test_ignores_uncatalogued_history(self):
        self.assertEqual(gate.active_pair('NKE', self.root), (self.record, self.analysis))

    def test_missing_active_record_does_not_fall_back(self):
        self.catalog['valoraciones'] = []
        self.write('catalogo.json', self.catalog)
        with self.assertRaisesRegex(AssertionError, 'exactamente un'):
            gate.active_pair('NKE', self.root)

    def test_duplicate_active_records_rejected(self):
        self.catalog['valoraciones'].append('valoraciones/NKE-old.json')
        self.write('catalogo.json', self.catalog)
        with self.assertRaisesRegex(AssertionError, 'encontrados 2'):
            gate.active_pair('NKE', self.root)

    def test_wrong_link_rejected(self):
        self.analysis['linkedValuation']['sourcePath'] = 'valoraciones/NKE-old.json'
        self.write(self.ap, self.analysis)
        with self.assertRaisesRegex(AssertionError, 'enlace'):
            gate.active_pair('NKE', self.root)

    def test_wrong_revision_rejected(self):
        self.analysis['revisionId'] = 'OLD'
        self.write(self.ap, self.analysis)
        with self.assertRaisesRegex(AssertionError, 'revisión activa discordante'):
            gate.active_pair('NKE', self.root)


if __name__ == '__main__':
    unittest.main()
