const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {validateRecord}=require('../auditar_integridad.cjs');
const read=name=>JSON.parse(fs.readFileSync(path.join(__dirname,'../../valoraciones',name),'utf8'));
test('acepta cálculo con advertencias económicas',()=>assert.doesNotThrow(()=>validateRecord(read('AAPL-1791720000000.json'))));
test('rechaza contar celdas N/D como matrices',()=>{const r=read('DUOL-1791409167000.json');r.sensibilidadMultiples.noDisponibles=255;assert.throws(()=>validateRecord(r),/Contador N\/D/);});
test('rechaza MOS sobre el ponderado',()=>{const r=read('SHAK-1790595627129.json');r.precioMOS=r.valorPresentePonderado.base*(1-r.mos);assert.throws(()=>validateRecord(r),/MOS diferente/);});
test('rechaza cifras ausentes aunque el texto diga OK',()=>{const r=read('AAPL-1791720000000.json');r.descuentoMultiples.metodos[0].base.vp[2]=null;assert.throws(()=>validateRecord(r),/sin cifras/);});
test('SOTP no depende de la aprobación del DCF opcional',()=>assert.doesNotThrow(()=>validateRecord(read('GRUPOARGOS-1791805502454.json'))));
