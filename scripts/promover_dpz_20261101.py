#!/usr/bin/env python3
"""Promueve DPZ-20261101-A1 a revisión activa EN_REVISION (autorización del usuario del 1-nov-2026: «Hazlo»).

DPZ no estaba en el catálogo activo (su valoración B histórica y el análisis antiguo analisis/DPZ-research-1790597462756-7k8ad.json
quedan fuera y sin cambios). Copia la valoración y el análisis candidatos a sus rutas oficiales y añade DPZ al catálogo.
No toca otras empresas ni fórmulas. Idempotente."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'DPZ-20261101-A1'
VP, AP = f'valoraciones/{REV}.json', 'analisis/DPZ-research-20261101-A1.json'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'validationStatus': 'CONTROLES_TECNICOS_APROBADOS_EN_REVISION',
          'publicationAuthorization': "Usuario 1-nov-2026: «Hazlo» (actualizar el verificador de múltiplos y pasar a EN_REVISION); sin auditoría económica."})
(ROOT / VP).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / AP).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
assert not any(p.startswith('valoraciones/DPZ-') and p != VP for p in cat['valoraciones'])
if VP not in cat['valoraciones']: cat['valoraciones'].append(VP)
if AP not in cat['analisis']: cat['analisis'].append(AP)
cat['controlModeloA']['empresas']['DPZ'] = {'rutaValoracion': VP, 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'NATIVOS_CINCO_PRIORITARIOS_EN_REVISION',
    'diagnostico': 'Valoración desde cero en copia limpia: DCF, cuatro escenarios, cinco múltiplos con descuento y matrices 5×5 nativos conciliados con la hoja (captura SHA-256). P/BV N/A por patrimonio negativo. Sin auditoría económica ni QA visual autenticado.'}
if '+DPZ-A1-20261101' not in cat['version']: cat['version'] += '+DPZ-A1-20261101'
cat['actualizadoEl'] = '2026-11-01'
if 'DPZ nueva selección A-1.2' not in cat['nota']:
    cat['nota'] += '\nDPZ nueva selección A-1.2 EN_REVISION (1-nov-2026, autorizada): DCF Base US$308,46 y MOS35 US$200,50 calculados por la copia limpia (Análisis/DPZ); Conservadora 210,71, Optimista 401,74, Disrupción 92,44; promedio 302,03; corte 30-sep-2026 (299,61). Auditoría económica pendiente.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV, len(cat['valoraciones']), len(cat['analisis']))
