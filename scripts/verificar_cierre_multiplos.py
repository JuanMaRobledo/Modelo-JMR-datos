"""Comprueba la evidencia de los siete múltiplos y sus tres piezas publicables.

Solo lectura; no sustituye controles_todas.sh ni certifica hipótesis del DCF.
Uso: python scripts/verificar_cierre_multiplos.py
"""
import json
import math
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHODS = ['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV']
SCENARIOS = ['conservador','base','optimista']

def equal(a,b):
    return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isfinite(a) and math.isfinite(b) and abs(a-b)<=max(1e-6,abs(b)*1e-8)

def verify_snapshot_release(record, analysis, evidence, audit):
    """Check reviewed snapshots without assuming the legacy FY+3-only convention.

    Source hashes, original seven outputs, discount dates and linked documents
    remain mandatory. This contract supports both existing consolidation modes.
    It does not approve economic assumptions or replace the valuation audit.
    """
    source=(ROOT/evidence['sourcePath']).resolve()
    assert source.is_relative_to(ROOT.resolve()) and source.is_file()
    raw=source.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==evidence['sourceSha256']
    snap=json.loads(raw)
    revision=record['revisionId']
    assert revision==analysis['revisionId']==analysis['valoracionRevisionId']==evidence['revisionId']==snap['revision_id']
    assert revision==record['auditoria']['revisionId'] and revision in audit
    assert snap['sheet_id']==evidence['sourceSheetId']
    assert snap['sheet_id'] in record['hojaGoogle']
    data_hash=hashlib.sha256(json.dumps(snap['data'],ensure_ascii=False,sort_keys=True,default=str).encode()).hexdigest()
    assert data_hash==snap['data_sha256']==evidence['resultadosSha256']==record['resultsSnapshotSha256']==analysis['resultsSnapshotSha256']
    d=snap['data'];dm=record['descuentoMultiples']
    criterion=d['multiples_discount'][2][1]
    assert criterion==evidence['criterion']==dm['criterio']
    assert criterion in ('Solo 3 años','Promedio 1-3 años')
    assert equal(record['valorPrincipal'],d['stories'][1][7])
    assert equal(record['valorEsperado']['valor'],d['stories'][6][7])
    assert [m['method'] for m in evidence['methods']]==METHODS
    assert equal(sum(m['weightRelative'] for m in evidence['methods']),1)
    tabs=['mult_EVEBITDA','mult_EVFCFF','mult_PE','mult_PFCFE','mult_POCF','multiples_ps','multiples_pbv']
    count=0;ke=d['multiples_discount'][1][1]
    for i,method in enumerate(evidence['methods']):
        block=d[tabs[i]]
        target=next(m for m in record['metodos'] if m['nombre']==METHODS[i])
        discounted=next(m for m in dm['metodos'] if m['nombre']==METHODS[i])
        for s,scenario in enumerate(SCENARIOS):
            row=7+11*s
            assert equal(method['inputs'][s],block[row][9])
            assert all(equal(v,method['inputs'][s]) for v in block[row][5:8])
            prices=block[row+2][5:8];dividends=block[row+3][5:8]
            assert len(prices)==len(dividends)==3
            present=[]
            for year,price in enumerate(prices):
                calc=price/(1+ke)**(year+1)+sum((dividends[t]-(dividends[t-1] if t else 0))/(1+ke)**(t+1) for t in range(year+1))
                present.append(calc)
                assert equal(calc,discounted[scenario]['vp'][year])
                assert equal(price+dividends[year],discounted[scenario]['fy'][year])
                count+=1
            assert equal(target[scenario],prices[-1]+dividends[-1])
            expected=present[-1] if criterion=='Solo 3 años' else sum(present)/3
            assert equal(expected,discounted[scenario]['consolidado'])
    for key in ('linkedValuation','linkedValuationAtResearch'):
        assert analysis[key]['revisionId']==revision
        assert analysis[key]['metodos']==record['metodos']
        assert analysis[key]['descuentoMultiples']==record['descuentoMultiples']
    assert analysis['html']==analysis['articleHtml'] and len(analysis['articleHtml'])>50000
    return {'ticker':record['ticker'],'revisionId':revision,'methods':7,'scenarios':21,
            'pricesAndDiscountsReplayed':count,'criterion':criterion,'dcfBase':record['valorPrincipal'],'ok':True}

def verify(ticker):
    record=json.loads(next((ROOT/'valoraciones').glob(ticker+'*.json')).read_text())
    analysis=json.loads(next((ROOT/'analisis').glob(ticker+'*.json')).read_text())
    evidence=json.loads((ROOT/record['cierreMultiplos']['evidencePath']).read_text())
    audit=(ROOT/'auditorias/narrativas'/f'{ticker}.md').read_text()
    if evidence.get('schema')=='jmr-reviewed-snapshot-release-v1':
        return verify_snapshot_release(record,analysis,evidence,audit)
    revision=record['revisionId']
    assert revision==analysis['revisionId']==analysis['valoracionRevisionId']==evidence['revisionId']==record['auditoria']['revisionId']
    assert revision in audit.split('## Auditoría anterior')[0]
    assert equal(record['valorEsperado']['dcfBase'],evidence['dcfBase'])
    assert equal(sum(m['weightRelative'] for m in evidence['methods']),1)
    assert [m['method'] for m in evidence['methods']]==METHODS
    count=0
    for i,method in enumerate(evidence['methods']):
        target=next(m for m in record['metodos'] if m['nombre']==method['method'])
        discounted=next(m for m in record['descuentoMultiples']['metodos'] if m['nombre']==method['method'])
        for s,scenario in enumerate(SCENARIOS):
            proof=method['scenarios'][scenario]
            assert proof['input']>0
            assert proof['inputFormula']==f"='Financials Multiples'!${'BCD'[s]}${162+i}"
            assert all(equal(m,proof['input']) for m in proof['applied'])
            assert len(proof['prices'])==len(proof['cumulativeDividends'])==len(proof['present'])==3
            for year,price in enumerate(proof['prices']):
                dividends=proof['cumulativeDividends']
                calculated=price/(1+evidence['ke'])**(year+1)
                calculated+=sum((dividends[t]-(dividends[t-1] if t else 0))/(1+evidence['ke'])**(t+1) for t in range(year+1))
                assert equal(calculated,proof['present'][year])
                assert equal(price+dividends[year],proof['targetWithDividends'][year])
                assert equal(calculated,discounted[scenario]['vp'][year])
                if i>=2:
                    assert equal(price,proof['input']*proof['metric'][year]/proof['shares'][year])
                count+=1
            assert equal(target[scenario],proof['targetWithDividends'][-1])
            assert equal(discounted[scenario]['consolidado'],proof['consolidated'])
            assert equal(proof['consolidated'],proof['present'][-1])
    for link in ['linkedValuation','linkedValuationAtResearch']:
        assert analysis[link]['revisionId']==revision
        assert analysis[link]['metodos']==record['metodos']
        assert analysis[link]['descuentoMultiples']==record['descuentoMultiples']
    assert len(analysis['articleHtml'])>50000, 'No sustituir artículo completo por resumen'
    assert analysis['html']==analysis['articleHtml']
    return {'ticker':ticker,'revisionId':revision,'methods':7,'scenarios':21,'pricesAndDiscountsReplayed':count,'dcfBase':evidence['dcfBase'],'scope':'Múltiplos y consistencia de entrega; no certificación DCF integral','ok':True}

if __name__=='__main__':
    print(json.dumps([verify(ticker) for ticker in ['NKE','NFLX','META']],ensure_ascii=False,indent=2))

