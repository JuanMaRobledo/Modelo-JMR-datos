'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const src='evidencia/banca/NU-20261029-R1-sensibilidad-fcfe-nativa.json';
const val='valoraciones/NU-20261029-R1.json';
const near=(a,b)=>typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<=1e-7;

function valueAt(e,k,g){
 const b=e.base;
 const pv=b.fcfeTenYearMillions.reduce((s,x,i)=>s+x/(1+k)**(i+1),0);
 const keT=b.keTerminal+k-b.keCentral;
 const terminal=b.niTerminalMillions*(1+g)*(1-g/b.roeTerminal)/(keT-g)/(1+k)**10;
 return (pv+terminal)/b.sharesMillions;
}
function verify(e,v){
 assert.equal(e.ticker,'NU');
 assert.equal(v.ticker,e.ticker);
 assert.equal(e.revisionId,v.revisionId);
 assert.equal(e.sourceSheetId,v.sheet_id);
 assert.equal(e.kind,'EVIDENCIA_SENSIBILIDAD_FCFE_BANCARIA_NO_PUBLICADA');
 assert.match(e.method,/NO FCFF industrial/);
 assert.equal(v.estado,'EN_REVISION');
 assert.equal(e.checks.originalValuationModified,false);
 assert.equal(e.checks.bankMultiplesCertified,false);
 assert.equal(e.checks.economicAuditPerformed,false);
 assert.equal(e.checks.formulas,25);
 assert.equal(e.checks.independentCellsReconciled,25);
 assert.equal(e.keInicial.length,5);assert.equal(e.crecimientoTerminal.length,5);
 assert.equal(e.matrix.length,5);assert.equal(e.formulas.length,5);
 assert.equal(e.base.fcfeTenYearMillions.length,10);
 assert.ok(near(e.base.valorPorAccion,v.valorPrincipal));
 assert.ok(near(e.base.valorPorAccion,e.matrix[2][2]));
 assert.ok(near(e.base.keCentral,e.keInicial[2]));
 assert.ok(near(e.base.gTerminal,e.crecimientoTerminal[2]));
 assert.ok(e.base.roeTerminal>e.base.gTerminal);
 let count=0;
 for(let i=0;i<5;i++){
   assert.equal(e.matrix[i].length,5);assert.equal(e.formulas[i].length,5);
   for(let j=0;j<5;j++){
     const k=e.keInicial[i],g=e.crecimientoTerminal[j];
     assert.ok(e.base.keTerminal+k-e.base.keCentral>g,'Ke terminal <= g');
     assert.ok(near(valueAt(e,k,g),e.matrix[i][j]),'NU: matriz independiente difiere '+i+'/'+j);
     assert.ok(e.formulas[i][j].startsWith('=('),'No se conserva fórmula original');
     assert.ok(e.formulas[i][j].includes("'FCFE bancario A'!G17"));
     assert.ok(e.formulas[i][j].includes("'FCFE bancario A'!B5"));
     count++;
   }
 }
 assert.equal(count,25);
}
test('NU: Ke×g FCFE bancario concilia 25 fórmulas y DCF sin crear múltiplos industriales',()=>{
 const e=read(src),v=read(val);
 verify(e,v);
 assert.equal(v.sensibilidadMultiples?.matrices?.length||0,0,'No publicar matrices relativas pendientes');
});
test('NU: centro o valor alterado NO supera control',()=>{
 const e=read(src),v=read(val);
 for(const mutate of [x=>x.matrix[2][2]+=1,x=>x.base.roeTerminal=.035,x=>x.base.sharesMillions*=2]){
  const d=JSON.parse(JSON.stringify(e));mutate(d);
  assert.throws(()=>verify(d,v));
 }
});
module.exports={verify};