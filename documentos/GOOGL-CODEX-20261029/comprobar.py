#!/usr/bin/env python3
"""Diagnóstico de capturas nativas. No valora de nuevo ni escribe en Sheets.

Ejecutar: python3 documentos/GOOGL-CODEX-20261029/comprobar.py
Las salidas de fórmulas son evidencia capturada, no recálculo nativo.
"""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def col(n):
    out = ''
    while n:
        n, rem = divmod(n - 1, 26)
        out = chr(65 + rem) + out
    return out


def capture(name):
    raw = json.loads((ROOT / 'evidencia' / name).read_text())
    cells = {}
    for sheet in raw['sheets']:
        tab = sheet['properties']['title']
        for block in sheet.get('data', []):
            for r, row in enumerate(block.get('rowData', []), block.get('startRow', 0) + 1):
                for c, cell in enumerate(row.get('values', []), block.get('startColumn', 0) + 1):
                    cells[f'{tab}!{col(c)}{r}'] = cell
    return raw, cells


def value(cells, addr):
    v = cells[addr].get('effectiveValue', {})
    if len(v) != 1 or 'errorValue' in v:
        raise ValueError(f'No value: {addr}: {v}')
    return next(iter(v.values()))


def vector(cells, tab, row):
    return [value(cells, f'{tab}!{c}{row}') for c in 'CDEFGHIJKL']


def close(a, b, atol=1e-6):
    return math.isclose(a, b, rel_tol=1e-11, abs_tol=atol)


