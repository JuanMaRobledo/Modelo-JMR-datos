#!/usr/bin/env python3
"""Quita las claves `posicion` (acciones, costo promedio, compras) de los registros JSON.

Este repositorio es público y su README excluye las posiciones de cartera. Las posiciones viven en la app
Cartera; el visor las lee de allí. Uso: python3 scripts/quitar_posicion.py [--aplicar] [carpetas...]
Sin --aplicar solo informa. Conserva el formato de cada archivo (sangría y orden de claves).
"""
import json, sys, pathlib

def limpiar(o):
    n = 0
    if isinstance(o, dict):
        if 'posicion' in o:
            del o['posicion']; n += 1
        for v in o.values(): n += limpiar(v)
    elif isinstance(o, list):
        for v in o: n += limpiar(v)
    return n

def serializar(d, texto):
    sangria = 1 if texto.startswith('{\n ') and not texto.startswith('{\n  ') else (2 if texto.startswith('{\n  ') else None)
    return json.dumps(d, ensure_ascii=False, indent=sangria, separators=(',', ': ') if sangria else (',', ':')) + ('\n' if texto.endswith('\n') else '')

def main(argv):
    aplicar = '--aplicar' in argv
    carpetas = [a for a in argv if not a.startswith('--')] or ['valoraciones', 'analisis', 'archivo']
    total = archivos = 0
    omitidos = []
    for c in carpetas:
        for p in sorted(pathlib.Path(c).rglob('*.json')):
            texto = p.read_text(encoding='utf-8')
            if '"posicion"' not in texto: continue
            d = json.loads(texto)
            if serializar(d, texto) != texto:  # el formato no se reproduce byte a byte: no se toca
                omitidos.append(str(p)); continue
            n = limpiar(d)
            if not n: continue
            archivos += 1; total += n
            if aplicar: p.write_text(serializar(d, texto), encoding='utf-8')
    print(('Aplicado' if aplicar else 'En seco') + f': {total} bloques `posicion` en {archivos} archivos')
    for o in omitidos: print('OMITIDO (formato no reproducible, revisar a mano):', o)

if __name__ == '__main__':
    main(sys.argv[1:])
