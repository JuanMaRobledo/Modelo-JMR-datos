#!/usr/bin/env python3
"""Captura de SOLO LECTURA de la hoja NU-20261102-A12-R1 (valores calculados + fórmulas) con hash SHA-256.
Salida: evidencia/captura-hoja-20261102/NU-20261102-A12-R1_resultados_hoja.json"""
import hashlib, json, os, sys, requests
sys.path[:0] = ['/home/user/JMR-valuation/scripts']
from nu_a12_fcfe import Hoja
SID = '1zKbHKOIei5vaWY0HYL5Gd1p7eeKDgQhlNhXJM1Pm9NI'; REV = 'NU-20261102-A12-R1'
H = Hoja(SID)
def rng(r, fr):
    return H.req('GET', H.b + '/values/' + requests.utils.quote(r), params={'valueRenderOption': fr}).get('values', [])
R = {'fcfe': "'NU FCFE'!A1:L140", 'sens': "'NU Sensibilidad'!A1:F75", 'mult': "'NU Múltiplos'!A1:I75",
     'input': "'Input sheet'!A1:D30"}
data = {k: rng(v, 'UNFORMATTED_VALUE') for k, v in R.items()}
forms = {k: rng(v, 'FORMULA') for k, v in R.items()}
nform = {k: sum(1 for row in forms[k] for x in row if isinstance(x, str) and x.startswith('=')) for k in forms}
meta = H.req('GET', H.b + '?fields=properties.title,sheets.properties.title')
out = {'revision_id': REV, 'sheet_id': SID, 'titulo': meta['properties']['title'], 'pestanas': len(meta['sheets']),
       'rangos': R, 'formulas_por_rango': nform, 'data': data, 'formulas': forms}
p = f'/home/user/Modelo-JMR-datos/evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json'
s = json.dumps(out, ensure_ascii=False, indent=1, default=str)
open(p, 'w').write(s)
print(p, hashlib.sha256(s.encode()).hexdigest(), nform, out['pestanas'])
