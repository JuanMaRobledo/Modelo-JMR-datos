#!/usr/bin/env python3
"""Auditoría de registro: contrasta cada valoración guardada y su análisis con modelo/REGLAS_VIGENTES.md (v10).

Solo usa lo que está en el repositorio. NO consulta la SEC, ni las hojas de Google, ni precios: por eso nunca emite VERIFICADO.
Uso: python3 scripts/auditar_registro.py [TICKER ...]   (sin argumentos: las empresas no colombianas de valoraciones/)
Escribe auditorias/revision-2026-10-26/<T>.md y resumen.json / resumen.md.
"""
import json, glob, re, sys, os, collections

SALIDA = 'auditorias/revision-2026-10-26'
COLOMBIA = {'GRUPOARGOS', 'GRUPOSURA', 'PFDAVVNDA', 'PFGRUPOARG', 'PFGRUPSURA'}
SIETE = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF', 'P/V', 'P/BV']
G_TERMINAL = 0.04
ALTA, MEDIA, BAJA = 'ALTA', 'MEDIA', 'BAJA'


def cerca(a, b, tol=1e-6):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) <= max(tol, abs(b) * 1e-9)


def cargar(ruta):
    with open(ruta, encoding='utf-8') as f:
        return json.load(f)


def nums(x):
    """Variantes de formato de una cifra para buscarla en el artículo."""
    v = round(x, 2)
    ent = f'{v:,.2f}'
    return {ent, ent.replace(',', 'X').replace('.', ',').replace('X', '.'), f'{v:.2f}', f'{v:.2f}'.replace('.', ','), f'{x:.1f}', f'{x:.1f}'.replace('.', ',')}


def clave(h):
    """Nombre corto de la historia: Base, Conservadora, Disrupción u Optimista (por id A/B/C/D si el nombre trae frase)."""
    return {'A': 'Base', 'B': 'Conservadora', 'C': 'Disrupción', 'D': 'Optimista'}.get(h.get('id'), h.get('nombre'))


def vector_pesos(r):
    return tuple(round(m.get('peso', 0), 3) for m in (r.get('metodos') or []))


