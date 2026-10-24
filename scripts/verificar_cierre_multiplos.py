"""Comprueba la evidencia de los siete múltiplos y sus tres piezas publicables.

Solo lectura; no sustituye controles_todas.sh ni certifica hipótesis del DCF.
Uso: python scripts/verificar_cierre_multiplos.py
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHODS = ['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV']
SCENARIOS = ['conservador','base','optimista']

def equal(a,b):
    return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isfinite(a) and math.isfinite(b) and abs(a-b)<=max(1e-6,abs(b)*1e-8)

def verify(ticker):
    record=json.loads(next((ROOT/'valoraciones').glob(ticker+'*.json')).read_text())
    analysis=json.loads(next((ROOT/'analisis').glob(ticker+'*.json')).read_text())
    evidence=json.loads((ROOT/record['cierreMultiplos']['evidencePath']).read_text())
    audit=(ROOT/'auditorias/narrativas'/f'{ticker}.md').read_text()
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
