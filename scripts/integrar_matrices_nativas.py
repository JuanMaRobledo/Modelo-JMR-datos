"""Integra solo matrices verificadas, EN_REVISION; no publica ni calcula.

Entradas: registro oficial, copia candidata del motor #181, foto completa
de sus rangos y celdas con fórmulas de A76:I144. La salida debe ser distinta.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

CORE = ('EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF')
METHODS = CORE + ('P/V', 'P/BV')
REQUIRED = {'stories','growth_base','growth_cons','growth_disr','growth_opt',
 'valuation_base','valuation_cons','valuation_opt','valuation_disr','input',
 'wacc','wacc_regions','rd','options','summary','multiples_discount',
 'multiples_ps','multiples_pbv','fm','sens_dcf','sens_mult','trailing',
 'is','bs','cf','audit_internal'} | {'mult_'+t for t in ('EVEBITDA','EVFCFF','PE','PFCFE','POCF')}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def negative_flow_na(official, method):
    """N/A económico únicamente para FCFF/FCFE FY+3 negativos, sin peso.

    La fuente puede conservar N/D; NO se convierten celdas vacías a ceros
    ni se infieren resultados de múltiplos sin ancla.
    """
    if method not in ('EV/FCFF', 'P/FCFE'):
        return False
    selected = next((x for x in official.get('descuentoMultiples',{}).get('metodos',[])
                     if x.get('nombre') == method), None)
    if not selected or selected.get('peso') != 0:
        return False
    if not str(selected.get('estado','')).startswith('N/A: flujo negativo'):
        return False
    base = selected.get('base',{})
    fy, vp = base.get('fy'), base.get('vp')
    return (isinstance(fy,list) and len(fy)>=3 and isinstance(vp,list) and len(vp)>=3
            and type(fy[2]) in (int,float) and fy[2]<0
            and type(vp[2]) in (int,float) and vp[2]<0)

def integrate(official, candidate, snapshot, cells):
    require(official.get('estado') == 'EN_REVISION', 'Solo EN_REVISION')
    require(official.get('version_metodo') == 'A-1.2' and official.get('metodo_valoracion') == 'A', 'Solo Método A-1.2')
    require(official.get('ticker') != 'NU', 'Banca requiere contrato propio')
    require(not official.get('sensibilidadMultiples',{}).get('matrices'), 'No sobrescribir matrices existentes')
    before = copy.deepcopy(official); after = copy.deepcopy(candidate)
    before.pop('sensibilidadMultiples',None); after.pop('sensibilidadMultiples',None)
    require(before == after, 'El candidato modifica campos ajenos a matrices')
    s = candidate.get('sensibilidadMultiples',{})
    require(s.get('contrato') == 'base-native-five-priority-v1' and s.get('estadoPublicacion') == 'CANDIDATO_NO_PUBLICADO', 'Solo candidato nativo del motor')
    require(snapshot.get('revision_id') == official.get('revisionId') == s.get('revisionId'), 'Revisión divergente')
    require(snapshot.get('sheet_id') == official.get('sheet_id') == s.get('sourceSheetId') == cells.get('spreadsheetId'), 'Hoja divergente')
    data = snapshot.get('data',{})
    require(set(data) == REQUIRED, 'Foto sin todos los rangos del extractor')
    digest = hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True,default=str).encode()).hexdigest()
    require(digest == snapshot.get('data_sha256') == s.get('resultadosSha256'), 'SHA256 divergente')
    blocks = [d for tab in cells.get('sheets',[]) if tab['properties']['title']=='Sensibilidad por múltiplo' for d in tab.get('data',[]) if d.get('startRow',0)==75 and d.get('startColumn',0)==0]
    require(len(blocks)==1, 'Falta bloque de fórmulas A76:I144')
    rows = blocks[0].get('rowData',[])
    def cell(row,col):
        line = rows[row-76].get('values',[]) if row-76<len(rows) else []
        return line[col-1] if col<=len(line) else {}
    def value(c):
        e=c.get('effectiveValue',{})
        for k in ('numberValue','stringValue','boolValue'):
            if k in e:return e[k]
        return ''
    def snap(row,col):
        line=data['sens_mult'][row-1]
        return line[col-1] if col<=len(line) else ''
    matrices=s.get('matrices',[])
    require([m.get('metodo') for m in matrices]==list(METHODS), 'Siete métodos sin duplicados y en orden')
    for i,m in enumerate(matrices):
        start=76+10*i; name=METHODS[i]
        require(m.get('origen')==f"'Sensibilidad por múltiplo'!A{start}:I{start+8}", 'Origen divergente')
        require(m.get('escenario')=='base' and m.get('ancla')=='JMR', 'Historia o ancla divergente')
        require(str(snap(start,1)).startswith('BASE · '+name+' ·'), 'Encabezado divergente')
        # Contraste de TODAS las celdas con la foto, no solamente el centro.
        for row in range(start,start+9):
            for col in range(1,10):
                require(value(cell(row,col))==snap(row,col), 'Fórmulas y fotografía de valores divergentes')
        require(m.get('estado')==snap(start+8,9), 'Estado divergente')
        if m['estado']=='OK':
            grid=[[snap(r,c) for c in range(2,7)] for r in range(start+3,start+8)]
            xs=[snap(start+2,c) for c in range(2,7)];ys=[snap(r,1) for r in range(start+3,start+8)]
            require(m.get('matriz')==grid and m.get('fundamentalFY3')==xs and m.get('multiploElegido')==ys, 'Matriz o ejes divergentes')
            nums=xs+ys+[v for row in grid for v in row]
            require(all(type(v) in (int,float) and abs(v)<float('inf') for v in nums), 'Valores no finitos')
            require(m.get('centro')==m.get('vp3Original')==grid[2][2]==snap(start+8,7)==snap(start+8,8), 'Centro FY+3 divergente')
            require(all(cell(r,c).get('userEnteredValue',{}).get('formulaValue') for r in range(start+3,start+8) for c in range(2,7)), 'Matriz sin fórmulas nativas')
        else:
            require(m['estado']=='N/D' and m.get('matriz') is None, 'Solo N/D sin matriz puede ser excepción')
            chosen=next((x for x in official.get('descuentoMultiples',{}).get('metodos',[]) if x.get('nombre')==name),{})
            require(chosen.get('peso',0)==0, 'N/D con peso positivo')
            if name in CORE:
                require(negative_flow_na(official,name), 'N/D prioritario: no existe justificación financiera verificable de N/A')
    result=copy.deepcopy(candidate)
    # La hoja conserva el estado literal N/D. Únicamente el expediente
    # expresa N/A económico, con causa comprobada en la misma revisión.
    for m in result['sensibilidadMultiples']['matrices']:
        if m['estado']=='N/D' and negative_flow_na(official,m['metodo']):
            m['estado']='N/A'
            m['estadoFuente']='N/D'
            m['motivo']='Flujo proyectado FY+3 y VP3 negativos en esta revisión; el múltiplo no representa un precio económico interpretable. Método sin ponderación (peso cero). La hoja original permanece N/D.'
    result['sensibilidadMultiples'].update(estadoPublicacion='INTEGRADO_EN_REVISION',controlesTecnicosAprobados=True,
        certificado=False,nota='Integración técnica de matrices OK: celdas, ejes, fórmulas, origen y centro FY+3 contrastados con foto SHA256. N/D solo puede convertirse a N/A por flujos negativos acreditados, sin alterar la hoja. Pendiente revisión visual y auditoría económica independiente.')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('oficial','candidato','foto','formulas','salida'):p.add_argument('--'+key,required=True,type=Path)
    a=p.parse_args()
    require(a.salida.resolve() not in [x.resolve() for x in (a.oficial,a.candidato,a.foto,a.formulas)], 'Salida debe ser distinta de entradas')
    require(not a.salida.exists(), 'Salida ya existe')
    result=integrate(*[json.loads(x.read_text()) for x in (a.oficial,a.candidato,a.foto,a.formulas)])
    a.salida.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
