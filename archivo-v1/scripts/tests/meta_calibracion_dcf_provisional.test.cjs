'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const path=require('node:path'),fs=require('node:fs');
const root=path.resolve(__dirname,'../..');
const read=x=>JSON.parse(fs.readFileSync(path.join(root,x),'utf8'));
const x=read('candidatos/valoraciones/META-20261031-A12-R1/CALIBRACION_DCF_PROVISIONAL.json');
const ws=read('candidatos/valoraciones/META-20261031-A12-R1/workspace.json');
const c=read('catalogo.json');
function close(a,b,tol=1e-7){assert.ok(Math.abs(a-b)<=tol, `${a} no concilia con ${b}`);}
test('META cuatro DCF reproducibles, sin mezclar unidades ni publicar',()=>{
 assert.equal(x.status,'CALIBRACION_INDEPENDIENTE_NO_PUBLICAR');
 assert.equal(x.units,'USD millones excepto precios por acción');
 assert.equal(x.scenarios.length,4);
 assert.equal(x.assumptions.sharesMillions,2556.241253);
 assert.equal(ws.valorPrincipal,null);assert.equal(ws.precioMOS,null);
 assert.ok(!c.valoraciones.some(p=>p.includes(x.revision)));
 assert.equal(ws.publicationStatus,'NO_PUBLICAR');
 close(x.scenarios.reduce((a,v)=>a+v.probability,0),1);
});
test('FCFF, valor presente y deuda/equity concilian para todos los escenarios',()=>{
 for(const s of x.scenarios){
   const r=s.scenario,p=r.projection,a=x.assumptions;
   assert.equal(p.length,10);
   for(let i=0;i<p.length;i++){
     close(p[i].fcff,p[i].nopat-p[i].reinvestment);
     close(p[i].presentValue,p[i].fcff*p[i].discountFactor);
     assert.ok(p[i].revenue>0);
     if(i>0)close(p[i].revenue,p[i-1].revenue*(1+p[i].revenueGrowth));
   }
   close(r.pvExplicit,p.reduce((t,v)=>t+v.presentValue,0));
   close(r.enterpriseValue,r.pvExplicit+r.terminal.presentValue);
   close(r.terminal.value,r.terminal.fcff/(r.terminal.wacc-r.terminal.growth));
   close(r.equityValue,r.enterpriseValue-a.debtMillions+a.cashMillions+a.nonOperatingAssetsBookProxy-a.legalClaimUpperBound-a.optionLiabilityProxy);
   close(r.perShare,r.equityValue/a.sharesMillions);
   close(r.MOS35,r.perShare*.65);
   assert.ok(r.terminal.wacc>r.terminal.growth);
   assert.ok(r.terminal.roic>r.terminal.growth);
 }
});
test('Centro Base de dos matrices 5x5 concilia y no sustituye sensibilidades de múltiples',()=>{
 const b=x.scenarios.find(y=>y.name==='Base').scenario.perShare;
 for(const matrix of Object.values(x.sensitivity)){
   assert.equal(matrix.rows.length,5);assert.equal(matrix.columns.length,5);
   assert.equal(matrix.values.length,5);
   for(const row of matrix.values){assert.equal(row.length,5);assert.ok(row.every(Number.isFinite));}
   close(matrix.values[2][2],b);close(matrix.center,b);
 }
 assert.equal(x.controls.multiplesSensitivitiesCertified,false);
 assert.equal(x.controls.DCFOutputGoogleSheetCertified,false);
 assert.equal(x.controls.reviewGateK5,'PENDIENTE');
});
test('Probabilidades excluyen Disrupción y referencia precio no es valor intrínseco',()=>{
 const three=x.scenarios.filter(z=>z.name!=='Disrupción');
 const den=three.reduce((t,z)=>t+z.probability,0);
 close(den,.9);
 close(x.expectedThreeNoDisruption,three.reduce((t,z)=>t+z.probability*z.scenario.perShare,0)/den);
 assert.equal(x.assumptions.marketPrice,614.99);
 assert.equal(x.assumptions.marketPriceDate,'2026-10-30');
 assert.ok(Math.abs(x.expectedThreeNoDisruption-x.assumptions.marketPrice)>1);
});
