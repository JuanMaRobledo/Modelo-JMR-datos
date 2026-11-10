'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'../..');const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const x=read('candidatos/valoraciones/NVDA-20261031-A12-R1/CALIBRACION_DCF_PROVISIONAL.json');
const work=read('candidatos/valoraciones/NVDA-20261031-A12-R1/workspace.json');const c=read('catalogo.json');
const close=(a,b,tol=1e-7)=>assert.ok(Math.abs(a-b)<=tol, `${a} != ${b}`);
test('NVDA no mezcla LTM, unidades, fechas ni revisiones',()=>{
assert.equal(x.status,'CALIBRACION_INDEPENDIENTE_NO_PUBLICAR');
assert.equal(x.accountingCut,'2026-07-26');assert.equal(x.asOf,'2026-10-31');
assert.equal(x.inputs.revenueLTM,302970);assert.equal(x.inputs.sharesMillions,24268);
assert.equal(x.inputs.debtBook,1000+32366+509+4985);
assert.equal(work.valorPrincipal,null);assert.equal(work.publicationStatus,'NO_PUBLICAR');
assert.ok(!c.valoraciones.some(p=>p.includes(x.revision)));
});
test('NVDA cuatro DCF de diez años y puentes NOPAT/FCFF/EV/equity conciliados',()=>{
assert.equal(x.scenarios.length,4);close(x.scenarios.reduce((v,s)=>v+s.probability,0),1);
for(const s of x.scenarios){
 const r=s.result,a=x.inputs;assert.equal(r.projection.length,10);
 for(const t of r.projection){close(t.fcff,t.nopat-t.reinvestment);close(t.presentValue,t.fcff*t.discountFactor);}
 close(r.pvExplicit,r.projection.reduce((t,v)=>t+v.presentValue,0));
 close(r.terminal.value,r.terminal.fcff/(r.terminal.discountRate-r.terminal.growth));
 close(r.enterpriseValue,r.pvExplicit+r.terminal.pv);
 close(r.equityValue,r.enterpriseValue-a.debtBook+a.cashAndMarketableSecurities+a.nonOperatingBookProxy-a.optionsProxy);
 close(r.perShare,r.equityValue/a.sharesMillions);close(r.mos35,r.perShare*.65);
 assert.ok(r.terminal.roic>r.terminal.growth);
}
});
test('Dos sensibilidades 5x5 conservan el centro de NVDA Base sin aprobar múltiplos',()=>{
const base=x.scenarios[0].result.perShare;
for(const matrix of Object.values(x.sensitivity)){
 assert.equal(matrix.values.length,5);assert.equal(matrix.rows.length,5);assert.equal(matrix.columns.length,5);
 for(const row of matrix.values){assert.equal(row.length,5);assert.ok(row.every(Number.isFinite));}
 close(matrix.values[2][2],base);close(matrix.center,base);
}
assert.equal(x.controls.officialMultiplesSensitivities,false);
assert.equal(x.controls.economicAudit,false);
assert.equal(x.controls.officialScenarioGates,'PENDIENTE');
});
test('NVDA no mezcla valoración nueva con antigua ni Disrupción en ponderado',()=>{
const three=x.scenarios.filter(v=>v.name!=='Disrupción');close(three.reduce((a,v)=>a+v.probability,0),.9);
close(x.expectedValueThree,three.reduce((a,v)=>a+v.probability*v.result.perShare,0)/.9);
assert.ok(x.caveats.some(v=>v.includes('17-nov')));
});
