'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const near=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=Math.max(1e-8,Math.abs(b)*1e-9);
test('NU: 25 fórmulas DCF FCFE bancario y centro Ke/g reproducibles, sin múltiplos industriales',()=>{
  const v=read('valoraciones/NU-20261029-R1.json');
  const e=read('evidencia/nu-fcfe-bancario-20261031/NU-20261029-R1-sensibilidad-25-formulas.json');
  assert.equal(v.ticker,'NU');assert.equal(v.version_metodo,'A-1.2');
  assert.equal(v.revisionId,e.revisionId);assert.equal(v.sheet_id,e.sourceSheetId);
  assert.match(v.metodoPrincipal,/FCFE bancario/);
  assert.equal(v.estado,'EN_REVISION');
  assert.equal(e.kind,'EVIDENCIA_SOLO_LECTURA_FCFE_BANCARIO');
  assert.equal(e.status,'NO_ES_VALORACION_RELATIVA');
  assert.equal(e.range,"'Sensibilidad FCFE A'!A3:F12");
  assert.equal(e.baseLinkedFormula,"='FCFE bancario A'!B12");
  assert.equal(e.centerLinkedFormula,'=D8-B3');
  assert.ok(near(e.baseLinkedValue,v.valorPrincipal));
  assert.ok(near(e.centerDifference,0));
  assert.deepEqual(e.keValues,v.sensibilidadDCF.KeEscenarios);
  assert.deepEqual(e.gValues,v.sensibilidadDCF.gEscenarios);
  assert.ok(near(e.centralKe,v.sensibilidadDCF.Ke0));
  assert.equal(e.matriz.length,5);
  for(let r=0;r<5;r++){
    assert.equal(e.matriz[r].length,5);assert.equal(e.formulas[r].length,5);
    for(let c=0;c<5;c++){
      const f=e.formulas[r][c],value=e.matriz[r][c];
      assert.equal(typeof f,'string','Fórmula de origen requerida');
      assert.ok(f.startsWith('=') && f.includes("'FCFE bancario A'!G17") &&
        f.includes("'FCFE bancario A'!G26") && f.includes("'FCFE bancario A'!B5"),
        'Solo referencias del FCFE bancario, no flujos industriales');
      assert.ok(near(value,v.sensibilidadDCF.valorPorAccion[r][c]),
        'Valor distinto de la fotografía vigente en '+r+','+c);
      if(r>0) assert.ok(value<e.matriz[r-1][c],'Ke superior debe reducir VP');
      if(c>0) assert.ok(value>e.matriz[r][c-1],'Mayor crecimiento terminal debe aumentar VP');
    }
  }
  assert.ok(near(e.matriz[2][2],v.valorPrincipal));
  assert.ok(near(v.precioMOS,v.valorPrincipal*(1-v.mos)));
  const methods=v.metodos;
  assert.equal(methods.find(m=>m.nombre==='DCF FCFE bancario').peso,1);
  for(const name of ['P/E','P/FCFE','P/BV']){
    const m=methods.find(m=>m.nombre===name);
    assert.ok(m && m.peso===null && m.valorHoy===null);
  }
  for(const name of ['EV/EBITDA','EV/FCFF']){
    const m=methods.find(m=>m.nombre===name);
    assert.ok(m && m.peso===0);
  }
  assert.equal(v.descuentoMultiples.multiplesHoy,null);
  assert.equal(v.descuentoMultiples.ponderadoHoy,null);
});
