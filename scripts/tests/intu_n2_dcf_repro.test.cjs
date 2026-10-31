'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const near=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=Math.max(1e-5,Math.abs(b)*1e-8);
test('INTU Nivel 2: cinco años DCF reproducibles sin tocar el cálculo ni las matrices exploratorias',()=>{
const rev='INTU-20261029-R1';
const v=read('valoraciones/'+rev+'.json');
const a=read('analisis/INTU-research-'+rev+'.json');
const before=read('evidencia/intu-dcf-20261031/'+rev+'-analisis_antes.json');
const e=read('evidencia/intu-dcf-20261031/'+rev+'-cinco-anios-formulas.json');
assert.equal(e.kind,'EVIDENCIA_DCF_INTU_SOLO_LECTURA_NO_PUBLICADA');
assert.equal(v.revisionId,rev);assert.equal(a.revisionId,rev);
assert.equal(e.sourceSheetId,v.sheet_id);
assert.equal(v.estado,'EN_REVISION');assert.equal(a.estado,'EN_REVISION');
assert.deepEqual(a.articleHtml,before.articleHtml);
assert.deepEqual(
 Object.fromEntries(Object.entries(a).filter(([k])=>!['html','calculationHtml'].includes(k))),
 Object.fromEntries(Object.entries(before).filter(([k])=>!['html','calculationHtml'].includes(k))));
assert.equal(a.html,a.articleHtml+a.calculationHtml);
assert.equal((a.calculationHtml.match(/id="jmr-n2-intu-dcf-repro-20261031"/g)||[]).length,1);
assert.ok(a.calculationHtml.includes('matrices Base nativas'));
const grid=e.gridValues,formula=e.gridFormulas,bridge=e.bridgeValues;
assert.equal(grid.length,12);assert.equal(formula.length,11);
for(let c=2;c<=6;c++){
 const revenue=grid[1][c],prior=c===2?21448:grid[1][c-1],s2c=grid[7][c];
 const nopat=grid[6][c],reinvest=grid[8][c],fcff=grid[9][c],pv=grid[11][c];
 assert.ok(near((revenue-prior)/s2c,reinvest));
 assert.ok(near(nopat-reinvest,fcff));
 assert.ok(near(fcff*grid[10][c],pv));
 for(const j of [0,3,4,5,6,7,8,9,10])assert.match(formula[j][c-2],/^=/);
}
assert.ok(near(bridge[6][3],bridge[0][3]+bridge[5][3]));
assert.ok(near(bridge[7][3],bridge[6][3]-469));
assert.ok(near(bridge[8][3],v.valorPrincipal));
assert.ok(near(e.originalDcf,v.valorPrincipal));
assert.equal(e.originalMos,v.precioMOS);
assert.ok(near(bridge[10][3],bridge[5][3]/bridge[6][3]));
// En la revisión INTU A-1.2 no hay bloque de descuento relativo
// certificado. No crear ni simular un 0: mantener métodos pendientes.
assert.equal(v.descuentoMultiples,undefined);
assert.equal(v.metodos.find(m=>m.nombre==='DCF Damodaran').peso,1);
assert.ok(v.metodos.filter(m=>m.nombre!=='DCF Damodaran').length>=5);
for(const m of v.metodos.filter(m=>m.nombre!=='DCF Damodaran')){
 assert.equal(m.estado,'PENDIENTE_MULTIPLOS_NATIVOS');
 assert.equal(m.peso,null);
 assert.equal(m.valorHoy,null);
}
assert.ok(!v.sensibilidadMultiples?.matrices?.length);
});
