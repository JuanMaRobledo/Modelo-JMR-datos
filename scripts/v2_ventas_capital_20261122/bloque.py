"""Genera el bloque de anclas (mismo diseño que scripts/v2-libro-operativo.py) para pegar en Google Sheets (separador ';')."""
import json,sys
def bloque(sel):
    e=lambda k,c: "'JMR Estados'!%s%d"%(c,{'ingresos':6,'patrimonio':27,'minoritarios':28,'deuda':24,'arrend':25,'caja':19}[k])
    ic=lambda c:'(%s-%s+%s+%s-%s)'%(e('patrimonio',c),e('minoritarios',c),e('deuda',c),e('arrend',c),e('caja',c))
    m3='=IFERROR(IF((%s-%s)>0;(%s-%s)/(%s-%s);"NA");"NA")'%(ic('L'),ic('I'),e('ingresos','L'),e('ingresos','I'),ic('L'),ic('I'))
    A=[('Empresa actual',"='Input sheet'!I27",'Ingresos / capital invertido actual («look at your company\'s current number»).'),
       ('Empresa marginal (último año)',"='Input sheet'!I28",'Δingresos / Δcapital del último año.'),
       ('Empresa marginal (3 años)',m3,'Δingresos / Δcapital en tres años (JMR Estados L frente a I).'),
       ('Industria EE. UU. (promedio)',"='Input sheet'!J27",''),
       ('Industria global (promedio)',"='Input sheet'!K27",'Valor por defecto del Ginzu maestro (B31 = K27; B32 = B31).'),
       ('Global 1.er cuartil',"='Input sheet'!L27",''),('Global mediana',"='Input sheet'!M27",'Precedente NVIDIA 2023/24.'),
       ('Global 3.er cuartil',"='Input sheet'!N27",'Precedente MercadoLibre 2026.')]
    rows=[['ANCLAS DE VENTAS/CAPITAL (fórmulas del Ginzu de Damodaran; elegir una por escenario y tramo)','','','','','',''],
          ['Ancla','Origen','Valor','','','','Lectura (Damodaran)']]
    for n,f,l in A: rows.append([n,'Input I/J/K/L/M/N27' if 'Input' in f else 'JMR Estados',f,'','','',l])
    rows.append(['Manual (solo con relato documentado en G43)','Digitado','']+[sel[s].get('manual','') for s in ('conservador','base','optimista')]+[sel.get('relatoManual','')])
    rows.append(['','','','','','',''])
    rows.append(['Ancla elegida · años 1–5','','']+[sel[s]['1a5'] for s in ('conservador','base','optimista')]+[sel.get('relato','')])
    rows.append(['Ancla elegida · años 6–10','','']+[sel[s].get('6a10',sel[s]['1a5']) for s in ('conservador','base','optimista')]+[''])
    rows.append(['Factor sobre el ancla (1 = ancla pura)','','']+[sel[s].get('factor',1) for s in ('conservador','base','optimista')]+['Conserva la proporción de cada escenario frente al Base.'])
    rows.append(['Contrato V2, enmienda 22-nov-2026: el ventas/capital sale de estas anclas por fórmula; un valor manual exige relato.','','','','','',''])
    f12=[['=IF(%s45="Manual";%s43;INDEX($C$35:$C$42;MATCH(%s45;$A$35:$A$42;0)))*%s47'%(c,c,c,c) for c in 'DEF'],
         ['=IF(%s46="Manual";%s43;INDEX($C$35:$C$42;MATCH(%s46;$A$35:$A$42;0)))*%s47'%(c,c,c,c) for c in 'DEF']]
    return rows,f12
if __name__=='__main__':
    sel=json.loads(sys.argv[1]); r,f=bloque(sel); print(json.dumps({'rows':r,'f12':f},ensure_ascii=False))