def run():
    _, r = capture('r5-cells.json')
    _, more = capture('r5more.json')
    r.update(more)
    _, t = capture('template.json')
    _, az = capture('az.json')
    _, terminal = capture('az-terminal.json')
    az.update(terminal)
    results = []

    def check(name, ok, detail):
        results.append({'control': name, 'estado': 'APROBADO' if ok else 'FALLIDO', 'detalle': detail})

    shares = value(r, 'Valuation output!B34')
    fcff = vector(r, 'Valuation output', 11)
    wacc = vector(r, 'Valuation output', 14)
    df = 1.0
    pv = 0.0
    for cash, rate in zip(fcff, wacc):
        df /= 1 + rate
        pv += cash * df
    g = value(r, 'Valuation output!M4')
    wt = value(r, 'Valuation output!M14')
    terminal_pv = value(r, 'Valuation output!M11') / (wt - g) * df
    equity_bridge = (value(r, 'Valuation output!B29') + value(r, 'Valuation output!B30')
                     - value(r, 'Valuation output!B27') - value(r, 'Valuation output!B28')
                     - value(r, 'Valuation output!B32') - value(r, 'Input sheet!B76'))
    replay = (pv + terminal_pv + equity_bridge) / shares
    check('R5 aritmética desde FCFF capturados', close(replay, value(r, 'Valuation output!B35')),
          {'replay': replay, 'hoja': value(r, 'Valuation output!B35'), 'MOS35': replay * .65,
           'VP_explicito_USDm': pv, 'VP_terminal_USDm': terminal_pv,
           'puente_equity_USDm': equity_bridge, 'acciones_millones': shares,
           'alcance': 'No reproduce inputs ni recalcula fórmulas en copia oficial.'})
    check('R5 FCFF = NOPAT menos reinversión, 10 años',
          all(close(value(r, f'Valuation output!{c}11'), value(r, f'Valuation output!{c}9') - value(r, f'Valuation output!{c}10')) for c in 'CDEFGHIJKL'),
          'Identidad aritmética de valores capturados; no certifica clasificación económica.')
    check('R5 reinversión física más I+D neta, 10 años',
          all(close(value(r, f'Valuation output!{c}10'), value(r, f'Puente CAPEX ROIC!{c}36') + value(r, f'Puente CAPEX ROIC!{c}34')) for c in 'CDEFGHIJKL'),
          'S/C no se suma a esta reinversión. No prueba ausencia de solapamiento en gastos de origen.')
    differences = []
    replaced = []
    validations = []
    for addr, cell in t.items():
        if addr not in r:
            continue
        original = cell.get('userEnteredValue', {})
        observed = r[addr].get('userEnteredValue', {})
        if 'formulaValue' in original and original != observed:
            differences.append({'celda': addr, 'plantilla': original, 'R5': observed})
            if 'formulaValue' not in observed:
                replaced.append(addr)
        if cell.get('dataValidation') != r[addr].get('dataValidation'):
            validations.append(addr)
    check('Fórmulas R5 conservadas vs plantilla, solo rangos capturados', not differences,
          {'diferencias': len(differences), 'formulas_sustituidas_por_literal_o_vacio': replaced,
           'inventario': 'evidencia/diferencias-formulas.json', 'cobertura': 'Parcial, no todas las 48 pestañas.'})
    check('Validaciones R5 vs plantilla en celdas comunes capturadas', not validations, validations)
    check('Fracción I+D uniforme explícito-terminal',
          'Cohortes IA 2026' in r['Puente CAPEX ROIC!M32']['userEnteredValue'].get('formulaValue', ''),
          {'C32': r['Puente CAPEX ROIC!C32']['userEnteredValue'],
           'L32': r['Puente CAPEX ROIC!L32']['userEnteredValue'],
           'M32': r['Puente CAPEX ROIC!M32']['userEnteredValue'],
           'hallazgo': 'C:L multiplican por 85%; M no. Cambio no explicado de base contable.'})
    # Impacto local y aislado del factor omitido, sin alterar la hoja o su resultado publicado.
    rd_terminal = value(r, 'Puente CAPEX ROIC!M32')
    delta_nopat = rd_terminal * (.85 - 1) * value(r, 'Valuation output!M8')
    roic = value(r, 'Valuation output!M42')
    delta_price = delta_nopat * (1 - g / roic) / (wt - g) * df / shares
    check('WACC terminal > g y ROIC terminal > g R5', wt > g and roic > g,
          {'wacc_terminal': wt, 'g': g, 'roic_terminal': roic})
    # Replay de AZ: entradas de SU hoja, sin importar supuestos JMR.
    az_results = {}
    for label, growrow, marginrow, darow, caprow, nwcrow, growcell, roiccell, outrow, modelstart in [
        ('Base', 42, 44, 45, 46, 47, 'C48', 'C83', 10, 34),
        ('Conservador', 54, 56, 57, 58, 59, 'C60', 'C85', 11, 59),
        ('Optimista', 30, 32, 33, 34, 35, 'C36', 'C86', 9, 9),
    ]:
        rev = value(az, 'Inputs!C9')
        nwc = rev * value(az, 'Inputs!C25')
        rate = value(az, 'Inputs!C21')
        tax = value(az, 'Inputs!C20')
        pvaz = 0.0
        maxflowerror = 0.0
        for i, c in enumerate('CDEFGHIJKL', 1):
            rev *= 1 + value(az, f'Inputs!{c}{growrow}')
            nopat = rev * value(az, f'Inputs!{c}{marginrow}') * (1 - tax)
            nextnwc = rev * value(az, f'Inputs!{c}{nwcrow}')
            cash = nopat + rev * value(az, f'Inputs!{c}{darow}') - rev * value(az, f'Inputs!{c}{caprow}') - (nextnwc - nwc)
            nwc = nextnwc
            pvaz += cash / (1 + rate) ** i
            maxflowerror = max(maxflowerror, abs(cash - value(az, f'Model!{c}{modelstart+13}')))
        gaz = value(az, f'Inputs!{growcell}')
        rocaz = value(az, f'Inputs!{roiccell}')
        tv = nopat * (1 + gaz) * (1 - gaz / rocaz) / (rate - gaz)
        price = (pvaz + tv / (1 + rate) ** 10 - value(az, 'Inputs!C10')) / value(az, 'Inputs!C11')
        target = value(az, f'Outputs!E{outrow}')
        az_results[label] = {'replay': price, 'hoja': target, 'error_max_FCFF_USDm': maxflowerror,
                             'MOS35_comparativo': .65 * price}
        check(f'AZ {label}: FCFF desde sus entradas y perpetuidad', close(price, target) and maxflowerror < 1e-6,
              az_results[label])
    check('AZ WACC desde sus componentes',
          close((value(az, 'Inputs!C15') + value(az, 'Inputs!C16') * value(az, 'Inputs!C17')) * (1-value(az, 'Inputs!C19')) + value(az, 'Inputs!C18') * (1-value(az, 'Inputs!C20')) * value(az, 'Inputs!C19'), value(az, 'Inputs!C21')),
          {'WACC': value(az, 'Inputs!C21'), 'alcance': 'Identidad, no validación de Rf/ERP/beta/pesos.'})
    check('Comparación: mismo puente EV-equity', close(equity_bridge, -value(az, 'Inputs!C10')),
          {'R5': equity_bridge, 'AZ': -value(az, 'Inputs!C10')})
    for name, reason in [
        ('Reproducción R5 desde copia oficial de 46 pestañas', 'NO EJECUTADA: R5 no conserva el motor; no se copiaron modificaciones.'),
        ('Nueva valoración JMR independiente A-1.2', 'PENDIENTE: no se han completado datos, fichas de calibración ni cuatro DCF nativos.'),
        ('Nueva valoración AZ independiente', 'PENDIENTE: el replay usa hipótesis AZ existentes, no hipótesis nuevas.'),
        ('18 secciones de research completo', 'PENDIENTE: informe de hallazgos no sustituye research completo.'),
        ('Siete múltiplos, DCF inverso y sensibilidades nuevas', 'NO EJECUTADOS.'),
        ('Integridad global, perfil 46, selectores y regresión nativa', 'NO EJECUTADOS integralmente; comparación acotada arriba.'),
        ('Trazabilidad primaria de todos los datos históricos/LTM', 'PENDIENTE: historia heredada no validada línea a línea contra SEC.'),
    ]:
        results.append({'control': name, 'estado': 'NO_EJECUTADO', 'detalle': reason})
    output = {'revision_id': 'GOOGL-CODEX-20261029', 'fecha_corte_informacion': '2026-10-29',
              'estado': 'PENDIENTE_NO_PUBLICADO', 'controles': results,
              'diagnostico_factor_RD_terminal': {'delta_USD_accion_aislado': delta_price,
                'valor_diagnostico_no_oficial': replay + delta_price,
                'limitacion': 'Solo aplica 85% a M32 y propaga escudo fiscal/retención terminal manteniendo resto fijo. No recalibra cohortes, GAAP ni ROIC.'},
              'replay_R5': replay, 'replay_AZ_existente': az_results}
    (ROOT / 'evidencia' / 'diferencias-formulas.json').write_text(json.dumps(differences, ensure_ascii=False, indent=2)+'\n')
    (ROOT / 'resultados-controles.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'evidencia').glob('*.json'))}
    (ROOT / 'manifest-sha256.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return output


if __name__ == '__main__':
    run()