def auditar(t, r, a, vectores):
    h = []  # (sev, regla, texto)
    def add(sev, regla, txt): h.append((sev, regla, txt))
    vp = r.get('valorPrincipal'); mos = r.get('mos'); pm = r.get('precioMOS'); precio = r.get('precio')
    ve = r.get('valorEsperado') or {}
    dm = r.get('descuentoMultiples') or {}

    # §1 valor principal y MOS
    if r.get('baseMOS') not in ('dcfBase', 'sotpBase'):
        add(ALTA, '§1', f"baseMOS = {r.get('baseMOS')!r}: el MOS debe ir sobre el DCF Base o el SOTP Base.")
    if mos != 0.35:
        add(ALTA, '§1', f'MOS = {mos}: la regla vigente es 35 % (registro del 19-oct con 25 %).')
    if isinstance(vp, (int, float)) and isinstance(pm, (int, float)) and isinstance(mos, (int, float)) and not cerca(pm, vp * (1 - mos)):
        add(ALTA, '§1', f'precioMOS {pm:.2f} no es valorPrincipal {vp:.2f} × (1 − {mos}).')
    base_hoy = (dm.get('dcfHoy') or {}).get('base')
    if base_hoy is not None and not cerca(base_hoy, vp, 1e-4):
        add(ALTA, '§1', f'DCF Base hoy del panel ({base_hoy:.2f}) ≠ valor principal ({vp:.2f}).')
    if r.get('metodoPrincipal') in (None, ''):
        add(ALTA, '§1', 'Sin método principal declarado.')

    # §2/§3 historias y probabilidades
    hs = ve.get('historias') or []
    if len(hs) != 4:
        add(ALTA, '§2', f'{len(hs)} historias en el registro; la regla pide 4.')
    else:
        ps = {clave(x): x.get('probabilidad') for x in hs}
        if abs(sum(v for v in ps.values() if v is not None) - 1) > 1e-6:
            add(ALTA, '§3', f'Las probabilidades suman {sum(v for v in ps.values() if v is not None):.4f}.')
        c, o = ps.get('Conservadora'), ps.get('Optimista')
        if c is not None and o is not None and abs(c - o) > 1e-6 and r.get('tipo') not in ('Declive',):
            add(MEDIA, '§3', f'Conservadora {c:.3f} ≠ Optimista {o:.3f}: la previa vigente es simétrica salvo en declive.')
        b = ps.get('Base')
        if b is not None and b < 0.40:
            add(MEDIA, '§3', f'Base con {b:.0%}: la previa mínima por etapa es 40 %.')
        # §4 crecimiento terminal
        gs = {clave(x): x.get('terminalGrowth') for x in hs}
        for n in ('Base', 'Conservadora', 'Optimista'):
            g = gs.get(n)
            if isinstance(g, (int, float)) and abs(g - G_TERMINAL) > 1e-9 and r.get('tipo') != 'Financiera':
                add(MEDIA, '§4', f'g terminal de {n} = {g:.2%}; la regla del 21-oct fija {G_TERMINAL:.0%} (con techo en la tasa libre).')
        # ordenar Cons ≤ Base ≤ Opt
        vals = {clave(x): x.get('valor') for x in hs}
        if all(isinstance(vals.get(n), (int, float)) for n in ('Conservadora', 'Base', 'Optimista')):
            if not (vals['Conservadora'] <= vals['Base'] <= vals['Optimista']):
                add(MEDIA, '§2', f"Orden de valores Conservadora {vals['Conservadora']:.2f} / Base {vals['Base']:.2f} / Optimista {vals['Optimista']:.2f} no es creciente.")
        if not cerca(vals.get('Base'), vp, 1e-4):
            add(ALTA, '§1', f"Valor de la historia Base ({vals.get('Base')}) ≠ valor principal ({vp}).")

    # §5A siete métodos y pesos
    nombres = [m.get('nombre') for m in (dm.get('metodos') or [])]
    faltan = [m for m in SIETE if m not in nombres and not (m == 'P/V' and 'P/S' in nombres)]
    if faltan:
        add(ALTA, '§5A', f"Faltan métodos en el panel: {', '.join(faltan)}.")
    ms = r.get('metodos') or []
    pesos = [m.get('peso', 0) for m in ms]
    if ms and abs(sum(pesos) - 1) > 1e-6:
        add(ALTA, '§5A', f'Los pesos de los métodos suman {sum(pesos):.4f}.')
    v = vector_pesos(r)
    if v and vectores[v] >= 5:
        add(ALTA, '§5A', f'Vector de pesos {v[:6]} idéntico en {vectores[v]} de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método.')
    if isinstance(dm.get('pesoDcf'), (int, float)) and abs(dm.get('pesoDcf', 0) + dm.get('pesoMultiplos', 0) - 1) > 1e-6:
        add(ALTA, '§5A', 'pesoDcf + pesoMultiplos ≠ 1.')
    for m in dm.get('metodos') or []:
        for esc in ('conservador', 'base', 'optimista'):
            ch = (m.get(esc) or {}).get('chequeo')
            if ch not in (None, 'OK'):
                add(MEDIA, '§5A', f"Método {m.get('nombre')} / {esc}: chequeo = {ch}.")

    # sanidad económica
    cg = r.get('cagr') or {}
    if cg and all(isinstance(x, (int, float)) and x < 0 for x in cg.values()):
        add(MEDIA, '§5', f'CAGR implícito negativo en los tres escenarios ({", ".join(f"{k} {x:.1%}" for k, x in cg.items())}): el precio exige más de lo que descuenta cualquiera.')
    if isinstance(precio, (int, float)) and isinstance(vp, (int, float)) and vp > 0:
        ratio = precio / vp
        if ratio > 1.5 or ratio < 0.67:
            add(MEDIA, '§8', f'Precio {precio:.2f} frente a Base {vp:.2f} (×{ratio:.2f}): diferencia grande que el informe debe explicar sin tocar la Base.')

    # estado de la publicación
    cp = r.get('controlPublicacion') or {}
    au = r.get('auditoria') or {}
    est = str(au.get('estado') or '')
    if 'salvedad' in est.lower() or 'no certific' in est.lower():
        add(MEDIA, '§8', f'Estado heredado: «{est[:90]}». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE.')
    if cp.get('comparablesValidados') is False:
        add(MEDIA, '§5', 'Comparables sin validar (comparablesValidados = false).')
    if cp.get('verificacionVisual') == 'PENDIENTE':
        add(BAJA, '§6', 'Verificación visual pendiente.')
    fuente = str(r.get('precioReferenciaFuente') or '')
    m = re.search(r'(\d{1,2})-(\w{3})-(\d{4})', fuente)
    if m:
        add(BAJA, '§4', f'Precio de referencia del {m.group(0)}; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común.')

    # análisis enlazado
    if a is None:
        add(ALTA, '§9', 'No hay análisis fundamental restaurado para este ticker.')
    else:
        art = a.get('articleHtml') or ''
        h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', art, re.S)
        num = [x for x in (re.sub('<[^>]+>', '', t_).strip() for t_ in h2) if re.match(r'\d{1,2}\.\s', x)]
        if len(num) != 18:
            add(ALTA, '§9', f'El artículo tiene {len(num)} secciones numeradas; la regla pide 18.')
        if not (a.get('calculationHtml') or '') and not a.get('nivel2'):
            add(MEDIA, '§9', 'Sin nivel 2 (calculationHtml) separado.')
        if not (a.get('linkedValuation') or {}).get('sourcePath'):
            add(MEDIA, '§10', 'El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza.')
        if isinstance(vp, (int, float)):
            plano = re.sub('<[^>]+>', ' ', art + ' ' + (a.get('calculationHtml') or ''))
            if not any(n in plano for n in nums(vp)):
                add(ALTA, '§9', f'La cifra del valor principal ({vp:.2f}) no aparece en el artículo ni en el nivel 2.')
        if 'Valor intrínseco base' not in art[:6000] and 'Valor intrínseco base' not in (a.get('articleHtml') or '')[:20000]:
            add(BAJA, '§9', 'Falta el recuadro inicial «Valor intrínseco base:».')
    return h


