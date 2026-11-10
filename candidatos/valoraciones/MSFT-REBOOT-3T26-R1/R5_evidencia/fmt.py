def f(x,d=0):
    if x is None: return 'N/D'
    s=f'{abs(x):,.{d}f}'.replace(',','§').replace('.',',').replace('§','.')
    return ('−' if x<0 and float(s.replace('.','').replace(',','.'))!=0 else '')+s
def p(x,d=1): return 'N/D' if x is None else f(x*100,d)+' %'
def usd(x,d=2): return 'US$'+f(x,d)
def table(head,rows,cls=''):
    h=''.join(f'<th>{c}</th>' for c in head)
    b=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<table{cls}><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def P(t): return f'<p>{t}</p>'
def H3(t): return f'<h3>{t}</h3>'
def UL(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
