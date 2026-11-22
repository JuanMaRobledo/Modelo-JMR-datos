"""Helpers para la revisión S/C Damodaran (22-nov-2026)."""
import json, re, copy, pathlib, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/gen')
from figtabla import tabla
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
W = pathlib.Path('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/sc6')
IMG = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2/imagenes')
RAW = 'https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/'
def n(v, d=2): return f'{v:,.{d}f}'.replace(',', '@').replace('.', ',').replace('@', '.')
def pc(x, d=1, sign=True):
    s = n(100*x, d) + ' %'
    return ('+' + s if x >= 0 else s.replace('-', '−' if False else '-')) if sign else s
def load(t):
    return json.load(open(W/'origen/empresas'/f'{t}.json')), json.load(open(W/'origen/analisis'/f'{t}.json'))
def save(t, e, a):
    json.dump(e, open(W/'origen/empresas'/f'{t}.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(a, open(W/'origen/analisis'/f'{t}.json', 'w'), ensure_ascii=False, indent=1)
class Rep:
    """Reemplazos verificados: cada (old,new) debe aparecer en algún bloque (o exactamente `cnt` veces)."""
    def __init__(s, blocks): s.b = blocks; s.log = []
    def __call__(s, old, new, cnt=None, keys=None, regex=False):
        tot = 0
        for k in (keys or list(s.b)):
            v = s.b[k]
            if not isinstance(v, str): continue
            if regex: v2, c = re.subn(old, lambda m: new, v)
            else: c = v.count(old); v2 = v.replace(old, new)
            s.b[k] = v2; tot += c
        if tot == 0 or (cnt is not None and tot != cnt): raise SystemExit(f'Reemplazo {old[:80]!r}: {tot} (esperado {cnt or ">0"})')
        s.log.append((old[:60], tot)); return tot
def cortar_just(blocks):
    for k in blocks:
        v = blocks[k]
        if isinstance(v, str):
            i = v.find('<div id="justificacion-supuestos'); blocks[k] = v if i < 0 else v[:i]
def barras(path, items, cur, pie):
    """items: [(etiqueta, valor, tipo)] tipo in opt|base|precio|cons|estres. Estilo de las figuras de destrucción."""
    col = {'opt': '#4c8c6a', 'base': '#1f3a56', 'precio': '#8a959e', 'cons': '#a85c3c', 'estres': '#c9a27e', 'mos': '#5b8baa'}
    fig, ax = plt.subplots(figsize=(13.6, 0.5*len(items)+1.0), dpi=100)
    lab = [x[0] for x in items][::-1]; val = [x[1] for x in items][::-1]; c = [col[x[2]] for x in items][::-1]
    ax.barh(lab, val, color=c, height=0.65)
    mx = max(val)
    for i, v in enumerate(val): ax.text(v + mx*0.01, i, f'{cur}{n(v, 0)}', va='center', fontweight='bold', color='#1d3449', fontsize=13, family='Liberation Sans')
    ax.set_xlim(0, mx*1.12); ax.axis('off')
    for i, l in enumerate(lab): ax.text(-mx*0.012, i, l, ha='right', va='center', fontsize=13, color='#1d3449', family='Liberation Sans')
    fig.text(0.5, 0.02, pie, ha='center', color='#8a959e', fontsize=12, family='Liberation Sans')
    fig.subplots_adjust(left=0.27, right=0.97, top=0.97, bottom=0.12); fig.savefig(path, dpi=100); plt.close(fig)
def grid_png(t, name, g, precio, rfmt, cfmt):
    p = IMG/t/name; tabla(p, g['rows'], g['cols'], g['m'], precio, rfmt=rfmt, cfmt=cfmt); return p
def expediente(e, t, rev, sheet, calc, anclas, nota, extra_libro=None, just_sc=None, warn=None):
    ant = e['revision']['id'] if isinstance(e['revision'], dict) else e['revision']
    for s, A in calc['assumptions'].items():
        for k in ('salesToCapital1to5', 'salesToCapital6to10', 'waccInitial'): e['assumptions'][s][k] = A[k]
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/edit'
    L = e['libro']; L_old = {k: L.get(k) for k in ('id', 'url', 'valores', 'sha256')}
    L.update({'id': f'{rev}_VALORACION', 'url': url, 'googleSheetId': sheet, 'formatoPrincipal': 'google_sheets', 'valores': dict(calc['esc']), 'contratoVersion': '1.5.6',
              'anclasVentasCapital': anclas, 'revisionAnterior': {'id': ant, **L_old},
              'cambios': nota})
    if isinstance(L.get('googleSheets'), dict): L['googleSheets'] = {**L['googleSheets'], 'id': sheet, 'url': url}
    if extra_libro: L.update(extra_libro)
    dl = e.get('documentLinks') or {}
    e['documentLinks'] = {**dl, 'workbook': url, 'workbookGoogleSheets': url, 'workbookAnterior': L_old['url']}
    hist = (e['revision'].get('historial') if isinstance(e['revision'], dict) else None) or {}
    hist = {**hist, ant: {k: v for k, v in (L_old['valores'] or {}).items()}}
    e['revision'] = {'id': rev, 'anterior': ant, 'historial': hist, 'nota': nota}
    if just_sc:
        e.setdefault('justificaciones', {})['salesToCapital1to5'] = just_sc; e['justificaciones']['salesToCapital6to10'] = just_sc
    e['warnings'] = [w for w in e.get('warnings', []) if 'ventas/capital' not in w.lower() or 'Corrección pendiente' not in w] + ([warn] if warn else [])
    e['estado'] = 'EN_REVISION'
    return e
# ---------- estilo de los informes GOOGL/AMZN/ONON (matplotlib por defecto, paleta azul) ----------
NAVY, GREY, TAN, STEEL = '#1d3449', '#7d8790', '#c4a282', '#5b8baa'
def _sty(ax):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'): ax.spines[s].set_color('#5d6b78')
def vvp(path, V, mos, px, plabel, xlabel='USD por acción', dec=2):
    lab = ['Conservador', 'Base', 'Optimista', 'Precio con MOS 35 % (Base)']; val = [V['conservador'], V['base'], V['optimista'], mos]
    fig, ax = plt.subplots(figsize=(8.2, 3.1), dpi=150); y = range(len(lab))[::-1]
    ax.barh(list(y), val, color=[GREY, NAVY, TAN, STEEL], height=0.55)
    for yy, v in zip(y, val): ax.text(v + max(val)*0.01, yy, n(v, dec), va='center', fontsize=9)
    ax.axvline(px, color='#222', ls='--', lw=1.1); ax.text(px + max(val)*0.01, -0.62, plabel, fontsize=8.5, va='bottom')
    ax.set_yticks(list(y)); ax.set_yticklabels(lab, fontsize=10); ax.set_xlabel(xlabel); ax.set_xlim(0, max(val + [px])*1.16); _sty(ax)
    fig.tight_layout(); fig.savefig(path); plt.close(fig)
def heat(ax, M, rl, cl, title, xl, yl, center=(2, 2), dec=0):
    import numpy as np
    M = np.array(M, float); ax.imshow(M, cmap='Blues', aspect='auto', vmin=M.min()*0.9, vmax=M.max()*1.05)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, n(M[i, j], dec), ha='center', va='center', fontsize=9.5, color='white' if M[i, j] > M.min() + 0.75*(M.max()-M.min()) else '#1d3449', fontweight='bold' if (i, j) == center else 'normal')
    ax.set_xticks(range(len(cl))); ax.set_xticklabels(cl, fontsize=8.5); ax.set_yticks(range(len(rl))); ax.set_yticklabels(rl, fontsize=8.5)
    ax.set_title(title, fontsize=10.5); ax.set_xlabel(xl, fontsize=9.5); ax.set_ylabel(yl, fontsize=9.5)
    for s in ax.spines.values(): s.set_visible(False)
def heat2(path, A, Bm, dec=0):
    fig, axs = plt.subplots(1, 2, figsize=(8.4, 3.5), dpi=150)
    for ax, g in zip(axs, (A, Bm)): heat(ax, g['m'], g['rl'], g['cl'], g['title'], g['xl'], g['yl'], g.get('center', (2, 2)), dec)
    fig.tight_layout(); fig.savefig(path); plt.close(fig)
def estres_fig(path, items, px, base, plabel, blabel, xlabel='USD por acción (ilustrativo, no oficial)', dec=1):
    fig, ax = plt.subplots(figsize=(6.2, 0.42*len(items)+1.3), dpi=150); y = list(range(len(items)))[::-1]
    ax.barh(y, [v for _, v, _ in items], color=[TAN if hi else GREY for _, _, hi in items], height=0.62)
    mx = max([v for _, v, _ in items] + [px, base])
    for yy, (_, v, _) in zip(y, items): ax.text(v + mx*0.006, yy, n(v, dec), va='center', fontsize=10)
    ax.axvline(px, color='#222', ls='--', lw=1.1); ax.axvline(base, color=NAVY, lw=1.6)
    ax.text(px, len(items) - 0.45, plabel, ha='right', fontsize=9, color='#333'); ax.text(base + mx*0.006, -0.7, blabel, fontsize=9, color=NAVY)
    ax.set_yticks(y); ax.set_yticklabels([l for l, _, _ in items], fontsize=9.5); ax.set_xlabel(xlabel); ax.set_xlim(0, mx*1.16); _sty(ax)
    fig.tight_layout(); fig.savefig(path); plt.close(fig)
def html_table(corner, rl, cl, M, dec=2, fmt=None):
    f = fmt or (lambda v: n(v, dec))
    h = '<table><thead><tr><th class="">%s</th>' % corner + ''.join('<th class="num">%s</th>' % c for c in cl) + '</tr></thead><tbody>'
    for r_, row in zip(rl, M): h += '<tr><td class="">%s</td>' % r_ + ''.join('<td class="num">%s</td>' % f(v) for v in row) + '</tr>'
    return h + '</tbody></table>'
def swap_table(B, key, marker, new):
    v = B[key]; i = v.find(marker); assert i >= 0, marker
    j = v.rfind('<table', 0, i); k = v.find('</table>', i) + len('</table>'); B[key] = v[:j] + new + v[k:]
def swap_row(B, key, label, vals, cnt=1):
    """Sustituye las celdas de la fila cuya primera celda empieza por `label` (tantas celdas como `vals`, desde la segunda)."""
    v = B[key]; hits = 0; pos = 0
    while True:
        i = v.find('>' + label, pos)
        if i < 0: break
        a = v.rfind('<tr', 0, i); b = v.find('</tr>', i)
        row = v[a:b]; cells = re.findall(r'(<t[dh][^>]*>)(.*?)(</t[dh]>)', row)
        assert len(cells) == len(vals) + 1, (label, len(cells), len(vals))
        new = row[:row.find('>', row.find('<tr')) + 1] + cells[0][0] + cells[0][1] + cells[0][2] + ''.join(o + str(x) + c for (o, _, c), x in zip(cells[1:], vals))
        v = v[:a] + new + v[b:]; hits += 1; pos = a + len(new)
    assert hits == cnt, (label, hits); B[key] = v
YEARS = json.load(open(W/'years.json'))
