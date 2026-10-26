#!/usr/bin/env python3
"""Mide si cada análisis fundamental guardado cumple los mínimos de profundidad del prompt de investigación v5 (REGLAS §9).

Por sección numerada (h2) cuenta párrafos sustantivos (<p> de 40 palabras o más), palabras y tablas. Mínimos del prompt:
secciones 2, 4, 5, 6 y 8: al menos 3 párrafos sustantivos; secciones 3 y 7: al menos 2; sección 13: cinco filosofías con un párrafo cada una;
sección 11: tabla con al menos 5 argumentos por lado; sección 9: al menos 4 catalizadores; sección 10: al menos 6 riesgos;
sección 15: 8 a 12 indicadores; sección 17: al menos 8 fuentes. Los títulos 'Las 5 fuerzas de Porter' y 'Síntesis final' son obligatorios.
Es un control de forma: no juzga la calidad del razonamiento. Uso: python3 scripts/auditar_profundidad.py  → auditorias/revision-2026-10-26/PROFUNDIDAD.md
"""
import glob, json, re, os

def texto(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()

def secciones(art):
    partes = re.split(r'(?=<h2[^>]*>)', art)
    out = {}
    for p in partes:
        m = re.match(r'<h2[^>]*>(.*?)</h2>', p, re.S)
        if not m:
            continue
        t = texto(m.group(1)); n = re.match(r'(\d{1,2})\.\s', t)
        if n:
            out[int(n.group(1))] = (t, p)
    return out

def filas(html):
    return max(0, len(re.findall(r'<tr', html)) - len(re.findall(r'<table', html)))

MIN_P = {2: 3, 4: 3, 5: 3, 6: 3, 8: 3, 3: 2, 7: 2}
res = []
for p in sorted(glob.glob('analisis/*.json')):
    a = json.load(open(p, encoding='utf-8')); art = a.get('articleHtml') or ''
    sec = secciones(art); falta = []
    for n in range(1, 19):
        if n not in sec:
            falta.append(f'falta la sección {n}'); continue
        _, h = sec[n]
        ps = [x for x in re.findall(r'<p[^>]*>(.*?)</p>', h, re.S) if len(texto(x).split()) >= 40]
        if n in MIN_P and len(ps) < MIN_P[n]:
            falta.append(f'§{n}: {len(ps)} párrafos sustantivos (mín. {MIN_P[n]})')
        if n == 9 and filas(h) < 4: falta.append(f'§9: {filas(h)} catalizadores (mín. 4)')
        if n == 10 and filas(h) < 6: falta.append(f'§10: {filas(h)} filas de riesgos (mín. 6)')
        if n == 15 and not 8 <= filas(h) <= 14: falta.append(f'§15: {filas(h)} indicadores (8 a 12)')
        if n == 13:
            f = sum(1 for x in ('Buffett', 'Munger', 'Lynch', 'Marks', 'Greenblatt') if x in h)
            if f < 5: falta.append(f'§13: {f} de 5 filosofías')
        if n == 17:
            enl = len(re.findall(r'https?://', h))
            if enl < 8: falta.append(f'§17: {enl} enlaces (mín. 8)')
    if 'Las 5 fuerzas de Porter' not in art: falta.append('falta «Las 5 fuerzas de Porter»')
    if 'Síntesis final' not in art: falta.append('falta «Síntesis final»')
    pal = len(texto(art).split())
    res.append((a.get('ticker'), p, pal, len(a.get('calculationHtml') or ''), falta))
L = ['# Profundidad del análisis fundamental · 26-oct-2026', '',
     'Generado por `scripts/auditar_profundidad.py`. Mide forma (secciones, párrafos, tablas, enlaces) frente a los mínimos del prompt de investigación v5; no juzga el razonamiento.', '',
     '| Empresa | Palabras del artículo | Nivel 2 (caracteres) | Incumplimientos de forma |', '|---|---:|---:|---|']
for t, p, pal, n2, f in sorted(res):
    L.append(f"| {t} | {pal:,} | {n2:,} | {'; '.join(f) if f else '—'} |")
ok = sum(1 for r in res if not r[4])
L += ['', f'Sin incumplimientos de forma: {ok} de {len(res)}.']
open('auditorias/revision-2026-10-26/PROFUNDIDAD.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f'{ok} de {len(res)} sin incumplimientos')
for t, p, pal, n2, f in sorted(res): print(t, pal, n2, len(f), f[:2])
