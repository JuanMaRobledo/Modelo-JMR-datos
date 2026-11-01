import copy
import hashlib
import importlib.util
import json
import re
import sys
import unittest
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from integrar_descuentos_nativos import integrate
from estandarizar_nivel1 import standardize, Document
from restaurar_nivel2_desde_foto import active_analysis_path

class NativeDiscountTests(unittest.TestCase):
    SEIS=('NKE','PYPL','EPAM','ZTS','NVO','ONON')
    def fixture(self,ticker='ADBE'):
        carpeta='evidencia/descuentos-20261101' if ticker in self.SEIS else 'evidencia/descuentos-20261031'
        p=next(p for p in (ROOT/carpeta).glob('*-UNFORMATTED_VALUE.json') if '-DCF-' not in p.name and json.loads(p.read_text())['ticker']==ticker)
        c=json.loads(p.read_text())
        f=json.loads(p.with_name(p.name.replace('UNFORMATTED_VALUE','FORMULA')).read_text())
        # La captura anterior a los descuentos completos se prueba con su
        # respaldo exacto. El test MSFT nuevo comprueba la extensión actual.
        if ticker=='MSFT':
            prev=ROOT/'evidencia/descuentos-nativos-20261031'/c['revisionId']/'registro_antes.json'
            v=json.loads(prev.read_text())
        else:
            v=json.loads((ROOT/'valoraciones'/(c['revisionId']+'.json')).read_text())
        return v,c,f,hashlib.sha256(p.read_bytes()).hexdigest()

    def test_all_fourteen_reproduce_and_preserve_financial_fields(self):
        paths=[p for p in (ROOT/'evidencia/descuentos-20261031').glob('*-UNFORMATTED_VALUE.json') if '-DCF-' not in p.name]
        self.assertEqual(len(paths),14)
        for p in paths:
            ticker=json.loads(p.read_text())['ticker']
            v,c,f,h=self.fixture(ticker)
            before=copy.deepcopy(v)
            self.assertEqual(integrate(v,c,f,h),before,ticker)

    def test_reject_wrong_revision(self):
        v,c,f,h=self.fixture();c['revisionId']='OTHER'
        with self.assertRaises(AssertionError): integrate(v,c,f,h)

    def test_reject_wrong_sheet(self):
        v,c,f,h=self.fixture();c['sourceSheetId']='OTHER'
        with self.assertRaises(AssertionError): integrate(v,c,f,h)

    def test_reject_dcf_change(self):
        v,c,f,h=self.fixture();c['values'][37][3]+=1
        with self.assertRaises(AssertionError): integrate(v,c,f,h)

    def test_reject_vp3_change(self):
        v,c,f,h=self.fixture();c['values'][19][8]+=1
        with self.assertRaises(AssertionError): integrate(v,c,f,h)

    def test_reject_constant_formula(self):
        v,c,f,h=self.fixture();f['values'][19][6]=123
        with self.assertRaises(AssertionError): integrate(v,c,f,h)

    def test_missing_scenarios_stay_null(self):
        for ticker in ['MSFT']:
            v,c,f,h=self.fixture(ticker);d=integrate(v,c,f,h)['descuentoMultiples']
            self.assertIn('PENDIENTE',d['integracionNativa']['estado'])
            for method in d['metodos']:
                self.assertIsNone(method['conservador'])
                self.assertIsNone(method['optimista'])
                self.assertEqual(len(method['base']['vp']),3)

    def test_six_resolved_have_all_scenarios_and_sheet_weights(self):
        for ticker in self.SEIS:
            v,c,f,h=self.fixture(ticker);d=integrate(v,c,f,h)['descuentoMultiples']
            self.assertEqual(d['integracionNativa']['estado'],'METODOS_Y_CONSOLIDACION_CONCILIADOS',ticker)
            self.assertAlmostEqual(d['pesoDcf'],c['values'][37][1],msg=ticker)
            for method in d['metodos']:
                self.assertIsNotNone(method['conservador'],ticker);self.assertIsNotNone(method['optimista'],ticker)

class EditorialTests(unittest.TestCase):
    def test_historical_filename_never_selects_active_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'analisis').mkdir()
            (root/'analisis/AFYA-000-historico.json').write_text('{}')
            active=root/'analisis/AFYA-activo.json';active.write_text('{}')
            (root/'catalogo.json').write_text(json.dumps({'analisis':['analisis/AFYA-activo.json']}))
            self.assertEqual(active_analysis_path(root,'AFYA'),active)

    def test_ambiguous_active_catalog_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'catalogo.json').write_text(json.dumps({'analisis':['analisis/AFYA-one.json','analisis/AFYA-two.json']}))
            with self.assertRaises(ValueError): active_analysis_path(root,'AFYA')

    def test_all_active_a12_linked_indices_and_cycle_chapters(self):
        catalog=json.loads((ROOT/'catalogo.json').read_text())
        files=[ROOT/p for p in catalog['analisis'] if (ROOT/p).exists()]
        selected=[json.loads(p.read_text()) for p in files if json.loads(p.read_text()).get('version_metodo')=='A-1.2']
        self.assertEqual(len(selected),22)
        for a in selected:
            h=a['articleHtml'];doc=Document(h)
            ids=[n.attrs.get('id') for n in doc.nodes]
            headings=re.findall(r'<h2[^>]*>\s*(\d+)\.',h)
            self.assertEqual(headings,list(map(str,range(1,15))),a['ticker'])
            self.assertEqual(h.count('data-jmr-n1-standard='),1,a['ticker'])
            for i in range(1,15):
                self.assertEqual(ids.count('jmr-n1-chapter-'+str(i)),1)
                self.assertIn('href="#jmr-n1-chapter-'+str(i)+'"',h)
            self.assertEqual(a['html'],h+a.get('calculationHtml',''))
            if a.get('controlCobertura',{}).get('secciones') is not None:
                self.assertEqual(a['controlCobertura']['secciones'],14)
            self.assertEqual(standardize(copy.deepcopy(a)),a)

    def test_two_n2_reports_have_twelve_sourced_sections(self):
        for ticker in ['AFYA','DUOL']:
            a=json.loads(active_analysis_path(ROOT,ticker).read_text())
            h=a['calculationHtml']
            for i in range(1,13):
                self.assertIn('id="jmr-'+ticker.lower()+'-n2-repro-'+str(i)+'"',h)
            self.assertNotIn('Soporte cuantitativo pendiente de importación',h)
            self.assertEqual(a['nivel2Reproduccion20261031']['apartados'],12)
            self.assertFalse(a['nivel2Reproduccion20261031']['auditoriaEconomicaEjecutada'])

    def test_four_expansions_are_specific_and_do_not_certify(self):
        for ticker in ['SHAK','UBER','AFYA','DUOL']:
            a=json.loads(active_analysis_path(ROOT,ticker).read_text())
            self.assertEqual(a['ampliacionEditorial20261031']['capitulosAmpliados'],list(range(1,15)))
            self.assertFalse(a['ampliacionEditorial20261031']['supuestosModificados'])
            self.assertFalse(a['ampliacionEditorial20261031']['auditoriaEconomicaEjecutada'])

if __name__=='__main__': unittest.main()
