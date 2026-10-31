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

def verify_recaptura(record,analysis):
    """Registros regenerados por recaptura (campo evidenciaRecaptura): la evidencia de múltiplos de la revisión anterior ya no aplica.
    Se verifica la evidencia propia de la recaptura (foto de la hoja, hashes, estado) y la coherencia interna de los valores
    descontados y ponderados del registro. No repite la reproducción año a año del cierre de múltiplos."""
    ev=ROOT/record['evidenciaRecaptura']
    rec=json.loads((ev/'recaptura.json').read_text()); man=json.loads((ev/'manifiesto_candidato.json').read_text())
    revision=record['revisionId']
    assert revision==rec['revision_id']==analysis['revisionId']==analysis['valoracionRevisionId']==record['auditoria']['revisionId']
    assert record['resultsSha256']==rec['foto_despues']['data_sha256']==man['resultados_sha256']
    assert record['publicationStatus']=='PUBLICADA' and rec['estado']=='PUBLICADA_CON_SALVEDADES'
    for path,h in man['artifacts'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h['sha256'],path
    d=record['descuentoMultiples']
    assert [m['nombre'] for m in d['metodos']]==METHODS
    for sc in SCENARIOS:
        for m in d['metodos']:
            x=m[sc]
            assert len(x['vp'])==len(x['fy'])==3 and all(math.isfinite(a) for a in x['vp']+x['fy'])
            assert equal(x['consolidado'],x['vp'][-1] if d['criterio']=='Solo 3 años' else sum(x['vp'])/3)
        tot=sum(m['peso']*m[sc]['consolidado'] for m in d['metodos'])
        esperado=tot+(d.get('pesoDcf') or 0)*d['dcfHoy'][sc]
        assert equal(record['valorPresentePonderado'][sc],esperado)
    for key in ('linkedValuation','linkedValuationAtResearch'):
        assert analysis[key]['revisionId']==revision
        assert analysis[key]['descuentoMultiples']==record['descuentoMultiples']
    return {'ticker':record['ticker'],'revisionId':revision,'recaptura':True,'dcfBase':record['valorPrincipal'],
            'scope':'Recaptura: evidencia propia, hashes y coherencia interna de descuentos y ponderados; no reproduce año a año el cierre de múltiplos','ok':True}


def verify_a_native(record):
    """Método A: verificar cuadrículas nativas Base y descuentos del mismo registro.

    Esta comprobación complementa (no reemplaza) el gate obligatorio
    validateNativeMatrices del catálogo y no depende del esquema legacy
    'cierreMultiplos'. Solo lee y coteja revisiones publicadas.
    """
    rev=record['revisionId']
    sens=record.get('sensibilidadMultiples') or {}
    assert sens.get('contrato')=='base-native-five-priority-v1',rev
    assert sens.get('revisionId')==rev
    assert sens.get('estadoPublicacion')=='INTEGRADO_EN_REVISION'
    assert sens.get('controlesTecnicosAprobados') is True
    methods=('EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF')
    matrices={v['metodo']:v for v in sens.get('matrices') or []}
    for name in methods:
        m=matrices[name]
        assert m['estado'] in ('OK','N/A'),(rev,name,m['estado'])
        if m['estado']=='OK':
            grid=m['matriz']
            assert len(grid)==5 and all(len(row)==5 and all(isinstance(x,(int,float)) and math.isfinite(x) for x in row) for row in grid)
            assert equal(grid[2][2],m['centro'])
            assert equal(m['centro'],m['vp3Original'])
            disc=next(x for x in record['descuentoMultiples']['metodos'] if x['nombre']==name)
            assert equal(disc['base']['vp'][2],m['vp3Original'])
        else:
            assert m['matriz'] is None and len(m.get('motivo',''))>=20
    return {'ticker':record['ticker'],'revisionId':rev,'contract':'A-1.2-BASE-NATIVE',
            'matrices':len(matrices),'verifiedRequired':len(methods),'ok':True,
            'scope':'Base 5x5 y VP3; NO auditoría económica'}

def verify(ticker):
    record=json.loads(next((ROOT/'valoraciones').glob(ticker+'*.json')).read_text())
    analysis=json.loads(next((ROOT/'analisis').glob(ticker+'*.json')).read_text())
    if record.get('evidenciaRecaptura'):
        return verify_recaptura(record,analysis)
    if record.get('version_metodo')=='A-1.2' and not record.get('cierreMultiplos'):
        return verify_a_native(record)
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

