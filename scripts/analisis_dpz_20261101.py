#!/usr/bin/env python3
"""Análisis fundamental de DPZ (revisión DPZ-20261101-A1): convierte el informe del expediente
(JMR-valuation data/DPZ_Research_JMR_A1_2026-11-01.md, N1 14 capítulos + N2 12 apartados) al JSON que lee la app.
No recalcula cifras: el texto ya usa los valores de la hoja; se verifica que el DCF Base, el MOS y los escenarios del
informe coinciden con la valoración construida desde la captura de la hoja."""
import json, re, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
REV = 'DPZ-20261101-A1'
MD = ROOT.parent / 'JMR-valuation' / 'data' / 'DPZ_Research_JMR_A1_2026-11-01.md'
VAL = ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json'
V = json.loads(VAL.read_text())
txt = MD.read_text()
body = txt.split('---\n', 2)[2]
n1, n2 = body.split('\n# NIVEL 2', 1)
n2 = '# NIVEL 2' + n2
es = lambda x: f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
for k, x in (('Base', V['valorPrincipal']), ('MOS', V['precioMOS']), ('promedio', V['valorEsperado']['valor'])):
    if es(x) not in txt: sys.exit(f'FALLA: {k} {es(x)} no aparece en el informe')
for x in V['escenarios'].values():
    if es(x) not in txt: sys.exit(f'FALLA: escenario {es(x)} no aparece en el informe')
md = lambda s: markdown.markdown(s, extensions=['tables'])
def sections(s, prefix, pat):
    parts = re.split(r'\n(?=## )', s)
    head, out, titles = parts[0], [], []
    for i, p in enumerate(parts[1:], 1):
        t = p.splitlines()[0][3:].strip(); titles.append(t)
        html = md(p)
        out.append(f'<section id="{prefix}{i}">{html}</section>')
    return head, out, titles
h1, c1, t1 = sections(n1, 'jmr-n1-chapter-', None)
h2, c2, t2 = sections(n2, 'jmr-n2-', None)
assert len(c1) == 14 and len(c2) == 12, (len(c1), len(c2))
nav = '<nav aria-label="Índice del análisis fundamental" data-jmr-n1-standard="14-20261031"><ol>' + ''.join(
    f'<li><a href="#jmr-n1-chapter-{i+1}">{t}</a></li>' for i, t in enumerate(t1)) + '</ol></nav>'
head = re.sub(r'<p><strong>Índice\.</strong>.*?</p>', '', md(h1.replace('# NIVEL 1 — Artículo de inversión', '')), flags=re.S)
article = f'<article data-jmr-revision="{REV}" data-metodo="A-1.2"><header>{head}</header>{nav}{"".join(c1)}</article>'
calc = f'<article data-jmr-revision="{REV}" data-nivel="2" data-metodo="A-1.2"><h1>Domino\'s Pizza — Nivel 2 reproducible · Método A-1.2 / FCFF nominal USD</h1>{"".join(c2)}</article>'
w = lambda h: len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).split())
print('N1 palabras', w(article), 'capítulos', len(c1), '| N2 palabras', w(calc), 'apartados', len(c2))
out = {'id': f'research-{REV}', 'ticker': 'DPZ', 'company': "Domino's Pizza, Inc.", 'title': "Domino's Pizza, Inc. · Modelo JMR A-1.2 · Análisis fundamental",
  'date': '2026-11-01', 'revisionId': REV, 'revision_id': REV, 'valoracionRevisionId': REV, 'price': V['precio'], 'priceFetchedAt': '2026-09-30',
  'estado': 'EN_REVISION', 'publicationStage': 'PUBLICACION_EN_REVISION', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
  'linkedValuation': {'sourcePath': f'valoraciones/{REV}.json', 'revisionId': REV, 'valorPrincipal': V['valorPrincipal'], 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2'},
  'remotePath': 'analisis/DPZ-research-20261101-A1.json', 'html': article + calc, 'articleHtml': article, 'calculationHtml': calc,
  'jmrNarrative': {'version': 'A-1.2-20261101', 'nivel1Capitulos': 14, 'nivel2Apartados': 12},
  'documentoNivel1': 'JMR-valuation: data/DPZ_Research_JMR_A1_2026-11-01.md', 'documentoNivel2': 'JMR-valuation: data/DPZ_Research_JMR_A1_2026-11-01.md',
  'salvedades': 'EN_REVISION: sin auditoría económica ni QA visual autenticado. Ver capítulo 14 y apartado 12 del Nivel 2.',
  'controlCobertura': {'secciones': 14, 'niveles': 'N1_14_N2_12', 'revisionFinanciera': REV, 'auditoriaEconomicaEjecutada': False},
  'estandarizacionEditorial20261031': {'nivel1Capitulos': 14, 'indiceInteractivo': True, 'ciclosSeparados': True, 'calculosModificados': False,
                                       'auditoriaEconomicaEjecutada': False, 'completitudInvestigacion': 'EN_REVISION_SALVEDADES'}}
sys.path.insert(0, str(ROOT / 'scripts'))
from estandarizar_nivel1 import standardize
out = standardize(out)
assert standardize(json.loads(json.dumps(out))) == out, 'estandarización no idempotente'
dest = ROOT / f'candidatos/valoraciones/{REV}/ANALISIS_A12_EN_REVISION.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n'); print('escrito', dest.relative_to(ROOT))
