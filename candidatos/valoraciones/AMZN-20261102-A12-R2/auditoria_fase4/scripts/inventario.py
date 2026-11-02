"""Inventario de celdas de entrada (no fórmula) de 4 pestañas exigidas por el prompt 3/3 §3, con nota de fuente.
Entrada = celda sin fórmula en la hoja R2 que en la maestra IA vigente tampoco es fórmula y no es rótulo de columna A."""
import sys, json, csv
sys.path[:0]=['.','scripts']
from jmr_valuation.io.sheets_auth import get_gspread_client
gc=get_gspread_client()
R2='1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI'; M='1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ'
TABS=['Input sheet','Cost of capital worksheet','Financials Multiples','Option value']
F='sheets(properties.title,data(startRow,startColumn,rowData(values(note,userEnteredValue,effectiveValue))))'
def grid(sid):
    r=gc.open_by_key(sid).fetch_sheet_metadata(params={'includeGridData':'true','ranges':[f"'{t}'!A1:N140" for t in TABS],'fields':F})
    out={}
    for s in r['sheets']:
        t=s['properties']['title']; cells={}
        for d in s.get('data',[]):
            for i,row in enumerate(d.get('rowData',[]) or []):
                for j,v in enumerate(row.get('values',[]) or []):
                    cells[(i,j)]=v
        out[t]=cells
    return out
def col(j): s='';j+=1
def a1(i,j):
    s='';j+=1
    while j: j,r=divmod(j-1,26); s=chr(65+r)+s
    return f'{s}{i+1}'
r2=grid(R2); m=grid(M)
rows=[]
for t in TABS:
    for (i,j),v in sorted(r2[t].items()):
        uev=v.get('userEnteredValue') or {}
        if not uev or 'formulaValue' in uev or j==0: continue
        mv=(m[t].get((i,j)) or {}).get('userEnteredValue') or {}
        if 'formulaValue' in mv: continue  # sería reemplazo de fórmula (lo cubre diff_formulas)
        val=list(uev.values())[0]
        if isinstance(val,str) and t!='Input sheet' and t!='Cost of capital worksheet': 
            if len(val)>40: continue
        if isinstance(val,str) and len(val)>60 and not v.get('note'): continue  # textos explicativos de la plantilla
        mval=list(mv.values())[0] if mv else None
        rows.append(dict(hoja=t,celda=a1(i,j),valor=val,valor_maestra=mval,cambiada=(val!=mval),nota=(v.get('note') or '').replace('\n',' ')[:300]))
w=csv.DictWriter(open(sys.argv[1],'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
ch=[r for r in rows if r['cambiada']]
print('celdas no-fórmula examinadas:',len(rows),'| distintas de la maestra (entradas diligenciadas):',len(ch),'| con nota de fuente:',sum(1 for r in ch if r['nota']),'| sin nota:',sum(1 for r in ch if not r['nota']))
by={}
for r in ch: by.setdefault(r['hoja'],[0,0]); by[r['hoja']][0]+=1; by[r['hoja']][1]+=bool(r['nota'])
print(by)
for r in ch:
    if not r['nota']: print('SIN NOTA', r['hoja'], r['celda'], str(r['valor'])[:60])
