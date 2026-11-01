#!/usr/bin/env python3
"""Promueve NVDA-20261101-A12-R1 a revisión activa EN_REVISION conservando R4 fuera del catálogo activo.

Copia la valoración y el análisis candidatos a sus rutas oficiales, sustituye las entradas de NVDA en catalogo.json y archiva la
narrativa de auditoría anterior (sin borrar R4). No toca otras empresas ni fórmulas. Idempotente.
"""
import json, shutil, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'NVDA-20261101-A12-R1'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'publicationAuthorization': "Usuario 1-nov-2026: 'Sí, sigue con el JSON y la redacción de NVDA' dentro del encargo de publicar como EN_REVISION cuando los controles técnicos pasen; sin auditoría económica."})
(ROOT / f'valoraciones/{REV}.json').write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / f'analisis/NVDA-research-20261101-A12-R1.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
cat['valoraciones'] = [f'valoraciones/{REV}.json' if x == 'valoraciones/NVDA-20261025-R4.json' else x for x in cat['valoraciones']]
cat['analisis'] = [f'analisis/NVDA-research-20261101-A12-R1.json' if x == 'analisis/NVDA-research-20261025-r4.json' else x for x in cat['analisis']]
narr = ROOT / 'auditorias/narrativas/NVDA.md'
if 'auditorias/narrativas/NVDA.md' in cat['auditorias']:
    cat['auditorias'].remove('auditorias/narrativas/NVDA.md')
    if narr.exists():
        subprocess.run(['git', 'mv', str(narr), str(ROOT / 'archivo/NVDA-20261025-R4-legacy.md')], cwd=ROOT, check=True)
cat['controlModeloA']['empresas']['NVDA'] = {'rutaValoracion': f'valoraciones/{REV}.json', 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'NATIVOS_CINCO_PRIORITARIOS_EN_REVISION',
    'diagnostico': 'DCF, cuatro escenarios, cinco múltiplos con descuento y matrices 5×5 nativos conciliados con la hoja (captura SHA-256). Sin auditoría económica ni QA visual autenticado; año 1 Base 1,8 % bajo la guía anualizada; inversiones no operativas a valor contable.'}
cat['version'] = cat['version'] + '+NVDA-A12-20261101'
cat['actualizadoEl'] = '2026-11-01'
cat['nota'] = cat['nota'] + '\nNVDA nueva selección A-1.2 EN_REVISION (1-nov-2026): DCF Base US$205,95 y MOS35 US$133,87 calculados por la hoja con K5:K8 en LISTO; Conservadora 109,66, Optimista 354,62, Disrupción 50,08; cinco múltiplos nativos y matrices 5×5. R4 (381,79) conservada fuera del catálogo activo. Auditoría económica pendiente.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV)
