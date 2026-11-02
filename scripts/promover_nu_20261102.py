#!/usr/bin/env python3
"""Promueve NU-20261102-A12-R1 a revisión activa EN_REVISION (sin auditoría económica).
Autorización: instrucción del usuario del 2-nov-2026 («publica la valoración y el análisis en EN_REVISION» si los controles obligatorios se aprueban).
NU-20261029-R1 permanece en candidatos/ sin cambios. Idempotente."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'NU-20261102-A12-R1'
VP, AP = f'valoraciones/{REV}.json', f'analisis/NU-research-20261102-A12-R1.json'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'validationStatus': 'CONTROLES_TECNICOS_APROBADOS_EN_REVISION',
          'publicationAuthorization': 'Usuario 2-nov-2026: publicar valoración y análisis en EN_REVISION si los controles obligatorios se aprueban; sin auditoría económica.'})
a['linkedValuation']['sourcePath'] = VP; a['remotePath'] = AP; a['publicationStage'] = 'PUBLICACION_EN_REVISION'
(ROOT / VP).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / AP).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
assert not any(p.startswith('valoraciones/NU-') and p != VP for p in cat['valoraciones'])
if VP not in cat['valoraciones']: cat['valoraciones'].append(VP)
if AP not in cat['analisis']: cat['analisis'].append(AP)
cat['controlModeloA']['empresas']['NU'] = {'rutaValoracion': VP, 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'CONTRASTE_BANCARIO_PE_PBV_CALCULADOS_PFCFE_PENDIENTE_ANCLA',
    'diagnostico': 'DCF FCFE nativo en las pestañas añadidas de la hoja, cuatro historias, sensibilidades 5x5 y DCF inverso conciliados con la hoja (SHA-256). P/E y P/BV contraste con peso 0; P/FCFE pendiente de ancla; reserva material de capital regulatorio (APR por entidad) y de Ke; sin auditoría económica.'}
if '+NU-A12-20261102' not in cat['version']: cat['version'] += '+NU-A12-20261102'
cat['actualizadoEl'] = '2026-11-02'
cat['nota'] += '\nNU nueva selección A-1.2 EN_REVISION (2-nov-2026): DCF FCFE Base y MOS35 calculados por la copia limpia de la plantilla IA (Análisis/NU); NU-20261029-R1 queda en candidatos sin cambios.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV, len(cat['valoraciones']), len(cat['analisis']))