def main(argv):
    vals = {}
    for p in sorted(glob.glob('valoraciones/*.json')):
        r = cargar(p)
        if r.get('ticker') in COLOMBIA:
            continue
        vals[r['ticker']] = (p, r)
    analisis = {}
    for p in sorted(glob.glob('analisis/*.json')):
        a = cargar(p)
        analisis[a.get('ticker')] = (p, a)
    tickers = argv or sorted(vals)
    vectores = collections.Counter(vector_pesos(r) for _, r in vals.values())
    os.makedirs(SALIDA, exist_ok=True)
    resumen = []
    for t in tickers:
        p, r = vals[t]
        pa, a = analisis.get(t, (None, None))
        h = auditar(t, r, a, vectores)
        altas = [x for x in h if x[0] == ALTA]
        estado = 'PENDIENTE' if altas else 'SIN ALTAS · fuentes sin verificar' if any(x[0] == MEDIA for x in h) else 'SIN HALLAZGOS · fuentes sin verificar'
        resumen.append({'ticker': t, 'registro': p, 'analisis': pa, 'estado_preliminar': estado, 'alta': len(altas),
                        'media': sum(x[0] == MEDIA for x in h), 'baja': sum(x[0] == BAJA for x in h),
                        'hallazgos': [{'sev': s, 'regla': g, 'texto': x} for s, g, x in h]})
        with open(f'{SALIDA}/{t}.md', 'w', encoding='utf-8') as f:
            f.write(f'# Auditoría de registro · {t} · 26-oct-2026\n\n')
            f.write(f"- Registro: `{p}` ({r.get('nombreActivo')}, {r.get('fecha')})\n- Análisis: `{pa}`\n")
            f.write(f"- Valor principal: {r.get('valorPrincipal')} · precio {r.get('precio')} · MOS {r.get('mos')} · precio con MOS {r.get('precioMOS')}\n")
            f.write(f'- **Estado preliminar: {estado}**\n\n')
            f.write('**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.\n\n')
            if not h:
                f.write('Sin hallazgos en lo que el registro permite comprobar.\n')
            else:
                f.write('| Prioridad | Regla | Hallazgo |\n|---|---|---|\n')
                for s, g, x in sorted(h, key=lambda z: [ALTA, MEDIA, BAJA].index(z[0])):
                    f.write(f'| {s} | {g} | {x} |\n')
            f.write('\n**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.\n')
    with open(f'{SALIDA}/resumen.json', 'w', encoding='utf-8') as f:
        json.dump({'fecha': '2026-10-26', 'reglas': 'REGLAS_VIGENTES v10', 'empresas': resumen}, f, ensure_ascii=False, indent=1)
    cnt = collections.Counter(x['estado_preliminar'] for x in resumen)
    print(len(resumen), 'empresas;', dict(cnt))
    reglas = collections.Counter((s['sev'], s['regla'], re.sub(r'[\d.,%]+', '#', s['texto'])[:70]) for x in resumen for s in x['hallazgos'])
    for k, v in reglas.most_common(14): print(v, k)


if __name__ == '__main__':
    main(sys.argv[1:])
