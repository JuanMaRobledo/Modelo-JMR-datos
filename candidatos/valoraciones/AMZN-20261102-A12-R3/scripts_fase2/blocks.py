from h import g
VO='Valuation output'
def block(top):  # top = fila 'Modelo ...'; offsets idénticos al bloque Base (fila 2)
    o=top-2; cols='CDEFGHIJKL'
    G=lambda a,r: g(VO,f'{a}{r+o}')
    return dict(rev0=G('B',5), gr=[G(c,4) for c in cols], mg=[G(c,6) for c in cols], tx=[G(c,8) for c in cols],
        sc=[G(c,40) for c in cols], wacc=[G(c,14) for c in cols], g=G('M',4), mg_t=G('M',6), tx_t=G('M',8),
        roic_t=G('M',42), wacc_t=G('M',14), debt=G('B',27), cash=G('B',29), nonop=G('B',30), minority=G('B',28),
        opt=G('B',32), shares=G('B',34), sheet_ps=G('B',35), prob=G('B',24))
