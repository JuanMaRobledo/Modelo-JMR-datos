#!/usr/bin/env python3
"""Promueve META-20261101-A12-R1 a revisión activa EN_REVISION conservando R5 fuera del catálogo activo.

Copia la valoración y el análisis candidatos a sus rutas oficiales, sustituye las entradas de META en catalogo.json y archiva la
narrativa de auditoría anterior (sin borrar R4). No toca otras empresas ni fórmulas. Idempotente.
"""
import json, shutil, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'META-20261101-A12-R1'
cand = ROOT / f'candidatos/valoraciones/{REV}'
v = json.loads((cand / 'VALORACION_A12_EN_REVISION.json').read_text())
a = json.loads((cand / 'ANALISIS_A12_EN_REVISION.json').read_text())
v.update({'valorVigenteEnCatalogo': True, 'publicadaEnApp': True, 'publicationAuthorized': True, 'auditPendingUserVisualReview': True,
          'publicationAuthorization': "Usuario 1-nov-2026: 'Sigue con META' dentro del encargo de publicar como EN_REVISION cuando los controles técnicos pasen; sin auditoría económica."})
(ROOT / f'valoraciones/{REV}.json').write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
(ROOT / f'analisis/META-research-20261101-A12-R1.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
cat = json.loads((ROOT / 'catalogo.json').read_text())
cat['valoraciones'] = [f'valoraciones/{REV}.json' if x == 'valoraciones/META-20261025-R5.json' else x for x in cat['valoraciones']]
cat['analisis'] = [f'analisis/META-research-20261101-A12-R1.json' if x == 'analisis/META-research-20261025-r5.json' else x for x in cat['analisis']]
narr = ROOT / 'auditorias/narrativas/META.md'
if 'auditorias/narrativas/META.md' in cat['auditorias']:
    cat['auditorias'].remove('auditorias/narrativas/META.md')
    if narr.exists():
        subprocess.run(['git', 'mv', str(narr), str(ROOT / 'archivo/META-20261025-R5-legacy.md')], cwd=ROOT, check=True)
cat['controlModeloA']['empresas']['META'] = {'rutaValoracion': f'valoraciones/{REV}.json', 'metodo': 'A-1.2', 'estado': 'INCOMPLETA_EN_REVISION',
    'multiplos': 'NATIVOS_CINCO_PRIORITARIOS_EN_REVISION',
    'diagnostico': 'DCF, cuatro escenarios, cinco múltiplos con descuento y matrices 5×5 nativos conciliados con la hoja (captura SHA-256). Sin auditoría económica ni QA visual autenticado; arrendamientos no iniciados (355.730 M) y compromisos (454.520 M) no cuantificados en la valoración; provisiones legales deducidas en bruto; múltiplos 46 % bajo el DCF.'}
cat['version'] = cat['version'] + '+META-A12-20261101'
cat['actualizadoEl'] = '2026-11-01'
cat['nota'] = cat['nota'] + '\nMETA nueva selección A-1.2 EN_REVISION (1-nov-2026): DCF Base US$737,51 y MOS35 US$479,38 calculados por la hoja con K5:K8 en LISTO; Conservadora 457,18, Optimista 1.086,77, Disrupción 232,18; cinco múltiplos nativos y matrices 5×5; provisiones legales de 19.881 M deducidas. R5 (726,65) conservada fuera del catálogo activo. Arrendamientos no iniciados y compromisos no cancelables sin cuantificar; auditoría económica pendiente.'
(ROOT / 'catalogo.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n')
print('promovido', REV)
