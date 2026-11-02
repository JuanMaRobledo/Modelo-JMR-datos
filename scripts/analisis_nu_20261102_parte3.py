#!/usr/bin/env python3
"""Ensambla ANALISIS_A12_EN_REVISION.json de NU-20261102-A12-R1 (Nivel 1 de 14 capítulos + Nivel 2 de 12 apartados)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_nu_20261102_parte1 as p1, analisis_nu_20261102_parte2 as p2
ROOT = p1.ROOT; REV = p1.REV; V = p1.V
n1, n2 = p1.nivel1_html(), p2.nivel2_html()
a = {'id': f'research-{REV}', 'ticker': 'NU', 'company': 'Nu Holdings Ltd.', 'title': 'Nu Holdings Ltd. · Modelo JMR A-1.2 · Análisis fundamental',
     'date': '2026-11-02', 'revisionId': REV, 'revision_id': REV, 'valoracionRevisionId': REV, 'price': V['precio'], 'priceFetchedAt': '2026-10-30',
     'estado': 'EN_REVISION', 'publicationStage': 'PREPUBLICACION_CONTROLADA', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
     'linkedValuation': {'sourcePath': f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json', 'revisionId': REV, 'valorPrincipal': V['valorPrincipal'],
                         'metodo_valoracion': 'A', 'version_metodo': 'A-1.2', 'estado': 'EN_REVISION'},
     'remotePath': f'candidatos/valoraciones/{REV}/ANALISIS_A12_EN_REVISION.json',
     'html': n1 + n2, 'articleHtml': n1, 'calculationHtml': n2,
     'jmrNarrative': {'version': 'A-1.2-20261102', 'nivel1Capitulos': 14, 'nivel2Apartados': 12},
     'documentoNivel1': 'scripts/analisis_nu_20261102_parte1.py', 'documentoNivel2': 'scripts/analisis_nu_20261102_parte2.py',
     'salvedades': 'EN_REVISION: sin auditoría económica ni QA visual autenticado. Ver capítulo 14 y apartado 12 del Nivel 2.',
     'controlCobertura': {'secciones': 14, 'niveles': 'N1_14_N2_12', 'revisionFinanciera': REV, 'auditoriaEconomicaEjecutada': False,
                         'seccionesAntesEstandarizacion': 14,
                         'notaConteos': 'secciones cuenta capítulos N1; entradas y resoluciones anteriores se conservan como inventario de evidencia, no como certificación.'},
     'estandarizacionEditorial20261031': {'nivel1Capitulos': 14, 'indiceInteractivo': True, 'ciclosSeparados': True, 'calculosModificados': False,
                                          'auditoriaEconomicaEjecutada': False, 'completitudInvestigacion': 'EN_REVISION_SALVEDADES'}}
out = ROOT / f'candidatos/valoraciones/{REV}/ANALISIS_A12_EN_REVISION.json'
out.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
v = json.loads((ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json').read_text())
v['controlEditorial'] = {'nivel1Capitulos': 14, 'nivel2Apartados': 12, 'estado': 'DOCUMENTOS_COMPLETADOS'}
(ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json').write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
print('ok', len(n1), len(n2))
