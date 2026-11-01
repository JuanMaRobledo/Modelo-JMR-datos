#!/usr/bin/env python3
"""Import native FY/VP rows only; validate identity, formulas, DCF and matrix centers."""
import copy
import hashlib
import json
import math
from pathlib import Path

METHODS = ['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
SCENARIOS = [('conservador',10),('base',19),('optimista',28)]

def numeric(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)

def close(a,b,tol=1e-6):
    return numeric(a) and numeric(b) and abs(a-b)<=max(tol,abs(b)*1e-8)

def integrate(v, capture, formulas, raw_hash):
    before=copy.deepcopy(v)
    for c in (capture,formulas):
        assert c['ticker']==v['ticker'] and c['revisionId']==v['revisionId']
        assert c['sourceSheetId']==v['sheet_id'] and c['range']=="'Descuento de múltiplos'!A1:M80"
    rows, frows = capture['values'],formulas['values']
    assert len(rows)>=52 and len(frows)>=52
    assert close(rows[37][3],v['valorPrincipal']), 'DCF changed: new review required'
    assert numeric(rows[4][1]) and rows[4][1]>-1
    assert rows[5][1] in ('Promedio 1-3 años','Solo 3 años')
    centers={m['metodo']:m['vp3Original'] for m in v['sensibilidadMultiples']['matrices'] if m['escenario']=='base' and m['estado']=='OK'}
    methods=[]
    weights_ready=numeric(rows[37][1]) and close(rows[37][1]+rows[38][1],1)
    scenarios_ready=all(len(rows[start+n])>=11 for _,start in SCENARIOS for n in range(5))
    complete_weights=weights_ready and scenarios_ready
    for n,name in enumerate(METHODS):
        method={'nombre':name,'peso':rows[19+n][1], 'pesoRelativo':rows[19+n][2],
                'estado':'CALCULADO_NATIVO_EN_REVISION' if complete_weights else 'CONTRASTE_SIN_CONSOLIDACION'}
        for scenario,start in SCENARIOS:
            row, frow=rows[start+n],frows[start+n]
            assert row[0]==name
            if len(row)==3 and scenario!='base' and not scenarios_ready:
                method[scenario]=None
                continue
            assert len(row)>=11
            assert all(numeric(row[i]) for i in range(1,10)), (name,scenario,'incomplete')
            assert row[10]=='OK', (name,scenario,'native control')
            assert all(isinstance(frow[i],str) and frow[i].startswith('=') for i in range(3,10)), 'formula missing'
            method[scenario]={'fy':row[3:6],'vp':row[6:9],'consolidado':row[9],'chequeo':row[10],
                              'origen':f"'Descuento de múltiplos'!D{start+n+1}:K{start+n+1}"}
            # The arithmetic comparison validates; no computed value is exported.
            expected=row[8] if rows[5][1]=='Solo 3 años' else sum(row[6:9])/3
            assert close(expected,row[9])
        assert name in centers and close(method['base']['vp'][2],centers[name]), 'matrix center does not match source'
        methods.append(method)
    d=copy.deepcopy(v.get('descuentoMultiples') or {})
    d['metodos']=methods
    d['integracionNativa']={'revisionId':v['revisionId'],'sourceSheetId':v['sheet_id'],
       'rango':"'Descuento de múltiplos'!A1:M80",'capturaSha256':raw_hash,
       'fechaCaptura':capture.get('fechaCaptura','2026-10-31'),'estado':'METODOS_Y_CONSOLIDACION_CONCILIADOS' if complete_weights else 'METODOS_BASE_CONCILIADOS_ESCENARIOS_Y_PONDERACION_PENDIENTE',
       'certificadoEconomico':False,'calculosExternosExportados':False,
       'motivoPendiente':None if complete_weights else 'Faltan resultados conservador/optimista y/o ponderaciones nativas. No se interpreta el ponderado cero como valor ni se inventan datos. Consultar la fotografía fuente.'}
    if complete_weights:
        summary={key:{scenario:rows[row][col] for scenario,col in [('conservador',2),('base',3),('optimista',4)]}
                 for key,row in [('dcfHoy',37),('multiplesHoy',38),('ponderadoHoy',39)]}
        assert all(numeric(x) for values in summary.values() for x in values.values())
        # Preserve existing summary precision and decisions; only fill missing fields.
        for key,val in summary.items():
            if isinstance(d.get(key),dict):
                assert all(d[key].get(s) is None or close(d[key][s],x,0.02) for s,x in val.items()), ('summary conflict',key)
            else:
                d[key]=val
        d.setdefault('costoPatrimonio',rows[4][1])
        d.setdefault('criterio',rows[5][1])
        d.setdefault('pesoDcf',rows[37][1]);d.setdefault('pesoMultiplos',rows[38][1])
        d['resumenNativo']=summary
    d['integracionNativa']={**(before.get('descuentoMultiples') or {}).get('integracionNativa',{}),**d['integracionNativa']}
    v['descuentoMultiples']=d
    assert all(v[k]==before[k] for k in before.keys()-{'descuentoMultiples'})
    return v

if __name__=='__main__':
    root=Path(__file__).resolve().parent.parent
    for p in sorted((root/'evidencia/descuentos-20261031').glob('*-UNFORMATTED_VALUE.json')):
        if '-DCF-' in p.name:
            continue
        capture=json.loads(p.read_text())
        fp=p.with_name(p.name.replace('UNFORMATTED_VALUE','FORMULA'))
        vp=root/'valoraciones'/(capture['revisionId']+'.json')
        v=integrate(json.loads(vp.read_text()),capture,json.loads(fp.read_text()),hashlib.sha256(p.read_bytes()).hexdigest())
        vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
        print(v['ticker'],v['descuentoMultiples']['integracionNativa']['estado'])
