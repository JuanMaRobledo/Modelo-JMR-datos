"""Matriz de sensibilidad como imagen-tabla, mismo estilo que las figuras fig-08/09/10 de los informes homologados."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
def fmt(x, d=0): return f'{x:,.{d}f}'.replace(',', '@').replace('.', ',').replace('@', '.')
def tabla(path, rows, cols, M, precio, centro=(2, 2), rfmt=lambda r: fmt(100*r, 2)+' %', cfmt=lambda c: fmt(100*c, 1)+' %', dec=0):
    nr, nc = len(rows), len(cols); W, H = 13.6, 0.45*(nr+1)
    fig = plt.figure(figsize=(W, H), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
    c0 = 2.6; cw = (W-c0)/nc; rh = 0.45
    ax.add_patch(plt.Rectangle((0, H-rh), W, rh, color='#5b8baa'))
    for j, c in enumerate(cols): ax.text(c0+(j+1)*cw-0.15, H-rh/2, cfmt(c), ha='right', va='center', color='white', fontweight='bold', fontsize=13, family='Liberation Sans')
    for i, r in enumerate(rows):
        y = H-rh*(i+2)
        ax.add_patch(plt.Rectangle((0, y), c0, rh, color='#f3f5f7')); ax.text(0.12, y+rh/2, rfmt(r), va='center', fontweight='bold', fontsize=13, color='#1d3449', family='Liberation Sans')
        for j in range(nc):
            v = M[i][j]; col = '#e6f0e7' if v >= 1.2*precio else ('#edf2f7' if v >= precio else '#f6e6e1')
            ax.add_patch(plt.Rectangle((c0+j*cw, y), cw, rh, color=col))
            ax.text(c0+(j+1)*cw-0.15, y+rh/2, fmt(v, dec), ha='right', va='center', fontsize=13, color='#1d3449', family='Liberation Sans', fontweight='bold' if (i, j) == centro else 'normal')
        ax.plot([0, W], [y, y], color='#dde3e8', lw=.8)
    ci, cj = centro; ax.add_patch(plt.Rectangle((c0+cj*cw+0.02, H-rh*(ci+2)+0.02), cw-0.04, rh-0.04, fill=False, ec='#1d3449', lw=1.8))
    fig.savefig(path, dpi=100); plt.close(fig)
