#!/usr/bin/env python3
"""Promueve INTU-20261101-A12-R1 a revisión activa EN_REVISION (autorización del usuario del 1-nov-2026).

INTU estaba fuera del catálogo (candidato INTU-20261029-R1 sin DCF nativo, conservado en candidatos/). Copia la valoración
y el análisis candidatos a sus rutas oficiales y añade INTU al catálogo. No toca otras empresas ni fórmulas. Idempotente.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'INTU-20261101-A12-R1'
VP, AP = f'valoraciones/{REV}.json', 'analisis/INTU-research-20261101-A12-R1.json'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'validationStatus': 'CONTROLES_TECNICOS_APROBADOS_EN_REVISION',
          'publicationAuthorization': "Usuario 1-nov-2026: «Autorizo» la promoción a EN_REVISION tras los controles técnicos; sin auditoría económica."})
v['salvedades'][0] = v['salvedades'][0].replace('EN_REVISION propuesta:', 'EN_REVISION:')
a['html'] = a['html'].replace('Candidato a EN_REVISION.', 'EN_REVISION.')
a['articleHtml'] = a['articleHtml'].replace('Candidato a EN_REVISION.', 'EN_REVISION.')
a['html'] = a['articleHtml'] + a['calculationHtml']
(ROOT / VP).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / AP).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
assert not any(p.startswith('valoraciones/INTU-') and p != VP for p in cat['valoraciones'])
if VP not in cat['valoraciones']: cat['valoraciones'].append(VP)
if AP not in cat['analisis']: cat['analisis'].append(AP)
cat['controlModeloA']['empresas']['INTU'] = {'rutaValoracion': VP, 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'NATIVOS_CINCO_PRIORITARIOS_EN_REVISION',
    'diagnostico': 'Valoración desde cero en copia limpia: DCF, cuatro escenarios, cinco múltiplos con descuento y matrices 5×5 nativos conciliados con la hoja (captura SHA-256). Sin auditoría económica ni QA visual autenticado; múltiplos Base 26 % bajo el DCF por el tope de la regla de ciclo.'}
if '+INTU-A12-20261101' not in cat['version']: cat['version'] += '+INTU-A12-20261101'
cat['actualizadoEl'] = '2026-11-01'
if 'INTU nueva selección A-1.2' not in cat['nota']:
    cat['nota'] += '\nINTU nueva selección A-1.2 EN_REVISION (1-nov-2026, autorizada): DCF Base US$402,00 y MOS35 US$261,30 calculados por la copia limpia con K5:K8 en LISTO; Conservadora 295,30, Optimista 506,93, Disrupción 187,79; corte 30-sep-2026 (275,71). El candidato INTU-20261029-R1 sigue conservado fuera del catálogo. Auditoría económica pendiente.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV, len(cat['valoraciones']), len(cat['analisis']))
