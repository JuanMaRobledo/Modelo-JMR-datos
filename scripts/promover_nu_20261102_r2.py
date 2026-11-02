#!/usr/bin/env python3
"""Promueve NU-20261102-A12-R2 a revisión activa EN_REVISION y retira del catálogo la R1 (sin borrarla).
Autorización: el usuario pidió el 2-nov-2026 atender la auditoría de la R1 («utiliza tu criterio para escoger el mejor curso») tras haber
autorizado la publicación EN_REVISION con controles aprobados. La R1 (valoraciones/NU-20261102-A12-R1.json y su análisis) se conserva
en el repositorio fuera del catálogo, con la marca 'sustituidaPor'. Idempotente."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV, R1 = 'NU-20261102-A12-R2', 'NU-20261102-A12-R1'
VP, AP = f'valoraciones/{REV}.json', 'analisis/NU-research-20261102-A12-R2.json'
VP1, AP1 = f'valoraciones/{R1}.json', 'analisis/NU-research-20261102-A12-R1.json'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'validationStatus': 'CONTROLES_DEL_CATALOGO_APROBADOS_INTEGRIDAD_DE_HOJA_CON_4_HALLAZGOS_FCFE_PENDIENTE_QA_VISUAL',
          'publicationAuthorization': 'Usuario 2-nov-2026: atender la auditoría A1/A1.1 de la R1 con criterio propio («utiliza tu criterio para escoger el mejor curso»), dentro de la autorización previa de publicar EN_REVISION con controles aprobados. Sin auditoría económica de la R2 ni QA visual autenticado.',
          'sustituyeA': R1})
a['linkedValuation']['sourcePath'] = VP; a['remotePath'] = AP; a['publicationStage'] = 'PUBLICACION_EN_REVISION'
(ROOT / VP).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / AP).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
# R1: fuera del catálogo, conservada con marca
for p in (VP1,):
    r1 = json.loads((ROOT / p).read_text())
    if r1.get('sustituidaPor') != REV:
        r1.update({'sustituidaPor': REV, 'valorVigenteEnCatalogo': False, 'publicadaEnApp': False,
                   'notaSustitucion': 'Retirada del catálogo el 2-nov-2026 al promover la R2 (Ke y capital revisados por la auditoría A1/A1.1); cifras y análisis sin cambios.'})
        (ROOT / p).write_text(json.dumps(r1, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
cat['valoraciones'] = [p for p in cat['valoraciones'] if p != VP1]
cat['analisis'] = [p for p in cat['analisis'] if p != AP1]
assert not any(p.startswith('valoraciones/NU-') and p != VP for p in cat['valoraciones'])
if VP not in cat['valoraciones']: cat['valoraciones'].append(VP)
if AP not in cat['analisis']: cat['analisis'].append(AP)
cat['controlModeloA']['empresas']['NU'] = {'rutaValoracion': VP, 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'CONTRASTE_BANCARIO_PE_PBV_CALCULADOS_PFCFE_PENDIENTE_ANCLA',
    'diagnostico': 'R2: DCF FCFE nativo con capital ligado al APR (τ × APR) y Ke con beta 1,00, prima país y ERP al 30-oct-2026; cuatro historias, sensibilidades 5x5, DCF inverso y retención sobre dividendos conciliados con la hoja (SHA-256). P/E y P/BV contraste con peso 0; P/FCFE pendiente de ancla; sin auditoría económica de la R2.'}
if '+NU-A12-R2-20261102' not in cat['version']: cat['version'] += '+NU-A12-R2-20261102'
cat['actualizadoEl'] = '2026-11-02'
if 'NU R2 A-1.2 EN_REVISION (2-nov-2026)' not in cat['nota']:
    cat['nota'] += '\nNU R2 A-1.2 EN_REVISION (2-nov-2026): sustituye a NU-20261102-A12-R1 tras su auditoría (Ke y capital revisados); la R1 se conserva fuera del catálogo.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV, len(cat['valoraciones']), len(cat['analisis']))
